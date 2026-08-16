# Kalaignar Public Speeches

A source-first digital archive of public speeches by **M. Karunanidhi (Kalaignar)**.

The repository preserves each available source as evidence and separates four layers of work:

1. **Source record** - bibliographic and scan provenance.
2. **Tamil transcription** - faithful to the printed source; no silent modernization or correction.
3. **Verification** - page-by-page comparison against the scan, with uncertain readings explicitly marked or formally resolved.
4. **English translation** - started only after the Tamil transcription has passed the source audit, then fidelity-reviewed against that verified Tamil layer.

## Processing guide

**Before starting or continuing any speech, read [`SPEECH_PROCESSING_GUIDE.md`](SPEECH_PROCESSING_GUIDE.md) completely.** It defines the mandatory source-inspection, Tamil transcription, visual-fidelity, translation, review, verification, handover, and closure workflow established through the completed `அறப்போர்` archive.

## Editorial principles

- Preserve original spelling, punctuation, names, numbers, and wording wherever legible.
- Do not silently repair historical printing, grammar, or factual claims.
- Mark genuinely uncertain or damaged text instead of guessing.
- Keep publication date separate from speech date; do not infer an event date or venue when the source does not state one.
- Record the source filename and SHA-256 so later copies can be checked for identity.
- Treat advertisements and other back matter as source context, not as part of the speech transcript.
- Keep English translation subordinate to the verified Tamil source layer; translation must not be used to silently rewrite the archival transcription.
- Source PDFs are **not uploaded to this GitHub repository**. Preserve their identity through provenance metadata, checksum, size, and page mapping.

## Catalogue

| ID | Tamil title | Source edition | Speech date | Tamil transcription | English translation |
|---|---|---|---|---|---|
| `arappor` | அறப்போர் | Second edition, April 1949 | Not stated in source | **Verified complete - 17/17 speech pages** | **Verified complete - 17/17 speech pages** |
| `idhaya-perikai` | இதய பேரிகை | First edition, December 1951 | Not stated in source | **Verified complete - 32/32 body pages** | **Verified complete - 32/32 body pages** |
| `poonthottam` | பூந்தோட்டம் | Fourth edition, 2019; first edition 1951 | 06.12.1951 | **Verified complete - 12/12 speech pages** | **Verified complete - 12/12 speech pages** |
| `palli-vazhkkai` | பள்ளி வாழ்க்கை | First edition, March 1952 | Not stated as a single speech date; compilation source | **Verified complete - 76/76 body pages** | **Verified complete - 76/76 body pages** |

## Repository layout

```text
SPEECH_PROCESSING_GUIDE.md
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
```

## Completed works

### அறப்போர்

The archival text workflow is complete: source identification, 17-page Tamil transcription, strict visual fidelity audit, English translation, English fidelity review, and final Tamil→English verification have all passed. The supplied source itself does not establish the original speech date, venue, or event, so those fields remain deliberately unset.

### இதய பேரிகை

The archival text workflow is complete for the full 32-page body: source inspection and page mapping, Tamil transcription, strict visual Tamil audit, Tamil consolidation/freeze, English translation, English fidelity review with all 19 confirmed corrections consolidated, and final end-to-end Tamil→English verification have all passed. Both Tamil and English layers are **`verified-complete`**.

The source is a printed multi-section booklet whose title page does not explicitly label it as `பேச்சு`; it is therefore archived as one source unit without inventing a single speech event. The scan does not establish a single speech date, venue, event, occasion, or audience. The exact printer name on PDF page 3 also remains unresolved because a later library stamp obscures part of the printed line; this is a bibliographic limitation rather than pending text work.

### பூந்தோட்டம்

The archival workflow is complete for the 12-page speech body on PDF pages 6-17 / printed pages 5-16. The source explicitly states that தோழர் மு.கருணாநிதி delivered the speech at சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி on **06.12.1951**. It does not separately name an event/occasion or define the audience, so those fields remain unset.

Tamil transcription, strict visual audit, Tamil consolidation/freeze, English translation, independent fidelity review, and final end-to-end Tamil→English verification have all passed. Both Tamil and English layers are **`verified-complete`**. E2 produced one confirmed English correction; E3 found no additional correction. The source PDF is not committed under repository policy; provenance is preserved in metadata through filename, SHA-256, file size, page count, and page map.

### பள்ளி வாழ்க்கை

The archival workflow is complete for the **76-page body on PDF pages 6-81 / printed pages 5-80**. The March 1952 first edition is a printed compilation rather than one securely identified single speech event. PDF page 5 says that speeches delivered by Kalaignar M. Karunanidhi at **திருவாரூர் நகராண்மைக் கழக உயர்நிலைப்பள்ளி** and **வேறு சில இடங்களிலும்** were collected by **தோழர் மு. நமச்சிவாயம்**. Component-speech dates and one common venue/event/occasion/audience are not supplied by the source and are therefore not inferred.

Tamil T1, strict visual T2, final Tamil consolidation/freeze T3, full English translation, 16-batch independent English fidelity review, and the final 76-page E3 Tamil→English verification have all passed. Both Tamil and English are **`verified-complete`**. E3 checked all 75 internal page transitions and found no additional correction after E2 consolidation.

The source uses traditional pre-1978 Tamil glyph forms; the archival Tamil resolves those to scan-supported underlying characters while retaining genuine source-supported irregular wording rather than silently modernizing it. Detailed T2 evidence and the T3 final verification record are retained with the speech. The source PDF is not committed; its filename, SHA-256, size, page count, and page map remain preserved in metadata.
