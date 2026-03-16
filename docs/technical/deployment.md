# Deployment

Both doc sites run as Flask apps in debug mode on the Hetzner server. Same repo, different `.env` files, different ports.

## Services

### docs.tiffanywoodyoga.com (User Guide)

| Setting | Value |
|---------|-------|
| Unit file | `/etc/systemd/system/twy-docs.service` |
| Port | 5005 |
| URL | https://docs.tiffanywoodyoga.com |
| Process | `/usr/bin/python3 /root/twy/overview/app.py` |
| Working dir | `/root/twy/overview` |
| Env file | `/root/twy/overview/.env.docs` |
| DOCS_DIR | `docs/user-guide` |
| SITE_TITLE | `TWY User Guide` |

### tech.tiffanywoodyoga.com (Technical Reference)

| Setting | Value |
|---------|-------|
| Unit file | `/etc/systemd/system/twy-tech.service` |
| Port | 5006 |
| URL | https://tech.tiffanywoodyoga.com |
| Process | `/usr/bin/python3 /root/twy/overview/app.py` |
| Working dir | `/root/twy/overview` |
| Env file | `/root/twy/overview/.env.tech` |
| DOCS_DIR | `docs/technical` |
| SITE_TITLE | `TWY Technical Reference` |

### Management

```bash
# User guide
systemctl status twy-docs
systemctl restart twy-docs
journalctl -u twy-docs -f

# Technical reference
systemctl status twy-tech
systemctl restart twy-tech
journalctl -u twy-tech -f
```

Both apps run with `debug=True` and `use_reloader=True` — editing markdown files or Python code takes effect immediately without a restart.

## nginx

Add two server blocks to the nginx config (e.g., `/etc/nginx/sites-available/twy`):

```nginx
server {
    listen 443 ssl;
    server_name docs.tiffanywoodyoga.com;

    ssl_certificate     /etc/letsencrypt/live/docs.tiffanywoodyoga.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/docs.tiffanywoodyoga.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5005;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 443 ssl;
    server_name tech.tiffanywoodyoga.com;

    ssl_certificate     /etc/letsencrypt/live/tech.tiffanywoodyoga.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/tech.tiffanywoodyoga.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5006;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Test and reload:
```bash
nginx -t && systemctl reload nginx
```

## SSL

Issue certs for both hostnames:

```bash
certbot certonly --nginx -d docs.tiffanywoodyoga.com
certbot certonly --nginx -d tech.tiffanywoodyoga.com
```

Auto-renewal via certbot systemd timer (same as existing certs).

## All Cron Jobs (System-Wide Reference)

```bash
# twy-download: classes every 30 min
15,45 * * * * cd /root/twy/download && python3 src/zoom/zoom_download_classes.py --days-back 1 >> logs/classes.log 2>&1

# twy-download: privates every hour
0 * * * * cd /root/twy/download && python3 src/zoom/zoom_download_privates.py --days-back 1 >> logs/privates.log 2>&1

# twy-download: shorts daily at 2am
0 2 * * * cd /root/twy/download && python3 src/zoom/zoom_download_shorts.py --days-back 1 >> logs/shorts.log 2>&1

# twy-clips: watchdog every 5 min
*/5 * * * * cd /root/twy/clips && src/class_recording_watchdog.sh >> logs/watchdog.log 2>&1

# twy-announce: email reminders every 30 min
*/30 * * * * cd /root/twy/announce && REMINDER_OFFSETS=26 ./scripts/run_class_email_reminders.sh >> logs/reminders.log 2>&1

# twy-announce: Marvelous sync twice daily
0 9,18 * * * cd /root/twy/announce && /usr/bin/python3 scripts/refresh_marvelous_events.py >> logs/marvelous_sync.log 2>&1

# twy-announce: daily status report at 6am MT (1pm UTC)
0 13 * * * cd /root/twy/announce && python3 src/daily_status_report.py

# twy-announce: YouTube data hourly
0 * * * * /root/twy/announce/src/youtube_daily.sh

# twy-announce: Instagram data hourly (from non-datacenter machine)
# 0 * * * * /path/to/repo/src/instagram_daily.sh
```
