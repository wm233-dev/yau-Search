
import json, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"sources/book_research"
p = BASE + r"data\subject_classification.json"
with open(p,'r',encoding='utf-8') as f: d=json.load(f)
print("type", type(d).__name__)
if isinstance(d,dict):
    print("keys", list(d.keys())[:20])
    for k in list(d.keys())[:6]:
        v=d[k]
        print(" ",k,type(v).__name__,(len(v) if hasattr(v,'__len__') else v if not isinstance(v,(list,dict)) else ''))
    for k in list(d.keys()):
        v=d[k]
        if isinstance(v,list) and v and isinstance(v[0],dict):
            print("### ",k)
            print(json.dumps(v[0],ensure_ascii=False)[:1500])
            print("n=",len(v))
            break
        if isinstance(v,dict) and v:
            kk=list(v.keys())[:3]
            print("### dict",k, kk)
            print(json.dumps({x:v[x] for x in kk},ensure_ascii=False)[:1200])
            break
