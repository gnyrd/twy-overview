# Downloading Recordings

Zoom cloud recordings are downloaded automatically by twy-download. You normally don't need to do anything — but here's how it works and how to intervene.

## How It Works

Four specialized scripts each handle one type of recording:

| Script | What It Downloads | Output Directory |
|--------|-------------------|-----------------|
| `zoom_download_classes.py` | "Zoom Meeting" recordings ≥ 15 min | `data/classes/` |
| `zoom_download_shorts.py` | "Zoom Meeting" recordings < 15 min | `data/outtakes/` |
| `zoom_download_privates.py` | All non-"Zoom Meeting" recordings | `data/privates/` |
| `zoom_download.py` | Legacy all-in-one (classes + privates) | `data/classes/` + `data/privates/` |

Each script runs on cron and maintains its own state file in `state/` to prevent duplicate downloads.

## What Gets Downloaded

For each recording, the script downloads:

- Video file (shared screen with speaker view, gallery view, or audio-only)
- Per-participant audio tracks (`audio/audio_firstname_lastname.m4a`)
- Transcript (`audio_transcript.vtt`)
- Participant list (`participants.json`)
- Timeline (`timeline.json`)
- Summary (`summary.json`)

All files land in a dated directory: `YYYY-MM-DD_HHMM_{topic}/`

## How Do I...

### Check if a recording was downloaded

```bash
# SSH to the server, then:
ls /root/twy/data/classes/ | grep 2026-03-15
```

Or check the state file:
```bash
cat /root/twy/download/state/downloads_classes.json | python3 -m json.tool | grep "2026-03-15"
```

### Force re-download a specific recording

Delete the recording's entry from the relevant state file, then re-run the script:

```bash
# Edit the state file to remove the entry
vi /root/twy/download/state/downloads_classes.json

# Re-run
python3 /root/twy/download/src/zoom/zoom_download_classes.py --days-back 7
```

### Download recordings from further back

By default, scripts look back 7 days. Use `--days-back`:

```bash
python3 /root/twy/download/src/zoom/zoom_download_classes.py --days-back 30
```

### List available recordings without downloading

```bash
python3 /root/twy/download/src/zoom/zoom_list.py --days-back 14
```

### Check download health

Look at the cron logs:
```bash
tail -50 /root/twy/download/logs/classes.log
```

## Troubleshooting

- **Recording not appearing**: Zoom takes 5–15 min to process cloud recordings after a meeting ends. The download cron runs every 30 min.
- **Incomplete files**: The download script validates file sizes (≥ 95% of expected) and retries up to 5 times with exponential backoff.
- **"No recordings found"**: Check that the Zoom API credentials in `/root/twy/download/.env` are valid and that recordings exist in the date range.
