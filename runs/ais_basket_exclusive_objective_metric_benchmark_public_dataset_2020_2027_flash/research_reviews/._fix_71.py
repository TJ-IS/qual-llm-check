import re
edits = {
 '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md': [
  ('IS 预测文献已证明多源信号整合的价值（Wang et al., 2020; Shangguan et al., 2022）与前瞻式决策的有效性（Lin & Fang, 2021; Zhang et al., 2024），IS 优化文献已发展出预算约束下的分配方法（Ray et al., 2021; Wu et al., 2023; Qu et al., 2026），但这些方法的应用对象是医疗、灾害响应、众包与数据治理，其情境结构均不同于编码智能体安全运营。',
   '预测与优化方法已在诸多决策情境中确立先例，但均未涉及编码智能体的事前防御分配。'),
 ],
 '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md': [
  ('IS 检测文献已确立多源信号互补融合的共识（Zhang et al., 2023; Gopal et al., 2022; Benjamin & Raghu, 2023），并已证明外部验证信号的增量检测价值（Lausen et al., 2020）与对抗重训的增强规范（Li & Chai, 2022），但这些方法的应用对象是虚假评论者、欺诈网站与社交机器人，其信号通道与威胁结构均不同于编码智能体的信息操纵攻击。',
   '融合、验证与鲁棒化方法已在诸多检测情境中确立先例，但均未涉及编码智能体的流式信息操纵攻击检测。'),
 ],
}
for fn, pairs in edits.items():
    t = open(fn, encoding='utf-8').read()
    for old, new in pairs:
        assert t.count(old) == 1, (fn, old[:30], t.count(old))
        t = t.replace(old, new)
    open(fn, 'w', encoding='utf-8', newline='').write(t)
    print('已修改', fn)
