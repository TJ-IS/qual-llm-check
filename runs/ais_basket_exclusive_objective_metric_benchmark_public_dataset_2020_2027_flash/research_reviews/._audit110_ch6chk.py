# -*- coding: utf-8 -*-
import io, re
t = io.open('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md', encoding='utf-8').read()
m = re.search(r'^## 六、[^\n]*\n(.*?)^## 七、', t, flags=re.M|re.S)
ch6 = m.group(1)
finds = re.findall(r'预期发现[一二三四五六七八九十]+（[^）]+）', ch6)
print('预期发现序列:')
for f in finds:
    print('  ', f)
print()
print('ch6 字数:', len(ch6))
# 检查是否有引用旧编号的残余
for pat in ['预期发现四（标注质量）', '预期发现五（攻击面覆盖）', '预期发现六（迁移性）']:
    print(pat, '残留:', ch6.count(pat))
