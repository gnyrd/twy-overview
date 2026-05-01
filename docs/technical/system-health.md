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

### 🟠 HIGH (42)

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
- **undefined_env_vars** ([docs-scanner](docs-scanner/index.md)): Env var MC_ENV_PATH is referenced but never defined in .env
- **undefined_env_vars** ([marvy](marvy/index.md)): Env var OUTPUT_FILE is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var REMINDER_OFFSETS is referenced but never defined in .env
- **undefined_env_vars** ([overview](overview/index.md)): Env var SITE_TITLE is referenced but never defined in .env
- **undefined_env_vars** ([announce](announce/index.md)): Env var SLACK_CHANNEL is referenced but never defined in .env
- **undefined_env_vars** ([classes](classes/index.md)): Env var SLACK_TWEEE_WRITES_CHANNEL is referenced but never defined in .env
- **undefined_env_vars** ([marvy](marvy/index.md)): Env var STUDIO_SLUG is referenced but never defined in .env
- **undefined_env_vars** ([paths](paths/index.md)): Env var TWY_ASPECT_RATIO is referenced but never defined in .env
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

### 🟡 MEDIUM (30)

- **duplicate_utilities** ([announce](announce/index.md)): Mailchimp client code duplicated between announce and classes
- **duplicate_utilities** ([announce](announce/index.md)): Slack integration duplicated between announce and classes
- **mc_duplicate_journey_name** (system): Multiple journeys named 'Welcome new contacts' (IDs: 4659,6126)
- **mc_near_duplicate_tag** (system): Near-duplicate tags (likely hyphen vs em-dash): 'Membership - Yoga Lifestyle'(29), 'Membership – Yoga Lifestyle'(1). Canonical form: 'Membership - Yoga Lifestyle'
- **mc_zombie_journey** (system): Journey 'Optimal Blueprint Series' (ID 3921): Status=sending but last enrollment 807 days ago (stale)
- **mc_zombie_journey** (system): Journey 'YLM AD Campaign Sign Up' (ID 4635): Status=sending but last enrollment 260 days ago (stale)
- **mc_zombie_journey** (system): Journey 'Palouse 2025 Welcome Email' (ID 6032): Status=sending but last enrollment 383 days ago (stale)
- **mc_zombie_journey** (system): Journey 'FINAL Palouse 2025 Registration Email Sequence' (ID 6057): Status=sending but last enrollment 320 days ago (stale)
- **mc_zombie_journey** (system): Journey 'Retreat Info – Auto Send' (ID 6059): Status=sending but last enrollment 317 days ago (stale)
- **mc_zombie_journey** (system): Journey 'Palouse 2 free classes email sequence' (ID 6060): Status=sending but last enrollment 320 days ago (stale)
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 15,45 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back ...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 9,18 * * * cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >>...
- **missing_failure_wrappers** ([clips](clips/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/clips && ./src/pipeline/class_recording_watchdog.sh >> logs/watchdo...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 * * * * cd /root/twy/announce && /usr/bin/python3 src/refresh_jwt.py >> logs/jwt_refresh...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 1 * * * cd /root/twy/announce && ./scripts/run_mailchimp_sync.sh
- **missing_failure_wrappers** ([classes](classes/index.md)): Cron job missing failure wrapper: 5 7 * * * cd /root/twy/classes && /usr/bin/python3 scripts/sync.py --db /root/twy/data/mar...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 13 * * * cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/dai...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 55 11 * * * cd /root/twy/announce && /usr/bin/python3 src/mailchimp_subscriber_data.py >> lo...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 55 11 * * * cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1
- **missing_failure_wrappers** ([video-editor](video-editor/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 8 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../da...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 9 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/...
- **missing_failure_wrappers** ([download](download/index.md)): Cron job missing failure wrapper: 0 10 * * * cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs...
- **missing_failure_wrappers** ([classes](classes/index.md)): Cron job missing failure wrapper: 0 8 1 * * cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /...
- **missing_failure_wrappers** ([classes](classes/index.md)): Cron job missing failure wrapper: 0 8 7 * * cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: */5 * * * * cd /root/twy/announce && /usr/bin/python3 src/class_video_notifier.py >> /root/t...
- **missing_failure_wrappers** ([announce](announce/index.md)): Cron job missing failure wrapper: 0 9 * * * cd /root/twy/announce && /usr/bin/python3 src/generate_newsletter_prompts.py >> ...
- **missing_failure_wrappers** ([classes](classes/index.md)): Cron job missing failure wrapper: 0 13 28 * * cd /root/twy/classes && /usr/bin/python3 scripts/create_next_habit_event.py >> /...
- **missing_failure_wrappers** ([yoga-habit](yoga-habit/index.md)): Cron job missing failure wrapper: 0 10 1 * * /root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2...

### 🔵 LOW (67)

- **mc_journey_trigger_unknown** (system): Journey 'Optimal Blueprint Series' (ID 3921) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_journey_trigger_unknown** (system): Journey 'YLM AD Campaign Sign Up' (ID 4635) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_journey_trigger_unknown** (system): Journey 'Palouse 2025 Welcome Email' (ID 6032) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_journey_trigger_unknown** (system): Journey 'FINAL Palouse 2025 Registration Email Sequence' (ID 6057) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_journey_trigger_unknown** (system): Journey 'Retreat Info – Auto Send' (ID 6059) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_journey_trigger_unknown** (system): Journey 'Palouse 2 free classes email sequence' (ID 6060) has no HM product mapped - enrollment cannot be cross-referenced
- **mc_orphan_segment** (system): Segment 'Campaign Pasted Segment - 17 May 2024 09:47:51 am' (ID 2977799) has 0 members
- **mc_orphan_tag** (system): Tag 'Kripalu' (ID 282) has 0 members
- **mc_orphan_tag** (system): Tag 'Kripalu 2022' (ID 5018) has 0 members
- **mc_orphan_tag** (system): Tag 'Top 20 Mexico' (ID 6186) has 0 members
- **mc_orphan_tag** (system): Tag 'Free Course Members' (ID 2959807) has 0 members
- **mc_orphan_tag** (system): Tag 'Foundations of Anusara Yoga - Four Class Series Btests' (ID 2980520) has 0 members
- **mc_orphan_tag** (system): Tag 'Retreat Info Sent' (ID 3017624) has 0 members
- **mc_orphan_tag** (system): Tag 'test' (ID 3017831) has 0 members
- **mc_orphan_tag** (system): Tag 'Campaign Pasted Segment - 19 Jul 2024 03:59:58 pm' (ID 3018781) has 0 members
- **mc_orphan_tag** (system): Tag 'Lifecycle – Alumni' (ID 3018795) has 0 members
- **mc_orphan_tag** (system): Tag 'Lifecycle – VIP' (ID 3018796) has 0 members
- **mc_orphan_tag** (system): Tag 'Region – Utah' (ID 3018797) has 0 members
- **mc_orphan_tag** (system): Tag 'Blitz – Dec 2025 – Yoga Lifestyle – Responded' (ID 3018802) has 0 members
- **mc_orphan_tag** (system): Tag 'YLM Ad Hoc' (ID 3018913) has 0 members
- **mc_orphan_tag** (system): Tag 'Status - Member Canceled' (ID 3018914) has 0 members
- **mc_unused_template** (system): Template 'Mexico Retreat Template: Short' (ID 1831): Last used 1204 days ago
- **mc_unused_template** (system): Template 'Mexico Retreat Template: Medium' (ID 1868): Never used
- **mc_unused_template** (system): Template 'Mexico Retreat Template: Long' (ID 1870): Never used
- **mc_unused_template** (system): Template '2023 Newsletter Template' (ID 2845): Never used
- **mc_unused_template** (system): Template 'Mexico Welcome Email' (ID 4775): Last used 1153 days ago
- **mc_unused_template** (system): Template 'March 2023 Series Promo with Playable Video' (ID 5125): Never used
- **orphan_env_vars** (system): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** ([stats](stats/index.md)): Env var INSTAGRAM_ACCOUNT is defined but never referenced in code
- **orphan_env_vars** (system): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([stats](stats/index.md)): Env var INSTAGRAM_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var INSTAGRAM_REMOTE_DEST is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MAILCHIMP_NONMEMBER_LIST_ID is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MAILCHIMP_TYL_LIST_ID is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var MARVELOUS_ADMIN_SECONDARY_PASSWORD is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_AUTH_JSON is defined but never referenced in code
- **orphan_env_vars** (system): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([announce](announce/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([stats](stats/index.md)): Env var MARVELOUS_MAGIC_URL is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var MAXMIND_LICENSE_KEY is defined but never referenced in code
- **orphan_env_vars** (system): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([stats](stats/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** ([video-editor](video-editor/index.md)): Env var NOTIFY_EMAIL_FROM is defined but never referenced in code
- **orphan_env_vars** (system): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- **orphan_env_vars** ([secrets](secrets/index.md)): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
- **orphan_env_vars** ([stats](stats/index.md)): Env var NOTIFY_EMAIL_TO is defined but never referenced in code
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
- **orphan_env_vars** ([announce](announce/index.md)): Env var VERNIO_API_KEY is defined but never referenced in code
- **orphan_env_vars** ([classes](classes/index.md)): Env var YOGA_HABIT_REGISTER_URL is defined but never referenced in code
