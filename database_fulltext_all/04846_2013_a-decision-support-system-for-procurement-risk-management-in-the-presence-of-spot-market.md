---
otero_id: 4846
otero_key: "ATHV4SRR"
title: "A decision support system for procurement risk management in the presence of spot market"
authors: "Zhen Hong; CKM Lee"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.031"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for procurement risk management in the presence of spot market

Zhen Hong <sup>a</sup>, CKM Lee <sup>b,</sup>⁎

<sup>a</sup> Division of Systems Engineering Management, School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore <sup>b</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, The Hong Kong Polytechnic University, Hong Kong

a r t i c l e i n f o

Article history: Received 3 May 2012 Received in revised form 12 December 2012 Accepted 27 December 2012 Available online 9 January 2013

Keywords: Procurement risk management Spot market Supplier selection Order allocation Monte Carlo simulation Goal programming

## a b s t r a c t

In the presence of spot market, this paper presents a decision support system to model risks for procurement processes and to design a robust purchasing plan, including supplier selection and order allocation. Taking advantages of contract supplier and spot market, the buyer can better meet business requirements in this dynamic business environment. However, there are limitations of existing methods for modeling multiple correlated risks to support decision makers for allocating orders among multiple suppliers in the presence of spot market. Therefore, Monte Carlo simulation algorithm termed as Expected Pro<sup>fi</sup>t–Supply at Risk (A-EPSaR) is proposed to quantify each supplier's risk so as to let decision maker realize the trade-off between pro<sup>fi</sup>t and risk. The goal programming model helps to allocate orders among the supplier pool and the contract-spot allocation model can assign orders between the spot market and the supplier pool, respectively. The signi<sup>fi</sup>cance of this paper is to propose a novel decision support framework which helps the buyer to make optimal and robust procurement decision including supplier selection and order allocation among multiple supplier sources in the existence of correlated demand, yield and spot price uncertainties. A case study is used to illustrate the performance of the proposed framework and the proposed methods show the promising result.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Procurement risk management is of great importance and is crucial to the success of supply management [25,34]. With the popularity of outsourcing from 1980s, many companies outsource the business which is not their core competency [15]. For example, Dell outsources the manufacturing of computer components to other companies and focuses on assembling each ordered unit according to a selection of custom options. Outsourcing becomes a business strategy for Dell and other business partners, so enterprises can focus on its core technology and enhance their competency. But this brings a great challenge for procurement. Indeed, procurement is becoming more and more demanding in this dynamic market environment in terms of supplier risk management [20,22,24]. Nowadays the majority of raw materials and components are manufactured in countries where costs are lower. Many of the business partners and component producers are overseas and dif<sup>fi</sup>cult to be monitored. Therefore, supply from these contract suppliers is hard to be controlled and has different extents of uncertainty. In fact, there are many uncertainties that existed in procurement [5,11,19], such as variable lead time and uncertain demand. Since the lead times of these contracts are usually quite long, the buyer doesn't have enough time to place a second order when the uncertain demand or uncertain yield is realized. Or when the supply is affected by nature disasters, part or all of suppliers' production capability is halted. More and more companies have already realized the importance of managing procurement risk. For example, HP has formed a Procurement Risk Management (PRM) team and enabled \$100 million dollars in accumulative savings over the past 5 years according to [25].

The incorporation of a reactive supply channel in procurement is advocated by many scholars. These reactive supply channels can be spot market [29], option contracts [30] or a back up supplier [31]. Utilizing the short lead time advantage of spot market, Seifert et al. [29] <sup>fi</sup>gure out the optimal order allocation among the single contract supplier and the spot market under demand uncertainty. Haksöz and Kadam [13] provide a tool to assess the effects of contract breaches in the presence of demand and spot price risks. A new term Supply at Risk (SaR), which returns the worst loss that will not be exceeded with a given level of con<sup>fi</sup>dence, is introduced by Haksöz and Kadam [13] to evaluate supply risk. Indeed, SaR is a similar concept akin to the Value at Risk (VaR) statistic in <sup>fi</sup>nance [18]. A portfolio of contracts are evaluated and SaR is obtained to <sup>fi</sup>nd out the optimal supplier portfolio according to [13].

As the shortcomings from contract supplier can be made up and compensated by the reactive supply, therefore, to deal with the procurement risk management, it is essential to utilize both supply sources and take related risk factors into consideration. At the beginning of every procurement period, the buyer will place orders on the supplier pool of long term contract suppliers. Because of the uncertain yield from these contract suppliers and unstable demand, spot market with negligible lead time is adopted as the reactive supply source to meet unexpected demand or sell extra stock. The price from spot market changes continuously and is higher compared with the long term contract suppliers. Indeed, these uncertain factors are not independent and can affect one another. In this paper, the most general case of a completely correlated demand, spot price and uncertain supply is considered. The risk attitude of a buyer is also taken into consideration as it affects the procurement decision. In addition, the following factors are also studied: procurement cost, minimal order and maximal order proportion assigned to a single supplier and <sup>fi</sup>xed cost of adding one more supplier. In order to assist decision making in formulating the management plan, a novel PRM framework is proposed. The proposed framework helps to generate a procurement plan which includes 1) the selection of appropriate suppliers; 2) the order allocation for the respective supplier; 3) the aggregate order to be purchased from the selected supplier pool; and 4) the total order amount purchased from spot market.

This paper is organized as follows: Section 2 describes the related research work and the gaps in these areas. Section 3 presents the integrated framework from supply risk identi<sup>fi</sup>cation to risk monitoring. Section 4 illustrates the framework with a case study. In Section 5, conclusions are drawn and future research directions are stated.

## 2. Literature review

Supply and procurement risk management are part of the supply chain risk management [33]. Haksöz et al. [11] mentioned that the top three risks in procurement are demand, price and breach of contract risks. The aim of risk management in supply chain is to identify the potential risks and implement the risk management technique to reduce the impact and probability of occurrence of risks in supply chain. In fact, the utilization of a pool of suppliers to diversify risks is quite common and effective in the industry especially when the suppliers are not reliable [1]. Spot market is also adopted as a reactive supply source as it has the advantage of short lead time, i.e., the extra demand can be met by spot market within a negligible time [29]. In addition, the prediction market is an effective approach to manage demand uncertainty [10].

In the area of utilizing multiple suppliers under yield uncertainty, Agrawal and Nahmias [1] derived the optimal number of suppliers and the corresponding lot sizes. They have studied both the following two cases: identical suppliers and non-identical suppliers. They discover that the expected pro<sup>fi</sup>t is strictly concave with the order quantity and the number of suppliers. Another observation is that the ratio of optimal order size is inversely proportional to the yield variance. If suppliers want to increase their shares of the total order, they have to improve their yield performances. Federgruen and Yang [6] proposed a model to con<sup>fi</sup>gure the supply base in the presence of yield and demand uncertainties under a single period setting. The generated optimal procurement plan includes the optimal set of suppliers to be chosen and the optimal orders to be assigned to each supplier. If there is no reactive supply after the uncertain demand or yield is realized, the unmet demand is usually penalized at a certain value; and the extra products are also salvaged.

