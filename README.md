# yau-Search

**丘成桐大学生数学竞赛（S.-T. Yau College Student Mathematics Contests）题目结构化检索、分类与分析项目。**

把 2010–2026 年初赛与 2012–2025 年总决赛的历年真题从 PDF 抽取成结构化数据，做成
**可离线检索的题库页面**、**考点统计**、**母题归类**、**官方考纲覆盖率**和**备考材料**。

> 本项目是一个**语料库 + 分析项目**，不是一个刷题 App，也不是竞赛官方项目。
> 题目与官方解答的版权归竞赛主办方与原作者所有 —— 见 [NOTICE.md](NOTICE.md)。

---

## Features

| 能力 | 产物 | 说明 |
|---|---|---|
| **离线题库检索** | `yau_index.html` | 单文件、零依赖、双击即用。按年份 / 科目 / 卷别 / 考点标签筛选 + 关键词全文搜索 |
| 结构化题目数据 | `data/problems_full.json` | **757 道题**的完整题面 + 年份 / 科目 / 卷别 / 题号（唯一权威口径） |
| 题目级指标 | `data/problems_enriched.json` | 每题的考点标签、词数、小问数、任务动词、难度代理 |
| 考点统计 | `reports/stats_overview.md` · `reports/problem_metrics.md` | 逐年逐科题量矩阵、考点 × 年份热力表、动词分布 |
| 官方考纲覆盖率 | `reports/syllabus_coverage.md` | 6 份 Syllabus 拆成 **319 条**，逐条统计真题命中（**153 条 17 年零命中**） |
| 母题归类 | `reports/mother_*.md` · `data/mother_*.json` | 把 757 题按**数学内核**归并（**675 题 / 89.2% 被覆盖**），含每族的"升级链" |
| 近重复题分析 | `data/near_duplicates.json` · `reports/theme_clusters.md` | 词元 shingle 相似度；**注意漏检率 >85%**，需配合母题表使用 |
| 分科综合报告 | `reports/subject_*.md` | 六科各自 490–737 行的横向分析（考点频次、演变、孪生题、优先级） |
| 解题讲义 | `reports/solutions_*.md` | 三科各 10 道精讲（完整分步解答），**已过对抗性审稿并回填 58 处修正** |
| 对抗性审稿 | `reports/referee_*.md` | 独立复核讲义的每一步，指出 10 处必须先改再用的错误 |
| 仿真模拟卷 | `reports/mock_exam_A/B/C.md` | 六科各 6 题 / 100 分，含参考答案与分档给分判据 |
| 学习路线 | `reports/study_roadmap.md` | 考点 → 书目 → 章节 → 配套真题的 12 周路线图 |

---

## Quick Start

### 1. 只想看题（零依赖，推荐）

下载仓库后直接双击打开：

```text
yau_index.html
```

一个自包含的 HTML 页面（约 490 KB，题库内嵌），**不需要联网、不需要装任何东西、不需要起服务器**。
左侧下拉框可按年份 / 科目 / 卷别 / 考点筛选，搜索框支持全文关键词。

纯文本索引（适合 grep 与 GitHub 网页预览）：[reports/all_problems_index.md](reports/all_problems_index.md)。

### 2. 想把题目当数据用

```python
import json
from pathlib import Path

problems = json.loads(Path("data/problems_full.json").read_text(encoding="utf-8"))
print(len(problems))                      # 757

analysis = [p for p in problems if p["subject"] == "Analysis & PDE"]
print(len(analysis), analysis[0]["year"], analysis[0]["n"])
```

单条记录的字段：

```json
{
  "year": "2022",
  "subject": "Analysis & PDE",
  "paper": "2022_ExamPaper_2022_analysis_and_differential_22s",
  "kind": "individual",
  "n": 4,
  "chars": 201,
  "text": "Let C([0,1]) be the space of all continuous C-valued functions ..."
}
```

### 3. 想跑脚本

