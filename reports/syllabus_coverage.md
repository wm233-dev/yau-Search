# 丘成桐大学生数学竞赛 · 考纲覆盖率分析报告

**对象**：Yau Contest 官方 Syllabus（6 份）× 历年笔试真题 **758** 道（个人赛 individual + 团体赛 team，含完整题面）。

**数据**：`data/problems_full.json`（题面）、`data/syllabus_coverage.json`（逐条命中明细）。
**脚本**：`scripts/syllabus_coverage.py` + `scripts/make_syllabus_reports.py`（可复跑）。**生成时间**：2026-09-18T12:39:32

## 0. 关键结论（先看这 8 条）

1. 考纲共拆出 **319** 条：高频命中（≥8 题）**31** 条、偶发命中（1–7 题）**135** 条、**零命中 153 条（占 48.0%）**。
2. 考纲**不是命题清单**：近五成条目（48.0%）从未在笔试中以该术语出现过，它更像「研究生资格考范围」而非「竞赛出题范围」。
3. 命中高度集中：各科目 Top 条目吃掉大半考卷——代数「因子分解与素数」44 题、几何「曲率的定义」46 题、概率「随机变量」60 题。
4. **分析卷是最「虚」的科目**：63 条里 39 条零命中（61.9%），实分析测度论与泛函分析几乎整块不考。
5. **数理物理是最「窄」的科目**：78 条里 42 条零命中（53.8%），但命中的 36 条全部落在近五年，属「窄而深」。
6. 反向发现：真题大量考查**考纲完全没写**的内容——线性代数与矩阵论（代数卷 37 题）、点集拓扑（几何卷 52 题）、数值线性代数（应用卷 32 题）。
7. 考纲标题含 **Combinatorics（组合数学），正文却没有任何组合条目**，真题中组合类题面也仅 4 道——名实不符。
8. 趋势结构：**上升** 35 条、**平稳** 23 条、**下降/已消失** 56 条。上涨最明显的是应用与计算（数值稳定性）与概率统计（多元分布、条件期望）。

## 1. 方法与口径

| 项 | 设定 |
|---|---|
| 检索对象 | 同科目真题题面全文（**不跨科目串味**：代数条目只在代数卷里搜） |
| 匹配方式 | 每条考纲条目配一组正则（以英文术语为主），题面命中任一即计 1 题 |
| 文本归一化 | 修正 PDF 抽取噪声：独立重音字符（Poincar´e 到 Poincare）、行尾连字符断词（prob- ability 到 probability）、统一撇号与破折号 |
| 近年窗口 | 2022–2026（数理物理 2022 年才设科） |
| 早期窗口 | 2010–2021 |
| 状态判据 | **高频命中** ≥8 题；**偶发命中** 1–7 题；**零命中** 0 题 |
| 趋势判据 | 近五年命中率 ÷ 早期命中率：≥1.5 上升；0.67–1.5 平稳；小于 0.67 下降；仅近五年出现 = 新兴；近五年为 0 = 已消失 |
| 优先级得分 | **科目内命中密度(%) × 趋势系数**（上升 1.4 / 新兴 1.5 / 平稳 1.0 / 下降 0.75 / 已消失 0.4）。用密度而非绝对题数，才能让 30 题的数理物理与 159 题的几何同尺度比较 |
| 等级 | **A** 得分 ≥12；**B** 4–12；**C** 大于 0 且小于 4；**D** 命中 0 题 |

> **重要口径提醒**：关键词命中是**下界**而非真值。真题常直接陈述结论而不点名定理——分析卷 157 道题里 `Cauchy`、`residue`、`Schwarz` **一次都没出现**，但复分析仍以「全纯/亚纯函数」形态考了 25 题。
> 因此「零命中」应读作「**从不以该术语/该形态出现**」，不等于该数学内容绝对不考。

## 2. 总览：六科考纲覆盖率

| 科目 | 考纲条目 | 高频命中(≥8) | 偶发命中(1–7) | **零命中** | 零命中占比 | 真题数 | 近五年真题 |
|---|---|---|---|---|---|---|---|
| Algebra & Number Theory | 46 | 6 | 21 | **19** | 41.3% | 150 | 28 |
| Analysis & PDE | 63 | 4 | 20 | **39** | 61.9% | 157 | 28 |
| Computational & Applied | 34 | 3 | 17 | **14** | 41.2% | 135 | 30 |
| Geometry & Topology | 53 | 6 | 23 | **24** | 45.3% | 159 | 30 |
| Probability & Statistics | 45 | 10 | 20 | **15** | 33.3% | 127 | 27 |
| Mathematical Physics | 78 | 2 | 34 | **42** | 53.8% | 30 | 30 |
| **合计** | **319** | **31** | **135** | **153** | **48.0%** | **758** | **173** |

按零命中占比排序（越靠前 = 考纲与该科实际考卷越脱节）：

| 排名 | 科目 | 零命中 / 条目 | 零命中占比 |
|---|---|---|---|
| 1 | Analysis & PDE | 39 / 63 | 61.9% |
| 2 | Mathematical Physics | 42 / 78 | 53.8% |
| 3 | Geometry & Topology | 24 / 53 | 45.3% |
| 4 | Algebra & Number Theory | 19 / 46 | 41.3% |
| 5 | Computational & Applied | 14 / 34 | 41.2% |
| 6 | Probability & Statistics | 15 / 45 | 33.3% |

## 3. 逐条覆盖率明细（按考纲顺序）

### 3.1 代数与数论（Algebra and Number Theory）

真题 150 道（近五年 28 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| ALG-G1 | Sylow 定理（Sylow theorems） | 5 | 0 | 5 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-G2 | p-群（p-groups） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-G3 | 可解群（solvable groups） | 4 | 1 | 3 | 平稳 | 偶发命中 | **C** |
| ALG-G4 | 自由群（free groups） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-R1 | 张量积（tensor products） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-R2 | 行列式（determinants） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-R3 | Jordan 标准形（Jordan canonical form） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-R4 | 主理想整环（PID） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-R5 | 唯一分解整环（UFD） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-R6 | 多项式环（polynomial rings） | 2 | 1 | 1 | 上升 | 偶发命中 | **C** |
| ALG-F1 | 分裂域（splitting fields） | 8 | 2 | 6 | 平稳 | 高频命中 | **B** |
| ALG-F2 | 可分与不可分扩张（separable and inseparable extensions） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| ALG-GA1 | Galois 理论基本定理（Fundamental theorems of Galois theory） | 18 | 4 | 14 | 平稳 | 高频命中 | **A** |
| ALG-GA2 | 有限域（finite fields） | 12 | 5 | 7 | 上升 | 高频命中 | **B** |
| ALG-GA3 | 分圆域（cyclotomic fields） | 4 | 1 | 3 | 平稳 | 偶发命中 | **C** |
| ALG-H1 | 正合列（exact sequences） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| ALG-H2 | 分裂（splittings） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-H3 | 蛇引理与五引理（snake and five lemmas） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-H4 | 投射、内射、平坦模（projective, injective, and flat modules） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-H5 | 复形与（上）同调（complexes, (co)homology） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-C1 | 局部化（localizations） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| ALG-C2 | Hilbert 基定理（Hilbert's basis theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-C3 | 整扩张（integral extensions） | 2 | 1 | 1 | 上升 | 偶发命中 | **C** |
| ALG-C4 | 理想的根（radicals of ideals） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| ALG-C5 | Zariski 拓扑与 Hilbert 零点定理（Zariski topology and Hilbert's Nullstellensatz） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-C6 | Dedekind 环（Dedekind rings） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-C7 | 离散赋值环（DVRs） | 2 | 2 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| ALG-REP1 | 特征标理论（character theory） | 2 | 1 | 1 | 上升 | 偶发命中 | **C** |
| ALG-REP2 | 诱导表示（induced representations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-REP3 | 群环的结构（structure of the group ring） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-LIE1 | 指数映射（exponential map） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| ALG-LIE2 | 幂零与半单 Lie 代数、Lie 群（nilpotent and semi-simple Lie algebras and Lie groups） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| NT-1 | 因子分解与素数（Factorization and the primes） | 44 | 12 | 32 | 上升 | 高频命中 | **A** |
| NT-2 | 同余（congruences） | 10 | 3 | 7 | 上升 | 高频命中 | **B** |
| NT-3 | 二次剩余与互反律（quadratic residues and reciprocity） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| NT-4 | 连分数与逼近（continued fractions and approximations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| NT-5 | eta 函数（eta functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| NT-6 | zeta 函数（zeta functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| NT-7 | 数域（Number fields） | 6 | 4 | 2 | 上升 | 偶发命中 | **B** |
| NT-8 | 理想的唯一分解（unique factorization of ideals） | 5 | 2 | 3 | 上升 | 偶发命中 | **B** |
| NT-9 | 类群的有限性（finiteness of class group） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| NT-10 | 单位群的结构（structure of unit group） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| NT-11 | Frobenius 元素（Frobenius elements） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| NT-12 | 局部域（local fields） | 13 | 5 | 8 | 上升 | 高频命中 | **A** |
| NT-13 | 分歧（ramification） | 5 | 3 | 2 | 上升 | 偶发命中 | **B** |
| NT-14 | 弱逼近（weak approximation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |

### 3.2 分析与偏微分方程（Analysis and Differential Equations）

