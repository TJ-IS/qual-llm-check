import re
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
for kw in ['研究一', '研究二', '研究三', 'D_att', 'AgentShield-Anticipate', '风险分']:
    hits = [m.start() for m in re.finditer(kw, main)]
    print(f'--- {kw} x{len(hits)}')
    for h in hits:
        s = max(0, h-90); e = min(len(main), h+110)
        print('   ', main[s:e].replace(chr(10),' '))
        print()
