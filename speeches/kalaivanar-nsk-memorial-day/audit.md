# கலைவாணர் நினைவு நாள் விழா உரை — audio fidelity audit

**Source:** `05.Kalaivanar N.S.Krishnan Ninnaivu Naal Vizha vil Kalaigar Speech.mp3`  
**Source SHA-256:** `7457004d3c3ee87722edfe6814e830d3521b834dcf29b4de45bb7174a2278148`  
**Duration:** 00:07:22.549  
**Audit status:** **Textual precheck complete — 12/12; machine-aided auditory pre-audit complete for segments 1–3; strict direct-listening audit 0/12**

## Current state

Source inspection and technical provenance are complete. A complete T1 first-pass Tamil transcript covers the available recording from 00:00 through the abrupt ending at 07:22.549.

Preparatory textual prechecks are complete for all 12 segments. A checksum-verified machine-aided auditory pre-audit has also been completed for the opening through approximately 01:30. This produced one source-supported archival correction: the first four navigation boundaries were too early and have been corrected to approximately `00:00`, `00:18`, `00:55`, and `01:11`.

The machine evidence supports the structure and phonetic substance of the opening but does not reliably resolve every Tamil inflection, the first addressee, audience reactions, or other fine-grained details. The Tamil wording therefore remains **not source-verified**, and English translation remains blocked.

## Records

Textual prechecks:

- `t2-batches/batch-01-00-00-01-06-precheck.md`
- `t2-batches/batch-02-01-06-03-15-precheck.md`
- `t2-batches/batch-03-03-15-05-42-precheck.md`
- `t2-batches/batch-04-05-42-07-22-precheck.md`

Machine-aided audio evidence:

- `t2-batches/batch-05-machine-audio-evidence-00-00-01-30.md`

## Audit method

- Treat the MP3 as authoritative; ASR and surfaced text are aids only.
- Verify source identity by SHA-256 before processing.
- Use multiple independent model passes and raw/enhanced audio only to identify likely wording and boundaries.
- Do not promote a machine reading when models disagree or confidence is inadequate.
- Replay every segment directly before marking strict T2 complete.
- Preserve spoken forms instead of silently regularizing them.
- Preserve the abrupt ending; do not infer the missing continuation.

## Segment progress

| Segment | Corrected navigation range | Status |
|---:|---:|---|
| 1 | 00:00–00:18 | textual precheck and machine-aided auditory pre-audit complete; strict direct-listening verification pending |
| 2 | 00:18–00:55 | textual precheck and machine-aided auditory pre-audit complete; strict direct-listening verification pending |
| 3 | 00:55–01:11 | textual precheck and machine-aided auditory pre-audit complete; strict direct-listening verification pending |
| 4 | 01:11–02:21 | opening boundary machine-corrected; wording verification pending |
| 5 | 02:21–02:51 | textual precheck complete; auditory verification pending |
| 6 | 02:51–03:15 | textual precheck complete; auditory verification pending |
| 7 | 03:15–04:00 | textual precheck complete; auditory verification pending |
| 8 | 04:00–04:44 | textual precheck complete; auditory verification pending |
| 9 | 04:44–05:42 | textual precheck complete; auditory verification pending |
| 10 | 05:42–06:02 | textual precheck complete; auditory verification pending |
| 11 | 06:02–06:53 | textual precheck complete; auditory verification pending |
| 12 | 06:53–07:22.549 | textual precheck complete; auditory verification pending |

Strictly direct-listening-verified segments: **0 / 12**.  
Machine-aided auditory pre-audit: **3 / 12**.  
Textually prechecked segments: **12 / 12**.

## Machine-aided opening findings

Three independent checksum-verified GitHub Actions runs were used:

1. multilingual Whisper `small` and `medium` on `00:00–01:06`;
2. multilingual Whisper `large-v3-turbo` on raw and speech-enhanced `00:00–01:06`;
3. multilingual Whisper `large-v3-turbo` on raw and speech-enhanced `00:45–01:30`, with silence detection.

The stronger passes support the opening sequence in substance:

- `கலைவாணர் நினைவுக் குழுவின் தலைவர்`;
- an `அருமை நண்பர் ... அவர்களே` first addressee;
- `அருமை நண்பர் சின்ன அண்ணாமலை அவர்களே`;
- `கலையுலகப் பெருமக்களே, தாய்மார்களே, நண்பர்களே`;
- the annual memorial-function paragraph;
- the gratitude sentence.

The models do not reliably decode the first personal name. Their approximate phonetic outputs are compatible with the provisional `[ஏ. எல். சீனிவாசன்?]`, but not strong enough to remove the uncertainty marker.

The extended run establishes that the gratitude sentence continues beyond the old provisional `01:06` boundary. It ends at approximately `01:10`, followed by a meaningful pause, and `கலைவாணருடைய குடும்பம்...` begins at approximately `01:11`. The canonical transcript and time map have therefore been corrected without altering the Tamil wording.

