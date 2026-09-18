# 丘成桐大学生数学竞赛 · **总决赛**（2012–2025）真题分析
## 范围：代数与数论/组合 + 分析与微分方程

> 语料：`.tmp/burn2026/txt_finals/`（195 个 txt，源自 ` F:\丘成桐大学生数学竞赛历年总决赛真题 `）
> 加上本报告新增恢复的 `.tmp/burn2026/txt_finals_extra/`。
> 元数据：`.tmp/burn2026/data/finals_index.json`；txt 与原卷的映射由 `.tmp/burn2026/scripts/finals_map.py` 建立
> （规则：把「科目_kind_原文件名去扩展名」中的**非字母数字连续段压成一个下划线**，再去掉首尾下划线）。
> 统计脚本：`finals_alg_ana_stats.py`、`finals_alg_ana_stats2.py`、`finals_final_stats.py`、
> `finals_compare.py`、`finals_forms.py`、`finals_alg_ana_problems.py`（逐题标注库）、
> `finals_alg_ana_extras.py`（恢复卷标注库）、`render_2015_alg.py`、`extract_extra_finals.py`、`gen_report.py`。
> **本题库共 73 卷 / 244 题**（PDF 主集 66 卷 215 题 + 恢复集 7 卷 29 题）。
> 所有题面均来自真实抽取文本，未做任何编造；公式抽取有损处一律逐条标注。

---

## 1. 可分析范围声明

### 1.1 全语料（195 个 txt）的文字层情况

| 科目目录 | 文件数 | chars<800 | chars<100 | chars=0 |
|---|---|---|---|---|
| Algebra, Number Theory and Combinatorics | 37 | 19 | 1 | 1 |
| Analysis and Differential Equations | 32 | 10 | 0 | 0 |
| Applied Math and Computational Math | 40 | 11 | 3 | 3 |
| Geometry and Topology | 33 | 12 | 0 | 0 |
| Probability and Statistics | 41 | 13 | 1 | 1 |
| Mathematical Physics (2022–2025) | 12 | 0 | 0 | 0 |
| **合计** | **195** | **65** | **5** | **5** |

### 1.2 对任务书「约 65 个文件几乎没有文字层」的重要更正

- `chars<800` **不能**等价于「扫描件/图片版」。逐卷核对后确认：本范围（代数+分析 67 个 txt）中，
  chars<800 的短卷绝大多数是**文字层完好、只是题目少或题面短**的正常 PDF。
  例：`2012 Algebra (Individual)` 仅 376 字符 / 1 页，却完整含 3 道题（文本止于第 3 题，无截断）；
  `2024 Analysis (Overall)` 仅 381 字符 / 1 页，完整含 2 道题。若按 chars<800 一律剔除，会丢掉大量真题。
- 真正的「无文字层」在本范围内只有 **1 卷**：`2015 Algebra (Overall)`（0 字符，页面由 **11 张图片**构成）。
- 另有 **2 卷**文字层存在但 **CJK 字体 ToUnicode 表损坏**（抽出来是乱码）：
  `2015 Algebra (Individual)`、`2015 Algebra (Team)`（乱码样例：`1. •Äî¼˜mRn§Ùƒ´•þ`）。
- 上述 3 卷已用 PyMuPDF 以 200 dpi 渲染为 PNG，再由视觉逐字识读（脚本 `render_2015_alg.py`，产物 `.tmp/burn2026/data/render/`），
  题面已补全并进入本题库；因为是人工识读，个别符号可能失真，相关行在 §7 单列。

### 1.3 本范围实际可分析的卷（计数）

| 项目 | 卷数 | 题数 | 说明 |
|---|---|---|---|
| PDF 文字层直接可用 | 63 | 207 | 除 2015 三卷外的全部 PDF |
| 原无/坏文字层，渲染后人工识读 | 3 | 8 | 2015 ALG Individual(3) / Team(3) / Overall(2) |
| **PDF 主集小计** | **66** | **215** | 对应 67 个 txt：2020 ANA Individual 有 I、II 两份文件，此处合为一「卷」 |
| 原 pipeline 完全未转换、本报告从 .doc/.docx 恢复 | 7 | 29 | 见 §1.4 |
| **总计** | **73** | **244** | — |

### 1.4 新发现：7 卷真题从未进入 txt 语料（不是扫描问题，是格式问题）

原抽取管线只处理 `.pdf`；下列真题在 F 盘以 `.doc` / `.docx` 存在，**此前从未被任何报告覆盖**：

| 原文件 | 卷 | 题数 | 本报告恢复方式 | 恢复质量 |
|---|---|---|---|---|
| `2014 Algebra (Team).docx` | 2014 ALG Team | 4 | zipfile 解析 word/document.xml | 文本完整，公式丢失 |
| `2012 Analysis (Individual).doc` | 2012 ANA Individual | 3 | Word COM 另存 ANSI 文本，再按 GBK 解码 | 文本完整，公式全丢（EQ 占位） |
| `2013 Analysis (Individual).docx` | 2013 ANA Individual | 4 | docx 解析 | 文本完整，公式丢失 |
| `2014 Analysis (Individual and Overall).doc` | 2014 ANA Individual | 6 | Word COM，再按 GBK 解码 | 文本完整，公式全丢 |
| `2013 Analysis (Team).docx` | 2013 ANA Team | 4 | docx 解析 | 文本完整；**原文件第 2 题本身为空** |
| `2014 Analysis (Team).docx` | 2014 ANA Team | 6 | docx 解析 | 文本完整，公式丢失 |
| `2013 Analysis (Overall).docx` | 2013 ANA Overall | 2 | docx 解析 | 文本完整，公式丢失 |

恢复脚本：`.tmp/burn2026/scripts/extract_extra_finals.py`；两个 `.doc` 用 Word COM **只读打开、只写工作区**（未改动 F 盘任何文件）。
产物目录：`.tmp/burn2026/txt_finals_extra/`。它们的价值：把分析科目的年份覆盖从「2015 起」提前到 **2012**，
并补出 2013/2014 的 Team 与 Overall 两栏（此前全空）。

### 1.5 明确无法分析的内容清单（先给结论，§7 详列）

| 出处 | 内容 | 原因 | 处理 |
|---|---|---|---|
| 2012 ANA Individual #2 | 整函数迭代题 | .doc 中公式全为 OLE 对象，条件全部丢失 | 放弃分析，仅登记 |
| 2014 ANA Individual #3 | 「对素数全体证明级数发散」 | 公式丢失 | 放弃分析，仅登记 |
| 2014 ANA Individual #5 | (a)(b) 两小问 | 公式丢失 | 放弃分析，仅登记 |
| 2013 ANA Team #2 | 空题 | 原文件即为空标题 | 登记为「原文缺题」 |
| 恢复集其余题的公式 | 条件式 | Word 公式对象无法在禁装库的条件下取出 | 只保留可辨认主题，逐条标注「公式缺失」 |

---

## 2. 逐年逐卷结构表

### 2.1 PDF 主集（66 卷 / 215 题）

难度为**本报告自评 1–5**：1=常规课程题；2=标准题；3=需一两步非平凡想法；4=需专门工具或较长构造；
5=需专门理论（局部域/类域论、特征和、非线性 PDE 估计等），属压轴级。子领域标签定义见 §3.1。题号沿用原卷题号。

