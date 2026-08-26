---
otero_id: 8010
otero_key: "MVSKDDDM"
title: "A method for classifying offer strategies observed in an electricity market"
authors: "HyungSeon Oh; Robert J. Thomas; Bernard C. Leiseutre; Timothy D. Mount"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A method for classifying offer strategies observed in an electricity market

HyungSeon Oh<sup>a,\*</sup>, Robert J. Thomas<sup>a</sup>, Bernard C. Leiseutre<sup>b</sup>, Timothy D. Mount<sup>c</sup>

<sup>a</sup>School of Electrical and Computer Engineering, Cornell University, Ithaca, NY 14853, United States <sup>b</sup>Energy Analysis, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States <sup>c</sup>Applied Economics and Management, Cornell University, Ithaca, NY 14853, United States

Available online 20 July 2004

## Abstract

The idea that large-scale generating units will operate at marginal cost when given the ability to offer their power for sale in a uniform price auction is at best wishful thinking. In fact, both real and experimental data show that the more uncertainty a supplier faces (e.g., load uncertainty, uncertainty of other suppliers, etc.), the more they will hedge their profits through higher than marginal cost offers and through withholding units if permitted. This makes predicting unit commitment and dispatch ahead of time difficult. This paper explores characteristics of software agents that were designed based on the outcome of human subject experiments on a uniform price auction with stochastic load. The agent behavior is compared to the behavior of the subjects. Both subject and agent behavior is classified based on the data. Differences and similarities are noted and explained. Based on the result of the simulation, a model was suggested to explain an offer submitted in deregulated markets based on double layer diffusion. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Standardized agent; Marginal cost offer agent; Speculator; Fair share; Diffusion model

## 1. Introduction

Restructuring of the electric power industry has been going on in many countries over the past 10 or so years. In all restructured markets, auctions play a major role in determining the price for electricity. Auction-based markets are thought to be more effective and in the long run, more efficient than traditional regulation. As a result of the new mechanisms where generation set points are determined by market forces rather than by engineering design, new tools are needed both for planning the new system and for operating it. Our aim in this paper is to discuss the agent-based components needed to develop a new tool for power system planning. Specifically, we wish to develop a planning tool that uses the results of a market-based simulation using software agents as a replacement for the human agents used in the real world to offer energy into a market. Well-designed software agents can be used to emulate the offer behavior of human agents provided that it can be shown that, in some sense, their behaviors are roughly identical.

Our experiments with trained humans have shown that humans adopt one of a small number of offer strategies for any given market design. So, a simulation should require only a limited number of different software agents. We seek to identify the combination of strategies that could cause anomalous operating conditions for a power network. Each of the agents represents a firm that owns several generators. Since it takes too much time to test all the possible permutations of all the software agents, we seek a way to identify only those combinations that will produce interesting results. That is, if there is a way to classify agents into small number of groups, not based on the code but based on the effects the agents have on the market and on the network, significant computational and design time will be saved.

All well-functioning agents, whether human or software, are driven to maximize their individual profits. Of the several different types of strategies used by human agents in a uniform price auction, the most prominent strategies are to either offer marginal cost or to use some degree of speculation, either by withholding capacity or by offering high prices or both. Individual earnings are determined by the market clearing price and quantity dispatched. A marginal cost offer agent tries to maximize quantity dispatched by offering low prices while free riding on the efforts of a speculator to raise prices. A speculator is interested in hedging his uncertainty and risk by raising the market-clearing price. While it is easy to model a marginal cost offer agent since it offers all its blocks at marginal cost, there are many different types of speculators depending on the degree that they speculate.

In this study, five standardized agents were designed for simulation and classification—four different types of speculators and a marginal cost offer agent. A human agent and a software agent competed against combinations of the standardized agents. They were classified into five different groups based on their performance as discussed in the sequel.

## 2. Electricity market

Agents develop auction rules for themselves based on the rules of the auction they are participating in and, in repeated auctions, based on the actions of their competitors. In the design considered here, the electricity market was assumed to be a uniform price auction with an inelastic but time varying load demand. In this market, an independent system operator (ISO) provides a load forecast and collects offers submitted by six participating agents. The ISO then clears the market and checks the security of the system.

