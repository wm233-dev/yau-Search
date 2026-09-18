
import json, collections, statistics, re
d=json.load(open(r'E:\deepseek_exclusive\math\.tmp\burn2026\data\problems_full.json',encoding='utf-8'))
print("TOTAL problems", len(d))
print("subjects", collections.Counter(x["subject"] for x in d))
print("kinds", collections.Counter(x["kind"] for x in d))
SUB=re.compile(r"(Applied|Physics)")
sub=[x for x in d if SUB.search(x["subject"])]
print("applied+phys problems", len(sub))
for name in sorted(set(x["subject"] for x in sub)):
    v=[x for x in sub if x["subject"]==name]
    sp=[len(re.findall(r"(?:^|\n|\s)\(([a-e]|\d)\)", x["text"])) for x in v]
    print("%-24s n=%3d meanchars=%6.1f medchars=%5.0f meansub=%.2f team=%d indiv=%d" % (
        name, len(v), statistics.mean([x["chars"] for x in v]), statistics.median([x["chars"] for x in v]),
        statistics.mean(sp), sum(1 for x in v if x["kind"]=="team"), sum(1 for x in v if x["kind"]=="individual")))
# per year for these subjects
for name in sorted(set(x["subject"] for x in sub)):
    v=[x for x in sub if x["subject"]==name]
    c=collections.Counter(x["year"] for x in v)
    print(name, dict(sorted(c.items())))
# whole corpus
print("ALL mean chars %.1f median %.0f" % (statistics.mean([x["chars"] for x in d]), statistics.median([x["chars"] for x in d])))
# verb distribution applied+phys
VERBS=["show","prove","find","compute","derive","determine","construct","solve","calculate","explain","estimate"]
for name in sorted(set(x["subject"] for x in sub)):
    v=[x for x in sub if x["subject"]==name]
    print(name, {k: sum(1 for x in v if re.search(r"\b"+k, x["text"], re.I)) for k in VERBS})
# overall/all-around in preliminary
print("all-round hits:", sum(1 for x in d if re.search(r"all.round|overall", x["text"], re.I)))
print("papers with overall in name:", len([p for p in set(x["paper"] for x in d) if re.search(r"overall|allround|all_round", p, re.I)]))
