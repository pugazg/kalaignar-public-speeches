# பள்ளி வாழ்க்கை — T3 handover

## Repository
- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/palli-vazhkkai/`

## Source
- Canonical source: `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`
- SHA-256: `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`
- PDF pages: 81
- Speech body: PDF 6-81 / printed 5-80 = 76 pages
- Source PDF committed: No

## Workflow state

### T1 — COMPLETE
All **76/76** body pages have first-pass readings.

### T2 — COMPLETE
All **76/76** body pages passed strict visual audit. Detailed evidence remains under `t2-batches/`, including Batches 1-16 and the two legacy-glyph recheck records.

### T3 — IN PROGRESS
The canonical `transcription-ta.md` has now been rebuilt and corrected through:

- **PDF 6-45 / printed 5-44 — T3 consolidated into the canonical file**
- PDF 46-50 / printed 45-49 — still in `t1-batches/batch-09-pdf-46-50.md`
- PDF 51-60 / printed 50-59 — still in `t1-batches/batch-10-pdf-51-60.md`
- PDF 61-70 / printed 60-69 — still in `t1-batches/batch-11-pdf-61-70.md`
- PDF 71-81 / printed 70-80 — still in `t1-batches/batch-12-pdf-71-81.md`

Tamil is **not yet frozen / verified-complete**. English remains blocked.

## T3 work completed in this activity

All known T2 corrections applicable to PDF 6-45 were incorporated into the canonical layer, including the user-triggered traditional-glyph corrections and the verified cross-page word joins.

The T3 stale-reading sweep also exposed two residual old-glyph misreadings that had survived the earlier audit summaries. Both were rechecked directly against their scan pages before correction:

- PDF 24 / printed 23: `மனிதனுக` → **`மனிதனாக`**
- PDF 39 / printed 38: `தேவைத்தானு?` → **`தேவைத்தானா?`**

These are underlying-character corrections for traditional 1952 glyph forms, not modernization.

Important verified joins already applied in the canonical PDF 6-45 segment include:
- PDF 31→32: `தமிழினத்` / `தைப்` → `தமிழினத்தைப்`
- PDF 32→33: `பசுமரத்` / `தாணிபோலப்` → `பசுமரத்தாணிபோலப்`
- PDF 40→41: `தேடு` / `கிறீர்;` → `தேடுகிறீர்;`
- PDF 41→42: `சுயமரியாதை` / `யற்ற` → `சுயமரியாதையற்ற`
- PDF 44→45: `ஊட்` / `டிடும்` → `ஊட்டிடும்`

Earlier verified joins already present in the canonical T1 segment were retained.

## Mandatory traditional-glyph rule

The 1952 printing uses traditional Tamil glyphs. Encode the underlying Tamil characters, not visually similar modern Unicode syllables. Do not resurrect superseded readings such as `கவலிப்பட`, `நன்றுக`, `தமிழனுக`, `மனிதனுக`, `தேவைத்தானு`, `தோழனுக`, `அவனுகத்தான்`, or `தேவனே` where the scan proves `கவலைப்பட`, `நன்றாக`, `தமிழனாக`, `மனிதனாக`, `தேவைத்தானா`, `தோழனாக`, `அவனாகத்தான்`, or `தேவனை`.

At the same time, do not regularize genuine source-supported oddities such as `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `உலகந்தான்`, `தன்னுலே`, or `உலகியலேக் காண` unless the scan itself proves otherwise.

## Exact next activity

Continue **T3 canonical consolidation with PDF 46-60 / printed 45-59**:

1. merge `t1-batches/batch-09-pdf-46-50.md` and the PDF 51-60 portion of `batch-10-pdf-51-60.md` into `transcription-ta.md`;
2. apply T2 Batches 9-11 corrections and traditional-glyph mappings exactly;
3. apply the verified PDF 50→51 `சிந்தித்` / `தான்!` → `சிந்தித்தான்!`, PDF 55→56 `மற்` / `றொன்று` → `மற்றொன்று`, and PDF 56→57 `வாழ்` / `வாகத்தானே` → `வாழ்வாகத்தானே` joins;
4. run a stale-reading sweep on the newly consolidated segment before proceeding to PDF 61-81.

Only after all PDF 6-81 pages are in one continuous canonical file, every T2 correction is applied, stale readings are absent, source-supported oddities are retained, and page continuity is checked may Tamil be marked `verified-complete` / frozen.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- T3 is consolidation and verification, not language editing.
- Do not modernize, normalize, reconstruct or improve source wording.
- Preserve source-supported spelling, punctuation, names, numbers, repetition and unusual grammar.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until T3 passes.