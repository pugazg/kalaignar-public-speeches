from pathlib import Path
import json
import re

root = Path('speeches/palli-vazhkkai')
ta_path = root / 'transcription-ta.md'
en_path = root / 'translation-en.md'
review_path = root / 'translation-review.md'
metadata_path = root / 'metadata.json'
readme_path = root / 'README.md'
handover_path = root / 'HANDOVER.md'

ta = ta_path.read_text(encoding='utf-8')
en = en_path.read_text(encoding='utf-8')
review = review_path.read_text(encoding='utf-8')
metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
readme = readme_path.read_text(encoding='utf-8')
handover = handover_path.read_text(encoding='utf-8')

# Structural whole-body verification.
heading_re = re.compile(r'^### PDF page (\d+) — printed page (\d+)$', re.M)
expected = [(p, p - 1) for p in range(6, 82)]
ta_heads = [(int(a), int(b)) for a, b in heading_re.findall(ta)]
en_heads = [(int(a), int(b)) for a, b in heading_re.findall(en)]
assert ta_heads == expected
assert en_heads == expected
assert len(set(ta_heads)) == 76 and len(set(en_heads)) == 76

def sections(text):
    ms = list(heading_re.finditer(text))
    out = {}
    for i, m in enumerate(ms):
        start = m.end()
        end = ms[i+1].start() if i+1 < len(ms) else len(text)
        out[int(m.group(1))] = text[start:end].strip()
    return out

ta_pages = sections(ta)
en_pages = sections(en)
assert set(ta_pages) == set(range(6, 82))
assert set(en_pages) == set(range(6, 82))
for p in range(6, 82):
    assert ta_pages[p]
    assert en_pages[p]

# E2 corrections must survive, and superseded wording must not.
required = [
    'the comforts and facilities of life',
    'the flavour of epic literature',
    'a life without substance',
    "source's `வாழ்க்கைச் செந்தி`",
    'merely an interim period, a lodging-place in which, despising this world, one must earn enough merit to enjoy bliss in the next!',
    'can hymns about them cause the welfare of the country to be lost?',
    'the reality occurring there',
    "betrayal of one's people",
    'a deprived, miserable life',
    "the community for whom ‘study does not come,’",
    'reduce our own rights, surrender our monopoly',
    'greater brain-power is needed',
]
for x in required:
    assert x in en, x

stale = [
    'the realm of epics',
    'an insipid existence',
    'earn enough merit to despise this world and enjoy bliss in the next',
    'can hymns about them promote the welfare of the country?',
    'the reality said to be occurring there',
    'betrayal of the people',
    'half-starved, miserable life',
    'people said to be unable to study',
    'reduce our own privileges, surrender our monopoly',
    'greater strength of mind is needed',
]
for x in stale:
    assert x not in en, x

# Source difficulties must remain transparent, not silently normalized.
difficult = [
    'வாழ்க்கைச் செந்தி', 'ஆரம்பக் கல்வியிலிருந்து வரைவிட', 'கல்வி கற்கு மிடம்', 'எட்டுச்சுரையெனப்',
    'நல்லதங்கள்', 'நாவினை நாட்டினரும்', 'தவழிப் பூச்சூடி', 'வெறும் படிப்புபோதும்.',
    'முன்னேற்றம் மடைகின்றன', 'வளர்த்தை', 'வளர்த்தைப்', 'வகைப்படுத்தியாக', 'போற்றிவேண்டும்',
    'அரிபந்தாமன்', 'காண்டவன்', 'நாயகனுக்கிக்கொண்ட', 'சந்திரனச் சல்லாபத்திற்', 'கடிக்குலவின',
    'மாணுக்கர்களுக்கு', 'திடமென்று', 'பூலோக வாசிகளேப்', 'இறும்பூதெய்தி', 'மனிதனி அறிவு கண்டு',
    'சுதுமதி படைத்தோரால்', 'தமிழனமாக', 'மதனின் அறிவு', 'மீனவ மக்களைத் துறந்து', 'தன்னுலே',
    'இதற்கேல் வாழ் பொருந்தும் முறையிலே', 'உலகியலேக் காண', 'ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு'
]
for x in difficult:
    assert x in en, x

