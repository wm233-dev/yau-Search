# -*- coding: utf-8 -*-
"""Referee verification, part A: problems 1,2,4,5,6 of solutions_algebra.md.
All arithmetic exact (Fraction / integer).  Run:
  python.exe .tmp/burn2026/referee/checkA.py
"""
from fractions import Fraction as F
from itertools import product
import random

def hdr(t): print("\n" + "="*72 + "\n" + t + "\n" + "="*72)

# ---------------------------------------------------------------- 题 1
def solve_exact(M, b):
    n = len(M); m = len(M[0])
    A = [list(M[i]) + [b[i]] for i in range(n)]
    piv = []; r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]; A[r] = [v/pv for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [A[i][j]-f*A[r][j] for j in range(m+1)]
        piv.append(c); r += 1
        if r == n: break
    for i in range(r, n):
        if all(A[i][j] == 0 for j in range(m)) and A[i][m] != 0: return None
    x = [F(0)]*m
    for i, c in enumerate(piv): x[c] = A[i][m]
    return x

def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def matpow(X, k):
    n = len(X); R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k): R = matmul(R, X)
    return R

hdr("题 1 (2010 ind #1): AB-BA=B  随机验证")
random.seed(20260101)
ok1 = True
for trial in range(6):
    n = random.choice([2, 3, 4])
    B = [[F(random.randint(-3, 3)) if j > i else F(0) for j in range(n)] for i in range(n)]
    # unknowns: entries of A (n^2), equations: (AB - BA)[i][j] = B[i][j]
    M = []; b = []
    for i in range(n):
        for j in range(n):
            row = [F(0)]*(n*n)
            for t in range(n):
                row[i*n+t] += B[t][j]      # (AB)_{ij} = sum_t A_{it} B_{tj}
                row[t*n+j] -= B[i][t]      # (BA)_{ij} = sum_t B_{it} A_{tj}
            M.append(row); b.append(B[i][j])
    sol = solve_exact(M, b)
    assert sol is not None, "no A found"
    A = [[sol[i*n+j] for j in range(n)] for i in range(n)]
    AB = matmul(A, B); BA = matmul(B, A)
    comm = [[AB[i][j]-BA[i][j] for j in range(n)] for i in range(n)]
    ok_ab = (comm == B)
    # [A,B^k] = k B^k ; tr(B^k)=0 ; B^n = 0
    ok_pow = all([[matmul(A, matpow(B,k))[i][j]-matmul(matpow(B,k),A)[i][j] for j in range(n)]
                  for i in range(n)] == [[k*matpow(B,k)[i][j] for j in range(n)] for i in range(n)]
                 for k in range(1, n+1))
    tr = [sum(matpow(B,k)[i][i] for i in range(n)) for k in range(1, n+1)]
    ok_nil = all(v == 0 for v in tr) and all(v == 0 for row in matpow(B, n) for v in row)
    ok1 &= ok_ab and ok_pow and ok_nil
    print(f"  n={n} trial={trial}: AB-BA==B {ok_ab}, [A,B^k]=kB^k {ok_pow}, tr(B^k)=0 & B^n=0 {ok_nil}")
print("  ==> 题1 代数恒等式全部通过:", ok1)

# ---------------------------------------------------------------- 题 2
def poly_divmod(a, b, p):
    a = [x % p for x in a]; b = [x % p for x in b]
    while len(b) > 1 and b[-1] == 0: b.pop()
    if b == [0]: raise ZeroDivisionError
    inv = pow(b[-1], p-2, p)
    q = [0]*max(1, len(a)-len(b)+1); r = a[:]
    while len(r) >= len(b) and any(r):
        d = len(r)-len(b)
        c = r[-1]*inv % p
        q[d] = c
        for i in range(len(b)):
            r[d+i] = (r[d+i] - c*b[i]) % p
        while len(r) > 1 and r[-1] == 0: r.pop()
    return q, r

def poly_mulmod(a, b, mod, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] = (c[i+j] + x*y) % p
    _, r = poly_divmod(c, mod, p)
    return r

def poly_powmod(a, e, mod, p):
    r = [1]
    while e:
        if e & 1: r = poly_mulmod(r, a, mod, p)
        a = poly_mulmod(a, a, mod, p); e >>= 1
    return r

