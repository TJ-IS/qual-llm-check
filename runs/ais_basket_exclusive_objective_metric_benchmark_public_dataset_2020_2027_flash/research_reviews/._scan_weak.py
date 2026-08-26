# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
weak = ['值得注意的是','需要指出','事实上','显然','本质上','可以看出','不难发现','显而易见','众所周知',
        '具有重要意义','重要的实践意义','重要价值','值得关注','值得注意','由此可见','因此，本文','为此，本文',
        '具体而言','也就是说','换句话说','进一步地','进一步，','整体而言','总的来说','总而言之','归根结底',
        '我们认为','我们认为，','可以说','所谓','的所谓','的缺位','缺乏对','尚未有','鲜有','甚少']
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    print('='*12, n, '='*12)
    total = 0
    for w in weak:
        c = body.count(w)
        if c:
            total += c
            print(f'  {w}: {c}')
    print('  TOTAL weak:', total)
