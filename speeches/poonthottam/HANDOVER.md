# கலைஞரின் பூந்தோட்டம் - final archival handover

The `speeches/poonthottam/` archive is complete. All mandatory gates in `SPEECH_PROCESSING_GUIDE.md` have passed, repository-level synchronization is complete, and no transcription or translation work remains pending.

## Repository

- Repository: `pugazg/kalaignar-public-speeches`
- Branch: `main`
- Speech directory: `speeches/poonthottam/`
- Stable slug: `poonthottam`

## Source identity

- Source filename: `TVA_BOK_0065784_கலைஞரின்_பூந்தோட்டம்.pdf`
- SHA-256: `2a8bf5f6f42970ee95912f41662f9bc448581a5aaca15a55fee9b44ba20a4c52`
- File size: `49,297,657` bytes
- PDF pages: `18`
- PDF 6-17 = speech body / printed 5-16 = **12 speech pages**
- Source binary committed: **No** — this is intentional repository policy, not pending work.

## Source-supported bibliographic facts

- Booklet title: `கலைஞரின் பூந்தோட்டம்`
- Speech heading: `பூந்தோட்டம்`
- Speaker attribution: `தோழர் மு.கருணாநிதி`
- Speech date explicitly stated by source: **06.12.1951**
- Venue explicitly stated by source: **சென்னை கிண்டி இன்ஜினியரிங் கல்லூரி**
- Named event / occasion: **not stated**
- Defined audience: **not stated**
- First-edition statement: `முதற்பதிப்பு - 1951 (திராவிடப் பண்ணை)`
- Current scanned edition: `நான்காம் பதிப்பு : 2019`

## Final gate status

- Source inspection / page map: **complete**
- T1 Tamil first pass: **12/12 complete**
- T2 strict visual Tamil audit: **12/12 complete**
- T3 Tamil consolidation / page-boundary / stale-reading check: **complete**
- Tamil canonical layer: **`verified-complete` and frozen**
- E1 English first pass: **12/12 complete**
- E2 independent Tamil→English fidelity review: **12/12 complete**
- E2 confirmed English corrections: **1**
- E3 final end-to-end Tamil→English verification: **12/12 complete**
- E3 internal page transitions checked: **11/11**
- E3 additional corrections: **0**
- English canonical layer: **`verified-complete`**
- **Post-freeze re-inspection (T4, printed p.16): complete - 1 Tamil correction; Tamil re-frozen**
- **Post-freeze English re-verification (fresh E2 of p.16 + full 12-page E3): complete - 2 English corrections**
- Speech `README.md` synchronization: **complete**
- `metadata.json` synchronization: **complete**
- Root catalogue / root `README.md` synchronization: **complete**
- Final archival handover: **complete**

## Important audit record

T2 made two scan-confirmed Tamil corrections on printed p.15:

- `புரிவோடு` → `பூரிப்போடு`
- `வளர்த்தான்` → `வளரத்தான்`

E2 made one confirmed English correction on PDF 10 / printed p.9. The final English translates the grammatical relation in:

`அவன் அண்ணன் அயோத்தியானுக்கு, தன் அண்ணன் இராவணனைக் காட்டிக் கொடுத்த...`

as Vibhishana betraying Ravana to **Bharata's elder brother, the Ayodhyan**. The frozen Tamil itself was not altered.

E3 found no further correction and confirmed no stale E1 wording survives.

## Post-freeze correction record (2026-08-19)

Both layers had been closed when two findings were raised against the final sentence on printed p.16. Both were handled under the post-freeze rules — documented evidence first, then dependent re-verification. **T1, T2 and E1 were not re-run.**

**Finding B - Tamil transcription defect (scan-decided).** The controlling scan was re-opened with its identity verified first (SHA-256 `2a8bf5f6…`, 49,297,657 bytes, 18 pages, matching the recorded provenance). PDF 17 was rendered at 400 and 600 dpi. The word after `குயில்,` shows one `ட` between `மா` and `ப்`, so the print reads **`மாடப்புறா`**, not the frozen `மாட்டுப்புறா`:

- `மாட்டுப்புறா` → **`மாடப்புறா`** (T4; Tamil re-consolidated and re-frozen).

`மானிடம்` and `தேன்சிட்டு`, recorded in the same T2 Batch 3 group, were re-confirmed as printed. Dictionary expectation did not decide this correction; the scan did.

**Finding A - English rendering only (Tamil unchanged).** `மானிடம்` had been left in Tamil script with a note claiming its referent was uncertain. It is an established noun for *humanity/mankind* and heads the closing subject list gathered by `எல்லாமே`, so:

- `மானிடம்` → **humanity**, and the unfounded translator note was removed;
- dependent on the T4 correction, *mattuppura* → **dove**.

**Dependent verification.** A fresh E2 of printed p.16 and a complete 12-page E3 re-run were performed. All 12 speech pages and all 11 internal transitions were re-checked; no other text changed in either layer; no stale `மாட்டுப்புறா`, *mattuppura* or untranslated `மானிடம்` survives in the canonical layers. Translator notes: 6 → 5.

Both layers are again **`verified-complete`**.

## Difficult source-supported forms retained transparently

The archive deliberately does not conjecturally normalize these verified source forms:

- `அகம்புற மென்ற அன்றலர்ந்த`
- `அயோத்தியானுக்கு`
- `தண்ட காரணயத்திலே`
- `பெய்ப்படி`
- `வழக்கு மன்றத்திற்கு`

`மானிடம்` was formerly listed here. The post-freeze review established it is an ordinary lexical item (*humanity*) rather than a difficult form; it is now translated and its note removed. The Tamil reading itself was re-confirmed against the scan and is unchanged.

Their handling is documented in `translation-en.md` and `translation-review.md` where relevant.

## Directory / PDF-policy verification

The archival directory contains the standard seven text/data files:

- `README.md`
- `metadata.json`
- `transcription-ta.md`
- `audit.md`
- `translation-en.md`
- `translation-review.md`
- `HANDOVER.md`

No source PDF is present in `speeches/poonthottam/`. The PDF's identity remains preserved in metadata through filename, SHA-256, size, page count and page map.

## Final state

**No transcription or translation work is pending for `poonthottam`.**

If this archive is revisited later, do not restart any completed stage. Reopen Tamil or English only if a newly documented source-based defect is established; any Tamil change after freeze requires dependent English re-verification.