# NEXT CHAT PROMPT — வரலாற்றுச் சுவடு / T3 Tamil consolidation and freeze

Continue directly in `pugazg/kalaignar-public-speeches`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Active speech

`speeches/varalattru-suvadu/`

Controlling source: `TVA_BOK_0065598_வரலாற்றுச்_சுவடு.pdf`

Read first:

1. `SPEECH_PROCESSING_GUIDE.md`
2. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. `speeches/varalattru-suvadu/HANDOVER.md`
4. `speeches/varalattru-suvadu/README.md`
5. `speeches/varalattru-suvadu/metadata.json`
6. `speeches/varalattru-suvadu/transcription-ta.md`
7. `speeches/varalattru-suvadu/audit.md`

## Durable state

- canonical speech body — PDF **4–25**, **22 speech pages**
- Tamil T1 — **COMPLETE — 22/22**
- T2 strict visual audit — **COMPLETE / PASS — 22/22**
- T2 batches — **5/5 PASS**
- cumulative T2 corrections — **58**
- T2 unresolved — **0**
- T3 consolidation/freeze — **PENDING**
- English — **BLOCKED**

Final T2 corrections include:

- PDF 24 — **`என்பதேகூட எனக்குக்`**
- PDF 24 — **`அல்ல;`**
- PDF 24 — **`தாழ்த்தப்பட்ட மக்களுக்கும் தாக்காது`**
- PDF 25 — **`எவனுவது கால் வைத்தால்`**
- PDF 24→25 — **`முகமதலி / அவர்களுக்கும்...`** PASS
- terminal — **`சிந்திப்பது உங்கள் கடன்!`** + printed star PASS

Durable historical reading:

- PDF 5 — **`வினாக் குறிக்கு`**; reject `வினக்` / `வினைக்`

## Exact next activity — T3

Perform Tamil consolidation / freeze:

1. verify all 58 T2 corrections are present in `transcription-ta.md`;
2. recheck all recorded page-boundary joins;
3. search for stale/superseded readings and rejected historical-glyph guesses;
4. confirm PDF 4–25 all occur exactly once, in order, with no missing/duplicate speech page;
5. reconcile `metadata.json`, `audit.md`, `README.md`, `HANDOVER.md`, root `README.md` and this prompt;
6. if and only if all checks pass, mark Tamil **`verified-complete` / FROZEN**.

Do not begin English in the same activity unless T3 has first been committed closed.

The Audio 06 archive remains pending separately at its previous T2 checkpoint.
