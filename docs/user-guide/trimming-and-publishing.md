# Trimming and Publishing

The trim editor at `classes.tiffanywood.yoga/trim/<date>` lets you set IN/OUT points on a class recording, add bumpers, and publish the result to Vimeo and HeyMarvelous in one step.

## Opening the Trim Editor

From the calendar at **https://classes.tiffanywood.yoga**:

1. Find the class date
2. Click the **camera icon** (🎥) on the day cell
3. The trim editor loads with the video, waveform, and transcript

## Setting IN and OUT Points

The editor shows three synchronized views:

- **Video player** — scrub or use keyboard shortcuts
- **Waveform** — visual overview of audio; red ticks indicate non-host audio (student participation)
- **Transcript** — click any line to seek; each line has IN/OUT buttons

### Using the Waveform

- Scroll-wheel to zoom in/out
- Drag to pan
- Use zoom presets for different time scales
- Red ticks on the waveform show where students are speaking (non-host audio detected)

### Using the Transcript

- Click any transcript line to seek the video to that point
- Click the **IN** or **OUT** button on a transcript line to set that line's timestamp as the trim point

## Trim Options

### Trim Only (Local)

Click **✂ Trim** (left button) to:
- Stream-copy trim with bumpers
- Save the output locally to `data/class-videos/`
- Does NOT upload or create a library entry

### Trim & Publish

Click **✂ Trim & Publish** to run the full workflow:

1. **Phase 0 (0–10%)** — Add to Library: runs `post_recording_workflow.py`, creates the HeyMarvelous media record, stores `marvelous_media_id` in the plan JSON
2. **Phase 1 (10–50%)** — ffmpeg stream-copy trim: intro bumper + trimmed main + outro bumper (fast — no re-encode)
3. **Phase 2 (50–99%)** — TUS upload to Vimeo (replaces source on the existing media item)

Output: `data/class-videos/<date>-<class_type>-<title>.mp4`

## Technical Notes

- The trim uses ffmpeg `concat` demuxer with `-c copy` (stream-copy) — no quality loss, takes seconds not minutes
- IN point is snapped to the nearest keyframe via `ffprobe` to avoid black-frame gaps
- Bumper files live at `/root/twy/thumbnails/twy_bumper_intro_720p25.mp4` and `twy_bumper_outro_720p25.mp4`
- All source files are H.264 1280×720 25fps AAC
