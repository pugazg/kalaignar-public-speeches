# Future Audio Speech Archival Guidelines

## Scope

These guidelines apply to every Kalaignar public speech whose controlling source is audio or video with an audio track. They supplement:

- `SPEECH_PROCESSING_GUIDE.md`;
- `AUDIO_SPEECH_PROCESSING_GUIDE.md`.

The rules below are mandatory. They incorporate the lessons recorded in:

- `speeches/kalaivanar-nsk-memorial-day/LEARNINGS.md`.

## Governing principle

The supplied media file is the controlling witness. Filename, catalogue description, surfaced transcript, subtitles, ASR, historical research and another edition are aids only.

Never claim that a word, name, date, venue, boundary or ending is verified unless the controlling source supports that claim.

---

## 1. Mandatory startup

Before creating or changing a speech archive:

1. read `SPEECH_PROCESSING_GUIDE.md` completely;
2. read `AUDIO_SPEECH_PROCESSING_GUIDE.md` completely;
3. read this document completely;
4. inspect the repository and target slug for existing work;
5. continue existing work rather than creating a duplicate;
6. inspect the actual attached media, not only its filename;
7. identify whether the available file is complete, clipped, edited or part of a longer source.

Do not begin translation during startup or Tamil T1/T2 work.

---

## 2. Source identity and technical inspection

Record from the exact controlling binary:

- source filename;
- original URL, where known;
- SHA-256;
- byte size;
- decoded duration;
- codec;
- sample rate;
- channels and channel layout;
- average bitrate where available;
- embedded metadata, clearly separated from event facts;
- whether the binary is committed;
- whether the start or end is damaged, clipped or complete.

### Required checks

- Recompute the checksum whenever the user reattaches the source.
- Compare byte size and duration with existing metadata.
- Do not assume matching filenames mean matching files.
- Do not assume a matching checksum validates an earlier transcription or interpretation; it validates only source identity.

### Duration rule

Use the decoded duration of the complete controlling binary. Do not use:

- a preview duration;
- an ASR segment end;
- a cropped working file;
- a stale copied value;
- a UI progress display.

---

## 3. Standard files

Create or maintain:

```text
speeches/<speech-slug>/
  README.md
  metadata.json
  transcription-ta.md
  audit.md
  translation-en.md
  translation-review.md
  HANDOVER.md
  LEARNINGS.md                 # when project-specific lessons are material
  t2-batches/
  research/                    # only when clearly separated contextual research exists
```

Recommended repository-level documents:

```text
docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md
docs/START_NEW_AUDIO_SPEECH_PROMPT.md
```

Do not commit the media binary unless repository policy explicitly changes.

---

## 4. Evidence classes must remain separate

Use explicit labels for the kind of work performed.

### A. Surfaced-text or transcript comparison

Status examples:

- `textual-precheck-in-progress`;
- `textual-precheck-complete`.

This does not count as auditory verification.

### B. Machine-aided audio analysis

Status examples:

- `machine-aided-pre-audit-in-progress`;
- `machine-aided-pre-audit-complete`.

ASR or forced alignment may help locate boundaries and candidate readings. It does not automatically verify wording.

### C. Direct auditory comparison

Status examples:

- `direct-listening-audit-in-progress`;
- `direct-listening-audit-complete`.

This status may be used only when the source has actually been replayed and compared.

### D. Boundary verification

Beginning and ending checks are independent requirements. A speech may not be marked verified merely because all interior segments were checked.

Never merge these evidence classes into one ambiguous `audited` label.

---

## 5. T1 — complete Tamil first pass

Transcribe every audible part of the recording in manageable time segments.

### Preserve

- Kalaignar's exact wording where audible;
- repetition;
- honorifics;
- names and initials;
- historical and spoken forms;
- numbers and monetary amounts;
- rhetorical questions;
- false starts where meaningful;
- audience responses when meaningful;
- interruptions or overlapping speech when intelligible;
- incomplete sentences only when the source is genuinely incomplete.

### Editorial additions

Punctuation, paragraphing, word spacing and timestamp headings may be editorial. State this clearly.

### Uncertainty

Mark uncertain readings. Do not guess and later present the guess as a source fact.

### Coverage rule

T1 is not complete until the first pass reaches the true decoded end of the controlling file.

---

## 6. Time map rules

Use timestamps as navigation aids, not as false frame-accurate claims.

For each segment record:

- segment number;
- approximate start;
- approximate end;
- subject;
- boundary status.

When a boundary changes, update:

- `transcription-ta.md`;
- `metadata.json`;
- `audit.md`;
- `README.md`;
- relevant batch records;
- `HANDOVER.md`.

Do not allow adjacent segment ranges to omit or duplicate audible speech.

---

## 7. T2 — strict auditory fidelity audit

Replay every segment directly against the controlling source.

For each segment verify:

- every word;
- names and initials;
- honorifics;
- numbers and amounts;
- repetitions;
- quotations;
- case endings and verb forms where distinguishable;
- pauses and transitions;
- audience reaction;
- cross-talk;
- edits or recording artefacts;
- first and last words at segment boundaries.

### Batch size

Use approximately 30–60 seconds per batch when practical. Shorter crops should be used for uncertain passages.

### Listening aids

Slower playback, channel isolation, conservative noise reduction and ASR may be used as aids. They must not introduce words that are not supported by the unaltered controlling source.

### Audit record

For every substantive correction record:

- prior reading;
- corrected reading;
- source range;
- method used;
- whether uncertainty remains.

---

## 8. Mandatory opening audit

Independently verify:

- the first audible word;
- whether leading silence exists;
- title/name sequence;
- salutation order;
- the first complete sentence;
- the first transition into the speech body.

Do not infer the opening from a catalogue title or an expected formula.

---

