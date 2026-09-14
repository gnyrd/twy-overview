# How do I see the files behind the TWY systems?

Everything TWY runs on lives in one folder on the Hetzner server, and [files.tiffanywoodyoga.com](https://files.tiffanywoodyoga.com/) shows that folder in the browser. Sign in as admin@tiffanywoodyoga.com with the same password as classes and clips. Live since 2026-09-14. The Files button at the bottom of the Classes calendar menu opens it, below Docs (this guide) and Stats.

## What you will find

- `classes/`: the Class Plans tool, the calendar and the blog editor.
- `clips/`: the Clips and Quotes tool.
- `www/`: the website build, every page of tiffanywoodyoga.com as it is served.
- `data/`: what the tools produce and keep: class plans, recordings and their clips, blog posts, exports, the deletions ledger.
- `announce/`: newsletters, campaigns, journeys and the social schedulers.
- `stats/`, `docs-scanner/`, `overview/`: the stats pages, and the generators behind this guide and the technical reference.
- The rest are smaller tools, one folder each, named for what they do.

Open any folder, preview a file, or download a copy. A search box at the top finds a file by name.

## What it will not do

- It never changes anything. There is no upload, edit, rename or delete, and the server itself refuses writes from this tool, whatever button might appear.
- It hides the secrets folder and every settings file that holds a key or a password. Those are not missing, they are kept out of the browser on purpose.
- It is not a way to edit the website. Blog posts are edited in the blog editor. Other pages of the site still change through JP.

## Who has been here

Visits are counted by Plausible, the same privacy-friendly analytics as the website (no cookies, no personal data), so files.tiffanywoodyoga.com has its own page at analytics.tiffanywoodyoga.com next to the website, the studio and the Habit page: how many people came, which folders they opened, from where. Since 2026-09-14. Plausible only sees browsers, so on top of it the server keeps a log of every request to this address, and that log is what answers whether anyone besides Tiffany and JP has reached the sign-in page or tried a password. JP reads it on request.
