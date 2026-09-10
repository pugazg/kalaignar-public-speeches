# Kalaignar Public Speeches

A source-first digital archive of public speeches by **M. Karunanidhi (Kalaignar)**.

The repository preserves each available source as evidence and separates four layers of work:

1. **Source record** - bibliographic and media provenance.
2. **Tamil transcription** - faithful to the controlling source; no silent modernization or correction.
3. **Verification** - direct comparison against the controlling source, with uncertain readings explicitly marked or formally resolved.
4. **English translation** - started only after the Tamil transcription has passed the source audit, then fidelity-reviewed against that verified Tamil layer.

## Processing guides

**Before starting or continuing any speech, read [`SPEECH_PROCESSING_GUIDE.md`](SPEECH_PROCESSING_GUIDE.md) completely.** It defines the mandatory source-inspection, Tamil transcription, fidelity, translation, review, verification, handover and closure workflow established through the completed `அறப்போர்` archive.

For audio or video sources, also read:

- [`AUDIO_SPEECH_PROCESSING_GUIDE.md`](AUDIO_SPEECH_PROCESSING_GUIDE.md)
- [`docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md`](docs/FUTURE_AUDIO_SPEECH_GUIDELINES.md)

## Editorial principles

- Preserve original spelling, punctuation, names, numbers and wording wherever supported by the controlling source.
- Do not silently repair historical printing, grammar, spoken forms or factual claims.
- Mark genuinely uncertain or damaged text instead of guessing.
- Keep publication/file dates separate from speech dates; do not infer an event date or venue when the source does not establish one.
- Record source filenames and SHA-256 checksums so later copies can be checked for identity.
- Keep English translation subordinate to the verified Tamil source layer; translation must not be used to silently rewrite the archival transcription.
- Source PDFs and source audio binaries are **not uploaded to this GitHub repository**. Preserve their identity through provenance metadata, checksum, size, page mapping or decoded duration as applicable.

## Catalogue

| ID | Tamil title | Source edition/media | Speech date | Tamil transcription | English translation |
|---|---|---|---|---|---|
| `arappor` | அறப்போர் | Second edition, April 1949 | Not stated in source | **Verified complete - 17/17 speech pages** | **Verified complete - 17/17 speech pages** |
| `idhaya-perikai` | இதய பேரிகை | First edition, December 1951 | Not stated in source | **Verified complete - 32/32 body pages** | **Verified complete - 32/32 body pages** |
| `poonthottam` | பூந்தோட்டம் | Fourth edition, 2019; first edition 1951 | 06.12.1951 | **Verified complete - 12/12 speech pages** | **Verified complete - 12/12 speech pages** |
| `palli-vazhkkai` | பள்ளி வாழ்க்கை | First edition, March 1952 | Not stated as a single speech date; compilation source | **Verified complete - 76/76 body pages** | **Verified complete - 76/76 body pages** |
| `kalaivanar-nsk-memorial-day` | கலைவாணர் என். எஸ். கிருஷ்ணன் நினைவு நாள் விழாவில் கலைஞர் உரை | Tamil Digital Library MP3, 00:07:23.559 | Not stated in source | **Verified complete - 12/12 audio segments** | **Verified complete - 12/12 timestamp sections** |
| `desiya-ilainjar-kondatta-thodakka-vizha` | தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா | `முத்துக் குளியல் — பாகம் II`, first edition June 2000; constituent pp.11–17 | 12.01.1998 | **Verified complete - 7/7 speech pages** | **Verified complete - 7/7 speech pages** |
| `murasoli-arakkattalai-virudhu-vazhangu-vizha` | முரசொலி அறக்கட்டளை விருது வழங்கு விழா | `முத்துக் குளியல் — பாகம் II`, first edition June 2000; constituent pp.18–32 | 13.01.1998 | **Verified complete - 15/15 speech pages** | **Verified complete - 15/15 speech pages** |
| `thiruvalluvar-vizha` | திருவள்ளுவர் விழா | `முத்துக் குளியல் — பாகம் II`, first edition June 2000; constituent pp.33–48 | 15.01.1998 | **Verified complete - 16/16 speech pages** | **Verified complete - 16/16 speech pages** |
| `indiya-suvishesha-thiruchabai-vizha` | இந்திய சுவிசேஷத் திருச்சபை விழா | `முத்துக் குளியல் — பாகம் II`, first edition June 2000; constituent pp.49–52 | 16.01.1998 | **Verified complete - 4/4 speech pages** | **Verified complete - 4/4 speech pages** |

