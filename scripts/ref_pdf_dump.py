
import os, sys, io
sys.path.insert(0, r"E:\deepseek_exclusive\math\pylibs")
import fitz
root = r"F:\丘成桐大学生数学竞赛历年笔试真题"
out = open(r"E:\deepseek_exclusive\math\.tmp\burn2026\work\ref_pdf_dump.txt","w",encoding="utf-8")
files = {
 "2011": r"2011\1.AnalysisDiffEquation-Individual-2011.pdf",
 "2014team": r"2014\analysis2014(team).pdf",
 "2015": r"2015\analysis2015-individual.pdf",
 "2010": r"2010\Analysis and differential equations individual.pdf",
 "2013": r"2013\analysis2013(individual).pdf",
 "2017team": r"2017\2017-team.pdf",
 "2020": r"2020\Analysis&DifferentialEquations\analysis_and_differential_20.pdf",
 "2020soln": r"2020\analysis_and_differential_soln_20.pdf",
 "2018": r"2018\analysis2018-individual.pdf",
 "2025": r"2025\analysis.pdf",
}
for k,rel in files.items():
    p = os.path.join(root, rel)
    out.write("#"*90+"\n")
    out.write("## %s exists=%s\n" % (k, os.path.exists(p)))
    try:
        doc = fitz.open(p)
        out.write("pages: %d\n" % doc.page_count)
        for i in range(doc.page_count):
            out.write("---- page %d ----\n" % (i+1))
            out.write(doc[i].get_text())
    except Exception as e:
        out.write("ERR %r\n" % (e,))
out.close()
print("ok")
