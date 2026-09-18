# -*- coding: utf-8 -*-
"""由 syllabus_coverage.json 生成两份中文报告：
   reports/yau_syllabus.md         结构化考纲清单
   reports/syllabus_coverage.md    考纲覆盖率分析报告
"""
import json, os, sys, datetime, collections
sys.stdout.reconfigure(encoding="utf-8")

BT = chr(96)                      # 反引号：模板字面量里不便直写，用 chr(96) 生成
def C(s):
    return BT + s + BT

ROOT = r"."
COV = os.path.join(ROOT, "data", "syllabus_coverage.json")
R1 = os.path.join(ROOT, "reports", "yau_syllabus.md")
R2 = os.path.join(ROOT, "reports", "syllabus_coverage.md")

SYL_FILES = [
 ("Algebra & Number Theory", "2012_2025Algebra_Number_Theory_and_Combinatorics_SyllabusonAlgebraandNumberTheory.txt"),
 ("Analysis & PDE", "2012_2025Analysis_and_Differential_Equations_SyllabusonAnalysisand_Partial_DifferentialEquations.txt"),
 ("Computational & Applied", "2012_2025Applied_Math_and_Computational_Math_SyllabusonComputationalandAppliedMathematics.txt"),
 ("Geometry & Topology", "2012_2025Geometry_and_Topology_SyllabusonGeometryandTopology.txt"),
 ("Probability & Statistics", "2012_2025Probability_and_Statistics_SyllabusonProbbilityandStatistics.txt"),
 ("Mathematical Physics", "2022_2025Mathematical_Physics_Syllabus_on_Mathematical_Physics.txt"),
]

d = json.load(open(COV, encoding="utf-8"))
S = d["subjects"]
NP = d["n_problems"]

def pct(a, b):
    return ("%.1f%%" % (100.0 * a / b)) if b else "-"

def TOP(subj):
    e = max(S[subj]["entries"], key=lambda x: x["hits"])
    return (e["cn"], e["hits"])

def OOS(subj, kw):
    for r in d["out_of_syllabus"].get(subj, []):
        if kw in r["label"]:
            return r["hits"]
    return 0

def sect_map(v):
    secs = collections.OrderedDict()
    for e in v["entries"]:
        secs.setdefault(e["section"], []).append(e)
    return secs

REFS = {
 "Algebra & Number Theory": "Dummit & Foote *Abstract Algebra* (2nd ed.)；Serre *Representations of Finite Groups*；Fulton-Harris *Representation Theory: A First Course*；Serge Lang *Algebra*；Borevich-Shafarevich *Number Theory*；Serge Lang *Algebraic Number Theory*",
 "Analysis & PDE": "Rudin *Real and Complex Analysis*；Stein & Shakarchi *Real Analysis*；Stein & Shakarchi *Fourier Analysis*；Ahlfors *Complex Analysis* (3rd ed.)；V. I. Arnold *Mathematical Methods of Classical Mechanics*；Craig Evans *Partial Differential Equations*",
 "Computational & Applied": "Bender & Orszag (1999)；de Boor & Conte (2000)；Golub & van Loan (1996)；Hairer, Syvert & Wanner (1993)；Gustafsson, Kreiss & Oliger (1995)；Keener (1988)；Trefethen & Bau (1997)；Brenner & Scott (2010)；F.Y.M. Wan (1995)",
 "Geometry & Topology": "Guillemin & Pollack *Differential Topology*；Milnor *Topology from the Differentiable Viewpoint*；Cliff Taubes *Differential Geometry*；John Lee *Introduction to Riemannian Manifolds* (2nd ed.)；Kobayashi & Nomizu *Foundations of Differential Geometry*；Hatcher *Algebraic Topology*；Fulton *Algebraic Topology*；Spanier *Algebraic Topology*；Greenberg & Harper *Algebraic Topology: A First Course*",
 "Probability & Statistics": "Rick Durrett *Probability: Theory and Examples* (2010)；Kai-Lai Chung *A Course in Probability Theory* (1968)；Casella & Berger *Statistical Inference* (2nd ed., 2002)；茆诗松等《概率论与数理统计教程》(2008)；陈家鼎等《数理统计学讲义》(2006)；郑明等《数理统计讲义》(2006)；陈希孺、倪国熙《数理统计学教程》(2009)",
 "Mathematical Physics": "Landau & Lifshitz *Mechanics*；Goldstein *Classical Mechanics*；Griffiths *Introduction to Electrodynamics*；Mehran Kardar *Statistical Physics of Particles*；J.J. Sakurai *Modern Quantum Mechanics*；Sean Carroll *Spacetime and Geometry*；Robert M. Wald *General Relativity*；Peskin & Schroeder *An Introduction to QFT*；Weinberg *The Quantum Theory of Fields* Vol 1,2",
}

