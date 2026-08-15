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

### T2 — IN PROGRESS: 65/76
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

Detailed T2 records are under `t2-batches/`; the latest is `batch-13-pdf-66-70.md`.

## Mandatory traditional-glyph rule

The 1952 edition uses traditional Tamil glyph shapes. Encode the underlying Tamil characters, not a visually similar modern Unicode syllable. Earlier glyph misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8-13 were audited with this rule from the outset. Do not reintroduce withdrawn forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `ஒன்றுக`, or `தோழனுகவே` where the scan establishes the corresponding `-னா/-னாக/-ஆக` sequence.

## Important Batch 13 resolutions

Confirmed corrections:
- PDF 66: `மாட்டானு?` → **`மாட்டானா?`**
- PDF 66: `ஒன்றன்பின் ஒன்றுக` → **`ஒன்றன்பின் ஒன்றாக`**
- PDF 66: `அவல் மூச்சாக` → **`அனல் மூச்சாக`**
- PDF 66: `முயல்வதுபோல` → **`முயல்வது போல`**
- PDF 66: `நன்றுக நினைவில்` → **`நன்றாக நினைவில்`**
- PDF 67: `நன்றுக நினைவிருக்கட்டும்` → **`நன்றாக நினைவிருக்கட்டும்`**
- PDF 67: `வளர்ப்படுத்திக்` → **`வளப்படுத்திக்`**
- PDF 68: `புத்தக வித்தகர்` → **`புத்தகவித்தகர்`**
- PDF 68: `உலகம்தான்` → **`உலகந்தான்`**
- PDF 69: `தந்திரங்களைக் தவறாது` → **`தந்திரங்களைத் தவறாது`**
- PDF 69: `கூடாது; நேரடித்` → **`கூடாது, நேரடித்`**
- PDF 69: `நன்றுக நினைவு` → **`நன்றாக நினைவு`**
- PDF 70: `தோழனுகவே` → **`தோழனாகவே`**

Source-supported form to preserve:
- PDF 68: **`உலகந்தான்`** — do not silently regularize it to `உலகம்தான்`.

Page-boundary decisions:
- PDF 67→68 `... தோன்றிடப்` / `போகிறார்கள்!` is ordinary phrase continuation.
- PDF 69→70 `அறிவைப் பெருக்கிடும்` / `கல்வியறிவைப் புறக்கணித்துப்...` is ordinary phrase continuation.
- PDF 70→71 `... பாடத்தைப் போதித்தோம்,` / `படிக்கிற பிள்ளைகள்...` is ordinary sentence continuation. PDF 71 was inspected only as a boundary witness and is **not** yet counted audited.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.
- All T2 corrections, including the user-triggered traditional-glyph recheck, are mandatory T3 inputs.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 71-75 / printed pages 70-74**.

Specifically:
- audit PDF 71 fully even though its opening was inspected only as a boundary witness in Batch 13;
- apply the traditional-glyph rule from the outset;
- compare every line and punctuation mark against the scan;
- record only scan-proven changes;
- inspect PDF 76 only if needed as a page-boundary witness, and do not count it audited until its own batch.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- Source-faithful transcription preserves spelling while mapping obsolete glyph shapes to the correct underlying Tamil characters.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.