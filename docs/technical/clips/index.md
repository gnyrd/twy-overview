# Clips

Video clip extraction pipeline from class recordings.

## Service

- **Status**: active (running)
- **Systemd unit**: `twy-clips-dashboard`
- **Port**: 5002

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `*/5 * * * *` | `cd /root/twy/clips && ./src/pipeline/class_recording_watchdo...` | No | `-` |

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |
| GET | `/` | No |  |
| GET | `/` | No |  |
| POST | `/api/extract-custom-clip` | No |  |
| POST | `/api/extract-custom-clip` | No |  |
| POST | `/api/extract-custom-clip` | No |  |
| POST | `/api/extract-custom-opening` | No |  |
| POST | `/api/extract-custom-opening` | No |  |
| POST | `/api/extract-custom-opening` | No |  |
| GET | `/api/health` | No |  |
| GET | `/api/health` | No |  |
| GET | `/api/health` | No |  |
| POST | `/api/ig/queue` | No |  |
| DELETE | `/api/ig/queue` | No |  |
| POST | `/api/ig/queue` | No |  |
| DELETE | `/api/ig/queue` | No |  |
| POST | `/api/ig/queue` | No |  |
| DELETE | `/api/ig/queue` | No |  |
| POST | `/api/save-transcript` | No |  |
| POST | `/api/save-transcript` | No |  |
| POST | `/api/save-transcript` | No |  |
| POST | `/api/wa/queue` | No |  |
| DELETE | `/api/wa/queue` | No |  |
| POST | `/api/wa/queue` | No |  |
| DELETE | `/api/wa/queue` | No |  |
| POST | `/api/wa/queue` | No |  |
| DELETE | `/api/wa/queue` | No |  |
| POST | `/api/yt/queue` | No |  |
| DELETE | `/api/yt/queue` | No |  |
| POST | `/api/yt/queue` | No |  |
| DELETE | `/api/yt/queue` | No |  |
| POST | `/api/yt/queue` | No |  |
| DELETE | `/api/yt/queue` | No |  |
| GET | `/class/<class_name>` | No |  |
| GET | `/class/<class_name>` | No |  |
| GET | `/class/<class_name>` | No |  |
| GET | `/class/<class_name>/captioned` | No |  |
| GET | `/class/<class_name>/captioned` | No |  |
| GET | `/class/<class_name>/captioned` | No |  |
| GET | `/class/<class_name>/uncaptioned` | No |  |
| GET | `/class/<class_name>/uncaptioned` | No |  |
| GET | `/class/<class_name>/uncaptioned` | No |  |
| GET | `/clip/uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/clip/uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/clip/uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/download-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/download-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/download-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/download/<class_name>/<variant>/<filename>` | No |  |
| GET | `/download/<class_name>/<variant>/<filename>` | No |  |
| GET | `/download/<class_name>/<variant>/<filename>` | No |  |
| GET | `/download/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/download/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/download/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/ig/queue` | No |  |
| GET | `/ig/queue` | No |  |
| GET | `/ig/queue` | No |  |
| GET | `/login` | No |  |
| POST | `/login` | No |  |
| GET | `/login` | No |  |
| POST | `/login` | No |  |
| GET | `/login` | No |  |
| POST | `/login` | No |  |
| GET | `/logout` | No |  |
| GET | `/logout` | No |  |
| GET | `/logout` | No |  |
| GET | `/media/clip-thumbnail-uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/media/clip-thumbnail-uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/media/clip-thumbnail-uncaptioned/<class_name>/<clip_name>` | No |  |
| GET | `/media/clip-thumbnail/<class_name>/<variant>/<clip_name>` | No |  |
| GET | `/media/clip-thumbnail/<class_name>/<variant>/<clip_name>` | No |  |
| GET | `/media/clip-thumbnail/<class_name>/<variant>/<clip_name>` | No |  |
| GET | `/media/thumbnail/<class_name>` | No |  |
| GET | `/media/thumbnail/<class_name>` | No |  |
| GET | `/media/thumbnail/<class_name>` | No |  |
| GET | `/media/video-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/media/video-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/media/video-uncaptioned/<class_name>/<filename>` | No |  |
| GET | `/media/video/<class_name>/<variant>/<filename>` | No |  |
| GET | `/media/video/<class_name>/<variant>/<filename>` | No |  |
| GET | `/media/video/<class_name>/<variant>/<filename>` | No |  |
| GET | `/media/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/media/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/media/youtube/<class_name>/opening.mp4` | No |  |
| GET | `/media/youtube/<class_name>/opening_thumb.jpg` | No |  |
| GET | `/media/youtube/<class_name>/opening_thumb.jpg` | No |  |
| GET | `/media/youtube/<class_name>/opening_thumb.jpg` | No |  |
| GET | `/preview/<action>` | No |  |
| GET | `/preview/<action>` | No |  |
| GET | `/preview/<action>` | No |  |
| GET | `/yt/queue` | No |  |
| GET | `/yt/queue` | No |  |
| GET | `/yt/queue` | No |  |