## Textual precheck findings

### Segments 1–3

1. The surfaced transcript supports the provisional opening identification `ஏ. எல். சீனிவாசன்`, but the uncertainty marker remains.
2. The memorial-event and gratitude sentences agree in substance across T1, surfaced text, and machine-audio evidence.
3. The exact spoken form around `மெத்த உணர்ச்சிப் பெருக்கோடும்` remains unresolved.
4. No audience reaction, overlapping voice, or exact pause pattern has yet been certified by direct listening.

### Segments 4–6

1. The `கலைக்குடும்பம்` passage agrees in substance.
2. Differences such as `நலிந்து போகின்ற` / `நலிந்துபோகின்ற` and `பெரு மதிப்புக்கு` / `பெருமதிப்பிற்கு` are textual presentation differences, not audio evidence.
3. The Udumalai Narayana Kavirayar passage agrees in substance, including `பொன்னாடை`, `பொற்கிழி`, and the amount described as more than approximately fifteen thousand rupees.
4. `கலைவாணரோடிருந்து`, `பொற்கிழியும்`, the exact amount, and `பணமுடிப்பும்` require replay.
5. The former hall names and complete renaming sentence require listening confirmation.

### Segments 7–9

1. The construction passage agrees in substance, including `சற்றொப்ப இருபத்தைந்து இலட்ச ரூபாய்`.
2. The 03:15 naming clause remains unresolved: T1 has `[ஏற்றிவைக்கப்பட்டது?]`, while the surfaced layer appears as `ஏற்க வைக்கப்பட்டது`. Neither is authoritative.
3. The `அப்துல் சமது` passage and objection to changing `பாலர் அரங்கம்` agree in substance.
4. The Tirukutralam hall-naming passage agrees in substance, but its exact spoken constructions require replay.

### Segments 10–12

1. The repeated `தேவையை நிறைவு செய்கின்ற அளவிற்கு` construction is supported in substance; exact sandhi and pauses remain unverified.
2. The memorial-gift passage agrees in argument: the amount may be small, but the emotional value is large.
3. T1 has `வள்ளல் தன்மையோடு`; the surfaced layer appears to contain a `வள்ளல் பண்மையோடு`-type reading. This remains unresolved.
4. The recipient names appear as `தங்கப்பன்`, `பகவதி`, and `வெங்கடாசலம்`; exact pronunciation and honorifics remain unverified.
5. The recording boundary is correctly preserved as unfinished; no continuation has been supplied.

## Open readings requiring direct replay

1. **00:00:** opening title/name sequence and `[ஏ. எல். சீனிவாசன்?]`.
2. **00:18:** exact spoken form around `மெத்த உணர்ச்சிப் பெருக்கோடும்` and `பேரார்வத்தோடும்`.
3. **00:55–01:11:** every inflection in the gratitude sentence and the exact pause before `கலைவாணருடைய குடும்பம்`.
4. **01:11:** exact joins and case endings in the long `கலைக்குடும்பம்` passage.
5. **02:21:** `கலைவாணரோடிருந்து`, `உடுமலை நாராயணக் கவிராயர்`, `பொற்கிழியும்`, `பதினைந்தாயிரம் ரூபாய்க்குமேல்`, and `பணமுடிப்பும்`.
6. **02:51:** exact former hall names and the complete renaming sentence.
7. **03:15:** amount and naming verb represented by T1 `[ஏற்றிவைக்கப்பட்டது?]` / surfaced `ஏற்க வைக்கப்பட்டது`.
8. **04:00:** `அப்துல் சமது` and the old-name objection.
9. **04:44:** the complete Tirukutralam ministerial/naming passage.
10. **06:02:** `வள்ளல் தன்மையோடு` / surfaced `வள்ளல் பண்மையோடு`-type reading, `இயலாவிட்டாலும்`, and `பொற்கிழியினை`.
11. **06:53:** exact names and honorifics for `தங்கப்பன்`, `பகவதி`, and `வெங்கடாசலம்`, plus `அதைப்போலவே` / `அதே போலவே`.
12. Whether audience reactions or other voices should be represented anywhere in the recording.

## Source-boundary finding

The recording ends during the unfinished clause:

> `...வெங்கடாசலம் அவர்கள் எத்தகைய நிலையிலே இருக்கிறார் என்பதையும்—`

This is an archival source limitation, not a transcription omission. The archive must not reconstruct what followed in the original live speech.

## Exact next activity

Perform direct word-by-word listening verification of the corrected opening window **00:00–01:11**.

Confirm the first addressee, exact inflections in the memorial and gratitude paragraphs, audience/background sounds, and the pause before segment 4. Only after that direct comparison may segments 1–3 be marked strict-verified and the strict counter advance from 0 to 3.