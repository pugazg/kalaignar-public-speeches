# NEXT CHAT PROMPT — முத்துக்குளியல் பாகம் I / incremental closure after split 003

Continue directly in `pugazg/kalaignar-public-speeches`, branch `main`, active collection `collections/muthukkuliyal-part-1/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

## Revised workflow policy — authoritative

Do **not** wait for all 39 split PDFs before transcription.

Each supplied split must be processed to the **maximum durable state supported by the pages currently available**.

For each fully bounded constituent:
**source gate → Tamil T1 → Tamil T2 → Tamil T3 / freeze → English E1 → E2 → E3 → repository closure**.

For a constituent crossing a split boundary:
- process all currently available pages immediately;
- create a durable page-level checkpoint;
- do not invent missing pages or claim full constituent closure;
- when the next split arrives, continue only the missing tail / boundary / final closure work;
- do not re-open already verified pages unless a new source-fidelity issue appears.

## Current source state

- original PDF: **641 pages**, user-confirmed;
- split count: **39**;
- received: **3/39**;
- continuous scan coverage: **1–49 / 641**;
- contents: **61/61 complete**;
- source/body mapping: **PDF = printed + 1** confirmed through scan 49;
- source-gated constituents: **1–3**.

### Constituent 1 — `வள்ளுவர் வழி எது?`
- PDF **18–28** / printed **17–27** — **11/11 source-gated**;
- ready for **T1 → repository closure**.

### Constituent 2 — `வள்ளுவர்க்கோர் ஆலயம்`
- PDF **29–32** / printed **28–31** — **4/4 source-gated**;
- ready for **T1 → repository closure**.

### Constituent 3 — `கம்பர் விழா (1)`
- PDF **33–41** / printed **32–40** — **9/9 source-gated**;
- ready for **T1 → repository closure**.

### Constituent 4 — `கம்பர் விழா (2)`
- provisional full range: PDF **42–56** / printed **41–55**;
- currently supplied: PDF **42–49** / printed **41–48** — **8 pages**;
- process these supplied pages now to a durable page-level checkpoint;
- final constituent freeze / English final verification / repository closure must wait for PDF **50–56**.

## Exact next activity

1. Process constituents **1–3 from Tamil T1 through repository closure** using only the supplied scan pixels.
2. Then process constituent 4 PDF **42–49** to the highest safe durable page-level checkpoint.
3. Update constituent and collection README / metadata / audit / HANDOVER / page-map.
4. Preserve source binaries as uncommitted.

No OCR, no web, no alternate source.