The other alternative to solve the procurement problem is to adopt spot market as a reactive supply channel. In fact, spot market is studied by many economists for pricing and hedging of commodities [3,28,32]. But there are still a lot of researches that can be done such as investigating the effect of spot market on supply chain and the trade-offs between the spot market and contract suppliers [24]. Haksöz and Seshadri [12] have done a comprehensive literature review regarding the study of spot market in supply chain operations. It is mentioned that these works can be divided into two categories: optimal procurement strategy and the valuation of procurement contracts. Under the assumption of demand uncertainty, Seifert et al. [29] quantify the bene<sup>fi</sup>ts of using spot market from a buyer's perspective. They develop and solve mathematical models that determine the optimal amount of orders to be purchased via forward contract and spot market, respectively. Also under the assumption of uncertain demand, Chen and Liu [4] quantify the bene<sup>fi</sup>ts of using spot market from both the buyer's and the supplier's perspective. The optimal order size is obtained under uniformly distributed demand and spot price. Apart from the spot market, procurement using option contract can also be a reactive supply channel. It gives buyers the right, but not the obligation to purchase at the exercise price from the seller within a pre-speci<sup>fi</sup>ed time period. In order to gain the option right, buyers have to pay an option price to reserve the capacity. If buyers don't want to execute the contract, the payment would not be refunded. This kind of contract ensures a buyer's <sup>fl</sup>exibility to respond to the actual demand. At the same time, it also provides a certain amount of compensation for the supplier in the form of option price. Fu et al. [7] derive the optimal number of option contracts and the corresponding lot sizes from option contracts and spot market under uncertain demand. The results show that the adoption of both option contracts and spot market can help control the supply risk.

In addtion, adoption of prediction market is proved to be quite effective in supply chain risk management by providing an accurate demand forecast and promoting channel coordination. Guo et al. [10] designs macro prediction market analoygy to a real money fu tures market where a retail index with a payoff depends on the future realization of uncertain macroeconmic factor. By the adoption of this prediction market appraoch, useful informaiton is shared and market participants are motivated to produce a reliable forecast. Therefore, the incorporation of prediction market approach into supply chain management helps to achieve accurate demand forecast sharing; reduce the order variance and improve the expected supply chain pro<sup>fi</sup>t. With the popularity of social netowrk (e.g. Twitter), the simulation result of a Twitter-based prediction market shows that the price dispersion is small as agents acquire more information in the network. Network based prediction market has a better prediction and the <sup>fi</sup>nding gives insight about how social network affects information acquired by agents so as to affect the overall market performance [27]. The similarity between the spot market trading appraoch and the prediction market appraoch is that they can be both used for managing demand uncertainty. The difference is that the spot market trading approach tries to minimze risk impacts after risk events happen, while the prediction market appraoch can help to reduce the uncertainty of risk factor before risk events happen. In addtion, the spot market trading approach can also be used to manage uncertain yield which is hard to predict for individual suppliers.

Based on the literature review, the above researchers have already extensively studied both the effectiveness of supplier diversi<sup>fi</sup>cation to reduce supply volatility as well as applying spot market to manage demand uncertainty. However, limited research works have been carried out by adopting both reactive supply and multiple contract suppliers for yield uncertainty management. The incorporation of yield uncertainty into procurement decision making makes the supply more reliable and effective. Taking the advantages of both risk diversi<sup>fi</sup>cations from a supplier portfolio and spot market, this paper manages to solve the problem of order allocation among multiple suppliers in the presence of spot market. Uncertain demand, volatiles spot price and unreliable supply are considered in the problem formulation. Moreover, the risk attitude of the buyer is also incorporated in the proposed model. Generally, two broad areas are related to our research: supplier diversi<sup>fi</sup>cation under yield uncertainty and procurement in the presence of spot market.

In addition, there is a lack of method to quantify the multiple di mensional and correlated risks when selecting suppliers. Some paper suggests using Analytic Hierarchy Process (AHP) to model the multiple dimensions of supply risks [8,21]. But AHP fails to express the correlation among risks which actually exist in the industry. For

example, Kull and Talluri [21] assess the delivery, cost, quality and <sup>fl</sup>exibility risks using AHP. But the problem is that AHP is incapable of taking risk dependences into consideration. In addition, although there are numerous research works about developing the sourcing model under demand uncertainty, there is lack of research work about order allocation among supplier in the presence of spot market and demand, yield and spot price uncertainties. Without solving these gaps, it is dif<sup>fi</sup>cult to implement an effective and practical procurement risk management solution. Hence, our proposed framework uses a practical approach, simulation, to assess the multiple dimensions of risks and adopts a reactive supply source (spot market) to better manage yield uncertainty.

## 3. The proposed PRM framework

The proposed PRM framework provides a novel procurement risk management solution, which includes four stages: (1) supply risk identi<sup>fi</sup>cation; (2) supply risk assessment based on Monte Carlo simulation and Pro<sup>fi</sup>t–SaR map; (3) Supply risk mitigation with goal programming model; and (4) supply risk monitoring. Fig. 1 depicts the <sup>fl</sup>owchart of the PRM framework.

In the PRM framework, all potential suppliers are found out and the supply risks are identi<sup>fi</sup>ed, such as unpredictable demand, volatile pric and uncertain supply yield. Based on the identi<sup>fi</sup>ed risks and the cost components of the procurement, a pro<sup>fi</sup>t model is built to simulate the performance (expected pro<sup>fi</sup>t and SaR) of each of the potential suppliers. An algorithm is derived to calculate pro<sup>fi</sup>t and SaR of each supplier, and only quali<sup>fi</sup>ed suppliers from the supplier's pool are selected. The goal programming model helps to obtain the order proportions among the selected supplier pool by achieving the objectives and considering related constraints. After knowing the proportion of the order assigned to individual suppliers, the mean of supplier portfolio yield and average wholesale price can be computed. Then, according to the analytical result of the contract-spot allocation model in Hong et al. [16], the total amount of products purchased from both contract supplier and spot market are found out, respectively. Thus, the detail order allocation plan is formulated based on the total purchased amount and the order shares.

## 3.1. Supply risk identification

In stage one, the buyer tries to <sup>fi</sup>nd out all the potential suppliers from both local and overseas. These long term contract suppliers are for Proactive Procurement Risk Management (PPRM) and each supplier is different in terms of the price and supply uncertainty. Their supply uncertainty may be caused by different factors such as limited production capability or poor quality control of supplier. In the presence of spot market, the supplier may deliver partially but sell the inventory to the spot market if he or she observes that the spot market's price is quite high [13]. At the same time, spot market is adopted by the buyer as Reactive Procurement Risk Management (RPRM) to meet extra demand or sell the surplus items; but this will lead to risk of volatile spot prices for the procurement model. In addition, the unstable demand from the downstream customer is also dif<sup>fi</sup>cult to be predicted [14]. According to Haksöz et al. [11], the challenges of procurement are to control demand price and supply uncertainties. Besides, the risk attitude of the buyer also affects the procurement decision. A more risk-averse buyer tends to control risk instead of caring more pro<sup>fi</sup>ts. Therefore, the risk attitude of buyer is also considered in our model. Fig. 2 illustrates the possible risks associated with multiple suppliers in the presence of spot market.

![](/api/attachments/ATHV4SRR/fulltext/images/b1793c7eb6b1fb14430b89b1e911b50e10442aff1832d5b0bccd72e819660f31.jpg)  
Fig. 1. Framework of the integrated PRM solution.

## 3.2. Design of PRM assessment (Profit–SaR map based on Monte Carlo simulation)

After identifying three most important risks in procurement in the presence of spot market, risk assessment is carried out with an innovative Pro<sup>fi</sup>t–SaR map based on Monte Carlo simulation. In fact, simulation is widely used to build model-driven decision support system and help de cision makers to assess the potential in<sup>fl</sup>uences [2,17,26]. The advantages of using Monte Carlo simulation are as follows: 1) including random ness through studying the input data for suitable probability distribution; 2) considering correlations and inter-dependency of yield, demand and sport price; and 3) making it possible to study the complicated procurement risk assessment model in the presence of spot market which doesn't have the available analytical solution.

