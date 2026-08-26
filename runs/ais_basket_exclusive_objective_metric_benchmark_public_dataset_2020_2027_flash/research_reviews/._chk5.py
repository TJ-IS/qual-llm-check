# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk5.txt','w',encoding='utf-8')
t34 = io.open('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md', encoding='utf-8').read()
t35 = io.open('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()

# 1. ARText 引用
for m in re.finditer(r'ARText[^。]{0,120}', t36):
    out.write('36 ARText 上下文: ' + m.group(0).replace('\n',' ') + '\n')
# 是否有 ARText 年份
out.write('36 ARText 后同句含年份: ' + str(bool(re.search(r'ARText[^。]*?\d{4}', t36))) + '\n\n')

# 2. 35 重复短语
out.write('35 任务开始前可获得的静态信号未被系统利用 计数: ' + str(t35.count('任务开始前可获得的静态信号未被系统利用')) + '\n')
out.write('35 分配策略的设计直接决定权衡质量 计数: ' + str(t35.count('分配策略的设计直接决定权衡质量')) + '\n\n')

# 3. 三篇第二章章首段
for k, t in [('34', t34), ('35', t35), ('36', t36)]:
    m = re.search(r'## 二、文献综述与研究缺口\n\n(.*?)(?=\n### 2\.1)', t, re.S)
    out.write(k + ' 章首: ' + m.group(1).strip().replace('\n',' ') + '\n\n')

# 4. 叙述式引用统计
for k, t in [('34', t34), ('35', t35), ('36', t36)]:
    body = t.split('## 参考文献')[0]
    narr = len(re.findall(r'[A-Z][A-Za-z]+ 等（\d{4}）', body))
    par = len(re.findall(r'（[^）]*[A-Z][A-Za-z]+ et al\., \d{4}', body))
    out.write(k + ' | 叙述式等（年份）:' + str(narr) + ' | 括号式 et al.:' + str(par) + '\n')
out.close()
