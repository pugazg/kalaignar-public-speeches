# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake and machine-aided navigation complete. Tamil T1 first pass is provisionally complete through the true decoded end at `00:26:22.080`. Direct-listening audit has not started.**

The controlling MP3 is authoritative. Machine transcripts are secondary navigation evidence only and must not be promoted to verified Tamil without direct listening.

## Source identity

- filename: `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`;
- official URL: `https://tamildigitallibrary.in/kalaignar/audio/06.Kalavaivannar%20N.S.Krishnnan%20Ninavul%20Naal%20Vizha%20Vil%20Kaligar%20Speech.mp3`;
- SHA-256: `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`;
- file size: `25,313,377` bytes;
- decoded duration: `1582.080` seconds / `00:26:22.080`;
- remote identity: verified by exact checksum and byte-size reproduction;
- binary committed: No.

## Technical and boundary state

- MP3, stereo, 44.1 kHz, approximately 128 kb/s;
- right channel approximately 6 dB stronger than left;
- original stereo MP3 remains the controlling witness;
- spoken lead-in `00:00–approximately 00:14` remains unverified;
- main speech begins approximately `00:41.9`;
- final activity continues to approximately `00:26:21.4`;
- machine navigation proposes a grammatically complete ending followed by `நன்றி, வணக்கம்`;
- final 60 seconds and final 30 seconds still require separate direct replay;
- `recording_truncated` remains unresolved.

## Machine evidence rules

Two whole-file passes were rejected after repetition drift/hallucination. Useful navigation instead uses the stronger right channel, independent short chunks, `condition_on_previous_text=false`, and large-v3-turbo. Machine evidence remains navigation only.

The standard printed wording of any quoted source, including Tirukkural, must not be used to normalize the speech silently. The Audio 06 T1 currently preserves the machine-supported spoken candidate `எச்சத்தால்`; T2 direct listening must decide the actual recording.

## T2 opening preparation — no direct-listening pass claimed

The original Audio 06 conversation attachment was re-resolved before beginning the T2 opening gate. Its filename and byte size match the controlling source already recorded in this archive.

The currently available attachment-reading interface exposes a machine-produced transcript rather than an audible replay. Under `AUDIO_SPEECH_PROCESSING_GUIDE.md`, textual/ASR comparison **must not** be called direct listening. Therefore this preparation does **not** increment T2 checked or passed counters and does not promote any wording to verified Tamil.

### Signal/boundary preparation

Direct signal analysis of the controlling MP3 gives the following useful opening gates:

- at a `-25 dB` silence threshold, the announcer/lead-in activity gives way to a quiet interval beginning at approximately `00:13.966` and ending at approximately `00:41.641`;
- at a stricter `-30 dB` threshold, a strong silence interval runs from approximately `00:13.982` to `00:29.653`, followed by low-level ambience before the main speech;
- independent opening speech-navigation evidence places Kalaignar's first main-speech activity at approximately `00:41.88`.

These are technical/navigation boundaries, not T2 auditory verification.

### Lead-in candidate evidence

Multiple machine views converge on a short announcer lead-in referring to:

- `கலைவாணர்`;
- Chennai `கலைவாணர் அரங்கம்`;
- `கலைவாணர் நகைச்சுவை`;
- `டாக்டர் கலைஞர் அவர்கள்`;
- an announcement equivalent to `இப்போது உரையாற்றுவார்`.

The first few words and exact grammatical joins remain unstable across machine views. No lead-in wording has been inserted into the canonical transcript from this evidence alone.

### Main-speech opening candidate

The attachment-level machine transcript and the prior independent right-channel navigation both support the existing T1 opening beginning around `00:41.88` with the same broad sentence:

`கலைவாணருடைய விழாவிலே நகைச்சுவைக்குப் பஞ்சமிருக்கக் கூடாது ...`

The current T1 version remains the stronger provisional reading. Competing machine output introduces obvious distortions in words such as `நகைச்சுவை`, `மிகுந்த`, `சிரிப்பொலி`, `படையல்` and the closing `மிகையாகாது`; none of those competing distortions has been adopted.

