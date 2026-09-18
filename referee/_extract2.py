
import sys, os
sys.path.insert(0, r'E:\deepseek_exclusive\math\pylibs')
import fitz
base = r'F:\丘成桐大学生数学竞赛历年笔试真题'
out = open(r'E:\deepseek_exclusive\math\.tmp\burn2026\referee\_pdf_dump2022.txt','w',encoding='utf-8')
for sub in ['2022\\ExamPaper_2022','2022\\Solution_2022','2011','2010']:
    d0 = os.path.join(base, sub)
    out.write('#### DIR '+sub+'\n')
    if not os.path.isdir(d0):
        out.write('   MISSING\n'); continue
    for f in sorted(os.listdir(d0)):
        out.write('    '+f+'\n')
out.write('\n')
# extract algebra 2022 exam + solution
for sub in ['2022\\ExamPaper_2022','2022\\Solution_2022']:
    d0 = os.path.join(base, sub)
    if not os.path.isdir(d0): continue
    for f in sorted(os.listdir(d0)):
        if 'lgebra' in f or 'umber' in f or 'alg' in f.lower():
            p = os.path.join(d0,f)
            if not p.lower().endswith('.pdf'): continue
            out.write('='*78+'\nFILE: '+sub+'\\'+f+'\n')
            doc = fitz.open(p)
            for i in range(doc.page_count):
                out.write('--- page %d ---\n'%(i+1)); out.write(doc[i].get_text())
            doc.close()
# 2010 team + 2011 individual algebra
for rel in ['2010\\AlgebraNumberTheory-team.pdf','2011\\AlgebraNumberTheory-individual.pdf','2011\\AlgebraNumberTheory-indi.pdf']:
    p = os.path.join(base, rel)
    if os.path.exists(p):
        out.write('='*78+'\nFILE: '+rel+'\n')
        doc = fitz.open(p)
        for i in range(doc.page_count):
            out.write('--- page %d ---\n'%(i+1)); out.write(doc[i].get_text())
        doc.close()
out.close(); print('done')
