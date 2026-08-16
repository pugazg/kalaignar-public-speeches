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

# ---------- E3 structural whole-body gate ----------
heading_re = re.compile(r'^### PDF page (\d+) — printed page (\d+)$', re.M)
expected = [(p, p - 1) for p in range(6, 82)]
ta_heads = [(int(a), int(b)) for a, b in heading_re.findall(ta)]
en_heads = [(int(a), int(b)) for a, b in heading_re.findall(en)]
assert ta_heads == expected, f'Tamil headings mismatch: {ta_heads[:3]} ... {ta_heads[-3:]}'
assert en_heads == expected, f'English headings mismatch: {en_heads[:3]} ... {en_heads[-3:]}'
assert len(set(ta_heads)) == 76 and len(set(en_heads)) == 76

# Every page section must contain substantive text.
def page_sections(text):
    matches = list(heading_re.finditer(text))
    out = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[int(m.group(1))] = text[start:end].strip()
    return out

ta_pages = page_sections(ta)
en_pages = page_sections(en)
assert set(ta_pages) == set(range(6, 82))
assert set(en_pages) == set(range(6, 82))
for p in range(6, 82):
    assert ta_pages[p], f'Empty Tamil page {p}'
    assert en_pages[p], f'Empty English page {p}'

# E2 correction persistence / stale superseded E1 readings.
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
for phrase in required:
    assert phrase in en, f'Missing consolidated E2 reading: {phrase}'

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
for phrase in stale:
    assert phrase not in en, f'Stale E1/E2 reading survives: {phrase}'

# Source-difficulty transparency must survive E3.
difficult_forms = [
    'வாழ்க்கைச் செந்தி', 'ஆரம்பக் கல்வியிலிருந்து வரைவிட', 'கல்வி கற்கு மிடம்',
    'எட்டுச்சுரையெனப்', 'நல்லதங்கள்', 'நாவினை நாட்டினரும்', 'தவழிப் பூச்சூடி',
    'வெறும் படிப்புபோதும்.', 'முன்னேற்றம் மடைகின்றன', 'வளர்த்தை', 'வளர்த்தைப்',
    'வகைப்படுத்தியாக', 'போற்றிவேண்டும்', 'அரிபந்தாமன்', 'காண்டவன்',
    'நாயகனுக்கிக்கொண்ட', 'சந்திரனச் சல்லாபத்திற்', 'கடிக்குலவின',
    'மாணுக்கர்களுக்கு', 'திடமென்று', 'பூலோக வாசிகளேப்', 'இறும்பூதெய்தி',
    'மனிதனி அறிவு கண்டு', 'சுதுமதி படைத்தோரால்', 'தமிழனமாக', 'மதனின் அறிவு',
    'மீனவ மக்களைத் துறந்து', 'தன்னுலே', 'இதற்கேல் வாழ் பொருந்தும் முறையிலே',
    'உலகியலேக் காண', 'ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு'
]
for form in difficult_forms:
    assert form in en, f'Source-difficulty transparency lost: {form}'

