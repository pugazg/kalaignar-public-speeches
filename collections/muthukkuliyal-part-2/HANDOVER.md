# HANDOVER — முத்துக்குளியல் — பாகம் II

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Collection directory: `collections/muthukkuliyal-part-2/`

## Controlling source

- Filename: `TVA_BOK_0065802_முத்துக்குளியல்_பாகம்_2.pdf`
- SHA-256: `48631b4fc5258df33213dbb742aec70ff6aace4fcd294f377e5750b406f5d9b2`
- Byte size: `232,470,104`
- Actual PDF scans from the complete binary: **425**
- Source binary committed: **No**
- Source classification: **multi-speech collection / `சொற்பொழிவுகளின் தொகுப்பு`**

The earlier 150-page figure came from an incomplete/truncated file-rendering view and is **not** the source page count. Direct inspection of the complete PDF binary establishes **425 pages**.

## Edition/source inspection

Directly inspected:

- cover and title pages;
- imprint;
- `முன்னுரை` / `பதிப்புரை` front matter;
- contents scans 10–11;
- first constituent opening at PDF 12 / printed 11;
- final constituent ending at PDF 424 / printed 423;
- true final PDF page 425, which is the back cover.

Edition facts and embedded PDF metadata are recorded separately in `metadata.json` so the 2024 PDF timestamps are not confused with the June 2000 publication.

## Mapping state

- contents entries captured: **36 / 36 — COMPLETE**
- constituent printed-page ranges mapped: **36 / 36 — COMPLETE**
- constituent PDF scan ranges mapped: **36 / 36 — COMPLETE**
- parent collection source intake: **PASS / COMPLETE**
- constituent archives completed from this volume: **0 / 36**

The stable body relationship is `PDF scan = printed page + 1` for PDF 12–424 / printed 11–423. Full details are in `page-map.md`.

## Important cautions

- Do **not** treat the 425-page volume as one speech.
- Do **not** create a single `speeches/muthukkuliyal-part-2/` transcript.
- Each constituent item must be checked for an existing archive before creating a new `speeches/<slug>/` tree.
- Contents dates are source evidence as printed. Do not reorder the collection by date.
- Entries 7 and 16 have no date in the contents; leave their dates unresolved until their own pages establish one.
- Do not copy the June 2000 publication date into speech-event dates.
- Do not commit the PDF binary.

## Exact next incomplete gate

Start/continue constituent **1 / 36**:

**`தேசிய இளைஞர் கொண்டாட்டத் தொடக்கவிழா`**  
Contents date: **12-01-98**  
Printed pages: **11–17**  
PDF scans: **12–18**  
Mapped body pages: **7**

Before creating a speech tree, search live `main` for the title, likely slug, event wording, parent source filename and equivalent records. If no existing archive is found, create the constituent speech directory with parent-collection provenance and begin Tamil T1 from PDF 12–18. English remains blocked until Tamil T3 passes.
