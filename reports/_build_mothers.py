# -*- coding: utf-8 -*-
import json, os, sys
from collections import Counter

BASE = r'E:\deepseek_exclusive\math\.tmp\burn2026'
P    = os.path.join(BASE, 'data', 'problems_full.json')
OUT  = os.path.join(BASE, 'data', 'mother_probability.json')

d  = json.load(open(P, encoding='utf-8'))
ps = [x for x in d if x['subject'] == 'Probability & Statistics']
K  = lambda x: (x['year'], x['kind'], x['n'])
avail = {}
for x in ps:
    avail.setdefault(K(x), 0)
    avail[K(x)] += 1
dups = {k:v for k,v in avail.items() if v != 1}
print('TOTAL problems in file :', len(d))
print('P&S records            :', len(ps))
print('P&S unique (year,kind,n):', len(avail), 'dups:', dups)

# (name, trend, [members])
MOTHERS = [
 ("由函数恒等式/不变性反推分布（Stein 恒等式、旋转不变性、和差独立）","升要求",
  [("2014","individual",1),("2020","individual",2),("2020","individual",4),("2026","individual",6)]),
 ("用特征函数刻画与识别分布（正定性、单位根消去、稳定律）","升要求",
  [("2012","team",4),("2013","team",1),("2016","team",3),("2022","individual",1),("2026","individual",5)]),
 ("条件期望作为最优预测（正态线性投影、给定统计量的最优猜测）","换皮",
  [("2010","individual",1),("2014","individual",4)]),
 ("归一化比值导出 Beta/Dirichlet/F（Gamma 和与正态二次型）","升要求",
  [("2010","individual",3),("2012","individual",6),("2015","team",3)]),
 ("次序统计量与间距的分布及其渐近","升要求",
  [("2010","team",1),("2016","team",5),("2018","team",1)]),
 ("正态族的独立性层级：不相关、独立与条件独立","升要求",
  [("2012","individual",5),("2015","team",4),("2018","individual",4)]),
 ("正态向量的旋转/正交投影技巧与 t 分布构造","换皮",
  [("2013","individual",2),("2018","individual",5)]),
 ("收敛模式之间的关系（依概率、依分布、矩收敛、随机下标、一致可积）","升要求",
  [("2012","individual",2),("2014","team",1),("2015","team",2),("2017","team",2),("2021","individual",1)]),
 ("Borel-Cantelli 与 limsup 几乎必然极限（含逆命题）","升要求",
  [("2012","team",1),("2012","team",2),("2013","team",2),("2013","individual",1),("2016","team",4),
   ("2019","team",1),("2019","individual",1),("2021","individual",3)]),
 ("部分和/平均的几乎必然收敛与可积性","升要求",
  [("2010","individual",2),("2014","individual",2),("2015","individual",3),("2019","team",2)]),
 ("Markov 链的常返性、平稳分布与几何混合","升要求",
  [("2017","individual",5),("2019","individual",2),("2021","individual",2),("2022","individual",4)]),
 ("赌局与随机游走的吸收概率、停止时间（赌徒输光型）","升要求",
  [("2017","team",3),("2018","individual",2),("2020","individual",3),("2024","individual",1)]),
 ("随机游走的极值与访问计数","升要求",
  [("2016","individual",5),("2024","individual",2)]),
 ("格点随机游走的相交与自回避","换皮",
  [("2016","individual",1),("2017","team",4)]),
 ("树上随机游走与信号传播的临界阈值","升要求",
  [("2016","team",1),("2017","individual",2)]),
 ("指定模式首次出现的等待时间","换皮",
  [("2015","individual",2),("2022","individual",3)]),
 ("经典递推/对称性技巧求期望（飞机座位、无放回取球）","换皮",
  [("2015","team",1),("2017","individual",1)]),
 ("充分性、完备性与 UMVUE","升要求",
  [("2013","individual",6),("2022","individual",5),("2023","individual",5)]),
 ("估计量的无偏性、相合性、渐近正态与渐近效率","升要求",
  [("2014","team",4),("2015","individual",4),("2017","team",5)]),
 ("极小极大估计与风险下界","升要求",
  [("2010","team",3),("2022","individual",6)]),
 ("支撑依赖参数的非正则 MLE 及其极限分布","升要求",
  [("2012","team",5),("2014","team",5),("2024","individual",5)]),
 ("多项/离散模型的 MLE、似然比检验与渐近分布","升要求",
  [("2010","individual",4),("2010","team",4),("2014","individual",5),("2023","individual",6)]),
 ("检验统计量的构造、p 值分布与功效","换皮",
  [("2012","team",6),("2013","individual",4)]),
 ("重随机化与基于设计的因果推断","升要求",
  [("2019","individual",4),("2020","individual",5),("2020","individual",6),("2021","individual",5),("2021","individual",6)]),
 ("秩检验与 P(X<Y) 型效应量","升要求",
  [("2012","individual",4),("2026","individual",1)]),
 ("置信区间的覆盖概率与构造","升要求",
  [("2013","individual",5),("2015","individual",5),("2025","individual",1)]),
 ("贝叶斯更新、贝叶斯检验与经验贝叶斯","升要求",
  [("2012","individual",1),("2013","team",4),("2018","individual",1),("2018","team",5)]),
 ("线性模型的代数：可估性、FWL 定理与 OLS 投影","升要求",
  [("2013","team",6),("2026","individual",2)]),
 ("Lasso 与稀疏估计的刻画","升要求",
  [("2013","team",5),("2015","team",5)]),
 ("高维 M 估计量的均匀偏差界","换皮",
  [("2024","individual",4),("2025","individual",4)]),
 ("集中不等式：MGF/矩方法","换皮",
  [("2016","team",2),("2017","team",1),("2020","individual",1)]),
 ("非传递性与决策悖论","换皮",
  [("2025","individual",2),("2025","individual",3)]),
 ("记录值与排列圈数：调和和型期望及其极限","升要求",
  [("2013","individual",3),("2019","team",3),("2023","individual",3)]),
 ("占位与匹配问题的极限分布","升要求",
  [("2016","individual",3),("2018","individual",3)]),
 ("随机图的阈值现象","换皮",
  [("2017","individual",4),("2019","team",4)]),
 ("随机矩阵的典型性质","换皮",
  [("2016","individual",2),("2021","individual",4)]),
 ("矩约束下的极值与可达集","换皮",
  [("2015","individual",1),("2016","individual",4)]),
 ("条件期望的测度论性质：测度变换、分布不变性与条件独立","升要求",
  [("2012","individual",3),("2013","team",3),("2014","individual",3),("2014","team",3)]),
 ("正则条件概率与条件期望的极限逼近","换皮",
  [("2023","individual",2),("2023","individual",4)]),
]