| 年份 | 卷别 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|---|
| 2012 | ALG Individual | 1 | k 域上 GL2(k) 中上三角子群 B 的 B×B-轨道分类（(b1,b2)·g=b1gb2^{-1}） | linear/ag | Bruhat 分解 / 双陪集 | 3 |
| 2012 | ALG Individual | 2 | 证明 det(I−AB)=det(I−BA) | linear | Sylvester 行列式恒等式 | 1 |
| 2012 | ALG Individual | 3 | 求所有 Q-代数 R 使 R[X,Y] 中 X²+Y²=(aX+bY)² | comm/quad | 二次型 / 环上分解 | 4 |
| 2012 | ALG Team | 1 | SO(2) 作用 C[X,Y] 的不变量环为 C[X²+Y²]；Fourier 变换与 P(∂) 交换；C[∂x,∂y]^{SO(2)} | rep/harm | 不变量论 / Fourier 变换 / 微分算子环 | 3 |
| 2012 | ALG Team | 2 | Gal(Q(ζ7)/Q)；找 Galois 群为 Z/3Z 的扩张；Q(ζ7) 的二次子域 | galois | 分圆域 / Galois 对应 | 2 |
| 2012 | ALG Overall | 1 | P¹ 上 6 点分支的双覆盖 C：分类其无分支 7-循环覆盖 D 及中间曲线 | ag/galois | Riemann 面 / Hurwitz 公式 / 覆盖理论 | 4 |
| 2013 | ALG Individual | 1 | 循环图 (Z/fZ) 上满足 Orpheus 条件 (φψ=ψφ=0) 的线性映射族，证存在不变直线 ℓ_i | linear/rep | 箭图表示 / 归纳法 | 4 |
| 2013 | ALG Individual | 2 | V_k=R[x]_{≤k} 上 SL2(R) 作用的不可约性、正合列分裂与不变量维数 | rep | Clebsch–Gordan 分解 | 3 |
| 2013 | ALG Individual | 3 | (x²+3)(x³+2) 是否对每个素数 p 都有 mod p 解 | ant/poly | 二次/三次互反律、Chebotarev | 4 |
| 2013 | ALG Team | 1 | tr(A^n)∈F (∀n≥2) ⟹ tr(A)∈F（分步引导：Newton 恒等式 + 特征值） | linear/field | Newton 恒等式 / 迹的域下降 | 3 |
| 2013 | ALG Team | 2 | R[x,y]/(x²+y²−1) 不是 UFD；C[x,y]/(x²+y²−1) 是 PID | comm/ag | 唯一分解 / 曲线的坐标环 | 3 |
| 2014 | ALG Individual | 1 | 解 End k^n 中的方程 x²=x | linear | 幂等元 / 投影分类 | 2 |
| 2014 | ALG Individual | 2 | 构造 Q 上 Galois 群为 Z/nZ 的 Galois 扩张 | galois/field | 分圆域 | 2 |
| 2014 | ALG Individual | 3 | p>3 时 x³+y³=1 在 Z/pZ 的解数；p≡1(3) 时 4p=a²+27b² 与解数 p−2+a | ant | Jacobi 和 / 三次剩余 / Gauss 定理 | 5 |
| 2015 | ALG Individual | 1 | GL_n(R) 中含于开单位球 B(I,1) 的子群 G 必为 {I}（特征值 |λ−1|<1） | linear | 谱半径 / 矩阵范数 | 3 |
| 2015 | ALG Individual | 2 | GL_n(Z)→GL_n(F_p) 在有限子群上单射；GL_2(Z) 有限阶元 m∈{1,…,6} | group | 模群 / 有限阶分类 | 2 |
| 2015 | ALG Individual | 3 | R(x) 中在整数上取整值的函数必为多项式 | comm/poly | 整值多项式 / 有限差分 | 3 |
| 2015 | ALG Team | 1 | Z[w]/(1−w)≅F_p；φ∈F_p[x] 的根重数 < 非零系数个数；(w^{a_ib_j}) 可逆 | ant/linear | 分圆整数 / Vandermonde 型行列式 | 3 |
| 2015 | ALG Team | 2 | 复根 α 的实部非正或 |α|<(1+√(1+4H))/2；由 p 的 b-进制展开得到的多项式不可约 | poly/ant | Cauchy 界 / Cohn 不可约性 | 4 |
| 2015 | ALG Team | 3 | 数值域 W(A)⊂△(z1,z2,z3) ⟺ A=z1A1+z2A2+z3A3（A_i 半正定，ΣA_i=I） | linear | 数值域 / 半正定分解 | 4 |
| 2015 | ALG Overall | 1 | P∈Z[x] 为 k 次本原多项式，d(P)=gcd{P(a):a∈Z} 整除 k! | poly/ant | 整值多项式 / 有限差分 | 3 |
| 2015 | ALG Overall | 2 | 存在 M_n(C) 的基 {X′_i} 使 Tr(X_iX′_j)=δ_ij 且 ΣX_iAX′_i=Tr(A)I_n | linear | 迹形式 / 对偶基 | 3 |
| 2015 | ANA Individual | 1 | Σ 2^n sin(x/3^n) 绝对收敛但在任何 (0,ε) 上不一致收敛 | real | 级数一致收敛 / Dirichlet 判别 | 2 |
| 2015 | ANA Individual | 2 | f∈C^(n)[0,1] 且 ∫f(t)t^j dt=0 (j=1..n) ⟹ ∃ξ, f^(n)(ξ)=0 | real | 正交性 / Rolle 定理迭代 | 3 |
| 2015 | ANA Individual | 3 | 单位盘到自身解析且在某段边界弧上为常数 ⟹ f 恒为常数；Jordan 域？ | cplx | Schwarz 反射 / 唯一性定理 | 3 |
| 2015 | ANA Individual | 4 | 求所有满足 L*(E∩[a,b]) ≤ (b−a)/2 的集合 E | real | Lebesgue 外测度 / 密度 | 4 |
| 2015 | ANA Team | 1 | f∈C_c^∞(R²) 且沿每条直线的积分为 0 ⟹ f≡0 | harm | Radon 变换 / 卷积 | 3 |
| 2015 | ANA Team | 2 | 存在域 D 使 Aut(D) 可数无限；使 Aut(D)≅Z；Aut(D)≅R 是否可能 | cplx | Riemann 面 / 自同构群 | 4 |
| 2015 | ANA Team | 3 | ∫ 1/|f| = +∞（f∈C¹）⟹ ẋ=f(x) 的解存在区间为 (−∞,∞) | ode | 解的存在区间 / 比较 | 3 |
| 2015 | ANA Overall | 1 | Cauchy 函数方程：连续 ⟹ 线性；Borel 可测 ⟹ 连续 | real | Cauchy 方程 / 可测性 | 2 |
| 2015 | ANA Overall | 2 | 概率测度 μ̂(ξ0)=1 ⟹ supp μ 含于 Z 的平移伸缩 | harm | Fourier 变换 / 测度刚性 | 4 |
| 2016 | ALG Individual | 1 | x⁴−4x²−1 的分裂域：不可约性与 Galois 群 | galois | 四次域 / 群阶判定 | 3 |
| 2016 | ALG Individual | 2 | 代数闭包 F̄_p^× 的初等描述与 Frobenius 的作用 | field | 有限域 / Prüfer 群 | 3 |
| 2016 | ALG Individual | 3 | A,B∈M_n(Q) 在 Q 上相似 ⟺ 在 C 上相似 | linear | 有理标准形 / 不变量因子 | 2 |
| 2016 | ALG Team | 1 | 有限生成 Z-代数的极大理想的商是有限域 | comm | Zariski 引理 / Nullstellensatz | 3 |
| 2016 | ALG Team | 2 | 确定阿贝尔群范畴与群范畴的“中心”（恒等函子到自身的自然变换） | cat | 范畴论 / Eckmann–Hilton | 3 |
| 2016 | ALG Team | 3 | Weyl 代数：char 0 无有限维表示；char p>0 时求所有有限维表示 | rep/comm | Weyl 代数 / 中心 / 模 p 约化 | 4 |
| 2016 | ALG Overall | 1 | Q(ζ_{p^n}) 的唯一二次子域；p=2,n≥3 时二次子域个数与具体域 | ant/galois | 分圆域 / Gauss 和 | 4 |
| 2016 | ANA Individual | 1.1 | |f|≤1 于单位盘且 f(±1/2)=0 ⟹ |f(0)|≤1/4 | cplx | Schwarz–Pick / Blaschke 乘积 | 3 |
| 2016 | ANA Individual | 1.2 | a_n=sin(a_{n−1}) ⟹ Σa_n² 发散 | real | 渐近展开 / 比较判别 | 2 |
| 2016 | ANA Individual | 1.3 | L^p[0,1] 范数满足平行四边形律 ⟺ p=2 | func | 内积 / Clarkson 不等式 | 2 |
| 2016 | ANA Individual | 1.4 | 上半平面 Laplace 方程、阶跃边界数据的全部有界解 | pde/potential | Poisson 积分 / 调和函数 | 3 |
| 2016 | ANA Individual | 1.5 | ∀a, f(x+a)−f(x)→0 ⟹ f=g+h, g→0, h′→0 | real | 分解 / 一致连续性 | 4 |
| 2016 | ANA Individual | 1.6 | |a_n|≤K/|n| 时 Fourier 部分和的一致界 sup|f|+2K | harm | Dirichlet 核 / 部分和估计 | 3 |
| 2016 | ANA Team | 1 | 多项式满足 M(R)/R^n ≤ M(r)/r^n，等号 ⟺ f(z)=cz^n | cplx | 最大模原理 | 2 |
| 2016 | ANA Team | 2 | b1=1,b2=2,b_{n+1}=b_n+b_{n−1}，判断 Σ1/b_n 是否收敛 | real | Fibonacci 增长 / 比值判别 | 2 |
| 2016 | ANA Team | 3 | Δu=0 于穿孔球 B1−{0}, u=0 于 ∂B1, u≥0 的全部解 | pde/potential | 可去奇点 / 调和函数 | 3 |
| 2016 | ANA Team | 4 | C¹ 函数的临界值集测度为零 | real | Sard 定理（一维）/ 覆盖 | 2 |
| 2016 | ANA Team | 5 | 迭代不等式 w(τr)≤γw(r)+σ(r) 的解估计（Morrey 型） | harm | 迭代引理 / Campanato 技巧 | 4 |
| 2016 | ANA Team | 6 | 根在 (−1,1) 的首一实多项式经 Chebyshev 代换后根仍在 (−1,1) | approx/special | Chebyshev 多项式 / 交错 | 4 |
| 2016 | ANA Overall | 1 | 正定对称 A 满足 tr A≤N+ε, det A≥1−ε ⟹ ‖A−I‖_HS ≤ C_N√ε | linear | 谱分解 / 特征值扰动 | 3 |
| 2016 | ANA Overall | 2 | T_n(e_m)=e_{nm}：{T_n,T_n*} 与 {T_m,T_m*} 交换 ⟺ (n,m)=1；与所有 T_n 交换的算子为 cI | func | 算子代数 / 交换子 | 4 |
| 2017 | ALG Individual | 1 | 分类 8 阶群及其 C 上不可约表示 | group/rep | 群分类 / 特征标表 | 3 |
| 2017 | ALG Individual | 2 | x⁴+x³+x²+x+1 不可约；Gal(Q(ζ5)/Q) 循环；Gal(Q(ζ20)/Q)≅(Z/20Z)^× | galois | 分圆多项式 / Eisenstein | 3 |
| 2017 | ALG Individual | 3 | R=C[x]/(f)：R 无幂零元 ⟺ 有限生成不可分解 R-模投射 | comm/homol | 交换代数 / Nakayama | 4 |
| 2017 | ALG Team | 1 | G=GL_2(C) 的有限维表示完全可约，并求所有不可约表示 | rep | 完全可约性 / 最高权 | 3 |
| 2017 | ALG Team | 2 | K,L 为素数次扩张，[KL:Q]=[K:Q][L:Q] ⟹ 二者 Galois 闭包相同 | galois/field | 线性无关 / Galois 闭包 | 4 |
| 2017 | ALG Team | 3 | 极小非平凡正规子群 N ≅ L×…×L（L 单群） | group | 正规子群 / 特征子群 | 3 |
| 2017 | ALG Overall | 1 | 有限域阶 p^n；二次互反律；691 素数时 439 非二次剩余；x²+6x+1 双根的 p | ant | 二次互反律 / Legendre 符号 | 3 |
| 2017 | ALG Overall | 2 | GL_2(F_p) 中幺幂上三角子群是 Sylow p-子群并数其个数 | group/sylow | Sylow 定理 / 阶计算 | 3 |
| 2017 | ANA Individual | 1 | 单调递减权 g 下的加权平均不等式 ∫xfg/∫fg ≤ ∫xf/∫f | real/ineq | Chebyshev 积分不等式 | 2 |
| 2017 | ANA Individual | 2 | 闭集 E 的等距集 E_r={d(x,E)=r} 可测且测度为零 | real | 覆盖 / 测度论 | 2 |
| 2017 | ANA Individual | 3 | w=∫_0^w(1−x^n)^{−2/n}dx 是圆到正 n 边形的共形映射及其 Laplace 边值问题 | cplx/pde | Schwarz–Christoffel 公式 | 4 |
| 2017 | ANA Individual | 4 | 热方程初边值问题解的唯一性，并证明一致有界条件 (∗) 是必要的 | pde | 极大值原理 / 反例构造 | 3 |
| 2017 | ANA Individual | 5 | 可压缩流体方程组：能量泛函单调不增；v 关于 t 的上下界（含 v_0^{-γ} 的显式估计） | pde | 能量方法 / 熵估计 | 5 |
| 2017 | ANA Team | 1 | 球平均相等的两个测度：绝对连续时相等；一般不绝对连续时如何 | real | 测度论 / 微分定理 | 3 |
| 2017 | ANA Team | 2 | f:Ω→Ω 解析，f(z0)=z0 且 f′(z0)=1 ⟹ f=id | cplx | Schwarz 引理 | 3 |
| 2017 | ANA Team | 3 | 第一象限上 Δu=0, u>0, 边界为 0 的全部解 | pde | 调和函数 / Poisson 核 | 3 |
| 2017 | ANA Team | 4 | 理想流体方程组：∫|v|² 守恒；无旋且有非零梯度 ⟹ ∂P/∂n<0 | pde | 能量恒等式 / 涡度 / 自由边界 | 5 |
| 2017 | ANA Overall | 1 | 单位盘上全纯函数的 Schwarz–Pick 型双边估计 | cplx | Schwarz–Pick 不等式 | 3 |
| 2017 | ANA Overall | 2 | 凸函数满足 |f(x)|≤C(1+|x|)：f(x)/|x| 的极限、上界与下界 | real | 凸分析 / 渐近斜率 | 2 |
| 2017 | ANA Overall | 3 | Δu=x/(x²+y²) 于单位盘、u|∂=0：是否有弱解及最优连续性 | pde | 弱解 / 椭圆正则性 | 4 |
| 2018 | ALG Individual | 1 | 把 6x⁵+3x⁴−9x³+15x²−13x−2 分解为 Q[x] 中不可约因子 | poly | 有理根定理 / 模 p 不可约 | 2 |
| 2018 | ALG Individual | 2 | 证明 588 阶群可解（已知 12 阶群可解） | group/sylow | Sylow 定理 / 正规子群链 | 3 |
| 2018 | ALG Individual | 3 | 判定哪些域 F 使任意 n×n 矩阵都可上三角化 | linear/field | 特征多项式分裂 / 代数闭性 | 2 |
| 2018 | ALG Individual | 4 | 求 A↦A^tA 在 M_n(C) 与 M_n(R) 上的像 | linear | 半正定 Hermite / 谱分解 | 3 |
| 2018 | ALG Individual | 5 | k(x,y)/k(x^p,y^p) 的次数为 p²，且中间域有无穷多个 | field | 纯不可分扩张 / 模 p 独立 | 3 |
| 2018 | ALG Team | 1 | Σ1/d_i>1 时 x_1^{d_1}+…+x_n^{d_n} 在 F_p^n 上的零点数被 p 整除 | field/comb | Chevalley–Warning 定理 | 4 |
| 2018 | ALG Team | 2 | 有限群 G 作用 k[x_1,…,x_n]，不变量子环 S 有限生成 | comm/rep | Noether 有限性定理 | 3 |
| 2018 | ALG Team | 3 | R=k[[t]]，v_i 的像构成 M/tM 的基 ⟹ {v_i} 是 M 的基 | comm/homol | Nakayama 引理 | 3 |
| 2018 | ALG Team | 4 | dim{AX−XA} ≤ n²−deg μ(t)，等号 ⟺ μ 的次数为 n | linear | 交换子空间 / 极小多项式 | 4 |
| 2018 | ALG Overall | 1 | N=∏_{(i,n)=1}(1−ζ_n^i)：n 为素数幂时等于 p，否则等于 1 | ant | 分圆域 / 范数 / 单位 | 4 |
| 2018 | ALG Overall | 2 | GL_2(F) 的 B×B 双陪集恰两个轨道（对角与反交换），推广到 GL_n | linear/ag | Bruhat 分解 / 双陪集 | 3 |
| 2018 | ALG Overall | 3 | 描述所有可嵌入 M_n(Q) 的域扩张 K | comm/field | 中心单代数 / 分裂域 | 4 |
| 2018 | ALG Overall | 4 | X={V⊃E:dim V=m} 是否紧流形、维数几何、是否齐性空间 | ag | Grassmann 流形 / 齐性空间 | 3 |
| 2018 | ANA Individual | 1 | 图与锥不相交 ⟹ Lipschitz；Lipschitz 映射可延拓到全空间 | real | 几何测度 / McShane 延拓 | 3 |
| 2018 | ANA Individual | 2 | 不用 Riemann 映射定理证明单连通真域上存在单叶映到单位圆盘的函数 | cplx | 正规族 / Montel 定理 | 4 |
| 2018 | ANA Individual | 3 | n 次多项式满足 |P(0)| ≤ C∫_{−1}^{1}|P(x)|dx | approx | 多项式不等式 / Markov 型 | 3 |
| 2018 | ANA Individual | 4 | Δu+√u=0, u>0 in Ω, u|∂Ω=0 的解唯一 | pde | 极大值原理 / 单调性 | 4 |
| 2018 | ANA Individual | 5 | 算子 u(x)_j=Σ_k x_k/(j+k) 在 ℓ² 上的范数 ‖u‖=π | func/harm | Hilbert 矩阵 / 积分表示 | 4 |
| 2018 | ANA Team | 1 | 等周不等式与 Steiner 对称化：等周集是凸的；面积不变、周长不减；只有圆盘是等周集 | geom | Steiner 对称化 / Brunn–Minkowski | 4 |
| 2018 | ANA Team | 2 | 用 Hankel 围道积分表示 ζ(s) 并证明其亚纯延拓 | cplx | 围道积分 / 解析延拓 | 4 |
| 2018 | ANA Team | 3 | 轴对称热方程基本解的显式表达式（含函数 H(y)） | pde | 热核 / 分离变量 / Bessel | 5 |
| 2018 | ANA Team | 4 | 带近似法向场的 Korn 型不等式 | pde | Korn 不等式 / 分部积分 / 边界修正 | 5 |
| 2018 | ANA Overall | 1 | f 在单位圆盘邻域解析且在 ∂U 上取实值 ⟹ f 为常数 | cplx | Schwarz 反射 / 唯一性 | 2 |
| 2018 | ANA Overall | 2 | 求 −u″=f 在周期边值条件 u(0)=u(1), u′(0)=u′(1), ∫u=∫f=0 下的 Green 函数 | ode | Green 函数 / 周期边值 | 3 |
| 2018 | ANA Overall | 3 | Hardy 不等式 ∫|v|²/|x|² ≤ C∫(|v_r|²+R^{−2}v²) | harm/ineq | Hardy 不等式 / 径向导数 | 4 |
| 2019 | ALG Individual | 1 | GL(m,R) 中 g=k1 d k2（正交×正对角×正交） | linear | 极分解 / SVD | 2 |
| 2019 | ALG Individual | 2 | 首一不可约 P∈Q[X] 的根单；存在特征多项式为 P 的整数/有理矩阵 | linear/poly | 伴侣矩阵 / 结式 | 3 |
| 2019 | ALG Individual | 3 | 48 阶群不可能是单群 | group/sylow | Sylow 计数 / 单群判定 | 3 |
| 2019 | ALG Individual | 4 | Fibonacci 矩阵 A 在 Q、F2、F5 上的分裂域与半单性；lim f_n^{1/n}=黄金比 | linear/field | 分裂域 / 二次剩余 / 周期 | 3 |
| 2019 | ALG Individual | 5 | k 无限域、K/k 扩张：A,B 在 K 上相似 ⟹ 在 k 上相似 | linear | 有理标准形 / 域下降 | 2 |
| 2019 | ALG Team | 1 | (a) 有 p−2 实根 2 复根的 p 次不可约多项式的分裂域 Galois 群为 S_p；(b) X⁵−6X+3 的 Galois 群 | galois | Galois 群 / 传递群 | 4 |
| 2019 | ALG Team | 2 | 方程组的解集可写成单个多项式 P=0 的解集 | comm/ag | 理想 / Nullstellensatz / 乘积技巧 | 3 |
| 2019 | ALG Team | 3 | K[X] 上 v_0-赋值给出 ultrametric，K[[X]] 为其完备化，K 有限时紧 | valua | 非阿基米德度量 / 完备化 | 4 |
| 2019 | ALG Team | 4 | 同余数：nm²=ab(a+b)(a−b) 判别；r∈{1,2,3,5,6,7} 有无穷多 n≡r (mod 8) | ant/quad | 同余数问题 / 二次型 / 椭圆曲线 | 5 |
| 2019 | ALG Team | 5 | 投射模的 Schanuel 引理：K⊕P′ ≅ K′⊕P | homol | 投射模 / 拉回构造 | 3 |
| 2019 | ALG Overall | 1 | 构造有 p−2 个实根与 2 个复根的 p 次不可约多项式（P_k=kp²P_0+X^p−p） | poly | 摄动 / 一致收敛 / 实根计数 | 4 |
| 2019 | ALG Overall | 2 | L=k(x,y)（x²+y²=1）在 k 上的 Galois 群 | galois/field | 有理函数域 / 二次扩张 | 3 |
| 2019 | ALG Overall | 3 | 存在 u∈V* 稳定子平凡；φ_u:S(V)→C[G] 满射；忠实不可约表示嵌入 S^n(V) | rep | 不变量论 / 特征标 / 分裂域 | 4 |
| 2019 | ANA Individual | 1 | 投影 E,F 满足 ‖E−F‖≤1/2 ⟹ 存在酉 U 使 UEU*=F | func | 算子扰动 / 谱投影 | 3 |
| 2019 | ANA Individual | 2 | ∀f∈L¹, fg∈L¹ ⟹ g∈L^∞；并给出 ‖g‖_∞ 的对偶刻画 | real | 对偶 / 一致有界原理 | 3 |
| 2019 | ANA Individual | 3 | 穿孔圆盘上调和函数的圆周平均等于 α log r + β | potential | 调和函数 / 平均值性质 | 3 |
| 2019 | ANA Individual | 4 | (0,1)×(0,∞) 上 Δu=0, u>0, u|∂D=0 的全部解 | pde | 调和函数 / 极大值原理 | 4 |
| 2019 | ANA Individual | 5 | Legendre 多项式：正交性、实单根、Gauss 求积节点与 L² 最佳逼近 | approx | 正交多项式 / Gauss–Legendre 求积 | 3 |
| 2019 | ANA Team | 1 | R¹×[0,1] 上有界凸函数（可不光滑）不依赖 x | real | 凸分析 / 单调性 | 3 |
| 2019 | ANA Team | 2 | 帐篷映射存在轨道在 [0,1] 中稠密的点 | dyn | 符号动力学 / 二进制展开 | 2 |
| 2019 | ANA Team | 3 | Burgers 方程：一致有界、周期性、∂_x u ≤ 1/t、全变差一致有界、ε→0 的收敛 | pde | 极大值原理 / 守恒律 / BV 估计 | 5 |
| 2019 | ANA Team | 4 | 上半圆盘上 Δu=0, u>0, 边界为 0 的全部解 | pde | 调和函数 / 极大值原理 | 3 |
| 2019 | ANA Overall | 1 | f(x,y) 限制到每条直线上连续是否推出 f 连续 | real | 多元连续性 / 反例构造 | 2 |
| 2019 | ANA Overall | 2 | 证明 π²/sin²(πz) = Σ_{n∈Z} 1/(z−n)² | cplx | 部分分式 / Mittag-Leffler | 3 |
| 2019 | ANA Overall | 3 | Δu=cos(xy)/√(x²+y²) 于单位盘、u|∂=0：解的意义与经典解成立范围 | pde | 弱解 / 奇性 | 3 |
| 2020 | ALG Individual | 1 | R={f∈C[x]:f′(0)=0} 是否为有限生成 C-代数 | comm | 不变量子环 / 有限生成性 | 3 |
| 2020 | ALG Individual | 2 | exp 把幂零矩阵一一映到幺幂矩阵；逆的描述与 exp 的像 | linear | 矩阵指数 / Jordan 形 | 3 |
| 2020 | ALG Individual | 3 | Gauss 和 G_d=Σ_{x∈F_p}ζ_p^{x^d} 在 Q 上的次数等于 (d,p−1) | ant | 分圆域 / 特征和 | 4 |
| 2020 | ALG Individual | 4 | A_ij=ζ^{ij}−ζ^{(i−1)j}：det(A)²∈Z，且 d≡0,3 (mod 4) 时 det(A)∉Z | ant/linear | Vandermonde 型行列式 / 分圆整数 | 4 |
| 2020 | ALG Individual | 5 | 特征 ≠2 的域上奇数阶正交矩阵有特征值 det(M) | linear | 正交群 / 行列式 | 2 |
| 2020 | ALG Individual | 6 | GL_n(Z) 的有限子群阶数存在仅依赖 n 的一致上界 c_n | group/rep | Minkowski 界 / 平均技巧 | 3 |
| 2020 | ALG Overall | 1 | 任何有限阿贝尔群都是 Q 的某个 Galois 扩张的 Galois 群；非阿贝尔例子 | ant/galois | Kronecker–Weber / 逆 Galois 问题 | 3 |
| 2020 | ALG Overall | 2 | SL_2(F_p) 的阶、Sylow p-子群个数、M_{a,b} 共轭类判定与个数 | group/sylow | Sylow 定理 / 共轭类 | 4 |
| 2020 | ANA Individual | 1 | |f′|≥β ⟹ m{|f|≤ε} ≤ 2ε/β；q 阶导数的相应估计 | real | Lebesgue 测度 / 覆盖论证 | 3 |
| 2020 | ANA Individual | 2 | 截断指数 E_p(z) 满足 |1−E_p(z)| ≤ |z|^{p+1} (|z|≤1) | cplx | 幂级数余项估计 | 2 |
| 2020 | ANA Individual | 3 | 用初等积分求解 x dy/dx = √(x⁶−y²) + 3y | ode | Riccati 型 / 变量替换 | 3 |
| 2020 | ANA Individual | 4 | 非降函数 f′ 可积且 ∫f′ ≤ f(1)−f(0)；级数可逐项求导 a.e. | real | 单调函数 / Vitali 覆盖 | 3 |
| 2020 | ANA Individual | 5 | f(0)=0, |f(e^{iθ})|≥3 ⟹ 1−f 在单位盘内零点的乘积模 < 1/2 | cplx | Jensen 公式 / 零点估计 | 4 |
| 2020 | ANA Individual | 6 | Σa_ij u_ij − u ≥ 0 且 u ≤ 2020+|x|^{2020} ⟹ u ≤ 0 | pde | 极大值原理 / 一致椭圆 | 3 |
| 2020 | ANA Overall | 1 | 用十进制构造实数：有界递增十进制序列有十进制极限 | real | 实数构造 / 完备性 | 3 |
| 2020 | ANA Overall | 2 | Σx_ix_j f_{ij}=0 且 ∇f(0)=0 ⟹ f 常数；旋转不变 ⟹ 球面上常数 | pde | 极值原理 / 齐次函数 | 3 |
| 2021 | ALG Individual | 1 | Q_p(ζ_{p^n}) 的范数映射 N_{L/Q_p}(L^×) 的像 | padic/ant | 局部域 / 类域论 / log-exp | 5 |
| 2021 | ALG Individual | 2 | φ:GL(V)→GL(∧²V) 的核与 det(∧²f)=det(f)^{n−1} | linear/rep | 外幂 / 初等矩阵 | 3 |
| 2021 | ALG Individual | 3 | 分类 Z⁵/AZ³（A 为 5×3 秩 2 整矩阵） | homol/linear | Smith 标准形 / 有限生成模 | 3 |
| 2021 | ALG Overall | 1 | 上三角矩阵代数 A 的所有单模有限维且恰为 n 个一维模 | rep/homol | Jacobson 根 / Schur 引理 | 3 |
| 2021 | ALG Overall | 2 | Euler 定理：p=x²+3y² 有解 ⟺ p=3 或 p≡1 (mod 3) | ant/quad | 二次互反 / Z[ω] 的 PID 性 | 3 |
| 2021 | ANA Individual | 1 | l²(Z)→l⁴(Z) 嵌入是否连续、是否紧、是否模平移紧 | func | 紧算子 / 平移不变性 | 4 |
| 2021 | ANA Individual | 2 | 凸开集的投影长度（或投影集）相同能否推出两凸集相同 | real/geom | 凸几何 / Radon 变换 | 3 |
| 2021 | ANA Individual | 3 | ∇(ρ^{4/3})+ρ∇φ=0（φ 为 Newton 势）时积分 ∫(3ρ^{4/3}+ρφ/2) 的值 | pde | Thomas–Fermi 方程 / 变分恒等式 | 5 |
| 2021 | ANA Individual | 4* | 确定单位圆盘的全纯自同构群 Aut(D)（选做） | cplx | Schwarz 引理 / Möbius 变换 | 2 |
| 2021 | ANA Individual | 5* | 内积空间中 x_k ⇀ x ⟹ 存在子列其 Cesàro 平均强收敛到 x（选做） | func | Banach–Saks 性质 | 3 |
| 2021 | ANA Overall | 1 | 解释 L^∞(R) 的对偶空间不是 L^1(R) | func | 对偶 / 测度表示 | 2 |
| 2021 | ANA Overall | 2 | G(t)=∫|φ(x)−t|dx 连续；在 t 可导 ⟺ λ({φ=t})=0 | real | Lebesgue 积分 / 可导性 | 3 |
| 2021 | ANA Overall | 3 | ∫_{B}|v|²/|x|² ≤ C(∫|v_r|² + ∫_{∂B}|v|²)（迹不等式） | harm | Hardy / 迹定理 | 4 |
| 2021 | ANA Overall | 4 | 方程 dy/dx=x²+y² 的任何解生命期有限 | ode | 比较定理 / 爆破 | 2 |
| 2022 | ALG Individual | 1 | 求所有满足 σ(AB)=σ(BA) 且 σ(I)=n 的 C-线性泛函 σ | linear | 迹的唯一性 / 交换子空间 | 3 |
| 2022 | ALG Individual | 2 | p 进域 O_F 中元素表为平方和：p≠2 三个平方，Q_2 四个平方 | padic/quad | 局部域 / Hilbert 符号 | 4 |
| 2022 | ALG Individual | 3 | R=∏_p F_p：存在极大理想使商域特征 0 且 −1 非平方；不存在 R/n↪R | comm/field | 超积 / Artin–Schreier / 形式实域 | 4 |
| 2022 | ALG Overall | 1 | C[x,y]/(x²+y²−1) 是 UFD，而 R[x,y]/(x²+y²−1) 不是 | comm/ag | 唯一分解 / 类群 / 实点 | 4 |
| 2022 | ALG Overall | 2 | f=x³−x−1：f 在 F_p 恰一根 ⟺ (p/23)=−1；求分裂中 e,f,g | ant/galois | 三次域判别式 / 分裂类型 | 4 |
| 2022 | ANA Individual | 1 | f_k ⇀ f in L^q 且 f_k→f a.e. ⟹ lim(‖f_k‖−‖f_k−f‖)=‖f‖ | real | Brezis–Lieb 引理 | 3 |
| 2022 | ANA Individual | 2 | 按 f′(z0)=sup_{g∈F}|g′(z0)| 的策略详细解释 Riemann 映射定理的证明 | cplx | 正规族 / 极值函数 | 4 |
| 2022 | ANA Individual | 3 | u_t=u_xx/u_x² 且 u_x>0：找一个变换把该非线性热方程化为线性 PDE | pde | Hopf–Cole 型变换 / 拟线性化 | 3 |
| 2022 | ANA Individual | 4 | 变系数线性波动方程的能量估计（含 Σ‖∂g_{αβ}‖_{L²} 的指数因子） | pde/wave | 能量方法 / Gronwall 不等式 | 4 |
| 2022 | ANA Overall | 1 | 非常数整函数的像是稠密的，且最多漏掉一个点 | cplx | Picard 小定理 / 正规族 | 3 |
| 2022 | ANA Overall | 2 | 积分算子 T 的有界性（Schur 检验）、Hilbert–Schmidt 紧性、弱奇异核的紧性 | func | Schur 检验 / Arzelà–Ascoli | 4 |
| 2022 | ANA Overall | 3 | 3 维波动方程径向解：∂_r(rφ)(0,t)≡0 (t≥T0)；在 u=t−r 坐标下的非零极限 | pde/wave | 球平均法 / 降维 | 5 |
| 2023 | ALG Individual | 1 | (1) 数 (Z/pZ)^n 的 p^k 阶子群个数；(2) 分类 Z⁵/AZ^n（二选一） | group/linear | 子群格 / Smith 标准形 | 3 |
| 2023 | ALG Individual | 2 | n 个两两交换的幂零自同态之复合 u_1∘…∘u_n 的性质 | linear | 同时三角化 / 幂零性 | 3 |
| 2023 | ALG Individual | 3 | 证明 dim V^G=(1/|G|)Σχ(g) 与 Molien 公式 Σdim(S^G∩S_d)t^d | rep/comm | 特征标平均 / 不变量环 | 3 |
| 2023 | ALG Team | 1 | Q/Z 中阶为 n 的子群唯一 | group | 可除群 / 挠子群 | 2 |
| 2023 | ALG Team | 2 | S_k(d)=Σ_{x∈F_{p^k}}ζ_p^{Tr_k(x^d)}∈Z（d | (p^k−1)/(p−1)） | field/ant | 特征和 / 迹映射 / Gauss 和 | 5 |
| 2023 | ALG Overall | 1 | 把 Z[x1,x2,x3]/(x1x2+x3²−2) 写成系数全为 1、次数≤2 的平方自由多项式商；一般情形？ | comm/ag | Gröbner 基 / 二次型配方 | 3 |
| 2023 | ANA Individual | 1 | Schwartz 函数的不确定性原理 ∫x²|ψ|²·∫|ψ′|² ≥ 1/4，等号 ⟺ 高斯 | harm | Fourier 变换 / 分部积分 / Cauchy–Schwarz | 3 |
| 2023 | ANA Individual | 2 | f 在闭盘邻域除单位圆上极点 z0 外全纯 ⟹ lim a_n/a_{n+1}=z0 | cplx | 奇点展开 / 系数比 | 3 |
| 2023 | ANA Individual | 3 | 平面系统 ẋ=xy+x³, ẏ=−y−2x² 在 (0,0) 的稳定性 | ode/dyn | 线性化 / Lyapunov 函数 | 3 |
| 2023 | ANA Individual | 4 | {y>x²} 上有界调和函数且边界值为 0 ⟹ 恒为 0 | pde | 极大值原理 / 无界域 Liouville | 3 |
| 2023 | ANA Team | 1 | 两个椭圆曲线之间的全纯映射必为 f(z)=az+b | cplx | Liouville / 双周期性 | 4 |
| 2023 | ANA Team | 2 | 有界自伴算子谱非空；无界自伴算子谱是否非空 | func | 谱定理 / 近似点谱 | 3 |
| 2023 | ANA Team | 3 | (−Δ+|x|²)g_n=f_n 且 f_n 在 L² 有界 ⟹ g_n 有界且有 L² 收敛子列 | func/pde | 谐振子 / 紧预解 / Rellich | 4 |
| 2023 | ANA Overall | 1 | 卷积算子 Tf=f∗φ 是否把 L³(R³) 有界映到 L²(R³) | harm | Young 不等式 / 齐次性检验 | 4 |
| 2023 | ANA Overall | 2 | 给定单位盘内离散点列，构造以该点列为零点集的全纯函数 | cplx | Weierstrass 乘积 / Blaschke 因子 | 3 |
| 2024 | ALG Individual | 1 | H≤G，(|H|,[N_G(H):H])=1 ⟹ N_G(H)=N_G(N_G(H)) | group | Burnside 正规 p-补 / Frattini 论证 | 4 |
| 2024 | ALG Individual | 2 | F-开集是否总构成 F̄^n 上的拓扑 | ag | Zariski 拓扑 / 下降 | 4 |
| 2024 | ALG Individual | 3 | 关系 a_ib_j±b_ja_i=δ_ij 生成的代数的单模分类（Clifford / Weyl 代数） | rep/comm | Clifford 代数 / Weyl 代数 / Schur 引理 | 4 |
| 2024 | ALG Individual | 4 | A=C[t,t^{−1}]，γ:f(t)↦f(−1/t) 的不动子环 R 及其性质 | comm | 不变量 / UFD 与 PID | 4 |
| 2024 | ALG Team | 1 | 求所有满足 A^T−I=A+A^{−1} 的可对角化可逆实特征值矩阵 | linear | 矩阵方程 / 谱 | 3 |
| 2024 | ALG Team | 2 | P+Q=R 互素 ⟹ deg R < deg rad(PQR) | poly/ant | Mason–Stothers（多项式 abc） | 4 |
| 2024 | ALG Team | 3 | Ẑ 的子群开 ⟺ 有限指数；∏_N Z/pZ 是否同样成立 | group | 射有限群 / 拓扑群 | 4 |
| 2024 | ALG Overall | 1 | G 是 p-群 ⟺ 每个非零 k-表示（char k=p）有非零不动点 | rep | 模表示 / 不动点函子 | 3 |
| 2024 | ALG Overall | 2 | 构造微分同胚 GL_3(R)→O(3)×R⁶，并给出 GL_n(C) 的类比 | linear | 极分解 / QR 分解 | 3 |
| 2024 | ANA Individual | 1 | 保向光滑映射的 Beltrami 系数 μ=|φ_z̄|/|φ_z|<1；圆映为椭圆且 μ 为轴比 | cplx | 拟共形映射 / 椭圆模 | 3 |
| 2024 | ANA Individual | 2 | 热方程 Cauchy 问题在 t=1/1000 是否有零点、能否在 t=1 复现方波；波动方程 t=1000 时是否有零点 | pde | 热核 / 有限传播速度 | 4 |
| 2024 | ANA Individual | 3 | Δu=0 于穿孔球 B−{0}, u>0, u|∂B=v|∂B, Δv=0 于 B ⟹ u≥v | pde | 调和函数 / 可去奇点 / 比较原理 | 4 |
| 2024 | ANA Individual | 4 | lim_{λ→∞}∫e^{iλx²}φ(x)dx=0 且 |∫e^{iλx²}φ| ≤ Cλ^{−α} | harm | 驻相法 / 振荡积分 | 3 |
| 2024 | ANA Team | 1 | 半空间波动方程的混合问题：M 为一阶传输算子，证 □(Mu)=0 并求 u | pde/wave | 半空间反射 / 传输方程 | 5 |
| 2024 | ANA Team | 2 | A≥B≥0 的两自伴算子，存在压缩算子 T 使 B=T*AT | func | Löwner 定理 / 算子单调性 | 3 |
| 2024 | ANA Team | 3 | 上半平面 ∫_H y^{k−2}|f| < ∞ ⟹ y^k f 有界 | cplx | Bergman 空间 / 次调和函数 | 4 |
| 2024 | ANA Overall | 1 | u 关于每个变量 1-周期 ⟹ ∫_{[0,1]²}det(D²u+A) = det A | pde | 弱收敛 / 行列式的散度结构 | 4 |
| 2024 | ANA Overall | 2 | σ(AB)=σ(BA)；A,B 不可逆时结论如何 | func | 谱理论 / 交换性 | 2 |
| 2025 | ALG Individual | 1 | GL_n(R) 共轭作用在对角矩阵上的轨道是闭集 | linear/ag | 轨道闭性 / 特征多项式 | 3 |
| 2025 | ALG Individual | 2 | 有限阿贝尔群范畴既无足够投射也无足够内射对象 | homol/cat | 范畴论 / 可除群 | 3 |
| 2025 | ALG Individual | 3 | |G|=n ⟹ |Aut(G)| ≤ n^{log_2 n} | group | 生成元个数 / 次正规列 | 3 |
| 2025 | ALG Individual | 4 | 平方和层次 l(K)：证明 l(K)=l(K(t)) 并计算两个数域的值 | quad/field | 二次型 / 形式实域 / 域扩张 | 4 |
| 2025 | ALG Team | 1 | 秩 k 矩阵循环延拓的指标函数 f_A 是双射，且 Σf_A(i)=C(n+1,2)+kn | linear/comb | 组合恒等式 / 生成集 | 4 |
| 2025 | ALG Team | 2 | X⁴+9 与 X⁸+9 在 Q_3 上不可约；X⁸+9 分裂域的次数 | padic | Eisenstein / 局部域分歧 | 4 |
| 2025 | ALG Team | 3 | GL_n(Z) 在同构意义下只有有限多个有限子群 | group | Minkowski / 有界阶 | 3 |
| 2025 | ALG Overall | 1 | 非阿贝尔有限 p-群满足 [G:G′] ≥ p² | group | 交换子群 / p-群中心 | 3 |
| 2025 | ALG Overall | 2 | 对称双线性型 B 与单 Jordan 块幂零算子 T 满足 B(Tv,w)=−B(v,Tw) ⟹ n 为奇数 | linear | 辛结构 / Jordan 形 | 4 |
| 2025 | ANA Individual | 1 | {nα} 在 [a,b] 中的频率收敛到 b−a（Weyl 等分布） | ergodic | 等分布 / 三角和估计 | 3 |
| 2025 | ANA Individual | 2 | 第一象限上有界全纯函数在边界模约束下满足 |f(x+iy)| ≤ 2^{(2/π)arctan(1/(2xy))} | cplx | Phragmén–Lindelöf / 调和测度 | 5 |
| 2025 | ANA Individual | 3 | V 是 L²([0,1]) 的闭子空间且 V⊂C([0,1]) ⟹ dim V < ∞ | func | 紧嵌入 / 一致有界 | 3 |
| 2025 | ANA Individual | 4 | Δ²u=0 且 u≥0 于 R^n ⟹ u=Σa_i(x_i−b_i)²+a_0 | pde | 双调和 Liouville 定理 | 4 |
| 2025 | ANA Team | 1 | 用网格地址系统给出 [0,1]² 上函数的组合逼近，误差 ≤ 6.01/7‖f‖（宣称是 AI 的数学基础） | approx | 分片线性逼近 / 覆盖论证 | 4 |
| 2025 | ANA Team | 2 | Banach 空间上 L_t=(1−t)L_0+tL_1 满足 ‖x‖≤C‖L_tx‖ ⟹ L_0,L_1 满射性等价 | func | 开映射定理 / 同伦方法 | 3 |
| 2025 | ANA Team | 3 | Δu=f, u=g on Γ, ∂u/∂n=0 on Γ 的混合边值问题至多一解 | pde | 能量方法 / 唯一性 | 3 |
| 2025 | ANA Overall | 1 | ∫|f|max{1,log|f|} < ∞ ⟹ 极大函数 ∫Mf < ∞ | harm | Hardy–Littlewood 极大函数 / 分布函数 | 3 |
| 2025 | ANA Overall | 2 | 环面上线性 Schrödinger 方程的 Strichartz 型估计 ∫∫|u|⁴ ≤ C(∫|f|²)² | harm/pde | Fourier 级数 / Plancherel / Strichartz | 4 |

