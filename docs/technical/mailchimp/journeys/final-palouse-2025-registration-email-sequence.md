# FINAL Palouse 2025 Registration Email Sequence

**Classification**: ZOMBIE
**Why**: Status=sending but last enrollment 306 days ago (stale)

## Trigger

- Type: `unknown`
- Detail: `unknown`
- HM product: not mapped -- enrollment cannot be cross-referenced from marvy.db

## Sequence

| # | Type | Subject | Delay | Sent |
|---|------|---------|-------|------|
| 1 | action-send_email | Root Into the Light: Retreat Agreements & Sacred Prep ✨ | - | 0 |
| 2 | delay | - | 2 | 0 |
| 3 | action-send_email | Get Ready to Ignite Your Light: What to Bring 🔥 | - | 0 |
| 4 | delay | - | 1 | 0 |
| 5 | action-send_email | Your Sacred Weekend: Schedule + Locations 🌾 | - | 0 |
| 6 | delay | - | 1 | 0 |
| 7 | action-send_email | Prepare to Shine: Your Solstice Soul Map Awaits ✨ | - | 0 |

## Lifetime stats

- Started: 24
- Completed: 2
- In progress (API stat, stale): 0

## Enrollment

_Cannot cross-reference enrollment -- trigger is not HM-driven. See lint finding `mc_journey_trigger_unknown`._
