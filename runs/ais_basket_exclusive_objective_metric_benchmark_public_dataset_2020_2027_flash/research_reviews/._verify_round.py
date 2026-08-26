import re
f34 = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
f35 = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
# 34 7.1 贡献一
t = open(f34, encoding='utf-8').read()
i = t.find('第一，本文框架以系统化刻画')
print('34 7.1 贡献一:')
print('  ', t[i:i+360].replace(chr(10),' '))
print()
# 35 P1 结尾
t = open(f35, encoding='utf-8').read()
i = t.find('多个编码助手平台已被披露存在真实漏洞')
print('35 P1 结尾:')
print('  ', t[i:i+150].replace(chr(10),' '))
print()
i = t.find('与此同时，防御资源的部署')
print('35 P2 预算句:')
print('  ', t[i:i+120].replace(chr(10),' '))
print()
i = t.find('编码智能体在软件开发中的采用正在重塑')
print('35 结论九开头:')
print('  ', t[i:i+150].replace(chr(10),' '))
print()
# 36 P1 结尾 + P2
t = open(f36, encoding='utf-8').read()
i = t.find('已有研究系统披露针对模型上下文协议的工具投毒攻击')
print('36 P1 结尾 + P2:')
print('  ', t[i:i+520].replace(chr(10),' '))
print()
i = t.find('现有检测机制的局限可从两个维度归纳')
print('36 2.1 两处:')
print('  ', t[i-330:i+60].replace(chr(10),' '))
