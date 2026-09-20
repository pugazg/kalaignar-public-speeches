# Pending direct-listening tail-gate templates

**Archive:** `speeches/kalaivanar-nsk-memorial-day-audio-06/`  
**Gate class:** mandatory T2 ending audit — independent of ordinary sequential range passes  
**Evidence class:** **template/preparation only — NOT T2 evidence**  
**Live T2 state:** **22 checked / 14 passed**  
**Canonical Tamil changes:** **0**  
**ending_verified:** **No**  
**recording_truncated:** **Unresolved**

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
**Duration:** 60.000s  
**Replay WAV SHA-256:** `04217be6591aa31a34cf4027fe262e7ec0296b21cdf15acc1e65280c465872df`  
**Status:** **PENDING — not yet directly replayed in this gate**

## Mandatory audible checks

- listen continuously for the full 60 seconds;
- verify the card-game/money-joke close without relying on candidate text;
- verify the transition into the friends/family conclusion;
- verify whether any low-volume speech is present after an apparent pause;
- verify the final farewell wording;
- identify any trailing ambience/applause/noise/other voice;
- identify the final audible event and approximate end time.

## Source-heard findings

**PENDING — fill only from true audible replay.**

## Decision

- tail gate completed — **No**;
- final audible word confirmed — **No**;
- grammatical thought complete — **Not adjudicated**;
- post-farewell audio — **Not adjudicated**;
- ending verified — **No**;
- recording truncated — **Unresolved**.

---

# Tail Gate TG-02 — final 30 seconds

**Replay interval:** `25:52.080–26:22.080`  
**Duration:** 30.000s  
**Replay WAV SHA-256:** `271824d85c12341ceff99ca377eb12f30ed5d777a5b74bc7b0aa570fa67ed4ef`  
**Status:** **PENDING — not yet directly replayed in this gate**

## Mandatory audible checks

This is a **separate replay**, not a subset automatically satisfied by TG-01.

Directly verify:

- the end of the money/friends transition;
- exact grammar of the friends-surrounding clause;
- `ஒரு பத்து நண்பர்கள் இல்லாமல் தனியாக இருக்க முடியாது` and joins;
- exact `கலைக்குடும்பம்` sentence;
- exact farewell noun after `அந்தக் கலைவாணருடைய`;
- exact count/form of repeated `வாழ்க`;
- whether `விடைபெற்றுக் கொள்கிறேன்` is verbatim;
- exact `நன்றி, வணக்கம்` wording/boundary;
- last audible spoken word/syllable;
- any sound after the final speech.

## Source-heard findings

**PENDING — fill only from true audible replay.**

## Decision

- tail gate completed — **No**;
- final audible word confirmed — **No**;
- grammatical thought complete — **Not adjudicated**;
- post-farewell audio — **Not adjudicated**;
- ending verified — **No**;
- recording truncated — **Unresolved**.

---

# Tail Gate TG-03 — final major pause to true decoded end

**Known decoded end:** `00:26:22.080`  
**Prepared navigation crop:** `26:15.000–26:22.080`  
**Navigation WAV SHA-256:** `110ed7ebfa7953e3f8380a9ac471511066d385e7f751036edb5391000c455930`  
**Status:** **PENDING — actual final major pause not yet established by listening**

## Important navigation rule

Signal-only analysis found a short low-energy interval around approximately `26:15.36–26:15.95`, but that does **not** prove it is the final major pause.

The listener must first identify the actual final major pause audibly.

- If the actual pause begins within the prepared `26:15.000–26:22.080` crop, replay from that audible pause through the true end.
- If the actual pause begins earlier, create/replay a wider source crop beginning before that pause.
- Do not use the signal timestamp itself as the gate result.

## Mandatory audible checks

- establish the final major pause from sound, not waveform alone;
- replay continuously from that pause to `00:26:22.080`;
- check for low-volume speech after the pause;
- identify the last audible spoken word/syllable;
- identify the last audible event of any kind;
- record trailing silence/ambience/applause/music/noise/edit/other voice;
- determine whether the final grammatical thought is complete;
- compare the final audible event with the decoded file end;
- determine whether the source ends naturally or is truncated.

## Source-heard findings

**PENDING — fill only from true audible replay.**

## Decision

- actual final major pause established — **No**;
- replay from actual pause to true end completed — **No**;
- final audible word confirmed — **No**;
- final audible event end time — **Not adjudicated**;
- grammatical thought complete — **Not adjudicated**;
- ending verified — **No**;
- recording truncated — **Unresolved**.

---

# Tail-gate closure decision

This section may be completed only after TG-01, TG-02 and TG-03 all pass.

- TG-01 final 60 seconds — **PENDING**
- TG-02 final 30 seconds — **PENDING**
- TG-03 final major pause to true end — **PENDING**
- final audible word — **UNVERIFIED**
- final grammatical thought — **UNVERIFIED**
- trailing audio classification — **UNVERIFIED**
- final audible event end time — **UNVERIFIED**
- `ending_verified` — **false**
- `recording_truncated` — **null / unresolved**
- Tamil T3 — **BLOCKED**
- English — **BLOCKED**

Do not close T2 until the opening/retry backlog, all sequential ranges, and all three independent tail gates are audibly complete.