### Gate result

- direct-listening segments checked: **0**;
- direct-listening segments passed: **0**;
- opening verified: **No**;
- canonical Tamil changes from this preparation: **None**;
- next required action remains a true audible replay from `00:00`.

## T2 textual precheck coverage

Twenty-four preparatory T2 records now exist:

- `t2-batches/batch-01-00-00-01-10-precheck.md` — lead-in, opening boundary and first main-speech sentence;
- `t2-batches/batch-02-01-10-02-34-precheck.md` — Chinna Annamalai anecdote and humorous conclusion.
- `t2-batches/batch-03-02-34-03-22-precheck.md` — Kannadasan–Sivaji recollection and the unresolved humorous transition.
- `t2-batches/batch-04-03-22-04-00-precheck.md` — opposition-period hotel-room setup and Kannadasan political-separation context.
- `t2-batches/batch-05-04-00-05-14-precheck.md` — crossed-telephone setup through the first unresolved exchange.
- `t2-batches/batch-06-05-14-06-00-precheck.md` — crossed-line conversation and the reply about Kannadasan's Tamil attacks.
- `t2-batches/batch-07-06-00-06-43-precheck.md` — Tamil/art transforming hostility, Anna's use of art, and the Kalaivanar reference before S. S. Rajendran.
- `t2-batches/batch-08-06-43-07-12-precheck.md` — Rajendran reference and Kalaivanar's early progressive / Self-Respect ideas.
- `t2-batches/batch-09-07-12-08-00-precheck.md` — Ilangovan, Kannagi adaptation, *Dravida Nadu* article/title and opening of Anna's assessment.
- `t2-batches/batch-10-08-00-08-38-precheck.md` — Anna's criticism of Ilangovan's *Silappathikaram* treatment.
- `t2-batches/batch-11-08-38-09-25-precheck.md` — `இஞ்சிப்பத்தர்` gold/brass deception and Anna's interpretation of Kalaivanar's performance.
- `t2-batches/batch-12-09-25-09-50-precheck.md` — Anna's `வஞ்சிப்பத்தர் / இஞ்சிப்பத்தர்` conclusion and medicine-with-honey transition.
- `t2-batches/batch-13-09-50-10-18-precheck.md` — K. R. Ramasamy, `நடிகவேள்`, reform-theatre brothers and the Rajendran boundary.
- `t2-batches/batch-14-10-18-10-48-precheck.md` — Rajendran/Narayanasamy boundary, Sivaji `சிம்மக்குரல்`, and the Periyar/Anna stage-screen statement.
- `t2-batches/batch-15-10-48-11-20-precheck.md` — Anna-call rhetoric, immediate artist response, and the professional-career fear contrast.
- `t2-batches/batch-16-11-20-12-00-precheck.md` — memories/assembled-artists transition, Kannadasan changed-position wording, and opening Krishna wordplay.
- `t2-batches/batch-17-12-00-12-22-precheck.md` — Kannadasan Krishna recommendation, central Krishna-joke conflict, temple-house remark and house-correction boundary.
- `t2-batches/batch-18-12-22-12-49-precheck.md` — house-purchase correction and mock-newspaper sequence, including corrupted political-status, place-name and mock-headline forms.
- `t2-batches/batch-19-12-49-13-15-precheck.md` — negative-evidence recovery of the machine-collapse interval before the retired postal-official house-sale narrative.
- `t2-batches/batch-20-13-15-14-00-precheck.md` — retired senior official / house sale, locality-agraharam objections, and the meeting sequence before the `14:00` remark.
- `t2-batches/batch-21-14-00-14-15-precheck.md` — `பேரைப் / தேரைப்` remark conflict, agraharam residents' agreement and the twenty-years-earlier house-purchase conclusion.
- `t2-batches/batch-22-14-15-14-59-precheck.md` — rationale for the house anecdote, changed ideological positions versus the continuing principle, gratitude to earlier workers and the Sivaji transition.
- `t2-batches/batch-23-14-59-15-35-precheck.md` — Sivaji stage-work recollection, humorous reversal of who acted with whom, and the unpaid-performance statement.
- `t2-batches/batch-24-15-35-16-00-precheck.md` — relief/election-fund theatre work, unstable co-actor list, and the transition into the art-and-politics reflection.

