# wskills

一组用于 [OpenClaw](https://github.com/openclaw/openclaw) 智能体的技能集合。

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

## 贡献

欢迎提交 issue 或 PR 来添加新技能或改进现有技能。

## 许可

MIT