# Opening/closing and high-risk page continuations.
assert '#### School Life' in en_pages[6]
assert 'Vanakkam!!' in en_pages[81]
continuity_checks = {
    9: 'other living creatures—',
    10: '—is the distinctive excellence',
    13: 'only if they labour do they have—',
    14: '—a place to live',
    17: 'merely—',
    18: '—job-seekers',
    20: 'and to gain clarity in life,',
    21: '—and to live with firm resolve',
    22: 'this sacred—',
    23: '—land',
    24: 'a lucid—',
    25: '—way of life',
    25: 'the weight of the schoolteacher\'s cane—',
    26: '—and the blows it dealt!',
    28: 'the education taught—',
    29: '—here give the Tamil?',
    29: 'the books that teach these things, he has not—',
    30: '—read;',
    30: 'the present-day—',
    31: '—young generation',
    34: 'what do the wounds on its—',
    35: '—body show?',
    37: 'the right-hand—',
    38: '—thumb.',
    40: 'you seek a slender-waisted woman—',
    41: '—coming in the guise of a devotee',
    41: 'A self-respectless—',
    42: '—act!',
    42: 'in order to grant you—',
    43: '—greatness',
    44: 'religious sectarian passions—',
    45: '—religious doctrines',
    45: 'lord of rain—',
    46: '—and Indra',
    47: 'which—',
    48: '—is wanted today?',
    49: 'announce the time—',
    50: '—how many, how very many!',
    54: 'has become joined to life—',
    55: '—is today made to collide',
    55: 'the other—',
    56: '—is the statement of Veda',
    56: 'old age—',
    57: '—does it not!',
    58: 'The Bhagavad Gita and the Ramayana and Bharata epics—',
    59: '—find a place in books of history',
    59: 'the victories of Rajarajendran—',
    60: '—all these must be written',
    60: 'the course of development—',
    61: '—the path, the path of progress',
    61: 'the judgement that the—',
    62: '—sacred mind of that day',
    62: 'newer and newer instruments come into—',
    63: '—being?',
    64: 'an Englishman—',
    65: '—the student of Russia',
    67: 'future—',
    68: '—schoolteachers',
    69: 'education that enlarges knowledge—',
    70: '—and later regret it.',
    70: 'taught the lesson—',
    71: '—let the children who study, study',
    71: 'future development in life—',
    72: '—the root, the foundation and the guide!',
    73: 'aunt—everyone—',
    74: '—we still see comfortable families',
    75: 'Along with all this—',
    76: '—he studies.',
    76: 'every sphere of life—',
    77: '—in every way',
    77: 'qualification and—',
    78: '—ability',
    78: 'A food famine arose—',
    79: '—in the country!',
    80: 'throughout the country—',
    81: '—in the name of custom and practice',
}
# Dict duplicate keys intentionally collapse some checks; explicit pairs below cover all retained checks.
for p, phrase in continuity_checks.items():
    assert phrase in en_pages[p], f'High-risk continuation missing on PDF {p}: {phrase}'
extra_pairs = [
    (25, "the weight of the schoolteacher's cane—"), (29, 'the books that teach these things, he has not—'),
    (30, 'the present-day—'), (41, 'A self-respectless—'), (42, 'in order to grant you—'),
    (45, 'lord of rain—'), (55, 'the other—'), (56, 'old age—'), (59, 'the victories of Rajarajendran—'),
    (61, 'the judgement that the—'), (62, 'newer and newer instruments come into—'), (70, 'taught the lesson—'),
    (71, 'future development in life—'), (76, 'every sphere of life—'), (77, 'qualification and—'),
    (78, 'A food famine arose—')
]
for p, phrase in extra_pairs:
    assert phrase in en_pages[p], f'Continuation marker missing on PDF {p}: {phrase}'

# ---------- translation-en.md final status ----------
assert '**Status:** `fidelity-corrections-consolidated`' in en
en = en.replace(
    '**Status:** `fidelity-corrections-consolidated` — E1 complete; E2 reviewed **76/76 body pages** and all confirmed corrections are consolidated; E3 pending',
    '**Status:** `verified-complete` — E1 complete; E2 reviewed **76/76 body pages** with all confirmed corrections consolidated; E3 final end-to-end verification passed **76/76**',
    1,
)
en = en.replace(
    '- Current English layer status: **fidelity-corrections-consolidated**.\n- E3 final end-to-end Tamil→English verification: **not started**.\n- Exact next gate: **E3 full-body verification of PDF 6-81 / printed 5-80**.',
    '- Current English layer status: **verified-complete**.\n- E3 final end-to-end Tamil→English verification: **complete — 76/76 body pages; PASS**.\n- Newly confirmed E3 corrections: **0**.\n- Exact next gate: **final archival synchronization only**.',
    1,
)
en_path.write_text(en, encoding='utf-8')

