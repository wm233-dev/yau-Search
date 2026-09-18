---

## 3. 考点频次表

统计方式：本报告为 241 道题逐题人工标注了**细分考点**（`topic` 字段），由 `scripts/finals_geo_prob_stats.py` 汇总；另用与初赛报告**完全相同的正则标签体系**（`scripts/finals_style_compare.py`）对题面原文做自动打标，作为交叉验证。

### 3.1 细分考点频次（人工标注，241 题）

@@TOPIC_MERGED@@

### 3.2 细分考点完整明细（按题次降序）

@@TOPIC_TABLE@@

### 3.3 关键词标签自动打标：总决赛 vs 初赛（同正则、同原子）

@@TAGBASE@@

@@TAG_COMPARE@@

@@TAGREAD@@

---

## 4. 总决赛 vs 初赛（笔试）的差异

对比口径：初赛数据取自 `.tmp/burn2026/reports/stats_overview.md`（136 PDF / 759 题）与 `problem_metrics.md`（679 题逐题指标）；总决赛数据为本报告。**所有"每题"指标都按同一段代码、同一公式重算**（`scripts/finals_problem_metrics.py`、`finals_vs_prelim.py`），不是拿两套口径的数字相减。

@@DIFF_VS_PRELIM@@

### 结论 1｜卷别结构：初赛收缩为单轨，总决赛保留 Individual / Team / Overall 三轨

初赛：2010–2019 年每年"个人卷 + 团体卷"，2020–2026 年**只剩个人卷**（stats_overview 单卷明细中 2020–2026 年的 40 条记录 kind 全为 individual）。总决赛：本学科范围内 Team 卷在 2013、2014、2015–2019、2023–2025 均存在（几何 10 个年份、概率 11 个年份），仅 2020–2022 三年缺失；Overall（全能）卷 2013、2015–2025 连续存在。→ **"团队协作型数学题"在总决赛里是长期的独立赛道，在初赛里已经取消。**

### 结论 2｜题量与选做制：总决赛从"全做"走向"选做"，单卷题数降到 2–4

总决赛几何个人卷题数：2012 年 7 题、2015–2022 年 3–4 题、2023–2025 年 4 题；全能卷 2017 年 3 题、2018 年起稳定 2 题；团体卷 2018 年 5 题、2023 年起 3 题。且 2023–2025 三年直接在卷首写明选做规则（个人卷 "Solve 3 out of 4"、团体卷 "Solve 2 out of 3"、全能卷 "Solve 1 out of 2"）。初赛仍是每卷 5–6 题全做（stats_overview：2016 年后每年 6 科 × 5–6 题）。→ **总决赛用"少题量 + 选做 + 口试答辩"筛人，初赛用"全覆盖 + 笔试"筛人。**

### 结论 3｜卷面长度腰斩而概念密度上升

同口径整卷文本：总决赛平均 @@WORDS_PER_PAPER_F@@ 词/卷，初赛几何与概率卷平均 @@WORDS_PER_PAPER_P@@ 词/卷（@@WORDS_PAPER_RATIO@@×）。但**每题**词数几乎持平：几何 @@WPP_G_F@@ vs 初赛 @@WPP_G_P@@，概率 @@WPP_P_F@@ vs 初赛 @@WPP_P_P@@。同时几何科目**每题小问数**从初赛 @@SUB_G_P@@ 升到总决赛 @@SUB_G_F@@（@@SUB_G_RATIO@@×）。→ 决赛不是"更长的题"，而是"更短的话说更难的事"：题目一句"State and prove Crofton formula"（6 词）背后是一整套积分几何。

### 结论 4｜证明/计算的偏斜是"科目差异"而非"轮次差异"（容易被误读）

卷面动词比（prove/show/establish/verify ÷ compute/calculate/find/determine/evaluate/derive/estimate）：

| 口径 | 总决赛 | 初赛 | 解读 |
|---|---|---|---|
| 几何与拓扑 | @@PC_G_F@@ | @@PC_G_P@@ | 决赛几何更纯证明 |
| 概率与统计 | @@PC_P_F@@ | @@PC_P_P@@ | **决赛概率反而更偏计算/构造** |
| 全部 | @@PC_ALL_F@@ | @@PC_ALL_P@@ | 总比值接近 |

题目级（"含证明动词的题数 ÷ 含计算动词的题数"）总决赛 2.11、初赛全部 2.24、初赛几何概率 2.16——**三者在题目层面差异不到 6%**。真正把决赛概率卷与初赛概率卷区分开的是"要构造什么"：决赛概率 114 题里有 26 题明确要求构造/设计（去偏硬币、耦合、最优阈值、采样分布、置信区间），而初赛概率以"求分布/求极限/证明估计量性质"为主。

### 结论 5｜决赛爱"点名定理"，初赛爱"直接算"

