# Data Viewer

SQL query builder for HeyMarvelous data.

## Service

- **Status**: active (running)
- **Systemd unit**: `data-viewer`
- **Port**: 5007

## Cron Jobs

No cron jobs.

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |
| POST | `/api/query` | No |  |
| GET | `/api/saved-queries` | No |  |
| POST | `/api/saved-queries` | No |  |
| DELETE | `/api/saved-queries/<name>` | No |  |
| GET | `/api/schema` | No |  |
| POST | `/api/sync` | No |  |
| GET | `/api/sync-status` | No |  |
| GET | `/login` | No |  |
| POST | `/login` | No |  |
| GET | `/logout` | No |  |

## Dependencies

- **Imports from**: [paths](../paths/index.md)
- **Pip packages**: flask>=3.0

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `DASHBOARD_PASS` | Yes | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |

## Key Files

- `data-viewer/app.py` (entry_point)

## Lint Findings

No lint findings.
