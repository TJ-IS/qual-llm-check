import re
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
# 风险分 contexts
for kw in ['风险分', '单元级操纵风险', '任务级风险']:
    hits = [m.start() for m in re.finditer(kw, main)]
    print(f'--- {kw} x{len(hits)}')
    for h in hits[:10]:
        s = max(0, h-70); e = min(len(main), h+80)
        print('   ', main[s:e].replace(chr(10),' '))
    print()
# 5.2 section
m = re.search(r'### 5.2 深度攻击面预测器\n(.*?)\n### 5.3', main, re.S)
print('===== 5.2 深度攻击面预测器 =====')
print(m.group(1).strip()[:3500])
