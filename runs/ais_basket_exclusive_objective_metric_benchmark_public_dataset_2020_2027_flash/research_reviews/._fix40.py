# -*- coding: utf-8 -*-
import io
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\40_引言逐段逐句二轮审计与模板对照改写记录.md"
t = io.open(fn, encoding="utf-8").read()
old = """w| S1 现有防护机制具有结构性缺陷 | 缺陷总起，与 35 P2 S1 系列平行（相似度 0.786） | 无 | 达标 |\nw| S2 其作用时点集中于输入时刻，以输入过滤与静态规则为主，忽视了任务执行过程中产生的行为证据 | 时点缺陷 | Yang et al., 2024 | 达标 |\nw| S3 事实上，信息操纵攻击具有流式特性 | 流式特性 | 无 | 达标 |\nw| S4 恶意内容在智能体逐步读取与执行的过程中逐步生效 | 流式展开 | 无 | 达标 |\nw| S5 其一，语义盲区 | First，对应 ARText P3 | 【占位】 | 达标 |\nw| S6 其二，信号单一 | Second | Yang et al., 2024 | 达标 |\nw| S7 其三，鲁棒性缺位 | Third | Li & Chai, 2022 | 达标 |\nw| S8 尽管编码智能体部署日益依赖运行时防护，如何在任务执行中实时识别攻击、以受控误报联动处置、并保持检测器自身的鲁棒性，目前知之甚少 | 知之甚少，对应 RADAR P2 S15 | 无 | 达标 |\n"""
new = """w| S1 现有防护机制具有结构性缺陷 | 缺陷总起，与 35 P2 S1 系列平行（相似度 0.786） | 无 | 达标 |\nw| S2 其作用时点集中于输入时刻，以输入过滤与静态规则为主，忽视了任务执行过程中产生的行为证据 | 时点缺陷 | Yang et al., 2024 | 达标 |\nw| S3 事实上，信息操纵攻击具有流式特性 | 流式特性 | 无 | 达标 |\nw| S4 恶意内容在智能体逐步读取与执行的过程中逐步生效，部分攻击只有在智能体运行时读取对应工具时才触发 | 流式展开 | 无 | 达标 |\nw| S5 其一，语义盲区 | First 标签 | 无 | 达标 |\nw| S6 主流防护依赖黑盒大语言模型过滤器或静态规则，对间接注入与新型攻击漏报率高 | First 展开，对应 ARText P3 | 【占位】 | 达标 |\nw| S7 其二，信号单一 | Second 标签 | 无 | 达标 |\nw| S8 现有检测以规则与静态分析为主，不利用行为轨迹与调用图结构信号 | Second 展开 | Yang et al., 2024 | 达标 |\nw| S9 其三，鲁棒性缺位 | Third 标签 | 无 | 达标 |\nw| S10 检测器自身的对抗鲁棒性鲜有报告，攻击者可以针对检测规则构造规避样本 | Third 展开 | Li & Chai, 2022 | 达标 |\nw| S11 尽管编码智能体部署日益依赖运行时防护，如何在任务执行中实时识别攻击、以受控误报联动处置、并保持检测器自身的鲁棒性，目前知之甚少 | 知之甚少，对应 RADAR P2 S15 | 无 | 达标 |\n"""
if old in t:
    t = t.replace(old, new)
    io.open(fn, "w", encoding="utf-8", newline="").write(t)
    print("36 P2 section fixed")
else:
    print("NOT FOUND - check raw content")
    i = t.find("### 4.2")
    print(t[i:i+1500])