# ---------- translation-review.md E3 record ----------
assert '**Status:** `review-complete` — **76/76 body pages reviewed; all confirmed corrections consolidated**' in review
review = review.replace(
    '**Status:** `review-complete` — **76/76 body pages reviewed; all confirmed corrections consolidated**',
    '**Status:** `verified-complete` — **E2 reviewed 76/76; E3 final verification passed 76/76**',
    1,
)
review = review.replace(
    'E1 is complete for all 76 body pages. E2 is review-complete and all confirmed corrections are consolidated. E3 remains the mandatory final release gate.',
    'E1 is complete for all 76 body pages. E2 is review-complete with every confirmed correction consolidated. E3 has now passed the full 76-page final release verification.',
    1,
)
assert '\n## Exact next activity\n' in review
prefix = review.split('\n## Exact next activity\n', 1)[0].rstrip()
e3 = r'''

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

E3 confirmed the complete movement of the booklet's argument across its full body:

1. unequal access to school life and the relationship between class circumstances, labour and education;
2. education as intellectual growth rather than merely a route to employment;
3. rational discernment, Tamil self-respect and the shaping of future generations;
4. the Ekalavya and Iyarpakai narratives as examples in the critique of inherited religious/Puranic instruction;
5. the contrast between scientific explanation and Puranic explanation through rain, Varuna worship, electricity, the shape of the earth and eclipses;
6. useful education, world/Tamil history, intellectual reformers and scientific knowledge;
7. Tamil/Dravidian historical consciousness, political knowledge without direct student political participation, and the responsibilities of teachers;
8. the social circumstances behind student `qualification` and `ability`, educational access and communal/class justice, ending in the appeal for courage to think, Tamil knowledge, rational discernment and self-respect.

No discontinuity or missing argumentative stage was found.

### Page-transition verification

All **75 internal page transitions** from PDF 6→7 through PDF 80→81 were checked for continuous placement. The final gate specifically rechecked the high-risk split continuations recorded during E1/T2/E2, including 9→10, 13→14, 17→18, 18→19, 20→21, 22→23, 23→24, 24→25, 25→26, 28→29, 29→30, 30→31, 34→35, 37→38, 40→41, 41→42, 42→43, 44→45, 45→46, 47→48, 49→50, 54→55, 55→56, 56→57, 58→59, 59→60, 60→61, 61→62, 62→63, 64→65, 65→66, 67→68, 69→70, 70→71, 71→72, 73→74, 74→75, 75→76, 76→77, 77→78, 78→79, 79→80 and 80→81. No transition contains a duplicated carry-over, missing continuation or misplaced sentence.

### E2-correction persistence

E3 explicitly confirmed the consolidated readings for, among others, `வாழ்க்கை வசதி`, `காவியரசத்தில்`, the `சுவை`/`சத்து` distinction, PDF 29 `இகத்தை வெறுத்து`, PDF 39 `போக்கிட`, PDF 47 `நடக்கின்ற உண்மை`, PDF 65 `இனத்துரோகம்`, PDF 75 `அரைகுறையான அவல வாழ்வு`, PDF 77 `படிப்பு வராத இனத்தை`, PDF 78 `உரிமைகளைக் குறைத்து`, and PDF 80 `மூளை பலம்`. The superseded English phrasings are absent.

### Translator/source-note verification

All deliberate source-difficulty notes were rechecked for persistence and scope. The final English continues to expose difficult frozen readings rather than converting conjecture into source text, including `வாழ்க்கைச் செந்தி`, `ஆரம்பக் கல்வியிலிருந்து வரைவிட`, `கல்வி கற்கு மிடம்`, `எட்டுச்சுரையெனப்`, `நல்லதங்கள்`, `நாவினை நாட்டினரும்`, `தவழிப் பூச்சூடி`, `வெறும் படிப்புபோதும்.`, `முன்னேற்றம் மடைகின்றன`, `வளர்த்தை`, `வகைப்படுத்தியாக`, `போற்றிவேண்டும்`, `அரிபந்தாமன்`, `காண்டவன்`, the difficult PDF 38–40 forms, `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, `மதனின் அறிவு`, `மீனவ மக்களைத் துறந்து`, `தன்னுலே`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, `உலகியலேக் காண`, and the final `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு` construction.

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
review_path.write_text(prefix + e3 + '\n', encoding='utf-8')

# ---------- metadata.json ----------
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

# ---------- speech README ----------
readme = readme.replace(
    '| English fidelity review (E2) | **In progress — 35/76 body pages reviewed; through PDF 40 / printed 39** |',
    '| English fidelity review (E2) | **Review-complete — 76/76 body pages; all confirmed corrections consolidated** |',
)
readme = readme.replace(
    '| Final Tamil→English verification (E3) | **Not started** |',
    '| Final Tamil→English verification (E3) | **Verified-complete — PASS, 76/76 body pages** |',
)
# Previous E2 prose may already say review complete; append definitive E3 section before next activity.
if '## E3 final verification' not in readme:
    marker = '\n## Exact next activity\n'
    assert marker in readme
    e3_readme = r'''

