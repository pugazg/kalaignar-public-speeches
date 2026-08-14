# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **T1 first-pass Batch 1**. It exists so continuation proceeds from the exact next incomplete batch without restarting source inspection or redoing drafted pages.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/poonthottam/`
- Stable slug: `poonthottam`

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

**IN PROGRESS - 5 / 12 speech pages drafted.**

Completed T1 Batch 1:

- PDF 6 / printed 5
- PDF 7 / printed 6
- PDF 8 / printed 7
- PDF 9 / printed 8
- PDF 10 / printed 9

These pages are present in `transcription-ta.md` as **first-pass text only**. They have not been declared verified.

Remaining T1:

- PDF 11 / printed 10
- PDF 12 / printed 11
- PDF 13 / printed 12
- PDF 14 / printed 13
- PDF 15 / printed 14
- PDF 16 / printed 15
- PDF 17 / printed 16

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**NOT STARTED.** Must wait until the complete 12-page first-pass Tamil body exists.

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED / BLOCKED.**

### English gates

All **NOT STARTED / BLOCKED** until Tamil reaches `verified-complete`.

## Preliminary T1 source watchpoints

These are not final audit resolutions; re-check them in T2:

- printed p.5 → p.6 continues `பண்படுத்த` / `வேண்டும்.` across the page boundary;
- printed p.6 → p.7 continues `...மொண்டு மொண்டு தரும்` / `தென்றலாக, ...`;
- printed p.6 visibly has `பரவசத்திலீடுபடுகிறான்`;
- printed p.6 transition wording is `அடுத்தது,`;
- printed p.6 retains the unusual phrase `அகம்புற மென்ற அன்றலர்ந்த`;
- printed p.7 phrase reads `சீர் குலுங்கும்`;
- printed p.8 emphasizes the joined form `அந்தக்காலம்`;
- printed p.9 contains the unusual source form `அயோத்தியானுக்கு`.

Do not normalize these merely because a modern or contextually smoother reading seems likely.

## Exact next activity

Continue **Stage T1 only** with the next working batch:

**PDF pages 11-15 / printed pages 10-14.**

Preserve explicit PDF/printed-page boundaries. Do not translate. Do not begin the strict T2 audit yet.

After that five-page batch, finish T1 with PDF pages 16-17 / printed pages 15-16. Only when all 12 speech pages are drafted may Stage T2 begin.

## Repository synchronization note

The root catalogue remains unchanged during T1. Per the repository processing guide, root catalogue synchronization belongs to archival closure after all textual gates pass.

`metadata.json`, the speech-level `README.md`, `transcription-ta.md`, `audit.md`, and this handover should remain synchronized with the current T1 page counters.