### 2.2 恢复集（7 卷 / 29 题，源为 .doc/.docx）

> 全部题面来自 Word 文本层；数学公式在源文件中是 OLE 公式对象，本环境（禁止安装任何库）无法取出，
> 故题面只保留可读的文字骨架，标注「公式缺失」的行请勿直接引用公式。

| 年份 | 卷别 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|---|
| 2012 | ANA Individual | 1 | 初边值问题的分离变量求解：解族构成正交基且完备、唯一性 | pde | Sturm–Liouville / 分离变量 | 3 |
| 2012 | ANA Individual | 2 | 整函数的迭代：若存在某常数使某不等式对所有 n 成立，则……（题面残缺） | cplx | 迭代 / 正规族 | — |
| 2012 | ANA Individual | 3 | 若 f 限制到平面每条直线上连续，f 是否必连续？光滑性同问？ | real | 多元连续性 / 反例 | 2 |
| 2013 | ANA Individual | 1 | R¹×[0,1] 上非光滑有界凸函数与 x 无关 | real | 凸分析 | 3 |
| 2013 | ANA Individual | 2 | 性质 f(1/n)=1/n³+e^{−2n}：不存在单位盘内解析 f 满足之；但存在 0<|z|<1 上解析 g 满足；能否使 f 永不为整数 | cplx | 解析延拓 / 唯一性定理 | 4 |
| 2013 | ANA Individual | 3 | L¹(E) 中 fg∈L¹(E) ⟹ 存在零测集 F 使 g∈L^∞(E\F)；并给出 ‖g‖_∞ 的上确界刻画 | real | 对偶 / 一致有界 | 3 |
| 2013 | ANA Individual | 4 | Poincaré 不等式：(a) C¹[−1,1] 上 ∫(f−平均)² ≤ C∫|f′|²；(b) C¹(B1)（B1⊂R²）上同型估计 | real/ineq | Poincaré 不等式 | 3 |
| 2013 | ANA Team | 1 | Fourier 部分和 u_n 在单位圆盘紧子集一致收敛到调和函数；∫_D(u_x²+u_y²)=πΣn(a_n²+b_n²)；Hölder 类 α∈(1/2,1) 时 Σ(a_n²+b_n²) ≤ C|f|_{C^α}² | harm | Poisson 积分 / Dirichlet 能量 / Hölder 估计 | 4 |
| 2013 | ANA Team | 2 | （源文件中该题无内容：仅 “Problem 2” 标题） | — | — | — |
| 2013 | ANA Team | 3 | ∂_t u−Δu=u² 于 B1，Neumann 边界：比较原理；常值解 u≡a；u0>0 时解在有限时刻爆破 | pde | 比较原理 / 爆破 | 5 |
| 2013 | ANA Team | 4 | f≥0 单调下降且 ∫_{x−a}^x f ≤ (5/4)∫_x^{x+a} f ⟹ f∈L^p(0,1) 对 1≤p< log2/(log3−log2) | real/ineq | L^p 提升 / 权重估计 | 5 |
| 2013 | ANA Overall | 1 | 调和函数的平均值性质、Harnack 不等式与最大值原理 | potential | 平均值性质 / Harnack / 极值原理 | 3 |
| 2013 | ANA Overall | 2 | φ(z)=λz+az²+…（a≠0）：构造近恒等解析 f 使 φ∘f = f∘(λz+O(z³))；λ>1 时能否线性化 φ∘f=f∘(λz) | cplx | Schröder 线性化 / 共轭方程 | 5 |
| 2014 | ALG Team | 1 | 求 C[x,y] 中在线性变换 α:(x,y)↦(−x,x+y) 与 β:(x,y)↦(x+y,−y) 下不变的多项式 | rep/comm | 不变量论 / 有限群作用 | 3 |
| 2014 | ALG Team | 2 | φ(u)=1+u+u²/2!+…+u^n/n! 给出“特征值全 0”与“特征值全 1”矩阵集之间的双射；n=2m 时由 A J + J A^t=0 推出 φ(A) J φ(A)^t=I | linear | 矩阵指数 / 幂零与幺幂 | 4 |
| 2014 | ALG Team | 3 | 解 x²−2y²=7（x,y∈Z）；并判定哪些整数 n 使 x²−2y²=n 可解 | ant/quad | Pell 方程 / 二次型 | 3 |
| 2014 | ALG Team | 4 | 有限群 G 的换位子群是 p-群，char R=p>0 的代数闭域上不可约 G-模必为 1 维 | rep | 模表示 / Clifford 定理 | 4 |
| 2014 | ANA Individual | 1 | 求 C、单位圆盘 D、Riemann 球面 Ĉ 的共形自同构群并证明 | cplx | Möbius 变换 / Aut(D) | 3 |
| 2014 | ANA Individual | 2 | 单位圆盘上收敛幂级数：证明 Schwarz 引理（|f(z)|≤|z| 与 |f′(0)|≤1） | cplx | Schwarz 引理 | 2 |
| 2014 | ANA Individual | 3 | 设（内容丢失）… 对素数全体证明级数发散 | real | 级数发散 | — |
| 2014 | ANA Individual | 4 | 区间上连续实值函数不可能是二到一的映射 | real | 连续映射 / 中值定理 | 3 |
| 2014 | ANA Individual | 5 | （a)(b) 两小问，题面公式丢失） | — | — | — |
| 2014 | ANA Individual | 6 | Burgers 方程：a) 初值满足某条件时存在整体解；b) 另一条件下存在爆破时刻 T | pde | Burgers / 整体解与爆破 | 5 |
| 2014 | ANA Team | 1 | f(z)=z² 的迭代：|z|<1 时趋于 0、|z|>1 时趋于 ∞；对 g(z)=z²−2 求所有 g^n(z)→∞ 的点 | dyn | 迭代 / Chebyshev 共轭 | 4 |
| 2014 | ANA Team | 2 | 求 A={z: 0<arg z<π/2, 0<|z|<1} 到单位圆盘的共形映射 | cplx | 共形映射 / 幂函数 | 3 |
| 2014 | ANA Team | 3 | 周期 2 连续函数的 Fourier 级数：部分和一致收敛到调和函数；∫_D(u_x²+u_y²)=πΣn(a_n²+b_n²) | harm | Poisson 积分 / Dirichlet 能量 | 4 |
| 2014 | ANA Team | 4 | 非减非负 ω 满足 ω(γR)≤ηω(R)+KR^α ⟹ ω(R) ≤ C(R/R0)^βω(R0)+CKR^α（迭代引理） | harm/ineq | 迭代引理 / Campanato | 4 |
| 2014 | ANA Team | 5 | l^∞(N) 上 f_n=e^{2πinθ}：值域在单位圆周稠密；{f_n,1} 生成的闭自伴子代数的极大理想空间同胚于单位圆周 | func | Gelfand 理论 / 极大理想空间 | 5 |
| 2014 | ANA Team | 6 | 证明 Σ_{n≥1} 1/n² = π²/6 | real | Fourier 级数 / Parseval | 3 |

