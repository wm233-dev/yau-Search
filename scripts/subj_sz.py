
import os
B = r"E:\deepseek_exclusive\math\.tmp\burn2026\reports"
for f in sorted(os.listdir(B)):
    p=os.path.join(B,f)
    print(f"{os.path.getsize(p):8d}  {f}")
