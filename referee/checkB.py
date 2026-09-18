# -*- coding: utf-8 -*-
"""Referee verification, part B: problems 3,6,7,9,10.
Run: python.exe .tmp/burn2026/referee/checkB.py
"""
from math import gcd, isqrt, sqrt
from itertools import product

def hdr(t): print("\n"+"="*72+"\n"+t+"\n"+"="*72)

def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, isqrt(n)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=False
    return [i for i,v in enumerate(s) if v]

# ------------------------------------------------------------------ 题 3
hdr("题 3 (2018 ind #3): 99 阶群交换")
print("  n_11 | 9 且 n_11 === 1 mod 11  ->", [d for d in (1,3,9) if d % 11 == 1])
print("  |Aut(Z/11)| = 10, gcd(9,10) =", gcd(9,10))
print("  99 阶交换群: Z/99 与 Z/33 x Z/3 (有限交换群基本定理)")

# ------------------------------------------------------------------ 题 6
hdr("题 6 (2017 ind #2): 有限 Abel 群 Fitting 分解 A = A_0 (+) A_nil")
def group_elements(mods):
    return list(product(*[range(m) for m in mods]))
def gadd(a, b, mods):
    return tuple((a[i]+b[i]) % mods[i] for i in range(len(mods)))
def order_of(a, mods):
    if not any(a): return 1
    o = 1; v = a
    while any(v): v = gadd(v, a, mods); o += 1
    return o
def endomorphisms(mods):
    opts = [[v for v in group_elements(mods) if mods[i] % order_of(v, mods) == 0] for i in range(len(mods))]
    for images in product(*opts):
        def phi(x, images=images):
            r = tuple(0 for _ in mods)
            for i, xi in enumerate(x):
                r = gadd(r, tuple(xi*images[i][j] % mods[j] for j in range(len(mods))), mods)
            return r
        yield phi
def all_subgroups(elems, mods):
    zero = (0,)*len(mods); seen = {}
    for r in range(0, 4):
        for combo in product(elems, repeat=r):
            S = {zero} | set(combo)
            while True:
                new = {gadd(a, b, mods) for a in S for b in S}
                if new <= S: break
                S |= new
            seen[frozenset(S)] = S
    return list(seen.values())
groups = [[4],[2,2],[8],[2,4],[2,2,2],[9],[3,3],[6],[12],[15],[10],[16],[2,8],[3,6],[5,5],[2,2,4]]
bad = []
for mods in groups:
    elems = group_elements(mods); zero = (0,)*len(mods)
    subs = all_subgroups(elems, mods) if len(elems) <= 16 else None
    nend = 0; fail = None
    for phi in endomorphisms(mods):
        nend += 1
        def it(k, x):
            for _ in range(k): x = phi(x)
            return x
        A_nil = {x for x in elems if any(it(k, x) == zero for k in range(1, 40))}
        K = 1
        while True:
            imgK = {it(K, x) for x in elems}; imgK1 = {it(K+1, x) for x in elems}
            if len(imgK) == len(imgK1) and A_nil <= {x for x in elems if it(K, x) == zero}: break
            K += 1
            if K > 60: break
        A0 = imgK
        ok1 = (A0 & A_nil) == {zero}
        sumset = {gadd(a, b, mods) for a in A0 for b in A_nil}   # 子群和 A0 + A_nil
        ok2 = len(A0)*len(A_nil) == len(elems) and sumset == set(elems)
        ok3 = {phi(x) for x in A0} == A0
        if not (ok1 and ok2 and ok3):
            fail = ("decomp", ok1, ok2, ok3); break
        if subs is not None:
            cand = [B for B in subs if len(B) == len(A0) and (B & A_nil) == {zero} and {phi(x) for x in B} == B]
            if len(cand) != 1 or cand[0] != A0:
                fail = ("unique", len(cand)); break
    print(f"  A={str(mods):10s} 内同态数={nend:4d}  Fitting 分解+唯一性: {'OK' if fail is None else 'FAIL '+str(fail)}")
    if fail: bad.append((mods, fail))
print("  ==> 题6 穷举:", "PASS (无失败)" if not bad else f"FAIL {bad}")

