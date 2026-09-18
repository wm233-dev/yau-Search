
import json, collections
TAGS = {
"2010|individual|1":["条件期望/测度论概率"],
"2010|individual|2":["极限定理/收敛"],
"2010|individual|3":["分布论/特征函数"],
"2010|individual|4":["估计理论","渐近统计","假设检验/置信区间"],
"2010|team|1":["顺序统计量/极值/记录","分布论/特征函数"],
"2010|team|2":["极限定理/收敛","渐近统计"],
"2010|team|3":["决策论/minimax","估计理论"],
"2010|team|4":["估计理论","渐近统计","假设检验/置信区间"],
"2011|individual|1":["经典随机模型题"],
"2011|individual|2":["概率不等式/集中"],
"2011|individual|3":["估计理论","假设检验/置信区间","渐近统计"],
"2011|individual|4":["估计理论","渐近统计"],
"2011|team|1":["分布论/特征函数"],
"2011|team|2":["概率不等式/集中","顺序统计量/极值/记录"],
"2011|team|3":["贝叶斯"],
"2011|team|4":["估计理论"],
"2012|individual|1":["经典随机模型题","极限定理/收敛"],
"2012|individual|2":["条件期望/测度论概率","分布论/特征函数"],
"2012|individual|3":["经典随机模型题","分布论/特征函数"],
"2012|individual|4":["非参数统计","假设检验/置信区间"],
"2012|individual|5":["概率不等式/集中","分布论/特征函数"],
"2012|individual|6":["分布论/特征函数"],
"2012|team|1":["极限定理/收敛","随机游走/Markov链"],
"2012|team|2":["分布论/特征函数","经典随机模型题"],
"2012|team|3":["概率不等式/集中"],
"2012|team|4":["分布论/特征函数","经典随机模型题"],
"2012|team|5":["估计理论","渐近统计"],
"2012|team|6":["假设检验/置信区间","渐近统计"],
"2013|individual|1":["极限定理/收敛"],
"2013|individual|2":["条件期望/测度论概率"],
"2013|individual|3":["顺序统计量/极值/记录"],
"2013|individual|4":["假设检验/置信区间","估计理论"],
"2013|individual|5":["假设检验/置信区间"],
"2013|individual|6":["估计理论","经典随机模型题"],
"2013|team|1":["分布论/特征函数"],
"2013|team|2":["极限定理/收敛"],
"2013|team|3":["条件期望/测度论概率"],
"2013|team|4":["贝叶斯","假设检验/置信区间"],
"2013|team|5":["高维/统计学习/回归","凸优化/次梯度"],
"2013|team|6":["高维/统计学习/回归","估计理论"],
"2014|individual|1":["分布论/特征函数","概率不等式/集中"],
"2014|individual|2":["极限定理/收敛"],
"2014|individual|3":["条件期望/测度论概率"],
"2014|individual|4":["条件期望/测度论概率","顺序统计量/极值/记录"],
"2014|individual|5":["估计理论","渐近统计","假设检验/置信区间"],
"2014|team|1":["极限定理/收敛"],
"2014|team|2":["分布论/特征函数"],
"2014|team|3":["条件期望/测度论概率"],
"2014|team|4":["估计理论","渐近统计"],
"2014|team|5":["估计理论","顺序统计量/极值/记录","渐近统计"],
"2015|individual|1":["概率不等式/集中","条件期望/测度论概率"],
"2015|individual|2":["经典随机模型题"],
"2015|individual|3":["极限定理/收敛"],
"2015|individual|4":["估计理论"],
"2015|individual|5":["假设检验/置信区间"],
"2015|team|1":["经典随机模型题"],
"2015|team|2":["极限定理/收敛"],
"2015|team|3":["分布论/特征函数"],
"2015|team|4":["概率不等式/集中","分布论/特征函数"],
"2015|team|5":["高维/统计学习/回归","凸优化/次梯度"],
"2016|individual|1":["随机游走/Markov链"],
"2016|individual|2":["随机矩阵","概率不等式/集中"],
"2016|individual|3":["经典随机模型题","分布论/特征函数"],
"2016|individual|4":["概率不等式/集中"],
"2016|individual|5":["随机游走/Markov链","极限定理/收敛"],
"2016|team|1":["随机游走/Markov链","条件期望/测度论概率"],
"2016|team|2":["概率不等式/集中","估计理论"],
"2016|team|3":["分布论/特征函数","数论概率/等分布"],
"2016|team|4":["极限定理/收敛"],
"2016|team|5":["顺序统计量/极值/记录"],
"2017|individual|1":["经典随机模型题"],
"2017|individual|2":["随机游走/Markov链"],
"2017|individual|3":["极限定理/收敛","大偏差/信息论"],
"2017|individual|4":["随机图/组合概率"],
"2017|individual|5":["随机游走/Markov链"],
"2017|team|1":["概率不等式/集中"],
"2017|team|2":["极限定理/收敛"],
"2017|team|3":["随机游走/Markov链","经典随机模型题"],
"2017|team|4":["随机游走/Markov链","极限定理/收敛"],
"2017|team|5":["估计理论","渐近统计"],
"2018|individual|1":["贝叶斯"],
"2018|individual|2":["随机游走/Markov链"],
"2018|individual|3":["经典随机模型题","分布论/特征函数"],
"2018|individual|4":["分布论/特征函数","条件期望/测度论概率"],
"2018|individual|5":["分布论/特征函数","估计理论"],
"2018|team|1":["顺序统计量/极值/记录","渐近统计"],
"2018|team|2":["随机游走/Markov链"],
"2018|team|3":["大偏差/信息论","凸优化/次梯度"],
"2018|team|4":["非参数统计"],
"2018|team|5":["估计理论","贝叶斯"],
"2019|individual|1":["极限定理/收敛"],
"2019|individual|2":["随机游走/Markov链"],
"2019|individual|3":["极限定理/收敛","随机游走/Markov链"],
"2019|individual|4":["因果推断/实验设计"],
"2019|team|1":["极限定理/收敛"],
"2019|team|2":["极限定理/收敛"],
"2019|team|3":["随机图/组合概率"],
"2019|team|4":["随机图/组合概率"],
"2020|single|1":["概率不等式/集中"],
"2020|single|2":["分布论/特征函数"],
"2020|single|3":["随机游走/Markov链"],
"2020|single|4":["分布论/特征函数","极限定理/收敛"],
"2020|single|5":["因果推断/实验设计"],
"2020|single|6":["因果推断/实验设计"],
"2021|single|1":["极限定理/收敛"],
"2021|single|2":["随机游走/Markov链"],
"2021|single|3":["极限定理/收敛"],
"2021|single|4":["随机矩阵"],
"2021|single|5":["因果推断/实验设计"],
"2021|single|6":["因果推断/实验设计"],
"2022|single|1":["极限定理/收敛","分布论/特征函数"],
"2022|single|2":["条件期望/测度论概率","分布论/特征函数"],
"2022|single|3":["随机游走/Markov链","经典随机模型题"],
"2022|single|4":["随机游走/Markov链","极限定理/收敛"],
"2022|single|5":["估计理论","高维/统计学习/回归"],
"2022|single|6":["决策论/minimax","高维/统计学习/回归"],
"2023|single|1":["贝叶斯","经典随机模型题"],
"2023|single|2":["条件期望/测度论概率","鞅/停时"],
"2023|single|3":["顺序统计量/极值/记录","极限定理/收敛"],
"2023|single|4":["条件期望/测度论概率"],
"2023|single|5":["估计理论","假设检验/置信区间"],
"2023|single|6":["估计理论","假设检验/置信区间","渐近统计"],
"2024|single|1":["随机游走/Markov链","鞅/停时"],
"2024|single|2":["随机游走/Markov链"],
"2024|single|3":["分布论/特征函数","数论概率/等分布"],
"2024|single|4":["高维/统计学习/回归","渐近统计"],
"2024|single|5":["估计理论","渐近统计"],
"2025|single|1":["假设检验/置信区间","决策论/minimax"],
"2025|single|2":["决策论/minimax","假设检验/置信区间"],
"2025|single|3":["分布论/特征函数"],
"2025|single|4":["估计理论","渐近统计"],
"2026|single|1":["因果推断/实验设计","分布论/特征函数"],
"2026|single|2":["高维/统计学习/回归"],
"2026|single|3":["分布论/特征函数"],
"2026|single|4":["布朗运动/随机分析"],
"2026|single|5":["分布论/特征函数","极限定理/收敛"],
"2026|single|6":["分布论/特征函数"],
}
b=json.load(open(r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\prob_ps_bodies.json",encoding='utf-8'))
missing=[k for k in b if k not in TAGS]
extra=[k for k in TAGS if k not in b]
print("missing tags:",missing); print("extra keys:",extra)
years=collections.defaultdict(set); counts=collections.Counter(); last={}
for k,tags in TAGS.items():
    y=k.split("|")[0]
    for t in tags:
        years[t].add(y); counts[t]+=1
        last[t]=max(last.get(t,"0"),y)
print()
print(f"{'考点':32s} {'年数':>4s} {'题次':>4s}  {'最近':>5s} {'骨架':>4s}  年份")
for t,_ in counts.most_common():
    ys=sorted(years[t])
    print(f"{t:32s} {len(ys):4d} {counts[t]:4d}  {last[t]:>5s} {'Y' if len(ys)>=5 else ' ':>4s}  {','.join(ys)}")
print()
print("tag total (题次含多标签重复):", sum(counts.values()), " 题目数:", len(TAGS))
PROB={"极限定理/收敛","条件期望/测度论概率","鞅/停时","随机游走/Markov链","随机图/组合概率","分布论/特征函数","顺序统计量/极值/记录","概率不等式/集中","随机矩阵","布朗运动/随机分析","经典随机模型题","数论概率/等分布"}
STAT=set(counts)-PROB
py=collections.defaultdict(set); pc=collections.Counter(); sy=collections.defaultdict(set); sc=collections.Counter()
for k,tags in TAGS.items():
    y=k.split("|")[0]
    for t in tags:
        if t in PROB: py[t].add(y); pc[t]+=1
        else: sy[t].add(y); sc[t]+=1
print("概率侧 题次合计:", sum(pc.values()), " 统计侧 题次合计:", sum(sc.values()))
print("每年前3大考点:")
for y in sorted({k.split('|')[0] for k in TAGS}):
    c=collections.Counter()
    for k,tags in TAGS.items():
        if k.split("|")[0]==y:
            for t in tags: c[t]+=1
    print(y, c.most_common(3))
