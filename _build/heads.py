import re, glob, os

ROOT = "/home/user/Doubao/chats/38452582422523394/点化学习系统"
for f in sorted(glob.glob(os.path.join(ROOT, "0*", "_work", "raw", "ch*.txt"))):
    print("=====", os.path.relpath(f, ROOT))
    heads = []
    for line in open(f, encoding="utf-8"):
        s = line.strip()
        if re.match(r"^\d{1,2}\s+\S", s) and len(s) < 40:
            heads.append(s)
    uniq = []
    for h in heads:
        if not uniq or uniq[-1] != h:
            uniq.append(h)
    print(" | ".join(uniq[:30]))
