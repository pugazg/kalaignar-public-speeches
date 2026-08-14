# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **T2 strict audit Batch 2**. It exists so continuation proceeds from the exact next incomplete audit batch without restarting source inspection, T1 transcription, or already audited pages.

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

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**IN PROGRESS - 10 / 12 speech pages audited.**

Completed T2 batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14

Both batches underwent fresh line-by-line scan comparison. No scan-confirmed wording correction was required in either batch. Confirmed source forms and page-boundary findings are recorded in `audit.md`.

Remaining T2:

- PDF 16-17 / printed 15-16

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED / BLOCKED until all 12 pages pass T2.**

### English gates

All **NOT STARTED / BLOCKED** until Tamil reaches `verified-complete` after T3.

## Confirmed T2 Batch 2 source points

The strict re-audit confirmed, among other items:

- p.10 `தண்ட காரணயத்திலே`;
- p.10 `வைத்தே இருக்குமிடத்தை`;
- p.10 `மிதிலாபுரிக்கு ஜனகனுக்கு` and `‘டிரங்கால்’`;
- p.10 `‘ரிஸ்ட் வாட்ச்’` and `“பஜகோவிந்த” மா`;
- p.10 → p.11 continuation `வேலைகளை விட்டு ஓய்வு` / `பெறுகிறவர் ...`;
- p.11 `பகுத்தறிவு புரியினருக்கும், பழமைத் தீவினருக்கும்`;
- p.11 `சொந்த மென்றான்`;
- p.12 `எப்படி பெய்ப்படி மாலை தொடுக்க முடியும்`;
- p.13 `வழக்கு மன்றத்திற்கு`;
- p.14 `பாமர நிலையவிட்டுக்`, `தன் தனிப் பெருமை யிழந்து`, `சொல்லே யில்லாத`, and `காரைக்காலம்மை`.

Do not normalize these in later work.

## Important watchpoints for the final audit batch

For PDF 16-17 / printed 15-16, deliberately re-check:

- `தாயைக் கட்டிலறைக் கழைத்து`;
- `வைகைக் கரையிலே`;
- `மோட்சலோக ‘பாஸ்போர்ட்’டன்`;
- separate `கை முஷ்டி` / joined `கைமுஷ்டி`;
- `பூர்ஷ்வாத் தன்மை`;
- first-pass `புரிவோடு`;
- p.15 → p.16 thought continuation;
- `அப்படி நடைபோடும் நல்லதம்பிகளைத்தான்`;
- printed `வணக்கம்` versus the later blue library stamp below it.

Decide only from the scan. Do not silently modernize or contextually repair source wording.

## Exact next activity

Continue **Stage T2 only** with the final strict audit batch:

**PDF pages 16-17 / printed pages 15-16.**

Perform a fresh line-by-line comparison against `transcription-ta.md`. Apply only scan-confirmed corrections and log substantive findings in `audit.md`.

After that batch, do **not** begin English translation yet. Proceed to the separate **T3 Tamil consolidation / page-boundary / stale-reading check** across the complete speech body. Only after T3 passes may the Tamil layer be frozen as `verified-complete` and English translation begin.

## Repository synchronization note

The root catalogue remains unchanged. Root catalogue synchronization belongs to archival closure after all textual and translation gates pass.
