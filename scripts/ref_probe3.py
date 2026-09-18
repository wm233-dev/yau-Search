
import os, sys
root = r"F:\丘成桐大学生数学竞赛历年笔试真题"
print("exists:", os.path.isdir(root))
if os.path.isdir(root):
    for d in sorted(os.listdir(root)):
        print(d)