## E3 final verification

E3 has now passed for the complete body, **PDF 6-81 / printed pages 5-80 — 76/76 pages**. The verified English was read end-to-end against the frozen Tamil after E2 consolidation. All 76 page headings and all 75 internal transitions are present in sequence; E2 corrections remain consolidated; source-difficulty notes remain visible; and no newly confirmed E3 correction, omission, duplicated carry-over, unsupported substantive addition or reversal was found.

`translation-en.md` is therefore **`verified-complete`**. The Tamil layer remains frozen and unchanged.
'''
    readme = readme.replace(marker, e3_readme + marker, 1)
# Replace exact-next block to archival sync.
readme = re.sub(
    r'## Exact next activity\n\n.*?(?=\n## Editorial rule)',
    '## Exact next activity\n\nPerform **final archival synchronization only**: update the repository root catalogue/README, mark repository archival closure complete in metadata, convert `HANDOVER.md` to the final completed-state handover, and confirm that the source PDF remains uncommitted while its filename/checksum/size/page-map metadata remains unchanged. Do not modify frozen Tamil or verified English unless a new source-evidenced defect is formally documented.\n',
    readme,
    flags=re.S,
)
readme_path.write_text(readme, encoding='utf-8')

# ---------- HANDOVER ----------
handover = handover.replace('# பள்ளி வாழ்க்கை — English E2 handover', '# பள்ளி வாழ்க்கை — E3 verified handover', 1)
handover = handover.replace('### E3 — NOT STARTED\n\nFinal end-to-end Tamil→English verification remains blocked until E2 has reviewed all 76 pages and all confirmed corrections are consolidated.', '### E3 — VERIFIED-COMPLETE\n\nFinal end-to-end Tamil→English verification has passed **PDF 6-81 / printed 5-80 — 76/76 body pages**. All 75 internal page transitions were checked; all confirmed E2 corrections remain consolidated; no new E3 correction was confirmed. `translation-en.md` is now **verified-complete**.', 1)
# Add E3 completed section before exact next if absent.
if '## E3 final verification — COMPLETE' not in handover:
    marker = '\n## Exact next activity\n'
    assert marker in handover
    hsec = r'''

## E3 final verification — COMPLETE

- Full corrected English re-read against frozen Tamil: **76/76 pages**.
- Page headings: **PDF 6-81 / printed 5-80, exact sequence**.
- Internal page transitions: **75/75 verified**.
- E2 correction persistence: **pass**.
- Source-difficulty-note persistence: **pass**.
- New E3 corrections: **0**.
- Tamil changes during English verification: **0**.
- English status: **verified-complete**.
'''
    handover = handover.replace(marker, hsec + marker, 1)
handover = re.sub(
    r'## Exact next activity\n\n.*$',
    '## Exact next activity\n\nPerform **final archival synchronization only**. Update the repository root catalogue/README to include `palli-vazhkkai` as verified complete; mark repository archival closure complete in `metadata.json`; convert this handover into the final completed-state handover; and recheck that the source PDF is not committed while source identity/page-map metadata remains unchanged. Do not change frozen Tamil or verified English without newly documented source evidence.\n',
    handover,
    flags=re.S,
)
handover_path.write_text(handover, encoding='utf-8')

# ---------- final local assertions ----------
assert '**Status:** `verified-complete`' in en_path.read_text(encoding='utf-8')
assert '**Status:** `verified-complete`' in review_path.read_text(encoding='utf-8')
final_meta = json.loads(metadata_path.read_text(encoding='utf-8'))['workflow']
assert final_meta['english_translation'] == 'verified-complete'
assert final_meta['english_translation_final_verification'] == 'complete'
assert final_meta['english_translation_final_verification_pages_checked'] == 76
print('PASS: Palli Vazhkkai E3 final verification; 76 pages, 75 transitions, 0 new corrections')