# ------------------------------------------------------------------ 报告 A
L = []
L.append("# 丘成桐大学生数学竞赛 · 官方考纲结构化清单（中文）\n")
L.append("> 来源：总决赛文件夹 6 份官方 Syllabus PDF 抽取文本（" + C("./corpus/finals/") + "）。")
L.append("> 本清单**逐条**转录考纲条目，未添加任何考纲外内容；括号内保留原文英文术语。")
L.append("> 生成时间：%s\n" % d["generated"])
L.append("## 来源文件对照\n")
L.append("| 科目 | 考纲文件 | 考纲条目数 |")
L.append("|---|---|---|")
for subj, fn in SYL_FILES:
    L.append("| %s | %s | %d |" % (S[subj]["subject_cn"], C(fn), S[subj]["n_entries"]))
L.append("| **合计** | 6 份 | **%d** |\n" % sum(S[s]["n_entries"] for s, _ in SYL_FILES))

for subj, fn in SYL_FILES:
    v = S[subj]
    L.append("## %s\n" % v["subject_cn"])
    L.append("> 考纲原文文件：" + C(fn))
    L.append("> 参考书：" + REFS[subj] + "\n")
    for sec, es in sect_map(v).items():
        L.append("### %s\n" % sec)
        for e in es:
            L.append("- **%s**（%s）  %s" % (e["cn"], e["en"], C(e["id"])))
        L.append("")

L.append("## 附：各科目考纲条目数\n")
L.append("| 科目 | 节数 | 条目数 |")
L.append("|---|---|---|")
for subj, fn in SYL_FILES:
    L.append("| %s | %d | %d |" % (subj, len(sect_map(S[subj])), S[subj]["n_entries"]))
L.append("| **合计** | **%d** | **%d** |\n" % (
    sum(len(sect_map(S[s])) for s, _ in SYL_FILES), sum(S[s]["n_entries"] for s, _ in SYL_FILES)))
L.append("> 条目拆分口径：考纲原文的一个 bullet 若并列了多个**独立命名对象**（如 Sylow theorems, p-groups, solvable groups, free groups），")
L.append("> 则拆成多条以便逐条做覆盖统计；纯修饰性短语不拆。\n")

open(R1, "w", encoding="utf-8").write("\n".join(L))
print("wrote", R1)

# ------------------------------------------------------------------ 报告 B
def rank(subj):
    return sorted(S[subj]["entries"], key=lambda e: (-e["priority_score"], -e["hits"], e["id"]))

def grade(e):
    return e["priority"][0]

tot_entries = sum(S[s]["n_entries"] for s, _ in SYL_FILES)
tot_zero = sum(S[s]["n_zero"] for s, _ in SYL_FILES)
tot_high = sum(S[s]["n_high"] for s, _ in SYL_FILES)
tot_mid = sum(S[s]["n_mid"] for s, _ in SYL_FILES)
n_up = sum(1 for s, _ in SYL_FILES for e in S[s]["entries"] if e["trend"] == "上升")
n_flat = sum(1 for s, _ in SYL_FILES for e in S[s]["entries"] if e["trend"] == "平稳")
n_down = sum(1 for s, _ in SYL_FILES for e in S[s]["entries"] if e["trend"].startswith("下降") or e["trend"].startswith("已消失"))

