# -*- coding: utf-8 -*-
import io, re
out = io.open('_accept90_out.txt','w',encoding='utf-8')
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
allok = True
for k, f in files.items():
    text = io.open(f, encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    hits = {w: body.count(w) for w in banned if body.count(w)}
    syms = {n: body.count(c) for c, n in [('：','全角冒号'),('；','全角分号'),('—','破折号'),('“','引号'),('”','引号'),('‘','引号'),('’','引号'),('…','省略号'),('→','箭头')] if body.count(c)}
    walls = body.count('Walls')
    ph = len(re.findall('【占位', body))
    groups = re.findall(r'[（(][^）)]*\d{4}[^）)]*[）)]', body)
    cites = sum(len(re.findall(r'\b(1[89]\d{2}|20\d{2})\b', g)) for g in groups)
    refs = text.split('## 参考文献',1)[1]
    n_ref = len([l for l in refs.split('\n') if l.strip() and not l.strip().startswith('#')])
    dsm = body.count('设计科学方法')
    row = f'{k} | 禁词:{hits or "无"} | 符号:{syms or "全零"} | Walls:{walls} | 占位:{ph} | 引用组:{cites} | 参考文献:{n_ref} | 设计科学方法:{dsm}'
    out.write(row + '\n')
    exp = {'34': (64,94), '35': (62,82), '36': (66,83)}
    if ph != exp[k][0] or cites != exp[k][1] or walls != 1 or dsm != 1 or hits or syms:
        allok = False
        out.write('  !! 未达预期\n')
out.write('\n总体: ' + ('通过' if allok else '未通过') + '\n')
out.close()
print('accept90 done')
