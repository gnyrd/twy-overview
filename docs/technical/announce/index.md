# Announce

Email/campaign automation, notifications, newsletter pipeline.

## Service

No service configured.

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `*/5 * * * *` | `cd /root/twy/announce && /usr/bin/python3 src/class_video_notifier.py >> /root/twy/data/logs/class_video_notifier.log 2>...` | No | `/root/twy/data/logs/class_video_notifier.log` |
| `0 * * * *` | `cd /root/twy/announce && /usr/bin/python3 src/refresh_jwt.py >> logs/jwt_refresh.log 2>&1...` | No | `-` |
| `0 1 * * *` | `cd /root/twy/announce && ./scripts/run_mailchimp_sync.sh` | No | `-` |
| `0 13 * * *` | `cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/daily_report.log 2>&1...` | No | `-` |
| `0 14 1 * *` | `cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py monthly_campaigns /usr/bin/python3 src/run_camp...` | Yes | `/root/twy/data/logs/run_campaigns.log` |
| `0 16 * * *` | `/root/twy/announce/scripts/notify_on_failure.py plan-versions-cleanup /usr/bin/python3 /root/twy/classes/scripts/cleanup...` | Yes | `/root/twy/data/logs/plan_versions_cleanup.log` |
| `0 17 * * *` | `/root/twy/announce/scripts/notify_on_failure.py campaign-send-check /usr/bin/python3 /root/twy/announce/src/verify_campa...` | Yes | `/root/twy/data/logs/verify_campaign_sent.log` |
| `0 18 * * *` | `cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py habit_followup /usr/bin/python3 src/run_habit_f...` | Yes | `/root/twy/data/logs/habit_followup.log` |
| `0 5 * * *` | `/root/twy/announce/scripts/notify_on_failure.py plans-rsync-mini /root/twy/classes/scripts/rsync_plans_to_mini.sh >> /ro...` | Yes | `/root/twy/data/logs/plans_rsync_mini.log` |
| `0 8 * * *` | `cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py hm-placeholder-topup /usr/bin/python3 scripts/hm...` | Yes | `/root/twy/data/logs/hm_placeholders_cron.log` |
| `0 9 * * *` | `cd /root/twy/announce && /usr/bin/python3 src/generate_newsletter_prompts.py >> /root/twy/data/logs/newsletter_prompts.l...` | No | `/root/twy/data/logs/newsletter_prompts.log` |
| `0 9,18 * * *` | `cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >> logs/marvelous_sync.log 2>&1...` | No | `-` |
| `55 11 * * *` | `cd /root/twy/announce && /usr/bin/python3 src/mailchimp_subscriber_data.py >> logs/mailchimp.log 2>&1...` | No | `-` |
| `55 11 * * *` | `cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1...` | No | `-` |

## Endpoints

No endpoints.

## Dependencies

- **Imports from**: [classplan](../classplan/index.md), [marvy](../marvy/index.md), [paths](../paths/index.md)
- **Pip packages**: google-api-python-client, google-auth, google-auth-oauthlib, instaloader, mailchimp3, markdown, marvy@ git+ssh://git@github.com/gnyrd/marvy.git, python-dateutil, python-dotenv, twy-classplan@ file:///root/twy/classplan, twy-paths@ file:///root/twy/paths

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `DRY_RUN` | No | Yes |
| `EMAIL_FROM` | Yes | Yes |
| `EMAIL_TO` | Yes | Yes |
| `GOOGLE_DOC_ID` | Yes | Yes |
| `INSTAGRAM_ACCOUNT` | Yes | No |
| `INSTAGRAM_HISTORY_DIR` | No | Yes |
| `INSTAGRAM_PASSWORD` | Yes | No |
| `INSTAGRAM_PROFILE` | No | Yes |
| `INSTAGRAM_REMOTE_DEST` | Yes | No |
| `INSTAGRAM_SESSION_FILE` | No | Yes |
| `MAILCHIMP_API_KEY` | Yes | Yes |
| `MAILCHIMP_AUDIENCE_ID` | Yes | Yes |
| `MAILCHIMP_SERVER_PREFIX` | Yes | Yes |
| `MAILCHIMP_TEMPLATE_CAMPAIGN_ID` | Yes | Yes |
| `MARVELOUS_ACTIVE_SUBSCRIPTIONS_CSV` | No | Yes |
| `MARVELOUS_ACTIVE_SUBS_REPORT_CATEGORY` | No | Yes |
| `MARVELOUS_ACTIVE_SUBS_REPORT_ID` | No | Yes |
| `MARVELOUS_AUTH_JSON` | Yes | No |
| `MARVELOUS_CANCELED_SUBSCRIPTIONS_CSV` | No | Yes |
| `MARVELOUS_CANCELED_SUBS_REPORT_CATEGORY` | No | Yes |
| `MARVELOUS_CANCELED_SUBS_REPORT_ID` | No | Yes |
| `MARVELOUS_EVENTS_PATH` | No | Yes |
| `MARVELOUS_EXTRA_HEADERS_JSON` | No | Yes |
| `MARVELOUS_FORCE_JWT_REFRESH` | No | Yes |
| `MARVELOUS_LOOKAHEAD_DAYS` | No | Yes |
| `MARVELOUS_MAGIC_URL` | Yes | No |
| `MARVELOUS_PASSWORD` | Yes | Yes |
| `MARVELOUS_SECONDARY_PASSWORD` | Yes | Yes |
| `MARVELOUS_TOKEN` | No | Yes |
| `MARVELOUS_TWY_PASSWORD` | Yes | Yes |
| `MARVELOUS_TWY_USERNAME` | Yes | Yes |
| `MARVELOUS_USERNAME` | Yes | Yes |
| `REMINDER_OFFSETS` | No | Yes |
| `REMINDER_STATE_PATH` | Yes | Yes |
| `SLACK_BOT_TOKEN` | Yes | Yes |
| `SLACK_CHANNEL` | No | Yes |
| `SLACK_REVIEW_CHANNEL` | Yes | Yes |
| `SLACK_STATUS_CHANNEL` | Yes | Yes |
| `SLACK_VIDEO_WEBHOOK_URL` | Yes | Yes |
| `SLACK_WEBHOOK_URL` | Yes | Yes |
| `TIMEZONE` | Yes | Yes |
| `TRELLO_API_KEY` | Yes | No |
| `TRELLO_BOARD_ID` | Yes | No |
| `TRELLO_TOKEN` | Yes | No |
| `TWY_REPORTER_BOT_TOKEN` | Yes | Yes |
| `VERNIO_API_KEY` | Yes | No |
| `YOUTUBE_API_KEY` | Yes | Yes |
| `YOUTUBE_CHANNEL_ID` | Yes | Yes |
| `YOUTUBE_HISTORY_DIR` | No | Yes |

