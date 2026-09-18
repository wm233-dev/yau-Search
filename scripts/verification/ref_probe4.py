
import os
root = r"sources/prelim"
for y in ["2010","2011","2013","2014","2015","2017","2018","2020","2025"]:
    d = os.path.join(root,y)
    print("###", y)
    for f in sorted(os.listdir(d)):
        print("   ", f)
