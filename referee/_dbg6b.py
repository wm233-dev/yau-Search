from itertools import product
mods=[2,2]
def gadd(a,b,mods): return tuple((a[i]+b[i]) % mods[i] for i in range(len(mods)))
def order_of(a,mods):
    if not any(a): return 1
    o=1; v=a
    while any(v): v=gadd(v,a,mods); o+=1
    return o
elems=list(product(*[range(m) for m in mods])); zero=(0,)*2
opts=[[v for v in elems if mods[i] % order_of(v,mods)==0] for i in range(2)]
images=((0,0),(0,1))
def phi(x):
    r=tuple(0 for _ in mods)
    for i,xi in enumerate(x):
        r=gadd(r, tuple(xi*images[i][j] % mods[j] for j in range(2)), mods)
    return r
def it(k,x):
    for _ in range(k): x=phi(x)
    return x
A_nil={x for x in elems if any(it(k,x)==zero for k in range(1,40))}
K=1
while True:
    imgK={it(K,x) for x in elems}; imgK1={it(K+1,x) for x in elems}
    if len(imgK)==len(imgK1) and A_nil <= {x for x in elems if it(K,x)==zero}: break
    K+=1
    if K>60: break
A0=imgK
c1=(A0 & A_nil)=={zero}
c2=len(A0)*len(A_nil)==len(elems)
c3=len(A0|A_nil)==len(elems)
c4={phi(x) for x in A0}==A0
print("A0",sorted(A0),"A_nil",sorted(A_nil),"K",K)
print("c1",c1,"c2",c2,"c3",c3,"c4",c4)
print("len(A0)*len(A_nil)",len(A0)*len(A_nil),"len(elems)",len(elems),"union",len(A0|A_nil))
