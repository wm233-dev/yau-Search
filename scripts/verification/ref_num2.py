
import math
import numpy as np
x,w = np.polynomial.legendre.leggauss(4000)

print("### 题1 re-check derivative")
up = lambda x: math.exp(x)-math.exp(-x)+2*x*math.exp(-x)
print("u'(0) =", up(0.0), " u'(1)=",up(1.0))

print("="*80)
print("### 题7: T(x0) for x''+x+x^3=0")
def T(x0, N=3000):
    # T = 4 int_0^{x0} ds / sqrt(2(E0 - V(s))), V= s^2/2+s^4/4, E0 = V(x0)
    # substitute s = x0(1-u^2), u in [0,1]
    E0 = 0.5*x0*x0 + 0.25*x0**4
    xx,ww = np.polynomial.legendre.leggauss(N)
    u = 0.5*(xx+1.0)             # u in [0,1]
    s = x0*(1.0-u*u)
    dsdu = 2*x0*u
    F = 2*(E0 - (0.5*s*s+0.25*s**4))
    integ = 4.0*dsdu/np.sqrt(F)
    return 0.5*np.sum(ww*integ)
for x0 in [0.01,0.1,0.5,1.0,10.0,100.0]:
    t = T(x0)
    print("  x0=%-7g T=%.6f   x0*T=%.6f" % (x0,t,x0*t))
print("  2*pi =", 2*math.pi)
print("  asymptotic const sqrt2*Gamma(1/4)*Gamma(1/2)/Gamma(3/4) =", math.sqrt(2)*3.6256099082219083*1.7724538509055159/1.2254167024651776)
print("  4*sqrt2*int_0^1 du/sqrt(1-u^4) (numeric):")
xx,ww = np.polynomial.legendre.leggauss(4000)
u = 0.5*(xx+1); s=1-u*u
print("     int_0^1 du/sqrt(1-u^4) =", 0.5*np.sum(ww/np.sqrt(s*(1+u*u))))
print("     4*sqrt2*that =", 4*math.sqrt(2)*0.5*np.sum(ww/np.sqrt(s*(1+u*u))))
print("  2nd-order small-amplitude: T ~ 2pi(1-3A^2/8): A=0.01 ->", 2*math.pi*(1-3*0.01**2/8), " A=0.1 ->", 2*math.pi*(1-3*0.1**2/8))

print("="*80)
print("### 题9: Hardy ratio for u_eps = |x|^{-alpha} eta, n=3")
# smooth flat bump eta: eta(r)=1 for r<=1, 0 for r>=2, C^inf
def make_eta():
    def g(t):
        return 0.0 if t<=0 else math.exp(-1.0/t)
    def f(t):  # 0 for t<=0, 1 for t>=1, smooth
        a=g(t); b=g(1-t)
        return a/(a+b) if (a+b)>0 else (0.0 if t<=0 else 1.0)
    return f
f = make_eta()
eta = lambda r: 1.0 if r<=1 else (0.0 if r>=2 else f(2-r))
# numerical derivative
def etap(r,h=1e-6):
    return (eta(r+h)-eta(r-h))/(2*h)
n=3
for eps in [0.2,0.1,0.05,0.02,0.01,0.001,1e-4]:
    al = (n-2)/2 - eps
    # N/omega_n = int_0^inf r^{-2al} eta^2 dr
    # D/omega_n = al^2 int r^{-2al} eta^2 dr + int r^{-2al+2} etap^2 dr
    # integrand on [0,1]: r^{-2al} ; on [1,2]: r^{-2al} eta^2 etc.
    xx,ww = np.polynomial.legendre.leggauss(4000)
    # [0,1] mapped
    r1 = 0.5*(xx+1)
    I1 = 0.5*np.sum(ww*r1**(-2*al))
    I2 = 0.5*np.sum(ww*r1**(-2*al+2)*(2*1.0)**2*0)  # placeholder none
    # [1,2]
    r2 = 0.5*(xx+3)
    e2 = np.array([eta(v)**2 for v in r2])
    d2 = np.array([etap(v)**2 for v in r2])
    J1 = 0.5*np.sum(ww*(r2**(-2*al))*e2)
    J2 = 0.5*np.sum(ww*(r2**(-2*al+2))*d2)
    Nk = I1+J1
    Dk = al*al*(I1+J1) + J2
    print("  eps=%-8g alpha=%.4f  1/alpha^2=%.4f | B1-only ratio=%.4f | FULL ratio=%.5f" % (eps,al,1/al**2,1/al**2, Nk/Dk))
print("  check: int_0^1 r^{-2al} dr = 1/(1-2al) ; omega_3/(2eps)=?")
for eps in [0.2,0.01]:
    al=(n-2)/2-eps
    print("     eps=",eps," 1/(1-2al)=",1/(1-2*al)," 1/(2eps)=",1/(2*eps))
