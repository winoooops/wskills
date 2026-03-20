# Eval Runner - Quick Reference

## Simplest Usage

Just tell me: **"Run evals on [skill-path]"**

Example:
> "Run evals on ~/.openclaw/skills/twitter"

I'll:
1. Read `evals/evals.json` from the skill
2. Create workspace at `~/.openclaw/skills/twitter-workspace/iteration-N/`
3. Spawn subagents for each test case (with + without skill)
4. Track results and calculate grades

## Manual Usage

```bash
# Generate spawn commands
~/.openclaw/skills/eval-runner/scripts/generate_evals.sh ~/.openclaw/skills/twitter iteration-1

# Run the Python runner
python3 ~/.openclaw/skills/eval-runner/scripts/eval_runner.py --skill-path ~/.openclaw/skills/twitter
```

## Directory Structure

```
~/.openclaw/skills/
├── twitter/                    # Skill
│   └── evals/
│       └── evals.json          # Test cases
└── twitter-workspace/         # Created alongside
    └── iteration-1/
        ├── eval-1-xxx/
        │   ├── with_skill/output.txt
        │   └── without_skill/output.txt
        └── results.json        # Generated grading report
```

## Result Format

```json
{
  "skill": "twitter",
  "iteration": "iteration-1",
  "timestamp": "2026-03-18T18:00:00Z",
  "evals": [
    {
      "id": 1,
      "prompt": "...",
      "with_skill": {
        "runtime_ms": 28000,
        "tokens": 21538,
        "status": "done"
      },
      "without_skill": {
        "runtime_ms": 79000,
        "tokens": 17400,
        "status": "done"
      },
      "grade": {
        "time_improvement_pct": 64.5,
        "token_improvement_pct": -23.8
      }
    }
  ],
  "summary": {
    "avg_time_improvement": "45%",
    "avg_token_improvement": "30%",
    "recommendation": "Skill improves efficiency"
  }
}
```
