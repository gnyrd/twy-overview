# Docs Scanner

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

No endpoints.

## Dependencies

No dependencies recorded.

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `MC_ENV_PATH` | No | Yes |
| `TWY_DOCS_DB` | No | Yes |
| `TWY_PROJECTS_ROOT` | No | Yes |
| `VAR` | No | Yes |

## Key Files

- `docs-scanner/twy_docs/cli.py` (entry_point)
- `docs-scanner/twy_docs/collectors/python_collector.py` (entry_point)
- `docs-scanner/twy_docs/render.py` (entry_point)
- `docs-scanner/tests/__init__.py` (module)
- `docs-scanner/twy_docs/__init__.py` (module)
- `docs-scanner/twy_docs/__main__.py` (module)
- `docs-scanner/twy_docs/collectors/__init__.py` (module)
- `docs-scanner/twy_docs/collectors/cron_collector.py` (module)
- `docs-scanner/twy_docs/collectors/env_collector.py` (module)
- `docs-scanner/twy_docs/collectors/git_info.py` (module)
- `docs-scanner/twy_docs/collectors/mc_campaigns.py` (module)
- `docs-scanner/twy_docs/collectors/mc_cross_ref.py` (module)
- `docs-scanner/twy_docs/collectors/mc_journeys.py` (module)
- `docs-scanner/twy_docs/collectors/mc_tags_segments.py` (module)
- `docs-scanner/twy_docs/collectors/mc_templates.py` (module)
- `docs-scanner/twy_docs/collectors/nginx_collector.py` (module)
- `docs-scanner/twy_docs/collectors/pip_collector.py` (module)
- `docs-scanner/twy_docs/collectors/projects.py` (module)
- `docs-scanner/twy_docs/collectors/systemd_services.py` (module)
- `docs-scanner/twy_docs/config.py` (module)
- `docs-scanner/twy_docs/db.py` (module)
- `docs-scanner/twy_docs/lint/__init__.py` (module)
- `docs-scanner/twy_docs/lint/checks.py` (module)
- `docs-scanner/twy_docs/lint/mc_checks.py` (module)
- `docs-scanner/twy_docs/mc/__init__.py` (module)
- `docs-scanner/twy_docs/mc/classify.py` (module)
- `docs-scanner/twy_docs/mc/client.py` (module)
- `docs-scanner/twy_docs/renderers/__init__.py` (module)
- `docs-scanner/twy_docs/renderers/mc_wiki.py` (module)
- `docs-scanner/twy_docs/renderers/tech_index.py` (module)
- `docs-scanner/twy_docs/renderers/tech_per_project.py` (module)
- `docs-scanner/twy_docs/renderers/tech_wiki.py` (module)
- `docs-scanner/twy_docs/renderers/user_guide.py` (module)
- `docs-scanner/twy_docs/scanner.py` (module)
- `docs-scanner/tests/test_mc_classify.py` (test)
- `docs-scanner/tests/test_mc_client.py` (test)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var MC_ENV_PATH is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_DOCS_DB is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_PROJECTS_ROOT is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var VAR is referenced but never defined in .env
