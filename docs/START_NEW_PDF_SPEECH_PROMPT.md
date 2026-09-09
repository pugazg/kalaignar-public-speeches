# Prompt — Start or Continue a Kalaignar PDF Speech Archive

Copy the prompt below into a new chat and attach the controlling PDF source.

---

Continue the Kalaignar Public Speeches archival project directly in:

`pugazg/kalaignar-public-speeches`

Work on `main`.

The controlling PDF source is attached.

## Mandatory startup

Before making any change, read these repository files completely and follow them exactly:

1. `SPEECH_PROCESSING_GUIDE.md`
2. root `README.md`
3. this prompt
4. completed speech archives only as workflow references, never as textual sources for the attached PDF

Inspect the repository first and determine whether this exact source, collection, or constituent speech has already been started. Search by:

- catalogue/file title;
- exact or likely Tamil title;
- speaker/event wording;
- source filename;
- checksum, if available;
- likely slug;
- collection/volume title when applicable.

If work exists, continue it. Do not create duplicate speech trees or duplicate collection/source records.

## Source authority

The attached PDF is the controlling source for this edition.

Do not rely on the filename alone. Do not silently modernise, correct, regularise, reconstruct or improve the printed Tamil.

Preserve source-supported:

- wording and repetitions;
- historical or unusual printed forms;
- names, initials and honorifics;
- dates, numbers and monetary amounts;
- rhetorical questions and parallel constructions;
- page boundaries and meaningful headings;
- the actual beginning and ending of each constituent speech represented by the source.

OCR, parsed text, catalogue entries and outside historical sources are aids only. They are never authoritative over the attached scan.

## Source inspection

Before creating metadata or a title:

1. inspect the actual attached PDF;
2. calculate SHA-256 from the complete binary when locally available;
3. record byte size;
4. determine the actual PDF page count from the complete binary, not from a preview or truncated parser;
5. inspect embedded PDF metadata, but keep it separate from edition/event facts;
6. inspect title, imprint, contents/index pages, first substantive page and true final page;
7. determine printed-page numbering and map it to PDF scans;
8. identify front matter, speech body, advertisements/back matter and blank/show-through scans;
9. establish whether the PDF is:
   - one complete speech;
   - an extract/part of one speech;
   - a multi-speech collection/volume;
10. do not infer speech dates, venues or events unless the source itself states them.

Do not commit the PDF binary. Preserve source identity through filename, checksum, byte size, actual PDF page count and bibliographic/source metadata.

## Single-speech versus multi-speech PDFs

### A. Single-speech PDF

Use the standard speech directory:

```text
speeches/<stable-speech-slug>/
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
```

### B. Multi-speech collection or volume

Do **not** treat the entire volume as one speech.

First create or continue a collection/source layer under:

```text
collections/<stable-collection-slug>/
```

Use it to preserve edition-level provenance and the source map. At minimum create:

```text
README.md
metadata.json
page-map.md
HANDOVER.md
```

The collection record must track:

- exact collection title and volume/part wording;
- author/editor wording as printed;
- publication/imprint facts supported by the PDF;
- source filename;
- SHA-256;
- byte size;
- actual PDF page count;
- printed-page range(s);
- table-of-contents entries;
- each constituent speech/event title;
- source-supported date/venue/occasion when present;
- PDF scan range and printed-page range for each constituent item;
- archival status and linked speech slug for each item.

Then archive each constituent speech separately under:

```text
speeches/<stable-speech-slug>/
```

Each constituent speech must cite the collection source in its metadata and retain its exact scan/printed-page range. Collection metadata must never be silently copied into speech-level event facts.

If a constituent item is not actually a speech, classify it conservatively and do not force it into `speeches/` merely because it appears in a speech collection.

## Tamil workflow

### T1 — complete first pass

Transcribe the complete source-supported speech body in manageable page batches.

- Preserve PDF scan and printed-page headings.
- Mark uncertainty rather than guessing.
- Preserve printed wording, repetition and historical forms.
- Treat punctuation, paragraphing and word joins as source-sensitive editorial work.
- Do not mark T1 complete until the complete mapped speech range has been transcribed.
- Do not begin English.

### T2 — strict visual fidelity audit

Re-read every speech page against the controlling scan.

For each page verify:

- every word;
- names, initials and honorifics;
- dates, numbers and amounts;
- repetitions;
- quotations;
- page joins and split words;
- headings and source notes;
- printed text versus stamps, handwriting, damage and bleed-through;
- first and last printed words of the mapped speech range.

OCR or textual comparison is never equivalent to visual verification.

### T3 — consolidation and freeze

After every mapped page passes T2:

- consolidate all corrections;
- verify no page/interval is missing or duplicated;
- search for stale names, amounts, page mappings and uncertainty markers;
- synchronize `metadata.json`, `README.md`, `audit.md` and `HANDOVER.md`;
- mark Tamil `verified-complete` only when the complete mapped source range is represented.

Any later Tamil correction reopens dependent English work.

## Correction rule

If the repository owner identifies missing or incorrect source material:

- reopen the exact page/range immediately;
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
- dates and amounts;
- source-supported incomplete/complete boundaries.

Stages:

1. E1 — complete first-pass translation in `translation-en.md`;
2. E2 — independent Tamil-to-English fidelity review in `translation-review.md`;
3. consolidate review corrections;
4. E3 — complete end-to-end Tamil-to-English verification.

Do not mark English verified merely because a translation exists.

## Metadata discipline

Use conservative, explicit states and counters. Status labels must agree with the actual files.

For a constituent speech track at minimum:

- parent collection/source identity when applicable;
- exact source scan range and printed-page range;
- Tamil pages total/drafted/audited;
- opening and ending verification;
- Tamil consolidation state;
- English translation, review and final-verification states.

For a collection track at minimum:

- source identity and actual PDF page count;
- contents/index capture state;
- page-map state;
- constituent items total/mapped/archived;
- unresolved source boundaries or classifications.

## Required updates during work

At meaningful checkpoints update the active speech files and, for a multi-speech volume, the parent collection files.

The handover must state the exact next incomplete gate. Do not restart completed work in a later chat.

## First activity

Inspect the repository and the actual attached PDF. Confirm whether the source or constituent speech already exists, establish exact source identity and actual PDF page count from the complete binary, inspect the title/imprint/contents and true final page, classify the PDF as single-speech or multi-speech, establish the page map, and then proceed with the exact next incomplete archival gate without creating duplicates.
