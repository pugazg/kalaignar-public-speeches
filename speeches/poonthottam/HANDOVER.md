# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **T1 first-pass completion**. It exists so continuation proceeds from the exact next incomplete gate without restarting source inspection or retranscribing drafted pages.

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

**FIRST-PASS COMPLETE - 12 / 12 speech pages drafted.**

Completed T1 batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-17 / printed 15-16

All speech-body pages are present in `transcription-ta.md` as **first-pass text only**. None is yet verified.

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**NOT STARTED - THIS IS THE EXACT NEXT GATE.**

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED / BLOCKED until T2 completes all 12 pages.**

### English gates

All **NOT STARTED / BLOCKED** until Tamil reaches `verified-complete`.

## Preliminary T1 source watchpoints

These are not final audit resolutions; re-check them in T2.

From Batch 1:

- printed p.5 → p.6 continues `பண்படுத்த` / `வேண்டும்.`;
- printed p.6 → p.7 continues `...மொண்டு மொண்டு தரும்` / `தென்றலாக, ...`;
- printed p.6 `பரவசத்திலீடுபடுகிறான்`;
- printed p.6 `அகம்புற மென்ற அன்றலர்ந்த`;
- printed p.7 `சீர் குலுங்கும்`;
- printed p.8 joined `அந்தக்காலம்`;
- printed p.9 `அயோத்தியானுக்கு`.

From Batch 2:

- printed p.10 `தண்ட காரணயத்திலே`, `வைத்தே இருக்குமிடத்தை`, `மிதிலாபுரிக்கு ஜனகனுக்கு`, `‘டிரங்கால்’`;
- printed p.10 `‘ரிஸ்ட் வாட்ச்’`, `“பஜகோவிந்த” மா`;
- printed p.10 → p.11 continues `வேலைகளை விட்டு ஓய்வு` / `பெறுகிறவர் ...`;
- printed p.11 `பகுத்தறிவு புரியினருக்கும், பழமைத் தீவினருக்கும்`, `சொந்த மென்றான்`;
- printed p.12 first-pass `பெய்ப்படி` requires character-level T2 reinspection;
- printed p.13 `வழக்கு மன்றத்திற்கு`;
- printed p.14 `பாமர நிலையவிட்டுக்`, `தன் தனிப் பெருமை யிழந்து`, `சொல்லே யில்லாத`, `காரைக்காலம்மை`.

From Batch 3:

- printed p.15 `தாயைக் கட்டிலறைக் கழைத்து`, `வைகைக் கரையிலே`, `மோட்சலோக ‘பாஸ்போர்ட்’டன்`, `பூர்ஷ்வாத் தன்மை`;
- printed p.15 uses both `கை முஷ்டி` and `கைமுஷ்டி`;
- printed p.15 first-pass `புரிவோடு` needs deliberate T2 character-level reinspection;
- printed p.15 → p.16 is a sentence/thought continuation, not a split word;
- printed p.16 `அப்படி நடைபோடும் நல்லதம்பிகளைத்தான்`;
- printed p.16 printed `வணக்கம்` is speech text; the large blue library stamp below it is not.

Do not normalize any of these merely because a smoother or modern reading seems likely.

## Exact next activity

Begin **Stage T2 - strict independent Tamil fidelity audit** with the first audit batch:

**PDF pages 6-10 / printed pages 5-9.**

This must be a fresh line-by-line scan comparison against the existing first-pass transcription. Check punctuation, spacing where meaningful, names, numerals, repeated wording, suspicious OCR-like forms, and page boundaries. Record substantive findings in `audit.md` and apply only scan-confirmed corrections to `transcription-ta.md`.

Do **not** begin English translation and do **not** mark Tamil `verified-complete` after one T2 batch. All 12 speech pages must pass T2, followed by the separate T3 consolidation/page-boundary/stale-reading check.

## Repository synchronization note

The root catalogue remains unchanged. Root catalogue synchronization belongs to archival closure after all textual gates pass.
