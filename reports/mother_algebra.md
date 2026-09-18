# 丘成桐大学生数学竞赛 · Algebra & Number Theory 母题归并

> 产物：本文件 + `data/mother_algebra.json`（机器可读版）
> 数据源：`data/problems_full.json`
> 通读用中间产物：`data/an_read.md`（149 条题面按年份导出，逐条读过）

---

## §0 方法与口径

### 0.1 数据口径（本次运行的基准）

| 项 | 值 |
| --- | --- |
| 数据文件 | `data/problems_full.json` |
| 全库题数 | **757 题**（此前某些报告按 751 / 758 题统计；本次一律以当前 757 题为基准） |
| 本科目题数 | **149 题**（`subject == "Algebra & Number Theory"`） |
| 年份跨度 | 2010 – 2026 |
| 卷别构成 | individual 94 题 / team 55 题 |
| 卷数 | 27 卷（2010–2019 每年 individual + team 各一卷；2020 起只保留 individual 卷，2026 亦只有 individual 卷） |

**数据本身的三个已知瑕疵（会影响引用，先声明）：**

1. **2010 team 缺 n=5**：该卷在库中只有 n = 1, 2, 3, 4, 6 五条，第 5 题缺失（原始 PDF 应有一题，但库内无文本，故本次不计入）。
2. **2010 team n=6 一条题面合并了两道题**：文本为「Prove that a group of order 150 is not simple.」+「SL2(C) 的对称幂表示」。本报告在需要时把它拆成两个成员引用（在 §1 表里标注，在 JSON 中该条目同时出现在 ALG-M02 与 ALG-M09）。因此「成员链接总数 116」> 「被覆盖的题目数 115」。
3. **2019 team n=2 的题面开头混入了 n=1 的答案残片**（`] ⋉ (Z/2Z)^{[n/2]}. 2) Recall that...`），但真正的问题主体（`C[End_C(V)]^{G×G}`）完整，不影响归并。
4. 「仍然在考」的判定：**该母题在 2021–2026 之间至少出现过一次 ⇒ 记为「是」**；否则记为「否（休眠）」。这只是一个运营口径，不是数学口径。

### 0.2 「同一母题」的判定标准

对任意两题 A、B，我按下面三条逐一检查，**必须同时满足 S1 与 S2 才并入同一母题**；S3 用于判断这是"同一个母题的不同实例"还是"两个恰好相似的母题"。

- **S1 数学结构相同**：把题面里的具体对象抹掉后，两者的命题形态（假设—结论的逻辑骨架）可以逐句对应。例如 2010 team 3 与 2014 team 2 都是「求 $\prod_{n=1}^{(p-1)/2}\cos(n\pi/p)$ 的精确有理值」，抹掉 p=7 后就完全同一。
- **S2 解法骨架相同**：核心引理与关键步骤可以一一对应，而不是"碰巧都能用某种通用工具"。典型反面例子：2022 individual 3（$\mathfrak{sl}_4\cong\mathfrak{so}_6$ 的显式同构）与 2017 team 3（李代数秩函数是多项式函数的零点集）都以"复李代数"为对象，但骨架毫不相干，故**不并**。
- **S3 对象可替换**：把对象换成同类对象后题目依然成立，而且**这种替换正是历年真题实际采用的换法**。例如 ALG-M23 里 2018 team 3 用 $\Phi_n(X)\bmod p$，2024 individual 6 换成 $\Phi_n(X)\bmod \mathbb F_q$ 并给出 $d=\operatorname{ord}_n(q)$ 的一般分解——这就是标准的"对象可替换"。

### 0.3 我**主动排除**的边界情况

| 排除类型 | 例子 | 理由 |
| --- | --- | --- |
| 只有"标签"相同 | 所有题都属于"有限群"或"交换代数" | 标签不是母题；母题必须是"这题在考什么" |
| 对象同类但骨架不同 | 2019 individual 4（$GL_n(\mathbb C)$ 的连通性）vs 2023 individual 1（$GL_n(F)$ 的生成元与可解性） | 一个用 Jordan 形/连续性，一个用初等矩阵与换位子；仅有"都是线性群" |
| 同年同卷的巧合 | 2016 individual 1（$\langle u_i,u_j\rangle\le 0$ 的基）与 2016 team 1（$kb$ 正定对称的 QR 分解） | 都以正定二次型为对象，但一个求正交基的组合构造、一个做矩阵分解 |
| 单成员即算孤题 | 见 §3 | 我不为只有 1 题的"母题"编号；它们列在 §3 孤题表里 |

### 0.4 计数约定

- 每道题**只做一次主归属**（按题目的"头部诉求"归属）；唯一例外是 2010 team 6，因为它本身就是合并题面。
- 被同一母题覆盖的题目，即便在同一份卷子里出现两次（如 2011 team 5 与 2012 team 2 逐字相同），仍各记 1 次——它们分别占用两年的考试名额。
- 覆盖率 = 进入某个多成员母题的题数 / 149；未进入的记为**孤题**。

### 0.5 引用格式

表格与正文中的成员一律写成「**年份 + 卷别 + 题号**」：
`10I4` = 2010 年 individual 卷第 4 题；`15T2` = 2015 年 team 卷第 2 题。JSON 中展开为 `{"year":"2015","kind":"team","n":2}`。

---

## §1 母题总表

共归并出 **41 个母题**，覆盖 **115 / 149 题（77.2%）**，另有 **34 题孤题**。

| 母题编号 | 母题名（一句话数学描述） | 成员（年份/卷别/题号） | 数 | 首现 | 末现 | 仍在考 | 变化趋势 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ALG-M01 | 幂迹刚性：对称幂和决定特征值，迹的代数整数性下降 | 13T2, 16I3, 17T2, 20I1 | 4 | 2013 | 2020 | 否 | 升要求 |
| ALG-M02 | 有限群的阶数决定结构：Sylow 计数、正规子群与半直积分类 | 10T6\*, 11I6, 13I1, 14T4, 16I5, 18I3 | 6 | 2010 | 2018 | 否 | 换皮（中期一次升要求） |
| ALG-M03 | 元素阶约束下的亚循环群与其在有限域上的不可约表示 | 15T2, 25I2 | 2 | 2015 | 2025 | **是** | 升要求 |
| ALG-M04 | 有限域上线性群：阶、Sylow 子群、生成元与可解性 | 11T5, 12I2, 12T2, 13T3, 23I1 | 5 | 2011 | 2023 | **是** | 换皮（11/12 原样重复） |
| ALG-M05 | 共轭类数与类方程：用类数控制群的大小与分类 | 10I3, 16T5 | 2 | 2010 | 2016 | 否 | 升要求 |
| ALG-M06 | 有限群表示论：不可约表示、特征标取值与忠实表示 | 10I6, 11I2, 13T4, 14I1, 18T4, 19I1, 24I1 | 7 | 2010 | 2024 | **是** | 换皮 + 升要求 |
| ALG-M07 | 张量平方的不变量空间与双中心化子 | 12I3, 14T5 | 2 | 2012 | 2014 | 否 | 升要求 |
| ALG-M08 | 不变量环与 Molien 公式：矩阵群作用下的多项式不变量 | 15I2, 15T4, 19T2 | 3 | 2015 | 2019 | 否 | 换皮 + 升要求 |
| ALG-M09 | SL2 的对称幂表示与 Clebsch–Gordan 分解 | 10T6\*, 13I4 | 2 | 2010 | 2013 | 否 | 升要求 |
| ALG-M10 | Fitting 引理与局部自同态环：不可分解对象的自同态 | 16T4, 17I2, 18T1 | 3 | 2016 | 2018 | 否 | 换皮 |
| ALG-M11 | p 进单位群：Teichmüller 提升、对数同构与 p 次幂判别 | 12T6, 20I5, 23I6 | 3 | 2012 | 2023 | **是** | 升要求 |
| ALG-M12 | 非阿基米德域的完备性与球完备性 | 20I6, 21I6, 24I5 | 3 | 2020 | 2024 | **是** | 换皮（含一次升要求） |
| ALG-M13 | 局部域扩张：不分叉扩张与半线性 Galois 下降 | 25I4, 26I5 | 2 | 2025 | 2026 | **是** | 升要求 |
| ALG-M14 | 可除群与 $\mathbb Z_p$：自同态环与连续表示 | 17I1, 23I5 | 2 | 2017 | 2023 | **是** | 升要求 |
| ALG-M15 | Chevalley–Warning 定理：低次方程组必有非零解 | 14I5, 17I4 | 2 | 2014 | 2017 | 否 | 升要求（用定理 → 证定理） |
| ALG-M16 | 有限域上不可约多项式的计数与参数化 | 13I3, 13T5 | 2 | 2013 | 2013 | 否 | 原样重复（同年两卷各一） |
| ALG-M17 | Artin–Schreier 扩张与 Hilbert 90 | 17T4, 19T5, 21I1 | 3 | 2017 | 2021 | **是** | 换皮 |
| ALG-M18 | 用代数数论（范形式、类数）求丢番图方程的整数解 | 14T6, 21I5 | 2 | 2014 | 2021 | **是** | 换皮 |
| ALG-M19 | 局部-整体原则的失效：处处局部可解而无整体解 | 13I5, 14I3 | 2 | 2013 | 2014 | 否 | 换皮 |
| ALG-M20 | 数域整数环中理想与元素的生成与互素 | 22I4, 26I3 | 2 | 2022 | 2026 | **是** | 换皮 |
| ALG-M21 | 曲线坐标环与函数域的整闭包（正规化） | 20I3, 21I3, 24I4 | 3 | 2020 | 2024 | **是** | 换皮 + 升要求 |
| ALG-M22 | 数域的判别式与整基 | 22I6, 26I4 | 2 | 2022 | 2026 | **是** | 换皮（一般三次域 → 纯三次域） |
| ALG-M23 | 分圆域、单位根与分圆多项式模 p | 15T3, 18T3, 19T4, 20I4, 22I5, 24I6 | 6 | 2015 | 2024 | **是** | 升要求 |
| ALG-M24 | 显式多项式的分裂域、Galois 群与子域格 | 10I4, 10T4, 13T6, 15T6, 16T3, 21I2, 25I5 | 7 | 2010 | 2025 | **是** | 换皮 + 升要求 |
| ALG-M25 | 素数分解律：惯性次数与剩余符号 | 15I3, 18I2 | 2 | 2015 | 2018 | 否 | 升要求 |
| ALG-M26 | 二次扩张、平方类群与 $(\mathbb Z/2)^n$-Galois 扩张 | 21I4, 22I1, 25I1 | 3 | 2021 | 2025 | **是** | 升要求 |
| ALG-M27 | SL2(Z) 及其同余子群的生成元与陪集分解 | 11T6, 14T1, 26I1 | 3 | 2011 | 2026 | **是** | 升要求 |
| ALG-M28 | 正交变换的反射分解 | 12T3, 15T1, 16I4 | 3 | 2012 | 2016 | 否 | 升要求 |
| ALG-M29 | 有限域上的乘法特征与点数计数（Legendre / Jacobi 和） | 19I5, 26I2 | 2 | 2019 | 2026 | **是** | 升要求 |
| ALG-M30 | 自由模的秩与 PID 上的子模 | 11T2, 23I2 | 2 | 2011 | 2023 | **是** | 升要求 |
| ALG-M31 | 投射模、平坦模与有限表现 | 22I2, 23I4 | 2 | 2022 | 2023 | **是** | 升要求 |
| ALG-M32 | 二项式系数、整值多项式与 p 进估值 | 11T4, 16T2, 18T2 | 3 | 2011 | 2018 | 否 | 换皮 |
| ALG-M33 | 公共特征向量与不变子空间的存在性 | 10I1, 11I4, 13I2 | 3 | 2010 | 2013 | 否 | 换皮 + 升要求 |
| ALG-M34 | 交换性的定量后果：矩阵对的行列式/范数不等式 | 14I6, 17I5 | 2 | 2014 | 2017 | 否 | 升要求 |
| ALG-M35 | 矩阵共轭性的判定：特征多项式何时决定相似类 | 10I2, 14T3 | 2 | 2010 | 2014 | 否 | 升要求 |
| ALG-M36 | 三角函数连乘积与分圆计算 | 10T3, 14T2 | 2 | 2010 | 2014 | 否 | 原样重复（2014 逐字重出） |
| ALG-M37 | 非负整数线性组合的表示与生成函数（数值半群） | 10I5, 17T5 | 2 | 2010 | 2017 | 否 | 换皮 |
| ALG-M38 | Cauchy 型矩阵与 Gram 矩阵的正定性 | 12T1, 14I2 | 2 | 2012 | 2014 | 否 | 换皮 |
| ALG-M39 | 特征 p 的函数域与不可分扩张 | 19I2, 24I3 | 2 | 2019 | 2024 | **是** | 升要求 |
| ALG-M40 | 线性群的拓扑：连通性与基本群 | 12T4, 19I4 | 2 | 2012 | 2019 | 否 | 换皮 |
| ALG-M41 | 无限 Galois 理论与 profinite 群 | 17I3, 23I3 | 2 | 2017 | 2023 | **是** | 升要求 |

\* 10T6 是合并题面，同时属于 ALG-M02 与 ALG-M09（见 §0.1 第 2 条）。

---

## §2 逐母题解剖

> 每节给出：**数学内核**（这题到底在考什么）→ **成员与年际差异** → **递进关系** → **标准解法骨架（3–8 步）** → **最容易卡住的一步**。

### ALG-M01 幂迹刚性：幂和决定特征值

**数学内核.** $A$ 的幂和 $p_k=\operatorname{tr}(A^k)$ 是特征值的初等对称函数的多项式（Newton 恒等式）。因此**只要知道全部幂和属于哪个域/哪个环，就控制了特征值的性质**；反过来，$A$ 是否幂零、$A$ 与 $B$ 是否同特征多项式，都等价于无穷多条幂和的等式。这是一条"把矩阵问题搬进特征值对称函数环"的通道。

**成员与差异**
- **13T2**：$E/F$ 域扩张，$A\in M_m(E)$ 且 $\operatorname{tr}(A^n)\in F$（$n\ge 2$）$\Rightarrow \operatorname{tr}(A)\in F$。差别：**只给 $n\ge2$**，故意扣掉 $n=1$ 这一条；靠 Cayley–Hamilton 造出 $F$-系数的递推关系 $\sum b_i \operatorname{tr}(A^{i+k})=0$（$k\ge2$），再用特征值 $t_i$ 与 $Q(t_i)=0$ 及"重数在 $F$ 中可逆"把 $\operatorname{tr}(A)$ 拽回 $F$。
- **16I3**：把"域"升级成"代数整数环"：$\operatorname{tr}(A^n)$ 全为代数整数（且允许 $n\ge N$ 起步）$\Rightarrow$ 特征值全为代数整数。差别：结论对象从迹换成每个特征值 $a_i$，需要先写 $a_i^n=\sum_j b_{ij}t_{n+j-1}$ 把 $a_i$ 表示成整数的有限组合，再引"$R[a]$ 落在有限生成 $R$-模中则 $a\in R$"这条代数整数判别法。
- **17T2**：$p>2$，$T$ 在 $\mathbb Q$-向量空间上阶为 $p$。差别：把"幂和给定"换成"算子本身阶有限"，于是特征值是 $p$ 次单位根（代数整数、Galois 不变 ⟹ 有理 ⟹ 整数），再加一步模 $p$ 同余 $\operatorname{tr}(T)\equiv n \pmod p$（用 $\zeta\equiv1 \bmod (1-\zeta)$）。
- **20I1**：把整条技术链**正面写出来并要求证明**：先证 Newton 恒等式 $p_k-p_{k-1}e_1+\cdots+(-1)^{k-1}p_1e_{k-1}+(-1)^k k e_k=0$，再推出"$A$ 幂零 $\iff$ 所有 $\operatorname{tr}(A^k)=0$"与"$A,B$ 同特征多项式 $\iff$ 幂和全同"。差别：这一年不再藏技巧，直接考恒等式本身。

**递进关系（升级链）**
13T2（迹的域下降，$n\ge2$）→ 16I3（换成代数整数环，结论细到每个特征值）→ 17T2（算子有限阶，加模 $p$ 同余）→ 20I1（要求证明 Newton 恒等式这一底层工具本身）。**要求逐级上抬：从"用一个引理"到"造一个引理"到"证这个引理"。**

**标准解法骨架**
1. 记特征值 $a_1,\dots,a_m$（在代数闭包中），$p_k=\sum a_i^k$ 是初等对称函数的整系数多项式（Newton 恒等式）。
2. 由 Cayley–Hamilton 得特征多项式 $\chi_A(t)=t^m+c_1t^{m-1}+\cdots+c_m$；由 Newton 恒等式把 $c_i$ 写成 $p_1,\dots,p_i$ 的有理函数。
3. 若已知 $p_k\in F$（或为代数整数）对足够多 $k$ 成立，则 $c_i$ 也落在同一个小环里（注意分母 $k!$ 的可逆性——这正是 13T2 要假设"重数可逆"的原因）。
4. 用 $Q(t)=\sum b_i t^i$ 作用在特征值上：$\sum_i b_i \operatorname{tr}(A^{i+k})=\sum_j m_j t_j^k \,Q(t_j)=0$。
5. 若某个 $t_j$ 是 $Q$ 的根，则由 $Q(t_j)=0$ 与常项为 1 得到 $t_j$ 是其余 $t$ 的整系数组合（代数整数性）；若不成立则得到 $t_j$ 与其它特征值的关系式，再回代 $m_j$。
6. 求和 $\operatorname{tr}(A)=\sum m_j t_j$，逐项检查落在目标环内。
7. （20I1 型）反方向：幂和全为 0 $\Rightarrow e_k=0$ $\Rightarrow$ 特征多项式为 $t^m$ $\Rightarrow$ 幂零。

**最容易卡住的一步**：第 3 步中 $k!$ 是否可逆。13T2 特意假设"特征值重数在 $F$ 中可逆"，16I3 特意把 $F$ 换成特征 0 的代数整数环——**丢开这个假设，Newton 恒等式立刻断链**。多数人会把 $\operatorname{tr}(A^k)$ 当成纯粹的"数值条件"而忽略分母问题。

### ALG-M02 有限群的阶数决定结构

**数学内核.** 给定 $|G|$ 的算术分解，用 Sylow 定理做**计数**（$n_p\equiv1\bmod p$ 且 $n_p\mid |G|/p^{a}$），把"某个 Sylow 子群必须正规"逼出来，再用正规子群 + 商群做半直积/直积分类，或直接推出矛盾（非单、交换）。核心不是"用 Sylow 定理"，而是**用 $n_p$ 的整除约束做排除法**。

**成员与差异**
- **10T6 / 11I6**（**逐字相同**："Prove that a group of order 150 is not simple."）：$150=2\cdot3\cdot5^2$，$n_5\mid6$ 且 $\equiv1\bmod5$ $\Rightarrow n_5=1$，正规 $\Rightarrow$ 不单。这是本母题的"种子题"，两年原样重出。
- **13I1**：$|G|=26=2\cdot13$，要求**分类**（$\mathbb Z/26$ 或 $D_{26}$）并求 $\operatorname{Aut}(G)$。差别：从"证明不单"升级为"完全分类 + 自同构群"。
- **14T4**：$|G|=8$ 的分类。差别：$p$-群情形，Sylow 论不管用，改用中心非平凡 + 商群归纳（$|G/Z|$ 只能是 2 或 4）。
- **16I5**：$|G|=2^nm$（$m$ 奇），$G$ 有 $2^n$ 阶元 $\Rightarrow G$ 有 $m$ 阶正规子群。差别：把"用 Sylow 排除"换成"构造性归纳"——用左乘的符号同态 $G\to\{\pm1\}$ 造出指数 2 的正规子群，再对 $n$ 归纳。
- **18I3**：$|G|=99=9\cdot11$，证交换。差别：Sylow 计数（$n_{11}=1$）+ 自同构群阶数整除（$\operatorname{Aut}(\mathbb Z_{11})$ 的 3 阶子群必平凡）双重限制，结论是"交换"。

**递进关系**
10T6/11I6（只证不单）→ 13I1（完全分类 + Aut）→ 14T4（换成 $p$-群，方法从 Sylow 计数换成中心归纳）→ 16I5（换成构造性正规子群存在性）→ 18I3（换成交换性）。**不是单调升要求，而是同一个计数骨架在不同阶数上的复用**。

**标准解法骨架**
1. 分解 $|G|=\prod p_i^{a_i}$，列出每个 $n_{p_i}$ 满足的两个约束（$n_{p_i}\equiv1\bmod p_i$，$n_{p_i}\mid |G|/p_i^{a_i}$）。
2. 若某个 $n_{p_i}=1$，该 Sylow 子群正规，进入第 5 步；否则统计"非正规 Sylow 子群贡献的元素个数"（同阶 Sylow 子群两两交于较小子群）。
3. 若元素计数超过 $|G|$，矛盾 ⇒ 某个 $n_p$ 必为 1。
4. 对 $p$-群：用 $Z(G)\ne1$，把 $G/Z(G)$ 拉到更小的阶数上归纳（14T4）。
5. 有了正规子群 $N$，看 $G/N$ 与 $N$ 的结构，用 $\operatorname{Aut}(N)$ 的信息判定扩张是直积还是半直积；若 $\operatorname{Aut}(N)$ 的阶与 $|G/N|$ 互素，则扩张必平凡。
6. 对分类题再补一步：验证构造出的每个群确实不同构（比较元素阶谱或中心）。

**最容易卡住的一步**：第 2–3 步的**元素计数**。多数人只会背"$n_p\equiv1\bmod p$"，不会主动去数非正规 Sylow 子群贡献的元素个数（如 $|G|=150$ 时 $n_5\mid6$ 与 $\equiv1\bmod5$ 已经只剩 $n_5=1$ 与 $n_5=6$ 两种，$n_5=6$ 会贡献 $6\times20=120$ 个 5 阶元，加上 $n_3$ 的情形就爆掉）。

### ALG-M03 元素阶约束下的亚循环群与其有限域表示

**数学内核.** 当一个有限群**所有非平凡元素的阶只取两个素数 $p,q$**（或由两条关系 $\sigma^f=\tau^e=1,\ \sigma\tau\sigma^{-1}=\tau^p$ 生成）时，群必然是 $\mathbb Z/q^n\rtimes\mathbb Z/p$ 型亚循环群，而对 $\mathbb F_q$（更一般 $\mathbb F_{p^f}$）的作用矩阵的特征值必须是**本原 $p$ 次单位根**。于是"群论问题"被翻译成"$\mathbb F_q$ 上矩阵的特征值与不可约性"问题——包括有限域上不可约表示与绝对不可约表示的差别。

**成员与差异**
- **15T2**：$p\ne q$ 素数，所有非平凡元阶为 $p$ 或 $q$，$q$-Sylow $H_q$ 正规且非平凡交换。结论：$G\cong(\mathbb Z/p)\ltimes(\mathbb Z/q)^n$，$1$ 的作用矩阵 $M(1)\in GL_n(\mathbb F_q)$ 的特征值全为本原 $p$ 次单位根。差别：**从阶条件出发**反推出半直积形状，并证明 $M$ 单射、$H_p\cong\mathbb Z/p$。
- **25I2**：**从关系出发**（$\sigma^f=1,\tau^e=1,\sigma\tau\sigma^{-1}=\tau^p$），先证明这样的群存在且唯一 $\iff p^f\equiv1\bmod e$；再证 $G$ 在 $A=\mathbb F_{p^f}$ 上的三条等价：绝对不可约 $\iff$ 不可约 $\iff p$ 在 $(\mathbb Z/e)^\times$ 中阶为 $f$。

**递进关系（升级链）**
15T2（给定群的阶条件，证明它是亚循环群且作用矩阵特征值是本原 $p$ 次单位根）→ 25I2（给定生成关系，先证**存在唯一性判据** $p^f\equiv1\bmod e$，再把"不可约"细分为"$\mathbb F_p$-不可约"与"绝对不可约"并给出判别）。要求从"验证形状"抬到"刻画存在性 + 表示论精细判据"。

**标准解法骨架**
1. 用 Sylow 把 $G$ 拆成 $G=H_p\ltimes H_q$，$H_q\cong(\mathbb Z/q)^n$（15T2）或 $G=\mathbb Z/e\rtimes\mathbb Z/f$（25I2）。
2. 写出共轭作用 $M:H_p\to \operatorname{Aut}(H_q)\cong GL_n(\mathbb F_q)$。
3. 对 $1\ne a\in H_p$，$M(a)^p=I$，故极小多项式整除 $x^p-1=(x-1)(x^{p-1}+\cdots+1)$；用"$H_p$ 中元素阶为 $p$"排除 $M(a)$ 有特征值 1 的可能（否则不动点集非平凡，与"所有非平凡元素阶为 $p$ 或 $q$"矛盾）。
4. 于是特征值全为本原 $p$ 次单位根 ⇒ $M$ 单射 ⇒ $p\mid q^k-1$ 型条件 ⇒ $H_p\cong\mathbb Z/p$。
5. （25I2）把 $A=\mathbb F_{p^f}$ 看成 $\mathbb F_p[G]$-模，用 Schur/有限域上不可约性判据：$\mathbb F_p$-不可约 $\iff$ 中心化子 $=\mathbb F_{p^f}$ $\iff \operatorname{ord}_e(p)=f$；绝对不可约再抬一步。
6. 反方向：由 $p^f\equiv1\bmod e$ 直接构造 $\mathbb Z/e\rtimes\mathbb Z/f$，并证唯一性。

**最容易卡住的一步**：第 3 步——**为什么 $M(a)$ 不能有特征值 1**。这一步同时用掉"所有非平凡元素阶为 $p$ 或 $q$"这条假设；漏掉它就只能得到"特征值是 $p$ 次单位根"，得不到"本原"。

### ALG-M04 有限域上线性群：阶、Sylow 子群、生成元与可解性

**数学内核.** $GL_n(\mathbb F_q)$ 与 $SL_n(\mathbb F_q)$ 是可被完全算清楚的群：阶为 $q^{n(n-1)/2}\prod_{i=1}^n(q^i-1)$，$p$-Sylow 就是单位上三角群，$p$-Sylow 的个数$=(q^n-1)\cdots(q^n-q^{n-1})/q^{n(n-1)/2}$，正规化子是上三角（Borel）子群；另一面，初等矩阵 $E_{ij}(\lambda)$ 生成 $SL_n$，换位子 $[E_{ij}(\lambda),E_{kl}(\mu)]$ 生成更小的子群，从而给出可解性判据。**这题在考"矩阵群的显式计算能力"**——能把群阶拆因子、能把 Sylow 写出来、能用换位子做导出列。

**成员与差异**
- **11T5**：$GL_3(\mathbb F_7)$：找出 7-Sylow $P_7$、求其正规化子 $N$、再找一个 2-Sylow。差别：最具体的一版，只考 $n=3,q=7$。
- **12T2**：**与 11T5 逐字相同**（同一道题在 team 卷里重出）。这是本库中最直白的一次"原样重复"。
- **12I2**：一般 $n,p$：算 $|GL_n(\mathbb F_p)|$、给出 $p$-Sylow、算 $p$-Sylow 的个数。差别：从具体 $(3,7)$ 升到一般 $(n,p)$。
- **13T3**：$G=SL_2(\mathbb F_p)$：求阶，并证明每个元素的阶整除 $p^2-1$ 或 $2p$。差别：换成 $SL_2$，"元素阶"视角（用 $SL_2$ 作用在 $\mathbb P^1(\mathbb F_p)$ 上的轨道结构）。
- **23I1**：由初等矩阵 $E_{ij}(\lambda)$ 生成 $SL_n(F)$；$n\ge3$ 时 $GL_n(F)$ 不可解（算换位子）；$n=2$ 且 $|F|\ge4$ 时也不可解；最后判定 $GL_2(\mathbb F_2)$、$GL_2(\mathbb F_3)$ 是否可解。差别：**视角从计数换成生成与导出列**，并且故意留下两个有限域的例外。

