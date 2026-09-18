# -*- coding: utf-8 -*-
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = './data/'
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))

PHYSRE = re.compile(r'''(
 Lagrangian|Hamiltonian|Killing|Ricci|scalar curvature|Einstein|cosmolog|wave ?function|
 eigenstate|harmonic oscillator|quantum|Maxwell|vector potential|gauge|
 electric (ﬁeld|field)|magnetic (ﬁeld|field)|electromagnetic|Lorentz|Minkowski|relativistic|
 partition function|entropy|Ising|heat capacity|speciﬁc heat|specific heat|thermodynamic|phase transition|
 Feynman|propagator|renormaliz|scalar ﬁeld|scalar field|black hole|gravitational wave|
 energy[- ]momentum|spin|angular momentum|boson|fermion|photon|Schr|Planck|wavelength|
 particle of mass|mass m|electric charge|potential energy|kinetic energy|Newton'?s law|
 harmonic|oscillat|pendulum|gravity|adiabatic|canonical|phase space|symplectic|
 conservation law|conserved|dipole|dielectric|wave equation|refractive|optics|
 uncertainty|Boltzmann|Fermi|Bose|heat (equation|kernel)|temperature|
 normal mode|small oscillation|Binet|Bertrand|effective potential|orbit|cross section|scattering length
)''', re.I | re.X)

cands = []
for p in full:
    if p['subject'] == 'Mathematical Physics': continue
    t = p.get('text', '')
    hits = set(m.group(0).lower() for m in PHYSRE.finditer(t))
    if len(hits) >= 2:
        cands.append((p['year'], p['subject'], p['paper'], p['n'], sorted(hits), t))
print('candidates:', len(cands))
for y, s, pap, n, hits, t in cands:
    print('-' * 70)
    print(f'{y} | {s} | {pap} | Q{n} | hits={hits}')
    print('   ' + t[:420].replace('\n', ' '))
