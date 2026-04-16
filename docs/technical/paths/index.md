# Paths

Path computation and central environment loading.

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

No endpoints.

## Dependencies

- **Depended on by**: [announce](../announce/index.md), [classes](../classes/index.md), [classplan](../classplan/index.md), [clips](../clips/index.md), [data-viewer](../data-viewer/index.md), [download](../download/index.md), [video-editor](../video-editor/index.md)

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `TWY_DATA_DIR` | Yes | Yes |
| `TWY_ENV_PATH` | No | Yes |

## Key Files

- `paths/twy_paths/__init__.py` (module)
- `paths/twy_paths/env.py` (module)
- `paths/twy_paths/paths.py` (module)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_ENV_PATH is referenced but never defined in .env
