# T2 execution checklist — Audio 06

**Archive:** `speeches/kalaivanar-nsk-memorial-day-audio-06/`  
**Controlling source:** `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`  
**SHA-256:** `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`  
**Decoded duration:** `00:26:22.080`

## Purpose

This file is the single execution view for the remaining Tamil T2 audit. It does not replace the individual audit records, replay manifests or metadata. It summarizes their current authoritative state.

Only true audible replay of the checksum-matching controlling MP3 may advance T2.

## Counter invariant

The ordinary T2 audit has **43 source segments**:

- Batch 43 splits precheck range 01 into **2 source segments**:
  - separate announcer lead-in;
  - first main-speech segment.
- Precheck ranges 02–42 contribute **41 more source segments**.
- Total ordinary T2 source segments: **43**.

Current live state:

- checked — **22 / 43**;
- passed — **14 / 43**;
- unchecked sequential segments — **21**;
- checked-but-not-passed retry segments — **8**;
- dedicated tail gates — **3 independent closure gates**, not included in 43/43 counters.

If every remaining ordinary segment eventually passes, the final ordinary T2 counter state must be exactly:

> **43 checked / 43 passed**

The tail gates must then also pass separately before T2 can close.

## A. Already checked and passed — 14

### Batch 43 main-speech opening

- [x] first main-speech segment — approximately `00:41.9–01:10`

### First 10-batch iteration passes

- [x] Batch 46 — `03:22–04:00`
- [x] Batch 50 — `06:43–07:12`
- [x] Batch 53 — `08:38–09:25`

### Second 10-batch iteration — all passed

- [x] Batch 54 — `09:25–09:50`
- [x] Batch 55 — `09:50–10:18`
- [x] Batch 56 — `10:18–10:48`
- [x] Batch 57 — `10:48–11:20`
- [x] Batch 58 — `11:20–12:00`
- [x] Batch 59 — `12:00–12:22`
- [x] Batch 60 — `12:22–12:49`
- [x] Batch 61 — `12:49–13:15`
- [x] Batch 62 — `13:15–14:00`
- [x] Batch 63 — `14:00–14:15`

## B. Checked but not passed — 8 mandatory retries

These segments are already counted in **checked = 22**. Replaying them must **not** increment checked again. When resolved fully, each may increment only the passed total.

Use:

`t2-batches/direct-listening-retry-manifest-opening-and-early-ranges.md`

- [ ] Batch 43 lead-in — `00:00–approximately 00:14`
- [ ] Batch 44 — `01:10–02:34`
- [ ] Batch 45 — `02:34–03:22`
- [ ] Batch 47 — `04:00–05:14`
- [ ] Batch 48 — `05:14–06:00`
- [ ] Batch 49 — `06:00–06:43`
- [ ] Batch 51 — `07:12–08:00`
- [ ] Batch 52 — `08:00–08:38`

Retry rule:

- checked counter effect — **0**;
- passed counter effect — **+1 only when the segment has no material unresolved wording**.

## C. Next sequential iteration — 10 unchecked segments

Use:

- `t2-batches/direct-listening-replay-manifest-ranges-22-31.md`;
- `t2-batches/direct-listening-record-templates-64-73.md`.

Each genuine first replay increments checked by 1; passed increments only if the segment passes.

- [ ] Batch 64 / range 22 — `14:15–14:59`
- [ ] Batch 65 / range 23 — `14:59–15:35`
- [ ] Batch 66 / range 24 — `15:35–16:00`
- [ ] Batch 67 / range 25 — `16:00–16:30`
- [ ] Batch 68 / range 26 — `16:30–17:15`
- [ ] Batch 69 / range 27 — `17:15–17:47`
- [ ] Batch 70 / range 28 — `17:47–18:00`
- [ ] Batch 71 / range 29 — `18:00–19:00`
- [ ] Batch 72 / range 30 — `19:00–19:33`
- [ ] Batch 73 / range 31 — `19:33–20:00`

After all ten are first-replayed, checked must be **32 / 43**.

If all ten pass immediately, passed becomes **24 / 43**.

## D. Later sequential ranges — 11 unchecked segments

Use:

- `t2-batches/direct-listening-replay-manifest-ranges-32-42-tail.md`;
- `t2-batches/direct-listening-record-templates-74-84.md`.

- [ ] Batch 74 / range 32 — `20:00–20:30`
- [ ] Batch 75 / range 33 — `20:30–21:04`
- [ ] Batch 76 / range 34 — `21:04–22:00`
- [ ] Batch 77 / range 35 — `22:00–22:52`
- [ ] Batch 78 / range 36 — `22:52–23:25`
- [ ] Batch 79 / range 37 — `23:25–23:44`
- [ ] Batch 80 / range 38 — `23:44–24:00`
- [ ] Batch 81 / range 39 — `24:00–24:46`
- [ ] Batch 82 / range 40 — `24:46–25:00`
- [ ] Batch 83 / range 41 — `25:00–26:00`
- [ ] Batch 84 / range 42 — `26:00–26:22.080`

After all 21 currently unchecked sequential segments have been first-replayed, checked must be **43 / 43**.

If all 21 pass on first replay, passed becomes **35 / 43**. The remaining 8 passed slots are exactly the mandatory retry backlog in section B.

## E. Independent ending gates — not part of 43/43 counters

Use:

`t2-batches/direct-listening-tail-gate-templates.md`

- [ ] TG-01 — final 60 seconds, `25:22.080–26:22.080`
- [ ] TG-02 — final 30 seconds, `25:52.080–26:22.080`
- [ ] TG-03 — actual final major pause through `00:26:22.080`

These gates must establish:

- [ ] exact final audible spoken word/syllable;
- [ ] complete/incomplete final grammatical thought;
- [ ] post-farewell audio classification;
- [ ] final audible event end time;
- [ ] actual final major pause;
- [ ] `ending_verified=true`;
- [ ] `recording_truncated` resolved from direct evidence.

## F. T2 closure conditions

Tamil T2 may be marked complete only when all are true:

- [ ] ordinary source counters are **43 checked / 43 passed**;
- [ ] the 8 retry segments in section B have all passed;
- [ ] Batches 64–84 have all passed;
- [ ] TG-01 passed;
- [ ] TG-02 passed;
- [ ] TG-03 passed;
- [ ] opening gate fully verified;
- [ ] ending verified;
- [ ] `recording_truncated` no longer null;
- [ ] all source-supported corrections consolidated into `transcription-ta.md`;
- [ ] no material unresolved Tamil wording remains;
- [ ] control documents and metadata synchronized.

Only after those conditions pass may Tamil T3 consolidation/freeze begin. English remains blocked until verified Tamil is frozen.

## Exact next source activity

True audible replay of **Batches 64–73 / precheck ranges 22–31 / 14:15–20:00**.


## Preparation-state guard

Non-auditory T2 preparation is **COMPLETE**. See `T2_PREPARATION_CLOSURE.md`.

Do not create additional generic manifests/templates merely to advance workflow state. Further progress must come from true audible source replay or genuinely new source evidence.
