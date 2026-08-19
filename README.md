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

The archival text workflow is complete for the full 32-page body: source inspection and page mapping, Tamil transcription, strict visual Tamil audit, Tamil consolidation/freeze, English translation, English fidelity review with all 19 confirmed corrections consolidated, and final end-to-end Tamil→English verification have all passed. Both Tamil and English layers are **`verified-complete`**.

The source is a printed multi-section booklet whose title page does not explicitly label it as `பேச்சு`; it is therefore archived as one source unit without inventing a single speech event. The scan does not establish a single speech date, venue, event, occasion or audience. The exact printer name on PDF page 3 also remains unresolved because a later library stamp obscures part of the printed line; this is a bibliographic limitation rather than pending text work.

### பூந்தோட்டம்

The archival workflow is complete for the 12-page speech body on PDF pages 6-17 / printed pages 5-16. The source explicitly states that தோழர் மு.கருணாநிதி delivered the speech at சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி on **06.12.1951**. It does not separately name an event/occasion or define the audience, so those fields remain unset.

Tamil transcription, strict visual audit, Tamil consolidation/freeze, English translation, independent fidelity review, and final end-to-end Tamil→English verification have all passed. Both Tamil and English layers are **`verified-complete`**. E2 produced one confirmed English correction; E3 found no additional correction. The source PDF is not committed under repository policy; provenance is preserved in metadata through filename, SHA-256, file size, page count and page map.

A later **post-freeze review of printed p.16** reopened both layers under documented evidence. A fresh inspection of the controlling scan established that the print reads `மாடப்புறா`, not the frozen `மாட்டுப்புறா`, giving one scan-confirmed Tamil correction; `மானிடம்`, previously left untranslated as an uncertain form, was established to be the ordinary noun for *humanity* and is now translated, with its note removed. Tamil was re-consolidated and re-frozen, and the dependent English layer was re-verified through a fresh E2 of the affected page plus a complete 12-page E3. Both layers remain **`verified-complete`**.

### பள்ளி வாழ்க்கை

The archival workflow is complete for the **76-page body on PDF pages 6-81 / printed pages 5-80**. The March 1952 first edition is a printed compilation rather than one securely identified single speech event. PDF page 5 says that speeches delivered by Kalaignar M. Karunanidhi at **திருவாரூர் நகராண்மைக் கழக உயர்நிலைப்பள்ளி** and **வேறு சில இடங்களிலும்** were collected by **தோழர் மு. நமச்சிவாயம்**. Component-speech dates and one common venue/event/occasion/audience are not supplied by the source and are therefore not inferred.

Tamil T1, strict visual T2, final Tamil consolidation/freeze T3, full English translation, 16-batch independent English fidelity review, and the final 76-page E3 Tamil→English verification have all passed. Both Tamil and English are **`verified-complete`**. E3 checked all 75 internal page transitions and found no additional correction after E2 consolidation.

The source uses traditional pre-1978 Tamil glyph forms; the archival Tamil resolves those to scan-supported underlying characters while retaining genuine source-supported irregular wording rather than silently modernizing it. Detailed T2 evidence and the T3 final verification record are retained with the speech. The source PDF is not committed; its filename, SHA-256, size, page count and page map remain preserved in metadata.

### கலைவாணர் என். எஸ். கிருஷ்ணன் நினைவு நாள் விழாவில் கலைஞர் உரை

The archival audio workflow is complete for the **443.559-second / 00:07:23.559** Tamil Digital Library MP3. Source identity is preserved through filename, URL, SHA-256, byte size and decoded technical metadata; the audio binary is not committed.

Tamil T1, strict direct-listening T2, Tamil consolidation/freeze T3, full English E1, four-batch English fidelity review E2, and continuous final Tamil→English verification E3 have all passed. Both Tamil and English are **`verified-complete`**.

A critical corrective audit restored the final approximately 25 seconds after an earlier false conclusion that the recording ended abruptly. The complete speech ends by describing any peace brought into the struggling recipients' lives as the offering Kalaignar places at Kalaivanar's feet. The controlling tail-correction record and a project learnings document are retained to prevent recurrence.

The recording establishes the venue as **கலைவாணர் அரங்கம், சென்னை** but does not state an exact speech date. Secondary chronology is retained only as context; `speech.date` remains `null`. E3 checked all 12 timestamp sections from the opening salutations through the true end and found no new correction after E2 consolidation.
