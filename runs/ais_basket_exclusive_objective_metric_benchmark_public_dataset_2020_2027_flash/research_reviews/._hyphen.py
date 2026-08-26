# -*- coding: utf-8 -*-
import io, re
# 统计 _apply_diff.py 中替换次数
with io.open('._apply_diff.py', encoding='utf-8') as f:
    src = f.read()
n1 = len(re.findall(r'\.replace\(', src))
n2 = len(re.findall(r'replace\(', src))
print('apply_diff replace 调用数:', n1, '(', n2, ')')
# 三篇连字符上下文统计
for k, f in [('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
             ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
             ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    text = io.open(f, encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    words = set()
    for m in re.finditer(r'[A-Za-z0-9πθ_\-]+-[A-Za-z0-9πθ_\-]+', body):
        words.add(m.group(0))
    print(k, '连字符词集合:', sorted(words))
