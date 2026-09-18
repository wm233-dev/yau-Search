
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
F = sys.argv[1]; want = sys.argv[2:]
txt = open(F, encoding='utf-8').read()
parts = re.split(r'^[=#]{80,}\s*$', txt, flags=re.M)
for s in parts:
    lines = s.strip().split("\n")
    if not lines or not lines[0].startswith("##"): continue
    if not any(w in lines[0] for w in want): continue
    out = [lines[0]]
    mode = None; nb = 0; nt = 0
    for l in lines[1:]:
        if l.startswith("-- BOOKS"): mode='b'; out.append(l); continue
        if l.startswith("-- TOC"): mode='t'; out.append(l); continue
        if mode=='b':
            if l.startswith("  ["):
                nb += 1
                if nb > 7: continue
                out.append(l.split(" | ")[0] + " | " + " | ".join(l.split(" | ")[1:]))
            # drop fn lines
        elif mode=='t':
            if l.startswith("  ["):
                nt += 1
                if nt > 3: continue
                out.append(l)
            elif l.startswith("      - "):
                if nt <= 3: out.append(l)
    print("="*80); print("\n".join(out))
