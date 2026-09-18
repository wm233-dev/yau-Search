import sys, io, unicodedata
p = sys.argv[1]
b = open(p,'rb').read()
s = b.decode('utf-8', errors='replace')
out = []
for ch in s:
    o = ord(ch)
    if o < 32 and ch not in '\n\r\t':
        out.append('[#%02X]' % o)
    else:
        out.append(ch)
print(''.join(out))
