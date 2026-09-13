# முத்துக் குளியல் — பாகம் I

Source-intake layer for `முத்துக் குளியல் / பாகம் - I` by **கலைஞர் மு. கருணாநிதி**.

## Source plan

The repository owner confirms that the original PDF has **641 pages** and is approximately **1.82 GB**. Because the original cannot be attached directly, it has been split into **39 exact-range PDF pieces**, each no larger than about 49 MB. These splits together are to be treated as **one controlling source**, not as independent editions.

Received so far:

- split 001 — `...part_001_pages_1-17.pdf` — scans **1–17**, 17 pages, **48,686,831** bytes, SHA-256 `fbcfc6c1ef07528c37ed8804cdcaea39b2f08b459b4896b649e1b06a24b5179d`;
- split 002 — `...part_002_pages_18-33.pdf` — scans **18–33**, 16 pages, **47,901,860** bytes, SHA-256 `ec425a2314344d78a4d9fad743896356ccce6d15dace20dba0360fb743c7d861`;
- split 003 — `...part_003_pages_34-49.pdf` — scans **34–49**, 16 pages, **48,934,218** bytes, SHA-256 `a5b47180a171b161f45d6c796ef5c90d5f1a66478191fdc36401dc5d69f41549`;
- continuity: **PASS — exact 1–49 coverage, no gap / no overlap**;
- parsed text layer: **none**; rendered scan pixels are controlling;
- source / split binaries: **not committed**.

## Bibliographic identity from split 001

- title: **முத்துக் குளியல் — பாகம் I**;
- author: **கலைஞர் மு. கருணாநிதி**;
- subject: **சொற்பொழிவுகளின் தொகுப்பு**;
- publisher: **பூம்புகார் பதிப்பகம்**;
- publication no.: **450**;
- price: **ரூ. 200/-**;
- print run: **2000**;
- size: **14 x 21 C.M.**;
- type size: **14 புள்ளி**;
- rights: **ஆசிரியருக்கே**;
- printer: **ஈகிள் பிரஸ், சென்னை - 13**.

The source contains two different month statements and they must not be silently reconciled:

- scan 3: **`முதற் பதிப்பு : மே 2000`**;
- scan 5: **`காலம் : ஜூன் 2000`**.

## Front matter / contents

Split 001 is entirely front matter. Scans **12–16** contain the complete contents, listing **61 constituent speeches**. No speech body begins inside scans 1–17.

The numbered-page relation **PDF scan = printed page + 1** is now **CONFIRMED for the speech body**: scan 18 is printed p.17 and opens constituent 1; scan 29 is printed p.28 and opens constituent 2; scan 33 is printed p.32 and opens constituent 3.

The foreword states that the speeches are issued as **two volumes, Part I and Part II**. The publisher's note describes the collection as selected speeches from 1969 onward, chosen for continuing relevance across art, literature, society, politics and economics.

See `page-map.md` for the full **61-item contents inventory** and provisional ranges.

## Split 002 source findings

Split 002 covers original scans **18–33** / printed pages **17–32**.

- constituent 1 `வள்ளுவர் வழி எது?` — PDF **18–28** / printed **17–27** — **11/11 source-gated / PASS**;
- constituent 2 `வள்ளுவர்க்கோர் ஆலயம்` — PDF **29–32** / printed **28–31** — **4/4 source-gated / PASS**;
- constituent 3 `கம்பர் விழா (1)` — opening confirmed at PDF **33** / printed **32**.

## Split 003 source findings

Split 003 covers original scans **34–49** / printed pages **33–48** and continues seamlessly from split 002.

### Constituent 3 — `கம்பர் விழா (1)`

**SOURCE-GATED / PASS — 9/9 pages total.**

- full range: PDF **33–41** / printed **32–40**;
- PDF33 is in split 002; PDF34–41 are split 003 extract pages 1–8;
- cross-split join **33→34 PASS**;
- all joins **8/8 PASS**;
- closing note on PDF41:
  `1969-ஆம் ஆண்டு ஏப்ரல் திங்கள் / காரைக்குடி கம்பர் விழாவில் / ஆற்றிய உரை.`;
- source gives **April 1969 only; exact day not stated**;
- source-explicit venue / event / role: **காரைக்குடி / கம்பர் விழா / ஆற்றிய உரை**;
- duplicate / boundary unresolved: **0 / 0**.

### Constituent 4 — `கம்பர் விழா (2)`

- opening PDF **42** / printed **41**: **VERIFIED**;
- current inspected coverage: PDF **42–49** / printed **41–48** — **8 pages**;
- available joins **42→43 ... 48→49 = 7/7 PASS**;
- provisional full range from contents: PDF **42–56** / printed **41–55** — **15 pages**;
- source gate remains **INCOMPLETE** because PDF50–56 are not yet supplied.

## Workflow state

- source splits received: **3/39**;
- original scan coverage received: **1–49 / 641**;
- contents: **CAPTURED 61/61**;
- page map: **PROVISIONAL FROM CONTENTS; boundaries directly verified through constituent 3**;
- source/body offset: **CONFIRMED — PDF = printed + 1 through scan 49**;
- constituent source gates: **3/61 complete**;
- active source intake: constituent **4**, PDF42–49 inspected;
- Tamil transcription: **NOT STARTED**;
- English translation: **NOT STARTED**.

## Revised per-split processing policy

The collection no longer waits for all 39 source pieces before transcription.

For every split:
- inspect and source-gate all supplied pages;
- fully process any complete constituent through **T1 → T2 → T3 → English E1/E2/E3 → repository closure**;
- for a constituent crossing the split boundary, process the supplied pages now and carry forward only the missing tail / final boundary / final closure work.

Current implication:
- constituents **1–3** can be closed now;
- constituent **4** can be processed for PDF **42–49**, but cannot be finally closed until PDF **50–56** is supplied.

## Exact next activity

Process constituents **1–3 from T1 through repository closure**, then checkpoint constituent 4 pages **42–49** to the highest safe durable state.
