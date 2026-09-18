# -*- coding: utf-8 -*-
"""Numeric verification for problem 3 (2026 Q1): Area(N(A_e))/Area(A_e) -> |K(p)|."""
import numpy as np

def make_case(name, f, fx, fy, fxx, fxy, fyy):
    return dict(name=name, f=f, fx=fx, fy=fy, fxx=fxx, fxy=fxy, fyy=fyy)

cases = [
  make_case("paraboloid z=x^2+y^2 (K(0)=4)",
     lambda x,y: x*x+y*y, lambda x,y: 2*x, lambda x,y: 2*y,
     lambda x,y: 2.0*x*0+2.0, lambda x,y: 0.0*x, lambda x,y: 2.0*x*0+2.0),
  make_case("saddle z=xy (K(0)=-1)",
     lambda x,y: x*y, lambda x,y: y, lambda x,y: x,
     lambda x,y: 0.0*x, lambda x,y: 0.0*x+1.0, lambda x,y: 0.0*x),
  make_case("monkey saddle z=x^3-3xy^2 (K(0)=0, N 2-to-1)",
     lambda x,y: x**3-3*x*y*y, lambda x,y: 3*x*x-3*y*y, lambda x,y: -6*x*y,
     lambda x,y: 6*x, lambda x,y: -6*y, lambda x,y: -6*x),
  make_case("flat quartic z=x^4+y^4 (K(0)=0, N injective)",
     lambda x,y: x**4+y**4, lambda x,y: 4*x**3, lambda x,y: 4*y**3,
     lambda x,y: 12*x*x, lambda x,y: 0.0*x, lambda x,y: 12*y*y),
]

N = 1600           # grid resolution on [-r,r]^2
def run(case, r):
    xs = np.linspace(-r, r, N)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    mask = (X*X+Y*Y) <= r*r
    fx = case["fx"](X,Y); fy = case["fy"](X,Y)
    fxx = case["fxx"](X,Y); fxy = case["fxy"](X,Y); fyy = case["fyy"](X,Y)
    W = 1.0 + fx*fx + fy*fy
    dA = np.sqrt(W)
    K = (fxx*fyy - fxy*fxy)/(W*W)
    cell = (2*r/(N-1))**2
    AreaA = dA[mask].sum()*cell
    J = (np.abs(K)*dA)[mask].sum()*cell            # multiplicity-weighted image area
    # image area estimate by fine binning of the Gauss image in the (p,q) chart
    p = -fx[mask]; q = -fy[mask]
    if p.size == 0: return None
    h = max((p.max()-p.min()), (q.max()-q.min()))/400.0
    if h <= 0: h = 1e-9
    ip = np.floor((p-p.min())/h).astype(np.int64); iq = np.floor((q-q.min())/h).astype(np.int64)
    key = ip.astype(np.int64)*100000 + iq
    uk, counts = np.unique(key, return_counts=True)
    up = p.min() + (uk//100000 + 0.5)*h; uq = q.min() + (uk % 100000 + 0.5)*h
    AreaImg = (h*h/(1.0+up*up+uq*uq)**1.5).sum()
    return AreaA, J, AreaImg, J/AreaA

print("== Problem 3 numeric test: ratio Area(N(A))/Area(A) for shrinking parameter disks ==")
for c in cases:
    print("\n---", c["name"], " K(0) =", end=" ")
    K0 = (c["fxx"](0.0,0.0)*c["fyy"](0.0,0.0)-c["fxy"](0.0,0.0)**2)/(1.0+c["fx"](0.0,0.0)**2+c["fy"](0.0,0.0)**2)**2
    print(K0)
    print(" r        Area(A)      J=int|K|dA   J/Area(A)   Area(Image)   ratio=Img/Area(A)")
    for r in (0.4, 0.2, 0.1, 0.05, 0.025, 0.0125):
        A, J, Img, wmean = run(c, r)
        print(" %-8.5g %-11.5g %-11.5g %-11.5g %-13.5g %-11.5g" % (r, A, J, wmean, Img, Img/A))
