
# -*- coding: utf-8 -*-
import json, re, sys, itertools, os, collections
sys.stdout.reconfigure(encoding='utf-8')
BASE=r'./txt'
def load(f):
    return open(os.path.join(BASE,f),'rb').read().replace(b'\x00',b'').decode('utf-8',errors='replace')
FILES = [
 (2010,'I','2010_Applied_Computational_Probability_and_Statistics_individual.txt','num'),
 (2010,'T','2010_Applied_Computational_Probability_and_Statistics_team.txt','num'),
 (2011,'I','2011_2_AppliedMathProb_Individual_2011.txt','num'),
 (2011,'T','2011_6_AppliedMathProb_Team_2011.txt','num'),
 (2012,'I','2012_Applied2012individual.txt','num'),(2012,'T','2012_Applied2012team.txt','num'),
 (2013,'I','2013_applied2013_individual.txt','num'),(2013,'T','2013_TeamProblems2013.txt','num'),
 (2014,'I','2014_applied2014_individual.txt','num'),(2014,'T','2014_applied2014_team.txt','num'),
 (2015,'I','2015_applied2015_individual.txt','prob'),(2015,'T','2015_team_applied2015.txt','prob'),
 (2016,'I','2016_applied2016_individual.txt','prob'),(2016,'T','2016_2016_team.txt','prob'),
 (2017,'I','2017_applied2017_individual.txt','num'),(2017,'T','2017_2017_team.txt','num'),
 (2018,'I','2018_applied2018_individual.txt','num'),(2018,'T','2018_2018_team.txt','num'),
 (2019,'I','2019_AppliedMath2019_individual.txt','num'),(2019,'T','2019_AppliedMath2019_team.txt','num'),
 (2020,'Q','2020_Applied_Math_and_Computational_Math_computational_and_applied_20.txt','prob'),
 (2021,'Q','2021_ExamPaper_21S_computational_and_applied_21s.txt','prob'),
 (2022,'Q','2022_ExamPaper_2022_computational_and_applied_22s.txt','prob'),
 (2023,'Q','2023_Computational_Applied.txt','num'),
 (2024,'Q','2024_2024_Computational_Math.txt','num'),
 (2025,'Q','2025_computational_and_applied_math.txt','prob'),
 (2026,'Q','2026_2026_Computation.txt','prob'),
]
SEC = {
 '2013_TeamProblems2013.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2013\s*\nApplied Math\. and Computational Math\.', r'=== page 10 ==='),
 '2016_2016_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2016\s*\nApplied Math\. and Computational Math\.', None),
 '2017_2017_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2017\s*\nApplied Math\. and Computational Math\.', None),
 '2018_2018_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2018\s*\nApplied Math\. and Computational Math\.', None)}
PATS={'prob': r'^\s*Problem\s+(\d+)\b','num': r'^\s*(\d+)[.)]\s'}
def seg(text,kind):
    ms=list(re.finditer(PATS[kind],text,flags=re.M)); picked=[]; exp=1
    for m in ms:
        v=int(m.group(1))
        if v==exp: picked.append(m); exp+=1
    out=[]
    for i,m in enumerate(picked):
        e=picked[i+1].start() if i+1<len(picked) else len(text)
        out.append((int(m.group(1)), text[m.end():e]))
    return out
def toks(s):
    s=re.sub(r'=== page \d+ ===','',s)
    s=s.replace('ﬁ','fi').replace('ﬂ','fl').replace('ﬀ','ff')
    s=re.sub(r'[^A-Za-z0-9]+',' ',s).lower()
    return s.split()
probs={}
for y,k,f,pat in FILES:
    t=load(f)
    if f in SEC:
        sp,ep=SEC[f]; m=re.search(sp,t); s=m.start()
        if ep:
            m2=re.search(ep,t[s+10:]); t=t[s:s+10+m2.start()]
        else: t=t[s:]
    for n,body in seg(t,pat):
        probs[(y,k,n)]=toks(body)
def grams(ws,k=6): return {tuple(ws[i:i+k]) for i in range(len(ws)-k+1)}
G={key:grams(ws) for key,ws in probs.items()}
keys=sorted(G)
pairs=[]
for a,b in itertools.combinations(keys,2):
    A,B=G[a],G[b]
    if not A or not B: continue
    j=len(A&B)/len(A|B)
    if j>=0.08: pairs.append((round(j,3),a,b))
pairs.sort(reverse=True)
print('pairs with 6-gram token Jaccard >= 0.08 :', len(pairs))
for j,a,b in pairs[:40]:
    print(f'{j:.3f}  {a}  <->  {b}')
print()
# specific candidate pairs
cands=[((2011,'T',2),(2016,'T',1)),((2012,'T',1),(2020,'Q',1)),((2012,'I',3),(2015,'I',3)),
       ((2014,'I',4),(2017,'I',4)),((2010,'I',6),(2012,'I',4)),((2010,'I',6),(2015,'T',5)),
       ((2012,'I',4),(2015,'T',5)),((2014,'T',3),(2014,'I',3)),((2016,'T',3),(2016,'I',3)),
       ((2013,'I',6),(2013,'T',6)),((2014,'T',4),(2015,'I',4)),((2024,'Q',6),(2023,'Q',5)),
       ((2024,'Q',6),(2025,'Q',5)),((2023,'Q',5),(2025,'Q',5)),((2021,'Q',1),(2019,'T',1)),
       ((2021,'Q',1),(2023,'Q',2)),((2021,'Q',1),(2024,'Q',3)),((2013,'T',4),(2010,'T',5)),
       ((2017,'I',5),(2024,'Q',4)),((2019,'I',2),(2024,'Q',5)),((2020,'Q',3),(2018,'T',3)),
       ((2016,'T',4),(2017,'I',4))]
for a,b in cands:
    A,B=G.get(a),G.get(b)
    if A and B:
        print(f'{len(A&B)/len(A|B):.3f}  {a} <-> {b}')
