# -*- coding: utf-8 -*-
import io, os
w = r"E:\deepseek_exclusive\math\.tmp\burn2026\work"
out = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports\referee_geometry.md"
parts = ["ref_geo_part1.md","ref_geo_part2.md","ref_geo_part3.md","ref_geo_part4.md"]
buf = []
for p in parts:
    buf.append(io.open(os.path.join(w,p), encoding="utf-8").read())
txt = "".join(buf)
io.open(out, "w", encoding="utf-8").write(txt)
print("WROTE", out, "chars:", len(txt), "lines:", txt.count(chr(10))+1)
