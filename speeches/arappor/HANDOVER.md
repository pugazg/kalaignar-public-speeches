# அறப்போர் - final archival handover

This document records the completed state of the `அறப்போர்` archival workflow. It exists so any future work begins from the verified repository state rather than restarting transcription or translation.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/arappor/`

## Source

- Canonical source record filename: `TVA_BOK_0064122_அறப்போர்.pdf`
- The same source binary was later re-uploaded under the shorter local filename `அறப்போர்.pdf` for final checking.
- SHA-256: `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`
- File size: `31,769,752` bytes
- Actual PDF page count: `22`
- PDF 1: cover
- PDF 2: title page
- PDF 3: imprint
- PDF 4-20: speech body, printed pages 3-19
- PDF 21-22: publisher advertisements / back matter
- The source binary is **not committed to the repository**; its checksum and source identity are recorded.

The title page identifies the item as `மு. கருணாநிதி - பேச்சு.` The imprint states `இரண்டாம்பதிப்பு ஏப்ரல் 1949`. The supplied booklet does **not** state the original speech date, venue, or event. Do not infer those fields from the publication date.

## Editorial rule

This is a source-faithful archive.

- Compare directly against the supplied scan for any future source correction.
- Do not silently modernize spelling, punctuation, wording, names, or unusual source forms.
- Preserve printer/source errors when the printed reading is clear.
- Join a printer line-wrap only when it splits one word.
- Record any future substantive Tamil source correction in `audit.md`.
- Do not use an outside edition to overwrite the supplied source.
- The verified Tamil layer is frozen except for a documented source correction.
- The English translation is subordinate to the verified Tamil layer and must not be used to rewrite it.
- Unusual or internally difficult printed forms should remain transparent through source/translator notes rather than silent emendation.

## Final completion state

### Tamil transcription

- Speech body: **17 / 17 pages complete**
- Strict line-by-line re-audit: **17 / 17 complete**
- Strict visual fidelity audit: **complete**
- Tamil consolidation: **complete**
- Page-boundary/stale-reading consistency pass: **complete**
- Status: **`verified-complete`**

### English translation

- First-pass translation: **17 / 17 pages complete**
- Fidelity review: **17 / 17 pages complete**
- Review corrections/source-transparency notes: **consolidated**
- Final end-to-end Tamil→English comparison: **17 / 17 complete**
- Status: **`verified-complete`**

### Review batches

Tamil strict audit:

1. PDF 4-8 / printed 3-7: complete
2. PDF 9-13 / printed 8-12: complete
3. PDF 14-18 / printed 13-17: complete
4. PDF 19-20 / printed 18-19: complete

English fidelity review:

1. PDF 4-8 / printed 3-7: complete
2. PDF 9-13 / printed 8-12: complete
3. PDF 14-18 / printed 13-17: complete
4. PDF 19-20 / printed 18-19: complete

## Important resolved Tamil fidelity points

- Printed p.18 rhetorical-question endings were confirmed as `தவறு?`.
- Printed p.19 first-line reading crossed by a later ink mark is `மக்களுக்கு`; the annotation is not edition text.
- Printed p.19 unusual forms `மார்க்குடியில்` and `தெரித்தாலும்` were confirmed and retained.
- Genuine page-boundary word splits were joined without changing wording: `மௌனம்`, `நடராஜன்`, `அதற்காக`, `சுப்பராயன்`, `கடைசியாக`.
- The former preliminary p.14 reading `சிலை` was rejected; `துடுப்புக்குச்` / `சியை` joins as `துடுப்புக்குச்சியை`.

## Important English fidelity resolutions

The English review identified and corrected substantive first-pass problems, including:

- the direct reversal around printed p.15 `எங்கள் எண்ணம் புரிபவர்`; the final English follows the verified printed wording and notes its syntactic difficulty;
- the omitted printed expression `அகோபாரடி`, now represented transparently;
- the unsupported closing additions `We will not run. This is the oath we take before the people.`, which were removed; the verified Tamil `இதை மறந்துவிடாதீர்கள்` is now rendered `Do not forget this.`;
- silent normalization of difficult forms such as `மார்க்குடியில்`, `சோதாக்கலா / சோதாக்கலாகி`, `குறுவளிப்பிரச்சாரம்`, `காரைக்கால்—மாக்களை`, and others was replaced by explicit source/translator transparency.

See `translation-review.md` for the full review record and `translation-en.md` for the verified final English layer.

## Canonical repository files

- `transcription-ta.md` — strict-verified Tamil transcription
- `audit.md` — Tamil visual/source-fidelity audit
- `translation-en.md` — verified English translation
- `translation-review.md` — English fidelity-review record
- `metadata.json` — source and workflow metadata
- `README.md` — speech-level archival summary
- root `README.md` — repository catalogue

At final closure, `metadata.json` records:

- `tamil_transcription: verified-complete`
- `tamil_visual_audit: complete`
- `english_translation: verified-complete`
- `english_translation_review: review-complete`
- `english_translation_final_verification: complete`
- all relevant page counters: **17 / 17**

## Future-work gate

**No transcription, Tamil visual-audit, English translation, or translation-fidelity work is currently pending for அறப்போர்.**

Do not restart any completed stage merely because a new chat begins. Reopen the text workflow only if:

1. a specific source-fidelity problem is identified;
2. a genuinely different edition/source is introduced and is being treated as a separate witness rather than overwriting this one; or
3. the user explicitly requests a new derivative layer (for example annotations, historical research, a reading edition, structured data, or publication output).

If a future source correction is necessary, fetch the current `main` versions first, document the evidence, preserve the distinction between source text and interpretation, and propagate only the necessary dependent changes.

## Remaining source-management item

The source PDF binary itself is **not committed to the repository**. This does not block the completed transcription/translation workflow because its identity is fixed by filename, size, page count, and SHA-256. If the binary is later added, verify its SHA-256 against the recorded checksum before treating it as the canonical scan.
