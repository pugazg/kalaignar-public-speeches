from pathlib import Path
import json
import re

root = Path('speeches/palli-vazhkkai')
translation = root / 'translation-en.md'
review = root / 'translation-review.md'
metadata = root / 'metadata.json'
readme = root / 'README.md'
handover = root / 'HANDOVER.md'

# --- translation-en.md confirmed E2 corrections ---
t = translation.read_text(encoding='utf-8')
replacements = [
    (
        'only a very few have the means, the opportunity, the standard of living, and the circumstances that make such a life possible.',
        'only a very few have the means, the opportunity, the standard of living, and the comforts and facilities of life that make it possible.'
    ),
    (
        'plunge into the sea of poetry and the realm of epics,',
        'plunge into the sea of poetry and the flavour of epic literature,'
    ),
    (
        'most of the people of this country lead an insipid existence with the weariness of merely saying, “Somehow, we are living.”',
        'most of the people of this country lead a life without substance, with the weariness of merely saying, “Somehow, we are living.”'
    ),
]
for old, new in replacements:
    assert t.count(old) == 1, (old, t.count(old))
    t = t.replace(old, new, 1)
translation.write_text(t, encoding='utf-8')

# --- translation-review.md ---
review_text = '''# Palli Vazhkkai — English Translation Fidelity Review

> **Review basis:** frozen `transcription-ta.md` compared directly with `translation-en.md`  
> **Scope:** semantic fidelity, rhetoric/repetition, source-supported oddities, names/terms, omissions/additions, and unintended normalization  
> **Tamil source layer:** `verified-complete` / frozen; this review does not alter `transcription-ta.md`

## Review status

**Status:** `in-progress` — **5/76 body pages reviewed**

| Review batch | PDF pages | Printed pages | Status |
|---|---:|---:|---|
| 1 | 6–10 | 5–9 | reviewed; confirmed corrections consolidated |
| 2 | 11–15 | 10–14 | next |

E1 is complete for all 76 body pages. E2 is now active. E3 remains blocked until all 76 pages have been independently reviewed and all confirmed E2 corrections have been consolidated.

## Batch 1 — PDF 6–10 / printed 5–9

### Result

The first-pass English is substantially aligned with the frozen Tamil across these five pages. No whole paragraph or clause is omitted, no unsupported historical fact is added, no meaning is reversed, and the PDF 9→10 sentence continuation is preserved.

Three lexical/rhetorical fidelity issues were confirmed and corrected in `translation-en.md`:

1. **PDF 6 / printed 5 — `வாழ்க்கை வசதி`.** The first pass ended the list with `circumstances`, which was broader than the source's repeated `வசதி` language. It is now rendered as `the comforts and facilities of life`, preserving the distinction among `வசதி`, `வாய்ப்பு`, `வாழ்க்கைத்தரம்`, and `வாழ்க்கை வசதி`.
2. **PDF 7 / printed 6 — `கவிதைக் கடலில், காவியரசத்தில்`.** The first pass used `the sea of poetry and the realm of epics`. `காவியரசத்தில்` here carries the `ரசம்` / flavour image rather than a `realm` image. The English now reads `the sea of poetry and the flavour of epic literature`.
3. **PDF 8 / printed 7 — `சுவையின்றி ... சத்தற்ற வாழ்க்கை`.** The first pass used `Without flavour ... an insipid existence`, effectively collapsing the source's two distinct images. The second phrase is now `a life without substance`, preserving the rhetorical distinction between `சுவை` and `சத்து`.

### Reviewed and retained without correction

- PDF 6 preserves the repeated `பேறு, பாக்கியம்` emphasis and the source's argument that school access is available only to very few.
- PDF 7 preserves the repeated questions, the Saraswati/Kamban references, `கல்விப் பஞ்சம்`, and the source-supported `கல்லூரனாக` as the conservative `a college man`.
- PDF 8 preserves the source's class/circumstance argument, the `நடைப் பிணங்களாக` image as `walking corpses`, and the quoted fatalist wording without adding explanation.
- PDF 9 retains the full catalogue of birds, animals, aquatic creatures, and amphibious/land-and-water creatures; `கெளதாரி` remains cautiously transliterated as `kauthari` rather than being assigned an unsupported species identification.
- PDF 9→10 preserves the unfinished `மனிதன் மற்ற உயிரினங்களைவிட` / `உயர்வு...` continuation.
- PDF 10 retains the complete rational-discernment argument, including good/evil, needed/unneeded, wanted/unwanted, danger/happiness, surroundings, climate, and the closing continuation into PDF 11. No omission or reversal was found.

## Exact next activity

Review **PDF 11–15 / printed pages 10–14** independently against the frozen Tamil. Record substantive findings here and consolidate only confirmed corrections into `translation-en.md`. Do not begin E3 until E2 has reviewed all 76 pages.
'''
review.write_text(review_text, encoding='utf-8')

