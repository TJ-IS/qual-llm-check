$base = "E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
# 用码点构造字符，避免引号类字符被解析器吃掉
$pairs = @(
 @([char]0x3A,'半角冒号'), @([char]0xFF1A,'全角冒号'), @([char]0x3B,'半角分号'), @([char]0xFF1B,'全角分号'),
 @([char]0x2014,'em破折号'), @([char]0x2013,'en短横'), @('--','双连字符'), @([char]0xFF0D,'全角连字符'),
 @([char]0x201C,'左双引号'), @([char]0x201D,'右双引号'), @([char]0x2018,'左单引号'), @([char]0x2019,'右单引号'),
 @('"','半角双引号'), @("'",'半角单引号'),
 @([char]0x300C,'左直角引'), @([char]0x300D,'右直角引'), @([char]0x300E,'左双直角引'), @([char]0x300F,'右双直角引'),
 @([char]0x300A,'左书名号'), @([char]0x300B,'右书名号'), @([char]0x3008,'左尖括号'), @([char]0x3009,'右尖括号'),
 @([char]0x2026,'省略号'), @([char]0xFF5E,'全角波浪'), @('~','半角波浪'),
 @([char]0x00B7,'间隔号'), @([char]0x2022,'项目符号'), @([char]0x203B,'参考符号'), @([char]0x2192,'箭头'), @([char]0x2190,'左箭头'),
 @([char]0x2460,'圈1'), @([char]0x2461,'圈2'), @([char]0x2462,'圈3'), @([char]0x2474,'括号1'), @([char]0x2488,'数字点')
)
foreach ($fn in @("34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md","35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md","36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md")) {
  $t = Get-Content -Raw -Encoding UTF8 (Join-Path $base $fn)
  $body = $t.Split('## 参考文献')[0]
  Write-Output ("==== " + $fn.Substring(0,12) + " 正文 ====")
  $found = $false
  foreach ($p in $pairs) {
    $c = ([regex]::Matches($body,[regex]::Escape($p[0]))).Count
    if ($c -gt 0) { Write-Output ("  {0} ({1}): {2}" -f $p[1], $p[0], $c); $found = $true }
  }
  if (-not $found) { Write-Output "  无" }
}
