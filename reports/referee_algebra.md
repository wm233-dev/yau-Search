# 对抗性审稿报告：`reports/solutions_algebra.md`

**审稿人角色**：referee（对抗性）。默认假设"有错"，对每一步追问依据的定理、条件是否满足、有无反例、边界情形（$p=2$、$n=1$、退化、空集）是否处理。
**被审对象**：`reports/solutions_algebra.md`（1134 行，10 道丘成桐大学生数学竞赛「代数与数论」真题详解）。**本报告不修改被审文件**。

---

## 0. 数据口径与复核手段（务必先读）

| 项目 | 本报告采用的口径 / 手段 |
|---|---|
| 题库快照 | `data/problems_full.json`，**当前共 757 条**；其中 `subject == "Algebra & Number Theory"` 的为 **149 条**（讲义正文写"150 条"，见 §3.5；年份范围 2010–2026，共 **17** 个年份，这条与讲义一致） |
| 原卷 PDF | `sources/prelim`（只读），含 2010–**2025** 共 16 个年份目录，**无 2026 目录**；官方解答 PDF 只存在于 `2020 / 2021 / 2022` 三年 |
| 题面核对 | 用 PyMuPDF 从原卷 PDF 逐字提取（`_extract_pdfs.py` / `_extract2.py`），与讲义题面**逐句比对**；题 10（2026）无原卷可查，只做到 JSON 级比对 |
| 数值/穷举复核 | 全部由本报告附带的脚本产生，**可复跑**：`checkA.py`（题 1,2,4,5）、`checkB.py`（题 3,6,7,9,10）、`checkC.py`（题 8 + 元数据）、`checkD.py`（交叉引用/抽取残缺） |
| 复跑命令 | 在 `` 下：`python scripts/verification/checkA.py`（checkB/checkC/checkD 同理）；PDF 提取：`$env:PYTHONPATH='sources/pylibs'; python scripts/verification/_extract_pdfs.py` |
| 无第三方库 | 只用 Python 标准库（`fractions` / `math` / `itertools`），**未安装任何包**（sympy 不可用，故所有代数验证均为手写精确算术） |

**审稿结论的力度声明**：本报告中所有"已验证"的断言都有脚本输出支撑；所有"成立/不成立"的判定都给出依据的定理或反例。凡我无法判定的，一律写进 §5 存疑清单，不凑数。

---

## 1. 总体裁定表

| 题号 | 出处 | 题面是否正确（对原卷） | 结论是否正确 | 证明是否完整 | 裁定 | 一句话理由 |
|---|---|---|---|---|---|---|
| 题 1 | 2010 ind №1 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | 取 $B$ 的特征子空间 + $A(W)\subseteq W$ 一行推导无误；$[A,B^k]=kB^k$、$\mathrm{tr}(B^k)=0\Rightarrow B$ 幂零亦正确（随机整数矩阵复算通过） |
| 题 2 | 2012 ind №1 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **MINOR-FIX** | 主证明（Eisenstein@3）无误；但补充说明"模约化这条路会失败"**是错的**——$f \bmod 11$ 不可约，模 11 约化本身就是一条完整证明 |
| 题 3 | 2018 ind №3 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | Sylow 计数、$p^2$ 阶群交换、$\mathrm{Aut}(\mathbb Z/11)$ 阶 10 三步链无懈可击（只有 "Langrange" 拼写笔误） |
| 题 4 | 2013 ind №1 | ✅ 与 PDF 逐字一致（含 160 分制、15+5 分） | ✅ | ✅ | **VERIFIED** | $|\mathrm{Aut}(D_{26})|=156$ 由穷举 $D_{26}\to D_{26}$ 全部生成元像独立确认；半直积分类与 Hol 乘法公式正确 |
| 题 5 | 2016 team №3 | ✅ 与 PDF 一致 | ✅ | ⚠️ 有一处论证缺口 | **MINOR-FIX** | 10 个子域、10 个不动域、全部包含关系经精确算术**逐项验证通过**；但 $\sigma$（$\alpha\mapsto i/\alpha$）存在性的理由只排除了线性因子，不足以说明 $\mathbb Q(i)$ 上不可约 |
| 题 6 | 2017 ind №2 | ✅ 与 PDF 逐字一致 | ✅ | ✅ | **VERIFIED** | Fitting 分解与唯一性在 16 个小交换群、其全部内同态（最多 1024 个）上穷举验证，含"唯一性"本身 |
| 题 7 | 2019 ind №5 | ✅ 与 PDF 逐字一致 | ✅ | ⚠️ $p=2$ 处理由不成立 | **MINOR-FIX** | 三问结论与 $p\le 3000$ 全素数数值一致；但第 3 问对 $p=2$ 用了只对奇素数成立的二次互反形式，且 Binet 的假设写成 $\mathrm{char}\ne2$ 却在 $p=2$ 使用 |
| 题 8 | 2022 ind №5 | ✅ 与 PDF 逐字一致，且与官方解答四问答案一致 | ✅ | ✅ | **VERIFIED** | Eisenstein、$\mathrm{Tr}=p$、$\mathcal N=p$、$\mathrm{disc}=\pm p^{p-2}$、(d) 的迹恒等式与 $a_0$ 归约全部精确复算通过 |
| 题 9 | 2014 ind №3 | ✅ 与 PDF 一致（5+7+8 分） | ✅ | ✅ | **VERIFIED** | 整数解穷举到 $y\le 2\times10^6$ 无解；模 $p^n$ 可解性与 $N_a\in\{p-1,p+1\}$ 逐素数验证；递降恒等式与 $T^2=-\mathrm{id}$ 全检 |
| 题 10 | 2026 ind №2 | ⚠️ **无法对原卷复核**（本地无 2026 卷），仅与 JSON 逐句一致 | ✅ | ✅ | **MINOR-FIX** | 主证明经 80 个素数精确核对无误；但**附录 B 公式卡把点数写成 $p-\sum\chi_2(x^3+1)$，符号写反**，与正文 $N_p=p+T$ 自相矛盾 |

**裁定统计见 §3。** 一句话总体判断：**被审讲义的 10 道题没有一道结论错误、没有一道主证明失效**；存在 4 处"必须改掉再用"的问题（题 2 的补充说明、题 5 的 $\sigma$ 论证、题 7 的 $p=2$ 理由、题 10 的附录公式），以及若干排版/措辞瑕疵。

---

## 2. 逐题详审

### 题 1｜2010 / Algebra, Number Theory and Combinatorics / Individual / 第 1 题

**题面核对**：原卷 `2010\AlgebraNumberTheory-individual.pdf` 第 1 题："Let V be a finite dimensional complex vector space. Let A, B be two linear endomorphisms of V satisfying AB − BA = B. Prove that there is a common eigenvector for A and B." —— 与讲义题面**逐字一致**。讲义出处行称"6 题选 5 题作答"亦与原卷 "(Please select 5 problems to solve)" 及原卷确有 6 题一致。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | 取 $B$ 的特征值 $\lambda$，置 $W=\ker(B-\lambda I)\ne0$ | 成立 | $\mathbb C$ 代数闭（代数基本定理）+ 有限维非零空间上算子必有特征值。注：$B=0$ 时 $W=V\ne0$，论证照旧 |
| 2 | $A(W)\subseteq W$：由 $AB=BA+B$ 得 $\lambda Aw=B(Aw)+\lambda w$ | 成立 | 纯算子恒等式，仅用 $Bw=\lambda w$；推出 $B(Aw-w)=\lambda(Aw-w)$，故 $Aw-w\in W$，$Aw\in W$ |
| 3 | 在 $W$ 上取 $A$ 的特征向量 | 成立 | $W$ 有限维、非零、$\mathbb C$ 代数闭；$W$ 同时 $A$-不变与 $B$-不变 |
| 4 | 点评：$[A,B^k]=kB^k$ | 成立 | Leibniz 型公式 $[A,B^k]=\sum_{i=0}^{k-1}B^i[A,B]B^{k-1-i}$，代入 $[A,B]=B$ |
| 5 | 点评：$\mathrm{tr}(B^k)=0\ \forall k\ge1\Rightarrow B$ 幂零 | 成立 | $\mathrm{tr}(XY)=\mathrm{tr}(YX)$ ⇒ 幂和全零；Newton 恒等式 ⇒ 初等对称多项式全零 ⇒ 特征多项式 $=t^n$。**条件**：$\mathrm{char}=0$（题设在 $\mathbb C$ 上），讲义 §4.3 第 6 条已如实说明 |

