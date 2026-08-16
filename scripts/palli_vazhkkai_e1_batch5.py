from pathlib import Path
import json
import re

root = Path('speeches/palli-vazhkkai')
translation = root / 'translation-en.md'
metadata = root / 'metadata.json'
readme = root / 'README.md'
handover = root / 'HANDOVER.md'

# --- translation-en.md ---
text = translation.read_text(encoding='utf-8')
old_status = '**Status:** `in-progress` — E1 translated through **PDF page 25 / printed page 24** (**20/76 body pages**)  '
new_status = '**Status:** `in-progress` — E1 translated through **PDF page 30 / printed page 29** (**25/76 body pages**)  '
assert old_status in text
text = text.replace(old_status, new_status, 1)
assert '\n## E1 progress\n' in text
text = text.split('\n## E1 progress\n', 1)[0].rstrip() + '\n\n'

batch = r'''### PDF page 26 — printed page 25

—and the blows it dealt!

For a child's education, it is not enough merely to feel pride, satisfaction, and contentment when he has learned his letters, learned to read words together, learned to do sums, practised writing letters, learned to tell and read stories, and reached the point of receiving the title and good certificate of “an educated man”!

School life must become a useful life; it must be made so.

School life must be a life in which one gains knowledge that gives encouragement and constructive power toward the ways and means of enriching life and enriching one's own life.

Mere study is enough. To pass through many classes, study up to a certain limit, pass an examination, and be satisfied that one is fit for employment—education pursued only to that extent has no benefit, no use!

Education necessary for life must be taught in schools. For a Tamil to live as a Tamil, to stand with self-respect, to honour his own language, to be capable of protecting his own country, as a valiant Tamil—

*[Translator/source note: the frozen Tamil has the abrupt sentence `வெறும் படிப்புபோதும்.` (“Mere study is enough”) immediately before rejecting education pursued only for examinations and employment. It is translated as printed rather than silently changed to “mere study is not enough.”]*

### PDF page 27 — printed page 26

—as a self-confident Tamil, as a self-respecting Tamil, a life that melts and moulds the Tamil son, the Tamil child—such a life is the “school life” needed by the Tamil, a life that prepares the way for a useful life!

The distinctive quality possessed by the human being, the condition that places him above other living creatures, is the rational discernment within him!

Rational discernment arises within worldly knowledge, within a condition of knowing well the nature of worldly affairs. To understand worldly life, one must know the affairs and practices of the world in every field.

Life in the world is changing very, very rapidly today; changing again and again, it continues to advance!

In the world, we see that those who until yesterday lived as savages have today changed the sphere of their lives into modern, civilized ways of living and stand in the forefront!

In the world, the instruments of life—the means by which nature is cultivated, prepared, and used for human life—are undergoing rapid advancement.

*[Translator/source note: the frozen Tamil contains the source-supported unusual form `முன்னேற்றம் மடைகின்றன`; “are undergoing rapid advancement” renders the sense contextually without changing the Tamil witness.]*

### PDF page 28 — printed page 27

If a human being wishes, he flies—in an aeroplane. If a human being thinks to speak, he speaks with others living in any part of the world through the instrument called the telephone.

If a human being speaks—speaks at one end of the world—it can be heard in an instant from any other part of the world! That is radio, is it not!

From radio, the world has today advanced to the stage called television, where it is possible even to see the person who is speaking!

The old days of tying up bundles of food, travelling on foot, riding on goats and cattle, and going in wooden carts along rough and rugged roads are not the days of today! Nor can they be. If they remained so, such people would be unable to live in today's world. They would be called dullards who do not know the value of time, people without rational discernment who waste time and squander human labour.

At a time when the world is advancing in civilization, in the fields that enrich life, what is the condition of this country—Tamil Nadu, this sacred land?

Here, what is the plan of educational instruction, the instrument by which people gain knowledge? What benefit does the education taught—

### PDF page 29 — printed page 28

—here give the Tamil? We must think about it. Is the education and growth of knowledge that are needed being provided here?

Even now, we do not see the history of the Nayanmars, Puranic songs, the flavour of the epics, and the Puranas of Ilayankudi Maranar and Iyarpakaiyar failing to find a place in the curriculum!

Religious knowledge—the ideas of a blissful life in a higher world beyond this worldly life—has been given first place! The texts explaining them are the most numerous! Those ideas are mixed and remixed, altered and altered again, and preserved in many forms—as epic, Purana, kavya, essay, and story!

There are more texts filled with ideas that foster the false Vedanta that this life, this worldly life, is only an interim period, a lodging-place in which one must earn enough merit to despise this world and enjoy bliss in the next!

The Tamil has still not learned the lesson of caring about himself, of living, of honouring the country in which he lives and the language he speaks, and of working for the welfare of his society and his country; the books that teach these things, he has not—

### PDF page 30 — printed page 29

—read; nor has he been given the opportunity to read them in his school life!

The future! The future of this country—whether it rises or falls, lives or collapses—depends upon the future youth of this country, upon the generations to come!

The generations to come are today's children! The future depends upon the growth, the mental growth, of children of school age!

The manner in which children are cared for, the great task of raising children into adults—the future condition of the Tamil people lies in preparing lion-like Tamils who will give life to the future world, to the Tamil world!

The knowledge today's young children receive—the knowledge they receive today—the lights of knowledge, Tamil feeling, Tamil ethnic feeling, self-awareness, the feeling of self-respect, and the methods of training for life: these must be put in order, refined, and properly arranged, so that the future may live, Tamil may flourish, Tamil Nadu may shine as a sacred land of self-respect, and Tamils may live with fulfilment and without equal!

Those who are to give life to the future—the present-day—

## E1 progress

- Completed: **PDF 6-30 / printed 5-29 — 25/76 pages**.
- Independent E2 fidelity review has **not** begun; per workflow it remains blocked until the full E1 body translation is complete.
- Exact next E1 batch: **PDF 31-35 / printed 30-34**.
'''
text += batch
translation.write_text(text, encoding='utf-8')

