# பள்ளி வாழ்க்கை — visual fidelity audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Source-inspection date:** 2026-08-15  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

Tamil first-pass transcription (T1) is **complete: 76/76 body pages**.

Strict visual Tamil audit (T2) is **in progress: 40/76 pages**, through PDF 45 / printed 44.

Before Batch 8, user review identified a systematic transcription issue with traditional pre-1978 Tamil glyphs. A corrective sweep was completed through PDF 40. Batch 8 was audited with the corrected glyph interpretation from the outset.

English remains blocked.

## Critical traditional-glyph rule

This 1952 edition uses traditional Tamil glyph forms. Some shapes changed in the later Tamil script reform while representing the same underlying Tamil characters. Source fidelity therefore means encoding the **underlying Tamil character sequence**, not selecting a visually similar but different modern Unicode syllable.

Special watch list includes traditional forms of:
- `னா`, `றா`, `ணா`
- `னை`, `ணை`, `லை`, `ளை`
- related `ஒ/ஓ` combinations

Do not misread these as modern-looking `னு`, `று`, `ணு`, `னே`, `லி`, etc.

Corrective records:
- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

## T2 batch records

- Batch 1: `t2-batches/batch-01-pdf-06-10.md`
- Batch 2: `t2-batches/batch-02-pdf-11-15.md`
- Batch 3: `t2-batches/batch-03-pdf-16-20.md`
- Batch 4: `t2-batches/batch-04-pdf-21-25.md`
- Batch 5: `t2-batches/batch-05-pdf-26-30.md`
- Batch 6: `t2-batches/batch-06-pdf-31-35.md`
- Batch 7: `t2-batches/batch-07-pdf-36-40.md`
- Batch 8: `t2-batches/batch-08-pdf-41-45.md`

## Confirmed substantive corrections that remain valid

### Batch 1
- `ஆராய்ந்து தெரிந்து` → `ஆராய்ந்து தெளிந்து`

### Batch 2
- `தோவினாலும்` → `தோலினாலும்`
- `மனித வாழ்க்கத்தின்` → `மனித வர்க்கத்தின்`
- `மனித வாழ்க்கத்தை` → `மனித வர்க்கத்தை`
- `ஒருபடியாக` → `ஒருப்படியாக`
- `வயல் உழுது` → `வயலில் உழுது`

### Batch 3
- `வரவிட` → `வரைவிட`

### Batch 4
- `இடம் கிடைத்து` → `இடம் உடைத்து`

### Batch 5
- `இத்தை வெறுத்து` → `இகத்தை வெறுத்து`
- `தன்னேப்பற்றிக்` → `தன்னைப்பற்றிக்`

### Batch 6
- `தனது வில்லெடுத்து,` → `தனது வில்லைபூட்டி,`
- `குறித்துவிட்டோடும்` → `குருதிவடிந்தோடும்`

### Batch 7
- `தாங்கள்தான்` → `தாங்கள் தான்`
- `ஏகலவனின் மறுபடி` → `ஏகலவனை மறுபடி`
- `பகுதிக்கு` → `பக்திக்கு`
- `சிரச் சினந்து` → `சீறிச் சினந்து`

### Batch 8
- PDF 41→42: `சுயமரியாதை` / `பற்ற செயல்` → `சுயமரியாதை` / `யற்ற செயல்` → `சுயமரியாதையற்ற செயல்`
- PDF 42: `தினதயாளன்` → `தீனதயாளன்`
- PDF 42: `ஆல கால` → `ஆலகால`
- PDF 42: `நீலகண்டனூர்` → `நீலகண்டனார்`
- PDF 42: `திடமென்று` → `திடீரென்று`
- PDF 43: `சிவத்தொண்டு` → `சிவத் தொண்டு` in the audited phrase
- PDF 43: `மினையாளைக்` → `மனையாளைக்`
- PDF 43: `முறைதானு?` → `முறைதானா?`
- PDF 44: `தேவைத்தான்` → `தேவைதான்`
- PDF 44: `கோட்டாடுகளைப்போற்றிப்` → `கோட்பாடுகளைப்போற்றிப்`
- PDF 44: `சிக்கச் சீழிய` → `சிக்கச் செய்ய`
- PDF 45: `தேவைத்தானு` → `தேவைதானா`

## Superseded readings caused by legacy-glyph misinterpretation

The following earlier T2 claims are withdrawn and must **not** enter T3:

- `கற்றோனுக` → use `கற்றோனாக`
- `கல்லூரனுக` → `கல்லூரனாக`
- `கதாசிரியனுக` → `கதாசிரியனாக`
- `கட்டுரையாசிரியனுக` → `கட்டுரையாசிரியனாக`
- `உத்தமனுக` → `உத்தமனாக`
- `மண்ணுவது` → `மண்ணாவது` (both audited occurrences)
- `நன்றுக` → `நன்றாக`
- `வாசனே` → `வாசனை`
- `நிணப்பார்` → `நினைப்பார்`
- `நிணக்க` → `நினைக்க`
- `நிணத்திடும்` → `நினைத்திடும்`
- `திடசித்தமுடையவனுக` → `திடசித்தமுடையவனாக`
- `தமிழனுக` → `தமிழனாக`
- `கவலிப்பட` → `கவலைப்பட`
- `தேவைத்தானு` on earlier audited pages → correct underlying `-தானா` reading as documented in the legacy-glyph recheck
- `நானு?` → `நானா?`

