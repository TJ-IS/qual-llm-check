# 检索精度增强 v2：head=标题+摘要+引言前8000字符；full=全文

| 变体 | 99命中 | 召回率 | 语料命中 | 命中密度(99/命中) |
|---|---|---|---|---|
| V1 短语only-head8000 | 85/99 | 85.9% | 962 | 8.84% |
| V2 短语+恶意代码单数-head8000 | 86/99 | 86.9% | 984 | 8.74% |
| V3 短语+强攻击单数(含collusion)-head8000 | 94/99 | 94.9% | 1258 | 7.47% |
| V5a Q1-Q8全词块-head8000(不含extra) | 98/99 | 99.0% | 4887 | 2.01% |
| V5b Q1-Q8+extra-head8000(推荐主用) | 99/99 | 100.0% | 4896 | 2.02% |
| V6 Q1-Q8全词块-full(基线) | 99/99 | 100.0% | 12070 | 0.82% |

## V5b（推荐主用）head8000 漏掉的 99 篇：0 篇


## 补充词噪声检查（head8000）

- 'collusion' 命中 15 篇（其中 99 篇 1），非99样本：
  - 00456_2020_integrating-relations-and-criminal-background-to-identifying-key-individuals-in-crime-networks.md
  - 00710_2014_union-values-for-games-with-coalition-structure.md
  - 01772_2008_the-role-of-market-pricing-mechanism-under-imperfect-competition.md
  - 02442_2006_sharing-and-access-right-delegation-for-confidential-documents-a-practical-solution.md
  - 02790_2007_binary-vickrey-auction-a-robust-and-efficient-multi-unit-sealed-bid-online-auction-protocol-agai.md
  - 03092_2005_an-electricity-market-game-between-consumers-retailers-and-network-operators.md
  - 03392_2010_a-multi-level-theory-approach-to-understanding-price-rigidity-in-internet-retailing.md
  - 04494_2011_identification-of-fraudulent-financial-statements-using-linguistic-credibility-analysis.md
  - 07122_2005_robust-double-auction-protocol-against-false-name-bids.md
  - 07460_2023_does-it-enable-collusion-or-competition-examining-the-effects-of-it-on-service-pricing-in-multim.md
  - 09098_2011_an-experimental-comparison-of-linear-and-nonlinear-price-combinatorial-auctions.md
  - 10096_2009_improving-efficiency-in-multiple-unit-combinatorial-auctions-bundling-bids-from-multiple-bidders.md