# Environment Variables

| Variable | Defined In | Referenced In | Status |
|----------|-----------|---------------|--------|
| `ANTHROPIC_API_KEY` |  (/root/twy/.env), clips, clips (/root/twy/clips/.env), secrets (/root/twy/secrets/.env), video-editor (/root/twy/video-editor/.env) | clips (/root/twy/clips/src/utils/ai_analyzer.py) | ✅ OK |
| `API_TOKEN` | - | classes (/root/twy/classes/scripts/duplicate_recordings.py), classes (/root/twy/classes/scripts/sync.py), marvy (/root/twy/marvy/examples/02_list_events.py), marvy (/root/twy/marvy/examples/basic_usage.py), marvy (/root/twy/marvy/examples/export_events_csv.py) | ⚠️ Undefined |
| `ASPECT_RATIO` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `CAPTIONED_SUBDIR` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `CLIPS_SUBDIR` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `DASHBOARD_PASS` |  (/root/twy/.env), classes, classes (/root/twy/classes/.env), clips, clips (/root/twy/clips/.env), data-viewer, overview, secrets (/root/twy/secrets/.env), video-editor, video-editor (/root/twy/video-editor/.env) | classes (/root/twy/classes/dashboard/auth.py), clips (/root/twy/clips/src/web/dashboard.py), data-viewer (/root/twy/data-viewer/app.py), overview (/root/twy/overview/auth.py), video-editor (/root/twy/video-editor/src/dashboard-archive/dashboard.py), video-editor (/root/twy/video-editor/src/dashboard/dashboard.py) | ✅ OK |
| `DIANES_OTP_EMAIL` | download (/root/twy/download/.env) | download (/root/twy/download/src/dianes_sharepoint_client.py) | ✅ OK |
| `DIANES_SHAREPOINT_SHARE_URL` | download (/root/twy/download/.env) | download (/root/twy/download/src/dianes_sharepoint_client.py) | ✅ OK |
| `DOCS_DIR` | - | overview (/root/twy/overview/app.py) | ⚠️ Undefined |
| `DRY_RUN` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `EMAIL_FROM` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `EMAIL_TO` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `EXTRACTED_SUBDIR` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `FLASK_PORT` | clips (/root/twy/clips/.env) | clips (/root/twy/clips/src/web/dashboard.py) | ✅ OK |
| `FLASK_SECRET_KEY` |  (/root/twy/.env), classes, classes (/root/twy/classes/.env), clips, clips (/root/twy/clips/.env), data-viewer, overview, secrets (/root/twy/secrets/.env), video-editor, video-editor (/root/twy/video-editor/.env) | classes (/root/twy/classes/dashboard/app.py), clips (/root/twy/clips/src/web/dashboard.py), data-viewer (/root/twy/data-viewer/app.py), overview (/root/twy/overview/app.py), video-editor (/root/twy/video-editor/src/dashboard-archive/dashboard.py), video-editor (/root/twy/video-editor/src/dashboard/dashboard.py) | ✅ OK |
| `GITHUB_WEBHOOK_SECRET` | - | overview (/root/twy/overview/app.py) | ⚠️ Undefined |
| `GOOGLE_DOC_ID` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `HM_DASHBOARD_PORT` | video-editor (/root/twy/video-editor/.env) | video-editor (/root/twy/video-editor/src/dashboard-archive/dashboard.py) | ✅ OK |
| `INSTAGRAM_ACCOUNT` |  (/root/twy/.env), announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | - | 🔵 Orphan |
| `INSTAGRAM_HISTORY_DIR` | - | announce (/root/twy/announce/src/instagram_follower_data.py) | ⚠️ Undefined |
| `INSTAGRAM_PASSWORD` |  (/root/twy/.env), announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | - | 🔵 Orphan |
| `INSTAGRAM_PROFILE` | - | announce (/root/twy/announce/src/instagram_follower_data.py) | ⚠️ Undefined |
| `INSTAGRAM_REMOTE_DEST` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `INSTAGRAM_SESSION_FILE` | - | announce (/root/twy/announce/src/instagram_follower_data.py) | ⚠️ Undefined |
| `MAILCHIMP_API_KEY` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), classes, classes (/root/twy/classes/.env), secrets (/root/twy/secrets/.env), tweee-gpt | announce (/root/twy/announce/src/mailchimp_campaigns.py), announce (/root/twy/announce/src/mailchimp_subscriber_data.py), announce (/root/twy/announce/src/run_campaigns.py), announce (/root/twy/announce/src/run_habit_followup.py), announce (/root/twy/announce/src/sync_mailchimp.py), announce (/root/twy/announce/src/track_redemptions.py), classes (/root/twy/classes/dashboard/config.py), tweee-gpt (/root/twy/tweee-gpt/send_to_mailchimp.py) | ✅ OK |
| `MAILCHIMP_AUDIENCE_ID` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), classes, secrets (/root/twy/secrets/.env), tweee-gpt | announce (/root/twy/announce/src/mailchimp_subscriber_data.py), announce (/root/twy/announce/src/run_habit_followup.py), announce (/root/twy/announce/src/sync_mailchimp.py), announce (/root/twy/announce/src/track_redemptions.py), classes (/root/twy/classes/dashboard/config.py), tweee-gpt (/root/twy/tweee-gpt/send_to_mailchimp.py) | ✅ OK |
| `MAILCHIMP_FROM_NAME` | - | tweee-gpt (/root/twy/tweee-gpt/send_to_mailchimp.py) | ⚠️ Undefined |
| `MAILCHIMP_NONMEMBER_LIST_ID` | classes (/root/twy/classes/.env) | - | 🔵 Orphan |
| `MAILCHIMP_REPLY_TO` | - | tweee-gpt (/root/twy/tweee-gpt/send_to_mailchimp.py) | ⚠️ Undefined |
| `MAILCHIMP_SERVER` | - | tweee-gpt (/root/twy/tweee-gpt/send_to_mailchimp.py) | ⚠️ Undefined |
| `MAILCHIMP_SERVER_PREFIX` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), classes, classes (/root/twy/classes/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/mailchimp_campaigns.py), announce (/root/twy/announce/src/run_campaigns.py), announce (/root/twy/announce/src/run_habit_followup.py), announce (/root/twy/announce/src/track_redemptions.py), classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `MAILCHIMP_TEMPLATE_CAMPAIGN_ID` |  (/root/twy/.env), announce, classes, secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/mailchimp_campaigns.py), classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `MAILCHIMP_TYL_LIST_ID` | classes (/root/twy/classes/.env) | - | 🔵 Orphan |
| `MARVELOUS_ACTIVE_SUBSCRIPTIONS_CSV` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_ACTIVE_SUBS_REPORT_CATEGORY` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_ACTIVE_SUBS_REPORT_ID` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_ADMIN_PASSWORD` | classes (/root/twy/classes/.env) | classes (/root/twy/classes/dashboard/marvelous.py) | ✅ OK |
| `MARVELOUS_ADMIN_SECONDARY_PASSWORD` | classes (/root/twy/classes/.env) | - | 🔵 Orphan |
| `MARVELOUS_ADMIN_USERNAME` | classes (/root/twy/classes/.env) | classes (/root/twy/classes/dashboard/marvelous.py) | ✅ OK |
| `MARVELOUS_AUTH_JSON` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `MARVELOUS_CANCELED_SUBSCRIPTIONS_CSV` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_CANCELED_SUBS_REPORT_CATEGORY` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_CANCELED_SUBS_REPORT_ID` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_EVENTS_PATH` | video-editor (/root/twy/video-editor/.env) | announce (/root/twy/announce/scripts/refresh_marvelous_events.py), announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `MARVELOUS_EXTRA_HEADERS_JSON` | - | announce (/root/twy/announce/scripts/refresh_marvelous_events.py) | ⚠️ Undefined |
| `MARVELOUS_FORCE_JWT_REFRESH` | - | announce (/root/twy/announce/src/sync_mailchimp.py) | ⚠️ Undefined |
| `MARVELOUS_LOOKAHEAD_DAYS` | - | announce (/root/twy/announce/scripts/refresh_marvelous_events.py) | ⚠️ Undefined |
| `MARVELOUS_MAGIC_URL` |  (/root/twy/.env), announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | - | 🔵 Orphan |
| `MARVELOUS_PASSWORD` |  (/root/twy/.env), announce, classes, secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/run_habit_followup.py), classes (/root/twy/classes/scripts/create_next_habit_event.py), classes (/root/twy/classes/scripts/sync.py) | ✅ OK |
| `MARVELOUS_SECONDARY_PASSWORD` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/marvelous_report_jwt.py), announce (/root/twy/announce/src/refresh_jwt.py) | ✅ OK |
| `MARVELOUS_TOKEN` | - | announce (/root/twy/announce/examples/marvelous_example.py) | ⚠️ Undefined |
| `MARVELOUS_TWY_PASSWORD` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/src/marvelous_report_jwt.py), announce (/root/twy/announce/src/refresh_jwt.py) | ✅ OK |
| `MARVELOUS_TWY_USERNAME` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/src/marvelous_report_jwt.py), announce (/root/twy/announce/src/refresh_jwt.py) | ✅ OK |
| `MARVELOUS_USERNAME` |  (/root/twy/.env), announce, classes, secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/run_habit_followup.py), classes (/root/twy/classes/scripts/create_next_habit_event.py), classes (/root/twy/classes/scripts/sync.py) | ✅ OK |
| `MARVY_AUTH_FILE` |  (/root/twy/.env), classes, secrets (/root/twy/secrets/.env) | classes (/root/twy/classes/dashboard/marvelous.py), classes (/root/twy/classes/dashboard/views.py), classes (/root/twy/classes/scripts/monthly_series_workflow.py), classes (/root/twy/classes/scripts/post_recording_workflow.py), classes (/root/twy/classes/scripts/remove_thumbnail.py), classes (/root/twy/classes/scripts/replace_video.py) | ✅ OK |
| `MAXMIND_LICENSE_KEY` | secrets (/root/twy/secrets/.env) | - | 🔵 Orphan |
| `MC_ENV_PATH` | - | docs-scanner (/root/twy/docs-scanner/tests/test_mc_client.py), docs-scanner (/root/twy/docs-scanner/twy_docs/mc/client.py) | ⚠️ Undefined |
| `NOTIFY_EMAIL_FROM` |  (/root/twy/.env), secrets (/root/twy/secrets/.env), video-editor (/root/twy/video-editor/.env) | - | 🔵 Orphan |
| `NOTIFY_EMAIL_TO` |  (/root/twy/.env), secrets (/root/twy/secrets/.env), video-editor (/root/twy/video-editor/.env) | - | 🔵 Orphan |
| `OPENAI_API_KEY` |  (/root/twy/.env), clips, clips (/root/twy/clips/.env), secrets (/root/twy/secrets/.env), video-editor (/root/twy/video-editor/.env) | clips (/root/twy/clips/src/utils/ai_analyzer.py) | ✅ OK |
| `OUTPUT_FILE` | - | marvy (/root/twy/marvy/examples/export_events_csv.py) | ⚠️ Undefined |
| `PARTICIPANTS_FILE` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `REMINDER_OFFSETS` | - | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ⚠️ Undefined |
| `REMINDER_STATE_PATH` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `SITE_TITLE` | - | overview (/root/twy/overview/app.py) | ⚠️ Undefined |
| `SLACK_BOT_TOKEN` |  (/root/twy/.env), announce, classes, classes (/root/twy/classes/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/scripts/notify_on_failure.py), announce (/root/twy/announce/src/daily_status_report.py), announce (/root/twy/announce/src/slack.py), classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `SLACK_CHANNEL` | - | announce (/root/twy/announce/src/daily_status_report.py) | ⚠️ Undefined |
| `SLACK_REVIEW_CHANNEL` |  (/root/twy/.env), announce, classes, classes (/root/twy/classes/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/run_habit_followup.py), classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `SLACK_STATUS_CHANNEL` |  (/root/twy/.env), announce, classes, classes (/root/twy/classes/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/generate_newsletter_prompts.py), announce (/root/twy/announce/src/run_campaigns.py), classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `SLACK_USER_JP` | secrets (/root/twy/secrets/.env) | classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `SLACK_USER_TIFF` | secrets (/root/twy/secrets/.env) | classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `SLACK_VIDEO_WEBHOOK_URL` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/src/class_video_notifier.py) | ✅ OK |
| `SLACK_WEBHOOK_URL` | announce (/root/twy/announce/.env) | announce (/root/twy/announce/src/daily_status_report.py) | ✅ OK |
| `SRT_SUBDIR` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `STUDIO_SLUG` | - | marvy (/root/twy/marvy/examples/02_list_events.py), marvy (/root/twy/marvy/examples/export_events_csv.py) | ⚠️ Undefined |
| `THUMBNAIL_SUFFIX` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `TIMEZONE` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/scripts/send_class_email_reminders.py) | ✅ OK |
| `TRELLO_API_KEY` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `TRELLO_BOARD_ID` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `TRELLO_TOKEN` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `TWY_BUMPERS_INTRO` | - | classes (/root/twy/classes/dashboard/config.py) | ⚠️ Undefined |
| `TWY_BUMPERS_OUTRO` | - | classes (/root/twy/classes/dashboard/config.py) | ⚠️ Undefined |
| `TWY_CLASSES_DIR` | classes (/root/twy/classes/.env), clips (/root/twy/clips/.env), video-editor (/root/twy/video-editor/.env) | - | 🔵 Orphan |
| `TWY_CLASS_PLANS_DIR` | classes (/root/twy/classes/.env) | - | 🔵 Orphan |
| `TWY_CLASS_VIDEOS_DIR` | - | classes (/root/twy/classes/dashboard/config.py) | ⚠️ Undefined |
| `TWY_CLIPS_URL` | - | classes (/root/twy/classes/dashboard/config.py) | ⚠️ Undefined |
| `TWY_DASHBOARD_PORT` | classes (/root/twy/classes/.env) | classes (/root/twy/classes/dashboard/config.py) | ✅ OK |
| `TWY_DATA_DIR` |  (/root/twy/.env), paths, secrets (/root/twy/secrets/.env) | paths (/root/twy/paths/twy_paths/paths.py) | ✅ OK |
| `TWY_DOCS_DB` | - | docs-scanner (/root/twy/docs-scanner/twy_docs/db.py) | ⚠️ Undefined |
| `TWY_DOCS_PORT` | - | overview (/root/twy/overview/app.py) | ⚠️ Undefined |
| `TWY_ENV_PATH` | - | paths (/root/twy/paths/twy_paths/env.py) | ⚠️ Undefined |
| `TWY_NOTIFY_EMAIL` | download (/root/twy/download/.env) | download (/root/twy/download/src/dianes_cleanup.py) | ✅ OK |
| `TWY_PROJECTS_ROOT` | - | docs-scanner (/root/twy/docs-scanner/twy_docs/config.py) | ⚠️ Undefined |
| `TWY_PROJECT_DIR` | clips (/root/twy/clips/.env), download (/root/twy/download/.env) | - | 🔵 Orphan |
| `TWY_REPORTER_BOT_TOKEN` |  (/root/twy/.env), announce | announce (/root/twy/announce/scripts/notify_on_failure.py) | ✅ OK |
| `TWY_STATE_DIR` | clips (/root/twy/clips/.env), download (/root/twy/download/.env) | clips (/root/twy/clips/src/ig/state.py), clips (/root/twy/clips/src/wa/state.py), clips (/root/twy/clips/src/yt/state.py), download (/root/twy/download/src/zoom/zoom_list.py) | ✅ OK |
| `TWY_THUMBNAIL_SCRIPT` | - | classes (/root/twy/classes/dashboard/config.py) | ⚠️ Undefined |
| `UNCAPTIONED_SUBDIR` | clips (/root/twy/clips/.env) | - | 🔵 Orphan |
| `VAR` | - | docs-scanner (/root/twy/docs-scanner/twy_docs/collectors/env_collector.py) | ⚠️ Undefined |
| `VERNIO_API_KEY` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `VIDEO_EDITOR_PORT` | video-editor (/root/twy/video-editor/.env) | video-editor (/root/twy/video-editor/src/dashboard/dashboard.py) | ✅ OK |
| `WATCHDOG_SCAN_DAYS` | - | download (/root/twy/download/src/zoom/zoom_download_watchdog.py) | ⚠️ Undefined |
| `YOGA_HABIT_REGISTER_URL` | classes (/root/twy/classes/.env) | - | 🔵 Orphan |
| `YOUTUBE_API_KEY` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/youtube_subscriber_data.py) | ✅ OK |
| `YOUTUBE_CHANNEL_ID` |  (/root/twy/.env), announce, announce (/root/twy/announce/.env), secrets (/root/twy/secrets/.env) | announce (/root/twy/announce/src/youtube_subscriber_data.py) | ✅ OK |
| `YOUTUBE_HISTORY_DIR` | - | announce (/root/twy/announce/src/youtube_subscriber_data.py) | ⚠️ Undefined |
| `YOUTUBE_REMOTE_DEST` | announce (/root/twy/announce/.env) | - | 🔵 Orphan |
| `ZOOM_ACCOUNT_ID` |  (/root/twy/.env), download, download (/root/twy/download/.env), secrets (/root/twy/secrets/.env) | download (/root/twy/download/src/classes_archive.py), download (/root/twy/download/src/dianes_cleanup.py), download (/root/twy/download/src/zoom/zoom_download_watchdog.py) | ✅ OK |
| `ZOOM_CLIENT_ID` |  (/root/twy/.env), download, download (/root/twy/download/.env), secrets (/root/twy/secrets/.env) | download (/root/twy/download/src/classes_archive.py), download (/root/twy/download/src/dianes_cleanup.py), download (/root/twy/download/src/zoom/zoom_download_watchdog.py) | ✅ OK |
| `ZOOM_CLIENT_SECRET` |  (/root/twy/.env), download, download (/root/twy/download/.env), secrets (/root/twy/secrets/.env) | download (/root/twy/download/src/classes_archive.py), download (/root/twy/download/src/dianes_cleanup.py), download (/root/twy/download/src/zoom/zoom_download_watchdog.py) | ✅ OK |
| `ZOOM_DAYS_BACK` | download (/root/twy/download/.env) | download (/root/twy/download/src/zoom/zoom_download.backup.py), download (/root/twy/download/src/zoom/zoom_download.py), download (/root/twy/download/src/zoom/zoom_download_classes.py), download (/root/twy/download/src/zoom/zoom_download_privates.py), download (/root/twy/download/src/zoom/zoom_download_shorts.py), download (/root/twy/download/src/zoom/zoom_list.py) | ✅ OK |
| `ZOOM_MIN_DURATION` | download (/root/twy/download/.env) | download (/root/twy/download/src/zoom/zoom_download.backup.py), download (/root/twy/download/src/zoom/zoom_download_classes.py), download (/root/twy/download/src/zoom/zoom_download_shorts.py) | ✅ OK |
