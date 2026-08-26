---
otero_id: 17083
otero_key: "CZMUJ5RE"
title: "An (interactive) decision support system for bank asset liability management"
authors: "Dieter Langen"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90018-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An (Interactive) Decision Support System for Bank Asset Liability Management

Dieter LANGEN $^{1}$

Institute for Statistics and Mathematical Economics, University of Karlsruhe, D-7500 Karlsruhe, FRG

We will present a short overview of the major quantifiable conflicting goals in bank asset/liability management and their definitions in our Multi-Criteria-Decision-Making (MCDM) model and DSS. Uncertain parameters are considered by user-given scenarios and the use of risk evaluation through risk measures. We describe the decision method (reference point approach) and the (interactive) decision support system IDSSBALM and its features with respect to DSS methodology. Finally, we provide a short example of the model and some possible banking strategies.

Keywords: MCDM; DSS; Banking; Vector-Optimization; Decision Support Systems; Uncertainty; Integrated Model Building.

![](/api/attachments/CZMUJ5RE/fulltext/images/77332c2e6b10f6768c0c8c85650e1c13007c02927a55848c4fe1f0c2fef60b8f.jpg)

Dieter Langen is a consultant at the Boston Consulting Group in Düsseldorf, Fed. Republic of Germany. He holds the degrees of Diplom-Wirtschaftsingenieur from the University of Karlsruhe, FRG and an MIB from the University of South Carolina, Columbia, USA. In 1988 he received a PhD in economics from the University of Karlsruhe, FRG. In his research he investigates the way operations research methods can practically help in the case of complex strategic bank planning problems with multiple objectives using decision support systems and vector optimization. Currently, his main interests are directed towards decision support systems in a variety of different areas, e.g. mergers and acquisitions, banking.

The Boston Consulting Group, Königsallee 1, D-4000 Düsseldorf 1, FRG. This paper is part of the research at the Institute for Statistics and Mathematical Economics.

## 1. Motivation and Problem Description

In the past few years the banking business has become more and more complex. New financial instruments, substantial risks connected with all kinds of banking business, volatile interest rates, market-oriented private and corporate customers and the internationalization and globalization of the national business systems have resulted in the biggest challenge to banks since the Great Depression and the big Banking Crash. The need for overall strategic asset/liability (A/L) management has become very obvious while the bank managers still have to deal with partial approaches leading to suboptimal overall solutions and strategies and often just act as “firefighters”.

The idea of our model is to create and build a model and decision support system which is able to comprise and to consider the most important quantifiable bank objectives and provide the user(s) with one (or several) solution(s) as a basis for further decision making. Since you deal with future and thereby uncertain events there is never anything like “the” best solution but only “a” best solution for the predicted future scenario, the chosen parameters and the set and importance of the chosen objectives. Therefore the system has to be interactive in order to react easily on all required problem changes. The DM must simultaneously have the freedom necessary to formulate his own specific model, but also the restrictions of an overall (sub-) model environment (for a complete overview see [12]).

## 2. The Model

There have been numerous publications on financial modelling in the past (for good overviews see [4], [17] and [18]) and some even dealt with bank A/L-management but almost all of them concentrated on a partial banking problem. Little academic work has been done so far for a global reconciliation. The very existence of efficient solution algorithms for all bank planning optimization models which can adequately handle the problems mentioned has been recently denied ([18], p. 312). Therefore we tried to consider all major quantifiable banking problems and objectives in an integrated approach which has to be solved by a suitable (combination of) optimization algorithm(s).

The model assumptions are the following: The bank is a (German) universal bank operating nationally and internationally, basically in its home currency (HC, e.g. Deutsche Mark) but also in foreign currencies (FC). It pursues several, conflicting objectives and faces legal (e.g. banking laws) and bank policy or market constraints. By active marketing it tries to steer its asset and liability balance positions which, for the purpose of planning, cannot be related to each other. The different A/L-positions are homogeneous among each other with respect to all model and scenario parameters. Considering uncertainty of future events and developments we assume that the bank can estimate scenarios of future outcomes of the uncertain parameters. Any bonds in the bank's portfolio are assumed to be held only for liquidity reasons and are not sold before the end of maturity.

As decision variables we take the (new) A/L-positions of business to be started in the next planning period (index "new") but for the objectives and constraints we also have to consider (old) A/L-positions of business started in the past (index "old") which cannot be changed anymore.

Our first objective is the maximization of the bank's gain or returns. We basically define gain as return of the interest business. Since it is almost impossible to connect any costs other than refinancing costs with a certain A/L-position and since the yield from provisions, especially the emission and the commission trade of corporate and public stock and bonds, is very volatile and depends on the overall “climate” at the stock exchange and in industry (i.e. the bank has almost no influence in the yields), they are neglected here. Besides, the yield from provisions does not play a major role at most (German) universal banks. Formally,

$$
f _ {1} \colon \mathbb {R} _ {+} ^ {n + m} \rightarrow \mathbb {R}, \quad \text { continuous },\tag{1}
$$

$$
\begin{array}{l}f _ {1} \left(\underline {{x}} ^ {\text { new }}, \underline {{y}} ^ {\text { new }}\right)\\:= \sum_ {i = 1} ^ {n} r x _ {i} ^ {\text { new }} \cdot x _ {i} ^ {\text { new }} + r x _ {i} ^ {\text { old }} \cdot \bar {x} _ {i} ^ {\text { old }} \cdot \left(1 - a _ {1, i} ^ {\text { old }}\right)\\- \sum_ {j = 1} ^ {m} r y _ {j} ^ {\text { new }} \cdot y _ {j} ^ {\text { new }} + r y _ {j} ^ {\text { old }} \cdot \bar {y} _ {j} ^ {\text { old }} \cdot \left(1 - b _ {1, j} ^ {\text { old }}\right)\\\rightarrow \max.\end{array}
$$

The gain is defined as the difference between the sum of the effective net interest earned and the one paid for by the bank. $x_{i}/y_{j}$ denote A/L positions, $rx_{i}/ry_{j}$ the effective net interest rates of $x_{i}/y_{j}$ and $a_{1,i}^{old}/b_{1,j}^{old}$ the percentage of $\bar{x}_{i}^{old}/\bar{y}_{j}^{old}$ (constant) that matures in the first planning period (we assume that all amounts to be paid back for A/L-positions are due at the beginning of the planning period which is also the time when “new” business is done). Therefore our objective is to maximize the average annual interest income by the bank.

Effective net interest rates are uncertain and in order to consider the different criteria of the A/L positions correctly they comprise effective interest rates ( $^{e}rx_{i}/^{e}ry_{j}$ ), effective credit loss rates ( $xcr_{i}$ ) and currency factors ( $^{FC}rx_{i}, ^{FC}ry_{j}$ ): $^{2}$

$$
\begin{array}{l} r x _ {i} = ^ {e} r x _ {i} - x c r _ {i} + / - ^ {\mathrm{FC}} r x _ {i}, \\ r y _ {j} = ^ {e} r y _ {j} + / - ^ {\mathrm{FC}} r y _ {j}. \end{array}\tag{2}
$$

For fixed interest rate A/L-positions ${}^{e}rx_{i}/{}^{e}ry_{j}$ is constant and for HC-business ${}^{FC}rx_{i}/{}^{FC}ry_{j}$ is 0 (if one does not consider credit losses and/or FC-changes one compares the A/L-position on a wrong basis). Further, the bank is assumed to be able to estimate a scenario for these uncertain rates.

As a second objective we take the maximization of the bank's balance or business volume which, for various reasons such as being an indicator for market power, customer popularity, management performance and ability to place corporate bonds, is important for the bank's standing, e.g. Japanese banks from 1984–1986. Formally,

$$
\begin{array}{l} f _ {2} ^ {1} \colon \mathbb {R} _ {+} ^ {n} \to \mathbb {R} _ {+}, \text {   cont. }, \qquad f _ {2} ^ {2} \colon \mathbb {R} _ {+} ^ {m} \to \mathbb {R} _ {+}, \text {   cont. }, \\ f _ {2} ^ {1} \big (\underline {{x}} ^ {\text { new }} \big) := \sum_ {i = 1} ^ {n} x _ {i} ^ {\text { new }} + \overline {{x}} _ {i} ^ {\text { old }} \cdot \big (1 - a _ {1, i} ^ {\text { old }} \big) \to \max, \end{array}\tag{or}
$$

(3)

(bank balance volume)

$$
\begin{array}{l}f _ {2} ^ {2} \left(\underline {{y}} ^ {\text { new }}\right) := \sum_ {j = 1} ^ {m} y _ {j} ^ {\text { new }} + \bar {y} _ {j} ^ {\text { old }} \cdot \left(1 - b _ {1, j} ^ {\text { old }}\right)\\\rightarrow \max, \quad \text { and }\end{array}\tag{4}
$$

