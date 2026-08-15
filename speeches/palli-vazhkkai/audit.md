# பள்ளி வாழ்க்கை — visual fidelity and consolidation audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

- Tamil T1 first pass: **complete — 76/76**.
- Strict visual Tamil audit T2: **complete — 76/76**.
- Tamil T3 consolidation/freeze: **in progress — canonical consolidation through PDF 45 / printed 44**.
- Tamil frozen / `verified-complete`: **No**.
- English: blocked until T3 passes.

The supplied scan is authoritative. OCR and T1 are aids only.

## T2 evidence

The detailed page-by-page T2 evidence remains preserved in `t2-batches/`:

- `batch-01-pdf-06-10.md`
- `batch-02-pdf-11-15.md`
- `batch-03-pdf-16-20.md`
- `batch-04-pdf-21-25.md`
- `batch-05-pdf-26-30.md`
- `batch-06-pdf-31-35.md`
- `batch-07-pdf-36-40.md`
- `batch-08-pdf-41-45.md`
- `batch-09-pdf-46-50.md`
- `batch-10-pdf-51-55.md`
- `batch-11-pdf-56-60.md`
- `batch-12-pdf-61-65.md`
- `batch-13-pdf-66-70.md`
- `batch-14-pdf-71-75.md`
- `batch-15-pdf-76-80.md`
- `batch-16-pdf-81.md`
- `legacy-glyph-recheck-pdf-06-35.md`
- `legacy-glyph-recheck-pdf-36-40.md`

Those files are the detailed correction log and remain mandatory inputs to T3.

## Critical traditional-glyph rule

This 1952 printing uses traditional pre-1978 Tamil glyph forms. Source fidelity requires encoding the underlying Tamil characters, not visually similar modern Unicode syllables.

Special watch forms include traditional shapes for `னா`, `றா`, `ணா`, `னை`, `ணை`, `லை`, `ளை`, and related combinations.

Do **not** resurrect superseded glyph readings such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, or `தேவனே` where the scan establishes the corresponding underlying `-னா/-னாக/-ஆக/-னை` reading.

At the same time, T3 must not regularize genuine scan-supported wording merely because it appears unusual.

## T3 consolidation completed so far — PDF 6-45

`transcription-ta.md` has been rebuilt as the active canonical layer through **PDF 45 / printed page 44**. All known T2 corrections for that range have been applied, including the legacy-glyph correction set and verified printer/page-boundary joins.

### T3 stale-reading discoveries

The T3 sweep exposed two residual old-glyph readings that had survived the earlier audit summaries. Both were visually rechecked against their actual scan pages before correction:

- PDF 24 / printed 23: `மனிதனுக` → **`மனிதனாக`**.
- PDF 39 / printed 38: `தேவைத்தானு?` → **`தேவைத்தானா?`**.

These are glyph-decoding corrections, not modernization. They are now present in the canonical transcription and must be carried into the final frozen layer.

### Important source-supported forms retained in PDF 6-45

Examples intentionally retained because the scan supports them include:

- PDF 14: `வாழ்க்கைச் செந்தி`
- PDF 19: `கல்வி கற்கு மிடம்`
- PDF 22: `பலமுறைகள்`
- PDF 24: `நல்லதங்கள்`, `நாவினை நாட்டினரும்`
- PDF 27: `முன்னேற்றம் மடைகின்றன`
- PDF 30: `வளர்த்தை`, `வளர்த்தைப்`, `வகைப்படுத்தியாக`
- PDF 32: `போற்றிவேண்டும்`
- PDF 33: `அரிபந்தாமன்`
- PDF 35: `காண்டவன்`
- PDF 38: `நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, `கடிக்குலவின`
- PDF 39: `மாணுக்கர்களுக்கு`, `பூலோக வாசிகளேப்`, `திடமென்று`
- PDF 40: `இறும்பூதெய்தி`, `என்ன கொடுமதி உமக்கு`

## Verified page-boundary decisions already consolidated in PDF 6-45

- PDF 9→10: `உயி` / `ரினங்களைவிட` → `உயிரினங்களைவிட`
- PDF 13→14: `இவர்` / `கட்கு` → `இவர்கட்கு`
- PDF 18→19: `கஞ்சிக்` / `காவது` → `கஞ்சிக்காவது`
- PDF 19→20: `எட்டுச்` / `சுரையெனப்` → `எட்டுச்சுரையெனப்`
- PDF 23→24: `உள்ள` / `படி` → `உள்ளபடி`
- PDF 31→32: `தமிழினத்` / `தைப்` → `தமிழினத்தைப்`
- PDF 32→33: `பசுமரத்` / `தாணிபோலப்` → `பசுமரத்தாணிபோலப்`
- PDF 37→38: ordinary phrase continuation after `வலதுகைப்`
- PDF 38→39: ordinary sentence continuation after `சாபந் தந்த`
- PDF 40→41: `தேடு` / `கிறீர்;` → `தேடுகிறீர்;`
- PDF 41→42: `சுயமரியாதை` / `யற்ற` → `சுயமரியாதையற்ற`
- PDF 42→43: ordinary phrase continuation after `உமக்குப்`
- PDF 44→45: `ஊட்` / `டிடும்` → `ஊட்டிடும்`

## Remaining T3 work

T1 staging still holds PDF 46-81:

- `t1-batches/batch-09-pdf-46-50.md`
- `t1-batches/batch-10-pdf-51-60.md`
- `t1-batches/batch-11-pdf-61-70.md`
- `t1-batches/batch-12-pdf-71-81.md`

The next T3 segment is **PDF 46-60 / printed 45-59**. Apply T2 Batches 9-11, then verify these boundary joins in particular:

- PDF 50→51: `சிந்தித்` / `தான்!` → `சிந்தித்தான்!`
- PDF 55→56: `மற்` / `றொன்று` → `மற்றொன்று`
- PDF 56→57: `வாழ்` / `வாகத்தானே` → `வாழ்வாகத்தானே`

After PDF 46-60 passes its stale-reading check, continue PDF 61-81. The final T3 gate requires:

1. one continuous canonical `transcription-ta.md` for PDF 6-81 / printed 5-80;
2. every T2/T3 correction applied;
3. no superseded stale glyph reading surviving in the body;
4. all verified page-boundary joins resolved;
5. all source-supported unusual readings retained;
6. no missing or duplicated page heading;
7. the verified final closing present;
8. only then mark Tamil `verified-complete` / frozen and remove obsolete T1 staging files.

English translation remains blocked until that gate passes.