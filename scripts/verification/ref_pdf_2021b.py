
import os, sys
sys.path.insert(0, r"sources/pylibs")
import fitz
out = open(r"./archive/work/ref_pdf_2021.txt","w",encoding="utf-8")
for sub in ["ExamPaper_21S","Solution_21S"]:
    root = os.path.join(r"sources/prelim\2021", sub)
    out.write("="*90+"\nSUBDIR %s : %s\n" % (sub, os.listdir(root)))
    for f in sorted(os.listdir(root)):
        p = os.path.join(root,f)
        out.write("#"*80+"\n## "+f+"\n")
        if f.lower().endswith(".pdf"):
            try:
                doc = fitz.open(p)
                for i in range(doc.page_count):
                    out.write("---- page %d ----\n"%(i+1)); out.write(doc[i].get_text())
            except Exception as e:
                out.write("ERR %r\n"%e)
out.close()
print("ok")
