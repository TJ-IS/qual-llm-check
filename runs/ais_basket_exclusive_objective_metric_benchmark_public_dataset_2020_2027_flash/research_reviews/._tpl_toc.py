# -*- coding: utf-8 -*-
import io, re, os
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
files = {
 '25465_assessing': '25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md',
 '11686_creating': '11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md',
 '00790_whois': '00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md',
 '16409_theory': '16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md',
 '28706_attending': '28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md',
}
for k, fn in files.items():
    p = os.path.join(base, fn)
    t = io.open(p, encoding='utf-8').read()
    print('='*15, k, 'LEN', len(t), '='*15)
    hdrs = [m.group(0)[:90] for m in re.finditer(r'^(#{1,4}) .*$', t, re.M)]
    for h in hdrs[:40]:
        print(h)
    print()
