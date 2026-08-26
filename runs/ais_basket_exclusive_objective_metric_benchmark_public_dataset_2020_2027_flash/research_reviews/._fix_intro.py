import re
edits = {
 '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md': [
  ('面对此类威胁，安全团队缺乏在任务执行前识别风险并预置防御的手段。',
   '面对此类威胁，仅靠任务执行中的运行时防护，难以在危害发生前阻止攻击。'),
 ],
 '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md': [
  ('面对此类威胁，组织缺乏在任务执行中实时识别攻击并联动处置的手段。',
   '面对此类威胁，仅靠输入侧的过滤与静态规则，难以识别在任务执行中逐步生效的攻击。'),
 ],
}
for fn, pairs in edits.items():
    t = open(fn, encoding='utf-8').read()
    for old, new in pairs:
        assert t.count(old) == 1, (fn, old[:20], t.count(old))
        t = t.replace(old, new)
    open(fn, 'w', encoding='utf-8', newline='').write(t)
    print('已修改', fn)
