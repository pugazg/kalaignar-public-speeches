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
```

## Completed works

### அறப்போர்

The archival text workflow is complete: source identification, 17-page Tamil transcription, strict visual fidelity audit, English translation, English fidelity review, and final Tamil→English verification have all passed. The supplied source itself does not establish the original speech date, venue, or event, so those fields remain deliberately unset.
