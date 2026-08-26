# -*- coding: utf-8 -*-
import io, re
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
pats = {
 'radar': [r'[^\n]*Given these gaps[^\n]*', r'[^\n]*Figure 1[^\n]*', r'[^\n]*baseline[^\n]*', r'[^\n]*First, our[^\n]*|Second, we[^\n]*|Third, we[^\n]*', r'[^\n]*practical[^\n]*'],
 'dsdl': [r'[^\n]*design science[^\n]*', r'[^\n]*challenge[^\n]*', r'[^\n]*overview[^\n]*'],
 'artext': [r'[^\n]*novelt[^\n]*', r'[^\n]*robustness[^\n]*'],
 'wolf': [r'[^\n]*[Dd]ata [Aa]cquisition[^\n]*', r'[^\n]*[Ee]valuation [Mm]ethodology[^\n]*'],
 'ampel': [r'[^\n]*[Dd]ata [Cc]ollection[^\n]*'],
}
for tag, fn in [('radar','27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'),
                ('dsdl','16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md'),
                ('artext','25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md'),
                ('wolf','00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md'),
                ('ampel','11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md')]:
    text = io.open(base + '\\' + fn, encoding='utf-8').read()
    print('#'*20, tag)
    for p in pats[tag]:
        ms = list(re.finditer(p, text))
        print(' PAT', p[:30], '->', len(ms), 'hits')
        for m in ms[:3]:
            s = max(0, m.start()-150); e = min(len(text), m.end()+150)
            print('   ...', text[s:e].replace('\n',' ')[:320])
