
# -*- coding: utf-8 -*-
import os,io,re,json,collections,statistics,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=r'.'
TXT=os.path.join(ROOT,'txt'); DATA=os.path.join(ROOT,'data')
LIG={"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl"}
def norm(s):
    for k,v in LIG.items(): s=s.replace(k,v)
    return re.sub(r"[ \t]+"," ",s.replace("\r\n","\n"))
TAGS=[
 ("Galois/域扩张",r"\bgalois\b|splitting field|field extension|finite field|algebraic closure"),
 ("群论",r"\bgroup\b|sylow|normal subgroup|solvable|nilpotent group|conjugat"),
 ("环与模",r"\bideal\b|\bmodule\b|noetherian|\bring\b|localization|polynomial ring|\bpid\b|\bufd\b"),
 ("线性代数/矩阵",r"matrix|matrices|eigenvalue|eigenvector|jordan|determinant|\brank\b|trace|hermitian|quadratic form"),
 ("表示论",r"representation|character|irreducible|semisimple|tensor product|schur"),
 ("数论",r"\bprime\b|congruen|diophantine|p-adic|valuation|reciprocity|elliptic curve|quadratic residue|farey|mobius"),
 ("范畴/同调代数",r"\bcategory\b|functor|exact sequence|homolog|projective module|injective|derived"),
 ("微分流形/形式",r"manifold|differential form|de rham|exterior derivative|stokes|closed form|exact form|tangent bundle|vector field|lie (group|algebra)"),
 ("微分几何",r"curvature|geodesic|riemannian|connection|parallel transport|first fundamental form|second fundamental form|mean curvature|gauss-bonnet|holonomy"),
 ("代数拓扑",r"fundamental group|covering space|homology|cohomology|euler characteristic|cw complex|mayer-vietoris|kunneth|cup product|poincare dual"),
 ("代数几何",r"algebraic variety|scheme|projective space|sheaf|coherent|divisor|blow-?up|intersection number"),
 ("辛几何/力学",r"symplectic|poisson bracket|hamiltonian|lagrangian|canonical transformation|liouville|hamilton-jacobi"),
 ("复分析",r"holomorphic|analytic function|meromorphic|residue|entire function|conformal|riemann mapping|cauchy('s)? (integral|theorem)"),
 ("偏微分方程",r"\bpde\b|heat equation|wave equation|laplace equation|elliptic|parabolic|hyperbolic|sobolev|weak solution|a priori|harnack|schauder|energy estimate"),
 ("数学物理/量子",r"schrodinger|wave function|quantum|commutator|uncertainty principle|angular momentum|hydrogen atom"),
]
TAG_RX=[(n,re.compile(p,re.I)) for n,p in TAGS]
VERBS=["prove","show that","show","compute","calculate","find","determine","construct","give an example","explain","evaluate","verify","establish","derive","estimate","solve","describe","characterize"]
SUB_RE=re.compile(r"(?m)^[ \t]*\(?([a-d])\)[ \t]|\((\d)\)[ \t]")
SYM_RE=re.compile(r"[∑∫∂∇√≤≥∈⊂⊆×⊗⊕→↦⇒∀∃|]")
def enrich(year,file,n,body):
    b=norm(body); low=b.lower()
    words=re.findall(r"[A-Za-z']+",b)
    tags=[nm for nm,rx in TAG_RX if rx.search(b)]
    verbs={v:len(re.findall(r"\b"+re.escape(v)+r"\b",low)) for v in VERBS}
    sp=len(SUB_RE.findall(b)); syms=len(SYM_RE.findall(b))
    diff=1.0+min(2.0,len(words)/160.0)+min(1.5,sp*0.5)+min(1.0,syms/40.0)+min(1.0,max(0,len(tags)-1)*0.25)
    return dict(year=year,file=file,n=n,chars=len(b),words=len(words),subparts=sp,symbols=syms,
                tags=tags,verbs={k:v for k,v in verbs.items() if v},difficulty_proxy=round(diff,2),
                head=" ".join(b.split())[:200])
probs=[]
d=json.load(io.open(os.path.join(DATA,'problems_enriched.json'),encoding='utf-8'))
for p in d:
    if 'Algebra' in p['subject']: probs.append(p)
# team algebra for 2013,2016,2017,2018
team_files={'2013':'2013_TeamProblems2013.txt','2016':'2016_2016_team.txt','2017':'2017_2017_team.txt','2018':'2018_2018_team.txt'}
for y,f in team_files.items():
    t=open(os.path.join(TXT,f),'rb').read().decode('utf-8','replace')
    lines=t.splitlines()
    i0=[i for i,l in enumerate(lines) if re.match(r'^\s*Algebra and Number Theory\s*$',l)][0]
    i1=len(lines)
    for j in range(i0+3,len(lines)):
        if 'College Student Mathematics Contests' in lines[j]: i1=j; break
    seg='\n'.join(lines[i0:i1])
    if y=='2013':
        parts=re.split(r'(?m)^\s*(\d)\.\s',seg); pairs=[(parts[k],parts[k+1]) for k in range(1,len(parts)-1,2)]
    else:
        parts=re.split(r'(?m)^Problem\s+(\d)\s*\(',seg); pairs=[(parts[k],parts[k+1]) for k in range(1,len(parts)-1,2)]
    for num,body in pairs:
        probs.append(enrich(y,f,int(num),body))
print('TOTAL algebra problems:',len(probs))
by=collections.defaultdict(list)
for p in probs: by[p['year']].append(p)
print()
hdr='| 年份 | 题数 | 总字符 | 平均题面字符 | 小问标记总数 | 平均小问/题 | 含小问题占比 | 符号密度(符号/题) | 平均难度代理 |'
print(hdr); print('|---|---|---|---|---|---|---|---|---|')
tot=0
for y in sorted(by):
    ps=sorted(by[y],key=lambda p:(p['file'],p['n']))
    n=len(ps); ch=sum(p['chars'] for p in ps); sp=sum(p['subparts'] for p in ps)
    sym=sum(p['symbols'] for p in ps)
    withsp=sum(1 for p in ps if p['subparts']>0)
    print('| %s | %d | %d | %.1f | %d | %.2f | %d%% | %.0f | %.2f |'%(y,n,ch,ch/n,sp,sp/n,round(100*withsp/n),sym/n,statistics.mean(p['difficulty_proxy'] for p in ps)))
    tot+=n
print('TOTAL',tot)
print()
print('--- verbs by year (algebra only) ---')
vy=collections.defaultdict(collections.Counter)
for p in probs:
    for v,c in p['verbs'].items(): vy[p['year']][v]+=c
keys=['prove','show that','show','prove+show','compute','calculate','find','determine','derive','verify','evaluate','construct','describe','explain','solve']
for y in sorted(vy):
    c=vy[y]
    print(y, 'prove=%d showthat=%d show=%d compute=%d calc=%d find=%d det=%d derive=%d verify=%d eval=%d constr=%d desc=%d expl=%d solve=%d'%(
        c['prove'],c['show that'],c['show'],c['compute'],c['calculate'],c['find'],c['determine'],c['derive'],c['verify'],c['evaluate'],c['construct'],c['describe'],c['explain'],c['solve']))
print()
print('--- tag counts by year ---')
allt=collections.Counter()
for p in probs:
    for t in p['tags']: allt[t]+=1
for t,k in allt.most_common(): print(k,t)
json.dump(probs,io.open(os.path.join(ROOT,'scripts','algebra_probs_full.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
