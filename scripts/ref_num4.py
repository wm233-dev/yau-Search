
import math, random
import numpy as np
xx,ww = np.polynomial.legendre.leggauss(4000)

print("### 题10: I_n = (1/n!) int_{-pi/2}^{pi/2} (pi^2/4 - t^2)^n cos t dt")
a = math.pi/2
def f_n(n):
    t = a*xx
    return a*np.sum(ww*((a*a-t*t)**n)*np.cos(t))
fs = [f_n(n) for n in range(0,8)]
print("  f_n numeric :", ["%.10f"%v for v in fs])
print("  I_n numeric :", ["%.10f"%(v/math.factorial(n)) for n,v in enumerate(fs)])
print("  I_n claimed : 2,4,4.260791,3.129494,1.760598,0.803887,0.309105")
# recurrence f_{m+1}=2(m+1)(2m+1) f_m - m(m+1) pi^2 f_{m-1}
print("  recurrence residuals (f):")
for m in range(1,7):
    lhs = fs[m+1]; rhs = 2*(m+1)*(2*m+1)*fs[m] - m*(m+1)*math.pi**2*fs[m-1]
    print("    m=%d  lhs=%.10f rhs=%.10f  diff=%.3e" % (m, lhs, rhs, lhs-rhs))
# I recurrence
I = [v/math.factorial(n) for n,v in enumerate(fs)]
print("  recurrence residuals (I):")
for m in range(1,7):
    lhs = I[m+1]; rhs = 2*(2*m+1)*I[m] - math.pi**2*I[m-1]
    print("    n=%d  lhs=%.10f rhs=%.10f diff=%.3e" % (m,lhs,rhs,lhs-rhs))
print("  I2=24-2pi^2 =", 24-2*math.pi**2, " I3=240-24pi^2 =", 240-24*math.pi**2, " I4=3360-360pi^2+2pi^4 =", 3360-360*math.pi**2+2*math.pi**4)
# irrationality gadget check
p,q = 355,36   # pi^2 ~ 9.8696
J = [q**n*I[n] for n in range(0,8)]
print("  with pi^2 ~ 355/36: J_n =", ["%.4f"%v for v in J])

print()
print("### 题3: Stieltjes counterexample moments int_0^inf x^n e^{-x^{1/4}} sin(x^{1/4}) dx")
for n in range(0,6):
    m = 4*n+3
    # 4 * Im[ m! / (1-i)^{m+1} ]
    z = complex(1,-1)**(m+1)
    val = (4*complex(math.factorial(m))/z).imag
    print("   n=%d  exact moment = %.3e" % (n, val))
# numeric Gauss-Laguerre-ish: substitute x=t^4 -> 4 int t^{4n+3} e^-t sin t dt
xg,wg = np.polynomial.laguerre.laggauss(300)
for n in range(0,4):
    v = 4*np.sum(wg*(xg**(4*n+3))*np.sin(xg))
    print("   n=%d  numeric laguerre = %.3e" % (n, v))

print()
print("### 题5: sum 1/p'(a_i) = 0 for random polynomials")
def check(coeffs_desc):
    # poly given as list of coefficients highest->lowest
    p = np.polynomial.Polynomial(coeffs_desc[::-1])
    rts = p.roots()
    dp = p.deriv()
    s = sum(1.0/dp(r) for r in rts)
    return len(rts), s
random.seed(7)
for trial in range(4):
    d = random.randint(2,6)
    c = [1.0]+[round(random.uniform(-3,3),2) for _ in range(d)]
    k,s = check(c)
    print("   deg=%d roots=%d  sum=%.3e" % (d,k,s))

print()
print("### 题6: radial laplacian identity  Delta f(r) = f'' + (n-1)/r f' and Delta(|x|^{2-n})=0")
def radial_laplacian_check(n, f, fp, fpp, r):
    return fpp(r)+(n-1)/r*fp(r)
for n in [2,3,5]:
    r0=1.7
    f = lambda r: r**(2-n); fp = lambda r:(2-n)*r**(1-n); fpp=lambda r:(2-n)*(1-n)*r**(-n)
    print("   n=%d  f''+(n-1)/r f' at r=%.2f = %.3e" % (n,r0,radial_laplacian_check(n,f,fp,fpp,r0)))
# numeric check of the divergence formula with finite differences
print()
print("### 题4: counterexample ODEs")
# ex1: x' = 2x -> x = x0 e^{2t}
print("   ex1: x(t)=e^{2t} at t=1:", math.exp(2))
# ex2: x' = x/(t+1) -> x = C(t+1)
print("   ex2: x(t)=t+1 at t=100:", 101)
# main theorem numerical: x' = -x + f, f= phi*x, phi = 1/(1+t)^2 (integrable)
# x' = (-1+phi)x  -> x = exp(-t + 1 - 1/(1+t)) (from t0=0, x0=1)
phi = lambda t: 1.0/(1+t)**2
x = lambda t: math.exp(-t + 1 - 1.0/(1+t))
print("   integrable phi: Phi=1, x(10)=%.6f  bound x0*e^Phi*e^-10=%.6f" % (x(10.0), math.exp(1)*math.exp(-10)))
