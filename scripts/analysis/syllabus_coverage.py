# -*- coding: utf-8 -*-
"""
考纲覆盖率分析（丘成桐大学生数学竞赛 Yau Contest）
--------------------------------------------------
输入： ./data/problems_full.json （757 道笔试真题，含完整题面）
      ./corpus/finals/*Syllabus*.txt （6 份官方考纲）
输出： ./data/syllabus_coverage.json

方法：把 6 份考纲逐条拆成"考纲条目"（每条 = 中文名 + 原文英文术语 + 一组正则），
      在【同科目】的真题题面里检索，统计命中题数 / 年份分布 / 近年趋势，
      再给出 高频命中 / 偶发命中 / 零命中 三态；并反向统计"超纲候选考点"。
"""
import json, re, os, sys, collections, datetime

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"."
PROBLEMS = os.path.join(ROOT, "data", "problems_full.json")
OUT = os.path.join(ROOT, "data", "syllabus_coverage.json")

# 近年窗口：2022-2026（数理物理 2022 年才设科）；早期窗口：2010-2021
RECENT_FROM = 2022

# ---------------------------------------------------------------------------
# 1) 结构化考纲：subject -> [ (section_cn, [ (id, cn, en, [patterns]) ]) ]
# ---------------------------------------------------------------------------
SYLLABUS = [
 ("Algebra & Number Theory", "代数与数论（Algebra and Number Theory）", [
  ("代数：群论（Group theory）", [
   ("ALG-G1", "Sylow 定理", "Sylow theorems", [r"Sylow"]),
   ("ALG-G2", "p-群", "p-groups", [r"\bp-groups?\b", r"\bp\b-group"]),
   ("ALG-G3", "可解群", "solvable groups", [r"solvab"]),
   ("ALG-G4", "自由群", "free groups", [r"free\s+group"]),
  ]),
  ("代数：环与模（Rings and modules）", [
   ("ALG-R1", "张量积", "tensor products", [r"tensor\s+product", r"tensor\s+power", r"\btensor\b"]),
   ("ALG-R2", "行列式", "determinants", [r"determinant"]),
   ("ALG-R3", "Jordan 标准形", "Jordan canonical form", [r"Jordan"]),
   ("ALG-R4", "主理想整环", "PID", [r"\bPIDs?\b", r"principal\s+ideal"]),
   ("ALG-R5", "唯一分解整环", "UFD", [r"\bUFDs?\b", r"unique\s+factorization"]),
   ("ALG-R6", "多项式环", "polynomial rings", [r"polynomial\s+ring", r"polynomial\s+algebra"]),
  ]),
  ("代数：域论（Field theory）", [
   ("ALG-F1", "分裂域", "splitting fields", [r"splitting\s+field"]),
   ("ALG-F2", "可分与不可分扩张", "separable and inseparable extensions", [r"separable", r"inseparable"]),
  ]),
  ("代数：Galois 理论（Galois theory）", [
   ("ALG-GA1", "Galois 理论基本定理", "Fundamental theorems of Galois theory", [r"Galois"]),
   ("ALG-GA2", "有限域", "finite fields", [r"finite\s+field", r"\bGF\(", r"\bF_[pq]\b"]),
   ("ALG-GA3", "分圆域", "cyclotomic fields", [r"cyclotomic"]),
  ]),
  ("代数：同调代数（Homological algebra）", [
   ("ALG-H1", "正合列", "exact sequences", [r"exact\s+sequence"]),
   ("ALG-H2", "分裂", "splittings", [r"splits?\s+(the\s+)?(exact\s+)?sequence", r"sequence\s+splits", r"split\s+exact"]),
   ("ALG-H3", "蛇引理与五引理", "snake and five lemmas", [r"snake\s+lemma", r"five\s+lemma"]),
   ("ALG-H4", "投射、内射、平坦模", "projective, injective, and flat modules", [r"projective\s+module", r"injective\s+module", r"flat\s+module", r"projective\s+resolution", r"injective\s+resolution"]),
   ("ALG-H5", "复形与（上）同调", "complexes, (co)homology", [r"cohomology", r"homology", r"chain\s+complex"]),
  ]),
  ("代数：交换环（Commutative ring）", [
   ("ALG-C1", "局部化", "localizations", [r"localiz", r"localis"]),
   ("ALG-C2", "Hilbert 基定理", "Hilbert's basis theorem", [r"basis\s+theorem", r"Hilbert.{0,24}basis"]),
   ("ALG-C3", "整扩张", "integral extensions", [r"integral\s+extension", r"integral\s+over", r"integrally\s+closed"]),
   ("ALG-C4", "理想的根", "radicals of ideals", [r"radical\s+of\s+(an\s+)?ideal", r"nilradical", r"Jacobson\s+radical", r"\bradical\b"]),
   ("ALG-C5", "Zariski 拓扑与 Hilbert 零点定理", "Zariski topology and Hilbert's Nullstellensatz", [r"Zariski", r"Nullstellensatz"]),
   ("ALG-C6", "Dedekind 环", "Dedekind rings", [r"Dedekind"]),
   ("ALG-C7", "离散赋值环", "DVRs", [r"\bDVRs?\b", r"discrete\s+valuation"]),
  ]),
  ("代数：有限群表示论（Representations of Finite Groups）", [
   ("ALG-REP1", "特征标理论", "character theory", [r"character\s+table", r"character\s+theory", r"character\s+of\s+a\s+representation", r"irreducible\s+character", r"\bcharacters\b"]),
   ("ALG-REP2", "诱导表示", "induced representations", [r"induced\s+representation", r"induction\s+of\s+representation", r"Frobenius\s+reciprocity"]),
   ("ALG-REP3", "群环的结构", "structure of the group ring", [r"group\s+ring", r"group\s+algebra"]),
  ]),
  ("代数：Lie 群与 Lie 代数基础（Basics of Lie groups and Lie algebras）", [
   ("ALG-LIE1", "指数映射", "exponential map", [r"exponential\s+map"]),
   ("ALG-LIE2", "幂零与半单 Lie 代数、Lie 群", "nilpotent and semi-simple Lie algebras and Lie groups", [r"Lie\s+algebra", r"Lie\s+group", r"nilpotent\s+Lie", r"semi[- ]?simple\s+Lie"]),
  ]),
  ("数论：初等与解析（Number Theory, elementary/analytic）", [
   ("NT-1", "因子分解与素数", "Factorization and the primes", [r"\bprimes?\b", r"prime\s+(number|factor|divisor)", r"factoriz"]),
   ("NT-2", "同余", "congruences", [r"congruen", r"\bmodulo\b", r"\bmod\s+\d"]),
   ("NT-3", "二次剩余与互反律", "quadratic residues and reciprocity", [r"quadratic\s+residue", r"quadratic\s+reciprocity", r"Legendre\s+symbol", r"Jacobi\s+symbol"]),
   ("NT-4", "连分数与逼近", "continued fractions and approximations", [r"continued\s+fraction", r"Diophantine\s+approximation", r"rational\s+approximation"]),
   ("NT-5", "eta 函数", "eta functions", [r"\beta\s+function"]),
   ("NT-6", "zeta 函数", "zeta functions", [r"zeta"]),
  ]),
  ("数论：代数数论（Number Theory, algebraic）", [
   ("NT-7", "数域", "Number fields", [r"number\s+field", r"algebraic\s+number"]),
   ("NT-8", "理想的唯一分解", "unique factorization of ideals", [r"unique\s+factorization\s+of\s+ideal", r"prime\s+ideal", r"Dedekind\s+domain"]),
   ("NT-9", "类群的有限性", "finiteness of class group", [r"class\s+group", r"class\s+number"]),
   ("NT-10", "单位群的结构", "structure of unit group", [r"unit\s+group", r"group\s+of\s+units", r"units\s+of"]),
   ("NT-11", "Frobenius 元素", "Frobenius elements", [r"Frobenius"]),
   ("NT-12", "局部域", "local fields", [r"local\s+field", r"p-adic", r"\bp-adic\b"]),
   ("NT-13", "分歧", "ramification", [r"ramif"]),
   ("NT-14", "弱逼近", "weak approximation", [r"weak\s+approximation"]),
  ]),
 ]),

 ("Analysis & PDE", "分析与偏微分方程（Analysis and Differential Equations）", [
  ("实分析（Real Analysis）", [
   ("AN-R1", "积分收敛定理", "Convergence theorems for integrals", [r"convergence\s+theorem", r"monotone\s+convergence", r"dominated\s+convergence", r"dominated"]),
   ("AN-R2", "Borel 测度", "Borel measure", [r"Borel"]),
   ("AN-R3", "Riesz 表示定理", "Riesz representation theorem", [r"Riesz"]),
   ("AN-R4", "Lp 空间", "Lp space", [r"L\^?p\b", r"\bLp\b", r"L\^p"]),
   ("AN-R5", "Lp 空间的对偶", "Duality of Lp space", [r"duality", r"dual\s+space", r"dual\s+of\s+L"]),
   ("AN-R6", "Jensen 不等式", "Jensen inequality", [r"Jensen"]),
   ("AN-R7", "Lebesgue 微分定理", "Lebesgue differentiation theorem", [r"Lebesgue\s+differentiation", r"differentiation\s+theorem", r"Lebesgue\s+point"]),
   ("AN-R8", "Fubini 定理", "Fubini theorem", [r"Fubini", r"Tonelli"]),
   ("AN-R9", "Hilbert 空间", "Hilbert space", [r"Hilbert\s+space"]),
   ("AN-R10", "有界变差复测度", "Complex measures of bounded variation", [r"bounded\s+variation", r"complex\s+measure"]),
   ("AN-R11", "Radon-Nikodym 定理", "Radon-Nikodym theorem", [r"Radon[- ]Nikodym", r"absolutely\s+continuous.{0,20}measure"]),
   ("AN-R12", "Hahn-Banach 定理", "Hahn-Banach Theorem", [r"Hahn[- ]Banach"]),
   ("AN-R13", "开映射定理", "open mapping theorem", [r"open\s+mapping"]),
   ("AN-R14", "一致有界性定理", "uniform boundedness theorem", [r"uniform\s+boundedness", r"Banach[- ]Steinhaus"]),
   ("AN-R15", "闭图像定理", "closed graph theorem", [r"closed\s+graph"]),
   ("AN-R16", "紧算子的基本性质", "Basic properties of compact operators", [r"compact\s+operator"]),
   ("AN-R17", "Riesz-Fredholm 理论", "Riesz-Fredholm Theory", [r"Fredholm"]),
   ("AN-R18", "紧算子的谱", "spectrum of compact operators", [r"spectrum", r"spectral\s+theorem", r"spectral\s+radius"]),
   ("AN-R19", "Fourier 级数", "Fourier series", [r"Fourier\s+series"]),
   ("AN-R20", "Fourier 变换", "Fourier transform", [r"Fourier"]),
   ("AN-R21", "卷积", "convolution", [r"convolut"]),
  ]),
  ("复分析（Complex Analysis）", [
   ("AN-C1", "全纯与亚纯函数", "Holomorphic and meromorphic functions", [r"holomorphic", r"meromorphic", r"entire\s+function", r"analytic\s+function"]),
   ("AN-C2", "共形映射", "Conformal maps", [r"conformal"]),
   ("AN-C3", "分式线性变换", "linear fractional transformations", [r"linear\s+fractional", r"fractional\s+linear", r"Mobius", r"Möbius"]),
   ("AN-C4", "Schwarz 引理", "Schwarz's lemma", [r"Schwarz"]),
   ("AN-C5", "Cauchy 定理", "Cauchy's theorem", [r"Cauchy.{0,12}theorem", r"Cauchy.{0,12}integral\s+theorem"]),
   ("AN-C6", "Cauchy 积分公式", "Cauchy integral formula", [r"Cauchy.{0,12}integral\s+formula", r"Cauchy\s+integral"]),
   ("AN-C7", "留数", "residues", [r"residue"]),
   ("AN-C8", "调和函数：平均值性质", "Harmonic functions: the mean value property", [r"mean\s+value\s+property", r"mean[- ]value"]),
   ("AN-C9", "反射原理", "the reflection principle", [r"reflection\s+principle", r"Schwarz\s+reflection"]),
   ("AN-C10", "Dirichlet 问题", "Dirichlet's problem", [r"Dirichlet\s+problem", r"Dirichlet\s+boundary"]),
   ("AN-C11", "Laurent 级数", "Laurent series", [r"Laurent"]),
   ("AN-C12", "部分分式展开", "partial fractions expansions", [r"partial\s+fraction"]),
   ("AN-C13", "典型乘积", "canonical products", [r"canonical\s+product", r"Weierstrass\s+product", r"infinite\s+product"]),
   ("AN-C14", "特殊函数：Gamma 函数", "the Gamma function", [r"Gamma\s+function", r"\\Gamma", r"gamma\s+function"]),
   ("AN-C15", "特殊函数：zeta 函数", "the zeta functions", [r"zeta"]),
   ("AN-C16", "特殊函数：椭圆函数", "elliptic functions", [r"elliptic\s+function", r"elliptic\s+integral", r"Weierstrass.{0,12}elliptic"]),
   ("AN-C17", "Riemann 曲面基础", "Basics of Riemann surfaces", [r"Riemann\s+surface"]),
   ("AN-C18", "Riemann 映射定理", "Riemann mapping theorem", [r"Riemann\s+mapping"]),
   ("AN-C19", "Picard 定理", "Picard theorems", [r"Picard"]),
  ]),
  ("微分方程（Differential Equations）", [
   ("AN-D1", "ODE 解的存在唯一性定理", "Existence and uniqueness theorems for solutions of ODE", [r"existence\s+and\s+uniqueness", r"Picard[- ]Lindel", r"uniqueness\s+theorem"]),
   ("AN-D2", "简单方程的显式解", "explicit solutions of simple equations", [r"explicit\s+solution", r"closed[- ]form\s+solution", r"solve\s+explicitly"]),
   ("AN-D3", "有限区间上的自伴边值问题", "self-adjoint boundary value problems on finite intervals", [r"self[- ]adjoint", r"boundary\s+value\s+problem"]),
   ("AN-D4", "临界点、相空间、稳定性分析", "critical points, phase space, stability analysis", [r"critical\s+point", r"equilibri", r"stability", r"stable", r"Lyapunov"]),
   ("AN-D5", "一阶偏微分方程", "First order partial differential equations", [r"first[- ]order\s+(partial|PDE|equation)", r"method\s+of\s+characteristics", r"characteristic\s+curve"]),
   ("AN-D6", "线性与拟线性 PDE", "linear and quasi-linear PDE", [r"quasi[- ]?linear", r"semi[- ]?linear", r"linear\s+PDE"]),
   ("AN-D7", "相平面分析", "Phase plane analysis", [r"phase\s+plane", r"phase\s+portrait"]),
   ("AN-D8", "Burgers 方程", "Burgers equation", [r"Burgers"]),
   ("AN-D9", "Hamilton-Jacobi 方程", "Hamilton-Jacobi equation", [r"Hamilton[- ]Jacobi"]),
   ("AN-D10", "位势方程：Green 函数", "Potential equations: Green functions", [r"Green'?s?\s+function"]),
   ("AN-D11", "Dirichlet 问题解的存在性", "existence of solutions of Dirichlet problem", [r"Dirichlet\s+problem"]),
   ("AN-D12", "调和函数", "harmonic functions", [r"harmonic\s+function", r"\bharmonic\b"]),
   ("AN-D13", "极大值原理及应用", "maximal principle and applications", [r"maxim(um|al)\s+principle"]),
   ("AN-D14", "Neumann 问题解的存在性", "existence of solutions of Neumann's problem", [r"Neumann\s+problem", r"Neumann\s+boundary"]),
   ("AN-D15", "热方程", "Heat equation", [r"heat\s+equation", r"\bheat\b"]),
   ("AN-D16", "基本解", "fundamental solutions", [r"fundamental\s+solution"]),
   ("AN-D17", "波动方程：初值与边值条件", "Wave equations: initial condition and boundary condition", [r"wave\s+equation"]),
   ("AN-D18", "适定性", "well-posedness", [r"well[- ]posed"]),
   ("AN-D19", "Sturm-Liouville 特征值问题", "Sturm-Liouville eigenvalue problem", [r"Sturm[- ]Liouville"]),
   ("AN-D20", "能量泛函方法", "energy functional method", [r"energy\s+(functional|method|estimate)", r"variational\s+method", r"variational\s+principle"]),
   ("AN-D21", "解的唯一性与稳定性", "uniqueness and stability of solutions", [r"uniqueness", r"stability"]),
   ("AN-D22", "分布", "Distributions", [r"distributional", r"weak\s+derivative", r"test\s+function", r"distribution\s+theory"]),
   ("AN-D23", "Sobolev 嵌入定理", "Sobolev embedding theorem", [r"Sobolev"]),
  ]),
 ]),

 ("Computational & Applied", "计算与应用数学（Computational and Applied Mathematics）", [
  ("插值与逼近（Interpolation and approximation）", [
   ("CA-1", "三角插值与逼近", "Trigonometric interpolation and approximation", [r"trigonometric\s+(interpolation|polynomial)", r"Fourier\s+interpolation"]),
   ("CA-2", "快速 Fourier 变换", "fast Fourier transform", [r"\bFFT\b", r"fast\s+Fourier"]),
   ("CA-3", "有理函数逼近", "approximations by rational functions", [r"rational\s+(function\s+)?approximation", r"Pade", r"Padé"]),
   ("CA-4", "多项式与样条插值与逼近", "polynomial and spline interpolations and approximation", [r"spline", r"polynomial\s+interpolation", r"interpolat"]),
   ("CA-5", "最小二乘逼近", "least-squares approximation", [r"least[- ]squares?"]),
  ]),
  ("非线性方程求解（Nonlinear equation solvers）", [
   ("CA-6", "二分法", "bisection", [r"bisection", r"bisect"]),
   ("CA-7", "Newton 法", "Newton's method", [r"Newton'?s?\s+method", r"Newton\s+iteration", r"Newton[- ]Raphson"]),
   ("CA-8", "拟 Newton 法", "quasi-Newton's methods", [r"quasi[- ]Newton", r"secant\s+method", r"Broyden"]),
   ("CA-9", "不动点方法", "fixed-point methods", [r"fixed[- ]point"]),
   ("CA-10", "多项式求根", "finding roots of polynomials", [r"roots?\s+of\s+(a\s+)?polynomial", r"polynomial\s+roots?", r"find\s+all\s+roots"]),
  ]),
  ("线性系统与特征值问题（Linear systems and eigenvalue problems）", [
   ("CA-11", "线性系统与特征值问题的经典与现代迭代法", "Classical and modern iterative method for linear systems and eigenvalue problems", [r"iterative\s+method", r"power\s+method", r"Jacobi\s+iteration", r"Gauss[- ]Seidel", r"conjugate\s+gradient", r"Krylov", r"Arnoldi", r"Lanczos"]),
   ("CA-12", "条件数与奇异值分解", "condition number and singular value decomposition", [r"condition\s+number", r"singular\s+value", r"\bSVD\b"]),
   ("CA-13", "大型稀疏线性方程组迭代法", "iterative methods for large sparse system of linear equations", [r"sparse", r"precondition"]),
  ]),
  ("常微分方程数值解（Numerical solutions of ODE）", [
   ("CA-14", "单步法", "Single step methods", [r"single[- ]step", r"Euler'?s?\s+method", r"Runge[- ]Kutta", r"Taylor\s+method"]),
   ("CA-15", "多步法", "multi-step methods", [r"multi[- ]?step", r"Adams[- ](Bashforth|Moulton)", r"predictor[- ]corrector"]),
   ("CA-16", "稳定性、精度与收敛性", "stability, accuracy and convergence", [r"truncation\s+error", r"order\s+of\s+accuracy", r"consisten(cy|t)", r"convergence\s+of\s+the\s+(scheme|method)", r"stability"]),
   ("CA-17", "绝对稳定性与长时间行为", "absolute stability, long time behavior", [r"absolute\s+stability", r"A[- ]stable", r"long[- ]time\s+behavio"]),
   ("CA-18", "刚性 ODE 的数值方法", "numerical methods for stiff ODE's", [r"\bstiff"]),
  ]),
  ("偏微分方程数值解（Numerical solutions of PDE）", [
   ("CA-19", "有限差分方法", "Finite difference method", [r"finite\s+differen"]),
   ("CA-20", "有限元方法", "finite element method", [r"finite\s+element", r"\bFEM\b"]),
   ("CA-21", "谱方法", "spectral method", [r"spectral\s+method", r"pseudospectral", r"Chebyshev", r"collocation"]),
   ("CA-22", "Lax 等价定理", "Lax equivalence theorem", [r"\bLax\b", r"equivalence\s+theorem"]),
  ]),
  ("数学建模、模拟与应用分析（Mathematical modeling, simulation, and applied analysis）", [
   ("CA-23", "数学建模、模拟与应用分析", "Mathematical modeling, simulation, and applied analysis", [r"model(ing|ling)?\b", r"simulat"]),
   ("CA-24", "尺度行为与渐近分析", "Scaling behavior and asymptotics analysis", [r"scaling\s+(law|behavio)", r"asymptot"]),
   ("CA-25", "驻相分析", "stationary phase analysis", [r"stationary\s+phase", r"steepest\s+descent", r"Laplace'?s?\s+method"]),
   ("CA-26", "边界层分析", "boundary layer analysis", [r"boundary\s+layer", r"matched\s+asymptot", r"singular\s+perturbation"]),
   ("CA-27", "模型的定性与定量分析", "qualitative and quantitative analysis of mathematical models", [r"qualitative", r"quantitative"]),
   ("CA-28", "Monte-Carlo 方法", "Monte-Carlo method", [r"Monte[- ]?Carlo"]),
  ]),
  ("线性与非线性规划（Linear and nonlinear programming）", [
   ("CA-29", "单纯形法", "Simplex method", [r"simplex"]),
   ("CA-30", "内点法", "interior method", [r"interior[- ]point", r"interior\s+method", r"barrier\s+method"]),
   ("CA-31", "罚函数法", "penalty method", [r"penalty"]),
   ("CA-32", "Newton 法（优化）", "Newton's method", [r"Newton'?s?\s+method"]),
   ("CA-33", "同伦方法与不动点方法", "homotopy method and fixed point method", [r"homotopy\s+method", r"continuation\s+method"]),
   ("CA-34", "动态规划", "dynamic programming", [r"dynamic\s+program"]),
  ]),
 ]),

 ("Geometry & Topology", "几何与拓扑（Geometry and Topology）", [
  ("微分几何：流形基础（Basics of smooth manifolds）", [
   ("GT-M1", "反函数定理", "Inverse function theorem", [r"inverse\s+function\s+theorem"]),
   ("GT-M2", "隐函数定理", "implicit function theorem", [r"implicit\s+function\s+theorem"]),
   ("GT-M3", "子流形", "submanifolds", [r"submanifold", r"embedded\s+manifold", r"immersed"]),
   ("GT-M4", "Sard 定理", "Sard's Theorem", [r"Sard"]),
   ("GT-M5", "嵌入定理", "embedding theorem", [r"embedding\s+theorem", r"Whitney\s+embedding", r"isometric\s+embedding"]),
   ("GT-M6", "横截性", "transversality", [r"transversal"]),
   ("GT-M7", "度理论", "degree theory", [r"degree\s+(theory|of\s+(a\s+)?(smooth\s+)?map)", r"\bdegree\b", r"winding\s+number"]),
   ("GT-M8", "流形上的积分", "integration on manifolds", [r"integrat\w*\s+on\s+(a\s+)?manifold", r"Stokes'?\s+theorem", r"volume\s+form"]),
  ]),
  ("微分几何：矩阵 Lie 群（Basics of matrix Lie groups）", [
   ("GT-L1", "GL(n)、SU(n)、SO(n)、U(n) 的定义", "The definitions of Gl(n), SU(n), SO(n), U(n)", [r"\b(GL|SL|SU|SO|U|O|PSU|PO)\s*\(\s*[n2-9]", r"\bSU\(2\)", r"\bSO\(3\)"]),
   ("GT-L2", "矩阵 Lie 群的流形结构", "their manifold structures", [r"matrix\s+Lie\s+group", r"matrix\s+group"]),
   ("GT-L3", "Lie 代数", "Lie algebras", [r"Lie\s+algebra"]),
   ("GT-L4", "左右不变向量场与微分形式", "right and left invariant vector fields and differential forms", [r"left[- ]invariant", r"right[- ]invariant", r"invariant\s+vector\s+field", r"Maurer[- ]Cartan"]),
   ("GT-L5", "指数映射", "the exponential map", [r"exponential\s+map"]),
  ]),
  ("微分几何：向量丛与联络（Vector bundles and connections）", [
   ("GT-V1", "实与复向量丛的定义", "Definition of real and complex vector bundles", [r"(real|complex)\s+vector\s+bundle", r"vector\s+bundle"]),
   ("GT-V2", "切丛与余切丛", "tangent and cotangent bundles", [r"tangent\s+bundle", r"cotangent\s+bundle", r"tangent\s+space"]),
   ("GT-V3", "丛上的基本运算（对偶、张量积、外积、直和、拉回）", "dual bundle, tensor products, exterior products, direct sums, pull-back bundles", [r"dual\s+bundle", r"exterior\s+power", r"direct\s+sum\s+of\s+bundle", r"tensor\s+product\s+of\s+bundle"]),
   ("GT-V4", "微分形式、外积、外微分", "Definition of differential forms, exterior product, exterior derivative", [r"differential\s+form", r"exterior\s+derivative", r"exterior\s+product", r"wedge\s+product"]),
   ("GT-V5", "de Rham 上同调", "de Rham cohomology", [r"de\s+Rham"]),
   ("GT-V6", "拉回下的行为", "behavior under pull-back", [r"pull[- ]?back"]),
   ("GT-V7", "向量丛上的度量", "Metrics on vector bundles", [r"metric\s+on\s+(a\s+)?(vector\s+)?bundle", r"Hermitian\s+metric"]),
  ]),
  ("微分几何：Riemann 几何（Riemannian geometry）", [
   ("GT-R1", "Riemann 度量", "Riemannian metrics", [r"Riemannian\s+metric", r"Riemann\s+metric", r"Riemannian\s+manifold"]),
   ("GT-R2", "测地线的定义", "definition of a geodesic", [r"geodesic"]),
   ("GT-R3", "测地线的存在性与唯一性", "existence and uniqueness of geodesics", [r"existence.{0,40}geodesic", r"geodesic.{0,40}exist"]),
   ("GT-R4", "矩阵群的主丛", "Definition of a principal Lie group bundle for matrix groups", [r"principal\s+(bundle|G[- ]bundle|Lie)"]),
   ("GT-R5", "相伴向量丛", "Associated vector bundles", [r"associated\s+(vector\s+)?bundle"]),
   ("GT-R6", "主丛与向量丛的关系", "Relation between principal bundles and vector bundles", [r"principal.{0,40}vector\s+bundle", r"vector\s+bundle.{0,40}principal"]),
   ("GT-R7", "协变导数与主丛上的联络", "covariant derivative for a vector bundle and connection on a principal bundle", [r"covariant\s+derivative", r"\bconnection\b"]),
   ("GT-R8", "两者的关系", "Relations between the two", [r"connection.{0,40}covariant", r"covariant.{0,40}connection"]),
   ("GT-R9", "曲率的定义", "Definition of curvature", [r"curvature"]),
   ("GT-R10", "平坦联络", "flat connections", [r"flat\s+connection", r"flatness"]),
   ("GT-R11", "平行移动", "parallel transport", [r"parallel\s+transport", r"parallel\s+translation"]),
   ("GT-R12", "Levi-Civita 联络", "Definition of Levi-Civita connection", [r"Levi[- ]Civita"]),
   ("GT-R13", "Riemann 曲率张量的性质", "properties of the Riemann curvature tensor", [r"Riemann\s+curvature", r"curvature\s+tensor", r"Ricci", r"sectional\s+curvature", r"scalar\s+curvature"]),
   ("GT-R14", "常曲率流形", "manifolds of constant curvature", [r"constant\s+curvature", r"space\s+form"]),
   ("GT-R15", "Jacobi 场", "Jacobi fields", [r"Jacobi\s+field"]),
   ("GT-R16", "测地线的第二变分", "second variation of geodesics", [r"second\s+variation", r"index\s+form", r"conjugate\s+point"]),
   ("GT-R17", "非正曲率流形", "Manifolds of nonpositive curvature", [r"non[- ]?positive\s+curvature", r"Hadamard"]),
   ("GT-R18", "正曲率流形", "manifolds of positive curvature", [r"positive\s+curvature", r"Myers", r"Synge"]),
  ]),
  ("代数拓扑（Algebraic Topology）", [
   ("GT-A1", "基本群", "Fundamental groups", [r"fundamental\s+group"]),
   ("GT-A2", "覆叠空间", "Covering spaces", [r"covering\s+(space|map)", r"universal\s+cover"]),
   ("GT-A3", "高阶同伦群", "Higher homotopy groups", [r"homotopy\s+group", r"\\pi_[nk]"]),
   ("GT-A4", "纤维化与纤维化的长正合列", "Fibrations and the long exact sequence of a fibration", [r"fibration", r"fiber\s+bundle", r"fibre\s+bundle", r"long\s+exact\s+sequence"]),
   ("GT-A5", "奇异同调与上同调", "Singular homology and cohomology", [r"singular\s+(homology|cohomology)", r"simplicial\s+(homology|cohomology)", r"\bhomology\b", r"cohomology"]),
   ("GT-A6", "相对同调", "Relative homology", [r"relative\s+homology", r"homology\s+of\s+the\s+pair"]),
   ("GT-A7", "CW 复形与 CW 复形的同调", "CW complexes and the homology of CW complexes", [r"CW\s+complex", r"cell\s+complex", r"attaching\s+map"]),
   ("GT-A8", "Mayer-Vietoris 序列", "Mayer-Vietoris sequence", [r"Mayer\s*[- ]\s*Vietoris"]),
   ("GT-A9", "万有系数定理", "Universal coefficient theorem", [r"universal\s+coefficient"]),
   ("GT-A10", "Kunneth 公式", "Kunneth formula", [r"K[uü]nneth"]),
   ("GT-A11", "Poincare 对偶", "Poincare duality", [r"Poincar[eé]\s+dual"]),
   ("GT-A12", "Lefschetz 不动点公式", "Lefschetz fixed point formula", [r"Lefschetz"]),
   ("GT-A13", "Hopf 指标定理", "Hopf index theorem", [r"Hopf"]),
   ("GT-A14", "Cech 上同调与 de Rham 上同调", "Cech cohomology and de Rham cohomology", [r"[Cc]ech"]),
   ("GT-A15", "奇异、Cech 与 de Rham 上同调的等价性", "Equivalence between singular, Cech and de Rham cohomology", [r"equivalen\w{0,30}(singular|[Cc]ech|de\s+Rham)", r"isomorph\w{0,30}(singular|[Cc]ech|de\s+Rham)"]),
  ]),
 ]),

 ("Probability & Statistics", "概率与统计（Probability and Statistics）", [
  ("概率论（Probability）", [
   ("PS-P1", "随机变量", "Random variable", [r"random\s+variable"]),
   ("PS-P2", "期望", "Expectation", [r"expectation", r"expected\s+value", r"\bE\[", r"\\mathbb\{E\}"]),
   ("PS-P3", "独立性", "Independence", [r"independen"]),
   ("PS-P4", "方差与协方差", "Variance and covariance", [r"variance", r"covariance"]),
   ("PS-P5", "相关", "correlation", [r"correlat"]),
   ("PS-P6", "矩", "moment", [r"\bmoments?\b", r"moment\s+generating"]),
   ("PS-P7", "各种分布函数", "Various distribution functions", [r"distribution\s+function", r"density\s+function", r"probability\s+density", r"\bcdf\b", r"\bpdf\b"]),
   ("PS-P8", "多元分布", "Multivariate distribution", [r"multivariate", r"joint\s+distribution", r"joint\s+density", r"random\s+vector"]),
   ("PS-P9", "特征函数", "Characteristic function", [r"characteristic\s+function"]),
   ("PS-P10", "母函数/生成函数", "Generating function", [r"generating\s+function"]),
   ("PS-P11", "随机变量各种收敛模式", "Various modes of convergence of random variables", [r"almost\s+sure", r"converge\w{0,4}\s+in\s+(probability|distribution|law|L)", r"convergence\s+in\s+(probability|distribution|law)", r"in\s+distribution", r"weak\s+convergence"]),
   ("PS-P12", "Bayes 公式", "Bayes formula", [r"Bayes"]),
   ("PS-P13", "条件概率", "Conditional probability", [r"conditional\s+probability"]),
   ("PS-P14", "给定 sigma-域的条件期望", "Conditional expectation given a sigma-field", [r"conditional\s+expectation", r"conditional\s+expect", r"sigma[- ]field", r"\b\sigma-algebra"]),
   ("PS-P15", "大数定律", "Laws of large numbers", [r"law\s+of\s+large\s+numbers", r"large\s+numbers"]),
   ("PS-P16", "中心极限定理", "Central limit theorems", [r"central\s+limit"]),
   ("PS-P17", "鞅", "Martingales", [r"martingale"]),
   ("PS-P18", "Markov 链", "Markov chains", [r"Markov\s+chain", r"Markov\s+process"]),
   ("PS-P19", "Poisson 过程的基本性质", "Basic properties of Poisson processes", [r"Poisson\s+process"]),
   ("PS-P20", "Brown 运动的基本性质", "Basic properties of Brownian motion", [r"Brownian", r"Wiener\s+process"]),
  ]),
  ("统计：分布理论与基本统计（Distribution Theory and Basic Statistics）", [
   ("PS-S1", "连续分布族 normal/chi-sq/t/F/gamma/beta", "Families of continuous distributions: normal, chi-sq, t, F, gamma, beta", [r"normal\s+distribution", r"Gaussian", r"chi[- ]?squar", r"Student'?s\s+t", r"\bt[- ]distribution", r"\bF[- ]distribution", r"gamma\s+distribution", r"beta\s+distribution"]),
   ("PS-S2", "离散分布族 multinomial/Poisson/negative binomial", "Families of discrete distributions: multinomial, Poisson, negative binomial", [r"multinomial", r"negative\s+binomial", r"binomial\s+distribution", r"Poisson\s+distribution"]),
   ("PS-S3", "基本统计量：样本均值、方差、中位数与分位数", "Basic statistics: sample mean, variance, median and quantiles", [r"sample\s+mean", r"sample\s+variance", r"\bmedian\b", r"quantile", r"order\s+statistic"]),
  ]),
  ("统计：检验（Testing）", [
   ("PS-T1", "Neyman-Pearson 范式", "Neyman-Pearson paradigm", [r"Neyman\s*[- ]\s*Pearson"]),
   ("PS-T2", "原假设与备择假设", "null and alternative hypotheses", [r"null\s+hypothesis", r"alternative\s+hypothesis", r"test\s+the\s+hypothesis", r"hypothesis\s+test"]),
   ("PS-T3", "简单与复合假设", "simple and composite hypotheses", [r"simple\s+hypothesis", r"composite\s+hypothesis"]),
   ("PS-T4", "第一类与第二类错误", "type I and type II errors", [r"type\s+I{1,2}\b", r"type\s+(I|II)\s+error", r"type\s+[12]\s+error"]),
   ("PS-T5", "功效", "power", [r"power\s+(of\s+(the\s+)?test|function)", r"\bpower\b.{0,20}test"]),
   ("PS-T6", "最大功效检验", "most powerful test", [r"most\s+powerful", r"\bUMP\b"]),
   ("PS-T7", "似然比检验", "likelihood ratio test", [r"likelihood\s+ratio"]),
   ("PS-T8", "Neyman-Pearson 定理", "Neyman-Pearson Theorem", [r"Neyman\s*[- ]\s*Pearson"]),
   ("PS-T9", "广义似然比检验", "generalized likelihood ratio test", [r"generalized\s+likelihood\s+ratio", r"\bGLRT\b"]),
  ]),
  ("统计：估计（Estimation）", [
   ("PS-E1", "参数估计", "Parameter estimation", [r"estimat"]),
   ("PS-E2", "矩方法", "method of moments", [r"method\s+of\s+moments"]),
   ("PS-E3", "极大似然估计", "maximum likelihood estimation", [r"maximum\s+likelihood", r"\bMLE\b"]),
   ("PS-E4", "估计量的评价准则", "criteria for evaluation of estimators", [r"unbiased", r"efficien", r"mean\s+squared\s+error", r"\bMSE\b"]),
   ("PS-E5", "Fisher 信息及其应用", "Fisher information and its use", [r"Fisher\s+information", r"information\s+matrix", r"Cram[eé]r\s*[- ]\s*Rao", r"information\s+inequality"]),
   ("PS-E6", "置信区间", "confidence interval", [r"confidence\s+(interval|region|set|level|bound)"]),
  ]),
  ("统计：Bayes 统计（Bayesian Statistics）", [
   ("PS-B1", "先验", "Prior", [r"\bpriors?\b"]),
   ("PS-B2", "后验", "posterior", [r"posterior"]),
   ("PS-B3", "共轭先验", "conjugate priors", [r"conjugate\s+prior"]),
   ("PS-B4", "Bayes 估计量", "Bayesian estimator", [r"Bayes\w*\s+estimat", r"Bayes\s+risk", r"posterior\s+mean"]),
  ]),
  ("统计：大样本性质（Large sample properties）", [
   ("PS-L1", "相合性", "Consistency", [r"consisten"]),
   ("PS-L2", "渐近正态性", "asymptotic normality", [r"asymptotic\w*\s+normal", r"asymptotically\s+normal"]),
   ("PS-L3", "似然比统计量的卡方近似", "chi-sq approximation to likelihood ratio statistic", [r"chi[- ]?squar"]),
  ]),
 ]),

 ("Mathematical Physics", "数学物理（Mathematical Physics，2022 年起设科）", [
  ("1. 经典力学（Classical mechanics）", [
   ("MP-1", "最小作用量原理", "principle of least action", [r"least\s+action", r"stationary\s+action", r"action\s+principle"]),
   ("MP-2", "Euler-Lagrange 方程", "Euler-Lagrangian equation", [r"Euler[- ]Lagrang"]),
   ("MP-3", "Noether 定理", "Noether theorem", [r"Noether"]),
   ("MP-4", "Kepler 问题", "Kepler problem", [r"Kepler"]),
   ("MP-5", "刚体", "rigid body", [r"rigid\s+body"]),
   ("MP-6", "Hamilton 方程", "Hamilton's equation", [r"Hamilton'?s?\s+equation", r"Hamiltonian"]),
   ("MP-7", "Poisson 括号", "Poisson bracket", [r"Poisson\s+bracket"]),
   ("MP-8", "Liouville 定理", "Liouville's theorem", [r"Liouville"]),
   ("MP-9", "正则变换", "canonical transformation", [r"canonical\s+transformation"]),
   ("MP-10", "Hamilton-Jacobi 理论", "Hamilton-Jacobi theory", [r"Hamilton[- ]Jacobi"]),
  ]),
  ("2. 电动力学（Electrodynamics）", [
   ("MP-11", "静电学与静磁学", "Electrostatics and magnetostatics", [r"electrostatic", r"magnetostatic"]),
   ("MP-12", "场、势、电荷", "fields, potentials, charges", [r"electric\s+field", r"magnetic\s+field", r"\bpotential\b", r"\bcharge\b"]),
   ("MP-13", "物质中的电场与磁场", "electric and magnetic fields in matter", [r"in\s+matter", r"dielectric", r"permittivity", r"permeability", r"polariz"]),
   ("MP-14", "Coulomb 定律", "Coulomb's law", [r"Coulomb"]),
   ("MP-15", "Lorentz 力定律", "Lorentz force law", [r"Lorentz"]),
   ("MP-16", "Ohm 定律", "Ohm's law", [r"Ohm"]),
   ("MP-17", "Faraday 定律", "Faraday's law", [r"Faraday"]),
   ("MP-18", "Gauss 定律", "Gauss's law", [r"Gauss'?s?\s+law"]),
   ("MP-19", "Maxwell 方程", "Maxwell's equation", [r"Maxwell"]),
   ("MP-20", "守恒律", "conservation laws", [r"conservation\s+law", r"conserved\s+(current|charge|quantity)", r"conservation\s+of"]),
   ("MP-21", "电磁波", "electromagnetic waves", [r"electromagnetic\s+wave", r"\bEM\s+wave"]),
   ("MP-22", "辐射", "radiation", [r"radiat"]),
   ("MP-23", "镜像法", "the method of images", [r"method\s+of\s+images"]),
   ("MP-24", "分离变量法", "separation of variables", [r"separation\s+of\s+variables"]),
   ("MP-25", "多极展开", "multipole expansion", [r"multipole"]),
  ]),
  ("3. 热力学与统计物理（Thermodynamics and statistical physics）", [
   ("MP-26", "热力学基本原理", "Fundamental principles of thermodynamics", [r"first\s+law", r"second\s+law", r"third\s+law", r"zeroth\s+law", r"thermodynamic\s+law"]),
   ("MP-27", "热力学势与过程", "thermodynamic potentials and processes", [r"thermodynamic\s+potential", r"free\s+energy", r"enthalpy", r"Helmholtz", r"Gibbs", r"adiabatic", r"isothermal"]),
   ("MP-28", "相平衡与相变", "phase equilibrium and phase transitions", [r"phase\s+(transition|equilibrium)", r"critical\s+temperature", r"Clausius[- ]Clapeyron"]),
   ("MP-29", "配分函数", "partition function", [r"partition\s+function"]),
   ("MP-30", "熵", "entropy", [r"entropy"]),
   ("MP-31", "概率论（统计物理）", "Probability theory", [r"probabilit"]),
   ("MP-32", "微正则、正则与巨正则系综", "microcanonical, canonical and grand-canonical ensembles", [r"microcanonical", r"canonical\s+ensemble", r"grand[- ]canonical", r"ensemble"]),
   ("MP-33", "Boltzmann、Bose 与 Fermi 统计分布", "The Boltzmann, Bose and Fermi statistical distributions", [r"Boltzmann", r"Bose\s*[-–]\s*Einstein", r"Fermi\s*[-–]\s*Dirac", r"Bose\s+distribution", r"Fermi\s+distribution"]),
   ("MP-34", "实例：理想气体模型", "ideal gas model", [r"ideal\s+gas"]),
   ("MP-35", "实例：顺磁体", "paramagnet", [r"paramagnet"]),
   ("MP-36", "实例：理想量子气体", "ideal quantum gases", [r"quantum\s+gas", r"photon\s+gas"]),
   ("MP-37", "实例：退化 Fermi 系统", "degenerate Fermi systems", [r"degenerate\s+Fermi", r"Fermi\s+(energy|sea|surface|gas|momentum)"]),
   ("MP-38", "实例：光子与声子", "photons and phonons", [r"photon", r"phonon"]),
   ("MP-39", "实例：Bose-Einstein 凝聚", "Bose-Einstein condensation", [r"Bose\s*[-–]\s*Einstein\s+condens"]),
  ]),
  ("4. 量子力学（Quantum mechanics）", [
   ("MP-40", "Hilbert 空间、态、可观测量、波函数", "Hilbert space, states, observables, wave functions", [r"Hilbert\s+space", r"wave\s+function", r"observable", r"state\s+vector"]),
   ("MP-41", "Schrodinger 方程", "Schrodinger equation", [r"Schr[oö]dinger"]),
   ("MP-42", "Schrodinger 与 Heisenberg 绘景", "Schrodinger and Heisenberg pictures", [r"Heisenberg\s+picture", r"Schr[oö]dinger\s+picture", r"interaction\s+picture"]),
   ("MP-43", "正则量子化", "canonical quantization", [r"canonical\s+quantization"]),
   ("MP-44", "密度矩阵", "density matrix", [r"density\s+matrix", r"density\s+operator"]),
   ("MP-45", "实例：谐振子", "harmonic oscillator", [r"harmonic\s+oscillator"]),
   ("MP-46", "实例：氢原子模型", "hydrogen atom model", [r"hydrogen\s+atom", r"hydrogen"]),
   ("MP-47", "实例：势阱问题", "potential well problems", [r"potential\s+well", r"infinite\s+well", r"square\s+well", r"delta\s+potential"]),
   ("MP-48", "量子力学中的对称性", "Symmetry in quantum mechanics", [r"symmetr"]),
   ("MP-49", "角动量", "angular momentum", [r"angular\s+momentum"]),
   ("MP-50", "自旋", "spin", [r"\bspin"]),
   ("MP-51", "全同粒子", "identical particles", [r"identical\s+particle", r"indistinguishable"]),
   ("MP-52", "原子结构", "atomic structure", [r"atomic\s+structure", r"fine\s+structure", r"hydrogen\s+spectrum"]),
   ("MP-53", "微扰论", "Perturbation theory", [r"perturbation\s+theory", r"perturbative", r"perturbation\s+expansion"]),
   ("MP-54", "散射", "scattering", [r"scatter"]),
   ("MP-55", "近似方法", "approximation method", [r"variational\s+method", r"\bWKB\b", r"semiclassical", r"approximation\s+method"]),
  ]),
  ("5. 广义相对论（General relativity）", [
   ("MP-56", "微分几何：度量、向量、张量、微分形式、流形、联络、曲率、测地线", "metric, vector, tensor, differential forms, manifold, connections, curvature, geodesic", [r"\bmetric\b", r"\btensor\b", r"manifold", r"\bconnection\b", r"curvature", r"geodesic", r"differential\s+form"]),
   ("MP-57", "标架、Lie 导数、等距与 Killing 向量", "tetrads, Lie derivatives, isometries and Killing vectors", [r"tetrad", r"Vierbein", r"Lie\s+derivative", r"Killing", r"isometr"]),
   ("MP-58", "等效原理", "the principle of equivalence", [r"equivalence\s+principle"]),
   ("MP-59", "Einstein 方程", "Einstein's equation", [r"Einstein'?s?\s+(field\s+)?equation"]),
   ("MP-60", "Hilbert-Einstein 作用量", "Hilbert-Einstein action", [r"Einstein\s*[-–]\s*Hilbert"]),
   ("MP-61", "精确解：Minkowski、de Sitter、anti-de Sitter 时空", "Minkowski, de Sitter, anti-de Sitter spacetimes", [r"Minkowski", r"de\s+Sitter", r"anti[- ]de\s+Sitter"]),
   ("MP-62", "黑洞解", "black hole solutions", [r"black\s+hole", r"Schwarzschild", r"\bKerr\b", r"Reissner"]),
   ("MP-63", "因果结构", "Causal structure", [r"causal", r"causality", r"event\s+horizon", r"light\s+cone"]),
  ]),
  ("6. 量子场论（Quantum field theory）", [
   ("MP-64", "经典场论：Lagrange 与 Hamilton 形式", "Classical field theory: Lagrangian and Hamiltonian formalism", [r"classical\s+field\s+theory", r"field\s+Lagrangian", r"Lagrangian\s+density"]),
   ("MP-65", "Noether 定理（场论）", "Noether's theorem", [r"Noether"]),
   ("MP-66", "量子化：正则量子化与路径积分", "canonical quantization and path integrals", [r"path\s+integral", r"functional\s+integral"]),
   ("MP-67", "费米子：Poincare 群的表示", "representations of Poincare group", [r"Poincar[eé]\s+group"]),
   ("MP-68", "Dirac 方程", "Dirac equation", [r"Dirac"]),
   ("MP-69", "S-矩阵：LSZ 约化", "LSZ reduction", [r"\bLSZ\b"]),
   ("MP-70", "Feynman 传播子", "Feymann propagator", [r"propagator"]),
   ("MP-71", "Feynman 规则", "Feymann rules", [r"Feynman\s+(rule|diagram)"]),
   ("MP-72", "正规序", "normal ordering", [r"normal\s+order"]),
   ("MP-73", "Wick 定理", "Wick's theorem", [r"\bWick\b"]),
   ("MP-74", "光学定理", "the optical theorem", [r"optical\s+theorem"]),
   ("MP-75", "定域性", "locality", [r"localit", r"local\s+quantum\s+field"]),
   ("MP-76", "重整化：正则化与截断", "regularization and cutoff", [r"regulariz", r"cut[- ]?off"]),
   ("MP-77", "重整化：抵消项", "counter terms", [r"counter\s*[- ]?\s*term"]),
   ("MP-78", "重整化群", "renormalization group", [r"renormaliz"]),
  ]),
 ]),
]