### 2.3 逐卷规模与文字量（PDF 主集）

| 年份 | 科目 | 卷别 | 题数 | 抽取字符 | 英文词 | 词/题 | 难度均值 |
|---|---|---|---|---|---|---|---|
| 2012 | ALG | Individual | 3 | 378 | 83 | 27.7 | 2.67 |
| 2012 | ALG | Team | 2 | 687 | 140 | 70.0 | 2.50 |
| 2012 | ALG | Overall | 1 | 278 | 50 | 50.0 | 4.00 |
| 2013 | ALG | Individual | 3 | 1519 | 281 | 93.7 | 3.67 |
| 2013 | ALG | Team | 2 | 779 | 169 | 84.5 | 3.00 |
| 2014 | ALG | Individual | 3 | 583 | 100 | 33.3 | 3.00 |
| 2015 | ALG | Individual | 3 | 407 | 75 | 25.0 | 2.67 |
| 2015 | ALG | Team | 3 | 717 | 130 | 43.3 | 3.67 |
| 2015 | ALG | Overall | 2 | 16 | 1 | 0.5 | 3.00 |
| 2015 | ANA | Individual | 4 | 732 | 120 | 30.0 | 3.00 |
| 2015 | ANA | Team | 3 | 636 | 127 | 42.3 | 3.33 |
| 2015 | ANA | Overall | 2 | 556 | 106 | 53.0 | 3.00 |
| 2016 | ALG | Individual | 3 | 734 | 139 | 46.3 | 2.67 |
| 2016 | ALG | Team | 3 | 1071 | 203 | 67.7 | 3.33 |
| 2016 | ALG | Overall | 1 | 440 | 87 | 87.0 | 4.00 |
| 2016 | ANA | Individual | 6 | 1122 | 191 | 31.8 | 2.83 |
| 2016 | ANA | Team | 6 | 1242 | 227 | 37.8 | 2.83 |
| 2016 | ANA | Overall | 2 | 734 | 130 | 65.0 | 3.50 |
| 2017 | ALG | Individual | 3 | 815 | 132 | 44.0 | 3.33 |
| 2017 | ALG | Team | 3 | 654 | 116 | 38.7 | 3.33 |
| 2017 | ALG | Overall | 2 | 605 | 107 | 53.5 | 3.00 |
| 2017 | ANA | Individual | 5 | 1682 | 295 | 59.0 | 3.20 |
| 2017 | ANA | Team | 4 | 1589 | 292 | 73.0 | 3.50 |
| 2017 | ANA | Overall | 3 | 713 | 127 | 42.3 | 3.00 |
| 2018 | ALG | Individual | 5 | 1137 | 205 | 41.0 | 2.60 |
| 2018 | ALG | Team | 4 | 1288 | 240 | 60.0 | 3.50 |
| 2018 | ALG | Overall | 4 | 1528 | 285 | 71.2 | 3.50 |
| 2018 | ANA | Individual | 5 | 2071 | 391 | 78.2 | 3.60 |
| 2018 | ANA | Team | 4 | 2690 | 495 | 123.8 | 4.50 |
| 2018 | ANA | Overall | 3 | 616 | 106 | 35.3 | 3.00 |
| 2019 | ALG | Individual | 5 | 1666 | 319 | 63.8 | 2.60 |
| 2019 | ALG | Team | 5 | 2683 | 521 | 104.2 | 3.80 |
| 2019 | ALG | Overall | 3 | 1361 | 256 | 85.3 | 3.67 |
| 2019 | ANA | Individual | 5 | 1544 | 291 | 58.2 | 3.20 |
| 2019 | ANA | Team | 4 | 1247 | 227 | 56.8 | 3.25 |
| 2019 | ANA | Overall | 3 | 413 | 70 | 23.3 | 2.67 |
| 2020 | ALG | Individual | 6 | 1738 | 357 | 59.5 | 3.17 |
| 2020 | ALG | Overall | 2 | 731 | 143 | 71.5 | 3.50 |
| 2020 | ANA | Individual | 6 | 936 | 162 | 27.0 | 3.00 |
| 2020 | ANA | Overall | 2 | 648 | 110 | 55.0 | 3.00 |
| 2021 | ALG | Individual | 3 | 4063 | 783 | 261.0 | 3.67 |
| 2021 | ALG | Overall | 2 | 2740 | 485 | 242.5 | 3.00 |
| 2021 | ANA | Individual | 5 | 1539 | 295 | 59.0 | 3.40 |
| 2021 | ANA | Overall | 4 | 869 | 167 | 41.8 | 2.75 |
| 2022 | ALG | Individual | 3 | 865 | 166 | 55.3 | 3.67 |
| 2022 | ALG | Overall | 2 | 557 | 102 | 51.0 | 4.00 |
| 2022 | ANA | Individual | 4 | 1378 | 237 | 59.2 | 3.50 |
| 2022 | ANA | Overall | 3 | 1570 | 300 | 100.0 | 4.00 |
| 2023 | ALG | Individual | 3 | 1077 | 192 | 64.0 | 3.00 |
| 2023 | ALG | Team | 2 | 534 | 99 | 49.5 | 3.50 |
| 2023 | ALG | Overall | 1 | 551 | 90 | 90.0 | 3.00 |
| 2023 | ANA | Individual | 4 | 926 | 156 | 39.0 | 3.00 |
| 2023 | ANA | Team | 3 | 970 | 169 | 56.3 | 3.67 |
| 2023 | ANA | Overall | 2 | 584 | 102 | 51.0 | 3.50 |
| 2024 | ALG | Individual | 4 | 976 | 189 | 47.2 | 4.00 |
| 2024 | ALG | Team | 3 | 831 | 148 | 49.3 | 3.67 |
| 2024 | ALG | Overall | 2 | 401 | 66 | 33.0 | 3.00 |
| 2024 | ANA | Individual | 4 | 1768 | 323 | 80.8 | 3.50 |
| 2024 | ANA | Team | 3 | 1219 | 230 | 76.7 | 4.00 |
| 2024 | ANA | Overall | 2 | 383 | 70 | 35.0 | 3.00 |
| 2025 | ALG | Individual | 4 | 915 | 172 | 43.0 | 3.25 |
| 2025 | ALG | Team | 3 | 917 | 174 | 58.0 | 3.67 |
| 2025 | ALG | Overall | 2 | 412 | 78 | 39.0 | 3.50 |
| 2025 | ANA | Individual | 4 | 999 | 169 | 42.2 | 3.75 |
| 2025 | ANA | Team | 3 | 2154 | 379 | 126.3 | 3.33 |
| 2025 | ANA | Overall | 2 | 845 | 156 | 78.0 | 3.50 |

