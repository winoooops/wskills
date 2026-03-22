# wskills

An opinionated collection of AI agent skills.

[中文版](./README_CN.md)

---

## Skills

### eval-runner

Run structured evals on any OpenClaw skill. Spawns subagents with and without the skill to compare performance — measures time, token usage, and success rate. Useful for skill development and optimization.

➡️ [Details](./eval-runner/)

### youtube-transcript

Download YouTube video transcripts, subtitles, and cover images. Supports multiple languages, chapters, speaker identification, and SRT output. Slim rewrite of [baoyu-youtube-transcript](https://github.com/JimLiu/baoyu-skills) — 62% smaller SKILL.md with identical correctness.

➡️ [Details](./youtube-transcript/)

---

## Usage

To install a skill, copy its folder into your OpenClaw skills directory. For example, to install `eval-runner`:

```bash
cp -r eval-runner ~/.openclaw/skills/
```

Or symlink for development:

```bash
ln -s $(pwd)/eval-runner ~/.openclaw/skills/eval-runner
```

The skill should appear in your agent's available skills list once placed in the directory.

---

## Note on README Files

The `README.md` and `README_CN.md` files in each skill folder are for human reference only. OpenClaw agents only read `SKILL.md` and will not load these files. However, if you want to keep your skills directory minimal, feel free to delete the READMEs after copying.

---

## Contributing

Feel free to open issues or PRs for new skills or improvements.

## License

MIT
