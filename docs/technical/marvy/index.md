# Marvy

Python client library for HeyMarvelous (Namastream) API.

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

No endpoints.

## Dependencies

- **Depended on by**: [announce](../announce/index.md), [classes](../classes/index.md)
- **Pip packages**: requests>=2.25.0, twy-classplan, twy-paths

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `API_TOKEN` | No | Yes |
| `OUTPUT_FILE` | No | Yes |
| `STUDIO_SLUG` | No | Yes |

## Key Files

- `marvy/examples/basic_usage.py` (entry_point)
- `marvy/examples/02_list_events.py` (module)
- `marvy/examples/export_events_csv.py` (module)
- `marvy/marvy/__init__.py` (module)
- `marvy/marvy/client.py` (module)
- `marvy/marvy/db.py` (module)
- `marvy/marvy/exceptions.py` (module)
- `marvy/marvy/reports.py` (module)
- `marvy/tests/__init__.py` (module)
- `marvy/tests/test_client.py` (test)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var API_TOKEN is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var OUTPUT_FILE is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var STUDIO_SLUG is referenced but never defined in .env
