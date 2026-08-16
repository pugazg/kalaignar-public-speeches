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
old_status = '**Status:** `in-progress` — E1 translated through **PDF page 30 / printed page 29** (**25/76 body pages**)  '
new_status = '**Status:** `in-progress` — E1 translated through **PDF page 60 / printed page 59** (**55/76 body pages**)  '
assert old_status in text
text = text.replace(old_status, new_status, 1)
assert '\n## E1 progress\n' in text
text = text.split('\n## E1 progress\n', 1)[0].rstrip() + '\n\n'

batch = r'''### PDF page 31 — printed page 30

—young generation. It is certain that the future will take shape, and can take shape, according to the instruction and knowledge this young generation receives today in school life!

For today's young generation, the world of youth, to gain sound knowledge and advance with principles directed toward living life, school life must become an excellent instrument, a spur, a guide. School instruction must be arranged accordingly. It must teach necessary ideas and must not hesitate to remove ideas that are unnecessary!

For the Tamil to live, for the Tamil people to live, for Tamil Nadu to prosper, Tamil feeling must be instilled in Tamil people, in Tamil children.

Tamil! Tamil! Tamilian! Tamil people, Tamil Nadu, sacred land—the feeling of these, self-respect, and a rising awareness of Tamil heritage must be nourished!

Courage must be taught to reject what is unworthy of the Tamil. The Tamil son of the future, the vibrant young Tamil of today, must be taught to reject blind doctrines that rob him of his honour and make him bow before foolishness!

The Tamil must study Tamil; he must honour the Tamil people—

### PDF page 32 — printed page 31

—protect Tamil Nadu, and live with self-respect. This rising drumbeat must sound as the song of the heart; these must be the great heart-drum of the young Tamil!

One must read books that urge and guide us to abandon customs and practices that do not accord with rational discernment, that drive away knowledge and foster ignorance!

To keep saying “antiquity, antiquity” and build a dam against the new renaissance and new knowledge now blossoming luxuriantly is an improper act!

In the age of the atomic bomb, what are we to gain by reciting the glory of Hanuman? Forgetting, rejecting and casting aside the happiness visible before our eyes, are explanatory texts about a life in another world to be obtained after death still necessary? No!

Think deeply today: what are the things students should not study and learn? What are the things they ought to study and understand?

The ideas impressed during student life, the qualities acquired in school life, are like a nail driven into green wood—

### PDF page 33 — printed page 32

—remaining embedded and continuing to endure until the very end.

At this stage, should students study doctrines of illusion? Are they necessary in this age? In an age of rational discernment in which one must live with self-confidence, are the story of the five Pandavas gambling, the scene of Draupadi being stripped of her garment, and the songs in which the source's `அரிபந்தாமன்` at that moment supplies countless saris from the sky and preserves Lady Draupadi's honour necessary? No!

In those days there was a hunter named Ekalavya. Wishing to learn archery, he went to Drona, who was accomplished in archery, and asked that he too be given training in the bow.

Drona said that he could not give training to a mere hunter who was not of royal lineage, and refused.

Ekalavya returned broken-hearted, then regained courage, made and installed an image resembling Drona, worshipped it every day, practised archery by himself, and grew proficient in many ways. Believing that Drona himself was present and training him, Ekalavya became skilled in every form—

*[Translator/source note: the frozen Tamil has the source-supported unusual name-form `அரிபந்தாமன்`. It is retained rather than silently replaced with a normalized mythological name.]*

### PDF page 34 — printed page 33

—of archery, the Bharata story says.

While matters stood thus, one day Arjuna, one of the Pandavas, came to the forest to hunt with his teacher Drona. There, one of his dogs is said to have defiled the image of Drona that Ekalavya had installed. Seeing this, Ekalavya strung his bow, set the string and shot an arrow, aiming at the dog. That arrow is said to have entered and re-entered the dog's body in many places, pierced through and emerged again and again, and then returned.

The dog howled and ran to Arjuna! Seeing the dog's condition, Arjuna cried out and shed tears. The next moment he became angry; he was astonished. With eagerness and agitation he ran to his guru. He showed him the dog. Drona too felt pity.

Arjuna did not stop there. “Guru, you told me that if one arrow is shot, the art—the archery—by which that single arrow enters many parts of one body, emerges, pierces, and returns had not been taught to anyone other than me. Look here at this dog; what do the wounds on its—

### PDF page 35 — printed page 34

—body show?” he asked.

The guru looked at the dog and saw the many wounds from which blood was flowing. He saw with his own eyes that what the source's `காண்டவன்` said was true. Then he said, “Arjuna, this seems to be some incomprehensible riddle. It is certain and true that I have taught this to no one except you. Let us investigate and find out,” and set off, finally reaching the place where Ekalavya was.

When Ekalavya saw Drona, whom he had regarded as his guru, he ran forward, bowed, greeted him, welcomed him and offered him hospitality.

Looking at Ekalavya standing there in reverence, Drona asked, “Who injured this dog?”

“I am the one who injured the dog,” Ekalavya replied and stood there.

“Where did you learn to shoot an arrow in this manner? Who taught you?” he asked further.

“I learned this method from you, my guru; the one who—

*[Translator/source note: `காண்டவன்` is preserved in the frozen Tamil as an unusual source form. The English renders the surrounding sense without altering that Tamil witness.]*

### PDF page 36 — printed page 35

—taught me this method is you,” Ekalavya answered.

“What? Me? I taught this to you?” Drona asked again, question upon question.

In reply, Ekalavya told how he had gone to Drona and asked to be taught archery; how Drona had refused; how afterward he had regarded him as his guru, placed his image before him, worshipped it, and trained himself in archery before that image until he became proficient. He said that Drona himself was his guru and stood pleading that Drona accept him.

Seeing this, Drona thought. The weapon-skill known only to Arjuna of royal lineage had now become known to Ekalavya, a hunter roaming the forest. He found a way, a device, to remove Arjuna's distress.

“Ekalavya, you are my student. Therefore you must give me a guru's fee. Will you give it?” Drona asked.

Hearing this, Ekalavya's heart filled with joy. “Ah—

### PDF page 37 — printed page 36

—I shall certainly give it, Swami. Ask for whatever you want; I shall give it, without any obstacle,” he said, rejoicing and dancing in delight!

Drona looked at Ekalavya again and asked, “Ekalavya, you say you will give whatever I ask. Will you really do so? Can you do it? Will you give whatever I ask—at once, without refusal?”

“Gurudeva, whatever you ask, without obstruction or delay, I shall give it immediately,” he answered without hesitation, and Ekalavya stood anxiously wondering what he would ask, his eyes fixed on Drona's lips.

“Ekalavya, cut off your right thumb and give it to me as an offering to your guru,” he asked.

Ekalavya did not deliberate at all; he did not even think! He felt no agitation or weariness at the thought that the Gurudeva was asking, as an offering, for the right thumb that was the foundation and an absolute necessity for the very archery for which he had yearned so intensely.

He took his sword and cut off his thumb. “Please accept it—the thumb, the right-hand—

### PDF page 38 — printed page 37

—thumb. Here it is as an offering, Gurudeva,” he said, and gave it away.

This is an incident in the Bharata story! An example of devotion meant to illustrate the philosophy of guru and disciple!

Are a guru possessing such a guru-nature and a disciple who closes his eyes in obedience the lessons, teachings, examples and models needed for this age, for the Tamils of the future? Absolutely not!

In this age there are no deceived Ekalavyas, nor are they needed. Likewise, there are no Dronacharyas possessing such guru-nature; there is no need for them to exist!

Similarly, there is a story in which Tara, wife of the divine preceptor Brihaspati, bewitches Chandra, Brihaspati's disciple, and makes him her lover; this too is mixed into kavya and served up! Are such revolting, obscene Puranas necessary?

Taras who, without regard for his being a disciple, draw Chandra into dalliance; disciples like Chandra who, without considering her the guru's wife, caress and sport with her; and Brihaspati Bhagavans who allow all this to happen and afterward pronounce a curse—

### PDF page 39 — printed page 38

—can hymns about them promote the welfare of the country? Are all these really necessary for students, the people of the future? No!

The Periya Puranam tells of a Nayanar called Iyarpakai Nayanar. The Periya Puranam is regarded as a work of literature and is being taught as a lesson to students!

One day Siva suddenly set out toward the earthly world. Why?

Was it to take charge of the people of the earth and free them from famine, hunger, starvation and other sufferings? Not at all! Then why?

Umaiyorubagan went to the earthly world precisely to take charge of someone—to test and take charge of his devotee named Iyarpakai.

Siva concealed his own form and adopted a disguise. Siva changed himself to look like a devotee of Siva, and in that form went to Iyarpakai's house.

Iyarpakai was a devotee who served Siva.

### PDF page 40 — printed page 39

Whatever a devotee of Siva asked, Iyarpakai gave lavishly without saying that he did not have it. He possessed the state of mind that service rendered to Siva's devotees was service to Siva, sacred service rendered to Siva himself. He had lived accordingly.

Our Lord, the Lord of holy Kailasa, Isan, came to Iyarpakai's house in the form of a devotee of Siva and asked, “Are you the Iyarpakai who gives without saying no? Will you say no and refuse what I ask?”

Seeing the wealthy devotee who loved Siva, Iyarpakai was filled with wonder, welcomed him, and asked with affection overflowing, “What do you want, devotee? I, your servant, shall not fail to give it.”

Looking at Iyarpakai who had asked thus, Ardhanarisvara, who was in the guise of a devotee of Siva, graciously asked, “My son, give me your wife; send her away with me.”

When he said, “Give me the wife you married; send your wedded wife with me at once,” do not imagine that Iyarpakai Nayanar trembled, flared up in anger and said, “What a wicked mind you have! You ask what ought not to be asked; you are going to suffer what ought not to be suffered; coming in the form of one who loves Siva, you seek a slender-waisted woman—

### PDF page 41 — printed page 40

—coming in the guise of a devotee, you boldly ask that another man's wife be sent with you,” speaking sparks of fire and crossing every limit of anger. Do not imagine any such thing!

Iyarpakai did not become angry with the devotee of Siva who asked, “I want your wife; you must send your wife with me.” Not only did he not become angry; Iyarpakai Nayanar folded his hands and bowed to that devotee and sent his wife along with him.

Neighbours, relatives and others who saw and heard of this improper act, this unworthy method, this ruinous conduct surrounded them and tried to stop it.

“Whoever may stop me, what does it matter? Serving a devotee of Siva is service to Siva, service that gives satisfaction to Siva. I will not fail to give whatever the devotee begs, asks or desires. Do not stop me,” he said, refusing them, and Iyarpakai Nayanar sent his wife—the mistress of his household, the lamp of his home—with the exalted holy man who had come along the road!

The townspeople cried, “Can this outrage be tolerated?” and rose up. The relatives hurled hot words: “A self-respectless—

### PDF page 42 — printed page 41

—act! We must not let that fraudulent holy man get away with it,” and set off in the direction taken by the merciful sacred servant (!).

With Iyarpakai's wife accompanying him, Neelakandan, who had drunk the Halahala poison and had come in the form of a servant of Hara, was walking away from Iyarpakai's home!

The people who had set out saying, “We will certainly stop this shameless act of sending one's wife with another man,” blocked the devotee of Siva on the road and spoke to him with abuse and condemnation.

Hearing this news, Iyarpakai trembled, sprang up, ran there, rebuked and attacked his kinsmen, relatives and the townspeople who had offered advice, and tried to send the devotee of Maheswaran, who was travelling with his wife, onward in safety.

The whole town was thrown into turmoil as the two sides hurled burning words and came to blows, the conflict growing ever more intense!

Suddenly the devotee of Siva was nowhere to be seen. A light appeared in the sky, and in it Siva Peruman appeared and said, “Iyarpakai, we rejoiced on seeing your service to Siva; our heart was cooled. We tested you, examined your devotion, and in order to grant you—

### PDF page 43 — printed page 42

—greatness, in order to make the world understand the greatness of your devotion, we performed this divine play,” and, speaking words of blessing, praised Iyarpakai and disappeared.

This is the history of Iyarpakai Nayanar, one of the sixty-three Nayanmars described in the Periya Puranam! A holy Purana!

What devotion! What service—service to Siva! What generosity, to donate one's wedded wife to someone who comes asking! Is this what is needed today?

The divine play of an all-powerful God; the degrading method of testing a devotee; asking for the wife of the household as a gift, obtaining her and taking her away—is that good? Is it just? Is that proper? Tell me!

Should such blind devotional intoxication, such a loss of self-awareness, such a self-respectless course, such an irrational quality, be studied and learned? Should these things be placed in lessons? Is the idea and arrangement that this path is necessary and essential for the present generation? Why should such degrading qualities be injected into the hearts of the young? And that too, in God's name—obscenity in educational institutions, the halls of knowledge, in school life! Is all this not an unnecessary sacred service?

### PDF page 44 — printed page 43

Even if, merely for the sake of argument, we verbally agree and consider that books about the Lord, God and Maheswaran are necessary, should an obscene Lord, mindless blind gods, and a demented Maheswaran who drags away another man's wife be made lessons for students?

Devotion! Faith; the Lord's Purana; the inherited fearful mentality that says belief brings moksha and disbelief brings hell; the belief that a book earns merit for one's fate after death—without thought, without weighing what is seen, praising and glorifying conduct opposed to the age and to reason, improper and unworthy doctrines, and reading, singing, dancing and rejoicing over intolerable outrages as the glory of divine incarnation and sacred plays: must school life continue, through instruction in Puranas and epics, the work of trapping the future generation too in this “devotional intoxication”?

What is needed is the concept that the Lord, God, lies beyond worldly knowledge: an unseen force! An entity that cannot be seen! Something beyond human power! Nature!

Puranas that, within school life itself, instil religious sectarian passions—

### PDF page 45 — printed page 44

—religious doctrines that contradict one another; lessons that inject knowledge and at the same time ignorance; instruction that teaches science and at the same time strange glories of divine incarnations, creating for the student an incomprehensible, confused environment and giving strength to philosophies that clash against one another—this strange, perverse curriculum, a scheme opposed to rational discernment: is it still necessary? Even in this age?

In science class the student studies how rain falls. With many instruments, before his very eyes, he studies the causes by which rain appears and the conditions under which rain falls.

The water on earth, he learns in general-knowledge class, changes into vapour under the heat of the sun, mixes with the air and rises, becoming clouds in the sky. When the clouds meet cold air, or strike cold mountain peaks, they cool, turn into water, and fall as rain!

Next, in the Puranas and epics, he is taught that Varuna Bhagavan is the lord of rain—

### PDF page 46 — printed page 45

—and Indra is the lord of thunder, and that rain falls only when these gods are praised and worshipped. What becomes of the knowledge and clarity of the student who studies this in another class?

Devotional books and holy Puranas, said to have blossomed from Bhagavan's sacred mouth, heard by great sages and supreme ascetics and passed down from generation to generation as Veda, epic and Purana, now appearing also as textbooks—should the student accept the reason they give for rain under the stamped label “word of the Supreme,” or should he believe what research in the world of knowledge, common knowledge and science states decisively and systematically? What is he to believe, accept and take? Will his mind not be confused? Will he not become dispirited?

Science is clear! It contains fitting truths. But if he believes it, will he not become a “wretch” who refuses to believe the holy Purana!

If he believes the Purana and follows the Puranic way, he will not acquire common knowledge!

Ruined either way! Distress! An unclear environment—in childhood, in school life!

### PDF page 47 — printed page 46

A concept, a contradictory concept and doctrine, concerning the same matter, the same natural event and process! How does rain fall? What a spectacle! What perversity! What a strange contradiction! A spectacle that gives pain!

On one side the student observes Varuna prayers still being conducted, Varuna sacrifices performed, and enormous sums spent on Varuna japas to make rain fall and make dry land prosper through the grace of Varuna Bhagavan.

At the same time, the student reads news of Russia and the reality said to be occurring there: people go among the clouds in aeroplanes and, through scientific instruments, draw the clouds in and make rain fall in their country!

Varuna japa—for rain! Did the rain come? Can it be stated with certainty that Varuna japa was performed, rain fell, and the country gained good prosperity? Is that not impossible to establish?

In our own day, do we not see and hear of clouds being drawn in with scientific instruments and made to rain in Russia?

Of the two paths mentioned above, which—

### PDF page 48 — printed page 47

—is wanted today? Which do the people need? Give your judgement!

The scientific path from which the source's `மனிதனி அறிவு கண்டு` and benefit were obtained—or the Varuna japa performed by Vedic men, handed down through generations of great men (!)?

What knowledge is the knowledge needed by the people, especially by school students? Of these two, which must be acquired in school life? Common knowledge or recitation of the Puranas? Tell me which is wanted.

Practical method? Or the penance-method of Narada's age? Which is wanted, which is needed today—for us, for our good life? Should we not think?

The useful path of rational discernment, or divine tales speaking of life in the other world? The quality of discriminating reason, or devotion that bows as soon as it hears “the word of Bhagavan, the saying of Parasara”? Which is needed, which is clarity, which is good, which is right? Tell me!

Science? Veda? Knowledge? Capacity? Or the old refrain, “the path left by his grace—who can conquer fate?” Which is the way, which is right, which is needed today?

*[Translator/source note: the frozen Tamil phrase `மனிதனி அறிவு கண்டு` is a source-supported unusual form. It is kept visible rather than silently reconstructed.]*

### PDF page 49 — printed page 48

Science—common knowledge—worldly knowledge holds first place in human life today!

Today science has become inseparably mixed into every sphere of human life!

Science serves human life as an unfading light, a garden of boundless joy, a sky cleared of darkness, a companion and friend that reduces labour and enlarges awareness!

Science appears and helps the human being in everything it touches!

The books needed for human study, the paper on which books are printed, are signs of scientific development! The printing press that prints them—reducing human labour, reducing the ceaseless work of writing on palm-leaf manuscripts—is surely a discovery of scientific development that has rendered a great service!

The carts and vehicles in which people travel, the running train, the driven motorcar, the flying aeroplane, the talking cinema, the gramophone that plays music, the radio that sings, the television that lets us see, the varieties of clocks that announce the time—

### PDF page 50 — printed page 49

—how many, how very many! Boundless instruments that science has given to humankind!

Electric light—electric fan, electric motor, electric train, electric stove, electric bell, electric power, kinds of electrical medicine, electric-shock method, electric ladder, electric pusher, electric lift, electric fitting, electrical safety system! Good heavens! Electricity, electricity, electricity—has not the human being today become electrified through and through!

Electricity—a force of nature! From the natural force of waterfalls, and beyond that by damming and storing water and generating electrical power, people use electricity in so many ways and forms: as an ally reducing their labour, as illumination suited to recreation, as a useful lamp, as an electric lift carrying them upward, as a servant driving machines. How did this knowledge—the knowledge of putting a natural force to use—arise?

Human beings began to think! They thought! They looked at the things around them and thought!

### PDF page 51 — printed page 50

Some human beings did not fail to observe and think even about the smallest movements. The noble results of such thinkers spread their fragrance through our lives today!

Fragrance! A useful fragrance! A fruitful fragrance blows throughout the world!

A drop of thought from someone, the result of research in which someone saw something and directed his mind toward it—scientific advancement makes life more convenient and is used throughout the world!

Work that benefits the common good of the world; the work of common knowledge! The work of rational discernment! Work that enables a human being to live as a human being! Work that gives liberation from brutish labour! Worldly knowledge, scientific knowledge—a great auxiliary army for increasing production!

An event happens at one end of the world! What rare instruments exist today for it to become known and spread throughout the world, across the whole world, that very day!

What of newspapers that capture and show the world's daily events? What of radio?

### PDF page 52 — printed page 51

An urgent event, urgent news? Send a telegram! What a marvel! Yet it happens; we see it happening in practice!

What easy, practicable methods are carried out by the “money gardens” called “banks” (Bank)?

Progress! Not merely in a few particular fields! In every sphere and every angle of life in the world, progress—progress of many kinds—has taken place and continues to take place!

At such a time, on such a path of progress, in the scientific age through which the world is moving, must we remain mere Vedantists, noble devotees singing of Ulagalandhan, servants rejoicing in singing the sacred-servant Purana of the beloved of Sivakami?

At one time, ideas and conceptions about the world and about the shape of the world were of one kind!

There was a time when people thought, “The world is flat! The world has the shape of a long rectangle!” But today?

### PDF page 53 — printed page 52

That the world is round is established fact—not merely established fact, but a conclusion reached by travelling around the world and seeing it!

Not only ordinary people proclaimed that the world was flat; the Puranas themselves proclaimed it! Even the gods of gods said so. An asura called Iranniyatchakan is said to have rolled the earth up like a mat, run into the sea and hidden there. Because of this the whole world disappeared.

The gods and sages are said to have praised the dark-hued protector, Tirumal, and begged him to destroy that evil being and bring the earth back again!

Maha Vishnu listened to the request of the sages and gods and gave them assurance: “We shall do what is required; fear not.”

The gods and sages plunged into a sea of joy on hearing Malon's words of reassurance!

Maha Vishnu at once took the Varaha incarnation (the form of a pig), plunged into the sea, searched for Iranniyatchakan, fought him, destroyed that demon, and the entire world—

### PDF page 54 — printed page 53

—was rescued from the deep sea. He brought out again from the sea the broad earth that the demon had rolled up like a mat, and spread out the mat—the earth that had been rolled like a mat—the world—once again!

The hidden world came out again! The rolled-up world was spread out again by Parandhaman!

This is Purana, a divine tale! Not a yarn spun by an ordinary person, but a devotional story sung by the tradition of devotion and said to grant liberation!

Varaha is one of the ten incarnations taken by Parandhaman! Is the truth accepted by the gods, the sages, and Maha Vishnu, one of the Trinity, that the world is flat and mat-like?

That divine word has today become a worn-out word before science! Before the clarity of human knowledge! It has been demonstrated that the world was, and is, round!

This change, this change of idea, this change visible to the eye, this change of idea taught by the speed of time, this change that cannot be ignored and has become joined to life—

### PDF page 55 — printed page 54

—is today made to collide with an idea that is finished, shown to be wrong and decisively settled, with an idea whose time has passed—in the country, and not only in the country but in life itself!

This collision, this work of making antiquity and modernity clash, can only ruin the school student's rational discernment and bring it into a state of confusion. It does so!

Solar eclipses and lunar eclipses occur! How?

In science class we study that these eclipses occur according to changes arising in the course of the earth rotating on itself while going around the sun, and according to changes arising when the moon goes around the earth.

Old texts say that solar and lunar eclipses occur when the serpents called Rahu and Ketu swallow the sun or the moon! And this too must be studied!

Two different causes for a single event. One is the conclusion of scientific research; the other—

### PDF page 56 — printed page 55

—is the statement of Veda, Agama and Purana! Should the student not gain clarity as to which of these is true and which is needed?

If the student is made to study the Purana and, at the same time, the modern idea that shows the Puranic idea to be false, and both are made to take up residence in young hearts, what becomes of the young heart, of the young person's clarity?

On one side we continue praising the claim that blind doctrines made rotten by time and of no practical use must not be abandoned; at the same time, we live using in everyday life the instruments of the new-age renaissance supplied by rapidly growing common knowledge. What a strange life!

A strange life! Science and the Vedas, which contain ideas contradictory and directly opposed to science, are being fostered together!

Through science we have obtained the conveniences necessary for life and gained change and renaissance outwardly, in our external form. Yet at the same time, our “inner life” remains the meaningless life of ignorance of that old age—

### PDF page 57 — printed page 56

—does it not! Must this condition, this condition without clarity, not be changed?

Study! It must not become mere study, empty study!

We studied; we learned many arts! We gained rational discernment! It helped remove want! It drove away cruelty; spread equality! Established fraternity! Clarity of thought arose! It helped remove and drive away contradictions of thought, blind customs and barbarous qualities—education in school life must be useful education, study that teaches us to discriminate and gives knowledge! It is needed! Very, very much needed! Needed immediately!

History! World history! The histories of every country in the world are taught in school life!

We study the histories of many countries! We have studied how people lived in those countries, how standards of life developed, how uncivilized life changed, gaining clarity day by day, thought maturing, and civilized life coming to be lived!

### PDF page 58 — printed page 57

We study the rise of many empires and the ways in which they were destroyed! We learn at what times renaissance and changes of mind occurred in those countries!

While studying all this, we also study the history of our own country!

Is our history, the history of our Tamil Nadu, properly presented? We see that the histories of our ancestors—the Chera, Chola and Pandya—are finished within only a few pages of the history books!

The history of Parantakan who conquered Burma, the Tamil king who conquered Eelam, and the Tamil kings who engraved the Tamil flag on the Himalayas is not set out broadly and clearly!

Is there any account in history of Cheran Senguttuvan, who made the Aryans Kanaka and Vijaya, who had spoken disparagingly of the Tamil, carry a stone on their heads?

Is there a small note, a word, a word of praise in history for the Tirukkural, acclaimed as the universal scripture of the world? Is there? Is there?

The Bhagavad Gita and the Ramayana and Bharata epics—

### PDF page 59 — printed page 58

—find a place in books of history, but there is no place for the Tirukkural!

Tamil! Is this your condition, the condition of your history? Is this not a state that makes Tamil weep—the condition in which the history of the Tamil people has disappeared!

Tamil history, the history of Tamil, must be written properly. The fragrance of Tamil hidden by those endowed with the source's `சுதுமதி`, and the history of the Tamils, must be written; the valour, courage and standard of life of the Tamil must be explained properly and clearly!

What is the reason that the valour and civilization of the Tamil—who travelled around the whole world, conducted trade at an exalted level, crossed the seas and saw many ships—have today disappeared, have been hidden?

History, the history of Tamil Nadu, must not begin on the banks of the Ganges; it must begin on the banks of the Cauvery!

The history of Gangaikonda Cholan; the history of Senguttuvan, who made Kanaka and Vijaya carry a stone upon their heads; Ilango's writing; the greatness of the Tirukkural; the age of Kulothunga; the victories of Rajarajendran—

*[Translator/source note: the frozen Tamil phrase `சுதுமதி படைத்தோரால்` is source-supported but semantically unusual. It is kept visible rather than silently reconstructed.]*

### PDF page 60 — printed page 59

—all these must be written in the history of Tamil Nadu.

A way must be made for the Tamil to study and know the history of Tamil Nadu.

One must study the antiquity of Tamil and the greatness of Tamil; one must honour Tamil, protect Tamil, and the Tamil must live as a Tamil?

The Tamil people—the Tamil of the future—must be enabled to become, in the source's forms, a `தமிழறிந்த தமிழனமாக`, a `தமிழின வரலாறு தெரிந்த தமிழனமாக`, a garden of Tamil, and to make the sacred Tamil land live as a distinct sacred land. What is necessary for this must be done.

In school life, the histories of noble people who reformed the world must be studied. Many biographies of noble people must be taught in schools.

The age when humankind wandered uncivilized as savages in forests, uplands and mountain caves changed; with the growth of the source's `மதனின் அறிவு`, people acquired religious, political and economic knowledge, began to live and advanced—the course of development—

*[Translator/source note: the frozen Tamil retains the unusual forms `தமிழனமாக` and `மதனின் அறிவு`. They are not silently normalized; the translation keeps them visible where a confident literal reconstruction is not supported.]*

## E1 progress

- Completed: **PDF 6-60 / printed 5-59 — 55/76 pages**.
- Independent E2 fidelity review has **not** begun; per workflow it remains blocked until the full E1 body translation is complete.
- Remaining E1 scope: **PDF 61-81 / printed 60-80 — 21 pages**.
'''
text += batch
translation.write_text(text, encoding='utf-8')

