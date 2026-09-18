# -*- coding: utf-8 -*-
"""生成 mother_computational.md 与 mother_computational.json（并校验成员真实性）。"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mothers_a import MOTHERS_A
from _mothers_b import ORPHANS, DOUBTS

ROOT = "E:/deepseek_exclusive/math/.tmp/burn2026"
DATA = ROOT + "/data/problems_full.json"
OUT_MD = ROOT + "/reports/mother_computational.md"
OUT_JSON = ROOT + "/data/mother_computational.json"
NL = chr(10)

SHORT_TREND = {
 "CA-M01":"升要求","CA-M02":"升要求","CA-M03":"换皮","CA-M04":"原样重复","CA-M05":"升要求",
 "CA-M06":"换皮","CA-M07":"换皮","CA-M08":"升要求","CA-M09":"升要求","CA-M10":"换皮",
 "CA-M11":"升要求","CA-M12":"升要求","CA-M13":"升要求","CA-M14":"升要求","CA-M15":"原样重复",
 "CA-M16":"换皮","CA-M17":"换皮","CA-M18":"升要求","CA-M19":"升要求","CA-M20":"升要求",
 "CA-M21":"升要求","CA-M22":"换皮","CA-M23":"升要求",
}

probs = json.load(open(DATA, encoding="utf-8"))
ca = [p for p in probs if p["subject"] == "Computational & Applied"]
index = {}
for p in ca:
    key = (p["year"], p["kind"], p["n"])
    if key in index:
        raise SystemExit("duplicate key: %s" % (key,))
    index[key] = p

used = {}
errors = []
for m in MOTHERS_A:
    for mem in m["members"]:
        key = (mem["year"], mem["kind"], mem["n"])
        if key not in index:
            errors.append("mother %s member missing: %s" % (m["id"], key))
        if key in used:
            errors.append("member %s used twice: %s / %s" % (key, used[key], m["id"]))
        used[key] = m["id"]
for o in ORPHANS:
    key = (o["year"], o["kind"], o["n"])
    if key not in index:
        errors.append("orphan missing: %s" % (key,))
    if key in used:
        errors.append("orphan %s already used by %s" % (key, used[key]))
    used[key] = "ORPHAN"
missing = [k for k in index if k not in used]
if missing:
    errors.append("unassigned problems: %s" % (missing,))
if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)
print("OK: %d problems all assigned (members %d + orphans %d)" % (len(ca), len(used)-len(ORPHANS), len(ORPHANS)))

KIND_CN = {"individual": "个", "team": "团"}
def recency(last):
    y = int(last)
    if y >= 2025: return 1.0
    if y == 2024: return 0.9
    if y >= 2022: return 0.8
    if y >= 2019: return 0.6
    return 0.4

for m in MOTHERS_A:
    ys = sorted(int(x["year"]) for x in m["members"])
    m["first"] = str(ys[0]); m["last"] = str(ys[-1]); m["count"] = len(m["members"])
    m["active"] = int(m["last"]) >= 2024
    m["score"] = round(m["count"] * recency(m["last"]), 2)
    m["short_trend"] = SHORT_TREND[m["id"]]
    m["years"] = sorted(set(ys))

jout = []
for m in MOTHERS_A:
    jout.append({
        "id": m["id"],
        "name": m["name"],
        "members": [{"year": x["year"], "kind": x["kind"], "n": x["n"]} for x in m["members"]],
        "first": m["first"],
        "last": m["last"],
        "trend": m["short_trend"],
        "trend_detail": m["trend"],
        "count": m["count"],
        "still_tested": m["active"],
        "cost_performance_score": m["score"],
        "years": m["years"],
    })
orphans_json = [{"year": o["year"], "kind": o["kind"], "n": o["n"], "why": o["why"]} for o in ORPHANS]
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump({"meta": {"source": "problems_full.json", "total_problems": len(probs),
                        "subject": "Computational & Applied", "subject_problems": len(ca),
                        "mothers": len(MOTHERS_A), "covered": len(ca) - len(ORPHANS),
                        "orphans": len(ORPHANS)},
               "mothers": jout, "orphans": orphans_json}, f, ensure_ascii=False, indent=1)
print("JSON written:", OUT_JSON)

L = []
A = L.append
A("# 丘成桐大学生数学竞赛 · Computational & Applied（计算与应用）母题归并")
A("")
A("> **数据口径**：`problems_full.json`（" + ROOT + "/data/problems_full.json），当前快照共 **%d 题**；" % len(probs))
A("> 其中 subject 为 Computational & Applied 的共 **%d 题**（个人赛 %d + 团体赛 %d，覆盖 2011-2026 年）。" % (
    len(ca), sum(1 for p in ca if p["kind"] == "individual"), sum(1 for p in ca if p["kind"] == "team")))
A("> 题目实体的唯一键是 **(year, kind, n)**（年份 / 卷别 / 题号），团体赛卷别记为 `team`、个人赛记为 `individual`。")
A("> 本报告基于 757 题的快照生成；若上游数据集再次变动，请按本文件 §0 的口径重跑 `scripts/build_mothers.py`。")
A("> 全部 %d 道题面已逐条通读（导出件：`reports/_ca_all_problems.md`），未使用任何自动查重结果。" % len(ca))
A("")
A("---")
A("")
A("## §0 方法与口径")
A("")
A("### 0.1 什么算「同一母题」")
A("")
A("判定的主标准是**解法骨架相同**，而不是措辞、对象或标签相同。具体按优先级：")
A("")
A("1. **数学骨架（必要条件）**：两道题的解题流程可以写成同一串 3-8 步的操作（例如「Taylor 展开定阶 → Fourier 模态求放大因子 → 由 |G|≤1 解出 CFL」）。只要骨架相同，即使**被离散的方程、被逼近的函数、被优化的目标完全不同**，也算同一母题——这正是本题库命题人的主要手法，也是字符串查重完全失效的原因。")
A("2. **对象可替换（加分项，不是必要条件）**：若把题目里的对象（权函数、矩阵结构、参数化方法、极限情形）换一个，题干仍是同一道题，则强烈支持归并。")
A("3. **提问方式相同（加分项）**：同一种问法反复出现（「求最高精度阶 k」「求稳定阈值 λ0」「讨论是否达 Fisher 界」）是母题的直接指纹。")
A("4. **数学对象的同一性（仅作辅助）**：同一主题（比如「都是数值代数」）**不足以**归并；主题相同而骨架不同的题一律不合并。")
A("")
A("### 0.2 排除的边界情况（宁缺勿滥）")
A("")
A("- **只共享主题、不共享证明骨架**的题不合并。例如「辛格式」（验证 Jacobian 满足 ΦᵀJΦ=J）、「稳定性在扰动下保持」（范数估计 + Gronwall）、「收缩性保持」（写成前向 Euler 凸组合）三者都属「结构保持」，但骨架不同，故 2018 个人赛 2 与 2020 个人赛 5 保留为孤题（见 §4 D3）。")
A("- **一次性出现、且没有同骨架第二例**的题一律进孤题清单，绝不为了压低孤题数而硬凑。")
A("- **同年个人赛与团体赛复用同一道题**（2013 个6 与 2013 团6 逐字相同）仍按题库中的两个题目实体各计 1 个成员；但会在 §3 单独标注，避免据此高估命题人的重视程度。")
A("- **题干残缺/串页**的记录（2017 个人赛 5）不强行归并，列入孤题并在 §4 D4 说明数据缺陷。")
A("- **概率统计块**（2011 年的 8 题）虽然与后来独立成科的内容不同，但只要骨架成立就照常归并（CA-M03 的三道题其实分属个人赛与团体赛两卷）。")
A("")
A("### 0.3 术语与记号")
A("")
A("- 成员记为「年份+卷别+题号」，如 `2011团2` = 2011 年团体赛第 2 题，`2025个5` = 2025 年个人赛第 5 题。")
A("- 母题编号 `CA-Mxx`，`CA` = Computational & Applied；编号按**首现年份**升序，同年内按成员数降序。")
A("- 「仍在考」的判据：该母题在 **2024-2026** 三年内至少出现过一次。")
A("- 报告中的 ψ、λ、ρ、σ、θ、α、β、γ、ε、δ、µ、Ω、κ、ℓ、≤、≥、≠、∈、∫、√、⟹、ᵀ 等符号沿用题目原意，均为纯文本形式。")
A("")
A("---")
A("")
A("## §1 母题总表")
A("")
A("共归并出 **%d 个母题**，覆盖 **%d/%d = %.1f%%** 的题目；**%d 道孤题**（%.1f%%）。" % (
    len(MOTHERS_A), len(ca)-len(ORPHANS), len(ca), 100.0*(len(ca)-len(ORPHANS))/len(ca),
    len(ORPHANS), 100.0*len(ORPHANS)/len(ca)))
A("")
A("| 母题编号 | 母题名（一句话数学描述） | 成员题目（年份/卷别/题号） | 成员数 | 首现 | 末现 | 是否仍在考 | 变化趋势 |")
A("|---|---|---|---|---|---|---|---|")
for m in MOTHERS_A:
    mem = "、".join("%s%s%s" % (x["year"], KIND_CN[x["kind"]], x["n"]) for x in m["members"])
    A("| **%s** | %s | %s | %d | %s | %s | %s | %s |" % (
        m["id"], m["name"], mem, m["count"], m["first"], m["last"],
        ("是（末现 %s）" % m["last"]) if m["active"] else ("否（末现 %s）" % m["last"]),
        m["short_trend"]))
A("")
A("> 变化趋势取值：原样重复 / 换皮 / 升要求 / 降要求（本科目未出现「降要求」型母题）；详细描述见 §2 各母题的「递进关系」。")
A("")
A("---")
A("")
A("## §2 各母题详解")
A("")
for m in MOTHERS_A:
    A("### %s %s" % (m["id"], m["name"]))
    A("")
    A("**成员**（%d 题，%s-%s，%s）：%s" % (
        m["count"], m["first"], m["last"], "仍在考" if m["active"] else "已淡出",
        "、".join("%s%s%s" % (x["year"], KIND_CN[x["kind"]], x["n"]) for x in m["members"])))
    A("")
    A("#### 数学内核")
    A("")
    A(m["core"])
    A("")
    A("#### 成员逐一对照（该年版本与母题的差异）")
    A("")
    for x in m["members"]:
        A("- **%s%s%d**：%s" % (x["year"], KIND_CN[x["kind"]], x["n"], x["diff"]))
    A("")
    A("#### 递进关系")
    A("")
    A(m["chain"])
    A("")
    A("#### 标准解法骨架")
    A("")
    for j, s in enumerate(m["skeleton"], 1):
        A("%d. %s" % (j, s))
    A("")
    A("**最容易卡住的一步**：%s" % m["stuck"])
    A("")
    A("---")
    A("")
A("## §3 统计")
A("")
A("### 3.1 总量")
A("")
A("| 指标 | 数值 |")
A("|---|---|")
A("| 本科目题目总数 | %d（个人赛 %d / 团体赛 %d） |" % (len(ca), sum(1 for p in ca if p["kind"]=="individual"), sum(1 for p in ca if p["kind"]=="team")))
A("| 归并出的母题数 | %d |" % len(MOTHERS_A))
A("| 被母题覆盖的题目数 | %d |" % (len(ca)-len(ORPHANS)))
A("| 覆盖率 | %.1f%% |" % (100.0*(len(ca)-len(ORPHANS))/len(ca)))
A("| 孤题数（无同骨架第二例） | %d（%.1f%%） |" % (len(ORPHANS), 100.0*len(ORPHANS)/len(ca)))
A("| 平均每个母题的成员数 | %.1f |" % (float(len(ca)-len(ORPHANS))/len(MOTHERS_A)))
A("| 成员数 ≥5 的大母题 | %d 个（占被覆盖题目的 %.1f%%） |" % (
    sum(1 for m in MOTHERS_A if m["count"]>=5),
    100.0*sum(m["count"] for m in MOTHERS_A if m["count"]>=5)/(len(ca)-len(ORPHANS))))
A("| 只在单一年份出现的母题 | %d 个（%s） |" % (
    sum(1 for m in MOTHERS_A if len(m["years"])==1),
    "、".join(m["id"] for m in MOTHERS_A if len(m["years"])==1)))
A("| 跨度 ≥10 年的母题 | %d 个（%s） |" % (
    sum(1 for m in MOTHERS_A if int(m["last"])-int(m["first"])>=10),
    "、".join(m["id"] for m in MOTHERS_A if int(m["last"])-int(m["first"])>=10)))
A("")
A("### 3.2 母题成员数分布")
A("")
dist = collections.Counter(m["count"] for m in MOTHERS_A)
ks = sorted(dist, reverse=True)
A("| 成员数 | " + " | ".join(str(k) for k in ks) + " |")
A("|---|" + "---|"*len(ks))
A("| 母题个数 | " + " | ".join(str(dist[k]) for k in ks) + " |")
A("")
A("成员数 ≥5 的母题：%s。" % "、".join("%s(%d)" % (m["id"], m["count"]) for m in sorted(MOTHERS_A, key=lambda x: -x["count"]) if m["count"]>=5))
A("")
A("### 3.3 覆盖率按年份")
A("")
A("| 年份 | 本科目题数 | 已归并 | 孤题 | 覆盖率 | 该年出现的母题 |")
A("|---|---|---|---|---|---|")
byyear = collections.defaultdict(list)
for m in MOTHERS_A:
    for x in m["members"]:
        byyear[x["year"]].append(m["id"])
orph_by_year = collections.Counter(o["year"] for o in ORPHANS)
for y in sorted(set(p["year"] for p in ca)):
    tot = sum(1 for p in ca if p["year"] == y)
    o = orph_by_year.get(y, 0)
    ids = sorted(set(byyear.get(y, [])))
    A("| %s | %d | %d | %d | %.0f%% | %s |" % (y, tot, tot-o, o, 100.0*(tot-o)/tot, "、".join(ids) if ids else "—"))
A("")
A("### 3.4 归并结果反映出的结构性事实")
A("")
A("- **概率统计只在 2011 年出现过**：2011 年本科目卷（卷名即 Applied Math. Prob. Stat.）12 题里有 8 题是概率统计，构成 CA-M03、CA-M04 以及 4 道孤题；自 2012 年起 Probability & Statistics 独立成科（数据集中 2012 年起即有该 subject），本科目再未出现纯概率统计题。")
A("- **图论/组合块 2013-2018 短暂存在后消失**：CA-M14（Ore 型度和条件，3 题）与 3 道图论孤题（2015团2、2018团1、2018团2）全部集中在 2013-2018；2019 年后无一道图论题。")
A("- **算法数论/离散算法块 2012-2017 后消失**：CA-M10（RSA 素数间距）、CA-M15（矩阵快速幂）、CA-M18（小整数解/可乘相关）与孤题 2014个2、2014团1、2014团2 都在这个窗口内，2018 年后不再出现。")
A("- **数值分析（差分格式、数值代数、逼近论、优化）是唯一贯穿全期的骨架**：CA-M01（2011-2025，15 题）、CA-M02（2011-2025，7 题）、CA-M08（2012-2025）、CA-M12（2012-2026）、CA-M19（2016-2026）、CA-M20（2016-2026）、CA-M23（2020-2026）。")
A("- **2020 年后题量收紧但单题变深**：2020 年起本科目固定为个人赛 6 题（无团体赛）。CA-M01 的 15 个成员中有 6 题落在 2020 年之后，且近年更倾向综合型出题（一题同时要求定阶 + 证稳定 + 证收敛，如 2023个5、2025个5）。")
A("")
A("### 3.5 性价比 TOP 10（出现次数 × 近年趋势）")
A("")
A("打分方式：`score = 成员数 × 时效权重`，时效权重按末现年份取：末现 ≥2025 → 1.0、2024 → 0.9、2022-2023 → 0.8、2019-2021 → 0.6、≤2018 → 0.4。既奖励考得多，也奖励还在考。")
A("")
A("| 排名 | 母题 | 成员数 | 末现 | 时效权重 | 性价比分 | 一句话理由 |")
A("|---|---|---|---|---|---|---|")
REASON = {
 "CA-M01":"本科目的绝对主干：同一条流水线从 2011 考到 2025，几乎每年卷面至少一题。",
 "CA-M02":"正交多项式 + 高斯求积是逼近论唯一的长寿母题，2023/2024/2025 连续三年出现，只换权函数与多项式族。",
 "CA-M20":"凸分析与一阶方法是近年稳定板块：2026 年一卷内占 2 题，且与 2016/2018/2019 旧题同骨架。",
 "CA-M23":"ODE 方法的阶与绝对稳定域几乎年年考，2020 起每年一题，要求从求稳定域升到证 A-稳定区间。",
 "CA-M08":"SVD/低秩逼近从 2012 考到 2025，形态从 Eckart-Young 升到核范数凸松弛与最小范数解。",
 "CA-M16":"特殊结构矩阵（三对角/对角占优）用固定套路出场：求逆 + 范数界 + 谱圆盘，2024/2025 连续出现。",
 "CA-M19":"特征值迭代算法（幂法→子空间→QR）是 2016 年后的固定考点，2026 年刚考过 QR 迭代。",
 "CA-M12":"椭圆 BVP 的变分形式 + 有限元误差估计，2021/2026 两次以综合大题出现，是压轴型母题。",
 "CA-M21":"非线性方程迭代法的收敛阶，题短但高频，2025 年刚考过。",
 "CA-M09":"定常迭代法的收敛判据与最优参数在 2012-2022 反复出现，是数值代数里最成体系的一条。",
}
for r, m in enumerate(sorted(MOTHERS_A, key=lambda x: (-x["score"], -x["count"], x["id"]))[:10], 1):
    A("| %d | **%s** %s | %d | %s | %.1f | %.1f | %s |" % (
        r, m["id"], m["name"], m["count"], m["last"], recency(m["last"]), m["score"], REASON[m["id"]]))
A("")
A("### 3.6 同年双卷复用与配对命题")
A("")
A("母题成员表的计数单位是题库中的题目实体，因此同一年个人赛与团体赛的配对会各计 1 个成员。为免高估命题人的重视程度，这里单独说明：")
A("")
A("| 类型 | 组 | 说明 |")
A("|---|---|---|")
A("| 逐字复用 | 2013个6 = 2013团6 | 题干、提示、要求完全一致（CA-M15） |")
A("| 同骨架配对 | 2011个4 / 2011团4 | 个人赛证不等式、团体赛证充要条件（CA-M04） |")
A("| 同骨架配对 | 2016个3 / 2016团3 | 个人赛应用引理、团体赛证明同一条引理（CA-M18） |")
A("| 同年同母题跨卷 | 2013个5 / 2013团5 | 度和条件下的 Hamilton 性与 cyclable（CA-M14） |")
A("| 同年同母题跨卷 | 2012个5 / 2012团4 | 孪生素数与相邻素数构造的 RSA 模数分解（CA-M10） |")
A("| 同年同母题跨卷 | 2011个5 + 2011个6 / 2011团6 | 同一年三题共用 UMVU + Fisher 界的骨架（CA-M03） |")
A("")
A("### 3.7 孤题清单（%d 题）" % len(ORPHANS))
A("")
A("| 出处 | 题目内容（截断至 80 字） | 为何不成母题 |")
A("|---|---|---|")
for o in sorted(ORPHANS, key=lambda x: (x["year"], x["kind"], x["n"])):
    txt = index[(o["year"], o["kind"], o["n"])]["text"].strip().replace(NL, " ")
    A("| %s%s%s | %s | %s |" % (o["year"], KIND_CN[o["kind"]], o["n"], (txt[:80] + "…") if len(txt) > 80 else txt, o["why"]))
A("")
A("---")
A("")
A("## §4 存疑（拿不准是否同一母题的边界情况）")
A("")
A("下列 %d 处判断均可有两解，我给出最终取舍与理由；若后续有新证据，应优先复核这几处。" % len(DOUBTS))
A("")
for i, d in enumerate(DOUBTS, 1):
    A("#### D%d. %s" % (i, d["title"]))
    A("")
    A("- **解释 A**：%s" % d["a"])
    A("- **解释 B**：%s" % d["b"])
    A("- **本次取舍**：%s" % d["pick"])
    A("")
A("### 附录：本次归并未能利用的信息")
A("")
A("- 原卷 PDF 只有 2010-2025（F 盘），2026 年 6 道题全部来自 JSON 抽取文本，无法与原卷核对。")
A("- 2017 个人赛 5 的抽取文本与 2014 个人赛 3 串页，是本批次唯一确认的数据缺陷（见 §3.6 与 D4）。")
A("")
with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write(NL.join(L))
print("MD written:", OUT_MD, "chars:", len(NL.join(L)))
print("mothers %d, covered %d, orphans %d" % (len(MOTHERS_A), len(ca)-len(ORPHANS), len(ORPHANS)))
