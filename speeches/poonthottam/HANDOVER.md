# கலைஞரின் பூந்தோட்டம் - working handover

This handover records the current state of `speeches/poonthottam/` after **T2 strict audit completion**. It exists so continuation proceeds from the exact next incomplete gate without restarting source inspection, T1 transcription, or the completed T2 audit.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/poonthottam/`
- Stable slug: `poonthottam`

## Source identity

- Source filename: `TVA_BOK_0065784_கலைஞரின்_பூந்தோட்டம்.pdf`
- SHA-256: `2a8bf5f6f42970ee95912f41662f9bc448581a5aaca15a55fee9b44ba20a4c52`
- File size: `49,297,657` bytes
- Actual PDF page count: `18`
- Source binary committed: **No - repository policy prohibits uploading the source PDF**

## Source-established speech facts

- Speech title in body: `பூந்தோட்டம்`;
- speech date: **1951-12-06**;
- venue: **சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி**;
- speaker: **தோழர் மு.கருணாநிதி**;
- event/occasion: **not separately stated**;
- audience: **not explicitly stated**.

Title-page wording:

`சென்னை கிண்டி இன்ஜினியரிங் கல்லூரியில் 06.12.1951இல் தோழர் மு.கருணாநிதி ஆற்றிய சொற்பொழிவு`

Do not replace these source-grounded fields with historical inference.

## Canonical page map

- PDF 1 - front cover
- PDF 2 - title page / speaker photo / explicit speech date and venue
- PDF 3 - bibliographic page (`நூல் குறிப்பு`)
- PDF 4 - publisher preface (`பதிப்புரை`)
- PDF 5 - prefatory poem `எரிமலை! (மு.கருணாநிதி)`
- PDF 6-17 - speech body, printed pages 5-16 (**12 pages total**)
- PDF 18 - back cover / promotional matter / barcode

The speech begins on PDF 6 under `பூந்தோட்டம்` and ends on PDF 17 with printed `வணக்கம்`.

## Scan-specific safeguards

- Blue circular library stamp on PDF 2 overlaps the title-page area: later marking, not edition text.
- Blue circular library stamp on PDF 17 lies below the speech ending: later marking, not edition text.
- Light bleed-through occurs on interior pages: do not transcribe reverse-side ghost text.
- The scan is authoritative; OCR/parsed text is only an aid.

## Workflow state

### Gate 1 - source inspection / bibliographic and page map

**COMPLETE.**

### Gate 2 / T1 - Tamil first-pass transcription

**FIRST-PASS COMPLETE - 12 / 12 speech pages drafted.**

### Gate 3 / T2 - strict line-by-line visual Tamil audit

**COMPLETE - 12 / 12 speech pages audited.**

Completed T2 batches:

- Batch 1: PDF 6-10 / printed 5-9
- Batch 2: PDF 11-15 / printed 10-14
- Batch 3: PDF 16-17 / printed 15-16

Batches 1 and 2 required no wording corrections. Batch 3 identified two scan-confirmed first-pass errors on printed p.15 and these are already corrected in `transcription-ta.md`:

- `புரிவோடு` → **`பூரிப்போடு`**;
- `வளர்த்தான்` → **`வளரத்தான்`**.

Other final-batch readings confirmed from the scan include `தாயைக் கட்டிலறைக் கழைத்து`, `வைகைக் கரையிலே`, `மோட்சலோக ‘பாஸ்போர்ட்’டன்`, separate `கை முஷ்டி` / joined `கைமுஷ்டி`, `பூர்ஷ்வாத் தன்மை`, `அப்படி நடைபோடும் நல்லதம்பிகளைத்தான்`, `மானிடம்`, and the printed final `வணக்கம்`.

### Gate 4 / T3 - Tamil consolidation and freeze

**NOT STARTED - THIS IS THE EXACT NEXT GATE.**

T3 must run across the complete speech body before Tamil can be frozen as `verified-complete`.

### English gates

All **NOT STARTED / BLOCKED** until T3 passes and Tamil is explicitly `verified-complete`.

## Confirmed T2 page-boundary points to carry into T3

- printed p.5 → p.6 continues `பண்படுத்த` / `வேண்டும்.`;
- printed p.6 → p.7 continues `...மொண்டு மொண்டு தரும்` / `தென்றலாக, ...`;
- printed p.10 → p.11 continues `வேலைகளை விட்டு ஓய்வு` / `பெறுகிறவர் ...`;
- printed p.15 → p.16 is a thought/sentence continuation ending `வேண்டாத ஒரு வெறுப்பு வளரத்தான் நேரிடும்.` and resuming `அந்த வெறுப்பு...`; no word is split.

Do not collapse these page boundaries in a way that creates omitted or duplicated wording.

## Exact next activity

Perform **Stage T3 - Tamil consolidation / page-boundary / stale-reading check** across the complete `transcription-ta.md`, PDF 6-17 / printed 5-16.

Required T3 checks:

1. confirm both T2 corrections (`பூரிப்போடு`, `வளரத்தான்`) are present and the superseded readings (`புரிவோடு`, `வளர்த்தான்`) no longer survive in the speech text;
2. review every PDF-page boundary for accidental duplication, omission, broken words, or lost punctuation;
3. check all unusual source forms confirmed in T2 against the consolidated text so later editing has not normalized them;
4. confirm running headers, bleed-through and the PDF 17 library stamp remain excluded;
5. perform an end-to-end stale-reading check of the complete Tamil body.

If and only if T3 passes, update `transcription-ta.md`, `metadata.json`, `README.md`, `audit.md`, and this handover to mark the Tamil layer **`verified-complete`**. Then English translation may begin as the next separate stage.

## Repository synchronization note

The root catalogue remains unchanged. Root catalogue synchronization belongs to archival closure after all textual and translation gates pass.
