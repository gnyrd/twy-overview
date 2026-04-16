# Yoga Habit

Yoga Habit landing page, Flask app on port 5008.

## Service

- **Status**: active (running)
- **Systemd unit**: `twy-yoga-habit`
- **Port**: 5008

## Cron Jobs

| Schedule | Command | Failure Wrapper | Log |
|----------|---------|-----------------|-----|
| `0 10 1 * *` | `/root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2_refresh.log 2>&1...` | No | `/root/twy/data/logs/geolite2_refresh.log` |

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No |  |
| GET | `/ping` | No |  |
| GET | `/stats` | No |  |
| POST | `/subscribe` | No |  |
| POST | `/track` | No |  |

## Dependencies

- **Pip packages**: Flask==3.1.0, geoip2==4.8.0, pytest==8.3.5, requests==2.32.3

## Environment Variables

No environment variables recorded.

## Key Files

- `yoga-habit/app.py` (entry_point)
- `yoga-habit/config.py` (module)
- `yoga-habit/content.py` (module)
- `yoga-habit/cta.py` (module)
- `yoga-habit/geo.py` (module)
- `yoga-habit/state.py` (module)
- `yoga-habit/stats_view.py` (module)
- `yoga-habit/tests/__init__.py` (module)
- `yoga-habit/tracking.py` (module)
- `yoga-habit/tests/test_content.py` (test)
- `yoga-habit/tests/test_cta.py` (test)
- `yoga-habit/tests/test_geo.py` (test)
- `yoga-habit/tests/test_state.py` (test)
- `yoga-habit/tests/test_tracking.py` (test)

## Lint Findings

- 🟡 **MEDIUM** [missing_failure_wrappers]: Cron job missing failure wrapper: 0 10 1 * * /root/twy/yoga-habit/scripts/refresh_geolite2.sh >> /root/twy/data/logs/geolite2...