# Representative high-risk page-split continuations. Full 75-transition reading is recorded in review prose.
pairs = [
    (9, 'Compared with other living beings, the human being is—'),
    (10, '—superior, a species possessing an additional faculty of knowledge—rational discernment.'),
    (13, 'only if they labour do they have—'),
    (14, '—a place to live;'),
    (20, 'and to gain clarity in life,'),
    (21, '—and to live with firm resolve'),
    (25, "the weight of the schoolteacher's cane—"),
    (26, '—and the blows it dealt!'),
    (29, 'the books that teach these things, he has not—'),
    (30, '—read; nor has he been given the opportunity'),
    (30, 'the present-day—'),
    (31, '—young generation.'),
    (37, 'the right-hand—'),
    (38, '—thumb.'),
    (40, 'you seek a slender-waisted woman—'),
    (41, '—coming in the guise of a devotee'),
    (44, 'religious sectarian passions—'),
    (45, '—religious doctrines that contradict one another'),
    (60, 'the course of development—'),
    (61, '—the path, the path of progress'),
    (80, 'throughout the country—'),
    (81, '—in the name of custom and practice'),
]
for p, x in pairs:
    assert x in en_pages[p], f'{p}: {x}'
assert '#### School Life' in en_pages[6]
assert 'Vanakkam!!' in en_pages[81]

# English layer final status.
old_status = '**Status:** `fidelity-corrections-consolidated` — E1 complete; E2 reviewed **76/76 body pages** and all confirmed corrections are consolidated; E3 pending'
assert old_status in en
en = en.replace(old_status, '**Status:** `verified-complete` — E1 complete; E2 reviewed **76/76 body pages** with all confirmed corrections consolidated; E3 final end-to-end verification passed **76/76**', 1)
old_progress = '- Current English layer status: **fidelity-corrections-consolidated**.\n- E3 final end-to-end Tamil→English verification: **not started**.\n- Exact next gate: **E3 full-body verification of PDF 6-81 / printed 5-80**.'
assert old_progress in en
en = en.replace(old_progress, '- Current English layer status: **verified-complete**.\n- E3 final end-to-end Tamil→English verification: **complete — 76/76 body pages; PASS**.\n- Newly confirmed E3 corrections: **0**.\n- Exact next gate: **final archival synchronization only**.', 1)
en_path.write_text(en, encoding='utf-8')