$$
\begin{array}{l} f _ {2} ^ {3} \colon \mathbb {R} _ {+} ^ {n _ {1} + n _ {2}} \to \mathbb {R} _ {+}, \text {cont.}, \\ f _ {2} ^ {4} \colon \mathbb {R} _ {+} ^ {m _ {1} + m _ {2}} \to \mathbb {R} _ {+}, \text {cont.}, \\ f _ {2} ^ {3} \left(\underline {{\mathrm{B}}} \underline {{x}} ^ {\text {new}}, \mathrm{NB} \underline {{x}} ^ {\text {new}}\right) \\ := \sum_ {i = 1} ^ {n _ {1}} ^ {B} x _ {i} ^ {\text {new}} + ^ {B} \overline {{x}} _ {i} ^ {\text {old}} \cdot \left(1 - ^ {B} a _ {1, i} ^ {\text {old}}\right) \\ + \sum_ {i = 1} ^ {n _ {2}} ^ {\mathrm{NB}} x _ {i} ^ {\text {new}} + ^ {\mathrm{NB}} \overline {{x}} _ {i} ^ {\text {old}} \cdot \left(1 - ^ {\mathrm{NB}} a _ {1, i} ^ {\text {old}}\right) \to \max, \end{array}\tag{5}
$$

or

(bank business volume)

$$
f _ {2} ^ {4} \left(\underline {{\mathrm{B}}} y ^ {\text { new }}, \mathrm{NB} \underline {{y}} ^ {\text { new }}\right) := \sum_ {j = 1} ^ {m _ {1}} \mathrm{B} y _ {j} ^ {\text { new }} + \mathrm{B} \bar {y} _ {j} ^ {\text { old }} \cdot \left(1 - \mathrm{B} b _ {1, j} ^ {\text { old }}\right)\tag{6}
$$

$$
+ \sum_ {j = 1} ^ {m _ {2}} ^ {\mathrm{NB}} y _ {j} ^ {\text { new }} + ^ {\mathrm{NB}} \bar {y} _ {j} ^ {\text { old }} \cdot \left(1 - ^ {\mathrm{NB}} b _ {1, j} ^ {\text { old }}\right)\rightarrow \max,
$$

where the indices "B" and "NB" denote balance and non-balance A/L-positions. Non-balance positions are basically eventual claims and/or liabilities.

