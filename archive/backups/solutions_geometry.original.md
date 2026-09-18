# 丘成桐大学生数学竞赛 · 几何与拓扑 (Geometry and Topology) 真题解题讲义

> **素材来源**：`data/problems_full.json`（757 道真题的结构化抽取，其中 Geometry & Topology 159 道）。
> **题面核对**：本讲义全部 10 道题的题面均已回到原始试卷 PDF 逐字核对（PDF 位于
> `sources/prelim`，抽取脚本见 `/check_pdfs*.py`）。
> 抽取文本对上下标有损（例如 `x2 + y2` 实为 $x^2+y^2$），凡此类处均已按 PDF 校正；
> PDF 原文中的拼写错误（如 2010 年卷的 `contsant`、`disctance`）原样保留并标注。
> **难度**为 1–5 的主观标度（1 最易，5 最难），依据是"竞赛考场上 25 分钟内能否完整写出证明"。

---

## 0. 选题说明

### 0.1 十道题的清单

| 编号 | 年份 | 卷别 | 题号 | 主题 | 难度 |
| --- | --- | --- | --- | --- | --- |
| 1 | 2010 | 个人卷 (`2010_GeometryTopology_indi`) | 3 | 覆盖空间与可定向性：$\mathbb{RP}^n$ | 2/5 |
| 2 | 2016 | 个人卷 (`2016_geometry2016_individual`) | 2 | de Rham 上同调、Stokes、恰当性障碍 | 2/5 |
| 3 | 2026 | 正卷 (`2026_2026_Geo_Topology`) | 1 | 高斯映射的 Jacobi 行列式与 $|K(p)|$ | 2/5 |
| 4 | 2010 | 个人卷 | 1 | 穿孔圆盘上的完备双曲度量与距离 | 3/5 |
| 5 | 2019 | 团体卷 (`2019_Geometry2019_team`) | 1 | 切丛 $TS^2$ 与非平凡性不变量 | 3/5 |
| 6 | 2022 | 正卷 (`2022_ExamPaper_2022_geometry_and_topology_22s`) | 5 | H-空间：Eckmann–Hilton 与 cup 积障碍 | 3/5 |
| 7 | 2013 | 个人卷 (`2013_geometry2013_individual`) | 6 | 极小曲面的 Gauss 映射是（反）共形 | 3/5 |
| 8 | 2011 | 个人卷 (`2011_3_GeomTop_Individual_2011`) | 5 | Bertrand 曲线与 Frenet 标架 | 4/5 |
| 9 | 2013 | 团体卷 (`2013_TeamProblems2013`) | 1 | 图补空间的基本群、van Kampen、Alexander 对偶 | 4/5 |
| 10 | 2018 | 个人卷 (`2018_geometry2018_individual`) | 6 | Synge 定理：偶维正曲率 $\Rightarrow$ 单连通 | 5/5 |

年份覆盖：**2010, 2011, 2013, 2016, 2018, 2019, 2022, 2026**，共 **8 个不同年份**，时间跨度 2010–2026
（其中 2010、2013 各取两题）。所有题目均**真实选自** `problems_full.json`，无自编题。

### 0.2 为什么挑这 10 道：骨架考点

几何与拓扑这一科目在丘赛里实际上横跨三大块，本讲义按"每一块都要有骨架题"挑选：

**(A) 代数拓扑 / 微分拓扑**（第 1、2、5、6、9、10 题）
- 覆盖空间、覆叠变换与定向（第 1 题）——这是"定向"这个概念的**唯一正确入口**；
- de Rham 理论的两个基本机制：同伦不变性（第 2 题）与 Stokes 定理（第 2 题第二问）；
- 向量丛与示性类（第 5 题）：用"零截面的自相交数/欧拉数"区分两个同伦等价的流形；
- 同伦论：H-空间、Eckmann–Hilton、cup 积障碍（第 6 题）——把"代数不变量挡几何存在性"这一手法讲透；
- van Kampen + Alexander 对偶 + 把柄体（第 9 题）：算补空间基本群的标准三段式；
- 变分与最短闭测地线、平行移动的 holonomy（第 10 题）：Synge 定理是"拓扑被曲率锁死"的典范。

**(B) 曲面论 / 子流形几何**（第 3、7、8 题）
- 高斯映射：局部面积比 = $|K|$（第 3 题），它的"升级版"就是极小曲面情形的保角性（第 7 题），
  两题合看即可打通"高斯曲率 = Gauss 映射的 Jacobi 行列式"这条主线；
- 经典曲线论：Frenet 标架、Bertrand 对（第 8 题），是"用 ODE 结构反推几何"的标准范式。

**(C) Riemann 几何 / 双曲几何**（第 4、10 题）
- Uniformization 的具体计算：把双曲距离算成一个具体数值（第 4 题）；
- 比较几何与刚性：Synge（第 10 题）。

三块的比例是 6 : 3 : 2（第 10 题同时计入 (A)(C)），与该科目 2010–2026 年真题的实际分布大致吻合：
159 道真题中，纯代数拓扑（同调、同伦、补空间、覆叠）约六成，经典曲面/曲线论约两成半，Riemann 几何约一成半。

### 0.3 难度分层

- **基础 3 道**（第 1、2、3 题）：结论经典、工具单一、计算量小，用来"校准手感"。
  它们的共同特征是——**只要想到正确的那个唯一工具，两分钟内就能收尾**（分别是覆叠变换判据、Stokes、Jacobi 行列式）。
- **中等 4 道**（第 4、5、6、7 题）：需要两步以上的结构判断（例如第 4 题要先认清"是哪一个双曲结构"，
  第 5 题要先造出不变量，第 6 题要先想清楚"用什么代数不变量挡"，第 7 题要先用 Weingarten 公式算 $dN$）。
- **偏难 3 道**（第 8、9、10 题）：第 8 题计算密集但有套路；第 9 题需要一条非平凡的拓扑引理；
  第 10 题（Synge）需要变分公式 + holonomy + 线性代数三段拼接，是十题中唯一"没有捷径"的题。

### 0.4 被放弃的题目（备查）

选题时排除了下列真题，原因记录如下（题号依 `problems_full.json` 的 `paper`+`n`）：

| 题号 | 年份/卷别 | 放弃原因 |
| --- | --- | --- |
| 2014 个人 2 | Bernstein 定理（极小图） | (a) 要求在**诱导度量**下的 Laplace 算子下验证 $K=\Delta\log(1+1/W)$，书写量极大；(b) 是真 Bernstein 定理，需要 Cheng–Yau / do Carmo–Peng 级别的工具，无法在讲义篇幅内**严格**给出。 |
| 2020 第 1 题 | $S^6$ 上的 6-形式与 Hopf 不变量 | (a)(b)(c) 可做，(d) 要求 Hopf 不变量为偶数的证明，属于 Hopf 不变量理论，超出手写讲义的严谨边界。 |
| 2021 第 1 题 | $P^{2n}$ 不能是紧流形边界 | 卷面上记号 $P^{n}$ **未定义**（按 $\mathbb{RP}^n$ 读才讲得通），存在歧义风险，故不选。 |
| 2023 第 4 题 | Leray–Hirsch 与旗流形 Euler 数 | 需要 Leray–Hirsch 定理、旗流形的胞腔分解与 Poincaré 多项式等一整套工具，篇幅性价比低。 |
| 2016 团体 6 | $S^{n+1}$ 中常数量曲率极小超曲面 $S=0$ 或 $S\ge n$ | 证明依赖 Simons 恒等式 $\Delta S=2|\nabla A|^2+2nS-2S^2$，只能"引理式"引用，与本讲义"每一步可验证"的定位冲突。 |
| 2013 个人 3 | 共轭点与 Sturm 比较 | 完全可解，但与第 10 题（同为 Jacobi 场/比较论证）主题重叠，为保证覆盖面而未选。 |
| 2012 个人 6 / 2012 团队 3 | 结构方程、Levi-Civita 唯一性 | 抽取文本中张量公式损伤较重（上下标、指标位置丢失），逐字校对成本高于其余候选题。 |

---

## 1. 【基础·2/5】2010 年 个人卷第 3 题 —— $\mathbb{RP}^n$ 可定向 ⟺ $n$ 为奇数

**出处**：2010 年 · Geometry and Topology · 个人卷（paper id `2010_GeometryTopology_indi`）· 第 3 题。

**题面**（**原文**；据 PDF 逐字核对，无公式损伤）：

> Prove that the real projective space $RP^n$ is orientable if and only if $n$ is odd.

**解答**

**第 1 步（引理：覆叠变换判据）.** 设 $p:\widetilde M\to M$ 是 $n$ 维连通流形 $M$ 的一个覆叠映射，$G$ 为其覆叠变换群。则

> $M$ 可定向 $\iff$ $G$ 中每个元素都保持 $\widetilde M$ 的定向。

*证明.* (⇒) 设 $\omega$ 是 $M$ 上处处非零的 $n$-形式（$M$ 定向即存在这样的形式）。令 $\widetilde\omega:=p^*\omega$。因 $p$ 是局部微分同胚，$\widetilde\omega$ 在 $\widetilde M$ 上处处非零。对 $\tau\in G$，
$$\tau^*\widetilde\omega=\tau^*p^*\omega=(p\circ\tau)^*\omega=p^*\omega=\widetilde\omega .$$
若 $\tau$ 反定向，则 $\tau^*\widetilde\omega=-\widetilde\omega$（因 $\widetilde\omega$ 处处非零，$\tau^*\widetilde\omega=f\cdot\widetilde\omega$，$f\in C^\infty$ 处处非零，而反定向给出 $f<0$ 于全空间）。与上式矛盾，故 $\tau$ 保定向。

(⇐) 设每个 $\tau\in G$ 都保持 $\widetilde M$ 的一个固定定向（$\widetilde M$ 可定向：任取一点处的定向沿道路传播即可，$\widetilde M$ 单连通故无单值性问题）。对 $x\in M$ 与 $\widetilde x\in p^{-1}(x)$，把 $T_{\widetilde x}\widetilde M$ 的定向经 $p_*$ 推前得到 $T_xM$ 的定向；若换 $\widetilde x'=\tau(\widetilde x)$，因 $\tau$ 保定向，推前结果相同，故良定义。局部上 $p$ 是微分同胚，故得到 $M$ 上处处非零的 $n$-形式。∎

**第 2 步（应用到射影空间）.** 设 $A:\mathbb R^{n+1}\to\mathbb R^{n+1}$，$A(x)=-x$，则 $A$ 限制为 $S^n$ 的对径映射，且 \(\mathbb{RP}^n=S^n/\langle A\rangle\)，商映射 $S^n\to\mathbb{RP}^n$ 是二重覆叠（$n\ge 2$ 时 $S^n$ 单连通，故它就是万有覆叠；$n=1$ 时 $S^1\to\mathbb{RP}^1$ 也是覆叠），覆叠变换群为 $\{1,A\}\cong\mathbb Z/2$。

因 $A$ 是线性映射 $-I_{n+1}$ 在 $S^n$ 上的限制，它在切空间上的微分同为 $-I_{n+1}$，于是
$$A \text{ 保定向}\iff \det(-I_{n+1})=(-1)^{n+1}>0\iff n\ \text{为奇数}.$$
由第 1 步引理，$\mathbb{RP}^n$ 可定向 $\iff$ $A$ 保定向 $\iff$ $n$ 为奇数。$\blacksquare$

