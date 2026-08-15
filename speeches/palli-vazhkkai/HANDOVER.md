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

### T2 — IN PROGRESS: 40/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34
- Batch 7: PDF 36-40 / printed 35-39
- Batch 8: PDF 41-45 / printed 40-44

Detailed records are under `t2-batches/`, including `batch-08-pdf-41-45.md`.

## Mandatory traditional-glyph rule

User review correctly identified an earlier error: the 1952 edition uses traditional Tamil glyph shapes, and some had been misread as different modern Unicode syllables. The corrective sweep through PDF 40 is preserved in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batch 8 was audited with this corrected rule from the outset.

When old glyphs represent `னா`, `றா`, `ணா`, `னை`, `ணை`, `லை`, `ளை` and related combinations, encode the underlying Tamil characters. Do not transcribe a visually similar modern `னு`, `று`, `ணு`, `னே`, `லி`, etc.

## Important Batch 8 resolutions

Confirmed corrections:
- PDF 41→42: T1 `சுயமரியாதை` / `பற்ற செயல்` → source `சுயமரியாதை` / `யற்ற செயல்` → **`சுயமரியாதையற்ற செயல்`**
- PDF 42: `தினதயாளன்` → **`தீனதயாளன்`**
- PDF 42: `ஆல கால` → **`ஆலகால`**
- PDF 42: `நீலகண்டனூர்` → **`நீலகண்டனார்`**
- PDF 42: `திடமென்று` → **`திடீரென்று`**
- PDF 43: `சிவத்தொண்டு` → **`சிவத் தொண்டு`** in the audited phrase
- PDF 43: `மினையாளைக்` → **`மனையாளைக்`**
- PDF 43: `முறைதானு?` → **`முறைதானா?`**
- PDF 44: `தேவைத்தான்` → **`தேவைதான்`**
- PDF 44: `கோட்டாடுகளைப்போற்றிப்` → **`கோட்பாடுகளைப்போற்றிப்`**
- PDF 44: `சிக்கச் சீழிய` → **`சிக்கச் செய்ய`**
- PDF 45: `தேவைத்தானு` → **`தேவைதானா`**

Page-boundary decisions:
- PDF 40→41 `தேடு` / `கிறீர்;` → `தேடுகிறீர்;` reconfirmed during full PDF 41 audit.
- PDF 41→42 `சுயமரியாதை` / `யற்ற செயல்` → `சுயமரியாதையற்ற செயல்`.
- PDF 42→43 `உமக்குப்` / `பெருமை தந்திடத்தான்` is ordinary phrase continuation.
- PDF 44→45 `ஊட்` / `டிடும்` → `ஊட்டிடும்`.
- PDF 45→46 `வருணபகவான் என்றும்` / `இடிக்குத் தலைவன் இந்திரன் என்றும்` is ordinary sentence continuation. PDF 46 was inspected only as a boundary witness and is **not** counted audited.

## Superseded legacy-glyph readings — DO NOT USE

Earlier incorrect forms such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?` and similar legacy-glyph misreadings remain withdrawn. Follow `audit.md` and the two legacy-glyph recheck files during T3.

Later T1 forms such as `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `கெட்டிக்காரனுக`, etc. must be checked first for traditional `னா` before being accepted as source oddities.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 46-50 / printed pages 45-49**.

Specifically:
- audit PDF 46 fully even though its opening was used only as a boundary witness in Batch 8;
- apply the traditional-glyph rule from the outset;
- scrutinize T1 forms such as `தோழனுக`, `உறுதுணைவனுக`, and `எவலனுக` before treating them as source spelling;
- resolve PDF 50→51 `சிந்தித்` / `தான்!` from both page images;
- inspect PDF 51 only as the boundary witness for that split and do not count PDF 51 audited until its own batch;
- record only scan-proven changes.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- Source-faithful transcription preserves spelling, not obsolete glyph shape as a wrong Unicode letter.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