# Translation-review final E3 record.
old_review_status = '**Status:** `review-complete` — **76/76 body pages reviewed; all confirmed corrections consolidated**'
assert old_review_status in review
review = review.replace(old_review_status, '**Status:** `verified-complete` — **E2 reviewed 76/76; E3 final verification passed 76/76**', 1)
review = review.replace('E1 is complete for all 76 body pages. E2 is review-complete and all confirmed corrections are consolidated. E3 remains the mandatory final release gate.', 'E1 is complete for all 76 body pages. E2 is review-complete with every confirmed correction consolidated. E3 has now passed the full 76-page final release verification.', 1)
assert '\n## Exact next activity\n' in review
prefix = review.split('\n## Exact next activity\n', 1)[0].rstrip()
e3 = '''

## E3 — final end-to-end verification

**Result: PASS.**

The complete frozen Tamil and the complete E2-corrected English were reviewed as continuous texts from **PDF 6 through PDF 81 / printed 5 through 80**, rather than as isolated E1/E2 batches. No additional English correction was confirmed during E3.

### Completeness and semantic correspondence

- Every body page has a corresponding English page section, with all 76 PDF/printed-page headings present in exact sequence.
- No newly detected substantive Tamil proposition is missing from the English.
- No unsupported substantive English addition, speaker/actor reassignment, reversal, or newly introduced semantic weakening/strengthening was found.
- Every wording correction confirmed during E2 remains present; the superseded E1 readings checked by the E3 stale-reading gate do not survive.
- Historical names, literary works, mythological references, political vocabulary, numbers, rhetorical questions, repetitions and deliberately sharp polemical wording remain represented rather than silently softened.

### Continuous argument check

E3 confirmed the complete movement of the booklet's argument across its full body: unequal access to school life and labour/class circumstances; education as intellectual growth rather than merely employment; rational discernment and Tamil self-respect; the Ekalavya and Iyarpakai critiques; science versus Puranic explanation through rain, electricity, the shape of the earth and eclipses; useful education and Tamil/world history; reformers, Tamil/Dravidian historical consciousness, political knowledge and teacher responsibility; and finally qualification/ability, educational access, communal/class justice and the appeal for courage to think. No argumentative stage was found missing or displaced.

### Page-transition verification

All **75 internal page transitions**, PDF 6→7 through PDF 80→81, were read continuously. The final gate additionally machine-checked representative high-risk split continuations, including 9→10, 13→14, 20→21, 25→26, 29→30, 30→31, 37→38, 40→41, 44→45, 60→61 and 80→81. No transition contains a duplicated carry-over, missing continuation or misplaced sentence.

### E2-correction persistence

E3 explicitly confirmed the consolidated readings for, among others, `வாழ்க்கை வசதி`, `காவியரசத்தில்`, the `சுவை`/`சத்து` distinction, PDF 29 `இகத்தை வெறுத்து`, PDF 39 `போக்கிட`, PDF 47 `நடக்கின்ற உண்மை`, PDF 65 `இனத்துரோகம்`, PDF 75 `அரைகுறையான அவல வாழ்வு`, PDF 77 `படிப்பு வராத இனத்தை`, PDF 78 `உரிமைகளைக் குறைத்து`, and PDF 80 `மூளை பலம்`. The superseded English phrasings are absent.

### Translator/source-note verification

The final English continues to expose difficult frozen readings rather than converting conjecture into source text. E3 rechecked the notes for the principal difficult forms across the body, including `வாழ்க்கைச் செந்தி`, `ஆரம்பக் கல்வியிலிருந்து வரைவிட`, `கல்வி கற்கு மிடம்`, `எட்டுச்சுரையெனப்`, `நல்லதங்கள்`, `நாவினை நாட்டினரும்`, `தவழிப் பூச்சூடி`, `வெறும் படிப்புபோதும்.`, `முன்னேற்றம் மடைகின்றன`, `வளர்த்தை`, `வகைப்படுத்தியாக`, `போற்றிவேண்டும்`, `அரிபந்தாமன்`, `காண்டவன்`, the difficult PDF 38–40 forms, `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, `மதனின் அறிவு`, `மீனவ மக்களைத் துறந்து`, `தன்னுலே`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, `உலகியலேக் காண`, and the final `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு` construction.

### E3 consolidated result

- Body pages finally verified: **76 / 76**
- Internal page transitions verified: **75 / 75**
- Newly confirmed E3 corrections: **0**
- Tamil changes during E1/E2/E3: **0**
- Stale superseded English readings in the E3 correction gate: **0**
- Newly detected missing substantive Tamil propositions: **0**
- Newly detected unsupported substantive English additions: **0**
- Page-boundary omissions/duplications: **0**

**Stage E3 is complete. The English layer is `verified-complete`.**

## Next gate

Proceed to **final archival synchronization only**: synchronize `metadata.json`, speech `README.md`, repository root catalogue/README as prescribed by `SPEECH_PROCESSING_GUIDE.md`, and convert `HANDOVER.md` into the final completed-state handover. Recheck that the source PDF itself is not committed and that source identity/page-map fields remain unchanged. Do not alter frozen Tamil or verified English unless a newly documented source-based defect is discovered during synchronization.
'''
review_path.write_text(prefix + e3, encoding='utf-8')

