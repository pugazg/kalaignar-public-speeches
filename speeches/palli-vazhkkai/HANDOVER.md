# பள்ளி வாழ்க்கை — startup handover

This document records the exact state after the mandatory source-inspection startup gate. It exists so the next chat or work session continues from the next incomplete gate rather than repeating completed startup work.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/palli-vazhkkai/`

## Source

- Canonical source filename: `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`
- SHA-256: `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`
- File size: `101,096,930` bytes
- Actual PDF page count: `81`
- Source PDF committed to repository: **No - repository policy is to preserve source identity through provenance metadata, not commit the source binary**

## Completed startup gate

The mandatory startup/source-inspection work is complete:

- `SPEECH_PROCESSING_GUIDE.md` read completely;
- root `README.md` read;
- completed `speeches/arappor/` reference implementation studied, including its README, metadata, Tamil audit, English fidelity review, and handover;
- repository inspected for an existing `பள்ளி வாழ்க்கை` / likely-slug work item; no existing target directory or matching archive entry was found;
- all 81 scan pages were inspected for document structure and page mapping;
- bibliographic evidence was taken from the scan itself rather than the filename;
- source checksum, file size, PDF page count, and page map were established;
- the initial standard archival files were created without beginning bulk transcription.

## Source-established bibliographic facts

- Title: `பள்ளி வாழ்க்கை`
- Creator line: `கலைஞர் : மு. கருணாநிதி`
- Publisher: `அறிவு மன்றம்`
- Publication place: `சென்னை.`
- Edition statement: `முதற்பதிப்பு மார்ச்சு 1952`
- Price: `விலை ரூ. 1-0-0`
- Printer: `Vinodan Press, 33, Jones St. G. T. Madras.`

PDF page 5 states that speeches delivered by Karunanidhi at `திருவாரூர் நகராண்மைக் கழக உயர்நிலைப்பள்ளி` and `வேறு சில இடங்களிலும்` were collected by `தோழர் மு. நமச்சிவாயம்`, resulting in `பள்ளி வாழ்க்கை`.

This is therefore treated as a **printed speech-compilation booklet** archived as one source unit. Do not invent one speech date, venue, event, occasion, or audience for the compilation.

## Page map

- PDF 1 - later donor/provenance gift label on an otherwise blank leaf; not edition/body text
- PDF 2 - title page
- PDF 3 - copyright / first-edition / price / printer imprint
- PDF 4 - publisher/editorial foreword signed `அறிவு மன்றத்தார்.`
- PDF 5 - compilation/source note
- PDF 6-81 - main body, printed pages 5-80 (**76 pages**)

PDF page 81 / printed page 80 contains the end of the text. No separate advertisements/back matter follow the body.

## Workflow state

### Source inspection

- Status: **complete**

### Tamil

- T1 first-pass transcription: **not started - 0/76 pages**
- T2 strict visual audit: **not started**
- T3 consolidation/freeze: **not started**
- Tamil status: **`not-started`**

### English

- E1 translation: **not started**
- E2 fidelity review: **not started**
- E3 final end-to-end verification: **not started**
- English status: **`not-started`**

## Exact next incomplete gate

**Stage T1 - first-pass Tamil transcription.**

Begin at **PDF page 6 / printed page 5** and proceed through **PDF page 81 / printed page 80**, retaining explicit PDF/printed-page headings. Work in manageable page batches and preserve the source exactly as printed; do not modernize, correct, or reconstruct unusual forms.

Do **not** begin T2 strict audit until a first-pass transcription exists for all 76 body pages. Do **not** begin English translation until T2 and T3 have passed and Tamil is frozen as `verified-complete`.

## Continuation safeguards

- The scan is authoritative; OCR/parsed text is only an aid.
- Distinguish print from later donor/library marks, handwriting, damage, and bleed-through.
- Do not infer component-speech dates or event metadata from the March 1952 publication date or outside history.
- Do not upload or commit the source PDF.
- Record substantive source-fidelity decisions in `audit.md` during T2.
- Keep this handover synchronized at meaningful checkpoints so continuation never restarts completed work.
