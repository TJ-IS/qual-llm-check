$base = "E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"

function Check-File($fn, $pairs) {
  $t = Get-Content -Raw -Encoding UTF8 (Join-Path $base $fn)
  $ok = $true
  foreach ($p in $pairs) {
    $c = ([regex]::Matches($t,[regex]::Escape($p[0]))).Count
    if ($c -ne 1) { Write-Output ("ERR count=" + $c + " : " + $p[0].Substring(0,[Math]::Min(20,$p[0].Length))); $ok = $false }
    else { $t = $t.Replace($p[0], $p[1]) }
  }
  if ($ok) {
    $body = $t.Split('## 参考文献')[0]
    $banned = @('旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑')
    $bHits = @()
    foreach ($w in $banned) { $cnt = ([regex]::Matches($body,[regex]::Escape($w))).Count; if ($cnt -gt 0) { $bHits += ($w + "=" + $cnt) } }
    $syms = @([string][char]0xFF1A,[string][char]0xFF1B,[string][char]0x2014,[string][char]0x201C,[string][char]0x201D,[string][char]0x2018,[string][char]0x2019,[string][char]0x2026+[string][char]0x2026)
    $sHits = @()
    foreach ($s in $syms) { $cnt = ([regex]::Matches($body,[regex]::Escape($s))).Count; if ($cnt -gt 0) { $sHits += ($s + "=" + $cnt) } }
    Write-Output ($fn.Substring(0,12) + " | 禁词: " + $(if($bHits){$bHits -join ' '}else{'无'}) + " | 符号: " + $(if($sHits){$sHits -join ' '}else{'全零'}) + " | Walls: " + ([regex]::Matches($body,'Walls')).Count + " | 占位符: " + ([regex]::Matches($body,'【占位')).Count)
  }
}

$p35 = @(
  @("随着编码智能体在软件开发组织中的采用日益广泛，问题描述、代码仓库与工具调用共同构成智能体的信息环境，而这一环境中的每一个单元都可能成为攻击者的操纵对象（Jimenez et al., 2024; Yang et al., 2024）。","随着编码智能体在软件开发组织中的采用日益广泛，问题描述、代码仓库与工具调用共同构成智能体的信息环境。这一环境中的每一个单元都可能成为攻击者的操纵对象（Jimenez et al., 2024; Yang et al., 2024）。"),
  @("实现这一终局结果的关键，在于显式利用被现有防御机制忽略的攻击者行为机制。","实现这一目的的关键，在于显式利用被现有防御机制忽略的攻击者行为机制。"),
  @("预测器以问题文本、仓库结构与工具元数据为输入，输出单元级操纵风险与任务级风险分，分配器在给定安全预算下选择隔离、监控或延迟的单元集合以最大化预期危害降低，评估协议则保证工件在对抗输入与效用代价两方面的可靠性。","预测器以问题文本、仓库结构与工具元数据为输入，输出单元级操纵风险与任务级风险分。分配器在给定安全预算下选择隔离、监控或延迟的单元集合，以最大化预期危害降低。评估协议则保证工件在对抗输入与效用代价两方面的可靠性。"),
  @("经由严格评估，我们预期该框架能够显著提升任务级风险筛查与单元级定位性能【占位】，在预算约束下显著降低攻击成功率【占位】，并将正常任务效用损失控制在可接受范围内【占位】。","我们预期，经由严格评估，该框架将显著提升任务级风险筛查与单元级定位性能【占位】，在预算约束下显著降低攻击成功率【占位】，并将正常任务效用损失控制在可接受范围内【占位】。")
)
Check-File "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md" $p35

$p36 = @(
  @("实现这一终局结果的关键，在于显式利用攻击行为在任务执行中留下的可观测证据。","实现这一目的的关键，在于显式利用攻击行为在任务执行中留下的可观测证据。"),
  @("信息操纵理论（information manipulation theory）与担保理论（warranting theory）分别解释了欺骗者为何在沟通中留下可检测的痕迹，以及外部验证信号为何提升信息的检测价值（McCornack, 1992; Walther et al., 2009）。","信息操纵理论（information manipulation theory）解释了欺骗者为何在沟通中留下可检测的痕迹，担保理论（warranting theory）解释了外部验证信号为何提升信息的检测价值（McCornack, 1992; Walther et al., 2009）。"),
  @("三通道特征提取与流式检测输出逐时间步攻击概率与通道级归因，分层动作门控在显式误报约束下将检测结果转化为隔离、降权或放行动作，对抗重训则维持检测器对自适应攻击的鲁棒性。","三通道特征提取与流式检测输出逐时间步攻击概率与通道级归因。分层动作门控在显式误报约束下将检测结果转化为隔离、降权或放行动作。对抗重训则维持检测器对自适应攻击的鲁棒性。"),
  @("经由严格评估，我们预期该框架能够显著提升检测性能【占位】，满足交互式门控的延迟要求【占位】，并将误报与任务效用损失控制在可接受范围内【占位】。","我们预期，经由严格评估，该框架将显著提升检测性能【占位】，满足交互式门控的延迟要求【占位】，并将误报与任务效用损失控制在可接受范围内【占位】。")
)
Check-File "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md" $p36