**递进关系（换皮链）**
11T5 = 12T2（具体 $(3,7)$，Sylow 计算）→ 12I2（一般 $(n,p)$ 计数）→ 13T3（换 $SL_2$，考元素阶）→ 23I1（换方法：初等矩阵生成 + 换位子 + 可解性，并考察两个 $\mathbb F_2,\mathbb F_3$ 反例）。**同一条主线的四个不同侧面。**

**标准解法骨架**
1. 把矩阵按列看成有序基：$GL_n(\mathbb F_q)$ 的阶 $=(q^n-1)(q^n-q)\cdots(q^n-q^{n-1})$。
2. $p$-Sylow：单位上三角群 $U$（对角全 1）阶恰为 $q^{n(n-1)/2}=p^{v_p(|G|)}$。
3. $p$-Sylow 个数 $=|G|/|N_G(U)|$；$N_G(U)$ 是 Borel（可逆上三角），阶 $=(q-1)^n q^{n(n-1)/2}$。
4. 生成性：$E_{ij}(\lambda)=I+\lambda e_{ij}$，用 $[E_{ij}(\lambda),E_{jk}(\mu)]=E_{ik}(\lambda\mu)$（$i\ne k$）与对角矩阵的共轭把 $SL_n$ 逐步生成出来；$GL_n$ 再加行列式调节（对角 $\operatorname{diag}(\lambda,1,\dots,1)$）。
5. 可解性：导出子群 $[GL_n,GL_n]\supseteq SL_n$，而 $SL_n$（$n\ge3$）是完美群（等于自己的换位子群）⇒ 导出列不终止 ⇒ 不可解。
6. 例外：$GL_2(\mathbb F_2)\cong S_3$、$GL_2(\mathbb F_3)$ 阶 48 可解，逐个验证。

**最容易卡住的一步**：第 5 步——**证明 $SL_n$ 等于自己的换位子群**。需要至少三条换位子恒等式（$[E_{ij},E_{jk}]=E_{ik}$、$[E_{ij}(\lambda),\operatorname{diag}]$ 给出对角元、再用 $[E_{ij},E_{ji}]$ 造对角）才能把任意初等矩阵写成换位子。只算出一两个换位子就断言"不可解"是这套题最常见的失分点。

### ALG-M05 共轭类数与类方程

**数学内核.** 类方程 $|G|=\sum_i |G|/|C_G(x_i)|$ 与 $1=\sum_i 1/n_i$（$n_i=|C_G(x_i)|$）把**共轭类的个数**与群的阶绑死。共轭类少 $\Rightarrow$ 群"接近交换"、交换子群指数小；共轭类数固定 $\Rightarrow$ 只有有限多个群。这题在考"用类数这个计数不变量反过来约束群"。

**成员与差异**
- **10I3**：$G$ 非交换有限群，$c(G)=$ 共轭类数$/|G|$。(a) 证 $c(G)\le5/8$；(b) 问 $c(H)=5/8$ 是否存在（$D_8$、$Q_8$ 达到）；(c) 开放题：若存在素数 $p$ 与元素 $x$ 使 $x$ 的共轭类大小被 $p$ 整除，求 $c(G)$ 的尖锐上界。差别：**求最优常数**，属于"极值型"。
- **16T5**：先证 $1=\sum_{i=1}^h 1/n_i$；(b) 对任意 $h$，只有有限多个恰有 $h$ 个共轭类的群；(c) 找出恰有 3 个共轭类的所有有限群。差别：**从极值常数换成有限性与分类**；$1=\sum1/n_i$ 配合"$n_i$ 有上界"给出有限性。

**递进关系**
10I3（非交换 + 求 $c(G)$ 的尖锐上界 $5/8$）→ 16T5（类方程恒等式 + 固定类数的**有限性定理** + 3 类群的分类）。从"一个常数"升到"一整套结构性结论"。

**标准解法骨架**
1. 写类方程 $|G|=\sum_{i=1}^h |G|/n_i$，两边除以 $|G|$ 得 $1=\sum 1/n_i$。
2. 对非交换 $G$：中心 $Z(G)\ne G$，$Z(G)$ 中每个元素自成一类，贡献 $|Z(G)|$ 个类；把这些项放进 $c(G)$ 的表达式 $c(G)=(|Z(G)|+\sum_{\text{非中心}}1/n_i)/|G|$。
3. 用 $|G/Z(G)|$ 与 $n_i\le |G|/2$（非中心元素的中心化子真包含 $Z(G)$，指数 $\ge2$）得到 $c(G)\le 1/2+|Z(G)|/(2|G|)$ 型不等式。
4. 用"$G/Z(G)$ 非交换"（否则 $G$ 交换）给出 $|G/Z(G)|\ge6$，代回得到 $5/8$ 并检查等号可达（$D_8$、$Q_8$）。
5. 有限性：由 $1=\sum1/n_i$ 与 $n_i\ge2$ 得 $h\le$ 由 $\sum1/n_i\le1$ 控制，$\min n_i$ 有界 ⇒ $|G|=|C_G(x_1)|\cdot n_1$ 有界；再对剩下的 $n_i$ 归纳。
6. 分类 $h=3$：$1=1/|G|+\sum_{i\ge2}1/n_i$ 且 $n_i\mid|G|$，枚举得 $|G|\in\{3,4,6\}$ 型有限个候选，逐个验证。

**最容易卡住的一步**：第 3–4 步里 **$|G/Z(G)|$ 不可能是素数**（否则 $G$ 交换）这条被反复用到，却最容易被写成"$|Z(G)|$ 很小"含糊过去。$5/8$ 这个常数恰恰是由 $|G/Z(G)|\ge6$ 卡出来的。

### ALG-M06 有限群表示论：不可约表示、特征标取值与忠实表示

**数学内核.** 特征标是定义在共轭类上的类函数，$\chi(g)$ 是若干单位根之和（$|\chi(g)|\le\dim V$，等号 $\iff g$ 是纯量），且全体 $\chi(g)$ 是代数整数、对 Galois 群封闭。**用"特征标能取哪些值"这个刚性去反推群的结构**（如不可约特征标必有零点、$g$ 与 $g^k$ 共轭），是本母题最核心的一条线；另一半是"具体群的不可约表示怎么算出来"。

**成员与差异**
- **10I6**：描述 $S_4$ 的所有不可约复表示。差别：最原始的一版，只要求分类（3 个来自 $S_4\to S_3$ 的一维、标准表示去掉平凡、以及 2 维的 tensor 型）。
- **13T4**：$S_4$ 的不可约表示 **+ 完整特征标表**。差别：同一对象（$S_4$）但多要一张表——典型的"原对象升要求"。
- **11I2**：$f$ 是 2 维复表示且每个 $f(\sigma)$ 都以 1 为特征值 $\Rightarrow f$ 分裂为两个一维。差别：不指定群，用"特征值全体含 1"这一约束做**表示论层面的刚性**。
- **14I1**：$G\le GL(V)$ 有限。(a) 纯量元组成的 $H$ 正规且 $h\mapsto\eta(h)$ 是单同态；(b) $|\chi_V(g)|\le n$ 且等号 $\iff g\in H$；(c) 任何不可约 $W$ 都是某个 $V^{\otimes m}$ 的直和项。差别：把"特征标的界"与"张量幂生成整个表示环"两件事绑在一起考。
- **18T4**：$B(\chi)=\prod_{\sigma\in\operatorname{Gal}}\prod_{g\in G}\sigma(\chi(g))\in\mathbb Z$；若 $\chi$ 不可约且 $\dim V\ge2$，则存在 $g$ 使 $\chi(g)=0$。差别：**代数整数性 + 算术-几何平均不等式**，是全线里技术最硬的一道。
- **19I1**：所有特征标取有理值，$g^{2019}=1$ $\Rightarrow g$ 与 $g^{19}$ 共轭。差别：用"有理值 $\Rightarrow$ 特征标被 Galois 群固定 $\Rightarrow$ 幂映射在共轭类上良定义"这条通道。
- **24I1**：忠实表示的存在性：任意有限群有忠实 $K$-线性表示；忠实一维复表示 $\iff G$ 循环；$G$ 交换时忠实 $n$ 维复表示 $\iff G$ 可由 $n$ 个元素生成；分类有忠实 2 维实表示的有限群。差别：**从"算特征标"转向"表示的存在性与忠实性"**，用到正则表示与实表示的 Frobenius–Schur 型判据。

**递进关系（升级链）**
10I6（只分 $S_4$）→ 13T4（$S_4$ + 特征标表）→ 11I2（换成"特征值约束"的抽象刚性）→ 14I1（特征标界 + 张量幂生成）→ 18T4（代数整数 + AGM 不等式逼出零点）→ 19I1（有理值特征标 + 幂映射共轭）→ 24I1（忠实表示与生成元数目）。**从"具体群算表"一路升到"用特征标值反推群结构"，最后转到忠实表示。**

**标准解法骨架**
1. 由共轭类数 $=$ 不可约表示个数，先数类。
2. 用一维表示（$G^{ab}$ 的特征标）、置换表示分解、张量积与对称/外幂造出候选不可约表示。
3. 用 $\sum (\dim)^2=|G|$ 与特征标正交关系验证它们确实互不同构且穷尽。
4. 特征标值的代数整数性：$\chi(g)$ 是 $\dim V$ 个单位根之和，故是代数整数，且 $\sigma(\chi(g))=\chi(g^k)$ 对 $\sigma:\zeta\mapsto\zeta^k$ 成立。
5. 不可约 $\chi$（$\dim\ge2$）的零点：$\prod_g\chi(g)$ 是代数整数又在 Galois 下不变 ⇒ 有理整数；$|B(\chi)|^2$ 用 AGM 与 $|\chi(g)|\le\dim V$ 夹逼，逼出某个 $\chi(g)=0$。
6. 有理值特征标 + $g^{2019}=1$：对每个 $k$ 与 $2019$ 互素的 $k$，$g\mapsto g^k$ 把共轭类映到共轭类（因为 $\chi(g^k)=\chi(g)$ 对所有 $\chi$）；取 $k$ 使 $k\equiv19\pmod{2019}$ 且 $(k,2019)=1$。
7. 忠实表示：正则表示给出 $K$-忠实；一维忠实 $\iff G\hookrightarrow\mathbb C^\times\iff$ 循环；交换情形用 $\bigoplus$ 特征标（把 $G$ 嵌入 $n$ 个 $\mathbb C^\times$）$\iff$ $n$ 个生成元。

**最容易卡住的一步**：**第 5 步的 AGM 夹逼**（18T4）。要同时用上"$B(\chi)$ 是非零整数"（故 $|B(\chi)|\ge1$）、"$|\chi(g)|\le\dim V$"以及"若所有 $\chi(g)\ne0$ 则几何平均严格小于算术平均"，三者合起来才逼出矛盾。多数人卡在想不到用 $\prod_g|\chi(g)|$ 这个全局量。

### ALG-M07 张量平方的不变量空间与双中心化子

**数学内核.** $V^{\otimes2}$ 上的不变量空间 $(V\otimes V)^G$ 与 $\operatorname{End}_G(V)$（$G$-等变自同态）维数相同，这是**双中心化子定理**的初等形态。对正交群 $O(V)$：$V\otimes V=\operatorname{Sym}^2\oplus\Lambda^2$，$O(V)$ 保持型 $\langle,\rangle$ 因而保持 Casimir 型张量 $\sum e_i\otimes e_i$，故不变量空间 1 维（由 1 与 $\operatorname{End}_{O(V)}(V)\cong\mathbb C$ 生成）。**这题在考"用最高权/不可约分解来数不变量"。**

**成员与差异**
- **12I3**：$V$ 复有限维带非退化对称双线性型，证 $(V\otimes_{\mathbb C}V)^{O(n)}$ 是 1 维。差别：只要结论（1 维），直接算。
- **14T5**：同一定义下，(a) **证同构** $(V\otimes V)^{O(V)}\cong\operatorname{End}_{O(V)}(V)$ 并把同构显式构造出来；(b) 再推出 1 维。差别：从"证明维数"升级为"给出同构 + 再推维数"。

**递进关系**：12I3（断言 1 维）→ 14T5（先把不变量空间与等变自同态环划等号，再导出 1 维）。**典型的"同一结论，要求补上机制"。**

**标准解法骨架**
1. 把 $V\otimes V$ 写成 $\operatorname{Sym}^2V\oplus\Lambda^2V$，$O(V)$ 保持该分解。
2. $\operatorname{Sym}^2V$ 作为 $O(V)$-模含一个一维不变子空间（由 $(\cdot,\cdot)$ 对应的 Casimir 张量 $\sum e_i\otimes e_i$ 张成）。
3. 剩余部分 $\operatorname{Sym}^2_0V\oplus\Lambda^2V$ 与 $\operatorname{End}_0(V)$（迹为零的等变自同态）同构，且无非零不变量。
4. 一般地：$\operatorname{Hom}_G(\mathbb C, V\otimes V)=\operatorname{Hom}_G(V^*,V)$，取型给出 $V\cong V^*$，于是 $(V\otimes V)^G\cong\operatorname{End}_G(V)$。
5. $O(V)$ 意义下 $\operatorname{End}_{O(V)}(V)=\mathbb C\cdot \operatorname{id}$（Schur 型论证：$O(V)$ 的不可约性 + 保持型），维数 1。
6. 汇合两步得 $\dim(V\otimes V)^{O(V)}=1$。

**最容易卡住的一步**：第 4 步**把不变量空间翻译成 $\operatorname{End}_G(V)$**。用 $\operatorname{Hom}(\mathbb C,W)=\operatorname{Hom}_G(\mathbb C,W)^G\otimes$ 型同构需要先把 $V\otimes V\cong V\otimes V^*\cong\operatorname{End}(V)$ 通过型识别出来——这一步的"型给出同构"是整题枢纽。

### ALG-M08 不变量环与 Molien 公式：矩阵群作用下的多项式不变量

**数学内核.** 若有限群 $G$ 作用在 $V$ 上，则不变量环的分次维数 $\dim (\mathbb C[V]_n)^G$ 由 **Molien 公式** $\sum_n a_n t^n=\frac1{|G|}\sum_g \frac1{\det(1-\pi(g)t)}$ 完全算出；把它用在矩阵空间 $\operatorname{End}(V)$ 上（$G\times G$ 左右作用）就得到**矩阵不变量第一基本定理**：不变量都是迹的单项式。**这题在考"用群作用下的平均投影把不变量算出来"。**

**成员与差异**
- **15T4**：$G$ 有限，$(\pi,V)$ 有限维 $\mathbb C G$-模，$a_n(\rho)$ 为 $\rho$ 在 $\mathbb C[V]_n$ 中的重数，证 $\sum_n a_n(\rho)t^n=\frac1{|G|}\sum_g \frac{\chi_\rho(g)}{\det(\operatorname{id}-\pi(g)t)}$。差别：**对偶形式**（带 $\chi_\rho$），本质是 Molien 公式的等变版。
- **15I2**：$O_n(\mathbb C)$ 作用在 $M_{n\times k}(\mathbb C)$ 上，把满足 $f(gx)=\det(g)^if(x)$ 的有理函数空间 $F_0,F_1$ 的结构搞清楚（用 $Q(x)=x^tx$ 刻画非退化点、$k<n$ 时 $F_1=0$、$k\ge n$ 时 $F_1$ 是 $F_0$ 上秩 1 自由模）。差别：**换成行列式扭变（半不变量）**这一新对象。
- **19T2**：$V=\mathbb C^2$，$G=SL_2(\mathbb C)$，算 $\mathbb C[\operatorname{End}(V)]^{G\times G}$。差别：**从"分次维数"换成"环的具体生成元"**——答案是迹的单项式生成的环（第一基本定理）。

**递进关系**：15T4（把不变量数目算成分母行列式的平均）→ 15I2（带 $\det^i$ 扭变、并处理退化点）→ 19T2（算出环本身，得到 FFT）。**从"数个数"升到"描述环"。**

**标准解法骨架**
1. 取平均投影 $\pi_G=\frac1{|G|}\sum_{g}\pi(g)$，它把任意模投到不变量子空间上。
2. 把它作用在 $\operatorname{Sym}^n V^*$ 上：迹即 $\dim (\mathbb C[V]_n)^G$。
3. 对每个 $g$，在 $g$ 的特征基下算 $\operatorname{tr}(\operatorname{Sym}^n g)$，用母函数 $\sum_n \operatorname{tr}(\operatorname{Sym}^n g)t^n=\frac1{\det(1-tg)}$（等变版换成 $\frac{\chi_\rho(g)}{\det(1-tg)}$）。
4. 交换求和次序得 Molien 公式。
5. (15I2) 在开集 $\det Q(x)\ne0$ 上先算，利用 $O_n(\mathbb C)$ 的可迁性把点约化为标准形；用 $g|_{V_x}=1,\det g=-1$ 的构造证明 $F_1$ 在一般点为零。
6. (19T2) 用 Weyl 整形化或直接对 $\operatorname{End}(V)$ 的坐标做不变量计算，得到 $\mathbb C[\operatorname{tr}(X^{i_1})\cdots]$ 型生成元，再用第一基本定理断言无其它关系。
7. 汇合：一般不变量环有限生成（Noether 界），于是维数公式反过来控制生成元个数。

**最容易卡住的一步**：**母函数 $\sum_n\operatorname{tr}(\operatorname{Sym}^n g)t^n=\det(1-tg)^{-1}$ 这个恒等式**。它把"无限多个分次维数"压缩成一个行列式，缺了它 Molien 公式推不出来；很多人会试图对每个 $n$ 单独算迹，然后卡死在组合计数上。

### ALG-M09 SL2 的对称幂表示与 Clebsch–Gordan 分解

**数学内核.** $V_k=\operatorname{Sym}^kV$（$V=\mathbb C^2$）给出了 $SL_2$ 的全部不可约表示；张量积分解 $V_m\otimes V_n=\bigoplus_{i=0}^{n}V_{m+n-2i}$ 可以用一条**显式正合列** $0\to V_{m-1,n-1}\xrightarrow{\cdot(y-x)}V_{m,n}\xrightarrow{y=x}V_{m+n}\to0$ 来证明；三张量积的不变量空间维数则由 Clebsch–Gordan 与 $-\operatorname{id}$ 的作用决定。**这题在考"用具体正合列代替抽象最高权理论做 CG 分解"。**

**成员与差异**
- **10T6**（合并题面）：(a) 证 $\operatorname{Sym}^nV$ 不可约；(b) 问 $V_2\otimes V_3$ 中哪些 $V_n$ 出现。差别：最简版，只要两个具体结论。
- **13I4**：换成 $SL_2(\mathbb R)$ 作用于 $V_k=\mathbb R[x]_{\le k}$（$\gamma\cdot P(x)=(cx+d)^kP(\frac{ax+b}{cx+d})$）。(4.1) $V_k$ 不可约；(4.2) 证那条**正合列**并 split，从而得 $V_m\otimes V_n=\bigoplus_{i=0}^n V_{m+n-2i}$；(4.3) $(V_\ell\otimes V_m\otimes V_n)^{SL_2}$ 或 0 或 1 维，非零 $\iff \ell+m+n\equiv0\bmod2$ 且 $\ell+m\ge n$。差别：**从"算一个例子"升到"证一般分解公式 + 算三张量不变量"。**

**递进关系**：10T6（具体 $V_2\otimes V_3$，用"验算"）→ 13I4（给出正合列机制，一般 $m,n$，再算三张量不变量）。**典型升要求：从"报答案"到"给证明装置"。**

**标准解法骨架**
1. 把 $V_k$ 看成二元 $k$ 次型（或 $\mathbb R[x]_{\le k}$），$SL_2$ 经由 Möbius 变换作用。
2. $V_k$ 的单生成性：$x^k$ 在最高权意义下生成整个 $V_k$；用降算子在 $V_k$ 上的传递性证不可约。
3. 构造嵌入 $V_{m-1,n-1}\xrightarrow{\cdot(y-x)}V_{m,n}$：核恰好是零，因为 $V_{m,n}\subset\mathbb C[x,y]$ 且 $y-x$ 非零因子。
4. 构造 $V_{m,n}\xrightarrow{y=x}V_{m+n}$：令 $y=x$ 把二元型限制到对角线；核恰为 $(y-x)V_{m-1,n-1}$（用次数与整除性验证）。
5. 正合列 split（因为 $SL_2$ 的表示完全可约：用不变 Hermite 型或 Weyl 的 unitary trick）。
6. 归纳得 $V_m\otimes V_n=\bigoplus_{i=0}^n V_{m+n-2i}$。
7. 三张量不变量：用 (6) 把 $V_\ell\otimes V_m\otimes V_n$ 展成不可约之和，$V_0$ 出现的重数即为所求；$-\operatorname{id}\in SL_2(\mathbb R)$ 或 $\mathbb C^*$ 的作用给出奇偶条件，$\ell+m\ge n$ 给出偏序条件。

**最容易卡住的一步**：**第 4  step 用 $y=x$ 求核**——必须同时证明 $(y-x)V_{m-1,n-1}\subseteq\ker$ 与反向包含。反向包含要用"$f(x,x)=0\Rightarrow (y-x)\mid f$"这条整除性，很多解法在这里含糊过去，导致分解公式的**互不重复性**（各 $V_{m+n-2i}$ 互不同构）没被验证。

### ALG-M10 Fitting 引理与局部自同态环

**数学内核.** 对**有限长度/不可分解**的对象 $M$，自同态 $u$ 的核链 $\ker u\subseteq\ker u^2\subseteq\cdots$ 必然稳定；于是 $u$ 要么可逆、要么幂零（Fitting 引理），不可逆元构成双边理想，商环 $\operatorname{End}(M)/I$ 是除环。**"不可分解 $\iff$ 自同态环局部"**是本母题的中心命题。这是一个可以被搬到模、表示、交换群三个层面上的同一骨架。

**成员与差异**
- **16T4**：$G$ 是（不必有限的）群，$V$ 是特征 $\ne2$ 域上不可分解的有限维表示，$R=\operatorname{End}_F(V)^G$。(a) $R$ 中元素可逆或幂零；(b) 不可逆元构成双边理想，$R/I$ 是除代数；(c) 存在 $G$-不变非退化双线性型 $\Rightarrow V$ 正交或辛；(d) $F$ 代数闭时不能既正交又辛。差别：**表示论层面**，并且多了一条"不变双线性型的正交/辛二分"。
- **17I2**：$A$ 有限交换群，$\varphi$ 是自同态，$A_{nil}=\{x:\varphi^k(x)=0\}$。(a) 存在子群 $A_0$ 使 $\varphi|_{A_0}$ 是自同构且 $A=A_0\oplus A_{nil}$；(b) 这样的 $A_0$ 唯一。差别：**交换群层面**，换成"Fitting 分解"（可逆部分 $\oplus$ 幂零部分）并额外要求唯一性。
- **18T1**：$E$ 局部环（$u$ 与 $1-u$ 至少一个可逆），$M$ 是 $R$-模。(a) $\operatorname{End}_R(M)$ 局部 $\Rightarrow M$ 不可分解；(b) $M$ 不可分解且有限长度 $\Rightarrow$ Fitting 引理成立 $\Rightarrow \operatorname{End}_R(M)$ 局部。差别：**模论层面**，并把双向等价写全。

**递进关系**：16T4（表示论版，附带双线性型二分）→ 17I2（交换群版，加唯一性）→ 18T1（模论版，加双向等价）。**同一骨架的三次换皮，每次换一个范畴并补一条附加要求。**

**标准解法骨架**
1. 对 $M$ 有限长度（或有限维），核链 $\ker u\subseteq\ker u^2\subseteq\cdots$ 稳定，设稳定于 $n$：$\ker u^n=\ker u^{2n}$。
2. 由 $\ker u^n=\ker u^{2n}$ 得 $M=\ker u^n\oplus \operatorname{im}u^n$（Fitting 分解：$x=x-u^n y+u^n y$）。
3. 若 $M$ 不可分解，则 $M=\ker u^n$ 或 $M=\operatorname{im}u^n$，即 $u$ 幂零或可逆。
4. 证不可逆元集 $I$ 是双边理想：若 $u,v$ 不可逆则 $u+v$ 不可逆（若 $u+v$ 可逆则 $1=(u+v)^{-1}u+(u+v)^{-1}v$，两项都不可逆，而局部环中两个不可逆元之和不可逆——用局部环定义 $u$ 与 $1-u$ 至少一个可逆）。
5. $R/I$ 中每个非零元可逆 $\Rightarrow$ 除环。
6. 反方向（18T1(a)）：$\operatorname{End}(M)$ 局部 $\Rightarrow$ 任何投影 $e$ 满足 $e$ 与 $1-e$ 至少一个可逆 $\Rightarrow e=0$ 或 $1$ $\Rightarrow M$ 不可分解。
7. （16T4(c,d)）若有不退化不变双线性型 $B$，则 $B$ 对称或反对称（由 $B\pm B^t$ 是等变自同态且 $R/I$ 是除代数逼出其中一个为零）；代数闭时 $R/I=F$，两者不能并存。

**最容易卡住的一步**：**局部环定义用的是"$u$ 与 $1-u$ 至少一个可逆"，而不是"不可逆元构成理想"**。第 4 步要从前者推出后者，需要先证明"两个不可逆元之和不可逆"；这一步是整条推理的技术枢纽，也是 18T1 把局部环定义写进题面的原因。

### ALG-M11 p 进单位群：Teichmüller 提升、对数同构与幂判别

**数学内核.** $\mathbb Z_p^\times$ 有**乘法分解** $\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)$，其中 $\mu_{p-1}$ 由 Teichmüller 提升 $\omega(a)=\lim a^{p^n}$ 给出，$1+p\mathbb Z_p\cong p\mathbb Z_p$ 由 $p$ 进对数实现，$1+p\mathbb Z_p$ 内的 $p$ 次幂恰是 $1+p^2\mathbb Z_p$。**这题在考"把 $p$ 进单位群拆成有限单位根部分与 pro-$p$ 部分"。**

**成员与差异**
- **12T6**：$\mathbb Z_p=\varprojlim\mathbb Z/p^n\mathbb Z$。(1) $a^{p^n}\to\omega(a)$，$\omega(a)^{p-1}=1,\ \omega(a)\equiv a\bmod p$，且 $\omega$ 只依赖 $a\bmod p$；(2) $\log(1+px)=\sum(-1)^{n-1}p^nx^n/n$ 收敛并给出同构 $1+p\mathbb Z_p\to p\mathbb Z_p$，在稠密子群 $\log(1+p)\mathbb Z$ 上逆映射是 $x\mapsto(1+p)^x$；(3) 推出 $\mathbb Z_p^\times\cong\mathbb Z_p\times\mathbb Z/(p-1)\mathbb Z$。差别：**建造整条分解**。
- **20I5**：$p\ge3$。(a) $1+p\mathbb Z_p$ 中元素是 $p$ 次幂 $\iff$ 它在 $1+p^2\mathbb Z_p$ 中；(b) 存在 $a,b,c\in\mathbb Z_p^\times$ 使 $a^p+b^p=c^p$ $\iff \sum_{i=1}^{p-1}i^{p-2}t^i\equiv0\bmod p$ 对某个 $t$；特别 $p=7$ 取 $t=3$ 成立——**FLT 在 $\mathbb Z_7$ 中不成立**。差别：用 (a) 的**过滤结构**去做一个反例（局部 FLT 失效），是全新的应用面。
- **23I6**：$K$ 是 $p$ 进局部域，$O_K$ 有素元 $\pi$。(1) $\log:1+pO_K\to pO_K$ 是同构，并能唯一延拓为 $\log_\pi:K^\times\to K$ 且 $\log_\pi(\pi)=0$，求核；(2) 由此证 $K^\times/K^{\times,n}$ 是有限群。差别：**从 $\mathbb Z_p$ 抬到一般局部域 $O_K$**，并用来做"$K^{\times}$ 的 $n$ 次幂商有限"这一结构结论。

