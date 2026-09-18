# 丘成桐大学生数学竞赛（笔试/初赛）仿真模拟卷 B
## 科目：几何与拓扑 ＋ 概率与统计

> **数据口径（本报告全部题面、计数、出处均以此为准）**
> - 题源：`.tmp\burn2026\data\problems_full.json`，**当前快照 757 题**（已核实：文件内 `len(d)==757`）。
> - 其中 **Geometry & Topology 156 题**、**Probability & Statistics 133 题**（本人用当前文件重新点数）。
> - ⚠️ **口径差异记录**：`reports\subject_geometry.md` §0.1 称结构化数据"只切出 159 道几何题"（另有 2012 个人卷 Q1 漏抽的第 160 题）。当前 757 题快照里几何为 **156** 题，与 159 相差 3 题；本报告一律以**当前 757 题文件**为准。引用该报告的"考点频次/优先级"结论时，只引用其**相对频次与年份结构**（这类结论对 ±3 题的样本扰动不敏感），不引用其绝对题数。
> - 抽取自 PDF 纯文本，公式、上下标、希腊字母有损；凡涉及本题面与答案的关键处，本报告均已回读 `.tmp\burn2026\txt\` 下的**原始抽取文本**核对（见 §5.1）。
> - 依据报告：`reports\subject_geometry.md`（160 题人工打标 / 35 标签 / 官方考纲逐条命中）、`reports\subject_probability.md`（137 题人工打标 / 11 个骨架考点）、`reports\yau_2024_2026_deep_analysis.md`（2024–2026 逐题难度 1–5 自评）、`reports\theme_clusters.md`、`reports\study_roadmap.md`、`reports\all_problems_index.md`。

---

## §0 组卷说明

### 0.1 一句话总纲

**一套 12 题的仿真卷：几何与拓扑 6 题、概率与统计 6 题，全部取自 2017–2026 真实真题原题（题设一字未改，仅做排版与记号还原），按 2020 年后的"单卷 6 题、全部必做"现代赛制重新组卷，每题给出分值建议与分档给分细则。**

### 0.2 现代赛制长什么样（组卷的形式依据）

| 时期 | 卷制 | 几何卷题量 | 概率卷题量 |
|---|---|---|---|
| 2010–2018 | 个人卷 ＋ 团体卷分开，卷面写 "Please select 5 problems to solve" / "Solve 5 out of the following 6" | 6 + 6 | 6 + 6 |
| 2019 | 个人卷 5 题 / 团体卷 5 题，**取消选做** | 5 + 5 | 4 + 4 |
| **2020–2026（现代赛制）** | **单卷 6 题（2025 概率卷例外为 4 题、2025 几何卷 5 题），卷面写 "Solve every problem."** | 6 | 6（2025 为 4） |

- 依据：`reports\subject_geometry.md` §0.1 的逐年"卷面选做规则"表；`reports\subject_probability.md` §1.1「卷制沿革（三个时代）」。
- **本卷采用现代赛制**：两科各 6 题，全部必做，不设"6 选 5"。
- 卷面原文中的纪律文字同样保留其精神：2011 年卷面写 "For the following problems, every example and statement must be backed up by proof. Examples and statements without proof will receive no-credit."（见 `reports\2010-2012_丘成桐竞赛笔试真题深度分析.md` §4.5）——本卷的零分判据严格照此执行（见 §2 各题"零分"条目）。

### 0.3 建议用时与依据

| 项目 | 本卷设定 | 依据 |
|---|---|---|
| 单科时长 | **150 分钟（2 小时 30 分）** | ① 2011 年几何个人卷卷面原文标注 "**9:30–12:00 am, July 10, 2011**"（`.tmp\burn2026\txt\2011_3_GeomTop_Individual_2011.txt` 第 6 行）；② 2011 年另有卷面标注 "2:30–5:00 pm, July 9, 2011"（`reports\2010-2012_丘成桐竞赛笔试真题深度分析.md` §4.5）；③ `reports\solutions_geometry.md` 明写"丘赛该科目个人卷历史上给 2.5 小时"；④ `reports\solutions_algebra.md` 结语"个人赛通常 5–6 题、2.5–3 小时，平均每题 25–35 分钟"。→ **2.5 小时是丘赛个人卷的可核验历史时长，本卷沿用。** |
| 压缩训练版 | 90 分钟（只做标"中"的 3 题 ＋"难"的 1 题）或 100 分钟（6 题中任选 5 题） | 模拟老赛制"6 选 5"的压力；不改变题目本身 |
| 时间分配建议 | 易题（12 分）各 ≤ 20 分钟；中题（18 分）各 ≤ 30 分钟；难题（22 分）≥ 40 分钟，并留 15 分钟检查 | 按 `solutions_analysis.md` 的三档分钟数（基础 10–30、中等 30–60、偏难 45–90）压缩到 2.5 小时内 |

### 0.4 选了什么：12 题清单（全部为真题原题）

**几何与拓扑卷（6 题 / 100 分）**

| 卷面号 | 出处 | 题面一句话 | 档位 | 分值 |
|---|---|---|---|---|
| 1 | **2026 几何 Q5** | 闭 aspherical（万有覆叠可缩）流形：证万有覆叠非紧；证 π₁ 的每个非平凡元无限阶 | 中(3) | 18 |
| 2 | **2024 几何 Q4** | 标量曲率 = Ricci 张量在单位球面 S^{n−1}⊂T_pM 上的平均值 | 易(2) | 12 |
| 3 | **2024 几何 Q2** | R³ 中闭（紧无边）嵌入曲面不可能是极小曲面 | 易(2) | 12 |
| 4 | **2024 几何 Q3** | 闭单连通 6 维流形，若 H₂(M)=Z₂ 则 χ(M) ≠ −1 | 中(3) | 18 |
| 5 | **2026 几何 Q1** | \|K(p)\| = lim Area(N(A_ε))/Area(A_ε)（Gauss 映射的面积伸缩率） | 中(3) | 18 |
| 6 | **2026 几何 Q3** | 双不变度规 Lie 群：截面曲率非负；z(g)=0 ⇒ G 紧；G 单连通 ⇒ G ≅ G′×R^k | 难(4) | 22 |

**概率与统计卷（6 题 / 100 分）**

| 卷面号 | 出处 | 题面一句话 | 档位 | 分值 |
|---|---|---|---|---|
| 1 | **2026 概率 Q2** | 分块回归：全回归的 β̂₂ 等于把 M₁Y 对 M₁X₂ 回归所得的 β̂₂（FWL 定理） | 易(2) | 12 |
| 2 | **2026 概率 Q3** | f(x)=2φ(x)Φ(ax)：证它是密度；求 E(Y) | 易(2) | 12 |
| 3 | **2020 概率 Q3** | 从 S₀=a 出发的 ±1 随机游走，对**一切** p∈[0,1] 求 P_a(τ₀<∞) | 中(3) | 18 |
| 4 | **2017 概率（团体卷）Q5** | 用零的比例 p̃ 与 MLE p̂ 估计 p=P(X_i=0)=e^{−λ}：极限分布与渐近相对效率 | 中(3) | 18 |
| 5 | **2021 概率 Q1** | X_n ⇒ X 且 sup_n E\|X_n\|^r ≤ C ⟹ 对一切 0<s<r 有 E\|X_n\|^s → E\|X\|^s | 中(3) | 18 |
| 6 | **2026 概率 Q6** | ξ,η 独立，若 S=ξ+η 与 D=ξ−η 也独立，则 ξ,η 必正态（Bernstein / Darmois–Skitovich） | 难(4) | 22 |

> 总分：每科 **100 分**（2×12 + 3×18 + 1×22 = 100）。

### 0.5 为什么这么选（四条硬约束）

**约束一：按现代赛制（6 题、全部必做、卷末不再分 Part I/II）。** 2020 年起卷面无选做提示，2022–2026 各科一律 6 题（2025 除外）。本卷不设选做，且**不把统计题全部堆在最后**（真实卷面本身也是混排：2026 概率卷的顺序是 copula → 分块回归 → 偏正态 → 布朗运动 → 稳定分布 → Bernstein）。

**约束二：覆盖该科目的骨架考点（以两份科目综合报告的人工打标为准）。**

几何与拓扑 —— `reports\subject_geometry.md` §2 的 21 个"骨架标签（≥5 个年份出现）"中，本卷覆盖 **10 个**：

| 骨架考点（报告口径） | 年份数/题次 | 本卷对应题 |
|---|---|---|
| 覆叠空间与群作用 | 8 年 / 13（★核心） | 几何 1（aspherical、万有覆叠、π₁ 扭自由） |
| 同调群计算（Betti 数/对偶） | 11 年 / 15（★核心） | 几何 4（Poincaré 对偶 ＋ 中间维交错配对） |
| 微分形式 / de Rham / **Poincaré 对偶** | 8 年 / 10（★核心） | 几何 4 |
| **Ricci 曲率 / Einstein / Schur 型刚性** | 9 年 / 9（★核心） | 几何 2（Ricci 张量的迹与球面平均） |
| 曲率张量代数与曲率计算 | 8 年 / 9（★核心） | 几何 6（双不变度规的 K = ¼·\|[X,Y]\|²） |
| 截面曲率与比较 | 7 年 / 9（★核心） | 几何 6 |
| Lie 群 / 双不变度量 / Killing 型 | 7 年 / 8（★核心） | 几何 6 |
| Euler 示性数与配边/边界障碍 | 7 年 / 7（☆骨架） | 几何 4 |
| 极小曲面 / 极小超曲面 | 6 年 / 7（☆骨架） | 几何 3 |
| 经典曲线曲面论（Gauss 映射/基本形式） | 6 年 / 9（☆骨架） | 几何 5 |
| 基本群与 van Kampen | 6 年 / 8（☆骨架） | 几何 1（部分覆盖：π₁ 的扭自由性） |

> 未覆盖但属核心的：映射度/同伦群（11 题次）、测地线/Jacobi/第二变分（9）、示性类（9）、复射影空间（7）、正曲率刚性（7）。6 题容量下的取舍见 §0.7，被考虑但落选的题见 §5.3。

概率与统计 —— `reports\subject_probability.md` §2.1 的 11 个骨架考点中，本卷覆盖 **6 个**（且覆盖了题次排名前 5 中的 4 个）：

| 骨架考点（报告口径，按累计题次排序） | 年份数/题次 | 本卷对应题 |
|---|---|---|
| 1 分布论 / 特征函数 / 变量替换 | 13 年 / 29 | 概率 2（偏正态构造＋矩）、概率 6（特征函数方程） |
| 2 极限定理与收敛模式 | 13 年 / 26 | 概率 5（L^s 收敛＋一致可积）、概率 3（大数律/游走） |
| 3 估计理论（无偏/MLE/Fisher） | 13 年 / 23 | 概率 4（p̃ vs p̂ 与 ARE） |
| 4 随机游走 / Markov 链 / 随机过程 | 9 年 / 18 | 概率 3（赌徒输光，一切 p） |
| 5 渐近统计（Delta 方法/渐近正态） | 9 年 / 16 | 概率 4（Delta 方法） |
| 11 高维统计 / 统计学习 / 回归 | 5 年 / 7（近年升温） | 概率 1（FWL / 分块回归） |
| （附带，备选）顺序统计量/极值/记录 | 7 年 / 8 | 见 §5.3 备选题（2024 概率 Q5，已给出可靠答案） |

> 未覆盖：假设检验与区间估计（8 年 / 14）、经典随机模型（9 年 / 14）、条件期望与测度论概率（9 年 / 13）、概率不等式与集中（7 年 / 12）——原因与替代方案见 §0.7。

**约束三：难易搭配 2 易 / 3 中 / 1 难。** 难度采用与 `reports\yau_2024_2026_deep_analysis.md` 同一套 1–5 自评标准（1=期末基础；2=本科高年级标准题、一步构造；3=需 2–3 步组合技巧或非平凡计算；4=需研究生一年级工具或非标准构造；5=研究级工具）。本卷几何均值 (2+2+3+3+3+4)/6 = **2.83**，概率均值同为 **2.83**。

**约束四：符合"2024 年后几何卷 prove 占比上升"。** 我用当前 757 题文件重算了"题面含 prove/show that/justify/disprove"的比例（正则匹配，几何子集）：

| 年份 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | **2024** | **2025** | **2026** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prove 型占比 | 0.82 | 0.75 | 0.55 | 0.50 | 0.83 | 0.67 | 1.00 | 0.67 | **1.00** | **1.00** | **0.83** |

→ 2024–2026 三年**全部 ≥0.83**，明显高于 2018–2019（0.55 / 0.50）。**本卷几何 6 题全部为 prove/show 型**（无一道"纯计算"），与 2024 后的命题风格一致。概率卷同法统计为 2024=0.60、2025=0.75、2026=0.67，本卷概率 6 题中 5 题为 prove/derive 型。

### 0.6 与原卷的差别（必须知道的三点）

1. **跨年重组。** 本卷不复制任何一年的原卷：几何 = 2024 原创 3 题 ＋ 2026 原创 3 题；概率 = 2017 / 2020 / 2021 各 1 题 ＋ 2026 原创 3 题（2017 那题取自**团体卷**，在现代赛制下团体卷已不存在，故按"个人卷 6 题"体量重新安置）。
2. **加了原卷没有的东西。** 真实卷面**不给分值、不给总分**（多数年份只写"取最高的 5 题计分"或"全部必做"）。本卷为便于自评，增加 100 分制与分档给分细则（§2）；**题面本身一字未改**。
3. **难度结构比 2024/2025 概率卷低、比 2026 概率卷略低。**
   - 参考数值（`reports\yau_2024_2026_deep_analysis.md` §4/§9）：概率统计三年难度均值 **4.40 → 4.50 → 3.33**（2026 骤降 1.17，同时题量 4 → 6，是三年中唯一一次"降难增面"）；几何与拓扑 **3.33 → 3.67 → 4.00**（2026 升至三年最高）；2024–2026 全 101 题总加权均值 3.66。
   - 本卷按指定的"2 易 / 3 中 / 1 难"组卷，两科均值都是 2.83，**低于 2024/2025 概率卷、也低于 2026 概率卷的 3.33**。这是"2 易"配比带来的结构性后果，不是选材偏软：本卷 6 道中/难题（几何 1、4、5、6；概率 3、4、5、6）单看都在 3–4 档。
   - **若要贴近 2024/2025（4.4–4.5）的强度**，把 §5.3 的备选题换入即可：几何换入 2026 Q2（Gauss–Bonnet 刚性，难度 4）与 2025 Q6（Lefschetz，难度 4）；概率换入 2026 Q5（稳定分布，难度 5）与 2024 Q2（sup S_n/n，难度 5）——但后两道正是 §5.2 中我**给不出可靠答案**而弃用的题，**不建议**。

### 0.7 取舍的坦白说明（为什么"未覆盖"是必然的）

- **几何**：6 题装不下 21 个骨架标签。放弃的四类是**我判断在 6 题内无法同时满足"题面零损失 ＋ 答案可靠 ＋ 难度达标"**的：映射度/Hopf 不变量（2024 Q1、2020 Q1 均需大量指标计算与 Steenrod 方等工具）、测地线/Jacobi/第二变分（2020 Q3、2013 I3，题面抽取含大量下标损失）、示性类（2025 Q4、2019 I4，均需 Chern–Weil 形式的完整推导）、正曲率刚性（2013 I5、2018 I6，证明链条长且多为"陈述并证明标准定理"型，与"现代赛制不考陈述定理"的趋势相悖）。
- **概率**：同样装不下 11 个。放弃的"假设检验与区间估计"与"经典随机模型"是**最可惜**的两项：前者 2025 Q1 的抽取已损（`reports\yau_2024_2026_deep_analysis.md` 存疑表 U10：第 2 问缺少连接词、语义不完整），后者 2022 Q3（骰子模式 11 vs 12）答案可靠但难度仅 2，换入会使"2 易"超编。**若要补这两项，建议把 2024 概率 Q5（次序统计量/极值）换入，§5.3 已给出可靠答案。**

---

## §1 模拟卷正文（可直接打印）

> 打印说明：本段只含题面，不含任何答案。建议每科单独一张卷、限时 150 分钟。

---

### 第一卷：几何与拓扑（6 题，满分 100 分，建议用时 150 分钟）

**说明：全部 6 题必做。每一处断言、每一个例子都必须给出证明；无证明的断言不得分。**

---

**第 1 题（18 分）**

Let $M^n$ be a connected, closed, smooth, aspherical manifold of dimension $n \ge 1$, that is, its universal covering space $\tilde M$ is contractible.

(1) Prove that the universal cover $\tilde M$ is noncompact.

(2) Prove that every nontrivial element of $\pi_1(M)$ has infinite order.

---

**第 2 题（12 分）**

Let $(M,g)$ be a closed oriented $n$-dimensional Riemannian manifold. Let $p \in M$ and $\mathrm{Ric}_p$ be the Ricci curvature tensor at $p$; let $S_p$ be the scalar curvature at $p$, defined to be

$S_p := \frac1n \operatorname{Tr}_g(\mathrm{Ric}_p).$

Prove that the scalar curvature at $p$ is given by

$S_p = \frac{1}{\omega_{n-1}}\int_{S^{n-1}} \mathrm{Ric}_p(V,V)\, dS^{n-1},$

where $\omega_{n-1}$ is the area of the unit sphere $S^{n-1}$ in $T_pM$, $V \in S^{n-1}$ are unit vector fields, and $dS^{n-1}$ is the area element on $S^{n-1}$.

---

**第 3 题（12 分）**

Let $\Sigma \subset \mathbb R^3$ be an embedded surface in $\mathbb R^3$. A surface is called *minimal* if for any $p \in \Sigma$ we have $\kappa_1(p) + \kappa_2(p) = 0$, where $\kappa_1(p)$ and $\kappa_2(p)$ are the two principal curvatures at $p$. Prove that if $\Sigma$ is closed, then $\Sigma$ cannot be minimal.

---

**第 4 题（18 分）**

Let $M$ be a closed, simply connected $6$-dimensional manifold. Suppose $H_2(M) = \mathbb Z_2$. Prove that the Euler characteristic $\chi(M) \ne -1$.

---

**第 5 题（18 分）**

Let $S \subset \mathbb R^3$ be a smooth regular surface without boundary, and let $p \in S$. Let $\{A_\varepsilon\}_{\varepsilon>0}$ be a family of regions in $S$ such that each $A_\varepsilon$ contains $p$, has area $|A_\varepsilon|$, and shrinks to $\{p\}$ as $\varepsilon \to 0$. Let $N : S \to S^2$ be the Gauss map. Show that the Gaussian curvature at $p$ satisfies

$|K(p)| = \lim_{\varepsilon \to 0} \frac{\operatorname{Area}\big(N(A_\varepsilon)\big)}{\operatorname{Area}(A_\varepsilon)}.$

---

**第 6 题（22 分）**

Let $G$ be a connected $n$-dimensional Lie group equipped with a bi-invariant Riemannian metric $\langle \cdot,\cdot\rangle$.

(1) Show that the sectional curvature of $G$ is nonnegative.

(2) Assume that the Lie algebra $\mathfrak g$ of $G$ has trivial center, i.e. $z(\mathfrak g) := \{X \in \mathfrak g \mid [X,Y]=0\ \forall Y \in \mathfrak g\} = \{0\}$. Show that $G$ is compact.

(3) Suppose that $G$ is simply connected. Show that $G$ decomposes as a direct product

$G \cong G' \times \mathbb R^k,$

where $G'$ is a simply connected compact Lie group whose Lie algebra has trivial center, and $\mathbb R^k$ is the additive Lie group.

---
---

### 第二卷：概率与统计（6 题，满分 100 分，建议用时 150 分钟）

**说明：全部 6 题必做。每一处断言、每一个例子都必须给出证明；无证明的断言不得分。**

---

**第 1 题（12 分）**

Consider the partitioned linear regression model

$Y = X_1\beta_1 + X_2\beta_2 + \varepsilon,$

where $Y \in \mathbb R^n$, $X_1 \in \mathbb R^{n\times k_1}$, $X_2 \in \mathbb R^{n \times k_2}$, $k_1,k_2 \ge 1$, and $[X_1\ X_2]$ has full column rank. Define the annihilator matrix

$M_1 = I_n - X_1(X_1^{\top}X_1)^{-1}X_1^{\top},$

which projects onto the orthogonal complement of the column space of $X_1$. Recall that for a generic regression of a response $\tilde Y$ on a predictor matrix $\tilde X$ with full column rank, the OLS estimator is $\hat\beta = (\tilde X^{\top}\tilde X)^{-1}\tilde X^{\top}\tilde Y$.

Prove: the OLS estimator $\hat\beta_2$ obtained from the full regression of $Y$ on $[X_1\ X_2]$ is identical to the OLS estimator obtained from regressing $M_1Y$ on $M_1X_2$.

---

**第 2 题（12 分）**

Let $\varphi$ and $\Phi$ be the density and distribution functions of the standard normal, and let $a>0$ be a constant.

(a) Show that $f(x) = 2\varphi(x)\Phi(ax)$ is the density of some random variable (denoted by $Y$).

(b) Calculate $E(Y)$.

---

**第 3 题（18 分）**

Consider the random walk

$S_n = a + X_1 + X_2 + \cdots + X_n,$

where $a$ is a positive integer and $\{X_i\}$ are independent and identically distributed random variables with common distribution

$P\{X_i = 1\} = p, \qquad P\{X_i = -1\} = 1-p .$

Let $\tau_0 = \inf\{n : S_n = 0\}$ be the first time the random walk reaches the state $x=0$. For **all** $p \in [0,1]$ find the probability $P_a\{\tau_0 < \infty\}$ that the random walk will eventually hit the state $x=0$.

---

**第 4 题（18 分）**

Suppose $X_1,\dots,X_n$ are i.i.d. Poisson variables with mean $\lambda$, and we are interested in estimating $p = P_\lambda(X_i = 0) = e^{-\lambda}$.

(a) One estimator for $p$ is the proportion of zeros in the sample, $\tilde p = \#\{i \le n : X_i = 0\}/n$. Determine the limiting distribution of $\sqrt n(\tilde p - p)$.

(b) Another estimator would be the maximum likelihood estimator $\hat p$. Give a formula for $\hat p$ and determine the limiting distribution of $\sqrt n(\hat p - p)$.

(c) Find the asymptotic relative efficiency of $\tilde p$ with respect to $\hat p$.

---

**第 5 题（18 分）**

Suppose that a sequence $\{X_n\}$ of real-valued random variables converges to $X$ in distribution, and there are positive constants $r$ and $C$ such that $E|X_n|^r \le C$ for all $n$. Show that

$\lim_{n\to\infty} E|X_n|^s = E|X|^s \qquad \text{for all } 0 < s < r .$

---

**第 6 题（22 分）**

Let $\xi$ and $\eta$ be independent random variables. If the sum $S = \xi + \eta$ and the difference $D = \xi - \eta$ are also independent, then $\xi$ and $\eta$ must follow normal distributions.

> （提示：本题**不存在任何矩条件假设**；一切论证必须只用特征函数与连续性完成。）

---

## §2 参考答案与评分标准

> 记号约定：$\Delta = \Delta_g$ 为 Laplace–Beltrami 算子（$\Delta f = \operatorname{div}(\nabla f) = \operatorname{tr}\,\mathrm{Hess} f$）；$\langle\cdot,\cdot\rangle$ 为 $g$ 或双不变度规；$B$ 为 Killing 型；$\varphi_X$ 为 $X$ 的特征函数。"满分"条目列出该题必须出现的关键步骤；缺哪个步骤就扣哪一项。

### 几何 1（2026 Q5，18 分）aspherical 流形

**答案：两个结论都成立。**

**(1) $\tilde M$ 非紧（6 分）。** 反设 $\tilde M$ 紧。由覆叠 $p:\tilde M \to M$ 是局部同胚且 $M$ 紧，得 $p$ 是**有限叶**覆叠，从而 $\tilde M$ 是闭（紧无边）连通 $n$ 维流形。闭连通 $n$ 维流形的最高同调 $H_n(\tilde M;\mathbb Z_2)\cong \mathbb Z_2 \ne 0$。但 $\tilde M$ 可缩，故对 $n\ge 1$ 有 $H_n(\tilde M;\mathbb Z_2)=0$。矛盾。故 $\tilde M$ 非紧。∎

**(2) $\pi_1(M)$ 无有限阶非平凡元（12 分）。** 设 $1\ne g \in \pi_1(M)$，$g^k=1$，$k\ge 2$。令 $\Gamma = \langle g\rangle \cong \mathbb Z_k$。$\Gamma$ 通过覆叠变换**自由、真不连续**地作用在 $\tilde M$ 上，故商 $N := \tilde M/\Gamma$ 是光滑 $n$ 维流形，且 $\tilde M \to N$ 是以 $\Gamma$ 为覆叠变换群的覆叠映射。由于 $\tilde M$ 可缩，$\tilde M$ 就是 $N$ 的万有覆叠，于是

$\pi_1(N) \cong \mathbb Z_k,\qquad \pi_i(N) = 0\ (i \ge 2),$

即 $N$ 是 $K(\mathbb Z_k,1)=B\mathbb Z_k$ 的模型。因此对一切 $i \ge 0$，

$H_i(N;\mathbb Z_2) \cong H_i(\mathbb Z_k;\mathbb Z_2) \cong \mathbb Z_2 \ne 0 .$

（有限循环群以 $\mathbb Z_2$ 为系数的群同调在每个度都是 $\mathbb Z_2$：用标准自由消解 $\cdots \to \mathbb Z[\mathbb Z_k]\xrightarrow{N}\mathbb Z[\mathbb Z_k]\xrightarrow{1-t}\mathbb Z[\mathbb Z_k]\to \mathbb Z$，张量上 $\mathbb Z_2$ 后范元 $N$ 与 $1-t$ 都化为 $0$，故所有边界映射为 $0$。）

特别地 $H_{n+1}(N;\mathbb Z_2)\ne 0$。但 $N$ 是 $n$ 维流形，对 $i>n$ 必有 $H_i(N;\mathbb Z_2)=0$（非紧流形的 Poincaré 对偶 $H_i(N;\mathbb Z_2)\cong H^{n-i}_c(N;\mathbb Z_2)=0$）。矛盾。故 $\pi_1(M)$ 扭自由。∎

**分档给分**
- **满分（18）**：两问都完成；第 (2) 问必须**显式出现**"$N=\tilde M/\langle g\rangle$ 是 $B\mathbb Z_k$"与"$H_i(B\mathbb Z_k;\mathbb Z_2)=\mathbb Z_2$ 对一切 $i$"这两步，并指出与 $n$ 维流形的高维同调消失矛盾。
- **部分分（12–17）**：第 (1) 问完整；第 (2) 问只证出"$g$ 有限阶 ⇒ $g$ 在 $\tilde M$ 上有不动点"但**没有合法依据**（例如直接对**非紧**流形引用 Lefschetz 不动点定理而不作紧化/说明），或只说"显然有限群自由作用不可能"。
- **零分**：把"万有覆叠可缩 ⇒ 非紧"当作显然；或把"$\chi(M)\ne 0$"之类的不变量当作判据；或第 (2) 问只重复题设。

### 几何 2（2024 Q4，12 分）标量曲率 = Ricci 在单位球面上的平均

**答案：$S_p=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)=\frac{1}{\omega_{n-1}}\int_{S^{n-1}}\mathrm{Ric}_p(V,V)dS^{n-1}$。**

**证明.** 取 $T_pM$ 的一组 $g$-标准正交基 $e_1,\dots,e_n$，记 $R_{ij}=\mathrm{Ric}_p(e_i,e_j)$，并令 $V=\sum_i V^i e_i$ 在单位球面 $S^{n-1}\subset T_pM$ 上按（归一化的）面积测度均匀取值。则

$\frac{1}{\omega_{n-1}}\int_{S^{n-1}}\mathrm{Ric}_p(V,V)dS^{n-1} = \mathbb E\left[\sum_{i,j}R_{ij}V^iV^j\right] = \sum_{i,j}R_{ij}\,\mathbb E[V^iV^j].$

矩阵 $\big(\mathbb E[V^iV^j]\big)_{ij}$ 在正交群 $O(n)$ 的作用下不变（球面测度与二次型表达式都在 $O(n)$ 下不变），故它是数量矩阵 $cI$；取迹得 $\sum_i\mathbb E[(V^i)^2]=\mathbb E|V|^2=1$，于是 $nc=1$，$c=1/n$。代入得

$\frac{1}{\omega_{n-1}}\int_{S^{n-1}}\mathrm{Ric}_p(V,V)dS^{n-1}=\frac1n\sum_i R_{ii}=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)=S_p . \qquad \blacksquare$

**分档给分**
- **满分（12）**：写出 $\mathbb E[V^iV^j]=\delta_{ij}/n$ 并**给出理由**（$O(n)$ 不变性 ＋ 取迹），然后代入。
- **部分分（6–11）**：只在 $\mathrm{Ric}_p$ 对角（取 $e_i$ 为其特征向量）的情形证，或直接断言"由对称性平均得 $\frac1n\mathrm{Tr}$"而不说明。
- **零分**：把 $S_p$ 当作通常约定的 $\operatorname{Tr}(\mathrm{Ric}_p)$ 计算（本题题面**明确定义** $S_p=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)$，用错约定会差因子 $n$）；或只写"这是标准事实"。

### 几何 3（2024 Q2，12 分）R³ 中闭极小嵌入曲面不存在

**答案：不存在。**

**证明.** 设 $\Sigma\subset\mathbb R^3$ 闭（紧、无边）且极小，即 $H=\frac{\kappa_1+\kappa_2}{2}\equiv 0$。把位置向量 $x:\Sigma\to\mathbb R^3$ 的坐标函数 $x^1,x^2,x^3$ 看作 $\Sigma$ 上的函数，则对等距浸入有

$\Delta x = 2H\,\vec n .$

由于 $H\equiv 0$，$\Delta x = 0$，即三个坐标函数都是 $\Sigma$ 上的调和函数。$\Sigma$ 紧（无边），由最大值原理，紧无边流形上的调和函数必为常数，故 $x$ 为常向量，$\Sigma$ 至多是一个点，与"曲面"矛盾。∎

**另一种等价做法（同样满分）**：令 $f=|x|^2$。取 $\Sigma$ 的局部标准正交标架 $e_1,e_2$，可得

$\Delta |x|^2 = 2\langle x,\Delta x\rangle + 2\sum_{i=1}^3|\nabla x^i|^2 = 0 + 2\sum_{i}\sum_{j=1}^2\big(e_j(x^i)\big)^2 = 2\sum_{j=1}^2|e_j|^2 = 4 .$

即 $\Delta|x|^2\equiv 4>0$ 处处成立；但紧无边流形上 $\int_\Sigma \Delta|x|^2\,dA = 0$（Stokes），于是 $0=4\,\mathrm{Area}(\Sigma)>0$，矛盾。（也可用最大值原理：$|x|^2$ 在某点取最大，该点处 $\Delta|x|^2\le 0$，与 $=4$ 矛盾。）

**分档给分**
- **满分（12）**：给出 $\Delta x = 2H\vec n$（或 $\Delta|x|^2=4$ 的计算）并正确使用紧性 ＋ 最大值原理/Stokes 收尾。
- **部分分（5–11）**：知道"极小 ⇒ 坐标函数调和"并由此说"故有界"，但**没有**用紧性把它推到"常数"，或漏掉"闭 = 紧无边"这一步；或者只对 $|x|^2$ 用最大值原理但漏算 $\Delta|x|^2=4$（写成 $2H\langle x,n\rangle$ 后无法定号）。
- **零分**：只引用"R³ 中不存在紧极小曲面"这一结论而不证明；或把"紧"误解为"有界闭集"从而试图用 $\mathbb R^3$ 的整体结果。

### 几何 4（2024 Q3，18 分）$\chi(M)\ne -1$

**答案：$\chi(M)\ne -1$（事实上 $\chi(M)$ 必为偶数）。**

**证明.** $M$ 闭、单连通 ⇒ $\pi_1(M)=0$ ⇒ $H_1(M;\mathbb Z)=0$，从而 $H^1(M;\mathbb Z_2)\cong \operatorname{Hom}(H_1(M;\mathbb Z),\mathbb Z_2)=0$，第一 Stiefel–Whitney 类 $w_1=0$，即 $M$ **可定向**。故 Poincaré 对偶成立，Betti 数满足 $b_k=b_{6-k}$，其中 $b_k=\dim_{\mathbb Q}H_k(M;\mathbb Q)$。

由单连通，$b_0=b_6=1$，$b_1=b_5=0$。由题设关于 $H_2$ 的两种读法分别讨论：

- **读法 A：$H_2(M;\mathbb Z)\cong \mathbb Z_2$（抽取值 $Z_2$ 表示循环群 $\mathbb Z/2$）**：则 $H_2(M;\mathbb Q)=H_2(M;\mathbb Z)\otimes\mathbb Q=0$，故 $b_2=0$，于是 $b_4=b_2=0$，得

$\chi(M)=1-0+b_2-b_3+b_4-0+1 = 2-b_3 .$

- **读法 B：$H_2(M;\mathbb Z)\cong \mathbb Z^2$（$Z_2$ 表示 $\mathbb Z^{\oplus 2}$）**：则 $b_2=b_4=2$，得

$\chi(M)=1+2-b_3+2+1 = 6-b_3 .$

两种读法下都只需再证 **$b_3$ 是偶数**：$M$ 紧可定向 6 维，杯积配对

$H^3(M;\mathbb Q)\times H^3(M;\mathbb Q)\to H^6(M;\mathbb Q)\cong\mathbb Q$

由 Poincaré 对偶非退化，且因 $3\cdot(6-3)=9$ 为奇数而**交错**（$\alpha\cup\beta=-\beta\cup\alpha$）；非退化交错双线性型所在空间的维数必为偶数，故 $b_3$ 为偶数。

于是 $\chi(M)=2-b_3$（读法 A）或 $6-b_3$（读法 B）**恒为偶数**；而 $-1$ 是奇数，故 $\chi(M)\ne -1$。∎

> 附注（不在给分要求内）：读法 A 下 $b_3\ge 0$ 偶数，故 $\chi(M)\equiv 2 \pmod 2$；读法 B 下 $\chi(M)\equiv 0\pmod 2$。两种读法结论一致，因此**抽取上下标丢失不影响本题可判**。

**分档给分**
- **满分（18）**：明确写出 $\chi=1+b_2-b_3+b_4+1$ 的展开；用 $b_3$ 偶数（**说清交错性来源**：$3\cdot3=9$ 为奇）收尾；对 $H_2=\mathbb Z_2$ 的记号歧义有处理（或明确采用一种读法并说明另一种同结论）。
- **部分分（9–17）**：知道用 Poincaré 对偶与 $\chi$ 的展开，但**漏掉"$b_3$ 偶数"**这一步（此时只能得到 $\chi=2-b_3$，无法排除 $-1$），或漏证可定向性。
- **零分**：直接写"$\chi$ 为偶数所以 $\ne -1$"而不给理由；或把 $H_2=\mathbb Z_2$ 误读为"秩 2"后仍不做任何对偶论证。

### 几何 5（2026 Q1，18 分）Gauss 映射的面积伸缩率

**答案：$|K(p)| = \lim_{\varepsilon\to0}\operatorname{Area}(N(A_\varepsilon))/\operatorname{Area}(A_\varepsilon)$。**

**证明.** 设 $S$ 定向（局部即可），$N:S\to S^2$ 为 Gauss 映射，则 $dN_p = -S_p$（$S_p$ 为形状算子，即 Weingarten 映射），于是

$\det dN_p = \det(-S_p) = (-1)^2\det S_p = K(p) .$

（$\dim S=2$，$S_p$ 的两个特征值是主曲率 $\kappa_1,\kappa_2$，$\det S_p=\kappa_1\kappa_2=K$。）

**面积公式。** 对 Lipschitz 映射 $N$ 与可测集 $A_\varepsilon\subset S$，面积公式（area formula）给出"按重数计"的像面积

$\int_{A_\varepsilon}|K|\,dA = \int_{A_\varepsilon}|\det dN|\,dA = \int_{S^2}\#\{N^{-1}(y)\cap A_\varepsilon\}\,dy \ \ge\ \operatorname{Area}\big(N(A_\varepsilon)\big).$

分两种情形取极限：

- **若 $K(p)\ne 0$**：由反函数定理，存在 $p$ 的邻域 $U$ 使 $N|_U$ 是到其像的微分同胚；$A_\varepsilon$ 收缩到 $\{p\}$ 故当 $\varepsilon$ 充分小时 $A_\varepsilon\subset U$，此时 $N$ 在 $A_\varepsilon$ 上单射，重数恒为 1，于是

$\operatorname{Area}\big(N(A_\varepsilon)\big)=\int_{A_\varepsilon}|K|\,dA,\qquad \frac{\operatorname{Area}(N(A_\varepsilon))}{|A_\varepsilon|}=\frac{1}{|A_\varepsilon|}\int_{A_\varepsilon}|K|\,dA \xrightarrow[\varepsilon\to0]{} |K(p)|$

（$K$ 连续；最后一个极限是连续函数在收缩区域上的平均值）。

- **若 $K(p)=0$**：由 $|K|$ 在 $p$ 连续，任给 $\delta>0$，当 $\varepsilon$ 小时 $\sup_{A_\varepsilon}|K|\le\delta$，故

$0\le \frac{\operatorname{Area}(N(A_\varepsilon))}{|A_\varepsilon|}\le \frac{1}{|A_\varepsilon|}\int_{A_\varepsilon}|K|\,dA\le \delta ,$

即该比值的 $\limsup \le \delta$；$\delta$ 任意，故极限为 $0=|K(p)|$。

两种情形合起来即得结论。∎

**分档给分**
- **满分（18）**：写出 $\det dN_p=K(p)$；用面积公式（或说明"按重数计"）处理**非单射**的情形；**分别**处理 $K(p)\ne0$ 与 $K(p)=0$ 两种情形中的至少一种、并说明另一种可由连续性夹逼。
- **部分分（8–17）**：只写"$\det dN_p=K(p)$，故比值趋于 $|K|$"而完全不处理 $K(p)=0$ 时 $N$ 未必单射的问题（这是本题唯一的真陷阱）；或把 $\operatorname{Area}(N(A_\varepsilon))$ 直接等于 $\int_{A_\varepsilon}|K|$ 而不加"按重数计"的说明——若在 $K(p)\ne0$ 情形下用反函数定理补上单射性，可给部分分上限。
- **零分**：把 $dN_p$ 的行列式写成 $K$ 的平方；或结论写成 $K(p)$ 而非 $|K(p)|$ 且不提绝对值来自面积的可加性。

### 几何 6（2026 Q3，22 分）双不变度规 Lie 群

**(1) 截面曲率非负（6 分）。**
双不变度规下，左不变向量场满足 Koszul 公式给出的

$\nabla_X Y = \tfrac12[X,Y]\qquad (X,Y \in \mathfrak g \text{ 左不变}).$

于是对正交单位对 $X,Y$，

$R(X,Y)Z = \nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z = \tfrac14[X,[Y,Z]] - \tfrac14[Y,[X,Z]] - \tfrac12[[X,Y],Z] = -\tfrac14[[X,Y],Z],$

$K(X,Y) = \langle R(X,Y)Y, X\rangle = -\tfrac14\big\langle [[X,Y],Y],X\big\rangle = \tfrac14\big\langle [X,Y],[X,Y]\big\rangle = \tfrac14|[X,Y]|^2 \ \ge 0$

（最后一步用了度规的 $\mathrm{ad}$-不变性：由 $\langle [Z,Y],X\rangle = -\langle Y,[Z,X]\rangle$ 取 $Z=[X,Y]$ 得 $\langle[[X,Y],Y],X\rangle = -|[X,Y]|^2$）。∎

**(2) $z(\mathfrak g)=0 \Rightarrow G$ 紧（8 分）。**
因度规双不变，$\mathrm{ad}_X$ 对 $\langle\cdot,\cdot\rangle$ 反自伴：$\langle \mathrm{ad}_X Y,Z\rangle = -\langle Y,\mathrm{ad}_X Z\rangle$。故 $\mathrm{ad}_X$ 的特征值全为纯虚数，从而 Killing 型

$B(X,X) = \operatorname{tr}(\mathrm{ad}_X\circ \mathrm{ad}_X) = \sum_i \lambda_i^2 \le 0$

（$\lambda_i$ 为纯虚特征值），且等号成立 $\iff \mathrm{ad}_X=0 \iff X\in z(\mathfrak g)=\{0\}$。于是 $B$ 在 $\mathfrak g$ 上**负定**。

由 Cartan 判据的标准推论：Killing 型负定的实 Lie 代数 $\mathfrak g$ 是紧型 Lie 代数，与其对应的**单连通** Lie 群 $\tilde G$ 紧。又 $G=\tilde G/\pi_1(G)$ 是紧群 $\tilde G$ 的连续同态像（$\pi_1(G)$ 是 $\tilde G$ 的离散中心子群，因而闭），故 $G$ 紧。∎

**(3) $G$ 单连通 $\Rightarrow G\cong G'\times\mathbb R^k$（8 分）。**

**第一步：正交分解 $\mathfrak g = z(\mathfrak g)\oplus[\mathfrak g,\mathfrak g]$。** 由度规的 $\mathrm{ad}$-不变性，

$X\perp[\mathfrak g,\mathfrak g] \iff \langle X,[Y,Z]\rangle = 0\ \forall Y,Z \iff \langle [X,Y],Z\rangle = 0\ \forall Y,Z \iff [X,Y]=0\ \forall Y \iff X\in z(\mathfrak g).$

故 $[\mathfrak g,\mathfrak g]^{\perp}=z(\mathfrak g)$，而度规正定非退化给出 $\mathfrak g = z(\mathfrak g)\oplus[\mathfrak g,\mathfrak g]$（正交直和）。

**第二步：直积分解。** 记 $\mathfrak g' = [\mathfrak g,\mathfrak g]$（是理想），$Z=\exp(z(\mathfrak g))$，$G'$ 为 $\mathfrak g'$ 生成的连通 Lie 子群。由 $[z(\mathfrak g),\mathfrak g]=0$ 知 $Z$ 与 $G'$ 交换，乘法映射

$\Phi: Z\times G' \to G,\qquad (z,g')\mapsto zg'$

是 Lie 群同态，且 $d\Phi$ 在单位元处是 $\mathfrak g=z(\mathfrak g)\oplus\mathfrak g'$ 的同构，故 $\Phi$ 是**局部同构**，从而是覆叠同态（其像是开子群，而 $G$ 连通故满）。$G$ 单连通且 $Z\times G'$ 连通，故覆叠 $\Phi$ 只有一叶，$\Phi$ 是同构：

$G\cong Z\times G' .$

又 $Z$ 是连通交换 Lie 群，$\exp: z(\mathfrak g)\to Z$ 是覆叠同态；由 $G\cong Z\times G'$ 单连通知 $Z$ 单连通，故 $Z\cong \mathbb R^k$。

**第三步：$G'$ 的性质。** $G'$ 是单连通 $G$ 的直因子，故单连通；它带有限制到 $\mathfrak g'$ 的双不变度规。

*$\mathfrak g'$ 的中心为 0：* 若 $X\in\mathfrak g'$ 且 $[X,\mathfrak g']=0$，则又因 $[\mathfrak g',z(\mathfrak g)]=0$ 得 $[X,\mathfrak g]=0$，即 $X\in z(\mathfrak g)\cap\mathfrak g'=0$。由 (2)（适用于连通群 $G'$，其 Lie 代数中心平凡）得 $G'$ **紧**。

于是 $G\cong G'\times\mathbb R^k$，$G'$ 单连通紧、其 Lie 代数中心平凡。∎

**分档给分**
- **满分（22）**：(1) 给出 $\nabla_XY=\frac12[X,Y]$ 与 $K=\frac14|[X,Y]|^2$（**1/4 因子必须正确**）；(2) 走通"$\mathrm{ad}$ 反自伴 ⇒ Killing 型负定 ⇒ 紧型 ⇒（单连通覆盖紧）⇒ $G$ 紧"这条链，并**说明为何由单连通覆盖的紧性回到 $G$**；(3) 出现 $[\mathfrak g,\mathfrak g]^\perp=z(\mathfrak g)$ 这一步，并用它构造 $Z\times G'\to G$ 的覆叠同态。
- **部分分（12–21）**：(1) 正确；(2) 只证"$G/Z(G)$ 同构于紧群 $O(\mathfrak g)$ 的子群"就宣称 $G$ 紧（缺"闭性/有限性"说明）；(3) 只做出 $G\cong Z\times G'$ 但没证 $G'$ 的中心平凡（这是 (2) 能用在 $G'$ 上的前提），或漏证 $Z\cong\mathbb R^k$。
- **零分**：曲率公式写成 $K=\frac12|[X,Y]|^2$ 或漏掉平方；把"$z(\mathfrak g)=0$"与"$Z(G)$ 平凡"混为一谈而不区分（$z(\mathfrak g)=0$ 只给出 $Z(G)$ **离散**）；(3) 中把 $\mathfrak g=z(\mathfrak g)\oplus[\mathfrak g,\mathfrak g]$ 当作"显然"（这正是需要 $\mathrm{ad}$-不变性来证的一步）。

### 概率 1（2026 Q2，12 分）分块回归（FWL）

**答案：两者恒等。**

**证明.** 全回归 $Y\sim[X_1\ X_2]$ 的正规方程为

$X_1^{\top}\big(Y-X_1\hat\beta_1-X_2\hat\beta_2\big)=0,\qquad X_2^{\top}\big(Y-X_1\hat\beta_1-X_2\hat\beta_2\big)=0 .$

由第一式（$X_1^{\top}X_1$ 可逆，因 $[X_1\ X_2]$ 列满秩）

$\hat\beta_1 = (X_1^{\top}X_1)^{-1}X_1^{\top}\big(Y-X_2\hat\beta_2\big).$

代入第二式：

$X_2^{\top}\Big(\big(I-X_1(X_1^{\top}X_1)^{-1}X_1^{\top}\big)\big(Y-X_2\hat\beta_2\big)\Big)=0,\qquad\text{即}\qquad X_2^{\top}M_1\big(Y-X_2\hat\beta_2\big)=0 .$

故 $X_2^{\top}M_1X_2\,\hat\beta_2 = X_2^{\top}M_1Y$。又 $M_1$ 对称幂等，故

$(M_1X_2)^{\top}(M_1Y)=X_2^{\top}M_1Y,\qquad (M_1X_2)^{\top}(M_1X_2)=X_2^{\top}M_1X_2 .$

因此 $M_1X_2$ 列满秩（若 $M_1X_2v=0$，则 $X_2v\in\operatorname{col}(X_1)$，与 $[X_1\ X_2]$ 列满秩矛盾），并且把 $M_1Y$ 对 $M_1X_2$ 回归得到的 OLS 估计恰为

$\big[(M_1X_2)^{\top}(M_1X_2)\big]^{-1}(M_1X_2)^{\top}(M_1Y)=\big(X_2^{\top}M_1X_2\big)^{-1}X_2^{\top}M_1Y=\hat\beta_2 . \qquad \blacksquare$

**分档给分**
- **满分（12）**：写出全回归的两个正规方程、消去 $\hat\beta_1$、用 $M_1$ 的对称幂等性把两边改写为缩减回归的正规方程，并说明 $M_1X_2$ 列满秩。
- **部分分（6–11）**：只写出正规方程后直接断言"两边相同"；或用了 $M_1$ 但没说明其对称幂等性。
- **零分**：把结论说成"$\hat\beta_1$ 也相同"（一般不成立）；或假设 $X_1^{\top}X_2=0$（正交设计）后才做，属于额外假设。

### 概率 2（2026 Q3，12 分）偏正态密度与均值

**(a) 是密度（5 分）。** $f(x)=2\varphi(x)\Phi(ax)\ge 0$ 显然。又

$\int_{\mathbb R}2\varphi(x)\Phi(ax)\,dx = 2\,\mathbb E[\Phi(aX)],\qquad X\sim N(0,1).$

由 $\Phi(t)+\Phi(-t)=1$ 与对称性 $X\overset{d}{=}-X$ 得 $\mathbb E[\Phi(aX)]=\mathbb E[\Phi(-aX)]$，于是

$1=\mathbb E[\Phi(aX)+\Phi(-aX)]=2\mathbb E[\Phi(aX)] \ \Longrightarrow\ \int_{\mathbb R} f = 1 .$

故 $f$ 是概率密度（即偏正态 $SN(0,1,a)$ 的密度）。∎

**(b) $E(Y)=\sqrt{\dfrac{2}{\pi}}\cdot\dfrac{a}{\sqrt{1+a^2}}$（7 分）。**
取 $Z\sim N(0,1)$ 与 $X$ 独立，则 $\Phi(ax)=\Pr(Z\le ax)$，故

$\mathbb E[Y] = 2\int_{\mathbb R}x\varphi(x)\Phi(ax)dx = 2\,\mathbb E\big[X\,\mathbf 1_{\{Z\le aX\}}\big] = 2\,\mathbb E\big[X\,\mathbf 1_{\{W\le0\}}\big],\qquad W:=Z-aX .$

$(X,W)$ 联合正态、均值为零，$\operatorname{Cov}(X,W)=-a$，$\operatorname{Var}(W)=1+a^2$，且

$\mathbb E[X\mid W]=\frac{\operatorname{Cov}(X,W)}{\operatorname{Var}(W)}\,W = \frac{-a}{1+a^2}W .$

于是

$\mathbb E\big[X\mathbf 1_{\{W\le0\}}\big]=\frac{-a}{1+a^2}\mathbb E\big[W\mathbf 1_{\{W\le0\}}\big]=\frac{-a}{1+a^2}\cdot\Big(-\frac{\sqrt{1+a^2}}{\sqrt{2\pi}}\Big)=\frac{a}{\sqrt{2\pi(1+a^2)}} ,$

故 $\mathbb E[Y]=2\cdot\frac{a}{\sqrt{2\pi(1+a^2)}}=a\sqrt{\frac{2}{\pi(1+a^2)}}$，即 $\mathbb E[Y]=\delta\sqrt{2/\pi}$，$\delta=a/\sqrt{1+a^2}$。合理性校验：$a\to\infty$ 时趋于 $\sqrt{2/\pi}$（半正态均值），$a\to0^+$ 时趋于 $0$（对称）。∎

**分档给分**
- **满分（12）**：(a) 用 $\Phi(t)+\Phi(-t)=1$ ＋ 对称性完成归一；(b) 化成 $\mathbb E[X\mathbf 1_{\{Z\le aX\}}]$ 后用 $W=Z-aX$ 的联合正态算出 $\frac{a}{\sqrt{2\pi(1+a^2)}}$。
- **部分分（5–10）**：(a) 只验 $f\ge0$ 与"由文献知是偏正态密度"；(b) 答案正确但用未经说明的"$\mathbb E[Xh(W)]=\operatorname{Cov}(X,W)\mathbb E[h'(W)]$"直接对示性函数 $h$ 求导（不合法，需平滑逼近或以 $\mathbb E[X|W]$ 论证）。
- **零分**：漏掉因子 2（给出 $\frac12 a\sqrt{\dots}$ 级答案）；或把结论写成 $\frac{a}{\sqrt{1+a^2}}$（漏 $\sqrt{2/\pi}$）。

### 概率 3（2020 Q3，18 分）赌徒输光的命中概率

**答案（对一切 $p\in[0,1]$）：**

$P_a\{\tau_0<\infty\}=\begin{cases} \left(\dfrac{1-p}{p}\right)^{a}, & p>\tfrac12,\\[2mm] 1, & p\le \tfrac12 .\end{cases}$

（约定 $p=0$ 时左式为 $+\infty$，取 $1$；$p=1$ 时为 $0^a=0$。）

**证明.** 令 $\rho=\dfrac{1-p}{p}$（$p>0$）、$\psi(x)=\rho^{\,x}$。则 $\psi$ 关于该游走是调和的：

$\mathbb E[\psi(S_{n+1})\mid S_n=x]=\psi(x)\big(p\rho+(1-p)\rho^{-1}\big)=\psi(x)\big((1-p)+p\big)=\psi(x).$

- **$p>1/2$**：$\rho<1$，$\psi$ 递减，$\psi(0)=1>\psi(a)$。对停时 $\tau=\tau_0\wedge\tau_M$（$M>a$，有界停时）用可选停止定理，
$1=\psi(a)\,P_a\{\tau_0<\tau_M\}+\mathbb E\big[\psi(S_\tau)\mathbf 1_{\{\tau_0>\tau_M\}}\big] .$
由 $\psi(S_\tau)\le\rho^{M}\to0$（$M\to\infty$）得 $1=\psi(a)\,P_a\{\tau_0<\infty\}$，即 $P_a\{\tau_0<\infty\}=\rho^{a}=\big(\tfrac{1-p}{p}\big)^{a}$。
- **$p<1/2$**：$S_n\to-\infty$ a.s.（强大数律，$\mathbb E X_i=2p-1<0$），而 $\pm1$ 游走（向下漂移）必经过每个低于出发点的层，故 $\tau_0<\infty$ a.s.，概率为 $1$。
- **$p=1/2$**：一维对称简单随机游走常返，故 $\tau_0<\infty$ a.s.，概率为 $1$。∎

**分档给分**
- **满分（18）**：三段讨论齐全；$p>1/2$ 给出 $\rho^{a}$ 并**给出调和函数 ＋ 停时的论证**；$p\le1/2$ 说明常返/负漂移。
- **部分分（9–17）**：只给对 $p>1/2$ 的公式 $\big(\tfrac{1-p}{p}\big)^a$（漏掉 $p\le1/2$ 时恒为 1，或把两种情形写反）；或只写"由经典赌徒输光公式"而不证。
- **零分**：写成 $\big(\tfrac{p}{1-p}\big)^{a}$；或用 $a\to\infty$ 的极限与漂移方向矛盾（例如对一切 $p$ 答 $1$）。

### 概率 4（2017 团体 Q5，18 分）$p=e^{-\lambda}$ 的估计与 ARE

记 $p=e^{-\lambda}$，$\hat\lambda=\bar X_n$，$\hat p=e^{-\bar X_n}$。

**(a)（5 分）** $\tilde p=\frac1n\sum_i \mathbf 1_{\{X_i=0\}}$ 是 i.i.d. Bernoulli($p$) 的均值，由 CLT

$\sqrt n(\tilde p-p)\xrightarrow{d} N\big(0,\ p(1-p)\big)=N\big(0,\ e^{-\lambda}(1-e^{-\lambda})\big).$

**(b)（7 分）** MLE：$\hat\lambda=\bar X_n$（Poisson 族的 MLE），由不变性 $\hat p=e^{-\bar X_n}$。由 CLT $\sqrt n(\bar X_n-\lambda)\xrightarrow{d}N(0,\lambda)$，并对 $g(\lambda)=e^{-\lambda}$ 用 **Delta 方法**（$g'(\lambda)=-e^{-\lambda}$）：

$\sqrt n(\hat p-p)\xrightarrow{d} N\Big(0,\ \lambda\,e^{-2\lambda}\Big).$

**(c)（6 分）** 渐近相对效率（以 $\hat p$ 为基准）

$\mathrm{ARE}(\tilde p:\hat p)=\frac{\text{asymp. Var}(\hat p)}{\text{asymp. Var}(\tilde p)}=\frac{\lambda e^{-2\lambda}}{e^{-\lambda}(1-e^{-\lambda})}=\frac{\lambda e^{-\lambda}}{1-e^{-\lambda}}=\frac{\lambda}{e^{\lambda}-1} .$

性质：因 $e^\lambda-1\ge\lambda$，恒有 $\mathrm{ARE}\le1$（即 $\hat p$ 渐近不劣于 $\tilde p$）；$\lambda\to0$ 时 $\mathrm{ARE}\to1$；$\lambda\to\infty$ 时 $\mathrm{ARE}\to0$（指数级低效——"零的比例"在大 $\lambda$ 下几乎不携带 $p$ 的信息）。∎

**分档给分**
- **满分（18）**：三问全对；(b) 明确用 Delta 方法并给出方差 $\lambda e^{-2\lambda}$；(c) 给出 $\lambda/(e^\lambda-1)$ 并说明 $\le1$。
- **部分分（9–17）**：(a)(b) 对而 (c) 把 ARE 的方向写反（给成 $(e^\lambda-1)/\lambda$），或 (b) 只给 $\hat p$ 的公式不算极限分布，或漏掉 $g'(\lambda)^2$ 只写 $e^{-2\lambda}$ 而漏 $\lambda$。
- **零分**：把 MLE 写成 $\tilde p$ 或 $\hat p=1-\bar X_n$；或只宣布"由 MLE 的渐近正态性"而不做任何计算。

### 概率 5（2021 概率 Q1，18 分）$L^s$ 收敛

**答案：结论成立；且 $0<s<r$ 的上界是最优的（$s=r$ 时结论不成立）。**

**证明.**

**第一步：$\{|X_n|^s\}$ 一致可积（8 分）。** 对 $M>0$，由 Hölder（指数 $r/s>1$ 与共轭指数）与 Markov：

$\mathbb E\big[|X_n|^s\mathbf 1_{\{|X_n|>M\}}\big]\le \big(\mathbb E|X_n|^r\big)^{s/r}\Big(\Pr(|X_n|>M)\Big)^{1-s/r}\le C^{s/r}\Big(\frac{C}{M^{r}}\Big)^{1-s/r}\xrightarrow[M\to\infty]{}0 ,$

且该收敛对 $n$ 一致。故 $\{|X_n|^s\}$ 一致可积。

**第二步：Skorokhod 表示（5 分）。** 由 $X_n\xrightarrow{d}X$，存在同一概率空间上的随机变量 $Y_n\overset{d}{=}X_n$、$Y\overset{d}{=}X$ 使得 $Y_n\to Y$ a.s.。于是 $|Y_n|^s\to|Y|^s$ a.s.，且 $\{|Y_n|^s\}$ 与 $\{|X_n|^s\}$ 同分布族，故也一致可积。

**第三步：Vitali 收敛定理（5 分）。** a.s. 收敛 ＋ 一致可积 ⇒ $L^1$ 收敛：

$\mathbb E|X_n|^s=\mathbb E|Y_n|^s\longrightarrow \mathbb E|Y|^s=\mathbb E|X|^s . \qquad \blacksquare$

（附带：由 Fatou，$\mathbb E|X|^r\le C$，故右端有限。最优性可举例：$X_n=\sqrt n\,\mathbf 1_{(0,1/n)}$ 有 $X_n\xrightarrow{d}0$、$\mathbb E X_n^2\equiv1$，故 $s=r=2$ 时结论不成立。）

**分档给分**
- **满分（18）**：给出**一致可积**的证明（Hölder ＋ Markov 的定量估计），经 Skorokhod 表示或截断逼近转到 a.s. 收敛，再用 Vitali/控制收敛。
- **部分分（9–17）**：只用截断 $\mathbb E|X_n|^s\le \mathbb E[|X_n|^s\wedge K]+\varepsilon$ 的路线但**没有**给出 $\varepsilon$ 关于 $n$ 一致的论证；或直接引用"$L^r$ 有界 ⇒ 一致可积"而不证。
- **零分**：只处理 $s$ 为整数；或用"由依分布收敛显然有矩收敛"这类错误依据。

### 概率 6（2026 概率 Q6，22 分）Bernstein / Darmois–Skitovich 定理

**答案：$\xi$ 与 $\eta$ 都服从（可能退化的）正态分布。**

**证明（只用特征函数与连续性，不假设任何矩条件）。**

**第一步：特征函数方程（5 分）。** 设 $\varphi_\xi,\varphi_\eta$ 为特征函数。由 $S=\xi+\eta$、$D=\xi-\eta$ **独立**：

$\mathbb E\big[e^{i(uS+vD)}\big]=\varphi_S(u)\varphi_D(v),$

而左端 $=\mathbb E\big[e^{i(u+v)\xi}e^{i(u-v)\eta}\big]=\varphi_\xi(u+v)\varphi_\eta(u-v)$。故

$\varphi_\xi(u+v)\varphi_\eta(u-v)=\varphi_\xi(u)\varphi_\eta(u)\,\varphi_\xi(v)\varphi_\eta(-v)\qquad \forall u,v\in\mathbb R. \tag{1}$

**第二步：局部取对数（4 分）。** 特征函数连续且 $\varphi(0)=1$，故存在 $\delta>0$ 使 $|\varphi_\xi|,|\varphi_\eta|,|\varphi_S|,|\varphi_D|>0$ 于 $(-\delta,\delta)$。于是可在 $(-\delta,\delta)$ 上取**连续对数分支**（在 $0$ 处取 $0$ 值）：

$A=\log\varphi_\xi,\quad B=\log\varphi_\eta,\quad C=\log(\varphi_\xi\varphi_\eta)=\log\varphi_S,\quad D_0=\log\big(\varphi_\xi(\cdot)\varphi_\eta(-\cdot)\big)=\log\varphi_D .$

（存在性：$(-\delta,\delta)$ 单连通且函数连续非零，故有连续对数。）对 (1) 取对数，并令 $s=u+v,\ t=u-v$，得

$A(s)+B(t)=C\Big(\frac{s+t}{2}\Big)+D_0\Big(\frac{s-t}{2}\Big),\qquad |s|,|t|<\delta' . \tag{2}$

**第三步：混合二阶差分 ⇒ 二次函数（9 分）。** 对 (2) 两端施加混合二阶差分算子 $\Delta_h^s\Delta_k^t$（$\Delta_h^s f(s,t)=f(s+h,t)-f(s,t)$）。左端因是 "$s$ 的函数 ＋ $t$ 的函数" 而**为零**：

$0=\Delta_h^s\Delta_k^t\Big[C\Big(\frac{s+t}{2}\Big)+D_0\Big(\frac{s-t}{2}\Big)\Big]=\Delta^2C\Big(p;\tfrac h2,\tfrac k2\Big)+\Delta^2D_0\Big(q;\tfrac h2,-\tfrac k2\Big),$

其中 $p=\frac{s+t}{2},\ q=\frac{s-t}{2}$，$\Delta^2f(x;\alpha,\beta):=f(x+\alpha+\beta)-f(x+\alpha)-f(x+\beta)+f(x)$。固定小 $h,k$，上式第一项只依赖 $p$、第二项只依赖 $q$，而 $(p,q)$ 取到原点附近的**整个邻域**，故二者都是常数：

$\Delta^2C(x;\alpha,\beta)\equiv c(\alpha,\beta)\quad\text{与 }x\text{ 无关}.$

同样地，把 $\Delta_h^u\Delta_k^v$ 施加于 (1) 取对数后的原始形式 $A(u+v)+B(u-v)=C(u)+D_0(v)$（右端对 $u,v$ 的混合差分为零），得到

$\Delta^2A(x;\alpha,\beta)\equiv a(\alpha,\beta),\qquad \Delta^2B(x;\alpha,\beta)\equiv b(\alpha,\beta).$

**引理（连续 ＋ 混合二阶差分为常数 ⇒ 二次多项式）**：若连续函数 $f$ 在 $(-\eta,\eta)$ 上满足 $\Delta_h\Delta_kf(x)=c(h,k)$（与 $x$ 无关）对所有小 $h,k$，则 $f(x)=f(0)+cx+\frac{\gamma}{2}x^2$。
*证明*：记 $\phi_h(x)=\Delta_hf(x)=f(x+h)-f(x)$，则对一切小 $k$ 有 $\phi_h(x+k)-\phi_h(x)=c(h,k)$；取 $x=0$ 得 $\phi_h(k)-\phi_h(0)=c(h,k)$，两式相减得 $\phi_h(x+k)-\phi_h(k)=\phi_h(x)-\phi_h(0)$，即 $\psi_h(x):=\phi_h(x)-\phi_h(0)$ 满足 Cauchy 方程，又 $\psi_h$ 连续，故 $\psi_h(x)=\beta(h)x$，即

$f(x+h)-f(x)=\phi_h(0)+\beta(h)x .$

对 $h+k$ 用同一式、并与"先 $h$ 后 $k$"相加比较系数，得 $\beta(h+k)=\beta(h)+\beta(k)$（Cauchy，连续故 $\beta(h)=\gamma h$）与 $\phi_{h+k}(0)=\phi_h(0)+\phi_k(0)+\gamma hk$；而 $\phi_t(0)=f(t)-f(0)$，故 $f(h+k)-f(0)=\big(f(h)-f(0)\big)+\big(f(k)-f(0)\big)+\gamma hk$。令 $g(x)=f(x)-f(0)-\frac{\gamma}{2}x^2$，则 $g(h+k)=g(h)+g(k)$，$g$ 连续，故 $g(x)=cx$。∎

由引理，在 $|x|<\eta$ 上

$\varphi_\xi(x)=e^{A(x)}=\exp\Big(a_0+a_1x+\tfrac{a_2}{2}x^2\Big),\qquad \varphi_\eta(x)=\exp\Big(b_0+b_1x+\tfrac{b_2}{2}x^2\Big).$

由 $\varphi(0)=1$ 得 $a_0=b_0=0$；由 $|\varphi_\xi(x)|\le1$ 得 $\operatorname{Re}a_2\le0$，且 $a_2$ 必为实数（否则 $|\varphi_\xi|$ 在 $x$ 的某方向上指数增长），故 $a_2=-\sigma_1^2\le0$，$a_1=i\mu_1$（$\mu_1\in\mathbb R$）；同理 $b_2=-\sigma_2^2\le0$，$b_1=i\mu_2$。

**第四步：局部等于正态特征函数 ⇒ 全局（4 分）。** 特征函数有"局部唯一性"：**两个特征函数若在 $0$ 的某邻域内相等，则处处相等**（对 $\varphi$ 与高斯特征函数作卷积、或用反演公式即可）。而

$g_1(x)=e^{i\mu_1x-\sigma_1^2x^2/2},\qquad g_2(x)=e^{i\mu_2x-\sigma_2^2x^2/2}$

分别是 $N(\mu_1,\sigma_1^2)$、$N(\mu_2,\sigma_2^2)$ 的特征函数，且在 $|x|<\eta$ 上与 $\varphi_\xi,\varphi_\eta$ 一致。故 $\varphi_\xi\equiv g_1$、$\varphi_\eta\equiv g_2$，即 $\xi\sim N(\mu_1,\sigma_1^2)$、$\eta\sim N(\mu_2,\sigma_2^2)$（$\sigma_i^2$ 可取 $0$，即退化正态）。∎

**分档给分**
- **满分（22）**：写出方程 (1)；说明"$\varphi$ 在 $0$ 附近非零 ⇒ 可取连续对数"；用**混合二阶差分**（而不是对特征函数求导——无矩条件下不可导）证明局部为二次指数；说明由"局部相等 ⇒ 处处相等"收尾。
- **部分分（12–21）**：方程 (1) 与"取对数"都写对，但随后**直接对 $u,v$ 求二阶偏导**（默认 $\varphi$ 二阶可导，即默认 $\mathbb E\xi^2<\infty$——题面无此假设，属实质缺口）；或只证出 $\varphi_\xi$ 局部等于某个二次指数函数却**没有**说明它可延拓为全局特征函数。
- **零分**：用"$S,D$ 独立且正态 ⇒ $\xi,\eta$ 正态"这类反向推理；或结论写成"$\xi,\eta$ 是正态且同方差"（同方差不是本题结论）；或只证 $\xi+\eta$ 正态。

---

## §3 逐题考点标注

难度为 1–5（与 `reports\yau_2024_2026_deep_analysis.md` 同一套自评标准）。"报告难度"列引用该报告对 2024–2026 原题的既有评级（2017/2020/2021 的题不在该报告范围内，标"—"）。

### 几何与拓扑卷

| 卷面号 | 出处（年份/卷别/题号） | 考点 | 难度 | 报告难度 | 骨架考点（subject_geometry.md 口径） | 与原题的关系 |
|---|---|---|---|---|---|---|
| 1 | 2026 / 个人卷 / Q5 | 覆叠空间与覆叠变换；万有覆叠；$K(\pi,1)$；群同调 $H_*(Z_k;\mathbb Z_2)$；流形的同调维数 | 3 | 3 | 覆叠空间与群作用（核心，8 年/13 题次）；基本群（骨架） | **原题原样**（两问全取）；仅把抽取中丢失的 $\tilde M$ 记号还原为 $\widetilde{M}$ |
| 2 | 2024 / 个人卷 / Q4 | Ricci 张量的迹；单位球面上二次型的平均；$O(n)$ 不变性 | 2 | **2** | Ricci 曲率/Einstein（核心，9 年/9 题次） | **原题原样**；原题定义 $S_p:=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)$ 保留（与通常约定相差因子 $n$） |
| 3 | 2024 / 个人卷 / Q2 | 极小曲面；$\Delta x=2H\vec n$；紧流形上调和函数必为常数；最大值原理 | 2 | 3 | 极小曲面/极小超曲面（骨架，6 年/7 题次） | **原题原样**；报告给 3 分，本人按"想到 $\Delta x=2Hn$ 即两行收尾"降到 2 分（`solutions_geometry.md` 亦以"25 分钟内能否写出完整证明"为标尺） |
| 4 | 2024 / 个人卷 / Q3 | 单连通 ⇒ 可定向；Poincaré 对偶；Betti 数配对；中间维杯积交错的奇偶性；Euler 示性数 | 3 | **4** | 同调群计算（核心，11 年/15）；Poincaré 对偶/de Rham（核心，8 年/10）；Euler 示性数与配边（骨架，7 年/7） | **原题原样**；抽取值 $H_2(M)=Z_2$ 的上下标有损，本卷在 §2 给出**两种读法**下都成立的证明 |
| 5 | 2026 / 个人卷 / Q1 | Gauss 映射；$dN=-S$ 与 $\det dN_p=K(p)$；面积公式（按重数计）；连续函数在收缩区域上的平均 | 3 | 3 | 经典曲线曲面论（Gauss 映射/基本形式，骨架，6 年/9）；Gauss 曲率的几何意义 | **原题原样** |
| 6 | 2026 / 个人卷 / Q3 | 双不变度规的 Levi-Civita 联络 $\nabla_XY=\frac12[X,Y]$；$K=\frac14\|[X,Y]\|^2$；Killing 型负定 ⇒ 紧型；$[\mathfrak g,\mathfrak g]^\perp=z(\mathfrak g)$；单连通群的中心分解 | 4 | **4** | 截面曲率与比较（核心，7 年/9）；曲率张量计算（核心，8 年/9）；Lie 群/双不变度量（核心，7 年/8） | **原题原样**（三问全取） |

### 概率与统计卷

| 卷面号 | 出处（年份/卷别/题号） | 考点 | 难度 | 报告难度 | 骨架考点（subject_probability.md 口径） | 与原题的关系 |
|---|---|---|---|---|---|---|
| 1 | 2026 / 个人卷 / Q2 | 分块回归；零化（投影）矩阵 $M_1$ 的对称幂等性；正规方程；FWL 定理；参数可识别性 | 2 | **2** | 高维统计/统计学习/回归（骨架，5 年/7 题次，2022–2026 密集） | **原题原样** |
| 2 | 2026 / 个人卷 / Q3 | 偏正态分布；密度的归一化；$\Phi(t)+\Phi(-t)=1$ 与对称性；联合正态的条件期望 | 2 | **2** | 分布论/特征函数/变量替换（骨架，13 年/29 题次，全科目第一） | **原题原样** |
| 3 | 2020 / 个人卷 / Q3 | 随机游走；命中概率；调和函数 ＋ 可选停止；强大数律与常返性 | 3 | — | 随机游走/Markov 链/随机过程（骨架，9 年/18）；极限定理（骨架，13 年/26） | **原题原样**；"对一切 $p\in[0,1]$"这一全参数要求完整保留，是本卷三段讨论的来源 |
| 4 | 2017 / **团体卷** / Q5 | 估计理论；MLE 及其不变性；Delta 方法；渐近相对效率；Poisson 族 | 3 | — | 估计理论（骨架，13 年/23，第三高）；渐近统计（骨架，9 年/16） | **原题原样**；原题在团体卷（现代赛制已取消团体卷），本卷按"个人卷 6 题"重新安置 |
| 5 | 2021 / 个人卷 / Q1 | 依分布收敛；$L^r$ 一致有界 ⇒ $L^s$ 一致可积（Hölder ＋ Markov）；Skorokhod 表示；Vitali 定理；收敛模式的封闭性 | 3 | — | 极限定理与收敛模式（骨架，13 年/26，第二高） | **原题原样**；本卷在答案中额外给出 $s=r$ 失效的反例（原题未要求，属**加分说明**，不计入满分要求） |
| 6 | 2026 / 个人卷 / Q6 | 独立性与特征函数方程；连续对数分支；混合二阶差分 ⇒ 局部二次指数；特征函数的局部唯一性；正态的刻画（Bernstein/Darmois–Skitovich） | 4 | **4** | 分布论/特征函数（骨架，13 年/29）；正态刻画（报告 §3.2 套路 19/20 同族） | **原题原样**；原题仅一句陈述，本卷第 6 题末尾加了一句**关于"无矩条件"的提示**，属考场提示，不改变题设 |

**难度配比核对**：几何 2 易（第 2、3 题）＋ 3 中（第 1、4、5 题）＋ 1 难（第 6 题）；概率 2 易（第 1、2 题）＋ 3 中（第 3、4、5 题）＋ 1 难（第 6 题）。✅ 符合"2 易 / 3 中 / 1 难"。

---

## §4 本卷失分预警

> 每条按"踩坑点 → 为什么会踩 → 现场怎么避免"写。

### 几何

**W1（几何第 1 题，(2) 问）用错 Lefschetz。** 最诱人的写法是"$g$ 有限阶 ⇒ $g$ 在 $\tilde M$ 上无不动点 ⇒ 用 Lefschetz 不动点定理，$L(g)=1\ne0$ ⇒ 有不动点 ⇒ 矛盾"。但 $\tilde M$ **非紧**，Lefschetz 定理的通常形式不适用，而这正是第 (1) 问存在的理由。**避免**：第 (1) 问不是装饰，它是"给第 (2) 问换工具"的信号——改用"$N=\tilde M/\langle g\rangle$ 是 $B\mathbb Z_k$，故各阶 $\mathbb Z_2$ 同调非零，与 $n$ 维流形的高维同调消失矛盾"。

**W2（几何第 2 题）用错标量曲率的约定。** 题面**自己定义** $S_p=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)$；若按通常约定 $S=\operatorname{Tr}(\mathrm{Ric})$ 计算，答案会差因子 $n$，整题归零。**避免**：先把题面定义抄在答题纸最上面。

**W3（几何第 3 题）忘掉"闭 = 紧"。** 写出 $\Delta x=0$ 后说"调和函数有界"就停笔，是本题最常见的半途失分——调和函数有界**不等于**常数（非紧情形的反例：$\mathbb R^n$ 上的坐标函数）。必须用 $\Sigma$ **紧**（最大值原理给出"常数"）或对 $\Delta|x|^2=4$ 用 Stokes。

**W4（几何第 4 题）漏掉"$b_3$ 为偶数"。** 只写"$\chi=2-b_3$，故 $\chi\ne-1$"是错的（$b_3=3$ 就给出 $-1$）。真正的锁是 6 维流形中间维 $H^3$ 上杯积的**交错性**（$3\times3=9$ 奇），从而 $b_3$ 偶。**避免**：凡是"证明某个数不等于某个指定的数"，都要追问"我把这个数算到了什么精度"。

**W5（几何第 5 题）把 Gauss 映射当单射。** 只有当 $K(p)\ne0$ 时 $N$ 才在 $p$ 附近是局部微分同胚；$K(p)=0$ 时 $N$ 可能把 $A_\varepsilon$ 压扁甚至折叠，此时 $\operatorname{Area}(N(A_\varepsilon))$ 与 $\int_{A_\varepsilon}|K|$ 不再相等（前者更小）。**避免**：分两种情形；$K(p)=0$ 时用 $0\le\frac{\operatorname{Area}(N(A_\varepsilon))}{|A_\varepsilon|}\le\sup_{A_\varepsilon}|K|\to0$ 夹逼。

**W6（几何第 6 题）三个高频错点。** ① 曲率公式的 $\frac14$ 因子（$\nabla_XY=\frac12[X,Y]$ 带出 $\frac14$，写成 $\frac12$ 或漏平方都错）；② 第 (2) 问只证"万有覆叠紧"就收尾——必须回到 $G$ 本身（$\pi_1(G)$ 离散 ⇒ $G$ 是紧群的商）；③ 第 (3) 问跳过 $[\mathfrak g,\mathfrak g]^\perp=z(\mathfrak g)$——这一步用 $\mathrm{ad}$-不变性一步可得，但**不写就等于没有**，因为 $Z\times G'\to G$ 是覆叠的论证全靠它。

### 概率

**W7（概率第 1 题）漏掉列满秩的验证。** 从 $X_2^{\top}M_1X_2\hat\beta_2=X_2^{\top}M_1Y$ 直接"除"，必须说明 $M_1X_2$ 列满秩。**避免**：用"$M_1X_2v=0\Rightarrow X_2v\in\operatorname{col}(X_1)$ ⇒ 与 $[X_1\ X_2]$ 列满秩矛盾"两行补上。另一个错法是把结论推广成"$\hat\beta_1$ 也相同"（一般不成立）。

**W8（概率第 2 题）归一化只做一半。** 只写"$f\ge0$"不证 $\int f=1$；或证 $\int f=1$ 时误用"$\Phi$ 关于 0 对称"（$\Phi$ 既非奇函数也非偶函数，真正的对称性是 $\Phi(t)+\Phi(-t)=1$ 加上 $X\overset d=-X$）。$E[Y]$ 的因子 2 也极易丢。

**W9（概率第 3 题）情形分不全。** 只答 $\big(\frac{1-p}{p}\big)^a$ 是最典型的失分（题面明写 "for all $p\in[0,1]$"）。$p\le1/2$ 时要分别处理负漂移（$S_n\to-\infty$，必命中）与对称（常返）。另有把比值写反成 $(p/(1-p))^a$ 的分数级错误——用一个极限校验：$p\to1$ 时应趋于 $0$。

**W10（概率第 4 题）ARE 方向与 Delta 方法。** ① 漏掉 $\operatorname{Var}(\bar X_n)=\lambda/n$ 里的 $\lambda$；② Delta 方法漏掉 $g'(\lambda)^2$ 的平方；③ ARE 定义方向写反（应为 $\tilde p$ 相对 $\hat p$，值 $\lambda/(e^\lambda-1)\le1$）。**校验**：效率不可能大于 1。

**W11（概率第 5 题）一致可积没证。** "依分布收敛 ＋ $L^r$ 有界 ⇒ $L^s$ 收敛"的全部内容就是一致可积，必须**量化**（Hölder ＋ Markov 给出的界关于 $n$ 一致）。只写"由控制收敛定理"而没有控制函数，直接扣掉大半分。还要注意 $s<r$ 的严格性：$X_n=\sqrt n\,\mathbf 1_{(0,1/n)}$ 说明 $s=r$ 失效。

**W12（概率第 6 题）对特征函数求导。** 题面**没有**任何矩条件，因此 $\varphi$ 未必二阶可导，"对 $u,v$ 求偏导得 $\log\varphi$ 是二次函数"是**隐藏假设**（等价于假设 $\mathbb E\xi^2<\infty$）。正确路线是**混合二阶差分**（把"二阶混合偏导"离散化）——它只需要连续性。另一个常见漏项：没有说明对数分支的存在（需要 $\varphi$ 在 0 附近非零，由连续性保证），以及没有说明"局部等于高斯特征函数 ⇒ 全局"这一步。

---

## §5 存疑

### 5.1 抽取有损但已回原文核对（本卷采用的题，均判定为"可用"）

| 题 | 抽取风险 | 核对结论 |
|---|---|---|
| 几何 4（2024 Q3） | $H_2(M)=Z_2$ 的上下标丢失：可能是 $H_2(M)\cong\mathbb Z_2$（循环群），也可能是 $\mathbb Z^2$ | 已回读 `.tmp\burn2026\txt\2024_2024_GeometryTopology.txt` 第 13–14 行确认原文如此（纯文本层面无上下标可辨）。**两种读法下 $\chi(M)$ 都是偶数，故结论 $\chi\ne-1$ 不受影响**；§2 已给出两套计算 |
| 几何 2（2024 Q4） | 原文 "…Ricci curvature tensor at $p$, $p$ be the scalar curvature at $p$…" 有字符错位，$S_p$ 与 $p$ 混用 | 已回读原文第 15–25 行：$S_p:=\frac1n\operatorname{Tr}_g(\mathrm{Ric}_p)$ 的定义完整，题面按此执行 |
| 概率 6（2026 Q6） | 仅一句陈述，无小问、无提示 | 已回读 `2026_2026_statistics.txt` 第 63–64 行确认原文即一句话；本卷第 6 题末尾加的"无矩条件提示"是**本卷新增的考场提示**，已在 §3 注明 |
| 概率 4（2017 团体 Q5） | 2017 年**个人卷与团体卷各有一道 Q5**（个人卷 Q5 是传染病 PDE 题） | 已回读 `2017_2017_team.txt` 第 95–104 行确认取的是**团体卷第 5 题**（Poisson 估计） |

### 5.2 因"给不出可靠答案"而被换掉的题（**宁可不选，也不给错答案**）

| 被换掉的题 | 换入 | 换掉的原因（如实记录） |
|---|---|---|
| **2024 概率 Q2**（$M=\sup_n S_n/n$：求 $P(M=0)$；证 $P(p-q<M\le1)=1$；问有理 $x$ 是否 $P(M=x)>0$） | 概率 3（2020 Q3） | 我尝试的候选公式 $P(M\le x)=\exp\big(-\sum_{n\ge1}\frac1nP(S_n>nx)\big)$ **被自身反例否定**：该公式在 $x\uparrow1$ 时给出 $P(M<1)=1$，但 $M\ge S_1/1=X_1$ 故 $P(M=1)\ge P(X_1=1)=p>0$。既然我连一个可用的分布公式都无法确认，就无法给出 (a)(b) 的可靠答案，故弃用。（`reports\yau_2024_2026_deep_analysis.md` 把该题标为难度 5，工具列为"Chung–Feller、上穿概率"；在 2023 年起官方解答停止公开的情况下无从核对。） |
| **2024 概率 Q1**（$r$ 人赌局，$E[X(S)]$ 是否依赖选人机制） | 概率 1、2（均取自 2026） | 我用 $r=3,\ n_i\equiv1$ 构造了两个合法机制，得到 $E[X(\{1,2\})]=1$ 与 $1/2$，**与** `reports\yau_2024_2026_deep_analysis.md` 表中"机制无关性"的结论相反。这是"报告结论 vs 我的反例"的实质冲突：在无法看到官方解答的前提下，我无法判定是我误解了 $X(S)$ 的定义（"只涉及 $S$ 中成员的局数"是否指"双方都在 $S$ 内"）还是报告有误，故弃用。**建议后续用原始 PDF（`F:\丘成桐大学生数学竞赛历年笔试真题`）核对本题定义再决定是否回收。** |
| **2026 概率 Q5**（稳定分布：$\alpha=1,b=0$ 时 $\varphi(t)=e^{i\mu t-\gamma\|t\|}$；且 $\mathbb E\|X_1\|<\infty$ 时 $\alpha\le1$ 不可能） | 概率 6（同卷 Q6） | (a) 可用特征函数方程做，但 (b) 是一般稳定律/Lévy 理论的定理，我无法在"关键步骤 ＋ 最终答案"的粒度内给出**自足且可靠**的证明；两问属同一题不可拆用，故整题弃用。 |
| **2025 概率 Q3**（构造 $X_1,\dots,X_n=X_0$ 使 $P(X_{k-1}<X_k)=1-\frac{1}{4\cos^2(\pi/(n+2))}$） | 概率 4（2017 团体 Q5） | 我无法可靠重构出这个三角常数的来源与匹配的构造（该常数与循环递推/特征多项式的谱有关），不敢给出构造。 |
| **2025 概率 Q1**（单观测 $X\sim N(\mu,\sigma^2)$ 的置信区间覆盖概率与 minimax 随机化区间） | 概率 5（2021 Q1） | 该题第 2 问的抽取已被上游标为**语义不完整**（`reports\yau_2024_2026_deep_analysis.md` 存疑表 U10：缺 "Prove that …" 连接词，两个公式直接并列）。题面有损，不宜入卷。 |
| **2026 几何 Q6**（$\mathrm{Ric}\ge\epsilon(n-1)r^{-2}$，$\epsilon>1/4$ ⇒ 紧；$\epsilon\le1/4$ 时举例说明失效） | 未替换（本卷 6 题已满） | (2) 要求给出反例，我无法可靠写出 $\epsilon\le1/4$ 时满足该曲率下界的非紧完备度量；且该题难度自评 5，与本卷"2 易/3 中/1 难"的配比不符。 |
| **2025 几何 Q1**（$S^{2n}\times S^{2n}$ 与 $S^{2n}\times S^{2n-1}$ 的切丛是否平凡） | 未替换 | (i) 否（$\chi=4\ne0$）；(ii) 我认为答案是"是"，但我的证明依赖"$T(S^{2n}\times S^{2n-1})\oplus\varepsilon^1$ 平凡 ＋ 稳定同伦意义下的消去定理（stable range：$\mathrm{rank}\ge\dim$）"，在卷面答案里无法自足给出。**结论方向我有把握，证明链条我没有把握**，故不入卷。 |
| **2026 几何 Q4**（$S^{2026}$ 的 $\mathbb Z_2$ Euler 类；单位切球丛的 Poincaré 级数；非对径点路径空间能量泛函的临界点/Morse 指标/环路空间同伦型/两类环路空间的 Poincaré 级数） | 未替换 | 抽取文本中页码 "2" 与题内编号 "(2)" 混排（`2026_2026_Geo_Topology.txt`）；且这是"4 小问巨型题"，单题篇幅超过本卷其余题的 3–4 倍，塞进 6 题卷会破坏配比。 |
| **2022 概率 Q5**（rank 可能亏的线性模型中 $\gamma=\mathbf x_1\beta/\sigma$ 的 UMVUE） | 未替换 | 我能给出 UMVUE 的候选形式（$\hat\gamma=\mathbf x_1\hat\beta/(c\,s)$，$c=\sqrt{\frac{n-k}{2}}\Gamma(\frac{n-k-1}{2})/\Gamma(\frac{n-k}{2})$，$s=\sqrt{RSS/(n-k)}$），但题面"**or prove it does not exist**"的双择提示让我怀疑在 $\mathrm{rank}(X)=k<p$ 的不可识别模型里，最小充分统计量的**完备性**论证有我没看到的缺口；报告篇幅内给不出无懈可击的版本，故弃用。 |
| **2023 概率 Q5**（四位统计学家停时规则下 $T=(X_1+X_2,X_3+X_4)$ 的完备性；$\theta$ 的 UMVUE） | 未替换 | $T$ 关于 $\theta$ 是否完备我无法可靠判定（$T$ 不是充分统计量，完备性要看 $T$ 自身的分布族），且 (b) 的 UMVUE 依赖 (a) 的结论，一错全错，故弃用。 |

### 5.3 备选题（可靠、但受"6 题 ＋ 2 易/3 中/1 难"约束未入选）

这些题我已核实答案，供换卷或加练使用；**不建议**把它们塞进本卷而不调整配比。

| 备选题 | 考点 | 难度 | 可靠答案（要点） | 未入选原因 |
|---|---|---|---|---|
| 2025 几何 Q6 | Lefschetz 不动点；$\mathrm{CP}^n$ 与 $\mathrm{CP}^2\times\mathrm{CP}^2$ 的上同调环 | 4 | (i) $\mathrm{CP}^n$ 上**存在**无不动点自同胚 $\iff n$ 为奇数（无不动点需 $L(f)=\sum_{i=0}^n a^i=0$，即 $a=-1$ 且 $n+1$ 偶；$n$ 奇时由 $[z_0:\cdots:z_n]\mapsto[-\bar z_1:\bar z_0:\cdots]$ 给出）。(ii) $\mathrm{CP}^2\times\mathrm{CP}^2$ 上**不存在**（设 $f^*|_{H^2}=A\in GL(2,\mathbb Z)$，由五次上同调群的迹可得 $L=1+s+(s^2-p)+s(3p-2ad)+p^2$，其中 $s=a+d,\ p=\det A=\pm1$；两种情形均证 $L\ne0$） | 会占掉"难"档，与几何第 6 题冲突；且它覆盖的是"复射影空间（6 年）＋ Lefschetz（2 年）"，骨架权重低于已选的"同调（11 年）＋ Poincaré 对偶（8 年）＋ Euler 示性数（7 年）" |
| 2026 几何 Q2 | Gauss–Bonnet；测地曲率；等距刚性 | 4 | 由 Gauss–Bonnet，$2\pi\chi(M)=\int_MK+\int_{\partial M}k_g\ge L\ge2\pi$ ⇒ $\chi(M)\ge1$ ⇒ $M$ 是圆盘；取等号 ⇒ $K\equiv0$、$k_g\equiv1$、$L=2\pi$ ⇒ 展开映射给出 $M$ 等距于单位圆盘 | 同上（难档冲突）；且等距刚性最后一步需要展开映射（developing map）的严格论证，超出本报告给"关键步骤"的粒度 |
| 2024 概率 Q5 | 次序统计量；极值分布；中位数无偏；分布收敛 | 4 | (a) 条件为 $(1-2^{-r_n})^{c_n}=1/2$（$c_n=n/r_n$），等价于 $c_n\log(1-2^{-r_n})=-\log2$，forcing $r_n\sim\log_2 n$；(b) $r_n(\hat\beta_n-\beta)\xrightarrow{d}$ 的分布函数为 $1-\exp\big(-(\log2)e^{2f(\beta)t}\big)$（Gumbel 型） | 难档已被概率第 6 题占据；且它替换掉任一"中"档题都会损失一个骨架考点（现有 6 题已覆盖题次前 5 中的 4 个） |
| 2026 概率 Q4 | 布朗运动；首次退出时；鞅/可选停止；Feynman–Kac | 3 | $\mathbb E[\tau_a^2]=\frac53a^4$（由 $\frac12u''=-1,\ u(\pm a)=0\Rightarrow u=a^2-x^2$，再由 $\frac12v''=-2u\Rightarrow v(x)=-2a^2x^2+\frac13x^4+\frac53a^4$ 得 $v(0)=\frac53a^4$） | 布朗运动/随机分析是**孤例考点**（`subject_probability.md` §2.3 第 22 项，仅 2026 一年），骨架权重最低；若想把"随机分析"纳入，可直接替换概率第 3 题 |
| 2022 概率 Q3 | 经典随机模型；停时；期望 | 2 | $\mathbb E\tau_{11}=42$，$\mathbb E\tau_{12}=36$（$p=1/6$，前者用 $\mathbb E\tau=(1+p)/p^2$ 型状态方程） | 难度仅 2，加入会使"2 易"超编；若要覆盖"经典随机模型（9 年/14 题次）"，可替换概率第 2 题 |
| 2021 概率 Q3 | 强大数律；Borel–Cantelli；0–1 律 | 3 | $\alpha>1/2$ 时 $P(\lim_n S_n/n^\alpha=0)=1$（$\sum_n P(|S_n|>n^\alpha\varepsilon)<\infty$，Borel–Cantelli） | 与概率第 5 题同属"极限定理"骨架，重复度高 |
| 2019 概率（个人卷）Q1 | Borel–Cantelli 双侧；$\limsup X_n^{1/n}$ | 3 | $\limsup_n X_n^{1/n}=1$ a.s.：上界由 Markov ＋ Borel–Cantelli（$P(X_n>(1+\varepsilon)^n)\le C(1+\varepsilon)^{-n}$ 可和）；下界由 $\mathbb E[(-\log X_n)^+]\le C$ 给出"若 $\limsup<1-\delta$ 则最终 $X_n\le(1-\delta/2)^n$ a.s.，与期望有界矛盾" | 同上（与概率第 5 题骨架重复） |

### 5.4 与上游报告的冲突（必须留痕）

1. **题量口径**：见开头的口径声明（当前 757 题里几何 156、概率 133，与 `reports\subject_geometry.md` 的 159/160 不一致）。
2. **2024 概率 Q1 的结论**：`reports\yau_2024_2026_deep_analysis.md` 表中把该题方法列为"机制无关性"，我的 $r=3$ 反例指向"机制相**关**"。**本报告不采用该题的结论，两说并存待核。**
3. **2024 概率 Q2 的难度**：该报告标 5，我不反对；但请注意我无法给出该题答案（§5.2），因此本卷的"概率难度均值 2.83"是**在剔除该题后**的结果。

---

**报告结束。** 全部 12 题的题面均可回溯到 `.tmp\burn2026\data\problems_full.json` 的具体记录（year / paper / n 见 §3），并已回读 `.tmp\burn2026\txt\` 下的原始抽取文本核对。