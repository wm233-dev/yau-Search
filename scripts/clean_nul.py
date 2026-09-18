
import glob, os, re
src = r'E:\deepseek_exclusive\math\.tmp\burn2026\txt'
dst = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_clean'
os.makedirs(dst, exist_ok=True)
fs = sorted(glob.glob(os.path.join(src, '201[678]_*.txt')))
for f in fs:
    raw = open(f, 'rb').read()
    t = raw.replace(b'\x00', b'').decode('utf-8', errors='replace')
    t = t.replace('\ufffd', '')
    out = os.path.join(dst, os.path.basename(f))
    open(out, 'w', encoding='utf-8').write(t)
    print(os.path.basename(f), '->', len(t))
