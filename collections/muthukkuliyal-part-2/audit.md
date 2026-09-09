# Audit — முத்துக்குளியல் — பாகம் II

Collection-level source inspection and mapping audit.

## Source identity

- Source: `TVA_BOK_0065802_முத்துக்குளியல்_பாகம்_2.pdf`
- SHA-256: `48631b4fc5258df33213dbb742aec70ff6aace4fcd294f377e5750b406f5d9b2`
- Byte size: `232,470,104`
- Actual PDF page count: **425**

The page count was taken from the complete local PDF binary. A truncated rendering surface exposed only 150 pages earlier; that was not the complete-file page count and is superseded by the direct binary result.

## Directly inspected source regions

- PDF 1–5: cover/title/imprint sequence
- PDF 6–9: front matter (`முன்னுரை`, `பதிப்புரை`, including blank/show-through verso)
- PDF 10–11: complete contents
- PDF 12: first constituent opening / printed p.11
- PDF 424: final constituent closing / printed p.423
- PDF 425: true final page / back cover

## Source classification

The imprint describes the work as **`சொற்பொழிவுகளின் தொகுப்பு`** and the contents contain **36 separately titled items**. Therefore the volume is classified as a **multi-speech collection**, not one speech.

## Mapping verification

The constituent body begins at PDF 12 / printed 11 and ends at PDF 424 / printed 423, establishing a stable offset of `PDF = printed + 1` across the body.

All 36 contents start pages were captured. Each end page was mapped to one page before the next contents start; item 36 ends at the directly inspected final body page, printed 423 / PDF 424.

Result:

- contents capture: **36 / 36 PASS**
- printed-page ranges: **36 / 36 mapped**
- PDF scan ranges: **36 / 36 mapped**
- front/back-matter boundary: **PASS**
- collection source intake: **COMPLETE**

## Source-fidelity cautions

- The contents order is preserved exactly; entries are not reordered chronologically.
- Entries 7 and 16 do not show dates in the contents and remain unresolved at collection level.
- Publication and embedded PDF metadata are kept distinct from speech/event facts.
- No OCR, outside edition or catalogue text was used to override the scanned contents.
- The PDF binary is not committed.

## Next gate

Constituent 1, `தேசிய இளைஞர் கொண்டாட்டத் தொடக்கவிழா`, PDF 12–18 / printed 11–17: repository duplicate check, constituent source intake, then Tamil T1.