The third objective is the minimization of credit losses. Although already considered with respect to the gain objective this is not enough. Besides national credit risks our bank faces international credit and country risk and regularly has to take risk precautions for faulty credits which for various reasons (e.g. possible bankruptcy of the bank or cancellation of dividends, public standing) have to be kept as small as possible in order to avoid negative side-effects (e.g. customer money withdrawals, higher refinancing interest rates, drop of the bank's stock price, lower credit and stock ratings). The current reevaluation of LDC-credits by major international banks and its results (started by Citicorp) are a good example of the importance of this objective. Formally,

(7)

$$
\begin{array}{l}f _ {3} ^ {1}: \mathbb {R} _ {+} ^ {n _ {1}} \to \mathbb {R} _ {+}, \text {cont.};\\f _ {3} ^ {1} \left(^ {B} \underline {{x}} ^ {\text {new}}\right)\\:= \sum_ {i = 1} ^ {n _ {1}} ^ {B} x c r _ {i} ^ {\text {new}} \cdot^ {B} x _ {i} ^ {\text {new}} + ^ {B} x c r _ {i} ^ {\text {old}} \cdot^ {B} \overline {{x}} _ {i} ^ {\text {old}}\\\cdot \left(1 - ^ {B} a _ {1, i} ^ {\text {old}}\right)\\\rightarrow \min,\\f _ {3} ^ {2}: \mathbb {R} _ {+} ^ {n _ {1} + n _ {2}} \to \mathbb {R} _ {+}, \text {cont.};\\f _ {3} ^ {2} \left(^ {B} \underline {{x}} ^ {\text {new}}, ^ {N B} \underline {{x}} ^ {\text {new}}\right)\\:= \sum_ {i = 1} ^ {n _ {1}} ^ {B} x c r _ {i} ^ {\text {new}} \cdot^ {B} x _ {i} ^ {\text {new}} + ^ {B} x c r _ {i} ^ {\text {old}} \cdot^ {B} \overline {{x}} _ {j} ^ {\text {old}}\\\cdot \left(1 - ^ {B} a _ {1, i} ^ {\text {old}}\right)\\+ \sum_ {i = 1} ^ {n _ {2}} ^ {N B} x c r _ {i} ^ {\text {new}} \cdot^ {N B} x _ {i} ^ {\text {new}} + ^ {N B} x c r _ {i} ^ {\text {old}} \cdot^ {N B} \overline {{x}} _ {i} ^ {\text {old}}\\\cdot \left(1 - ^ {N B} a _ {1, i} ^ {\text {old}}\right)\rightarrow \min.\end{array}\tag{8}
$$

The necessary objective function to be used depends on whether the bank has a lot of non-balance business and is especially important for the new financial instruments. The objective also considers when credit loss assessments of old credits change due to unforeseen events or developments. The effective credit loss rates ( $^{B}xcr_{i}^{new/old}$ , $^{NB}xcr_{i}^{new/old}$ ) are again assumed to be known to the bank as possible scenario.

As a fourth major objective we consider the minimization of interest rate risk. A great deal of banking profits usually result from structural disparities (short- vs. long-term) between asset and liability positions. The banks which let those disparities get out of hand in the past sometimes suffered huge losses when the interest rates in connection with different maturity dates of A/L-positions increased or decreased rapidly or even changed their structure (normal to inverse or vice versa). This basically resulted in the (wrong) point of view that all structural imbalances generally have to be avoided whereby this totally neglects any kind of interest rate chances. One possible conclusion was the development of the duration strategy approach (e.g. [16]) which more or less bans interest rate risk, i.e. the risk that the planned yield in the planning horizon, mainly for fixed rate A/L-positions, is lower than the realized one (e.g. [3]). This approach not only misses all interest rate chances, but also neglects variable interest rate risk and “interest rate breath”, i.e. different quantitative (structural) movements of interest rates on the A/L-side.

We define interest rate risk as a decrease of the interest revenues from one period to another due to interest rate changes. This is basically a gap management approach. Formally.

$$
\begin{array}{l}t = 1: \quad f _ {4, 1}: \mathbb {R} _ {+} ^ {n + m} \rightarrow \mathbb {R}, \text {cont.};\\f _ {4, 1} \left(\underline {{x}} ^ {\text {new}}, \underline {{y}} ^ {\text {new}}\right)\\:= \left(\sum_ {i = 1} ^ {n} a _ {1, i} ^ {\text {old}} \cdot \bar {x} _ {i} ^ {\text {old}} \cdot^ {\mathrm{e}} \overline {{r x _ {i} ^ {\text {old}}}} - x _ {i} ^ {\text {new}} \cdot^ {\mathrm{e}} r x _ {i} ^ {\text {new}}\right)\\- \left(\sum_ {j = 1} ^ {m} b _ {1, j} ^ {\text {old}} \cdot \bar {y} _ {j} ^ {\text {old}} \cdot^ {\mathrm{e}} \overline {{r y _ {j} ^ {\text {old}}}} - y _ {j} ^ {\text {new}} \cdot^ {\mathrm{e}} r y _ {j} ^ {\text {new}}\right)\rightarrow \min,\\t \geqslant 2: \quad f _ {4, t}: \mathbb {R} _ {+} ^ {n + m} \rightarrow \mathbb {R}, \text {cont.};\\f _ {4, t} \left(\underline {{x}} ^ {\text {new}}, \underline {{y}} ^ {\text {new}}\right)\\:= \left[ \sum_ {i = 1} ^ {n} a _ {t, i} ^ {\text {old}} \cdot \bar {x} _ {i} ^ {\text {old}} \cdot \left(^ {\mathrm{e}} \bar {r} \bar {x} _ {i} ^ {\text {old}} - ^ {\mathrm{e}} r x _ {i} ^ {t}\right) + a _ {t, i} ^ {\text {new}} \cdot x _ {i} ^ {\text {new}} \cdot \left(^ {\mathrm{e}} r x _ {i} ^ {\text {new}} - ^ {\mathrm{e}} r x _ {i} ^ {t}\right) \right]\\- \left[ \sum_ {j = 1} ^ {m} b _ {t, j} ^ {\text {old}} \cdot \bar {y} _ {j} ^ {\text {old}} \cdot \left(^ {\mathrm{e}} \overline {{r y _ {j}}} ^ {\text {old}} - ^ {\mathrm{e}} r y _ {j} ^ {t}\right) + b _ {t, j} ^ {\text {new}} \cdot y _ {j} ^ {\text {new}} \cdot \left(^ {\mathrm{e}} r y _ {j} ^ {\text {new}} - ^ {\mathrm{e}} r y _ {j} ^ {t}\right)\right]\rightarrow \min.\end{array}\tag {9}
$$

Hereby $^{e}rx_{i}/^{e}ry_{j}$ (constant for fixed-term A/L) denote the effective interest rates of old/new A/L-positions for period t=1, i.e. the coming period, while $^{e}rx_{i}^{t}/^{e}ry_{j}^{t}$ stand for the effective interest rate of the respective A/L-position in period t.

The basic idea is that the maturing amounts of all A/L-positions have to be reinvested or refinanced for the same interest rates as before so that there exist no risks nor chances. A higher refinancing and/or a lower reinvestment interest rate mean decreasing interest returns and thereby risk while lower refinancing and/or higher reinvestment interest rates mean increasing interest returns and thereby chances. The sum of all risk/chance effects is the net interest rate risk (>0) or chance (<0) in a period.

Although we don't consider the disposition of any future A/L-position beyond the next period we still have to take the effects of the decision variables on the future business into account. Hereby we assume that the maturing amounts will be again reinvested/refinanced in the same A/L-positions by the same amount in period $t \geq 2$ . In order to avoid interest rate risk the bank has to close all positive gaps during the planning horizon T. Therefore the overall interest rate risk function for periods $t = 1, \ldots, T$ is either the sum of the discounted risks in the single periods or the maximum possible risk in one single period. Formally, $f_{4a}: R_{+}^{n+m} \to R$ , cont.;

$$
\begin{array}{r l}f _ {4 a} \left(\underline {{x}} ^ {\text { new }}, \underline {{y}} ^ {\text { new }}\right)&= f _ {4, 1} (\cdot , \cdot) + \sum_ {t = 2} ^ {T} f _ {4, t} (\cdot , \cdot) \cdot (1 + i) ^ {- t + 1} \rightarrow \min,\\f _ {4 b}: \mathbb {R} _ {+} ^ {n + m} \rightarrow \mathbb {R},&\text { cont. };\\f _ {4 b} \left(\underline {{x}} ^ {\text { new }}, \underline {{y}} ^ {\text { new }}\right)&= \max \left\{f _ {4, 1} (\cdot , \cdot), f _ {4, 2} (\cdot , \cdot) \cdot (1 + i) ^ {- 1}, \dots , f _ {4, T} (\cdot , \cdot) \cdot (1 + i) ^ {- T + 1} \right\}\rightarrow \min.\end{array}\tag {11}
$$

In $f_{4b}$ you minimize the maximal discounted repricing gap for periods $t = 1, \ldots, T$ .

Since options other than for certain (public) bonds and interest rate futures will not be introduced to the German financial markets before 1990 and the use of futures and options besides the lack of correlation to DM A/L-positions would involve currency risk, they are not considered here. Their use, however, could be included without too much of complication.

Our fifth and last major objective is the minimization of currency or exchange rate risk. Usually currency risk is defined as the risk of losing money on FC A/L-positions due to changes of the HC/FC exchange rate connected with FC A/L-imbalances. Therefore the bank normally tries to match all FC-positions by corresponding counter-positions and/or by hedging transactions (e.g. on the forward market).

In reality FC-imbalances and HC/FC exchange rate changes do not have to be wrong by definition. If the bank can anticipate and consider them in the interest rates of FC-positions, the bank will always try to incorporate its FC development forecasts into its product prices (if the market allows it) resulting in a mark-up (or -down) of FC compared to HC interest rates.

We therefore define currency risk as the risk of deviations of the real from the considered (anticipated or forecasted) change of the exchange rate in a certain time period. Since banks tend to be highly conservative we only assume the bank motive of “mild” speculation (favorable FC gaps are not closed) in contrast to “active” speculation (the bank actively tries to build up favorable FC gaps). The prevention of currency risk can be planned for periods $t = 1, \ldots, T$ . Formally,

$$
\begin{array}{l}f _ {5, t} \colon \mathbb {R} _ {+} ^ {p + q} \rightarrow \mathbb {R}, \text {cont.};\\f _ {5, t} \left(\underline {{x}} ^ {\text {new}}, \underline {{y}} ^ {\text {new}}, ^ {\mathrm{S}} \underline {{x}} _ {f, t} ^ {\text {new}}, ^ {\mathrm{B}} \underline {{x}} _ {f, t} ^ {\text {new}}\right)\\:= \left(^ {\mathrm{FC}} h _ {t} - R _ {e, t} ^ {\mathrm{FC}}\right) \cdot^ {\mathrm{FC}} e _ {0}\\\cdot \left(\sum_ {i = 1} ^ {p} ^ {\mathrm{FC}} c _ {i, t} ^ {\text {new}} \cdot^ {\mathrm{FC}} x _ {i} ^ {\text {new}} \right.\\\left. - \sum_ {j = 1} ^ {q} ^ {\mathrm{FC}} d _ {j, t} ^ {\text {new}} \cdot^ {\mathrm{FC}} y _ {j} ^ {\text {new}}\right)\\- \left(^ {\mathrm{S}} R _ {f, t} ^ {\mathrm{FC}} - R _ {e, t} ^ {\mathrm{FC}}\right) \cdot^ {\mathrm{FC}} e _ {0} \cdot^ {\mathrm{S}} x _ {f, t} ^ {\text {new}}\\- \left(R _ {e, t} ^ {\mathrm{FC}} - ^ {\mathrm{B}} R _ {f, t} ^ {\mathrm{FC}}\right) \cdot^ {\mathrm{FC}} e _ {0} \cdot^ {\mathrm{B}} x _ {f, t} ^ {\text {new}}\\+ ^ {\mathrm{FC}} e _ {0} \cdot \left(^ {\mathrm{FC}} c _ {t} ^ {\text {old}} \cdot \left(^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {\mathrm{A}} - R _ {e, t} ^ {\mathrm{FC}}\right) \right.\\\left. - ^ {\mathrm{FC}} d _ {t} ^ {\text {old}} \cdot \left(^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {\mathrm{L}} - R _ {e, t} ^ {\mathrm{FC}}\right)\right)\\- \left(^ {\mathrm{S}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}} - R _ {e, t} ^ {\mathrm{FC}}\right) \cdot^ {\mathrm{FC}} e _ {0} \cdot^ {\mathrm{S}} x _ {f, t} ^ {\text {old}}\\- \left(R _ {e, t} ^ {\mathrm{FC}} - ^ {\mathrm{B}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}}\right)\\. ^ {\mathrm{FC}} e _ {0} \cdot^ {\mathrm{B}} x _ {f, t} ^ {\text {old}} \rightarrow \min,\end{array}\tag{13}
$$

(I)

(II)

(III)

(IV)

whereby ${}^{FC}x_{i}/{}^{FC}y_{j}$ denote the decision variables of (future) FC A/L-positions, ${}^{S}x_{f,t}/{}^{B}x_{f,t}$ the sales and purchases of FC on the forward market in period t, ${}^{FC}c_{i,t}^{new}/{}^{FC}d_{i,t}^{new}$ the percentages of maturing (new) A/L, ${}^{FC}c_{t}^{old}/{}^{FC}d_{t}^{old}$ the amounts of maturing (old) A/L, ${}^{FC}h_{t}({}^{FC}\overline{h}_{t}^{\mathrm{A}}/{}^{FC}\overline{h}_{t}^{\mathrm{L}})$ the (average) considered exchange rate change of new (old) A/L-positions, ${}^{S}R_{f,t}^{FC}/{}^{B}R_{f,t}^{FC}$ ( ${}^{S}\overline{R}_{f,t}^{FC}/{}^{B}\overline{R}_{f,t}^{FC}$ ) the (average) forward rate change for new (old) forward sales and purchases, $R_{e,t}^{FC}$ the HC/FC exchange rate change in period t compared to t=0 and ${}^{FC}e_{0}$ the current HC/FC exchange rate in $t = 0$ . In addition the following definitions hold:

$$
\begin{array}{l} R _ {e, t} ^ {\mathrm{FC}} = \frac {\mathrm{FC} e _ {t} - \mathrm{FC} e _ {0}}{\mathrm{FC} e _ {0}}; \quad^ {\mathrm{FC}} h _ {t} = \frac {f _ {c t} ^ {\mathrm{FC}} e _ {t} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \\ ^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {A} = \frac {f _ {c t} ^ {\mathrm{FC}} \overline {{e}} _ {t} ^ {A} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \\ ^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {L} = \frac {f _ {c t} ^ {\mathrm{FC}} \overline {{e}} _ {t} ^ {L} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \quad^ {\mathrm{S}} R _ {f, t} ^ {\mathrm{FC}} = \frac {f _ {c t} ^ {\mathrm{FC}} e _ {t} ^ {\mathrm{S}} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \\ ^ {\mathrm{B}} R _ {f, t} ^ {\mathrm{FC}} = \frac {f _ {c t} ^ {\mathrm{FC}} e _ {t} ^ {\mathrm{B}} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \\ ^ {\mathrm{S}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}} = \frac {f _ {c t} ^ {\mathrm{FC}} \overline {{e}} _ {t} ^ {\mathrm{S}} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}; \quad^ {\mathrm{B}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}} = \frac {f _ {c t} ^ {\mathrm{FC}} \overline {{e}} _ {t} ^ {\mathrm{B}} - ^ {\mathrm{FC}} e _ {0}}{\mathrm{FC} e _ {0}}. \end{array}
$$

Therefore you have currency risk if (i) more (less) FC-assets than liabilities mature and the real exchange rate $^{FC}e_{t}$ is lower (higher) than the (average) considered/forecasted one $(_{fct}^{FC}e_{t}, _{fct}^{FC}\overline{e}_{t}^{A}, _{fct}^{FC}\overline{e}_{t}^{L};$ see I and II); (ii) the real exchange rate is higher (lower) than the (average) forward HC/FC sale (purchase) rate $(_{fct}^{S}e_{f,t}^{FC}, _{fct}^{S}\overline{e}_{f,t}^{FC}, (_{fct}^{B}e_{f,t}^{FC}(_{fct}^{B}\overline{e}_{f,t}^{FC}))$ ; see II and IV). This means there is currency risk if $(c = R_{e,t}^{FC})$ :

$$
\begin{array}{l} ^ {\mathrm{FC}} h _ {t} \left(^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {\mathrm{A}}\right) > c (\text {assets}); \\ ^ {\mathrm{FC}} h _ {t} \left(^ {\mathrm{FC}} \overline {{h}} _ {t} ^ {\mathrm{L}}\right) <   c (\text {liabilities}); \\ ^ {\mathrm{S}} R _ {f, t} ^ {\mathrm{FC}} \left(^ {\mathrm{S}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}}\right) <   c (\text {forw.sales}); \\ ^ {\mathrm{B}} R _ {f, t} ^ {\mathrm{FC}} \left(^ {\mathrm{B}} \overline {{R}} _ {f, t} ^ {\mathrm{FC}}\right) > c (\text {forw.buys}). \end{array}
$$

To get currency chances you just have to switch the inequality sign. The overall currency risk for one FC in one period is the sum of all risks and chances in this period. In order to calculate the overall currency risk of the bank resulting from the new business in period $t = 1$ we have to consider all currency risks in period $t = 1, \ldots, T$ . Formally the bank has the following objective function possibilities ((·) denotes ( $^{FC} \underline{x}^{new}$ , $^{FC} \underline{y}^{new}$ , $^{S} \underline{x}_{f,t}^{new}$ , $^{B} \underline{x}_{f,t}^{new}$ )) :

$$
f _ {5} ^ {1}, f _ {5} ^ {2}, f _ {5} ^ {3}, f _ {5} ^ {4}, f _ {5} ^ {5}: \mathbb {R} _ {+} ^ {p + q} \rightarrow \mathbb {R}, \text { cont. };
$$

$$
f _ {5} ^ {1} (\cdot) := \sum_ {t = 1} ^ {T} f _ {5, t} (\cdot) \cdot (1 + i) ^ {- t + 1} \rightarrow \min,\tag{15}
$$

$$
f _ {5} ^ {2} (\cdot) := \max _ {t} \left(f _ {5, t} (\cdot) \cdot (1 + i) ^ {- t + 1}\right)\rightarrow \min,\tag{16}
$$

$$
f _ {5} ^ {3} (\cdot) := \sum_ {t = 1} ^ {T} \max \left(f _ {5, t} (\cdot) \cdot (1 + i) ^ {- t + 1}, 0\right)\rightarrow \min,\tag{17}
$$

$$
f _ {5} ^ {4} (\cdot) := \max \left(\sum_ {t = 1} ^ {T} f _ {5, t} (\cdot) \cdot (1 + i) ^ {- t + 1}, 0\right)\rightarrow \min,\tag{18}
$$

$$
f _ {5} ^ {5} (\cdot) := \max _ {t} \left(f _ {5, t} (\cdot) \cdot (1 + i) ^ {- t + 1}, 0\right)\rightarrow \min.\tag{19}
$$

Which objective formulation should be chosen (you need one for every FC) depends on the bank's internal policy: (i) keeping a constant FC-business performance (but perform at least "mild" speculation) leads to $f_5^5(f_5^2)$ ; (ii) being concerned only about the overall currency risk over the planning horizon and prevent overall "mild" speculation, periodical "mild" speculation allow ("mild") speculation leads to $f_5^4$ , $f_5^3$ or $f_5^1$ . The bank's choice of (no) speculation determines whether the bank still tries to hedge forward when their FC-positions are already covered.

For the above currency risk we assume again that all uncertain exchange rates $\left(^{FC}e_{t,fct}\right)^{S}e_{f,t}^{FC},\quad\left.^{B}e_{f,t}^{FC}\right)$ can be estimated by the bank in form of scenarios (e.g. through bank experts or scientific theories like purchasing power parity (PPP) or interest rate parity (IRP)). Currency futures, options and swaps are not considered in this stage of the model.

Other quantitative objectives, e.g. to keep certain balance sheet ratios, can easily be included (as an objective or as a constraint) but will not be discussed here. Qualitative bank objectives, e.g. enlarging the number of branches or the customer service, cannot be pursued in such a quantitative model.

The constraints are basically legal (principles I–III of the German Banking Law (“KWG”), reserve requirements, etc.), policy or market (e.g. financial, accounting and management constraints, lower and upper growth limits through market forecasts) and model constraints (e.g. the balance equation).

## 3. Uncertainty and Target Risk

All objectives except $f_{2}$ contain uncertain parameters whose outcomes are known to the decision maker in form of scenarios given by the bank itself. To transform this stochastic into a deterministic problem you need an evaluation or decision method (“risk evaluation” [8]). We evaluated five major concepts of risk measures (decision methods) with respect to their applicability for our model: expected utility (or utility dominance), stochastic dominance, probability dominance, three parameter risk measure (3-PRM) and prospect ranking vectors (PRV) or bipolar risk measures.

The first three ones are theoretically good risk measures but require so many assumptions and/or additional data that they are practically unusable. For expected utility you need to specify a utility function which is almost impossible over multiple objective functions and decision variables. For stochastic and probability dominance you need to know all possible A/L-portfolio alternatives (totally unrealistic). Besides they are both basically a ranking measure.

Three parameter risk measures (or moments) [19] with mean variance as the oldest approach consist of two objective functions: (i) the expected value function of the corresponding uncertain function (to be maximized or minimized); (ii) a function that considers the possible deviation from the expected value in (i) or any other target value (target risk): $L(h, \lambda, \alpha) = \int_{-\infty}^{\lambda} |t - h|^{\alpha} \, \mathrm{d}F(t)$ . By varying the triple $(h, \lambda, \alpha)$ you also get well-known moments like the variance $(\mu(F(t)), \infty, 2)$ , the neg.semi-variance $(\mu(F(t)), \mu(F(t)), 2)$ , etc. H, $\lambda$ and $\alpha$ determine the DM's attitude towards a target or reference level h (e.g. the expected value), the outcomes to be included ( $\lambda$ ) and the relative importance of large versus small deviations ( $\alpha$ , grade of risk aversion).

The PRV-concept [6] basically is nothing other than the 3-PRM but it is defined by the bipolar risk theory, i.e. instead of just one target risk measure it considers at least two: one for the negative deviations from EV (the actual risk or the 'risk-pole' to be minimized) and one for the positive ones (possible changes, e.g. the pos. semi-variance, i.e. the 'speculative pole', to be maximized [5]). From a practical point of view 3-PRM and PRV are the only suitable concepts for our problem. In relation to the bank's (implicit) utility function $U(x)$ which we do not know we can make the following realistic assumptions with $RM =$ risk measure (deviations $>$ or $< 0$ ), $PRM =$ positive (deviations > 0) and NRM = negative risk measure (deviations < 0):

$$
\begin{array}{r l} E (U (x)) & = f (E (f _ {i}), R M (f _ {i}), P R M (f _ {i}), \\ & \quad N R M (f _ {i}), f _ {2}) \end{array}
$$

for $i = 1,3,4,5$

(20)

with the properties (for $i = 3,4,5$ )

$$
\begin{array}{l l} \frac {\delta E (U (x))}{\delta E (f _ {1} (x))} \geq 0; & \frac {\delta E (U (x))}{\delta R M (f _ {1} (x))} \leq 0; \\ \frac {\delta E (U (x))}{\delta P R M (f _ {1} (x))} \geq 0; \\ \frac {\delta E (U (x))}{\delta N R M (f _ {1} (x))} \leq 0; & \frac {\delta E (U (x))}{\delta E (f _ {i} (x))} \leq 0; \\ \frac {\delta E (U (x))}{\delta R M (f _ {i} (x))} \leq 0; \\ \frac {\delta E (U (x))}{\delta P R M (f _ {i} (x))} \leq 0; & \frac {\delta E (U (x))}{\delta N R M (f _ {i} (x))} \geq 0; \\ \frac {\delta E (U (x))}{\delta f _ {2} (x)} \geq 0. \end{array}
$$

The DM within the bank now has to decide in the model formulation step which one of the different model components, i.e. objectives and target risk measures, it would like to have simultaneously optimized. The chosen risk measure crucially depends on the bank's attitude towards risk (not necessarily pure risk aversion). A strongly risk averse bank for example may favor the 3-PRM approach with just one target risk measure and a higher $\alpha$ , whereas less risk averse banks may choose the PRV approach with a positive and a negative target risk measure and reasonably low $\alpha$ 's and a risk-neutral bank may just optimize the expected values.

## 4. Solution Algorithm

We have the following general vector optimization or MCDM problem:

$$
\begin{array}{l} F \colon \mathbb {R} ^ {n} \to \mathbb {R}; \\ F (\underline {{x}}) = \min (f _ {1} (\underline {{x}}), \dots , f _ {k} (\underline {{x}})) \quad \text { subject   to } \\ g _ {i} (\underline {{x}}) \leq 0 \quad \text { for } \quad i = 1, \dots , m; \end{array}\tag{21}
$$

$$
\begin{array}{l} h _ {j} (\underline {{x}}) = 0 \quad \text { for } \quad j = 1, \ldots , p; \\ x _ {l} \leq b _ {l}, x _ {l} \geq a _ {l} \quad \text { for } \quad l = 1, \ldots , n; \\ \underline {{x}} \geq 0, \underline {{x}} = (x _ {1}, \ldots , x _ {n}) \in \mathbb {R} ^ {n}; \end{array}
$$

whereby $\underline{x}$ is an $n$ dimensional decision variable vector and there are $k$ objectives, $m$ inequality, $p$ equality and $n$ box constraints. In order to get a solution, i.e. an efficient point $^{3}$ of the MCDM-problem, you can either set upper bounds to all but one objective and minimize the remaining one or you can create an overall objective (distance) function which includes all the obj. functions $f_{k}(\underline{x})$ and determines the efficient point by minimizing this function with respect to a chosen reference point (compromise solution) [9]. Since our problem is too complex to provide the complete set of efficient solutions, the DSS is interactive, delivers one efficient point at a time and thereby gives the DM the possibility to gradually screen the solution space and finally to reach the efficient point which maximizes his unknown utility function.

The DSS is based on a testing version of the non-linear DIDAS-NL program $[13]$ but it contains numerous additional interactive features and program improvements. The basic decision method is the reference point method by Wierzbicki $[21,22]$ . It works with the conjugate gradient method in connection with the shifted penalty algorithm for all constraints and gradient projection for linear constraints.

The original MCDM-problem is reduced to a single (distance) objective problem using a scalarizing achievement function (SAF) for the different objectives, formally,

$$
\begin{array}{l} s (\underline {{x}}) = 1 / n _ {0} \cdot \left(\sum_ {i = 1} ^ {n _ {0}} \left(w _ {i} (\underline {{x}})\right) ^ {p}\right) ^ {1 / p} \quad \text {with} \\ w _ {i} (\underline {{x}}) = s _ {i} \cdot \left(f _ {i} (\underline {{x}}) - \bar {f} _ {i}\right) / \left(r _ {i} - \bar {f} _ {i}\right). \end{array}\tag{22}
$$

$s_i$ is a scaling factor, $p$ the SAF-parameter, $r_i$ the reference point, $\bar{f}_i = \min[0.5 \cdot \min(f_i^*, r_i), \min(f^*, r_i) - 0.1)]$ an absolute lower bound and $f_i^*$ the utopia-point of objective $i$ .

