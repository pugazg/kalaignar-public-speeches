# பள்ளி வாழ்க்கை — visual fidelity audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

- Tamil T1 first pass: **complete — 76/76**.
- Strict visual Tamil audit T2: **in progress — 45/76**, through PDF 50 / printed 49.
- Tamil T3 consolidation/freeze: not started.
- English: blocked until T2 and T3 pass.

The supplied scan is authoritative. OCR/T1 are only aids.

## Critical traditional-glyph rule

This 1952 printing uses traditional pre-1978 Tamil glyph forms. Source fidelity requires encoding the underlying Tamil characters, not a visually similar modern Unicode syllable.

Special watch forms include traditional shapes for `னா`, `றா`, `ணா`, `னை`, `ணை`, `லை`, `ளை`, and related combinations. Earlier glyph-based misreadings were corrected in:

- `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
- `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

Batches 8 and 9 were audited with the corrected rule from the outset.

## T2 batch records

- Batch 1: `t2-batches/batch-01-pdf-06-10.md`
- Batch 2: `t2-batches/batch-02-pdf-11-15.md`
- Batch 3: `t2-batches/batch-03-pdf-16-20.md`
- Batch 4: `t2-batches/batch-04-pdf-21-25.md`
- Batch 5: `t2-batches/batch-05-pdf-26-30.md`
- Batch 6: `t2-batches/batch-06-pdf-31-35.md`
- Batch 7: `t2-batches/batch-07-pdf-36-40.md`
- Batch 8: `t2-batches/batch-08-pdf-41-45.md`
- Batch 9: `t2-batches/batch-09-pdf-46-50.md`

## Confirmed scan-proven corrections retained for T3

### Batches 1-7

- `ஆராய்ந்து தெரிந்து` → `ஆராய்ந்து தெளிந்து`
- `தோவினாலும்` → `தோலினாலும்`
- `மனித வாழ்க்கத்தின்` → `மனித வர்க்கத்தின்`
- `மனித வாழ்க்கத்தை` → `மனித வர்க்கத்தை`
- `ஒருபடியாக` → `ஒருப்படியாக`
- `வயல் உழுது` → `வயலில் உழுது`
- `வரவிட` → `வரைவிட`
- `இடம் கிடைத்து` → `இடம் உடைத்து`
- `இத்தை வெறுத்து` → `இகத்தை வெறுத்து`
- `தன்னேப்பற்றிக்` → `தன்னைப்பற்றிக்`
- `தனது வில்லெடுத்து` → `தனது வில்லைபூட்டி`
- `குறித்துவிட்டோடும்` → `குருதிவடிந்தோடும்`
- `தாங்கள்தான்` → `தாங்கள் தான்`
- `ஏகலவனின் மறுபடி` → `ஏகலவனை மறுபடி`
- `பகுதிக்கு` → `பக்திக்கு`
- `சிரச் சினந்து` → `சீறிச் சினந்து`

### Batch 8 — PDF 41-45

- `சுயமரியாதை` / `பற்ற செயல்` → `சுயமரியாதை` / `யற்ற செயல்` → `சுயமரியாதையற்ற செயல்`
- `தினதயாளன்` → `தீனதயாளன்`
- `ஆல கால` → `ஆலகால`
- `நீலகண்டனூர்` → `நீலகண்டனார்`
- `திடமென்று` → `திடீரென்று`
- `சிவத்தொண்டு` → `சிவத் தொண்டு` in the audited phrase
- `மினையாளைக்` → `மனையாளைக்`
- `முறைதானு?` → `முறைதானா?`
- `தேவைத்தான்` → `தேவைதான்`
- `கோட்டாடுகளைப்போற்றிப்` → `கோட்பாடுகளைப்போற்றிப்`
- `சிக்கச் சீழிய` → `சிக்கச் செய்ய`
- `தேவைத்தானு` → `தேவைதானா`

### Batch 9 — PDF 46-50

