# Direct-listening replay manifest — T2 ranges 22–31

**Archive:** `speeches/kalaivanar-nsk-memorial-day-audio-06/`  
**Target:** precheck ranges `22–31` / `14:15–20:00`  
**Evidence class:** replay preparation only — **NOT T2 direct-listening evidence**  
**T2 counters:** unchanged at **22 checked / 14 passed**  
**Canonical Tamil changes:** **0**

## Controlling source

- filename: `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`;
- SHA-256: `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`;
- byte size: `25,313,377`;
- decoded duration: `00:26:22.080`;
- audio: MP3, stereo, 44.1 kHz, 128 kb/s.

The source identity was freshly recomputed from the reattached binary before creating the replay derivatives.

## Temporary replay derivatives

Ten sample-accurate stereo PCM WAV clips were decoded from the controlling MP3 with the following form:

```bash
ffmpeg -i "$SOURCE" -ss <START> -to <END> -map 0:a:0 -c:a pcm_s16le <OUTPUT.wav>
```

The derivatives are **not committed**, in accordance with repository media policy. Their hashes are recorded only to make any replay session reproducible.

| Range | Interval | Duration | WAV bytes | SHA-256 |
|---:|---|---:|---:|---|
| 22 | `14:15–14:59` | 44.000s | 7,761,678 | `8b0b43aa2235bf377143f05e9bfdfe1ecd6c7bcc38274cae60ffe0e1d8617fd9` |
| 23 | `14:59–15:35` | 36.000s | 6,350,478 | `120527391ed07ed8a19012a9b05e4cb15313edec1402c6f26f966c4889b8aab3` |
| 24 | `15:35–16:00` | 25.000s | 4,410,078 | `907f9e68dd9576aa16b9cb8efd4eb24c5215b9455f9900fd2c84957aba82ff60` |
| 25 | `16:00–16:30` | 30.000s | 5,292,078 | `f3edab6d63e870cd663665ead211b2fb7c9acf1a210e43f85a4ebe27c2b2330a` |
| 26 | `16:30–17:15` | 45.000s | 7,938,078 | `8558c165e015ba6029fd979b5f2d1de96dec487e61b6915819c34c6813b05d54` |
| 27 | `17:15–17:47` | 32.000s | 5,644,878 | `a5bcf9f6180ca028055d9aace19890e7e91f5dd806e9c434edb59571e8fd8ec0` |
| 28 | `17:47–18:00` | 13.000s | 2,293,278 | `fd12b65a9c91efad3696c1a24971b41faffa13cf04198204f8a2a2f520f5e0a3` |
| 29 | `18:00–19:00` | 60.000s | 10,584,078 | `3f04f9cf42f54de5c7669128d508b293f2a7a2d305ff128fa7f8f62cba425d7b` |
| 30 | `19:00–19:33` | 33.000s | 5,821,278 | `4c9950ea9f2aae0f0a66b0308972e63c083989a996850701219f6934a373e384` |
| 31 | `19:33–20:00` | 27.000s | 4,762,878 | `f78db85fd200903221e2d4bec2f223925c5ed8578a2e5aa7b22b1fa910f3a1a6` |

## Mandatory replay aids

Use these existing candidate-only records for navigation, never as source authority:

- `companion-transcript-crosscheck-ranges-22-31.md`;
- `dual-witness-discrepancy-ledger-ranges-22-31.md`;
- precheck records `batch-22-14-15-14-59-precheck.md` through `batch-31-19-33-20-00-precheck.md`.

Highest-risk replay targets remain:

1. range 24 — fund labels and co-actor identities;
2. range 28 — exact spoken Kural opening;
3. range 31 — Prahlada/Hiranya/Abdullah Gandhi wording;
4. range 23 — reversal-joke adjective and subject form;
5. range 22 — `ஆதாயம்` and gratitude syntax;
6. range 30 — movement terminology and compassion clause.

## Gate decision

This preparation does not satisfy T2. Do not mark any range checked or passed until a listener replays the controlling audio and verifies every word, name, number, repetition and boundary.

Exact next activity remains:

- replay ranges 22–31 directly;
- create direct-listening records 64–73;
- record checked/passed/unresolved state for each range;
- update `transcription-ta.md` only where audible replay supports the wording;
- synchronize `audit.md`, `metadata.json`, `README.md`, `HANDOVER.md`, root control documents and counters.
