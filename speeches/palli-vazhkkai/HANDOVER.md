# பள்ளி வாழ்க்கை — T3 handover

## Repository
- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/palli-vazhkkai/`

## Source
- Canonical source: `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`
- SHA-256: `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`
- PDF pages: 81
- Speech body: PDF 6-81 / printed 5-80 = 76 pages
- Source PDF committed: No

## Workflow state

### T1 — COMPLETE
All **76/76 speech-body pages** have first-pass readings.

Current T1 storage remains segmented pending T3 consolidation:
- `transcription-ta.md`: PDF 6-45 / printed 5-44
- `t1-batches/batch-09-pdf-46-50.md`: PDF 46-50 / printed 45-49
- `t1-batches/batch-10-pdf-51-60.md`: PDF 51-60 / printed 50-59
- `t1-batches/batch-11-pdf-61-70.md`: PDF 61-70 / printed 60-69
- `t1-batches/batch-12-pdf-71-81.md`: PDF 71-81 / printed 70-80

### T2 — COMPLETE: 76/76
Every body page from **PDF 6 through PDF 81 / printed 5 through 80** has passed strict visual line-by-line comparison against the supplied scan.

Detailed T2 records:
- Batches 1-16 under `t2-batches/`
- final batch: `t2-batches/batch-16-pdf-81.md`
- legacy-glyph corrective records:
  - `t2-batches/legacy-glyph-recheck-pdf-06-35.md`
  - `t2-batches/legacy-glyph-recheck-pdf-36-40.md`

The traditional pre-1978 Tamil glyph issue has been accounted for through the final page. T3 must encode the underlying Tamil characters and must not resurrect visual-lookalike T1/T2 readings such as `கவலிப்பட`, `நன்றுக`, `தமிழனுக`, `தேவனே` where the scan established `கவலைப்பட`, `நன்றாக`, `தமிழனாக`, `தேவனை`, etc.

### Final T2 page — PDF 81 / printed 80
Confirmed corrections:
- `தமிழமெல்லாம்` → **`தமிழரெல்லாம்`**
- `தமிழனத்தை` → **`தமிழினத்தை`**

PDF 80→81 was reconfirmed as ordinary sentence continuation after `என்றெல்லாம் நாட்டில் கூக்குரல்,`.

The scan-confirmed closing ends:
`... தீரத் தமிழராக, தன்மானச் சிங்கங்களாக விளங்க அடிப்படை காணுங்கள், பள்ளி வாழ்க்கையில்! வணக்கம் !!`

### T3 — ACTIVE NEXT GATE
- Canonical Tamil consolidation/freeze: **not started**.
- Tamil is not yet `verified-complete` or frozen.

### English
- E1 translation: not started.
- E2 fidelity review: not started.
- E3 final verification: not started.
- English remains blocked until T3 passes.

## Exact next activity

Perform **T3 canonical Tamil consolidation and freeze preparation**:

1. Build one continuous `transcription-ta.md` covering PDF 6-81 / printed 5-80 from the existing canonical segment plus T1 batches.
2. Apply every scan-proven correction from T2 Batches 1-16 and both legacy-glyph recheck records.
3. Apply all verified page-boundary/printer-wrap joins recorded in `audit.md`.
4. Run a stale-reading search for all superseded glyph misreadings and all specifically corrected T1 forms.
5. Verify page-label continuity, first/last text, and all source-supported unusual forms.
6. Only after the complete consolidated Tamil passes those checks, set the Tamil layer to `verified-complete` / frozen and remove temporary T1 staging files if the guide permits.

Do **not** begin English translation until the T3 gate has actually passed.

## Safeguards
- The scan is authoritative; OCR and T1 are only aids.
- Do not modernize, normalize, reconstruct or improve source wording.
- Decode obsolete glyph shapes to the correct underlying Tamil characters.
- Preserve source-supported spelling, punctuation, names, numbers, repetition, unusual grammar and typographical forms.
- Do not infer speech date/venue/event from publication data or outside history.
- Do not commit the source PDF.