
import importlib
for m in ["numpy","sympy","mpmath","scipy","fitz"]:
    try:
        mod = importlib.import_module(m)
        print(m, "OK", getattr(mod,"__version__","?"))
    except Exception as e:
        print(m, "MISSING", type(e).__name__)
import sys
print(sys.version)