Batch 2 exposes a fuller machine-supported narrative skeleton for the previously withheld `01:16–02:12` span, including the claim of telling something unknown to others, questioning whether the anecdote was later stage invention, an uncertainly transcribed conference/event reference, the possibility of asking Kalaivanar whether it was true, and a mock-boasting sequence about private knowledge/closeness. Proper nouns, honorific verb forms, the conference name and several examples remain too noisy for canonical promotion.

Batch 3 strongly supports the names Kannadasan and Sivaji Ganesan, their closeness to Kalaivanar, and the quotation ending in substance with `நான் காதலிக்கின்ற ஒரே கவிஞர்`. The attachment-level ASR corrupts the beginning of the quotation and the following humorous competition-in-affection sentence; therefore the current T1 candidate `என்னை வைதாலும் திட்டினாலும்...` remains provisional and the transition remains unresolved pending audible replay.

Batch 4 strongly supports the opposition-period setting, the speaker writing film dialogue alone while staying in a Chennai hotel, `காலை பதினொரு மணி இருக்கும்`, Kannadasan separating from Anna with another friend, starting another party, and attacking the speaker politically. The exact friend modifier and `வேகமாக/மிக வேகமாக` remain auditory checkpoints; no canonical change was made.

Batch 5 strongly supports the crossed-telephone narrative but leaves several lexical choices for replay: `மேகலா பட நிறுவனத்திலே` versus a machine `நிர்வாகத்திலே` reading, current `இன்னொரு பையனுடைய குரல்` versus machine `இன்னொரு பழகிய குரல்`, the full telephone-interference sentence, the Mekala contact/manager wording, and the exact clause describing two calls becoming connected. No canonical change was made.

Batch 6 supports the Kannadasan identification, the approximately ten-to-fifteen-minute telephone conversation, the newspaper-attacks question and the speaker's reply that he enjoyed the attacks because they were expressed in Tamil, especially sweet Tamil. It deliberately leaves `யாரய்யா/யாரையா`, `போன் செய்கிறேன்/செய்திருந்தேன்`, `பத்திரிகையிலே/பத்திரிகைகளில்`, `நன்றாகத் திட்டுகிறீர்` versus corrupted `நன்றாகச் சிந்திக்கிறேன்`, and `தமிழிலே` versus corrupted `தமிழுலகை` for true replay. No canonical change was made.

Batch 7 strongly supports the argument that Tamil and Tamil art can transform hostility, that Anna used art to convey good ideas, and that Kalaivanar N. S. Krishnan was an important artistic force behind that work. Exact replay must settle `மாற்றியமைக்க/மாற்றி அமைக்க`, `கலை மூலமாக/மூலமாகவும்`, the people/ideas phrase, honorific morphology, current `பக்கபலமாக இருந்த` versus machine-supported `தூண்டுகோலாக இருந்த`, and especially the badly corrupted venue/display phrase before Kalaivanar's name. No canonical change was made.

Batch 8 strongly supports the Rajendran–Anna–Kalaivanar comparison and the sequence of revolutionary, Self-Respect and Tamil-society ideas. Exact replay must settle current `லட்சிய நடிகர் எஸ். எஸ். ராஜேந்திரன்` versus machine `தேசிய நடிகர் ராஜேந்திரன்`, whether `அல்லது` occurs between film and theatre, `எடுத்தாளுவதற்கு/எடுத்து ஆள்வதற்கு`, full `என். எஸ். கிருஷ்ணன்` versus `என். எஸ். கே.`, the short indistinct clause before the final verb, and `எடுத்துச் சொன்னார்/எடுத்துச் சொன்னார்கள்`. No canonical change was made.

