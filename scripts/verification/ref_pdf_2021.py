
import os, sys
sys.path.insert(0, r"sources/pylibs")
import fitz
root = r"sources/prelim\2021"
print(os.listdir(root))
out = open(r"./archive/work/ref_pdf_2021.txt","w",encoding="utf-8")
for f in sorted(os.listdir(root)):
    if not f.lower().endswith(".pdf"): continue
    p = os.path.join(root,f)
    out.write("#"*80+"\n## "+f+"\n")
    try:
        doc = fitz.open(p)
        for i in range(doc.page_count):
            out.write("---- page %d ----\n"%(i+1)); out.write(doc[i].get_text())
    except Exception as e:
        out.write("ERR %r\n"%e)
out.close()
print("ok")
