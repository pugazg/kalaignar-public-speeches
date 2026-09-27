# HANDOVER — முல்லைக் கொல்லை

Repository: `pugazg/kalaignar-public-speeches`  
Branch: `main`  
Archive: `speeches/mullaik-kollai/`

## Durable source state

- parent — **முல்லைக் கொல்லை** (1954 source booklet)
- parent collection — `collections/mullaik-kollai-1954/`
- constituent — **1 / 5 — ACTIVE**
- source — `TVA_BOK_0064364_ முல்லைக்_கொல்லை.pdf`
- source ID — `TVA_BOK_0064364`
- SHA-256 — `1e14d215de1b109292ba2b2ba03f73cf844978d2d6b1bb4f912c3ca64733a15f`
- source range — **PDF7–18 / printed pp.7–18 / 12 pages**
- next boundary — **PDF19 — அத்தை மகள்**
- duplicate gate — **PASS**
- boundary gate — **PASS**
- Tamil T1 — **FIRST-PASS COMPLETE — PDF7–18 / 12/12 / 2 explicit unresolved**
- Tamil T2 — **IN PROGRESS — Batch 1 PDF7–11 COMPLETE / 5/12 pages / 19 corrections / 2 unresolved in audited pages**
- Tamil T3 — blocked pending T2
- English — blocked pending Tamil freeze
- speech date — **not established**
- venue — **not established**
- event — **not established**

Back-matter provenance says `முல்லைக் கொல்லை` appeared in `திராவிடன்` in December 1952. Do not convert that publication/provenance statement into a speech date without explicit source evidence.

## Historical Tamil rule

This source uses older Tamil typography. Apply `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` to every page and explicitly check the known historical families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Read character identity from enlarged source pixels; do not global-replace or modernize source wording.

## T1 durable checkpoint

- working Tamil — `transcription-ta.md`
- audit — `audit.md`
- T1 pages — **12/12 COMPLETE**
- explicit unresolved — **2**
  - PDF9 damaged right-edge terminal clause before PDF10;
  - PDF12 technical wing/anatomy phrase.
- page-boundary candidates — **8 logged**
- Tamil status — **FIRST-PASS COMPLETE / not verified / not frozen**

## T2 checkpoint after Batch 1

- audited — **PDF7–11 / 5/12 pages**
- cumulative corrections — **19**
- unresolved in audited pages — **2**
  - PDF8 physical left-edge loss after `காந்திப்`;
  - PDF9 physical right-edge loss ending `நான் சென்…`.
- explicit unresolved overall — **3**, including the pending PDF12 technical phrase
- boundary controls — **7→8 PASS / 9→10 unresolved / 10→11 PASS / 11→12 PASS**
- historical-glyph Batch 1 check — **COMPLETE**
- pages remaining — **PDF12–18 / 7 pages**

## Exact next activity

Tamil **T2 strict visual fidelity audit — Batch 2: PDF12–16 / printed pp.12–16 / 5 pages**.

Check every line directly against the rendered source. Resolve or preserve the PDF12 technical wing/anatomy phrase; verify PDF12→13, PDF13→14 and PDF14→15; and record all source-supported corrections in `audit.md` / `transcription-ta.md`.

Do **not** begin the final T2 batch, T3 or English in the same step.