In every period, each agent is asked to submit a price and quantity. No price can exceed a reservation price meant to represent the price above which no load would be willing to pay for power. The offers submitted by all the agents are then ranked according to the offer price from lowest to highest. Then, the ISO dispatched blocks beginning with the lowest offer until actual demand (which is different than forecasted demand) is met. If two or more blocks were offered at the same price, the ISO randomly selected which block(s) to be dispatched. All the winning agents were paid according to a second price auction, meaning that winners were paid at the same price (uniform price auction). If the actual demand were larger than the capacity offered, ISO would recall capacity from the blocks withheld at the price of the last accepted offer. The agent whose block was recalled would be charged a recall cost. After clearing the market, ISO published the market clearing price and quantity dispatched to corresponding agents. Each agent received information only related to its own generator such as the dispatch quantity and price. One scenario was comprised of 200 periods.

Six agents each had the same capacity with five blocks. Their generators had identical operating costs including fuel cost and standby cost as well as interest charges. For the sake of simplicity, startup costs were not taken into account. Based on its maximization algorithms, available history data and load forecast, each agent decided how many blocks to offer and the offer price of a block if offered.

Exchange of information among agents was not allowed.

## 3. Standardized agents

Five standardized agents consisting of one marginal cost offer agent and four speculators were designed and used in a test bed whose purpose is to a classify other software or human agents. That is, the thesis is that an agent with unknown behavior can be classified based on its play with known agent types. The marginal cost offer agent (MC) is an agent that offers all five blocks at marginal cost without any withholding. The four speculators had different degrees of speculation. In order to be a speculator, at least one block must be offered at a high price.

It is crucial to an ability to implement a speculator to be able to determine which block or blocks are to be offered at a high price. For simplicity, any offer submitted at a high price was made at the same price regardless of the type of speculation. A fair share of the market was calculated based on the load forecast. The block in which the fair share quantity falls is termed the <sup>b</sup>fair share block<sup>Q</sup>. If this were the last block chosen for the unit by the auction, then it would be the units’ marginal block. Thus, the fair share calculation is just a means for trying to predict a unit’s marginal block a period ahead and any calculation that accomplishes that prediction is suitable for the purpose we have in mind. Since all the competitors in the market considered here have the same capacity, fair share was calculated simply by dividing the load forecast by the number of market participants. If there were differences in the generating capacity being represented by an agent, the formula for a fair share is more complicated. In addition, if some agents have a locational benefit over others, their fair share should not be a simple dividend of a forecast. In this case, suppose all the agents that have the same locational benefit submit offers in order for them to get dispatched in the same fraction, which is the ratio of quantity dispatched to total capacity. The block containing the fair share was defined as the fair share block. For three speculators, only one block was offered at a high price, and the blocks with a lower operating cost than the fair share block were offered at marginal cost. The blocks with a higher operating cost than the fair share block were withheld from the market. There are several reasons why a speculator would withhold some of its capacity from the market. First, a speculator may suspect that the withheld block will not be dispatched if offered. In such a case, the speculator may avoid paying the standby cost which results in decreasing profit. Another reason is that physically withholding capacity increases the chance that a high offer will need to be dispatched since load must be met. If standby costs are ignored, the effect of withholding is essentially that of moving the supply curve to the left.

The strategies for offers of the standardized agents are shown in Table 1. The standardized agent with the weakest degree of speculation, called a weak speculator (WS), was designed to speculate with the block that is adjacent to and more expensive than its fair share block. If the load forecast had no significant error (i.e., if the forecast was similar to the actual demand), the behavior of WS was found to be similar to that of an MC with some withholding capacity. Since no speculator could speculate less than WS, the agent was called weak speculator. The agent with a stronger degree of speculation, termed strong speculator (SS), offered a high price for its fair share block. This agent took the risk not being dispatched for a higher market-clearing price. Two stronger speculators (SS2, SS3) were also implemented. One of them (SS2) offered at high price for the block before the fair share block while the other did from the first to the fair share block.

Offer strategies of the standardized agent when the fair share block is the jth block

<table><tr><td></td><td>Base unit</td><td>(j-1)th block</td><td>jth block</td><td>(j+1)th block</td><td>Higher block</td></tr><tr><td>MC</td><td>MCO</td><td>MCO</td><td>MCO</td><td>MCO</td><td>MCO</td></tr><tr><td>WS</td><td>MCO</td><td>MCO</td><td>MCO</td><td>S</td><td>W</td></tr><tr><td>SS</td><td>MCO</td><td>MCO</td><td>S</td><td>W</td><td>W</td></tr><tr><td>SS2</td><td>MCO</td><td>S</td><td>W</td><td>W</td><td>W</td></tr><tr><td>SS3</td><td>S</td><td>S</td><td>S</td><td>W</td><td>W</td></tr></table>

Here, MCO, S and W stand for the marginal cost offer, speculate and withhold, respectively.

## 4. Classification of an agent

