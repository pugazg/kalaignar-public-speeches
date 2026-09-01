# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake and machine-aided navigation complete. Tamil T1 provisional draft reaches approximately `24:00`. Direct-listening audit has not started.**

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

## Provisional T1 evidence through 16:00

The durable draft covers the humour-filled opening, Chinna Annamalai anecdote, Kannadasan/Sivaji recollections, crossed telephone story, Anna and Kalaivanar, Ilangovan/Kannagi and `இஞ்சிப்பத்தர்`, medicine-with-honey imagery, early movement artists, Krishna wordplay, the Gopalapuram house anecdote, gratitude to movement artists, and Sivaji's early unpaid stage work. Unstable names, joins and lists remain bracketed.

## `16:00–20:00` provisional pass

A targeted right-channel large-v3-turbo run used independent 30-second chunks.

The usable evidence supports art as a vehicle for political ideas without art itself becoming politics, beauty/taste as the essence of effective speech and writing, good and evil uses of art, Kalaivanar's noble artistic aim, and the beginning of the Tirukkural `எச்சம்` discussion.

The explanation from approximately `17:56–19:00` and the comparison around `19:33–20:00` remain withheld because the machine evidence repeatedly collapsed or became malformed. No printed Tirukkural wording was substituted.

## `20:00–24:00` provisional pass

This batch used three machine-navigation views of the same controlling source:

1. the already captured independent 120-second right-channel chunks;
2. their stored word-confidence data;
3. a new checksum-verified right-channel large-v3-turbo run in independent 30-second chunks with `condition_on_previous_text=false`.

All are navigation evidence only.

### `20:00–21:04` — usable provisional structure

The fresh 30-second pass strengthens the following ideas:

- `எச்சத்தால் காணப்படும்` does not simply mean being known through one's children or descendants;
- `எச்சம்` concerns what a person leaves behind, including ideas/intellectual wealth, although the exact explanatory syntax remains uncertain;
- Kalaivanar's ideas given to the people continue as his legacy;
- gathering after Kalaivanar to praise him, honour him and explain how his ideas were expressed through humour is itself part of what he left behind.

The exact opening words at `20:00`, Valluvar-explanation syntax and two joins remain unresolved.

### `21:04–22:00` — Congress-conference / `விலாங்கு மனிதன்` recollection

Both the older and fresh chunk evidence support:

- a Congress conference, with the exact introductory/place wording still uncertain;
- Kalaivanar being invited to perform a play;
- the title `விலாங்கு மனிதன்`;
- an explanation of `விலாங்கு` as a water-dwelling creature, while the exact snake-related comparison is unclear;
- Kalaivanar appearing as a hotel-keeper character.

The hotel-character example from approximately `21:38–22:00` remains withheld. The fresh short chunks still distort the political/shirt-colour comparison and do not support a safe exact reading.

### `22:00–22:52` — Independence/radio passage

The earlier independent 120-second evidence supports a provisional sequence beginning with:

- the year 1947 and the Indian subcontinent obtaining freedom;
- the freedom flag rising high;
- radio personnel asking Kalaivanar to sing a freedom song.

The dedicated 30-second pass collapses across much of this range and only recovers a later reference to `தன்மான உணர்வு`. Therefore Kalaivanar's exact response, the self-respect statement and a Sivaji-related reference remain explicitly unresolved. No historical quotation has been reconstructed from external sources.

### `22:52–23:25` — cross-party admirers / movement preference

The older machine evidence suggests references to Jeevanandam, Ma. Po. Si., Congress leaders and others. Because the fresh 30-second run collapses across much of this range, only the stable names already represented conservatively in the T1 draft are retained, with titles, other names and the contrast sentence bracketed.

### `23:25–24:00` — election campaigning and movement attachment

The machine passes converge on:

- Anna should win;
- Lakshiya Nadigar Rajendran should win;
- the speaker should win;
- Kazhagam comrades should win;
- Kalaivanar travelling widely for those electoral campaigns;
- his `வில்லுப்பாட்டு` being performed widely;
- an emotional/family-affection conclusion continuing beyond `24:00`.

The place/person reference, exact electoral-effect sentence and the subject/verb of the emotional reaction remain unresolved.

## Machine-readable T1 state

- provisional speech segments drafted: **26**;
- open unresolved ranges/phrases: **47**;
- provisional T1 coverage: **through approximately `24:00`**;
- T2 direct-listening segments checked: **0**;
- T2 direct-listening segments passed: **0**;
- English: blocked.

No T1 section is verified Tamil.

## Temporary workflow cleanup

All temporary Audio 06 workflow files used for the `20:00–24:00` chunk run, prior-artifact exposure and confidence inspection were removed after evidence capture. No temporary workflow file is part of the durable archive.

## Exact next activity

Process the **final provisional Tamil T1 batch: `24:00–00:26:22.080`**.

Requirements:

1. continue from the incomplete family-affection sentence at `24:00`;
2. transcribe through the true file end, not an assumed end;
3. use independent right-channel chunks as navigation only;
4. retain uncertain names, quotations and joins explicitly;
5. include the provisional final words only if supported by the source evidence;
6. after T1 reaches `00:26:22.080`, do **not** begin English;
7. the next gate must be T2 direct listening from `00:00`, including the separate spoken lead-in and exact opening boundary;
8. later in T2, separately replay the final 60 seconds and final 30 seconds and confirm the true final audible word before any Tamil freeze.