## Key Files

- `announce/examples/marvelous_example.py` (entry_point)
- `announce/scripts/notify_on_failure.py` (entry_point)
- `announce/scripts/refresh_marvelous_events.py` (entry_point)
- `announce/scripts/send_class_email_reminders.py` (entry_point)
- `announce/src/class_video_notifier.py` (entry_point)
- `announce/src/daily_status_report.py` (entry_point)
- `announce/src/generate_newsletter_prompts.py` (entry_point)
- `announce/src/historical_active_counts.py` (entry_point)
- `announce/src/instagram_follower_data.py` (entry_point)
- `announce/src/mailchimp_subscriber_data.py` (entry_point)
- `announce/src/refresh_jwt.py` (entry_point)
- `announce/src/run_campaigns.py` (entry_point)
- `announce/src/run_habit_followup.py` (entry_point)
- `announce/src/sync_mailchimp.py` (entry_point)
- `announce/src/track_redemptions.py` (entry_point)
- `announce/src/verify_campaign_sent.py` (entry_point)
- `announce/src/youtube_subscriber_data.py` (entry_point)
- `announce/scripts/analyze_extra_has_recurring.py` (module)
- `announce/scripts/compare_sync_accuracy.py` (module)
- `announce/src/habit_newsletter_prompt.py` (module)
- `announce/src/mailchimp_campaigns.py` (module)
- `announce/src/marvelous_client.py` (module)
- `announce/src/marvelous_report_jwt.py` (module)
- `announce/src/newsletter.py` (module)
- `announce/src/slack.py` (module)
- `announce/scripts/test_has_recurring.py` (test)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var DRY_RUN is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var INSTAGRAM_HISTORY_DIR is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var INSTAGRAM_PROFILE is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var INSTAGRAM_SESSION_FILE is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_ACTIVE_SUBSCRIPTIONS_CSV is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_ACTIVE_SUBS_REPORT_CATEGORY is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_ACTIVE_SUBS_REPORT_ID is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_CANCELED_SUBSCRIPTIONS_CSV is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_CANCELED_SUBS_REPORT_CATEGORY is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_CANCELED_SUBS_REPORT_ID is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_EXTRA_HEADERS_JSON is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_FORCE_JWT_REFRESH is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_LOOKAHEAD_DAYS is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MARVELOUS_TOKEN is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var REMINDER_OFFSETS is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var SLACK_CHANNEL is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var YOUTUBE_HISTORY_DIR is referenced but never defined in .env
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 9,18 * * * cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >>...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 * * * * cd /root/twy/announce && /usr/bin/python3 src/refresh_jwt.py >> logs/jwt_refresh...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 1 * * * cd /root/twy/announce && ./scripts/run_mailchimp_sync.sh
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 13 * * * cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/dai...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 55 11 * * * cd /root/twy/announce && /usr/bin/python3 src/mailchimp_subscriber_data.py >> lo...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 55 11 * * * cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: */5 * * * * cd /root/twy/announce && /usr/bin/python3 src/class_video_notifier.py >> /root/t...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 9 * * * cd /root/twy/announce && /usr/bin/python3 src/generate_newsletter_prompts.py >> ...
- 🟡 **MEDIUM** [duplicate_utilities]: Mailchimp client code duplicated between announce and classes
- 🟡 **MEDIUM** [duplicate_utilities]: Slack integration duplicated between announce and classes
- 🔵 **LOW** [orphan_env_vars]: Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var INSTAGRAM_REMOTE_DEST is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var MARVELOUS_AUTH_JSON is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TRELLO_API_KEY is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TRELLO_BOARD_ID is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TRELLO_TOKEN is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var VERNIO_API_KEY is defined but never referenced in code
