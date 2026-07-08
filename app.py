"""
TWY Docs — Flask application.
Serves a single directory of markdown documentation with session-based auth.

Configure via environment variables:
    DOCS_DIR        Path to the markdown docs directory (default: docs/user-guide)
    SITE_TITLE      Display name shown in sidebar and page titles (default: TWY Docs)
    TWY_DOCS_PORT   Port to listen on (default: 5005)
"""
import hashlib
import hmac
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from twy_paths import load_env

load_env()

import markdown
from flask import Flask, render_template, abort, request, jsonify

from auth import auth_bp, login_required

BASE_DIR = Path(__file__).parent
DOCS_DIR = Path(os.getenv("DOCS_DIR", BASE_DIR / "docs" / "user-guide")).resolve()
SITE_TITLE = os.getenv("SITE_TITLE", "TWY Docs")
PORT = int(os.getenv("TWY_DOCS_PORT", 5005))

md = markdown.Markdown(extensions=[
    "fenced_code",
    "codehilite",
    "tables",
    "toc",
    "sane_lists",
], extension_configs={
    "codehilite": {"css_class": "highlight", "guess_lang": False},
    "toc": {"permalink": True},
})


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

def _title_from_md(path: Path) -> str:
    """Extract the first H1 from a markdown file, or derive from filename."""
    try:
        for line in path.read_text().splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return path.stem.replace("-", " ").title()


def build_nav():
    """Build sidebar: top-level .md files, immediate-subdir .md files, and index.md at any depth.

    - Top-level .md files (excluding homepage indexes) become entries.
    - Files in immediate subdirectories appear as entries (e.g., mailchimp/tags.md).
    - index.md and _index.md at any depth represent their section.
    - Non-index pages deeper than depth-1 are NOT shown (they\'re drilled into from a section page).
    """
    pages = []
    seen = set()

    def add(slug, title):
        if slug in seen:
            return
        seen.add(slug)
        pages.append({"slug": slug, "title": title})

    # Top-level .md files
    for md_file in sorted(DOCS_DIR.glob("*.md")):
        if md_file.name in ("_index.md", "index.md"):
            continue
        add(md_file.stem, _title_from_md(md_file))

    # Walk subdirectories
    for subdir in sorted(p for p in DOCS_DIR.iterdir() if p.is_dir()):
        # The subdir\'s own index.md (or _index.md) becomes an entry
        for idx_name in ("index.md", "_index.md"):
            idx = subdir / idx_name
            if idx.is_file():
                add(subdir.name, _title_from_md(idx))
                break
        # Depth-1 .md siblings within this subdir (excluding indexes)
        for md_file in sorted(subdir.glob("*.md")):
            if md_file.name in ("index.md", "_index.md"):
                continue
            slug = f"{subdir.name}/{md_file.stem}"
            add(slug, _title_from_md(md_file))
        # Deeper subdirs: only include their index.md as a section entry
        for deeper_idx in sorted(subdir.rglob("index.md")):
            if deeper_idx.parent == subdir:
                continue  # already handled above
            rel = deeper_idx.parent.relative_to(DOCS_DIR)
            add(str(rel), _title_from_md(deeper_idx))
        for deeper_idx in sorted(subdir.rglob("_index.md")):
            if deeper_idx.parent == subdir:
                continue
            rel = deeper_idx.parent.relative_to(DOCS_DIR)
            add(str(rel), _title_from_md(deeper_idx))

    return sorted(pages, key=lambda x: x["title"].lower())


def _git_last_modified(path: Path) -> str | None:
    """Return the last git commit date for a file as a human-readable string."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", str(path)],
            cwd=BASE_DIR, capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            dt = datetime.fromisoformat(result.stdout.strip())
            return dt.strftime("%B %-d, %Y")
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-me-please")
app.config["SESSION_COOKIE_SECURE"]   = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

app.register_blueprint(auth_bp)


@app.context_processor
def inject_globals():
    return {"nav_pages": build_nav(), "site_title": SITE_TITLE}


@app.route("/")
@login_required
def index():
    path = DOCS_DIR / "_index.md"
    if not path.is_file():
        path = DOCS_DIR / "index.md"
    if not path.is_file():
        abort(404)
    md.reset()
    content = md.convert(path.read_text())
    title = _title_from_md(path)
    last_updated = _git_last_modified(path)
    return render_template("doc.html", content=content, title=title, current_slug=None, last_updated=last_updated)


@app.route("/<path:slug>")
@login_required
def doc_page(slug):
    # Strip .md extension if present (links may include it)
    if slug.endswith(".md"):
        slug = slug[:-3]
    # Strip trailing slash if present
    slug = slug.rstrip("/")
    # Try flat file first, then subdirectory index
    path = DOCS_DIR / f"{slug}.md"
    if not path.is_file():
        path = DOCS_DIR / slug / "index.md"
    if not path.is_file():
        path = DOCS_DIR / slug / "_index.md"
    if not path.is_file():
        abort(404)
    md.reset()
    html_content = md.convert(path.read_text())
    title = _title_from_md(path)
    last_updated = _git_last_modified(path)
    return render_template("doc.html", content=html_content, title=title, current_slug=slug, last_updated=last_updated)


@app.route("/api/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# GitHub webhook — auto-deploy on push
# ---------------------------------------------------------------------------

WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "")


def _verify_signature(payload: bytes, signature: str) -> bool:
    """Verify GitHub webhook HMAC-SHA256 signature."""
    if not WEBHOOK_SECRET:
        return False
    expected = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


@app.route("/api/webhook/deploy", methods=["POST"])
def webhook_deploy():
    signature = request.headers.get("X-Hub-Signature-256", "")
    if not _verify_signature(request.get_data(), signature):
        abort(403)

    result = subprocess.run(
        ["git", "pull", "--ff-only"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return jsonify({
        "ok": result.returncode == 0,
        "output": result.stdout.strip(),
        "error": result.stderr.strip() if result.returncode != 0 else None,
    })


if __name__ == "__main__":
    print(f"{SITE_TITLE} on port {PORT}")
    print(f"Docs: {DOCS_DIR}")
    app.run(host="127.0.0.1", port=PORT, debug=False, use_reloader=True)