$^{3}x^{*}\in\mathbb{R}^{n}$ is said to be efficient if there exists no other point $\bar{x}\in\mathbb{R}^{n}$ with $f_{i}(x^{*})\geq f_{i}(\bar{x})$ for all $i=1,\ldots,k$ and there exists at least one $j\in(1,\ldots,k)$ with $f_{j}(x^{*})>f_{j}(\bar{x})$ .

The auxiliary problem is defined as $P: \mathbb{R}^{n} \to \mathbb{R}$ ;

$$
\begin{array}{l} P (\underline {{x}}, \underline {{a}}, \underline {{b}}, \underline {{u}}, \underline {{v}}) \\ := s (\underline {{x}}) + 1 / 2 \cdot \sum_ {i = 1} ^ {m} a _ {i} \cdot \left(\max (0, g _ {i} (\underline {{x}}) + u _ {i})\right) ^ {2} \\ + 1 / 2 \cdot \sum_ {j = 1} ^ {p} b _ {j} \cdot \left(h _ {j} (\underline {{x}}) + v _ {j}\right) ^ {2} \end{array} \tag {23}
$$

and $a_{l} \leq x_{l} \leq b_{l} (l = 1, \ldots, n)$ whereby $u_{i} / v_{j}$ denote shift and $a_{i} / b_{j}$ penalty coefficients.

After getting a solution for P the shift/penalty coefficients are modified depending on the (non) violation of a constraint and the number of times that the coefficients were changed without finding a better solution for P. It has to be noted that because of the box constraints and the gradient projection P is always solved within the set of admissible solutions.

The conjugate gradient method, like other descent methods, first computes a descent direction vector

