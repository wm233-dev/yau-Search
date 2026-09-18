
# -*- coding: utf-8 -*-
import json, collections, os, sys
BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
d = json.load(open(os.path.join(BASE,'data','problems_full.json'), encoding='utf-8'))
ap = [x for x in d if x.get('subject') == 'Analysis & PDE']
valid = set((x['year'], x['kind'], x['n']) for x in ap)

def M(i,k,n): return (i,k,n)

MOTHERS = [
("AP-M01","Schwarz–Pick 型定量刚性：D→D 全纯函数被双曲距离压缩，零点越多估计越强、等号即自同构",
 [M("2010","individual",3),M("2010","team",1),M("2013","team",1),M("2017","team",3)],"升要求"),
("AP-M02","全纯自映射/自同构的刚性：局部数据（取值点、导数、迭代关系）唯一决定映射",
 [M("2012","team",2),M("2015","team",4),M("2022","individual",2)],"换皮"),
("AP-M03","圆盘到自身的边界对应与有限 Blaschke 乘积（分类 + 保弧长测度）",
 [M("2015","individual",4),M("2020","individual",6)],"升要求"),
("AP-M04","Poisson 核与调和函数 Dirichlet 问题的显式解（半平面、半空间、右半平面）",
 [M("2010","individual",4),M("2012","individual",6),M("2014","individual",4)],"换皮"),
("AP-M05","基本解与 Green 函数：Newton 位势、−Δf=g 与 Green 函数的对称性",
 [M("2018","individual",5),M("2018","team",5)],"换皮"),
("AP-M06","调和/次调和函数的结构定理：平均值性质、极值原理、Harnack、旋转对称化",
 [M("2010","team",6),M("2014","team",5),M("2017","individual",5),M("2017","team",5)],"换皮"),
("AP-M07","正调和函数的 Liouville 型结构定理：增长/正性限制 ⇒ 常数或显式基本解",
 [M("2013","individual",4),M("2018","individual",6),M("2019","individual",3),M("2021","individual",1),M("2022","individual",5)],"升要求"),
("AP-M08","椭圆方程 Δu=f 的先验估计：L² 能量估计、Schauder C^{2,α} 估计、小性 ⇒ 梯度界",
 [M("2015","team",6),M("2019","team",2),M("2020","individual",3)],"升要求"),
("AP-M09","最优常数型 Sobolev 不等式：Poincaré、Hardy、Gagliardo–Nirenberg",
 [M("2017","individual",6),M("2019","individual",2),M("2025","individual",2)],"升要求"),
("AP-M10","非线性椭圆方程的可解性：单调算子/小扰动/Lax–Milgram 给存在唯一性",
 [M("2019","individual",5),M("2021","individual",6),M("2024","individual",2)],"升要求"),
("AP-M11","热核与热方程的显式解及逐点/整体估计",
 [M("2016","team",6),M("2024","individual",4),M("2026","individual",5)],"升要求"),
("AP-M12","发展方程解的支集传播与点态先验界（能量法 / 抛物极值原理）",
 [M("2019","team",5),M("2023","individual",6)],"换皮"),
("AP-M13","紧算子与紧嵌入的判定：积分算子、Sobolev 嵌入、限制算子",
 [M("2010","individual",5),M("2011","individual",6),M("2011","team",1),M("2013","individual",5),M("2017","team",6)],"换皮"),
("AP-M14","Fredholm 二择一：紧扰动下核与余核有限维、像闭",
 [M("2015","individual",5),M("2015","team",5)],"原样重复"),
("AP-M15","自伴算子的谱结构：谱为实轴上的闭有界集；紧自伴算子的谱定理",
 [M("2013","team",5),M("2016","individual",6)],"换皮"),
("AP-M16","无特征值的紧算子（Volterra 型、加权移位）：谱的计算",
 [M("2012","team",6),M("2016","team",5)],"换皮"),
("AP-M17","弱收敛与范数收敛的关系：弱+范数 ⇒ 强；弱极限的计算",
 [M("2015","individual",1),M("2017","individual",2),M("2018","individual",1),M("2023","individual",4)],"升要求"),
("AP-M18","L^p 收敛 ⇒ 依测度收敛 / 几乎处处收敛子列",
 [M("2016","team",2),M("2018","team",1)],"换皮"),
("AP-M19","Hilbert 空间的正交基与 L² 中全纯子空间的完备性（Hardy/Bergman）",
 [M("2011","team",1),M("2012","team",5),M("2014","individual",6)],"升要求"),
("AP-M20","整函数的增长限制 ⇒ 刚性：增长界逼出多项式或恒零",
 [M("2015","individual",3),M("2020","individual",4),M("2023","individual",5)],"换皮"),
("AP-M21","用留数定理计算实积分（含 log 与分数幂的多值积分）",
 [M("2011","individual",1),M("2012","individual",2),M("2014","team",2),M("2016","individual",4)],"换皮"),
("AP-M22","留数与辐角原理的结构性推论：零点-极点计数、部分分式恒等式",
 [M("2013","individual",2),M("2016","individual",5)],"换皮"),
("AP-M23","区域到单位圆盘的显式共形映射（初等函数的几何构造）",
 [M("2011","individual",3),M("2012","individual",2),M("2016","individual",4),M("2017","individual",4)],"换皮"),
("AP-M24","单值化障碍与绕数：解析函数的周期、单值分支与原函数的存在性",
 [M("2014","individual",3),M("2017","team",4),M("2019","individual",4),M("2025","individual",4)],"升要求"),
("AP-M25","矩阵指数：指数映射的乘法公式、BCH 一阶/二阶项与交换性判别",
 [M("2011","team",5),M("2023","individual",1),M("2026","individual",2)],"升要求"),
("AP-M26","凸性与 Jensen 型不等式（含等号刻画）",
 [M("2010","individual",1),M("2019","individual",1),M("2019","individual",2)],"换皮"),
("AP-M27","一维导数插值不等式与 Sobolev 嵌入（Landau–Kolmogorov 型）",
 [M("2010","team",2),M("2011","individual",4),M("2012","individual",3),M("2015","individual",6)],"升要求"),
("AP-M28","磨光与逼近恒等式的收敛性（f∗φ_ε → f）",
 [M("2014","team",6),M("2016","individual",2),M("2020","individual",1),M("2021","individual",3)],"换皮"),
("AP-M29","对偶空间的范数等式与正线性泛函的 Riesz 表示",
 [M("2011","individual",5),M("2012","individual",5)],"换皮"),
("AP-M30","零化子判据：由积分恒等式或 Fourier 侧信息的缺失推出 f≡0",
 [M("2015","individual",2),M("2015","team",1),M("2018","team",2)],"换皮"),
("AP-M31","分布的层饼公式与可积性判据（level set 方法）",
 [M("2012","individual",4),M("2012","team",4),M("2013","individual",1)],"换皮"),
("AP-M32","正测度集合的加法结构：Steinhaus 定理与算术级数",
 [M("2021","individual",3),M("2022","individual",3)],"升要求"),
("AP-M33","一致收敛极限的正则性：Weierstrass 定理及其调和函数版本",
 [M("2016","team",3),M("2018","individual",3)],"换皮"),
("AP-M34","连续点集的结构与 Riemann 可积性（不连续点集的测度）",
 [M("2010","individual",2),M("2016","individual",3)],"换皮"),
("AP-M35","Cantor 型构造：测度为零但不可数（或很大的）集合",
 [M("2011","team",4),M("2012","team",3)],"换皮"),
("AP-M36","单调函数与绝对连续函数：牛顿–莱布尼茨公式、弱导数与间断点集",
 [M("2013","team",2),M("2014","team",2),M("2016","individual",1),M("2017","team",2)],"升要求"),
("AP-M37","平移连续性、Lebesgue 微分定理与极大函数型 L¹ 界",
 [M("2010","team",4),M("2015","team",2),M("2018","team",3)],"换皮"),
("AP-M38","Gauss 型与振荡型积分的计算（多元 Gauss、Fresnel、signature）",
 [M("2010","individual",1),M("2010","individual",2),M("2012","team",1),M("2012","team",2),M("2013","individual",6)],"升要求"),
("AP-M39","Fourier 级数：系数衰减 ⇔ 光滑性，以及收敛性与唯一性",
 [M("2010","team",5),M("2017","individual",1),M("2017","team",1),M("2020","individual",2)],"升要求"),
("AP-M40","Fourier 变换下的双线性估计与卷积算子的 Fourier 化",
 [M("2024","individual",3),M("2024","individual",5)],"换皮"),
("AP-M41","不确定性原理：函数与其 Fourier 变换不能同时局化",
 [M("2014","individual",5),M("2019","team",1)],"换皮"),
("AP-M42","常微分方程的不动点方法：稳定性、周期解与 shooting",
 [M("2010","individual",6),M("2010","team",3),M("2011","team",2),M("2022","individual",6),M("2023","individual",2)],"升要求"),
("AP-M43","初值/边值问题的显式求解（常系数、Euler 型、一阶拟线性 PDE 的特征线法）",
 [M("2011","individual",2),M("2011","team",3),M("2025","individual",1)],"换皮"),
("AP-M44","向量分析与散度定理的应用：Helmholtz 分解、立体角积分",
 [M("2013","team",4),M("2016","team",1)],"换皮"),
("AP-M45","保测变换：Poincaré 回复性与不变集的严格化",
 [M("2014","team",4),M("2019","team",3)],"换皮"),
("AP-M46","函数方程与近似可加性（Cauchy 方程及其稳定性）",
 [M("2011","individual",1),M("2014","individual",1)],"换皮"),
("AP-M47","无理性与超越性的分析证明（构造性积分与递推）",
 [M("2011","team",6),M("2026","individual",1)],"换皮"),
("AP-M48","孤立奇点的可去性与 Laurent 结构（增长界 ⇒ 可去/极点）",
 [M("2014","team",3),M("2016","team",3),M("2017","individual",3)],"升要求"),
("AP-M49","最大模原理的推论：极值位置、开映射与值域覆盖",
 [M("2014","individual",2),M("2018","individual",2)],"换皮"),
("AP-M50","Hadamard 三圆/三线定理：增长量的对数凸性",
 [M("2021","individual",5),M("2025","individual",3)],"换皮"),
("AP-M51","整函数的零点与增长：Hadamard 因子分解与 Picard/Rouché 型存在性",
 [M("2019","team",4),M("2021","individual",4)],"换皮"),
("AP-M52","C[0,1] 的闭子空间：有限维性、点态收敛 ⇒ 一致收敛",
 [M("2021","individual",2),M("2022","individual",4),M("2026","individual",4)],"原样重复"),
("AP-M53","球测度的半连续性（µ(B_ρ(x)) 的上半连续与不连续例子）",
 [M("2018","individual",4)],"原样重复"),
("AP-M54","Weyl 等分布：无理旋转的遍历平均与指数和估计",
 [M("2013","individual",3)],"原样重复"),
("AP-M55","Gauss–Lucas 定理：多项式临界点落在根的凸包内",
 [M("2013","team",3)],"原样重复"),
("AP-M56","凸函数的正则性与 Legendre 共轭（连续、几乎处处可微、共轭凸函数）",
 [M("2013","team",6)],"原样重复"),
("AP-M57","变分原理与 Euler–Lagrange 方程",
 [M("2015","team",3)],"原样重复"),
("AP-M58","复环面的全纯自同构群 = SL(2,Z)",
 [M("2016","team",4)],"原样重复"),
("AP-M59","度量空间的完备化：L¹ 度量下 C[0,1] 不完备",
 [M("2018","team",4)],"原样重复"),
("AP-M60","守恒量 ⇒ 非线性振子的周期解（能量方法）",
 [M("2020","individual",5)],"原样重复"),
("AP-M61","高维对称积分的极限与渐近（调和平均型被积函数）",
 [M("2022","individual",1)],"原样重复"),
("AP-M62","正定函数与 Bochner 型正性（卷积运算下的正性）",
 [M("2023","individual",3)],"原样重复"),
("AP-M63","Lyapunov–Schmidt 型正交性条件定参数（局部可解性）",
 [M("2024","individual",1)],"原样重复"),
("AP-M64","度量空间的正规性与 Urysohn 引理",
 [M("2025","individual",5)],"原样重复"),
("AP-M65","BMO 空间的基本性质（半范数、L∞⊂BMO、John–Nirenberg 型等价定义）",
 [M("2025","individual",6)],"原样重复"),
("AP-M66","非齐次 Cauchy–Riemann 方程 ∂̄g=f 的解（Cauchy–Pompeiu 公式）",
 [M("2026","individual",3)],"原样重复"),
]