**我发现的具体问题**：无数学问题。
（可选润色，非错误）第 83 行"由 $AB-BA=B$ 得 $AB=BA+B$，于是作为算子等式 $AB=BA+B$"重复了同一句话，可删去后半句。

**未解决疑点**：无。

---

### 题 2｜2012 / Algebra and Number Theory / Individual / 第 1 题

**题面核对**：原卷 `2012\Algebra2012Individual.pdf` 第 1 题与讲义题面**逐字一致**（$x^6+30x^5-15x^3+6x-120$，非首项系数为 $30,0,-15,0,6,-120$）。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $\gcd(30,15,6,120)=3$ ⇒ 唯一可能素数 $p=3$ | 成立 | 逐项整除（脚本 `checkA.py` 打印：gcd = 3）；$p=2\nmid 15$、$p=5\nmid 6$、$p\ge7$ 不可能 |
| 2 | Eisenstein@3 三条件（首项不被 3 整除；全部非首项系数被 3 整除；$9\nmid -120$） | 成立 | 脚本逐条输出 True/True/True |
| 3 | Gauss 引理回到 $\mathbb Q[x]$ | 成立 | 本原多项式在 $\mathbb Z[x]$ 不可约 ⟺ 在 $\mathbb Q[x]$ 不可约（题目要的正是"不能写成两个正次数有理系数多项式之积"） |
| 4 | 补充说明：$f \bmod 2$、$\bmod 5$、$\bmod 7$ 均可约 | 成立 | 复算：$\bmod 2$ 为 $x^3(x+1)(x^2+x+1)$；$\bmod 5$ 为 $x(x+1)(x^4-x^3+x^2-x+1)$；$\bmod 7$ 有根 $x=1$（$1+2+6+6+6=21\equiv0$）。三条全部正确 |
| 5 | 补充说明："**常用的『找一个模 $p$ 不可约的约化』这条路在本例中会失败**" | **不成立（反例）** | 见下 |

**我发现的具体问题（含修正文本）**

**问题 2-1（实质错误，必须改）**：讲义称模约化路线"在本例中会失败"。这是**错的**：用 Rabin 不可约判别法（`checkA.py`）复算得
$p\le 97$ 中使 $f \bmod p$ 不可约的素数 = $\{11,\ 53,\ 59,\ 79,\ 97\}$，
其中 $f\equiv x^6+8x^5+7x^3+6x+1 \pmod{11}$（已复算：常数项 1、$x$ 系数 6、$x^3$ 系数 7、$x^5$ 系数 8，且 $a=0,\dots,10$ 处取值 $1,1,4,10,1,6,6,9,9,5,3$ 全非零）。因此"$f \bmod 11$ 不可约 + Gauss 引理"本身就是一条完全有效、且更省事的证明路线。讲义这一句会误导读者以为模约化必然走不通。

**修正文本（替换第 149 行整段）**：

> 也就是说，**在最小的几个素数上模约化不可行**：$p=3$ 时 $f\equiv x^6$；$p=2,5,7$ 时 $f$ 都可约（见上）。但这条路并非走不通——$p=11$ 时 $f\equiv x^6+8x^5+7x^3+6x+1$ 在 $\mathbb F_{11}$ 上不可约（$a=0,\dots,10$ 处均不为零，且无二次、三次因式），故"模 11 约化 + Gauss 引理"同样是一条完整证明。本题的"机关"其实是**效率**：直接算非首项系数的公因数 $\gcd=3$，一步就锁定了 Eisenstein 素数，比逐个试模约化快得多。

**未解决疑点**：无（Eisenstein 路线本身完全正确）。

---

### 题 3｜2018 / Algebra and Number Theory / Individual / 第 3 题

**题面核对**：原卷 `2018\algebra2018-individual.pdf`："Problem 3 (20 points). Prove that every group of order 99 is abelian." 与讲义**一致**；讲义出处行"5 题 100 分"亦与原卷 "This test has 5 problems and is worth 100 points" 一致。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $n_{11}\equiv1\pmod{11}$，$n_{11}\mid9$ ⇒ $n_{11}=1$ ⇒ $P\trianglelefteq G$ | 成立 | Sylow 第三定理（$n_{11}\mid |G|/11=9$）；复算：$\{1,3,9\}$ 中 $\equiv1\bmod11$ 的只有 1 |
| 2 | 引理：$p^2$ 阶群交换 | 成立 | 类方程：$|Z(H)|=1$ 时 $p^2\equiv1\pmod p$ 矛盾 ⇒ $|Z(H)|=p$ ⇒ $H/Z(H)$ 循环 ⇒ $H$ 交换（标准引理） |
| 3 | $\mathrm{Aut}(P)\cong(\mathbb Z/11)^\times$ 阶 10；$|\mathrm{Im}\,\varphi|\mid\gcd(9,10)=1$ ⇒ 作用平凡 | 成立 | Lagrange + 同态基本定理；复算 gcd(9,10)=1 |
| 4 | $G\cong P\times Q$ 且 $P,Q$ 交换 ⇒ $G$ 交换；分类为 $\mathbb Z/99$、$\mathbb Z/33\times\mathbb Z/3$ | 成立 | 半直积平凡 ⇒ 直积；有限交换群基本定理（$99=3^2\cdot11$） |

**我发现的具体问题（含修正文本）**：仅文字瑕疵。
- 第 181 行"由 **Langrange**" → **"由 Lagrange"**。
- 同段"若 $|Z(H)|=1$ 则由类方程 $p^2=1+\sum(\text{非中心类大小})$ "建议补一句"（$Z(H)$ 是 $H$ 的正规子群，$H$ 非交换 ⇒ $Z(H)\ne H$ ⇒ $|Z(H)|<p^2$）"，使"$|Z(H)|\in\{1,p\}$"的来路完整。

**未解决疑点**：无。

---

### 题 4｜2013 / Algebra and Number Theory / Individual / 第 1 题

