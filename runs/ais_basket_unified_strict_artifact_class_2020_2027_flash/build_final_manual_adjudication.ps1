$ErrorActionPreference = 'Stop'

$runDir = 'E:\github\qual-llm-check-IS-utd\runs\ais_basket_unified_strict_artifact_class_2020_2027_flash'
$sourceCsv = Join-Path $runDir 'output_full_v3\decisions.csv'
$outputDir = Join-Path $runDir 'final_manual_adjudication'
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$audit = @{
    '1504'  = @{ decision = 'include'; code = ''; reason = '核心终点是系统日志中的知识共享行为；作者实际改造并运行KMS游戏化反馈组件，且贡献形成面向KMS游戏化设计的可复用机制。' }
    '1946'  = @{ decision = 'include'; code = ''; reason = '核心终点是真实点击率；作者实际修改位置广告应用的距离显示与排序界面，贡献明确面向位置广告应用的界面设计。' }
    '5112'  = @{ decision = 'include'; code = ''; reason = '核心终点是实际钓鱼点击；作者构建并现场运行游戏化安全培训系统，并提出可复用的SETA系统设计原则。' }
    '6738'  = @{ decision = 'include'; code = ''; reason = '核心终点是RFID记录的骑行天数；作者在运行平台中修改徽章、分享奖励与完成逻辑，结论面向徽章式游戏化系统设计。' }
    '8352'  = @{ decision = 'include'; code = ''; reason = '核心终点是自动评分的学习成绩；作者实现弱项检测、知识地图与调度引擎，形成电子学习系统的类级设计知识。' }
    '9230'  = @{ decision = 'include'; code = ''; reason = '欺诈标签具有外部事实依据，核心终点是检测性能与对抗鲁棒性；理论被转译为欺诈检测系统的设计原则和运行组件。' }
    '10556' = @{ decision = 'include'; code = ''; reason = '核心终点是事件解释、情境化和可视化延迟及固定规则下的正确性；AIC应急DSS实际运行，架构、元模型与规则机制可复用。' }
    '11292' = @{ decision = 'exclude'; code = 'HUMAN_SEMANTIC_JUDGMENT'; reason = '所谓正确性并非外部事实标签：专家需判断用户回答是否提供“恰当证据”，相关性、可信性和可操作性也依赖语义评价；F1/准确率不能使其客观化。' }
    '11474' = @{ decision = 'include'; code = ''; reason = '核心终点由眼动仪直接记录并确定性计算；作者实现实时眼动追踪和个性化视觉反馈，贡献为注意型仪表盘的设计原则与架构。' }
    '12330' = @{ decision = 'include'; code = ''; reason = '核心终点是评分时延、误报/漏报和完成率；运行系统以任务XML状态进行确定性评分，并形成大规模数字技能反馈系统的元需求和设计原则。' }
    '13398' = @{ decision = 'exclude'; code = 'HUMAN_SEMANTIC_JUDGMENT'; reason = 'PICO句子/片段标签由系统综述专家创建并核验，目标类别是语义角色而非脱离专家解释成立的外部事实；计算F1不能通过客观性门槛。' }
    '13598' = @{ decision = 'include'; code = ''; reason = '核心终点为任务正确性、完成效率和基于最短导航路径计算的透明交互；作者运行会话式仪表盘并形成该类仪表盘的设计理论。' }
    '14428' = @{ decision = 'include'; code = ''; reason = '勒索软件/合法程序是外部事实类别；作者实现并运行Windows保护应用，包含监听、FSM决策、告警和阻断等完整可复用系统机制，而非离线分类器包装。' }
    '14444' = @{ decision = 'exclude'; code = 'THEORY_OR_EXPLANATION_PRIMARY'; reason = '错误数只是ADR项目中证明交换合同合规性的评价证据；研究问题、主要贡献和结论着眼于数字制度化过程及其制度理论，而非以客观指标提升为最终制品贡献。' }
    '15528' = @{ decision = 'exclude'; code = 'ALGORITHM_OR_ANALYTICAL_METHOD'; reason = '论文贡献明确是自动发现BPS模型的方法、新相似度度量和超参数优化；Simod只是该分析方法的开源实现，删除工具外壳后仍是同一方法贡献。' }
    '16324' = @{ decision = 'exclude'; code = 'THEORY_OR_EXPLANATION_PRIMARY'; reason = '研究问题和贡献旨在解释AR相对手机如何经由注意力影响绩效及其边界条件；AR/手机是实验处理，论文没有把所做修改贡献为一类软件制品的设计。' }
    '16782' = @{ decision = 'exclude'; code = 'SUBJECTIVE_CONSTRUCT_WITH_FIXED_LABELS'; reason = 'F1衡量的是克隆对个人偏好、偏差和判断的复刻，目标标签不能脱离人的价值与偏好成立；“责任/韧性”也不是由完全客观的最终指标独立确证。' }
    '19644' = @{ decision = 'exclude'; code = 'DOMAIN_METHOD_NOT_ARTIFACT_CLASS'; reason = '核心贡献是道路标志众包更新中的聚类、负观测和置信度融合方法；云平台是计算与验证载体，未形成面向一类可运行软件产品的独立设计贡献。' }
    '19756' = @{ decision = 'exclude'; code = 'OPTIMIZER_WRAPPED_AS_DSS'; reason = '核心贡献是飞机维护约束下的调度优化模型；数据库、GUI和DSS命名只是领域求解器外壳，删除外壳后贡献完整保留为同一优化方案。' }
    '25465' = @{ decision = 'include'; code = ''; reason = '核心终点是事实标签下的预测性能与对抗鲁棒性；作者提出面向预测分析应用的设计框架，并在ARText运行制品中实例化。' }
    '25791' = @{ decision = 'include'; code = ''; reason = '核心终点是沟通任务时间与错误数；作者实现上下文感知AAC系统，并将机制抽象为可复用的AAC设计原则。' }
    '28035' = @{ decision = 'include'; code = ''; reason = '最终设计成败由点击、完成观看、观看时长及线上经济结果判断；问卷只验证中间画像，推荐组件在生产系统运行且贡献面向意外推荐系统。' }
    '28109' = @{ decision = 'exclude'; code = 'MIXED_CORE_OUTCOMES'; reason = '客观披露、匹配和消息数是重要结果，但文章同时以主观隐私担忧下降来证明“隐私增强”这一标题、设计目标和核心贡献；并非所有核心成功终点都完全客观。' }
    '28352' = @{ decision = 'include'; code = ''; reason = '核心终点是可复算的推荐性能；层次上下文表示作为CARS运行组件被实例化，并明确贡献于上下文感知推荐系统的设计。' }
    '28355' = @{ decision = 'exclude'; code = 'DOMAIN_MECHANISM_OR_POLICY_CONTRIBUTION'; reason = '贡献对象是多产品资源分配的智能市场机制与仿真评价；FleetPower命名不能把市场/运营机制转换成软件制品类级设计贡献。' }
    '28462' = @{ decision = 'include'; code = ''; reason = '核心终点是实际生成密码的确定性强度及修改行为；作者运行密码强度计并把ELM转译为该类软件反馈设计。' }
    '28480' = @{ decision = 'include'; code = ''; reason = '核心终点是外部事实标签下的机器人检测性能；众包反应与言语行为被实例化为社交机器人检测系统的可复用检测流程。' }
}

