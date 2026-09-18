
# -*- coding: utf-8 -*-
"""Tight topic->book search. Prints top books per topic (dedup by normalized title)."""
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
IDX = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\lib_index.json"
recs = json.load(open(IDX, encoding='utf-8'))

PLAN = [
 ("线性代数/矩阵", [r"高等代数|线性代数|代数学引论|矩阵论|矩阵分析"], ["特征值","Jordan|若当","二次型","线性变换"]),
 ("微分流形/形式", [r"微分流形|流形|微分形式|李群"], ["微分流形","外微分","Stokes","切空间"]),
 ("群论",          [r"群论|抽象代数|近世代数|有限群|代数学引论|代数学$"], ["Sylow|西罗|西洛","正规子群","置换群","可解"]),
 ("概率论",        [r"概率论"], ["大数定律","中心极限","鞅","特征函数"]),
 ("微分几何",      [r"微分几何|黎曼几何"], ["曲率","测地线","联络","第一基本形式"]),
 ("表示论",        [r"表示论|群表示|李代数|线性表示"], ["特征标","不可约表示","诱导表示","Schur"]),
 ("数论",          [r"数论"], ["同余","二次剩余|互反","原根","素"]),
 ("复分析",        [r"复变|复分析|单复变"], ["留数","解析函数|全纯","共形","最大模"]),
 ("环与模",        [r"近世代数|抽象代数|交换代数|环与模"], ["理想","模$|模的","诺特","局部化"]),
 ("Galois/域扩张", [r"伽罗瓦|Galois|域论|抽象代数|近世代数"], ["伽罗瓦|Galois","域扩张","分裂域","有限域"]),
 ("数值分析",      [r"数值分析|数值计算|计算方法|数值方法|数值逼近"], ["插值","数值积分","Runge|Kutta","收敛阶"]),
 ("数理统计",      [r"数理统计|统计学|统计推断|统计"], ["假设检验","极大似然|最大似然","充分统计","回归"]),
 ("代数拓扑",      [r"代数拓扑|拓扑学|同调"], ["同调群","基本群","覆叠|覆盖","同伦"]),
 ("范畴/同调代数", [r"同调代数|范畴"], ["函子","Ext|Tor","正合","范畴"]),
 ("代数几何",      [r"代数几何|代数曲线"], ["簇|代数簇","射影","层","椭圆曲线|Riemann-Roch"]),
 ("偏微分方程",    [r"偏微分方程|偏微分|数学物理方程|方程"], ["Sobolev|索伯列夫","弱解","椭圆","极大值原理"]),
 ("实分析/测度",   [r"实变函数|实分析|测度|实变"], ["测度","Lebesgue|勒贝格","可测","收敛定理"]),
 ("辛几何/力学",   [r"辛|哈密顿|经典力学|分析力学|力学"], ["哈密顿|Hamilton","辛","拉格朗日|Lagrange","泊松|Poisson"]),
 ("调和/位势",     [r"调和分析|位势|调和函数|傅里叶分析"], ["调和函数","位势","极大值原理","奇异积分"]),
 ("微分方程(常微)",[r"常微分方程|微分方程|动力系统"], ["存在唯一|解的存在","稳定性","边值","极限环"]),
 ("泛函分析",      [r"泛函分析"], ["Hahn|哈恩","Banach|巴拿赫","紧算子","谱"]),
 ("优化/线性规划", [r"最优化|运筹|线性规划|优化|凸分析|变分法|最优"], ["线性规划","单纯形","凸","变分"]),
 ("Fourier/变换",  [r"傅里叶|Fourier|小波"], ["傅里叶|Fourier","卷积","变换"]),
 ("数学物理/量子", [r"数学物理|量子"], ["薛定谔|Schr","量子","谐振子","谱"]),
 ("经典场论/相对论",[r"相对论|场论|电动力学"], ["相对论","张量","Maxwell|麦克斯韦","度规"]),
 ("科学计算/大规模",[r"数值代数|科学计算|矩阵计算|计算数学"], ["矩阵分解","迭代","稀疏|共轭梯度","QR|LU"]),
 ("流体/连续介质", [r"流体|连续介质|弹性"], ["Navier|Stokes","守恒律|激波","不可压缩|湍流","边界层"]),
 ("统计物理",      [r"统计物理|热力学|统计力学"], ["配分函数","系综","相变","熵"]),
 ("纤维丛/示性类", [r"纤维丛|示性类|向量丛"], ["纤维丛","示性类|陈类|Chern","向量丛|主丛","联络"]),
]

OUTF = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\topic_books2.txt"
_buf = []
def P(s=""):
    _buf.append(str(s))

def meta_blob(r):
    return " | ".join(str(r.get(k) or '') for k in ('title','fn','author','series'))
def sc(r): return (1 if r['text_layer'] else 0)*10000 + r['n_toc']

for topic, bkws, tocws in PLAN:
    P("\n" + "#"*80)
    P(f"## {topic}")
    mb = {}
    for r in recs:
        b = meta_blob(r)
        if any(re.search(k, b, re.I) for k in bkws):
            t = re.sub(r'\s+','', r['title'])
            if t not in mb or sc(r) > sc(mb[t]): mb[t] = r
    mbl = sorted(mb.values(), key=lambda r: -sc(r))
    P(f"-- BOOKS ({len(mbl)}):")
    for r in mbl[:9]:
        P(f"  [{r['id']}] {r['title']} | {r['author']} | {r['series']} | {r['publisher']} {r['year']} | toc={r['n_toc']} tl={r['text_layer']} pg={r['pages']}")
        P(f"        fn={r['fn']}")
    tb = {}
    for r in recs:
        if r['n_toc'] < 15: continue
        m = [l for l in r['toc'] if any(re.search(k, l, re.I) for k in tocws)]
        if m:
            t = re.sub(r'\s+','', r['title'])
            if t not in tb or len(m) > len(tb[t][1]): tb[t] = (r, m)
    tbl = sorted(tb.values(), key=lambda x: -len(x[1]))
    P(f"-- TOC BOOKS ({len(tbl)}):")
    for r, m in tbl[:6]:
        P(f"  [{r['id']}] {r['title']} (toc={r['n_toc']}, hits={len(m)})")
        for l in m[:12]:
            P(f"      - {l}")

open(OUTF,'w',encoding='utf-8').write("\n".join(_buf))
print("wrote", OUTF, len(_buf))
