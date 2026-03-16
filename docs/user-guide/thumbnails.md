# Thumbnails

Thumbnails are the images that represent each class in the HeyMarvelous library and on Vimeo. They're generated automatically but you pick the final one.

## Automatic Generation

After a class recording is processed, `twy-auto-thumbnail` generates:

- 6 candidate frame JPGs extracted from the video
- 6 thumbnail PNGs with text overlay (class title, apex pose, date)
- `thumbnail_ranking.json` — AI ranking of the candidates

Output goes to: `data/classes/<date>_<type>/class_thumbnails/`

## Selecting a Thumbnail

### From the Trim Editor (Preferred)

1. Open the trim editor for the class (`classes.tiffanywood.yoga/trim/<date>`)
2. Gold markers on the timeline show AI-ranked candidates (brightest = rank 1)
3. Use `<` / `>` keys to navigate between candidates
4. Press `T` at any point to capture the current playhead position as a thumbnail
   - This runs ffmpeg to extract the frame + `twy-thumbnail` to add text overlay
   - Works at any position, not just AI candidates
5. Preview appears in the side panel
6. Click **Publish Thumbnail** (amber button) to upload to Vimeo and HeyMarvelous

### From the Plan Detail Page

1. Open the class plan at `classes.tiffanywood.yoga/plan/<date>`
2. If thumbnails exist but none is selected, a grid of candidates appears
3. Click one to select it

## Manual Generation

If thumbnails weren't generated automatically:

```bash
# Generate for today's class
/root/twy/thumbnails/src/twy-auto-thumbnail

# Generate for a specific date
/root/twy/thumbnails/src/twy-auto-thumbnail 2026-03-15
```

## How Do I...

### Check if thumbnails exist for a class

```bash
ls /root/twy/data/classes/2026-03-15_*/class_thumbnails/
```

### Regenerate thumbnails

Delete the existing thumbnails directory and re-run:

```bash
rm -rf /root/twy/data/classes/2026-03-15_*/class_thumbnails/
/root/twy/thumbnails/src/twy-auto-thumbnail 2026-03-15
```

### See the thumbnails dashboard

Visit `classes.tiffanywood.yoga/thumbnails/` — this is the dedicated thumbnails app running on port 5004.
