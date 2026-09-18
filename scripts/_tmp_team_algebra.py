
import json,re,sys,os
sys.stdout.reconfigure(encoding='utf-8')
D=r'.tmp/burn2026/txt'
def load(f):
    return open(os.path.join(D,f),'rb').read().decode('utf-8','replace')
team_files={'2013':'2013_TeamProblems2013.txt','2016':'2016_2016_team.txt','2017':'2017_2017_team.txt','2018':'2018_2018_team.txt'}
out={}
tot={}
for y,f in team_files.items():
    t=load(f); lines=t.splitlines()
    idx=[i for i,l in enumerate(lines) if re.match(r'^\s*Algebra and Number Theory\s*$',l)]
    i0=idx[0]
    i1=len(lines)
    for j in range(i0+3,len(lines)):
        if 'College Student Mathematics Contests' in lines[j]:
            i1=j; break
    seg='\n'.join(lines[i0:i1])
    probs=[]
    if y=='2013':
        parts=re.split(r'(?m)^\s*(\d)\.\s', seg)
        probs=[(parts[k],parts[k+1]) for k in range(1,len(parts)-1,2)]
    else:
        parts=re.split(r'(?m)^Problem\s+(\d)\s*\(', seg)
        probs=[(parts[k],parts[k+1]) for k in range(1,len(parts)-1,2)]
    print('=====',y,'problems',[p[0] for p in probs])
    for num,body in probs:
        suba=len(re.findall(r'\(\s*[a-e]\s*\)\s*\(?\s*\d*\s*(?:pt|points)',body))
        suball=len(re.findall(r'\(\s*(?:[a-e]|\d)\s*\)',body))
        numsplit=len(re.findall(r'(?m)^\s*\d\.\d',body))
        print('  Q%s chars=%d sub_scored=%d sub_all=%d nested=%d'%(num,len(body.strip()),suba,suball,numsplit))
        out.setdefault(y,[]).append(dict(num=int(num),chars=len(body.strip()),suba=suba,suball=suball))
json.dump(out,open(r'.tmp/burn2026/scripts/team_algebra_metrics.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
