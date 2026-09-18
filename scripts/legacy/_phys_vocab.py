# -*- coding: utf-8 -*-
import os, re, sys, json
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding='utf-8')
TXT = './corpus/prelim/'
files = sorted(f for f in os.listdir(TXT) if f.endswith('.txt'))

def yr(f): return f[:4]

# ---------- A. where does "Mathematical Physics" appear as a title? ----------
print('### A. files whose text contains "Mathematical Physics"')
for f in files:
    t = open(TXT+f, encoding='utf-8', errors='replace').read()
    if re.search(r'Mathematical\s+Physics', t):
        print('   ', f)

# ---------- B. physics vocabulary across ALL years (papers only, no soln) ----------
KW = {
 'Lagrangian': r'Lagrangian',
 'Hamiltonian': r'Hamiltonian',
 'action/S=∫': r'\baction\b',
 'Euler-Lagrange': r'Euler[- ]Lagrange',
 'Killing vector': r'Killing',
 'Einstein equation': r"Einstein'?s?\s+equation|Einstein equation|R_?\{?\\?mu",
 'Ricci': r'Ricci',
 'scalar curvature': r'scalar curvature',
 'cosmological const': r'cosmological',
 'metric ds^2': r'ds2|ds\^2',
 'Schrodinger': r'Schr[oö]dinger|Schrodinger',
 'wave function': r'wave\s*function|wavefunction',
 'quantum': r'quantum',
 'eigenstate': r'eigenstate',
 'harmonic oscillator': r'harmonic oscillator',
 'commutator': r'commutator|commutation relation',
 'perturbation theory': r'perturbation',
 'Maxwell': r'Maxwell',
 'vector potential': r'vector potential|gauge',
 'electromagnetic': r'electric ﬁeld|electric field|magnetic ﬁeld|electromagnetic',
 'special relativity/Lorentz': r'Lorentz|relativistic|Minkowski',
 'statistical mech/partition fn': r'partition function',
 'entropy': r'entropy',
 'Ising': r'Ising',
 'heat capacity': r'heat capacity|speciﬁc heat|specific heat',
 'thermodynamic': r'thermodynamic',
 'phase transition': r'phase transition',
 'Feynman diagram': r'Feynman',
 'propagator': r'propagator',
 'renormaliz': r'renormaliz',
 'loop/dimensional reg': r'one[- ]loop|dimensional regularization',
 'scalar field': r'scalar ﬁeld|scalar field',
 'gauge field/Yang-Mills': r'Yang[- ]Mills|gauge ﬁeld|gauge field',
 'supersymmetry': r'supersymmetr',
 'string theory': r'string theory|worldsheet',
 'black hole': r'black hole',
 'gravitational wave': r'gravitational wave',
 'Noether': r'Noether',
 'Bohr/Planck/de Broglie': r'Planck|Bohr|de Broglie',
 'spin': r'\bspin\b',
 'angular momentum': r'angular momentum',
 'Fourier heat/diffusion': r'heat equation|diﬀusion equation|diffusion equation',
}
print()
print('### B. physics vocabulary per file (papers only)')
hits = defaultdict(dict)
for f in files:
    if 'soln' in f.lower() or 'Solution' in f: continue
    t = open(TXT+f, encoding='utf-8', errors='replace').read()
    y = yr(f)
    for k, pat in KW.items():
        c = len(re.findall(pat, t))
        if c: hits[k][y] = hits[k].get(y, 0) + c
for k in KW:
    d = hits[k]
    if not d: 
        print(f'{k:32s} : NEVER (0 hits in all 120 papers)')
        continue
    tot = sum(d.values())
    ys = ' '.join(f'{y}:{d[y]}' for y in sorted(d))
    print(f'{k:32s} : total={tot:4d} | {ys}')
