# அறப்போர் - continuation handover

This document records the exact state of the `அறப்போர்` archival workflow so work can continue safely in a new ChatGPT window without relying on conversation memory.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Baseline HEAD before this handover file was added: `d9897a408bb56e6e7344b5f6118e50277fef76df`
- Speech directory: `speeches/arappor/`

## Source

- Source filename: `TVA_BOK_0064122_அறப்போர்.pdf`
- SHA-256: `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`
- File size: `31,769,752` bytes
- Actual PDF page count: `22`
- PDF 1: cover
- PDF 2: title page
- PDF 3: imprint
- PDF 4-20: speech body, printed pages 3-19
- PDF 21-22: publisher advertisements / back matter
- The source binary is **not committed to the repository**. If it is not available in the new window, ask the user to upload the same PDF and verify the SHA-256 before continuing.

The title page identifies the item as `மு. கருணாநிதி - பேச்சு.` The imprint states `இரண்டாம்பதிப்பு ஏப்ரல் 1949`. The supplied booklet does **not** state the original speech date, venue, or event. Do not infer those fields from the publication date.

## Editorial rule

This is a source-faithful archival transcription.

- Compare directly against the scan.
- Do not silently modernize spelling, punctuation, wording, names, or unusual source forms.
- Preserve printer/source errors when the printed reading is clear.
- Join a printer line-wrap only when it splits one word.
- Record substantive corrections in `audit.md`.
- Do not use an outside edition to overwrite the supplied source.
- Do not start English translation until the strict Tamil re-audit and consolidation are complete.

## Why the audit was reopened

A first-pass Tamil transcription of all 17 speech pages was completed. An initial visual sweep then marked the whole speech verified, but a later stricter line-by-line check found additional transcription discrepancies. Therefore the earlier whole-document `verified` status is superseded.

The controlling state is now `audit.md` plus `metadata.json`, not the old `verified` header/table still present in `transcription-ta.md`.

## Current completion state

### Tamil transcription

- First-pass speech transcription: **17 / 17 pages complete**
- Strict line-by-line re-audit: **15 / 17 pages complete**
- Strict re-audit completion: **88.2%**
- Remaining strict audit: **2 pages**
- English translation: **blocked**

### Strict audit batches

1. Batch 1 - PDF 4-8 / printed 3-7: **complete**
2. Batch 2 - PDF 9-13 / printed 8-12: **complete**
3. Batch 3 - PDF 14-18 / printed 13-17: **complete**
4. Batch 4 - PDF 19-20 / printed 18-19: **PENDING**

The user requested batches of five pages when possible. Batch 4 naturally contains only the final two speech pages.

## Current critical repository files

- `speeches/arappor/audit.md`
  - current blob SHA: `b736b97f3d70d77c6609313f1dca36cc8204c887`
  - contains all strict Batch 1-3 findings
- `speeches/arappor/metadata.json`
  - current blob SHA: `8382cfa905fc24a0f3b6888810c3a1df224581ff`
  - records `strict_reaudit_pages_checked: 15`
- `speeches/arappor/transcription-ta.md`
  - current blob SHA: `8dc313f184ef7463fe8203c430448fb6e2eaea64`
  - contains the complete speech but **has not yet been consolidated with all strict Batch 1-3 corrections**
- `speeches/arappor/README.md`
  - project-level source/editorial description

Always fetch the current files from `main` before writing; the SHAs above are only the handover-time state.

## Strict Batch 1-3 findings already recorded

Do not redo these batches unless a later consistency check exposes a problem. `audit.md` is the authoritative detailed correction log. Important examples include:

