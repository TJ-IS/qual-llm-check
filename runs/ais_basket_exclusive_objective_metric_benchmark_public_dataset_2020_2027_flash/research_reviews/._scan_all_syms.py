# -*- coding: utf-8 -*-
import io, re, collections
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# 需要关注的符号类：冒号(全/半)、分号(全/半)、破折号家族、引号家族、书名号、省略号、箭头、项目符号、其他杂项
targets = [
    (':','half colon'), ('：','full colon'), (';','half semi'), ('；','full semi'),
    ('—','em dash'), ('–','en dash'), ('--','double hyphen'), ('－','full hyphen'),
    ('“','lquote'), ('”','rquote'), ('‘','lq'), ('’','rq'), ('"','half dquote'), ("'","half squote"),
    ('「','corner l'), ('」','corner r'), ('『','corner ll'), ('』','corner rr'),
    ('《','book l'), ('》','book r'), ('〈','angle l'), ('〉','angle r'),
    ('…','ellipsis'), ('……','ellipsis2'), ('～','tilde'), ('~','half tilde'),
    ('·','middot'), ('•','bullet'), ('※','reference mark'), ('→','arrow'), ('←','arrow2'),
    ('①','circled1'), ('②','circled2'), ('③','circled3'), ('⑴','paren1'), ('⒈','numdot'),
]
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    print('='*12, n, '='*12)
    for ch, name in targets:
        c = body.count(ch)
        if c:
            print(f'  {name} ({ch!r}): {c}')
    # 列出所有非ASCII、非常见标点的字符
    common = set('，。、（）【】·——')
    weird = collections.Counter()
    for ch in body:
        if ord(ch) > 127 and ch not in common and not ('\u4e00' <= ch <= '\u9fff') and not ('\u3000' <= ch <= '\u303f') and not ('\uff00' <= ch <= '\uffef'):
            weird[ch] += 1
    if weird:
        print('  other non-cjk chars:', dict(weird))
