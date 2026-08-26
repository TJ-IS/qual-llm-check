import re
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
for kw in ['Hevner', 'Yang']:
    for m in re.finditer(kw, main):
        s = max(0, m.start()-80); e = min(len(main), m.end()+80)
        print(f'--- {kw} @ {m.start()}:')
        print('   ', main[s:e].replace(chr(10),' '))
