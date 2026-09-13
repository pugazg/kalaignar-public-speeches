# முத்துக் குளியல் — பாகம் I

Source-first archival workflow for `முத்துக் குளியல் / பாகம் - I` by **கலைஞர் மு. கருணாநிதி**.

## Controlling source model

The repository owner confirms that the original PDF has **641 scans** and is approximately **1.82 GB**. It has been split into **39 exact-range PDF pieces**. The pieces are treated as **one controlling source**, not as independent editions.

Source binaries are **not committed**. Rendered scan pixels are controlling; OCR, web copies and alternate editions are not used for source transcription or fidelity review.

## Publication identity

- title — **முத்துக் குளியல் — பாகம் I**;
- author — **கலைஞர் மு. கருணாநிதி**;
- subject — **சொற்பொழிவுகளின் தொகுப்பு**;
- publisher — **பூம்புகார் பதிப்பகம்**;
- publication no. — **450**;
- price — **ரூ. 200/-**;
- print run — **2000**;
- source gives both:
  - `முதற் பதிப்பு : மே 2000`;
  - `காலம் : ஜூன் 2000`.
  
These two source month statements remain separate and are not silently reconciled.

## Split ledger

| Split | Original scans | Pages | Bytes | SHA-256 | State |
|---|---:|---:|---:|---|---|
| 001 | 1–17 | 17 | 48,686,831 | `fbcfc6c1ef07528c37ed8804cdcaea39b2f08b459b4896b649e1b06a24b5179d` | PASS |
| 002 | 18–33 | 16 | 47,901,860 | `ec425a2314344d78a4d9fad743896356ccce6d15dace20dba0360fb743c7d861` | PASS |
| 003 | 34–49 | 16 | 48,934,218 | `a5b47180a171b161f45d6c796ef5c90d5f1a66478191fdc36401dc5d69f41549` | PASS |
| 004 | 50–65 | 16 | 46,954,298 | `6848c3cd48611d60294215dd42aacd263fb0941c6b267e1efad4256edc1bbf2b` | PASS |

Continuous coverage is now **1–65 / 641**, with **no gap / no overlap**. The body relation **PDF scan = printed page + 1** is confirmed through scan 65.

## Contents

The complete contents were captured from split 001: **61/61 constituents**.

A later direct-scan fidelity review corrected the first contents/title reading from the provisional `வள்ளுவர் வழி எது?` to the source-supported **`வள்ளலார் வழி எது?`**. The closing-note event likewise reads **`வள்ளலார் விழா`**.

See `page-map.md` for all 61 mapped ranges.

## Incremental per-split workflow

Each supplied split is processed immediately to the maximum durable state supported by its pages:

**source gate → Tamil T1 → T2 → T3/freeze → English E1 → E2 → E3 → repository closure** for every fully bounded constituent.

When a constituent crosses a split boundary, the supplied pages are verified immediately and only the missing tail / closing boundary / final closure is carried forward.

## Closed constituents

### 1 — `வள்ளலார் வழி எது?`

- directory — `speeches/vallalar-vazhi-ethu/`;
- PDF **18–28** / printed **17–27** — **11/11**;
- Tamil — **verified-complete / FROZEN**;
- English — **verified-complete**;
- repository closure — **FULLY ARCHIVED**.

### 2 — `வள்ளுவர்க்கோர் ஆலயம்`

- directory — `speeches/valluvarkkor-aalayam/`;
- PDF **29–32** / printed **28–31** — **4/4**;
- Tamil — **verified-complete / FROZEN**;
- English — **verified-complete**;
- repository closure — **FULLY ARCHIVED**.

### 3 — `கம்பர் விழா (1)`

- directory — `speeches/kambar-vizha-1/`;
- PDF **33–41** / printed **32–40** — **9/9**;
- all **8/8** joins PASS, including cross-split **33→34**;
- source gives **April 1969** only; exact day not stated;
- Tamil / English — **verified-complete**;
- repository closure — **FULLY ARCHIVED**.

### 4 — `கம்பர் விழா (2)`

- directory — `speeches/kambar-vizha-2/`;
- PDF **42–56** / printed **41–55** — **15/15**;
- split 003 supplies PDF42–49; split 004 supplies PDF50–56;
- all **14/14** joins PASS, including cross-split **49→50**;
- closing note — **1974-04-04 / காரைக்குடி / கம்பர் விழா / ஆற்றிய உரை**;
- Tamil / English — **verified-complete**;
- repository closure — **FULLY ARCHIVED after post-closure fidelity repair**;
- resolved repair — omitted **PDF54 / printed p.53** restored in Tamil and English; following headings remapped to PDF55/PDF56; final page headings **15/15 / 15/15**; unresolved **0**.

### 5 — `ஏழையின் சிரிப்பில்`

- directory — `speeches/ezhaiyin-sirippil/`;
- PDF **57–63** / printed **56–62** — **7/7**;
- all **6/6** joins PASS;
- closing note — **1969-11-27 / சண்டிகார் / குருநானக் 500-ஆவது ஆண்டு பிறந்த தின விழா / ஆற்றிய உரை**;
- Tamil / English — **verified-complete**;
- repository closure — **FULLY ARCHIVED**.

## Active partial constituent

### 6 — `கலை வளர்ப்போம்`

- directory — `speeches/kalai-valarppom/`;
- provisional full range — PDF **64–69** / printed **63–68** — 6 pages;
- supplied so far — PDF **64–65** / printed **63–64** — **2/6**;
- opening/title — **VERIFIED**;
- join **64→65 — PASS**;
- Tamil T1 on supplied pages — **2/2 COMPLETE**;
- Tamil T2 on supplied pages — **2/2 PASS / 0 unresolved**;
- Tamil T3 / freeze — **blocked only by missing PDF66–69**;
- English — blocked pending frozen Tamil.

The PDF64–65 checkpoint is durable and does not need to be re-read when the next split arrives unless a new fidelity issue appears.

## Current collection state

- splits received — **4/39**;
- scans covered — **1–65 / 641**;
- contents — **61/61**;
- source-gated — **5/61 complete**;
- Tamil verified — **5/61**;
- English verified — **5/61**;
- fully archived — **5/61**;
- active partial — **6 / 61, PDF64–65 T2-verified**.

## Exact next activity

Ingest the next split beginning at **original scan 66**. Complete `கலை வளர்ப்போம்` PDF66–69, verify its closing note and next boundary, then perform **T3 → English E1/E2/E3 → repository closure**. Continue processing every later fully bounded constituent in that split through closure before moving on.
