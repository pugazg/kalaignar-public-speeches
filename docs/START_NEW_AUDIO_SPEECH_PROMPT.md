# Prompt — Start or Continue a Kalaignar Audio Speech Archive

Copy the prompt below into a new chat and attach the controlling audio file.

---

Continue the Kalaignar Public Speeches archival project directly in:

`pugazg/kalaignar-public-speeches`

Work on `main`.

The controlling audio source is attached.

## Mandatory startup

Before making any change, read these repository files completely and follow them exactly:

1. `SPEECH_PROCESSING_GUIDE.md`
2. `AUDIO_SPEECH_PROCESSING_GUIDE.md`
3. `docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md`
4. root `README.md`
5. `speeches/kalaivanar-nsk-memorial-day/LEARNINGS.md` as the cautionary audio-work example

Study completed speech archives only as workflow references. Never use another speech as a textual source for the attached recording.

Inspect the repository first and determine whether the attached speech has already been started. Search by:

- catalogue/file title;
- likely Tamil title;
- speaker/event wording;
- source filename;
- checksum, if available;
- likely slug.

If work exists, continue it. Do not create a duplicate speech tree.

## Source authority

The attached audio file is the controlling source for this edition.

Do not rely on the filename alone. Do not silently modernise, correct, regularise, reconstruct or improve Kalaignar's spoken Tamil.

Preserve source-supported:

- wording and repetitions;
- historical or unusual spoken forms;
- names, initials and honorifics;
- dates, numbers and monetary amounts;
- rhetorical questions and parallel constructions;
- meaningful pauses, audience reactions and interruptions;
- the actual beginning and ending of the available recording.

Surfaced transcripts, subtitles, ASR, catalogue entries and outside historical sources are aids only. They are never authoritative over the attached media.

## Source inspection

Before creating metadata or a title:

1. inspect the actual attached file;
2. calculate SHA-256;
3. record byte size;
4. determine the full decoded duration from the complete binary;
5. record codec, sample rate, channels, channel layout and bitrate where available;
6. inspect embedded metadata, but keep it separate from event facts;
7. inspect both the opening and the true final minute;
8. determine whether the recording begins or ends abruptly only from direct evidence;
9. confirm whether the source is one complete speech, an extract or part of a longer recording.

Do not commit the media binary. Preserve identity through filename, URL, checksum, size, duration and technical metadata.

## Required speech directory

Use:

```text
speeches/<stable-slug>/
```

Required files:

```text
README.md
metadata.json
transcription-ta.md
audit.md
translation-en.md
translation-review.md
HANDOVER.md
t2-batches/
```

Create `LEARNINGS.md` when the work produces material reusable lessons. Create `research/` only for clearly separated contextual research.

## Tamil workflow

### T1 — complete first pass

Transcribe the complete available recording in manageable timestamped segments.

- Mark uncertainty rather than guessing.
- Preserve Kalaignar's wording and rhetoric.
- Treat punctuation, paragraphing, word spacing and timestamp headings as editorial aids.
- Do not mark T1 complete until the transcript reaches the true decoded end.
- Do not begin English.

### T2 — strict direct-listening audit

Replay every segment against the controlling audio.

For each segment verify:

- every word;
- names, initials and honorifics;
- numbers and amounts;
- repetitions;
- quotations;
- segment joins;
- audience/cross-talk/noise distinctions;
- the first and last audible words.

Keep separate status labels for:

- textual precheck;
- machine-aided pre-audit;
- direct-listening audit.

Never call textual or ASR comparison direct auditory verification.

### Mandatory final-minute gate

Before any `verified-complete` state:

1. replay at least the final 60 seconds;
2. replay the final 30 seconds separately;
3. replay from the final major pause through the true file end;
4. confirm the final audible word;
5. confirm whether the final thought is grammatically complete;
6. compare the final segment end with the decoded duration;
7. document trailing silence, applause, music or editing.

Do not claim truncation merely because a model stops, a preview ends, a pause occurs or a provisional boundary was reached.

### T3 — consolidation and freeze

After every segment, the opening and the final-minute gate pass:

- consolidate all corrections;
- verify no interval is missing or duplicated;
- search for stale names, amounts, timestamps, uncertainty markers and boundary claims;
- search specifically for stale `abrupt`, `truncated` and `unfinished` wording;
- synchronize `metadata.json`, `README.md`, `audit.md` and `HANDOVER.md`;
- mark Tamil `verified-complete` only when the complete source is represented.

Any later Tamil correction reopens dependent English work.

## Correction rule

If the repository owner identifies missing or incorrect source material:

- reopen the exact range immediately;
- do not defend the previous verified claim;
- create a superseding correction record;
- state what earlier conclusion was wrong;
- preserve unaffected valid findings;
- update every dependent file;
- reset English statuses where required;
- remove stale claims throughout the repository.

## English workflow

English begins only after the latest Tamil is frozen as `verified-complete`.

Translate only from `transcription-ta.md`.

Retain:

- Kalaignar's formal public-speaking voice;
- argument order;
- repetition and parallelism;
- metaphors and images;
- names and titles;
- hall/institution names;
- amounts;
- the verified complete or incomplete ending.

Stages:

1. E1 — complete first-pass translation in `translation-en.md`;
2. E2 — independent Tamil-to-English fidelity review in `translation-review.md`;
3. consolidate review corrections;
4. E3 — complete end-to-end Tamil-to-English verification.

Do not mark English verified merely because a translation exists.

## Metadata discipline

Use conservative, explicit states and counters. Status labels must agree with the actual files.

Track at minimum:

- source identity and decoded duration;
- time map;
- Tamil segments total/drafted/audited;
- direct-listening records;
- opening and ending verification;
- `recording_truncated` as true, false or unresolved;
- Tamil consolidation state;
- English translation, review and final-verification states.

## Temporary analysis workflows

When temporary GitHub Actions are used for ASR or audio processing:

- verify checksum inside the job;
- process only the required ranges;
- retain outputs only as secondary evidence;
- do not commit media;
- delete the temporary workflow after evidence capture.

## Required updates during work

At meaningful checkpoints, update:

- `audit.md`;
- `metadata.json`;
- `README.md`;
- `HANDOVER.md`.

The handover must state the exact next incomplete gate. Do not restart completed work in a later chat.

## First activity

Inspect the repository and the actual attached audio. Confirm whether the speech already exists, establish the exact source identity and full duration, inspect the true beginning and ending, and then proceed with the next incomplete archival gate.