# twy-asset-management

Digital asset organization and AI yoga pose detection.

**Repo:** `gnyrd/twy-asset-management` → `/root/twy/asset-management/`

## Asset Organization

Reorganized 1.1TB of Dropbox content into a clean two-tier structure.

### Structure

```
TWY Assets/                         Location: /Volumes/media/TWY/TWY Assets/
├── Active/ (106GB, 3,645 files)
│   ├── Photo Shoots/ (3.4GB)       2020 Outdoor (145), 2022 Studio (1,127)
│   ├── Retreats/ (74GB)            8 retreat collections
│   ├── Brand Assets/ (68MB)        Logos, fonts, brand materials
│   └── Marketing/ (29GB)           Ads, email, thumbnails, Etifanies
└── Archive/ (13GB, 6,927 files)
    ├── Photo Shoots/
    ├── Retreats/
    ├── Teacher Training/
    └── Photo Archive/
```

- 10,572 total files, 3,355 images (15GB) in Active
- 177 duplicates removed (3.7GB freed)
- 946GB class videos excluded (stored separately in `data/classes/`)

### Storage Cost

| Option | Cost |
|--------|------|
| Current Dropbox (3TB) | $300/year |
| Cloudinary (images, free) + B2 (videos) | ~$78/year |
| ImageKit (images, free) alternative | ~$84/year total |

## Pose Detection

Uses Google MediaPipe to detect yoga poses in images and video.

### Pipeline

1. MediaPipe extracts 33 body keypoints per frame
2. Pre-trained classifier maps keypoints → named pose
3. Target: [CustomPose-Classification-Mediapipe](https://github.com/naseemap47/CustomPose-Classification-Mediapipe) for inference

### Status

- MediaPipe pose extraction: working (5/5 test images detected)
- Model: `pose_landmarker_lite.task` (included in repo)
- Classification: not yet integrated (next step)

### Files

```
mediapipe_test.py                    # Pose detection test
pose_landmarker_lite.task            # MediaPipe model weights
landmarks_TWY_01_05_21-*.json       # Sample detection outputs
test_cloudinary.py                   # Cloudinary upload test
```

### Dependencies

```
pip3 install cloudinary python-dotenv mediapipe opencv-python
```
