# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake and machine-aided navigation complete. Tamil T1 provisional draft reaches approximately `08:00`. Direct-listening audit has not started.**

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

### Corrected chunk strategy

Useful evidence was captured using:

- the stronger right channel;
- independent 60- or 120-second chunks;
- `condition_on_previous_text=false`;
- `large-v3-turbo`;
- no cross-chunk prompting.

The complete chunked pass supplies a topic map through the true file end and does not show the catastrophic whole-file repetition collapse. Some chunk starts and ends remain unstable, so it is still navigation evidence rather than verified wording.

### Targeted opening and `04:00–08:00` passes

Independent opening chunks confirmed stable portions concerning:

- humour at the memorial function;
- Chinna Annamalai's humorous response;
- Kannadasan and Sivaji Ganesan;
- the beginning of the hotel-room recollection.

The targeted `04:00–08:00` pass confirmed the narrative sequence:

- political hostility between the speaker and Kannadasan;
- an accidental crossed telephone connection;
- the later conversation about Kannadasan's attacks;
- Tamil and Tamil art softening hostility;
- Anna using art to communicate social ideas;
- Kalaivanar as an early supporting force;
- S. S. Rajendran's observation;
- the Kannagi film and Ilangovan discussion.

It did **not** safely resolve:

- the telephone-interference sentence around `04:48–05:14`;
- one name in the `03:22` political-party passage;
- the complete personal-name expansion before `இளங்கோவன்`;
- the quoted article opening near `07:44–08:00`.

Those ranges remain visibly unresolved rather than guessed.

## Provisional Tamil T1 state

`transcription-ta.md` now reaches approximately `08:00` and includes provisional sections for:

1. the humour-filled opening;
2. the beginning and conclusion of the Chinna Annamalai anecdote, with its unstable interior withheld;
3. Kannadasan and Sivaji Ganesan;
4. the hotel-room and crossed-telephone recollection;
5. Kannadasan asking how the speaker reacted to his political attacks;
6. Tamil/art transforming hostility;
7. Anna, Kalaivanar and S. S. Rajendran;
8. the beginning of the Ilangovan/Kannagi discussion.

No section has passed T2. The draft status is provisional throughout.

## Temporary workflow cleanup

All temporary Audio 06 GitHub Actions workflows used for intake, boundary checks and chunk generation were deleted after their artifacts were captured and their evidentiary limits documented. No Audio 06 workflow remains under `.github/workflows/`.

## Exact next activity

Process provisional Tamil T1 for `08:00–12:00`, covering:

- Anna's quotation about Ilangovan;
- the Silappathikaram/Kannagi discussion;
- the `இஞ்சி பத்தனே மேல்` article and Kalaivanar's character;
- Kalaivanar conveying political, economic and social ideas through humour;
- the medicine-and-honey image;
- K. R. Ramasamy and other early movement artists.

Use independent right-channel chunks as navigation only. Preserve uncertainty. Do not begin English.
