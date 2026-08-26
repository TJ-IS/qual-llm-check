# -*- coding: utf-8 -*-
import io, re
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
text = io.open(base + r'\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md', encoding='utf-8').read()
# RADAR Introduction 全文
m = re.search(r'## Introduction', text)
seg = text[m.start():m.start()+8000]
# 清理 markdown 图片与公式噪音，保留正文句子
seg = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', seg)
seg = re.sub(r'\$\$[^$]*\$\$', '', seg)
seg = re.sub(r'\s+', ' ', seg)
print(seg[:6500])
