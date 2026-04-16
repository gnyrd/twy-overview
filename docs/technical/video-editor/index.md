# Video Editor

Thumbnail extraction and Vimeo publishing pipeline.

## Service

No service configured.

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `*/5 * * * *` | `cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data/logs/thumbnail_watchdog.log 2>&1...` | No | `-` |

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |
| POST | `/api/generate-thumbnail-manual` | No |  |
| GET | `/api/health` | No |  |
| POST | `/api/rank-thumbnails` | No |  |
| POST | `/api/select-thumbnail` | No |  |
| GET | `/class/<class_name>` | No |  |
| GET | `/login` | No |  |
| POST | `/login` | No |  |
| GET | `/logout` | No |  |
| GET | `/media/candidate/<class_name>/<filename>` | No |  |

## Dependencies

- **Imports from**: [paths](../paths/index.md)
- **Pip packages**: flask>=3.0, google-api-python-client>=2.0, google-auth>=2.0, google-auth-oauthlib>=1.0, python-dotenv>=1.0

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `ANTHROPIC_API_KEY` | Yes | No |
| `DASHBOARD_PASS` | Yes | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |
| `HM_DASHBOARD_PORT` | Yes | Yes |
| `MARVELOUS_EVENTS_PATH` | Yes | No |
| `NOTIFY_EMAIL_FROM` | Yes | No |
| `NOTIFY_EMAIL_TO` | Yes | No |
| `OPENAI_API_KEY` | Yes | No |
| `TWY_CLASSES_DIR` | Yes | No |
| `VIDEO_EDITOR_PORT` | Yes | Yes |

## Key Files

- `video-editor/src/dashboard-archive/dashboard.py` (entry_point)
- `video-editor/src/dashboard/dashboard.py` (entry_point)

## Lint Findings

- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: */5 * * * * cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data...
- 🔵 **LOW** [orphan_env_vars]: Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_CLASSES_DIR is defined but never referenced in code