**第 3 步（旁证，另一种算法）.** $\mathbb{RP}^n$ 有胞腔分解（每个维度一个胞腔 $e^k$，$k=0,1,\dots,n$），其胞腔链复形的边界映射为 $\partial_k=0$（$k$ 奇）与 $\partial_k=\times 2$（$k$ 偶，$k<n$），于是
$$H_n(\mathbb{RP}^n;\mathbb Z)=\begin{cases}\mathbb Z,& n\ \text{奇},\\ 0,& n\ \text{偶}.\end{cases}$$
而"闭连通 $n$-流形 $M$ 可定向 $\iff H_n(M;\mathbb Z)\cong\mathbb Z$"（不可定向时 $H_n(M;\mathbb Z)=0$，因 $H_n$ 由定向局部系数的截面给出），再次得到同一结论。

**本题考点/技巧（一句话）**：`M` 可定向 ⟺ 万有覆叠的每个覆叠变换保定向；再把 `\det(-I)=(-1)^{n+1}` 代进去。

**难度**：2/5。

**同类题出现年份**：
- 同一结论用不同工具重做：**2014 团队 2**（用"$M/G$ 可定向 ⟺ $M$ 可定向且 $G$ 保定向"同时证明 Möbius 带不可定向、$\mathbb{RP}^n$ 当且仅当 $n$ 奇可定向）；
- 同族障碍（示性类挡住"存在性"）：**2021 第 1 题(a)**（$\mathbb{RP}^{2n}$ 不能是紧流形的边界，Stiefel–Whitney 类 $w_{2n}\neq0$）、**2024 第 5 题 (ii)(iii)**（$S^n$ 上自由 $G$-作用与 $G\cong\mathbb Z_2$）、**2021 第 6 题**（$\mathbb R^n$ 中紧嵌入超曲面必可定向，用 Jordan–Brouwer 分离）；
- 射影空间邻近考点：**2012 团队 1**（$\mathbb{RP}^n$ 是 $n$ 维微分流形）、**2014 个人 6** 与 **2020 第 4 题(b)**（$\mathbb{RP}^3\cong T^1S^2\cong SO(3)$）。

---

## 2. 【基础·2/5】2016 年 个人卷第 2 题 —— 挖点环面的 de Rham 上同调

**出处**：2016 年 · Geometry and Topology · 个人卷（`2016_geometry2016_individual`）· 第 2 题。

**题面**（**原文**；据 PDF 逐字核对）：

> Compute the de Rham cohomology of a punctured two-dimensional torus $T^2-\{p\}$, where $p\in T^2$. If $T^2=\mathbb R^2/\mathbb Z^2$ with coordinates $(x,y)\in\mathbb R^2$, then is the volume form $\omega=dx\wedge dy$ exact?

**解答**

**第 1 步（伦型）.** 取 $T^2$ 的标准胞腔分解 $T^2=e^0\cup e^1_a\cup e^1_b\cup e^2$，并取 $p$ 位于开 2-胞腔 $e^2$ 的内部。则 $e^2\setminus\{p\}$ 同胚于开圆环 $S^1\times(0,1)$，它可沿自 $p$ 出发的径向射线形变收缩到 $\partial e^2$（即 1-骨架），且该收缩在 $e^2$ 之外取恒同，故给出整个空间的一个形变收缩：
$$T^2\setminus\{p\}\simeq S^1\vee S^1 .$$

**第 2 步（算出上同调）.** de Rham 上同调是同伦不变量（de Rham 定理的同伦不变性），故
$$H^0_{dR}(T^2\setminus\{p\})=\mathbb R,\qquad H^1_{dR}(T^2\setminus\{p\})\cong\mathbb R^2,\qquad H^k_{dR}=0\ (k\ge 2).$$
（$H^1\cong\mathbb R^2$：$H_1(S^1\vee S^1;\mathbb Z)=\mathbb Z^2$ 加 de Rham 定理；也可用 Poincaré–Lefschetz 对偶 $H^k(T^2\setminus\{p\})\cong H_{2-k}(T^2,\{p\})$：$H^0=\mathbb R$，$H^1\cong H_1(T^2)=\mathbb R^2$，$H^2\cong \widetilde H_0(T^2)=0$。两种算法一致。）

**第 3 步（$\omega$ 是否恰当：不恰当）.** 注意 $dx\wedge dy$ 在平移 $(x,y)\mapsto(x+m,y+n)$ 下不变，因此从 $\mathbb R^2$ 下降到 $T^2$ 上，是 $T^2$ 上处处非零的 2-形式。

设 $\omega=d\eta$ 对某 $\eta\in\Omega^1(T^2)$ 成立。$T^2$ 是闭的（$\partial T^2=\varnothing$）定向 2-流形，由 **Stokes 定理**
$$\int_{T^2}\omega=\int_{T^2}d\eta=\int_{\partial T^2}\eta=0 .$$
另一方面，用 $[0,1]^2$ 作为基本域直接计算：
$$\int_{T^2}dx\wedge dy=\int_0^1\!\!\int_0^1 dx\,dy=1\neq 0 .$$
矛盾，故 $\omega$ **不**恰当。（等价说法：$[\omega]\in H^2_{dR}(T^2)\cong\mathbb R$ 是基本类，非零。）

**第 4 步（第二层含义，题目真正想考的对比）.** 把 $\omega$ 限制到**挖点环面**上：因 $H^2_{dR}(T^2\setminus\{p\})=0$（第 2 步），$\omega|_{T^2\setminus\{p\}}$ 是**恰当的**！也就是说存在 $\eta\in\Omega^1(T^2\setminus\{p\})$ 使 $d\eta=\omega$，但 $\eta$ **不能扩张**成 $T^2$ 上的光滑 1-形式（否则 $\omega$ 在 $T^2$ 上恰当，与第 3 步矛盾）。这就是"被挖掉的点 $p$ 是 $\eta$ 的极点"的 de Rham 说法，也是本题两问的呼应。

> 读法说明：若"is $\omega$ exact"被理解为在 $T^2\setminus\{p\}$ 上问，答案是"是"；按卷面语境（先给出 $T^2=\mathbb R^2/\mathbb Z^2$ 再问 $\omega$），问的是 $T^2$ 上的恰当性，答案是"否"。两种读法本讲义都已给出。

**本题考点/技巧（一句话）**：先用形变收缩把空间换成 $S^1\vee S^1$，再用"恰当 ⟹ 在闭流形上积分为 0"（Stokes）一击否掉 $dx\wedge dy$。

**难度**：2/5。

**同类题出现年份**：**2011 团队 4**（Mayer–Vietoris 长正合列与连接同态 $H^k(U\cap V)\to H^{k+1}(U\cup V)$）、**2018 团队 3**（证明 $f\omega$ 对任何处处非零 $f$ 都不闭，其中 $\omega=x\,dy-y\,dx+dz$）、**2019 个人 1**（$\omega_{ij}=(dz_i-dz_j)/(z_i-z_j)$ 在 $\mathrm{Conf}_n$ 上给出非零上同调类）、**2023 第 5 题**（$\alpha,d\alpha\in L^1$ 时 $\int_{\mathbb R^n}d\alpha=0$）、**2016 个人 5**（$\mathrm{Ric}>0\Rightarrow H^1(M;\mathbb R)=0$）、**2020 第 1 题**（$S^6$ 上 $d\alpha=0$、$\int_{S^6}\alpha=1$ 的构造）。

---

## 3. 【基础·2/5】2026 年 第 1 题 —— 高斯映射的面积比就是 $|K(p)|$

**出处**：2026 年 · Geometry and Topology · 正卷（`2026_2026_Geo_Topology`）· 第 1 题。

**题面**（**原文**；据 PDF 逐字核对）：

> Let $S\subset\mathbb R^3$ be a smooth regular surface without boundary, and let $p\in S$. Let $\{A_\varepsilon\}_{\varepsilon>0}$ be a family of regions in $S$ such that each $A_\varepsilon$ contains $p$, has area $|A_\varepsilon|$, and shrinks to $\{p\}$ as $\varepsilon\to0$. Let $N:S\to S^2$ be the Gauss map. Show that $|K(p)|=\lim_{\varepsilon\to0}\dfrac{\mathrm{Area}(N(A_\varepsilon))}{\mathrm{Area}(A_\varepsilon)}$.

**先约定**："shrinks to $\{p\}$" 理解为：存在 $r(\varepsilon)\to0$ 使 $A_\varepsilon\subset B(p;r(\varepsilon))\cap S$，且 $|A_\varepsilon|>0$。这是本题唯一自然的读法。

**解答**

**第 1 步（局部参数化与 Jacobi 行列式）.** 取 p 附近的正则参数化 $\varphi:U\to S$，$\varphi(0)=p$，$U\subset\mathbb R^2$ 开圆盘，记 $\varphi_u,\varphi_v$ 为坐标切向量，$E=\langle\varphi_u,\varphi_u\rangle$，$F=\langle\varphi_u,\varphi_v\rangle$，$G=\langle\varphi_v,\varphi_v\rangle$。

**引理.** 对一切 $(u,v)\in U$，
$$(N\circ\varphi)_u\times(N\circ\varphi)_v=K(\varphi(u,v))\,\big(\varphi_u\times\varphi_v\big).$$

*证明.* 由 Weingarten 方程 $dN(X)=-S(X)$（$S$ 为形状算子，$S:=-dN$），有 $N_u=-S\varphi_u$，$N_v=-S\varphi_v$。先在切平面内取正交基 $e_1,e_2$ 使 $e_1\times e_2=n$，写 $Se_1=ae_1+be_2$，$Se_2=ce_1+de_2$，则
$$(Se_1)\times(Se_2)=(ae_1+be_2)\times(ce_1+de_2)=ad\,(e_1\times e_2)+bc\,(e_2\times e_1)=(ad-bc)(e_1\times e_2)=\det(S)(e_1\times e_2),$$
而 $X\mapsto SX$ 与 $a\times b$ 都是双线性的，故对任意 $a,b\in T_pS$ 有 $(Sa)\times(Sb)=\det(S)(a\times b)$。取 $a=\varphi_u,b=\varphi_v$ 并注意 $\det S=K$：
$$N_u\times N_v=(-S\varphi_u)\times(-S\varphi_v)=K\,(\varphi_u\times\varphi_v). \qed$$
（自检：单位球面 $N(x)=x$ 时 $N_u\times N_v=\varphi_u\times\varphi_v$，而 $K=1$ ✓；马鞍面 $z=xy$ 在原点 $N_x\times N_y=(0,0,-1)=-1\cdot(\varphi_u\times\varphi_v)$，而 $K=-1$ ✓。）

于是
$$\big|(N\circ\varphi)_u\times(N\circ\varphi)_v\big|=|K|\cdot|\varphi_u\times\varphi_v|=|K|\sqrt{EG-F^2}.$$

**第 2 步（面积公式给出的上界）.** 对任意区域 $A\subset\varphi(U)$，对映射 $N\circ\varphi$ 用**带重数的面积公式**：
$$\int_{\varphi^{-1}(A)}\big|(N\circ\varphi)_u\times(N\circ\varphi)_v\big|\,du\,dv=\int_{S^2}\#\big((N\circ\varphi)^{-1}(y)\cap\varphi^{-1}(A)\big)\,dy\ \ge\ \mathrm{Area}\big(N(A)\big).$$
（重数 $\ge1$ 于像点上、$\ge0$ 处处。）结合第 1 步得
$$\mathrm{Area}(N(A))\ \le\ \int_A|K|\,d\sigma,\qquad d\sigma=\sqrt{EG-F^2}\,du\,dv,$$
等号成立当且仅当 $N$ 在 $A$ 上单射（重数处处为 1）。

