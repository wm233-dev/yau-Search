# -*- coding: utf-8 -*-
"""v2: 修正题量计数 + 补丁式趋势统计 (供报告引用)"""
import os, re, collections, json
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"

FILES = {
 2024: ["2024_2024_Algebra.txt","2024_2024_Analysis_and_diff_v2.txt","2024_2024_Computational_Math.txt",
        "2024_2024_GeometryTopology.txt","2024_2024_Math_physics.txt","2024_2024_statistics.txt"],
 2025: ["2025_algebra.txt","2025_analysis.txt","2025_computational_and_applied_math.txt",
        "2025_Geometry_and_Topology.txt","2025_physics.txt","2025_statistics.txt"],
 2026: ["2026_2026_Algebra_and_Number_Theory.txt","2026_2026_analysis.txt","2026_2026_Computation.txt",
        "2026_2026_Geo_Topology.txt","2026_2026_physics.txt","2026_2026_statistics.txt"],
}
SUBJ = {
 "2024_2024_Algebra.txt":"algebra","2024_2024_Analysis_and_diff_v2.txt":"analysis",
 "2024_2024_Computational_Math.txt":"computation","2024_2024_GeometryTopology.txt":"geometry",
 "2024_2024_Math_physics.txt":"physics","2024_2024_statistics.txt":"statistics",
 "2025_algebra.txt":"algebra","2025_analysis.txt":"analysis",
 "2025_computational_and_applied_math.txt":"computation","2025_Geometry_and_Topology.txt":"geometry",
 "2025_physics.txt":"physics","2025_statistics.txt":"statistics",
 "2026_2026_Algebra_and_Number_Theory.txt":"algebra","2026_2026_analysis.txt":"analysis",
 "2026_2026_Computation.txt":"computation","2026_2026_Geo_Topology.txt":"geometry",
 "2026_2026_physics.txt":"physics","2026_2026_statistics.txt":"statistics",
}
MANGLE = {"p":"(","q":")","Ñ":"->","ą":">","\u201c":"=","\u00b4":"-","\u02c6":"INT","\u0159":"SUM"}

def load(fn, demangle=False):
    raw = open(os.path.join(TXT, fn), "rb").read()
    t = None
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try: t = raw.decode(enc); break
        except UnicodeDecodeError: continue
    t = "".join(ch for ch in t if ch in "\n\t" or ord(ch) >= 32)
    for a,b in [("\ufb00","ff"),("\ufb01","fi"),("\ufb02","fl"),("\ufb03","ffi"),("\ufb04","ffl")]:
        t = t.replace(a,b)
    t = re.sub(r"-\n(?=[a-z])", "", t).replace("\u00ad","")
    t = re.sub(r"[ \t]+", " ", t)
    if demangle:
        t = "".join(MANGLE.get(ch, ch) for ch in t)
    return t

pm = re.compile(r"^[ \t]*(?:Problem|Question)[ \t]*(\d{1,2})\b", re.M)
nm = re.compile(r"^[ \t]*(\d{1,2})[\.\)][ \t]+\S", re.M)
pg = re.compile(r"^=== page (\d+) ===", re.M)
sub_re = re.compile(r"\((?:[a-j]|\d{1,2}|i{1,3}v?|iv|v|vi{0,3}|ix|x)\)")
sub_re2 = re.compile(r"\((?:\d{1,2}|[a-j]|i{1,3}v?|iv|v|vi{0,3}|ix|x)\)")

def contiguous(nums):
    s = sorted(set(nums)); n = 0
    for i in range(1, 40):
        if i in s: n = i
        else: break
    return n

rows=[]
for yr, fs in FILES.items():
    for fn in fs:
        dm = "Analysis_and_diff" in fn
        t = load(fn, demangle=dm)
        tp = load(fn, demangle=False)
        nums = [int(x) for x in pm.findall(t)]
        probs = contiguous(nums) if nums else 0
        if probs == 0:
            nums2 = [int(x) for x in nm.findall(t)]
            probs = contiguous(nums2)
        raw_text = tp
        sub = len(sub_re2.findall(t))
        pages = len(pg.findall(t))
        rows.append(dict(year=yr, subj=SUBJ[fn], probs=probs, pages=pages,
                         chars=len(raw_text), sub=sub,
                         sub_per=round(sub/probs,2) if probs else 0,
                         nums=sorted(set(nums)) if nums else sorted(set(int(x) for x in nm.findall(t)))))

for r in sorted(rows, key=lambda x:(x["year"], x["subj"])):
    print("%d %-12s pages=%d chars=%5d probs=%d sub=%3d sub/p=%-5s nums=%s" % (
        r["year"], r["subj"], r["pages"], r["chars"], r["probs"], r["sub"], r["sub_per"], r["nums"]))
print()
for yr in (2024,2025,2026):
    rs=[r for r in rows if r["year"]==yr]
    print("%d: files=%d probs=%d chars=%d" % (yr, len(rs), sum(x["probs"] for x in rs), sum(x["chars"] for x in rs)))
print("TOTAL probs:", sum(x["probs"] for x in rows), " chars:", sum(x["chars"] for x in rows))

# ---- 趋势指标 ----
TREND = {
 "证明类: prove/show that": r"\b(?:prove|show that|show the following)\b",
 "求解类: compute/derive/determine/calculate/find": r"\b(?:compute|derive|determine|calculate|find)\b",
 "判定类: is/does/can/are...?": r"\b(?:Does there exist|Is the|Is it|Are there|Are the|Can we|Can the|Can a|Is there|Does the|Is this)\b",
 "构造/反例: construct/example/counterexample/disprove": r"\b(?:construct|example|counterexample|disprove)\b",
 "小问(a)(b)(c) 结构": r"\([a-j]\)",
 "'if and only if'": r"if and only if",
 "'Hint'": r"\bHint\b",
 "矩阵/线性代数词": r"\b(?:matrix|matrices|eigenvalue|singular value|orthogonal|rank)\b",
 "曲率类": r"\b(?:curvature|Ricci|Riemann tensor|geodesic)\b",
 "p-adic/局部域": r"\b(?:p-adic|Qp|Zp|local field|unramified|ramified)\b",
 "有限元/差分/稳定性": r"\b(?:finite element|finite difference|stabilit|scheme|discretiz)\b",
 "量子场论/重整化": r"\b(?:renormaliz|propagator|counterterm|loop|Yukawa|phi4)\b",
 "引力/黑洞/引力波": r"\b(?:black hole|gravitational wave|general relativity|de Sitter)\b",
 "Brownian/随机分析": r"\b(?:Brownian|martingale|stopping time)\b",
}
print()
print("=== TREND (occurrences per year) ===")
print("%-52s %6s %6s %6s" % ("metric","2024","2025","2026"))
for name, pat in TREND.items():
    rx = re.compile(pat, re.I)
    c = collections.Counter()
    for r in rows:
        dm = r["subj"]=="analysis"
    for yr in (2024,2025,2026):
        pass
    for yr, fs in FILES.items():
        for fn in fs:
            dm = "Analysis_and_diff" in fn
            c[yr] += len(rx.findall(load(fn, demangle=dm)))
    print("%-52s %6d %6d %6d" % (name, c[2024], c[2025], c[2026]))
