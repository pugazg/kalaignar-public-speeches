# Kalaignar Public Speeches

A source-first digital archive of public speeches by **M. Karunanidhi (Kalaignar)**.

The repository preserves each available source as evidence and separates four layers of work:

1. **Source record** - bibliographic and scan provenance.
2. **Tamil transcription** - faithful to the printed source; no silent modernization or correction.
3. **Verification** - page-by-page comparison against the scan, with uncertain readings explicitly marked or formally resolved.
4. **English translation** - started only after the Tamil transcription has passed the source audit.

## Editorial principles

- Preserve original spelling, punctuation, names, numbers, and wording wherever legible.
- Do not silently repair historical printing, grammar, or factual claims.
- Mark genuinely uncertain or damaged text instead of guessing.
- Keep publication date separate from speech date; do not infer an event date or venue when the source does not state one.
- Record the source filename and SHA-256 so later copies can be checked for identity.
- Treat advertisements and other back matter as source context, not as part of the speech transcript.

## Catalogue

| ID | Tamil title | Source edition | Speech date | Tamil transcription | English translation |
|---|---|---|---|---|---|
| `arappor` | அறப்போர் | Second edition, April 1949 | Not stated in source | **Strict-verified complete - 17/17 speech pages** | **Ready; not started** |

## Repository layout

```text
speeches/
  arappor/
    README.md
    metadata.json
    transcription-ta.md
    audit.md
```

Original scans should be retained unchanged whenever possible. Large/binary source files may be added separately; their checksum is recorded in each speech's metadata.