def is_irreducible(f, p):
    """Rabin test for monic f over F_p."""
    n = len(f)-1
    if n == 0: return False
    x = [0, 1]
    # x^(p^n) == x mod f
    h = x[:]
    for _ in range(n): h = poly_powmod(h, p, f, p)
    if h != x: return False
    for q in {q for q in range(1, n+1) if n % q == 0 and all(n % d for d in range(2, q))}:
        pass
    # distinct prime divisors of n
    primes = []
    m = n
    d = 2
    while d*d <= m:
        if m % d == 0:
            primes.append(d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: primes.append(m)
    for q in primes:
        h = x[:]
        for _ in range(n//q): h = poly_powmod(h, p, f, p)
        g = [ (h[i] if i < len(h) else 0) - (x[i] if i < len(x) else 0) for i in range(max(len(h), len(x))) ]
        # gcd(g, f)
        a, b = g[:], f[:]
        while any(a):
            while len(a) > 1 and a[-1] == 0: a.pop()
            if len(a) < len(b): a, b = b, a
            _, r = poly_divmod(a, b, p)
            a = r if any(r) else [0]
            if a == [0]: break
            a, b = b, a
        if len(b)-1 > 0: return False
    return True

hdr("题 2 (2012 ind #1): f = x^6+30x^5-15x^3+6x-120")
f = [ -120, 6, 0, -15, 0, 30, 1 ]
print("  非首项系数:", f[:-1], " gcd =", __import__('math').gcd(*[abs(v) for v in f[:-1]]))
print("  Eisenstein at 3: 3|全部非首项系数 ->", all(v % 3 == 0 for v in f[:-1]),
      ";  9 ∤ 常数项 -120 ->", (-120) % 9 != 0, ";  3 ∤ 首项 1 ->", 1 % 3 != 0)
for p in [2, 5, 7]:
    fp = [v % p for v in f]
    print(f"  f mod {p} 可约 ? -> 不可约 = {is_irreducible(fp, p)}")
irr_ps = [p for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
          if is_irreducible([v % p for v in f], p)]
print("  使 f mod p 不可约的素数 (p<=97):", irr_ps)
print("  -> 最小的这样的素数 =", (irr_ps or [None])[0], " (对比讲义『模约化这条路会失败』的说法)")

# ---------------------------------------------------------------- 题 4
hdr("题 4 (2013 ind #1): 26 阶群与 Aut(D_26)")
def d26_mul(x, y):
    k, e = x; l, g = y
    return ((k + (l if e == 0 else -l)) % 13, (e+g) % 2)
G26 = [(k, e) for k in range(13) for e in range(2)]
ident = (0, 0)
auts = []
for im_s in G26:
    for im_t in G26:
        # von Dyck: need im_s^13 = 1, im_t^2 = 1, im_t*im_s*im_t = im_s^{-1}
        # im_s must have order dividing 13 -> automatic for k in Z/13
        if d26_mul(im_t, im_t) != ident: continue
        if d26_mul(d26_mul(im_t, im_s), im_t) != ((-im_s[0]) % 13, 0): continue
        phi = {}
        for k, e in G26:
            v = ident
            w = (im_s[0]*k % 13, 0) if True else None
            # s^k t^e -> im_s^k * im_t^e
            for _ in range(k): v = d26_mul(v, im_s)
            if e: v = d26_mul(v, im_t)
            phi[(k, e)] = v
        if len(set(phi.values())) == 26: auts.append(phi)
print("  |Aut(D_26)| =", len(auts), " (讲义断言 156)")
# 结构: 唯一的 13 阶正规子群 + 补群 Z/12, 且同构于 Hol(Z/13)
def aut_order(phi):
    o = 1; v = (1, 0)
    while phi[(v[0], v[1])] != (1, 0):
        v = phi[v]; o += 1
    return o
orders = {}
for phi in auts: orders[aut_order(phi)] = orders.get(aut_order(phi), 0) + 1
print("  自同构的阶分布:", dict(sorted(orders.items())))
nonab = None
for phi in auts:
    for psi in auts:
        comp = {x: phi[psi[x]] for x in G26}
        if comp not in auts: nonab = "NOT-A-GROUP"; break
print("  复合封闭 (=群):", nonab is None)
print("  存在阶 12 的自同构, 存在 12 阶循环子群:",
      max(orders) == 12, " 阶 12 元素个数 =", orders.get(12, 0))

# ---------------------------------------------------------------- 题 5
hdr("题 5 (2016 team #3): K = Q(i,alpha), alpha^4-alpha^2-1=0, 子域格")
# basis (k,m): alpha^k i^m, k=0..3, m=0..1 ;  alpha^4 = alpha^2+1, i^2=-1
from functools import lru_cache
@lru_cache(None)
def apow(n):
    if n < 4: return {n: F(1)}
    d = {}
    for k, v in apow(n-2).items(): d[k] = d.get(k, F(0)) + v
    for k, v in apow(n-4).items(): d[k] = d.get(k, F(0)) + v
    return d
def zero(): return {}
def mul(x, y):
    d = {}
    for (k1, m1), c1 in x.items():
        for (k2, m2), c2 in y.items():
            s = m1 + m2
            sgn = -1 if (s // 2) % 2 else 1
            e = s % 2
            for k, cc in apow(k1+k2).items():
                key = (k, e); d[key] = d.get(key, F(0)) + c1*c2*sgn*cc
    return {k: v for k, v in d.items() if v != 0}
def add(x, y):
    d = dict(x)
    for k, v in y.items():
        d[k] = d.get(k, F(0)) + v
        if d[k] == 0: del d[k]
    return d
def neg(x): return {k: -v for k, v in x.items()}
def one(): return {(0, 0): F(1)}
def alpha(): return {(1, 0): F(1)}
def ii(): return {(0, 1): F(1)}
def inv_alpha(): return {(3, 0): F(1), (1, 0): F(-1)}   # alpha^3-alpha
r = mul(neg(ii()), inv_alpha())  # r(alpha) = -i*alpha^{-1} = -i*alpha^3 + i*alpha
r_a = add({(3, 1): F(-1)}, {(1, 1): F(1)})   # -i*alpha^3 + i*alpha
assert r == r_a, (r, r_a)
r_i = {(0, 1): F(-1)}
c_a = alpha(); c_i = {(0, 1): F(-1)}
def lift(img_a, img_i):
    def f(x):
        out = {}
        for (k, m), coef in x.items():
            t = one()
            for _ in range(k): t = mul(t, img_a)
            if m: t = mul(t, img_i)
            out = add(out, {kk: coef*vv for kk, vv in t.items()})
        return out
    return f
R = lift(r_a, r_i); C = lift(c_a, c_i)
# 检查 R, C 是域自同构（保持乘法）
basis = [{(k, m): F(1)} for k in range(4) for m in range(2)]
ok_mult = all(mul(R(x), R(y)) == R(mul(x, y)) and mul(C(x), C(y)) == C(mul(x, y))
              for x in basis for y in basis)
print("  R, C 保持乘法 (基元素两两乘积全检):", ok_mult)
print("  R(alpha)^4-R(alpha)^2-1 =", add(add(mul(mul(R(alpha()),R(alpha())),mul(R(alpha()),R(alpha()))), neg(mul(R(alpha()),R(alpha())))), {(0,0): F(-1)}))
def comp(f, g): return lambda x: f(g(x))
e = lambda x: x
def mat(f): return tuple(tuple(f(b).get((k, m), F(0)) for m in range(2) for k in range(4)) for b in basis)
def order_of(f):
    o = 1; p = f
    while mat(p) != mat(e): p = comp(f, p); o += 1
    return o
print("  ord(R) =", order_of(R), " ord(C) =", order_of(C))
Rinv = comp(R, comp(R, R))   # ord(R)=4 -> R^{-1}=R^3
print("  ord(R)=4, R^3 == R^{-1}:", mat(comp(Rinv, R)) == mat(e))
print("  C R C == R^{-1}:", mat(comp(comp(C, R), C)) == mat(Rinv))
# 子群集合 (由生成元闭包构造), 用于与不动子群比较
def subgroup(gens):
    S = [e]; Sset = {mat(e)}
    cur = [e]
    while cur:
        nxt = []
        for f in cur:
            for g in gens:
                h = comp(g, f); mh = mat(h)
                if mh not in Sset: Sset.add(mh); nxt.append(h)
        S += cur; cur = nxt
    return {mat(f) for f in S}
R2 = comp(R, R); R3 = comp(R, R2)
c1 = comp(C, R); c2 = comp(C, R2); c3 = comp(C, R3)
SUB = {
 'G': subgroup([R, C]),
 '<r>': subgroup([R]), '<r2>': subgroup([R2]),
 '<c>': subgroup([C]),
 '<r2,c>': subgroup([R2, C]),
 '<r2,cr>': subgroup([R2, c1]),
 '<cr>': subgroup([c1]), '<cr2>': subgroup([c2]), '<cr3>': subgroup([c3]),
 '<e>': {mat(e)},
}

for nm, H in SUB.items():
    print(f"    子群 {nm:8s} 阶 {len(H)}")
Gset = []
cur = [e]
seen = {mat(e)}
while cur:
    nxt = []
    for f in cur:
        for g in (R, C):
            h = comp(g, f); mh = mat(h)
            if mh not in seen: seen.add(mh); nxt.append(h)
    Gset += cur; cur = nxt
print("  |<R,C>| =", len(Gset), " (应为 8)")
# 元素次数的线性代数
def vec(x):
    v = []
    for k in range(4):
        for m in range(2): v.append(x.get((k, m), F(0)))
    return v
def lindep(vs):
    """return True if vs are linearly dependent"""
    M = [list(v) for v in vs]; n = len(M); m = len(M[0]); r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [v/pv for v in M[r]]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f2 = M[i][c]; M[i] = [M[i][j]-f2*M[r][j] for j in range(m)]
        r += 1
    return r < n
def deg(x):
    pw = [one()]
    cur = one()
    for n in range(1, 9):
        cur = mul(cur, x); pw.append(cur)
        if lindep([vec(z) for z in pw]): return n
    return None
def stab(x): return sum(1 for g in Gset if g(x) == x)
sqrt5 = add(mul({(2,0): F(2)}, one()), {(0,0): F(-1)})    # 2*alpha^2 - 1
i_sqrt5 = mul(ii(), sqrt5)
u = add(alpha(), mul(ii(), inv_alpha()))
v = add(alpha(), neg(mul(ii(), inv_alpha())))
ia = mul(ii(), alpha())
elems = {
 'Q': ('G', one()),
 'Q(sqrt5)': ('<r2,c>', sqrt5),
 'Q(i)': ('<r2,cr>', ii()),
 'Q(sqrt-5)': ('<r>', i_sqrt5),
 'Q(i,sqrt5)': ('<r2>', add(ii(), sqrt5)),
 'Q(alpha)': ('<c>', alpha()),
 'Q(i,u)': ('<cr>', add(ii(), u)),
 'Q(i,v)': ('<cr3>', add(ii(), v)),
 'Q(i*alpha)': ('<cr2>', ia),
 'K': ('<e>', add(alpha(), ii())),
}
STAB = {name: {mat(g) for g in Gset if g(x) == x} for name, (_s, x) in elems.items()}
print("  u^2==1+2i:", mul(u,u) == add(one(), mul({(0,0): F(2)}, ii())))
print("  v^2==1-2i:", mul(v,v) == add(one(), neg(mul({(0,0): F(2)}, ii()))))
print("  u*v==sqrt5:", mul(u,v) == sqrt5)
print("  R(sqrt5) == -sqrt5:", R(sqrt5) == neg(sqrt5))
print("  不动子群核对 (Stab(生成元) ?= 讲义所给子群):")
allok = True
for name, (sub, x) in sorted(elems.items()):
    St = STAB[name]
    good = (St == SUB[sub]) and (deg(x) == 8//len(St))
    allok &= good
    print(f"    {name:12s} 讲义子群 {sub:10s} deg={deg(x)} |Stab|={len(St)} == |{sub}|={len(SUB[sub])} ? {St == SUB[sub]}  deg==8/|Stab| ? {deg(x)==8//len(St)}")
print("  ==> 题5 子域格 10 项全部核对通过:", allok)
# 讲义声称的子域包含关系
# 每对写作 (小, 大) 即 "小 含于 大"
contains = [('Q','Q(sqrt5)'),('Q','Q(i)'),('Q','Q(sqrt-5)'),
            ('Q(sqrt5)','Q(i,sqrt5)'),('Q(i)','Q(i,sqrt5)'),('Q(sqrt-5)','Q(i,sqrt5)'),
            ('Q(sqrt5)','Q(alpha)'),('Q(i)','Q(i,u)'),('Q(i)','Q(i,v)'),('Q(sqrt5)','Q(i*alpha)'),
            ('Q(alpha)','K'),('Q(i,u)','K'),('Q(i,v)','K'),('Q(i*alpha)','K'),('Q(i,sqrt5)','K')]
mutual = [('Q(sqrt5)','Q(i)'),('Q(sqrt5)','Q(sqrt-5)'),('Q(i)','Q(sqrt-5)'),
          ('Q(i)','Q(alpha)'),('Q(sqrt-5)','Q(alpha)'),('Q(i)','Q(i*alpha)'),
          ('Q(i,u)','Q(i,v)'),('Q(i,u)','Q(sqrt5)'),('Q(i,v)','Q(sqrt5)')]
def field_le(a, b):   # a 含于 b  <-> Stab(b) 包含于 Stab(a)
    return STAB[a] >= STAB[b]
bad = [(a,b) for a,b in contains if not field_le(a,b)]
bad2 = [(a,b) for a,b in mutual if field_le(a,b) or field_le(b,a)]
print("  讲义声称的包含关系 (应全为 True):", bad == [], " 反例:", bad)
print("  讲义声称的互不包含 (应全为 True):", bad2 == [], " 反例:", bad2)
print("  field_le 语义自检 (Q <= Q(sqrt5)):", field_le('Q','Q(sqrt5)'),
      " (Q(sqrt5) <= Q 应为 False):", field_le('Q(sqrt5)','Q'))
