# -*- coding: utf-8 -*-
"""One-off patch: clean control chars from templates, add markers, fix builder bugs."""
import io, os, re

SCR = r'E:\deepseek_exclusive\math\.tmp\burn2026\scripts'
BT = chr(96)

# ---- 1. clean control characters out of the tail template
p = os.path.join(SCR, '_report_tpl_tail.md')
t = io.open(p, encoding='utf-8', errors='replace').read()
before = len(t)
t = ''.join(c for c in t if ord(c) >= 32 or c in '\n\r\t')
t = t.replace('**\u9898\u9762\uff08\u539f\u6587\uff0c\u62bd\u53d6\u6587\u672c\u5df2\u6309\u6570\u5b66\u8bed\u4e49\u8fd8\u539f \n  \u7b49\u9519\u6620\u5c04\u7b26\u53f7\uff09**',
              '**\u9898\u9762\uff08\u539f\u6587\uff1bPDF \u6587\u672c\u5c42\u628a\u6570\u5b66\u5b57\u4f53\u9519\u6620\u5c04\uff0c\u5df2\u6309\u6570\u5b66\u8bed\u4e49\u8fd8\u539f\uff09**')
# marker for the theorem-citation number in section 8
t = t.replace('14. \u70b9\u540d\u5b9a\u7406\u7387\uff1a\u51b3\u8d5b\u9898\u9762 **12.1%**\uff0820/165\uff09',
              '14. \u70b9\u540d\u5b9a\u7406\u7387\uff1a\u51b3\u8d5b\u9898\u9762 **@@THEO_PCT@@%**\uff08@@THEO_N@@/@@THEO_D@@\uff09')
io.open(p, 'w', encoding='utf-8').write(t)
print('tail cleaned:', before, '->', len(t))
print('marker present:', '@@THEO_PCT@@' in t)

# ---- 2. fix builder bugs
b = os.path.join(SCR, 'build_finals_geo_prob_report.py')
src = io.open(b, encoding='utf-8').read()
assert "n_pG = sum(1 for s in pre_gp if s == 'G')" in src
src = src.replace("n_pG = sum(1 for s in pre_gp if s == 'G'); n_pP = sum(1 for s in pre_gp if s == 'P')",
                  "n_pG = sum(1 for x in pre_gp if x[1] == 'G'); n_pP = sum(1 for x in pre_gp if x[1] == 'P')")
# escape pipes inside table cells
src = src.replace("r['gist'].replace('|', '/'), r['topic'], r['method'].replace('|', '/')",
                  "r['gist'].replace('|', chr(92) + '|'), r['topic'], r['method'].replace('|', chr(92) + '|')")
