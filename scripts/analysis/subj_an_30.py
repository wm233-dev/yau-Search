
import os
for d in ["自编","丘","exam826","exam912","book_research_clean_restart"]:
    base=os.path.join(r".",d)
    print("### "+d)
    for root,dirs,files in os.walk(base):
        rel=os.path.relpath(root,base)
        lvl=0 if rel=="." else rel.count(os.sep)+1
        if lvl>1:
            dirs[:]=[]; continue
        fs=[f for f in files if not f.startswith(".")]
        print("   ["+rel+"] "+ "; ".join(fs[:18]) + (" ...(%d)"%len(fs) if len(fs)>18 else ""))
        dirs[:]=[x for x in dirs if not x.startswith(".")]
