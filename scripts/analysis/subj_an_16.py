
# -*- coding: utf-8 -*-
import os, re, json, collections
exec(open(r".\scripts\subj_an_13.py",encoding="utf-8").read().split("def split_problems")[0])
ALL = "\n".join(t for (y,p),t in sorted(secs.items()))
NAMES = ["Schwarz","Pick","Harnack","Liouville","Picard","Riemann mapping","Riemann map","Montel","Phragmen","Phragm\u00e9n","Hadamard","Mittag","Runge","Weierstrass","Blaschke","Jensen","Rouche","Rouch\u00e9","Riesz","Hahn","Banach-Steinhaus","Banach\u2013Steinhaus","Baire","Alaoglu","Fredholm","Arzel","Ascoli","Sobolev","Rellich","Kondrachov","Poincar\u00e9","Poincare","Lax","Milgram","Gronwall","Fubini","Tonelli","Radon","Carath","Borel","Cantelli","Vitali","Hardy","Littlewood","BMO","Calder","Zygmund","Schauder","Hopf","Karamata","Pompeiu","Cauchy","Rukowski","Green","Newton","Laplace","Poisson","Euler","Lagrange","Stokes","Gauss","Plancherel","Parseval","Fourier","Holder","H\u00f6lder","Minkowski","Jensen","Young","Fatou","Du Bois","Bocher","B\u00f4cher","Weyl","Abel","Fejer","F\u00e9jer","Riemann","Dirichlet","Neumann","Bernstein","Hyers","Ulam","Hilbert","Banach","Stone","Brouwer"]
print("NAMED-OBJECT SCAN (analysis problem statements, 27 sections)")
for nm in NAMES:
    yrs=[]
    for (y,p),t in sorted(secs.items()):
        if re.search(re.escape(nm), t, flags=re.I): yrs.append(y)
    if yrs: print(f"{nm}\t{sorted(set(yrs))}")
print("\n--- NOT FOUND in analysis problem statements ---")
print([nm for nm in NAMES if not any(re.search(re.escape(nm), t, flags=re.I) for t in secs.values())])
