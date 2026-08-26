# -*- coding: utf-8 -*-
import io, os, re
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
tpls = {
 'RADAR 27598': '27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md',
 'ARText 25465': '25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md',
 'CTI 11686': '11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md',
 'DSDL 16409': '16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md',
 'Attending 28706': '28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md',
 'Wolf 00790': '00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md',
}
targets = {'em dash —': '—', 'double ——': '——', 'en dash –': '–', 'lq “': '“', 'rq ”': '”', 'sq ‘': '‘', 'sq ’': '’', 'full colon ：': '：', 'half colon :': ':', 'semi ;': ';', 'ellipsis …': '…', 'middot ·': '·', 'tilde ~': '~'}
for name, fn in tpls.items():
    p = os.path.join(base, fn)
    t = io.open(p, encoding='utf-8').read()
    # 只统计正文主体（去掉 References 之后）
    body = t
    for marker in ['## References', '## REFERENCES', 'References\n', '## 参考文献']:
        i = body.find(marker)
        if i > 0:
            body = body[:i]
            break
    print('='*10, name, '正文字符数', len(body), '='*10)
    for k, ch in targets.items():
        c = body.count(ch)
        if c:
            print(f'  {k}: {c}')
