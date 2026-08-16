from pathlib import Path
import json
import re

root = Path('speeches/palli-vazhkkai')
translation = root / 'translation-en.md'
review = root / 'translation-review.md'
metadata = root / 'metadata.json'
readme = root / 'README.md'
handover = root / 'HANDOVER.md'

# ---------- translation-en.md ----------
text = translation.read_text(encoding='utf-8')
assert '**Status:** `first-pass-complete`' in text

# PDF 47: remove unsupported softening of a source-asserted claim.
old = "At the same time, the student reads news of Russia and the reality said to be occurring there: people go among the clouds in aeroplanes and, through scientific instruments, draw the clouds in and make rain fall in their country!"
new = "At the same time, the student reads news of Russia and the reality occurring there: people go among the clouds in aeroplanes and, through scientific instruments, draw the clouds in and make rain fall in their country!"
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 65: preserve the இனத்துரோகம் / betrayal-of-one's-people force more closely.
old = "Do not put a bolt on the Tamil's feeling of self-respect. That is betrayal of the people—a degrading act!"
new = "Do not put a bolt on the Tamil's feeling of self-respect. That is betrayal of one's people—a degrading act!"
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 70: E1 supplied a contextual negative sense; keep it but expose the difficult frozen syntax.
needle = "The life of the schoolteacher today is not a life of comfort; their wages and salaries are at such a level that they cannot obtain even the ordinary facilities necessary for life! Poverty has always remained the teacher's companion! A pitiable condition!\n"
assert text.count(needle) == 1
text = text.replace(
    needle,
    needle + "\n*[Translator/source note: the frozen Tamil here reads `பள்ளி ஆசிரியர் வாழ்வு, இன்று சுவைதரும் வாழ்வாக, வாழ்க்கைக்குத் தேவையான, சாதாரண வசதிகள் கூடக் கிடைக்க முடியாத அளவில்தான்...`. The following salary clause clearly describes deprivation; the readable English retains that contextual negative sense while recording, rather than silently repairing, the source's difficult syntax.]*\n",
    1,
)

# PDF 75: half-starved over-specified அரைகுறையான; use a closer deprivation rendering.
old = "To live, that poor student must labour with his family and help them! He eats what he can get, wears torn clothes and lives a half-starved, miserable life. Along with all this—"
new = "To live, that poor student must labour with his family and help them! He eats what he can get, wears torn clothes and lives a deprived, miserable life. Along with all this—"
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 77: preserve the source's repeated idiom படிப்பு வராத rather than turn it into reported speech.
old = "Therefore it is not proper, not just, and is contrary to human character to leave the poor and simple, the backward society, the people said to be unable to study, in an even more backward condition, while continuously sending forward on the path of progress only those educated people who already live and grow in educated lineages and favourable surroundings, the children of the rich, and Brahmin students of educated lineages."
new = "Therefore it is not proper, not just, and is contrary to human character to leave the poor and simple, the backward society, the community for whom ‘study does not come,’ in an even more backward condition, while continuously sending forward on the path of progress only those educated people who already live and grow in educated lineages and favourable surroundings, the children of the rich, and Brahmin students of educated lineages."
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 78: source says உரிமைகள் (rights), not privileges; monopoly follows separately as ஏக போகம்.
old = "The human heart must wish to enable others to live as oneself does. The thought, awakening and agitation that we must reduce our own privileges, surrender our monopoly, grant concessions to backward people, create opportunities for them and advance them is needed throughout the country! Very, very much needed!"
new = "The human heart must wish to enable others to live as oneself does. The thought, awakening and agitation that we must reduce our own rights, surrender our monopoly, grant concessions to backward people, create opportunities for them and advance them is needed throughout the country! Very, very much needed!"
assert text.count(old) == 1
text = text.replace(old, new, 1)

# PDF 80: retain the explicit மூளை பலம் metaphor.
old = "For human life to advance today, greater strength of mind is needed. Clarity of thought, the mental capacity and strength to investigate complicated problems, analyse them and reach conclusions play an important part in human life!"
new = "For human life to advance today, greater brain-power is needed. Clarity of thought, the mental capacity and strength to investigate complicated problems, analyse them and reach conclusions play an important part in human life!"
assert text.count(old) == 1
text = text.replace(old, new, 1)

