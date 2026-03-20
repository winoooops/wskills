# wskills

一组有态度的 AI 智能体技能集合。

[English](./README.md)

---

## 技能列表

### eval-runner

对任意 OpenClaw 技能运行结构化评测。分别生成带技能和不带技能的子智能体进行对比，衡量时间、token 消耗和成功率。适用于技能开发和优化。

➡️ [详情](./eval-runner/)

---

## 使用方法

将技能文件夹复制到你的 OpenClaw 技能目录即可安装。以安装 `eval-runner` 为例：

```bash
cp -r eval-runner ~/.openclaw/skills/
```

或者使用软链接方便开发：

```bash
ln -s $(pwd)/eval-runner ~/.openclaw/skills/eval-runner
```

技能放入目录后，应该会出现在你的智能体可用技能列表中。

---

## 关于 README 文件

每个技能文件夹中的 `README.md` 和 `README_CN.md` 仅供人类阅读。OpenClaw 智能体只会读取 `SKILL.md`，不会加载这些文件。如果你希望保持技能目录精简，复制后可以放心删除这些 README。

---

## 贡献

欢迎提交 issue 或 PR 来添加新技能或改进现有技能。

## 许可

MIT