In a simulation, five agents composed of some mix of the standardized agents and one agent of interest that was either a software design or a human agent were used. A specific combination of the five standardized agents comprised one scenario. It turned out that only six different scenarios were needed for a classification. Each software and human agent participated in the chosen six scenarios at a time. For each scenario, the six agents participated in 200 periods, and their earnings were collected and plotted as a function the earning of the agent of interest at each period. Fig. 1 shows one simplified plot of the earnings of all participating agents. The six lines show how the corresponding agents performed in each period. All the lines have different slopes, which characterizes the type of agent. Among the lines, the line showing y=x represents the earning of the agent of interest. If the y=x line is <sup>b</sup>close<sup>Q</sup> to one of lines showing the earnings of a standardized agent, the agent of interest is classified as an agent whose behavior is similar to that of the standardized agent that produced the close line. For example, the agent shown in Fig. 1 is classified as a strong speculator (SS). In the scenario that produced this plot, the MC (no speculating) agent earned the most while SS3 (the speculator with the strongest degree of speculation) earned the least. In simulations with software agents, this feature was found to be true in general. However, an agent with a less degree of speculation made the market more competitive and consequently made everyone including the agent itself earn less. This might encourage an agent to speculate if it wants to maximize its own profit without concern for the profits of others.

![](/api/attachments/MVSKDDDM/fulltext/images/ce60e64bcff732f17636b49cce2303ae6ec62cb990c17544d9b3443efd25ce15.jpg)  
Fig. 1. Earnings of the standardized agents and the agent of interest.

## 5. Expected earnings

It was assumed that the earning of a standardized agent was highly correlated to that of an actual agent of the same type. To calculate the earnings of six different types of agents, an electricity market was simulated only with the standardized agents. From the simulation, the earnings of participating agents were obtained in each scenario.

Expected earnings of the software agents were calculated based on the actual distribution of the software agents once they were classified. After classification, one could calculate the earning of each agent from each scenario, and then multiply the earning by a weight factor. The weight factor is calculated based on the probability that the agent might be in the same group in agent competition as the competition where it earned the profit considered now. For example, suppose that there were 24 agents. Suppose we had classified them as 5 speculators and 19 marginal cost offer agents. Now, suppose we were interested in one of the speculators competing with five other agents from the group of 24. The following enumerate the choices: Number of possible choices when selecting 5 agents without regard to type from the 23 agents left in the pool is: $_ { 2 3 } C _ { 5 } { \times } _ { 1 } C _ { 1 } { = } 2 3 ! /$ $( ( 2 3 - 5 ) ! 5 ! ) \times 1 ! / ( ( 1 - 1 ) ! 1 ! ) = 3 3 , 6 4 9$ . The number of choices that have no speculator in a group is 11,628 $( = _ { 4 } C _ { 0 } \times _ { 1 9 } C _ { 5 } \times _ { 1 } C _ { 1 } )$ . From similar calculations, the possible number of choices can be calculated for other mixes of agents. The corresponding probabilities can also be calculated. For example, the probability that the agent of interest participates in a market with no speculator is $0 . 3 4 5 6 ~ ( = 1 1 , 6 2 8 / 3 3 , 6 4 9 )$ . The probabilities that the market has one, two, three and four speculators are 0.4608, 0.1728, 0.0203 and $5 . 6 5 \times 1 0 ^ { - 4 } ,$ , respectively. That is, the probability that all marginal agents are competing with the chosen speculative agent (i.e., there are no speculators in the competition other than the chosen speculative agent) is 0.3456. If, for example, the agent of interest earns US\$100, US\$300, US\$700, US\$1800 and US\$2500 in each of five competitions where each has a different mix of competing agents as listed above, then the weighted earning of agent $k , E ^ { k }$ , is about

$$
E ^ {k} = \sum_ {i \in \text { possible   group }} p _ {i} ^ {k} \times e _ {i} ^ {k} \approx \text { US332 }
$$

where $p _ { i } ^ { k }$ and $e _ { i } ^ { k }$ stand for probability that agent $k$ is in group i and the earnings for agent k is in the group $i ,$ respectively. The expected earnings obtained in this way were used for a further comparison of the actual earnings.

## 6. Simulation results

In the fall 2002, 14 different software agents were submitted by the students taking the class ECE 551/ AEM655 at Cornell University. These agents were competed in a class competition and subsequently used as early tests of the classification ideas presented here. From experiments performed in the same class with the students, it was believed that MC, WS and SS were the most competitive types of agents. Therefore, only those types of standardized agents were used. After performing simulations in which all possible combinations of the three standardized agents were used, the classifications of each agent of interest by certain of those simulations were found to be redundant, i.e., classifications using one scenario and that by using another different one was identical. It was found that of the all the combinations of three agents choose five that are possible, only six were needed to produce distinctive classifications. The following scenarios were selected since they were found to be a complete set for the classification:

$$
4 \mathrm{WS} + 1 \mathrm{MC}, 3 \mathrm{WS} + 2 \mathrm{MC}, 4 \mathrm{SS}
$$

$$
+ 1 \mathrm{MC}, 3 \mathrm{SS} + 2 \mathrm{MC}, 1 \mathrm{SS} + 2 \mathrm{WS}
$$

$$
+ 2 \mathrm{MC} \text { and } 1 \mathrm{SS} + 1 \mathrm{WS} + 3 \mathrm{MC}.
$$

One randomly selected set of the forecasted and actual load was assigned for one scenario. Average load was 470 MW, and the maximum error between forecast and actual load was 20 MW.

Each of the 14 software agents and 5 standardized agents formed a group for the simulation, and corresponding plots were generated based on the results of the simulations. According to the plots, the 14 agents were classified into three groups—five MC, four WS and five SS. It seemed that most agents tested speculated to some extent with the degree of speculation somewhere between WS and SS. It is worthwhile noting that from a scenario the earnings of an agent was close to that of the standardized agent classified as the same type of the agent. Fig. 2 shows one example of the plots of the earning of a randomly selected software agent classified as SS. The classification of the software agents was fairly easy since the strategy used seemed consistent for a given scenario, which means no learning algorithms were implemented. For most of the agents, strategies seemed not to change for different scenarios, i.e., type of competitors. It was also found that no agents developed by the students used learning algorithms which would alter the results significantly.

For a simulation with a human agent, 20 students were recruited from the class ECE 451, electric power systems, at Cornell University. Each of the 20 students participated in the simulation with five standardized agents just like the software agents. The purpose of this experiment was to find out if the same technique that was successful for classifying software agents could be used to determine human strategies. The same sets of forecast and actual load were used for the simulation. They learned from experience, and were consistent only in some scenarios. Therefore, the data obtained only after a learning period were useful for classification of the scenarios. After examining earning data, 10 periods were assigned to the learning period. It was also found that one behaved SS in some scenarios while the same person did WS in other scenarios, i.e. different strategies were used for different types of competitors, which is logical behavior. Strategies other than ones used by the standardized agents were also observed. The conclusion was that the set of standardized agents was not rich enough and that it was possible to classify some of the different strategies by adding by the speculating agents SS2 and SS3 to the mix. A typical simulation result is shown in Fig. 3.

In the case of (a) and (b), one was classified as SS2 and SS3 while the same one was classified WS and SS in the case of (c) and (d), respectively. When SS3, a standardized agent with the strongest degree of speculation, participated in a scenario described above, plot (b) was a common feature. What SS3 did was effectively withhold its whole capacity from the market unless the market-clearing price was high. Therefore, the market-clearing price was high even in low-demand period, which caused the earnings of all competitors to increase considerably. Even though this type of strategy seemed not reasonable, it was often observed especially when the market was very competitive, i.e., for markets with an agent mix such as 3 WS+2 MC that is in aggregate not very speculative. In less competitive mixes such as 4 WS+1 MC or 3 SS+2 MC, the strategy was rarely used.

a) 4WS + 1 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/a167063fbc861c96316232a5e96ab4417cd098ea23a8a3a3c9f925295f35d5c0.jpg)

b) 3 WS + 2 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/b63ea8dbab80027e3885f9ca52d41a0917946f38e47817e5e602a93cc5ae5788.jpg)

c) 4 SS + 1 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/6c63ebb43fd34a2609caf0e9cc95f40cfb6ec96e2b2b5679ad742d71c953965d.jpg)

d) 3 SS + 2 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/258e21abeb79a658151eb6ebf50c953b6b2c3ad3597099f9b9d1fcf306867a5c.jpg)  
Fig. 2. Example of a performance of the software agents: in the plot, square and circle stand for the earning in a period of MC and speculator (WS or SS), respectively.

For the case in which it was possible to classify a human agent, the total earning of a human agent from the scenario was compared to that of the standardized agent of the same type from the same scenario. The comparison between the two earnings is shown in Fig. 4. The red line corresponds to a perfect correlation, which is y=x. In Section 5, it was assumed that standardized agent earnings were highly correlated to the earnings of actual agent of the same type. Fig. 4 shows the assumption was satisfied in the experiments performed in this study. The correlation between two earnings was checked for both a software agent and a human agent as long as it was possible to classify the agent of interest.

