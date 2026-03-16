# twy-overview

Documentation hub for the Tiffany Wood Yoga content pipeline. Two password-protected Flask sites serving markdown docs:

- **docs.tiffanywoodyoga.com** — User Guide (task-oriented, "How Do I" style)
- **tech.tiffanywoodyoga.com** — Technical Reference (developer-level architecture, APIs, deployment)

Both sites are the same Flask app pointed at different `docs/` subdirectories via environment variables.

## Run Locally

```bash
pip install -r requirements.txt

# User guide on port 5005
DOCS_DIR=docs/user-guide SITE_TITLE="TWY User Guide" DASHBOARD_PASS=test TWY_DOCS_PORT=5005 python3 app.py

# Technical reference on port 5006
DOCS_DIR=docs/technical SITE_TITLE="TWY Technical Reference" DASHBOARD_PASS=test TWY_DOCS_PORT=5006 python3 app.py
```

Both run in debug mode — edit any `.md` file and refresh the browser.

## Deploy

See `docs/technical/deployment.md` for full instructions. Quick version:

```bash
# Copy systemd units
cp deploy/twy-docs.service /etc/systemd/system/
cp deploy/twy-tech.service /etc/systemd/system/

# Create .env files from examples
cp .env.docs.example .env.docs
cp .env.tech.example .env.tech
# Edit both with real passwords and keys

# Start
systemctl daemon-reload
systemctl enable --now twy-docs twy-tech

# Set up nginx + SSL (see docs/technical/deployment.md)
```

## Structure

```
app.py                  Single Flask app, configured via env vars
auth.py                 Session-based single-password auth
templates/              Jinja2 templates (sidebar + content layout)
static/style.css        Reading stylesheet with syntax highlighting

docs/
├── user-guide/         Served at docs.tiffanywoodyoga.com
│   ├── _index.md
│   ├── daily-class-workflow.md
│   ├── downloading-recordings.md
│   ├── processing-clips.md
│   ├── trimming-and-publishing.md
│   ├── thumbnails.md
│   ├── newsletters.md
│   ├── announcements-and-reminders.md
│   └── asset-management.md
└── technical/          Served at tech.tiffanywoodyoga.com
    ├── _index.md
    ├── architecture.md
    ├── twy-download.md
    ├── twy-clips.md
    ├── twy-class-plans.md
    ├── twy-video-editor.md
    ├── twy-tweee-gpt.md
    ├── twy-announce.md
    ├── twy-asset-management.md
    ├── deployment.md
    └── environment-variables.md

deploy/
├── twy-docs.service    systemd unit (port 5005)
└── twy-tech.service    systemd unit (port 5006)
```
