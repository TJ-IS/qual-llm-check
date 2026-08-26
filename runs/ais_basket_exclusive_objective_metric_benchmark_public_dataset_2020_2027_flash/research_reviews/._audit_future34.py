import re
fn = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
for kw in ['研究二', '研究三', '未来研究', '事前预判', '事中检测']:
    hits = [m.start() for m in re.finditer(kw, main)]
    print(f'--- {kw} x{len(hits)}')
    for h in hits:
        s = max(0, h-90); e = min(len(main), h+110)
        print('   ', main[s:e].replace(chr(10),' '))
        print()