真题 157 道（近五年 28 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| AN-R1 | 积分收敛定理（Convergence theorems for integrals） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R2 | Borel 测度（Borel measure） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R3 | Riesz 表示定理（Riesz representation theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R4 | Lp 空间（Lp space） | 6 | 0 | 6 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R5 | Lp 空间的对偶（Duality of Lp space） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R6 | Jensen 不等式（Jensen inequality） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R7 | Lebesgue 微分定理（Lebesgue differentiation theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R8 | Fubini 定理（Fubini theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R9 | Hilbert 空间（Hilbert space） | 8 | 0 | 8 | 已消失（近五年未考） | 高频命中 | **C** |
| AN-R10 | 有界变差复测度（Complex measures of bounded variation） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R11 | Radon-Nikodym 定理（Radon-Nikodym theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R12 | Hahn-Banach 定理（Hahn-Banach Theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R13 | 开映射定理（open mapping theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R14 | 一致有界性定理（uniform boundedness theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R15 | 闭图像定理（closed graph theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R16 | 紧算子的基本性质（Basic properties of compact operators） | 6 | 0 | 6 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R17 | Riesz-Fredholm 理论（Riesz-Fredholm Theory） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-R18 | 紧算子的谱（spectrum of compact operators） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R19 | Fourier 级数（Fourier series） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-R20 | Fourier 变换（Fourier transform） | 8 | 2 | 6 | 上升 | 高频命中 | **B** |
| AN-R21 | 卷积（convolution） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| AN-C1 | 全纯与亚纯函数（Holomorphic and meromorphic functions） | 25 | 2 | 23 | 下降 | 高频命中 | **B** |
| AN-C2 | 共形映射（Conformal maps） | 5 | 0 | 5 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-C3 | 分式线性变换（linear fractional transformations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C4 | Schwarz 引理（Schwarz's lemma） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C5 | Cauchy 定理（Cauchy's theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C6 | Cauchy 积分公式（Cauchy integral formula） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C7 | 留数（residues） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C8 | 调和函数：平均值性质（Harmonic functions: the mean value property） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C9 | 反射原理（the reflection principle） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C10 | Dirichlet 问题（Dirichlet's problem） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-C11 | Laurent 级数（Laurent series） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C12 | 部分分式展开（partial fractions expansions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C13 | 典型乘积（canonical products） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C14 | 特殊函数：Gamma 函数（the Gamma function） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C15 | 特殊函数：zeta 函数（the zeta functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C16 | 特殊函数：椭圆函数（elliptic functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C17 | Riemann 曲面基础（Basics of Riemann surfaces） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C18 | Riemann 映射定理（Riemann mapping theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-C19 | Picard 定理（Picard theorems） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D1 | ODE 解的存在唯一性定理（Existence and uniqueness theorems for solutions of ODE） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D2 | 简单方程的显式解（explicit solutions of simple equations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D3 | 有限区间上的自伴边值问题（self-adjoint boundary value problems on finite intervals） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| AN-D4 | 临界点、相空间、稳定性分析（critical points, phase space, stability analysis） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D5 | 一阶偏微分方程（First order partial differential equations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D6 | 线性与拟线性 PDE（linear and quasi-linear PDE） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D7 | 相平面分析（Phase plane analysis） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D8 | Burgers 方程（Burgers equation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D9 | Hamilton-Jacobi 方程（Hamilton-Jacobi equation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D10 | 位势方程：Green 函数（Potential equations: Green functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D11 | Dirichlet 问题解的存在性（existence of solutions of Dirichlet problem） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D12 | 调和函数（harmonic functions） | 11 | 2 | 9 | 平稳 | 高频命中 | **B** |
| AN-D13 | 极大值原理及应用（maximal principle and applications） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D14 | Neumann 问题解的存在性（existence of solutions of Neumann's problem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D15 | 热方程（Heat equation） | 3 | 2 | 1 | 上升 | 偶发命中 | **C** |
| AN-D16 | 基本解（fundamental solutions） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| AN-D17 | 波动方程：初值与边值条件（Wave equations: initial condition and boundary condition） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D18 | 适定性（well-posedness） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D19 | Sturm-Liouville 特征值问题（Sturm-Liouville eigenvalue problem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D20 | 能量泛函方法（energy functional method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| AN-D21 | 解的唯一性与稳定性（uniqueness and stability of solutions） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D22 | 分布（Distributions） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| AN-D23 | Sobolev 嵌入定理（Sobolev embedding theorem） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |

### 3.3 计算与应用数学（Computational and Applied Mathematics）

真题 135 道（近五年 30 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| CA-1 | 三角插值与逼近（Trigonometric interpolation and approximation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-2 | 快速 Fourier 变换（fast Fourier transform） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-3 | 有理函数逼近（approximations by rational functions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-4 | 多项式与样条插值与逼近（polynomial and spline interpolations and approximation） | 5 | 1 | 4 | 平稳 | 偶发命中 | **C** |
| CA-5 | 最小二乘逼近（least-squares approximation） | 5 | 0 | 5 | 已消失（近五年未考） | 偶发命中 | **C** |
| CA-6 | 二分法（bisection） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-7 | Newton 法（Newton's method） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| CA-8 | 拟 Newton 法（quasi-Newton's methods） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| CA-9 | 不动点方法（fixed-point methods） | 4 | 2 | 2 | 上升 | 偶发命中 | **B** |
| CA-10 | 多项式求根（finding roots of polynomials） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-11 | 线性系统与特征值问题的经典与现代迭代法（Classical and modern iterative method for linear systems and eigenvalue problems） | 3 | 0 | 3 | 已消失（近五年未考） | 偶发命中 | **C** |
| CA-12 | 条件数与奇异值分解（condition number and singular value decomposition） | 9 | 1 | 8 | 下降 | 高频命中 | **B** |
| CA-13 | 大型稀疏线性方程组迭代法（iterative methods for large sparse system of linear equations） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-14 | 单步法（Single step methods） | 5 | 3 | 2 | 上升 | 偶发命中 | **B** |
| CA-15 | 多步法（multi-step methods） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| CA-16 | 稳定性、精度与收敛性（stability, accuracy and convergence） | 20 | 8 | 12 | 上升 | 高频命中 | **A** |
| CA-17 | 绝对稳定性与长时间行为（absolute stability, long time behavior） | 3 | 2 | 1 | 上升 | 偶发命中 | **C** |
| CA-18 | 刚性 ODE 的数值方法（numerical methods for stiff ODE's） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| CA-19 | 有限差分方法（Finite difference method） | 8 | 4 | 4 | 上升 | 高频命中 | **B** |
| CA-20 | 有限元方法（finite element method） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| CA-21 | 谱方法（spectral method） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| CA-22 | Lax 等价定理（Lax equivalence theorem） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| CA-23 | 数学建模、模拟与应用分析（Mathematical modeling, simulation, and applied analysis） | 6 | 0 | 6 | 已消失（近五年未考） | 偶发命中 | **C** |
| CA-24 | 尺度行为与渐近分析（Scaling behavior and asymptotics analysis） | 4 | 2 | 2 | 上升 | 偶发命中 | **B** |
| CA-25 | 驻相分析（stationary phase analysis） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-26 | 边界层分析（boundary layer analysis） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-27 | 模型的定性与定量分析（qualitative and quantitative analysis of mathematical models） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-28 | Monte-Carlo 方法（Monte-Carlo method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-29 | 单纯形法（Simplex method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-30 | 内点法（interior method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-31 | 罚函数法（penalty method） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| CA-32 | Newton 法（优化）（Newton's method） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| CA-33 | 同伦方法与不动点方法（homotopy method and fixed point method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| CA-34 | 动态规划（dynamic programming） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |

### 3.4 几何与拓扑（Geometry and Topology）

