# Multi-Constituent Batching Policy

This policy applies when a controlling source is a **multi-speech / multi-constituent collection** and several consecutive constituent speeches can be advanced through the same workflow gate together.

It supplements `SPEECH_PROCESSING_GUIDE.md`. For multi-constituent collection work, this policy governs the **iteration-level batch size** while all source-fidelity rules in the main guide remain mandatory.

## Maximum iteration size

- Process at most **25 source pages per iteration**.
- More than one consecutive speech/constituent may be included when their combined source-page count is **25 pages or fewer**.
- Do not split a shorter constituent merely to fill the 25-page ceiling.
- If one constituent itself exceeds 25 pages, split that constituent into consecutive batches of at most 25 source pages.
- The 25-page figure is a **maximum, not a target**. Use fewer pages when scan quality, difficult typography, unresolved glyphs, tables, annotations, or unusually dense material require it.

## Same-gate rule

A multi-constituent iteration must advance the **same workflow gate** across every included constituent.

Examples:

- T1 may process several consecutive not-yet-transcribed speeches whose combined length is ≤25 pages.
- T2 may audit several T1-complete speeches whose combined length is ≤25 pages.
- T3 may consolidate/freeze several T2-complete speeches whose combined length is ≤25 pages.
- The same principle may be used for E1, E2, or E3 once each constituent satisfies that gate's prerequisite.

Do **not** mix T1, T2, T3 and English stages merely to fill the 25-page allowance.

## Constituent independence

Batching several speeches together never merges their archival identity.

Each speech must retain its own:

- directory;
- source/duplicate gate;
- exact PDF and printed-page boundaries;
- `README.md`;
- `metadata.json`;
- `transcription-ta.md`;
- `audit.md`;
- `translation-en.md`;
- `translation-review.md`;
- `HANDOVER.md`;
- event/date/venue/role evidence;
- body-ending and source-closing-note distinction.

A failure or unresolved reading in one constituent does not authorize guessing or silently normalizing that constituent merely because other items in the same iteration pass.

## Visual-fidelity rule

The larger iteration allowance does **not** weaken page-level verification.

For T2 and equivalent fidelity gates:

- visually re-read every included source page once, in full;
- inspect page-boundary continuations;
- create crops/enhancements only when an actual reading is uncertain;
- record constituent-specific corrections in that constituent's audit;
- preserve all source-supported unusual forms;
- leave unresolved readings explicit.

The `SPEECH_PROCESSING_GUIDE.md` suggestion that roughly 4–6 pages is often effective remains useful as an **internal visual-review chunk**, but it is no longer the iteration-level limit for multi-constituent collection work. The iteration may contain several such internal chunks up to the **25-page maximum**.

## Commit and reporting rule

After the selected ≤25-page same-gate batch is complete:

1. synchronize every affected constituent control file;
2. synchronize collection/root progress controls that changed;
3. commit the durable result immediately;
4. report the combined page count, constituent count, gate result, correction/unresolved totals, live `main` SHA, and exact next gate.

Do not spend the turn narrating intermediate inspection unless an unresolved source issue requires user input.

## Selection rule

When choosing the next multi-constituent batch:

1. start with the earliest consecutive constituent eligible for the current gate;
2. keep adding the next consecutive eligible constituent while the total remains ≤25 source pages;
3. stop before adding an item that would take the total above 25 pages;
4. preserve source/contents order even when event dates are not chronological.

This policy is an efficiency optimization only. **Source fidelity, gate ordering, and constituent-level archival independence remain unchanged.**
