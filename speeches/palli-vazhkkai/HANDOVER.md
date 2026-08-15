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

## Current workflow state

### T1 Tamil first pass — COMPLETE
All **76/76 speech-body pages** have T1 first-pass readings.

Storage is deliberately non-destructive until T2/T3:
- `transcription-ta.md`: PDF 6-45 / printed 5-44
- `t1-batches/batch-09-pdf-46-50.md`: PDF 46-50 / printed 45-49
- `t1-batches/batch-10-pdf-51-60.md`: PDF 51-60 / printed 50-59
- `t1-batches/batch-11-pdf-61-70.md`: PDF 61-70 / printed 60-69
- `t1-batches/batch-12-pdf-71-81.md`: PDF 71-81 / printed 70-80

The final body page is PDF 81 / printed 80 and the T1 reading ends `பள்ளி வாழ்க்கையில்! வணக்கம் !!`.

The segmented T1 files are intentionally retained instead of performing a large destructive rewrite before visual verification. They must be merged into one final canonical Tamil file during T3 after T2 has resolved page-boundary and source-oddity readings.

### T2 — ACTIVE NEXT GATE
- Strict visual line-by-line audit: **0/76**.
- Start at PDF page **6 / printed page 5**.
- The supplied scan is the controlling source.
- T1 text is provisional and is not evidence against the scan.

### T3
- Canonical consolidation/freeze: not started.
- Tamil is not `verified-complete`.

### English
- E1 translation: not started.
- E2 fidelity review: not started.
- E3 final verification: not started.
- English remains blocked until T2 and T3 pass.

## Exact next activity

Perform the first manageable **T2 strict visual audit batch beginning PDF 6 / printed 5**. Compare every printed line and punctuation mark against the scan, preserve source-supported historical/odd forms, record corrections in `audit.md`, and update the relevant Tamil text only where the scan proves a correction.

Continue T2 sequentially until PDF 81 / printed 80. Then perform T3: resolve all queued page-boundary joins/stale readings, merge the segmented T1/T2 material into one continuous canonical `transcription-ta.md`, remove temporary staging files, and freeze Tamil only after end-to-end verification.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- Do not silently modernize, normalize, correct or reconstruct source wording.
- Preserve source-supported spelling, punctuation, names, numbers, repetition, unusual grammar and typographical forms.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until T2 and T3 pass.