# Advance layer status after E2 review and correction consolidation.
text = text.replace(
    '**Status:** `first-pass-complete` — E1 translated through **PDF page 81 / printed page 80** (**76/76 body pages**)  ',
    '**Status:** `fidelity-corrections-consolidated` — E1 complete; E2 reviewed **76/76 body pages** and all confirmed corrections are consolidated; E3 pending  ',
    1,
)
old_progress = """## E1 progress

- Completed: **PDF 6-81 / printed 5-80 — 76/76 body pages**.
- E1 status: **first-pass-complete**.
- Independent E2 fidelity review has **not** begun.
- Exact next gate: **E2 Tamil→English fidelity review**, beginning with **PDF 6-10 / printed 5-9**."""
new_progress = """## English workflow progress

- E1 first-pass translation: **complete — PDF 6-81 / printed 5-80, 76/76 body pages**.
- E2 Tamil→English fidelity review: **review-complete — 76/76 body pages**.
- All confirmed E2 corrections: **consolidated into this file**.
- Current English layer status: **fidelity-corrections-consolidated**.
- E3 final end-to-end Tamil→English verification: **not started**.
- Exact next gate: **E3 full-body verification of PDF 6-81 / printed 5-80**."""
assert old_progress in text
text = text.replace(old_progress, new_progress, 1)
translation.write_text(text, encoding='utf-8')

# ---------- translation-review.md ----------
r = review.read_text(encoding='utf-8')
assert '**Status:** `in-progress` — **35/76 body pages reviewed**' in r
r = r.replace('**Status:** `in-progress` — **35/76 body pages reviewed**', '**Status:** `review-complete` — **76/76 body pages reviewed; all confirmed corrections consolidated**', 1)
old_row = '| 8 | 41–45 | 40–44 | next |'
new_rows = '''| 8 | 41–45 | 40–44 | reviewed; no new correction required |
| 9 | 46–50 | 45–49 | reviewed; one source-assertion correction consolidated |
| 10 | 51–55 | 50–54 | reviewed; no new correction required |
| 11 | 56–60 | 55–59 | reviewed; existing source-difficulty notes confirmed |
| 12 | 61–65 | 60–64 | reviewed; one polemical-term correction consolidated |
| 13 | 66–70 | 65–69 | reviewed; one source-syntax transparency note consolidated |
| 14 | 71–75 | 70–74 | reviewed; one over-specific rendering corrected |
| 15 | 76–80 | 75–79 | reviewed; three fidelity corrections consolidated |
| 16 | 81 | 80 | reviewed; existing final-page source note confirmed |'''
assert old_row in r
r = r.replace(old_row, new_rows, 1)

