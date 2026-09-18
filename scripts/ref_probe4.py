
import os
root = r"F:\丘成桐大学生数学竞赛历年笔试真题"
for y in ["2010","2011","2013","2014","2015","2017","2018","2020","2025"]:
    d = os.path.join(root,y)
    print("###", y)
    for f in sorted(os.listdir(d)):
        print("   ", f)
