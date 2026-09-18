# 丘成桐大学生数学竞赛 · 总决赛真题分析
## 应用与计算数学（Applied & Computational Math）+ 数学物理（Mathematical Physics）

> 语料：`corpus/finals/`（195 个 txt，由 `sources/finals` 的 PDF 抽取）
> 索引：`data/finals_index.json` / `data/finals_manifest.json`
> 统计脚本：`scripts/finals_app_phys_stats.py`（输出 `finals_app_phys_stats.json`、`finals_app_phys_tables.md`）
> 2020 解密脚本：`scripts/_finals_2020_extract.py`
> 撰写日期：本轮分析；本报告只覆盖 **总决赛（Final / Oral Exam）** 卷，讨论「初赛」时一律指 `sources/prelim` 的笔试语料。

---

## 1. 可分析范围声明

### 1.1 筛选口径

`finals_index.json` 共 195 条记录。按 subj 含 `Applied` 或 `Mathematical_Physics` 筛出 **52 条**，占全语料 26.7%：

| 科目 | 记录数 | 卷别构成 |
|---|---|---|
| 2012-2025 Applied Math and Computational Math | 40 | Individual 15 / Overall 13 / Team 11 / 考纲 1 |
| 2022-2025 Mathematical_Physics | 12 | Individual 4 / Overall 4 / Team 3 / 考纲 1 |

### 1.2 文字层状态（**关键修正**）

`finals_index.json` 的 `chars` 字段显示有 3 条记录 `chars=0`（2020 年三份卷），另有 8 条 `chars<800`。按任务给出的「chars<800 视为无文字层」口径会被判为不可分析，**但实测并非如此**：

| 类别 | 计数 | 明细 | 是否可分析 |
|---|---|---|---|
| chars = 0（索引口径「无文字层」） | 3 | 2020 Individual set1 / set2 / 2020 Overall | **可分析**——PDF 只是被口令加密，文件名已给出密码 `Yau-ACM20`；`fitz` 的 `authenticate("Yau-ACM20")` 返回 6（成功），解密后 2 页、1618 / 1878 / 1892 字符，文字层完整 |
| 200 ≤ chars < 800（稀疏但可读） | 8 | 2013 Overall(545)、2015 Overall(213)、2016 Overall(543)、2017 Overall(537)、2018 Overall(389)、2018 Individual(789)、2018 Team(652)、2022 Overall(733) | 可分析；均为「一道题一张纸」的短卷，字符少是题量少，不是扫描件 |
| chars ≥ 800（正常） | 44 | — | 可分析 |
| **合计可分析** | **55 个卷面单元**（52 原文件 + 3 个 2020 解密文本） | — | **不可分析：0 个** |

结论：**本子领域总决赛卷没有真正的扫描件/图片版**，不存在因无文字层而无法分析的卷。此前「约 65 个文件几乎没有文字层」的判断会命中其它科目（代数/几何/分析/概率）的 2020 加密卷与部分 Overall 短卷；就 Applied + MathPhys 而言，唯一障碍（2020 加密）已解除。

### 1.3 可分析/不可分析的年份—卷别矩阵

| 年份 | ACM Individual | ACM Overall | ACM Team | MathPhys Individual | MathPhys Overall | MathPhys Team |
|---|---|---|---|---|---|---|
| 2012 | ✅ 2 题 | ✅ 1 | ✅ 2 | — | — | — |
| 2013 | ✅ 2 | ✅(稀疏) | ❌ 缺卷 | — | — | — |
| 2014 | ✅ 见注 A | 见注 A | ✅ 3 | — | — | — |
| 2015 | ✅ 3 | ✅(稀疏) | ✅ 3 | — | — | — |
| 2016 | ✅ 2 | ✅(稀疏) | ❌ 缺卷 | — | — | — |
| 2017 | ✅ 2 | ✅(稀疏) | ✅ 3 份文件 | — | — | — |
| 2018 | ✅(稀疏) | ✅(稀疏) | ✅(稀疏) | — | — | — |
| 2019 | ✅ 5（选 3） | ✅ 3 | ✅ 3 | — | — | — |
| 2020 | ✅ 2 套（解密） | ✅（解密） | ❌ 缺卷 | — | — | — |
| 2021 | ✅ 3 | ✅ 2 | ❌ 缺卷 | — | — | — |
| 2022 | ✅ 3 | ✅(稀疏) | ❌ 缺卷 | ✅ 3 | ✅ 2 | ❌ 缺卷（MP 团体 2022 未设） |
| 2023 | ✅ 4 | ✅ 1 | ✅ 3 | ✅ 4（选 3） | ✅ 2（选 1） | ✅ 3（选 2） |
| 2024 | ✅ 4 | ✅ 2 | ✅ 3 | ✅ 4（选 3） | ✅ 2（选 1） | ✅ 3（选 2） |
| 2025 | ✅ 4 | ✅ 2 | ✅ 3 | ✅ 4（选 3） | ✅ 2（选 1） | ✅ 3（选 2） |

- **注 A（2014）**：`2014 Applmath (Individual and Overall).pdf` 是 **4 份独立单页文档的拼接件**（6 页）。页 1 抬头 `S.-T. Yau College Student Mathematics Contest / Applied Mathematics, Individual, 2014`；页 4–6 抬头 `Oral exam, applied and computational mathematics, individual, 2014`（页码 1–3）；页 2、页 3 无抬头、页脚各自标「1」，与页 1 尺寸不同（579×819 vs 595×770）。据此**推断**页 1 + 页 4–6 属 Individual（3 题），页 2–3 属 Overall（2 题）。该文件在 `finals_index.json` 中被登记为 Individual，**Overall/2014 目录下无独立文件**，故 2014 Overall 只能从该拼接件中恢复，卷别归属标注为「推断」。
- **ACM Team 缺卷年份**：2013、2016、2020、2021、2022（5 年）；**MathPhys Team 仅 2023–2025**（2022 未设团体卷）。
- **MathPhys 是 2022 年新设科目**：总决赛与初赛同步从 2022 年开始（初赛 MathPhys 语料亦为 2022–2026，每年 6 题）。

### 1.4 两份官方考纲（Syllabus）的存在

| 考纲 | 文件 | 页/字符 | 覆盖主题数 |
|---|---|---|---|
| Computational and Applied Mathematics | `SyllabusonComputationalandAppliedMathematics.pdf` | 3 页 / 2462 字符 | 8 个大主题 + 9 本参考书 |
| Mathematical Physics | `Syllabus on Mathematical Physics.pdf` | 3 页 / 2973 字符 | 6 个大主题 + 参考书 |

App/Comp 考纲 8 个主题：插值与逼近（含 FFT、有理逼近、样条、最小二乘）／非线性方程求解（二分、Newton、拟 Newton、不动点、多项式求根）／线性方程组与特征值问题（经典与现代迭代、条件数、SVD、大型稀疏）／ODE 数值解（单步/多步、稳定性、精度、收敛性、绝对稳定性、长时间行为、刚性）／PDE 数值解（有限差分、有限元、谱方法：稳定性/精度/收敛性、Lax 等价定理）／数学建模、模拟与应用分析（标度与渐近、驻相、边界层、Monte-Carlo）／线性与非线性规划（单纯形、内点、罚方法、Newton、同伦、不动点、动态规划）／（第 3 页续）参考书 9 本。

MathPhys 考纲 6 个主题：经典力学（最小作用量、Euler-Lagrange、Noether、Kepler、刚体；Hamilton 方程、Poisson 括号、Liouville、正则变换、Hamilton-Jacobi）／电动力学（静电静磁、Maxwell、守恒律、电磁波、辐射；镜像法、分离变量、多极展开）／热力学与统计物理（热力学势、相平衡与相变、配分函数、熵；微正则/正则/巨正则、Boltzmann-Bose-Fermi 分布；理想气体、顺磁体、简并 Fermi、光子声子、BEC）／量子力学（Hilbert 空间、态与可观测量、Schrödinger 方程与两种绘景、正则量子化、密度矩阵；谐振子、氢原子、势阱；对称性、角动量、自旋、全同粒子、原子结构；微扰论、散射、近似方法）／广义相对论（度规、张量、微分形式、流形、联络、曲率、测地线、tetrad、Lie 导数、Killing 矢量；等效原理、Einstein 方程、Hilbert-Einstein 作用量；Minkowski/de Sitter/anti-de Sitter/黑洞精确解；因果结构）／量子场论（经典场论、Noether；正则量子化与路径积分；Poincaré 群表示、Dirac 方程；S 矩阵、LSZ、Feynman 传播子与规则、正规编序、Wick 定理、光学定理、定域性；重整化、正规化与截断、抵消项、重整化群）。

---

## 2. 逐年逐卷结构表

> 题量以**人工逐份阅读**为准（脚本自动切分单元数见 `finals_app_phys_tables.md`，2020 首次计入后为 128 个单元；差异主要来自「一题多小问」被脚本再切）。难度为**自评 1–5**（5 = 需要完整研究级推导）。
> 表中「Overall」= 卷面自称 All-Round / Overall（全能赛）。

### 2.1 Applied & Computational Math — Individual（个人赛，13 年可分析，共 41 题）

