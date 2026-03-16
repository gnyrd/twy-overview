# twy-download

Zoom cloud recording download service. Four specialized scripts each target a specific recording type.

**Repo:** `gnyrd/twy-download` → `/root/twy/download/`

## Scripts

| Script | Filter | Output |
|--------|--------|--------|
| `zoom_download_classes.py` | Topic = "Zoom Meeting", duration ≥ 15 min | `data/classes/` |
| `zoom_download_shorts.py` | Topic = "Zoom Meeting", duration < 15 min | `data/outtakes/` |
| `zoom_download_privates.py` | Topic ≠ "Zoom Meeting" | `data/privates/` |
| `zoom_download.py` | Legacy all-in-one | `data/classes/` + `data/privates/` |
| `zoom_list.py` | List only, no download | stdout |

All in `src/zoom/`.

## Shared Components

Defined in `src/zoom/zoom_api.py`:

- `ZoomAPI` — OAuth2 client for Zoom API (account credentials grant)
- `StateManager` — JSON-based download state tracking
- `FileDownloader` — Download with retry logic (5 retries, exponential backoff 2s–32s)
- `download_recording()` — Core download function
- `format_directory_name()` — `YYYY-MM-DD_HHMM_{topic}` naming

## State Management

Each script maintains independent state in `state/`:

```
state/downloads.json           # Legacy script
state/downloads_classes.json   # Classes
state/downloads_shorts.json    # Shorts
state/downloads_privates.json  # Privates
```

State tracks: recording UUID, download date, file paths, participant counts. Prevents duplicate downloads.

## Watchdog

`zoom_download_watchdog.py` scans `zoom_files/` directories directly (no state files). Covers both classes and privates directories. Runs on cron every 5 minutes.

## File Validation

All downloaded files validated against Zoom API's reported size. Files must be ≥ 95% of expected size. Incomplete files are retried automatically.

## Output Structure

```
YYYY-MM-DD_HHMM_{topic}/
├── shared_screen_with_speaker_view.mp4
├── audio_only.m4a
├── audio/
│   ├── audio_firstname_lastname_host.m4a
│   └── audio_firstname_lastname.m4a
├── audio_transcript.vtt
├── timeline.json
├── summary.json
└── participants.json
```

## CLI Arguments

All download scripts support:

- `--days-back N` — Look back N days (default: 7)
- `--min-duration N` / `--max-duration N` — Duration threshold in minutes (default: 15)

## Integration

Downloads feed into twy-clips. The watchdog in twy-clips monitors `data/classes/` for new directories with `zoom_files/` subdirectories.
