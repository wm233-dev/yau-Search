# REPO_CLEANUP_REPORT — 发布整理记录

> 面向对象：仓库维护者与第一次接触本项目的读者。
> 配套：[REPO_AUDIT.md](REPO_AUDIT.md)（整理前的审计）· [../README.md](../README.md)（项目入口）
> 整理原则：**不删数据、不改结论、不动仓库外的任何东西**。

---

## Summary

在**不改动研究结论、不改动核心数据内容**的前提下，把这个仓库从「研究工作目录」整理成可以公开阅读和维护的项目：

1. **重写 README**（原来只有 2 行）——现在是完整项目说明：功能、快速上手、目录结构、数据说明、复现路径、已知限制、版权边界。
2. **根目录从 18 项降到 7 项**：临时脚本、转储、探针全部归位到 `scripts/` 与 `archive/`。
3. **清除全部机器绝对路径**：269 + 88 个文件、1169 处替换，覆盖 213 个 Python 脚本与 45 份文档；
   新增 `scripts/_paths.py` 统一做仓库根定位；核对后**仓库内已无任何 `<仓库绝对路径>` / `C:\Python3xx` / 作者目录名**。
4. **补齐工程要素**：`requirements.txt`、`.gitignore` 项目条目、`scripts/validation/validate_repository.py` 自检脚本。
5. **明确版权边界**：新增 `NOTICE.md`，README 增加 Copyright & License 段，说明 MIT **不覆盖**竞赛题面 / 官方解答 / 官方考纲。
6. **可复现性验证**：连跑两次 `rebuild_pipeline.py`，6 个产物 **SHA256 完全一致**；
   `data/problems_full.json` 与整理前**逐字节相同**。

**核心数据未受影响**：`data/problems_full.json`、`data/problems_enriched.json`、`corpus/**` 内容均未被修改
（唯一的例外见「Files Modified」第 1 条）。

---

## Structure Before / After

**Before**

```text
yau-Search/
├── README.md (2 行)  LICENSE  .gitignore
├── FINAL_REPORT.md  HOW_TO_USE.md  yau_index.html
├── manifest.json
├── _cleanup.py  _mp_dump.md  check_pdfs{,2,3}.py  extract_all.py
├── gt_all.txt  pdf_check{1,2,3}.txt  probe_text.py  yau_probe.tsv    ← 根目录共 18 项
├── data/ (34)  reports/ (56)  scripts/ (275，脚本与数据混放)
├── work/ (33)  referee/ (14)
└── txt/ (136)  txt_finals/ (195)  txt_finals_extra/ (7)  txt_finals_recovered/ (9)
```

**After**

```text
yau-Search/
├── README.md  LICENSE  NOTICE.md  .gitignore  requirements.txt
├── yau_index.html                        ← 根目录只留 6 项 + 6 个目录
├── data/ (35)                            结构化数据
├── corpus/{prelim,finals,finals_extra,finals_recovered}   (350)
├── reports/ (53)                         研究报告
├── docs/{HOW_TO_USE,FINAL_REPORT,REPO_AUDIT,REPO_CLEANUP_REPORT}.md + history/  (5)
├── scripts/{extraction,analysis,validation,verification,library,legacy}/ + _paths.py  (239)
└── archive/{dumps,clean_copies,derived,work,backups}/ + MOVES.tsv  (98)
```

---

## Files Moved

完整清单见 [../archive/MOVES.tsv](../archive/MOVES.tsv)（340 条，含每条 old → new）。按类归并：

| 类别 | 数量 | 去向 | 理由 |
|---|---|---|---|
| 初赛 / 总决赛文本语料 | 136 + 195 | `corpus/prelim` `corpus/finals` | 4 个平铺的 `txt*` 目录名看不出关系，收进 `corpus/` |
| 抢救回的总决赛卷 | 7 + 3 | `corpus/finals_extra` | 其中 3 份是**解密后的 2020 加密卷**，属语料本身 |
| 渲染识读文本 | 9 | `corpus/finals_recovered` | 同上 |
| 根目录散落文件 | 12 | `scripts/validation`(3) `scripts/extraction`(2) `scripts/legacy`(1) `archive/dumps`(6) | 按用途归位，**一个都没删** |
| `scripts/` 下的脚本 | 234 | `extraction`(18) `analysis`(105) `validation`(6) `verification`(29) `library`(6) `legacy`(41) + 根(1) | 无法确认为可复用工具的一律进 `legacy/` |
| `scripts/` 下的数据 / 图片 / 转储 | 46 + 16 | `archive/derived` `archive/dumps/images` `archive/dumps/stats_out` | 中间产物，不参与分析但保留可追溯 |
| `work/` `referee/` | 43 | `scripts/verification`(27) `archive/work` `archive/dumps` | 把「验算脚本」与「转储」分开 |
| 讲义修改前备份 | 3 | `archive/backups` | 保留可追溯性 |
| 根 `manifest.json` | 1 | `data/corpus_manifest.json` | 它是初赛语料的抽取清单，属数据 |