| 年份 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|
| 2012 | 1 | 求形如 IN=(1/N)[a0(f0+fN)+a1(f1+f_{N−1})+Σf_i] 的求积公式能达到的最高阶 k，并给出求 a0,a1 的步骤 | 数值求积 | 矩条件（精确到 k 阶）、Euler–Maclaurin、待定系数 | 3 |
| 2012 | 2 | 用「只用减法与除 2」设计求 gcd(m,n) 的高效算法并估计复杂度 | 算法/离散 | 二进制 GCD（Stein 算法）、位运算复杂度摊还 | 3 |
| 2013 | 1 | (a) 给出 A+uvᵀ 可逆的条件并求其逆；(b) 把 A 第一列换成 b 后求 (Ā)⁻¹ | 数值线性代数 | Sherman–Morrison 秩一修正、分块求逆 | 3 |
| 2013 | 2 | 三角形网格上证明离散 Gauss–Bonnet（含多边形面、带边界两种推广） | 离散微分几何 | 角亏离散 Gauss 曲率、Euler 数 χ=V+F−E | 3 |
| 2014 | 1 | 求三对角矩阵（对角 b、上 c、下 a，ac>0）的特征值与特征向量 | 数值线性代数 | 三对角 Toeplitz/递推、Chebyshev 多项式、相似变换 | 3 |
| 2014 | 4 | 最优质量传输：power Voronoi 图的最优性、由凸 PL 函数梯度给出运输映射 | 最优传输/离散几何 | Kantorovich 对偶、Voronoi 图、凸函数梯度映射 | 4 |
| 2014 | 5 | Circle packing：证明「离散共形因子 u↦曲率 K」是微分同胚（先证导数余弦定理、单三角形、再全网格） | 离散共形几何 | 余弦定理求导、Jacobi 矩阵可逆性、凸能量 | 4 |
| 2015 | 1 | n×n 矩阵（对角 1、相邻 r）解 Ax=b，证明 ‖x‖≤C‖b‖ 且 C 与 n 无关 | 数值线性代数 | 三对角对角占优/M-矩阵、离散 Laplace 逆的一致范数界 | 3 |
| 2015 | 2 | 证明分段线性插值在 [0,π] 上 ‖u−Π_h u‖≤h²/π²‖u″‖、‖u′−(Π_h u)′‖≤h/π‖u″‖ | 插值/有限元 | Poincaré 不等式、插值误差估计 | 3 |
| 2015 | 3 | 证明 Newton 迭代 x_{n+1}=x_n−(x_n^k−C)/(k x_n^{k−1}) 对任意 x0>0 收敛 | 非线性方程 | Newton 法全局收敛、凸性/单调有界 | 2 |
| 2016 | 1 | Arnoldi 过程：(a) 写算法；(b) breakdown 时 K_n 不变且 H_n 特征值属于 A；(c) min‖p_n(A)b‖ 的最优多项式是 H_n 的特征多项式 | 数值线性代数 | Arnoldi/Krylov、隐式 Q 定理、Galerkin 最优性 | 4 |
| 2016 | 2 | FitzHugh–Nagumo 模型（Hodgkin–Huxley 简化）：慢/快解展开、慢流形、极限环 v 的极值与周期估计 | 应用分析/动力系统 | 奇异摄动（多时间尺度）、慢流形、相平面分析 | 4 |
| 2017 | 1 | Burgers 方程：Hopf–Cole 变换导出 φ 的方程并求解；ν=0 时证明光滑初值在 T_b=−1/min u₀′ 破裂（激波） | 应用 PDE | Hopf–Cole 变换、热核、特征线法、梯度 catastrophe | 3 |
| 2017 | 2 | (a) 推导 ROF 图像正则化的 Euler–Lagrange 方程；(b) cartoon-texture 分解的 EL 方程组；(c) 证明 ‖∇κ(u)‖=μ | 变分法/反问题 | 变分法、TV 曲率算子 κ=∇·(∇u/‖∇u‖) | 4 |
| 2018 | 1 | 复合梯形公式：(a) 构造；(b) f∈C² 时二阶精度；(c) f 光滑周期时谱精度 | 数值求积 | Euler–Maclaurin 展开、Poisson 求和 | 3 |
| 2018 | 2 | 证明 Stokes 方程的解 u 是所有散度为零、边界为 g 的 v 中耗散泛函 ∫|∇v|² 的极小元 | 变分/PDE | 能量法、散度约束变分 | 3 |
| 2019 | 1 | 证明 companion 矩阵 C 与 Vandermonde 矩阵 V 满足 V C V⁻¹=diag(λ₁,…,λ_n) | 数值线性代数 | 特征多项式、Vandermonde、相似变换 | 2 |
| 2019 | 2 | 证明 Simpson 法则误差 ∫f−(b−a)/6·[f(a)+4f(mid)+f(b)] = −((b−a)/2)⁵ f⁽⁴⁾(ξ)/90 | 数值求积 | 插值余项、Hermite 插值、积分中值 | 2 |
| 2019 | 3 | 不动点迭代：收敛的充分条件与收敛阶判据；构造 Steffensen 型 G(x) 并证明不动点性质 | 非线性方程 | 压缩映射、收敛阶、Aitken/Steffensen 加速 | 3 |
| 2019 | 4 | 已知一个时二阶、空四阶的紧致隐格式，问如何修改以处理变系数 u_t=σ(x)u_xx 且保持精度 | 数值 PDE | 紧致（Padé）差分、变系数离散 | 4 |
| 2019 | 5 | 块 2×2 系统 Ax₁+Bx₂=b₁, Bx₁+Ax₂=b₂ 的块 Jacobi 迭代收敛的充要条件 | 数值线性代数 | 块迭代、谱半径、矩阵多项式 | 3 |
| 2020 (set1) | I | 广义逆 A⁺=UF⁺Vᵀ：(1) x*=A⁺b 是最小二乘解；(2) lim(αI+AᵀA)⁻¹Aᵀ=A⁺ | 数值线性代数 | SVD、Tikhonov 正则化极限 | 3 |
| 2020 (set1) | II | 紧致格式 [(v^{n+1}−v^{n−1})/(2τ)] + a(1+h²δ²/6)⁻¹δ₀vⁿ=fⁿ 的稳定充要条件 \|aλ\|<1/√3，及变系数改造 | 数值 PDE | von Neumann 分析、Padé 紧致格式 | 4 |
| 2020 (set1) | III | 证明平面系统 x′=0.5x+2.5y−x(x²+y²), y′=−0.5x+1.5y−y(x²+y²) 至少有一个周期解 | 动力系统 | Poincaré–Bendixson、Lyapunov 函数/环域 | 3 |
| 2020 (set2) | I | Lanczos 迭代：(1) Q_k 列正交且张成 K_k；(2) 说明算法用途 | 数值线性代数 | Lanczos/Krylov 子空间 | 3 |
| 2020 (set2) | II | 振荡 ODE y″+λ²y+g(y)=0：常数变易法写积分形式，导出 y_{n+1}=2cos(λτ)y_n−y_{n−1}−(sin λτ/λ)g(y_n)，并证误差 ≤Cτ² | 数值 ODE | 常数变易公式、三角/指数型积分器 | 4 |
| 2020 (set2) | III | 概率测度上泛函 F[ρ] 的 Euler–Lagrange 方程，及其 Wasserstein 梯度流下 F 单调递减 | 变分/最优传输 | 变分、Wasserstein 梯度流、熵 | 4 |
| 2021 | I | Richardson 迭代 x^{(k+1)}=(I−ωA)x^{(k)}+ωb：(1) 收敛 iff 0<ω<2/λ_n；(2) 最优 ω=2/(λ₁+λ_n) 与 ρ(G_ω) 分段公式；(3) SPD 时 ρ=(κ₂−1)/(κ₂+1) | 数值线性代数 | 谱半径、条件数、Chebyshev 型最优阻尼 | 3 |
| 2021 | II | 能量泛函 E[u]=∫(½\|∂_x u\|²+(1−\|u\|²)²/(4ε²)) 的梯度流：E 递减、初值在 [−1,1] 则永在 [−1,1]、设计能量递减格式 | 数值 PDE/能量稳定 | 凸分裂、最大值原理、能量法 | 4 |
| 2021 | III | Toda 型系统 da_k/dt=2(b_k²−b_{k−1}²), db_k/dt=b_k(a_{k+1}−a_k)：证明 L(a,b) 特征值与 t 无关且 b_k→0 | 可积系统/数值线代 | Lax 对、等谱流、逆散射 | 4 |
| 2022 | I | Allen–Cahn 方程：能量递减、半隐格式 u^{n+1} 唯一且能量稳定 | 数值 PDE/能量稳定 | 凸分裂、凸性单调算子 | 3 |
| 2022 | II | f(x)=x^{n+1}−bⁿx+abⁿ 恰有两个正根 iff a<n/(n+1)^{1+1/n}·b；且 Newton 法自 a 收敛到小根、自 b 收敛到大根 | 非线性方程 | 凸性、Newton 吸引域、AM–GM | 3 |
| 2022 | III | 三对角矩阵 Jacobi 与 Gauss–Seidel 特征多项式的关系 p_{B_J}(λ)=det(−D⁻¹)det(L+λD+U) 等，推出 ρ(B_GS)=ρ(B_J)² | 数值线性代数 | 迭代矩阵谱理论、行列式恒等式 | 3 |
| 2023 | 1 | (a) 证明 det=1 的正交阵可写成有限个 Givens 旋转之积；(b) 给出算法 | 数值线性代数 | Givens 旋转、QR 分解 | 3 |
| 2023 | 2 | 自伴阵 k 个主特征值的幂迭代：PX^{(m)} 列独立、X^{(m)} 列独立、tan∠(X^{(m+1)},W_k)≤\|λ_{k+1}/λ_k\|tan∠(X^{(m)},W_k) | 数值线性代数 | 子空间迭代、主角、谱隙 | 4 |
| 2023 | 3 | 双速率显式 Euler（g 计算更贵）：(a) 局部二阶；(b) 线性问题 x′=−x+y,y′=−y 的稳定性条件 | 数值 ODE | 多速率方法、放大矩阵稳定性 | 3 |
| 2023 | 4 | 对流方程五点格式：(a) CFL 条件；(b) 放大因子 g(ω) 与 von Neumann 条件，并与 CFL 比较 | 数值 PDE | CFL、von Neumann、依赖域 | 3 |
| 2024 | 1 | 求 (ST−λI)x=b（S,T 上三角）的 O(n²) 算法 | 数值线性代数 | Sylvester 结构、序贯回代 | 3 |
| 2024 | 2 | 由 d_{n+1}−d_n≤k(g_n d_n+h_n) 及三类部分和界，证明 d_n≤(a₂+a₃/r)exp(a₁) | 数值分析 | 离散 Gronwall 不等式 | 3 |
| 2024 | 3 | 周期变系数热传导均匀化：(1) H¹₀ 弱解唯一；(2) u_ε ⇀ u 于 H¹₀ 并求极限系数 A | PDE/均匀化 | Lax–Milgram、双尺度渐近、调和平均 | 4 |
| 2024 | 4 | 反应扩散方程 Neumann 边值 FTCS 格式：(a) 稳定性对 Δt 的条件；(b) 误差 e^n 收敛 | 数值 PDE | von Neumann、Lax 等价、一致性+稳定性 | 3 |
| 2025 | 1 | 稳态 Schrödinger 反问题：证明 F(V)=M_ψ 的 Fréchet 可导并给出导数；设计 Newton 型算法 | 反问题 | 隐函数定理、形状/边界导数 | 4 |
| 2025 | 2 | 变系数输运 u_t+a(x)u_x+a′(x)u=0：守恒形式与守恒含义、二阶中心数值通量格式与条件稳定、a≡a₀ 时的 CFL | 数值 PDE | 守恒律、数值通量、von Neumann | 3 |
| 2025 | 3 | 固定面积下等周问题：变分形式化并证明圆最小周长 | 变分法 | Lagrange 乘子、Euler–Lagrange | 2 |
| 2025 | 4 | 证明单位 4-范数球 x⁴+y⁴+z⁴≤1 与平面 x+y+z=0 的交是圆盘 | 凸几何/优化 | 对称性、Lagrange 乘子、锥优化 | 2 |

### 2.2 Applied & Computational Math — Overall / All-Round（全能赛，13 年可分析，共 18 题）

| 年份 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|
| 2012 | 1 | L2 投影到分段 k 次多项式空间：(1) 证 ‖u−u_h‖≤Ch^{k+1} 并说明 C 对导数的依赖；(2) 证 \|∫(u−u_h)φ\|≤Ch^{2k+2} | 有限元/逼近 | 正交投影、Aubin–Nitsche 对偶论证 | 4 |
| 2013 | 1 | 用同伦 H(x,t)=(1−t)(x−a)+t(x−f(x)) 证明 Brouwer 不动点：H⁻¹(0) 是光滑曲线、曲线留在 Dⁿ 内、如何沿曲线跟踪（弧长参数化） | 数值/拓扑 | Sard 定理、隐函数定理、同伦/路径跟踪 | 4 |
| 2015 | 1 | 求 εx³−x−2=0 三个根关于小 ε 的渐近展开 | 渐近分析 | 奇异摄动、尺度匹配（一正则 + 两奇异根） | 3 |
| 2016 | 1 | 设计只访问每个 a(i) 一次的最大子段和算法并给出正确性口头证明 | 算法 | Kadane 单遍扫描、循环不变式 | 2 |
| 2017 | 1 | m_t=−a×m 的显式时间推进格式：(a) 稳定性分析；(b) 改进稳定性的数值策略 | 数值 ODE | 反对称矩阵谱、保持范数格式（Crank–Nicolson/旋转） | 3 |
| 2018 | 1 | du/dt=a×u 前向差分格式恒不稳定；讨论改进稳定性的办法 | 数值 ODE | 特征值模为 1 落在单位圆上（放大因子恒 >1） | 2 |
| 2019 | 1 | 证明对任意 n≥3 存在无限多个形如 xⁿ+(6a−1)x²+(7b−3)x+25c 的不可约多项式 | 代数（混入 ACM 全能卷） | 模 p 不可约、Eisenstein 型构造 | 3 |
| 2019 | 2 | 0-1 矩阵 A（a_ij=1 当 i+j 偶，2n 阶）：证明 ‖A‖_F=‖A‖_∞=n 且 Σ(1/2n)^k A^k = A/n | 数值线性代数 | Frobenius/∞ 范数、矩阵级数、幂等结构 | 2 |
| 2019 | 3 | Tikhonov 泛函 J(f)=½‖Tf−z‖²+β/2‖f‖²：(1) 变分方程；(2) 各阶导数方程；(3) F′(β),F″(β)；(4) z∉ker T* 时 F 严格单调且严格凹 | 反问题/泛函 | Hilbert 空间对偶、隐函数微分 | 4 |
| 2021 | I | 幂迭代 x_{m+1}=Ax_m：(1) 主角与投影的关系式；(2) tan∠(x_{m+1},W_k)≤\|λ_{k+1}/λ_k\|tan∠(x_m,W_k) | 数值线性代数 | 正交投影、子空间主角、谱隙 | 4 |
| 2021 | II | GMRES：近似解是三角最小二乘问题、残差正交性、残差范数公式、完整算法 | 数值线性代数 | Arnoldi/GMRES、Krylov 投影 | 4 |
| 2022 | I | 奇异摄动 ODE ε²y″+(µ²+1/ε²)y=f：(1) 常数变易积分形式；(2) 构造精度与 ε 无关的二阶格式；(3) 证明收敛率 | 数值 ODE | 变分常数公式、ε-一致（uniform）收敛 | 4 |
| 2022 | II | 证明 u_t=u_xx+u 的显式差分格式在 Δt/Δx²≤1/2 时稳定 | 数值 PDE | von Neumann 分析 | 2 |
| 2023 | 1 | 非线性 Klein–Gordon 方程：(1) Hamiltonian E(t) 守恒；(2) 构造时空二阶显格式并求线性稳定条件；(3) 构造离散能量守恒格式并证明 | 数值 PDE/能量守恒 | 能量法、辛/守恒格式、线性化稳定性 | 4 |
| 2024 | 1 | L1 最小化稀疏恢复：(a) 每个 s-稀疏 x₀ 是唯一解 iff Ker(A)∩C_s={0}；(b) C_s∩B₂ 的有界性 | 压缩感知 | 零空间性质、凸几何、s-范数 | 4 |
| 2024 | 2 | (a) 一维随机游走 → 扩散方程（h²/τ→d）；(b) 二维随机游走 → 扩散方程；(c) 用边界观测 M_f=u\|∂Ω×(0,T) 反演初值 f（含 δ 源定位） | 随机过程/反问题 | 扩散极限、唯一延拓/反演、矩方法 | 4 |
| 2025 | 1 | proximal 算子：(a) prox_{α,‖·‖₁} 显式解；(b) prox_{α,‖·‖₂} 显式解；(c) 证明 prox_{f+g}=prox_g∘prox_f | 凸优化 | 软阈值、Moreau 分解、次梯度 | 3 |
| 2025 | 2 | εy″+(1+ε)y′+y=0, y(0)=0,y(1)=1 的 ε→0 一致渐近 | 渐近分析 | 边界层、匹配渐近展开 | 3 |

