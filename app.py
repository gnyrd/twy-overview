"""
TWY Docs — Flask application.
Serves a single directory of markdown documentation with session-based auth.

Configure via environment variables:
    DOCS_DIR        Path to the markdown docs directory (default: docs/user-guide)
    SITE_TITLE      Display name shown in sidebar and page titles (default: TWY Docs)
    TWY_DOCS_PORT   Port to listen on (default: 5005)
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

import markdown
from flask import Flask, render_template, abort

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
    return render_template("doc.html", content=content, title=title, current_slug=None)


@app.route("/<slug>")
@login_required
def doc_page(slug):
    path = DOCS_DIR / f"{slug}.md"
    if not path.is_file():
        abort(404)
    md.reset()
    content = md.convert(path.read_text())
    title = _title_from_md(path)
    return render_template("doc.html", content=content, title=title, current_slug=slug)


@app.route("/api/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    print(f"{SITE_TITLE} on port {PORT}")
    print(f"Docs: {DOCS_DIR}")
    app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=True)
