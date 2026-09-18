import re
p = r'E:\deepseek_exclusive\math\.tmp\burn2026\reports\solutions_algebra.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
print("bytes:", len(open(p,'rb').read()), " lines:", len(lines))
print("backspace chars (should be 0):", s.count(chr(8)))
mark = [i+1 for i,l in enumerate(lines) if '✅ 已按 referee_algebra.md 修正' in l]
print("marker count:", len(mark), mark)
bad = [(i+1, l.strip()[:90]) for i,l in enumerate(lines)
       if re.search(r'\$(gcd|mathrm|mathbb|alpha|beta|eta|zeta|gamma|Tr)\b', l) or re.search(r'\b(subseteq|Rightarrow|mid)\b', l)]
print("remaining missing-backslash lines:", bad)
for kw in ['p-\\sum_x\\chi_2', '150 条', 'Langrange', '照旧成立，故第 3 问', '在任意特征 $\\ne2$ 的域中']:
    print("still contains", repr(kw), ":", kw in s)
for kw in ['referee_algebra.md', '共 149 条', 'p+\\sum_{x\\in\\mathbb F_p}\\chi_2', 'c\\tau c', '1\\pm 2i 不是', 'x^2+x+1$ 在 $\\mathbb F_2$ 上取值', '二面体群']:
    print("contains", repr(kw), ":", kw in s)
