# Cron Schedule

All times shown as cron expressions (server runs in UTC; MT = UTC-6/UTC-7).

| Schedule | Project | Description | Failure Wrapper | Log |
|----------|---------|-------------|-----------------|-----|
| `*/5 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | `/root/twy/data/logs/class_video_notifier.log` |
| `*/5 * * * *` | [clips](clips/index.md) | cd /root/twy/clips && ./src/pipeline/class_recordi | ❌ | - |
| `*/5 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom | ❌ | - |
| `*/5 * * * *` | [video-editor](video-editor/index.md) | cd /root/twy/video-editor && /usr/bin/python3 src/ | ❌ | - |
| `0 * * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | - |
| `0 1 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | - |
| `0 10 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/clas | ❌ | - |
| `0 10 1 * *` | [yoga-habit](yoga-habit/index.md) | /root/twy/yoga-habit/scripts/refresh_geolite2.sh > | ❌ | `/root/twy/data/logs/geolite2_refresh.log` |
| `0 13 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /usr/bin/python3 src/dail | ❌ | - |
| `0 13 28 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/habit-event.log` |
| `0 15 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | `/root/twy/data/logs/habit_redemptions.log` |
| `0 17 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | `/root/twy/data/logs/habit_followup.log` |
| `0 8 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dian | ❌ | - |
| `0 8 1 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/monthly_series.log` |
| `0 8 7 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/monthly_series.log` |
| `0 9 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | `/root/twy/data/logs/newsletter_prompts.log` |
| `0 9 * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/dian | ❌ | - |
| `0 9 * * 0` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `0 9,18 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | - |
| `15,45 * * * *` | [download](download/index.md) | cd /root/twy/download && /usr/bin/python3 src/zoom | ❌ | - |
| `30 10 1 * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `5 7 * * *` | [announce](announce/index.md) | cd /root/twy/classes && /root/twy/announce/scripts | ✅ | `/root/twy/data/logs/marvy_sync.log` |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && /root/twy/announce/script | ✅ | - |
| `55 11 * * *` | [announce](announce/index.md) | cd /root/twy/announce && ./src/youtube_daily.sh >> | ❌ | - |
