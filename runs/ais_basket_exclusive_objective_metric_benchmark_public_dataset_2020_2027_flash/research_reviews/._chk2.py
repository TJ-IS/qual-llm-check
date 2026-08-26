# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk2.txt','w',encoding='utf-8')
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
texts = {k: io.open(f, encoding='utf-8').read() for k, f in files.items()}
for k in ['34','35','36']:
    body = texts[k].split('## 参考文献')[0]
    cites = re.findall(r'[（(][^）)]*\d{4}[^）)]*[）)]', body)
    out.write(k + ' | 占位:' + str(len(re.findall('【占位', body))) + ' | 引用组:' + str(len(cites)) + '\n')
out.write('\n34 结论关键需求句存在: ' + str('基于这一关键需求' in texts['34']) + '\n')
out.write('34 综合以上文献计数: ' + str(texts['34'].count('综合以上文献')) + '\n')
out.write('34 此外开源SWE计数: ' + str(texts['34'].count('此外，开源编码智能体 SWE-agent')) + '\n')
out.write('34 OWASP括号计数: ' + str(texts['34'].count('（OWASP, 2025【占位，需核对公开出处】）')) + '\n')
out.write('35 终局结果计数: ' + str(texts['35'].count('实现这一终局结果的关键')) + '\n')
out.write('36 终局结果计数: ' + str(texts['36'].count('实现这一终局结果的关键')) + '\n')
out.close()
