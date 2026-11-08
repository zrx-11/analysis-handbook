import re, glob, os, sys

ROOT = "/home/user/Doubao/chats/38452582422523394/点化学习系统"
SEC = re.compile(r"^\d{1,2}\s+[\u4e00-\u9fa5][^\d]{0,18}$")


def digest(path, out, width=700):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    chunks = []
    seen = set()
    for i, line in enumerate(lines):
        s = line.strip()
        if len(s) <= 20 and SEC.match(s) and s not in seen:
            seen.add(s)
            body = " ".join(x.strip() for x in lines[i + 1:i + 10] if x.strip())
            chunks.append(f"\n### {s}\n{body[:width]}")
    with open(out, "w", encoding="utf-8") as f:
        f.write("".join(chunks))
    print(out, len("".join(chunks)), "字符")


if __name__ == "__main__":
    for f in sorted(glob.glob(os.path.join(ROOT, "0*", "_work", "raw", "ch*.txt"))):
        book = f.split(os.sep)[-3]
        out = os.path.join(os.path.dirname(f), "digest-" + os.path.basename(f))
        digest(f, out)