## Dependencies

- **Imports from**: [paths](../paths/index.md)
- **Pip packages**: flask>=3.0, openai>=1.0, openai-whisper>=20231117, opencv-python>=4.8, python-dotenv>=1.0, requests>=2.31, tqdm>=4.66

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `ANTHROPIC_API_KEY` | Yes | Yes |
| `ASPECT_RATIO` | Yes | No |
| `CAPTIONED_SUBDIR` | Yes | No |
| `CLIPS_SUBDIR` | Yes | No |
| `DASHBOARD_PASS` | Yes | Yes |
| `EXTRACTED_SUBDIR` | Yes | No |
| `FLASK_PORT` | Yes | Yes |
| `FLASK_SECRET_KEY` | Yes | Yes |
| `OPENAI_API_KEY` | Yes | Yes |
| `PARTICIPANTS_FILE` | Yes | No |
| `SRT_SUBDIR` | Yes | No |
| `THUMBNAIL_SUFFIX` | Yes | No |
| `TWY_CLASSES_DIR` | Yes | No |
| `TWY_PROJECT_DIR` | Yes | No |
| `TWY_STATE_DIR` | Yes | Yes |
| `UNCAPTIONED_SUBDIR` | Yes | No |

## Key Files

- `clips/docs/ig_posting_example/generate_image.py` (entry_point)
- `clips/docs/ig_posting_example/post_to_instagram.py` (entry_point)
- `clips/docs/ig_posting_example/refresh_token.py` (entry_point)
- `clips/src/utils/ai_analyzer.py` (entry_point)
- `clips/src/utils/class_names.py` (entry_point)
- `clips/src/utils/verify_env.py` (entry_point)
- `clips/src/utils/vtt_parser.py` (entry_point)
- `clips/src/utils/whisper_refine.py` (entry_point)
- `clips/src/video/add_captions.py` (entry_point)
- `clips/src/video/add_fades.py` (entry_point)
- `clips/src/video/extract_audio_clips.py` (entry_point)
- `clips/src/video/extract_clips.py` (entry_point)
- `clips/src/video/extract_opening_segment.py` (entry_point)
- `clips/src/video/generate_thumbnail.py` (entry_point)
- `clips/src/video/identify_segments.py` (entry_point)
- `clips/src/video/srt_clip_from_vtt.py` (entry_point)
- `clips/src/video/transcribe_clip.py` (entry_point)
- `clips/src/web/dashboard.py` (entry_point)
- `clips/docs/ig_posting_example/lib/__init__.py` (module)
- `clips/docs/ig_posting_example/lib/background.py` (module)
- `clips/docs/ig_posting_example/lib/constants.py` (module)
- `clips/docs/ig_posting_example/lib/data.py` (module)
- `clips/docs/ig_posting_example/lib/drawing.py` (module)
- `clips/docs/ig_posting_example/lib/fonts.py` (module)
- `clips/docs/ig_posting_example/lib/slides.py` (module)
- `clips/src/__init__.py` (module)
- `clips/src/ig/__init__.py` (module)
- `clips/src/ig/state.py` (module)
- `clips/src/utils/__init__.py` (module)
- `clips/src/utils/project_base.py` (module)
- `clips/src/video/__init__.py` (module)
- `clips/src/video/timing_config.py` (module)
- `clips/src/wa/__init__.py` (module)
- `clips/src/wa/state.py` (module)
- `clips/src/web/__init__.py` (module)
- `clips/src/yt/__init__.py` (module)
- `clips/src/yt/state.py` (module)
- `clips/docs/ig_posting_example/test_slide.py` (test)

## Lint Findings

- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: */5 * * * * cd /root/twy/clips && ./src/pipeline/class_recording_watchdog.sh >> logs/watchdo...
- 🔵 **LOW** [orphan_env_vars]: Env var ASPECT_RATIO is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var CAPTIONED_SUBDIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var CLIPS_SUBDIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var EXTRACTED_SUBDIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var PARTICIPANTS_FILE is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var SRT_SUBDIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var THUMBNAIL_SUFFIX is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_CLASSES_DIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_PROJECT_DIR is defined but never referenced in code
- 🔵 **LOW** [orphan_env_vars]: Env var UNCAPTIONED_SUBDIR is defined but never referenced in code
