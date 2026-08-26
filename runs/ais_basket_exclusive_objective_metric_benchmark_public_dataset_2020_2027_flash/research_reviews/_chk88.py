# -*- coding: utf-8 -*-
import io, glob
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
olds = [
 "攻击面地图以威胁模型的三维分类学为骨架，包括通道维度（问题改写、仓库文件注入、工具描述篡改）、载体维度（自然语言段落、代码文件、配置与元数据、工具与技能描述）与手法维度（改写、注入、篡改、组合）。",
 "由攻击轨迹与原始输入对比自动生成并经人工校验。",
 "标注质量以独立标注者的一致性（Cohen's kappa）评估【占位】。",
]
for o in olds:
    print(t.count(o), o[:20])
