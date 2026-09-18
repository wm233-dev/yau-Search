
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
args = sys.argv[1:]
if args and os.path.isfile(args[0]):
    F = args[0]; want = args[1:]
else:
    F = r".\scripts\topic_books_compact.txt"; want = args
txt = open(F, encoding='utf-8').read()
parts = re.split(r'^[=#]{80,}\s*$', txt, flags=re.M)
for s in parts:
    lines = s.strip().split("\n")
    if not lines or not lines[0].startswith("##"): continue
    head = lines[0]
    if any(w in head for w in want):
        print("="*90); print(s.strip())
