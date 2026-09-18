# -*- coding: utf-8 -*-
r"""补充统计: 题型分布 / 多小问占比 / 题面长度 / 去连字符后的具名定理检索"""
import os, re, json, glob, collections, statistics

TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
files = sorted(set(sum([glob.glob(os.path.join(TXT, p)) for p in ("2010_*.txt","2011_*.txt","2012_*.txt")], [])))

def subject_of(name):
    low=name.lower()
    for k,v in (("algebranumbertheory","代数"),("algebra","代数"),("analysis","分析"),
                ("applied","应用/概率统计"),("geometrytopology","几何拓扑"),("geomtop","几何拓扑"),
                ("geometry","几何拓扑"),("probability","概率统计")):
        if k in low: return v
    return "?"

# 切题: 行首 "N." 递增
def split_problems(txt):
    lines = txt.split("\n"); idx=[]
    for i,ln in enumerate(lines):
        m=re.match(r"^\s*(\d{1,2})\.\s*(.*)$", ln)
        if m and int(m.group(1))==len(idx)+1: idx.append(i)
    idx.append(len(lines))
    return ["\n".join(lines[idx[k]:idx[k+1]]) for k in range(len(idx)-1)]

PROVE = re.compile(r"\b(prove|show that|show |verify|justify|demonstrate|explain|derive)\b", re.I)
COMPUTE = re.compile(r"\b(compute|calculate|find|evaluate|solve|determine|construct|describe)\b", re.I)
MULTI = re.compile(r"^\s*[\(（]?[a-e1-9][\)）]\s", re.M)

stat = collections.defaultdict(lambda: dict(n=0, prove=0, comp=0, multi=0, lens=[]))
allrec=[]
for f in files:
    base=os.path.basename(f); year=base[:4]; subj=subject_of(base)
    kind = "个人" if ("individual" in base.lower() or "_indi" in base.lower()) else "团体"
    for prob in split_problems(open(f,encoding="utf-8").read()):
        head = prob[:400]
        s = stat[(year,kind)]; s["n"]+=1; s["lens"].append(len(prob))
        if PROVE.search(head): s["prove"]+=1
        if COMPUTE.search(head): s["comp"]+=1
        if MULTI.search(prob): s["multi"]+=1
        s2 = stat[(year,"ALL")]; s2["n"]+=1; s2["lens"].append(len(prob))
        if PROVE.search(head): s2["prove"]+=1
        if COMPUTE.search(head): s2["comp"]+=1
        if MULTI.search(prob): s2["multi"]+=1
        allrec.append(dict(year=year,kind=kind,subj=subj,len=len(prob)))

print("| 年份 | 卷别 | 题数 | 含'证明/说明'的题 | 占比 | 含'计算/求'的题 | 占比 | 多小问题 | 占比 | 题面平均字符 | 中位数字符 |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for k in sorted(stat, key=lambda x:(x[0],x[1])):
    s=stat[k]; n=s["n"]
    print("| %s | %s | %d | %d | %.0f%% | %d | %.0f%% | %d | %.0f%% | %.0f | %.0f |" % (
        k[0],k[1],n,s["prove"],100*s["prove"]/n,s["comp"],100*s["comp"]/n,s["multi"],100*s["multi"]/n,
        statistics.mean(s["lens"]), statistics.median(s["lens"])))

print()
print("总体: 题数=%d 多小问=%d (%.0f%%) 平均题面=%.0f 字符" % (len(allrec),
      sum(1 for r in allrec if r["len"]), 0, statistics.mean([r["len"] for r in allrec])))

# 按科目题面长度
bysub=collections.defaultdict(list)
for r in allrec: bysub[r["subj"]].append(r["len"])
print("\n| 科目 | 题数 | 平均题面字符 |")
print("| --- | --- | --- |")
for k,v in sorted(bysub.items(), key=lambda kv:-len(kv[1])):
    print("| %s | %d | %.0f |" % (k,len(v),statistics.mean(v)))

# 去连字符后检索具名对象 (处理 PDF 断词 "Cheby-\nshev")
def dehyph(t): return re.sub(r"-\s*\n\s*", "", t)
NAMES2 = {
 "Chebyshev 多项式": r"chebyshev", "最大(值)原理": r"maximum principle",
 "共轭梯度法": r"conjugate gradient", "Schwarz 引理": r"schwarz",
 "Lagrange 乘子": r"lagrange", "Taylor 展开": r"taylor",
 "Cauchy 积分/序列": r"cauchy", "Sylow 定理": r"sylow",
 "Galois 群": r"galois", "Riemann 度量": r"riemannian",
 "Gauss-Bonnet": r"gauss-bonnet", "Stokes 定理": r"stokes",
 "von Neumann 稳定性": r"von neumann", "Bessel/Parseval": r"parseval|bessel",
 "Krylov 子空间": r"krylov", "Hölder/插值不等式": r"holder|hölder",
}
print("\n| 具名对象(去连字符后检索) | 命中次数 | 覆盖卷数 |")
print("| --- | --- | --- |")
texts = {f: dehyph(open(f,encoding="utf-8").read()) for f in files}
for name,pat in NAMES2.items():
    rx=re.compile(pat,re.I); tot=0; nf=0
    for f,t in texts.items():
        c=len(rx.findall(t))
        if c: tot+=c; nf+=1
    print("| %s | %d | %d |" % (name,tot,nf))
