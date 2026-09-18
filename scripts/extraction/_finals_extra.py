
import json, re, collections, statistics, os
S=json.load(open(r'.\scripts\finals_app_phys_stats.json',encoding='utf-8'))
probs=S["problems"]; papers=S["papers"]
def subj(p): return "Applied" if "Applied" in p.split(os.sep)[0] else "MathPhys"
# verbs by subject
VERBS=["show","prove","find","compute","derive","determine","construct","solve","calculate","explain","estimate","discuss","write","verify","define","sketch","identify","count","recast","compare","describe"]
for s in ["Applied","MathPhys"]:
    v=[x for x in probs if subj(x["paper"])==s]
    tot=len(v)
    print(s, "units", tot, {k: "%d(%.0f%%)"%(sum(1 for x in v if re.search(r"\b"+k,x["full"],re.I)), 100*sum(1 for x in v if re.search(r"\b"+k,x["full"],re.I))/tot) for k in ["show","prove","find","compute","derive","calculate","determine","construct","solve","explain"]})
# by subject x kind detail
for s in ["Applied","MathPhys"]:
    for k in ["Individual","Overall","Team"]:
        v=[x for x in probs if subj(x["paper"])==s and x["kind"]==k]
        if not v: continue
        print(s,k,"n=",len(v),"meanchars=%.1f"%statistics.mean([x["chars"] for x in v]),
              "medchars=%.0f"%statistics.median([x["chars"] for x in v]),
              "meansub=%.2f"%statistics.mean([x["subparts"] for x in v]),
              "meansym=%.1f"%statistics.mean([x["syms"] for x in v]))
# 'choose k out of N' instruction count
CHOOSE=re.compile(r"(choose|answer|select)\s+(?:any\s+)?(\d+|one|two|three|at least \d+)\s+(?:out of|of the)\s+(\w+)", re.I)
n=0; ex=[]
for p in papers:
    if p["kind"]=="Syllabus": continue
    t=open(os.path.join(r'.\txt_finals',[x for x in os.listdir(r'.\txt_finals') if True][0]),encoding='utf-8') if False else None
print("---- choose-instruction scan ----")
import io
TXT=r'.\txt_finals'
MAN=json.load(open(r'.\data\finals_manifest.json',encoding='utf-8'))
cnt=0
for m in MAN:
    top=m["rel"].split(os.sep)[0]
    if "Applied" not in top and "Mathematical_Physics" not in top: continue
    if not m.get("txt"): continue
    t=open(os.path.join(TXT,m["txt"]),encoding="utf-8",errors="replace").read()
    mm=CHOOSE.search(t)
    if mm:
        cnt+=1
        print("  ", m["rel"].split(os.sep)[-1][:46], "->", re.sub(r"\s+"," ",mm.group(0)))
print("papers with choose/answer-k-of-N instruction:", cnt)
# year coverage
print("---- files per year/kind ----")
c=collections.Counter((subj(p["rel"]), p["kind"], p["year"]) for p in papers if p["kind"]!="Syllabus")
for k in sorted(c): print(k)