> 注 1：2021 ALG Individual（261 词/题）与 2021 ALG Overall（243 词/题）原卷**附带官方解答**，词数被解答抬高。
> 注 2：2015 三卷（ALG Ind/Team/Ov）为中文卷或图片卷，英文词数为 0，会拉低 ALG 平均词数。

---

## 3. 考点频次表

### 3.1 子领域标签定义与频次（244 题；主集=PDF，恢复=.doc/.docx）

ALG 侧：`linear` 线性代数/矩阵；`comm` 交换代数与环；`ant` 代数数论；`rep` 表示论；`group` 群论；
`field` 域论；`galois` Galois 理论；`ag` 代数几何；`poly` 多项式；`quad` 二次型/平方和；
`homol` 同调代数与模；`sylow` Sylow 与有限群结构；`padic` p 进与局部域；`cat` 范畴论；`comb` 组合；`valua` 赋值论。

ANA 侧：`pde` 偏微分方程；`real` 实分析/测度；`cplx` 复分析；`harm` 调和分析与 Fourier；
`func` 泛函分析与算子；`ode` 常微分方程；`ineq` 不等式；`potential` 位势/调和函数；
`approx` 逼近与正交多项式；`dyn` 动力系统；`geom` 几何测度；`wave` 波动/色散；
`ergodic` 遍历论；`special` 特殊函数。

| 考点 | 题次 | 主集 | 恢复 | ALG | ANA | 出现年份(20xx) |
|---|---|---|---|---|---|---|
| `linear` | 33 | 32 | 1 | 32 | 1 | 12,13,14,15,16,18,19,20,21,22,23,24,25 |
| `pde` | 33 | 30 | 3 | 0 | 33 | 12,13,14,16,17,18,19,20,21,22,23,24,25 |
| `real` | 30 | 22 | 8 | 0 | 30 | 12,13,14,15,16,17,18,19,20,21,22 |
| `cplx` | 28 | 22 | 6 | 0 | 28 | 12,13,14,15,16,17,18,19,20,21,22,23,24,25 |
| `comm` | 18 | 17 | 1 | 18 | 0 | 12,13,14,15,16,17,18,19,20,22,23,24 |
| `ant` | 18 | 17 | 1 | 18 | 0 | 13,14,15,16,17,18,19,20,21,22,23,24 |
| `rep` | 16 | 14 | 2 | 16 | 0 | 12,13,14,16,17,18,19,20,21,23,24 |
| `harm` | 16 | 13 | 3 | 1 | 15 | 12,13,14,15,16,18,21,23,24,25 |
| `group` | 15 | 15 | 0 | 15 | 0 | 15,17,18,19,20,23,24,25 |
| `func` | 15 | 14 | 1 | 0 | 15 | 14,16,18,19,21,22,23,24,25 |
| `field` | 13 | 13 | 0 | 13 | 0 | 13,14,16,17,18,19,22,23,25 |
| `galois` | 11 | 11 | 0 | 11 | 0 | 12,14,16,17,19,20,22 |
| `ag` | 10 | 10 | 0 | 10 | 0 | 12,13,18,19,22,23,24,25 |
| `poly` | 8 | 8 | 0 | 8 | 0 | 13,15,18,19,24 |
| `quad` | 6 | 5 | 1 | 6 | 0 | 12,14,19,21,22,25 |
| `homol` | 6 | 6 | 0 | 6 | 0 | 17,18,19,21,25 |
| `ineq` | 5 | 2 | 3 | 0 | 5 | 13,14,17,18 |
| `ode` | 5 | 5 | 0 | 0 | 5 | 15,18,20,21,23 |
| `sylow` | 4 | 4 | 0 | 4 | 0 | 17,18,19,20 |
| `potential` | 4 | 3 | 1 | 0 | 4 | 13,16,19 |
| `approx` | 4 | 4 | 0 | 0 | 4 | 16,18,19,25 |
| `padic` | 3 | 3 | 0 | 3 | 0 | 21,22,25 |
| `wave` | 3 | 3 | 0 | 0 | 3 | 22,24 |
| `dyn` | 3 | 2 | 1 | 0 | 3 | 14,19,23 |
| `cat` | 2 | 2 | 0 | 2 | 0 | 16,25 |
| `comb` | 2 | 2 | 0 | 2 | 0 | 18,25 |
| `geom` | 2 | 2 | 0 | 0 | 2 | 18,21 |
| `valua` | 1 | 1 | 0 | 1 | 0 | 19 |
| `ergodic` | 1 | 1 | 0 | 0 | 1 | 25 |
| `special` | 1 | 1 | 0 | 0 | 1 | 16 |

### 3.2 考点 × 年份 题次矩阵（前 18 个考点）

