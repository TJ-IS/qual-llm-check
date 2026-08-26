# -*- coding: utf-8 -*-
import io, re
out = io.open('_ctx_out2.txt','w',encoding='utf-8')
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for k, f in files.items():
    text = io.open(f, encoding='utf-8').read()
    out.write('### '+k+' 第八章标题\n')
    for m in re.finditer(r'^#{2,4} 8\.[0-9][^\n]*\n', text, re.M):
        out.write(m.group(0))
    # 找(1)...(5)编号列表
    m = re.search(r'（1）评估以相对比较为主[^#]{0,900}', text)
    if m: out.write('### '+k+' 8.3列表原文\n'+m.group(0)+'\n')
    m = re.search(r'（1）核心结论以相对比较报告[^#]{0,900}', text)
    if m: out.write('### '+k+' 8.3列表原文\n'+m.group(0)+'\n')
    m = re.search(r'（1）结论以相对比较为主[^#]{0,900}', text)
    if m: out.write('### '+k+' 8.3列表原文\n'+m.group(0)+'\n')
out.close()