# ---------------------------------------------------------------------------
# 2) 超纲候选：考纲未写、但可能在真题里反复出现的考点
# ---------------------------------------------------------------------------
OUT_OF_SYLLABUS = {
 "Algebra & Number Theory": [
  ("线性代数与矩阵论（特征值/秩/迹/矩阵分解）", [r"eigenvalue", r"eigenvector", r"\brank\b", r"\btrace\b", r"\bmatrix\b", r"linear\s+(map|transformation|operator)", r"vector\s+space", r"diagonaliz"]),
  ("有限群的分类、阶与正规子群（群论基本功）", [r"group\s+of\s+order", r"simple\s+group", r"normal\s+subgroup", r"quotient\s+group", r"symmetric\s+group", r"alternating\s+group", r"\bcyclic\s+group", r"automorphism", r"center\s+of\s+(the\s+)?group", r"\bA_n\b", r"\bS_n\b"]),
  ("群作用、轨道与 Burnside 引理", [r"group\s+action", r"\borbit", r"stabilizer", r"Burnside"]),
  ("域扩张的代数性与次数", [r"algebraic\s+extension", r"transcendental", r"minimal\s+polynomial", r"degree\s+of\s+(the\s+)?extension"]),
  ("模与 Noether 环结构", [r"\bmodule\b", r"Noetherian", r"Artinian", r"composition\s+series", r"finitely\s+generated"]),
  ("范畴与函子", [r"\bcategor", r"functor", r"natural\s+transformation", r"adjoint"]),
  ("代数几何初步（簇、Scheme、层）", [r"algebraic\s+variet", r"\bscheme", r"algebraic\s+set", r"projective\s+space"]),
  ("计算数论（RSA/原根/离散对数/中国剩余）", [r"\bRSA\b", r"primitive\s+root", r"discrete\s+log", r"totient", r"Chinese\s+remainder", r"Euler'?s\s+(phi|function)"]),
  ("组合数学（考纲标题含 Combinatorics，但正文无对应条目）", [r"combinat", r"counting", r"graph\s+theor", r"pigeonhole", r"\bgraph\b", r"colour", r"color"]),
 ],
 "Analysis & PDE": [
  ("不等式的证明与估计技巧", [r"inequalit"]),
  ("数列、级数与极限运算", [r"sequence\s+of", r"infinite\s+series", r"series\s+converge", r"limit\s+of\s+the\s+sequence"]),
  ("函数方程与迭代", [r"functional\s+equation", r"iteration\s+of"]),
  ("凸性与凸分析", [r"convex"]),
  ("动力系统、分支与混沌", [r"dynamical\s+system", r"bifurcation", r"chaos", r"periodic\s+orbit"]),
  ("调和分析（Hardy-Littlewood / 插值定理）", [r"harmonic\s+analysis", r"Hardy", r"Littlewood", r"interpolation\s+theorem", r"maximal\s+function"]),
  ("复动力系统（Julia/Fatou 集）", [r"Julia\s+set", r"Mandelbrot", r"Fatou"]),
  ("解析数论（PNT / L 函数 / Riemann 假设）", [r"prime\s+number\s+theorem", r"Dirichlet\s+L", r"Riemann\s+hypothesis", r"analytic\s+number\s+theory"]),
  ("线性算子谱与紧性（泛函分析进阶）", [r"Banach\s+space", r"operator\s+norm", r"weak\s+topology", r"reflexive", r"Banach\s+algebra"]),
 ],
 "Computational & Applied": [
  ("数值线性代数算法（LU/QR/Cholesky/Gram-Schmidt）", [r"\bLU\b", r"\bQR\b", r"Cholesky", r"Gram[- ]Schmidt", r"Householder", r"Gaussian\s+elimination", r"Givens"]),
  ("误差分析与浮点运算", [r"round[- ]off", r"floating[- ]point", r"machine\s+epsilon", r"backward\s+error", r"error\s+(analysis|bound|estimate)"]),
  ("算法复杂度与计算量", [r"complexity", r"O\(n", r"computational\s+cost", r"operation\s+count"]),
  ("图论与网络优化", [r"\bgraph\b", r"network\s+flow", r"shortest\s+path", r"matching", r"traveling\s+salesman"]),
  ("纯数学式线性代数（矩阵/向量空间）", [r"\bmatrix\b", r"\bmatrices\b", r"eigenvalue", r"rank\s+of", r"determinant", r"linear\s+algebra"]),
  ("概率/统计方法在应用数学中的使用", [r"random\s+variable", r"probabilit", r"expectation"]),
  ("数值实验与编程", [r"MATLAB", r"write\s+a\s+program", r"\bcode\b", r"computer\s+program"]),
 ],
 "Geometry & Topology": [
  ("代数几何（簇、除子、层与上同调）", [r"algebraic\s+variet", r"\bscheme", r"\bdivisor", r"sheaf", r"coherent", r"blow[- ]up"]),
  ("复几何与 Kaehler 几何", [r"K[aä]hler", r"complex\s+manifold", r"Hermitian", r"holomorphic\s+(bundle|vector)"]),
  ("辛几何与 Poisson 几何", [r"symplectic", r"moment\s+map", r"Poisson\s+manifold"]),
  ("示性类（Chern / Stiefel-Whitney / Pontryagin）", [r"Chern", r"characteristic\s+class", r"Stiefel[- ]Whitney", r"Pontryagin", r"Euler\s+class"]),
  ("点集拓扑基础（紧性/连通性/分离公理）", [r"compact(ness)?", r"Hausdorff", r"connected", r"topological\s+space", r"homeomorph", r"separation\s+axiom", r"open\s+set"]),
  ("经典曲线曲面论（第一/第二基本形式）", [r"first\s+fundamental\s+form", r"second\s+fundamental\s+form", r"mean\s+curvature", r"Gauss\s+curvature"]),
  ("Euler 示性数与 Betti 数", [r"Euler\s+characteristic", r"Betti", r"Euler\s+number"]),
  ("不动点定理与度理论应用（Brouwer / Borsuk-Ulam）", [r"Brouwer", r"Borsuk[- ]Ulam", r"fixed\s+point\s+theorem"]),
  ("群作用与等变拓扑", [r"group\s+action", r"equivariant", r"\bG[- ]bundle"]),
  ("三维流形与纽结", [r"three[- ]manifold", r"3[- ]manifold", r"\bknot", r"Heegaard", r"Dehn", r"handlebody"]),
  ("度规与测地线的具体计算（微分几何习题化）", [r"first\s+variation", r"minimal\s+surface", r"isometric\s+immersion"]),
 ],
 "Probability & Statistics": [
  ("概率不等式与集中不等式", [r"inequalit", r"Chernoff", r"Hoeffding", r"concentration", r"Chebyshev", r"Markov'?s\s+inequality", r"Jensen"]),
  ("随机游走与分支过程", [r"random\s+walk", r"branching\s+process", r"Galton"]),
  ("停时与可选停时定理", [r"stopping\s+time", r"optional\s+stopping", r"hitting\s+time"]),
  ("次序统计量与充分统计量", [r"order\s+statistic", r"sufficient\s+statistic", r"Rao[- ]Blackwell", r"complete\s+statistic", r"minimal\s+sufficient"]),
  ("回归与线性模型", [r"regression", r"linear\s+model", r"\bANOVA", r"least\s+squares\s+estimat", r"design\s+matrix"]),
  ("非参数与重抽样方法", [r"bootstrap", r"nonparametr", r"kernel\s+density", r"U[- ]statistic", r"empirical\s+distribution"]),
  ("随机过程进阶（平稳分布/耦合/遍历）", [r"stationary\s+distribution", r"coupling", r"ergodic", r"renewal", r"queue", r"birth[- ]and[- ]death"]),
  ("组合概率与离散模型", [r"combinatorial\s+probability", r"\burn\b", r"balls?\s+(and|into)\s+bins", r"\bdice\b", r"coin\s+(toss|flip)", r"\bdeck\s+of\s+cards"]),
  ("信息论与熵", [r"Kullback", r"information\s+theory", r"Shannon", r"differential\s+entropy"]),
 ],
 "Mathematical Physics": [
  ("凝聚态与多体模型（Ising / spin chain / Hubbard）", [r"Ising", r"\bXY\s+model", r"Heisenberg\s+model", r"Hubbard", r"Bethe\s+ansatz", r"spin\s+chain", r"tight[- ]binding", r"Landau\s+level"]),
  ("量子信息（纠缠 / Bell / qubit）", [r"entangle", r"Bell\s+inequality", r"qubit", r"von\s+Neumann\s+entropy", r"CHSH"]),
  ("拓扑物态与 Berry 相位", [r"topological\s+insulator", r"Berry\s+phase", r"Aharonov[- ]Bohm", r"Chern\s+number", r"geometric\s+phase"]),
  ("共形场论 / 弦论 / 全息", [r"conformal\s+field\s+theory", r"\bCFT\b", r"string\s+theory", r"AdS/CFT", r"holograph"]),
  ("超对称", [r"supersymmetr", r"\bSUSY\b", r"supergravity", r"supercharge"]),
  ("场论进阶（瞬子 / 反常 / theta 真空）", [r"instanton", r"anomal", r"theta\s+vacuum", r"soliton", r"monopole"]),
  ("等离子体/流体力学等连续介质", [r"fluid", r"Navier[- ]Stokes", r"plasma", r"magnetohydrodynamic"]),
  ("数值与计算手段", [r"numerical", r"Monte[- ]?Carlo", r"simulat"]),
 ],
}

