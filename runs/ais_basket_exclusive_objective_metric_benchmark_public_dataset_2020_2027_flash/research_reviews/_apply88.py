# -*- coding: utf-8 -*-
import io, glob
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
pairs = [
 ("攻击面地图以威胁模型的三维分类学为骨架，包括通道维度（问题改写、仓库文件注入、工具描述篡改）、载体维度（自然语言段落、代码文件、配置与元数据、工具与技能描述）与手法维度（改写、注入、篡改、组合）。",
  "攻击面地图以威胁模型为骨架，将攻击证据按通道、载体与手法三个维度组织为分类学单元。通道维度对应问题描述、仓库文件以及工具与技能描述。载体维度刻画通道内被操纵的内容位置，包括自然语言段落、代码文件、配置与元数据以及工具与技能描述。手法维度记录操纵方式，包括改写、注入、篡改与组合。"),
 ("由攻击轨迹与原始输入对比自动生成并经人工校验。",
  "由攻击输入与原始输入的差异自动生成并经人工校验。"),
 ("标注质量以独立标注者的一致性（Cohen's kappa）评估【占位】。",
  "标注质量以独立标注者在抽样实例上的标注一致性（Cohen's kappa）评估【占位】。"),
]
for old, new in pairs:
    n = t.count(old)
    assert n == 1, (old[:25], n)
    t = t.replace(old, new)
io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("ok")
