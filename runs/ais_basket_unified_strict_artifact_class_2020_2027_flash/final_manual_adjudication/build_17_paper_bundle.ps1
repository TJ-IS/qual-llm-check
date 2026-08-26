$ErrorActionPreference = 'Stop'

$baseDir = 'E:\github\qual-llm-check-IS-utd'
$adjudicationDir = Join-Path $baseDir 'runs\ais_basket_unified_strict_artifact_class_2020_2027_flash\final_manual_adjudication'
$sourceDir = Join-Path $baseDir 'database_fulltext_all'
$inputCsv = Join-Path $adjudicationDir 'final_included_17.csv'
$outputMd = Join-Path $adjudicationDir '17_papers_fulltext_combined.md'

$rows = @(Import-Csv -LiteralPath $inputCsv)
if ($rows.Count -ne 17) {
    throw "Expected 17 included papers, found $($rows.Count)."
}

$utf8Bom = New-Object System.Text.UTF8Encoding($true)
$writer = New-Object System.IO.StreamWriter($outputMd, $false, $utf8Bom)

try {
    $writer.WriteLine('# 17篇严格纳入文献全文合集')
    $writer.WriteLine()
    $writer.WriteLine('本文件按照最终纳入清单拼接17篇本地全文。每篇文章前增加统一书目信息；其后保留原始Markdown全文，包括原始YAML元数据、正文、表格、图片引用与参考文献。')
    $writer.WriteLine()
    $writer.WriteLine('- 筛选范围：AIS Basket，2020–2027')
    $writer.WriteLine('- 实际纳入年份：2020–2025')
    $writer.WriteLine('- 文献数量：17')
    $writer.WriteLine('- 生成日期：2026-08-08')
    $writer.WriteLine()
    $writer.WriteLine('## 目录')
    $writer.WriteLine()

    for ($i = 0; $i -lt $rows.Count; $i++) {
        $row = $rows[$i]
        $writer.WriteLine(('{0}. {1}（{2}，{3}）' -f ($i + 1), $row.title, $row.journal, $row.year))
    }

    for ($i = 0; $i -lt $rows.Count; $i++) {
        $row = $rows[$i]
        $sourcePath = Join-Path $sourceDir $row.source_file
        if (-not (Test-Path -LiteralPath $sourcePath)) {
            throw "Missing source full text: $sourcePath"
        }

        $raw = [System.IO.File]::ReadAllText($sourcePath, [System.Text.Encoding]::UTF8)
        $authorsMatch = [regex]::Match($raw, '(?m)^authors:\s*"(?<value>.*)"\s*$')
        $doiMatch = [regex]::Match($raw, '(?m)^doi:\s*"(?<value>.*)"\s*$')
        $authors = if ($authorsMatch.Success) { $authorsMatch.Groups['value'].Value } else { '原始全文未提供结构化作者字段' }
        $doi = if ($doiMatch.Success) { $doiMatch.Groups['value'].Value } else { '' }

        $writer.WriteLine()
        $writer.WriteLine('---')
        $writer.WriteLine()
        $writer.WriteLine(('## {0}. {1}' -f ($i + 1), $row.title))
        $writer.WriteLine()
        $writer.WriteLine(('- **作者**：{0}' -f $authors))
        $writer.WriteLine(('- **期刊**：{0}' -f $row.journal))
        $writer.WriteLine(('- **年份**：{0}' -f $row.year))
        $writer.WriteLine(('- **DOI**：{0}' -f $doi))
        $writer.WriteLine(('- **Otero ID**：{0}' -f $row.record_id))
        $writer.WriteLine(('- **本地源文件**：`{0}`' -f $row.source_file))
        $writer.WriteLine()
        $writer.WriteLine(('<!-- BEGIN ORIGINAL FULL TEXT: {0} -->' -f $row.record_id))
        $writer.WriteLine()
        $writer.Write($raw.TrimEnd())
        $writer.WriteLine()
        $writer.WriteLine()
        $writer.WriteLine(('<!-- END ORIGINAL FULL TEXT: {0} -->' -f $row.record_id))
    }
}
finally {
    $writer.Dispose()
}

Write-Output "Wrote: $outputMd"
Write-Output "Articles: $($rows.Count)"
