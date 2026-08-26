$base = "E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"

function Check-File($fn, $old, $new) {
  $t = Get-Content -Raw -Encoding UTF8 (Join-Path $base $fn)
  $c = ([regex]::Matches($t,[regex]::Escape($old))).Count
  if ($c -ne 1) {
    Write-Output ("ERR count=" + $c + " in " + $fn.Substring(0,12))
    $i = $t.IndexOf($old.Substring(0,10))
    Write-Output ("  index=" + $i)
    return
  }
  $t = $t.Replace($old, $new)
  $body = $t.Split('## 参考文献')[0]
  $banned = @('旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑')
  $bHits = @()
  foreach ($w in $banned) { $cnt = ([regex]::Matches($body,[regex]::Escape($w))).Count; if ($cnt -gt 0) { $bHits += ($w + "=" + $cnt) } }
  $syms = @([string][char]0xFF1A,[string][char]0xFF1B,[string][char]0x2014,[string][char]0x201C,[string][char]0x201D,[string][char]0x2018,[string][char]0x2019,[string][char]0x2026+[string][char]0x2026)
  $sHits = @()
  foreach ($s in $syms) { $cnt = ([regex]::Matches($body,[regex]::Escape($s))).Count; if ($cnt -gt 0) { $sHits += ($s + "=" + $cnt) } }
  Write-Output ($fn.Substring(0,12) + " | 禁词: " + $(if($bHits){$bHits -join ' '}else{'无'}) + " | 符号: " + $(if($sHits){$sHits -join ' '}else{'全零'}) + " | Walls: " + ([regex]::Matches($body,'Walls')).Count + " | 占位符: " + ([regex]::Matches($body,'【占位')).Count)
}

$old35 = "（1）核心结论以相对比较报告（预置前后、与基线的差异），不依赖单一绝对数字。（2）主评估使用独立于本文构建的公开基准，本文构建的攻击基准仅作补充压力测试。（3）预测器的核心假设（任务前静态信息可预测攻击面）以小型可行性实验先行验证【占位，二分类 AUC 阈值】，再推进正式版。（4）统计检验与置信区间附于核心结果。（5）分配器的求解质量以整数规划最优解或间隙上界交叉验证，避免启发式结论依赖单一求解路径。"
$new35 = "核心结论以相对比较报告，即预置前后与基线的差异，不依赖单一绝对数字。主评估使用独立于本文构建的公开基准，本文构建的攻击基准仅作补充压力测试。预测器的核心假设，即任务前静态信息可预测攻击面，以小型可行性实验先行验证【占位，二分类 AUC 阈值】，再推进正式版。统计检验与置信区间附于核心结果。分配器的求解质量以整数规划最优解或间隙上界交叉验证，避免启发式结论依赖单一求解路径。"
Check-File "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md" $old35 $new35

$old36 = "（1）结论以相对比较为主，不依赖单一绝对数字。（2）主评估使用独立于本文构建的公开基准（AgentDojo、MalSkillBench），D_att 仅作对抗压力测试与归因真值。（3）检测性能与任务效用双指标报告，效用保持为第一约束。（4）统计显著性检验与置信区间随核心结果一并报告。（5）归因质量的评估以 D_att 操纵单元标注为真值，避免仅依赖主观判断。"
$new36 = "结论以相对比较为主，不依赖单一绝对数字。主评估使用独立于本文构建的公开基准（AgentDojo、MalSkillBench），D_att 仅作对抗压力测试与归因真值。检测性能与任务效用双指标报告，效用保持为第一约束。统计显著性检验与置信区间随核心结果一并报告。归因质量的评估以 D_att 操纵单元标注为真值，避免仅依赖主观判断。"
Check-File "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md" $old36 $new36