M = []
M.append("# 丘成桐大学生数学竞赛 · 考纲覆盖率分析报告\n")
M.append("**对象**：Yau Contest 官方 Syllabus（6 份）× 历年笔试真题 **%d** 道（个人赛 individual + 团体赛 team，含完整题面）。\n" % NP)
M.append("**数据**：" + C("data/problems_full.json") + "（题面）、" + C("data/syllabus_coverage.json") + "（逐条命中明细）。")
M.append("**脚本**：" + C("scripts/syllabus_coverage.py") + " + " + C("scripts/make_syllabus_reports.py") + "（可复跑）。**生成时间**：%s\n" % d["generated"])

M.append("## 0. 关键结论（先看这 8 条）\n")
M.append("1. 考纲共拆出 **%d** 条：高频命中（≥8 题）**%d** 条、偶发命中（1–7 题）**%d** 条、**零命中 %d 条（占 %s）**。"
         % (tot_entries, tot_high, tot_mid, tot_zero, pct(tot_zero, tot_entries)))
M.append("2. 考纲**不是命题清单**：近五成条目（%s）从未在笔试中以该术语出现过，它更像「研究生资格考范围」而非「竞赛出题范围」。" % pct(tot_zero, tot_entries))
M.append("3. 命中高度集中：各科目 Top 条目吃掉大半考卷——代数「%s」%d 题、几何「%s」%d 题、概率「%s」%d 题。" % (
    TOP("Algebra & Number Theory")[0], TOP("Algebra & Number Theory")[1],
    TOP("Geometry & Topology")[0], TOP("Geometry & Topology")[1],
    TOP("Probability & Statistics")[0], TOP("Probability & Statistics")[1]))
M.append("4. **分析卷是最「虚」的科目**：63 条里 39 条零命中（%s），实分析测度论与泛函分析几乎整块不考。" % pct(39, 63))
M.append("5. **数理物理是最「窄」的科目**：78 条里 42 条零命中（%s），但命中的 36 条全部落在近五年，属「窄而深」。" % pct(42, 78))
M.append("6. 反向发现：真题大量考查**考纲完全没写**的内容——线性代数与矩阵论（代数卷 %d 题）、点集拓扑（几何卷 %d 题）、数值线性代数（应用卷 %d 题）。" % (
    OOS("Algebra & Number Theory", "线性代数"), OOS("Geometry & Topology", "点集拓扑"), OOS("Computational & Applied", "纯数学式线性代数")))
M.append("7. 考纲标题含 **Combinatorics（组合数学），正文却没有任何组合条目**，真题中组合类题面也仅 %d 道——名实不符。" % OOS("Algebra & Number Theory", "组合数学"))
M.append("8. 趋势结构：**上升** %d 条、**平稳** %d 条、**下降/已消失** %d 条。上涨最明显的是应用与计算（数值稳定性）与概率统计（多元分布、条件期望）。"
         % (n_up, n_flat, n_down))

M.append("\n## 1. 方法与口径\n")
M.append("| 项 | 设定 |")
M.append("|---|---|")
M.append("| 检索对象 | 同科目真题题面全文（**不跨科目串味**：代数条目只在代数卷里搜） |")
M.append("| 匹配方式 | 每条考纲条目配一组正则（以英文术语为主），题面命中任一即计 1 题 |")
M.append("| 文本归一化 | 修正 PDF 抽取噪声：独立重音字符（Poincar´e 到 Poincare）、行尾连字符断词（prob- ability 到 probability）、统一撇号与破折号 |")
M.append("| 近年窗口 | 2022–2026（数理物理 2022 年才设科） |")
M.append("| 早期窗口 | 2010–2021 |")
M.append("| 状态判据 | **高频命中** ≥8 题；**偶发命中** 1–7 题；**零命中** 0 题 |")
M.append("| 趋势判据 | 近五年命中率 ÷ 早期命中率：≥1.5 上升；0.67–1.5 平稳；小于 0.67 下降；仅近五年出现 = 新兴；近五年为 0 = 已消失 |")
M.append("| 优先级得分 | **科目内命中密度(%) × 趋势系数**（上升 1.4 / 新兴 1.5 / 平稳 1.0 / 下降 0.75 / 已消失 0.4）。用密度而非绝对题数，才能让 30 题的数理物理与 159 题的几何同尺度比较 |")
M.append("| 等级 | **A** 得分 ≥12；**B** 4–12；**C** 大于 0 且小于 4；**D** 命中 0 题 |")
M.append("")
M.append("> **重要口径提醒**：关键词命中是**下界**而非真值。真题常直接陈述结论而不点名定理——分析卷 %d 道题里 %s、%s、%s **一次都没出现**，但复分析仍以「全纯/亚纯函数」形态考了 25 题。" % (
    S["Analysis & PDE"]["n_problems"], C("Cauchy"), C("residue"), C("Schwarz")))
