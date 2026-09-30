# “கைத்தறி வாங்கலையோ” — Tamil source-fidelity audit

**Source:** `TVA_BOK_0064364_ முல்லைக்_கொல்லை.pdf`  
**Source SHA-256:** `1e14d215de1b109292ba2b2ba03f73cf844978d2d6b1bb4f912c3ca64733a15f`  
**Constituent:** 4 / 5  
**Scope:** PDF57–62 / printed pp.57–62 / 6 pages  
**Current gate:** Tamil T1 **IN PROGRESS — Batch 1 COMPLETE — PDF57–61 / 5/6 pages**; Tamil T2 **NOT STARTED**; English blocked pending Tamil freeze.

## T1 method

- transcribe directly from rendered source pixels;
- preserve physical PDF/printed-page provenance;
- preserve source wording, punctuation, spacing, names, repetitions and unusual grammar;
- do not infer a speech date, venue or event;
- apply the historical-Tamil glyph guide page by page;
- encode proven historical glyph identity in modern Unicode without modernizing source wording;
- do not use global replacement;
- record genuine source damage/obscurity rather than guessing;
- inspect adjoining pages only as needed to establish page-boundary continuity.

## T1 Batch 1 — PDF57–61 / printed pp.57–61

**Status: COMPLETE — 5/5 batch pages drafted.**

- PDF57 — heading + body first-pass complete
- PDF58 — first-pass complete
- PDF59 — first-pass complete
- PDF60 — first-pass complete
- PDF61 — first-pass complete
- cumulative T1 — **5/6**
- explicit source-obscured readings — **0**
- contextual reconstruction guesses inserted — **0**

### Page-boundary controls

- **PDF57→58** — physical split `வேண்டு / மென்றும்` → assembled reading `வேண்டுமென்றும்` — **PASS**
- **PDF58→59** — physical split `வீட் / டுக்குச்` → assembled reading `வீட்டுக்குச்` — **PASS**
- **PDF59→60** — PDF59 ends `செய்ய வேண்டிய வேலை.`; PDF60 begins `போராட்டத்திலே ஈடுபட வேண்டும்.` — **PASS / no split word**
- **PDF60→61** — PDF60 ends `அந்த வழி காணத் தவற மாட்டோம்.`; PDF61 begins `இந்த உறுதியுடனே தான்—...` — **PASS / no split word**
- **PDF61→62** — physical split `அறி / வுரையை,` → assembled reading `அறிவுரையை,` — **PASS**; PDF62 inspected only as boundary context

### Historical-glyph first-pass

PDF57–61 were inspected at enlarged/native resolution under `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, including the known reform-sensitive families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Representative source-sensitive checks include:

- PDF57 — `அண்ணா`, `கைத்தறியாளரின்`, `சரசமானது`
- PDF58 — `நாலணா`, `காலணா`, `கைக்குட்டை`
- PDF59 — `மணவாளன்`, `நெசவாளி`, `கைத்தறி`
- PDF60 — `கைத்தறியாளர்`, `வடநாட்டுப்`, `சதிராடக்கூடிய`
- PDF61 — `கைத்தறியாளர்`, `லக்ஷாதிபதிகளாகும்`, `நரம்பின்றிப்`

Character identity was decoded before transcription. No global replacement or lexical modernization was used.

### Source-sensitive T1 forms for later T2 recheck

The following are retained exactly as read from the source at T1 and are **not silently normalized**:

- PDF57 — `சரசமானது`
- PDF60 — `கழுக்கான`
- PDF61 — `மாற்றுணிடம்`
- PDF61 — `லக்ஷாதிபதிகளாகும்`
- PDF61 — `சவடாக்கள்`
- PDF61 — `ஸ்டண்டுகள்`

These are source-sensitive review controls, not unresolved source damage.

## T1 state after Batch 1

- drafted — **PDF57–61 / 5/6**
- explicit source-limit markers — **0**
- historical-glyph first-pass — **through PDF61**
- actionable unresolved — **0 at T1 Batch 1**
- Tamil T1 — **IN PROGRESS**
- Tamil T2 — **NOT STARTED**
- Tamil — **not verified / not frozen**
- English — **blocked**

## Next gate

Proceed to **Tamil T1 Batch 2 FINAL — PDF62 / printed p.62 / 1 page**. Complete the cross-page `அறி / வுரையை` continuation, inspect PDF63 for the outgoing constituent boundary to **இலட்சிய இதழ்கள்**, then synchronize controls. Do not begin T2 or English.