a) 4 WS + 1 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/640b95266469a35639b10e502fffc172fb9c492e04e37ca99a0359c6d50029ff.jpg)

b) 3 WS + 2 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/04105ca9c0462860fd87645de73b8c897bea8219760dc96688dbfc609b53decd.jpg)

c) 4 SS + 1 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/1a8cf149fc6f9494a772975c71f514527d170d9362b52d760e85cbfc3ffe5a12.jpg)

d) 3 SS + 2 MC  
![](/api/attachments/MVSKDDDM/fulltext/images/0d28e0c1001196f0d6a188f0b0b12a6adc3881b1acdf68e96e2761605e2bbf9c.jpg)  
Fig. 3. Example of a performance of the human agents: square and circle stand for the earning in a period of MC and speculator (WS or SS), respectively.

There was an interesting software agent worthy of special note. It offered some capacity into the market at marginal cost, but started to withhold some from the fair share block. Therefore, its offer function was similar to that of SS except for withholding capacity from the fair share block instead of offering at a high price. This offer behavior is known as a Cournot speculator [1,3]. This agent was classified as SS as long as at least one speculator exists in the market regardless of type such as WS or SS. For a further investigation, other types of agents were implemented. For example, an agent similar to WS that withheld its normally high offer block was tested. The agent was classified as WS by classification tests. It was concluded that the degree of speculation is closely related to which, block of capacity an agent chooses to deviate from the marginal cost (or low offer).

In an agent simulation, it was found that in general a higher earning for everyone was achieved, as the speculation got stronger. However, in a given scenario, the agent who earns most was the least speculating agent—MC, WS, SS, SS2 and SS3 in decreasing order. For the agent simulation, the objective of each agent was the profit maximization. The best strategy of an agent to serve the objective depended on the scenario in which the agent participated. Therefore, it is important to figure out the type of the competitors in the market.

![](/api/attachments/MVSKDDDM/fulltext/images/eee2fc698a8e8e5cab8f2bda72640da8028c6d67c00f35a216af44bbfb583a31.jpg)  
Fig. 4. Actual earning vs. Expected earnings calculated from simulation.

In the class ECE 551/AEM 655, a round robin type tournament was designed to determine a winner among submitted agents based on earnings. In the tournament, submitted agents were randomly divided into three groups of six agents. A group of six agents participated in a simulation. Based on earnings from the simulation, two agents from each group were selected for a final simulation. The winner was chosen from the final competition composed of two winning agents from each of three groups. The winner was classified by using the classification method, and turned out to be a type of MC. In such a competition, not many combinations were given to agent even though the group selection was random. Therefore, it is reasonable that the winner was an MC type when one considers that the least speculating agent (MC) in a given scenario is the most rewarding agent.

When all possible combinations were tried (complete search), the winner was a type of an SS. The method seems fair to all the agents, but it takes too much time because a large number of simulations are needed. For an alternative method, it was suggested that one should select only small number of agents, and then give all the combination for the selected agents. It is important how effectively and fairly one can select the small number of agents out of all the agents. Based on expected earnings, $E ^ { k }$ , obtained by using the method described in Section 5, one can rank all the agents by assuming that the actual earning of agent k has a good correspondence with the expected earning, $E ^ { k }$ . The rank is to be used for a selection of small number of agents. By using this method, 10 agents were selected for the final competition. Eight out of 10 selected agents were ranked in top 10 from complete search method. The winner determined by this method was also turned out to be the winner from the complete search.

## 7. Diffusion model

In this study, four different types of standardized agents were used for a simulation. Each type has a different degree of speculation defined by the block (quantity) at which the offer price deviates from marginal cost. It was observed that in most scenarios the most rewarding strategy is some degree of speculation such as SS or WS. However, in very competitive scenarios, the most rewarding one is marginal cost (MC). The same characteristics of the speculators and marginal cost offer agent have been found in all the deregulated markets we have looked at. Fig. 5 shows the most common types among the offer curves submitted in the Pennsylvania–New Jersey–Massachusetts (PJM) market during 1998 for example. In the figure, D8 and Y6 stand for the company codes named by the PJM ISO.

![](/api/attachments/MVSKDDDM/fulltext/images/5bdd425b426ccfca45c65861366da43bdd70b7f0f658870f2552e3d028a75035.jpg)  
Fig. 5. Two common offer curves in all the deregulated markets. These specific offer curves were found in the PJM market where D8 and Y6 stand for the company code.