$source = Import-Csv -LiteralPath $sourceCsv
$modelCandidates = @($source | Where-Object { $_.strict_include -eq 'True' })

if ($modelCandidates.Count -ne 27) {
    throw "Expected 27 V3 candidates, found $($modelCandidates.Count)."
}

$rows = foreach ($row in $modelCandidates) {
    $id = [string]$row.record_id
    if (-not $audit.ContainsKey($id)) {
        throw "Missing manual adjudication for record_id=$id"
    }
    $a = $audit[$id]
    [pscustomobject][ordered]@{
        record_id = $id
        title = $row.title
        year = [int]$row.year
        journal = $row.journal
        model_v3_decision = 'include'
        final_decision = $a.decision
        manual_override = if ($a.decision -eq 'include') { 'false' } else { 'true' }
        final_exclusion_code = $a.code
        final_audit_reason_cn = $a.reason
        metric_status_v3 = $row.metric_status
        core_goal_status_v3 = $row.core_goal_status
        artifact_status_v3 = $row.artifact_status
        contribution_target_status_v3 = $row.contribution_target_status
        generalization_status_v3 = $row.generalization_status
        artifact_role_status_v3 = $row.artifact_role_status
        source_file = $row.source_file
    }
}

$included = @($rows | Where-Object { $_.final_decision -eq 'include' } | Sort-Object year, journal, title)
$excluded = @($rows | Where-Object { $_.final_decision -eq 'exclude' } | Sort-Object year, journal, title)

$rows | Sort-Object {[int]$_.record_id} | Export-Csv -LiteralPath (Join-Path $outputDir 'final_adjudication_27.csv') -NoTypeInformation -Encoding UTF8
$included | Export-Csv -LiteralPath (Join-Path $outputDir 'final_included_17.csv') -NoTypeInformation -Encoding UTF8
$excluded | Export-Csv -LiteralPath (Join-Path $outputDir 'final_excluded_10.csv') -NoTypeInformation -Encoding UTF8

$yearCounts = [ordered]@{}
$included | Group-Object year | Sort-Object {[int]$_.Name} | ForEach-Object { $yearCounts[$_.Name] = $_.Count }
$journalCounts = [ordered]@{}
$included | Group-Object journal | Sort-Object Name | ForEach-Object { $journalCounts[$_.Name] = $_.Count }
$exclusionCounts = [ordered]@{}
$excluded | Group-Object final_exclusion_code | Sort-Object Name | ForEach-Object { $exclusionCounts[$_.Name] = $_.Count }

$summary = [ordered]@{
    corpus_years = '2020-2027'
    corpus_fulltexts = $source.Count
    model = 'deepseek-v4-flash'
    request_unit = 'one full text per request'
    model_v3_candidates = $modelCandidates.Count
    final_included = $included.Count
    manual_excluded_from_v3 = $excluded.Count
    theory_filter_applied = $false
    final_year_counts = $yearCounts
    final_journal_counts = $journalCounts
    exclusion_code_counts = $exclusionCounts
    source_model_output = $sourceCsv
    prompt_fingerprint = '3fe999fdfd248f34c4711cccbdeb03e8257448aab6ef4f86d0622060efe5c10c'
    adjudication_note = 'V3 full-text model screening followed by conservative human full-text red-team adjudication of all 27 model-positive records.'
}

$summary | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $outputDir 'final_summary.json') -Encoding UTF8

Write-Output "Final adjudication complete."
Write-Output "V3 candidates: $($modelCandidates.Count)"
Write-Output "Final included: $($included.Count)"
Write-Output "Manual exclusions: $($excluded.Count)"
