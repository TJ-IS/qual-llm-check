# -*- coding: utf-8 -*-
import io, re, difflib

files = [
 "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
 "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
 "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md",
]
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
sym_map = {"：":"全角冒号","；":"中文分号","—":"破折号","—":"破折号","“":"中文引号","”":"中文引号","‘":"中文引号","’":"中文引号"}

for fname in files:
    with io.open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    # 正文区（参考文献之前）
    body = text.split("## 参考文献")[0]
    hits = {}
    for w in banned:
        c = body.count(w)
        if c: hits[w] = c
    print("==", fname[:14])
    print(" 禁词:", hits if hits else "无")
    syms = {}
    for ch, name in sym_map.items():
        c = body.count(ch)
        if c: syms[name] = c
    print(" 正文符号:", syms if syms else "全零")
    print(" Walls:", body.count("Walls"))
    # 占位符数量
    print(" 占位符:", len(re.findall(r"【占位", body)))

# 39号记录禁词
with io.open("39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md", "r", encoding="utf-8") as f:
    t39 = f.read()
for w in banned:
    c = t39.count(w)
    if c:
        idx = t39.find(w)
        print("39号记录禁词:", w, c, "处; 上下文:", t39[max(0,idx-30):idx+30].replace("\n"," "))
