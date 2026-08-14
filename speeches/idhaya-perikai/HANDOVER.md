# இதய பேரிகை — working handover

This document records the exact state after **Stage T2 strict visual Tamil fidelity audit completion**. Continue from Stage T3 without repeating startup, T1, or the completed page-by-page T2 audit, and do not begin English early.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Directory: `speeches/idhaya-perikai/`
- Slug: `idhaya-perikai`

## Source identity

- Source filename: `TVA_BOK_0016120_இதய_பேரிகை(1).pdf`
- SHA-256: `4217717379b028de17ed9830dac4bdfd54ae7256705b891c207d646707640b9d`
- File size: `21,135,384` bytes
- PDF page count: `36`
- Source binary committed to GitHub: **No — repository policy**

The scan does not establish a single speech date, venue, event, occasion, or audience. Do not infer those fields from internal dates/events or outside knowledge.

## Page map

- PDF 4–11 / printed 3–10 — `சிறு துளி பெரு வெள்ளம்.`
- PDF 12–16 / printed 11–15 — `வீதிதேவர் மயக்கம்.`
- PDF 17–20 / printed 16–19 — `பூம்புகார் மாநாடு.`
- PDF 21–23 / printed 20–22 — `வெற்றி விளக்கு!`
- PDF 24–29 / printed 23–28 — `நமது உரிமை.`
- PDF 30–32 / printed 29–31 — `பந்தல் ஆடுகிறது!`
- PDF 33–35 / printed 32–34 — `கருகிடும் மொட்டுக்கள்!`
- PDF 35 lower portion — publisher advertisement; exclude from body transcription

## Completed work

Gate 1 source inspection/bibliographic mapping is **complete**.

Stage T1 first-pass Tamil transcription is **complete — 32/32 body pages drafted**.

Stage T2 strict visual Tamil fidelity audit is **complete — 32/32 body pages checked and corrections consolidated**:

- T2 Batch 1: PDF 4–8 / printed 3–7
- T2 Batch 2: PDF 9–13 / printed 8–12
- T2 Batch 3: PDF 14–18 / printed 13–17
- T2 Batch 4: PDF 19–23 / printed 18–22
- Final remaining-pages sweep: PDF 24–35 / printed 23–34

The strict visual audit therefore covers the **entire body through PDF 35 / printed 34**. No T2 page remains unaudited, and no `⟦...?⟧` unresolved T2 marker remains in the canonical transcript.

The Tamil layer is nevertheless **not yet `verified-complete`** because Stage T3 consolidation, stale-reading/page-boundary review and freeze have not begun.

## Final remaining-pages audit findings — PDF 24–35

- PDF 24→25: `விஷ` / `யத்தில்` page-spanning word confirmed.
- PDF 25→26: `“மோர்` / `தாப்படவில்லை”` confirmed; unusual `தாப்படவில்லை` retained.
- PDF 26: later handwritten/accession `68206` excluded; source quotation punctuation restored as `“விடாதே பறிமுதல்!”`.
- PDF 27: unresolved `⟦நெசவாளர்களார்ச்சியை?⟧` resolved from the scan as **`நெசவாளர்கிளர்ச்சியை`**; `போலீஸ்காரணங்களை` confirmed.
- PDF 28: `முச்ச விடக்` → **`மூச்சு விடக்`**; PDF 28→29 `கூட்ட` / `மல்ல!` confirmed.
- PDF 29: `வரவேற்போம் என்று வைர...` → **`வரவேற்போம் என்ற வைர...`**.
- PDF 30: `துண்களாக` → **`தூண்களாக`**; `முடிகூடா` → **`முடிசூடா`**; `படையிலே காட்டினார்` → **`படையலைக் காட்டினார்`**; `படப்படவென` → **`படபடவென`**; `நரம்புகளைக் கீற்றுகளாக முடைந்து போட்டு` confirmed; PDF 30→31 `குழந்தை` / `கள்.` confirmed.
- PDF 31: source comma in `ஜீவன்கள், “இறப்புலகில்...` restored; `சுமன்றன கேள்விகள்` and `சூறவளிக் காற்று` confirmed; page ends `ஓமாந்தூரார்—` with no invented bridge.
- PDF 32: opening corrected to **`காணவில்லை தொண்டாற்றும் இந்தத் தூண்கள்!`**; comma after `வெளியேறிவிட்டனர்` restored; `சொல்லுவார்` → **`சொல்வார்`**; `துன்மார்க்க முறையை தொடர்கதையாக` and `செயல்வீரர் என்பதையும்` confirmed.
- PDF 33→34: `கொழும்புக் கோரம்` / `வெளிவந்த செய்தி!` continuation confirmed.
- PDF 34: comma after `செல்லப்பட்டாள்` restored; source single hyphens restored in `மாட்டுக்கார்களாக-கூப்பிட்ட` and `வீட்டுக் கூலிகளாக-அடிமைப்பட்டுக்`.
- PDF 35: only body above the ornament is canonical; publisher advertisement, stamp, handwritten `68206`, and later markings below are excluded.

See `audit.md` for the complete T2 findings across all batches.

## Current workflow state

| Gate | State |
|---|---|
| 1. Source inspection / bibliographic-page map | **complete** |
| 2. Tamil first-pass transcription (T1) | **complete — 32/32** |
| 3. Strict visual Tamil fidelity audit (T2) | **complete — 32/32; through PDF 35 / printed 34** |
| 4. Tamil consolidation / freeze (T3) | **not-started** |
| 5. English first-pass translation (E1) | **not-started / locked** |
| 6. English fidelity review (E2) | **not-started / locked** |
| 7. Final Tamil→English verification (E3) | **not-started / locked** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete activity

Proceed with **Stage T3 — Tamil consolidation, stale-reading/page-boundary review, and freeze**.

T3 must, at minimum, follow `SPEECH_PROCESSING_GUIDE.md` and:

- review the consolidated Tamil layer end to end rather than assuming the individual T2 batches compose perfectly;
- check every PDF-page boundary for stale first-pass fragments, accidental duplication/omission, and page-spanning words/sentences;
- search the canonical transcript for any stale uncertainty markers or superseded readings from T1/T2;
- confirm all 32 body pages remain represented exactly once and in source order;
- confirm PDF 35 body/ad boundary remains correct;
- only after those checks pass, change the Tamil layer to `verified-complete` and mark T3 complete;
- do **not** begin English translation before that freeze.

## Root catalogue

Root `README.md` remains intentionally unchanged until final archival closure, as required by `SPEECH_PROCESSING_GUIDE.md`.