### 2.3 Applied & Computational Math — Team（团体赛，7 个年份 / 11 份文件，共 26 题）

| 年份 | 文件 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|---|
| 2012 | 2012 Applmath (Team) | 1 | 对 u_t+u_x=u 的差分格式，用 ‖u^{n+1}‖≤‖u^n‖ 定义稳定性是否合理？不合理则修改定义并说明 | 数值 PDE | 离散 L2 稳定性定义、增长因子、加权内积 | 3 |
| 2012 | 同 | 2 | 证明根树中「度≥3 的顶点集」到「非根叶集」存在单射 f，使每个 v 位于 r 到 f(v) 的路径上 | 组合/图论 | 树结构归纳、Hall 型计数 | 3 |
| 2014 | 2014 Applied (Team) | 1 | 证明分段线性插值误差 ‖u−Π_h u‖≤h²/π²‖u″‖，‖u′−(Π_h u)′‖≤h/π‖u″‖ | 插值/有限元 | Poincaré 不等式（与 2015 Individual 同题） | 3 |
| 2014 | 同 | 2 | claw-free 图（无 K₁,₃ 诱导子图）满足 α≤2n/(δ+2) | 图论 | 独立集、局部结构计数、度序列 | 4 |
| 2014 | 同 | 3 | 隐式格式 u^{n+1} 解热方程带源项，证明 ‖u^k‖²≤‖u⁰‖²+C₄²M² 且与时间步无关 | 数值 PDE/能量法 | Poincaré、归纳、一致 L² 界 | 4 |
| 2015 | 2015 Applied (Team) | 1 | 求广义特征值问题（三对角 (2,−1) 乘 x = λ(4,1) 乘 x）的 λ 与特征向量 | 数值线性代数 | 广义特征问题、Toeplitz 谱 | 3 |
| 2015 | 同 | 2 | 最速下降法证明 g(x_{k+1})≤((k−1)/(k+1))² g(x_k)≤((k−1)/(k+1))^{2(k+1)}g(x₀) | 优化/数值线代 | Kantorovich 不等式、精确线搜索 | 3 |
| 2015 | 同 | 3 | 液滴平衡形状：由总界面能最小化证明曲线曲率为常数（圆） | 变分法 | 变分、Lagrange 乘子、Laplace 压力 | 3 |
| 2017 | 2017 Applied (Team) | 1 | 三角形角的导数：∂θ_i/∂l_i=l_i/(2A)、∂θ_i/∂l_j=−(l_i/2A)cosθ_k；共形因子缩放后的 cot 形式；急性三角形邻域的微分同胚 | 离散共形几何 | 导数余弦定理、Jacobi 矩阵 | 4 |
| 2017 | 同 | 2 | Lanczos 迭代：(a) AQ_k=Q_kT_k+r_k e_kᵀ；(b) 正交列张成 K_k；(c) k=m=rank(K_n) 时终止；(d) 算法用途 | 数值线性代数 | Lanczos、三项递推、Krylov | 3 |
| 2017 | 2017 Applied (Team) (2) | 1 | 最优质量传输：power Voronoi 映射的 L² 运输代价最小；上包络凸 PL 函数诱导 Voronoi 图 | 最优传输 | Kantorovich 对偶、凸对偶 | 4 |
| 2017 | 2017 Applmath (Team) | 1（含 4 小问） | 由质量守恒与动量守恒推导流体 PDE（密度、速度、压强）；给出两种质量/动量变化表达式 | 流体力学 | Reynolds 输运定理、守恒律、Euler/NS 方程 | 3 |
| 2018 | 2018 Applied (Team) | 1 | 用 ℓ 个标准正交向量 ψ_i 最小化 J=Σ‖y_j−Σ(y_jᵀψ_i)ψ_i‖² | 数值线性代数 | PCA/SVD、Eckart–Young | 3 |
| 2018 | 同 | 2 | n 个超平面把 R^d 分成凸胞的最大数 f_d(n)：d=2 公式并证明，再给一般 d 的公式 | 组合几何 | 递推 f_d(n)=f_d(n−1)+f_{d−1}(n−1)、求和恒等式 | 3 |
| 2019 | 2019 Applied (Team) | 1 | 整数系数秩 r≤n−1 齐次方程组有小整数解：(i) ‖x‖_∞≤K 的解数 ≤(2K+1)ⁿ；(ii) 用抽屉原理证存在 0≠x∈Zⁿ, Ax=0 且 ‖x‖_∞≤(2nH)^{n−1} | 算法/数论 | Dirichlet 抽屉原理、计数 | 3 |
| 2019 | 同 | 2 | (i) 变系数二阶导离散 (a_{i+1}+a_i)(u_{i+1}−u_i)−(a_i+a_{i−1})(u_i−u_{i−1})/2h² 的精度阶；(ii) 证明离散系统 Gauss–Seidel 收敛 | 数值分析/PDE | Taylor 展开、M-矩阵、对角占优 | 4 |
| 2019 | 同 | 3 | 最大熵原理：(i) 熵最大分布为指数族 p_i=exp(Σλ_j f_j(x_i))/Z；(ii) E_j=∂log Z/∂λ_j | 统计物理/优化 | Lagrange 乘子、配分函数、对偶 | 3 |
| 2023 | 2023 ACM GROUP | 1 | 三对角阵 LU 部分主元：(i) 增长因子 ρ≤2；(ii) 列对角占优时带/不带主元逐步等价（不换行） | 数值线性代数 | 增长因子、对角占优、主元分析 | 4 |
| 2023 | 同 | 2 | λ-变形 Legendre 变换 f^{(λ)}：证明 f(x)+f^{(λ)}(u^{(λ)})=λ⁻¹log(1+λ⟨x,u^{(λ)}⟩)、λ-梯度的 Jacobian 计算、(f^{(λ)})^{(λ)} 是否等于 f | 凸分析 | Legendre–Fenchel 变换、变形代数 | 4 |
| 2023 | 同 | 3 | 仿射等价有限元：证明 Sobolev 半范数缩放不等式 \|v̂\|≤C‖B‖^m\|det B\|^{−1/2}\|v\| 及逆式；‖B‖≤h_K/ρ_K̂ | 有限元 | 仿射映射、Sobolev 半范数、形状正则 | 4 |
| 2024 | 2024 ACM (Team) | 1 | 非线性 Gronwall 型：由 z_n+Σw_kΔt≤M+Σφ(z_k)Δt 证明 y_{n*}≤C*（与 Δt 无关） | 数值分析 | 非线性 Gronwall、Bihari 型论证 | 4 |
| 2024 | 同 | 2 | 输运方程三种半离散（D₋, D₊, D₀）：(a-i) 哪一个不稳定及原因；(a-ii) 两个稳定格式对应哪个图；(b) 用隐式（Crank–Nicolson 型）时间步证明一个保范数、一个耗散 | 数值 PDE | von Neumann、能量恒等式、D±=D₀±α±D₊D₋ | 5 |
| 2024 | 同 | 3 | 曲面演化保网格（Gu–Yau）：(i) 证明满足 (3) 的 X 是 ∫\|∇_{Γ₀}X\|² 的局部极小；(ii) 证明弱形式有限元离散解存在唯一 | 数值 PDE/几何 | 能量泛函变分、鞍点适定性、LBB | 5 |
| 2025 | 2025 ACM (Team) | 1 | 有限元能量极小化：(a) W 连续时 lim_{h→0}E_h=inf E；(b) 给出 W 使 lim E_h≠inf_{A₁}E | 变分/有限元 | Γ-收敛、Lavrentiev 现象 | 4 |
| 2025 | 同 | 2 | softmax/log-sum-exp：(a) lse 凸；(b) 共轭 lse*；= 负熵（y∈单纯形）；(c) 二次共轭等于 lse；(d) softmax 是 z·p−p·log p 的 argmax | 凸分析/机器学习 | Fenchel 共轭、biconjugate、KKT | 3 |
| 2025 | 同 | 3 | A=λI+N（N^m=0）：(a) f(A) 的 Jordan/插值表达式；(b) e^A；(c) 实矩阵复特征值时高效算 e^{At}；(d) A=[[0,1],[−1,0]] 的 e^{At} 及解释 | 矩阵函数/数值线代 | Jordan 分解、矩阵函数、Cayley 变换 | 3 |

### 2.4 Mathematical Physics（2022–2025，新设科目，共 32 题）