**第 3 步（分两种情形取极限）.**

*情形 (i)：$K(p)\neq0$.* 此时 $dN_p$ 可逆（$|\det dN_p|=|K(p)|\neq0$），由反函数定理存在 $p$ 的邻域 $V$ 使 $N|_V$ 是到其像的微分同胚，特别地**单射**。因 $A_\varepsilon$ 收缩到 $p$，当 $\varepsilon$ 充分小时 $A_\varepsilon\subset V$，故第 2 步取等号：
$$\frac{\mathrm{Area}(N(A_\varepsilon))}{\mathrm{Area}(A_\varepsilon)}=\frac{1}{|A_\varepsilon|}\int_{A_\varepsilon}|K|\,d\sigma=\text{$|K|$ 在 } A_\varepsilon \text{ 上关于面积测度的平均值}.$$
对任意 $\delta>0$，由 $K$ 的连续性取 $r>0$ 使 $B(p;r)$ 上 $\big||K|-|K(p)|\big|<\delta$；当 $A_\varepsilon\subset B(p;r)$ 时平均值的偏差 $<\delta$。故极限为 $|K(p)|$。

*情形 (ii)：$K(p)=0$.* 此时 $N$ 在 $p$ 处可能根本不是局部单射（例如 $z=x^3$ 型平点，$N$ 把一个邻域压到一条曲线上），下界无从谈起；但第 2 步的**上界**与 $K$ 的连续性已经够用：
$$0\ \le\ \frac{\mathrm{Area}(N(A_\varepsilon))}{\mathrm{Area}(A_\varepsilon)}\ \le\ \sup_{A_\varepsilon}|K|\ \xrightarrow[\varepsilon\to0]{}\ |K(p)|=0 .$$
由夹逼定理，极限为 $0=|K(p)|$ ✓。

两种情形合并即得 $|K(p)|=\lim_{\varepsilon\to0}\mathrm{Area}(N(A_\varepsilon))/\mathrm{Area}(A_\varepsilon)$。$\blacksquare$

> 常见错误：不加讨论地写 $\mathrm{Area}(N(A))=\int_A|K|d\sigma$。当 $N|_A$ 不是单射时该式不成立（折叠会损失面积），只有 $\le$ 方向无条件成立。本题的全部技术含量就在这个"单射 + 夹逼"的区分上。

**本题考点/技巧（一句话）**：高斯映射的 Jacobi 行列式恰为高斯曲率（Weingarten + $(Sa)\times(Sb)=\det S\,(a\times b)$），再用面积公式的重数不等式加连续性夹逼。

**难度**：2/5（若判分要求讨论 $K(p)=0$ 的退化情形，可记 3/5）。

**同类题出现年份**：**2013 个人 6**（同一恒等式的"极小曲面版" $N^*g_{S^2}=-K\,ds^2$，见第 7 题）、**2012 个人 5**（支撑函数 $p=x\cdot n$ 与 $\iint_M H\,dA+\iint_M pK\,dA=0$，同属"Gauss 映射换元"）、**2018 个人 4**（Crofton 公式 $\iint_{S^2}n(W)dW=4L$，同属"用测度换元算几何量"）、**2026 第 2 题**（Gauss–Bonnet 型刚性）、**2018 团队 5**（$\int_M|K|d\sigma\ge4\pi(1+g)$）。

---

## 4. 【中等·3/5】2010 年 个人卷第 1 题 —— 穿孔圆盘上的双曲距离

**出处**：2010 年 · Geometry and Topology · 个人卷（`2010_GeometryTopology_indi`）· 第 1 题。

**题面**（**据 PDF 校正**：原文有拼写错误 `contsant`/`disctance`，且上下标在抽取文本中丢失，此处按 PDF 页面校正）：

> Let $D^*=\{(x,y)\in\mathbb R^2\mid 0<x^2+y^2<1\}$ be the punctured unit disc in the Euclidean plane. Let $g$ be the complete Riemannian metric on $D^*$ with constant curvature $-1$. Find the distance under the metric between the points $(e^{-2\pi},0)$ and $(-e^{-\pi},0)$.

**答案**：$\;d=\operatorname{arccosh}\tfrac32=\ln\dfrac{3+\sqrt5}{2}\approx0.9624$。

**解答**

**第 1 步（认清是哪一个完备双曲度量）.** $D^*$ 带标准共形结构。由单值化定理（Poincaré–Koebe：每个共形类中含唯一的完备双曲度量）与 Killing–Hopf 定理（完备、单连通、常曲率 $-1$ 的曲面等距于双曲平面 $\mathbb H$），$D^*$ 上的这个度量有显式模型：
$$\mathbb H=\{w\in\mathbb C:\operatorname{Im}w>0\},\qquad ds_{\mathbb H}^2=\frac{du^2+dv^2}{v^2}\ (w=u+iv),$$
覆叠映射
$$\pi:\mathbb H\longrightarrow D^*,\qquad \pi(w)=e^{2\pi i w},$$
覆叠变换群为 $\langle T\rangle\cong\mathbb Z$，$T(w)=w+1$（因 $\pi(w+1)=\pi(w)$，且 $\mathbb H$ 单连通故 $\pi$ 就是万有覆叠）。把 $ds^2_{\mathbb H}$ 推前即得 $D^*$ 上完备、常曲率 $-1$ 的度量。

*为什么答案与 $g$ 的选取无关*：设 $g$ 满足题设。万有覆叠 $\mathbb H\to D^*$ 上取拉回度量 $\pi^*g$：覆叠的拉回度量仍完备（测地线可提升），且仍单连通、常曲率 $-1$，由 Killing–Hopf 它与 $ds^2_{\mathbb H}$ 等距；再由 $\pi$ 与该等距的相容性，$(D^*,g)$ 与推前度量等距。故距离唯一确定。
（**注意**：这里用到了"共形类固定"这一隐含前提。若只要求"完备 + 常曲率 $-1$"而不要求与标准共形结构相容，则环带上还存在"漏斗型"完备双曲度量，答案会不同——见第 12 节存疑清单第 2 条。）

**第 2 步（算出推前度量的显式形式）.** 由 $z=e^{2\pi iw}$ 得 $dz=2\pi i\,z\,dw$，即 $|dw|=\dfrac{|dz|}{2\pi|z|}$；又 $|z|=e^{-2\pi v}$，故 $v=\dfrac{-\ln|z|}{2\pi}$。于是
$$ds^2=\frac{|dw|^2}{v^2}=\frac{|dz|^2/(4\pi^2|z|^2)}{(\ln|z|)^2/(4\pi^2)}=\frac{|dz|^2}{|z|^2(\ln|z|)^2}.$$
*完备性自检*：令 $r=|z|=e^{-t}$，径向弧长微元为 $\dfrac{dr}{r|\ln r|}=\dfrac{dt}{t}$，在 $r\to0$（$t\to\infty$）与 $r\to1$（$t\to0$）两端均发散，端点都在无穷远 ⟹ 度量完备 ✓。

**第 3 步（把两点提升到 $\mathbb H$）.** 由 $|z|=e^{-2\pi v}$ 与 $\arg z=2\pi u$ 得
$$u=\frac{\arg z}{2\pi},\qquad v=\frac{-\ln|z|}{2\pi}.$$
- $A=(e^{-2\pi},0)$：$|z|=e^{-2\pi}\Rightarrow v=1$；$\arg z=0\Rightarrow u=0$。取提升 $w_A=i$。
- $B=(-e^{-\pi},0)$：$|z|=e^{-\pi}\Rightarrow v=\tfrac12$；$\arg z=\pi\Rightarrow u=\tfrac12$。取提升 $w_B=\tfrac12+\tfrac i2$。

（不同提升相差平移 $w\mapsto w+k$，$k\in\mathbb Z$，给出同一距离 ✓。）

**第 4 步（用双曲平面距离公式收尾）.** 对 $w_1,w_2\in\mathbb H$，
$$\cosh d(w_1,w_2)=1+\frac{|w_1-w_2|^2}{2\operatorname{Im}w_1\cdot\operatorname{Im}w_2}.$$
代入 $|w_A-w_B|^2=\left(\tfrac12\right)^2+\left(\tfrac12\right)^2=\tfrac12$，$\operatorname{Im}w_A=1$，$\operatorname{Im}w_B=\tfrac12$：
$$\cosh d=1+\frac{1/2}{2\cdot1\cdot\frac12}=1+\frac12=\frac32,\qquad
d=\operatorname{arccosh}\frac32=\ln\left(\frac32+\sqrt{\frac94-1}\right)=\ln\frac{3+\sqrt5}{2}\approx0.9624 .$$

**自检**：同在实轴上的 $(e^{-2\pi},0)$ 与 $(e^{-\pi},0)$ 对应 $w=i$ 与 $w=\tfrac i2$，距离 $=\operatorname{arccosh}\left(1+\tfrac14\right)=\ln2$，与直接积分 $\int_{e^{-\pi}}^{e^{-2\pi}}\frac{dr}{r|\ln r|}=\ln2$ 完全一致 ✓；本题两点夹角为 $\pi$，距离增大到 $0.9624$ ✓ 合理。

**本题考点/技巧（一句话）**：先用单值化把"完备常曲率 $-1$"认成 $\mathbb H/\langle z\mapsto z+1\rangle$，再用 $z=e^{2\pi iw}$ 把两点提升到 $\mathbb H$ 并套 $\cosh$ 距离公式。

**难度**：3/5。

**同类题出现年份**：**2014 团队 5**（$(\mathbb R^2_+,(dx^2+dy^2)/y^k)$ 何时完备？答 $k\ge2$，同为"径向积分判端点是否在无穷远"）、**2021 第 4 题**（$\mathbb H^3$ 中平面 $z=x\tan\alpha$ 的平均曲率）、**2022 第 2 题**（$\sec\le-1$ 时极小曲面面积 $\le4\pi(g-1)$，双曲比较几何）、**2010 团队 1**（球极投影的保角性与 $S^n$ 的标准度量）、**2010 团队 2**（$\mathbb R^2$ 上 $\Delta f\ge0$ 且上有界 ⟹ 无最大值点）。

---

## 5. 【中等·3/5】2019 年 团体卷第 1 题 —— $TS^2$ 与 $S^2\times\mathbb R^2$ 是否微分同胚

**出处**：2019 年 · Geometry and Topology · 团体卷（`2019_Geometry2019_team`）· 第 1 题（**原文**：题面据原始 TeX 源 `Geometry2019-team.tex` 第 66 行逐字核对）。

**题面**（**原文**；据原始 TeX 源逐字核对）：

> Is $TS^2$ diffeomorphic to $S^2\times\mathbb R^2$? Verify your answer. Here $TS^2$ is the total space of the tangent bundle of $S^2$.

**答案**：不微分同胚（实际上连拓扑都不同）。

**解答**

**第 1 步（两个事实）.**