```bash
git clone https://github.com/wm233-dev/yau-Search.git
cd yau-Search
pip install -r requirements.txt        # 仅 PDF 抽取与数值验算需要；读 data/ 和看 HTML 不需要

python scripts/validation/validate_repository.py   # 自检：文件完整性 / JSON 可解析 / 条目数 / 字段
```

所有脚本都从**仓库根目录**运行，路径由 `scripts/_paths.py` 统一解析，不含任何机器绝对路径。

---

## Repository Structure

```text
yau-Search/
├── README.md                 本文件
├── LICENSE                   MIT（仅覆盖代码与原创分析文字）
├── NOTICE.md                 第三方材料（题面 / 官方解答 / 考纲）的版权边界
├── requirements.txt          pymupdf（抽取用）+ numpy（验算用）
├── yau_index.html            ★ 离线题库检索页（主要产品入口）
├── data/                     结构化数据：题库、考点、母题、考纲命中、总决赛索引
├── corpus/                   从 PDF 抽取的纯文本语料
│   ├── prelim/               初赛 2010–2026（136 个 txt）
│   ├── finals/               总决赛 2012–2025（195 个 txt，含 6 份官方考纲）
│   ├── finals_extra/         从 .doc/.docx/加密 PDF 抢救回的卷（10 个）
│   └── finals_recovered/     乱码卷渲染后逐字识读的文本（9 个）
├── reports/                  研究报告：分科 / 年代 / 母题 / 讲义 / 审稿 / 模拟卷
├── docs/                     使用指南、总报告、审计与整理记录
├── scripts/
│   ├── _paths.py             仓库根定位（所有脚本共用）
│   ├── extraction/           PDF → 纯文本 → 结构化题库
│   ├── analysis/             统计、打标签、母题归并、报告生成
│   ├── validation/           仓库自检、HTML/JSON/PDF 检查
│   ├── verification/         数值验算与审稿脚本
│   ├── library/              考点 → 藏书章节 的映射脚本
│   └── legacy/               一次性探针与调试脚本（保留可追溯）
└── archive/                  中间产物：转储、旧副本、备份、移动记录
```

---

## Data

| 文件 | 大小 | 内容 |
|---|---|---|
| `data/problems_full.json` | 482 KB | **权威题库**：757 道题，字段 `year/subject/paper/kind/n/chars/text` |
| `data/problems_enriched.json` | 840 KB | 上述 + `tags` / `words` / `subparts` / `verbs` / `difficulty_proxy` |
| `data/papers_manifest.json` `data/corpus_manifest.json` | 39 KB / 25 KB | 卷级元数据（页数、字符数、解析题数、抽取规则） |
| `data/papers.json` `data/problems_index.json` | 405 KB / 94 KB | **早期流水线的旧口径快照**，保留仅为可追溯；阅读与二次开发请以 `problems_full.json` 为准 |
| `data/mother_algebra.json` 等 6 个 | 各 16–27 KB | 六科母题归并结果（id / name / members / first / last / trend） |
| `data/syllabus_coverage.json` | 236 KB | 319 条考纲条目的逐条命中明细 |
| `data/finals_index.json` `finals_manifest.json` | 35 / 44 KB | 总决赛 195 份卷的映射与元数据 |
| `data/near_duplicates.json` `data/text_families.json` | 2–3 KB | 近重复题对与文本家族 |
| `data/render/*.png` | 400 KB | 2015 代数卷的页面渲染（该卷字体损坏，靠它抢救） |

**覆盖范围**

* 年份：2010–2026（17 届初赛）+ 2012–2025（总决赛）
* 科目：代数与数论 149 · 分析与 PDE 155 · 几何与拓扑 156 · 概率统计 133 · 计算与应用 135 · 数学物理 29
* 语料：初赛 136 份卷（120 份试卷 + 16 份官方解答卷）、总决赛 195 份卷 + 抢救回 19 份
* 官方解答只在 **2020–2022** 三年发布；其他年份的"解法"均来自本项目的独立推导

---