| 年份 | 卷别 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |
|---|---|---|---|---|---|---|
| 2022 | Individual | 1 | Hellmann–Feynman 定理 ⟨Ψ_j\|A\|Ψ_j⟩=∂E_j/∂γ；对 H=−∂²+ω²x²/4 证明 ⟨x²⟩=(2j+1)/ω | 量子力学 | 微扰论/导数的谱表示 | 3 |
| 2022 | Individual | 2 | 由弱场度规 ds²=−(1+2φ)dt²+dx²+… 与广义协变性推导完整 Einstein 场方程 | 广义相对论 | 等效原理、协变化、Bianchi 恒等式、Newton 极限 | 5 |
| 2022 | Individual | 3 | 6 维 2-形式场 B₍₂₎ 的自由作用量：(a) 有质量时的 on-shell 自由度与 Poincaré 表示；(b) 无质量时消规范后的自由度与表示 | 量子场论 | 规范固定、自由度计数、Poincaré 群表示（小群） | 5 |
| 2022 | Overall | 1 | D 维标量-引力作用量：(1) Einstein 方程与标量场运动方程；(2) 二维中 Riemann 张量与 Ricci 标量的关系；(3) D=2 时 Einstein 方程的推论 | 广义相对论 | 变分、2D 曲率恒等式、Weyl 张量 | 4 |
| 2022 | Overall | 2 | 4D U(1) 规范不变算子 O_{2n}（2 个 F 与 2n−4 个导数、n 对缩并）：(1) F 满足的方程；(2) n=2 唯一；(3) n=3 唯一；(4) n=4 的独立算子集；(5) 一般 n | 量子场论 | 场方程 on-shell、Bianchi、张量缩并计数 | 5 |
| 2023 | Individual | 1 | Newton 力学：(1) 第一定律是否需独立公理；(2) 势阶跃面上 v 与 x 轴夹角 θ₁、θ₂ 在 V₁<V₂ 与 V₁>V₂ 时的关系 | 经典力学 | 能量守恒、切向动量守恒（折射类比） | 3 |
| 2023 | Individual | 2 | 圆环上带电粒子 L=½θ̇²+(B/2π)θ̇：(1) 谱与波函数、B=π 时基态二重简并；(2) Z₂×Z₂ 作用与中心扩张为 D₈；(3) 加 V=λcos2θ 后仍两基态、用单瞬子验证非微扰简并不被解除 | 量子力学/QFT | θ-角变量量子化、瞬子、投影表示、中心扩张 | 5 |
| 2023 | Individual | 3 | spinor-helicity 形式：(1) p²=m²⇔det p^{α̇α}=m²，无质量时分解为 λλ̃；(2) A·B 与 Mandelstam s_ij 的括号表示；(3) 3 点振幅指数 x_ij 与 A₃(1⁻2⁺3⁻) | 量子场论 | 自旋螺旋、Lorentz 不变性、小群 | 5 |
| 2023 | Individual | 4 | 3 维纯引力：把 Einstein–Hilbert 作用量改写为 vierbein + spin connection，并证明等价于 ISO(1,2) 上的 Chern–Simons 理论 S=(k/4π)∫Tr(AdA+⅔A³) | 引力/QFT | 一阶形式、Chern–Simons、规范等价 | 5 |
| 2023 | Overall | 1 | d 维周期 Ising：配分函数写成 Z=N∫Dψ e^{−S[ψ]}；低温柔量展开求 c_i；Fourier 变换后得 φ⁴ 理论；由 m 变号求相变温度 | 统计场论 | Hubbard–Stratonovich、路径积分、φ⁴、Wilson–Fisher | 5 |
| 2023 | Overall | 2 | 2D 无质量 Dirac：(1) 由 J^μ=ε^{μν}∂_νφ 得 φ 的场方程或两点函数；(2) 写出 φ 的局部作用量；(3) 关于 2D 中玻色–费米关系的讨论；(4) 与自旋统计定理的一致性；(5) 耦合 U(1) 后 2D QED 的粒子谱（质量是否为零） | 量子场论 | Bosonization、Sine–Gordon、Schwinger 模型 | 5 |
| 2023 | Team | 1 | 电子-正电子谱 E_n=ε₀(n−½)：由 Dirac 海得 Z₀(q)=Π(1−qⁿ)⁻¹、Z_N=q^{N²/2}Z₀；用反对易产生算子重写并证明 Jacobi 三乘积恒等式；命名对应相对论模型 | 统计物理/QFT | 巨正则系综、Jacobi 三乘积、Dirac 海 | 4 |
| 2023 | Team | 2 | 一维方势阱（深 −V₀/L、宽 L）束缚态：(1) L→0 与 L→∞ 哪个束缚态多；(2) L∈(0,∞) 变时最少束缚态数；(3) 半无限深阱时的最少束缚态数 | 量子力学 | 奇偶束缚态、超越方程、零点计数 | 4 |
| 2023 | Team | 3 | 3D Abelian 规范场 + CS 项：(1) 量子层面是否自洽；(2a) λ=0 的对称性哪些破缺；(2b) 是否有能隙；(2c) 有没有规范不变守恒流与内部量子数、生成哪个紧 Lie 群；(2d) 谱（质量、自旋、态数、Q_a） | 量子场论 | Chern–Simons 量子化、拓扑质量、anyon | 5 |
| 2024 | Individual | 1 | 三维各向同性弹簧束缚的平面量子粒子（三定点为正三角形）：(a) 连续对称 Lie 群；(b) 能级 | 量子力学 | 群论、简并度、二次型对角化 | 4 |
| 2024 | Individual | 2 | Cayley 树（价 v≥3）上 Ising 模型、自由边界：是否存在 T_c>0 使相变发生而自由能 F(T) 在 (0,∞) 解析 | 统计物理 | Bethe 格/递归、解析性、相变与 Lee–Yang | 4 |
| 2024 | Individual | 3 | 黑洞霍金辐射数量级：(1) 温度与功率（Planck 单位及 SI）；(2) 宇宙年龄内可蒸发的最大质量与 CMB 温度对比；(3) 最后一秒辐射的质量；(4) 太阳质量黑洞 Q=M 所需电荷与太阳质量质子总电荷比较 | 引力/天体物理 | 量纲分析、Hawking 温度、Stefan–Boltzmann | 3 |
| 2024 | Individual | 4 | 球形容器内环氧树脂在双轴旋转（ω₁ 绕 O₁O₂、ω₂ 绕 O₃O₄）下固化后的最终形状 | 经典力学 | 非惯性系有效势、等势面形状 | 3 |
| 2024 | Overall | 1 | Feynman 气体：一维 N 个不可穿透粒子 [0,L]、相互作用 −λ·Σlog\|x_{i+1}−x_i\|，求热力学极限下 Gibbs 自由能 | 统计力学 | 可积 Calogero–Sutherland 型、Sellberg 积分、热力学极限 | 4 |
| 2024 | Overall | 2 | 相对论带电粒子从高 h 处以速度 v 水平抛出、在竖直电场 E 中落地，落点距离 R：求相对论 Hamiltonian、Hamilton 方程与 R(h,m,v) | 相对论力学 | 相对论 Hamilton 量、正则方程 | 3 |
| 2024 | Team | 1 | 常数磁场带（x₂∈[−L,0]）散射：(1) 渐近波函数、可穿透的 E 阈值、出射角 θ′；(2) L→∞ 半平面情形下 p₁=0 且 x₂=0 处全反射条件的能谱 | 量子力学 | Landau 能级、Airy/抛物柱函数、散射 | 5 |
| 2024 | Team | 2 | 外场中标量场 S=∫[−g^{μν}(∂_μ+iqA_μ)ϕ(∂_ν−iqA_ν)ϕ*]：(1) 场方程；(2) ϕ_ω=e^{−iωt}ψ_ω 的方程；(3) 台阶势 qA₀、ω<μ 的出射解；(4) 用产生湮灭算子表示 ϕ_ω 并解释物理意义；(5) 初态真空后续演化 | 量子场论 | Klein 佯谬、Bogoliubov 变换、粒子产生 | 5 |
| 2024 | Team | 3 | 广义相对论三连问：(1) Killing–Yano 张量 Y_ab 满足 ∇_aY_bc=∇_[aY_bc]，及曲面通量守恒；(2) 证明 Maxwell 作用量共形不变并由此得能动张量无迹；(3) dS 型度规 −dt²+t²γ 中 P,Q 有共同过去事件，换成 −dt²+t^{3/2}γ 是否仍成立 | 广义相对论 | Killing–Yano、共形变换、粒子视界/因果结构 | 5 |
| 2025 | Individual | 1 | Born–Infeld 电动力学 L=b²(1−√(1−(E²−B²)/b²))：(1) 点电荷静电场与有限自能；(2) 背景场 E₀ 中的光速 | 电动力学 | 非线性电动力学、自能积分、小信号波速 | 4 |
| 2025 | Individual | 2 | 一维 Ising 模型、相互作用 J(r)∝r^{−α}，α∈(1,2)：(1) α=3/2 时近似自由能；(2) 求 T_c(α) | 统计物理 | Kac 型长程相互作用、平均场/重整化 | 4 |
| 2025 | Individual | 3 | 任意维 Maxwell 理论：(1) 规范不变；(2) Coulomb 规范量子化与极化态数；(3) d=2 时 F₁₂ 为常数、旋转不变解；(4) S² 上南北半球粘合 ⇒ ∫F 量子化；(5) d=3 时等价于自由无质量标量 | QFT/拓扑 | 规范固定、拓扑量子化（Dirac）、Hodge 对偶 | 5 |
| 2025 | Individual | 4 | 一般 Lorentz 变换：(1) 沿 x 轴的速度 v 变换；(2) 任方向 v 的矢量形式；(3) 两学生先 x 后 y 与先 y 后 x 谁对 | 狭义相对论 | Lorentz 变换、boost 不闭合（Wigner 旋转） | 3 |
| 2025 | Overall | 1 | 连接数（linking number）：(1) 几何意义与非零即不可分离、形变不变；(2) 由物理推导 Gauss 连接积分；(3) L₁↔L₂ 对称性与电-磁对偶；(4) 投影交叉 ±1/2 求和规则 | 电磁学/拓扑 | Ampère/Biot–Savart、Gauss 积分、磁单极对偶 | 4 |
| 2025 | Overall | 2 | 线性势 V(x)=2gx 中自旋为零非相对论粒子的热核 ⟨x′\|e^{−βH}\|x⟩，用路径积分直接计算 | 量子力学 | 路径积分、平移/线性势精确传播子 | 4 |
| 2025 | Team | 1 | O(N) 全局对称标量理论（四次势）：(1) 基本表示下自发破缺、真空流形与 G→H；(2) 伴随表示下的破缺模式与非唯一性；(3) 非线性实现、ϕ^a 用 Goldstone 场 π^m 的指数表达；(4) Goldstone 有效作用量的几何意义 | 量子场论 | 自发对称破缺、陪集空间 G/H、非线性 σ 模型 | 4 |
| 2025 | Team | 2 | 黑洞热力学（微正则系综）：(1) 态密度 Ω(E) 指数增长；(2) 负热容 C=−k_B E²/E_p²；(3) 对蒸发的意义 | 引力/统计物理 | Bekenstein–Hawking 熵、Legendre 变换、负热容 | 3 |
| 2025 | Team | 3 | 球面三角形（内角 π/2, π/2, π/3、半径 R、V≡0、A=0）内自旋为零粒子的能量本征值与简并度 | 量子力学 | 球面调和、球面三角形 Dirichlet 谱、对称性 | 4 |

---

## 3. 考点频次表

> 数据来自脚本 `finals_app_phys_stats.py`（关键词规则打标，一个切分单元可命中多个考点）。统计基数 = **128 个切分单元**（含 2020 解密后的 3 份卷）。明细见 `finals_app_phys_tables.md`。
> **注意**：这是「考点出现次数」而不是「题目数」；同一题可命中 2–4 个考点。

### 3.1 考点 × 年份（按总计降序）

| 考点 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 数值线性代数/矩阵分解（SVD、特征值、Krylov、迭代法谱） | . | . | . | 1 | 1 | 1 | . | 1 | 2 | 4 | 2 | 4 | . | 3 | **19** |
| 变分法/Euler–Lagrange/最优化 | . | . | 1 | 1 | 1 | 2 | 2 | 1 | 1 | . | . | 1 | 2 | 4 | **16** |
| 量子力学 | . | . | . | . | . | . | . | 1 | . | . | 1 | 7 | 5 | 2 | **16** |
| 广义相对论/引力 | . | 1 | 1 | 1 | . | 1 | . | . | . | . | 4 | 1 | 4 | 2 | **15** |
| 经典力学/哈密顿-拉格朗日 | . | . | . | . | . | 1 | . | . | . | . | 2 | 6 | 3 | 3 | **15** |
| PDE 有限差分/CFL/von Neumann | 1 | . | 1 | . | . | 2 | 1 | 1 | 1 | . | 1 | 3 | 2 | 1 | **14** |
| 量子场论/QFT | . | . | 1 | . | . | . | . | . | . | . | 2 | 6 | 3 | 1 | **13** |
| 概率/随机过程/统计物理 | . | . | . | . | . | . | . | 1 | . | . | . | 2 | 3 | 3 | **9** |
| 电动力学/电磁学 | . | . | . | . | . | . | . | . | . | . | . | 1 | 5 | 3 | **9** |
| 插值/逼近与求积 | . | . | 2 | 1 | . | . | 1 | 1 | 1 | 1 | . | . | 1 | . | **8** |
| 有限元/弱解/Sobolev | . | . | . | . | . | 1 | . | . | . | . | 1 | 1 | 2 | 2 | **7** |
| 迭代法收敛性（Jacobi/Gauss–Seidel/不动点） | . | . | . | . | . | . | . | 2 | . | . | 2 | 2 | 1 | . | **7** |
| 离散微分几何/网格/共形 | . | 1 | 2 | . | . | 2 | . | . | . | . | . | . | 1 | . | **6** |
| 渐近分析/奇异摄动/边界层 | . | . | . | 1 | 1 | . | . | . | . | . | . | . | 2 | 1 | **5** |
| 离散数学/组合算法 | 2 | . | 1 | . | . | . | 1 | 1 | . | . | . | . | . | . | **5** |
| 能量稳定/能量守恒格式 | . | . | . | . | . | . | 1 | . | 1 | 1 | 1 | 1 | . | . | **5** |
| 常微分方程数值解 | . | . | . | . | . | 1 | . | 1 | . | . | . | 1 | 1 | . | **4** |
| 流体力学/连续介质 | . | . | . | 2 | . | 1 | 1 | . | . | . | . | . | . | . | **4** |
| 反问题/正则化/稀疏 | . | . | . | . | . | 1 | . | . | . | . | . | . | 1 | 1 | **3** |
| 凸分析/机器学习（softmax、prox） | . | . | . | . | . | . | . | . | . | . | . | . | . | 2 | **2** |
| 谱方法/FFT/Fourier | . | . | . | . | . | . | 1 | . | . | . | . | 1 | . | . | **2** |
| 非线性方程/牛顿法 | . | . | . | 1 | . | . | . | . | . | . | . | . | . | 1 | **2** |

### 3.2 考纲主题覆盖情况（Applied/Comp 8 主题）

| 考纲主题 | 总决赛是否出现 | 题次（估） | 代表年份 |
|---|---|---|---|
| 插值与逼近（FFT、样条、最小二乘） | 部分（缺 FFT/有理逼近） | 8 | 2014 Team、2015 Ind/Team、2018 Ind |
| 非线性方程求解 | 是（Newton 为主，二分/拟 Newton 几乎不考） | 4 | 2015 Ind、2019 Ind、2022 Ind |
| 线性系统与特征值问题 | **是，最高频** | 19 | 2012–2025 全程 |
| ODE 数值解（稳定性、刚性） | 是 | 8 | 2017 Overall、2020 set2、2023 Ind、2024 Ind |
| PDE 数值解（FD/FE/谱、Lax 等价） | **是，最高频** | 14 | 2012 Team、2019–2024 每年 |
| 数学建模/渐近/边界层/Monte-Carlo | 是（渐近强、Monte-Carlo 从未出现） | 6 | 2015 Overall、2022 Overall、2025 Overall |
| 线性与非线性规划（单纯形、内点、动态规划） | 弱（被凸优化/prox/压缩感知替代） | 4 | 2024 Overall、2025 Overall、2019 Overall |
| 参考书所载「谱方法」 | 弱（仅 2018/2023 各 1 次提及 spectral） | 2 | 2018 Ind、2023 Ind |

