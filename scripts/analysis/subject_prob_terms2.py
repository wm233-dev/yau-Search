
import re, os, json
TXT = r".\txt"
PS = {
 "2010": ["2010_Applied_Computational_Probability_and_Statistics_individual.txt","2010_Applied_Computational_Probability_and_Statistics_team.txt"],
 "2011": ["2011_2_AppliedMathProb_Individual_2011.txt","2011_6_AppliedMathProb_Team_2011.txt"],
 "2012": ["2012_Probability2012_individual.txt","2012_Probability2012_team.txt"],
 "2013": ["2013_probability2013_individual.txt","2013_TeamProblems2013.txt"],
 "2014": ["2014_probability2014_individual.txt","2014_probability2014_team.txt"],
 "2015": ["2015_probability2015_individual.txt","2015_team_probability2015.txt"],
 "2016": ["2016_probability2016_individual.txt","2016_2016_team.txt"],
 "2017": ["2017_probability2017_individual.txt","2017_2017_team.txt"],
 "2018": ["2018_probability2018_individual.txt","2018_2018_team.txt"],
 "2019": ["2019_ProbaStat2019_individual.txt","2019_ProbaStat2019_team.txt"],
 "2020": ["2020_Prob_Stat_probability_and_statistics_20.txt"],
 "2021": ["2021_ExamPaper_21S_probability_and_statistics_21s.txt"],
 "2022": ["2022_ExamPaper_2022_probability_and_statistics_22s.txt"],
 "2023": ["2023_probability_statistics.txt"],
 "2024": ["2024_2024_statistics.txt"],
 "2025": ["2025_statistics.txt"],
 "2026": ["2026_2026_statistics.txt"],
}
def read(p):
    return open(p,'rb').read().replace(b'\x00',b' ').decode('utf-8','replace')
def norm(t):
    t = re.sub(r'-\s*\n\s*','',t); t=re.sub(r'\s+',' ',t); return t
def slice_ps(f, t):
    if f == "2013_TeamProblems2013.txt":
        i = t.find("Probability and Statistics Problems"); return t[i:] if i>=0 else ""
    if f in ("2016_2016_team.txt","2017_2017_team.txt","2018_2018_team.txt"):
        for m in re.finditer(r"Probability and Statistics", t):
            i = m.start()
            if "Team" in t[i:i+80]:
                nx = re.search(r"S\.-T\. Yau College Student Mathematics Contests", t[i+50:])
                end = i+50+nx.start() if nx else len(t)
                return t[i:end]
        return ""
    return t
docs=[]
for y,fs in sorted(PS.items()):
    for f in fs:
        s = norm(slice_ps(f, read(os.path.join(TXT,f))))
        docs.append((y,f,s))
big = " ".join(d[2] for d in docs)
terms = ["Borel","Cantelli","martingale","large number","Chebyshev","Cauchy","Jensen","Fubini","Radon","Tonelli","Kolmogorov","Poisson","Dirichlet","Brownian","Fisher","Cramer","Wilcoxon","Mann-Whitney","Bayes","Sklar","SUTVA","Mahalanobis","Horvitz","re-randomi","lasso","Lasso","soft threshold","Lyapunov","Lindeberg","coupling","Chernoff","Bernstein","Darmois","Chung","Feller","Polya","copula","ANOVA","Stein","empirical Bayes","minimax","UMVU","sufficient","unbiased","exponential family","central limit","law of large numbers","ergodic","recurrent","order statistic","indicator","moment generating","characteristic function","conditional expectation","Radon-Nikodym","Dickey","Lasso","consisten","efficien","score function","nuisance","ancillary","pivot","power function","most powerful","uniformly most powerful","UMP","invariance","group family","SUTVA","estimand","attrition","blocking","stratif","propensity","IPW","inverse probability"]
for t in terms:
    c = len(re.findall(re.escape(t), big, re.I))
    if c:
        yrs = sorted({d[0] for d in docs if re.search(re.escape(t), d[2], re.I)})
        print(f"{c:3d}  {t:28s} {','.join(yrs)}")
print("\n== words per year in P&S papers (P&S-sliced) ==")
tot=0
for y in sorted(PS):
    s = " ".join(d[2] for d in docs if d[0]==y)
    tot += len(s)
    print(f"{y}: chars={len(s)}")
print("total chars over 17y P&S slice:", tot)
