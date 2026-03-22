---
name: youtube-transcript
description: Download YouTube video transcripts/subtitles and cover images. Use when user says "get transcript", "download subtitles", "get captions", "YouTube字幕", or provides a YouTube URL wanting text extracted. Also triggers on requests for video cover images, speaker identification, or subtitle translation.
version: 1.0.0
author: winoooops
original_author: JimLiu (https://github.com/JimLiu/baoyu-skills)
tags:
  - youtube
  - transcript
  - subtitles
---

# YouTube Transcript

Download transcripts from YouTube videos via InnerTube API. No API key needed.

## Setup

Resolve `${BUN_X}`: if `bun` installed → `bun`; else → `npx -y bun`. `{baseDir}` = this SKILL.md's directory.

## Commands

```bash
# Basic transcript (markdown with timestamps)
${BUN_X} {baseDir}/scripts/main.ts '<youtube-url-or-id>'

# List available languages
${BUN_X} {baseDir}/scripts/main.ts '<url>' --list

# Specify language
${BUN_X} {baseDir}/scripts/main.ts '<url>' --languages zh,en,ja

# With chapters + speaker identification (richest output)
${BUN_X} {baseDir}/scripts/main.ts '<url>' --chapters --speakers

# SRT subtitle format
${BUN_X} {baseDir}/scripts/main.ts '<url>' --format srt

# No timestamps / translate / force refresh
${BUN_X} {baseDir}/scripts/main.ts '<url>' --no-timestamps
${BUN_X} {baseDir}/scripts/main.ts '<url>' --translate zh-Hans
${BUN_X} {baseDir}/scripts/main.ts '<url>' --refresh
```

**Always single-quote URLs** — zsh treats `?` as a glob wildcard.

## Key Options

| Option | Description |
|--------|-------------|
| `--languages <codes>` | Comma-separated language codes, priority order (default: `en`) |
| `--format srt` | Output SRT instead of markdown |
| `--chapters` | Segment by chapter timestamps from description |
| `--speakers` | Raw output for AI speaker identification (implies chapters) |
| `--translate <code>` | Translate to specified language |
| `--no-timestamps` | Omit timestamps |
| `--list` | List available transcripts (stdout only) |
| `--refresh` | Ignore cache, re-fetch |
| `-o <path>` | Save to specific file |

## Output

Files cached under `youtube-transcript/{channel-slug}/{title-slug}/`:
- `meta.json` — video metadata
- `transcript-raw.json` — raw snippets from API
- `transcript-sentences.json` — sentence-segmented
- `imgs/cover.jpg` — thumbnail
- `transcript.md` or `transcript.srt` — final output

Subsequent runs reuse cache. Use `--refresh` to force re-fetch.

## Speaker Identification Workflow

When using `--speakers`, the script outputs a raw `.md` with metadata + SRT transcript. After saving:

1. Read the saved `.md` file
2. Read `{baseDir}/prompts/speaker-transcript.md`
3. Spawn a sub-agent (cheap model) to process: identify speakers from metadata, label turns with `**Speaker:**`, group into chapters with timestamps
4. Overwrite the `.md` with processed output

## Workflow

1. If language unknown, run `--list` first
2. Default to `--chapters --speakers` for richest output
3. Script auto-saves and prints file path
4. For `--speakers`: follow speaker identification workflow above

## Errors

| Error | Meaning |
|-------|---------|
| Transcripts disabled | No captions on video |
| No transcript found | Requested language unavailable |
| Video unavailable | Deleted, private, or region-locked |
| IP blocked | Rate limited, retry later |