### 3.3 考纲主题覆盖情况（MathPhys 6 主题）

| 考纲主题 | 题次 | 年份分布 | 备注 |
|---|---|---|---|
| 经典力学 | 15 | 2022–2025 | Hamilton/Lagrangian 形式只作工具，专门考「Hamilton–Jacobi」「Noether 定理」「刚体」的题几乎没有 |
| 电动力学 | 9 | 2023–2025 | 2025 年集中爆发（Born–Infeld、连接数/Gauss 积分、Lorentz 变换） |
| 热力学与统计物理 | 9 | 2019、2023–2025 | Ising（Cayley 树、长程）、Feynman 气体、黑洞微正则 |
| 量子力学 | 16 | 2019、2022–2025 | 每份个人卷必考；瞬子、球面三角形、路径积分 |
| 广义相对论 | 15 | 2013、2014、2015、2017、2022–2025 | 2022 Overall 起成为指定必考块 |
| 量子场论 | 13 | 2014、2022–2025 | 2023 起份额最大（spinor-helicity、CS 理论、O(N) 破缺） |
| 考纲未列但实际考到 | — | — | 黑洞霍金辐射数量级估算（2024 Ind Q3）、Born–Infeld 非线性电动力学（2025 Ind Q1）、拓扑连接数（2025 Overall Q1）、Calogero 型可积气体（2024 Overall Q1） |

### 3.4 任务动词分布（128 单元，全题面）

| 动词 | 题次 | 占比 |
|---|---|---|
| show | 59 | 46.1% |
| prove | 35 | 27.3% |
| find | 26 | 20.3% |
| derive | 18 | 14.1% |
| write | 12 | 9.4% |
| compute / determine / solve / explain | 各 9 | 各 7.0% |
| construct | 7 | 5.5% |
| describe / give / state | 各 5 | 各 3.9% |
| estimate / compare / define / discuss | 各 4 | 各 3.1% |
| verify | 3 | 2.3% |
| sketch / calculate | 各 2 | 各 1.6% |
| analyze / analyse / identify / count / recast | 各 1 | 各 0.8% |

**「证明/展示」类（show+prove）合计命中 94 个单元，占 73.4%**——这是总决赛卷最鲜明的风格特征。

### 3.5 卷别 × 规模（脚本切分单元）

| 卷别 | 单元数 | 总字符 | 平均字符 | 中位字符 | 平均小问数 |
|---|---|---|---|---|---|
| Individual | 59 | 39529 | 670.0 | 565 | 1.69 |
| Overall | 33 | 19095 | 578.6 | 434 | 1.48 |
| Team | 36 | 28730 | 798.1 | 654 | 2.64 |
| **全部** | **128** | **87354** | **682.5** | **523** | **1.91** |
| ACM 合计 | 95 | 60413 | 635.9 | 495 | 1.89 |
| MathPhys 合计 | 33 | 26941 | 816.4 | 665 | 1.94 |

| 科目 × 卷别 | 单元数 | 平均字符 | 平均小问数 |
|---|---|---|---|
| ACM × Individual | 44 | 645.1 | 1.70 |
| ACM × Overall | 24 | 515.7 | 1.21 |
| ACM × Team | 27 | 727.9 | 2.81 |
| MathPhys × Individual | 15 | 743.0 | 1.67 |
| MathPhys × Overall | 9 | 746.6 | 2.22 |
| MathPhys × Team | 9 | **1008.6** | 2.11 |

---

## 4. 总决赛 vs 初赛（笔试）的差异

> 初赛数据来自既有报告：`reports/stats_overview.md`（136 个 PDF / 757 道题）、`reports/problem_metrics.md`（按科目词数与难度代理）。本报告用 `data/problems_full.json`（757 题）复算得到与 finals 可比的字符级指标。
> 初赛语料中 Computational & Applied 共 **135 题**（2011–2026），Mathematical Physics 共 **30 题**（2022–2026，每年 6 题）。

### 4.1 差异一：**Overall（全能赛）是总决赛独有赛制，初赛完全没有**

- 统计 `problems_full.json` 的 757 题所属 120 份试卷名：**含 `overall` / `all-round` 的试卷数 = 0**。
- 总决赛本子领域则有 **Overall 卷 13 份**（ACM 2012–2025 除 2014 外每年 1 份 + MathPhys 2022–2025 每年 1 份），卷面自称 `ALL-AROUND TEST / ORAL EXAM`（2012）、`Applied Mathematics ( All Round )`（2015）、`Individual Overall Contest`（2022–2024）、`Individual All-Round Competition`（2025）。
- 规模上 Overall 卷**最小**：33 个单元 / 19095 字符，平均 578.6 字符、平均小问 1.48，明显低于 Individual（670.0）与 Team（798.1）。
- 数据支撑：ACM Overall 卷中有 6 份字符数 < 800（2013:545、2015:213、2016:543、2017:537、2018:389、2022:733），即「一场考试只问一道题」。

### 4.2 差异二：**总决赛题量按「卷」看远低于初赛，且出现「N 选 k」免答机制**

- 初赛：Computational & Applied **每份卷固定 6 题**（2011–2014 为 10–12 题），135 题 / 16 个年份 ≈ **8.4 题/年**（含个人+团体）；MathPhys 固定 **6 题/年**。
- 总决赛：ACM Individual 每年 **2–5 题**（中位 3，13 年共 41 题 ≈ **3.2 题/年**）；ACM Overall 每年 **1–3 题**（13 年 18 题 ≈ 1.4 题/年）；ACM Team 每年 **2–3 题**（共 26 题）。
- 因题量少，总决赛引入「**N 选 k**」：脚本扫描到 **10 份卷**含此类指令——`2019 Applmath (Individual): CHOOSE ANY 3 OUT OF 5`、`2023/2024/2025 Math-Phys (Individual): choose 3 out of the 4 / answer at least 3 of the following 4`、`2023/2024/2025 Math-Phys (Overall): choose one of the following two / answer at least 1 of the following 2`、`2023/2024/2025 Math-Phys (Team): choose 2 out of the following 3`。初赛语料中**无一份卷**出现此类指令。

### 4.3 差异三：**单题更「重」——字符长度与小问数全面上移**

| 指标 | 初赛 Computational & Applied (135 题) | 初赛 Mathematical Physics (30 题) | 总决赛 ACM (95 单元) | 总决赛 MathPhys (33 单元) | 全初赛 (757 题) |
|---|---|---|---|---|---|
| 平均字符 | 688.4 | 959.8 | **635.9**（Ind 645.1 / Ov 515.7 / Team 727.9） | **816.4**（Ind 743.0 / Ov 746.6 / **Team 1008.6**） | 438.6 |
| 中位字符 | 592 | 802 | 495 | 665 | 329 |
| 平均小问数 | 2.48 | 3.37 | **1.89**（Ind 1.70 / Ov 1.21 / Team 2.81） | **1.94**（Ind 1.67 / Ov 2.22 / Team 2.11） | — |
| 「小问≥10 的巨型题」 | — | — | 有：2024 ACM Team Q3、2024 MathPhys Team Q1/Q3、2025 MathPhys Ind Q3/Q4 | — | — |

**结论修正**：与「初赛整体」比，总决赛单题长度高 **55.6%**（682.5 vs 438.6）；但若只与初赛**同科目**比，字符长度其实**基本持平或略低**（ACM finals 635.9 vs prelim 688.4；MathPhys finals 816.4 vs prelim 959.8），而**平均小问数反而下降**（ACM 1.89 vs 2.48；MathPhys 1.94 vs 3.37）。
→ 所以**总决赛的「更难」不体现在篇幅/小问数上，而体现在要求上**：见差异四。真正拉高体量的是 **Team 卷**（MathPhys Team 平均 1008.6 字符、ACM Team 2.81 小问）。

### 4.4 差异四：**证明型任务占比上升，计算型任务下降（ACM 尤其明显）**

| 动词 | 初赛 ACM (135) | 总决赛 ACM (95 单元) | 初赛 MathPhys (30) | 总决赛 MathPhys (33 单元) |
|---|---|---|---|---|
| show | 61 (45.2%) | 47 (49.5%) | 9 (30.0%) | 13 (39.4%) |
| prove | 54 (40.0%) | 31 (32.6%) | 8 (26.7%) | 4 (12.1%) |
| **show+prove（命中单元数）** | **115 (85.2%)** | **74 (77.9%)** | 17 (56.7%) | 17 (51.5%) |
| find | 37 (27.4%) | 14 (14.7%) | 11 (36.7%) | **12 (36.4%)** |
| compute | 14 (10.4%) | **4 (4.2%)** | 9 (30.0%) | 7 (21.2%) |
| derive | 13 (9.6%) | **12 (12.6%)** | 6 (20.0%) | 6 (18.2%) |
| calculate | 1 (0.7%) | 1 (1.1%) | 6 (20.0%) | 1 (3.0%) |

- ACM：`compute` 占比从 10.4% 掉到 **4.2%**，`find` 从 27.4% 掉到 **14.7%**，`derive` 从 9.6% 升到 **12.6%** → **从「算一个数」转向「推一个结论/一个方程」**。
- MathPhys：`calculate` 从 20.0% 崩到 **3.0%**，`prove` 从 26.7% 掉到 12.1%，但 `find` 稳定在 36% → **从「求解析结果」转向「画出结构/给出算法/判断存在性」**（如 2023 Math-Phys Overall Q2 的「不必算质量数值，只说零或非零」）。

### 4.5 差异五：**考点深度与「研究前沿性」显著前移**

| 维度 | 初赛（笔试） | 总决赛 |
|---|---|---|
| 线性代数题的最高层级 | SVD/特征值/标准 Jordan（difficulty proxy 2.6 档） | **Arnoldi/Lanczos/GMRES 全过程**（2016 Ind Q1、2017 Team Q2、2020 set2 I、2021 Overall II）、**子空间迭代主角几何**（2021 Overall I、2023 Ind Q2） |
| PDE 数值题的最高层级 | 差分格式 + von Neumann | **紧致格式（Padé）稳定充要条件**（2020 set1 II）、**保能量/保 Hamiltonian 格式的构造与证明**（2023 Overall、2024 Team Q2）、**曲面演化保网格 FEM（Gu–Yau）**（2024 Team Q3） |
| 几何相关 | 无（在 Applied 科目内） | **离散微分几何/共形几何成为 ACM 的传统考点**：2013 Ind Q2、2014 Ind Q4–5、2017 Team Q1、2024 Team Q3（6 个考点命中，2013/2014/2017 集中） |
| MathPhys 的最高层级 | 量子力学、相对论、统计的基本题型（2024/Q2 难度 5.0 已是初赛上限） | **瞬子计算与非微扰简并**（2023 Ind Q2）、**spinor-helicity 与 3 点振幅**（2023 Ind Q3）、**3D 引力 = Chern–Simons**（2023 Ind Q4）、**Bosonization / Jacobi 三乘积**（2023 Overall/Team）、**S² 上 Maxwell 的通量量子化**（2025 Ind Q3）、**任意维 p-形式自由度与 Poincaré 表示**（2022 Ind Q3） |
| 参考教材层级 | 本科高年级（Golub–Van Loan、Hairer 等） | 部分题目**只在研究生教材/文献中**（Carroll–Wald、Peskin–Schroeder、Weinberg、Kardar，见考纲参考文献） |

### 4.6 差异六：**「跨科目交融」与「近代数学工具」是总决赛专属**

- 初赛每份卷严格属于单一科目（Algebra / Analysis / Geometry / Probability / Applied / Physics 六选一）。
- 总决赛 ACM 卷中反复出现**跨到几何/拓扑/组合**的题：离散 Gauss–Bonnet（2013）、power Voronoi 最优传输（2014 Ind、2017 Team×2）、circle packing/共形因子微分同胚（2014 Ind、2017 Team）、claw-free 图的 α≤2n/(δ+2)（2014 Team）、超平面分割数 f_d(n)（2018 Team）、4-范数球与平面交为圆盘（2025 Ind Q4）、连接数/Gauss 积分（2025 MP Overall Q1）。
- 2019 的 **ACM Overall 卷整卷是代数题**（不可约多项式 + 0-1 矩阵范数 + Tikhonov 泛函），说明 Overall 卷的科目边界是松的。
- 工具箱也升级：Sard 定理 + 隐函数定理（2013 Overall）、同伦/路径跟踪（2013 Overall）、Bregman 散度（2020 Overall Q2）、Wasserstein 梯度流（2020 set2 III）、压缩感知零空间性质（2024 Overall Q1）、phenomenon of Γ-收敛/Lavrentiev（2025 Team Q1）、Fenchel 共轭与 Moreau 分解（2025 Overall Q1、2025 Team Q2）。

