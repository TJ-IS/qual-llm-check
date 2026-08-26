# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk3.txt','w',encoding='utf-8')
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for k, f in files.items():
    body = io.open(f, encoding='utf-8').read().split('## 参考文献')[0]
    groups = re.findall(r'[（(][^）)]*\d{4}[^）)]*[）)]', body)
    n_year = sum(len(re.findall(r'\b(1[89]\d{2}|20\d{2})\b', g)) for g in groups)
    n_group = len(groups)
    out.write(f'{k} | 组:{n_group} | 组内年份总数:{n_year}\n')
    # 34 删除S6后应减少: Ebrahimi2025, Kwon&Lee2024, Ghoshal2020, Menon2022
    if k == '34':
        s6 = '此外，IS 文献虽然已确立以强化学习开发攻击侧工件的范式（Ebrahimi et al., 2025; Kwon & Lee, 2024），以及数据操纵与数据效用权衡的分析框架（Ghoshal et al., 2020; Menon et al., 2022），但这些范式与框架均未在编码智能体情境中得到整合。'
        out.write('S6 组内年份数: ' + str(sum(len(re.findall(r'\b(1[89]\d{2}|20\d{2})\b', g)) for g in re.findall(r'[（(][^）)]*\d{4}[^）)]*[）)]', s6))) + '\n')
out.close()