题面出现经典定理名（Bonnet-Myers、Synge、Cartan-Hadamard、Hopf-Poincaré、Crofton、Brouwer、Lefschetz、Hilbert、Gauss-Bonnet、Mayer-Vietoris、Künneth、Cramér-Rao、Neyman-Pearson、Wald、Fatou、Jensen…）的比例：**总决赛题面 @@THEO_PCT@@%（@@THEO_N@@/@@THEO_D@@）**，初赛全部题目 8.3%（62/751），初赛几何+概率 5.7%（16/283）。典型题如 2012 个人卷 Q3/Q4（"State and prove the Crofton formula"、"State and sketch the proof of Bonnet-Meyer's theorem"）、2013 团体卷 Q1（"State and prove Synge Theorem"）、2014 个人卷 Q3（"State and prove the maximal diameter theorem"）、2014 团体卷 Q3（"State Hopf-Poincaré Theorem, idea of proof, interesting application"）。→ 决赛考的是"你是否真的会讲一个定理"，初赛考的是"你是否会做一道题"。

### 结论 6｜零复用：决赛题几乎不来自初赛

对 75 份总决赛卷子逐一与 136 份初赛卷做 6-gram Jaccard 相似度：**最大仅 0.085，≥0.15 的配对 0 对**（初赛内部则有 12 对 ≥0.15，最高 1.000，见 stats_overview §4）。同一批出题人大致维持同一份 syllabus（几何 syllabus 明列 Guillemin-Pollack、Milnor、Taubes、Hatcher、Fulton、Spanier），但**题面层面完全不重叠**。

### 结论 7｜科目切分更细：决赛把"概率"与"统计"分成两张卷

总决赛自 2019 年起，个人赛/团体赛/全能赛各自有独立的 "prob" 与 "stat" 卷（2019 年 6 份文件：prob-individual、stat-individual、prob-team、stat-team、prob-personal-overall、stat-personal-overall）；2020 年后又合并为 "Probability and Statistics" 单卷但内部稳定保持"概率题 + 统计题"配比（例如 2012 概率卷 4 题纯概率 + 统计卷 4 题纯统计；2019 个人赛 3 概率 + 3 统计）。初赛早期（2010–2012）则把"应用与计算 + 概率统计"合成一张卷（stats_overview 中 2010–2012 的 "Applied & Computational Probability and Statistics"）。→ **决赛对"统计推断"的考查是独立且成体系的**，不是应用题的点缀。

### 结论 8｜解答公开度与语言

我范围内 77 个卷次中带官方解答的只有 4 份（2012 Probability (1)、2012 Probability (2)/Statistics、2021 Individual、2021 Overall），占 5.2%；初赛语料则含 16 份官方解答卷（stats_overview：2020–2022 三年）。语言上，决赛保留中文卷 **7 份**（2013 概率个人+团体、2014 概率个人+团体、2015 概率个人+团体+全能，共 7 份），初赛 2016 年后全英文。

---

## 5. Individual 卷 vs Team 卷差异（附 Overall）

@@KIND_COMPARE@@

**五条结论：**

1. **题量**：Individual @@N_I@@ 题/@@P_I@@ 卷次 ≈ @@PP_I@@ 题/卷；Team @@N_T@@ 题/@@P_T@@ 卷次 ≈ @@PP_T@@ 题/卷；Overall @@N_O@@ 题/@@P_O@@ 卷次 ≈ @@PP_O@@ 题/卷。Overall 卷最少题（2 题为主），但每题的**小问数最高**（@@SUB_O@@ 个/题 vs Individual @@SUB_I@@、Team @@SUB_T@@）——Overall 卷是"一道题走完一个主题的多步链"。
2. **文字量**：Individual 每题 @@WPP_I@@ 词 > Team @@WPP_T@@ 词 > Overall @@WPP_O@@ 词。个人卷表述最完整，团体/全能卷更依赖考生自己补全设定。
3. **证明强度**：卷面证明/计算动词比 Team @@PC_T@@ > Overall @@PC_O@@ > Individual @@PC_I@@。团体赛要求"给出完整证明"的比例最高（如 2018 几何团体 Q1 证闭单连通 3-流形同伦等价 S³、Q5 Cartan 不动点定理）。
4. **难度不用于区分卷别**：自评难度 Individual @@D_I@@、Team @@D_T@@、Overall @@D_O@@（满分 5），三者相差 < 0.1。**卷别区分的不是难度而是"任务形态"**：Individual 考具体对象的计算与分类（流形、曲线、分布、估计量），Team 考整体性定理与构造（示性类 T8 题、极小曲面 T5 题、微分拓扑 T5 题），Overall 考跨领域综合（比较定理 O4、极小曲面 O3、Laplace 谱 O3）。
5. **同一套母卷切片**：2016 年概率三卷题号连续（Individual 1–3、Overall 4–5、Team 6–8），说明同年三卷由同一批 8 道题按"个人可做 / 需综合 / 需协作"切分。类似的合卷还有 2013 几何（Individual&Team 同 PDF）、2022 几何（Individual&Overall 同 PDF）。
