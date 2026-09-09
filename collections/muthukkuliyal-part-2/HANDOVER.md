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
- constituent archives started: **1 / 36**
- constituent Tamil T1 first passes complete: **1 / 36**
- constituent Tamil T2 audits complete: **1 / 36**
- constituent Tamil T3 freezes complete: **1 / 36**
- constituent Tamil layers verified complete: **1 / 36**
- constituent English E1 first passes complete: **1 / 36**
- constituent English E2 reviews complete: **0 / 36**
- constituent English E3 final verifications complete: **0 / 36**
- constituent archives fully completed from this volume: **0 / 36**

The stable body relationship is `PDF scan = printed page + 1` for PDF 12–424 / printed 11–423. Full details are in `page-map.md`.

## Active constituent 1 / 36

**`தேசிய இளைஞர் கொண்டாட்டத் தொடக்கவிழா`**  
Speech tree: `speeches/desiya-ilainjar-kondatta-thodakka-vizha/`  
Contents date: **12-01-98**  
Printed pages: **11–17**  
PDF scans: **12–18**  
Mapped body pages: **7**

Durable constituent state:

- duplicate search: **PASS — no existing matching speech tree**;
- source intake / boundaries: **PASS / COMPLETE**;
- closing note directly establishes **12-1-98**, **சென்னை ஜவகர்லால் நேரு விளையாட்டரங்கம்**, and **தலைமை உரை**;
- Tamil T1: **COMPLETE — 7 / 7 pages**;
- Tamil T2: **PASS / COMPLETE — 7 / 7 pages; 5 substantive corrections; 0 unresolved**;
- Tamil T3: **PASS / COMPLETE**;
- Tamil status: **`verified-complete`**;
- English E1: **COMPLETE — 7 / 7 pages**;
- English E2: **READY / NOT STARTED — 0 / 7**;
- English E3: **BLOCKED / NOT STARTED**.

Important Tamil T2 resolutions are retained in the speech-level `audit.md`; notably `இந்தியர்களிடையே` and `சமாதானத்திற்கும்` were recovered from printer line-wraps, while unusual `ஐக்கிய இந்தியர் மீது` was confirmed as printed.

The E1 translation was produced only from frozen `transcription-ta.md`. The unusual p.13 source form `ஐக்கிய இந்தியர் மீது` is explicitly surfaced in an English source note for independent E2 review rather than being silently used to alter the Tamil layer.

## Important cautions

- Do **not** treat the 425-page volume as one speech.
- Do **not** create a single `speeches/muthukkuliyal-part-2/` transcript.
- Do **not** start constituent 2 while constituent 1 remains in its active archival sequence unless separately authorized.
- Contents dates are source evidence as printed. Do not reorder the collection by date.
- Entries 7 and 16 have no date in the contents; leave their dates unresolved until their own pages establish one.
- Do not copy the June 2000 publication date into speech-event dates.
- Do not commit the PDF binary.

## Exact next incomplete gate

Continue constituent **1 / 36** with **English E2 independent Tamil→English fidelity review** across PDF **12–18** / printed **11–17**. Compare the complete E1 against frozen Tamil, record every omission/addition/reversal/source-transparency finding, consolidate confirmed English corrections, and leave E3 blocked until that review is fully resolved.
