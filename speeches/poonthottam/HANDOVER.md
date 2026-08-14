# கலைஞரின் பூந்தோட்டம் - startup handover

This handover records the completed **source-inspection startup gate** for `speeches/poonthottam/`. It is intentionally written before transcription begins so another chat can continue at the exact next incomplete stage without redoing source establishment.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/poonthottam/`
- Stable slug: `poonthottam`

## Mandatory startup completed

The following were completed before any transcription work:

- repository-level `SPEECH_PROCESSING_GUIDE.md` read completely;
- root `README.md` read;
- completed `speeches/arappor/` reference implementation studied, especially `README.md`, `metadata.json`, `audit.md`, `translation-review.md`, and `HANDOVER.md`;
- repository inspected for duplicate work;
- actual attached scan inspected rather than relying on the upload filename;
- source checksum, file size, PDF count, bibliographic evidence, and page map established;
- initial archival files created;
- **no bulk Tamil transcription begun**;
- **no English translation begun**.

## Source identity

- Source filename: `TVA_BOK_0065784_கலைஞரின்_பூந்தோட்டம்.pdf`
- SHA-256: `2a8bf5f6f42970ee95912f41662f9bc448581a5aaca15a55fee9b44ba20a4c52`
- File size: `49,297,657` bytes
- Actual PDF page count: `18`
- Source binary committed: **No - repository policy prohibits uploading the source PDF**

## Source-established speech facts

Title page:

`கலைஞரின் பூந்தோட்டம்`

`சென்னை கிண்டி இன்ஜினியரிங் கல்லூரியில் 06.12.1951இல் தோழர் மு.கருணாநிதி ஆற்றிய சொற்பொழிவு`

Therefore:

- speech title in body: `பூந்தோட்டம்`;
- speech date: **1951-12-06**;
- venue: **சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி**;
- speaker: **தோழர் மு.கருணாநிதி**;
- event/occasion: **not separately stated**;
- audience: **not explicitly stated**.

Do not replace these source-grounded fields with historical inference.

## Edition / publication evidence

PDF page 3 records:

- `முதற்பதிப்பு - 1951 (திராவிடப் பண்ணை)`;
- `நான்காம் பதிப்பு : 2019`;
- `திராவிடர் கழக (இயக்க) வெளியீடு` as current publisher / rights holder;
- `‘விடுதலை’ ஆஃப்செட் பிரிண்டர்ஸ், சென்னை - 600 007.` as printer;
- `நன்கொடை (குறைந்த அளவு): ரூ.12/-`.

PDF page 4 is a publisher's preface dated 12.01.2018; that date is front-matter evidence, **not** the speech date.

## Canonical page map

- PDF 1 - front cover
- PDF 2 - title page / speaker photo / explicit speech date and venue
- PDF 3 - bibliographic page (`நூல் குறிப்பு`)
- PDF 4 - publisher preface (`பதிப்புரை`)
- PDF 5 - prefatory poem `எரிமலை! (மு.கருணாநிதி)`
- PDF 6-17 - speech body, printed pages 5-16 (**12 pages total**)
- PDF 18 - back cover / promotional matter / barcode

The speech begins on PDF 6 under `பூந்தோட்டம்` and ends on PDF 17 with `வணக்கம்`.

## Scan-specific safeguards

- Blue circular library stamp on PDF 2 overlaps the title-page area: later marking, not edition text.
- Blue circular library stamp on PDF 17 lies below the speech ending: later marking, not edition text.
- Light bleed-through occurs on interior pages: do not transcribe reverse-side ghost text.
- Visually inspect the scan whenever any Tamil reading is uncertain; OCR/parsed text is never authoritative.

## Workflow state

### Gate 1 - source inspection / bibliographic and page map

**COMPLETE.**

### Gate 2 / T1 - Tamil first-pass transcription

**NOT STARTED.** 0 / 12 speech pages drafted.

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**NOT STARTED.** Must wait until the complete first-pass Tamil body exists.

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED.**

### English gates

All **NOT STARTED / BLOCKED** until Tamil reaches `verified-complete`.

## Exact next activity

Proceed with **Stage T1 only**: first-pass Tamil transcription of the complete speech body **PDF pages 6-17 / printed pages 5-16**.

Recommended first working batch: **PDF pages 6-10 / printed pages 5-9**. Preserve explicit PDF/printed-page boundaries. Do not translate during T1, and do not mark any page visually verified merely because a first-pass transcription exists.

After all 12 pages are drafted, only then begin the independent strict T2 scan comparison across every line of every speech page.

## Repository synchronization note

The root catalogue has **not** been changed during this startup gate. Per the repository processing guide, final catalogue synchronization belongs to archival closure after the textual gates pass. `metadata.json`, the speech-level `README.md`, and this handover reflect the current startup state.
