
import re, os, json, itertools
rows=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_rows_v2.json",encoding='utf-8'))
def shingles(s,k=6):
    w=re.findall(r"[A-Za-z0-9]+", s.lower())
    return set(tuple(w[i:i+k]) for i in range(max(1,len(w)-k+1)))
S={}
for r in rows:
    S[(r['year'],r['kind'],r['n'])]=shingles(r['head'])
keys=list(S)
out=[]
for a,b in itertools.combinations(keys,2):
    A,B=S[a],S[b]
    if not A or not B: continue
    j=len(A&B)/len(A|B)
    if j>=0.06:
        out.append((round(j,3),len(A&B),a,b))
out.sort(reverse=True)
for j,sh,a,b in out[:40]:
    print(f"J={j:.3f} shared={sh:3d}  {a}  <->  {b}")
print("\n-- also compare full problem bodies (need bodies) --")