# --- metadata.json ---
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation_pages_completed'] == 20
assert wf['english_translation_through_pdf_page'] == 25
assert wf['english_translation_through_printed_page'] == 24
wf['english_translation'] = 'in-progress'
wf['english_translation_pages_completed'] = 25
wf['english_translation_through_pdf_page'] = 30
wf['english_translation_through_printed_page'] = 29
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# --- README.md ---
r = readme.read_text(encoding='utf-8')
r = r.replace('| English translation (E1) | **In progress — 20/76 body pages; through PDF 25 / printed 24** |',
              '| English translation (E1) | **In progress — 25/76 body pages; through PDF 30 / printed 29** |', 1)
assert '## English translation progress\n' in r and '## Exact next activity\n' in r
new_progress = '''## English translation progress

E1 is being translated only from the frozen Tamil layer. `translation-en.md` now contains **PDF 6-30 / printed pages 5-29 — 25/76 pages**.

Batch 5, PDF 26-30, continues the schoolteacher's-cane sentence from PDF 25 and develops the argument that school life must form a useful, self-respecting life rather than merely produce credentials for employment. It then turns to rational discernment, rapid technological change, the content of the curriculum, religious and otherworldly instruction, and the responsibility of today's children for the Tamil future.

Page-spanning continuations remain explicit at PDF 26→27, PDF 28→29, PDF 29→30, and PDF 30→31. Source-supported difficulties are not silently repaired: the abrupt `வெறும் படிப்புபோதும்.` and unusual `முன்னேற்றம் மடைகின்றன` are called out in concise translator/source notes.

No E2 fidelity review has begun; that gate remains blocked until the entire E1 body is translated.

'''
r = re.sub(r'## English translation progress\n.*?(?=## Exact next activity\n)', new_progress, r, flags=re.S)
r = re.sub(r'## Exact next activity\n\n.*?(?=\n## Editorial rule)',
           '## Exact next activity\n\nContinue **E1 English translation with PDF 31-35 / printed pages 30-34** from the frozen `transcription-ta.md`, beginning with the continuation of the unfinished PDF 30 phrase `இன்றைய` / `இளஞ்சமுதாயம்`. Preserve PDF/printed-page correspondence, argument structure, repetition, rhetorical force, historical references, and source difficulty. Do not translate independently from OCR or silently repair unusual Tamil; where a literal rendering would mislead, use a concise translator/source note.\n',
           r, flags=re.S)
