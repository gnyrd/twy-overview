# How does the website get found by Google and AI search?

## What is in place

Since 2 September 2026 the public site at [https://tiffanywoodyoga.com](https://tiffanywoodyoga.com) is served as static pages from the TWY server instead of WordPress. Every time the site is rebuilt and deployed, each page that should be found gets the pieces search engines and AI answer tools read:

- A short description under the title in Google results, taken from the first real paragraph of the page (or written by hand for the home, membership, about, blog, events, donations and privacy pages).
- A share card, so a link pasted into Facebook, Instagram, iMessage or Slack shows the page title, description and an image. Blog posts use their own cover image; other pages use a studio photo of Tiffany.
- Structured facts about the business and the author (Tiffany Wood, Tiffany Wood Yoga, the Instagram, Facebook and YouTube profiles, and for blog posts the headline and publication date). AI tools such as ChatGPT, Perplexity and Google's AI Overviews use these to cite a page.
- A sitemap at [https://tiffanywoodyoga.com/sitemap.xml](https://tiffanywoodyoga.com/sitemap.xml) listing the 34 pages worth indexing: the home page, membership, about, blog, events, donations, the new-year offer, the privacy policy and every blog post.
- A plain-text summary of the site for AI tools at [https://tiffanywoodyoga.com/llms.txt](https://tiffanywoodyoga.com/llms.txt).

Date archives, author pages, category pages and page 2 and 3 of the blog are deliberately marked as not worth indexing. They repeat the posts and would dilute the real pages.

Old addresses from the site before WordPress (for example /blog/some-old-post or /events/june-masterclass/) now send visitors to the blog or events page instead of a not-found page.

## What you need to do

Nothing for the pages themselves. The descriptions and cards are generated from the page content at every deploy, so editing a page and redeploying updates them.

One thing only a Google account owner can do: Google Search Console, which shows which searches bring people to the site, needs the site verified under a Google account. The WordPress plugin that did this before is gone with WordPress. JP will ask when he needs the account.

## What this will not do

- It does not write new pages or posts. Search traffic grows with content that answers what people search for; this work only makes the existing pages readable to search and AI tools.
- It does not change how any page looks. Everything added is invisible to visitors.
- It does not guarantee a Google ranking or an AI citation. It gives the site the same footing as a well-built site, which it did not have before.

Traffic to the site is measured in Plausible and summarised on the stats dashboard. The starting point on 2 September 2026: 281 visitors in the previous 30 days, 29 of them from Google.
