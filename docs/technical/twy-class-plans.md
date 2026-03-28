# twy-class-plans

Flask dashboard for class plan management, video trim/publish workflow, and thumbnail selection. Also serves the API consumed by TWEEE GPT.

**Repo:** `gnyrd/twy-class-plans` → `/root/twy/class-plans/`
**Live:** https://classes.tiffanywood.yoga (port 5003)
**Service:** `twy-class-dashboard`

## Application Structure

```
dashboard/
├── app.py          # Flask app factory, health endpoint
├── views.py        # UI routes + trim editor + thumbnail API
├── api.py          # Tweee GPT API endpoints (/api/plans/*, /api/overview/*)
├── auth.py         # Session-based single-password login
├── marvelous.py    # HeyMarvelous integration (publish/unpublish events)
├── data.py         # Plan JSON read/write, file discovery
├── config.py       # Path constants, class types, categories
├── templates/      # Jinja2 templates
├── static/
│   ├── trim.css
│   └── js/         # trim-state, trim-timeline, trim-thumbnails, trim-job, trim-transcript, trim-init
└── requirements.txt
```

## Routes

### UI Routes

| Route | Description |
|-------|-------------|
| `GET /` | Monthly calendar (6-month view, scrollable) |
| `GET /plan/new` | New plan form |
| `GET /plan/<date>` | Plan detail / edit |
| `POST /plan/<date>/save` | Save plan (triggers HeyMarvelous publish/unpublish if `published` changed) |
| `POST /plan/<date>/select-thumb` | Set selected thumbnail |
| `POST /plan/<date>/add-to-library` | Run post-recording workflow |
| `GET /trim/<date>` | Video trim editor |

### Trim Editor API

| Route | Description |
|-------|-------------|
| `GET /api/trim/<date>/video` | Stream video (HTTP Range requests) |
| `GET /api/trim/<date>/waveform` | SVG waveform (generated + cached) |
| `GET /api/trim/<date>/noise` | Noise marker positions JSON |
| `GET /api/trim/<date>/transcript` | VTT transcript as JSON segments |
| `GET /api/trim/<date>/info` | Duration, output filename, bumper availability |
| `POST /api/trim/<date>/process` | Start trim+bumper+upload job |
| `GET /api/trim/<date>/status` | Poll trim job status + progress |
| `GET /api/trim/<date>/thumbnails` | AI-ranked thumbnail candidates |
| `POST /api/trim/<date>/select-thumbnail` | Save selected thumbnail |
| `POST /api/trim/<date>/capture-frame` | Capture playhead frame as thumbnail (ffmpeg + text overlay) |
| `POST /api/trim/<date>/publish-thumbnail` | Upload thumbnail to Vimeo/HeyMarvelous |

### TWEEE GPT API

| Route | Description |
|-------|-------------|
| `GET /api/plans` | List plans (optional `?from=&to=` date range) |
| `GET /api/plans/<date>` | Get single plan |
| `POST /api/plans/<date>` | Upsert plan |
| `POST /api/plans/batch` | Batch upsert |
| `GET /api/overview` | Full-year monthly overview |
| `GET /api/overview/<month>` | Single month overview |
| `GET /openapi.yaml` | OpenAPI spec for TWEEE Custom GPT |
| `GET /api/ping` | Health check |

## Class Plan Schema

Files: `data/class-plans/YYYY-MM-DD.json`

Key fields: `id`, `date`, `time`, `duration`, `title`, `series`, `class_type`, `description`, `apex_pose`, `energetic_pulse`, `teaching_lens`, `physical_focus`, `physical_arc`, `upas_key_actions`, `affirmation`, `categories`, `level`, `props`, `published`, `marvelous_event_id`, `marvelous_media_id`, `selected_thumbnail`

## Trim & Publish Workflow

1. **Phase 0 (0–10%)** — Add to Library: `post_recording_workflow.py` creates HeyMarvelous media record, stores `marvelous_media_id`
2. **Phase 1 (10–50%)** — ffmpeg stream-copy trim: `concat` demuxer with intro + trimmed main (keyframe-snapped IN) + outro
3. **Phase 2 (50–99%)** — TUS upload to Vimeo via `marvy` client

Output: `data/class-videos/<date>-<class_type>-<title>.mp4`

### ffmpeg IN Point Accuracy

`_find_keyframe_at_or_after(video_path, ts_s)` uses `ffprobe -skip_frame nokey` to snap the IN point to the nearest keyframe. This eliminates both pre-IN frames and black-frame gaps that occur with naive stream-copy seeking.

## Preview Mode

Cookie-based feature flag for WIP features.

- Enable: `?on` on any URL (or `/preview/on`)
- Disable: `?off` (or `/preview/off`)
- In templates: `{% if preview %}...{% endif %}`

## Data Paths

```
../data/class-plans/       # Plan JSON files
../data/classes/           # Zoom recording directories (read-only)
../data/class-videos/      # Trimmed output videos
../video-editor/           # Bumper files (intro + outro mp4)
../marvy/                  # HeyMarvelous API library
```

All paths configured via environment variables with sensible defaults in `config.py`.

## Class Types

| Value | Display | Description File |
|-------|---------|-----------------|
|  | Strength |  |
|  | Stretch |  |
|  | Flow |  |
|  | Dynamic Flow |  |
|  | Slow Flow |  |
|  | Principles |  |
|  | Expansion |  |
|  | Meditation | *(none)* |
|  | Final Integration |  |
|  | Habit |  — second Saturday of each month |

Description files live in . They are injected into the HeyMarvelous event description when publishing.

## Class Types

| Value | Display | Description File |
|-------|---------|-----------------|
|  | Strength |  |
|  | Stretch |  |
|  | Flow |  |
|  | Dynamic Flow |  |
|  | Slow Flow |  |
|  | Principles |  |
|  | Expansion |  |
|  | Meditation | *(none)* |
|  | Final Integration |  |
|  | Habit |  - second Saturday of each month |

Description files live in . They are injected into the HeyMarvelous event description when publishing.

## Class Types

| Value | Display | Description File |
|-------|---------|-----------------|
| `Strength` | Strength | `strength.md` |
| `Stretch` | Stretch | `stretch.md` |
| `Flow` | Flow | `flow.md` |
| `Dynamic Flow` | Dynamic Flow | `flow.md` |
| `Slow Flow` | Slow Flow | `flow.md` |
| `Principles of Anusara®` | Principles | `principles.md` |
| `Expansion` | Expansion | `expansion.md` |
| `Meditation` | Meditation | *(none)* |
| `Final Integration` | Final Integration | `integration.md` |
| `Habit` | Habit | `habit.md` - second Saturday of each month |

Description files live in `class_type_descriptions/`. They are injected into the HeyMarvelous event description when publishing.
