# -*- coding: utf-8 -*-
"""Yau 竞赛 2016-2018 关键词正则自检: 打印每个模式的命中样例, 用于人工核查是否过宽"""
import glob, os, re, collections

CLEAN = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean'
files = sorted(glob.glob(os.path.join(CLEAN, '201[678]_*.txt')))
YEAR_RE = re.compile(r'S\.-T\. Yau College Student Mathematics Contests\s+(\d{4})')

def norm(t):
    for a, b in [('\ufb01','fi'),('\ufb02','fl'),('\ufb00','ff'),('\ufb03','ffi'),
                 ('\ufb04','ffl'),('\u2019',"'"),('\u201c','"'),('\u201d','"')]:
        t = t.replace(a, b)
    return t

def subject_of(b):
    for k, v in [('Analysis and Di','Analysis'),('Probability and Statistics','Probability'),
                 ('Geometry and Topology','Geometry'),('Algebra and Number Theory','Algebra'),
                 ('Applied Math','Applied')]:
        if k in b: return v
    return 'UNKNOWN'

def kind_of(b):
    head = '\n'.join(b.split('\n')[:8])
    if re.search(r'\bIndividual\b', head): return 'Individual'
    if re.search(r'\bTeam\b', head): return 'Team'
    return 'UNKNOWN'

PROB_RE = re.compile(r'(?m)^\s*(?:Problem\s+)?(\d{1,2})\s*(?:\([^)]*points\)\s*)?[\.\)]')
records = []
for f in files:
    txt = norm(open(f, encoding='utf-8').read())
    base = os.path.basename(f)
    idx = [m.start() for m in YEAR_RE.finditer(txt)] + [len(txt)]
    for a, b in zip(idx[:-1], idx[1:]):
        blk = txt[a:b]
        ms = list(PROB_RE.finditer(blk)); keep = []; expect = 1
        for m in ms:
            if int(m.group(1)) == expect and 1 <= expect <= 12:
                keep.append(m); expect += 1
        for i, m in enumerate(keep):
            end = keep[i+1].start() if i+1 < len(keep) else len(blk)
            records.append(dict(year=base[:4], kind=kind_of(blk), subject=subject_of(blk),
                                body=blk[m.start():end].strip()))

# 待自检模式 (v4 候选)
CHECK = {
 '随机矩阵/算子范数': r'random matrix|Wigner|operator norm|\|X\|op',
 '闭/恰当微分形式':   r'\bexact\b|\bclosed\b|not closed',
 '留数/围道积分':     r'residue|Rukowski|contour integral',
 '马氏链/生灭':       r'Markov process|Markov chain|Poisson process|\bX\(t\)\b|G\(s, t\)',
 '迭代法/收敛率':      r'iterative scheme|spectral radius|residual|convergence rate|converges in n iterations',
 'Laplace/调和':      r'Laplace equation|Delta f|u11|harmonic',
 '插值/逼近':         r'interpolat|approximation is|approximate',
 'Frobenius 定理':    r'Frobenius',
 'Sylow':            r'Sylow',
 '格/LLL':           r'multiplicatively dependent|integer non-zero vector|integer.*x = 0|2nH',
 '共形映射':          r'conformal',
 '树/分支':           r'binary tree|branching|level h',
}
for name, pat in CHECK.items():
    rx = re.compile(pat)
    hs = [r for r in records if rx.search(r['body'])]
    print('=' * 90)
    print(f'{name}  -> 命中 {len(hs)} 题')
    subs = collections.Counter(f"{r['year']}/{r['kind'][:4]}/{r['subject'][:4]}" for r in hs)
    print('   分布:', dict(subs))
    for r in hs[:3]:
        mo = rx.search(r['body'])
        s = max(0, mo.start()-40); e = min(len(r['body']), mo.end()+40)
        print('   样例:', repr(r['body'][s:e].replace('\n', ' ')))
