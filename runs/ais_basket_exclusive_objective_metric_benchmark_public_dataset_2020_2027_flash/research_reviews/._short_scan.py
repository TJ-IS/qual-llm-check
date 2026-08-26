# -*- coding: utf-8 -*-
import io, re
for f, tag in [('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','35'),
               ('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','36')]:
    t = io.open(f, encoding='utf-8').read()
    body = t.split('## \u53c2\u8003\u6587\u732e')[0]
    body = re.sub(r'^#{1,4}.*$', '', body, flags=re.M)
    parts = re.split(r'(?<=[\u3002\uff1f\uff01])', body)
    print('====', tag)
    for p in parts:
        s = re.sub(r'\s', '', p)
        if 0 < len(s) < 14 and not s.startswith(('图','表','RQ','【')):
            print('  short(%d): %s' % (len(s), s))
