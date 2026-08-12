# அறப்போர் - continuation handover

This document records the exact current state of the `அறப்போர்` archival workflow so work can continue safely in a new ChatGPT window without relying on conversation memory.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Baseline HEAD immediately before this handover refresh: `de3e9cc5b3193de5c0be2086337134e80749ef0d`
- Speech directory: `speeches/arappor/`

## Source

- Canonical source record filename: `TVA_BOK_0064122_அறப்போர்.pdf`
- The same binary was re-uploaded for the final audit under the shorter local filename `அறப்போர்.pdf`.
- SHA-256: `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`
- File size: `31,769,752` bytes
- Actual PDF page count: `22`
- PDF 1: cover
- PDF 2: title page
- PDF 3: imprint
- PDF 4-20: speech body, printed pages 3-19
- PDF 21-22: publisher advertisements / back matter
- The source binary is **not committed to the repository**.

The title page identifies the item as `மு. கருணாநிதி - பேச்சு.` The imprint states `இரண்டாம்பதிப்பு ஏப்ரல் 1949`. The supplied booklet does **not** state the original speech date, venue, or event. Do not infer those fields from the publication date.

## Editorial rule

This is a source-faithful archival transcription.

- Compare directly against the supplied scan for any future source correction.
- Do not silently modernize spelling, punctuation, wording, names, or unusual source forms.
- Preserve printer/source errors when the printed reading is clear.
- Join a printer line-wrap only when it splits one word.
- Record any future substantive source correction in `audit.md`.
- Do not use an outside edition to overwrite the supplied source.
- The verified Tamil layer should now remain frozen except for documented source corrections.

## Current completion state

### Tamil transcription

- First-pass speech transcription: **17 / 17 pages complete**
- Strict line-by-line re-audit: **17 / 17 pages complete**
- Strict re-audit completion: **100%**
- Tamil consolidation: **complete**
- Final stale-reading / page-boundary consistency pass: **complete**
- English translation: **ready-not-started**

### Strict audit batches

1. Batch 1 - PDF 4-8 / printed 3-7: **complete**
2. Batch 2 - PDF 9-13 / printed 8-12: **complete**
3. Batch 3 - PDF 14-18 / printed 13-17: **complete**
4. Batch 4 - PDF 19-20 / printed 18-19: **complete**

## Batch 4 result

PDF pages 19-20 / printed pages 18-19 were re-audited line by line against the verified source binary.

- Printed p.18: every rhetorical-question ending checked in the opening paragraph is confirmed as the printed form `தவறு?`, not the earlier `தவறா?` reading.
- Printed p.19: the first-line word crossed by a later blue/ink mark is definitively `மக்களுக்கு`; the annotation is not part of the edition text.
- Printed p.19 unusual forms `மார்க்குடியில்` and `தெரித்தாலும்` were re-confirmed from the printed glyphs and retained.
- No additional substantive wording correction was required on these final two pages beyond readings already incorporated during the preliminary sweep.

## Final consolidation completed

All strict Batch 1-4 corrections recorded in `audit.md` have been applied to `transcription-ta.md`.

The final consistency pass also joined genuine words split at PDF-page boundaries without changing source wording:

- `மௌ` / `னம்` -> `மௌனம்`
- `நடரா` / `ஜன்` -> `நடராஜன்`
- `அதற்` / `காக` -> `அதற்காக`
- `சுப்பரா` / `யன்` -> `சுப்பராயன்`
- `கடை` / `சியாக` -> `கடைசியாக`

The former preliminary p.14 reading `சிலை` is not valid: the printer line-wrap `துடுப்புக்குச்` / `சியை` joins as `துடுப்புக்குச்சியை`.

## Current critical repository state

Fetch the current versions from `main` before any future write. At this handover refresh the content blobs are:

- `speeches/arappor/transcription-ta.md` - `4a42154fe26c97063c786df68951ca918ece46b7`
  - status: strict-verified complete, 17/17
- `speeches/arappor/audit.md` - `bd6fb45d9ac6b82823e682e3d6f8514bee85271c`
  - status: Batch 1-4 audit complete and consolidated
- `speeches/arappor/metadata.json` - `537d3f8c5b3e38a7426941d0ffd8f358093149d6`
  - `tamil_transcription: verified-complete`
  - `strict_reaudit_pages_checked: 17`
  - `strict_reaudit_through_pdf_page: 20`
  - `strict_reaudit_through_printed_page: 19`
  - `tamil_visual_audit: complete`
  - `combined_transcript_pending_batch_corrections: false`
  - `english_translation: ready-not-started`
- `speeches/arappor/README.md` - `3c753ace1da0b1cd079b8b39ff1552c324fbd048`
  - strict-verification status updated
- root `README.md` - `5e47999370c3f12ba415e2440b3b830837709d68`
  - catalogue updated to strict-verified complete / translation ready-not-started

## Exact next task

**Do not re-audit or retranscribe the Tamil speech unless a specific source-fidelity issue is identified.**

When the user asks to continue this speech, the next archival layer is English translation:

1. Fetch the latest `speeches/arappor/transcription-ta.md`, `audit.md`, `metadata.json`, and this handover from `main`.
2. Create a separate `speeches/arappor/translation-en.md`.
3. Translate from the verified Tamil transcription, not from OCR or an outside edition.
4. Preserve the rhetoric, repeated constructions, political/historical references, and source distinctions as faithfully as practical in English.
5. Do not silently rewrite the Tamil source while translating.
6. Do not present April 1949 as the speech date; it is the second-edition publication date only.
7. Update metadata/README/catalogue translation status only after the English layer has actually been created and reviewed.

## Do not do

- Do not restart Tamil transcription from scratch.
- Do not redo strict Batches 1-4 without a specific source reason.
- Do not normalize unusual printed Tamil merely because another form seems grammatically preferable.
- Do not infer a speech date, venue, or event.
- Do not modify the verified Tamil layer merely to make an English translation read more smoothly.
