# அறப்போர் - visual fidelity audit

**Source:** `TVA_BOK_0064122_அறப்போர்.pdf`  
**Source SHA-256:** `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`  
**Audit date:** 2026-08-12  
**Scope:** PDF pages 4-20, corresponding to printed pages 3-19

## Important audit state

The earlier whole-document sweep has been **re-opened** for a stricter line-by-line fidelity pass. A five-page re-audit found additional source/transcription discrepancies that the preliminary sweep had missed. Therefore the Tamil text must **not** yet be treated as final/canonical, and English translation is blocked again until this stricter pass is complete.

## Method

- Compare directly against the supplied scan, not against modern spelling or outside editions.
- Preserve printed wording, historical spelling, punctuation, names, and unusual/possibly erroneous source forms when legible.
- Join printer line-wraps only when they split a single word.
- Record substantive corrections rather than silently normalizing them.
- Work in batches of **5 speech pages**.

## Strict re-audit progress

| Batch | PDF pages | Printed pages | Status |
|---|---|---|---|
| 1 | 4-8 | 3-7 | re-audited |
| 2 | 9-13 | 8-12 | pending |
| 3 | 14-18 | 13-17 | pending |
| 4 | 19-20 | 18-19 | pending |

Strictly re-audited pages: **5 / 17**.

## Batch 1 findings - PDF pages 4-8 / printed pages 3-7

The following readings were confirmed or corrected against the scan during the stricter pass:

| Printed page | Existing reading | Scan-supported reading / action |
|---:|---|---|
| 3 | `வோட்டுக்களே` | `வோட்டுகளே` |
| 3 | earlier draft `மற்றுக் கட்சியினர்` | `மாற்றுக் கட்சியினர்` - current combined transcript already has this correction |
| 4 | `போர் மூள்வதற்குக் காரணம் கால்கோள் விழா` | `போர் மூள்வதற்குக் கால்கோள் விழா` |
| 4 | `எம்மீது ஏவிய` | `எம் மீது எவிய` - retain the printed form rather than modernizing it |
| 4 | earlier draft `அந்தக் கணைகள்` | `அந்தக் கணைகளை` - current combined transcript already has this correction |
| 4 | earlier draft `வேல், வில் ஈட்டிகொண்டு` | `வேல், வில், ஈட்டிகொண்டு` - current combined transcript already has this correction |
| 4 | `குஷ்டரோகிப்` | `குஷ்ட ரோகிப்` |
| 4 | `மகாவிஷ்ணுவை` | `மகா விஷ்ணுவை` |
| 7 | earlier draft `தடையோட்ட` | `தடைபோட` - current combined transcript already has this correction |
| 7 | `நெரிக்கும்காட்சி` | `நெறிக்கும் காட்சி` |
| 7 | `கேள்விகேட்போம்` | `கேள்விகிளப்பினோம்` |

Printed pages 5 and 6 required no additional substantive correction in this stricter pass beyond corrections already incorporated by the preliminary sweep.

## Integration note

`transcription-ta.md` still contains some of the newly identified Batch 1 readings above. They will be integrated as part of the strict re-audit consolidation. Until that integration and the remaining page batches are complete, its earlier `verified` header/table should be regarded as **superseded by this audit log and `metadata.json`**.

## Next batch

PDF pages **9-13**, corresponding to printed pages **8-12**.

## Audit boundary

This audit does **not** infer a speech date, venue, or event. The supplied booklet itself does not establish those fields in the examined front matter, so they remain `null` pending independent source evidence.
