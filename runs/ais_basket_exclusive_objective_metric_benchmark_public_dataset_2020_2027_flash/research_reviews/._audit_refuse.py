import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# reference key -> search patterns (author forms, year)
refkeys = {
 '34': {
  'Apruzzese et al., 2019': [('Apruzzese', 2019)],
  'Rai, 2017': [('Rai', 2017)],
  'Jimenez et al., 2024': [('Jimenez', 2024)],
  'Yuan et al., 2019': [('Yuan', 2019)],
  'Goosen et al., 2018': [('Goosen', 2018)],
  'Li & Chai, 2022': [('Li', 2022), ('Chai', 2022)],
  'Sutton & Barto, 2018': [('Sutton', 2018), ('Barto', 2018)],
  'Kolter & Madry, 2018': [('Kolter', 2018), ('Madry', 2018)],
  'Shostack, 2014': [('Shostack', 2014)],
  'Gregor & Hevner, 2013': [('Gregor', 2013), ('Hevner', 2013)],
  'Yang et al., 2024 (AgentDojo)': [('AgentDojo', 2024), ('Yang et al', 2024)],
  'Ebrahimi et al., 2025 (RADAR)': [('Ebrahimi', 2025), ('RADAR', 2025)],
  'Ghoshal et al., 2020': [('Ghoshal', 2020)],
  'Menon et al., 2022': [('Menon', 2022)],
  'Qu et al., 2026': [('Qu', 2026)],
  'Lausen et al., 2020': [('Lausen', 2020)],
  'Madry et al., 2018': [('Madry', 2018)],
  'Kwon & Lee, 2024': [('Kwon', 2024), ('Lee', 2024)],
  'Ampel et al., 2024': [('Ampel', 2024)],
  'Benjamin & Raghu, 2023': [('Benjamin', 2023), ('Raghu', 2023)],
  'Hevner et al., 2004': [('Hevner', 2004)],
  'Walls et al., 1992': [('Walls', 1992)],
  'Goodfellow et al., 2018': [('Goodfellow', 2018)],
  'Schulman et al., 2017': [('Schulman', 2017)],
  'Bertsimas et al., 2011': [('Bertsimas', 2011)],
  'Yang et al., 2023 (voice)': [('Yang et al', 2023), ('Yang', 2023)],
  'Greshake et al., 2023': [('Greshake', 2023)],
  'OWASP, 2025': [('OWASP', 2025)],
 },
 '35': {
  'Jimenez et al., 2024': [('Jimenez', 2024)],
  'Yang et al., 2024 (AgentDojo)': [('AgentDojo', 2024), ('Yang et al', 2024)],
  'Apruzzese et al., 2019': [('Apruzzese', 2019)],
  'Lin & Fang, 2021': [('Lin', 2021), ('Fang', 2021)],
  'Zhang et al., 2024 (disaster)': [('Zhang', 2024), ('Zhao', 2024), ('Fang', 2024)],
  'Qu et al., 2026': [('Qu', 2026)],
  'Gregor & Hevner, 2013': [('Gregor', 2013), ('Hevner', 2013)],
  'Rai, 2017': [('Rai', 2017)],
  'Ampel et al., 2024': [('Ampel', 2024)],
  'Wang et al., 2020': [('Wang', 2020)],
  'Shangguan et al., 2022': [('Shangguan', 2022)],
  'Yang & Subramanyam, 2023': [('Subramanyam', 2023), ('Yang', 2023)],
  'Yang et al., 2023a (sDTM)': [('Yang et al', 2023), ('Yang', 2023)],
  'Ray et al., 2021': [('Ray', 2021)],
  'Tsagkarakis et al., 2021': [('Tsagkarakis', 2021)],
  'du Jardin, 2021': [('du Jardin', 2021), ('Jardin', 2021)],
  'Wu et al., 2023': [('Wu', 2023)],
  'Ghoshal et al., 2020': [('Ghoshal', 2020)],
  'Menon et al., 2022': [('Menon', 2022)],
  'Li & Chai, 2022': [('Li', 2022), ('Chai', 2022)],
  'Lausen et al., 2020': [('Lausen', 2020)],
  'Hevner et al., 2004': [('Hevner', 2004)],
  'Walls et al., 1992': [('Walls', 1992)],
  'Yang et al., 2023b (voice)': [('Yang et al', 2023), ('Yang', 2023)],
 },
 '36': {
  'Jimenez et al., 2024': [('Jimenez', 2024)],
  'Yang et al., 2024 (AgentDojo)': [('AgentDojo', 2024), ('Yang et al', 2024)],
  'Apruzzese et al., 2019': [('Apruzzese', 2019)],
  'Li & Chai, 2022': [('Li', 2022), ('Chai', 2022)],
  'McCornack, 1992': [('McCornack', 1992)],
  'Glancy & Yadav, 2011': [('Glancy', 2011), ('Yadav', 2011)],
  'Humpherys et al., 2011': [('Humpherys', 2011)],
  'Siering et al., 2016': [('Siering', 2016)],
  'Walther et al., 2009': [('Walther', 2009)],
  'Lausen et al., 2020': [('Lausen', 2020)],
  'Zhang et al., 2023 (fake reviewers)': [('Zhang', 2023), ('Niu', 2023), ('Wu', 2023)],
  'Kumar et al., 2022': [('Kumar', 2022)],
  'Gopal et al., 2022': [('Gopal', 2022)],
  'Benjamin & Raghu, 2023': [('Benjamin', 2023), ('Raghu', 2023)],
  'Liang & Xue, 2009': [('Liang', 2009), ('Xue', 2009)],
  'Gregor & Hevner, 2013': [('Gregor', 2013), ('Hevner', 2013)],
  'Rai, 2017': [('Rai', 2017)],
  'Walls et al., 1992': [('Walls', 1992)],
  'Hevner et al., 2004': [('Hevner', 2004)],
  'Yang et al., 2023b (voice)': [('Yang et al', 2023), ('Yang', 2023)],
  'Gupta et al., 2025': [('Gupta', 2025)],
  'Vamosi et al., 2022': [('Vamosi', 2022)],
  'Zhu et al., 2021': [('Zhu', 2021)],
  'Shan et al., 2020': [('Shan', 2020)],
  'Ebrahimi et al., 2025 (RADAR)': [('Ebrahimi', 2025), ('RADAR', 2025)],
  'Ghoshal et al., 2020': [('Ghoshal', 2020)],
  'Menon et al., 2022': [('Menon', 2022)],
  'Qu et al., 2026': [('Qu', 2026)],
  'Lin & Fang, 2021': [('Lin', 2021), ('Fang', 2021)],
 },
}
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print(f'########## {n}: 参考文献是否被正文引用 ##########')
    for key, pairs in refkeys[n].items():
        found = []
        for auth, yr in pairs:
            cnt = len(re.findall(re.escape(auth)+r'[^。\n]{0,30}'+str(yr), main))
            found.append((auth, cnt))
        if not any(c>0 for a,c in found):
            print(f'  MISS: {key}  ({found})')
    print()
