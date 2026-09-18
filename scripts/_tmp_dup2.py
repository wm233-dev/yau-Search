
# -*- coding: utf-8 -*-
import json,io,os,re,sys,itertools
sys.stdout.reconfigure(encoding='utf-8')
ROOT=r'E:\deepseek_exclusive\math\.tmp\burn2026'
papers=json.load(io.open(os.path.join(ROOT,'data','papers.json'),encoding='utf-8'))['papers']
def shingles(s,k=6):
    w=re.findall(r"[a-z]{3,}",s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(0,len(w)-k+1))),w
def get(fn,n):
    for r in papers:
        if r['file']==fn:
            for p in r['problems']:
                if p['n']==n: return p['head']
    return None
# need full body - papers.json keeps only head(400). Use txt directly via best_run replication
PROB_RE=re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):：、]?(?=[ \t\n]|$)")
LIG={"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl"}
def norm(s):
    for k,v in LIG.items(): s=s.replace(k,v)
    return re.sub(r"[ \t]+"," ",s.replace("\r\n","\n"))
def best_run(t):
    c=[(m.start(),int(m.group(1)),m.end()) for m in PROB_RE.finditer(t)]
    best=[]
    for i,(st,n,en) in enumerate(c):
        if n!=1: continue
        run,want=[c[i]],2
        for j in range(i+1,len(c)):
            if c[j][1]==want: run.append(c[j]); want+=1
        if len(run)>len(best): best=run
    return best
def split_problems(t,limit=None):
    r=best_run(t); out=[]
    for i,(st,n,en) in enumerate(r):
        stop=r[i+1][0] if i+1<len(r) else len(t)
        out.append((n,t[en:stop].strip()))
    return out
def body(fn,n):
    t=norm(io.open(os.path.join(ROOT,'txt',fn),encoding='utf-8').read())
    for num,b in split_problems(t):
        if num==n: return b
    return None
cands=[('2010_AlgebraNumberTheory_team.txt',3,'2014_algebra2014_team.txt',2),
       ('2010_AlgebraNumberTheory_team.txt',5,'2011_4_Algebra_Individual_2011.txt',6),
       ('2011_8_Algebra_Team_2011.txt',5,'2012_Algebra2012team.txt',2),
       ('2014_algebra2014_individual.txt',5,'2017_algebra2017_individual.txt',4),
       ('2012_Algebra2012Individual.txt',3,'2014_algebra2014_team.txt',5)]
for fa,na,fb,nb in cands:
    ba,bb=body(fa,na),body(fb,nb)
    if ba is None or bb is None:
        print('MISSING BODY',fa,na,fb,nb); continue
    sa,wa=shingles(ba); sb,wb=shingles(bb)
    inter=len(sa&sb); j=inter/max(1,len(sa|sb))
    print('%s Q%d (%d words,%d sh) vs %s Q%d (%d words,%d sh): inter=%d jaccard=%.3f'%(fa,na,len(wa),len(sa),fb,nb,len(wb),len(sb),inter,j))