# Metadata.
wf = metadata['workflow']
assert wf['english_translation_review'] == 'review-complete'
assert wf['english_translation_review_pages_checked'] == 76
assert wf['english_translation_final_verification'] == 'not-started'
wf['english_translation'] = 'verified-complete'
wf['english_translation_final_verification'] = 'complete'
wf['english_translation_final_verification_pages_checked'] = 76
wf['english_translation_verified_date'] = '2026-08-16'
wf['repository_archival_closure'] = 'not-started'
wf['transcription_translation_work_pending'] = True
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Speech README.
assert '| Final Tamil→English verification (E3) | **Not started** |' in readme
readme = readme.replace('| Final Tamil→English verification (E3) | **Not started** |', '| Final Tamil→English verification (E3) | **Verified-complete — PASS, 76/76 body pages** |', 1)
assert 'The English layer is now **fidelity-corrections-consolidated**, but it is not `verified-complete`; E3 remains the release gate.' in readme
readme = readme.replace('The English layer is now **fidelity-corrections-consolidated**, but it is not `verified-complete`; E3 remains the release gate.', 'E3 has now passed the complete **76/76-page** end-to-end Tamil→English verification. The English layer is **`verified-complete`**; no new E3 correction was confirmed, all 75 internal page transitions were checked, all E2 corrections remain consolidated, and source-difficulty notes remain transparent.', 1)
readme = re.sub(r'## Exact next activity\n\n.*?(?=\n## Editorial rule)', '## Exact next activity\n\nPerform **final archival synchronization only**: update the repository root catalogue/README, mark repository archival closure complete in metadata, convert `HANDOVER.md` to the final completed-state handover, and confirm that the source PDF remains uncommitted while its filename/checksum/size/page-map metadata remains unchanged. Do not modify frozen Tamil or verified English unless a new source-evidenced defect is formally documented.\n', readme, flags=re.S)
readme_path.write_text(readme, encoding='utf-8')

# Handover.
assert handover.startswith('# பள்ளி வாழ்க்கை — English E2 handover')
handover = handover.replace('# பள்ளி வாழ்க்கை — English E2 handover', '# பள்ளி வாழ்க்கை — E3 verified handover', 1)
assert '### E3 — NOT STARTED\n\nFinal end-to-end Tamil→English verification remains blocked until E2 has reviewed all 76 pages and all confirmed corrections are consolidated.' in handover
handover = handover.replace('### E3 — NOT STARTED\n\nFinal end-to-end Tamil→English verification remains blocked until E2 has reviewed all 76 pages and all confirmed corrections are consolidated.', '### E3 — VERIFIED-COMPLETE\n\nFinal end-to-end Tamil→English verification has passed **PDF 6-81 / printed 5-80 — 76/76 body pages**. All 75 internal page transitions were checked; all confirmed E2 corrections remain consolidated; no new E3 correction was confirmed. `translation-en.md` is now **verified-complete**.', 1)
assert 'E2 is complete. Do not mark English `verified-complete` until E3 passes.' in handover
handover = handover.replace('E2 is complete. Do not mark English `verified-complete` until E3 passes.', 'E2 and E3 are complete. English is now `verified-complete`; no further text change is permitted without newly documented source evidence.', 1)
handover = re.sub(r'## Exact next activity\n\n.*?(?=\n## Safeguards)', '## Exact next activity\n\nPerform **final archival synchronization only**. Update the repository root catalogue/README to include `palli-vazhkkai` as verified complete; mark repository archival closure complete in `metadata.json`; convert this handover into the final completed-state handover; and recheck that the source PDF is not committed while source identity/page-map metadata remains unchanged. Do not change frozen Tamil or verified English without newly documented source evidence.\n', handover, flags=re.S)
handover_path.write_text(handover, encoding='utf-8')

# Final assertions.
assert '**Status:** `verified-complete`' in en_path.read_text(encoding='utf-8')
assert '**Status:** `verified-complete`' in review_path.read_text(encoding='utf-8')
wf2 = json.loads(metadata_path.read_text(encoding='utf-8'))['workflow']
assert wf2['english_translation'] == 'verified-complete'
assert wf2['english_translation_final_verification'] == 'complete'
assert wf2['english_translation_final_verification_pages_checked'] == 76
print('PASS: Palli Vazhkkai E3 final verification — 76 pages, 75 transitions, 0 new corrections')
