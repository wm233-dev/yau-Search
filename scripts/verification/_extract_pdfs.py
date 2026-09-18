
import sys, os
sys.path.insert(0, r'sources/pylibs')
import fitz
base = r'sources/prelim'
out = open(r'./scripts/verification/_pdf_dump.txt','w',encoding='utf-8')
jobs = [
 r'2010\AlgebraNumberTheory-individual.pdf',
 r'2012\Algebra2012Individual.pdf',
 r'2013\algebra2013(individual).pdf',
 r'2014\algebra2014(individual).pdf',
 r'2016\2016-team.pdf',
 r'2017\algebra2017-individual.pdf',
 r'2018\algebra2018-individual.pdf',
 r'2019\Algebra2019-individual.pdf',
]
for rel in jobs:
    p = os.path.join(base, rel)
    out.write('='*78+'\n'+'FILE: '+rel+' exists='+str(os.path.exists(p))+'\n')
    if not os.path.exists(p): continue
    d = fitz.open(p)
    for i in range(d.page_count):
        out.write('--- page %d ---\n' % (i+1))
        out.write(d[i].get_text())
    d.close()
out.write('=== 2022 dir listing:\n')
for f in os.listdir(os.path.join(base,'2022')): out.write('    '+f+'\n')
out.close()
print('done')
