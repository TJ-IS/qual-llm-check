import re
fn = '37_论文v3.1_逐段严格对照重写记录.md'
t = open(fn, encoding='utf-8').read()
# 直引号上下文抽样
idxs = [m.start() for m in re.finditer('"', t)]
print('直引号总数:', len(idxs))
for i in idxs[:6]:
    s = max(0, i-70); e = min(len(t), i+70)
    print('...', t[s:e].replace(chr(10),' '))
    print()
# 半角冒号与破折号上下文
for ch, name in [(':', '半角冒号'), ('—','长破折号'), ('–','中破折号')]:
    for m in list(re.finditer(re.escape(ch), t))[:4]:
        s = max(0, m.start()-70); e = min(len(t), m.end()+70)
        print(f'{name}:', t[s:e].replace(chr(10),' '))
        print()
