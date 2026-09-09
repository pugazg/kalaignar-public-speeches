# HANDOVER — முத்துக்குளியல் — பாகம் II

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Collection directory: `collections/muthukkuliyal-part-2/`

## Controlling source

- Filename: `TVA_BOK_0065802_முத்துக்குளியல்_பாகம்_2.pdf`
- SHA-256: `48631b4fc5258df33213dbb742aec70ff6aace4fcd294f377e5750b406f5d9b2`
- Byte size: `232,470,104`
- Actual PDF scans: **425**
- Source binary committed: **No**
- Source classification: **multi-speech collection / `சொற்பொழிவுகளின் தொகுப்பு`**

## Mapping state

- contents entries captured: **36 / 36 — COMPLETE**
- constituent printed-page ranges mapped: **36 / 36 — COMPLETE**
- constituent PDF scan ranges mapped: **36 / 36 — COMPLETE**
- constituent archives started: **2 / 36**
- constituent Tamil T1 complete: **1 / 36**
- constituent Tamil T2/T3 complete: **1 / 36**
- constituent Tamil verified: **1 / 36**
- constituent English E1/E2/E3 complete: **1 / 36**
- constituent archives fully completed: **1 / 36**

The stable body relationship is `PDF scan = printed page + 1` for PDF 12–424 / printed 11–423.

## Closed constituent 1 / 36

`தேசிய இளைஞர் கொண்டாட்டத் தொடக்கவிழா` — `speeches/desiya-ilainjar-kondatta-thodakka-vizha/` — **CLOSED / FULLY ARCHIVED**. Tamil and English are both `verified-complete`; no text work is pending.

## Active constituent 2 / 36

**`முரசொலி அறக்கட்டளை விருது வழங்கு விழா`**  
Speech tree: `speeches/murasoli-arakkattalai-virudhu-vazhangu-vizha/`  
Contents date: **13-01-98**  
Printed pages: **18–32**  
PDF scans: **19–33**  
Mapped body pages: **15**

### Source gate — PASS / COMPLETE

Live `main` was searched for exact title, closing-note variant and likely slug terms; no existing equivalent archive was found.

Direct source inspection establishes:

- heading: `முரசொலி அறக்கட்டளை விருது வழங்கு விழா` on PDF 19 / printed p.18;
- speech body ends on PDF 33 / printed p.32;
- separate closing note: `13-1-98 அன்று முரசொலி அறக்கட்டளை விருது வழங்கும் விழாவில் ஆற்றிய உரை`;
- date: **1998-01-13**;
- event wording: **`முரசொலி அறக்கட்டளை விருது வழங்கும் விழா`**;
- source role: **`ஆற்றிய உரை`**;
- venue: **not stated in inspected opening/closing evidence**; do not infer it from contextual mentions of Chennai.

### Tamil T1

- Batch 1 PDF **19–23** / printed **18–22**: **DONE**;
- total drafted: **5 / 15**;
- Batch 2 PDF **24–28** / printed **23–27**: **NEXT**;
- Batch 3 PDF **29–33** / printed **28–32**: pending.

T2, T3 and English remain blocked until T1 is complete.

## Important cautions

- `transcription-ta.md` is first-pass only; do not treat current wording as scan-verified before T2.
- preserve unusual source spelling/wording; do not modernize silently.
- PDF 23 ends mid-sentence at `அதை அடமானம்`; inspect PDF 24 directly before joining the continuation.
- the closing note is metadata, not speech body text.
- do not commit the source PDF binary.

## Exact next incomplete gate

Continue constituent **2 / 36** with **Tamil T1 batch 2 — PDF 24–28 / printed 23–27**. Commit the five-page first pass and synchronize speech and collection controls. Do not begin T2 or English in that iteration.
