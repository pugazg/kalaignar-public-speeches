# பள்ளி வாழ்க்கை — visual fidelity and consolidation audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

- Tamil T1 first pass: **complete — 76/76**.
- Strict visual Tamil audit T2: **complete — 76/76**.
- Tamil T3 consolidation/freeze: **verified-complete — 76/76; frozen**.
- Final whole-body T3 gate: **PASS**.
- English E1: **not started — permitted to begin from frozen Tamil**.

The supplied scan is authoritative. OCR and T1 are aids only. Later Tamil changes require documented source evidence and dependent English re-verification.

## T2 evidence retained

The detailed page-by-page visual evidence remains under `t2-batches/`:

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

These files remain the correction log and source-fidelity evidence. Obsolete T1 staging files were removed only after the final T3 gate passed.

## Critical traditional-glyph rule

This 1952 printing uses traditional pre-1978 Tamil glyph forms. Source fidelity requires encoding the underlying Tamil characters, not visually similar modern Unicode syllables.

Superseded readings such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, and `தேவனே` were rejected wherever the scan established the corresponding underlying `-னா/-னாக/-னை` reading.

At the same time, T3 did not regularize genuine scan-supported wording merely because it appears unusual.

## T3 consolidation history

### Pass 1 — PDF 6-45

All applicable T2 corrections were incorporated. The stale-reading sweep additionally rechecked and corrected PDF 24 `மனிதனுக` → `மனிதனாக` and PDF 39 `தேவைத்தானு?` → `தேவைத்தானா?` directly against the scan.

### Pass 2 — PDF 46-60

T2 Batches 9-11 were merged. Verified page-boundary joins included `சிந்தித்தான்!`, `மற்றொன்று`, and `வாழ்வாகத்தானே`. Source-supported forms including `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, `மதனின் அறிவு வளர்ச்சி பெற்று`, and `இராஜ இராஜேந்திரனின்` were retained.

### Pass 3 — PDF 61-75

T2 Batches 12-14 were merged. Important corrected forms include `கல்லெறிபட்டுக்`, `மீனவ மக்களைத் துறந்து`, `மனிதனாக`, `மிருகத் தன்மையினின்றும்`, `படைத்தவனாக`, `மூளை கெட்டு`, `அறியும் தன்மை`, `தமிழ் வீரனாகத்`, `மாட்டானா?`, `ஒன்றன்பின் ஒன்றாக`, `அனல் மூச்சாக`, `நன்றாக`, `வளப்படுத்திக்`, `புத்தகவித்தகர்`, `உலகந்தான்`, `தந்திரங்களைத்`, `தோழனாகவே`, `மனோபாவங்கொண்ட`, `வேதனைதரும்`, `பரம்பரையினராகவே`, `வழிகாட்டியையும்`, `கெட்டிக்காரனாக`, `பெறுபவனாக`, `தானாகவே`, and `வாழ, அவன்`.

### Pass 4 — PDF 76-81

T2 Batches 15-16 were merged. Corrections included `அவனாகத்தான்`, `ஒவ்வொருவனுக்கும்`, `ஏய்ப்பது`, `நாடெங்கும்`, `தேவனை நம்பு!`, `தமிழரெல்லாம்`, and `தமிழினத்தை`. Verified split-word joins included `துறைகளிலும்`, `தகுதியையும்`, `ஏற்பட்டது`, and `விளங்குகின்றனர்`.

PDF 75→76 and PDF 80→81 remain ordinary phrase/sentence continuations, exactly as established by T2.

## Final whole-body T3 verification

The end-to-end gate passed across **PDF 6-81 / printed 5-80**. The durable result is recorded in `t3-final-verification.md`.

The gate confirmed:

- exactly **76** unique sequential page headings, PDF 6-81 mapped to printed 5-80;
- no empty or exact-duplicate page body;
- the verified canonical opening and closing;
- absence of the superseded stale forms as complete readings;
- representative scan-proven corrections from T2 Batches 1-16;
- all recorded non-obvious split-word joins used during T3;
- representative ordinary page-boundary continuations;
- representative source-supported unusual forms;
- presence of all 16 T2 batch records and both legacy-glyph recheck records.

Two validation details are worth preserving. The first stale-search implementation reported `தமிழனுக` and `மனிதனுக`, but diagnosis showed those byte sequences only as prefixes inside legitimate words such as `தமிழனுக்கு` and `மனிதனுக்கு`; the gate was therefore corrected to test complete stale forms instead of substrings. No Tamil source text was changed for those false positives. A later check expected the contiguous phrase `சுயமரியாதையற்ற செயல்`, but the canonical page structure correctly keeps `சுயமரியாதையற்ற` at the end of PDF 41 and `செயல்` on PDF 42; the final gate therefore verifies the reconstructed word and the preserved page boundary separately.

Representative source-supported unusual readings retained through freeze include `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `மதனின் அறிவு வளர்ச்சி பெற்று`, `சுதுமதி படைத்தோரால்`, `இராஜ இராஜேந்திரனின்`, `உலகந்தான்`, `தன்னுலே`, `சோம்பேறி மாணக்கர்`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, and `உலகியலேக் காண`.

## Freeze decision

`transcription-ta.md` is now the **verified-complete frozen Tamil layer**. Any later Tamil change requires documented source evidence and dependent English re-verification.

The next textual gate is **E1 English translation**, which must be produced only from the frozen `transcription-ta.md` while retaining PDF/printed-page correspondence.