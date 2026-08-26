# -*- coding: utf-8 -*-
import io
fn = "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()

reps = [
 ("随机基线包括随机改写。学习式基线包括 RLbreaker【占位，需核对公开出处】。",
  "随机基线包括随机改写，即不经过任何学习地对输入进行随机修改。学习式基线包括 RLbreaker【占位，需核对公开出处】。"),
 ("本文使用三类评估指标。攻击成功率（attack success rate, ASR）指攻击导致智能体产出漏洞补丁或执行有害动作的回合比例。隐蔽性指标包括平均编辑成本与公开检测基线的检测率【占位】。攻击面覆盖度指成功攻击覆盖的分类学单元比例。核心结论以相对比较报告，并附统计显著性检验与置信区间【占位】。",
  "本文使用三类评估指标。攻击成功率（attack success rate, ASR）定义为成功攻击回合数与总回合数之比，其中成功攻击回合指攻击导致智能体产出漏洞补丁或执行有害动作的回合。隐蔽性指标包括平均编辑成本与公开检测基线的检测率【占位】。攻击面覆盖度指成功攻击覆盖的分类学单元比例，用于检验生成攻击是否覆盖威胁模型定义的空间，是 D_att 支撑防御算法系统评估的前提。核心结论以相对比较报告。每个实验重复【占位】次并报告平均结果，附统计显著性检验与置信区间【占位】。"),
 ("任务基座采用公开编码基准的真实问题与补丁对【占位，需核对公开出处】。智能体基座采用公开可用的编码智能体配置，包括基线模型与默认工具集。",
  "任务基座采用公开编码基准的真实问题与补丁对【占位，需核对公开出处】。任务按仓库划分为训练集与评估集，评估集仓库不参与攻击策略训练，以支持跨仓库泛化检验并避免评估偏差（Pendlebury et al., 2019）。智能体基座采用公开可用的编码智能体配置，包括基线模型与默认工具集。"),
 ("此外，AttackRL-Agent 在能够处理内容操纵离散动作空间的学习式替代方法中同样胜出，表明其在大型仓库状态空间上的建模能力是实现这一结果的关键【占位】。",
  "此外，在与能够处理内容操纵离散动作空间的学习式基线 RLbreaker 的比较中，AttackRL-Agent 同样胜出，表明其在大型仓库状态空间上的建模能力是实现这一结果的关键【占位】。"),
 ("其二，攻击面地图在通道与载体维度上的覆盖度。",
  "其二，攻击面地图在通道、载体与手法维度上的覆盖度。"),
]
for old, new in reps:
    assert t.count(old) == 1, "NOT UNIQUE or MISSING: " + old[:30]
    t = t.replace(old, new)

# 新增参考文献 [29] Pendlebury et al., 2019，插入到 OWASP 条目之后、注之前
ref_old = "[28] OWASP. (2025). *OWASP Top 10 for LLM Applications 2025*. Open Worldwide Application Security Project. 【占位，需核对公开出处】"
assert t.count(ref_old) == 1
ref_new = ref_old + "\n\n[29] Pendlebury, F., Pierazzi, F., Jordaney, R., Kinder, J., & Cavallaro, L. (2019). TESSERACT: Eliminating experimental bias in malware classification across space and time. In *Proceedings of the 28th USENIX Security Symposium*, 729-746."
t = t.replace(ref_old, ref_new)

io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply89 done, %d replacements" % len(reps))