真题 159 道（近五年 30 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| GT-M1 | 反函数定理（Inverse function theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-M2 | 隐函数定理（implicit function theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-M3 | 子流形（submanifolds） | 7 | 1 | 6 | 平稳 | 偶发命中 | **B** |
| GT-M4 | Sard 定理（Sard's Theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-M5 | 嵌入定理（embedding theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-M6 | 横截性（transversality） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-M7 | 度理论（degree theory） | 5 | 0 | 5 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-M8 | 流形上的积分（integration on manifolds） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-L1 | GL(n)、SU(n)、SO(n)、U(n) 的定义（The definitions of Gl(n), SU(n), SO(n), U(n)） | 6 | 3 | 3 | 上升 | 偶发命中 | **B** |
| GT-L2 | 矩阵 Lie 群的流形结构（their manifold structures） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| GT-L3 | Lie 代数（Lie algebras） | 3 | 3 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| GT-L4 | 左右不变向量场与微分形式（right and left invariant vector fields and differential forms） | 2 | 2 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| GT-L5 | 指数映射（the exponential map） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-V1 | 实与复向量丛的定义（Definition of real and complex vector bundles） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-V2 | 切丛与余切丛（tangent and cotangent bundles） | 6 | 2 | 4 | 上升 | 偶发命中 | **B** |
| GT-V3 | 丛上的基本运算（对偶、张量积、外积、直和、拉回）（dual bundle, tensor products, exterior products, direct sums, pull-back bundles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-V4 | 微分形式、外积、外微分（Definition of differential forms, exterior product, exterior derivative） | 3 | 0 | 3 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-V5 | de Rham 上同调（de Rham cohomology） | 3 | 0 | 3 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-V6 | 拉回下的行为（behavior under pull-back） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-V7 | 向量丛上的度量（Metrics on vector bundles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R1 | Riemann 度量（Riemannian metrics） | 32 | 10 | 22 | 上升 | 高频命中 | **A** |
| GT-R2 | 测地线的定义（definition of a geodesic） | 11 | 2 | 9 | 平稳 | 高频命中 | **B** |
| GT-R3 | 测地线的存在性与唯一性（existence and uniqueness of geodesics） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R4 | 矩阵群的主丛（Definition of a principal Lie group bundle for matrix groups） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R5 | 相伴向量丛（Associated vector bundles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R6 | 主丛与向量丛的关系（Relation between principal bundles and vector bundles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R7 | 协变导数与主丛上的联络（covariant derivative for a vector bundle and connection on a principal bundle） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| GT-R8 | 两者的关系（Relations between the two） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R9 | 曲率的定义（Definition of curvature） | 46 | 9 | 37 | 平稳 | 高频命中 | **A** |
| GT-R10 | 平坦联络（flat connections） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R11 | 平行移动（parallel transport） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R12 | Levi-Civita 联络（Definition of Levi-Civita connection） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| GT-R13 | Riemann 曲率张量的性质（properties of the Riemann curvature tensor） | 25 | 5 | 20 | 平稳 | 高频命中 | **A** |
| GT-R14 | 常曲率流形（manifolds of constant curvature） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-R15 | Jacobi 场（Jacobi fields） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-R16 | 测地线的第二变分（second variation of geodesics） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-R17 | 非正曲率流形（Manifolds of nonpositive curvature） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-R18 | 正曲率流形（manifolds of positive curvature） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-A1 | 基本群（Fundamental groups） | 12 | 3 | 9 | 平稳 | 高频命中 | **B** |
| GT-A2 | 覆叠空间（Covering spaces） | 7 | 2 | 5 | 上升 | 偶发命中 | **B** |
| GT-A3 | 高阶同伦群（Higher homotopy groups） | 2 | 1 | 1 | 上升 | 偶发命中 | **C** |
| GT-A4 | 纤维化与纤维化的长正合列（Fibrations and the long exact sequence of a fibration） | 2 | 1 | 1 | 上升 | 偶发命中 | **C** |
| GT-A5 | 奇异同调与上同调（Singular homology and cohomology） | 15 | 1 | 14 | 下降 | 高频命中 | **B** |
| GT-A6 | 相对同调（Relative homology） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A7 | CW 复形与 CW 复形的同调（CW complexes and the homology of CW complexes） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A8 | Mayer-Vietoris 序列（Mayer-Vietoris sequence） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A9 | 万有系数定理（Universal coefficient theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A10 | Kunneth 公式（Kunneth formula） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A11 | Poincare 对偶（Poincare duality） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| GT-A12 | Lefschetz 不动点公式（Lefschetz fixed point formula） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A13 | Hopf 指标定理（Hopf index theorem） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| GT-A14 | Cech 上同调与 de Rham 上同调（Cech cohomology and de Rham cohomology） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| GT-A15 | 奇异、Cech 与 de Rham 上同调的等价性（Equivalence between singular, Cech and de Rham cohomology） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |

### 3.5 概率与统计（Probability and Statistics）

真题 127 道（近五年 27 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| PS-P1 | 随机变量（Random variable） | 60 | 15 | 45 | 平稳 | 高频命中 | **A** |
| PS-P2 | 期望（Expectation） | 18 | 4 | 14 | 平稳 | 高频命中 | **A** |
| PS-P3 | 独立性（Independence） | 47 | 9 | 38 | 平稳 | 高频命中 | **A** |
| PS-P4 | 方差与协方差（Variance and covariance） | 17 | 3 | 14 | 平稳 | 高频命中 | **A** |
| PS-P5 | 相关（correlation） | 5 | 0 | 5 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-P6 | 矩（moment） | 4 | 1 | 3 | 平稳 | 偶发命中 | **C** |
| PS-P7 | 各种分布函数（Various distribution functions） | 14 | 4 | 10 | 平稳 | 高频命中 | **B** |
| PS-P8 | 多元分布（Multivariate distribution） | 6 | 3 | 3 | 上升 | 偶发命中 | **B** |
| PS-P9 | 特征函数（Characteristic function） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| PS-P10 | 母函数/生成函数（Generating function） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-P11 | 随机变量各种收敛模式（Various modes of convergence of random variables） | 14 | 4 | 10 | 平稳 | 高频命中 | **B** |
| PS-P12 | Bayes 公式（Bayes formula） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-P13 | 条件概率（Conditional probability） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-P14 | 给定 sigma-域的条件期望（Conditional expectation given a sigma-field） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| PS-P15 | 大数定律（Laws of large numbers） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-P16 | 中心极限定理（Central limit theorems） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-P17 | 鞅（Martingales） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-P18 | Markov 链（Markov chains） | 4 | 1 | 3 | 平稳 | 偶发命中 | **C** |
| PS-P19 | Poisson 过程的基本性质（Basic properties of Poisson processes） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-P20 | Brown 运动的基本性质（Basic properties of Brownian motion） | 1 | 1 | 0 | 新兴（仅近五年出现） | 偶发命中 | **C** |
| PS-S1 | 连续分布族 normal/chi-sq/t/F/gamma/beta（Families of continuous distributions: normal, chi-sq, t, F, gamma, beta） | 11 | 3 | 8 | 平稳 | 高频命中 | **B** |
| PS-S2 | 离散分布族 multinomial/Poisson/negative binomial（Families of discrete distributions: multinomial, Poisson, negative binomial） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| PS-S3 | 基本统计量：样本均值、方差、中位数与分位数（Basic statistics: sample mean, variance, median and quantiles） | 7 | 1 | 6 | 下降 | 偶发命中 | **B** |
| PS-T1 | Neyman-Pearson 范式（Neyman-Pearson paradigm） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-T2 | 原假设与备择假设（null and alternative hypotheses） | 3 | 1 | 2 | 上升 | 偶发命中 | **C** |
| PS-T3 | 简单与复合假设（simple and composite hypotheses） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-T4 | 第一类与第二类错误（type I and type II errors） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-T5 | 功效（power） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-T6 | 最大功效检验（most powerful test） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-T7 | 似然比检验（likelihood ratio test） | 2 | 0 | 2 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-T8 | Neyman-Pearson 定理（Neyman-Pearson Theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-T9 | 广义似然比检验（generalized likelihood ratio test） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-E1 | 参数估计（Parameter estimation） | 24 | 6 | 18 | 平稳 | 高频命中 | **A** |
| PS-E2 | 矩方法（method of moments） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-E3 | 极大似然估计（maximum likelihood estimation） | 8 | 1 | 7 | 下降 | 高频命中 | **B** |
| PS-E4 | 估计量的评价准则（criteria for evaluation of estimators） | 15 | 4 | 11 | 平稳 | 高频命中 | **B** |
| PS-E5 | Fisher 信息及其应用（Fisher information and its use） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-E6 | 置信区间（confidence interval） | 5 | 1 | 4 | 平稳 | 偶发命中 | **C** |
| PS-B1 | 先验（Prior） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-B2 | 后验（posterior） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-B3 | 共轭先验（conjugate priors） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-B4 | Bayes 估计量（Bayesian estimator） | 1 | 0 | 1 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-L1 | 相合性（Consistency） | 3 | 0 | 3 | 已消失（近五年未考） | 偶发命中 | **C** |
| PS-L2 | 渐近正态性（asymptotic normality） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| PS-L3 | 似然比统计量的卡方近似（chi-sq approximation to likelihood ratio statistic） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |

### 3.6 数学物理（Mathematical Physics，2022 年起设科）

真题 30 道（近五年 30 道）。

| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |
|---|---|---|---|---|---|---|---|
| MP-1 | 最小作用量原理（principle of least action） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-2 | Euler-Lagrange 方程（Euler-Lagrangian equation） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-3 | Noether 定理（Noether theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-4 | Kepler 问题（Kepler problem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-5 | 刚体（rigid body） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-6 | Hamilton 方程（Hamilton's equation） | 7 | 7 | 0 | n/a（该科目无早期样本） | 偶发命中 | **A** |
| MP-7 | Poisson 括号（Poisson bracket） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-8 | Liouville 定理（Liouville's theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-9 | 正则变换（canonical transformation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-10 | Hamilton-Jacobi 理论（Hamilton-Jacobi theory） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-11 | 静电学与静磁学（Electrostatics and magnetostatics） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-12 | 场、势、电荷（fields, potentials, charges） | 11 | 11 | 0 | n/a（该科目无早期样本） | 高频命中 | **A** |
| MP-13 | 物质中的电场与磁场（electric and magnetic fields in matter） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-14 | Coulomb 定律（Coulomb's law） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-15 | Lorentz 力定律（Lorentz force law） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-16 | Ohm 定律（Ohm's law） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-17 | Faraday 定律（Faraday's law） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-18 | Gauss 定律（Gauss's law） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-19 | Maxwell 方程（Maxwell's equation） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-20 | 守恒律（conservation laws） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-21 | 电磁波（electromagnetic waves） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-22 | 辐射（radiation） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-23 | 镜像法（the method of images） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-24 | 分离变量法（separation of variables） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-25 | 多极展开（multipole expansion） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-26 | 热力学基本原理（Fundamental principles of thermodynamics） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-27 | 热力学势与过程（thermodynamic potentials and processes） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-28 | 相平衡与相变（phase equilibrium and phase transitions） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-29 | 配分函数（partition function） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-30 | 熵（entropy） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-31 | 概率论（统计物理）（Probability theory） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-32 | 微正则、正则与巨正则系综（microcanonical, canonical and grand-canonical ensembles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-33 | Boltzmann、Bose 与 Fermi 统计分布（The Boltzmann, Bose and Fermi statistical distributions） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-34 | 实例：理想气体模型（ideal gas model） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-35 | 实例：顺磁体（paramagnet） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-36 | 实例：理想量子气体（ideal quantum gases） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-37 | 实例：退化 Fermi 系统（degenerate Fermi systems） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-38 | 实例：光子与声子（photons and phonons） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-39 | 实例：Bose-Einstein 凝聚（Bose-Einstein condensation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-40 | Hilbert 空间、态、可观测量、波函数（Hilbert space, states, observables, wave functions） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-41 | Schrodinger 方程（Schrodinger equation） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-42 | Schrodinger 与 Heisenberg 绘景（Schrodinger and Heisenberg pictures） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-43 | 正则量子化（canonical quantization） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-44 | 密度矩阵（density matrix） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-45 | 实例：谐振子（harmonic oscillator） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-46 | 实例：氢原子模型（hydrogen atom model） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-47 | 实例：势阱问题（potential well problems） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-48 | 量子力学中的对称性（Symmetry in quantum mechanics） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-49 | 角动量（angular momentum） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-50 | 自旋（spin） | 5 | 5 | 0 | n/a（该科目无早期样本） | 偶发命中 | **A** |
| MP-51 | 全同粒子（identical particles） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-52 | 原子结构（atomic structure） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-53 | 微扰论（Perturbation theory） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-54 | 散射（scattering） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-55 | 近似方法（approximation method） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-56 | 微分几何：度量、向量、张量、微分形式、流形、联络、曲率、测地线（metric, vector, tensor, differential forms, manifold, connections, curvature, geodesic） | 9 | 9 | 0 | n/a（该科目无早期样本） | 高频命中 | **A** |
| MP-57 | 标架、Lie 导数、等距与 Killing 向量（tetrads, Lie derivatives, isometries and Killing vectors） | 4 | 4 | 0 | n/a（该科目无早期样本） | 偶发命中 | **A** |
| MP-58 | 等效原理（the principle of equivalence） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-59 | Einstein 方程（Einstein's equation） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-60 | Hilbert-Einstein 作用量（Hilbert-Einstein action） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-61 | 精确解：Minkowski、de Sitter、anti-de Sitter 时空（Minkowski, de Sitter, anti-de Sitter spacetimes） | 4 | 4 | 0 | n/a（该科目无早期样本） | 偶发命中 | **A** |
| MP-62 | 黑洞解（black hole solutions） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-63 | 因果结构（Causal structure） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-64 | 经典场论：Lagrange 与 Hamilton 形式（Classical field theory: Lagrangian and Hamiltonian formalism） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-65 | Noether 定理（场论）（Noether's theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-66 | 量子化：正则量子化与路径积分（canonical quantization and path integrals） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-67 | 费米子：Poincare 群的表示（representations of Poincare group） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-68 | Dirac 方程（Dirac equation） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-69 | S-矩阵：LSZ 约化（LSZ reduction） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-70 | Feynman 传播子（Feymann propagator） | 3 | 3 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-71 | Feynman 规则（Feymann rules） | 1 | 1 | 0 | n/a（该科目无早期样本） | 偶发命中 | **C** |
| MP-72 | 正规序（normal ordering） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-73 | Wick 定理（Wick's theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-74 | 光学定理（the optical theorem） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-75 | 定域性（locality） | 0 | 0 | 0 | 从未考过 | 零命中 | **D** |
| MP-76 | 重整化：正则化与截断（regularization and cutoff） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-77 | 重整化：抵消项（counter terms） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |
| MP-78 | 重整化群（renormalization group） | 2 | 2 | 0 | n/a（该科目无早期样本） | 偶发命中 | **B** |

## 4. 按考纲复习的优先级排序 ★核心节

排序键 = **科目内命中密度(%) × 近年趋势系数**（记为「预估收益」）。
A = 主战场，必须拿下；B = 高频，值得投入；C = 边角，按时间取舍；D = 从未考过，可战略性放弃。

### 4.1 跨科目 A 级总榜（共 18 条）

| # | 科目 | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | Probability & Statistics | 随机变量（Random variable） | 60 | 15 | 47.2% | 平稳 | **47.2** |
| 2 | Algebra & Number Theory | 因子分解与素数（Factorization and the primes） | 44 | 12 | 29.3% | 上升 | **41.1** |
| 3 | Probability & Statistics | 独立性（Independence） | 47 | 9 | 37.0% | 平稳 | **37.0** |
| 4 | Mathematical Physics | 场、势、电荷（fields, potentials, charges） | 11 | 11 | 36.7% | n/a（该科目无早期样本） | **36.7** |
| 5 | Mathematical Physics | 微分几何：度量、向量、张量、微分形式、流形、联络、曲率、测地线（metric, vector, tensor, differential forms, manifold, connections, curvature, geodesic） | 9 | 9 | 30.0% | n/a（该科目无早期样本） | **30.0** |
| 6 | Geometry & Topology | 曲率的定义（Definition of curvature） | 46 | 9 | 28.9% | 平稳 | **28.9** |
| 7 | Geometry & Topology | Riemann 度量（Riemannian metrics） | 32 | 10 | 20.1% | 上升 | **28.2** |
| 8 | Mathematical Physics | Hamilton 方程（Hamilton's equation） | 7 | 7 | 23.3% | n/a（该科目无早期样本） | **23.3** |
| 9 | Computational & Applied | 稳定性、精度与收敛性（stability, accuracy and convergence） | 20 | 8 | 14.8% | 上升 | **20.7** |
| 10 | Probability & Statistics | 参数估计（Parameter estimation） | 24 | 6 | 18.9% | 平稳 | **18.9** |
| 11 | Mathematical Physics | 自旋（spin） | 5 | 5 | 16.7% | n/a（该科目无早期样本） | **16.7** |
| 12 | Geometry & Topology | Riemann 曲率张量的性质（properties of the Riemann curvature tensor） | 25 | 5 | 15.7% | 平稳 | **15.7** |
| 13 | Probability & Statistics | 期望（Expectation） | 18 | 4 | 14.2% | 平稳 | **14.2** |
| 14 | Probability & Statistics | 方差与协方差（Variance and covariance） | 17 | 3 | 13.4% | 平稳 | **13.4** |
| 15 | Mathematical Physics | 标架、Lie 导数、等距与 Killing 向量（tetrads, Lie derivatives, isometries and Killing vectors） | 4 | 4 | 13.3% | n/a（该科目无早期样本） | **13.3** |
| 16 | Mathematical Physics | 精确解：Minkowski、de Sitter、anti-de Sitter 时空（Minkowski, de Sitter, anti-de Sitter spacetimes） | 4 | 4 | 13.3% | n/a（该科目无早期样本） | **13.3** |
| 17 | Algebra & Number Theory | 局部域（local fields） | 13 | 5 | 8.7% | 上升 | **12.1** |
| 18 | Algebra & Number Theory | Galois 理论基本定理（Fundamental theorems of Galois theory） | 18 | 4 | 12.0% | 平稳 | **12.0** |

### 4.2 代数与数论（Algebra and Number Theory）：条目优先级排序

**A 级 · 主战场（得分 ≥12） —— 3 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | NT-1 | 因子分解与素数（Factorization and the primes） | 44 | 12 | 29.3% | 上升 | 41.1 |
| 2 | NT-12 | 局部域（local fields） | 13 | 5 | 8.7% | 上升 | 12.1 |
| 3 | ALG-GA1 | Galois 理论基本定理（Fundamental theorems of Galois theory） | 18 | 4 | 12.0% | 平稳 | 12.0 |

**B 级 · 高优先（4–12） —— 6 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | ALG-GA2 | 有限域（finite fields） | 12 | 5 | 8.0% | 上升 | 11.2 |
| 2 | NT-2 | 同余（congruences） | 10 | 3 | 6.7% | 上升 | 9.3 |
| 3 | NT-7 | 数域（Number fields） | 6 | 4 | 4.0% | 上升 | 5.6 |
| 4 | ALG-F1 | 分裂域（splitting fields） | 8 | 2 | 5.3% | 平稳 | 5.3 |
| 5 | NT-13 | 分歧（ramification） | 5 | 3 | 3.3% | 上升 | 4.7 |
| 6 | NT-8 | 理想的唯一分解（unique factorization of ideals） | 5 | 2 | 3.3% | 上升 | 4.7 |

**C 级 · 一般优先（小于 4） —— 18 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | ALG-H1 | 正合列（exact sequences） | 3 | 1 | 2.0% | 上升 | 2.8 |
| 2 | ALG-LIE2 | 幂零与半单 Lie 代数、Lie 群（nilpotent and semi-simple Lie algebras and Lie groups） | 3 | 1 | 2.0% | 上升 | 2.8 |
| 3 | ALG-G3 | 可解群（solvable groups） | 4 | 1 | 2.7% | 平稳 | 2.7 |
| 4 | ALG-GA3 | 分圆域（cyclotomic fields） | 4 | 1 | 2.7% | 平稳 | 2.7 |
| 5 | ALG-C7 | 离散赋值环（DVRs） | 2 | 2 | 1.3% | 新兴（仅近五年出现） | 2.0 |
| 6 | ALG-C3 | 整扩张（integral extensions） | 2 | 1 | 1.3% | 上升 | 1.9 |
| 7 | ALG-R6 | 多项式环（polynomial rings） | 2 | 1 | 1.3% | 上升 | 1.9 |
| 8 | ALG-REP1 | 特征标理论（character theory） | 2 | 1 | 1.3% | 上升 | 1.9 |
| 9 | ALG-G1 | Sylow 定理（Sylow theorems） | 5 | 0 | 3.3% | 已消失（近五年未考） | 1.3 |
| 10 | ALG-C1 | 局部化（localizations） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.0 |
| 11 | ALG-C4 | 理想的根（radicals of ideals） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.0 |
| 12 | ALG-F2 | 可分与不可分扩张（separable and inseparable extensions） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 13 | ALG-R2 | 行列式（determinants） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 14 | NT-10 | 单位群的结构（structure of unit group） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 15 | ALG-R1 | 张量积（tensor products） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |
| 16 | ALG-R4 | 主理想整环（PID） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |
| 17 | ALG-R5 | 唯一分解整环（UFD） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |
| 18 | NT-9 | 类群的有限性（finiteness of class group） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |

### 4.3 分析与偏微分方程（Analysis and Differential Equations）：条目优先级排序

**A 级 · 主战场（得分 ≥12）**：无。

**B 级 · 高优先（4–12） —— 3 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | AN-C1 | 全纯与亚纯函数（Holomorphic and meromorphic functions） | 25 | 2 | 15.9% | 下降 | 11.9 |
| 2 | AN-R20 | Fourier 变换（Fourier transform） | 8 | 2 | 5.1% | 上升 | 7.1 |
| 3 | AN-D12 | 调和函数（harmonic functions） | 11 | 2 | 7.0% | 平稳 | 7.0 |

**C 级 · 一般优先（小于 4） —— 21 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | AN-D15 | 热方程（Heat equation） | 3 | 2 | 1.9% | 上升 | 2.7 |
| 2 | AN-D3 | 有限区间上的自伴边值问题（self-adjoint boundary value problems on finite intervals） | 3 | 1 | 1.9% | 上升 | 2.7 |
| 3 | AN-R21 | 卷积（convolution） | 3 | 1 | 1.9% | 上升 | 2.7 |
| 4 | AN-R9 | Hilbert 空间（Hilbert space） | 8 | 0 | 5.1% | 已消失（近五年未考） | 2.0 |
| 5 | AN-R16 | 紧算子的基本性质（Basic properties of compact operators） | 6 | 0 | 3.8% | 已消失（近五年未考） | 1.5 |
| 6 | AN-R4 | Lp 空间（Lp space） | 6 | 0 | 3.8% | 已消失（近五年未考） | 1.5 |
| 7 | AN-C2 | 共形映射（Conformal maps） | 5 | 0 | 3.2% | 已消失（近五年未考） | 1.3 |
| 8 | AN-D16 | 基本解（fundamental solutions） | 1 | 1 | 0.6% | 新兴（仅近五年出现） | 1.0 |
| 9 | AN-D4 | 临界点、相空间、稳定性分析（critical points, phase space, stability analysis） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 10 | AN-R18 | 紧算子的谱（spectrum of compact operators） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 11 | AN-R2 | Borel 测度（Borel measure） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 12 | AN-C10 | Dirichlet 问题（Dirichlet's problem） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 13 | AN-D11 | Dirichlet 问题解的存在性（existence of solutions of Dirichlet problem） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 14 | AN-D13 | 极大值原理及应用（maximal principle and applications） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 15 | AN-D17 | 波动方程：初值与边值条件（Wave equations: initial condition and boundary condition） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 16 | AN-D21 | 解的唯一性与稳定性（uniqueness and stability of solutions） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 17 | AN-D22 | 分布（Distributions） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 18 | AN-D23 | Sobolev 嵌入定理（Sobolev embedding theorem） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 19 | AN-D6 | 线性与拟线性 PDE（linear and quasi-linear PDE） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 20 | AN-R10 | 有界变差复测度（Complex measures of bounded variation） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 21 | AN-R19 | Fourier 级数（Fourier series） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |

### 4.4 计算与应用数学（Computational and Applied Mathematics）：条目优先级排序

**A 级 · 主战场（得分 ≥12） —— 1 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | CA-16 | 稳定性、精度与收敛性（stability, accuracy and convergence） | 20 | 8 | 14.8% | 上升 | 20.7 |

**B 级 · 高优先（4–12） —— 5 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | CA-19 | 有限差分方法（Finite difference method） | 8 | 4 | 5.9% | 上升 | 8.3 |
| 2 | CA-14 | 单步法（Single step methods） | 5 | 3 | 3.7% | 上升 | 5.2 |
| 3 | CA-12 | 条件数与奇异值分解（condition number and singular value decomposition） | 9 | 1 | 6.7% | 下降 | 5.0 |
| 4 | CA-24 | 尺度行为与渐近分析（Scaling behavior and asymptotics analysis） | 4 | 2 | 3.0% | 上升 | 4.2 |
| 5 | CA-9 | 不动点方法（fixed-point methods） | 4 | 2 | 3.0% | 上升 | 4.2 |

**C 级 · 一般优先（小于 4） —— 14 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | CA-4 | 多项式与样条插值与逼近（polynomial and spline interpolations and approximation） | 5 | 1 | 3.7% | 平稳 | 3.7 |
| 2 | CA-17 | 绝对稳定性与长时间行为（absolute stability, long time behavior） | 3 | 2 | 2.2% | 上升 | 3.1 |
| 3 | CA-20 | 有限元方法（finite element method） | 3 | 1 | 2.2% | 上升 | 3.1 |
| 4 | CA-21 | 谱方法（spectral method） | 3 | 1 | 2.2% | 上升 | 3.1 |
| 5 | CA-23 | 数学建模、模拟与应用分析（Mathematical modeling, simulation, and applied analysis） | 6 | 0 | 4.4% | 已消失（近五年未考） | 1.8 |
| 6 | CA-5 | 最小二乘逼近（least-squares approximation） | 5 | 0 | 3.7% | 已消失（近五年未考） | 1.5 |
| 7 | CA-18 | 刚性 ODE 的数值方法（numerical methods for stiff ODE's） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.1 |
| 8 | CA-22 | Lax 等价定理（Lax equivalence theorem） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.1 |
| 9 | CA-32 | Newton 法（优化）（Newton's method） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.1 |
| 10 | CA-7 | Newton 法（Newton's method） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.1 |
| 11 | CA-8 | 拟 Newton 法（quasi-Newton's methods） | 1 | 1 | 0.7% | 新兴（仅近五年出现） | 1.1 |
| 12 | CA-11 | 线性系统与特征值问题的经典与现代迭代法（Classical and modern iterative method for linear systems and eigenvalue problems） | 3 | 0 | 2.2% | 已消失（近五年未考） | 0.9 |
| 13 | CA-15 | 多步法（multi-step methods） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |
| 14 | CA-31 | 罚函数法（penalty method） | 1 | 0 | 0.7% | 已消失（近五年未考） | 0.3 |

### 4.5 几何与拓扑（Geometry and Topology）：条目优先级排序

**A 级 · 主战场（得分 ≥12） —— 3 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | GT-R9 | 曲率的定义（Definition of curvature） | 46 | 9 | 28.9% | 平稳 | 28.9 |
| 2 | GT-R1 | Riemann 度量（Riemannian metrics） | 32 | 10 | 20.1% | 上升 | 28.2 |
| 3 | GT-R13 | Riemann 曲率张量的性质（properties of the Riemann curvature tensor） | 25 | 5 | 15.7% | 平稳 | 15.7 |

**B 级 · 高优先（4–12） —— 7 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | GT-A1 | 基本群（Fundamental groups） | 12 | 3 | 7.5% | 平稳 | 7.5 |
| 2 | GT-A5 | 奇异同调与上同调（Singular homology and cohomology） | 15 | 1 | 9.4% | 下降 | 7.1 |
| 3 | GT-R2 | 测地线的定义（definition of a geodesic） | 11 | 2 | 6.9% | 平稳 | 6.9 |
| 4 | GT-A2 | 覆叠空间（Covering spaces） | 7 | 2 | 4.4% | 上升 | 6.2 |
| 5 | GT-L1 | GL(n)、SU(n)、SO(n)、U(n) 的定义（The definitions of Gl(n), SU(n), SO(n), U(n)） | 6 | 3 | 3.8% | 上升 | 5.3 |
| 6 | GT-V2 | 切丛与余切丛（tangent and cotangent bundles） | 6 | 2 | 3.8% | 上升 | 5.3 |
| 7 | GT-M3 | 子流形（submanifolds） | 7 | 1 | 4.4% | 平稳 | 4.4 |

