# -*- coding: utf-8 -*-
import os, re, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')
TXT = 'E:/deepseek_exclusive/math/.tmp/burn2026/txt/'
files = sorted(f for f in os.listdir(TXT) if f.endswith('.txt'))
papers = [f for f in files if 'soln' not in f.lower() and 'Solution' not in f]

pats = {
 'Schrodinger(loose)': r'din\s*ger|Schr|odinger',
 'Noether': r'Noether',
 'particle (of mass)': r'particle of mass|mass m|particle of charge',
 'electric charge/field': r'electric charge|electric ﬁeld|electric field',
 'photon/light/optics': r'photon|light ray|refractive|optics|polariz',
 'atomic/Bohr': r'Bohr|atomic|hydrogen atom',
 'Fermi/Bose': r'Fermi|Bose|boson|fermion',
 'ideal gas/thermo': r'ideal gas|temperature T|Boltzmann',
 'special functions (Legendre/Bessel)': r'Legendre|Bessel|Hermite|spherical harmonic',
 'variational principle': r'variational principle|least action|principle of least',
 'Killing/geodesic in phys sense': r'geodesic',
 'conserved quantity/current': r'conserved|conservation law|Noether current',
 'Feynman integral/path integral': r'path integral|Feynman',
 'symplectic/Hamilton eq': r"Hamilton'?s? equation|canonical|symplectic",
 'scattering/cross section': r'scattering|cross section|S-matrix',
 'uncertainty principle': r'uncertainty',
 'commutator/operator algebra': r'operator|\(A, ?B\)|\[A, ?B\]',
 'de Broglie/wavelength': r'wavelength|de Broglie',
 'tensor/index notation': r'energy momentum|energy-momentum|stress-energy',
}

print('### loose physics-topic probing (papers only, all 17 years)')
for k, p in pats.items():
    d = defaultdict(int)
    for f in papers:
        t = open(TXT+f, encoding='utf-8', errors='replace').read()
        c = len(re.findall(p, t))
        if c: d[f[:4]] += c
    s = ' '.join(f'{y}:{d[y]}' for y in sorted(d))
    print(f'{k:38s} : {sum(d.values()):4d} | {s}')

print()
print('### files containing "dinger"/"Noether"')
for f in files:
    t = open(TXT+f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'.{60}(?:dinger|Noether).{60}', t):
        print(f'  [{f}] ...{m.group(0).replace(chr(10)," ")}...')
