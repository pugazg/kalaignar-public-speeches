# HANDOVER — முத்துக் குளியல் — பாகம் I

## Repository

- repository — `pugazg/kalaignar-public-speeches`;
- branch — `main`;
- collection — `collections/muthukkuliyal-part-1/`;
- **LIVE MAIN IS AUTHORITATIVE**.

## Source model

- original source — `TVA_BOK_0065801_முத்துக்குளியல்_பாகம்_1.pdf`;
- original extent — **641 scans**, user-confirmed;
- approximate original size — **1.82 GB**;
- user-created splits — **39** exact-range PDFs;
- binaries — **not committed**;
- authority — rendered scan pixels only;
- OCR / web / alternate editions — **not used**.

## Durable split ledger

- split 001 — scans **1–17** — PASS — SHA256 `fbcfc6c1ef07528c37ed8804cdcaea39b2f08b459b4896b649e1b06a24b5179d`;
- split 002 — scans **18–33** — PASS — SHA256 `ec425a2314344d78a4d9fad743896356ccce6d15dace20dba0360fb743c7d861`;
- split 003 — scans **34–49** — PASS — SHA256 `a5b47180a171b161f45d6c796ef5c90d5f1a66478191fdc36401dc5d69f41549`;
- split 004 — scans **50–65** — PASS — SHA256 `6848c3cd48611d60294215dd42aacd263fb0941c6b267e1efad4256edc1bbf2b`.

Continuity **1–65** — **PASS / no gap / no overlap**.  
Mapping — **PDF = printed + 1** confirmed through scan 65.  
Contents — **61/61 COMPLETE**.

## Authoritative incremental policy

Do not wait for all 39 splits.

For each fully bounded constituent:
**source gate → T1 → T2 → T3/freeze → English E1 → E2 → E3 → repository closure**.

For a constituent spanning a split, verify all supplied pages now and carry only the missing tail forward.

## Closed constituents

1. **வள்ளலார் வழி எது?** — PDF18–28 — Tamil + English verified — **FULLY ARCHIVED**.
   - direct scan corrected earlier intake reading `வள்ளுவர்` → **`வள்ளலார்`**.
2. **வள்ளுவர்க்கோர் ஆலயம்** — PDF29–32 — Tamil + English verified — **FULLY ARCHIVED**.
3. **கம்பர் விழா (1)** — PDF33–41 — Tamil + English verified — **FULLY ARCHIVED**.
4. **கம்பர் விழா (2)** — PDF42–56 — Tamil + English verified — **FULLY ARCHIVED after fidelity repair**.
   - cross-split 49→50 PASS;
   - closing note: **1974-04-04 / காரைக்குடி / கம்பர் விழா / ஆற்றிய உரை**;
   - resolved post-closure repair: restored omitted **PDF54 / printed p.53** in Tamil and English, corrected PDF55/PDF56 section boundaries, final explicit headings **15/15** in both layers, unresolved **0**.
5. **ஏழையின் சிரிப்பில்** — PDF57–63 — Tamil + English verified — **FULLY ARCHIVED**.
   - closing note: **1969-11-27 / சண்டிகார் / குருநானக் 500-ஆவது ஆண்டு பிறந்த தின விழா / ஆற்றிய உரை**.

## C4 repair checkpoint

`கம்பர் விழா (2)` remains **CLOSED / FULLY ARCHIVED**, with closure **REVALIDATED** after one post-closure fidelity repair.

- affected source: PDF **53–56** / printed **52–55**;
- omitted PDF54 / printed53 restored;
- shifted PDF55–56 boundaries corrected;
- visible source parenthetical verse forms restored;
- final page structure: **Tamil 15/15 / English 15/15**;
- unresolved: **0**.

## Active constituent 6 — `கலை வளர்ப்போம்`

- provisional full range — PDF **64–69** / printed **63–68**;
- currently supplied / durable — PDF **64–65** / printed **63–64**;
- T1 — **2/2 COMPLETE**;
- T2 — **2/2 PASS / 0 unresolved**;
- join 64→65 — **PASS**;
- closing note / ending — **not yet supplied**;
- T3/freeze — blocked pending PDF66–69;
- English — blocked pending frozen Tamil;
- do not re-read PDF64–65 unless a new fidelity issue appears.

## Current totals

- splits — **4/39**;
- scans — **1–65 / 641**;
- started — **6/61**;
- source-gated — **5/61**;
- Tamil verified — **5/61**;
- English verified — **5/61**;
- fully archived — **5/61**.

## Exact next activity

The next split must begin at **original scan 66**.

1. verify split continuity;
2. transcribe/audit only C6's new tail PDF66–69;
3. verify C6 closing note / boundary;
4. T3 freeze C6;
5. English E1/E2/E3 and repository closure C6;
6. process any subsequent fully bounded constituents in that same split through closure;
7. checkpoint any final boundary-spanning constituent at the highest safe page-level state.
