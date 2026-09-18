# 丘成桐大学生数学竞赛 · 代数与数论（Algebra and Number Theory）真题解题讲义

## 审稿状态

- **审稿报告**：`.tmp/burn2026/reports/referee_algebra.md`（对抗性审稿，逐题复核题面、结论、证明与全部关键步骤，附可复跑脚本 `.tmp/burn2026/referee/checkA~D.py`）。
- **裁定统计**：VERIFIED **6** 道（题 1、3、4、6、8、9）；MINOR-FIX **4** 道（题 2、5、7、10）；SERIOUS-ERROR **0**；UNVERIFIED **0**。**10 道题的结论与主证明均正确**，全部已发现问题已按下述标记回填修正。
- **修正日期**：2026-09-18（审稿与回填同日完成）。修正处一律带一行标记「✅ 已按 referee_algebra.md 修正」。
- **高风险题（结论正确，但建议自己复算）**：**题 5**（子域格 10 个子域、24 条包含关系最易抄错）、**题 8(d)**（判别式—指数—迹三步串联，最能检验是否真懂）。另外 **题 2、7、10** 的补充说明/边界讨论/附录公式曾被审出实质错误（已修正），复习时请以**正文**为准，不要沿用旧记忆。
- **题面复核口径**：题 1–9 已用原卷 PDF（`F:\丘成桐大学生数学竞赛历年笔试真题\`）逐字复核；**题 10（2026 ind №2）本地无原卷**，仅与 `problems_full.json` 抽取文本比对，标点细节可能与原卷有出入。

**数据来源与核对方式**

- 题目全部取自 `.tmp/burn2026/data/problems_full.json`（该库共 757 条真题条目，其中 `subject = "Algebra & Number Theory"` 共 149 条，年份 2010–2026）

> ✅ 已按 referee_algebra.md 修正（原表述：「共 150 条」——当前 757 题快照下精确匹配为 149 条），**没有任何一道是自编题**。
- 凡题面中公式可能因 PDF 抽取而受损者，均已用 PyMuPDF（`pylibs/fitz`）从原始试卷 PDF（`F:\丘成桐大学生数学竞赛历年笔试真题\`，只读）重新提取原文逐字比对，并在题面下标注「据 PDF 校正」。
- 标注「原文」者表示 JSON 抽取文本与 PDF 原文一致、或（2026 年）本地无 PDF 归档可查。

**记号约定**

$p$ 恒表示素数；$\zeta_n = e^{2\pi i/n}$；$K^{\times}$ 表示 $K\setminus\{0\}$；$\mathrm{Tr}_{K/F},\ \mathrm{N}_{K/F}$ 为迹与范数；$\left(\frac{\cdot}{\cdot}\right)$ 为 Legendre 符号；$v_p$ 为 $p$ 进赋值，$|p|_p=p^{-1}$；$\mathcal O_K$ 为 $K$ 的整数环；$D_4$ 按竞赛惯例指 8 阶二面体群（正方形的对称群）；$Q_8$ 指 8 阶四元数群。

---

## 一、选题说明

### 1.1 为什么是这 10 道

本讲义要在一份材料里给出「代数与数论」这门科目的骨架，因此选题同时受四条约束支配：**跨年份分散**、**难度分层（3 基础 + 4 中等 + 3 偏难）**、**考点骨架完整**、**可给出毫不含糊的完整证明**。最终 10 道题覆盖 **10 个不同年份**（2010、2012、2013、2014、2016、2017、2018、2019、2022、2026），横跨丘赛代数科目全部 17 个年份中的 10 个，其中既有 2010 年首届的题目，也有最新一届（2026）的压轴题。

选材时遵循三条原则：

1. **宁可少、不可糊。** 丘赛代数卷里有相当比例的题目依赖超出本科必修范围的重型工具（类域论、CM 理论、完备化上的测度论、代数几何），这类题即使抄来参考答案也难以讲出「思路的来路」。本讲义优先选取那些**工具全部可自足、证明可以写到最后一个等号**的题。例如 2012 individual 第 5 题（复环面的 endomorphism ring、$R^{\times}$ 的最大阶）需要虚二次域的 CM 理论，果断放弃；2014 individual 第 2 题（Hilbert 矩阵型正定性）虽是漂亮的实分析题，但完全落在分析与矩阵论，不算代数骨架，也放弃。
2. **一道题尽量充当一个「公式/定理的载体」。** 例如选 2019 individual 第 5 题是为了让「有限域上 Binet 公式 + 范数映射满射」这一整套手法落地；选 2022 individual 第 5 题是为了让「分圆域的单位元、$1-\zeta_p$ 的迹与范、$\mathcal O_K=\mathbb Z[\zeta_p]$ 的证明」一次性讲透。
3. **难度分层要服务于讲义用途。** 3 道基础题（题 1、2、3）是「看穿一步就能做完」的题，用来校准手感；4 道中等题（题 4、5、6、7）是丘赛个人赛的主流难度；3 道偏难题（题 8、9、10）分别代表三种「硬」：题 8 硬在代数数论的技术堆叠（判别式、指数、整数环的判定），题 9 硬在「局部处处可解却无整数解」的无穷递降（含模 $p^n$ 计数与 Hensel 型提升），题 10 硬在构造性工具（特征和、Jacobi 和）的引入。

> ✅ 已按 referee_algebra.md 修正（原表述：把「Hensel 型论证」挂在题 8 名下——Hensel 提升属题 9(b)）

### 1.2 覆盖了哪些考点（骨架表）

| 编号 | 年份 / 卷别 / 题号 | 骨架考点 | 核心工具 / 定理 | 难度 |
|---|---|---|---|---|
| 题 1 | 2010 individual №1 | 线性变换的交换子、共同特征向量 | 特征子空间不变性；Lie 定理（作点评） | 2 |
| 题 2 | 2012 individual №1 | 整系数多项式在 $\mathbb Q$ 上的不可约性 | Eisenstein 判别法 + Gauss 引理 | 1 |
| 题 3 | 2018 individual №3 | 有限群的 Sylow 理论、半直积的平凡性 | Sylow 三定理；$p^2$ 阶群交换 | 2 |
| 题 4 | 2013 individual №1 | 群扩张的分类、自同构群 | Sylow + 半直积；全形 $\mathrm{Hol}(C_{13})$ | 3 |
| 题 5 | 2016 team №3 | Galois 理论、Galois 对应、子域格 | 分裂域、正规性、$D_4$ 的子群格 | 3 |
| 题 6 | 2017 individual №2 | 有限 Abel 群的 Fitting 分解 | 链稳定 + 有限集上自映射的单满等价 | 3 |
| 题 7 | 2019 individual №5 | 有限域、Fibonacci、范数映射 | Binet 公式、二次互反、有限域乘法群的循环性 | 3 |
| 题 8 | 2022 individual №5 | 分圆域：极小多项式、迹与范、整数环 | Eisenstein、$\Phi_p(1)$、判别式与指数、迹的 $\mathbb Z$-线性 | 4 |
| 题 9 | 2014 individual №3 | 二次型/ Pell 型方程、局部–整体 | 模 $p$ 计数、Hensel 引理、无穷递降（用范 $-1$ 单位 $9+\sqrt{82}$） | 4 |
| 题 10 | 2026 individual №2 | 有限域上的椭圆曲线、特征和 | Legendre 特征、特征群正交性、Jacobi 和、三角不等式 | 5 |

可以看到，这张表恰好把「代数与数论」的四大板块各占若干：

- **群论**：Sylow 理论（题 3、4）、群扩张与自同构（题 4）、有限 Abel 群与模论（题 6）；
- **线性代数与表示论**：交换子与不变子空间（题 1）、Galois 群作为置换群（题 5）；
- **域论与 Galois 理论**：分裂域、Galois 对应、子域格（题 5）、分圆域（题 8）、有限域（题 7、10）；
- **数论**：不可约判别（题 2）、Pell 型方程与局部–整体（题 9）、二次互反与 Fibonacci（题 7）、代数数论（题 8）、椭圆曲线与特征和（题 10）。

### 1.3 与「年代批次报告」的关系

仓库中 `.tmp/burn2026/reports/*.md` 的各年代批次报告在题号归属上偶有错位（尤其是跨页切分的 team 卷，例如 JSON 中 2017-team 的第 1、2 题条目互相串行、2019-team 的第 1、2 题之间混入了第 1 题的结尾）。因此**本讲义所有题面均以原始 PDF 为准逐一核对**，不采用二手报告中的题面。

---

## 二、十道真题详解

---

### 题 1｜2010 / Algebra, Number Theory and Combinatorics / Individual / 第 1 题

**出处行**：2010 年，Algebra, Number Theory and Combinatorics（当时该科目名含组合），Individual Test（个人赛，6 题选 5 题作答），第 1 题。

**题面（原文，与 PDF 一致）**

> Let $V$ be a finite dimensional complex vector space. Let $A, B$ be two linear endomorphisms of $V$ satisfying $AB - BA = B$. Prove that there is a common eigenvector for $A$ and $B$.

（中文：设 $V$ 是有限维复向量空间，$A,B\in \mathrm{End}(V)$ 满足 $AB-BA=B$。证明 $A$ 与 $B$ 有公共特征向量。）

**解答**

记 $L_A, L_B$ 为 $A,B$，我们不用任何 Lie 代数定理，直接做。

**第一步：$B$ 有特征值，其（真）特征子空间被 $A$ 保持。**

因 $\mathbb C$ 代数闭，有限维非零空间上的 $B$ 至少有一个特征值 $\lambda\in\mathbb C$。置

$$W := \ker(B-\lambda I) \ne \{0\}.$$

显然 $B(W)\subseteq W$（$W$ 就是 $B$ 的 $\lambda$-特征子空间，元素 $w$ 满足 $Bw=\lambda w$）。

**第二步：$A(W)\subseteq W$。**

任取 $w\in W$。由 $AB-BA=B$ 得 $AB=BA+B$，于是作为算子等式 $AB=BA+B$。对 $w$ 作用：

$$A(Bw)=(BA+B)w=B(Aw)+Bw.$$

左边 $A(Bw)=A(\lambda w)=\lambda Aw$，右边 $B(Aw)+\lambda w$。故

$$\lambda Aw = B(Aw)+\lambda w\ \Longrightarrow\ B(Aw)=\lambda Aw-\lambda w=\lambda(Aw-w).$$

此式说明 $Aw-w$ 满足 $B(Aw-w)=\lambda(Aw-w)$，即 $Aw-w\in W$。于是 $Aw=(Aw-w)+w\in W+W=W$。$w$ 任意，故 $A(W)\subseteq W$。

**第三步：在 $W$ 上取 $A$ 的特征向量。**

$W\ne 0$ 是有限维复向量空间，且已证 $W$ 同时是 $A$-不变与 $B$-不变的。$A|_W$ 有特征值 $\mu$（$\mathbb C$ 代数闭），取 $0\ne v\in W$ 使 $Av=\mu v$。又 $v\in W$ 给出 $Bv=\lambda v$。于是 $v$ 是 $A$ 与 $B$ 的公共特征向量。$\blacksquare$

**点评（可写成一段「顺手的收获」）**：由 $AB-BA=B$ 可立刻推出 $B$ 幂零，且证明是纯线性的。对任意 $k\ge1$，用归纳法（或直接展开）可得

$$[A,B^k]=AB^k-B^kA=\sum_{i=0}^{k-1}B^i[A,B]B^{k-1-i}=\sum_{i=0}^{k-1}B^i\,B\,B^{k-1-i}=kB^k .$$

取迹（$\mathbb C$ 上 $\mathrm{tr}(XY)=\mathrm{tr}(YX)$，故 $\mathrm{tr}[A,B^k]=0$），得 $k\,\mathrm{tr}(B^k)=0$，即 $\mathrm{tr}(B^k)=0$ 对一切 $k\ge1$ 成立。若 $B$ 的特征值为 $\lambda_1,\dots,\lambda_n$，则 $\sum_i \lambda_i^k=0$ 对一切 $k\ge1$，由 Newton 恒等式得所有初等对称多项式为 $0$，从而特征多项式为 $t^n$，即 $B$ 幂零。

**本题考点 / 技巧（一句话）**：把等式 $AB-BA=B$ 重写成「$B$ 与 $A$ 的交换子还是 $B$」，再用 $A(Bw)=\lambda Aw$ 把它翻译成「$A$ 把 $B$ 的特征子空间拉回自己」，一步到位。

**难度**：$\boxed{2/5}$（关键是想到取 $B$ 的特征子空间而不是 $A$ 的）。

**同类题在哪几年出现过**：$[A,B]=B$ 型的交换子条件是丘赛的常客：2011 individual №4（极小多项式不可约 + 循环向量 $\Rightarrow$ 无非平凡不变子空间）、2014 individual №6（$AB=BA$ 时 $\det(A^2+B^2)\ge0$）、2017 individual №5（$U$ 可对角化且与 $VUV^{-1}$ 交换）、2023 individual №1（初等矩阵生成 $\mathrm{SL}_n$）。相关的「同时三角化 / 公共特征向量」思路也出现在 2010 individual №6（$S_4$ 的不可约复表示）与 2015 team №5（正规矩阵的对角化）。

---

### 题 2｜2012 / Algebra and Number Theory / Individual / 第 1 题

**出处行**：2012 年，Algebra and Number Theory，Individual Test（个人赛，6 题选 5 题），第 1 题。

**题面（据 PDF 校正，逐字一致）**

> Prove that the polynomial $x^6 + 30x^5 - 15x^3 + 6x - 120$ cannot be written as a product of two polynomials of rational coefficients and positive degrees.

（中文：证明整系数多项式 $f(x)=x^6+30x^5-15x^3+6x-120$ 不能分解为两个正次数的有理系数多项式之积，即 $f$ 在 $\mathbb Q[x]$ 中不可约。）

**解答**

**第一步：找出唯一可能的 Eisenstein 素数。**

Eisenstein 判别法要求存在素数 $p$，它整除**所有**非首项系数、但不整除常数项的次数够高（对 $p^2$ 不整除常数项的标准版本）。$f$ 的非首项系数为

$$30,\quad 0,\quad -15,\quad 0,\quad 6,\quad -120 .$$

它们的公因数为 $\gcd(30,15,6,120)=3$。所以能同时整除全部非首项系数的素数只有 $p=3$。（$p=2$ 不整除 $15$，$p=5$ 不整除 $6$，$p\ge7$ 更不可能。）

**第二步：验证 Eisenstein 条件。**

- 首项系数 $1$ 不被 $3$ 整除；
- $3\mid 30,\ 3\mid 0,\ 3\mid -15,\ 3\mid 0,\ 3\mid 6,\ 3\mid -120$；
- $3^2=9\nmid -120$（$120=3\times 40$，$40$ 不被 $3$ 整除）。

故 $f$ 是 $\mathbb Z[x]$ 中关于素数 $3$ 的 Eisenstein 多项式。

**第三步：引用判别法并回到有理系数。**

Eisenstein 判别法（含 Gauss 引理的标准形式）：若本原整系数多项式 $f$ 对某素数 $p$ 满足上述条件，则 $f$ 在 $\mathbb Q[x]$ 中不可约。由 Gauss 引理「$\mathbb Z[x]$ 中本原多项式的可约性等价于在 $\mathbb Q[x]$ 中的可约性」，即得 $f$ 不能写成两个正次数的有理系数多项式之积。$\blacksquare$

**补充说明（为什么不能靠「模约化」偷懒）**

模 $2$：$f\equiv x^6+x^3=x^3(x+1)(x^2+x+1)\pmod 2$，可约；
模 $5$：$f\equiv x^6+x = x(x+1)(x^4-x^3+x^2-x+1)\pmod 5$，可约；
模 $7$：$30\equiv2,\ -15\equiv6,\ 6\equiv6,\ -120\equiv6$，故 $f\equiv x^6+2x^5+6x^3+6x+6\pmod 7$，而 $x=1$ 是根（$1+2+6+6+6=21\equiv0$），可约。

也就是说，**在最小的几个素数上模约化不可行**：$p=3$ 时 $f\equiv x^6$（完全可约）；$p=2,5,7$ 时 $f$ 都可约（见上）。但这条路并非走不通，**「模约化必然失败」是错的**——$p=11$ 时
$$f\equiv x^6+8x^5+7x^3+6x+1\pmod{11}$$
在 $\mathbb F_{11}$ 上不可约（$a=0,1,\dots,10$ 处取值 $1,1,4,10,1,6,6,9,9,5,3$ 全非零，且无二次、三次因式），故「模 $11$ 约化 + Gauss 引理」同样是一条完整证明（$p\le 97$ 内还有 $53,59,79,97$ 也可行）。本题的「机关」其实是**效率**：直接算非首项系数的公因数 $\gcd=3$，一步就锁定 Eisenstein 素数 $3$，比逐个试模约化快得多。

> ✅ 已按 referee_algebra.md 修正（原表述：「常用的『找一个模 $p$ 不可约的约化』这条路在本例中会失败」——该断言为假，$f \bmod 11$ 不可约）

**本题考点 / 技巧（一句话）**：遇整系数高次多项式先算非首项系数的 $\gcd$ 与常数项的 $p^2$ 可除性，Eisenstein 往往就藏在那里；不要一上来就模约化。

**难度**：$\boxed{1/5}$（一旦想到 Eisenstein 就已结束；难点只在「不要被 6 次与不规则系数吓住」）。

**同类题在哪几年出现过**：不可约性判别是丘赛最高频的单点考点之一：2013 individual №5（整系数多项式在每个 $\mathbb F_p$ 上有根但在 $\mathbb Q$ 上无根，并问最小次数）、2013 team №5（$\mathbb F_2$ 上 2、3 次不可约多项式与 6 次不可约多项式的计数）、2020 individual №4（$\Phi_\ell$ 在 $\mathbb Q[x]$ 中的不可约性）、2021 individual №1（$x^p-x-a$ 在 $\mathbb F_p$ 上不可约且可分）、2024 individual №3（非完全域上 $X^p-a$ 的不可约性）、2025 individual №1 与 №5。可见「Eisenstein + Gauss 引理」是所有后续代数数论题的前置技能。

---

### 题 3｜2018 / Algebra and Number Theory / Individual / 第 3 题

**出处行**：2018 年，Algebra and Number Theory，Individual Test（个人赛，5 题 100 分），第 3 题（20 分）。

**题面（据 PDF 校正）**

> Prove that every group of order $99$ is abelian.

**解答**

设 $|G|=99=3^2\cdot 11$。

**第一步：Sylow 11-子群正规。**

设 $n_{11}$ 为 Sylow $11$-子群的个数。由 Sylow 第三定理：

$$n_{11}\equiv 1 \pmod{11},\qquad n_{11}\mid 9 .$$

$9$ 的因数为 $1,3,9$，其中模 $11$ 余 $1$ 的只有 $1$。故 $n_{11}=1$。设 $P$ 为唯一的 Sylow $11$-子群，则 $P\trianglelefteq G$，且 $|P|=11$ 为素数阶，所以 $P\cong \mathbb Z/11\mathbb Z$ **是循环群（因而交换）**。

**第二步：Sylow 3-子群是可交换的。**

取 Sylow $3$-子群 $Q$（$|Q|=9=3^2$）。引理：**$p^2$ 阶群必交换**。证明：设 $|H|=p^2$，若 $H$ 非交换则 $Z(H)\ne H$，故 $|Z(H)|<p^2$；由 Lagrange 定理（$|Z(H)|$ 整除 $p^2$）得 $|Z(H)|\in\{1,p\}$；若 $|Z(H)|=1$ 则由类方程 $p^2=1+\sum (\text{非中心类大小})$，每个非中心类大小被 $p$ 整除，右边 $\equiv 1\pmod p$，与左边 $\equiv 0\pmod p$ 矛盾；故 $|Z(H)|=p$，于是 $H/Z(H)$ 是 $p$ 阶群（循环），而「$H/Z(H)$ 循环 $\Rightarrow H$ 交换」（标准引理：若 $H/Z(H)=\langle gZ(H)\rangle$，则每个元素形如 $g^iz$，两个这样的元素相乘可交换）导致矛盾。故 $H$ 交换。

> ✅ 已按 referee_algebra.md 修正（原表述：「由 Langrange $|Z(H)|\in\{1,p\}$」——拼写笔误，且未说明 $|Z(H)|<p^2$ 的来路）

于是

$$Q\cong \mathbb Z/9\mathbb Z \quad\text{或}\quad Q\cong \mathbb Z/3\mathbb Z\times\mathbb Z/3\mathbb Z ,$$

两种情形都交换。

**第三步：$G$ 是 $P$ 与 $Q$ 的半直积，且作用平凡。**

因 $\gcd(11,9)=1$，有 $P\cap Q=\{1\}$ 且

$$|PQ|=\frac{|P||Q|}{|P\cap Q|}=11\cdot 9=99=|G| ,$$

故 $G=PQ$，且 $P\trianglelefteq G$ 给出 $G\cong P\rtimes_\varphi Q$，其中 $\varphi:Q\to \mathrm{Aut}(P)$ 是共轭作用。

而 $\mathrm{Aut}(P)\cong (\mathbb Z/11\mathbb Z)^{\times}$ 是 $10$ 阶循环群，所以 $|\mathrm{Aut}(P)|=10$。同态 $\varphi$ 的像的阶同时整除 $|Q|=9$ 与 $|\mathrm{Aut}(P)|=10$，故 $|\mathrm{Im}\,\varphi|\mid \gcd(9,10)=1$，即 $\varphi\equiv 1$ 平凡。

**第四步：结论。**

作用平凡意味着 $P$ 与 $Q$ 中元素两两交换，于是

$$G\cong P\times Q ,$$

而 $P$、$Q$ 都交换，故 $G$ 交换。$\blacksquare$

**附带得到的分类**：$G\cong \mathbb Z/11\times\mathbb Z/9\cong \mathbb Z/99$，或 $G\cong \mathbb Z/11\times\mathbb Z/3\times\mathbb Z/3\cong \mathbb Z/33\times \mathbb Z/3$。即 99 阶群只有两个同构类，且都交换。

**本题考点 / 技巧（一句话）**：Sylow 个数 $n_p\mid$ 余因子、$n_p\equiv1\bmod p$ 定出正规性，再用「$\mathrm{Aut}(\text{素数阶群})$ 的阶与另一 Sylow 子群阶互素 $\Rightarrow$ 作用平凡」把半直积降为直积。

**难度**：$\boxed{2/5}$。

**同类题在哪几年出现过**：这是丘赛的「保留曲目」。2010 team №5 与 2011 individual №6 是**同一道题**：证明 150 阶群不是单群；2016 individual №5（$|G|=2^nm$，$m$ 奇，$G$ 有 $2^n$ 阶元 $\Rightarrow$ $G$ 有 $m$ 阶正规子群）用的是同一套 Sylow + 作用的技术；2012 individual №2 与 2012 team №2（$\mathrm{GL}_n(\mathbb F_p)$ 的 Sylow 结构与 Sylow 子群个数）、2011 team №5（$\mathrm{GL}_3(\mathbb F_7)$ 的 Sylow 7-子群与其正规化子）、2025 individual №2（由 $\sigma^f=\tau^e=1,\ \sigma\tau\sigma^{-1}=\tau^p$ 定出的群的存在唯一性，本质也是 $\mathbb F_{p^f}^{\times}$ 上的半直积）都把 Sylow 计数与半直积当成主要工具。


---

### 题 4｜2013 / Algebra and Number Theory / Individual / 第 1 题

**出处行**：2013 年，Algebra and Number Theory，Individual（个人赛，160 分制），第 1 题，1.1 小题 15 分、1.2 小题 5 分。

**题面（据 PDF 校正）**

> 1.1 (15 pt) Classify finite groups of order $26$ up to isomorphisms.
> 1.2 (5 pt) For each finite group $G$ of order $26$, describe the group $\mathrm{Aut}(G)$ of automorphisms of $G$.

**解答 (1.1)：$26=2\cdot 13$ 阶群的分类**

设 $|G|=26$。

**第一步：Sylow 13-子群正规。** 设 $n_{13}$ 为 Sylow $13$-子群个数，则 $n_{13}\equiv1\pmod{13}$ 且 $n_{13}\mid 2$。$2$ 的因数为 $1,2$，模 $13$ 余 $1$ 的只有 $1$，故 $n_{13}=1$。记 $P$ 为唯一的 Sylow $13$-子群，$P\trianglelefteq G$，$P\cong \mathbb Z/13\mathbb Z$。

**第二步：$G=P\rtimes H$。** 取 $H$ 为 Sylow $2$-子群，$H=\langle t\rangle\cong\mathbb Z/2\mathbb Z$。因 $\gcd(13,2)=1$，$P\cap H=1$ 且 $|PH|=26=|G|$，故 $G=PH$，于是 $G\cong \mathbb Z/13\mathbb Z\rtimes_\varphi \mathbb Z/2\mathbb Z$，其中 $\varphi:\mathbb Z/2\to \mathrm{Aut}(\mathbb Z/13)$ 由 $\varphi(1)=$「$x\mapsto x^{a}$」给出。

**第三步：枚举可能的 $a$。** $\mathrm{Aut}(\mathbb Z/13)\cong (\mathbb Z/13)^{\times}$ 是 $12$ 阶循环群。同态的像的阶整除 $\gcd(2,12)=2$，故 $a^2\equiv 1\pmod{13}$。在域 $\mathbb F_{13}$ 中 $a^2=1$ 的解只有 $a=\pm1$（$a^2-1=(a-1)(a+1)$，域中无零因子；或直接说 $(\mathbb Z/13)^{\times}$ 循环，其 2 阶元唯一）。所以只有两种：

- $a\equiv1$：作用是平凡的，$G\cong \mathbb Z/13\times\mathbb Z/2\cong \mathbb Z/26\mathbb Z$（循环群）；
- $a\equiv-1\equiv12$：$t\,s\,t^{-1}=s^{-1}$（$s$ 是 $P$ 的生成元），得二面体群
  $$D_{26}=\langle s,t \mid s^{13}=t^{2}=1,\ tst^{-1}=s^{-1}\rangle,\qquad |D_{26}|=26 .$$

**第四步：两个群不同构。** $\mathbb Z/26$ 是交换群；$D_{26}$ 中 $tst^{-1}=s^{-1}\ne s$（因 $s$ 的阶为 $13>2$），故 $D_{26}$ 非交换。因此**恰好两类**，即

$$\boxed{\ \text{26 阶群恰有两个同构类：}\ \mathbb Z/26\ \text{与}\ D_{26}\ }$$

（严格说，$P\rtimes_\varphi Q\cong P\rtimes_{\varphi'}Q$ 当且仅当存在 $\alpha\in\mathrm{Aut}(P)$ 与 $\beta\in\mathrm{Aut}(Q)$ 使 $\varphi'(q)=\alpha\circ\varphi(\beta^{-1}q)\circ\alpha^{-1}$ 对一切 $q\in Q$ 成立，即 $\varphi,\varphi'$ 落在 $\mathrm{Aut}(P)\times\mathrm{Aut}(Q)$ 作用的同一轨道上；这里 $a=1$ 与 $a=-1$ 分别对应于平凡同态与唯一非平凡同态，两者不同构，与上面的交换性论证一致。）

> ✅ 已按 referee_algebra.md 修正（原表述：「同构当且仅当 $\varphi,\varphi'$ 相差 $\mathrm{Aut}(P)$ 的共轭作用」——判据不完整，漏了补群 $Q$ 的重参数化）

**解答 (1.2)：两个群的自同构群**

**(a) $G=\mathbb Z/26\mathbb Z$。** 自同构由 $1\mapsto a$ 决定，$a$ 必须是 $\mathbb Z/26$ 的可逆元，故

$$\mathrm{Aut}(\mathbb Z/26)\cong (\mathbb Z/26\mathbb Z)^{\times}.$$

由中国剩余定理 $(\mathbb Z/26)^{\times}\cong(\mathbb Z/2)^{\times}\times(\mathbb Z/13)^{\times}\cong \{1\}\times\mathbb Z/12\cong \mathbb Z/12\mathbb Z$。因此

$$\boxed{\mathrm{Aut}(\mathbb Z/26)\cong \mathbb Z/12\mathbb Z,\qquad |\mathrm{Aut}(\mathbb Z/26)|=\varphi(26)=12 .}$$

**(b) $G=D_{26}$。** 断言

$$\boxed{\mathrm{Aut}(D_{26})\cong \mathbb Z/13\mathbb Z\rtimes (\mathbb Z/13\mathbb Z)^{\times}=\mathrm{Hol}(\mathbb Z/13),\qquad |\mathrm{Aut}(D_{26})|=13\cdot 12=156 .}$$

证明分三步。

*第一步：$\langle s\rangle$ 特征，且 $D_{26}$ 的 2 阶元恰为 $s^{i}t\ (i\in\mathbb Z/13)$。*
$\langle s\rangle$ 是唯一的 Sylow $13$-子群（$n_{13}=1$），故对任意 $\psi\in\mathrm{Aut}(G)$ 有 $\psi(\langle s\rangle)=\langle s\rangle$。

$G$ 的每个元素唯一地写成 $s^{i}$ 或 $s^{i}t$（$i\in\mathbb Z/13$）。$s^{i}$ 的阶整除 $13$，故为 $1$ 或 $13$。而

$$(s^{i}t)^{2}=s^{i}\,t\,s^{i}\,t=s^{i}\,s^{-i}\,t^{2}=1 ,$$

故 $s^{i}t$ 的阶为 $2$（$s^it\ne1$）。于是 $G$ 的 2 阶元恰好是这 $13$ 个 $s^{i}t$。

*第二步：自同构由 $(a,b)$ 参数化。* 设 $\psi\in\mathrm{Aut}(G)$。由第一步，$\psi(s)=s^{a}$，其中 $a\in(\mathbb Z/13)^{\times}$ 唯一确定；又 $\psi(t)$ 必须是 2 阶元，故 $\psi(t)=s^{b}t$，$b\in\mathbb Z/13$ 唯一确定。反过来，对任意 $(a,b)\in(\mathbb Z/13)^{\times}\times\mathbb Z/13$，由 von Dyck 定理，定义

$$\psi_{a,b}(s)=s^{a},\qquad \psi_{a,b}(t)=s^{b}t$$

给出群同态，只需验证定义关系被保持：

- $\psi_{a,b}(s)^{13}=(s^{a})^{13}=1$；
- $\psi_{a,b}(t)^{2}=(s^{b}t)^{2}=s^{b}t s^{b}t=s^{b}s^{-b}t^{2}=1$；
- 用 $t^{-1}=t$、$ts^{-b}=s^{b}t$（由 $tst^{-1}=s^{-1}$ 得 $ts^{m}t=s^{-m}$）：
  $$\psi(t)\,\psi(s)\,\psi(t)^{-1}=(s^{b}t)\,s^{a}\,(t s^{-b})=s^{b}\,t s^{a} t\, s^{-b}=s^{b}\,s^{-a}\,s^{-b}=s^{-a}=\psi(s)^{-1}. $$

故 $\psi_{a,b}$ 是良定义的同态。它是单射：若 $\psi_{a,b}(s^{i}t^{j})=1$；$j=0$ 时 $s^{ai}=1\Rightarrow i=0$；$j=1$ 时 $s^{ai+b}t=1\Rightarrow t=s^{-(ai+b)}\in\langle s\rangle\cap\langle t\rangle=1$，矛盾。有限集上的单射即双射，故 $\psi_{a,b}\in\mathrm{Aut}(G)$，且 $\psi\mapsto(a,b)$ 是双射。于是

$$|\mathrm{Aut}(D_{26})|=12\cdot 13=156 .$$

*第三步：群结构。* 计算复合（约定先作用右边）：

$$\psi_{a,b}\circ\psi_{a',b'}(s)=s^{aa'},\qquad \psi_{a,b}\circ\psi_{a',b'}(t)=\psi_{a,b}(s^{b'}t)=s^{ab'}\,s^{b}\,t=s^{ab'+b}\,t .$$

即

$$(a,b)\cdot(a',b')=(aa',\ ab'+b),$$

这正是全形 $\mathrm{Hol}(\mathbb Z/13)=\mathbb Z/13\rtimes(\mathbb Z/13)^{\times}$ 的乘法（正规子群 $\{(1,b)\}\cong\mathbb Z/13$，补群 $\{(a,0)\}\cong(\mathbb Z/13)^{\times}\cong\mathbb Z/12$）。$\blacksquare$

（顺带：$\mathrm{Aut}(D_{26})$ 非交换，因为 $\mathrm{Hol}(C_{13})$ 中 $(a,0)$ 对 $(1,b)$ 的作用是 $b\mapsto ab$，非平凡。）

**本题考点 / 技巧（一句话）**：有限群分类的固定套路 —— Sylow 定出正规子群 $\Rightarrow$ 写成半直积 $\Rightarrow$ 枚举 $\mathrm{Aut}(N)$ 中的合法作用（这里「合法」= 像的阶整除补群的阶）；自同构群则通过「特征子群 + 2 阶元枚举 + von Dyck 检验」参数化。

**难度**：$\boxed{3/5}$（1.1 是标准动作；1.2 需要意识到「$s^it$ 全是 2 阶元」这一枚举技巧，并验证 $\psi_{a,b}$ 确实保持关系）。

**同类题在哪几年出现过**：群分类与 $\mathrm{Aut}$ 计算：2014 team №4（分类 8 阶群）、2013 team №3（$\mathrm{SL}_2(\mathbb F_p)$ 的阶与元素阶）、2012 individual №2（$\mathrm{GL}_n(\mathbb F_p)$ 的 Sylow 结构）、2011 team №5（$\mathrm{GL}_3(\mathbb F_7)$）。$\mathrm{Hol}$ 类型的自同构群描述也出现在 2019 team №1（对称群中对换之积的中心化子 $\cong S_{\lceil n/2\rceil}\ltimes(\mathbb Z/2)^{\lfloor n/2\rfloor}$）。

---

### 题 5｜2016 / Algebra and Number Theory / Team / 第 3 题

**出处行**：2016 年，Algebra and Number Theory，Team（团体赛，5 题 100 分），Problem 3（20 分，(a) 10 分 + (b) 10 分）。

**题面（据 PDF 校正）**

> Let $K$ be the splitting field of the polynomial $x^{4}-x^{2}-1$.
> (a) (10 points) Show that the Galois group of $K$ over $\mathbb Q$ is isomorphic to the dihedral group $D_4$. Here we adopt the convention that $D_4$ is the group of symmetries of a square and has order $8$.
> (b) (10 points) Determine the lattice of subfields of $K$: find all subfields of $K$ and describe the partial order induced by inclusion.

**解答**

记 $f(x)=x^{4}-x^{2}-1$。解 $y^{2}-y-1=0$ 得 $y=\dfrac{1\pm\sqrt5}{2}$。置

$$\varphi=\frac{1+\sqrt5}{2},\qquad \psi=\frac{1-\sqrt5}{2}=-\frac1\varphi ,\qquad \alpha=\sqrt{\varphi } .$$

则 $f$ 的四个复根为

$$x_1=\alpha,\quad x_2=-\alpha,\quad x_3=\frac{i}{\alpha},\quad x_4=-\frac{i}{\alpha},$$

因为 $(i/\alpha)^{2}=-1/\varphi=\psi$，即 $\pm i/\alpha$ 正是 $x^{2}=\psi$ 的两根。

**第一步：$f$ 在 $\mathbb Q$ 上不可约，$[\mathbb Q(\alpha):\mathbb Q]=4$。**

$f$ 无有理根（$f(\pm1)=-1,\ 1\ne0$）。若 $f$ 在 $\mathbb Q[x]$ 中可约，则因它是首一四次且无有理根，必分解为两个首二因式：

$$x^{4}-x^{2}-1=(x^{2}+ax+b)(x^{2}+cx+d),\qquad a,b,c,d\in\mathbb Q .$$

比较系数：$a+c=0$，$b+d+ac=-1$，$ad+bc=0$，$bd=-1$。

由 $c=-a$ 得 $ad+bc=a(d-b)=0$。

- 若 $a=0$：则 $c=0$，$b+d=-1$ 且 $bd=-1$，故 $b,d$ 是 $T^{2}+T-1$ 的两根，即 $\dfrac{-1\pm\sqrt5}{2}\notin\mathbb Q$，矛盾；
- 若 $b=d$：则 $b^{2}=bd=-1$，$b^{2}=-1$ 在 $\mathbb Q$ 中无解，矛盾。

故 $f$ 不可约，从而 $f$ 是 $\alpha$ 的极小多项式，$[\mathbb Q(\alpha):\mathbb Q]=4$。

*（另一种说法：$\mathbb Q(\alpha)\supseteq\mathbb Q(\alpha^{2})=\mathbb Q(\sqrt5)$ 是二次子域，而 $\alpha\notin\mathbb Q(\sqrt5)$（因 $\varphi$ 不是 $\mathbb Q(\sqrt5)$ 中的平方；等价地由上面的不可约性），故次数为 $4$。）*

**第二步：$K=\mathbb Q(i,\alpha)$ 且 $[K:\mathbb Q]=8$。**

$\mathbb Q(\alpha)\subseteq\mathbb R$，而 $i\notin\mathbb R$，故 $i\notin\mathbb Q(\alpha)$，于是 $[\mathbb Q(\alpha,i):\mathbb Q(\alpha)]=2$（$i$ 满足 $x^{2}+1$），

$$[K:\mathbb Q]=4\cdot2=8 .$$

又四个根 $\alpha,-\alpha,i/\alpha,-i/\alpha$ 全在 $\mathbb Q(\alpha,i)$ 中（$i/\alpha=i\cdot\alpha^{-1}$），故 $\mathbb Q(\alpha,i)$ 就是 $f$ 的分裂域，即 $K=\mathbb Q(i,\alpha)$，且 $K/\mathbb Q$ 是 Galois 扩张（分裂域必正规，$\mathrm{char}\,\mathbb Q=0$ 必可分）。

**第三步：$G:=\mathrm{Gal}(K/\mathbb Q)\cong D_4$。**

$|G|=[K:\mathbb Q]=8$。$G$ 忠实作用在 4 个根上，故 $G\hookrightarrow S_4$，其像是一个 8 阶子群，即 $S_4$ 的 Sylow $2$-子群。$|S_4|=24=8\cdot3$，Sylow 第二定理给出所有 Sylow $2$-子群共轭，特别地都同构；而

$$\langle (1\,2\,3\,4),\ (1\,3)\rangle \le S_4$$

是由正方形对称群（$4$ 个顶点上的旋转与翻转）给出的 8 阶群，同构于 $D_4$。故 $G\cong D_4$。$\blacksquare$

**（第三步的显式版本，供 (b) 使用）** 记 $c$ 为复共轭、$\sigma$ 为「固定 $i$、把 $\alpha$ 送到 $i/\alpha$」的 $\mathbb Q(i)$-自同构（存在性：$[K:\mathbb Q(i)]=2$，故 $K/\mathbb Q(i)$ 是 Galois 扩张，设 $\tau$ 为其非平凡元。$\tau(\alpha)$ 是 $\alpha$ 在 $\mathbb Q(i)$ 上的共轭，必为 $\pm\alpha$ 或 $\pm i/\alpha$。若 $\tau(\alpha)=\alpha$，则 $\tau$ 固定 $i$ 与 $\alpha$，即 $\tau=\mathrm{id}$，矛盾；若 $\tau(\alpha)=-\alpha$，则 $\alpha^{2}=\varphi\in\mathbb Q(i)$，迫使 $\sqrt5=2\varphi-1\in\mathbb Q(i)$，与 $\mathbb Q(i)$ 是虚二次域矛盾。故 $\tau(\alpha)=\pm i/\alpha$；若为 $-i/\alpha$，把 $\tau$ 与复共轭 $c$ 复合（$c\tau c$ 把 $\alpha$ 送到 $c(\tau(\alpha))=c(-i/\alpha)=i/\alpha$）即得。因此 $\sigma$ 存在。等价地，也可直接验证 $\alpha$ 在 $\mathbb Q(i)$ 上不可约：设 $x^4-x^2-1=(x^2+ax+b)(x^2-ax+d)$ 于 $\mathbb Q(i)[x]$，则 $a=0$ 迫使 $(-1\pm\sqrt5)/2\in\mathbb Q(i)$（不可能），$b=d=\pm i$ 迫使 $a^{2}=1\pm2i$，而 $1\pm2i$ 不是 $\mathbb Q(i)$ 中的平方——这正是下文 $\langle cr\rangle$ 一行的计算），令

> ✅ 已按 referee_algebra.md 修正（原表述：「存在性：$\alpha$ 在 $\mathbb Q(i)$ 上的极小多项式仍是 $x^4-x^2-1$，因为在 $\mathbb Q(i)$ 上 $x^{2}=\varphi$ 与 $x^{2}=\psi$ 仍无解」——只排除了线性因子，未排除二次因式）

$$r:=c\circ\sigma .$$

作为 $K$ 上的自同构（按 $(\,\cdot\,)\mapsto$ 逐坐标写出）：

$$c:\ i\mapsto -i,\ \alpha\mapsto\alpha;\qquad \sigma:\ i\mapsto i,\ \alpha\mapsto \frac{i}{\alpha};\qquad r=c\sigma:\ i\mapsto-i,\ \alpha\mapsto-\frac{i}{\alpha}.$$

直接计算得

$$r^{2}:\ i\mapsto i,\ \alpha\mapsto-\alpha;\qquad r^{4}=\mathrm{id};\qquad crc=r^{-1}$$

（最后一条：用共轭置换写法验证——$crc$ 就是把 $r$ 的轮换记法中每个字母换成它在 $c$ 下的像，$r=(x_1x_4x_2x_3)\mapsto(x_1x_3x_2x_4)=r^{-1}$，见下）。

> ✅ 已按 referee_algebra.md 修正（原表述：残留未清理的「$i\mapsto c(r(-i))=c(i)=-i\cdot$？」残句）

因此

$$G=\{e,\ r,\ r^{2},\ r^{3},\ c,\ cr,\ cr^{2},\ cr^{3}\}\cong D_4=\langle r,c\mid r^{4}=c^{2}=1,\ crc=r^{-1}\rangle .$$

若把 $G$ 看成 $\{x_1,x_2,x_3,x_4\}$ 上的置换群（$x_1=\alpha,x_2=-\alpha,x_3=i/\alpha,x_4=-i/\alpha$），则

$$r=(x_1\,x_4\,x_2\,x_3),\qquad c=(x_3\,x_4),\qquad r^{2}=(x_1x_2)(x_3x_4),\qquad cr=(x_1x_3)(x_2x_4).$$

其中 $crc=r^{-1}$ 可用「用 $c$ 把 $r$ 的轮换记法中每个字母替换」验证：$r=(x_1x_4x_2x_3)\mapsto(x_1x_3x_2x_4)=r^{-1}$。$\square$

**第四步：（b）子域格。**

由 Galois 基本定理，$K/\mathbb Q$ 的子域与 $G$ 的子群反序一一对应，$[E:\mathbb Q]=[G:\mathrm{Gal}(K/E)]$。

$D_4=\langle r,c\rangle$ 的子群共 $10$ 个：

- 8 阶：$G$ 本身；
- 4 阶：$\langle r\rangle\cong C_4$，$\langle r^{2},c\rangle\cong C_2\times C_2$，$\langle r^{2},cr\rangle\cong C_2\times C_2$（注：$r^2$ 是中心元，$c,cr,cr^2,cr^3$ 是仅有的四个对合，其中 $c\cdot cr=r$ 阶为 4，故只有 $c,cr^2$ 与 $cr,cr^3$ 两两交换，于是只有上述三个 4 阶子群）；
- 2 阶：$\langle r^{2}\rangle,\ \langle c\rangle,\ \langle cr\rangle,\ \langle cr^{2}\rangle,\ \langle cr^{3}\rangle$ 共 5 个；
- 1 阶：$\{e\}$。

合计 $1+3+5+1=10$。

逐一求不动域。先记 $u:=\alpha+\dfrac{i}{\alpha},\ v:=\alpha-\dfrac{i}{\alpha}$。由

$$\frac1\varphi=\varphi-1,\qquad \varphi+\psi=-1$$

得

$$u^{2}=\alpha^{2}+2i+\frac{i^{2}}{\alpha^{2}}=\varphi+2i-\frac1\varphi=\varphi+2i-(\varphi-1)=1+2i,\qquad v^{2}=1-2i,\qquad uv=\alpha^{2}-\frac{i^{2}}{\alpha^{2}}=\varphi+\frac1\varphi=\sqrt5 .$$

| 子群 $H$ | $|H|$ | 不动域 $K^{H}$ | $[K^{H}:\mathbb Q]$ | 判据 |
|---|---|---|---|
| $G$ | 8 | $\mathbb Q$ | 1 | — |
| $\langle r\rangle$ | 4 | $\mathbb Q(\sqrt{-5})$ | 2 | $r(\sqrt5)=-\sqrt5$（因 $r(\alpha^{2})=(\frac{-i}{\alpha})^{2}=\psi$），故 $r(i\sqrt5)=i\sqrt5$ |
| $\langle r^{2},c\rangle$ | 4 | $\mathbb Q(\sqrt5)$ | 2 | $r^{2},c,cr^{2}$ 都固定 $\alpha^{2}=\varphi$ |
| $\langle r^{2},cr\rangle$ | 4 | $\mathbb Q(i)$ | 2 | $r^{2},cr,cr^{3}$ 都固定 $i$ |
| $\langle r^{2}\rangle$ | 2 | $\mathbb Q(i,\sqrt5)$ | 4 | $r^{2}$ 固定 $i$ 与 $\alpha^{2}$ |
| $\langle c\rangle$ | 2 | $\mathbb Q(\alpha)$ | 4 | $c$ 固定 $\alpha$；$[K:\mathbb Q(\alpha)]=2$ |
| $\langle cr\rangle$ | 2 | $\mathbb Q(i,\alpha+\frac{i}{\alpha})=\mathbb Q(i,\sqrt{1+2i})$ | 4 | $cr(u)=u$（见下） |
| $\langle cr^{2}\rangle$ | 2 | $\mathbb Q(i\alpha)$ | 4 | $cr^{2}(i\alpha)=(-i)(-\alpha)=i\alpha$ |
| $\langle cr^{3}\rangle$ | 2 | $\mathbb Q(i,\alpha-\frac{i}{\alpha})=\mathbb Q(i,\sqrt{1-2i})$ | 4 | $cr^{3}(v)=v$（见下） |
| $\{e\}$ | 1 | $K=\mathbb Q(i,\alpha)$ | 8 | — |

表中的验算举例：

- $cr(u)=(cr)(\alpha)+\dfrac{(cr)(i)}{(cr)(\alpha)}=\dfrac{i}{\alpha}+\dfrac{i}{i/\alpha}=\dfrac{i}{\alpha}+\alpha=u$；同理 $cr^{3}(v)=\dfrac{-i}{\alpha}+\dfrac{i}{-i/\alpha}=-\dfrac{i}{\alpha}+\alpha=v$。
- 反之 $r^{2}(u)=-u\ne u$，$r^{2}(v)=-v\ne v$，说明 $u\notin \mathbb Q(i,\sqrt5)$、$v\notin\mathbb Q(i,\sqrt5)$，故这两个 4 次域与 $\mathbb Q(i,\sqrt5)$ 不同。
- $\mathbb Q(i,\sqrt{1+2i})$ 与 $\mathbb Q(i,\sqrt{1-2i})$ 的确是 4 次域：$u^{2}=1+2i$，若 $u\in\mathbb Q(i)$ 则 $1+2i$ 是 $\mathbb Q(i)$ 中的平方，设 $(a+bi)^{2}=1+2i$（$a,b\in\mathbb Q$），得 $ab=1$、$a^{2}-b^{2}=1$，代入 $b=1/a$ 得 $a^{4}-a^{2}-1=0$，即 $a^{2}=\varphi\notin\mathbb Q$，矛盾。故 $[\mathbb Q(i,u):\mathbb Q]=4$。$v$ 同理。

**包含关系（偏序）。** 由 Galois 反序对应，只需读子群格：

- 三个二次域：$\mathbb Q(\sqrt5),\ \mathbb Q(i),\ \mathbb Q(\sqrt{-5})$ 都在 $\mathbb Q$ 之上、在 $K$ 之下，彼此互不包含；
- $\mathbb Q(i,\sqrt5)$（唯一 Galois 的 4 次子域，即双二次域）包含全部三个二次域；
- $\mathbb Q(\alpha)$ 只包含 $\mathbb Q(\sqrt5)$（它是实域，不含 $i$ 与 $\sqrt{-5}$）；
- $\mathbb Q(i,\sqrt{1+2i})$ 与 $\mathbb Q(i,\sqrt{1-2i})$ 都只包含 $\mathbb Q(i)$；
- $\mathbb Q(i\alpha)$ 只包含 $\mathbb Q(\sqrt5)$（因 $\varphi=-(i\alpha)^{2}$，故 $\sqrt5=2\varphi-1=-2(i\alpha)^{2}-1\in\mathbb Q(i\alpha)$；而若 $i\in\mathbb Q(i\alpha)$ 则 $\alpha=i\alpha/i\in\mathbb Q(i\alpha)$，与 $[\mathbb Q(i\alpha):\mathbb Q]=4<8$ 矛盾，故不含 $\mathbb Q(i)$）。

一致性检验（可当作自检）：$\mathbb Q(\alpha)\cap\mathbb Q(i\alpha)$ 由 Galois 对应等于 $K^{\langle c,\,cr^{2}\rangle}=K^{\langle r^{2},c\rangle}=\mathbb Q(\sqrt5)$，与上表一致。

**本题考点 / 技巧（一句话）**：算分裂域时先用「$\alpha$ 与 $i$ 分开看」定出 $[K:\mathbb Q]$，再用「8 阶子群必是 $S_4$ 的 Sylow 2-子群因而 $\cong D_4$」免去逐元素验证；子域格完全由子群格 + 不动域元素（这个题里最漂亮的三个元素是 $i,\ \sqrt5,\ i\alpha$ 与 $u=\alpha+i/\alpha$，它们满足 $u^2=1+2i$、$v^2=1-2i$、$uv=\sqrt5$）译出。

**难度**：$\boxed{3/5}$（结构不难，但要把 10 个子域全部写对、且证明它们互不相同，工作量与细心程度要求高）。

**同类题在哪几年出现过**：分裂域 + Galois 群 + 子域格是丘赛每年必考：2010 individual №4（$x^{8}-5$ 的分裂域次数与 Galois 群）、2013 team №6（$x^{4}-2$ 的域与全部子域）、2021 individual №2（$x^{3}-3x+1$ 的分裂域自同构群）、2015 team №6（$x^{5}-80x+5$，$\mathrm{Gal}\cong S_5$）、2018 team №3（$\Phi_n$ 在 $\mathbb F_p$ 上的分解）、2025 individual №5（$X^5-X+1$ 的分裂域与分歧素数）。$D_4$ 作为 Galois 群在 2016 team №3 与 2013 team №6 中出现两次。

---

### 题 6｜2017 / Algebra and Number Theory / Individual / 第 2 题

**出处行**：2017 年，Algebra and Number Theory，Individual（个人赛，5 题 100 分），Problem 2（20 分，(a) 15 分 + (b) 5 分）。

**题面（据 PDF 校正）**

> Let $A$ be a finite abelian group and let $\varphi:A\to A$ be an endomorphism. Put
> $$A_{\mathrm{nil}}:=\{x\in A\mid \varphi^{k}(x)=0\ \text{for some}\ k\ge1\}.$$
> (a) (15 points) Show that there is a subgroup $A_0$ of $A$ such that $\varphi$ restricts to an automorphism of $A_0$ and $A=A_0\oplus A_{\mathrm{nil}}$.
> (b) (5 points) Show that such a subgroup is unique.

**解答**

先把两个基本事实摆出来。

**(F1) $A_{\mathrm{nil}}$ 是子群。** 显然 $0\in A_{\mathrm{nil}}$。若 $\varphi^{k}(x)=0,\varphi^{l}(y)=0$，则 $\varphi^{\max(k,l)}(x-y)=0$，故 $A_{\mathrm{nil}}$ 对减法封闭。又 $\varphi$ 是自同态，$\varphi(A_{\mathrm{nil}})\subseteq A_{\mathrm{nil}}$。

**(F2) 链稳定。** $A$ 有限，故降链

$$A\supseteq \mathrm{im}\,\varphi\supseteq \mathrm{im}\,\varphi^{2}\supseteq\cdots$$

不能无限严格下降，存在 $K\ge0$ 使

$$\mathrm{im}\,\varphi^{K}=\mathrm{im}\,\varphi^{K+1}=\mathrm{im}\,\varphi^{K+2}=\cdots .$$

（必要时把 $K$ 取得更大，使 $A_{\mathrm{nil}}\subseteq \ker\varphi^{K}$；后者可行，因为 $\varphi|_{A_{\mathrm{nil}}}$ 幂零且 $A_{\mathrm{nil}}$ 有限，取 $k_0$ 使 $A_{\mathrm{nil}}\subseteq\ker\varphi^{k_0}$ 即可。）以下固定这样的 $K$，记 $m:=\varphi^{K}$。

**（a）第一步：$A=\mathrm{im}\,m+\ker m$。**

任取 $x\in A$。$m(x)\in\mathrm{im}\,m=\mathrm{im}\,m^{2}$，故存在 $y\in A$ 使 $m(x)=m^{2}(y)=m(m(y))$。于是

$$m\bigl(x-m(y)\bigr)=m(x)-m^{2}(y)=0,$$

即 $x-m(y)\in\ker m$，而 $m(y)\in\mathrm{im}\,m$。故 $x\in \mathrm{im}\,m+\ker m$。

**（a）第二步：$\mathrm{im}\,m\cap\ker m=0$。**

$m$ 把 $\mathrm{im}\,m=\mathrm{im}\,\varphi^{K}$ 满射到 $\mathrm{im}\,\varphi^{K+1}=\mathrm{im}\,m$ 上，即 $m|_{\mathrm{im}\,m}:\mathrm{im}\,m\to \mathrm{im}\,m$ 是**满射**。有限集上的满射即双射，故 $\ker\bigl(m|_{\mathrm{im}\,m}\bigr)=0$。若 $x\in\mathrm{im}\,m\cap\ker m$，则 $x\in\mathrm{im}\,m$ 且 $m(x)=0$，由单射性得 $x=0$。

由两步得

$$A=\mathrm{im}\,\varphi^{K}\oplus\ker\varphi^{K}.$$

**（a）第三步：识别核与幂零部分。** 按 $K$ 的取法，

$$\ker\varphi^{K}\subseteq A_{\mathrm{nil}}\subseteq\ker\varphi^{K},$$

故 $\ker\varphi^{K}=A_{\mathrm{nil}}$。于是取

$$\boxed{A_0:=\mathrm{im}\,\varphi^{K}},\qquad A=A_0\oplus A_{\mathrm{nil}}.$$

**（a）第四步：$\varphi|_{A_0}$ 是自同构。** 由链稳定，$\varphi(A_0)=\varphi(\mathrm{im}\,\varphi^{K})=\mathrm{im}\,\varphi^{K+1}=\mathrm{im}\,\varphi^{K}=A_0$，即 $\varphi$ 把 $A_0$ 满射到自身；$A_0$ 有限，故 $\varphi|_{A_0}$ 是双射，即自同构。$\blacksquare$

**（b）唯一性。** 设 $A=B\oplus C$，其中 $\varphi|_{B}$ 是自同构、$\varphi$ 在 $C$ 上幂零（即 $C\subseteq A_{\mathrm{nil}}$）。

- $B\subseteq \mathrm{im}\,\varphi^{K}=A_0$：任取 $b\in B$，因 $\varphi|_B$ 是自同构，$b=\varphi^{K}\bigl((\varphi|_B)^{-K}b\bigr)\in\mathrm{im}\,\varphi^{K}$。
- $C\subseteq A_{\mathrm{nil}}=\ker\varphi^{K}$（取 $K$ 足够大）。

于是 $B\subseteq A_0$，$C\subseteq A_{\mathrm{nil}}$。由 $A=B\oplus C=A_0\oplus A_{\mathrm{nil}}$ 得

$$|B|\cdot|C|=|A|=|A_0|\cdot|A_{\mathrm{nil}}|,$$

结合 $|B|\le|A_0|,\ |C|\le|A_{\mathrm{nil}}|$ 得 $|B|=|A_0|,\ |C|=|A_{\mathrm{nil}}|$，从而 $B=A_0,\ C=A_{\mathrm{nil}}$。故 $A_0$ 唯一。$\blacksquare$

**两点补充（加深理解）**

1. 本题就是**有限 Abel 群的 Fitting 分解**，也是「有限集上的自映射的最终周期性」在群情形下的表现：$A_0$ 是 $\varphi$ 的「可逆部分」，$A_{\mathrm{nil}}$ 是「幂零部分」。若把 $A$ 看成有限 $\mathbb Z[\varphi]$-模，则 $A_0=\varphi^{K}A$ 就是 $\varphi$ 在 $A$ 上作用为可逆的那个直和项（即 $\mathbb Z[\varphi]$ 的某个局部化作用的部分）。
2. $A_0$ 也可以刻画为 $A_{\mathrm{nil}}$ 的「补」：$A_0\cong A/A_{\mathrm{nil}}$，且 $\varphi$ 在 $A/A_{\mathrm{nil}}$ 上诱导自同构。

**本题考点 / 技巧（一句话）**：有限集上「满射 = 双射」，因此降链稳定后 $\varphi^{K}$ 在 $\mathrm{im}\,\varphi^{K}$ 上是自同构，Fitting 分解就自动成立；唯一性靠「可逆部分必落在所有 $\mathrm{im}\,\varphi^{K}$ 中、幂零部分必落在 $\ker\varphi^{K}$ 中」。

**难度**：$\boxed{3/5}$（思路完全是标准的 Fitting 引理，但要写清 $K$ 的选法与「满射即双射」这一步）。

**同类题在哪几年出现过**：Fitting 型分解在丘赛出现频率极高：2016 team №4（不可分解表示的自同态环中每个元素可逆或幂零）、2018 team №1（局部环与非分解模、Fitting 引理）、2015 individual №1（有限 Abel 群 + 交错非退化配对 $\Rightarrow$ $G\cong H_1\oplus H_2$，其中 $H_1\cong H_2$ 且各自迷向，也是一整套「逐步取极大双曲子群 + 归纳」的分解论证）、2013 team №2（$\mathrm{tr}(A^{n})\in F\ (n\ge2)\Rightarrow \mathrm{tr}(A)\in F$，用特征多项式的线性递推，思路同样是「用稳定的线性关系控制幂零/周期部分」）。另外 2023 individual №4（有限表现模的核有限生成，即 Schanuel 引理）与 2022 individual №4（每个理想 2-生成）都属于同一族「模论技术型」题目。

---

### 题 7｜2019 / Algebra and Number Theory / Individual / 第 5 题

**出处行**：2019 年，Algebra and Number Theory，Individual（个人赛，5 题），第 5 题。

**题面（据 PDF 校正）**

> The Fibonacci sequence is defined by $F_0=0,\ F_1=1,\ F_{n+2}=F_{n+1}+F_n$. Let $p$ be a prime number.
> 1. Show that if $p\equiv 1,4\pmod5$, then $p$ divides $F_{p-1}$.
> 2. Let $\mathbb F_{p^{2}}$ be the finite field of $p^{2}$ elements. Show that the norm map $N:\mathbb F_{p^{2}}^{\times}\to\mathbb F_p^{\times}$ is surjective, and deduce the cardinality of the kernel of $N$.
> 3. Show that if $p\equiv 2,3\pmod5$, then $p$ divides $F_{p+1}$.

**解答**

全题的枢纽是**有限域上的 Binet 公式**。

**Binet 公式（在任意域中，只要 $x^{2}-x-1$ 有两个不同的根 $\alpha\ne\beta$）。** 设 $R$ 是任意域，$\alpha,\beta\in R$ 是多项式 $x^{2}-x-1$ 的两个根（可能在扩域中），$\alpha\ne\beta$。则

$$\alpha+\beta=1,\qquad \alpha\beta=-1,\qquad \alpha^{2}=\alpha+1,\ \beta^{2}=\beta+1,$$

且对一切 $n\ge0$ 有

$$F_n=\frac{\alpha^{n}-\beta^{n}}{\alpha-\beta}.\qquad(\ast)$$

证明：$n=0,1$ 时右边分别为 $0,1$，正确。若 $n,n+1$ 成立，则由 $\alpha^{n+2}=\alpha^{n}(\alpha+1)=\alpha^{n+1}+\alpha^{n}$ 同理 $\beta^{n+2}=\beta^{n+1}+\beta^{n}$，两式相减除以 $\alpha-\beta$ 得 $F_{n+2}=F_{n+1}+F_n$，归纳成立（**过程中未用到 $\mathrm{char}\ne2$**，只用了 $\alpha\ne\beta$，故特征 $2$ 的情形同样适用）。$\square$

> ✅ 已按 referee_algebra.md 修正（原表述：Binet 公式限定「特征 $\ne2$ 的域」，但下文第 3 问在 $p=2$ 时仍在使用该公式）

**第 1 问：$p\equiv1,4\pmod5\Rightarrow p\mid F_{p-1}$。**

先注意 $p\equiv1,4\pmod5$ 时 $p\ne5$，且 $p$ 为奇素数（$p=2$ 时 $2\equiv2\pmod5$，不在本情形）。

由二次互反律，因 $5\equiv1\pmod4$，有 $\left(\dfrac{5}{p}\right)=\left(\dfrac{p}{5}\right)$；而模 $5$ 的平方剩余为 $\{1,4\}$，故

$$\left(\frac5p\right)=1\iff p\equiv\pm1\pmod5 .$$

于是 $5$ 是 $\mathbb F_p$ 中的平方，$\sqrt5\in\mathbb F_p$，且 $2$ 在 $\mathbb F_p$ 中可逆，故

$$\alpha=\frac{1+\sqrt5}{2},\qquad \beta=\frac{1-\sqrt5}{2}$$

都是 $\mathbb F_p$ 中的元素，并且 $\alpha\ne\beta$（$\sqrt5\ne0$）。由 $\alpha\beta=-1$ 知 $\alpha,\beta\in\mathbb F_p^{\times}$。

在 $\mathbb F_p$ 中应用 $(\ast)$，并用 Fermat 小定理 $\alpha^{p-1}=\beta^{p-1}=1$：

$$F_{p-1}\equiv\frac{\alpha^{p-1}-\beta^{p-1}}{\alpha-\beta}=\frac{1-1}{\alpha-\beta}=0\pmod p .$$

（严格说：$F_{p-1}$ 是整数，把 $(\ast)$ 在 $\mathbb F_p$ 中解读即得 $F_{p-1}\bmod p=0$。）故 $p\mid F_{p-1}$。$\blacksquare$

*数值检验*：$p=11$：$F_{10}=55=5\cdot11$；$p=19$：$F_{18}=2584=19\cdot136$；$p=29$：$F_{28}=317811=29\cdot10959$；$p=31$：$F_{30}=832040=31\cdot26840$。

**第 2 问：范数映射 $N:\mathbb F_{p^{2}}^{\times}\to\mathbb F_p^{\times}$ 满射，核的大小为 $p+1$。**

$\mathbb F_{p^{2}}/\mathbb F_p$ 是 2 次 Galois 扩张，Galois 群由 Frobenius $\sigma:x\mapsto x^{p}$ 生成，故

$$N(x)=x\cdot\sigma(x)=x\cdot x^{p}=x^{p+1}.$$

**满射性（两种等价证明，任选其一）。**

*证法 A（循环群计数）*：$\mathbb F_{p^{2}}^{\times}$ 是 $p^{2}-1$ 阶循环群，取生成元 $g$。映射 $\psi:x\mapsto x^{p+1}$ 是群同态，故 $\mathrm{Im}\,\psi=\langle g^{p+1}\rangle$，其阶为

$$|\mathrm{Im}\,\psi|=\frac{p^{2}-1}{\gcd(p^{2}-1,\,p+1)}=\frac{(p-1)(p+1)}{p+1}=p-1 .$$

而 $\mathbb F_p^{\times}\le\mathbb F_{p^{2}}^{\times}$ 是 $p-1$ 阶子群，$\mathrm{Im}\,\psi$ 也是 $p-1$ 阶子群；循环群 $\mathbb F_{p^{2}}^{\times}$ 的每个阶数的子群唯一，故 $\mathrm{Im}\,\psi=\mathbb F_p^{\times}$，即 $N$ 满射。

*证法 B（有限域范数的可除性）*：对任意 $a\in\mathbb F_p^{\times}$，多项式 $X^{p+1}-a$ 在 $\mathbb F_{p^{2}}$ 中有根（因为 $\mathbb F_{p^2}$ 是 $X^{p^2}-X$ 的分裂域、且 $X^{p+1}-a\mid X^{p^{2}}-X$：$a^{p-1}=1$ 使 $a^{p^2-1}=1$，任一满足 $x^{p+1}=a$ 的 $x$ 满足 $x^{p^2}=x^{p+1\cdot(p-1)+1}=a^{p-1}x=x$）。

**核的大小**：由同态基本定理与满射性，

$$|\ker N|=\frac{|\mathbb F_{p^{2}}^{\times}|}{|\mathbb F_p^{\times}|}=\frac{p^{2}-1}{p-1}=p+1 .$$

即 $\ker N=\{x\in\mathbb F_{p^{2}}^{\times}:x^{p+1}=1\}$ 恰有 $p+1$ 个元素。$\blacksquare$

**第 3 问：$p\equiv2,3\pmod5\Rightarrow p\mid F_{p+1}$。**

此时（$p$ 为奇素数——二次互反律的这一形式要求 $p$ 奇）$\left(\dfrac5p\right)=\left(\dfrac p5\right)=-1$，故 $5$ 不是 $\mathbb F_p$ 中的平方，从而多项式 $x^{2}-x-1$ 在 $\mathbb F_p$ 上不可约（其判别式为 $5$，非平方；特征 $\ne2$）。

> ✅ 已按 referee_algebra.md 修正（原表述：未注明 $(5/p)=(p/5)$ 只对奇素数成立；$p=2$ 的情形见下）取它在其分裂域 $\mathbb F_{p^{2}}$ 中的一个根 $\alpha$，则另一根为

$$\beta=\alpha^{p}$$

（Frobenius 把两根互换：$\alpha^{p}$ 也是 $x^{2}-x-1$ 的根，因为系数在 $\mathbb F_p$ 中；而 $\alpha^{p}\ne\alpha$，否则 $\alpha\in\mathbb F_p$，与不可约性矛盾）。于是 $\alpha,\beta\in\mathbb F_{p^{2}}$，$\alpha\ne\beta$，可以应用 $(\ast)$。

计算两个 $p+1$ 次幂：

$$\alpha^{p+1}=\alpha\cdot\alpha^{p}=\alpha\beta,\qquad \beta^{p+1}=\beta\cdot\beta^{p}=\beta\cdot\alpha\qquad(\text{因}\ \beta^{p}=(\alpha^{p})^{p}=\alpha^{p^{2}}=\alpha) .$$

两者相等，故

$$F_{p+1}\equiv\frac{\alpha^{p+1}-\beta^{p+1}}{\alpha-\beta}=0\quad\text{在}\ \mathbb F_{p^{2}}\ \text{中} ,$$

特别地 $F_{p+1}\equiv0\pmod p$，即 $p\mid F_{p+1}$。$\blacksquare$

*数值检验*：$p=2$：$F_3=2$；$p=3$：$F_4=3$；$p=7$：$F_8=21=3\cdot7$；$p=13$：$F_{14}=377=13\cdot29$；$p=17$：$F_{18}=2584=17\cdot152$；$p=23$：$F_{24}=46368=23\cdot2016$。

*关于 $p=2$*：$p=2$ 时**不能**沿用上面「$(5/p)=(p/5)=-1$ ⇒ $x^2-x-1$ 不可约」这一步——二次互反律的该形式要求 $p$ 为奇素数，而且 $(5/2)=1$、$5\equiv1$ 在 $\mathbb F_2$ 中本来就是平方，判别式判据（「判别式为平方 $\iff$ 二次多项式可约」）在特征 $2$ 也失效。正确做法是直接检验：$x^2-x-1=x^2+x+1$ 在 $\mathbb F_2$ 上取值 $1,1$ 均非零，故不可约；取根 $\alpha\in\mathbb F_4\setminus\mathbb F_2$，则 $\beta=\alpha^p=\alpha^2=\alpha+1$ 为另一根，$\alpha^{p+1}=\alpha\beta=\beta^{p+1}$，于是 $F_3=(\alpha^3-\beta^3)/(\alpha-\beta)=0$ 于 $\mathbb F_4$，即 $2\mid F_3$。第 1 问中 $p=2$ 不出现（$2\equiv2\bmod5$），无碍。

> ✅ 已按 referee_algebra.md 修正（原表述：「上面的论证照旧成立」——对 $p=2$ 不成立：二次互反律该形式要求 $p$ 奇，且 $(5/2)=1$）

**顺带的收获**：$p\mid F_{p-1}$（当 $p\equiv\pm1\bmod5$）与 $p\mid F_{p+1}$（当 $p\equiv\pm2\bmod5$）合起来给出「对任意素数 $p\ne5$，$p$ 整除 $F_{p-(5/p)}$」；而 $5\mid F_5=5$。这正是 Fibonacci 数列模 $p$ 的 Pisano 周期整除 $p-1$ 或 $2(p+1)$ 的前身。

**本题考点 / 技巧（一句话）**：把递推数列写成「特征根幂之差除以根差」，再让特征根活在合适大小的有限域里，用 Frobenius/ Fermat 让幂次归 $1$；范数满射则是「$\mathbb F_{p^n}^{\times}$ 循环 + 指数映射计数」的模板题。

**难度**：$\boxed{3/5}$（Binet 公式本身不稀奇，关键是意识到 $\sqrt5$ 是否落入 $\mathbb F_p$ 由二次互反律决定，以及第 3 问要跳到 $\mathbb F_{p^2}$）。

**同类题在哪几年出现过**：Fibonacci 本题在 150 道代数题中**只出现这一次**，但「有限域 + 二次互反 + 特征和」的家族很大：2019 team №4（$\mathbb F_p$ 上的 Gauss 和、$g_p^2=(-1)^{(p-1)/2}p$、$\mathbb Q(\zeta_p)$ 的唯一二次子域）、2026 individual №2（椭圆曲线 $y^2=x^3+1$ 上的点计数与 Jacobi 和）、2012 individual №2（$\mathrm{GL}_n(\mathbb F_p)$ 的计数）、2017 team №4（$\mathbb F_p(T)$ 上 $X^p-TX-T$ 与 $X^{p-1}-T$ 的分裂域）、2013 individual №3 与 2013 team №5（$\mathbb F_5,\mathbb F_2$ 上多项式的计数）。2018 individual №1（Mersenne/Fermat 素数的初等判别）也是同一种「初等数论 + 模运算」的风格。


---

### 题 8｜2022 / Algebra and Number Theory / Individual / 第 5 题

**出处行**：2022 年，Algebra and Number Theory，Individual（个人赛，「Solve every problem」，6 题），Problem 5。

**题面（据 PDF 校正）**

> Let $p$ be a prime number and $\zeta_p$ be a primitive $p$-th root of unity. Let $K=\mathbf Q(\zeta_p)$.
> (a) Show that $\Phi_p=\sum_{i=0}^{p-1}X^{i}$ is the minimal polynomial of $\zeta_p$ over $\mathbf Q$.
> (b) Compute the trace $\mathrm{Tr}_{K/\mathbf Q}(1-\zeta_p)$ and the norm $\mathcal N_{K/\mathbf Q}(1-\zeta_p)$.
> (c) Show that $(1-\zeta_p)\mathcal O_K\cap\mathbf Z=p\mathbf Z$ and deduce that for all $y\in\mathcal O_K$, we have $\mathrm{Tr}_{K/\mathbf Q}\bigl(y(1-\zeta_p)\bigr)\in p\mathbf Z$.
> (d) Determine explicitly the ring of integers of $K$.

以下设 $p$ 为奇素数（$p=2$ 时 $K=\mathbf Q,\ \mathcal O_K=\mathbf Z=\mathbf Z[\zeta_2]$，$1-\zeta_2=2$，$\mathrm{Tr}=2,\ \mathcal N=2$，结论平凡）。记 $\zeta=\zeta_p$。

**解答 (a)：$\Phi_p$ 是极小多项式**

令 $Y=X-1$，并把 $X=Y+1$ 代入 $\Phi_p(X)=\dfrac{X^{p}-1}{X-1}$（$X\ne1$，作为多项式恒等式成立）：

$$\Phi_p(Y+1)=\frac{(Y+1)^{p}-1}{Y}=\sum_{k=0}^{p-1}\binom{p}{k+1}Y^{k}=Y^{p-1}+\binom{p}{p-1}Y^{p-2}+\cdots+\binom{p}{2}Y+\binom{p}{1}.$$

即

$$\Phi_p(Y+1)=Y^{p-1}+pY^{p-2}+\binom p2Y^{p-3}+\cdots+\binom{p}{p-2}Y+p .$$

对 $1\le j\le p-1$，$\dbinom{p}{j}=\dfrac{p(p-1)\cdots(p-j+1)}{j!}$ 被 $p$ 整除（分母 $j!$ 与 $p$ 互素，故 $\dbinom pj$ 是 $p$ 的倍数）。于是：

- 首项系数 $1$ 不被 $p$ 整除；
- 其余系数 $\dbinom{p}{p-1},\dots,\dbinom{p}{2},\dbinom{p}{1}=p$ 都被 $p$ 整除；
- 常数项 $\dbinom{p}{1}=p$ 不被 $p^{2}$ 整除。

由 **Eisenstein 判别法**，$\Phi_p(Y+1)$ 在 $\mathbf Q[Y]$ 中不可约。代换 $Y\mapsto X-1$（它是 $\mathbf Q[X]$ 的自同构）保持不可约性，故 $\Phi_p(X)$ 在 $\mathbf Q[X]$ 中不可约。

又 $\Phi_p(\zeta)=\dfrac{\zeta^{p}-1}{\zeta-1}=0$，且 $\Phi_p$ 首一、不可约、以 $\zeta$ 为根，故它就是 $\zeta$ 在 $\mathbf Q$ 上的极小多项式，于是

$$[K:\mathbf Q]=\deg\Phi_p=p-1 .\qquad\blacksquare$$

（同时得到 $\mathrm{Gal}(K/\mathbf Q)=\{\sigma_a:\zeta\mapsto\zeta^{a},\ a\in(\mathbf Z/p\mathbf Z)^{\times}\}\cong(\mathbf Z/p\mathbf Z)^{\times}\cong\mathbf Z/(p-1)\mathbf Z$：因为 $K$ 是 $\Phi_p$ 的分裂域，且上述 $p-1$ 个映射都是 $K$ 的自同构。）

**解答 (b)：迹与范**

$1-\zeta$ 的共轭元为 $\{\sigma_a(1-\zeta)=1-\zeta^{a}:a=1,\dots,p-1\}$（$a$ 取遍 $(\mathbf Z/p)^{\times}$，$\zeta^{a}$ 取遍全部本原 $p$ 次单位根）。

**迹：**

$$\mathrm{Tr}_{K/\mathbf Q}(1-\zeta)=\sum_{a=1}^{p-1}(1-\zeta^{a})=(p-1)-\sum_{a=1}^{p-1}\zeta^{a} .$$

由 $1+\zeta+\cdots+\zeta^{p-1}=0$ 得 $\sum_{a=1}^{p-1}\zeta^{a}=-1$，于是

$$\boxed{\ \mathrm{Tr}_{K/\mathbf Q}(1-\zeta_p)=p-1+1=p\ }$$

**范：**

$$\mathcal N_{K/\mathbf Q}(1-\zeta)=\prod_{a=1}^{p-1}(1-\zeta^{a})=\Phi_p(1),$$

> ✅ 已按 referee_algebra.md 修正（原表述：连等式把同一个 $\prod_{a=1}^{p-1}(1-\zeta^{a})$ 写了两遍）

最后一步用了 $\Phi_p(X)=\prod_{a=1}^{p-1}(X-\zeta^{a})$（$\Phi_p$ 的根恰为全部本原 $p$ 次单位根）。代入 $X=1$：

$$\boxed{\ \mathcal N_{K/\mathbf Q}(1-\zeta_p)=\Phi_p(1)=1+1+\cdots+1=p\ }\qquad\blacksquare$$

**解答 (c)：$(1-\zeta)\mathcal O_K\cap\mathbf Z=p\mathbf Z$，以及迹的整除性**

**第一步：$p\in(1-\zeta)$。** 由 $\Phi_p(1)=\prod_{a=1}^{p-1}(1-\zeta^{a})=p$，而对每个 $a$，

$$1-\zeta^{a}=(1-\zeta)(1+\zeta+\cdots+\zeta^{a-1})\in(1-\zeta)\mathcal O_K ,$$

故 $p$ 是 $1-\zeta$ 的倍元：$p\in(1-\zeta)\mathcal O_K$。

**第二步：交是 $p\mathbf Z$。** $(1-\zeta)\mathcal O_K\cap\mathbf Z$ 是 $\mathbf Z$ 的理想，且含 $p\mathbf Z$，故它等于 $p\mathbf Z$ 或 $\mathbf Z$。若等于 $\mathbf Z$，则 $1\in(1-\zeta)\mathcal O_K$，即 $1-\zeta$ 是 $\mathcal O_K$ 中的单位，于是 $\mathcal N_{K/\mathbf Q}(1-\zeta)=\pm1$；但 (b) 给出 $\mathcal N(1-\zeta)=p\ne\pm1$，矛盾。故

$$\boxed{\ (1-\zeta)\mathcal O_K\cap\mathbf Z=p\mathbf Z\ }$$

**第三步：对任意 $y\in\mathcal O_K$ 有 $\mathrm{Tr}(y(1-\zeta))\in p\mathbf Z$。** 置 $z:=y(1-\zeta)\in(1-\zeta)\mathcal O_K$。

- $z$ 是代数整数（$y$ 与 $1-\zeta$ 都是），故 $\mathrm{Tr}_{K/\mathbf Q}(z)$ 是代数整数；同时它是有理数，故 $\mathrm{Tr}(z)\in\mathcal O_K\cap\mathbf Q=\mathbf Z$。
- 对每个 $a$，$\sigma_a(z)=\sigma_a(y)\cdot\sigma_a(1-\zeta)=\sigma_a(y)(1-\zeta^{a})\in(1-\zeta)\mathcal O_K$（用第一步的分解），故 $\mathrm{Tr}(z)=\sum_{a}\sigma_a(z)\in(1-\zeta)\mathcal O_K$。

于是 $\mathrm{Tr}(z)\in(1-\zeta)\mathcal O_K\cap\mathbf Z=p\mathbf Z$，即 $\boxed{\mathrm{Tr}_{K/\mathbf Q}\bigl(y(1-\zeta_p)\bigr)\in p\mathbf Z}$。$\blacksquare$

*（等价说法：$(1-\zeta)\mathcal O_K$ 是 $p$ 之上的素理想，$(p)=(1-\zeta)^{p-1}$，即 $p$ 在 $K$ 中完全分歧、剩余次数为 $1$，$\mathcal O_K/(1-\zeta)\cong\mathbf F_p$；上面第三步正是「乘上 $1-\zeta$ 的迹落在 $p\mathbf Z$」这一事实。）*

**解答 (d)：$\mathcal O_K=\mathbf Z[\zeta_p]$**

**第一步：判别式。** 记 $\mathrm{disc}\bigl(1,\zeta,\dots,\zeta^{p-2}\bigr)=\mathrm{disc}(\Phi_p)$。由恒等式 $(X-1)\Phi_p(X)=X^{p}-1$ 求导：

$$\Phi_p(X)+(X-1)\Phi_p'(X)=pX^{p-1}.$$

代入 $X=\zeta$（$\Phi_p(\zeta)=0$）：$(\zeta-1)\Phi_p'(\zeta)=p\zeta^{p-1}=p\zeta^{-1}$。取范数（$\mathcal N$ 在 $K$ 上是从 $K^{\times}$ 到 $\mathbf Q^{\times}$ 的群同态）：

$$\mathcal N(\zeta-1)\cdot\mathcal N\bigl(\Phi_p'(\zeta)\bigr)=p^{p-1}\cdot\mathcal N(\zeta^{-1})=p^{p-1}.$$

而 $\mathcal N(\zeta-1)=(-1)^{p-1}\mathcal N(1-\zeta)=p$（$p$ 为奇数），故

$$\mathcal N\bigl(\Phi_p'(\zeta)\bigr)=p^{p-2},\qquad \bigl|\mathrm{disc}(\Phi_p)\bigr|=\bigl|\mathcal N(\Phi_p'(\zeta))\bigr|=p^{p-2}.$$

即 $\mathrm{disc}\bigl(1,\zeta,\dots,\zeta^{p-2}\bigr)=\pm p^{p-2}$。

**第二步：指数只能是 $p$ 的幂。** 设 $f:=\bigl[\mathcal O_K:\mathbf Z[\zeta]\bigr]$（有限，因为 $1,\zeta,\dots,\zeta^{p-2}$ 是 $K$ 的一组 $\mathbf Q$-基，$\mathcal O_K\supseteq\mathbf Z[\zeta]$）。由判别式与指数的关系

$$\mathrm{disc}\bigl(1,\zeta,\dots,\zeta^{p-2}\bigr)=f^{2}\cdot d_K,\qquad d_K\in\mathbf Z\setminus\{0\}\ \text{是}\ K\ \text{的域判别式},$$

得 $f^{2}\mid p^{p-2}$，故 $f=p^{j}$（$j\ge0$）。

**第三步：反证。** 设 $j\ge1$。因 $\mathcal O_K/\mathbf Z[\zeta]$ 是 $p^{j}$ 阶有限 Abel 群（$p$-群），由 Cauchy 定理存在 $\alpha\in\mathcal O_K\setminus\mathbf Z[\zeta]$ 使

$$p\alpha=:\gamma\in\mathbf Z[\zeta],\qquad \gamma\notin p\mathbf Z[\zeta] .$$

（$\gamma\notin p\mathbf Z[\zeta]$ 的理由：若 $\gamma=p\beta$ 且 $\beta\in\mathbf Z[\zeta]$，则 $p\alpha=p\beta$，由 $\mathcal O_K$ 无挠得 $\alpha=\beta\in\mathbf Z[\zeta]$，与 $\alpha\in\mathcal O_K\setminus\mathbf Z[\zeta]$ 矛盾。）

> ✅ 已按 referee_algebra.md 修正（原表述：直接断言 $\gamma\notin p\mathbf Z[\zeta]$，未给理由）

把 $\gamma$ 的系数模 $p$ 归约：$\gamma\equiv\sum_{i=0}^{p-2}a_i\zeta^{i}\pmod{p\mathbf Z[\zeta]}$，其中 $a_i\in\{0,1,\dots,p-1\}$，且（因 $\gamma\notin p\mathbf Z[\zeta]$）某个 $a_i\ne0$。取最小的 $i_0$ 使 $a_{i_0}\ne0$，并把 $\alpha$ 替换为 $\zeta^{-i_0}\alpha$（$\zeta$ 是 $\mathcal O_K$ 中的单位，$\zeta^{-i_0}\alpha\in\mathcal O_K\setminus\mathbf Z[\zeta]$ 仍然成立）。于是可设

$$\gamma=\sum_{i=0}^{p-2}a_i\zeta^{i},\qquad a_i\in\{0,1,\dots,p-1\},\qquad a_0\ne0,\qquad p\alpha=\gamma .$$

**第四步：用迹导出矛盾。** 记 $S:=\sum_{i=0}^{p-2}a_i$。先算两个迹：由 (a) 的 Galois 群，对 $1\le k\le p-1$ 有

$$\mathrm{Tr}_{K/\mathbf Q}(\zeta^{k})=\sum_{a=1}^{p-1}\zeta^{ak}=\sum_{b=1}^{p-1}\zeta^{b}=-1,\qquad \mathrm{Tr}_{K/\mathbf Q}(1)=p-1 .$$

于是

$$\mathrm{Tr}(\gamma)=a_0(p-1)+\sum_{i=1}^{p-2}a_i\cdot(-1)=a_0p-S,$$

（其中用了 $\sum_{i=1}^{p-2}a_i=S-a_0$）；而 $1\le i+1\le p-1$ 对 $0\le i\le p-2$ 恒成立，故

$$\mathrm{Tr}(\gamma\zeta)=\sum_{i=0}^{p-2}a_i\,\mathrm{Tr}(\zeta^{i+1})=\sum_{i=0}^{p-2}a_i\cdot(-1)=-S .$$

相减：

$$\mathrm{Tr}\bigl(\gamma(1-\zeta)\bigr)=\mathrm{Tr}(\gamma)-\mathrm{Tr}(\gamma\zeta)=(a_0p-S)-(-S)=a_0p .$$

由迹的 $\mathbf Q$-线性性（$\gamma=p\alpha$）：

$$\mathrm{Tr}\bigl(\alpha(1-\zeta)\bigr)=\frac1p\,\mathrm{Tr}\bigl(\gamma(1-\zeta)\bigr)=a_0 .$$

但 $\alpha(1-\zeta)\in\mathcal O_K$，由 (c) 应有 $\mathrm{Tr}\bigl(\alpha(1-\zeta)\bigr)\in p\mathbf Z$；而 $1\le a_0\le p-1$，$a_0\notin p\mathbf Z$。矛盾。故 $j=0$，即 $f=1$，

$$\boxed{\ \mathcal O_K=\mathbf Z[\zeta_p],\quad\text{且}\ 1,\zeta_p,\dots,\zeta_p^{p-2}\ \text{是一组整基}\ }\qquad\blacksquare$$

**本题考点 / 技巧（一句话）**：分圆域是「Eisenstein $\Rightarrow$ 极小多项式 $\Rightarrow$ 迹 = 系数和、范 = $\Phi_p(1)$ $\Rightarrow$ $(1-\zeta)\cap\mathbf Z=p\mathbf Z$ $\Rightarrow$ 用迹的整除性把指数压成 $1$」这一条链；其中 (c) 的迹整除性正是 (d) 中「反证」步骤的关键，题的内部结构是环环相扣的。

**难度**：$\boxed{4/5}$（每一步都是标准动作，但 (d) 的证明需要同时掌握「判别式与指数的关系」「Cauchy 定理取 $p$ 阶元」「迹的 $\mathbf Q$-线性性」三件事并串起来）。

**同类题在哪几年出现过**：分圆域与分圆多项式：2018 team №3（$\Phi_n$ 在 $\mathbb F_p$ 上根的刻画）、2024 individual №6（$\Phi_n$ 在 $\mathbb F_q$ 上分解为 $\varphi(n)/d$ 个 $d$ 次不可约因式，$d=$ $q$ 在 $(\mathbf Z/n)^{\times}$ 中的阶；并对 $n=2^{r}+1$、$p\equiv-3\bmod8$ 讨论 $p\mathcal O_K$ 的分解与最短向量）、2019 team №4（$\mathbf Q(\zeta_p)$ 的 Galois 群、唯一二次子域与 Gauss 和、$|g_p|^2=p$）、2020 individual №4（$\Phi_\ell$ 的不可约性与模 $p$ 分解、$p$ 在 $\mathbb F_\ell$ 中的阶与 $\mathrm{GL}_m(\mathbb F_p)$ 的关系）、2015 team №3（$\zeta=1+N\eta$，$N\ge3$，$\eta$ 代数整数 $\Rightarrow\zeta=1$，用的正是 $\mathcal N(1-\zeta)$ 只能为 $\pm p$ 或 $1$ 这一事实）。**特别提示：2015 team №3 与本题 (b) 是同一个事实的两种用法，值得对照阅读。**

---

### 题 9｜2014 / Algebra and Number Theory / Individual / 第 3 题

**出处行**：2014 年，Algebra and Number Theory，Individual（个人赛，6 题），Problem 3（(a) 5 分 + (b) 7 分 + (c) 8 分）。

**题面（据 PDF 校正）**

> Consider the equations $X^{2}-82Y^{2}=\pm2$.
> (a) (5 points) Show that if $(x,y)$ is a solution for $X^{2}-82Y^{2}=\pm2$, then $(9x-82y,\ x-9y)$ is a solution for $X^{2}-82Y^{2}=\mp2$.
> (b) (7 points) Show that the equations have solutions over $\mathbf Z/p^{n}\mathbf Z$ for any $n$ and odd prime $p$.
> (c) (8 points) Show that the equations have no solutions over $\mathbf Z$.

**解答 (a)：一个「换号」映射**

直接展开：

$$(9x-82y)^{2}=81x^{2}-2\cdot9\cdot82\,xy+82^{2}y^{2}=81x^{2}-1476xy+6724y^{2},$$
$$82(x-9y)^{2}=82x^{2}-2\cdot82\cdot9\,xy+82\cdot81y^{2}=82x^{2}-1476xy+6642y^{2}.$$

相减：

$$(9x-82y)^{2}-82(x-9y)^{2}=(81-82)x^{2}+(6724-6642)y^{2}=-x^{2}+82y^{2}=-(x^{2}-82y^{2}).$$

故若 $x^{2}-82y^{2}=\pm2$，则 $(9x-82y)^{2}-82(x-9y)^{2}=\mp2$，即 $(9x-82y,\ x-9y)$ 是 $X^{2}-82Y^{2}=\mp2$ 的解。$\blacksquare$

**结构性理解**：在实二次域 $\mathbf Q(\sqrt{82})$ 中，$9+\sqrt{82}$ 的范数为 $9^{2}-82=-1$，是一个**范 $-1$ 的单位**。映射 $(x,y)\mapsto(9x-82y,\ x-9y)$ 对应的正是把 $x+y\sqrt{82}$ 乘以共轭单位 $9-\sqrt{82}$（范 $-1$）后再取共轭，因此它翻转范数的符号；并且

$$T(x,y):=(9x-82y,\ x-9y)\ \Longrightarrow\ T^{2}=-\mathrm{id},$$

即 $T$ 是一个「$\pm$ 对换」的对合（这一点在 (c) 的递降中会用到：$T$ 与 $(-x,-y)$ 都保持方程，因而可以自由地把解规范化到 $y>0$）。

**解答 (b)：模 $p^{n}$ 可解（$p$ 为奇素数，$n\ge1$）**

**第一步：模 $p$ 可解。**

设 $p$ 为奇素数，记 $d=82$。

*情形 1：$p=41$。* 此时 $d\equiv0\pmod{41}$。因 $41\equiv1\pmod8$，由 Legendre 符号的补充律 $\left(\dfrac2{41}\right)=1$，即存在 $x_0$ 使 $x_0^{2}\equiv2\pmod{41}$。取 $(x,y)=(x_0,0)$ 得 $x^{2}-82y^{2}\equiv2$，即 $X^{2}-82Y^{2}=2$ 在模 $41$ 下可解，且解是本原的（$x_0\not\equiv0$）。

*情形 2：$p\ne2,41$。* 此时 $d=82\not\equiv0\pmod p$，且 $a:=2\ne0\pmod p$。我们数一数同余方程

$$x^{2}-d\,y^{2}\equiv a\pmod p\qquad(\ast)$$

的解数 $N_a$。

- 若 $d$ 是模 $p$ 的平方，$d=r^{2}$（$r\ne0$）：作可逆线性代换 $u=x-ry,\ v=x+ry$（变换矩阵 $\begin{pmatrix}1&-r\\1&r\end{pmatrix}$ 的行列式 $2r\ne0$，因 $p$ 奇），它是 $\mathbb F_p^{2}$ 的双射，且 $x^{2}-dy^{2}=uv$。于是 $N_a=\#\{(u,v):uv=a\}=p-1$。
- 若 $d$ 是模 $p$ 的非平方：则 $X^{2}-d$ 在 $\mathbb F_p$ 上不可约，$\mathbb F_{p^{2}}=\mathbb F_p[\sqrt d]$，而 $x^{2}-dy^{2}=N_{\mathbb F_{p^{2}}/\mathbb F_p}(x+y\sqrt d)$。由题 7 第 2 问（对任意素数 $p$ 成立的范数满射 + 核的大小 $p+1$），$N_a=p+1$。

两种情形都有 $N_a\ge p-1\ge2>1$（$p\ge3$）。而 $x\equiv y\equiv0\pmod p$ 至多给出 $1$ 个「非本原」解，故 $(\ast)$ 至少有一个**本原解** $(x_0,y_0)$（即 $p\nmid x_0$ 或 $p\nmid y_0$）。

**第二步：Hensel 提升。**

记 $F(X,Y)=X^{2}-82Y^{2}-a\in\mathbf Z_p[X,Y]$（这里 $a=\pm2$，取定符号：情形 1 取 $a=2$；情形 2 中 $a=2$ 已可解）。设 $(x_0,y_0)$ 是本原解，则

$$\frac{\partial F}{\partial X}=2X,\qquad \frac{\partial F}{\partial Y}=-164Y .$$

若 $p\nmid x_0$，则 $\dfrac{\partial F}{\partial X}(x_0,y_0)=2x_0\not\equiv0\pmod p$（$p$ 奇）；若 $p\mid x_0$，则由 $x_0^{2}-82y_0^{2}\equiv a\not\equiv0$ 得 $p\nmid y_0$，于是 $\dfrac{\partial F}{\partial Y}(x_0,y_0)=-164y_0\not\equiv0\pmod p$。两种情形都有某个偏导数在 $(x_0,y_0)$ 处是 $p$-进单位。

**多元 Hensel 引理（单根形式）**：设 $F\in\mathbf Z_p[X,Y]$，$(x_0,y_0)\in\mathbf Z_p^{2}$ 满足 $F(x_0,y_0)\equiv0\pmod p$，且某个 $\partial F/\partial X_i$ 在 $(x_0,y_0)$ 处的值是 $\mathbf Z_p$ 中的单位。则对一切 $n\ge1$，存在 $(x_n,y_n)\equiv(x_0,y_0)\pmod p$ 使 $F(x_n,y_n)\equiv0\pmod{p^{n}}$。

（证明即 Newton 迭代：若 $F(x,y)\equiv0\bmod p^{k}$ 且 $F_{X}(x,y)$ 为单位，置 $x'=x-F(x,y)/F_X(x,y)$ 得 $F(x',y)\equiv0\bmod p^{2k}$；若 $F_X$ 非单位而 $F_Y$ 是单位，对 $y$ 做同样的修正。迭代收敛于 $\mathbf Z_p$ 中的解，逐步取截断即得每个 $n$ 的模 $p^n$ 解。）

因此对每个 $n$，$X^{2}-82Y^{2}\equiv a\pmod{p^{n}}$（即 $X^{2}-82Y^{2}=\pm2$ 之一）在 $\mathbf Z/p^{n}\mathbf Z$ 中有解。特别地两个方程在模 $p^{n}$ 下都可解：情形 2 中 $a=2$ 与 $a=-2$ 都可解（$N_2=N_{-2}\ge2$），情形 1 中 $2$ 可解、且因 $41\equiv1\bmod4$ 使 $-1$ 是平方、从而 $-2$ 也是平方，故 $a=-2$（取 $y=0$）可解。$\blacksquare$

*（补充，非原题要求）*：$p=2$ 时结论同样成立。事实上 $(x,y)=\left(\dfrac{10}{3},\dfrac13\right)$ 满足

$$\left(\frac{10}{3}\right)^{2}-82\left(\frac13\right)^{2}=\frac{100-82}{9}=2 ,$$

而 $3$ 是 $2$-进单位，故 $(10/3,1/3)\in\mathbf Z_2^{2}$ 是 $X^{2}-82Y^{2}=2$ 的一个真正的 $\mathbf Z_2$ 解。于是 $X^{2}-82Y^{2}=\pm2$ 在 $\mathbf Z_p$（$p$ 任意，含 $p=2$）以及 $\mathbf R$ 中都有解，却在 $\mathbf Z$ 中无解——这正是 (c) 要证的。

**解答 (c)：$\mathbf Z$ 上无解（无穷递降）**

**准备。** 设 $(x,y)\in\mathbf Z^{2}$ 满足 $x^{2}-82y^{2}=\pm2$。

1. $y\ne0$：若 $y=0$ 则 $x^{2}=\pm2$，无整数解。
2. $x\ne0$：若 $x=0$ 则 $-82y^{2}=\pm2$，即 $y^{2}=\mp\dfrac1{41}$，无整数解。
3. 若 $(x,y)$ 是解，则 $(-x,-y)$ 也是同符号方程的解（$(-x)^{2}-82(-y)^{2}=x^{2}-82y^{2}$）。故可**约定 $y>0$**。
4. 由 $x^{2}=82y^{2}\pm2$ 得

$$x^{2}\ge 82y^{2}-2>81y^{2}\quad(\text{当}\ y\ge2),\qquad x^{2}<82y^{2}+2<100y^{2}\quad(\text{当}\ y\ge1).$$

而 $y=1$ 时 $x^{2}=82\pm2\in\{80,84\}$ 都不是完全平方，故只能 $y\ge2$。于是

$$81y^{2}<x^{2}<100y^{2}\ \Longrightarrow\ 9y<|x|<10y .$$

**反证。** 假设解集非空，取其中一个使 $|y|$ 最小者；由第 3 条可设 $y>0$。由上一条，$9y<|x|<10y$，于是 $x\ne\pm9y$。

- **若 $x>0$**：则 $x\in(9y,10y)$。令
  $$(x_1,y_1):=(9x-82y,\ x-9y).$$
  由 (a)，$x_1^{2}-82y_1^{2}=\mp2$，即 $(x_1,y_1)$ 仍是解；并且
  $$y_1=x-9y\in(0,y)\ \Longrightarrow\ 0<|y_1|<y .$$
- **若 $x<0$**：则 $x\in(-10y,-9y)$。改用另一个「换号」映射
  $$T'(x,y):=(9x+82y,\ x+9y),$$
  它与 (a) 中的 $T$ 有完全相同的性质：直接展开
  $$(9x+82y)^{2}-82(x+9y)^{2}=(81-82)x^{2}+(82^{2}-82\cdot81)y^{2}=-x^{2}+82y^{2},$$
  故 $(x_1,y_1):=T'(x,y)$ 仍是 $X^{2}-82Y^{2}=\mp2$ 的解，且
  $$y_1=x+9y\in(-y,0)\ \Longrightarrow\ 0<|y_1|<y .$$

两种情形都得到了一个新解 $(x_1,y_1)$ 满足 $0<|y_1|<|y|$，与 $(x,y)$ 的 $|y|$ 最小性矛盾。

因此解集为空，即 $X^{2}-82Y^{2}=\pm2$ **在 $\mathbf Z$ 中无解**。$\blacksquare$

**本题考点 / 技巧（一句话）**：二次域中的范 $-1$ 单位 $9+\sqrt{82}$ 给出一个「把解搬到 $y$ 更小的解」的递降算子（乘共轭单位再取共轭），配合 $(\pm x,\pm y)$ 的符号规范化，就得到无穷递降；而局部可解性则是「二次型在 $\mathbb F_p$ 上的解数 $=p-1$ 或 $p+1$」加 Hensel 的标准两连击。

**难度**：$\boxed{4/5}$（(a)(b) 是常规操作；(c) 的关键在于意识到 $9^{2}-82=-1$、从而用一个单位来「缩小」解，并且要处理 $x<0$ 的分支）。

**同类题在哪几年出现过**：Pell 型/二次型方程的整数解在丘赛代数卷中较少（150 题里只有 2014 individual №2、№3 两道），因此本题具有代表性。但「局部可解 $\ne$ 整体可解」的精神在后继年份反复出现：2014 team №6（$x^{3}+cy^{3}+c^{2}z^{3}-3cxyz=1$ 的整数解个数，当 $c$ 是立方时为有限、否则无限，本质是三次域上范数方程的分析）、2018 individual №2（$K=\mathbf Q(\sqrt[3]5)$ 的 Galois 闭包上的素理想分解律：$p\equiv1\bmod3$ 且 $5$ 为三次剩余时完全分裂，否则惯性次数为 3，$p\equiv2\bmod3$ 时 $5$ 必为三次剩余且 $f_p=2$）、2025 individual №5（$X^{5}-X+1$ 的分歧素数判定）、2026 individual №4（$K=\mathbf Q(\sqrt[3]a)$ 的整基在 $a\equiv\pm1\bmod9$ 时的修正）。做 2014 №3 是为这些「分解律 / 整基 / 素理想分解」题目打底。

---

### 题 10｜2026 / Algebra and Number Theory / Individual / 第 2 题

**出处行**：2026 年，Algebra and Number Theory，Individual（个人赛），第 2 题。
**题面标注：原文**（说明：本地 PDF 归档 `F:\丘成桐大学生数学竞赛历年笔试真题\` 只到 2025 年，没有 2026 年的试卷文件，因此本题题面取自 `problems_full.json` 的抽取文本，**未做 PDF 复核**；好在题面自足，所需外部事实（$|J(\chi,\mu)|=\sqrt p$）已在题面中给出。）

**题面（原文，清理后）**

> Let $p$ be a prime, and let $\mathbb F_p$ denote the field of $p$ elements. Consider the equation $Y^{2}=X^{3}+1$ over $\mathbb F_p$, and denote by $N_p$ its number of solutions in $\mathbb F_p$: $N_p:=\#\{(x,y)\in\mathbb F_p^{2}\mid y^{2}=x^{3}+1\}$. In the following we want to show $|N_p-p|\le2\sqrt p$.
> For $m\in\mathbf Z_{\ge1}$, let $X_m=X_m(\mathbb F_p^{\times})$ be the group of (complex) characters of $\mathbb F_p^{\times}$ of order dividing $m$. For $\chi$ a character of $\mathbb F_p^{\times}$, set $\chi(0)=1$ if $\chi=1$ and $\chi(0)=0$ otherwise. For $\chi,\mu$ two characters of $\mathbb F_p^{\times}$, write $J(\chi,\mu)$ the Jacobi sum attached to them:
> $$J(\chi,\mu):=\sum_{a+b=1}\chi(a)\mu(b)\in\mathbf C .$$
> Recall that $|J(\chi,\mu)|=\sqrt p$ if the characters $\chi$, $\mu$ and $\chi\mu$ are all non-trivial.
> (1) Assume $p=3$ or $p\equiv2\pmod3$. Show that $N_p=p$, and thus $|N_p-p|\le2\sqrt p$ in this case.
> (2) Assume $p\equiv1\pmod m$. Let $a\in\mathbb F_p$. Write $N(X^{m}=a)$ for the number of solutions of $X^{m}=a$. Show that $N(X^{m}=a)=\sum_{\chi\in X_m}\chi(a)$.
> (3) Suppose $p\equiv1\pmod3$. Show that we still have $|N_p-p|\le2\sqrt p$.

**解答**

以下约定：$\chi_2$ 表示 $\mathbb F_p^{\times}$ 的二次特征（Legendre 符号），按题面约定延拓到 $0$：$\chi_2(0)=0$；$\mathbf 1$ 表示平凡特征。记 $\zeta_3=e^{2\pi i/3}$。

**第 (2) 问（先做，它是后面计数的工具）**

设 $p\equiv1\pmod m$，$N=p-1$，$a\in\mathbb F_p$。

**情形 $a=0$：** $X^{m}=0$ 只有解 $x=0$，故 $N(X^{m}=0)=1$。另一方面 $\sum_{\chi\in X_m}\chi(0)=1+\underbrace{0+\cdots+0}_{\text{非平凡}\ \chi}=1$。等式成立。

**情形 $a\ne0$：** 取 $\mathbb F_p^{\times}$ 的生成元 $g$，写 $a=g^{s}$。方程 $x^{m}=a$ 的解集（若非空）是陪集 $x_0\cdot\ker(\cdot)^{m}$，其中 $(\cdot)^{m}:\mathbb F_p^{\times}\to\mathbb F_p^{\times}$ 是 $m$ 次幂映射。因 $m\mid p-1$，在循环群 $\mathbb F_p^{\times}$ 中

$$|\ker(\cdot)^{m}|=\gcd(m,\,p-1)=m,\qquad |\mathrm{im}(\cdot)^{m}|=\frac{p-1}{m},\qquad \mathrm{im}(\cdot)^{m}=\{g^{mj}\}=\langle g^{m}\rangle .$$

故

$$N(X^{m}=a)=\begin{cases}m,& a\in\langle g^{m}\rangle,\\ 0,& a\notin\langle g^{m}\rangle .\end{cases}$$

另一方面，$X_m$ 是 $m$ 阶循环群（生成元 $\chi_0(g)=\zeta_m$），且

$$\chi\in X_m\iff \chi^{m}=1\iff \chi\ \text{在}\ \langle g^{m}\rangle\ \text{上为}\ 1 .$$

由特征的正交关系（严格说，是把它用在商群 $G/\bigcap_{\chi\in X_m}\ker\chi$ 上——该商群的特征群恰为 $X_m$；$X_m$ 本身一般不是 $G$ 的全体特征）：

$$\sum_{\chi\in X_m}\chi(a)=\begin{cases}m,& \chi(a)=1\ \text{对一切}\ \chi\in X_m,\\ 0,& \text{否则},\end{cases}$$

而后一条件恰好等价于 $a\in\bigcap_{\chi\in X_m}\ker\chi=\langle g^{m}\rangle$。

> ✅ 已按 referee_algebra.md 修正（原表述：「由特征的正交关系（对循环群 $G=\mathbb F_p^{\times}$ 与其特征群 $X_m$）」——未说明须先在子群 $X_m$ 的公共核上取商）

故

$$\boxed{\ N(X^{m}=a)=\sum_{\chi\in X_m}\chi(a)\ }$$

（该式对 $a=0$ 也成立，已单独验证。）$\blacksquare$

*说明：整个问题只用两种情形：$m=2$（得到 $\#\{y:y^{2}=t\}=1+\chi_2(t)$，$p$ 为奇素数时对一切 $t$ 成立：$t=0$ 时右边 $=1+0=1$ ✓；$t\ne0$ 时为 $2$ 或 $0$ ✓）与 $m=3$（得到 $\#\{x:x^{3}=a\}=\mathbf 1(a)+\psi(a)+\psi^{2}(a)$）。*

**第 (1) 问：$p=3$ 或 $p\equiv2\pmod3$ 时 $N_p=p$**

先处理 $p=2$（题面未列，但 $p=2$ 时 $p\equiv2\pmod3$，为完整起见单独算）：$\mathbb F_2$ 上 $y^{2}=x^{3}+1$：$x=0$ 得 $y^{2}=1$，$\mathbb F_2$ 中 $1$ 只有一个平方根 $y=1$；$x=1$ 得 $y^{2}=0$，$y=0$。故 $N_2=2=p$，$|N_2-p|=0\le2\sqrt2$ ✓。以下设 $p$ 为奇素数。

当 $p\equiv2\pmod3$ 时 $\gcd(3,p-1)=1$，故 $x\mapsto x^{3}$ 是 $\mathbb F_p^{\times}$ 的自同构，也是 $\mathbb F_p$ 的双射（$0\mapsto0$）；$p=3$ 时 $x\mapsto x^{3}$ 是 Frobenius，同样是 $\mathbb F_3$ 的双射。于是由 (2) 的 $m=2$ 情形：

$$N_p=\sum_{x\in\mathbb F_p}\#\{y:y^{2}=x^{3}+1\}=\sum_{x\in\mathbb F_p}\bigl(\mathbf 1(x^{3}+1)+\chi_2(x^{3}+1)\bigr)=p+\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1).$$

令 $u=x^{3}+1$，由于 $x\mapsto x^{3}$ 是双射，$u$ 遍历 $\mathbb F_p$。故

$$\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1)=\sum_{u\in\mathbb F_p}\chi_2(u)=0$$

（最后一个等号：$\chi_2$ 非平凡，$\sum_{u}\chi_2(u)=0$；按约定 $\chi_2(0)=0$ 无影响）。于是

$$\boxed{N_p=p,\qquad |N_p-p|=0\le2\sqrt p\ }\qquad\blacksquare$$

**第 (3) 问：$p\equiv1\pmod3$ 时 $|N_p-p|\le2\sqrt p$**

此时 $p\ge7$ 为奇素数。取

$$T:=\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1),\qquad\text{则}\ N_p=p+T .$$

**第一步：把 $T$ 用 Jacobi 和表出。** 取 $\psi$ 为 $\mathbb F_p^{\times}$ 的一个 **3 阶**特征（存在，因 $3\mid p-1$）。由 (2) 的 $m=3$ 情形，对 $a\in\mathbb F_p$，

$$\#\{x\in\mathbb F_p:x^{3}=a\}=\sum_{i=0}^{2}\psi^{i}(a)\qquad(\psi^{0}=\mathbf 1),$$

（该式对 $a=0$ 也对：左边 $=1$，右边 $=\mathbf 1(0)+\psi(0)+\psi^{2}(0)=1+0+0=1$ ✓）。

按 $a=x^{3}$ 归并 $T$ 中的求和：

$$T=\sum_{a\in\mathbb F_p}\chi_2(a+1)\cdot\#\{x:x^{3}=a\}=\sum_{i=0}^{2}\ \sum_{a\in\mathbb F_p}\psi^{i}(a)\,\chi_2(a+1).$$

逐项计算：

- $i=0$：$\sum_{a}\chi_2(a+1)=0$（$a\mapsto a+1$ 是 $\mathbb F_p$ 的双射，$\chi_2$ 非平凡）。
- $i=1$：作代换 $a=-u$，
  $$\sum_{a}\psi(a)\chi_2(1+a)=\sum_{u}\psi(-u)\chi_2(1-u)=\psi(-1)\sum_{u}\psi(u)\chi_2(1-u)=\psi(-1)\,J(\psi,\chi_2),$$
  其中最后一步用 $u+(1-u)=1$ 直接对照 Jacobi 和的定义（$u=0$ 与 $u=1$ 两项分别贡献 $\psi(0)\chi_2(1)=0$ 与 $\psi(1)\chi_2(0)=0$，与定义一致）。
- $i=2$：同理得 $\psi^{2}(-1)\,J(\psi^{2},\chi_2)$，而 $\psi^{2}(-1)=\psi(-1)^{2}=1$（因 $\psi(-1)^{2}=\psi((-1)^{2})=1$）。

于是

$$\boxed{\ T=\psi(-1)\,J(\psi,\chi_2)+J(\psi^{2},\chi_2)\ }\qquad(\psi(-1)=\pm1) .$$

*数值检验*（$p=7$）：取 $\psi$ 使 $\psi(3)=\zeta_3$。可算出 $J(\psi,\chi_2)=3+2\zeta_3$，$J(\psi^{2},\chi_2)=1-2\zeta_3$，且 $\psi(-1)=\psi(6)=1$（$6\equiv3^{3}$ 是立方数），故 $T=(3+2\zeta_3)+(1-2\zeta_3)=4$，从而 $N_7=7+4=11$。直接点数：$x=0,1,2,4$ 时 $x^{3}+1$ 为非零平方（各 $2$ 解），$x=3,5,6$ 时 $x^{3}+1=0$（各 $1$ 解），共 $4\cdot2+3\cdot1=11$ ✓。

**第二步：三角不等式。** 已知 $|J(\chi,\mu)|=\sqrt p$ 当 $\chi,\mu,\chi\mu$ 都非平凡。这里：

- $\chi_2$ 非平凡（$p$ 奇，$\chi_2$ 阶为 $2$）；
- $\psi,\psi^{2}$ 的阶为 $3$，非平凡；
- $\psi\chi_2$ 与 $\psi^{2}\chi_2$ 非平凡：$\psi\chi_2=1$ 将迫使 $\psi=\chi_2$，但两者阶分别为 $3$ 与 $2$，不可能（$\psi\chi_2$ 的阶为 $\mathrm{lcm}$ 意义上的 $6$，因为 $\gcd(2,3)=1$ 且两特征生成不同的子群）。

故 $|J(\psi,\chi_2)|=|J(\psi^{2},\chi_2)|=\sqrt p$，于是

$$|T|=\bigl|\psi(-1)J(\psi,\chi_2)+J(\psi^{2},\chi_2)\bigr|\ \le\ |J(\psi,\chi_2)|+|J(\psi^{2},\chi_2)|=2\sqrt p .$$

由 $N_p=p+T$ 得

$$\boxed{\ |N_p-p|=|T|\le2\sqrt p\ }\qquad\blacksquare$$

**结论（$p\equiv1\bmod3$ 时）**：$N_p\in[p-2\sqrt p,\ p+2\sqrt p]$。这与「$\#E(\mathbb F_p)=1+N_p$、$a_p=p+1-\#E(\mathbb F_p)=p-N_p$，Hasse 界 $|a_p|\le2\sqrt p$」完全一致：本题证明的正是曲线 $E:y^{2}=x^{3}+1$（$j$-不变量为 $0$、具有复乘 $\mathbf Z[\zeta_3]$）的 Hasse 界的一个特例。

**本题考点 / 技巧（一句话）**：把「数点」翻译成「特征和」——先用特征正交性把「方程 $X^{m}=a$ 的解数」写成特征和，再把 $\sum_x\chi_2(x^{3}+1)$ 通过 $a=x^{3}$ 归并成两个 Jacobi 和（一个带 $\psi(-1)$ 的符号），最后用 $|J|=\sqrt p$ 与三角不等式收尾。

**难度**：$\boxed{5/5}$（需要自己想到引入 3 阶特征 $\psi$ 并用 $\#\{x:x^3=a\}=\sum_i\psi^i(a)$ 做变换；$\psi(-1)=\pm1$ 的符号讨论是容易掉进去的坑——若只用三角不等式而不先合并，会得到 $2\sqrt p+1$ 而非 $2\sqrt p$；最后还需单独处理 $p=2$，因为二次特征的平方根计数公式对 $p=2$ 失效）。

**同类题在哪几年出现过**：特征和/椭圆曲线的题目集中在 2026 年（同年第 1 题是 $\Gamma_0(p)\alpha\Gamma_0(p)$ 的右陪集分解即 Hecke 算子结构，第 5 题是 $p$ 进域上给定次数的有限扩张个数与完全分歧 Galois 扩张的循环性），以及 2019 team №4（Gauss 和 $g_p=\sum_a\left(\frac ap\right)\zeta_p^a$、$g_p^{2}=\left(\frac{-1}p\right)p$、$|g_p|^{2}=p$）与 2014 individual №5（Chevalley–Warning 定理）。若想再练这一族，2019 team №4 是最接近的姊妹题——它证明的是「Gauss 和的模长」，本题用的是「Jacobi 和的模长」。


---

## 三、讲义使用建议

### 3.1 建议的刷题顺序（三轮制）

不要按题号顺序刷（题号的编排是「年份」，不是「难度」）。建议按下面的三轮推进：

**第一轮：基础校准（题 2 → 题 1 → 题 3，共约 50–70 分钟）**

| 顺序 | 题 | 预计耗时 | 目的 |
|---|---|---|---|
| 1 | 题 2（2012 individual №1，Eisenstein） | 10–15 分钟 | 热身。检验「遇多项式先算 $\gcd$ 再看 $p^2$」的条件反射 |
| 2 | 题 1（2010 individual №1，$AB-BA=B$） | 15–20 分钟 | 检验「取哪个算子的特征子空间」的判断力；顺手学「$\mathrm{tr}(B^k)=0\Rightarrow B$ 幂零」 |
| 3 | 题 3（2018 individual №3，99 阶群交换） | 15–20 分钟 | 把 Sylow 三定理 + $p^2$ 阶群交换 + 半直积作用平凡三件事连成一条链 |

> ✅ 已按 referee_algebra.md 修正（本表第 1 行原写作 $gcd$，缺反斜杠）

**第二轮：主流难度（题 4 → 题 6 → 题 7 → 题 5，共约 2.5–3 小时）**

| 顺序 | 题 | 预计耗时 | 目的 |
|---|---|---|---|
| 4 | 题 4（2013 individual №1，26 阶群分类 + Aut） | 30–40 分钟 | 群分类的标准流程；重点练 $\mathrm{Aut}(D_{2n})=\mathrm{Hol}(C_n)$ 的参数化写法 |
| 5 | 题 6（2017 individual №2，Fitting 分解） | 25–35 分钟 | 有限集上「满射 = 双射」这一句是很多题的钥匙 |
| 6 | 题 7（2019 individual №5，Fibonacci + 范数） | 40–50 分钟 | 有限域上的 Binet 公式与二次互反；第 3 问的「跳到 $\mathbb F_{p^2}$」是分水岭 |
| 7 | 题 5（2016 team №3，$x^4-x^2-1$ 的域格） | 60–90 分钟 | 工作量最大的一道中等题：要写全 10 个子域并证明互不相同 |

> ✅ 已按 referee_algebra.md 修正（本表第 2、3 行原写作 $mathrm{tr}$、$mathrm{Aut}$、$mathbb F$，缺反斜杠）

**第三轮：偏难突破（题 8 → 题 9 → 题 10，共约 3.5–4.5 小时）**

| 顺序 | 题 | 预计耗时 | 目的 |
|---|---|---|---|
| 8 | 题 8（2022 individual №5，分圆域） | 60–80 分钟 | 分圆域的标准套路；若 (d) 的指数论证卡住，先只做出 (a)(b)(c) |
| 9 | 题 9（2014 individual №3，$X^2-82Y^2=pm2$） | 50–70 分钟 | 学会用「范 $-1$ 单位」造递降算子；$(b)$ 的计数 + Hensel 是通用技术 |
| 10 | 题 10（2026 individual №2，Jacobi 和/Hasse 界） | 90–120 分钟 | 全卷最难。建议先读第 (2) 问、把它当工具，再攻第 (3) 问 |

### 3.2 时间预算与「卡住怎么办」

- **单题硬上限**：基础题 20 分钟、中等题 60 分钟、偏难题 120 分钟。超过上限就先看「考点一句话」和「解题的第一步」，然后合上讲义自己重做——**看懂不等于会做**，这是本讲义唯一想强调的学习方法。
- **丘赛实战节奏**：个人赛通常 5–6 题、2.5–3 小时，平均每题 25–35 分钟；且多数年份明确写「选做 5 题，或取最高 5 题计分」。因此**战略性放弃**（例如看到 2026 №1 的 Hecke 双陪集、2023 №6 的 $p$ 进对数，若不熟就跳过）比死磕更划算。本讲义题 8、9、10 正是按「值得花 60–120 分钟」来标定的。
- **复现清单**：做完每题后，请独立写出下列五条（这是丘赛评分最看重的「可检验步骤」）：
  1. 题 1：$A(W)\subseteq W$ 的那一行等式；
  2. 题 2：$\gcd$ 与 $p^2\nmid$ 常数项两个条件；
  3. 题 4：$\mathrm{Aut}(D_{26})$ 的 $(a,b)$ 参数化与乘法公式；
  4. 题 7：$\alpha^{p+1}=\alpha\beta=\beta^{p+1}$ 这三步等号；
  5. 题 8：$\mathrm{Tr}(\gamma(1-\zeta))=a_0p$ 的完整计算。

> ✅ 已按 referee_algebra.md 修正（本清单五条原有 7 处 LaTeX 命令缺反斜杠（$gcd$、$p^2 mid$ 断行、$mathrm{...}$、$alpha...eta$ 处还混入了退格字符），已逐条补全）

### 3.3 与其他材料的配合

- 想系统练「Sylow + 半直积」：本讲义题 3、4 + 2010 team №5 / 2011 individual №6（150 阶群非单）+ 2016 individual №5。
- 想系统练「Galois 对应与子域格」：本讲义题 5 + 2010 individual №4（$x^8-5$）+ 2013 team №6（$x^4-2$）。
- 想系统练「代数数论」：本讲义题 8 + 2018 individual №2（三次域分解律）+ 2018 team №3 与 2024 individual №6（分圆多项式模 $p$）+ 2026 individual №3、№4（互素性与整基）。
- 想系统练「有限域与特征和」：本讲义题 7、10 + 2019 team №4（Gauss 和）+ 2013 team №5（$\mathbb F_2$ 上不可约多项式计数）。

> ✅ 已按 referee_algebra.md 修正（原文此处写作 $mathbb F_2$，缺反斜杠）

---

## 四、无法完整解出 / 存疑清单

本节如实记录三类问题：**题面未能复核的**、**被我放弃的题号及原因**、**解答中需要读者留意或属于我个人补充的部分**。

### 4.1 题面未能用原始 PDF 复核的题

| 年份 / 题号 | 情况 | 影响 |
|---|---|---|
| 2026 individual №2（**已选入，即题 10**） | 本地 PDF 归档 `F:\丘成桐大学生数学竞赛历年笔试真题\` 只有 2010–2025 共 16 个年份目录，**没有 2026 年的任何试卷文件**；因此题面只能取自 `problems_full.json` 的抽取文本并清理排版 | 题面自足（所需外部事实 $|J(\chi,\mu)|=\sqrt p$ 已在题面给出），解答不依赖题面的任何隐含条件；但**题面文字的标点、括号可能与原始试卷有出入** |
| 2026 individual №1、№3、№4、№5（未选入） | 同上，无法 PDF 复核 | 未选入，无影响 |

### 4.2 被我评估后放弃的题号与原因

以下题都是我在 150 道代数题中评估过、但最终**没有**选入本讲义的。放弃原因分三类，全部如实记录：

**(A) 抽取文本残缺或需要读 PDF 才能恢复，且性价比低**

1. **2017 team №1 与 №2**：`problems_full.json` 中 `kind=team, n=1` 的条目结尾停在 "...such that $g_1g_2=g_2g_1=g$
"，而 `n=2` 的条目开头是 "= 1 and $g_1g_2=g_2g_1=g$."——两题的正文被跨页切分并互相错位。要正确取题必须回读 PDF；因同类考点（Cauchy 型分解 $g=g_1g_2$）已被题 6 覆盖，放弃。

> ✅ 已按 referee_algebra.md 修正（原表述：称 2017 team №1/№2 条目跨页错位——在当前 757 题快照中这两条文本已完整，此说明仅适用于旧快照；2019 team №1/№2 的错位仍然存在）
2. **2019 team №1 与 №2**：`n=1` 条目结尾被截断为 "$S_{\lceil n/2\rceil}$"，`n=2` 条目开头是 "$]\ltimes(\mathbb Z/2\mathbb Z)^{\lfloor n/2\rfloor}$．2) Recall that..."——同样是跨页错位。放弃。
3. **2011 individual №5**（五项正合列、中间映射为同构）：抽取文本把页眉/页脚（`附件/试卷 4 Appendix/Contest Paper 4 Algebra, Number Theory and Combinatorics, 2011-Individual`）混入题面，且五列图的箭头排版全部丢失（变成一串孤立的 `A → B → C → D → E` 与 `↓`）。题意本身可通过 PDF 恢复，但同型的「五项引理」不在本讲义骨架内，放弃。

**(B) 需要超出本讲义自足范围的重型工具**

4. **2012 individual №5**（复环面 $\mathbb C/\Lambda$ 的乘子环 $R$ 与 $R^{\times}$ 的最大阶）：需要虚二次域的 CM 理论（$R$ 是虚二次域的序、$R^\times$ 的有限性与最大阶的判定），无法在 3–5 页内自足地写完整证明。**明确标注：此题我没有把握在不引用 CM 理论的前提下给出完整解答**，故不选。
5. **2015 individual №2**（$O_n(\mathbb C)$-不变有理函数空间 $F_0,F_1$ 的结构）与 **2015 individual №4**（$\mathbb Z_p$ 上映射 $\varphi(x)=x^p+p\sum a_nx^n$ 的动力学与 $\varphi^{*}$ 在局部常值函数空间上的特征值 $\{0,1\}$）：前者需要不变量环/矩阵空间上的几何商理论，后者需要 $p$ 进紧集上局部常值函数空间的完整铺垫（收缩映射、极限点 $\epsilon_R$、Hecke 型算子）。两题都能做，但需要一整节篇幅，本讲义为了 10 题的完整度放弃。
6. **2020 individual №6**（球完备空间、$\mathbb Q_p(\mu_{p^\infty})$）：需要 $p$ 进代数扩张与球完备性的深入讨论，放弃。
7. **2022 individual №3**（显式构造 $\mathfrak{sl}(4,\mathbb C)\cong\mathfrak{so}(6,\mathbb C)$ 的 Lie 代数同构）：可以构造 $\Lambda^{2}(\mathbb C^{4})$ 上的作用并验证，但完整的「为什么这是同构」需要若干页的计算；本讲义已有题 1 覆盖 Lie 代数味道，放弃。

**(C) 考点已被选入题目覆盖，或属于其他科目**

8. **2016 individual №2**（$\mathbb Z^{d}$ 的指数 $n$ 子群计数 $f_d(n),g_d(n)$ 与 Dirichlet 级数）：很好的题，但考点（有限生成 Abel 群 + 计数）与题 6 有一定重叠，且更偏组合数论，放弃。
9. **2012 individual №4、2012 individual №6、2014 individual №2、2014 individual №5、2019 team №3、2020 individual №2、2023 individual №1–№4、2024 individual №1、2025 individual №1–№3** 等：其中不少是好题（如 2022 individual №4「每个理想 2-生成」、2023 individual №1「初等矩阵生成 $\mathrm{SL}_n$」）。放弃理由统一为：**与已选题目的骨架考点重复**（Sylow/半直积、模论、表示论、不可约性），或属于交换代数/同调代数的独立专题，收入会稀释讲义的聚焦度。
10. **2014 individual №2**（$(t^{a_i+a_j})$ 与 $\left(\frac1{1+a_i+a_j}\right)$ 的正定性）：数学上是漂亮的矩阵分析题，但严格说属于分析与线性代数而非「代数与数论」骨架，放弃。

### 4.3 解答中属于我个人补充、或需读者留意的地方

1. **题 9 (b)**：原题只要求「任一 $n$ 与**奇**素数 $p$」。我额外补充了 $p=2$ 的情形，方法是对 $\mathbf Z_2$ 给出**显式点** $(10/3,\,1/3)$（验证 $(10/3)^2-82(1/3)^2=2$，且 $3\in\mathbf Z_2^{\times}$）。这属于我的补充论证，不是原题要求，也没有做完整的 $p=2$ 局部理论分析。
2. **题 10 第 (1) 问**：题面写「Assume $p=3$ or $p\equiv2\pmod3$」，字面上 $p=2$ 也满足 $p\equiv2\pmod3$，而第 (2) 问的特征计数对 $p=2$ 失效（$\mathbb F_2$ 中 $1$ 只有一个平方根）。因此我**单独用直接点数**处理了 $p=2$（$N_2=2=p$），并明确标注这是补充。
3. **题 8 (d)**：证明中用到两条标准事实，我作引用处理而未重证：（i）$\mathrm{disc}(\Phi_p)=\pm p^{p-2}$（我给出了由 $(X-1)\Phi_p(X)=X^{p}-1$ 求导取范数的完整推导，故这一条实际上是自足的）；（ii）$\mathrm{disc}(1,\zeta,\dots,\zeta^{p-2})=[\mathcal O_K:\mathbf Z[\zeta]]^{2}\cdot d_K$（判别式与指数的关系），这一条是代数数论教材的标准结论，我未重新证明。
4. **题 5 (b)**：10 个子域「互不相同」的判定，我是通过「与子群格的反序对应」以及显式不动元素（$i,\ \sqrt5,\ i\alpha,\ u=\alpha+i/\alpha,\ v=\alpha-i/\alpha$）双向核对得到的；其中 $u^2=1+2i$、$v^2=1-2i$、$uv=\sqrt5$ 三个恒等式我已逐步验证（用到 $1/\varphi=\varphi-1$）。读者若想更保险，可直接用 Galois 对应：不同的子群给出不同的不动域，因此只需把 10 个子群列全，已由上文完成。
5. **题 6**：$K$ 的取法我要求同时满足「$\mathrm{im}\,\varphi^{K}$ 稳定」与「$A_{\mathrm{nil}}\subseteq\ker\varphi^{K}$」。后者总可通过把 $K$ 取得更大来保证（$\varphi$ 在有限的 $A_{\mathrm{nil}}$ 上幂零），这一点在原文中没有强调，但证明里必须显式处理，否则 $\ker\varphi^{K}=A_{\mathrm{nil}}$ 这一步不成立。
6. **题 1**：主证明是完全初等的（只用特征子空间与代数闭性）。文末「$B$ 幂零」的点评用到了 $\mathrm{tr}(XY)=\mathrm{tr}(YX)$ 与 Newton 恒等式；在特征 $0$ 下成立，这也是原题设在 $\mathbb C$ 上的原因。若把题面换到正特征域上，该点评不再成立（但主证明中的「代数闭」一步仍需，因为要取 $B$ 与 $A|_W$ 的特征值）。
7. **题 4**：$\mathrm{Aut}(D_{26})\cong \mathrm{Hol}(\mathbb Z/13)$ 的证明中，我用 von Dyck 定理验证「保持定义关系的映射给出同态」，这是标准做法；若读者偏好更谨慎的写法，可改用「先构造 $\psi_{a,b}$ 在生成元上的像、证明其满足全部关系、再说明它是双射」的等价叙述（文中已包含双射性验证）。
8. **未做的核对**：本讲义没有对 2012–2026 年的**官方解答 PDF**（归档中 2020–2022 年有 `*_soln_*.pdf`）做逐字比对。所有解答都是我独立推导的；若读者发现与官方解答不一致之处，请以原始 PDF 为准并在报告上加注。

---

## 附录 A：考点 × 年份 速查表

| 考点 | 本讲义题号 | 同年份/邻近年份的同类真题 |
|---|---|---|
| 交换子与不变子空间 | 题 1 | 2011 ind №4；2014 ind №6；2017 ind №5；2023 ind №1 |
| 不可约性判别（Eisenstein / 模约化） | 题 2 | 2013 ind №5；2013 team №5；2020 ind №4；2021 ind №1；2024 ind №3 |
| Sylow 理论与群的非单性 | 题 3、题 4 | 2010 team №5；2011 ind №6；2016 ind №5；2011 team №5；2012 ind №2 |
| 群扩张分类与自同构群 | 题 4 | 2014 team №4；2019 team №1 |
| Galois 对应与子域格 | 题 5 | 2010 ind №4；2013 team №6；2015 team №6；2021 ind №2 |
| 有限 Abel 群 / Fitting 分解 | 题 6 | 2015 ind №1；2016 team №4；2018 team №1；2013 team №2 |
| 有限域与二次互反 | 题 7、题 10 | 2019 team №4；2017 team №4；2012 ind №2 |
| 分圆域、单位根、整数环 | 题 8 | 2015 team №3；2018 team №3；2019 team №4；2024 ind №6；2020 ind №4 |
| Pell 型方程与局部–整体 | 题 9 | 2014 team №6；2018 ind №2 |
| 特征和 / Jacobi 和 / 椭圆曲线 | 题 10 | 2026 ind №1、№5；2019 team №4；2014 ind №5（Chevalley–Warning） |
| 迹与范数 | 题 8、题 7 | 2017 team №2；2020 ind №1；2019 ind №5 |

## 附录 B：一页公式卡

**有限群**

- Sylow：$n_p\equiv1\pmod p$，$n_p\mid|G|/p^{a}$（$p^a\|\,|G|$）。
- $p^2$ 阶群交换；$|G|=pq$（$p<q$ 素数，$p\nmid q-1$）$\Rightarrow G\cong C_{pq}$；$p\mid q-1$ 时 $\Rightarrow G\cong C_{pq}$ 或 $C_q\rtimes C_p$。
- $\mathrm{Aut}(C_n)\cong(\mathbb Z/n)^{\times}$；$\mathrm{Aut}(D_{2n})\cong \mathrm{Hol}(C_n)=C_n\rtimes(\mathbb Z/n)^{\times}$（$n$ 奇），阶为 $n\varphi(n)$。

**Galois 理论**

- $[\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n)$，$\mathrm{Gal}\cong(\mathbb Z/n)^{\times}$（$\zeta_n$ 是本原 $n$ 次单位根）。
- 子域 $\leftrightarrow$ 子群（反序）；$[E:F]=[\mathrm{Gal}(L/F):\mathrm{Gal}(L/E)]$；$E/F$ Galois $\iff \mathrm{Gal}(L/E)\trianglelefteq\mathrm{Gal}(L/F)$。

**数论**

- $\sum_{a=1}^{p-1}\zeta_p^{a}=-1$，$\mathrm{Tr}_{\mathbb Q(\zeta_p)/\mathbb Q}(1-\zeta_p)=p$，$\mathcal N(1-\zeta_p)=\Phi_p(1)=p$。
- $\mathcal N(\zeta_n-1)=\begin{cases}p,& n=p^{k}\\ 1,& \text{其他}\end{cases}$（对比 2015 team №3）。
- $\left(\frac5p\right)=\left(\frac p5\right)$，故 $\left(\frac5p\right)=1\iff p\equiv\pm1\pmod5$。
- Fibonacci：$F_n=\dfrac{\alpha^{n}-\beta^{n}}{\alpha-\beta}$，$\alpha\beta=-1$，$\alpha+\beta=1$。
- 对奇素数 $p$：$\#\{(x,y)\in\mathbb F_p^{2}:y^{2}=x^{3}+1\}=p+\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1)$（$p=2$ 时该式不成立，需单独点数 $N_2=2$），且 $\left|\sum_x\chi_2(x^{3}+1)\right|\le2\sqrt p$。检验：$p=7$ 时 $\sum_x\chi_2(x^{3}+1)=4$，$N_7=7+4=11$，与直接点数一致。

> ✅ 已按 referee_algebra.md 修正（原表述：$p-\sum_x\chi_2(x^{3}+1)$——符号写反，与正文 $N_p=p+T$ 及 $N_7=11$ 矛盾）
- Jacobi 和：$J(\chi,\mu)=\sum_{a+b=1}\chi(a)\mu(b)$，$|J(\chi,\mu)|=\sqrt p$（$\chi,\mu,\chi\mu$ 非平凡）。

---

**文件**：`.tmp/burn2026/reports/solutions_algebra.md`
**选题**：2010 ind№1、2012 ind№1、2018 ind№3、2013 ind№1、2016 team№3、2017 ind№2、2019 ind№5、2022 ind№5、2014 ind№3、2026 ind№2（10 个不同年份）。
**全部 10 题均给出完整解答**；未解出/未选入的题号与原因见第四节。



