# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **Tamil T3 consolidation/freeze completion**. Continue from the exact next incomplete gate; do not repeat source inspection, Tamil transcription, T2 audit, or T3 consolidation.

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
- Light bleed-through occurs on interior pages and is excluded from the speech body.
- The scan is authoritative; OCR/parsed text is only an aid.

## Workflow state

### Gate 1 - source inspection / bibliographic and page map

**COMPLETE.**

### Gate 2 / T1 - Tamil first-pass transcription

**COMPLETE - 12 / 12 speech pages drafted.**

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**COMPLETE - 12 / 12 speech pages audited.**

Completed batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-17 / printed 15-16

T2 corrections on printed p.15:

- `புரிவோடு` → **`பூரிப்போடு`**;
- `வளர்த்தான்` → **`வளரத்தான்`**.

### Gate 4 / T3 - Tamil consolidation and freeze

**COMPLETE - Tamil is `verified-complete`.**

T3 confirmed:

- both T2 corrections are present in the speech text;
- superseded readings no longer survive in the speech text;
- all 11 page transitions contain no accidental omission, duplication, broken word, or lost punctuation;
- PDF-page headings 6 through 17 occur once in correct order, so no speech page is missing or duplicated;
- T2-confirmed unusual source forms remain preserved rather than normalized;
- running headers, reverse-side bleed-through, and the PDF 17 library stamp remain excluded;
- the complete Tamil body passed the end-to-end stale-reading check.

Important page-boundary continuations preserved correctly:

- printed p.5 → p.6: `பண்படுத்த` / `வேண்டும்.`;
- printed p.6 → p.7: `...மொண்டு மொண்டு தரும்` / `தென்றலாக, ...`;
- printed p.10 → p.11: `வேலைகளை விட்டு ஓய்வு` / `பெறுகிறவர் ...`;
- printed p.15 → p.16: `வேண்டாத ஒரு வெறுப்பு வளரத்தான் நேரிடும்.` / `அந்த வெறுப்பு...`.

The verified Tamil layer is now frozen. Any later Tamil change requires documented source evidence and dependent English re-verification.

### English gates

- E1 English first-pass translation: **NOT STARTED - EXACT NEXT GATE**
- E2 Tamil→English fidelity review: **NOT STARTED / BLOCKED until E1 complete**
- E3 final end-to-end Tamil→English verification: **NOT STARTED / BLOCKED**

## Exact next activity

Begin **E1 - English first-pass translation** from the frozen `transcription-ta.md` only.

Recommended first translation batch: **PDF pages 6-10 / printed pages 5-9**.

Requirements:

1. retain explicit PDF/printed-page headings;
2. translate only from the verified Tamil layer, not OCR or the source PDF independently;
3. preserve argument structure, rhetorical force, repetition, metaphors, polemical language and historical references;
4. do not silently repair unusual Tamil such as `அகம்புற மென்ற அன்றலர்ந்த`, `அயோத்தியானுக்கு`, or other source-supported forms;
5. where a difficult source form creates genuine translation ambiguity, keep the translation transparent and record a concise note rather than inventing certainty;
6. do not begin E2 review until the complete English first pass exists.

## Repository synchronization note

The root catalogue remains unchanged. Root catalogue synchronization belongs to final archival closure after E1, E2, E3, metadata synchronization, and final handover are complete.