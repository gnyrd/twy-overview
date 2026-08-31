# How do campaigns work?

A campaign sends a set of emails to a whole audience, on a schedule. That is the difference from a welcome sequence: a sequence sends to one person when they buy a product, while a campaign sends to a group of people you choose. The monthly free-class invitations and the member newsletter are both campaigns.

## Where to go

Open [https://classes.tiffanywoodyoga.com/journeys](https://classes.tiffanywoodyoga.com/journeys), or click **Emails** in the toolbar above the class calendar. A campaign sits in the same list as your welcome sequences. A one-time campaign is labeled **Campaign**; one that runs every month is labeled **Monthly**, in its own lavender capsule.

## How do I send a one-off newsletter?

**New**, then **Newsletter**, is the fast path for when you just want to write one email and send it to one audience on one date. It skips everything below that a simple newsletter does not need: no sequence of other emails, no send condition, no resend, nothing recurring. Under the hood it saves as a one-time campaign, so once it exists it sits in your Emails list, tagged **Newsletter**, and from there it works exactly like any other one-time campaign.

1. Open **Emails**.
2. Click **New**, then **Newsletter**.
3. Give it a title and choose who it goes to.
4. Pick the date and time it sends, or choose Send immediately.
5. Write the subject, preheader and body.
6. Save.
7. On its own page, tick the email **Approved** and turn it **On**.
8. Click **Review launch** to see exactly what it will send and to whom.
9. Click **Confirm and schedule**. Nothing sends before that click. If the time you picked passes while you are writing, the confirm page says so and offers Send Now.

Your Emails list tags every row **Newsletter**, **Campaign**, **Monthly** or **Journey**, and the checkboxes above the list show or hide each kind. A second row of checkboxes filters by where each one is in its life: **Active** has started and is not finished, **Approved** is ready and waiting for its start date, **Pending** is still waiting on approval or a sending condition, and **Complete** is all done. Each row's capsule shows the same four states, so the capsule you see and the boxes you filter with always speak the same language. Both groups apply together, so you can look at, say, only campaigns that are still pending.

## What is built and what is not

You can build a campaign now: write its emails, set who each one goes to, set the conditions below, and see the whole thing laid out. When JP launches it, the system schedules every email for the period, honoring each of those settings.

What is not switched on yet: your live monthly newsletters and class invitations still go out through the current system, unchanged, up until a campaign's own first period arrives. This new campaign builder runs alongside the current system until then. A campaign set to run every month is different: once JP turns it On and every email is approved, it can sit fully armed for a future period, then launches itself each month from its first period onward, with nothing more for JP to do per period.

## Who each email goes to

The campaign has one audience, and by default every email in it goes to that audience. Any single email can override that and go to its own audience instead. That is how one campaign sends an invitation to people who are not members and, in the same campaign, a day-before reminder only to the people who registered.

On each email, **Who this email goes to** is either *Use the campaign audience* or a segment you pick. Leave it on the campaign audience unless that one message really targets a different group.

The Emails list on the campaign page states each row's real audience too, woven into its timing line, so you can see who everything goes to without opening each email. Opening an email shows the same two facts in its top card: the calendar date it will actually send (worked out from the run date and the waits between emails) and who it goes to.

## Only send when it makes sense

Each email has a **send condition**. Most of the time it is *No Sending Conditions*, meaning it sends on its schedule no matter what. The other choices hold an email back until a fact is true:

- *Only if there is a class that month* skips the invitation set in a month with no free class. A class counts only once its plan is actually written: a date reserved with a placeholder does not send invitations, so nobody is ever invited to a class that has not been created yet.
- *Only once the recording is ready* holds the recording email until the edited class video is attached to its free product.
- *Only after the class has happened* keeps a follow-up from going out before the class.

A held email holds **only itself**. The rest of the campaign still sends on schedule. The condition is checked at the moment each email would go, so a class added late or a recording attached late still lets the email through.

## Resend to people who did not open

Any email can resend itself to the people who did not open it the first time. Turn on **Resend to people who did not open it** and it adds a follow-up under that email in the list.

- Its audience is fixed: the people who did not open the original. You do not pick it.
- It goes a set number of days **after the original sends**, so the opens have time to come in first.
- It reuses the original's subject and words unless you give it a new subject or body, which most people do to catch a second glance.
- If the original never sent, held by its condition, the resend does not send either. There is no one to be a non-opener of.

One resend per email. A resend does not get a resend of its own.

## One time or every month

A campaign is **One time** or **Every month**. A one-time campaign, like a seasonal series, runs once on the date you set. A monthly campaign runs every month with no new date picked each time, because each of its emails is anchored to the month instead of a fixed day.

An anchored email hangs on one of three points and shifts by a number of days: **the first weekday of the month**, **the class date**, or **a weekday before the class**. A day offset of minus one on the class date means the day before class; plus one means the day after. The weekday choice lands the email on, say, the Monday before whatever day the class falls on, so an invitation keeps its weekday even in a month when the class is not a Saturday. That is what lets the same campaign send before whatever this month's class turns out to be, without anybody editing a date.

Each email can also set its own **send time**, an hour and a minute, or leave both blank to use the campaign's default time. This is optional and separate from the anchor.

## The class plans come first

A campaign email anchored to the class date cannot work out its own date until that month's class plans exist. Your class plans stay the single source everything else follows. The campaign only removes the manual step of retyping the copy; it never authors a class for you.

## Where an email's copy comes from

Each campaign email has a **Copy source**. Left on **Written here**, it sends the subject and body you type in its editor, which is how a one-time campaign works. Set to one of the monthly drafts (the member newsletter, the class invitation, and so on), it sends that month's draft instead, so a recurring campaign carries fresh copy each month with nothing retyped.

An email set to a draft waits until that draft is ready. If the month comes and the draft has not been written, that one email holds and the rest of the campaign still sends, the same way a send condition holds an email. It never falls back to old placeholder text.

A draft can also name things that are not settled until later in the month, like the class title or the recording link. Those fill in automatically from that month's real details right before the email goes out. If one of them is not ready yet, for example the recording link before the recording is posted, that email waits too, the same way it waits on the draft itself. It never sends with a placeholder still sitting where a name or a link should be.

## Who an email goes to

Each campaign email has an audience. Most send to **the campaign audience**, the segment the whole campaign is set to. An email may instead pick **a specific segment** of its own, so one campaign can invite non-members and remind registrants.

Two audiences are worked out fresh each time the campaign sends, so you never build a list by hand:

- **Interested non-members**: everyone who registered for that month's free class and has not become a member. This is who the follow-up emails go to.
- **Openers of an earlier email who did not register**: people who opened one earlier email in the same campaign (you pick which) and still have not registered. This is the gentle reminder's audience. Because it is built from that earlier email's opens, it only goes out after that email has sent; if that email held this month, the reminder holds too.

## Approving a campaign

Each email carries an **Approved** box in its editor. Tick it and save to approve that email's copy. Any later save without the box ticked clears the approval, because the copy just changed and a stale approval must not carry to words you have not signed off.

The campaign page shows the running count, like **1 of 3 approved**, and each email reads **Approved** or **Needs approval**. A campaign can be launched only once the **whole set** is approved, not one email at a time. Until every email is approved, the launch button is replaced by a note saying how many are left.

## When a campaign actually sends

A **one-time** campaign, like a seasonal series, is launched from its own page: **Review launch** shows exactly what it would schedule, who each email goes to and when, and **Confirm and schedule** sends it. Nothing sends before that second click.

A **monthly** campaign launches itself. Once it is On and every email is approved, the system sends it each month on its own, on the dates each email is anchored to, with no button to press. The campaign page says so in place of the launch button. Nothing sends until it is On, fully approved, and its first period has arrived, so a campaign can sit fully armed and still not be sending anything yet.

For a monthly campaign, approval starts over every month. The Approved boxes on its emails approve the setup (who, when, which draft each email reads). The words themselves are approved month by month, through that month's newsletter drafts: an email whose draft for the month is not yet approved simply waits, and sends once it is. So a new month always begins as Pending and becomes Approved when you approve that month's drafts, and last month's approval never sends this month's words.

Nothing about a monthly campaign's emails locks once a period has sent: the subject, body and Approved box stay editable. Once that month's run has gone out, its campaign page and each email's editor show a plain note that the run is complete, so you know any change you save now is for the next period, not the one that already went.

The email carrying the class recording waits for the recording to be attached to its free product before it may send. The system now checks this on its own at send time: once the edited recording is attached to the month's free product, that email goes out with the rest of the campaign. Until it is attached, that one email holds and every other email in the campaign sends normally.

## Seeing what it has sent

A campaign page has a **Sent history** section listing every month the campaign has ever sent, with each email's sent, opened and clicked. This reaches back before the new system: the monthly Yoga Habit and Yoga Lifestyle mailings that went out through the earlier version of the monthly setup show here too, so nothing is lost in the switch-over. Opened counts people, not the automatic scans some mail apps do, so it is a floor and the true number is a little higher. Sent is those actually delivered.

Months that have not sent yet but come before the campaign takes over also appear as their own rows, so the list shows September even while the campaign itself starts in October. Their state follows that month's draft approvals. When a month's push to the same audience already has its own campaign (the way Transitions carries September for non-members), only that campaign's row shows for the month.

The Emails list works as the same ledger, one row per month. A monthly campaign appears once for every month it has sent, each marked **Complete** (months sent by the earlier version of the monthly setup included). Its rows read **Monthly: name: month**, so an August row says 2026_08. A month that has not arrived shows no row at all: the list never shows a future month it has nothing for. All of a Monthly's rows open the same page, and that page is headed with just the name, no month, because it is the machine that runs every month rather than any one month's sending. Months that finished before the campaign system took over sit at the very bottom of the list: they are the archive, not the news. A one-time campaign whose emails have all gone out shows **Complete**: it is finished work and will not send again.

## Deleting one that never went out

A campaign or journey that is off and has never sent can be deleted from its own page. A **Delete** button appears there only when that is true. The confirmation says plainly that deleting it is permanent and cannot be undone, and names the one you are about to delete.

Anything that is on, has ever sent (even once, even a single email), or already has anyone in it, active, stopped or finished, cannot be deleted this way, and the button does not appear on its page. Turn it off instead if it should stop running.

## One thing to know about punctuation

Saving converts em-dashes to commas, the house rule for every TWY email and name. Colons, apostrophes and emoji come through exactly as you typed them.

## What you need to do

Write and edit the copy, set each email's audience, condition and resend, and approve each email. A monthly campaign then launches itself; a one-time campaign is launched with Review launch and Confirm and schedule, and JP handles the switch-over from the current newsletter system.

## If something breaks

If the Emails page will not load, a campaign will not save, or the audience list comes up empty, contact JP.
