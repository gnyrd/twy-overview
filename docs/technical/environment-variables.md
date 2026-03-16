# Environment Variables

All secrets and configuration live in `.env` files per repo. Never hardcoded.

## twy-download (`/root/twy/download/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `ZOOM_ACCOUNT_ID` | Yes | Zoom API account ID |
| `ZOOM_CLIENT_ID` | Yes | Zoom API client ID |
| `ZOOM_CLIENT_SECRET` | Yes | Zoom API client secret |
| `TWY_CLASSES_DIR` | No | Output dir for classes (default: `data/classes`) |
| `TWY_PRIVATES_DIR` | No | Output dir for privates (default: `data/privates`) |
| `TWY_OUTTAKES_DIR` | No | Output dir for outtakes (default: `data/outtakes`) |
| `TWY_STATE_DIR` | No | State file directory (default: `download/state`) |
| `ZOOM_DAYS_BACK` | No | Days to look back (default: 7) |
| `ZOOM_MIN_DURATION` | No | Duration threshold in minutes (default: 15) |

## twy-clips (`/root/twy/clips/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `TWY_CLASSES_DIR` | Yes | Path to class recordings |
| `OPENAI_API_KEY` | Yes | OpenAI API key (segment identification) |

## twy-class-plans (`/root/twy/class-plans/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `DASHBOARD_PASS` | Yes | Single password for login |
| `FLASK_SECRET_KEY` | Yes | Flask session signing key |
| `TWY_DASHBOARD_PORT` | No | Port (default: 5003) |
| `TWY_CLASS_PLANS_DIR` | No | Plan JSON directory (default: `../data/class-plans`) |
| `TWY_CLASSES_DIR` | No | Class recordings directory (default: `../data/classes`) |
| `TWY_CLASS_VIDEOS_DIR` | No | Trimmed video output (default: `../data/class-videos`) |
| `TWY_BUMPERS_INTRO` | No | Intro bumper path |
| `TWY_BUMPERS_OUTRO` | No | Outro bumper path |
| `TWY_CLIPS_URL` | No | Clips dashboard URL (default: `https://clips.tiffanywood.yoga`) |

## twy-video-editor (`/root/twy/thumbnails/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `DASHBOARD_PASS` | Yes | Single password for login |
| `FLASK_SECRET_KEY` | Yes | Flask session signing key |

## twy-tweee-gpt (`.mailchimp.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `MAILCHIMP_API_KEY` | Yes | Mailchimp API key |
| `MAILCHIMP_SERVER_PREFIX` | Yes | Mailchimp server (e.g., `us21`) |

## twy-announce (`/root/twy/announce/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_DRIVE_CREDENTIALS_PATH` | Yes | Google Drive API credentials JSON |
| `GOOGLE_DRIVE_DOCUMENT_ID` | Yes | Class schedule document ID |
| `SMTP_SERVER` | Yes | Email SMTP server |
| `SMTP_PORT` | Yes | SMTP port (typically 587) |
| `SMTP_USERNAME` | Yes | SMTP username |
| `SMTP_PASSWORD` | Yes | SMTP password |
| `SMTP_FROM` | Yes | From address |
| `SMTP_TO` | Yes | Recipient address(es) |
| `SLACK_WEBHOOK_URL` | Yes | Slack incoming webhook |
| `MARVELOUS_TWY_USERNAME` | Yes | HeyMarvelous login email |
| `MARVELOUS_TWY_PASSWORD` | Yes | HeyMarvelous login password |
| `MARVELOUS_SECONDARY_PASSWORD` | Yes | HeyMarvelous unlock password |
| `MAILCHIMP_API_KEY` | Yes | Mailchimp API key |
| `MAILCHIMP_AUDIENCE_ID` | Yes | Mailchimp audience/list ID |
| `YOUTUBE_API_KEY` | Yes | YouTube Data API key |
| `YOUTUBE_CHANNEL_ID` | Yes | YouTube channel ID |
| `YOUTUBE_REMOTE_DEST` | No | SCP destination for YouTube data |
| `INSTAGRAM_REMOTE_DEST` | No | SCP destination for Instagram data |
| `WHATSAPP_SESSION_PATH` | No | WhatsApp session storage |
| `WHATSAPP_GROUP_ID` | No | WhatsApp target group |
| `REMINDER_OFFSETS` | No | Hours before class to send reminder (default: 26) |

## twy-overview (`/root/twy/overview/.env.docs` and `.env.tech`)

| Variable | Required | Description |
|----------|----------|-------------|
| `DASHBOARD_PASS` | Yes | Single password for login |
| `FLASK_SECRET_KEY` | Yes | Flask session signing key |
| `DOCS_DIR` | Yes | Path to markdown docs directory |
| `SITE_TITLE` | Yes | Display title for the site |
| `TWY_DOCS_PORT` | Yes | Port (5005 for docs, 5006 for tech) |

## twy-asset-management (`/root/twy/asset-management/.env`)

| Variable | Required | Description |
|----------|----------|-------------|
| `CLOUDINARY_URL` | No | Cloudinary connection string |
