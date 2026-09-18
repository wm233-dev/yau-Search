# -*- coding: utf-8 -*-
"""Normalise the curated finals inventories: fix mis-split entries, de-duplicate, unify difficulty type."""
import json, io, os, collections

BASE = r'.'
DATA = os.path.join(BASE, 'data')

FIX = {
    ('2019', 'Individual', '2019 stat-individual.pdf', 4): "简单线性回归 Y 对 X 的系数估计恰为 1，若交换 X 与 Y 的角色（以 X 为响应）会得到什么结论",
    ('2019', 'Individual', '2019 stat-individual.pdf', 5): "10 题测验、Logistic/IRT 模型 P(Y_i=1)=e^{θ−b_i}/(1+e^{θ−b_i})：A 错了两道最简单题、B 错了两道最难题目却同为 80 分，A 关于评分不公平的申诉是否成立",
    ('2019', 'Individual', '2019 stat-individual.pdf', 6): "两个研究中心各自发现 X、Y 正相关，合并数据后却负相关，这是否可能",
}

def norm(path):
    rows = json.load(io.open(path, encoding='utf-8'))
    seen, out = set(), []
    for r in rows:
        year, kind, paper, n, gist, topic, method, diff = r
        key = (year, kind, paper, int(n))
        if key in FIX:
            gist = FIX[key]
        if key in seen:
            continue
        seen.add(key)
        out.append({
            'year': year, 'kind': kind, 'paper': paper, 'n': int(n),
            'gist': gist, 'topic': topic, 'method': method, 'diff': int(diff),
        })
    json.dump(out, io.open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out

g = norm(os.path.join(DATA, 'finals_geo_problems.json'))
p = norm(os.path.join(DATA, 'finals_prob_problems.json'))
print('geo', len(g), 'prob', len(p), 'total', len(g) + len(p))
c = collections.Counter((r['year'], r['kind']) for r in g)
print('geo by year/kind:', sorted(c.items()))
c2 = collections.Counter((r['year'], r['kind']) for r in p)
print('prob by year/kind:', sorted(c2.items()))
