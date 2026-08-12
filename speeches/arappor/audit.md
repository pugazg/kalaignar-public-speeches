# அறப்போர் - visual fidelity audit

**Source:** `TVA_BOK_0064122_அறப்போர்.pdf`  
**Source SHA-256:** `8172cf4f04e804ebbcfe1b1e236c9d41bda2e07377952c162be4e4bb098ce01c`  
**Audit date:** 2026-08-12  
**Scope:** PDF pages 4-20, corresponding to printed pages 3-19

## Method

Every speech-body page was visually compared with `transcription-ta.md`. The audit is a **text-fidelity check**, not a historical fact-check. Printed wording, historical spelling, punctuation, names, and unusual/possibly erroneous source forms are retained when supported by the scan. The transcription joins printer line-wraps for readability while preserving page and paragraph boundaries.

## Result

- Speech pages checked: **17 / 17**
- Tamil transcription status: **verified complete**
- Remaining explicitly uncertain readings: **0**
- English translation: **unblocked; not started**

## Corrections made during visual audit

| PDF page | Printed page | First-pass reading | Verified source reading / action |
|---:|---:|---|---|
| 4 | 3 | `மற்றுக் கட்சியினர்` | `மாற்றுக் கட்சியினர்` |
| 5 | 4 | `கோல் விழா` | `கால்கோள் விழா` |
| 5 | 4 | `அந்தக் கணைகள்` | `அந்தக் கணைகளை` |
| 5 | 4 | `வேல், வில் ஈட்டிகொண்டு` | `வேல், வில், ஈட்டிகொண்டு` |
| 8 | 7 | `தடையோட்ட` | `தடைபோட` |
| 10 | 9 | `⟦திலகுப்புற?⟧` | `தலைகுப்புற` |
| 13 | 12 | `சோற்றுலவித்த` | `சோற்றுவலித்த` |
| 15 | 14 | `⟦ஜமீனேடு?⟧` | `ஜமீனோடு` |
| 15 | 14 | `இனுங்கலோடு` | `இனும்களோடு` |
| 15 | 14 | `ஈரோட்டில் நான் குறித்திருப்போம்` | `ஈரோட்டில் நாள் குறித்திருப்போம்` |
| 15 | 14 | `⟦சிலை?⟧` | `சிலை` - unusual form retained because it is what the scan prints |
| 15 | 14 | `பெட்டியில்வாய்ப் பெட்டி திறந்து` | `பெட்டியில்பாய்—பெட்டி திறந்து` |
| 16 | 15 | `நாலுவயது குழந்தை` | `நாலுவயதுக் குழந்தை` |
| 16 | 15 | `பரிதாபப்பட்டதை` | `பரிதாபப்படலத்தை` |
| 17 | 16 | `வேண்டும் மென்` | `வேண்டுமென` after joining the printer line-wrap |
| 17 | 16 | `போரை விரும்பமாட்டோம்;` | `போரை விரும்பமாட்டோம்:` |
| 18 | 17 | `மாநாடு செய்திகள்` | `மாநாடு செய்திகளை` |
| 19 | 18 | five instances of `தவறா?` | source prints `தவறு?`; all five restored |
| 20 | 19 | `⟦மண்ணுக்கு?⟧` | `மக்களுக்கு` |

## Source-damage / annotation note

On printed p. 19 (PDF p. 20), a later blue/ink annotation crosses part of the word `மக்களுக்கு` in the first line. The annotation is not part of the printed edition. Enough of the underlying printed glyphs remains visible to recover the reading, so the earlier uncertainty marker has been removed.

## Audit boundary

This audit does **not** infer a speech date, venue, or event. The supplied booklet itself does not establish those fields in the examined front matter, so they remain `null` in `metadata.json` pending independent source evidence.
