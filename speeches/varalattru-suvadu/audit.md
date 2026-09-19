# வரலாற்றுச் சுவடு — Tamil source audit

**Source:** `TVA_BOK_0065598_வரலாற்றுச்_சுவடு.pdf`  
**SHA-256:** `f96525a5a3867985856764d02f8dabd9bef4e110076ddbf4e995113e474c51bf`

## Current audit state

This speech was initially misrouted to `pugazg/kalaignar-essays`. That intake has been removed. The source and verified first-pass work are now under the correct repository: `pugazg/kalaignar-public-speeches`.

## Source boundary

- PDF 4–25 — canonical speech body, **22 pages**
- PDF 26–33 — separate non-speech letter/article; outside speech body
- speech event printed on PDF 4 — Madurai American College student-union inaugural function
- printed speech date — **not stated**
- handwritten `1.9.1975` — physical-copy mark only

## First-pass transcription progress

PDF pages **4–10 — 7/22 speech pages transcribed and source-checked**.

Important durable readings:

| PDF | Earlier / provisional | Source-supported reading / action |
|---:|---|---|
| 4 | descriptor omitted `தலைவர்` | restore **`தலைவர் கலைஞர்`** |
| 5 | `வினக் குறிக்கு` / `வினைக் குறிக்கு` | **`வினாக் குறிக்கு`** — historical `னா` identity |
| 8 | semantic-normalized alternatives | retain source **`மாண்டுமறைந்தது`** |
| 9 | normalized wording | retain source **`பக்கவில்`**, **`இவைகளே அன்னியில்`** pending later strict gate |
| 10 | inferred printed folio 9 | **no visible printed folio; do not infer** |

Cross-page controls:

- PDF 4 **`மாண்பைக்`** → PDF 5 **`குறிக்கின்ற ஒன்று!`**
- PDF 5 **`பேரவை`** → PDF 6 **`தொடக்க விழாவுக்கு...`**
- PDF 8 **`மாநாட்டில்`** → PDF 9 **`முதறிஞர் ராஜாஜி...`**
- PDF 9 **`வரலாறும்—`** → PDF 10 **`வெள்ளையரை எதிர்த்த...`**
- PDF 10 ends **`விடுதலையை மட்டும்`** → continuation pending PDF 11

## Historical-glyph policy

`HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` is mandatory. Old shape is not read by modern visual resemblance. Character identity must be established before Unicode encoding. Never global-replace.

## Gate discipline

The direct source checks already performed are part of the **first-pass transcription layer** after migration. The repository's independent strict Tamil visual-audit gate remains **not started** and must later re-read all 22 speech pages before Tamil can be frozen.

## Next

Transcribe/source-check **PDF pages 11–20**. Do not begin English.
