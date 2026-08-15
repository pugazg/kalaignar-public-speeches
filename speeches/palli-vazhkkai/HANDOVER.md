# பள்ளி வாழ்க்கை — T3 handover

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
All **76/76** body pages have first-pass readings.

### T2 — COMPLETE
All **76/76** body pages passed strict visual audit. Detailed evidence remains under `t2-batches/`, including Batches 1-16 and the two legacy-glyph recheck records.

### T3 — IN PROGRESS
The canonical `transcription-ta.md` has now been rebuilt and corrected through:

- **PDF 6-75 / printed 5-74 — T3 consolidated into the canonical file**
- PDF 76-81 / printed 75-80 — still staged within `t1-batches/batch-12-pdf-71-81.md`

Tamil is **not yet frozen / verified-complete**. English remains blocked.

## T3 work completed

### First canonical pass — PDF 6-45
All known T2 corrections applicable to PDF 6-45 were incorporated, including the user-triggered traditional-glyph corrections and verified cross-page word joins.

The stale-reading sweep exposed two residual old-glyph misreadings that were rechecked directly against the scan:

- PDF 24 / printed 23: `மனிதனுக` → **`மனிதனாக`**
- PDF 39 / printed 38: `தேவைத்தானு?` → **`தேவைத்தானா?`**

### Second canonical pass — PDF 46-60
All scan-proven corrections from T2 Batches 9-11 were merged into the canonical transcription. Important examples include:

- PDF 48: `மழையவர்` → `மறையவர்`
- PDF 49: `தோழனுகத்` → `தோழனாகத்`; `அதனின் அச்சிடும்` → `அதன் அச்சிடும்`
- PDF 50: `உறுதுணைவனுக` → `உறுதுணைவனாக`; `உயிரே செல்லும்` → `உயரே செல்லும்`; `எவலனுக` → `ஏவலனாக`
- PDF 51: `மனிதனுக` → `மனிதனாக`
- PDF 52: `ஆளும்` → `ஆனாலும்`
- PDF 53: `இரண்யாட்சன் / இரண்யாட்சனைத்` → `இரண்ணியாட்சகன் / இரண்ணியாட்சகனைத்`
- PDF 54: `பார்ந்த பூமியை` → `பரந்தபூமியை`; `மூம்மூர்த்திகளில்` → `மும்மூர்த்திகளில்`
- PDF 55: source semicolon restored after `மோதவிடப்படுகிறது`; corrupted eclipse explanation replaced with the full scan-supported sentence; `வேறு வேறு காரணங்கள்` → `வேறு வேறான காரணங்கள்`
- PDF 56: `ஒன்றுகவே` → `ஒன்றாகவே`; `உபயோகப்படுத்திக்கொண்டும்` → `உபயோகப் படுத்திக்கொண்டும்`; `அங்கக் கால` → `அந்தக் கால`
- PDF 57: `சிந்தனை முதிர்ச்சி படைந்து` → `சிந்தனை முதிர்ச்சி யடைந்து`; source comma restored in `நாகரிக வாழ்வு, வாழ்வதைப்`
- PDF 60: `தமிழனுக` → `தமிழனாக`; `தமிழ் அறிந்த` → `தமிழறிந்த`

Verified page-boundary joins applied in this pass:
- PDF 50→51: `சிந்தித்` / `தான்!` → `சிந்தித்தான்!`
- PDF 55→56: `மற்` / `றொன்று` → `மற்றொன்று`
- PDF 56→57: `வாழ்` / `வாகத்தானே` → `வாழ்வாகத்தானே`

### Third canonical pass — PDF 61-75
All scan-proven corrections from T2 Batches 12-14 were merged and the segment-level stale-reading validation passed.

Important incorporated corrections include:

- PDF 62: `கல்வெறிபட்டுக்` → `கல்லெறிபட்டுக்`; `மீனவி மக்களைத் திருந்து` → `மீனவ மக்களைத் துறந்து`
- PDF 63: both `மனிதனுக` → `மனிதனாக`; `மிருகத் தன்மையின்றும்` → `மிருகத் தன்மையினின்றும்`; `படைத்தவனுக` → `படைத்தவனாக`
- PDF 64: `மூன்கெட்டு` → `மூளை கெட்டு`; `அறிவும் தன்மை` → `அறியும் தன்மை`
- PDF 65: `தெரிவித்து கொள்வதும்` → `தெரிவித்துக்கொள்வதும்`; `தமிழ் வீரனைத் திகழ்வான்` → `தமிழ் வீரனாகத் திகழ்வான்`
- PDF 66: `மாட்டானு?` → `மாட்டானா?`; `ஒன்றன்பின் ஒன்றுக` → `ஒன்றன்பின் ஒன்றாக`; `அவல் மூச்சாக` → `அனல் மூச்சாக`; `முயல்வதுபோல` → `முயல்வது போல`; `நன்றுக நினைவில்` → `நன்றாக நினைவில்`
- PDF 67: `நன்றுக நினைவிருக்கட்டும்` → `நன்றாக நினைவிருக்கட்டும்`; `வளர்ப்படுத்திக்` → `வளப்படுத்திக்`
- PDF 68: `புத்தக வித்தகர்` → `புத்தகவித்தகர்`; `உலகம்தான்` → source-supported `உலகந்தான்`
- PDF 69: `தந்திரங்களைக் தவறாது` → `தந்திரங்களைத் தவறாது`; semicolon before `நேரடித்` corrected to the source comma; `நன்றுக நினைவு` → `நன்றாக நினைவு`
- PDF 70: `தோழனுகவே` → `தோழனாகவே`
- PDF 71: quotation marks restored in `‘தேர்வு’`; `மினுபாவங்கொண்ட` → `மனோபாவங்கொண்ட`
- PDF 72: `வேதனை தரும்` → `வேதனைதரும்`; `கேள்விகள், எழுப்புங்கள்?` → `கேள்விகளை, எழுப்புங்கள்?`
- PDF 73: `பரம்பரையின் ராகவே` → `பரம்பரையினராகவே`
- PDF 74: `வழிகத்தையும்` → `வழிகாட்டியையும்`; `கெட்டிக்காரனுக` → `கெட்டிக்காரனாக`; `பெறுபவனுக` → `பெறுபவனாக`; `தானுகவே` → `தானாகவே`
- PDF 75: `வாழும் பொருந்தும்` → `வாழ் பொருந்தும்`; `வறி, அவன்` → `வாழ, அவன்`

T2 records establish the PDF 61-75 page boundaries as ordinary phrase/sentence continuations rather than split-word joins, so no extra lexical reconstruction was introduced in this pass.

Source-supported unusual forms deliberately retained include `உலகந்தான்`, `தன்னுலே`, `சோம்பேறி மாணக்கர்`, and `இதற்கேல் வாழ் பொருந்தும் முறையிலே`.

## Mandatory traditional-glyph rule

The 1952 printing uses traditional Tamil glyphs. Encode the underlying Tamil characters, not visually similar modern Unicode syllables. Do not resurrect superseded readings such as `கவலிப்பட`, `நன்றுக`, `தமிழனுக`, `மனிதனுக`, `தேவைத்தானு`, `தோழனுக`, `மாட்டானு`, `ஒன்றுக`, `தோழனுகவே`, `கெட்டிக்காரனுக`, `பெறுபவனுக`, `தானுகவே`, `அவனுகத்தான்`, or `தேவனே` where the scan proves the corresponding underlying reading.

At the same time, do not regularize genuine source-supported oddities such as `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `உலகந்தான்`, `தன்னுலே`, or `உலகியலேக் காண` unless the scan itself proves otherwise.

## Exact next activity

Continue **T3 canonical consolidation with the final PDF 76-81 / printed 75-80 segment**:

1. take PDF 76-81 from `t1-batches/batch-12-pdf-71-81.md`;
2. apply every scan-proven correction from T2 Batches 15-16 and the traditional-glyph rule;
3. honor the recorded PDF 75→76 ordinary continuation `அத்துடன்` / `படிக்கிறான்.` without inventing a word join;
4. preserve source-supported oddities exactly;
5. run a segment stale-reading check, then the **whole-body T3 gate** across PDF 6-81;
6. verify exactly one heading for every PDF page 6-81, the correct printed-page mapping 5-80, the verified beginning, all recorded boundary decisions, and the verified final closing;
7. only after that passes, mark Tamil `verified-complete` / frozen and update the repository status files accordingly.

Do not begin English translation until Tamil is frozen.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- T3 is consolidation and verification, not language editing.
- Do not modernize, normalize, reconstruct or improve source wording.
- Preserve source-supported spelling, punctuation, names, numbers, repetition and unusual grammar.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until T3 passes.