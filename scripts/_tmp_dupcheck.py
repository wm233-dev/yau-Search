
# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=r'E:\deepseek_exclusive\math\.tmp\burn2026'
probs=json.load(io.open(os.path.join(ROOT,'scripts','algebra_probs_full.json'),encoding='utf-8'))
allkeys=set()
TKEYS="""2010T5 2011I6 2011T5 2012I2 2012T2 2013I1 2013T3 2014I4 2014T4 2015T2 2016I5 2017T1 2018I3 2019T1 2023Q1 2025Q2
2010I1 2011I4 2012T1 2013I2 2013T1 2013T2 2014I2 2014I6 2014T3 2015T5 2016I1 2016T1 2017I5 2018I4 2018T5 2019I4 2020Q1
2012I5 2014T6 2015I3 2015T3 2016I3 2018I2 2019T4 2021Q5 2022Q4 2022Q5 2022Q6 2024Q6 2025Q5 2026Q3 2026Q4
2011T5 2012I2 2012T2 2013I3 2013T3 2013T5 2014I5 2017I4 2018I4 2019I5 2020Q4 2021Q1 2025Q2 2026Q2
2011T1 2011T3 2012T5 2015I5 2019I3 2019T3 2020Q2 2020Q3 2021Q3 2022Q2 2023Q4 2025Q3 2026Q3
2010I4 2010T4 2011I1 2013T6 2015I3 2015T6 2016T3 2017T4 2019I2 2019T5 2021Q2 2025Q1 2025Q5
2010I6 2010T6 2011I2 2013I4 2013T4 2014I1 2016T4 2018T4 2019I1 2024Q1 2025Q2
2012T6 2015I4 2017I1 2018I5 2020Q5 2020Q6 2021Q6 2023Q5 2024Q5
2010T3 2014T2 2015T3 2018T3 2019T4 2020Q4 2022Q5 2024Q6
2010I2 2011I3 2012I1 2013T2 2021Q4 2022Q1 2024Q3 2024Q4
2010T1 2010T2 2011T4 2017T5 2018I1 2018T2 2019I5
2012T3 2014T1 2015T1 2015I1 2016I1 2016I4 2026Q1
2011T2 2018T1 2022Q2 2023Q2 2023Q4
2012I3 2014T5 2015I2 2015T4 2019T2
2013T2 2016I3 2017T2 2020Q1
2011I5 2022Q2 2023Q4 2025Q4
2012I6 2015I1 2017I2
2023Q6 2025Q4 2026Q5
2012T4 2019I4
2017T3 2022Q3
2017I3 2023Q3
2013I5 2014I3
2010I5 2016T2
2014T1 2026Q1
2024Q2
2012I4""".split()
allkeys=set(TKEYS)
def key(p):
    f=p['file']; y=p['year']
    if y>='2020': t='Q'
    elif 'ndividual' in f: t='I'
    else: t='T'
    return y+t+str(p['n'])
have={key(p) for p in probs}
print('missing from tagged set:',sorted(have-allkeys))
print('tagged but nonexistent:',sorted(allkeys-have))
# 6-gram jaccard
def sh(t,k=6):
    w=re.findall(r"[a-z0-9]+",t.lower())
    return {tuple(w[i:i+k]) for i in range(max(1,len(w)-k+1))} if len(w)>=k else set()
byk={key(p):p for p in probs}
pairs=[("2010T5","2011I6"),("2010T3","2014T2"),("2011T5","2012T2"),("2014I5","2017I4"),
       ("2012I3","2014T5"),("2010I6","2013T4"),("2013I1","2014T4"),("2020Q3","2021Q3"),
       ("2021Q4","2022Q1"),("2015I3","2021Q2"),("2015T6","2025Q5"),("2016T3","2013T6"),
       ("2018T3","2020Q4"),("2019T5","2017T4"),("2012T6","2023Q5"),("2017I1","2012T6"),
       ("2016I2","2023Q3"),("2020Q1","2020Q2"),("2022Q5","2024Q6"),("2019I4","2012T4"),
       ("2026Q4","2022Q6"),("2016T5","2010I3"),("2013I3","2013T5"),("2018I2","2025Q5"),
       ("2011T2","2023Q2"),("2014I1","2019I1")]
for a,b in pairs:
    if a in byk and b in byk:
        sa,sb=sh(byk[a]['head']),sh(byk[b]['head'])
        j=len(sa&sb)/max(1,len(sa|sb))
        print('%-8s %-8s jaccard=%.3f shared=%d  | %s || %s'%(a,b,j,len(sa&sb),byk[a]['head'][:52],byk[b]['head'][:52]))
    else:
        print(a,b,'MISSING')
