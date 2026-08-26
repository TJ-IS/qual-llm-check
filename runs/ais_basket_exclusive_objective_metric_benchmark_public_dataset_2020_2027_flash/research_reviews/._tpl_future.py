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
out = []
for k, fn in files.items():
    t = open(os.path.join(base, fn), encoding='utf-8').read()
    out.append(f'########## {k} 未来研究/结论 ##########')
    hits = [m.start() for m in re.finditer(r'future research', t, re.I)]
    for h in hits[:2]:
        s = max(0, h-200); e = min(len(t), h+700)
        out.append('--- '+t[s:e].replace(chr(10),' ')[:900])
    if not hits:
        hits2 = [m.start() for m in re.finditer(r'conclusion', t, re.I)]
        for h in hits2[-2:]:
            s = max(0, h-100); e = min(len(t), h+900)
            out.append('--- '+t[s:e].replace(chr(10),' ')[:1000])
    out.append('')
open('._tpl_future_out.txt','w',encoding='utf-8').write('\n'.join(out))
print('done')