**C 级 · 一般优先（小于 4） —— 19 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | GT-L3 | Lie 代数（Lie algebras） | 3 | 3 | 1.9% | 新兴（仅近五年出现） | 2.8 |
| 2 | GT-R7 | 协变导数与主丛上的联络（covariant derivative for a vector bundle and connection on a principal bundle） | 3 | 1 | 1.9% | 上升 | 2.6 |
| 3 | GT-L4 | 左右不变向量场与微分形式（right and left invariant vector fields and differential forms） | 2 | 2 | 1.3% | 新兴（仅近五年出现） | 1.9 |
| 4 | GT-A3 | 高阶同伦群（Higher homotopy groups） | 2 | 1 | 1.3% | 上升 | 1.8 |
| 5 | GT-A4 | 纤维化与纤维化的长正合列（Fibrations and the long exact sequence of a fibration） | 2 | 1 | 1.3% | 上升 | 1.8 |
| 6 | GT-M7 | 度理论（degree theory） | 5 | 0 | 3.1% | 已消失（近五年未考） | 1.3 |
| 7 | GT-A13 | Hopf 指标定理（Hopf index theorem） | 1 | 1 | 0.6% | 新兴（仅近五年出现） | 0.9 |
| 8 | GT-L2 | 矩阵 Lie 群的流形结构（their manifold structures） | 1 | 1 | 0.6% | 新兴（仅近五年出现） | 0.9 |
| 9 | GT-R12 | Levi-Civita 联络（Definition of Levi-Civita connection） | 1 | 1 | 0.6% | 新兴（仅近五年出现） | 0.9 |
| 10 | GT-V4 | 微分形式、外积、外微分（Definition of differential forms, exterior product, exterior derivative） | 3 | 0 | 1.9% | 已消失（近五年未考） | 0.8 |
| 11 | GT-V5 | de Rham 上同调（de Rham cohomology） | 3 | 0 | 1.9% | 已消失（近五年未考） | 0.8 |
| 12 | GT-A11 | Poincare 对偶（Poincare duality） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 13 | GT-M8 | 流形上的积分（integration on manifolds） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 14 | GT-V1 | 实与复向量丛的定义（Definition of real and complex vector bundles） | 2 | 0 | 1.3% | 已消失（近五年未考） | 0.5 |
| 15 | GT-L5 | 指数映射（the exponential map） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 16 | GT-R14 | 常曲率流形（manifolds of constant curvature） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 17 | GT-R15 | Jacobi 场（Jacobi fields） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 18 | GT-R16 | 测地线的第二变分（second variation of geodesics） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |
| 19 | GT-R18 | 正曲率流形（manifolds of positive curvature） | 1 | 0 | 0.6% | 已消失（近五年未考） | 0.2 |

### 4.6 概率与统计（Probability and Statistics）：条目优先级排序

**A 级 · 主战场（得分 ≥12） —— 5 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | PS-P1 | 随机变量（Random variable） | 60 | 15 | 47.2% | 平稳 | 47.2 |
| 2 | PS-P3 | 独立性（Independence） | 47 | 9 | 37.0% | 平稳 | 37.0 |
| 3 | PS-E1 | 参数估计（Parameter estimation） | 24 | 6 | 18.9% | 平稳 | 18.9 |
| 4 | PS-P2 | 期望（Expectation） | 18 | 4 | 14.2% | 平稳 | 14.2 |
| 5 | PS-P4 | 方差与协方差（Variance and covariance） | 17 | 3 | 13.4% | 平稳 | 13.4 |

**B 级 · 高优先（4–12） —— 7 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | PS-E4 | 估计量的评价准则（criteria for evaluation of estimators） | 15 | 4 | 11.8% | 平稳 | 11.8 |
| 2 | PS-P11 | 随机变量各种收敛模式（Various modes of convergence of random variables） | 14 | 4 | 11.0% | 平稳 | 11.0 |
| 3 | PS-P7 | 各种分布函数（Various distribution functions） | 14 | 4 | 11.0% | 平稳 | 11.0 |
| 4 | PS-S1 | 连续分布族 normal/chi-sq/t/F/gamma/beta（Families of continuous distributions: normal, chi-sq, t, F, gamma, beta） | 11 | 3 | 8.7% | 平稳 | 8.7 |
| 5 | PS-P8 | 多元分布（Multivariate distribution） | 6 | 3 | 4.7% | 上升 | 6.6 |
| 6 | PS-E3 | 极大似然估计（maximum likelihood estimation） | 8 | 1 | 6.3% | 下降 | 4.7 |
| 7 | PS-S3 | 基本统计量：样本均值、方差、中位数与分位数（Basic statistics: sample mean, variance, median and quantiles） | 7 | 1 | 5.5% | 下降 | 4.1 |

**C 级 · 一般优先（小于 4） —— 18 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | PS-E6 | 置信区间（confidence interval） | 5 | 1 | 3.9% | 平稳 | 3.9 |
| 2 | PS-P14 | 给定 sigma-域的条件期望（Conditional expectation given a sigma-field） | 3 | 1 | 2.4% | 上升 | 3.3 |
| 3 | PS-S2 | 离散分布族 multinomial/Poisson/negative binomial（Families of discrete distributions: multinomial, Poisson, negative binomial） | 3 | 1 | 2.4% | 上升 | 3.3 |
| 4 | PS-T2 | 原假设与备择假设（null and alternative hypotheses） | 3 | 1 | 2.4% | 上升 | 3.3 |
| 5 | PS-P18 | Markov 链（Markov chains） | 4 | 1 | 3.1% | 平稳 | 3.1 |
| 6 | PS-P6 | 矩（moment） | 4 | 1 | 3.1% | 平稳 | 3.1 |
| 7 | PS-P5 | 相关（correlation） | 5 | 0 | 3.9% | 已消失（近五年未考） | 1.6 |
| 8 | PS-P20 | Brown 运动的基本性质（Basic properties of Brownian motion） | 1 | 1 | 0.8% | 新兴（仅近五年出现） | 1.2 |
| 9 | PS-P9 | 特征函数（Characteristic function） | 1 | 1 | 0.8% | 新兴（仅近五年出现） | 1.2 |
| 10 | PS-L1 | 相合性（Consistency） | 3 | 0 | 2.4% | 已消失（近五年未考） | 0.9 |
| 11 | PS-T7 | 似然比检验（likelihood ratio test） | 2 | 0 | 1.6% | 已消失（近五年未考） | 0.6 |
| 12 | PS-B1 | 先验（Prior） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 13 | PS-B4 | Bayes 估计量（Bayesian estimator） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 14 | PS-P10 | 母函数/生成函数（Generating function） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 15 | PS-P12 | Bayes 公式（Bayes formula） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 16 | PS-P13 | 条件概率（Conditional probability） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 17 | PS-P16 | 中心极限定理（Central limit theorems） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |
| 18 | PS-T5 | 功效（power） | 1 | 0 | 0.8% | 已消失（近五年未考） | 0.3 |

### 4.7 数学物理（Mathematical Physics，2022 年起设科）：条目优先级排序

**A 级 · 主战场（得分 ≥12） —— 6 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | MP-12 | 场、势、电荷（fields, potentials, charges） | 11 | 11 | 36.7% | n/a（该科目无早期样本） | 36.7 |
| 2 | MP-56 | 微分几何：度量、向量、张量、微分形式、流形、联络、曲率、测地线（metric, vector, tensor, differential forms, manifold, connections, curvature, geodesic） | 9 | 9 | 30.0% | n/a（该科目无早期样本） | 30.0 |
| 3 | MP-6 | Hamilton 方程（Hamilton's equation） | 7 | 7 | 23.3% | n/a（该科目无早期样本） | 23.3 |
| 4 | MP-50 | 自旋（spin） | 5 | 5 | 16.7% | n/a（该科目无早期样本） | 16.7 |
| 5 | MP-57 | 标架、Lie 导数、等距与 Killing 向量（tetrads, Lie derivatives, isometries and Killing vectors） | 4 | 4 | 13.3% | n/a（该科目无早期样本） | 13.3 |
| 6 | MP-61 | 精确解：Minkowski、de Sitter、anti-de Sitter 时空（Minkowski, de Sitter, anti-de Sitter spacetimes） | 4 | 4 | 13.3% | n/a（该科目无早期样本） | 13.3 |

**B 级 · 高优先（4–12） —— 20 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | MP-13 | 物质中的电场与磁场（electric and magnetic fields in matter） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 2 | MP-15 | Lorentz 力定律（Lorentz force law） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 3 | MP-19 | Maxwell 方程（Maxwell's equation） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 4 | MP-45 | 实例：谐振子（harmonic oscillator） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 5 | MP-48 | 量子力学中的对称性（Symmetry in quantum mechanics） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 6 | MP-70 | Feynman 传播子（Feymann propagator） | 3 | 3 | 10.0% | n/a（该科目无早期样本） | 10.0 |
| 7 | MP-11 | 静电学与静磁学（Electrostatics and magnetostatics） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 8 | MP-20 | 守恒律（conservation laws） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 9 | MP-27 | 热力学势与过程（thermodynamic potentials and processes） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 10 | MP-28 | 相平衡与相变（phase equilibrium and phase transitions） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 11 | MP-29 | 配分函数（partition function） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 12 | MP-30 | 熵（entropy） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 13 | MP-31 | 概率论（统计物理）（Probability theory） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 14 | MP-49 | 角动量（angular momentum） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 15 | MP-54 | 散射（scattering） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 16 | MP-62 | 黑洞解（black hole solutions） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 17 | MP-64 | 经典场论：Lagrange 与 Hamilton 形式（Classical field theory: Lagrangian and Hamiltonian formalism） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 18 | MP-76 | 重整化：正则化与截断（regularization and cutoff） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 19 | MP-77 | 重整化：抵消项（counter terms） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |
| 20 | MP-78 | 重整化群（renormalization group） | 2 | 2 | 6.7% | n/a（该科目无早期样本） | 6.7 |

**C 级 · 一般优先（小于 4） —— 10 条**

| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |
|---|---|---|---|---|---|---|---|
| 1 | MP-16 | Ohm 定律（Ohm's law） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 2 | MP-2 | Euler-Lagrange 方程（Euler-Lagrangian equation） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 3 | MP-22 | 辐射（radiation） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 4 | MP-38 | 实例：光子与声子（photons and phonons） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 5 | MP-40 | Hilbert 空间、态、可观测量、波函数（Hilbert space, states, observables, wave functions） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 6 | MP-42 | Schrodinger 与 Heisenberg 绘景（Schrodinger and Heisenberg pictures） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 7 | MP-53 | 微扰论（Perturbation theory） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 8 | MP-59 | Einstein 方程（Einstein's equation） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 9 | MP-68 | Dirac 方程（Dirac equation） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |
| 10 | MP-71 | Feynman 规则（Feymann rules） | 1 | 1 | 3.3% | n/a（该科目无早期样本） | 3.3 |

