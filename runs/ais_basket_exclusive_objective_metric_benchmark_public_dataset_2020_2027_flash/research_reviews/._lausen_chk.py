# -*- coding: utf-8 -*-
import io, re, difflib
def norm(s):
    s = re.sub(r"【[^】]*】", "P", s)
    s = re.sub(r"\s+", "", s)
    return s
a = "Lausen 等（2020）在金融中介不当行为检测中按外部验证级别递增组织特征集，证明外部可验证信号带来增量检测价值。"
b = "在不当行为检测情境中，Lausen 等（2020）证明按外部验证级别递增组织的特征集可显著提升金融中介不当行为的检测性能。"
r = difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
print("Lausen 36 P4 vs P5:", round(r, 3))
# also 34 vs 36 Lausen
c = "在检测情境中，Lausen 等（2020）证明外部验证信息可显著提升对操纵性自披露的检测性能。"
print("34 vs 36 Lausen:", round(difflib.SequenceMatcher(None, norm(c), norm(b)).ratio(), 3))
print("34 vs 36 Lausen2:", round(difflib.SequenceMatcher(None, norm(c), norm(a)).ratio(), 3))