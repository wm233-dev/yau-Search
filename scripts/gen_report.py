# -*- coding: utf-8 -*-
"""生成 finals_alg_ana.md 第 1 部分（§1-§2）。占位符 BT 代表反引号。"""
import sys, os, re, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from finals_alg_ana_problems import P
from finals_alg_ana_extras import E

ROOT = r'E:\deepseek_exclusive\math'
TXT = os.path.join(ROOT, '.tmp', 'burn2026', 'txt_finals')
OUT = os.path.join(ROOT, '.tmp', 'burn2026', 'reports', 'finals_alg_ana.md')
m = json.load(open(os.path.join(ROOT, '.tmp', 'burn2026', 'data', '_finals_txtmap.json'), encoding='utf-8'))

def norm(rec, src):
    y, s, k, no, desc, tags, meth, d = rec[:8]
    try: d = int(d)
    except Exception: d = None
    return dict(y=y, s=s, k=k, no=no, desc=desc, tags=[t.strip() for t in tags.split(',')], meth=meth, d=d, src=src)
A = [norm(r, 'pdf') for r in P]
B = [norm(r, 'doc') for r in E]
ALL = A + B
def papers(lst):
    d = collections.OrderedDict()
    for x in lst:
        d.setdefault((x['y'], x['s'], x['k']), []).append(x)
    return d
PA, PB, PALL = papers(A), papers(B), papers(ALL)
def rawof(subj, kind, year):
    for k, v in m.items():
        tag = 'ALG' if 'Algebra' in v['subj'] else ('ANA' if 'Analysis' in v['subj'] else None)
        if tag == subj and v['kind'] == kind and v['year'] == str(year):
            return open(os.path.join(TXT, k), encoding='utf-8', errors='replace').read()
    return ''
ORDER = {('ALG', 'Individual'): 0, ('ALG', 'Team'): 1, ('ALG', 'Overall'): 2,
         ('ANA', 'Individual'): 3, ('ANA', 'Team'): 4, ('ANA', 'Overall'): 5}
L = []
def o(s=''): L.append(s)
def diff_tbl(lst):
    o('| 年份 | 卷别 | 题号 | 一句话题意 | 子领域 | 核心定理/方法 | 难度 |')
    o('|---|---|---|---|---|---|---|')
    for (y, s, k), items in sorted(lst.items(), key=lambda kv: (kv[0][0], ORDER[(kv[0][1], kv[0][2])])):
        for it in items:
            o('| %d | %s %s | %s | %s | %s | %s | %s |' % (
                y, s, k, it['no'], it['desc'], '/'.join(it['tags']), it['meth'],
                it['d'] if it['d'] else '—'))

