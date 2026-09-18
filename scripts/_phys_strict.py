# -*- coding: utf-8 -*-
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))

STRICT = {
 'Lagrangian': r'Lagrangian',
 'Hamiltonian': r'Hamiltonian',
 'Killing': r'Killing',
 'Einstein(phys)': r'Einstein metric|Einstein equation|Einstein.{0,12}curvature depends',
 'cosmological': r'cosmolog',
 'eigenstate/wavefunction': r'eigenstate|wave ?function',
 'quantum': r'\bquantum\b',
 'Maxwell': r'Maxwell',
 'vector potential/gauge': r'vector potential|gauge (transformation|ﬁeld|field|invariant)',
 'E&M fields': r'electric (ﬁeld|field)|magnetic (ﬁeld|field)|electromagnetic|polariz',
 'Schrodinger': r'Schr',
 'Planck': r'Planck',
 'partition function': r'partition function',
 'entropy': r'entropy',
 'Ising': r'Ising',
 'heat capacity': r'heat capacity|speciﬁc heat|specific heat',
 'thermodynamic/phase transition': r'thermodynamic|phase transition|coexist',
 'Feynman/propagator': r'Feynman|propagator',
 'renormaliz/loop': r'renormaliz|one[- ]loop',
 'scalar ﬁeld': r'scalar ﬁeld|scalar field',
 'black hole': r'black hole',
 'gravitational wave': r'gravitational wave',
 'energy-momentum tensor': r'energy momentum|energy-momentum|stress-energy',
 'boson/fermion/photon': r'boson|fermion|photon',
 'harmonic oscillator': r'harmonic oscillator',
 'symplectic/Hamilton eq': r'symplectic|Hamilton.{0,3}s equation|canonical momentum',
 'normal mode/small osc': r'small oscillation|normal mode|frequency of small',
 'central potential/orbit': r'central potential|circular orbit|eﬀective potential|effective potential',
 'conserved quantity': r'conserved quantit|constant of motion|conservation of (energy|angular)',
 'uncertainty': r'uncertainty principle',
 'heat/diﬀusion eq': r'heat equation|diﬀusion equation|diffusion equation',
 'ideal gas/Boltzmann': r'ideal gas|Boltzmann|temperature T',
}
res = []
for p in full:
    if p['subject'] == 'Mathematical Physics': continue
    t = p.get('text', '')
    hits = [k for k, pat in STRICT.items() if re.search(pat, t)]
    if hits:
        res.append((p['year'], p['subject'], p['paper'], p['n'], hits, t))
from collections import defaultdict
byyear = defaultdict(list)
for y, s, pap, n, hits, t in res:
    byyear[y].append((s, pap, n, hits))
print('files/subject-questions with >=1 strict physics keyword:', len(res))
for y in sorted(byyear):
    for s, pap, n, hits in byyear[y]:
        print(f'{y} | {s:24s} | Q{n:2d} | {hits}')
