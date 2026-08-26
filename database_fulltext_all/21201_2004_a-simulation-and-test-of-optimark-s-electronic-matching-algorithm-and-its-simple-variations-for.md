---
otero_id: 21201
otero_key: "QSGWYFRC"
title: "A simulation and test of OptiMark's electronic matching algorithm and its simple variations for institutional block trading"
authors: "Christian Gerber; Jeffrey Teich; Hannele Wallenius; Jyrki Wallenius"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00146-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A simulation and test of OptiMark’s electronic matching algorithm and its simple variations for institutional block trading

Christian Gerber<sup>a</sup>, Jeffrey Teich<sup>b,c</sup>, Hannele Wallenius<sup>d,</sup>\*, Jyrki Wallenius<sup>e</sup>

<sup>a</sup> IBM Germany, Erzgießereistr. 21, Mu¨nchen 80335, Germany

<sup>b</sup> Rotterdam School of Management, Erasmus University, POB 1738, 3000 DR Rotterdam, The Netherlands

<sup>c</sup> Department of Management, New Mexico State University, Las Cruces, NM 88003, USA <sup>d</sup> Department of Industrial Engineering and Management, Helsinki University of Technology, POB 9500, 02015 HUT Helsinki, Finland <sup>e</sup> Helsinki School of Economics, POB 1210, 00101 Helsinki, Finland

Received 1 July 2002; accepted 18 August 2002

## Abstract

OptiMark, an automated crossing system that matches institutional buyers and sellers of company stock, is simulated via a multi-agent system. The results are contrasted with two algorithm variations, which are based on a cruder rating system. Performance measures include the volume of stocks traded, the extent of price discrimination, trader utility, efficiency of matches, and processing time. Our results indicate that the cruder rating schemes perform as well as the original version for moderately sized markets. Yet, a test with human subjects implies that our crudest preference elicitation scheme appears simpler to use than the original scheme. We hope that this finding will help resolve some recent problems that OptiMark’s system has faced concerning the difficulty of use. C.2002. E1sevier Sci ence B V All rigk

Keywords: Electronic trading; Multiagent simulation; Behavioral experimentation

## 1. Introduction

