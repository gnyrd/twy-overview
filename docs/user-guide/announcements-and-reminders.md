# Announcements and Reminders

twy-announce handles automated communications: email class reminders, daily Slack status reports, and optional WhatsApp posting.

## Email Class Reminders

Automated email reminders go out ~26 hours before each class.

### How It Works

1. Cron runs `scripts/run_class_email_reminders.sh` every 30 minutes on the Hetzner server
2. The script loads `.env` and runs `scripts/send_class_email_reminders.py`
3. It reads the class schedule from a Google Doc (auto-detects the current month's tab)
4. For each upcoming class, if a reminder hasn't been sent yet (checked via `data/reminder_state.json`), it sends an email
5. The email includes: class title, description, affirmation, apex pose, and join link

### How Do I...

#### Check if reminders are running

```bash
# Check cron
crontab -l | grep reminder

# Check recent logs
tail -50 /root/twy/announce/logs/reminders.log

# Check reminder state
cat /root/twy/announce/data/reminder_state.json | python3 -m json.tool
```

#### Test a reminder without sending

```bash
cd /root/twy/announce
REMINDER_OFFSETS=26 ./scripts/run_class_email_reminders.sh --now 2026-03-15T06:05
```

#### Force re-send a reminder

Back up and delete the state file, then re-run:

```bash
cd /root/twy/announce
mv data/reminder_state.json data/reminder_state_backup.json
REMINDER_OFFSETS=26 ./scripts/run_class_email_reminders.sh
```

## Daily Slack Status Report

A daily report posts to Slack at 6am Mountain Time with:

- **Subscribers**: Email (Mailchimp), Instagram, YouTube counts with week/month/year deltas
- **Membership**: Active subscription counts from HeyMarvelous (Marvelous) with per-product breakdowns
- **Revenue**: Monthly/annual billing cycle counts

### Data Sources

| Metric | Source | Fetch Script |
|--------|--------|-------------|
| Email subscribers | Mailchimp API | `src/mailchimp_subscriber_data.py` |
| Instagram followers | Instaloader | `src/instagram_follower_data.py` |
| YouTube subscribers | YouTube Data API v3 | `src/youtube_subscriber_data.py` |
| Membership data | HeyMarvelous Metabase | `src/daily_status_report.py` (via JWT) |

### How Do I...

#### Check the daily report

Look in Slack, or run it manually:

```bash
cd /root/twy/announce
python3 src/daily_status_report.py
```

#### Fix the JWT token

The Marvelous JWT is refreshed automatically by `src/refresh_jwt.py` (runs as part of the daily report). Tokens last ~7 days.

If the token expires:

```bash
cd /root/twy/announce
python3 src/refresh_jwt.py
```

This opens a headless browser, logs into HeyMarvelous, and extracts a fresh JWT.

## WhatsApp (Optional Toolbox)

WhatsApp posting tools exist but are optional. The main communication channel is email.

```bash
# Authenticate
node whatsapp_bot.js auth

# Send a test message
node whatsapp_bot.js test

# List available groups
node list_groups.js
```

> ⚠️ WhatsApp automation uses an unofficial API and may trigger account restrictions. Use with caution.
