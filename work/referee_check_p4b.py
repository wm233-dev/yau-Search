# -*- coding: utf-8 -*-
"""Independent numerical verification of problem 4 (2010 individual Q1).

The punctured-disc metric ds^2 = |dz|^2/(|z|^2 (ln|z|)^2) becomes, in the
coordinates (theta, u) with u = -ln|z|, theta = arg z, exactly
        ds^2 = (dtheta^2 + du^2)/u^2 .
A = (e^{-2pi}, 0)  ->  (theta,u) = (0, 2pi);   B = (-e^{-pi},0) -> (pi, pi).

We minimise length over polylines with fixed endpoints (exact segment length
for a straight segment in (theta,u): |seg| * ln(u2/u1)/(u2-u1)) by coordinate
descent with golden-section line search.  The infimum over polylines -> the
true geodesic distance (from above).
"""
import numpy as np, math

def seg_len(t1,u1,t2,u2):
    dt, du = t2-t1, u2-u1
    L = math.hypot(dt, du)
    if abs(du) < 1e-12: return L/u1
    return L*math.log(u2/u1)/du

def poly_len(P):
    return sum(seg_len(P[i,0],P[i,1],P[i+1,0],P[i+1,1]) for i in range(len(P)-1))

def minimise(A, B, n, sweeps=60, init="line", seed=0):
    rng = np.random.default_rng(seed)
    t = np.linspace(A[0], B[0], n+1); u = np.linspace(A[1], B[1], n+1)
    if init == "arc":                      # semicircle guess in (theta,u)
        c = -math.pi; R = math.pi*math.sqrt(5)
        t = np.linspace(0, math.pi, n+1)
        u = np.sqrt(np.maximum(R*R-(t-c)**2, 1e-6))
    P = np.column_stack([t,u]); P[0] = A; P[-1] = B
    P[1:-1] += rng.normal(0, 0.02, size=(n-1,2))*np.array([0.1,1.0])
    best = poly_len(P)
    step = 0.5
    for s in range(sweeps):
        for i in range(1, n):
            for k in (0,1):
                lo, hi = -step, step
                for _ in range(28):        # golden-section on one coordinate
                    m1 = lo + 0.382*(hi-lo); m2 = lo + 0.618*(hi-lo)
                    old = P[i,k]
                    P[i,k] = old + m1; f1 = poly_len(P)
                    P[i,k] = old + m2; f2 = poly_len(P)
                    if f1 < f2: hi = m2
                    else:       lo = m1
                    P[i,k] = old
                cand = P[i,k] + 0.5*(lo+hi)
                oldv = P[i,k]; P[i,k] = cand; f = poly_len(P)
                if f < best: best = f
                else: P[i,k] = oldv
        step *= 0.7
    return best, P

for label, A, B in (("A=(0,2pi) B=(pi,pi)  [the two given points]", (0.0,2*math.pi), (math.pi,math.pi)),
                    ("A=(0,2pi) B=(0,pi)   [same ray, self-check]",    (0.0,2*math.pi), (0.0,math.pi))):
    print(label)
    for init in ("line","arc"):
        for n in (20, 60, 150):
            val,_ = minimise(A,B,n, sweeps=40, init=init, seed=1)
            print("   start=%-5s n=%3d  -> length = %.6f" % (init, n, val))
print()
print("handout claims: %.6f  (= arccosh(3/2))  and  %.6f (= ln 2)"
      % (math.acosh(1.5), math.log(2)))
