# Documentation

Your company's document management inside Hub365: **shelves, books, chapters and pages**, with a full editor
and each topic's **documents** (PDF, Word, Excel, images…) in the same place.

## What it does

- **Shelves and books.** Organise documentation like a library: shelves with a cover and colour, books with
  chapters and pages, and loose pages inside a book. Everything can be reordered by dragging.
- **Full editor.** Headings, lists, task lists, tables, callouts (info, success, warning, danger), code blocks with
  highlighting, collapsible sections, text highlighting, pasted or dropped images, embedded PDFs, file cards and
  links between pages (type `[[`). With keyboard shortcuts and their help.
- **Documents.** Every page has its **attachments** (drag-and-drop multi-upload) and every book has a
  **Documents** tab with all its files, a type filter and previews of PDFs, images and text.
- **Upload documents.** Upload several files at once to a book or chapter and each one becomes a page: Word,
  Markdown, HTML and text become editable content; PDFs are embedded and searchable by their text; anything
  else stays as a downloadable file.
- **Revisions.** Every save is a revision: compare two versions (words and source), go back to an earlier one
  and see who changed what.
- **Drafts and simultaneous editing.** The editor saves a draft while you type and tells you when someone else
  is editing the same page. If two people save at once, nobody overwrites the other's work.
- **Templates.** Meeting minutes, procedure, policy, step-by-step guide, report, FAQ, decision log, project… plus your
  own, with variables such as the date, the author or the book.
- **Import and export.** Import Markdown, HTML, text, Word, PDF or a ZIP with a whole book. Export pages,
  chapters and books to HTML, Markdown, text or ZIP, and print them (or save them as PDF) from the browser.
- **Search.** Searches titles, content, tags and the text of attached PDFs and Word documents, ignoring
  accents.
- **Favourites, recent items and trash.** Whatever you delete goes to the trash and can be recovered; it empties
  itself after the number of days you choose.
- **Who sees what.** Each book can be seen by everyone, only by certain Hub365 **departments** (or those of its
  shelf), or only by managers.
- **Audit and backups.** Change log for administrators, downloadable backup and automatic nightly backups.
- **Light or dark theme**, in Spanish or English, and mobile-friendly, with the same look as Hub365.

## Permissions

Each person's role is chosen in Hub365 › *Applications* › **Documentation** › **Access** and applies
immediately:

| Hub365 | In Documentation | Can |
|---|---|---|
| Viewer | **Viewer** | read, download, export and print what they can see; favourites |
| Editor | **Manager** | also create and edit shelves, books and pages, upload documents, import, templates and trash |
| Administrator | **Administrator** | everything: settings, emptying the trash, audit, users and backups |

Everyone uses their Hub365 account: there are no separate users or passwords.

## Requirements

- Hub365 **2.3** or later (Windows or Linux).
- **Docker** for the app container.
- A Hub365 licence that includes **Documentation** (`app:documentacion`).

## Installing from Hub365

1. *App catalog* › **Documentation** › **Install**.
   - If Hub365 controls Docker, it starts the container itself and publishes it at `/apps/documentacion/`.
   - If not, copy the `compose` file it shows you, start it on your Docker server (on the same network as
     Hub365) and Hub365 publishes it through its proxy.
2. Open the app from the portal. The first time it is empty: create a shelf and a book, or import what you
   already have (*Import*).

## Data and backups

The database and the files live in the Docker volume `documentacion-data`. They are kept when you update and
when you uninstall, unless you choose to delete them. **Hub365 backups do not include Docker volumes**:

- The app makes a backup every night inside the volume itself (`backups` folder, kept for the number of days
  you choose in *Settings*).
- In *Settings* › **Backup** you can download a full backup (database and files) as a ZIP.
- To copy the whole volume from the server:
  `docker run --rm -v hub365-documentacion_documentacion-data:/data -v "$PWD":/copia alpine tar czf /copia/documentacion.tgz -C /data .`

## What's new in 1.0.0

First release.