# --- metadata.json ---
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation'] == 'first-pass-complete'
assert wf['english_translation_pages_completed'] == 76
assert wf['english_translation_review'] == 'not-started'
assert wf['english_translation_review_pages_checked'] == 0
wf['english_translation_review'] = 'in-progress'
wf['english_translation_review_pages_checked'] = 5
wf['english_translation_review_through_pdf_page'] = 10
wf['english_translation_review_through_printed_page'] = 9
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# --- README.md ---
r = readme.read_text(encoding='utf-8')
assert '| English fidelity review (E2) | **Not started** |' in r
r = r.replace('| English fidelity review (E2) | **Not started** |', '| English fidelity review (E2) | **In progress — 5/76 body pages reviewed; through PDF 10 / printed 9** |', 1)
old = '''E2 has **not** begun. Per repository workflow, the next gate is a separate page-by-page Tamil→English fidelity review against the frozen `transcription-ta.md`.

## Exact next activity

Begin **E2 English fidelity review with PDF 6-10 / printed pages 5-9**. Compare each English page independently against the frozen Tamil, looking specifically for omitted clauses, additions, reversals, softened or strengthened rhetoric, pronoun/subject errors, historical-name errors, removed repetition, page-boundary omissions, and silent normalization of difficult Tamil. Record findings in `translation-review.md` and consolidate only confirmed corrections into `translation-en.md`.
'''
new = '''E2 is now **in progress**. Batch 1 reviewed **PDF 6-10 / printed 5-9 — 5/76 pages** independently against the frozen Tamil. No paragraph/clause omission, unsupported addition, reversal, or page-boundary loss was found. Three confirmed lexical/rhetorical fidelity corrections were consolidated: PDF 6 `வாழ்க்கை வசதி`, PDF 7 `காவியரசத்தில்`, and PDF 8 the distinction between `சுவையின்றி` and `சத்தற்ற வாழ்க்கை`. Full findings are recorded in `translation-review.md`.

## Exact next activity

Continue **E2 English fidelity review with PDF 11-15 / printed pages 10-14**. Compare each English page independently against the frozen Tamil, record substantive findings in `translation-review.md`, and consolidate only confirmed corrections into `translation-en.md`. Do not begin E3 until all 76 pages have passed E2.
'''
assert old in r
r = r.replace(old, new, 1)
readme.write_text(r, encoding='utf-8')

# --- HANDOVER.md ---
h = handover.read_text(encoding='utf-8')
h = h.replace('# பள்ளி வாழ்க்கை — English E1 handover', '# பள்ளி வாழ்க்கை — English E2 handover', 1)
h = h.replace('### E2 / E3 — NOT STARTED\n\nIndependent English fidelity review and final end-to-end Tamil→English verification have not begun. Do **not** begin E2 until the full E1 body translation is complete.',
'''### E2 — IN PROGRESS\n\nBatch 1 is complete: **PDF 6-10 / printed 5-9 — 5/76 body pages reviewed**. Three confirmed lexical/rhetorical corrections were consolidated into `translation-en.md`; no omission, unsupported addition, reversal, or page-boundary loss was found in this batch.\n\n### E3 — NOT STARTED\n\nFinal end-to-end Tamil→English verification remains blocked until E2 has reviewed all 76 pages and all confirmed corrections are consolidated.''', 1)
insert = '''\n## E2 Batch 1 — PDF 6-10 / printed 5-9\n\nCompleted and consolidated.\n\nConfirmed corrections:\n\n- PDF 6 `வாழ்க்கை வசதி`: replaced overly broad `circumstances` with `the comforts and facilities of life`.\n- PDF 7 `காவியரசத்தில்`: replaced `the realm of epics` with `the flavour of epic literature`, preserving the source's `ரசம்` image.\n- PDF 8 `சுவையின்றி ... சத்தற்ற வாழ்க்கை`: retained `without flavour` for the first image and changed the second from `insipid existence` to `a life without substance`, preserving the two-image distinction.\n\nNo whole paragraph/clause omission, unsupported addition, reversal, or page-boundary loss was found. PDF 9→10 continuity and the complete PDF 10 rational-discernment argument were checked and retained.\n\n'''
marker = '\n## Source-fidelity safeguards carried into English\n'
assert marker in h
h = h.replace(marker, '\n' + insert + '## Source-fidelity safeguards carried into English\n', 1)
h = re.sub(r'## Exact next activity\n\n.*?(?=\n## Safeguards)',
'''## Exact next activity\n\nContinue **E2 English fidelity review with PDF pages 11-15 / printed pages 10-14**.\n\nFor that review batch:\n\n1. compare each English page independently against the frozen `transcription-ta.md`;\n2. check omissions, additions, reversals, altered rhetoric/repetition, subjects/pronouns, names/titles, silent normalization and page-boundary loss;\n3. record substantive findings in `translation-review.md`;\n4. consolidate only confirmed corrections into `translation-en.md`;\n5. update metadata/README/HANDOVER with the cumulative E2 page count;\n6. keep E3 blocked until E2 reaches 76/76 pages and all corrections are consolidated.\n''',
           h, flags=re.S)
handover.write_text(h, encoding='utf-8')

# Sanity checks
assert 'the flavour of epic literature' in translation.read_text(encoding='utf-8')
assert 'a life without substance' in translation.read_text(encoding='utf-8')
assert '5/76 body pages reviewed' in review.read_text(encoding='utf-8')
print('Prepared Palli Vazhkkai E2 Batch 1: PDF 6-10 / printed 5-9')
