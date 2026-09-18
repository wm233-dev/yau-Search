# -*- coding: utf-8 -*-
"""Theme clustering over all 757 problems: textual near-duplicate families (shingle Jaccard)
plus topic-tag co-occurrence families; outputs reports/theme_clusters.md."""
import os, io, re, json, itertools, collections

ROOT = r"."
DATA, REP = os.path.join(ROOT, "data"), os.path.join(ROOT, "reports")
problems = json.load(io.open(os.path.join(DATA, "problems_full.json"), encoding="utf-8"))
enr = json.load(io.open(os.path.join(DATA, "problems_enriched.json"), encoding="utf-8"))
print("problems", len(problems), "enriched", len(enr))

def sh(s, k=6):
    w = re.findall(r"[a-z]{3,}", s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(0, len(w)-k+1)))
for p in problems:
    p["sh"] = sh(p["text"])

# ---- textual families ----
parent = list(range(len(problems)))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[rb] = ra

edges = []
for i, j in itertools.combinations(range(len(problems)), 2):
    a, b = problems[i], problems[j]
    if not a["sh"] or not b["sh"]: continue
    inter = len(a["sh"] & b["sh"])
    if inter < 3: continue
    jac = inter / len(a["sh"] | b["sh"])
    if jac >= 0.10:
        union(i, j); edges.append((i, j, round(jac, 3), inter))
groups = collections.defaultdict(list)
for i in range(len(problems)): groups[find(i)].append(i)
fam = [sorted(v) for v in groups.values() if len(v) >= 2]
fam.sort(key=lambda g: -len(g))
print("text families>=2:", len(fam), "edges:", len(edges))

# ---- tag families (topic signature) ----
tag_of = {}
for e in enr:
    tag_of[(e["year"], e["subject"], e["n"])] = set(e["tags"])
def key(p): return (p["year"], p["subject"], p["n"])
for p in problems: p["tags"] = tag_of.get(key(p), set())

L = ["# 考点家族聚类（自动生成）\n",
     "输入：757 道题的题面文本与规则化考点标签。方法：(a) 词元 6-gram Jaccard ≥ 0.10 连边求连通分量；",
     "(b) 考点标签集合按出现年份做时间线。\n",
     "> 说明：文本家族近似「同源题/孪生题」；标签家族近似「同一考点的不同包装」。\n",
     "## 1. 文本近重复家族（成员 ≥ 2）\n"]
for gi, g in enumerate(fam[:40], 1):
    yrs = sorted(set(problems[i]["year"] for i in g))
    subs = sorted(set(problems[i]["subject"] for i in g))
    L.append("### 家族 T%02d（%d 题，年份 %s）\n" % (gi, len(g), "/".join(yrs)))
    L.append("- 科目：" + "、".join(subs))
    for i in g[:8]:
        p = problems[i]
        L.append("  - %s %s Q%d：%s" % (p["year"], p["subject"], p["n"], " ".join(p["text"].split())[:150]))
    if len(g) > 8: L.append("  - …… 另有 %d 题" % (len(g) - 8))
    L.append("")

# tag timeline
tt = collections.defaultdict(list)
for p in problems:
    for t in p["tags"]: tt[t].append((p["year"], p["subject"], p["n"]))
L += ["", "## 2. 考点时间线（出现 ≥ 6 个年份的骨架考点）\n",
      "| 考点 | 覆盖年份数 | 累计题次 | 年份分布 | 最近出现 |", "|---|---|---|---|---|"]
for t, lst in sorted(tt.items(), key=lambda kv: -len(set(y for y, _, _ in kv[1]))):
    yrs = sorted(set(y for y, _, _ in lst))
    if len(yrs) < 6: continue
    hist = collections.Counter(y for y, _, _ in lst)
    L.append("| %s | %d | %d | %s | %s |" % (t, len(yrs), len(lst),
             " ".join("%s:%d" % (y, hist[y]) for y in yrs), yrs[-1]))
L.append("")
L += ["## 3. 只在最近 3 年(2024-2026)出现的新考点\n",
      "| 考点 | 2024 | 2025 | 2026 | 历史总题次 |", "|---|---|---|---|---|"]
for t, lst in sorted(tt.items(), key=lambda kv: -sum(1 for y, _, _ in kv[1] if y >= "2024")):
    recent = collections.Counter(y for y, _, _ in lst if y >= "2024")
    if sum(recent.values()) < 3: continue
    L.append("| %s | %d | %d | %d | %d |" % (t, recent["2024"], recent["2025"], recent["2026"], len(lst)))
L.append("")
io.open(os.path.join(REP, "theme_clusters.md"), "w", encoding="utf-8").write("\n".join(L))
json.dump({"families": [[{"year": problems[i]["year"], "subject": problems[i]["subject"], "n": problems[i]["n"]} for i in g] for g in fam]},
          io.open(os.path.join(DATA, "text_families.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("families:", len(fam), "-> reports/theme_clusters.md")
print("top families sizes:", [len(g) for g in fam[:12]])
