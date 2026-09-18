# -*- coding: utf-8 -*-
import json, re, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))

TAGS = [
 ('变分/Lagrangian力学', r'Lagrangian|Euler[- ]Lagrange|least action', None),
 ('Hamiltonian/正则方程', r'Hamiltonian', r'Hamiltonian (cycle|quaternion)|quaternions'),
 ('对称性与守恒量', r'conserved quantit|constant of motion|conservation of energy|conservation of .{0,12}angular|is conserved|are conserved', None),
 ('Killing矢量场', r'Killing', None),
 ('度规/诱导度规/线元', r'ds2|ds\^2|induced metric|Minkowski metric|line element', None),
 ('测地线/联络/Christoffel', r'geodesic|Christo', None),
 ('曲率/Ricci/标量曲率', r'Ricci|Riemann (tensor|curvature tensor)|scalar curvature', None),
 ('Einstein方程/宇宙常数', r'Einstein.{0,25}equation|cosmolog|Einstein metric', None),
 ('引力波/黑洞', r'gravitational wave|black hole', None),
 ('de Sitter/视界/零曲面', r'de Sitter|horizon|null (surface|hypersurface)', None),
 ('量子力学/波函数/量子态', r'wave ?function|Hilbert space|eigenstate|\bquantum\b', None),
 ('算符代数/升降算符/对易子', r'creation and annihilation|ladder operator|commutation relation|commutator', None),
 ('微扰论/简并能级', r'perturbation|degenerac|first order correction', None),
 ('谐振子', r'harmonic oscillator|harmonic potential', None),
 ('角动量/su(2)/自旋', r'angular momentum|su\(2\)|\bspin\b', None),
 ('散射/隧穿/散射长度', r'scattering|tunnel|transmission coe|reﬂection coe|reflection coe', None),
 ('Maxwell方程/规范不变性', r'Maxwell|gauge (transformation|invariance|ﬁeld|field)|vector potential|Lorentz gauge', None),
 ('推迟势/Green函数/波包', r'retarded|Green.s function|wave packet|plane wave|damped wave-like', None),
 ('磁场/线圈/近轴展开', r'magnetic ﬁeld|magnetic field|coil|solenoid', None),
 ('统计力学/配分函数/Ising', r'partition function|Ising|mean ﬁeld|magnetization|susceptibility', None),
 ('热力学/相变/临界指数', r'thermodynamic|phase transition|coexist|critical (temperature|exponent)|Clausius|vapor pressure|\bentropy\b', None),
 ('热容/玻色费米分布', r'heat capacity|speciﬁc heat|specific heat|\bboson|\bfermion|dispersion relation', None),
 ('量子场论/传播子/费曼图', r'propagator|Feynman|interaction vertex|scalar ﬁeld|scalar field|loop', None),
 ('重整化/维数正规化/反项', r'renormaliz|dimensional regularization|counterterm|counter-term|divergen', None),
 ('标度/共形不变性/迹反常', r'scale invariant|scale transformation|conformal|rescaling|Weyl|trace anomaly|traceless', None),
 ('有效势/圆轨道稳定性', r'eﬀective (potential|one)|effective (potential|one)|circular orbit|stable', None),
 ('小振动/简正频率', r'small oscillation|frequency of small|normal mode|angular frequency', None),
 ('能量-动量张量', r'energy momentum|energy-momentum|stress-energy|µν', None),
 ('Dirac/Yukawa/旋量场', r'Dirac|Yukawa', None),
 ('Klein圆盘/双曲几何', r'Klein disk|Klein model|non-Euclidean|hyperbolic', None),
 ('热方程/扩散方程', r'heat equation|diﬀusion equation|diffusion equation', None),
 ('不确定性原理', r'uncertainty principle', None),
 ('辛结构/相空间', r'symplectic|phase space', None),
 ('变分原理/能量最小', r'variational (principle|problem)|energy minimi', None),
 ('流体/连续介质', r'fluid|incompressible|Navier|Euler equation', None),
]

def scan_problem(text):
    out = []
    for item in TAGS:
        name, pat = item[0], item[1]
        neg = item[2] if len(item) > 2 else None
        if not re.search(pat, text, re.I): continue
        if neg and re.search(neg, text, re.I):
            if not re.search(r'Hamiltonian system|canonical|phase space|symplectic (map|method|integrator|form on)', text, re.I):
                continue
        out.append(name)
    return out

rows = []
for p in full:
    t = p.get('text','')
    tags = scan_problem(t)
    if not tags: continue
    rows.append((p['year'], p['subject'], p['paper'], p['n'], tags, p['subject']=='Mathematical Physics'))

print('### problems with >=1 physics tag:', len(rows), '| MP subject:', sum(1 for r in rows if r[5]), '| other:', sum(1 for r in rows if not r[5]))
print()
print('### Non-MP-subject problems carrying physics tags, year<=2021')
for y,s,pap,n,tags,_ in rows:
    if int(y)<=2021:
        print(f'  {y} | {s:26s} | Q{n:2d} | {tags}')
print()
tagyears = defaultdict(list)
for y,s,pap,n,tags,isphys in rows:
    for tg in tags:
        tagyears[tg].append((y, s, n, isphys))
print('### 考点 -> 年份/题次 (problem level, all subjects 2010-2026)')
for item in TAGS:
    tg = item[0]
    lst = tagyears.get(tg, [])
    ys = sorted(set(x[0] for x in lst))
    phys_ys = sorted(set(x[0] for x in lst if x[3]))
    print(f'{tg:32s} | {len(lst):3d}题 | {len(ys):2d}年 | {" ".join(ys)} | MP-years: {" ".join(phys_ys) if phys_ys else "-"}')
