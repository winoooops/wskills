# wskills

A collection of skills for [OpenClaw](https://github.com/openclaw/openclaw) agents.

一组用于 [OpenClaw](https://github.com/openclaw/openclaw) 智能体的技能集合。

---

## Skills / 技能列表

| Skill | Description | 描述 |
|-------|-------------|------|
| [eval-runner](./eval-runner/) | Run structured evals on any skill | 对任意技能运行结构化评测 |

---

## Usage / 使用方法

### Install a skill / 安装技能

Copy the skill folder into your OpenClaw skills directory:

将技能文件夹复制到你的 OpenClaw 技能目录：

```bash
cp -r eval-runner ~/.openclaw/skills/
```

Or symlink for development:

或者使用软链接方便开发：

```bash
ln -s $(pwd)/eval-runner ~/.openclaw/skills/eval-runner
```

### Verify / 验证

The skill should appear in your agent's available skills list once placed in the skills directory.

技能放入目录后，应该会出现在你的智能体可用技能列表中。

---

## Contributing / 贡献

Feel free to open issues or PRs for new skills or improvements.

欢迎提交 issue 或 PR 来添加新技能或改进现有技能。

## License / 许可

MIT
