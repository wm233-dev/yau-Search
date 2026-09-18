
import fitz, os, re
BASE = r"sources/finals\2012-2025Applied Math and Computational Math"
targets = []
for root, dirs, files in os.walk(BASE):
    for fn in files:
        if "2020" in fn and fn.lower().endswith(".pdf"):
            targets.append(os.path.join(root, fn))
for p in targets:
    print("=" * 80)
    print(os.path.basename(p))
    try:
        d = fitz.open(p)
        print("  needs_pass:", d.needs_pass, "pages:", d.page_count)
        for pw in ["Yau-ACM20", "Yau-ACM20)", "YauACM20", "yau-acm20"]:
            rc = d.authenticate(pw)
            print("   try", repr(pw), "->", rc)
            if rc:
                tot = 0
                for i in range(d.page_count):
                    t = d[i].get_text() or ""
                    tot += len(t)
                print("   AUTHENTICATED pages=%d chars=%d" % (d.page_count, tot))
                break
        d.close()
    except Exception as e:
        print("  ERR", e)