OptiMark (http://www.optimark.com) has developed an electronic matching algorithm for the purpose of reducing the market impact of large stock market transactions ([3]; see also Ref. [5]). The idea is that large institutional investors will be matched together, based on their expressed preferences, anonymously, so that markets do not have time to react to the buy/sell orders that would occur in traditional stock markets.

Traders express their preferences over both quantity and price.

Parallel to the emergence of electronic stock markets and the growth of electronic commerce in general, agent-based systems are becoming more and more mature for applications distributed over large networks, such as the Internet. Although the types of applications vary, ranging from information retrieval to electronic commerce, such systems can be supported, simulated or implemented by agent techniques. We use multiagent simulation technology to compare OptiMark’s original algorithm to two simple variations, which we have described in Teich et al. [7]. We have argued that OptiMark’s preference elicitation is (too) sophisticated and may for that reason be cumbersome and not user friendly.<sup>1</sup> We wish to investigate whether the adoption of a cruder preference elicitation scheme would negatively impact the performance of OptiMark’s algorithm. Our argument is that, if not, then the cruder preference elicitation schemes should be used.

This paper is organized as follows. OptiMark’s algorithm and the proposed variations are overviewed in Section 2. An agent-based implementation of Opti-Mark’s algorithm is discussed in Section 3. The performance measures and the results of our simulations are described in Section 4. In Section 5 we report the results of an experiment with human subjects focusing on the ease of use of the different variations. Section 6 concludes the paper.

## 2. Description of OptiMark’s algorithm

## 2.1. OptiMark’s original algorithm

The OptiMark system has originally been described in Ref. [3] (see also Ref. [1]). In the OptiMark system, two issues—price of stock and quantity traded—are crossed in the market. The motivation is to reduce the market impact of large institutional trades by encouraging traders to (anonymously) state preferences across ranges of price and quantity. These preferences are used to match buyers and sellers. Large traders may be willing to accept a higher or lower price than the current market price for such large volumes of trades. In economic terms, they try to eliminate the shifts of demand or supply curves when new buyers/sellers enter or exit the market.

We have reproduced three figures from OptiMark’s web site and explain their electronic market system based on them. See Figs. 1–3.

In Fig. 1, a buyer’s satisfaction density profile is exhibited. The size/price combinations are assigned a satisfaction value ranging from 0 to 1; a value of 0 indicates unwillingness to trade at that price/size combination; a value of 1 indicates the highest level of satisfaction. Discrete levels of types 0.1, 0.2, 0.3 are inserted, with values in between allowed for the contours, higher values indicating higher levels of preference for that price/size trade. Every trader is required to indicate his/her satisfaction profiles for each stock he/she wants to trade, using the 0 to 1 scale; however, the actual detail and accuracy will vary from trader to trader.

OptiMark then matches buyers and sellers based on a two-stage system. Fig. 2 explains the aggregation procedure, which is the first stage. Starting with the size/price cells containing a value ‘‘1’’ for both buyer and seller, the algorithm attempts to match traders by combining/aggregating smaller quantity traders to larger quantity traders at a single price. In the second stage, in Fig. 3, for remaining buyer – seller combinations, a ‘‘mutual satisfaction density profile value’’ is calculated by multiplying the individual satisfaction density profiles. They define the mutual satisfaction density profile between the ith buyer and the kth seller to be the cross products of the buyer’s and seller’s satisfaction values for each price–size combination. The matching is based on the ranked list of the cross products for all price/size cells.

![](/api/attachments/QSGWYFRC/fulltext/images/5eacacce88dbb432273e97420855971e530cd5b55cade6183e3a309e1e09c66c.jpg)  
Fig. 1. OptiMark: buyer’s satisfaction density profile. Source: http:// www.OptiMark.com.

![](/api/attachments/QSGWYFRC/fulltext/images/3cbe7c1b81a2fb538cfca8a478cade72e0d2ddeeb3b4172dacd8fa9252a276e3.jpg)  
Fig. 2. OptiMark aggregation stage. Source: http://www.OptiMark. com.

In case of multiple matches with equal utilities, rules exist to break such ties. They include the importance of the trader, time of entry, and trade size. (Source: Private communication with OptiMark President, Dr. T. Rickard; see Teich et al. [7]).

OptiMark’s system does indeed have several appealing features: anonymity, possible elimination of market impact, preference elicitation over two (or more in other e-commerce applications) issues, and the aggregation of small trades matched with larger quantities. OptiMark allows price discrimination, that is, trading same stocks at the same time at different prices.

## 2.2. Critique and simple variations of OptiMark’s algorithm

In Ref. [7] we have criticized OptiMark’s 0, 0.1, 0.2, $\ldots , 0 . 9 ,$ 1 preference elicitation scale, where scores in between 0 and 1 differentiate between levels of preference. The elicitation task seems very complicated to be done every 90 s or even every few minutes, even though OptiMark has argued that traders can input preference scores as ‘quick and dirty’ as they desire. (Early experience with the algorithm helped OptiMark to determine that matching every 90 s resulted in low liquidity so the matching cycle time was extended.) We have questioned why traders would be willing to furnish preference scores between 0 and 1 with their system and wonder why they do not specify a unique single (‘feasible’) best $^ { \circ } 1 ^ { \circ }$ cell. Furthermore, some traders may be more skilful than others in strategically manipulating scores to gain advantage over other traders. Obviously, inter-personal comparisons of values/preference scores cannot be made. We suggest the use of a cruder scale. Furthermore, even if traders shared the same preference scale and accurately represented it, ranking the cells based on the product of preference scores is arbitrary. This is equivalent to the Nash bargaining solution, which has been criticized in the negotiation literature [4].

We have proposed two simple preference elicitation schemes [7]. The first is based on a 0 – 4 (0, 1, 2, 3, 4) scheme and the second on an even cruder 0–2 (0, 1, 2) scheme. In the 0–4 scheme a trader will only specify a single best $\cdot _ { 4 } ,$ value, as well as at most a single ‘2’ value. The interpretation is that $\cdot _ { 4 } ,$ is best of ‘3s’ and $\cdot _ { 2 } \cdot $ is best of ‘1s’. Likewise, in the 0–2 scheme a trader would specify only a single best $\bullet _ { 2 } \bullet _ { }$ value. The 0– 4 and the 0–2 scales are ‘quick and dirty’ and fairly easy to specify. In both of these scales, the maximum of the minimum scores is the same as the maximum of the cross products, which is untrue in the original Opti-

![](/api/attachments/QSGWYFRC/fulltext/images/617ccf3522e890abaf55b79977bade7bfd6a0fa898cb9bd44a93985257974e58.jpg)  
Fig. 3. OptiMark Cross Products in Stage 2. Source: http:// www.OptiMark.com.

Mark scheme. According to Raiffa [4], the max–min rule may be fairer than the max cross product rule. These perceived benefits are offset by the additional cost of an increased number of ties, which must be resolved one way or another. There will be ties, especially on the ‘‘one’’ cross products. Possible tie breaker rules follow. If there are still ties remaining, we use the original OptiMark rules. Our description is specifically tailored for the 0–2 scheme.

(1) Count the number of ties for each pair. Start matching based on the largest number of ties (1s most likely). Mark the tied region. Select from the individual utility matrices the two peek points where the 2s (in the 0 – 2 scheme) or 4s (in the 0 –4 scheme) have been inserted. Due to the definition, there exist only two such points. For each matching pair, draw a line in the mutual utility matrix through those two points. All points on such a line are Pareto-optimal, if a Gaussian utility distribution around the peek points is assumed. If the line passes through the marked region, select the cell where the midpoint of the line segment passing through the marked region is located. If the line does not pass through the marked region, then select the cell that is closest to the overall midpoint of the line connecting the two best cells.

(2) Force the matches, which simply maximize the quantity of shares traded. The true maximum quantity would be computationally difficult to calculate with a large number of tied traders. Therefore, we suggest a greedy heuristic to approximate this maximum quantity by simply calculating for all tied traders the maximum quantity for each paired buyer/seller combination.

## 3. Agent-based implementation of OptiMark’s algorithm and its variations

We next describe our implementation of the original OptiMark algorithm and our simple variations, where the Central Matching Controllers (CMC) and the traders were realized as agents. We make use of the generic agent toolbox Social Interaction Framework (SIF). A detailed description of SIF can be found in Ref. [2]. To make sure that the implemented algorithm was the same as OptiMark’s original algorithm, we studied and followed the patent specifications, had discussions with Dr. Rickard from OptiMark, and compared the results of our simulations against the original algorithm with the help of an example.

## 3.1. The multi-agent system SIF

SIF’s underlying basic mechanism is the Effector-Medium-Sensor (EMS) architecture based on Russell and Norvig’s [6] definition of an agent acting and interacting with its environment and other agents:

An agent is an entity that can be viewed as perceiving its environment through sensors and acting upon that environment through effectors.

SIF is a JAVAk library, which supports agentoriented programming. It consists of a scenario-independent simulation engine and a number of ready-touse components. SIF contains a mechanism to specify simulations in a simple script language. These scripts can be loaded, modified and reloaded by using the graphical user interface (GUI).

The SIF agent framework reflects the EMS paradigm (Fig. 4). EMS provides an appropriate abstraction of an agent acting and interacting with its environment and other agents. The central component of the architecture is the medium. Effectors emit actions to the medium, which in turn sends the effect as percepts to sensors. In SIF, agents are entities equipped with effectors and sensors in order to emit actions to and receive percepts from the world server, the medium representing the environment. Examples of effectors of an agent are communication, motion, use of a robotic arm, etc. Examples of sensors are virtual vision and communication. The world server defines the ‘world representation’, a data structure which carries information about position, appearance, and capabilities of objects in the environment, the specification of the environment itself and the services needed or connected to these objects. It also organizes the information flow during the simulation. Furthermore, the world server starts and stops the simulation and provides debugging and data collection facilities. The Graphical User Interface (GUI) is linked to the core of SIF just like a regular agent, i.e. it communicates with the core via sensors and effectors. The GUI offers a control pad, which is capable of forcing agents to perform certain actions. It also provided information windows for easy access to internal data. Agents sent messages to the world server, which, in turn, sent them to other agents (possibly the CMC). In the simulation, messaging was realized via Java method calls, but could also easily be realized via RMI or TCP/IP. We used an abstract data structure to represent, insert, or alter the agents’ preferences.

![](/api/attachments/QSGWYFRC/fulltext/images/985a27af8dd6d0cb1e0770adfa0993099aef7c3ef1495b578fe55d6d8c7133e2.jpg)  
Fig. 4. SIF framework.

## 3.2. Implementation of the algorithms

It was not our purpose to actually install an automated trading system, but to simulate OptiMark’s original algorithm and two of its simple variations. We have implemented two modes of the simulation system: one for on-line simulation and one for off-line simulation of the trading process with a pre-defined input stream of trading offers.

## 3.2.1. General properties

We implemented the Central Matching Controllers (CMC) and the traders as SIF agents that communicated via the world server. All agents had sensors and effectors at their disposal. For both scenarios (on-line and off-line) buyer and seller agents were equipped with the following effectors and sensors:

 Logging and unlogging effectors

 Satisfaction transmission effectors

 Information sensor

Trader agents could login to different CMCs simultaneously, if the traders wished to trade on different stocks at the same time. The system was able to cope with the use of multiple CMC agents. Agents of that type had similar sensors and effectors at their disposal.

The implementation of the OptiMark variations differed only in the specification of the satisfaction profiles and the use of the tiebreaker rules. Trader agents did not have to be modified, since their satisfaction profiles could be inserted conveniently in a script to be read during the start-up. The CMC agents used different tie-breaking rules for the methods. CMC agents stored all mutual matches of trading agents currently participating in a trading process in a priority queue ordered according to the mutual satisfaction value.

## 3.2.2. Registering, unregistering in the simulations

In the on-line simulation mode, trader agents could enter or exit a matching cycle at any time. In contrast to the original OptiMark system, our simulations were run on a regular computer and not a super computer. Hence we extended the original OptiMark cycle duration of 90 s. In SIF, it is the task of the world server to control the trading cycles. The world server also allows the simulation of disturbances in communication, such as a breakdown of an Internet server.

In order to have controlled conditions in our simulation tests, we did not allow agents to dynamically register to or unregister from the CMCs. Prior to a simulation run, a fixed number of buyer and seller agents with pre-specified satisfaction profiles were chosen which registered immediately and which were not supposed to unregister during a simulation. For our purposes, there was no need to run several CMC agents simultaneously since the result of further trading would be identical. We simulated only one trading cycle, which was comparable to 90 s in the original OptiMark algorithm.

## 4. The simulations

In our study, we used the following five measures to compare and contrast the algorithms.

1. Volume of stocks traded at each iteration.

2. Total satisfaction. We summed up the traders individual satisfaction values over the whole trading cycle in order to obtain an estimate of the total trader satisfaction.

3. Extent of price discrimination. We used the variance in price as the measure of price discrimina-tion. We argue that it is in the traders’ interest to have a market with relatively little price discrimination.

4. Efficiency. Efficiency of markets is measured as the percentage of the maximum possible gains from trade realized by the matching process, which is the standard welfare measure of efficiency. We illustrate with an example. Assume that the highest total satisfaction between two buyers (b1 and b2) and two sellers (s1 and s2) is: $0 . 9 5 + 0 . 9 0 + 0 . 8 5 + 0 . 8 0 = 3 . 5 0 ,$ based on a match between b1/s1 and b2/s2. Now, assume that in the simulation b1/s2 and b2/s1 are matched, resulting in the following satisfaction scores: $0 . 7 5 + 0 . 5 0 + 0 . 6 0 + 0 . 6 5 = 2 . 5 0 .$ Thus, the ‘‘efficiency’’ for this particular match is 2.50/3.50 or 71%.

5. Processing time. Processing time was measured in minutes. Since the computational effort to calculate the mutual satisfaction ranking is $O ( n ^ { 4 } )$ where n denotes the number of traders, the execution of the matching procedure can be very time consuming for large n.

![](/api/attachments/QSGWYFRC/fulltext/images/60e9644bf4f3f0d5a0ea432a7b19a74d4d012ebce341196a20745c3021c4ba25.jpg)

![](/api/attachments/QSGWYFRC/fulltext/images/59eab6b0ce41b503ac6b7bd214e32dcb94137075dd8dabb8472959e6789cb4f7.jpg)

In the simulations, buyer agents followed an underlying satisfaction profile (function) of $( 1 - p ^ { a } ) q ,$ , where $p$ stands for price normalized to (0,1); q represents quantity also normalized to (0,1); a denotes a random parameter (scaled to (0,1)) enabling different satisfaction profiles for the various buyer agents. Similarly, seller agents followed an underlying satisfaction profile (function) of $p ^ { a } q$ . In the original OptiMark approach, we have rounded the satisfaction values to (0, 0.1, 0.2, $\ldots , 0 . 9 , 1 )$ . In the 0–2 approach, we rounded all positive value pairs to $\cdot _ { 1 } \cdot$ and the best value pair to $\bullet _ { 2 } \cdot$ . In the 0–4 approach, we rounded value pairs in (0,0.5) to $\cdot _ { 1 } \cdot$ (the highest to ‘2’), and value pairs in (0.5,1) to $\cdot _ { 3 } \cdot $ (the highest to ‘4’).

Test runs with $5 \times 5 , 1 0 \times 1 0 , 2 0 \times 2 0$ , and $3 0 \times 3 0$ buyers and sellers were performed. In order to increase the validity of the results, we replicated each test run three times; varying only the parameter a. The average results for the three runs are reported in Fig. 5.

![](/api/attachments/QSGWYFRC/fulltext/images/cd4f529349f853b5a3b7dfa3c058e5b3042033f1da78a7f37109ef1c7fbcf212.jpg)

![](/api/attachments/QSGWYFRC/fulltext/images/b7b88eedad690240d15843e4ceea0a65d9e4cac9cd51dda478bb3fb666a8f32d.jpg)

![](/api/attachments/QSGWYFRC/fulltext/images/964baba053adb8949b96d23c591ed80f56489f3a27abefa396fdbf0443775b10.jpg)  
Fig. 5. Results figures.

## 4.1. Results

It was no surprise that, generally speaking, the original OptiMark performed best in the simulations, since the other two algorithms used cruder satisfaction profiles. In terms of quantity traded, total satisfaction, and processing time the differences among the algorithms were rather small. Differences in efficiency and price discrimination existed for small markets. However, the larger the market size, the smaller were the differences. The next logical question is that, given the results of the simulations, are the 0–2 and 0–4 schemes easier to use than the original 0–10 scheme? If this were true, we would recommend their use. This question is further investigated in the following section.

## 5. Ease of use of the various preference elicitation schemes

In the simulations reported in Section 4 there did not appear to be significant differences in the performance of the original OptiMark algorithm and two of its variations, particularly for larger markets. Our hypothesis, however, is that the 0–2 and 0–4 preference elicitation schemes are easier to use than the original 0–10 scheme. In order to test our hypothesis, we performed an experiment with 50 human subjects (24 MBA and 26 undergraduate students at NMSU, College of Business) with the sole purpose of finding out whether the 0–2 and 0–4 schemes would be easier to use than the 0 –10 scheme. Four out of the 50 responses were incomplete, leaving us 46 usable responses.

Our research hypotheses were:

$\mathbf { H _ { 0 } } \colon 0$ – 10 and 0 –2 schemes are equally easy to use ${ \bf H } _ { \mathbf { a } } \colon 0 { - } 2$ scheme is easier to use than the 0– 10 scheme and

$\mathbf { H _ { 0 } } \colon 0 - 1 0$ and 0 –4 schemes are equally easy to use

$\mathbf { H _ { a } } \colon 0 \cdot$ – 4 scheme is easier to use than the 0– 10 scheme

Our justification for the one-sided research hypotheses is based on the conjecture that it would be psychologically easier to provide preferences on a 0– 2 and 0 –4 scales than a 0– 10 scale, which requires fairly precise knowledge of one’s preferences.

In the experiment, half of the subjects were buying stock, half were selling. We reproduce the case description for the buying situation.

‘‘For over 80 years TIAA-CREF has been providing benefits for the education and non-profit research communities, earning a reputation for high-quality, low-cost financial products, as well as responsive service, disciplined investment management, and unrivalled professional integrity.

With more than \$290 billion in assets under management, TIAA-CREF, headquartered in New York City, is a leading financial services organization, a major institutional investor, and the world’s largest retirement system. TIAA is the Teachers Insurance and Annuity Association, one of only three U.S. firms to hold triple-A ratings from all four major independent analysts of the insurance industry. CREF is the College Retirement Equities Fund, an open-end, diversified management company registered with the federal Securities Exchange Commission.

The CREF Stock Account seeks favorable longterm returns through capital appreciation and current income. Because its primary purpose is to provide retirement benefits, the account avoids the extremes of conservatism and high risk. In general, we expect the account’s performance closely to follow that of the overall stock market. Over the long periods typical of pension-plan participation, the account’s gains have significantly outweighed setbacks, but past performance doesn’t guarantee comparable returns in the future. (Source: http://www.tiaa-cref.org).

You are the portfolio manager for TIAA-CREF’s Stock account. You are considering a possible trade in Hewlett Packard (financial info on following page—Appendix A). Because of HP’s buyout of Compaq computer, you need to rebalance your portfolio to reduce risk and by diversifying and purchasing more HP. Currently, the price of HP is \$50 on the open market. Because of your potentially large position in this company, you expect that there will be a ‘‘market impact’’ of this trade, meaning, if word leaks of the trade, the price will surely increase.

You are trying, however, to anonymously post your intention to trade by filling in the table(s) below with your preferences across 100 cells of price/quantity combinations (see Appendix B). If a match is found on the other side, a trade will result. You currently own 10,000,000 shares and you would be willing to purchase 10,000,000 for the right price. For a higher price you would be willing to buy fewer shares.’’

Each of the subjects used all three elicitation schemes, but the order was systematically (randomly) changed. At the end of each session the subjects were asked to fill-in a short questionnaire, focusing on the ease of use of the three schemes (see Appendix C).

## 5.1. Results: comparing 0– 10 and 0 – 2 schemes

## Question 1:

The p-value for the one-tailed test was 0.042 (Wilcoxon Signed Ranks Test: Z = - 1.727), supporting at 5% level of significance our claim that the 0– 2 scheme is easier to use than the 0–10 scheme. The average and median scores for the 0–2 scheme were 1.67 and 1.0 and for the 0–10 scheme 2.06 and 2.0, respectively (smaller value implying easier use).

## Questions 2 and 3:

The average and median scores for the 0 – 2 scheme were 3.45 and 4.0 and for the 0–10 scheme 3.02 and 3.0, respectively (larger value implying easier use). The Wilcoxon test p-value for a onesided test was 0.072 (not significant at 5% level).

## Question 5:

The average and median scores for the 0–2 scheme were 68.5 and 80.0 and for the 0–10 scheme 63.5 and 70.0, respectively (larger value implying easier use).

The overall conclusion is that the data provides support for rejecting the null hypothesis in favor of the alternative hypothesis that the 0 –2 scheme is easier to use than the 0– 10 scheme.

## 5.2. Results: comparing 0– 10 and 0 – 4 schemes

## Question 1:

The p-value for the one-tailed test was 0.82 (Wilcoxon Signed Ranks Test: Z = - 0.923), not supporting our claim that the 0– 4 scheme is easier to use than the 0 –10 scheme. The average and median scores for the 0–4 scheme were 2.22 and 2.0 and for the 0– 10 scheme 2.06 and 2.0, respectively (smaller value implying easier use).

## Questions 2 and 4:

The average and median scores for the 0 – 4 scheme were 2.88 and 3.0 and for the 0–10 scheme 3.02 and 3.0, respectively (larger value implying easier use). The Wilcoxon test p-value for a onesided test was 0.78 (not significant at 5% level).

## Question 5:

The average and median scores for the 0–4 scheme were 52.5 and 50.0 and for the 0–10 scheme 63.5 and 70.0, respectively (larger value implying easier use).

The tests provide no support for the alternative hypothesis. Hence we cannot reject the null hypothesis.

## 6. Conclusion

We have discussed the original OptiMark algorithm for finding optimal matches between institutional buyers and sellers of stock. In a recent publication, we have proposed two simple variations to the original OptiMark algorithm and have in this paper compared and contrasted them against the original OptiMark algorithm according to a variety of performance measures in a series of simulation runs. We have shown that, particularly when the size of the market increases, our simple variations perform equally well. Yet the crude 0–2 preference elicitation scheme appears easier to use. We hope that our findings will help solve some recent problems that OptiMark’s system has faced concerning the difficulty of use, as discussed in footnote 1. We also hope that our findings can be more generally used when developing matching algorithms based on user preferences.

## Acknowledgements

We would like to thank Dr. J.T. Rickard from OptiMark for fruitful discussions concerning the OptiMark system and two anonymous reviewers for useful comments. Mr. Tim vor der Brueck contributed to the implementation of the simulation. Mr. Michael Schillo assisted in the integration of the simulation

into the SIF system. This research has been funded, in part, by Siemens AG Germany (first author); Wihuri Foundation and the Foundation for Economic Education (third and fourth authors); the Academy of Finland and the Foundation of the Helsinki School of Economics (fourth author).

## Appendix A. Financial data of HP

<table><tr><td colspan="2">Per-Share Data</td><td colspan="2">Fiscal Year</td></tr><tr><td>Book Value (mrq*)</td><td>$7.27</td><td>Fiscal Year Ends</td><td>Oct 31</td></tr><tr><td>Earnings (ttm)</td><td>$0.69</td><td>Most recent quarter (fully updated)</td><td>30-Apr-2001</td></tr><tr><td>Earnings (mrq)</td><td>$0.05</td><td>Most recent quarter (flash earnings)</td><td>31-July-2001</td></tr><tr><td>Sales (ttm)</td><td>$23.22</td><td></td><td></td></tr><tr><td>Cash (mrq*)</td><td>$2.15</td><td colspan="2">Management Effectiveness</td></tr><tr><td colspan="2">Valuation Ratios</td><td>Return on Assets (ttm)</td><td>4.15%</td></tr><tr><td>Price/Book (mrq*)</td><td>2.49</td><td>Return on Equity (ttm)</td><td>9.71%</td></tr><tr><td>Price/Earnings (ttm)</td><td>26.24</td><td colspan="2">Financial Strength</td></tr><tr><td>Price/Sales (ttm)</td><td>0.78</td><td>Current Ratio (mrq*)</td><td>1.45</td></tr><tr><td colspan="2">Income Statements</td><td>Debt/Equity (mrq*)</td><td>0.43</td></tr><tr><td>Sales (ttm)</td><td>$47.0 B</td><td>Total Cash (mrq)</td><td>$3.24 B</td></tr><tr><td>EBITDA (ttm*)</td><td>$4.33 B</td><td colspan="2">Short Interest as of 8-Aug-2001</td></tr><tr><td rowspan="2">Income available to common (ttm)</td><td rowspan="2">$1.39 B</td><td>Shares Short</td><td>22.8 M</td></tr><tr><td>Percent of Float</td><td>1.4%</td></tr><tr><td colspan="2">Profitability</td><td>Shares Short (prior month)</td><td>17.4 M</td></tr><tr><td>Profit Margin (ttm)</td><td>2.9%</td><td>Short Ratio</td><td>3.97</td></tr><tr><td>Operating Margin (ttm)</td><td>6.2%</td><td>Daily Volume</td><td>5.74 M</td></tr></table>

See Profile Help for a description of each item above; K = thousands; M = millions; B = billions; mrq = most-recent quarter; ttm = trailing twelve months; (as of 31-July-2001, except mrq\*/ttm\* items as of 30-Apr-2001).

Appendix B. Preference elicitation task  
![](/api/attachments/QSGWYFRC/fulltext/images/e0c1e6a9e8c6e277499ace000473d28eb22de61fa385931edf3527a16240b2b2.jpg)  
Number of Shares 1000's

Instructions: 0–10 scheme

Under this system, a zero (or a blank cell) indicates you are not willing to trade at that price and quantity. The values from 1 –10 express your willingness to trade. 10 indicates that you are most willing to trade at that level. A 10 is better than a 9, a 9 better than an 8, and so on down the line. Insert the numbers in the cells, which express your preference.

## Instructions: 0– 2 scheme

Under this system, a zero (or a blank cell) indicates you are not willing to trade at that price and quantity. Mark only one cell with a 2 to indicate your most preferred cell. Mark the cells with a one if you are willing to trade at that price and quantity.

Instructions: 0 –4 scheme

Under this system, a zero (or a blank cell) indicates you are not willing to trade at that price and quantity. One cell contains a 4 to indicate your most preferred trade. Insert cells with a 3 if you are very willing to trade at that price and quantity. Insert cells with a 1 if you are willing to trade, but less willing than those cells marked with a 3. The one cell that is the best of those marked with a 1, change to a two. Therefore, the one cell marked 4 is the best of the 3s, and the one cell marked with a 2 is the best of the 1s.

## Appendix C. Questionnaire

1. In terms of Ease of Use, I would rank the three systems: 1= Easiest; 3 = hardest

0-10 system 0-2 system 0-4 system

2. In terms of Ease of Use, I would rate the 0-10 system to be: (mark with an x)

Very difficult difficult neither easy very easy

3. In terms of Ease of Use, I would rate the 0-2 system to be: (mark with an x)

Very difficult difficult neither easy very easy

4. In terms of Ease of Use, I would rate the 0-4 system to be: (mark with an x)

Very difficult difficult neither easy very easy

5. On a scale of 0-100, where 0 is very difficult and 100 is very easy, how would you rate the three systems on Ease of Use?

## References

[1] E. Clemons, B. Weber, Restructuring institutional block trading: an overview of the OptiMark system, Journal of Management Information Systems 15 (2) (1998, Fall).

[2] P. Funk, C. Gerber, J. Lind, M. Schillo, SIF: an agent-based simulation toolbox using the EMS paradigm, Proceedings of the Third International Congress of the Federation of EURO pean SIMulation Societies (EuroSim), 1998.

[3] W.A. Lupien, T.J. Rickard, Crossing Network Utilizing Optimal Mutual Satisfaction Density Profile, United States Patent #5689652 (1997).

[4] H. Raiffa, The Art and Science of Negotiation, Harvard Univ. Press, Cambridge, MA, 1982.

[5] J.T. Rickard, N.G. Torre, Information systems for optimal trans-

action implementation, Journal of Management Information Systems 16 (2) (1999, Fall) 47 – 62.

[6] S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, Prentice Hall, New Jersey, 1995.

[7] J. Teich, H. Wallenius, J. Wallenius, Multiple issue auction and market algorithms for the World Wide Web, Decision Support Systems 26 (1) (1999) 49 – 66.

Dr. Christian Gerber is an expert in agent and Web-technology. He has worked for IBM for the past 2.5 years. He is now an IBMcertified IT consultant in the field of e-business. He was formerly a researcher at the German Research Center for Artificial Intelligence (DFKI), Saarbru¨cken, Germany. Dr. Gerber’s research interests focus on Multi-Agent Systems, in particular the scalability of such systems. In addition, Dr. Gerber has worked as a Fulbright scholar at Rutgers University, NJ.

Dr. Jeffrey Teich, an Associate Professor at the New Mexico State University, is currently faculty at the Rotterdam School of Management, Erasmus University in the Netherlands. His research interests and publications are in the areas of negotiation modeling, decision support, and electronic auctions and markets. In addition, he has served as a Visiting Professor at the Helsinki School of Economics teaching in its international programs.

![](/api/attachments/QSGWYFRC/fulltext/images/bc7dd66f04c1b0058865768cb31ec4670a1b17791b1d34e7bc4dcb95653359a9.jpg)

Dr. Hannele Wallenius is Professor of Industrial Economics at the Helsinki University of Technology. Her research interests and publications are in the areas of electronic auctions and markets, negotiation modeling, multiple criteria decision making, and public sector operations research. Dr. Wallenius has also served as a Visiting Professor at the Helsinki School of Economics teaching in its international programs.

Dr. Jyrki Wallenius is Professor of Management Science and Director of the International Center at the Helsinki School of Economics. Dr. Wallenius’ academic interests and published research lie in the areas of multiple criteria decision making, negotiation modeling, and electronic auctions and markets. He is Editor of the European Journal of Operational Research and serves on the editorial boards of numerous journals. Recipient of the Pareto-Edgeworth award from the International Society of Multiple Criteria Decision Making.
