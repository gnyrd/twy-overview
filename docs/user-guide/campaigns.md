# How do campaigns work?

A campaign sends a set of emails to a whole audience, on a schedule. That is the difference from a welcome sequence: a sequence sends to one person when they buy a product, while a campaign sends to a group of people you choose. The monthly free-class invitations and the member newsletter are both campaigns.

## Where to go

Open [https://classes.tiffanywoodyoga.com/journeys](https://classes.tiffanywoodyoga.com/journeys), or click **Emails** in the toolbar above the class calendar. A campaign sits in the same list as your welcome sequences and is labeled **Campaign**.

## What is built and what is not

You can build a campaign now: write its emails, set who each one goes to, set the conditions below, and see the whole thing laid out. When JP launches it, the system schedules every email for the period, honoring each of those settings.

What is not switched on yet: your live monthly newsletters and class invitations still go out through the current system, unchanged, up until a campaign's own first period arrives. This new campaign builder runs alongside the current system until then. A campaign set to run every month is different: once JP turns it On and every email is approved, it can sit fully armed for a future period, then launches itself each month from its first period onward, with nothing more for JP to do per period.

## Who each email goes to

The campaign has one audience, and by default every email in it goes to that audience. Any single email can override that and go to its own audience instead. That is how one campaign sends an invitation to people who are not members and, in the same campaign, a day-before reminder only to the people who registered.

On each email, **Who this email goes to** is either *Use the campaign audience* or a segment you pick. Leave it on the campaign audience unless that one message really targets a different group.

The Emails list on the campaign page states each row's real audience too, woven into its timing line, so you can see who everything goes to without opening each email.

## Only send when it makes sense

Each email has a **send condition**. Most of the time it is *Always send*. The other choices hold an email back until a fact is true:

- *Only if there is a class that month* skips the invitation set in a month with no free class.
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

Nothing about a monthly campaign's emails locks once a period has sent: the subject, body and Approved box stay editable. Once that month's run has gone out, its campaign page and each email's editor show a plain note that the run is complete, so you know any change you save now is for the next period, not the one that already went.

The email carrying the class recording waits for the recording to be attached to its free product before it may send. The system now checks this on its own at send time: once the edited recording is attached to the month's free product, that email goes out with the rest of the campaign. Until it is attached, that one email holds and every other email in the campaign sends normally.

## Seeing what it has sent

A campaign page has a **Sent history** section listing every month the campaign has ever sent, with each email's sent, opened and clicked. This reaches back before the new system: the monthly Yoga Habit and Yoga Lifestyle mailings that went out through the old setup show here too, so nothing is lost in the switch-over. Opened counts people, not the automatic scans some mail apps do, so it is a floor and the true number is a little higher. Sent is those actually delivered.

## One thing to know about punctuation

Saving converts em-dashes to commas, the house rule for every TWY email and name. Colons, apostrophes and emoji come through exactly as you typed them.

## What you need to do

Write and edit the copy, set each email's audience, condition and resend, and approve each email. A monthly campaign then launches itself; a one-time campaign is launched with Review launch and Confirm and schedule, and JP handles the switch-over from the current newsletter system.

## If something breaks

If the Emails page will not load, a campaign will not save, or the audience list comes up empty, contact JP.
