# பள்ளி வாழ்க்கை — T1 handover

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

## Current workflow state

### T1 Tamil first pass
All **76/76 speech-body pages now have a first-pass T1 reading available in the repository**.

Canonical `transcription-ta.md` remains safely preserved through PDF 45 / printed 44 (40/76). The remaining 36 pages are staged in contiguous source-controlled batches pending one careful canonical consolidation:

- Batch 9: `t1-batches/batch-09-pdf-46-50.md` — PDF 46-50 / printed 45-49
- Batch 10: `t1-batches/batch-10-pdf-51-60.md` — PDF 51-60 / printed 50-59
- Batch 11: `t1-batches/batch-11-pdf-61-70.md` — PDF 61-70 / printed 60-69
- Batch 12: `t1-batches/batch-12-pdf-71-81.md` — PDF 71-81 / printed 70-80

The supplied scan was visually inspected across the remaining pages. The final body page is PDF 81 / printed 80 and ends `பள்ளி வாழ்க்கையில்! வணக்கம் !!`.

These staged files are **T1 only**. They are not T2-verified and must not be silently normalized. Any doubtful/unusual historical forms must be resolved only during the independent strict visual audit.

### T2 / T3
- T2 strict visual line-by-line audit: **not started — 0/76**.
- T3 consolidation/freeze: not started.
- Tamil is not yet `verified-complete`.

### English
- E1 translation: not started.
- E2 review: not started.
- E3 final verification: not started.
- English remains blocked until Tamil passes T2 and T3.

## Exact next activity

1. Consolidate staged Batches 9-12 into `transcription-ta.md` without altering the canonical PDF 6-45 text.
2. Synchronize `metadata.json`, speech `README.md`, and `audit.md` to T1 **76/76 complete**.
3. Remove the temporary `t1-batches/` staging files only after confirming the canonical transcription is continuous PDF 6-81 / printed 5-80.
4. Then begin **T2 strict visual fidelity audit at PDF page 6 / printed page 5**, page-by-page against the scan.

## Safeguards
- Scan is authoritative; OCR is never authoritative.
- Preserve historical spelling, punctuation, wording, numbers, repetition and typographical forms unless the scan itself proves otherwise.
- Do not infer speech date/venue/event from publication data or outside knowledge.
- Do not commit the source PDF.
- Do not begin English translation until T2 and T3 pass.