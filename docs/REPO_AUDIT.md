# REPO_AUDIT.md — yau-Search 仓库审计

> 审计时间：2026-09-18
> 审计范围：仓库工作副本（原位于作者本机，路径已泛化）
> 审计方式：只读扫描（774 个文件全量遍历 + 关键词扫描），**未做任何修改**。
> 本文件是"先审计后动手"的产物；实施结果见 `docs/REPO_CLEANUP_REPORT.md`。

---

## 1. 当前项目结构

```text
yau-Search/
├── README.md                 58 B      ← 只有两行标题
├── LICENSE                   1.1 KB    MIT, Copyright (c) 2026 wm233-dev
├── .gitignore                4.8 KB    GitHub 官方 Python 模板（未做项目定制）
├── FINAL_REPORT.md           25 KB     总报告
├── HOW_TO_USE.md             9.0 KB    使用指南
├── yau_index.html            498 KB    离线题库检索页（核心产品入口）
├── manifest.json             25 KB     初赛语料抽取清单
├── _cleanup.py / _mp_dump.md / check_pdfs{,2,3}.py / extract_all.py
├── gt_all.txt / pdf_check{1,2,3}.txt / probe_text.py / yau_probe.tsv   ← 根目录散落 12 个
├── data/         34 files   3.2 MB    结构化数据 + 部分中间导出 + data/render/*.png
├── reports/      56 files   3.6 MB    研究报告 + 子代理脚本 + _backup/
├── scripts/     275 files   7.6 MB    脚本 + 数据产物 + 图片 + 清理副本混放
├── work/         33 files   271 KB    调试脚本 + PDF 抽取转储
├── referee/      14 files    93 KB    讲义审稿的验算脚本与转储
├── txt/         136 files   563 KB    初赛真题纯文本
├── txt_finals/  195 files   294 KB    总决赛真题纯文本
├── txt_finals_extra/      7 files     恢复卷（.doc/.docx 转出）
└── txt_finals_recovered/  9 files     渲染/识读抢救回的卷
```

**规模**：774 个文件（不含 `.git`），约 16.4 MB；其中 `.git` 6.0 MB。

**文件类型分布**

| 类型 | 数量 | 体积 |
|---|---|---|
| .txt | 392 | 2.0 MB |
| .py | 245 | 938 KB |
| .md | 66 | 3.7 MB |
| .json | 54 | 6.3 MB |
| .png | 12 | 2.3 MB |
| .html | 1 | 498 KB |
| 其他（.tsv/.mjs/无扩展名） | 4 | 26 KB |

---

## 2. 文件分类

### 2.1 用户真正应该看到的入口（保留并强化）
1. `README.md` —— 但目前只有两行，**必须重写**（最高优先级）
2. `yau_index.html` —— 离线检索页，双击即用，是最低门槛的入口
3. `data/problems_full.json` —— 唯一权威题库（757 题）
4. `docs/HOW_TO_USE.md`（现 `HOW_TO_USE.md`）—— 场景化使用指南
5. `reports/all_problems_index.md` —— 纯文本题目索引

### 2.2 核心数据（不得改动内容）
| 文件 | 说明 |
|---|---|
| `data/problems_full.json` (482 KB) | 757 题完整题面，权威口径 |
| `data/problems_enriched.json` (840 KB) | 上述 + 考点标签/词数/难度代理 |
| `data/papers_manifest.json` / `manifest.json` | 卷级元数据 |
| `data/mother_*.json` (6 个) | 六科母题归并结果 |
| `data/syllabus_coverage.json` (236 KB) | 319 条考纲命中明细 |
| `data/finals_*.json` (7 个) | 总决赛卷索引/统计 |
| `data/near_duplicates.json` `data/text_families.json` | 近重复题对 |
| `txt*/` 四个目录（347 个文件） | 从 PDF 抽取的纯文本语料 |