# --- metadata.json ---
data = json.loads(metadata.read_text(encoding='utf-8'))
wf = data['workflow']
assert wf['english_translation_pages_completed'] == 25
assert wf['english_translation_through_pdf_page'] == 30
assert wf['english_translation_through_printed_page'] == 29
wf['english_translation'] = 'in-progress'
wf['english_translation_pages_completed'] = 55
wf['english_translation_through_pdf_page'] = 60
wf['english_translation_through_printed_page'] = 59
metadata.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# --- README.md ---
r = readme.read_text(encoding='utf-8')
r = r.replace('| English translation (E1) | **In progress — 25/76 body pages; through PDF 30 / printed 29** |',
              '| English translation (E1) | **In progress — 55/76 body pages; through PDF 60 / printed 59** |', 1)
assert '## English translation progress\n' in r and '## Exact next activity\n' in r
new_progress = '''## English translation progress

E1 is being translated only from the frozen Tamil layer. `translation-en.md` now contains **PDF 6-60 / printed pages 5-59 — 55/76 pages**.

The present activity translated **PDF 31-60 / printed 30-59** as one continuous source-faithful block. It continues the future-generation argument, carries the long Ekalavya and Iyarpakai Nayanar critiques, contrasts Puranic and scientific explanations of rain and eclipses, develops the case for science and worldly knowledge, and turns to the representation of Tamil history in school curricula.

All source page boundaries remain explicit. Difficult frozen readings are not silently regularized; translator/source notes identify forms such as `அரிபந்தாமன்`, `காண்டவன்`, `மனிதனி அறிவு கண்டு`, `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, and `மதனின் அறிவு` where a confident reconstruction is not supported by the frozen witness.

No E2 fidelity review has begun; that gate remains blocked until the entire E1 body is translated.

'''
r = re.sub(r'## English translation progress\n.*?(?=## Exact next activity\n)', new_progress, r, flags=re.S)
r = re.sub(r'## Exact next activity\n\n.*?(?=\n## Editorial rule)',
           '## Exact next activity\n\nComplete the remaining **E1 English translation for PDF 61-81 / printed pages 60-80** from the frozen `transcription-ta.md`. Continue the unfinished PDF 60 sentence faithfully onto PDF 61, preserve all page correspondence and source difficulty, and do not begin E2 until E1 reaches 76/76 pages.\n',
           r, flags=re.S)
