# பள்ளி வாழ்க்கை — T2 handover

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
All **76/76 speech-body pages** have first-pass readings.

### T2 — IN PROGRESS: 75/76
Strict visual audit is complete through **PDF 80 / printed 79**.

Completed batches:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34
- Batch 7: PDF 36-40 / printed 35-39
- Batch 8: PDF 41-45 / printed 40-44
- Batch 9: PDF 46-50 / printed 45-49
- Batch 10: PDF 51-55 / printed 50-54
- Batch 11: PDF 56-60 / printed 55-59
- Batch 12: PDF 61-65 / printed 60-64
- Batch 13: PDF 66-70 / printed 65-69
- Batch 14: PDF 71-75 / printed 70-74
- Batch 15: PDF 76-80 / printed 75-79

Detailed records are under `t2-batches/`; latest: `batch-15-pdf-76-80.md`.

Only **PDF 81 / printed 80** remains unaudited.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not visually similar modern Unicode syllables. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-15 were audited with this rule from the outset.

Do not reintroduce superseded readings such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, or the later `-னுக/-னு` forms corrected in the T2 batch records.

## Important Batch 15 resolutions

Confirmed corrections:
- PDF 76: `அவனுகத்தான்` → **`அவனாகத்தான்`**
- PDF 77: `ஒவ்வொரு வனுக்கும்` → **`ஒவ்வொருவனுக்கும்`**
- PDF 77: `எய்ப்பது` → **`ஏய்ப்பது`**
- PDF 78: `நாட்டெங்கும்` → **`நாடெங்கும்`**
- PDF 80: `தேவனே நம்பு!` → **`தேவனை நம்பு!`**

The last correction is another traditional-glyph issue: the printed old `னை` form must be encoded as `னை`, not misread as modern `னே`.

Page-boundary decisions:
- PDF 75→76: `அத்துடன்` / `படிக்கிறான்.` — ordinary phrase continuation, reconfirmed.
- PDF 76→77: `வாழ்வின் எல்லாத் துறை` / `களிலும்` → **`வாழ்வின் எல்லாத் துறைகளிலும்`**.
- PDF 77→78: `தகுதியை` / `யும்` → **`தகுதியையும்`**.
- PDF 78→79: `ஏற்பட்` / `டது` → **`ஏற்பட்டது`**.
- PDF 79→80: `விளங்குகின்ற` / `னர்.` → **`விளங்குகின்றனர்.`**.
- PDF 80→81: ordinary sentence continuation after `என்றெல்லாம் நாட்டில் கூக்குரல்,`. PDF 81 was inspected only as a boundary witness and is not yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 correction records and page-boundary decisions are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform the final strict T2 visual audit of **PDF page 81 / printed page 80**.

Specifically:
- audit every line and punctuation mark on the final body page against the scan;
- reconfirm the PDF 80→81 sentence continuation;
- apply the traditional-glyph rule from the outset, especially `னை/லை/ளை/னா` shapes;
- record every scan-proven correction in a final T2 batch record;
- only then mark T2 **complete — 76/76**.

After T2 completion, the next gate is T3 canonical Tamil consolidation/freeze: merge the segmented T1 material, apply all T2 corrections and boundary joins, run an end-to-end stale-reading check, and freeze only when the Tamil layer is verified-complete.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves wording while decoding obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until T2 and T3 pass.