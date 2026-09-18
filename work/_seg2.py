
import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r'.tmp/burn2026/txt'
def load(f):
    return open(os.path.join(BASE,f),'rb').read().replace(b'\x00',b'').decode('utf-8',errors='replace')
files = [
 '2010_Applied_Computational_Probability_and_Statistics_individual.txt',
 '2010_Applied_Computational_Probability_and_Statistics_team.txt',
 '2011_2_AppliedMathProb_Individual_2011.txt',
 '2011_6_AppliedMathProb_Team_2011.txt',
 '2012_Applied2012individual.txt','2012_Applied2012team.txt',
 '2013_applied2013_individual.txt',
 '2014_applied2014_individual.txt','2014_applied2014_team.txt',
 '2015_applied2015_individual.txt','2015_team_applied2015.txt',
 '2016_applied2016_individual.txt',
 '2017_applied2017_individual.txt',
 '2018_applied2018_individual.txt',
 '2019_AppliedMath2019_individual.txt','2019_AppliedMath2019_team.txt',
 '2020_Applied_Math_and_Computational_Math_computational_and_applied_20.txt',
 '2021_ExamPaper_21S_computational_and_applied_21s.txt',
 '2022_ExamPaper_2022_computational_and_applied_22s.txt',
 '2023_Computational_Applied.txt','2024_2024_Computational_Math.txt',
 '2025_computational_and_applied_math.txt','2026_2026_Computation.txt']
pats = [(r'^\s*Problem\s+(\d+)\.','Problem N.'),(r'^\s*(\d+)[.)]\s','N. / N)')]
for f in files:
    t=load(f)
    row=[]
    for p,lab in pats:
        ms=list(re.finditer(p,t,flags=re.M))
        row.append(lab+':'+str(len(ms)))
    print(f[:60].ljust(62), ' | '.join(row))
