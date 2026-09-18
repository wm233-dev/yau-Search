# 对抗性审稿报告：<code>/reports/solutions_analysis.md</code>

> **被审对象**：《丘成桐大学生数学竞赛 · 分析与偏微分方程 真题解题讲义》（10 道题）
> **审稿人立场**：默认"有错"，逐题回原卷 PDF 核对题面、逐步审计证明、独立数值复算。
> **原始试卷**：<code>sources/prelim\</code>（只读；经核实**只有 2010–2025，无 2026**，讲义对此的声明属实）。
> **题库**：<code>/data/problems_full.json</code>（本次审稿快照：**757 条记录**，其中 subject = "Analysis & PDE" 者 **155 道**）。
> **全部数值结论的可复跑脚本**：<code>/scripts/referee_verify.py</code>
> 运行：<code>python scripts\referee_verify.py</code>（工作目录 <code></code>）
> 辅助脚本：<code>ref_pdf_dump.py</code>（10 道题的原卷 PDF 文本转储 → <code>/archive/work/ref_pdf_dump.txt</code>）、<code>ref_pdf_dump2.py</code>、<code>ref_pdf_2021b.py</code>、<code>ref_probe2/6/7/8.py</code>（题库检索）。

---

## 1. 总体裁定表

| 题号 | 讲义标注出处 | 题面是否正确（对原卷） | 结论是否正确 | 证明是否完整 | 裁定 | 一句话理由 |
|---|---|---|---|---|---|---|
| 1 | 2011 Individual #2 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | 共振特解 $\alpha xe^{-x}$、$\alpha=-2$、$A=1,B=-1$ 全部正确，残差 $8.9\times10^{-16}$ |
| 2 | 2014 Team #1 | ✅ 与 PDF 逐字一致（题库编号偏移说明亦属实） | ✅（$I=0$） | ⚠️ 法一、法二正确；**法三有两处实质错误**；法二控制函数多写一个因子 | **MINOR-FIX** | 主解答对，但讲义自称"已修正"的法三仍然错：留数用错支、$\oint=0$ 与 keyhole 恒等式矛盾 |
| 3 | 2015 Individual #2 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | Weierstrass + 三角不等式 + 非负连续函数积分零；Stieltjes 反例的矩经精确验算确为 0 |
| 4 | 2010 Individual #6 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | 关键在"对 $\lvert x\rvert$ 而非 $\lvert x\rvert^2$ 写不等式"；两个反例均经独立求解验证 |
| 5 | 2013 Individual #2 | ✅ 与 PDF 逐字一致（含 $d\ge2$） | ✅ | ✅ | **VERIFIED** | 三种证法均正确；随机多项式（$d=2,3,4,6,8$）复算恒为零 |
| 6 | 2017 Team #5 | ✅ 与 PDF 逐字一致（PDF 为 5 科合卷第 1 页，亦属实） | ✅ | ✅ | **VERIFIED** | 正交性计算、径向 ODE 分类（$n\ge3$ / $n=2$ / $n=1$）与基本解归一化全部正确 |
| 7 | 2020 Individual #5 | ✅ 与 PDF 逐字一致 | ✅ | ✅（第 4 步宜补一句反证） | **VERIFIED** | 时间映射 $\Psi$ + 奇对称 + 唯一性的路线正确；$T(x_0)$ 全部数值逐位复现 |
| 8 | 2018 Individual #6 | ✅ 与 PDF 逐字一致（$n\ge2$ 瑕疵说明亦属实） | ✅ | ⚠️ 引理 8.1 证明中 **(8.6) 差一个符号**、第 4 步 (a) 有一处**无效论证**（结论仍成立） | **MINOR-FIX** | 结论与主线正确、可修补；但两处瑕疵必须改写 |
| 9 | 2025 Individual #2 | ✅ 与 PDF 逐字一致 | ✅（$C_{\rm opt}=\frac4{(n-2)^2}$） | ✅ 解析部分；❌ **数值核对表不可复现** | **MINOR-FIX** | 表格里的 5 个数恰等于 $1/\alpha_\epsilon^2$（只在 $B_1$ 上的比值），真实完整比值在 $\epsilon=0.2$ 时是 **0.818**，不是 11.111 |
| 10 | 2026 Individual #1 | ⚠️ **无法回原卷核对**（F 盘确无 2026 卷；题库文本完整） | ✅ | ✅ | **VERIFIED**（题面无法核对） | 两次分部积分 + 指标回代正确；$I_0..I_6$ 与递推残差 $<10^{-12}$ 全部复现；$q^nI_n$ 整性论证严密 |

---

## 2. 逐题详审

### 题 1 —— 2011 · Individual · #2

**题面核对**（原卷 <code>2011\1.AnalysisDiffEquation-Individual-2011.pdf</code>，逐行比对 <code>ref_pdf_dump.txt</code> 第 17–23 行）

