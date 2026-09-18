# -*- coding: utf-8 -*-
import re, collections
p = r".\reports\2010-2012_丘成桐竞赛笔试真题深度分析.md"
lines = open(p, encoding="utf-8").read().split("\n")
print("总行数:", len(lines))
print("标题行:", [l for l in lines if l.startswith("#")][:12])
bad = []
block = []
for i, l in enumerate(lines, 1):
    if l.startswith("|"):
        block.append((i, l.count("|")))
    else:
        if block:
            cnt = collections.Counter(c for _, c in block)
            if len(cnt) > 1:
                bad.append((block[0][0], block[-1][0], dict(cnt)))
            block = []
print("列数不一致的表格块:", bad if bad else "无")
# 表格行数
tbl = sum(1 for l in lines if l.startswith("|"))
print("表格行数:", tbl)
# 检查是否有遗留占位符/异常字符
for pat in ["TODO", "占位", "XXX", "�"]:
    hits = [i for i, l in enumerate(lines, 1) if pat in l]
    print(pat, "->", hits[:5] if hits else "无")
# 章节完整性
for h in ["## 0.", "## 1.", "## 2.", "## 3.", "## 4.", "## 5.", "## 6."]:
    print(h, "存在" if any(l.startswith(h) for l in lines) else "缺失")
