# -*- coding: utf-8 -*-
import json, re, sys, itertools
sys.stdout.reconfigure(encoding='utf-8')
segs = json.load(open('./scripts/_phys_segs.json', encoding='utf-8'))
items = [(y, n, segs[y][n]) for y in sorted(segs) for n in sorted(segs[y], key=int)]

def toks(t):
    t = t.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    ws = [w for w in t.split() if len(w) > 1]
    return ws
def shingles(ws, k=5):
    return set(tuple(ws[i:i+k]) for i in range(len(ws)-k+1))

S = {}
for y, n, t in items:
    S[(y,n)] = shingles(toks(t))
print('pairwise Jaccard >= 0.06 among the 30 MP problems (5-gram):')
pairs = []
for a, b in itertools.combinations(items, 2):
    ka, kb = (a[0],a[1]), (b[0],b[1])
    A, B = S[ka], S[kb]
    if not A or not B: continue
    j = len(A & B) / len(A | B)
    if j >= 0.06:
        pairs.append((j, ka, kb, len(A&B)))
pairs.sort(reverse=True)
for j, ka, kb, sh in pairs:
    print(f'  {j:.3f}  {ka[0]}Q{ka[1]}  <->  {kb[0]}Q{kb[1]}   shared={sh}')
print()
print('total pairs(>=0.06):', len(pairs))

# also compare each MP problem against 2023 Computational Q6 (WKB) and 2013 team Q2
TXT='./corpus/prelim/'
pre = {}
t = open(TXT+'2013_TeamProblems2013.txt',encoding='utf-8',errors='replace').read()
m = re.search(r'Fokker-Planck', t)
pre['2013TeamQ2(FokkerPlanck/Schrodinger)'] = t[m.start()-200:m.start()+1600]
t2 = open(TXT+'2023_Computational_Applied.txt',encoding='utf-8',errors='replace').read()
m2 = re.search(r'Schr', t2)
pre['2023CompQ6(WKB)'] = t2[m2.start()-100:m2.start()+1400]
print('precursor blocks captured:', {k: len(v) for k,v in pre.items()})
json.dump(pre, open('./scripts/_phys_precursors.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
