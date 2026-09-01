# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake and machine-aided navigation complete. Tamil T1 provisional draft reaches approximately `20:00`. Direct-listening audit has not started.**

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

The standard printed wording of any quoted source, including Tirukkural, must not be used to normalize the speech silently. The Audio 06 T1 currently preserves the machine-supported spoken form `எச்சத்தால்`; T2 direct listening must decide the actual recording.

## Provisional T1 evidence through 16:00

The durable draft already covered the humour-filled opening, Chinna Annamalai anecdote, Kannadasan/Sivaji recollections, crossed telephone story, Anna and Kalaivanar, Ilangovan/Kannagi and `இஞ்சிப்பத்தர்`, medicine-with-honey imagery, early movement artists, Krishna wordplay, the Gopalapuram house anecdote, gratitude to movement artists, and Sivaji's early unpaid stage work. Unstable names, joins and lists were kept bracketed.

## `16:00–20:00` provisional pass

A targeted right-channel large-v3-turbo run used independent 30-second chunks.

### `16:00–18:00` — usable provisional structure

The chunks converge on:

- people in the arts serving a movement without seeking to turn art itself into politics;
- `அரசியலுக்குக் கலை தேவை`;
- Anna sharing the aim of using art to convey political ideas;
- beauty/taste in words, speech and writing;
- `சொல்லில் சுவை இருந்தால்தான் மற்றவர்களுடைய உள்ளத்திலே பதியும்`;
- `அந்தச் சுவைக்குப் பேர்தான் கலை`;
- `அரசியலுக்குக் கலை தேவை; ஆனால் கலையே அரசியல் அல்ல`;
- the comparison `பெண்களுக்கு நகை தேவை; ஆனால் நகையே பெண்கள் அல்ல`;
- art being usable for both good and evil;
- the claim that art used for good should grow and be nurtured;
- Kalaivanar following that noble aim;
- the beginning of the Tirukkural passage `தக்கார் தகவிலர் என்பது அவரவர் எச்சத்தால் காணப்படும்`.

A few linking subjects and an epithet remain unresolved.

### `18:00–19:00` — withheld

The earlier 120-second chunk collapsed into repetition. The dedicated large-model 30-second rerun also produced repeated-token collapse across most of this hour-minute. The Kural explanation is therefore withheld instead of being reconstructed from the printed Kural or historical knowledge.

### `19:00–approximately 19:33` — partially recoverable

The machine evidence supports a legacy passage involving:

- Kalaivanar's Self-Respect ideas;
- work against caste;
- his artistic service;
- his compassion/social concern;
- those qualities remaining his `எச்சம்` many years later;
- the explicit clarification that the Kural does not mean merely being known through one's children.

Some opening and interior phrases remain bracketed because exact lexical readings do not converge.

### `approximately 19:33–20:00` — withheld

The large-model pass becomes malformed and then produces non-Tamil output. This comparison/wordplay is intentionally withheld pending source replay.

## Machine-readable T1 state

- provisional speech segments drafted: **19**;
- open unresolved ranges/phrases: **31**;
- T2 direct-listening segments checked: **0**;
- T2 direct-listening segments passed: **0**;
- English: blocked.

No T1 section is verified Tamil.

## Temporary workflow cleanup

The temporary `16:00–20:00` large-model workflow and the separate `18:00–20:00` small-model cross-check workflow were deleted after the useful evidence boundary was established. The small-model run was not used to fill any withheld text.

## Exact next activity

Process provisional Tamil T1 for **`20:00–24:00`**.

Requirements:

1. continue from the unresolved comparison at `20:00` without reconstructing the missing preceding words;
2. use captured/targeted right-channel chunks as navigation only;
3. add only stable provisional wording;
4. mark uncertain names, quotations and joins explicitly;
5. do not begin T2 yet unless T1 has reached the true end;
6. do not begin English.