**递进关系（升级链）**
12T6（$\mathbb Z_p$ 上把 Teichmüller + 对数 + 分解全套建好）→ 20I5（用 $1+p^k$ 过滤做 $p$ 次幂判别，并给出 $\mathbb Z_7$ 中 FLT 反例）→ 23I6（把同一个对数搬到一般 $p$ 进局部域 $O_K$，并导出 $K^\times/K^{\times,n}$ 有限）。

**标准解法骨架**
1. 先证 $\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)$：用 $\mathbb F_p^\times$ 是 $p-1$ 阶循环群 + Hensel 提升（或直接 $a^{p^n}\to\omega(a)$）。
2. Teichmüller 提升：证 $a^{p^n}$ 是 Cauchy 列（$a^{p^{n+1}}-a^{p^n}=a^{p^n}(a^{p^n(p-1)}-1)$ 且 $v_p(a^{p^n(p-1)}-1)\ge n+1$），极限 $\omega(a)$ 满足 $\omega^{p-1}=1$。
3. 对数：在 $1+p\mathbb Z_p$ 上 $v_p(x^n/n)\ge n-v_p(n)\to\infty$，级数收敛；证 $\log(xy)=\log x+\log y$（在收敛范围内可交换极限）；逆由指数级数给出。
4. 同构 $1+p\mathbb Z_p\cong p\mathbb Z_p$ 转成加法群结构 $\cong\mathbb Z_p$。
5. $p$ 次幂判别：在 $1+p\mathbb Z_p$ 中 $p$ 次幂的像在 $\log$ 下是 $p\cdot p\mathbb Z_p=p^2\mathbb Z_p$，故对应 $1+p^2\mathbb Z_p$。
6. 一般 $O_K$：把 $\mathbb Z_p$ 换成 $O_K$，$p$ 换成 $\pi$，对数在 $1+\pi O_K$（或 $1+pO_K$）上同样收敛（用 $v(\pi^n/n)\to\infty$ 与分歧指数 $e$）。
7. $K^\times/K^{\times,n}$ 有限：由 $\log$ 把 $1+pO_K$ 同构到 $pO_K$（有限生成 $\mathbb Z_p$-模），商掉 $n$ 次幂后成为有限群；再处理 $\mu$ 与 $\pi^\mathbb Z$ 部分。

**最容易卡住的一步**：**第 2 步中 $v_p(a^{p^n(p-1)}-1)\ge n+1$ 的估计**。要用到 $v_p(x^{p-1}-1)\ge1$ 对 $x\equiv1$ 或 $x\in\mathbb Z_p^\times$ 的加强版（LTE 引理），才能让 Cauchy 性成立。很多人只证了"$a^{p^n}$ 模 $p$ 稳定"就以为完成了。

### ALG-M12 非阿基米德域的完备性与球完备性

**数学内核.** 完备 $\ne$ 球完备：$\mathbb Q_p$ 完备（Cauchy 列收敛）但不球完备（下降闭球列交可以空，只要球心序列不收敛）；代数扩张 $\mathbb Q_p(\mu_{p^n})$ 仍球完备，而 $\mathbb Q_p(\mu_{p^\infty})$ **不是**，它的完备化又**是**球完备——这是一个由"值群离散/稠密"决定的精细二分。另一半 $\mathbb Z$ 在 $\mathbb Z_p$ 中的稠密性与"连续延拓 $\iff$ 一致连续"（$\mathbb Z_p$ 上的函数论）是同一拓扑骨架。

**成员与差异**
- **20I6**：判断 $\mathbb Q_p$、$\mathbb Q_p(\mu_{p^n})$、$\mathbb Q_p(\mu_{p^\infty})$、其完备化是否球完备。差别：**四元对比**，题目给出"构造 $|a_1|>|a_2|>\cdots$ 且 $\lim|a_i|>0$、闭球交为空"的提示，考"球完备是比完备更强的条件"。
- **21I6**：$\bar{\mathbb Q}_p$ 上的 $g:\mathbb Z_{\ge0}\to\mathbb N$ 严格递增，$\zeta_i$ 取本原 $(p^{g(i)}-1)$ 次单位根。(a) $K_i=\mathbb Q_p(\zeta_i)$ 是不分叉扩张且次数 $g(i)$；(b) 给出使 $K_{i-1}\subset K_i$ 的显式 $g$，证明 $K_i=\mathbb Q_p(\alpha_i)$ 且 $(\alpha_i)$ 是 Cauchy 列；(c) $\eta$ 的模 $p^M$ 同余阻塞；(d) 取合适 $(N_i)$ 使 $(\alpha_i)$ 在 $\bar{\mathbb Q}_p$ 中不收敛，推出 $\bar{\mathbb Q}_p$ 关于 $p$ 进拓扑**不完备**。差别：**从"球完备性"抬到"$\bar{\mathbb Q}_p$ 不完备"**，并且需要在无限次不分叉扩张里造不收敛的 Cauchy 列。
- **24I5**：$\mathbb Z$ 在 $\mathbb Z_p$ 稠密；$f:\mathbb Z\to\mathbb Q_p$ 可连续延拓 $\iff$ 一致连续（即模 $p^N$ 同余控制）；$n\mapsto a^n$ 何时可延拓；能否延拓成 $a^x:\mathbb Q_p\to\mathbb Q_p$ 且 $a^{x+y}=a^xa^y$。差别：同一拓扑骨架的**函数论面**——把"完备性/连续性"换成"延拓与乘性同态"。

**递进关系**：20I6（$\mathbb Q_p$ 完备但非球完备，$\mathbb Q_p(\mu_{p^\infty})$ 更不球完备）→ 21I6（造出 $\bar{\mathbb Q}_p$ 中不收敛的 Cauchy 列，证明它不完备）→ 24I5（把拓扑换成"稠密子集上的连续延拓"，并追问乘性同态 $a^x$）。**同一条"非阿基米德拓扑"主线的三次不同切面。**

**标准解法骨架**
1. 球完备 $\Rightarrow$ 完备：任意 Cauchy 列可造出球心为该列项的下降闭球列。
2. 反方向找反例：在值群稠密（$|\mathbb Q_p^\times|$ 的闭包含 $\lim|a_i|>0$）的域上，取 $|a_1|>|a_2|>\cdots$ 且 $\lim|a_i|>0$，则球 $B_i=\{x:|x-a_1-\cdots-a_i|\le|a_i|\}$ 下降且交空。
3. $\mathbb Q_p$ 的值群离散，凡下降闭球列球心必收敛，故球完备；同理 $\mathbb Q_p(\mu_{p^n})$（有限扩张，值群仍离散）。
4. $\mathbb Q_p(\mu_{p^\infty})$ 的值群稠密，用第 2 步构造，故不球完备。
5. 完备化 $\widehat{\mathbb Q_p(\mu_{p^\infty})}$ 反而是**极大完备/球完备**的：其值群仍是 $p^\mathbb Q$（稠密），但完备化之后任何下降闭球列的"半径趋于 0 或模长为极限值"两种情形都能处理——直接把闭球列取极限元素。
6. （24I5）稠密性：$\mathbb Z$ 在 $\mathbb Z_p$ 中稠密由"$\mathbb Z\to\mathbb Z/p^N$ 满射"；一致连续 $\Rightarrow$ 延拓：用 $\mathbb Z$ 中的 Cauchy 列逼近；$a^n$ 一致连续 $\iff v_p(a-1)>0$（或 $a$ 是 1 的 $p$ 进邻域中的元素）；$a^x$ 存在 $\iff a\in1+p\mathbb Z_p$ 且用 $\log/\exp$ 定义。

**最容易卡住的一步**：**把"完备"与"球完备"分开**。很多人第一反应是"完备的域都球完备"，于是把 (a)(b)(c)(d) 全答"是"。真正的分界是**值群是否离散**：值群离散 $\Rightarrow$ 球完备；值群稠密且域不完备 $\Rightarrow$ 不球完备。

### ALG-M13 局部域扩张：不分叉扩张与半线性 Galois 下降

**数学内核.** 局部域的不分叉扩张 $E/F$ 满足**最简单的 Galois 下降**：$O_E\otimes_{O_F}O_E\cong\prod_{\gamma\in\Gamma}O_E$（因为 $O_E/O_F$ 是有限 étale 且剩余域扩张可分），从而"带半线性 $\Gamma$-作用的 $O_E$-模"范畴 $\equiv$ "$O_F$-模"范畴，等价函子就是 $M\mapsto O_E\otimes_{O_F}M$。分歧扩张时该函子失效。另一半是**完全不分歧扩张的分类**：$[K:\mathbb Q_p]=d$ 的扩张只有有限多个，$(d,p)=1$ 时完全分歧的 Galois 扩张必循环且个数可数。**这题在考"用不分叉 $\Rightarrow$ étale $\Rightarrow$ 下降"这条链。**

**成员与差异**
- **25I4**：$E/F$ 有限 Galois 局部域扩张，$\Gamma=\operatorname{Gal}$。(1) $E/F$ 不分叉时 $\alpha:O_E\otimes_{O_F}O_E\to\prod_{\gamma\in\Gamma}O_E,\ c\otimes x\mapsto(c\gamma(x))_\gamma$ 是同构；(2) 半线性作用模 $M$ 的不变量映射 $\iota_M:O_E\otimes_{O_F}M^\Gamma\to M$ 是同构；(3) 函子 $\Phi_{E/F}:\operatorname{Mod}_{O_F}\to\operatorname{Mod}^\Gamma_{O_E}$ 是范畴等价；(4) 分歧时是否仍等价。差别：**整套下降理论**，最后一问用反例收尾。
- **26I5**：$K/\mathbb Q_p$ 有限。(1) 固定 $d$，$K$ 的 $d$ 次扩张只有有限多个同构类；(2) $(d,p)=1$ 时，若 $L/K$ 是完全分歧的 $d$ 次 Galois 扩张，则 $K$ 含本原 $d$ 次单位根且 $L/K$ 循环；(3) $(d,p)=1$ 时算出这种扩张的同构类数目。差别：**从"不分叉下降"换到"完全分歧扩张的分类与计数"**，用的是 Kummer 理论（因为 $(d,p)=1$ 且 $\mu_d\subset K$）。

**递进关系**：25I4（不分叉情形的下降等价 + 分歧失败）→ 26I5（分歧情形的分类与计数，用 Kummer 补上另一块拼图）。**两者合起来是"局部域 Galois 扩张的两个极端"**（不分叉 vs 完全分歧），2025→2026 连续两年出现。

**标准解法骨架**
1. 不分叉：$O_E/O_F$ 是有限 étale 代数，$\operatorname{Frac}$ 与剩余域都对应；$O_E\otimes_{O_F}O_E$ 是 $\Gamma$-Galois 代数（因为 $E/F$ 是 Galois 且 $O_E/O_F$ 是 Galois 覆盖的整模型）。
2. 用**迹配对**：$O_E\otimes_{O_F}O_E\to O_E,\ a\otimes b\mapsto ab$ 与 $\Gamma$-作用配合，证 $\alpha$ 是单射（无幂零元，因为不分叉）；比较 $O_F$-秩（两边都是 $|\Gamma|\dim$）得同构。
3. 下降到模：$\iota_M$ 的单射性由"$\alpha$ 是同构 $\Rightarrow$ 取不变量后仍满"；满射性用 $m$ 的 $\Gamma$-轨道生成 $O_E\otimes M^\Gamma$。
4. 范畴等价：构造逆函子 $M\mapsto M^\Gamma$，验证两个复合都自然同构于恒等（用第 3 步）。
5. 分歧时失效：取 $E/F$ 完全分歧，$O_E\otimes_{O_F}O_E$ 不再是 $\Gamma$-Galois 代数（有幂零元/非 étale），$M=O_E$ 时 $\iota_M$ 不满。
6. （26I5）完全分歧 Galois：$(d,p)=1$ $\Rightarrow$ 分歧指数 $e=d$ 且 $L/K$ 由 Kummer 给出（若 $\mu_d\subset K$）；由 $L=K(\sqrt[d]{a})$ 与 Galois 性推出 $\mu_d\subset K$ 且群循环。
7. 计数：$K^\times/K^{\times,d}$ 中每个元素对应一个 $d$ 次 Kummer 扩张，去掉非完全分歧的部分，得指数为 $d$ 的元素个数。

**最容易卡住的一步**：**第 2 步用"不分叉 $\Rightarrow$ 迹配对非退化"**。分歧扩张里迹形会退化（$\operatorname{Tr}$ 可能落在 $\pi$ 的倍数上），这正是 (4) 失败的原因。多数人做 (1) 时会直接说"因为 $E\otimes_F E\cong\prod E$，张量 $O$ 就好"，忽略了必须验证无幂零元。

### ALG-M14 可除群与 $\mathbb Z_p$：自同态环与连续表示

**数学内核.** Prüfer 群 $\mathbb Q_p/\mathbb Z_p$ 与 $\mathbb Q/\mathbb Z$ 是可除群，其自同态环分别是 $\mathbb Z_p$ 与 $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$；Pontryagin 对偶把"$\mathbb Z_p$ 的连续复表示"翻译成"$\mathbb Z_p$-模上的结构问题"，而有限维连续复表示全靠**单位根刚性**（$a^{p^r}\to1\Rightarrow a$ 是单位根）来分类。**这题在考"profinite 群 / 可除群的自同态与表示"。**

**成员与差异**
- **17I1**：$\mathbb Q_p,\mathbb Z_p$。(a) $(p^{-k}\mathbb Z_p)/\mathbb Z_p\cong\mathbb Z/p^k\mathbb Z$；(b) 求该群的自同态环；(c) 求 $\operatorname{End}(\mathbb Q_p/\mathbb Z_p)$；(d) 求 $\operatorname{End}(\mathbb Q/\mathbb Z)$。差别：**纯代数**，用"自同态由生成元的像决定 + 可除性/挠性限制"算出 $\mathbb Z_p$ 与 $\prod\mathbb Z_p$。
- **23I5**：(1) $a\in\mathbb C$ 且 $a^{p^r}\to1$ $\Rightarrow a$ 是某个 $p^m$ 次单位根；(2) $A\in M_n(\mathbb C)$ 且 $A^{p^r}\to I_n$ $\Rightarrow A^{p^m}=I_n$；(3) 确定 $\mathbb Z_p$ 的所有有限维连续复表示。差别：**从"自同态环"换到"连续表示"**，用 (1)(2) 的刚性把表示限制在有限商 $\mathbb Z/p^m$ 上，再用 $\mathbb Z/p^m$ 的不可约复表示全是特征标分类。

**递进关系**：17I1（算出 $\operatorname{End}(\mathbb Q_p/\mathbb Z_p)=\mathbb Z_p$、$\operatorname{End}(\mathbb Q/\mathbb Z)=\widehat{\mathbb Z}$）→ 23I5（用单位根刚性把 $\mathbb Z_p$ 的有限维连续复表示全部分类）。**注意这两题有 Pontryagin 对偶的血缘：$\mathbb Z_p=\operatorname{End}(\mathbb Q_p/\mathbb Z_p)=\widehat{\mathbb Q_p/\mathbb Z_p}$。**

**标准解法骨架**
1. $\mathbb Q_p/\mathbb Z_p$ 的 $p^k$-挠部分：$p^{-k}\mathbb Z_p/\mathbb Z_p$ 是 $p^k$ 阶循环群（用 $\mathbb Z_p$ 是 DVR 且 $\mathbb Z_p/p^k$ 的挠结构）。
2. 自同态 $f$ 由 $f(1/p^k)$ 决定，$f$ 与所有 $\mathbb Z$-作用交换且保持挠性；把 $f$ 在每个 $p^k$-挠层上的作用写成乘 $a_k\in\mathbb Z/p^k$。
3. 相容性 $a_{k+1}\equiv a_k\bmod p^k$ 给出 $a\in\varprojlim\mathbb Z/p^k=\mathbb Z_p$，故 $\operatorname{End}=\mathbb Z_p$。
4. $\mathbb Q/\mathbb Z=\bigoplus_p\mathbb Q_p/\mathbb Z_p$（挠分解），$\operatorname{End}=\prod_p\operatorname{End}(\mathbb Q_p/\mathbb Z_p)=\prod_p\mathbb Z_p$。
5. (23I5) 单位根刚性：$|a^{p^r}-1|\to0$ 且 $a\ne0$；若 $a$ 不是单位根，取 $a$ 的无穷多条不同幂次，$a^{p^r}$ 会有无穷多个不同的模长/极角取值，与收敛矛盾；若 $a$ 是单位根，则 $a^{p^r}$ 只能取有限多个值且需最终为 1。
6. 矩阵版：把 $A$ 化成 Jordan 形，$A^{p^r}\to I$ 逼出 $A$ 可对角化且特征值是单位根，再用 (1)。
7. $\mathbb Z_p$ 的连续复表示 $\rho$：由连续性，$\rho^{-1}(\{1\})$ 是开子群 $\supseteq p^m\mathbb Z_p$，故 $\rho$ 过 $\mathbb Z/p^m$；$\mathbb Z/p^m$ 的不可约复表示由 (1)(2) 全是特征标；一般有限维表示完全可约（有限群 + 特征 0）⇒ 直和。

**最容易卡住的一步**：**第 5 步的"$a^{p^r}\to1$ 推出 $a$ 是单位根"**。注意这是关于复数的命题（不是 $p$ 进！），必须用 $|a|$ 与幅角两条信息：$|a|^{p^r}\to1$ 逼出 $|a|=1$，再在单位圆上论证 $a^{p^r}\to1$ 只能发生在 $a$ 是有限阶元时。很多人只看到 $p$ 进类似物（Teichmüller），把题目当成 $p$ 进问题做，方向就错了。

### ALG-M15 Chevalley–Warning 定理

**数学内核.** 有限域上方程组的解数可以被"次数和"控制：若 $\sum \deg f_i<n$，则 $\sum_{x\in\mathbb F_q^n}\prod_i(1-f_i(x)^{q-1})=0$，而左边恰好数出解数模 $p$ ⇒ 解数被 $p$ 整除 ⇒ 既然 $(0,\dots,0)$ 是解，就必有**非零解**。核心工具是 $\sum_{x\in\mathbb F_q}x^a=0$（$0\le a<q-1$）。

**成员与差异**
- **14I5**：$f_i\in F[X_1,\dots,X_n]$，$\deg f_i=d_i$，$f_i(0)=0$，若 $n>\sum d_i$ 则方程组有非零解。差别：**直接使用**定理，题面已经给出 $\sum_X\prod_i(1-f_i(X)^{q-1})$ 这个提示式。
- **17I4**：把定理**当作目标**：(a) 先证 $S(X^a)=\sum_{x\in\mathbb F_q}x^a=0$（$0\le a<q-1$，约定 $x^0=1$）；(b) 再证 $S(P)=0$ 并推出 $p\mid|V|$。差别：把底层引理与证明步骤全都摊开来考。

**递进关系**：14I5（给提示、用定理）→ 17I4（拆成 (a)(b) 两步、证明定理）。**典型的"同一结论，从应用升到证明"。**

**标准解法骨架**
1. 证 $\sum_{x\in\mathbb F_q}x^a=0$（$0\le a<q-1$）：$a=0$ 时和为 $q\equiv0$；$a>0$ 时取生成元 $g$，和为等比级数 $\sum g^{aj}=0$。
2. 把"$f_i(x)=0$"编码成 $1-f_i(x)^{q-1}$（在 $\mathbb F_q$ 中当且仅当 $f_i(x)=0$ 时为 1，否则为 0——Fermat 小定理）。
3. 于是 $N=\#\{x: f_i(x)=0\ \forall i\}$ 满足 $N\equiv S(\prod_i(1-f_i^{q-1}))\pmod p$。
4. 展开 $\prod_i(1-f_i^{q-1})$，每一项的 $X$-次数 $\le\sum_i d_i(q-1)<n(q-1)$。
5. 由于每一项的次数严格小于 $n(q-1)$，必存在某个变量的指数 $<q-1$，对该变量用第 1 步逐层求和 ⇒ $S(P)=0$。
6. 于是 $p\mid N$；因为 $0$ 是解，$N\ge1$ ⇒ $N\ge p$ ⇒ 存在非零解。

**最容易卡住的一步**：**第 5 步"必存在某个变量的指数小于 $q-1$"**。单变量次数 $\le n(q-1)$ 不等于每个变量都逼近 $q-1$；必须用"总次数 $<$ 变量个数 $\times(q-1)$"来保证至少有一个变量掉队，才能对该变量单独求和得 0。这一步是整题的组合核心。

### ALG-M16 有限域上不可约多项式的计数与参数化

**数学内核.** 有限域上首一不可约多项式的个数由 Möbius 反演给出：$N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}$；更强的是**结构**：$\mathbb F_{q^n}$ 的 Frobenius 轨道把不可约多项式与 $\mathbb F_{q^n}$ 中的元素一一对应，于是"数个数"升级为"用 Frobenius 给所有不可约多项式参数化"。本题的具体形态是：用 $\mathbb F_5$ 的元素排列构造一个 $\mathbb F_5$-参数族，使其恰好覆盖全部 40 个首一不可约三次多项式。

**成员与差异**
- **13I3**：$t=(t_0,\dots,t_5)\in\mathbb F_5^6$，$t_0\ne0$，$\{t_i,i>0\}$ 是 $\mathbb F_5$ 的一个排列，$P_t(x)=(x-t_1)(x-t_2)(x-t_3)+t_0(x-t_4)(x-t_5)$。(1) $P_t$ 在 $\mathbb F_5[x]$ 中不可约；(2) $t,t'$ 给同一多项式 $\iff t_0=t_0'$ 且 $\{t_4,t_5\}=\{t_4',t_5'\}$；(3) 每个首一不可约三次多项式都能这样得到。差别：**完整的参数化 + 唯一性 + 满射性**。
- **13T5**：$\mathbb F_2$ 上次数 2、3 的所有不可约多项式；次数 6 的不可约多项式个数。差别：**纯计数**，用 $\mathbb F_{2^n}$ 的元素个数与 Frobenius 轨道数（答案：次数 6 有 9 个）。

**递进关系**：13T5（先会用 $N_q(n)=\frac1n\sum\mu(d)q^{n/d}$ 数个数）→ 13I3（要求把每个不可约三次多项式**具体构造出来**并证明参数化是双射）。**同年、同一卷别体系内的升要求：从"数"到"造"。**

**标准解法骨架**
1. $N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}$：把 $\mathbb F_{q^n}$ 中元素按 Frobenius $x\mapsto x^q$ 的轨道（大小 $=$ 该元素的次数）分类，两边数元素个数再 Möbius 反演。
2. $q=2$：$N_2(2)=\frac12(2^2-2)=1$（$x^2+x+1$）；$N_2(3)=\frac13(2^3-2)=2$（$x^3+x+1,\ x^3+x^2+1$）；$N_2(6)=\frac16(2^6-2^3-2^2+2)=9$。
3. $q=5,n=3$：$N_5(3)=\frac13(5^3-5)=40$。
4. （13I3）先证 $P_t$ 在 $\mathbb F_5$ 中无根：对 $x\in\{t_4,t_5\}$ 有 $P_t(x)=(x-t_1)(x-t_2)(x-t_3)\ne0$（三个非零因子之积），对 $x\in\{t_1,t_2,t_3\}$ 有 $P_t(x)=t_0(x-t_4)(x-t_5)\ne0$；三次无根 ⇒ 不可约。
5. （13I3）唯一性：由 $P_t$ 反解——给定 $P$，$P-Q$ 必须是一个二次式的非零倍数，其中 $Q=\prod_{i\le3}(x-t_i)$；比较首项与二次项系数即可确定 $t_0$ 与 $\{t_4,t_5\}$。
6. （13I3）满射：参数空间 $(t_0,\{t_4,t_5\})$ 有 $4\times\binom52=40$ 个点，与 $N_5(3)=40$ 相等；又由第 5 步映射是单射，故必为双射。
7. 计数与构造汇合，完成证明。

**最容易卡住的一步**：**第 6 步的"用计数 + 单射逼出满射"**。若直接去证"任给不可约三次式都能写成 $Q+t_0R$"，需要处理 $\mathbb F_5$ 的五元素划分组合，非常繁琐；聪明的解法是数两边点数（$4\cdot10=40=N_5(3)$）再配合单射性。看到 $t_0\ne0$ 与"$\{t_i\}$ 是排列"这两个条件就该想到"这是在数点数"。

### ALG-M17 Artin–Schreier 扩张与 Hilbert 90

**数学内核.** 特征 $p$ 的循环扩张 $E/F$ 必然由方程 $y^p-y=x$ 给出（Artin–Schreier），其可解性由**加性 Hilbert 90** 控制：$x=\sigma(y)-y$ $\iff \operatorname{tr}_{E/F}(x)=0$。这把"域扩张的循环性"翻译成"迹映射的满射性 + 一个多项式方程"，是特征 $p$ 上唯一可用的 Kummer 替代品。

**成员与差异**
- **17T4**：$K=\mathbb F_p(T)$，$f(X)=X^p-TX-T$，$g(X)=X^{p-1}-T$。(a) $f,g$ 在 $K$ 上不可约且可分；(b) $M$ 是 $g$ 的分裂域，$\operatorname{Gal}(M/K)\cong\mathbb F_p^\times$；(c) $L$ 是 $f$ 的分裂域，证 $g$ 在 $L$ 中分裂且 $\operatorname{Gal}(L/K)\cong\mathbb F_p\rtimes\mathbb F_p^\times$（$\mathbb F_p^\times$ 以伸缩作用）。差别：**函数域版**，多项式是"混合型"（既有 $X^p$ 又有 $T$ 系数），需要变量替换 $X=sZ$（$s^{p-1}=T$）把它化成标准 AS 形式。
- **19T5**：(1) $E/F$ 有限 Galois 且 $\operatorname{Gal}(E/F)=\langle\sigma\rangle$，$x\in E$ 且 $\operatorname{tr}_{E/F}(x)=0$ $\Rightarrow \exists y:x=\sigma(y)-y$；(2) $\operatorname{char}F=p$，$E/F$ 是 $p$ 次 Galois 扩张 $\Rightarrow \exists x\in F$ 使 $E\cong F[T]/(T^p-T-x)$。差别：**一般域版**，把 AS 理论的两根支柱（Hilbert 90 + AS 生成）拆开考。
- **21I1**：$p$ 素数，$a\in\mathbb F_p^\times$，证 $x^p-x-a$ 在 $\mathbb F_p$ 上不可约且可分。差别：**有限域上的最简实例**，用"若 $\alpha$ 是根，则 $\alpha+i$（$i\in\mathbb F_p$）也是根"这一平移对称性。

**递进关系**：21I1（最简：有限域上 $x^p-x-a$ 不可约，用平移对称）→ 19T5（一般域：Hilbert 90 + AS 生成定理，两个方向）→ 17T4（函数域：混合型多项式，用 $g$ 的根做变量替换，再把 Galois 群算成 $\mathbb F_p\rtimes\mathbb F_p^\times$）。**注意年份顺序与逻辑顺序相反（2021 最简、2017 最难），说明命题人在这条线上并不追求单调升级。**

