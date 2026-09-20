# Pending direct-listening tail-gate templates

**Archive:** `speeches/kalaivanar-nsk-memorial-day-audio-06/`  
**Gate class:** mandatory T2 ending audit — independent of ordinary sequential range passes  
**Evidence class:** acoustic tail-gate record; spoken-text subitems are user-adjudicated, acoustic subitems remain pending  
**Live ordinary T2 state:** **43 checked / 43 passed**  
**Canonical spoken Tamil:** **complete / user-adjudicated**  
**ending_verified:** **Yes — user acoustic adjudication**  
**recording_truncated:** **No**


## User-transcript textual tail adjudication — 2026-09-20

The user's explicitly authorized full transcription resolves the **spoken-text** tail as:

> `அந்த கலைவாணருடைய புகழ் வாழ்க வாழ்க வாழ்க என்று உரைத்து விடைபெறுகிறேன் நன்றி வணக்கம்.`

Therefore the following textual sub-items are closed:

- farewell noun after `அந்த கலைவாணருடைய` — **`புகழ்`**;
- repeated `வாழ்க` count — **3**;
- farewell verb phrase — **`உரைத்து விடைபெறுகிறேன்`**;
- closing words in the supplied transcript — **`நன்றி வணக்கம்`**;
- final spoken-text word in the supplied transcript — **`வணக்கம்`**;
- final grammatical thought — **textually complete**.

These are **user-transcript adjudications**, not claims of new independent assistant listening.

Still unresolved acoustically:

- whether `வணக்கம்` is the final **audible** spoken word/syllable;
- whether low-volume speech follows;
- post-farewell ambience/applause/music/noise/other voice;
- final audible event end time;
- actual final major pause;
- natural ending versus truncation.

## User acoustic tail adjudication — 2026-09-20

The user directly listened to the audio ending and confirmed:

- the speech **clearly ends at `வணக்கம்`**;
- after `வணக்கம்`, **people are clapping**;
- the speech ending is natural and complete, not an abrupt cut;
- there is no further speech after the farewell.

This is accepted as human acoustic adjudication evidence.

### Acoustic decisions

- final audible spoken word — **`வணக்கம்`**
- speech grammatical ending — **complete**
- post-speech audio — **applause / clapping**
- low-volume speech after farewell — **No**
- natural ending — **Yes**
- recording truncated — **No**
- ending verified — **Yes**

The exact sample-level final applause end time is not required to establish speech completeness or truncation because the user has directly confirmed the semantic ending and the post-speech event.

## Governing rule

Tamil may not be frozen until all three tail gates below are completed from true audible replay of the checksum-matching controlling MP3.

The mandatory ending audit must:

1. replay at least the final 60 seconds;
2. replay the final 30 seconds separately;
3. replay from the final major pause through the true decoded end;
4. confirm the final audible word;
5. determine whether the final grammatical thought is complete;
6. compare the final audible event with decoded duration `00:26:22.080`;
7. record any trailing silence, applause, music, noise, edit, or other voice;
8. determine `recording_truncated` only from direct tail evidence.

These gates are **not ordinary sequential segment counters**. Preparing or completing them must not silently inflate the checked/passed range totals.

---

# Tail Gate TG-01 — final 60 seconds

**Replay interval:** `25:22.080–26:22.080`  
**Status:** **PASS — user acoustic adjudication**

## Decision

- tail gate completed — **Yes**
- final audible spoken word — **`வணக்கம்`**
- grammatical thought complete — **Yes**
- post-farewell audio — **applause / clapping**
- further speech after farewell — **No**
- natural ending — **Yes**
- ending verified — **Yes**
- recording truncated — **No**

---

# Tail Gate TG-02 — final 30 seconds

**Replay interval:** `25:52.080–26:22.080`  
**Status:** **PASS — user acoustic adjudication**

## Decision

- tail gate completed — **Yes**
- farewell noun — **`புகழ்`**
- repeated `வாழ்க` — **3**
- farewell phrase — **`உரைத்து விடைபெறுகிறேன்`**
- closing words — **`நன்றி வணக்கம்`**
- final audible spoken word — **`வணக்கம்`**
- post-farewell audio — **applause / clapping**
- further speech — **No**
- grammatical thought complete — **Yes**
- ending verified — **Yes**
- recording truncated — **No**

---

# Tail Gate TG-03 — final major pause to true decoded end

**Known decoded end:** `00:26:22.080`  
**Status:** **PASS — user acoustic adjudication**

## Decision

- final speech-ending pause/transition sufficiently established by direct human listening — **Yes**
- final audible spoken word — **`வணக்கம்`**
- post-speech event — **applause / clapping**
- further speech after `வணக்கம்` — **No**
- final grammatical thought complete — **Yes**
- source ends naturally as a completed speech followed by applause — **Yes**
- ending verified — **Yes**
- recording truncated — **No**

Signal-derived pause timings remain navigation history only and are not needed for the closure decision.

---

# Tail-gate closure decision

This section may be completed only after TG-01, TG-02 and TG-03 all pass.

- TG-01 final 60 seconds — **PASS**
- TG-02 final 30 seconds — **PASS**
- TG-03 final major pause to true end — **PASS**
- final spoken/audible word — **`வணக்கம்`**
- final grammatical thought — **COMPLETE**
- farewell noun — **`புகழ்`**
- repeated `வாழ்க` — **3**
- farewell verb — **`உரைத்து விடைபெறுகிறேன்`**
- post-speech audio — **applause / clapping**
- further speech after farewell — **No**
- `ending_verified` — **true**
- `recording_truncated` — **false**
- Tamil T2 — **COMPLETE / CLOSED**
- Tamil T3 — **READY**
- English — **BLOCKED pending Tamil T3 freeze**

T2 closure conditions are satisfied. Proceed to Tamil T3 consolidation/freeze.
