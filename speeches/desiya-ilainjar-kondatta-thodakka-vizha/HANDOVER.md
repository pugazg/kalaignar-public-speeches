# HANDOVER — தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/desiya-ilainjar-kondatta-thodakka-vizha/`
- Parent collection: `collections/muthukkuliyal-part-2/`

## Controlling source

- Filename: `TVA_BOK_0065802_முத்துக்குளியல்_பாகம்_2.pdf`
- SHA-256: `48631b4fc5258df33213dbb742aec70ff6aace4fcd294f377e5750b406f5d9b2`
- Byte size: `232,470,104`
- Complete PDF scans: **425**
- Constituent range: PDF **12–18** / printed **11–17**
- Source binary committed: **No**

## Source-supported event facts

The separate closing note on PDF 18 / printed p.17 states:

`12-1-98 அன்று சென்னை ஜவகர்லால் நேரு விளையாட்டரங்கில் தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழாவில் தலைமை உரை`

Therefore:

- date: **1998-01-12**;
- venue: **சென்னை ஜவகர்லால் நேரு விளையாட்டரங்கம்**;
- event: **தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா**;
- role: **தலைமை உரை**.

Do not confuse the parent volume's June 2000 publication date with this speech date.

## Durable workflow state

- duplicate check: **PASS — no existing matching speech tree**;
- constituent source intake/boundaries: **PASS / COMPLETE**;
- Tamil T1: **COMPLETE — 7 / 7 pages**;
- Tamil T2 strict visual audit: **PASS / COMPLETE — 7 / 7**;
- T2 substantive corrections: **5**;
- T2 unresolved readings: **0**;
- Tamil T3 consolidation/freeze: **PASS / COMPLETE**;
- Tamil status: **`verified-complete`**;
- English E1: **COMPLETE — 7 / 7 pages**;
- English E2 fidelity review: **READY / NOT STARTED — 0 / 7**;
- English E3 final verification: **BLOCKED / NOT STARTED**.

## Tamil source-fidelity resolutions

Five first-pass readings were corrected from direct scan evidence:

1. `தங்கள் சொந்த நாடாகக் கொள்வர்` → `தங்கள் சொந்த நாடாக்கிக் கொள்வர்`;
2. `அர்ஜுனனை` → `அர்ஜூனனை`;
3. `அர்ஜுனன்` → `அர்ஜூனன்`;
4. `இந்தியர் கனிவை` → `இந்தியர்களிடையே` from the source line-wrap `இந்தியர்` / `களிடையே`;
5. `சமாதானத் திறக்கும்` → `சமாதானத்திற்கும்` from the source line-wrap `சமாதானத்` / `திற்கும்`.

Directly confirmed and retained:

- unusual printed p.13 `ஐக்கிய இந்தியர் மீது`;
- printed p.15 `அளிக்கப்படாவிட்டாலும் நீடித்த நட்புறவைச் சாதிக்க முடியாது`;
- the source's repeated p.15 `ஆக்கபூர்வ நடவடிக்கைகளில்` / `ஏழைகளின் நலனை மேம்படுத்த...` sequence;
- `இருபத்தையாயிரத்துக்கு` as the proper join of `இருபத்தையாயிரத்` / `துக்கு`;
- quotation wording/spacing and all recorded numerals.

`transcription-ta.md` remains the canonical frozen Tamil layer. Any later Tamil change requires specific source evidence, an audit record, and reopening of dependent English work.

## English E1 checkpoint

`translation-en.md` now contains the complete first-pass English for all seven mapped pages, derived only from the frozen Tamil layer.

E1 preserved the page sequence, names, historical references, repeated source wording, numerical claims and the verified ending. It also translates the separate closing note as source metadata, clearly outside the speech body.

One item is explicitly flagged for E2 rather than silently resolved: verified printed p.13 `ஐக்கிய இந்தியர் மீது`. E1 gives a cautious readable rendering, “our commitment to a united India,” and records the exact Tamil in a source note. E2 must independently review that choice.

## Exact next incomplete gate

Perform **E2 independent Tamil→English fidelity review for all 7 pages, PDF 12–18 / printed 11–17**. Compare `translation-en.md` against frozen `transcription-ta.md`, record every omission/addition/reversal/source-transparency issue in `translation-review.md`, then consolidate confirmed corrections into the English translation. E3 remains blocked until E2 is fully resolved.
