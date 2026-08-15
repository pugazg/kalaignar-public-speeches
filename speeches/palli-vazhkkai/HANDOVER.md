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

### T2 — IN PROGRESS: 30/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29
- Batch 6: PDF 31-35 / printed 30-34

Detailed records are under `t2-batches/`, including `batch-06-pdf-31-35.md`.

### Important Batch 6 resolutions

Confirmed corrections:
- PDF 34 / printed 33: `தனது வில்லெடுத்து,` → `தனது வில்லைபூட்டி,`
- PDF 35 / printed 34: `குறித்துவிட்டோடும்` → `குருதிவடிந்தோடும்`

Confirmed source forms that must be preserved:
- `போற்றிவேண்டும்`
- `தேவைத்தானு`
- `அரிபந்தாமன்`
- `வில்லைபூட்டி`
- `காண்டவன்`

Confirmed page-boundary joins:
- PDF 31→32: `தமிழினத்` / `தைப்` → `தமிழினத்தைப்`
- PDF 32→33: `பசுமரத்` / `தாணிபோலப்` → `பசுமரத்தாணிபோலப்`

Verified corrections remain staged in `t2-batches/` and are mandatory inputs to T3. Do not reintroduce superseded T1 readings or normalize the source-supported forms.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 36-40 / printed pages 35-39**.

Specifically:
- compare every line and punctuation mark against the scan;
- resolve PDF 37→38 `வலதுகைப்` / `பெருவிரல்` from both page images;
- inspect PDF 38→39 `சாபந் தந்த` / `பிரகஸ்பதி பகவான்களும்` without assuming whether it is a split word or sentence continuation;
- preserve the exact unfinished ending of PDF 40 and verify its continuation only from PDF 41 in the following audit batch;
- record only scan-proven changes.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct source text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