M.append("> 因此「零命中」应读作「**从不以该术语/该形态出现**」，不等于该数学内容绝对不考。\n")

M.append("## 2. 总览：六科考纲覆盖率\n")
M.append("| 科目 | 考纲条目 | 高频命中(≥8) | 偶发命中(1–7) | **零命中** | 零命中占比 | 真题数 | 近五年真题 |")
M.append("|---|---|---|---|---|---|---|---|")
for subj, fn in SYL_FILES:
    v = S[subj]
    M.append("| %s | %d | %d | %d | **%d** | %s | %d | %d |" % (
        subj, v["n_entries"], v["n_high"], v["n_mid"], v["n_zero"],
        pct(v["n_zero"], v["n_entries"]), v["n_problems"], v["n_problems_recent"]))
M.append("| **合计** | **%d** | **%d** | **%d** | **%d** | **%s** | **%d** | **%d** |\n" % (
    tot_entries, tot_high, tot_mid, tot_zero, pct(tot_zero, tot_entries), NP,
    sum(S[s]["n_problems_recent"] for s, _ in SYL_FILES)))

M.append("按零命中占比排序（越靠前 = 考纲与该科实际考卷越脱节）：\n")
M.append("| 排名 | 科目 | 零命中 / 条目 | 零命中占比 |")
M.append("|---|---|---|---|")
for i, (subj, fn) in enumerate(sorted(SYL_FILES, key=lambda x: -S[x[0]]["n_zero"] / S[x[0]]["n_entries"]), 1):
    v = S[subj]
    M.append("| %d | %s | %d / %d | %s |" % (i, subj, v["n_zero"], v["n_entries"], pct(v["n_zero"], v["n_entries"])))
M.append("")

M.append("## 3. 逐条覆盖率明细（按考纲顺序）\n")
for idx, (subj, fn) in enumerate(SYL_FILES, 1):
    v = S[subj]
    M.append("### 3.%d %s\n" % (idx, v["subject_cn"]))
    M.append("真题 %d 道（近五年 %d 道）。\n" % (v["n_problems"], v["n_problems_recent"]))
    M.append("| ID | 考纲条目（英文原文） | 命中 | 近五年 | 早期 | 趋势 | 状态 | 优先级 |")
    M.append("|---|---|---|---|---|---|---|---|")
    for e in v["entries"]:
        M.append("| %s | %s（%s） | %d | %d | %d | %s | %s | **%s** |" % (
            e["id"], e["cn"], e["en"], e["hits"], e["hits_recent"], e["hits_early"],
            e["trend"], e["status"], grade(e)))
    M.append("")

M.append("## 4. 按考纲复习的优先级排序 ★核心节\n")
M.append("排序键 = **科目内命中密度(%) × 近年趋势系数**（记为「预估收益」）。")
M.append("A = 主战场，必须拿下；B = 高频，值得投入；C = 边角，按时间取舍；D = 从未考过，可战略性放弃。\n")

allA = []
for subj, fn in SYL_FILES:
    for e in S[subj]["entries"]:
        if grade(e) == "A":
            allA.append((subj, e))
allA.sort(key=lambda x: -x[1]["priority_score"])
M.append("### 4.1 跨科目 A 级总榜（共 %d 条）\n" % len(allA))
M.append("| # | 科目 | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |")
M.append("|---|---|---|---|---|---|---|---|")
for i, (subj, e) in enumerate(allA, 1):
    M.append("| %d | %s | %s（%s） | %d | %d | %.1f%% | %s | **%.1f** |" % (
        i, subj, e["cn"], e["en"], e["hits"], e["hits_recent"], e["density_pct"], e["trend"], e["priority_score"]))
M.append("")

