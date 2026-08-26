# -*- coding: utf-8 -*-
import io, glob
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
pairs = [
 ("框架以三个现实假设为基础。",
  "框架以三个现实假设为基础，其内容源自 3.2 节威胁模型与既有攻击证据。"),
 ("奖励函数 R 定义为 r_t = harm(traj) − κ·cost(a_t)，其中 harm(·) 为危害信号（智能体产出漏洞补丁或执行有害动作时为 1，被拒绝或行为正常时为 0），cost(a_t) 为编辑成本（修改幅度，用于约束攻击的隐蔽性），κ 为权衡系数。",
  "奖励函数 R 定义为 r_t = harm(traj_t) − κ·cost(a_t)，其中 harm(·) 为截至当前时间步的累积危害信号，由过程级塑形项与任务级判定项构成。过程级塑形项检测越权读取、危险命令执行等中间行为并给予密集奖励（详见 5.3 节），任务级判定项在智能体产出漏洞补丁或执行有害动作后取 1，被拒绝或行为正常时取 0。cost(a_t) 为编辑成本（修改幅度，用于约束攻击的隐蔽性），κ 为权衡系数。"),
]
for old, new in pairs:
    n = t.count(old)
    assert n == 1, (old[:30], n)
    t = t.replace(old, new)
io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("ok")
