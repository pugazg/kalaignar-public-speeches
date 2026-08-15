# பள்ளி வாழ்க்கை — T2 handover

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

## Current workflow state

### T1 — COMPLETE
All **76/76 speech-body pages** have first-pass readings.

Storage remains segmented until T3:
- `transcription-ta.md`: PDF 6-45 / printed 5-44
- T1 Batches 9-12: PDF 46-81 / printed 45-80

### T2 — IN PROGRESS: 5/76
Completed strict visual audit:
- **PDF 6-10 / printed 5-9**

Detailed verified correction record:
- `t2-batches/batch-01-pdf-06-10.md`

Confirmed corrections from Batch 1:
- `ஆராய்ந்து தெரிந்து` → `ஆராய்ந்து தெளிந்து`
- `கற்றோனாக` → `கற்றோனுக`
- `கல்லூரனாக` → `கல்லூரனுக`
- `கதாசிரியனாக` → `கதாசிரியனுக`
- `கட்டுரையாசிரியனாக` → `கட்டுரையாசிரியனுக`
- `உத்தமனாக` → `உத்தமனுக`
- `மண்ணாவது` → `மண்ணுவது`

PDF 9→10 split `உயி` / `ரினங்களைவிட` was visually checked on both pages and the consolidated one-word reading `உயிரினங்களைவிட` is confirmed.

Because the repository currently uses source-controlled segmented T1 text, verified T2 corrections are being retained in `t2-batches/` and must be applied during T3. This avoids destructive whole-file replacement while auditing. The T3 stale-reading check must ensure none of the superseded T1 forms survive.

### T3
- Not started.
- Tamil is not frozen or `verified-complete`.

### English
- Not started; blocked until T2 and T3 pass.

## Exact next activity

Perform T2 strict visual audit of **PDF pages 11-15 / printed pages 10-14**.

Specifically:
- compare every line against the scan;
- resolve PDF 13→14 `இவர்` / `கட்கு`;
- inspect queued unusual readings including `வாழ்க்கத்தின்`, `நன்றுக`, `உயிரினங்களின் றும்`, `வாழ்க்கைச் செந்தி`, and `வாசனே`;
- record only scan-supported corrections, without modernization.

## Safeguards
- Scan is authoritative; OCR is only an aid.
- T2 is source comparison, not proofreading.
- Preserve historical spelling, punctuation, wording, names, numbers, repetition, unusual grammar and typographical forms.
- Do not infer event metadata from publication data or outside history.
- Do not commit the source PDF.
- Do not begin English translation until Tamil passes T2 and T3.