| 考点 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear | 2 | 2 | 2 | 4 | 2 | . | 4 | 4 | 3 | 2 | 1 | 2 | 2 | 3 | 33 |
| pde | 1 | 1 | 1 | . | 2 | 6 | 3 | 4 | 2 | 1 | 3 | 2 | 4 | 3 | 33 |
| real | 1 | 4 | 3 | 4 | 4 | 4 | 1 | 3 | 3 | 2 | 1 | . | . | . | 30 |
| cplx | 1 | 2 | 3 | 2 | 2 | 3 | 3 | 1 | 2 | 1 | 2 | 3 | 2 | 1 | 28 |
| comm | 1 | 1 | 1 | 1 | 2 | 1 | 3 | 1 | 1 | . | 2 | 2 | 2 | . | 18 |
| ant | . | 1 | 2 | 3 | 1 | 1 | 1 | 1 | 3 | 2 | 1 | 1 | 1 | . | 18 |
| rep | 1 | 2 | 2 | . | 1 | 2 | 1 | 1 | 1 | 2 | . | 1 | 2 | . | 16 |
| harm | 1 | 1 | 2 | 2 | 2 | . | 2 | . | . | 1 | . | 2 | 1 | 2 | 16 |
| group | . | . | . | 1 | . | 3 | 1 | 1 | 2 | . | . | 2 | 2 | 3 | 15 |
| func | . | . | 1 | . | 2 | . | 1 | 1 | . | 3 | 1 | 2 | 2 | 2 | 15 |
| field | . | 1 | 1 | . | 1 | 1 | 4 | 2 | . | . | 1 | 1 | . | 1 | 13 |
| galois | 2 | . | 1 | . | 2 | 2 | . | 2 | 1 | . | 1 | . | . | . | 11 |
| ag | 2 | 1 | . | . | . | . | 2 | 1 | . | . | 1 | 1 | 1 | 1 | 10 |
| poly | . | 1 | . | 3 | . | . | 1 | 2 | . | . | . | . | 1 | . | 8 |
| quad | 1 | . | 1 | . | . | . | . | 1 | . | 1 | 1 | . | . | 1 | 6 |
| homol | . | . | . | . | . | 1 | 1 | 1 | . | 2 | . | . | . | 1 | 6 |
| ineq | . | 2 | 1 | . | . | 1 | 1 | . | . | . | . | . | . | . | 5 |
| ode | . | . | . | 1 | . | . | 1 | . | 1 | 1 | . | 1 | . | . | 5 |

### 3.3 方法/定理关键词频次（按题计）

| 方法/定理 | 题次 |
|---|---|
| 调和函数 | 7 |
| 极大值原理 | 7 |
| 分圆域 | 5 |
| 二次型 | 4 |
| 正规族 | 4 |
| Sylow 定理 | 3 |
| 分裂域 | 3 |
| 不变量论 | 3 |
| Fourier 变换 | 3 |
| Poisson 积分 | 3 |
| 能量方法 | 3 |
| 对偶 | 3 |
| Schwarz 引理 | 3 |
| 凸分析 | 3 |
| Bruhat 分解 | 2 |
| 双陪集 | 2 |
| 整值多项式 | 2 |
| 有限差分 | 2 |
| 有理标准形 | 2 |
| Eisenstein | 2 |
| 谱分解 | 2 |
| 极分解 | 2 |
| 矩阵指数 | 2 |
| Jordan 形 | 2 |
| 特征和 | 2 |
| Vandermonde 型行列式 | 2 |
| 分圆整数 | 2 |
| 局部域 | 2 |
| Smith 标准形 | 2 |
| 交换子空间 | 2 |

> §3 全部数字由 `finals_final_stats.py` 从逐题标注库 `finals_alg_ana_problems.py` + `finals_alg_ana_extras.py` 汇总，
> 标签是**人工逐题标注后再机器汇总**，不是关键词匹配噪声。卷面动词的机器统计见 `finals_alg_ana_stats.py` 与 §4。


---

## 4. 总决赛 vs 初赛（笔试）的差异

对比基准取自既有笔试报告：`.tmp/burn2026/reports/stats_overview.md`（136 PDF / 120 卷 / 759 题）与
`.tmp/burn2026/reports/problem_metrics.md`（679 道可度量题）。以下 8 条差异均有计数支撑。

### D1. 卷别体系多一层：笔试只有 Individual/Team，总决赛多出 Overall（All-round）
- 笔试：stats_overview.md §3 的 120 卷明细中卷别只有 `individual` / `team` 两类，**没有 Overall 类**。
- 总决赛：73 卷里 **24 卷是 Overall**（占 33% 的卷数），共 **54 题**（占 244 题的 22%）。
- Overall 卷题量最少（**2.25 题/卷**），卷面多写 `All-round` / `All-around` / `Overall individual round`，
  是总决赛特有的「口试总轮」。**只看笔试语料会系统性漏掉这 22% 的真题。**

### D2. 单卷题量只有笔试的一半左右
- 笔试 759 题 / 120 卷 = **6.32 题/卷**；总决赛 244 题 / 73 卷 = **3.34 题/卷**。
- 分卷别：Individual 4.14、Team 3.52、Overall 2.25 题/卷。
- 佐证：笔试报告多卷标注「解析题数 6」，而总决赛 14 年里最大的卷面题号是 6（2020 ALG Individual）。

### D3. 命题动词更偏证明：计算类几乎消失
- 机器统计（`finals_alg_ana_stats.py`，对本范围 67 卷全文计数）：
  - ALG：prove 63 / show 42 / find 8 / compute+calculate 4 / determine 10 / solve 1 / classify 8 / describe 7
  - ANA：prove 61 / show 41 / find 9 / compute+calculate 2 / determine 2 / solve 16 / estimate 3
  - ALG 中 prove+show 占全部动词的 88%，纯计算类仅 4 次。
- 笔试对照（problem_metrics.md §4）：compute 64 题、calculate 19 题、derive 27 题、solve 25 题、evaluate 5 题，
  计算/推导类动词覆盖 110 题以上（约 16% 的题），显著高于总决赛。

### D4. 题目长度：分析卷变长、代数卷变短
- 剔除附官方解答的 2021 代数两卷后：总决赛 **ALG 61.0 词/题**（92 题）、**ANA 56.5 词/题**（110 题）。
- 笔试：**ALG 84 词/题**、**ANA 49 词/题**（problem_metrics.md §2）。
- 即 ANA 由 49 升到 56.5（+15%），ALG 由 84 降到 61（−27%）。
- 解释：总决赛代数题常是「短题干 + 长推导」（2025 ALG Individual Q2 只有一行），
  分析题则必须写清方程、区域、边界条件与待证估计，题面自然更长。

### D5. 考点重心不同：总决赛把权重压到核心硬分析 + 线性代数 + 交换代数/数论
- 总决赛 ANA 前四：**pde 33、real 30、cplx 28、harm 16**（func 15）。
  笔试（problem_metrics.md §3）：复分析 36、PDE 27、实分析 26、泛函 15、调和/位势 18。
  即总决赛**明显抬高 PDE 与调和分析权重**，并新增笔试几乎不考的波动/色散（3 题）与遍历论（1 题）。
- 总决赛 ALG 前四：**linear 32、comm 18、ant 18、rep 16**（group 15、field 13、galois 11）。
- 笔试几乎不涉及的高端考点在总决赛反复出现：p 进/局部域 **3 题**（2021 范数群、2022 平方和、2025 Q_3 不可约性）、
  同余数与椭圆曲线（2019 ALG Team #4）、赋值完备化（2019 ALG Team #3）、范畴中心（2016 ALG Team #2）、
  Weyl/Clifford 代数单模（2016 ALG Team #3、2024 ALG Individual #3）、Mason–Stothers（2024 ALG Team #2）。

### D6. 难度整体上移
- 总决赛自评难度：均值 **3.32**，≥4 占 **38%**（92/240），=5 有 **18 题**。
- 笔试启发式难度代理 ALG 2.64 / ANA 1.72（problem_metrics.md §2；口径为长度+小问数+符号密度，不能直接相减）。
- 更可比的口径：笔试 ANA 平均小问 0.51，而总决赛 ANA 大量题带 (1)(2)(3) 多步结构
  （2023 ANA Individual #1 的 (i)(ii)(iii)、2024 ANA Individual #2 的 (i)(a)(b)(ii)、2019 ANA Individual #5 的四小问），
  同一道题要求的推导链条更长。

### D7. 卷面形式：总决赛是「口试」，笔试是「笔试」
- 出现 **Oral / ORAL** 的卷共 6 卷：2012 ALG Individual（ALGEBRA ORAL）、2013 ALG Individual（Individual Oral Test）、
  2013 ALG Team（Team Oral Test）、2014 ALG Individual（2014 ORAL EXAM）、2021 ANA Individual / 2021 ANA Overall（12th Oral Exam）。
- 另有 `All-round / Overall / All-around` 共 11 卷、`Final Contest` 3 卷（2023）。
- 笔试语料没有这类口试标记，且 2020–2022 出现「试卷 + 解答」成对文件。

### D8. 总决赛有「选做」机制，笔试没有
- 总决赛 **8 卷**允许选做（`finals_forms.py` 关键词扫描）：
  - 2023 ANA Individual：solve three out of the following four problems
  - 2023 ANA Overall：solve one of the following two problems
  - 2023 ANA Team：solve two from the following three problems
  - 2023 ALG Individual：Choose (1) or (2), but not both
  - 2025 ANA Individual：solve at least three out of the following four
  - 2025 ANA Overall：solve one out of the following two
  - 2025 ANA Team：solve at least two out of the following three
  - 2021 ANA Individual 第 4、5 题标注 optional（星号）
- 选做机制**全部集中在 2021 年之后的 ANA**（2023 年 4 卷 + 2025 年 3 卷 + 2021 年 1 卷，共 8 卷），是总决赛近年最显著的卷面变化。


---

## 5. Individual 卷 vs Team 卷差异

### 5.1 总体量化（含恢复集）

| 指标 | Individual | Team | Overall |
|---|---|---|---|
| 卷数 | 28 | 21 | 24 |
| 题数 | 116 | 74 | 54 |
| 题/卷 | 4.14 | 3.52 | 2.25 |
| 难度均值(自评) | 3.18 | 3.56 | 3.30 |
| 难度 ≥4 占比 | 30% | 51% | 39% |

### 5.2 分科目难度分布

| 科目 | 卷别 | 题数 | 难度均值 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|
| ALG | Individual | 51 | 3.12 | 1 | 9 | 26 | 13 | 2 |
| ALG | Team | 34 | 3.47 | 0 | 2 | 16 | 14 | 2 |
| ALG | Overall | 24 | 3.42 | 0 | 0 | 14 | 10 | 0 |
| ANA | Individual | 65 | 3.23 | 0 | 9 | 34 | 15 | 4 |
| ANA | Team | 40 | 3.64 | 0 | 4 | 14 | 13 | 8 |
| ANA | Overall | 30 | 3.20 | 0 | 7 | 12 | 9 | 2 |

### 5.3 六条差异结论

**T1. 题量：Individual > Team > Overall（4.14 : 3.52 : 2.25 题/卷）。**
Individual 卷 2018–2020 稳定 5–6 题（2018/2019 ALG 各 5 题、2020 ALG 6 题）；Team 卷 2–6 题；
Overall 卷 1–4 题，且常写「solve one out of the following two」。

**T2. 难度：Team 卷最难。** 全部题合计：Team 3.56 > Overall 3.30 > Individual 3.18；
难度 ≥4 的比例 Team **50%**、Individual 30%、Overall 38%。分科目看 **ANA Team 最高（3.64）**，
18 道难度 =5 的题里 9 道出自 Team 卷（2013 ANA Team #3/#4、2017 ANA Team #4、2018 ANA Team #3/#4、
2019 ANA Team #3、2024 ANA Team #1、2014 ANA Team #5、2013 ANA Overall #2）。

**T3. 题面长度：Team 卷最长。** ANA Team 平均 **71.5 词/题** vs ANA Individual 50.6 / Overall 51.6；
ALG Team 64.7 vs ALG Individual 50.2。Team 题通常给出完整方程组、区域与多小问。

**T4. 结构：Team 卷偏爱「带引导的分步证明」。**
2013 ALG Team #1 把「tr(Aⁿ)∈F ∀n≥2 ⟹ tr(A)∈F」拆成 a)–d) 四步并附 Hint；
2018 ANA Team #1 把等周不等式拆成「凸性 → Steiner 对称化 → 只有圆盘」三步；
2019 ALG Team #4 把同余数问题拆成 (a) 判别式、(b) 无穷多 n≡r (mod 8)。
Individual 卷则多为单问直给（2016 ALG Individual #3、2019 ALG Individual #5 各只有一句话）。

**T5. 考点分化：Team 承担体系性/工具性考点，Individual 承担基础必修考点。**
- 只在 Team 出现的（代数）：范畴的中心（2016 #2）、Nakayama（2018 #3）、Chevalley–Warning（2018 #1）、
  Noether 有限性（2018 #2）、Schanuel 引理（2019 #5）、模表示 Clifford 定理（2014 #4）、
  赋值完备化（2019 #3）、同余数（2019 #4）、Mason–Stothers（2024 #2）、射有限群 Ẑ（2024 #3）。
- 只在 Team 出现的（分析）：Steiner 对称化/等周（2018 #1）、ζ 的围道积分（2018 #2）、
  Korn 不等式（2018 #4）、Burgers 全变差（2019 #3）、半空间波动方程（2024 #1）、
  Gelfand 极大理想空间（2014 #5）、迭代引理（2014 #4）、爆破（2013 #3）。
- 只在 Individual 出现的：Gauss 和次数（2020 #3）、det(A)²∈Z（2020 #4）、Q_p(ζ_{pⁿ}) 范数群（2021 #1）、
  ∧²V（2021 #2）、Molien 公式（2023 #3）；分析侧：不确定性原理（2023 #1）、Legendre 求积（2019 #5）、
  Phragmén–Lindelöf 型边界估计（2025 #2）、等分布（2025 #1）。

