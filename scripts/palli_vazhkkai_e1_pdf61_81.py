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
old_status = '**Status:** `in-progress` — E1 translated through **PDF page 60 / printed page 59** (**55/76 body pages**)  '
new_status = '**Status:** `first-pass-complete` — E1 translated through **PDF page 81 / printed page 80** (**76/76 body pages**)  '
assert old_status in text
text = text.replace(old_status, new_status, 1)
assert '\n## E1 progress\n' in text
text = text.split('\n## E1 progress\n', 1)[0].rstrip() + '\n\n'

batch = r'''### PDF page 61 — printed page 60

—the path, the path of progress, and the history of the civilization that fostered this development must be studied and understood.

The manner in which “God,” the Lord, arose; the present condition of the gods worshipped by early humanity; the manner in which religions originated; the changes that occurred within religions; and the ways and paths by which, from time to time, the state of people's minds and the development of their minds changed—all these must certainly find a place in school life.

When people lived under blind doctrines without even thinking, the Greek thinker Socrates declared, “Think; reflect; observe cause and effect! Dare to think; act; do not follow anything blindly.” We must not fail to study Socrates!

For the crime of teaching people the courage to think, Athens gave its judgement: the cup of poison!

For declaring that “thinking is not a sin; it is human nature,” the reward Socrates received was “the cup of poison!”

“You must drink poison and die”—this was the judgement that the—

### PDF page 62 — printed page 61

—sacred mind of that day and that age gave to Socrates, who dared to think!

In the sphere of religion, in Christianity, we must study in school life the work done amid opposition and ridicule by Martin Luther, who courageously wished to see change and struggled against the Pope!

We must know about Jesus, who died nailed to the cross; Muhammad, who fled in distress after being stoned; Gautama Buddha, who, in the frozen source's wording, left the fisherfolk and went out at midnight seeking peace of mind; Abraham Lincoln, who laboured to break the chains of slavery; Kemal Pasha, who gave new life to Turkey, mocked as a sick man; Sun Yat-sen of China; Karl Marx and Engels, who formulated principles of common ownership; the thinker Rousseau; Voltaire; Lenin; and the noble Gandhi. The lives of all such people must be learned as lessons and understood in school life.

Who discovered radio? Find out. What is the history of the emergence of electricity? Learn it! How did the telescope arise? Learn it! Under what circumstances did newer and newer instruments come into—

*[Translator/source note: the frozen Tamil on this page reads `மீனவ மக்களைத் துறந்து` in the Gautama Buddha clause. That unusual source wording is not silently replaced with an outside historical reconstruction.]*

### PDF page 63 — printed page 62

—being? Do not disregard these things; understand them clearly! School life needs books that explain them!

Human nature, human qualities, humanity must develop. Many books are needed that develop humanity!

A human being must live as a human being. Books of knowledge and works explaining the qualities of the mind must be written so that a person may value himself and others as human beings, possess a humane heart, move away from brutishness, become one endowed with rational discernment, and acquire the ability, knowledge and firmness of mind to examine his circumstances.

All these must find a place in school curricula! They must be made to find a place.

Education for life—the educational knowledge that guides life—is what is needed.

Books that instil ideas of social progress must be read by students in school life.

A human being steals. A human being lies.

### PDF page 64 — printed page 63

At times a human being even abandons his mother and father and wanders as a vagabond! Why? Why does a human being become broken-hearted, lose interest in life and wander in dejection? Why does the human being's brain fail, his reason become clouded, and he become insane? By what causes? By what circumstances? Students must come to know all these things.

Students must read books that give work to human thought—books that foster the capacity to understand even small events and occurrences and the desire to investigate them.

Students must compare past life, past ways of living and past facilities with present life, present ways of living and present facilities; observe the distance, progress and change between the two; and study deeply everything that is needed, every idea that helps knowledge and opens a way to live.

The Tamil son must certainly read books that make him feel and declare that he is a Tamil and that he belongs to the Tamil people!

The student of England calls himself an Englishman—

### PDF page 65 — printed page 64

—the student of Russia declares himself Russian; the Japanese student says he is Japanese; the student of China takes pride in saying that he is Chinese. To say that all this is wrong, an improper act, a fostering of difference, would be as foolish, unfitting, meaningless and unsupported as condemning the student of Tamil Nadu—of the Dravidian land—for saying and feeling that he is a Dravidian and that his country is Dravida Nadu!

A dam against the student's intellectual growth! A barrier to thought, a barrier to progress—unnecessary!

Do not put a bolt on the Tamil's feeling of self-respect. That is betrayal of the people—a degrading act!

The Tamil son who studies the self-respecting history of the Tamil people will shine as a Tamil warrior! When he studies the greatness and noble life of the Tamil land ruled by his ancestors, can he avoid thinking about its condition today? A desire, capacity, knowledge and fearlessness to reform it, refine it, give Tamil Nadu a life of self-respect and establish a distinct Tamil land will surely arise! Why place a barrier, a bolt, against this? There is no need!

### PDF page 66 — printed page 65

When the histories of departed valiant Tamils surge through students' hearts; when thoughts arise that we are descendants of the Three Crowned Kings, born in the land where *Kalingattupparani* was sung, descendants of Cheran Senguttuvan, and that our ancestors conquered Kadaram and lived lives of dignity—what form will their castles of thought, their drops of reflection about the future, take?

“The people who once ruled have become enslaved! Those who stood high have fallen—warriors—are we still to remain in the low condition of bowing at the warrior's feet?” Will the student not think so? As historical events of the past run one after another before his eyes, the student lets out a deep sigh!

A deep sigh! Rising from longing, thinking of the future, recalling the writings of tricksters and the lying Puranas of impostors, will it not, through the anguish of the heart, inevitably become the fiery breath of a boiling volcano?

Writers must remember well that, like trying to extinguish a volcano by pouring water upon it, there is no longer any use in hiding the Tamil people and their history!

### PDF page 67 — printed page 66

Students who must gain such an awakening must not, while seized by that awakening, forget to study during school life!

Do not forget that your “school life” today is the ladder, the staircase, of future ascent and advancement!

Do not ruin the life that gives knowledge! Do not neglect school life, the part of life in which knowledge is gained!

“School life” is the weapon that will restore to the Tamil the rights he has lost; the “school life” you receive is the ammunition that will gather power for the cannon seated upon the rampart of our fortress of knowledge! Remember this! Remember it well!

I emphasize once again: enrich yourselves in school life with the useful education for life that will be needed when “school life” ends and you enter “life.”

Today's students are the future leaders of the country! From among them will arise the scientists and lecturers of the future—

### PDF page 68 — printed page 67

—schoolteachers, college professors, economists, sculptors of thought who reform society, preachers of the righteous path, rulers, government officials, government envoys, commanders who lead soldiers, scholars of books, poets, story writers, creators of epics, essayists, architects who build halls of art, masters of the arts, professors of history, researchers, sculptors of the world of knowledge and thinkers. “School life” is the world in which all these are born and made!

Such excellent training and endeavour are given to the student in school life!

In school life, the student must first direct his full attention and thought toward study!

During school life, students must not enter the broad world of politics; having entered, they must not become directly involved in politics!

Students must not take part in politics; absolutely not! I state this emphatically!

### PDF page 69 — printed page 68

Students must unfailingly observe the political world—the course of politics, its changes and transformations, political events and strategies. They must know political matters. I say that students must gain political knowledge! But at the same time, I will not fail to say that they must not become entangled in day-to-day political life and political events, must not establish direct involvement and turn school life into political life, and must not enter such a condition or environment!

Political knowledge is needed; political events must be watched. But school students must not participate in politics!

Without taking a direct part in politics, students must keep the course of politics in view. It is good for students to engage in politics only after school life has ended and they have reached the position of former students!

Students must remember this well. They must not needlessly become trapped in the gambling and whirl of politics, abandon their studies, descend into mere emotional haste, neglect the education that enlarges knowledge—

### PDF page 70 — printed page 69

—and later regret it. A student's mind must not be allowed to take such a form—must not, must not; absolutely must not! I insist once again!

Everyone knows that the great task of shaping the school student during school life belongs to the schoolteacher!

The life of the schoolteacher today is not a life of comfort; their wages and salaries are at such a level that they cannot obtain even the ordinary facilities necessary for life! Poverty has always remained the teacher's companion! A pitiable condition!

Even in this pitiable condition, their work of teaching school students is good work, beneficial work rendered to the country!

Teachers meet, together in one place at school, students of many, many different kinds. Not only that: they teach them lessons, shape them, and stand in the position of giving them the good certificate of being an “educated person”!

Teachers must not merely say, “We came to school, herded the children together, taught the lesson—

### PDF page 71 — printed page 70

—let the children who study, study; let those who do not, go; what can we do?” and stop there, preparing examination questions, correcting answer sheets and announcing the “result,” thinking that their duty and the labour corresponding to their salary have ended!

The salary is low! There are troubles at home! And the children's mischief in school is beyond description! Dull children, dull-witted frogs, quick children, clever students, lazy pupils, pranksters, clowns—and students of how many other kinds of disposition study in schools!

The teacher is a revolutionary human being who guides students possessing all these contradictory qualities onto the right path, teaches them how to live well, clearly shows good ways and bad ways, teaches lessons, and melts and moulds the student into a person of character, a clear-minded and educated human being.

During the student years, the lessons and teachings, habits and good conduct that teachers impart—speaking with affection, loving with interest, restraining, disciplining and, at some times, even striking—are the beginning of the human being's future development in life—

### PDF page 72 — printed page 71

—the root, the foundation and the guide!

Teachers must understand their responsibility well and shape today's student world—their later generations—so that it acquires sound knowledge and gives life to the future.

We hear many people say that for many students “study does not come,” and that they have to drag along students who possess neither qualification nor ability!

Qualification and ability! “Study does not come; it will not come!” Strange phrases—painful phrases!

An unqualified person, one without qualification; an incapable person, one without ability! Because of what? Why? Study does not come; study will not come! Because of what, why? Raise these questions! Try raising them.

Why is it that only a few students possess qualification and ability while many others lack them? In what respect is qualification absent, and why? In what respect is ability deficient, and because of what?

Who are those who possess qualification and ability? Who?

### PDF page 73 — printed page 72

Which students? What facilities do they possess? In what kind of lineage and living environment do they live? Investigate and see!

Who lacks qualification? With whom is ability deficient or absent? Who are the students unable, in their studies and school lessons, to obtain high marks and pass examinations? What facilities do they possess? In what lineages and living environments do they live? These things too must be investigated.

Who possesses qualification? With whom does it lie? For whom does ability, in the frozen source's `தன்னுலே` wording, arise in study, and why? We must think.

In this country, in sacred Tamil Nadu, there are already certain hereditary groups of learners—educated lineages—that, generation after generation, have lived and grown as lineages of educated people, educated families and educated communities!

The elder brother is educated, the father learned, the grandfather a scholar; one brother a lawyer, another a doctor, another employed in a government office, another a school professor. Mother, elder sister, younger sister—all are educated! The *athimber*, brother-in-law, aunt—everyone—

*[Translator/source note: the frozen Tamil contains the source-supported unusual form `தன்னுலே`. The surrounding sense is rendered without silently altering that witness.]*

### PDF page 74 — printed page 73

—we still see comfortable families living in such surroundings, continuing as educated lineages in which all are educated.

For a student born into a family possessing such comforts of life, such prosperous surroundings, the atmosphere and guidance of an educated lineage, what is surprising about his possessing qualification and ability, being clever in what he studies, in school and examinations, and standing as the student who gains the first mark in the class?

A child of an educated household, generation after generation; a student with a comfortable and prosperous life who has never seen even the shadow of life's suffering and has no need to see it, with no work other than eating, sleeping, studying and playing—why would he not possess qualification and ability? He surely will!

In study, qualification and ability arise almost by themselves for those with means, those whose surroundings and environment are comfortable, those born into an educated lineage!

It is not enough merely to say that the poor cultivator's son has no qualification or ability in learning! Why does he not have qualification?

### PDF page 75 — printed page 74

Why is his ability not visible? We must think about it!

What kind of life does the poor person live? We must look closely at his dwelling, his way of life, his facilities, and the time and money available for study, and ask whether his life and standard of living are prosperous and comfortable under those conditions.

The poor cultivator's son must rise early in the morning, go to the fields with his father and help him. After finishing the morning's work in the fields, he drinks whatever is available—*kambu*, ragi gruel or rice gruel—takes whatever packed food or old rice he can get, and is in the pitiable condition of having to walk even many miles to study!

His is a life of poverty in which he cannot obtain the food he needs, a comfortable dwelling, the necessary clothes, or even buy all the textbooks—all the books—he requires.

To live, that poor student must labour with his family and help them! He eats what he can get, wears torn clothes and lives a half-starved, miserable life. Along with all this—

*[Translator/source note: the frozen Tamil on this page contains the syntactically irregular phrase `இதற்கேல் வாழ் பொருந்தும் முறையிலே`. The surrounding argument is rendered closely without silently rewriting the Tamil source.]*

### PDF page 76 — printed page 75

—he studies. In that family, he will be the first person to have seen school life, the first learner, the first student of the family.

A condition of poverty in which all textbooks cannot be bought! The burden of walking many miles to study and return! The burden of the family besides! In such circumstances, where can clarity be found in him—how can it possibly be found!

Caught in such a constricted environment of life, that poor student is at times unable to obtain even the small number of marks needed for an examination. We must not forget that it is not merely that study “does not come” because of circumstances; because of those very circumstances, his thought, feeling and enthusiasm do not and cannot turn toward study; and that the environment of poverty itself is the cause of what is called his lack of qualification and ability!

We must not calculate qualification and ability merely by looking at the lower marks obtained by a student living an unsettled life of poverty in comparison with a student living a peaceful life!

Qualification and ability are shaped according to each person's circumstances—not only in the field of study but in every sphere of life—

### PDF page 77 — printed page 76

—in every way, as we can see.

Therefore it is not proper, not just, and is contrary to human character to leave the poor and simple, the backward society, the people said to be unable to study, in an even more backward condition, while continuously sending forward on the path of progress only those educated people who already live and grow in educated lineages and favourable surroundings, the children of the rich, and Brahmin students of educated lineages.

This is the age of democracy. Every human being has rights. Every human being must live. This is an age of renaissance in which the principle is blossoming that one human being must not exploit, deceive or degrade another.

Human rights—the rights of the individual, individual rights that do not degrade other human beings or make it impossible for them to live—are being unanimously honoured everywhere in the world!

Rights! Everyone has the right to live. The right to study is an important part of the right to live! A part that gives knowledge! A part that develops knowledge!

In this sphere, in school life, if students are admitted by looking only at qualification and—

### PDF page 78 — printed page 77

—ability, how can ordinary people, the poor and simple, enter school life?

School life must not become the exclusive right of those who are already privileged—the educated, the rich, the Brahmin—those with facilities and opportunities, prosperous conditions of life and educated lineages!

People who have fallen behind because of birth, backward doctrines and poverty must be brought to a condition in which they can come forward and stand alongside others!

The human heart must wish to enable others to live as oneself does. The thought, awakening and agitation that we must reduce our own privileges, surrender our monopoly, grant concessions to backward people, create opportunities for them and advance them is needed throughout the country! Very, very much needed!

The schools that exist are few! The number of students is very large! To say that, because there is not enough money or space to establish new schools, only those with the best qualifications and the greatest ability should be admitted to school is a great betrayal of backward people.

World war broke out! A food famine arose—

### PDF page 79 — printed page 78

—in the country! Did the government not measure, ration and distribute essential foodstuffs to the people?

Could the principle of measured distribution and rationing be abandoned merely because some people possessed more fields and facilities? It could not be abandoned in food distribution!

Likewise, in educational institutions, a method of admitting students according to population, together with the intention of raising those who have fallen behind to the level of others, is needed. Communal/class justice is needed; the Communal G.O. is compulsory as long as classes exist—so that classes and communities may live, so that all communities may live equally!

Those who rule must do what is necessary to change the condition in which it is said that there are no schools, no money and no space!

Those who rule—the politicians governing the country—must give first place to the growth of knowledge and to school life and do everything necessary for it. They must abandon wasteful schemes and spend money in ways that improve school life and make the people discerning!

The people appear as people of low standards of living, as people who do not truly live, as people unable to live.

### PDF page 80 — printed page 79

This is the condition of the majority of the people today in this sacred Tamil land!

In every aspect of life today, ability is required; knowledge becomes necessary! Qualification is regarded as important!

Qualification, ability, the power to plan, the capacity to complete anything properly and clearly, knowledge, the capacity to investigate—all these are needed by the human being today!

For human life to advance today, greater strength of mind is needed. Clarity of thought, the mental capacity and strength to investigate complicated problems, analyse them and reach conclusions play an important part in human life!

A human being must gain the courage to think. Courage is necessary; today the human being is in a condition in which courage is needed even to think!

“Do not investigate this; do not even speak about this; do not doubt that! Do not disobey the Lord's command; live submissively; do not regard this insignificant human life as great and become bound by desires and attachments! Believe in God! Live with devotion, with religious faith! Revere great men! Help the sacred work of monasteries!”—we hear such cries rise throughout the country—

### PDF page 81 — printed page 80

—in the name of custom and practice, in the name of shastra and tradition.

In this condition, is not courage needed in order to think? Thus the existing condition is one in which even to think requires courage, determined thought and a firm mind!

This condition must change. Humanity must become a people with courage, ready to think; Tamils must live with self-respect; all Tamils must shine as Tamils who know Tamil and have learned Tamil. Learn Tamil, gain clarity, and live!

Students! Hold fast to school life and gain clarity; with rational discernment, learn to see worldly life, find the way to rise and live with the world. Study! Study and gain clarity! Make the Tamil people rise with vigour and establish the sacred Tamil land!

To bring into being and establish a sacred land, a Dravidian land—a separate land comprising Tamil, Andhra, Kerala, Kannada and Malayalam peoples—learn and gain clarity from the knowledge that removes ignorance, the capacity for research, histories of peoples, biographies of noble people, science, and the events of the wide world. In school life, lay the foundation to become people of fiery intellect, valiant Tamils, lions of self-respect! Vanakkam!!

*[Translator/source note: the frozen final page retains the unusual form `உலகியலேக் காண` and the structurally difficult phrase `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு`. The English renders the surrounding sense while preserving the source's categories rather than replacing them with an outside reconstruction.]*

## E1 progress

- Completed: **PDF 6-81 / printed 5-80 — 76/76 body pages**.
- E1 status: **first-pass-complete**.
- Independent E2 fidelity review has **not** begun.
- Exact next gate: **E2 Tamil→English fidelity review**, beginning with **PDF 6-10 / printed 5-9**.
'''
text += batch
translation.write_text(text, encoding='utf-8')

