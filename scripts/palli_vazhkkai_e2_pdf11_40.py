from pathlib import Path
import json
import re

root = Path('speeches/palli-vazhkkai')
translation = root / 'translation-en.md'
review = root / 'translation-review.md'
metadata = root / 'metadata.json'
readme = root / 'README.md'
handover = root / 'HANDOVER.md'

# ---------- translation-en.md: confirmed E2 corrections / transparency notes ----------
text = translation.read_text(encoding='utf-8')
assert '### PDF page 11 — printed page 10' in text
assert '### PDF page 40 — printed page 39' in text

# PDF 14: preserve the scan-supported unusual form instead of silently smoothing it.
old = 'His anger is the blazing fire of their lives.'
new = "His anger is the source's `வாழ்க்கைச் செந்தி`—the blazing fire of their lives."
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 17: the comparative sense is readable, but the frozen wording itself is unusual.
needle = 'Those who overcome all the circumstances involved—the facilities for study, financial means, the condition of the family—and manage to reach this stage are very, very few compared with those at the elementary-education stage.\n'
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: the frozen Tamil in this sentence reads `ஆரம்பக் கல்வியிலிருந்து வரைவிட`, a scan-verified but syntactically unusual form. The comparative English is retained without altering the Tamil witness.]*\n", 1)

# PDF 29: E1 attached 'despise this world' to the earning of merit; restore source structure.
old = 'There are more texts filled with ideas that foster the false Vedanta that this life, this worldly life, is only an interim period, a lodging-place in which one must earn enough merit to despise this world and enjoy bliss in the next!'
new = 'There are more texts filled with ideas that foster the false Vedanta that this life, this worldly life, is merely an interim period, a lodging-place in which, despising this world, one must earn enough merit to enjoy bliss in the next!'
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 30: record unusual frozen forms that E1 rendered contextually.
needle = "The knowledge today's young children receive—the knowledge they receive today—the lights of knowledge, Tamil feeling, Tamil ethnic feeling, self-awareness, the feeling of self-respect, and the methods of training for life: these must be put in order, refined, and properly arranged, so that the future may live, Tamil may flourish, Tamil Nadu may shine as a sacred land of self-respect, and Tamils may live with fulfilment and without equal!\n"
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: PDF 30 retains the unusual frozen forms `வளர்த்தை`, `வளர்த்தைப்`, and `வகைப்படுத்தியாக`. The English renders their surrounding sense as growth, mental growth, and ordering/refining without silently changing the Tamil source.]*\n", 1)

# PDF 32: make the source-supported unusual form visible.
needle = '—protect Tamil Nadu, and live with self-respect. This rising drumbeat must sound as the song of the heart; these must be the great heart-drum of the young Tamil!\n'
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: the frozen Tamil here retains the unusual form `போற்றிவேண்டும்`; the English `honour` follows the surrounding sense without altering that source form.]*\n", 1)

