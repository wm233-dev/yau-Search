# -*- coding: utf-8 -*-
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = 'E:/deepseek_exclusive/math/.tmp/burn2026/data/'
full = json.load(open(base + 'problems_full.json', encoding='utf-8'))
targets = {('2010','Geometry & Topology',6),('2011','Algebra & Number Theory',1),('2013','Computational & Applied',2),
('2013','Computational & Applied',5),('2014','Analysis & PDE',5),('2014','Computational & Applied',5),
('2016','Algebra & Number Theory',4),('2016','Computational & Applied',2),('2018','Computational & Applied',1),
('2018','Computational & Applied',2),('2018','Computational & Applied',3),('2019','Computational & Applied',2),
('2019','Geometry & Topology',5),('2023','Computational & Applied',6),('2023','Geometry & Topology',6),
('2024','Analysis & PDE',4),('2024','Computational & Applied',6),('2026','Analysis & PDE',5)}
for p in full:
    key = (p['year'], p['subject'], p['n'])
    if p['subject']=='Mathematical Physics': continue
    if key in targets:
        print('='*76)
        print(f"{p['year']} | {p['subject']} | {p['paper']} | Q{p['n']}")
        print(p['text'][:700].replace('\n',' '))