$$
\begin{array}{l} p _ {k} = - f ^ {\prime} (x _ {k}) + \beta_ {k} \cdot p _ {k - 1}, \\ \beta_ {k + 1} = - \frac {(f ^ {\prime} (x _ {k}) , f ^ {\prime} (x _ {k}) - f ^ {\prime} (x _ {k - 1})}{(f ^ {\prime} (x _ {k - 1}) , (f ^ {\prime} (x _ {k - 1}))} \end{array}\tag{24}
$$

and then during a line-search procedure finds $x_{k+1}=x_{k}+\alpha_{k}\cdot p_{k}$ whereby $\alpha$ fulfills $f(x_{k}+a_{k}\cdot p_{k})=\min_{\alpha\geq0}f(x_{k}+\alpha\cdot p_{k})$ and $p_{0}=-f'(x_{0})$ . After n steps (dimension of decision space) the process starts again.

Although originally designed to solve strict convex, differentiable, quadratic optimization problems the algorithm works well with basically all kinds of non-linear differentiable optimization problems and normally converges much faster than other comparable methods [15]. Since the algorithm for non-convex problems only gives local solutions you have to vary the starting points to obtain the global solution.

In our problem some of the objective functions $(f_{4b}, f_{5}^{2}-f_{5}^{5})$ and some risk measures, e.g. the neg. semi-variance $(\Sigma_{k}\max^{2}(0, E(t_{k})-t_{k})\cdot P(t_{k}))$ , are non-differentiable functions of the type $\min\max_{i}(f_{i})$ . Since the DSS only works with differentiable functions (or constraints) we transform the problem $F, f_{i}: R^{n}\to R, F(\underline{x}):=\max_{i}(f_{i}(x))\to\min$ into $\overline{F}, f_{i}: R^{n+1}\to R, \overline{F}(\underline{x}, x_{n+1}):=x_{n+1}\to\min$ subject to $x_{n+1}\geq f_{i}(\underline{x})$ for $i=1,\ldots,m$ . Thus substituted problem can be applied to all non-differentiable objectives/constraints of the aforementioned type.

The calculation of an efficient point stops (with success) when the gradient norm and the max. constraint violation are below the required limits.

## 5. Description and Features of the Decision Support System IDSSBALM

At present IDSSBALM basically is a traditional decision support system (DSS) whereby a DSS is defined as an interactive, computerized system which uses dialogue, databases and (mostly mathematical) methods to help DMs with the recognition of problems and the preparation, choice and implementation of decisions, strategies and/or alternatives (e.g. [10]).

Now one can distinguish between two principle versions of IDSSBALM: the current (implemented) and a future (final) version. In the current one the user basically has to perform three tasks before working with the DSS: (i) collect the necessary data, (ii) make his choice of the possible model components, i.e. objectives, constraints, etc. and (iii) store the problem (raw) data in certain data files: the general problem specifications (e.g. number of objectives, (in)equality constraints, etc.) in SPECS.DAT, the specific problem specifications (e.g. the linear coefficients, bounds, starting point, etc.) in MODEL.DAT and a (short) FORTRAN program containing the definition and the gradients of all objectives and all non-linear constraints. Nevertheless, almost all problem description parameters can be interactively changed. In addition the user has the chance to conduct a sensitivity analysis which is fairly easy for (lower or upper) bounds of decision variables, the right hand side of constraints and objectives and different objective settings whereby he can switch to a different set within MODEL.DAT (specifying a different BOU/RHS name) or the FORTRAN program (different problem number). For different scenarios however he still has to undergo the model building procedure from the beginning. The normal way to use the DSS is the following: the DM inputs raw data (e.g. the uncertain parameters) into STATISTICS and makes his choice(s) of objectives and constraints. Using the output of STATISTICS he then writes the FORTRAN program MODEL and specifies the two input files
MODEL.DAT and SPECS.DAT.

![](/api/attachments/CZMUJ5RE/fulltext/images/3622ac87de52197e29bf7a33813b1953002b7a3c5043dd544da3ab72b268ded3.jpg)  
Fig. 1. Current structure of IDSSBALM with pre-program tasks (→ or -->) and program execution (⇒).

As he interacts with the program, the DM has several types of command possibilities: SPECS and MODEL (change problem parameters or sets), PRINT (specify output media and the desire for intermediate results), OBJECT (change reference points or scaling factors), RESULT (display different kinds of results), START (manipulate starting points), OTHER (get help, show parameters) and RUN (compute solution or utopia points) commands.

Although our DSS does not (yet) contain a knowledge base, it does have a suitable and rather complicated OR-algorithm (see 4). Our model, which is a 'top down' approach for high level strategic planning [7] and can be split into several sub-models (for objectives and risk measures), is custom-built. The data still have to be collected externally but in an applied bank version this process should look as in fig. 2, whereby the necessary data would be provided internally on a regular basis by the forecasting, the accounting and the different functional departments in coordination with each other. Through this internal information and data system the central strategic planning unit could be freed from data research and could concentrate on model building and planning.

In a future version the model building step should be integrated (see fig. 3).

After processing the internal data, the DM, who is either a financial analyst (interpreter, intermediary; trained in mathematical programming) or a bank manager, could specify his model and problem structure by quite flexibly choosing among the different submodel possibilities without writing a program (in the current version the analyst is definitely needed, at least to input the correct model formulation). The bank manager might be able to conduct the model building himself using automatic model building tools [1] to make a choice from the submodel possibilities which are available. 'Interactive' so far in our DSS 'only' means that the DM can make a decision on the selection of (efficient) alternatives based on his preferences and change problem specifications. This might, however, also be worthwhile to help the DM in his model building process by asking him a catalogue of questions (e.g. about his level of risk aversion) and letting the system develop the model with the appropriate objectives in a way of extended support (e.g. [20]).

![](/api/attachments/CZMUJ5RE/fulltext/images/0b5389e14265202b981d40a90df31b8ac967755a9fb5fa3b6d4bf0a89f8ed776.jpg)  
Fig. 2. Possible applications of IDSSBALM with integrated information gathering.

![](/api/attachments/CZMUJ5RE/fulltext/images/563933c89c3920241c987ff5386a050c8817b476ab3e79df6cc5b7270b0d904b.jpg)  
Fig. 3. Possible application of IDSSBALM with internal and integrated model building.

The basic idea for the present interaction with IDSSBALM is that two types of users can work with it: (i) the sophisticated user (financial analyst) who knows the influence of the different parameters and wants to change them according to his needs, and (ii) the merely practical bank-oriented user, i.e. the bank manager himself, who is able – after the problem has been specified or the model has been formulated – to get the different efficient alternatives by just varying the reference points.

Since banks are very conservative it is quite complicated to get and work with real data. Therefore our examples so far are basically run with simulated data which have about the same structure as real ones (we are quite willing to cooperate with any bank).

The DSS is implemented on a VAX 8900 in FORTRAN. For problems of the example size you need 500–7.000 (on average 2.500) iterations to reach an efficient point depending on the chosen parameters and the starting point (average waiting time 3–6 sec.). For larger and more complex problems this time span can somewhat grow but it is still within an acceptable range.

IDSSBALM is different from DIDAS-NL in several aspects. First of all, it contains quite a few program changes, and improvements and interactive command types, e.g. PRINT, RESULT, START, OTHER and a few options of the other types. Although the solver principally has not been changed IDSSBALM is much more user-friendly and provides results in a meaningful way (e.g. [2]; there is a new, improved DIDAS-NL PC-version to be coming out at the end of 1987 [11] but our model is too large to be run on a PC for a suitable problem size) although its comfort might still be improved (e.g. with a screen able to run in graphics mode). Besides, DIDAS-NL is a general non-linear MCDM DSS while IDSS-BALM, considering model and DSS, is tailored to a special problem environment. Within the DIDAS family of multi-objective DSS, linear ones are already widely used but for the non-linear one we did not hear about other applications so far besides water pollution control problems.

## 6. Example

Because of the limited space we provide a small sample data in a condensed form (not the original program in- or output) in table 1, whereby ST (MT, LT) = short- (medium-, long-) term; B (NB) = (non) bank customers; CL (LI) = claims (liabilities); P (C) = private (corporate) customers; $x_3$ denotes bills of exchange, $x_2$ deposits held at the Federal Bank and $x_{14}$ investments in other corporations, plant and equipment. The bank is assumed to be risk-neutral towards target risk, does not work in FC and has 3 basic objectives: (i) max. the expected returns on interest business, (ii) max. the balance volume and (iii) min. the expected credit risk:

$$
\begin{array}{l}\bar {f} _ {1} = E \left(f (\underline {{x}} ^ {\text { new }})\right)\rightarrow \max.; \quad \bar {f} _ {2} = f _ {2} ^ {1} (\underline {{x}} ^ {\text { new }}) \rightarrow \max.;\\\bar {f} _ {3} = E \left(f _ {3} ^ {1} (\underline {{x}} ^ {\text { new }})\right)\rightarrow \min.\end{array}
$$

In addition we have the following constraints: Reserve requirements (g1), German banking law principles I (g2), II and III (g3) and §12 (g4), a required cash position (g5), available capital stock (g6), balance equation (g7, g8) and a managerial balance structure constraint (g9).

$$
\begin{array}{r l} (g 1) & 1. 0 5 x _ {2} + 0. 0 8 7 x _ {1 8} + 0. 0 4 5 x _ {1 9} + 0. 0 3 7 5 x _ {2 1} \\ & + 0. 0 2 2 5 x _ {2 2} \leq - 4. 1 6 9 1; \end{array}
$$

$$
(g 4) x _ {1 4} - x _ {2 3} \leq 1. 6;
$$

$$
\begin{array}{r l} (g 5) - x _ {1} + 0. 0 0 5 \cdot (x _ {1 5} + x _ {1 6} + x _ {1 8} + x _ {1 9} + x _ {2 1}) \\ & \leq - 0. 4 1 0 5; \end{array}
$$

$$
0. 2 \cdot \sum_ {i = 4} ^ {6} x _ {i} + \sum_ {i = 7} ^ {1 2} x _ {i} + x _ {1 4} - 1 8 x _ {2 3} \leq 1 4 7 3 2 0. 0;\tag{g2}
$$

$$
\begin{array}{l} (g 3) 0. 2 x _ {5} + \sum_ {i = 6} ^ {1 2} x _ {i} + 0. 1 x _ {1 5} + 0. 5 x _ {1 6} - x _ {1 7} \\ \qquad - 0. 7 \cdot (x _ {1 8} + x _ {1 9}) - x _ {2 0} - 0. 8 x _ {2 1} \\ \qquad - x _ {2 2} - x _ {2 3} \leq 4. 6 1; \end{array}
$$

Parameter Values (Amounts in Mill. of DM).

<table><tr><td>Var</td><td>Name</td><td> $\bar{x}_{i}^{old}$ </td><td> $rx_{i}^{old}$ </td><td> $rx_{i}^{new}$ </td><td> $^{n}rx_{i}$ </td><td> $a_{1,i}^{old}$ </td><td colspan="3"> $xcr_{i}^{old}(\%)$ </td><td colspan="3"> $xcr_{i}^{new}(\%)$ </td></tr><tr><td> $x_{1}$ </td><td>CASH</td><td>0.6</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $x_{2}$ </td><td>RESERVE</td><td>5.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td> $x_{3}$ </td><td>BILLEX</td><td>4.0</td><td>5.5</td><td>6.0</td><td>5.75</td><td>0.3</td><td>0.55</td><td>0.7</td><td>0.85</td><td>0.5</td><td>0.6</td><td>0.7</td></tr><tr><td> $x_{4}$ </td><td>STBCL</td><td>25.0</td><td>6.0</td><td>6.5</td><td>6.25</td><td>0.3</td><td>0.1</td><td>0.1</td><td>0.15</td><td>0.1</td><td>0.1</td><td>0.15</td></tr><tr><td> $x_{5}$ </td><td>MTBCL</td><td>9.0</td><td>7.0</td><td>7.75</td><td>7.5</td><td>0.2</td><td>0.15</td><td>0.2</td><td>0.2</td><td>0.15</td><td>0.15</td><td>0.2</td></tr><tr><td> $x_{6}$ </td><td>LTBCL</td><td>28.0</td><td>8.0</td><td>8.75</td><td>8.5</td><td>0.1</td><td>0.25</td><td>0.3</td><td>0.35</td><td>0.2</td><td>0.25</td><td>0.3</td></tr><tr><td> $x_{7}$ </td><td>STNBCLP</td><td>14.0</td><td>8.0</td><td>9.0</td><td>7.75</td><td>0.5</td><td>0.45</td><td>0.5</td><td>0.6</td><td>0.35</td><td>0.45</td><td>0.55</td></tr><tr><td> $x_{8}$ </td><td>STNBCLC</td><td>9.0</td><td>7.5</td><td>8.25</td><td>8.0</td><td>0.5</td><td>1.2</td><td>0.8</td><td>0.7</td><td>0.8</td><td>0.65</td><td>0.5</td></tr><tr><td> $x_{9}$ </td><td>MTNBCLP</td><td>8.0</td><td>9.0</td><td>10.0</td><td>9.5</td><td>0.3</td><td>0.5</td><td>0.6</td><td>0.75</td><td>0.45</td><td>0.5</td><td>0.6</td></tr><tr><td> $x_{10}$ </td><td>MTNBCLC</td><td>6.0</td><td>8.5</td><td>9.25</td><td>9.0</td><td>0.2</td><td>1.25</td><td>1.05</td><td>0.95</td><td>0.9</td><td>0.7</td><td>0.6</td></tr><tr><td> $x_{11}$ </td><td>LTNBCLP</td><td>50.0</td><td>10.0</td><td>11.25</td><td>10.75</td><td>0.1</td><td>0.55</td><td>0.65</td><td>0.75</td><td>0.5</td><td>0.6</td><td>0.75</td></tr><tr><td> $x_{12}$ </td><td>LTNBCLC</td><td>36.0</td><td>9.5</td><td>10.25</td><td>9.75</td><td>0.1</td><td>1.75</td><td>1.45</td><td>1.15</td><td>1.05</td><td>0.9</td><td>0.75</td></tr><tr><td> $x_{13}$ </td><td>BONDS</td><td>20.0</td><td>10.0</td><td>11.5</td><td>11.0</td><td>0.2</td><td>0.25</td><td>0.35</td><td>0.55</td><td>0.25</td><td>0.35</td><td>0.5</td></tr><tr><td> $x_{14}$ </td><td>INVEST</td><td>13.0</td><td>7.5</td><td>8.0</td><td>7.75</td><td>-</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.15</td><td>0.25</td></tr><tr><td></td><td>Σ</td><td>228.0</td><td></td><td></td><td colspan="2"> $P(xcr_{k})=$ </td><td>0.25</td><td>0.65</td><td>0.1</td><td>0.25</td><td>0.65</td><td>0.1</td></tr><tr><td></td><td></td><td> $\bar{y}_{j}^{old}$ </td><td> $ry_{j}^{old}$ </td><td> $ry_{j}^{new}$ </td><td> $^{n}ry_{j}$ </td><td> $b_{1,j}^{old}$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{15}$ </td><td>STBLI</td><td>22.0</td><td>3.25</td><td>3.75</td><td>3.75</td><td>0.3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{16}$ </td><td>MTBLI</td><td>4.0</td><td>3.75</td><td>4.25</td><td>4.0</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{17}$ </td><td>LTBLI</td><td>18.0</td><td>4.25</td><td>4.75</td><td>4.5</td><td>0.1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{18}$ </td><td>STNBLI</td><td>28.0</td><td>3.0</td><td>3.5</td><td>3.25</td><td>0.4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{19}$ </td><td>MTNBLI</td><td>15.0</td><td>3.5</td><td>4.0</td><td>3.75</td><td>0.1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{20}$ </td><td>LTNBLI</td><td>26.0</td><td>4.0</td><td>4.75</td><td>4.5</td><td>0.1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{21}$ </td><td>SAVINGS</td><td>46.0</td><td>5.0</td><td>5.5</td><td>5.25</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{22}$ </td><td>BONDS</td><td>40.0</td><td>3.0</td><td>3.5</td><td>3.25</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $x_{23}$ </td><td>CAPSTO</td><td>15.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Σ</td><td>228.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

$$
(g 6) - x _ {2 3} + \sum_ {i = 1} ^ {1 4} ^ {n} r x _ {i} \cdot x _ {i} - \sum_ {j = 1 5} ^ {2 2} ^ {n} r x _ {j} \cdot x _ {j} \leq 2. 0;
$$

$$
(g 7) \sum_ {i = 1} ^ {1 4} x _ {i} - \sum_ {j = 1 5} ^ {2 3} x _ {j} \leq 5. 3 0 1;
$$

$$
(g 8) - \sum_ {i = 1} ^ {1 4} x _ {i} + \sum_ {j = 1 5} ^ {2 3} x _ {j} \leq - 5. 2 9 9;
$$

$$
(g 9) x _ {6} + x _ {1 1} + x _ {1 2} / \sum_ {i = 4} ^ {1 2} x _ {i} \leq 0. 3 5.
$$

The box constraints (market constraints based on forecasts and management politics) are listed in table 3.

As an example we conducted 4 different strategies to get an efficient point each: a) a maximal return strategy ( $\bar{f}_{2}$ and $\bar{f}_{3}$ are less important), b) a minimal credit risk strategy ( $\bar{f}_{1}$ and $\bar{f}_{2}$ are less important), c) a maximal balance volume strategy ( $\bar{f}_{1}$ and $\bar{f}_{3}$ are about equally important) and d) a mixed strategy with a required low credit risk.

