# -*- coding: utf-8 -*-
"""Independent numeric check of problem 4 (2010 Q1).
   ds^2 = |dz|^2/(|z|^2 (ln|z|)^2).  In polar coords (rho,theta):
      radial  : d rho/(rho |ln rho|)      angular : d theta/|ln rho|   (the rho cancels!)
   Dijkstra on the polar grid gives an upper bound converging to the true distance."""
import numpy as np, heapq, math

def grid_dist(nrho, nth, rho_lo, rho_hi, r_src, r_dst, ang_dst):
    rho = np.exp(np.linspace(math.log(rho_lo), math.log(rho_hi), nrho))
    dth = 2*math.pi/nth; lrho = np.log(rho)
    sr = np.abs(np.diff(rho)) / (0.5*(rho[:-1]+rho[1:]) * np.abs(0.5*(lrho[:-1]+lrho[1:])))
    st = dth/np.abs(lrho)                      # <-- corrected: no factor rho
    i_src = int(np.argmin(np.abs(rho - r_src))); j_src = 0
    i_dst = int(np.argmin(np.abs(rho - r_dst))); j_dst = int(round(ang_dst/(2*math.pi)*nth)) % nth
    tgt = i_dst*nth + j_dst
    D = np.full(nrho*nth, float("inf")); D[i_src*nth + j_src] = 0.0
    pq = [(0.0, i_src, j_src)]
    while pq:
        d, i, j = heapq.heappop(pq)
        k = i*nth + (j % nth)
        if d > D[k] + 1e-15: continue
        if k == tgt: return d
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            i2, j2 = i+di, j+dj
            if i2 < 0 or i2 >= nrho: continue
            if di == 0:      l = st[i]
            elif dj == 0:    l = sr[i] if di == 1 else sr[i-1]
            else:
                rstep = sr[i] if di == 1 else sr[i-1]
                l = rstep + 0.5*(st[i] + st[i2])
            nd = d + l; k2 = i2*nth + (j2 % nth)
            if nd < D[k2] - 1e-15:
                D[k2] = nd; heapq.heappush(pq, (nd, i2, j2))
    return None

for nrho, nth in ((400,720), (800,1440), (1600,2880)):
    d1 = grid_dist(nrho, nth, 1e-12, 0.9, math.exp(-2*math.pi), math.exp(-math.pi), math.pi)
    d2 = grid_dist(nrho, nth, 1e-12, 0.9, math.exp(-2*math.pi), math.exp(-math.pi), 0.0)
    print("grid %4dx%4d : d(A,B)=%.6f   d(A,(e^-pi,0))=%.6f" % (nrho, nth, d1, d2))
print()
print("handout: d(A,B) = arccosh(3/2) = %.6f ; self-check d(A,(e^-pi,0)) = ln2 = %.6f"
      % (math.acosh(1.5), math.log(2)))
