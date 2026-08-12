# அறப்போர் - visual fidelity audit

**Source:** `TVA_BOK_0064122_அறப்போர்.pdf`  
**Source SHA-256:** `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`  
**Audit date:** 2026-08-12  
**Scope:** PDF pages 4-20, corresponding to printed pages 3-19

## Important audit state

The earlier whole-document sweep has been **re-opened** for a stricter line-by-line fidelity pass. The strict pass has continued to find source/transcription discrepancies that the preliminary sweep missed. Therefore the Tamil text must **not** yet be treated as final/canonical, and English translation remains blocked until this stricter pass is complete.

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
| 2 | 9-13 | 8-12 | re-audited |
| 3 | 14-18 | 13-17 | pending |
| 4 | 19-20 | 18-19 | pending |

Strictly re-audited pages: **10 / 17**.

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

## Batch 2 findings - PDF pages 9-13 / printed pages 8-12

The second five-page strict comparison found the following additional discrepancies:

| Printed page | Existing reading | Scan-supported reading / action |
|---:|---|---|
| 8 | `எங்கே உத்தரவு` | `எங்கே உத்திரவு` |
| 9 | `இந்துவும் மந்திரனும்` | `இந்துவும் மித்திரனும்` |
| 9 | quoted: `இரண்டாம் மொழிக்கு மட்டும் கட்டாயம்` | quoted: `இரண்டாம் மொழிக்கும்தான் கட்டாயம்` |
| 11 | first analogy ends `இருப்பதுபோல்` | source ends `இருப்பதுபோல்!` |
| 11 | second analogy ends `போல்` | source ends `போல்!` |
| 11 | `ஏற்றதுதானா?` | `ஏற்றதுதானு?` - retain the printed colloquial/source form |
| 11 | `சிவசிந்தாமணியைக்` | `சிவகசிந்தாமணியைக்` - retain the booklet's printed form |
| 11 | `பிசிராந்தையும்நாட்டுக்கு` | `பிசிராந்தையும்—நாட்டுக்கு` |
| 12 | `தேசயத்திரா விட்டோரே!` | `தேசியத்திராவிடரே!` - the word is split across printer lines in the scan and is joined here |
| 12 | `குரல்வளையை கிழிபடாமலிருந்தால்` | `குரல்வளையைக் கிழிபடாமலிருந்தால்` |

Printed page 10 required **no additional substantive correction** in this strict pass.

The page-9 quotation was checked against the damaged but still legible print. The substantive wording is `இரண்டாம் மொழிக்கும்தான் கட்டாயம்`; this must not be normalized to the semantically different `இரண்டாம் மொழிக்கு மட்டும் கட்டாயம்`.

## Integration note

`transcription-ta.md` still contains some readings superseded by Batch 1 and Batch 2 findings. They will be integrated as part of the strict re-audit consolidation. Until that integration and the remaining page batches are complete, its earlier `verified` header/table should be regarded as **superseded by this audit log and `metadata.json`**.

## Next batch

PDF pages **14-18**, corresponding to printed pages **13-17**.

## Audit boundary

This audit does **not** infer a speech date, venue, or event. The supplied booklet itself does not establish those fields in the examined front matter, so they remain `null` pending independent source evidence.