readme.write_text(r, encoding='utf-8')

# --- HANDOVER.md ---
h = handover.read_text(encoding='utf-8')
h = h.replace('Completed E1 scope: **PDF 6-25 / printed 5-24 — 20/76 body pages**.',
              'Completed E1 scope: **PDF 6-30 / printed 5-29 — 25/76 body pages**.', 1)
h = h.replace('- Batch 4: PDF 21-25 / printed 20-24',
              '- Batch 4: PDF 21-25 / printed 20-24\n- Batch 5: PDF 26-30 / printed 25-29', 1)
insert = '''
## E1 Batch 5 — PDF 26-30 / printed 25-29

Completed and committed.

Important translation decisions:

- PDF 25→26 explicitly continues the schoolteacher-cane image: `கம்பின் கனத்தை` / `அடியையும்` is kept as “the weight of the schoolteacher's cane—” / “—and the blows it dealt!”.
- The frozen PDF 26 sentence `வெறும் படிப்புபோதும்.` is translated literally as “Mere study is enough.” A translator/source note records the abrupt tension with the immediately following rejection of examination-and-employment-only education; the Tamil is not silently changed to “not enough.”
- PDF 26→27 preserves the sentence describing the valiant, self-confident, self-respecting Tamil rather than moving the continuation across the page boundary.
- PDF 27's source-supported `முன்னேற்றம் மடைகின்றன` is rendered contextually as “are undergoing rapid advancement” and identified in a translator/source note without altering the frozen Tamil.
- PDF 28's examples of aeroplane, telephone, radio and television are translated in source order; its older travel imagery, including travel on foot, on goats/cattle and in wooden carts, is not modernized away.
- PDF 28→29 keeps `இங்கு போதிக்கப்படும்` / `கல்வி` as “the education taught—” / “—here”.
- PDF 29's religious, Puranic and otherworldly-life critique is translated without adding external explanation or softening its polemical wording.
- PDF 29→30 explicitly preserves the split `கற்பிக்கும் ஏடுகளைப்` / `படிக்கவில்லை` as “the books that teach these things, he has not—” / “—read”.
- PDF 30 retains the repeated `இன்று பெறும் அறிவு` emphasis and the sequence of Tamil feeling, ethnic feeling, self-awareness, self-respect and life-training.
- PDF 30 ends at the source's unfinished `இன்றைய`; English therefore ends “the present-day—” for continuation with `இளஞ்சமுதாயம்` on PDF 31.

'''
assert '\n## Source-fidelity safeguards carried into English\n' in h
h = h.replace('\n## Source-fidelity safeguards carried into English\n', '\n' + insert + '## Source-fidelity safeguards carried into English\n', 1)
h = re.sub(r'## Exact next activity\n\n.*?(?=\n## Safeguards)',
           '## Exact next activity\n\nContinue **E1 English translation with PDF pages 31-35 / printed pages 30-34** from `transcription-ta.md`.\n\nFor that batch:\n\n1. retain the same PDF/printed-page headings in `translation-en.md`;\n2. continue the unfinished PDF 30 phrase faithfully onto PDF 31;\n3. translate every paragraph from the frozen Tamil, with no omitted clause or added historical explanation;\n4. preserve repetition and rhetorical questions rather than smoothing them away;\n5. flag any genuinely difficult frozen Tamil with a concise translator/source note rather than silently correcting it;\n6. update `metadata.json`, `README.md`, and this `HANDOVER.md` with E1 page progress after the batch.\n',
           h, flags=re.S)
handover.write_text(h, encoding='utf-8')

# Sanity checks
out = translation.read_text(encoding='utf-8')
for p in range(26, 31):
    assert f'### PDF page {p} — printed page {p-1}' in out
assert '25/76 body pages' in out.splitlines()[2]
assert 'Exact next E1 batch: **PDF 31-35 / printed 30-34**.' in out
print('Prepared Palli Vazhkkai E1 Batch 5: PDF 26-30 / printed 25-29')
