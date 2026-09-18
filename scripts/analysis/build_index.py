# -*- coding: utf-8 -*-
"""Canonical extractor + builds (a) problems_full.json, (b) markdown index, (c) standalone HTML browser."""
import os, io, re, json, html, collections

ROOT = r"."
TXT, DATA, REP = (os.path.join(ROOT, d) for d in ("txt", "data", "reports"))
LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl",
       "\u2019":"'","\u2018":"'","\u201c":'"',"\u201d":'"',"\u2013":"-","\u2014":"--","\u00a0":" "}
def norm(s):
    for k, v in LIG.items(): s = s.replace(k, v)
    return re.sub(r"[ \t]+", " ", s.replace("\r\n", "\n").replace("\x00", " "))

PROB_RE = re.compile(r"(?m)^[ \t]*(?:(?:Problem|Question|Exercise)[ \t]*)?(\d{1,2})[ \t]*[.):：、]?(?=[ \t\n]|$)")
def best_run(t):
    c = [(m.start(), int(m.group(1)), m.end()) for m in PROB_RE.finditer(t)]
    best = []
    for i, (st, n, en) in enumerate(c):
        if n != 1: continue
        run, want = [c[i]], 2
        for j in range(i + 1, len(c)):
            if c[j][1] == want: run.append(c[j]); want += 1
        if len(run) > len(best): best = run
    return best
def cutp(t, limit=None):
    r = best_run(t); out = []
    for i, (st, n, en) in enumerate(r):
        stop = r[i+1][0] if i+1 < len(r) else len(t)
        out.append((n, t[en:stop].strip()))
    return out[:limit] if limit else out

HEAD_RE = re.compile(r"(?m)^[ \t]*(Algebra and Number Theory|Analysis and Di.{1,3}erential Equations|"
                     r"Geometry and Topology|Probability and Statistics|"
                     r"Applied.{0,40}(Math|Statistics|Probability).{0,20}|Computational and Applied Mathematics|"
                     r"Mathematical Physics)[ \t]*$")
SUBJ_PATTERNS = [
    ("Algebra & Number Theory", r"algebra"),
    ("Analysis & PDE",          r"analysis"),
    ("Geometry & Topology",     r"geometry|geomtop|geo_topo|geotop"),
    ("Probability & Statistics", r"probab|proba|statistic"),
    ("Mathematical Physics",    r"physic"),
    ("Computational & Applied", r"applied|comput"),
]
def subj_of(name):
    low = name.lower()
    for label, pat in SUBJ_PATTERNS:
        if re.search(pat, low): return label
    return "Other/Combined"

def clean(b):
    b = re.sub(r"(?m)^[ \t]*=== page \d+ ===[ \t]*$", " ", b)
    b = re.sub(r"\[[0-9,\s]{1,12}\]", "", b)
    b = re.sub(r"\n{3,}", "\n\n", b)
    return b.strip()

problems = []
for fn in sorted(os.listdir(TXT)):
    if not fn.endswith(".txt"): continue
    name = fn[:-4]
    year = name[:4]
    kind = "solution" if ("soln" in name.lower() or "solution" in name.lower()) else ("team" if "team" in name.lower() else "individual")
    if kind == "solution": continue
    text = norm(io.open(os.path.join(TXT, fn), encoding="utf-8").read())
    m = re.search(r"\((\d+)\s+problems?\)", text, re.I)
    limit = int(m.group(1)) if m else None
    multi = kind == "team" and text.count("=== page ") >= 5
    if multi:
        marks = [(mm.start(), mm.group(1)) for mm in HEAD_RE.finditer(text)]
        segs = []
        if len(marks) >= 2:
            for i, (st, lab) in enumerate(marks):
                stop = marks[i+1][0] if i+1 < len(marks) else len(text)
                segs.append((subj_of(lab.lower()), text[st:stop]))
        else:
            segs = [(subj_of(name), text)]
    else:
        segs = [(subj_of(name), text)]
    for sj, seg in segs:
        for n, body in cutp(seg, limit if not multi else None):
            body = clean(body)
            if len(body) < 30: continue
            problems.append({"year": year, "subject": sj, "paper": name, "kind": kind,
                             "n": n, "chars": len(body), "text": body})