# --- metadata.json ---
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation'] == 'in-progress'
assert wf['english_translation_pages_completed'] == 55
assert wf['english_translation_through_pdf_page'] == 60
assert wf['english_translation_through_printed_page'] == 59
wf['english_translation'] = 'first-pass-complete'
wf['english_translation_pages_completed'] = 76
wf['english_translation_through_pdf_page'] = 81
wf['english_translation_through_printed_page'] = 80
wf['english_translation_review'] = 'not-started'
wf['english_translation_review_pages_checked'] = 0
wf['english_translation_final_verification'] = 'not-started'
wf['english_translation_final_verification_pages_checked'] = 0
wf['transcription_translation_work_pending'] = True
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# --- README.md ---
r = readme.read_text(encoding='utf-8')
r = r.replace('| English translation (E1) | **In progress — 55/76 body pages; through PDF 60 / printed 59** |',
              '| English translation (E1) | **First-pass complete — 76/76 body pages; PDF 6-81 / printed 5-80** |', 1)
assert '## English translation progress\n' in r and '## Exact next activity\n' in r
new_progress = '''## English translation progress

E1 is now **first-pass complete** for the entire frozen Tamil body. `translation-en.md` covers **PDF 6-81 / printed pages 5-80 — 76/76 pages**.

The final E1 activity translated **PDF 61-81 / printed 60-80**. It completes the argument for teaching world history, intellectual and social reformers, science and human conduct; develops the case for Tamil/Dravidian self-respect and political awareness without direct student participation; examines the responsibilities and material condition of teachers; challenges inherited ideas of student “qualification” and “ability” by comparing privileged and poor students' circumstances; argues for educational access, communal/class justice and the Communal G.O.; and closes by calling for courage to think, Tamil knowledge, rational discernment and a self-respecting future.

All page boundaries remain explicit, including the PDF 60→61 continuation and the final PDF 80→81 continuation. Difficult frozen forms are not silently repaired. Translator/source notes retain or identify source-supported difficulties including `மீனவ மக்களைத் துறந்து`, `தன்னுலே`, `இதற்கேல் வாழ் பொருந்தும் முறையிலே`, `உலகியலேக் காண`, and the final phrase concerning `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு`.

E2 has **not** begun. Per repository workflow, the next gate is a separate page-by-page Tamil→English fidelity review against the frozen `transcription-ta.md`.

'''
r = re.sub(r'## English translation progress\n.*?(?=## Exact next activity\n)', new_progress, r, flags=re.S)
r = re.sub(r'## Exact next activity\n\n.*?(?=\n## Editorial rule)',
           '## Exact next activity\n\nBegin **E2 English fidelity review with PDF 6-10 / printed pages 5-9**. Compare each English page independently against the frozen Tamil, looking specifically for omitted clauses, additions, reversals, softened or strengthened rhetoric, pronoun/subject errors, historical-name errors, removed repetition, page-boundary omissions, and silent normalization of difficult Tamil. Record findings in `translation-review.md` and consolidate only confirmed corrections into `translation-en.md`.\n',
           r, flags=re.S)
