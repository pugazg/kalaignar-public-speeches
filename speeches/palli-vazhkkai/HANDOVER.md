# பள்ளி வாழ்க்கை — T1 handover

This document records the exact state after completion of the second Tamil first-pass transcription batch. Continue from the next incomplete page rather than repeating startup work or redoing completed T1 batches as an audit.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/palli-vazhkkai/`

## Source

- Canonical source filename: `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`
- SHA-256: `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`
- File size: `101,096,930` bytes
- Actual PDF page count: `81`
- Main body: PDF 6-81 / printed 5-80 (**76 pages**)
- Source PDF committed to repository: **No - repository policy is to preserve source identity through provenance metadata, not commit the source binary**

## Source form

The booklet is `பள்ளி வாழ்க்கை`, creator line `கலைஞர் : மு. கருணாநிதி`, first edition March 1952, அறிவு மன்றம், சென்னை. PDF page 5 states that speeches at `திருவாரூர் நகராண்மைக் கழக உயர்நிலைப்பள்ளி` and `வேறு சில இடங்களிலும்` were collected by `தோழர் மு. நமச்சிவாயம்`.

Treat it as a printed compilation of multiple speeches. Do not invent one speech date, venue, event, occasion, or audience.

## Completed gates / work

### Source inspection

- Status: **complete**
- Page map and bibliographic/source-provenance record established.

### Tamil T1 first pass

- Status: **in progress**
- Completed: **10 / 76 body pages**
- Completed range: **PDF 6-15 / printed 5-14**
- Batch 1: PDF 6-10 / printed 5-9 — complete first pass
- Batch 2: PDF 11-15 / printed 10-14 — complete first pass
- `transcription-ta.md` contains all 10 page-bounded first-pass transcriptions.
- Page-boundary joins carried forward for T2 verification: PDF 9→10 `உயி` / `ரினங்களைவிட` → `உயிரினங்களைவிட`; PDF 13→14 `இவர்` / `கட்கு` → `இவர்கட்கு`.
- T1 preserved several unusual printed forms rather than normalizing them; see `audit.md` for the provisional carry-forward list.

### Tamil T2 strict visual audit

- Status: **not started**
- Pages audited: **0 / 76**
- Do not treat either T1 batch as audited merely because transcription was made from page images.

### Tamil T3 consolidation / freeze

- Status: **not started**
- Tamil is **not frozen** and is not `verified-complete`.

### English

- E1 translation: **not started**
- E2 fidelity review: **not started**
- E3 final end-to-end verification: **not started**
- English remains blocked until Tamil T2/T3 pass.

## Exact next incomplete activity

Continue **Stage T1 first-pass Tamil transcription** with the next manageable batch beginning at:

- **PDF page 16 / printed page 15**

Proceed forward from there, retaining explicit PDF/printed-page headings and joining only genuine printer word-wraps. Preserve historical spelling, punctuation, wording, names, numbers, repetition, unusual grammar, and source-supported typographical forms. Do not silently modernize or repair the text.

## Continuation safeguards

- The supplied scan is authoritative; OCR/parsed text is only an aid.
- T1 is transcription, not the later independent T2 audit.
- Do not start T2 until all 76 body pages have a first-pass transcription.
- Do not begin English translation until T2 and T3 have passed and Tamil is frozen as `verified-complete`.
- Distinguish print from donor/library markings, handwriting, damage, and bleed-through.
- Do not infer event metadata from publication date or outside history.
- Do not upload or commit the source PDF.
- Update metadata, README, audit state, and this handover after each meaningful T1 batch.