## Reproducibility

**层级一：读数据 / 看页面** —— 零依赖，clone 下来就能用（见 Quick Start）。

**层级二：重建统计与页面** —— 只需要 Python 标准库：

```bash
python scripts/extraction/rebuild_pipeline.py
```

从 `corpus/prelim/` 重新解析题目 → 合并碎片小问 → 打标签 → 生成
`data/problems_full.json`、`data/problems_enriched.json`、
`reports/stats_overview.md`、`reports/all_problems_index.md` 和 `yau_index.html`。

**层级三：从原始 PDF 重建语料** —— 需要 `pip install pymupdf`，**且需要自备原始 PDF**：

```bash
mkdir -p sources/prelim && cp -r /path/to/历年笔试真题/* sources/prelim/
python scripts/extraction/extract_all.py
```

`sources/` 已被 `.gitignore` 排除。原始 PDF **不随仓库分发**（版权原因，见 NOTICE.md），
所以「从 PDF 到文本」这一步无法在纯 clone 环境下自动完成 —— 这是本项目最主要的复现断点。

**验证**：

```bash
python scripts/validation/validate_repository.py   # 必要文件、JSON 可解析、条目数、字段完整性
node scripts/validation/check_html.mjs             # 校验 yau_index.html 内嵌 JSON 与筛选项
```

---

## Known Limitations

**语料层**

1. **题面来自 PDF 文本层，不是 OCR。** 公式的上下标、负号、根号会在抽取中丢失。
   例如 2019 分析个人卷第 5 题被抽成 `Δu=|u|^{q-1}u+f`，按该符号命题为假，原题几乎必然是 `-Δu=...`。
   凡可疑处，各报告都标了「抽取存疑」，**引用题面前建议回原卷核对**。
2. **本地归档只到 2025。** 2026 年的初赛卷没有 PDF 原件，其题面完全依赖抽取文本，已知至少 3 处符号可疑。
3. **团体卷存在题号错位。** 2013 / 2014 的应用卷、2017 个人应用卷第 5 题在不同 JSON 中切分不一致
   （这是各报告口径差异的主要来源，已在对应报告的「存疑」章节逐条记录）。
4. **部分文件含控制字符**（来自 PDF 的原生噪声，如 0x08 退格），少数文本用普通编辑器打开会显示异常。
5. **总决赛语料尚未统一题库化。** 三份总决赛报告各自切题（244 / 241 / 117 题），口径不同，
   尚未并入 `problems_full.json` 的同一结构。

**分析层**

6. **难度有两套尺度，不可相减。** `difficulty_proxy`（长度+小问数+符号密度）是启发式指标；
   各报告里的「难度 1–5」是分析者人工自评。
7. **自动查重漏检率 >85%。** 命题人会改写措辞与对象，字符串相似度对这套题库几乎无效。
   实测：几何 2011 团体 Q5 与 2024 个人 Q4 是同一道题，跨 13 年，字符 **Jaccard 仅 0.013**。
   请以 `data/mother_*.json` 的母题归类为准。
8. **名词命中统计是下界。** 考纲「零命中」应读作「从不以该术语形态出现」，不等于绝对不考。
9. **人工判断的部分有主观性。** 母题归并、难度评分、复习优先级都由分析者裁定，
   各报告都给出了口径与「存疑清单」，请以报告内的口径为准。

---

## Copyright & License

* **代码与原创分析文字**采用 [MIT License](LICENSE)。
* **竞赛题面、官方解答、官方考纲及第三方材料不适用 MIT 授权**，其版权归各自权利人所有。
  本项目不对其主张任何权利，也不对其再授权；收录目的仅为检索、引用与研究。
  详见 [NOTICE.md](NOTICE.md)。

> Contest problems, official solutions, syllabi and other third-party materials
> remain the property of their respective copyright holders. The repository
> licence applies only to original code and materials unless otherwise stated.

如果你是权利人并希望移除或修改某份材料，请在本仓库开 issue。
