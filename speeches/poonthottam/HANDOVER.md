# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **T2 strict audit Batch 1**. It exists so continuation proceeds from the exact next incomplete audit batch without restarting source inspection, T1 transcription, or already audited pages.

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

- Speech title in body: `பூந்தோட்டம்`;
- speech date: **1951-12-06**;
- venue: **சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி**;
- speaker: **தோழர் மு.கருணாநிதி**;
- event/occasion: **not separately stated**;
- audience: **not explicitly stated**.

Title-page wording:

`சென்னை கிண்டி இன்ஜினியரிங் கல்லூரியில் 06.12.1951இல் தோழர் மு.கருணாநிதி ஆற்றிய சொற்பொழிவு`

Do not replace these source-grounded fields with historical inference.

## Canonical page map

- PDF 1 - front cover
- PDF 2 - title page / speaker photo / explicit speech date and venue
- PDF 3 - bibliographic page (`நூல் குறிப்பு`)
- PDF 4 - publisher preface (`பதிப்புரை`)
- PDF 5 - prefatory poem `எரிமலை! (மு.கருணாநிதி)`
- PDF 6-17 - speech body, printed pages 5-16 (**12 pages total**)
- PDF 18 - back cover / promotional matter / barcode

The speech begins on PDF 6 under `பூந்தோட்டம்` and ends on PDF 17 with printed `வணக்கம்`.

## Scan-specific safeguards

- Blue circular library stamp on PDF 2 overlaps the title-page area: later marking, not edition text.
- Blue circular library stamp on PDF 17 lies below the speech ending: later marking, not edition text.
- Light bleed-through occurs on interior pages: do not transcribe reverse-side ghost text.
- The scan is authoritative; OCR/parsed text is only an aid.

## Workflow state

### Gate 1 - source inspection / bibliographic and page map

**COMPLETE.**

### Gate 2 / T1 - Tamil first-pass transcription

**FIRST-PASS COMPLETE - 12 / 12 speech pages drafted.**

Completed T1 batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-17 / printed 15-16

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**IN PROGRESS - 5 / 12 speech pages audited.**

Completed T2 Batch 1:

- PDF 6 / printed 5
- PDF 7 / printed 6
- PDF 8 / printed 7
- PDF 9 / printed 8
- PDF 10 / printed 9

This batch underwent a fresh line-by-line scan comparison. No substantive wording correction was required. Confirmed source forms and page-boundary findings are recorded in `audit.md`.

Remaining T2:

- PDF 11-15 / printed 10-14
- PDF 16-17 / printed 15-16

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED / BLOCKED until all 12 pages pass T2.**

### English gates

All **NOT STARTED / BLOCKED** until Tamil reaches `verified-complete` after T3.

## Confirmed T2 Batch 1 source points

The strict re-audit confirmed, among other items:

- p.5 → p.6 continues `பண்படுத்த` / `வேண்டும்.`;
- p.6 → p.7 continues `...மொண்டு மொண்டு தரும்` / `தென்றலாக, ...`;
- p.6 `பரவசத்திலீடுபடுகிறான்`;
- p.6 `அகம்புற மென்ற அன்றலர்ந்த`;
- p.7 `சீர் குலுங்கும்`;
- p.8 first highlighted `அந்தக்காலம்` is joined, while later source occurrences use `அந்தக் காலம்`;
- p.9 `அயோத்தியானுக்கு`;
- p.9 `பாராளப் பிறந்த ராமனின்`.

Do not normalize these in later work.

## Important watchpoints for the next audit batch

For PDF 11-15 / printed 10-14, deliberately re-check:

- `தண்ட காரணயத்திலே`;
- `வைத்தே இருக்குமிடத்தை`;
- `மிதிலாபுரிக்கு ஜனகனுக்கு`;
- `‘டிரங்கால்’`;
- `‘ரிஸ்ட் வாட்ச்’`;
- `“பஜகோவிந்த” மா`;
- p.10 → p.11 continuation `வேலைகளை விட்டு ஓய்வு` / `பெறுகிறவர் ...`;
- `பகுத்தறிவு புரியினருக்கும், பழமைத் தீவினருக்கும்`;
- `சொந்த மென்றான்`;
- the first-pass `பெய்ப்படி` reading on printed p.12;
- `வழக்கு மன்றத்திற்கு`;
- `பாமர நிலையவிட்டுக்`;
- `தன் தனிப் பெருமை யிழந்து`;
- `சொல்லே யில்லாத`;
- `காரைக்காலம்மை`.

Do not silently modernize or contextually repair them. Decide only from the scan.

## Exact next activity

Continue **Stage T2 only** with:

**PDF pages 11-15 / printed pages 10-14.**

Perform a fresh line-by-line comparison against `transcription-ta.md`. Apply only scan-confirmed corrections and log substantive findings in `audit.md`.

Do **not** begin English translation and do **not** mark Tamil `verified-complete` after this next batch. After T2 Batch 2, the final strict audit batch will be PDF 16-17 / printed 15-16, followed by the separate T3 consolidation/page-boundary/stale-reading check.

## Repository synchronization note

The root catalogue remains unchanged. Root catalogue synchronization belongs to archival closure after all textual and translation gates pass.
