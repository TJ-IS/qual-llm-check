# -*- coding: utf-8 -*-
import io, glob, re
jobs = [
 ('dsdl', r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\11058_2023_unlocking-the-power-of-voice-for-financial-risk-prediction-a-theory-d*.md'),
 ('acaa', r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leve*.md'),
]
for tag, pat in jobs:
    fs = glob.glob(pat)
    t = io.open(fs[0], encoding='utf-8').read()
    ms = list(re.finditer(r'^#{1,4}\s*[^\n]*[Ii]ntroduction[^\n]*$', t, flags=re.M))
    print(tag, [m.start() for m in ms])
    if ms:
        start = ms[0].start()
        rest = t[start:]
        m2 = re.search(r'\n#{1,4}\s', rest[10:])
        end = start + 10 + m2.start() if m2 else len(t)
        io.open(f'._audit108_{tag}_intro.txt','w',encoding='utf-8').write(t[start:end])
        print('  saved', end-start)
