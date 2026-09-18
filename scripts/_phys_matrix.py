# -*- coding: utf-8 -*-
import json, re, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')
segs = json.load(open('E:/deepseek_exclusive/math/.tmp/burn2026/scripts/_phys_segs.json', encoding='utf-8'))

T = [
 ('经典力学：极坐标拉氏量', r'Lagrangian using polar|polar coordinates'),
 ('经典力学：有效势/径向化归', r'eﬀective|effective (potential|Lagrangian|one)'),
 ('经典力学：圆轨道稳定性', r'circular orbit|stable equilibrium|stability|stable'),
 ('经典力学：小振动周期', r'small oscillation|frequenc.{0,12}small|ω\b'),
 ('经典力学：Hamilton形式/正则动量', r'Hamiltonian|canonical|vector potential A'),
 ('经典力学：守恒量/对称性', r'conserv|symmetr|Killing'),
 ('经典力学：E-L方程求解', r'Euler-Lagrange|equations of motion'),
 ('连续/受约束系统(摆/环)', r'pendulum|bead|hoop|tension|rod'),
 ('量子力学：态/波函数/反幺正', r'anti-unitary|wave ?function|state vector|Hilbert'),
 ('量子力学：谐振子', r'harmonic oscillator|harmonic potential'),
 ('量子力学：升降算符/对易子', r'creation and annihilation|ladder operator|commutation relation|commutator|a†'),
 ('量子力学：su(2)/角动量/自旋', r'su\(2\)|angular momentum|spin|J_?\+|Jz'),
 ('量子力学：微扰论/简并', r'perturb|degenerac|correction to the energy|first order'),
 ('量子力学：时间演化/跃迁概率', r'Heisenberg picture|transition|probabilit|time evolution'),
 ('量子力学：相干态/位移算符', r'ground state|shift operator|dipole moment'),
 ('量子力学：散射/隧穿/散射长度', r'scattering|tunnel|reﬂection|reflection|bound state'),
 ('电动力学：Maxwell方程组', r'Maxwell'),
 ('电动力学：规范不变性/势', r'gauge (transformation|invariance|ﬁeld)|vector potential|Lorentz gauge|scalar and vector potentials'),
 ('电动力学：推迟势/Green函数', r'retarded|Green.s function|θ\(t'),
 ('电动力学：平面波/波包/偏振', r'plane wave|wave packet|polariz|circularly|ˆx \+ iˆy'),
 ('电动力学：导体/集肤深度/反射', r'conductivity|ohmic|skin|reﬂect|reflect|boundary condition'),
 ('电动力学：静磁/线圈展开', r'magnetic ﬁeld|magnetic field|coil|solenoid|Bz|Bρ'),
 ('统计力学：配分函数/自由能', r'partition function|free energy'),
 ('统计力学：Ising/平均场', r'Ising|mean ﬁeld|magnetization|susceptibility'),
 ('统计力学：临界指数/相变', r'critical (exponent|temperature)|phase transition|coexist|Clausius|vapor pressure|entropy'),
 ('统计力学：热容/玻色费米', r'heat capacity|speciﬁc heat|specific heat|\bboson|\bfermion|dispersion relation'),
 ('热力学：平衡条件', r'thermodynamic equilibrium|liquid.{0,6}gas|latent'),
 ('相对论：Killing场/守恒量', r'Killing'),
 ('相对论：度规/诱导度规', r'ds2|induced from|Minkowski metric'),
 ('相对论：Christoffel/Ricci/R', r'Christo|Ricci|scalar curvature|Rµν'),
 ('相对论：Einstein方程/Λ', r"Einstein.{0,30}(equation|metric)|cosmolog"),
 ('相对论：黑洞/视界/零超曲面', r'black hole|horizon|null|r −2M|2M'),
 ('相对论：引力波/四极辐射', r'gravitational wave|h\+|h×|coalesc|quadrupole'),
 ('相对论：测地线/粒子运动', r'geodesic|free falling|equation of motion for the free'),
 ('量子场论：传播子/顶点', r'propagator|vertex'),
 ('量子场论：费曼图/单圈', r'Feynman|loop'),
 ('量子场论：维数正规化/反项', r'dimensional regularization|counterterm|counter-term|δm|renormaliz'),
 ('量子场论：RG流/β函数', r'renormalization group|RG|ﬂow equation|running'),
 ('量子场论：标度/共形不变', r'scale invariant|scale transformation|conformal|rescaling|Weyl|traceless'),
 ('量子场论：能量-动量张量', r'energy momentum|θµν|stress'),
 ('量子场论：大N极限/指标', r'large N|N go|1\s*N|O\(N\)|g0 = λ0N'),
 ('量子场论：Dirac/旋量/Yukawa', r'Dirac|Yukawa|ψ¯|γ5'),
 ('微分几何：Klein/双曲', r'Klein|hyperbolic|non-Euclidean'),
 ('微分几何：度量诱导/距离函数', r'cosh d|distance d'),
 ('微分几何：Christoffel/Riemann/K', r'Christo|Riemann tensor|Rrθrθ|curvature K'),
]

rows = {}
for y in sorted(segs):
    for n in sorted(segs[y], key=int):
        s = segs[y][n]
        hits = [name for name, pat in T if re.search(pat, s, re.I)]
        rows[(y, n)] = hits
        print(f'{y} Q{n}: ({len(hits)}) {hits}')
print()
counts = defaultdict(list)
for (y, n), hits in rows.items():
    for h in hits:
        counts[h].append((y, n))
print('### tag -> count, years')
for name, _ in T:
    lst = counts.get(name, [])
    ys = sorted(set(a for a, b in lst))
    print(f'{name:34s} | {len(lst):2d}题 | {len(ys)}年 {ys} | {[a+"Q"+b for a,b in lst]}')
