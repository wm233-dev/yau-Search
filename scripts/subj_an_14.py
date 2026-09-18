
# -*- coding: utf-8 -*-
import os, re, json, collections
exec(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])

def split_problems(t, year):
    lines=t.split("\n")
    idx=0
    for i,l in enumerate(lines):
        if re.match(r"^\s*(1\.|1\)|Problem\s+1\b)", l):
            idx=i; break
    body="\n".join(lines[idx:])
    pat = r"(?m)^\s*(?:Problem\s+)?(\d{1,2})\s*[\.\)]?\s+(?=[A-Z(\\])"
    ms=[m for m in re.finditer(pat, body)]
    out=[]; 
    for j,m in enumerate(ms):
        n=int(m.group(1))
        if n!=len(out)+1: continue
        end = ms[j+1].start() if j+1<len(ms) else len(body)
        txt=body[m.start():end].strip()
        if len(txt)<40: continue
        out.append((n, txt))
    return out

probs=[]
for (y,part),t in sorted(secs.items()):
    for n,txt in split_problems(t,y):
        probs.append({"year":y,"part":part,"n":n,"chars":len(txt),"text":txt})
cnt=collections.Counter((p["year"],p["part"]) for p in probs)
print("COUNTS:", {f"{k[0]}{k[1]}":v for k,v in sorted(cnt.items())})
print("TOTAL", sum(len(re.findall(r'\S+',p['text'])) for p in probs), "words;", len(probs), "problems")

VERBS=["prove","show","derive","compute","calculate","find","determine","construct","verify","state","solve","give","explain","justify","check","estimate","establish"]
print("\n| 年份 | 题数 | 总字符 | 平均字符/题 | (a)-(j) 子问 | (1)-(9) 子问 | 总小问 | " + " | ".join(VERBS) + " |")
tot=collections.Counter()
prev=None
for y in sorted(set(p["year"] for p in probs)):
    sel=[p for p in probs if p["year"]==y]
    ch=sum(p["chars"] for p in sel)
    sa=sum(len(re.findall(r"(?m)^\s*\(?[a-j]\)", p["text"])) for p in sel)
    s1=sum(len(re.findall(r"(?m)^\s*\(?[1-9]\)", p["text"])) for p in sel)
    vc=collections.Counter()
    for p in sel:
        low=p["text"].lower()
        for v in VERBS:
            c=len(re.findall(r"\b"+v+r"(?:s|d|ed|ing)?\b", low))
            if c: vc[v]+=c; tot[v]+=c
    print(f"| {y} | {len(sel)} | {ch} | {ch/len(sel):.1f} | {sa} | {s1} | {sa+s1} | " + " | ".join(str(vc.get(v,0)) for v in VERBS) + " |")
print("\nTOTALS:", dict(sorted(tot.items(), key=lambda kv:-kv[1])))

# hint count
print("\nHINT题:")
for p in probs:
    if re.search(r"Hint", p["text"]): print(" ", p["year"], p["part"], p["n"])
# problem length extremes
srt=sorted(probs,key=lambda p:-p["chars"])
print("\nLONGEST:", [(p["year"],p["part"],p["n"],p["chars"]) for p in srt[:8]])
print("SHORTEST:", [(p["year"],p["part"],p["n"],p["chars"]) for p in srt[-8:]])
json.dump(probs, open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\an_probs.json","w"), ensure_ascii=False, indent=1)
