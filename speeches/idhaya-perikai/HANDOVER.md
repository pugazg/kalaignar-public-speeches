# இதய பேரிகை — working handover

This document records the exact state after **Stage E1 English first-pass translation Batch 1**. Startup, T1, T2 and T3 are complete. The Tamil layer is frozen as `verified-complete`. E1 is now in progress; do not repeat completed Tamil work unless new source evidence requires a documented correction, and do not begin E2 before all 32 body pages have an English first pass.

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

- Gate 1 source inspection/bibliographic mapping: **complete**.
- Stage T1 first-pass Tamil transcription: **complete — 32/32**.
- Stage T2 strict visual Tamil fidelity audit: **complete — 32/32**.
- Stage T3 consolidation/freeze: **complete — passed 2026-08-14**.
- Canonical `transcription-ta.md`: **`verified-complete` and frozen**.

Tamil freeze commit: `c0e327a5cc0cbe15edd9e02253d02f4eb67764cb`.

See `audit.md` for the complete T2 correction trail and T3 consolidation record.

## Stage E1 progress

Stage E1 first-pass English translation is **in progress — 5 / 32 body pages complete**.

Completed E1 Batch 1:

- PDF 4 / printed 3
- PDF 5 / printed 4
- PDF 6 / printed 5
- PDF 7 / printed 6
- PDF 8 / printed 7

The English file retains PDF/printed-page headings and follows the frozen Tamil paragraph and rhetorical sequence. Translation is being made only from `transcription-ta.md`, not from OCR or an outside edition.

The PDF 7 source wording `சீனத் தீவு` is sufficiently unusual that the English translation preserves the literal “Chinese island” wording and includes a concise translator/source note rather than silently correcting it.

PDF 8 ends in the middle of a continuing source sentence (`...தேனியிலே திருவிளையாடல் புரிந்து`); the English first pass intentionally ends the page with the corresponding continuation dash. Resume from the beginning of PDF 9 without inventing bridging wording.

E1 Batch 1 translation commit: `fad8c27a24a85ca03066e0ce9aafde5b53f253b8`.

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
| 5. English first-pass translation (E1) | **in progress — 5/32; through PDF 8 / printed 7** |
| 6. English fidelity review (E2) | **not-started / locked until E1 completes** |
| 7. Final Tamil→English verification (E3) | **not-started / locked** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete activity

Continue **Stage E1 — English first-pass translation** at **PDF page 9 / printed page 8**.

A practical next batch is PDF **9–13 / printed 8–12**, continuing the sentence from PDF 8 and then proceeding through the source page boundaries exactly.

For E1:

- translate **only from the frozen `transcription-ta.md`**;
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

The exact printer name on PDF page 3 remains unresolved because a later library stamp crosses the printed line. It must not be guessed. This does not affect the frozen Tamil body or ongoing English translation.
