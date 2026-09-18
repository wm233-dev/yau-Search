p = r'E:\deepseek_exclusive\math\.tmp\burn2026\reports\solutions_algebra.md'
lines = open(p, encoding='utf-8').read().split('\n')
for n in [999,1000,1007,1009,1025,1026,1027,1028,1029,1030,1037,5]:
    print(n, repr(lines[n-1]))
print("bytes:", len(open(p,'rb').read()))
