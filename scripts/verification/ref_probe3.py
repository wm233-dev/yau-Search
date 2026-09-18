
import os, sys
root = r"sources/prelim"
print("exists:", os.path.isdir(root))
if os.path.isdir(root):
    for d in sorted(os.listdir(root)):
        print(d)
