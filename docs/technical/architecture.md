# Architecture

## Infrastructure

Everything runs on a single Hetzner server at `/root/twy/`. All repos are cloned as sibling directories sharing a common `data/` directory.

```
/root/twy/
├── download/          → twy-download (Zoom API → files)
├── clips/             → twy-clips (pipeline + dashboard)
├── class-plans/       → twy-class-plans (Flask dashboard)
├── thumbnails/        → twy-video-editor (thumbnail generation)
├── tweee-gpt/         → twy-tweee-gpt (GPT config + knowledge)
├── announce/          → twy-announce (email reminders + reports)
├── asset-management/  → twy-asset-management (asset org + pose detection)
├── marvy/             → HeyMarvelous API client library (shared)
├── data/
│   ├── classes/       → Downloaded class recordings + clips
│   ├── privates/      → Downloaded private recordings
│   ├── outtakes/      → Short recordings (< 15 min)
│   ├── class-plans/   → JSON plan files (one per class date)
│   ├── class-videos/  → Trimmed + bumpered output videos
│   └── monthly-overview.json
└── video-editor/      → Bumper source files (intro + outro mp4)
```

## Data Flow

```
Zoom Cloud Recordings
        │
        ▼
┌──────────────┐     cron / watchdog
│ twy-download │────────────────────────┐
└──────────────┘                        │
        │                               │
        ▼                               ▼
  data/classes/                   data/privates/
  data/outtakes/
        │
        ▼ (watchdog, every 5 min)
┌──────────────┐
│  twy-clips   │ → AI segments → extract → captions → thumbnails
└──────────────┘
        │
        ▼
  clips/9x16/captioned/
  clips/9x16/uncaptioned/
        │
        ├──────────────────────────────┐
        ▼                              ▼
┌────────────────┐            ┌────────────────┐
│twy-class-plans │            │twy-video-editor│
│  (Flask :5003) │            │  (Flask :5004)  │
└────────────────┘            └────────────────┘
   │          │                       │
   │          ▼                       ▼
   │   Trim & Publish          Thumbnail gen
   │   (ffmpeg → Vimeo)        (twy-auto-thumbnail)
   │
   ├── /api/plans/* ──────────┐
   │                          ▼
   │                   ┌──────────────┐
   │                   │twy-tweee-gpt │ (Custom GPT on ChatGPT)
   │                   └──────────────┘
   │                          │
   │                          ▼
   │                   Newsletter → Mailchimp
   │
   ▼
HeyMarvelous (Namastream API)
   │
   ▼
┌──────────────┐
│ twy-announce │ → Email reminders (cron)
│              │ → Daily Slack report
│              │ → WhatsApp (optional)
└──────────────┘
```

## Web Services

| Service | Port | URL | systemd Unit |
|---------|------|-----|-------------|
| Class Plans Dashboard | 5003 | `classes.tiffanywood.yoga` | `twy-class-dashboard` |
| Thumbnails Dashboard | 5004 | `classes.tiffanywood.yoga/thumbnails/` | `twy-thumbnails` |
| Clips Dashboard | — | `clips.tiffanywood.yoga` | — |
| Docs (this site) | 5005 | `docs.tiffanywood.yoga` | `twy-docs` |

All behind nginx reverse proxy with Let's Encrypt SSL.

## Shared Dependencies

### marvy (HeyMarvelous Client)

Located at `/root/twy/marvy/`. Reverse-engineered Python client for the undocumented HeyMarvelous (Namastream) API. Used by:

- **twy-class-plans**: publish/unpublish events, post-recording workflow, media library
- **twy-announce**: daily status report (subscription data via Metabase JWT)

### Data Directory

`/root/twy/data/` is shared across multiple services:

- **twy-download** writes to `classes/`, `privates/`, `outtakes/`
- **twy-clips** reads from `classes/`, writes clips into each class directory
- **twy-class-plans** reads/writes `class-plans/` (JSON), reads `classes/` (recordings), writes `class-videos/` (trimmed output)
- **twy-video-editor** reads from `classes/` (for thumbnail generation)

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.x (primary), Node.js (WhatsApp toolbox) |
| Web framework | Flask |
| Video processing | FFmpeg, OpenCV |
| Speech-to-text | Whisper |
| AI/ML | OpenAI API (segment identification), MediaPipe (pose detection) |
| Platform integrations | Zoom API, Vimeo (TUS upload), HeyMarvelous/Namastream, Mailchimp, YouTube Data API, Google Docs API |
| Browser automation | Playwright (JWT refresh) |
| Infrastructure | Hetzner VPS, systemd, nginx, Let's Encrypt, cron |
