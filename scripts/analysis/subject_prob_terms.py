
import re, os, collections
TXT = r".\txt"
files = [f for f in os.listdir(TXT) if re.search(r'prob|stat|ProbaStat|TeamProblems2013|Applied_Computational|AppliedMathProb|2016_team|2017_team|2018_team|2012_Applied', f, re.I)]
def read(p):
    return open(p,'rb').read().replace(b'\x00',b' ').decode('utf-8','replace')
terms = ["Borel","Cantelli","martingale","large number","Chebyshev","Cheby","Cauchy","Jensen","Fubini","Radon","Tonelli","Kolmogorov","Poisson","Dirichlet","Brownian","Fisher","Neyman","Pearson","Wilks","Wald","Lehmann","Scheffe","Rao","Blackwell","Bayes","de Finetti","Sklar","SUTVA","Mahalanobis","Horvitz","Thompson","Fisher exact","re-randomi","soft threshold","lasso","Lasso","Lyapunov","Lindeberg","Slutsky","Portmanteau","Prokhorov","Skorokhod","coupling","Hoeffding","Chernoff","Bernstein","Darmois","Cramer","Wald","Glivenko","Kolmogorov-Smirnov","Wilcoxon","Mann-Whitney","Kruskal","Anderson","Chung","Feller","Polya","Pólya","urn","Dirichlet process","copula","Sklar","ANOVA","Kiefer","Stein","James-Stein","empirical Bayes","minimax","UMVU","complete sufficient","sufficient","unbiased","efficient","consistent","Delta method","delta method","information inequality","Cramer-Rao"]
allt = []
for f in sorted(files):
    if f.endswith('.txt') and not re.search(r'soln', f, re.I):
        allt.append((f, read(os.path.join(TXT,f))))
big = "\n".join(t for _,t in allt)
bigflat = re.sub(r'-\s*\n\s*', '', big)
bigflat = re.sub(r'\s+',' ', bigflat)
for t in terms:
    c = len(re.findall(re.escape(t), bigflat, re.I))
    if c:
        yrs = []
        for f,txt in allt:
            tf = re.sub(r'-\s*\n\s*','',txt); tf=re.sub(r'\s+',' ',tf)
            if re.search(re.escape(t), tf, re.I):
                m = re.match(r'(\d{4})', f)
                if m: yrs.append(m.group(1))
        print(f"{c:3d}  {t:26s} {sorted(set(yrs))}")
