# Daily Class Workflow

What happens from "class is over" to "published and ready for students" — and what you need to do at each step.

## Automatic Steps (No Action Needed)

After a Zoom class ends:

1. **Zoom processes the cloud recording** (5–15 min after class ends)
2. **twy-download** picks it up automatically (cron runs every 30 min for classes, every 5 min for the watchdog)
   - Long classes (≥ 15 min) → `data/classes/`
   - Short recordings (< 15 min) → `data/outtakes/`
   - Private/named meetings → `data/privates/`
3. **twy-clips watchdog** detects the new recording (runs every 5 min)
   - Runs AI segment identification
   - Extracts clips in 9:16 vertical format
   - Generates Whisper SRT captions
   - Burns captions onto clips
   - Creates a thumbnail from the first clip

At this point, clips are ready and visible on the clips dashboard at `clips.tiffanywood.yoga`.

## Manual Steps

### 1. Create or Review the Class Plan

Open **https://classes.tiffanywood.yoga** and find the class date on the calendar.

- If no plan exists: click the date → **New Plan** → fill in title, series, class type, apex pose, affirmation, etc.
- If a plan exists: review it, make sure the `published` checkbox is set if you want it on HeyMarvelous.
- Click **Save** — this syncs the plan to the HeyMarvelous calendar automatically.

### 2. Trim and Publish the Video

From the calendar, click the **camera icon** on the class date to open the trim editor.

1. Set the **IN** point (keyboard: `i`) — where the class content starts
2. Set the **OUT** point (keyboard: `o`) — where it ends
3. The waveform and transcript panel help you find the right spots
4. Click **✂ Trim & Publish** — this does three things:
   - Adds the recording to the HeyMarvelous library (creates the media record)
   - Trims the video with bumpers (intro + main + outro) via stream-copy (fast, no re-encode)
   - Uploads the trimmed video to Vimeo via TUS

Progress shows as a two-bar overlay: ✂ Trim → ☁ Upload.

### 3. Select a Thumbnail

Still in the trim editor:

1. Gold markers on the timeline show AI-ranked thumbnail candidates
2. Navigate with `<` / `>` keys or buttons
3. Press `T` to capture any frame at the current playhead position (adds text overlay automatically)
4. Click **Publish Thumbnail** (amber button) to push it to Vimeo and HeyMarvelous

### 4. Verify

- Check the class on **https://classes.tiffanywood.yoga** — the day cell should show a blue gradient if published
- Check the HeyMarvelous library to confirm the video and thumbnail are live
- Social media clips are at `clips.tiffanywood.yoga` — review and download as needed

## Keyboard Shortcuts (Trim Editor)

| Key | Action |
|-----|--------|
| `Space` | Play / pause |
| `←` / `→` | Frame step (1/25s) |
| `⌥←` / `⌥→` | 10-frame jump |
| `i` | Set IN point |
| `o` | Set OUT point |
| `<` / `>` | Navigate thumbnail candidates |
| `T` | Capture/set thumbnail at playhead |
