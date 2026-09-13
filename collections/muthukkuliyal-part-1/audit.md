# Audit — முத்துக் குளியல் — பாகம் I

## Source intake through split 007

**PASS — continuous original scans 1–114 / 641.**

| Split | Scans | Pages | State | SHA-256 |
|---|---:|---:|---|---|
| 001 | 1–17 | 17 | PASS | `fbcfc6c1ef07528c37ed8804cdcaea39b2f08b459b4896b649e1b06a24b5179d` |
| 002 | 18–33 | 16 | PASS | `ec425a2314344d78a4d9fad743896356ccce6d15dace20dba0360fb743c7d861` |
| 003 | 34–49 | 16 | PASS | `a5b47180a171b161f45d6c796ef5c90d5f1a66478191fdc36401dc5d69f41549` |
| 004 | 50–65 | 16 | PASS | `6848c3cd48611d60294215dd42aacd263fb0941c6b267e1efad4256edc1bbf2b` |
| 005 | 66–82 | 17 | PASS | `962e0c572fb86f8ee45eeff6abcd6bf81e933b7c59023c6c979851f271220916` |
| 006 | 83–98 | 16 | PASS | `1eca8cd01d310515f000ca3c9ebc766b8271463ebed4db8fe4530a3d67d90cef` |
| 007 | 99–114 | 16 | PASS | `61efd5d8c6b55f1a46faec8ae66a47fcdd60656a75f7f3535ad3ca87fff274f0` |

- gaps / overlaps — **0 / 0**;
- mapping — **PDF = printed + 1** confirmed through scan114;
- OCR — **not used**;
- web / alternate source — **not used**;
- source binaries committed — **No**.

## Closure state

Constituents **1–13 — CLOSED / FULLY ARCHIVED**.

For C6–C13:
- source gates — **PASS / COMPLETE**;
- Tamil T1/T2/T3 — **COMPLETE / PASS / PASS**;
- Tamil — **verified-complete / FROZEN**;
- English E1/E2/E3 — **COMPLETE / PASS / PASS**;
- English — **verified-complete**;
- unresolved — **0**.

### Fidelity repairs in this block

- C11 `தமிழிசை இயக்கம்`: incorrect C10 material in the PDF95 title-page section was removed; PDF95–98 were reverified and Tamil re-frozen before English.
- C13 `மொழிமானம் பெறுவோம்`: missing PDF111 / printed110 content and the PDF110→111→112 boundary were restored; Tamil was reverified/re-frozen before English.

## Constituent 14 — `கருத்துச் சுதந்திரம்` partial

**DURABLE T2 CHECKPOINT — PDF113–114 / 2 of provisional 6 pages.**

- opening/title — **PASS**;
- join113→114 — **PASS**;
- T1 supplied pages — **2/2 COMPLETE**;
- T2 supplied pages — **2/2 PASS / 0 unresolved**;
- closing note / terminal boundary — **not supplied**;
- T3/freeze — **BLOCKED pending PDF115–118**;
- English — **BLOCKED pending frozen Tamil**.

## Totals

- contents — **61/61**;
- splits — **7/39**;
- source-gated — **13/61**;
- Tamil verified — **13/61**;
- English verified — **13/61**;
- fully archived — **13/61**;
- active partial — **C14 PDF113–114 T2-verified**.

## Next gate

**Next split beginning PDF115. Complete C14 tail and close it, then continue incremental per-split closure.**