It is difficult to determine the type of the agents D8 and Y6 since the load forecast data were not provided. If the fare share of D8 were less than 1500 MW and that of Y6 were larger than 6100 MW, D8 and Y6 would be classified as a marginal cost offer agent and a speculator, respectively. In the setup for the current software agents, they could decide only offer prices— not offer quantities. In real life, each generator was allowed to submit several blocks and each company owns many generators. There have been suggested two different ways to overcome this limitation. The one was implementing many blocks for each agent classified such that quasi-continuous offer could be submitted. It is easy to modify in such a way, but introducing many blocks may be computationally demanding. The other suggestion was to allow each agent to decide the quantity as well as the price of each block. In order to decide quantity and price consistently, a proper model is needed.

As shown in Fig. 5, there exist at least two different types of agents in a real market. There are two different blocks in the offer curve of Y6—the one shows low price offers with a plain increase, and the other does high price offers with a steep increase in offer price. In the offer curve of D8, only the first block showed up. To model the different types of agents consistently, the underlying different objects of two blocks were considered. The first block was submitted at a low price in order to be dispatched while the second was done for the purpose of raising the dispatched price. Due to these objects, the very beginning of the first block is exposed to the minimum offer price, and the end of the second is done to the maximum price that an agent might think of. In comparing two blocks, the second block is more sensitive to the change in the market condition determined by the competitiveness of the market. It is reasonable to assume that as the market condition changes the change in the offer price depends on the offer price gradient with respect to the offer quantity, Fick’s first law [2].

$$
j _ {p _ {1}} = D _ {1} \frac {\partial p _ {1}}{\partial q}
$$

$$
j _ {p _ {2}} = D _ {2} \frac {\partial p _ {2}}{\partial q}\tag{1}
$$

where j, $p , D$ and $q$ represent the offer price change with respect to the change in the market condition, offer price, diffusion coefficient and quantity, and subscript 1 and 2 stand for the 1st and the 2nd block, respectively.

In this model, limits such as a maximum generator capacity and reservation price are ignored. In other words, if there were no limitation (i.e., all the agents were allowed to submit any offer), there would be two blocks visible in an offer curve. Due to all the physical limits, each agent has a limited window to the whole offer curve. It cannot submit an offer price higher than a reservation price, and quantity larger than its maximum capacity. With the limited window, an agent decides where to locate the window to maximize its profit. Furthermore, it can also partially close the window by withholding its capacity. This locating and partially closing window is determined based on an optimization process of each agent.

This modeling can be described by solving Fick’s second law [2] (i.e., diffusion equation that is derived from Fick’s first law) with proper boundary conditions,

$$
\frac {\partial p _ {1}}{\partial y} = D _ {1} \frac {\partial^ {2} p _ {1}}{\partial q ^ {2}}
$$

$$
\frac {\partial p _ {2}}{\partial y} = D _ {2} \frac {\partial^ {2} p _ {2}}{\partial q ^ {2}}\tag{2}
$$

$$
p (q = q _ {\mathrm{min}}) = p _ {\mathrm{min}}
$$

$$
p (q = q _ {\max}) = p _ {\max}\tag{3}
$$

where $y$ represents the market condition. By solving the diffusion equation [4], one obtains an expression for offer price as a function of market condition, $y ,$ and quantity, $q ,$ , for the 1st block $( q { < } q _ { \mathrm { b } }$ where $q _ { \mathrm { b } }$ is the quantity at the boundary between two blocks)

$$
p _ {1} (y, q) = \frac {p _ {\max} - p _ {\min}}{1 + \sqrt {D _ {1} / D _ {2}}} \left[ e r f c \left(\frac {q _ {\mathrm{b}} - q}{2 \sqrt {D _ {1} y}}\right) - p _ {1} ^ {\mathrm{b}} \right]\tag{4}
$$

where

$$
\begin{array}{l} p _ {1} ^ {b} (y, q) = \exp \left[ h _ {1} (q _ {b} - q) + h _ {1} ^ {2} D _ {1} y \right] \\ \times e r f c \left(\frac {q _ {b} - q}{2 \sqrt {D _ {1} y}} + h _ {1} \sqrt {D _ {1} y}\right) \end{array}
$$

$$
h _ {1} = \frac {k}{D _ {1}} \left(1 + \sqrt {\frac {D _ {1}}{D _ {2}}}\right)\tag{5}
$$

![](/api/attachments/MVSKDDDM/fulltext/images/59387fe34e8d2dbc71230d2968ce1df73f20d7906ca18762272522389896cbd7.jpg)

