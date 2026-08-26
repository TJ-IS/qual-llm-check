import re
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
m = re.search(r'### 5.3 融合检测模型\n(.*?)\n### 5.4', main, re.S)
print('===== 36 5.3 融合检测模型 =====')
print(m.group(1).strip()[:4000])