*(1) $TS^2$ 中零截面的法欧拉数 = 2.* 零截面 $Z=\{(x,0):x\in S^2\}\subset TS^2$ 是嵌入的 2-球面，其法丛就是 $TS^2$ 本身（沿零截面，总空间的切丛分裂为 $TZ\oplus\nu$，而 $\nu\cong TS^2$ ✓）。于是 ($Z$ 在 $TS^2$ 中的自相交数) $=e(\nu)=e(TS^2)=\chi(S^2)=2$ ✓。（一般原理：截面的自相交数等于该向量丛的欧拉数。）

*(2) $S^2\times\mathbb R^2$ 中任何紧嵌入 2-球面的法欧拉数都是 0.* 记该 4-流形为 $X=S^2\times\mathbb R^2$。由同伦等价 $X\simeq S^2$ 得 $H_2(X;\mathbb Z)\cong\mathbb Z$，由 $S^2\times\{0\}$ 生成。设 $\Sigma\subset X$ 紧嵌入 2-球面，则 $[\Sigma]=n\,[S^2\times\{0\}]$ 对某 $n\in\mathbb Z$。用交积（先把 $\Sigma$ 同痕推离自身，或直接用紧支撑同调上的交积，均良定义）：
$$e(\nu(\Sigma))=[\Sigma]\cdot[\Sigma]=n^2\big([S^2\times\{0\}]\cdot[S^2\times\{0\}]\big)=n^2\cdot0=0,$$
最后一步因为 $S^2\times\{0\}$ 可同痕移到与之不交的 $S^2\times\{1\}$，自相交数为 0 ✓。

**第 2 步（法欧拉数是微分同胚不变量）.** 设 $\Phi:S^2\times\mathbb R^2\to TS^2$ 是微分同胚，令 $\Sigma:=\Phi(Z)$。$\Sigma$ 是 $X$ 中的紧嵌入 2-球面。微分同胚把管状邻域映成管状邻域，从而把法丛同构地映过去：
$$\nu(\Sigma)\ \cong\ \nu(Z)\ \cong\ TS^2\quad\Longrightarrow\quad e(\nu(\Sigma))=e(TS^2)=2 .$$
但第 1 步 (2) 给出 $e(\nu(\Sigma))=0$。矛盾（$2\neq0$）⟹ 这样的微分同胚不存在。$\blacksquare$

**第 3 步（旁证：端的 $\pi_1$）.** $TS^2$ 去掉一个紧核心后剩下单位切丛 $T^1S^2\cong\mathbb{RP}^3$，$\pi_1=\mathbb Z/2$；$S^2\times\mathbb R^2$ 去掉紧核心后剩下 $S^2\times S^1$，$\pi_1=\mathbb Z$。流形的"端"的 $\pi_1$（$\varprojlim\pi_1(\text{补紧集})$）是同胚不变量，而 $\mathbb Z/2\not\cong\mathbb Z$，故二者连拓扑都不同 ✓。（此条用到 Siebenmann 端理论，仅作旁证；正式解答用第 1、2 步。）

**第 4 步（为什么直觉会骗人）.** 二者**同伦等价**（$TS^2\simeq S^2\simeq S^2\times\mathbb R^2$），同调群、同伦群、可定向性、甚至"是否可平行化"（作为非紧 4-流形二者都可平行化）全都一致。真正的区别是零截面的自相交数，它属于**纤维丛层面**而非伦型层面的信息——这正是"示性类"存在的理由。

**本题考点/技巧（一句话）**：用"零截面的自相交数 = 欧拉数"造一个微分同胚不变量，再算出它在 $S^2\times\mathbb R^2$ 中必为 0 而在 $TS^2$ 中为 2。

**难度**：3/5。

**同类题出现年份**：**2015 个人 1**（$S^n\times S^m$ 切丛平凡 ⟺ $n$ 或 $m$ 为奇，同样是"偶维球面 $\chi\neq0$"挡路）、**2025 第 1 题**（$S^{2n}\times S^{2n}$ 与 $S^{2n}\times S^{2n-1}$ 的切丛是否平凡）、**2018 个人 3**（分类 $S^1$ 上向量丛）、**2014 个人 6**（$T^1S^2\cong\mathbb{RP}^3$）、**2020 第 4 题(b)**（$SO(3)\cong\mathbb{RP}^3$ 吗）、**2026 第 4 题(1)**（$TS^{2026}$ 的 $\mathbb Z_2$ 欧拉类）、**2025 第 4 题**（$\mathbb{CP}^2$ 不能浸入 $\mathbb R^6$）。

---

## 6. 【中等·3/5】2022 年 第 5 题 —— H-空间：$\pi_1$ 交换与 $S^{2022}$ 不是 H-空间

**出处**：2022 年 · Geometry and Topology · 正卷（`2022_ExamPaper_2022_geometry_and_topology_22s`）· 第 5 题。

**题面**（**原文**；据 PDF 逐字核对）：

> A topological space $X$ is called an H-space if there exist $e\in X$ and $\mu:X\times X\to X$ such that $\mu(e,e)=e$ and the maps $x\to\mu(e,x)$ and $x\to\mu(x,e)$ are both homotopic to the identity map.
> **(a)** Show that the fundamental group of an H-space is Abelian.
> **(b)** Show that the sphere $S^{2022}$ is not an H-space.

**解答 (a)：$\pi_1$ 交换**

不妨设 $X$ 道路连通（只涉及 $e$ 所在的道路连通分支）。记 $\pi_1(X,e)$ 的群运算为 $\cdot$（道路类的连接）。

定义第二个运算
$$\ast:\ \pi_1(X,e)\times\pi_1(X,e)\longrightarrow\pi_1(X,e),\qquad
a\ast b:=\mu_*\big(a\times b\big),$$
其中 $a\times b\in\pi_1(X\times X,(e,e))$ 是 $t\mapsto(a(t),b(t))$ 的道路类，并用到了标准同构 $\pi_1(X\times X,(e,e))\cong\pi_1(X,e)\times\pi_1(X,e)$。因 $\mu(e,e)=e$，$\ast$ 良定义 ✓。

**互换律.** 对任意 $a,b,c,d\in\pi_1(X,e)$，
$$(a\ast c)\cdot(b\ast d)=\mu_*(a\times c)\cdot\mu_*(b\times d)
=\mu_*\big((a\times c)\cdot(b\times d)\big)
=\mu_*\big((a\cdot b)\times(c\cdot d)\big)=(a\cdot b)\ast(c\cdot d),$$
第二个等号用了 $\mu_*$ 是群同态，第三个等号用了"乘积空间中的连接是逐分量连接"：$(a\times c)\cdot(b\times d)=(a\cdot b)\times(c\cdot d)$ ✓。

**关键一步.** 令 $i_1(x)=(x,e)$、$i_2(x)=(e,x)$，并记
$$\varphi:=(\mu\circ i_1)_*,\qquad \psi:=(\mu\circ i_2)_*.$$
由定义 $a\ast b=\varphi(a)\cdot\psi(b)$ ✓。又 $\mu\circ i_1\simeq\mathrm{id}$、$\mu\circ i_2\simeq\mathrm{id}$（都是同伦等价），故 $\varphi,\psi$ 都是 $\pi_1(X,e)$ 的自同构，特别地
$$\mathrm{im}\,\varphi=\mathrm{im}\,\psi=\pi_1(X,e).$$
在互换律中取 $a=1$（群的单位元）、$d=1$：
$$(1\ast c)\cdot(b\ast 1)=(1\cdot b)\ast(c\cdot 1)\;\Longrightarrow\;\psi(c)\cdot\varphi(b)=\varphi(b)\cdot\psi(c).$$
（右端 $b\ast c=\varphi(b)\psi(c)$ ✓。）于是 $\mathrm{im}\,\psi$ 的每个元素与 $\mathrm{im}\,\varphi$ 的每个元素交换，而两个像都是整个群，故 $\pi_1(X,e)$ 交换 ✓。$\blacksquare$

> 注：本题**不需要** $e$ 是严格单位（题面只给同伦意义下的单位）。上面的写法用"互换律 + 两个自同构的像"取代了经典 Eckmann–Hilton"公共严格单位元"的论证，因此对题面的弱假设也适用。

**解答 (b)：$S^{2022}$ 不是 H-空间**

记 $n=2022$（偶数，$n>0$）。反设 $S^n$ 是 H-空间，取乘法 $\mu:S^n\times S^n\to S^n$ 与单位 $e$。

