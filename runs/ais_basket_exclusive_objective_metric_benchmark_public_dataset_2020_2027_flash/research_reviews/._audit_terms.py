import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
kws = ['通道', '载体', '手法', '操纵单元', '真值', '任务级', '单元级', '风险分', '逐时间步', '通道级', '归因', '攻击面地图', '危害判定', '预期危害', '先验', '预置', '门控', '弱监督', '强监督']
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print(f'========== {n} 术语出现次数 ==========')
    for kw in kws:
        c = len(re.findall(kw, main))
        print(f'  {kw}: {c}')
    print()
