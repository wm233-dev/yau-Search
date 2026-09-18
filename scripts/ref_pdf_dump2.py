
import os, sys
sys.path.insert(0, r"E:\deepseek_exclusive\math\pylibs")
import fitz
root = r"F:\丘成桐大学生数学竞赛历年笔试真题"
out = open(r"E:\deepseek_exclusive\math\.tmp\burn2026\work\ref_pdf_dump2.txt","w",encoding="utf-8")
for y in ["2021","2014","2016","2019"]:
    d = os.path.join(root,y)
    for f in sorted(os.listdir(d)):
        if not f.lower().endswith(".pdf"): continue
        if "analysis" not in f.lower() and "Analysis" not in f: continue
        p = os.path.join(d,f)
        out.write("#"*90+"\n## %s / %s\n" % (y,f))
        try:
            doc = fitz.open(p)
            for i in range(doc.page_count):
                out.write("---- page %d ----\n"%(i+1))
                out.write(doc[i].get_text())
        except Exception as e:
            out.write("ERR %r\n"%e)
out.close()
print("ok")
