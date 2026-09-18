
# -*- coding: utf-8 -*-
"""mock_exam_C.md 的数值/代数交叉校验脚本（可复跑）
运行: C:\Python314\python.exe .tmp/burn2026/work/_mockC_check.py
校验四件事:
  1. Klein 圆盘度规的 Christoffel、Riemann 分量与标量曲率 (模拟卷第 6 题 / 物理卷第 6 题)
  2. 2024 计算 #6 的 von Neumann 稳定性约束 (FE 与 CN)
  3. V=alpha r^k 中心势的径向/角向频率比 sqrt(k+2) (物理卷第 4 题)
  4. sqrt(k+2) 的有理性与闭合轨道的关系(数值验证 k=1,2)
"""
import numpy as np
np.set_printoptions(precision=6, suppress=True)

print("=== 1. Klein disk ===")
def g(r):
    return np.array([[1.0/(1-r*r)**2, 0.0], [0.0, r*r/(1-r*r)]])
def christ(r):
    G = np.zeros((2,2,2))
    G[0,0,0] = 2*r/(1-r*r)                 # Gam^r_{rr}
    G[0,1,1] = -r                          # Gam^r_{th th}
    G[1,0,1] = G[1,1,0] = 1.0/(r*(1-r*r))  # Gam^th_{r th}
    return G
h = 1e-6
# 由度规数值求 Christoffel 并与解析式比对
for r in [0.2, 0.5, 0.8]:
    d = np.zeros((2,2,2)); gi = np.linalg.inv(g(r))
    for k in range(2):
        e = np.zeros(2); e[k] = h
        d[k] = (g(r+e[0]) - g(r-e[0]))/(2*h)
    Gn = np.zeros((2,2,2))
    for a in range(2):
        for i in range(2):
            for j in range(2):
                Gn[a,i,j] = 0.5*sum(gi[a,s]*(d[i,j,s]+d[j,i,s]-d[s,i,j]) for s in range(2))
    print("  r=%.1f  Christoffel 解析/数值最大偏差 = %.2e" % (r, np.abs(Gn-christ(r)).max()))
# Riemann: R^r_{th r th}
def Rhat(r):
    G = christ(r)
    dG = np.zeros((2,2,2,2))
    for k in range(2):
        for a in range(2):
            for i in range(2):
                for j in range(2):
                    e = np.zeros(2); e[k] = h
                    dG[k,a,i,j] = (christ(r+e[0])[a,i,j] - christ(r-e[0])[a,i,j])/(2*h)
    v = dG[0,0,1,1] - dG[1,0,0,1]
    for l in range(2):
        v += G[0,0,l]*G[l,1,1] - G[0,1,l]*G[l,0,1]
    return v
for r in [0.2, 0.5, 0.8]:
    Rr = Rhat(r)
    print("  r=%.1f  R^r_thrth = %+.6f  (解析 -r^2/(1-r^2) = %+.6f)" % (r, Rr, -r*r/(1-r*r)))
    print("        R_rthrth  = %+.6f  (解析 -r^2/(1-r^2)^3 = %+.6f)" % (Rr/(1-r*r)**2, -r*r/(1-r*r)**3))
    # 标量曲率 = 2 * g^{rr} g^{thth} R_rthrth
    Rsc = 2*(1-r*r)**2 * ((1-r*r)/r**2) * (Rr/(1-r*r)**2)
    print("        R = %+.6f   (双曲平面 K=-1 => R=-2)" % Rsc)
# 用 rho = artanh r 变换验证: ds^2 = drho^2 + sinh^2 rho dth^2 => K = -1
for r in [0.2,0.5,0.8]:
    print("  r=%.1f  rho=artanh r=%.6f  sinh(rho)=%.6f  r/sqrt(1-r^2)=%.6f"
          % (r, np.arctanh(r), np.sinh(np.arctanh(r)), r/np.sqrt(1-r*r)))

print("=== 2. 2024 computational #6 von Neumann ===")
N = 64; hh = 2*np.pi/N; mu = 1.0
lam = np.array([(2*np.cos(2*np.pi*l/N)-2)/hh**2 for l in range(N)])
for k in [0.5*hh**2/(2*mu), hh**2/(2*mu), 1.01*hh**2/(2*mu)]:
    print("  FE: k/h^2=%.4f  max|1+mu*k*lam| = %.6f" % (k/hh**2, np.abs(1+mu*k*lam).max()))
for k in [hh**2/(2*mu), 1.0, 1e6]:
    gain = np.abs((1+mu*k*lam)/(1-mu*k*lam))
    print("  CN: k=%.6g  max|gain| = %.6f" % (k, gain.max()))
k = hh**2/(2*mu)
print("  phi=(-1)^m 时 FE 增益 = %.6f ; CN 增益 = %.6f"
      % (1-4*mu*k/hh**2, (1-4*mu*k/hh**2)/(1+4*mu*k/hh**2)))

print("=== 3. V=alpha r^k : omega_r/Omega = sqrt(k+2) ===")
from math import sqrt, pi
def radial_period(k, alpha=1.0, r0=1.0, eps=1e-4, T=60.0, n=2000000):
    l2 = alpha*k*r0**(k+2)          # l^2 = m alpha k r0^{k+2}, m=1
    def acc(r): return l2/r**3 - alpha*k*r**(k-1)
    dt = T/n; r = r0+eps; v = 0.0; prev = r-r0; cross = []
    for i in range(n):
        v += acc(r)*dt; r += v*dt
        cur = r-r0
        if prev < 0 <= cur: cross.append(i*dt)
        prev = cur
    return cross
for k in [1.0, 2.0, -0.5, 3.0]:
    c = radial_period(k)
    if len(c) > 2:
        Tr = float(np.mean(np.diff(c)))
        Om = sqrt(k)/1.0   # Omega = l/r0^2 = sqrt(alpha k) r0^{k/2-1} = sqrt(k)
        print("  k=%5.2f  T_r=%.5f  Omega=%.5f  omega_r/Omega=%.6f  sqrt(k+2)=%.6f"
              % (k, Tr, Om, 2*pi/Tr/Om, sqrt(k+2)))
print("=== done ===")