In order to build the simulation model, the components of the pro<sup>fi</sup>t and cost of procurement need to be found out, such as the sales revenue, purchasing cost, penalty cost for not meeting demand, salvage value for extra inventory, <sup>fi</sup>xed cost for purchasing. Let's denote sales revenue sources by $R _ { 1 } , R _ { 2 } , . . . , R _ { m }$ (m is the number of possible revenue sources or ways to add value) and other cost components as $C _ { 1 } , C _ { 2 } , . . . , C _ { n }$ (n is the number of possible costs categories). The pro<sup>fi</sup>t of buyer $\Pi _ { b u y e r }$ purchasing from supplier i is expressed as:

$$
\prod_ {b u y e r} = f _ {i} (R _ {1}, R _ {2}, \dots , R _ {m}; C _ {1}, C _ {2}, \dots , C _ {n});
$$

The simulation model can be implemented using .NET, Java, Matlab, Visual Basic and other languages with Solver SDK Platform, which is a comprehensive software development kit for developing applications using optimization and Monte Carlo simulation. A list of available distributions in cluded in Solver SDK is presented in Table 1.

The selection of suitable distributions depends on the practical situation, but general guidelines are as follows:

The data is collected to run the trial of simulation and “trace driven simulation” can be adopted. Correlation plot is used to decide whether the observation input data is independent or not. With the input data, it is important to identify the input data as continuous, discrete or empirical dis tribution. Various families of distribution can be veri<sup>fi</sup>ed with statistics characteristics such as shape, mean, variance and central tendency. The same set of input data can be used to estimate the parameters with maximum-likelihood estimators. Finally, determination of the representative of the <sup>fi</sup>tted distribution can be done by probability plots, box-plot comparison while the goodness-of-<sup>fi</sup>t hypothesis can be done by Chi-Square Tests. The detail theoretical concept can be referred to Law and Kelton [23]

Table 1  
Available distributions in Solver SDK platform.

<table><tr><td>Distribution category</td><td>Distributions</td></tr><tr><td>Continuous analytic distributions</td><td>Beta; BetaGen; Cauchy; ChiSquare; Erf; Erlang; Exponential; Gamma; InvNormal; Laplace; Logistic; LogLogistics; LogNormal; LogNom2; MaxExtreme; MinExtreme; Myerson; Normal; Pareto; Pareto2; Pareson5; Pearson6; Pert; Rayleigh; Student; Triangular; Uniform; and Weibull,TriangGen.</td></tr><tr><td>Discrete analytic distributions</td><td>Bernoulli; Binomial; Geometric; HyperGeo; IntUniform; Logarithmic; NegBinomial; Poisson;</td></tr><tr><td>Custom distributions</td><td>Cumul; Discrete; DisUniform; Genearl; and Histogram.</td></tr><tr><td>Stochastic information packets (SIPs)</td><td>Creating SIP from data source or distribution</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
The pseudo code of A-EPSaR

Main function ()
{
    Initialize the number of uncertain variables nvars;
    Calculating the correlation coefficients and construct the correlation matrix correl;
    Create instance of the Problem class: Problem = new problem (Solver_Type.Simulate, nvars, nf cns);
    Pass the distribution to uncertain variables;
    Create the simulation evaluator and pass the Evaluator function values to the SDK;
    Tell the SDK to continue simulation until the trial number is reached;
    Save the values of Expected profit and SaR for each supplier.
};

Evaluator function ()
{
    Create a pointer p to the Problem: Problem p = evaluator. Problem;
    Create a pointer pVar to uncertain values;
    The uncertain profit function:
    $\Pi_{buyer} = f_i(R_1, R_2, ..., R_m; C_1, C_2, ..., C_n) = F(pVar_1, pVar_2, ..., pVar_{n vars})$.

}.
</div>

![](/api/attachments/ATHV4SRR/fulltext/images/0e2430fed36843fc5db04ec7fa5baf8fbb3e5d99a9bae1042f3c23bb4d16c404.jpg)  
Fig. 2. Multiple suppliers sourcing in the presence of spot market under uncertainties.

According to the actual situation, distribution can be chosen from the list in Table 1 for every uncertain variable and detailed instructions can be found in the risk solver SDK manual. The correlations among variables can be denoted by the Spearman rank order correlation matrix. The Spearman rank correlation coefficient is used to induce dependency between any two uncertain variables, whether they are both from analytical distribution or even custom distribution. The value of the coef<sup>fi</sup>cient ranges from −1 to 1. The coef<sup>fi</sup>cient $r _ { x , y }$ between random variable x and y can be computed from the sample values x[] and y[] over n trials in Monte Carlo simulation as:

$$
r _ {x, y} = \frac {n \sum_ {i = 1} ^ {n} x _ {i} y _ {i} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) \left(\sum_ {i = 1} ^ {n} y _ {i}\right)}{\sqrt {\left[ n \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2} \right] \left[ n \sum_ {i = 1} ^ {n} y _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} y _ {i}\right) ^ {2} \right]}};
$$

After assigning values to all the risk variables and constructing the correlations among them, the model can be solved by calling a Monte Carlo simulation engine in the Solver SDK. Based on the output of the model, two values can be calculated: Expected pro<sup>fi</sup>t and SaR. The concept of SaR is similar as the VaR (Value at Risk) concept in <sup>fi</sup>nance applications. VaR is used to show the maximal loss that can occur at a given con-<sup>fi</sup>dence level. SaR is the pro<sup>fi</sup>t at risk for the uncertain pro<sup>fi</sup>t function at a speci<sup>fi</sup>ed ‘con<sup>fi</sup>dence level', which can also be expressed as percentile (e.g., 0.95 or 0.99). The above procedures of Monte Carlo simulation are implemented using C#.NET based on the Solver platform. The following is the pseudo code of the simulation algorithm which is named as A-EPSaR.

In order to better con<sup>fi</sup>gure and optimize the supply base, the performance of each potential supplier is evaluated with the simulation algorithm A-EPSaR. For the standardization of the pro<sup>fi</sup>t index and SaR index, the values of the outputs are normalized. The normalized expected pro<sup>fi</sup>t and SaR are then used to classify suppliers into three groups: Preferred supplier; Approved supplier; and Avoided supplier. Preferred suppliers are those suppliers who can help the buyer to achieve a high level of expected pro<sup>fi</sup>t with a low level SaR risk; Approved suppliers are those suppliers who have medium level expected pro<sup>fi</sup>t and risks; An avoided supplier's performance in terms of pro<sup>fi</sup>t and risk is the worst among the three groups, i.e. low pro<sup>fi</sup>t but high risk. Similar classi<sup>fi</sup>cation method for suppliers is also found in Gosling et al. [9], in which suppliers are grouped under three categories based on sourcing <sup>fl</sup>exibility.

From Fig. 3, it is easy to observe that some of the suppliers are less favorable than others. For instance, the type of preferred supplier is de<sup>fi</sup>nitely better than avoided supplier. In order to remove suppliers whose performances are worse than others, pairwise comparisons are conducted among the potential suppliers. For example, if supplier A's expected pro<sup>fi</sup>t is less than that of supplier B and the SaR of supplier A is larger than supplier B, supplier A should then be removed from the supplier pool. Based on the result of pairwise comparisons, the suppliers whose performances are inferior to others are deleted from the supplier's pool and a selected supplier pool P\* is obtained.

## 3.3. The selection of optimal supplier portfolio and risk monitoring

Supply risk assessment enables us to get a selected supplier pool P\* from the original supplier pool. At time t−1, the buyer orders $Q _ { i t }$ units from the contract supplier $i ( i { = } 1 , 2 , . . . , N )$ in the selected supplier pool P\*. At time t, demand d is realized, but the supplier i could deliver only $Y _ { i t }$ units because of random yield. $\lvert \mathbf { f } \sum _ { i = 1 } ^ { N } Y _ { i t }$ is larger than demand d, the buyer will use the spot market to sell $( \textstyle \sum _ { i = 1 } ^ { N } \bar { Y _ { i t } } - d ) ^ { + }$ units at the unit price s.

