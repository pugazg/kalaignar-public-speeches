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

### T2 — IN PROGRESS: 15/76
Completed strict visual audit:
- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19

Detailed records:
- `t2-batches/batch-01-pdf-06-10.md`
- `t2-batches/batch-02-pdf-11-15.md`
- `t2-batches/batch-03-pdf-16-20.md`

### Important Batch 3 resolutions

Confirmed correction:
- `வரவிட` → `வரைவிட` on PDF 17 / printed 16.

Confirmed source form:
- `கல்வி கற்கு மிடம்` on printed p.18 — preserve exactly; do not normalize.

Confirmed page-boundary / line-wrap joins:
- PDF 18→19: `கஞ்சிக்` / `காவது` → `கஞ்சிக்காவது`
- PDF 19→20: `எட்டுச்` / `சுரையெனப்` → `எட்டுச்சுரையெனப்`
- printed p.19 internal wrap `தன்னம்` / `பிக்கையும்` → `தன்னம்பிக்கையும்`

Verified corrections remain in the T2 batch layer and are mandatory inputs to T3 canonical consolidation. Do not reintroduce superseded T1 readings.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started and remains blocked until T2 and T3 pass.

## Exact next activity

Perform strict T2 visual audit of **PDF pages 21-25 / printed pages 20-24**.

Specifically:
- compare every line and punctuation mark against the scan;
- resolve PDF 23→24 `உள்ள` / `படி` from both images;
- inspect `திடசித்தமுடையவனுக`, `பலமுறைகள்`, `மனிதனுக`, `நல்லதங்கள்`, and `நாவினை நாட்டினரும்` as source readings rather than assuming corrections;
- record only scan-proven changes.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not modern-language proofreading.
- Do not infer or reconstruct source text.
- Do not commit the source PDF.
- Do not begin English translation until all 76 pages pass T2 and Tamil passes T3.
