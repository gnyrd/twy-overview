# Paths

Path computation and central environment loading.

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

No endpoints.

## Dependencies

- **Depended on by**: [announce](../announce/index.md), [classes](../classes/index.md), [classplan](../classplan/index.md), [clips](../clips/index.md), [data-viewer](../data-viewer/index.md), [download](../download/index.md), [stats](../stats/index.md), [video-editor](../video-editor/index.md), [yoga-habit](../yoga-habit/index.md)

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `MARVY_AUTH_FILE` | Yes | Yes |
| `TWY_ASPECT_RATIO` | No | Yes |
| `TWY_DATA_DIR` | Yes | Yes |
| `TWY_ENV_PATH` | No | Yes |

## Key Files

- `paths/build/lib/twy_paths/__init__.py` (module)
- `paths/build/lib/twy_paths/env.py` (module)
- `paths/build/lib/twy_paths/paths.py` (module)
- `paths/twy_paths/__init__.py` (module)
- `paths/twy_paths/env.py` (module)
- `paths/twy_paths/paths.py` (module)
- `paths/tests/test_aspect_ratio.py` (test)
- `paths/tests/test_clips_dirs.py` (test)
- `paths/tests/test_habit_stats.py` (test)
- `paths/tests/test_logs.py` (test)
- `paths/tests/test_marvy_desc.py` (test)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_ASPECT_RATIO is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_ENV_PATH is referenced but never defined in .env
