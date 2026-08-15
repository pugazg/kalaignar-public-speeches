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

### T2 — IN PROGRESS: 60/76
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
- Batch 12: PDF 61-65 / printed 60-64

Detailed T2 records are under `t2-batches/`; the latest is `batch-12-pdf-61-65.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-12 were audited with this rule from the outset. Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, or glyph-based `வீரனைத்` where the source underlying sequence is `வீரனாகத்`.

## Important Batch 12 resolutions

Confirmed corrections:
- PDF 62: `கல்வெறிபட்டுக்` → **`கல்லெறிபட்டுக்`**
- PDF 62: `மீனவி மக்களைத் திருந்து` → **`மீனவ மக்களைத் துறந்து`**
- PDF 63: first `மனிதனுக` → **`மனிதனாக`**
- PDF 63: second `மனிதனுக` → **`மனிதனாக`**
- PDF 63: `மிருகத் தன்மையின்றும்` → **`மிருகத் தன்மையினின்றும்`**
- PDF 63: `படைத்தவனுக` → **`படைத்தவனாக`**
- PDF 64: `மூன்கெட்டு` → **`மூளை கெட்டு`**
- PDF 64: `அறிவும் தன்மை` → **`அறியும் தன்மை`**
- PDF 65: `தெரிவித்து கொள்வதும்` → **`தெரிவித்துக்கொள்வதும்`**
- PDF 65: `தமிழ் வீரனைத் திகழ்வான்` → **`தமிழ் வீரனாகத் திகழ்வான்`**

Page-boundary decisions:
- PDF 60→61 `வளர்ச்சி` / `வழியை...` is ordinary phrase continuation and was reconfirmed during full PDF 61 audit.
- PDF 61→62 `இது அந்த` / `நாள், ...` is ordinary phrase continuation.
- PDF 62→63 `புதுப் புதுக் கருவிகள் உண்டான` / `சூழ்நிலைகள் என்ன?` is ordinary phrase continuation.
- PDF 64→65 `ஆங்கில நாட்டு மாணவன் தன்னை ஆங்கிலேயன்` / `என்று கூறுவதும்...` is ordinary sentence continuation.
- PDF 65 ends a complete sentence, so no PDF 65→66 join is required.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 corrections, including the user-triggered traditional-glyph recheck, are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 66-70 / printed pages 65-69**.

Specifically:
- audit PDF 66 fully from the beginning even though its image was visible during Batch 12;
- apply the traditional-glyph rule from the outset;
- compare every line and punctuation mark against the scan;
- record only scan-proven changes;
- inspect PDF 71 only if needed as a page-boundary witness, and do not count it audited until its own batch.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves spelling while mapping obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.