> 原卷：<code>2. Solve the following problem: { d²u/dx² − u(x) = 4e^{−x}, x ∈ (0,1), u(0)=0, du/dx(0)=0.</code>

讲义题面与之**逐字一致**（仅把 PDF 抽取出的 <code>½</code> 花括号噪声还原为 cases 环境），无缺失、无改写、符号无误。讲义 §12.1 指出"区间写 $x\in(0,1)$ 而初值给在端点 $x=0$"属**题面原样**，不是讲义改写，属实。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | 特征方程 $\lambda^2-1=0\Rightarrow\lambda=\pm1$，$u_h=Ae^x+Be^{-x}$ | **成立** | 常系数线性 ODE 基本定理（二阶、特征根互异） |
| 2 | 共振规则：$\lambda=-1$ 是单根 $\Rightarrow$ 试 $u_p=\alpha xe^{-x}$ | **成立** | 待定系数法的共振规则（重数 $s=1$ 时乘 $x^s$） |
| 3 | 代入得 $u_p''-u_p=-2\alpha e^{-x}$，$\alpha=-2$ | **成立** | 直接计算；脚本 [R1] 复核 |
| 4 | 初值 $A+B=0$、$A-B=2$ $\Rightarrow A=1,B=-1$ | **成立** | 线性方程组 |
| 5 | 唯一性（Picard–Lindelöf / 延拓） | **成立**（但属多余） | 线性方程显式解已在 $\mathbb R$ 上整体存在，唯一性可由"两解之差满足齐次方程 + 零初值"直接得到，不必引 Picard–Lindelöf |

**具体问题**：**未发现数学错误。**

- 复核结果：$\max_{[0,1]}\lvert u''-u-4e^{-x}\rvert = 8.88\times10^{-16}$；$u(0)=0$、$u'(0)=0$、$u(1)=1.614643504944718$（讲义称 $1.6146435049$ ✔）。
- 讲义补充的**常数变易法**对照也正确：$W=-2$，$u_p=2e^x\int_0^xe^{-2s}ds-2xe^{-x}=e^x-e^{-x}-2xe^{-x}$ ✔，与待定系数法一致。

**未解决疑点**：无。

---

### 题 2 —— 2014 · Team · #1

**题面核对**（<code>2014\analysis2014(team).pdf</code>）

> 原卷：<code>1. Calculate the integral: ∫_0^∞ (log x)/(1+x²) dx.</code>

讲义题面**逐字一致** ✔。讲义"编号差异"的说明也属实：题库 <code>2014_analysis2014_team</code> 无 $n=1$，其 $n=2$ 的 text 把原卷第 1 题与第 2 题开头（"Construct an increasing function…"）合并（本次复核已确认该 text 内容）。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | 绝对收敛性（$(0,1]$ 用 $\lvert\log x\rvert$；$[1,\infty)$ 用 $\log x/x^2$） | **成立** | 比较判别法；$\int_0^1\lvert\log x\rvert dx=1$、$\int_1^\infty\frac{\log x}{x^2}dx=1$ |
| 2 | $x\mapsto1/x$ 得 $I=-I$ | **成立** | 换元积分（绝对收敛保证合法） |
| 3 | 法二：$F(a)=\frac{\pi}{2\sin(\pi a/2)}$，$I=F'(1)=0$ | **成立** | Beta/Gamma 反射公式 + Leibniz 积分号下求导 |
| 4 | 法二"控制函数"写法 | **不成立（需修正）** | 见下 |
| 5 | 法三：keyhole 围道 | **不成立（两处实质错误）** | 见下 |

**具体问题与修正文本**

**(A) 法二的控制函数多写了一个因子。** 原文：

> 被与 $a$ 无关的可积函数 $C\Big(x^{a_0-1}+x^{a_1-1}\Big)\dfrac{\lvert\log x\rvert}{1+x^2}\cdot\dfrac{1}{1+x^2}$ 型控制函数控制

**修正文本（直接替换该句）**：

> 被与 $a$ 无关的可积函数 $C\big(x^{a_0-1}+x^{a_1-1}\big)\dfrac{\lvert\log x\rvert}{1+x^{2}}$ 控制：当 $0<x\le1$ 时 $x^{a-1}\le x^{a_0-1}$，$\int_0^1x^{a_0-1}\lvert\log x\rvert dx<\infty$（因 $a_0>0$）；当 $x\ge1$ 时 $x^{a-1}\le x^{a_1-1}$，$\dfrac{x^{a_1-1}\lvert\log x\rvert}{1+x^2}\le x^{a_1-3}\lvert\log x\rvert$，$\int_1^\infty x^{a_1-3}\lvert\log x\rvert dx<\infty$（因 $a_1<2$）。于是由 **Leibniz 积分号下求导定理**，$F$ 在 $(0,2)$ 上可导。

（原文保留那个多余的 $1/(1+x^2)$ 会**使控制不等式失效**：$x\to\infty$ 时左端 $\sim x^{a-3}\lvert\log x\rvert$，右端 $\sim x^{a_1-5}\lvert\log x\rvert$，取 $a=a_1=1.9$ 即得左端远大于右端。）

**(B) 法三整体错误，必须删除或按下文改写。** 原文声称：

> $\operatorname{Res}_{z=-i}\frac{(\log z)^2}{1+z^2}=\frac{\pi^2}{8i}$，两者之和为 $0$，故围道积分为 $0$，从而 $\int_0^\infty\frac{\log x}{1+x^2}dx=0$（同时可得 $\int_0^\infty\frac{(\log x)^2}{1+x^2}dx=\frac{\pi^3}{8}$）。

三处问题：

1. **留数用错了支。** keyhole 围道的割线在 $[0,\infty)$，必须取支 $\arg z\in(0,2\pi)$，此时 $\log i=\frac{\pi i}{2}$、$\log(-i)=\frac{\mathbf{3}\pi i}{2}$。讲义用的是主支 $\log(-i)=-\frac{\pi i}{2}$，与所用围道不自洽。
2. **"围道积分为 0" 是错的。** 无论留数怎么算，keyhole 恒等式都给出 $\oint\frac{(\log z)^2}{1+z^2}dz=\int_0^\infty\frac{(\log x)^2-(\log x+2\pi i)^2}{1+x^2}dx=4\pi^2\cdot\frac{\pi}{2}-4\pi i\,I=2\pi^3-4\pi i\,I$，其实部恒为 $2\pi^3\neq0$。若真取 $\oint=0$，就要推出 $\frac{\pi}{2}=0$——荒谬。脚本 [R2b] 直接数值积分 keyhole 得 $\oint=62.012553=\mathbf{2\pi^3}$（与"正确留数之和 $\frac{\pi^2}{i}$"完全吻合）。
3. **"同时可得 $\int_0^\infty\frac{(\log x)^2}{1+x^2}dx=\frac{\pi^3}{8}$"** 这个副产品不是 $(\log z)^2$ 给的（它给的是 $J=\int_0^\infty\frac{dx}{1+x^2}=\frac{\pi}{2}$），要用 $(\log z)^3$。

**修正文本（整段替换"法三"）**：

> #### 法三：围道积分（用正确的支）
>
> 取 $f(z)=\dfrac{(\log z)^2}{1+z^2}$，其中 $\log$ 取支 $\arg z\in(0,2\pi)$（割线为 $[0,\infty)$），沿标准 keyhole 围道（外圆半径 $R\to\infty$、内圆半径 $\epsilon\to0$、两岸紧贴实轴）积分。此时 $\log i=\frac{\pi i}{2}$，$\log(-i)=\frac{3\pi i}{2}$，故
> $$\operatorname{Res}_{z=i}f=\frac{(\pi i/2)^2}{2i}=-\frac{\pi^2}{8i},\qquad
> \operatorname{Res}_{z=-i}f=\frac{(3\pi i/2)^2}{-2i}=\frac{9\pi^2}{8i},\qquad \sum=\frac{\pi^2}{i},$$
> $$\oint f\,dz=2\pi i\cdot\frac{\pi^2}{i}=2\pi^3 .$$
> 另一方面，两岸相减后 $\log$ 增加 $2\pi i$，留下 $-4\pi i\log x+4\pi^2$：
> $$\oint f\,dz=\int_0^\infty\frac{(\log x)^2-(\log x+2\pi i)^2}{1+x^2}dx
> =4\pi^2\underbrace{\int_0^\infty\frac{dx}{1+x^2}}_{=\pi/2}-4\pi i\,I=2\pi^3-4\pi i\,I .$$
> 与 $\oint f\,dz=2\pi^3$ 比较，实部自动一致、虚部给出 $\boxed{I=0}$。
>
> **若还想要 $\int_0^\infty\frac{(\log x)^2}{1+x^2}dx=\frac{\pi^3}{8}$，必须改用 $g(z)=\frac{(\log z)^3}{1+z^2}$**（同一支）：$\operatorname{Res}_ig=-\frac{\pi^3}{16}$、$\operatorname{Res}_{-i}g=\frac{27\pi^3}{16}$，$\sum=\frac{13\pi^3}{8}$，$\oint g=\frac{13\pi^4 i}{4}$；而两岸之差为 $-6\pi iK+12\pi^2 I+8\pi^3 i$（$K:=\int_0^\infty\frac{(\log x)^2}{1+x^2}dx$）。与 $I=0$ 联立得 $K=\frac{\pi^3}{8}$ ✔。

**未解决疑点**：讲义 §12.3 第 3 条自称"法三在最初草稿中出过相位记账的错误，我已删除错误版本、改写成对 $(\log z)^2$ 的正确处理"——**这句话本身不成立**，现版本仍是错的。除此之外主解答无问题。

---

### 题 3 —— 2015 · Individual · #2

**题面核对**（<code>2015\analysis2015-individual.pdf</code>，PDF 第 110–113 行）

> 原卷：<code>2. Let f be a continuous function on [a,b], define M_n = ∫_a^b f(x)x^n dx. Suppose that M_n = 0 for all integers n ≥ 0, show that f(x) = 0 for all x.</code>

讲义题面**逐字一致** ✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | 由线性性把条件升级为 $\int fq=0$ 对一切多项式 $q$ | **成立** | 积分线性性；条件对每个 $n$ 单独成立 |
| 2 | Weierstrass 逼近：紧区间上连续函数可被多项式一致逼近 | **成立** | Weierstrass 逼近定理；$[a,b]$ 紧（讲义已指出紧性本质） |
| 3 | $\lvert\int f^2\rvert\le\lVert f-q_j\rVert_\infty\int\lvert f\rvert\to0$ | **成立** | 三角不等式 + $f$ 在紧区间有界 |
| 4 | 连续非负函数积分为零 $\Rightarrow$ 恒零 | **成立** | 连续性 + 正测度邻域（端点取单侧） |
| 5 | Stieltjes 反例：$f=e^{-x^{1/4}}\sin(x^{1/4})$ 的**所有**矩为零 | **成立** | 见下 |

**具体问题**：**未发现数学错误。** 讲义给的反例经我精确验算成立：代换 $x=t^4$ 后矩 $=4\int_0^\infty t^{4n+3}e^{-t}\sin t\,dt=4\,\Im\frac{(4n+3)!}{(1-i)^{4n+4}}$，而 $(1-i)^{4n+4}=\big((1-i)^4\big)^{n+1}=(-4)^{n+1}\in\mathbb R$，故虚部恒为 $0$。脚本 [R3] 对 $n=0,\dots,7$ 输出全为 $0.000e{+}00$ ✔。（讲义由此断言"$\{x^n\}$ 在 $L^2(e^{-x^{1/4}}dx)$ 中不完备"，与矩量问题非唯一性等价，表述恰当。）

**未解决疑点**：无。

---

### 题 4 —— 2010 · Individual · #6

**题面核对**（<code>2010\Analysis and differential equations individual.pdf</code> 第 2 页）

> 原卷：<code>6. Consider the equation ẋ = −x + f(t,x), where |f(t,x)| ≤ φ(t)|x| for all (t,x) ∈ R×R, ∫^∞ φ(t)dt < ∞. Prove that every solution approaches zero as t→∞.</code>

讲义题面**逐字一致** ✔（$\int^\infty$ 未写下限也是原卷如此，讲义 §12.1 已如实标注）。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $\lvert\dot x\rvert\le(1+\varphi)\lvert x\rvert$ + Grönwall $\Rightarrow$ 解不爆破、可延拓到 $\mathbb R_+$ | **成立** | Grönwall 积分形式 + 解的延拓定理 |
| 2 | $\frac{d}{dt}\lvert x\rvert\le(\varphi(t)-1)\lvert x\rvert$（$x\neq0$ 处） | **成立** | $\frac{d}{dt}\lvert x\rvert=\frac{x\dot x}{\lvert x\rvert}$，$xf\le\lvert x\rvert\varphi\lvert x\rvert$ |
| 3 | 零点的处理（$\{t:x(t)=0\}$ 无内点 / 分段 Grönwall） | **成立**（论证可简化） | 其实**不必**引唯一性：由 $\lvert\dot x\rvert\le(1+\varphi)\lvert x\rvert$ 与 Grönwall，$x(t_1)=0\Rightarrow x\equiv0$ 于 $t\ge t_1$（无需 $f$ 对 $x$ 的 Lipschitz 条件） |
| 4 | 第二次 Grönwall（$\beta=\varphi-1$ 可取负值） | **成立** | Grönwall 允许 $\beta$ 变号 |
| 5 | $\lvert x(t)\rvert\le\lvert x(t_0)\rvert e^{\Phi}e^{-(t-t_0)}\to0$ | **成立** | 指数衰减 |
| 6 | 两个反例 | **成立** | 见下 |

**具体问题**：**未发现数学错误。**

- 讲义担心"$\varphi\ge0$ 未声明"其实**不必要**：由 $\lvert f(t,x)\rvert\le\varphi(t)\lvert x\rvert$ 对**一切** $x\in\mathbb R$ 成立，取 $x\neq0$ 即得 $\varphi(t)\ge0$ 自动成立。可补一句："（由条件对一切 $x$ 成立可知 $\varphi\ge0$。）"
- 两个反例均经独立验算：$\varphi\equiv3,f=3x\Rightarrow\dot x=2x\Rightarrow x(t)=x_0e^{2t}\to\infty$ ✔；$\varphi=1+\frac1{t+1},f=\varphi x\Rightarrow\dot x=\frac{x}{t+1}\Rightarrow x=C(t+1)\to\infty$ ✔。
- 可补一句更精确的收尾（非必须）：由 (4.2) 得 $\lvert x(t)\rvert\le\lvert x(t_0)\rvert e^{\Phi}e^{-(t-t_0)}$，故不仅趋零，而且是**指数**趋零，与讲义"衰减速率至少是指数的"一致。

**未解决疑点**：无。

---

### 题 5 —— 2013 · Individual · #2

**题面核对**（<code>2013\analysis2013(individual).pdf</code>）

> 原卷：<code>2. Let p(z) be a polynomial of degree d ≥ 2, with distinct roots a₁,…,a_d. Show that Σ_{i=1}^d 1/p'(a_i) = 0.</code>

讲义题面**逐字一致**（含 $d\ge2$）✔。讲义"预备"中"根互异 $\Rightarrow$ 单根 $\Rightarrow p'(a_i)\ne0$"成立 ✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $\frac1p$ 在 $a_i$ 的主部为 $\frac{1}{p'(a_i)(z-a_i)}$ | **成立** | 单零点留数（$\lim(z-a_i)/p(z)=1/p'(a_i)$） |
| 2 | $R=\frac1p-\sum_i\frac{1}{p'(a_i)(z-a_i)}$ 为整函数 | **成立** | 奇点全为可去奇点 |
| 3 | $R(z)=O(\lvert z\rvert^{-1})\to0$ $\Rightarrow R\equiv0$ | **成立** | Liouville 定理（有界整函数为常数；再取无穷远极限） |
| 4 | 乘 $z$ 取极限 $\Rightarrow S=0$，**用 $d\ge2$** | **成立** | 左端 $z/p(z)=O(\lvert z\rvert^{1-d})\to0$ 恰需 $d\ge2$ |
| 5 | 法二次数论证：$Q=1$ 但 $Q$ 首项 $cSz^{d-1}$ | **成立** | 多项式次数比较 |
| 6 | 法三留数总和，且 $d=1$ 反例 $-\frac1c\ne0$ | **成立** | 扩充复平面留数总和为 0；$\operatorname{Res}_\infty\frac1p=-\operatorname{Res}_{w=0}\big(\frac{1}{w^2}\frac{1}{p(1/w)}\big)$ |

**具体问题**：**未发现数学错误。** 随机多项式复算（脚本 [R5]）$d=2,3,4,6,8$ 时 $\sum 1/p'(a_i)$ 均为 $\lvert\cdot\rvert<10^{-14}$ ✔。

**未解决疑点**：无。

---

### 题 6 —— 2017 · Team · #5

**题面核对**（<code>2017\2017-team.pdf</code> 第 1 页 = 分析与 PDE 团体卷）

> 原卷：<code>5. In R^n, consider the Laplace equation u₁₁ + u₂₂ + … + u_nn = 0. Show that the equation is invariant under orthogonal transformation. Find all rotationally symmetric solutions to this equation.</code>

讲义题面**逐字一致**（把 PDF 连字符断行的 "rota-tionally" 还原为 "rotationally" 属正常排版还原，不构成改写）✔。"该 PDF 是当年 5 个科目的合卷、分析与 PDE 部分在第 1 页"的说明亦属实 ✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $\partial_iv=\sum_kO_{ki}\partial_ku(Ox)$；$\partial_i^2v=\sum_{k,l}O_{ki}O_{li}\partial_{kl}u$ | **成立** | 链式法则（$O$ 为常矩阵） |
| 2 | $\Delta v=\sum_{k,l}(OO^{\mathsf T})_{kl}\partial_{kl}u=\Delta u(Ox)$ | **成立** | $O$ 正交 $\Leftrightarrow OO^{\mathsf T}=I$ |
| 3 | $\Delta f(r)=f''+\frac{n-1}{r}f'=\frac1{r^{n-1}}\frac{d}{dr}(r^{n-1}f')$ | **成立** | 直接计算（脚本 [R6] 复核） |
| 4 | 径向 ODE 解：$a+br^{2-n}$（$n\ge3$）/ $a+b\log r$（$n=2$）/ $a+br$（$n=1$） | **成立** | 一阶线性 ODE |
| 5 | 若要求 $u$ 在 $\mathbb R^n$（含 0）上 $C^2$，则必为常数 | **成立** | 奇性 + 旋转不变 $\Rightarrow\nabla u(0)=0$，或让 $r^{n-1}f'(r)\equiv C$ 中 $r\to0$ |
| 6 | 基本解归一化：$-\Delta(\lvert x\rvert^{2-n})=(n-2)\omega_n\delta_0$ | **成立** | 散度定理算通量 $\int_{\partial B_\rho}\partial_\nu\lvert x\rvert^{2-n}d\sigma=(2-n)\omega_n$ 与 $\rho$ 无关 |

**具体问题**：**未发现数学错误。** 唯一可补的是：题面"Find all rotationally symmetric solutions"未指明定义域，讲义同时给出"含原点"与"$\mathbb R^n\setminus\{0\}$"两种读法的答案，处理恰当。

**未解决疑点**：无。


---

### 题 7 —— 2020 · Individual · #5

**题面核对**（<code>2020\Analysis&DifferentialEquations\analysis_and_differential_20.pdf</code>；官方解答在同目录 <code>analysis_and_differential_soln_20.pdf</code>）

> 原卷：<code>Problem 5. We consider the following ordinary differential equation: { x''(t)+x(t)+x(t)³ = 0, (x(0),x'(0)) = (x₀,0), } where x(t) takes values in R. Prove that for all x₀ ∈ R, the solution of the above system is periodic.</code>

讲义题面**逐字一致** ✔。（顺带核对：讲义称 2020 卷存在官方解答，属实 ✔。）

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | 能量守恒 $E=\frac12x'^2+\frac12x^2+\frac14x^4\equiv E_0$ | **成立** | 首次积分（自治系统） |
| 2 | $V$ 偶、$[0,\infty)$ 严格增 $\Rightarrow\{V\le E_0\}=[-x_0,x_0]$ $\Rightarrow$ 解有界、整体存在 | **成立** | 延拓定理 + $V\to\infty$（强制性） |
| 3 | 时间映射 $\Psi(\xi)=\int_\xi^{x_0}\frac{ds}{\sqrt{2(E_0-V(s))}}$ 在 $(-x_0,x_0]$ 连续严格递减、端点收敛 | **成立** | $E_0-V(s)\sim V'(x_0)(x_0-s)$，$V'(x_0)>0$，故 $s=x_0$ 处为 $1/2$ 次奇性、可积 |
| 4 | $\Psi(x(t))=t$ 于 $[0,t_*)$，且 $t_*=T_{1/2}$、$x(T_{1/2})=-x_0$、$x'(T_{1/2})=0$ | **成立，但宜补一句反证** | 见下 |
| 5 | 奇对称 $z(t)=-x(t-T_{1/2})$ + Picard–Lindelöf 唯一性 $\Rightarrow x(t+T)=x(t)$ | **成立** | 初值 $(-x_0,0)$ 相同 |
| 6 | $T=4\int_0^{x_0}\frac{ds}{\sqrt{2(E_0-V(s))}}$ 及大小振幅渐近 | **成立** | 偶性 + 尺度代换 |

**具体问题与修正文本**

第 4 步"关键：$t_*=T_{1/2}$，$x$ 不会'提前'停下或跑出 $(-x_0,x_0)$"是**对的**，但讲义只用了一句断言。建议在"由于 $\Psi$ 是严格递减的连续双射，由 (7.3) 得 $x(t)=\Psi^{-1}(t)$"之后、在断言 $x(T_{1/2})=-x_0$ 之前插入：

> 严格地说：由 (7.3) 知 $t=\Psi(x(t))<T_{1/2}$ 对一切 $t\in[0,t_*)$ 成立，故 $t_*\le T_{1/2}$。若 $t_*<T_{1/2}$，则取极限得 $x(t_*)=\Psi^{-1}(t_*)\in(-x_0,x_0)$，于是 $x'(t_*)=-\sqrt{2\big(E_0-V(x(t_*))\big)}<0$；由 $x'$ 的连续性，存在 $\delta>0$ 使 $x'<0$ 于 $(t_*,t_*+\delta)$，这与 $t_*$ 的定义矛盾。故 $t_*=T_{1/2}$，再由 $x$ 连续与 $\Psi^{-1}(t)\to-x_0\ (t\to T_{1/2}^-)$ 得 $x(T_{1/2})=-x_0$。

**数值复现**（脚本 [R7]，Gauss–Legendre 3000 点，代换 $s=x_0(1-u^2)$ 消端点奇性）：

| $x_0$ | 讲义 | 本次复算 |
|---|---|---|
| 0.01 | 6.28295 | **6.282950** |
| 0.1 | 6.2598 | **6.259762** |
| 0.5 | 5.7688 | **5.768846** |
| 1 | 4.7680 | **4.768022** |
| 10（$x_0T$） | 7.3629 | **7.362890** |
| 100（$x_0T$） | 7.4158 | **7.415759** |

渐近常数 $\sqrt2\,\Gamma(1/4)\Gamma(1/2)/\Gamma(3/4)=7.4162987$（讲义 7.4163 ✔）；$4\sqrt2\int_0^1du/\sqrt{1-u^4}=7.415683$ ✔。$2\pi=6.283185$，小振幅二阶公式 $2\pi(1-\frac38A^2)$ 给 $A=0.01$ 时 $6.282950$ ✔。

**未解决疑点**：无（第 4 步补一句后即为完整证明）。

---

### 题 8 —— 2018 · Individual · #6

**题面核对**（<code>2018\analysis2018-individual.pdf</code> 第 2 页）

> 原卷：<code>6. If u is a positive harmonic function on R^n \ {0} (n ≥ 2), then exist constants a ≥ 0, b ≥ 0 such that u(x) = a + b|x|^{2-n} for all x ∈ R^n \ {0}.</code>

讲义题面**逐字一致** ✔。讲义对 $n=2$ 时 $\lvert x\rvert^{0}\equiv1$ 使公式退化为"$u$ 为常数"的说明**正确**，且这确实是 $n=2$ 的真结论，属题面本身瑕疵而非求解缺陷 ✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $F(r)=\int_{\partial B_r}\partial_\nu u\,d\sigma$ 与 $r$ 无关；$A'(r)=\frac{n-1}{r}A(r)+F$ | **成立** | 散度定理（环域上 $\Delta u=0$） |
| 2 | $\bar u(r)=\frac{F}{(2-n)\omega_n}r^{2-n}+\frac{C}{\omega_n}$，正性 $\Rightarrow c_1,c_2\ge0$ | **成立** | 一阶线性 ODE + $r\to0,\infty$ 取极限；脚本 [R8] 用 $u=3+2\lvert x\rvert^{-1}$ 复核该式 ✔ |
| 3 | 环域 Harnack：$M(r)\le C_0\bar u(r)$，从而 $u=O(\lvert x\rvert^{2-n})$（$0$ 附近）、$O(1)$（$\infty$） | **成立** | Harnack 不等式（位似不变，常数只依赖 $n$）+ 最小值 $\le$ 平均值 |
| 4 | 引理 8.1（可去奇点）：条件 (a) 球面平均为零 + (b) $W=O(\lvert x\rvert^{2-n})$ $\Rightarrow$ 可去 | **结论成立**；**证明中两处瑕疵** | 见下 |
| 5 | 引理 8.2（无穷远，Kelvin 变换） | **成立**（一处书写瑕疵） | Kelvin 变换保调和 + 引理 8.1 |
| 6 | Liouville 收尾，$W\equiv0$ | **成立** | $\mathbb R^n$ 上有界调和函数为常数 |
| 7 | $n=2$ 单独处理：$F=0$、$\bar u\equiv c$、$W=u-c$ 有界、可去、Liouville | **成立** | 同上 + 有界调和函数在孤立奇点可去 |

**具体问题与修正文本**

**(A) (8.6) 差一个符号。** 原文由
$$\int_{\Omega_\epsilon}\big(W\Delta\varphi-\varphi\Delta W\big)dx=\int_{\partial\Omega_\epsilon}\big(W\partial_\nu\varphi-\varphi\partial_\nu W\big)d\sigma$$
并注意到"在 $\partial B_\epsilon$ 上 $\nu=-\hat x$"，却得到
$$\int_{\Omega_\epsilon}W\Delta\varphi\,dx=\int_{\partial B_\epsilon}\big(W\partial_r\varphi-\varphi\partial_rW\big)d\sigma .$$
由于 $\nu=-\hat x$ 意味着 $\partial_\nu=-\partial_r$，右端应为 **$-W\partial_r\varphi+\varphi\partial_rW$**。

**修正文本**：(8.6) 改为
$$\int_{\Omega_\epsilon}W\Delta\varphi\,dx=\int_{\partial B_\epsilon}\big(-W\,\partial_r\varphi+\varphi\,\partial_rW\big)d\sigma .$$
（用 $W\equiv1$ 检验：应得 $\int_{\Omega_\epsilon}\Delta\varphi=-\int_{\partial B_\epsilon}\partial_r\varphi$，与散度定理一致。）由于后面两项都是取绝对值估计，**这个符号错误不改变最终结论**，但必须改正。

**(B) 第 4 步 (a) 的论证无效。** 原文：

> 由条件 (a)，$\int_{\partial B_\epsilon}W\,d\sigma=0$，故可把 $\nabla\varphi(x)$ 换成 $\nabla\varphi(0)$：…（因为 $\int_{\partial B_\epsilon}W(\nabla\varphi(0)\cdot\hat x)\,d\sigma=0$——这是 $W$ 乘一个常向量场与 $\hat x$ 的内积，而 $\int_{\partial B_\epsilon}W=0$ 使该项逐分量消失）。

**这一步是错的**：球面平均为零只给出**零阶矩**为零，**一阶矩** $\int_{\partial B_\epsilon}Wx_i\,d\sigma$ 一般不为零。反例：取 $W(x)=x_1$（在 $\mathbb R^n\setminus\{0\}$ 上调和），它满足 (a)（奇函数）与 (b)（$\lvert W\rvert=O(1)=O(\lvert x\rvert^{2-n})$，$n\ge3$），但 $\int_{\partial B_\epsilon}Wx_1\,d\sigma=\frac{\omega_n}{n}\epsilon^{n+1}\ne0$。

**修正文本（替换该段的整段论证）**：

> **(a) 第一项 $\int_{\partial B_\epsilon}W\partial_r\varphi\,d\sigma\to0$。** 由条件 (b) 有 $\lvert W(x)\rvert\le C_W\lvert x\rvert^{2-n}$ 于 $\lvert x\rvert=\epsilon$，而 $\lvert\partial_r\varphi\rvert\le\lVert\nabla\varphi\rVert_\infty$，故直接估计
> $$\Big|\int_{\partial B_\epsilon}W\,\partial_r\varphi\,d\sigma\Big|\le\lVert\nabla\varphi\rVert_\infty\int_{\partial B_\epsilon}\lvert W\rvert\,d\sigma
> \le\lVert\nabla\varphi\rVert_\infty C_W\,\omega_n\epsilon^{2-n}\cdot\epsilon^{n-1}
> =\lVert\nabla\varphi\rVert_\infty C_W\omega_n\,\epsilon\xrightarrow[\epsilon\to0]{}0 .$$
> （此处**不需要**条件 (a)，也不需要把 $\nabla\varphi(x)$ 换成 $\nabla\varphi(0)$。）

**(C) 第 5 步 (i) 的书写瑕疵。** 原文把 $\int_{\partial B_s}\widetilde W\,d\sigma$ 的系数写成 $\frac{s}{\omega_n}$ 后乘 0；按 $\int_{S^{n-1}}W(\omega/s)d\sigma=s^{n-1}\int_{\partial B_{1/s}}W\,d\sigma$，正确系数是 $s\cdot s^{n-1}=s^{n}$。因为 $\int_{\partial B_r}W\,d\sigma=0$，**结果同样是 0**，但系数应更正为 $s^{n}$（或直接写"由假设 $\int_{\partial B_{1/s}}W\,d\sigma=0$ 得积分为 0"）。

另可补一句使第 4 步 (b) 更严谨：原文写作
$\int_{\partial B_\epsilon}\varphi\,\partial_rW\,d\sigma=\int_{\partial B_\epsilon}(\varphi(x)-\varphi(0))\partial_rW\,d\sigma\le\dots$，
中间一步应写成 $\Big|\int\cdots\Big|\le\dots$（被积函数可变号）。

**未解决疑点**：讲义 §12.1 提到"环域 Harnack 只给了论证思路、未写有限覆盖细节"。作为竞赛讲义可接受（标准结论：固定环域上的 Harnack 常数经位似不变性推广），不构成错误。

---

### 题 9 —— 2025 · Individual · #2

**题面核对**（<code>2025\analysis.pdf</code>）

> 原卷：<code>(1). Prove that for n ≥ 3, there exists a constant C > 0 such that ∫_{R^n} u²/|x|² dx ≤ C ∫_{R^n} |∇u|² dx, ∀u ∈ H¹(R^n); (2). Prove that the optimal constant C in (1) is 4/(n−2)².</code>

讲义题面**逐字一致** ✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $\nabla\cdot(x/\lvert x\rvert^2)=(n-2)\lvert x\rvert^{-2}$ | **成立** | 直接求导 |
| 2 | 环域散度定理 + 内边界项 $O(\delta^{n-2})\to0$（$n\ge3$） | **成立** | 散度定理；$n=2$ 时该项为 $O(1)$，正是二维失效机制 |
| 3 | 由 (9.2) 取绝对值 + Cauchy–Schwarz 得 $\int u^2/\lvert x\rvert^2\le\frac4{(n-2)^2}\int\lvert\nabla u\rvert^2$ | **成立** | Cauchy–Schwarz（$L^2$） |
| 4 | 由 $C_c^\infty$ 稠密 + Fatou 推广到 $H^1$ | **成立** | $C_c^\infty(\mathbb R^n)\subset H^1$ 稠密 + Fatou 引理 |
| 5 | 最佳性：$u_\epsilon=\lvert x\rvert^{-\alpha_\epsilon}\eta$，$\alpha_\epsilon=\frac{n-2}{2}-\epsilon$ | **成立**（函数族构造正确） | $u_\epsilon\in H^1$；$\int_{B_1}u_\epsilon^2/\lvert x\rvert^2=\frac{\omega_n}{2\epsilon}$、$\int_{B_1}\lvert\nabla u_\epsilon\rvert^2=\alpha_\epsilon^2\frac{\omega_n}{2\epsilon}$ |
| 6 | 比值 $\to\frac1{\alpha_0^2}=\frac4{(n-2)^2}$ | **成立** | $O(1)$ 项被 $\frac1{2\epsilon}$ 项吞掉 |
| 7 | "数值核对"表（$\epsilon=0.2,\dots,0.01$ 给 11.111 … 4.165） | **❌ 不成立** | 见下 |

**具体问题与修正文本**

表中 5 个数**恰好等于** $1/\alpha_\epsilon^2$（$=1/0.3^2,\,1/0.4^2,\dots$），也就是说它们是**只在 $B_1$ 上的比值**（在 $B_1$ 上三个被积函数同为 $r^{2\epsilon-1}$，比值精确等于 $1/\alpha_\epsilon^2$），**不是**函数族在整个 $\mathbb R^n$ 上的真实比值。差值并非小数：截断函数在 $1<\lvert x\rvert<2$ 上的梯度项是 $O(1)$ 量级，而 $\int_{B_1}u_\epsilon^2/\lvert x\rvert^2=\frac{\omega_n}{2\epsilon}$ 只有 $\epsilon$ 小时才占主导。

**独立复算**（脚本 [R9]，取讲义所述的光滑截断 $\eta$：$0\le\eta\le1$、$\eta\equiv1$ 于 $\lvert x\rvert\le1$、$\eta\equiv0$ 于 $\lvert x\rvert\ge2$；$B_1$ 段用解析值 $1/(2\epsilon)$，$[1,2]$ 段用 6000 点 Gauss–Legendre）：

| $\epsilon$ | $\alpha_\epsilon$ | 只在 $B_1$ 上 $=1/\alpha_\epsilon^2$（= 讲义表格） | **完整比值（$\mathbb R^n$）** |
|---|---|---|---|
| 0.2 | 0.30 | 11.1111 | **0.81811** |
| 0.1 | 0.40 | 6.2500 | **1.35359** |
| 0.05 | 0.45 | 4.9383 | **2.01997** |
| 0.02 | 0.48 | 4.3403 | **2.87202** |
| 0.01 | 0.49 | 4.1649 | **3.34313** |
| $10^{-3}$ | 0.499 | 4.0160 | **3.92288** |
| $10^{-4}$ | 0.4999 | 4.0016 | **3.99215** |

**结论**：讲义"$\epsilon=0.2,0.1,0.05,0.02,0.01$ 时比值分别为 $11.111,6.250,4.938,4.340,4.165$，单调下降趋向 $4$"是**错的**——真实比值从 $0.818$ **单调上升**趋向 $4$（符合 $\le4$ 的不等式方向），且只有 $\epsilon\lesssim10^{-3}$ 才看得出极限。这个错误不影响"$C_{\rm opt}=\frac4{(n-2)^2}$"的结论（第 6 步的比值极限推导是对的），但"所有数值均由脚本独立验算"的声明在本题上不成立。

**修正文本（替换该数值核对段落）**：

> （数值核对，$n=3$，$C_{\rm opt}=4$）：取 $\eta$ 为上述光滑截断。$B_1$ 段有闭式 $\int_{B_1}u_\epsilon^2/\lvert x\rvert^2=\frac{\omega_n}{2\epsilon}$，$[1,2]$ 段用 Gauss–Legendre 6000 点。$\epsilon=0.2,0.1,0.05,0.02,0.01,10^{-3},10^{-4}$ 时**完整比值**分别为 $0.818,1.354,2.020,2.872,3.343,3.923,3.992$，单调上升趋于 $4$ ✔。（注意：若只在 $B_1$ 上算比值，会得到恰好等于 $1/\alpha_\epsilon^2$ 的数列 $11.111,6.250,\dots$——那**不是**本函数族的真实比值。）

**未解决疑点**：无（解析部分完整；§12.1 关于"稠密性只给思路"的自我披露可接受）。

---

### 题 10 —— 2026 · Individual · #1

**题面核对**：**无法回原卷核对。** 已核实 <code>sources/prelim\</code> 下只有 2010–2025（17 个年份目录 + 1 个无关 png），**确实没有 2026**，讲义 §0.4/§12.1 的声明属实。题库文本（<code>2026_2026_analysis</code>，$n=1$）完整可读：

> <code>For any n ∈ N, define I_n := (1/n!)∫_{−π/2}^{π/2} (π²/4 − t²)^n cos t dt. (a) Prove I_{n+1} = 2(2n+1)I_n − π²I_{n−1}. (b) Show that π² ∉ Q.</code>

讲义转写与之语义一致（仅把 PDF 私用区字符还原为括号），✔。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $f_n=n!I_n=\int_{-a}^a(a^2-t^2)^n\cos t\,dt$，$a=\pi/2$ | **成立** | 定义 |
| 2 | 一次分部积分：$f_n=2n g_{n-1}$，$g_m=\int t(a^2-t^2)^m\sin t\,dt$ | **成立** | 分部积分，边界项因 $a^2-t^2=0$ 消失 |
| 3 | 二次分部积分（$v=\sin t-t\cos t$）：$g_m=2mg_{m-1}-2m\int t^2(a^2-t^2)^{m-1}\cos t$ | **成立** | $v'=t\sin t$ 已验证 ✔ |
| 4 | 拆 $t^2=a^2-(a^2-t^2)$，指标回代得 $f_{m+1}=2(m+1)(2m+1)f_m-m(m+1)\pi^2f_{m-1}$ | **成立** | 代数；脚本 [R10] 残差 $\le10^{-11}$ |
| 5 | 除以 $(m+1)!$ 得 $I_{n+1}=2(2n+1)I_n-\pi^2I_{n-1}$（$n\ge1$） | **成立**，且"$n\ge1$"的注记正确 | $I_{-1}$ 无定义，题面"for any $n\in\mathbb N$"严格说应为 $n\ge1$ |
| 6 | $I_n>0$、$0<I_n\le\frac{2}{n!}(\pi^2/4)^n$ | **成立** | 被积函数严格正；$(\pi^2/4-t^2)^n\le(\pi^2/4)^n$ |
| 7 | $J_n=q^nI_n$ 为**正整数**（归纳） | **成立** | 递推式分母被 $q^{n+1}$ 吸收；$J_0=2$、$J_1=4q$ |
| 8 | $0<J_n\le\frac2{n!}(p/4)^n\to0$，与 $J_n\ge1$ 矛盾 | **成立** | 比值判别法（$c^n/n!\to0$） |

**具体问题**：**未发现数学错误。**

**数值复现**（脚本 [R10]，Gauss–Legendre 4000 点）：

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 讲义 | 2 | 4 | 4.260791 | 3.129494 | 1.760598 | 0.803887 | 0.309105 |
| 复算 | 2.000000000 | 4.000000000 | 4.260791198 | 3.129494374 | 1.760597676 | 0.803886720 | 0.309105262 |

递推残差（用 $I$）：$-3.6\times10^{-15},\,7.1\times10^{-15},\,7.1\times10^{-15},\,7.1\times10^{-15},\,0,\,8.9\times10^{-16}$；$I_2=24-2\pi^2$、$I_3=240-24\pi^2$、$I_4=3360-360\pi^2+2\pi^4$ 全部吻合 ✔。

**未解决疑点**：题面无法回原卷复核（唯一来源是题库 txt）。若日后拿到 2026 原卷，应核对 (a) 是否要求 $n\ge0$（那样递推式需另作说明）。


---

## 3. 统计

| 裁定 | 题数 | 题号 |
|---|---|---|
| **VERIFIED** | **7** | 1、3、4、5、6、7、10 |
| **MINOR-FIX** | **3** | 2、8、9 |
| **SERIOUS-ERROR** | **0** | —— |
| **UNVERIFIED** | **0** | —— |

- **错误率（至少有一处需修正的题）**：$3/10 = \mathbf{30\%}$。
- **结论错误的题**：$0/10$ —— 10 道题的**最终答案全部正确**。
- **含"可致论证失效"错误的题**：$1/10$（题 2 法三：一条被明确断言为真的等式 $\oint=0$ 实为假；因其非主解答，未升级为 SERIOUS-ERROR）。
- **数值声明不可复现**：$1/10$（题 9 的最佳性核对表）。
- **题面核对结果**：9 道可核对的原卷题面**全部逐字正确、无缺失、无改写**（0 处题面错误）；1 道（题 10）因原卷缺失**无法核对**。

---

## 4. 给使用者的提醒：哪些内容不可信、必须自己重做

**必须重做 / 不要照抄：**

1. **题 2 的"法三：围道积分"整段——不可信，必须删除或按 §2 的修正文本重写。** 它的留数用了错误的分支、并把一个真实值为 $2\pi^3$ 的围道积分说成 $0$，还附带一个用错被积函数的副产品。讲义 §12.3 自称"已经改正"，实际**并未改对**。（题 2 的**答案 $I=0$ 与法一、法二**是可信的，可放心使用；法二只需删掉控制函数里多余的 $1/(1+x^2)$。）
2. **题 9 的数值核对表——不可信，必须按 §2 的表重算。** 表里的数不是该函数族的真实比值；照它理解"$\epsilon=0.2$ 时已接近最优"会得到完全错误的直觉（真实值 $0.818$，离 $4$ 还很远，且是**上升**而非下降趋于 $4$）。题 9 的**解析证明与最佳常数**是可信的。
3. **题 8 的引理 8.1 证明（式 (8.6) 与第 4 步 (a)）——不要照抄。** 一处符号错误 + 一处无效论证；结论正确，但请按 §2 的修正文本写。题 8 其余部分（第 1–3 步、引理 8.2、Liouville 收尾、$n=2$ 情形）可信。

**可以放心使用（但建议按 §2 补一句）：**

4. **题 7 第 4 步** "$t_*=T_{1/2}$"：方向正确但过于简略，考场上建议补上 §2 给出的两行反证。
5. **题 4（2010 #6）**：可补"由条件对一切 $x$ 成立可知 $\varphi\ge0$"，以及"$\lvert\dot x\rvert\le(1+\varphi)\lvert x\rvert$ + Grönwall 即可断言 $x(t_1)=0\Rightarrow x\equiv0$，无需 Lipschitz 唯一性"。
6. **外围内容**：见 §5 第 (B) 组的 6 条——尤其是 §0.3/§12.2/§C.4 关于"2021 #2 = 2022 #4 = 2026 #4 原题三度出现"的说法**是错的**（2021 #2 是另一道题），以及 §C.7 关于 2014 两卷第 3 题"是同一道题"的说法**是错的**。这些不影响 10 道题的解答，但会影响你按"重复题"做的去重统计。

**结论**：讲义可以作为备考主干使用（10 道题的最终结论全对、题面全对），但**上述 3 处必须自己重做**，且不能引用讲义 §12.3 的"自我修复声明"作为法三正确的依据。

---

## 5. 存疑清单

### (A) 与 10 道题直接相关

| 题号 | 存疑内容 | 我的判定 | 建议 |
|---|---|---|---|
| 2 | 法三的两处错误（分支、$\oint=0$） | **已判定为错误**，修正文本见 §2 | 删除或改用修正文本 |
| 2 | 法二控制函数多一个 $1/(1+x^2)$ | **已判定为错误**（控制不等式失效） | 按 §2 删除该因子 |
| 8 | (8.6) 符号、第 4 步 (a) 的"$\int W\hat x=0$"、第 5 步 (i) 的 $s^n$ 系数 | **已判定为错误/瑕疵**（均不改变结论） | 按 §2 改写 |
| 9 | 最佳性数值表 | **已判定为不可复现**（数值为 $1/\alpha_\epsilon^2$） | 按 §2 换表 |
| 7 | 第 4 步 $t_*=T_{1/2}$ 的措辞 | **成立但偏紧** | 补两行反证 |
| 10 | 题面无法回原卷核对；(a) 中 $n$ 的取值范围 | 讲义已如实声明；$n\ge1$ 的注记正确 | 拿到 2026 原卷后复核 |
| 4 | 题面 $\int^\infty\varphi$ 未写下限、$f$ 未声明正则性 | 讲义处理恰当（尾部积分读法、默认连续） | 无需改动 |

### (B) 讲义外围内容中我发现的错误（不属于 10 道题，但会影响使用）

以下 6 条均**已用题库/原卷证实**，建议一并勘误：

1. **§0.3、题 3 同类题、§12.2、§C.4："2021 Individual #2 = 2022 Individual #4 = 2026 Individual #4 是同一道题（原题三度出现）" —— ❌ 错误。**
   已核对原卷 <code>2021\ExamPaper_21S\</code> 与 <code>Solution_21S\</code>：**2021 Individual #2 是"设 $X\subset C[0,1]$ 是有限维线性子空间，若 $\{f_k\}\subset X$ 逐点收敛则一致收敛"**，与"$C[0,1]$ 中由多项式组成的闭子空间必有限维"（2022 #4、2026 #4）**不是同一道题**。正确表述：该题在 **2022、2026 出现过两次**（不是三次）。
2. **§C.7："2014 Individual #3 与 2014 Team #3 是同一道题" —— ❌ 错误。**
   已核对两卷 PDF：2014 Individual #3 是"两环域间存在共形映射 $\Rightarrow \frac{r_2}{r_1}=\frac{\rho_2}{\rho_1}$"；2014 Team #3 才是"环域上有界解析函数 $F=z^\alpha f$"。二者不同，去重时不应合并。
3. **§12.2 与 §C.1："2020 Individual 第 3 题混入了第 4 题" —— ⚠️ 对当前题库快照（757 条）已不成立。**
   当前 <code>2020 individual 3</code>（334 字符）与 <code>4</code>（170 字符）各自完整、互不包含。若该缺陷存在于早期快照，应注明"快照编号"，否则会误导读者。
4. **§0 头部与附录 B 的题库条数自相矛盾。** 文件头写"截至本讲义定稿为 751 条记录"，附录 B/C.6 写"早期 757 条/156 道 → 定稿 751 条/155 道"。**本次实测该文件为 757 条、其中 Analysis & PDE 155 道**；即"757 条"配的是"155 道"，"156 道"的配对在当前文件中不存在。建议统一为实测值。
5. **题 6 同类题中 2019 Individual #3 的题面转写有误。** 原卷（及 <code>Analysis2019-individual.tex</code>）是 $\lim_{\lvert x\rvert\to\infty}\frac{\lvert f(x)\rvert}{\ln\lvert x\rvert}=0$（**除法**），讲义写成 $\lim\lvert f(x)\rvert\ln\lvert x\rvert=0$（**乘法**，强得多且使结论平凡）。
6. **§C.4："2015 Individual #5 与 Team #5 是同一年两卷的同一道 Fredholm 题" —— ⚠️ 表述过强。** 二者是**不同**的题：Individual #5 是 $QT=\mathrm{Id}-S_1,\ TQ=\mathrm{Id}-S_2$（二择一型）；Team #5 是 $T+S$（紧扰动型）。同源但不同题。

### (C) 我确实没有能力判定 / 没有做的

1. **题 10 的题面**无法回原卷核对（F 盘无 2026 卷，属环境事实）。
2. 讲义中大量"同类题"引用的**逐题正确性**我只抽查了约 15 条（2013 #1/#4/#5、2013 Team #3、2014 #4/#5、2014 Team #3/#5/#6、2015 Team #1、2016 #2/#4(2)、2016 Team #3、2017 #2/#6、2019 #2/#3/#4、2020 #1/#2、2021 #2/#4、2022 #4/#5/#6、2025 #1/#3、2011 Team #1/#2/#6、2012 Team 等），**其余未逐条核对**；上面 (B) 只列出已被证伪的几条。
3. 讲义 §11 的"时间分配""刷题顺序"属主观建议，未作评判。
4. 讲义 §12.2 中"放弃某题"的**取舍理由**（如"名额已满""篇幅预算不匹配"）属主观，未作评判；其中涉及题面残缺的具体断言我只核了 2010、2012 Team、2014 Team、2019、2020 五处。

---

## 附：本次审稿的复算与核对产物

| 文件 | 内容 |
|---|---|
| <code>/scripts/referee_verify.py</code> | **全部数值结论的一键复算脚本**（题 1–10 共 10 组，含题 2 法三 keyhole 的数值围道积分、题 9 真实比值表） |
| <code>/scripts/ref_pdf_dump.py</code> → <code>/archive/work/ref_pdf_dump.txt</code> | 10 道题对应原卷 PDF 的文本转储（题面逐字核对的依据） |
| <code>/scripts/ref_pdf_dump2.py</code>、<code>ref_pdf_2021b.py</code> → <code>/archive/work/ref_pdf_dump2.txt</code>、<code>ref_pdf_2021.txt</code> | 2014/2016/2019/2021 卷 PDF 转储（用于核对"同类题"与"重复出题"的断言） |
| <code>/scripts/ref_probe2/6/7/8.py</code> | 题库检索脚本（提取 10 道题原文、核对被引用的其他题目、核对题库条数与边界粘连断言） |

*（本报告所有数值结论均可由上述脚本复跑得到；所有"题面一致"的判定均基于 <code>F:</code> 盘原卷 PDF 的 PyMuPDF 文本抽取，无一处仅凭题库文本推断；题 10 因原卷缺失，明确标注为"无法核对"。被审阅的报告 <code>solutions_analysis.md</code> 未被修改。）*
