# பள்ளி வாழ்க்கை — visual fidelity and consolidation audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

- Tamil T1 first pass: **complete — 76/76**.
- Strict visual Tamil audit T2: **complete — 76/76**.
- Tamil T3 consolidation/freeze: **in progress — canonical consolidation through PDF 75 / printed 74**.
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

Those files remain the detailed correction log and mandatory T3 evidence.

## Critical traditional-glyph rule

This 1952 printing uses traditional pre-1978 Tamil glyph forms. Source fidelity requires encoding the underlying Tamil characters, not visually similar modern Unicode syllables.

Special watch forms include traditional shapes for `னா`, `றா`, `ணா`, `னை`, `ணை`, `லை`, `ளை`, and related combinations.

Do **not** resurrect superseded glyph readings such as `கற்றோனுக`, `மண்ணுவது`, `நன்றுக`, `வாசனே`, `நிணப்பார்`, `தமிழனுக`, `கவலிப்பட`, `நானு?`, `தோழனுக`, `உறுதுணைவனுக`, `எவலனுக`, `மனிதனுக`, `படைத்தவனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, or `தேவனே` where the scan establishes the corresponding underlying `-னா/-னாக/-ஆக/-னை` reading.

At the same time, T3 must not regularize genuine scan-supported wording merely because it appears unusual.

## T3 canonical consolidation — PDF 6-45

The first canonical pass incorporated all scan-proven T2 corrections for PDF 6-45 and resolved the recorded printer/page-boundary joins.

The T3 stale-reading sweep additionally rechecked and corrected:

- PDF 24 / printed 23: `மனிதனுக` → **`மனிதனாக`**.
- PDF 39 / printed 38: `தேவைத்தானு?` → **`தேவைத்தானா?`**.

Important source-supported forms retained in this range include `வாழ்க்கைச் செந்தி`, `கல்வி கற்கு மிடம்`, `பலமுறைகள்`, `நல்லதங்கள்`, `நாவினை நாட்டினரும்`, `முன்னேற்றம் மடைகின்றன`, `வளர்த்தை`, `வளர்த்தைப்`, `வகைப்படுத்தியாக`, `போற்றிவேண்டும்`, `அரிபந்தாமன்`, `காண்டவன்`, `நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, `கடிக்குலவின`, `மாணுக்கர்களுக்கு`, `பூலோக வாசிகளேப்`, `திடமென்று`, `இறும்பூதெய்தி`, and `என்ன கொடுமதி உமக்கு`.

## T3 canonical consolidation — PDF 46-60

The second canonical pass applied T2 Batches 9-11 to the staged T1 text and passed segment-level stale-reading validation.

### Confirmed corrections incorporated

- PDF 48: `மழையவர்` → `மறையவர்`
- PDF 49: `தோழனுகத்` → `தோழனாகத்`; `அதனின் அச்சிடும்` → `அதன் அச்சிடும்`
- PDF 50: `உறுதுணைவனுக` → `உறுதுணைவனாக`; `உயிரே செல்லும்` → `உயரே செல்லும்`; `எவலனுக` → `ஏவலனாக`
- PDF 51: `மனிதனுக` → `மனிதனாக`
- PDF 52: `ஆளும் நடக்கிறதே` → `ஆனாலும் நடக்கிறதே`
- PDF 53: `இரண்யாட்சன்` → `இரண்ணியாட்சகன்`; `இரண்யாட்சனைத்` → `இரண்ணியாட்சகனைத்`
- PDF 54: `பார்ந்த பூமியை` → `பரந்தபூமியை`; `மூம்மூர்த்திகளில்` → `மும்மூர்த்திகளில்`
- PDF 55: `மோதவிடப்படுகிறது,` → `மோதவிடப்படுகிறது;`; corrupted eclipse sentence replaced with the full scan-supported T2 sentence; `வேறு வேறு காரணங்கள்` → `வேறு வேறான காரணங்கள்`
- PDF 56: `ஒன்றுகவே` → `ஒன்றாகவே`; `உபயோகப்படுத்திக்கொண்டும்` → `உபயோகப் படுத்திக்கொண்டும்`; `அங்கக் கால` → `அந்தக் கால`
- PDF 57: `சிந்தனை முதிர்ச்சி படைந்து` → `சிந்தனை முதிர்ச்சி யடைந்து`; source comma restored in `நாகரிக வாழ்வு, வாழ்வதைப்`
- PDF 60: `தமிழனுக` → `தமிழனாக`; `தமிழ் அறிந்த` → `தமிழறிந்த`

### Verified page-boundary decisions incorporated

- PDF 50→51: `சிந்தித்` / `தான்!` → `சிந்தித்தான்!`
- PDF 55→56: `மற்` / `றொன்று` → `மற்றொன்று`
- PDF 56→57: `வாழ்` / `வாகத்தானே` → `வாழ்வாகத்தானே`

Other page boundaries in PDF 46-60 remain ordinary sentence/phrase continuations as recorded by T2.

### Source-supported forms retained

The consolidation deliberately preserves scan-supported forms including:

- PDF 48: `மனிதனி அறிவு கண்டு`
- PDF 59: `சுதுமதி படைத்தோரால்`
- PDF 59→60: `இராஜ இராஜேந்திரனின்`
- PDF 60: `தமிழனமாக`
- PDF 60: `மதனின் அறிவு வளர்ச்சி பெற்று`

## T3 canonical consolidation — PDF 61-75

The third canonical pass applied T2 Batches 12-14 and passed a segment-level stale-reading validation before the canonical file was advanced to PDF 75.

### Confirmed corrections incorporated

- PDF 62: `கல்வெறிபட்டுக்` → `கல்லெறிபட்டுக்`; `மீனவி மக்களைத் திருந்து` → `மீனவ மக்களைத் துறந்து`
- PDF 63: two `மனிதனுக` readings → `மனிதனாக`; `மிருகத் தன்மையின்றும்` → `மிருகத் தன்மையினின்றும்`; `படைத்தவனுக` → `படைத்தவனாக`
- PDF 64: `மூன்கெட்டு` → `மூளை கெட்டு`; `அறிவும் தன்மை` → `அறியும் தன்மை`
- PDF 65: `தெரிவித்து கொள்வதும்` → `தெரிவித்துக்கொள்வதும்`; `தமிழ் வீரனைத் திகழ்வான்` → `தமிழ் வீரனாகத் திகழ்வான்`
- PDF 66: `மாட்டானு?` → `மாட்டானா?`; `ஒன்றன்பின் ஒன்றுக` → `ஒன்றன்பின் ஒன்றாக`; `அவல் மூச்சாக` → `அனல் மூச்சாக`; `முயல்வதுபோல` → `முயல்வது போல`; `நன்றுக நினைவில்` → `நன்றாக நினைவில்`
- PDF 67: `நன்றுக நினைவிருக்கட்டும்` → `நன்றாக நினைவிருக்கட்டும்`; `வளர்ப்படுத்திக்` → `வளப்படுத்திக்`
- PDF 68: `புத்தக வித்தகர்` → `புத்தகவித்தகர்`; `உலகம்தான்` → source `உலகந்தான்`
- PDF 69: `தந்திரங்களைக் தவறாது` → `தந்திரங்களைத் தவறாது`; `கூடாது; நேரடித்` → source comma `கூடாது, நேரடித்`; `நன்றுக நினைவு` → `நன்றாக நினைவு`
- PDF 70: `தோழனுகவே` → `தோழனாகவே`
- PDF 71: `தேர்வு அறிவிப்பதோடு` → `‘தேர்வு’ அறிவிப்பதோடு`; `மினுபாவங்கொண்ட` → `மனோபாவங்கொண்ட`
- PDF 72: `வேதனை தரும்` → `வேதனைதரும்`; `கேள்விகள், எழுப்புங்கள்?` → `கேள்விகளை, எழுப்புங்கள்?`
- PDF 73: `பரம்பரையின் ராகவே` → `பரம்பரையினராகவே`
- PDF 74: `வழிகத்தையும்` → `வழிகாட்டியையும்`; `கெட்டிக்காரனுக` → `கெட்டிக்காரனாக`; `பெறுபவனுக` → `பெறுபவனாக`; `தானுகவே` → `தானாகவே`
- PDF 75: `வாழும் பொருந்தும்` → `வாழ் பொருந்தும்`; `வறி, அவன்` → `வாழ, அவன்`

### Page-boundary decisions

T2 Batches 12-14 establish the PDF 61-75 boundaries as ordinary phrase/sentence continuations rather than split-word joins. No additional lexical reconstruction was introduced during this T3 pass.

The final boundary witness for this range is PDF 75→76: `அத்துடன்` / `படிக்கிறான்.` — ordinary phrase continuation. It must be preserved when PDF 76 is merged.

### Source-supported forms retained

Examples deliberately preserved include:

- PDF 68: `உலகந்தான்`
- PDF 71: `சோம்பேறி மாணக்கர்`
- PDF 73: `தன்னுலே`
- PDF 75: `இதற்கேல் வாழ் பொருந்தும் முறையிலே`

These must not be silently regularized in the final pass.

## Remaining T3 work

The canonical file now covers **PDF 6-75 / printed 5-74**. Only one staged body segment remains:

- PDF **76-81 / printed 75-80** within `t1-batches/batch-12-pdf-71-81.md`

The final T3 segment must use T2 Batches 15-16. After that merge, run the whole-body T3 gate.

The final T3 gate requires:

1. one continuous canonical `transcription-ta.md` for PDF 6-81 / printed 5-80;
2. every T2/T3 correction applied;
3. no superseded stale glyph reading surviving in the body;
4. all verified page-boundary decisions honored;
5. all source-supported unusual readings retained;
6. no missing or duplicated page heading;
7. exact PDF→printed page mapping 6→5 through 81→80;
8. the verified canonical beginning and final closing present;
9. only then mark Tamil `verified-complete` / frozen and update status files.

English translation remains blocked until that gate passes.