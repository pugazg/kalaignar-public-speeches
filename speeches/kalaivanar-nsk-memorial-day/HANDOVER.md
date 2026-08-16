# Handover — Kalaivanar N. S. Krishnan Memorial-Day Speech

## Repository and path

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech path: `speeches/kalaivanar-nsk-memorial-day/`
- Audio-specific procedure: root `AUDIO_SPEECH_PROCESSING_GUIDE.md`
- General procedure: root `SPEECH_PROCESSING_GUIDE.md`

## Controlling source

- Filename: `05.Kalaivanar N.S.Krishnan Ninnaivu Naal Vizha vil Kalaigar Speech.mp3`
- Source URL: `https://tamildigitallibrary.in/kalaignar/audio/05.Kalaivanar%20N.S.Krishnan%20Ninnaivu%20Naal%20Vizha%20vil%20Kalaigar%20Speech.mp3`
- SHA-256: `7457004d3c3ee87722edfe6814e830d3521b834dcf29b4de45bb7174a2278148`
- Size: 7,087,106 bytes
- Duration: 442.549250 seconds / 00:07:22.549
- Format: MP3, stereo, 44.1 kHz, approximately 128 kb/s
- Binary committed: No

The MP3 is authoritative. The filename, surfaced transcript, machine-ASR outputs, and outside historical sources are aids only.

## Source findings

- Speaker: மு. கருணாநிதி.
- Event stated in speech: annual `கலைவாணர் நினைவு நாள் விழா`.
- Speech date: not stated.
- Venue: strongly indicated by the spoken content as the Chennai Kalaivanar Arangam, but remains provisional until strict auditory verification.
- Recording boundary: the file ends abruptly during a sentence about actor வெங்கடாசலம். Do not reconstruct the continuation.

## Workflow state

### Source inspection — COMPLETE

Checksum, file size, duration, codec, stream details, URL, embedded-file metadata, and recording-boundary condition are recorded.

### T1 Tamil first pass — COMPLETE

`transcription-ta.md` covers all 12 time segments from 00:00 through 07:22.549. The Tamil wording remains provisional pending strict auditory verification.

### Textual precheck — COMPLETE FOR ALL 12 SEGMENTS

Completed records:

- `t2-batches/batch-01-00-00-01-06-precheck.md`
- `t2-batches/batch-02-01-06-03-15-precheck.md`
- `t2-batches/batch-03-03-15-05-42-precheck.md`
- `t2-batches/batch-04-05-42-07-22-precheck.md`

Cumulative result:

- textually prechecked: **12/12 segments**;
- no Tamil wording has been promoted as source-verified from the surfaced transcript;
- textual precheck is preparation only.

### Machine-aided auditory pre-audit — SEGMENTS 1–3 COMPLETE

Record:

- `t2-batches/batch-05-machine-audio-evidence-00-00-01-30.md`

Three checksum-verified GitHub Actions runs independently downloaded the public source and processed it without committing the MP3:

1. multilingual Whisper `small` and `medium` on 00:00–01:06;
2. multilingual Whisper `large-v3-turbo` on raw and speech-enhanced 00:00–01:06;
3. multilingual Whisper `large-v3-turbo` on raw and speech-enhanced 00:45–01:30, with silence detection.

Important result:

- the old opening boundaries `00:20`, `00:50`, and `01:06` were too early;
- the corrected approximate navigation markers are `00:18`, `00:55`, and `01:11`;
- the gratitude sentence continues beyond 01:06 and ends around 01:10;
- `கலைவாணருடைய குடும்பம்...` begins around 01:11 after a meaningful pause.

These boundary corrections have been consolidated into:

- `transcription-ta.md`;
- `metadata.json`;
- `audit.md`;
- `README.md`.

No Tamil wording correction was authorized. The models support the opening structure and phonetic substance but do not reliably resolve every inflection or the first addressee.

### Secondary chronology research — COMPLETE

Record:

- `research/chronology.md`

Findings:

- the earlier Balar Arangam event recalled by the speaker occurred on **4 September 1971**;
- Udumalai Narayana Kavirayar received a ₹15,000 gold purse and Kalaignar announced the Kalaivanar Arangam name at that earlier event;
- the renovated Kalaivanar Arangam was inaugurated on **29 January 1974**;
- the Tamil Digital Library catalogue lists the present memorial-day speech separately from the hall-opening speech.

Safeguard:

- **4 September 1971 is not the date of the present recording**;
- the present recording is cautiously treated as likely **29 January 1974 or later**;
- the exact date remains unknown and `speech.date` remains `null`.

### Strict direct-listening T2 — NOT STARTED

- Strictly direct-listening-verified: **0/12 segments**.
- Machine-aided auditory pre-audit: **3/12 segments**.
- Textually prechecked: **12/12 segments**.
- The Tamil layer is not verified or frozen.

Do not equate model agreement with strict human/direct listening. In particular, the first addressee remains `[ஏ. எல். சீனிவாசன்?]`, and exact inflections in the memorial and gratitude paragraphs remain unresolved.

### T3 Tamil consolidation/freeze — BLOCKED

Do not freeze until all 12 segments pass strict direct-listening comparison and all confirmed corrections are consolidated.

### English — BLOCKED

Do not begin English translation until Tamil is `verified-complete`.

## Corrected opening map

| Segment | Corrected approximate range | Current state |
|---:|---|---|
| 1 | 00:00–00:18 | machine pre-audited; first name and wording verification pending |
| 2 | 00:18–00:55 | machine pre-audited; exact inflections pending |
| 3 | 00:55–01:11 | machine pre-audited; exact inflections pending |
| 4 | begins 01:11 | boundary corrected; wording verification pending |

## Exact next activity

Perform strict direct-listening verification of **00:00–01:11**:

1. verify the opening title/name sequence and `[ஏ. எல். சீனிவாசன்?]`;
2. verify `மெத்த உணர்ச்சிப் பெருக்கோடும்` and `பேரார்வத்தோடும்`;
3. verify the memorial-event and gratitude sentences word by word;
4. verify the pause and transition at approximately 01:10–01:11;
5. identify audience reaction, overlap, background speech, or recording artefacts;
6. record every source-supported wording correction in `audit.md`;
7. consolidate confirmed corrections into `transcription-ta.md`;
8. advance `strict_audio_audit_segments_checked` to 3 only after all three segments pass.

## Safeguards

- Do not treat surfaced transcription, machine ASR, or textual prechecks as authoritative.
- Do not use secondary chronology to overwrite spoken wording.
- Do not set the speech date to 1971-09-04.
- Do not infer a date from the 2024 XMP metadata.
- Do not silently modernize spoken Tamil.
- Do not fill the truncated ending.
- Do not commit the MP3 unless repository policy is explicitly changed.
- Do not begin English before T2 and T3 are complete.
