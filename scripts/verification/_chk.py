
# -*- coding: utf-8 -*-
import json, sys, collections, statistics as st, re, os
sys.stdout.reconfigure(encoding='utf-8')
BASE=r'./txt'
def load(f): return open(os.path.join(BASE,f),'rb').read().replace(b'\x00',b'').decode('utf-8',errors='replace')
# show 2017 individual Q5 raw tail and 2019 individual raw
t=load('2017_applied2017_individual.txt')
i=t.find('5. Consider the differential')
print('--- 2017 individual Q5 raw ---')
print(t[i:i+2000])
print()
t2=load('2019_AppliedMath2019_individual.txt')
print('--- 2019 individual: all "N)" line starts ---')
for m in re.finditer(r'^\s*(\d+)\)', t2, flags=re.M):
    print(m.start(), repr(t2[m.start():m.start()+70].replace(chr(10),' | ')))
