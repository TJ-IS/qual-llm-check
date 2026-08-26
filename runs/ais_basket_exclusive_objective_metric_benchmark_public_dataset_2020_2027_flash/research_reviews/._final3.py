# -*- coding: utf-8 -*-
import io, re
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
print('=== 正文终核 ===')
for k, f in files.items():
    text = io.open(f, encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    hits = [w for w in banned if w in body]
    syms = [n for c, n in [('：','冒号'),('；','分号'),('—','破折号'),('“','引号'),('”','引号'),('‘','引号'),('’','引号')] if c in body]
    refs = text.split('## 参考文献',1)[1]
    n_ref = len([l for l in refs.split('\n') if l.strip() and not l.strip().startswith('#')])
    print(f'{k} | 禁词:{hits or "无"} | 符号:{syms or "全零"} | Walls(正文):{body.count("Walls")} | 参考文献条目约:{n_ref} | 占位:{len(re.findall(chr(12304)+chr(21344), body))}')
print()
print('=== 记录终核 ===')
t39 = io.open('39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md', encoding='utf-8').read()
hits = [w for w in banned if w in t39]
print('记录禁词:', hits or '无', '| 记录含第8节:', '## 8. v3.1' in t39, '| 记录含第8.8节:', '### 8.8' in t39)
