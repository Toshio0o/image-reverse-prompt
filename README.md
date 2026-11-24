# 图像反推 · 通用分层拆解

把任意图片反推成结构化元数据 + 中文提示词 + 英文提示词，本地图片可附 6 色色卡。

给 AI 编程助手 / Agent 用的 Skill，遵循 `SKILL.md` + `skill.yaml` 规范，Muse、Claude Code、Codex 等支持 Skill 的工具均可直接安装。

## 方法：通用层 + 类型层

先分类，再拆解，逐项核验，最后合成提示词：

1. **分类**：定主类型（混合图定主次）
2. **拆解**：通用层 8 项全填，主类型层逐项填，不适用留空不编
3. **核验**：逐项对照原图过核验门（方向、数量、左右手、文字、材质……），不确定的标问号，不编造
4. **合成**：先写中文提示词，再按生图习惯重组英文提示词（不是中文直译）
5. **色卡（可选）**：脚本从像素算 6 色色卡，不用眼睛估

**通用层 8 项**：图像类型、画面氛围、构图取景、光线、色彩配色、成像质感、风格滤镜、防错提示。

**11 个类型层**：人像（10 项）、风景、产品、建筑、室内、食物、动物、艺术绘画、车辆、插画、海报（各 6–7 项）。每个类型层都由两张不同图片跑通全流程、核验无误后才正式建层。

## 文件结构

- `SKILL.md` — 五步流程、核验门、合成规则、输出格式
- `skill.yaml` — Skill 元数据
- `references/schema.md` — 元数据字段定义（通用层 + 11 个类型层）与 JSON 骨架
- `references/examples.md` — 24 个实测范例（街拍、风景、建筑、产品、室内、食物、动物、油画、车辆、插画、海报、品牌横幅），每例含元数据要点、核验教训、中英提示词与脚本实测色卡
- `scripts/extract_palette.py` — 6 色色卡提取脚本（LAB 空间 k-means 聚类，固定种子，结果可复现）

## 安装

```bash
git clone https://github.com/Toshio0o/image-reverse-prompt.git
```

把整个目录放进你的 Skills 目录即可，例如 Muse 的 `~/workspace/custom-skills/`、Claude Code 的 `~/.claude/skills/`、Codex 的 `~/.codex/skills/`。

## 用法

发一张图，说一声「反推」即可。默认交付元数据 JSON + 中文提示词 + 英文提示词；只要提示词时只给提示词。

色卡脚本（依赖 Pillow + numpy，不联网，不写文件）：

```bash
python3 scripts/extract_palette.py <图片路径> [--colors N] [--json]
```

## 扩展新类型

新类型按主体、细节、环境三层展开写专属字段，复用通用层 8 项；先拿两张该类型的图跑通全流程、核验无误后，再把新类型写进 `references/schema.md`。

## 许可证

MIT License，见 [LICENSE](LICENSE)。

## 作者

Toshi — X [@0xToshio_O](https://x.com/0xToshio_O) · GitHub [@Toshio0o](https://github.com/Toshio0o)
