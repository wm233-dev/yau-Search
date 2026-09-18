
# -*- coding: utf-8 -*-
"""For each exam topic, list candidate books from the merged index + matching TOC lines.
Writes topic_books.txt (condensed) for human/agent review."""
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
IDX = r".\scripts\lib_index.json"
OUT = r".\scripts\topic_books.txt"
recs = json.load(open(IDX, encoding='utf-8'))

# topic -> (book metadata regexes [any-of groups], toc regexes [any-of])
TOPICS = {
 "线性代数/矩阵": (["线性代数","高等代数","线性代数与矩阵","矩阵论","矩阵分析"], ["特征值","Jordan","若尔当","二次型","线性变换","矩阵的秩","不变量"]),
 "微分流形/形式": (["微分流形","流形","光滑流形","微分形式"], ["流形","切空间","微分形式","外微分","Stokes","德拉姆","de Rham","向量场"]),
 "群论": (["群论","抽象代数","近世代数","代数学引论"], ["Sylow","西罗","正规子群","商群","群作用","可解群","单群","置换群","同态"]),
 "概率论": (["概率论","概率"], ["大数定律","中心极限","鞅","条件期望","特征函数","独立","随机变量","收敛"]),
 "微分几何": (["微分几何","黎曼几何","曲线与曲面","黎曼"], ["曲率","测地线","联络","第一基本形式","第二基本形式","高斯","活动标架"]),
 "表示论": (["表示论","群表示"], ["表示","特征标","不可约","Schur","舒尔","诱导表示","李代数"]),
 "数论": (["数论","初等数论","解析数论"], ["同余","二次剩余","原根","素数","二次互反","连分数","pell","不定方程","fermat"]),
 "复分析": (["复变","复分析","单复变"], ["留数","解析函数","全纯","共形","调和函数","级数展开","儒歇","Rouch","最大模"]),
 "环与模": (["近世代数","抽象代数","环与模","交换代数","代数学"], ["理想","环","模","诺特","Noether","唯一分解","局部化","整闭"]),
 "Galois/域扩张": (["伽罗瓦","Galois","域论","抽象代数","近世代数"], ["Galois","伽罗瓦","域扩张","分裂域","可分","正规扩张","代数扩张"]),
 "数值分析": (["数值分析","数值计算","计算方法","数值方法"], ["插值","数值积分","迭代法","误差","收敛阶","Runge","Kutta","差分格式","稳定性"]),
 "数理统计": (["数理统计","统计学","统计推断"], ["估计","假设检验","充分统计量","极大似然","置信区间","贝叶斯","回归","方差分析"]),
 "代数拓扑": (["代数拓扑","拓扑学","同调","同伦"], ["同调群","同伦","基本群","覆叠","单纯","奇异同调","上同调","胞腔"]),
 "范畴/同调代数": (["同调代数","范畴论","范畴"], ["范畴","函子","Abel","导出函子","Ext","Tor","正合列","投射","内射"]),
 "代数几何": (["代数几何","代数曲线","交换代数"], ["簇","scheme","概形","射影","层","除子","Riemann-Roch","黎曼罗赫","椭圆曲线"]),
 "偏微分方程": (["偏微分方程","偏微分","数学物理方程","sobolev"], ["Sobolev","索伯列夫","弱解","椭圆","热方程","波动方程","极大值原理","特征值问题","边值问题"]),
 "实分析/测度": (["实变函数","实分析","测度","实变"], ["测度","可测","Lebesgue","勒贝格","积分","收敛定理","绝对连续","有界变差"]),
 "辛几何/力学": (["辛","哈密顿","经典力学","分析力学"], ["辛","Hamilton","哈密顿","Poisson","拉格朗日","正则","变分"]),
 "调和/位势": (["调和分析","位势","调和函数","傅里叶分析"], ["调和函数","位势","极大值原理","Poisson","Hardy","傅里叶","奇异积分"]),
 "微分方程(常微)": (["常微分方程","微分方程","动力系统"], ["常微分","解的存在唯一","稳定性","线性系统","Sturm","边值","相图","极限环"]),
 "泛函分析": (["泛函分析"], ["Hahn","Banach","希尔伯特","Hilbert","有界线性","紧算子","谱","对偶","弱收敛"]),
 "优化/线性规划": (["最优化","运筹","线性规划","优化","凸分析"], ["线性规划","单纯形","对偶","KKT","凸","梯度","变分不等式","最优控制"]),
 "Fourier/变换": (["傅里叶","Fourier","调和分析","小波"], ["傅里叶","Fourier","变换","卷积","级数","Parseval","采样"]),
 "数学物理/量子": (["数学物理","量子力学","量子"], ["量子","薛定谔","Schrodinger","算子","谱","路径积分","heisenberg","谐振子"]),
 "经典场论/相对论": (["相对论","场论","广义相对论","电动力学"], ["相对论","场论","拉格朗日密度","张量","Maxwell","麦克斯韦","Einstein","度规"]),
 "科学计算/大规模": (["数值代数","科学计算","矩阵计算","计算数学"], ["矩阵分解","迭代","稀疏","QR","LU","共轭梯度","特征值算法"]),
 "流体/连续介质": (["流体力学","连续介质","弹性力学"], ["Navier","Stokes","欧拉方程","激波","守恒律","不可压缩","湍流","边界层"]),
 "统计物理": (["统计物理","热力学","统计力学"], ["配分函数","熵","系综","Ising","伊辛","相变","玻色","费米"]),
 "纤维丛/示性类": (["纤维丛","示性类","丛论"], ["纤维丛","示性类","陈类","Chern","向量丛","主丛","联络"]),
}

def meta_blob(r):
    return " | ".join(str(r.get(k) or '') for k in ('title','fn','author','series'))

lines = []
for topic,(bkws,tocws) in TOPICS.items():
    lines.append("\n" + "="*100)
    lines.append(f"## TOPIC: {topic}")
    # metadata matches
    mb = [r for r in recs if any(re.search(k, meta_blob(r), re.I) for k in bkws)]
    def pg(r):
        try: return -int(r['pages'] or 0)
        except Exception: return 0
    mb.sort(key=lambda r: (-r['n_toc'], pg(r)))
    lines.append(f"-- metadata matches: {len(mb)}")
    for r in mb[:14]:
        lines.append(f"  [{r['id']}] {r['title']} | auth={r['author']} | series={r['series']} | pub={r['publisher']} {r['year']} | n_toc={r['n_toc']} | tl={r['text_layer']} | pg={r['pages']}")
        lines.append(f"        fn={r['fn']}")
    # toc matches
    tb = []
    for r in recs:
        if r['n_toc'] < 10: continue
        m = [l for l in r['toc'] if any(re.search(k, l, re.I) for k in tocws)]
        if m: tb.append((r, m))
    tb.sort(key=lambda x: -len(x[1]))
    lines.append(f"-- toc matches: {len(tb)}")
    for r, m in tb[:10]:
        lines.append(f"  [{r['id']}] {r['title']} (n_toc={r['n_toc']}) hits={len(m)}")
        for l in m[:18]:
            lines.append(f"        - {l}")

open(OUT,'w',encoding='utf-8').write("\n".join(lines))
print("wrote", OUT, len(lines), "lines")