![](/api/attachments/ATHV4SRR/fulltext/images/e1cf3996a2672c8a8274799ffa015fdca41743247922cde57e429830795a824b.jpg)  
Fig. 3. Classi<sup>fi</sup>cation of potential suppliers.

On the other hand, $\mathrm { i f } \sum _ { i = 1 } ^ { N } Y _ { i t }$ is smaller than demand d, spot market will be used for buying $\begin{array} { r } { ( d - \sum _ { i = 1 } ^ { N } Y _ { i t } ) ^ { + } } \end{array}$ units at price s. Fig. 4 shows the decision making process of procurement.

The following is a summary of related notations:Random yield of supplier i $( i = 1 , 2 , . . . , N )$ y : Normal random variable with mean ${ . \mu _ { i } }$ and stan dard deviation (SD) σ ;Random yield of the optimal supplier pool y: Normal random variable with mean μ and standard deviation σ ;d: Demand is assumed to be a normal random variable with mean $\mu _ { d }$ and standard deviation $\sigma _ { d } ;$ Spot market price s: Normal random variable with mean $\mu _ { s }$ and standard deviation $\sigma _ { s } ;$

r Final value per unit;

w<sub>i</sub> Wholesale price from supplier i;

$w$ Average portfolio wholesale price paid to the supplier per unit;

$k$ The buyer's risk aversion parameter.

$\rho _ { d , s }$ Correlation coef<sup>fi</sup>cient between demand and spot price;

$\rho _ { y , s }$ Correlation coef<sup>fi</sup>cient between yield and spot price;

$\rho _ { d , y }$ Correlation coef<sup>fi</sup>cient between demand and yield;

$p _ { i t }$ The order allocation share for supplier i in period t;

$x _ { i t }$ 1 or 0, if supplier i is selected in period $t , x _ { i t } = 1 ;$

$d _ { j } { \mathrm { . } }$ −/+ The deviation with the idea objective;

$\omega _ { j }$ The weight of the $j ^ { \mathrm { t h } }$ objective;

$M$ A large value to balance the inconformity of data; and

$F C$ The <sup>fi</sup>xed cost of doing business with an additional supplier;

The function of the goal programming model is to calculate the order proportions among the selected suppliers in the pool $P ^ { * } .$ . Supposing that supplier $i ( i { = } 1 , 2 , . . . , N )$ is allocated $p _ { i t }$ percentages in period t. The wholesale price of supplier i is w with <sup>fi</sup>xed cost FC. A goal programming model for aiding order proportions decision making is built as follows:

Objective function: The objective of this optimization model is to <sup>fi</sup>gure out the optimal order shares among the selected supplier pool to obtain the minimal cost at the lowest risk level. The cost contains the purchasing cost of products $\sum _ { i = 1 } ^ { N } \sum _ { t = 1 } ^ { T } p _ { i t } w _ { i }$ and the <sup>fi</sup>xed cost of buying from a supplier i at time period $\vdots \sum _ { i = 1 } ^ { N } \sum _ { t = 1 } ^ { T } \boldsymbol { x } _ { i t } F C$ . The weight of ω denotes the importance of objective j based on the buyer's judgment. $x _ { i t }$ equals to 1 or 0. At the same time, the SaR score is minimized and expected pro<sup>fi</sup>t score is maximized.

$$
\operatorname{Min} \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} p _ {i t} w _ {i} + \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} F C x _ {i t} + M \sum_ {j = 1} ^ {J} \omega_ {j} d _ {j} ^ {- / +};
$$

![](/api/attachments/ATHV4SRR/fulltext/images/be9aea581237f54f8558acd49ecddc8c669a4758359ece90326af83c819c3aed.jpg)  
Fig. 4. The purchasing process in the $t ^ { t h }$ period.

Goal 1: To minimize the SaR (supply at risk): SaR is the SaR risk score of supplier i in the period $t . S a R ^ { + * }$ is the best score. The objective is met by reducing the underachievement of SaR<sup>+</sup>\*.

$$
\sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} S a R _ {i t} x _ {i t} - S a R ^ {+} * \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} x _ {i t} + d _ {1} ^ {-} = 0;
$$

Goal 2: To maximize the expected pro<sup>fi</sup>t score: $E P _ { i t }$ is the pro<sup>fi</sup>t's risk score in the $t ^ { t h }$ period of supplier $\cdot E P ^ { - * }$ is the worst performance score in terms of expected pro<sup>fi</sup>t. The objective is met by maximizing the overachievement of $E P ^ { - * }$

$$
\sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} E P _ {i t} x _ {i t} - E P ^ {-} * \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} x _ {i t} - d _ {2} ^ {+} = 0;
$$

Constraint 1: Demand should be satis<sup>fi</sup>ed:

$$
\sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} p _ {i t} - 1 = 0;
$$

Constraint 2: With the aim of diversifying risks among the selected supplier pool, the order proportion assigned to a single supplier should be bigger than $p ^ { M i n }$ and small than $p ^ { M a x } ;$

