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

### T2 — IN PROGRESS: 35/76
Completed strict visual audit through:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34
- Batch 7: PDF 36-40 / printed 35-39

## CRITICAL correction before continuing

User review correctly identified that PDF 29 / printed 28 reads **`கவலைப்பட`**, not `கவலிப்பட`.

This exposed a systematic issue: the 1952 scan uses **traditional pre-1978 Tamil glyph shapes**. Several earlier T2 decisions had treated those old glyph shapes as different modern Unicode syllables. That is wrong. The glyph changed; the underlying Tamil letter did not.

Corrective records:
- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Affected Batch 1/2/4/5/6/7 files have been rewritten so their instructions no longer contradict this rule.

### Traditional glyphs: mandatory rule

When the scan uses traditional forms of `னா`, `றா`, `ணா`, `னை`, `ணை`, `லை`, `ளை` (and related old `ஒ/ஓ` combinations), encode the **underlying Tamil characters**. Do not convert an old glyph to a visually similar modern `னு`, `று`, `ணு`, `னே`, `லி`, etc.

This is not spelling modernization; it is correct Unicode interpretation of the printed glyph.

### Superseded readings — DO NOT USE

- `கற்றோனுக` → use `கற்றோனாக`
- `கல்லூரனுக` → `கல்லூரனாக`
- `கதாசிரியனுக` → `கதாசிரியனாக`
- `கட்டுரையாசிரியனுக` → `கட்டுரையாசிரியனாக`
- `உத்தமனுக` → `உத்தமனாக`
- `மண்ணுவது` → `மண்ணாவது`
- `நன்றுக` → `நன்றாக`
- `வாசனே` → `வாசனை`
- `நிணப்பார்` → `நினைப்பார்`
- `நிணக்க` → `நினைக்க`
- `நிணத்திடும்` → `நினைத்திடும்`
- `திடசித்தமுடையவனுக` → `திடசித்தமுடையவனாக`
- `தமிழனுக` → `தமிழனாக`
- `கவலிப்பட` → `கவலைப்பட`
- `தேவைத்தானு` → `தேவைத்தானா`
- `நானு?` → `நானா?`

Later T1 forms such as `மனிதனுக`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `கெட்டிக்காரனுக`, etc. are **not** to be accepted as source oddities automatically. Check first whether the printed glyph is traditional `னா`.

### Valid corrections already established

The glyph correction does not cancel unrelated scan-proven corrections, including:
- `ஆராய்ந்து தெளிந்து`
- `தோலினாலும்`
- `மனித வர்க்கத்தின்` / `மனித வர்க்கத்தை`
- `ஒருப்படியாக`
- `வயலில் உழுது`
- `வரைவிட`
- `இடம் உடைத்து`
- `இகத்தை வெறுத்து`
- `தன்னைப்பற்றிக்`
- `வில்லைபூட்டி`
- `குருதிவடிந்தோடும்`
- `தாங்கள் தான்`
- `ஏகலவனை மறுபடி`
- `பக்திக்கு`
- `சீறிச் சினந்து`

All remain subject to the final T3 stale-reading check.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Now—and only with the corrected traditional-glyph rule—perform strict T2 audit of **PDF pages 41-45 / printed pages 40-44**.

Specifically:
- re-audit PDF 41 fully despite the earlier boundary-only consultation;
- resolve PDF 41→42 `சுயமரியாதை` / `பற்ற செயல்` from both images;
- resolve PDF 42→43 `உமக்குப்` / `பெருமை தந்திடத்தான்`;
- resolve PDF 44→45 `ஊட்` / `டிடும்`;
- inspect PDF 46 only as a boundary witness if needed;
- before declaring any strange vowel form source-supported, test whether it is a traditional glyph for the same Tamil character sequence.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- Source-faithful transcription preserves spelling, not obsolete glyph shape as a wrong Unicode letter.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
