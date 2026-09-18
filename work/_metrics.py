
# -*- coding: utf-8 -*-
import re, os, sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
BASE = r'.tmp/burn2026/txt'
def load(f):
    return open(os.path.join(BASE,f),'rb').read().replace(b'\x00',b'').decode('utf-8',errors='replace')

FILES = [
 (2010,'I','2010_Applied_Computational_Probability_and_Statistics_individual.txt','num',6),
 (2010,'T','2010_Applied_Computational_Probability_and_Statistics_team.txt','num',6),
 (2011,'I','2011_2_AppliedMathProb_Individual_2011.txt','num',6),
 (2011,'T','2011_6_AppliedMathProb_Team_2011.txt','num',6),
 (2012,'I','2012_Applied2012individual.txt','num',5),
 (2012,'T','2012_Applied2012team.txt','num',5),
 (2013,'I','2013_applied2013_individual.txt','num',6),
 (2013,'T','2013_TeamProblems2013.txt','num',6),
 (2014,'I','2014_applied2014_individual.txt','num',5),
 (2014,'T','2014_applied2014_team.txt','num',5),
 (2015,'I','2015_applied2015_individual.txt','prob',5),
 (2015,'T','2015_team_applied2015.txt','prob',5),
 (2016,'I','2016_applied2016_individual.txt','prob',5),
 (2016,'T','2016_2016_team.txt','prob',5),
 (2017,'I','2017_applied2017_individual.txt','num',5),
 (2017,'T','2017_2017_team.txt','num',5),
 (2018,'I','2018_applied2018_individual.txt','num',5),
 (2018,'T','2018_2018_team.txt','num',5),
 (2019,'I','2019_AppliedMath2019_individual.txt','num',4),
 (2019,'T','2019_AppliedMath2019_team.txt','num',5),
 (2020,'Q','2020_Applied_Math_and_Computational_Math_computational_and_applied_20.txt','prob',6),
 (2021,'Q','2021_ExamPaper_21S_computational_and_applied_21s.txt','prob',6),
 (2022,'Q','2022_ExamPaper_2022_computational_and_applied_22s.txt','prob',6),
 (2023,'Q','2023_Computational_Applied.txt','num',6),
 (2024,'Q','2024_2024_Computational_Math.txt','num',6),
 (2025,'Q','2025_computational_and_applied_math.txt','prob2025',6),
 (2026,'Q','2026_2026_Computation.txt','prob',6),
]
SEC = {  # restrict to applied section for multi-subject team files
 '2013_TeamProblems2013.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2013\s*\nApplied Math\. and Computational Math\.', r'=== page 10 ==='),
 '2016_2016_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2016\s*\nApplied Math\. and Computational Math\.', None),
 '2017_2017_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2017\s*\nApplied Math\. and Computational Math\.', None),
 '2018_2018_team.txt': (r'S\.-T\. Yau College Student Mathematics Contests 2018\s*\nApplied Math\. and Computational Math\.', None),
}
PATS = {'prob': r'^\s*Problem\s+(\d+)\b', 'num': r'^\s*(\d+)[.)]\s', 'prob2025': r'^\s*Problem\s+(\d+)\b'}
VERBS = ['prove','show','derive','compute','find','determine','explain','describe','construct','verify','estimate','solve','analyze','analyse','justify','design','identify']

def segment(text, kind, want):
    ms = list(re.finditer(PATS[kind], text, flags=re.M))
    # sequential matcher
    picked=[]; expect=1
    for m in ms:
        try: v=int(m.group(1))
        except: continue
        if v==expect:
            picked.append(m); expect+=1
    out=[]
    for i,m in enumerate(picked):
        e = picked[i+1].start() if i+1<len(picked) else len(text)
        body = text[m.end():e]
        body = re.sub(r'=== page \d+ ===','',body)
        out.append((int(m.group(1)), body))
    return out

rows=[]
for year,kind,f,pat,want in FILES:
    t=load(f)
    if f in SEC:
        sp,ep=SEC[f]
        m=re.search(sp,t); s=m.start()
        if ep:
            m2=re.search(ep,t[s+10:]); t=t[s:s+10+m2.start()]
        else: t=t[s:]
    segs=segment(t,pat,want)
    status='OK' if len(segs)==want else 'MISMATCH got %d want %d'%(len(segs),want)
    print(year,kind,f[:46].ljust(48),status)
    for n,body in segs:
        b=re.sub(r'\s+',' ',body).strip()
        # strip trailing page numbers / footer
        subparts = len(re.findall(r'\((?:[a-j]|[ivx]{1,3}|\d{1,2})\)', b))
        sub2 = len(re.findall(r'^\s*\((?:[a-j]|[ivx]{1,3}|\d{1,2})\)', re.sub(r'\s+',' ',body), flags=re.M))
        vb=collections.Counter()
        low=b.lower()
        for v in VERBS:
            c=len(re.findall(r'\b'+v+r'(?:s|d)?\b', low))
            if c: vb[v]=c
        rows.append(dict(year=year,kind=kind,file=f,n=n,chars=len(b),subparts=subparts,verbs=dict(vb)))
json.dump(rows, open(r'.tmp/burn2026/work/prob_metrics_curated.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('total problems measured:', len(rows))
