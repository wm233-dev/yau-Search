# -*- coding: utf-8 -*-
"""Finals corpus: text-layer availability + verb statistics for ALG/ANA scope."""
import json, os, re, collections

ROOT = r'E:\deepseek_exclusive\math'
TXT = os.path.join(ROOT, '.tmp', 'burn2026', 'txt_finals')
idx = json.load(open(os.path.join(ROOT, '.tmp', 'burn2026', 'data', 'finals_index.json'), encoding='utf-8'))
m = json.load(open(os.path.join(ROOT, '.tmp', 'burn2026', 'data', '_finals_txtmap.json'), encoding='utf-8'))

print('### A. 全语料文字层可用性（195 文件）')
zero = [a for a in idx if a['chars'] == 0]
lt100 = [a for a in idx if a['chars'] < 100]
lt800 = [a for a in idx if a['chars'] < 800]
print('total=%d  chars==0: %d  chars<100: %d  chars<800: %d' % (len(idx), len(zero), len(lt100), len(lt800)))
byS = collections.defaultdict(lambda: [0, 0, 0])
for a in idx:
    k = a['subj'].split('Algebra')[0].strip() or a['subj'][:20]
    byS[k][0] += 1
    if a['chars'] < 800: byS[k][1] += 1
    if a['chars'] < 100: byS[k][2] += 1
for k, v in byS.items():
    print('  %-45s total=%2d  <800=%2d  <100=%2d' % (k[:45], v[0], v[1], v[2]))

print()
print('### B. 本次范围（subj 含 Algebra 或 Analysis）逐卷字符与文字层')
sel = sorted([(k, v) for k, v in m.items() if ('Algebra' in v['subj']) or ('Analysis' in v['subj'])],
             key=lambda kv: (('ALG' if 'Algebra' in kv[1]['subj'] else 'ANA'), kv[1]['kind'], kv[1]['year']))
empty = []
for k, v in sel:
    raw = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read().strip()
    tag = 'ALG' if 'Algebra' in v['subj'] else 'ANA'
    # garbling detector: ratio of chars outside ASCII+common latin
    bad = len(re.findall(r'[\u00a7\u2022\u00c4\u00ee\u00bc\u02dc\u0161\u00dd\u00ea\u00e5\u00e4\u00f6\u00fc\u00df]', raw))
    flag = ''
    if len(raw) < 100: flag = 'EMPTY'
    elif bad > 10: flag = 'GARBLED(%d)' % bad
    if flag: empty.append((tag, v['kind'], v['year'], len(raw), flag))
    print('%s|%s|%s|%4d|%s' % (tag, v['kind'], v['year'], len(raw), flag))
print()
print('NO-TEXT/GARBLED in scope:', empty)

print()
print('### C. 任务动词统计（作用域内 67 卷全文）')
VERBS = {'prove': r'\bprove\b|\bProof\b', 'show': r'\bshow\b', 'find': r'\bfind\b',
         'compute/calculate': r'\bcompute\b|\bcalculate\b|\bevaluate\b', 'determine': r'\bdetermine\b',
         'solve': r'\bsolve\b', 'construct': r'\bconstruct\b', 'classify': r'\bclassify\b|\bclassification\b',
         'describe': r'\bdescribe\b', 'estimate': r'\bestimate\b', 'prove-or-show': r'\bprove\b|\bshow\b'}
buckets = collections.defaultdict(collections.Counter)
for k, v in sel:
    raw = open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    grams = ' '.join(re.findall(r'[A-Za-z]+', raw))
    tag = 'ALG' if 'Algebra' in v['subj'] else 'ANA'
    for name, pat in VERBS.items():
        buckets[tag][name] += len(re.findall(pat, grams, re.I))
        buckets[tag + '/' + v['kind']][name] += len(re.findall(pat, grams, re.I))
for key in sorted(buckets):
    c = buckets[key]
    tot = sum(c.values())
    print('%-14s ' % key + '  '.join('%s=%d' % (n, c[n]) for n in VERBS if n != 'prove-or-show'))