### 4.8 可以「战略性放弃」的零命中条目（全 153 条）

下列条目在 2010–2026 全部 758 道真题中**零命中**（按考纲分节归并）。除非时间极其充裕，不建议优先投入。

#### Algebra & Number Theory —— 19 / 46 条零命中（41.3%）

- **代数：群论（Group theory）**（2 条）：p-群（p-groups）；自由群（free groups）
- **代数：环与模（Rings and modules）**（1 条）：Jordan 标准形（Jordan canonical form）
- **代数：同调代数（Homological algebra）**（4 条）：分裂（splittings）；蛇引理与五引理（snake and five lemmas）；投射、内射、平坦模（projective, injective, and flat modules）；复形与（上）同调（complexes, (co)homology）
- **代数：交换环（Commutative ring）**（3 条）：Hilbert 基定理（Hilbert's basis theorem）；Zariski 拓扑与 Hilbert 零点定理（Zariski topology and Hilbert's Nullstellensatz）；Dedekind 环（Dedekind rings）
- **代数：有限群表示论（Representations of Finite Groups）**（2 条）：诱导表示（induced representations）；群环的结构（structure of the group ring）
- **代数：Lie 群与 Lie 代数基础（Basics of Lie groups and Lie algebras）**（1 条）：指数映射（exponential map）
- **数论：初等与解析（Number Theory, elementary/analytic）**（4 条）：二次剩余与互反律（quadratic residues and reciprocity）；连分数与逼近（continued fractions and approximations）；eta 函数（eta functions）；zeta 函数（zeta functions）
- **数论：代数数论（Number Theory, algebraic）**（2 条）：Frobenius 元素（Frobenius elements）；弱逼近（weak approximation）

#### Analysis & PDE —— 39 / 63 条零命中（61.9%）

- **实分析（Real Analysis）**（12 条）：积分收敛定理（Convergence theorems for integrals）；Riesz 表示定理（Riesz representation theorem）；Lp 空间的对偶（Duality of Lp space）；Jensen 不等式（Jensen inequality）；Lebesgue 微分定理（Lebesgue differentiation theorem）；Fubini 定理（Fubini theorem）；Radon-Nikodym 定理（Radon-Nikodym theorem）；Hahn-Banach 定理（Hahn-Banach Theorem）；开映射定理（open mapping theorem）；一致有界性定理（uniform boundedness theorem）；闭图像定理（closed graph theorem）；Riesz-Fredholm 理论（Riesz-Fredholm Theory）
- **复分析（Complex Analysis）**（16 条）：分式线性变换（linear fractional transformations）；Schwarz 引理（Schwarz's lemma）；Cauchy 定理（Cauchy's theorem）；Cauchy 积分公式（Cauchy integral formula）；留数（residues）；调和函数：平均值性质（Harmonic functions: the mean value property）；反射原理（the reflection principle）；Laurent 级数（Laurent series）；部分分式展开（partial fractions expansions）；典型乘积（canonical products）；特殊函数：Gamma 函数（the Gamma function）；特殊函数：zeta 函数（the zeta functions）；特殊函数：椭圆函数（elliptic functions）；Riemann 曲面基础（Basics of Riemann surfaces）；Riemann 映射定理（Riemann mapping theorem）；Picard 定理（Picard theorems）
- **微分方程（Differential Equations）**（11 条）：ODE 解的存在唯一性定理（Existence and uniqueness theorems for solutions of ODE）；简单方程的显式解（explicit solutions of simple equations）；一阶偏微分方程（First order partial differential equations）；相平面分析（Phase plane analysis）；Burgers 方程（Burgers equation）；Hamilton-Jacobi 方程（Hamilton-Jacobi equation）；位势方程：Green 函数（Potential equations: Green functions）；Neumann 问题解的存在性（existence of solutions of Neumann's problem）；适定性（well-posedness）；Sturm-Liouville 特征值问题（Sturm-Liouville eigenvalue problem）；能量泛函方法（energy functional method）

#### Computational & Applied —— 14 / 34 条零命中（41.2%）

- **插值与逼近（Interpolation and approximation）**（3 条）：三角插值与逼近（Trigonometric interpolation and approximation）；快速 Fourier 变换（fast Fourier transform）；有理函数逼近（approximations by rational functions）
- **非线性方程求解（Nonlinear equation solvers）**（2 条）：二分法（bisection）；多项式求根（finding roots of polynomials）
- **线性系统与特征值问题（Linear systems and eigenvalue problems）**（1 条）：大型稀疏线性方程组迭代法（iterative methods for large sparse system of linear equations）
- **数学建模、模拟与应用分析（Mathematical modeling, simulation, and applied analysis）**（4 条）：驻相分析（stationary phase analysis）；边界层分析（boundary layer analysis）；模型的定性与定量分析（qualitative and quantitative analysis of mathematical models）；Monte-Carlo 方法（Monte-Carlo method）
- **线性与非线性规划（Linear and nonlinear programming）**（4 条）：单纯形法（Simplex method）；内点法（interior method）；同伦方法与不动点方法（homotopy method and fixed point method）；动态规划（dynamic programming）

#### Geometry & Topology —— 24 / 53 条零命中（45.3%）

- **微分几何：流形基础（Basics of smooth manifolds）**（5 条）：反函数定理（Inverse function theorem）；隐函数定理（implicit function theorem）；Sard 定理（Sard's Theorem）；嵌入定理（embedding theorem）；横截性（transversality）
- **微分几何：向量丛与联络（Vector bundles and connections）**（3 条）：丛上的基本运算（对偶、张量积、外积、直和、拉回）（dual bundle, tensor products, exterior products, direct sums, pull-back bundles）；拉回下的行为（behavior under pull-back）；向量丛上的度量（Metrics on vector bundles）
- **微分几何：Riemann 几何（Riemannian geometry）**（8 条）：测地线的存在性与唯一性（existence and uniqueness of geodesics）；矩阵群的主丛（Definition of a principal Lie group bundle for matrix groups）；相伴向量丛（Associated vector bundles）；主丛与向量丛的关系（Relation between principal bundles and vector bundles）；两者的关系（Relations between the two）；平坦联络（flat connections）；平行移动（parallel transport）；非正曲率流形（Manifolds of nonpositive curvature）
- **代数拓扑（Algebraic Topology）**（8 条）：相对同调（Relative homology）；CW 复形与 CW 复形的同调（CW complexes and the homology of CW complexes）；Mayer-Vietoris 序列（Mayer-Vietoris sequence）；万有系数定理（Universal coefficient theorem）；Kunneth 公式（Kunneth formula）；Lefschetz 不动点公式（Lefschetz fixed point formula）；Cech 上同调与 de Rham 上同调（Cech cohomology and de Rham cohomology）；奇异、Cech 与 de Rham 上同调的等价性（Equivalence between singular, Cech and de Rham cohomology）

#### Probability & Statistics —— 15 / 45 条零命中（33.3%）

- **概率论（Probability）**（3 条）：大数定律（Laws of large numbers）；鞅（Martingales）；Poisson 过程的基本性质（Basic properties of Poisson processes）
- **统计：检验（Testing）**（6 条）：Neyman-Pearson 范式（Neyman-Pearson paradigm）；简单与复合假设（simple and composite hypotheses）；第一类与第二类错误（type I and type II errors）；最大功效检验（most powerful test）；Neyman-Pearson 定理（Neyman-Pearson Theorem）；广义似然比检验（generalized likelihood ratio test）
- **统计：估计（Estimation）**（2 条）：矩方法（method of moments）；Fisher 信息及其应用（Fisher information and its use）
- **统计：Bayes 统计（Bayesian Statistics）**（2 条）：后验（posterior）；共轭先验（conjugate priors）
- **统计：大样本性质（Large sample properties）**（2 条）：渐近正态性（asymptotic normality）；似然比统计量的卡方近似（chi-sq approximation to likelihood ratio statistic）

#### Mathematical Physics —— 42 / 78 条零命中（53.8%）

- **1. 经典力学（Classical mechanics）**（8 条）：最小作用量原理（principle of least action）；Noether 定理（Noether theorem）；Kepler 问题（Kepler problem）；刚体（rigid body）；Poisson 括号（Poisson bracket）；Liouville 定理（Liouville's theorem）；正则变换（canonical transformation）；Hamilton-Jacobi 理论（Hamilton-Jacobi theory）
- **2. 电动力学（Electrodynamics）**（7 条）：Coulomb 定律（Coulomb's law）；Faraday 定律（Faraday's law）；Gauss 定律（Gauss's law）；电磁波（electromagnetic waves）；镜像法（the method of images）；分离变量法（separation of variables）；多极展开（multipole expansion）
- **3. 热力学与统计物理（Thermodynamics and statistical physics）**（8 条）：热力学基本原理（Fundamental principles of thermodynamics）；微正则、正则与巨正则系综（microcanonical, canonical and grand-canonical ensembles）；Boltzmann、Bose 与 Fermi 统计分布（The Boltzmann, Bose and Fermi statistical distributions）；实例：理想气体模型（ideal gas model）；实例：顺磁体（paramagnet）；实例：理想量子气体（ideal quantum gases）；实例：退化 Fermi 系统（degenerate Fermi systems）；实例：Bose-Einstein 凝聚（Bose-Einstein condensation）
- **4. 量子力学（Quantum mechanics）**（8 条）：Schrodinger 方程（Schrodinger equation）；正则量子化（canonical quantization）；密度矩阵（density matrix）；实例：氢原子模型（hydrogen atom model）；实例：势阱问题（potential well problems）；全同粒子（identical particles）；原子结构（atomic structure）；近似方法（approximation method）
- **5. 广义相对论（General relativity）**（3 条）：等效原理（the principle of equivalence）；Hilbert-Einstein 作用量（Hilbert-Einstein action）；因果结构（Causal structure）
- **6. 量子场论（Quantum field theory）**（8 条）：Noether 定理（场论）（Noether's theorem）；量子化：正则量子化与路径积分（canonical quantization and path integrals）；费米子：Poincare 群的表示（representations of Poincare group）；S-矩阵：LSZ 约化（LSZ reduction）；正规序（normal ordering）；Wick 定理（Wick's theorem）；光学定理（the optical theorem）；定域性（locality）

