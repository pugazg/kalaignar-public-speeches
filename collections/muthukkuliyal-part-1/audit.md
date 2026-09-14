# Audit — முத்துக் குளியல் — பாகம் I

## Source intake through split 013

**PASS — continuous original scans 1–209 / 641.**

| Split | Scans | Pages | State | SHA-256 |
|---|---:|---:|---|---|
| 011 | 162–177 | 16 | PASS | `f3402df27678ef8b711358363618cc67bd8d610eee67e0a0f74f37bd89fca971` |
| 012 | 178–193 | 16 | PASS | `0d70dc5150ee33a3e3769ffe92cab2c5e2918f79cda1b9a67548e8415981081e` |
| 013 | 194–209 | 16 | PASS | `5b85e25417856354772d66311503fadfef761e72768f35682cf76d281730f6bc` |

- gaps / overlaps through scan209 — **0 / 0**;
- mapping — **PDF = printed + 1** confirmed through scan209;
- OCR — **not used**;
- web / alternate source — **not used**;
- source binaries committed — **No**.

## Closure state

Constituents **1–27 — CLOSED / FULLY ARCHIVED**.

For C21–C27:
- source gates — **PASS / COMPLETE**;
- Tamil T1/T2/T3 — **COMPLETE / PASS / PASS**;
- Tamil — **verified-complete / FROZEN**;
- English E1/E2/E3 — **COMPLETE / PASS / PASS**;
- English — **verified-complete**;
- unresolved — **0**.

Boundary checks:
- C23 split 011→012 join **PDF177→178 PASS**;
- C26 split 012→013 join **PDF193→194 PASS**.

## Constituent 28 — `யாதும் ஊரே யாவரும் கேளிர்!` partial

**DURABLE T2 CHECKPOINT — PDF205–209 / 5 of provisional 7 pages.**

- opening/title — **PASS**;
- available joins — **4/4 PASS**;
- T1 supplied pages — **5/5 COMPLETE**;
- T2 supplied pages — **5/5 PASS / 0 unresolved**;
- closing note / terminal boundary — **not supplied**;
- T3/freeze — **BLOCKED pending PDF210–211**;
- English — **BLOCKED pending frozen Tamil**.

## Totals

- contents — **61/61**;
- splits — **13/39**;
- source-gated — **27/61**;
- Tamil verified — **27/61**;
- English verified — **27/61**;
- fully archived — **27/61**;
- active partial — **C28 PDF205–209 T2-verified**.

## Next gate

**Next split beginning PDF210. Complete C28 tail and close it, then continue incremental per-split closure.**
