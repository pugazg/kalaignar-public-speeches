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

### T2 — IN PROGRESS: 45/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34
- Batch 7: PDF 36-40 / printed 35-39
- Batch 8: PDF 41-45 / printed 40-44
- Batch 9: PDF 46-50 / printed 45-49

Detailed records are under `t2-batches/`, including `batch-09-pdf-46-50.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8 and 9 were audited with this corrected rule from the outset.

Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, or other legacy-glyph misreadings. Follow `audit.md` and the corrective files during T3.

## Important Batch 9 resolutions

Confirmed corrections:
- PDF 48 / printed 47: `மழையவர்` → **`மறையவர்`**
- PDF 49 / printed 48: `தோழனுகத்` → **`தோழனாகத்`**
- PDF 49 / printed 48: `அதனின் அச்சிடும்` → **`அதன் அச்சிடும்`**
- PDF 50 / printed 49: `உறுதுணைவனுக` → **`உறுதுணைவனாக`**
- PDF 50 / printed 49: `உயிரே செல்லும்` → **`உயரே செல்லும்`**
- PDF 50 / printed 49: `எவலனுக` → **`ஏவலனாக`**

Source-supported reading retained:
- PDF 48: **`மனிதனி அறிவு கண்டு`** — do not silently change to `மனிதனின்`.

Page-boundary decisions:
- PDF 45→46 `வருணபகவான் என்றும்` / `இடிக்குத் தலைவன் இந்திரன் என்றும்` is ordinary sentence continuation.
- PDF 47→48 `... இரண்டு வழிகளில், எது` / `வேண்டும் இன்று!` is ordinary phrase continuation.
- PDF 49→50 `காலம் அறிவிக்கும்` / `கடிகார வகைகள்` is ordinary phrase continuation.
- PDF 50→51 `சிந்தித்` / `தான்!` → **`சிந்தித்தான்!`**. PDF 51 was inspected only as a boundary witness and is **not** yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 51-55 / printed pages 50-54**.

Specifically:
- audit PDF 51 fully even though its opening `தான்!` was used only as a boundary witness in Batch 9;
- apply the traditional-glyph rule from the outset;
- record only scan-proven changes;
- inspect PDF 56 only if needed as a boundary witness for PDF 55 and do not count it audited until its own batch.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- Source-faithful transcription preserves spelling, not obsolete glyph shape as a wrong Unicode letter.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
