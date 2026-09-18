# 丘成桐大学生数学竞赛 · 总决赛（Oral / Final Round）几何与拓扑 + 概率与统计 真题分析（2012–2025）

> 素材：`corpus/finals/`（195 个 txt，由 `sources/finals` 的 PDF 抽取）+ 本报告新增的抢救性抽取（见 §1.3）
> 索引与映射：`data/finals_index.json` → `data/geoprob_map.json`（74 条记录 = 2 份 syllabus + 72 份卷子）
> 统计脚本：`scripts/finals_quality.py`、`finals_geo_prob_stats.py`、`finals_problem_metrics.py`、`finals_vs_prelim.py`、`finals_style_compare.py`、`finals_tables.py`、`build_finals_geo_prob_report.py`
> 数据产物：`data/finals_geo_problems.json`、`data/finals_prob_problems.json`、`data/finals_geo_prob_stats.json`、`data/finals_vs_prelim.json`、`data/finals_problem_metrics.json`

**一句话结论**：总决赛（口试/面试）卷与初赛（笔试）卷几乎是两个物种——同口径下题面文字量只有初赛的 40%，但"叙述并证明某个经典定理 / 构造某个几何对象"的比重高得多（点名定理率 12.8% vs 初赛几何概率卷 5.7%），且几何与拓扑科目的证明动词/计算动词比高达 4.58（初赛同科目 3.23）；卷别上保留 Individual / Team / Overall（全能）三轨直到 2025 年，而初赛 2020 年后已收缩为单一"个人卷"。

---

## 1. 可分析范围声明

### 1.1 语料映射方法

`finals_index.json` 的 `file` 字段是原 PDF 相对路径末段，而 `txt_finals` 的文件名是 **"科目/卷别/原文件名词干" 整串非字母数字字符折叠成单个下划线** 后再加 `.txt`。例如：

```
subj  = "2012-2025Probability and Statistics"
kind  = "Individual"
file  = "2012 Probability (1).pdf"
path  = "2012-2025Probability and Statistics/Individual/2012 Probability (1)"
slug  = re.sub(r"[^A-Za-z0-9]+", "_", path) + ".txt"
      = "2012_2025Probability_and_Statistics_Individual_2012_Probability_1.txt"
```

按此规则 **74/74 条记录全部命中**（0 缺失），映射结果存 `data/geoprob_map.json`。

### 1.2 文字层质量分级（本报告口径）

判定规则（`scripts/finals_quality.py`）：去空白后 `len < 50` → EMPTY；控制字符（除去 \\n\\r\\t）占比 > 8% → MOJIBAKE（CJK 字体缺 ToUnicode，正文变乱码而数学字体正常）；否则 OK。

@@QUALITY_TABLE@@

**结论**：几何与拓扑 32 份卷子 **全部有可用文字层**；概率与统计 35/40 可用，4 份为 CJK 乱码（2013/2014 的个人卷与团体卷）、1 份为 0 字符空文字层（2013 全能卷）。**注意**：`finals_index.json` 里 `chars < 800` 的"扫描件"判定在本学科并不成立——本学科有 25 份卷子 `chars < 800`，其中绝大多数是**正常可读的短卷**（口试题本就只有 2–7 题，2015 团体几何卷仅 261 字符但三题完整）。真正不可读的只有上述 5 份。

### 1.3 非文本层的抢救（本报告新增）

这 5 份不可读卷子 **全部抢救成功**，另有 4 份从未进入 PDF 语料的原卷（.doc/.docx/.JPG）也被恢复：

@@RECOVERED_TABLE@@

抢救手段（未安装任何新依赖）：
1. **PyMuPDF 渲染 + 视觉识读**：`scripts/render_garbled.py` 把乱码 PDF 以 200dpi 渲染成 PNG（`scripts/archive/dumps/images/`），再逐页识读转写（`txt_finals_recovered/*.txt`）。5 份全部得到完整题面，其中 2013 全能概率卷是**手写扫描件**（识别置信度较低，已在正文标注）。
2. **.docx → OMML 数学文本**：`scripts/read_docx.py` 用标准库 `zipfile`+`re` 同时抽取 `<w:t>` 与 `<m:t>`（数学公式在此），恢复 2013 几何全能卷、2014 几何团体卷（另一来源版）。
3. **老式 .doc → ASCII 串扫描**：Word 97 复合文档里正文以单字节存储，直接扫描可打印 ASCII 串即可恢复英文正文，恢复 2014 几何个人卷 + 团体卷（`scripts/read_doc.py`）。
4. **.JPG 照片**：2014 概率全能卷只有 JPG，直接视觉识读。
5. **.tex 源文件交叉校验**：2022 几何卷与 2024 几何团体卷有 `.tex` 源，用于核对 PDF 抽取的公式是否有损——**核对结果：2022、2024 两卷 PDF 抽取与 .tex 完全一致，无公式丢失**。

### 1.4 逐年 × 卷别存在矩阵

@@PRESENCE_G@@

@@PRESENCE_P@@

@@PRESENCE_NOTE@@

### 1.5 无法分析清单（含原因）

@@MISSING_LIST@@

其中 **2012 年只有 Individual 卷、2014 年几何卷未以 PDF 形式入库、2020–2022 年无团体赛几何/概率卷** 是语料本身的空缺（原目录下确实没有对应文件），不是抽取失败。2022 与 2013 的几何卷是"Individual&Overall" 或 "Individual&Team" 合卷（同一 PDF 在索引中被登记为两条 kind 记录），已在题目层面拆分、未重复计数。

---

## 2. 逐年逐卷结构表

题量口径：**顶层题号个数**（(a)(b)(c) 小问不计一题）。难度自评 1–5 为分析者判断（5 = 需要完整掌握该定理证明或非常规构造），**与 §4 中初赛报告的启发式难度代理不是同一把尺子**，不可直接相减。

### 2.1 几何与拓扑（37 卷次 / 127 题）

@@PROBLEM_TABLE_GEO@@

### 2.2 概率与统计（40 卷次 / 114 题）

@@PROBLEM_TABLE_PROB@@

### 2.3 年度汇总（科目 × 卷别）

@@YEAR_TABLE@@

@@SUBJ_KIND_TABLE@@