Batch 9 strongly supports the Ilangovan/Kannagi/*Dravida Nadu* sequence and supplies useful machine candidates, including `தனிகாசலம் என்கின்ற இளங்கோவன்`, machine `இஞ்சிப் பத்தரை மேல்`, and the stable later praise `வசன நடையில் ஒரு புதிய சகாப்தத்தை இளங்கோவன் உருவாக்கியிருக்கிறார்`. Exact replay must settle the personal-name expansion, `போற்றுதலுக்கும் புகழுதலுக்கும்` wording, `ஆக்கினாரே/ஆக்கினார்கள்`, whether the publication relation is `நடத்திய` or machine `எழுதிய`, the exact article-title segmentation, the article-opening setup, and two badly corrupted praise phrases resembling `பத்திவாய்ந்த எழுத்தாளர்` and `அவருடைய எழுதுவோலி தமிழ் நர்த்தனம் ஆடுகிறது`. No canonical change was made.

Batch 10 exposes major ASR-versus-T1 conflicts in Anna's criticism of Ilangovan's *Silappathikaram* treatment. Machine evidence supports a candidate `கர்ணபரம்பரைக் கதையைப் போலவே`, but conflicts with the current provisional rhetorical question (`இலக்கிய வளமல்லவா?` versus machine `ஒரு இலட்சியவாதமா?`), the Chera–Chola–Pandya clause, the literary noun represented as `பனுவலல்லவா?`, and the corrupted phrase resembling `புராண நெறு கொடுத்து` before `வீணாக்கியிருக்க வேண்டுமா?`. No canonical change was made.

Batch 11 strongly supports the `இஞ்சிப்பத்தர்` role, the gold/brass substitution scheme, and the interpretation that Kalaivanar's acting exposes Ilangovan's treatment of *Silappathikaram*. Exact replay must settle `இஞ்சிப்பத்தராக/இஞ்சிப் பத்தராக`, full `என். எஸ். கிருஷ்ணன்` versus `என்.எஸ்.கே.`, the clause order around gold, brass and theft, `ஒருவனாக/ஒருவராக`, current `பித்தளைக்கு நிறம் ஏற்றி` versus machine `பித்தளைக்கு நிகரேற்றி`, and concluding honorific/name morphology. No canonical change was made.

Batch 12 strongly supports the two-part transition from Anna's `வஞ்சிப்பத்தர் / இஞ்சிப்பத்தர்` conclusion to Kalaivanar's ability to convey political, economic and social ideas like medicine mixed with honey. Exact replay must settle `ஆக/ஆகவே`, current `வஞ்சிப்பத்தரை` and `இஞ்சிப்பத்தரே மேல்` versus machine-segmented `வஞ்சிப் பட்டறையை / இஞ்சிப் பட்டறை மேல்`, `பற்றிப்/பற்றி`, and especially current `தேனிலே மருந்தைக் கலந்து` versus machine `தேனிடை மருந்தை கலந்து`, plus final case morphology. No canonical change was made.

Batch 13 supports the opening artist-list structure and K. R. Ramasamy identification, then exposes heavy machine corruption around the `நடிகவேள்` proper name and the reform-theatre brothers' title/name sequence. Independent right-channel navigation also supports an institutional clause resembling `அவர்களுடைய நிறுவனத்திலே இருந்து` and the transition near `10:18` toward `போராடிய நம்முடைய லட்சிய நடிகர் ராஜேந்திரன்`. Exact names, initials, titles and syntax remain for true audible replay. No canonical change was made.

Batch 14 strongly supports `நடிகமணி டி. வி. நாராயணசாமி`, `இந்த நாவினால்`, the idea that revolutionary views gain force when voiced, `சிம்மக்குரல்`, and `என்னுடைய நண்பர் சிவாஜி கணேசன்`. Machine evidence also proposes a boundary join from `லட்சிய நடிகர் ராஜேந்திரன்` into Narayanasamy. Exact replay must settle whether `எஸ். எஸ்.` and `ஆகியவர்கள்` are audible, `பேசினால்/பேசினால்தான்`, `முதல் முதலாகச்/முதன் முதலாக`, and the badly corrupted final statement about carrying Periyar and Anna's ideas onto stage and screen. No canonical change was made.

Batch 15 gives a clearer machine-supported skeleton for the previously withheld `10:48–11:20` rhetoric: Anna calls, the artists go immediately, do not first ask `என்ன நாடகம், என்ன வேடம்`, are willing to speak what is asked, hold strong regard for Anna, and are contrasted with people who would flee from fear that acting or public association might damage their profession. Exact joins around `ஓடோடி`, the willingness-to-speak clause, the second Anna-reference, and the professional-career sentence remain for true audible replay. The canonical placeholder was intentionally retained; no Tamil was reconstructed from ASR.

Batch 16 supports the `எனக்கு எவ்வளவோ நினைவுகள் / எத்தனையோ பசுமையான எண்ணங்கள்` transition, a candidate assembled-artists address resembling `இங்கு வீற்றிருக்கின்ற கலை உலகப் பெருமக்கள்`, Sivaji's `கிருஷ்ணனை நாம் பாராட்ட வேண்டும்` remark, and the contrast that Krishna's condition is not so pitiable. It also exposes a major conflict: current T1 `வேறு விரக்தியிலே... பல்வேறு விரக்திகளை...` versus machine `வேறொரு இயக்கத்திலே... வேறொரு கொள்கையை...`, plus `அந்தக் கிருஷ்ணன்` versus machine `ஸ்ரீகிருஷ்ணன்`. These remain for true audible replay; no canonical Tamil was changed.

Batch 17 supports Kannadasan's `நீ கிருஷ்ணனை ஏற்றுக்கொள்` recommendation, `பரமாத்மா கிருஷ்ணன்`, the reported `கிருஷ்ண பரமாத்மா` temple-house remark and a strong connective candidate `இது போதாதா எதிரிகளுக்கு?` before `நான் வீடு கட்டவில்லை`. It exposes a major central conflict: current T1 `அவருடைய பெருமதிப்புக்கு இலக்காக இருப்பதாக` versus machine `அவ்வளவு பரிதாபத்துக்குரிய நிலையில் இருப்பதாகவும்`, plus `அருகாமையிலே / அருகாமையிலேதான்`. These remain for true audible replay; no canonical Tamil was changed.

Batch 18 supports `நான் வீடு கட்டவில்லை`, the twenty-years-earlier house-purchase correction, the newspaper-parody structure, and `கருணாநிதியின் நண்பர் கண்ணதாசனே குட்டை உடைத்துவிட்டார்`. It also establishes that the attachment transcript itself is badly corrupted at three crucial points: machine `முதலாளித்துவமான பிறகுதான்`, `கோவாலவரத்தில்`, and `மரண நம்பலமானது` do not verify the cleaner candidates `முதலமைச்சர் ஆன பிறகுதான்`, `கோபாலபுரத்திலே`, or `மர்மம் அம்பலமானது`. The press-style join, `தெரியுமா?`, `இதை கண்ணதாசனே வெளியிட்ட தகவல்`, and the exact `12:49` boundary remain for true audible replay. No canonical Tamil was changed.

Batch 19 revisits the previously withheld `12:49–13:15` interval. Fresh semantic retrieval produced no stable passage, and exact-anchor checks recover only the post-collapse boundary (`ஓய்வு பெற்றவர்`, `அந்த வீட்டை விற்க`, `வாங்குவதற்காக நான் முயற்சித்த`) rather than trustworthy words inside the gap. The cleaner `தபால் இலாகாவிலே` form is not preserved by the attachment transcript. The entire 26-second interval therefore remains withheld; no bridge was reconstructed from narrative context and no canonical Tamil was changed.

Batch 20 gives a much fuller machine-supported skeleton for `13:15–14:00`: a retired senior official sells the house; Karunanidhi attempts to buy it; a locality rendered with `பெரிய அக்கிரகாரம்` objects with questions resembling `கருணாநிதியா? அவனுக்கா?`; residents who had not seen him want to see him first; and the seller/elder arranges an occasion leading into the `14:00` mild-personality remark. Crucially, machine `ததாலிவாக்காகிலே`, `தயுத்த பழம்`, `கோவாலவரம்`, the third resident question, and the invitation/meeting syntax remain corrupted and are not normalized. No canonical Tamil was changed.

Batch 21 covers the short `14:00–14:15` conclusion of the house anecdote. Machine evidence supports `சாதுவாகத்தான் இருக்கிறார்`, a following clause resembling `அதற்குப் பிறகு அந்த அக்கிரகாரத்தில் உள்ள அத்தனை பேரும் ஒத்துக்கொண்டுதான்`, and the house-purchase conclusion. It conflicts directly with current T1 at `பேரைப் பார்த்து` versus machine `தேரைப் பார்த்து`, and leaves the post-quotation attribution, agreement-verb morphology, `வீட்டைக் / வீட்டை`, and exact `14:15` transition for true audible replay. No canonical Tamil was changed.

Batch 22 maps `14:15–14:59`. Machine evidence strongly supports `அதே இடத்தில், அதே கொள்கையில் நின்று நிலைத்திராவிட்டாலும்`, `இந்த கொள்கை நிலைத்திருக்கிறதல்லவா?`, and a gratitude clause resembling `பாடுபட்டவர்களுக்கு நன்றி கூறுகிற இடத்திலே நான் இருக்கின்றேன்`, followed directly by the Sivaji stage-recollection boundary. It leaves the opening `கலை உலகம் / தலைஉலகம்` corruption, the phrase rendered as `நாம் பலர் ஆதாயம் பெற்றாவிட்டாலும்`, exact case/morphology, and the gratitude wording for true audible replay. No canonical Tamil was changed.

Batch 23 covers `14:59–15:35`. Machine evidence strongly supports the Sivaji stage-recollection skeleton, the reversal from `என்னோடு சேர்ந்து சிவாஜி நடித்திருக்கிறார்` to `சிவாஜியோடு சேர்ந்து நான் நடித்தேன்`, the present-day `சூழ்நிலைக்குப் பொருத்தமாக இருக்கும்` idea, and the `பணம் வாங்காமல் வந்து நடிக்கின்ற` statement. It leaves the current `நகைச்சுவையாக` versus machine-corrupted `ரேடிக்கியாக`, `கருணாநிதி` versus machine `கலைஞர் அவர்கள்`, exact play-syntax and `விளங்கினார் / விளங்கினார்கள்` honorific morphology for true audible replay. No canonical Tamil was changed.

Batch 24 covers `15:35–16:00`. Machine evidence maps a fund-raising theatre list with clearer `வெள்ள நிவாரண நிதி` and `வரட்சி நிதி`, but leaves corrupted `பொய்யல் நிவாக நிதி` and `கலகத் தேர்தல் நிதி` for true replay. The co-actor sequence contains machine-corrupted `நம்முடைய ரக்சி நடிகர்களும்`, plus `டி.வி.என்`, `கே.ஆர். ராமசாமி`, `கவிஞர் அவர்களும்`, and a closing `வேடம் புனைந்திருக்கின்றார்கள்`. Play titles, the first co-actor/title, expanded identities and exact morphology remain unresolved. No canonical Tamil was changed.

These are textual/machine prechecks only. They do **not** change canonical Tamil and do **not** increment T2 direct-listening counters.

## Provisional T1 evidence through 20:00

The durable draft covers the humour-filled opening, Chinna Annamalai anecdote, Kannadasan/Sivaji recollections, crossed telephone story, Anna and Kalaivanar, Ilangovan/Kannagi and `இஞ்சிப்பத்தர்`, medicine-with-honey imagery, early movement artists, Krishna wordplay, the Gopalapuram house anecdote, gratitude to movement artists, Sivaji's early unpaid stage work, the art/politics distinction, and the Tirukkural `எச்சம்` discussion.

The explanation from approximately `17:56–19:00` and the comparison around `19:33–20:00` remain withheld because machine evidence repeatedly collapsed or became malformed. No printed Tirukkural wording was substituted.

## `20:00–24:00` provisional pass

Three machine-navigation views were compared: captured independent 120-second right-channel chunks, stored confidence data, and a checksum-verified independent 30-second large-v3-turbo run.

The provisional draft preserves:

- `எச்சம்` as more than merely one's children/descendants;
- Kalaivanar's ideas and humorous expression as part of what he left behind;
- a Congress-conference recollection and `விலாங்கு மனிதன்`;
- Kalaivanar's hotel-keeper role;
- the 1947 Independence/radio invitation;
- cross-party admirers;
- election campaigning for Anna, Lakshiya Nadigar Rajendran, the speaker and Kazhagam comrades;
- widespread `வில்லுப்பாட்டு` campaigning;
- a family-affection sentence leading into the final batch.

The hotel example, Kalaivanar's exact radio response, several political names/titles and much of `22:00–23:30` remain unresolved rather than reconstructed.

## `24:00–26:22.080` final provisional T1 pass

Two independent machine-navigation witnesses were compared:

1. the previously captured right-channel `24:00–26:00` plus `26:00–26:22` artifact;
2. a fresh checksum-verified right-channel large-v3-turbo pass in independent approximately 20-second chunks with `condition_on_previous_text=false`.

They converge on the broad final sequence:

- Kalaivanar treating suffering lightly;
- laughter and emotional state being discussed in relation to bodily well-being;
- `சிரிப்பு மாமருந்து` and Kalaivanar being described as a good doctor who taught this to the country;
- a personal recollection involving Kalaivanar, Karunanidhi and Kannadasan sitting together and playing cards for recreation;
- the repeated Kannadasan line `எங்கே தேடுவேன் பணத்தை எங்கே தேடுவேன்` after losing money;
- Kalaivanar repeatedly responding to Kannadasan's losses with money, while the exact response and transfer verbs remain noisy;
- Kalaivanar surrounding himself with many friends and being unable to remain alone without a group around him;
- Kalaivanar having built a great `கலைக்குடும்பம்`;
- a provisional repeated `வாழ்க, வாழ்க, வாழ்க` farewell and machine-supported `நன்றி, வணக்கம்` ending.

### Final-batch uncertainties retained

The final T1 text deliberately leaves unresolved:

- two short laughter-related aphorisms;
- part of the physiological description of anger and praise;
- the exact place/joining wording in the card-game setup;
- how the first hundred rupees enters the game;
- exact Kalaivanar response/money-transfer wording after Kannadasan's song;
- a later repeated money-giving joke;
- the exact grammatical form of the friends-surrounding clause;
- the noun in the final `அந்தக் கலைவாணருடைய ... வாழ்க` phrase.

The provisional `நன்றி, வணக்கம்` ending is **not** a T2 verification. The true final audible wording, grammatical completeness and truncation status remain open.

## Machine-readable T1 state

- provisional speech segments drafted: **30**;
- open unresolved ranges/phrases: **60**;
- provisional T1 coverage: **complete through the true decoded end `00:26:22.080`**;
- T2 direct-listening segments checked: **0**;
- T2 direct-listening segments passed: **0**;
- English: blocked.

No T1 section is verified Tamil.

## Temporary workflow cleanup

All temporary Audio 06 workflow files used for the final tail evidence, short-chunk cross-check and one-time transcript patch were removed after the evidence was captured and the durable transcript updated. No temporary workflow file is part of the archive.

## Exact next activity

Begin **Tamil T2 strict direct-listening audit from `00:00`**.

Requirements:

1. directly transcribe/verify the separate spoken lead-in at `00:00–approximately 00:14`;
2. use the prepared `00:13.966–00:41.641` quiet-boundary evidence only as navigation, not as a substitute for listening;
3. confirm the exact first speech word and main-speech opening boundary;
4. audit every provisional speech segment sequentially against the controlling MP3;
5. resolve bracketed T1 uncertainty only from direct source listening, not external history or printed text;
6. later perform separate direct replays of the final 60 seconds and final 30 seconds;
7. replay from the final major pause to the true `00:26:22.080` file end;
8. confirm the final audible word, grammatical completeness and `recording_truncated` status;
9. do not begin T3 until T2 is complete;
10. do not begin English until verified Tamil is frozen.