readme.write_text(r, encoding='utf-8')

# --- HANDOVER.md ---
h = handover.read_text(encoding='utf-8')
h = h.replace('Completed E1 scope: **PDF 6-30 / printed 5-29 — 25/76 body pages**.',
              'Completed E1 scope: **PDF 6-60 / printed 5-59 — 55/76 body pages**.', 1)
if '- Batch 5: PDF 26-30 / printed 25-29' in h:
    h = h.replace('- Batch 5: PDF 26-30 / printed 25-29',
                  '- Batch 5: PDF 26-30 / printed 25-29\n- Extended Batch 6: PDF 31-60 / printed 30-59', 1)
insert = '''
## E1 Extended Batch 6 — PDF 31-60 / printed 30-59

Completed and committed as one 30-page translation activity at the repository owner's request.

Important translation decisions:

- PDF 30→31 remains an explicit continuation: “the present-day—” / “—young generation”.
- The repeated Tamil/Tamilian/Tamil Nadu/self-respect rhetoric on PDF 31-32 is preserved rather than compressed.
- The Ekalavya narrative on PDF 33-38 is translated paragraph-by-paragraph, including the guru-dakshina demand for the right thumb and the source's polemical conclusion. The unusual frozen forms `அரிபந்தாமன்` and `காண்டவன்` are not normalized.
- The Iyarpakai Nayanar narrative on PDF 39-43, including its sexual/marital content and the author's sharp polemical criticism, is translated without sanitizing or adding external explanation.
- PDF 44-48 preserves the source's contrast between Puranic/religious teaching and science, including rain, Varuna worship and the Russia cloud/rain example. The unusual `மனிதனி அறிவு கண்டு` is kept visible in a translator/source note.
- PDF 49-56 preserves the long catalogue of scientific and electrical technologies, the flat-earth/Varaha narrative, and the competing explanations of eclipses. The translation reports these as source claims and does not independently validate or modernize them.
- PDF 57-60 preserves the argument for useful education and the critique of history curricula, including the source's claims about Tamil rulers, Tirukkural, Ganges/Cauvery framing and Tamil history.
- The frozen source-supported forms `சுதுமதி படைத்தோரால்`, `தமிழனமாக`, and `மதனின் அறிவு` are explicitly flagged rather than silently repaired.
- PDF 60 ends mid-sentence at `வளர்ச்சி`; the English likewise ends “the course of development—” for continuation on PDF 61.

'''
assert '\n## Source-fidelity safeguards carried into English\n' in h
h = h.replace('\n## Source-fidelity safeguards carried into English\n', '\n' + insert + '## Source-fidelity safeguards carried into English\n', 1)
h = re.sub(r'## Exact next activity\n\n.*?(?=\n## Safeguards)',
           '## Exact next activity\n\nComplete the remaining **E1 English translation for PDF pages 61-81 / printed pages 60-80** from `transcription-ta.md`. Continue the unfinished PDF 60 sentence onto PDF 61, retain every PDF/printed-page heading and paragraph sequence, preserve rhetoric and difficult frozen readings, and keep E2 blocked until the full E1 body reaches 76/76 pages.\n',
           h, flags=re.S)
handover.write_text(h, encoding='utf-8')

# Sanity checks
out = translation.read_text(encoding='utf-8')
for p in range(31, 61):
    assert f'### PDF page {p} — printed page {p-1}' in out
assert '55/76 body pages' in out.splitlines()[2]
assert 'Remaining E1 scope: **PDF 61-81 / printed 60-80 — 21 pages**.' in out
print('Prepared Palli Vazhkkai E1: PDF 31-60 / printed 30-59')
