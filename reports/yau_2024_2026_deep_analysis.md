# 丘成桐大学生数学竞赛（Yau College Student Mathematics Competition）
# 2024–2026 笔试真题深度分析报告

- **负责时段**：2024、2025、2026 三个年份（共 18 份卷子，全部为个人赛卷）
- **语料目录**：E:\deepseek_exclusive\math\.tmp\burn2026\txt\
- **统计脚本**：E:\deepseek_exclusive\math\.tmp\burn2026\scripts\yau_2024_2026_stats.py
- **统计原始输出**：E:\deepseek_exclusive\math\.tmp\burn2026\reports\stats_2024_2026.md
- **分析方法**：全文人工精读 18 卷 → Python 脚本做结构/词频/趋势量化 → 人工校核题量与小问数
- **重要前提**：语料为 PyMuPDF 从 PDF 抽取的纯文本，公式的上下标、希腊字母、根号、矩阵括号存在错乱。本报告中所有数学内容均以抽取文本为准，凡有疑虑处一律标注，**不凭猜测补全题目**。

---

## 0. 一个必须先说清的结构性事实：2024–2026 已经没有「团体卷」

任务模板假定存在「个人卷 / 团体卷」两栏。但对本批语料逐一核查后，结论是：

**2024、2025、2026 三年，语料中只存在 6 份个人赛卷／年，没有任何团体卷文件。**

核查依据（对整个 136 份语料做文件名枚举）：

| 年份 | 语料文件数 | 是否含团体卷 | 备注 |
|---|---|---|---|
| 2010 | 8 | 有（4 份 team） | 团体卷与个人卷并列 |
| 2011 | 8 | 有（4 份 Team） | |
| 2012 | 10 | 有（5 份 team） | 5 个科目 |
| 2013 | 6 | 有（1 份 TeamProblems2013，合并卷） | |
| 2014 | 10 | 有（5 份 team） | |
| 2015 | 10 | 有（5 份 team） | |
| 2016 | 6 | 有（1 份合并 team） | |
| 2017 | 6 | 有（1 份合并 team） | |
| 2018 | 6 | 有（1 份合并 team） | |
| 2019 | 10 | 有（5 份 team） | **最后一次出现团体卷** |
| 2020 | 10 | 无 | 但含 5 份官方解答（soln） |
| 2021 | 10 | 无 | 含 5 份解答 |
| 2022 | 12 | 无 | 6 科（新增数学物理）+ 6 份解答 |
| 2023 | 6 | 无 | 6 科，无解答 |
| 2024 | 6 | 无 | 6 科，无解答 |
| 2025 | 6 | 无 | 6 科，无解答 |
| 2026 | 6 | 无 | 6 科，无解答 |

由此得到两条可直接引用的结论：

1. **赛制在 2020 年前后发生了一次结构性收缩**：团体卷自 2020 年起从语料中消失（2019 是最后一年），个人赛从 5 科（代数数论／分析微分方程／几何拓扑／计算应用／概率统计）扩展为 **6 科，新增「数学物理」（Mathematical Physics）**，该科目自 2022 年首次出现在语料中并延续至 2026。
2. **官方解答自 2023 年起停止公开**：2020–2022 每年都有 soln 文件，2023–2026 一份都没有。这意味着 2024–2026 的题目难度信息只能从题面本身推断，本报告的难度自评因此是**主观标定**，标准见下文。

**难度自评标准（1–5）**：
- 1 = 期末考基础题，套定义即可；2 = 本科高年级标准题，一步构造；3 = 需要 2–3 步组合技巧，或有非平凡计算量；4 = 需要研究生一年级课程工具（交换代数／黎曼几何／泛函分析／Sobolev），或需要非标准构造；5 = 需要研究级工具或较长推理链（Bruhat–Tits、Jacobi 和、Morse 理论、凸分析次微分、经验过程一致收敛率）。

---

## 1. 逐年逐卷逐题结构表

### 1.1 2024 年（6 卷，34 题，24229 字符）

**卷 A：Algebra and Number Theory（代数与数论）** — 6 题，2 页，4438 字符，小问标记 20 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| Q1 | 有限群 G 的忠实表示：(1) 存在有限维忠实 K-表示；(2) 有忠实 1 维复表示 ⟺ G 循环；(3) G 交换时，有忠实 n 维复表示 ⟺ G 可由 n 个元素生成；(4) 分类有忠实 2 维实表示的有限群 | 有限群表示论 | 正则表示、Cayley 定理、特征标、循环群结构、Frobenius–Schur 指标 | 3 |
| Q2 | A 为离散赋值环、π 为 uniformizer，D_λ=diag(π^{λ1},…,π^{λn})；证明 GL_n(A)·D_μ·GL_n(A) ∩ U(K)·D_λ 非空 ⟺ λ_dom ≤ μ_dom（支配序） | 代数群 / 约化理论 | Bruhat 分解、Cartan 分解、Smith 标准形、支配序（dominance order）、仿射 Grassmann 型论证 | 5 |
| Q3 | k 为特征 p>0 的非完全域，a ∉ k^p：(1) X^p−a 不可约；(2) A=k[X]/(X^{p²}−aX^p)，求 A_red | 域论 / 交换代数 | 纯不可分扩张、Frobenius 映射、幂零根与既约化 | 3 |
| Q4 | k 特征 p>0，k(t)⊂k((t))：(1) k((t))/k(t) 是超越扩张；(2) α∈k[[t]] 在 k(t) 上超越，β=α^p，A=k[[t]]∩k(t,β)，求 A 在 L=k(t,α) 中的整闭包 B，证 A、B 均为 DVR；(3) B 是否 A 上有限生成模 | 赋值论 / 代数数论 | 整闭包、离散赋值环、野分歧（wild ramification）、p 次纯不可分 | 5 |
| Q5 | p-adic：(1) 证 Z 在 Z_p 中稠密，并推出 f:Z→Q_p 可连续延拓到 Z_p ⟺ f 一致连续（模 p^N 判据）；(2) a∈Q_p\{0\}，a^n 何时可连续延拓到 Z_p；(3) 满足条件时能否延拓为连续同态 a^x:Q_p→Q_p | p-adic 分析 | p-adic 绝对值非阿基米德性、稠密性、连续性延拓定理、连续同态的分类 | 3 |
| Q6 | 分圆多项式：(1) (q,n)=1 时 Φ_n 在 F_q 上分解为 φ(n)/d 个 d 次不可约因子，d=ord_n(q)；(2) n=2^r+1 时，(a) 证 (x,y)=∑_τ τ(x)τ(y) 是 K_R 上的内积且 (ζ^i,ζ^j)=2^r δ_ij；(b) 分解 pO_K；(c) 对含 p 的素理想 𝔭 证 α∈𝔭 时 ‖α‖²∈2^r pZ，并求 𝔭 中最短非零向量长度 | 代数数论 / 格 | Frobenius 的阶、Dedekind 分解定理、Kummer–Dedekind、迹型内积、Minkowski 格最短向量 | 5 |

**卷 B：Analysis and Differential Equations（分析与微分方程）** — 5 题，2 页，2471 字符
> ⚠️ 本卷为 Cambria-Math 字体抽取，**整卷字符错乱**（括号变成 p/q，箭头变成 Ñ，积分号变成 ˆ 等），详见第 5 节存疑清单。以下题意基于反混淆后的可读内容。

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| P1 | 给定偶的 C_c^∞ 函数 Q、T1=xQ、T2=x²Q、T3=e^{−x²}(1+x^{2024})；断言存在 δ,ε>0，使对任意 |c|<δ 存在唯一 (λ,α) 满足 ‖λ−1‖+|α|<ε 与两条正交性不等式 ⟨Q_{λ,α}−Q−cT3, T1⟩≥0、⟨…,T2⟩≥0。**问该断言是否正确并证明** | 调和分析 / 隐函数定理 | 尺度-平移扰动、线性化、正交性条件、隐函数定理、判断命题真伪 | 5 |
| P2 | V(x)=e^{−|x|²}，证明 T = I + (−Δ+1)^{−1}V 在 L²(R³) 上可逆 | PDE / 算子论 | (−Δ+1)^{−1} 的显式核（Bessel 势）、V 的紧性、Fredholm 二择一、Kato–Rellich | 3 |
| P3 | u1, u2 为 ψ(ξ) 截断的振荡积分（色散关系分别为 ξ 与 ξ²），证明 ‖u1u2‖_{L²(R²)} ≤ C‖f1‖_{L²}‖f2‖_{L²} | 调和分析 | Plancherel 定理、双线性振荡积分、张量积结构、Strichartz 型估计 | 4 |
| P4 | R² 上热方程 u_t−Δu=0，u(0)=u0∈L²，证明 ∫_0^∞ ‖u(t)‖²_{L^∞} dt ≤ C‖u0‖²_{L²} | 抛物型 PDE | 热核估计、频域分解、Sobolev 嵌入、时空估计 | 4 |
| P5 | 对双线性积分算子 Q(g,f)(x)（含单位球面 S^{N−1} 上的积分与 x',y' 的中点-半径参数化），推导其 Fourier 变换的显式公式 | 调和分析 / 算子 | 球面积分与 Fourier 变换交换、变量替换、B(‖η‖, ξ·σ/|ξ|) 的 Fourier 变换 | 4 |