## Repository layout

```text
SPEECH_PROCESSING_GUIDE.md
AUDIO_SPEECH_PROCESSING_GUIDE.md
docs/
  FUTURE_AUDIO_SPEECH_GUIDELINES.md
  START_NEW_AUDIO_SPEECH_PROMPT.md
speeches/
  arappor/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
    translation-en.md
    translation-review.md
    HANDOVER.md
  idhaya-perikai/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
    translation-en.md
    translation-review.md
    HANDOVER.md
  poonthottam/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
    translation-en.md
    translation-review.md
    HANDOVER.md
  palli-vazhkkai/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
    t2-batches/
    t3-final-verification.md
    translation-en.md
    translation-review.md
    HANDOVER.md
  kalaivanar-nsk-memorial-day/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
    t2-batches/
    translation-en.md
    translation-review.md
    e3-final-verification.md
    LEARNINGS.md
    HANDOVER.md
```

## Completed works

### அறப்போர்

The archival text workflow is complete: source identification, 17-page Tamil transcription, strict visual fidelity audit, English translation, English fidelity review, and final Tamil→English verification have all passed. The supplied source itself does not establish the original speech date, venue or event, so those fields remain deliberately unset.

### இதய பேரிகை

The archival workflow is complete for the full 32-page body: source inspection and page mapping, Tamil transcription, strict visual Tamil audit, Tamil consolidation/freeze, English translation, English fidelity review with all 19 confirmed corrections consolidated, and final end-to-end Tamil→English verification have all passed. Both Tamil and English layers are **`verified-complete`**.

### பூந்தோட்டம்

The archival workflow is complete for the 12-page speech body on PDF pages 6-17 / printed pages 5-16. Both Tamil and English layers are **`verified-complete`**.

### பள்ளி வாழ்க்கை

The archival workflow is complete for the **76-page body on PDF pages 6-81 / printed pages 5-80**. Both Tamil and English are **`verified-complete`**.

### கலைவாணர் என். எஸ். கிருஷ்ணன் நினைவு நாள் விழாவில் கலைஞர் உரை

The archival audio workflow is complete for the **443.559-second / 00:07:23.559** Tamil Digital Library MP3. Both Tamil and English are **`verified-complete`**.

### தேசிய இளைஞர் கொண்டாட்டத் தொடக்க விழா

The archival workflow is complete for constituent **1 / 36** of `முத்துக் குளியல் — பாகம் II`, covering PDF **12–18** / printed pages **11–17**. Repository-level closure is complete.

### முரசொலி அறக்கட்டளை விருது வழங்கு விழா

The archival workflow is complete for constituent **2 / 36** of `முத்துக் குளியல் — பாகம் II`, covering PDF **19–33** / printed pages **18–32**. Repository-level closure is complete.

### திருவள்ளுவர் விழா

The archival workflow is complete for constituent **3 / 36** of `முத்துக் குளியல் — பாகம் II`, covering PDF **34–49** / printed pages **33–48**. Repository-level closure is complete.

### இந்திய சுவிசேஷத் திருச்சபை விழா

The archival workflow is complete for constituent **4 / 36** of `முத்துக் குளியல் — பாகம் II`, covering PDF **50–53** / printed pages **49–52**. Repository-level closure is complete.
