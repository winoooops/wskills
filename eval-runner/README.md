# eval-runner

Run structured evaluations on any OpenClaw skill to measure its effectiveness.

对任意 OpenClaw 技能运行结构化评测，衡量技能的实际效果。

---

## How It Works / 工作原理

1. **Reads** `evals/evals.json` from the target skill directory / 从目标技能目录读取 `evals/evals.json`
2. **Creates** a workspace alongside the skill / 在技能旁创建工作目录
3. **Spawns** two subagents per test case / 每个测试用例生成两个子智能体：
   - **With skill** — includes the skill context / 带技能上下文
   - **Without skill** — baseline comparison / 无技能基线对比
4. **Collects** runtime, tokens, and output / 收集运行时间、token 消耗和输出
5. **Grades** results and saves to `results.json` / 评分并保存至 `results.json`

---

## Quick Start / 快速开始

### 1. Add evals to your skill / 为你的技能添加评测

Create `evals/evals.json` in your skill directory:

在技能目录下创建 `evals/evals.json`：

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

### 2. Run evals / 运行评测

Tell your agent:

告诉你的智能体：

```
Run evals on ~/.openclaw/skills/my-skill
```

Or use the scripts directly / 或直接使用脚本：

```bash
# Generate spawn commands
./scripts/generate_evals.sh ~/.openclaw/skills/my-skill iteration-1

# Run via Python
python3 scripts/eval_runner.py --skill-path ~/.openclaw/skills/my-skill
```

### 3. Check results / 查看结果

Results are saved to `{skill}-workspace/{iteration}/results.json`:

结果保存在 `{skill}-workspace/{iteration}/results.json`：

```
my-skill-workspace/
└── iteration-1/
    ├── eval-1-task-name/
    │   ├── with_skill/output.txt
    │   └── without_skill/output.txt
    └── results.json
```

---

## Grading Metrics / 评分指标

| Metric | Description | 描述 |
|--------|-------------|------|
| Time efficiency | How much faster with skill? | 使用技能后快了多少？ |
| Token efficiency | How much less context used? | 上下文 token 消耗减少了多少？ |
| Success rate | Did it complete the task? | 是否完成了任务？ |
| Quality score | Human-graded output quality | 人工评分的输出质量 |

---

## Configuration / 配置

Edit `config.json` to change the model used for eval runs:

编辑 `config.json` 修改评测使用的模型：

```json
{
  "model": "minimax/MiniMax-M2.5"
}
```

Any model supported by your OpenClaw setup works here.

支持你 OpenClaw 配置中的任何模型。

---

## License / 许可

MIT