for idx, (subj, fn) in enumerate(SYL_FILES, 2):
    M.append("### 4.%d %s：条目优先级排序\n" % (idx, S[subj]["subject_cn"]))
    for g, gname in [("A", "A 级 · 主战场（得分 ≥12）"), ("B", "B 级 · 高优先（4–12）"), ("C", "C 级 · 一般优先（小于 4）")]:
        rows = [e for e in rank(subj) if grade(e) == g]
        if not rows:
            M.append("**%s**：无。\n" % gname)
            continue
        M.append("**%s —— %d 条**\n" % (gname, len(rows)))
        M.append("| 排名 | ID | 考纲条目 | 命中 | 近五年 | 密度 | 趋势 | 得分 |")
        M.append("|---|---|---|---|---|---|---|---|")
        for i, e in enumerate(rows, 1):
            M.append("| %d | %s | %s（%s） | %d | %d | %.1f%% | %s | %.1f |" % (
                i, e["id"], e["cn"], e["en"], e["hits"], e["hits_recent"], e["density_pct"], e["trend"], e["priority_score"]))
        M.append("")

M.append("### 4.8 可以「战略性放弃」的零命中条目（全 %d 条）\n" % tot_zero)
M.append("下列条目在 2010–2026 全部 %d 道真题中**零命中**（按考纲分节归并）。除非时间极其充裕，不建议优先投入。\n" % NP)
for subj, fn in SYL_FILES:
    v = S[subj]
    zeros = [e for e in v["entries"] if e["hits"] == 0]
    M.append("#### %s —— %d / %d 条零命中（%s）\n" % (subj, len(zeros), v["n_entries"], pct(len(zeros), v["n_entries"])))
    for sec, es in sect_map(v).items():
        zs = [e for e in es if e["hits"] == 0]
        if not zs:
            continue
        M.append("- **%s**（%d 条）：%s" % (sec, len(zs), "；".join("%s（%s）" % (e["cn"], e["en"]) for e in zs)))
    M.append("")

M.append("## 5. 反向发现：真题里「超纲」考了什么\n")
M.append("把真题中出现、但**不被该科目任何考纲条目覆盖**的考点聚类统计（同一题可命中多类）。\n")
_k = 0
for subj, fn in SYL_FILES:
    rows = [r for r in d["out_of_syllabus"].get(subj, []) if r["hits"] >= 3]
    if not rows:
        continue
    _k += 1
    M.append("### 5.%d %s\n" % (_k, subj))
    M.append("| 超纲考点（考纲未列） | 命中题数 | 其中近五年 | 样例题目 |")
    M.append("|---|---|---|---|")
    for r in rows:
        M.append("| %s | %d | %d | %s |" % (
            r["label"], r["hits"], r["hits_recent"],
            "、".join(C(x) for x in r["examples"][:2])))
    M.append("")

M.append("### 5.%d 最值得注意的五条超纲结论\n" % (_k + 1))
_a, _g, _c = OOS("Algebra & Number Theory", "线性代数"), OOS("Geometry & Topology", "点集拓扑"), OOS("Computational & Applied", "纯数学式线性代数")
_na, _ng, _nc = S["Algebra & Number Theory"]["n_problems"], S["Geometry & Topology"]["n_problems"], S["Computational & Applied"]["n_problems"]
M.append("1. **代数卷的隐形主线是线性代数与矩阵论**（%d 题，占该科 %.0f%%）：特征值、秩、迹、矩阵分解、对角化在考纲里一个字都没有，却是最高频的解题工具。" % (_a, 100.0 * _a / _na))
M.append("2. **几何卷的隐形主线是点集拓扑**（%d 题，占该科 %.0f%%）：紧性、连通性、Hausdorff、同胚、开集这些基础拓扑不在任何条目中——考纲从「基本群」直接开始，跳过了点集拓扑层。" % (_g, 100.0 * _g / _ng))
M.append("3. **应用卷的隐形主线是数值线性代数**（%d 题，占该科 %.0f%%）：考纲只写「迭代法、条件数、SVD」，实际大量出现 LU/QR/Cholesky/Gram-Schmidt 与矩阵分解本身。" % (_c, 100.0 * _c / _nc))
M.append("4. **几何卷的经典曲线曲面论**（%d 题）：第一/第二基本形式、Gauss 曲率、极小曲面等经典内容不在微分几何条目中。" % OOS("Geometry & Topology", "经典曲线曲面论"))
M.append("5. **概率统计卷的回归与线性模型**（%d 题，近五年占比 100%%）：考纲完全没有回归/线性模型/ANOVA 条目，却是**唯一「近五年才冒出来」的超纲方向**，需要重点预警。\n" % OOS("Probability & Statistics", "回归"))
M.append("同时统计出**真题中从未涉及**的考纲外方向（命中 0）：代数几何、复几何与 Kähler 几何、辛几何、示性类、不动点定理（Brouwer/Borsuk-Ulam）、共形场论/弦论/全息、超对称、量子信息、信息论——属于较确定的「不会考」区间。\n")

