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

### T2 — IN PROGRESS: 55/76
Completed strict visual audit through:
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

Detailed T2 records are under `t2-batches/`; the latest is `batch-11-pdf-56-60.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-11 were audited with this rule from the outset. Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, or `மனிதனுக`.

## Important Batch 11 resolutions

Confirmed corrections:
- PDF 56: `ஒன்றுகவே` → **`ஒன்றாகவே`**
- PDF 56: `உபயோகப்படுத்திக்கொண்டும்` → **`உபயோகப் படுத்திக்கொண்டும்`**
- PDF 56: `அங்கக் கால` → **`அந்தக் கால`**
- PDF 57: `சிந்தனை முதிர்ச்சி படைந்து` → **`சிந்தனை முதிர்ச்சி யடைந்து`**
- PDF 57: `நாகரிக வாழ்வு வாழ்வதைப்` → **`நாகரிக வாழ்வு, வாழ்வதைப்`**
- PDF 60: `தமிழனுக` → **`தமிழனாக`**
- PDF 60: `தமிழ் அறிந்த தமிழனமாக` → **`தமிழறிந்த தமிழனமாக`**

Source-supported unusual readings to preserve:
- PDF 60: **`தமிழனமாக`** (the extra `ம` is visibly present)
- PDF 60: **`மதனின் அறிவு வளர்ச்சி பெற்று`**

Page-boundary decisions:
- PDF 55→56 `மற்` / `றொன்று` → `மற்றொன்று` reconfirmed during full PDF 56 audit.
- PDF 56→57 `வாழ்` / `வாகத்தானே` → **`வாழ்வாகத்தானே`**.
- PDF 58→59 is ordinary sentence continuation after `பாரத இதிகாசங்கள்`.
- PDF 59→60 is ordinary phrase continuation after `இராஜ இராஜேந்திரனின்`.
- PDF 60→61 `வளர்ச்சி` / `வழியை...` is ordinary phrase continuation. PDF 61 was inspected only as a boundary witness and is **not** yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 corrections, including the user-triggered traditional-glyph recheck, are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 61-65 / printed pages 60-64**.

Specifically:
- audit PDF 61 fully even though its opening was used only as a boundary witness in Batch 11;
- apply the traditional-glyph rule from the outset;
- compare every line and punctuation mark against the scan;
- record only scan-proven changes;
- inspect PDF 66 only if needed as a page-boundary witness, and do not count it audited until its own batch.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves spelling while mapping obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
