
import re,os,difflib
exec(open(r".\scripts\prob_twins2.py").read().split("keys=list(store)")[0])
def show(k):
    print("### ",k)
    print(store[k])
    print()
for k in [("2011","individual",3),("2012","team",6),("2012","individual",2),("2015","individual",1)]:
    show(k)
A=store[("2011","individual",3)]; B=store[("2012","team",6)]
sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
print("=== matching blocks longer than 40 between 2011-ind-Q5 and 2012-team-Q6 ===")
for blk in sm.get_matching_blocks():
    if blk.size>40:
        print(blk.size, repr(A[blk.a:blk.a+blk.size]))