**标准解法骨架**
1. （21I1）设 $\alpha$ 是 $x^p-x-a$ 的根，则 $\alpha+i$（$i\in\mathbb F_p$）给出全部 $p$ 个根；若 $\alpha\in\mathbb F_p$ 则 $\alpha^p-\alpha-a=-a\ne0$，矛盾 ⇒ 无有理根 ⇒ 次数 $p$ 且无低次因子 ⇒ 不可约；导数 $=-1$ ⇒ 可分。
2. （19T5(1)）取 $z\in E$ 使 $\operatorname{tr}(z)\ne0$，令 $y=\frac1{\operatorname{tr}(z)}\sum_{i=0}^{p-1}\big(\sum_{j=i+1}^{p-1}\sigma^j(x)\big)\sigma^i(z)$ 型拉格朗日插值元素，直接验证 $\sigma(y)-y=x$。
3. （19T5(2)）$E/F$ 是 $p$ 次循环，取 $\theta\in E\setminus F$，则 $\theta^p-\theta\in F$（因为 $\sigma(\theta^p-\theta)=\theta^p-\theta$）；令 $x=\theta^p-\theta$，则 $E\cong F[T]/(T^p-T-x)$。
4. （17T4）(a) 用 Capelli 型判据：$X^{p-1}-T$ 在 $\mathbb F_p(T)$ 上不可约（$T$ 不是 $p-1$ 次幂）；$X^p-TX-T$ 用 Eisenstein 型/赋值论证（在 $T=0$ 处的赋值）。
5. （17T4）(b) $g$ 的根是 $T^{1/(p-1)}$ 与 $\zeta T^{1/(p-1)}$，$\zeta\in\mu_{p-1}\subset\mathbb F_p\subset K$ ⇒ $M=K(T^{1/(p-1)})$，$\operatorname{Gal}(M/K)=\mathbb F_p^\times$。
6. （17T4）(c) 代入 $X=sZ$（$s^{p-1}=T$）化 $f$ 为 $Z^p-Z=1/s$，故 $L=M(Z)$ 且 $[L:M]=p$（$1/s$ 不是 $M$ 中元素的 $p$ 次幂减自身）；于是 $[L:K]=p(p-1)$，且 $T^{1/(p-1)}\in L$ ⇒ $g$ 在 $L$ 中分裂；最后确定群结构：$\operatorname{Gal}(L/K)$ 是 $\mathbb F_p$ 被 $\mathbb F_p^\times$ 的扩张，且作用就是伸缩 ⇒ $\mathbb F_p\rtimes\mathbb F_p^\times$。
7. 若需要唯一性：$H^1(G,\mathbb F_p)$ 的显式计算。

**最容易卡住的一步**：**第 6 步的变量替换 $X=sZ$**。看出 $X^p-TX-T$ 在代入 $s^{p-1}=T$ 后化为纯 Artin–Schreier 形式 $Z^p-Z=1/s$，是本题的关键；看不出这一点就只能在原多项式上硬算 Galois 群。

### ALG-M18 用代数数论（范形式、类数）求丢番图方程的整数解

**数学内核.** 把方程左边写成**范形式** $N(x+\alpha y+\cdots)$ 或"三线性型"，则"求整数解"就变成"在整数环/序中分解整数 $1$ 或某个小整数"；再用类数有限、单位群有限（或无限但有对数坐标）判定解的有限性与具体值。**这题在考"用理想分解与单位把丢番图方程降为有限搜索"。**

**成员与差异**
- **14T6**：$c\ne0$ 整数，$f(x,y,z)=x^3+cy^3+c^2z^3-3cxyz$。(a) 在 $\mathbb C$ 上分解 $f$（设 $c=\theta^3$）：$f=(x+\theta y+\theta^2z)(x+\omega\theta y+\omega^2\theta^2z)(x+\omega^2\theta y+\omega\theta^2z)$；(b) 当 $c$ 是整数的立方时 $f=1$ 只有有限多组整数解；(c) 当 $c$ 不是整数立方时 $f=1$ 有无穷多组整数解。差别：**解的有限性随 $c$ 的算术性质二分**，答案在"单位群秩 0/正"之间跳变。
- **21I5**：$x^2+13=y^3$ 的全部整数解（提示：$\mathbb Q(\sqrt{-13})$ 类数为 2）。差别：**具体方程 + 给出类数提示**，用 $\mathbb Z[\sqrt{-13}]$（非 UFD）中理想分解 + 类群阶 2 来恢复唯一分解，答案 $(x,y)=(\pm70,17)$。

**递进关系**：14T6（范形式 + $c$ 是否为立方决定有限/无限，属"定性二分"）→ 21I5（具体数值方程，用类数 $2$ 恢复唯一分解，属"定量求解"）。**同一骨架的"定性→定量"升级。**

**标准解法骨架**
1. 把方程整理成范形式：$x^3+cy^3+c^2z^3-3cxyz=(x+\theta y+\theta^2z)(x+\omega\theta y+\omega^2\theta^2z)(x+\omega^2\theta y+\omega\theta^2z)$（$\theta^3=c$）。
2. 当 $c=\theta^3$（$\theta\in\mathbb Z$）时三个因子都是 $\mathbb Z[\theta,\omega]$ 中的代数整数，$f=1$ $\Rightarrow$ 每个因子是单位；用 Dirichlet 单位定理/范数界证明只有有限多个单位三元组。
3. 当 $c$ 不是立方时，$1$ 不再是范形式的最简目标，改用一次因子的乘积等于某有理整数，并构造 Pell 型递推（利用 $x\mapsto x\cdot u$ 的乘法作用）产生无穷多解。
4. （21I5）在 $K=\mathbb Q(\sqrt{-13})$，$O_K$ 的类数为 2。令 $y$ 为奇数、$x$ 为偶数的情形逐层剥离，将 $y^3=(x+\sqrt{-13})(x-\sqrt{-13})$ 写成理想等式 $(x+\sqrt{-13})=(\mathfrak a)^3$。
5. 用类群阶 2 把 $\mathfrak a^3$ 的主性归约到 $\mathfrak a$ 的主性（$\mathfrak a^3$ 主 $\Rightarrow \mathfrak a$ 主，因为类群中元素的阶整除 3 与 2 ⇒ 阶为 1）。
6. 于是 $x+\sqrt{-13}=(a+b\frac{1+\sqrt{-13}}{2})^3$，展开比较系数，解出 $a,b$，得 $(x,y)=(\pm70,17)$。
7. 处理小素数/奇偶例外（$y$ 偶、$13\mid x$ 等情形逐个排除）。

**最容易卡住的一步**：**第 5 步"从 $\mathfrak a^3$ 主推出 $\mathfrak a$ 主"**。这要求同时知道"类群阶为 2"与"$\mathfrak a^3$ 主"，两者共同forced $[\mathfrak a]=1$（因为在阶 2 的群里 $3[\mathfrak a]=0\Rightarrow[\mathfrak a]=0$）。只用"类数 2"而不做这一步归约，就会停在"$\mathfrak a^3$ 是主理想"上无法继续。

### ALG-M19 局部-整体原则的失效

**数学内核.** "在每个 $\mathbb Z/p^n$（或每个 $\mathbb Q_p$）中可解"**推不出**"在 $\mathbb Z$ 中可解"。两个经典失效机制是：(i) 二次型/二次域中的障碍只是"局部符号"之和，用二次互反律可造出全局部可解而整体不可解的方程；(ii) 多项式"模每个 $p$ 有根"与"有有理根"之间的缺口，由 Galois 群的**不动点自由元素**（Chebotarev 密度）来度量。

**成员与差异**
- **14I3**：$X^2-82Y^2=\pm2$。(a) 若 $(x,y)$ 是解则 $(9x-82y,\ x-9y)$ 是对 $\mp2$ 的解（用 $9^2-82=-1$ 这个范数为 $-1$ 的单位）；(b) 对任意 $n$ 与奇素数 $p$，方程在 $\mathbb Z/p^n\mathbb Z$ 中有解（Hensel）；(c) 在 $\mathbb Z$ 中无解。差别：**二次型/单位版**，用 $\mathbb Z[\sqrt{82}]$ 的基本单位做下降。
- **13I5**：(5.1) 找一个整系数多项式 $f$，对每个素数 $p$ 在 $\mathbb F_p$ 上有根，但在 $\mathbb Q$ 上无根（答：$f=(x^2-2)(x^2-3)$——因为对任意奇素数 $p$，$(2/p)=1$ 或 $(3/p)=1$，否则 $(6/p)=(2/p)(3/p)=1$，故三者必有其一根；$p=2,3$ 单独验证）；(5.2) 能否取 $f$ 不可约（**不能**）；(5.3) $f$ 的最小可能次数（**4**）。差别：**多项式版**，是一条更漂亮的"用 Chebotarev + 不动点计数"的定理。

**递进关系**：14I3（具体方程，用手算单位与 Hensel 造局部解）→ 13I5（把现象升级为定理：不可约时不可能，最小次数 4）。**注意年份倒挂（2013 的题在逻辑上更"一般"）**。

**标准解法骨架**
1. （14I3(a)）注意 $9^2-82=(-1)$，即 $9+\sqrt{82}$ 是范 $-1$ 的单位：$(x+y\sqrt{82})(9+\sqrt{82})=(9x+82y)+(x+9y)\sqrt{82}$；对 $X^2-82Y^2$ 用共轭 $(9-\sqrt{82})$ 得到 $(9x-82y)^2-82(x-9y)^2=-(x^2-82y^2)$。
2. （14I3(b)）在 $\mathbb Q_p$ 上先找解（$82$ 是二次剩余或方程 $X^2-82Y^2=\pm2$ 在 $\mathbb Q_p$ 中有解，用 Hilbert 符号），再用 Hensel 提升到 $\mathbb Z/p^n$。
3. （14I3(c)）在 $\mathbb Z$ 中设 $x^2-82y^2=\pm2$；模 $82$（或模 $41$、模 $2$）取二次特征：$x^2\equiv\pm2\pmod{41}$，用 $(\pm2/41)$ 的符号冲突（$-1$ 的二次特征）推出矛盾。
4. （13I5(5.1)）构造 $f=(x^2-2)(x^2-3)$，对每个 $p$ 用 Legendre 符号二分：$p=2,3$ 直接验证，$p\ne2,3$ 时 $(2/p),(3/p)$ 之一为 1，否则二者皆 $-1$ 从而 $(6/p)=1$。
5. （13I5(5.3)）次数下界：$\deg f\le3$ 且模每个 $p$ 有根 ⇒ 每个不可约因子次数 $\le3$，用 Chebotarev 断言"每个素数都有根"要求 Galois 群每个元素都有不动点；但 $f$ 若不可约则 Galois 群在根集上**传递**，而传递群必有不动点自由的元素（因为 $\frac1{|G|}\sum_g|\mathrm{Fix}(g)|=$ 轨道数 $=1$，若所有 $|\mathrm{Fix}(g)|\ge1$ 又 $|\mathrm{Fix}(e)|=\deg f>1$ 则平均 $>1$，矛盾）⇒ 正密度个素数上无根 ⇒ 与假设矛盾。
6. （13I5(5.2)）由上一步立即得"不可约的 $f$ 不存在"。
7. 最小次数 4 的达成由第 4 步的例子给出。

**最容易卡住的一步**：**第 5 步"传递群必有不动点自由的元素"**——用 Burnside 引理"平均不动点数 $=$ 轨道数 $=1$"一句话解决，但绝大多数人会绕过它去尝试构造反例或引用 Grunwald–Wang。看到"传递 + 每个元素都有不动点"就该立刻用平均不动点数把 $|\mathrm{Fix}(e)|=\deg f$ 代进去。

### ALG-M20 数域整数环中理想与元素的生成与互素

**数学内核.** $O_K$ 是 Dedekind 域：理想唯一分解成素理想，类群有限，每个理想可以由 2 个元素生成，且"两个元素互素"（$(a,b)=O_K$）等价于"存在 $u$ 使 $au+b$ 是单位"。**这题在考"用素理想分解与类群有限性把元素层面的问题翻译成理想层面的有限组合"。**

**成员与差异**
- **22I4**：$A=O_K$，$\mathfrak a\ne0$ 理想，$a\in\mathfrak a$ 非零，证存在 $b\in\mathfrak a$ 使 $a,b$ 生成 $\mathfrak a$（即每个理想 2-生成）。差别：**理想层面的生成元数目**。
- **26I3**：$K$ 数域，$O_{\bar K}$ 是 $\bar K$ 中的代数整数环，$a,b\in O_{\bar K}$，证 $(a,b)=O_K$ $\iff$ $\exists u$ 使 $au+b\in O_K^\times$。差别：**元素层面的互素判据**，且允许 $a,b$ 取自 $\bar K$ 的代数整数环。

**递进关系**：22I4（理想由 2 个元素生成）→ 26I3（"生成整个环"的判据升级为"能凑出单位"）。**同一骨架的两次使用：一次数生成元，一次造单位。**

**标准解法骨架**
1. 把 $\mathfrak a$ 分解为 $\prod\mathfrak p_i^{e_i}$；对每个 $\mathfrak p_i$，$\mathfrak a/\mathfrak p_i\mathfrak a$ 是 $O_K/\mathfrak p_i$ 上的向量空间。
2. 把 $a$ 在每个局部块中的"赋值" $v_{\mathfrak p_i}(a)=f_i\le e_i$ 记下来；取 $b$ 使 $v_{\mathfrak p_i}(b)=0$（当 $f_i>0$）或 $v_{\mathfrak p_i}(b)=e_i$（当 $f_i=0$）。
3. 用中国剩余定理（或对每个 $\mathfrak p_i$ 单独构造后拼接）造出这样的 $b\in\mathfrak a$。
4. 验证 $(a,b)=\mathfrak a$：逐素理想比较赋值。
5. （26I3）$\Rightarrow$：$(a,b)=O_K$ ⇒ 存在 $u,v$ 使 $au+bv=1$；取 $u$ 即可（$b\in O_K$，故 $au+b = 1 + b - bv = 1+b(1-v)$ 不直接是单位，需要用"$au+b\equiv au \bmod b$ 与 $a$ 互素于 $b$"的等价刻画，或直接用 $au+bv=1$ 中令 $u'=u$、$b'=b$ 并调整）。
6. （26I3）$\Leftarrow$：若 $au+b\in O_K^\times$，则它模任何素理想都不为 $0$，从而 $(a,b)$ 不含任何素理想 ⇒ $(a,b)=O_K$。
7. 对 $a,b\in O_{\bar K}$ 的情形，把论证搬到每个有限生成子域上（$a,b$ 只涉及有限多个共轭，落在某个数域中）。

**最容易卡住的一步**：**第 2–3 步"逐素理想指派赋值再把 $b$ 拼起来"**。关键观察是：$a$ 在某素理想处赋值已经等于 $e_i$ 时，$b$ 在该处随便取；赋值小于 $e_i$ 时，$b$ 必须取到赋值 0（即 $b$ 不在该素理想中）。CRT 拼接时要注意 $b\in\mathfrak a$（即在 $f_i=0$ 处赋值 $\ge e_i$）。

### ALG-M21 曲线坐标环与函数域的整闭包（正规化）

**数学内核.** 奇点在代数上的表现是坐标环**不整闭**；正规化就是取分数域中的整闭包。对尖点三次曲线 $y^2=x^3+x^2$（或 $x^2=y^3$），参数化 $x=t^2-1,\ y=t(t^2-1)$ 给出正规化 $F[t]$；在函数域一侧，$A=k[[t]]\cap k(t,\beta)$ 的整闭包 $B$ 是赋值环，问题是 $B/A$ 是否有限生成（即分歧是否有限）。**这题在考"用显式参数化做整闭包 + 判定有限性"。**

**成员与差异**
- **20I3**：$R=F[x,y]/(y^2-x^2-x^3)$。(a) $R$ 是整环；(b) 求 $R$ 的正规化。差别：**结点/尖点三次曲线的坐标环**，正规化由 $t=y/x$ 给出，$x=t^2-1,\ y=t(t^2-1)$。
- **21I3**：$R=F[x,y]/(x^2-y^3)$。(a) 整环；(b) $t=x/y$，$K=F(t)$；(c) $F[t]$ 是 $R$ 在 $K$ 中的整闭包。差别：**与 20I3 是同一个母题的"换皮"**（把 $y^2-x^2-x^3$ 换成 $x^2-y^3$），但多要求证明 $K=F(t)$ 这一步。
- **24I4**：$k$ 特征 $p$，$k(t)\subset k((t))$。(1) $k((t))/k(t)$ 是超越扩张；(2) $\alpha\in k[[t]]$ 在 $k(t)$ 上超越，$\beta=\alpha^p$，$K=k(t,\beta)$，$L=k(t,\alpha)$，$A=k[[t]]\cap k(t,\beta)$，求 $A$ 在 $L$ 中的整闭包 $B$，并证 $A,B$ 都是离散赋值环；(3) $B$ 作为 $A$-模是否有限生成。差别：**从曲线坐标环抬到函数域 + 赋值环**，并且第 (3) 问的答案是"否"（分歧无限 ⇒ 不有限生成），把"整闭包"这个对象推进到**非有限型**的新现象。

**递进关系（升级链）**
20I3（尖点/结点三次曲线的坐标环正规化，全部显式）→ 21I3（换一条曲线，并要求先证 $K=F(t)$）→ 24I4（把场景从"曲线坐标环"抬到"函数域的赋值环"，并追问整闭包是否有限生成——答案是反例）。

**标准解法骨架**
1. 证整环：给出 $R$ 到某个整环的单同态（例如 $R\to F[t]$，$x\mapsto t^2-1,\ y\mapsto t(t^2-1)$），并证明核就是那个理想。
2. 找候选参数 $t$：从奇异处入手，$t=y/x$（20I3）或 $t=x/y$（21I3）——它是"斜率"，在 $R$ 中不出现但在分数域中出现。
3. 用关系式反解：$t^2=(y^2/x^2)=(x^2+x^3)/x^2=1+x$ ⇒ $x=t^2-1,\ y=tx=t(t^2-1)$（20I3）；同理 $y=t^{-2},\ x=t^{-3}$ 得 $x^2=y^3$ 关系（21I3）。
4. 于是 $K=F(t)$，且 $F[t]\supseteq R$ 是整扩张（$t$ 满足 $t^2-1-x=0$，系数在 $R$ 中）。
5. 证 $F[t]$ 是整闭的：$F[t]$ 是 PID/UFD，整闭。
6. 证 $R$ 的整闭包含于 $F[t]$：任何 $z\in K$ 整于 $R$，写 $z=a(t)/b(t)$，用赋值论证/整除性证明 $b$ 必为常数（这一步等价于"$t$ 处的赋值在 $R$ 上已经是整数环"）。
7. （24I4）$A$ 与 $B$ 是 DVR：用 $k[[t]]$ 中的赋值限制；$B/A$ 不有限生成：分歧指数无限（$\alpha$ 的 $p$ 次方落入 $k(t)$ 而 $\alpha$ 不在 ⇒ 无穷多 $p$ 幂分歧层）。

**最容易卡住的一步**：**第 6 步"整闭包恰好是 $F[t]$ 而不是更大"**。需要证明任何整于 $R$ 的元素都落在 $F[t]$ 中；标准做法是把 $z$ 写成分式并对曲线在无穷远处的赋值（或对 $t$ 的赋值 $v_t$）做整除性分析。只证"$F[t]$ 整闭且含 $R$"是不够的——必须排除 $F[t]$ 的局部化之外的元素。

### ALG-M22 数域的判别式与整基

**数学内核.** 数域 $K$ 的整数环 $O_K$ 是 $\mathbb Z$-格：给定一组元素 $a_1,\dots,a_n$，它们构成整基 $\iff$ 判别式 $d_K(a_1,\dots,a_n)$ 等于域判别式 $d_K$（等价地：该判别式无平方因子部分为 1）。**这题在考"用判别式把'是否是整基'这个存在性问题变成一个可计算的条件"。**

**成员与差异**
- **22I6**：$\theta$ 是 $f(X)=X^3+12X^2+8X+1$ 的根，$K=\mathbb Q(\theta)$。(a) 算 $g(X)=X^3+pX+q$ 的判别式 $\operatorname{disc}(g)=-4p^3-27q^2$；(b) $f$ 在 $\mathbb Q$ 上不可约；(c) 算 $d_K(1,\theta,\theta^2)$；(d) 对任意 $n$ 次数域，给出"$a_1,\dots,a_n$ 构成整基"的充分条件；(e) 用该条件写出 $K$ 的显式整基。差别：**从"一般判别式公式"到"具体域"的完整流程**，并要求自己找到充分条件。
- **26I4**：$a\in\mathbb Z$ 无平方因子，$\alpha=\sqrt[3]{a}$，$f(x)=x^3-a$，$\operatorname{Disc}(f)=-27a^2$，$K=\mathbb Q(\alpha)$。证 $O_K$ 有整基 $\{1,\alpha,\alpha^2\}$（当 $a\not\equiv\pm1\bmod9$），以及 $\{1,\alpha,(1\pm\alpha+\alpha^2)/3\}$（当 $a\equiv\pm1\bmod9$）。差别：**纯三次域的分类结果**，把"充分条件"具体化到 $a\bmod 9$ 的二分。

**递进关系**：22I6（一般三次域，要求自己找充分条件）→ 26I4（纯三次域 $\mathbb Q(\sqrt[3]{a})$，$a\bmod9$ 决定整基形状）。**同一条线的"一般方法 → 具体分类"，难度持平（26I4 的答案已在题面给出，属于**降要求**）。**

**标准解法骨架**
1. 三次式 $g(X)=X^3+pX+q$ 的判别式：$\operatorname{disc}(g)=\prod_{i<j}(r_i-r_j)^2=-4p^3-27q^2$。
2. $f$ 不可约：Eisenstein（$f(X+1)=X^3+15X^2+35X+56$？按具体系数验证）或检查无有理根。
3. 计算 $d_K(1,\theta,\theta^2)=\operatorname{disc}(f)=\prod_{i<j}(\theta_i-\theta_j)^2$（用第 1 步的公式代入 $p,q$）。
4. 充分条件：$d_K(1,\theta,\theta^2)$ 与真实的域判别式 $d_K$ 满足 $d_K(1,\theta,\theta^2)=[O_K:\mathbb Z[\theta]]^2\cdot d_K$；因此**若 $d_K(1,\theta,\theta^2)$ 无平方因子（或它的平方因子部分为 1），则 $\{1,\theta,\theta^2\}$ 已是整基**。
5. 若判别式有平方因子 $\ell^2$，就需检查 $\frac1\ell(\theta+c)$ 型元素是否整（即 $X^3-a$ 的"加减 $1$"变形），从而把 $\mathbb Z[\theta]$ 扩大。
6. （26I4）$d_K(1,\alpha,\alpha^2)=-27a^2=-3^3a^2$；平方因子只可能来自 $3$。计算 $\mathbb Z[\alpha]$ 在 $3$ 处的指数：由 $a\bmod9$ 决定 $3$ 是否整除 $[O_K:\mathbb Z[\alpha]]$，得到二分。
7. 验证给定集合确是整基：算其判别式 $=d_K$。

**最容易卡住的一步**：**第 4 步"判别式只差一个平方因子"这个关系式**。很多人以为"$\operatorname{disc}(f)$ 无平方因子"是整基的**必要**条件；实际上 $d_K(1,\theta,\dots)=[O_K:\mathbb Z[\theta]]^2d_K$，所以它只是**充分**条件，而指数为素数的情形必须另作局部检查（这正是 26I4 中 $a\equiv\pm1\bmod9$ 时用 $(1\pm\alpha+\alpha^2)/3$ 的理由）。

### ALG-M23 分圆域、单位根与分圆多项式模 p

**数学内核.** $\Phi_n(X)$ 在 $\mathbb Q$ 上不可约，$\mathbb Q(\zeta_n)/\mathbb Q$ 是 Galois 扩张且群 $(\mathbb Z/n\mathbb Z)^\times$（通过 $\zeta\mapsto\zeta^a$ 作用）；模 $p$（$p\nmid n$）时它分解为 $\varphi(n)/d$ 个 $d$ 次不可约因子，$d=\operatorname{ord}_{(\mathbb Z/n)^\times}(p)$——因为分解对应于 Frobenius $x\mapsto x^p$ 在 $n$ 次单位根集合上的轨道。另一方面 $1-\zeta_p$ 的**迹为 1、范数为 $p$**，这给出 $O_{\mathbb Q(\zeta_p)}=\mathbb Z[\zeta_p]$ 与 $(1-\zeta_p)O_K\cap\mathbb Z=p\mathbb Z$，也给出"单位根不能离 1 太近"的刚性。

**成员与差异（6 次，是本科目最稳定的主线之一）**
- **15T3**：$\zeta$ 是单位根，$\zeta=1+N\eta$（$N\ge3$ 整数，$\eta$ 代数整数）$\Rightarrow\zeta=1$。差别：**只用 $1-\zeta$ 的范数 $"\mid \ell$"这一条事实**（$\ell$ 为 $\zeta$ 的阶），做模长/范数比较。是本主线最早的一次。
- **18T3**：$p\nmid n$，$\bar\Phi_n$ 的根恰是本原 $n$ 次单位根；$\bar\Phi_n$ 在 $\mathbb F_p[X]$ 中不可约 $\iff (\mathbb Z/n\mathbb Z)^\times$ 是由 $p$ 生成的循环群。差别：**模 $p$ 分解的最基本形态**（只问"是否不可约"，不讲 $d$ 的显式公式）。
- **19T4**：$\Phi_p=\mathbb Q(\zeta_p)$，$\operatorname{Gal}\cong(\mathbb Z/p)^\times$；含唯一二次子域；Gauss 和 $g_p=\sum_{a=1}^{p-1}(a/p)\zeta_p^a$ 满足 $\bar g_p=(-1/p)g_p$，$|g_p|^2=p$；确定那个唯一二次子域。差别：**加入 Gauss 和与二次子域的显式判定**（答案 $\mathbb Q(\sqrt{(-1)^{(p-1)/2}p})$）。
- **20I4**：设 $[\ell x]=1+x+\cdots+x^{\ell-1}$。(a) 在 $\mathbb Q[x]$ 中不可约；(b) $\ell=p$ 时在 $\mathbb F_p[x]$ 中被 $x-1$ 整除；(c) $p\ne\ell$，$a$ 是 $p$ 在 $\mathbb F_\ell$ 中的阶，证 $a$ 是使 $GL_m(\mathbb F_p)$ 含有 $\ell$ 阶元的最小 $m$。差别：**把"$\operatorname{ord}_\ell(p)$"翻译成矩阵群的语言**（用 $|GL_m(\mathbb F_p)|$ 中 $\ell$ 的幂次），是同一事实的一次"换语言"。
- **22I5**：$K=\mathbb Q(\zeta_p)$：(a) $\Phi_p$ 是极小多项式；(b) 算 $\operatorname{Tr}_{K/\mathbb Q}(1-\zeta_p)=1$ 与 $N_{K/\mathbb Q}(1-\zeta_p)=p$；(c) 证 $(1-\zeta_p)O_K\cap\mathbb Z=p\mathbb Z$，并推出 $\operatorname{Tr}(y(1-\zeta_p))\in p\mathbb Z$；(d) 确定 $O_K=\mathbb Z[\zeta_p]$。差别：**把 (b)(c)(d) 三者串成一条链**（迹/范数 → 判别式 → 整基）。
- **24I6**：(1) $\Phi_n$ 在 $\mathbb F_q[X]$ 中分解为 $\varphi(n)/d$ 个 $d$ 次不可约因子，$d=\operatorname{ord}_{(\mathbb Z/n)^\times}(q)$；(2) $n=2^r+1$，$p\equiv-3\bmod8$ 时在 $K=\mathbb Q[\zeta_n]$ 上定义 $(x,y)=\sum_\tau\tau(x)\overline{\tau(y)}$，证它是 $K_{\mathbb R}$ 上的内积且 $(\zeta^i,\zeta^j)=2^r\delta_{ij}$；分解 $pO_K$；求素理想 $\mathfrak p$ 中最短非零向量。差别：**把 (1) 的一般分解公式与"格/最短向量"结合**，是全线里最新的、也是最"几何"的一版。

**递进关系（升级链，非常清晰）**
15T3（只用 $N(1-\zeta)=\ell$ 一条事实）→ 18T3（$\Phi_n\bmod p$ 是否不可约 ⟺ $(\mathbb Z/n)^\times=\langle p\rangle$）→ 19T4（$\Phi_p$ + Gauss 和 + 唯一二次子域）→ 20I4（把 $\operatorname{ord}_\ell(p)$ 说成 $GL_m(\mathbb F_p)$ 中含 $\ell$ 阶元的最小 $m$）→ 22I5（$\operatorname{Tr}(1-\zeta_p)=1$、$N(1-\zeta_p)=p$、$O_K=\mathbb Z[\zeta_p]$ 一条链）→ 24I6（一般 $\Phi_n\bmod\mathbb F_q$ 的分解 + 内积/最短向量）。**要求逐级上抬：从一条范数事实，到一般分解公式，再到与几何数论（最短向量）结合。**

