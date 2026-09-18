# -*- coding: utf-8 -*-
import os, io, re, json
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
t = io.open(os.path.join(TXT, "2013_TeamProblems2013.txt"), encoding="utf-8").read().replace("\x00", " ")
t = re.sub(r"[ \t]+", " ", t)
HEAD = re.compile(r"(?m)^[ \t]*(Algebra and Number Theory|Analysis and Di.{1,3}erential Equations|"
                  r"Geometry and Topology|Probability and Statistics|"
                  r"Applied.{0,40}(Math|Statistics|Probability).{0,20}|Computational and Applied Mathematics|"
                  r"Mathematical Physics)[ \t]*$")
print("HEADINGS:")
for m in HEAD.finditer(t):
    print("  pos", m.start(), "->", m.group(1))
print("page markers:", t.count("=== page "))
print("Fibonacci occurrences:", [m.start() for m in re.finditer("Fibonacci", t)])
print("linear model occurrences:", [m.start() for m in re.finditer(r"linear model", t)])
# where does the applied section start, per heading
ms = [(m.start(), m.group(1)) for m in HEAD.finditer(t)]
for i, (st, lab) in enumerate(ms):
    stop = ms[i+1][0] if i+1 < len(ms) else len(t)
    seg = t[st:stop]
    nums = [int(x.group(1)) for x in re.finditer(r"(?m)^[ \t]*(\d{1,2})[ \t]*[.):、]?(?=[ \t\n]|$)", seg)]
    print("SEG", lab, "chars", len(seg), "num-like", nums[:12])
    print("   head:", " ".join(seg.split())[:140])
