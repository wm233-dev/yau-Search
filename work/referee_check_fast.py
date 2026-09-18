# -*- coding: utf-8 -*-
"""Fast independent checks for the geometry solutions referee report.

(1) Problem 4 (2010 ind. Q1).  With u = -ln|z|, theta = arg z the metric
    |dz|^2/(|z|^2 (ln|z|)^2) becomes (dtheta^2+du^2)/u^2, and
    A=(e^{-2pi},0) -> (0,2pi),  B=(-e^{-pi},0) -> (pi,pi).
    Exact length of a straight segment in (theta,u): L*ln(u2/u1)/(u2-u1).
    Check (a) the semicircle candidate has length arccosh(3/2);
          (b) random perturbations of it are LONGER (local geodesic);
          (c) the L-shaped path (arc at u=2pi then radial) is longer.
(2) Problem 10 remark: the product metric on S^1 x S^2 has sectional
    curvature 0 on mixed planes (so it is NOT a positive-curvature example).
(3) Problem 8 remark: for a helix, lambda = k/(k^2+tau^2), mu = tau/(k^2+tau^2)
    satisfy lambda*k+mu*tau=1, but the offset curve gamma+lambda*n is a STRAIGHT LINE.
"""
import numpy as np, math

print("="*72); print("(1) problem 4 : hyperbolic distance on the punctured disc")
def seg_len(t1,u1,t2,u2):
    dt, du = t2-t1, u2-u1; L = math.hypot(dt,du)
    return L/u1 if abs(du) < 1e-14 else L*math.log(u2/u1)/du
def poly_len(P): return sum(seg_len(*P[i], *P[i+1]) for i in range(len(P)-1))
c = -math.pi; R = math.pi*math.sqrt(5)
for n in (50, 200, 1000, 5000):
    t = np.linspace(0, math.pi, n+1)
    u = np.sqrt(np.maximum(R*R-(t-c)**2, 0.0))
    P = np.column_stack([t,u]); P[0] = (0.0, 2*math.pi); P[-1] = (math.pi, math.pi)
    print("   semicircle candidate, n=%5d : length = %.9f" % (n, poly_len(P)))
print("   arccosh(3/2) = %.9f" % math.acosh(1.5))
# perturbation test
t = np.linspace(0, math.pi, 2001); u = np.sqrt(np.maximum(R*R-(t-c)**2,0.0))
P0 = np.column_stack([t,u]); P0[0]=(0.0,2*math.pi); P0[-1]=(math.pi,math.pi)
base = poly_len(P0); rng = np.random.default_rng(7); worse = 0; best = 1e9
for _ in range(400):
    Q = P0.copy(); k = rng.integers(1, len(Q)-1)
    Q[k,0] += rng.normal(0,0.02); Q[k,1] += rng.normal(0,0.05)
    if Q[k,1] <= 0.05: continue
    L = poly_len(Q); best = min(best,L); worse += (L > base)
print("   perturbations: %d/400 are longer, shortest perturbed length = %.9f (base %.9f)"
      % (worse, best, base))
# L-shaped path: arc at u = 2pi, then radial
n=2000; t=np.linspace(0,math.pi,n+1); u=np.full(n+1,2*math.pi)
P=np.column_stack([t,u]); P[0]=(0.0,2*math.pi); P[-1]=(math.pi,math.pi)
print("   L-shaped path (arc at u=2pi then radial) : length = %.6f" % poly_len(P))
print("   same-ray self-check: radial (0,2pi)->(0,pi) length = %.6f  (ln2 = %.6f)"
      % (seg_len(0,2*math.pi,0,math.pi), math.log(2)))

