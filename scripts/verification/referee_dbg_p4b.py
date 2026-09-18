# -*- coding: utf-8 -*-
"""Diagnose the polar-grid Dijkstra for problem 4.
   In (theta,u), u=-ln rho, the metric is the hyperbolic metric (du^2+dtheta^2)/u^2.
   Test: (a) radial pair, (b) same-radius arc pair, (c) the true geodesic sampled on the grid."""
import numpy as np, math

# grid in (u,theta) directly
def build(nu, nth, u_lo, u_hi):
    u = np.linspace(u_lo, u_hi, nu)
    dth = 2*math.pi/nth
    sr = np.abs(np.diff(u)) / (0.5*(u[:-1]+u[1:]))     # radial edge length (u-direction)
    st = dth/u                                       # angular edge length
    return u, sr, st, dth

# exact hyperbolic distance between (theta1,u1),(theta2,u2)
def hdist(t1,u1,t2,u2):
    return math.acosh(1 + ((t2-t1)**2 + (u2-u1)**2)/(2*u1*u2))

nu, nth = 1600, 2880
u_lo, u_hi = math.log(1/0.9), math.log(1e12)
u, sr, st, dth = build(nu, nth, u_lo, u_hi)
print("u range", u_lo, u_hi, " du =", u[1]-u[0], " dtheta =", dth)
A = (0.0, 2*math.pi); B = (math.pi, math.pi)
print("exact hdist(A,B)          = %.6f" % hdist(*A, *B))
print("exact hdist radial pair   = %.6f" % hdist(0.0, 2*math.pi, 0.0, math.pi))
print("exact hdist same-radius   = %.6f" % hdist(0.0, 2*math.pi, math.pi, 2*math.pi))
# length of the true geodesic sampled through the grid: semicircle centre c=-pi, R=pi*sqrt5
c = -math.pi; R = math.pi*math.sqrt(5)
ts = np.linspace(0.0, math.pi, 200001)
pts = []
for t in ts:
    theta = t
    # point on circle: theta = c + R cos phi  ->  phi determined by theta; u = R sin phi
    cosphi = (theta - c)/R
    sinphi = math.sqrt(max(0.0, 1-cosphi*cosphi))
    pts.append((theta, R*sinphi))
L = 0.0
for k in range(len(pts)-1):
    (t1,u1),(t2,u2) = pts[k], pts[k+1]
    L += math.hypot(t2-t1, u2-u1)/(0.5*(u1+u2))
print("length of true geodesic (fine sampling) = %.6f" % L)
print("check endpoints: first", pts[0], " last", pts[-1])