$$
p _ {i t} = \left\{ \begin{array}{l l} 0, & x _ {i t} = 0; \\ p _ {i t}, & x _ {i t} = 1. \end{array} \right. \text {   and   } p ^ {M i n} \ll p _ {i t} \leq p ^ {M a x};
$$

The above constraint can be expressed as the following form and it is solvable by linear programming software:

$$
p _ {i t} - x _ {i t} p ^ {M i n} \geq 0;
$$

$$
p _ {i t} \leq x _ {i t} p ^ {M a x};
$$

The order allocation model based on goal programming will generate an optimal order proportion among the supplier pool P\*. The optimal plan is expressed as $\boldsymbol { p } ^ { * } \left( \boldsymbol { p _ { 1 t } } ^ { * } , \boldsymbol { p _ { 2 t } } ^ { * } , . . . , \boldsymbol { p _ { N t } } ^ { * } \right)$ . Supposing that the total amount of products purchased from contract supplier in period $t ( t { = } 1 , 2 , . . . , T )$ is ${ Q _ { t } } ^ { * }$ , the optimal order quantity $Q _ { i t }$ from supplier i in period t equals to ${ Q _ { t } } ^ { * } { p _ { i t } } ^ { * }$

In order to obtain the total order quantity ${ Q _ { t } } ^ { * }$ for the entire selected contract supplier pool, the yield mean, yield standard deviation and average wholesale price need to be determined <sup>fi</sup>rst. As contract suppliers are assumed to be independent with each other, the portfolio yield and wholesale price in the $t ^ { t h }$ period can be expressed as:

the yield mean of the selected portfolio of supplier: $\begin{array} { r } { \mu _ { y } = \sum _ { i = 1 } ^ { N } p _ { i t } ^ { * } \mu _ { i } } \end{array}$

the yield standard deviation of the selected portfolio of supplier: $\begin{array} { r } { \sigma _ { y } = \sqrt { \sum _ { i = 1 } ^ { N } p _ { i t } ^ { * 2 } \sigma _ { i } ^ { 2 } } } \end{array}$ ; and

the average wholesale price of the selected portfolio of supplier: $\begin{array} { r } { w = \sum _ { i = 1 } ^ { N } p _ { i t } ^ { * } w _ { i } . } \end{array}$

Based on the result of contract-spot allocation model in Hong et al. [16], the total number of products purchased from contract supplier in period $t  _ { t } { } ^ { * }$ can be calculated by inputting all the related parameters of the selected supplier pool and spot market.

$$
Q _ {t} ^ {*} = \frac {\frac {\left[ (\mu_ {s} - w) \mu_ {y} + \rho_ {y , s} \sigma_ {y} \sigma_ {s} \right]}{2 k} + \mu_ {d} \mu_ {y} \sigma_ {s} ^ {2} - \rho_ {d , s} \mu_ {y} \sigma_ {s} \sigma_ {d} (r - \mu_ {s}) + \rho_ {y , s} \mu_ {d} \sigma_ {s} \sigma_ {y} (\mu_ {s} - w) - 2 \rho_ {d , s} \rho_ {y , s} \sigma_ {d} \sigma_ {y} \sigma_ {s} ^ {2} + \rho_ {d , y} \sigma_ {d} \sigma_ {y} \left[ (\mu_ {s} - r) (\mu_ {s} - w) + \sigma_ {s} ^ {2} \right]}{(w - \mu_ {s}) ^ {2} \sigma_ {y} ^ {2} + \left(\mu_ {y} ^ {2} + \sigma_ {y} ^ {2}\right) \sigma_ {s} ^ {2} + \rho_ {y , s} ^ {2} \sigma_ {y} ^ {2} + 2 \rho_ {y , s} \mu_ {y} \sigma_ {s} \sigma_ {y} (\mu_ {s} - w)}.
$$

Therefore, the order quantity $Q _ { i t }$ from contract supplier i in the $t ^ { t h }$ period is ${ Q _ { t } } ^ { * } { * } { p _ { i t } } ^ { * }$ . As the changing of both suppliers' performances and market environment will affect the decision of the optimal procurement plan, then in order to ensure the resilient of supply, buyers should keep track of the changing of market environment (e.g., spot price movement) and the performance of potential suppliers (e.g., individual wholesale price and yield), so as to update the procurement plan period by period.

The novel procurement decision support framework helps buyers to make optimal and robust procurement decision including supplier selection and order allocation among multiple supplier sources. The effectiveness of dealing with uncertain supply using spot market along with a traditional contract supplier is studied and validated. Meanwhile, the model also solves the complexity of comparing suppliers with multiple dimension risks, an innovative Pro<sup>fi</sup>t–SaR matrix is proposed to evaluate suppliers and eliminate those less favorable suppliers. Correlations among all the potential uncertainties (demand, supply and spot price) are also considered in the model.

## 4. Case study

In this section, the proposed PRM framework is illustrated by using it to solve a practical problem of <sup>fl</sup>ash memory procurement (Model No: 16Gb 2Gx8 SLC). The case company designs and produces equipments used in the manufacturing and testing of wafers, devices and other electrical components. It also provides third-party semiconductor and burn-in testing services through its test facilities in the United States, Singapore, Thailand, Malaysia and China. Those manufacturing and testing services enable semiconductor devices and other electronic components to meet the requirements of military, aerospace, industrial and commercial applications. Flash memory is one of the most commonly used components in semiconductor manufacturing. The following analysis shows how the case company uses the proposed framework to conduct its procurement risk management with both contract and spot sourcing.

## 4.1. Data collection

The procurement department in the case company is responsible for purchasing items that the Singapore branch requests. After interviewing with the procurement of<sup>fi</sup>cers, it is found that cost, on time delivery, quality and demand are the most important factors considered while choosing suppliers.

Cost is the one of the main decision factor. For a manufacturing company, the cost of raw material largely determines the minimum price of their product that they can offer to the market. Therefore, the company requires the purchasing department to select suppliers who can provide lower price raw material and components. As a procurement of<sup>fi</sup>cer, his/her performance bonus is also tied to his/her ability to get more discounts with the supplier. Meanwhile, on time delivery is also a very important factor to be considered. It is common that one <sup>fi</sup>nished product possibly has several hundred of components. If one of the components can't be delivered on time; the whole manufacturing plan would be affected. Moreover, the factor of quality cannot be overlooked either. If raw materials' quality does not reach the required standard, this quality risk would transmit through supply chain and cause greater loss in pro<sup>fi</sup>t and reputation. Last but not least, the demand of the required <sup>fl</sup>ash memory is also quite dif<sup>fi</sup>cult to predict due to the dynamic business environment.

According to the staff in the procurement department, the conventional procedures of procurement in the case company include the following processes: 1) Estimating the demand of this <sup>fl</sup>ash memory based on their experience; 2) Determining the potential supplier pool by searching their procurement database (IBM Lotus 7.0) with transaction history of the same or similar items; 3) Sending out email to all the suppliers in the pool and request quotations; and 4) Summarizing the quotations from suppliers, selecting a set of suitable suppliers and allocating orders among them. The problem with this procedure is that all the procurement plans are formulated based on the buyer's personal judgment, which is inherently subjective and not accurate. Besides, the unmet extra demand reduces the potential pro<sup>fi</sup>ts and affects the service level of the procurement department. Keeping the additional items as inventory for a long time also causes the risks of dead stock of obsolete component. The fast pace of the high-tech industry might cause the inventories to depreciate dramatically if it is substituted by new model.

In order to support the case company to mitigate the risk of supply, the proposed PRM framework in Section 3 is used. The changes for the existing procurement procedures are mainly in three aspects: using the supplier assessment model to update supplier pool and eliminate those suppliers whose performances are worse than others; adopting goal programming model to support the decision on allocating the order proportions among selected suppliers and utilizing spot market to buy extra demand or sell inventories.

After sending out the requests of quotation emails to the supplier pool at the beginning of the procurement period, <sup>fi</sup>ve suppliers replied and offered their price. The statistics of the <sup>fi</sup>ve suppliers' uncertain yield based on their past performance are recorded in the database. For the value added process in manufacturing company, the product's value is increased as the <sup>fi</sup>nal product. Same as Haksöz and Kadam [13], we assume that the value of each unit is increased to r in the <sup>fi</sup>nal product. The correlation coef<sup>fi</sup>cient can be computed by Monte Carlo simulation using the historical data. Table 2 is the summary of the case company data.

## 4.2. Applying the PRM framework in the case company

According to the situation of the case company, the buyer plans to buy Q units of product with price w to meet demand from end user. The procurement of the case company is exposed to the uncertain demand d and yield y. In order to help the case company to meet the unexpected demand or sell extra stock, spot market is suggested to be adopted as a reactive source with selling price s per unit. Before designing the optimal procurement plan, the performances of each of the supplier from the supplier pool should be quanti<sup>fi</sup>ed so as to select the optimal portfolio of suppliers. Therefore, supposing the Q units of order are placed on a certain supplier from the supplier pool, yQ units are delivered on time by the supplier because of the uncertain yield y. The additional $( y Q - d ) ^ { + }$ <sup>fl</sup>ash memories are sold to spot market with the pro<sup>fi</sup>t (s−w) per unit if s>w (or loss w−s per unit if sbw), and the unexpected demand $( d - y Q ) ^ { + }$ is met via spot market with price s per unit. The <sup>fi</sup>xed cost of doing business with a supplier is FC. Therefore, the assessment model of a potential supplier's pro<sup>fi</sup>t can be expressed as:

Table 2  
Data of the case company.

