import re, glob, os
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
files = {
 'radar': '27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md',
 'artext': '25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md',
 'ampel': '11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md',
 'dsdl': '16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md',
 'acaa': '28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md',
 'wolf': '00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md',
}
for k, fn in files.items():
    t = open(os.path.join(base, fn), encoding='utf-8').read()
    print(f'########## {k} ({fn[:40]}...) ##########')
    # find design science mentions
    for m in re.finditer(r'design science', t, re.I):
        s = max(0, m.start()-350); e = min(len(t), m.end()+350)
        print('--- DS:', t[s:e].replace(chr(10),' ')[:700])
    print()
