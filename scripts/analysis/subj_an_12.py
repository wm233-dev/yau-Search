
# -*- coding: utf-8 -*-
import os, re, json, collections
TXT = r".\txt"
CLEAN = r".\scripts\_clean"
def rd(p): return open(p, encoding="utf-8", errors="replace").read()
def norm(s):
    s = s.replace("\ufb01","fi").replace("\ufb02","fl").replace("\ufb00","ff").replace("\ufb03","ffi").replace("\ufb04","ffl")
    s = s.replace("\u2019","'").replace("\u201c",'"').replace("\u201d",'"')
    return s
papers = {
 2010: ["2010_Analysis_and_differential_equations_individual.txt","2010_Analysis_and_differential_equations_team.txt"],
 2011: ["2011_1_AnalysisDiffEquation_Individual_2011.txt","2011_5_AnalysisDiffEquation_Team_2011.txt"],
 2012: ["2012_Analysis_individual.txt","2012_Analysis_team.txt"],
 2013: ["2013_analysis2013_individual.txt"],
 2014: ["2014_analysis2014_individual.txt","2014_analysis2014_team.txt"],
 2015: ["2015_analysis2015_individual.txt","2015_team_analysis2015.txt"],
 2016: ["2016_analysis2016_individual.txt"],
 2017: ["2017_analysis2017_individual.txt"],
 2018: ["2018_analysis2018_individual.txt"],
 2019: ["2019_Analysis2019_individual.txt","2019_Analysis2019_team.txt"],
 2020: ["2020_Analysis_DifferentialEquations_analysis_and_differential_20.txt"],
 2021: ["2021_ExamPaper_21S_analysis_and_differential_21s.txt"],
 2022: ["2022_ExamPaper_2022_analysis_and_differential_22s.txt"],
 2023: ["2023_Analysis_and_differential_equation.txt"],
 2024: ["2024_2024_Analysis_and_diff_v2.txt"],
 2025: ["2025_analysis.txt"],
 2026: ["2026_2026_analysis.txt"],
}
t13 = norm(rd(os.path.join(TXT,"2013_TeamProblems2013.txt")))
team13 = [p for p in re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests 2013)", t13) if "Analysis and Di" in p[:400]][0]
team = {2013: team13}
for y,f in [(2016,"2016_2016_team.txt"),(2017,"2017_2017_team.txt"),(2018,"2018_2018_team.txt")]:
    t = norm(rd(os.path.join(CLEAN,f)))
    for p in re.split(r"(?=S\.-T\. Yau College Student Mathematics Contests "+str(y)+")", t):
        if "Analysis and Di" in p[:400]:
            team[y]=p
secs = {}   # (year,part) -> text
for y,fs in papers.items():
    for f in fs:
        part = "T" if "team" in f.lower() else "I"
        secs[(y,part)] = norm(re.sub(r"=== page \d+ ==="," ",rd(os.path.join(TXT,f))))
for y,t in team.items():
    secs[(y,"T")] = norm(re.sub(r"=== page \d+ ==="," ",t))

print("year part chars words")
per = collections.defaultdict(lambda: [0,0])
for (y,p),t in sorted(secs.items()):
    w=len(re.findall(r"[A-Za-z][A-Za-z'\-]*", t))
    per[y][0]+=len(t); per[y][1]+=w
    print(f"{y} {p} {len(t):5d} {w:4d}")

