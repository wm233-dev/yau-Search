# -*- coding: utf-8 -*-
import json
from collections import Counter
path = r'E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json'
d = json.load(open(path, encoding='utf-8'))
print("subject 取值分布:", Counter(x['subject'] for x in d).most_common())
alg = [x for x in d if x['subject'] == 'Algebra & Number Theory']
print("精确匹配 'Algebra & Number Theory' 条数:", len(alg))
subj_alg = [x for x in d if 'Algebra' in x['subject']]
print("含 'Algebra' 的 subject:", Counter(x['subject'] for x in subj_alg).most_common())
print("含 Algebra 的条数:", len(subj_alg))
print()
print("--- 讲义 4.2 节关于 JSON 抽取残缺的声明核查 ---")
def show(y,k,n):
    hits=[x for x in d if x['year']==y and x['kind']==k and x['n']==n]
    for h in hits:
        print(f"[{y} {k} #{n}] text = {h['text']!r}"[:700])
    if not hits: print(f"[{y} {k} #{n}] <无此条目>")
for y,k,n in [('2017','team',1),('2017','team',2),('2019','team',1),('2019','team',2),('2011','individual',5),('2011','individual',6)]:
    show(y,k,n)
print()
print("--- 题 10 讲义里引用的 2026 题 ---")
for n in [1,3,4,5]:
    show('2026','individual',n)
print()
print("--- 其他交叉引用抽查 ---")
for y,k,n in [('2021','individual',2),('2020','individual',4),('2024','individual',3),('2024','individual',6),
              ('2017','team',4),('2013','team',3),('2013','team',6),('2013','individual',3),
              ('2018','team',1),('2013','team',2),('2023','individual',4),('2015','individual',1),
              ('2011','team',5),('2025','individual',5),('2018','individual',1),('2014','individual',5),
              ('2016','individual',5)]:
    hits=[x for x in d if x['year']==y and x['kind']==k and x['n']==n]
    for h in hits:
        t=" ".join(h['text'].split())
        print(f"[{y} {k} #{n}] {t[:230]}")
    if not hits: print(f"[{y} {k} #{n}] <无此条目>")
