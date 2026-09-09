# Workflow Prompts and Source-Specific Guidance

Use the repository-level `SPEECH_PROCESSING_GUIDE.md` for every speech.

## Starting prompts

- **PDF / scanned print source:** [`START_NEW_PDF_SPEECH_PROMPT.md`](START_NEW_PDF_SPEECH_PROMPT.md)
- **Audio source:** [`START_NEW_AUDIO_SPEECH_PROMPT.md`](START_NEW_AUDIO_SPEECH_PROMPT.md)

## Audio-specific guidance

- [`FUTURE_AUDIO_SPEECH_GUIDELINES.md`](FUTURE_AUDIO_SPEECH_GUIDELINES.md)
- root [`AUDIO_SPEECH_PROCESSING_GUIDE.md`](../AUDIO_SPEECH_PROCESSING_GUIDE.md)

## Multi-speech PDF volumes

A PDF containing multiple speeches or event texts must first receive a collection/source record under `collections/<stable-collection-slug>/`. Do not treat the whole volume as a single speech. Map each constituent item's exact printed-page and PDF-scan range, then archive each constituent separately under `speeches/<stable-speech-slug>/`.

The first collection using this model is `collections/muthukkuliyal-part-2/`.
