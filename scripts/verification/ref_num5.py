
import math, cmath
import numpy as np

print("### contour check: oint (log z)^k/(1+z^2) dz over keyhole, branch arg in (0,2pi)")
def keyhole(k, R=50.0, eps=1e-4, N=20000):
    tot = 0j
    # upper lip: x from eps to R, arg -> 0+
    def lg(z):  # arg in (0,2pi)
        return cmath.log(abs(z)) + 1j*(cmath.phase(z) % (2*math.pi))
    # upper lip: z = x + i*y with y small positive ; use exact branch: log = ln x
    xs = np.linspace(eps, R, N)
    f = lambda x, L: (L**k)/(1+x*x)
    # upper: L = ln x
    vals = np.array([f(x, math.log(x)) for x in xs])
    tot += np.trapezoid(vals, xs)
    # big circle counterclockwise: z = R e^{i th}, th 0 -> 2pi
    th = np.linspace(0, 2*math.pi, N)
    z = R*np.exp(1j*th)
    Lz = np.array([math.log(R)+1j*t for t in th])
    vals = (Lz**k)/(1+z*z)*1j*z
    tot += np.trapezoid(vals, th)
    # lower lip: z = x e^{2pi i}, x from R down to eps ; L = ln x + 2pi i
    vals = np.array([f(x, math.log(x)+2j*math.pi) for x in xs])
    tot += -np.trapezoid(vals, xs)
    # small circle: z = eps e^{i th}, th 2pi -> 0
    th2 = np.linspace(2*math.pi, 0, 2000)
    z2 = eps*np.exp(1j*th2)
    Lz2 = np.array([math.log(eps)+1j*t for t in th2])
    vals = (Lz2**k)/(1+z2*z2)*1j*z2
    tot += np.trapezoid(vals, th2)
    return tot

for k in [1,2,3]:
    c = keyhole(k)
    res = {1: 1j*math.pi/2 - 3j*math.pi/2, 2: math.pi**2/(1j), 3: 26*math.pi**3/16}[k]
    print("  k=%d  contour=%.6f%+.6fj   2*pi*i*sumRes=%.6f%+.6fj" % (k, c.real, c.imag, (2j*math.pi*res).real, (2j*math.pi*res).imag))
# k=1: residues: log i/(2i) + log(-i)/(-2i) = (i pi/2)/(2i) + (3i pi/2)/(-2i) = pi/4 - 3pi/4 = -pi/2
print("  note k=1: sumRes = -pi/2 ; 2pi i*(-pi/2) = -pi^2 i")
c1 = keyhole(1)
print("  k=1 contour:", c1, "  -pi^2 i =", -math.pi**2*1j)

print()
print("### 题3 numeric moments (sub x=t^4): 4 int_0^inf t^{4n+3} e^-t sin t dt")
xg,wg = np.polynomial.laguerre.laggauss(120)
for n in range(0,5):
    v = 4*np.sum(wg*(xg**(4*n+3))*np.sin(xg))
    print("   n=%d numeric = %.3e" % (n,v))
# also do it by exact formula Im[m!/(1-i)^{m+1}] *4
for n in range(0,5):
    m=4*n+3
    val = (4*complex(math.factorial(m))/(1-1j)**(m+1)).imag
    print("   n=%d exact   = %.3e" % (n,val))
