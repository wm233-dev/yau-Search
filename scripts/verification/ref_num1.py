
import math
import numpy as np

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

print("="*80)
print("### 题1: u''-u = 4e^{-x}, u(0)=u'(0)=0;  claimed u = e^x - e^-x - 2x e^-x")
u = lambda x: math.exp(x)-math.exp(-x)-2*x*math.exp(-x)
up = lambda x: math.exp(x)+math.exp(-x)+2*x*math.exp(-x)
upp = lambda x: math.exp(x)+3*math.exp(-x)-2*x*math.exp(-x)
xs = np.linspace(0,1,2001)
res = max(abs(upp(x)-u(x)-4*math.exp(-x)) for x in xs)
print("max |u''-u-4e^-x| =", res, " u(0)=",u(0.0)," u'(0)=",up(0.0))
print("u(1) =", u(1.0), " 2sinh(1)-2/e =", 2*math.sinh(1)-2/math.e)

print("="*80)
print("### 题2: int_0^inf log x/(1+x^2) dx")
# split at 1, substitute x=e^t on (0,1] -> t in (-inf,0]; x = e^t; and x = e^t on [1,inf)
# I = int_{-inf}^{0} t e^t/(1+e^{2t}) dt + int_0^{inf} t e^t/(1+e^{2t}) dt  = int_{-inf}^{inf} t e^t/(1+e^{2t})dt
# integrand is odd in t -> 0 exactly. numeric:
f = lambda t: t*math.exp(t)/(1+math.exp(2*t)) if abs(t) < 700 else 0.0
# integrate over [-60,60] with substitution t = 60*tanh? use Gauss-Legendre on [-60,60]
x,w = np.polynomial.legendre.leggauss(4000)
T = 60*x
val = 60*np.sum(w*np.array([t*math.exp(t)/(1+math.exp(2*t)) for t in T]))
print("int via t-substitution over [-60,60]:", val)
# direct split
x,w = np.polynomial.legendre.leggauss(2000)
# (0,1]: x = (1+u)/2 *? use x = exp(-s), s in [0,60]
s = 30*(x+1); # s in [0,60]
I1 = np.sum(w*30*np.array([(-ss)*math.exp(-ss)/(1+math.exp(-2*ss)) for ss in s]))
s2 = 30*(x+1)
I2 = np.sum(w*30*np.array([ss*math.exp(-ss)/(1+math.exp(-2*ss)) for ss in s2])) * 0  # placeholder
# (1,inf): x=e^s, s in [0,60]
I2 = np.sum(w*30*np.array([ss*math.exp(ss)/(1+math.exp(2*ss)) for ss in s2]))
print("partial (0,1]:",I1," [1,inf):",I2," sum:",I1+I2)
print("tail estimate int_60^inf (1+log60)/60 =", (1+math.log(60))/60)
print("int_{1e-6}^{60} log x/(1+x^2) dx :")
lo, hi = 1e-6, 60.0
s = (hi-lo)/2*x + (hi+lo)/2
val2 = (hi-lo)/2*np.sum(w*np.array([math.log(v)/(1+v*v) for v in s]))
print("   =", val2)

print("="*80)
print("### 题2 附: F(a)=pi/(2 sin(pi a/2)) 数值核对")
for a in [0.3,1.0,1.7]:
    # int_0^inf x^{a-1}/(1+x^2) dx ; x = exp(t), t in R : int exp(a t)/(1+exp(2t)) dt
    tt = 30*(x+1)-30
    Ig = np.sum(w*30*np.array([math.exp(a*t)/(1+math.exp(2*t)) for t in (30*(x+1)-30)]))
    print("  a=",a," numeric:",Ig," formula:",math.pi/(2*math.sin(math.pi*a/2)))
print("int_0^inf (log x)^2/(1+x^2) dx :")
tt = 30*(x+1)-30
Ig2 = np.sum(w*30*np.array([(t*t)*math.exp(t)/(1+math.exp(2*t)) for t in tt]))
print("   =", Ig2, " pi^3/8 =", math.pi**3/8)