readme.write_text(r, encoding='utf-8')

# --- HANDOVER.md ---
h = handover.read_text(encoding='utf-8')
# Replace E1 status block conservatively.
h = re.sub(r'### E1 — IN PROGRESS\n\n.*?(?=### E2 / E3 — NOT STARTED)',
'''### E1 — FIRST-PASS COMPLETE\n\nEnglish translation has been produced only from the frozen Tamil layer.\n\nCompleted E1 scope: **PDF 6-81 / printed 5-80 — 76/76 body pages**.\n\n`translation-en.md` preserves PDF/printed-page headings and paragraph sequence throughout the full body. E1 is textually complete but is **not yet verified**; E2 and E3 remain mandatory.\n\n### E2 / E3 — NOT STARTED''', h, flags=re.S)
# The substitution above consumes the E2 heading marker; normalize accidental duplication if present.
h = h.replace('### E2 / E3 — NOT STARTED### E2 / E3 — NOT STARTED', '### E2 / E3 — NOT STARTED')

# Add a compact record of final E1 scope before source-fidelity safeguards.
insert = '''\n## E1 final block — PDF 61-81 / printed 60-80\n\nCompleted and committed.\n\nImportant translation decisions:\n\n- PDF 60→61 remains an explicit continuation of the sentence about the historical course of civilizational development.\n- PDF 61-63 preserves the source's sequence from Socrates and Martin Luther through Jesus, Muhammad, Gautama Buddha, Lincoln, Kemal Pasha, Sun Yat-sen, Marx–Engels, Rousseau, Voltaire, Lenin and Gandhi, without adding outside historical explanation.\n- The frozen PDF 62 phrase `மீனவ மக்களைத் துறந்து` is not silently repaired; a translator/source note records it.\n- PDF 64-66 preserves the argument about Tamil/Dravidian identity, self-respect and historical consciousness, including its rhetorical repetition and political vocabulary.\n- PDF 67-70 preserves the distinction between gaining political knowledge and direct student participation in politics.\n- PDF 71-74 retains the source's sharp and sometimes pejorative language about different kinds of students; it is not sanitized. The unusual frozen `தன்னுலே` is recorded in a translator/source note.\n- PDF 75's syntactically irregular `இதற்கேல் வாழ் பொருந்தும் முறையிலே` is not reconstructed; the surrounding argument about poverty and educational opportunity is translated closely and the difficulty is noted.\n- PDF 76-79 preserves the qualification/ability argument, the rights language, the call for concessions and opportunities for backward groups, and the terms `வகுப்பு நீதி` / `கம்யூனல் ஜி. ஓ` without replacing the source with outside historical exposition.\n- PDF 80→81 remains an explicit continuation of the closing argument about the courage required to think.\n- The final page preserves the source-supported difficult `உலகியலேக் காண` and the source's own categories in the phrase concerning `ஆந்திர, கேரள, கன்னட, மலையாளரைக் கொண்ட தனி நாடு`.\n- Final closing is rendered `Vanakkam!!`, preserving the source's emphatic `வணக்கம் !!`.\n\n'''
if '## E1 final block — PDF 61-81 / printed 60-80' not in h:
    h = h.replace('\n## Source-fidelity safeguards carried into English\n', '\n' + insert + '## Source-fidelity safeguards carried into English\n', 1)

