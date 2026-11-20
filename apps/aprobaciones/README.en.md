# Approvals

Approval workflows inside Hub365: **request types** with their own form, **stages** with who approves and in
what order, **deadlines** in working hours and a **PDF receipt** that can be verified.

## What it does

- **Request types.** Each type has its form, its flow, its numbering (for example `COMP-2026-0007`) and who can
  request it. Types have **versions**: a request keeps the version it was sent with, even if a new one is
  published.
- **Built-in templates.** Purchase / order, expense report, vacation and absence, business trip, overtime,
  contract or document, system account or access, IT change, equipment loan and general approval. They are
  installed and changed like any other type.
- **Forms.** 25 field types: text, numbers and amounts, dates and ranges, lists, people, department, files, line
  tables with totals and calculated fields. A field can show up or become required only when a condition is met.
- **Stages and approvers.** A person, a group, the requester's manager (or one further up, up to 10 levels), the
  head of the department, someone chosen in the form or an **authority matrix** (by amount, department…). Each
  stage can ask everyone, the first one, a **quorum** (with veto) or go one after another. Stages can run in
  parallel and be skipped when their condition is not met. A **simulator** tells you who would approve and with
  what deadlines.
- **Deciding.** Approve, reject, return for changes or the type's own responses. You can also reassign, add an
  approver or **consult** someone without a vote. A stage can require a comment or a **signature** (typing your
  name). You can approve several at once.
- **Return and resubmit.** On resubmitting, a new revision is saved with the field-by-field differences and a
  note.
- **Deadlines.** In working or calendar hours, with **calendars** (hours per day and holidays). Reminders and, if
  still undecided after the hours you choose, escalation: notify, reassign, add someone or approve or reject on
  its own. Urgent requests get half the time.
- **Absences and delegations.** In *My absence* you choose a substitute and some dates: new tasks go to the
  substitute, or both see them (the first decision counts).
- **Inboxes and search.** Waiting for me, my requests (with who is missing), I'm involved, all requests and
  drafts. Saved filters, search and keyboard shortcuts.
- **Confidential requests.** Only the people taking part see the data; administrators and the type's managers
  only see the header.
- **Timeline with a hash chain.** Every step is recorded with its SHA-256 hash, chained to the previous one. The
  **PDF receipt** has the data, the decisions, the signatures, the attachments with their hash and the chain. In
  *Verify receipt* you check with the number and the hash whether it matches or has been altered.
- **Notifications.** The app's bell, email with a "Review and decide" button, daily digest, **Microsoft Teams**
  (a card in a channel, general or per type) and **webhooks** signed with HMAC, with retries and a log.
- **Reports.** Volume, approval rate, cycle time (median and p90) by type, stage and approver, deadline
  compliance, bottlenecks, rejection reasons, workload and amounts, in clock or working hours. Reports and
  inboxes export to CSV and Excel.
- **Own API.** Tokens created in *Settings › API* to create and look up requests and decide tasks from other
  programs. Requests still go through Hub365: without a Hub365 session they only get through if the public portal
  is on and the app can be seen without signing in.
- **Audit, retention and backups.** Change log for administrators, deletion of closed requests after the number
  of days you choose for each type, and backups.
- **Light or dark theme**, in Spanish or English, and mobile-friendly, with the same look as Hub365.

## Permissions

Each person's role is chosen in Hub365 › *Applications* › **Approvals** › **Access** and applies immediately:

| Hub365 | In Approvals | Can |
|---|---|---|
| Viewer | **User** | request the types they are allowed to, decide what is assigned to them, comment, see their own requests and those they take part in, their absence and their notifications |
| Editor | **Process manager** | also create types and manage their own (form, flow, versions and their requests), groups, calendars and reports on their types |
| Administrator | **Administrator** | everything: all requests, people and departments, other people's delegations, settings, Teams, API, webhooks, audit and backups |

Everyone uses their Hub365 account: there are no separate users or passwords.

## Requirements

- Hub365 **2.3** or later (Windows or Linux).
- **Docker** for the app container.
- A Hub365 licence that includes **Approvals** (`app:aprobaciones`).

**With Hub365 2.4** the app uses Hub365's app API. It asks for three permissions, which are granted on install
and can be withdrawn in *Applications* › **Approvals** › **Hub365 integration**:

- **People directory** (`directory`): reads Hub365's people and departments, with their job title and manager,
  to choose approvers who have not opened the app yet.
- **Hub365 notifications** (`notify`): also notifies in the Hub365 bell.
- **Email** (`mail`): sends emails through Hub365's SMTP, only to Hub365 users.

**With Hub365 2.3** (or without those permissions) the app still works: it gets to know people the first time
they come in, and you can import them from a CSV file (with job title and manager). Emails go through the app's
own SMTP (*Settings › Email*) and notifications show in the app's bell.

## Installing from Hub365

1. *App catalog* › **Approvals** › **Install**.
   - If Hub365 controls Docker, it starts the container itself and publishes it at `/apps/aprobaciones/`.
   - If not, copy the `compose` file it shows you, start it on your Docker server (on the same network as
     Hub365) and Hub365 publishes it through its proxy.
2. Open the app from the portal as an administrator. Check the calendar and the settings, and install the types
   you need from *Templates*.

## Data and backups

The database and the attachments live in the Docker volume `aprobaciones-data`. They are kept when you update
and when you uninstall, unless you choose to delete them. **Hub365 backups do not include Docker volumes**:

- The app makes a backup every night inside the volume itself (`backups` folder, kept for the number of days
  you choose).
- In **Backups** you can download a full backup (database and files) as a ZIP.
- To copy the whole volume from the server:
  `docker run --rm -v hub365-aprobaciones_aprobaciones-data:/data -v "$PWD":/copia alpine tar czf /copia/aprobaciones.tgz -C /data .`

## What's new in 1.0.0

First release.
