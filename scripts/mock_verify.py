# -*- coding: utf-8 -*-
import sys, math
from fractions import Fraction
sys.stdout.reconfigure(encoding="utf-8")

# ---------- 1. disc(x^3-3x+1) ----------
def disc_cubic_depressed(p,q): return -4*p**3-27*q**2
print("disc(x^3-3x+1) =", disc_cubic_depressed(-3,1))
# rational root test
for r in (1,-1):
    print("  f(%d) =" % r, r**3-3*r+1)
print("  sqrt(81) =", math.isqrt(81), "-> square:", math.isqrt(81)**2==81)
# numeric roots
import cmath
def roots_cubic(a,b,c):  # x^3+a x^2+b x+c
    # depressed
    p = b - a*a/3.0
    q = 2*a**3/27.0 - a*b/3.0 + c
    # Cardano
    D = (q/2)**2 + (p/3)**3
    out=[]
    for k in range(3):
        th = 2*math.pi*k/3
        r = (-q/2 + cmath.sqrt(D))**(1/3)
        out.append(r - p/(3*r) - a/3)
    return out
print("  roots:", [round(z.real,6) for z in roots_cubic(0,-3,1)])

# ---------- 2. 2022 #6: X^3+12X^2+8X+1 ----------
a,b,c = 12,8,1
p = b - a*a/3
q = 2*a**3/27 - a*b/3 + c
print("depressed p,q =", p, q)
D = disc_cubic_depressed(p,q)
print("disc =", D, "factor?", [d for d in range(2,200) if D%d==0])
print("1957 = 19*103 ->", 19*103)
print("rational root test f(1),f(-1) =", 1+a+b+c, -1+a-b+c)
# numeric roots: all real? disc>0 for cubic with negative p -> 3 real roots
print("roots:", sorted(round(z.real,6) for z in roots_cubic(a,b,c)))

# ---------- 3. ODE R(r)=2025 - r/4 + (r ln r)/2 + 1/(4r) ----------
def R(r): return 2025 - r/4 + (r*math.log(r))/2 + 1/(4*r)
def R1(r): return -1/4 + (math.log(r)+1)/2 - 1/(4*r*r)
def R2(r): return 1/(2*r) + 1/(2*r**3)
def R3(r): return -1/(2*r*r) - 3/(2*r**4)
for r in (1.0,2.0,3.7,10.0):
    lhs = r**3*R3(r) + 2*r*r*R2(r) - r*R1(r) + R(r)
    print("r=%5.1f  LHS=%.12f  (R,R',R'')=(%.6f,%.6f,%.6f)" % (r, lhs, R(r), R1(r), R2(r)))

# ---------- 4. 2020 #2 jump size check ----------
def h(x):
    G = (x/(2*math.pi))*math.exp(math.sin(x)) + x**2019*(x-2*math.pi) + 2019*math.sin(x)
    return math.atan(G)
print("h(1e-9) =", h(1e-9), " h(2pi-1e-9) =", h(2*math.pi-1e-9))
print("h(1.0)=",h(1.0)," h(0.99)=",h(0.99)," h(1.01)=",h(1.01))
print("jump h(2pi-)-h(0+) =", h(2*math.pi-1e-9)-h(1e-9), " -pi/2 =", -math.pi/2)
print("leading coeff of Fourier (1/(2pi))*(h2pi-h0)/(-i k) -> imag part:", (h(2*math.pi-1e-9)-h(1e-9))/(2*math.pi))
