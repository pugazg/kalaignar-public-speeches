# பள்ளி வாழ்க்கை — English E1 handover

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/palli-vazhkkai/`

## Source

- Canonical scan: `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`
- SHA-256: `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`
- PDF pages: 81
- Speech body: PDF 6-81 / printed 5-80 = 76 pages
- Source PDF committed: No

## Workflow state

### T1 — COMPLETE

All **76/76** body pages have first-pass readings.

### T2 — COMPLETE

All **76/76** body pages passed strict line-by-line visual audit. Detailed evidence remains under `t2-batches/`, including Batches 1-16 and both legacy-glyph recheck records.

### T3 — VERIFIED-COMPLETE / FROZEN

`transcription-ta.md` is the frozen canonical Tamil layer for **PDF 6-81 / printed 5-80**.

The final whole-body gate passed and is recorded in `t3-final-verification.md`. It verified page count/order, page mapping, canonical opening and closing, stale-reading absence, representative T2 corrections, recorded split-word joins, ordinary page-boundary continuations, source-supported unusual forms, and absence of empty/exact-duplicate page bodies.

Tamil must not now be changed without documented source evidence. Any later Tamil correction requires dependent English re-verification.

### E1 — NOT STARTED / READY

English translation is now permitted. `translation-en.md` remains `not-started` until actual translated body text is added.

### E2 / E3 — NOT STARTED

Independent English fidelity review and final end-to-end Tamil→English verification have not begun.

## Mandatory translation source

Translate **only from the frozen `transcription-ta.md`**. Do not independently translate from OCR or replace the frozen Tamil using another edition.

Preserve as far as practical:

- argument structure and paragraph order;
- rhetorical force and repetition;
- metaphors and polemical language;
- historical names/references;
- PDF/printed-page correspondence;
- uncertainty or syntactic difficulty present in the frozen Tamil.

Do not silently repair an unusual Tamil reading merely because a smoother English sentence is possible. If a literal rendering would materially mislead, use a concise, clearly labelled translator/source note.

## Source-fidelity safeguards carried into English

Traditional-glyph errors have already been resolved in the frozen Tamil. Translate the verified forms, not the superseded T1 readings. Examples include `கவலைப்பட`, `நன்றாக`, `மனிதனாக`, `தமிழனாக`, `தோழனாக`, `அவனாகத்தான்`, and `தேவனை`.

Conversely, genuine source-supported oddities remain part of the frozen witness and must not be silently normalized in translation. Representative examples include `கல்வி கற்கு மிடம்`, `நல்லதங்கள்`, `முன்னேற்றம் மடைகின்றன`, `மனிதனி அறிவு கண்டு`, `தமிழனமாக`, `உலகந்தான்`, `தன்னுலே`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, and `உலகியலேக் காண`.

## Exact next activity

Begin **E1 English translation with PDF pages 6-10 / printed pages 5-9** from `transcription-ta.md`.

For that batch:

1. retain the same PDF/printed-page headings in `translation-en.md`;
2. translate every paragraph from the frozen Tamil, with no omitted clause or added historical explanation;
3. preserve repetition and rhetorical questions rather than smoothing them away;
4. flag any genuinely difficult frozen Tamil with a concise translator/source note rather than silently correcting it;
5. update `metadata.json`, `README.md`, and this `HANDOVER.md` with E1 page progress after the batch.

Do **not** begin E2 fidelity review until the full E1 translation is complete.

## Safeguards

- Scan remains the authority behind the frozen Tamil; frozen Tamil is the authority for English.
- Do not modernize or sanitize difficult historical language.
- Do not infer speech date, venue, event, occasion, or audience from publication data or outside knowledge.
- Do not commit the source PDF.
- T2 evidence and `t3-final-verification.md` are permanent audit records.