json.dump(problems, io.open(os.path.join(DATA, "problems_full.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOTAL_PROBLEMS", len(problems))
cnt = collections.Counter((p["year"], p["subject"]) for p in problems)
print("YEARS", len(set(p["year"] for p in problems)), "SUBJECTS", len(set(p["subject"] for p in problems)))

# markdown index
L = ["# Yau 竞赛 2010-2026 全题目索引（自动生成）\n",
     "共 %d 道题。字段：年份 / 科目 / 卷别 / 题号 / 字数 / 题面前 260 字。\n" % len(problems)]
for p in sorted(problems, key=lambda x: (x["year"], x["subject"], x["n"])):
    head = " ".join(p["text"].split())[:260]
    L.append("- **[%s | %s | %s | Q%d]** (%d chars) %s" % (p["year"], p["subject"], p["kind"], p["n"], p["chars"], head))
io.open(os.path.join(REP, "all_problems_index.md"), "w", encoding="utf-8").write("\n".join(L))

# standalone HTML
payload = json.dumps([{k: p[k] for k in ("year","subject","paper","kind","n","chars")} | {"text": p["text"][:4000]} for p in problems], ensure_ascii=False)
HT = """<!doctype html><html lang="zh"><head><meta charset="utf-8">
<title>Yau 竞赛题库索引 2010-2026</title>
<style>
body{font-family:system-ui,"Microsoft YaHei",sans-serif;margin:0;background:#f6f7f9;color:#1c1e21}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid #dcdfe4;padding:12px 16px;z-index:5}
h1{font-size:18px;margin:0 0 8px}
select,input{font-size:13px;padding:5px 8px;border:1px solid #c8ccd4;border-radius:6px;margin-right:8px}
#count{color:#5b6472;font-size:13px}
main{padding:12px 16px;display:grid;gap:10px}
.card{background:#fff;border:1px solid #dfe3e8;border-radius:8px;padding:10px 12px}
.meta{font-size:12px;color:#5b6472;margin-bottom:6px}
.badge{display:inline-block;background:#eef2ff;color:#33418f;border-radius:4px;padding:1px 6px;margin-right:6px}
pre{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Consolas,monospace;font-size:12.5px;margin:0}
</style></head><body>
<header><h1>丘成桐大学生数学竞赛 题库索引 2010-2026（共 <span id="total"></span> 题）</h1>
<select id="year"><option value="">全部年份</option></select>
<select id="subject"><option value="">全部科目</option></select>
<select id="kind"><option value="">全部卷别</option></select>
<input id="q" placeholder="关键词搜索，如 Galois / Sobolev / martingale" size="34">
<span id="count"></span></header>
<main id="list"></main>
<script>
const DATA=__DATA__;
const $=s=>document.querySelector(s);
const uniq=k=>[...new Set(DATA.map(d=>d[k]))].sort();
for(const k of ['year','subject','kind']){const el=$('#'+k);for(const v of uniq(k)){const o=document.createElement('option');o.value=v;o.textContent=v;el.appendChild(o);}}
$('#total').textContent=DATA.length;
function render(){
 const y=$('#year').value,s=$('#subject').value,k=$('#kind').value,q=$('#q').value.trim().toLowerCase();
 const rows=DATA.filter(d=>(!y||d.year===y)&&(!s||d.subject===s)&&(!k||d.kind===k)&&(!q||d.text.toLowerCase().includes(q)));
 $('#count').textContent='命中 '+rows.length+' 题';
 $('#list').innerHTML=rows.slice(0,400).map(d=>'<div class="card"><div class="meta"><span class="badge">'+d.year+'</span><span class="badge">'+d.subject+'</span>'+d.kind+' · Q'+d.n+' · '+d.chars+' chars · '+d.paper+'</div><pre>'+d.text.replace(/[<>&]/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;'}[c]))+'</pre></div>').join('');
}
for(const id of ['#year','#subject','#kind']) $(id).addEventListener('change',render);
$('#q').addEventListener('input',render);
render();
</script></body></html>"""
io.open(os.path.join(ROOT, "yau_index.html"), "w", encoding="utf-8").write(HT.replace("__DATA__", payload))
print("WROTE", os.path.join(ROOT, "yau_index.html"), os.path.getsize(os.path.join(ROOT, "yau_index.html")), "bytes")
print("WROTE", os.path.join(REP, "all_problems_index.md"))
per = collections.Counter(p["year"] for p in problems)
print("PER_YEAR", dict(sorted(per.items())))
