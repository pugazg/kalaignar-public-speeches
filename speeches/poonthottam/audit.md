# பூந்தோட்டம் - visual fidelity audit

**Source:** `TVA_BOK_0065784_கலைஞரின்_பூந்தோட்டம்.pdf`  
**Source SHA-256:** `2a8bf5f6f42970ee95912f41662f9bc448581a5aaca15a55fee9b44ba20a4c52`  
**Startup inspection date:** 2026-08-14  
**Speech-body scope:** PDF pages 6-17 / printed pages 5-16

## Current audit state

Source inspection is complete. Stage **T1 first-pass Tamil transcription is complete: 12 / 12 speech pages drafted**.

Stage **T2 strict line-by-line visual fidelity audit is in progress: 10 / 12 speech pages checked**. Audit Batch 1 covered PDF pages 6-10 / printed pages 5-9. Audit Batch 2 covered PDF pages 11-15 / printed pages 10-14 by a fresh line-by-line comparison against the scan. Only PDF pages 16-17 / printed pages 15-16 remain unaudited.

## Source / page-map safeguards

- PDF 6-17 are the canonical speech body, printed pages 5-16.
- The scan, not OCR or parsed text, is authoritative.
- Preserve historical/source spelling, punctuation, spacing where meaningful, unusual grammar, repetition, and typography.
- Running headers, reverse-side bleed-through, and later library stamps are not speech text.
- PDF 17 has a large blue library stamp below the printed `வணக்கம்`; it remains excluded from transcription.

## T1 first-pass progress

| T1 batch | PDF pages | Printed pages | Status |
|---|---:|---:|---|
| 1 | 6-10 | 5-9 | drafted |
| 2 | 11-15 | 10-14 | drafted |
| 3 | 16-17 | 15-16 | drafted |

T1 drafted pages: **12 / 12 - first-pass-complete**.

## T2 strict audit progress

| T2 batch | PDF pages | Printed pages | Status |
|---|---:|---:|---|
| 1 | 6-10 | 5-9 | **re-audited** |
| 2 | 11-15 | 10-14 | **re-audited** |
| 3 | 16-17 | 15-16 | not-started |

Strictly re-audited pages: **10 / 12**.

### T2 Batch 1 - PDF 6-10 / printed 5-9

Every line of these five pages was compared again against the rendered scan pages. The first-pass transcription was found to be substantively faithful across the batch, so **no wording correction was required in `transcription-ta.md` during this batch**.

Confirmed scan readings include `பரவசத்திலீடுபடுகிறான்`, `அகம்புற மென்ற அன்றலர்ந்த`, `சீர் குலுங்கும்`, the first highlighted joined `அந்தக்காலம்`, `அயோத்தியானுக்கு`, and `பாராளப் பிறந்த ராமனின்`. Page continuations `பண்படுத்த` → `வேண்டும்.` and `...மொண்டு மொண்டு தரும்` → `தென்றலாக, ...` were also confirmed.

### T2 Batch 2 - PDF 11-15 / printed 10-14

Every line of these five pages was independently re-read against the scan and compared with the existing first-pass transcription. **No scan-confirmed wording correction was required in `transcription-ta.md` in this batch.**

The following T1 watchpoints were deliberately rechecked and confirmed from the scan:

- printed p.10 retains the source form `தண்ட காரணயத்திலே`;
- printed p.10 reads `வைத்தே இருக்குமிடத்தை`;
- printed p.10 reads `மிதிலாபுரிக்கு ஜனகனுக்கு` and uses `‘டிரங்கால்’`;
- printed p.10 retains `‘ரிஸ்ட் வாட்ச்’` and the sequence `“பஜகோவிந்த” மா`;
- printed p.10 → p.11 continues the sentence from `வேலைகளை விட்டு ஓய்வு` to `பெறுகிறவர் ...`;
- printed p.11 retains `பகுத்தறிவு புரியினருக்கும், பழமைத் தீவினருக்கும்`;
- printed p.11 retains the spacing `சொந்த மென்றான்`;
- printed p.12 clearly supports the unusual first-pass reading `எப்படி பெய்ப்படி மாலை தொடுக்க முடியும்`;
- printed p.13 reads `வழக்கு மன்றத்திற்கு`;
- printed p.14 retains `பாமர நிலையவிட்டுக்`, `தன் தனிப் பெருமை யிழந்து`, and `சொல்லே யில்லாத`;
- printed p.14 reads `காரைக்காலம்மை`;
- running headers and visible reverse-side bleed-through on these pages were excluded from the speech transcription.

Punctuation, quotation structure, rhetorical exclamation marks, names, and page boundaries on printed pp.10-14 were also checked against the scan and found aligned with the current transcription.

### Remaining T2 watchpoints - PDF 16-17 / printed 15-16

Recheck especially:

- `தாயைக் கட்டிலறைக் கழைத்து`;
- `வைகைக் கரையிலே`;
- `மோட்சலோக ‘பாஸ்போர்ட்’டன்`;
- separate `கை முஷ்டி` and joined `கைமுஷ்டி`;
- `பூர்ஷ்வாத் தன்மை`;
- first-pass `புரிவோடு`;
- p.15 → p.16 thought continuation;
- `அப்படி நடைபோடும் நல்லதம்பிகளைத்தான்`;
- printed final `வணக்கம்` versus the later blue library stamp below it.

## T1 / T2 / T3 state

| Stage | Pages | Status |
|---|---:|---|
| T1 first-pass Tamil transcription | 12 / 12 | first-pass-complete |
| T2 strict visual fidelity audit | 10 / 12 | in-progress |
| T3 consolidation / page-boundary / stale-reading check | - | blocked |

## Exact next gate

Continue **T2 strict visual fidelity audit** with the final batch: **PDF pages 16-17 / printed pages 15-16**. Compare every line independently against the scan, apply only scan-confirmed corrections to `transcription-ta.md`, and record substantive findings here.

Do not begin English translation after T2 Batch 3. First run the separate T3 consolidation, page-boundary and stale-reading check across the complete Tamil layer and freeze it as `verified-complete` only if that gate passes.
