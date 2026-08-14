# இதய பேரிகை — working handover

This document records the exact state after **Stage T3 Tamil consolidation and freeze completion**. Startup, T1, T2 and T3 are complete. The Tamil layer is frozen as `verified-complete`; the next incomplete gate is English first-pass translation. Do not repeat completed Tamil work unless new source evidence requires a documented correction.

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
- PDF 35 lower portion — publisher advertisement; excluded from canonical body

## Completed Tamil work

Gate 1 source inspection/bibliographic mapping is **complete**.

Stage T1 first-pass Tamil transcription is **complete — 32/32 body pages drafted**.

Stage T2 strict visual Tamil fidelity audit is **complete — 32/32 body pages checked and corrections consolidated**:

- T2 Batch 1: PDF 4–8 / printed 3–7
- T2 Batch 2: PDF 9–13 / printed 8–12
- T2 Batch 3: PDF 14–18 / printed 13–17
- T2 Batch 4: PDF 19–23 / printed 18–22
- Final remaining-pages sweep: PDF 24–35 / printed 23–34

Stage T3 consolidation/freeze is **complete — passed 2026-08-14**. The canonical `transcription-ta.md` is now **`verified-complete` and frozen**.

## Stage T3 checks completed

- Reviewed the consolidated Tamil layer as one end-to-end unit after all T2 corrections were applied.
- Confirmed PDF page headings **4–35** / printed pages **3–34** are present once each, in source order.
- Confirmed all seven section starts remain at PDF 4, 12, 17, 21, 24, 30 and 33.
- Rechecked every page boundary for stale fragments, omission/duplication and page-spanning words/sentences.
- Rechecked significant boundaries including `சமுத்தி` / `ரத்தின்`, `சிந்தனைப் பூந்தோட்டத்` / `திலே`, `எப்படி` / `யிருந்தது`, `நெருப்பு அவர்கள்` / `சரீரத்தின்மீது தாவியது.`, `விஷ` / `யத்தில்`, `“மோர்` / `தாப்படவில்லை”`, `கூட்ட` / `மல்ல!`, `குழந்தை` / `கள்.`, `ஓமாந்தூரார்—` / `காணவில்லை தொண்டாற்றும் இந்தத் தூண்கள்!`, `கொழும்புக் கோரம்` / `வெளிவந்த செய்தி!`, and `செயல்களில்` / `ஈடுபடவேண்டும்.`.
- Searched for superseded T1/T2 readings; none remains in the canonical transcript.
- Confirmed no unresolved `⟦...?⟧` marker remains in the body.
- Confirmed PDF 35 body ends above the ornament; publisher advertising and later library/accession markings are excluded.
- T3 required **no further Tamil body correction**. The freeze commit changed only editorial status/workflow text, not the body.

Tamil freeze commit: `c0e327a5cc0cbe15edd9e02253d02f4eb67764cb`.

See `audit.md` for the complete T2 correction trail and T3 consolidation record.

## Important verified source readings to preserve in English work

These are source-supported and must not be silently normalized during translation:

- `மன்றத்திலே இராவணனுக்கு அண்ணா.`
- `திராவிடர் வாழ்வு உயரும்வரையில்`
- `சிலந்திக்கூடு`
- `எச்சு ஒருபுறம் - எண்ணம் - ஒருபுறம்`
- `சீர்திருத்தம் முன்னவிட்டது`
- `சீர்திருத்த கிடந்த`
- `தாப்படவில்லை`
- `நெசவாளர்கிளர்ச்சியை`
- `போலீஸ்காரணங்களை`
- `சுமன்றன கேள்விகள்`
- `சூறவளிக் காற்று`
- `துன்மார்க்க முறையை தொடர்கதையாக`
- `செயல்வீரர் என்பதையும்`

If a literal English rendering of a difficult printed form would mislead, preserve transparency with a concise translator/source note rather than silently repairing the Tamil.

## Current workflow state

| Gate | State |
|---|---|
| 1. Source inspection / bibliographic-page map | **complete** |
| 2. Tamil first-pass transcription (T1) | **complete — 32/32** |
| 3. Strict visual Tamil fidelity audit (T2) | **complete — 32/32** |
| 4. Tamil consolidation / freeze (T3) | **complete — `verified-complete`, frozen 2026-08-14** |
| 5. English first-pass translation (E1) | **not-started — ready** |
| 6. English fidelity review (E2) | **not-started / locked until E1 completes** |
| 7. Final Tamil→English verification (E3) | **not-started / locked** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete activity

Proceed with **Stage E1 — English first-pass translation**.

For E1:

- translate **only from the frozen `transcription-ta.md`**, not from OCR and not independently from the PDF or an outside edition;
- retain PDF/printed-page headings and source paragraph/page sequence;
- preserve argument structure, rhetorical force, repetition, metaphors, polemical language and historical references;
- do not silently normalize difficult verified Tamil forms;
- use concise translator/source notes where literal rendering would otherwise mislead;
- translate the complete 32-page body before beginning E2;
- keep `translation-review.md` at not-started until E1 is complete;
- do not perform root catalogue closure yet.

## Root catalogue

Root `README.md` remains intentionally unchanged until final archival closure, as required by `SPEECH_PROCESSING_GUIDE.md`.

## Unresolved bibliographic issue

The exact printer name on PDF page 3 remains unresolved because a later library stamp crosses the printed line. It must not be guessed. This does not affect the frozen Tamil body or the start of English translation.
