# Technical Reference

Developer-level documentation for the TWY content pipeline. Covers architecture, per-repo internals, deployment, and configuration.

## Contents

- [Architecture](architecture) — System diagram, data flow, repo relationships
- [twy-download](twy-download) — Zoom recording download service
- [twy-clips](twy-clips) — Video/audio clip processing pipeline
- [twy-class-plans](twy-class-plans) — Flask dashboard, API, trim workflow
- [twy-video-editor](twy-video-editor) — Thumbnail generation and bumper tools
- [twy-tweee-gpt](twy-tweee-gpt) — Custom GPT for newsletter generation
- [twy-announce](twy-announce) — Email reminders, status reports, WhatsApp toolbox
- [twy-asset-management](twy-asset-management) — Asset organization and pose detection
- [marvy](marvy) — HeyMarvelous/Namastream API client library (shared)
- [Deployment](deployment) — systemd services, nginx, SSL, cron
- [Environment Variables](environment-variables) — All `.env` variables across repos