**第 1 步（$\mu^*$ 在 $H^n$ 上的形状）.** 取生成元 $\alpha\in H^n(S^n;\mathbb Z)\cong\mathbb Z$。由 Künneth 公式（$H^*(S^n)$ 无挠 ✓）
$$H^n(S^n\times S^n;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z,\qquad\text{基为 }\ \alpha\otimes1,\ 1\otimes\alpha .$$
故存在整数 $a,b$ 使
$$\mu^*(\alpha)=a\,(\alpha\otimes1)+b\,(1\otimes\alpha).$$
取 $i_1(x)=(x,e)$。由 $\mu\circ i_1\simeq\mathrm{id}$ 得 $\alpha=(\mu\circ i_1)^*\alpha=i_1^*\mu^*\alpha$。而 $i_1^*(\alpha\otimes1)=\alpha$（第一投影 ✓），$i_1^*(1\otimes\alpha)=(\mathrm{pr}_2\circ i_1)^*\alpha=(\text{常值映射 }x\mapsto e)^*\alpha=0$（因 $n>0$ ✓）。故 $\alpha=a\alpha$，即 $a=1$；同理（用 $i_2$）得 $b=1$。于是
$$\mu^*(\alpha)=\alpha\otimes1+1\otimes\alpha .$$

**第 2 步（cup 积给出矛盾）.** 因 $2n>n$，$H^{2n}(S^n;\mathbb Z)=0$，故 $\alpha\cup\alpha=0$，从而
$$0=\mu^*(\alpha\cup\alpha)=\mu^*(\alpha)\cup\mu^*(\alpha)=(\alpha\otimes1+1\otimes\alpha)^2 .$$
用 Künneth 的符号规则 $(x\otimes x')\cup(y\otimes y')=(-1)^{|x'||y|}(x\cup y)\otimes(x'\cup y')$ 逐项展开：
$$(\alpha\otimes1)^2=0,\qquad(1\otimes\alpha)^2=0,$$
$$(\alpha\otimes1)(1\otimes\alpha)=\alpha\otimes\alpha,\qquad
(1\otimes\alpha)(\alpha\otimes1)=(-1)^{n\cdot n}\,\alpha\otimes\alpha=\alpha\otimes\alpha\quad(n\ \text{为偶}).$$
故
$$0=2\,(\alpha\otimes\alpha)\in H^{2n}(S^n\times S^n;\mathbb Z)\cong\mathbb Z\langle\alpha\otimes\alpha\rangle .$$
但 $2\neq0$ 于 $\mathbb Z$ 中，矛盾 ✓。故 $S^{2022}$ 不是 H-空间。$\blacksquare$

**为什么必须是偶维**：若 $n$ 为奇数，则 $(1\otimes\alpha)(\alpha\otimes1)=(-1)^{n^2}\alpha\otimes\alpha=-\alpha\otimes\alpha$，两项相消，第 2 步得不到矛盾——这与 $S^1,S^3,S^7$ 确实是 H-空间（$\mathbb C,\mathbb H,\mathbb O$ 的单位球）相符 ✓。完整分类（$S^n$ 是 H-空间 $\iff n\in\{1,3,7\}$）即 Adams 的 Hopf 不变量一（深度定理，本讲义不证）。

**本题考点/技巧（一句话）**：H-空间的乘法在 $\pi_1$ 上诱导出第二个满足互换律的乘法 ⟹ Eckmann–Hilton；在球面上则用 $\mu^*(\alpha)=\alpha\otimes1+1\otimes\alpha$ 配合 $\alpha^2=0$ 与 Künneth 的符号规则，制造 $2\alpha\otimes\alpha\neq0$ 的矛盾。

**难度**：3/5。

**同类题出现年份**：**2018 个人 2**（$S^2\to S^1\times S^1$ 的所有可能度数为 0）、**2017 个人 2**（$(S^2\vee S^2)\cup_f D^3$ 的整同调由 $d_1,d_2$ 决定）、**2012 团队 4**（$\deg f$ 为奇数 ⟹ $\exists x_0,\ f(-x_0)=-f(x_0)$，Borsuk–Ulam 型）、**2010 团队 6**（度的良定义与实现）、**2024 第 1 题**（$S^{2n}\to\mathbb{CP}^n$ 与 $\mathbb{CP}^n\to S^{2n}$ 是否存在非零度映射）、**2020 第 1 题**（Hopf 纤维化 $S^{11}\to S^6$ 与 Hopf 不变量的整性/偶性）。

---

## 7. 【中等·3/5】2013 年 个人卷第 6 题 —— 极小曲面的度量 $-K\,ds^2$ 曲率恒为 1

**出处**：2013 年 · Geometry and Topology · 个人卷（`2013_geometry2013_individual`）· 第 6 题。

**题面**（**据 PDF 校正**；抽取文本把 $\widetilde K$ 打成 `eK`、$\widetilde{ds^2}$ 打成 `f ds2`，此处已按 PDF 页面校正）：

> Let $(M^2,ds^2)$ be a minimal surface in $\mathbb R^3$, where $ds^2$ is the restriction of the Euclidean metric. Assume that the Gaussian curvature $K$ of $(M^2,ds^2)$ is negative. Denote by $\widetilde K$ the Gaussian curvature of the metric $\widetilde{ds^2}=-K\,ds^2$. Show that $\widetilde K=1$.

**解答**

**第 1 步（主方向标架下的极小性）.** 取一点 $p\in M$ 与单位正交主方向 $e_1,e_2\in T_pM$，对应主曲率 $\kappa_1,\kappa_2$。极小性 $H=\tfrac12(\kappa_1+\kappa_2)=0$ 给出
$$\kappa_2=-\kappa_1=:\kappa,\qquad K=\kappa_1\kappa_2=-\kappa^2<0 .$$
（$K<0$ 与题设一致，且 $\kappa\neq0$，即 $dN_p$ 可逆——下文要用。）

**第 2 步（高斯映射的拉回度量）.** 设 $N:M\to S^2$ 为高斯映射，$S:=-dN$ 为形状算子（此时 $\det S=K$，主曲率是 $S$ 的特征值）。由 Weingarten 方程 $dN(e_i)=-S(e_i)=-\kappa_i e_i$，取对偶余标架 $\{\theta^1,\theta^2\}$（$\theta^i(e_j)=\delta^i_j$），则
$$\big(N^*g_{S^2}\big)(e_i,e_j)=\langle dN(e_i),dN(e_j)\rangle=\kappa_i\kappa_j\,\delta_{ij},$$
即
$$N^*g_{S^2}=\kappa_1^2\,\theta^1\otimes\theta^1+\kappa_2^2\,\theta^2\otimes\theta^2
=\kappa^2\big((\theta^1)^2+(\theta^2)^2\big)=\kappa^2\,ds^2=-K\,ds^2,$$
最后一步用了 $K=-\kappa^2$，而 $ds^2=(\theta^1)^2+(\theta^2)^2$ 是诱导度量 ✓。

**第 3 步（局部等距）.** 由 $K<0$ 知 $-K\,ds^2$ 正定，故 $\widetilde{ds^2}:=-K\,ds^2$ 是 $M$ 上的 Riemann 度量。第 2 步说明
$$N^*g_{S^2}=\widetilde{ds^2},$$
即 $N:(M,\widetilde{ds^2})\to(S^2,g_{S^2})$ 是**局部等距**（$N^*g$ 正定 ⟹ $N$ 是浸入；由反函数定理，$N$ 在每点附近是到其像的微分同胚 ✓）。

**第 4 步（局部等距保曲率）.** 高斯曲率是度量的局部等距不变量（在局部坐标下由 $E,F,G$ 及其一、二阶导数完全决定；也可由 Gauss 方程或结构方程直接看出）。故
$$\widetilde K=K_{S^2}=1 .\qquad\blacksquare$$

**补充（这条恒等式的一般含义）.** $N^*g_{S^2}=-K\,ds^2$ 正是"极小曲面的高斯映射（反）共形"的精确表述，而且保角因子恒为 1——即 $N$ 在这里是等距而非仅仅共形。当 $K>0$ 时 $-K\,ds^2$ 负定，需把 $S^2$ 反向定向（或改看 $-N$），结论相应地变成 $\widetilde K=-1$；本题的 $K<0$ 恰使 $-K\,ds^2$ 正定，这正是命题能这样陈述的原因。

**本题考点/技巧（一句话）**：极小性使两个主曲率互为相反数，于是 $N^*g_{S^2}=\kappa^2 ds^2=-K\,ds^2$——度量 $-K ds^2$ 无非就是把高斯映射当等距用。

**难度**：3/5。

**同类题出现年份**：**2026 第 1 题**（同一恒等式的"面积/一阶"版本 $|K(p)|=\lim\mathrm{Area}(N(A_\varepsilon))/\mathrm{Area}(A_\varepsilon)$，见第 3 题）、**2014 个人 2**（极小图的 $K$ 表达式与 Bernstein 定理）、**2014 个人 5**（$\int_M H^2d\sigma\ge4\pi$）、**2011 个人 6**（管状曲面 $\int H^2d\sigma\ge2\pi^2$ 及等号刻画）、**2016 个人 3**（$H_r\equiv\mathrm{const}$ 且 $\lambda_i>0$ ⟹ 超球面）、**2016 个人 6**（极小超曲面第一特征值 $\lambda_1\ge n/2$）、**2016 团队 6**（$S^{n+1}$ 中常数量曲率极小超曲面 $S=0$ 或 $S\ge n$）、**2017 个人 6 / 2017 团队 5 / 2018 个人 5 / 2018 团队 5 / 2022 第 2 题 / 2022 第 6 题 / 2024 第 2 题 / 2025 第 4 题**（极小曲面簇）。

---

## 8. 【偏难·4/5】2011 年 个人卷第 5 题 —— Bertrand 曲线

**出处**：2011 年 · Geometry and Topology · 个人卷（`2011_3_GeomTop_Individual_2011`）· 第 5 题。

**题面**（**原文**；据 PDF 逐字核对）：

> A regular curve $C$ in $\mathbb R^3$ is called a Bertrand Curve, if there exists a diffeomorphism $f:C\to D$ from $C$ onto a different regular curve $D$ in $\mathbb R^3$ such that $N_xC=N_{f(x)}D$ for any $x\in C$. Here $N_xC$ denotes the principal normal line of the curve $C$ passing through $x$, and $T_xC$ will denote the tangent line of $C$ at $x$. Prove that:
> **a)** The distance $|x-f(x)|$ is constant for $x\in C$; and the angle made between the directions of the two tangent lines $T_xC$ and $T_{f(x)}D$ is also constant.
> **b)** If the curvature $k$ and torsion $\tau$ of $C$ are nowhere zero, then there must be constants $\lambda$ and $\mu$ such that $\lambda k+\mu\tau=1$.

**解答**

设 $C$ 以弧长参数化 $\gamma:I\to\mathbb R^3$（弧长参数 $s$），Frenet 标架 $(t,n,b)$、曲率 $k>0$、挠率 $\tau$；$D$ 以弧长参数化 $\gamma^*$，标架 $(t^*,n^*,b^*)$、曲率 $k^*$、挠率 $\tau^*$。"$f$ 是 $C$ 到 $D$ 的微分同胚"即存在重参数化，故可用同一参数 $s$ 标记对应点：$\gamma(s)\leftrightarrow\gamma^*(s)$。

**第 1 步（把"主法线相同"写成方程）.** $N_xC=N_{f(x)}D$ 意味着两主法线是**同一条直线**，故存在常数 $\varepsilon=\pm1$（由连续性，符号不能跳变 ✓）与函数 $\lambda=\lambda(s)$ 使
$$\gamma^*(s)=\gamma(s)+\lambda(s)\,n(s),\qquad n^*(s)=\varepsilon\, n(s),$$
且 $|x-f(x)|=|\lambda(s)|$ ✓。

**第 2 步（$\lambda$ 为常数）.** 对 $s$ 求导并用 Frenet 公式 $n'=-kt+\tau b$：
$$\frac{d\gamma^*}{ds}=t+\lambda' n+\lambda(-kt+\tau b)=(1-\lambda k)\,t+\lambda'\,n+\lambda\tau\,b .$$
左端与 $D$ 的单位切向量 $t^*$ 平行（$\gamma^*$ 是 $D$ 的正则参数化 ✓），而 $t^*\perp n^*=\pm n$，故右端沿 $n$ 的分量必须为 0：
$$\lambda'(s)=0\quad\Longrightarrow\quad\lambda\equiv\text{常数}.$$
于是 $|x-f(x)|=|\lambda|$ 为常数 ✓（(a) 的第一句）。

**第 3 步（两切向的夹角为常数）.** 由第 2 步，$\dfrac{d\gamma^*}{ds}=(1-\lambda k)t+\lambda\tau b\in\mathrm{span}\{t,b\}$，故 $t^*\in\mathrm{span}\{t,b\}$（注意 $\{t,b\}$ 与 $\{t^*,b^*\}$ 张成同一平面 $n^\perp$ ✓）。设 $\theta=\theta(s)$ 为 $t$ 与 $t^*$ 的带号夹角，则
$$t^*=\cos\theta\; t+\sin\theta\; b .$$
对 $s$ 求导：
$$\frac{dt^*}{ds}=-\theta'\sin\theta\; t+\cos\theta\,(k n)+\theta'\cos\theta\; b+\sin\theta\,(-\tau n)
=-\theta'\sin\theta\;t+\theta'\cos\theta\;b+(k\cos\theta-\tau\sin\theta)\,n .$$
另一方面，$t^*$ 是 $D$ 的单位切向量，按 $D$ 的弧长 $s^*$ 的 Frenet 公式 $\dfrac{dt^*}{ds^*}=k^*n^*=\varepsilon k^* n$，故
$$\frac{dt^*}{ds}=\frac{ds^*}{ds}\,\varepsilon k^*\,n ,$$
它没有 $t$、$b$ 分量。比较分量得
$$-\theta'\sin\theta=0,\qquad \theta'\cos\theta=0 .$$
由 $\sin^2\theta+\cos^2\theta=1$，两式强迫 $\theta'=0$，即 $\theta$ **为常数** ✓（(a) 的第二句）。