<table><tr><td colspan="5">Date and parameters</td></tr><tr><td colspan="2">Final value per unit r=30</td><td>Risk aversion parameter Trials per simulation</td><td colspan="2">k=0.005 100,000</td></tr><tr><td colspan="5">Potential supplier pool</td></tr><tr><td>The supplier no.</td><td>Wholesale price  $w_i$ </td><td>Yield mean  $\mu_y$ </td><td colspan="2">Yield SD  $\sigma_y$ </td></tr><tr><td>The supplier A</td><td>8.5</td><td>0.65</td><td colspan="2">0.05</td></tr><tr><td>The supplier B</td><td>9.0</td><td>0.70</td><td colspan="2">0.05</td></tr><tr><td>The supplier C</td><td>9.5</td><td>0.75</td><td colspan="2">0.05</td></tr><tr><td>The supplier D</td><td>10.0</td><td>0.80</td><td colspan="2">0.05</td></tr><tr><td>The supplier E</td><td>10.5</td><td>0.85</td><td colspan="2">0.05</td></tr><tr><td colspan="5">Demand and spot price in 12 periods</td></tr><tr><td>Period no.</td><td>Demand mean  $\mu_d$ </td><td>Demand SD  $\sigma_d$  deviation</td><td>Spot price mean  $\mu_s$ </td><td>Spot price SD  $\sigma_s$  deviation</td></tr><tr><td>1</td><td>110</td><td>26</td><td>11.5</td><td>2.0</td></tr><tr><td>2</td><td>100</td><td>25</td><td>12.0</td><td>2.5</td></tr><tr><td>3</td><td>115</td><td>20</td><td>12.5</td><td>2.5</td></tr><tr><td>4</td><td>125</td><td>24</td><td>13.0</td><td>2.8</td></tr><tr><td>5</td><td>120</td><td>23</td><td>13.5</td><td>2.4</td></tr><tr><td>6</td><td>126</td><td>34</td><td>15.0</td><td>2.5</td></tr><tr><td>7</td><td>140</td><td>29</td><td>15.5</td><td>3.5</td></tr><tr><td>8</td><td>139</td><td>41</td><td>16.0</td><td>2.3</td></tr><tr><td>9</td><td>142</td><td>39</td><td>15.6</td><td>2.4</td></tr><tr><td>10</td><td>140</td><td>35</td><td>15.2</td><td>2.6</td></tr><tr><td>11</td><td>136</td><td>36</td><td>14.8</td><td>2.3</td></tr><tr><td>12</td><td>130</td><td>25</td><td>13.5</td><td>2.4</td></tr><tr><td colspan="5">Correlations</td></tr><tr><td></td><td>Yield</td><td>Spot price</td><td colspan="2">Demand</td></tr><tr><td>Yield</td><td>1.0</td><td>-0.1</td><td colspan="2">-0.05</td></tr><tr><td>Spot price</td><td>-0.1</td><td>1.0</td><td colspan="2">0.2</td></tr><tr><td>Demand</td><td>-0.05</td><td>0.2</td><td colspan="2">1.0</td></tr><tr><td colspan="5">Business policies</td></tr></table>

Estimated <sup>fi</sup>xed cost of adding one more supplier FC=50;  
Prohibitions: 1. Place 60% of total order on a single supplier; 2. Place less than 10% of total order on a single supplier.

$$
\prod_ {b u y e r} = f _ {i} (R _ {1}, R _ {2}, \dots , R _ {m}; C _ {1}, C _ {2}, \dots , C _ {n})
$$

is equal to value added from meeting demand of end user minus procurement cost for the order from contract supplier plus the sales revenue from selling extra stock to the spot market when spot price is higher than the wholesale price (or minus loss by selling extra stock to the spot market when spot price is lower than the wholesale price) plus sales revenue from meeting demand via spot market when <sup>fi</sup>nal value is higher than spot price (or minus loss from meeting demand via spot market when <sup>fi</sup>nal value is lower than spot price) minus <sup>fi</sup>xed cost of doing business with the supplier;

Table 3  
The simulation result of the Pro<sup>fi</sup>t–SaR map.

<table><tr><td>Supplier no.</td><td>Expected profit</td><td>SaR(95%)</td><td>Normalized EP</td><td>Normalized SaR</td></tr><tr><td>Supplier A</td><td>597.01</td><td>243.95</td><td>0.00000</td><td>0.66249</td></tr><tr><td>Supplier B</td><td>709.00</td><td>144.05</td><td>0.24213</td><td>0.32085</td></tr><tr><td>Supplier C</td><td>839.13</td><td>50.23</td><td>0.52348</td><td>0.00000</td></tr><tr><td>Supplier D</td><td>954.03</td><td>181.12</td><td>0.77190</td><td>0.44762</td></tr><tr><td>Supplier E</td><td>1059.53</td><td>342.64</td><td>1.00000</td><td>1.00000</td></tr></table>

The normalization function used is x=Min Max-Min

![](/api/attachments/ATHV4SRR/fulltext/images/e61347f5f031f2456f752e9f16bbbb5da9b8be130dd0ff4ba4b9500d5918a7f4.jpg)  
Table 4  
Step 2: input of the suppliers’ information  
Fig. 5. The decision support system in the case study.  
Step 3: Assess risk of supplier and formulate the order allocation plan

$$
= r \min [ d, y Q ] - w y Q + (s - w) (y Q - d) ^ {+} + (r - s) (d - y Q) ^ {+} - F C;
$$

The model is implemented and simulated according to the simulation algorithm A-EPSaR proposed in Section 3.2. The expected pro<sup>fi</sup>t and SaR are calculated, the results are shown in Table 3. Based on these performances, those less favorable suppliers can be eliminated from the potential supplier pool. For example, as it can be seen from Table 3, the buyer can obtain a normalized expected pro<sup>fi</sup>t of 0.0 and normalized SaR 0.66249 by choosing supplier A. Supplier A is obviously worse than supplier C (normalized expected pro<sup>fi</sup>t 0.52348 and normalized SaR 0.0). As a result, supplier A should be removed from the supplier's pool. By doing the similar comparison analysis, supplier B is also removed from the supplier's pool because it is less favorable comparing with supplier C.

With the help of our designed algorithm, all similar less favorable suppliers are weeded out from the pool and an optimal supplier set is determined. A decision support system which integrates all the risk management steps of PRM framework is implemented and it is shown in Fig. 5. This system can help to assess suppliers and generate the Pro<sup>fi</sup>t–SaR map.

The goal programming model in the decision support system then helps us to determine the proportions of order allocation for each of the supplier. This enables us to further obtain the optimal number of products to source from contract supplier by inputting the portfolio yield and average wholesale price of the portfolio by using the result of contract-spot allocation model in [16]. From Fig. 5, we can observe that both supplier 1 and 2 are sifted out from the pool. Supplier C, D, and E are selected to purchase the products from.

Optimal order allocation among the supplier pool.

<table><tr><td></td><td>Supplier level</td><td>1st period</td><td>2nd period</td><td>3rd period</td><td>4th period</td><td>5th period</td><td>6th period</td><td>7th period</td><td>8th period</td><td>9th period</td><td>10th period</td><td>11th period</td><td>12th period</td><td>Total</td></tr><tr><td>Supplier A</td><td>Avoided</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Supplier B</td><td>Approved</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Supplier C</td><td>Preferred</td><td>82</td><td>77</td><td>101</td><td>106</td><td>116</td><td>131</td><td>126</td><td>158</td><td>152</td><td>140</td><td>142</td><td>124</td><td>1455</td></tr><tr><td>Supplier D</td><td>Preferred</td><td>40</td><td>39</td><td>51</td><td>53</td><td>58</td><td>65</td><td>63</td><td>79</td><td>76</td><td>70</td><td>71</td><td>62</td><td>727</td></tr><tr><td>Supplier E</td><td>Approved</td><td>14</td><td>13</td><td>17</td><td>18</td><td>19</td><td>22</td><td>21</td><td>26</td><td>25</td><td>23</td><td>24</td><td>21</td><td>243</td></tr><tr><td colspan="2">Total quantity</td><td>136</td><td>129</td><td>169</td><td>177</td><td>193</td><td>218</td><td>210</td><td>263</td><td>253</td><td>233</td><td>237</td><td>207</td><td>2425</td></tr><tr><td colspan="15">Portfolio mean: 0.77; portfolio SD: 0.05; portfolio average wholesale price: 9.75.</td></tr></table>