### 4.7 差异七：**MathPhys 团体卷是总决赛独有**

- 初赛 MathPhys 语料 30 题**全部为 individual**（team = 0）；ACM（Computational & Applied）初赛有 team 47 题 / individual 88 题。
- 总决赛 MathPhys 从 **2023 年起设 Team 卷**（2022 仅 Individual + Overall），3 年共 9 题，且平均字符 **1008.6**，是本子领域最长的一类卷。
- 同时 ACM Team 卷在总决赛**缺 2013、2016、2020、2021、2022 五年**，ACM Overall 则**没有 2014 独立文件**。

---

## 5. Individual 卷 vs Team 卷差异

| 维度 | Individual | Team | 数据出处 |
|---|---|---|---|
| 单元数 | 59 | 36 | finals_app_phys_tables.md §2 |
| 平均字符 | 670.0 | **798.1**（+19.1%） | 同上 |
| 中位字符 | — | 610 | 同上 |
| 平均小问数 | 1.69 | **2.64**（+56%） | 同上 |
| 平均符号数（ACM） | 12.9 | 12.9（持平） | 脚本 JSON |
| 平均符号数（MathPhys） | 9.8 | **16.2**（+65%） | 脚本 JSON |
| 是否含「N 选 k」 | 是（2019 ACM Ind 5 选 3；MathPhys Ind 4 选 3） | 是（MathPhys Team 3 选 2；ACM 2023 Team 卷名即「3 choose 2」） | _finals_extra 扫描 |
| 题型倾向 | 单一技术点、深度推导（Newton 法全局收敛、Givens 分解、powert 迭代收敛率） | 多技术点拼接 / 长链条推导（2024 ACM Team Q2 三小问连做、2024 ACM Team Q3 从变分到 FEM 适定性） | 逐卷阅读 |
| 最难的卷 | 2023 Math-Phys Individual（4 选 3，含瞬子 + spinor-helicity + Chern–Simons） | 2024 ACM (Team)（3 题，其中 2 题达研究级：曲面演化保网格 FEM、稳定/耗散半离散分类） | 人工自评 5/5 |

### 5.1 结构性差异（Team 卷独有的配方）

1. **Team 卷几乎总是「分小问递进」**：2024 ACM Team Q2 用 (a-i)→(a-ii)→(b) 三步从「判断哪个格式不稳定」走到「证明保范数/耗散」；2024 MathPhys Team Q3 用 1(a)(b)(c) 递进；2025 MathPhys Team Q1 用 1–4 递进。Individual 卷则多以 (1)(2)(3) 并列而非递进。
2. **Team 卷更爱考「构造 + 证明」的闭环**：2014 Team Q3（构造隐式格式并证一致 L² 界）、2019 Team Q2（求精度阶 + 证 GS 收敛）、2023 Team Q3（仿射等价的缩放不等式双向）、2024 Team Q2（构造并证明两种性质）、2025 Team Q1（构造反例）。Individual 卷更爱考「给定对象、求性质」。
3. **Team 卷会跨科目拼接**：2014 Team（插值 + 图论 + 数值 PDE）、2018 Team（数值线代 + 组合几何）、2019 Team（算法/数论 + 数值分析 + 统计物理）、2023 Team（数值线代 + 凸分析 + 有限元）、2025 Team（变分 + 凸分析 + 矩阵函数）。Individual 卷单卷内基本单一主题。
4. **Team 卷「同题重出」现象**：2014 Team Q1 与 2015 Individual Q2 是**同一道分段线性插值误差估计题**（`‖u−Π_h u‖≤h²/π²‖u″‖`）；2017 Team Q2 的 Lanczos 与 2020 Individual set2 Q1 的 Lanczos 几乎逐字相同（含同一段伪代码）；2014 Individual Q4（power Voronoi 最优传输）与 2017 Team (2) 是同一主题的两种叙述。→ **团体卷常复用个人卷/往年团的题作为「保底题」**。
5. **Overall 卷夹在两者之间**：平均 578.6 字符、1.48 小问，但**小问可极长**（2024 ACM Overall Q2 含 (a)(b)(c-i)(c-ii)(c-iii) 五个子问）——即「一道题＝一整场考试」。

---

## 6. 代表题完整题面 + 解题思路

以下 8 题题面**逐字取自抽取文本**（仅把 LaTeX 化后的换行合并）；公式若抽取有损会标注。

### 代表题 1｜2014 应用与计算数学 Individual 第 3 题（能量稳定性，离散梯度法）

**题面（抽取原文，第 3 页）**：
> Consider the following equation over an one-dimensional (1-D) domain Ω = (0, 1):
> ∂_t φ = −φ³ + φ + ε²φ_xx, in Ω; φ_x = 0, at x = 0, x = 1, with ε > 0 a given constant.
> The following semi-implicit, semi-discrete numerical scheme is formulated:
> (φ^{n+1} − φ^n)/Δt = −(φ^{n+1})³ + φ^n + ε²φ^{n+1}_xx, in Ω; φ^{n+1}_x = 0, at x = 0, x = 1.
> Prove the following energy stability for the numerical solution: E(φ^{n+1}) ≤ E(φ^n) for any Δt > 0,
> with the energy functional E(φ) = ∫_Ω (¼φ⁴ − ½φ² + (ε²/2)|φ_x|²) dx.
> **Hint.** Take an L² inner product with (3) by μ̃^{n+1} = (φ^{n+1})³ − φ^n − ε²φ^{n+1}_xx.

**解题思路**：
1. 令 μ̃^{n+1} = (φ^{n+1})³ − φ^n − ε²φ^{n+1}_xx，则格式 (3) 可写成 (φ^{n+1}−φ^n)/Δt = −μ̃^{n+1}。
2. 两边与 μ̃^{n+1} 作 L² 内积：左侧 = (1/Δt)⟨φ^{n+1}−φ^n, μ̃^{n+1}⟩ = −‖μ̃^{n+1}‖² ≤ 0。
3. 关键恒等式（离散梯度/凸分裂）：对 F(φ)=¼φ⁴−½φ²（F′=(φ)³−φ）有
   F(φ^{n+1})−F(φ^n) ≤ ⟨φ^{n+1}−φ^n, (φ^{n+1})³−φ^n⟩ = ⟨φ^{n+1}−φ^n, μ̃^{n+1}+ε²φ^{n+1}_xx⟩，
   其中用到凸性：ξ↦¼ξ⁴ 凸、ξ↦−½ξ² 凹 → 在 (φ^{n+1}−φ^n) 方向取线性化的上/下界。
4. 于是 E(φ^{n+1})−E(φ^n) ≤ ⟨φ^{n+1}−φ^n, μ̃^{n+1}+ε²φ^{n+1}_xx⟩ + (ε²/2)(‖φ^{n+1}_x‖²−‖φ^n_x‖²)。
5. 分部积分（Neumann 边条件使边界项为零）：⟨φ^{n+1}−φ^n, ε²φ^{n+1}_xx⟩ = −ε²⟨φ^{n+1}_x−φ^n_x, φ^{n+1}_x⟩，
   与 (ε²/2)Δ‖φ_x‖² 合并得 −(ε²/2)‖φ^{n+1}_x−φ^n_x‖² ≤ 0。
6. 结合第 2 步的 −Δt‖μ̃^{n+1}‖² 项，得到 E(φ^{n+1})−E(φ^n) ≤ −Δt‖μ̃^{n+1}‖² − (ε²/2)‖φ^{n+1}_x−φ^n_x‖² ≤ 0，**与 Δt 无关（无条件稳定）**。
> 这题是 2021 Ind Q2、2022 Ind Q1、2023 Overall、2024 Team Q2 的同一族「能量稳定/守恒格式」母题的最早版本（2014），说明该考点在总决赛中**跨越 10 年反复出现（考点表中命中 5 次）**。

### 代表题 2｜2016 应用与计算数学 Individual 第 1 题（Arnoldi 与 Krylov 最优性）

**题面（抽取原文）**：
> Given a vector b ∈ R^m and A ∈ R^{m×m}, the Arnoldi process is a systematic way of constructing an orthonormal bases for the successive Krylov subspaces K_n = ⟨b, Ab, …, A^{n−1}b⟩. It gives AQ_n = Q_{n+1}H̃_n, where Q_n ∈ R^{m×n}, Q_{n+1} ∈ R^{m×(n+1)} are with orthonormal columns and H̃_n ∈ R^{(n+1)×n} is upper-Hessenberg. Let H_n ∈ R^{n×n} be obtained by deleting the last row of H̃_n.
> (a) Write out the Arnoldi algorithm.
> (b) Assume that at step n, the (n+1, n)-th entry of H̃_n is zero. i. Show that K_n is an invariant subspace of A and that K_n = K_{n+1} = K_{n+2} = …. ii. Show that each eigenvalue of H_n is an eigenvalue of A for n > 1.
> (c) Let P_n be the set of monic polynomials of degree n. Show that the minimizer of min_{p_n∈P_n} ‖p_n(A)b‖₂ is given by the characteristic polynomial of H_n.

**解题思路**：
- (a) 标准 Arnoldi：q₁=b/‖b‖；对 k=1,2,…：v=Aq_k；对 j=1..k 做修正 Gram–Schmidt h_{j,k}=⟨v,q_j⟩, v←v−h_{j,k}q_j；h_{k+1,k}=‖v‖；q_{k+1}=v/h_{k+1,k}。得到的 H̃_k 是 (k+1)×k 上 Hessenberg。
- (b) h_{n+1,n}=0 意味着 AQ_n = Q_n H_n，即 range(Q_n) 是 A-不变子空间；由于 Q_{n+1} 的第 n+1 列是 r_n/‖r_n‖，而 r_n=0 时算法终止，K_n=K_{n+1}=…。由 AQ_n=Q_nH_n 得 H_n = Q_n*AQ_n 是 A 在不变子空间上的限制，故 H_n 的每个特征值都是 A 的特征值（取特征向量 Q_n y）。
- (c) 对任意首一 p_n∈P_n，p_n(A)b ∈ K_{n+1}=K_n 且 b=Q_n(βe₁)，记 c=Q_n*b，则 ‖p_n(A)b‖₂=‖p_n(H_n)c‖₂ 且 c∝e₁（因 Q_n 的第一列是 b 的单位化）。于是 min_{p_n}‖p_n(H_n)e₁‖₂ 由 H_n 的特征多项式 p(λ)=det(λI−H_n) 达到（该多项式把 H_n 的所有特征值湮灭）。这就是 Arnoldi 与「隐式 Q 定理」的核心，也是 GMRES/FOM 的最优性来源。

### 代表题 3｜2021 应用与计算数学 Individual Question III（可积 Lax 流）

**题面（抽取原文）**：
> Let a_k(t), b_k(t) ∈ R (k = 1, 2, …, n) satisfy the differential equations:
> d/dt a_k(t) = 2(b_k² − b_{k−1}²), d/dt b_k(t) = b_k(a_{k+1} − a_k), k = 1, 2, …, n,
> where b₀(t) = b_n(t) = 0. Consider the n×n tri-diagonal matrix L(a, b) = [a₁,b₁; b₁,a₂,0; …; b_{n−1}; a_n]. Show that:
> 1. The eigenvalues of L(t) = L(a(t), b(t)) are independent of t.
> 2. lim_{t→∞} b_k(t) = 0, k = 1, 2, …, n−1.

