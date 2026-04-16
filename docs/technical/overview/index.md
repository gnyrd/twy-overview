# Overview

Documentation sites (docs.tiffanywoodyoga.com, tech.tiffanywoodyoga.com). Flask markdown renderer.

## Service

- **Status**: active (running)
- **Systemd unit**: `twy-docs`
- **Port**: 5005

## Cron Jobs

No cron jobs.

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |
| GET | `/<path:slug>` | No |  |
| GET | `/api/health` | No |  |
| POST | `/api/webhook/deploy` | No |  |

## Dependencies

- **Pip packages**: flask>=3.0, markdown>=3.5, pygments>=2.17, python-dotenv>=1.0

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `DASHBOARD_PASS` | Yes | Yes |
| `DOCS_DIR` | No | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |
| `GITHUB_WEBHOOK_SECRET` | No | Yes |
| `SITE_TITLE` | No | Yes |
| `TWY_DOCS_PORT` | No | Yes |

## Key Files

- `overview/app.py` (entry_point)
- `overview/auth.py` (module)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var DOCS_DIR is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var GITHUB_WEBHOOK_SECRET is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var SITE_TITLE is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_DOCS_PORT is referenced but never defined in .env