### 2.3 原始材料 / 派生材料
- **原始材料**：不在仓库内。真正的 PDF 原件留在作者本机（ `E:\...\.tmp\yau\` 与 `F:\丘成桐大学生数学竞赛历年{笔试,总决赛}真题`，**仓库只有抽取后的文本**。
- **派生材料**：`txt*/`（PDF→文本）、`data/*.json`（文本→结构化）、`yau_index.html`（JSON→HTML）。

### 2.4 生成物（可复现，但体积大）
`yau_index.html`、`data/problems_*.json`、`reports/*.md`、`scripts/archive/dumps/stats_out/*`、`scripts/*.json`（tag_stats/lib_index/prob_ps_rows 等 20 余个中间 JSON）。

### 2.5 开发/调试过程留下的文件（数量最多的类别）
- `scripts/subj_an_1.py … subj_an_30.py`（30 个）：某位分析者的编号式临时脚本
- `scripts/ref_probe1..8.py`、`ref_num1..5.py`（13 个）：审稿探针
- `scripts/roadmap_probe1..5.py`、`_phys_*.py`（19 个）、`_geom_*.py`（13 个）、`prob_*.py`（11 个）
- `work/` 全部 33 个、`referee/` 全部 14 个：验算与转储
- 根目录 12 个散落文件

**初步统计**：`scripts/` 275 个文件里，约 **200 个是一次性分析脚本**，约 **50 个是数据/图片/文本产物**混在其中。

### 2.6 存在本地绝对路径的文件（重点）

| 标记 | 命中文件数 | 命中次数 |
|---|---|---|
| 作者的项目目录名 | 223 | 343 |
| 作者的工作目录名 | 250 | 567 |
| `E:\` | 2 | 2 |
| `F:\` | 2 | 3 |
| `C:\` / `/Users/` / `/home/` / `AppData` / 用户名 `61569` | 0 | 0 |

按类型：**.py 213 个、.md 45 个、.json 1 个、.mjs 1 个、.txt 1 个**，合计 261 个文件受影响。

最严重的（含量降序）：`reports/subject_probability.md`(28)、`reports/finals_alg_ana.md`(21)、`reports/referee_geometry.md`(20)、`reports/study_roadmap.md`(20)、`scripts/gen_report3.py`(14)、`scripts/gen_report.py`(12)。

典型形态：
- 代码：`BASE = r"sources/prelim"`
- 文档散记：`产物在 reports/ 下`
- 数据字段：`"source_problems": "E:\\...\\data\\problems_full.json"`

### 2.7 明显环境依赖的脚本
- `import fitz`（PyMuPDF）：**19 个脚本** —— 仅 PDF 抽取/渲染需要
- `import numpy`：**15 个脚本** —— 仅数值验算需要
- 其余全部是标准库（json 83、os 79、re 25、collections 17、sys 16…）
- `scripts/lib_index.py` 等依赖作者本机书库目录（F: 盘）——**仓库外资源**
- 没有任何 `requirements.txt` / `pyproject.toml` / `environment.yml`

---

## 3. 已发现的问题

| # | 问题 | 严重度 | 影响 |
|---|---|---|---|
| 1 | README 只有 2 行，无法解释项目 | **高** | 新访客 100% 流失 |
| 2 | 261 个文件含机器绝对路径 | **高** | 换台机器脚本全废；泄露作者目录结构 |
| 3 | 无依赖声明文件 | **高** | `pip install -r requirements.txt` 无从谈起 |
| 4 | LICENSE 是标准 MIT，**未区分第三方竞赛材料** | **高** | 可能被误读为"竞赛题面也被 MIT 授权" |
| 5 | 根目录散落 12 个临时文件 | 中 | 打开仓库第一眼是杂乱 |
| 6 | `scripts/` 脚本与产物混放，无子目录 | 中 | 找不到入口 |
| 7 | `work/` `referee/` `scripts/archive/dumps/stats_out/` `scripts/archive/clean_copies/` `scripts/archive/dumps/images/` `scripts/archive/dumps/images/` `scripts/_finals_2020/` 命名以 `_` 开头 | 中 | 语义不清 |
| 8 | 文本语料有 4 个目录平铺在根（`txt/ txt_finals/ …`） | 中 | 4 个目录名看不出层级关系 |
| 9 | `FINAL_REPORT.md` 混入会话时间线、token/交付时间等过程性内容 | 中 | 不像正式研究报告 |
| 10 | `data/an_ids.txt` 是 0 字节空文件 | 低 | 噪声 |
| 11 | `scripts/lib_index.json` (2.0 MB) 是作者私有书库索引 | 低 | 体积大、与检索项目无关 |
| 12 | 图片产物分散在 `data/render/` `scripts/archive/dumps/images/` `scripts/archive/dumps/images/` | 低 | 同类东西三处 |
| 13 | 无 `validate` 类自检脚本 | 低 | 改动后无法快速验证 |
| 14 | 无 `NOTICE`/`THIRD_PARTY_NOTICE` | 中 | 版权边界不清 |
| 15 | `scripts/gen_report*.py` 里出现程序化生成的 `BT` 占位符残留 | 低 | 复跑会产出乱码文本 |

**未发现**：任何 API key、token、密码、cookie、邮箱、AWS/GitHub 凭据（760 个文本文件全量扫描，0 命中）。
唯一的"密码"是总决赛 2020 卷的**公开文件口令 `Yau-ACM20`**（官方随卷公布），属于正常记录，非个人凭据。

### 3.1 敏感信息结论
**可以公开发布**，但建议：
- 在 NOTICE 中说明竞赛材料的版权归属；
- 绝对路径里的作者个人目录名虽不敏感，但应一律清除。

---

## 4. 建议的目标结构

```text
yau-Search/
├── README.md                 ← 重写（第一优先）
├── LICENSE                   ← 保留 MIT，正文不动
├── NOTICE.md                 ← 新增：第三方材料版权声明
├── .gitignore                ← 追加项目相关条目
├── requirements.txt          ← 新增：pymupdf（可选）+ numpy（验算用）
├── yau_index.html            ← 保留在根（核心产品入口）
├── data/                     ← 核心数据（内容不动，极少量中间产物移出）
├── docs/
│   ├── HOW_TO_USE.md         ← 由根目录移入 + 清除绝对路径
│   ├── FINAL_REPORT.md       ← 由根目录移入，剥离过程性内容
│   ├── REPO_AUDIT.md         ← 本文件
│   ├── REPO_CLEANUP_REPORT.md
│   └── history/
│       └── development_notes.md   ← 从 FINAL_REPORT 抽出的过程记录
├── reports/                  ← 研究报告（正文不动，仅路径规范化）
├── corpus/
│   ├── prelim/               ← 原 txt/
│   ├── finals/               ← 原 txt_finals/
│   ├── finals_extra/         ← 原 txt_finals_extra/
│   └── finals_recovered/     ← 原 txt_finals_recovered/
├── scripts/
│   ├── _paths.py             ← 新增：统一的仓库根定位
│   ├── extraction/           ← PDF→文本、语料构建
│   ├── analysis/             ← 统计/打标签/母题归并
│   ├── validation/           ← PDF/HTML/JSON 检查 + validate_repository.py
│   ├── verification/         ← 讲义审稿与数值验算（原 referee/ + work/ 中的验算）
│   ├── library/              ← 考点→书目映射（原 topic_books*/lib_*）
│   └── legacy/               ← 一次性探针、调试脚本（保留可追溯）
└── archive/
    ├── dumps/                ← 中间转储（gt_all.txt、_mp_dump.md、pdf_check*.txt…）
    ├── work/                 ← 原 work/
    └── backups/              ← 原 reports/_backup/
