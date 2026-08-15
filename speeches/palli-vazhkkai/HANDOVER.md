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
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34
- Batch 7: PDF 36-40 / printed 35-39

Detailed records are under `t2-batches/`, including `batch-07-pdf-36-40.md`.

### Important Batch 7 resolutions

Confirmed corrections:
- PDF 36 / printed 35: `தாங்கள்தான்` → `தாங்கள் தான்`
- PDF 36 / printed 35: `நானா?` → `நானு?`
- PDF 37 / printed 36: `ஏகலவனின் மறுபடி` → `ஏகலவனை மறுபடி`
- PDF 38 / printed 37: `பகுதிக்கு` → `பக்திக்கு`
- PDF 40 / printed 39: `சிரச் சினந்து` → `சீறிச் சினந்து`

Confirmed source forms that must be preserved include:
- `நானு?`
- `நாயகனுக்கிக்கொண்ட`
- `சந்திரனச் சல்லாபத்திற்`
- `கடிக்குலவின`
- `மாணுக்கர்களுக்கு`
- `பூலோக வாசிகளேப்`
- `திடமென்று`
- `இறும்பூதெய்தி`
- `என்ன கொடுமதி உமக்கு`
- `சீறிச் சினந்து`

Page-boundary decisions:
- PDF 37→38 `வலதுகைப்` / `பெருவிரல்` is phrase continuation: `வலதுகைப் பெருவிரல்`; retain the page boundary and the space between words.
- PDF 38→39 `சாபந் தந்த` / `பிரகஸ்பதி பகவான்களும்` is ordinary sentence continuation, not a split word.
- PDF 40→41 `தேடு` / `கிறீர்;` is a genuine split word → `தேடுகிறீர்;`. PDF 41 was inspected only as a boundary witness; it has **not** yet received its full T2 audit and does not count in the 35 pages completed.

Verified corrections remain staged in `t2-batches/` and are mandatory inputs to T3. Do not reintroduce superseded T1 readings or normalize source-supported forms.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 41-45 / printed pages 40-44**.

Specifically:
- re-audit PDF 41 fully from its first line despite the boundary-only check already made;
- resolve PDF 41→42 `சுயமரியாதை` / `பற்ற செயல்` from both page images without normalizing the source;
- resolve PDF 42→43 `உமக்குப்` / `பெருமை தந்திடத்தான்`;
- resolve PDF 44→45 `ஊட்` / `டிடும்`;
- inspect PDF 46 only if needed as a boundary witness for PDF 45, and do not count PDF 46 audited until its own batch;
- record only scan-proven changes.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct source text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
