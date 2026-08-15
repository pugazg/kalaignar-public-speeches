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

### T3 — ALL PAGES MERGED; FINAL GATE PENDING
`transcription-ta.md` now contains the T2-corrected canonical Tamil for **PDF 6-81 / printed 5-80**.

Tamil is **not yet frozen / verified-complete**. The final whole-body T3 verification gate has not yet been run. English remains blocked.

## Final segment just consolidated — PDF 76-81

Applied scan-proven T2 corrections:

- PDF 76: `அவனுகத்தான்` → `அவனாகத்தான்`
- PDF 77: `ஒவ்வொரு வனுக்கும்` → `ஒவ்வொருவனுக்கும்`; `எய்ப்பது` → `ஏய்ப்பது`
- PDF 78: `நாட்டெங்கும்` → `நாடெங்கும்`
- PDF 80: `தேவனே நம்பு!` → `தேவனை நம்பு!`
- PDF 81: `தமிழமெல்லாம்` → `தமிழரெல்லாம்`; `தமிழனத்தை` → `தமிழினத்தை`

Verified split-word joins incorporated:

- PDF 76→77: `துறை` / `களிலும்` → `துறைகளிலும்`
- PDF 77→78: `தகுதியை` / `யும்` → `தகுதியையும்`
- PDF 78→79: `ஏற்பட்` / `டது` → `ஏற்பட்டது`
- PDF 79→80: `விளங்குகின்ற` / `னர்` → `விளங்குகின்றனர்`

PDF 75→76 and PDF 80→81 remain ordinary phrase/sentence continuations, exactly as established by T2.

The canonical final page preserves source-supported wording including `உலகியலேக் காண` and the verified closing:

`... தீரத் தமிழராக, தன்மானச் சிங்கங்களாக விளங்க அடிப்படை காணுங்கள், பள்ளி வாழ்க்கையில்! வணக்கம் !!`

## Mandatory traditional-glyph rule

The 1952 printing uses traditional Tamil glyphs. Encode the underlying Tamil characters, not visually similar modern Unicode syllables. Do not resurrect superseded readings such as `கவலிப்பட`, `நன்றுக`, `தமிழனுக`, `மனிதனுக`, `தேவைத்தானு`, `தோழனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, or `தேவனே` where the scan proves the corrected underlying reading.

At the same time, do not regularize genuine scan-supported oddities such as `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `உலகந்தான்`, `தன்னுலே`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, or `உலகியலேக் காண` unless the scan itself proves otherwise.

## Exact next activity — whole-body T3 gate

Run an end-to-end verification of the canonical `transcription-ta.md` across **PDF 6-81 / printed 5-80**:

1. verify exactly 76 unique page headings, sequential PDF 6-81 and printed 5-80;
2. search the complete body for every superseded T1/T2/traditional-glyph stale reading;
3. verify every recorded split-word/page-boundary reconstruction from the T2 records;
4. verify the canonical beginning and final closing;
5. verify representative source-supported unusual readings remain unchanged;
6. check for missing or duplicated page text around all merge boundaries;
7. only if all checks pass, mark `transcription-ta.md` as `verified-complete`, set `metadata.json` `tamil_frozen: true`, synchronize README/audit/HANDOVER, and then unlock English translation.

T1 staging and T2 evidence should remain retained until this gate passes.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- T3 is consolidation and verification, not language editing.
- Do not modernize, normalize, reconstruct or improve source wording.
- Preserve source-supported spelling, punctuation, names, numbers, repetition and unusual grammar.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until the T3 whole-body gate passes.