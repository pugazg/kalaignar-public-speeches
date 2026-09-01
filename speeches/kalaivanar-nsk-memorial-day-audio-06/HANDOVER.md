# Handover — Kalaivanar Memorial-Day Speech, Audio 06

## Repository and path

- repository: `pugazg/kalaignar-public-speeches`;
- branch: `main`;
- active path: `speeches/kalaivanar-nsk-memorial-day-audio-06/`.

## Mandatory continuation reading

1. `SPEECH_PROCESSING_GUIDE.md`;
2. `AUDIO_SPEECH_PROCESSING_GUIDE.md`;
3. `docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md`;
4. `docs/START_NEW_AUDIO_SPEECH_PROMPT.md`;
5. `speeches/kalaivanar-nsk-memorial-day/LEARNINGS.md`;
6. this `HANDOVER.md`;
7. `README.md`;
8. `metadata.json`;
9. `audit.md`;
10. `transcription-ta.md`.

## Controlling source

- filename: `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`;
- source URL: `https://tamildigitallibrary.in/kalaignar/audio/06.Kalavaivannar%20N.S.Krishnnan%20Ninavul%20Naal%20Vizha%20Vil%20Kaligar%20Speech.mp3`;
- SHA-256: `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`;
- file size: `25,313,377` bytes;
- decoded duration: `1582.080` seconds / `00:26:22.080`;
- audio: MP3, stereo, 44.1 kHz, approximately 128 kb/s;
- source binary committed: No;
- remote source identity: verified against the attachment by checksum and byte size.

## Archive identity

Official catalogue title:

`கலைவாணர் என்.எஸ்.கிருஷ்ணன் நினைவு நாள் விழா உரை`

This source is distinct from the completed `00:07:23.559` recording at `speeches/kalaivanar-nsk-memorial-day/`. The `audio-06` suffix is an explicit disambiguator.

Exact speech date and venue are not yet established.

## Source-boundary state

- right channel is approximately 6 dB stronger than left;
- original stereo remains authoritative;
- spoken lead-in: `00:00–approximately 00:14`;
- detected low-level silence begins `00:13.982` and ends `00:29.653` at the intake threshold;
- main speech begins approximately `00:41.9`;
- final activity continues to approximately `00:26:21.4`;
- machine navigation proposes a complete ending with a tribute to Kalaivanar's artistic family followed by `நன்றி, வணக்கம்`;
- opening and ending are **not** yet strict-direct-listening verified;
- `recording_truncated`: unresolved.

Never promote the provisional ending to verified status before the mandatory final-60-second and final-30-second direct replays.

## Machine-navigation state

Machine navigation is **complete** and its evidence has been captured.

Two whole-file outputs were rejected after repetition drift/hallucination. The useful navigation strategy was:

- stronger right channel;
- independent 60- or 120-second chunks;
- `condition_on_previous_text=false`;
- large-v3-turbo;
- no cross-chunk prompting.

This evidence is navigation only. It is not T2 direct listening.

All temporary Audio 06 workflow files have been removed from the durable repository after evidence capture.

## Tamil workflow state

- T1 first pass: **in progress — provisional through approximately `16:00`**;
- provisional speech segments drafted: **15**;
- open unresolved ranges/phrases: **24**;
- T2 strict direct-listening audit: **not started**;
- T3 consolidation/freeze: **blocked**;
- English: **blocked**.

### Durable T1 coverage through 12:00

The draft includes:

- humour at the function;
- Chinna Annamalai's anecdote, with its unstable interior withheld;
- Kannadasan and Sivaji;
- crossed-telephone recollection;
- Tamil/art softening political hostility;
- Anna and Kalaivanar;
- S. S. Rajendran;
- Ilangovan/Kannagi and the `இஞ்சிப்பத்தர்` discussion;
- medicine-with-honey image;
- early movement artists;
- Kannadasan/Krishna wordplay.

### Newly completed provisional T1: 12:00–16:00

The draft now also covers:

- Kannadasan recommending “accept Krishna”;
- Krishna/Paramatma wordplay;
- beginning of the Gopalapuram house anecdote;
- the speaker saying he bought an existing house rather than constructing a new one;
- mock-newspaper phrasing, with unstable joins explicitly bracketed;
- a retired postal official selling the house;
- reactions to Karunanidhi moving into the locality/agraharam;
- the remembered “பேரைப் பார்த்து ... ஆளைப் பார்த்தால் சாதுவாக...” comment;
- gratitude to people who carried movement ideas even where later positions differed;
- Sivaji's early stage work without payment;
- the beginning of a play-title/co-actor list.

### Important unresolved ranges in 12:00–16:00

Do not silently fill these from memory or historical knowledge:

1. the exact connective after the Krishna joke;
2. exact joins/inflections in the mock newspaper quotation;
3. `12:49–13:15`, where the captured machine chunk itself enters repeated-token collapse;
4. the retired postal official's exact name/title wording;
5. the locality/agraharam exchange around `13:28–14:00`;
6. part of the `14:00` house-owner/locality conclusion;
7. the ideological-position/gratitude sentence around `14:29–14:54`;
8. the complete play-title and co-actor list around `15:35–16:00`.

T. V. Narayanasamy/T.V.N. and K. R. Ramasamy are candidate anchors in the final list, not verified readings for that range.

## Exact next activity

Process **provisional Tamil T1 for `16:00–20:00`**.

Procedure:

1. continue exactly from the unresolved play-title/co-actor list at approximately `16:00`;
2. use the already captured right-channel independent chunk evidence as navigation;
3. add only wording stable enough for provisional T1;
4. mark uncertain names, titles, quotations and chunk joins explicitly;
5. update `transcription-ta.md`, `metadata.json`, `audit.md`, `README.md`, and this handover after the batch;
6. do **not** begin English;
7. do **not** call any machine-derived wording direct-listening verified.

## Later mandatory gates

After T1 reaches the true `00:26:22.080` end:

1. begin T2 at `00:00`, including the separate spoken lead-in and first-word verification;
2. directly audit every speech segment;
3. separately replay the final 60 seconds;
4. separately replay the final 30 seconds;
5. replay from the final major pause to the true file end;
6. confirm the final audible word and grammatical completeness;
7. only then perform T3 consolidation/freeze;
8. only after verified Tamil may English E1 begin.