h = re.sub(r'## Exact next activity\n\n.*?(?=\n## Safeguards)',
'''## Exact next activity\n\nBegin **E2 English fidelity review with PDF pages 6-10 / printed pages 5-9**.\n\nFor that review batch:\n\n1. compare each English page independently against the frozen `transcription-ta.md`;\n2. check for omitted clauses, added ideas, reversed meaning, softened/strengthened rhetoric, incorrect subjects/pronouns, mistranslated names/titles, removed repetition, page-boundary omissions and silent normalization;\n3. record every substantive finding in `translation-review.md`;\n4. apply only confirmed corrections to `translation-en.md`;\n5. update metadata/README/HANDOVER with E2 pages checked;\n6. do not begin E3 until E2 has reviewed all 76 pages and all confirmed corrections are consolidated.\n''', h, flags=re.S)
handover.write_text(h, encoding='utf-8')

# Sanity checks.
out = translation.read_text(encoding='utf-8')
for p in range(61, 82):
    assert f'### PDF page {p} — printed page {p-1}' in out
assert out.count('### PDF page ') == 76
assert '**Status:** `first-pass-complete`' in out
assert 'Completed: **PDF 6-81 / printed 5-80 — 76/76 body pages**.' in out
assert 'Vanakkam!!' in out
m = json.loads(metadata.read_text(encoding='utf-8'))['workflow']
assert m['english_translation'] == 'first-pass-complete'
assert m['english_translation_pages_completed'] == 76
assert m['english_translation_through_pdf_page'] == 81
assert m['english_translation_through_printed_page'] == 80
print('Prepared Palli Vazhkkai E1 final block: PDF 61-81 / printed 60-80; E1 first-pass complete 76/76')
