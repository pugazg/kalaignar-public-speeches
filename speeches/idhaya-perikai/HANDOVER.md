# இதய பேரிகை — working handover

This document records the exact state after **Stage E1 English first-pass translation completion**. Startup, T1, T2, T3 and E1 are complete. The Tamil layer remains frozen as `verified-complete`. The next incomplete gate is Stage E2 independent English fidelity review.

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

## Stage E1 completion

Stage E1 first-pass English translation is **complete — 32 / 32 body pages translated**, through PDF page 35 / printed page 34.

The user requested that the remaining pages be handled in a single activity, so after the initial PDF 4–8 batch the complete remaining body, PDF **9–35 / printed 8–34**, was translated in this activity.

The English translation:

- was produced only from the frozen `transcription-ta.md` layer;
- retains every PDF/printed-page heading and section boundary;
- preserves source paragraph order, argument structure, repetition, metaphors, historical references and polemical force;
- does not silently repair difficult verified Tamil readings;
- uses concise translator/source notes where an apparently smooth English rendering would conceal a genuine source difficulty;
- stops with the body text on PDF 35 and does not translate the excluded publisher advertisement below the ornament.

E1 completion translation commit: `332f17ec074f26588a898417f1efba802a221102`.

## First-pass source-difficulty notes requiring special E2 attention

The E1 translation deliberately surfaces difficult source readings rather than normalizing them. E2 must inspect these carefully:

- PDF 7: `சீனத் தீவு`;
- PDF 15: `மன்றத்திலே இராவணனுக்கு அண்ணா.`;
- PDF 20: dense classical quotation beginning `கொங்கணர் கலிங்கர் கொடுங்கருநாடர்`;
- PDF 21: `எச்சு ஒருபுறம் - எண்ணம் - ஒருபுறம்`;
- PDF 22: `சுயநலம் அவர்கள் வாழ்வில் சுற்றிக்கிடந்தது`, followed by sentences denying personal-interest interference;
- PDF 23: `சீர்திருத்தம் முன்னவிட்டது` and `சீர்திருத்த கிடந்த`;
- PDF 26: `தாப்படவில்லை`;
- PDF 27: `போலீஸ்காரணங்களை`;
- PDF 31: `சுமன்றன கேள்விகள்` and `சூறவளிக் காற்று`;
- PDF 32: `துன்மார்க்க முறையை தொடர்கதையாக` and `செயல்வீரர் என்பதையும்`.

The classical quotation on PDF 20 was translated cautiously from this frozen source only; no outside edition was consulted or substituted. E2 should treat that passage as a priority review item.

## Current workflow state

| Gate | State |
|---|---|
| 1. Source inspection / bibliographic-page map | **complete** |
| 2. Tamil first-pass transcription (T1) | **complete — 32/32** |
| 3. Strict visual Tamil fidelity audit (T2) | **complete — 32/32** |
| 4. Tamil consolidation / freeze (T3) | **complete — `verified-complete`, frozen 2026-08-14** |
| 5. English first-pass translation (E1) | **complete — 32/32; through PDF 35 / printed 34** |
| 6. English fidelity review (E2) | **ready-not-started** |
| 7. Final Tamil→English verification (E3) | **not-started / locked until E2 completes** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete activity

Proceed with **Stage E2 — independent Tamil→English fidelity review**.

For E2:

- compare every translated page in `translation-en.md` independently against frozen `transcription-ta.md`;
- review all **32 body pages**; completeness matters more than batch size;
- check omissions, additions, reversals, changed subjects/pronouns, softened or strengthened rhetoric, lost repetition, historical names/titles, source-supported oddities and page-boundary continuity;
- review every translator/source note to ensure it does not overstate what the Tamil establishes;
- record findings first in `translation-review.md`;
- apply only confirmed corrections to `translation-en.md`;
- do not change the frozen Tamil unless new source evidence justifies a documented correction;
- do not begin E3 until E2 is complete and all confirmed English corrections are consolidated;
- do not perform root catalogue closure yet.

## Root catalogue

Root `README.md` remains intentionally unchanged until final archival closure, as required by `SPEECH_PROCESSING_GUIDE.md`.

## Unresolved bibliographic issue

The exact printer name on PDF page 3 remains unresolved because a later library stamp crosses the printed line. It must not be guessed. This does not affect the frozen Tamil body or the English workflow.
