# Audit — Kalaivanar Memorial-Day Speech, Audio 06

## Status

**Source intake complete. Machine-aided navigation in progress. Tamil T1 starting.**

The controlling MP3 is authoritative. Machine transcripts recorded during intake are secondary evidence only and must not be promoted to verified Tamil without direct listening.

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
- right-channel extraction is permitted as a navigation/listening aid only.

## Duplicate check

Repository search found no existing record for the filename or checksum.

The earlier completed `speeches/kalaivanar-nsk-memorial-day/` source is only `00:07:23.559` and has a different checksum. This 26-minute source is therefore registered separately under:

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
- machine navigation proposes a complete tribute to Kalaivanar's large artistic family followed by `நன்றி, வணக்கம்`;
- the final minute and final 30 seconds must still pass dedicated direct replay;
- `recording_truncated` remains unresolved;
- no abrupt-ending claim is permitted at this stage.

## Machine-aided navigation findings

The opening and tail models agree on several navigation points, but their spellings are not canonical:

- the speech explicitly frames the event as a Kalaivanar function rich in humour;
- early passages mention Chinna Annamalai, Periyar, Sivaji Ganesan and Kannadasan;
- the tail discusses laughter, anger and praise, recalls Kalaivanar and Kannadasan playing cards, and closes by praising Kalaivanar for nurturing a large artistic family;
- the final machine-proposed shape is grammatically complete.

All wording remains provisional until direct comparison.

## Temporary analysis infrastructure

Temporary workflows currently active or awaiting evidence capture:

- `.github/workflows/audio-06-intake.yml`;
- `.github/workflows/audio-06-boundaries.yml`;
- `.github/workflows/audio-06-boundaries-small.yml`;
- `.github/workflows/audio-06-right-small.yml`.

They must be deleted after their artifacts are captured and useful evidence is recorded.

## Next audit activity

1. capture the right-channel full navigation transcript;
2. establish stable 2–3 minute T1 batches;
3. directly replay and draft the spoken lead-in and first speech batch;
4. mark unresolved words instead of adopting ASR guesses;
5. separately audit the final 60 and final 30 seconds before any completion claim.