print("="*72); print("(2) problem 10 remark : sectional curvature of S^1(r) x S^2")
def christoffel(g, x, h=1e-5):
    n=len(x); dg=np.zeros((n,n,n))
    for k in range(n):
        xp=list(x); xp[k]+=h; xm=list(x); xm[k]-=h
        dg[k]=(g(xp)-g(xm))/(2*h)
    ginv=np.linalg.inv(g(x)); G=np.zeros((n,n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                G[i,j,k]=0.5*sum(ginv[i,l]*(dg[j][l,k]+dg[k][l,j]-dg[l][j,k]) for l in range(n))
    return G
def riemann(g, x, h=1e-4):
    n=len(x); G0=christoffel(g,x); dG=np.zeros((n,n,n,n))
    for m in range(n):
        xp=list(x); xp[m]+=h; xm=list(x); xm[m]-=h
        dG[m]=(christoffel(g,xp)-christoffel(g,xm))/(2*h)
    Rm=np.zeros((n,n,n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    Rm[i,j,k,l]=dG[k][i,j,l]-dG[l][i,j,k]
                    for a in range(n):
                        Rm[i,j,k,l]+=G0[i,k,a]*G0[a,j,l]-G0[i,l,a]*G0[a,j,k]
    return Rm, g(x)
# coordinates (t, theta, phi) on S^1(r) x S^2, metric diag(r^2, 1, sin^2 theta)
r = 2.4
g = lambda x: np.diag([r*r, 1.0, math.sin(x[1])**2])
x0 = [0.3, 1.1, 0.4]
Rm, gx = riemann(g, x0)
def sec(Rm,gx,v,w):
    n=len(v); V=np.zeros((n,n,n,n))
    num=sum(Rm[i,j,k,l]*v[i]*w[j]*w[k]*v[l] for i in range(n) for j in range(n) for k in range(n) for l in range(n))
    vv=sum(gx[i,j]*v[i]*v[j] for i in range(n) for j in range(n))
    ww=sum(gx[i,j]*w[i]*w[j] for i in range(n) for j in range(n))
    vw=sum(gx[i,j]*v[i]*w[j] for i in range(n) for j in range(n))
    return num/(vv*ww-vw*vw)
print("   sec(d/dt, d/dtheta) [mixed plane]        = %.3e   <-- 0, not > 0" % sec(Rm,gx,[1,0,0],[0,1,0]))
print("   sec(d/dtheta, d/dphi) [S^2 plane]        = %.6f   (should be 1)" % sec(Rm,gx,[0,1,0],[0,0,1]))

print("="*72); print("(3) problem 8 remark : the degenerate Bertrand offset")
a, b = 1.3, 0.7                      # helix: gamma(s) = (a cos(s/c), a sin(s/c), b s/c)
cc = math.sqrt(a*a+b*b)
k, tau = a/cc**2, b/cc**2
lam, mu = k/(k*k+tau*tau), tau/(k*k+tau*tau)
print("   helix k = %.6f, tau = %.6f ; lambda = %.6f, mu = %.6f ; lambda*k+mu*tau = %.9f"
      % (k, tau, lam, mu, lam*k+mu*tau))
def gamma(s):  return np.array([a*math.cos(s/cc), a*math.sin(s/cc), b*s/cc])
def nrm(s):    return np.array([-math.cos(s/cc), -math.sin(s/cc), 0.0])
def D(s):      return gamma(s) + lam*nrm(s)
h = 1e-4
maxcurv = 0.0
for s in np.linspace(0, 12, 25):
    d1 = (D(s+h)-D(s-h))/(2*h); d2 = (D(s+h)-2*D(s)+D(s-h))/h**2
    curv = np.linalg.norm(np.cross(d1,d2))/np.linalg.norm(d1)**3
    maxcurv = max(maxcurv, curv)
print("   curvature of the offset curve gamma+lambda*n : max = %.3e  (0 => straight line, no principal normal)"
      % maxcurv)
# non-degenerate choice lambda = 1/k, mu = 0
lam2 = 1.0/k
D2 = lambda s: gamma(s) + lam2*nrm(s)
mx = 0.0
for s in np.linspace(0, 12, 25):
    d1=(D2(s+h)-D2(s-h))/(2*h); d2=(D2(s+h)-2*D2(s)+D2(s-h))/h**2
    mx = max(mx, np.linalg.norm(np.cross(d1,d2))/np.linalg.norm(d1)**3)
print("   curvature of gamma+(1/k)*n (mu=0)            : max = %.6f (>0: genuine Bertrand mate)" % mx)