**标准解法骨架**
1. $\Phi_n$ 在 $\mathbb Q$ 上不可约：用 $\zeta\mapsto\zeta^p$ 作用保持极小多项式（Eisenstein 于 $\Phi_p(x+1)$，一般 $n$ 用 Dedekind 引理）。
2. $\mathbb Q(\zeta_n)/\mathbb Q$ 的 Galois 群：$\sigma_a:\zeta\mapsto\zeta^a$，$a\in(\mathbb Z/n)^\times$ ⇒ 群 $=(\mathbb Z/n)^\times$。
3. 模 $p$ 分解：$\bar\Phi_n$ 的根是 $\mathbb F_{p^d}$ 中的本原 $n$ 次单位根，$d=\operatorname{ord}_n(p)$；每个不可约因子对应 Frobenius 的一个轨道 ⇒ 因子个数 $=\varphi(n)/d$，次数 $=d$。
4. $1-\zeta_p$ 的迹与范数：$N(1-\zeta_p)=\prod_{a=1}^{p-1}(1-\zeta_p^a)=\Phi_p(1)=p$；$\operatorname{Tr}(1-\zeta_p)=1$（因为 $\Phi_p$ 中 $x^{p-1}$ 的系数为 1）。
5. 由 $N(1-\zeta_p)=p$ 与 $(1-\zeta_p)^{p-1}\sim p\cdot\text{unit}$ 得 $pO_K=(1-\zeta_p)^{p-1}$（完全分歧），进而 $(1-\zeta_p)O_K\cap\mathbb Z=p\mathbb Z$。
6. $O_K=\mathbb Z[\zeta_p]$：算 $d_K(1,\zeta,\dots)=$ 判别式 $=(-1)^{(p-1)/2}p^{p-2}$，比较 $[O_K:\mathbb Z[\zeta_p]]^2$ 与 $p$ 的幂次（由第 5 步知无额外指数）。
7. Gauss 和：$g_p^2=(-1)^{(p-1)/2}p$，$\sigma_a(g_p)=(a/p)g_p$ ⇒ $g_p$ 生成的那个二次子域固定于 $\{a:(a/p)=1\}$ ⇒ 唯一二次子域 $=\mathbb Q(\sqrt{(-1)^{(p-1)/2}p})$。
8. （15T3）若 $\zeta\ne1$ 阶为 $\ell$，则 $N_{\mathbb Q(\zeta)/\mathbb Q}(1-\zeta)=\ell$；由 $1-\zeta=N\eta$（$\eta$ 整）得 $N^{\varphi(\ell)}\mid\ell$，与 $N\ge3$、$\ell\ge$ 某个界矛盾；小 $\ell$ 逐个验证。

**最容易卡住的一步**：**第 5 步"$p=(1-\zeta_p)$ 的 $p-1$ 次幂乘单位"**。要证明 $\frac{p}{(1-\zeta_p)^{p-1}}$ 是单位，必须用 $\prod_{a=1}^{p-1}(1-\zeta_p^a)=p$ 并把每个 $\frac{1-\zeta_p^a}{1-\zeta_p}$ 证成代数整数（它是 $1+\zeta_p+\cdots+\zeta_p^{a-1}$ 型的和，显然是代数整数，且其逆也是代数整数）。这一步是"$O_K$ 是整基"与"$p$ 完全分歧"两件事的共同前提。

### ALG-M24 显式多项式的分裂域、Galois 群与子域格

**数学内核.** 给出一个具体多项式，要求算出它的**分裂域次数、Galois 群、子域格**（有时再加惯性/分歧信息）。核心手段是：不可约 ⇒ 群在根集上传递；判别式是否为平方 ⇒ 是否含于 $A_n$；实根个数 ⇒ 复共轭是哪种置换；配合 $n$ 次传递群的完全列表（$n=4$ 时是 $C_4,V_4,D_4,A_4,S_4$；$n=5$ 时是 $C_5,D_5,F_{20},A_5,S_5$）定位群；再用 Galois 对应把子域算成子群的固定域。

**成员与差异（7 次，本科目最高频）**
- **10I4**：$x^8-5$：求 $[F:\mathbb Q]$ 与 $\operatorname{Gal}(F/\mathbb Q)$。差别：**纯根式 + 分圆混合**，$F=\mathbb Q(5^{1/8},\zeta_8)$；关键是判定 $\mathbb Q(5^{1/8})\cap\mathbb Q(\zeta_8)=\mathbb Q$（因为 $\sqrt5=(5^{1/8})^4$ 而 $\sqrt5\notin\mathbb Q(i,\sqrt2)$），得 $[F:\mathbb Q]=8\cdot4=32$。
- **10T4**：$f_a=x^6+3ax^4+3x^3+3ax^2+1$ 不可约，分裂域的 Galois 群可解。差别：**参数族 + 只问"可解"**；关键是替换 $t=x+\frac1x$：$f_a/x^3=t^3+3(a-1)t+3$，故分裂域由三次式 $g(t)$ 的分裂域与若干个二次扩张 $x^2-t_ix+1$ 拼成 ⇒ 可解。
- **13T6**：$x^4-2$：分裂域、Galois 群、全部子域及对应子群。差别：**入门版 + 子域格**（答案：$\mathbb Q(\sqrt[4]2,i)$，群 $D_4$，子域共 10 个）。
- **15T6**：$x^5-80x+5$：不可约；恰有两个复根；$G\hookrightarrow S_5$ 且像含 $(12345)$ 与 $(12)$；$G\cong S_5$。差别：**引入"实根个数 ⇒ 复共轭置换类型"这条判据**，并用"传递 + 含 5-循环 + 含对换 ⇒ S5"。
- **16T3**：$x^4-x^2-1$：Galois 群 $\cong D_4$（8 阶）；求全部子域及包含关系的偏序。差别：**双二次型四次式**，根的显式结构 $\sqrt{\frac{1\pm\sqrt5}{2}}$ 让子域格更容易算。
- **21I2**：求 $f(x)=x^3-3x+1$ 的分裂域的**自同构群**。差别：**最简版**，只需注意到 $\operatorname{disc}=81=9^2$ 是平方 ⇒ 群含于 $A_3$ ⇒ 群 $=\mathbb Z/3$。
- **25I5**：$f=X^5-X+1$：不可约；求分歧的有限素数并算惯性子群的阶；证 $E/\mathbb Q(\sqrt D)$ 在所有有限素数处不分歧而在阿基米德素处分歧；证 $\operatorname{Gal}(E/\mathbb Q)$ 由惯性子群生成；$\operatorname{Gal}\cong S_5$，$\operatorname{Gal}(E/\mathbb Q(\sqrt D))\cong A_5$。差别：**最新、最重的一版**：把"算群"升级为"用**分歧/惯性**算群"（$D=\operatorname{disc}$，$\operatorname{disc}(X^5+aX+b)=4^4a^5+5^5b^4=4^4(-1)^5+5^5=-256+3125=2869=19\cdot151$）。

**递进关系（升级链，本母题最典型）**
21I2（三次、判别式是平方，一步得 $\mathbb Z/3$）→ 13T6 / 16T3（四次、要算完整子域格）→ 10I4（八次、要把"复合域的交"算清楚）→ 10T4（参数族、用替换 $t=x+1/x$ 降为三次）→ 15T6（五次、引入复共轭置换判据）→ 25I5（五次、改用**惯性子群 + 无分歧性**重算 Galois 群，并把 $\operatorname{Gal}$ 与 $A_5$ 的关系一并给出）。**从"两步算完"到"用分歧理论重算"，要求明确逐级上抬。**

**标准解法骨架**
1. 不可约性：Eisenstein（必要时对 $f(x+c)$ 用）或模 $p$ 约化或直接查有理根。
2. 群在根集上传递 ⇒ $G$ 是 $S_n$ 的传递子群，查 $n$ 次传递群列表缩小范围。
3. 判别式 $\Delta=\prod_{i<j}(r_i-r_j)^2$：$\Delta$ 是有理数平方 $\iff G\subseteq A_n$（对 $n=4$，$\Delta$ 是否为平方把 $V_4/A_4$ 与 $C_4/D_4/S_4$ 分开）。
4. 实根个数：若恰有 $n-2$ 个实根，则复共轭是**一个对换** ⇒ $G$ 含对换。
5. 用"传递 + 含 $n$-循环 + 含对换 $\Rightarrow G=S_n$"（$n$ 素数时）或类似的群论判据定为 $S_n$；否则回到第 2 步的列表逐一排除。
6. 子域格：Galois 对应，把 $G$ 的子群列表与固定域对应起来；对 $D_4$（8 阶）共有 10 个子群，其中 5 个是 2 阶（对应 5 个二次子域）；对子域的包含关系用子群的包含关系反序对应。
7. 纯根式/混合情形（10I4）：先把分裂域写成 $\mathbb Q(a^{1/n},\zeta_n)$，再判定 $\mathbb Q(a^{1/n})\cap\mathbb Q(\zeta_n)$（用 Capelli 判据：$X^n-a$ 在 $K$ 上不可约 $\iff$ $a\notin K^p$（$p\mid n$）且（$4\mid n$ 时）$a\notin-4K^4$），得次数与群。
8. （25I5）用分歧：$\Delta$ 的素因子给出分歧素数，$p$ 处的惯性子群由 $f\bmod p$ 的分解型（Dedekind 定理）给出；"$\operatorname{Gal}$ 由惯性子群生成"用于排除真子群，从而定出 $S_5$ 与 $A_5$。

**最容易卡住的一步**：**第 3–5 步的"$\Delta$ 是否平方 + 实根个数 ⇒ 群"**。以 15T6 为例：$x^5-80x+5$ 恰有两个复根 ⇒ 复共轭是**一个对换**；再配合不可约给出的 5-循环，传递群中含 5-循环与对换的只能是 $S_5$——这条推理只需两步，但需要先正确数出实根个数（用 Sturm 序列或介值定理）。而在 25I5 中则要放弃这条便捷路径，改用"$\operatorname{Gal}$ 由惯性子群生成"（因为 $\operatorname{disc}=19\cdot151$ 无平方因子 ⇒ 群含于 $A_5$，必须换工具）。

### ALG-M25 素数分解律：惯性次数与剩余符号

**数学内核.** 对 Galois 扩张 $L/\mathbb Q$，未分歧素数 $p$ 的分解型由 Frobenius 共轭类决定：$f_p=\operatorname{ord}$ of Frobenius，分解为 $[L:\mathbb Q]/f_p$ 个 $f_p$ 次素理想；而具体判断"$p$ 分裂/惯性"往往变成"某个元素 $\alpha$ 是否是模 $p$ 的 $k$ 次剩余"（三次剩余、二次剩余），即把 Galois 理论翻译成**剩余符号**。$p$ 在中间域中的行为（例如 $p$ 在 $\mathbb Q(\sqrt{\Delta})$ 中分裂还是惯性）给出判别式的二次特征。

**成员与差异**
- **15I3**：$f(x)=x^3+x+1$，$x_i$ 是根，$F=\mathbb Q(x_1)$，$L=\mathbb Q(x_1,x_2,x_3)$，$K=\mathbb Q(\sqrt\Delta)$，$\Delta=-31$。(3.1) $f$ 不可约、$\Delta=-31$、$F$ 非 Galois；(3.2) $\operatorname{Gal}(L/\mathbb Q)\cong S_3$，$\operatorname{Gal}(L/K)\cong\mathbb Z/3$，$\operatorname{Gal}(L/F)\cong\mathbb Z/2$；(3.3) 若 $x^3+x+1=0$ 在 $\mathbb Z/p\mathbb Z$ 中不可解，则 $pO_F$ 仍是素理想、$pO_L$ 是两个素理想之积、$pO_K$ 是两个素理想之积，且 $x^2+31=0$ 在 $\mathbb F_p$ 中可解。差别：**带辅助条件的"不可解 ⇒ 分解型"**，把"模 $p$ 无根"与"$p$ 在 $K$ 中分裂"划等号。
- **18I2**：$K=\mathbb Q(\sqrt[3]5)$，$L$ 是 Galois 闭包。(a) $L$ 有唯一二次子域 $M$，且每个 $p\equiv1\bmod3$ 在 $M$ 中分裂；(b) 定出 $L$ 中分歧的所有素数；(c) $p\ge7$ 时 $f_p$ 与"$5$ 是三次剩余"的三分律：(i) $p\equiv1\bmod3$ 且 $5$ 是三次剩余 ⇒ $p$ 完全分裂；(ii) $p\equiv1\bmod3$ 且 $5$ 不是三次剩余 ⇒ $f_p=3$；(iii) $p\equiv2\bmod3$ ⇒ $5$ 是三次剩余且 $f_p=2$。差别：**把二次符号升级为三次剩余**，并用 $\mathbb Q(\sqrt[3]5)$ 的 Galois 闭包 $=\mathbb Q(\sqrt[3]5,\zeta_3)$ 结构给出完整三分律。

**递进关系**：15I3（二次符号 $\Delta=-31$ 的 Legendre 符号 + $S_3$ 扩张的分解型）→ 18I2（三次剩余符号 + $S_3$ 在 $\mathbb Q(\sqrt[3]5)$ 上的完整分解律，含 $p\bmod3$ 的三分）。**从"二次判别式符号"升到"三次剩余符号"，并要求给出完整的素数分类。**

**标准解法骨架**
1. 算 $\Delta=\prod_{i<j}(r_i-r_j)^2$，判断 $\Delta$ 是否平方 ⇒ $\operatorname{Gal}\subseteq A_3$ 与否。
2. 三次不可约 + $\Delta$ 非平方 ⇒ $\operatorname{Gal}(L/\mathbb Q)\cong S_3$；用 Galois 对应读出 $\operatorname{Gal}(L/K)\cong\mathbb Z/3$（$K=\mathbb Q(\sqrt\Delta)$ 是 $L$ 中唯一二次子域）与 $\operatorname{Gal}(L/F)\cong\mathbb Z/2$。
3. 分解型与 Frobenius：$p$ 未分歧时，$f$ 在 $\mathbb F_p$ 上的分解型 = Frobenius 在根集上的轨道型。因此"$f$ 模 $p$ 无根" ⟺ Frobenius 是 3-循环（对 $S_3$ 只有这一种无不动点的元素）。
4. $p$ 在 $K=\mathbb Q(\sqrt{\Delta})$ 中分裂还是惯性，由 $\Delta$ 是否是模 $p$ 的二次剩余决定（Kronecker 符号）。
5. 由 (2)(3)(4) 拼出 (3.3) 的四条结论（15I3）。
6. 三次情形：$L=\mathbb Q(\sqrt[3]5,\zeta_3)$，$\operatorname{Gal}(L/\mathbb Q)\cong S_3$（或 $\mathbb Z/3\rtimes\mathbb Z/2$）；对 $p\equiv1\bmod3$，$\mathbb F_p$ 含三次单位根，$5$ 的三次剩余性直接决定 $f_p=1$ 或 $3$。
7. 对 $p\equiv2\bmod3$，$\mathbb F_p$ 中三次单位根不存在，$x\mapsto x^3$ 是双射 ⇒ $5$ 自动是三次剩余，且 $p$ 在 $L$ 中的 Frobenius 阶为 2 ⇒ $f_p=2$。

**最容易卡住的一步**：**第 3 步"模 $p$ 的分解型 = Frobenius 的轨道型"（Dedekind 分解定理）**。这是整套推理的枢纽：它把"数论问题（$p$ 怎么分裂）"翻译成"群论问题（Frobenius 属于哪一共轭类）"。这条定理在真题题面里从不写出，必须自己知道。

### ALG-M26 二次扩张、平方类群与 $(\mathbb Z/2)^n$-Galois 扩张

**数学内核.** 特征 $\ne2$ 的域 $F$ 上，二次扩张与 $F^\times/F^{\times2}$ 的元素一一对应（Kummer 理论的最低层）；于是"$F$ 有多少个二次扩张""能否实现 $ (\mathbb Z/2)^n$-Galois 扩张""$F$ 上的元素能否用平方根线性表出"全部归结为**平方类群的大小**。

**成员与差异**
- **21I4**：$p_1,\dots,p_n$ 互异素数，证 $\sqrt{p_1}+\cdots+\sqrt{p_n}\notin\mathbb Q$。差别：**具体数**，用 Galois 群 $(\mathbb Z/2)^n$ 与线性无关性。
- **22I1**：(a) 有理根定理（$a/b$ 是根 ⇒ $a\mid a_0,\ b\mid a_n$）；(b) 证 $\mathbb Q(\sqrt2,\sqrt3)=\mathbb Q(\sqrt2+\sqrt3)$。差别：**本原元素**的实例，把"多个二次扩张的复合 $=$ 单生成"这一步做出来。
- **25I1**：$\operatorname{char}F\ne2$。(1) $F$ 有群为 $\mathbb Z/2\times\mathbb Z/2$ 的 Galois 扩张 $\iff [F^\times:F^{\times2}]>2$；(2) 这样的 Galois 扩张恰是形如 $X^4+aX^2+b$（$b\in F^{\times2}$）的不可约多项式的分裂域。差别：**一般域上的完整 Kummer 判据**，把 (1)(2) 两件事都做成充要条件。

**递进关系（升级链）**
21I4（具体数 $\sqrt{p_i}$ 之和无理性，用 Galois 群 $(\mathbb Z/2)^n$）→ 22I1(b)（多个二次扩张的复合是单生成：本原元素）→ 25I1（一般域上 $[F^\times:F^{\times2}]>2$ $\iff$ $(\mathbb Z/2)^2$-Galois 扩张存在，并给出这类扩张的多项式形状 $X^4+aX^2+b$）。**从"具体数的无理性"升到"一般域的 Kummer 判据"。**

**标准解法骨架**
1. 取 $\sqrt{p_1},\dots,\sqrt{p_n}$ 生成的域 $M=\mathbb Q(\sqrt{p_1},\dots,\sqrt{p_n})$，$\operatorname{Gal}(M/\mathbb Q)\cong(\mathbb Z/2)^n$（每个 $\sqrt{p_i}$ 独立变号）。
2. 设 $\alpha=\sum\sqrt{p_i}\in\mathbb Q$，则 $\alpha$ 被全部 Galois 元固定；取 $\sigma_i$ 只变 $\sqrt{p_i}$ 的号：$\sigma_i(\alpha)-\alpha=-2\sqrt{p_i}$，故 $\sqrt{p_i}\in\mathbb Q$，矛盾（或由 $\{\sqrt{p_i}\}$ 的 $\mathbb Q$-线性无关性直接得）。
3. （22I1(b)）$\mathbb Q(\sqrt2+\sqrt3)\subseteq\mathbb Q(\sqrt2,\sqrt3)$ 显然；反包含：$(\sqrt2+\sqrt3)^2=5+2\sqrt6$ ⇒ $\sqrt6\in$，再由 $\frac{6}{\sqrt6}=\sqrt6$ 与 $(\sqrt2+\sqrt3)\sqrt6=3\sqrt2+2\sqrt3$ 解线性方程组得 $\sqrt2,\sqrt3$。
4. （25I1）$\Leftarrow$：若 $[F^\times:F^{\times2}]>2$，取三个互不同余的平方类 $1,a,b$ ⇒ $F(\sqrt a,\sqrt b)$ 是 $(\mathbb Z/2)^2$-Galois 扩张。
5. $\Rightarrow$：若存在这样的扩张 $L/F$，则 $L=F(\sqrt a,\sqrt b)$（Kummer），从而 $a,b$ 是 $F^{\times2}$ 中不同的类 ⇒ $[F^\times:F^{\times2}]\ge4>2$。
6. （25I1(2)）$X^4+aX^2+b$ 的分裂域：$Y=X^2$ 给出 $Y^2+aY+b=0$，两根之积 $b\in F^{\times2}$；于是分裂域 $=F(\sqrt{y_1},\sqrt{y_2})=F(\sqrt{y_1},\sqrt{b/y_1})$，当 $y_1y_2=b$ 是平方时正好给出 $(\mathbb Z/2)^2$ 型扩张；反向由 Kummer 构造 $X^4-(y_1+y_2)X^2+y_1y_2$。
7. 处理特征 $2$ 的排除（题设 $\operatorname{char}F\ne2$ 使得平方类群与 Kummer 理论可用）。

**最容易卡住的一步**：**第 6 步"$b\in F^{\times2}$ 恰好对应 $(\mathbb Z/2)^2$ 型"**。要看出 $X^4+aX^2+b$ 的分裂域是 $F(\sqrt{y_1},\sqrt{y_2})$，其中 $y_1y_2=b$；当 $b$ 是平方时 $\sqrt{y_2}=\sqrt b/\sqrt{y_1}$，两个平方根只产生一个二次扩张，故 Galois 群恰是 $(\mathbb Z/2)^2$。漏掉 $b\in F^{\times2}$ 这个条件就会得到 $\mathbb Z/4$ 型扩张。

### ALG-M27 SL2(Z) 及其同余子群的生成元与陪集分解

**数学内核.** $SL_2(\mathbb Z)$ 由 $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ 与 $T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ 生成；它在 $\mathbb Q\cup\{\infty\}$（以及上半平面 $\mathcal H$）上的作用是理解同余子群结构的基本工具：$\Gamma(2)$ 在 cusp 上有 3 个轨道，而 Hecke 算子 $\Gamma_0(p)\alpha\Gamma_0(p)$ 的双陪集分解给出矩阵形式 $\begin{pmatrix}a&b\\0&d\end{pmatrix}$（$ad=n$，$0\le b<d$，$\gcd(a,b,d)=1$）的**显式代表元集合**。

**成员与差异**
- **11T6**：证 $SL_2(\mathbb Z)$ 由 $T,S$ 生成；问 $SL_2(\mathbb R)$ 如何。差别：**最基本的生成元问题**，用带余除法做矩阵约化；$SL_2(\mathbb R)$ 不是由这两个生成的（它不是离散的，实际上由所有初等矩阵与 $S$ 生成，但 $\langle S,T\rangle$ 是离散的 $SL_2(\mathbb Z)$）。
- **14T1**：$SL_2(\mathbb R)$ 经分式线性变换作用在 $\mathcal H$ 上。(a) 作用可迁；(b) 定点稳定化子 $\cong SO_2(\mathbb R)$；(c) $\Gamma(2)$ 作用在 $\mathbb Q\cup\{\infty\}$ 上有多少轨道？每轨道给一个代表元。差别：**连续群 $+$ 离散子群的轨道**，答案 3 个轨道，代表元 $0,1,\infty$。
- **26I1**：$p$ 素数，$\gcd(n,p)=1$，$\Gamma_0(p)=\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z):c\equiv0\bmod p\}$，$\alpha=\begin{pmatrix}1&0\\0&n\end{pmatrix}$。证 $\Gamma_0(p)\alpha\Gamma_0(p)=\bigsqcup_{\gamma\in R}\Gamma_0(p)\gamma$，其中 $R=\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:ad=n,\ a>0,\ 0\le b<d,\ \gcd(a,b,d)=1\}$。差别：**Hecke 算子的双陪集分解**，是本主线技术最重的一版（需要处理 $\gcd(a,b,d)=1$ 这个额外条件，并用 $\Gamma_0(p)$ 的左作用把代表元标准化）。

**递进关系（升级链）**
11T6（$SL_2(\mathbb Z)$ 的生成元，纯初等数论）→ 14T1（$SL_2(\mathbb R)$ 在 $\mathcal H$ 上的可迁性 + $\Gamma(2)$ 的 cusp 轨道，开始用群作用）→ 26I1（$\Gamma_0(p)$ 的双陪集分解，Hecke 算子的显式代表元，用到 $\gcd$ 条件与模 $p$ 条件）。**从"生成元"到"轨道"到"双陪集"逐级上抬。**

**标准解法骨架**
1. （11T6）对 $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z)$ 做带余除法：用 $T^{\mp1}$ 把 $b$ 或 $a$ 的绝对值降到小于 $|c|$ 或 $|d|$，再用 $S$ 交换行列；重复至 $c=0$，此时 $ad=1$ 得 $\gamma=\pm T^k$（调整符号后用 $S^2=-I$）。
2. （14T1(a)）可迁性：给定 $z=x+iy$，$\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix}$ 把 $i$ 送到 $z$。
3. （14T1(b)）稳定化子：$\frac{ai+b}{ci+d}=i$ $\Rightarrow$ $a=d,\ b=-c$ 且 $a^2+c^2=1$ ⇒ 矩阵形如 $\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ ⇒ $\cong SO_2(\mathbb R)$。
4. （14T1(c)）$\Gamma(2)$ 的 cusp 轨道：cusp 由 $\mathbb Q\cup\{\infty\}$ 中元素的 $SL_2(\mathbb Z)$ 等价类给出；$\Gamma(2)$ 指数 6，$SL_2(\mathbb Z)$ 传递地作用在 cusp 上，稳定化子由 $\pm T$ 生成；用 $\Gamma(2)$ 的作用把 cusp 分为 3 个轨道：$\{\infty\}$、$\{0\}$、$\{1\}$（因为 $T^2\in\Gamma(2)$ 保持 $\infty$，而 $\Gamma(2)$ 不传递地把奇偶分母分开）。
5. （26I1）双陪集分解：左乘 $\Gamma_0(p)$ 可以把 $\gamma\in\Gamma_0(p)\alpha\Gamma_0(p)$ 化为 $\begin{pmatrix}a&b\\0&d\end{pmatrix}$ 型（用 $\Gamma_0(p)$ 中形如 $\begin{pmatrix}*&*\\0&*\end{pmatrix}$ 的元素消去左下角）。
6. 再证 $ad=n$、$a>0$ 可以规范化（用对角元 $\begin{pmatrix}u&0\\0&u^{-1}\end{pmatrix}\in\Gamma_0(p)$ 的伸缩）。
7. 再用 $\begin{pmatrix}1&k\\0&1\end{pmatrix}\in\Gamma_0(p)$（$k\in\mathbb Z$）把 $b$ 调到 $0\le b<d$，并用 $\gcd(a,b,d)=1$ 排除重复代表元。
8. 唯一性：两个归一化后的代表元若属于同一左陪集，则差一个 $\Gamma_0(p)$ 元，比较左下角与对角元即可推出它们相等。

**最容易卡住的一步**：**第 7–8 步的 $\gcd(a,b,d)=1$ 条件**。它来自 $\Gamma_0(p)$ 能把 $b$ 的模 $d$ 类进一步约化而**不改变** $a,d$ 的条件；若漏掉这一条，$R$ 中会出现两个不同参数给出同一陪集（因为可以用对角 $\begin{pmatrix}u&0\\0&u^{-1}\end{pmatrix}$ 同时缩放并把 $b$ 平移 $d$），导致分解不是不交并。

### ALG-M28 正交变换的反射分解

**数学内核.** 每个正交变换都是若干**反射** $s_a(x)=x-\frac{2(x,a)}{(a,a)}a$ 的乘积，并且所需反射个数恰有精确下界：$g$ 是 $\dim[(g-1)V]$ 个反射之积，$\le2\dim V$。核心恒等式是 $\ker(s_ag-1)=\ker(g-1)\oplus\mathbb Rb$（$a=(g-1)b\ne0$），它让"每乘一个反射就增加一维不动点"可以归纳。平面情形还给出"三线反射生成有限群 ⇒ 三线共点"这种组合结构结论。

**成员与差异**
- **12T3**：$V$ 带正定二次型。(1) $s_v\in O(V)$；(2) $\|v\|=\|w\|$ 时存在一个反射或两个反射之积把 $v$ 送到 $w$；(3) 推出 $O(V)$ 中每个元素可写成不超过 $2\dim V$ 个反射之积。差别：**入门版**，只给上界 $2\dim V$，用"把 $v$ 送到 $w$"这一步引理。
- **15T1**：$V=\mathbb R^n$。(1.1) 若 $a=(g-1)b\ne0$，则 $\ker(s_ag-1)=\ker(g-1)\oplus\mathbb Rb$；(1.2) $g$ 是 $\dim[(g-1)V]$ 个反射之积。差别：**精确版**，把上界 $2\dim V$ 收紧成 $\dim[(g-1)V]$，并把关键引理的**等式**（而非包含）证明出来。
- **16I4**：欧氏平面 $E$ 中的反射。(a) 两直线 $l_1,l_2$ 的反射生成有限群的充要条件（夹角是有理角，即夹角 $\in\pi\mathbb Q$）；(b) 三条两两不同直线的反射生成有限群 ⇒ 三线共点；(c) 由反射生成的有限子群 $G\le\operatorname{Iso}(E)$ 可由至多两个反射生成。差别：**平面情形的组合/分类面**，把"反射分解"与"有限反射群"的结构挂钩。

