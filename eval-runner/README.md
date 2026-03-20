# eval-runner

Run structured evaluations on any OpenClaw skill to measure its effectiveness.

[🇨🇳 中文版](./README_CN.md)

---

## How It Works

1. **Reads** `evals/evals.json` from the target skill directory
2. **Creates** a workspace alongside the skill
3. **Spawns** two subagents per test case:
   - **With skill** — includes the skill context
   - **Without skill** — baseline comparison
4. **Collects** runtime, tokens, and output
5. **Grades** results and saves to `results.json`

---

## Quick Start

### 1. Add evals to your skill

Create `evals/evals.json` in your skill directory:

```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic user prompt",
      "expected_output": "What success looks like",
      "files": []
    }
  ]
}
```

### 2. Run evals

Tell your agent:

```
Run evals on ~/.openclaw/skills/my-skill
```

Or use the scripts directly:

```bash
# Generate spawn commands
./scripts/generate_evals.sh ~/.openclaw/skills/my-skill iteration-1

# Run via Python
python3 scripts/eval_runner.py --skill-path ~/.openclaw/skills/my-skill
```

### 3. Check results

Results are saved to `{skill}-workspace/{iteration}/results.json`:

```
my-skill-workspace/
└── iteration-1/
    ├── eval-1-task-name/
    │   ├── with_skill/output.txt
    │   └── without_skill/output.txt
    └── results.json
```

---

## Grading Metrics

| Metric | Description |
|--------|-------------|
| Time efficiency | How much faster with skill? |
| Token efficiency | How much less context used? |
| Success rate | Did it complete the task? |
| Quality score | Human-graded output quality |

---

## Configuration

Edit `config.json` to change the model used for eval runs:

```json
{
  "model": "minimax/MiniMax-M2.5"
}
```

Any model supported by your OpenClaw setup works here.

---

## License

MIT
