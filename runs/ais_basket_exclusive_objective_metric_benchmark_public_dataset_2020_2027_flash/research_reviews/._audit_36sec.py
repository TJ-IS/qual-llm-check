import re
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
m = re.search(r'### 5.2 三通道特征提取\n(.*?)\n### 5.3', main, re.S)
print('===== 36 5.2 三通道特征提取 =====')
print(m.group(1).strip()[:3000])
print()
m = re.search(r'## 九、结论与未来研究\n(.*?)\n## 参考文献', main, re.S)
print('===== 36 未来研究（结论节） =====')
print(m.group(1).strip()[-1800:])