**卷 C：Computational and Applied Mathematics（计算与应用数学）** — 6 题，3 页，4310 字符，小问标记 44 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | A 非奇异，考虑秩 1 扰动 Â=A+uv^T：(a) 推导 Â 可逆的充要条件；(b) 若 Az=b 可用 O(n) 算出，设计 O(n) 算法解 Âx=b 并论证 | 数值线性代数 | Sherman–Morrison 公式、Woodbury、稳定性 | 3 |
| 2 | 积分 ∫_0^∞ f（f'(0)≠0，尾部衰减 x^{−1−α}）：(a) 复合梯形法误差渐近式；(b) L 如何随 n 增长以最优；(c) 变量替换 x=L(1+y)/(1−y) 后的误差；(d) 依 α 比较「截断定义域」与「变量替换」 | 数值积分 | Euler–Maclaurin、端点奇性、变换后的解析性、收敛率比较 | 4 |
| 3 | 第一类 Chebyshev 多项式 T_n 与第二类 U_n：(a) 推导 U_n 的递推；(b) 证 U_n 关于权 1/√(1−x²) 正交；(c) 导出 2 点 Gauss–Chebyshev 求积 | 数值逼近 | 三项递推、正交多项式、Gauss 求积（n 点精确到 2n−1 次） | 2 |
| 4 | −(a(x)u')'=f，u(0)=u(1)=0，a 已知但 a' 不可得：(a) 用等距网格有限差分离散，给出三对角矩阵元素；(b) 用已有信息给出（越小越好的）包含全部特征值的圆盘 | 数值 PDE / 特征值定位 | 二阶中心差分、Gershgorin 圆盘定理 | 3 |
| 5 | (a) 验证 u_t=u_{xxx} 作为初值问题适定；(b) 对给定 leapfrog 型显式格式判定稳定性条件 | 数值 PDE | 适定性（Fourier 乘子增长）、von Neumann 稳定性分析 | 3 |
| 6 | 周期边界扩散方程 v_t=μv_{xx}，中心差分 L：(a) L 的精度阶；(b) 给出 Forward Euler 与 Crank–Nicolson 的 Fourier 模态更新（含 l=0）；(c) 初值 φ(mΔx)=(−1)^m 时给出显式解；(d) 两法的稳定性约束 k ≤ F(h,μ) | 数值 PDE | 二阶中心差分、DFT 对角化、von Neumann 分析、无条件/条件稳定 | 4 |

**卷 D：Geometry and Topology（几何与拓扑）** — 6 题，1 页，2303 字符，小问标记仅 9 个（本卷风格：**几乎不设小问，每题一问到底**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | (i) 是否存在 f:S^{2n}→CP^n 使 deg f≠0；(ii) 是否存在 f:CP^n→S^{2n} 使 deg f≠0 | 代数拓扑 | 上同调环 H*(CP^n)=Z[x]/(x^{n+1})、映射度、Hopf 不变量 | 3 |
| 2 | 证明 R³ 中的闭嵌入曲面不可能是极小曲面（κ1+κ2=0） | 微分几何 | Gauss 映射、紧致性、极值原理、平均曲率与有界性 | 3 |
| 3 | M 为闭单连通 6 维流形，H₂(M)=Z₂ ⟹ χ(M)≠−1 | 代数拓扑 | Poincaré 对偶、Betti 数奇偶性、Euler 示性数模 2 | 4 |
| 4 | 证明标量曲率 S_p = (1/ω_{n−1})∮_{S^{n−1}} Ric_p(V,V) dS | 黎曼几何 | Ricci 张量的迹、单位球面上的平均、极坐标积分 | 2 |
| 5 | S^n（n≥2）上有限群 G 自由作用：(i) 计算 π_i(S^n/G)，0≤i≤n；(ii) n 偶 ⟹ G≅Z₂；(iii) n 奇 ⟹ G 不同构于 Z_p×Z_p | 代数拓扑 / 群作用 | 覆叠空间同伦序列、球面同调、Lefschetz 不动点、群作用的度 | 4 |
| 6 | 度规族 g_t 与特征对 (f_t,λ_t)，Δ_{g_t}f_t=λ_t f_t：(i) 证 λ̇ 是 Π∘Δ′:V_{λ0}→V_{λ0} 的特征值；(ii) 若 g_t=φ_t*g_0 则 λ̇=0 | 黎曼几何 / 谱几何 | 特征值的一阶变分公式、Rayleigh 商、等距不变性 | 4 |

**卷 E：Mathematical Physics（数学物理）** — 6 题，4 页，6715 字符，小问标记 36 个（**卷面最长**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 经典力学：吸引中心势 V(r)=αr^k（k,α 同号）(a) 极坐标 Lagrangian；(b) 用角动量守恒化为一维有效问题；(c) 圆轨道半径与周期；(d) 哪些 k 使圆轨道稳定；(e) 稳定时小振动周期与轨道闭合条件；(f) 消去时间得到轨道微分方程 | 经典力学 | 有效势、Binet 方程、Bertrand 定理、线性稳定性分析 | 3 |
| 2 | 量子力学：一维谐振子初始处于基态，受瞬态扰动 ΔH=F(t)x：(a) 用升降算符写 H 并解 Heisenberg 方程，给出 a_{+∞} 与 a_{−∞} 的关系；(b) 求跃迁概率 |c_n|²；(c) 末态能量期望；(d) F(t)=F_0 e^{−t²/(2σ_t²)} 时，短脉冲 σ_tω≪1 下保证基态损失 <1% 的最大 η，及长脉冲下损失被抑制的论证 | 量子力学 | 位移算符、Heisenberg 绘景、相干态、sudden/adiabatic 极限 | 4 |
| 3 | 电动力学：欧姆金属（σ 大、μ=1）(a) 导出阻尼波解 H=H_c e^{−iωt+ik_c z}，k_c=(1+i)√(σω)/√2/c；(b) 用 Maxwell 方程给出 E_c 与 H_c 关系；(c) 理想导体（σ=∞）反射波振幅相等且极化反转，用边界条件解释；(d) 有限大 σ 时求金属内场到 ω/σ 的领头阶 | 电动力学 | Maxwell 方程组、复波数、集肤深度、边界条件、极化反转 | 3 |
| 4 | 统计力学：平均场 Ising，H_MF=(1/2)NJm²−(Jm+h)∑σ_i：(a) 求配分函数与自由能；(b) 导出磁化约束方程并图解 h=0 情形，讨论解的物理意义、找出临界温度 T_c；(c) 在 β(Jm+h)≪1 下求 m、比热、磁化率随 t=(T−T_c)/T_c 的依赖，定出临界指数 α_c,β_c,γ_c | 统计力学 | 平均场近似、自洽方程、Landau 理论、临界指数 | 3 |
| 5 | 广义相对论：de Sitter 空间 dS_n 由 −(x⁰)²+∑(x^i)²=α² 定义，取静态坐标 (a) 证其为局部坐标；(b) 计算诱导度规；(c) n=3 时求 Ricci 张量与标量曲率，判断是否 Einstein 度规；(d) ∂_t 与 ∂_φ 是否为 Killing 矢量场 | 广义相对论 | 诱导度规、Christoffel 符号、Ricci 张量、Einstein 流形、Killing 方程 | 4 |
| 6 | 量子场论：Yukawa 理论 Lagrangian（实标量 φ 与 Dirac 旋量 ψ）(a) 找出 φ 自能 1-loop 图的所有发散与抵消项；(b) 找出 ψ 自能的发散与抵消项；(c) 是否存在不可重整的发散 | 量子场论 | 1-loop 计算、维数正规化、抵消项、可重整性判据、手征 γ⁵ | 4 |

**卷 F：Probability and Statistics（概率统计）** — 5 题，2 页，3992 字符，小问标记 10 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | r 个玩家分别持有 n_i 单位，每局随机选两人对战、赢者从输者得 1 单位，破产者淘汰；对 S⊆{1,…,r}，X(S) 为只涉及 S 中成员的局数。问 E[X(S)] 是否依赖选人机制？不依赖则算出，依赖则给出两个机制反例 | 概率 / 随机过程 | 鞅与可选停止、势函数、吸收马尔可夫链、机制无关性 | 4 |
| 2 | 独立 Bernoulli X_i（P=1 取 p，=−1 取 q），S_n=∑X_i，M=sup_{n≥1}(S_n/n)：(a) 求 P(M=0)；(b) 证 P(p−q<M≤1)=1；问对有理数 x∈(p−q,1] 是否 P(M=x)>0，若否找出概率为 0 的点 | 随机游走 | 强大数定律、游走的上穿概率、Chung–Feller、可数状态 | 5 |
| 3 | X~U[0,1]，N_{m,k} 为 X^k 小数点后第 m 位数字：(a) 求 lim_m P(N_{m,m}=i)；(b) 设 k(m)>1，求使 lim_m P(N_{m,k(m)}=i)=1/10 的充要条件 | 概率 / 数论概率 | 小数展开的等分布、特征函数、进位分析 | 4 |
| 4 | 指数族 GLM：f(y_i;θ_i)=exp{θ_i y_i − b(θ_i)}，θ_i=x_i^Tβ；在假设 (I)(II)（Hessian 特征值上下界、局部二次逼近）下证明包含全部重要协变量的模型类上 max_{α∈A}‖β̂_α−β(α)‖ = O_p(n^{−1/3}) | 数理统计 / 渐近理论 | MLE 的局部二次展开、Hessian 谱界、概率集中、模型误指定 | 5 |
| 5 | r_n×c_n 矩阵样本 {X_{ij}} i.i.d. ~F（连续密度 f），β̂_n=min_j max_i X_{ij}：(a) 使 β（中位数）也为 β̂_n 的中位数的 r_n 条件；(b) 在该条件下证明 r_n(β̂_n−β) 依分布收敛并给出极限分布 | 数理统计 / 极值 | 次序统计量、极值分布、中位数无偏性、分布收敛 | 4 |

### 1.2 2025 年（6 卷，33 题，22991 字符）

**卷 A：Algebra and Number Theory** — 5 题，2 页，3629 字符，小问标记 21 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | F 特征 ≠2：证明 F 有 Galois 群为 Z/2×Z/2 的扩张 ⟺ [F*:F*²]>2；并证明这类扩张恰为形如 X⁴+aX²+b（b∈F*²）的不可约多项式的分裂域 | 域论 / Galois 理论 | Kummer 理论、二次扩张、F*/(F*)²、群同态分类 | 3 |
| 2 | p 素数，e,f≥1，G=⟨σ,τ | σ^f=1, τ^e=1, στσ^{−1}=τ^p⟩：(1) 证 G 存在唯一 ⟺ p^f≡1 (mod e)；(2) A=F_{p^f} 上 G 以 σ(a)=a^p、τ(a)=ηa 作用，证三个条件等价：C⊗_{F_p}A 不可约（绝对不可约）、A 不可约、p 在 (Z/eZ)^× 中的阶为 f | 有限群 / 有限域表示 | 半直积、Frobenius 自同构、绝对不可约性、Brauer 群 / Schur 指标 | 4 |
| 3 | (1) R=k[T] 在素理想 (T) 的局部化，α_i∈k\{0} 互异，证 1/(T−α_i)（1≤i≤n）构成 k-向量空间 R/(T^n) 的一组基；(2) A⊂k 无限，K/k 有限，V⊂K(T) 由 1/(T−α)（α∈A）张成，β∈K\A 定义赋值 ord_β，Ω={ord_β(f): f∈V}，u_n=#{Ω∩{0,…,n−1}}，证 u_n/n ≥ 1/[K:k] | 交换代数 / 赋值论 | 局部化、部分分式、赋值、维数计数、Riemann–Roch 式下界 | 4 |
| 4 | E/F 为 p-adic 局部域的有限 Galois 扩张，Γ=Gal：(1) 非分歧时 α:O_E⊗_{O_F}O_E→∏_{γ∈Γ}O_E，c⊗x↦(cγ(x))_γ 是同构；(2) 半线性 Γ-模 M 上 O_E⊗_{O_F}M^Γ→M 是同构；(3) 证 Φ_{E/F}:M↦O_E⊗_{O_F}M 是 Mod_{O_F} 到 Mod^Γ_{O_E} 的范畴等价；(4) 分歧时该函子是否仍为等价 | 局部域 / 下降理论 | 正规基定理、Galois 下降、Hilbert 90、Galois 上同调 H¹=0 | 5 |
| 5 | f(X)=X⁵−X+1∈Q[X]，判别式 4⁴a⁵+5⁵b⁴：(1) 证不可约；(2) 定出所有分歧有限素数与惯性群阶；(3) 证 E/Q(√D) 在所有有限素处非分歧、在阿基米德素处分歧；(4) 证 Gal(E/Q) 由其惯性子群生成；(5) 证 Gal(E/Q)≅S₅、Gal(E/Q(√D))≅A₅ | 代数数论 | Dedekind 分解定理、判别式、Frobenius、惯性群、非分歧扩张、Galois 群计算 | 5 |

**卷 B：Analysis and Differential Equations** — 6 题，2 页，2621 字符

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 求 r³R'''+2r²R''−rR'+R=2025（r>1）满足 R(1)=2025, R'(1)=0, R''(1)=1 的解 R(r) | 常微分方程 | Euler（等维）方程、指标方程、重根、待定特解 | 2 |
| 2 | (1) 证 n≥3 时存在 C 使 ∫_{R^n} u²/|x|² ≤ C∫|∇u|²，∀u∈H¹；(2) 证最优常数 C=4/(n−2)² | 泛函分析 / 变分 | Hardy 不等式、加权 Sobolev、最优常数与 Euler–Lagrange 方程、u=|x|^{−(n−2)/2} 型极值函数 | 3 |
| 3 | (1) 圆环上次调和函数 u 的 M(r)=max_{|x|=r}u，证 log-凸插值不等式 M(r) ≤ [M(r1)(log r2−log r)+M(r2)(log r−log r1)]/log(r2/r1)；(2) 若 u 在 R²\{0} 上次调和且上有界，证 u 为常数 | 位势论 | 次调和函数、极大值原理、Liouville 定理 | 3 |
| 4 | 光滑闭曲线 γ:S¹→R² 的度 d(γ)=(1/2π)∮(xdy−ydx)/(x²+y²)：(1) 证 d(γ)=(1/2πi)∮dz/z 从而是整数；(2) 对 γ(s)=re^{2πins} 计算 d(γ)；(3) 证 γ0 与 γ1 正则同伦 ⟺ 两者度相等 | 代数拓扑 / 几何 | 绕数、同伦提升、Whitney–Graustein 定理 | 4 |
| 5 | 设 A、B 是度量空间 (X,d) 中两个不相交闭集，[a,b] 为给定闭区间，证存在连续 f:X→[a,b] 使 f(A)={a}、f(B)={b} | 一般拓扑 | Urysohn 引理、距离函数构造 f=d(x,A)/(d(x,A)+d(x,B)) | 2 |
| 6 | 定义 ‖f‖_BMO 与 BMO(R^n)：证 (1) 只是半范数不是范数；(2) L^∞⊂BMO 且 ‖f‖_BMO≤2‖f‖_∞；(3) 若存在 A>0 使每个方体 Q 存在常数 c_Q 满足 sup_Q (1/|Q|)∫_Q|f−c_Q| ≤ A，则 f∈BMO 且 ‖f‖_BMO≤2A；(4) L^∞ 是 BMO 的真子空间 | 调和分析 | BMO 定义与等价刻画、John–Nirenberg、log|x|∈BMO\L^∞ | 3 |

**卷 C：Computational and Applied Mathematics** — 6 题，3 页，3551 字符，小问标记 18 个
> ⚠️ 本卷抽取文本含控制字符残留（0x00/0x01/0x10–0x13），矩阵圆括号出现空洞，详见第 5 节。

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 多点迭代 x_{k+1}=x_k−α f(x_k)/f'(x_k−β f(x_k)/f'(x_k))，求使收敛阶最高的 α、β（f 有单根 ξ） | 数值分析 / 迭代法 | 局部误差展开、收敛阶定义、Taylor 匹配 | 4 |
| 2 | 计算 A^{−1} 的谱半径，其中 A 为 8×8 三对角矩阵（对角线为 0、上下副对角线为 1，即 8 点路径图 P₈ 的邻接矩阵） | 数值线性代数 | 路径图邻接矩阵特征值 2cos(kπ/9)、谱半径 = 1/min|λ| = 1/(2cos(π/9)) ≈ 0.5321 | 3 |
| 3 | 连带 Legendre 函数 P_k^m=(−1)^m(1−x²)^{m/2} d^mP_k/dx^m：(a) 证插值方程组（用 P_k¹(x_i)）在 x_i≠±1 互异时非奇异；(b) 导出 L² 逼近的最小二乘（正规）方程组并说明非奇异；(c) 证系数矩阵 M_{k,j}=0 当 k+j 为奇数 | 数值逼近 | 正交多项式、Sturm–Liouville、Chebyshev 系统（Haar 条件）、奇偶性 | 4 |
| 4 | 给定 y_1,…,y_n∈R^m，V=span{y_j}，如何求 ℓ≤dim V 个标准正交向量 ψ_i 最小化投影残差平方和 J | 数值线性代数 / 降维 | SVD、Eckart–Young–Mirsky 定理、PCA、Rayleigh 商 | 3 |
| 5 | u_t+u=u_{xx} 的 θ-格式：(a) 在 A(θ)Δt ≤ Δx²/(2+Δx²) 下证 ‖U^m‖_{ℓ^∞} ≤ ((1−(1−θ)Δt)/(1+θΔt))^m‖U⁰‖_{ℓ^∞}，定出 A(θ)；(b) θ∈[1/2,1] 时 ℓ² 无条件稳定；θ∈[0,1/2) 时需 B(θ)Δt ≤ 2Δx²/(4+Δx²)，定出 B(θ) | 数值 PDE | 最大原理、von Neumann 分析、θ-方法的无条件/条件稳定 | 4 |
| 6 | 刚性系统 y'=(−1000y₁+999y₂, −y₂)，y(0)=(2,1)^T：(a) 求精确解；(b) 显式 Euler 的绝对稳定域并证 h>0.002 时发散；(c) 隐式 Euler 任意 h 无条件稳定；(d) 梯形法则的稳定性分析 | 数值 ODE | 刚性、绝对稳定域、A-稳定 / L-稳定、放大因子 | 3 |

**卷 D：Geometry and Topology** — 6 题，1 页，1983 字符（**三年中最短的一份卷子**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 对 n>1：(i) S^{2n}×S^{2n} 的切丛是否平凡；(ii) S^{2n}×S^{2n−1} 的切丛是否平凡 | 微分拓扑 | Euler 示性数、向量场、切丛的 Whitney 和、Pontryagin/Euler 类 | 3 |
| 2 | SU(2)≅S³，X1,X2,X3 为 Lie 代数基；Berger 度规 g_ε 使 ε^{−1}X1, X2, X3 为标准正交：(i) 证 ∇_{X_i}X_i=0（i=1,2,3）；(ii) 计算 g_ε 的标量曲率 | 黎曼几何 | Levi-Civita 联络、Koszul 公式、左不变标架、Berger 球面、标量曲率 | 3 |
| 3 | U(n)：(i) 计算 π₂(U(n))、π₃(U(n))；(ii) 证 det:U(n)→S¹ 在基本群上诱导同构 | 代数拓扑 / Lie 群 | 纤维化 U(n−1)→U(n)→S^{2n−1}、同伦长正合列、Bott 周期性 | 3 |
| 4 | 证明 CP² 不能浸入 R⁶ | 微分拓扑 | Whitney 对偶、法丛、示性类、Chern 类、浸入的维数限制 | 5 |
| 5 | (M,g) 二维闭定向，K 为 Gauss 曲率，g̃=e^{2u}g：(i) 证 Δu−K+K̃e^{2u}=0；(ii) 若 χ(M)=0，证 K̃≡0 或 ∮_M K̃e^{2f}dVol_g<0，其中 f 满足 Δf=K | 微分几何 / 共形几何 | 共形度规的 Gauss 方程、Laplace–Beltrami、可解性、Gauss–Bonnet | 4 |
| 6 | (i) CP^n 上是否存在无不动点的自同胚（构造或证明不存在）；(ii) CP²×CP² 上是否存在 | 代数拓扑 | Lefschetz 不动点定理、上同调环、Lefschetz 数计算 | 4 |

**卷 E：Mathematical Physics** — 6 题，4 页，8122 字符（**三年中单卷字符数最多**），小问标记 31 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 珠（质量 m）在半径 R 的圆环上无摩擦滑动，圆环以角速度 ω 绕竖轴旋转：(1) Lagrangian 与运动方程；(2) 守恒量与 Hamiltonian，判断其是否等于固定系能量、固定系能量是否守恒；(3) 求临界角速度 Ω、ω<Ω 与 ω>Ω 时的稳定平衡位置；(4) 计算稳定平衡点附近的小振动频率 | 经典力学 | 约束系统、广义能量与 Hamiltonian 的区别、有效势、稳定性判据、线性化 | 3 |
| 2 | 横向剖面 E₀(x,y) 的高斯波包沿 z 传播：(1) 忽略 E₀ 的导数时验证 (3) 是 Maxwell 方程解（ω=ck）；(2) 计算单位长度时间平均能量 ⟨U⟩；(3) 在 kσ≫1 下求梯度一阶修正 E^{(1)}；(4) 用平面波叠加定性解释并精确重现该修正；(5) 求 z 方向时间平均角动量 ⟨L_z⟩ 的最低非平凡阶；(6) 求 ⟨L_z⟩/⟨U⟩ 并用光子解释 | 电动力学 / 光学 | Maxwell 方程、傍轴近似、Gauss 积分、角动量、自旋-轨道（光子自旋） | 4 |
| 3 | H=p²/2m+½mω²x²−qEx=H₀−qEx：(1) 写成 H=e^{−A}H₀e^A+B 并显式确定 A、B，说明谱是 H₀ 的平移；(2) 用 a、a† 表达 A，求 t=0 处于 H₀ 基态时在时刻 t 测得 H 基态的概率；(3) 求 t=0 在 H₀ 基态且时刻 t 仍在 H₀ 基态的概率及该概率为 1 的时刻；(4) 求时刻 t 处于 H₀ 第一激发态的概率；(5) 用 a、a† 表达偶极矩 d=qx 并求其期望 | 量子力学 | 位移算符、相干态、对易关系、Weyl 群、时间演化算符 | 4 |
| 4 | 三角形上的 Ising 模型 E=−J(σ₁σ₂+σ₂σ₃+σ₃σ₁)−h(σ₁+σ₂+σ₃)：(1) 计算配分函数；(2) 自由能与熵；(3) h=0 时的比热及其在 T≪J 与 T≫J 的极限；(4) T≪J 给定 h,T 下的磁化 M=⟨σ⟩ 与磁化率 χ；T≪J 时的行为；(5) T≪J 时磁化涨落 ⟨(σ−M)²⟩ | 统计力学 | 精确可解模型、配分函数求和、涨落-耗散、低/高温展开 | 3 |
| 5 | 双黑洞引力波（黑洞视为质点）：(1) 由给定的 h₊、h_× 公式导出圆轨道双星（质量 m₁,m₂、间距 r）的 h₊、h_× 及引力波频率 f；(2) 求平均辐射功率 P；(3) 给定初始频率 f₀，求 f(t)；(4) 求并合时间 T_C；(5) m₁=m₂=10M⊙ 时估计能在宇宙年龄内并合的最大初始间距 r₀（au） | 广义相对论 / 天体物理 | 四极辐射公式、开普勒第三定律、能量损失率、轨道衰减、量纲估计 | 4 |
| 6 | 共形标量场（c=ℏ=1）：(1) 无质量标量在 Minkowski 中刚性标度 η→Ω²η 与 φ→Ω^Δφ 下不变，求 Δ；(2) 局部标度下求作用量的变换，是否能通过选 Δ 保持不变；(3) 给定 g→Ω²g 求 R̃；(4) 加 ξRφ² 项恢复不变性，求 ξ；(5) 在 ds²=(−dτ²+dx²)/(Hτ)² 中证共形标量等价于有质量标量并求 m | 量子场论 / 共形场论 | Weyl 变换、共形耦合、Ricci 标量的变换律、de Sitter 空间、标度不变性 | 5 |

**卷 F：Probability and Statistics** — 4 题，2 页，3085 字符（**三年中最少题量的一份卷子**）
> ⚠️ 本卷抽取文本含控制字符残留（0x00/0x01/0x12/0x13）。

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 单观测 X~N(µ,σ²)，µ、σ² 均未知，对 µ 构造 CI(X;c1,c2)（X>0 与 X<0 分别对应不同取向）：(1) 求该 CI 的覆盖概率；(2) 给定由分布函数 F(x;b1,b2) 生成的随机化 CI，证明存在由 G(c1,c2) 决定的随机化 CI 满足题给的 minimax 性质与长度期望等式 | 数理统计 | 覆盖概率的精确计算、随机化区间、minimax 最优性、Neyman–Pearson 式对偶 | 4 |
| 2 | 单次观测 r 来自总体 1 或 2（各 1/2 概率），ν 为无界且期望有限之函数，判定规则 φ:R→[0,1] 一一对应。问：对满足 E₁ν(X)>E₂ν(Y) 的任意密度，选对总体 1 的概率是否总 ≥1/2？若是给出证明，若否对任意给定 φ 构造 p₁、p₂ 使 E₁ν(X)>E₂ν(Y) 但选对概率 <1/2 | 数理统计 / 决策论 | 假设检验、似然比、选择规则的相合性、反例构造 | 4 |
| 3 | 设 n≥2。证明存在独立随机变量 X₁,…,X_n=X₀ 使得 P(X_{k−1}<X_k)=1−1/(4cos²(π/(n+2))) 对所有 1≤k≤n 成立 | 概率 / 构造 | 递推构造、三角恒等式、循环结构、可能用到特征多项式/递推序列 | 5 |
| 4 | 单因素 ANOVA：Y_{ij}=β_j+R_{ij}，i=1..n/p，j=1..p，{R_{ij}} i.i.d.，真值 β_j=0；β̂_j 为 ψ 估计方程 ∑_i ψ(Y_{ij}−β̂_j)=0 的解，ψ 有界、ψ' 有界且在 0 附近连续，Eψ(R)=0、Eψ'(R)=d≠0，p log p/n→0。证明存在解与常数 B>0 使 P(max_j|β̂_j| ≥ (B^{−1} p log n/n)^{1/2}) ≤ 2p/n → 0 | 数理统计 / 稳健统计 | M-估计、估计方程、经验过程、集中不等式、Bonferroni | 5 |

### 1.3 2026 年（6 卷，34 题，21995 字符 — **三年中总字符最少，但题量最多**）

**卷 A：Algebra and Number Theory** — 5 题，2 页，2604 字符（**三年中字符数最少的一份代数卷**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | p 素数，gcd(n,p)=1，Γ₀(p)={γ∈SL₂(Z): c≡0 mod p}，α=diag(1,n)。证明双陪集 Γ₀(p)αΓ₀(p) 分解为右陪集的并，指标集 R={(a b; 0 d): ad=n, a>0, 0≤b<d, gcd(a,b,d)=1} | 模形式 / 群论 | Hecke 算子、双陪集分解、Smith 标准形、陪集代表元计数 | 4 |
| 2 | F_p 上 y²=x³+1 的解数 N_p：(1) p=3 或 p≡2 (mod 3) 时 N_p=p；(2) 证 N(X^m=a)=∑_{χ∈X_m}χ(a)；(3) p≡1 (mod 3) 时仍证 |N_p−p|≤2√p（用 Jacobi 和 |J(χ,µ)|=√p） | 代数数论 / 特征和 | 特征标与 Jacobi 和、Hasse 界、椭圆曲线上的点计数、Weil 猜想一维情形 | 4 |
| 3 | K 为数域，O_K̄ 为代数整数环，a,b∈O_K̄。证明等价：(1) (a,b)=O_K（互素）；(2) 存在 u∈O_K̄ 使 au+b∈O_K̄^× | 交换代数 / 数论 | 理想互素、局部化、Bézout 型论证、单位群 | 3 |
| 4 | a∈Z 无平方因子，α=∛a，f(x)=x³−a，Disc(f)=−27a²，K=Q(α)。证明 O_K 的整基为 {1,α,α²}（当 a≢±1 mod 9），或 {1, α, (1±α+α²)/3}（当 a≡±1 mod 9） | 代数数论 | 判别式与整基、Dedekind 判据、三次域、指数（index）计算 | 4 |
| 5 | K/Q_p 有限扩张：(1) 对固定 d≥1，K 只有有限多个 d 次非同构有限扩张；(2) 若 (d,p)=1 且 K 有 d 次全分歧 Galois 扩张 L/K，证 K 含 d 次本原单位根且 L/K 必循环；(3) 在 (d,p)=1 下计算 K 的 d 次非同构全分歧 Galois 扩张的个数 | 局部域 / 分歧理论 | Krasner 引理、Hensel 引理、局部类域论、全分歧扩张的分类、Eisenstein 多项式 | 5 |

**卷 B：Analysis and Differential Equations** — 5 题，2 页，2724 字符

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 定义 I_n=(1/n!)∫_{−π/2}^{π/2}(π²/4−t²)^n cos t dt：(a) 证递推 I_{n+1}=2(2n+1)I_n−π²I_{n−1}；(b) 证 π² 不是有理数 | 特殊函数 / 数论 | 分部积分、递推关系、Beukers 型无理证明（I_n→0 与整性） | 4 |
| 2 | 矩阵指数：(a) 若 [X,Y]=0 则 e^Xe^Y=e^{X+Y}=e^Ye^X；(b) 若 [X,[X,Y]]=[Y,[X,Y]]=0 则 e^Xe^Y=e^{X+Y+½[X,Y]} | 线性代数 / Lie 理论 | 矩阵指数级数、BCH 公式的特殊情形、二项式重排 | 3 |
| 3 | f 在 |z|<R 上光滑，0<ρ<R，g(z)=(1/2πi)∬_{|ζ|≤ρ} f(ζ)/(ζ−z) dζ∧dζ̄，证明 ∂g/∂z̄=f(z)（|z|<ρ） | 复分析 | Cauchy–Green（Pompeiu）公式、广义 Cauchy 积分、∂̄ 算子 | 3 |
| 4 | C([0,1]) 赋 L^∞ 范数是 Banach 空间，P 为由多项式构成的闭线性子空间，证明 dim P<∞ | 泛函分析 | 有限维子空间刻画、Arzelà–Ascoli / Baer 判据、等度连续性、Weierstrass 逼近的对照 | 3 |
| 5 | 单位区间周期热方程：(1) 写出 L²([0,1]) 的正交基并证 f↦f''（定义域 F={f∈H²: f(0)=f(1), f'(0)=f'(1)}）自伴；(2) 求基本解 h(t,x,y) 并验证 (a)(b)；(3) 求 h 的最大值点、t→∞ 行为，并证 A t^{−1/2}e^{−Bd(x,y)²/t} ≤ h ≤ C t^{−1/2}e^{−Dd(x,y)²/t}（d 为环面距离） | 偏微分方程 | 热半群、特征函数展开、自伴算子谱定理、Poisson 求和公式、Gauss 型上下界估计 | 4 |

**卷 C：Computational and Applied Mathematics** — 6 题，2 页，4413 字符，小问标记 46 个（**三年中单卷小问最多**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | αu_t+βu_x−γu_{xx}=f，零初值、零边界，α>0,β∈R,γ>0：(a) 用 P1 有限元（空间）与隐式 Euler（时间）写全离散变分形式；(b) 证 L² 稳定性 ‖u_h^n‖≤C‖f‖（C 与 h,τ,n 无关）；(c) 写出代数线性方程组 | 有限元 / 数值 PDE | 变分形式、P1 基函数、隐式 Euler、能量法稳定性、Galerkin 正交性 | 4 |
| 2 | J(u)=∫_Ω(½|∇u|²+¼u⁴−fu)，Ω⊂R^d (d≤3)：(a) 求 Fréchet 梯度与 Hessian，证 J 严格凸；(b) 写 Newton 法并证局部二阶收敛 ‖u_{k+1}−u*‖_{H¹} ≤ C‖u_k−u*‖²；(c) 证 BFGS 更新（满足割线方程）在 B_k 正定时良定义 | 变分 / 优化 | 变分法、单调性、Hessian 的一致正定性、Newton 收敛定理、BFGS 割线条件 | 4 |
| 3 | 单步法 x_{n+1}=x_n+(1−b)hf(t_n,x_n)+bhf(t_{n+1},x_{n+1})：(a) 求使局部截断误差为 O(h³) 的 b；(b) 用于 x'=λx 时求 g 使 x_n=g(hλ)^n x₀；(c) 确定使方法 A-稳定的 b 值 | 数值 ODE | 局部截断误差展开、放大函数（稳定性函数）、A-稳定（左半平面 |g|≤1） | 3 |
| 4 | 位移 QR 迭代 A_n−σ_n I=Q_nR_n，A_{n+1}=R_nQ_n+σ_n I：(a) 若无 σ_n 是 A 的特征值，证 {A_n},{Q_n},{R_n} 唯一确定且 A_{n+1}=Q_n^T A_n Q_n=R_n A_n R_n^{−1}；(b) A 为对称 2×2、特征值 λ1,λ2，取 σ0=λ1，求 A1；(c) 证 Q̂_{k+1}R̂_{k+1}=∏_{i=0}^{k}(A−σ_i I) | 数值线性代数 | QR 分解唯一性、相似变换、位移策略、收缩（deflation） | 4 |
| 5 | A∈R^{n×n}，σ_i(A) 为奇异值，x 满足 Ax=x 称为不动点：(a) 若 σ1(A)≤1，证 A 的每个不动点也是 A^T 的不动点；(b) 用 A=[[1,1],[0,0]] 说明不假设 σ1≤1 时断言不真；(c) 若 AA^T=A^TA，证结论成立 | 矩阵分析 | 奇异值分解、正交投影几何、正规矩阵、谱半径与奇异值关系 | 3 |
| 6 | 次微分（n≥2）：(a) f(x)=max_i x_i，计算 ∂f(0)；(b) g(x)=max_i x_i+δ_{R^n_+}(x)，证 ∂g(0)=∂f(0)−R^n_+ | 凸分析 | 次微分、凸函数的加法法则、指示函数、法锥 | 3 |

**卷 D：Geometry and Topology** — 6 题，2 页，3071 字符，小问标记 22 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | S⊂R³ 为无边界光滑正则曲面，N 为 Gauss 映射，{A_ε} 收缩到 p。证明 |K(p)| = lim_{ε→0} Area(N(A_ε))/Area(A_ε) | 微分几何 | Gauss 映射的 Jacobian、第二基本形式、Gauss 曲率的几何意义 | 3 |
| 2 | (M²,g) 紧、定向、带非空边界，K_g≥0、k_g≥1、Length(∂M)≥2π，证明 (M,g) 等距于带标准欧氏度规的单位圆盘 (D²(1), g_flat) | 微分几何 | Gauss–Bonnet 定理、测地曲率、等周型刚性论证 | 4 |
| 3 | G 为连通 n 维 Lie 群带双不变度规：(1) 证截面曲率非负；(2) 若 g 的中心 z(g)={0}，证 G 紧；(3) 若 G 单连通，证 G≅G'×R^k（G' 单连通紧、其 Lie 代数中心平凡） | Lie 群 / 黎曼几何 | Cartan–Schouten 定理、Killing 型、紧 Lie 群的结构、双不变度规的曲率公式 | 4 |
| 4 | S^{2026}⊂R^{2027}：(1) 计算切丛的 Z₂ Euler 类；(2) 计算单位切球丛 US^{2026} 的 Poincaré 级数（Z₂ 系数）；(3) 对 p,q 非对径点，考虑能量泛函 E 下的路径空间 Ω(S^{2026};p,q)：(a) 求 E 的全部临界点；(b) 求 Morse 指标 λ(E,γ)；(c) 确定基于环路空间 Ω(S^{2026},p) 的同伦型；(d) 计算 Ω(S^{2026},p) 与自由环路空间 ΛS^{2026} 的 Poincaré 级数 | 代数拓扑 / Morse 理论 | Gysin 序列、Euler 类、Morse 指标定理、测地线的指标、环路空间的同伦分解、Poincaré 级数 | 5 |
| 5 | M^n 连通、闭、光滑、aspherical（万有覆叠可缩）：(1) 证万有覆叠非紧；(2) 证 π₁(M) 的每个非平凡元有无限阶 | 代数拓扑 / 几何群论 | 覆叠空间理论、度规提升、Cartan–Hadamard、有限群作用的 Lefschetz 论证 | 3 |
| 6 | (M^n,g) 完备黎曼流形 n≥2，若存在 ε>1/4 使 Ric_g(x) ≥ ε(n−1)r(p,x)^{−2}（r 充分大），(1) 证 M 必紧；(2) 举例说明 ε≤1/4 时结论失效 | 黎曼几何 | 体积比较、Raychaudhuri 方程、Laplacian 比较、Ambrosio–Gigli–Savaré 型论证 | 5 |

**卷 E：Mathematical Physics** — 6 题，3 页，6082 字符，小问标记 19 个

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | 滑动摆（质量 M 沿水平杆无摩擦滑动，经无质量杆长 l 连接 m）：(1) 求 x-z 面内小振动角频率；(2) 滑动圆锥摆（M 在 x-y 面内滑动），给定 θ 求圆运动角频率并检验小 θ 极限；(3) 倒立滑动摆从 θ=π 静止下落，M→∞ 时求张力 T 为零的角度；(4) 一般 M,m 时求 θ=π/2 与 θ=π 处的张力 | 经典力学 | 拉格朗日力学、约束反力、有效势、椭圆曲率半径 | 3 |
| 2 | 两个相同圆形线圈（半径 a，间距 h）载 I(t)=I₀cos(ωt)，轴沿 z：(1) 低频下用磁静态近似，在轴线附近与 z≈0 处证明 B_z≃B₀+½β₂(z²−ρ²/2)、B_ρ≃−½β₂zρ；(2) 求近轴磁场到 z、ρ 的二次阶，描述 h=a 情形；(3) 求 z=0 近轴电场到频率与 ρ 的最低非平凡阶；(4) (a) 估计有限频率修正的大小；(b) 估计磁静态近似在轴上失效的 z | 电动力学 | 磁静态近似、Biot–Savart、Taylor 展开、∇·B=0、Faraday 定律、矢量势 | 4 |
| 3 | 一维粒子散射于 U(x)=β[δ(x)+δ(x−a)]：(1) 能否无反射穿透？(2) 若能，对应的动能值？三维两 δ 势 U(r⃗)=β₃(δ³(r⃗−r⃗₁)+δ³(r⃗−r⃗₂))，每个中心 S 波散射长度 a<0：(3) 写出每个中心附近的 S 波束缚波函数，验证 a<0 时不支持束缚态；(4) 双中心势能否支持束缚态？条件为何？ | 量子力学 | δ 势的匹配条件、透射共振、散射长度、束缚态与散射长度的符号判据 | 4 |
| 4 | (1) 写出液-气共存曲线上两相热力学平衡的条件；(2) 利用该条件并考虑相变的熵变，推导共存曲线上蒸气压的关系式 | 热力学 | 化学势相等、Clausius–Clapeyron 方程、潜热 | 2 |
| 5 | φ⁴ 模型 L=−½∂_μφ∂^μφ−½m²φ²−(1/4!)gφ⁴：(1) 写出动量空间传播子与相互作用顶点；(2) 用维数正规化计算四点函数的 1-loop 修正；(3) 确定抵消项并给出 1-loop 重整化耦合（可用最小减除）；(4) 写出耦合常数的重整化群流方程 | 量子场论 | Feynman 参数、维数正规化、Γ 函数极点、MS 方案、β 函数与 RG 方程 | 4 |
| 6 | Klein 圆盘模型：cosh d(x⃗,y⃗)=(1−x⃗·y⃗)/(√(1−x⃗·x⃗)√(1−y⃗·y⃗))：(1) 由距离公式求度规分量；(2) 引入极坐标 (r,θ) 写出线元；(3) 求非零 Christoffel 符号；(4) 计算 R_{rθrθ}；(5) 证 R_{μνρσ}=K(g_{μσ}g_{νρ}−g_{μρ}g_{νσ}) 并定出 K；(6) 求标量曲率 | 微分几何 / 双曲几何 | 由距离反求度规、Christoffel 符号、Riemann 张量、常曲率空间、标量曲率 | 3 |

**卷 F：Probability and Statistics** — 6 题，2 页，3101 字符，小问标记 12 个（**题量从 2025 的 4 题回升到 6 题**）

| 题号 | 一句话题意 | 子领域 | 核心定理 / 方法 | 难度 |
|---|---|---|---|---|
| 1 | Copula 与有序结局：(1) 由 Pr(Y₁≤k,Y₀≤j)=C{F₁(k),F₀(j)} 推导 ψ=Pr(Y₁>Y₀) 的闭式表达；(2) 在潜变量阈值模型 Y*_a=µ_a+ε_a 下（残差联合分布由同一 copula 决定）证明 Pr(Y₁≤k,Y₀≤j)=C{F₁(k),F₀(j)} | 统计 / 因果推断 | Sklar 定理、copula、潜变量阈值模型、序数结局 | 4 |
| 2 | 分块线性回归 Y=X₁β₁+X₂β₂+ε，M₁=I−X₁(X₁^TX₁)^{−1}X₁^T。证明全回归得到的 β̂₂ 与把 M₁Y 对 M₁X₂ 回归得到的 OLS 估计相同 | 线性模型 | Frisch–Waugh–Lovell 定理、投影矩阵、分块求逆 | 2 |
| 3 | φ、Φ 为标准正态的密度与分布函数，a>0：(a) 证 f(x)=2φ(x)Φ(ax) 是某随机变量的密度；(b) 计算 E(Y) | 概率 / 分布论 | 偏正态（skew-normal）分布、积分换序、正态矩 | 2 |
| 4 | B_t 为标准 Brownian 运动，τ_a=inf{t≥0: |B_t|=a}，计算 E[τ_a²] | 随机分析 | 可选停止定理、鞅、Brownian 二次变差、级数求和 | 3 |
| 5 | X₁,X₂,… i.i.d.，存在 n≥2、a>0、b∈R 使 (X₁+…+X_n) =d aX₁+b，α=ln n/ln a：(a) 证 α=1 且 b=0 时特征函数 φ(t)=exp{iµt−γ|t|}；(b) 若另有 E|X₁|<∞，证除非退化情形，否则 (U1) 与 α≤1 不能同时成立 | 概率 / 稳定分布 | 特征函数、独立和的分布方程、稳定分布（Cauchy）、退化性 | 5 |
| 6 | ξ 与 η 独立，若和 S=ξ+η 与差 D=ξ−η 也独立，则 ξ、η 必服从正态分布 | 概率论 | Darmois–Skitovich / Bernstein 定理、特征函数方程、Cramér 分解 | 4 |

---

## 2. 高频考点统计

### 2.1 数据来源与口径说明

- 统计对象：2024–2026 共 **18 份 txt、69215 个抽取字符**。
- 统计方法：Python 脚本（.tmp/burn2026/scripts/yau_2024_2026_stats.py）对规范化后的文本做**大小写不敏感的子串计数**。
- ⚠️ **口径警告**：子串计数会过计数。例如 norm 会命中 normal / normalized；prime 会命中 primitive；character 会命中 characteristic；wave 会命中 wave packet / wavefunction；metric 会命中 geometric 的一部分。因此下表的数字应读作**「该词族的出现次数」**，用于横向比较趋势，不能当作严格的术语计数。原始逐词统计见 .tmp/burn2026/reports/stats_2024_2026.md。

### 2.2 通用题型动词（三年合计）

| 关键词 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| show that | 61 | 18 | 19 | 21 | 21 |
| prove | 50 | 16 | 15 | 22 | 13 |
| assume | 34 | 13 | 12 | 9 | 13 |
| determine | 34 | 13 | 13 | 8 | 13 |
| suppose | 28 | 12 | 7 | 11 | 10 |
| compute | 27 | 14 | 9 | 10 | 8 |
| derive | 12 | 8 | 4 | 4 | 4 |
| construct | 8 | 6 | 4 | 3 | 1 |
| hint | 7 | 5 | 3 | 1 | 3 |
| if and only if | 7 | 6 | 4 | 3 | 0 |
| justify | 6 | 4 | 2 | 3 | 1 |
| example | 3 | 3 | 2 | 1 | 0 |
| disprove | 2 | 2 | 1 | 1 | 0 |
| classify | 1 | 1 | 1 | 0 | 0 |
| counterexample | 0 | 0 | 0 | 0 | 0 |

**读数**：show that + prove 合计 111 次，是绝对主导的题型动词；construct / disprove / counterexample 三年合计仅 10 次，且在 2026 年几乎消失（construct 1 次、disprove 0 次、example 0 次）。

### 2.3 分学科高频考点

#### 2.3.1 代数与数论（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| norm（含 normal/normalized 过计数） | 19 | 10 | 3 | 9 | 7 |
| prime（含 primitive 过计数） | 16 | 4 | 7 | 5 | 4 |
| polynomial | 14 | 5 | 7 | 6 | 1 |
| character（含 characteristic 过计数） | 10 | 6 | 3 | 2 | 5 |
| ramified | 9 | 2 | 0 | 7 | 2 |
| irreducible | 7 | 2 | 2 | 5 | 0 |
| representation | 7 | 2 | 4 | 3 | 0 |
| Galois | 6 | 2 | 0 | 4 | 2 |
| finite group | 5 | 3 | 3 | 2 | 0 |
| ideal | 5 | 3 | 3 | 1 | 1 |
| module | 4 | 2 | 1 | 3 | 0 |
| p-adic | 4 | 3 | 2 | 1 | 1 |
| unramified | 4 | 1 | 0 | 4 | 0 |
| tensor | 3 | 3 | 2 | 0 | 1 |
| valuation | 3 | 2 | 2 | 1 | 0 |
| discriminant | 2 | 2 | 0 | 1 | 1 |
| ring of integers | 2 | 1 | 0 | 0 | 2 |
| field extension | 2 | 2 | 1 | 1 | 0 |
| inertia | 2 | 1 | 0 | 2 | 0 |
| coset | 2 | 1 | 0 | 0 | 2 |
| splitting field | 2 | 1 | 0 | 2 | 0 |
| category / equivalence of categories | 3 | 2 | 0 | 3 | 0 |
| SL2 | 1 | 1 | 0 | 0 | 1 |
| cyclotomic | 1 | 1 | 1 | 0 | 0 |
| localization | 1 | 1 | 0 | 1 | 0 |

**结构观察**：命脉词是 **Galois / 不可约 / 理想 / 分歧**。2025 是「分歧理论大年」（ramified 7 + unramified 4 + inertia 2 + splitting field 2，集中在 P4、P5 两题）；2026 则转向 **交换代数与编码式构造**（coset 2 全在 Hecke 双陪集题；ring of integers 2 全在三次域整基题；character 5 全在 Jacobi 和题）。p-adic 相关词三年为 16→8→5，**局部域权重明显下滑**。

#### 2.3.2 几何与拓扑（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| metric（含 geometric 过计数） | 20 | 8 | 6 | 8 | 6 |
| curvature（含 scalar/Gaussian/geodesic 复合词） | 16 | 5 | 5 | 3 | 8 |
| CP（CP^n 记号） | 9 | 2 | 5 | 4 | 0 |
| manifold | 8 | 4 | 4 | 1 | 3 |
| compact | 6 | 2 | 1 | 0 | 5 |
| sphere | 6 | 4 | 3 | 1 | 2 |
| Lie group | 5 | 2 | 0 | 2 | 3 |
| disk | 5 | 2 | 0 | 0 | 5 |
| scalar curvature | 5 | 4 | 3 | 1 | 1 |
| conformal | 4 | 2 | 0 | 4 | 0 |
| Gaussian curvature | 3 | 2 | 0 | 2 | 1 |
| Ricci | 3 | 3 | 2 | 1 | 0 |
| critical point | 3 | 2 | 1 | 0 | 2 |
| index（Morse 指标） | 3 | 3 | 0 | 1 | 2 |
| loop space | 3 | 1 | 0 | 0 | 3 |
| tangent bundle | 3 | 2 | 0 | 2 | 1 |
| Hessian | 2 | 1 | 0 | 0 | 2 |
| Poincar | 2 | 1 | 0 | 0 | 2 |
| geodesic / geodesic curvature | 4 | 1 | 0 | 0 | 4 |
| homotopy | 2 | 2 | 1 | 0 | 1 |
| universal cover | 2 | 1 | 0 | 0 | 2 |
| Euler characteristic | 2 | 2 | 1 | 1 | 0 |
| Betti / Euler class / Gauss map / aspherical / energy functional / isometric / sectional curvature | 各 1 | 1 | 0 | 0 | 各 1 |
| immersion | 1 | 1 | 0 | 1 | 0 |
| fundamental group | 1 | 1 | 0 | 1 | 0 |
| Killing | 1 | 1 | 1 | 0 | 0 |

**结构观察**：几何卷的「重心迁移」最明显 —— 2024 偏 **CP^n / 映射度 / 同调** 的代数拓扑计算；2025 偏 **CP^n 障碍论 + 共形几何**（conformal 4 次全在 P5）；2026 则同时压上 **黎曼几何硬核（curvature 8、compact 5、disk 5、Ricci 型曲率下界）与 Morse 理论/环路空间（loop space 3、Poincar 2、index 2、Betti 1、critical point 2）**。2026 首次出现 index、loop space、Poincaré 级数、Betti 数、Euler 类、能量泛函这类「研究生代数拓扑」词汇。

#### 2.3.3 分析与微分方程（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| L2（L^2 空间记号） | 20 | 7 | 12 | 2 | 6 |
| norm（过计数严重） | 19 | 10 | 3 | 9 | 7 |
| smooth | 19 | 7 | 6 | 7 | 6 |
| boundary | 11 | 5 | 5 | 0 | 6 |
| BMO | 9 | 1 | 0 | 9 | 0 |
| eigenvalue | 8 | 5 | 5 | 1 | 2 |
| integral | 8 | 4 | 5 | 1 | 2 |
| harmonic（含 subharmonic） | 6 | 3 | 3 | 3 | 0 |
| estimate | 4 | 3 | 0 | 1 | 3 |
| fundamental solution | 4 | 1 | 0 | 0 | 4 |
| heat equation | 3 | 1 | 0 | 0 | 3 |
| periodic | 3 | 2 | 2 | 0 | 1 |
| Fourier | 2 | 1 | 2 | 0 | 0 |
| convergence | 2 | 2 | 0 | 1 | 1 |
| measure | 2 | 1 | 0 | 2 | 0 |
| subharmonic | 2 | 1 | 0 | 2 | 0 |
| Plancherel / Laplacian | 各 1 | 1 | 2024 各 1 | 0 | 0 |
| Banach / Poisson summation / inequality / irrational / orthonormal basis / self-adjoint | 各 1 | 1 | 0 | 0 | 2026 各 1 |

**结构观察**：分析卷三年三次换血 ——
2024：**振荡积分与 Fourier 分析**（Plancherel、Laplacian、compact support、L² 12 次、eigenvalue 5 次），主题是色散型双线性估计与算子可逆性；
2025：**经典不等式与位势论**（BMO 9 次、subharmonic 2 次、measure 2 次；Hardy 不等式最优常数、次调和函数、曲线度）；
2026：**热方程/谱理论与无理数证明**（fundamental solution 4、heat equation 3、self-adjoint 1、orthonormal basis 1、Poisson summation 1、irrational 1、Banach 1）。三年没有重复的题目结构。

#### 2.3.4 计算与应用数学（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| norm（过计数严重） | 19 | 10 | 3 | 9 | 7 |
| Euler（显式/隐式 Euler 法） | 8 | 7 | 2 | 3 | 3 |
| eigenvalue | 8 | 5 | 5 | 1 | 2 |
| stability | 6 | 3 | 2 | 3 | 1 |
| Newton（Newton 法 / Newton–Cotes 式） | 5 | 2 | 0 | 2 | 3 |
| orthogonal | 4 | 4 | 2 | 0 | 2 |
| rank | 4 | 2 | 2 | 0 | 2 |
| Chebyshev | 3 | 1 | 3 | 0 | 0 |
| perturbation | 3 | 2 | 3 | 0 | 0 |
| trapezoid | 3 | 2 | 2 | 1 | 0 |
| BFGS | 2 | 1 | 0 | 0 | 2 |
| Legendre | 2 | 1 | 0 | 2 | 0 |
| convex | 2 | 1 | 0 | 0 | 2 |
| convergence | 2 | 2 | 0 | 1 | 1 |
| finite difference | 2 | 1 | 2 | 0 | 0 |
| flop | 2 | 1 | 2 | 0 | 0 |
| interpolation | 2 | 1 | 0 | 2 | 0 |
| iteration | 2 | 2 | 0 | 1 | 1 |
| quadrature | 2 | 1 | 2 | 0 | 0 |
| A-stable / stiff / spectral radius | 各 1 | 1 | 0 | 2025 各 1 | 0 |
| Crank-Nicolson / Gaussian quadrature / discretiz / order of accuracy / tridiagonal | 各 1 | 1 | 2024 各 1 | 0 | 0 |
| QR / finite element / mesh / singular value / subgradient / truncation error / variational | 各 1 | 1 | 0 | 0 | 2026 各 1 |

**结构观察**：计算卷稳定保留「**差分格式稳定性 + 特征值/谱 + 正交多项式**」三条主线，但每年新增一件现代工具：
2024 = 秩 1 扰动（Sherman–Morrison）、Gershgorin 圆盘、Gauss–Chebyshev 求积、Crank–Nicolson / von Neumann 分析；
2025 = 多点迭代的收敛阶、连带 Legendre 函数的 Chebyshev 系统、θ-格式的 ℓ^∞ 与 ℓ² 双稳定性、刚性系统的 A-稳定；
2026 = **P1 有限元变分形式与能量法稳定性、凸泛函的 Newton / BFGS、位移 QR 的相似变换链、SVD 与不动点几何、凸分析的次微分**。2026 是三年中「研究生数值分析」色彩最重的一年。

#### 2.3.5 数学物理（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| wave（含 wave packet / wavefunction 过计数） | 23 | 3 | 6 | 11 | 6 |
| energy | 18 | 4 | 7 | 7 | 4 |
| curvature（含 Riemann / scalar curvature） | 16 | 5 | 5 | 3 | 8 |
| Lagrangian | 6 | 3 | 3 | 2 | 1 |
| magnetization | 6 | 2 | 4 | 2 | 0 |
| scalar field | 6 | 3 | 1 | 4 | 1 |
| Hamiltonian | 5 | 2 | 3 | 2 | 0 |
| black hole | 5 | 1 | 0 | 5 | 0 |
| gravitational wave | 5 | 1 | 0 | 5 | 0 |
| specific heat | 5 | 2 | 3 | 2 | 0 |
| Maxwell | 4 | 2 | 1 | 3 | 0 |
| conformal | 4 | 2 | 0 | 4 | 0 |
| oscillation | 4 | 3 | 2 | 1 | 1 |
| Ising | 3 | 2 | 1 | 2 | 0 |
| renormaliz | 3 | 2 | 1 | 0 | 2 |
| susceptibility | 3 | 2 | 2 | 1 | 0 |
| entropy | 2 | 2 | 0 | 1 | 1 |
| Klein | 2 | 1 | 0 | 0 | 2 |
| quantum / vacuum / Dirac / Yukawa | 各 1–3 | 1 | 2024 | 0 | 0 |
| de Sitter / Killing vector / critical exponent / mean field / harmonic oscillator | 各 1 | 1 | 2024 各 1 | 0 | 0 |
| photon / spectrum | 各 1 | 1 | 0 | 2025 各 1 | 0 |
| Riemann tensor / Christoffel / propagator | 各 1 | 1 | 0 | 0 | 2026 各 1 |

**结构观察**：物理卷是六年一贯的「六题＝六个物理分支」结构，但分支组合每年不同，而且**几乎没有重复的物理系统**：
- 2024：中心势轨道 / 谐振子瞬态扰动 / 欧姆金属电磁波 / 平均场 Ising / de Sitter / Yukawa QFT —— **教科书四大力学 + 广义相对论 + 量子场论，覆盖面最宽**。
- 2025：旋转圆环上的珠子 / 高斯波包（含光子自旋）/ 电场中的谐振子 / 三角形 Ising / 双黑洞引力波 / 共形标量场 —— **引入"计算链长、物理图像新"的题目**（波包角动量与光子自旋的类比是明显新意）。
- 2026：滑动摆（含倒立摆张力）/ 双线圈近轴展开 / δ 势散射与散射长度 / Clausius–Clapeyron / φ⁴ 重整化群 / Klein 圆盘双曲几何 —— **把纯微分几何（Klein 圆盘）放进物理卷**，并用维数正规化 + RG 流方程取代 2024 的"找发散"式问题。

#### 2.3.6 概率统计（6 卷）

| 关键词 / 定理 / 方法 | 总次数 | 出现卷数 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| distribution | 15 | 3 | 4 | 5 | 6 |
| probability | 15 | 4 | 2 | 11 | 2 |
| normal（正态） | 12 | 9 | 3 | 3 | 6 |
| independent | 8 | 5 | 2 | 2 | 4 |
| random variable | 8 | 3 | 1 | 3 | 4 |
| copula | 6 | 1 | 0 | 0 | 6 |
| OLS | 5 | 3 | 1 | 0 | 4 |
| covariate | 5 | 1 | 5 | 0 | 0 |
| density | 5 | 3 | 2 | 0 | 3 |
| expectation | 5 | 3 | 3 | 2 | 0 |
| estimator | 4 | 2 | 1 | 0 | 3 |
| regression | 4 | 2 | 1 | 0 | 3 |
| CDF | 3 | 1 | 0 | 0 | 3 |
| asymptotic | 3 | 1 | 3 | 0 | 0 |
| confidence interval | 3 | 1 | 0 | 3 | 0 |
| i.i.d | 3 | 3 | 1 | 1 | 1 |
| median | 3 | 2 | 3 | 0 | 0 |
| ANOVA / Poisson / log-likelihood | 各 1 | 1 | 2024 各 1 | 0 | 0 |
| Brownian / characteristic function | 各 1 | 1 | 0 | 2025 各 1 | 0 |

**结构观察**：2024 = **渐近理论与极值统计**（asymptotic 3、covariate 5、median 3），题目偏 O_p 型收敛率；2025 = **决策论与构造性概率**（probability 11 次集中在决策规则题，另有 Brownian、随机化置信区间、奇怪的三角常数构造题）；2026 = **copula/因果推断 + 经典极限定理**（copula 6、CDF 3、OLS 4、regression 3、estimator 3）。三年**互不重复**。

### 2.4 命题风格趋势指标（逐年出现次数）

| 指标 | 2024 | 2025 | 2026 | 三年合计 |
|---|---|---|---|---|
| 证明要求：prove / show that | 30 | 42 | 37 | 109 |
| 求解要求：compute / derive / determine / find / calculate | 32 | 40 | 30 | 102 |
| 判定句式：Does there exist / Is the / Is it / Is there / Are there / Can we / Can the / Can a / Does the | 22 | 18 | 12 | 52 |
| 构造 / 反例 / 证伪：construct / counterexample / disprove | 4 | 4 | 0 | 8 |
| 小问标记 (a)–(j) | 64 | 24 | 47 | 135 |
| 小问标记 (1)–(9) | 31 | 44 | 50 | 125 |
| if and only if | 4 | 3 | 0 | 7 |
| Hint | 3 | 1 | 3 | 7 |
| 线性代数词族（matrix / eigenvalue / eigenvector / singular value / orthogonal / rank） | 11 | 4 | 15 | 30 |
| 曲率词族（curvature / Ricci / Riemann tensor / geodesic） | 6 | 4 | 11 | 21 |
| p-adic / 局部域词族（p-adic / Qp / Zp / local field / unramified / ramified） | 16 | 8 | 5 | 29 |
| 数值格式词族（finite element / finite difference / stabilit / scheme / discretiz） | 3 | 1 | 1 | 5 |
| QFT 词族（renormaliz / propagator / counterterm / loop / Yukawa） | 3 | 0 | 7 | 10 |
| 广义相对论词族（black hole / gravitational wave / de Sitter / general relativity） | 2 | 4 | 0 | 6 |
| 随机分析词族（Brownian / martingale / stopping time） | 0 | 0 | 1 | 1 |
| 拓扑词族（homotopy / homology / cohomology / bundle / fundamental group） | 1 | 2 | 3 | 6 |

### 2.5 难度自评汇总（按学科求均值）

| 年份 | 代数与数论 | 分析与微分方程 | 计算与应用 | 几何与拓扑 | 数学物理 | 概率统计 | 全卷均值 |
|---|---|---|---|---|---|---|---|
| 2024 | 4.00 (6 题) | 4.00 (5 题) | 3.17 (6 题) | 3.33 (6 题) | 3.50 (6 题) | **4.40 (5 题)** | 3.71 |
| 2025 | 4.20 (5 题) | **2.83 (6 题)** | 3.50 (6 题) | 3.67 (6 题) | 3.83 (6 题) | **4.50 (4 题)** | 3.70 |
| 2026 | 4.00 (5 题) | 3.40 (5 题) | 3.50 (6 题) | **4.00 (6 题)** | 3.33 (6 题) | **3.33 (6 题)** | **3.59** |
| 三年均值（按题数加权） | 4.06 | 3.38 | 3.39 | 3.67 | 3.56 | 4.00 | 3.66 |
| 三年均值（各年均值再平均） | 4.07 | 3.41 | 3.39 | 3.67 | 3.55 | 4.08 | 3.67 |

> 说明：两种口径都列出。按题数加权 ＝ 该科三年难度总分 除以 该科三年总题数；后者 ＝ 三个年度均值的算术平均。下文引用一律采用**按题数加权**口径（更贴近「随机抽一道题的期望难度」）。

**读数**：
- **最难的两科始终是「代数与数论」和「概率统计」**（三年加权均值 4.06 / 4.00）。
- **概率统计在 2026 年出现显著"降难增面"**：难度均值从 4.40 / 4.50 降到 3.33，同时题量从 4–5 题增到 6 题。这是三年中唯一一次「同一科目同时降难度、加题量」，也是最清晰的一次命题调整信号。
- **几何与拓扑在 2026 年反向上行**（3.33 → 3.67 → 4.00），配合 2.3.2 的词频迁移，可判断 2026 几何卷是三年中最难的一份。
- 全卷均值小幅下行（3.71 → 3.70 → 3.59），但这是**科目权重再平衡**的结果，不是整体难度下降。

---

## 3. 代表性题目精析（8 道）

> 说明：题面保留抽取原文（仅做连字还原、断行连字符修复与最必要的符号清理）；解题思路为本报告自撰，**无官方解答可核对**。

### 题 1｜2024 分析与微分方程 Problem 1 —— 「断言是否正确」型题的典型

**题面（原始抽取，已做最小清理）**：

> Let Q : R to R be a C_c^inf function, i.e. it is smooth and has compact support. We assume Q is even, i.e. Q(x) = Q(-x). We assume Q is non-trivial, (i.e. Q does not equal to zero everywhere).
> Let T1(x) := xQ(x), and let T2(x) = x^2 Q(x). Let T3 := exp(-x^2)(1 + x^2024).
> We also introduce the following notation. For any f : R to R, lambda > 0, alpha in R, we define
> f_{lambda,alpha}(x) := (1/lambda^{1/2}) f((x - alpha)/lambda).       (0.1)
> We claim: There exists delta > 0, epsilon > 0, so that for any c in R with |c| < delta, one can find unique lambda, alpha such that the followings hold
> 1. |lambda - 1| + |alpha| < epsilon.
> 2. <Q_{lambda,alpha} - Q - c*T3, T1> >= 0
> 3. <Q_{lambda,alpha} - Q - c*T3, T2> >= 0
> (Here, for any two functions f1, f2, we define <f1, f2> := integral of f1(x) f2(x) dx).
> Is the above claim correct? Prove your conclusion.

**解题思路**：
1. lambda = 1, alpha = 0 时三项都成立（c = 0 的平凡解），所以问题实质是**在 c 附近是否有唯一解**——关键在 unique 一词。
2. 做一阶线性化。令 a = lambda - 1、b = alpha。由 f_{lambda,alpha} = lambda^{-1/2} f((x-alpha)/lambda) 得，在 (1,0) 处对 lambda 求导为 -(1/2)Q - xQ'，对 alpha 求导为 -Q'，故
   g := Q_{lambda,alpha} - Q 约等于  a*(-(1/2)Q - xQ') - b*Q'。
3. 用 Q 为**偶函数**做分部积分：积分 x*Q^2 = 0；积分 x^2*Q*Q' = -(积分 x*Q^2) = 0；积分 x^3*Q*Q' = -(3/2)*I2，其中 I2 = 积分 x^2*Q^2 > 0。于是
   <g, T1> = (1/2)*b*(积分 Q^2)，
   <g, T2> = a*I2。
4. 又 <T3, T1> = 0（**偶函数乘奇函数**），而 <T3, T2> =: J，对一般非平凡偶函数 Q 有 J 不等于 0和零。所以线性化后两个条件化为
   b*(积分 Q^2) >= 0（或 <= 0），  a >= c*J/I2（或 <=）。
5. 这是**一个二维半平面区域，而不是一个点**：alpha（即 b）在一阶上完全自由，lambda（即 a）只被一个单边不等式约束。
6. **结论：断言为假。** 解通常存在（只要 c 足够小），但绝不唯一。需要注意的是，抽取文本中的不等号方向不可完全信赖（见第 5 节 U1），因此本解答刻意不依赖符号方向：把 >= 读成 <= 只会把半平面换成另一个半平面，**非唯一性的结论不变**。这道题考的是「发现隐藏退化（T1 与尺度方向正交）并拒绝接受题面断言」。

### 题 2｜2024 代数与数论 Question 2 —— 支配序与 Bruhat / Cartan 分解

**题面（节选）**：

> Let A be a discrete valuation ring with K its field of fractions and pi in A a uniformizer. For lambda = (lambda1, ..., lambdan) in Z^n write D_lambda = diag(pi^{lambda1}, ..., pi^{lambdan}) in GL_n(K).
> Show that, for lambda, mu in Z^n, the following intersection inside GL_n(K)
> GL_n(A) . D_mu . GL_n(A)  intersect  U(K) . D_lambda
> is non-empty if and only if lambda_dom <= mu_dom.
> Here ... U(K) is the standard unipotent subgroup, that is, the subgroup of upper triangular matrices with coefficients 1 on the diagonal; and for alpha = (a1,...,an), beta = (b1,...,bn) we write alpha <= beta if sum_{i<=k} a_i <= sum_{i<=k} b_i for all 1 <= k <= n and sum a_i = sum b_i; alpha_dom is the decreasing rearrangement.

**解题思路**：
1. 先把两层结构拆开。GL_n(A) . D_mu . GL_n(A) 是「**A-格的相对位置**」：在离散赋值环上，它恰是「Smith 标准形（初等因子）为 mu_dom」的矩阵全体。
2. U(K) . D_lambda 则是「**在标准旗** 0 包含于 <e1> 包含于 <e1,e2> 包含于 ... 下可对角化为 D_lambda」的矩阵全体，等价于存在与标准旗相容的格分解 L = 直和 A * pi^{lambda_i} * f_i。
3. 于是问题变成：**给定初等因子序列（等价于不变因子 mu_dom），能否把它放在一个指定旗上、使第 i 步的对角元恰为 pi^{lambda_i}？**
4. 这是 Hall 婚配定理 / Gale–Ryser 定理的经典形态：在一族线性子空间上实现指定的对角元，其可行性条件正是**弱优超（majorization），即支配序**。把「第 k 步子模的秩」写成前缀和条件，即得 sum_{i<=k} lambda_{dom,i} <= sum_{i<=k} mu_{dom,i}（总次数相等由行列式给出）。
5. 必要性用秩的单调性：任何 M 属于 GL_n(A) D_mu GL_n(A) 时，其前 k 个不变因子之和被 mu_dom 的前缀和控制；而 U(K) D_lambda 的实现要求第 k 步的次幂至少达到 lambda_dom 的前缀和。两端合并即得充要条件。
6. 这是一道**把线性代数（Smith 标准形）、代数群（Bruhat / Cartan 分解）与组合学（优超序）三者接起来**的题，也是三年中唯一一道明确要求「充要条件 + 反向构造」的高难度代数题。

### 题 3｜2025 代数与数论 Problem 2 —— 半直积群与绝对不可约性

**题面（节选）**：

> Let p be prime number, e, f in Z_{>=1}. Let G be a finite group of order n := ef generated by two elements sigma and tau, satisfying the relations
> sigma^f = 1,  tau^e = 1,  and  sigma tau sigma^{-1} = tau^p.
> (1) Show that such a group G exists if and only if p^f = 1 (mod e). If the latter condition is satisfied, there exists, up to isomorphisms, a unique finite group G as described above.
> (2) Let F_{p^f} denote the finite field with p^f elements, and eta in F_{p^f} a primitive e-th root of unity. Let G act on A := F_{p^f} via sigma(a) = a^p, tau(a) = eta * a. Show that the following three assertions are equivalent: (a) the F_p-representation A of G is absolutely irreducible in the sense that the C-representation C (x)_{F_p} A of G is irreducible, where C is any algebraically closed field containing F_p; (b) the F_p-representation A is irreducible; (c) p is of order f in (Z/eZ)^x.

**解题思路**：
1. **存在性**：由 στσ⁻¹ = τ^p 迭代得 σ^f τ σ^(−f) = τ^(p^f)；又 σ^f = 1，故 τ^(p^f) = τ，即 e | p^f − 1（由此 e 与 p 自动互素，p 在模 e 下可逆）。充分性用半直积 Z/e ⋊ Z/f 实现；唯一性由 |G| = ef 与生成关系推出。
2. **关键化简（把表示论问题化为特征值的算术）**：把 A = F_(p^f) 视作 F_p-向量空间并复化。由于 η ∈ F_(p^f)，其共轭元恰为 η, η^p, η^(p²), …（Frobenius 轨道）。
3. 分解 C ⊗_(F_p) A = ⊕_(i=0)^(f−1) V_i，其中每个 V_i 都是 τ 的特征空间（特征值 η^(p^i)）。σ（Frobenius 自同构）把 V_i 循环地送到 V_(i+1)。
4. 于是：**若 ord_e(p) = f，则各 V_i 互不同构、全为 1 维，任何 σ-不变子空间必须是全体，故不可约**；**若 ord_e(p) = d < f，则每个 V_i 的维数变为 f/d > 1，从每个 V_i 中各取一条线张成的子空间在 G 下不变，故可约**。
5. 这一步同时给出 (a) ⟺ (c) 与 (b) ⟺ (c)：因为所有 V_i 的维数相同，C-不可约与 F_p-不可约等价（绝对不可约性与普通不可约性在这个具体模块上重合）。
6. 题目把「绝对不可约性」这种看似抽象的条件，完全转化为「p 模 e 的阶」这一个数论量——这是 2025 代数卷「用具体计算代替抽象论证」风格的缩影。

### 题 4｜2025 几何与拓扑 Problem 4 —— 特征类障碍：CP² 不能浸入 R⁶

**题面（原文）**：

> Problem 4. Prove that CP2 does not admit an immersion into R6.

**解题思路**：
1. 反设存在浸入 f : CP² ↬ R⁶。余维数为 2，法丛 ν 是实秩 2 丛，且 Whitney 和给出 T(CP²) ⊕ ν ≅ f*T(R⁶) ≅ ε⁶（平凡 6 维实丛）。
2. 取 Z₂ 系数的全 Stiefel–Whitney 类，由 Whitney 乘积公式得 w(T(CP²)) · w(ν) = 1，即 w(ν) = w(T(CP²))⁻¹。
3. 计算 w(T(CP²))。CP² 是复流形，切丛复化后 c(T(CP²)) = (1 + a)³（a 为 H²(CP²; Z) 的生成元），故 c₁ = 3a、c₂ = 3a²。由 w_(2i) = c_i mod 2 得 w(T(CP²)) = 1 + a + a²，这里在 H*(CP²; Z₂) = Z₂[a]/(a³) 中运算（a 是 H² 的 Z₂ 生成元，a³ = 0）。
4. 求逆：注意到 (1 + a + a²)(1 + a) = 1 + a + a² + a + a² + a³ = 1（特征 2 使交叉项相消，且 a³ = 0）。所以 w(ν) = 1 + a，即 **w₁(ν) = a ≠ 0**。
5. **矛盾**：CP² 单连通，故 H¹(CP²; Z₂) = Hom(π₁, Z₂) = 0。任何实向量丛的第一 Stiefel–Whitney 类都落在 H¹(·; Z₂) 中，因此必须为零，与 w₁(ν) = a ≠ 0 矛盾。
6. **结论：不存在这样的浸入。** 全部工作量在于「正确算出并求逆 w(T(CP²))」加「意识到 w₁ 必须落在 H¹ 这个零群中」。这也说明 2025 几何卷偏好「短题面 + 一步到位的特征类障碍」。

### 题 5｜2025 数学物理 Problem 5 —— 双黑洞引力波与并合时间

**题面（节选）**：

> In this problem, we study the gravitational waves emitted from a binary system of two black holes. As a simplifying assumption, we treat black holes as point masses. ...
> 1. For a point mass m moving near the origin in the (x, y) plane along a trajectory x = x(t), y = y(t), general relativity predicts that the gravitational waves emitted by m have the following amplitudes h at distance L from the origin with inclination angle theta:
> h_+ = (1/L)(G/c^4) ((1 + cos^2 theta)/2) m (d^2/dt^2 (x^2 - y^2)),   h_x = (1/L)(G/c^4) (cos theta) m (d^2/dt^2 (2xy)).
> For two black holes with masses m1 and m2 separated by r, forming a circular orbit under Newtonian gravity with their center-of-mass at the origin, please derive h_+ and h_x. What is the gravitational wave frequency f?
> 2. ... p = (c^3 L^2 / 16 pi G) [ (dh_+/dt)^2 + (dh_x/dt)^2 ]. Please find the average power P radiated ... over all directions and averaged over one orbital period.
> 3. ... Let the gravitational wave frequency be f0 at the initial time t = t0. Please determine f(t).
> 4. ... Let the initial separation be r0. Please find the coalescence time TC.
> 5. For m1 = m2 = 10 Msun, please estimate the maximum initial separation r0 (in au) allowing coalescence within the age of the universe (T = 10^10 years). Order-of-magnitude estimation suffices.

**解题思路**：
1. 质心系中取 x₁ = −(m₂/M) r cos ωt，y₁ = −(m₂/M) r sin ωt；x₂ = +(m₁/M) r cos ωt，y₂ = +(m₁/M) r sin ωt，其中 M = m₁ + m₂，开普勒关系 ω = √(GM/r³)。
2. 题目公式是**对每个质量求和**的四极辐射公式。先算被求导的两个量（关键恒等式：∑ mᵢ xᵢ² = μ r²，μ = m₁m₂/M 为约化质量）：
   ∑ mᵢ (xᵢ² − yᵢ²) = μ r² cos 2ωt，  ∑ mᵢ (2xᵢyᵢ) = μ r² sin 2ωt。
3. 两次求导放大 4ω²，得
   h₊ = −(4/L)(G/c⁴)((1+cos²θ)/2) μ ω² r² cos 2ωt，  hₓ = −(4/L)(G/c⁴) cos θ · μ ω² r² sin 2ωt。
   引力波频率是轨道频率的两倍：**f = 2 f_orb = ω/π**。
4. **辐射功率**：把 p 对立体角积分并作时间平均（用到 ∫(1+cos²θ)² dΩ 与 ∫cos²θ dΩ），得标准四极公式
   P = (32/5)(G⁴/c⁵) m₁²m₂²(m₁+m₂)/r⁵ = (32/5)(G/c⁵) μ² r⁴ ω⁶。
5. **f(t)**：由 E = −Gm₁m₂/(2r) 与 dE/dt = −P 得 dr/dt = −(64/5) G³m₁m₂M/(c⁵ r³)，积分得
   r(t)⁴ = r₀⁴ − (256/5)(G³m₁m₂M/c⁵)(t − t₀)。
   代入 ω ∝ r^(−3/2) 得 **f(t) = f₀ (1 − (t − t₀)/T_C)^(−3/8)**。
6. **并合时间**：T_C = (5/256) c⁵ r₀⁴ / [G³ m₁m₂ (m₁+m₂)]。
7. **数值估计**：m₁ = m₂ = 10 M☉ 时 M = 20 M☉。用 GM☉/c² ≈ 1.48 km、GM☉/c³ ≈ 4.93 × 10⁻⁶ s 得 G³m₁m₂M/c⁵ ≈ 1.93 × 10²¹ m⁴/s。令 T_C = 10¹⁰ yr = 3.16 × 10¹⁷ s，解得
   r₀ ≈ [ (256/5) × 1.93×10²¹ × 3.16×10¹⁷ ]^(1/4) m ≈ 1.8 × 10¹⁰ m ≈ **0.12 au**。
   即「两个 10 太阳质量黑洞若想在一个宇宙年龄内并合，初始间距只能是约 0.1 au 的量级」——这正是 LIGO 探测到双黑洞并合后必须面对的「并合时间尺度问题」的定量表述。

### 题 6｜2026 计算与应用数学 Problem 5 —— 不动点、奇异值与转置

**题面（原文）**：

> Let A in R^{n x n} be an n by n real matrix and sigma_i(A) be its i-th largest singular value. A vector x in R^n such that Ax = x is called a fixed point of A.
> (a). Assume sigma_1(A) <= 1, show that every fixed point of A is a fixed point of its transpose A^T.
> (b). Consider A = [[1, 1], [0, 0]] to verify that the assertion in (a) is not generally true without assuming sigma_1(A) <= 1.
> (c). Assume A A^T = A^T A, show that every fixed point of A is a fixed point of its transpose A^T.

**解题思路**：
1. **核心不等式**：对任意 x 有 ‖Ax‖ ≤ σ₁(A)‖x‖ ≤ ‖x‖。设 Ax = x 且 x ≠ 0，则 ‖Ax‖ = ‖x‖，逼出**两处都必须取等号**。
2. 用 SVD A = UΣVᵀ 分析等号条件：‖Ax‖ = σ₁‖x‖ 当且仅当 x 落在「奇异值等于 σ₁ 的右奇异向量」张成的子空间 E 中；而 σ₁ ≤ 1 又迫使 σ₁ = 1。在 E 上 AᵀA = I。
3. 于是 Aᵀx = Aᵀ(Ax) = AᵀAx = x，(a) 得证。（若 σ₁ < 1 则只有 x = 0，平凡成立。）
4. **(b) 反例**：A = [[1,1],[0,0]] 的不动点由 x₁ + x₂ = x₁ 与 0 = x₂ 给出，即 {(t, 0)}；但 Aᵀ(t,0) = (t, t) ≠ (t, 0)。同时 σ₁(A) = √2 > 1，说明 σ₁ ≤ 1 不可去。
5. **(c)**：AAᵀ = AᵀA 即 A 正规。由正规矩阵谱定理 A = UΛU*，且 |λᵢ| = σᵢ。Ax = x 说明 x 落在特征值 1 的特征子空间中；在该子空间上 Aᵀ = A* 同样作用为 1，故 Aᵀx = x。
6. 这道题极短，却精确地考了「**等号条件 + SVD 几何**」这一最易被忽略的技术点，并且用了「先一般、再反例、再加强条件」的三段式结构——这是 2026 卷反复出现的命题模板。

### 题 7｜2026 几何与拓扑 Problem 4 —— S²⁰²⁶ 的 Euler 类、Morse 指标与环路空间

**题面（节选）**：

> Let S2026 be the unit sphere in R2027.
> (1) Compute the Euler class of the tangent bundle TS2026 -> S2026 with Z2 coefficients.
> (2) Let US2026 -> S2026 denote the unit tangent sphere bundle; that is, the fiber over each point is identified with S2025. Compute the Poincare series P_t(US2026; Z2) = sum_{i>=0} b_i(US2026; Z2) t^i.
> (3) Let p, q in S2026 be two non-antipodal points. Consider the space of piecewise smooth paths from p to q, Omega(S2026; p, q) = { gamma : [0,1] -> S2026 | gamma(0) = p, gamma(1) = q }, equipped with the energy functional E(gamma) = (1/2) integral_0^1 |gamma-dot(t)|^2 dt.
> (a) Determine all critical points of E. (b) The index lambda(E, gamma) of E at a critical point gamma is defined as the dimension of the maximal subspace of T_gamma Omega(S2026; p, q) on which Hess E is negative definite. Compute lambda(E, gamma). (c) Determine the homotopy type of the based loop space Omega(S2026, p). (d) Compute the Poincare series of both the based loop space Omega(S2026, p) and the free loop space Lambda S2026 with Z2 coefficients.

**解题思路**：
1. **(1)** Euler 类在基本类上的取值等于 χ(S^(2m)) = 2。模 2 后 2 ≡ 0，故 **Euler 类为 0**（这也正是偶数维球面存在无处为零向量场的上同调解释）。
2. **(2)** 对纤维化 S²⁰²⁵ → US²⁰²⁶ → S²⁰²⁶ 用 Gysin 序列
   … → H^(i−2026)(S²⁰²⁶) --∪e--> H^i(S²⁰²⁶) → H^i(US²⁰²⁶) → H^(i−2025)(S²⁰²⁶) --∪e--> H^(i+1)(S²⁰²⁶) → …
   因 e = 0，序列裂成短正合列 0 → H^i(S²⁰²⁶) → H^i(US²⁰²⁶) → H^(i−2025)(S²⁰²⁶) → 0，于是
   dim H^i(US²⁰²⁶; Z₂) = dim H^i(S²⁰²⁶) + dim H^(i−2025)(S²⁰²⁶)，非零维数只在 i = 0, 2025, 2026, 4047，各 1 维：
   **P_t(US²⁰²⁶; Z₂) = 1 + t²⁰²⁵ + t²⁰²⁶ + t⁴⁰⁴⁷**。
3. **(3a)** 能量泛函的临界点就是 p → q 的测地线。p、q 非对径，故测地线沿过 p、q 的大圆，共有**两族**，长度分别为
   L_k = d + 2πk 与 L'_k = (2π − d) + 2πk，k ≥ 0，其中 d = d(p,q) ∈ (0, π)。
4. **(3b)** S^n 上沿测地线的共轭点出现在弧长 π, 2π, 3π, … 处，每处贡献重数 (n−1)。故
   λ(γ) = (n−1) · #{ m ≥ 1 : mπ < L(γ) }。
   对 L = d + 2πk（因 d < π）得 **λ = 2k(n−1)**；对 L = (2π−d) + 2πk 得 **λ = (2k+1)(n−1)**。取 n = 2026 即得 2025 × 2k 与 2025 × (2k+1)。
5. **(3c)** 基于环路空间：对 n ≥ 2，ΩS^n 有 James 构造给出的 CW 分解，在维度 k(n−1)（k ≥ 0）处各有一个胞腔：
   **ΩS²⁰²⁶ ≃ CW 复形 { pt, S²⁰²⁵, S^(2·2025), S^(3·2025), … }**。
6. **(3d)** 因 S²⁰²⁶ 单连通，自由环路空间满足 ΛS^n ≃ S^n × ΩS^n，于是
   **P_t(ΩS²⁰²⁶; Z₂) = 1/(1 − t²⁰²⁵) = 1 + t²⁰²⁵ + t⁴⁰⁵⁰ + t⁶⁰⁷⁵ + …**
   **P_t(ΛS²⁰²⁶; Z₂) = (1 + t²⁰²⁶)/(1 − t²⁰²⁵) = 1 + t²⁰²⁵ + t²⁰²⁶ + t⁴⁰⁵⁰ + t⁴⁰⁵¹ + …**
7. 这道题把 **Gysin 序列 → 谱序列计算 → 测地线的 Morse 指标 → 环路空间的同伦分解 → Poincaré 级数** 串成一条完整链条，是三年中单题内部结构最「长」的一题，也是 2026 卷「现代代数拓扑下放」的标志性证据。

### 题 8｜2026 概率统计 Problem 6 —— Bernstein / Darmois–Skitovich 定理

**题面（原文）**：

> Problem 6. Let xi and eta be independent random variables. If the sum S = xi + eta and the difference D = xi - eta are also independent, then xi and eta must follow normal distributions.

**解题思路**：
1. 记 φ(t) = E[e^(itξ)]、ψ(t) = E[e^(itη)]（特征函数）。由 ξ、η 独立：
   E[e^(i(uS+vD))] = φ(u+v) ψ(u−v)；
   而由 S 与 D 独立：E[e^(iuS)] E[e^(ivD)] = φ(u)ψ(u) · φ(v)ψ(−v)。
2. 合并得到**函数方程**（对所有 u, v 成立）：
   φ(u+v) ψ(u−v) = φ(u) ψ(u) φ(v) ψ(−v)。
3. 换元 s = u+v、t = u−v 后，对 s 与 t 各求一次偏导，再令 t = 0（或 s = 0），可消去 ψ，得到二阶常微分方程
   φ''(s) φ(s) − φ'(s)² = c · φ(s)²，  即  (log φ)'' ≡ c（c 为常数）。
4. 解之：log φ(t) = iμt + (c/2) t²。由 φ 是特征函数须满足 |φ| ≤ 1 与 φ(0) = 1，得 c = −σ² ≤ 0。于是
   **φ(t) = exp( iμt − (σ²/2) t² )**，即 ξ ~ N(μ, σ²)（σ = 0 为退化情形，ξ 几乎必然为常数）。
5. 对 ψ 同理得 η 服从正态。**结论：ξ、η 必为正态（或退化）。**
6. 这是经典的 **Bernstein / Darmois–Skitovich 定理**，标准证明就是「**把独立性翻译成特征函数的函数方程，再求导化为二阶 ODE**」。2026 卷把它作为压轴题，却只给了一行题面——这正是 2026 卷「陈述极简、工具固定」风格的极致体现。

---

## 4. 命题风格变化观察（2024 → 2025 → 2026）

### 4.1 结构层面：赛制收缩后趋于固化

- **团体卷自 2020 年起消失，2024–2026 三年全部只有 6 份个人赛卷**（2019 是语料中最后一次出现 team 文件）。本批三年完全不含 team 卷，也不含官方解答。
- **官方解答自 2023 年起停止公开**：2020 / 2021 / 2022 每年都有 soln 文件，2023–2026 为 0 份。这直接导致 2024–2026 的题目缺乏「官方难度标定」，也是本报告难度自评存在不确定性的根源。
- 六科固定为：代数与数论、分析与微分方程、几何与拓扑、计算与应用数学、概率统计、**数学物理**（数学物理自 2022 年进入语料并稳定至今）。
- 三年题量为 34 / 33 / 34，**总量高度稳定**；但同届内部的不平衡度不小：2025 概率统计只有 4 题（三年唯一低于 5 题者），2025 几何卷只有 1 页 1983 字符（三年最短），2025 数学物理卷 4 页 8122 字符（三年最长）。**同一届内各卷体量差异可达 4 倍**，这是本竞赛一个容易被忽视的特征。

### 4.2 篇幅层面：题面变短，但「梯子」变密

| 指标 | 2024 | 2025 | 2026 |
|---|---|---|---|
| 总字符 | 24229 | 22991 | 21995 |
| 题量 | 34 | 33 | 34 |
| 平均每题字符 | 712.6 | 696.7 | 646.9 |
| 小问标记总数 | 95 | 68 | 97 |

题面字数三年连降（−9.2%），但小问标记数在 2026 反弹到三年最高。**含义：题目本身写得更短，但被切成更多、更细的台阶。** 典型例子是 2026 计算卷 Problem 2（(a) 求梯度与 Hessian 并证严格凸；(b) Newton 法与二阶收敛；(c) BFGS 更新良定义）与 2026 代数卷 Problem 5（(1) 有限性；(2) 循环性；(3) 计数）。这种「**短题面 + 长阶梯**」的设计，把大问题拆成可分别得分的若干小问，是 2026 年最清晰的形式变化。

### 4.3 题型层面：「判伪题」退场，「证明既定结论」成为默认

量化证据（见 2.4 节）：

- 判定句式（Does there exist / Is the / Can …）：**22 → 18 → 12**，2026 比 2024 下降 **45%**。
- 构造 / 反例 / 证伪动词（construct / counterexample / disprove）：**4 → 4 → 0**，2026 年**完全归零**。
- 与之相对，prove / show that 保持高位（30 / 42 / 37）。

需要特别指出一个**微妙的反例**：2026 虽然不再使用 construct / disprove 这类动词，但「举反例」的实质仍然存在，只是被包进了小问里——例如 2026 计算卷 P5(b)「用 A = [[1,1],[0,0]] 验证断言在去掉 σ₁ ≤ 1 时不真」、2026 几何卷 P6(2)「举例说明 ε ≤ 1/4 时结论失效」。**所以准确的说法是：反例从「整题的独立目标」降格为「证明链条中的一个验证步骤」。**

2024 年那种「给你一个断言，你说对不对」的整题（2024 分析 P1）、以及 2025 年那种「构造出具有指定概率的随机变量」（2025 统计 P3），在 2026 年完全绝迹。**这是三年里最显著、最可量化的命题风格转变。**

### 4.4 内容层面：现代工具明显下放

按 2.3 的分类统计，2026 年首次（或近三年唯一）出现的工具包括：

- 计算卷：**H¹₀ 空间上的 Fréchet 二阶导数与严格凸性、BFGS 割线条件、位移 QR 迭代的相似变换链、凸分析次微分与法锥**。
- 几何卷：**Euler 类与 Gysin 序列、Morse 指标、环路空间的 CW 同伦型、Poincaré 级数、双不变度规的 Cartan–Schouten 曲率公式**。
- 统计卷：**copula 与 Sklar 定理、潜变量阈值模型、Frisch–Waugh–Lovell 定理**。
- 物理卷：**维数正规化 + 最小减除 + 重整化群流方程**（2024 只要求「找出发散与抵消项」，2026 升级为完整 RG 流程）。

反方向的收缩也很明确：

- **p-adic / 局部域权重下滑**（16 → 8 → 5 次词频）：2024 有 Q5 一整题 p-adic 分析；2025 有两题（P4 局部域范畴等价、P5 分歧与惯性）；2026 收缩为 P5 一题，且重点转向「分类计数」。
- **广义相对论词族 2025 达峰后 2026 归零**（2 → 4 → 0）：2024 的 de Sitter、2025 的双黑洞引力波都是整题，2026 物理卷没有 GR 题目。
- **数值格式稳定性（finite difference / stability 词族）持续走低**：2024 有 3 道差分格式题（含 von Neumann 分析、Crank–Nicolson），2026 只剩 1 道隐式 Euler 稳定性，其余计算题转向有限元、优化与矩阵分析。

### 4.5 一个好玩且可核查的传统：年份彩蛋

命题组连续三年把当年年份嵌进题目：

| 年份 | 彩蛋位置 | 抽取原文（已 grep 核实） |
|---|---|---|
| 2024 | 分析与微分方程 Problem 1 | Let T3 := e^{−x2}(1 + x2024) |
| 2025 | 分析与微分方程 Problem 1 | r3R'''(r) + 2r2R''(r) − rR'(r) + R(r) = 2025；R(1) = 2025 |
| 2026 | 几何与拓扑 Problem 4 | Let S2026 be the unit sphere in R2027 |

三年里两次出现在分析卷、一次出现在几何卷，且 2026 年直接让「球面维数 = 年份」，把彩蛋变成了题目的核心参数。可作为「**命题组有稳定的个人趣味**」的直接证据（三处均已在语料中用文本检索确认）。

### 4.6 三年各卷「性格」速写

- **2024 代数**：广度优先——一题打尽有限群表示论（4 小问）、一题打通交换代数与赋值论、一题分圆域 + 格。是全三年最「教科书式」的一份代数卷。
- **2024 分析**：唯一「判断命题真伪」整题 + 算子可逆性 + 双线性振荡估计，且题目符号从根上就不给答案。
- **2024 计算**：最「工科」的一份——Sherman–Morrison、梯形法误差渐近、Chebyshev、Gershgorin、von Neumann，五道经典数值分析。
- **2024 几何**：以映射度、Euler 示性数、Ricci 迹公式为主的「本科可懂」选题，1 页 6 题，是全三年最「轻」的一份几何卷。
- **2024 物理**：分支覆盖最全（力学 / 量子 / 电动力学 / 统计 / GR / QFT 各一），每题结构工整，像一份「物理系四大力学期末考合集」。
- **2024 统计**：最难的一份统计卷（4.40），O_p 收敛率题（n^(−1/3)）与极值统计题都是研究生统计方向的内容。
- **2025 代数**：分歧理论大年，P4（局部域范畴等价）与 P5（X⁵−X+1 的 S₅）两道重题压阵。
- **2025 分析**：全三年单卷最易（2.83）——Hardy 不等式、Euler 方程、次调和函数、Urysohn 引理、BMO 都是标准结论，只有曲线度那一题需要一点组织。
- **2025 计算**：最「分析化」的一份——多点迭代收敛阶、连带 Legendre 函数、θ-格式的双范数稳定性。
- **2025 几何**：短小锋利，6 题全部围绕「上同调类 / 不变量」做文章（切丛平凡性、Berger 度规、U(n) 同伦群、CP² 浸入障碍、共形变换、Lefschetz 不动点）。
- **2025 物理**：最有「研究味道」的一份——高斯波包的角动量与光子自旋比值、共形标量场在 de Sitter 度规下等价于有质量标量，都是文献级的标准结论。
- **2025 统计**：题量最少（4 题）但含三年最「怪」的一道题——要求构造出 P(X_{k−1} < X_k) = 1 − 1/(4cos²(π/(n+2))) 的随机变量，常数与 Chebyshev 型递推的谱量同源。
- **2026 代数**：最「数论」的一份——Hecke 双陪集、Jacobi 和与 Hasse 界、三次域整基、局部域分歧分类，几乎不碰抽象代数。
- **2026 分析**：最「古典分析」的一份——π² 无理、BCH 公式、Cauchy–Green 公式、多项式子空间有限维、周期热核。**题面最短（5 题 2724 字符）但每题都可深挖。**
- **2026 计算**：最「研究生」的一份——P1 有限元、凸泛函 Newton / BFGS、位移 QR、SVD 不动点几何、次微分。
- **2026 几何**：三年最难（4.00）且最「现代」的一份——Gauss 映射、Gauss–Bonnet 刚性、双不变度规、Morse 与环路空间、aspherical 流形、Ricci 下界紧性。
- **2026 物理**：最「计算密集」的一份——滑动摆的多情形张力、线圈的近轴 Taylor 展开、φ⁴ 的 RG 流方程，且首次把 Klein 圆盘（纯几何）纳入物理卷。
- **2026 统计**：最「应用统计」的一份——copula、序数结局、分块回归、偏正态、Brownian 出界时间、稳定分布、Bernstein 定理；难度从 4.40 / 4.50 大幅降到 3.33。

### 4.7 对备考者的五条结论

1. **不要指望押到原题**：三年 101 道题里几乎找不到跨年重复的具体对象（唯一的「重复」是 2024 与 2025 几何卷都用 CP^n 出题）。押题收益极低，**押方法收益极高**。
2. **六科的「必考方法内核」分别是**：代数＝Galois / 分歧 / 理想论（三年稳定）；分析＝不等式与估计（每年换载体，从 Fourier 估计到 Hardy 到热核）；几何＝特征类 + 曲率（三年都在，只是切入方式从同调换成 Morse 理论）；计算＝离散格式的稳定性与谱（三年稳定）；物理＝拉格朗日/哈密顿力学 + 一个「现代」分支；统计＝渐近理论（每年换方向，从 O_p 到决策论到 copula）。
3. **小问是得分点**：2024 与 2026 的小问标记都在 95 个以上（平均每题近 3 个小问）。2026 的题型是典型的「爬梯子」，**第一问往往是基础题（不可放弃）**，例如 2026 计算 P4(a) 只要写 QR 分解的唯一性。
4. **「举反例」依然要会，但只需写两行**：2026 把反例降级为小问中的一个验证步骤（A = [[1,1],[0,0]]、ε ≤ 1/4 的反例），不再需要长篇构造。
5. **注意难度在科目间的再平衡**：如果只按 2024 的经验分配复习时间，会严重低估 2026 的几何与计算卷、同时高估统计卷。**难度是逐年重新分配的，不是固定的。**

---

## 5. 不确定 / 存疑清单

> 本节列出所有我**无法确证**的地方。凡涉及题目内容者，一律不做补全猜测。

### 5.1 抽取质量类

| # | 位置 | 问题 | 影响 | 处理 |
|---|---|---|---|---|
| U1 | 2024_2024_Analysis_and_diff_v2.txt（**整卷**） | Cambria-Math 字体抽取导致**字符级错乱**：括号变成 p / q，箭头 → 变成 Ñ，大于号 变成 ą，等号 = 变成引号，减号 − 变成 ´，积分号 ∫ 变成 ˆ，求和号 ∑ 变成 ř，偏导 ∂ 变成 B，属于号 ∈ 变成 ‰ 等 | **不等号方向、上下标、根号覆盖范围不可完全复原** | 统计前做反混淆映射；第 3 节题 1 的解答**刻意给出对 ≥ / ≤ 两种读法都成立的结论（非唯一性）**，避免依赖符号方向 |
| U2 | 2025_computational_and_applied_math.txt | 含控制字符 0x00、0x01、0x10、0x11、0x12、0x13（6 种），出现在矩阵括号与范数双竖线处；read 工具判为 binary 并拒绝读取 | 矩阵的行列边界在抽取中丢失 | 改用 PowerShell 按 UTF-8 读取（已验证可正常解码） |
| U3 | 同上，Problem 2 的矩阵 A | 抽取把全部 64 个元素压成一行（无换行、无括号）。逐位还原后为 8×8、对角线 0、上下副对角线 1 的**路径图 P₈ 邻接矩阵**，数字序列为 01000000 10100000 01010000 00101000 00010100 00001010 00000101 00000010 | 若还原有误，「求 A⁻¹ 谱半径」的答案（1/(2cos(π/9)) ≈ 0.5321）随之改变 | 报告按还原结果给出，并**在此明确标注为「基于逐位还原的推断」** |
| U4 | 2025_statistics.txt | 含控制字符 0x00、0x01、0x12、0x13，出现在 Problem 1 的区间括号处；read 工具判为 binary | 置信区间 CI(X; c1, c2) 的分段定义边界可能不完整 | 改用 PowerShell 读取；题目语义基本可读 |
| U5 | 2024 Analysis Problem 5 | 积分核 B(|x−y|, (x−y)/|x−y| · σ)、x′ = (x+y)/2 + |x−y|σ/2、ξ± = ξ ± |ξ|σ/2 等公式抽取严重残缺（上下标与括号层级丢失） | **题面精确形式存疑** | 仅按「双线性积分算子的 Fourier 变换」理解，已在结构表中标注为推断，不给出完整解析 |
| U6 | 全局 | 所有公式的上下标、矩阵括号、分式结构在纯文本中均被压平（例如 D_λ = diag(π^λ1, …, π^λn) 显示为 pi-λ1 连写） | 逐字转录不可行 | 报告对题面只做「一句话题意」式概括；代表题只摘录可读部分 |

### 5.2 数学内容类

| # | 位置 | 存疑点 |
|---|---|---|
| U7 | 2025 Algebra Problem 5 第 (3) 问 | **疑似原题内部不一致。** 由题给公式算得 Disc(X⁵ − X + 1) = 4⁴(−1)⁵ + 5⁵(1)⁴ = 2869 = 19 × 151，为无平方因子，故 [O_E : Z[α]] = 1、d_(E/Q) = 2869。若取 D = 2869，则由 Gal(E/Q) ≅ S₅ 得 [E : Q(√D)] = 60，塔公式 d_(E/Q) = N(d_(E/Q(√D))) · d_(Q(√D))^60 要求 2869 被 2869⁶⁰ 整除，不可能成立。可能原因：(a) 原题中 D 并非 Disc(f)；(b) 第 (3) 问「非分歧」的修饰范围与本报告理解不同；(c) 抽取或原题存在笔误。**本报告不猜测原题的正确版本，此条挂起。** |
| U8 | 2024 Algebra Question 6 (2)(a) | 抽取给出 (x, y) := ∑_τ τ(x) · τ(y)（同一个 τ 用了两次），但结论要求它是 K_R 上的**内积**且 (ζ^i, ζ^j) = 2^r δ_ij。按标准构造应是带共轭的配对（∑_τ τ(x) · conj(τ(y)) 或 ∑_τ τ(xy) 一类）。**共轭上划线在抽取中整体丢失**，故该式存疑。 |
| U9 | 2024 Algebra Question 2 | D_μ 与 D_λ 的位置（哪个在 GL_n(A) 两侧、哪个在 U(K) 侧）以及 λ_dom ≤ μ_dom 的方向均已按原文转录，但**不等号方向无法用抽取之外的证据验证**。 |
| U10 | 2025 Statistics Problem 1 第 2 问 | 抽取文本中第 2 问缺少「Prove that …」的连接词，两个公式（minimax 不等式与长度期望等式）直接并列，**语义不完整**。本报告按「证明存在同时满足这两条性质的随机化置信区间」理解。 |
| U11 | 2024 统计 P2(b) 与 P5、2025 统计 P3 与 P4、2026 统计 P5 | 这些题的完整解答需要相当长的技术构造，本报告未给出完整解（仅在结构表中给出方法方向）。**尤其 2025 统计 P3 的常数 1 − 1/(4cos²(π/(n+2)))，本报告仅指出它与 Chebyshev 型递推的谱量同源、且 n → ∞ 时趋于 3/4，未给出构造方法。** |

### 5.3 统计口径类

| # | 说明 |
|---|---|
| U12 | **关键词计数是子串计数**（大小写不敏感），存在系统性过计数：norm ← normal / normalized；prime ← primitive；character ← characteristic；wave ← wave packet / wavefunction；metric ← geometric；integral ← integrable。表中数字应读作「词族频次」，不是术语精确计数。 |
| U13 | **小问计数口径不统一**：脚本同时统计 (a)–(j) 与 (1)–(9) 两种形式，因此会把公式编号（例如 2024 Analysis 的 (0.1)(0.2)(0.3)）与文献编号一并计入。2024 Analysis 的小问数 11、2025 Statistics 的 3 都明显偏离实际（前者因字符错乱、后者因控制字符）。**小问统计仅用于相对比较。** |
| U14 | **题量计数**：脚本对六卷分别用「Problem/Question 标记」与「行首编号」两套规则，并取从 1 开始的最长连续段。人工逐卷复核后与脚本一致（34 / 33 / 34），可采信。 |
| U15 | **2024 Analysis 卷的页数无法从抽取文本获得**（页码标记本身被字符错乱破坏），统计表中该卷页数记为 0，已剔除出页数汇总。 |
| U16 | **难度自评是主观标定**（标准见第 0 节），不同评阅人可能相差 ±1；且 2024–2026 无官方解答可比对。 |
| U17 | 本报告第 3 节的 8 道代表题解答**全部为自撰**，未经官方答案或独立复算校验（其中题 4 的 Stiefel–Whitney 计算与题 6 的 SVD 论证为逐步推演，可靠性最高；题 5 的数值估计为量纲级估算）。 |

### 5.4 语料覆盖类

| # | 说明 |
|---|---|
| U18 | **2024–2026 语料中不存在任何团体卷文件**。这不排除实际竞赛仍有团体赛或其他环节（如面试、口试），但**语料无法证实**，故本报告「卷别」列一律填「个人」。 |
| U19 | **2024–2026 语料中不存在官方解答文件**（2020–2022 有 soln）。所有「核心定理/方法」列均为根据题面推断的工具清单，不是官方解法路径。 |
| U20 | 2024 Analysis 卷文件名带 _v2 后缀，且与其他五卷的抽取字体明显不同，**推测该卷 PDF 来源或版本与其余五卷不同**；未在语料中找到 v1 版本。 |

---

## 6. 附录：方法与可复现产物

### 6.1 本报告使用的脚本与产物

| 路径 | 内容 |
|---|---|
| .tmp/burn2026/scripts/yau_2024_2026_stats.py | 最终统计脚本：反混淆、结构统计、关键词频次、趋势指标，输出 stats_2024_2026.md |
| .tmp/burn2026/scripts/yau_stats_v2.py | 中间版本：题量计数修正与趋势指标的探测脚本 |
| .tmp/burn2026/reports/stats_2024_2026.md | 脚本自动生成的统计表（287 行），本报告第 2 节数据的直接来源 |
| .tmp/burn2026/reports/yau_2024_2026_deep_analysis.md | 本报告 |

### 6.2 运行方式

脚本使用本机 Python 3.14（C:\Python314\python.exe），仅依赖标准库（os / re / collections），无需 PyMuPDF。运行命令（在 E:\deepseek_exclusive\math 下）：

    $env:PYTHONPATH = 'E:\deepseek_exclusive\math\pylibs'
    C:\Python314\python.exe .tmp\burn2026\scripts\yau_2024_2026_stats.py

### 6.3 文本规范化流程（脚本中的 load 函数）

1. 按 utf-8-sig 解码（两个含控制字符的文件已验证可正常解码）。
2. 删除除换行与制表符外的全部控制字符（清除矩阵/表格抽取残留，如 0x00、0x01、0x10–0x13）。
3. 连字还原：ﬀ → ff、ﬁ → fi、ﬂ → fl、ﬃ → ffi、ﬄ → ffl。
4. 断行连字符修复：删除「连字符 + 换行 + 小写字母」中的连字符与换行；删除软连字符 U+00AD。
5. 连续空格与制表符折叠为单个空格。
6. **仅对 2024 Analysis 卷**额外施加反混淆映射：p → ( 、q → ) 、Ñ → 箭头、ą → 大于号、引号 → 等号、´ → 减号、ˆ → 积分号、ř → 求和号。

### 6.4 逐卷文件清单（18 份，全部为个人卷）

| 年份 | 文件名 | 学科 | 页数 | 字符 | 题量 |
|---|---|---|---|---|---|
| 2024 | 2024_2024_Algebra.txt | 代数与数论 | 2 | 4438 | 6 |
| 2024 | 2024_2024_Analysis_and_diff_v2.txt | 分析与微分方程 | 抽取异常 | 2471 | 5 |
| 2024 | 2024_2024_Computational_Math.txt | 计算与应用数学 | 3 | 4310 | 6 |
| 2024 | 2024_2024_GeometryTopology.txt | 几何与拓扑 | 1 | 2303 | 6 |
| 2024 | 2024_2024_Math_physics.txt | 数学物理 | 4 | 6715 | 6 |
| 2024 | 2024_2024_statistics.txt | 概率统计 | 2 | 3992 | 5 |
| 2025 | 2025_algebra.txt | 代数与数论 | 2 | 3629 | 5 |
| 2025 | 2025_analysis.txt | 分析与微分方程 | 2 | 2621 | 6 |
| 2025 | 2025_computational_and_applied_math.txt | 计算与应用数学 | 3 | 3551 | 6 |
| 2025 | 2025_Geometry_and_Topology.txt | 几何与拓扑 | 1 | 1983 | 6 |
| 2025 | 2025_physics.txt | 数学物理 | 4 | 8122 | 6 |
| 2025 | 2025_statistics.txt | 概率统计 | 2 | 3085 | 4 |
| 2026 | 2026_2026_Algebra_and_Number_Theory.txt | 代数与数论 | 2 | 2604 | 5 |
| 2026 | 2026_2026_analysis.txt | 分析与微分方程 | 2 | 2724 | 5 |
| 2026 | 2026_2026_Computation.txt | 计算与应用数学 | 2 | 4413 | 6 |
| 2026 | 2026_2026_Geo_Topology.txt | 几何与拓扑 | 2 | 3071 | 6 |
| 2026 | 2026_2026_physics.txt | 数学物理 | 3 | 6082 | 6 |
| 2026 | 2026_2026_statistics.txt | 概率统计 | 2 | 3101 | 6 |

---

## 关键数字摘要

1. 负责时段：**2024、2025、2026** 三年，共 **18 份 txt 卷**，**101 道题**，**69215 个抽取字符**。
2. 卷别构成：**个人赛 6 科 × 3 年 = 18 卷**；**团体卷 0 份**（团体卷自 2020 年起已从语料中消失，2019 为最后一次出现）。
3. 官方解答：**2023–2026 共 0 份**（2020 / 2021 / 2022 各有 5–6 份 soln 文件）。
4. 逐年题量：**2024 = 34 题**（24229 字符）、**2025 = 33 题**（22991 字符）、**2026 = 34 题**（21995 字符）。
5. 平均每题字符数：**712.6 → 696.7 → 646.9**，三年下降 **9.2%**（题面持续变短）。
6. 小问标记总数：**95 → 68 → 97**；2026 平均每题 **2.85** 个小问（短题面 + 密集阶梯）。
7. 单卷最长：**2025 数学物理，8122 字符 / 4 页**；单卷最短：**2025 几何与拓扑，1983 字符 / 1 页**（同届内体量差 4.1 倍）。
8. 题量最少的单卷：**2025 概率统计，仅 4 题**（三年唯一低于 5 题者）；2026 概率统计回升至 6 题。
9. 全卷难度均值（自评 1–5）：**2024 = 3.71、2025 = 3.70、2026 = 3.59**。
10. 分科难度三年加权均值：**代数与数论 4.06 > 概率统计 4.00** > 几何与拓扑 3.67 > 数学物理 3.56 > 计算与应用 3.39 > 分析与微分方程 3.38；全 101 题总加权均值 **3.66**。
11. 最大难度变动：**概率统计 4.40 → 4.50 → 3.33**（2026 骤降 1.17，同时题量 4 → 6，属"降难增面"）；**几何与拓扑 3.33 → 3.67 → 4.00**（2026 升至三年最高）。
12. 判定句式（Does there exist / Is the / Can …）：**22 → 18 → 12**，2026 比 2024 下降 **45%**。
13. 构造 / 反例 / 证伪动词：**4 → 4 → 0**，2026 年**完全归零**（反例降级为小问内的验证步骤）。
14. 证明要求（prove + show that）：**109 次**（2.4 节正则口径 30 / 42 / 37），是绝对主导题型；若按 2.2 节逐词计数则为 111 次（show that 61 + prove 50）。纯求解（compute / derive / determine / find / calculate）**102 次**。
15. 词频迁移（2024 → 2025 → 2026）：p-adic / 局部域 **16 → 8 → 5**；曲率词族 **6 → 4 → 11**；线性代数词族 **11 → 4 → 15**；QFT 词族 **3 → 0 → 7**；广义相对论词族 **2 → 4 → 0**。
16. 单卷题量取值范围 **4–6 题**；六科三年题量总和分别为 **16 / 16 / 18 / 18 / 18 / 15**（代数与数论 / 分析与微分方程 / 计算与应用 / 几何与拓扑 / 数学物理 / 概率统计），合计 101。
17. 2026 首次下放的现代工具：Gysin 序列与 Euler 类、Morse 指标、环路空间 CW 型、Poincaré 级数、BFGS、次微分与法锥、copula 与 Sklar 定理、Frisch–Waugh–Lovell 定理、维数正规化 + 重整化群流方程。
18. 年份彩蛋：2024 分析卷的 x^2024、2025 分析卷的常数 2025、2026 几何卷的 S^2026（三处均已用文本检索核实，可 100% 复核）。
19. 抽取异常卷数：**2 份含控制字符**（2025 计算、2025 统计，read 工具判为 binary），**1 份整卷字符错乱**（2024 分析，Cambria-Math）。
20. 存疑条目：**20 条**（抽取质量 6 条、数学内容 5 条、统计口径 6 条、语料覆盖 3 条），其中 **1 条为疑似原题内部不一致**（2025 代数 P5 第 (3) 问）。本报告自撰题解 **8 道**，覆盖 3 年与全部 6 个科目，均未经官方答案校验。

---

*报告完 — 全部数字均可由 .tmp/burn2026/scripts/yau_2024_2026_stats.py 重跑复现。*
