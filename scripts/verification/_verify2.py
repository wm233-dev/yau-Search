import re
p = r'.\reports\solutions_algebra.md'
s = open(p, encoding='utf-8').read()
BS = chr(8)
olds = ['遇多项式先算 $gcd$', '$mathrm{tr}(B^k)=0Rightarrow B$', '$mathrm{Aut}(D_{2n})=mathrm{Hol}(C_n)$',
        '$mathbb F_{p^2}$」是分水岭', '$A(W)subseteq W$', '与 $p^2' + chr(10) + 'mid$',
        '$mathrm{Aut}(D_{26})$ 的 $(a,b)$', '$alpha^{p+1}=alpha' + BS, '$mathrm{Tr}(gamma(1-zeta))',
        '$mathbb F_2$ 上不可约多项式计数']
for o in olds:
    print("OLD-STILL-PRESENT", repr(o[:45]), "->", o in s)
print()
news = ['共 149 条', 'p+\\sum_{x\\in\\mathbb F_p}\\chi_2(x^{3}+1)', 'x^2+x+1$ 在 $\\mathbb F_2$ 上取值 $1,1$ 均非零',
        'c\\tau c$ 把 $\\alpha$ 送到', '$1\\pm2i$ 不是 $\\mathbb Q(i)$ 中的平方', '$\\mathrm{tr}(B^k)=0\\Rightarrow B$',
        '$\\mathrm{Aut}(D_{2n})=\\mathrm{Hol}(C_n)$', '$\\mathbb F_{p^2}$」是分水岭', '$A(W)\\subseteq W$ 的那一行等式',
        '$\\gcd$ 与 $p^2\\nmid$ 常数项', '$\\mathrm{Aut}(D_{26})$ 的 $(a,b)$', '$\\alpha^{p+1}=\\alpha\\beta=\\beta^{p+1}$ 这三步等号',
        '$\\mathrm{Tr}(\\gamma(1-\\zeta))=a_0p$ 的完整计算', '$\\mathbb F_2$ 上不可约多项式计数', '落在 $\\mathrm{Aut}(P)\\times\\mathrm{Aut}(Q)$ 作用的同一轨道上',
        '在最小的几个素数上模约化不可行', '由 Lagrange 定理（$|Z(H)|$ 整除 $p^2$）', '该商群的特征群恰为 $X_m$',
        '若 $\\gamma=p\\beta$ 且 $\\beta\\in\\mathbf Z[\\zeta]$']
for n in news:
    print("NEW-PRESENT", repr(n[:48]), "->", n in s)
