# twy-announce

Automated communications: email class reminders, daily Slack status reports, social media tracking, and WhatsApp toolbox.

**Repo:** `gnyrd/twy-announce` → `/root/twy/announce/`

## Components

### Email Class Reminders (Python, cron)

Sends reminder emails ~26 hours before each class.

**Entry point:** `scripts/run_class_email_reminders.sh` → `scripts/send_class_email_reminders.py`

**Flow:**
1. Reads class schedule from Google Doc (auto-detects current month tab via Google Docs API `includeTabsContent=True`)
2. Parses class entries — supports both `"Monday, Jan 5 — Title"` and `"FEB 2 – Title"` formats
3. Checks `data/reminder_state.json` for already-sent reminders
4. For each unsent reminder within the offset window: builds email, sends via SMTP
5. Updates state file

**Cron:** `*/30 * * * * cd /root/twy/announce && REMINDER_OFFSETS=26 ./scripts/run_class_email_reminders.sh >> logs/reminders.log 2>&1`

### Daily Slack Status Report (Python, cron)

Posts subscriber counts and membership data to Slack at 6am MT.

**Entry point:** `src/daily_status_report.py`

**Data pipeline:**

| Script | Source | Data | Storage |
|--------|--------|------|---------|
| `src/mailchimp_subscriber_data.py` | Mailchimp API | Email subscriber count | `data/mailchimp/history/{date}.json` |
| `src/instagram_follower_data.py` | Instaloader | IG follower count | `data/instagram/history/{date}.json` |
| `src/youtube_subscriber_data.py` | YouTube Data API v3 | YT subscriber/view/video counts | `data/youtube/history/{date}.json` |
| `src/refresh_jwt.py` | Playwright → HeyMarvelous | JWT token for Metabase | `.jwt_cache.json` |
| `src/daily_status_report.py` | HeyMarvelous Metabase | Active subscriptions by product | Slack webhook |

Historical comparisons: week-over-week (7d), month-over-month (30d), year-over-year (365d).

**Cron:** `0 13 * * * cd /root/twy/announce && python3 src/daily_status_report.py` (1pm UTC = 6am MT)

### Marvelous Event Sync (Python, cron)

Refreshes HeyMarvelous event data twice daily.

**Cron:** `0 9,18 * * * cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >> logs/marvelous_sync.log 2>&1`

### Social Media Data Fetch (shell + Python, cron)

Each runs hourly, skips if today's file exists (effective once-per-day):

- `src/instagram_daily.sh` → `src/instagram_follower_data.py` (must run from non-datacenter IP)
- `src/youtube_daily.sh` → `src/youtube_subscriber_data.py`

### WhatsApp Toolbox (Node.js, manual)

Optional CLI tools — not part of automated pipeline.

- `node whatsapp_bot.js auth` — QR code authentication
- `node whatsapp_bot.js test` — send test message
- `node whatsapp_bot.js post "Message"` — post to group
- `node list_groups.js` — list available groups
- `node src/send_to_whatsapp.js "Group Name" "Message"` — one-off post

Uses `whatsapp-web.js` (unofficial API).

## JWT Refresh

`src/refresh_jwt.py` manages HeyMarvelous JWT tokens:

1. Checks cached token expiry (`TOKEN_REFRESH_BUFFER_HOURS = 24`)
2. If valid, skips refresh
3. If expired: launches headless Chromium via Playwright
4. Logs in at `app.heymarvelous.com/login` (email → password → secondary password → unlock)
5. Navigates to Reports → extracts JWT from report iframe
6. Caches to `.jwt_cache.json`

Tokens last ~7 days. Refresh runs automatically as part of `daily_status_report.py`.

## Key Paths

```
scripts/
├── run_class_email_reminders.sh    # Cron entry point
├── send_class_email_reminders.py   # Reminder logic
└── refresh_marvelous_events.py     # Event sync

src/
├── daily_status_report.py          # Slack report
├── refresh_jwt.py                  # JWT automation
├── mailchimp_subscriber_data.py
├── instagram_follower_data.py
├── youtube_subscriber_data.py
├── instagram_daily.sh              # Wrapper (cron)
└── youtube_daily.sh                # Wrapper (cron)

data/
├── reminder_state.json             # Sent reminder tracking
├── mailchimp/history/              # Daily snapshots
├── instagram/history/
├── youtube/history/
└── marvelous/history/
```