- printed p.3: `வோட்டுக்களே` -> `வோட்டுகளே`
- printed p.4: `போர் மூள்வதற்குக் காரணம் கால்கோள் விழா` -> `போர் மூள்வதற்குக் கால்கோள் விழா`
- printed p.4: `எம்மீது ஏவிய` -> printed `எம் மீது எவிய`
- printed p.7: `நெரிக்கும்காட்சி` -> `நெறிக்கும் காட்சி`
- printed p.7: `கேள்விகேட்போம்` -> `கேள்விகிளப்பினோம்`
- printed p.8: `உத்தரவு` -> `உத்திரவு`
- printed p.9: `இந்துவும் மந்திரனும்` -> `இந்துவும் மித்திரனும்`
- printed p.9 quotation: `இரண்டாம் மொழிக்கு மட்டும் கட்டாயம்` -> `இரண்டாம் மொழிக்கும்தான் கட்டாயம்`
- printed p.11: `சிவசிந்தாமணியைக்` -> printed `சிவகசிந்தாமணியைக்`
- printed p.12: `தேசயத்திரா விட்டோரே!` -> `தேசியத்திராவிடரே!`
- printed p.14: `துடுப்புக்குச் சிலை` -> line-wrap joins as `துடுப்புக்குச்சியை`
- printed p.16: `பலிபீடத்தில் தலைபிழந்த` -> `பலிபீடத்தில் தலையிழந்த`
- printed p.17: `மாநாடு செய்திகளை` -> `மாநாட்டு செய்திகளை`
- printed p.17: `பண்டிதநேருஜி படத்துப் புரண்டதும்` -> `பண்டிதநேருஜி படுத்துப் புரண்டதும்`

See `audit.md` for the complete list and source-fidelity notes.

## Exact next task - Batch 4

Strictly re-audit:

- PDF page 19 = printed page 18
- PDF page 20 = printed page 19

Work line by line against the rendered source images. Do **not** trust the current transcript merely because the older table says verified.

Pay special attention to readings that were changed during the preliminary sweep, but re-confirm them from the scan rather than assuming they are correct. In particular:

- printed p.18 contains a sequence of rhetorical questions where the preliminary sweep changed several `தவறா?` readings to source `தவறு?`; verify every instance directly.
- printed p.19 first line previously had an uncertainty marker around the word later read as `மக்களுக்கு`; a later ink mark crosses that area, so verify the underlying printed reading carefully.
- check punctuation, word boundaries, and printer line-wraps throughout both pages, not only previously flagged words.

After Batch 4, append its findings to `audit.md` and update progress to **17 / 17** only if both pages have been fully checked.

## Required post-Batch-4 consolidation

Do not jump straight to English translation. Complete these steps first:

1. Fetch the latest `transcription-ta.md`.
2. Apply **all** strict corrections from Batch 1, Batch 2, Batch 3, and Batch 4 to the complete transcript.
3. Remove obsolete uncertainty markers only where the scan supports a definite reading.
4. Update the page status table so all 17 pages are strict-verified only after consolidation.
5. Change the transcription header from the obsolete preliminary status to a final strict-verification status.
6. Search the consolidated transcript for stale forms listed in `audit.md` to make sure none were missed.
7. Check page-boundary joins and paragraph boundaries one more time.
8. Update `metadata.json` to something equivalent to:
   - `tamil_transcription: verified-complete`
   - `strict_reaudit_pages_checked: 17`
   - `strict_reaudit_through_pdf_page: 20`
   - `strict_reaudit_through_printed_page: 19`
   - `tamil_visual_audit: complete`
   - `combined_transcript_pending_batch_corrections: false`
   - `english_translation: ready-not-started`
9. Update `speeches/arappor/README.md` and the root catalogue status if they still describe an earlier stage.
10. Only then may English translation begin.

## Translation rule after Tamil verification

When English translation starts, create a separate `translation-en.md`. Keep the verified Tamil transcription untouched except for documented source corrections. Translation should preserve the rhetoric and historical context without silently rewriting the Tamil source or presenting the April 1949 publication date as the speech date.

## Recommended prompt for the next window

Use this as the continuation prompt:

> Continue `pugazg/kalaignar-public-speeches` on `main`. First read `speeches/arappor/HANDOVER.md`, `speeches/arappor/audit.md`, `speeches/arappor/metadata.json`, and `speeches/arappor/transcription-ta.md`. Treat those repository files as controlling instructions. I will provide `TVA_BOK_0064122_அறப்போர்.pdf` if the source is not already available. Verify its SHA-256 is `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`. Complete strict Batch 4 for PDF pages 19-20 / printed pages 18-19, then consolidate all strict Batch 1-4 corrections into `transcription-ta.md`, perform the final consistency check, update the audit/metadata/README statuses, and keep English translation blocked until Tamil verification is genuinely complete.

## Do not do

- Do not restart transcription from scratch.
- Do not redo completed batches without a specific reason.
- Do not trust the old `verified` table in `transcription-ta.md` until consolidation is complete.
- Do not infer a speech date, venue, or event.
- Do not modernize or normalize unusual printed Tamil merely because another form seems grammatically preferable.
- Do not start English translation before the final Tamil consolidation gate passes.
