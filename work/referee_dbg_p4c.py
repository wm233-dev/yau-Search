# -*- coding: utf-8 -*-
"""Dijkstra directly on the (theta,u) grid with metric (du^2+dtheta^2)/u^2."""
import numpy as np, heapq, math

def dij(nu, nth, u_lo, u_hi, src, dst, label):
    u = np.linspace(u_lo, u_hi, nu); dth = 2*math.pi/nth
    sr = np.abs(np.diff(u))/(0.5*(u[:-1]+u[1:]))
    st = dth/u
    i_src = int(np.argmin(np.abs(u-src[1]))); j_src = int(round(src[0]/dth)) % nth
    i_dst = int(np.argmin(np.abs(u-dst[1]))); j_dst = int(round(dst[0]/dth)) % nth
    tgt = i_dst*nth + j_dst
    D = np.full(nu*nth, float("inf")); D[i_src*nth+j_src] = 0.0
    pq = [(0.0, i_src, j_src)]
    while pq:
        d, i, j = heapq.heappop(pq)
        k = i*nth + (j % nth)
        if d > D[k] + 1e-15: continue
        if k == tgt:
            print("%-28s grid(%dx%d) -> %.6f" % (label, nu, nth, d)); return d
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            i2, j2 = i+di, j+dj
            if i2 < 0 or i2 >= nu: continue
            if di == 0:   l = st[i]
            elif dj == 0: l = sr[i] if di == 1 else sr[i-1]
            else:
                rstep = sr[i] if di == 1 else sr[i-1]
                l = rstep + 0.5*(st[i]+st[i2])
            nd = d + l; k2 = i2*nth + (j2 % nth)
            if nd < D[k2] - 1e-15:
                D[k2] = nd; heapq.heappush(pq, (nd, i2, j2))
    print(label, "UNREACHED"); return None

def hdist(t1,u1,t2,u2): return math.acosh(1+((t2-t1)**2+(u2-u1)**2)/(2*u1*u2))
A = (0.0, 2*math.pi); B = (math.pi, math.pi)
print("exact:", round(hdist(*A,*B),6))
for nu, nth in ((400,720), (800,1440), (1600,2880)):
    dij(nu, nth, 0.05, 30.0, A, B, "A=(0,2pi)->B=(pi,pi)")
for nu, nth in ((800,1440),):
    dij(nu, nth, 0.05, 30.0, (0.0,2*math.pi), (0.0,math.pi), "radial pair (expect ln2)")
    dij(nu, nth, 0.05, 30.0, (0.0,2*math.pi), (math.pi,2*math.pi), "same-radius pair (0.4949)")