**第 4 步（导出 $\lambda k+\mu\tau=1$）.** 由第 2、3 步，
$$\frac{d\gamma^*}{ds}=(1-\lambda k)\,t+\lambda\tau\,b=c(s)\,t^*=c(s)\big(\cos\theta\,t+\sin\theta\,b\big),\qquad c(s)=\Big|\frac{d\gamma^*}{ds}\Big|=\frac{ds^*}{ds}>0 .$$
比较系数：
$$1-\lambda k=c\cos\theta,\qquad \lambda\tau=c\sin\theta .$$
题设 $k,\tau$ 处处非零；又 $D\neq C$（题面说 a different regular curve）且 $\lambda$ 为常数，若 $\lambda=0$ 则 $\gamma^*=\gamma$ 即 $D=C$，矛盾，故 $\lambda\neq0$ ✓，于是 $\lambda\tau\neq0$，从而 $\sin\theta\neq0$（否则 $\lambda\tau=0$ ✗）。两式相除：
$$\frac{1-\lambda k}{\lambda\tau}=\cot\theta=\text{常数}\quad(\theta\ \text{为常数}),$$
即 $1-\lambda k=-(\lambda\cot\theta)\,\tau$。取 $\mu:=-\lambda\cot\theta$（常数 ✓）得
$$\lambda k+\mu\tau=1 .\qquad\blacksquare$$

**补充（反向与特例）**：反过来，若 $C$ 的 $k,\tau$ 处处非零且存在常数 $\lambda,\mu$ 使 $\lambda k+\mu\tau=1$，则把 $C$ 沿主法线方向平移 $\lambda$ 所得的曲线 $D$ 与 $C$ 构成 Bertrand 对（$D$ 的主法线与 $C$ 的自动相同）。特别地 $\mu=0$ 对应 $k\equiv1/\lambda$ 为常数，这说明"每个常曲率的空间曲线都是 Bertrand 曲线"。

**本题考点/技巧（一句话）**：Frenet 求导一次，用"切向量平行于 $t^*$ 且 $t^*\perp n^*$"逼出 $\lambda'=0$；再用"$dt^*/ds$ 的 $t,b$ 分量同时为 0"逼出 $\theta'=0$；最后比较系数相除。

**难度**：4/5（无技巧难点，但计算链条长、符号多，考场上容易漏掉 $\varepsilon$、$\lambda\neq0$、$\sin\theta\neq0$ 这几处交代）。

**同类题出现年份**：**2017 团队 3**（测地挠率 $\tau_g$ 的那个 $3\times3$ 行列式公式）、**2017 个人 4**（测地曲率的 Liouville 公式）、**2013 团队 6**（任意闭曲线的全挠率为整数 ⟹ 曲面是球面或平面的一部分）、**2017 团队 6**（$|\mathrm{grad}\,f|=1$ ⟹ 积分曲线是测地线）、**2011 个人 6**（管状曲面 $\int_MH^2d\sigma\ge2\pi^2$，等号 $\iff$ $C$ 是半径 $\sqrt2\,r$ 的圆）。

---

## 9. 【偏难·4/5】2013 年 团体卷第 1 题 —— $\pi_1(\mathbb R^3\setminus X)=F_3$

**出处**：2013 年 · Geometry and Topology · 团体卷（`2013_TeamProblems2013`，PDF 第 3 页）· 第 1 题。

**题面**（**据 PDF 校正**：抽取文本上下标丢失，已按 PDF 页面校正）：

> Let $X$ be the space $\{(x,y,0)\mid x^2+y^2=1\}\cup\{(x,0,z)\mid x^2+z^2=1\}$. Find the fundamental group $\pi_1(\mathbb R^3\setminus X)$.

**答案**：
$$\pi_1(\mathbb R^3\setminus X)\cong F_3=\langle a,b,c\mid\ \varnothing\rangle .$$

**解答**

**第 0 步（几何图像）.** 记 $C_1=\{z=0,\ x^2+y^2=1\}$、$C_2=\{y=0,\ x^2+z^2=1\}$。二者都是单位球面 $S^2$ 上的**大圆**（$C_1$ 上每点满足 $x^2+y^2+z^2=1+0=1$ ✓，$C_2$ 同理）；两条不同的大圆恰交于一对对径点 $(1,0,0)$ 与 $(-1,0,0)$ ✓。
把 $X$ 看作图：顶点数 $V=2$（两个交点），边数 $E=4$（每个圆被两个交点切成 2 段弧），故
$$\beta_1(X)=E-V+1=3 .$$
两条大圆把 $S^2$ 分成 4 个球面二角形（lune），每个都同胚于开圆盘 ✓。

**第 1 步（把问题搬进 $S^3$）.** $X$ 紧，取 $R>1$ 使 $X\subset B_R$。映射 $x\mapsto x\cdot\min(1,R/|x|)$ 是 $\mathbb R^3\setminus X$ 到 $B_R\setminus X$ 的形变收缩（收缩路径上的半径始终 $\ge\min(|x|,R)>1$，绝不会碰到 $X\subset S^2_1$ ✓），故
$$\pi_1(\mathbb R^3\setminus X)\cong\pi_1(B_R\setminus X).$$
再用 van Kampen 把 $B_R$ 换成 $S^3$：取 $U=\mathbb R^3\setminus X$、$V=S^3\setminus \mathrm{int}\,B_{R/2}$，则 $U,V$ 为开集、$U\cup V=S^3\setminus X$，而 $U\cap V=\{R/2<|x|<R\}\cong S^2\times(0,1)$ 连通且单连通，$V$ 可缩，故
$$\pi_1(S^3\setminus X)\cong\pi_1(\mathbb R^3\setminus X).$$

**第 2 步（补空间 = "两个 3 球沿 4 个圆盘粘合"）.** 设 $N$ 为 $X$ 在 $S^3$ 中的正则邻域。因 $X\subset S^2$，可取
$$N=P\times[-\varepsilon,\varepsilon],\qquad P:=N_{S^2}(X)\ \text{（$X$ 在 $S^2$ 中的正则邻域）},$$
$P$ 是一个 4 洞平面曲面（4 个边界圆 ✓）。又 $N\setminus X\cong\partial N\times(0,1]$ 形变收缩到 $\partial N$，故
$$\mathbb R^3\setminus X\ \simeq\ S^3\setminus\mathrm{int}\,N .$$
把 $S^3$ 沿 $S^2$ 分成两个闭球：$B_+$（单位球内部）与 $B_-$（单位球外部连同 $\infty$）。则
$$S^3\setminus\mathrm{int}\,N=\big(B_+\setminus\mathrm{int}\,N\big)\ \cup_{S^2\setminus\mathrm{int}\,P}\ \big(B_-\setminus\mathrm{int}\,N\big).$$
- $B_\pm\setminus\mathrm{int}\,N$：这是从一个 3 球里挖去一块**贴在边界上的板** $P\times[0,\varepsilon]$。板沿法向可被压平到边界面 $\partial B_\pm$ 上的 $P$（板本身就是"边界面上一块薄片的乘积" ✓），压平后即为"3 球挖去边界面上的一个曲面 $P$"，这仍同胚于 3 球（把余下部分径向缩到球心 ✓）。故
$$B_\pm\setminus\mathrm{int}\,N\ \simeq\ \text{一点（可缩）}.$$
- 粘合面 $S^2\setminus\mathrm{int}\,P$ 是 **4 个互不相交的圆盘** $D_1,\dots,D_4$（4 个"面"各缩一点后的样子 ✓）。
于是
$$\mathbb R^3\setminus X\ \simeq\ Y:=\big(B_1\sqcup B_2\big)\Big/\big(D_i^{(1)}\sim D_i^{(2)},\ i=1,\dots,4\big),$$
即"两个 3 球沿各自球面上两两对应的 4 个圆盘粘起来"。

**第 3 步（算 $\pi_1(Y)$）.** 取 $Y$ 中的开覆盖
$$U:=B_1\cup\big(\text{$D_i$ 在 $B_2$ 中的领状邻域}\big),\qquad
V:=B_2\cup\big(\text{$D_i$ 在 $B_1$ 中的领状邻域}\big).$$
（二者在 $Y$ 中都是开的：$B_i$ 的内点是内点 ✓；边界球面上不在 $D_i$ 的点只属于一个球，其邻域仍开 ✓；$D_i$ 的内点与其边界圆周附近，$U$ 同时含两侧的半邻域 ✓。）
于是 $U\simeq B_1\simeq$ 点、$V\simeq B_2\simeq$ 点（都可缩 ✓），而
$$U\cap V=\bigsqcup_{i=1}^{4}\big(D_i\times(-\varepsilon,\varepsilon)\big)=\text{4 个互不相交的开球}.$$

> **引理（van Kampen 的广群形式）.** 设 $W=U\cup V$，$U,V$ 开且都单连通，$U\cap V$ 有 $k$ 个连通分支，则 $\pi_1(W)\cong F_{k-1}$。
> *理由.* Brown 的广群 van Kampen 定理把 $\Pi_1(W)$ 写为基本广群在 $\Pi_1(U\cap V)$ 上的推出。由于 $U,V$ 单连通，$\Pi_1(U),\Pi_1(V)$ 是"离散型广群"（任意两点间恰有一个态射）；$U\cap V$ 的每个分支贡献一条边（分支单连通时边群平凡）。该推出即"两个顶点、$k$ 条边、所有顶点群与边群皆平凡"的图的基本群，等于 $F_{k-1}$ ✓。（若某分支的 $\pi_1$ 非平凡，则须按该 $\pi_1$ 追加关系；本题每个分支都是开球，故无附加关系。）

代入 $k=4$：
$$\pi_1(\mathbb R^3\setminus X)\cong\pi_1(Y)\cong F_{4-1}=F_3 .$$
具体地，可取三个自由生成元为"在 $U$ 中从 $D_1$ 走到 $D_j$、再在 $V$ 中走回 $D_1$"的换轨环路（$j=2,3,4$），它们在 $\pi_1$ 中自由生成 ✓。

**第 4 步（两处独立校验）.**

*(i) Alexander 对偶.* 因 $X\subset S^3$ 紧，有 $\widetilde H_1(S^3\setminus X;\mathbb Z)\cong\widetilde H^1(X;\mathbb Z)=\mathbb Z^3$（$X\simeq S^1\vee S^1\vee S^1$，$\beta_1=3$ ✓）。而 $F_3$ 的交换化正是 $\mathbb Z^3$ ✓ 完全吻合。

*(ii) 把柄体观点.* $N=P\times[-\varepsilon,\varepsilon]$ 是亏格为 $b(P)-1=3$ 的柄体（$P$ 有 4 个边界圆、$\chi(P)=-2$，$P\times I$ 的亏格 $=1+(-\chi(P))-1=3$ ✓）。由于 $X$ 是**平面图**（躺在 $S^2$ 上、补集是 4 个圆盘），$N$ 是标准柄体，其在 $S^3$ 中的外部也是亏格 3 的柄体，故 $\pi_1$ 自由、秩 3 ✓。

*（第三法）* $X$ 作为平面图可沿 $S^2$ 同痕地"摊平"到某个平面上，而"平面图补空间的基本群自由、秩等于图的圈数"是经典结论，圈数 $=E-V+1=3$ ✓。

**本题考点/技巧（一句话）**：把紧集外部的补空间先收缩进球内、再沿一张球面把它切成两块可缩块，粘合面是 $k$ 个圆盘，于是 $\pi_1$ 由 van Kampen 的广群形式给出 $F_{k-1}$，最后用 Alexander 对偶验算交换化。

