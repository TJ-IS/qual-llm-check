# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk6.txt','w',encoding='utf-8')
t36 = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
body = t36.split('## 参考文献')[0]
refs = t36.split('## 参考文献')[1]
# ARText 出现次数
out.write('36 正文 ARText 计数: ' + str(body.count('ARText')) + '\n')
for m in re.finditer(r'[^。]{0,60}ARText[^。]{0,120}。', body):
    out.write('  ARText 句: ' + m.group(0).replace('\n',' ') + '\n')
# 参考文献中鲁棒性相关条目（含鲁棒/robust 或 25465）
for m in re.finditer(r'^\s*\[(\d+)\][^\n]*', refs, re.M):
    line = m.group(0)
    if any(w in line for w in ['Chai','Li','鲁棒','Robust','Yuan','Zhou','Liang']):
        out.write('REF: ' + line.strip()[:150] + '\n')
out.close()
