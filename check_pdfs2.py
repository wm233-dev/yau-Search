# -*- coding: utf-8 -*-
import fitz, os, io
BASE = r"E:\deepseek_exclusive\math\.tmp\yau\2010-2026历年笔试真题"
files = [r"2013\TeamProblems2013.pdf"]
out=[]
for rel in files:
    p=os.path.join(BASE, rel)
    d=fitz.open(p)
    out.append("FILE: "+rel+" pages="+str(d.page_count))
    for i in range(d.page_count):
        out.append("--- page %d ---"%(i+1))
        out.append(d[i].get_text() or "")
    d.close()
io.open(r"E:\deepseek_exclusive\math\.tmp\burn2026\pdf_check2.txt","w",encoding="utf-8").write("\n".join(out))
print("ok")