**难度**：4/5（几何图像与"不连通交集"的 van Kampen 是两处易错点）。

**同类题出现年份**：**2011 个人 3**（相扣两圆 $C_1,C_2$：$C_1$ 在 $\mathbb R^3\setminus C_2$ 中不可缩，用环绕数/linking）、**2018 团队 2**（$\mathbb R^3$ 中一个圆、以及上下半空间两个不相交圆的 $\pi_1$）、**2019 团队 2**（"A Beautiful Mind" 的 $\dim(V/W)$，与 $\mathbb R^3\setminus X$ 的 $H^1$ 同源）、**2014 团队 1**（$S^1\vee T^2$ 的基本群与同调）、**2013 个人 1**（环面粘两点后的同调与基本群）、**2020 第 6 题**（$F_2$ 的自由性与指数子群）、**2022 第 1 题**（两个四面体粘出的复形不是闭流形的伦型）、**2017 团队 1**（两个 Möbius 带沿边界粘合的 $\pi_1$）、**2016 团队 2 / 2015 团队 2**（悬挂 $\Sigma X$ 与同调）。

---

## 10. 【偏难·5/5】2018 年 个人卷第 6 题 —— Synge 定理

**出处**：2018 年 · Geometry and Topology · 个人卷（`2018_geometry2018_individual`）· 第 6 题。

**题面**（**原文**；据 PDF 逐字核对）：

> Let $M$ be an even dimensional compact and oriented Riemannian manifold with positive sectional curvature. Show that $M$ is simply connected.

**解答（反证 + 最短闭测地线 + 平行移动的 holonomy）**

设 $\dim M=n$（$n$ 为偶数），截面曲率处处 $>0$，$M$ 紧且可定向。

**第 1 步（非平凡自由同伦类中存在最短闭测地线）.** 反设 $\pi_1(M)\neq1$。则存在非平凡的**自由**同伦类 $\alpha$（闭曲线的自由同伦类与 $\pi_1$ 的共轭类一一对应 ✓）。

> *标准事实.* 紧 Riemann 流形上，每个非平凡自由同伦类中都存在长度最短的闭测地线。

*证明草图.* (i) 该类中曲线长度有正下界：长度 $<2\,\mathrm{inj}(M)$ 的闭曲线必可缩（它落在某个测地凸球内），故长度下确界 $L_0>0$。(ii) 取该类中长度趋于 $L_0$ 的极小化序列，按弧长参数化（$|\sigma'|\equiv1$）后由 Arzelà–Ascoli 取一致收敛子列。(iii) 极限曲线 $\gamma$ 的长度恰为 $L_0$、仍属于该类（自由同伦类对一致收敛封闭 ✓）；若 $\gamma$ 不是测地线，则可沿它把一小段"削角"，得到同伦的、更短的曲线，与极小性矛盾 ✓。

记 $\gamma:[0,L]\to M$ 为这样一条最短闭测地线：$\gamma(0)=\gamma(L)$、$\gamma'(0)=\gamma'(L)$、$|\gamma'|\equiv1$、$L>0$。

**第 2 步（Synge 引理）.**

> **引理.** 若 $\gamma$ 是紧流形上截面曲率 $>0$ 的最短闭测地线，$P=P_\gamma$ 为沿 $\gamma$ 的平行移动，则不存在 $v\in T_{\gamma(0)}M$ 同时满足 $v\neq0$、$v\perp\gamma'(0)$、$Pv=v$。

