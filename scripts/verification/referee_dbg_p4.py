# -*- coding: utf-8 -*-
import numpy as np, heapq, math
def dbg(nrho, nth, rho_lo, rho_hi, r_src, r_dst, ang_dst):
    rho = np.exp(np.linspace(math.log(rho_lo), math.log(rho_hi), nrho))
    dth = 2*math.pi/nth; lrho = np.log(rho)
    sr = np.abs(np.diff(rho)) / (0.5*(rho[:-1]+rho[1:]) * np.abs(0.5*(lrho[:-1]+lrho[1:])))
    st = rho*dth/np.abs(lrho)
    i_src = int(np.argmin(np.abs(rho - r_src))); j_src = 0
    i_dst = int(np.argmin(np.abs(rho - r_dst))); j_dst = int(round(ang_dst/(2*math.pi)*nth)) % nth
    print("i_src,i_dst,j_dst =", i_src, i_dst, j_dst, "rho near src/dst:", rho[i_src], rho[i_dst], "target", r_src, r_dst)
    print("sr range", sr.min(), sr.max(), "st range", st.min(), st.max())
    def idx(i,j): return i*nth + (j % nth)
    D = np.full(nrho*nth, float("inf")); D[idx(i_src,j_src)] = 0.0
    pq = [(0.0, i_src, j_src)]; popped=0
    while pq:
        d, i, j = heapq.heappop(pq); popped += 1
        if d > D[idx(i,j)] + 1e-15: continue
        if (i,j) == (i_dst,j_dst):
            print("reached in", popped, "pops, d =", d); return
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            i2, j2 = i+di, j+dj
            if i2 < 0 or i2 >= nrho: continue
            if di == 0: l = st[i]
            elif dj == 0: l = sr[i] if di == 1 else sr[i-1]
            else:
                rstep = sr[i] if di == 1 else sr[i-1]
                l = rstep + 0.5*(st[i] + st[i2])
            nd = d + l; k2 = idx(i2,j2)
            if nd < D[k2] - 1e-15:
                D[k2] = nd; heapq.heappush(pq, (nd, i2, j2))
    print("EXHAUSTED after", popped, "pops; D[dst] =", D[idx(i_dst,j_dst)])
dbg(300, 720, 1e-11, 0.9, math.exp(-2*math.pi), math.exp(-math.pi), math.pi)
