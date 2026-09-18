
import os
for root in [r"E:\deepseek_exclusive\math"]:
    for d in sorted(os.listdir(root)):
        p=os.path.join(root,d)
        if os.path.isdir(p):
            try: n=len(os.listdir(p))
            except: n=-1
            print(f"{'DIR ' if True else ''}{d}  ({n} entries)")
