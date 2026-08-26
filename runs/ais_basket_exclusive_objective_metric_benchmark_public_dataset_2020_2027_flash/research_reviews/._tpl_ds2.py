import re, os
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
files = {
 'artext': '25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md',
 'ampel': '11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md',
 'dsdl': '16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md',
 'wolf': '00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md',
}
out = []
for k, fn in files.items():
    t = open(os.path.join(base, fn), encoding='utf-8').read()
    out.append(f'########## {k} ##########')
    # design rationale / design science positioning (first two matches)
    cnt = 0
    for m in re.finditer(r'design (?:rationale|science|theory)', t, re.I):
        s = max(0, m.start()-300); e = min(len(t), m.end()+400)
        out.append('--- '+t[s:e].replace(chr(10),' ')[:750])
        cnt += 1
        if cnt >= 3: break
    out.append('')
open('._tpl_ds2_out.txt','w',encoding='utf-8').write('\n'.join(out))
print('done')
