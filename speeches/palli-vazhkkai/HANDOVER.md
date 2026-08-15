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

### T2 — IN PROGRESS: 70/76
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
- Batch 13: PDF 66-70 / printed 65-69
- Batch 14: PDF 71-75 / printed 70-74

Detailed T2 records are under `t2-batches/`; the latest is `batch-14-pdf-71-75.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-14 were audited with this rule from the outset. Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, or `தானுகவே` where the scan establishes the corresponding underlying `-னா/-னாக/-ஆக` sequence.

## Important Batch 14 resolutions

Confirmed corrections:
- PDF 71: `தேர்வு அறிவிப்பதோடு` → **`‘தேர்வு’ அறிவிப்பதோடு`**
- PDF 71: `மினுபாவங்கொண்ட` → **`மனோபாவங்கொண்ட`**
- PDF 72: `வேதனை தரும்` → **`வேதனைதரும்`**
- PDF 72: `கேள்விகள், எழுப்புங்கள்?` → **`கேள்விகளை, எழுப்புங்கள்?`**
- PDF 73: `பரம்பரையின் ராகவே` → **`பரம்பரையினராகவே`**
- PDF 74: `வழிகத்தையும்` → **`வழிகாட்டியையும்`**
- PDF 74: `கெட்டிக்காரனுக` → **`கெட்டிக்காரனாக`**
- PDF 74: `பெறுபவனுக` → **`பெறுபவனாக`**
- PDF 74: `தானுகவே` → **`தானாகவே`**
- PDF 75: `வாழும் பொருந்தும்` → **`வாழ் பொருந்தும்`**
- PDF 75: `வறி, அவன்` → **`வாழ, அவன்`**

Page-boundary decisions:
- PDF 70→71 ordinary sentence continuation after `பாடத்தைப் போதித்தோம்,` was reconfirmed during full PDF 71 audit.
- PDF 71→72 `மனிதனது வருங்கால வாழ்க்கை வளர்ச்சிக்கு` / `ஆரம்பம், அணிவேர்...` is ordinary phrase continuation.
- PDF 72→73 has no split-word join; consecutive questions.
- PDF 73→74 `மைத்துனர், மாமி, எல்லோரும்` / `படித்தவர்கள் என்ற சூழ்நிலையில்...` is ordinary phrase continuation.
- PDF 74→75 has no split-word join; consecutive questions.
- PDF 75→76 `அத்துடன்` / `படிக்கிறான்.` is ordinary phrase continuation. PDF 76 was inspected only as a boundary witness and is **not** yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 corrections, including the user-triggered traditional-glyph recheck, are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 76-80 / printed pages 75-79**.

Specifically:
- audit PDF 76 fully even though its opening `படிக்கிறான்.` was inspected only as a boundary witness in Batch 14;
- apply the traditional-glyph rule from the outset;
- compare every line and punctuation mark against the scan;
- record only scan-proven changes;
- inspect PDF 81 only if needed as a page-boundary witness, and do not count it audited until the final batch.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves spelling while mapping obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.