# ---------------------------------------------------------------------------
# PDF 抽取噪声：重音被拆成独立字符（Poincar´e）、行尾连字符断词（prob- ability）
ACCENTS = {"\u00b4": "", "\u0301": "", "\u00a8": "", "\u02bc": ""}
FOLD = {"\u00f6": "o", "\u00e9": "e", "\u00e8": "e", "\u00ea": "e", "\u00fc": "u",
        "\u00e4": "a", "\u00e1": "a", "\u00e0": "a", "\u00ed": "i", "\u00f3": "o",
        "\u00fa": "u", "\u00f1": "n", "\u00e7": "c", "\u00e2": "a", "\u00ee": "i",
        "\u00f4": "o", "\u00fb": "u", "\u00e7": "c", "\u00df": "ss"}

def norm(t):
    return t.replace("\u00a0", " ")

def variants(t):
    """返回同一题面的多个等价文本变体，任一命中即算命中。"""
    t = norm(t)
    out = [t]
    t2 = t
    for k, v in ACCENTS.items():
        t2 = t2.replace(k, v)
    for k, v in FOLD.items():
        t2 = t2.replace(k, v)
    t2 = t2.replace("\u2019", "'").replace("\u2018", "'").replace("\u2013", "-").replace("\u2014", "-")
    out.append(t2)
    # 断词连字符：prob- ability -> probability；同时保留 well-posed 形态
    out.append(re.sub(r"-\s*\n\s*", "", t2))
    out.append(re.sub(r"-\s*\n\s*", "-", t2))
    return out