![](/api/attachments/MVSKDDDM/fulltext/images/ff7f3d5b8d6892c39acde5f4a760cb85d70181a7e165322953eeeb77d9da5326.jpg)  
Fig. 6. Fitting results of two offer curves in a same day to Eq. (11). Two blocks are visible only in (b), but the same $p ^ { \mathrm { m a x } }$ was used for both fittings.

and for the 2nd block $( q { > } q _ { \mathrm { 6 } } )$

$$
\begin{array}{l} p _ {2} (y, q) = \frac {p _ {\max} - p _ {\min}}{1 + \sqrt {D _ {1} / D _ {2}}} \\ \times \left\{1 + \sqrt {\frac {D _ {2}}{D _ {1}}} \left[ e r f \left(\frac {q - q _ {\mathrm{b}}}{2 \sqrt {D _ {2} y}}\right) + p _ {2} ^ {\mathrm{b}} \right] \right\} \end{array}\tag{6}
$$

where

$$
\begin{array}{l} p _ {2} ^ {\mathrm{b}} (y, q) = \exp \left[ h _ {2} (q - q _ {\mathrm{b}}) + h _ {2} ^ {2} D _ {2} y \right] \\ \times e r f c \left(\frac {q - q _ {\mathrm{b}}}{2 \sqrt {D _ {2} y}} + h _ {2} \sqrt {D _ {2} y}\right) \end{array}
$$

$$
h _ {2} = \frac {k}{D _ {2}} \left(1 + \sqrt {\frac {D _ {2}}{D _ {1}}}\right)\tag{7}
$$

where the superscript b means boundary effect, which came from the different characteristics of the substances, and k stands for the boundary constant quantifying the boundary effect.

If a generator (or a firm) has only one decision maker submitting its offer, there should be no boundary effect, i.e., $k ^ {  } \infty$ . In such a case, both $p _ { 1 } ^ { \mathrm { b } }$ and $p _ { 2 } ^ { \mathrm { { \bar { b } } } }$ approach zero, and the expression for the offer price is

$$
p _ {1} (y, q) = \frac {p _ {\max} - p _ {\min}}{1 + \sqrt {D _ {1} / D _ {2}}} \left[ 1 - \operatorname{erf} \left(\frac {q _ {\mathrm{b}} - q}{2 \sqrt {D _ {1} y}}\right) \right]\tag{8}
$$

$$
p _ {2} (y, q) = \frac {p _ {\max} - p _ {\min}}{1 + \sqrt {D _ {1} / D _ {2}}} \left[ 1 + \sqrt {\frac {D _ {2}}{D _ {1}}} \operatorname{erf} \left(\frac {q - q _ {\mathrm{b}}}{2 \sqrt {D _ {2} y}}\right) \right]\tag{9}
$$

Furthermore, the maximum offer price might be considered shared information, which means that all of the participating agents have practically the same price for a given condition. With these assumptions, offer curves could be fitted to the following equation

$$
\begin{array}{c} p (y, q) = H (q _ {\mathrm{b}} - q) p _ {1} (y, q) \\ + H (q - q _ {\mathrm{b}}) p _ {2} (y, q) \end{array}\tag{10}
$$

where H stands for the Heavyside function;

