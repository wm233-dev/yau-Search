
import json, re, os, sys, collections

ROOT = r"E:\deepseek_exclusive\math\.tmp\burn2026"
TXT  = os.path.join(ROOT, "txt")

# P&S paper files 2010-2026 (exam papers only, no solutions)
PS = {
 "2010": ["2010_Applied_Computational_Probability_and_Statistics_individual.txt",
          "2010_Applied_Computational_Probability_and_Statistics_team.txt"],
 "2011": ["2011_2_AppliedMathProb_Individual_2011.txt",
          "2011_6_AppliedMathProb_Team_2011.txt"],
 "2012": ["2012_Probability2012_individual.txt","2012_Probability2012_team.txt",
          "2012_Applied2012individual.txt","2012_Applied2012team.txt"],
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
    b = open(p,'rb').read()
    b = b.replace(b'\x00', b' ')
    return b.decode('utf-8','replace')

KEYWORDS = {
 "Borel-Cantelli": r"Borel[–\-]?\s*Cantelli",
 "central limit theorem / CLT": r"central limit|CLT\b|Lindeberg|Lyapunov",
 "law of large numbers": r"law of large numbers|strong law|SLLN|weak law",
 "characteristic function": r"characteristic function",
 "martingale": r"martingale|optional stopping|stopping time",
 "Markov chain/proc": r"Markov chain|Markov process|Markov",
 "random walk": r"random walk",
 "coupling": r"coupling|coupl",
 "total variation": r"total variation",
 "uniform integrability": r"uniformly integrable|uniform integrab",
 "sufficiency/completeness": r"sufficient statistic|minimal sufficient|complete sufficient|completeness|exponential family|exponential fam",
 "UMVU/UMVUE": r"UMVU|uniformly minimum variance",
 "unbiased": r"unbiased",
 "Cramer-Rao/Fisher info": r"Cramer[–\-]?\s*Rao|Fisher information",
 "MLE / maximum likelihood": r"maximum likelihood|MLE|likelihood ratio",
 "confidence interval/set": r"confidence interval|confidence set|credible interval|coverage probability",
 "hypothesis test / p-value": r"p-value|p value|hypothesis test|test of the hypothesis|power of the test|test statistic|significance level|critical region",
 "Bayes/prior/posterior": r"Bayes|prior|posterior",
 "Lasso / soft threshold": r"lasso|soft threshold|L1-penalty",
 "order statistics": r"order statistic|rank|ranks|rankings",
 "delta method": r"delta method|after appropriate normalization|asymptotic distribution",
 "minimax / empirical Bayes": r"minimax|empirical Bayes",
 "Brownian motion / Poisson process": r"Brownian|Poisson process",
 "copula": r"copula|Sklar",
 "randomized experiment / causal": r"randomi[sz]ed (experiment|trial|allocation)|re-?randomization|Mahalanobis|causal|SUTVA|potential outcome|allocat",
 "Dirichlet process": r"Dirichlet process",
 "concentration / Chernoff": r"concentration|Chernoff|moment generating function|sub-?gaussian",
 "records / extremes": r"record|maximum record|lim sup",
 "stable distribution": r"stable distribution|stable law",
 "conditional expectation": r"conditional expectation|conditional distribution|conditional probabilit|E\(X\||E\[X\|",
 "normal / Gaussian": r"normal|Gaussian|N\(0,\s*1\)",
 "exponential distribution": r"exponential",
 "Bernoulli": r"Bernoulli",
 "Poisson dist": r"Poisson",
 "variance/covariance": r"variance|covariance|Var\b",
 "independence": r"independen",
 "convergence in prob/dist": r"in probability|in distribution|converges? in distribution|weak convergence|almost surely|a\.s\.",
 "i.i.d.": r"i\.i\.d|independent and identically|independently and identically",
 "ergodic/recurrence": r"recurrent|recurrence|transient|stationary",
 "sufficient/complete": r"complete",
 "regression / linear model": r"regression|linear model|OLS|design matrix",
 "GLM / exponential family": r"exponential family|GLM|log-likelihood",
 "nonparametric / density est": r"nonparametric|histogram|kernel density|density estimat",
 "ANOVA": r"ANOVA",
 "Stein / shrinkage": r"James[–\-]?\s*Stein|shrink",
}

def clean(s):
    s = s.replace('=== page', ' ')
    s = re.sub(r'\s+',' ', s)
    return s

rows = []
for y, files in sorted(PS.items()):
    for f in files:
        p = os.path.join(TXT, f)
        if not os.path.exists(p):
            print("MISSING", f); continue
        rows.append((y, f, read(p)))

print("== per-file char counts (P&S papers, raw txt) ==")
for y,f,t in rows:
    print(f"{y} {f:70s} chars={len(t)}")

# keyword counts restricted to P&S papers, but for 2013/2016/2017/2018 multi-subject team files we must slice P&S section only.
def slice_ps(y, f, t):
    if f == "2013_TeamProblems2013.txt":
        i = t.find("Probability and Statistics Problems")
        return t[i:] if i>=0 else ""
    if f in ("2016_2016_team.txt","2017_2017_team.txt","2018_2018_team.txt"):
        # take from the 'Probability and Statistics' header that precedes 'Team'
        idxs = [m.start() for m in re.finditer(r"Probability and Statistics", t)]
        # choose the one followed within 60 chars by 'Team'
        for i in idxs:
            if "Team" in t[i:i+80]:
                # section ends at next subject header
                nxt = re.search(r"S\.-T\. Yau College Student Mathematics Contests", t[i+50:])
                end = i+50+nxt.start() if nxt else len(t)
                return t[i:end]
        return ""
    if f in ("2010_Applied_Computational_Probability_and_Statistics_individual.txt",
             "2010_Applied_Computational_Probability_and_Statistics_team.txt",
             "2011_2_AppliedMathProb_Individual_2011.txt",
             "2011_6_AppliedMathProb_Team_2011.txt",
             "2012_Applied2012individual.txt","2012_Applied2012team.txt"):
        return t  # combined paper: whole file is in scope, but we flag it
    return t

corpus = []
for y,f,t in rows:
    s = slice_ps(y,f,t)
    corpus.append((y,f,clean(s)))

alltext = " ".join(c[2] for c in corpus)
print("\n== keyword counts over P&S papers ==")
kw = {}
for name, pat in KEYWORDS.items():
    n = len(re.findall(pat, alltext, re.I))
    years = sorted({y for y,f,s in corpus if re.search(pat, s, re.I)})
    kw[name] = (n, years)
for name,(n,years) in sorted(kw.items(), key=lambda kv:-kv[1][0]):
    print(f"{n:4d}  {name:38s} years={','.join(years)}")

json.dump({k:{"n":v[0],"years":v[1]} for k,v in kw.items()}, open(os.path.join(ROOT,"scripts","subject_prob_kw.json"),"w"), ensure_ascii=False, indent=1)
print("\nwritten scripts/subject_prob_kw.json")