## 9. Mandatory final-minute audit

This is a separate gate and may not be skipped.

### Procedure

1. replay at least the last 60 seconds;
2. replay the last 30 seconds separately;
3. replay from the final major pause to the true file end;
4. check whether low-volume speech follows an apparent ending;
5. confirm the final audible word;
6. determine whether the final grammatical thought is complete;
7. compare the final segment end with the decoded file duration;
8. inspect for trailing silence, music, applause or a recording edit.

### Truncation claim standard

Do not write `recording ends abruptly` or `source is truncated` unless all of the following are documented:

- exact final audible words;
- exact decoded duration;
- confirmation that no further speech follows;
- direct replay of the tail;
- grammatical or acoustic evidence of interruption.

A model stopping, a waveform display ending, a pause or a provisional timestamp is not proof of truncation.

---

## 10. T3 — consolidation and freeze

Tamil may be marked `verified-complete` only after:

- all segments pass direct audit;
- first-word verification passes;
- final-minute verification passes;
- every correction is consolidated;
- no audible interval is missing or duplicated;
- the complete decoded duration is represented;
- all open uncertainties are counted accurately;
- stale readings are searched and removed.

### Required stale-term search

Search the speech folder and repository documentation for superseded terms, especially:

- old names;
- old amounts;
- old timestamps;
- old duration values;
- `abrupt`;
- `truncated`;
- `unfinished`;
- obsolete bracketed uncertainties;
- superseded translation instructions.

### Freeze rule

Any later Tamil source correction reopens dependent gates. Do not treat the earlier freeze as permanent when new source evidence appears.

---

## 11. Correction and supersession procedure

When a previous verified claim is found wrong:

1. stop downstream work affecting that passage;
2. reopen the exact source range;
3. create a correction audit record;
4. state the false earlier conclusion plainly;
5. state which earlier record is superseded and only to what extent;
6. preserve valid unaffected findings;
7. update the canonical Tamil;
8. update metadata and all reader-facing files;
9. reset English statuses where required;
10. search for stale references;
11. remove temporary workflows after evidence capture.

Do not silently rewrite history. The archive should show why the correction was necessary.

---

## 12. English translation gate

English begins only after the latest Tamil layer is frozen as `verified-complete`.

Translate from `transcription-ta.md`, not from:

- ASR;
- surfaced transcript;
- catalogue prose;
- research notes;
- memory;
- another edition.

Preserve:

- argument order;
- rhetorical repetition;
- formal public-speaking voice;
- metaphors and images;
- names and titles;
- institutions and hall names;
- amounts;
- completed or incomplete source ending exactly as verified.

If Tamil changes after English begins:

- identify all affected English passages;
- mark translation/review status conservatively;
- replace the affected translation;
- repeat fidelity review and final verification.

---

## 13. English review gates

### E1 — first-pass translation

Translate the complete verified Tamil, preserving timestamp correspondence.

### E2 — fidelity review

Compare Tamil and English separately, checking for:

- omission;
- addition;
- reversal;
- softened or strengthened rhetoric;
- lost repetition;
- mistranslated image;
- wrong subject or pronoun;
- altered names, titles or amounts;
- modernizing paraphrase;
- missing beginning or ending.

Record findings in `translation-review.md` and consolidate corrections.

### E3 — final end-to-end verification

Read the complete Tamil and final English from beginning to end. Confirm that the final English includes the true closing passage.

---

## 14. Metadata requirements

For audio work, metadata should explicitly track:

```json
{
  "duration_seconds": 0,
  "duration_display": "00:00:00.000",
  "recording_boundary": {
    "start": "...",
    "end": "..."
  },
  "direct_listening_audit": {
    "status": "...",
    "segments_checked": 0,
    "segments_passed": 0,
    "recording_boundary_verified": false,
    "recording_truncated": null
  },
  "workflow": {
    "tamil_transcription": "...",
    "strict_audio_audit": "...",
    "tamil_consolidation": "...",
    "english_translation": "...",
    "english_translation_review": "...",
    "english_translation_final_verification": "..."
  }
}
```

Counters, labels and narrative files must agree.

---

## 15. Temporary analysis infrastructure

When GitHub Actions or another temporary workflow is created for ASR/audio inspection:

- limit it to the required range;
- verify the source checksum inside the job;
- upload evidence as an expiring artifact;
- do not commit the source media;
- record what the output can and cannot establish;
- delete the workflow after evidence is captured;
- never allow machine output to silently overwrite the canonical transcript.

---

## 16. Handover requirements

Every active audio speech must have a current `HANDOVER.md` containing:

- repository and path;
- controlling source identity;
- decoded duration;
- completed gates;
- current counters;
- exact unresolved readings;
- all superseding correction records;
- exact next activity;
- explicit beginning/end status;
- warning against stale or false boundary claims;
- English status and next review gate.

A future chat must continue the exact next incomplete gate rather than restarting completed work.

---

## 17. Completion checklist

An audio speech is not fully archived until all are true:

- [ ] exact binary identified;
- [ ] technical metadata recorded;
- [ ] Tamil T1 covers the true full duration;
- [ ] every segment directly audited;
- [ ] opening independently verified;
- [ ] final minute independently verified;
- [ ] true ending established;
- [ ] Tamil corrections consolidated;
- [ ] stale readings removed;
- [ ] Tamil frozen;
- [ ] English first pass complete;
- [ ] English fidelity review complete;
- [ ] review corrections consolidated;
- [ ] English final end-to-end verification complete;
- [ ] metadata synchronized;
- [ ] README synchronized;
- [ ] handover finalized;
- [ ] temporary workflows removed;
- [ ] root catalogue synchronized.

## Non-negotiable rule

Never let the confidence of a status statement exceed the evidence actually obtained from the controlling source.