# ------------------------------------------------------------------ 题 7
hdr("题 7 (2019 ind #5): Fibonacci mod p 与范数映射")
def fib_mod(n, m):
    a, b = 0, 1
    for _ in range(n): a, b = b, (a+b) % m
    return a
bad7 = []
for p in primes_upto(3000):
    if p == 5: continue
    if p % 5 in (1, 4):
        if fib_mod(p-1, p) % p != 0: bad7.append((p, "p-1"))
    else:
        if fib_mod(p+1, p) % p != 0: bad7.append((p, "p+1"))
print("  p<=3000 全部素数: p|F_{p-1} (p=±1 mod 5) 与 p|F_{p+1} (p=±2 mod 5) 反例 =", bad7 if bad7 else "无")
for p, n in [(11,10),(19,18),(29,28),(31,30),(2,3),(3,4),(7,8),(13,14),(17,18),(23,24)]:
    F = fib_mod(n, 10**18)
    print(f"    讲义数值: F_{n} = {F} = {F//p}*{p}  被 {p} 整除 = {F % p == 0}")
def field_p2(p):
    if p == 2:
        els = [(a,b) for a in range(2) for b in range(2)]
        def mul(x,y): return ((x[0]*y[0]+x[1]*y[1]) % 2, (x[0]*y[1]+x[1]*y[0]+x[1]*y[1]) % 2)  # t^2=t+1
        return els, mul
    d0 = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)
    els = [(a,b) for a in range(p) for b in range(p)]
    def mul(x,y): return ((x[0]*y[0]+x[1]*y[1]*d0) % p, (x[0]*y[1]+x[1]*y[0]) % p)
    return els, mul
def pw(mul, x, e):
    r = (1,0)
    while e:
        if e & 1: r = mul(r, x)
        x = mul(x, x); e >>= 1
    return r
badN7 = []
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
    els, mul = field_p2(p)
    nz = [x for x in els if x != (0,0)]
    ker = [x for x in nz if pw(mul, x, p+1) == (1,0)]
    im = {pw(mul, x, p+1) for x in nz}
    if not (len(ker) == p+1 and len(im) == p-1): badN7.append((p, len(ker), len(im)))
    print(f"    p={p}: |ker N| = {len(ker)} (应 p+1={p+1}), |Im N| = {len(im)} (应 p-1={p-1})")
print("  反例:", badN7 if badN7 else "无")

# ------------------------------------------------------------------ 题 9
hdr("题 9 (2014 ind #3): X^2-82Y^2 = +-2")
LIM = 2_000_000
found = []
for y in range(0, LIM+1):
    for s in (2, -2):
        t = 82*y*y + s
        if t >= 0:
            r = isqrt(t)
            if r*r == t: found.append((y, s, r))
print(f"  0 <= y <= {LIM} 的整数解:", found if found else "无 (符合 (c))")
print("  模 p^n 可解性 (枚举 y, 判断 82y^2+-2 是否平方剩余):")
for p in [2,3,5,7,11,13,41,43,83]:
    row = []; m = 1
    while m <= 400000:
        m *= p
        sq = {(x*x) % m for x in range(m)}
        s2 = any((82*y*y + 2) % m in sq for y in range(m))
        sm2 = any((82*y*y - 2) % m in sq for y in range(m))
        row.append(f"{p}^{len(row)+1}={m}: +2:{s2} -2:{sm2}")
        if m > 400000 // p: break
    print(f"    p={p}: " + " | ".join(row))
