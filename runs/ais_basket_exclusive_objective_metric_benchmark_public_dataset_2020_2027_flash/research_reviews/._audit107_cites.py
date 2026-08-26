# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for k,f in files.items():
    t = io.open(f, encoding='utf-8').read()
    body, refs = t.split('## 参考文献',1)
    # refs: collect (surname, year)
    ref_entries = []
    for m in re.finditer(r'^\[(\d+)\]\s*(.+)$', refs, flags=re.M):
        num, rest = m.group(1), m.group(2)
        y = re.search(r'\((\d{4})\)', rest)
        sur = re.search(r'^([A-Za-z\u4e00-\u9fff\-]+)', rest.strip())
        ref_entries.append((num, sur.group(1) if sur else '?', y.group(1) if y else '?'))
    ref_set = set()
    for num, sur, y in ref_entries:
        ref_set.add((sur.lower().rstrip(','), y))
    # in-text citations: (Name et al., YYYY)  /  (Name & Name, YYYY) / Name 等（YYYY）/ Name 与 Name（YYYY）
    cites = set()
    for m in re.finditer(r'([A-Z][A-Za-z\u00e9\-]+)(?: et al\.| 等| 与 ([A-Z][A-Za-z\-]+)| & ([A-Z][A-Za-z\-]+))?,? (?:et al\.?, )?\(?(\d{4})\)?', body):
        pass
    # simpler: collect all (Xxxx, YYYY) forms in parentheses and Name 等（YYYY） forms
    for m in re.finditer(r'[（(]([^（）()]{1,120}?\d{4}[^（）()]*)[）)]', body):
        g = m.group(1)
        for cm in re.finditer(r'([A-Z][A-Za-z\u00e9\-]+)(?:\s*&\s*[A-Z][A-Za-z\-]+|\set\sal\.)?,?\s*(\d{4})', g):
            cites.add((cm.group(1).lower(), cm.group(2)))
    for m in re.finditer(r'([\u4e00-\u9fffA-Za-z\-]+)(?: 等| 与 [\u4e00-\u9fffA-Za-z\-]+)?（(\d{4})[a-z]?）', body):
        nm = m.group(1)
        if nm not in ('见','本文','图','表','节'):
            cites.add((nm.lower(), m.group(2)))
    # check missing
    missing = sorted(c for c in cites if c not in ref_set)
    # check refs not cited
    # approximate: surnames in refs vs surname mentions
    uncited = []
    for num, sur, y in ref_entries:
        key = (sur.lower().rstrip(','), y)
        if key not in cites:
            # allow et al forms where first author surname appears
            uncited.append((num, sur, y))
    print('='*20, k)
    print('  正文引用(去重):', len(cites))
    print('  参考文献条目:', len(ref_entries))
    print('  正文有但参考文献无:', missing)
    print('  参考文献未见正文(近似):', uncited)
