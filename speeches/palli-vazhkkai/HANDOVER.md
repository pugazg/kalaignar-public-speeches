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

### T2 — IN PROGRESS: 50/76
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
- Batch 10: PDF 51-55 / printed 50-54

Detailed T2 records are under `t2-batches/`; the latest is `batch-10-pdf-51-55.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-10 were audited with this corrected rule from the outset.

Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, or later `-னுக` glyph misreadings.

## Important Batch 10 resolutions

Confirmed corrections:
- PDF 51 / printed 50: `மனிதனுக` → **`மனிதனாக`**
- PDF 52 / printed 51: `ஆளும்` → **`ஆனாலும்`**
- PDF 53 / printed 52: `இரண்யாட்சன்` → **`இரண்ணியாட்சகன்`**
- PDF 53 / printed 52: `இரண்யாட்சனைத்` → **`இரண்ணியாட்சகனைத்`**
- PDF 54 / printed 53: `பார்ந்த பூமியை` → **`பரந்தபூமியை`**
- PDF 54 / printed 53: `மூம்மூர்த்திகளில்` → **`மும்மூர்த்திகளில்`**
- PDF 55 / printed 54: `மோதவிடப்படுகிறது,` → **`மோதவிடப்படுகிறது;`**
- PDF 55 / printed 54: the T1 eclipse explanation was materially corrupted and omitted a full clause. Use the scan-supported sentence recorded in `batch-10-pdf-51-55.md`.
- PDF 55 / printed 54: `வேறு வேறு காரணங்கள்` → **`வேறு வேறான காரணங்கள்`**

Page-boundary decisions:
- PDF 50→51 `சிந்தித்` / `தான்!` → `சிந்தித்தான்!` reconfirmed during full PDF 51 audit.
- PDF 55→56 `மற்` / `றொன்று` → **`மற்றொன்று`**. PDF 56 was inspected only as a boundary witness and is **not** yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 corrections, including the user-triggered traditional-glyph recheck, are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 56-60 / printed pages 55-59**.

Specifically:
- audit PDF 56 fully even though its opening `றொன்று` was used only as a boundary witness in Batch 10;
- apply the traditional-glyph rule from the outset;
- compare every line and punctuation mark against the scan;
- record only scan-proven changes;
- inspect PDF 61 only if needed as a page-boundary witness, and do not count it audited until its own batch.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves spelling while mapping obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.