## 5. 反向发现：真题里「超纲」考了什么

把真题中出现、但**不被该科目任何考纲条目覆盖**的考点聚类统计（同一题可命中多类）。

### 5.1 Algebra & Number Theory

| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |
|---|---|---|---|
| 线性代数与矩阵论（特征值/秩/迹/矩阵分解） | 37 | 5 | `2010_AlgebraNumberTheory_individual#1`、`2010_AlgebraNumberTheory_individual#2` |
| 有限群的分类、阶与正规子群（群论基本功） | 17 | 1 | `2010_AlgebraNumberTheory_individual#6`、`2010_AlgebraNumberTheory_team#5` |
| 模与 Noether 环结构 | 13 | 6 | `2011_8_Algebra_Team_2011#2`、`2012_Algebra2012Individual#4` |
| 域扩张的代数性与次数 | 6 | 3 | `2011_4_Algebra_Individual_2011#4`、`2014_algebra2014_team#3` |
| 组合数学（考纲标题含 Combinatorics，但正文无对应条目） | 4 | 0 | `2011_4_Algebra_Individual_2011#5`、`2013_algebra2013_individual#2` |

### 5.2 Analysis & PDE

| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |
|---|---|---|---|
| 数列、级数与极限运算 | 6 | 0 | `2015_analysis2015_individual#1`、`2015_team_analysis2015#6` |
| 凸性与凸分析 | 4 | 0 | `2013_TeamProblems2013#3`、`2013_TeamProblems2013#6` |
| 线性算子谱与紧性（泛函分析进阶） | 4 | 2 | `2011_1_AnalysisDiffEquation_Individual_2011#5`、`2017_analysis2017_individual#6` |
| 不等式的证明与估计技巧 | 3 | 0 | `2014_analysis2014_individual#5`、`2015_analysis2015_individual#3` |

### 5.3 Computational & Applied

| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |
|---|---|---|---|
| 纯数学式线性代数（矩阵/向量空间） | 32 | 10 | `2011_6_AppliedMathProb_Team_2011#1`、`2012_Applied2012individual#4` |
| 概率/统计方法在应用数学中的使用 | 11 | 0 | `2011_2_AppliedMathProb_Individual_2011#3`、`2011_2_AppliedMathProb_Individual_2011#4` |
| 图论与网络优化 | 5 | 0 | `2013_applied2013_individual#5`、`2015_team_applied2015#2` |
| 误差分析与浮点运算 | 3 | 1 | `2013_applied2013_individual#4`、`2021_ExamPaper_21S_computational_and_applied_21s#6` |

### 5.4 Geometry & Topology

| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |
|---|---|---|---|
| 点集拓扑基础（紧性/连通性/分离公理） | 52 | 14 | `2010_GeometryTopology_indi#4`、`2010_GeometryTopology_team#2` |
| 经典曲线曲面论（第一/第二基本形式） | 14 | 2 | `2010_GeometryTopology_indi#2`、`2011_3_GeomTop_Individual_2011#6` |
| Euler 示性数与 Betti 数 | 6 | 4 | `2016_geometry2016_individual#1`、`2017_geometry2017_individual#1` |
| 度规与测地线的具体计算（微分几何习题化） | 4 | 1 | `2013_geometry2013_individual#6`、`2014_geometry2014_individual#2` |

### 5.5 Probability & Statistics

| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |
|---|---|---|---|
| 随机游走与分支过程 | 5 | 0 | `2016_2016_team#1`、`2016_probability2016_individual#1` |
| 回归与线性模型 | 4 | 4 | `2022_ExamPaper_2022_probability_and_statistics_22s#5`、`2024_2024_statistics#4` |
| 次序统计量与充分统计量 | 3 | 0 | `2010_Applied_Computational_Probability_and_Statistics_team#1`、`2013_probability2013_individual#6` |

### 5.6 最值得注意的五条超纲结论

1. **代数卷的隐形主线是线性代数与矩阵论**（37 题，占该科 25%）：特征值、秩、迹、矩阵分解、对角化在考纲里一个字都没有，却是最高频的解题工具。
2. **几何卷的隐形主线是点集拓扑**（52 题，占该科 33%）：紧性、连通性、Hausdorff、同胚、开集这些基础拓扑不在任何条目中——考纲从「基本群」直接开始，跳过了点集拓扑层。
3. **应用卷的隐形主线是数值线性代数**（32 题，占该科 24%）：考纲只写「迭代法、条件数、SVD」，实际大量出现 LU/QR/Cholesky/Gram-Schmidt 与矩阵分解本身。
4. **几何卷的经典曲线曲面论**（14 题）：第一/第二基本形式、Gauss 曲率、极小曲面等经典内容不在微分几何条目中。
5. **概率统计卷的回归与线性模型**（4 题，近五年占比 100%）：考纲完全没有回归/线性模型/ANOVA 条目，却是**唯一「近五年才冒出来」的超纲方向**，需要重点预警。

同时统计出**真题中从未涉及**的考纲外方向（命中 0）：代数几何、复几何与 Kähler 几何、辛几何、示性类、不动点定理（Brouwer/Borsuk-Ulam）、共形场论/弦论/全息、超对称、量子信息、信息论——属于较确定的「不会考」区间。

## 6. 复习建议（由数据直接推出）

| 科目 | 主攻（A 级） | 保底（B 级，前 5） | 可放弃 |
|---|---|---|---|
| Algebra & Number Theory | 因子分解与素数、局部域、Galois 理论基本定理 | 有限域、同余、数域、分裂域、分歧 | 19 条零命中 |
| Analysis & PDE | **无 A 级条目** | 全纯与亚纯函数、Fourier 变换、调和函数 | 39 条零命中 |
| Computational & Applied | 稳定性、精度与收敛性 | 有限差分方法、单步法、条件数与奇异值分解、尺度行为与渐近分析、不动点方法 | 14 条零命中 |
| Geometry & Topology | 曲率的定义、Riemann 度量、Riemann 曲率张量的性质 | 基本群、奇异同调与上同调、测地线的定义、覆叠空间、GL(n)、SU(n)、SO(n)、U(n) 的定义 | 24 条零命中 |
| Probability & Statistics | 随机变量、独立性、参数估计、期望、方差与协方差 | 估计量的评价准则、随机变量各种收敛模式、各种分布函数、连续分布族 normal/chi-sq/t/F/gamma/beta、多元分布 | 15 条零命中 |
| Mathematical Physics | 场、势、电荷、微分几何：度量、向量、张量、微分形式、流形、联络、曲率、测地线、Hamilton 方程、自旋、标架、Lie 导数、等距与 Killing 向量、精确解：Minkowski、de Sitter、anti-de Sitter 时空 | 物质中的电场与磁场、Lorentz 力定律、Maxwell 方程、实例：谐振子、量子力学中的对称性 | 42 条零命中 |

> 注：分析卷最高分条目为「全纯与亚纯函数（Holomorphic and meromorphic functions）」，得分 11.9，仅差 0.1 分未达 A 级阈值，实际应按 A 级强度对待。

- **若只复习一件事**：概率统计卷的「随机变量 / 独立性」组合（60 + 47 题）是全竞赛命中密度最高的考点群。
- **若只放弃一件事**：数理物理的 42 条零命中条目（占该科目 53.8%）与几何的代数拓扑进阶块（相对同调、CW 复形、Mayer-Vietoris、万有系数、Künneth、Poincaré 对偶、Lefschetz、Čech）是性价比最低的投入。
- **小心「趋势下降」的高命中条目**：Hilbert 空间（8 题全在 2021 年前）、Lp 空间（6 题全在早期）、Sylow 定理（5 题全在早期）——历史上考过，近五年已不再出现。
- **注意「新兴」条目**（近五年才首次出现，趋势系数 1.5）：离散赋值环、局部化、理想的根、Newton 法、拟 Newton 法、刚性 ODE、Lax 等价定理、Levi-Civita 联络、矩阵 Lie 群结构、特征函数、Brown 运动等。

## 7. 局限与免责

1. 关键词/正则命中是**下界**，不是真值；术语不出现的题不会计入。
2. 同一题可同时命中多条考纲条目，各条目命中数之和大于真题总数（刻意设计，用于刻画考点重叠度）。
3. 「超纲」判定基于正则覆盖与否，语义相近而措辞不同的考点可能被误判为超纲。
4. 语料在分析期间处于动态更新，本次分析基准为 **758** 题；复跑 `scripts/syllabus_coverage.py` 与 `scripts/make_syllabus_reports.py` 即可刷新全部数字。
5. 趋势的「上升/下降」用率比而非绝对数，故小样本科目（数理物理 30 题）单题权重较大。
