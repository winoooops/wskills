# wskills

一组用于 [OpenClaw](https://github.com/openclaw/openclaw) 智能体的技能集合。

[🇬🇧 English](./README.md)

---

## 技能列表

| 技能 | 描述 |
|------|------|
| [eval-runner](./eval-runner/) | 对任意技能运行结构化评测 |

---

## 使用方法

### 安装技能

将技能文件夹复制到你的 OpenClaw 技能目录：

```bash
cp -r eval-runner ~/.openclaw/skills/
```

或者使用软链接方便开发：

```bash
ln -s $(pwd)/eval-runner ~/.openclaw/skills/eval-runner
```

### 验证

技能放入目录后，应该会出现在你的智能体可用技能列表中。

---

## 贡献

欢迎提交 issue 或 PR 来添加新技能或改进现有技能。

## 许可

MIT
