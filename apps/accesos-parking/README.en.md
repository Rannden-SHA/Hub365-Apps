# Parking Access

Automatic log of **parking entries and exits by number plate**, from your cameras and **Frigate** (an NVR
with AI detection).

## What it does

- **Passage log.** Records each entry and exit with the number plate, the photo and the reading confidence.
  Doubtful passages are kept for review.
- **Second reading.** If Frigate can't read the plate, the app reads it from the video with its own YOLOv9
  detector and OCR (MIT licensed).
- **Vehicles.** A list of vehicles with their type (employee, visitor, supplier…). Gates can open on their
  own for the types and hours you choose (iSmartGate / Gogogate2, Home Assistant, Tasmota or webhook).
- **Quick search.** Type a plate at the top (shortcut `/`) and see at once whether it's inside, who it
  belongs to and its latest passages.
- **Blacklist.** Plates to watch: they show in red across the app, raise an alert when they come in and
  the gate never opens on its own for them.
- **Visitors.** Pre-register who is coming: when their plate is read you see who they are and who they're
  visiting, and no unknown-plate alert is raised.
- **Statistics.** Peak hours, hourly occupancy, length of stay, most frequent vehicles and plate reading
  quality.
- **Reception screen.** A full-screen view for a reception or gatehouse monitor that refreshes on its own.
- **Alerts.** Through Microsoft Teams or webhook, plus Home Assistant integration.
- **Personal data.** Deleted automatically after 30 days, as the Spanish data protection agency (AEPD)
  recommends.
- **Web-based setup.** Cameras, NVR, gates, users, integrations and an installation guide.
- **Light or dark theme.** Follows your system or the one you pick in your account menu. Works on mobile
  too.

The app's screens are in Spanish.

## Requirements

- Hub365 2.3 or later (1.3.0 works with 2.2), **on Linux with Docker**. The app is a container and needs about 2 GB of RAM for
  the second reading.
- Frigate 0.16 or later with number plate recognition (LPR) and its MQTT. The Home Assistant one works.
- A Hub365 license that includes **Parking Access** (`app:accesos-parking`).

## Installing from Hub365

1. *App catalog* › **Parking Access** › **Install**.
   - If Hub365 controls Docker, it starts the container itself and publishes it at `/apps/accesos-parking/`.
   - If not, copy the `compose` it shows you, start it on your Docker server (on the same network as
     Hub365) and Hub365 publishes it through its proxy.
2. Open the app and follow its **guide** (*Settings › Guide*): Frigate, MQTT, cameras and gates.

The data (database and photos) goes in the `accesos-parking-data` volume. It's kept when you update and
when you uninstall, unless you choose to delete it.

## What's new in 1.5.2

- **A car that passes once is a single passage.** Sometimes a car leaving showed up as two exits: Frigate
  tracked the same car with two objects (for example, a car parked in the background that briefly "takes"
  the box of the one leaving) and the second one arrived without a plate or without a direction. It is now
  merged into the existing passage, also when its plate arrives later (second reading), and the passage that
  stays keeps the best reading and the direction the camera saw.
- Two **almost identical** readings from the same camera within a few seconds (one different character, or
  letters that get mixed up such as 0/O or 6/G) count as the same car. New setting in *Settings ›
  Recognition*: **Seconds to merge similar readings** (30 by default; 0 = don't merge).
- Two different cars leaving one after the other, or an exit and an entry, are still separate passages.

## What's new in 1.5.1

- Reading the gate log waits as long as the iSmartGate takes to return a day with many events (in 1.5.0
  the first copy could stop at "timed out").

## What's new in 1.5.0

- **Gate log** (iSmartGate only): Parking Access copies the event log from the iSmartGate's local web page
  using the controller's user and tells you, for each opening, **who or what opened it**: the iSmartGate app
  (with the user and whether it was remote or local), Parking Access (automatic or manual), a remote control
  or another external route. It also shows how long it stayed open and any obstructions.
- **Each car with its opening**: the first car through gets the origin; the next ones show as "Came in
  behind #N". It also flags cars with no recorded opening and openings with no car. New **Opening** column
  in the passes log.
- **Matching** between iSmartGate users and people in Parking Access: the app suggests them and an
  administrator confirms them.
- Alerts for a gate left open too long, a missing close event and a remote control used by someone whose key
  is the app; periods with no data (for example, when the connection drops) are marked.
- Turn it on in the iSmartGate controller's page (**Read the event log**); it's off by default. Parking
  Access only reads the log: it never clears it or changes anything on the device.

## What's new in 1.4.0

Requires **Hub365 2.3**: upgrade Hub365 first and then the app.

- **Hub365 decides the role**: who is administrator, manager or read-only in Parking Access is chosen in
  Hub365 › *Apps* › **Parking Access** › **Access** (or in each person's *Apps* tab) and applies on the
  next request. Extra permissions (open the gate, configure) stay in the app. The roles there were before
  the first change are saved in the audit log.
- **Each person is matched by their Hub365 account**, not by email: nobody can take over someone else's
  record by changing their email. Administrators can unlink a record.
- **Deduced direction**: when the camera can't tell whether the car was coming in or going out but the plate
  matches a registered vehicle exactly, the direction is deduced from its last pass and it doesn't wait for
  review. The gate doesn't open automatically on those passes.
- **Old Spanish and foreign plates**: provincial plates (e.g. IB-1234-BC) and any plate that matches a
  registered vehicle exactly are recognised. Unknown foreign plates are kept for review. *Settings ›
  Recording and detection* sets the format Frigate accepts.
- **Edit vehicles** from the person's record, without deleting and re-creating them.

## What's new in 1.3.0

- **Custom fields for people**: create from the app the data you need to keep for each person (for example
  "Remote", "Parking space" or "Card"), as text, number, date, yes/no or a list of options, without waiting
  for a new version. They show on every person's record, are filled in only where needed, can be shown as a
  column in the list, are searchable and go in the Excel export and import.
- **Side menu**: the group of the section you are in is highlighted.

## What's new in 1.2.0

- **Backups**: manual and scheduled backups (with or without photos, optionally encrypted), download,
  restore checked before it is applied, and import/export of people and vehicles (CSV) and of the settings
  without secrets.
- **Extra recording for unknown vehicles**: when a plate belongs to nobody, Frigate is asked for a few more
  seconds of video; it stops early if the plate turns out to be known.
- **Frigate recording and detection settings** from the app (days kept, seconds before and after,
  thresholds), with a backup first and rollback if Frigate rejects them.
- Better reading: parked cars are no longer mixed up with the one driving past, fewer arrivals split in two
  and fewer false "unknown" vehicles.
- Accordion side menu: opening a group closes the others.

## What's new in 1.1.0

- New interface, matching Hub365: grouped side menu with your account inside, light or dark theme and a
  better mobile layout.
- Quick search, blacklist, pre-registered visitors, occupancy statistics and a reception screen.
- Updating from 1.0.0 keeps all your data.
