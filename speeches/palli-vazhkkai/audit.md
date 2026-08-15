# பள்ளி வாழ்க்கை — visual fidelity and consolidation audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

- Tamil T1 first pass: **complete — 76/76**.
- Strict visual Tamil audit T2: **complete — 76/76**.
- Tamil T3 consolidation: **all 76 pages merged into canonical `transcription-ta.md`**.
- Final whole-body T3 freeze gate: **pending**.
- Tamil frozen / `verified-complete`: **No**.
- English: blocked until T3 passes.

The supplied scan is authoritative. OCR and T1 are aids only.

## T2 evidence

The detailed page-by-page T2 evidence remains preserved under `t2-batches/`:

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

Those files remain the correction log and mandatory T3 evidence.

## Critical traditional-glyph rule

This 1952 printing uses traditional pre-1978 Tamil glyph forms. Source fidelity requires encoding the underlying Tamil characters, not visually similar modern Unicode syllables.

Do **not** resurrect superseded glyph readings such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, or `தேவனே` where the scan establishes the corrected underlying reading.

At the same time, T3 must not regularize genuine scan-supported wording merely because it appears unusual.

## T3 consolidation history

### Pass 1 — PDF 6-45
All scan-proven T2 corrections applicable to PDF 6-45 were incorporated. The stale-reading sweep additionally rechecked and corrected PDF 24 `மனிதனுக` → `மனிதனாக` and PDF 39 `தேவைத்தானு?` → `தேவைத்தானா?` against the scan.

### Pass 2 — PDF 46-60
T2 Batches 9-11 were merged. Verified page-boundary joins included `சிந்தித்தான்!`, `மற்றொன்று`, and `வாழ்வாகத்தானே`. Source-supported forms such as `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, `மதனின் அறிவு வளர்ச்சி பெற்று`, and `இராஜ இராஜேந்திரனின்` were retained.

### Pass 3 — PDF 61-75
T2 Batches 12-14 were merged. Important corrected forms include `கல்லெறிபட்டுக்`, `மீனவ மக்களைத் துறந்து`, `மனிதனாக`, `மிருகத் தன்மையினின்றும்`, `படைத்தவனாக`, `மூளை கெட்டு`, `அறியும் தன்மை`, `தமிழ் வீரனாகத்`, `மாட்டானா?`, `ஒன்றன்பின் ஒன்றாக`, `அனல் மூச்சாக`, `நன்றாக`, `வளப்படுத்திக்`, `புத்தகவித்தகர்`, `உலகந்தான்`, `தந்திரங்களைத்`, `தோழனாகவே`, `மனோபாவங்கொண்ட`, `வேதனைதரும்`, `பரம்பரையினராகவே`, `வழிகாட்டியையும்`, `கெட்டிக்காரனாக`, `பெறுபவனாக`, `தானாகவே`, and `வாழ, அவன்`.

Source-supported oddities including `உலகந்தான்`, `தன்னுலே`, `சோம்பேறி மாணக்கர்`, and `இதற்கேல் வாழ் பொருந்தும் முறையிலே` were preserved.

### Pass 4 — PDF 76-81
T2 Batches 15-16 were merged.

Confirmed corrections incorporated:

1. PDF 76: `அவனுகத்தான்` → `அவனாகத்தான்`
2. PDF 77: `ஒவ்வொரு வனுக்கும்` → `ஒவ்வொருவனுக்கும்`
3. PDF 77: `எய்ப்பது` → `ஏய்ப்பது`
4. PDF 78: `நாட்டெங்கும்` → `நாடெங்கும்`
5. PDF 80: `தேவனே நம்பு!` → `தேவனை நம்பு!`
6. PDF 81: `தமிழமெல்லாம்` → `தமிழரெல்லாம்`
7. PDF 81: `தமிழனத்தை` → `தமிழினத்தை`

Verified split-word joins incorporated:

- PDF 76→77: `துறை` / `களிலும்` → `துறைகளிலும்`
- PDF 77→78: `தகுதியை` / `யும்` → `தகுதியையும்`
- PDF 78→79: `ஏற்பட்` / `டது` → `ஏற்பட்டது`
- PDF 79→80: `விளங்குகின்ற` / `னர்` → `விளங்குகின்றனர்`

PDF 75→76 and PDF 80→81 are ordinary phrase/sentence continuations and were not lexically reconstructed.

The pass-level validation confirmed:

- canonical headings now span PDF **6-81** / printed **5-80**;
- the final segment contains none of its superseded T1 readings;
- required corrected forms are present;
- `உலகியலேக் காண` is retained;
- the canonical file ends with the verified closing `பள்ளி வாழ்க்கையில்! வணக்கம் !!`.

## Exact next activity — final whole-body T3 gate

Run an end-to-end verification across the complete canonical file:

1. confirm exactly **76** unique sequential page headings: PDF 6-81 / printed 5-80;
2. search for every superseded T1/T2/traditional-glyph reading across the whole body;
3. verify every recorded split-word reconstruction and ordinary boundary continuation from all T2 batches;
4. verify no page was omitted or duplicated during the four consolidation passes;
5. verify the canonical opening and final closing;
6. verify representative source-supported unusual readings remain unchanged;
7. only if all checks pass, change the canonical status to `verified-complete`, set `tamil_frozen: true`, synchronize metadata/README/audit/HANDOVER, and unlock English translation.

T1 staging files and T2 evidence remain retained until this gate passes.