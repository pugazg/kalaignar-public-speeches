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

- **PDF 6-60 / printed 5-59 — T3 consolidated into the canonical file**
- PDF 61-70 / printed 60-69 — still staged in `t1-batches/batch-11-pdf-61-70.md`
- PDF 71-81 / printed 70-80 — still staged in `t1-batches/batch-12-pdf-71-81.md`

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

The stale-reading validation passed for the consolidated PDF 46-60 segment. Source-supported unusual forms were deliberately retained, including `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, `மதனின் அறிவு வளர்ச்சி பெற்று`, and `இராஜ இராஜேந்திரனின்`.

## Mandatory traditional-glyph rule

The 1952 printing uses traditional Tamil glyphs. Encode the underlying Tamil characters, not visually similar modern Unicode syllables. Do not resurrect superseded readings such as `கவலிப்பட`, `நன்றுக`, `தமிழனுக`, `மனிதனுக`, `தேவைத்தானு`, `தோழனுக`, `அவனுகத்தான்`, or `தேவனே` where the scan proves `கவலைப்பட`, `நன்றாக`, `தமிழனாக`, `மனிதனாக`, `தேவைத்தானா`, `தோழனாக`, `அவனாகத்தான்`, or `தேவனை`.

At the same time, do not regularize genuine source-supported oddities such as `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `உலகந்தான்`, `தன்னுலே`, or `உலகியலேக் காண` unless the scan itself proves otherwise.

## Exact next activity

Continue **T3 canonical consolidation with PDF 61-75 / printed 60-74**:

1. merge PDF 61-70 from `t1-batches/batch-11-pdf-61-70.md` and PDF 71-75 from `t1-batches/batch-12-pdf-71-81.md` into `transcription-ta.md`;
2. apply every scan-proven correction from T2 Batches 12-14 and the traditional-glyph rule;
3. preserve verified source oddities rather than normalizing them;
4. reconstruct only page/printer splits established by the T2 records;
5. run a stale-reading sweep on PDF 61-75 before proceeding to the final PDF 76-81 segment.

Only after all PDF 6-81 pages are in one continuous canonical file, every T2 correction is applied, stale readings are absent, source-supported oddities are retained, and page continuity is checked may Tamil be marked `verified-complete` / frozen.

## Safeguards
- Scan is authoritative; OCR and T1 are only aids.
- T3 is consolidation and verification, not language editing.
- Do not modernize, normalize, reconstruct or improve source wording.
- Preserve source-supported spelling, punctuation, names, numbers, repetition and unusual grammar.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until T3 passes.