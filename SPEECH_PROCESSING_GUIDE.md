# Kalaignar Public Speeches — Processing Guide

This is the repository-level operating procedure for adding each new public-speech booklet by **M. Karunanidhi (Kalaignar)**.

The completed `speeches/arappor/` archive is the reference implementation for workflow and file structure. It is a reference for method, not a textual source for another speech.

## Core principle

This repository is a **source-faithful archival project**. The supplied scan is the controlling witness for its own edition. The objective is not to silently produce a corrected or modernized reading edition.

Every speech must pass these gates in order:

1. source inspection and bibliographic identification;
2. Tamil transcription;
3. strict visual Tamil fidelity audit;
4. Tamil consolidation/freeze;
5. English translation from the verified Tamil layer;
6. English fidelity review;
7. final end-to-end Tamil→English verification;
8. repository-level archival closure.

A later gate must not be marked complete before its prerequisite gate passes.

---

## 1. Starting a new speech

### 1.1 Inspect repository state first

Before creating files:

- read this guide completely;
- read root `README.md`;
- inspect `speeches/arappor/` as the completed reference implementation, especially `README.md`, `metadata.json`, `audit.md`, `translation-review.md`, and `HANDOVER.md`;
- search the repository for the new title and likely slug;
- if work already exists, continue it rather than creating a duplicate.

### 1.2 Inspect the actual PDF

Never rely only on the uploaded filename.

Inspect the scan itself and establish, where the source supports them:

- exact Tamil title;
- author/speaker wording;
- edition statement;
- publication date;
- publisher and printer;
- printed price;
- actual PDF page count;
- printed page numbering;
- front matter, speech body, advertisements/back matter;
- whether a speech date, venue, event, occasion, or audience is explicitly stated.

**Publication date is not automatically the speech date.** Never infer a speech date, venue, or event merely because it seems historically likely.

### 1.3 Source provenance

Record:

- uploaded/source filename;
- SHA-256 checksum when the binary is locally available;
- file size;
- actual PDF page count;
- page map;
- source status/provenance.

**Repository policy: source PDFs are not uploaded to GitHub.** Store provenance/checksum metadata, not the binary.

---

## 2. Standard directory and files

Create one stable slug under:

```text
speeches/<speech-slug>/
```

Standard files:

```text
README.md
metadata.json
transcription-ta.md
audit.md
translation-en.md
translation-review.md
HANDOVER.md
```

Do not create unnecessary duplicate transcript files or temporary versions on `main`.

### `README.md`

Human-readable source summary, page map, editorial rules, and current completion state.

### `metadata.json`

Machine-readable bibliographic/source/workflow state. Unknown source facts must be `null` or explicitly described as unstated; never manufacture them.

### `transcription-ta.md`

Canonical Tamil transcription. Preserve page boundaries using clear PDF-page and printed-page headings.

### `audit.md`

Tamil source-fidelity audit trail: page/batch checked, corrections made, ambiguous readings, annotations/damage, page-boundary joins, and final verification state.

### `translation-en.md`

English translation produced **only after the Tamil layer is verified**. Keep page correspondence with the Tamil source.

### `translation-review.md`

Independent Tamil→English fidelity review and correction record.

### `HANDOVER.md`

Current state, exact completed/pending gates, source identity, important unresolved/resolved readings, and instructions for continuation. Update it whenever a chat is likely to end at a meaningful checkpoint. At completion convert it into a final archival handover.

---

## 3. Tamil transcription rules

The scan is authoritative for transcription.

### Preserve

Preserve, where legible:

- historical spelling;
- punctuation;
- capitalization/typographic distinctions where meaningful;
- names and honorifics;
- numbers and dates;
- repeated words and rhetorical repetition;
- unusual grammar;
- source-supported typographical oddities;
- headings and meaningful section breaks.

### Never silently do

Do not silently:

- modernize Tamil spelling;
- correct grammar;
- replace an unusual word with the word you think the printer intended;
- rewrite rhetoric for readability;
- insert missing ideas from historical knowledge;
- use an outside edition to overwrite this edition;
- treat handwritten/library stamps or later annotations as printed text.

### Line wraps and page boundaries

A printer line-wrap may be joined when it clearly splits **one word**. Record non-obvious joins during audit.

Do not merge distinct words merely because a modern form seems preferable.

When a word is split across two pages, inspect both page images before joining it.

### Uncertain text

Do not guess. Mark genuinely unreadable/uncertain text explicitly in the working transcription and resolve it during visual audit if possible. If it remains unresolved, preserve the uncertainty in the final archive and document it in `audit.md`.

### Parsed text/OCR

OCR or parsed text is an aid, never the authority. For old Tamil typography, visually inspect the scan. A clean OCR string is not evidence against a visibly different printed form.

---

## 4. Tamil transcription workflow

### Stage T1 — first-pass transcription

Transcribe the complete speech body in manageable page batches. Keep PDF and printed-page mappings explicit.

Do not begin English translation during T1.

### Stage T2 — strict visual fidelity audit

After the entire Tamil speech body exists, re-read **every speech page against the page image**, line by line.

This is not proofreading for modern correctness. It is source comparison.