*证明.* 反设这样的 $v$ 存在。定义沿 $\gamma$ 的向量场 $V(t):=P_tv$（$P_t$：沿 $\gamma$ 从 $0$ 到 $t$ 的平行移动）。则
$$V'\equiv0,\qquad |V(t)|=|v|\neq0,\qquad V(t)\perp\gamma'(t)\ \ \forall t,\qquad V(L)=P_Lv=v=V(0),$$
即 $V$ 是**周期**向量场 ✓。平行向量场沿测地线是 Jacobi 场 ✓。
取变分
$$F(t,s):=\exp_{\gamma(t)}\big(s\,V(t)\big),\qquad |s|<\delta .$$
因 $V$ 周期，每条曲线 $\sigma_s(t):=F(t,s)$ 都是**闭曲线**，且经此变分与 $\gamma$ 自由同伦 ✓。由第一变分公式（$\gamma$ 是测地线）得长度函数满足 $\mathcal L'(0)=0$；第二变分公式给出
$$\mathcal L''(0)=\int_0^L\Big(\langle V',V'\rangle-\langle R(V,\gamma')\gamma',V\rangle\Big)\,dt
=-\int_0^L K\big(V\wedge\gamma'\big)\,|V|^2\,dt\;<\;0,$$
这里用到 $V'\equiv0$ ✓、$|V(t)|\equiv|v|\neq0$ ✓、$V\perp\gamma'$ 保证 $V,\gamma'$ 张成真的二维平面，其截面曲率 $K>0$ ✓。于是存在 $s\neq0$ 充分小使 $\mathcal L(\sigma_s)<\mathcal L(\gamma)=L$，与 $\gamma$ 在其自由同伦类中长度最短矛盾。引理得证 ∎

**第 3 步（线性代数：$SO(\text{奇数})$ 必有特征值 $+1$）.** 平行移动 $P$ 保持内积（$P\in O(T_{\gamma(0)}M)$ ✓），保持 $\gamma'(0)$（测地线切向量的平行移动 ✓），并且因 $M$ 可定向，$P$ 保定向：
$$P\in SO\big(T_{\gamma(0)}M\big),\qquad \det P=1 .$$
于是 $P$ 保持子空间 $\gamma'(0)^\perp$ 不变，并给出
$$P\big|_{\gamma'(0)^\perp}\in SO(n-1),\qquad \det\big(P|_{\gamma'(0)^\perp}\big)=\det P=1 .$$

> **事实.** 奇数维 $SO$ 中每个元素都有实特征值 $+1$。
> *证明.* 设 $A\in SO(2m+1)$，则 $\det A=\prod\lambda_i=1$。$A$ 的非实特征值成共轭对 $\lambda,\bar\lambda$ 出现，且 $\lambda\bar\lambda=|\lambda|^2>0$，对乘积贡献为正；故实特征值之积为 1。实特征值只能取 $\pm1$；若全为 $-1$，因个数为奇数，乘积为 $-1\neq1$，矛盾。故至少有一个实特征值 $+1$ ✓。

由 $n$ 偶知 $n-1$ 为奇数，故存在 $v\neq0$、$v\in\gamma'(0)^\perp$、$Pv=v$——与第 2 步的 Synge 引理矛盾 ✓。

**结论**：$\pi_1(M)\neq1$ 会导出矛盾，故 $\pi_1(M)=1$，即 $M$ 单连通。$\blacksquare$

**补充（三个条件都必需）**：本证明的机制可拆成三块——"最短闭测地线存在"（用紧性）、"第二变分 $<0$"（用正曲率）、"奇维 $SO$ 有特征值 $+1$"（用偶维 + 可定向）。相应地：
- 去掉"正曲率"：平坦环面 $T^2$ 偶维紧可定向但不单连通；
- 去掉"偶维"：$S^1\times S^2$ 紧、可定向、有正曲率乘积度量（$S^1$ 取任意度量）且 $\pi_1=\mathbb Z$；
- 去掉"可定向"：$\mathbb{RP}^{2}$（以及 $\mathbb{RP}^{2n}$）偶维紧、正曲率、但 $\pi_1=\mathbb Z_2$——这正是第 3 步中"$P$ 保定向"这一条被抽掉后的反例。

**本题考点/技巧（一句话）**：Synge 的"平行场变分"引理 + 偶维可定向情形下 holonomy 的初等线性代数。

**难度**：5/5。

**同类题出现年份**：**2013 个人 5**（偶维正曲率流形上任意闭测地线都可被长度更短的闭曲线扰动——正是本题第 2 步"变分"那一半）、**2021 第 5 题**（2 维正曲率紧流形上两条闭测地线必相交，Synge 型论证）、**2018 团队 6**（$\frac14<K_M\le1$ 的紧单连通流形同胚于 $S^n$，球面定理）、**2015 个人 5**（$\mathrm{diam}=\pi/c$ 且 $\mathrm{Ric}\ge(n-1)c^2$ ⟹ 等距于标准球面）、**2013 团队 5**（Myers 定理）、**2016 个人 5**（$\mathrm{Ric}>0\Rightarrow H^1(M;\mathbb R)=0$）、**2019 团队 5**（弱负曲率流形无非平凡 Killing 场）、**2020 第 2 题**（是否存在 $h>0$ 使 $\mathrm{Ric}(h)=1$）。

---

## 11. 讲义使用建议

### 11.1 总原则：三轮刷题

- **第一轮（独立限时做，不看解答）**：每题限时（见下表"首刷限时"）。做不出来就记下"卡在哪一步"，**立刻**看解答，然后合上解答，凭记忆把关键步骤默写一遍。
- **第二轮（隔 2–3 天，只写纲要）**：不做细节计算，只写"关键三句话"——用什么不变量/什么公式/矛盾在哪。能在 3 分钟内说出这三句，才算真会。
- **第三轮（考前一周，限时全套）**：本讲义按难度分 3 组，每组 3–4 题，用 150 分钟（丘赛该科目个人卷历史上给 2.5 小时，例如 2011 年卷面标注 9:30–12:00）做一组，模拟"6 选 5"的压力。

### 11.2 推荐顺序与用时

| 次序 | 题号 | 主题 | 首刷限时 | 复盘用时 | 前置知识 |
| --- | --- | --- | --- | --- | --- |
| 1 | 第 1 题（2010 个人 3） | 覆叠与定向 | 15 min | 20 min | 覆叠空间、行列式 |
| 2 | 第 2 题（2016 个人 2） | de Rham / Stokes | 20 min | 25 min | CW 复形、de Rham 定理 |
| 3 | 第 3 题（2026 第 1 题） | 高斯映射面积比 | 25 min | 30 min | 第一/第二基本形式、反函数定理 |
| 4 | 第 4 题（2010 个人 1） | 双曲距离 | 30 min | 35 min | 单值化、双曲平面距离公式 |
| 5 | 第 5 题（2019 团体 1） | 切丛非平凡 | 30 min | 30 min | 零截面自相交、欧拉类 |
| 6 | 第 6 题（2022 第 5 题） | H-空间 | 35 min | 35 min | cup 积、Künneth、Eckmann–Hilton |
| 7 | 第 7 题（2013 个人 6） | 极小曲面的 Gauss 映射 | 30 min | 30 min | Weingarten、主曲率 |
| 8 | 第 8 题（2011 个人 5） | Bertrand 曲线 | 45 min | 40 min | Frenet 公式（必须烂熟） |
| 9 | 第 9 题（2013 团体 1） | 补空间的基本群 | 50 min | 45 min | van Kampen、正则邻域、Alexander 对偶 |
| 10 | 第 10 题（2018 个人 6） | Synge 定理 | 60 min | 60 min | Jacobi 场、第二变分、平行移动 |

合计首刷约 **5.5 小时**，复盘约 **6 小时**。若时间紧，按 1 → 2 → 4 → 5 → 9 → 10 这个"最小骨架"顺序刷（覆盖覆叠、de Rham、双曲、丛、$\pi_1$、比较几何六条主线）。

### 11.3 备选的"考点串烧"顺序

若想按知识线而不是按难度刷，可用下面三条复线：

- **代数拓扑线**：第 1 题 → 第 2 题 → 第 5 题 → 第 9 题 → 第 6 题 → 第 10 题
  （覆叠/定向 → 上同调 → 示性类 → 基本群 → 同伦运算 → holonomy 锁拓扑）。
- **曲面/子流形线**：第 3 题 → 第 7 题 → 第 8 题 → （可选）2014 个人 5、2011 个人 6
  （Gauss 映射 → 极小性 → Frenet 计算 → 平均曲率积分不等式）。
- **Riemann/双曲线**：第 4 题 → 第 10 题 → （可选）2015 个人 5、2013 团队 5、2018 团队 6
  （具体模型计算 → 变分与 holonomy → 比较定理与刚性）。

### 11.4 每道题"必须写出来"的一句话

考场上时间紧，若只来得及写一句话，也要把下面这些写出来（阅卷看到关键结构通常就给分）：

| 题号 | 必须写出的一句话 |
| --- | --- |
| 1 | 用 $S^n\to\mathbb{RP}^n$ 的覆叠变换 $A=-I$，判定 $\det A=(-1)^{n+1}$ |
| 2 | 恰当 ⟹ 在闭流形上积分为 0（Stokes），而 $\int_{T^2}dx\wedge dy=1$ |
| 3 | $(N\circ\varphi)_u\times(N\circ\varphi)_v=K(\varphi_u\times\varphi_v)$，再取面积平均值 |
| 4 | 完备常曲率 −1 度量 = $\mathbb H/\langle z\mapsto z+1\rangle$，用 $z=e^{2\pi iw}$ 提升 |
| 5 | 零截面自相交数 = 欧拉数：$TS^2$ 给 2，$S^2\times\mathbb R^2$ 给 0 |
| 6 | $(a\ast c)\cdot(b\ast d)=(a\cdot b)\ast(c\cdot d)$；$\mu^*(\alpha)=\alpha\otimes1+1\otimes\alpha$ 且 $(\alpha\otimes1+1\otimes\alpha)^2=2\alpha\otimes\alpha$ |
| 7 | 极小 ⟹ $\kappa_2=-\kappa_1$ ⟹ $N^*g_{S^2}=\kappa^2ds^2=-K\,ds^2$ |
| 8 | $(\gamma^*)'=(1-\lambda k)t+\lambda'n+\lambda\tau b$ 必须与 $t^*\perp n$ 平行 ⟹ $\lambda'=0$ |
| 9 | 补空间 ≃ 两个 3 球沿 4 个圆盘粘合；$U\cap V$ 有 4 个分支 ⟹ \(\pi_1=F_3\) |
| 10 | 最短闭测地线 + 周期平行场的第二变分 $<0$ + $SO(\text{odd})$ 有 $+1$ 特征值 |

---

## 12. 无法完整解出 / 存疑清单

本讲义不含"假证明"：下面逐条列出**证明中的引用、隐含假设与不确定处**，以及被放弃的题目。

### 12.1 引用了外部定理（已尽量给出证明或证明草图）

1. **第 1 题**引用"覆叠变换群中每元素保定向 ⟺ 底空间可定向"。该引理已在解答中完整证明 ✓。$\mathbb{RP}^n$ 的胞腔同调只作旁证，未展开计算。
2. **第 2 题**引用 de Rham 定理（含同伦不变性）与 Poincaré–Lefschetz 对偶；$T^2\setminus\{p\}\simeq S^1\vee S^1$ 的收缩已显式写出 ✓。
3. **第 3 题**引用"带重数的面积公式"。这是标准结果；本题真正的技术点是 $K(p)=0$ 时 (N) 可能不单射，故只能用上界夹逼（已在解答中显式分开两种情形处理 ✓）。
4. **第 4 题**引用单值化定理与 Killing–Hopf 定理（"完备单连通常曲率 −1 曲面等距于 $\mathbb H$"）。这是本题的**必要背景**，无法在讲义篇幅内证明。
5. **第 5 题**第 1 步 (2) 引用"紧嵌入曲面的法欧拉数 = 自相交数"（交截理论的标准结论），并说明了 $S^2\times\mathbb R^2$ 中生成元的自相交数为 0 的理由 ✓。第 3 步的"端理论"仅作旁证，未展开。
6. **第 6 题 (b)** 只用到 Künneth 公式与 cup 积的自然性 ✓（可自查）。$S^n$ 是 H-空间的**完整**分类（$n\in\{1,3,7\}$）依赖 Adams 的 Hopf 不变量一，**未证**（题目只要求偶维反例，故不影响解答完整性）。
7. **第 9 题**第 3 步使用 van Kampen 的广群形式（Brown 定理）。我给出的是"两个顶点、$k$ 条边、群全平凡 ⟹ $F_{k-1}$"的图-of-groups 形式，并解释了为何不连通交集不能用朴素 van Kampen。**这是本讲义引用力度最大的一处**；若需要完全自足，可改用第 9 题第 4 步的第三法（平面图补空间基本群自由的经典结论）或把柄体法，二者结论一致，且与 Alexander 对偶 $\widetilde H_1=\mathbb Z^3$ 相符。
8. **第 10 题**引用两个标准事实：非平凡自由同伦类中最短闭测地线的存在性（已给 Arzelà–Ascoli 草图）、第二变分公式（未推导）。这两条属于 Riemann 几何课程的常规内容。

### 12.2 题面/前提上的存疑（如实标注）

9. **第 4 题（2010 个人 1）的定冠词问题**：题面说"**the** complete Riemannian metric on $D^*$ with constant curvature $-1$"。严格地说，若不要求与 $D^*$ 的标准共形结构相容，环带（$\cong D^*$）上还存在"漏斗型"完备双曲度量（例如 $\mathbb H/\langle z\mapsto2z\rangle$ 的推前），它与本题所用的"两端都是尖点"的度量**不**等距（有无闭测地线核心不同），答案也不同。本解答按竞赛意图取"与标准共形结构相容的完备双曲度量"（单值化度量），并在第 4 题第 1 步中写明了这一隐含前提 ✓。
10. **第 3 题（2026 第 1 题）中 "shrinks to $\{p\}$" 未给精确定义**：本解答按 $A_\varepsilon\subset B(p;r(\varepsilon))$、$r(\varepsilon)\to0$、$|A_\varepsilon|>0$ 理解。若允许 $A_\varepsilon$ 不连通或有分形边界，结论仍成立（证明只用到包含关系与面积正性）✓。
11. **第 2 题（2016 个人 2）第二问的读法歧义**：在 $T^2$ 上问 $\omega$ 是否恰当，答案是"否"；在 $T^2\setminus\{p\}$ 上问，答案是"是"。两种读法本讲义都给了 ✓。
12. **第 8 题（2011 个人 5）**：解答中用到了 $\lambda\neq0$（因 $D\neq C$）与 $\sin\theta\neq0$（因 $\tau\neq0$）。若题面允许 $D$ 与 $C$ 相差一个刚体运动（即重合的曲线），则 $\lambda=0$，(b) 的结论需要另行讨论——但题面明确写 a different regular curve ✓。
13. **第 9 题（2013 团体 1）**：题面只说"find the fundamental group"，未指明基点；$\mathbb R^3\setminus X$ 道路连通，故无歧义 ✓。答案 $F_3$ 已用 Alexander 对偶独立验证 ✓。
14. **第 10 题（2018 个人 6）**：证明只用到"正截面曲率"，而 Synge 定理的经典形式只要求正的 Ricci 曲率（偶维可定向）。本题按卷面假设（正截面曲率）作答 ✓。

### 12.3 被我放弃、未写入本讲的真题（含原因）

15. **2014 个人 2**（极小图的 $K=\Delta\log(1+1/W)$ 与 Bernstein 定理）：(a) 要求在**诱导度量**下的 Laplace 算子下验证恒等式，书写量极大；(b) 是真 Bernstein 定理，需 Cheng–Yau / do Carmo–Peng 级别的工具，无法在讲义篇幅内严格给出。
16. **2020 第 1 题**（$S^6$ 上的 6-形式、$f^*\alpha=d\phi$、Hopf 不变量 $H(f)\in2\mathbb Z$）：(a)(b)(c) 可做，(d) 属于 Hopf 不变量理论，超出手写讲义的严谨边界。
17. **2021 第 1 题**（$P^{2n}$ 不能是紧流形的边界、$P^3$ 可以）：卷面上记号 $P^{n}$ **未定义**（按 $\mathbb{RP}^n$ 读才讲得通），有歧义风险，故不选。
18. **2023 第 4 题**（Leray–Hirsch 定理与旗流形的 Euler 数）：需要 Leray–Hirsch、旗流形胞腔分解与 Poincaré 多项式一整套工具，篇幅性价比低。
19. **2016 团队 6**（$S^{n+1}$ 中常数量曲率极小超曲面：$S=0$ 或 $S\ge n$）：证明依赖 Simons 恒等式 $\Delta S=2|\nabla A|^2+2nS-2S^2$，只能"引理式"引用，与本讲义"每一步可验证"的定位冲突。
20. **2013 个人 3**（共轭点与 Sturm 比较）：完全可解，但与第 10 题同为 Jacobi 场/比较论证，为保证覆盖面而未选。
21. **2012 个人 6 / 2012 团队 3**（结构方程证常截面曲率；Levi-Civita 连接的唯一性）：抽取文本中张量公式损伤较重（上下标与指标位置丢失），逐字校对成本高于其余候选题。

### 12.4 额外的自我校验记录

- 第 4 题的答案 $\operatorname{arccosh}(3/2)$ 用两条独立路径核对：覆盖到 $\mathbb H$ 后用 $\cosh$ 距离公式；以及沿实轴的径向积分（得 $\ln2$，与 $\mathbb H$ 中 $i$ 到 $i/2$ 的距离一致）✓。
- 第 9 题的答案 $F_3$ 用三条独立路径核对：广群 van Kampen（$k=4\Rightarrow F_3$）、Alexander 对偶（$\widetilde H^1(X)=\mathbb Z^3$）、把柄体/平面图（圈秩 3）✓。
- 第 10 题第 3 步的"奇维 $SO$ 有 $+1$ 特征值"已给出完整证明 ✓；第 8 题第 3 步"由 $\theta'\sin\theta=\theta'\cos\theta=0$ 得 $\theta'=0$"也已交代 $\sin^2+\cos^2=1$ 的理由 ✓。
- 全部 10 道题的题面均与原始 PDF 逐字核对，核对文件为：
  `2010/GeometryTopology-indi.pdf`、`2011/3.GeomTop-Individual-2011.pdf`、`2013/geometry2013(individual).pdf`、
  `2013/TeamProblems2013.pdf`（第 3 页）、`2016/geometry2016-individual.pdf`、`2018/geometry2018-individual.pdf`、
  `2019/Geometry2019-team.tex`、`2022/ExamPaper_2022/geometry_and_topology_22s.pdf`、`2026/2026 Geo_Topology.pdf`。
  抽取脚本与抽取结果留存于 `/check_pdfs.py`、`check_pdfs2.py`、`check_pdfs3.py` 与
  `pdf_check1.txt`、`pdf_check2.txt`、`pdf_check3.txt`。