## Confirmed page-boundary / printer-wrap decisions

- PDF 9→10: `உயி` / `ரினங்களைவிட` → `உயிரினங்களைவிட`
- PDF 13→14: `இவர்` / `கட்கு` → `இவர்கட்கு`
- PDF 18→19: `கஞ்சிக்` / `காவது` → `கஞ்சிக்காவது`
- PDF 19→20: `எட்டுச்` / `சுரையெனப்` → `எட்டுச்சுரையெனப்`
- printed p.19 internal: `தன்னம்` / `பிக்கையும்` → `தன்னம்பிக்கையும்`
- PDF 23→24: `உள்ள` / `படி` → `உள்ளபடி`
- PDF 31→32: `தமிழினத்` / `தைப்` → `தமிழினத்தைப்`
- PDF 32→33: `பசுமரத்` / `தாணிபோலப்` → `பசுமரத்தாணிபோலப்`
- PDF 37→38: `வலதுகைப்` / `பெருவிரல்` is ordinary phrase continuation → `வலதுகைப் பெருவிரல்`
- PDF 38→39: `சாபந் தந்த` / `பிரகஸ்பதி பகவான்களும்` is ordinary sentence continuation
- PDF 40→41: `தேடு` / `கிறீர்;` → `தேடுகிறீர்;`
- PDF 41→42: `சுயமரியாதை` / `யற்ற செயல்` → `சுயமரியாதையற்ற செயல்`
- PDF 42→43: `உமக்குப்` / `பெருமை தந்திடத்தான்` is ordinary phrase continuation, not a split word
- PDF 44→45: `ஊட்` / `டிடும்` → `ஊட்டிடும்`
- PDF 45→46: `வருணபகவான் என்றும்` / `இடிக்குத் தலைவன் இந்திரன் என்றும்` is ordinary sentence continuation; PDF 46 was only a boundary witness in Batch 8

## Current readings still requiring ordinary source scrutiny

Do not call a form historical merely because it looks strange. These remain provisional until the relevant T2/T3 check:

- `உயிரினங்களின் றும்`
- `வாழ்க்கைச் செந்தி`
- `கல்வி கற்கு மிடம்`
- `பலமுறைகள்`
- `நல்லதங்கள்`
- `நாவினை நாட்டினரும்`
- `முன்னேற்றம் மடைகின்றன`
- `வளர்த்தை`, `வளர்த்தைப்`, `வகைப்படுத்தியாக`
- `போற்றிவேண்டும்`
- `அரிபந்தாமன்`
- `காண்டவன்`
- `நாயகனுக்கிக்கொண்ட`
- `சந்திரனச் சல்லாபத்திற்`
- `கடிக்குலவின`
- `மாணுக்கர்களுக்கு`
- `பூலோக வாசிகளேப்`
- `இறும்பூதெய்தி`
- `என்ன கொடுமதி உமக்கு`
- later T1 forms such as `மனிதனுக`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `கெட்டிக்காரனுக`, etc. are specifically flagged for traditional `னா` reinterpretation before acceptance

## Remaining page-boundary queue

- PDF 50→51: `சிந்தித்` / `தான்!`
- later boundaries in Batches 10-12 remain pending direct visual inspection

## T2 progress

| PDF pages | Printed pages | T2 state |
|---:|---:|---|
| 6-10 | 5-9 | **audited; legacy glyphs rechecked** |
| 11-15 | 10-14 | **audited; legacy glyphs rechecked** |
| 16-20 | 15-19 | **audited** |
| 21-25 | 20-24 | **audited; legacy glyphs rechecked** |
| 26-30 | 25-29 | **audited; legacy glyphs rechecked** |
| 31-35 | 30-34 | **audited; legacy glyphs rechecked** |
| 36-40 | 35-39 | **audited; legacy glyphs rechecked** |
| 41-45 | 40-44 | **audited with corrected traditional-glyph rule** |
| 46-81 | 45-80 | pending |

## Exact next activity

Audit **PDF pages 46-50 / printed pages 45-49** line-by-line against the scan. PDF 46 must be audited fully despite having been used only as a boundary witness for Batch 8. Apply the traditional-glyph rule from the outset, especially to T1 forms such as `தோழனுக`, `உறுதுணைவனுக`, and `எவலனுக`. Resolve PDF 50→51 `சிந்தித்` / `தான்!` by consulting PDF 51 only as a boundary witness; do not count PDF 51 audited until its own batch.

After all 76 pages pass T2, perform T3 canonical consolidation, apply every valid correction, reject every superseded legacy-glyph misreading, run stale-reading/page-boundary checks, and freeze Tamil only when verified-complete.
