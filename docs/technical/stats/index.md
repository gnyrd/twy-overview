# Stats

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |

## Dependencies

- **Imports from**: [paths](../paths/index.md)
- **Pip packages**: flask==3.0.3, gunicorn==23.0.0, pytest==8.3.3, requests==2.32.3, twy-paths@ file:///root/twy/paths

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `ANTHROPIC_API_KEY` | Yes | No |
| `DASHBOARD_PASS` | Yes | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |
| `INSTAGRAM_ACCOUNT` | Yes | No |
| `INSTAGRAM_PASSWORD` | Yes | No |
| `MAILCHIMP_API_KEY` | Yes | Yes |
| `MAILCHIMP_AUDIENCE_ID` | Yes | Yes |
| `MAILCHIMP_SERVER_PREFIX` | Yes | Yes |
| `MAILCHIMP_TEMPLATE_CAMPAIGN_ID` | Yes | No |
| `MARVELOUS_MAGIC_URL` | Yes | No |
| `MARVELOUS_PASSWORD` | Yes | No |
| `MARVELOUS_SECONDARY_PASSWORD` | Yes | No |
| `MARVELOUS_USERNAME` | Yes | No |
| `MARVY_AUTH_FILE` | Yes | No |
| `NOTIFY_EMAIL_FROM` | Yes | No |
| `NOTIFY_EMAIL_TO` | Yes | No |
| `OPENAI_API_KEY` | Yes | No |
| `SLACK_BOT_TOKEN` | Yes | No |
| `SLACK_REVIEW_CHANNEL` | Yes | No |
| `SLACK_STATUS_CHANNEL` | Yes | No |
| `TIMEZONE` | Yes | No |
| `TWY_DATA_DIR` | Yes | No |
| `TWY_REPORTER_BOT_TOKEN` | Yes | No |
| `YOUTUBE_API_KEY` | Yes | No |
| `YOUTUBE_CHANNEL_ID` | Yes | No |
| `ZOOM_ACCOUNT_ID` | Yes | No |
| `ZOOM_CLIENT_ID` | Yes | No |
| `ZOOM_CLIENT_SECRET` | Yes | No |

## Key Files

- `stats/app.py` (entry_point)
- `stats/auth.py` (module)
- `stats/config.py` (module)
- `stats/yoga_habit/__init__.py` (module)
- `stats/yoga_habit/data.py` (module)
- `stats/yoga_habit/views.py` (module)
- `stats/tests/conftest.py` (test)
- `stats/tests/test_auth.py` (test)
- `stats/tests/test_data_funnel_attendance.py` (test)
- `stats/tests/test_data_funnel_clicks.py` (test)
- `stats/tests/test_data_funnel_marvy.py` (test)
- `stats/tests/test_data_funnel_redemption.py` (test)
- `stats/tests/test_data_loader.py` (test)
- `stats/tests/test_data_months_funnel.py` (test)
- `stats/tests/test_data_slices.py` (test)
- `stats/tests/test_views.py` (test)

## Lint Findings

- 🔵 **LOW** [orphan_env_vars]: Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var NOTIFY_EMAIL_TO is defined but never referenced in code
