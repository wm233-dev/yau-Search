# -*- coding: utf-8 -*-
import sys, math, cmath
sys.stdout.reconfigure(encoding="utf-8")

# ---- 2020#2: evaluate h via logs to locate the jump ----
def Gsign_log(x):
    # G = (x/2pi) e^{sin x} + x^2019 (x-2pi) + 2019 sin x
    if x <= 0 or x >= 2*math.pi: return None
    t1 = (x/(2*math.pi))*math.exp(math.sin(x))
    t2sign = -1.0  # x^2019>0, (x-2pi)<0
    t2log = 2019*math.log(x) + math.log(2*math.pi - x)
    t3 = 2019*math.sin(x)
    # magnitude of G: dominated by t2 unless t2log very negative
    return (t1, t2sign, t2log, t3)

for x in [1e-9, 0.5, 0.99, 0.9999, 1.0, 1.0001, 1.01, 3.0, 2*math.pi-1e-9]:
    t1, s2, l2, t3 = Gsign_log(x)
    # decide arctan limit
    dom = "t2" if l2 > max(math.log(max(t1,1e-300)), math.log(max(abs(t3),1e-300))) + 5 else "small"
    print("x=%.9f  t1=%.6g  log|t2|=%.3f (sign %+d)  t3=%.3f  arctan-> %s" % (
        x, t1, l2, s2, t3, ("-pi/2 (t2 huge negative)" if dom=="t2" else "finite/small")))

# ---- 2023#4 sanity: <x_n, e^{ikt}> for sawtooth x(t)=t on [0,2pi) ----
def inner(n, k, N=400000):
    # integral_0^{2pi} x(nt) e^{-i k t} dt  with x(u) = u mod 2pi
    s = 0j
    dt = 2*math.pi/N
    for j in range(N):
        t = (j+0.5)*dt
        u = (n*t) % (2*math.pi)
        s += u*cmath.exp(-1j*k*t)*dt
    return s
for n in (5,):
    for k in (0,1,5,10):
        val = inner(n,k)
        theory = 0j
        if k % n == 0:
            # integral_0^{2pi} x(v) e^{-i k v/n} dv
            N=200000; dv=2*math.pi/N; theory=0j
            for j in range(N):
                v=(j+0.5)*dv
                theory += v*cmath.exp(-1j*k*v/n)*dv
        print("n=%d k=%2d  numeric=%.4f%+.4fi   theory(n|k)=%.4f%+.4fi" % (n,k,val.real,val.imag,theory.real,theory.imag))
