# Direct-listening retry manifest — opening gate + early checked-but-not-passed ranges

**Archive:** `speeches/kalaivanar-nsk-memorial-day-audio-06/`  
**Evidence class:** focused replay preparation only — **NOT new T2 evidence**  
**T2 counters:** unchanged at **22 checked / 14 passed**  
**Canonical Tamil changes:** **0**

## Controlling source

- filename: `06.Kalavaivannar N.S.Krishnnan Ninavul Naal Vizha Vil Kaligar Speech.mp3`;
- SHA-256: `6f0149229196b1d6df092d9fee006253591afec7ba9512bfbeb46dd0ab82c836`;
- byte size: `25,313,377`;
- decoded duration: `00:26:22.080`;
- audio: MP3, stereo, 44.1 kHz, approximately 128 kb/s.

The source checksum was freshly recomputed before these retry derivatives were made.

## Why this packet exists

The first direct-listening iteration left the opening lead-in and seven ranges **checked but not passed**. The already-passed material is not reopened here. Each retry crop is intentionally limited to the smallest conservative interval supported by the durable audit/transcript notes.

## Focused retry derivatives

| Retry | Source record | Interval | Duration | WAV bytes | SHA-256 | Audible target |
|---:|---|---|---:|---:|---|---|
| 1 | Batch 43 lead-in | `00:00–00:14.500` | 14.500s | 2,557,878 | `5c3f6a4899bab31ffba26d33fda614953ed4ec9df2f11d1d5de72071b41f4c5b` | first short announcer phrase + short hall-description phrase |
| 2 | Batch 44 | `01:16–02:34` | 78.000s | 13,759,278 | `ee3430a1d9ad6c70a0d3870d3493b573c354e609c62a4c98d2b32eb49c7a5a74` | conference/event name + later proper-name/closeness example |
| 3 | Batch 45 | `03:08–03:22` | 14.000s | 2,469,678 | `35a21e8bc08ca44d22ca78ba6f6cce2595ca03d2713dd59063fcd2cabbb01af2` | exact humorous affection/competition transition before `03:22` |
| 4 | Batch 47 | `04:48–05:14` | 26.000s | 4,586,478 | `ade0c8f93e9473a8d1d94dddffc92dc37ef332a150efa69569779458aec5b424` | Mekala-side contact/manager syntax + first joined-line exchange |
| 5 | Batch 48 | `05:14–05:55` | 41.000s | 7,232,478 | `32efb6c1b1825f0cc33e92e218116a13dea8bb4912d15903e5bf7863f45f3fd9` | crossed-line question/answer ordering + first short reply to `என்ன உணருகிறாய்?` |
| 6 | Batch 49 | `06:24–06:43` | 19.000s | 3,351,678 | `667937259bcebca7e154801d38112ae58f9763f5dfad981dc396521c4238d592` | hall/display phrase immediately before Kalaivanar's name |
| 7 | Batch 51 | `07:38–08:00` | 22.000s | 3,880,878 | `bf8ae4ee6f059a9afa0782a40d835c9f819cd3a18e95a81c5423c159c88b9cfe` | one unresolved praise word immediately before `எழுத்தாளர்` |
| 8 | Batch 52 | `08:05–08:34` | 29.000s | 5,115,678 | `d3d9e68c954a45819d9a2e44185415c18c9eaff60141c69534acf0d6f5f91655` | unresolved rhetorical question immediately before `தமிழ்நாட்டு வரலாறல்லவா?` |

The temporary PCM derivatives are **not committed**. Their hashes are retained so a later audible session can reproduce and identify the exact retry media.

## Durable retry state

Already passed and not reopened:

- Batch 46 / `03:22–04:00`;
- Batch 50 / `06:43–07:12`;
- Batch 53 / `08:38–09:25`;
- records 54–63 / `09:25–14:15` — all ten PASS.

Still requiring focused retry:

1. lead-in / Batch 43 segment 0;
2. Batch 44;
3. Batch 45;
4. Batch 47;
5. Batch 48;
6. Batch 49;
7. Batch 51;
8. Batch 52.

## Gate decision

This packet does **not** increment `checked` or `passed`.

The sequential active gate remains direct audible replay of ranges **22–31 / 14:15–20:00**. These retry crops may be replayed either before or after the remaining sequential ranges, but all eight must be resolved before T2 can close.