**T6. 2020–2022 三年 Team 卷整体缺席。** ALG Team 缺 2014、2020、2021、2022；ANA Team 缺 2012–2014、2020、2021、2022。
2020–2022 连续三年两个科目**都没有 Team 卷**；核对 F 盘目录后确认这不是抽取失败（目录里确实没有对应文件），属赛制/语料共同缺口。


---

## 6. 代表题（8 道完整题面 + 解题思路）

> 题面按抽取原文转录，只做了最小必要的排版 LaTeX 化（如 x2+y2 写成 x²+y²、p−2 写成 p−2），
> 题号、条件、结构均未改动；凡抽取有损处均在该题末尾标注。

### R1 · 2014 · 代数与数论 · Individual · Problem 3（三次域与 F_p 上的点数）

出处：`.tmp/burn2026/txt_finals/2012_2025Algebra_Number_Theory_and_Combinatorics_Individual_2014_Algebra_Individual.txt`（文字层完好）

> Problem 3. Let p > 3 be a prime. Consider the equation
>
> $$x^3 + y^3 = 1 \quad (\ast)$$
>
> in Z/pZ.
> (1) When p ≡ 2 (3), find the number of solutions.
> (2) When p ≡ 1 (3), prove that there exists a pair (a, b) of integers such that
>   (a) 4p = a² + 27b²,
>   (b) a ≡ 1 mod 3. (Note: a is unique.)
> (3) (Continuation of (2)) When p ≡ 1 (3). Prove that (*) has p−2+a solution in Z/pZ.

**解题思路**
1. 把问题看成有限域上仿射三次曲线的点数：N = #{(x,y) ∈ F_p² : x³+y³=1}。
2. (1) p ≡ 2 (mod 3) 时 gcd(3, p−1) = 1，故 x ↦ x³ 是 F_p 上的置换。
   于是对每个 y 恰有一个 x，解数直接是 p（含 y 任意取遍 F_p 的 p 个选择）——用「置换」代替枚举即可。
3. (2) 是经典 Gauss 结果：p ≡ 1 (mod 3) 时 p 在 Q(ζ_3) = Q(√−3) 中分裂，p = ππ̄；
   令 π = (a + b√−27)/2 即得 4p = a² + 27b²；再对 π 乘上 ζ_3 的幂使 a ≡ 1 (mod 3)，唯一性由单位的选择固定。
4. (3) 是关键一步：用三次特征标 χ（F_p^× → μ_3）把点数的偏差写成 Jacobi 和。
   对 t ≠ 0 记 N(t) = #{x³+y³ = t}，则 N(t) = p − 1 + χ(...) 形式；把 t = 1 代回并整理出 N = p − 2 + a，
   其中 a 正好是 π + π̄（即 4p = a²+27b² 中那个 ≡1 mod 3 的 a）。
   **不必真的算出 (a,b)**：题目只要求把解数用 (2) 中的 a 表示。
5. 这道题是「数域分裂 × 特征标和 × 有限域点数」三件事的标准缝合，属总决赛压轴级（自评 5）。

### R2 · 2021 · 代数与数论 · Individual · Problem 1（局部域范数群）★ 原卷附官方解答

出处：`.tmp/burn2026/txt_finals/2012_2025Algebra_Number_Theory_and_Combinatorics_Individual_2021_Algebra_Individual_S.txt`
（文件名带 `(S)` = 含官方解答；本题是本报告范围内**唯一能看到出题方解答**的题之一，另有 2021 ALG Overall 两题）

> Problem 1. (Individual round.) Let p be a prime number and Q_p the field of p-adic numbers.
> Let n ≥ 1 be an integer and L = Q_p(ζ_{p^n}), where ζ_{p^n} denotes a primitive p^n-th roots of unity.
> Determine the image of the norm map N_{L/Q_p} : L^× → Q_p^×.
> You may use the inequality [L : Q_p] ≤ (Q_p^× : N_{L/Q_p}(L^×)) without proof in the case n ≥ 2.

**官方解答要点（原文抽取，已压缩）**
> We will show that N_{L/Q_p}(L^×) = p^Z (1 + p^n Z_p).
> Let Φ(X) = (X^{p^n} − 1)/(X^{p^{n−1}} − 1). Then Φ(X+1) is an Eisenstein polynomial. Thus Φ(X) is the minimal
> polynomial of ζ_{p^n}, so that N_{L/Q_p}(1 − ζ_{p^n}) = Φ(1) = p.
> We have [L : Q_p] = φ(p^n) = p^n − p^{n−1}. For p odd, the φ(p^n)-th power map on 1 + pZ_p is the composition
> 1 + pZ_p −log→ pZ_p −φ(p^n)→ p^n Z_p −exp→ 1 + p^n Z_p. Thus N(1 + pZ_p) = 1 + p^n Z_p.
> For p = 2 (n ≥ 2) 同理在 1 + 4Z_2 上得 N(1 + 4Z_2) = 1 + 2^{n+1}Z_2，并利用
> 1 + 2^n Z_2 = (1 + 2^{n+1}Z_2) ⊔ 5^{2^{n−2}}(1 + 2^{n+1}Z_2) 与 5^{2^{n−2}} = N(2 + ζ_4)。
> 反向包含：O_L 的剩余域是 F_p，故 N 在 O_L^× 上与 F_p^× 的 φ(p^n) 次幂映射相容，
> 得 N(L^×) ∩ Z_p^× ⊆ 1 + pZ_p；n ≥ 2 时用题给不等式卡指数即可。

**解题思路**
1. 先猜答案：范数群应该是「p 的整数次幂 × 主单位群 1 + p^nZ_p」——两个因子分别对应分歧与剩余域。
2. 下界：用 1 − ζ_{p^n} 造出 p（Eisenstein 判别法给出极小多项式），再用 log/exp 把乘法群同构到加法群，
   在加法群上 φ(p^n) 次幂映射就是乘 φ(p^n)，于是 1 + pZ_p 被映到 1 + p^n Z_p。
3. 上界：范数在剩余域上诱导 φ(p^n) 次幂映射，F_p^× 的 φ(p^n) 次幂全为 1，故单位范数只能落在 1 + pZ_p。
4. 最后用题给指数不等式（局部类域论的 [L:Q_p] ≤ 范数指数）夹逼，指数恰好对上。
5. 自评难度 5：需要局部域的分歧理论 + log/exp + 类域论的标准不等式，是总决赛代数里最「研究生课」的一题。

### R3 · 2025 · 代数与数论 · Individual · Question 4（平方和层次 l(K)）

出处：`.tmp/burn2026/txt_finals/..._Individual_2025_Algebra_Individual.txt`（文字层完好）

> Question 4. Let K be a field, we define l(K) to be the smallest natural number n such that there are n
> elements x_1, ..., x_n in K satisfying −1 = x_1² + x_2² + · · · + x_n². If no such n exists, we denote l(K) by ∞.
> 1. Prove that l(K) = l(K(t)), here K(t) is the field of rational functions with coefficients in K.
> 2. Compute l(K) when K are the following fields: Q(e^{2iπ/3}), Q(e^{2iπ/3}, 2^{1/3}).

**解题思路**
1. 这是形式实域/二次型层次（level of a field，经典结果是 level ∈ {1,2,4,8,…} 或 ∞）的竞赛化版本。
2. 第一部分：l(K(t)) ≤ l(K) 显然（常数解）。反向用**赋值/首项系数**论证：
   若 −1 = Σ f_i(t)² 于 K(t)，取一个赋值（t 的阶）使某项在赋值下严格占优，则首项平方和不可能抵消为 0，矛盾。
   等价的说法：K(t) 的 t-进赋值是实赋值，形式实域的有理函数域仍形式实。
3. 第二部分（两个具体域）——两者可用同一条恒等式处理：
   - 关键观察：设 ω = e^{2πi/3}，则 ω² + ω + 1 = 0，即 **−1 = ω + ω²**；
     而 ω 与 ω² 在 Q(ω) 中都是平方：ζ_6 = e^{iπ/3} = −ω² ∈ Q(ω)，且 (ζ_6)² = ω、(ζ_6²)² = ω²。
     于是 −1 = (ζ_6)² + (ζ_6²)² 已是**两个平方之和**，故 l(Q(ω)) ≤ 2；
     又 i ∉ Q(ω)（Q(ω) = Q(√−3) 不含 √−1），故 −1 不是平方，l(Q(ω)) = **2**。
   - K = Q(ω, 2^{1/3})：上面的 ω、ω² 仍是 K 中的平方，所以 l(K) ≤ 2；
     而 l(K) = 1 需要 −1 是平方（即 i ∈ K）。K 是 x³−2 的分裂域，Gal(K/Q) ≅ S_3，
     其唯一指数 2 子群 A_3 对应唯一二次子域 Q(ω)，因此 i ∉ K，l(K) = **2**。
   （**抽取存疑**：第 2 问的两个域在抽取文本中是 `Q(e2iπ/3), Q(e2iπ/321/3)`，
   可读作 Q(e^{2πi/3}, 2^{1/3}) 或 Q(e^{2πi/3}·2^{1/3})。上面按前一种记法推理；
   若原意是后一种（即 Q(ω∛2)，一个三次域），则「l ≤ 2」的论证仍成立，
   而 l = 1 的排除理由换成「三次域不含 Q(i)」——结论同样是 2。引用前请以原卷为准。）
4. 自评难度 4：需要知道「域的形式实性 ⟺ 存在序 ⟺ −1 不是平方和」这条链，以及有理函数域保序。

### R4 · 2018 · 代数与数论 · Team · Problem 1（Chevalley–Warning）

出处：`.tmp/burn2026/txt_finals/..._Team_2018_Algebra_Team.txt`（文字层完好）

> Let d_i (1 ≤ i ≤ n) be positive integers such that Σ_{i=1}^{n} 1/d_i > 1.
> For a prime number p, let F_p be the finite field of p elements. For
>
> f(x_1, · · · , x_n) = x_1^{d_1} + x_2^{d_2} + · · · + x_n^{d_n},
>
> prove that the number
>
> N := #{(x_1, · · · , x_n) ∈ F_p^n | f(x_1, · · · , x_n) = 0}
>
> is divisible by p. Hint: consider the sum Σ_{(x_1,···,x_n) ∈ F_p^n} f(x_1, · · · , x_n)^{p−1}.

**解题思路**
1. 这是 **Chevalley–Warning 定理**的标准证明路线，题干给了提示。
2. 记 S = Σ_x f(x)^{p−1}。在 F_p 中 f(x)^{p−1} 当 f(x) ≠ 0 时为 1，f(x)=0 时为 0，
   所以 S ≡ #(非零点) = p^n − N (mod p)。若能证 S ≡ 0，则 N ≡ 0 (mod p)。
3. 展开 f^{p−1} = (Σ x_i^{d_i})^{p−1}，得到形如 Π x_i^{e_i d_i} 的单项式之和，
   其中 Σ e_i = p−1。每个单项式的全空间和 Σ_{x∈F_p^n} Π x_i^{e_i d_i} 是乘积 Σ_{x_i} x_i^{e_i d_i}；
   而 Σ_{x ∈ F_p} x^m = 0 除非 m > 0 且 (p−1) | m（此时等于 −1）。
4. 于是只有那些「所有 e_i d_i 都是 (p−1) 的正倍数」的项才可能非零；
   由 Σ 1/d_i > 1 可证这样的项不存在（因为那要求 Σ e_i ≥ Σ (p−1)/d_i > p−1，与 Σ e_i = p−1 矛盾）。
5. 因此 S = 0，N ≡ 0 (mod p)。自评难度 4：技巧全在「有限域上单项式求和」这一个引理。

### R5 · 2019 · 分析与微分方程 · Team · Question 3（Burgers 方程的全变差估计）

出处：`.tmp/burn2026/txt_finals/..._Team_2019_Analysis_Team.txt`（文字层完好）

> Consider the Cauchy problem for the Burger’s equation (B):
>
> $$\partial_t u + u\partial_x u = \epsilon \partial_x^2 u, \quad x \in \mathbb{R},\ t > 0; \qquad u(x, t = 0) = u_0(x)$$
>
> where ε ∈ (0, 1) is a constant, and u_0(x) is a smooth periodic function of period 1.
> (1) Prove that if u^ε(x, t) is a solution to (B), then u^ε(x, t) is uniformly bounded independent of ε.
> (2) Prove that the solution u^ε(x, t) is periodic in x with period 1.
> (3) Show that if u^ε(x, t) is a solution to (B), then ∂_x u^ε(x, t) ≤ 1/t for all x ∈ R, t > 0.
> (4) Show that the total variation of u^ε(x, t) in x is uniformly bounded independent of ε for t > 0,
>     i.e. TV_{[0,1]} u^ε(x, t) ≤ C(t).
> (5)(*) Discuss the convergence property of u^ε(x, t) as ε → 0+.

**解题思路**
1. (1) 是标量守恒律的标准 **极大值原理**：u_t + u u_x = ε u_xx 在极值点处 u_xx ≤ 0、u_x = 0，
   故 max|u| 不随时间增加，一致界就是 ‖u_0‖_∞。
2. (2) 用**初值周期性的唯一性**：把 u(x+1,t) 与 u(x,t) 看成两个解，初值相同 ⟹ 解相同（抛物方程唯一性）。
3. (3) 是 **Hopf 引理/导数下界**：对 v = ∂_x u 求导得 v_t + u v_x + v² = ε v_xx，
   在 v 的最大值点处 v_x=0、v_xx ≤ 0，得 d/dt v_max ≤ −v_max²，解常微分不等式得 v ≤ 1/t。
4. (4) 由 (3) 与 (1)：TV 的负变差被「单调下降段的总下降量」控制，
   TV(u) ≤ 2 max|u| + ∫(正变差) ≤ 2‖u_0‖_∞ + (1/t)·(周期长度)，故 TV ≤ C(t) 且与 ε 无关。
5. (5) 是开放题，指向 ε → 0 时解收敛到熵解（无粘极限）。
6. 自评难度 5：五个小问把「最大值原理 → 抛物唯一性 → 导数界 → BV 估计 → 无粘极限」串成一条完整链条，
   是 Team 卷「引导式长题」的典型。

