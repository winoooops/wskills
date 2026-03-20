# wskills

A collection of skills for [OpenClaw](https://github.com/openclaw/openclaw) agents.

[🇨🇳 中文版](./README_CN.md)

---

## Skills

| Skill | Description |
|-------|-------------|
| [eval-runner](./eval-runner/) | Run structured evals on any skill |

---

## Usage

### Install a skill

Copy the skill folder into your OpenClaw skills directory:

```bash
cp -r eval-runner ~/.openclaw/skills/
```

Or symlink for development:

```bash
ln -s $(pwd)/eval-runner ~/.openclaw/skills/eval-runner
```

### Verify

The skill should appear in your agent's available skills list once placed in the skills directory.

---

## Contributing

Feel free to open issues or PRs for new skills or improvements.

## License

MIT
