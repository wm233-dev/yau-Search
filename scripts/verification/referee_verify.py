
# -*- coding: utf-8 -*-
r"""
referee_verify.py  —  对 ./reports/solutions_analysis.md 中全部可数值检验的
结论做独立复算。运行方式（Windows / PowerShell，工作目录 .）：

    python .\scripts\referee_verify.py

只依赖 numpy（本机 numpy 2.5.2 已装）。不需要 sympy / fitz。
每个小节前的 [Rn] 与审稿报告 referee_analysis.md 中的编号对应。
"""
import math
import numpy as np

def hdr(s): print("\n" + "="*88 + "\n" + s)

# ---------------------------------------------------------------- [R1] 题1
hdr("[R1] 题1 2011#2  u''-u = 4e^-x , u(0)=u'(0)=0 ;  讲义答案 u = e^x-e^-x-2x e^-x")
u   = lambda x: math.exp(x) - math.exp(-x) - 2*x*math.exp(-x)
up  = lambda x: math.exp(x) - math.exp(-x) + 2*x*math.exp(-x)
upp = lambda x: math.exp(x) + 3*math.exp(-x) - 2*x*math.exp(-x)
xs = np.linspace(0.0, 1.0, 2001)
print("  max|u''-u-4e^-x| =", max(abs(upp(x)-u(x)-4*math.exp(-x)) for x in xs))
print("  u(0) =", u(0.0), "   u'(0) =", up(0.0))
print("  u(1) =", u(1.0), "  (讲义称 1.6146435049)")

# ---------------------------------------------------------------- [R2] 题2
hdr("[R2] 题2 2014Team#1  int_0^inf log x/(1+x^2) dx = 0")
x, w = np.polynomial.legendre.leggauss(4000)
s  = 30.0*(x+1.0)                                  # s in [0,60]; x = e^{-s} on (0,1]
I1 = float(np.sum(w*30.0*np.array([(-t)*math.exp(-t)/(1+math.exp(-2*t)) for t in s])))
I2 = float(np.sum(w*30.0*np.array([  t *math.exp( t)/(1+math.exp( 2*t)) for t in s])))
print("  int_0^1 = %.12f   int_1^inf = %.12f   sum = %.3e" % (I1, I2, I1+I2))
print("  int_{1e-6}^{60} =", float((60-1e-6)/2*np.sum(w*np.array(
      [math.log(v)/(1+v*v) for v in ((60-1e-6)/2*x+(60+1e-6)/2)]))), " (讲义 -0.0849)")
print("  tail int_60^inf ~ (1+log60)/60 =", (1+math.log(60))/60, " (讲义 0.0849)")
tt = 30.0*x                              # t in [-30,30];  x = e^t
print("  int_0^inf (log x)^2/(1+x^2) =", float(np.sum(w*30.0*np.array(
      [t*t*math.exp(t)/(1+math.exp(2*t)) for t in tt]))), "  pi^3/8 =", math.pi**3/8)

hdr("[R2b] 题2 法三 keyhole 支 arg in (0,2pi) 下的留数与围道积分")
def keyhole(k, R=60.0, eps=1e-4, N=60000):
    tot = 0j
    xs = np.linspace(eps, R, N)
    tot += np.trapezoid(np.array([(math.log(v))**k/(1+v*v) for v in xs]), xs)      # upper lip
    th = np.linspace(0, 2*math.pi, N); z = R*np.exp(1j*th)
    Lz = np.array([math.log(R)+1j*t for t in th])
    tot += np.trapezoid((Lz**k)/(1+z*z)*1j*z, th)                                   # big circle
    tot += -np.trapezoid(np.array([(math.log(v)+2j*math.pi)**k/(1+v*v) for v in xs]), xs)  # lower lip
    th2 = np.linspace(2*math.pi, 0, 5000); z2 = eps*np.exp(1j*th2)
    Lz2 = np.array([math.log(eps)+1j*t for t in th2])
    tot += np.trapezoid((Lz2**k)/(1+z2*z2)*1j*z2, th2)                              # small circle
    return tot