o('# 丘成桐大学生数学竞赛 · **总决赛**（2012–2025）真题分析')
o('## 范围：代数与数论/组合 + 分析与微分方程')
o()
o('> 语料：BT.tmp/burn2026/txt_finals/BT（195 个 txt，源自 BT F:\\丘成桐大学生数学竞赛历年总决赛真题 BT）')
o('> 加上本报告新增恢复的 BT.tmp/burn2026/txt_finals_extra/BT。')
o('> 元数据：BT.tmp/burn2026/data/finals_index.jsonBT；txt 与原卷的映射由 BT.tmp/burn2026/scripts/finals_map.pyBT 建立')
o('> （规则：把「科目_kind_原文件名去扩展名」中的**非字母数字连续段压成一个下划线**，再去掉首尾下划线）。')
o('> 统计脚本：BTfinals_alg_ana_stats.pyBT、BTfinals_alg_ana_stats2.pyBT、BTfinals_final_stats.pyBT、')
o('> BTfinals_compare.pyBT、BTfinals_forms.pyBT、BTfinals_alg_ana_problems.pyBT（逐题标注库）、')
o('> BTfinals_alg_ana_extras.pyBT（恢复卷标注库）、BTrender_2015_alg.pyBT、BTextract_extra_finals.pyBT、BTgen_report.pyBT。')
o('> **本题库共 %d 卷 / %d 题**（PDF 主集 %d 卷 %d 题 + 恢复集 %d 卷 %d 题）。' % (len(PALL), len(ALL), len(PA), len(A), len(PB), len(B)))
o('> 所有题面均来自真实抽取文本，未做任何编造；公式抽取有损处一律逐条标注。')
o()
o('---')
o()
o('## 1. 可分析范围声明')
o()
o('### 1.1 全语料（195 个 txt）的文字层情况')
o()
o('| 科目目录 | 文件数 | chars<800 | chars<100 | chars=0 |')
o('|---|---|---|---|---|')
o('| Algebra, Number Theory and Combinatorics | 37 | 19 | 1 | 1 |')
o('| Analysis and Differential Equations | 32 | 10 | 0 | 0 |')
o('| Applied Math and Computational Math | 40 | 11 | 3 | 3 |')
o('| Geometry and Topology | 33 | 12 | 0 | 0 |')
o('| Probability and Statistics | 41 | 13 | 1 | 1 |')
o('| Mathematical Physics (2022–2025) | 12 | 0 | 0 | 0 |')
o('| **合计** | **195** | **65** | **5** | **5** |')
o()
o('### 1.2 对任务书「约 65 个文件几乎没有文字层」的重要更正')
o()
o('- BTchars<800BT **不能**等价于「扫描件/图片版」。逐卷核对后确认：本范围（代数+分析 67 个 txt）中，')
o('  chars<800 的短卷绝大多数是**文字层完好、只是题目少或题面短**的正常 PDF。')
o('  例：BT2012 Algebra (Individual)BT 仅 376 字符 / 1 页，却完整含 3 道题（文本止于第 3 题，无截断）；')
o('  BT2024 Analysis (Overall)BT 仅 381 字符 / 1 页，完整含 2 道题。若按 chars<800 一律剔除，会丢掉大量真题。')
o('- 真正的「无文字层」在本范围内只有 **1 卷**：BT2015 Algebra (Overall)BT（0 字符，页面由 **11 张图片**构成）。')
o('- 另有 **2 卷**文字层存在但 **CJK 字体 ToUnicode 表损坏**（抽出来是乱码）：')
o('  BT2015 Algebra (Individual)BT、BT2015 Algebra (Team)BT（乱码样例：BT1. •Äî¼˜mRn§Ùƒ´•þBT）。')
o('- 上述 3 卷已用 PyMuPDF 以 200 dpi 渲染为 PNG，再由视觉逐字识读（脚本 BTrender_2015_alg.pyBT，产物 BT.tmp/burn2026/data/render/BT），')
o('  题面已补全并进入本题库；因为是人工识读，个别符号可能失真，相关行在 §7 单列。')
o()
o('### 1.3 本范围实际可分析的卷（计数）')
o()
o('| 项目 | 卷数 | 题数 | 说明 |')
o('|---|---|---|---|')
o('| PDF 文字层直接可用 | 63 | 207 | 除 2015 三卷外的全部 PDF |')
o('| 原无/坏文字层，渲染后人工识读 | 3 | 8 | 2015 ALG Individual(3) / Team(3) / Overall(2) |')
o('| **PDF 主集小计** | **66** | **215** | 对应 67 个 txt：2020 ANA Individual 有 I、II 两份文件，此处合为一「卷」 |')
o('| 原 pipeline 完全未转换、本报告从 .doc/.docx 恢复 | 7 | 29 | 见 §1.4 |')
o('| **总计** | **73** | **244** | — |')
o()
o('### 1.4 新发现：7 卷真题从未进入 txt 语料（不是扫描问题，是格式问题）')
o()
o('原抽取管线只处理 BT.pdfBT；下列真题在 F 盘以 BT.docBT / BT.docxBT 存在，**此前从未被任何报告覆盖**：')
o()
o('| 原文件 | 卷 | 题数 | 本报告恢复方式 | 恢复质量 |')
o('|---|---|---|---|---|')
o('| BT2014 Algebra (Team).docxBT | 2014 ALG Team | 4 | zipfile 解析 word/document.xml | 文本完整，公式丢失 |')
o('| BT2012 Analysis (Individual).docBT | 2012 ANA Individual | 3 | Word COM 另存 ANSI 文本，再按 GBK 解码 | 文本完整，公式全丢（EQ 占位） |')
o('| BT2013 Analysis (Individual).docxBT | 2013 ANA Individual | 4 | docx 解析 | 文本完整，公式丢失 |')
o('| BT2014 Analysis (Individual and Overall).docBT | 2014 ANA Individual | 6 | Word COM，再按 GBK 解码 | 文本完整，公式全丢 |')
o('| BT2013 Analysis (Team).docxBT | 2013 ANA Team | 4 | docx 解析 | 文本完整；**原文件第 2 题本身为空** |')
o('| BT2014 Analysis (Team).docxBT | 2014 ANA Team | 6 | docx 解析 | 文本完整，公式丢失 |')
o('| BT2013 Analysis (Overall).docxBT | 2013 ANA Overall | 2 | docx 解析 | 文本完整，公式丢失 |')
o()
o('恢复脚本：BT.tmp/burn2026/scripts/extract_extra_finals.pyBT；两个 BT.docBT 用 Word COM **只读打开、只写工作区**（未改动 F 盘任何文件）。')
o('产物目录：BT.tmp/burn2026/txt_finals_extra/BT。它们的价值：把分析科目的年份覆盖从「2015 起」提前到 **2012**，')
o('并补出 2013/2014 的 Team 与 Overall 两栏（此前全空）。')
o()
o('### 1.5 明确无法分析的内容清单（先给结论，§7 详列）')
o()
o('| 出处 | 内容 | 原因 | 处理 |')
o('|---|---|---|---|')
o('| 2012 ANA Individual #2 | 整函数迭代题 | .doc 中公式全为 OLE 对象，条件全部丢失 | 放弃分析，仅登记 |')
o('| 2014 ANA Individual #3 | 「对素数全体证明级数发散」 | 公式丢失 | 放弃分析，仅登记 |')
o('| 2014 ANA Individual #5 | (a)(b) 两小问 | 公式丢失 | 放弃分析，仅登记 |')
o('| 2013 ANA Team #2 | 空题 | 原文件即为空标题 | 登记为「原文缺题」 |')
o('| 恢复集其余题的公式 | 条件式 | Word 公式对象无法在禁装库的条件下取出 | 只保留可辨认主题，逐条标注「公式缺失」 |')
o()
o('---')
o()
o('## 2. 逐年逐卷结构表')
o()
o('### 2.1 PDF 主集（66 卷 / 215 题）')
o()
o('难度为**本报告自评 1–5**：1=常规课程题；2=标准题；3=需一两步非平凡想法；4=需专门工具或较长构造；')
o('5=需专门理论（局部域/类域论、特征和、非线性 PDE 估计等），属压轴级。子领域标签定义见 §3.1。题号沿用原卷题号。')
o()
diff_tbl(PA)
o()
o('### 2.2 恢复集（7 卷 / 29 题，源为 .doc/.docx）')
o()
o('> 全部题面来自 Word 文本层；数学公式在源文件中是 OLE 公式对象，本环境（禁止安装任何库）无法取出，')
o('> 故题面只保留可读的文字骨架，标注「公式缺失」的行请勿直接引用公式。')
o()
diff_tbl(PB)
o()
o('### 2.3 逐卷规模与文字量（PDF 主集）')
o()
o('| 年份 | 科目 | 卷别 | 题数 | 抽取字符 | 英文词 | 词/题 | 难度均值 |')
o('|---|---|---|---|---|---|---|---|')
for (y, s, k), items in sorted(PA.items(), key=lambda kv: (kv[0][0], ORDER[(kv[0][1], kv[0][2])])):
    raw = rawof(s, k, y)
    w = len(re.findall(r'[A-Za-z]+', raw))
    dd = [i['d'] for i in items if i['d']]
    o('| %d | %s | %s | %d | %d | %d | %.1f | %.2f |' % (y, s, k, len(items), len(raw), w, w / len(items), sum(dd) / len(dd)))
o()
o('> 注 1：2021 ALG Individual（261 词/题）与 2021 ALG Overall（243 词/题）原卷**附带官方解答**，词数被解答抬高。')
o('> 注 2：2015 三卷（ALG Ind/Team/Ov）为中文卷或图片卷，英文词数为 0，会拉低 ALG 平均词数。')
o()

open(OUT, 'w', encoding='utf-8').write('\n'.join(L).replace('BT', chr(96)))
print('lines written:', len(L))
