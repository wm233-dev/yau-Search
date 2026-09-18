
import os
base = r"."
for f in ["_p1.md","_p2.md","_p3.md","_merge.py","_verify.py","_chk.py","_chk2.py","_chk3.py","_chk4.py","_chk5.py","_chk6.py","_chk7.py","_xsub_dump.md"]:
    p = os.path.join(base,f)
    if os.path.exists(p):
        os.remove(p); print("removed", f)
print("remaining scratch:", [f for f in os.listdir(base) if f.startswith("_")])
