# Processing Clips

twy-clips automatically turns Zoom recordings into social media clips with captions. The watchdog runs every 5 minutes and processes new recordings through a 7-stage pipeline.

## What Gets Created

For each class recording, the pipeline produces:

```
data/classes/YYYY-MM-DD_classname/
├── zoom_files/          # Original Zoom files (untouched)
└── clips/
    ├── ig_segments_ai.json    # AI-identified segments
    ├── srt/                   # Whisper-generated captions
    └── 9x16/
        ├── thumbnail.jpg      # Class thumbnail
        ├── extracted/         # Raw extracted clips
        ├── uncaptioned/       # Clips with fades (no text)
        └── captioned/         # Final clips with burned-in captions
```

## The Pipeline Stages

| Stage | What It Does |
|-------|--------------|
| 0 | Renames old-format files to new format (if needed) |
| 1 | AI segment identification — finds interesting moments |
| 2 | Clip extraction in 9:16 vertical format |
| 3 | Adds fade in/out to uncaptioned clips |
| 4 | Whisper SRT generation (speech-to-text) |
| 5 | Burns captions onto clips |
| 6 | Adds fades to captioned clips |

Each stage is idempotent — safe to re-run.

## Viewing Clips

Open **clips.tiffanywood.yoga** in your browser. The dashboard shows:

- Recent classes with their clips
- Each clip shows: name, classification, and duration
- Click to preview captioned or uncaptioned versions
- Classes older than 6 weeks show a simplified read-only view

## How Do I...

### Check if clips were generated for a class

```bash
ls /root/twy/data/classes/2026-03-15_*/clips/9x16/captioned/
```

Or check the clips dashboard.

### Re-process a class

The pipeline is idempotent. Just run it again:

```bash
/root/twy/clips/src/process_class.sh /root/twy/data/classes/2026-03-15_1730_Zoom\ Meeting/
```

### Re-run just one stage

Each stage is a separate script. For example, to regenerate captions only:

```bash
python3 /root/twy/clips/src/transcription/stage_4_whisper_srt.py /root/twy/data/classes/2026-03-15_*/
```

### Check the watchdog status

```bash
# Is the watchdog cron running?
crontab -l | grep watchdog

# Check recent watchdog activity
tail -50 /root/twy/clips/logs/watchdog.log
```

## Timing Configuration

Clips have standardized fades and freezes:

- Fade duration: 0.75s
- Start freeze: 0.75s (with audio silence)
- End freeze: 1.5s
- Total added per clip: 2.25s

Configured in `src/video/timing_config.py`.
