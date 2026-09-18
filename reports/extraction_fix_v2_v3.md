# 抽取规则修正 v2 -> v3（去碎片）

v2 的裸编号规则会把分数/公式残留（单独一行的一个数字）当成新题号，v3 要求裸编号后必须跟 >=12 字符的正文。

| 年份 | 科目 | 卷别 | v2 | v3 | 变化 |
|---|---|---|---|---|---|
| 2010 | Algebra & Number Theory | team | 6 | 5 | -1 |
| 2010 | Analysis & PDE | individual | 6 | 0 | -6 |
| 2010 | Analysis & PDE | team | 6 | 0 | -6 |
| 2010 | Geometry & Topology | individual | 6 | 5 | -1 |
| 2010 | Probability & Statistics | individual | 6 | 3 | -3 |
| 2011 | Geometry & Topology | team | 6 | 5 | -1 |
| 2012 | Analysis & PDE | individual | 6 | 5 | -1 |
| 2012 | Geometry & Topology | individual | 5 | 4 | -1 |
| 2012 | Geometry & Topology | team | 6 | 4 | -2 |
| 2012 | Probability & Statistics | team | 6 | 5 | -1 |
| 2013 | Computational & Applied | individual | 6 | 3 | -3 |
| 2013 | Geometry & Topology | team | 6 | 4 | -2 |
| 2014 | Analysis & PDE | team | 6 | 4 | -2 |
| 2014 | Computational & Applied | team | 5 | 0 | -5 |
| 2014 | Geometry & Topology | individual | 6 | 3 | -3 |
| 2014 | Geometry & Topology | team | 6 | 5 | -1 |
| 2015 | Analysis & PDE | team | 6 | 2 | -4 |
| 2016 | Geometry & Topology | individual | 6 | 5 | -1 |
| 2016 | Geometry & Topology | team | 6 | 3 | -3 |
| 2017 | Computational & Applied | team | 5 | 4 | -1 |
| 2017 | Geometry & Topology | individual | 6 | 1 | -5 |
| 2018 | Analysis & PDE | team | 5 | 2 | -3 |
| 2018 | Geometry & Topology | individual | 6 | 4 | -2 |
| 2018 | Geometry & Topology | team | 6 | 3 | -3 |
| 2019 | Algebra & Number Theory | individual | 5 | 3 | -2 |
| 2019 | Algebra & Number Theory | team | 5 | 4 | -1 |
| 2019 | Computational & Applied | individual | 4 | 0 | -4 |
| 2019 | Computational & Applied | team | 5 | 0 | -5 |
| 2019 | Geometry & Topology | individual | 5 | 4 | -1 |
| 2019 | Geometry & Topology | team | 5 | 4 | -1 |
| 2022 | Mathematical Physics | individual | 6 | 0 | -6 |
| 2023 | Geometry & Topology | individual | 6 | 0 | -6 |
| 2024 | Computational & Applied | individual | 6 | 4 | -2 |

v2 合计 758 题 -> v3 合计 669 题。
仍有 <60 字符碎片小问的卷：31 个（碎片通常来自分数/公式换行，属已知抽取噪声）。

- 2010_AlgebraNumberTheory_individual.txt：题号 [6]
- 2010_AlgebraNumberTheory_team.txt：题号 [5]
- 2010_Applied_Computational_Probability_and_Statistics_individual.txt：题号 [1]
- 2010_GeometryTopology_indi.txt：题号 [2, 3, 5]
- 2010_GeometryTopology_team.txt：题号 [5]
- 2011_1_AnalysisDiffEquation_Individual_2011.txt：题号 [2, 3]
- 2011_3_GeomTop_Individual_2011.txt：题号 [3]
- 2011_4_Algebra_Individual_2011.txt：题号 [6]
- 2011_5_AnalysisDiffEquation_Team_2011.txt：题号 [2]
- 2011_7_GeomTop_Team_2011.txt：题号 [2]
- 2011_8_Algebra_Team_2011.txt：题号 [2, 4]
- 2012_Analysis_individual.txt：题号 [1, 3]
- 2012_Geometry2012individual.txt：题号 [1, 3]
- 2012_Geometry2012team.txt：题号 [1, 3, 5]
- 2012_Probability2012_team.txt：题号 [3]
- 2013_TeamProblems2013.txt：题号 [4, 5]
- 2013_analysis2013_individual.txt：题号 [2, 4]
- 2014_algebra2014_team.txt：题号 [4]
- 2014_analysis2014_team.txt：题号 [1, 2]
- 2014_geometry2014_team.txt：题号 [1, 4]
- 2015_analysis2015_individual.txt：题号 [3]
- 2015_geometry2015_individual.txt：题号 [1, 2, 4]
- 2015_team_analysis2015.txt：题号 [1]
- 2015_team_geometry2015.txt：题号 [5]
- 2016_2016_team.txt：题号 [1, 3, 4]
