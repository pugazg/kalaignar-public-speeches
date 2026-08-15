# Kalaignar Public Speeches — Audio Source Processing Guide

This guide supplements `SPEECH_PROCESSING_GUIDE.md` when the controlling source is an audio recording rather than a printed booklet or scan. The repository’s source-faithful principles and gate order remain unchanged; only the source-inspection and verification mechanics differ.

## 1. Controlling source

The supplied audio file is the controlling witness for its recording. A surfaced transcript, ASR output, filename, catalogue title, or outside edition may assist navigation but is never authoritative.

Do not silently modernize, regularize, complete, or improve spoken Tamil. Preserve source-supported:

- wording, repetitions, false starts, and rhetorical pauses;
- names, honorifics, numbers, and quoted expressions;
- colloquial or historically specific forms;
- meaningful audience reactions and speaker interruptions;
- abrupt starts, missing passages, damage, and truncated endings.

Editorial punctuation and paragraphing may be added for readability, but must not change the spoken meaning. State clearly that punctuation is editorial.

## 2. Source provenance

Record where available:

- source filename and original source URL;
- SHA-256 checksum and file size;
- duration to millisecond precision;
- codec, bitrate, sample rate, channel count, and channel layout;
- embedded metadata separately from event facts;
- whether the recording begins or ends abruptly;
- whether the source binary is committed.

Embedded creation or modification timestamps describe the digital file, not necessarily the speech date. Do not infer an event date from them.

**Repository policy:** source media binaries are not committed by default. Preserve identity through URL, filename, checksum, size, technical metadata, and a time map.

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

## 4. Tamil workflow for audio

### T1 — first-pass transcription

Transcribe the complete available recording in manageable time segments. Mark uncertain words instead of guessing. If the recording ends in the middle of a sentence, preserve the unfinished sentence and document the truncation.

### T2 — strict auditory fidelity audit

Replay every segment directly against the recording, preferably in 30–60 second batches. For each batch:

- verify every word, name, number, repetition, and quoted phrase;
- distinguish speech from noise, applause, cross-talk, or later editing;
- check segment boundaries for omitted or duplicated words;
- replace speculative ASR readings only when the audio supports a correction;
- log substantive changes and unresolved passages in `audit.md`.

A clean surfaced transcript is not evidence against the audio.

### T3 — consolidation and freeze

After every segment passes T2:

- consolidate all corrections into `transcription-ta.md`;
- recheck time-segment joins and the beginning/end of the file;
- search for superseded preliminary readings;
- confirm no audible speech segment is missing or duplicated;
- mark Tamil `verified-complete` only then.

## 5. Event facts

A filename or catalogue label may identify an event, but it does not by itself establish the date, venue, organizers, or audience. Record only what the audio or accompanying source record explicitly supports. Where spoken deictic wording strongly suggests a location, keep the identification provisional until the relevant passage passes T2.

## 6. English workflow

English translation remains blocked until the Tamil layer is `verified-complete`. Translate from the frozen Tamil transcript, retain timestamp correspondence, and perform the same independent fidelity review and final verification required by `SPEECH_PROCESSING_GUIDE.md`.
