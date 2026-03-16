# Asset Management

twy-asset-management handles two things: organizing the 1.1TB of TWY digital assets and AI-powered yoga pose detection.

## Asset Organization

The original Dropbox had 1.1TB of mixed content. It's been organized into a clean structure:

```
TWY Assets/
├── Active/ (106GB, 3,645 files)
│   ├── Photo Shoots/       — 2020 Outdoor + 2022 Studio (1,272 images)
│   ├── Retreats/           — 8 retreat collections (74GB)
│   ├── Brand Assets/       — Logos, fonts, brand materials (68MB)
│   └── Marketing/          — Ads, email newsletters, thumbnails, Etifanies videos (29GB)
└── Archive/ (13GB, 6,927 files)
    ├── Photo Shoots/
    ├── Retreats/
    ├── Teacher Training/
    └── Photo Archive/
```

**Key numbers:**
- 3,355 images (15GB) in Active
- 177 duplicates removed (3.7GB freed)
- 946GB of class videos excluded (stored separately)

### Storage Location

- Current: `/Volumes/media/TWY/TWY Assets/` (local)
- Dropbox: `/Volumes/media/TWY/Dropbox/` (original, $300/year for 3TB)
- Recommended migration: Cloudinary (free) for images + Backblaze B2 for videos = ~$78/year

## Pose Detection

Find specific yoga poses across images and video using MediaPipe.

### How It Works

1. MediaPipe extracts 33 body keypoints from each image/video frame
2. A pre-trained classifier maps keypoints to named poses (e.g., "Warrior II")
3. Results can be used to search the image library or find timestamps in video

### Current Status

- MediaPipe pose detection: tested and working on TWY photos (5/5 success)
- Model: `pose_landmarker_lite.task`
- Next step: integrate the [CustomPose-Classification-Mediapipe](https://github.com/naseemap47/CustomPose-Classification-Mediapipe) repo for named pose classification

### Running Pose Detection

```bash
cd /root/twy/asset-management
python3 mediapipe_test.py
```

### Testing Cloudinary Upload

```bash
cd /root/twy/asset-management
python3 test_cloudinary.py
```

Requires `CLOUDINARY_URL` in `.env`.