# validate
bad = []
for mid,name,mem,tr in MOTHERS:
    for m in mem:
        if m not in valid: bad.append((mid,m))
if bad:
    print('INVALID MEMBERS:'); [print(' ',b) for b in bad]; sys.exit(1)

slots = sum(len(m[2]) for m in MOTHERS)
covered = set()
for mid,name,mem,tr in MOTHERS:
    for m in mem: covered.add(m)
print('mothers', len(MOTHERS))
print('member slots', slots)
print('unique covered', len(covered), '/', len(valid))
print('uncovered', sorted(valid-covered))
dup = [k for k,v in collections.Counter([m for _,_,ms,_ in MOTHERS for m in ms]).items() if v>1]
print('dual-listed', len(dup), sorted(dup))
sing = [mid for mid,_,mem,_ in MOTHERS if len(mem)==1]
print('singletons', len(sing))

out=[]
for mid,name,mem,tr in MOTHERS:
    yrs=sorted(set(m[0] for m in mem))
    out.append({"id":mid,"name":name,
      "members":[{"year":m[0],"kind":m[1],"n":m[2]} for m in mem],
      "first":yrs[0],"last":yrs[-1],"trend":tr})
json.dump(out, open(os.path.join(BASE,'data','mother_analysis.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote json')
# year distribution of covered
cnt=collections.Counter(m[0] for m in covered)
print('covered by year', sorted(cnt.items()))

