# marvy

Reverse-engineered Python client for the undocumented HeyMarvelous (Namastream) API. Shared library used by twy-class-plans and twy-announce.

**Repo:** `gnyrd/marvy` → `/root/twy/marvy/`

## Why It Exists

HeyMarvelous (built on Namastream) has no official API. This library was created by analyzing HAR files captured from the web dashboard, then building a full CRUD client.

**This is unstable by nature.** The upstream API can change without notice. See `CONTRIBUTING.md` in the marvy repo for documented quirks and the process for handling API breakage.

## Package Structure

```
marvy/
├── marvy/
│   ├── __init__.py       # exports Client, APIError, AuthError
│   ├── client.py         # Client class (~1500 lines)
│   └── exceptions.py     # APIError, AuthError
├── examples/
│   ├── basic_usage.py
│   ├── 02_list_events.py
│   └── export_events_csv.py
├── pyproject.toml        # setuptools build, requires requests>=2.25.0
├── CONTRIBUTING.md       # API quirks, error handling patterns, testing policy
└── README.md
```

Install: `pip install git+https://github.com/gnyrd/marvy.git`

## API Details

- **Base URL:** `https://api.namastream.com`
- **Auth:** Token-based (`Authorization: Token {key}`)
- **Common pattern:** GET returns full nested objects, PUT expects IDs for nested references (handled by `_prepare_*_for_update()` helpers)
- **Pagination:** 10–12 items per page depending on resource
- **Media storage:** Videos hosted on Vimeo (thumbnail and video upload go through Vimeo API first, then sync back to Namastream)
- **Vimeo API:** `https://api.vimeo.com` — requires separate `vimeo_token` for thumbnail/video uploads

## Coverage

### Fully Implemented (CRUD)

- **Events** — `list_events`, `get_event`, `create_event`, `update_event`, `delete_event`
- **Products** — `get_product`, `create_product`, `update_product`, `delete_product`, `list_product_tags`
- **Coupons** — `list_coupons`, `get_coupon`, `create_coupon`, `update_coupon`, `delete_coupon`, `get_coupon_stats`
- **Customers** — `list_customers`, `get_customer`, `create_customer`, `update_customer`, `delete_customer`

### Media Library (Extensive)

- `list_media`, `get_media`, `update_media`, `duplicate_media`
- `upload_thumbnail` — multi-step: Vimeo picture slot → upload → activate → sync to Namastream via multipart PUT to `/api/files/{file_id}`
- `upload_video` — TUS chunked upload to Vimeo → create new Namastream file record → swap media pointer → delete old file record (7-step process with progress callback)
- `add_media_to_product`, `add_media_to_playlist`
- `list_playlists`, `find_playlist_by_name`, `create_playlist`, `update_playlist`

### Helpers

- `_create_description(text)` — plain text → EditorJS JSON for event descriptions
- `create_rich_description(blocks)` — custom EditorJS blocks → JSON
- `_prepare_event_for_update()`, `_prepare_product_for_update()`, `_prepare_coupon_for_update()`, `_prepare_media_for_update()` — convert nested objects to ID arrays for PUT requests

## Authentication

Two-step flow:

1. `POST /auth/login/` with email + password (triggers magic code email)
2. `POST /auth/magic-code/` with magic code → returns `{ "key": "token..." }`

Token stored on `Client` instance. In production, token management is handled by `twy-announce/src/refresh_jwt.py` (Playwright-based browser automation). Token cached at `/root/twy/marvy/.marvy_auth.json` (gitignored), read by twy-class-plans at startup.

## Usage

```python
from marvy import Client, APIError, AuthError

# Initialize with existing token
client = Client(auth_token="your-token")

# Or with Vimeo token for media uploads
client = Client(auth_token="ns-token", vimeo_token="vimeo-bearer-token")

# Events
events = client.list_events(studio_slug="my-studio")
event_id = client.create_event(
    event_name="Morning Yoga",
    event_start_datetime="2026-02-01T09:00:00.000Z",
    event_end_datetime="2026-02-01T10:00:00.000Z",
    date="2026-02-01",
    start_time="09:00",
    duration_hours=1,
    duration_minutes=0,
    instructors=[123],
    products=[456],
)
client.update_event(event_id, event_name="Updated Name")
client.delete_event(event_id)

# Products
product_id = client.create_product(product_name="Monthly Membership")
tags = client.list_product_tags()

# Coupons
coupon_id = client.create_coupon(code="SAVE50", name="Half Off", discount_amount="50")
stats = client.get_coupon_stats()

# Customers
customer_id = client.create_customer(email="j@example.com", first_name="Jane", last_name="Doe")

# Media + Vimeo
media_items = client.list_media(page=1)
client.upload_thumbnail(media_id=999, image_path="/path/to/thumb.png")
client.upload_video(media_id=999, video_path="/path/to/video.mp4")
client.add_media_to_playlist(product_id=51605, playlist_id=9065, media_id=999)
```

## Exception Handling

```python
from marvy import Client, APIError, AuthError

try:
    client.get_event(event_id=99999)
except AuthError as e:
    # 401/403 or missing token
    print(f"Auth problem: {e}")
except APIError as e:
    # All other API errors (404, 429, 500, network, etc.)
    # Includes helpful context: endpoint URL, operation name, API-change hints for 404s
    print(f"API error: {e}")
```

`AuthError` is a subclass of `APIError`, so catching `APIError` catches both.

## Consumers

- **twy-class-plans** — publish/unpublish events, post-recording workflow (create media record, set metadata/thumbnail/product/series via `upload_video`, `upload_thumbnail`, `add_media_to_playlist`), Vimeo TUS upload
- **twy-announce** — daily status report reads subscription data via Metabase JWT (token refreshed by `refresh_jwt.py`)

## Known Limitations

- Token expiration behavior not fully documented
- Rate limiting not documented by HeyMarvelous
- Some instructor/product IDs must be obtained from existing data (no search/list-all for some resources)
- Media file creation (without replacing an existing record) requires the upload workflow — no simple POST with a file path