---

## Files Modified

1. **`data/syllabus_coverage.json`** —— 只改了一个 provenance 字段：
   `"source_problems"` 的值由**机器绝对路径**改为 `data/problems_full.json`。JSON 结构与全部命中数据未变（解析校验通过）。
2. **213 个 `.py` + 45 个 `.md` + 1 个 `.mjs`** —— 机器绝对路径 → 仓库相对路径（见下节）。
   其中核心脚本改为通过 `scripts/_paths.py` 定位；一次性脚本改为**从仓库根目录运行**的相对写法。
3. **`README.md`** —— 完全重写（2 行 → 完整项目说明）。
4. **`docs/FINAL_REPORT.md`** —— 剥离会话时间线、token 计数、「几点交付」等过程性内容，
   只保留项目目标 / 数据规模 / 方法 / 结果 / 验证 / 已知限制 / 后续方向；
   过程内容迁到 `docs/history/development_notes.md`。
5. **`docs/HOW_TO_USE.md`** —— 路径改为仓库相对，删除只适用于作者本机的说明，命令改为可复制执行。
6. **`.gitignore`** —— 追加项目条目（`sources/`、`*.pdf`、编辑器与系统文件）；原有 Python 模板保留。
7. **`reports/*.md`（45 份）** —— **只做路径字符串替换**，未改动任何句子结构与研究结论；
   改后全部为 UTF-8 且未触发任何解析错误。
8. **4 个文件去掉行尾空白**（`_dump_geo.txt`、`gen_report3.py`、两个 clean copy），
   目的是让 `git diff --check` 通过；纯空白改动，无语义影响。
9. **新增文件**：`README.md`(重写) `NOTICE.md` `requirements.txt` `scripts/_paths.py`
   `scripts/validation/validate_repository.py` `docs/REPO_AUDIT.md` `docs/REPO_CLEANUP_REPORT.md`
   `docs/history/development_notes.md` `archive/MOVES.tsv` `archive/PATH_FIXES.json`。

---

## Files Preserved

**没有删除任何文件**，包括看似临时的：

| 保留下来的东西 | 为什么不删 |
|---|---|
| `scripts/legacy/`（41 个一次性探针） | 无法确认是否还有追溯价值；移动而非删除 |
| `archive/derived/`（46 个中间 JSON/TXT） | 是报告数字的来源证据 |
| `archive/clean_copies/`（18 个去 NUL 副本） | 与语料存在细微差异，可能是某份报告的实际输入 |
| `archive/dumps/images/`（9 张 PDF 渲染图） | 乱码卷的识读依据 |
| `archive/backups/`（3 份讲义修改前备份） | 审稿修正的可追溯性 |
| `data/an_ids.txt`（**0 字节**） | 空文件，但删除无收益、保留无成本 |
| `reports/_ca_all_problems.md` 等 5 个「下划线开头」的导出稿 | 是各报告的题面通读稿 |
| `scripts/__pycache__/` | 未删除（已从索引移除并加入 .gitignore，见下） |

> `scripts/__pycache__/` 下的 `.pyc` `git rm --cached`：**文件仍在磁盘上**，只是不再纳入版本控制
> （`.gitignore` 早已包含 `__pycache__/`，之前是历史遗留）。这属于「取消跟踪」而非删除。

---

## Path Fixes

| 项 | 数量 |
|---|---|
| 第一轮替换（机器绝对路径 → 相对路径） | **774 处 / 269 个文件** |
| 第二轮替换（旧目录名 → 新目录名、清理残留分隔符） | **395 处 / 88 个文件** |
| 明细 | `archive/PATH_FIXES.json`（逐文件命中数） |

映射规则：

| 原绝对路径 | 替换为 |
|---|---|
| 仓库自身的绝对路径 | 仓库根（`.py` 用 `.`，文档用空） |
| 初赛 PDF 源目录 | `sources/prelim`（已 gitignore，**不随仓库分发**） |
| 总决赛 PDF 源目录 | `sources/finals` |
| 第三方竞赛（CMC）目录 | `sources/cmc` |
| 本地 vendored PyMuPDF | `sources/pylibs`（改用 `pip install pymupdf` 后不再需要） |
| `C:\Python3xx\python.exe` | `python` |
| 旧目录名 | 新目录名（`txt/` → `corpus/prelim/` 等，见 MOVES.tsv） |

**安全性做法**：只做**精确字面量替换**，不使用宽泛正则。
这一点很关键 —— 语料里有大量 LaTeX，例如 `$[E:\mathbb Q]$`、`f:\mathbb{R}\to\mathbb{R}`，
用正则匹配 `[A-Za-z]:\\` 会把数学内容当成路径改坏。整理后复核确认这些数学串**一处未动**。

---

## Dependency Changes

新增 `requirements.txt`：