# PDF 38: preserve transparency around three difficult printed forms.
needle = "Similarly, there is a story in which Tara, wife of the divine preceptor Brihaspati, bewitches Chandra, Brihaspati's disciple, and makes him her lover; this too is mixed into kavya and served up! Are such revolting, obscene Puranas necessary?\n"
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: PDF 38 retains the difficult forms `நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, and `கடிக்குலவின`. The readable English renders the surrounding sense without silently rewriting those frozen forms.]*\n", 1)

# PDF 39: direct semantic correction. The frozen Tamil says போக்கிட (remove/cause to be lost), not promote.
old = '—can hymns about them promote the welfare of the country? Are all these really necessary for students, the people of the future? No!'
new = '—can hymns about them cause the welfare of the country to be lost? Are all these really necessary for students, the people of the future? No!'
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 39: record contextual renderings of unusual source forms.
needle = 'Was it to take charge of the people of the earth and free them from famine, hunger, starvation and other sufferings? Not at all! Then why?\n'
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: PDF 39 retains the unusual printed forms `மாணுக்கர்களுக்கு`, `திடமென்று`, and `பூலோக வாசிகளேப்`. The English uses the contextual readings `students`, `suddenly`, and `people of the earth` while preserving the frozen Tamil unchanged.]*\n", 1)

# PDF 40: make the unusual wonder-form transparent.
needle = 'Seeing the wealthy devotee who loved Siva, Iyarpakai was filled with wonder, welcomed him, and asked with affection overflowing, “What do you want, devotee? I, your servant, shall not fail to give it.”\n'
assert text.count(needle) == 1
text = text.replace(needle, needle + "\n*[Translator/source note: the frozen Tamil on PDF 40 reads `இறும்பூதெய்தி`; `filled with wonder` is a contextual rendering of that source-supported unusual form.]*\n", 1)

translation.write_text(text, encoding='utf-8')

# ---------- translation-review.md ----------
r = review.read_text(encoding='utf-8')
assert '**Status:** `in-progress` — **5/76 body pages reviewed**' in r
assert '## Batch 2 — PDF 11–15 / printed 10–14' not in r
r = r.replace('**Status:** `in-progress` — **5/76 body pages reviewed**', '**Status:** `in-progress` — **35/76 body pages reviewed**', 1)
r = r.replace('| 2 | 11–15 | 10–14 | next |', '| 2 | 11–15 | 10–14 | reviewed; confirmed transparency correction consolidated |\n| 3 | 16–20 | 15–19 | reviewed; confirmed transparency note consolidated |\n| 4 | 21–25 | 20–24 | reviewed; no new correction required |\n| 5 | 26–30 | 25–29 | reviewed; two confirmed corrections/transparency notes consolidated |\n| 6 | 31–35 | 30–34 | reviewed; confirmed transparency note consolidated |\n| 7 | 36–40 | 35–39 | reviewed; semantic correction plus source-difficulty notes consolidated |\n| 8 | 41–45 | 40–44 | next |', 1)

prefix = r.split('\n## Exact next activity\n', 1)[0].rstrip()
extended = r'''

## Batch 2 — PDF 11–15 / printed 10–14

### Result

The five pages are substantially faithful. The PDF 10→11 and 13→14 continuations are intact; the long civilization-development list, the difficult PDF 12 `கேள்வி ஞானங்களைத் தூர்த்திடும் போதனைகள்`, the Kuppan family labour sequence, and the class/circumstance contrast on PDF 15 are all represented without omitted clauses or reversed argument.

### Confirmed correction

1. **PDF 14 `வாழ்க்கைச் செந்தி`.** E1 rendered this only as `the blazing fire of their lives`, hiding a scan-supported unusual frozen form. The English now keeps `வாழ்க்கைச் செந்தி` visible while retaining the contextual fire image. No Tamil change was made.

## Batch 3 — PDF 16–20 / printed 15–19

### Result

No clause omission, unsupported addition, reversal, or lost page continuation was found. The education-stage sequence (elementary → middle → high school → college → technical/professional colleges), employment-seeking argument, and PDF 19–20 discussion of education as life-guidance remain complete.

### Confirmed transparency action

1. **PDF 17 `ஆரம்பக் கல்வியிலிருந்து வரைவிட`.** The comparative E1 sense is defensible, but the frozen phrase itself is syntactically unusual. A translator/source note now records the exact form rather than leaving the contextual English unqualified.
2. PDF 19's `கல்வி கற்கு மிடம்` and `எட்டுச்சுரையெனப்` were already explicitly preserved by the E1 translator/source note; no further correction was needed.

## Batch 4 — PDF 21–25 / printed 20–24

### Result

No new correction was required. The resource-versus-poverty argument, repeated `வாழ்ந்தும் வாழாத` rhetoric, the fatalist/Vedantic quotation sequence, the PDF 23→24 continuation, and the argument for knowledge and clarity are complete. Existing E1 notes correctly preserve `நல்லதங்கள்`, `நாவினை நாட்டினரும்`, and `தவழிப் பூச்சூடி` instead of silently repairing them.

## Batch 5 — PDF 26–30 / printed 25–29

### Result

The main argument is complete, including the schoolteacher-cane continuation, the source's abrupt `வெறும் படிப்புபோதும்.`, the Tamil/self-respect programme, the technology catalogue, and the PDF 29→30 continuation. Two fidelity issues required action.

### Confirmed corrections

1. **PDF 29 `இகத்தை வெறுத்து ... புண்ணியம் சம்பாதிக்க ... பரத்தில் இன்பந் துய்க்க`.** E1 attached `despise this world` to the purpose of earning merit (`earn enough merit to despise this world and enjoy bliss`). The source structure is instead: despising this world, treat worldly life as an interim lodging in which merit is earned to enjoy bliss in the next. The English sentence was corrected accordingly.
2. **PDF 30 unusual frozen morphology.** `வளர்த்தை`, `வளர்த்தைப்`, and `வகைப்படுத்தியாக` had been rendered contextually without making the unusual witness visible. A translator/source note now records all three forms; the readable English remains otherwise unchanged.

## Batch 6 — PDF 31–35 / printed 30–34

### Result

No omission, reversal, or page-boundary loss was found. The Tamil/Tamilian/Tamil Nadu/self-respect repetitions, the atomic-bomb/Hanuman contrast, the green-wood-nail image, and the opening of the Ekalavya narrative remain structurally faithful. Existing notes preserve `அரிபந்தாமன்` and `காண்டவன்`.

### Confirmed transparency action

1. **PDF 32 `போற்றிவேண்டும்`.** Because the frozen source deliberately retains this unusual form, a translator/source note now records it while keeping the contextual English `honour`.

## Batch 7 — PDF 36–40 / printed 35–39

### Result

The Ekalavya guru-dakshina sequence, the Tara–Chandra/Brihaspati criticism, and the beginning of the Iyarpakai Nayanar narrative are complete. The PDF 40→41 sentence continuation remains intact. One direct semantic error and several source-transparency issues were confirmed.

### Confirmed corrections

1. **PDF 39 `நாட்டு நலனைப் போக்கிட முடியுமா?` — direct meaning error.** E1 read this as `can hymns about them promote the welfare of the country?`, reversing the frozen verb `போக்கிட`. It is now rendered `can hymns about them cause the welfare of the country to be lost?`. The awkwardness is source-derived and must not be silently regularized into the likely rhetorical intention.
2. **PDF 38 difficult forms.** `நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, and `கடிக்குலவின` are now explicitly recorded in a translator/source note; the surrounding readable English remains contextual rather than pretending a normalized Tamil reading exists.
3. **PDF 39 difficult forms.** `மாணுக்கர்களுக்கு`, `திடமென்று`, and `பூலோக வாசிகளேப்` are now explicitly recorded alongside the contextual English readings `students`, `suddenly`, and `people of the earth`.
4. **PDF 40 `இறும்பூதெய்தி`.** The contextual `filled with wonder` is retained, but the exact frozen form is now visible in a translator/source note.
5. PDF 40's `என்ன கொடுமதி உமக்கு` remains contextually rendered as `What a wicked mind you have!`; the review records that this is a close contextual reading of the frozen wording, not a Tamil correction.

