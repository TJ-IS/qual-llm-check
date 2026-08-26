# -*- coding: utf-8 -*-
import io, re
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def grab(fn, start_pat, end_pat, span=0):
    text = io.open(base + '\\' + fn, encoding='utf-8').read()
    m = re.search(start_pat, text)
    if not m: return 'NOT FOUND: ' + start_pat
    s = m.start()
    if span:
        return text[s:s+span].replace('\n', ' ')
    e = re.search(end_pat, text[s+10:])
    return text[s:s+10+(e.start() if e else span)].replace('\n', ' ')

print('=== RADAR Research Gaps and Questions ===')
print(grab('27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md', r'## Research Gaps and Questions', r'## ', 1600))
print()
print('=== RADAR Proposed Design 图注句 ===')
print(grab('27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md', r'Figure 1 illustrates an overview', r'\.', 400))
print()
print('=== RADAR Discussion 贡献与启示 ===')
print(grab('27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md', r'## Discussion', r'## ', 1800))
print()
print('=== DSDL 挑战段 ===')
print(grab('16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md', r'fraught with challenges', r'\.', 700))
print()
print('=== ARText Technical Novelties ===')
print(grab('25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md', r'## Technical Novelties', r'## ', 1000))
print()
print('=== Wolf 3.2 Data Acquisition ===')
print(grab('00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md', r'## 3\.2 Data Acquisition', r'## ', 900))
print()
print('=== Ampel Data Collection ===')
print(grab('11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md', r'## Data Collection', r'## ', 700))
print()
print('=== ARText 鲁棒性评估规范句 ===')
print(grab('25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md', r'robustness assessment', r'\.', 500))