![](/api/attachments/ATHV4SRR/fulltext/images/9b331e63b5dbc416306fd92646de4d63570a6d660b47462baa8a878301834901.jpg)

<table><tr><td></td><td>t=1</td><td>t=2</td><td>t=3</td><td>t=4</td><td>t=5</td><td>t=6</td><td>t=7</td><td>t=8</td><td>t=9</td><td>t=10</td><td>t=11</td><td>t=12</td></tr><tr><td>■ High</td><td>196</td><td>182</td><td>181</td><td>204</td><td>196</td><td>238</td><td>235</td><td>267</td><td>270</td><td>255</td><td>254</td><td>212</td></tr><tr><td>◆ Low</td><td>24</td><td>18</td><td>49</td><td>46</td><td>44</td><td>14</td><td>45</td><td>11</td><td>14</td><td>25</td><td>18</td><td>48</td></tr><tr><td>× Average</td><td>110</td><td>100</td><td>115</td><td>125</td><td>120</td><td>126</td><td>140</td><td>139</td><td>142</td><td>140</td><td>136</td><td>130</td></tr><tr><td>- Optimal</td><td>136</td><td>129</td><td>169</td><td>177</td><td>193</td><td>218</td><td>210</td><td>263</td><td>253</td><td>233</td><td>237</td><td>207</td></tr></table>

Fig. 6. High-low-average demand and the ordered quantity from selected suppliers.

## 4.3. Result analysis

The <sup>fi</sup>nal procurement plan is shown in Table 4. Within the <sup>fi</sup>ve potential suppliers, supplier A is the avoided supplier with high risk and low expected pro<sup>fi</sup>t if chosen by the buyer. Supplier B is approved but its performance is worse comparing with supplier C, so it is also eliminated from the pool. The buyer allocates the order among supplier C, D and E from period 1 to 12. Within the selected supplier pool, the preferred type of supplier C obtains the largest portion of order with a total of 1455 units during the 12 periods. The preferred supplier D get the orders with 727 units at the medium level, and the approved type supplier E obtain the least order with 243 units. After comparing the amount of orders from the suppliers and their offered wholesale price to the manufacturer, we <sup>fi</sup>nd that it is not usually the suppliers with lowest price are selected. For example, supplier A and B offer the lowest price among the <sup>fi</sup>ve suppliers, but none of them are chosen. On the contrary, the most expensive supplier E wins a certain amount of order because of its strong capability on controlling supply uncertainty. As supplier C strikes for the balance between price and uncertain supply, it wins the majority of the order. The managerial challenge faced by a buyer is to set the priority between price and yield. It implies that suppliers should improve their capability to have stable supply rather than putting the competition only on price. It's crucial for management to realize the co-relation between yield, demand and sport price. Instead of using single supplier, risk can hedge against multiple suppliers and multiple periods. Apart from considering the contract supplier, buying in spot market can help to improve pro<sup>fi</sup>t by considering the risk aversion. To generalize the purchase problem, most purchaser buys the average amount but it's realized that slight above average amount can help to reduce risk and improve pro<sup>fi</sup>t performance.

The function and responsibilities of a purchasing department in a manufacturing company are not only to maximize the pro<sup>fi</sup>t as large as possible; at the same time they should try their best to meet the end user's requirements and needs within the speci<sup>fi</sup>ed delivery time. Fig. 6 is plotted to show how the proposed PRM framework can help to meet demand at a low risk. As demand is assumed to be normal distribution, high demand is picked to be (demand mean+3.290527\*demand standard deviation); low demand is (demand mean−3.290527\*demand standard deviation). The range between high and low demand value is selected for ensuring that the possibility of the uncertain demand is within the range of 0.999. Therefore, we can con<sup>fi</sup>dently say that the situation of demand out of the selected range is quite rare. From period 1 to 12, the buyer can purchase the <sup>fl</sup>ash memory chips according to the formulated plan. After comparing the ordered quantity with the high demand, it is found out that high demand and our optimal order quantity are quite close and their average difference is about only 9.89%. This shows the purchasing department can meet the end user's demand with highly reliability. And the gap between the ordered quantity and the actual demand is purchased through spot market. With the help of spot market and the proposed PRM framework, supply risks are controlled and minimized. Therefore, companies are encouraged to adopt spot market sourcing along with their traditional contract supplier, and the related risk management knowledge and capability should also be built up to enhance the procurement processes.

![](/api/attachments/ATHV4SRR/fulltext/images/b5717f7995a16824e457487d2df62985f4dd4c4289586d62628038831c368e40.jpg)  
Fig. 7. Comparisons between ordering average quantity and optimal quantity.

It is obviously that a purchasing department wants to purchase more items from the low cost contract supplier in advance to better meet end user's demand on the premise that the supply risk is controlled. However, without the decision support system, it is often the case that the amount of average order quantity is purchased. Even though the lead time from spot market is negligible, the price is quite high comparing with long term contract supplier. Therefore, the buyer may not meet the end user's demand with a high service level, because the gap between the high demand and average demand is as high as 43.41%. With the help of proposed system, purchaser can order the suggested quantity from the contract supplier so as to maximize the revenue by considering yield risk. The detailed comparisons between ordering average quantity and optimal quantity are shown in Fig. 7. The results show that the buyer can obtain higher expected pro<sup>fi</sup>t and larger objective value after countering the effect of its risk aversion attitude. The value of objective value is determined from [16], which is used to show the combinatorial effects of both expected pro<sup>fi</sup>t and profit standard deviation. The larger the value of the objective value, the better consequence of purchase plan you obtain. For example, during the <sup>fi</sup>rst period, the buyer can obtain 2524.1 units pro<sup>fi</sup>t for buying the optimal quantity instead of 2449.3 units as the average quantity. Even though the pro<sup>fi</sup>t standard deviation is higher for buying with the optimal quantity compared with average quantity, the objective value is much higher using the optimal quantity.

## 5. Conclusions and future research

In this paper, a novel PRM framework is proposed to support decision making of order allocation among multiple suppliers in the presence of spot market. Unlike the majority of previous research on procurement risk management, the effects of correlated demand, yield and price uncertainties are considered in the proposed model. To our knowledge, there is a lack of complete and quantitative procurement decision support system with the existence of spot market. This model provides a solution to address the limitations of the current gap, i.e. the lack of method to model multiple correlated procurement risks, and providing decision support for utilizing multiple contract suppliers and the spot market for procurement from the perspective of risk management. The performance of the proposed model is illustrated by a real case of purchasing <sup>fl</sup>ash memory. Compared with the conventional method of procurement plan formulation which is merely based on estimation and experience, the proposed PRM framework supports purchasers to make the decision about the order quantity to which supplier and determine the supplier portfolio by pair wise comparison. The risk of supply is reduced and a sustainable procurement plan is formulated.

The DSS based on PRM framework are designed and developed. The buyer can identify its speci<sup>fi</sup>c risks in their procurement and build their own pro<sup>fi</sup>t model. Supply risk assessment is supported by the Monte Carlo simulation with the two comparison indicators: expected pro<sup>fi</sup>t and SaR. These two uni<sup>fi</sup>ed risk indexes resolve the complexity of multi dimensions risks assessment. After conducting the pairwise comparisons of performance among the potential suppliers, only those who are favorable are still kept in the pool. For assigning orders in the supplier pool, the buyer can adjust the weight of the two objectives (increase pro<sup>fi</sup>t and mitigate risks) in line with their needs. Once the optimal portfolio with order share is determined, the buyer can <sup>fi</sup>gure out the average portfolio yield and wholesale price. The buyer can then obtain the optimal total quantity from contract suppliers, while the rest of uncertain demand can be met through the reactive supply channel (spot market).