- PDF 48: `மழையவர்` → `மறையவர்`
- PDF 49: `தோழனுகத்` → `தோழனாகத்`
- PDF 49: `அதனின் அச்சிடும்` → `அதன் அச்சிடும்`
- PDF 50: `உறுதுணைவனுக` → `உறுதுணைவனாக`
- PDF 50: `உயிரே செல்லும்` → `உயரே செல்லும்`
- PDF 50: `எவலனுக` → `ஏவலனாக`

The scan also confirms PDF 48 `மனிதனி அறிவு கண்டு`; retain that source wording rather than silently changing it to `மனிதனின்`.

## Superseded legacy-glyph readings — DO NOT USE

Earlier claims caused only by visual misinterpretation of traditional glyphs are withdrawn. These include forms such as:

- `கற்றோனுக` → `கற்றோனாக`
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
- earlier `தேவைத்தானு` glyph readings → underlying `-தானா` where documented
- `நானு?` → `நானா?`

T3 must not resurrect any superseded glyph-misreading.

## Confirmed page-boundary / printer-wrap decisions

- PDF 9→10: `உயி` / `ரினங்களைவிட` → `உயிரினங்களைவிட`
- PDF 13→14: `இவர்` / `கட்கு` → `இவர்கட்கு`
- PDF 18→19: `கஞ்சிக்` / `காவது` → `கஞ்சிக்காவது`
- PDF 19→20: `எட்டுச்` / `சுரையெனப்` → `எட்டுச்சுரையெனப்`
- PDF 23→24: `உள்ள` / `படி` → `உள்ளபடி`
- PDF 31→32: `தமிழினத்` / `தைப்` → `தமிழினத்தைப்`
- PDF 32→33: `பசுமரத்` / `தாணிபோலப்` → `பசுமரத்தாணிபோலப்`
- PDF 37→38: `வலதுகைப்` / `பெருவிரல்` — ordinary phrase continuation; retain space
- PDF 38→39: `சாபந் தந்த` / `பிரகஸ்பதி பகவான்களும்` — ordinary sentence continuation
- PDF 40→41: `தேடு` / `கிறீர்;` → `தேடுகிறீர்;`
- PDF 41→42: `சுயமரியாதை` / `யற்ற செயல்` → `சுயமரியாதையற்ற செயல்`
- PDF 42→43: `உமக்குப்` / `பெருமை தந்திடத்தான்` — ordinary phrase continuation
- PDF 44→45: `ஊட்` / `டிடும்` → `ஊட்டிடும்`
- PDF 45→46: `வருணபகவான் என்றும்` / `இடிக்குத் தலைவன் இந்திரன் என்றும்` — ordinary sentence continuation
- PDF 47→48: `... இரண்டு வழிகளில், எது` / `வேண்டும் இன்று!` — ordinary phrase continuation
- PDF 49→50: `காலம் அறிவிக்கும்` / `கடிகார வகைகள்` — ordinary phrase continuation
- PDF 50→51: `சிந்தித்` / `தான்!` → `சிந்தித்தான்!`; PDF 51 used only as boundary witness in Batch 9

## T2 progress

| PDF pages | Printed pages | State |
|---:|---:|---|
| 6-10 | 5-9 | audited |
| 11-15 | 10-14 | audited |
| 16-20 | 15-19 | audited |
| 21-25 | 20-24 | audited |
| 26-30 | 25-29 | audited |
| 31-35 | 30-34 | audited |
| 36-40 | 35-39 | audited |
| 41-45 | 40-44 | audited |
| 46-50 | 45-49 | audited |
| 51-81 | 50-80 | pending |

## Exact next activity

Audit **PDF pages 51-55 / printed pages 50-54** line-by-line against the scan. PDF 51 must be fully audited even though its opening `தான்!` was already inspected only to resolve the PDF 50→51 split. Apply the traditional-glyph rule from the outset and record only scan-proven corrections.

After all 76 pages pass T2, perform T3 canonical consolidation, apply every valid correction, run stale-reading/page-boundary checks, and freeze Tamil only when verified-complete.