### R6 · 2025 · 分析与微分方程 · Individual · Problem 2（Phragmén–Lindelöf 型边界估计）

出处：`.tmp/burn2026/txt_finals/..._Individual_2025_Analysis_Individual.txt`（文字层完好）

> Let Ω = { x + iy ∈ C : x > 0, y > 0 }. Assume that f : Ω → C is a bounded continuous function on Ω
> and holomorphic on Ω such that
>
> ∀x ∈ [0, +∞], max{|f(x)|, |f(ix)|} ≤ { 2 if x ≤ 1; 1 if x > 1 }.
>
> Show that ∀x + iy ∈ Ω, |f(x + iy)| ≤ 2^{(2/π) arctan(1/(2xy))}.

**解题思路**
1. Ω 是第一象限（角域，开口 π/2）。边界条件只有**两条正半轴**上「以 1 为界、在 [0,1] 段放宽到 2」。
2. 标准工具是 **Phragmén–Lindelöf / 调和测度**：右端指数 (2/π)·arctan(1/(2xy)) 恰是
   角域边界上「哪一段可见」的调和测度（= 共形映射到条带后的 Poisson 核权重）。
3. 做法：把 Ω 用 z ↦ z² 映到上半平面（角域 → 半平面），此时边界条件变成上半平面实轴上的两段界：
   |z| ≤ 1 段给 2、|z| > 1 段给 1；再用上半平面的 Poisson 公式/次调和函数比较，
   得到 log|f| 不超过边界势的调和延拓，即 log|f(w)| ≤ (2/π)·arctan(1/(2xy))·log 2。
4. 指数化即得结论；关键是把 arctan 项识别成「从点 (x,y) 看 [0,1] 段的视角/调和测度」。
5. 自评难度 5：需要会「把角域映成半平面 + 用调和测度把边界数据加权」，是总决赛分析卷近年最难的构型题之一。

### R7 · 2018 · 分析与微分方程 · Team · Problem 1（等周不等式与 Steiner 对称化）

出处：`.tmp/burn2026/txt_finals/..._Team_2018_Analysis_Team.txt`（文字层完好，原文分 3 步）

> 1. Isoperimetric inequality and Steiner symmetrization.
> It is well known that in R², any region Ω with continuous piecewise C¹ boundary ∂Ω satisfies that
> 4π|Ω| ≤ Length(∂Ω)². When the equality holds ..., it is then called an isoperimetric set.
> For example, all disks are isoperimetric sets.
> 1) Prove that any isoperimetric set is convex;
> 2) Given a line V in R² passing through the origin, the Steiner symmetrization with respect to V is the
>    operation which associates with each bounded convex subset C of R² the subset S(C) of R² such that,
>    for every line L perpendicular to V, either L ∩ C = ∅ and L ∩ S(C) = ∅, or L ∩ C ≠ ∅ and L ∩ S(C)
>    is a closed segment with center in V, and Length(L ∩ S(C)) = Length(L ∩ C).
>    Prove that |S(C)| = |C|, and Length(∂S(C)) ≥ Length(C), equality holds if and only if C is symmetric
>    with respect to V.
> 3) Deduce that the only isoperimetric sets are the disks.

**解题思路**
1. (1) 若等周集 Ω 不凸，取凸包：凸包面积变大（若真有凹陷）而周长不增，与等周等式矛盾。
2. (2) 面积不变是 Fubini（每条垂直线上线段长度不变）；周长不减需要把周长拆成
   「与 V 垂直的边」与「两个函数图像（上半/下半边界）」，
   前者按构造不变，后者用一元函数的**变差/弧长**在「把两端点向中线压缩」下不增（等号 ⟺ 每层对称）来证。
3. (3) 反复做不同方向 V 的 Steiner 对称化，面积不变、周长不增，序列收敛到圆盘（对称化 + 紧性），
   结合 (1) 的凸性，得到等周集只能是圆盘。
4. 自评难度 4：这是一道「把一个经典定理拆成可验证步骤」的证明题，计算量大但每一步都是标准工具。

### R8 · 2024 · 分析与微分方程 · Individual · Problem 2（热/波方程解的水平集与传播）

出处：`.tmp/burn2026/txt_finals/..._Individual_2024-_Analysis_Individual-new1.txt`（文字层完好，原文分 (i)(a)(b)(ii)）

> (i) Consider the following Cauchy problem:
>
> $$u_t - (a(x)u_x)_x = 0 \quad \text{for } x \in \mathbb{R},\ t > 0, \qquad u|_{t=0} = u_0(x),$$
>
> where a(x) ∈ C² is bounded with a(x) ≥ a_0 > 0.
> (a) Let u(x, t) be the solution with u_0(x) = 1 for x ∈ [−1, 1], 0 otherwise.
>     Does u(x, t) have zero points on the line t = 1/1000? Explain your reasons.
> (b) Is it possible to prepare some bounded initial data u_0(x) such that the solution becomes
>     u(x, 1) = 1 for x ∈ [−1, 1], 0 otherwise, at t = 1? Explain your reasons.
> (ii) Consider the following Cauchy problem:
>
> $$u_{tt} - (a(x)u_x)_x = 0, \qquad u|_{t=0} = u_0(x),\ u_t|_{t=0} = 0,$$
>
> with the same u_0. Does u(x, t) have zero points on the line t = 1000? Explain your reasons.

**解题思路**
1. 三个小问考的是**同一件事的不同侧面：解在多大范围内「记得」初值**。
2. (i)(a) 抛物方程具有**无穷传播速度**：热核在任意正时刻都有全支撑。u_0 ≥ 0 且不恒为 0，
   故 t = 1/1000 时 u(·, t) > 0 处处成立（用极大值原理证：若某点取 0，则与正初值矛盾）→ **没有零点**。
3. (i)(b) 不可能。方向相反：解算子把非负初值磨成处处正的函数，
   而目标函数在 [−1,1] 外取 0，在其边界处不满足抛物方程的正则性/无穷传播速度蕴含的严格正性 → 矛盾。
4. (ii) 波动方程具有**有限传播速度**（c = √(a(x)) 有正上下界）：
   t = 1000 远大于支撑传播所需时间，故依赖域内的信息早已离开，
   u(·, 1000) 在 [−1,1] 的传播锥之外恒为 0 → **有零点**。
5. 自评难度 4：每个小问都只需一条定性原理（无穷传播速度 vs 有限传播速度），
   但要在「是否有零点」这个很弱的问题上把它用对，需要对两套方程的性质分得非常清楚。

> **抽取说明**：2024 ANA Individual 的 PDF 抽取在第 2 页末尾把 「in B \ {0}」 一行错位到文末，
> 该错位不影响本题题面。


---

## 7. 存疑与无法分析清单

### 7.1 完全无法分析（放弃）

| 出处 | 内容 | 原因 |
|---|---|---|
| 2012 ANA Individual #2 | 整函数与其迭代的题 | 源为 .doc，公式全是 OLE 对象，条件（f 的规范化、迭代估计）全部丢失 |
| 2014 ANA Individual #3 | 「对素数全体证明级数发散」 | 级数本身丢失，只剩结论文字 |
| 2014 ANA Individual #5 | (a)(b) 两个小问 | 题面公式全丢，只剩 a) b) 两行 |
| 2013 ANA Team #2 | 无内容 | 原 Word 文件里只有标题 |

### 7.2 分析但需存疑

| 出处 | 存疑点 | 处理 |
|---|---|---|
| 2015 ALG Individual / Team / Overall | 无文字层或 CJK 字体损坏，本报告的题面由**渲染后人工识读**得到 | 题面按识读结果录入；个别符号（如 Z[w]/(1−w)、‖M‖=sup 的写法）以原卷渲染图为准 |
| 2014 ALG Team #1、#2 | .docx 抽取把 α, β 的作用式与矩阵 J 打散 | 描述中标「题面公式经抽取后残缺，按上下文重排」 |
| 2025 ALG Individual #4 第 2 问 | e^{2iπ/3} 与 e^{2iπ/3}·2^{1/3} 的域记号在抽取中略糊 | 结论依赖记号判读，已在 R3 标注 |
| 2018 ANA Individual #5 | 抽取出的 (c) 与 (d) 两小问文字**完全相同** | 疑为原卷排版重复或抽取重复；本题仍按 5 题计入，但小问数（记为 1 题）不变 |
| 2020 ALG Individual | 两页各自从 Problem 1 重新编号 | 本报告合为 1 卷 6 题（页 1 三题 + 页 2 三题）；若按两卷计则卷数会变化 |
| 2013 ALG Individual #2 | 题面写「polynomials with both x, y-degrees at most k」但变量用 m, n | 原文即如此，未改动 |
| 2021 ANA Overall | 文件被索引为 Overall，但**卷面自称 Group Contest** | 报告按索引归入 Overall；实际可能是 Team 轮，属原始语料元数据不一致 |
| 2017 ALG Individual 等 7 卷 | 抽取出现反引号与 ă 等连字/字体替换残留（如 K “ Qpe^{2πi/m}q） | 已在引用时按语义还原，未改结构 |
| 全部恢复集 | 公式缺失 | 已在 §2.2 逐行标注「公式缺失」 |

### 7.3 语料层面的缺口（不是分析失败，是文件不存在）

| 年份 | 缺失卷 |
|---|---|
| 2012–2014 | ANA Individual 原本为 .doc/.docx（本报告已恢复）；ANA Team、ANA Overall 的 2012 年缺 |
| 2014 | ALG Team 原本为 .docx（已恢复）；ALG Overall 2014 缺失 |
| 2013、2014 | ALG Overall 缺（F 盘无对应文件） |
| 2020–2022 | ALG Team 与 ANA Team 全部缺失（连续三年） |

### 7.4 与本报告无关但影响横向比较的既有报告问题

- `.tmp/burn2026/reports/problem_metrics.md` 的难度是「长度+小问+符号密度」的启发式代理，与本题库的人工自评**不可直接比较**，
  本报告在 §4 只把它当方向性证据，并明确标注口径差异。
- 既有笔试报告统计的是 2010–2026 的**笔试**语料，其「混合/Team（多科目）」类目的是按卷切的，
  与总决赛按科目切分的 Team 卷不可直接对齐；本报告的对比只取可以对齐的口径（题量、词数、动词、考点）。


---

## 关键数字摘要

1. 分析范围：代数与数论/组合 + 分析与微分方程，总决赛 **73 卷 / 244 题**（PDF 主集 66 卷 215 题 + 从 .doc/.docx 恢复 7 卷 29 题）。
2. 全语料 195 个 txt 中 chars<800 有 65 个，但**真正无文字层**在本范围只有 1 卷（2015 ALG Overall，0 字符 / 11 张图）；
   另有 2 卷 CJK 字体损坏（2015 ALG Individual、Team）。三卷已渲染后人工识读，补回 8 题。
3. 新发现：**7 卷真题从未被原管线转换**（2014 ALG Team、2012/2013/2014 ANA Individual、2013/2014 ANA Team、2013 ANA Overall），
   本报告首次恢复，把分析科目的覆盖从 2015 年提前到 **2012 年**。
4. 卷别结构：Individual 28 卷 116 题（4.14 题/卷）、Team 21 卷 74 题（3.52 题/卷）、Overall 24 卷 54 题（2.25 题/卷）。
5. 考点前五：linear 33、pde 33、real 30、cplx 28、comm/ant 各 18（rep 16、harm 16、group/func 各 15）。
6. 难度自评：均值 **3.32**；=5 共 18 题、≥4 占 38%；Team 卷最难（3.56，≥4 占 50%），Individual 最平（3.18，≥4 占 30%）。
7. 与笔试差异 1：笔试只有 Individual/Team 两类卷，总决赛多出 **Overall（All-round）24 卷 54 题，占 22% 的题量**。
8. 与笔试差异 2：题量密度 笔试 6.32 题/卷 vs 总决赛 **3.34 题/卷**（约为一半）。
9. 与笔试差异 3：总决赛基本是纯证明卷——ALG 全文 prove 63 / show 42，而 compute+calculate 仅 4 次（prove+show 占 88%）。
10. 与笔试差异 4：题长 ANA 49 → **56.5 词/题**（+15%），ALG 84 → **61 词/题**（−27%）。
11. 与笔试差异 5：总决赛显著抬高 PDE（27→33 题次）与调和分析，并新出现波动/色散、遍历论、p 进局部域等笔试几乎不考的考点。
12. 与笔试差异 6：出现 **Oral/ORAL 字样的卷 6 卷**、All-round/Overall 11 卷、Final Contest 3 卷——总决赛是口试。
13. 与笔试差异 7：总决赛 **8 卷有「选做」机制**（2021 ANA Individual 两题 optional；2023 年 4 卷；2025 年 3 卷），笔试没有。
14. Individual vs Team：Team 平均难度 3.56 > Overall 3.30 > Individual 3.18；ANA Team 最高（**3.64**）。
15. Individual vs Team：题面长度 Team 最长（ANA Team **71.5 词/题** vs ANA Individual 50.6）。
16. Individual vs Team：Team 卷偏爱「a)–d) 分步引导 + Hint」（2013 ALG Team #1、2018 ANA Team #1、2019 ALG Team #4 等）。
17. Individual vs Team：**2020–2022 连续三年两个科目都没有 Team 卷**（F 盘目录核实确无文件）。
18. 官方解答：本范围只有 **2021 ALG Individual 与 2021 ALG Overall** 两卷随卷附官方解答（原文件名带 (S)）。
19. 语料缺口：ALG Overall 缺 2013、2014；ALG Team 缺 2014、2020、2021、2022；ANA Team 原本缺 2012–2014（已从 Word 恢复）、缺 2020–2022。
20. 全部题面均可追溯到 `.tmp/burn2026/txt_finals/` 或 `.tmp/burn2026/txt_finals_extra/` 的具体文件；本题库与统计脚本见
    `.tmp/burn2026/scripts/finals_alg_ana_problems.py`、`finals_alg_ana_extras.py`、`finals_final_stats.py`、`gen_report.py`。

