# Cron Schedule

All times shown as cron expressions (server runs in UTC; MT = UTC-6/UTC-7).

| Schedule | Project | Description | Failure Wrapper | Log |
|----------|---------|-------------|-----------------|-----|
| `*/5 * * * *` | [clips](clips/index.md) | cd /root/twy/clips && ./src/pipeline/class_recording_watchdog.sh >> logs/watchdog.log 2>&1 | ❌ | - |
| `*/5 * * * *` | [video-editor](video-editor/index.md) | cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data/logs/thumbnail_watchdog.log 2>&1 | ❌ | - |
| `*/5 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ../data/logs/zoom_download_watchdog.log  | ❌ | - |
| `*/5 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/class_video_notifier.py >> /root/twy/data/logs/class_video_notifier.log 2> | ❌ | `/root/twy/data/logs/class_video_notifier.log` |
| `0 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/refresh_jwt.py >> logs/jwt_refresh.log 2>&1 | ❌ | - |
| `0 1 * * *` | [announce](announce/index.md) | cd /root/twy/announce && ./scripts/run_mailchimp_sync.sh | ❌ | - |
| `0 10 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs/classes_archive.log 2>&1 | ❌ | - |
| `0 10 1 * *` | [yoga-habit](yoga-habit/index.md) | /root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2_refresh.log 2>&1 | ❌ | `/root/twy/data/logs/geolite2_refresh.log` |
| `0 13 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/daily_report.log 2>&1 | ❌ | - |
| `0 13 28 * *` | [classes](classes/index.md) | cd /root/twy/classes && /usr/bin/python3 scripts/create_next_habit_event.py >> /root/twy/data/logs/habit-event.log 2>&1 | ❌ | `/root/twy/data/logs/habit-event.log` |
| `0 8 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../data/logs/dianes_upload.log 2>&1 | ❌ | - |
| `0 8 * * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py hm-placeholder-topup /usr/bin/python3 scripts/hm | ✅ | `/root/twy/data/logs/hm_placeholders_cron.log` |
| `0 8 1 * *` | [classes](classes/index.md) | cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /root/twy/data/logs/monthly_series.log 2> | ❌ | `/root/twy/data/logs/monthly_series.log` |
| `0 8 7 * *` | [classes](classes/index.md) | cd /root/twy/classes && /usr/bin/python3 scripts/monthly_series_workflow.py >> /root/twy/data/logs/monthly_series.log 2> | ❌ | `/root/twy/data/logs/monthly_series.log` |
| `0 9 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/dianes_cleanup.log 2>&1 | ❌ | - |
| `0 9 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/generate_newsletter_prompts.py >> /root/twy/data/logs/newsletter_prompts.l | ❌ | `/root/twy/data/logs/newsletter_prompts.log` |
| `0 9,18 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >> logs/marvelous_sync.log 2>&1 | ❌ | - |
| `15,45 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back 1 >> ../data/logs/zoom_download.log 2>&1 | ❌ | - |
| `5 7 * * *` | [classes](classes/index.md) | cd /root/twy/classes && /usr/bin/python3 scripts/sync.py --db /root/twy/data/marvy.db >> /root/twy/data/logs/marvy_sync. | ❌ | `/root/twy/data/logs/marvy_sync.log` |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/mailchimp_subscriber_data.py >> logs/mailchimp.log 2>&1 | ❌ | - |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1 | ❌ | - |
