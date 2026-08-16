# Kalaignar Public Speeches — Audio Source Processing Guide

This guide supplements `SPEECH_PROCESSING_GUIDE.md` when the controlling source is an audio recording rather than a printed booklet or scan. The repository's source-faithful principles and gate order remain unchanged; only the source-inspection and verification mechanics differ.

## Mandatory companion documents

Before starting or continuing audio work, also read:

- `docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md`;
- the target speech's `HANDOVER.md`;
- any target-speech `LEARNINGS.md`.

For the principal cautionary example, read:

- `speeches/kalaivanar-nsk-memorial-day/LEARNINGS.md`.

The reusable startup prompt is:

- `docs/START_NEW_AUDIO_SPEECH_PROMPT.md`.

The future-audio guidelines are mandatory where they are more specific than this overview, particularly for evidence classification, true-duration verification, final-minute audit, correction supersession and downstream English resets.

## 1. Controlling source

The supplied audio file is the controlling witness for its recording. A surfaced transcript, ASR output, filename, catalogue title or outside edition may assist navigation but is never authoritative.

Do not silently modernize, regularize, complete or improve spoken Tamil. Preserve source-supported:

- wording, repetitions, false starts and rhetorical pauses;
- names, honorifics, numbers and quoted expressions;
- colloquial or historically specific forms;
- meaningful audience reactions and speaker interruptions;
- abrupt starts, missing passages, damage and genuinely truncated endings;
- complete closing passages when they exist.

Editorial punctuation and paragraphing may be added for readability, but must not change the spoken meaning. State clearly that punctuation is editorial.

## 2. Source provenance

Record where available:

- source filename and original source URL;
- SHA-256 checksum and file size;
- decoded duration from the complete controlling binary;
- codec, bitrate, sample rate, channel count and channel layout;
- embedded metadata separately from event facts;
- whether the recording begins or ends abruptly;
- whether the source binary is committed.

Embedded creation or modification timestamps describe the digital file, not necessarily the speech date. Do not infer an event date from them.

**Repository policy:** source media binaries are not committed by default. Preserve identity through URL, filename, checksum, size, technical metadata and a time map.

Whenever the source is reattached, recompute checksum, size and decoded duration. A matching checksum confirms source identity, not the correctness of an earlier interpretation.

## 3. Time map and canonical files

Use the normal directory:

```text
speeches/<speech-slug>/
```

Use the normal archival files:

```text
README.md
metadata.json
transcription-ta.md
audit.md
translation-en.md
translation-review.md
HANDOVER.md
```

For audio sources, timestamps replace PDF/printed-page headings. Use stable `HH:MM:SS` or `MM:SS` segment starts in `transcription-ta.md`. Timecodes are navigation markers; exact word-level timing is not required unless explicitly produced and audited.

Maintain separate status labels for:

- textual precheck;
- machine-aided audio pre-audit;
- strict direct-listening audit;
- beginning/end boundary verification.

Do not call textual or ASR comparison direct listening.

## 4. Tamil workflow for audio

### T1 — first-pass transcription

Transcribe the complete available recording in manageable time segments. Mark uncertain words instead of guessing.

T1 is not complete until transcription reaches the true decoded end of the controlling binary.

If the recording genuinely ends in the middle of a sentence, preserve the unfinished sentence and document the truncation. Do not infer truncation from a pause, preview, waveform display, model boundary or stale duration.

### T2 — strict auditory fidelity audit

Replay every segment directly against the recording, preferably in 30–60 second batches. For each batch:

- verify every word, name, number, repetition and quoted phrase;
- distinguish speech from noise, applause, cross-talk or later editing;
- check segment boundaries for omitted or duplicated words;
- replace speculative ASR readings only when the audio supports a correction;
- log substantive changes and unresolved passages in `audit.md`.

A clean surfaced transcript is not evidence against the audio.

### Mandatory opening verification

Independently confirm:

- first audible word;
- salutation/title sequence;
- first complete sentence;
- transition into the speech body.

### Mandatory final-minute verification

Before Tamil may be frozen:

1. replay at least the final 60 seconds;
2. replay the final 30 seconds separately;
3. replay from the final major pause through the true file end;
4. confirm the final audible word;
5. determine whether the final grammatical thought is complete;
6. compare the final segment end with the decoded duration;
7. record trailing silence, applause, music or edits.

Do not state that the source is truncated unless direct tail replay proves that speech is interrupted and no further speech follows.

### T3 — consolidation and freeze

After every segment, the opening and the final minute pass T2:

- consolidate all corrections into `transcription-ta.md`;
- recheck time-segment joins and the beginning/end of the file;
- search for superseded preliminary readings;
- search for stale duration and boundary claims, including `abrupt`, `truncated` and `unfinished`;
- confirm no audible speech segment is missing or duplicated;
- mark Tamil `verified-complete` only then.

## 5. Correction and supersession

When a previously verified source claim is found wrong:

1. reopen the disputed source range immediately;
2. create a correction record;
3. state what earlier conclusion is superseded;
4. retain unaffected valid findings;
5. update the canonical transcript, audit, metadata, README and handover;
6. search for stale claims throughout the repository;
7. reopen affected English stages;
8. remove temporary analysis workflows after evidence capture.

Do not silently rewrite the audit history.

## 6. Event facts

A filename or catalogue label may identify an event, but it does not by itself establish the date, venue, organizers or audience. Record only what the audio or accompanying source record explicitly supports. Where spoken deictic wording strongly suggests a location, keep the identification provisional until the relevant passage passes T2.

## 7. English workflow

English translation remains blocked until the latest Tamil layer is `verified-complete`. Translate from the frozen Tamil transcript, retain timestamp correspondence, and perform the same independent fidelity review and final verification required by `SPEECH_PROCESSING_GUIDE.md`.

If Tamil changes after English begins:

- identify affected English passages;
- reset translation/review states conservatively;
- translate the corrected Tamil;
- repeat fidelity review;
- repeat final end-to-end verification.

The English beginning and ending must be checked against the verified Tamil beginning and true complete ending.