## Cumulative E2 state

- Reviewed: **PDF 6–40 / printed 5–39 — 35/76 body pages**.
- Confirmed corrections have been consolidated as each reviewed batch completed.
- E3 remains blocked until E2 reaches 76/76 pages.
'''
next_section = r'''

## Exact next activity

Review **PDF 41–45 / printed pages 40–44** independently against the frozen Tamil. Record substantive findings here and consolidate only confirmed corrections into `translation-en.md`. Do not begin E3 until E2 has reviewed all 76 pages and every confirmed correction has been consolidated.
'''
review.write_text(prefix + extended + next_section, encoding='utf-8')

# ---------- metadata.json ----------
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation_review'] == 'in-progress'
assert wf['english_translation_review_pages_checked'] == 5
wf['english_translation_review_pages_checked'] = 35
wf['english_translation_review_through_pdf_page'] = 40
wf['english_translation_review_through_printed_page'] = 39
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------- README.md ----------
rd = readme.read_text(encoding='utf-8')
assert '| English fidelity review (E2) | **In progress — 5/76 body pages reviewed; through PDF 10 / printed 9** |' in rd
rd = rd.replace('| English fidelity review (E2) | **In progress — 5/76 body pages reviewed; through PDF 10 / printed 9** |', '| English fidelity review (E2) | **In progress — 35/76 body pages reviewed; through PDF 40 / printed 39** |', 1)
old_para = 'E2 is now **in progress**. Batch 1 reviewed **PDF 6-10 / printed 5-9 — 5/76 pages** independently against the frozen Tamil. No paragraph/clause omission, unsupported addition, reversal, or page-boundary loss was found. Three confirmed lexical/rhetorical fidelity corrections were consolidated: PDF 6 `வாழ்க்கை வசதி`, PDF 7 `காவியரசத்தில்`, and PDF 8 the distinction between `சுவையின்றி` and `சத்தற்ற வாழ்க்கை`. Full findings are recorded in `translation-review.md`.'
assert old_para in rd
new_para = old_para + '\n\nThe extended E2 activity then reviewed **PDF 11-40 / printed 10-39**, bringing the cumulative total to **35/76 pages**. Confirmed actions include preserving the unusual PDF 14 `வாழ்க்கைச் செந்தி`, documenting PDF 17 `வரைவிட`, correcting the PDF 29 attachment of `இகத்தை வெறுத்து` versus merit-for-the-next-world, making PDF 30 `வளர்த்தை` / `வளர்த்தைப்` / `வகைப்படுத்தியாக` visible, documenting PDF 32 `போற்றிவேண்டும்`, and correcting the direct PDF 39 reversal where `போக்கிட` had been translated as `promote`. Difficult PDF 38-40 forms are now explicitly documented rather than silently normalized. Full page-group findings are in `translation-review.md`.'
rd = rd.replace(old_para, new_para, 1)
rd = re.sub(r'## Exact next activity\n\nContinue \*\*E2 English fidelity review with PDF 11-15 / printed pages 10-14\*\*\.[\s\S]*?Do not begin E3 until all 76 pages have passed E2\.', '## Exact next activity\n\nContinue **E2 English fidelity review with PDF 41-45 / printed pages 40-44**. Compare each English page independently against the frozen Tamil, record substantive findings in `translation-review.md`, and consolidate only confirmed corrections into `translation-en.md`. Do not begin E3 until all 76 pages have passed E2.', rd, count=1)
readme.write_text(rd, encoding='utf-8')

# ---------- HANDOVER.md ----------
h = handover.read_text(encoding='utf-8')
old = 'Batch 1 is complete: **PDF 6-10 / printed 5-9 — 5/76 body pages reviewed**. Three confirmed lexical/rhetorical corrections were consolidated into `translation-en.md`; no omission, unsupported addition, reversal, or page-boundary loss was found in this batch.'
assert old in h
new = 'E2 is complete through **PDF 40 / printed 39 — 35/76 body pages reviewed**. Batch 1 covered PDF 6-10. The repository-owner-requested extended review covered PDF 11-40 in six five-page review groups. Confirmed corrections and transparency notes have already been consolidated into `translation-en.md`; the detailed audit is in `translation-review.md`.'
h = h.replace(old, new, 1)
insert_before = '\n## Source-fidelity safeguards carried into English\n'
assert insert_before in h
summary = r'''

