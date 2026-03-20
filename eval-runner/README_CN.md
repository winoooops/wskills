# eval-runner

对任意 OpenClaw 技能运行结构化评测，衡量技能的实际效果。

[🇬🇧 English](./README.md)

---

## 工作原理

1. 从目标技能目录**读取** `evals/evals.json`
2. 在技能旁**创建**工作目录
3. 每个测试用例**生成**两个子智能体：
   - **带技能** — 包含技能上下文
   - **无技能** — 基线对比
4. **收集**运行时间、token 消耗和输出
5. **评分**并保存至 `results.json`

---

## 快速开始

### 1. 为你的技能添加评测

在技能目录下创建 `evals/evals.json`：

```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "一个真实的用户提示",
      "expected_output": "成功的样子",
      "files": []
    }
  ]
}
```

### 2. 运行评测

告诉你的智能体：

```
Run evals on ~/.openclaw/skills/my-skill
```

或直接使用脚本：

```bash
# 生成 spawn 命令
./scripts/generate_evals.sh ~/.openclaw/skills/my-skill iteration-1

# 通过 Python 运行
python3 scripts/eval_runner.py --skill-path ~/.openclaw/skills/my-skill
```

### 3. 查看结果

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

## 评分指标

| 指标 | 描述 |
|------|------|
| 时间效率 | 使用技能后快了多少？ |
| Token 效率 | 上下文 token 消耗减少了多少？ |
| 成功率 | 是否完成了任务？ |
| 质量评分 | 人工评分的输出质量 |

---

## 配置

编辑 `config.json` 修改评测使用的模型：

```json
{
  "model": "minimax/MiniMax-M2.5"
}
```

支持你 OpenClaw 配置中的任何模型。

---

## 许可

MIT
