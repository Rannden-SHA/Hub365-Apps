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
- **Alerts.** Through Microsoft Teams or webhook, plus Home Assistant integration.
- **Personal data.** Deleted automatically after 30 days, as the Spanish data protection agency (AEPD)
  recommends.
- **Web-based setup.** Cameras, NVR, gates, users, integrations and an installation guide.

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
