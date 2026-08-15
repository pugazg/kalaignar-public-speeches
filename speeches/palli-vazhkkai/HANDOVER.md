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

### T2 — IN PROGRESS: 25/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24
- Batch 5: PDF 26-30 / printed 25-29

Detailed records are under `t2-batches/`, including `batch-05-pdf-26-30.md`.

### Important Batch 5 resolutions

Confirmed corrections:
- PDF 29 / printed 28: `இத்தை வெறுத்து` → `இகத்தை வெறுத்து`
- PDF 29 / printed 28: `தன்னேப்பற்றிக் கவலிப்பட` → `தன்னைப்பற்றிக் கவலிப்பட`

Confirmed source forms that must be preserved:
- `தமிழனுக`
- `முன்னேற்றம் மடைகின்றன`
- `வளர்த்தை`
- `வளர்த்தைப்`
- `வகைப்படுத்தியாக`

Verified corrections remain staged in `t2-batches/` and are mandatory inputs to T3. Do not reintroduce superseded T1 readings or normalize the source-supported odd forms.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 31-35 / printed pages 30-34**.

Specifically:
- compare every line and punctuation mark against the scan;
- resolve PDF 31→32 `தமிழினத்` / `தைப்` from both page images;
- resolve PDF 32→33 `பசுமரத்` / `தாணிபோலப்` from both page images;
- inspect unusual T1 forms only from the printed source;
- record only scan-proven changes.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct source text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