badN = []
for p in primes_upto(200):
    if p == 2 or p == 41: continue   # p=41: 82=0 mod 41, 讲义单独处理 (情形1)
    qr = pow(82 % p, (p-1)//2, p) == 1
    for a in (2, p-2):
        N = sum(1 for x in range(p) for y in range(p) if (x*x - 82*y*y - a) % p == 0)
        if N != (p-1 if qr else p+1): badN.append((p, a, N))
print("  模 p 解数 N_a = p-1 (82 为平方) / p+1 (否则) 的反例:", badN if badN else "无")
okT = all(((9*x-82*y)**2 - 82*(x-9*y)**2) == -(x*x - 82*y*y) for x in range(-60,61) for y in range(-60,61))
okT2 = all(((9*x+82*y)**2 - 82*(x+9*y)**2) == -(x*x - 82*y*y) for x in range(-60,61) for y in range(-60,61))
print("  (9x-82y)^2-82(x-9y)^2 == -(x^2-82y^2):", okT, " | (9x+82y)^2-82(x+9y)^2 == -(x^2-82y^2):", okT2)
print("  T^2 = -id:", all((9*(9*x-82*y)-82*(x-9*y), (9*x-82*y)-9*(x-9*y)) == (-x,-y) for x in range(-50,51) for y in range(-50,51)))

# ------------------------------------------------------------------ 题 10
hdr("题 10 (2026 ind #2): y^2 = x^3+1 上的点数与 Jacobi 和")
def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
def Np(p):
    return sum(1 for x in range(p) for y in range(p) if (y*y - x*x*x - 1) % p == 0)
bad10 = []
for p in primes_upto(2000):
    n = Np(p)
    if abs(n - p) > 2*sqrt(p): bad10.append(("bound", p, n))
    if (p == 3 or p % 3 == 2) and n != p: bad10.append(("Np=p", p, n))
print("  p<=2000: |N_p-p| <= 2 sqrt(p) 与 (p=3 或 p=2 mod 3 => N_p=p) 反例:", bad10 if bad10 else "无")
def zmul(x,y):
    a,b = x; c,d = y
    return (a*c - b*d, a*d + b*c - b*d)
def zadd(x,y): return (x[0]+y[0], x[1]+y[1])
def znorm(x): return x[0]*x[0] - x[0]*x[1] + x[1]*x[1]
def primroot(p):
    fs = set(); m = p-1; d = 2
    while d*d <= m:
        if m % d == 0:
            fs.add(d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: fs.add(m)
    for g in range(2, p):
        if all(pow(g, (p-1)//f, p) != 1 for f in fs): return g
badJ = []; checked = 0
for p in primes_upto(1000):
    if p % 3 != 1: continue
    g = primroot(p); log = {}; v = 1
    for k in range(p-1): log[v] = k; v = v*g % p
    def psim(a, m=1):
        if a % p == 0: return (0,0)
        return [(1,0),(0,1),(-1,-1)][(m*log[a % p]) % 3]
    T = sum(legendre(x*x*x + 1, p) for x in range(p))
    J1 = (0,0); J2 = (0,0)
    for a in range(p):
        b = (1 - a) % p
        J1 = zadd(J1, zmul(psim(a,1), (legendre(b,p), 0)))
        J2 = zadd(J2, zmul(psim(a,2), (legendre(b,p), 0)))
    rhs = zadd(zmul(psim(p-1,1), J1), J2)
    ok = (rhs == (T,0)) and znorm(J1) == p and znorm(J2) == p and T == Np(p) - p
    checked += 1
    if not ok: badJ.append((p, T, rhs, znorm(J1), znorm(J2)))
    if p <= 31:
        print(f"    p={p}: T={T}, N_p={p+T}, J(psi,chi2)={J1}, J(psi^2,chi2)={J2}, |J|^2={znorm(J1)},{znorm(J2)}, psi(-1)={psim(p-1,1)}, 公式= {rhs}")
print(f"  核验了 {checked} 个 p=1 mod 3 素数 (T 的 Jacobi 表示 + |J|^2=p + T=N_p-p), 反例:", badJ if badJ else "无")
p = 7; g = primroot(p); log = {}; v = 1
for k in range(p-1): log[v] = k; v = v*g % p
def psi7(a): return (0,0) if a % p == 0 else [(1,0),(0,1),(-1,-1)][log[a % p] % 3]
J1 = (0,0)
for a in range(p):
    J1 = zadd(J1, zmul(psi7(a), (legendre((1-a) % p, p), 0)))
print("  讲义 p=7 数值复现: 生成元 g =", g, " psi(3) =", psi7(3), "(应为 omega=(0,1))  J(psi,chi2) =", J1, " (讲义: 3+2*zeta_3 = (3,2))")
