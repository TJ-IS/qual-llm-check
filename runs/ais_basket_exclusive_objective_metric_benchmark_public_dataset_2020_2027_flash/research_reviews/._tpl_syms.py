import re, os
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
files = {
 'radar': '27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md',
 'artext': '25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md',
 'ampel': '11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md',
 'dsdl': '16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md',
 'acaa': '28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md',
 'wolf': '00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md',
}
syms = {'em-dash—': '—', 'en-dash–': '–', 'curly"': '“', 'curly"2': '”', 'straight"': '"', 'colon:': ':', 'colon：': '：', 'semi;': ';', 'semi；': '；'}
for k, fn in files.items():
    t = open(os.path.join(base, fn), encoding='utf-8').read()
    # 仅统计引言部分（第一个 ## 小节之前）和全文
    intro = t.split('## Introduction')[1].split('\n##')[0] if '## Introduction' in t else ''
    print(f'== {k}  (引言, 全文)')
    for name, ch in syms.items():
        ci = intro.count(ch) if intro else -1
        cf = t.count(ch)
        if ci or cf: print(f'   {name}: 引言{ci} 全文{cf}')