**递进关系（升级链，非常干净）**
12T3（上界 $2\dim V$）→ 15T1（精确下界 $\dim[(g-1)V]$，并给出核的直和分解）→ 16I4（平面情形的完全分类：两线夹角必须是有理角、三线必共点、$\le2$ 个反射足够）。**同一条"反射分解"主线，从"能给上界"到"能给下界"到"能分类"。**

**标准解法骨架**
1. 验证 $s_a$ 保距：$\|s_a(x)\|^2=\|x\|^2$。
2. 用正交变换的标准形（实正交变换在适当正交基下是若干 2 阶旋转块与 $\pm1$ 块）逐步分解：$\dim[(g-1)V]$ 等于非 1 特征值块的总维数。
3. 关键引理：取 $b$ 使 $a=(g-1)b\ne0$，令 $s_a$ 为对应反射，则 $s_ag$ 固定 $\ker(g-1)$ 与 $b$，且 $\ker(s_ag-1)\supseteq\ker(g-1)\oplus\mathbb Rb$；反向包含由维数或直接计算给出。
4. 归纳：每次构造一个反射减去一维 $\dim[(g-1)V]$，重复有限次后得恒等变换。
5. 于是 $g=s_{a_1}\cdots s_{a_k}$，其中 $k=\dim[(g-1)V]$（这是最优的，因为每个反射最多把 $\dim[(g-1)V]$ 降 1）。
6. （16I4(a)）两个反射之积是旋转 $2\theta$（$\theta$ 是两线夹角）⇒ 生成的群有限 $\iff\theta\in\pi\mathbb Q$。
7. （16I4(b)）三个反射之积是反射或滑移反射；若三线不共点则生成含平移的无限群 ⇒ 有限 $"\Rightarrow"$ 三线共点。
8. （16I4(c)）有限反射群一定是二面体群（正 $n$ 边形的对称群），由两个反射生成。

**最容易卡住的一步**：**第 3 步核的等式 $\ker(s_ag-1)=\ker(g-1)\oplus\mathbb Rb$**。左 $\subseteq$ 右的方向需要做一次真正的计算（把 $s_a$ 的显式公式代入 $s_ag(x)=x$ 再与 $a=(g-1)b$ 联立），仅靠"显然"或维数论证只能得到 $\supseteq$。这一步做对了，归纳才成立、下界才紧。

### ALG-M29 有限域上的乘法特征与点数计数

**数学内核.** 方程 $y^2=x^3+1$ 或递推数列模 $p$，都可以用**乘法特征**处理：$\#\{x^m=a\}=\sum_{\chi\in X_m}\chi(a)$ 把"是否 $m$ 次剩余"写成特征和；Jacobi 和 $J(\chi,\mu)=\sum_{a+b=1}\chi(a)\mu(b)$ 满足 $|J(\chi,\mu)|=\sqrt p$（当 $\chi,\mu,\chi\mu$ 非平凡），于是点数自动落在 $p\pm2\sqrt p$ 内——这就是椭圆曲线 Hasse 界在 $y^2=x^3+1$ 这一特例上的初等证明。另一侧是**范数映射与 Frobenius**：$N:F_{p^2}^\times\to F_p^\times$ 满射，配合 $\alpha^p$ 的作用给出递推数列的周期整除性。

**成员与差异**
- **19I5**：Fibonacci 数列。(1) $p\equiv1,4\bmod5$ ⇒ $p\mid F_{p-1}$；(2) 证范数映射 $N:F_{p^2}^\times\to F_p^\times$ 满射并求核的基数（$p+1$）；(3) $p\equiv2,3\bmod5$ ⇒ $p\mid F_{p+1}$。差别：**Legendre 符号版**，把 $F_n$ 写成 $\frac{\alpha^n-\beta^n}{\alpha-\beta}$（$\alpha,\beta$ 是 $X^2-X-1$ 的根），用 $\alpha\in\mathbb F_p$ 还是 $\mathbb F_{p^2}$ 分情形，$5$ 的二次特征是判据。
- **26I2**：$N_p=\#\{(x,y)\in\mathbb F_p^2:y^2=x^3+1\}$，目标是不等式 $|N_p-p|\le2\sqrt p$。(1) $p=3$ 或 $p\equiv2\bmod3$ 时 $N_p=p$；(2) $N(X_m=a)=\sum_{\chi\in X_m}\chi(a)$；(3) $p\equiv1\bmod3$ 时仍成立。差别：**Jacobi 和版**，题面直接把 $|J(\chi,\mu)|=\sqrt p$ 作为已知，考的是"如何把点数写成 Jacobi 和"。

**递进关系**：19I5（用二次特征 + 范数处理递推数列）→ 26I2（用一般 Jacobi 和证明曲线的 Hasse 界）。**同一条"特征和"主线，从二次特征升到一般乘法特征。**

**标准解法骨架**
1. 把 $F_n$ 用 $\alpha,\beta$ 表示：$F_n=\frac{\alpha^n-\beta^n}{\alpha-\beta}$，$\alpha\beta=-1,\ \alpha+\beta=1$。
2. 判 $\alpha$ 落在 $\mathbb F_p$ 还是 $\mathbb F_{p^2}$：$\alpha\in\mathbb F_p\iff$ 判别式 $5$ 是 $\mathbb F_p$ 中的平方 $\iff (5/p)=1\iff p\equiv\pm1\bmod5$。
3. $\alpha\in\mathbb F_p$ 时用 Fermat $\alpha^{p-1}=1$ 得 $F_{p-1}\equiv0$；$\alpha\notin\mathbb F_p$ 时用 $\alpha^p=\beta$（Frobenius 交换两根）得 $F_{p+1}\equiv0$。
4. 范数映射满射：$\mathbb F_{p^2}^\times/\mathbb F_p^\times$ 的阶为 $p+1$，范数 $N(x)=x^{p+1}=x\cdot x^p$，用 $N(x)=x^{1+p}$ 与 $\mathbb F_{p^2}^\times$ 循环（阶 $p^2-1$）计算核：$\ker N$ 阶 $=(p^2-1)/(p-1)=p+1$。
5. （26I2）把 $N_p$ 写成 $1+\sum_{x\in\mathbb F_p}\big(1+\big(\frac{x^3+1}{p}\big)\big)=p+\sum_x\big(\frac{x^3+1}{p}\big)$（$x^3+1=0$ 时特征取 0 的处理要小心）。
6. $p\equiv2\bmod3$ 时 $x\mapsto x^3$ 是 $\mathbb F_p$ 上的双射 ⇒ 三次特征平凡 ⇒ 特征和为 0 ⇒ $N_p=p$。
7. $p\equiv1\bmod3$ 时把四次特征和分解为两个 Jacobi 和 $J(\chi,\chi)$ 与 $J(\bar\chi,\bar\chi)$，用 $|J|=\sqrt p$ 与三角不等式得 $|N_p-p|\le2\sqrt p$。

**最容易卡住的一步**：**第 6–7 步"把 $\sum_x\big(\frac{x^3+1}{p}\big)$ 识别为 Jacobi 和"**。关键是先写出 $x^3+1=(x+1)(x+\omega)(x+\omega^2)$（$\omega$ 为三次单位根）或做变量替换 $x\mapsto$ 使 $x^3+1$ 变成两个线性因子之积，然后用"乘性特征把乘积拆成 $\chi(a)\mu(b)$ 且 $a+b=1$"——这正是 Jacobi 和的定义。看不出这一层替换，特征和就没法估计。

### ALG-M30 自由模的秩与 PID 上的子模

**数学内核.** PID 上的有限生成模有唯一的分解 $D^n$ 结构，其子模仍自由且秩不超过 $n$；而在一般（甚至非交换）环上，"自由模的秩"这个概念本身可能失效——$R^n\cong R^m$（$n\ne m$）可以发生。**这题在考"秩（IBN）这个不变量在什么条件下存在、何时失效"。**

**成员与差异**
- **11T2**：$D$ 是 PID，$D^n$ 的任意子模是自由模且秩 $m\le n$。差别：**经典结构定理版**，用主理想环上的矩阵对角化（Smith 标准形）。
- **23I2**：(1) $R$ 交换且有 $R^n\cong R^m$ ⇒ $n=m$；(2) 非交换反例：$K$ 非平凡环，$F$ 是可数基 $e_1,e_2,\dots$ 的自由 $K$-模，$R=\operatorname{End}_K(F)$：(a) $R$ 不交换；(b) $f_0(e_{2i})=e_i,f_0(e_{2i-1})=0$ 与 $f_1(e_{2i})=0,f_1(e_{2i-1})=e_i$ 构成 $R$ 作为左 $R$-模的一组基；(c) 对任意 $n,m$ 有 $R^n\cong R^m$。差别：**反例版**，用无限维自同态环构造 IBN 失效。

**递进关系**：11T2（PID 上秩良定义 + 子模自由）→ 23I2（一般交换环秩良定义，非交换环上可失效，并给出显式反例）。**从"性质成立"升到"性质何时成立、何时失效"。**

**标准解法骨架**
1. （11T2）取子模 $M\subseteq D^n$ 的有限生成组（D Noether ⇒ 有限生成，或用 $D^n$ 上的归纳）。
2. 用 $D$ 上矩阵的 Smith 标准形（行/列初等变换）把生成矩阵化为对角形 $\operatorname{diag}(d_1,\dots,d_r,0,\dots)$。
3. 于是 $M\cong D^{r}$ 自由、秩 $r\le n$。
4. （23I2(1)）交换环：取极大理想 $\mathfrak m$，张量到 $R/\mathfrak m$ 上：$R^n\cong R^m$ ⇒ $(R/\mathfrak m)^n\cong(R/\mathfrak m)^m$ ⇒ 向量空间维数相等 ⇒ $n=m$。
5. （23I2(2)(b)）验证 $\{f_0,f_1\}$ 是左 $R$-模 $R$ 的基：任意 $g\in R$，$g=g\circ f_0+g\circ f_1$（因为 $f_0+f_1=\operatorname{id}$ 的"分块"形式），且 $r_0f_0+r_1f_1=0\Rightarrow r_0=r_1=0$。
6. 用 $\{f_0,f_1\}$ 构造 $R\cong R^2$，从而 $R\cong R^n$ 对一切 $n$；复合得 $R^n\cong R^m$。

**最容易卡住的一步**：**第 5 步"$f_0+f_1=\operatorname{id}$"的验证**。必须意识到 $f_0$ 与 $f_1$ 是把可数基"按奇偶分成两半"，两半拼回原基；写成矩阵时它们是互补的两个投影型映射（$f_0$ 把第 $2i$ 个基向量送到第 $i$ 个，其余送 0）。看不出"$\{f_0,f_1\}$ 作为左 $R$-模的基"就构造不出 $R\cong R^2$。

### ALG-M31 投射模、平坦模与有限表现

**数学内核.** 对有限表现的模，"平坦 $\iff$ 投射 $\iff$ 局部自由"三者等价（有限表现把平坦的"局部自由"性质从逐点提升为整体）；但**去掉有限表现，"平坦但不投射"的例子存在**（$S=\prod_{\mathbb N}R$，$I=\oplus_{\mathbb N}R$，$S/I$ 平坦但不投射）。另一条路是可逆分式理想：$A\cdot B=R$ ⇒ $A\oplus$（某模）$\cong$ 自由模 ⇒ $A$ 投射。**这题在考"投射性判据与有限性假设的必要性"。**

**成员与差异**
- **22I2**：$R$ 整环，$K$ 是分式域，$A=d^{-1}I$ 是可逆分式理想（$AB=R$ 对某分式理想 $B$），证 $A$ 是投射 $R$-模。差别：**具体构造投射性**：由 $AB=R$ 取有限多个 $a_i\in A,b_i\in B$ 使 $\sum a_ib_i=1$，定义 $A\to R^n,\ a\mapsto(a_ib)$ 并构造收缩。
- **23I4**：(1) $f:N\twoheadrightarrow M$ 满射，$N$ 有限型、$M$ 有限表现 ⇒ $\ker f$ 有限型；(2) $M$ 有限型时，"平坦 + 有限表现"、"局部自由"、"投射"三者等价；(3) $S=\prod_{\mathbb N}R$，$I=\oplus_{\mathbb N}R\subseteq S$，$S/I$ 是平坦但非投射的 $S$-模。差别：**加上了"有限表现"这一假设的完整讨论 + 反例**；技术含量高于 22I2。

**递进关系**：22I2（具体情形：可逆理想投射，给出显式收缩）→ 23I4（一般理论：三条等价 + 去掉有限表现的反例）。**从"一个例子"升到"完整判据 + 反例"。**

**标准解法骨架**
1. （22I2）由 $AB=R$，存在 $a_i\in A,b_i\in B$（$i=1,\dots,n$）使 $\sum a_ib_i=1$（因为 $1\in AB$ 且是有限和）。
2. 定义 $\varphi:A\to R^n,\ a\mapsto(a b_1,\dots,a b_n)$ 与 $\psi:R^n\to A,\ (r_i)\mapsto\sum r_ia_i$。
3. 验证 $\psi\circ\varphi=\operatorname{id}_A$（因为 $\psi(\varphi(a))=\sum ab_ia_i=a\sum a_ib_i=a$）⇒ $A$ 是 $R^n$ 的直和项 ⇒ 投射。
4. （23I4(1)）由 $M$ 有限表现得 $R^n\to R^m\to M\to0$，与 $N\twoheadrightarrow M$ 做拉回，用 Schanuel 引理：$\ker f$ 是有限生成模的核。
5. （23I4(2)）(b)$\Rightarrow$(c)$\Rightarrow$(a) 是标准；(a)$\Rightarrow$(b)：有限表现 + 平坦 ⇒ 在每点局部自由（用"平坦 + 有限表现 ⇒ 自由"的局部判据，把 $M_f$ 的自由性用 Nakayama 从 $M\otimes R/\mathfrak m$ 的维数读出）。
6. （23I4(3)）$S/I$ 平坦：$I$ 是纯理想（pure ideal）——对任意 $s\in S$，$sI=sS\cap I$ 成立，故 $S/I$ 平坦。
7. $S/I$ 不投射：投射模是 $S$ 的直和项，而 $I$ 不是 $S$ 的直和项（若 $S=I\oplus J$，取 $e\in J$ 的幂等元，与 $\prod$/$\oplus$ 的结构矛盾）。

**最容易卡住的一步**：**第 6 步"$I=\oplus_{\mathbb N}R$ 在 $S=\prod_{\mathbb N}R$ 中是纯理想"**。需要证明 $sI = sS\cap I$：$\subseteq$ 显然；$\supseteq$ 需要把 $s\cdot t\in I$（$t\in S$）逐坐标分析，并识别出 $s$ 的"零坐标集"这一组合结构。这一步是"平坦"判据的实质，也是 $S/I$ 平坦而非投射的关键。

### ALG-M32 二项式系数、整值多项式与 p 进估值

**数学内核.** 二项式系数 $\binom xk$ 构成整值多项式 $\mathbb Z$-基；它的 $p$ 进估值 $v_p\binom nm$ 被 $\log_p n$ 控制（因为 $n!$ 中 $p$ 的幂次是 $\sum\lfloor n/p^i\rfloor$，不超过 $n/(p-1)$ 量级）；这两件事配合可得初等数论估计（Chebyshev 的 $\pi(n)$ 下界、调和级数不为整数）。**这题在考"用二项式系数的整数性与估值做算术估计"。**

**成员与差异**
- **11T4**：$1+\frac12+\frac13+\cdots+\frac1n$ 是否是整数？差别：**估值版的最简应用**——取 $2^k\le n<2^{k+1}$，把和乘 $2^{k-1}\cdot\operatorname{lcm}$ 后看奇偶性。
- **16T2**：$\binom xk$ 的整数性；每个 $f:\mathbb Z_{\ge0}\to\mathbb Z$ 唯一写成 $\sum a_k\binom xk$（$a_k\in\mathbb Z$）；每个 $f:\mathbb Z\to\mathbb Z$ 唯一写成 $\sum a_k\varphi_k(x)$（$\varphi_k(x)=\binom{x+\lfloor k/2\rfloor}{k}$）。差别：**整值多项式的 $\mathbb Z$-基**，把"整数性"升级为"结构定理"。
- **18T2**：(a) 存在 $1\le m\le n-1$ 使 $\binom nm\ge2^n/n$；(b) 对任意素数 $p$，$v_p\binom nm\le\log_p n$；(c) 推出 Chebyshev 不等式 $\pi(n)\ge\frac{n}{\log_2 n}-1$。差别：**估值 + 不等式估计**，把 (b) 用作 (c) 的输入。

**递进关系**：11T4（用一个估值技巧证明"不是整数"）→ 16T2（把二项式系数的整数性升级为整值函数的 $\mathbb Z$-基结构定理）→ 18T2（用估值上界推出 $\pi(n)$ 的下界）。**同一条"二项式系数 + $p$ 进估值"主线的三种用法。**

**标准解法骨架**
1. 设 $2^k\le n<2^{k+1}$，取 $L=\operatorname{lcm}(1,\dots,n)$；$L\sum_{i=1}^n\frac1i=L\cdot\frac{?}{}$——更干净的做法：通分后分子中的 $2^k$ 项只有 $\frac1{2^k}$ 贡献奇数分子（其它项在通分后分子为偶数），故和不是整数。
2. $\binom xk$ 整值：$\binom xk=\frac{x(x-1)\cdots(x-k+1)}{k!}$，$x\in\mathbb Z$ 时是 $k$ 个连续整数之积除以 $k!$，即 $\binom nk$（$n\ge k$）或 0（$0\le n<k$）或 $(-1)^k\binom{k-n-1}{k}$（$n<0$）。
3. 整值多项式基：用有限差分 $\Delta f(x)=f(x+1)-f(x)$，$a_k=(\Delta^kf)(0)\in\mathbb Z$，唯一性由差分公式给出。
4. $\varphi_k$ 版：把 $\mathbb Z$ 上的函数拆成 $\mathbb Z_{\ge0}$ 上的两半（$x\ge0$ 与 $x<0$），分别用 $\binom xk$ 与 $\binom{-x-1}{k}$ 展开再拼接。
5. $v_p\binom nm$：用 Legendre 公式 $v_p(n!)=\sum_{i\ge1}\lfloor n/p^i\rfloor$，得 $v_p\binom nm=v_p(n!)-v_p(m!)-v_p((n-m)!)\le v_p(n!)\le\frac{n}{p-1}$；对 $n<2^k$ 型范围估到 $\log_p n$。
6. Chebyshev：$\prod_{m=1}^{n-1}\binom nm=\frac{(n!)^{n-1}}{\prod}$ 型恒等式配合 $\binom nm\le2^n$ 与 $v_p$ 的上界，把 $\log(n!)$ 夹在 $\pi(n)\log n$ 与 $n\log 2$ 之间。

**最容易卡住的一步**：**第 5 步 $v_p\binom nm\le\log_p n$ 的估计**。Legendre 公式给的是 $v_p(n!)=\frac{n-s_p(n)}{p-1}$（$s_p$ 为 $p$ 进制数字和），由此得 $v_p\binom nm\le\frac{\log_2 n}{\log_2 p}=\log_p n$。直接用 $v_p(n!)\le\frac{n}{p-1}$ 是**不够的**（那是关于 $n$ 的线性界），必须用数字和形式才能压到 $\log_p n$。

### ALG-M33 公共特征向量与不变子空间的存在性

**数学内核.** "存在公共特征向量/一维不变子空间"与"不存在任何非平凡不变子空间"是同一枚硬币的两面：前者靠**交换性/可解性**（若一族算子互相交换或构成可解李代数，则在代数闭域上可同时上三角化，从而有公共特征向量——Lie 定理的初等情形），后者靠**模的单纯性**（$V$ 是单生成的 $F[T]$-模且极小多项式不可约 ⇒ $V\cong F[T]/(m_T)$ 是域 ⇒ 单纯）。

**成员与差异**
- **10I1**：$AB-BA=B$，证 $A,B$ 有公共特征向量。差别：**"几乎交换"**——$B$ 由换位子给出，故 $B$ 幂零、$\ker B$ 是 $A$-不变子空间，在 $\ker B$ 上对 $A$ 用归纳法。
- **11I4**：$T$ 的极小多项式不可约，且存在 $v$ 使 $\{T^iv\}$ 张成 $V$，证 $V$ 无非平凡 $T$-不变子空间。差别：**"没有"的一侧**——$V\cong F[T]/(m_T)$ 而 $m_T$ 不可约 ⇒ $F[T]/(m_T)$ 是域 ⇒ $V$ 是单模（注意此题的 $F=\mathbb R$，$m_T$ 不可约意味着没有实特征值）。
- **13I2**：$f\in\mathbb Z_{>0}$，$V_i$（$i\in\mathbb Z/f\mathbb Z$）非零，$\varphi_i:V_i\to V_{i+1}$，$\psi_i:V_i\to V_{i-1}$，满足 $\varphi_{i-1}\psi_i=0$、$\psi_{i+1}\varphi_i=0$（"Orpheus 条件"：回头即死）。证在 (2.1) 所有 $\psi_i=0$、或 (2.2) 各 $\dim V_i$ 相等时，存在**直线** $\ell_i\subset V_i$ 使 $\varphi_i(\ell_i)\subset\ell_{i+1}$、$\psi_i(\ell_i)\subset\ell_{i-1}$。差别：**环形复形上的公共特征直线**，是"公共特征向量"母题的**结构性升级**：不是在单个空间上找，而是在一个循环箭图表示中处处找，且要用到 $\dim V_i$ 相等这个约束。

**递进关系（升级链）**
10I1（单个交换关系 $[A,B]=B$ ⇒ 一个公共特征向量）→ 11I4（反方向：极小多项式不可约 + 单生成 ⇒ 不存在不变子空间）→ 13I2（环形箭图上处处找到公共特征直线，且需要 $\dim V_i$ 相等或 $\psi=0$ 这种全局条件）。**从"存在一个"到"不存在任何"到"在环形图上同时处处存在"。**

**标准解法骨架**
1. （10I1）由 $AB-BA=B$ 得 $B$ 幂零（用 $[A,B^k]=kB^k$ 与 $\operatorname{tr}$，或直接看 $B$ 的特征值全为 0），故 $\ker B\ne0$。
2. $A(\ker B)\subseteq\ker B$：因为 $ABx=BAx+Bx$，$Bx=0$ ⇒ $ABx=BAx$ ⇒ $BAx\in\operatorname{im}B$ 但 $Ax\in\ker B$ ⇒ $BAx=0$。
3. 在 $\ker B$ 上对 $\dim$ 归纳（或直接在 $\ker B$ 上取 $A$ 的特征向量，$\mathbb C$ 上必有）。
4. （11I4）$V=F[T]v$ ⇒ $V\cong F[T]/\operatorname{Ann}(v)$，$\operatorname{Ann}(v)=$ 极小多项式的理想；$m_T$ 不可约 ⇒ $F[T]/(m_T)$ 是域 ⇒ 理想都是平凡的 ⇒ 无不变子空间。
5. （13I2）先做 (2.1)：$\psi_i=0$ 时环退化为 $\varphi$ 的链，在 $V_1$ 上取 $\varphi_{f}\varphi_{f-1}\cdots$ 的不动/特征直线并逐步推进（用 $\mathbb C$ 上线性算子必有特征向量）。
6. （13I2）再做 (2.2)：取所有维数相等的 $d$。若某个 $\varphi_i$ 奇异，则其核给出维数下降，与"所有 $V_i$ 维数相等 + 条件 $\psi_{i+1}\varphi_i=0$"矛盾 ⇒ 所有 $\varphi_i$ 是同构（或至少秩恒为 $d$）；于是 $\{\varphi\}$ 构成一个可交换（循环）的同构族，取 $\varphi_f\cdots\varphi_1$ 的特征向量 $\ell_1$ 再前推。
7. 验证 $\varphi_i(\ell_i)=\ell_{i+1}$ 与 $\psi_i(\ell_i)=\ell_{i-1}$（后者由 $\psi_{i+1}\varphi_i=0$ 与秩条件推出）。

**最容易卡住的一步**：**13I2 (2.2) 的"所有 $\varphi_i$ 秩相同"论证**。需要从"$\dim V_i$ 全相等"与"$\psi_{i+1}\varphi_i=0$"推出 $\operatorname{rk}\varphi_i+\operatorname{rk}\psi_{i+1}\le d$，再由循环性与维数守恒锁定等号处处成立，从而 $\varphi_i$ 全为同构。漏掉这一步就只能得到"存在一条链"而得不到"环形闭合"。

### ALG-M34 交换性的定量后果：矩阵对的行列式/范数不等式

**数学内核.** 交换性（或不交换性）对**谱**施加了可量化的约束：$AB=BA$ 时 $A,B$ 可同时上三角化，$\det(A^2+B^2)=\prod(\lambda_j^2+\mu_j^2)=\det(A+iB)\overline{\det(A+iB)}=|\det(A+iB)|^2\ge0$；反过来 $UV\ne VU$ 时，$U$ 与 $VUV^{-1}$ 的特征值配对会出现"错位"，并用酉结构把这个错位量化为 $N(1+V)\ge4$。

**成员与差异**
- **14I6**：(a) $A,B$ 实矩阵交换 ⇒ $\det(A^2+B^2)\ge0$；(b) 推广到 $k$ 个两两交换的矩阵（$\det(\sum A_i^2)\ge0$ 型）。差别：**用 $|\det(A+iB)|^2$ 一步解决**，推广靠同时复化 + 同时上三角化。
- **17I5**：$UV\ne VU$，$U$ 可对角化且与 $VUV^{-1}$ 交换。(a) 存在两对不同的 $(\lambda_i,\mu_i)$ 且 $\lambda_i\ne\mu_i$ 使 $E_{\lambda_i,\mu_i}\ne0$；(b) $U,V$ 酉时证 $N(1+V)=\operatorname{tr}((1+V)^*(1+V))\ge4$。差别：**不交换的定量后果**；核心是"$V$ 把 $U$ 的特征空间置换，非交换意味着置换非平凡"，再借助酉性把两组配对距离的平方和下界算出来。

**递进关系**：14I6（交换 ⇒ 行列式非负，一步复化）→ 17I5（不交换 ⇒ 范数有下界，需要特征空间置换 + 酉性）。**从"交换的正向推论"升到"不交换的反向下界"。**

**标准解法骨架**
1. （14I6）$A,B$ 实且交换 ⇒ 复化后仍在 $\mathbb C$ 上交换 ⇒ 可同时上三角化（对 $A$ 的特征空间归纳）。
2. 在上三角形式下 $\det(A^2+B^2)=\prod_j(\lambda_j^2+\mu_j^2)$，其中 $\lambda_j,\mu_j$ 是同一个三角化下的对角元。
3. 关键改写：$\prod_j(\lambda_j^2+\mu_j^2)=\prod_j(\lambda_j+i\mu_j)\prod_j(\lambda_j-i\mu_j)=\det(A+iB)\overline{\det(A+iB)}=|\det(A+iB)|^2\ge0$。
4. 推广：对 $k$ 个交换矩阵，任何"实系数且每项为偶数次"的乘积组合都可用"复数化 + 共轭配对"或直接对角元论证。
5. （17I5(a)）$U$ 可对角化，在 $U= \operatorname{diag}(\lambda_1,\dots,\lambda_n)$ 的基下，$VUV^{-1}$ 也与 $U$ 交换 ⇒ $V$ 置换 $U$ 的特征空间；$UV\ne VU$ ⇒ 该置换非平凡 ⇒ 存在两个不同特征值配对 $(\lambda,\mu),(\lambda',\mu')$。
6. 由非平凡置换可得 $\lambda\ne\mu$ 且 $\lambda'\ne\mu'$（否则 $V$ 保持某个特征空间），且 $(\lambda,\mu)\ne(\lambda',\mu')$。
7. （17I5(b)）在酉情形用 $\|(1+V)x\|^2=2\|x\|^2+2\operatorname{Re}\langle Vx,x\rangle$ 与置换结构，在 $E_{\lambda,\mu}$ 上得到两块互不相消的贡献，相加得 $N(1+V)\ge4$。

