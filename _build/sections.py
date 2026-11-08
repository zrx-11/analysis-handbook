import re, glob, os

ROOT = "/home/user/Doubao/chats/38452582422523394/点化学习系统"
HEAD = re.compile(r"^\d{1,2}\s+[\u4e00-\u9fa5][^\d]{0,20}$")

for f in sorted(glob.glob(os.path.join(ROOT, "0*", "_work", "raw", "ch*.txt"))):
    print("=====", os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(f)))), os.path.basename(f))
    pages = open(f, encoding="utf-8").read().split("[[PDF p")
    secs = []
    for pg in pages[1:]:
        pg = pg.split("]]", 1)[-1]
        lines = [l.strip() for l in pg.split("\n") if l.strip()]
        if not lines:
            continue
        # 第一行是页眉，通常就是节标题
        cand = lines[0]
        if HEAD.match(cand) and cand not in secs:
            secs.append(cand)
    print("  " + " / ".join(secs))
