# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
terms = ['仓库投毒','工具投毒','问题改写','仓库文件注入','工具描述篡改','文本伪装','仓库投递']
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    print('='*10, n, '='*10)
    for w in terms:
        for m in re.finditer(w, body):
            print(f'  {w}: {body[max(0,m.start()-30):m.end()+20].replace(chr(10)," ")}')
