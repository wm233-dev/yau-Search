
import re, json, sys, io, os
sys.stdout.reconfigure(encoding='utf-8')
BASE = r'.tmp/burn2026/txt'

def load(f):
    d = open(os.path.join(BASE,f),'rb').read().replace(b'\x00',b'')
    return d.decode('utf-8',errors='replace')

def section(text, startpat, endpat=None):
    m = re.search(startpat, text)
    if not m: return None
    s = m.start()
    if endpat:
        m2 = re.search(endpat, text[s+10:])
        if m2: return text[s:s+10+m2.start()]
    return text[s:]

def split_problems(sec, pat):
    ms = list(re.finditer(pat, sec, flags=re.M))
    out=[]
    for i,m in enumerate(ms):
        e = ms[i+1].start() if i+1<len(ms) else len(sec)
        body = sec[m.end():e]
        out.append((m.group(1), re.sub(r'\s+',' ',body).strip()))
    return out

# --- team papers: isolate applied section
specs = [
 ('2013_TeamProblems2013.txt', r'S\.-T\. Yau College Student Mathematics Contests 2013\s*\nApplied Math\. and Computational Math\.', r'=== page 10 ==='),
 ('2016_2016_team.txt', r'S\.-T\. Yau College Student Mathematics Contests 2016\s*\nApplied Math\. and Computational Math\.', None),
 ('2017_2017_team.txt', r'S\.-T\. Yau College Student Mathematics Contests 2017\s*\nApplied Math\. and Computational Math\.', None),
 ('2018_2018_team.txt', r'S\.-T\. Yau College Student Mathematics Contests 2018\s*\nApplied Math\. and Computational Math\.', None),
]
pat_prob = r'^\s*Problem\s+(\d+)\.'
pat_num  = r'^\s*(\d+)\.\s'
for f,sp,ep in specs:
    t=load(f)
    sec=section(t,sp,ep)
    print('####',f,'section len',len(sec) if sec else None)
    for p in (pat_prob,pat_num):
        parts=split_problems(sec,p)
        print('   pat',p,'-> n=',len(parts),[a for a,_ in parts], [len(b) for _,b in parts])
