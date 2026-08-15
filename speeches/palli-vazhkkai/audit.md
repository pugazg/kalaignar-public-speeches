# பள்ளி வாழ்க்கை — visual fidelity audit

**Source:** `TVA_BOK_0064116_பள்ளி_வாழ்க்கை.pdf`  
**Source SHA-256:** `e20bf80e8e5b65abbfdb5bcefbdaf85b8e5385112f6de8efcc0e733ed3aceea3`  
**Source-inspection date:** 2026-08-15  
**Main-body scope:** PDF pages 6-81 / printed pages 5-80

## Audit state

Tamil first-pass transcription (T1) is **complete: 76/76 body pages**.

The strict visual line-by-line Tamil fidelity audit (T2) is **in progress: 5/76 pages**, through PDF page 10 / printed page 9.

No page beyond PDF 10 is T2-verified yet. English remains blocked.

## T2 Batch 1 — PDF 6-10 / printed 5-9

The actual page images were compared against T1 line-by-line. Confirmed corrections are preserved in `t2-batches/batch-01-pdf-06-10.md` and are mandatory inputs to T3 canonical consolidation.

### Confirmed corrections

On PDF 7 / printed 6:

- `ஆராய்ந்து தெரிந்து` → `ஆராய்ந்து தெளிந்து`
- `கற்றோனாக` → `கற்றோனுக`
- `கல்லூரனாக` → `கல்லூரனுக`
- `கதாசிரியனாக` → `கதாசிரியனுக`
- `கட்டுரையாசிரியனாக` → `கட்டுரையாசிரியனுக`
- `உத்தமனாக` → `உத்தமனுக`

On PDF 8 / printed 7:

- `மண்ணாவது` → `மண்ணுவது`

These are source readings, not modernization choices.

### Page-boundary resolution

PDF 9 / printed 8 ends `உயி`; PDF 10 / printed 9 begins `ரினங்களைவிட`. Both page images were inspected. The consolidated one-word reading `உயிரினங்களைவிட` is therefore confirmed as a legitimate cross-page printer split under the repository guide.

### Batch result

- PDF 6 / printed 5 — audited
- PDF 7 / printed 6 — audited; 6 confirmed corrections
- PDF 8 / printed 7 — audited; 1 confirmed correction
- PDF 9 / printed 8 — audited
- PDF 10 / printed 9 — audited; split-word join confirmed

## Remaining page-boundary / lineation queue

- PDF 13→14 / printed 12→13: `இவர்` / `கட்கு`
- PDF 18→19 / printed 17→18: `கஞ்சிக்` / `காவது`
- PDF 19→20 / printed 18→19: `எட்டுச்` / `சுரையெனப்`
- PDF 23→24 / printed 22→23: `உள்ள` / `படி`
- PDF 31→32 / printed 30→31: `தமிழினத்` / `தைப்`
- PDF 32→33 / printed 31→32: `பசுமரத்` / `தாணிபோலப்`
- PDF 37→38 / printed 36→37: `வலதுகைப்` / `பெருவிரல்`
- PDF 38→39 / printed 37→38: `சாபந் தந்த` / `பிரகஸ்பதி பகவான்களும்`
- PDF 40→41 / printed 39→40: `சிற்றிடையாளைத் தேடு` / `கிறீர்`
- PDF 41→42 / printed 40→41: `சுயமரியாதை` / `பற்ற செயல்`
- PDF 42→43 / printed 41→42: `உமக்குப்` / `பெருமை தந்திடத்தான்`
- PDF 44→45 / printed 43→44: `ஊட்` / `டிடும்`
- PDF 45→46 / printed 44→45: `வருணபகவான் என்றும்` / `இடிக்குத் தலைவன் இந்திரன் என்றும்`
- PDF 50→51 / printed 49→50: `சிந்தித்` / `தான்!`
- later Batch 10-12 boundaries remain pending direct visual inspection.

## Provisional source-oddity queue

Still pending T2 confirmation where relevant: `வாழ்க்கத்தின்`, `நன்றுக`, `உயிரினங்களின் றும்`, `வாழ்க்கைச் செந்தி`, `வாசனே`, `கல்வி கற்கு மிடம்`, `திடசித்தமுடையவனுக`, `தமிழனுக`, `முன்னேற்றம் மடைகின்றன`, `தேவைத்தானு`, `அரிபந்தாமன்`, `காண்டவன்`, `மாணுக்கர்களுக்கு`, `சுயமரியாதை பற்ற செயல்`, `தினதயாளன்`, `நீலகண்டனூர்`, `மினையாளைக்`, `சிக்கச் சீழிய`, and other unusual T1 forms.

## T2 progress

| PDF pages | Printed pages | T2 state |
|---:|---:|---|
| 6-10 | 5-9 | **audited** |
| 11-81 | 10-80 | pending |

## Exact next activity

Audit **PDF pages 11-15 / printed pages 10-14** line-by-line against the scan. Resolve the queued PDF 13→14 split and visually verify the provisional forms on printed pages 11-14.

After all 76 pages pass T2, perform T3 canonical consolidation, apply every staged confirmed correction, run stale-reading/page-boundary checks, and freeze Tamil only when verified-complete.