There are some limitations and potential future works of our study. One issue is that the general applicability of our model to purchase all commodities and products. Currently, purchasers may not purchase all the raw materials and commodities from spot markets. Indeed, only some of the items are commonly sourced from spot markets. For example, spot markets are quite common for purchasing memory chips, such as dynamic random access memory and <sup>fl</sup>ash memory. One of the popular B2B platforms is DRAMeXchange. Other products available for spot market trading include grains, livestock, steel, oil and chemicals. To generalize our model into the procurement of other commodities, it may need to consider other reactive channels, such as local supplier or option and futures contracts.

The other future work is to consider inventory in the multiple periods setting. In our study, we focus on some of the time sensitive components such as memory chips. With the rapid development of technology, it is very risky to keep excess inventory in the warehouse. Instead, companies are recommended to meet the extra demand from spot market, and sell surplus items into the spot market too. Therefore, using the platform of DRAMeXchange, buyers are active in both buying and selling memory chips. Companies may choose to sell all their additional reserves in the spot market. However, it is suitable to keep inventory for some kinds of commodities, for instance, grains, oil and steels. In order to enable our model to be also applicable to these commodities, inventory should be considered in the future model.

## References

[1] N. Agrawal, S. Nahmias, Rationalization of the supplier base in the presence of yield uncertainty, Production and Operations Management 6 (3) (1997) 291–308.

[2] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (3) (2008) 657–672.

[3] M.J. Chambers, A. Bailey, A theory of commodity price <sup>fl</sup>uctuations, Journal of Political Economy 104 (5) (1996) 924–957.

[4] S.L. Chen, C.L. Liu, Procurement strategies in the presence of the spot market and analytical framework, Production Planning and Control 18 (4) (2007) 297–309.

[5] S. Chopra, M.S. Sodhi, Managing risk to avoid supply-chain breakdown, MIT Sloan Management Review 46 (1) (2004) 52–61.

[6] A. Federgruen, N. Yang, Selecting a portfolio of suppliers under demand and supply risks, Operations Research 56 (4) (2008) 916–936.

[7] Q. Fu, C.Y. Lee, C.P. Teo, Procurement management using options: Random spot price and the portfolio effect, IIE Transactions 42 (11) (2010) 793–811.

[8] S.H. Ghodsypour, C. O'Brien, A decision support system for supplier selection using an integrated analytical hierarchy process and linear programming, International Journal of Production Economics 56 (1) (1998) 199–212.

[9] J. Gosling, L. Purvis, M.M. Naim, Supply chain <sup>fl</sup>exibility as a determinant of supplier selection, International Journal of Production Economics 128 (1) (2010) 11–21

[10] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a macro prediction market, Decision Support Systems 42 (3) (2006) 1944–1958.

[11] C. Haksöz, C. Kadam, T. Orhanl, Supply risk in fragile contracts, MIT Sloan Management Review 49 (2) (2008) 6–8.

[12] C. Haksöz, S. Seshadri, Supply chain operations in the presence of a spot market: A review with discussion, Journal of the Operational Research Society 58 (2007) 1412–1429.

[13] C. Haksöz, A. Kadam, Supply portfolio risk, The Journal of Operational Risk 4 (1) (2009) 59–77.

[14] J. Hazra, B. Mahadevan, A procurement model using capacity reservation, European Journal of Operational Research 193 (1) (2009) 303–316.

[15] J. Hätönen, T. Eriksson, 30+ years of research and practice of outsourcing – Exploring the past and anticipating the future, Journal of International Management 15 (2) (2009)142-155

[16] Z. Hong, C.K.M. Lee, X. Nie, Proactive and reactive purchasing planning under dependent demand, price and yield risks, Working paper, 2012.

[17] Z. Hua, Y. Sun, X. Xu, Operational causes of bankruptcy propagation in supply chain, Decision Support Systems 51 (3) (2011) 671–681.

[18] P. Jorion, Value at Risk: The new benchmark for managing <sup>fi</sup>nancial risk, McGraw-Hill, New York, 2007.

[19] Kim, Y-H, Memory-Chip prices on asia spot market following Japan earthquake. Wall Street Journal, http://online.wsj.com/article/BT-CO-20110313-704916.html. Accessed on 2 February 2012.

[20] P. Kraljic, Purchasing must become supply management, Harvard Business Review 61 (1983) 109–117.

[21] T.J. Kull, S. Talluri, A supply risk reduction model using integrated multicriteria decision kaking, IEEE Transactions on Engineering Management 55 (3) (2008) 409–419.

[22] O. Lavastre, A. Gunasekaran, A. Spalanzani, Supply chain risk management in French companies, Decision Support Systems 52 (4) (2012) 828–838.

[23] A.M. Law, W.D. Kelon, Simulatin Modeling & Analysis, Mc-Graw-Hill International editons, Fourth edition, Industrial Engineering Series, 2007, pp. 292–397.

[24] S. Li, A. Murat, W. Huang, Selection of contract suppliers under price and demand uncertainty in a dynamic market, European Journal of Operational Research 198 (3) (2009) 830–847.

[25] V. Nagali, J. Hwang, D. Sanghera, M. Gaskins, M. Pridgen, T. Thurston, P. Mackenroth, D. Branvold, P. Scholler, G. Shoemaker, Procurement risk management (PRM) at Hewlett-Packard company, Interfaces 38 (1) (2008) 51–60.

[26] D.J. Power, R. Sharda, Model-driven decision support systems: concept and research directions, Decision Support Systems 43 (3) (2007) 1044–1061.

[27] Qiu, L.F., H.X. Rui, and A.B. Whinston, A Twitter-Based Prediction Market: Social Network Approach (December 6, 2011). ICIS 2011 Proceedings.

[28] B.R. Routledge, D.J. Seppi, C.S. Spatt, Equilibrium forward curves for commodities, Journal of Finance 55 (3) (2000) 1294–1388.

[29] R. Seifert, U. Thonemann, W. Hausman, Optimal procurement strategies for online spot markets, European Journal of Operational Research 152 (3) (2004) 781–799.

[30] S. Spinler, A. Huchzermeier, P. Kleindorfer, Risk hedging via options contracts for physical delivery, OR Spectrum 25 (3) (2003) 379–395.

[31] F.J. Sting, A. Huchzermeier, Ensuring responsive capacity: How to contract with back up suppliers, European Journal of Operational Research 207 (2) (2010) 725–735.

[32] H.R. Stoll, R.E. Whaley, Futures and Options: Theory and Applications, South-Western Publishing Co., Cincinnati, OH, 1993.

[33] C. Tang, Perspectives in supply chain risk management, International Journal of Production Economics 103 (2) (2006) 451–488.

[34] C.A. Watts, K.Y. Kim, C.K. Hahn, Linking purchasing to corporate competitive strategy, International Journal of Supply Chain Management 31 (2) (1995) 2–8.

Hong Zhen joined Nanyang Technological University in August 2009 to pursue his PhD degree under the supervision of Assistant Prof. Carmen Lee Ka Man, after he obtained his bachelor degree in Logistics System Engineering from Huazhong University of Science and Technology, People's Republic of China. His PhD research work focuses on the development of new model for procurement risk management, supplier selection and logistics outsourcing.

Dr LEE Ka Man is currently an assistant professor of the Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University. She obtained her PhD and B. Eng degree from The Hong Kong Polytechnic University. She was awarded Bronze Award of 16th China National Invention Exhibition Award in 2006 and Outstanding Professional Service and Innovation Award, The Hong Kong Polytechnic University in 2006. Her current research areas include logistics information management, manufacturing information systems, product development and data mining techniques. She focuses on applying computational intelligence such as genetic algorithm and arti<sup>fi</sup>cial neural network for supply and demand chain management.
