# Retreat Info – Auto Send

**Classification**: ZOMBIE
**Why**: Status=sending but last enrollment 303 days ago (stale)

## Trigger

- Type: `unknown`
- Detail: `unknown`
- HM product: not mapped -- enrollment cannot be cross-referenced from marvy.db

## Sequence

| # | Type | Subject | Delay | Sent |
|---|------|---------|-------|------|
| 1 | delay | - | - | 0 |
| 2 | action-send_email | Everything You Need for the Solstice Retreat 🌿 | - | 0 |

## Lifetime stats

- Started: 0
- Completed: 0
- In progress (API stat, stale): 0

## Enrollment

_Cannot cross-reference enrollment -- trigger is not HM-driven. See lint finding `mc_journey_trigger_unknown`._