**题面核对**：原卷 `2013\algebra2013(individual).pdf`："1. (20pt) 1.1 (15 pt) Classify finite groups of order 26 up to isomorphisms. 1.2 (5 pt) For each finite group G of order 26, describe the group Aut(G) of automorphisms of G." 与讲义**逐字一致**；讲义"160 分制"亦与原卷 "This exam of 160 points" 一致。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $n_{13}\equiv1\bmod13$，$n_{13}\mid2$ ⇒ $n_{13}=1$，$P\cong\mathbb Z/13$ 正规 | 成立 | Sylow 第三定理（复算：$\{1,2\}$ 中只有 1） |
| 2 | $G\cong\mathbb Z/13\rtimes_\varphi\mathbb Z/2$，$\varphi(1)=$"$x\mapsto x^a$" | 成立 | $\gcd(13,2)=1$ ⇒ $P\cap H=1$、$|PH|=26$；无需 Schur–Zassenhaus，直接算阶 |
| 3 | $a^2\equiv1\pmod{13}$ ⇒ $a=\pm1$ ⇒ 只有 $\mathbb Z/26$ 与 $D_{26}$ | 成立 | 像的阶整除 $\gcd(2,12)=2$；域 $\mathbb F_{13}$ 中 $x^2=1$ 只有 $\pm1$（无零因子） |
| 4 | 两群不同构：$\mathbb Z/26$ 交换、$D_{26}$ 非交换 | 成立 | $tst^{-1}=s^{-1}\ne s$（$\mathrm{ord}(s)=13>2$） |
| 5 | $\mathrm{Aut}(D_{26})$：$s^it$ 全体为 2 阶元；参数化 $(\psi(s),\psi(t))=(s^a,s^bt)$；von Dyck 验证关系 | 成立 | $(s^it)^2=s^it s^it=s^i s^{-i}t^2=1$；关系 $s^{13}=t^2=1$、$tst^{-1}=s^{-1}$ 保持 ⇒ 同态；有限集上单射 ⇒ 双射 |
| 6 | 复合 $(a,b)(a',b')=(aa',ab'+b)$，即 $\mathrm{Hol}(\mathbb Z/13)$，阶 $13\cdot12=156$ | 成立 | 直接代入：$\psi_{a,b}\psi_{a',b'}(t)=s^{ab'+b}t$；与全形乘法一致 |

**独立计算验证**（`checkA.py` 第 4 节）：穷举 $D_{26}\to D_{26}$ 的全部 $26^2=676$ 组生成元像，用 von Dyck 关系筛选并检验双射，得 **$|\mathrm{Aut}(D_{26})|=156$**；自同构的阶分布为 $\{1{:}13,\ 2{:}13,\ 3{:}26,\ 4{:}26,\ 6{:}26,\ 12{:}52\}$，存在 52 个 12 阶元（与 $\mathrm{Hol}(C_{13})=C_{13}\rtimes(\mathbb Z/13)^\times$ 一致），复合在集合内封闭（确实是群）。**与讲义断言完全吻合。**

**我发现的具体问题（含修正文本）**

**问题 4-1（措辞不准，建议改）**：第 243 行括号内"两个半直积 $\rtimes_\varphi$ 与 $\rtimes_{\varphi'}$ 同构当且仅当 $\varphi,\varphi'$ 相差 $\mathrm{Aut}(P)$ 的共轭作用"**不完整**：标准判据还要允许重新参数化补群 $Q$。

> **修正文本**：严格说，$P\rtimes_\varphi Q\cong P\rtimes_{\varphi'}Q$ 当且仅当存在 $\alpha\in\mathrm{Aut}(P)$ 与 $\beta\in\mathrm{Aut}(Q)$ 使 $\varphi'(q)=\alpha\circ\varphi(\beta^{-1}q)\circ\alpha^{-1}$（$\forall q\in Q$），即 $\varphi,\varphi'$ 落在 $\mathrm{Aut}(P)\times\mathrm{Aut}(Q)$ 作用的同一轨道上。本题两群不同构的判定只用到"交换 vs 非交换"，不依赖这一判据。

**未解决疑点**：无。

---

### 题 5｜2016 / Algebra and Number Theory / Team / 第 3 题

**题面核对**：原卷 `2016\2016-team.pdf` 中 "Algebra and Number Theory / Team"（5 题 100 分）的 "Problem 3 (20 points). Let K be the splitting field of the polynomial $x^4-x^2-1$. (a) (10 points) Show that the Galois group of K over Q is isomorphic to the dihedral group $D_4$ … has order 8. (b) (10 points) Determine the lattice of subfields of K: Find all subfields of K and describe the partial order induced by inclusion." —— 与讲义**一致**（仅 (b) 的 "Find" 大小写差异）。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | $f=x^4-x^2-1$ 无有理根；设 $(x^2+ax+b)(x^2+cx+d)$，由 $c=-a$、$bd=-1$、$a(d-b)=0$ 分两支均矛盾 ⇒ $f$ 不可约，$[\mathbb Q(\alpha):\mathbb Q]=4$ | 成立 | 首一四次可约 ⇒ 有二因式分解；$a=0$ 时 $b,d$ 是 $T^2+T-1$ 的根 $\notin\mathbb Q$；$b=d$ 时 $b^2=-1$ 在 $\mathbb Q$ 无解 |
| 2 | $K=\mathbb Q(i,\alpha)$，$[K:\mathbb Q]=4\cdot2=8$，$K/\mathbb Q$ Galois | 成立 | $\alpha\in\mathbb R$、$i\notin\mathbb R$；分裂域必正规，$\mathrm{char}\,0$ 必可分 |
| 3 | $G\hookrightarrow S_4$（忠实作用在 4 个根上），$|G|=8$ ⇒ 是 Sylow 2-子群 ⇒ $G\cong D_4$ | 成立 | Sylow 第二定理（$|S_4|=24=8\cdot3$，所有 Sylow 2-子群共轭） |
| 4 | 显式 $r=c\sigma$、$c$ 满足 $r^4=c^2=1$、$crc=r^{-1}$；置换写法 $r=(x_1x_4x_2x_3)$、$c=(x_3x_4)$ | 成立 | 见下方独立复算 |
| 5 | $D_4$ 的子群共 10 个（1+3+5+1），对应 10 个子域 | 成立 | 群论枚举正确：4 阶子群恰 $\langle r\rangle,\langle r^2,c\rangle,\langle r^2,cr\rangle$（$c\cdot cr=r$ 阶 4，故 Klein 子群只有两个） |
| 6 | 不动域表 + 包含关系 | 成立 | 见下方独立复算（**逐项**验证） |

**独立计算验证**（`checkA.py` 第 5 节）：在 $K=\mathbb Q(i,\alpha)$ 上建立精确有理算术（基 $\{\alpha^ki^m\}$，$\alpha^4=\alpha^2+1$、$i^2=-1$），得到：

- $r:\alpha\mapsto-i\alpha^3+i\alpha=-i/\alpha$、$i\mapsto-i$；$c:\alpha\mapsto\alpha$、$i\mapsto-i$。**$8\times8$ 基元素两两乘积全检：$r,c$ 都保持乘法**（确是域自同构）；
- $\mathrm{ord}(r)=4$、$\mathrm{ord}(c)=2$、$\langle r,c\rangle$ 阶 8、$crc=r^{-1}$（我第一次跑脚本时报 False，是我把比较对象写成了 $r$ 而非 $r^{-1}$，改正后为 True）；
- $u^2=1+2i$、$v^2=1-2i$、$uv=\sqrt5$、$r(\sqrt5)=-\sqrt5$ **全部成立**；
- 对讲义表格中 10 个生成元逐个计算其不动子群 $\mathrm{Stab}$ 与 $\mathbb Q$-次数：**10 项的 $\mathrm{Stab}$ 都恰好等于讲义所给子群，且次数都等于 $8/|\mathrm{Stab}|$**（$\mathbb Q$、$\mathbb Q(\sqrt5)$、$\mathbb Q(i)$、$\mathbb Q(\sqrt{-5})$、$\mathbb Q(i,\sqrt5)$、$\mathbb Q(\alpha)$、$\mathbb Q(i,u)$、$\mathbb Q(i,v)$、$\mathbb Q(i\alpha)$、$K$）；
- 讲义声称的 **15 条包含关系**与 **9 条互不包含关系**，按 Galois 反序对应逐条检验，**全部成立、无反例**。

**我发现的具体问题（含修正文本）**

**问题 5-1（论证缺口，必须补）**：第 360 行对 $\sigma$ 存在性的理由——"$\alpha$ 在 $\mathbb Q(i)$ 上的极小多项式仍是 $x^4-x^2-1$，因为在 $\mathbb Q(i)$ 上 $x^2=\varphi$ 与 $x^2=\psi$ 仍无解"——**只能排除线性因子**（即 $\alpha^2\in\mathbb Q(i)$ 的情形），**不能排除二次因式**。而二次因式确实需要额外计算：$x^4-x^2-1=(x^2+ax+b)(x^2-ax+d)$ 于 $\mathbb Q(i)[x]$ 时，$b=d=\pm i$ 一支要求 $a^2=1\pm2i$ 在 $\mathbb Q(i)$ 中可开方——这正是讲义自己在 $\langle cr\rangle$ 那一行证明过的"$1+2i$ 不是 $\mathbb Q(i)$ 中的平方"，但正文没有把它接上。补一句后者、或改用下面的 Galois 论证，缺口即闭合。

> **修正文本（替换第 360 行括号内整段）**：
> （存在性：$[K:\mathbb Q(i)]=2$，故 $K/\mathbb Q(i)$ 是 Galois 扩张，设 $\tau$ 为其非平凡元。$\tau(\alpha)$ 是 $\alpha$ 在 $\mathbb Q(i)$ 上的共轭，必为 $\pm\alpha$ 或 $\pm i/\alpha$。若 $\tau(\alpha)=\alpha$，则 $\tau$ 固定 $i$ 与 $\alpha$，即 $\tau=\mathrm{id}$，矛盾；若 $\tau(\alpha)=-\alpha$，则 $\alpha^2=\varphi\in\mathbb Q(i)$，迫使 $\sqrt5=2\varphi-1\in\mathbb Q(i)$，与 $\mathbb Q(i)$ 是虚二次域矛盾。故 $\tau(\alpha)=\pm i/\alpha$；若为 $-i/\alpha$，把 $\tau$ 与复共轭 $c$ 复合（$c\tau c$ 把 $\alpha$ 送到 $c(\tau(\alpha))=c(-i/\alpha)=i/\alpha$）即得。因此 $\sigma$ 存在。）

**问题 5-2（残句，必须清理）**：第 372 行 "（最后一条：$crc$ 把 $i\mapsto c(r(-i))=c(i)=-i\cdot$？更简单地用 (b) 的置换描述验证，见下）" 中的"**？**"是未清理的残句。结论没错（随后用置换 $r=(x_1x_4x_2x_3)\mapsto(x_1x_3x_2x_4)=r^{-1}$ 正确验证了 $crc=r^{-1}$，我已独立复算确认）。建议改写成：

> （最后一条：用共轭置换写法验证——$crc$ 就是把 $r$ 的轮换记法中每个字母换成它在 $c$ 下的像，$r=(x_1x_4x_2x_3)\mapsto(x_1x_3x_2x_4)=r^{-1}$。）

**未解决疑点**：无（子域格与全部包含关系已由脚本穷举确认）。

---

### 题 6｜2017 / Algebra and Number Theory / Individual / 第 2 题

**题面核对**：原卷 `2017\algebra2017-individual.pdf`："Problem 2 (20 points). Let A be a finite abelian group and let φ : A → A be an endomorphism. Put A_nil := {x ∈ A | φ^k(x) = 0 for some k ≥ 1}. (a) (15 points) … (b) (5 points) Show that such a subgroup is unique." —— 与讲义**逐字一致**。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | (F1) $A_{\mathrm{nil}}$ 是子群且 $\varphi$-不变 | 成立 | $\varphi^{\max(k,l)}(x-y)=0$；$\varphi(A_{\mathrm{nil}})\subseteq A_{\mathrm{nil}}$ |
| 2 | (F2) 降链稳定；再把 $K$ 取大以保证 $A_{\mathrm{nil}}\subseteq\ker\varphi^K$ | 成立 | 有限群 ⇒ 链稳定；$\varphi|_{A_{\mathrm{nil}}}$ 幂零 + $A_{\mathrm{nil}}$ 有限 ⇒ 存在 $k_0$。**这一步是必需的**，讲义自己已点明（§4.3 第 5 条） |
| 3 | $A=\mathrm{im}\,m+\ker m$（$m=\varphi^K$） | 成立 | $\mathrm{im}\,m=\mathrm{im}\,m^2$ ⇒ $m(x)=m^2(y)$ ⇒ $x-m(y)\in\ker m$ |
| 4 | $\mathrm{im}\,m\cap\ker m=0$ | 成立 | $m|_{\mathrm{im}\,m}$ 是满射（$\mathrm{im}\,\varphi^{K+1}=\mathrm{im}\,\varphi^K$），有限集上满射=双射 |
| 5 | $A=A_0\oplus A_{\mathrm{nil}}$，$A_0:=\mathrm{im}\,\varphi^K$，$\varphi|_{A_0}$ 自同构 | 成立 | $\varphi(A_0)=\mathrm{im}\,\varphi^{K+1}=A_0$，满射 + 有限 ⇒ 双射 |
| 6 | (b) 唯一性：$B\subseteq\mathrm{im}\,\varphi^K$、$C\subseteq\ker\varphi^K$，比阶得 $B=A_0,C=A_{\mathrm{nil}}$ | 成立 | $b=\varphi^K((\varphi|_B)^{-K}b)$；阶的相等 |

**独立计算验证**（`checkB.py` 第 6 节）：对 16 个有限交换群（$\mathbb Z/4,\ \mathbb Z/2^2,\ \mathbb Z/8,\ \mathbb Z/2\times\mathbb Z/4,\ \mathbb Z/2^3,\ \mathbb Z/9,\ \mathbb Z/3^2,\ \mathbb Z/6,\ \mathbb Z/12,\ \mathbb Z/15,\ \mathbb Z/10,\ \mathbb Z/16,\ \mathbb Z/2\times\mathbb Z/8,\ \mathbb Z/3\times\mathbb Z/6,\ \mathbb Z/5^2,\ \mathbb Z/2^2\times\mathbb Z/4$）**穷举全部内同态**（最多 1024 个），逐一验证：① $A_0\cap A_{\mathrm{nil}}=\{0\}$；② $A_0+A_{\mathrm{nil}}=A$ 且 $|A_0|\cdot|A_{\mathrm{nil}}|=|A|$；③ $\varphi(A_0)=A_0$；④ 在所有子群中穷举，满足"$B\cap A_{\mathrm{nil}}=0$ 且 $\varphi(B)=B$ 且 $|B|=|A_0|$"的 $B$ **唯一**，且恰为 $A_0$。**全部通过，无例外。**

**我发现的具体问题**：无数学问题。（唯一提示：讲义 §3.2 复现清单第 2 条把 $\gcd$ 与 $p^2$ 写成了缺反斜杠的 `$gcd$`、`$p^2 mid$`，见 §3.6 排版清单。）

**未解决疑点**：无。

---

### 题 7｜2019 / Algebra and Number Theory / Individual / 第 5 题

**题面核对**：原卷 `2019\Algebra2019-individual.pdf` 第 5 题与讲义**逐字一致**（含 $p\equiv1,4\pmod5$、$\mathbb F_{p^2}$ 的范数映射、$p\equiv2,3\pmod5$ 三个小问）。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | Binet 公式 $F_n=(\alpha^n-\beta^n)/(\alpha-\beta)$ 由归纳证明 | 成立（但假设写窄了，见 7-2） | 只需 $\alpha+\beta=1$、$\alpha\beta=-1$、$\alpha\ne\beta$；**不需要 $\mathrm{char}\ne2$** |
| 2 | $p\equiv\pm1\bmod5$ ⇒ $(5/p)=(p/5)=1$（因 $5\equiv1\bmod4$）⇒ $\alpha,\beta\in\mathbb F_p^\times$，$\alpha\ne\beta$，Fermat ⇒ $F_{p-1}\equiv0$ | 成立（$p\ne5$、$p$ 奇） | 二次互反律（$5\equiv1\bmod4$ 的补充律）；$\alpha\beta=-1\ne0$；$p=2$ 不在本情形（$2\equiv2\bmod5$），无边界问题 |
| 3 | $N(x)=x^{p+1}$；$\mathbb F_{p^2}^\times$ 循环 ⇒ $|\mathrm{Im}\,N|=(p^2-1)/\gcd(p^2-1,p+1)=p-1$，与 $\mathbb F_p^\times$ 同为 $p-1$ 阶子群 ⇒ 满射；$|\ker N|=p+1$ | 成立 | 有限域乘法群的循环性 + 循环群每个阶数的子群唯一 |
| 4 | $p\equiv\pm2\bmod5$ ⇒ $x^2-x-1$ 不可约 ⇒ 取 $\alpha\in\mathbb F_{p^2}$，$\beta=\alpha^p$ ⇒ $\alpha^{p+1}=\beta^{p+1}=\alpha\beta$ ⇒ $F_{p+1}\equiv0$ | 成立（$p$ 奇时） | 判别式为 5 非平方（**需 $p$ 奇**）；Frobenius 互换两根（$\alpha^p\ne\alpha$ 因 $\alpha\notin\mathbb F_p$）；$\beta^p=\alpha^{p^2}=\alpha$ |
| 5 | 数值检验 | 成立 | 我复算：$p\le3000$ 全部素数 $p\mid F_{p-1}$（$p\equiv\pm1$）与 $p\mid F_{p+1}$（$p\equiv\pm2$）**无例外**；讲义引用的 10 个数字（$F_{10}=55=5\cdot11$、$F_{18}=2584=136\cdot19$、$F_{28}=317811=10959\cdot29$、$F_{30}=832040=26840\cdot31$、$F_3=2$、$F_4=3$、$F_8=21=3\cdot7$、$F_{14}=377=29\cdot13$、$F_{18}=2584=152\cdot17$、$F_{24}=46368=2016\cdot23$）**全部正确** |
| 6 | $|\ker N|=p+1$、$N$ 满射 | 成立 | 在 $\mathbb F_{p^2}$ 上直接枚举复算 $p\le47$：$|\ker N|=p+1$、$|\mathrm{Im}\,N|=p-1$ 全部吻合 |

**我发现的具体问题（含修正文本）**

**问题 7-1（$p=2$ 处理由不成立，必须改）**：第 3 问开头写"此时 $(5/p)=(p/5)=-1$，故 5 不是 $\mathbb F_p$ 中的平方"，随后文末断言"$p=2$ 时…上面的论证照旧成立"。**这两处对 $p=2$ 都不成立**：
- 二次互反律的"$(5/p)=(p/5)$"形式（由 $5\equiv1\bmod4$ 化简而来）**要求 $p$ 为奇素数**；$p=2$ 时 $(5/2)=1$（$5\equiv1\bmod8$），而 $(2/5)=-1$，两者不等；
- 事实上 $5\equiv1=1^2$ 在 $\mathbb F_2$ 中**是**平方，而"判别式是平方 ⟺ 二次多项式可约"这一判据在特征 2 也失效（需要 2 可逆）。

结论（$2\mid F_3$）仍然对，但必须换理由——直接检验 $x^2+x+1$ 在 $\mathbb F_2$ 上无根更省事。

> **修正文本（替换第 606 行整段）**：
> *关于 $p=2$*：$p=2$ 时**不能**沿用"$(5/p)=(p/5)=-1$ ⇒ $x^2-x-1$ 不可约"——二次互反律的该形式要求 $p$ 为奇素数，而且 $(5/2)=1$、$5\equiv1$ 在 $\mathbb F_2$ 中本来就是平方，判别式判据在特征 2 也失效。正确做法是直接检验：$x^2-x-1=x^2+x+1$ 在 $\mathbb F_2$ 上的取值 $1,1$ 均非零，故不可约；取根 $\alpha\in\mathbb F_4\setminus\mathbb F_2$，则 $\beta=\alpha^p=\alpha^2=\alpha+1$ 为另一根，$\alpha^{p+1}=\alpha\beta=\beta^{p+1}$，于是 $F_3=(\alpha^3-\beta^3)/(\alpha-\beta)=0$ 于 $\mathbb F_4$，即 $2\mid F_3$。第 1 问中 $p=2$ 不出现（$2\equiv2\bmod5$），无碍。

**问题 7-2（假设写窄，建议改）**：第 532 行把 Binet 公式的适用范围写成"在任意特征 $\ne2$ 的域中"，但第 3 问对 $p=2$ 时仍在用该公式；而证明本身只用到 $\alpha^2=\alpha+1$、$\beta^2=\beta+1$、$\alpha\ne\beta$，**没有任何地方用到 2 可逆**。

> **修正文本**：标题行改为"**Binet 公式（在任意域中，只要 $x^2-x-1$ 有两个不同的根 $\alpha\ne\beta$）**"，并在证明末尾加一句"（过程未用到 $\mathrm{char}\ne2$，故特征 2 情形同样适用。）"

**未解决疑点**：无（结论对全部素数成立已数值确认）。

---

### 题 8｜2022 / Algebra and Number Theory / Individual / 第 5 题

**题面核对**：原卷 `2022\ExamPaper_2022\algebra_and_numbertheory_22s.pdf` Problem 5 与讲义题面**逐字一致**（(a)–(d) 四问，含 "Solve every problem" 说明）。更进一步：归档中**存在官方解答** `2022\Solution_2022\algebra_and_numbertheory_22s_soln.pdf`，其四问答案——$\mathrm{Tr}=p$、$\mathcal N=\Phi_p(1)=p$、$(1-\zeta)\mathcal O_K\cap\mathbb Z=p\mathbb Z$ 及迹的整除性、$\mathcal O_K=\mathbb Z[\zeta_p]$——**与讲义结论完全一致**（官方 (d) 走迹的路线，讲义走判别式/指数路线，两条都对）。**无需改动题面。**

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | (a) $\Phi_p(Y+1)=\sum_{k=0}^{p-1}\binom{p}{k+1}Y^k$ 对 $p$ 是 Eisenstein ⇒ $\Phi_p$ 不可约，$[K:\mathbb Q]=p-1$ | 成立 | 对 $1\le j\le p-1$，$p\mid\binom pj$（分母 $j!$ 与 $p$ 互素）；常数项 $=p$，$p^2\nmid p$；$Y\mapsto X-1$ 是环自同构。复算 $p=3,5,7,11,13$ 全部满足 |
| 2 | (b) 迹 $=\sum_a(1-\zeta^a)=(p-1)-(-1)=p$；范 $=\prod(1-\zeta^a)=\Phi_p(1)=p$ | 成立 | 共轭元恰为 $\{1-\zeta^a\}$（$a\in(\mathbb Z/p)^\times$）；$\sum_{a=1}^{p-1}\zeta^a=-1$；$\Phi_p(X)=\prod(X-\zeta^a)$ |
| 3 | (c) $p\in(1-\zeta)$；$(1-\zeta)\mathcal O_K\cap\mathbb Z=p\mathbb Z$（否则 $1-\zeta$ 是单位，$\mathcal N=\pm1$）；$\mathrm{Tr}(y(1-\zeta))\in p\mathbb Z$ | 成立 | $1-\zeta^a=(1-\zeta)(1+\zeta+\cdots+\zeta^{a-1})$；$\mathbb Z$ 的理想含 $p\mathbb Z$ 只能是 $p\mathbb Z$ 或 $\mathbb Z$；迹是代数整数且属 $\mathbb Q$ ⇒ $\in\mathbb Z$，又每个 $\sigma_a(z)\in(1-\zeta)\mathcal O_K$ |
| 4 | (d) 由 $(\zeta-1)\Phi_p'(\zeta)=p\zeta^{-1}$ 取范数 ⇒ $\mathcal N(\Phi_p'(\zeta))=p^{p-2}$ ⇒ $|\mathrm{disc}|=p^{p-2}$ | 成立 | $(X-1)\Phi_p(X)=X^p-1$ 求导；范数是乘法同态；$\mathcal N(\zeta)=1$（$p$ 奇时 $p-1$ 为偶数） |
| 5 | (d) $\mathrm{disc}=f^2d_K$ ⇒ $f^2\mid p^{p-2}$ ⇒ $f=p^j$；Cauchy 取 $\alpha$，$p\alpha=\gamma\notin p\mathbb Z[\zeta]$ | 成立 | **引用**：判别式与指数关系（讲义 §4.3 第 3 条已如实声明未重证）；Cauchy 定理用于 $p$-群 $\mathcal O_K/\mathbb Z[\zeta]$；$\gamma\notin p\mathbb Z[\zeta]$ 需一句"否则 $p\alpha=p\beta$ ⇒ $\alpha=\beta\in\mathbb Z[\zeta]$" |
| 6 | (d) $\mathrm{Tr}(\gamma)=a_0p-S$、$\mathrm{Tr}(\gamma\zeta)=-S$ ⇒ $\mathrm{Tr}(\gamma(1-\zeta))=a_0p$ ⇒ $\mathrm{Tr}(\alpha(1-\zeta))=a_0\in p\mathbb Z$ 矛盾 | 成立 | $\mathrm{Tr}(\zeta^k)=-1\ (1\le k\le p-1)$、$\mathrm{Tr}(1)=p-1$；迹的 $\mathbb Q$-线性性 |

**独立计算验证**（`checkC.py`）：
1. $\Phi_p(Y+1)$ 的系数与 Eisenstein 条件：$p=3,5,7,11,13$ 全部满足（常数项 $p$ 不被 $p^2$ 整除）；
2. $\mathrm{Tr}(1-\zeta)=p$、$\mathcal N(1-\zeta)=\Phi_p(1)=p$：$p=3,5,7,11,13$ 全部正确；
3. 判别式 $\det(\mathrm{Tr}(\zeta^{i+j}))_{0\le i,j\le p-2}$ 用精确有理消元计算：$p=3,5,7,11,13,17$ 依次得 $-3,\ 125,\ -16807,\ -2357947691,\ 1792160394037,\ 2862423051509815793$，**$|\mathrm{disc}|=p^{p-2}$ 全部严格相等**；
4. (d) 的关键恒等式：$p=3,5,7,11$ 各 300 组随机整数系数（$a_0\ne0$），验证 $\mathrm{Tr}(\gamma)=a_0p-S$、$\mathrm{Tr}(\gamma\zeta)=-S$、$\mathrm{Tr}(\gamma(1-\zeta))=a_0p$ —— **1200 组全部成立**；
5. "乘 $\zeta^{-i_0}$ 后可设 $a_0\ne0$"：$p=3,5,7,11,13$ 各 300 组随机向量，按 $\zeta^{p-1}=-(1+\zeta+\cdots+\zeta^{p-2})$ 精确归约后新常数项 $\not\equiv0\bmod p$ —— **1500 组全部成立**（原因是 $i<i_0$ 的系数在模 $p$ 下全为 0，$\zeta^{p-1}$ 的归约不贡献常数项）。

**我发现的具体问题（含修正文本）**：仅排版／表述。
- 第 671 行 $\mathcal N(1-\zeta)$ 的连等式把同一个 $\prod_{a=1}^{p-1}(1-\zeta^a)$ **写了两遍**，建议改为 $\mathcal N_{K/\mathbb Q}(1-\zeta)=\prod_{a=1}^{p-1}(1-\zeta^a)=\Phi_p(1)=p$。
- 第 720 行"由 Cauchy 定理存在 $\alpha$ 使 $p\alpha=\gamma$"之后建议补一句 $\gamma\notin p\mathbb Z[\zeta]$ 的理由（上文已给）。
- §4.3 第 3 条自认"判别式与指数的关系未重证"——**这是诚实的、也是可接受的**；官方 2022 解答 (d) 用迹绕过了这一条，两条路都成立。

**未解决疑点**：无。

---

### 题 9｜2014 / Algebra and Number Theory / Individual / 第 3 题

**题面核对**：原卷 `2014\algebra2014(individual).pdf` Problem 3 与讲义**一致**（$X^2-82Y^2=\pm2$；(a) 5 分、(b) 7 分、(c) 8 分）。**无需改动**。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | (a) $(9x-82y)^2-82(x-9y)^2=-(x^2-82y^2)$ | 成立 | 直接展开（在 $[-60,60]^2$ 全检）；结构解释：$9+\sqrt{82}$ 范 $-1$ 的单位，映射 = 乘 $9-\sqrt{82}$ 再取共轭。$T^2=-\mathrm{id}$ 亦全检成立 |
| 2 | (b) 模 $p$ 解数 $N_a=p-1$（$d$ 为平方，可逆线性代换 $u=x-ry,\ v=x+ry$）或 $p+1$（$d$ 非平方，用范数映射核） | 成立 | 行列式 $2r\ne0$（$p$ 奇）；非平方情形用题 7 的范数满射（讲义此处交叉引用正确） |
| 3 | $N_a\ge p-1\ge2$ ⇒ 存在**本原**解（非本原解至多 $(0,0)$ 一个） | 成立 | 计数论证 |
| 4 | 多元 Hensel 引理（某偏导为 $p$ 进单位）：$p\nmid x_0$ 用 $\partial_X F=2x_0$；否则 $p\nmid y_0$ 用 $\partial_Y F=-164y_0$ | 成立 | $p$ 奇 ⇒ $2x_0\not\equiv0$；$x_0\equiv0$ 且 $a=\pm2\not\equiv0$ ⇒ $y_0\not\equiv0$；**情形 2 排除 $p=41$**，故 $-164y_0\not\equiv0$ |
| 5 | (b) $p=41$ 单独处理：$41\equiv1\bmod8$ ⇒ $(2/41)=1$；$41\equiv1\bmod4$ ⇒ $-1$ 是平方 ⇒ $\pm2$ 都是平方，取 $y=0$ | 成立 | Legendre 符号补充律；$\partial_X F=2x_0\ne0$ 可 Hensel 提升 |
| 6 | (c) $9y<|x|<10y$（$y\ge2$；$y=0,1$ 排掉）⇒ $x>0$ 用 $T$、$x<0$ 用 $T'$，得 $0<|y_1|<y$，与 $|y|$ 最小性矛盾 | 成立 | $82y^2-2>81y^2$、$82y^2+2<100y^2$（$y\ge1$）；$T,T'$ 的换号恒等式；$y_1=x-9y\in(0,y)$、$y_1=x+9y\in(-y,0)$ |

**独立计算验证**（`checkB.py` 第 9 节）：
1. $0\le y\le 2\times10^6$ 范围内（配合 $x^2=82y^2\pm2$ 的完全平方检验）**无任何整数解**，与 (c) 一致；
2. 模 $p^n$ 可解性：对 $p\in\{2,3,5,7,11,13,41,43,83\}$ 逐个 $n$（$p^n\le4\times10^5$）枚举全部 $y$ 残类、判断 $82y^2\pm2$ 是否平方剩余 —— **两个方程在全部检验过的 $(p,n)$ 上都有解**（含讲义未要求的 $p=2$）；
3. 模 $p$ 解数 $N_a$：对全部奇素数 $p\le200$（除 $p=41$，讲义已单列情形 1）逐一枚举 $(x,y)\in\mathbb F_p^2$，**$N_a$ 恒等于 $p-1$（82 为平方）或 $p+1$（否则）**，无反例；
4. 两个递降映射的换号恒等式与 $T^2=-\mathrm{id}$ 全检通过；
5. 讲义补充的 $p=2$ 显式点 $(10/3,1/3)$：$(100-82)/9=2$ ✓，且 $1/3\in\mathbb Z_2$ ✓，故确为 $\mathbb Z_2$ 上的真解。

**我发现的具体问题**：无数学问题。（Hensel 引理是引用，但讲义给出了 Newton 迭代的证明梗概，足以自足。）

**未解决疑点**：无。

---

### 题 10｜2026 / Algebra and Number Theory / Individual / 第 2 题

**题面核对**：本地归档 `sources/prelim` **只有 2010–2025 共 16 个年份目录，没有 2026**（已用 `Get-ChildItem` 确认），故**无法对原卷复核**——讲义自己在 §4.1 已如实标注，态度正确。与 `problems_full.json` 的抽取文本逐句比对：方程、$N_p$ 的定义、$m\in\mathbb Z_{\ge1}$ 与 $X_m$、$\chi(0)$ 的约定、$J(\chi,\mu):=\sum_{a+b=1}\chi(a)\mu(b)$、$|J(\chi,\mu)|=\sqrt p$ 的提示、(1)(2)(3) 三问的文字与顺序，**全部一致**（仅标点/排版被清理）。**内容自足，无需改动**；风险仅在于无法排除原卷标点细节差异。

**关键步骤审计**

| # | 步骤 | 判定 | 依据 |
|---|---|---|---|
| 1 | (2) $a=0$：两边都等于 1 | 成立 | $\chi(0)$ 约定：平凡特征取 1，其余取 0 |
| 2 | (2) $a\ne0$：$N(X^m=a)=|\ker(\cdot)^m|=m$ 或 0；$\sum_{\chi\in X_m}\chi(a)$ 用**特征正交关系**给出 $m$ 或 0 | 成立 | $\mathbb F_p^\times$ 循环（$m\mid p-1$）；对子群 $X_m\le\widehat{\mathbb F_p^\times}$ 的正交关系 $\sum_{\chi\in X_m}\chi(a)=m\cdot[\chi(a)=1\ \forall\chi\in X_m]$，而 $\bigcap_{\chi\in X_m}\ker\chi=\langle g^m\rangle$ |
| 3 | (1) $p=3$ 或 $p\equiv2\bmod3@@ ⇒ $x\mapsto x^3$ 是双射 ⇒ $T=\sum_u\chi_2(u)=0$ ⇒ $N_p=p$ | 成立 | $\gcd(3,p-1)=1$；$p=3$ 时 Frobenius 是恒等；$p=2$ 时讲义单独直接点数（$N_2=2$，我已复算 ✓） |
| 4 | (3) $T=\sum_a\chi_2(a+1)\#\{x:x^3=a\}=\sum_{i=0}^{2}\sum_a\psi^i(a)\chi_2(a+1)$ | 成立 | (2) 的 $m=3$ 情形；按 $a=x^3$ 归并求和 |
| 5 | $i=0$ 项 $=0$；$i=1$ 项 $=\psi(-1)J(\psi,\chi_2)$；$i=2$ 项 $=J(\psi^2,\chi_2)$（因 $\psi^2(-1)=1$） | 成立 | 代换 $a=-u$；$J$ 定义中 $u=0,1$ 两项因 $\chi(0)$ 约定而消失 |
| 6 | $|J(\psi,\chi_2)|=|J(\psi^2,\chi_2)|=\sqrt p$ ⇒ $|N_p-p|\le2\sqrt p$ | 成立 | 题面给出的 $|J|=\sqrt p$（要求 $\chi,\mu,\chi\mu$ 都非平凡）；$\psi,\psi^2$ 阶 3、$\chi_2$ 阶 2，$\gcd(2,3)=1$ ⇒ $\psi\chi_2,\psi^2\chi_2$ 非平凡 |

**独立计算验证**（`checkB.py` 第 10 节）：
1. $p\le2000$ 全部素数：$|N_p-p|\le2\sqrt p$ **无反例**；$p=3$ 与 $p\equiv2\bmod3$ 时 $N_p=p$ **无反例**；
2. 对 **全部 80 个 $p\equiv1\bmod3$、$p\le1000$** 的素数，在 $\mathbb Z[\omega]$（$\omega^2=-1-\omega$）中**精确**计算 $J(\psi,\chi_2)$、$J(\psi^2,\chi_2)$：验证 ① $\psi(-1)J(\psi,\chi_2)+J(\psi^2,\chi_2)=N_p-p$（结果为整数，$\omega$ 分量为 0）；② $|J|^2=p$ —— **全部成立，无反例**；
3. 讲义 $p=7$ 的数值全部复现：取生成元 $g=3$（$\psi(3)=\zeta_3$ ✓）、$J(\psi,\chi_2)=3+2\zeta_3$、$J(\psi^2,\chi_2)=1-2\zeta_3$、$\psi(-1)=1$、$T=4$、$N_7=11$，且直接点数 $4\cdot2+3\cdot1=11$ ✓。

**我发现的具体问题（含修正文本）**

**问题 10-1（实质错误，必须改）**：**附录 B 公式卡第 1124 行**写的是
`- $\#\{(x,y)\in\mathbb F_p^{2}:y^{2}=x^{3}+1\}=p-\sum_x\chi_2(x^{3}+1)$，...`
符号写反了：正确应为 $p+\sum_x\chi_2(x^3+1)$（正文第 938 行"$N_p=p+T$，$T=\sum_x\chi_2(x^3+1)$"**是对的**，两者矛盾）。反例检验：$p=7$ 时 $\sum_x\chi_2(x^3+1)=4$，$7+4=11$ 与直接点数一致，而 $7-4=3$ 显然错误。

> **修正文本（替换该行）**：
> - 对奇素数 $p$：$\#\{(x,y)\in\mathbb F_p^{2}:y^{2}=x^{3}+1\}=p+\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1)$（$p=2$ 时该式不成立，需单独点数 $N_2=2$），且 $\left|\sum_{x\in\mathbb F_p}\chi_2(x^{3}+1)\right|\le2\sqrt p$。例：$p=7$ 时 $\sum_x\chi_2(x^3+1)=4$，$N_7=11$。

**问题 10-2（可加强的表述）**：第 (2) 问的证明里"由特征的正交关系…"一步，严格说是对"商去 $\bigcap\ker\chi$ 后的循环群"用正交关系；讲义结果正确，但可加半句说明，避免读者以为对一般子群 $X_m$ 直接成立。

**未解决疑点**：
- 2026 年原卷缺失 ⇒ 题面只做到 JSON 级复核（标点、括号、分行可能与原卷有出入；讲义已自我声明）；
- 解法所依赖的 $|J(\chi,\mu)|=\sqrt p$ 是题面**给出的**已知事实（我没有独立重证，只做了数值验证 $|J|^2=p$）。

---

## 3. 统计

### 3.1 裁定分布

| 裁定 | 数量 | 题号 |
|---|---|---|
| **VERIFIED** | **6** | 题 1、题 3、题 4、题 6、题 8、题 9 |
| **MINOR-FIX** | **4** | 题 2、题 5、题 7、题 10 |
| **SERIOUS-ERROR** | **0** | —（没有任何一道题的结论错误或主证明失效） |
| **UNVERIFIED** | **0** | — |

### 3.2 错误率（分层口径，避免一个数字误导）

| 口径 | 数值 |
|---|---|
| 有瑕疵题比例（需改一处及以上） | $4/10 = 40\%$ |
| **影响结论正确性的错误率** | $\mathbf{0/10 = 0\%}$（10 题的结论全部正确） |
| **影响主证明有效性的错误率** | $\mathbf{0/10 = 0\%}$（4 处问题中 3 处位于补充说明/附录/边界讨论，1 处是可一行补上的论证缺口） |
| 会**误导读者**的实质错误 | 3 处：题 2 的"模约化会失败"、题 7 对 $p=2$ 的理由、题 10 附录 B 的点数公式符号 |
| 论证缺口（结论对，理由不足） | 1 处：题 5 的 $\sigma$ 存在性 |
| 表述不准 | 2 处：题 4 的半直积同构判据、题 10 的正交关系用法 |
| 纯排版/笔误 | 9 处 LaTeX 反斜杠丢失（§3.6）+ 2 处（"Langrange"、$\prod$ 连等式重复） |

### 3.3 题面核对结果

| 题 | 题面来源 | 结果 |
|---|---|---|
| 题 1,2,3,4,5,6,7,8,9 | 原卷 PDF（PyMuPDF 逐字提取） | **9/9 与讲义一致**，无缺失、无改写、无符号错误 |
| 题 10 | 仅 `problems_full.json`（本地无 2026 卷） | 逐句一致，但**无法与原卷复核**（讲义已声明） |

### 3.4 独立计算验证覆盖度

| 验证方式 | 覆盖题目 | 规模 |
|---|---|---|
| 精确有理/整数算术（$\mathbb Q(i,\alpha)$、$\mathbb Z[\omega]$、判别式） | 题 5、题 8、题 10 | 题 5 全部 10 个子域 + 24 条包含关系；题 8 六组判别式 + 2700 组随机恒等式；题 10 80 个素数的 Jacobi 和 |
| 穷举（群、模算术、点数） | 题 3、题 4、题 6、题 7、题 9、题 10 | 题 4：$676$ 组生成元像；题 6：16 个群的全部内同态（最多 1024 个）+ 全部子群；题 9：$y\le2\times10^6$ + 9 组 $(p,n)$；题 10：$p\le2000$ 点数 |
| 素数范围扫描 | 题 7、题 10 | 题 7：$p\le3000$ 全部素数；题 10：$p\le1000$ 中全部 $p\equiv1\bmod3$（80 个） |

### 3.5 元数据差异（与讲义正文陈述不符）

| 讲义陈述 | 实际情况（当前 757 题快照） | 影响 |
|---|---|---|
| "problems_full.json 共 757 条" | ✅ 757 条 | 无 |
| "其中 subject = Algebra & Number Theory 共 **150** 条" | ❌ **149 条**（`subject` 精确匹配；无第二种写法） | 仅数字，不影响选题与解答 |
| "年份 2010–2026，17 个年份" | ✅ 2010–2026，17 个年份（2026 代数题 5 道） | 无 |
| §4.2(1) "2017 team №1/№2 的 JSON 条目跨页错位（$g_1g_2=g_2g_1=g$ 被切断）" | ⚠️ **当前快照中 2017-team 的两条代数条目文本完整**（№1 完整到 "(b) Show that such a pair is unique."；№2 是"$\mathrm{tr}(T)\in\mathbb Z$ / $\mathrm{tr}(T)\equiv n \bmod p$"那道题），未见该处截断 | 该说明可能基于旧快照；不影响 10 道题 |
| §4.2(2) "2019 team №1 结尾截断为 $S_{\lceil n/2\rceil}$、№2 开头为 $]\ltimes(\mathbb Z/2\mathbb Z)^{\lfloor n/2\rfloor}$" | ✅ **仍然成立**（当前快照确实如此） | 无 |
| §4.3(8) "归档中 2020–2022 年有官方解答 PDF" | ✅ 成立（2020/2021/2022 各有代数科官方解答；2010–2019、2023–2025 无） | 我已用 2022 官方解答复核题 8，四条结论一致 |
| §1.1 "题 8 硬在代数数论的技术堆叠（判别式、指数、**Hensel 型论证**）" | ❌ 措辞错位：Hensel 型论证属**题 9**；题 8 的难点是判别式/指数/迹 | 纯文字 |

### 3.6 排版缺陷清单（LaTeX 反斜杠丢失，共 9 处）

被审文件中下列行出现了丢失反斜杠的数学命令（会渲染成普通文字），**建议逐个修**：第 999（`$gcd$`）、1000（`$mathrm{tr}(B^k)=0Rightarrow B$`）、1007（`$mathrm{Aut}(D_{2n})=mathrm{Hol}(C_n)$`）、1009（`$mathbb F_{p^2}$`）、1026–1027（`$gcd$` 与 `$p^2 mid$`，且中间的换行把数学环境切断）、1028（`$mathrm{Aut}(D_{26})$`）、1029（`$alpha^{p+1}=alpha\beta=\beta^{p+1}$`）、1030（`$mathrm{Tr}(gamma(1-zeta))=a_0p$`）、1037（`$mathbb F_2$`）。这些位于"复现清单"与"配合材料"两节，正是读者会照抄的地方，务必修。

---

## 4. 给使用者的提醒：哪些题的解答需要先改再用

**先说结论：没有任何一道题的结论或主证明是不可信的**——题 1、3、4、6、8、9 可以原样使用；题 2、7、10 的**主证明**可以原样使用，但下面 4 处文字**必须改掉**，否则会把错误内容背进考场：

| 优先级 | 位置 | 问题 | 后果 | 改法 |
|---|---|---|---|---|
| 🔴 高 | 题 2 补充说明（第 149 行） | "模约化这条路在本例中会失败"是假命题 | 形成错误认知：以为此题不能模约化；事实上 $f\bmod 11$ 不可约 | 用 §2 题 2 的修正段替换（明确列出 $p=11,53,59,79,97$ 可行） |
| 🔴 高 | 题 10 附录 B（第 1124 行） | 点数公式符号写反（$p-\sum\chi_2$） | **背公式必错**；与正文 $N_p=p+T$ 及 $N_7=11$ 自相矛盾 | 改为 $p+\sum_x\chi_2(x^3+1)$，并注明 $p=2$ 例外 |
| 🟠 中 | 题 7 第 3 问的 $p=2$ 说明（第 588、606 行） | 对 $p=2$ 使用只对奇素数成立的二次互反形式；"论证照旧成立"不实 | 结论对但理由错，考试写出来会失分 | 用 §2 题 7 的修正段替换（$x^2+x+1$ 直接检验） |
| 🟠 中 | 题 5 $\sigma$ 存在性（第 360 行）与 $crc$ 残句（第 372 行） | 论证缺口（只排除线性因子）+ 残留"？" | 结论对，但照原文写会被判"论证不完整" | 用 §2 题 5 的修正段替换 |
| 🟡 低 | 题 4 半直积判据（第 243 行）、题 10 正交关系（第 906 行）、题 3 "Langrange"、题 8 $\prod$ 重复 | 措辞/笔误 | 不影响使用 | 按 §2 各题的修正文本改 |

**"必须自己重做"的题目**：**没有**。若一定要点名"最该自己算一遍"的，是**题 5**（子域格共 24 条关系，最容易抄错）与**题 8(d)**（判别式—指数—迹三件事串起来，检验自己是否真懂）；这两题的正确性我已用脚本逐项确认，重做的目的是确认**自己**会做，而不是因为讲义有错。

---

## 5. 存疑清单

1. **题 10 题面无法对原卷复核**：本地归档只到 2025 年，2026 卷缺失。我做到的上限是与 `problems_full.json` 逐句一致。若日后拿到 2026 原卷，应重新核对 (1)(2)(3) 的措辞与 $\chi(0)$ 约定。
2. **9 道题没有官方解答可比对**：归档中只有 2020–2022 三年有官方解答 PDF（题 8 属 2022，已比对一致）。题 1–7、9 的结论只经过"我独立推导 + 脚本复算"，没有第二方文本对照。这是本次审稿最大的结构性限制。
3. **题 8(d)** 依赖"判别式 $=f^2 d_K$"这一标准事实（讲义已声明引用，我未重证）。若要求零引用自足，可改用官方 2022 解答的迹方法（我已读过，方法正确）。
4. **题 9(b)** 中"多元 Hensel 引理"是引用（讲义给了 Newton 迭代梗概）。我未给出完整证明，但已用穷举验证结论在大量 $(p,n)$ 上成立。
5. **元数据 149 vs 150**：若讲义作者手中是含 150 条代数题的旧快照，请以当前 757 题口径为准；§4.2(1) 关于 2017-team 的截断描述在当前快照中已不适用。
6. **交叉引用只抽查了 18 条**（题 1/2/3/5/6/7/8/9/10 的"同类题"），抽查结果与 JSON 全部吻合（含 2010 team №5 与 2011 individual №6 确为同一道 150 阶群题）。剩余约 30 条未逐条核对，属指引性内容，不影响 10 道题的解答。
7. **未做**：官方答案与讲义的**风格差异**评估（例如题 8(d) 两条路线哪个更适合考场）；这超出审稿范围。

---

## 附：本报告用到的全部可复跑脚本

| 脚本 | 覆盖 | 关键输出 |
|---|---|---|
| `scripts/verification/checkA.py` | 题 1、2、4、5 | 交换子恒等式（6 组随机整数矩阵）；Eisenstein 与 $f\bmod p$ 不可约性扫描；$D_{26}$ 全部 676 组生成元像 ⇒ $|\mathrm{Aut}|=156$；$K=\mathbb Q(i,\alpha)$ 的 10 个子域与 24 条包含关系（精确算术） |
| `scripts/verification/checkB.py` | 题 3、6、7、9、10 | 99 阶群 Sylow 算术；16 个交换群的全部内同态 + Fitting 分解与唯一性穷举；$p\le3000$ Fibonacci 整除扫描与 $|\ker N|=p+1$；$y\le2\times10^6$ 无解 + 模 $p^n$ 可解性 + $N_a$ 扫描；$p\le2000$ 点数与 80 个素数的 Jacobi 和精确核对 |
| `scripts/verification/checkC.py` | 题 8 + 元数据 | Eisenstein 系数、$\mathrm{Tr}$、$\mathcal N$、判别式 $\pm p^{p-2}$（$p\le17$）、(d) 的 2700 组随机恒等式与 $a_0$ 归约；题库条数与年份 |
| `scripts/verification/checkD.py` | 元数据与交叉引用 | `subject` 分布（Algebra = 149）、2017/2019 team 抽取残缺核查、18 条交叉引用原文 |
| `scripts/verification/_extract_pdfs.py`、`_extract2.py` | 题面核对 | 9 份原卷 PDF 的逐字文本（含 2022 官方解答） |

**被审文件**：`reports/solutions_algebra.md`（未被本报告修改）
**本报告**：`reports/referee_algebra.md`
**审稿口径**：problems_full.json 当前快照（757 条，Algebra & Number Theory 149 条）；原卷 PDF 只读复核 2010–2019、2022 共 9 题。
