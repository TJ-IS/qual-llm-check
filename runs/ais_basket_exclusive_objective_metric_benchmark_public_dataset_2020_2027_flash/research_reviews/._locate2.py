# -*- coding: utf-8 -*-
import io
targets = {
 "35": ["自动修复智能体可被诱导生成带漏洞的补丁","自动修复智能体可被诱导生成带漏洞补丁","现有防御机制存在结构性缺陷","这一中间状态同时满足两个前提"],
 "36": ["现有防护并不充分","自动修复智能体在修复过程中可被诱导生成带漏洞的补丁","现有防护机制存在结构性缺陷","这一中间状态同时满足三个前提"],
}
files = {
 "34": "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
 "35": "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
 "36": "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md",
}
for k, ts in targets.items():
    with io.open(files[k], "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("=====", k)
    for t in ts:
        for i, ln in enumerate(lines):
            if t in ln:
                print(f"  [{i+1}] {ln.strip()[:130]}")