for k, ressum, label in [(1, -math.pi/2, "-pi/2"),
                         (2, (9-1)*math.pi**2/8/1j, "pi^2/i"),
                         (3, 26*math.pi**3/16, "13pi^3/8")]:
    c = keyhole(k)
    print("  k=%d  contour = %+.6f%+.6fj | 2*pi*i*sumRes = %+.6f%+.6fj  (sumRes=%s)"
          % (k, c.real, c.imag, (2j*math.pi*ressum).real, (2j*math.pi*ressum).imag, label))
print("  => k=2 时 oint = 2pi^3 = %.6f  != 0  —— 讲义法三称'围道积分为 0'是错的" % (2*math.pi**3))
print("     恒等式 oint = 4pi^2*J - 4pi*i*I, J=pi/2  =>  oint=2pi^3-4pi*i*I, 取 =2pi^3 得 I=0")

# ---------------------------------------------------------------- [R3] 题3
hdr("[R3] 题3 2015#2  Stieltjes 反例的矩：4*Im[ m!/(1-i)^{m+1} ], m=4n+3")
for n in range(0, 8):
    m = 4*n+3
    print("   n=%d   moment = %.3e" % (n, (4*complex(math.factorial(m))/(1-1j)**(m+1)).imag))

# ---------------------------------------------------------------- [R4] 题4
hdr("[R4] 题4 2010#6  反例核对")
print("   反例一 phi=3, f=3x -> x'=2x, x(1)=%.6f (不趋于0)" % math.exp(2))
print("   反例二 phi=1+1/(t+1), f=phi*x -> x'=x/(t+1), x(t)=t+1 -> x(100)=101")
phi = lambda t: 1.0/(1+t)**2
print("   可积情形 phi=1/(1+t)^2: x(10)=%.6e <= e^Phi e^-10 = %.6e"
      % (math.exp(-10+1-1.0/11), math.exp(1)*math.exp(-10)))

# ---------------------------------------------------------------- [R5] 题5
hdr("[R5] 题5 2013#2  sum 1/p'(a_i) = 0  随机多项式检验")
rng = np.random.default_rng(7)
for d in [2, 3, 4, 6, 8]:
    c = np.concatenate(([1.0], rng.uniform(-3, 3, d)))
    p = np.polynomial.Polynomial(c[::-1]); dp = p.deriv()
    rts = p.roots()
    val = np.sum([1.0/dp(r) for r in rts])
    print("   deg=%d  #roots=%d  sum=%.3e" % (d, len(rts), val.real))

# ---------------------------------------------------------------- [R6] 题6
hdr("[R6] 题6 2017Team#5  径向 Laplace 与基本解通量")
for n in [1, 2, 3, 5]:
    r0 = 1.7
    f   = lambda r: r**(2-n); fp = lambda r: (2-n)*r**(1-n); fpp = lambda r: (2-n)*(1-n)*r**(-n)
    print("   n=%d  f''+(n-1)/r f'  (f=r^{2-n}) at r=%.2f :  %.3e" % (n, r0, fpp(r0)+(n-1)/r0*fp(r0)))
print("   单位球面面积 omega_n = 2 pi^{n/2}/Gamma(n/2):  n=3 ->", 2*math.pi**1.5/math.gamma(1.5),
      " (4pi =", 4*math.pi, ")")

# ---------------------------------------------------------------- [R7] 题7
hdr("[R7] 题7 2020#5  T(x0) = 4 int_0^{x0} ds/sqrt(2(E0-V(s))),  V=s^2/2+s^4/4")
def T(x0, N=3000):
    E0 = 0.5*x0*x0 + 0.25*x0**4
    xx, ww = np.polynomial.legendre.leggauss(N)
    u = 0.5*(xx+1.0); s_ = x0*(1.0-u*u)
    return 0.5*float(np.sum(ww*4.0*(2*x0*u)/np.sqrt(2*(E0-(0.5*s_*s_+0.25*s_**4)))))
for x0 in [0.01, 0.1, 0.5, 1.0, 10.0, 100.0]:
    print("   x0=%-7g T=%.6f   x0*T=%.6f" % (x0, T(x0), x0*T(x0)))