prefix = r.split('\n## Exact next activity\n', 1)[0].rstrip()
# Remove old cumulative state so the final one is unique.
prefix = re.sub(r'\n## Cumulative E2 state\n.*$', '', prefix, flags=re.S).rstrip()
remaining = r'''

## Batch 8 — PDF 41–45 / printed 40–44

### Result

The continuation and completion of the Iyarpakai Nayanar episode, the author's polemical critique, and the opening science-versus-Purana rain argument are complete. No clause omission, unsupported addition, reversal, or page-boundary loss was found. The PDF 40→41 and 44→45 continuations remain intact. No new correction was required.

## Batch 9 — PDF 46–50 / printed 45–49

### Result

The rain/Varuna contrast, the Russia example, the repeated rational-discernment questions, and the opening catalogue of science/electricity are structurally complete.

### Confirmed correction

1. **PDF 47 `ரஷ்ய நாட்டுச் செய்தியையும், நடக்கின்ற உண்மையையும்`.** E1 inserted `the reality said to be occurring there`, adding an evidential hedge not present in the frozen Tamil, which presents it as `நடக்கின்ற உண்மை`. The unsupported `said to be` has been removed. This correction follows the source claim without independently endorsing or verifying it.
2. PDF 48's difficult `மனிதனி அறிவு கண்டு` was already preserved explicitly in a translator/source note; no further change was needed.

## Batch 10 — PDF 51–55 / printed 50–54

### Result

No new correction was required. The thought/scientific-progress passage, newspapers/radio/telegram/bank sequence, flat-earth and Varaha narrative, and science-versus-Purana eclipse explanations are complete and preserve their page continuations and rhetorical contrasts.

## Batch 11 — PDF 56–60 / printed 55–59

### Result

No new semantic correction was required. The argument against simultaneously teaching incompatible Puranic and scientific explanations, the call for useful education, and the Tamil-history curriculum critique are complete. Existing notes correctly preserve `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, and `மதனின் அறிவு`; the PDF 60→61 continuation remains explicit.

## Batch 12 — PDF 61–65 / printed 60–64

### Result

The Socrates/Martin Luther/reformer sequence, life-education programme, human-behaviour questions, and Tamil/Dravidian identity argument are complete. Existing transparency for PDF 62 `மீனவ மக்களைத் துறந்து` remains adequate.

### Confirmed correction

1. **PDF 65 `இனத்துரோகம்`.** E1 rendered this as `betrayal of the people`, which weakened the source's explicit `இனம்` force. It now reads `betrayal of one's people`, preserving the polemical collective identity without importing an outside formulation.

## Batch 13 — PDF 66–70 / printed 65–69

### Result

The historical-consciousness argument, school-life-as-weapon metaphor, future-professions catalogue, and distinction between political knowledge and direct student participation are complete. No omission or reversal was found.

### Confirmed transparency action

1. **PDF 70 `பள்ளி ஆசிரியர் வாழ்வு, இன்று சுவைதரும் வாழ்வாக, ...`.** E1 supplied the contextually obvious negative sense (`not a life of comfort`) because the following clause says teachers' salaries do not provide even ordinary necessities. The frozen syntax itself does not state that negation cleanly. A translator/source note now records the exact difficult wording so the readable English is not mistaken for a Tamil correction.

## Batch 14 — PDF 71–75 / printed 70–74

### Result

The teacher-responsibility passage and the extended challenge to inherited ideas of student `qualification` and `ability` are complete. The source's sharp labels for different students remain unsanitized. Existing notes for `தன்னுலே` and `இதற்கேல் வாழ் பொருந்தும் முறையிலே` remain adequate.

### Confirmed correction

1. **PDF 75 `அரைகுறையான அவல வாழ்வு`.** E1's `half-starved, miserable life` added a specific hunger condition beyond the phrase itself. The sentence now reads `a deprived, miserable life`, while the surrounding source references to limited food remain separately translated.

## Batch 15 — PDF 76–80 / printed 75–79

### Result

The poverty/marks argument, human-rights and educational-access sequence, communal/class-justice passage, and the transition into the closing argument are complete. Three fidelity issues were corrected.

### Confirmed corrections

1. **PDF 77 `படிப்பு வராத இனத்தை`.** E1's `people said to be unable to study` turned the source phrase into reported speech. It now retains the text's repeated idiom as `the community for whom ‘study does not come’`.
2. **PDF 78 `தன்னுடைய உரிமைகளைக் குறைத்து`.** E1 used `reduce our own privileges`; the source says `உரிமைகள்` (`rights`) and then separately uses `ஏக போகம்` for monopoly/exclusive enjoyment. The English now reads `reduce our own rights, surrender our monopoly`.
3. **PDF 80 `மூளை பலம்`.** E1's `strength of mind` softened the explicit brain-strength metaphor. It now reads `greater brain-power is needed`.

## Batch 16 — PDF 81 / printed 80

### Result

The final page passed E2 without a new correction. The PDF 80→81 continuation is intact; the closing sequence preserves courage to think, Tamil knowledge, rational discernment, `தமிழினத்தை`, the call to establish `தமிழ்த் திருநாடு`, and the final `வணக்கம் !!`. The existing translator/source note adequately records `உலகியலேக் காண` and the structurally difficult `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு` rather than replacing the frozen witness with outside historical reconstruction.

## Cumulative E2 state

- Reviewed: **PDF 6–81 / printed 5–80 — 76/76 body pages**.
- E2 fidelity review: **review-complete**.
- Every confirmed E2 correction identified in Batches 1–16 has been consolidated into `translation-en.md`.
- The English layer is now **fidelity-corrections-consolidated**, but **not yet verified-complete**.
- E3 final end-to-end Tamil→English verification remains mandatory.
'''
next_section = r'''

## Exact next activity

Perform **E3 final end-to-end Tamil→English verification for PDF 6–81 / printed pages 5–80**. Compare the complete corrected English layer once more against the frozen Tamil from beginning to end, verify page headings and page-boundary continuity, confirm that all E2 corrections are present and no reviewed source difficulties were accidentally normalized, and only then mark the English translation `verified-complete`.
'''
review.write_text(prefix + remaining + next_section, encoding='utf-8')

