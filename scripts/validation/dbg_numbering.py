# -*- coding: utf-8 -*-
import os, io, re
TXT = r".\txt"
LIG = {"\ufb01":"fi","\ufb02":"fl","\ufb00":"ff","\ufb03":"ffi","\ufb04":"ffl"}
def norm(s):
    for k,v in LIG.items(): s = s.replace(k,v)
    return s.replace("\r\n","\n")
RE_A = re.compile(r"(?m)^[ \t]*(?:Problem[ \t]*)?(\d{1,2})[.、][ \t]")
RE_B = re.compile(r"(?m)^[ \t]*(\d{1,2})[)][ \t]")
RE_C = re.compile(r"(?m)^[ \t]*(?:Problem[ \t]*)(\d{1,2})\b")
targets = ["2019_Algebra2019_individual","2020_Algebra_NumberTheory_algebra_and_numbertheory_20",
           "2021_ExamPaper_21S_algebra_and_numbertheory_21s","2022_ExamPaper_2022_algebra_and_numbertheory_22s",
           "2024_2024_Algebra","2025_algebra","2026_2026_Algebra_and_Number_Theory","2023_Algebra_Number_theory"]
for t in targets:
    p = os.path.join(TXT, t + ".txt")
    s = norm(io.open(p, encoding="utf-8").read())
    for nm, rx in (("A",RE_A),("B",RE_B),("C",RE_C)):
        nums = [int(m.group(1)) for m in rx.finditer(s)]
        print(t, nm, "n=", len(nums), nums[:14])
    print("  first120:", " ".join(s.split())[:120])
