# Classes

Class plan dashboard, Tweee API, Flask web app on port 5003.

## Service

- **Status**: active (running)
- **Systemd unit**: `twy-class-dashboard`
- **Port**: 5003
- **URL**: [https://classes.tiffanywoodyoga.com/thumbnails/](https://classes.tiffanywoodyoga.com/thumbnails/)

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `0 13 28 * *` | `cd /root/twy/classes && /usr/bin/python3 scripts/create_next_habit_event.py >> /root/twy/data/logs/habit-event.log 2>&1...` | No | `/root/twy/data/logs/habit-event.log` |
| `0 8 1 * *` | `cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /root/twy/data/logs/monthly_series.log 2>...` | No | `/root/twy/data/logs/monthly_series.log` |
| `0 8 7 * *` | `cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /root/twy/data/logs/monthly_series.log 2>...` | No | `/root/twy/data/logs/monthly_series.log` |
| `5 7 * * *` | `cd /root/twy/classes && /usr/bin/python3 scripts/sync.py --db /root/twy/data/marvy.db >> /root/twy/data/logs/marvy_sync....` | No | `/root/twy/data/logs/marvy_sync.log` |

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/health` | No |  |

## Dependencies

- **Imports from**: [classplan](../classplan/index.md), [marvy](../marvy/index.md), [paths](../paths/index.md)
- **Pip packages**: flask>=3.0, mailchimp3>=3.0, markdown>=3.5, python-dotenv>=1.0, requests>=2.31, twy-classplan@ file:///root/twy/classplan, twy-paths@ file:///root/twy/paths

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `API_TOKEN` | No | Yes |
| `DASHBOARD_PASS` | Yes | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |
| `MAILCHIMP_API_KEY` | Yes | Yes |
| `MAILCHIMP_AUDIENCE_ID` | Yes | Yes |
| `MAILCHIMP_NONMEMBER_LIST_ID` | Yes | No |
| `MAILCHIMP_SERVER_PREFIX` | Yes | Yes |
| `MAILCHIMP_TEMPLATE_CAMPAIGN_ID` | Yes | Yes |
| `MAILCHIMP_TYL_LIST_ID` | Yes | No |
| `MARVELOUS_ADMIN_PASSWORD` | Yes | Yes |
| `MARVELOUS_ADMIN_SECONDARY_PASSWORD` | Yes | No |
| `MARVELOUS_ADMIN_USERNAME` | Yes | Yes |
| `MARVELOUS_PASSWORD` | Yes | Yes |
| `MARVELOUS_USERNAME` | Yes | Yes |
| `SLACK_BOT_TOKEN` | Yes | Yes |
| `SLACK_REVIEW_CHANNEL` | Yes | Yes |
| `SLACK_STATUS_CHANNEL` | Yes | Yes |
| `SLACK_TWEEE_WRITES_CHANNEL` | No | Yes |
| `SLACK_USER_JP` | No | Yes |
| `SLACK_USER_TIFF` | No | Yes |
| `TWY_BUMPERS_INTRO` | No | Yes |
| `TWY_BUMPERS_OUTRO` | No | Yes |
| `TWY_CLASSES_DIR` | Yes | No |
| `TWY_CLASS_PLANS_DIR` | Yes | No |
| `TWY_CLASS_VIDEOS_DIR` | No | Yes |
| `TWY_CLIPS_URL` | No | Yes |
| `TWY_DASHBOARD_PORT` | Yes | Yes |
| `TWY_REPORTER_BOT_TOKEN` | Yes | Yes |
| `TWY_THUMBNAIL_SCRIPT` | No | Yes |
| `YOGA_HABIT_REGISTER_URL` | Yes | No |

## Key Files

- `classes/dashboard/app.py` (entry_point)
- `classes/scripts/cleanup_plan_versions.py` (entry_point)
- `classes/scripts/create_from_template.py` (entry_point)
- `classes/scripts/create_next_habit_event.py` (entry_point)
- `classes/scripts/duplicate_recordings.py` (entry_point)
- `classes/scripts/hm_placeholder_topup.py` (entry_point)
- `classes/scripts/monthly_series_workflow.py` (entry_point)
- `classes/scripts/post_recording_workflow.py` (entry_point)
- `classes/scripts/remove_thumbnail.py` (entry_point)
- `classes/scripts/replace_video.py` (entry_point)
- `classes/scripts/sync.py` (entry_point)
- `classes/dashboard/api.py` (module)
- `classes/dashboard/auth.py` (module)
- `classes/dashboard/config.py` (module)
- `classes/dashboard/data.py` (module)
- `classes/dashboard/mailchimp.py` (module)
- `classes/dashboard/marvelous.py` (module)
- `classes/dashboard/newsletter.py` (module)
- `classes/dashboard/plan_versions.py` (module)
- `classes/dashboard/slack.py` (module)
- `classes/dashboard/tests/__init__.py` (module)
- `classes/dashboard/views.py` (module)
- `classes/scripts/create_habit_events.py` (module)
- `classes/scripts/tests/__init__.py` (module)
- `classes/dashboard/tests/test_data_write_plan.py` (test)
- `classes/dashboard/tests/test_newsletter.py` (test)
- `classes/dashboard/tests/test_newsletter_prompt.py` (test)
- `classes/dashboard/tests/test_plan_versions.py` (test)
- `classes/scripts/tests/test_cleanup_plan_versions.py` (test)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var API_TOKEN is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var SLACK_TWEEE_WRITES_CHANNEL is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_BUMPERS_INTRO is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_BUMPERS_OUTRO is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_CLASS_VIDEOS_DIR is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_CLIPS_URL is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var TWY_THUMBNAIL_SCRIPT is referenced but never defined in .env
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 5 7 * * * cd /root/twy/classes && /usr/bin/python3 scripts/sync.py --db /root/twy/data/mar...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 8 1 * * cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 8 7 * * cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 13 28 * * cd /root/twy/classes && /usr/bin/python3 scripts/create_next_habit_event.py >> /...
- 🔵 **LOW** [orphan_env_vars]: Env var MAILCHIMP_NONMEMBER_LIST_ID is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var MAILCHIMP_TYL_LIST_ID is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var MARVELOUS_ADMIN_SECONDARY_PASSWORD is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_CLASSES_DIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_CLASS_PLANS_DIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var YOGA_HABIT_REGISTER_URL is defined but never referenced in code
