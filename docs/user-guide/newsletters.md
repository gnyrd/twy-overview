# How do newsletters work?

## Timeline

On the **25th of each month**, the system generates prompts for the next month's newsletter. For example, on March 25th, it generates the April newsletter.

## The review process

1. The system generates a draft newsletter automatically.
2. The draft appears in the **#review-newsletters** Slack channel for your review.
3. Reply with any edits, or approve it.
4. After you approve, JP schedules the send for early the next month (typically the first Tuesday).
5. If you don't respond within a few days, JP follows up.

## Two versions go out

- **Lifestyle** -- sent to current members (TYL subscribers).
- **Non-Lifestyle** -- sent to non-members, focused on the free Yoga Habit class.

Both use the same approved template design (blue background, cream card, sans-serif text).

## What you need to do

- Review the draft in Slack when it appears.
- Reply with any edits, or approve it.
- Everything else (scheduling, sending, audience targeting) is automated.

## Why the 25th matters

Class plans for next month need to be done by the 25th so the newsletter can reference them. At minimum, the Yoga Habit class date must have a plan by the 25th.

---

# Post-Habit follow-ups (PH1 and PH2)

Separate from the monthly newsletter. These go out around the free Yoga Habit class (second Saturday of each month).

## What PH1 and PH2 are

Two follow-up emails sent to people who attended or signed up for the monthly Yoga Habit class.

- **PH1** -- subject: "Thank you for practicing with us". Sends the day after the class.
- **PH2** -- subject: "Your center has not gone anywhere". Sends one week after PH1.

## Who they go to

Only non-Lifestyle members. Anyone tagged with the current month's `Yoga Habit - YYYY-MM` tag who is not already a Yoga Lifestyle member.

Existing Lifestyle members are excluded -- they already get the regular Lifestyle newsletter.

## What they contain

Both emails include the monthly coupon code (format: `HABIT_MONYYYY`, e.g., `HABIT_APR2026`) for $50 off the first month of a Yoga Lifestyle subscription. The coupon is generated automatically each month.

## Automation

The `run_habit_followup.py` cron job runs every day at 11am MT. It checks whether today is a Yoga Habit class day. If yes, it creates and schedules PH1 and PH2 in MailChimp. If no, it exits.

## What you need to do

Nothing. The PH1/PH2 copy is pre-written and was approved on 2026-04-13.

If the copy ever needs to change, JP edits the source files at `/root/twy/data/newsletters/` (PH1.md and PH2.md).

## Tracking

Redemptions are tracked automatically. When someone uses the coupon to subscribe, they get tagged `Yoga Habit - YYYY-MM - Redeemed` so we know the conversion came from the Habit funnel.
