
import fitz, os, io
BASE = r"F:\丘成桐大学生数学竞赛历年总决赛真题\2012-2025Applied Math and Computational Math"
OUT = r"E:\deepseek_exclusive\math\.tmp\burn2026\scripts\_finals_2020"
os.makedirs(OUT, exist_ok=True)
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        if "2020" not in fn or not fn.lower().endswith(".pdf"):
            continue
        p = os.path.join(root, fn)
        d = fitz.open(p)
        d.authenticate("Yau-ACM20")
        parts = []
        for i in range(d.page_count):
            parts.append("\n=== page %d ===\n" % (i + 1))
            parts.append(d[i].get_text() or "")
        d.close()
        txt = "".join(parts)
        safe = fn[:-4].replace(" ", "_")
        io.open(os.path.join(OUT, safe + ".txt"), "w", encoding="utf-8").write(txt)
        print("#" * 88)
        print("### FILE:", fn, "pages", txt.count("=== page"), "chars", len(txt))
        print("#" * 88)
        print(txt)
