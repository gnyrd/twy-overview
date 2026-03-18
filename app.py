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
from dotenv import load_dotenv

load_dotenv()

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
    """Build sidebar navigation from the docs directory."""
    pages = []
    for md_file in sorted(DOCS_DIR.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        pages.append({"slug": md_file.stem, "title": _title_from_md(md_file)})
    return pages


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
        abort(404)
    md.reset()
    content = md.convert(path.read_text())
    title = _title_from_md(path)
    last_updated = _git_last_modified(path)
    return render_template("doc.html", content=content, title=title, current_slug=None, last_updated=last_updated)


@app.route("/<slug>")
@login_required
def doc_page(slug):
    path = DOCS_DIR / f"{slug}.md"
    if not path.is_file():
        abort(404)
    md.reset()
    content = md.convert(path.read_text())
    title = _title_from_md(path)
    last_updated = _git_last_modified(path)
    return render_template("doc.html", content=content, title=title, current_slug=slug, last_updated=last_updated)


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
    app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=True)