**最容易卡住的一步**：**17I5(b) 的"$\ge4$"从何而来**。要在两个 $E_{\lambda_i,\mu_i}$ 上分别做估计：每个非零分块给出的贡献至少是 $2$（因为 $\lambda_i\ne\mu_i$ 迫使 $V$ 在该块上"把向量搬到别处"），两块相加得 $4$。直接对 $1+V$ 做整体估计只能得到 $\ge0$；必须用 (a) 给出的**两个**分块结构。

### ALG-M35 矩阵共轭性的判定：特征多项式何时决定相似类

**数学内核.** 对 $2\times2$ 且特征多项式不可约的矩阵，"同一个特征多项式"就等价于"共轭"（有理标准形的唯一性）；特征多项式可约时这一结论失效（$\operatorname{diag}(1,1)$ 与 $\operatorname{diag}(1,1)$ 的两个不同 Jordan 型/或 $-I$ 与 $\operatorname{diag}(1,1)$ 型反例）。对块矩阵 $A_{\mathrm{db}}=\begin{pmatrix}0&I\\A&0\end{pmatrix}$，其特征/极小多项式可由 $A$ 的算出（$\chi_{A_{\mathrm{db}}}(x)=\pm\chi_A(x^2)$ 型），而 $A_{\mathrm{db}}$ 与 $B_{\mathrm{db}}$ 共轭**并不**蕴含 $A$ 与 $B$ 共轭。**这题在考"相似类的判定究竟需要哪些不变量"。**

**成员与差异**
- **10I2**：(a) 给出单同态 $\mathbb C\hookrightarrow M_2(\mathbb R)$；(b) 任意两个这样的同态相差一个 $GL_2(\mathbb R)$-共轭；(c) $h\in GL_2(\mathbb R)$ 的特征多项式 $f$ 不可约，$F=\langle h,aI\rangle\cong\mathbb C$；(d) $h'$ 与 $h$ 特征多项式相同 ⇒ 在 $GL_2(\mathbb R)$ 中共轭；(e) $f$ 可约时是否仍成立？差别：**由"不可约特征多项式"驱动**——$f$ 不可约时 $h$ 的极小多项式 $=$ 特征多项式，有理标准形唯一；$f$ 可约时（如 $h=I$ 与 $h$ 有重根）反例立即出现。
- **14T3**：$A\in M_3(\mathbb Q)$，$A_{\mathrm{db}}=\begin{pmatrix}0&I_3\\A&0\end{pmatrix}\in M_6(\mathbb Q)$。(a) 用 $A$ 的特征/极小多项式表示 $A_{\mathrm{db}}$ 的；(b) 若 $A_{\mathrm{db}}$ 与 $B_{\mathrm{db}}$ 在 $GL_6(\mathbb Q)$ 中共轭，$A$ 与 $B$ 是否共轭？差别：**换成块矩阵**，(a) 是"用最小多项式算特征多项式"，(b) 是"共轭性是否可下推"——答案是不一定（题面明确要求"证明或给反例"）。

**递进关系**：10I2（$2\times2$、不可约 vs 可约的二分，结论是"不可约 ⇒ 共轭"）→ 14T3（$6\times6$ 块矩阵，问"共轭能否下推"，答案是否定的）。**从"什么时候能决定"到"什么时候不能决定"。**

**标准解法骨架**
1. （10I2(a)）把 $\mathbb C$ 实现为 $M_2(\mathbb R)$ 的子环：$a+bi\mapsto\begin{pmatrix}a&-b\\b&a\end{pmatrix}$。
2. (b) 任意单同态 $\varphi$ 的像由 $\varphi(i)=J$（$J^2=-I$）决定；所有满足 $J^2=-I$ 的实矩阵在 $GL_2(\mathbb R)$ 下共轭（它们都相似于 $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$）。
3. (c) $f$ 不可约 ⇒ $\mathbb R[h]\cong\mathbb R[x]/(f)\cong\mathbb C$（$f$ 是二次不可约 ⇒ 商是二次域，即 $\mathbb C$）。
4. (d) $h,h'$ 有相同的不可约特征多项式 $f$ ⇒ 极小多项式都等于 $f$ ⇒ 有理标准形（友矩阵）相同 ⇒ 在 $GL_2(\mathbb R)$ 中共轭。
5. (e) $f$ 可约（例如 $f=(x-1)^2$）：$h=I$ 与 $h=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ 特征多项式相同但不共轭 ⇒ 结论失效。
6. （14T3(a)）计算 $A_{\mathrm{db}}$ 的特征多项式：$\det(xI-A_{\mathrm{db}})=\det\begin{pmatrix}xI&-I\\-A&xI\end{pmatrix}=\det(x^2I-A)$（分块行列式公式）$=\prod(x^2-\lambda_i)$，故 $\chi_{A_{\mathrm{db}}}(x)=\chi_A(x^2)$ 型；极小多项式由 $A$ 的极小多项式的偶次化给出（要小心 $x^2-\lambda$ 分解情形）。
7. （14T3(b)）构造反例：取 $A,B$ 有相同特征多项式但不共轭，使 $\chi_A(x^2)$ 与 $\chi_B(x^2)$ 相同且 $A_{\mathrm{db}},B_{\mathrm{db}}$ 共轭（例如用 $A\oplus B^t$ 型对称化），从而证否。

**最容易卡住的一步**：**14T3(a) 的分块行列式公式**。$\det\begin{pmatrix}xI_n&-I_n\\-A&xI_n\end{pmatrix}=\det(x^2I_n-A)$ 需要先在 $xI$ 可逆的假设下化简再用多项式恒等式延拓，或直接对分块做行列变换。写错一块符号（$-I$ 与 $I$）就会得到 $\det(x^2I+A)$，后面全错。

### ALG-M36 三角函数连乘积与分圆计算

**数学内核.** $2\cos\frac{k\pi}{p}=\zeta_p^k+\zeta_p^{-k}$，于是 $\prod_{k=1}^{(p-1)/2}2\cos\frac{k\pi}{p}=\prod_{k=1}^{(p-1)/2}\zeta_p^{-k}(1+\zeta_p^{2k})$；再用 $\prod_{k=1}^{p-1}(1+\zeta_p^k)=\Phi_p(-1)=1$ 与幅角配平，得到 $\prod_{k=1}^{(p-1)/2}2\cos\frac{k\pi}{p}=1$，即 $\prod\cos\frac{k\pi}{p}=2^{-(p-1)/2}$——一个永远是有理数（事实上是 2 的负幂）的乘积。

**成员与差异**
- **10T3**：(a) 求 $\cos\frac\pi7\cos\frac{2\pi}7\cos\frac{3\pi}7$（$=1/8$）；(b) 证 $\prod_{n=1}^{(p-1)/2}\cos\frac{n\pi}{p}\in\mathbb Q$ 并定值。差别：具体 $p=7$ + 一般 $p$。
- **14T2**：**与 10T3 逐字相同**（只是把 (a) 标成"to warm up"，分值从 (a)5+(b)15 略作调整）。这是本库中除 150 阶群之外的另一次**逐字重出**。

**递进关系**：无递进，**原样重复**。2010 team 与 2014 team 的同一道题，说明命题人把它当作稳定的"送分题"。

**标准解法骨架**
1. 令 $\zeta=e^{2\pi i/p}$，注意 $2\cos\frac{k\pi}{p}=\zeta^{k/2}+\zeta^{-k/2}$，取 $\omega=e^{\pi i/p}$（$2p$ 次单位根）则 $2\cos\frac{k\pi}{p}=\omega^k+\omega^{-k}$。
2. 写 $\omega^k+\omega^{-k}=\omega^{-k}(1+\omega^{2k})$；$\omega^{2k}=\zeta^k$。
3. 乘积 $=\omega^{-\sum_{k=1}^{(p-1)/2}k}\prod_{k=1}^{(p-1)/2}(1+\zeta^k)=\omega^{-(p^2-1)/8}\prod_{k\ \text{奇}}(1+\zeta^k)$。
4. $\prod_{k=1}^{p-1}(1+\zeta^k)=\Phi_p(-1)=((-1)^p-1)/((-1)-1)=1$，且偶 $k$ 部分与奇 $k$ 部分之积为 1、两者模长相等 ⇒ $\prod_{k\ \text{奇}}(1+\zeta^k)$ 的模为 1、幅角为 $\sum_{k\ \text{奇}}\frac{k\pi}{p}=\frac{(p^2-1)\pi}{8p}$。
5. 于是 $\prod_{k\ \text{奇}}(1+\zeta^k)=\omega^{(p^2-1)/8}$，与第 3 步的 $\omega^{-(p^2-1)/8}$ 相消，得乘积 $=1$。
6. 结论 $\prod_{k=1}^{(p-1)/2}2\cos\frac{k\pi}{p}=1$ ⇒ $\prod\cos\frac{k\pi}{p}=2^{-(p-1)/2}$；$p=7$ 给出 $1/8$。

**最容易卡住的一步**：**第 4 步"$\prod_{k\ \text{奇}}(1+\zeta^k)$ 的幅角"**。乘积是复数，要先用 $|1+\zeta^k|=2\cos\frac{k\pi}{p}$（正数）确定模长，再用 $\arg(1+\zeta^k)=\frac{k\pi}{p}$（因为 $1+e^{i\theta}=2\cos\frac\theta2e^{i\theta/2}$）求幅角之和。漏掉幅角只证模长，就会得到一个"模为 1 的复数"，无法断定它等于 1。

### ALG-M37 非负整数线性组合的表示与生成函数（数值半群）

**数学内核.** 用有限集合 $T$（或 $\{a,b\}$）的非负整数线性组合表示 $n$，其计数 $a_n$ 的生成函数恰是 $\frac1{1-\sum_{t\in T}z^t}$（因为"序列"的分解对应形式幂级数的乘积，而"有序序列"对应 $(\sum z^t)^m$）；而 $\{a,b\}$ 生成的**数值半群**的亏格恰为 $\frac{(a-1)(b-1)}2$（Frobenius 数 $ab-a-b$）。

**成员与差异**
- **10I5**：$T\subset\mathbb Z_{>0}$ 有限，$a_n=$ 满足 $m\le n$、$t_i\in T$、$\sum t_i=n$ 的有限序列 $(t_1,\dots,t_m)$ 之个数。证 $1+\sum_{n\ge1}a_nz^n$ 是有理函数并求出它（$=\frac1{1-\sum_{t\in T}z^t}$）。差别：**生成函数版**，"序列"（有序）对应无穷级数的几何展开。
- **17T5**：$N(a,b)=\{ax+by:x,y\ge0\}$。(a) $N\ge a(b-1)$ ⇒ $N\in N(a,b)$；(b) 恰有 $\frac{(a-1)(b-1)}2$ 个正整数不属于 $N(a,b)$。差别：**数值半群版**，(b) 用"配对 $n\leftrightarrow ab-a-b-n$"这一对称性直接数出亏格。

**递进关系**：10I5（生成函数把"表示个数"编码成有理函数）→ 17T5（把"能否表示"这一**定性**问题做成 Frobenius 数的精确值 + 亏格计数）。**从"数表示个数"到"刻画可表示性"。**

**标准解法骨架**
1. （10I5）设 $S(z)=\sum_{t\in T}z^t$。恰有 $m$ 项的序列的生成函数是 $S(z)^m$。
2. 求和（$m\ge0$，注意 $m\le n$ 自动满足）得 $\sum_{m\ge0}S(z)^m=\frac1{1-S(z)}$，这是 $z$ 的有理函数。
3. 由于 $S$ 的系数非负且 $S(0)=0$，$\frac1{1-S}$ 作为形式幂级数良定义，其 $z^n$ 系数就是 $a_n$。
4. （17T5(a)）设 $N\ge a(b-1)$。取 $0\le y\le a-1$ 使 $by\equiv N\pmod a$（$b$ 可逆 mod $a$，因为 $(a,b)=1$）；则 $N-by\ge a(b-1)-b(a-1)=a-b$ hmm——更精确地：$N-by\ge a(b-1)-b(a-1)=ab-a-ab+b=b-a$，需按 $a>b$ 或 $b>a$ 讨论；标准做法是取 $y$ 为 $N b^{-1}\bmod a$ 的最小非负代表，则 $by\le b(a-1)$，$N-by\ge a(b-1)-b(a-1)=b-a$，当 $a<b$ 时可能为负——此时交换 $a,b$ 的角色（不妨 $a<b$）：$N\ge a(b-1)\ge$ 使 $N-by\ge0$，且 $a\mid (N-by)$，故 $N=ax+by$。
5. （17T5(b)）配对：$n\in N(a,b)\iff ab-a-b-n\notin N(a,b)$（对 $0\le n\le ab-a-b$），验证 $n=ax+by$ 与 $ab-a-b-n=a(a-1-x)+b(b-1-y)$ 互为补。
6. 数出 $\{1,\dots,ab-a-b\}$ 中的配对数 $=\frac{ab-a-b+1}2=\frac{(a-1)(b-1)}2$。

**最容易卡住的一步**：**第 5 步的配对映射**。恒等式 $ab-a-b-n=a(a-1-x)+b(b-1-y)$（当 $n=ax+by$）要求 $x\le a-1,\ y\le b-1$——即每个可表示数都有这样的"规范表示"。这一步需要先用"若 $x\ge a$ 则 $ax+by=a(x-a)+b(y+b)$"把表示规范化（$x<a$ 且 $y<b$），再谈配对。跳过规范化，配对就不成立。

### ALG-M38 Cauchy 型矩阵与 Gram 矩阵的正定性

**数学内核.** 形如 $\big(\frac1{a_i+a_j}\big)$、$\big(\frac1{1+a_i+a_j}\big)$、$\big(t^{a_i+a_j}\big)$ 的矩阵都是**Gram 矩阵**：$\frac1{1+a_i+a_j}=\int_0^1t^{a_i}t^{a_j}dt$，$t^{a_i+a_j}=\langle t^{a_i},t^{a_j}\rangle$，因此自动半正定；正定性则等价于这些函数线性无关，即 $a_i$ 互异。行列式的显式公式（Cauchy 行列式）进一步给出秩与零空间。

**成员与差异**
- **12T1**：$a_i+b_j\ne0$，$c_{ij}=\frac1{a_i+b_j}$，证 $\det C=\frac{\prod_{i<j}(a_i-a_j)(b_i-b_j)}{\prod_{i,j}(a_i+b_j)}$。差别：**行列式的显式公式**（Cauchy 行列式），证法是对 $n$ 归纳做行/列消去。
- **14I2**：$a_1,\dots,a_n\ge0$ 实数。(a) $A=(t^{a_i+a_j})$ 对一切 $t>0$ 半正定，并求秩；(b) $B=\big(\frac1{1+a_i+a_j}\big)$ 半正定；(c) $B$ 正定 $\iff a_i$ 互异。差别：**Gram 矩阵视角**，用 $f_i(t)=t^{a_i}$ 在 $L^2$ 中的内积解释一切；(a) 的秩 $=$ 不同 $a_i$ 的个数。

**递进关系**：12T1（Cauchy 行列式的显式公式，纯代数归纳）→ 14I2（Gram 矩阵的半正定性与正定判据，用积分表示）。**两条路都通向同一个对象类，14I2 提供了"为什么半正定"的结构性解释。**

**标准解法骨架**
1. （12T1）对 $n$ 归纳：把最后一列减去第 $n$ 列（或对 $\frac1{a_i+b_j}$ 做部分分式），提出公因子 $\frac{a_i-a_n}{a_i+b_n}$ 与 $\frac{b_j-b_n}{a_j+b_n}$ 型因子。
2. 化为 $n-1$ 阶的 Cauchy 行列式，归纳完成。
3. （12T1）或用"行列式是 $a_i,b_j$ 的有理函数，两边极点与零点相同"的一般性论证。
4. （14I2(a)）$A_{ij}=t^{a_i}t^{a_j}=\langle t^{a_i},t^{a_j}\rangle_{L^2([0,1])}$ ⇒ 半正定；秩 $=$ 函数族 $\{t^{a_i}\}$ 的线性无关个数 $=$ 不同 $a_i$ 的个数。
5. （14I2(b)）$B_{ij}=\int_0^1t^{a_i}t^{a_j}dt=\frac1{1+a_i+a_j}$ ⇒ 同上半正定。
6. （14I2(c)）$B$ 正定 $\iff$ $\{t^{a_i}\}$ 线性无关 $\iff$ $a_i$ 互异（若 $a_i=a_j$ 则两行相同；若互异则 $\sum c_it^{a_i}=0$ 迫使所有 $c_i=0$，用 $t\to0^+$ 的最低次项论证）。

**最容易卡住的一步**：**第 4 步"$t^{a_i}$ 线性无关 ⟺ $a_i$ 互异"的论证**。对非整数指数的 $a_i$（题中只要求非负实数），不能直接用多项式次数；标准做法是把 $\sum c_it^{a_i}\equiv0$ 改写为 $c_{i_0}+\sum_{i\ne i_0}c_it^{a_i-a_{i_0}}\equiv0$（$a_{i_0}$ 最小），再令 $t\to0^+$，除最小指数项外全部趋于 0。

### ALG-M39 特征 p 的函数域与不可分扩张

**数学内核.** 特征 $p$ 的域扩张不再由"可分性"兜底：$X^p-a$（$a\notin k^p$）不可约但**纯不可分**，扩张 $k(\sqrt[p]a)/k$ 的 Galois 群平凡；由此产生两个现象：(i) 有限 Galois（要求可分）子扩张的"最小底域"问题需要 Artin–Schreier 型工具；(ii) 不可分多项式的商环会出现**幂零元**，取 $A_{\mathrm{red}}$ 就是剥掉不可分层的重叠部分。

**成员与差异**
- **19I2**：$F=\mathbb F_p(t)$，考察所有使 $F/C$ 有限 Galois 的子域 $C$。(1) 其中存在最小的 $C_0$（含于所有其它 $C$）；(2) $[F:C_0]=$？差别：**纯不可分背景下的 Galois 理论**；关键在于"有限 Galois 扩张族对交封闭"（$[F:C_1\cap C_2]\le[F:C_1][F:C_2]$），以及 $\mathbb F_p(t)$ 上有任意大的 Artin–Schreier 扩张 $\mathbb F_p(t)/\mathbb F_p(t^{p^n}-t)$。**注：本题答案依赖"Galois 是否要求可分"这一约定，本报告的母题归并不受其影响（见 §4）。**
- **24I3**：$k$ 是不完全域（imperfect），$\mathrm{char}\,k=p>0$，$a\in k\setminus k^p$。(1) $X^p-a$ 在 $k[X]$ 中不可约；(2) $A=k[X]/(X^{p^2}-aX^p)$，求 $A_{\mathrm{red}}$。差别：**不可分多项式的商环与幂零根**；关键是 $X^{p^2}-aX^p=X^p\big((X^{p-1})^p-a\big)$，$X^p$ 贡献幂零根，$A_{\mathrm{red}}=k[X]/\big((X^{p-1})^p-a\big)$。

**递进关系**：19I2（不可分背景下的 Galois 子扩张与最小底域）→ 24I3（不可分扩张的代数结构与幂零根）。**同一"特征 $p$ 不完全性"主线，一个走 Galois 方向、一个走交换代数方向。**

**标准解法骨架**
1. （24I3(1)）设 $\alpha$ 是 $X^p-a$ 的根，则 $X^p-a=(X-\alpha)^p$；若 $\alpha\in k$ 则 $a=\alpha^p\in k^p$，矛盾 ⇒ 无根 ⇒ 次数 $p$ 且不可约（$p$ 素数）；导数 $=0$ ⇒ 不可分。
2. （24I3(2)）写成 $X^{p^2}-aX^p=X^p\big(X^{p(p-1)}-a\big)=X^p\big((X^{p-1})^p-a\big)$。
3. 识别幂零根：$A=k[X]/(X^p\cdot g(X))$ 中 $X^p$ 类是幂零的，$\sqrt{(0)}=(X)$ 型 ⇒ $A_{\mathrm{red}}=k[X]/(g(X))=k[X]/\big((X^{p-1})^p-a\big)$。
4. 再判定 $A_{\mathrm{red}}$ 是否是域：$Y^p-a$（$Y=X^{p-1}$）在 $k$ 上不可约（第 1 步），故 $A_{\mathrm{red}}\supseteq k(Y)=k(\sqrt[p]a)$ 是纯不可分扩张；是否等于 $k(\sqrt[p]a)$ 取决于 $X^{p(p-1)}-a$ 是否不可约（Capelli 判据）。
5. （19I2(1)）有限 Galois 族对交封闭：$[F:C_1\cap C_2]\le[F:C_1][F:C_2]<\infty$，且交仍是 Galois 底域 ⇒ 存在最小元 $C_0$。
6. （19I2(2)）对每个 $n$，$\mathbb F_p(t)/\mathbb F_p(t^{p^n}-t)$ 是 $p^n$ 次 Galois（Artin–Schreier）⇒ $C_0$ 由这些底域的交给出（其"相对度"由所有有限 Galois 子群共同决定）。

**最容易卡住的一步**：**从 $X^p-a=(X-\alpha)^p$ 出发处理 $X^{p^2}-aX^p$**。很多人直接写 $X^{p^2}-aX^p=(X^p)^p-aX^p=(X^p)((X^p)^{p-1}-a)$ 就停了，没意识到幂零根来自 $X^p$ 这个因子、而"真正的域部分"是 $(X^{p-1})^p-a$。判断 $A_{\mathrm{red}}$ 是否等于 $k(\sqrt[p]a)$ 还需要一次 Capelli 判据。

### ALG-M40 线性群的拓扑：连通性与基本群

**数学内核.** 线性群既是代数对象也是拓扑对象：$GL_n(\mathbb C)$ 作为 $\mathbb C^{n^2}$ 中的开集（$\det\ne0$）是**道路连通**的（用 $\det$ 的连续性 + 极分解或 Jordan 形把任意 $A$ 连通到 $I$）；而 $SL_2(\mathbb R)$ 的基本群是 $\mathbb Z$（$SL_2(\mathbb R)\cong SO_2\times$（可缩空间）型分解或 Iwasawa 分解），其万有覆盖是无限叶的 Lie 群。

**成员与差异**
- **12T4**：计算 $SL_2(\mathbb R)$ 的基本群，并描述万有覆盖 $\widetilde{SL_2(\mathbb R)}\to SL_2(\mathbb R)$ 上的 Lie 群结构。差别：**基本群 + 覆盖群结构**，用 Iwasawa 分解 $SL_2(\mathbb R)=KAN$（$K=SO_2$，$A$ 对角正，$N$ 上三角幂零）或 $SL_2(\mathbb R)$ 作用在 $\mathcal H$ 上的纤维化。
- **19I4**：(1) 证 $GL_n(\mathbb C)$ 道路连通；(2) $X=\{A\in GL_n(\mathbb C):A^m=I\}$，描述其道路连通分支并证明。差别：**连通性与连通分支计数**，用"$A^m=I$ ⇒ $A$ 可对角化、特征值是 $m$ 次单位根"把 $X$ 分解为若干共轭类，每个连通分支由一个特征值重数分布决定。

**递进关系**：12T4（$SL_2(\mathbb R)$ 的基本群与万有覆盖，用实 Lie 群分解）→ 19I4（$GL_n(\mathbb C)$ 的连通性与 $\{A^m=I\}$ 的分支，用 Jordan 形 + 特征值连续性）。**同一条"线性群拓扑"主线，从实 Lie 群换到复线性群，从基本群换到连通分支。**

**标准解法骨架**
1. （19I4(1)）$GL_n(\mathbb C)$ 道路连通：对任意 $A$，用 $A=PU$（极分解，$P$ 正定 Hermite，$U$ 酉）或 Jordan 形；把 $P$ 沿正定矩阵的指数路径 $P^t=\exp(t\log P)$ 连通到 $I$，把 $U$ 沿 $U^t$ 连通到 $I$。
2. 更简单：$\mathbb C^\times$ 道路连通，用 $\det$ 的路径 $t\mapsto$ …… 或用 $A(t)$ 直接插值时绕开 $\det=0$。
3. （19I4(2)）$A^m=I$ ⇒ 极小多项式整除 $x^m-1$（无重根）⇒ $A$ 可对角化，特征值都是 $m$ 次单位根。
4. 按特征值的重数分布 $(n_1,\dots,n_m)$ 分类：每一类是一个 $GL_n(\mathbb C)$-轨道，本身连通（是 $GL_n$ 的连续像）。
5. 判定两个轨道何时在同一连通分支：$\zeta^j\mapsto\zeta^{jk}$ 型连续变形；最终连通分支由"特征值重数**按单位根的代数共轭类**分组"决定——即把 $\zeta$ 与 $\zeta^k$（$(k,m)=1$）视为同组。
6. （12T4）$SL_2(\mathbb R)$ 用 Iwasawa 分解 $SL_2(\mathbb R)=K\cdot A\cdot N$（$K=SO_2\cong S^1$，$A\cong\mathbb R_{>0}$，$N\cong\mathbb R$），$AN$ 可缩 ⇒ $SL_2(\mathbb R)\simeq S^1$ ⇒ $\pi_1=\mathbb Z$。
7. 万有覆盖 $\widetilde{SL_2(\mathbb R)}$：把 $K$ 换成 $\mathbb R$（$\theta$ 取任意实数），$\widetilde{SL_2(\mathbb R)}=\{(\theta,a,n)\}$ 型，群结构由 $SO_2$ 的覆盖与 $AN$ 的乘积给出（非平凡的中心扩张）。

**最容易卡住的一步**：**19I4(2) 的"连通分支按单位根共轭类分组"**。$\{A:A^m=I\}$ 作为集合是有限多个 $GL_n$-轨道的并，但两个轨道可以被一条连续路径连接——判据是特征值能否被 $\zeta\mapsto\zeta^k$（$(k,m)=1$）的连续变形互相转化。若两个轨道对应的重数分布在某个 $k$ 下互换，则它们在同一分支；否则不同。多数人只按"特征值重数分布"分类，会把分支数数多。

### ALG-M41 无限 Galois 理论与 profinite 群

**数学内核.** 无限 Galois 扩张的"子群 $\leftrightarrow$ 中间域"对应要求子群**闭**；与之对偶的是 profinite 群的**有限性条件**：拓扑有限生成 $\Rightarrow$ 每个指数 $n$ 的开子群只有有限多个（因为到 $S_n$ 的连续同态只有有限多个）；反过来 $\mathbb Q$ 的绝对 Galois 群 $G_{\mathbb Q}$ **不是**拓扑有限生成的（因为它有无限多个互不相同的指数 2 开子群，对应于 $\mathbb Q$ 的无限多个二次扩张）。对无限 Galois 扩张，"$x\in L$ 落在哪个中间域里"这类问题用**极大性论证 + Galois 闭包**解决。