```

**不变的东西**：`data/` 的 JSON 内容、`reports/` 的研究结论、`corpus/` 的文本内容、`yau_index.html`。

---

## 5. 有风险的修改（需要谨慎或不做）

| 风险项 | 判断 | 处理 |
|---|---|---|
| 批量重写 `reports/*.md` 正文以去掉路径 | **中风险**：45 个报告含路径，多为"产物位置"说明 | 只做**机械字符串替换**（把机器前缀换成相对形式），不改任何句子结构与结论；改后逐文件校验 JSON/MD 结构 |
| 移动 `txt*/` 到 `corpus/` | **中风险**：脚本与报告里引用了 `txt/xxx.txt` | 移动后做**配套的引用替换**，并用脚本验证"被引用的文件都存在" |
| 移动 `scripts/` 200+ 脚本 | **中风险**：脚本之间的 `import` 可能失效 | 先扫描跨脚本 import（已发现 `_mothers_a/_mothers_b/finals_alg_ana_problems/finals_alg_ana_extras` 4 个本地模块），确保同目录移动 |
| 改动 `data/*.json` | **高风险** | **不做**。唯一例外：`syllabus_coverage.json` 里的 `source_problems` 绝对路径字段→改相对；改后必须 `json.load` 校验 |
| 改动 `LICENSE` 正文 | **高风险** | **不做**。只在 `NOTICE.md` + README 里补充边界说明 |
| 删除任何文件 | **高风险** | **一律不删**。0 字节的 `data/an_ids.txt` 与重复副本也保留（移入 `archive/`） |
| 修改 Git 全局配置 | 禁止 | 本机 `git` 因 "dubious ownership" 拒绝运行；**不使用 `git config --global`**，改用每次调用加 `-c safe.directory=…` 的临时覆盖 |

---

## 6. 可以安全执行的修改（本次实施范围）

1. **重写 README.md**（无风险，收益最大）
2. **新增 `NOTICE.md` + README 版权段**（无风险）
3. **新增 `requirements.txt`**（无风险）
4. **追加 `.gitignore` 条目**（无风险，只增不减）
5. **根目录 12 个散落文件归位**（低风险，git mv）
6. **`txt*/` 四目录 → `corpus/`**（中风险，配套引用替换 + 校验）
7. **`scripts/` 分子目录**（中风险，保持本地 import 同目录）
8. **`referee/` `work/` → `scripts/verification/` `archive/archive/work/`**（低风险）
9. **`HOW_TO_USE.md` `FINAL_REPORT.md` → `docs/`**，并把过程性内容抽到 `docs/history/development_notes.md`（低风险）
10. **清除绝对路径**：新增 `scripts/_paths.py`；核心脚本改为 `Path(__file__)` 定位；其余文件做机械前缀替换（中风险，改后全量校验）
11. **新增 `scripts/validation/validate_repository.py`**（无风险）
12. **新增 `docs/REPO_CLEANUP_REPORT.md`**（无风险）

**明确不做**：不改研究结论、不改 `data/*.json` 内容（除 1 个 provenance 字段）、不删文件、不改 LICENSE 正文、不碰仓库外的任何东西。

---

## 7. 复现路径（审计结论：目前**不可复现**，整理后可达"部分可复现"）

当前状态：从零 clone 后，`yau_index.html` 与 `data/*.json` **可以直接看**（这部分是好的），但**任何脚本都跑不起来**（绝对路径 + 缺依赖声明 + 原始 PDF 不在仓库）。

整理后应达到：
1. `git clone` + 打开 `yau_index.html` → **立即可用**（零依赖）
2. `pip install -r requirements.txt` → 可以读取 `data/`、跑校验脚本
3. 想从 PDF 重建语料：需自备原始 PDF（版权原因不入库），放到 `sources/`（已 gitignore），再跑 `scripts/extraction/rebuild_pipeline.py`

---

## 8. README 当前缺少什么

一句话：**除了标题，什么都缺**。需要补齐：
是什么 / 数据覆盖 / 题目数量 / 功能 / Quick Start / 数据在哪里 / 如何检索 / 如何跑脚本 / 项目结构 / 数据与研究方法 / 已知限制 / License 与版权边界。

---

## 9. LICENSE 的版权风险（结论：**存在，必须补声明**）

- 当前 `LICENSE` = 标准 MIT，署名 `wm233-dev`，覆盖范围写的是泛指的 "the Software"。
- 但仓库里有大量**非作者原创内容**：
  1. `corpus/*`（347 个文本文件）= **竞赛题面与官方解答的逐字抽取**（2010–2026 初赛 + 2012–2025 总决赛）
  2. `data/problems_full.json` 等 = 上述题面的结构化副本
  3. `data/render/*.png` = 原卷页面渲染图
  4. 6 份官方 Syllabus 的文本（在 `corpus/finals/` 内）
  5. `reports/*.md` 里逐字引用的题面
- **不建议**处理方式：改 LICENSE 正文、声称 fair use / public domain（无法验证）。
- **建议**处理方式：新增 `NOTICE.md`，明确写出：
  - MIT 只覆盖**作者原创的代码、脚本、数据处理逻辑与原创分析文字**；
  - 竞赛题面、官方解答、官方考纲及其他第三方材料的版权归**各自权利人**所有，本仓库不主张权利、也不对其再授权；
  - 若权利人提出异议，将按要求移除相应材料。
- 同时在 README 末尾放一段简版声明。

---

## 10. 审计阶段的未决问题（需在实施中确认）

1. `scripts/` 中 4 个本地 import（`_mothers_a` `_mothers_b` `finals_alg_ana_problems` `finals_alg_ana_extras`）——移动时必须保持同目录。
2. `data/papers.json` (405 KB) 与 `data/problems_index.json` (94 KB) 是旧口径产物（757/758 版本混用），**保留但需在 README 里标注"以 problems_full.json 为准"**，避免误导。
3. `reports/_backup/*.original.md`（266 KB）是讲义修正前的备份，**保留**（可追溯性有价值），移入 `archive/backups/`。
4. `scripts/gen_report*.py` 里程序化产生的 `BT` 占位符残留 —— 属生成器缺陷，**不在本次修复范围**（改它等于改生成逻辑），仅在报告中注明。
