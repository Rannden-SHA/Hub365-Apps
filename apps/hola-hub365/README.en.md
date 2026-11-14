# Hello Hub365

Sample app from the Hub365 catalog. It greets the user who opens it and counts the visits.

It's there to check that the catalog works end to end:

- **Signed identity.** The app knows who opens it thanks to the `X-Hub365-*` headers signed by Hub365
  (signature `v2`).
- **License.** It checks that your Hub365 license includes `app:hola-hub365`. If it doesn't, it shows
  "Needs a license".
- **Data.** The visit counter is stored in the app's data folder and is kept when you update or uninstall
  it.

No dependencies needed: just the Python that comes with Hub365.
