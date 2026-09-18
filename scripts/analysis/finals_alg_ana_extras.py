# -*- coding: utf-8 -*-
"""总决赛：原 pipeline 遗漏、由本报告从 .doc/.docx 源文件恢复的卷（公式多为 OLE 对象，已丢失）。"""
E = [
# ---- ALG 2014 Team (源: 2014 Algebra (Team).docx) ----
(2014,'ALG','Team','1','求 C[x,y] 中在线性变换 α:(x,y)↦(−x,x+y) 与 β:(x,y)↦(x+y,−y) 下不变的多项式','rep,comm','不变量论 / 有限群作用',3,'docx','题面公式经 .docx 抽取后残缺，α,β 的具体形式按残文重排，存疑'),
(2014,'ALG','Team','2','φ(u)=1+u+u²/2!+…+u^n/n! 给出“特征值全 0”与“特征值全 1”矩阵集之间的双射；n=2m 时由 A J + J A^t=0 推出 φ(A) J φ(A)^t=I','linear','矩阵指数 / 幂零与幺幂',4,'docx','抽取残缺，矩阵 J 的形式按上下文还原'),
(2014,'ALG','Team','3','解 x²−2y²=7（x,y∈Z）；并判定哪些整数 n 使 x²−2y²=n 可解','ant,quad','Pell 方程 / 二次型','3','docx',''),
(2014,'ALG','Team','4','有限群 G 的换位子群是 p-群，char R=p>0 的代数闭域上不可约 G-模必为 1 维','rep','模表示 / Clifford 定理','4','docx',''),
# ---- ANA 2012 Individual (源: 2012 Analysis (Individual).doc) ----
(2012,'ANA','Individual','1','初边值问题的分离变量求解：解族构成正交基且完备、唯一性','pde','Sturm–Liouville / 分离变量','3','doc','方程本体与边界条件丢失（[EQ] 占位）'),
(2012,'ANA','Individual','2','整函数的迭代：若存在某常数使某不等式对所有 n 成立，则……（题面残缺）','cplx','迭代 / 正规族','—','doc','题面公式全部丢失，无法判定结论，放弃分析'),
(2012,'ANA','Individual','3','若 f 限制到平面每条直线上连续，f 是否必连续？光滑性同问？','real','多元连续性 / 反例','2','doc',''),
# ---- ANA 2013 Individual (源: 2013 Analysis (Individual).docx) ----
(2013,'ANA','Individual','1','R¹×[0,1] 上非光滑有界凸函数与 x 无关','real','凸分析','3','docx',''),
(2013,'ANA','Individual','2','性质 f(1/n)=1/n³+e^{−2n}：不存在单位盘内解析 f 满足之；但存在 0<|z|<1 上解析 g 满足；能否使 f 永不为整数','cplx','解析延拓 / 唯一性定理','4','docx',''),
(2013,'ANA','Individual','3','L¹(E) 中 fg∈L¹(E) ⟹ 存在零测集 F 使 g∈L^∞(E\\F)；并给出 ‖g‖_∞ 的上确界刻画','real','对偶 / 一致有界','3','docx',''),
(2013,'ANA','Individual','4','Poincaré 不等式：(a) C¹[−1,1] 上 ∫(f−平均)² ≤ C∫|f′|²；(b) C¹(B1)（B1⊂R²）上同型估计','real,ineq','Poincaré 不等式','3','docx',''),
# ---- ANA 2013 Team (源: 2013 Analysis (Team).docx) ----
(2013,'ANA','Team','1','Fourier 部分和 u_n 在单位圆盘紧子集一致收敛到调和函数；∫_D(u_x²+u_y²)=πΣn(a_n²+b_n²)；Hölder 类 α∈(1/2,1) 时 Σ(a_n²+b_n²) ≤ C|f|_{C^α}²','harm','Poisson 积分 / Dirichlet 能量 / Hölder 估计','4','docx',''),
(2013,'ANA','Team','2','（源文件中该题无内容：仅 “Problem 2” 标题）','—','—','—','docx','原文缺题'),
(2013,'ANA','Team','3','∂_t u−Δu=u² 于 B1，Neumann 边界：比较原理；常值解 u≡a；u0>0 时解在有限时刻爆破','pde','比较原理 / 爆破','5','docx',''),
(2013,'ANA','Team','4','f≥0 单调下降且 ∫_{x−a}^x f ≤ (5/4)∫_x^{x+a} f ⟹ f∈L^p(0,1) 对 1≤p< log2/(log3−log2)','real,ineq','L^p 提升 / 权重估计','5','docx',''),
# ---- ANA 2013 Overall (源: 2013 Analysis (Overall).docx) ----
(2013,'ANA','Overall','1','调和函数的平均值性质、Harnack 不等式与最大值原理','potential','平均值性质 / Harnack / 极值原理','3','docx',''),
(2013,'ANA','Overall','2','φ(z)=λz+az²+…（a≠0）：构造近恒等解析 f 使 φ∘f = f∘(λz+O(z³))；λ>1 时能否线性化 φ∘f=f∘(λz)','cplx','Schröder 线性化 / 共轭方程','5','docx',''),
# ---- ANA 2014 Individual (源: 2014 Analysis (Individual and Overall).doc) ----
(2014,'ANA','Individual','1','求 C、单位圆盘 D、Riemann 球面 Ĉ 的共形自同构群并证明','cplx','Möbius 变换 / Aut(D)','3','doc',''),
(2014,'ANA','Individual','2','单位圆盘上收敛幂级数：证明 Schwarz 引理（|f(z)|≤|z| 与 |f′(0)|≤1）','cplx','Schwarz 引理','2','doc',''),
(2014,'ANA','Individual','3','设（内容丢失）… 对素数全体证明级数发散','real','级数发散','—','doc','题面公式全丢，仅余“证明发散”'),
(2014,'ANA','Individual','4','区间上连续实值函数不可能是二到一的映射','real','连续映射 / 中值定理','3','doc',''),
(2014,'ANA','Individual','5','（a)(b) 两小问，题面公式丢失）','—','—','—','doc','放弃分析'),
(2014,'ANA','Individual','6','Burgers 方程：a) 初值满足某条件时存在整体解；b) 另一条件下存在爆破时刻 T','pde','Burgers / 整体解与爆破','5','doc','条件公式丢失'),
# ---- ANA 2014 Team (源: 2014 Analysis (Team).docx) ----
(2014,'ANA','Team','1','f(z)=z² 的迭代：|z|<1 时趋于 0、|z|>1 时趋于 ∞；对 g(z)=z²−2 求所有 g^n(z)→∞ 的点','dyn','迭代 / Chebyshev 共轭','4','docx',''),
(2014,'ANA','Team','2','求 A={z: 0<arg z<π/2, 0<|z|<1} 到单位圆盘的共形映射','cplx','共形映射 / 幂函数','3','docx',''),
(2014,'ANA','Team','3','周期 2 连续函数的 Fourier 级数：部分和一致收敛到调和函数；∫_D(u_x²+u_y²)=πΣn(a_n²+b_n²)','harm','Poisson 积分 / Dirichlet 能量','4','docx',''),
(2014,'ANA','Team','4','非减非负 ω 满足 ω(γR)≤ηω(R)+KR^α ⟹ ω(R) ≤ C(R/R0)^βω(R0)+CKR^α（迭代引理）','harm,ineq','迭代引理 / Campanato','4','docx',''),
(2014,'ANA','Team','5','l^∞(N) 上 f_n=e^{2πinθ}：值域在单位圆周稠密；{f_n,1} 生成的闭自伴子代数的极大理想空间同胚于单位圆周','func','Gelfand 理论 / 极大理想空间','5','docx',''),
(2014,'ANA','Team','6','证明 Σ_{n≥1} 1/n² = π²/6','real','Fourier 级数 / Parseval','3','docx',''),
]