def main():
    with open(PROBLEMS, encoding="utf-8") as f:
        probs = json.load(f)
    for p in probs:
        p["_y"] = int(p["year"])
        p["_v"] = variants(norm(p["text"]))

    by_subject = collections.defaultdict(list)
    for p in probs:
        by_subject[p["subject"]].append(p)

    total_recent = collections.Counter()
    total_early = collections.Counter()
    for s, ps in by_subject.items():
        for p in ps:
            if p["_y"] >= RECENT_FROM:
                total_recent[s] += 1
            else:
                total_early[s] += 1

    result = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "source_problems": PROBLEMS,
        "n_problems": len(probs),
        "recent_window": "2022-2026",
        "early_window": "2010-2021",
        "status_rule": "高频命中 >= 8 题；偶发命中 1-7 题；零命中 0 题",
        "subjects": {},
        "out_of_syllabus": {},
    }

    for subject, subject_cn, sections in SYLLABUS:
        ps = by_subject.get(subject, [])
        entries_out = []
        for section_cn, entries in sections:
            for eid, cn, en, pats in entries:
                regs = [re.compile(p, re.IGNORECASE) for p in pats]
                hits, years, examples = [], collections.Counter(), []
                for p in ps:
                    if any(r.search(v) for v in p["_v"] for r in regs):
                        hits.append(p)
                        years[p["_y"]] += 1
                        if len(examples) < 3:
                            examples.append(p["paper"] + "#" + str(p["n"]))
                n = len(hits)
                n_recent = sum(1 for p in hits if p["_y"] >= RECENT_FROM)
                n_early = n - n_recent
                status = "高频命中" if n >= 8 else ("偶发命中" if n >= 1 else "零命中")
                # 趋势
                if n == 0:
                    trend = "从未考过"
                    mult = 1.0
                elif total_early[subject] == 0:
                    trend = "n/a（该科目无早期样本）"
                    mult = 1.0
                elif n_early == 0 and n_recent > 0:
                    trend = "新兴（仅近五年出现）"
                    mult = 1.5
                elif n_recent == 0 and n_early > 0:
                    trend = "已消失（近五年未考）"
                    mult = 0.4
                else:
                    r_recent = n_recent / total_recent[subject]
                    r_early = n_early / total_early[subject]
                    ratio = r_recent / r_early if r_early > 0 else 99.0
                    if ratio >= 1.5:
                        trend = "上升"
                        mult = 1.4
                    elif ratio < 0.67:
                        trend = "下降"
                        mult = 0.75
                    else:
                        trend = "平稳"
                        mult = 1.0
                n_sub = len(ps)
                dens = (n / n_sub) if n_sub else 0.0          # 科目内命中密度
                score_raw = round(n * mult, 2)                 # 命中题数 x 趋势
                score = round(dens * 100 * mult, 2)            # 密度(%) x 趋势 -> 跨科目可比
                if n == 0:
                    prio = "D 零命中（战略性放弃候选）"
                elif score >= 12:
                    prio = "A 最高优先"
                elif score >= 4:
                    prio = "B 高优先"
                else:
                    prio = "C 一般优先"
                entries_out.append({
                    "id": eid, "section": section_cn, "cn": cn, "en": en,
                    "patterns": pats,
                    "hits": n, "hits_recent": n_recent, "hits_early": n_early,
                    "year_hist": dict(sorted(years.items())),
                    "status": status, "trend": trend, "trend_mult": mult,
                    "density_pct": round(dens * 100, 2),
                    "score_raw": score_raw,
                    "priority_score": score, "priority": prio,
                    "examples": examples,
                })
        nzero = sum(1 for e in entries_out if e["hits"] == 0)
        nhigh = sum(1 for e in entries_out if e["hits"] >= 8)
        nmid = sum(1 for e in entries_out if 1 <= e["hits"] < 8)
        result["subjects"][subject] = {
            "subject_cn": subject_cn,
            "n_problems": len(ps),
            "n_problems_recent": total_recent[subject],
            "n_problems_early": total_early[subject],
            "n_entries": len(entries_out),
            "n_high": nhigh, "n_mid": nmid, "n_zero": nzero,
            "entries": entries_out,
        }

    # 超纲
    for subject, cands in OUT_OF_SYLLABUS.items():
        ps = by_subject.get(subject, [])
        syl_pats = []
        for _s, _scn, secs in SYLLABUS:
            if _s != subject:
                continue
            for _sec, ents in secs:
                for _eid, _cn, _en, pats in ents:
                    syl_pats.extend(pats)
        syl_regs = [re.compile(p, re.IGNORECASE) for p in syl_pats]
        rows = []
        for label, pats in cands:
            regs = [re.compile(p, re.IGNORECASE) for p in pats]
            hits, years, ex = [], collections.Counter(), []
            for p in ps:
                if any(r.search(v) for v in p["_v"] for r in regs):
                    hits.append(p)
                    years[p["_y"]] += 1
                    if len(ex) < 3:
                        ex.append(p["paper"] + "#" + str(p["n"]))
            # 该候选是否被任何考纲条目覆盖
            covered = any(any(r.search(v) for v in h["_v"] for r in syl_regs) for h in hits) if hits else False
            rows.append({
                "label": label, "hits": len(hits),
                "hits_recent": sum(1 for h in hits if h["_y"] >= RECENT_FROM),
                "year_hist": dict(sorted(years.items())),
                "examples": ex,
                "shares_text_with_syllabus_hits": covered,
            })
        rows.sort(key=lambda r: -r["hits"])
        result["out_of_syllabus"][subject] = rows

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)

    print("wrote", OUT)
    print("total problems", len(probs))
    for s, v in result["subjects"].items():
        print("%-28s entries=%-4d high=%-3d mid=%-3d ZERO=%-3d  (probs=%d, recent=%d)" % (
            s, v["n_entries"], v["n_high"], v["n_mid"], v["n_zero"], v["n_problems"], v["n_problems_recent"]))
    print()
    for s, rows in result["out_of_syllabus"].items():
        print("== OUT-OF-SYLLABUS", s)
        for r in rows[:12]:
            print("   %-58s %3d (recent %d)" % (r["label"][:58], r["hits"], r["hits_recent"]))

if __name__ == "__main__":
    main()
