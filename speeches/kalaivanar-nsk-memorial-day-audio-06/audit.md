# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake and machine-aided navigation complete. Tamil T1 provisional draft reaches approximately `16:00`. Direct-listening audit has not started.**

The controlling MP3 is authoritative. Machine transcripts are secondary navigation evidence only and must not be promoted to verified Tamil without direct listening.

## Source identity

- filename: `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`;
- official URL: `https://tamildigitallibrary.in/kalaignar/audio/06.Kalavaivannar%20N.S.Krishnnan%20Ninavul%20Naal%20Vizha%20Vil%20Kaligar%20Speech.mp3`;
- SHA-256: `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`;
- file size: `25,313,377` bytes;
- decoded duration: `1582.080` seconds / `00:26:22.080`;
- remote identity: verified by exact checksum and byte-size reproduction;
- binary committed: No.

## Technical inspection

- MP3, stereo, 44.1 kHz, approximately 128 kb/s;
- right channel approximately 6 dB stronger than left;
- no useful embedded event metadata found;
- right-channel extraction was used only as a navigation/listening aid;
- the original stereo MP3 remains the controlling witness.

## Duplicate check

Repository search found no existing record for the filename or checksum.

The earlier completed `speeches/kalaivanar-nsk-memorial-day/` source is `00:07:23.559` and has a different checksum. This 26-minute source is therefore registered separately under:

`speeches/kalaivanar-nsk-memorial-day-audio-06/`

## Boundary precheck

### Opening

- separate spoken lead-in begins at `00:00`;
- lead-in ends approximately `00:14`;
- silence detector found a low-level interval from `00:13.982` to `00:29.653` at the intake threshold;
- main speech begins approximately `00:41.9`;
- exact lead-in wording and exact first speech word remain to be verified directly.

### Ending

- audible activity continues to approximately `00:26:21.4`;
- independent boundary-navigation passes propose a complete tribute to Kalaivanar's artistic family followed by `நன்றி, வணக்கம்`;
- the final minute and final 30 seconds must still pass dedicated direct replay;
- `recording_truncated` remains unresolved;
- no abrupt-ending claim is permitted at this stage.

## Machine-aided evidence

### Rejected whole-file outputs

1. The first mono full-file pass entered repeated-token hallucination after the useful opening range.
2. The full-file right-channel small-model pass improved early anchors but later repeatedly generated `எல்லாம்` and another repeated phrase.

Both are rejected as transcripts. They may not be copied wholesale into `transcription-ta.md`.

### Accepted navigation strategy

Useful evidence was captured using:

- the stronger right channel;
- independent 60- or 120-second chunks;
- `condition_on_previous_text=false`;
- `large-v3-turbo`;
- no cross-chunk prompting.

The complete chunked pass supplies a topic map through the true file end and does not show the catastrophic whole-file repetition collapse. Some chunk starts and ends remain unstable, so it is still navigation evidence rather than verified wording.

### Targeted opening and `04:00–08:00` checks

Independent opening chunks confirmed stable portions concerning:

- humour at the memorial function;
- Chinna Annamalai's humorous response;
- Kannadasan and Sivaji Ganesan;
- the beginning of the hotel-room recollection.

The targeted `04:00–08:00` pass confirmed the narrative sequence involving political hostility, an accidental crossed telephone connection, Kannadasan's attacks, Tamil/art softening hostility, Anna's use of art, Kalaivanar's supporting role, S. S. Rajendran, and the Kannagi/Ilangovan discussion.

It did **not** safely resolve several telephone-interference words, one political-party/name phrase, the full personal-name expansion before `இளங்கோவன்`, or the article opening near `07:44–08:00`.

### `08:00–12:00` provisional pass

Stable candidate structure supported:

- Anna praising and criticizing Ilangovan's *Silappathikaram* adaptation;
- the `இஞ்சிப்பத்தர்` character and the gold/brass image;
- `வஞ்சிப்பத்தரை விட இந்த இஞ்சிப்பத்தரே மேல்`;
- political, economic and social ideas presented like medicine mixed with honey;
- early movement artists including K. R. Ramasamy, T. V. Narayanasamy and Sivaji Ganesan;
- the transition to Kannadasan/Krishnan wordplay.

Names, titles and rhetorical joins that did not converge remain bracketed in the canonical T1 draft.

### `12:00–16:00` provisional pass

The previously captured chunk artifact was re-read, including its stored word-confidence data. Stable candidate structure supports:

- Kannadasan recommending that the speaker “accept Krishna”;
- a Krishna/Paramatma joke moving into a Gopalapuram house anecdote;
- the speaker saying he did not construct a new house but bought an existing house about twenty years earlier;
- mock-newspaper phrasing including the stable anchors `கருணாநிதியின் நண்பர் கண்ணதாசனே குட்டை உடைத்துவிட்டார்` and `மர்மம் அம்பலமானது`;
- a retired postal-department official selling the house;
- reactions to Karunanidhi moving into the locality/agraharam;
- the remembered comment that the name had caused fear although the person looked mild;
- a transition from the house story to gratitude for artists who carried movement ideas;
- Sivaji's early unpaid stage work with the speaker;
- a list of stage plays and co-actors continuing to approximately `16:00`.

The following were **not** reconstructed:

- `12:49–13:15`, where the stored machine chunk itself enters repeated-token collapse;
- the exact retired official's name/title sequence;
- the detailed locality/agraharam exchange around `13:28–14:00`;
- the exact ideological-position sentence around `14:29–14:54`;
- the stage-play titles and complete co-actor list around `15:35–16:00`.

Candidate anchors such as T. V. Narayanasamy/T.V.N. and K. R. Ramasamy are explicitly not treated as verified list readings.

An additional full-download `12:00–16:00` 60-second rerun was triggered for comparison but was not needed to establish the durable provisional text. The durable T1 update relies on the already captured chunk evidence and its confidence inspection, not on an unfinished or partial rerun.

## Provisional Tamil T1 state

`transcription-ta.md` now reaches approximately `16:00`.

Machine-readable state:

- provisional speech segments drafted: **15**;
- open unresolved ranges/phrases: **24**;
- T2 direct-listening segments checked: **0**;
- T2 direct-listening segments passed: **0**.

No section has passed T2. The draft status is provisional throughout.

## Temporary workflow cleanup

All temporary Audio 06 workflow files used for intake, boundary checks, chunk generation, artifact exposure and confidence inspection have been deleted after useful evidence was captured and its limitations documented.

No temporary workflow file is part of the durable archive.

## Exact next activity

Process provisional Tamil T1 for **`16:00–20:00`** using the previously captured independent right-channel chunk evidence.

Requirements:

1. continue exactly from the unresolved stage-play/co-actor list at `16:00`;
2. add only wording that is stable enough for a provisional T1 draft;
3. retain uncertain names, titles and quotations as explicit unresolved ranges;
4. do not call any machine-derived text direct listening;
5. do not begin English;
6. after T1 reaches the true end, begin T2 with the spoken lead-in and opening boundary, not with English.