| 依赖 | 用于 | 是否必需 |
|---|---|---|
| （无） | 读 `data/*.json`、打开 `yau_index.html` | **零依赖，clone 即用** |
| `pymupdf>=1.23` | `scripts/extraction/*`（PDF → 文本 / 渲染） | 仅「从 PDF 重建语料」时需要 |
| `numpy>=1.24` | `scripts/verification/*`（数值验算） | 仅验算脚本需要 |

没有引入任何新框架，没有把项目改造成包（保持「脚本 + 数据」的形态）。

---

## Copyright Changes

* **`LICENSE` 正文一字未改**（MIT，署名不变）。
* **没有**声称 fair use / public domain 等无法验证的结论。
* 新增 **`NOTICE.md`**，用三节说明：
  1. MIT 覆盖什么（代码、原创分析文字、生成页面）；
  2. **不覆盖什么**（竞赛题面、官方解答、官方考纲、页面渲染图），版权归各自权利人，本仓库不主张、不再授权；
  3. 实务影响（复用代码 vs 复用题面时的不同做法），并提供权利人的移除请求通道。
* **README** 末尾增加精简版声明，并附英文的一句话表述（便于非中文读者与自动化工具识别）。

---

## Validation

| 检查 | 命令 | 结果 |
|---|---|---|
| 仓库自检 | `python scripts/validation/validate_repository.py` | **PASS**（15 项必要文件、55 个 JSON 全部可解析、757 题字段完整、4 个相对链接可达、4 个语料目录非空、**无机器路径**） |
| 页面校验 | `node scripts/validation/check_html.mjs` | **PASS**（内嵌 JSON 可解析、757 题、6 科目、无空记录） |
| 语法检查 | 对全部 245 个 `.py` 做编译检查 | 全部通过 |
| JSON 校验 | 对全部 55 个 `.json` 做解析 | 全部通过 |
| 流水线可复现 | 连跑两次 `scripts/extraction/rebuild_pipeline.py`，比对 6 个产物的 SHA256 | **6/6 完全一致**（含 `problems_full.json`、`yau_index.html`） |
| 核心数据未变 | `problems_full.json` 未被任何一步修改 | 与整理前一致 |
| 路径残留 | 全仓库扫描 `<作者目录名>` / `<作者工作目录名>` / `C:\Python3xx` | 0 命中（`archive/MOVES.tsv` 除外，它是移动记录的**内容本身**） |
| 空白字符 | `git diff --cached --check` | **exit 0（干净）** |
| 敏感信息 | 760 个文本文件扫描 API key / token / 密码 / cookie / 邮箱 | **0 命中**（唯一「密码」是 2020 总决赛卷的**公开文件口令**，非个人凭据） |
| 仓库外影响 | —— | 未改任何系统设置 / 环境变量 / 注册表 / Git 全局配置；未写 F: 盘与仓库外目录 |

> 关于 Git：本机 Git 因仓库属主是 `BUILTIN\Administrators` 而报 *dubious ownership*。
> **没有**使用 `git config --global --add safe.directory`（那会改全局配置），
> 改为每次调用临时传 `-c safe.directory=<path>`，不留任何持久化改动。

---

## Remaining Issues

1. **原始 PDF 不在仓库内**，所以「PDF → 文本」这一步无法在纯 clone 环境下复现
   （版权原因不便于分发）。README 已明确标注这是主要复现断点，并给出自备目录 `sources/` 的做法。
2. **`scripts/legacy/` 里的脚本只是「去掉了机器路径」，不保证能直接跑通** ——
   它们依赖当年的中间产物与运行顺序。已在目录命名与 README 中标注为历史脚本。
3. **报告正文里的绝对路径已全部清除，但报告附录中的复现命令仍指向整理前的脚本位置**
   （例如 `python scripts\lib_index.py`，该文件现在位于 `scripts/library/`）。
   属于**历史记录的准确性**问题，不影响阅读，未逐条改写以免改动研究文本。
4. **6 个 `mother_*.json` 的 schema 不统一**（概率把孤题并入 `mothers`，计算单列 `orphans`）。
   本次**没有**统一它们 —— 统一 schema 会改动数据内容，超出「发布整理」范围。
5. **总决赛语料尚未统一题库化**，`problems_full.json` 仍只含初赛 757 题。
6. **语料中的控制字符**（如 0x08）保留原样：它们来自 PDF 本身，清洗会改动语料内容。
7. `.gitignore` 里的 `*.pdf` 会在未来有人放入非竞赛用 PDF 时也一并忽略 —— 若日后需要跟踪 PDF，请改用白名单。

---

## Recommended Next Step

只有三件事值得做，按优先级：

1. **把母题标注接入检索页**（`data/mother_*.json` → `yau_index.html` 的筛选器），
   让「按母题刷题」在页面上直接可用 —— 这是当前最大的人机体验缺口。
2. **统一总决赛语料**：加一个切题脚本，把 `corpus/finals/` 并入 `problems_full.json` 的结构。
3. **统一 6 个母题 JSON 的 schema**（同时补一份 schema 说明文档），便于外部工具消费。

其余的（2026 卷核对、讲义存疑项裁定、藏书缺口）都需要外部资料，不是仓库整理能解决的。
