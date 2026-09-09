# தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா — source-fidelity audit

**Controlling source:** `TVA_BOK_0065802_முத்துக்குளியல்_பாகம்_2.pdf`  
**Parent collection:** `collections/muthukkuliyal-part-2/`  
**Source SHA-256:** `48631b4fc5258df33213dbb742aec70ff6aace4fcd294f377e5750b406f5d9b2`  
**Scope:** PDF 12–18 / printed pp. 11–17

## Source intake

- Repository duplicate search for the exact title returned no existing speech tree.
- Constituent number: **1 / 36**.
- Opening: PDF 12 / printed p.11.
- Ending: PDF 18 / printed p.17.
- The printed closing note on PDF 18 establishes date **12-1-98**, venue **சென்னை ஜவகர்லால் நேரு விளையாட்டரங்கம்**, event wording **தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா**, and role **தலைமை உரை**.
- The closing note is source metadata, not part of the speech body.

## T1 first pass

Tamil T1: **COMPLETE — 7 / 7 mapped pages**.

T1 was made directly from rendered scans but was not itself a verification claim. Several uncertain first-pass readings were deliberately left for T2 rather than normalized.

## T2 strict visual fidelity audit

Every mapped page was re-read line by line against the controlling scan.

| PDF | Printed | T2 state | Substantive result |
|---:|---:|---|---|
| 12 | 11 | **PASS** | no wording correction; title and திருவள்ளுவர் quotation checked |
| 13 | 12 | **PASS** | 3 corrections |
| 14 | 13 | **PASS** | no correction; unusual `ஐக்கிய இந்தியர் மீது` confirmed as printed |
| 15 | 14 | **PASS** | no correction; பாரதி quotation and surrounding wording checked |
| 16 | 15 | **PASS** | 1 correction; source repetition confirmed |
| 17 | 16 | **PASS** | 1 correction; line-wrap join and all employment figures checked |
| 18 | 17 | **PASS** | no correction; final speech words, விவேகானந்தர் quotation and closing note checked |

Strictly audited pages: **7 / 7**.  
T2 substantive corrections: **5**.  
Unresolved source readings: **0**.

### T2 corrections

1. **PDF 13 / printed p.12**  
   T1: `தங்கள் சொந்த நாடாகக் கொள்வர்`  
   Source: `தங்கள் சொந்த நாடாக்கிக் கொள்வர்`  
   Action: corrected.

2. **PDF 13 / printed p.12**  
   T1: `அபிமன்யு அர்ஜுனனை விட`  
   Source: `அபிமன்யு அர்ஜூனனை விட`  
   Action: corrected; the long `ூ` is visible in the scan.

3. **PDF 13 / printed p.12**  
   T1: `அர்ஜுனன் புகழ்பெற்ற போர் வீரனாக`  
   Source: `அர்ஜூனன் புகழ்பெற்ற போர் வீரனாக`  
   Action: corrected.

4. **PDF 16 / printed p.15**  
   T1: `இந்தியர் கனிவை ஒன்றுபட்ட மனப்பான்மையை உருவாக்க வேண்டும்`  
   Source line-wrap: `இந்தியர்` / `களிடையே ஒன்றுபட்ட மனப்பான்மையை உருவாக்க வேண்டும்`  
   Action: joined the split word and corrected to `இந்தியர்களிடையே ஒன்றுபட்ட மனப்பான்மையை உருவாக்க வேண்டும்`.

5. **PDF 17 / printed p.16**  
   T1: `சமாதானத் திறக்கும் வளர்ச்சிக்கும்`  
   Source line-wrap: `சமாதானத்` / `திற்கும் வளர்ச்சிக்கும்`  
   Action: joined the split word and corrected to `சமாதானத்திற்கும் வளர்ச்சிக்கும்`.

### T2 confirmed unusual/source-sensitive readings

- **PDF 14 / printed p.13:** `ஐக்கிய இந்தியர் மீது` is visibly printed and is retained without modernization or contextual repair.
- **PDF 16 / printed p.15:** `அளிக்கப்படாவிட்டாலும் நீடித்த நட்புறவைச் சாதிக்க முடியாது` is retained as printed.
- **PDF 16 / printed p.15:** the apparently repetitive sequence beginning `சக்தியும் முயற்சிகளும் ஆக்கபூர்வ நடவடிக்கைகளில்...` and repeating `ஏழைகளின் நலனை மேம்படுத்த அரசாங்கங்கள் மேற்கொள்ளும் முயற்சிகளுக்கு...` is present in the source and is intentionally retained; it is not a transcription duplication.
- **PDF 17 / printed p.16:** printer line-wrap `இருபத்தையாயிரத்` / `துக்கு` is one word and is correctly joined as `இருபத்தையாயிரத்துக்கு`.
- Numerals and amounts checked directly: `78.4`, `10 ஆயிரம்`, `பதிமூன்றாயிரம்`, `அறுநூறு`, `சுமார் ஆயிரம்`, `பத்தாயிரத்துக்கு மேற்பட்ட`, `மேலும் பத்தாயிரம்`, and `15 சதவிகித`.
- Quotation wording and punctuation/spacing for திருவள்ளுவர், பாரதி and விவேகானந்தர் were checked against the scans and retained.

## Opening / ending verification

- First speech heading: `தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா` — **verified**.
- First body words: `முதலில் இந்த விழாவை...` — **verified**.
- Final body sentence ends: `என்ற சொற்களைக் கூறி என் உரையை நிறைவு செய்ய விரும்புகிறேன்.` — **verified**.
- The source closing note begins only after the speech body and remains metadata, not speech text — **verified**.

## T3 consolidation and freeze

T3: **PASS / COMPLETE**.

The five T2 corrections are consolidated into `transcription-ta.md`. A final consistency sweep confirmed:

- PDF 12–18 / printed 11–17 is represented once, contiguously, with no missing or duplicated page interval;
- the stale T1 readings `நாடாகக் கொள்வர்`, `அர்ஜுனனை`, `அர்ஜுனன்`, `இந்தியர் கனிவை`, and `சமாதானத் திறக்கும்` are absent from the canonical transcript;
- the page title `தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா` remains distinct from the contents-table spelling `தேசிய இளைஞர் கொண்டாட்டத் தொடக்கவிழா`;
- event/date/venue facts remain sourced only from the constituent closing note and are not inferred from the June 2000 parent publication;
- no uncertainty marker remains.

Tamil status is **`verified-complete`** and frozen. Any later source-supported Tamil correction must reopen dependent English work.

## English workflow checkpoint

English E1 is now **COMPLETE — 7 / 7 pages** in `translation-en.md`, produced only from the frozen `transcription-ta.md`.

This audit does not treat E1 completion as English verification. The independent review record is `translation-review.md`.

One translation-sensitive Tamil source form remains explicitly surfaced for review rather than silently normalized: printed p.13 `ஐக்கிய இந்தியர் மீது`. E1 records the exact Tamil in a source note alongside its cautious English rendering.

## Exact next gate

Perform **E2 independent Tamil→English fidelity review for all seven pages**, comparing `translation-en.md` directly against frozen `transcription-ta.md`. Record all English findings in `translation-review.md`, consolidate confirmed corrections, and keep E3 blocked until E2 is fully resolved.