# extra markers: presence note, tag base, tag reading, theorem rate
extra = '''
# ---------- 12. extra markers
M['@@PRESENCE_NOTE@@'] = ('**合卷说明**：2013 \u51e0\u4f55\u7684 Individual \u4e0e Team \u5408\u5e76\u4e8e\u540c\u4e00\u4efd PDF'
  '\uff08\u7d22\u5f15\u4e2d\u767b\u8bb0\u4e3a Individual\uff09\uff0c2022 \u51e0\u4f55\u7684 Individual \u4e0e Overall \u4e5f\u5408\u5e76\u4e8e\u540c\u4e00\u4efd PDF\uff0c'
  '2017 \u51e0\u4f55\u7684 Individual \u6587\u4ef6\u5b9e\u9645\u5305\u542b Individual + Team + Overall \u4e09\u8282\u3002\u56e0\u6b64\u77e9\u9635\u4e2d 2013 \u51e0\u4f55\u7684 Team \u683c\u663e\u793a\u4e3a\u2014'
  '\uff08\u5b9e\u9645\u5728 Individual \u6587\u4ef6\u5185\uff0c\u5df2\u8ba1 4 \u9898\uff09\u3002')
M['@@TAGBASE@@'] = ('\u5355\u4f4d\uff1d\u547d\u4e2d\u8be5\u6807\u7b7e\u7684**\u9898\u76ee\u6570**\u3002\u603b\u51b3\u8d5b\u7528\u53ef\u81ea\u52a8\u5207\u5206\u7684 %d \u9898\u9898\u9762'
  '\uff08\u51e0\u4f55 %d + \u6982\u7387 %d\uff1b\u5207\u5206\u9898\u6570\u4e0e\u539f\u5377\u9898\u6570\u4e00\u81f4\u7684\u5377\u5b50\uff0c\u5df2\u542b\u62a2\u6551\u5377\uff09\uff1b'
  '\u521d\u8d5b\u7528 %s \u4e2d\u51e0\u4f55/\u6982\u7387\u4e24\u79d1\u7684 %d \u9898\u3002'
  ) % (n_fG + n_fP, n_fG, n_fP, BT + 'data/problems_full.json' + BT, n_pG + n_pP)
_dg_f = 100 * fG['\u5fae\u5206\u51e0\u4f55'] / max(1, n_fG); _dg_p = 100 * pG['\u5fae\u5206\u51e0\u4f55'] / max(1, n_pG)
_at_f = 100 * fG['\u4ee3\u6570\u62d3\u6251'] / max(1, n_fG); _at_p = 100 * pG['\u4ee3\u6570\u62d3\u6251'] / max(1, n_pG)
_fb_f = 100 * fG['\u7ea4\u7ef4\u4e1b/\u793a\u6027\u7c7b'] / max(1, n_fG); _fb_p = 100 * pG['\u7ea4\u7ef4\u4e1a/\u793a\u6027\u7c7b'] if False else 100 * pG['\u7ea4\u7ef4\u4e1b/\u793a\u6027\u7c7b'] / max(1, n_pG)
M['@@TAGREAD@@'] = ('**\u8bfb\u6cd5**\uff1a%s\u5fae\u5206\u51e0\u4f55%s\uff08curvature / geodesic / Riemannian / mean curvature\u2026\uff09\u5728\u603b\u51b3\u8d5b\u51e0\u4f55\u9898\u4e2d\u547d\u4e2d %d/%d = %.0f%%\uff0c'
  '\u521d\u8d5b\u51e0\u4f55\u9898 %d/%d = %.0f%%\uff1b%s\u4ee3\u6570\u62d3\u6251%s \u51b3\u8d5b %.0f%% vs \u521d\u8d5b %.0f%%\uff1b%s\u7ea4\u7ef4\u4e1b/\u793a\u6027\u7c7b%s \u51b3\u8d5b %.0f%% vs \u521d\u8d5b %.0f%%\u3002'
  '\u2192 \u51e0\u4f55\u7684\u201c\u8003\u70b9\u9aa8\u67b6\u201d\u4e24\u8fb9\u63a5\u8fd1\uff0c\u5dee\u5f02\u4e3b\u8981\u5728\u201c\u62bd\u8c61\u4ee3\u6570\u62d3\u6251\u201d\u4e0e\u201c\u4e1b\u4e0e\u793a\u6027\u7c7b\u201d\u7684\u6bd4\u91cd\u4e0a\u3002'
  ) % (BT, BT, fG['\u5fae\u5206\u51e0\u4f55'], n_fG, _dg_f, pG['\u5fae\u5206\u51e0\u4f55'], n_pG, _dg_p, BT, BT, _at_f, _at_p, BT, BT, _fb_f, _fb_p)
THEO_RX = re.compile('|'.join(re.escape(x) for x in ['bonnet', 'myers', 'synge', 'cartan', 'hadamard', 'hopf',
    'poincar', 'crofton', 'brouwer', 'lefschetz', 'hilbert', 'gauss-bonnet', 'stokes', 'mayer-vietoris',
    'kunneth', 'sard', 'whitney', 'nash', 'cauchy', 'radon-nikodym', 'cram\u00e9r-rao', 'cramer-rao',
    'neyman-pearson', 'kolmogorov', 'wald', 'fatou', 'jensen', 'h\u00f6lder', 'minkowski', 'doob',
    'birkhoff', 'alexander', 'noether', 'schur', 'banach', 'hahn-banach', 'parseval', 'jacobi', 'liouville',
    'maximum principle', 'reilly', 'simons', 'alexandrov', 'willmore', 'morse', 'euler characteristic',
    'r\u00e9nyi', 'stein', 'hodge']), re.I)
_thn = sum(1 for b in fin_bodies if THEO_RX.search(b))
M['@@THEO_N@@'] = str(_thn); M['@@THEO_D@@'] = str(len(fin_bodies))
M['@@THEO_PCT@@'] = '%.1f' % (100.0 * _thn / max(1, len(fin_bodies)))
'''
src = src.replace("# ---------- assemble", extra + "\n# ---------- assemble")
io.open(b, 'w', encoding='utf-8').write(src)
print('builder patched; length', len(src))
