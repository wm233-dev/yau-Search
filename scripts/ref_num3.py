
import math
import numpy as np
xx,ww = np.polynomial.legendre.leggauss(6000)

def g(t): return 0.0 if t<=0 else math.exp(-1.0/t)
def f(t):
    a=g(t); b=g(1-t)
    return a/(a+b) if (a+b)>0 else (0.0 if t<=0 else 1.0)
eta = lambda r: 1.0 if r<=1 else (0.0 if r>=2 else f(2-r))
def etap(r,h=1e-5): return (eta(r+h)-eta(r-h))/(2*h)

n=3; om = 4*math.pi
print("### 题9 full vs B1-only ratio, n=3, eta smooth-flat (eta=1 on r<=1, 0 on r>=2)")
r2 = 0.5*(xx+3)           # [1,2]
e2 = np.array([eta(v) for v in r2])
d2 = np.array([etap(v) for v in r2])
for eps in [0.2,0.1,0.05,0.02,0.01,0.001,1e-4]:
    al = 0.5-eps
    # exact: int_0^1 r^{-2al} dr = 1/(1-2al) = 1/(2eps)
    I1 = 1.0/(2*eps)
    w = 0.5*ww
    J1 = np.sum(w*r2**(-2*al)*e2**2)          # int_1^2 r^{-2al} eta^2 dr
    J2 = np.sum(w*r2**(-2*al+2)*d2**2)        # int_1^2 r^{-2al+2} eta'^2 dr
    J3 = np.sum(w*r2**(-2*al+1)*e2*d2)        # int_1^2 r^{-2al+1} eta eta' dr  (cross)
    N = om*(I1+J1)                            # int u^2/|x|^2
    D = om*(al*al*(I1+J1) + J2 - 2*al*J3)     # int |grad u|^2
    B1 = I1/(al*al*I1)
    print("  eps=%-8g alpha=%.4f | 1/alpha^2=B1only=%.4f | FULL ratio=%.5f  (N/om=%.4f D/om=%.4f)" % (eps,al,B1,N/D,N/om,D/om))
print()
print("  J1,J2,J3 at eps=0.01:", J1,J2,J3)
print("  -> so at eps=0.2 the report's '11.111' cannot be the full ratio (it equals exactly 1/alpha^2).")
