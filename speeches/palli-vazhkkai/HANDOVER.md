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

### T2 — IN PROGRESS: 20/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24

Detailed records:
- `t2-batches/batch-01-pdf-06-10.md`
- `t2-batches/batch-02-pdf-11-15.md`
- `t2-batches/batch-03-pdf-16-20.md`
- `t2-batches/batch-04-pdf-21-25.md`

### Important Batch 4 resolutions

Confirmed corrections:
- PDF 22 / printed 21: `இடம் கிடைத்து` → `இடம் உடைத்து`
- PDF 23 / printed 22: `மண்ணாவது` → `மண்ணுவது`

Confirmed source forms that must be preserved:
- `திடசித்தமுடையவனுக`
- `பலமுறைகள்`
- `நல்லதங்கள்`
- `நாவினை நாட்டினரும்`
- `இடம் உடைத்து`

Page-boundary resolution:
- PDF 23→24 `உள்ள` / `படி` is confirmed as the one-word join `உள்ளபடி`.

Verified corrections remain staged in `t2-batches/` and are mandatory inputs to T3. Do not reintroduce superseded T1 readings or normalize the source-supported odd forms.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 26-30 / printed pages 25-29**.

Compare every line and punctuation mark against the scan, verify unusual forms only from the printed page, and record only source-proven corrections. Do not modernize or reconstruct.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not modern-language proofreading.
- Do not infer event metadata from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