For each batch:

- compare every line;
- verify names, punctuation, numerals and repeated phrases;
- inspect suspicious OCR-like readings;
- inspect beginning/end of pages for split words;
- distinguish print from stamps, handwriting, damage and bleed-through;
- log substantive corrections in `audit.md`;
- apply confirmed corrections to `transcription-ta.md`.

Use manageable batches (roughly 4–6 pages is usually effective), but completeness matters more than batch size.

### Stage T3 — consolidation and freeze

After all pages pass T2:

- ensure all batch corrections are present in the combined transcript;
- check page boundaries again;
- search for stale superseded readings;
- confirm no speech page is missing or duplicated;
- mark Tamil transcription `verified-complete` only then.

The verified Tamil layer becomes frozen. Later changes require documented source evidence and dependent English re-verification.

---

## 5. English translation rules

Translation starts only after Tamil is `verified-complete`.

Translate from `transcription-ta.md`, not from OCR and not independently from an outside edition.

Preserve as far as practical:

- argument structure;
- rhetorical force;
- repetition;
- metaphors;
- polemical language;
- historical references;
- paragraph/page sequence;
- uncertainty in the source.

Do not sanitize politically or socially difficult historical language merely to make it contemporary. Translation is archival representation, not endorsement.

Do not silently repair an odd Tamil reading. Where a literal rendering would mislead or the printed form is internally difficult, preserve transparency with a concise translator/source note.

Do not add explanatory sentences to the body unless they are clearly labelled as editorial notes.

---

## 6. English workflow

### Stage E1 — first-pass translation

Translate all verified Tamil speech pages, retaining PDF/printed-page headings.

### Stage E2 — fidelity review

Perform a separate page-by-page comparison of English against the verified Tamil.

Look specifically for:

- omitted clauses;
- added ideas;
- reversed meaning;
- softened/strengthened rhetoric;
- incorrect subjects or pronouns;
- mistranslated historical names/titles;
- silently normalized difficult Tamil;
- repetition accidentally removed;
- page-boundary omissions;
- translator inference presented as source fact.

Record findings in `translation-review.md`, then consolidate confirmed corrections into `translation-en.md`.

### Stage E3 — final end-to-end verification

After corrections, compare all pages once more from beginning to end. This is the release gate.

Only after E3 passes may metadata say:

```text
english_translation: verified-complete
english_translation_final_verification: complete
```

---

## 7. Metadata workflow states

Use explicit, conservative states. Suggested progression:

Tamil:

```text
not-started
in-progress
first-pass-complete
audit-in-progress
verified-complete
```

English:

```text
not-started
in-progress
first-pass-complete
review-in-progress
fidelity-corrections-consolidated
verified-complete
```

Track page counts separately. A status label must agree with the counters.

Never mark a stage complete merely because text exists.

---

## 8. Audit discipline

The archive must make it possible to answer: **Why does the transcription/translation say this?**

Record meaningful decisions, especially:

- difficult characters/words;
- damaged text;
- unusual printed forms intentionally retained;
- later handwritten marks/stamps crossing print;
- page-boundary word joins;
- rejected preliminary readings;
- translation corrections involving omission/addition/reversal;
- source wording that remains syntactically difficult.

Do not clutter the audit with every ordinary correct word.

---

## 9. Repository closure

A speech is textually complete only when all applicable gates pass:

- source identified and mapped;
- Tamil first pass complete;
- Tamil visual audit complete for every speech page;
- Tamil consolidated and `verified-complete`;
- English first pass complete;
- English fidelity review complete for every speech page;
- all review corrections consolidated;
- final end-to-end English verification complete;
- `metadata.json` synchronized;
- speech `README.md` synchronized;
- root catalogue synchronized;
- `HANDOVER.md` converted to final archival state.

At closure, explicitly state that no transcription/translation work is pending.

The absence of the source PDF binary from GitHub is **not** a pending archival-text task; repository policy is not to upload source PDFs.

---

## 10. Restart / continuation rule

Never restart completed work simply because work moves to a new chat.

At the beginning of a continuation:

1. read this guide;
2. read the target speech's `HANDOVER.md` completely;
3. inspect current repository files/status;
4. continue the exact next incomplete gate.

If repository state and handover disagree, inspect the actual files and metadata before changing anything. Do not blindly overwrite newer work.

---

## 11. Outside research

The primary workflow does not require web research.

Outside sources may be used only when the user explicitly asks for historical verification/context or when a clearly labelled research layer is being created. Such research must remain distinct from source transcription.

Never use web research to silently fill a missing speech date, venue, event, damaged word, or bibliographic fact.

---

## 12. Quality standard established by `அறப்போர்`

`அறப்போர்` demonstrated several rules that are mandatory for future volumes:

- visually verify every page rather than trusting parsed text;
- retain confirmed strange print rather than normalize it;
- distinguish later ink/library markings from edition text;
- audit page-boundary word splits;
- conduct English fidelity review separately from translation;
- explicitly catch additions, omissions and reversals;
- run a final full English verification after corrections;
- synchronize repository documentation only after the textual gates pass.

Future speeches should meet or exceed this standard.
