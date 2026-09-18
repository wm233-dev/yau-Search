
import sys, os
sys.path.insert(0, r'sources/pylibs')
import fitz
sys.stdout.reconfigure(encoding='utf-8')
path = sys.argv[1]
doc = fitz.open(path)
out=[]
for i,page in enumerate(doc):
    out.append('---- page %d ----' % (i+1))
    out.append(page.get_text())
print('\n'.join(out))
