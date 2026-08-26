# -*- coding: utf-8 -*-
import io, re
for k, f in [('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
             ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    text = io.open(f, encoding='utf-8').read()
    refs = text.split('## 参考文献', 1)[1]
    print('='*15, k, '参考文献区冒号上下文（前6处）')
    for m in list(re.finditer(r':', refs))[:6]:
        s = max(0, m.start()-50); e = min(len(refs), m.end()+30)
        print('  ...', refs[s:e].replace('\n',' '), '...')
    print(' Greshake 正文出现次数:', text.split('## 参考文献')[0].count('Greshake'))
