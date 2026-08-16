# Machine-aided audio evidence — 00:00–01:30

**Primary focus:** segments 1–3 and the segment 3→4 boundary  
**Status:** **Machine-aided auditory pre-audit complete; strict human/direct-listening verification not complete**

## Controlling source

- Source: `05.Kalaivanar N.S.Krishnan Ninnaivu Naal Vizha vil Kalaigar Speech.mp3`
- Expected SHA-256: `7457004d3c3ee87722edfe6814e830d3521b834dcf29b4de45bb7174a2278148`
- The workflow downloaded the public source independently and obtained the expected checksum in every run.
- The MP3 was processed transiently inside GitHub Actions and was not committed to the repository or included in an artifact.

## Evidence runs

### Run 1 — Whisper small and medium

- Workflow run: `31949005627`
- Commit: `b1cb77b6b3c10e4f0cde6f4511e43f264b4cf989`
- Window: `00:00–01:06`
- Models: multilingual Whisper `small` and `medium`, CPU `int8`
- Artifact: `kalaivanar-audio-audit-segments-1-3`
- Artifact ID: `9264133443`
- Artifact digest: `sha256:8fd0773c534a1c4365462ad12abc0c628e30e8b05f2b2850193ab7035a518dbb`

### Run 2 — Whisper large-v3-turbo

- Workflow run: `31949187567`
- Commit: `c631ea4458e67b9988e7878ebc0d72b7780740c0`
- Window: `00:00–01:06`
- Model: multilingual Whisper `large-v3-turbo`, CPU `int8`
- Inputs: raw mono extraction and conservatively speech-enhanced extraction
- Artifact: `kalaivanar-audio-audit-turbo-segments-1-3`
- Artifact ID: `9264188366`
- Artifact digest: `sha256:43f00bb87e381b88799b3cf0c31f40fd0510a25cf5b8a4573965d40b58025747`

### Run 3 — boundary recheck

- Workflow run: `31949410974`
- Commit: `17092602c15f22ae91888c6010b71607f7d4e79b`
- Window: `00:45–01:30`
- Model: multilingual Whisper `large-v3-turbo`, CPU `int8`
- Inputs: raw and speech-enhanced
- Artifact: `kalaivanar-audio-boundary-00-45-01-30`
- Artifact ID: `9264237487`
- Artifact digest: `sha256:4797ef0c375b38deeac448daf1562d8c79c024ef0771b5598902ec33d2d38a0e`
- Additional evidence: silence detection at `-38 dB`, minimum duration `0.20 s`

## Findings

### Segment 1 — opening salutations

Across the stronger `medium` and `large-v3-turbo` outputs, the audio structure supports:

- `கலைவாணர் நினைவுக் குழுவின் தலைவர்`;
- an `அருமை நண்பர் ... அவர்களே` first addressee;
- `அருமை நண்பர் சின்ன அண்ணாமலை அவர்களே`;
- `கலையுலகப் பெருமக்களே`;
- `தாய்மார்களே, நண்பர்களே`.

The models do **not** reliably decode the first personal name. The large-v3-turbo raw output produces an approximate phonetic form beginning with an `ஏ...எல்...`-like sequence followed by an `ச...`-like name, which is compatible with the provisional `[ஏ. எல். சீனிவாசன்?]`, but this is not sufficient to remove the uncertainty marker.

Decision:

- retain `[ஏ. எல். சீனிவாசன்?]`;
- do not mark segment 1 strict-verified;
- revise only the following segment start from provisional `00:20` to approximately `00:18`, based on model boundaries and silence structure.

### Segment 2 — annual memorial function

The model consensus supports the structure and sequence of the current T1:

- `ஆண்டு தோறும் நடைபெறுகின்ற`;
- `கலைவாணர் நினைவு நாள் விழா`;
- `இந்த ஆண்டும்`;
- a phrase acoustically corresponding to `மெத்த உணர்ச்சிப் பெருக்கோடும்`;
- `கலைவாணரை நினைவுகூர்ந்து`;
- `அவர் விட்டுச் சென்ற பணிகளைத் தொடர்ந்து செய்திட வேண்டும்`;
- a phrase corresponding to `பேரார்வத்தோடும்`;
- `நான் மிகவும் மகிழ்ச்சியடைகின்றேன்`.

The models make predictable old-recording/Tamil ASR substitutions such as `மற்ற/நட்ட` for `மெத்த`, `பொறுக்கோடும்/பெடுக்கோடும்` for `பெருக்கோடும்`, and approximate forms for `பேரார்வத்தோடும்`. These outputs support the passage phonetically but do not independently certify every inflection.

Decision:

- retain the current Tamil wording unchanged;
- move the segment start to approximately `00:18`;
- move the next segment start from provisional `00:50` to approximately `00:55`;
- do not mark segment 2 strict-verified.

### Segment 3 — gratitude sentence

All stronger passes support the substance of:

> `கலைவாணர் அவர்களுக்கு நாம் செலுத்த வேண்டிய நன்றியினை இந்த ஒரு வகையிலேதான் செலுத்திட முடியும் என்பதை நான் சுட்டிக்காட்டாமல் இருக்க இயலாது.`

The extended boundary run is especially important. Both raw and enhanced large-v3-turbo outputs recover the sentence in two parts:

- approximately `00:55–01:05`: `கலைவாணர் அவர்களுக்கு நாம் செலுத்த வேண்டிய நன்றியினை இந்த ஒரு வகையிலேதான் செலுத்திட முடியும்`;
- approximately `01:06–01:10`: `என்பதை நான் சுட்டிக்காட்டாமல் இருக்க இயலாது`.

The earlier 66-second extraction ended before the sentence completed. The old provisional boundary `01:06` therefore split one sentence incorrectly.

### Segment 3→4 boundary

Evidence supports:

- gratitude sentence ending at approximately `01:10.18`;
- silence after the sentence;
- `கலைவாணருடைய குடும்பம்...` beginning at approximately `01:11.24` in the raw pass, with the enhanced pass beginning near `01:10.18` because preprocessing shortened the apparent pause;
- silence detection showing a substantial pause around `01:10.20–01:11.76`.

Decision:

- change the navigation heading for segment 4 from provisional `01:06` to `01:11`;
- change the segment 3 end to approximately `01:11` in metadata;
- preserve the Tamil wording unchanged;
- do not mark segment 3 or segment 4 strict-verified solely from ASR.

## Corrected navigation map for the opening

| Segment | Previous provisional range | Machine-evidence navigation range | Status |
|---:|---|---|---|
| 1 | 00:00–00:20 | approximately 00:00–00:18 | wording audit pending |
| 2 | 00:20–00:50 | approximately 00:18–00:55 | wording audit pending |
| 3 | 00:50–01:06 | approximately 00:55–01:11 | wording audit pending |
| 4 | began 01:06 | begins approximately 01:11 | boundary corrected; wording audit pending |

These are navigation markers, not word-perfect timestamp claims.

## Audit decision

- Machine-aided auditory pre-audit for segments 1–3: **complete**.
- Time-boundary correction: **supported and may be consolidated**.
- Tamil wording corrections: **none authorized**.
- Strict auditory T2 segments passed: **0/12**.
- The first addressee, exact inflections, audience reactions, and other fine-grained details remain direct-listening checkpoints.
- English translation remains blocked.
