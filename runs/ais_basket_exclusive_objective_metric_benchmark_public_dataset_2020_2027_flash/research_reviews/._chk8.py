# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk8.txt','w',encoding='utf-8')
for k, f in [('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    t = io.open(f, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    out.write(k + ' | 鲁棒性:' + str(body.count('鲁棒性')) + ' | 稳健性:' + str(body.count('稳健性')) + '\n')
    for m in re.finditer(r'[^。]{0,40}稳健性[^。]{0,40}', body):
        out.write('  稳健性句: ' + m.group(0) + '\n')
t36 = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
i = t36.find('这些证据表明，任务执行中的实时检测')
out.write('\n36 2.1 末句上下文:\n' + t36[i-260:i+180] + '\n')
out.close()
