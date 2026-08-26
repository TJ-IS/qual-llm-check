# -*- coding: utf-8 -*-
import io, glob, re
for pat in ['11058_2023*', '28706_2024*']:
    fs = glob.glob(r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\\' + pat)
    for f in fs:
        t = io.open(f, encoding='utf-8').read()
        title = re.search(r'title: "([^"]+)"', t)
        print(f.split(chr(92))[-1][:80], '|', title.group(1) if title else '?', '| len', len(t))
