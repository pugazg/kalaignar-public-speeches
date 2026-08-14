# இதய பேரிகை — working handover

This document records the exact state after **Stage E2 English fidelity review and correction consolidation**. Startup, T1, T2, T3, E1 and E2 are complete. The Tamil layer remains frozen as `verified-complete`. All **32/32 English body pages** were independently reviewed against frozen Tamil, **19 confirmed fidelity corrections** were recorded, and all **19/19 have now been consolidated into `translation-en.md`**.

The next incomplete gate is **Stage E3 — final beginning-to-end Tamil→English verification**.

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

## Stage E1

Stage E1 first-pass English translation is **complete — 32/32 body pages**, through PDF 35 / printed 34.

E1 completion translation commit: `332f17ec074f26588a898417f1efba802a221102`.

## Stage E2 completion

Stage E2 independently reviewed all **32/32 body pages** against frozen Tamil.

Batch results:

- PDF 4–8 / printed 3–7 — 0 corrections.
- PDF 9–13 / printed 8–12 — 6 corrections.
- PDF 14–18 / printed 13–17 — 2 corrections.
- PDF 19–23 / printed 18–22 — 4 corrections.
- PDF 24–28 / printed 23–27 — 3 corrections.
- PDF 29–35 / printed 28–34 — 4 corrections.

**Total confirmed E2 corrections: 19. All 19/19 are consolidated.**

English consolidation commit: `bc19daddaa67b079e372beeded1f58828289b839`.

The consolidation commit was checked against the correction ledger in `translation-review.md`. It contains the 19 source-supported corrections plus workflow/status changes and the required explanatory source notes; the frozen Tamil was not altered.

## Important consolidated E2 corrections

- PDF 11 `மனமுடைந்த பிறகுங்கூட` — now “had become disheartened,” not “hearts had been broken.”
- PDF 12 — `நிதானிக்காமல்`, `திருக்கல்யாணக் குணங்கள்`, and the `அம்மாமித் தமிழ்` note corrected/narrowed.
- PDF 13 — `பல்லாயிரவர்` and `லட்சம்பேர்` numerical scope corrected.
- PDF 16 — difficult `பொறுமையை அடக்கமுடியாத` exposed rather than silently normalized; source note added.
- PDF 18 — `வெறுப்பு` restored as “hatred.”
- PDF 20 — actual unresolved classical line `கடமலை வேட்டமென் கட்டபுலம்பிரியாது` restored verbatim inside the quotation; marked untranslated; no outside edition substituted.
- PDF 22 — source note added for `மடத்தனத்தை அழித்தது. மக்கள் சமுதாயத்தை...`; `மட்டமானது` rendered “inferior.”
- PDF 23 — editorial review commentary removed from translated body; difficult-source note retained.
- PDF 24 — `கோலாகலம்` rendered as “celebration,” not “music.”
- PDF 27 — `ஜாமீன் வழக்கு` rendered source-facing as “bail case,” not inferred “security proceedings.”
- PDF 28 — `பலாத்கார பேச்சுக்கள்` rendered “violent speeches.”
- PDF 31 — `பிணக்குவியல்கள்` rendered “heaps of corpses”; `வகுப்புவாரி உரிமை` rendered “class-wise rights.”
- PDF 34 — `ஆயிரக் கணக்கில்` reduced to “stories in the thousands.”
- PDF 35 — critical correction: `குருதியிலே மிதக்கவிட்டிருக்கிறது` now reads **“left a ten-year-old boy floating in blood,”** not “trampled in blood.”

The complete numbered ledger is retained in `translation-review.md`.

## Reviewed difficult-source outcomes to preserve in E3

- PDF 7 `சீனத் தீவு` — literal “Chinese island” rendering/note accepted.
- PDF 15 `மன்றத்திலே இராவணனுக்கு அண்ணா.` — compact rendering/note accepted.
- PDF 16 `பொறுமையை அடக்கமுடியாத` — difficult form explicitly surfaced.
- PDF 20 classical quotation — unresolved printed line retained verbatim, untranslated; no outside edition substitution.
- PDF 21 `எச்சு ஒருபுறம் - எண்ணம் - ஒருபுறம்` — current rendering/note accepted.
- PDF 22 `சுயநலம் அவர்கள் வாழ்வில் சுற்றிக்கிடந்தது` — tension-preserving rendering/note accepted; separate syntax note retained.
- PDF 23 `சீர்திருத்தம் முன்னவிட்டது` / `சீர்திருத்த கிடந்த` — difficult-source note retained.
- PDF 26 `தாப்படவில்லை` — current transliteration/note accepted.
- PDF 27 `போலீஸ்காரணங்களை` — current source-facing rendering/note accepted.
- PDF 31 `சுமன்றன கேள்விகள்` / `சூறவளிக் காற்று` — current rendering/note accepted.
- PDF 32 `துன்மார்க்க முறையை தொடர்கதையாக` / `செயல்வீரர் என்பதையும்` — current rendering accepted.

## Current workflow state

| Gate | State |
|---|---|
| 1. Source inspection / bibliographic-page map | **complete** |
| 2. Tamil first-pass transcription (T1) | **complete — 32/32** |
| 3. Strict visual Tamil fidelity audit (T2) | **complete — 32/32** |
| 4. Tamil consolidation / freeze (T3) | **complete — `verified-complete`, frozen 2026-08-14** |
| 5. English first-pass translation (E1) | **complete — 32/32** |
| 6. English fidelity review (E2) | **complete — 32/32** |
| 6a. E2 correction consolidation | **complete — 19/19 applied** |
| 7. Final Tamil→English verification (E3) | **ready-not-started** |
| 8. Repository closure/catalogue synchronization | **not-started** |

## Exact next incomplete activity

Proceed with **Stage E3 — final Tamil→English verification** across the complete **PDF 4–35 / printed 3–34** body.

For E3:

- compare the complete reviewed `translation-en.md` against frozen `transcription-ta.md` from beginning to end;
- verify every page and section appears exactly once and in source order;
- recheck every PDF-page continuation and section boundary;
- explicitly verify all 19 consolidated E2 corrections in context;
- recheck every translator/source note so it states no more than the frozen Tamil supports;
- detect any omission, duplication, reversal, changed subject/pronoun, altered rhetoric, or editorial commentary leakage introduced during consolidation;
- make only source-supported final English corrections, if any;
- do not alter frozen Tamil without new source evidence and dependent English re-verification;
- do not update the root catalogue until E3 passes and final archival closure begins.

## Root catalogue

Root `README.md` remains intentionally unchanged until final archival closure, as required by `SPEECH_PROCESSING_GUIDE.md`.

## Unresolved bibliographic issue

The exact printer name on PDF page 3 remains unresolved because a later library stamp crosses the printed line. It must not be guessed. This does not affect the frozen Tamil body or English workflow.
