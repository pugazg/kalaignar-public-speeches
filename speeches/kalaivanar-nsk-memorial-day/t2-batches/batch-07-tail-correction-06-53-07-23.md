# T2 Batch 7 — correction and direct audit of the final speech tail

**Source range:** 06:53–07:23.559  
**Status:** **Passed — replaces the false truncated-ending finding in Batch 6**

## Why this correction was required

The earlier audit stopped transcription after:

> `...வெங்கடாசலம் அவர்கள் எத்தகைய நிலையிலே இருக்கிறார் என்பதையும்—`

and incorrectly labelled the recording as ending abruptly. The repository owner correctly identified that approximately another 25 seconds of speech remained.

The reattached MP3 was inspected again from 06:20 through the true end. Its identity matches the archived controlling source:

- SHA-256: `7457004d3c3ee87722edfe6814e830d3521b834dcf29b4de45bb7174a2278148`
- File size: 7,087,106 bytes
- Decoded duration in the current inspection: 443.559 seconds / 00:07:23.559

## Method

1. Replayed 06:53 through the true end directly from the reattached MP3.
2. Replayed the last 35 seconds in shorter, slower and conservatively noise-reduced chunks.
3. Used a checksum-verified `large-v3-turbo` raw/enhanced decoding pass only as a secondary aid.
4. Treated the audible MP3 as authoritative when machine text was malformed.

## Corrected final passage

The complete audible ending is:

> பரிசுகளைப் பெற்றவர்களைக் கண்டீர்கள். தங்கப்பன் அவர்களும், பகவதி அவர்களும் எந்தக் கோலத்திலே இன்றைக்கு இருக்கிறார்கள் என்பதை நேரில் நீங்கள் உணர்ந்தீர்கள்.
>
> அதைப்போலவே பல்வேறு நாடகங்களிலே மிகத் திறம்பட நடித்த வெங்கடாசலம் அவர்கள் எத்தகைய நிலையிலே இருக்கிறார் என்பதையும் நீங்கள் அறிவீர்கள்.
>
> அவர்களுக்கெல்லாம் நாம் செய்கின்ற இந்தச் சிறு உதவி, அவர்களுடைய வாழ்க்கையிலே ஓரளவு நிம்மதியாவது ஏற்படுத்துமேயானால், அந்த நிம்மதிதான் கலைவாணருடைய காலடியிலே நான் வைக்கின்ற காணிக்கை என்று மாத்திரம் நான் குறிப்பிட்டுக் கொள்ள விரும்புகின்றேன்.

## Decisions

- The claim that the source ends abruptly is withdrawn.
- Segment 12 now ends at approximately `07:23.559`.
- The final sentence is complete and must not carry an em dash or truncation notice.
- The canonical transcript, audit, metadata, README and handover must all use the corrected ending.
- Batch 6 is superseded only on its final-boundary finding; Batch 7 is the controlling record for 06:53–07:23.559.
