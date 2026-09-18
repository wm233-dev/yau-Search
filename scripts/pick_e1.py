# -*- coding: utf-8 -*-
import os, re
TXT = r"E:\deepseek_exclusive\math\.tmp\burn2026\txt"
t = open(os.path.join(TXT,"2014_algebra2014_team.txt"), encoding="utf-8", errors="replace").read()
m = re.search(r"Problem 6\..*", t, re.S)
print(repr(t[t.find("Problem 6"):t.find("Problem 6")+40]))
print("-----")
print(m.group(0).strip() if m else "none")
