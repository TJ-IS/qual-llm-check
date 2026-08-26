# -*- coding: utf-8 -*-
import io, sys, re
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
files = {
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
def is_junk(s):
    if re.search(r'[a-zA-Z]', s):
        return True
    return False
for k, fn in files.items():
    t = open(base+fn, encoding='utf-8').read()
    t = re.sub(r'【[^】]*】', '【】', t)
    c = Counter()
    n = len(t)
    for i in range(n-15):
        s = t[i:i+16]
        if not re.search(r'[\s（），。、：；\u3000]', s[0]) and '。' not in s and '，' not in s and '：' not in s:
            c[s] += 1
    reps = {s:cnt for s,cnt in c.items() if cnt >= 2 and len(set(s)) > 7 and not is_junk(s)}
    seen = set()
    print('====', k)
    for s in sorted(reps, key=lambda x: -len(x)):
        if any(s in v for v in seen): continue
        seen.add(s)
        print(len(s), s, reps[s])