# singletons (recognised but not merged) + non-probability mis-filed records
SINGLES = [
 ("自归一化/三角阵列的中心极限定理", [("2010","team",2)]),
 ("iid 对称化测度不等式 P(|X+Y|<1) <= 3P(|X-Y|<1)", [("2012","team",3)]),
 ("随机变量之比的密度（Jacobian 变换）", [("2014","team",2)]),
 ("用可测集把 Bernoulli 概率测度两两分离", [("2017","individual",3)]),
 ("灯泡随机切换过程的返回概率", [("2018","team",2)]),
 ("Sanov 型熵函数 l(mu) 的凹性与单调性", [("2018","team",3)]),
 ("直方图密度估计的偏差-方差与窗宽选择", [("2018","team",4)]),
 ("随机幂级数的零点无穷多次", [("2019","individual",3)]),
 ("耦合与全变差距离的变分刻画", [("2022","individual",2)]),
 ("Dirichlet 过程的边缘分布与二值化", [("2023","individual",1)]),
 ("X^k 数位的等分布与 k(m) 的充要条件", [("2024","individual",3)]),
 ("验证 2*phi(x)*Phi(ax) 是密度并求期望（skew-normal）", [("2026","individual",3)]),
 ("Brownian 运动首次退出区间的二阶矩", [("2026","individual",4)]),
]
NONPROB = [("2010","individual",5),("2010","individual",6),("2010","team",5),("2010","team",6)]

# ---------- validate ----------
used = Counter()
errs = []
for name, tr, mem in MOTHERS + [('SINGLE', '孤题', m) for (n, m) in SINGLES]:
    for k in mem:
        if k not in avail:
            errs.append(('MISSING', name, k))
        used[k] += 1
for k in NONPROB:
    if k not in avail:
        errs.append(('MISSING-NONPROB', '', k))
    used[k] += 1
multi = {k:v for k,v in used.items() if v > 1}
uncovered = [k for k in avail if k not in used]
print('ERRORS:', errs)
print('DOUBLE-ASSIGNED:', multi)
print('UNCOVERED:', sorted(uncovered))
print('mothers:', len(MOTHERS), 'singletons:', len(SINGLES), 'nonprob:', len(NONPROB))
print('members in mothers:', sum(len(m) for _,_,m in MOTHERS))

# ---------- build json ----------
def first_last(mem):
    ys = sorted(int(k[0]) for k in mem)
    return str(ys[0]), str(ys[-1])

# order mothers by first year, then size desc, then original order
order = sorted(range(len(MOTHERS)), key=lambda i: (first_last(MOTHERS[i][2])[0], -len(MOTHERS[i][2]), i))
out = []
idmap = {}
for pos, i in enumerate(order, 1):
    name, tr, mem = MOTHERS[i]
    fid = 'PS-M%02d' % pos
    idmap[fid] = name
    f, l = first_last(mem)
    out.append({"id": fid, "name": name,
                "members": [{"year": y, "kind": k, "n": n} for (y,k,n) in sorted(mem)],
                "first": f, "last": l, "trend": tr, "size": len(mem)})
for pos, (name, mem) in enumerate(SINGLES, 1):
    f, l = first_last(mem)
    out.append({"id": 'PS-S%02d' % pos, "name": name,
                "members": [{"year": y, "kind": k, "n": n} for (y,k,n) in sorted(mem)],
                "first": f, "last": l, "trend": "孤题", "size": len(mem)})

json.dump(out, open(OUT,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('WROTE', OUT)

recent = lambda mem: sum(1 for k in mem if int(k[0]) >= 2021)
print()
print('| id | size | first | last | recent | score | trend | name |')
for r in out:
    mem = [(m['year'], m['kind'], m['n']) for m in r['members']]
    rc = recent(mem); sc = r['size'] + 2*rc
    print('| %s | %d | %s | %s | %d | %d | %s | %s |' % (r['id'], r['size'], r['first'], r['last'], rc, sc, r['trend'], r['name']))

n_mem = sum(len(m) for _,_,m in MOTHERS)
print()
print('coverage vs 133 =', round(100.0*n_mem/len(ps),1), '%  vs 129 (excl non-prob) =', round(100.0*n_mem/129,1), '%')
print('TOP10:')
rank = sorted([r for r in out if r['id'].startswith('PS-M')],
              key=lambda r: (-(r['size'] + 2*recent([(m['year'],m['kind'],m['n']) for m in r['members']])), -r['size']))
for r in rank[:12]:
    mem = [(m['year'],m['kind'],m['n']) for m in r['members']]
    print('  %s size=%d score=%d last=%s %s' % (r['id'], r['size'], r['size']+2*recent(mem), r['last'], r['name']))
