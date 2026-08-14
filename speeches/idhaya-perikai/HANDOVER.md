# இதய பேரிகை — startup handover

This document records the exact state after the mandatory startup/source-inspection gate. It is intended to let another chat continue from the next incomplete stage without repeating completed work or jumping ahead to translation.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Target directory: `speeches/idhaya-perikai/`
- Proposed/stable slug: `idhaya-perikai`

## Mandatory startup completed

- `SPEECH_PROCESSING_GUIDE.md` read completely before work.
- Root `README.md` read.
- Completed `speeches/arappor/` implementation studied for workflow/file structure, including its README, metadata, Tamil audit, English translation review, and final HANDOVER.
- Repository inspected before creation. At startup `speeches/` contained only `arappor/`; repository searches for `இதய பேரிகை`, `idhaya perikai`, and `idhaya-perikai` found no existing target work.
- The actual attached scan, not merely its filename, was inspected across all 36 PDF pages before metadata/page mapping was created.

## Source identity

- Source filename: `TVA_BOK_0016120_இதய_பேரிகை(1).pdf`
- SHA-256: `4217717379b028de17ed9830dac4bdfd54ae7256705b891c207d646707640b9d`
- File size: `21,135,384` bytes
- Actual PDF page count: `36`
- Source binary committed to GitHub: **No — by repository policy**

## Bibliographic evidence established from the scan

- Title: `இதய பேரிகை.`
- Author: `மு. கருணாநிதி.`
- Edition statement: `முதற்பதிப்பு—டிசம்பர் 1951`
- Publisher: `கலைப்பூங்கா, திருவாரூர்.`
- Rights line: `"கலைப்பூங்கா" உரிமை பெற்றது.`
- Printed price: `விலை அணா எட்டு.`
- Printer: unresolved in full because a later library stamp crosses the printer line on PDF page 3. Do not reconstruct the obscured wording without source evidence.

The title page does not explicitly identify the item as `பேச்சு`. The source is a seven-section printed booklet being archived as one unit in the public-speeches project. The scan does not establish one speech date, venue, event, occasion, or audience as bibliographic metadata; those fields remain unset.

## Page map

- PDF 1 — front cover
- PDF 2 — title page
- PDF 3 — imprint/rights/price/printer information plus `என் நினைவு!` front matter
- PDF 4–11 / printed 3–10 — `சிறு துளி பெரு வெள்ளம்.`
- PDF 12–16 / printed 11–15 — `வீதிதேவர் மயக்கம்.`
- PDF 17–20 / printed 16–19 — `பூம்புகார் மாநாடு.`
- PDF 21–23 / printed 20–22 — `வெற்றி விளக்கு!`
- PDF 24–29 / printed 23–28 — `நமது உரிமை.`
- PDF 30–32 / printed 29–31 — `பந்தல் ஆடுகிறது!`
- PDF 33–35 / printed 32–34 — `கருகிடும் மொட்டுக்கள்!`
- PDF 35 lower portion — publisher advertisement beginning `பூங்காவின் அடுத்த மலர்!`; exclude from body transcription
- PDF 36 — back cover

Body page count for workflow tracking: **32 / 32 pages mapped; 0 / 32 transcribed**.

## Current workflow state

| Gate | State |
|---|---|
| 1. Source inspection / bibliographic-page map | **complete** |
| 2. Tamil first-pass transcription (T1) | **not-started — 0/32** |
| 3. Strict visual Tamil fidelity audit (T2) | **not-started — 0/32** |
| 4. Tamil consolidation / freeze (T3) | **not-started** |
| 5. English first-pass translation (E1) | **not-started / locked** |
| 6. English fidelity review (E2) | **not-started / locked** |
| 7. Final Tamil→English verification (E3) | **not-started / locked** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete gate

Proceed with **Stage T1 — first-pass Tamil transcription of the complete body**, starting at **PDF page 4 / printed page 3** and continuing through the body portion of **PDF page 35 / printed page 34**.

Requirements for the next chat/batch:

- transcribe from the scan, using OCR only as an aid;
- keep PDF/printed page boundaries explicit;
- preserve the seven section headings and source-supported historical forms;
- do not silently modernize or correct the Tamil;
- treat stamps/handwriting/accession marks as later annotations, not printed text;
- on PDF page 35 stop the body at the ornament and do not transcribe the publisher advertisement as speech/body text;
- do **not** begin Stage T2 until the entire body first pass exists;
- do **not** begin any English translation until T2 and T3 pass and the Tamil layer is frozen as `verified-complete`.

## Root catalogue

The root catalogue has **not** been updated at this startup stage. Per `SPEECH_PROCESSING_GUIDE.md`, repository-level catalogue synchronization belongs to final archival closure after the textual gates pass.
