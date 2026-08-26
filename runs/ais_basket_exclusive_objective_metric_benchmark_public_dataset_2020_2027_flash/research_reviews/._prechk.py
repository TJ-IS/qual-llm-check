import re
for n, fn in [
 ('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'),
]:
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print(n, '据我们所知:', len(re.findall('据我们所知', main)), '| 当务之急:', len(re.findall('当务之急', main)))
    for kw in ['同等强度的防御', '不加区分', '逐步生效', '恶意内容在智能体', '植入恶意内容', '恶意内容在任务']:
        c = len(re.findall(kw, main))
        if c: print('   ', kw, c)