Tables 2 and 3 give the objective function/constraints values and the decision variables.

Strategy (a) results in the best possible return (liabilities are at their upper bounds, cash and reserves are quite low) with comparably high credit risk. Strategy (b) sets risk-bearing assets to their lower limits (the structural constraint is also at its limit). Strategy (c) gets a maximal balance volume. Strategy (d) lies in between them all.

Lower and Upper Bounds and Decision Variable Values for Strategies (a)-(d) (amounts in mill. of DM).  
Objective Function/Constraint Values of Efficient Points for Strategies (a)-(d) (amounts in mill. of DM).

<table><tr><td rowspan="2">Name</td><td colspan="5">Values of</td></tr><tr><td>Up bnd</td><td>(a)</td><td>(b)</td><td>(c)</td><td>(d)</td></tr><tr><td>f1</td><td>500.0</td><td>11.851</td><td>8.677</td><td>11.74</td><td>10.498</td></tr><tr><td>f2</td><td>500.0</td><td>270.755</td><td>206.2</td><td>273.4</td><td>246.5</td></tr><tr><td>f3</td><td>10.0</td><td>1.45</td><td>1.174</td><td>1.459</td><td>1.33</td></tr><tr><td>g1</td><td>-4.169</td><td>-4.169</td><td>-7.376</td><td>-4.805</td><td>-5.77</td></tr><tr><td>g2</td><td>147.32</td><td>-81.269</td><td>-60.945</td><td>-75.691</td><td>-77.677</td></tr><tr><td>g3</td><td>4.61</td><td>-2.174</td><td>-2.313</td><td>-4.417</td><td>-2.189</td></tr><tr><td>g4</td><td>1.6</td><td>-6.001</td><td>-3.989</td><td>-5.691</td><td>-5.126</td></tr><tr><td>g5</td><td>-0.41</td><td>-0.411</td><td>-0.945</td><td>-0.728</td><td>-0.806</td></tr><tr><td>g6</td><td>-2.0</td><td>-3.481</td><td>-3.227</td><td>-3.269</td><td>-3.731</td></tr><tr><td>g7</td><td>5.301</td><td>5.301</td><td>5.3</td><td>5.3</td><td>5.3</td></tr><tr><td>g8</td><td>-5.299</td><td>-5.301</td><td>-5.3</td><td>-5.3</td><td>-5.3</td></tr><tr><td>g9</td><td>0.35</td><td>0.318</td><td>0.35</td><td>0.318</td><td>0.314</td></tr></table>

One can also see that the optimization of objectives $\bar{f}_{1}$ and $\bar{f}_{2}$ leads to quite similar solutions (they seem to be highly correlated although the degree of correlation does not have to be the same over the efficient set) while $\bar{f}_{3}$ contradicts $\bar{f}_{1}$ and partially $\bar{f}_{2}$ .

