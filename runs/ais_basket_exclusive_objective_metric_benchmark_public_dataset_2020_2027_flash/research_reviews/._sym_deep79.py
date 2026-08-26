# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
out = []
for k, f in files.items():
    t = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    # 分离正文与参考文献表（以 '## 参考文献' 或 '[1] ' 起始的参考文献段为界）
    m = re.search(r'\n## 参考文献\n', t)
    if m:
        body, refs = t[:m.start()], t[m.start():]
    else:
        body, refs = t, ''
    syms = {
        '全角冒号：': body.count('：'), '全角分号；': body.count('；'),
        '破折号—': body.count('—'), '破折号―': body.count('―'),
        '左引号“': body.count('“'), '右引号”': body.count('”'),
        '单引号‘': body.count('‘'), '单引号’': body.count('’'),
        '省略号…': body.count('…'), '箭头→': body.count('→'),
        '半角冒号:': body.count(':'), '半角分号;': body.count(';'),
        '半角双引号"': body.count('"'), '半角单引号\'': body.count(chr(39)),
        '括号()': body.count('('), '方括号[]': body.count('['), '花括号{}': body.count('{'),
        '等号=': body.count('='), '加号+': body.count('+'), '乘号×': body.count('×'),
        '中点·': body.count('·'), '小于号<': body.count('<'), '大于号>': body.count('>'),
        '竖线|': body.count('|'), '斜杠/': body.count('/'), '反斜杠\\': body.count('\\'),
        '下划线_': body.count('_'), '连字符-': body.count('-'),
    }
    out.append('===== %s =====' % k)
    for name, cnt in syms.items():
        if cnt > 0:
            out.append('%s %d' % (name, cnt))
    # 参考文献区符号（仅统计，不改）
    if refs:
        out.append('参考文献区: 全角冒号 %d, 半角冒号 %d, 双引号 %d, 斜杠 %d' % (
            refs.count('：'), refs.count(':'), refs.count('“')+refs.count('”'), refs.count('/')))
io.open(os.path.join(DIR, '_sym_deep79.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
