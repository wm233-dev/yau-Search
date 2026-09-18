
import os
for d in ["一些数学书","自编","丘","exam826","exam912","book_research_clean_restart"]:
    p=os.path.join(r".",d)
    print("###",d)
    for root,dirs,files in os.walk(p):
        for f in files[:40]:
            print("   ", os.path.join(root,f).replace(r".\\",""))
        if len(files)>40: print("    ...",len(files))
