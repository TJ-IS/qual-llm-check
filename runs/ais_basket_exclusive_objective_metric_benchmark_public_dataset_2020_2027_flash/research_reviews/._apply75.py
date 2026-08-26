# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
edits = {
 '34': [
   ('其三，评估基础设施缺口。', '其三，评估真值缺口。'),
   ('最后刻画与交付攻击面（评估基础设施）。', '最后刻画与交付攻击面（评估资源）。'),
   ('AttackRL-Agent 在所有攻击通道与所有智能体基线上显著优于全部基线方法。', 'AttackRL-Agent 在所有攻击通道与智能体基线上显著优于全部基线方法。'),
   ('将有限的预算配置到成功率最高、代价最低的攻击通道。', '将有限的预算配置到防御收益最高的攻击通道。'),
 ],
 '35': [
   ('与哪些特征应被掩码对应，本文回答哪些单元应被隔离、监控或延迟。与噪声水平选择对应，本文回答防御动作强度的选择。', '与哪些特征应被掩码对应，本文回答哪些单元应被隔离、监控或延迟。与噪声水平选择对应，本文确定防御动作的强度。'),
   ('这一评估规范同时回应了防护机制损害正常任务完成率的实证担忧【占位，需核对公开出处】，并与 IS 防御评估的双指标规范一致（Li & Chai, 2022）。', '这一评估规范既回应了防护机制损害正常任务完成率的实证担忧【占位，需核对公开出处】，也与 IS 防御评估的双指标规范一致（Li & Chai, 2022）。'),
 ],
 '36': [
   ('输入侧防护以 guardrail 过滤器为主', '输入侧防护以护栏（guardrail）过滤器为主'),
   ('第一，我们形式化了编码智能体部署中的一个新的且重要的安全管理问题，即流式轨迹上的信息操纵攻击检测与受控门控问题。', '第一，我们提出并形式化了编码智能体部署中的信息操纵攻击检测与受控门控问题。'),
   ('该问题的形式化直接借鉴了 IS 检测文献的多源融合范式', '这一形式化直接借鉴了 IS 检测文献的多源融合范式'),
   ('隔离、降权与放行构成成本递增的规避路径', '隔离、降权与放行构成成本递增的处置层级'),
 ],
}
log = []
allok = True
for k, f in files.items():
    p = os.path.join(DIR, f)
    text = io.open(p, encoding='utf-8').read()
    for old, new in edits.get(k, []):
        c = text.count(old)
        if c != 1:
            allok = False
            log.append('[%s] 匹配 %d 次，未落盘: %s' % (k, c, old[:40]))
            continue
        text = text.replace(old, new)
        log.append('[%s] 已落盘: %s' % (k, old[:44]))
    io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply75_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')

