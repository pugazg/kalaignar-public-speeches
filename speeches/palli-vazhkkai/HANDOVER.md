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

The final whole-body gate passed and is recorded in `t3-final-verification.md`. Tamil must not now be changed without documented source evidence; any later Tamil correction requires dependent English re-verification.

### E1 — IN PROGRESS

English translation is being produced only from the frozen Tamil layer.

Completed E1 scope: **PDF 6-25 / printed 5-24 — 20/76 body pages**.

`translation-en.md` preserves the PDF/printed-page headings and paragraph sequence. Completed batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-20 / printed 15-19
- Batch 4: PDF 21-25 / printed 20-24

### E2 / E3 — NOT STARTED

Independent English fidelity review and final end-to-end Tamil→English verification have not begun. Do **not** begin E2 until the full E1 body translation is complete.

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

## E1 Batch 1 — PDF 6-10 / printed 5-9

Completed and committed. Preserve emphatic repetitions and rhetorical questions; keep page-spanning sentences page-spanning where practical. `கல்லூரனாக` was conservatively rendered as “a college man.”

## E1 Batch 2 — PDF 11-15 / printed 10-14

Completed and committed. PDF 10→11 and 11→12 continuations remain explicit. The difficult frozen phrase `கேள்வி ஞானங்களைத் தூர்த்திடும் போதனைகள்` is rendered closely with a translator/source note. The agricultural `ஏற்றம்` is rendered as a water-lift. Labour repetitions are preserved.

## E1 Batch 3 — PDF 16-20 / printed 15-19

Completed and committed. `திண்ணைப்பள்ளி` is retained as a *thinnai* school. PDF 17→18 and 18→19 continuations remain explicit. `கல்வி கற்கு மிடம்` is translated closely without correcting the frozen Tamil. The uncertain `எட்டுச்சுரையெனப்` is retained in Tamil with a translator/source note rather than assigned an unsupported meaning. PDF 20 ends with an unfinished clause and was deliberately left open for PDF 21.

## E1 Batch 4 — PDF 21-25 / printed 20-24

Completed and committed.

Important translation decisions:

- PDF 20→21 continues explicitly: the clause about gaining clarity in life continues into living with firm resolve and school-life ideas serving as a guide.
- The resource/poverty contrast on PDF 21-22 retains the repeated rhetorical emphasis rather than being compressed.
- PDF 22→23 remains a page-spanning sentence: `இந்தத் திரு` / `நாட்டில்` is represented as “this sacred—” / “—land”.
- PDF 23's fatalist and Vedantic quotations are translated as quotations in source order without adding historical explanation.
- PDF 23→24 keeps `உள்ளபடி` / `உணர வேண்டும்` as an explicit English continuation: “understand it as it is—” / “—only then...”.
- PDF 24's source-supported `நல்லதங்கள்` is kept visible in Tamil rather than silently normalized. The irregular `நாவினை நாட்டினரும்` is rendered contextually and called out in a translator/source note.
- PDF 24→25 preserves `தெள்ளிய` / `வாழ்க்கை முறையை` as “a lucid—” / “—way of life”.
- PDF 25's difficult `தவழிப் பூச்சூடி` is retained in Tamil with a translator/source note rather than silently reconstructed.
- PDF 25 ends with the unfinished phrase about the weight of the schoolteacher's cane; English deliberately ends `the weight of the schoolteacher's cane—` for continuation on PDF 26.

## Source-fidelity safeguards carried into English

Traditional-glyph errors have already been resolved in the frozen Tamil. Translate the verified forms, not superseded T1 readings. Conversely, genuine source-supported oddities remain part of the frozen witness and must not be silently normalized.

## Exact next activity

Continue **E1 English translation with PDF pages 26-30 / printed pages 25-29** from `transcription-ta.md`.

For that batch:

1. retain the same PDF/printed-page headings in `translation-en.md`;
2. continue the unfinished PDF 25 sentence faithfully onto PDF 26;
3. translate every paragraph from the frozen Tamil, with no omitted clause or added historical explanation;
4. preserve repetition and rhetorical questions rather than smoothing them away;
5. flag any genuinely difficult frozen Tamil with a concise translator/source note rather than silently correcting it;
6. update `metadata.json`, `README.md`, and this `HANDOVER.md` with E1 page progress after the batch.

## Safeguards

- Scan remains the authority behind the frozen Tamil; frozen Tamil is the authority for English.
- Do not modernize or sanitize difficult historical language.
- Do not infer speech date, venue, event, occasion, or audience from publication data or outside knowledge.
- Do not commit the source PDF.
- T2 evidence and `t3-final-verification.md` are permanent audit records.