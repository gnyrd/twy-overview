# System Health

## Service Status

| Service | Project | Unit | Status |
|---------|---------|------|--------|
| data-viewer | [data-viewer](data-viewer/index.md) | `data-viewer` | ❓ activating (auto-restart) |
| twy-class-dashboard | [classes](classes/index.md) | `twy-class-dashboard` | ✅ active (running) |
| twy-clips-dashboard | [clips](clips/index.md) | `twy-clips-dashboard` | ✅ active (running) |
| twy-docs | [overview](overview/index.md) | `twy-docs` | ✅ active (running) |
| twy-tech | [overview](overview/index.md) | `twy-tech` | ✅ active (running) |
| twy-yoga-habit | [yoga-habit](yoga-habit/index.md) | `twy-yoga-habit` | ✅ active (running) |
| twy-zoom-downloader | [download](download/index.md) | `twy-zoom-downloader` | ✅ active (running) |

## Lint Findings

### 🟠 HIGH (39)

- **broken_services** ([data-viewer](data-viewer/index.md)): Service data-viewer is activating (auto-restart)
- **undefined_env_vars** ([classes](classes/index.md)): Env var API_TOKEN is referenced but never defined in .env
- **undefined_env_vars** ([marvy](marvy/index.md)): Env var API_TOKEN is referenced but never defined in .env
- **undefined_env_vars** ([overview](overview/index.md)): Env var DOCS_DIR is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var DRY_RUN is referenced but never defined in .env
- **undefined_env_vars** ([overview](overview/index.md)): Env var GITHUB_WEBHOOK_SECRET is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_HISTORY_DIR is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_PROFILE is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_SESSION_FILE is referenced but never defined in .env
- **undefined_env_vars** ([tweee-gpt](tweee-gpt/index.md)): Env var MAILCHIMP_FROM_NAME is referenced but never defined in .env
- **undefined_env_vars** ([tweee-gpt](tweee-gpt/index.md)): Env var MAILCHIMP_REPLY_TO is referenced but never defined in .env
- **undefined_env_vars** ([tweee-gpt](tweee-gpt/index.md)): Env var MAILCHIMP_SERVER is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_ACTIVE_SUBSCRIPTIONS_CSV is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_ACTIVE_SUBS_REPORT_CATEGORY is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_ACTIVE_SUBS_REPORT_ID is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_CANCELED_SUBSCRIPTIONS_CSV is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_CANCELED_SUBS_REPORT_CATEGORY is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_CANCELED_SUBS_REPORT_ID is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_EXTRA_HEADERS_JSON is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_FORCE_JWT_REFRESH is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_LOOKAHEAD_DAYS is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_TOKEN is referenced but never defined in .env
- **undefined_env_vars** ([marvy](marvy/index.md)): Env var OUTPUT_FILE is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var REMINDER_OFFSETS is referenced but never defined in .env
- **undefined_env_vars** ([overview](overview/index.md)): Env var SITE_TITLE is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var SLACK_CHANNEL is referenced but never defined in .env
- **undefined_env_vars** ([marvy](marvy/index.md)): Env var STUDIO_SLUG is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var TWY_BUMPERS_INTRO is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var TWY_BUMPERS_OUTRO is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var TWY_CLASS_VIDEOS_DIR is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var TWY_CLIPS_URL is referenced but never defined in .env
- **undefined_env_vars** ([docs-scanner](docs-scanner/index.md)): Env var TWY_DOCS_DB is referenced but never defined in .env
- **undefined_env_vars** ([overview](overview/index.md)): Env var TWY_DOCS_PORT is referenced but never defined in .env
- **undefined_env_vars** ([paths](paths/index.md)): Env var TWY_ENV_PATH is referenced but never defined in .env
- **undefined_env_vars** ([docs-scanner](docs-scanner/index.md)): Env var TWY_PROJECTS_ROOT is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var TWY_THUMBNAIL_SCRIPT is referenced but never defined in .env
- **undefined_env_vars** ([docs-scanner](docs-scanner/index.md)): Env var VAR is referenced but never defined in .env
- **undefined_env_vars** ([download](download/index.md)): Env var WATCHDOG_SCAN_DAYS is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var YOUTUBE_HISTORY_DIR is referenced but never defined in .env

### 🟡 MEDIUM (12)

- **duplicate_utilities** ([announce](announce/index.md)): Mailchimp client code duplicated between announce and classes
- **duplicate_utilities** ([announce](announce/index.md)): Slack integration duplicated between announce and classes
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 13 * * * cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/dai...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 55 11 * * * cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1
- **missing_failure_wrappers** ([clips](clips/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/clips && ./src/pipeline/class_recording_watchdog.sh >> logs/watchdo...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 15,45 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back ...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 8 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../da...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 9 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 10 * * * cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs...
- **missing_failure_wrappers** ([video-editor](video-editor/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data...
- **missing_failure_wrappers** ([yoga-habit](yoga-habit/index.md)): Cron job missing failure wrapper: 0 10 1 * * /root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2...

### 🔵 LOW (41)

- **orphan_env_vars** ([clips](clips/index.md)): Env var ASPECT_RATIO is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var CAPTIONED_SUBDIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var CLIPS_SUBDIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var EXTRACTED_SUBDIR is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([central](central/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([central](central/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_REMOTE_DEST is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MAILCHIMP_NONMEMBER_LIST_ID is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MAILCHIMP_TYL_LIST_ID is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MARVELOUS_ADMIN_SECONDARY_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_AUTH_JSON is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([central](central/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var MAXMIND_LICENSE_KEY is defined but never referenced in code
- **orphan_env_vars** ([central](central/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([video-editor](video-editor/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([central](central/index.md)): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- **orphan_env_vars** ([video-editor](video-editor/index.md)): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var PARTICIPANTS_FILE is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var SRT_SUBDIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var THUMBNAIL_SUFFIX is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var TRELLO_API_KEY is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var TRELLO_BOARD_ID is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var TRELLO_TOKEN is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var TWY_CLASSES_DIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var TWY_CLASSES_DIR is defined but never referenced in code
- **orphan_env_vars** ([video-editor](video-editor/index.md)): Env var TWY_CLASSES_DIR is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var TWY_CLASS_PLANS_DIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var TWY_PROJECT_DIR is defined but never referenced in code
- **orphan_env_vars** ([download](download/index.md)): Env var TWY_PROJECT_DIR is defined but never referenced in code
- **orphan_env_vars** ([clips](clips/index.md)): Env var UNCAPTIONED_SUBDIR is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var VERNIO_API_KEY is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var YOGA_HABIT_REGISTER_URL is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var YOUTUBE_REMOTE_DEST is defined but never referenced in code
