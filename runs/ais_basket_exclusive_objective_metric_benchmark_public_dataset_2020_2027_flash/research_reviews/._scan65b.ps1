$base = "E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
$pairs = @(
 @([char]0xFF1A,'全角冒号'), @([char]0xFF1B,'全角分号'), @([char]0x2014,'em破折号'), @([char]0x2013,'en短横'),
 @([char]0x201C,'左双引号'), @([char]0x201D,'右双引号'), @([char]0x2018,'左单引号'), @([char]0x2019,'右单引号'),
 @([char]0x300C,'左直角引'), @([char]0x300D,'右直角引'), @([char]0x2026,'省略号'), @([char]0x2192,'箭头')
)
$files = Get-ChildItem -Path $base -File -Filter "*.md" | Where-Object { $_.Name -match '^\d+_' } | Sort-Object Name
foreach ($f in $files) {
  $t = Get-Content -Raw -Encoding UTF8 $f.FullName
  $hits = @()
  foreach ($p in $pairs) {
    $c = ([regex]::Matches($t,[regex]::Escape($p[0]))).Count
    if ($c -gt 0) { $hits += ("{0}={1}" -f $p[1], $c) }
  }
  if ($hits.Count -gt 0) { Write-Output ("{0}: {1}" -f $f.Name, ($hits -join ' ')) }
}
