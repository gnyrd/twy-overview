# twy-clips

Video/audio clip processing pipeline with AI-powered content analysis and a web dashboard.

**Repo:** `gnyrd/twy-clips` → `/root/twy/clips/`

## Pipeline Stages

Processing is handled by `src/process_class.sh`, which calls individual stage scripts in order:

| Stage | Script | Purpose |
|-------|--------|---------|
| 0 | `stage_0_rename_files.sh` | Rename old-format files (`raw.mp4`, `transcript.vtt`) to new format |
| 1 | `stage_1_identify_segments.sh` | AI segment identification via OpenAI API |
| 2 | `extract_clips.py` | Clip extraction in 9:16 vertical format |
| 3 | uncaptioned clip generation | Adds fade in/out to extracted clips |
| 4 | `stage_4_whisper_srt.py` | Whisper SRT generation (speech-to-text) |
| 5 | caption burning | Burns SRT captions onto clips |
| 6 | captioned clip fades | Adds fades to captioned clips (duration-based idempotency, 1.25s threshold) |

All stages are idempotent with skip logic.

## Output Structure

```
data/classes/YYYY-MM-DD_classname/
├── zoom_files/                    # Source (from twy-download)
│   ├── shared_screen_with_speaker_view.mp4
│   ├── audio_transcript.vtt
│   ├── participants.json
│   └── audio/
└── clips/
    ├── ig_segments_ai.json        # AI-identified segments
    ├── srt/                       # Whisper-generated SRTs
    └── 9x16/
        ├── thumbnail.jpg          # Class thumbnail
        ├── extracted/             # Raw extracted clips
        ├── uncaptioned/           # Final uncaptioned clips with fades
        └── captioned/             # Final captioned clips with fades
```

## Timing Configuration

Defined in `src/video/timing_config.py`:

- Fade duration: 0.75s
- Start freeze: 0.75s (with audio silence)
- End freeze: 1.5s
- Total added per clip: 2.25s

## Watchdog

`class_recording_watchdog.sh` runs every 5 minutes via cron. Scans `data/classes/` for directories needing processing.

Detection logic (`src/utils/class_names.py`):
- Time window: 60 minutes before to 20 minutes after scheduled class time
- Checks for final products (uncaptioned + captioned clips with thumbnails)
- Classes dir read from `.env` (`TWY_CLASSES_DIR`)

## Dashboard

Web interface for viewing processed clips. Shows:

- Recent classes with clip thumbnails
- Clip titles with classification and duration
- Captioned/uncaptioned previews
- Classes ≥ 6 weeks old: simplified read-only layout (thumbnail + transcript text only, clips labeled "Quote 1", "Quote 2", etc.)

## Key Source Files

```
src/
├── zoom/              # Zoom-related utilities
├── video/
│   ├── extract_clips.py
│   ├── extract_audio_clips.py
│   ├── generate_thumbnail.py
│   ├── timing_config.py
│   └── srt_clip_from_vtt.py
├── transcription/
│   └── stage_4_whisper_srt.py
├── utils/
│   └── class_names.py
└── process_class.sh   # Main pipeline orchestrator
```

## Dependencies

- Python 3.x, FFmpeg, OpenCV
- OpenAI API (segment identification)
- Whisper (transcription)
- tqdm (progress bars)
- Zoom API credentials (shared with twy-download)
