# -*- coding: utf-8 -*-
"""Debug the 题6 (Fitting) brute force harness."""
from itertools import product
mods = [2,2]
def gadd(a,b,mods): return tuple((a[i]+b[i]) % mods[i] for i in range(len(mods)))
def order_of(a, mods):
    if not any(a): return 1
    o=1; v=a
    while any(v): v=gadd(v,a,mods); o+=1
    return o
elems = list(product(*[range(m) for m in mods]))
zero = (0,)*len(mods)
opts = [[v for v in elems if mods[i] % order_of(v,mods) == 0] for i in range(len(mods))]
print("每个生成元允许的像:", opts)
print("内同态总数:", len(opts[0])*len(opts[1]))
for images in product(*opts):
    def phi(x, images=images):
        r = tuple(0 for _ in mods)
        for i, xi in enumerate(x):
            r = gadd(r, tuple(xi*images[i][j] % mods[j] for j in range(len(mods))), mods)
        return r
    def it(k,x):
        for _ in range(k): x = phi(x)
        return x
    A_nil = {x for x in elems if any(it(k,x) == zero for k in range(1, 40))}
    K = 1
    while True:
        imgK = {it(K,x) for x in elems}; imgK1 = {it(K+1,x) for x in elems}
        if len(imgK)==len(imgK1) and A_nil <= {x for x in elems if it(K,x)==zero}: break
        K += 1
        if K > 60: break
    A0 = imgK
    ok = (A0 & A_nil) == {zero} and len(A0)*len(A_nil) == len(elems) and len(A0|A_nil)==len(elems) and {phi(x) for x in A0}==A0
    if not ok:
        print("FAIL images=", images, " phi:", [(x, phi(x)) for x in elems])
        print("  K=",K," A0=",sorted(A0)," A_nil=",sorted(A_nil))
        print("  |A0|=",len(A0),"|A_nil|=",len(A_nil),"|A|=",len(elems), " A0&A_nil=",A0&A_nil)
        break
