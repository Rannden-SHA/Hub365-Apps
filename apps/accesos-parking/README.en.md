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

- Hub365 2.2 or later, **on Linux with Docker**. The app is a container and needs about 2 GB of RAM for
  the second reading.
- Frigate 0.14 or later with number plate recognition (LPR) and its MQTT. The Home Assistant one works.
- A Hub365 license that includes **Parking Access** (`app:accesos-parking`).

## Installing from Hub365

1. *App catalog* › **Parking Access** › **Install**.
   - If Hub365 controls Docker, it starts the container itself and publishes it at `/apps/accesos-parking/`.
   - If not, copy the `compose` it shows you, start it on your Docker server (on the same network as
     Hub365) and Hub365 publishes it through its proxy.
2. Open the app and follow its **guide** (*Settings › Guide*): Frigate, MQTT, cameras and gates.

The data (database and photos) goes in the `accesos-parking-data` volume. It's kept when you update and
when you uninstall, unless you choose to delete it.

## What's new in 1.1.0

- New interface, matching Hub365: grouped side menu with your account inside, light or dark theme and a
  better mobile layout.
- Quick search, blacklist, pre-registered visitors, occupancy statistics and a reception screen.
- Updating from 1.0.0 keeps all your data.