print("   2pi =", 2*math.pi)
print("   大振幅常数 sqrt2*Gamma(1/4)*Gamma(1/2)/Gamma(3/4) =",
      math.sqrt(2)*3.6256099082219083*1.7724538509055159/1.2254167024651776)

# ---------------------------------------------------------------- [R8] 题8
hdr("[R8] 题8 2018#6  第1步公式自洽性（用 u=3+2|x|^{-1}, n=3, omega=4pi）")
n, om = 3, 4*math.pi
a, b = 3.0, 2.0
for r in [0.5, 1.0, 2.0]:
    A = om*r*r*(a+b/r)                 # int_{|x|=r} u
    F = om*r*r*(-b/r**2)               # int_{|x|=r} du/dnu
    ubar = A/(om*r*r)
    c1 = F/((2-n)*om); c2 = a
    print("   r=%.1f  ubar=%.6f   c1 r^{2-n}+c2=%.6f   F=%+.6f (与 r 无关)" % (r, ubar, c1*r**(2-n)+c2, F))

# ---------------------------------------------------------------- [R9] 题9
hdr("[R9] 题9 2025#2  最佳性函数族的真实比值 vs 讲义表格")
def g(t): return 0.0 if t <= 0 else math.exp(-1.0/t)
def fb(t):
    A, B = g(t), g(1-t)
    return A/(A+B) if (A+B) > 0 else (0.0 if t <= 0 else 1.0)
eta  = lambda r: 1.0 if r <= 1 else (0.0 if r >= 2 else fb(2-r))
etap = lambda r, h=1e-5: (eta(r+h)-eta(r-h))/(2*h)
xx, ww = np.polynomial.legendre.leggauss(6000)
r2 = 0.5*(xx+3); e2 = np.array([eta(v) for v in r2]); d2 = np.array([etap(v) for v in r2]); w = 0.5*ww
print("   讲义表格: 11.111 6.250 4.938 4.340 4.165  (= 1/alpha_eps^2, 即只在 B_1 上的比值)")
print("   eps      alpha   1/alpha^2(B1)   FULL ratio (整个 R^n)")
for eps in [0.2, 0.1, 0.05, 0.02, 0.01, 0.001, 1e-4]:
    al = 0.5-eps; I1 = 1.0/(2*eps)
    J1 = float(np.sum(w*r2**(-2*al)*e2**2)); J2 = float(np.sum(w*r2**(-2*al+2)*d2**2))
    J3 = float(np.sum(w*r2**(-2*al+1)*e2*d2))
    N  = om*(I1+J1); D = om*(al*al*(I1+J1)+J2-2*al*J3)
    print("   %-8g %.4f  %.4f          %.5f" % (eps, al, 1/al**2, N/D))

# ---------------------------------------------------------------- [R10] 题10
hdr("[R10] 题10 2026#1  I_n 与递推")
aa = math.pi/2
xx, ww = np.polynomial.legendre.leggauss(4000)
def fr(n):
    t = aa*xx
    return float(aa*np.sum(ww*((aa*aa-t*t)**n)*np.cos(t)))
fs = [fr(k) for k in range(0, 8)]
Is = [v/math.factorial(k) for k, v in enumerate(fs)]
print("   I_n 数值:", ["%.9f" % v for v in Is])
print("   讲义表格: 2  4  4.260791  3.129494  1.760598  0.803887  0.309105")
print("   递推残差 (f):", ["%.2e" % (fs[m+1]-2*(m+1)*(2*m+1)*fs[m]+m*(m+1)*math.pi**2*fs[m-1]) for m in range(1, 7)])
print("   递推残差 (I):", ["%.2e" % (Is[m+1]-2*(2*m+1)*Is[m]+math.pi**2*Is[m-1]) for m in range(1, 7)])
print("   I2=24-2pi^2=%.9f  I3=240-24pi^2=%.9f  I4=3360-360pi^2+2pi^4=%.9f"
      % (24-2*math.pi**2, 240-24*math.pi**2, 3360-360*math.pi**2+2*math.pi**4))
print("\nALL DONE")