<table><tr><td>Name</td><td>Lo bnd</td><td>Up bnd</td><td>(a)</td><td>(b)</td><td>(c)</td><td>(d)</td></tr><tr><td> $x_1$ </td><td>0.0</td><td>1.0</td><td>0.663</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td> $x_2$ </td><td>0.0</td><td>7.5</td><td>6.754</td><td>7.5</td><td>7.5</td><td>7.5</td></tr><tr><td> $x_3$ </td><td>0.5</td><td>2.4</td><td>0.855</td><td>0.5</td><td>2.4</td><td>0.5</td></tr><tr><td> $x_4$ </td><td>3.0</td><td>15.0</td><td>14.996</td><td>3.0</td><td>15.0</td><td>10.884</td></tr><tr><td> $x_5$ </td><td>0.3</td><td>3.6</td><td>3.598</td><td>0.3</td><td>3.6</td><td>0.786</td></tr><tr><td> $x_6$ </td><td>1.0</td><td>5.6</td><td>5.598</td><td>1.0</td><td>5.6</td><td>4.795</td></tr><tr><td> $x_7$ </td><td>2.5</td><td>14.0</td><td>13.598</td><td>2.5</td><td>14.0</td><td>12.164</td></tr><tr><td> $x_8$ </td><td>2.0</td><td>9.0</td><td>8.997</td><td>2.0</td><td>9.0</td><td>6.134</td></tr><tr><td> $x_9$ </td><td>1.0</td><td>4.8</td><td>4.799</td><td>1.0</td><td>4.8</td><td>2.63</td></tr><tr><td> $x_{10}$ </td><td>0.5</td><td>2.4</td><td>2.4</td><td>0.5</td><td>2.4</td><td>0.5</td></tr><tr><td> $x_{11}$ </td><td>2.5</td><td>10.0</td><td>10.0</td><td>2.5</td><td>10.0</td><td>7.335</td></tr><tr><td> $x_{12}$ </td><td>1.5</td><td>7.2</td><td>7.199</td><td>1.5</td><td>7.2</td><td>2.995</td></tr><tr><td> $x_{13}$ </td><td>1.5</td><td>8.0</td><td>8.0</td><td>1.5</td><td>8.0</td><td>6.673</td></tr><tr><td> $x_{14}$ </td><td>0.0</td><td>1.5</td><td>1.499</td><td>0.0</td><td>1.5</td><td>1.204</td></tr><tr><td> $x_{15}$ </td><td>2.5</td><td>6.0</td><td>5.998</td><td>2.647</td><td>5.667</td><td>4.829</td></tr><tr><td> $x_{16}$ </td><td>0.3</td><td>6.2</td><td>6.2</td><td>0.45</td><td>5.864</td><td>1.042</td></tr><tr><td> $x_{17}$ </td><td>1.0</td><td>3.6</td><td>3.599</td><td>1.16</td><td>3.26</td><td>2.43</td></tr><tr><td> $x_{18}$ </td><td>3.0</td><td>22.4</td><td>22.398</td><td>3.136</td><td>22.068</td><td>13.873</td></tr><tr><td> $x_{19}$ </td><td>1.0</td><td>3.0</td><td>2.999</td><td>1.146</td><td>2.665</td><td>1.829</td></tr><tr><td> $x_{20}$ </td><td>1.5</td><td>6.6</td><td>6.599</td><td>1.661</td><td>6.26</td><td>4.719</td></tr><tr><td> $x_{21}$ </td><td>3.5</td><td>18.4</td><td>12.766</td><td>3.675</td><td>18.056</td><td>17.229</td></tr><tr><td> $x_{22}$ </td><td>1.5</td><td>16.0</td><td>15.996</td><td>1.636</td><td>15.668</td><td>7.519</td></tr><tr><td> $x_{23}$ </td><td>0.0</td><td>7.5</td><td>7.5</td><td>7.5</td><td>7.191</td><td>6.33</td></tr></table>

## 7. Conclusion

IDSSBALM is an (interactive) decision support system which is able to consider today's urgent bank planning problems and objectives and comprise them in a way which is attractive to both experienced and inexperienced (practical) users. The model contains several submodels which can be combined in a flexible manner. Considering uncertainty and letting the user apply his own approach and (intuitive) opinion about the major objectives, his attitude towards risk (which does not have to be consistent) and his (implicit) utility function within the model environment allows him to find his own best solution to the problem by specifying his preferences. IDSSBALM is therefore a valuable decision aid.

## References

[1] M. Binbasioglu, M. Jarke. Domain Specific DSS Tools for Knowledge-Based Model Building. Decision Support Systems 2 (1986), 213–223.

[2] J.J. Brennan, J.J. Elam. Understating and Validating Results in Model-Based Decision Support Systems. Decision Support Systems 2 (1986), 49–54.

[3] W. Bühler. Anlagestrategien zur Begrenzung des Zinsänderungsrisikos von Portefeuilles aus festverzinslichen Titeln, Zeitschrift für betriebswirtschaftliche Forschung. Sonderheft 16/1983, 82–137.

[4] K.J. Cohen, S. Maier, J. van der Weide. Recent Developments in Management Science, Vol. 22, No. 10 (Oct. 1980), 1097–1119.

[5] G. Colson. The Bipolar Theory of Risk in Finance: A Tutorial. Paper presented at the 2.Meeting of the Euro Working Group on Financial Modelling, Paderborn, FRG, Nov. 19–20, 1987.

[6] G. Colson, M. Zeleny. Uncertain Prospects Ranking and Portfolio Analysis under the Conditions of Partial Information. Oelgeschläger, Gunn & Hain, Cambridge, MA., Anton Hain, 1980.

[7] D.R. Dolk. Data as Models: An Approach to Implementing Model Management. Decision Support Systems 2 (1986), 73–80.

[8] Y.Y. Haimes, M. Leach. Risk Assessment and Management in a Multiobjective Framework. In: Lecture Notes in Economics and Mathematical Systems 242 - Decision Making with Multiple Objectives - Proceedings (eds. Y.Y. Haimes and V. Chankong). Cleveland, Ohio 1984, 23-35.

[9] C.-L. Hwang, A. Masud. Multiple Objective Decision Making – Methods and Applications – A State-of-the-Art Survey. Lecture Notes in Economics and Mathematical Systems 164, Springer Verlag 1979.

[10] M. Jarke. Kopplung qualitativer und quantitativer Theorien in der Entscheidungsunterstützung. Fakultät für Mathematik und Informatik, Universität Passau, MIP-8716, August 1987.

[11] T. Kreglewski, J. Pacziynski, A. Wierzbicki. A Version of Nonlinear DIDAS for an IBM PC Computer. Lecture held at the IIASA International Workshop on Methodology and Software for Interactive Decision Support in Albena, Bulgaria, oct. 19–23, 1987.

[12] D. Langen. Strategic Bank Asset Liability Management - A Multi-Objective Decision Model and Decision Support System for Strategic Bank Asset Liability Management. Peter Lang Verlag, Frankfurt–Genf, 1989.

[13] A. Lewandowski, T. Kreglewski, T. Rogowski. DIDAS-NL - A Nonlinear Version of DIDAS System. Software, Theory and Testing Examples in Decision Support Systems, by A. Lewandowski and A. Wierzbicki (eds.), IIASA, August 1985, 128–141.

[14] W. Mair. Die reale Effektivverzinsung. Österreichisches Bank-Archiv, 19.Jg.(1971), Heft 10, 334–348.

[15] B.N. Psenicnyj, J.M. Danilin. Numerische Methoden für Extremalwertaufgaben. Deutscher Verlag der Wissenschaften, Berlin, 1982.

[16] B. Rudolph. Eine Strategie zur Immunisierung der Portfeuilleentnahmen gegen Zinsänderungsrisiken. Zeitschrift für die betriebswirtschaftliche Forschung 1/1981, 22–35.

[17] A.M. Santomero. Modelling the Banking Firm - A Survey. Journal of Money, Credit and Banking, Vol. 16, No. 4 (Nov. 1984), part 2, 576-602.

[18] R. Schmidt. Neuere Entwicklungen der modellgestützten Gesamtplanung von Banken. Zeitschrift für Betriebswirtschaft, 53.Jg.(1983), Heft 3, 304–318.

[19] B.K. Stone. A General Class of Three-Parameter Risk Measures. Journal of Finance 28 (1973), 675–685.

[20] Universität Passau. Fakultät für Mathematik und Informatik, Wirtschaftswissenschaftliche Fakultät. Interaktive Entscheidungsunterstützungssysteme. DFG-Sonderforschungsbereich, Finanzierungsantrag 1987–1988–1989, November 1986.

[21] A. Wierzbicki. A Mathematical Basis for Satisficing Decision Making. IIASA Working Paper WP-80-90, May 1980.

[22] A. Wierzbicki. On the Completeness and Constructiveness of Parametric Characterizations to Vector Optimization Problems. OR Spektrum Vol. 8, 1986, No. 2, 73–88.
