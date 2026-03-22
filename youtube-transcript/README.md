# youtube-transcript

Download YouTube video transcripts, subtitles, and cover images. Supports multiple languages, chapters, speaker identification, translation, and SRT output.

[中文版](./README_CN.md)

Based on [baoyu-youtube-transcript](https://github.com/JimLiu/baoyu-skills) by JimLiu — rewritten as a slim skill to reduce token overhead.

---

## What It Does

- Downloads transcripts from YouTube via InnerTube API (no API key needed)
- Supports manual and auto-generated captions
- Outputs markdown or SRT format
- Caches results for fast re-formatting
- Speaker identification via AI post-processing

## Quick Start

```bash
# Basic transcript
bun scripts/main.ts 'https://www.youtube.com/watch?v=VIDEO_ID'

# With chapters + speakers (richest output)
bun scripts/main.ts 'https://youtu.be/VIDEO_ID' --chapters --speakers

# Chinese subtitles with translation fallback
bun scripts/main.ts 'URL' --languages zh,en --translate zh-Hans

# SRT format
bun scripts/main.ts 'URL' --format srt

# List available languages
bun scripts/main.ts 'URL' --list
```

## Eval Results

Compared slim SKILL.md (3.3KB) vs original (8.8KB) across 5 test cases using MiniMax-M2.7:

| Metric | Slim | Original | Change |
|--------|------|----------|--------|
| SKILL.md size | 3.3KB | 8.8KB | **-62%** |
| Total tokens | 27,853 | 40,988 | **-32%** |
| Total runtime | 116s | 152s | **-24%** |
| Success rate | 5/5 | 5/5 | Same |

**Verdict:** Identical correctness with 62% less context, 32% fewer tokens, and 24% faster execution. No functional regression.

<details>
<summary>Eval details</summary>

| # | Prompt | Slim | Original | Result |
|---|--------|------|----------|--------|
| 1 | Basic transcript fetch | ✅ Correct flags, single-quoted URL | ✅ Same | PASS |
| 2 | Chinese subtitles + translation | ✅ `--languages zh,en --translate zh-Hans` | ✅ Same | PASS |
| 3 | SRT without timestamps | ✅ `--format srt --no-timestamps` | ✅ Same | PASS |
| 4 | List available languages | ✅ `--list` | ✅ Same | PASS |
| 5 | Re-download with cache refresh | ✅ `--refresh` | ✅ Same | PASS |

Full results: [evals/results.json](./evals/results.json)
</details>

---

## Note on README Files

The `README.md` and `README_CN.md` files are for human reference only. OpenClaw agents only read `SKILL.md`. Feel free to delete READMEs after copying the skill.

## License

MIT