$$
H (x) = \left\{ \begin{array}{l l} 0 & \text { if } x <   0 \\ 1 & \text { otherwise } \end{array} \right.\tag{11}
$$

The data shown in Fig. 5 were used to fit Eq. (11), and the results are shown in Fig. 6. The cutoff quantity, $q _ { \mathrm { c } } ,$ can be defined as an agent’s maximum offer quantity. The cutoff quantities for D8 and Y6 were about 1500 and 6200 MW, respectively. The $q _ { \mathrm { c } }$ of D8 was larger than the quantity at the boundary, q<sub>b</sub>, while that of Y6 was smaller than $q _ { \mathrm { c } } .$ In order to characterize the behavior of an agent, it is useful to define the deviation quantity

$$
q _ {\mathrm{d}} \equiv \min \left\{q _ {\mathrm{c}}, q _ {\mathrm{b}} \right\}\tag{12}
$$

Then, the distance from the fair share to the deviation quantity is a measure of the degree of speculation in accordance with the simulation result in this study. With this model, it is possible to submit a price, corresponding to a quantity. Five standardized agents were modified in accordance with this model in a following way;

(1) Degree of speculation, $q _ { \mathrm { d } } .$ —fair share, is set to +5, 5 and 15 MW for WS, SS and SS2, respectively—for MC and SS3, the quantity $( q _ { \mathrm { d } }$ —fair share) is not relevant,

(2) The relative distance from $q _ { \mathrm { c } }$ to $q _ { \mathrm { d } }$ equals to 0 and 8 MW for MC and speculators (WS, SS and SS2)—for SS3, the relative distance is not relevant,

(3) Other parameters such as maximum and minimum offer price, diffusion coefficients do not change with the type of the standardized agents.

With the modified standardized agents, the software agents submitted by the students taking the class ECE 551/655 were tested in the same simulation. The results of agent classification and expected earnings were identical to those with the original standardized agents.

## 8. Conclusions

In this paper, several simplifications have been made for the system for both a market and agent used here such as all equal marginal cost, equal capacity, no startup cost and no line constraints. From a market simulation with those simplifications, offer strategies under a uniform price auction are classified. Under the auction rule, the last accepted block determines the market-clearing price, second price auction. The earning is approximately determined by the quantity dispatched as well as the market clearing price. To maximize earnings, a software and a human agent choose several different strategies. Each strategy produces a different offer function. The main results of this paper describe how to classify the strategy not by inspecting individual offer function but by comparing the result of simulation with its competitors. Different types of agent can be characterized by their degrees of speculation. The degree of speculation is closely related to where its offer function deviates from the low offer or marginal cost offer. The most rewarding strategy is to speculate in most cases while a marginal cost offer strategy is one that is preferred when speculators are present. A model for both marginal cost offers and speculation was developed based on a diffusion model. The diffusion model was fit with real data from the PJM market. This paper also shows that only a small number of standardized agents need be used for the classification, and their earnings have a good correspondence with the earning of an actual agent.

## Acknowledgements

This project was supported in part by the US Department of Energy through the Consortium for Electric Reliability Technology Solutions (CERTS) and in part by the National Science Foundation Power Systems Engineering Research Center (PSERC). The authors would like to thank Dr. Oh and Peter Wong for the actual offer curves in the PJM market and valuable help on the computer simulation for this work, respectively. They also thank all the students from ECE 551/AEM 655 and ECE 451 for participating the experiments.

## References

[1] A. Cournot, Researches Into the Mathematical Principles of the Theory of Wealth, Macmillan, New York, 1897.

[2] J. Crank, The Mathematics of Diffusion, Oxford University Press, London, 1957.

[3] A. Daughety, Cournot Oligopoly, Characterization and Applications, Cambridge University Press, New York, 1988.

[4] L. Tian, M. Thompson, R. Dieckmann, C.Y. Hui, Y.Y. Lin, Bulk diffusion measurements to study the effectiveness of barrier layers: I. Mathematical treatment, Journal of Applied Physics 90 (8) (2001) 3799–3809.

![](/api/attachments/MVSKDDDM/fulltext/images/bf2493f37062d0bab7d7a6377eca5677228efffe7630dbe505248a8c1872eb13.jpg)  
HyungSeon Oh received his MS degree in Materials Science and Engineering in 2002, and he is currently enrolled in the PhD program in Electrical and Computer Engineering at the Cornell University. His research interest includes electricity trading, computer modeling and simulation.

![](/api/attachments/MVSKDDDM/fulltext/images/2311f652a9317d030f28ff560ba9c8bcb84c1c1281e9a1c5d6032fd1f6085d10.jpg)  
Robert J. Thomas is a Professor in Electrical and Computer Engineering at the Cornell University. His current research interests are broadly in the areas of analysis and control of nonlinear continuous and discrete-time systems with applications to large-scale electric-utility systems.

![](/api/attachments/MVSKDDDM/fulltext/images/154fa318697c6714815cbd989b9e3b6a4c94ddff33383f93436331afb0f6fffc.jpg)  
Timothy D. Mount is a Professor in Applied Economics and Management at the Cornell University. His research interests include econometric modeling and policy analysis relating to the use of fuels and electricity, and to their environmental consequences (acid rain, smog, and global warming). He is currently conducting research on the restructuring of markets for electricity and the implications for (1) price behavior in auctions for electricity, (2)  
the rates charged to customers, and (3) the environment.

![](/api/attachments/MVSKDDDM/fulltext/images/ce28ce7acd08ace5011e296ea6f161f7522ff8aa01b0dbee39e08ff7447fb411.jpg)

Bernard C. Leiseutre is a staff scientist at the Lawrence Berkeley National Laboratory. He received his BS, MS, and PhD degrees in Electrical Engineering from the University of Illinois in 1986, 1988, and 1993 respectively. From 1993 to 2001, he served as an Assistant Professor and then Associate Professor of Electrical Engineering at MIT. He has held visiting associate professor positions at Caltech and Cornell University. His research interests include

all aspects of the electric power, simulation techniques, and nonlinear dynamics.