PATS = {
 "全纯/解析": r"holomorphic|analytic function|analytic on|entire function|meromorphic",
 "整函数(entire)": r"entire function|entire f",
 "共形映射": r"conformal|Mobius|M\u00f6bius|biholomorphic|one to one holomorphic",
 "调和函数": r"harmonic function|harmonic on|harmonic over|harmonic in|subharmonic|superharmonic",
 "Laplace/Δ 方程": r"Laplace|\\bLaplacian|delta u|\u2206u|\u2206 =|\u2206f|\u2206g|\\\\Delta",
 "Poisson 核/积分": r"Poisson",
 "Newton 位势/基本解": r"Newton potential|fundamental solution|Newtonian",
 "Green 函数/Dirichlet 问题": r"Green function|Dirichlet problem|Dirichlet",
 "极大值原理": r"maximum principle|maximal principle|maximum of|maximum value|Harnack",
 "Sobolev/H^1/W^{1,2}": r"Sobolev|W1,2|W\^\{?1,2|H1\b|H\u00b9|H1 0|H\u00b9\u2080|H_0\^1|H1\n0",
 "Fourier/Plancherel/卷积": r"Fourier|Plancherel|convolution|convolve",
 "逼近恒等/磨光": r"approximate identity|mollif|\u03d5\u03b5|\u03c6\u03b5|K\u03b4",
 "弱收敛": r"weakly|weak convergence|weak limit",
 "紧算子": r"compact operator|compactness of|is compact|compact linear|precompact|relatively compact",
 "Fredholm/余核/闭值域": r"Fredholm|Coker|cokernel|KerT|Ker T|finite dimensional and Im|closed in H",
 "自伴/谱/特征值": r"self-adjoint|spectrum|eigenvalue|eigenvector|orthonormal basis of H|orth-normal",
 "Hilbert 空间": r"Hilbert space",
 "Banach 空间": r"Banach",
 "有界线性泛函/Riesz 表示": r"linear functional|Riesz representation|Borel measure",
 "测度/可测/Lebesgue": r"measurable|Lebesgue measure|Borel measure|measure zero|m\(E|measure of",
 "几乎处处/收敛定理": r"almost everywhere|a\.e\.|a\.s\.|dominated convergence|monotone convergence",
 "Borel-Cantelli/覆盖论证": r"Borel|Cantelli|Vitali|covering",
 "凸性/Jensen": r"convex|Jensen",
 "Gronwall/ODE 比较": r"Gronwall|Lyapunov|stability of the solution",
 "不确定性原理": r"uncertainty",
 "Liouville/Picard": r"Liouville|Picard",
 "Schwarz 引理/Pick": r"Schwarz|Pick",
 "Arzela-Ascoli": r"Arzel|Ascoli",
 "一致有界原理(Banach-Steinhaus)": r"Banach-Steinhaus|Banach\u2013Steinhaus|uniform boundedness|Banach Steinhaus",
 "Poincare 不等式": r"Poincar\u00e9 inequality|Poincare inequality|smallest constant C",
 "热方程/热核": r"heat equation|heat kernel|fundamental solution of the heat",
 "波动方程/双曲": r"wave equation|semilinear wave|\u25a1u",
 "椭圆型非线性 PDE": r"semilinear|monotone|variational|Lax-Milgram|weak solution|exists a unique",
 "Euler-Lagrange/变分": r"Euler-Lagrange|Euler\u2013Lagrange|variational|functional S|extremal",
 "留数/围道/Rouche": r"residue|Rouch\u00e9|Rouche|argument principle|contour|closed curve|winding",
 "开映射/最大模": r"open mapping|maximum modulus|maps .* onto itself",
 "H\u00f6lder/Schauder 估计": r"H\u00f6lder|Holder|Schauder|C2,\u03b1|C2,a",
 "估计/不等式": r"inequality|estimate|bound",
 "单调/一致性": r"uniformly|uniform convergence|converges uniformly",
 "分步小问": r"^\(?[a-e]\)|^\(?[1-9]\)",
 "年份彩蛋数字": r"\b20(1[0-9]|2[0-9])\b",
}
years = sorted(set(y for y,_ in secs))
print("\n| 关键词 | 命中题面段数/次数 | 年份 |")
allt = "\n".join(t for _,t in sorted(secs.items()))
res={}
for name,pat in PATS.items():
    ys=[]; cnt=0
    for (y,p),t in sorted(secs.items()):
        c=len(re.findall(pat,t,flags=re.M))
        if c: ys.append(y); cnt+=c
    res[name]=(cnt, sorted(set(ys)))
for name,(c,ys) in sorted(res.items(), key=lambda kv:-kv[1][0]):
    print(f"{name}\t{c}\t{','.join(map(str,ys))}")
json.dump({k:[v[0],v[1]] for k,v in res.items()}, open(r".\scripts\an_kw.json","w"), ensure_ascii=False, indent=1)