# ---------- metadata.json ----------
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation_review'] == 'in-progress'
assert wf['english_translation_review_pages_checked'] == 35
wf['english_translation'] = 'fidelity-corrections-consolidated'
wf['english_translation_review'] = 'review-complete'
wf['english_translation_review_pages_checked'] = 76
wf['english_translation_review_through_pdf_page'] = 81
wf['english_translation_review_through_printed_page'] = 80
wf['english_translation_final_verification'] = 'not-started'
wf['english_translation_final_verification_pages_checked'] = 0
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------- README.md ----------
rd = readme.read_text(encoding='utf-8')
old = '| English fidelity review (E2) | **In progress — 35/76 body pages reviewed; through PDF 40 / printed 39** |'
new = '| English fidelity review (E2) | **Review-complete — 76/76 body pages; all confirmed corrections consolidated** |'
assert old in rd
rd = rd.replace(old, new, 1)
rd = re.sub(
    r'E2 is now \*\*in progress\*\*\..*?(?=\n## Exact next activity)',
    "E2 is now **review-complete** for the full body, **PDF 6-81 / printed 5-80 — 76/76 pages**. The remaining review from PDF 41-81 confirmed the Iyarpakai/science/history/reformer/student-politics/teacher/educational-access/closing sequences and consolidated all confirmed fidelity corrections. Important final actions include removing an unsupported hedge from the PDF 47 Russia passage, preserving the `இனத்துரோகம்` force on PDF 65, documenting the difficult PDF 70 teacher-salary syntax, correcting the over-specific PDF 75 `அரைகுறையான` rendering, restoring the PDF 77 `படிப்பு வராத` idiom, retaining `உரிமைகள்` as `rights` on PDF 78, and preserving the `மூளை பலம்` metaphor as `brain-power` on PDF 80. Full findings for all 16 review batches are in `translation-review.md`.\n\nThe English layer is now **fidelity-corrections-consolidated**, but it is not `verified-complete`; E3 remains the release gate.",
    rd,
    count=1,
    flags=re.S,
)
rd = re.sub(
    r'## Exact next activity\n\n.*?(?=\n## Editorial rule)',
    "## Exact next activity\n\nPerform **E3 final end-to-end Tamil→English verification for PDF 6-81 / printed pages 5-80**. Recompare every corrected English page against the frozen Tamil, verify all page boundaries and E2 corrections, confirm source-supported difficult forms remain transparent, and only after that gate passes mark English `verified-complete`.",
    rd,
    count=1,
    flags=re.S,
)
readme.write_text(rd, encoding='utf-8')

