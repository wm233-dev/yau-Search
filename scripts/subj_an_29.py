
import os
def tree(d, depth=2, maxf=14):
    base=os.path.join(r"E:\deepseek_exclusive\math",d)
    print("### "+d)
    for root,dirs,files in os.walk(base):
        rel=os.path.relpath(root,base)
        lvl=0 if rel=="." else rel.count(os.sep)+1
        if lvl>depth: 
            dirs[:]=[]
            continue
        fs=[f for f in files if not f.startswith(".")]
        print("  "*lvl + f"[{rel}] " + "; ".join(fs[:maxf]) + (" ..." if len(fs)>maxf else ""))
        dirs[:] = [x for x in dirs if not x.startswith(".")]
for d in ["一些数学书","自编","丘","exam826","exam912","book_research_clean_restart","pages","高代"]:
    try: tree(d)
    except Exception as e: print(d,"ERR",e)
