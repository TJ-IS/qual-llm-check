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
    lines = io.open(os.path.join(DIR, f), encoding='utf-8').read().split('\n')
    headers = []
    for i, ln in enumerate(lines):
        m = re.match(r'^#{2,4} (\d+(?:\.\d+)?)[ 　]', ln)
        if m:
            headers.append((m.group(1), i+1))
    out.append('===== %s 章节表 =====' % k)
    for h, l in headers:
        out.append('  %s (L%d)' % (h, l))
    out.append('----- %s 交叉引用 -----' % k)
    for i, ln in enumerate(lines):
        for m in re.finditer(r'见\s*(\d+(?:\.\d+)?)\s*节', ln):
            ref = m.group(1)
            ok = any(ref == h for h, _ in headers)
            out.append('L%d 引用 %s 节 -> %s' % (i+1, ref, '存在' if ok else '!!不存在!!'))
        for m in re.finditer(r'(\d+(?:\.\d+)?)节中?详?述|(\d+(?:\.\d+)?)节中(?:详述|落实|校准|综述|推导)', ln):
            ref = m.group(1) or m.group(2)
            ok = any(ref == h for h, _ in headers)
            if ref:
                out.append('L%d 隐含引用 %s 节 -> %s' % (i+1, ref, '存在' if ok else '!!不存在!!'))
io.open(os.path.join(DIR, '_xref79.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
