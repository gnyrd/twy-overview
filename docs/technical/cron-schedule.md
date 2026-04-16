# Cron Schedule

All times shown as cron expressions (server runs in UTC; MT = UTC-6/UTC-7).

| Schedule | Project | Description | Failure Wrapper | Log |
|----------|---------|-------------|-----------------|-----|
| `*/5 * * * *` | [clips](clips/index.md) | cd /root/twy/clips && ./src/pipeline/class_recording_watchdog.sh >> logs/watchdog.log 2>&1 | ❌ | - |
| `*/5 * * * *` | [video-editor](video-editor/index.md) | cd /root/twy/video-editor && /usr/bin/python3 src/twy-thumbnail-watchdog >> data/logs/thumbnail_watchdog.log 2>&1 | ❌ | - |
| `*/5 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ../data/logs/zoom_download_watchdog.log  | ❌ | - |
| `*/5 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py class-video-notifier /usr/bin/python3 src/class | ✅ | `/root/twy/data/logs/class_video_notifier.log` |
| `0 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py refresh-jwt /usr/bin/python3 src/refresh_jwt.py | ✅ | - |
| `0 1 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py mailchimp-sync ./scripts/run_mailchimp_sync.sh | ✅ | - |
| `0 10 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs/classes_archive.log 2>&1 | ❌ | - |
| `0 10 1 * *` | [yoga-habit](yoga-habit/index.md) | /root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2_refresh.log 2>&1 | ❌ | `/root/twy/data/logs/geolite2_refresh.log` |
| `0 13 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/daily_status_report.py >> logs/daily_report.log 2>&1 | ❌ | - |
| `0 13 28 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py create-next-habit-event /usr/bin/python3 scripts | ✅ | `/root/twy/data/logs/habit-event.log` |
| `0 15 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py track-redemptions /usr/bin/python3 src/track_re | ✅ | `/root/twy/data/logs/habit_redemptions.log` |
| `0 17 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py run-habit-followup /usr/bin/python3 src/run_hab | ✅ | `/root/twy/data/logs/habit_followup.log` |
| `0 8 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../data/logs/dianes_upload.log 2>&1 | ❌ | - |
| `0 8 1 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py monthly-series-workflow /usr/bin/python3 scripts | ✅ | `/root/twy/data/logs/monthly_series.log` |
| `0 8 7 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py monthly-series-workflow /usr/bin/python3 scripts | ✅ | `/root/twy/data/logs/monthly_series.log` |
| `0 9 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/dianes_cleanup.log 2>&1 | ❌ | - |
| `0 9 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py generate-newsletter-prompts /usr/bin/python3 sr | ✅ | `/root/twy/data/logs/newsletter_prompts.log` |
| `0 9 * * 0` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py marvy-sync-weekly /usr/bin/python3 scripts/sync. | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `0 9,18 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py refresh-marvelous-events /usr/bin/python3 scrip | ✅ | - |
| `15,45 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back 1 >> ../data/logs/zoom_download.log 2>&1 | ❌ | - |
| `30 10 1 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py marvy-sync-monthly /usr/bin/python3 scripts/sync | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `5 7 * * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts/notify_on_failure.py marvy-sync-daily /usr/bin/python3 scripts/sync.p | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/scripts/notify_on_failure.py mailchimp-subscriber-data /usr/bin/python3 src/ | ✅ | - |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && ./src/youtube_daily.sh >> logs/youtube.log 2>&1 | ❌ | - |
