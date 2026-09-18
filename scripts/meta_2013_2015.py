# -*- coding: utf-8 -*-
import os, re, glob
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
files = sorted(sum([glob.glob(os.path.join(TXT, y+"_*.txt")) for y in ("2013","2014","2015")], []))
pats = {
 "solve 5 out of 6 / choose 5": r"solve\s+5\s+out\s+of\s+the\s+following\s+6|choose\s+5|Solve\s+5\s+out\s+of\s+6",
 "as many problems as you can": r"as\s+many\s+problems\s+as\s+you\s+can",
 "Please solve the following 5": r"solve\s+the\s+following\s+5\s+problems",
 "This exam of 160 points": r"160\s+points",
 "This exam of 6 problems": r"exam\s+of\s+6\s+problems",
 "highest 5 scores counted": r"highest\s+5\s+scores",
 "5 problems (title)": r"Individual\s*\(5\s+problems\)|Team\s*\(5\s+problems\)",
 "page separators": r"===\s*page\s+\d+\s*===",
}
for y in ("2013","2014","2015"):
    sub = [f for f in files if os.path.basename(f).startswith(y)]
    print("### " + y + "  files=%d  chars=%d  pages=%d" % (
        len(sub),
        sum(len(open(f,encoding='utf-8',errors='replace').read()) for f in sub),
        sum(len(re.findall(pats["page separators"], open(f,encoding='utf-8',errors='replace').read())) for f in sub)))
    for k,p in pats.items():
        if k=="page separators": continue
        c = sum(len(re.findall(p, open(f,encoding='utf-8',errors='replace').read(), re.I)) for f in sub)
        if c: print("    %-34s %d" % (k, c))
print()
allt = "\n".join(open(f,encoding='utf-8',errors='replace').read() for f in files)
for k,p in pats.items():
    print("%-34s %d" % (k, len(re.findall(p, allt, re.I))))
