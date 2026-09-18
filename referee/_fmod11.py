f = [-120, 6, 0, -15, 0, 30, 1]
def trim(a):
    a = [x % 11 for x in a]
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a
print("f mod 11 =", trim(f), " (从常数项到最高次)")
print("x^6+8x^5+7x^3+6x+1 的系数向量 =", [1,6,0,7,0,8,1])
# 无根检查 + Rabin 不可约性已在 checkA.py 验证；此处再确认无一次因子
print("f(a) mod 11 for a=0..10:", [sum(c*pow(a,i,11) for i,c in enumerate(f)) % 11 for a in range(11)])
