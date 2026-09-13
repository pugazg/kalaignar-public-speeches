# HANDOVER — முத்துக் குளியல் — பாகம் I

## Repository

- repository: `pugazg/kalaignar-public-speeches`;
- branch: `main`;
- collection: `collections/muthukkuliyal-part-1/`;
- live `main` is authoritative.

## Controlling-source model

The original source is user-confirmed as **641 PDF pages**, approximately **1.82 GB**. It has been split by the repository owner into **39 exact-range PDFs**, each <= about 49 MB. Treat the splits as one source.

Original expected source name: `TVA_BOK_0065801_முத்துக்குளியல்_பாகம்_1.pdf`.

Original binary / SHA-256: **not available yet / not committed**.

## Durable intake state

Splits **1–3 / 39** received and inspected:

- split 001 — scans **1–17** — **17/17 PASS** — SHA-256 `fbcfc6c1ef07528c37ed8804cdcaea39b2f08b459b4896b649e1b06a24b5179d`;
- split 002 — scans **18–33** — **16/16 PASS** — SHA-256 `ec425a2314344d78a4d9fad743896356ccce6d15dace20dba0360fb743c7d861`;
- split 003 — scans **34–49** — **16/16 PASS** — SHA-256 `a5b47180a171b161f45d6c796ef5c90d5f1a66478191fdc36401dc5d69f41549`;
- continuity **1–49**: **PASS — no gap / no overlap**;
- no parsed text layer; scan pixels controlling;
- OCR / web / alternate source use: **none**.

Contents remain **COMPLETE — 61/61**.

Body mapping remains **CONFIRMED: PDF scan = printed page + 1** through scan 49.

### Source-gated constituents

1. `வள்ளுவர் வழி எது?` — PDF **18–28** / printed **17–27** — **11/11 PASS**.
2. `வள்ளுவர்க்கோர் ஆலயம்` — PDF **29–32** / printed **28–31** — **4/4 PASS**.
3. `கம்பர் விழா (1)` — PDF **33–41** / printed **32–40** — **9/9 PASS**; all **8/8** joins pass including cross-split **33→34**; closing note source gives **April 1969 / காரைக்குடி / கம்பர் விழா / ஆற்றிய உரை**, exact day not stated.

### Active constituent 4

`கம்பர் விழா (2)`

- opening PDF **42** / printed **41**: **VERIFIED**;
- currently inspected PDF **42–49** / printed **41–48** — **8/15 provisional pages**;
- available joins: **7/7 PASS**;
- expected remaining under contents map: PDF **50–56** / printed **49–55**;
- source gate: **INCOMPLETE**.

## Revised workflow policy — effective now

The earlier rule to wait for all **39 splits** before beginning Tamil T1 was a workflow choice, not a technical requirement. It is now **retired**.

Going forward, every newly supplied split is processed to the **maximum durable state supported by the pages currently available**:

1. source / duplicate / boundary gate;
2. Tamil T1;
3. Tamil T2 strict direct-scan fidelity audit;
4. Tamil T3 consolidation / freeze;
5. English E1 / E2 / E3;
6. repository closure **for every constituent whose full opening-to-closing boundary is present**.

For a constituent that crosses a split boundary, process all currently supplied pages immediately to a durable page-level checkpoint. Do not invent the missing tail and do not mark the constituent closed until the closing boundary is supplied. When the next split arrives, continue only the missing tail / join / final closure work. Previously verified pages should not require re-reading unless a new source-fidelity issue appears.

This means the already supplied material should now be handled as follows:

- constituent 1 `வள்ளுவர் வழி எது?` — **eligible for T1 → repository closure now**;
- constituent 2 `வள்ளுவர்க்கோர் ஆலயம்` — **eligible for T1 → repository closure now**;
- constituent 3 `கம்பர் விழா (1)` — **eligible for T1 → repository closure now**;
- constituent 4 `கம்பர் விழா (2)` — only PDF **42–49 / printed 41–48** are currently available; process these pages now to a durable page-level checkpoint, but final constituent freeze / English final verification / repository closure must wait for PDF **50–56**.

## Workflow status

- source inspection: **IN PROGRESS**;
- splits received: **3/39**;
- scans covered: **1–49 / 641**;
- contents: **61/61 COMPLETE**;
- constituent source gates: **3/61 COMPLETE**;
- fully bounded constituents eligible for immediate full workflow: **1–3**;
- active partial constituent: **4 / 61 — PDF42–49 available, PDF50–56 pending**;
- collection-wide transcription/translation is now **incremental per split**, not deferred.

## Exact next activity

Retroactively process constituents **1–3 from Tamil T1 through repository closure**, then process constituent 4's currently available pages **42–49** to the highest safe page-level checkpoint without pretending the constituent is complete.

After that, each future split should be closed as far as its evidence allows before moving on.
