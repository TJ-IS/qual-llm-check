import re
f35 = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t35 = open(f35, encoding='utf-8').read()
t36 = open(f36, encoding='utf-8').read()
m = re.search(r'### 3.1 计算设计科学的定位\n(.*?)\n### 3.2', t36, re.S)
print('===== 36 3.1（修改后） =====')
print(m.group(1).strip())
print()
m = re.search(r'### 3.5 方法论挑战\n(.*?)\n## 四、研究问题', t35, re.S)
print('===== 35 3.5（修改后） =====')
print(m.group(1).strip()[:1600])
print()
for kw in ['训练标签来自', '对抗鲁棒性评估资源', '单元级操纵风险作为先验']:
    for fn, label in [(f35,'35'),(f36,'36')]:
        t = open(fn, encoding='utf-8').read()
        for m in re.finditer(re.escape(kw), t):
            s = max(0, m.start()-80); e = min(len(t), m.end()+80)
            print(f'--- {label} {kw}:', t[s:e].replace(chr(10),' '))
            print()
