# -*- coding: utf-8 -*-
"""Near-duplicate / overlap detection among 2013-2015 Yau CSMC problem texts."""
import os, re, glob, itertools, json

TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
files = sorted(sum([glob.glob(os.path.join(TXT, y + "_*.txt")) for y in ("2013","2014","2015")], []))

def norm(t):
    t = re.sub(r"===\s*page\s*\d+\s*===", " ", t)
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def shingles(t, k=6):
    w = t.split()
    return set(tuple(w[i:i+k]) for i in range(max(0, len(w)-k+1)))

docs = {os.path.basename(p): norm(open(p, encoding="utf-8", errors="replace").read()) for p in files}

# split 2013 combined team file into subject blocks by its title lines
combo = open(os.path.join(TXT, "2013_TeamProblems2013.txt"), encoding="utf-8").read()
titles = list(re.finditer(r"S\.-T\. Yau College Student Mathematics Contests 2013\s*\n(.+?)\nTeam", combo, re.S))
blocks = {}
for i, m in enumerate(titles):
    s = m.start()
    e = titles[i+1].start() if i+1 < len(titles) else len(combo)
    nm = re.sub(r"\s+", " ", m.group(1)).strip()
    blocks["2013_TEAM::" + nm] = norm(combo[s:e])
print("2013 combined team blocks:", list(blocks.keys()))

allpairs = dict(docs)
docs2 = dict(docs)
docs2.update(blocks)
sh = {k: shingles(v) for k, v in docs2.items()}

pairs = []
keys = sorted(sh)
for a, b in itertools.combinations(keys, 2):
    if not sh[a] or not sh[b]:
        continue
    inter = len(sh[a] & sh[b])
    if inter < 12:
        continue
    j = inter / len(sh[a] | sh[b])
    pairs.append((j, inter, a, b))
pairs.sort(reverse=True)
print("\n--- top overlapping pairs (Jaccard on 6-word shingles, >=12 shared) ---")
for j, inter, a, b in pairs[:25]:
    print("%.4f  shared=%4d  %s  <->  %s" % (j, inter, a, b))

# exact repeated sentences across the whole corpus
sents = {}
for k, v in docs2.items():
    for s in re.split(r"(?<=[\.\?])\s+", v):
        s = s.strip()
        if len(s.split()) >= 12:
            sents.setdefault(s, set()).add(k)
dup = {s: ks for s, ks in sents.items() if len(ks) > 1}
print("\n--- repeated long sentences (>=12 words) across 2013-2015: %d ---" % len(dup))
for s, ks in list(dup.items())[:15]:
    print("  [%s] %s" % (",".join(sorted(ks)), s[:160]))

stats = {"pairs": [(round(j,4), inter, a, b) for j,inter,a,b in pairs], "dup_sentences": len(dup)}
json.dump(stats, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\dup_2013_2015.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nTOTAL docs compared:", len(docs2), " total chars:", sum(len(v) for v in docs2.values()))