# ---------- HANDOVER.md ----------
h = handover.read_text(encoding='utf-8')
h = h.replace(
    '`translation-en.md` preserves PDF/printed-page headings and paragraph sequence throughout the full body. E1 is textually complete but is **not yet verified**; E2 and E3 remain mandatory.',
    '`translation-en.md` preserves PDF/printed-page headings and paragraph sequence throughout the full body. E1 is complete, E2 review/correction consolidation is complete, and E3 final verification remains mandatory.',
    1,
)
h = re.sub(
    r'### E2 — IN PROGRESS\n\n.*?\n\n### E3 — NOT STARTED',
    '### E2 — REVIEW COMPLETE\n\nAll **76/76 body pages, PDF 6-81 / printed 5-80**, have undergone independent Tamil→English fidelity review. Every confirmed E2 correction has been consolidated into `translation-en.md`; `translation-review.md` contains the full Batch 1-16 audit. The English layer state is now **fidelity-corrections-consolidated**.\n\n### E3 — NOT STARTED',
    h,
    count=1,
    flags=re.S,
)
insert_marker = '\n## Source-fidelity safeguards carried into English\n'
assert insert_marker in h
summary = r'''

## E2 remaining review — PDF 41-81 / printed 40-80

Completed and consolidated at the repository owner's request as the final 41-page E2 activity.

Key outcomes:

- PDF 41-45: Iyarpakai conclusion and opening rain/science contrast passed without a new correction.
- PDF 46-50: removed the unsupported `said to be` hedge from the PDF 47 `நடக்கின்ற உண்மை` Russia sentence; existing `மனிதனி அறிவு கண்டு` transparency remains.
- PDF 51-60: scientific/technical catalogues, Varaha/eclipses, useful-education and Tamil-history arguments passed; existing `சுதுமதி`, `தமிழனமாக`, and `மதனின் அறிவு` notes remain adequate.
- PDF 61-65: reformer/humanity/Tamil-identity material passed; PDF 65 `இனத்துரோகம்` is now rendered `betrayal of one's people`.
- PDF 66-70: political-awareness material passed; PDF 70 now documents the difficult `சுவைதரும் வாழ்வாக ... சாதாரண வசதிகள் கூடக் கிடைக்க முடியாத` teacher-salary syntax behind the contextual English negative.
- PDF 71-75: teacher and qualification/ability discussion passed; PDF 75 `அரைகுறையான அவல வாழ்வு` is now `a deprived, miserable life`, not the over-specific `half-starved`.
- PDF 76-80: PDF 77 retains the source's `படிப்பு வராத` idiom, PDF 78 restores `உரிமைகள்` as `rights`, and PDF 80 restores the `மூளை பலம்` metaphor as `brain-power`.
- PDF 81: final page passed with the existing notes for `உலகியலேக் காண` and the difficult Dravidian-land phrase; closing `Vanakkam!!` remains.

E2 is complete. Do not mark English `verified-complete` until E3 passes.
'''
h = h.replace(insert_marker, summary + insert_marker, 1)
h = re.sub(
    r'## Exact next activity\n\n.*?(?=\n## Safeguards)',
    "## Exact next activity\n\nPerform **E3 final end-to-end Tamil→English verification for PDF 6-81 / printed pages 5-80**. Re-read every corrected English page against the frozen Tamil, verify page-boundary continuity and all E2 corrections, confirm difficult source forms remain transparent, and only after the full gate passes set English to `verified-complete`.",
    h,
    count=1,
    flags=re.S,
)
handover.write_text(h, encoding='utf-8')

# ---------- validation ----------
final_t = translation.read_text(encoding='utf-8')
assert 'reality said to be occurring there' not in final_t
assert "betrayal of one's people—a degrading act!" in final_t
assert 'lives a deprived, miserable life' in final_t
assert 'the community for whom ‘study does not come,’' in final_t
assert 'reduce our own rights, surrender our monopoly' in final_t
assert 'greater brain-power is needed' in final_t
assert '**Status:** `fidelity-corrections-consolidated`' in final_t
final_r = review.read_text(encoding='utf-8')
assert '**Status:** `review-complete` — **76/76 body pages reviewed; all confirmed corrections consolidated**' in final_r
assert '| 16 | 81 | 80 | reviewed; existing final-page source note confirmed |' in final_r
assert 'E3 final end-to-end Tamil→English verification' in final_r
final_meta = json.loads(metadata.read_text(encoding='utf-8'))['workflow']
assert final_meta['english_translation'] == 'fidelity-corrections-consolidated'
assert final_meta['english_translation_review'] == 'review-complete'
assert final_meta['english_translation_review_pages_checked'] == 76
assert final_meta['english_translation_review_through_pdf_page'] == 81