**解题思路**：
1. 这是 **Toda 格点（finite non-periodic Toda lattice）** 的 Lax 对形式。构造反对称矩阵 B = [0, −b₁; b₁, 0, −b₂; …]，验证 dL/dt = [B, L] = BL − LB。
2. 由 dL/dt=[B,L] 与相似变换：d/dt(e^{−tB} L e^{tB}) = e^{−tB}((dL/dt)+[L,B])e^{tB} = 0 → L(t) 与 L(0) 相似，**谱不变**（这是 Lax 对的标准论证）。
3. 因此所有 a_k、b_k 是有界且解析的（Toda 流完整、解全局存在）；且 I_k = ½Σb_k² 等是守恒量。
4. 第二部分用 **等谱流收敛性（Moser 1975；Deift–Li–Nanda 排序定理）**：由第 1 步，轨道落在等谱集 𝒪 = {L' = QΛQᵀ : Q 正交, Λ=diag(λ₁,…,λ_n)} 内，这是一个**紧致连通流形**；Toda 流是 𝒪 上的完全可积 Hamilton 流，其不动点恰为对角矩阵 diag(λ_{σ(1)},…,λ_{σ(n)})。用 Sturm 序列（Jacobi 矩阵的特征多项式递推 p_k(λ)）可把 b_k² 表达为相邻谱区间上的"谱隙"量，并证明沿流单调趋于 0；等价地，沿不变环面上的角变量线性演化 t→∞ 时趋于"排序"极限，故 lim b_k(t)=0、a_k(t)→λ 的一个排列。
> 该题在总决赛中把「数值线性代数」与「可积系统」直接缝合，是初赛笔试语料完全没有的题型。

### 代表题 4｜2024 应用与计算数学 Team 第 2 题（输运方程三种半离散的稳定性判据）

**题面（抽取原文）**：
> Let u be the solution to the transport equation u_t + u_x = 0 on 0 ≤ x ≤ 2π with periodic boundary conditions and u(x,0)=exp(−(x−π)²). Consider the discrete approximation v_j ≈ u(x_j,t) on x_j = jh, h = 2π/(N+1). Define D₋v_j=(v_j−v_{j−1})/h, D₊v_j=(v_{j+1}−v_j)/h, D₀v_j=(v_{j+1}−v_{j−1})/(2h).
> (a) 三种半离散：(i) dv_j/dt + D₋v_j = 0, (ii) dv_j/dt + D₊v_j = 0, (iii) dv_j/dt + D₀v_j = 0。已知其中两个稳定。(a-i) 哪个不稳定，为什么？(a-ii) 两个稳定的分别对应图 1 的哪条曲线，为什么？
> (b) 取时间离散 (v_j^{n+1}−v_j^n)/Δt + D((v_j^{n+1}+v_j^n)/2) = 0。证明对应图 1(A) 的离散满足 ‖v^{n+1}‖²_h = ‖v^n‖²_h，而对应图 1(B) 的满足 ‖v^{n+1}‖²_h ≤ ‖v^n‖²_h，其中 ‖v‖²_h=(v,v)_h, (v,w)_h=Σ h v_j w_j。**Hint.** 先找 α_± 使 D_±v_j = D₀v_j + α_±D₊D₋v_j。

**解题思路**：
1. (a-i) 用离散 L² 内积检验：D₋ 对应 (D₋v,v)_h = −½hΣ|D₊v|² ≤ 0（半负定）；D₊ 对应 (D₊v,v)_h = +½hΣ|D₊v|² ≥ 0（半正定）→ **D₊（ii）不稳定**（半离散层面放大因子模 >1）；D₀ 是反对称 → 稳定但无耗散。
2. (a-ii) 稳定的两个是 (i) D₋ 与 (iii) D₀。用 RK4 演化一周期：**D₀（中心差分）无色散误差以外还产生振荡，表现为图 1 中带振荡尾巴的那条**；**D₋（迎风）有强数值耗散，表现为幅值被抹平、但无振荡的那条**。图中 (A) 一般是**保幅值的中心差分**，(B) 是**耗散的迎风差分**——由 (b) 的结论「(A) 保范数、(B) 耗散」反推可确定。
3. (b) 关键恒等式（Hint 所指）：由 Taylor 展开
   D₋v_j = D₀v_j − (h/2)D₊D₋v_j，D₊v_j = D₀v_j + (h/2)D₊D₋v_j。
   于是 D = D₀ + αD₊D₋，其中 α = ∓h/2。
4. 对 Crank–Nicolson 型格式取内积 (·, v^{n+1}+v^n)_h。D₀ 的反对称性使带 D₀ 的项在**周期边条件**下（求和相消）消失；只剩 α(D₊D₋(v^{n+1}+v^n), v^{n+1}+v^n)_h = −α h Σ|D₊(v^{n+1}+v^n)_j|²。
5. 于是 (1/Δt)(‖v^{n+1}‖²−‖v^n‖²) = −(1/2)(Dw,w)_h = (Δt·α·h/2)‖D₊w‖²，w=v^{n+1}+v^n：
   - α = 0，即 **D₀（中心差分）** → 右端恒为 0 → **‖v^{n+1}‖²_h = ‖v^n‖²_h（严格保范数，对应图 1(A)）**；
   - α = −h/2，即 **D₋（迎风）** → 右端 = −(Δth²/4)‖D₊w‖² ≤ 0 → **‖v^{n+1}‖²_h ≤ ‖v^n‖²_h（耗散，对应图 1(B)）**；
   - α = +h/2，即 D₊（下风）→ 右端 > 0，**每步放大 → 不稳定**，这正是 (a-i) 的答案，也解释了它为何不在图 1 中。
> 这题把「von Neumann 稳定性」升级为「能量恒等式级别的精确结论」，是 Team 卷最典型的风格。

### 代表题 5｜2023 数学物理 Individual 第 2 题（θ 角变量、中心扩张与瞬子）

**题面（抽取原文，含抽取存疑标注）**：
> Consider a charged particle on a circle, parameterized by angle θ ∼ θ + 2π. It moves under a constant magnetic field B perpendicular to the plane of the circle. The Lagrangian of the system is given by L = ½θ̇² + (B/2π)θ̇.
> (1) Find the spectra and corresponding wave functions of the system (set ℏ = 1), and show the ground states have a two-fold degeneracy for B = π.
> (2) For B = π, the system admits a Z₂×Z₂ symmetry generated by θ → θ+π and θ → −θ. Find how they act on the two-fold ground states and the commutation relation of the two operators, and thus show that the Z₂×Z₂ symmetry is central extended to the dihedral group with 8 elements D₈ = ⟨r, s | r⁴ = s² = 1, s r s = r³⟩.
> (3) Suppose now the particle moves under an extra potential V = λ cos(2θ). Show that there are still two ground states perturbatively. Use the above results to argue that the two-fold ground states cannot be lifted non-perturbatively for generic λ, and explicitly verify it via an one-instanton computation (i.e. the leading contribution as ℏ→0 to the tunnelling amplitude between the two perturbative vacua).

**解题思路**：
1. **谱**：L 中 θ̇ 线性项给出规范势 A_θ = B/2π，动量 p_θ = θ̇ + B/2π；量子化 p_θ→−i∂_θ，哈密顿量 H = −½(∂_θ + iB/2π)²（与 (1/L²) 的惯量因子无关）。本征函数 ψ_m(θ)=e^{imθ}/√(2π)，m∈Z，本征值 E_m = ½(m + B/2π)²（**注意 B=π 时 E_m=½(m+1/2)²**，抽取文本未显式给出该式，此处为推断，属**抽取存疑**）。
2. **B=π 的两重简并**：m 与 −m−1 给同一能量（因为 m+1/2 与 −(m+1/2) 平方相同），最低两个态 m=0 与 m=−1 简并。
3. **Z₂×Z₂ 的投影表示**：T: θ→θ+π 作用在基态上给出 e^{iπ m} 的相位差，两个生成元在**二重简并子空间**上的矩阵满足 rs = −sr（反对易），故 ⟨r,s | r⁴=s²=1, srs=r³⟩ 且 s r = r³ s = r⁻¹ s，在投影表示里升级为 srs⁻¹ = r³ 与额外相位 → 中心扩张成 8 元二面体群 D₈（2 维不可约表示正是 D₈ 的忠实 2 维表示）。
4. **加 V=λcos2θ 的微扰**：在简并子空间内计算 V 的 2×2 矩阵，因 V(θ+π)=V(θ) 且 V(−θ)=V(θ)，矩阵是对角/同号的，**微扰层面不劈裂**。
5. **非微扰（思路，非完整解）**：把 θ 视为在双阱势 V=λcos2θ 的两个极小（对应两个微扰真空）之间运动，WKB/瞬子近似给出隧穿振幅 A ∝ e^{−S_inst/ℏ}，其中 S_inst=∫√(2(V(θ)−E)) dθ 由势垒形状决定。题目要求"显式验证"：需写出瞬子解 θ_cl(τ)（虚时间中的运动方程解）并算出 ΔE ∝ e^{−S_inst/ℏ}，再用 (2) 得到的 Z₂×Z₂ 投影表示说明该振幅在对称性下只能取 0 或纯相位，故**简并到所有阶微扰以及单瞬子阶都不被解除**。这正是「对称性保护简并」的物理。（本题完整瞬子计算超出题面抽取信息，此处仅给出步骤。）
> 该题同时命中「量子力学、QFT、拓扑/瞬子」三个考点，是 MathPhys Individual 卷难度 5 的代表。

### 代表题 6｜2024 数学物理 Team 第 3 题（Killing–Yano、共形不变性、粒子视界）

**题面（抽取原文）**：
> **1. Conservation laws:** Let (M, g_ab) be a 4-dimensional vacuum spacetime. Recall that a Killing–Yano 2-tensor is a 2-form Y_ab = Y_[ab], satisfying ∇_(a Y_b)c = 0.
> (a) Show that ∇_a Y_bc = ∇_[a Y_bc]. (b) Use the result from (a) to show that for S₁, S₂ closed surfaces in M bounding a 3-volume Σ, it holds that ∫_{S₁} R_abcd Y^cd dS^ab = ∫_{S₂} R_abcd Y^cd dS^ab.
> **2. Stress–energy tensor:** Show that the Maxwell action S = (1/16π)∫ F_ab F^ab √|det g| d⁴x is conformally invariant and use this to show the Maxwell stress–energy tensor is traceless.
> **3. Particle horizon:** Let M = (0,∞)×Σ where Σ is hyperbolic 3-space. Assume that M has line element ds² = −dt² + t²γ for t > 0. Let P, Q be two events at time t₀ > 0. Show that there is an event to the past of P, Q that can send signals to both P, Q. Is the same true for the line element −dt² + t^{3/2}γ?

**解题思路**：
1.(a) 把 ∇_(a Y_b)c = 0 全反对称化：3 个指标循环求和，利用 Y 是 2 形式（Y_ab 反对称）与联络无挠，得到 3∇_[aY_bc] = 0，即 ∇_aY_bc = ∇_[aY_bc]。
1.(b) 对 4 形式 J = R_abcd Y^cd (在 Y 为 KY 张量时) 取外微分 dJ = ∇_[e(R_abcd Y^cd])；用 Bianchi 恒等式 ∇_[eR_abcd]=0 与 (a) 得 ∇_[eY_cd]=0，故 dJ=0；对 3-体 Σ 用 Stokes 定理即得两个边界曲面积分相等（这也是 KY 张量给出守恒荷的机制）。
2. 4 维中 g→Ω²g 时 √|det g|→Ω⁴√|det g|，F 是 2 形式故 F_ab F^ab 不变（两个逆度规 × 两个正度规抵消），总权重 Ω⁴·Ω^{−4}=1 → **作用量共形不变**。能动张量 T_ab = (1/4π)(F_ac F_b^c − ¼g_ab F²)，其迹 T^a_a ∝ F² − (4/4)F² = 0；等价论证：共形变换 δS/δΩ|Ω=1 ∝ ∫T^a_a = 0。
3. **判据**：Δx = ∫ dt/a(t) 是否发散决定有没有粒子视界。a(t)=t 时 ∫_0^{t₀} dt/t = ∞ → 无粒子视界。
3. **第一种度规** ds²=−dt²+t²γ 即 **Milne 宇宙**（取 γ 为平直度规时它就是平直 Minkowski 的加速坐标）：令 T=ln t、X=x 可把度规写成 −dT²+|dX|²，故它局部等起于平直空间；Minkowski 中任意两个未来事件的过去光锥必有交（例如取它们的中点向过去的时间轴），所以第一问答案是**是**。
3'. **第二种度规** ds²=−dt²+t^{3/2}γ 对应 a(t)=t^{3/4}，而 ∫_0^{t₀} t^{−3/4}dt = 4t₀^{1/4} < ∞，即 **存在粒子视界**：等时事件 P,Q 的共动距离超过 2×视界半径时，它们的过去光锥不再相交，**结论不成立**（只有足够近的 P,Q 才有公共过去事件）。

### 代表题 7｜2025 应用与计算数学 Overall 第 1 题（prox 算子与 Moreau 分解）

**题面（抽取原文）**：
> Given a convex function f : R^n → R and a scalar α > 0, the proximal operator prox_{α,f} of f is defined as the mapping from a point x ∈ R^n to the unique solution of the minimization problem: min_{y∈R^n} f(y) + (1/2α)‖y−x‖²₂.
> (a) Derive the explicit formula for prox_{α,f} when f(x)=‖x‖₁. (b) Derive the explicit formula for prox_{α,g} when g(x)=‖x‖₂. (c) Prove that prox_{f+g} = prox_g ∘ prox_f holds for f(x)=‖x‖₁ and g(x)=‖x‖₂.

**解题思路**：
- (a) 逐坐标可分：min_y |y_i| + (1/2α)(y_i−x_i)² 的次梯度条件 0 ∈ ∂|y_i| + (y_i−x_i)/α 给出**软阈值** (prox_{α,‖·‖₁} x)_i = sign(x_i)max(|x_i|−α, 0)。
- (b) min_y ‖y‖₂ + (1/2α)‖y−x‖²：由对称性 y 与 x 同向，令 y=t·x/‖x‖，对 t≥0 最小化 t + (1/2α)(t−‖x‖)² 得 t = max(‖x‖−α, 0)，故 **prox_{α,‖·‖₂}x = max(0, 1−α/‖x‖)x**（块软阈值）。
- (c) 验证复合：先做 ℓ₁ 软阈值 s=sign(x)max(|x|−α,0)，再对 s 做 ℓ₂ 块软阈值。由于 ℓ₂ 收缩只按整体范数缩放、ℓ₁ 只逐坐标收缩，两者都保持各分量符号且**同向**，可逐项验证 prox_{α,‖·‖₁+‖·‖₂}(x) = prox_{α,‖·‖₂}(prox_{α,‖·‖₁}(x))。一般地这只在特定 f,g 成立（Moreau 分解 prox_f + prox_{f*}∘... 的等号对 ℓ₁/ℓ₂ 组合有专门结论），题目要求的是**具体验证**。
> 这题是 2025 年总决赛新引入的「机器学习/凸优化」味道的题，与 2024 Overall 的压缩感知、2025 Team 的 softmax 共轭构成同一条新线索。

### 代表题 8｜2023 应用与计算数学 Overall（Klein–Gordon 离散能量守恒格式）

**题面（抽取原文）**：
> Consider the nonlinear Klein–Gordon equation ε²∂_tt u(x,t) − ∂_xx u(x,t) + (1/ε²)u(x,t) + f(u(x,t)) = 0, 0<x<1, 0<t<T, u(x,0)=g₀(x), ∂_t u(x,0)=(1/ε²)g₁(x), u(0,t)=u(1,t)=0.
> 1. Define the Hamiltonian (or energy) as E(t) := ∫₀¹ [ε²|∂_t u|² + |∂_x u|² + (1/ε²)u² + F(u)] dx, where F(u)=2∫₀^u f(s)ds. Show that the Hamiltonian is conserved, i.e. E(t) ≡ E(0).
> 2. Construct an explicit second-order (in space and time) finite difference (EXFD) method for the problem and find its linear stability.
> 3. Construct a second-order (in space and time) finite difference method for the problem such that the Hamiltonian (or energy) is conserved in the discretized level and prove it.

**解题思路**：
1. 用 (1/ε²)∂_t u 乘方程并积分：ε²∂_tt u·(1/ε²)∂_t u = ∂_t u ∂_tt u = ½∂_t[(∂_t u)²]；−∂_xx u·∂_t u 分部积分后 = ∂_t[½|∂_x u|²]（边条件使边界项为零）；(1/ε²)u∂_t u = ∂_t[u²/(2ε²)]；f(u)∂_t u = ½∂_t F(u)（因 F(u)=2∫f）。全部对 x 积分得 dE/dt = 0。
2. **EXFD**：空间用 u_{j+1}−2u_j+u_{j−1})/h²；时间用中心二阶 (u^{n+1}−2u^n+u^{n−1})/τ²。线性化后对 f(u)=mu 做 von Neumann 分析：放大因子满足
   ε²(ξ−2+ξ⁻¹)/τ² − (e^{ikh}−2+e^{−ikh})/h² + 1/ε² + m = 0 → ξ+ξ⁻¹ = 2 − (τ²/ε²)[4sin²(kh/2)/h² + 1/ε² + m]，
   稳定条件为 |ξ|≤1 ⟺ (τ²/ε²)[4/h² + 1/ε² + m] ≤ 4，即 **τ ≤ 2ε/√(4/h² + 1/ε² + m)**，且因 1/ε² 项使 τ = O(ε²)（**ε 越小时间步必须越小**，这是该问题被出成考题的关键难点）。
