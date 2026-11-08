#!/usr/bin/env python3
"""按章切分三本 PDF 的文本，输出到各书 _work/raw/chNN.txt，并打印结构地图。"""
import os
import re
import sys
import pymupdf

BOOKS = [
    ("01-分析I", "分析 I (Herbert Amann  Joachim Escher) (z-library.sk, 1lib.sk, z-lib.sk).pdf", range(1, 6)),
    ("02-分析II", "分析 II (Herbert Amann  Joachim Escher) (z-library.sk, 1lib.sk, z-lib.sk).pdf", range(6, 9)),
    ("03-分析III", "分析 III (Herbert Amann  Joachim Escher) (z-library.sk, 1lib.sk, z-lib.sk).pdf", range(9, 13)),
]
ATT = "/home/user/.doubao/agent_mode/workspace/.sessions/38452582422523394/attachments"
ROOT = "/home/user/Doubao/chats/38452582422523394/点化学习系统"

HEAD = re.compile(r"^第\s*(\d+)\s*章\s*(.+?)\s*$")


def first_lines(text, k=3):
    return [l.strip() for l in text.split("\n") if l.strip()][:k]


def main():
    for sub, fname, chapters in BOOKS:
        doc = pymupdf.open(os.path.join(ATT, fname))
        pages = [p.get_text("text") for p in doc]
        starts = {}
        for idx, t in enumerate(pages):
            fl = first_lines(t, 2)
            if not fl:
                continue
            m = HEAD.match(fl[0])
            if m and int(m.group(1)) in chapters:
                ch = int(m.group(1))
                # 章首页正文通常紧随其后有"第 N 章"标题与章节内容，排除目录页（页码点线）
                if ".." in t and t.count("..") > 20:
                    continue
                starts.setdefault(ch, (idx, m.group(2)))
        print(f"== {sub}")
        ordered = []
        for ch in chapters:
            if ch not in starts:
                print(f"  !! 未找到第 {ch} 章起始页")
                continue
            start, title = starts[ch]
            ordered.append((ch, start, title))
            print(f"  第{ch}章 {title} -> PDF p{start + 1}")
        for i, (ch, start, title) in enumerate(ordered):
            end = ordered[i + 1][1] if i + 1 < len(ordered) else len(pages)
            body = "\n\n".join(
                f"[[PDF p{j + 1}]]\n{pages[j]}" for j in range(start, end))
            out = os.path.join(ROOT, sub, "_work", "raw", f"ch{ch:02d}.txt")
            with open(out, "w", encoding="utf-8") as f:
                f.write(f"# 第 {ch} 章 {title}\n\n" + body)
            print(f"    ch{ch:02d}: p{start + 1}-{end}  {len(body)} 字符")
        doc.close()


if __name__ == "__main__":
    main()
