# youtube-transcript

下载 YouTube 视频字幕、字幕文件和封面图。支持多语言、章节分段、说话人识别、翻译和 SRT 输出。

[English](./README.md)

基于 JimLiu 的 [baoyu-youtube-transcript](https://github.com/JimLiu/baoyu-skills) 重写为精简版技能，减少 token 开销。

---

## 功能

- 通过 InnerTube API 下载 YouTube 字幕（无需 API 密钥）
- 支持手动和自动生成的字幕
- 输出 Markdown 或 SRT 格式
- 缓存结果，快速重新格式化
- 通过 AI 后处理进行说话人识别

## 快速开始

```bash
# 基本字幕
bun scripts/main.ts 'https://www.youtube.com/watch?v=VIDEO_ID'

# 章节 + 说话人识别（最丰富输出）
bun scripts/main.ts 'https://youtu.be/VIDEO_ID' --chapters --speakers

# 中文字幕，不可用时翻译为简体中文
bun scripts/main.ts 'URL' --languages zh,en --translate zh-Hans

# SRT 格式
bun scripts/main.ts 'URL' --format srt

# 列出可用语言
bun scripts/main.ts 'URL' --list
```

## 评测结果

精简版 SKILL.md（3.3KB）与原版（8.8KB）在 5 个测试用例上对比，使用 MiniMax-M2.7：

| 指标 | 精简版 | 原版 | 变化 |
|------|--------|------|------|
| SKILL.md 大小 | 3.3KB | 8.8KB | **-62%** |
| 总 token 数 | 27,853 | 40,988 | **-32%** |
| 总运行时间 | 116s | 152s | **-24%** |
| 成功率 | 5/5 | 5/5 | 相同 |

**结论：** 正确性完全一致，上下文减少 62%，token 减少 32%，执行速度提升 24%。无功能退化。

---

## 关于 README 文件

`README.md` 和 `README_CN.md` 仅供人类阅读。OpenClaw 智能体只读取 `SKILL.md`。复制技能后可放心删除 README。

## 许可

MIT