## E2 extended review — PDF 11-40 / printed 10-39

Completed and consolidated.

Key review outcomes:

- PDF 11-15: no omission/reversal; `வாழ்க்கைச் செந்தி` is now visible rather than silently smoothed.
- PDF 16-20: structure and page continuations pass; a note records the scan-verified but unusual `ஆரம்பக் கல்வியிலிருந்து வரைவிட`.
- PDF 21-25: no new correction required; existing notes for `நல்லதங்கள்`, `நாவினை நாட்டினரும்`, and `தவழிப் பூச்சூடி` were confirmed adequate.
- PDF 26-30: corrected the PDF 29 semantic attachment around `இகத்தை வெறுத்து` / merit / other-world bliss; PDF 30 now records `வளர்த்தை`, `வளர்த்தைப்`, and `வகைப்படுத்தியாக`.
- PDF 31-35: no omission/reversal; PDF 32 `போற்றிவேண்டும்` is now documented; existing `அரிபந்தாமன்` and `காண்டவன்` notes remain.
- PDF 36-40: corrected the direct PDF 39 reversal `போக்கிட` ≠ `promote`; documented difficult PDF 38 forms `நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, `கடிக்குலவின`; PDF 39 `மாணுக்கர்களுக்கு`, `திடமென்று`, `பூலோக வாசிகளேப்`; and PDF 40 `இறும்பூதெய்தி`.
- PDF 40→41 continuation remains intact; page 41 itself is not yet counted as reviewed.
'''
h = h.replace(insert_before, summary + insert_before, 1)
h = re.sub(r'## Exact next activity\n\nContinue \*\*E2 English fidelity review with PDF pages 11-15 / printed pages 10-14\*\*\.[\s\S]*?keep E3 blocked until E2 reaches 76/76 pages and all corrections are consolidated\.', '## Exact next activity\n\nContinue **E2 English fidelity review with PDF pages 41-45 / printed pages 40-44**. Compare each page independently against frozen `transcription-ta.md`, record findings in `translation-review.md`, consolidate only confirmed corrections, update the cumulative E2 count, and keep E3 blocked until E2 reaches 76/76 pages and all corrections are consolidated.', h, count=1)
handover.write_text(h, encoding='utf-8')

# ---------- validation ----------
final_translation = translation.read_text(encoding='utf-8')
for s in [
    "source's `வாழ்க்கைச் செந்தி`",
    '`ஆரம்பக் கல்வியிலிருந்து வரைவிட`',
    'despising this world, one must earn enough merit to enjoy bliss in the next',
    '`வளர்த்தை`, `வளர்த்தைப்`, and `வகைப்படுத்தியாக`',
    '`போற்றிவேண்டும்`',
    '`நாயகனுக்கிக்கொண்ட`, `சந்திரனச் சல்லாபத்திற்`, and `கடிக்குலவின`',
    'cause the welfare of the country to be lost?',
    '`மாணுக்கர்களுக்கு`, `திடமென்று`, and `பூலோக வாசிகளேப்`',
    '`இறும்பூதெய்தி`'
]:
    assert s in final_translation, s
assert 'promote the welfare of the country?' not in final_translation
assert '**Status:** `in-progress` — **35/76 body pages reviewed**' in review.read_text(encoding='utf-8')
assert data['workflow']['english_translation_review_pages_checked'] == 35
print('E2 PDF 11-40 review consolidation validated')