**成员与差异**
- **17I3**：$L/F$ 是 Galois 扩张（不必有限），$x\in L$。(a) 不包含 $x$ 的子扩张集合 $\mathcal P$ 有极大元 $E$；若 $K/E$ 是 $L$ 中非平凡有限扩张，则 $x\in K$；(b) $K'$ 是 $K/E$ 在 $L$ 中的 Galois 闭包，则存在 $g\in\operatorname{Gal}(K'/E)$ 使 $gx\ne x$；(c) 推出 $K/E$ 是循环 Galois 扩张。差别：**无限 Galois 对应 + 极大性论证**，用 Zorn 引理找 $E$，再用 (b) 的"某个 Galois 元移动 $x$"逼出循环性。
- **23I3**：$G$ 是 profinite 群，拓扑有限生成。(1) 固定 $n$，$G$ 只有有限多个指数 $n$ 的开子群；(2) $K$ 是数域，其绝对 Galois 群 $G_K$ 不拓扑有限生成。差别：**profinite 群的有限性 + 数论应用**，用"连续同态 $G\to S_n$ 由生成元的像决定"与"$\mathbb Q$ 有无限多个二次扩张"。

**递进关系**：17I3（无限 Galois 扩张的中间域与极大性论证，结论是"某个有限子扩张循环"）→ 23I3（profinite 群的拓扑有限生成性，结论是"绝对 Galois 群太大了"）。**同一条"无限 Galois/profinite"主线，前者走子域结构，后者走有限性。**

**标准解法骨架**
1. （17I3(a)）取 $\mathcal P=\{$中间域 $\subseteq L$ 不含 $x\}$，用链的并封闭 + Zorn 引理得极大元 $E$。
2. 若 $K/E$ 是 $L$ 中非平凡有限扩张且 $x\notin K$，则 $K\in\mathcal P$，与 $E$ 的极大性矛盾 ⇒ $x\in K$。
3. (b) $K'$ 是 $K/E$ 在 $L$ 中的 Galois 闭包；$\operatorname{Gal}(K'/E)$ 有限。若所有 $g$ 都固定 $x$，则 $x\in$ 固定域 $=E$，与 $x\notin E$ 矛盾 ⇒ 存在 $g$ 使 $gx\ne x$。
4. (c) 用 (b) 得到的 $g$ 与 Galois 对应的子群结构推出 $\operatorname{Gal}(K/E)$ 循环：关键在于 $E$ 的极大性使得 $K/E$ 的极小多项式在 $E$ 上"不可再分"，从而 Galois 群必须是循环的（每个非平凡子域都含 $x$，用 (a) 逐个排除）。
5. （23I3(1)）指数 $n$ 的开子群 $H$ 对应连续满同态 $G\to G/H\hookrightarrow S_n$；这样的同态由 $n$ 个生成元的像决定，而 $S_n$ 有限 ⇒ 只有有限多个。
6. （23I3(2)）$\mathbb Q$ 有无限多个二次扩张 $\mathbb Q(\sqrt d)$ ⇒ $G_{\mathbb Q}$ 有无限多个指数 2 的开子群 ⇒ 若拓扑有限生成则与 (1) 矛盾。
7. 对一般数域 $K$：$K$ 也有无限多个二次扩张（Kummer/二次特征），同一论证。

**最容易卡住的一步**：**23I3(2) 的"数域有无限多个二次扩张"**。这需要构造：对任意有限集合 $S$ 的素数，取 $d$ 为它们的乘积（适当符号），则 $\mathbb Q(\sqrt d)$ 互不相同且都是 $\mathbb Q$ 的二次扩张——用"$\sqrt{d_1}\notin\mathbb Q(\sqrt{d_2})$"（可由 $\mathbb Q(\sqrt{d})$ 的唯一二次子域性质或范数论证）。把它正确地组织成"无限多个指数 2 子群"，是与 (1) 直接冲突的关键。

---

## §3 统计

### 3.1 总量与覆盖率

| 指标 | 数值 |
| --- | --- |
| 本科目题目总数 | 149（`subject == "Algebra & Number Theory"`，来源 `problems_full.json`，全库 757 题） |
| 归并出的母题数 | **41** |
| 母题—题目成员链接总数 | **116** |
| 被母题覆盖的**唯一**题目数 | **115**（116 − 1，因为 2010 team 6 是合并题面，同时计入 ALG-M02 与 ALG-M09） |
| **覆盖率** | **115 / 149 = 77.2%** |
| **孤题**（未进入任何多成员母题） | **34**（22.8%） |
| 平均每母题成员数 | 116 / 41 ≈ 2.83 |
| 成员数 ≥ 5 的"主干母题" | 4 个（ALG-M24、ALG-M06、ALG-M23、ALG-M02；ALG-M04 为 5 次） |
| 2021 年以来仍出现的活跃母题 | 21 个（休眠 20 个） |

**与"字符串查重"的对照**：本库中**逐字或近似逐字重复**的只有 4 组（2010 team 3 = 2014 team 2；2010 team 6 前半 = 2011 individual 6；2011 team 5 = 2012 team 2；2010 individual 6 与 2013 team 4 高度重叠）。也就是说，字符串查重能抓到的只有约 7 题；而按语义归并后，**115 题进入了 41 个母题**——这正是"必须人读"的价值所在。

### 3.2 孤题清单（34 题）

孤题 = 在全部 41 个母题中都找不到满足 S1 + S2 的伙伴。它们本身就是"冷门但可能回潮"的考点，值得单独建档。

| # | 出处 | 题目要点（一句话） | 备注（可能的潜在母题方向） |
| --- | --- | --- | --- |
| 1 | 10T1 | Beatty 定理：$\lfloor ax\rfloor,\lfloor bx\rfloor$（$1/a+1/b=1$）无重复地覆盖全部自然数 | 初等数论（floor 函数），唯一一次 |
| 2 | 10T2 | $X^n+Y^n=Z^n$ 在 $\mathbb C[t]$ 中的非平凡解 | Mason–Stothers（多项式 ABC），唯一一次 |
| 3 | 11I1 | 含 $\mathbb Q(\sqrt{-3})$ 的 Galois 扩张能否有群 $S_3,\mathbb Z/4,Q_8$ | 逆 Galois 问题（与 ALG-M26 有远亲关系，见 §4） |
| 4 | 11I3 | 实代数数域 $F$：是域；其唯一自同构是恒等 | 实闭域/序结构，唯一一次 |
| 5 | 11I5 | 五引理：两行正合、除中间外全为同构 ⇒ 中间也是同构 | 同调代数入门，唯一一次 |
| 6 | 11T1 | $\gcd(f,g)=1$ ⇒ $f=g=0$ 只有有限多个公共零点，可推广到多变量 | 弱 Nullstellensatz/Bezout，唯一一次 |
| 7 | 11T3 | $\mathbb Z[x,y]/(x^2-y^n)\cong\mathbb Z[x,y]/(x^2-y^m)$ 的 $n,m$ 分类 | 单项式理想的同构分类，唯一一次 |
| 8 | 12I1 | $x^6+30x^5-15x^3+6x-120$ 不能分解为两个正次数有理系数多项式之积 | 不可约性判定（Eisenstein 型），唯一一次 |
| 9 | 12I4 | 微分算子环 $D$ 作用在 $\mathbb R[x]$ 上：给定线性无关的 $b_i$ 与任意 $c_i$，存在 $D$ 使 $D(b_i)=c_i$ | $D$-模/插值，唯一一次 |
| 10 | 12I5 | 格 $\Lambda\subset\mathbb C$ 的自同态环 $R$；$(R/nR)^\times$ 的嵌入；$R^\times$ 的最大阶 | 虚二次序与单位（与 15T3 相邻，见 §4） |
| 11 | 12I6 | 加法子群 $A$：$A/2A$ 有限且局部有限 ⇒ $A$ 有限 $\mathbb Z$-秩 | 离散子群/2-进论证，唯一一次 |
| 12 | 12T5 | $f$ 不可约齐次，$P(n)=\dim\mathbb C[x,y,z]_n/f\mathbb C[x,y,z]_{n-d}$ 对充分大 $n$ 等于 $dn+c$ | Hilbert 函数/多项式，唯一一次 |
| 13 | 13T1 | 实反对称 $A$：特征值为纯虚或 0，$e^A$ 正交；$B=e^A$ 可解的充要条件 | 矩阵指数/正交群，唯一一次 |
| 14 | 14I4 | $G=S\times T$（$S,T$ 非交换有限单群）：正规子群共 4 个；极大子群与同构的互相判定 | 有限单群的结构，唯一一次 |
| 15 | 15I1 | 有限交换群 $G$ 带非退化交错配对 $\ell:G\times G\to\mathbb Q/\mathbb Z$ ⇒ $G\cong H_1\oplus H_2$（$H_1\cong H_2$，相互正交） | 双曲分解（与 16T4(c) 相邻，见 §4） |
| 16 | 15I4 | $\mathbb Z_p$ 上 $\varphi(x)=x^p+p\sum a_nx^n$，局部常值函数空间上 $\varphi^*$ 的特征值恰为 $\{0,1\}$ | $p$ 进动力系统/算子，唯一一次 |
| 17 | 15I5 | 判断 $\mathbb Z[\sqrt6]$、$\mathbb Z[(1+\sqrt{-11})/2]$、$\mathbb C[x,y]/(x^2+y^2-1)$、$\mathbb C[x,y]/(x^3+y^3-1)$ 是否 UFD | UFD 判定，唯一一次 |
| 18 | 15T5 | $\ker(A-\lambda)^\perp=(A^*-\bar\lambda)V$；$A$ 正规 $\iff$ 可酉对角化 | 正规矩阵谱定理，唯一一次（与 14I6 相邻，见 §4） |
| 19 | 16I1 | $\langle u_i,u_j\rangle\le0$ ⇒ 存在正交基 $u_i'$ 为 $u_1,\dots,u_i$ 的非负组合；对偶基的符号 | 正定型的组合构造，唯一一次 |
| 20 | 16I2 | $\mathbb Z^d$ 中指数 $n$ 的子群个数 $f_d(n)$、循环商个数 $g_d(n)$、乘性、$g_d(p^r)$、$f_2(20)$ | 子群计数/Hecke 型，唯一一次 |
| 21 | 16T1 | 求所有实正交 $2\times2$ 矩阵 $k$，使存在对角元正的上三角 $b$ 与 $kb$ 正定对称 | QR/极分解，唯一一次 |
| 22 | 17T1 | 群元 $g$ 的阶 $n=rs$（$(r,s)=1$）⇒ 唯一分解 $g=g_1g_2$（$g_1^r=g_2^s=1$） | 群中的中国剩余，唯一一次 |
| 23 | 17T3 | 李代数 $\mathfrak g$ 的秩 $\operatorname{rank}(\mathfrak g)=\min_x\dim\ker(\operatorname{ad}x)^{\dim\mathfrak g}$，$\{x:n(x)>\operatorname{rank}\}$ 是多项式零点集 | Lie 代数正则元，唯一一次 |
| 24 | 18I1 | $2^k-1$ 素 ⇒ $k$ 素；$2^k+1$ 素 ⇒ $k$ 是 2 的幂；Fermat 数两两互素 | 初等因式分解，唯一一次（见 §4） |
| 25 | 18I4 | $V$ 不是有限多个真子空间之并；Radon 变换可逆；由线性像的信息重构向量组 | 线性代数/组合几何，唯一一次 |
| 26 | 18I5 | $A^2=p^{n+1}I$、$v_p(a_{ij})\ge i$ ⇒ $v_p(a_{ij})\ge\max\{i,n+1-j\}$ 且反对角元取到 $p^iZ_p^\times$ | $p$ 进矩阵赋值（与 24I2 相邻，见 §4） |
| 27 | 18T5 | 满足"唯一不变子空间是 $\{0\}$"的 $f:W\to V$ 可延拓为 $\tilde f:V\to V$，特征多项式任意指定 | 线性算子的延拓构造，唯一一次 |
| 28 | 19I3 | $R\subset R'$ 整扩张，$\mathfrak p'$ 极大 $\iff\mathfrak p'\cap R$ 极大 | 整扩张/极大理想，唯一一次 |
| 29 | 19T1 | $S_n$ 中对合 $(1,n)(2,n-1)\cdots$ 的中心化子 $\cong S_{\lceil n/2\rceil}\ltimes(\mathbb Z/2)^{\lfloor n/2\rfloor}$ | 置换群的中心化子，唯一一次 |
| 30 | 19T3 | $R$ Noether，$I\subset R$，Rees 代数 $\operatorname{Rees}(I,R)=\bigoplus I^nt^n$ 是 Noether 环 | Rees 代数/Hilbert 基定理，唯一一次 |
| 31 | 20I2 | 有限生成模 + $\varphi(M)\subseteq\mathfrak aM$ ⇒ 存在首一多项式（行列式技巧）；$\mathfrak aM=M$ ⇒ $\exists x$：$1-x\in\mathfrak a,xM=0$（Nakayama） | Cayley–Hamilton/Nakayama，唯一一次（与 19T3 相邻，见 §4） |
| 32 | 22I3 | 直接构造 $\mathfrak{sl}(4,\mathbb C)\cong\mathfrak{so}(6,\mathbb C)$ 的同构（不用 Dynkin 图） | 典型李代数的例外同构，唯一一次 |
| 33 | 24I2 | 赋值环上的 Iwahori–Bruhat 型：$GL_n(A)D_\mu GL_n(A)\cap U(K)D_\lambda\ne\emptyset\iff\lambda_{\text{dom}}\le\mu_{\text{dom}}$ | 仿射 Grassmann 型分解，唯一一次（见 §4） |
| 34 | 25I3 | $R=k[T]_{(T)}$ 中 $\frac1{T-\alpha_i}$ 构成 $R/(T^n)$ 的基；$u_n/n\ge1/[K:k]$ | 插值/Pólya 型估计，唯一一次 |

### 3.3 主线分布

| 主线 | 母题 | 成员数 | 占比（116 链接） |
| --- | --- | --- | --- |
| 代数数论（数域、理想、整基、丢番图） | M18, M19, M20, M21, M22, M23, M25, M26, M39 | 24 | 20.7% |
| 有限群表示论与不变量 | M06, M07, M08, M09, M10 | 17 | 14.7% |
| 有限群结构与群论 | M02, M03, M04, M05 | 15 | 12.9% |
| 线性代数与矩阵结构 | M01, M33, M34, M35, M38 | 13 | 11.2% |
| Galois 理论 | M17, M24, M41 | 12 | 10.3% |
| p 进与局部域 | M11, M12, M13, M14 | 10 | 8.6% |
| 群作用 / Lie 群 / 正交群 | M27, M28, M40 | 8 | 6.9% |
| 组合与初等数论 | M32, M36, M37 | 7 | 6.0% |
| 有限域 | M15, M16, M29 | 6 | 5.2% |
| 模论与交换代数 | M30, M31 | 4 | 3.4% |

**读法**：代数数论 + Galois 理论合计 36 条链接（31%），是本科目的绝对重心；p 进/局部域 10 条（8.6%）并且**近年明显扩张**（2020、2021、2023、2024、2025、2026 都有）。

### 3.4 TOP 10 性价比母题

**打分口径**：$\text{score}=$ 出现次数 $+\ 2\times$（2021 年以来出现次数）。第一项衡量"历史稳定性"，第二项衡量"近年热度"。并列时依次按"出现次数多者优先""末现年份晚者优先"。

| 排名 | 母题 | 一句话价值 | 次数 | 近年次数 | score |
| --- | --- | --- | --- | --- | --- |
| 1 | **ALG-M24 显式多项式的分裂域、Galois 群与子域格** | 7 次、跨 2010–2025、2021/2025 仍在考；把"不可约性 + 判别式 + 实根数 + 传递群列表"四步练熟即可通吃 | 7 | 2 | **11** |
| 2 | **ALG-M23 分圆域、单位根与分圆多项式模 p** | 6 次且技术含量逐年加码（2024 已到"素理想分解 + 最短向量"）；$\Phi_n\bmod p$ 的因子个数 $=\varphi(n)/\mathrm{ord}_n(p)$ 是必备武器 | 6 | 2 | **10** |
| 3 | **ALG-M06 有限群表示论：不可约表示、特征标取值与忠实表示** | 7 次、覆盖 2010–2024；特征标的代数整数性与零点定理是"可做但易失分"的密集区 | 7 | 1 | **9** |
| 4 | **ALG-M26 二次扩张、平方类群与 $(\mathbb Z/2)^n$-Galois 扩张** | 虽只 3 次，但 **2021/2022/2025 三连出现**且难度阶梯清晰，是近年命题人明显偏爱的低门槛高回报题 | 3 | 3 | **9** |
| 5 | **ALG-M04 有限域上线性群：阶、Sylow、生成元与可解性** | 5 次、跨 2011–2023；$|GL_n(\mathbb F_q)|$、单位上三角 Sylow、初等矩阵生成与导出列可一次打包练完 | 5 | 1 | **7** |
| 6 | **ALG-M12 非阿基米德域的完备性与球完备性** | 2020/2021/2024 三次，全部集中在最近 5 年；"值群离散 $\iff$ 球完备"这一分界是拿分关键 | 3 | 2 | **7** |
| 7 | **ALG-M21 曲线坐标环与函数域的整闭包（正规化）** | 2020/2021/2024 三次；两步走（找参数 $t$ → 证整闭包恰好是 $F[t]$）可模板化 | 3 | 2 | **7** |
| 8 | **ALG-M02 有限群的阶数决定结构** | 6 次但**末现 2018**、已休眠 8 年；作为基本功必练，但按"近年趋势"加权后性价比下降 | 6 | 0 | **6** |
| 9 | **ALG-M13 局部域扩张：不分叉扩张与半线性 Galois 下降** | 只在 2025、2026 出现两次，但两年连考、且 2026 题有三问，属**最新热点**，值得优先补 | 2 | 2 | **6** |
| 10 | **ALG-M22 数域的判别式与整基** | 2022、2026（纯三次域 $a\bmod9$ 的二分）；"$\operatorname{disc}(a_1,\dots,a_n)=[O_K:\mathbb Z a_i]^2d_K$ 是充分条件"是通用钥匙 | 2 | 2 | **6** |

**并列第 11（同样 score = 6）**：ALG-M20（数域整数环中理想与元素的生成与互素，2022/2026）、ALG-M31（投射模、平坦模与有限表现，2022/2023）。若只取 10 条，可把 ALG-M02 与 ALG-M13 互换——取决于读者是"补基本功"还是"押近年热点"。

**读法提示**：score 高不等于"必须刷"，还取决于**单题工程量**。例如 ALG-M24 的单题（如 25I5 要算惯性子群、$A_5$、无分歧性）比 ALG-M26 的单题重得多；若以"单位时间得分"衡量，**ALG-M26、ALG-M16、ALG-M15、ALG-M05** 这类"一题一两个引理"的小母题性价比更高。

### 3.5 三条可直接执行的结论

1. **字符串查重在这套题库上确实无效**：真正逐字重复的只有 4 组、约 7 题；而语义上有 115 题落在 41 个母题里。以"母题"为单位备考，比以"题目"为单位节省约 60% 的题量。
2. **升级链是命题人的主要换题方式**：41 个母题里有 21 个（51%）可以被读成明确的升级链（同一骨架，每年加一条要求或换一个更一般的对象），只有 4 个是"原样重复/并列"。**备考时应当按"链"准备，即从最简版本一路做到最难版本，而不是按年份平铺。**
3. **近五年新增压力集中在三块**：非阿基米德拓扑（M12）、局部域 Galois 扩张与下降（M13/M11/M14）、以及代数数论的结构性定理（M20/M21/M22/M23/M39 合计 15 条链接）。而 2010–2018 的重心（有限群结构 M02、有限群表示 M06、矩阵结构 M01/M33–M35）已明显降温。

---

## §4 存疑：拿不准是否同一母题的配对

以下条目我**没有并入**母题（或并入了但在理由上有摇摆），逐条给出两种解释，供后续裁定。凡"已并入"的，JSON 中按并入处理；凡"未并入"的，两侧题目都留在孤题表里。

| # | 配对 | 解释 A（应视为同一母题） | 解释 B（应视为两个母题） | 本报告处理 |
| --- | --- | --- | --- | --- |
| 1 | **18I5**（$A^2=p^{n+1}I$、$v_p(a_{ij})\ge i$ ⇒ 赋值矩阵的形状）vs **24I2**（$GL_n(A)D_\mu GL_n(A)\cap U(K)D_\lambda$ 的 Iwahori–Bruhat 判据） | 都以"赋值环上矩阵的赋值形状"为唯一对象，都在问"哪些赋值型可以被允许"，S3 对象可替换成立（把 $\mathbb Z_p$ 换成一般 DVR 正是 24I2 的做法） | 骨架完全不同：18I5 是"用 $A^2=p^{n+1}I$ 与初等行变换逐步抬升赋值"的**显式计算**；24I2 是"双陪集与支配序"的**结构定理**，几乎无法互相代入 | **未并入**（各自孤题），见本条 |
| 2 | **15I1**（有限交换群 + 非退化交错配对 ⇒ 双曲分解）vs **16T4(c)**（不可分解表示上的不变正交/辛形式） | 都是"非退化双线性型的标准形/分类"，技术骨架都含"取极大全迷向子群 → 正交补 → 归纳" | 15I1 的对象是**有限交换群 + $\mathbb Q/\mathbb Z$-值配对**（纯群论）；16T4 的对象是**$G$-等变形式 + Fitting 引理**（表示论），后者的核心结论是"正交或辛"而非"双曲分解" | 16T4 归入 ALG-M10；15I1 保留为孤题 |
| 3 | **19I5**（Fibonacci mod $p$，Legendre 符号 + 范数映射）vs **26I2**（$y^2=x^3+1$ 的点数，Jacobi 和） | 同属"有限域上的乘法特征 + 计数"，且 26I2 用的是 19I5 的二次特征的推广（Legendre $\subset$ Jacobi），构成清晰的升级链 | 19I5 的技术核心是**范数映射与 Frobenius 的二次特征**（用 $\alpha^{p}=\beta$ 分情形）；26I2 的核心是 **Jacobi 和的模长估计**（$|J|=\sqrt p$），两者没有共同引理 | **已并入 ALG-M29**，但若严格按 S2，也可拆为两个单成员母题 |
| 4 | **19I2**（$\mathbb F_p(t)$ 的有限 Galois 子扩张与最小底域）vs **24I3**（不完全域上 $X^p-a$ 不可约、$A_{\mathrm{red}}$） | 都在"特征 $p$ 的不完全性"这一背景上，24I3 的 $X^p-a$ 不可约正是 19I2 中"纯不可分扩张不构成 Galois 扩张"的根源 | 一个走 **Galois 理论**（子域格/Zorn 引理），一个走 **交换代数**（商环的幂零根），骨架毫不相干 | **已并入 ALG-M39**，S2 上有保留 |
| 5 | **12T4**（$\pi_1(SL_2(\mathbb R))$ 与万有覆盖）vs **19I4**（$GL_n(\mathbb C)$ 道路连通 + $\{A^m=I\}$ 的分支） | 同属"线性群的拓扑"这一主线，都是"把一个 Lie 群的拓扑分解为已知空间的乘积" | 12T4 用 **Iwasawa 分解 + 覆盖空间理论**；19I4 用 **Jordan 形 + 特征值连续性**。二者连"拓扑不变量"都不同（$\pi_1$ vs $\pi_0$） | **已并入 ALG-M40**，S1 成立而 S2 勉强 |
| 6 | **15T3**（$\zeta=1+N\eta$ ⇒ $\zeta=1$）归入 **ALG-M23**（分圆域）是否恰当 | 该题唯一用到的实质事实是 $N_{\mathbb Q(\zeta_\ell)/\mathbb Q}(1-\zeta_\ell)=\ell$，这正是 22I5(b) 要求计算的对象，属于同一技术内核 | 题面完全不含"分圆域/分圆多项式"字样，只含"单位根 + 代数整数"，把它放进"分圆域"母题有点**按技巧归类而非按对象归类** | **已并入 ALG-M23**（理由：S2 完全命中，且是本主线最早的一次出现） |
| 7 | **12I5**（格 $\Lambda$ 的自同态环与 $R^\times$ 的最大阶）vs **15I5**（四个环的 UFD 判定） | 都以"代数整数环/序的算术性质"为对象（单位群、唯一分解性），属于"环的算术" | 12I5 的核心是**虚二次序的单位群结构与 $(R/nR)^\times$ 的嵌入**；15I5 的核心是**逐个环判断 UFD（含两条曲线坐标环）**，共同点仅是"都在算环" | **均未并入**（各自孤题） |
| 8 | **12I1**（$x^6+30x^5-15x^3+6x-120$ 不可约）vs **ALG-M32**（二项式系数与估值）或自成"不可约性判定"母题 | 若按"有理多项式不可约性判定"立母题，可把 12I1、22I1(a)（有理根定理）、22I6(b)、25I5(1) 全部收入 | 这四题的"不可约性"都只是各自大题的**第一步热身**，剥出来单独成题会破坏原题的完整性；且 12I1 的手法（Eisenstein 变形/模 $p$）与另三题（查有理根）不同 | **未**立"不可约性"母题；12I1 保留为孤题 |
| 9 | **19T3**（Rees 代数 Noether）vs **20I2**（行列式技巧 + Nakayama） | 都是"交换代数中的有限性/局部性工具"，都可以挂在"Noether 环上的有限生成模"这一主线下 | 19T3 证的是**分次环的 Noether 性**（Hilbert 基定理的变形）；20I2 证的是**Cayley–Hamilton 型整除关系与 Nakayama**。二者共用"有限生成"这一个词，无共同引理 | **均未并入**（各自孤题） |
| 10 | **16I1**（$\langle u_i,u_j\rangle\le0$ 的基 ⇒ 正交基为前若干个的非负组合）vs **16T1**（$kb$ 正定对称的 $2\times2$ 正交 $k$） | 同在 2016 年、同以"正定二次型的 Gram 矩阵"为对象 | 16I1 是**组合/正性论证**（类似于 Cartan 矩阵/Weitzenböck 型）；16T1 是 **QR/极分解**。骨架不同，且同年同卷别不等于同母题 | **均未并入**（各自孤题） |
| 11 | **16I5**（$|G|=2^nm$，有 $2^n$ 阶元 ⇒ 有 $m$ 阶正规子群）归入 **ALG-M02** 是否恰当 | 结论形态相同：给定 $|G|$ 的算术性质，判定/构造正规子群，是"阶决定结构" | 骨架完全不同：M02 其它成员用 **Sylow 计数**,16I5 用 **左乘符号同态 + 归纳**（Burnside 正规 $p$-补的初等版） | **已并入 ALG-M02**，在 §2 中已注明差异 |
| 12 | **11I1**（含 $\mathbb Q(\sqrt{-3})$ 的 Galois 扩张的群能否是 $S_3,\mathbb Z/4,Q_8$）vs **ALG-M26**（$[F^\times:F^{\times2}]>2$ $\iff$ $(\mathbb Z/2)^2$-Galois 扩张存在） | 两者都在问"给定有限群能否实现为 Galois 群"，2025 版给出了 Kummer 判据，2011 版给出了 $Q_8$ 的失败判据 | 11I1 的技术核心是**具体域的构造与 $Q_8$ 的结构障碍**（与四元数/嵌入问题有关），不是平方类群；把它并入 M26 会把"逆 Galois 问题"这一独立方向吞掉 | **未并入**；11I1 保留为孤题，但建议后续单独立"逆 Galois 问题"母题 |
| 13 | **19I2 的最终数值答案**（$[F:C_0]=$？） | 若"Galois"要求**可分**（主流定义），$C_0$ 由 Artin–Schreier 型扩张 $\mathbb F_p(t)/\mathbb F_p(t^{p^n}-t)$ 的交给出，$[F:C_0]$ 为无穷 | 若"Galois"只要求**正规**（含纯不可分），则 $\mathbb F_p(t)/\mathbb F_p(t^{p^n})$ 都是 Galois，$C_0$ 会发生改变 | **不影响归并**：本题与 24I3 同属 ALG-M39；此处只记录"答案依赖定义约定"，本报告不裁定 |

**最后一条方法学提醒**：本报告的 41 个母题是按"S1 + S2 同时成立"的保守口径给出的，因此 §3.2 的 34 道孤题里，有一部分（尤其 #1、#2、#12、#14、#15、#34）在更宽的口径下是可以相互配对的。**我选择不配对**，理由是：把它们硬凑在一起会让"母题"退化成"考点标签"，失去"按链备考"的指导价值。








