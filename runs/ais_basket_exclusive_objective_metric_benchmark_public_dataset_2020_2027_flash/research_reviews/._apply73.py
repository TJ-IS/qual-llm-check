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
   ("然而，这些攻击资源在支撑系统防御研究方面存在明显边界，其具体表现与影响详见 2.4 节与 2.5 节。其一，攻击实例多由静态模板生成，难以随防御升级而自动演化。其二，各基准的攻击格式与成功标准不一，攻击成功与否缺乏统一的真值标注。",
    "然而，这些攻击资源在支撑系统防御研究方面存在明显边界。其一，攻击实例多由静态模板生成，难以随防御升级而自动演化。其二，各基准的攻击格式与成功标准不一。"),
   ("表明生成攻击能够跨仓库情境泛化，可作为防御算法的压力测试资源。",
    "表明生成攻击能够跨仓库情境泛化，可用于防御算法的压力评估。"),
 ],
 '35': [
   ("组织无法对每一个单元都实施隔离与深度扫描，不加区分地防御以任务效用为代价【占位，需核对公开出处】。",
    "组织无法对每一个单元都实施隔离与深度扫描，防御强度与单元风险的错配以任务效用为代价【占位，需核对公开出处】。"),
   ("Qu 等（2026）以 Shapley 值对披露风险做特征级归因，并在风险降低与效用保持的权衡前沿上给出掩蔽特征与噪声水平的选择准则。",
    "Qu 等（2026）以 Shapley 值对披露风险做特征级归因，沿风险与效用的权衡前沿给出特征掩蔽与噪声注入的选择准则。"),
 ],
 '36': [
   ("其启示在于，攻击仿真的质量决定鲁棒化的上限。没有系统生成的攻击，防御评估缺乏压力测试资源。",
    "其启示在于，攻击仿真的质量决定鲁棒化的上限，评估与增强均依赖系统化的攻击来源。"),
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
io.open(os.path.join(DIR, '_apply73_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')