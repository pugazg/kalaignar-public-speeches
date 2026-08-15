# பள்ளி வாழ்க்கை — visual fidelity audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Source-inspection date:** 2026-08-15  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

Tamil first-pass transcription (T1) is **in progress: 30/76 body pages**, through PDF page 35 / printed page 34.

The strict visual line-by-line Tamil fidelity audit (T2) is **not started** and must not begin until the complete 76-page body has first been transcribed in T1. All readings below remain provisional T1 carry-forward items.

## T1 progress context

| Batch | PDF pages | Printed pages | T1 state | T2 state |
|---|---:|---:|---|---|
| 1 | 6-10 | 5-9 | first-pass transcribed | not audited |
| 2 | 11-15 | 10-14 | first-pass transcribed | not audited |
| 3 | 16-20 | 15-19 | first-pass transcribed | not audited |
| 4 | 21-25 | 20-24 | first-pass transcribed | not audited |
| 5 | 26-30 | 25-29 | first-pass transcribed | not audited |
| 6 | 31-35 | 30-34 | first-pass transcribed | not audited |

### Page-boundary / lineation items to recheck during T2

- PDF 9→10 / printed 8→9: `உயி` / `ரினங்களைவிட` was joined as `உயிரினங்களைவிட`.
- PDF 13→14 / printed 12→13: `இவர்` / `கட்கு` was joined as `இவர்கட்கு`.
- PDF 18→19 / printed 17→18: `கஞ்சிக்` / `காவது` was joined as `கஞ்சிக்காவது`.
- PDF 19→20 / printed 18→19: `எட்டுச்` / `சுரையெனப்` was joined as `எட்டுச்சுரையெனப்`.
- PDF 23→24 / printed 22→23: `உள்ள` / `படி` was treated as `உள்ளபடி`.
- PDF 31→32 / printed 30→31: source wraps `தமிழினத்` / `தைப்`; T1 currently preserves the page split and T2 must decide consolidated lineation (`தமிழினத்தைப்`).
- PDF 32→33 / printed 31→32: source wraps `பசுமரத்` / `தாணிபோலப்`; T1 currently preserves the page split and T2 must decide consolidated lineation (`பசுமரத்தாணிபோலப்`).

### Provisional source-oddity readings from T1

Do not normalize these before T2 visual recheck:

- printed p.11: `வாழ்க்கத்தின்`, `நன்றுக`
- printed p.12: `உயிரினங்களின் றும்`
- printed p.13: `வாழ்க்கைச் செந்தி`
- printed p.14: `வாசனே`
- printed p.18: `கல்வி கற்கு மிடம்`
- printed pp.20-24: `திடசித்தமுடையவனுக`, `பலமுறைகள்`, `மனிதனுக`, `நல்லதங்கள்`, `நாவினை நாட்டினரும்`
- printed pp.25-29: `தமிழனுக`, `முன்னேற்றம் மடைகின்றன`, `இளையான் குடிமாறனார்`, `இத்தை வெறுத்து`, `தன்னேப்பற்றிக் கவலிப்பட`, `வளர்த்தை`, `வகைப்படுத்தியாக`
- printed pp.30-34: `தேவையற்ற கருத்துக்களே`, `போற்றிவேண்டும்`, `புதியக் மறுமலர்ச்சிக்கு`, `தேவைத்தானு`, `எவை யெவை`, `அரிபந்தாமன்`, `காண்டவன்`, and other visibly unusual forms in the Ekalavya passage.

### Structural correction during T1

After Batch 5, `transcription-ta.md` had accidentally been replaced with a shortened file containing a placeholder for the already completed PDF 6-25 text. Before adding Batch 6, the continuous PDF 6-25 transcription was restored from the repository's prior verified T1 state and Batches 5-6 were appended. This is a repository-structure repair, **not** a T2 textual verification claim.

## Pending workflow

1. Continue T1 first-pass Tamil transcription from PDF page **36 / printed page 35** through PDF page 81 / printed page 80.
2. Only after T1 is complete, perform T2 strict visual line-by-line comparison of every body page against the scan.
3. Then perform T3 consolidation, stale-reading/page-boundary checks, and freeze the verified Tamil layer.
4. English work remains blocked until T3 passes.
