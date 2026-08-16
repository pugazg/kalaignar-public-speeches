# Learnings — Kalaivanar N. S. Krishnan Memorial-Day Audio Archive

## Purpose

This document records the technical, editorial and workflow lessons learned while processing the Kalaivanar memorial-day speech audio. It is intended to prevent the same failures from recurring in this repository or in future Kalaignar audio archives.

## What happened

The project initially progressed through:

1. source provenance and checksum capture;
2. a surfaced-text-based Tamil first pass;
3. textual prechecks;
4. machine-aided opening checks;
5. a claimed full direct-listening audit.

The first claimed full audit incorrectly stopped the transcript after:

> `...வெங்கடாசலம் அவர்கள் எத்தகைய நிலையிலே இருக்கிறார் என்பதையும்—`

and classified the recording as ending abruptly. The repository owner correctly identified that approximately another 25 seconds of speech remained. A focused tail re-audit recovered the complete closing passage and established that the source does **not** end abruptly.

The controlling correction is documented in:

- `t2-batches/batch-07-tail-correction-06-53-07-23.md`

## Primary failure

The central failure was not merely a mistranscribed word. It was an unsupported **source-boundary conclusion** that was promoted into a verified archival state.

The false truncation finding then propagated into:

- `transcription-ta.md`;
- `audit.md`;
- `metadata.json`;
- `README.md`;
- `HANDOVER.md`;
- translation instructions;
- earlier T2 batch records.

This demonstrated that a wrong boundary judgment can contaminate every downstream layer even when the preceding text is substantially correct.

## Technical learnings

### 1. Verify the complete decoded duration

Do not rely on:

- a UI preview;
- a displayed waveform fragment;
- an earlier `ffprobe` result copied from another extraction;
- a model's final timestamp;
- a time map created before the full file is inspected.

Record the duration from the actual controlling binary and recheck it whenever the user reattaches the file. In this project, the corrected decoded duration is:

- `443.559` seconds;
- `00:07:23.559`.

### 2. Audit the final minute as an independent gate

Even after sequential whole-file playback, create a dedicated tail check:

- replay at least the final 60 seconds;
- replay the final 30 seconds separately;
- check for low-volume continuation after a pause;
- inspect whether speech continues beyond a model or provisional segment boundary;
- confirm that the final grammatical thought is complete or genuinely interrupted.

### 3. A pause is not an ending

A long rhetorical pause, a drop in volume, a model segmentation break or a display boundary must never be treated as proof that the recording has ended.

### 4. ASR is corroboration, not authority

Whisper and other ASR outputs were useful for:

- locating likely boundaries;
- surfacing candidate readings;
- identifying where to replay.

They were not reliable enough to determine every name, inflection or final source boundary. The MP3 remains authoritative.

### 5. Source identity must be reconfirmed

When a file is reattached, verify:

- filename;
- SHA-256;
- byte size;
- decoded duration;
- stream properties.

A matching checksum proves binary identity; it does not prove that the earlier interpretation of that binary was correct.

## Editorial learnings

### 1. Never claim direct listening that has not actually occurred

Textual comparison, ASR agreement and historical corroboration are not direct auditory verification. Each must have a separate status label.

Recommended distinctions:

- `textual-precheck`;
- `machine-aided-pre-audit`;
- `direct-listening-audit`;
- `tail-boundary-audit`;
- `verified-complete`.

### 2. Do not freeze Tamil until the beginning and end are rechecked

T3 consolidation must include:

- the first audible words;
- every segment join;
- the last full minute;
- the final audible word;
- the grammatical completeness of the ending.

### 3. Boundary claims require positive evidence

Before writing `recording ends abruptly`, the audit must state:

- the exact final audible words;
- the confirmed file duration;
- whether additional speech exists after the apparent cutoff;
- whether the final waveform/audio tail was replayed independently.

### 4. User correction is source-significant evidence

When the repository owner states that speech remains, do not defend the earlier audit. Reopen the source immediately, isolate the disputed range and treat the previous conclusion as untrusted until reverified.

### 5. Corrections must be explicit and superseding

When a verified claim is later found wrong:

- create a correction record;
- identify exactly what is superseded;
- retain valid earlier findings;
- update all dependent files;
- search for stale wording such as `abrupt`, `truncated`, `unfinished`, old duration values and obsolete translation instructions.

## Workflow learnings

### 1. Verification counters are not enough

A counter such as `12/12` can still hide an incomplete last segment. Completion requires both:

- all segments checked;
- full source coverage confirmed from first audible speech through the true file end.

### 2. Tail completeness must be machine-readable

Metadata should explicitly include:

- decoded duration;
- final segment end;
- `recording_truncated`;
- boundary verification status;
- controlling correction record when applicable.

### 3. Temporary automation must be removed

Temporary GitHub Actions workflows used for audio analysis should be deleted after their evidence is captured, so they do not remain as accidental permanent infrastructure.

### 4. English must depend on the latest frozen Tamil

If Tamil changes after being marked verified:

- English translation must be paused or reopened;
- any translated affected passage must be replaced;
- English review status must be reset as necessary;
- the restored Tamil must be translated in full.

## Translation-specific learning

The restored ending is not a minor appendix. It contains the speech's closing moral dedication: the small assistance given to struggling artists, if it brings even a measure of peace to their lives, is the offering Kalaignar places at Kalaivanar's feet.

Omitting that passage would remove the rhetorical and ethical conclusion of the speech. Future translations must therefore verify the source ending before attempting to interpret the speech's final argument.

## Permanent safeguards adopted

For every future audio source:

1. checksum and inspect the exact binary;
2. record the decoded duration from the complete file;
3. transcribe the full file before any verification claim;
4. distinguish textual, machine and direct-listening evidence;
5. audit all segment joins;
6. conduct a separate final-minute audit;
7. confirm whether the final sentence is complete;
8. search the repository for stale boundary claims before freezing Tamil;
9. begin English only from the latest verified Tamil;
10. reopen downstream gates whenever the Tamil source layer changes.

## Final lesson

Archival confidence must come from demonstrated source coverage, not from confident wording in a status file. A polished audit statement is not evidence. The evidence is the controlling source, completely inspected from beginning to true end, with every consequential decision traceable.