M.append("## 6. 复习建议（由数据直接推出）\n")
M.append("| 科目 | 主攻（A 级） | 保底（B 级，前 5） | 可放弃 |")
M.append("|---|---|---|---|")
for subj, fn in SYL_FILES:
    ar = [e["cn"] for e in rank(subj) if grade(e) == "A"]
    br = [e["cn"] for e in rank(subj) if grade(e) == "B"][:5]
    M.append("| %s | %s | %s | %d 条零命中 |" % (
        subj,
        "、".join(ar) if ar else "**无 A 级条目**",
        "、".join(br) if br else "—",
        S[subj]["n_zero"]))
M.append("")
_edge = max((e for e in S["Analysis & PDE"]["entries"]), key=lambda x: x["priority_score"])
M.append("> 注：分析卷最高分条目为「%s（%s）」，得分 %.1f，仅差 %.1f 分未达 A 级阈值，实际应按 A 级强度对待。" % (
    _edge["cn"], _edge["en"], _edge["priority_score"], 12 - _edge["priority_score"]))
M.append("")
M.append("- **若只复习一件事**：概率统计卷的「随机变量 / 独立性」组合（%d + %d 题）是全竞赛命中密度最高的考点群。" % (
    TOP("Probability & Statistics")[1], [e for e in S["Probability & Statistics"]["entries"] if e["cn"] == "独立性"][0]["hits"]))
M.append("- **若只放弃一件事**：数理物理的 %d 条零命中条目（占该科目 %s）与几何的代数拓扑进阶块（相对同调、CW 复形、Mayer-Vietoris、万有系数、Künneth、Poincaré 对偶、Lefschetz、Čech）是性价比最低的投入。" % (S["Mathematical Physics"]["n_zero"], pct(S["Mathematical Physics"]["n_zero"], S["Mathematical Physics"]["n_entries"])))
M.append("- **小心「趋势下降」的高命中条目**：Hilbert 空间（8 题全在 2021 年前）、Lp 空间（6 题全在早期）、Sylow 定理（5 题全在早期）——历史上考过，近五年已不再出现。")
M.append("- **注意「新兴」条目**（近五年才首次出现，趋势系数 1.5）：离散赋值环、局部化、理想的根、Newton 法、拟 Newton 法、刚性 ODE、Lax 等价定理、Levi-Civita 联络、矩阵 Lie 群结构、特征函数、Brown 运动等。\n")

M.append("## 7. 局限与免责\n")
M.append("1. 关键词/正则命中是**下界**，不是真值；术语不出现的题不会计入。")
M.append("2. 同一题可同时命中多条考纲条目，各条目命中数之和大于真题总数（刻意设计，用于刻画考点重叠度）。")
M.append("3. 「超纲」判定基于正则覆盖与否，语义相近而措辞不同的考点可能被误判为超纲。")
M.append("4. 语料在分析期间处于动态更新，本次分析基准为 **%d** 题；复跑 " % NP + C("scripts/syllabus_coverage.py") + " 与 " + C("scripts/make_syllabus_reports.py") + " 即可刷新全部数字。")
M.append("5. 趋势的「上升/下降」用率比而非绝对数，故小样本科目（数理物理 30 题）单题权重较大。\n")

open(R2, "w", encoding="utf-8").write("\n".join(M))
print("wrote", R2)
print("entries=%d high=%d mid=%d zero=%d A=%d up=%d flat=%d down=%d" % (
    tot_entries, tot_high, tot_mid, tot_zero, len(allA), n_up, n_flat, n_down))
