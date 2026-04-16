# Download

Zoom recording download and archive pipeline.

## Service

- **Status**: active (running)
- **Systemd unit**: `twy-zoom-downloader`

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `*/5 * * * *` | `cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ../data/logs/zoom_download_watchdog.log ...` | No | `-` |
| `0 10 * * *` | `cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs/classes_archive.log 2>&1...` | No | `-` |
| `0 8 * * *` | `cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../data/logs/dianes_upload.log 2>&1...` | No | `-` |
| `0 9 * * *` | `cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/dianes_cleanup.log 2>&1...` | No | `-` |
| `15,45 * * * *` | `cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back 1 >> ../data/logs/zoom_download.log 2>&1...` | No | `-` |

## Endpoints

No endpoints.

## Dependencies

- **Imports from**: [paths](../paths/index.md)
- **Pip packages**: google-api-python-client>=2.0, google-auth>=2.0, google-auth-oauthlib>=1.0, playwright>=1.40, python-dotenv>=1.0, requests>=2.31, tqdm>=4.66

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `DIANES_OTP_EMAIL` | Yes | Yes |
| `DIANES_SHAREPOINT_SHARE_URL` | Yes | Yes |
| `TWY_NOTIFY_EMAIL` | Yes | Yes |
| `TWY_PROJECT_DIR` | Yes | No |
| `TWY_STATE_DIR` | Yes | Yes |
| `WATCHDOG_SCAN_DAYS` | No | Yes |
| `ZOOM_ACCOUNT_ID` | Yes | Yes |
| `ZOOM_CLIENT_ID` | Yes | Yes |
| `ZOOM_CLIENT_SECRET` | Yes | Yes |
| `ZOOM_DAYS_BACK` | Yes | Yes |
| `ZOOM_MIN_DURATION` | Yes | Yes |

## Key Files

- `download/src/classes_archive.py` (entry_point)
- `download/src/dianes_cleanup.py` (entry_point)
- `download/src/dianes_gmail_auth.py` (entry_point)
- `download/src/dianes_upload_privates.py` (entry_point)
- `download/src/utils/verify_env.py` (entry_point)
- `download/src/zoom/zoom_download.backup.py` (entry_point)
- `download/src/zoom/zoom_download.py` (entry_point)
- `download/src/zoom/zoom_download_classes.py` (entry_point)
- `download/src/zoom/zoom_download_privates.py` (entry_point)
- `download/src/zoom/zoom_download_shorts.py` (entry_point)
- `download/src/zoom/zoom_download_watchdog.py` (entry_point)
- `download/src/zoom/zoom_list.py` (entry_point)
- `download/src/__init__.py` (module)
- `download/src/dianes_sharepoint_client.py` (module)
- `download/src/utils/__init__.py` (module)
- `download/src/utils/project_base.py` (module)
- `download/src/zoom/__init__.py` (module)
- `download/src/zoom/download_utils.py` (module)
- `download/src/zoom/zoom_api.py` (module)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var WATCHDOG_SCAN_DAYS is referenced but never defined in .env
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 15,45 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download.py --days-back ...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: */5 * * * * cd /root/twy/download && /usr/bin/python3 src/zoom/zoom_download_watchdog.py >> ...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 8 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_upload_privates.py >> ../da...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 9 * * * cd /root/twy/download && /usr/bin/python3 src/dianes_cleanup.py >> ../data/logs/...
- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 10 * * * cd /root/twy/download && /usr/bin/python3 src/classes_archive.py >> ../data/logs...
- 🔵 **LOW** [orphan_env_vars]: Env var TWY_PROJECT_DIR is defined but never referenced in code
