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

Four preparatory T2 records now exist:

- `t2-batches/batch-01-00-00-01-10-precheck.md` — lead-in, opening boundary and first main-speech sentence;
- `t2-batches/batch-02-01-10-02-34-precheck.md` — Chinna Annamalai anecdote and humorous conclusion.
- `t2-batches/batch-03-02-34-03-22-precheck.md` — Kannadasan–Sivaji recollection and the unresolved humorous transition.
- `t2-batches/batch-04-03-22-04-00-precheck.md` — opposition-period hotel-room setup and Kannadasan political-separation context.

Batch 2 exposes a fuller machine-supported narrative skeleton for the previously withheld `01:16–02:12` span, including the claim of telling something unknown to others, questioning whether the anecdote was later stage invention, an uncertainly transcribed conference/event reference, the possibility of asking Kalaivanar whether it was true, and a mock-boasting sequence about private knowledge/closeness. Proper nouns, honorific verb forms, the conference name and several examples remain too noisy for canonical promotion.

Batch 3 strongly supports the names Kannadasan and Sivaji Ganesan, their closeness to Kalaivanar, and the quotation ending in substance with `நான் காதலிக்கின்ற ஒரே கவிஞர்`. The attachment-level ASR corrupts the beginning of the quotation and the following humorous competition-in-affection sentence; therefore the current T1 candidate `என்னை வைதாலும் திட்டினாலும்...` remains provisional and the transition remains unresolved pending audible replay.

Batch 4 strongly supports the opposition-period setting, the speaker writing film dialogue alone while staying in a Chennai hotel, `காலை பதினொரு மணி இருக்கும்`, Kannadasan separating from Anna with another friend, starting another party, and attacking the speaker politically. The exact friend modifier and `வேகமாக/மிக வேகமாக` remain auditory checkpoints; no canonical change was made.

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
