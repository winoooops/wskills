---
name: eval-runner
description: Run structured evals on any skill. Reads evals.json, spawns subagents with/without skill, collects results, and generates a grading report.
author: cthulhu
version: "1.0.0"
tags:
  - eval
  - testing
  - benchmark
  - skill-development
---

# Eval Runner Skill

Run structured evaluations on any skill to measure its effectiveness.

## Usage

```bash
# Run evals on a specific skill
run_evals --skill-path /path/to/skill

# Run evals with custom iteration name
run_evals --skill-path /path/to/skill --iteration iteration-2

# Run only specific eval IDs
run_evals --skill-path /path/to/skill --ids 1,2,3
```

## How It Works

1. **Reads** `evals/evals.json` from the skill directory
2. **Creates** workspace at `{skill}-workspace/{iteration}/`
3. **Spawns** two subagents per test case:
   - With skill: includes skill context
   - Without skill: baseline comparison
4. **Collects** runtime, tokens, and output
5. **Grades** and saves results to `results.json`

## Expected evals.json Format

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's realistic prompt",
      "expected_output": "What success looks like",
      "files": ["optional/input-files.csv"]
    }
  ]
}
```

## Output Structure

```
skill-workspace/
└── iteration-1/
    ├── eval-1-task-name/
    │   ├── with_skill/
    │   │   ├── output.txt
    │   │   └── metadata.json
    │   └── without_skill/
    │       ├── output.txt
    │       └── metadata.json
    └── results.json
```

## Grading Metrics

- **Time efficiency**: How much faster with skill?
- **Token efficiency**: How much less context used?
- **Success rate**: Did it complete the task?
- **Quality score**: (Optional) Human-graded output quality

## Configuration

Model and other options are set in `config.json` (alongside `SKILL.md`):

```json
{
  "model": "minimax/MiniMax-M2.5"
}
```

To change the model, edit `config.json` before running evals. Any model supported by your OpenClaw setup works here.

## Notes

- Workspace is always created *alongside* the skill, not inside it
- Default model is MiniMax-M2.5 (cost-efficient); override via `config.json`
- Results are saved in JSON for programmatic analysis
