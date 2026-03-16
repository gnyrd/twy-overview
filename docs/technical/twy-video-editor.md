# twy-video-editor

Thumbnail generation and video bumper tools for Tiffany Wood Yoga.

**Repo:** `gnyrd/twy-video-editor` → `/root/twy/thumbnails/`
**Live:** https://classes.tiffanywood.yoga/thumbnails/ (port 5004)
**Service:** `twy-thumbnails`

## Components

### twy-auto-thumbnail

Generates thumbnail candidates for a class recording.

```bash
# Today's class
./src/twy-auto-thumbnail

# Specific date
./src/twy-auto-thumbnail 2026-02-19
```

Output: `data/classes/<date>_<type>/class_thumbnails/`
- 6 frame JPGs extracted from the video
- 6 thumbnail PNGs with text overlay (title, apex pose, date)
- `thumbnail_ranking.json` — AI ranking of candidates

### twy-add-bumpers

Concatenates intro and outro bumpers to a video.

```bash
./twy-add-bumpers
# Prompts for main video path
```

Bumper files:
- `twy_bumper_intro_720p25.mp4`
- `twy_bumper_outro_720p25.mp4`

Both H.264 1280×720 25fps AAC — matches class recording format for stream-copy concat.

### Thumbnails Dashboard

Flask app mounted at `/thumbnails/` via Werkzeug `DispatcherMiddleware`. Shows thumbnail status for each class and allows selection.

## Deployment

| Setting | Value |
|---------|-------|
| Unit file | `/etc/systemd/system/twy-thumbnails.service` |
| Port | 5004 |
| URL | `classes.tiffanywood.yoga/thumbnails/` |
| Process | `/usr/bin/python3 /root/twy/thumbnails/src/dashboard/dashboard.py` |
| Working dir | `/root/twy` |
| Env file | `/root/twy/thumbnails/.env` |

nginx routes `location /thumbnails/` → `127.0.0.1:5004/thumbnails/`.

## Key Paths

- Bumper source: `/root/twy/thumbnails/twy_bumper_intro_720p25.mp4`, `twy_bumper_outro_720p25.mp4`
- Class recordings: `data/classes/` (relative to `/root/twy`)
- Thumbnail output: `data/classes/<date>_<slug>/class_thumbnails/`