3. **离散能量守恒格式**：对非线性项用「离散链式法则」——把 f(u) 在时间上离散为 (F(u^{n+1})−F(u^{n−1}))/(2τ) / ((u^{n+1}−u^{n−1})/(2τ))，即
   f → [F(u^{n+1})−F(u^{n−1})] / (u^{n+1}−u^{n−1})，
   再以 (u^{n+1}−u^{n−1}) 为权与方程作内积；线性部分用中心差分。此时离散能量
   E^n = Σ h[ε²((u^{n+1}−u^n)/τ)² /2 + ½|D₊u^n|² + (1/2ε²)|u^n|² + F(u^n)/2 + F(u^{n+1})/2]（对称化写法）
   逐步严格守恒，证明方式是**与 u^{n+1}−u^{n−1} 作内积后逐项配成差分**。

---

## 7. 存疑 / 无法分析清单

### 7.1 无法分析的文件（0 个真正不可分析）

| 文件 | 索引显示 | 实际情况 | 处置 |
|---|---|---|---|
| 2020 Applmath (Individual)- set1（密码Yau-ACM20).pdf | chars=0, pages=0 | 加密 PDF，密码 Yau-ACM20 有效，解密后 2 页 1618 字符 | ✅ 已恢复并纳入统计（`scripts/_finals_2020/`） |
| 2020 Applmath (Individual)- set2（密码Yau-ACM20).pdf | chars=0, pages=0 | 同上，2 页 1878 字符 | ✅ 已恢复 |
| 2020 Applmath (Overall)（密码Yau-ACM20).pdf | chars=0, pages=0 | 同上，2 页 1892 字符 | ✅ 已恢复 |

解密时 MuPDF 会打印 `MuPDF error: format error: corrupt object stream (N 0 R)` ——这是**加密对象的正常提示**，不影响取文本。

### 7.2 卷别归属存疑

| 项 | 问题 | 证据 | 处置 |
|---|---|---|---|
| 2014 Individual vs Overall | `2014 Applmath (Individual and Overall).pdf` 是 4 份单页文档拼接（6 页）。页 1 抬头 “Applied Mathematics, Individual, 2014”；页 4–6 抬头 “Oral exam, applied and computational mathematics, individual, 2014”（页码 1–3）；页 2、页 3 无抬头、页脚均标 “1”，且页面尺寸与页 1 不同 | 逐页渲染确认（595×770 vs 579×819） | 推断 页 1+4–6 = Individual（3 题），页 2–3 = Overall（2 题）；标为「推断」 |
| 2017 Applied Team 三个文件 | `2017 Applied (Team).pdf`(2 页: 三角形角导数 + Lanczos)、`2017 Applied (Team) (2).pdf`(2 页: 最优质量传输 + 一幅图)、`2017 Applmath (Team).pdf`(1 页: 流体守恒律) | 三份都标 2017、都为 Team，内容互不重复 | 视为 **2017 Team 卷的 3 个片段**（合计 4 题），不视为 3 份独立考试 |
| 2017 Applied (Team) (2) 的第 2 页 | 只有一幅插图（Ω、W_i、F_i、π_j、u_h(x) 标注）与页码 | 抽取文本仅 2 行 | 该页无题面，不影响题目完整性 |

### 7.3 公式抽取存疑（已尽力交叉核对，仍标注）

| 位置 | 现象 | 影响 |
|---|---|---|
| 2023 Math-Phys Individual Q2 (1) | 抽取文本只说 “Find the spectra and corresponding wave functions”，**未印出能量本征值表达式**；报告中的 E_m=½(m+B/2π)² 为推断 | 结论（B=π 两重简并）可由文本直接支持；具体公式标注推断 |
| 2019 Applmath (Individual) Q4 | 差分算子的系数 1/12、5/6、1/12 与 δ² 定义在抽取中跨行断开，分子分母被拆散 | 题意（时二阶空四阶紧致格式）明确，系数按上下文复原 |
| 2024 ACM (Overall) Q1 | ∥x∥_(s) 的「原子分解」定义在抽取中出现换行错位 | 题意（C_s∩B₂ 有界性）明确，具体范数记号按上下文复原 |
| 2013 Applmath (Individual) Q2 | 图 1/图 2 的说明文字混入正文；χ(M)=|V|+|F|−|E| 的符号顺序与常规 χ=V−E+F 一致，无歧义 | 不影响 |
| 2015 Applied (Team) Q1 | 广义特征值问题中两个矩阵的非零元位置在抽取中排列错乱（−1 与 1 的上下三角归属） | 题目类型（三对角广义特征值）明确；**具体矩阵元归属存疑** |
| 2014 Individual Q5 / 2017 Team Q1 | 图中符号（θ_i, l_i, r, d）与正文公式交错 | 公式本身（∂θ_i/∂l_i=l_i/(2A) 等）抽取完整，可用 |
| 2024 Math-Phys Team Q3 | Maxwell 作用量抽取为 “S = (1/16π)∫ F_ab F^ab √|det g| d⁴x”，其中 √ 符号被抽成 “p” （`p| det g|`） | 已按上下文复原为 √|det g|；标注为抽取噪声 |

### 7.4 语料结构性缺口（不是分析失败，而是原始目录缺文件）

| 缺口 | 年份 | 说明 |
|---|---|---|
| ACM Team 卷缺失 | 2013、2016、2020、2021、2022 | 原目录 `2012-2025Applied Math and Computational Math/Team/` 只含 2012、2014、2015、2017(×3)、2018、2019、2023、2024、2025 |
| ACM Overall 2014 无独立文件 | 2014 | 只能从拼接件恢复（见 7.2） |
| MathPhys Team 2022 | 2022 | 原目录不含；MathPhys Team 自 2023 开始 |
| 官方解答 | 全部 | 总决赛语料**只有题目、没有解答**（与初赛语料 2020–2022 有 16 份解答卷不同） |

---

## 8. 关键数字摘要

- 语料：`txt_finals` 195 个 txt；本分析范围内 **52 条索引记录**（Applied 40 + MathPhys 12），占 26.7%。
- 可分析卷面：**55 个单元**（52 原文件 + 3 个 2020 解密文本）；**真正无法分析的文件 = 0 个**。
- 2020 三份卷（Individual set1 / set2 / Overall）被 `Yau-ACM20` 口令加密，索引 `chars=0` 是假阴性；解密后 2 页 / 1618、1878、1892 字符，全部可用。
- chars<800 的「稀疏」卷共 **8 份**，全部是「一题一张纸」的 Overall/短卷，不是扫描件。
- 人工逐卷计数：**约 117 道题**（ACM Individual 41、ACM Overall 18、ACM Team 26、MathPhys Individual 15、MathPhys Overall 8、MathPhys Team 9）。
- 脚本自动切分单元：**128 个**（2020 计入后），总字符 **87354**，平均 682.5 字符/单元。
- 卷别规模：Individual 59 单元 / 平均 670.0 字符 / 1.69 小问；Overall 33 / 578.6 / 1.48；Team 36 / **798.1** / **2.64**。
- 科目×卷别最长：**MathPhys Team 1008.6 字符**；最短：**ACM Overall 515.7 字符**。
- 考点 Top5（命中题次）：数值线性代数 19、变分法/最优化 16、量子力学 16、广义相对论 15、经典力学 15；PDE 有限差分 14、QFT 13。
- 任务动词：`show` 59（46.1%）、`prove` 35（27.3%），**show+prove 合计 94 单元 = 73.4%**；`compute` 仅 9（7.0%）。
- 与初赛同科目对比（平均字符）：ACM 总决赛 **635.9** vs 初赛 688.4；MathPhys 总决赛 **816.4** vs 初赛 959.8 —— **总决赛单题并不更长，平均小问数反而更少**（ACM 1.89 vs 2.48；MathPhys 1.94 vs 3.37）。
- 与初赛整体对比：初赛全语料平均 438.6 字符（中位 329），总决赛平均 682.5 / 中位 523 —— 均值高 **55.6%**，中位高 **59.0%**。
- **Overall（全能赛）是总决赛独有**：初赛 120 份试卷中含 overall/all-round 的 = 0 份；总决赛本子领域有 13 份。
- **「N 选 k」免答指令 10 份卷**（2019 ACM Ind 5 选 3；MathPhys 2023–2025 各 3 份），初赛 0 份。
- MathPhys 是 **2022 年新设**科目；初赛 MathPhys 30 题**全为 individual**，总决赛自 2023 起设 Team（9 题，平均 1008.6 字符）。
- ACM Team 卷缺 5 个年份（2013、2016、2020、2021、2022）；ACM Overall 2014 无独立文件。
- 新增（初赛无）考点线索：离散微分几何/共形几何 6 次、压缩感知 3 次、凸优化/prox/softmax 4 次、Wasserstein 梯度流 1 次、Γ-收敛 1 次。
- 题目复用：2014 Team Q1 与 2015 Individual Q2 完全相同；2017 Team Q2 与 2020 Individual set2 Q1 的 Lanczos 题几乎逐字相同。
- 语料无官方解答：总决赛部分**只有题面、没有答案卷**。

---

*报告完。所有题号、题面均逐字取自 `corpus/finals/` 或 `scripts/_finals_2020/` 的 PyMuPDF 抽取文本；公式有损处已在第 7.3 节逐条标注。统计脚本与中间表：`scripts/finals_app_phys_stats.py`、`finals_app_phys_stats.json`、`finals_app_phys_tables.md`。*
