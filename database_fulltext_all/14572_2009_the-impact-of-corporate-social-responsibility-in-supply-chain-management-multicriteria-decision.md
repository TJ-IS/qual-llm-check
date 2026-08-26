---
otero_id: 14572
otero_key: "QGTP4GN9"
title: "The impact of corporate social responsibility in supply chain management: Multicriteria decision-making approach"
authors: "Jose M. Cruz"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of corporate social responsibility in supply chain management: Multicriteria decision-making approach

Jose M. Cruz ⁎

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269-2041, United States

## a r t i c l e i n f o

Article history: Received 8 August 2007 Received in revised form 8 July 2009 Accepted 30 July 2009 Available online 8 August 2009

Keywords: Supply chain networks Environment Corporate social responsibility Risk management Multicriteria optimization

## a b s t r a c t

This paper develops a decision support framework for modeling and analysis of supply chain networks with corporate social responsibility (CSR). We consider the multicriteria decision-making behavior of the various decision makers (manufacturers, retailers, and consumers), which includes the maximization of net return, the minimization of emission, and the minimization of risk. The emission and the risk are penalized by variable weights. The model allows one to investigate the interplay of the heterogeneous decision makers in the supply chain and to compute the resultant equilibrium pattern of product outputs, transactions, product prices, and levels of social responsibility activities. The results show that social responsibility activities can potentially reduce transaction costs, risk and environmental impact.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

In recent years, there has been a considerable shift in thinking with regard to improving the social and environmental performance of companies [81]. On one hand, there are those that argue that the government should regulate the social and environmental performance of companies [69]. On the other hand, there are those that believe that the private sector generally prefers the <sup>fl</sup>exibility of selfdesigned voluntary standards [80]. Many researchers have tried to understand business motivation to voluntarily adopt CSR programs [23,54]. Swindley [79] argues that many <sup>fi</sup>rms regard CSR as cost of doing business though other <sup>fi</sup>rms may <sup>fi</sup>nd CSR bene<sup>fi</sup>cial. Firms engage in CSR activities as a way to enhance their reputation [30,31], preempt legal sanction [68], respond to NGO action [78], manage their risk [32,38], and to generate customer loyalty [4,5]. Bowman [7] asserts that <sup>fi</sup>rms with proactive CSR that engage in managerial practices like environmental assessment and stakeholder management [84] tend to anticipate and reduce potential sources of business risk, such as potential governmental regulation, labor unrest, or environmental damage [67].

CSR has been a theme of many researchers. Carroll [9] traced the evolution of the CSR concept and found that the CSR construct originated in the 1950s. Carroll [10,11] integrated various streams of CSR research to de<sup>fi</sup>ne a model that extended corporate performance beyond traditional economic and legal considerations to include ethical and discretionary responsibilities. Wartick and Coghran [82] traced the evolution of the corporate social performance model by focusing on three challenges to the concept of CSR: economic responsibility, public responsibility, and social responsiveness. They examined the management of social issues as a dimension of corporate social performance and concluded that the corporate social performance model is valuable for business and society. Carter and Jennings [15] indicated that CSR not only is synonymous with business ethics but also encompasses dimensions including philanthropy, community, workplace diversity, safety, human rights, and environment.

CSR issues surrounding supply chains have only recently come to the fore, notably, in the context of conceptual and survey studies [13,15]. Murphy and Poist [55] stated that although supply chain practitioners have been slow to adopt CSR considerations, social responsibility concepts in the supply chain are increasing in importance. Carter and Jennings [13,15] empirically established primary supply chain CSR categories of environment, diversity, human rights, philanthropy, and safety. Some researchers have examined individual elements of CSR in the supply chain. In response to growing CSR concerns, researchers have begun to deal with environmental risks [2,8,12,70,71], labor practices [25,73,74], procurement [13,14,37,72], and af<sup>fi</sup>rmative action purchasing [16]. Moreover, organizations are expanding their responsibility for their products beyond their sales and delivery locations (cf. [6]) and start managing the CSR of their partners within the supply chain [25,49].

Nevertheless, decision support models that integrate CSR into supply chain management and design are surely needed. Within this new business environment, trade-offs between various objectives while providing resources to CSR activities, are becoming increasingly complex. The questions that arise when applying CSR to supply chain management and design are: (1) given that there is a vast array of decisions to be made on all levels (strategic, tactical, and operational), how does CSR govern and apply to those decisions, and (2) what are the potential con<sup>fl</sup>icts that arise from CSR decision-making in supply chain management and design? To that end, this paper presents a decision support model that incorporates the challenges, opportunities and constraints that managers face when deciding on the level of investment in CSR activities and the choice of trading partners (manufacturer or retailer) given their transaction cost, environmental consciousness and perceived riskiness.

In particular, we develop a multicriteria decision-making supply chain network framework that captures the economic and CSR activities of manufacturing, retailer, and demand market. The models that yield the system optima associated the maximization of net pro<sup>fi</sup>t, emission (waste) minimization, and the minimization of risk, with the weights associated with the environmental and risk criteria being distinct and variable for each such decision maker. This framework makes it possible to simulate different scenarios depending on how concerned (or not) the decision makers are about environmental issues, risk and CSR over all. Moreover, it allows for the explicit determination of the equilibrium levels of social responsibility activities between the decision makers, as well as, product transactions and prices. Hence, the resulting network model allows the decision makers to assess the impact of CSR activities on their key objectives, pro<sup>fi</sup>t, environment and risk.

The network model presented is multilevel in structure and the <sup>fl</sup>ows are product transactions and levels of social responsibility activities. We consider both business-to-business (B2B) and businessto-consumer (B2C) transactions. Prices are associated with the nodes in the network which correspond to the different tiers of decision makers. Manufacturers are assumed to produce homogeneous product and to sell them either over physical or electronic links via the Internet to retailers and through electronic links directly to consumers. Retailers, in turn, can sell the products over physical or virtual links to consumers. Increasing levels of social responsibility activities are assumed to reduce transaction costs, risk, and environmental emissions.

This paper is organized as follows. In Section 2, we develop the model and describe the decision makers' multicriteria decisionmaking behavior. We establish the governing equilibrium conditions along with the corresponding variational inequality formulation. The variables are the equilibrium prices, the equilibrium product <sup>fl</sup>ows, and the equilibrium levels of social responsibility activities. In Section 3, we propose an algorithm, which is then applied to several illustrative numerical examples in Section 4. In Section 5, we provide managerial insights. In Section 6, we discuss the role of decision support systems in CSR. We conclude the paper with Section 7 in which we summarize our results and suggest directions for future research.

## 2. The supply chain network sustainability equilibrium model

In this section, we develop the network model with manufacturers, retailers, and demand markets in which we explicitly integrate levels of social responsibility activities between buyers and sellers. The model assumes that the manufacturing <sup>fi</sup>rms are involved in the production of a homogeneous product and considers I manufacturers, and J retailers, which can be either physical or virtual, as in the case of electronic commerce. There are K demand markets for the homogeneous product in the economy. We assume, for the sake of generality, that each manufacturer can transact directly electronically with the consumers at the demand market through the Internet and can also conduct transactions with the retailers either physically or electronically. We let l refer to a mode of transaction with l=1 denoting a physical transaction and l=2 denoting an electronic transaction via the Internet.

The top-tiered nodes in the supply chain network in Fig. 1, enumerated by $1 , . . . , i . . . , I ,$ represent the I manufacturers. We assume that each manufacturer seeks to determine his optimal production and his sales allocations of the product to the retailers and demand market in order to maximize his own pro<sup>fi</sup>t. We also assume that each manufacturer seeks to minimize the total emission and risk associated with production and transportation to the retailers and demand markets.

Retailers, which are represented by the second-tiered nodes in Fig. 1, function as intermediaries. The nodes corresponding to the retailers are enumerated as: $1 , \ldots j , \ldots J$ with node j corresponding to retailer j. They purchase the product from the manufacturers and sell the product to the consumers at the different demand markets. We assume that the retailers compete with one another in a noncooperative manner. Also, we assume that the retailers are multicriteria decision makers with environmental and risk concerns and they also seek to minimize the emissions and risk associated with transacting (which can include transportation) with manufacturers and consumers as well as in operating their retail outlets.

The bottom-tiered nodes in Fig. 1 represent the demand markets, which can be distinguished from one another by their geographic locations or the type of associated consumers such as whether they correspond, for example, to businesses or to households. There are K bottom-tiered nodes with node k corresponding to demand market k.

The structure of the network in Fig. 1 guarantees that the conservation of <sup>fl</sup>ow equations associated with the production and distribution is satis<sup>fi</sup>ed. The <sup>fl</sup>ows on the links joining the manufacturers with the retailers and demand market nodes are denoted respectively by the components of the vectors $Q ^ { 1 }$ and $Q ^ { 2 } .$ . The <sup>fl</sup>ows on the links joining the retailer nodes with the demand markets are given by the respective components of the vector: $Q ^ { 3 } .$ The variables for this model are given in Table 1. All vectors are assumed to be column vectors.

We now turn to the description of the functions. We <sup>fi</sup>rst discuss the production cost, transaction cost, handling, and unit transaction cost functions given in Table 2. Each manufacturer is faced with a certain production cost function that may depend, in general, on the entire vector of production outputs. Furthermore, each manufacturer and each retailer are faced with transaction costs. The transaction costs are affected/in<sup>fl</sup>uenced by the amount of the product transacted and the levels of social responsibility activities.

Each retailer is also faced with what we term a handling/conversion cost (cf. Table 2), which may include, for example, the cost of handling and storing the product. The handling/conversion cost of a retailer is a function of how much he has obtained of the product from the various manufacturers in what transaction mode.

The consumers at each demand market are faced with a unit transaction cost. As in the case of the manufacturers and the retailers, higher level of social responsibility activities may potentially reduce transaction costs, which means that they can lead to quanti<sup>fi</sup>able cost reductions. The unit transaction costs depend on the amounts of the product that the retailers and the manufacturers transact with the demand markets as well as on the vectors of social responsibility activities established with the demand markets. The generality of the unit transaction cost function structure enables the modeling of competition on the demand side. Moreover, it allows for information exchange between the consumers at the demand markets who may inform one another as to their social responsibility activities which, in turn, can be re<sup>fl</sup>ected in the transaction costs. We assume that the production cost, the transaction cost, and the handling cost functions are convex and continuously differentiable and that the unit cost functions are continuous.

![](/api/attachments/QGTP4GN9/fulltext/images/be62d0f7689fa43180d7f27623bf2d75667a020273644c66abe89c64bae7ad25.jpg)  
Fig. 1. The structure of the supply chain network with electronic commerce.

Table 1  
Variables in the supply chain network sustainability model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $q$ </td><td> $I$ -dimensional vector of the amounts of the product produced by the manufacturers with component  $i$  denoted by  $q_i$ .</td></tr><tr><td> $Q^1$ </td><td>2IJ-dimensional vector of the amounts of the product transacted between the manufacturers with the retailers via the two modes with component  $ijl$  denoted by  $q_{ijl}$ </td></tr><tr><td> $Q^2$ </td><td>IK-dimensional vector of the amounts of the product transacted between the manufacturers and the demand markets with component  $ik$  denoted by  $q_{ik}$ </td></tr><tr><td> $Q^3$ </td><td>2JK-dimensional vector of the amounts of the product transacted between the retailers and the demand markets via the two modes with component  $jkl$  denoted by  $q_{jkl}$ </td></tr><tr><td> $\eta^1$ </td><td>2IJ-dimensional vector of the levels social responsibility activities between the manufacturers and the retailers/mode combinations with component  $ijl$  denoted by  $r_{ijl}$ </td></tr><tr><td> $\eta^2$ </td><td>IK-dimensional vector of the levels social responsibility activities between the manufacturers and the demand market combinations with component  $ik$  denoted by  $r_{ik}$ </td></tr><tr><td> $\eta^3$ </td><td>2JK-dimensional vector of the levels social responsibility activities between the retailers and the demand market/mode combinations with component  $jkl$  denoted by  $r_{jkl}$ </td></tr><tr><td> $\rho_{1ijl}$ </td><td>Price associated with the product transacted between manufacturer  $i$  and retailer  $j$  via mode  $l$ </td></tr><tr><td> $\rho_{1ik}$ </td><td>Price associated with the product transacted between manufacturer  $i$  and demand market  $k$ </td></tr><tr><td> $\rho_{2jkl}$ </td><td>Price associated with the product transacted between retailer  $j$  and demand market  $k$  via mode  $l$ </td></tr><tr><td> $\rho_3$ </td><td>K-dimensional vector of the demand market prices of the product at the demand markets with component  $k$  denoted by  $\rho_{3k}$ </td></tr></table>

Table 2  
Production, handling, transaction, and unit transaction cost functions.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $f_i(q_i)$ </td><td>The production cost function of manufacturer  $i$ </td></tr><tr><td> $c_{ijl}(q_{ijl},\eta_{ijl})$ </td><td>The transaction cost function of manufacturer  $i$  transacting with retailer  $j$  via mode  $l$ </td></tr><tr><td> $c_{ik}(q_{ik},\eta_{ik})$ </td><td>The transaction cost function of manufacturer  $i$  transacting with demand market  $k$  via the Internet</td></tr><tr><td> $c_j(q_j)$ </td><td>The handling/conversion cost function of retailer  $j$ .  $q_j = \sum_{i=1}^{l} \sum_{l=1}^{2} q_{ijl}$ </td></tr><tr><td> $\hat{c}_{ijkl}(q_{ijl},\eta_{ijl})$ </td><td>The transaction cost function of retailer  $j$  transacting with manufacturer  $i$  via mode  $l$ </td></tr><tr><td> $c_{jkl}(q_{jkl},\eta_{jkl})$ </td><td>The transaction cost function of retailer  $j$  transacting with demand market  $k$  via mode  $l$ </td></tr><tr><td> $\hat{c}_{ik}(Q^2,Q^3,\eta^2,\eta^3)$ </td><td>The unit transaction cost function associated with consumers at demand market  $k$  in obtaining the product from manufacturer  $i$ </td></tr><tr><td> $\hat{c}_{jkl}(Q^2,Q^3,\eta^2,\eta^3)$ </td><td>The unit transaction cost function associated with consumers at demand market  $k$  in obtaining the product from retailer  $j$  via mode  $l$ </td></tr></table>

We now turn to the description of the social responsibility activities production cost, emission functions and, <sup>fi</sup>nally, the risk functions and the demand functions. We assume that the social responsibility activities production cost functions as well as the emission and the risk functions are convex and continuously differentiable. The demand functions are assumed to be continuous.

We start by describing the social responsibility activities production cost functions that are given in Table 3. We assume that each manufacturer may spend money, for example, in the form of time/ service, investment in new technology, training employees, and information sharing in order to promote a sound environmental policy. Here social responsibility activities are activities that promote quality assurance, environmental preservation, and compliance. According to Simpson [77], positive relationships have been established between environmental performance and improvements to the manufacturing quality management [45,46], lean manufacturing practice [44,46,76] and worker involvement [34,45,75]. Furthermore, each retailer may actively try to achieve a certain relationship level with a manufacturer and/or demand market.

These social responsibility activities production cost functions may be distinct for each such combination. Their speci<sup>fi</sup>c functional forms may be in<sup>fl</sup>uenced by such factors as the willingness of retailers or demand markets to establish/maintain a level of social responsibility activities as well as the level of previous activities that exist. Hence, we assume that these production cost functions are also affected and in<sup>fl</sup>uenced by the levels of social responsibility activities. We assume that these levels of social responsibility activities (cf. Table 1) take on a value that lies in the range [0,1]. No social responsibility activity is indicated by a level of zero and the strongest possible level of social responsibility activity is indicated by a level of one. The levels of social responsibility activities, along with the product ows, are endogenously determined in the model.

We now describe the emission functions as presented in Table 4. We also assume that the emission functions depend on the volume of transactions between the particular pair via the particular mode, and on the levels of social responsibility activities between decision makers (see, e.g., [20,29,34,36,51]). We assume that each manufacturer seeks to minimize the total emission (waste) generated in the production process as well as in the process of product delivery to the next tier of decision makers. We also assume that the retailers follow similar behavior.

Table 5 describes the risk functions. We note that the risk functions in our model are functions of both the product transactions and the levels of social responsibility activities. Juttner et al. [40] suggest that supply chain-relevant risk sources fall into three categories: environmental risk sources (e.g., <sup>fi</sup>re, social–political actions, or acts of God), organizational risk sources (e.g., production uncertainties), and network-related risk sources. Johnson [39] and Norrman and Jansson [66] argue that network-related risk arises from the interaction between organizations within the supply chain, e.g., due to insuf<sup>fi</sup>- cient interaction and cooperation. Here, we model supply chain organizational risk, environmental risk, and network-related risk by de<sup>fi</sup>ning the risk as a function of product <sup>fl</sup>ows as well as the levels of social responsibility activities. We use levels of social responsibility activities (levels of cooperation) as a way of possibly mitigating these supply risk sources. Indeed, high levels of social responsibility activities are assumed to reduce risk and transactional uncertainty. The results in Feldman et al. [27] suggest that adopting a more environmentally proactive posture has, in addition to any direct environmental and cost reduction bene<sup>fi</sup>ts, a signi<sup>fi</sup>cant and favorable impact on the <sup>fi</sup>rm's perceived riskiness to investors and, accordingly, its cost of equity capital and value in the market place.

Table 3  
Social responsibility activities production cost functions.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $b_{ijl}(\eta_{ijl})$ </td><td>The social responsibility activities production cost function associated with manufacturer i and retailer j transacting in mode l</td></tr><tr><td> $b_{ik}(\eta_{ik})$ </td><td>The social responsibility activities production cost function associated with manufacturer i and demand market k</td></tr><tr><td> $\hat{b}_{ijl}(\eta_{ijl})$ </td><td>The social responsibility activities production cost function associated with retailer j transacting with manufacturer i via mode l</td></tr><tr><td> $b_{jkl}(\eta_{jkl})$ </td><td>The social responsibility activities production cost function associated with retailer j and demand market k in transacting via mode l</td></tr></table>

Table 4 Emission functions.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $e^{i}(\eta^{1},\eta^{2},Q^{1},Q^{2})$ </td><td>The emission function associated with manufacturer  $i$ </td></tr><tr><td> $e^{j}(\eta^{1},\eta^{3},Q^{1},Q^{3})$ </td><td>The emission function associated with retailer  $j$ </td></tr></table>

Table 5 Risk functions.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $r^{i}(Q^{1}, Q^{2}, \eta^{1}, \eta^{2})$ </td><td>The risk incurred by manufacturer i in his transactions</td></tr><tr><td> $r^{j}(Q^{1}, Q^{3}, \eta^{1}, \eta^{3})$ </td><td>The risk incurred by retailer j in his transactions</td></tr></table>

The demand functions as given in Table 6 are associated with the bottom-tiered nodes of the supply chain network. The demand of consumers for the product at a demand market depends, in general, not only on the price of the product at that demand market but also on the prices of the product at the other demand markets. Consequently, consumers at a demand market, in a sense, also compete with consumers at other demand markets.

We now turn to describing the behavior of the various economic decision makers. The model is presented, for ease of exposition, for the case of a single homogeneous product. It can also handle multiple products through a replication of the links and added notation. We <sup>fi</sup>rst focus on the manufacturers. We then turn to the retailers, and, subsequently, to the consumers at the demand markets. An equilibrium solution is denoted by ⁎.

## 2.1. Decision-makers' multicriteria behavior

Multicriteria decision-making methodology is widely used in supply chain research. For background on decision-making in general and on multicriteria decision-making, in particular, see Karwan et al. [41]. Recently, various researchers have argued that multicriteria decision-making with equally weighted objective functions might not adequately reveal an agents preference. Choo and Wedley [18] surveyed procedures for estimating implied criterion weights. See also Ballestero and Romero [1], Weber and Borcherding [83], Yu [86], and Ma et al. [53]. Subsequently, Choo et al. [19] provided interpretations of criteria and their appropriate roles in distinct multicriteria decision-making models. Dong and Nagurney [24] and Nagurney and Ke [60] introduced state-dependent weights for the modeling of a sector's bicriteria decision-making problem in the context of a <sup>fi</sup>nancial network. Nagurney et al. [61] also considered variable weights in the context of a multicriteria network equilibrium model but the model was single-tiered and not supply chain. In this paper, we introduce a class of objective functions with variable weights for multicriteria decision-making in supply chain network equilibrium framework.

Table 6 Demand functions.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $d_k(\rho_3)$ </td><td>The demand for the product at demand market  $k$  as a function of the demand market price vector</td></tr></table>

## 2.1.1. The behavior of the manufacturers and their optimality conditions

The manufacturers are involved in the production of a homogeneous product and in transacting with the retailers physically or electronically as well as directly with the demand markets electronically. Furthermore, they are also involved in establishing social responsibility activities. The quantity of the product produced by manufacturer i must satisfy the following conservation of <sup>fl</sup>ow equation:

$$
q _ {i} = \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} q _ {i j l} + \sum_ {k = 1} ^ {K} q _ {i k},\tag{1}
$$

which states that the quantity of the product produced by manufacturer i is equal to the sum of the quantities transacted between the manufacturer and all retailers (via the two modes) and the demand markets. Hence, in view of Eq. (1), and as noted in Table 2, we have that for each manufacturer i the production cost function is denoted by $f _ { i } ( q _ { i } )$ . Furthermore, each manufacturer may actively try to achieve a certain level of social responsibility activity with a retailer and/or a demand market.

Each manufacturer i tries to maximize his pro<sup>fi</sup>ts. He faces total costs that equal to the sum of his production cost plus the total transaction costs and the costs that he incurs in establishing social responsibility activities. His revenue, in turn, is equal to the sum of the price multiplied by quantities of the product transacted.

Noting the conservation of <sup>fl</sup>ow Eq. (1) one can express the criterion of pro<sup>fi</sup>t maximization for manufacturer i as:

Maximize

$$
\begin{array}{l} z _ {1 i} = \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} \rho_ {1 i j l} q _ {i j l} + \sum_ {k = 1} ^ {K} \rho_ {1 i k} q _ {i k} - f _ {i} (q _ {i}) \\ \quad - \sum_ {j = 1} ^ {I} \sum_ {l = 1} ^ {2} c _ {i j l} \Big (q _ {i j l}, n _ {i j l} \Big) - \sum_ {k = 1} ^ {K} c _ {i k} (q _ {i k}, n _ {i k}) \\ \quad - \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} b _ {i j l} \Big (n _ {i j l} \Big) - \sum_ {k = 1} ^ {K} b _ {i k} (n _ {i k}). \end{array}\tag{2}
$$

Note that in $\operatorname { E q . } \ ( 2 ) ,$ , the <sup>fi</sup>rst two terms represent the revenue whereas the subsequent <sup>fi</sup>ve terms represent the various costs.

In addition to the criterion of pro<sup>fi</sup>t maximization, we assume that each manufacturer also seeks to minimize the total emissions (waste) generated in the production of the product as well as its delivery to the next tier of decision makers, whether retailers or consumers at the demand markets. Here, we also assume that the emission function depends on the volume of transactions between the particular pair via the particular mode, and on the levels of social responsibility activities between decision makers.

The following are some reasons why <sup>fi</sup>rms may decide to minimize their emissions. First, because of public concern regarding environmental issues. Promoting environmental care can enhance a company's image. Second, by minimizing emissions, <sup>fi</sup>rms can reduce their transactions costs in dealing with regulators, local communities, environmental groups, and other external stakeholders [48]. Finally, the main factor driving companies to improve their environmental performance is the risk of being held liable, or found negligent, for accidents or incident with signi<sup>fi</sup>cant real or perceived environmental damage. Klassen and McLaughlin [47], estimate that losses in shareholder value for large publicly traded <sup>fi</sup>rms from environmental incidents can be on the order of hundreds of millions of dollars per incident. To limit liability and negligence claims, a company may choose to implement strict emission reduction mechanisms. Environmental improvements, in turn, can lead to economic bene<sup>fi</sup>ts for companies.

We assume that the emission function for manufacturer i is convex and continuously differentiable and given by the function $e ^ { i } = e ^ { i } ( { \cal Q } ^ { 1 }$ $Q ^ { 2 } , \eta _ { 1 } , \eta _ { 2 } )$ (cf. Table 4).

Hence, the second criterion of each manufacturer can be expressed mathematically as:

$$
\text { Minimize } \quad z _ {2 i} = e ^ {i} \left(Q ^ {1}, Q ^ {2}, \eta_ {1}, n _ {2}\right).\tag{3}
$$

Finally, we analyze the effects of CSR on risk. We assume that each manufacturer is concerned with risk minimization. Risk is de<sup>fi</sup>ned as the possibility for companies to suffer harm or loss for their activities and also for the activities of their partners in the supply chain. In terms of CSR risk, companies may be found liable for pollution, non compliance with regulation, dangerous operations, use of hazardous raw materials, production of hazardous waste, and for health and safety issues. Firms with proactive CSR programs tend to anticipate and reduce potential sources of business risk, such as potential governmental regulation, labor unrest, or environmental damage [67]. Moreover, in addition to any direct environmental and cost reduction bene<sup>fi</sup>ts, CSR activities have a signi<sup>fi</sup>cant and favorable impact on the <sup>fi</sup>rm's perceived riskiness to investors and, accordingly, its cost of equity capital and value in the market place [27].

The third criterion faced by manufacturer i, thus, corresponds to risk (cf. Table 5) minimization and can be expressed mathematically as:

$$
\text { Minimize } \quad z _ {3 i} = r ^ {i} \left(Q ^ {1}, Q ^ {2}, \eta_ {1}, \eta_ {2}\right).\tag{4}
$$

We note that optimization problems of net revenue maximization and risk minimization are fairly standard [24]. Here, use a general risk function and assume that it depends on the volume of transactions between the particular pair via the particular mode, and on the levels of social responsibility activities between decision makers. However, we can also use variance–covariance matrices for measuring risk and return relationship.

The problem that each decision maker will meet is the value tradeoff. That is, the decision maker is faced with a problem of trading off the gain of one objective against another objective. The essence of the issue ${ \mathrm { i } } s ,$ “How much achievement on objective $z _ { 1 i }$ is the decision maker willing to give up in order to improve achievement on objective $z _ { 2 i }$ or/and objective $z _ { 3 i }$ by some amoun $t ? "$ It is rational to assume that most decision makers will not weight all the objectives the same. For example, a risk-averse decision maker may be willing to accept a portfolio with a little lower mean return if the portfolio has lower risk. In other words, the risk-averse decision maker would be willing to take certain risks only if the risk return is much higher. As discussed in Dong and Nagurney $[ 2 4 ]$ , more attention will generally be given to reduce the risk when the risk is high and this kind of decision rationality argues that the objective function should penalize the states with high risk by imposing a greater weight to $z _ { 3 i }$ of high risks than to those $z _ { 3 i }$ with low risks. Thus, we apply the weights which are usually higher than 1 for penalization of the emission and the risk objectives.

De<sup>fi</sup>nition 1. (Criterion-dependent weight). A weight $\omega _ { h t } = \omega _ { h t } ( z _ { h t } )$ is called a criterion-dependent weight for criterion h and decision maker i, if it is strictly increasing, convex, smooth, and nonnegative.

In this paper, the weighted criteria of concern will be that of total emission and risk minimization so we will have that $h = 2 , 3$ in the case of the manufacturers and the retailers. Also, since we have that all decision makers are faced with variable weights, in the case of the manufacturers: $t = i ; i = 1 , \dots I .$ In the case of the retailers, we will have: $t = j ; j = 1 , . . . , J .$

Hence, let $\omega _ { 2 i } ( z _ { 2 i } )$ denote the emission-penalizing weight which depends on the amount of emissions generated per unit of product produced and transacted by manufacturer i. Moreover let $\omega _ { 3 i } ( z _ { 3 i } )$ denote the risk-penalizing weight which depends on the value of risk objective associated with manufacturer i. Furthermore, according to De<sup>fi</sup>nition $1 \omega _ { h i }$ where $h = 2 , 3$ , are strictly increasing, convex, smooth, and nonnegative functions. We now state the following de<sup>fi</sup>nition.

De<sup>fi</sup>nition 2. (Emission and risk-penalizing value function of manufacturer $i ) .$ A value function $U _ { i }$ for manufacturer i is called emission and risk-penalizing value function if

Maximize $U _ { i } = z _ { 1 i } - \omega _ { 2 i } ( z _ { 2 i } ) z _ { 2 i } - \omega _ { 3 i } ( z _ { 3 i } ) z _ { 3 i } ,$

5

where $\omega _ { 2 i } ( z _ { 2 i } ) z _ { 2 i }$ and $\omega _ { 3 i } ( z _ { 3 i } ) z _ { 3 i }$ are as indicated in De<sup>fi</sup>nition 1.

Thus, the multicriteria decision-making problem of manufacturer i can be expressed as:

$$
\begin{array}{l} \text { Maximize } \quad \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} \rho_ {1 i j l} q _ {i j l} + \sum_ {k = 1} ^ {K} \rho_ {1 i k} q _ {i k} - f _ {i} (q _ {i}) \\ \quad - \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} c _ {i j l} \left(q _ {i j l}, \eta_ {i j l}\right) - \sum_ {k = 1} ^ {K} c _ {i k} (q _ {i k}, \eta_ {i k}) - \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} b _ {i j l} \left(\eta_ {i j l}\right) \\ \quad - \sum_ {k = 1} ^ {K} b _ {i k} (\eta_ {i k}) - \omega_ {2 i} \left(e ^ {i}\right) e ^ {i} \left(Q ^ {1}, Q ^ {2}, \eta_ {1}, n _ {2}\right) - \omega_ {3 i} \left(r ^ {i}\right) r ^ {i} \left(Q ^ {1}, Q ^ {2}, \eta_ {1}, \eta_ {2}\right) \end{array}\tag{6}
$$

subject to: $\begin{array} { r } { q _ { i j l } \ge 0 , q _ { i k } \ge 0 , 0 \le \eta _ { i j l } \le 1 , 0 \le \eta _ { i k } \le 1 ; \forall j , k , l . } \end{array}$

Thus, the expression consisting of the <sup>fi</sup>rst seven terms to the right-hand side of the equal sign in Eq. (6) represents the net revenue (which is to be maximized), whereas the last two terms in Eq. (6) represent the weighted dollar values of total emission and risk which are to be minimized by manufacturer i.

We note that value functions have been studied extensively and used for decision problems with multiple criteria (cf. [24,28,42,85,87]). Of course, a special example of a constant weight value function is the one with equal weights (see, e.g., [22,63]). We now prove a theorem and then derive the optimality conditions of the manufacturers. The proof is similar to that found in Dong and Nagurney [24].

Theorem 1. (Concavity). The value function $U _ { i }$ defined in Eq. (6) is strictly concave with respect to $( Q ^ { I } , Q ^ { \bar { 2 } } , \eta ^ { I } , \eta ^ { 2 } ) \in \mathcal { K } ^ { I }$ , ∀i where

$$
\mathcal {K} ^ {1} \equiv \left[ \left(Q ^ {1}, Q ^ {2}, \eta^ {1}, \eta^ {2}\right) | q _ {i j l} \geq 0, q _ {i k} \geq 0, 0 \leq \eta_ {i j l} \leq 1, 0 \leq \eta_ {i k} \leq 1, \forall i, j, k, l \right].
$$

Proof. Let $g _ { i } ( z _ { h i } ) = \omega _ { h i } ( z _ { h i } ) z _ { h i } .$

Since $\omega _ { h i } ( z _ { h i } )$ is assumed to be convex, strictly increasing, and nonnegative, and $z _ { h i } > 0 ,$ , we have

$$
\frac {d g _ {i} (z _ {h i})}{d z _ {h i}} = \frac {d \omega_ {h i} (z _ {h i})}{d z _ {h i}} z _ {h i} + \omega_ {h i} (z _ {h i}) > 0\tag{7}
$$

$$
\frac {d ^ {2} g _ {i} (z _ {h i})}{d z _ {h i} ^ {2}} = \frac {d ^ {2} \omega_ {h i} (z _ {h i})}{d z _ {h i} ^ {2}} z _ {h i} + 2 \frac {d \omega_ {h i} (z _ {h i})}{d z _ {h i}} > 0.\tag{8}
$$

Combining Eqs. (7) and (8), we know that $g _ { i }$ is increasing and strictly convex. $z _ { h i }$ is convex with respect to $( Q ^ { 1 } , \breve { Q } ^ { 2 } , \eta ^ { 1 } , \eta ^ { 2 } )$ according to De<sup>fi</sup>nition 1. Hence the composition of $G _ { i } \equiv - g _ { i } \circ z _ { h i }$ is strictly concave with respect to $( Q ^ { 1 } , Q ^ { 2 } , \eta ^ { 1 } , \eta ^ { 2 } )$ . Since $z _ { h i }$ is linear with respect to $( Q ^ { 1 } , Q ^ { 2 } , \eta ^ { 1 } , \eta ^ { 2 } )$ , the proof is complete.

Now we turn to the optimality conditions of the manufacturers. We assume that the manufacturers compete in a noncooperative fashion following Nash [64,65]. Hence, each manufacturer seeks to determine his optimal strategies, that is production outputs (and shipments), given those of the other manufacturers. De<sup>fi</sup>ne the I-dimensional vector U with components: $U _ { 1 } , . . . , U _ { i }$ and $U ^ { * } { = } U ( Q ^ { 1 * }$ $Q ^ { 2 * } , \eta ^ { 1 * } , \eta ^ { 2 * } )$ . The optimality conditions of all manufacturers $i ; i =$ $1 , . . . ,$ I simultaneously, under the above assumptions (cf. [3,33,56]), can be compactly expressed as:determine $( Q ^ { 1 \dag } , Q ^ { 2 \ast } , \dot { \eta } ^ { 1 \ast } , \dot { \eta } ^ { 2 \ast } ) \in \bar { \mathcal { K } } ^ { \dot { 1 } }$ satisfying

$$
\begin{array}{r l} - \nabla_ {Q ^ {1}} U ^ {* T} \cdot (Q ^ {1} - Q ^ {1 *}) - \nabla_ {Q ^ {2}} U ^ {* T} \cdot (Q ^ {2} - Q ^ {2 *}) - \nabla_ {\eta^ {1}} U ^ {* T} \cdot (\eta^ {1} - \eta^ {1 *}) \\ - \nabla_ {\eta^ {2}} U ^ {* T} \cdot (\eta^ {2} - \eta^ {2 *}) & \geq 0, \forall (Q ^ {1}, Q ^ {2}, \eta^ {1}, \eta^ {2}) \in \mathcal {K} ^ {1}, \end{array} \tag {9}
$$

$$
\mathcal {K} ^ {1} \equiv \left[ \left(Q ^ {1}, Q ^ {2}, \eta^ {1}, \eta^ {2}\right) \mid q _ {i j l} \geq 0, q _ {i k} \geq 0, 0 \leq \eta_ {i j l} \leq 1, 0 \leq \eta_ {i k} \leq 1, \forall i, j, k, l \right].\tag{10}
$$

See Appendix A for the complete formulation.

The inequality (9), which is a variational inequality (cf. [56]) has a meaningful economic interpretation. From the <sup>fi</sup>rst term in $\operatorname { E q . } \left( 9 \right)$ ) we can see that, if there is a positive volume of the product transacted either in a classical manner or via the Internet from a manufacturer to a retailer, then the marginal cost of production plus the marginal cost of transacting plus the weighted marginal cost of emission and risk must be equal to the price that the retailer is willing to pay for the product. If that sum, in turn, exceeds that price then there will be no product transacted.

The second term in Eq. (9) states that there will be a positive <sup>fl</sup>ow of the product transacted between a manufacturer and a demand market if the marginal cost of production of the manufacturer plus the marginal cost of transacting via the Internet for the manufacturer with consumers and the weighted marginal cost of emission and risk is equal to the price the consumers are willing to pay for the product at the demand market.

The third and the fourth term in Eq. (9) show that if there is a positive level of social responsibility activity (and that level is less than one) between a pair of decision makers then the marginal cost associated with the level is equal to the marginal reduction in transaction costs plus the weighted marginal reduction in emission and risk.

## 2.1.2. The behavior of the retailers and their optimality conditions

The retailers, in turn, are involved in transactions both with the manufacturers since they wish to obtain the product for their retail outlets, as well as with the consumers, who are the ultimate purchasers of the product. Thus, as depicted in Fig. 1, a retailer conducts transactions both with the manufacturers and with the consumers. The retailers are also assumed to be multicriteria decision makers in that they seek to maximize pro<sup>fi</sup>ts with manufacturers and consumers, to minimize their individual risk associated with their transactions and to minimize the emissions generated from the perspective of the amounts of the product that they purchase from the manufacturers and the manner in which the transactions occur and the products are shipped.

The actual price charged for the product by retailers j is denoted by ρ , and is associated with transacting with consumers at demand market k via mode l. Similarly, as in the case of manufacturers, later, we discuss how such prices are arrived at. We assume that the retailers are also pro<sup>fi</sup>t maximizers.

The utility maximization problem for retailer j can, hence, be expressed as:

Maximize

$$
\begin{array}{l} z _ {1 j} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} \rho_ {2 j k l} q _ {j k l} - c _ {j} \left(q _ {j}\right) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \hat {c} _ {i j l} \left(q _ {i j l}, \eta_ {i j l}\right) \\ \quad - \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} c _ {j k l} \left(q _ {j k l}, \eta_ {j k l}\right) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \hat {b} _ {i j l} \left(\eta_ {i j l}\right) \\ \quad - \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} b _ {j k l} \left(\eta_ {j k l}\right) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \rho_ {1 i j l} q _ {i j l}. \end{array}\tag{11}
$$

Objective function (11) expresses that the difference between the revenue minus the handling cost and the transaction costs in dealing with manufacturers and the demand markets and the costs for establishing levels of social responsibility activities with manufacturers and demand markets and the payout to the manufacturers should be maximized.

In addition, we assume that each retailer seeks to minimize the emissions and waste associated with his transactions with manufacturers and the demand markets. Hence, the second criterion of each retailer can be expressed mathematically as:

Minimize

$$
z _ {2 j} = e ^ {j} \left(Q ^ {1}, Q ^ {3}, \eta_ {1}, \eta_ {3}\right).\tag{12}
$$

Furthermore, we assume that each retailer is also concerned with risk minimization. For the sake of generality, we assume, as given, a risk function $r ^ { j } ,$ for retailer j in transacting with manufacturer i and with consumers at demand market k through mode l. The risk function is assumed to be continuous and convex and a function of both the product transactions and the levels of social responsibility activities. The third criterion of each retailer can be expressed mathematically as:

Minimize z<sub>3j</sub> = r <sup>j</sup> Q <sup>1</sup>; Q <sup>3</sup>; η<sub>1</sub>; η<sub>3</sub><sup>-</sup> <sup></sup>:

13

Each retailer, as was the case for each manufacturer, will be faced with a value trade-off problem. Depending upon the environmental and risk attitude of the particular retailer, a variable weight associated with his environmental and risk objectives can be constructed in a manner similar to that done for the manufacturers. We assume that the emission and risk-penalizing weights of retailer j are denoted respectively by $\omega _ { 2 j } ( z _ { 2 j } )$ and $\omega _ { 3 j } ( z _ { 3 j } )$ . We also assume that they are strictly increasing, convex, smooth, and nonnegative for each j.

We now, for completeness, provide the following de<sup>fi</sup>nition (akin to De<sup>fi</sup>nition 2).

De<sup>fi</sup>nition 3. (Emission and risk-penalizing value function of retailer j). A value function $U _ { j }$ for retailer j is called emission and risk-penalizing value function if

Maximize U<sub>j</sub> = z<sub>1j</sub> − ω<sub>2j</sub> z<sub>2j</sub><sup>-</sup> <sup></sup>z<sub>2j</sub> − ω<sub>3j</sub> z<sub>3j</sub><sup>-</sup> <sup></sup>z<sub>3j</sub>;

14

where $\omega _ { 2 j } ( z _ { 2 j } )$ and $\omega _ { 3 j } ( z _ { 3 j } )$ are as indicated in Definition 1.

The optimization problem of retailer j can, thus, be expressed as:

Maximize

$$
\begin{array}{l} U _ {j} = \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} \rho_ {2 j k l} q _ {j k l} - c _ {j} (q _ {j}) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \hat {c} _ {i j l} (q _ {i j l}, \eta_ {i j l}) \\ \quad - \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} c _ {j k l} (q _ {j k l}, \eta_ {j k l}) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \hat {b} _ {i j l} (\eta_ {i j l}) \\ \quad - \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} b _ {j k l} (\eta_ {j k l}) - \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} \rho_ {1 i j l} q _ {i j l} \\ \quad - \omega_ {2 j} (e ^ {j}) e ^ {j} (Q ^ {1}, Q ^ {3}, \eta_ {1}, \eta_ {3}) - \omega_ {3 j} (r ^ {j}) r ^ {j} (Q ^ {1}, Q ^ {3}, \eta_ {1}, \eta_ {3}) \end{array}\tag{15}
$$

subject to:

$$
\sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} q _ {j k l} \leq \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} q _ {i j l}\tag{16}
$$

and the nonnegativity constraints: $q _ { i j l } { \ge } 0 , q _ { j k l } { \ge } 0 , 0 { \le } { \eta } _ { i j l } { \le } 1 , 0 { \le } { \eta } _ { j k l } { \le } 1$ $\forall i , k , l .$

Constraint (16) states that consumers cannot purchase more from a retailer than is held in stock.

Now we turn to the optimality conditions of the retailers. Each retailer faces the multicriteria decision-making problem (15), subject to Eq. (16) and the nonnegativity assumption on the variables. As in the case of manufacturers, we assume that the retailers compete in a noncooperative manner, given the actions of the other retailers. Retailers seek to determine the optimal transactions associated with the demand markets and with the manufacturers. In equilibrium, all the transactions between the tiers of network decision makers will have to coincide, as we will see later in this section.

De<sup>fi</sup>ne the J-dimensional vector V with components: $U _ { 1 } , . . . , U _ { j }$ and $V ^ { * } = V ( Q ^ { 1 * } , \ { \bar { Q } } ^ { 3 * } , \ \eta ^ { 1 * } , \ \eta ^ { 3 * } , \ \lambda _ { j } ^ { * } )$ . If one assumes that the handling, transaction cost, production function for levels of social responsibility activities, emission and risk functions are continuously differentiable and convex, then the optimality conditions for all the retailers satisfy the variational inequality: determine $( Q ^ { 1 * } , Q ^ { 3 * } , \eta ^ { 1 * } , \eta ^ { 3 * } , \lambda _ { j } ^ { * } ) \in K ^ { 2 }$ , such that

$$
\begin{array}{l} - \nabla_ {Q ^ {1}} V ^ {* T} \cdot \left(Q ^ {1} - Q ^ {1 *}\right) - \nabla_ {Q ^ {3}} V ^ {* T} \cdot \left(Q ^ {3} - Q ^ {3 *}\right) - \nabla_ {\eta 1} V ^ {* T} \cdot \left(\eta^ {1} - \eta^ {1 *}\right) \\ - \nabla_ {\eta^ {3}} V ^ {* T} \cdot \left(\eta^ {3} - \eta^ {3 *}\right) + \sum_ {j = 1} ^ {J} \left[ \sum_ {i = 1} ^ {I} \sum_ {l = 1} ^ {2} q _ {i j l} ^ {*} - \sum_ {k = 1} ^ {K} \sum_ {l = 1} ^ {2} q _ {j k l} ^ {*} \right] \\ \times \left[ \lambda_ {j} - \lambda_ {j} ^ {*} \right] \geq 0, \forall \left(Q ^ {1}, Q ^ {3}, \eta^ {1}, \eta^ {3}, \lambda\right) \in \mathcal {K} ^ {2}, \end{array} \tag {17}
$$

$$
\mathcal {K} ^ {2} \equiv \left[ \left(Q ^ {1}, Q ^ {3}, \eta^ {1}, \eta^ {3}, \lambda\right) | q _ {i j l} \geq 0, q _ {j k l} \geq 0, 0 \leq \eta_ {i j l} \leq 1, 0 \leq \eta_ {j k l} \leq 1, \lambda_ {j} \geq 0, \forall i, k, l \right].\tag{18}
$$

See Appendix A for the complete formulation.

Here $\lambda _ { j }$ denotes the Lagrange multiplier associated with constraint (16) and λ is the column vector of all the retailers' Lagrange multipliers. These Lagrange multipliers can also be interpreted as shadow prices. Indeed, according to the last term in Eq. (17), λ<sup>⁎</sup> serves as the price to “clear the market” at retailer j.

The economic interpretation of the retailers' optimality conditions is very interesting. The <sup>fi</sup>rst term in Eq. (17) states that if there is a positive amount of product transacted between a manufacturer/ retailer pair via mode l, that is, $q _ { i j l } ^ { * } > 0 ,$ , then the shadow price at the retailer, ${ \bf \bar { \boldsymbol { \Lambda } } } _ { j } ^ { * } ,$ , is equal to the price charged for the product plus the various marginal costs and the associated weighted marginal emission and risk. In addition, the second term in Eq. (17) shows that, if consumers at demand market k purchase the product from a particular retailer j transacted through mode l, which means that, if the $q _ { j k l } ^ { * }$ is positive, then the price charged by retailer $j , \rho _ { 2 j k l } ^ { * } ,$ is equal to ${ \boldsymbol { \lambda } } _ { j } ^ { * }$ plus the marginal transaction costs in dealing with the demand market and the weighted marginal costs for the risk and emission that he has to bear. One also obtains interpretations from Eq. (17) as to the economic conditions at which the levels of social responsibility activities associated with retailers interacting with either the manufacturers or the demand markets will take on positive values.

## 2.1.3. Equilibrium conditions for the demand markets

We now describe the consumers located at the demand markets. The consumers can transact through physical and electronic links with the retailers and through electronic links with the manufacturers. The consumers at the demand market k take the price charged by the retailer, which was denoted by $\rho _ { 2 j k } ^ { * }$ for retailer $\cdot _ { j , \cdot }$ via mode l, the price charged by manufacturer i, which was denoted by $\rho _ { 1 i k } ^ { * }$ , plus the transaction costs, in making their consumption decisions. The equilibrium conditions for the consumers at demand market k, thus, take the form: for all retailers: $j = 1 , . . . ,$ n and all mode $l ; l = 1 ,$ 2:

$$
\rho_ {2 j k l} ^ {*} + \hat {c} _ {j k l} \Big (Q ^ {2 *}, Q ^ {3 *}, \eta_ {2} ^ {*}, \eta_ {3} ^ {*} \Big) \left\{ \begin{array}{l l} = \rho_ {3 k} ^ {*}, & \text {if} q _ {j k l} ^ {*} > 0 \\ \geq \rho_ {3 k} ^ {*}, & \text {if} q _ {j k l} ^ {*} = 0 \end{array} \right.,\tag{19}
$$

and for all source agents $i ; i { = } 1 , . . . ,$ m:

$$
\rho_ {1 i k} ^ {*} + \hat {c} _ {i k} \big (Q ^ {2 *}, Q ^ {3 *}, \eta_ {2} ^ {*}, \eta_ {3} ^ {*} \big) \left\{ \begin{array}{l l} = \rho_ {3 k} ^ {*}, & \text {if} \quad q _ {i k} ^ {*} > 0 \\ \geq \rho_ {3 k} ^ {*}, & \text {if} \quad q _ {i k} ^ {*} = 0 \end{array} \right..\tag{20}
$$

In addition, we must have that

$$
d _ {k} \left(\rho_ {3} ^ {*}\right) \left\{ \begin{array}{l l} = \sum_ {j = 1} ^ {n} \sum_ {l = 1} ^ {2} q _ {j k l} ^ {*} + \sum_ {i = 1} ^ {m} q _ {i k} ^ {*} & \text { if } \quad \rho_ {3 k} ^ {*} > 0 \\ \leq \sum_ {j = 1} ^ {n} \sum_ {l = 1} ^ {2} q _ {j k l} ^ {*} + \sum_ {i = 1} ^ {m} q _ {i k} ^ {*} & \text { if } \quad \rho_ {3 k} ^ {*} = 0 \end{array} . \right.\tag{21}
$$

Condition (19) states that consumers at demand market k will purchase the product from retailer $j ,$ if the price charged by the retailer for the product plus the transaction cost (from the perspective of the consumer) does not exceed the price that the consumers are willing to pay for the product, $i . { \mathrm { e . , } } \rho _ { 3 k } ^ { * }$ . Note that, according to Eq. (19), if the transaction costs are identically equal to zero, then the price faced by the consumers for a given product is the price charged by the retailer. Condition (20) states the analogue, but for the case of electronic transactions with the manufacturers.

Condition (21), on the other hand, states that, if the price the consumers are willing to pay for the product at a demand market is positive, then the quantity purchased/consumed by the consumers at the demand market is precisely equal to the demand.

In equilibrium, conditions (19), (20), and (21) will have to hold for all demand markets and these, in turn, can be expressed also as an inequality analogous to those in Eqs. (9) and (17) and given by: determine $( Q ^ { 2 * } , Q ^ { 3 * } , \rho _ { 3 } ^ { * } ) \in R _ { + } ^ { ( I + 2 J + 1 ) ^ { \bf \hat { K } } }$ , such that

$$
\begin{array}{l} \sum_ {k = 1} ^ {o} \sum_ {j = 1} ^ {n} \sum_ {l = 1} ^ {2} \left[ \rho_ {2 j k l} ^ {*} + \hat {c} _ {j k l} ^ {*} - \rho_ {3 k} ^ {*} \right] \times \left[ q _ {j k l} - q _ {j k l} ^ {*} \right] \\ + \sum_ {i = 1} ^ {m} \sum_ {k = 1} ^ {o} \left[ \rho_ {1 i k} ^ {*} + \hat {c} _ {i k} ^ {*} - \rho_ {3 k} ^ {*} \right] \times \left[ q _ {i k} - q _ {i k} ^ {*} \right] \\ + \sum_ {k = 1} ^ {o} \left[ \sum_ {j = 1} ^ {n} \sum_ {l = 1} ^ {2} q _ {j k l} ^ {*} + \sum_ {i = 1} ^ {m} q _ {i k} ^ {*} - d _ {k} (\rho_ {3} ^ {*}) \right] \times \left[ \rho_ {3 k} - \rho_ {3 k} ^ {*} \right] \geq 0, \\ \forall (Q ^ {2}, Q ^ {3}, \rho_ {3}) \in R _ {+} ^ {(I + 2 J + 1) K} \end{array}\tag{22}
$$

where $\hat { c } _ { j k l } ^ { * } = \hat { c } _ { j k l } ( Q ^ { 2 * } , Q ^ { 3 * } , \eta _ { 2 } ^ { * } , \eta _ { 3 } ^ { * } )$ and $\hat { c } _ { i k } ^ { * } { = } \hat { c } _ { i k } ( Q ^ { 2 * } , Q ^ { 3 * } , \eta _ { 2 } ^ { * } , \eta _ { 3 } ^ { * } )$

In the context of the consumption decisions, we have utilized demand functions, whereas pro<sup>fi</sup>t functions, which correspond to objective functions, were used in the case of the manufacturers and the retailers. Since we can expect the number of consumers to be much greater than that of the manufacturers and retailers we believe that such a formulation is more natural.

## 2.2. The equilibrium conditions of the supply chain network

In equilibrium, the product <sup>fl</sup>ows that the manufacturers transact with the retailers must coincide with those that the retailers actually accept from them. In addition, the amounts of the products that are obtained by the consumers must be equal to the amounts that both the manufacturers and the retailers actually provide. Hence, although there may be competition between decision makers at the same level of tier of nodes of the supply chain network there must be, in a sense, cooperation between decision makers associated with pairs of nodes (through positive <sup>fl</sup>ows on the links joining them). Thus, in equilibrium, the prices and product <sup>fl</sup>ows must satisfy the sum of the optimality conditions (9) and (17) and the equilibrium conditions (22). We make these relationships rigorous through the subsequent de<sup>fi</sup>nition and variational inequality derivation below.

De<sup>fi</sup>nition 4. (Supply chain network equilibrium). The equilibrium state of the supply chain network is one where the <sup>fl</sup>ows and levels of social responsibility activities between the tiers of the network coincide and the product transactions, levels of social responsibility activities and prices satisfy the sum of conditions (9), (17), and (22).

The equilibrium state is equivalent to the following:

Theorem 2. (variational inequality formulation). The equilibrium conditions governing the supply chain network model according to De<sup>fi</sup>nition 4 are equivalent to the solution of the variational inequality given by: determine $( Q ^ { I * } , Q ^ { 2 * } , Q ^ { 3 * } , \eta ^ { I * } , \eta ^ { 2 * } , \stackrel { . } { \eta } ^ { 3 * } , \lambda ^ { * } , \rho _ { 3 } ^ { * } ) \in \kappa ,$ , satisfying:

$$
\langle F (X ^ {*}), X - X ^ {*} \rangle \geq 0, \quad \forall X \in \mathcal {K},\tag{23}
$$

where $X \equiv ( Q ^ { 1 } , Q ^ { 2 } , Q ^ { 3 } , \eta ^ { 1 } , \eta ^ { 2 } , \eta ^ { 3 } , \lambda , \rho _ { 3 } )$ and $\boldsymbol { F } ( \boldsymbol { X } ) \equiv ( F _ { i j l } , F _ { i k } , F _ { j k l } , \hat { F } _ { i j l } , \hat { F } _ { i k } ,$ $\hat { F } _ { j k l } , F _ { j } , F _ { k } )$ with indices: $i = 1 , . . . , I ; j = 1 , . . . , J ; k = 1 , . . . , K ; l = 1 , 2$ , and the speci<sup>fi</sup>c components of F given by the functional terms preceding the multiplication signs of the sum of conditions (9), (17), and (22). The term $\langle \cdot , \cdot \rangle$ denotes the inner product in N-dimensional Euclidean space [56].

We now describe how to recover the prices associated with the <sup>fi</sup>rst two tiers of nodes in the supply chain network. Clearly, the components of the vector $\rho _ { 3 } ^ { * }$ are obtained directly from the solution of variational inequality (23). In order to recover the second tier prices associated with the retailers one can (after solving variational inequality (23) for the particular numerical problem) either (cf. (19)) set $\rho _ { 2 j k l } ^ { * } = \mathrm { \bar { [ } } \rho _ { 3 k . } ^ { * } - \hat { c } _ { j k l } ^ { * } \mathrm { ] } ,$ , for any $j , \ k , \ l$ such that $q _ { j k l } ^ { * } > 0 ,$ , or (cf. (17)) for any $q _ { j k l } ^ { * } > 0 ,$ set $\begin{array} { r } { \rho _ { 2 j k l } ^ { * } = \left[ \frac { \partial c _ { j k l } ^ { * } } { \partial q _ { j k l } } + \omega _ { 2 j } \left( e ^ { j ^ { * } } \right) \frac { \partial e ^ { j ^ { * } } } { \partial q _ { j k l } } + \frac { \partial _ { \omega _ { 2 j } } \left( e ^ { j ^ { * } } \right) } { \partial q _ { j k l } } e ^ { j ^ { * } } + \omega _ { 3 j } \left( r ^ { j ^ { * } } \right) \frac { \partial r ^ { j ^ { * } } } { \partial q _ { j k l } } + \frac { \partial _ { \omega _ { 3 j } } \left( r ^ { j ^ { * } } \right) } { \partial q _ { j k l } } r ^ { j ^ { * } } + \lambda _ { j } ^ { * } \right] . } \end{array}$

-<sub>Similarly, from Eq. (9) we can infer that the top tier prices</sub> comprising the vector $\rho _ { 1 } ^ { * }$ can be recovered (once the variational inequality (23) is solved with particular data) thus: for any $i , j , l ,$ such that $q _ { i j l } ^ { * } > 0 ,$ , set $\begin{array} { r } { \rho _ { 1 i j l } ^ { * } = \left\lceil \frac { \partial f _ { i } \left( q _ { i } ^ { * } \right) } { \partial q _ { i j l } } \right. + \left. \frac { \partial c _ { i j l } \left( q _ { i j l } ^ { * } , n _ { i i j } ^ { * } \right) } { \partial q _ { i j l } } + \omega _ { 2 i } \left( e ^ { i * } \right) \frac { \partial e ^ { i ^ { * } } } { \partial q _ { i j l } } \right. + } \end{array}$ $\begin{array} { r } { e ^ { i * } \frac { \partial \omega _ { 2 i } \left( e ^ { i * } \right) } { \partial q _ { i j l } } + \omega _ { 3 i } ( r ^ { i * } ) \frac { \partial r ^ { i ^ { * } } } { \partial q _ { i j l } } + r ^ { i ^ { * } } \frac { \partial \omega _ { 3 i } \left( r ^ { i ^ { * } } \right) } { \partial q _ { i j l } } \biggr ] } \end{array}$ ; or, equivalently to $\left[ \lambda _ { j } ^ { \ast } - \right.$ $\begin{array} { r l } & { \frac { \partial c _ { j } \left( q _ { j } ^ { * } \right) } { \partial q _ { j l } } - \frac { \partial \hat { c } _ { i j l } \left( q _ { i l } ^ { * } , n _ { i l i } ^ { * } \right) } { \partial q _ { i j l } } - \omega _ { 2 j } \left( e ^ { j ^ { * } } \right) \frac { \partial e ^ { j * } } { \partial q _ { i j l } } - \frac { \partial \omega _ { 2 j } \left( e ^ { j * } \right) } { \partial q _ { i j l } } e ^ { j * } - \omega _ { 3 j } \left( r ^ { j * } \right) \frac { \partial r ^ { j * } } { \partial q _ { i j l } } - } \end{array}$ ${ \frac { \partial \omega _ { 3 j } ( r ^ { j * } ) } { \partial q _ { i i l } } } r ^ { j * } ] ( \mathrm { c f . } \ ( 1 7 ) ) .$

-<sub>In addition, in order to recover the first tier prices associated with</sub> the demand market one can (after solving variational inequality (23) for the particular numerical problem) either (cf. (9)) set $\bar { \rho } _ { 1 i k } ^ { * } = $ $\begin{array} { r } { \left[ \frac { \partial f _ { i } ( q _ { i } ^ { * } ) } { \partial q _ { i k } } + \frac { \partial c _ { i k } ^ { * } } { \partial q _ { i k } } + \omega _ { 2 i } ( e ^ { i * } ) \frac { \partial e ^ { i * } } { \partial q _ { i k } } + e ^ { i * } \frac { \partial \omega _ { 2 i } ( e ^ { i * } ) } { \partial q _ { i k } } + \omega _ { 3 i } ( r ^ { i * } ) \frac { \partial r ^ { i * } } { \partial q _ { i k } } + r ^ { i * } \frac { \partial \omega _ { 3 i } ( r ^ { i * } ) } { \partial q _ { i k } } \right] , } \end{array}$ for any i; k such that $q _ { i k } ^ { * } > 0 ,$ , or (cf. (20)) for any $q _ { i k } ^ { * } > 0 ,$ , set $\rho _ { 1 i k } ^ { * } =$ $[ \rho _ { 3 k } ^ { * } - \hat { c } _ { i k } ^ { * } ]$

Under the above pricing mechanism, the optimality conditions (9) and (17) as well as the equilibrium conditions (22) also hold separately (as well as for each individual decision maker).

## 3. Qualitative properties and computational procedure

In this section, we provide some qualitative properties of the solution to variational inequality (23). In particular, we derive existence and uniqueness results. We also investigate properties of the function F (cf. (23)) that enters the variational inequality of interest here.

Since the feasible set is not compact we cannot derive existence simply from the assumption of continuity of the functions. Nevertheless, we can impose a rather weak condition to guarantee existence of a solution pattern. Let

$$
\begin{array}{l} \mathcal {K} _ {b} = \Big \{\big (Q ^ {1}, Q ^ {2}, Q ^ {3}, \eta^ {1}, \eta^ {2}, \eta^ {3}, \lambda , \rho_ {3} \big) | 0 \leq Q ^ {1} \leq b _ {1}; 0 \leq Q ^ {2} \leq b _ {2}; \\ \qquad 0 \leq Q ^ {3} \leq b _ {3}; 0 \leq \eta^ {1} \leq b _ {4}; 0 \leq \eta^ {2} \leq b _ {5}; 0 \leq \eta^ {3} \leq b _ {6}; 0 \leq \lambda \leq b _ {7}; \\ \qquad 0 \leq \rho_ {3} \leq b _ {8} \Big \}. \end{array}\tag{24}
$$

where $b = ( b _ { 1 } , b _ { 2 } , b _ { 3 } , b _ { 4 } = 1 , b _ { 5 } = 1 , b _ { 6 } = 1 , b _ { 7 } , b _ { 8 } ) \geq 0$ and $Q ^ { 1 } \leq b _ { 1 } ;$ $Q ^ { 2 } \leq b _ { 2 } ; \ Q ^ { 3 } \leq b _ { 3 } ; \ \eta ^ { 1 } \leq b 4 ; \ \eta ^ { 2 } \leq b _ { 5 } ; \ \eta ^ { 3 } \leq b _ { 6 } ; \ \Lambda \leq b _ { 7 } ; \ \rho _ { 3 } \leq b _ { 8 }$ means that $q _ { i j l } \leq b _ { 1 } ; ~ q _ { i k } \leq b _ { 2 } ; ~ q _ { j k l } \leq b _ { 3 } ; ~ \eta _ { i j l } \leq 1 ; ~ \eta _ { i k } \leq 1 ; ~ \eta _ { j k l } \leq 1 ; ~ \lambda _ { j } \leq b _ { 7 } ; ~ \mathrm { a n d } ~ \rho _ { 3 k } \leq b _ { 8 }$ for all $i , j , l , k .$ . Then $\displaystyle { \mathcal { K } } _ { b }$ is a bounded closed convex subset of $\kappa \equiv [ ( Q ^ { 1 }$ $Q ^ { 2 } , Q ^ { 3 } , \bar { \eta } ^ { 1 } , \eta ^ { 2 } , \eta ^ { 3 } , \lambda , \rho _ { 3 } ) | q _ { i j l } \geq 0 , q _ { i k } \geq 0 , q _ { j k l } \geq 0 , 0 \leq \eta _ { i j l } \leq 1 , 0 \leq \eta _ { i k } \leq 1$ $0 \le \eta _ { j k l } \le 1 , \ \rho _ { 3 k } \ge 0 , \ \lambda _ { j } \ge 0 ; \ \forall i , j , \ k , \ l ]$ . Thus, the following variational inequality

$$
\left\langle F \left(X ^ {b}\right) ^ {T}, X - X ^ {b} \right\rangle \geq 0, \quad \forall X ^ {b} \in \mathcal {K} _ {b},\tag{25}
$$

admits at least one solution $X ^ { b } \in \mathcal { K } _ { b } ,$ from the standard theory of variational inequalities, since $\displaystyle { \mathcal { K } } _ { b }$ <sup>K</sup>is compact and F is continuous. <sup>K</sup>Following Kinderlehrer and Stampacchia [43] (see also Theorem 1.5 in [56]), we then have:

Theorem 3. Variational inequality (23) admits a solution if and only if there exists a $b > 0 ,$ such that variational inequality (25) admits a solution in $\displaystyle { \mathcal { K } } _ { b }$ with

$$
Q ^ {1 b} <   b _ {1}, Q ^ {2 b} <   b _ {2}, Q ^ {3 b} <   b _ {3}, \eta^ {1 b} <   b _ {3} \quad \eta^ {2 b} <   b _ {5} \quad \eta^ {3 b} <   b _ {6} \quad \lambda^ {b} <   b _ {7}, \rho_ {3} ^ {b} <   b _ {8}.\tag{26}
$$

Theorem 4. (Existence). Suppose that there exist positive constants M, N, R with $R > 0 ,$ such that:

$$
\begin{array}{l} \frac {\partial f _ {i}}{\partial q _ {i j l}} + \frac {\partial c _ {i j l}}{\partial q _ {i j l}} + \frac {\partial c _ {j}}{\partial q _ {i j l}} + \frac {\partial \hat {c} _ {i j l}}{\partial q _ {i j l}} + \omega_ {2 i} \Big (e ^ {i} \Big) \frac {\partial e ^ {i}}{\partial q _ {i j l}} + e ^ {i} \frac {\partial \omega_ {2 i} \Big (e ^ {i} \Big)}{\partial q _ {i j l}} \\ \quad + \omega_ {3 i} \Big (r ^ {i} \Big) \frac {\partial r ^ {i}}{\partial q _ {i j l}} + r ^ {i} \frac {\partial \omega_ {3 i} \Big (r ^ {i} \Big)}{\partial q _ {i j l}} + \omega_ {2 j} \Big (e ^ {j} \Big) \frac {\partial e ^ {j}}{\partial q _ {i j l}} + \frac {\partial \omega_ {2 j} \Big (e ^ {j} \Big)}{\partial q _ {i j l}} e ^ {j} \\ \quad + \omega_ {3 j} \Big (r ^ {j} \Big) \frac {\partial r ^ {j}}{\partial q _ {i j l}} + \frac {\partial \omega_ {3 j} \Big (r ^ {j} \Big)}{\partial q _ {i j l}} r ^ {j} \geq M, \forall Q ^ {1} \text {with} q _ {i j l} \geq N, \forall i, j, l, \end{array}\tag{27}
$$

$$
\frac {\partial f _ {i}}{\partial q _ {i k}} + \frac {\partial c _ {i k}}{\partial q _ {i k}} + \omega_ {2 i} (e ^ {i}) \frac {\partial e ^ {i}}{\partial q _ {i k}} + e ^ {i} \frac {\partial \omega_ {2 i} (e ^ {i})}{\partial q _ {i k}} + \omega_ {3 i} (r ^ {i}) \frac {\partial r ^ {i}}{\partial q _ {i k}}\tag{28}
$$

$$
+ r ^ {i} \frac {\partial \omega_ {3 i} (r ^ {i})}{\partial q _ {i k}} + \hat {c} _ {i k} \geq M, \quad \forall Q ^ {2} \text {with} q _ {i k} \geq N, \quad \forall i, k,
$$

$$
\frac {\partial c _ {j k l}}{\partial q _ {j k l}} + \omega_ {2 j} (e ^ {j}) \frac {\partial e ^ {j}}{\partial q _ {j k l}} + \frac {\partial \omega_ {2 j} (e ^ {j})}{\partial q _ {j k l}} e ^ {j} + \omega_ {3 j} (r ^ {j}) \frac {\partial r ^ {j}}{\partial q _ {j k l}} + \frac {\partial \omega_ {3 j} (r ^ {j})}{\partial q _ {j k l}} r ^ {j}\tag{29}
$$

$$
+ \hat {c} _ {j k l} \geq M, \quad \forall Q ^ {3} \quad \text { with } \quad q _ {j k l} \geq N, \quad \forall j, k, l,
$$

$$
d _ {k} \left(\rho_ {3} ^ {*}\right) \leq N, \quad \forall \rho_ {3} \quad \text { with } \quad \rho_ {3 k} > R, \quad \forall k.\tag{30}
$$

Then variational inequality (23) admits at least one solution.

Proof. Follows using analogous arguments as the proof of existence for Proposition 1 in Nagurney and Zhao [57].

Assumptions (27) and (28) are reasonable from an economics perspective, since when the product shipment between a manufacturer and demand market pair or a manufacturer and retailer is large, we can expect the corresponding sum of the associated marginal costs of production, handling, and transaction from either the manufacturer's or the retailer's perspectives as well as the transaction cost associated with the consumers, to exceed a positive lower bound. Moreover, in the case where the price of the product as perceived by consumers at a demand market is high, we can expect that the demand for the product at the demand market to not exceed a positive bound.

De<sup>fi</sup>nition 5. (Additive production cost). Suppose that for each manufacturer i, the production cost f<sub>i</sub> is additive, that is,

$$
f _ {i} (q) = f _ {i} ^ {1} (q i) + f _ {i} ^ {2} (\overline {{q}} _ {i}),\tag{31}
$$

where $f _ { i } ^ { 1 } ( q _ { i } )$ is the internal production cost that depends solely on the manufacturer's own output level $q _ { i } ,$ which may include the production operation and the facility maintenance, etc., and $f _ { i } ^ { 2 } ( { \bar { q } } _ { i } )$ is the interdependent part of the production cost that is a function of all the other manufacturers' output levels $\bar { q } _ { i } = ( q _ { 1 } , . . . , q _ { i - 1 } , q _ { i + 1 } , . . . , q _ { I } )$ and reflects the impact of the other manufacturers' production patterns on manufacturer i's cost. This interdependent part of the production cost may describe the competition for the resources, consumption of the homogeneous raw materials, etc.

We now establish additional qualitative properties both of the function F that enters the variational inequality problem (cf. (23)), as well as uniqueness of the equilibrium pattern. Since the proofs of Theorems 5 and 6 are similar to the analogous proofs in Nagurney et al. [62], they are omitted here.

Theorem 5. (Monotonicity). Suppose that the production cost functions $f _ { i } ; i = 1 , . . . , I ,$ , are additive, as defined in De<sup>fi</sup>nition $5 ,$ and that the $f _ { i } ^ { 1 } ; i = 1 ,$ $\ldots , I ,$ , are convex functions. If the $c _ { i j l } , c _ { j } , \hat { c } _ { i j l } , c _ { i k } , b _ { i j l } , b _ { i k } , \hat { b } _ { i j l } , b _ { j k l } , e ^ { i } , e ^ { j } , r ^ { i } ,$ and $r ^ { j }$ functions are convex; the $\hat { c } _ { j k l }$ and the $\hat { c } _ { i k }$ functions are monotone increasing, and the $d _ { k }$ functions are monotone decreasing functions of the generalized prices, for all i, j, k, l, then the vector function F that enters the variational inequality (23) is monotone, that is,

$$
\left\langle \left(F (X ^ {\prime}) - F (X ^ {\prime \prime})\right) ^ {T}, X ^ {\prime} - X ^ {\prime \prime} \right\rangle \geq 0, \quad \forall X ^ {\prime}, X ^ {\prime \prime} \in \mathcal {K}.\tag{32}
$$

Theorem 6. (Strict monotonicity). Assume all the conditions of Theorem $5 .$ In addition, suppose that one of the families of convex functions $f _ { i } ^ { l } , c _ { i j l } , c _ { j } , \hat { c } _ { i j l } , c _ { i k } , b _ { i j l } , b _ { i k } , \hat { b } _ { i j l } , b _ { j k l } , e ^ { i } , e ^ { j } , r ^ { i } ,$ , and r <sup>j</sup>, for all i, j, k, l is a family of strictly convex functions. Suppose also that $\hat { c } _ { i k } , \hat { c } _ { j k l } , a n d - d _ { k } ,$ , are strictly monotone. Then, the vector function F that enters the variational inequality (23) is strictly monotone, with respect to $( Q ^ { l } , Q ^ { 2 } , Q ^ { 3 } , \eta ^ { l } , \eta ^ { 2 } , \eta ^ { 3 } ,$ $\lambda , \rho ^ { 3 } )$ , that is, for any two $X ^ { \prime } , X ^ { \prime \prime }$ with $( Q ^ { \hat { l } \prime } , \ Q ^ { 2 \prime } , \ { \dot { Q } } ^ { \bar { 3 } \prime } , \ { \dot { \eta } } ^ { 1 \prime } , \ \eta ^ { 2 \prime } , \ \eta ^ { \dot { 3 } \prime } , \ { \dot { \lambda } } ^ { \prime } ,$ $\rho ^ { 3 } { ' } ) \neq ( Q ^ { 1 } { ' } ^ { \prime } , Q ^ { 2 } { ' } ^ { \prime } , Q ^ { 3 } { ' } ^ { \prime } , \eta ^ { 1 } { ' } ^ { \prime } , \eta ^ { 2 } { ' } ^ { \prime } , \eta ^ { 3 } { ' } ^ { \prime } , \lambda ^ { \prime \prime } , \rho _ { 3 } ^ { \prime \prime } )$

$$
\left\langle \left(F (X ^ {\prime}) - F (X ^ {\prime \prime})\right) ^ {T}, X ^ {\prime} - X ^ {\prime \prime} \right\rangle > 0.\tag{33}
$$

Theorem 7. (Uniqueness). Assuming the conditions of Theorem 6, there must be a unique shipment solution $( Q ^ { I * } , Q ^ { 2 * } , Q ^ { 3 * } , \eta ^ { \bar { I } * } , \eta ^ { 2 * } , \eta ^ { 3 * } , \lambda ^ { * } ,$ $\rho _ { 3 } ^ { * } ) ,$ , satisfying the equilibrium conditions of the supply chain. In other words, if the variational inequality (23) admits a solution, then that is the only solution in $( Q ^ { I } , Q ^ { 2 } , Q ^ { 3 } , \eta ^ { I } , \dot { \eta } ^ { 2 } , \eta ^ { 3 } , \lambda , \rho _ { 3 } )$

Proof. Under the strict monotonicity result of Theorem $6 ,$ uniqueness follows from the standard variational inequality theory (cf. [43]).

## 3.1. The algorithm

Here, an algorithm is presented that can be applied to solve any variational inequality problem in standard form (see Eq. (23)). The algorithm is guaranteed to converge provided that the function F(X) that enters the variational inequality is monotone and Lipschitz continuous (and that a solution exists). The algorithm is the modi<sup>fi</sup>ed projection method of Korpelevich [50] and it has been applied to solve a plethora of network equilibrium problems (see [58]).

We <sup>fi</sup>rst provide a de<sup>fi</sup>nition of a Lipschitz continuous function:

De<sup>fi</sup>nition 6. The function F(x) is Lipschitz continuous, if there exists a constant L>0 such that:

$$
\left| \left| F \left(X ^ {\prime}\right) - F \left(X ^ {\prime \prime}\right) \right| \right| \leq L \left| \left| X ^ {\prime} - X ^ {\prime \prime} \right| \right|, \quad \forall X ^ {\prime}, X ^ {\prime \prime} \in \mathcal {K}, \text {   with   } L > 0.\tag{34}
$$

The realization of the modi<sup>fi</sup>ed projection method for the variational inequality (23) is as follows.

Step 0: initialization step F

Set $( Q ^ { 1 0 } , Q ^ { 2 0 } , Q ^ { 3 0 } \eta ^ { 1 0 } , \eta ^ { 2 0 } , \lambda ^ { 0 } , \rho _ { 3 } ^ { 0 } ) \in \mathcal { K } .$ . Let τ=1, where τ is the iteration counter, and set a so that $\textstyle 0 < a \leq { \frac { 1 } { I } }$ , where L is the Lipschitz constant (cf. De<sup>fi</sup>nition 6) for the problem.

Step 1: computation step Compute $( \overline { { { \sf Q } } } ^ { 1  T } , \overline { { { \sf Q } } } ^ { 2 T } , \overline { { { \sf Q } } } ^ { 3 T } , \overline { { { \eta } } } ^ { 1 T } , \overline { { { \eta } } } ^ { 2 T } , \overline { { { \boldsymbol { \Lambda } } } } ^ { T } , \overline { { { \rho } } } _ { 3 } ^ { T } ) \in \kappa$ by solving the variational inequality subproblem:

$$
\left\langle \overline {{{X}}} ^ {\mathcal {T}} + \alpha F \left(X ^ {\mathcal {T} - 1}\right) - X ^ {\mathcal {T} - 1}, X - \overline {{{X}}} ^ {\mathcal {T}} \right\rangle \geq 0, \quad \forall X \in \mathcal {K}.\tag{35}
$$

Step 2: adaptation

Compute $( Q ^ { 1 \mathcal { T } } , Q ^ { 2 \mathcal { T } } , Q ^ { 3 \mathcal { T } } , \eta ^ { 1 \mathcal { T } } , \eta ^ { 2 \mathcal { T } } , \lambda ^ { \mathcal { T } } , \rho _ { 3 } ^ { \mathcal { T } } ) \in \mathcal { K }$ by solving the variational inequality subproblem:

$$
\left\langle X ^ {\mathcal {T}} + \alpha F \left(\overline {{X}} ^ {\mathcal {T}}\right) - X ^ {\mathcal {T} - 1}, X - X ^ {\mathcal {T}} \right\rangle \geq 0, \quad \forall X \in \mathcal {K}.\tag{36}
$$

If $\begin{array} { r } { | X ^ { T } - X ^ { T - 1 } | \leq \epsilon , } \end{array}$ ; with $\epsilon > 0 ,$ , a pre-speci<sup>fi</sup>ed tolerance, then stop; else, set $\tau = : \tau + 1$ , and go to Step 1.

The following theorem states the convergence result for the modi<sup>fi</sup>ed projection method and is due to Korpelevich [50].

Theorem 8. (Convergence). Assume that the function that enters the variational inequality (23) has at least one solution and is monotone (cf. Theorem 5) and Lipschitz continuous (cf. De<sup>fi</sup>nition 6).

Then the modified projection method described above converges to the solution of the variational inequality (23).

## 4. Numerical examples

In this section, we applied the modi<sup>fi</sup>ed projection method described in the preceding section to several numerical examples.

The convergence criterion utilized was that the absolute value of the product transactions, levels of social responsibility activities, and prices between two successive iterations differed by no more than 10<sup>−4</sup>.

We initialized the modi<sup>fi</sup>ed projection method as follows: all the initial product transactions and prices were set equal to 1. The levels of social responsibility activities were set equal to 0.

The purpose of these examples is to illustrate the effects of social responsibility activities on the supply chain network. Detailed descriptions of the speci<sup>fi</sup>c data for the examples are given below.

Example 1. The <sup>fi</sup>rst numerical example consisted of two manufacturers, two retailers, two demand markets, with only physical transactions between manufacturers and retailers and the retailers and demand markets. Electronic transactions were not allowed.

Hence, $I { = } 2 , J { = } 2 , K { = } 2 \operatorname { w i t h } l { = } 1$ . There was a single link from each top-tiered node to each middle-tiered node. There was a single link joining each of the two middle-tiered nodes with each bottom-tiered node.

The data for the <sup>fi</sup>rst example were constructed for easy interpretation purposes. We set the variance–covariance matrices associated with the risk functions to the identity matrices. For the sake of simplicity, we considered the possibility of the existence of levels of social responsibility activities only between the manufacturers and the retailers, and between the retailers and the demand markets. Please refer to Tables 1–6 for a compact exposition of the notation.

The production cost functions faced by the manufacturers were

$$
f ^ {i} (q _ {i}) = 2. 5 \left(\sum_ {j = i} ^ {2} q _ {i j l}\right) ^ {2}, \quad \text { for } \quad i = 1, 2.
$$

The transaction cost functions faced by the manufacturers associated with transacting with the retailers were given by:

$$
\begin{array}{c} c _ {i j l} \Big (q _ {i j l}, \eta_ {i j l} \Big) = \Big (0. 5 - 0. 4 \eta_ {i j l} \Big) \Big (q _ {i j l} \Big) ^ {2} + \Big (3. 5 - \eta_ {i j l} \Big) q _ {i j l}, \\ \text {for} i = 1, 2; j = 1, 2; l = 1 \end{array}
$$

The handling costs of the retailers were given by:

$$
c _ {j} \left(q _ {j}\right) = . 5 \left(\sum_ {i = 1} ^ {4} q _ {i j l}\right) ^ {2}, \quad \text { for } \quad j = 1, 2.
$$

The transaction costs of the retailers associated with transacting with the manufacturers were given by:

$$
\hat {c} _ {i j l} \left(q _ {i j l}, \eta_ {i j l}\right) = 1. 5 q _ {i j l} ^ {2} + 3 q _ {i j l}, \quad \text { for } \quad i = 1, 2; l = 1; j = 1, 2.
$$

The demand functions at the demand markets were:

$$
d _ {1} (\rho_ {3}) = - 2 \rho_ {3 1} - 1. 5 \rho_ {3 2} + 1 0 0 0, d _ {2} (\rho_ {3}) = - 2 \rho_ {3 2} - 1. 5 \rho_ {3 1} + 1 0 0 0,
$$

and the transaction costs between the retailers and the consumers at the demand markets were given by:

$$
c _ {j k l} \left(Q ^ {2}, Q ^ {3}, \eta^ {2}, \eta^ {3}\right) = \left(1 - \eta_ {j k l}\right) q _ {j k l} ^ {2} + 2 q _ {j k l}, \quad \text { for } \quad j = 1, 2; k = 1, 2; l = 1.
$$

The emission functions were as follows:

$$
e ^ {i} \Big (Q ^ {1}, Q ^ {2}, \eta^ {1}, \eta^ {2} \Big) = e _ {r} ^ {i} \sum_ {j = 1} ^ {2} \Big (q _ {i j 1} - 5 \eta_ {i j 1} \Big), \mathrm{for} i = 1, 2.
$$

$$
e ^ {j} \left(Q ^ {1}, Q ^ {3}, \eta^ {1}, \eta^ {3}\right) = e _ {r} ^ {j} \left(\sum_ {i = 1} ^ {2} \left(q _ {i j 1} - 5 \eta_ {i j 1}\right) + \sum_ {k = 1} ^ {2} \left(q _ {j k 1} - 5 \eta_ {j k 1}\right)\right),
$$

$$
\mathrm{for} j = 1, 2,
$$

where e<sup>i</sup> and e<sup>j</sup> are emissions rate for manufacturer il and retailer j respectively.

The social responsibility activities cost functions were:

$$
b _ {i j l} \big (\eta_ {i j l} \big) = 2 \eta_ {i j l}, \quad \mathrm{for} \quad i = 1, 2; j = 1, 2; l = 1,
$$

$$
b _ {j k l} \left(\eta_ {j k l}\right) = \eta_ {j k l}, \quad \text { for } \quad j = 1, 2; k = 1, 2; l = 1.
$$

All other functions were set equal to zero.

For the <sup>fi</sup>rst example we assumed that all the weights associated with the different criteria were set equal to one by all the decision makers. Hence, in this example, the manufacturers and the retailers assigned the same weight to pro<sup>fi</sup>t maximization, risk minimization, and emissions value minimization. In addition, all levels of social responsibility variables η were kept at 0, which can be interpreted as that none of the decision makers have a possibility to invest into activities that promote quality assurance, environmental preservation, and/or compliance.

The computational results are presented in Table 7. The total emissions generated by each manufacturer were 30.40 and for each retailer 60.80.

Example 2. In the second example, the data were as in Example 1 except for the following changes: all manufacturers and retailers were able to invest in the social responsibility activities. In other words variable η<sub>ijl</sub> and η<sub>jkl</sub> can now take any value from 0 to 1.

As a result all manufacturers and retailers decided to increase the level of social responsibility activities to their maximum values (see Table 7). The result in Table 7 shows an increase of the product ow between manufacturers and retailers and between retailers and demand markets. The total emissions generated by manufacturers were now equal to 22.22 and for retailers 44.44. This represents a 26% reduction in total emissions generated for each manufacturer and for each retailer.

As expected, environmentally conscious decision makers can reduce the total emissions generated while increasing the levels of productions and transactions.

Example 3. In the third example, the data was as in Example 2 except for the following changes: Manufacturer 1 is less social responsible than Manufacturer 2 and therefore risker. As a result (Table 7), the volumes of ow and the levels of social responsibility activities on the links from the Manufacturer 1 to Retailers 1 and 2 are smaller than those in Example 2 and those from Manufacturer 2.

Example 4. In the fourth example, the data were as in Example 2 except for the following changes: Retailer 2 is not known to be socially responsible. Therefore, the risk of dealing with Retailer 2 is very high. As a result, the volumes of ow to and from Retailer 2 are equal to zero (see Table 7). Under this condition, all manufacturers deal only with Retailer 1. Hence, environmentally conscious consumers could significantly reduce the environmental emissions through the economics and change the underlying decision-making behavior in the supply chain network by not buying environmental unfriendly products.

Solutions to Examples 1–4.

<table><tr><td>Variable</td><td>Example 1</td><td>Example 2</td><td>Example 3</td><td>Example 4</td></tr><tr><td colspan="5">Product transactions between manufacturers and retailers</td></tr><tr><td> $q_{111}$ </td><td>15.20</td><td>16.11</td><td>12.74</td><td>23.69</td></tr><tr><td> $q_{121}$ </td><td>15.20</td><td>16.11</td><td>12.74</td><td>0.0</td></tr><tr><td> $q_{211}$ </td><td>15.20</td><td>16.11</td><td>16.54</td><td>23.69</td></tr><tr><td> $q_{221}$ </td><td>15.20</td><td>16.11</td><td>16.54</td><td>0.0</td></tr><tr><td> $\eta_{111}$ </td><td>0</td><td>1</td><td>0.35</td><td>1</td></tr><tr><td> $\eta_{121}$ </td><td>0</td><td>1</td><td>0.35</td><td>0</td></tr><tr><td> $\eta_{211}$ </td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\eta_{221}$ </td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td colspan="5">Product transactions between retailers and demand markets</td></tr><tr><td> $q_{111}$ </td><td>15.20</td><td>16.11</td><td>14.64</td><td>23.69</td></tr><tr><td> $q_{121}$ </td><td>15.20</td><td>16.11</td><td>14.64</td><td>23.69</td></tr><tr><td> $q_{211}$ </td><td>15.20</td><td>16.11</td><td>14.64</td><td>0</td></tr><tr><td> $q_{221}$ </td><td>15.20</td><td>16.11</td><td>14.64</td><td>0</td></tr><tr><td> $\eta_{111}$ </td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\eta_{121}$ </td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\eta_{211}$ </td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $\eta_{221}$ </td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td colspan="5">Shadow prices at retailers</td></tr><tr><td> $\lambda_1$ </td><td>238.61</td><td>252.36</td><td>254.70</td><td>247.23</td></tr><tr><td> $\lambda_2$ </td><td>238.61</td><td>252.36</td><td>254.70</td><td>-8.70</td></tr><tr><td colspan="5">Prices at demand markets</td></tr><tr><td> $\rho_{31}$ </td><td>277.02</td><td>276.49</td><td>277.34</td><td>278.96</td></tr><tr><td> $\rho_{32}$ </td><td>277.02</td><td>276.49</td><td>277.34</td><td>278.96</td></tr></table>

The results in Table 7 are as expected. In other words, in today's world information economy if companies are not socially responsible, they may loss sales and their most important asset, their reputation [26]. These examples (although stylized) have been presented to show both the model and the computational procedure. Obviously, different input data and dimensions of the problems solved will affect the equilibrium product transaction, levels of social responsibility activities, and price patterns. One now has a powerful environmental decision-making tool with which to explore the effects of perturbations to the data as well as the effects of changes in the number of manufacturers, retailers, demand markets, and levels of risk and social responsibility activities.

## 5. Managerial insights

The key insight derived from our study is that CSR in supply chain should be viewed holistically. Each stage in the supply chain gives rise to its own effects, impacts, and opportunities for improvement, but effective CSR strategies require an analysis that encompasses the entire supply chain. It is important for any <sup>fi</sup>rm in the supply chain to take a network approach to the investment in CSR. The network approach would bene<sup>fi</sup>t all members of the network and require lower individual investment in CSR. Moreover, it can lead to programs of collaborative waste reduction, environmental innovation at the interface, costeffective environmental solutions, the rapid development and uptake of innovation in environmental technologies, and allows <sup>fi</sup>rms to better understand the environmental impact of their supply chains.

CSR improvements, in turn, can lead to economic bene<sup>fi</sup>ts for companies. One advantage is the reduction of excess inputs and wastes throughout the supply chain, thereby lowering costs and promoting sustainable development. Other bene<sup>fi</sup>ts include reducing accident risks and lowering emissions, each of which leads to lower costs in the long run. Environmental prudence throughout the supply chain lowers costs not only for the company, but also for customers and vendors. By reducing pollution, wastes and the overall production and logistics costs, CSR can also promote reduced costs and better products for the customers.

In conclusion, it is very important for managers to <sup>fi</sup>nd the optimal level of investment in CSR activities so that they can allocate the appropriate amount of resources to these activities over time.

Managers should treat their decision regarding CSR as they treat all their long term investment decisions. In the short run, the cost of CSR may seem high, however, this cost would be less in the long run compared to the cost of liability for pollution, non compliance with regulation, dangerous operations, use of hazardous raw materials, and production of hazardous waste, as well as health and safety issues. Moreover, these liabilities may cost companies their reputation [26], brand image, sales, access to markets and <sup>fi</sup>nancial investments [27].

## 6. Discussion

Decision support systems are pivotal to the success of the integration of CSR into supply chain network [17]. Companies need to design decision support systems [21,35] to automate and integrate the management of social responsibility programs into their supply chain in order to meet their social and environmental targets. These include managing social and environmental standards and regulation, managing information ows more ef<sup>fi</sup>ciently [52] and sharing best practices in CSR and supply chains.

The decision support model presented in this paper can aid companies to reevaluate their investment in CSR and commitment to transparency, communication and collaboration in order to create a sustainable multi agent supply chain network. It allows the decision makers to simulate different scenarios depending on how concerned (or not) they are about environmental issues, risk and CSR over all. The resulting network model helps the decision makers assess the impact of CSR activities on their key objectives, pro<sup>fi</sup>t, environment and risk. Moreover, it determines the equilibrium levels of social responsibility investment between the decision makers, as well as, the levels of product transactions and prices.

Note that our network model includes the possibility of electronic commerce via virtual links from manufacturers to demand markets, Fig. 1. Designing a sustainable electronic commerce, in particular, its environmental impact is an important issue in supply chain management. The decision support model present in this paper can facilitate the integration of CSR decision into supply chain management and the design of the logistics behind electronic commerce. Therefore, improving the supply chain cooperate social responsibility of <sup>fi</sup>rms would improve their social and environmental impacts of sourcing, packaging and distribution of the products sold through electronic commerce.

## 7. Summary and conclusions

In this paper, we have proposed a theoretically rigorous framework for the modeling, qualitative analysis, and computation of solutions to supply chain networks sustainability. We model the multicriteria decision-making behavior of the various decision makers, which includes the maximization of net pro<sup>fi</sup>t, the emission (waste) minimization, and the minimization of risk, in the presence of both business-to-business (B2B) and business-to-consumer (B2C) transactions. Unlike the earlier literature on supply chain network equilibrium problems (cf. [22,63,59]), the weights associated with the objectives were no longer assumed to be equal. In particular, we applied emission and risk-penalizing weights, which were variable and dependent on the value of the emission and risk objective in the value function associated with each manufacturer as well as with each retailer.

The network had three tiers of decision makers, consisting of: manufacturers, retailers, as well as consumers associated with the demand markets. We allowed for physical as well as electronic transactions between the decision makers in the network. The levels of social responsibility activities were allowed to affect not only risk and emission functions but also the transaction cost functions (by reducing them, in general) and did have associated costs. We modeled the network in equilibrium, in which the product transactions between the tiers as well as the levels of social responsibility activities coincide and established the variational inequality formulation of the governing equilibrium conditions. Finite-dimensional variational inequality theory was used to formulate the derived equilibrium conditions, and also to obtain convergence results for the proposed algorithmic scheme. Finally, numerical examples were presented to illustrate the model and computational procedure.

The results show that investment in social responsibility activities is capable of increasing pro<sup>fi</sup>t, reducing risk and environmental impacts. CSR can potentially decrease production inef<sup>fi</sup>ciencies, reduce cost and risk and at the same time allow companies to increase sales, increase access to capital, new markets, and brand recognition. As a result of lower cost, lower risk and increase in sales, companies are more pro<sup>fi</sup>table. However, we also expect that as the investment in CSR activities increases, the percentage increase of the return of investment will be smaller. In our model we try to determine the level of CSR activity that maximize pro<sup>fi</sup>t, minimize emission, and minimize risk.

Future research will include the extension of this framework to the international arena, the incorporation of other criteria, the introduction of dynamics, as well as empirical applications.

## Appendix A

The complete formulation of the optimality conditions of the manufacturers. Eq. (9) can be express as:

$$
\begin{array}{l} \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} \left[ \frac {\partial f _ {i} (q _ {i} ^ {*})}{\partial q _ {i j l}} + \frac {\partial c _ {i j l} (q _ {i j l} ^ {*} , \eta_ {i j l} ^ {*})}{\partial q _ {i j l}} + \omega_ {2 i} (e ^ {i *}) \frac {\partial e ^ {i *}}{\partial q _ {i j l}} + e ^ {i *} \frac {\partial \omega_ {2 i} (e ^ {i *})}{\partial q _ {i j l}} + \omega_ {3 i} (r ^ {i *}) \frac {\partial r ^ {i *}}{\partial q _ {i j l}} + r ^ {i *} \frac {\partial \omega_ {3 i} (r ^ {i *})}{\partial q _ {i j l}} - \rho_ {1 i j l} ^ {*} \right] \\ \times [ q _ {i j l} - q _ {i j l} ^ {*} ] + \sum_ {i = 1} ^ {I} \sum_ {k = 1} ^ {K} \left[ \frac {\partial f _ {i} (q _ {i} ^ {*})}{\partial q _ {i k}} + \frac {\partial c _ {i k} (q _ {i k} ^ {*} , \eta_ {i k} ^ {*})}{\partial q _ {i k}} + \omega_ {2 i} (e ^ {i *}) \frac {\partial e ^ {i *}}{\partial q _ {i k}} + e ^ {i *} \frac {\partial \omega_ {2 i} (e ^ {i *})}{\partial q _ {i k}} + \omega_ {3 i} (r ^ {i *}) \frac {\partial r ^ {i *}}{\partial q _ {i k}} + r ^ {i *} \frac {\partial \omega_ {3 i} (r ^ {i *})}{\partial q _ {i k}} - \rho_ {1 i k} ^ {*} \right] \\ \times [ q _ {i k} - q _ {i k} ^ {*} ] + \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {J} \sum_ {l = 1} ^ {2} \left[ \frac {\partial c _ {i j l} (q _ {i j l} ^ {*} , \eta_ {i j l} ^ {*})}{\partial \eta_ {i j l}} + \frac {\partial b _ {i j l} (\eta_ {i j l} ^ {*})}{\partial \eta_ {i j l}} + \omega_ {2 i} (e ^ {i *}) \frac {\partial e ^ {i *}}{\partial \eta_ {i j l}} + e ^ {i *} \frac {\partial \omega_ {2 i} (e ^ {i *})}{\partial \eta_ {i j l}} + \omega_ {3 i} (r ^ {i *}) \frac {\partial r ^ {i *}}{\partial \eta_ {i j l}} + r ^ {i *} \frac {\partial \omega_ {3 i} (r ^ {i *})}{\partial \eta_ {i j l}} \right] \\ \times [ \eta_ {i j l} - \eta_ {i j l} ^ {*} ] + \sum_ {i = 1} ^ {I} \sum_ {k = 1} ^ {K} \left[ \frac {\partial c _ {i k} (q _ {i k} ^ {*} , \eta_ {i k} ^ {*})}{\partial \eta_ {i k}} + \frac {\partial b _ {i k} (\eta_ {i k} ^ {*})}{\partial \eta_ {i k}} + \omega_ {2 i} (e ^ {i *}) \frac {\partial e ^ {i *}}{\partial \eta_ {i k}} + e ^ {i *} \frac {\partial \omega_ {2 i} (e ^ {i *})}{\partial \eta_ {i k}} + \omega_ {3 i} (r ^ {i *}) \frac {\partial r ^ {i *}}{\partial \eta_ {i k}} + r ^ {i *} \frac {\partial \omega_ {3 i} (r ^ {i *})}{\partial \eta_ {i k}} \right] \end{array}
$$

$$
\times \left[ \eta_ {i k} - \eta_ {i k} ^ {*} \right] \geq 0, \quad \forall \left(Q ^ {1}, Q ^ {2}, \eta^ {1}, \eta^ {2}\right) \in K ^ {1},
$$

where $e ^ { i ^ { * } } = e ^ { i } ( Q ^ { 1 ^ { * } } , Q ^ { 2 ^ { * } } , \eta ^ { 1 ^ { * } } , \eta ^ { 2 ^ { * } } )$ and $r ^ { i * } = r ^ { i } ( { Q ^ { 1 } } ^ { * } , { Q ^ { 2 } } ^ { * } , { \eta ^ { 1 } } ^ { * } , { \eta ^ { 2 } } ^ { * } )$

The complete formulation of the optimality conditions of the retailers. Eq. (17) can be express as:

$$
\begin{array} { l } \sum _ { i = 1 } ^ { I } \sum _ { j = 1 } ^ { J } \sum _ { l = 1 } ^ { 2 } \left[ \frac { \partial c _ { j } \left( q _ { j } ^ { * } \right) } { \partial q _ { i j l } } + \frac { \hat { \partial } c _ { i j l } \left( q _ { i j l } ^ { * } , \eta _ { i j l } ^ { * } \right) } { \partial q _ { i j l } } + \omega _ { 2 j } \left( e ^ { j * } \right) \frac { \partial e ^ { j * } } { \partial q _ { i j l } } + \frac { \partial \omega _ { 2 j } \left( e ^ { j * } \right) } { \partial q _ { i j l } } e ^ { j * } + \omega _ { 3 j } \left( r ^ { j * } \right) \frac { \partial r ^ { j * } } { \partial q _ { i j l } } + \frac { \partial \omega _ { 3 j } \left( r ^ { j * } \right) } { \partial q _ { i j l } } r ^ { j * } + \rho _ { 1 i j l } ^ { * } - \lambda _ { j } ^ { * } \right] \\ \times \left[ q _ { i j l } - q _ { i j l } ^ { * } \right] + \sum _ { j = 1 } ^ { J } \sum _ { k = 1 } ^ { K } \sum _ { l = 1 } ^ { 2 } \left[ \frac { \partial c _ { j k l } \left( q _ { j k l } ^ { * } , \eta _ { j k l } ^ { * } \right) } { \partial q _ { j k l } } + \omega _ { 2 j } \left( e ^ { j * } \right) \frac { \partial e ^ { j * } } { \partial q _ { j k l } } + \frac { \partial \omega _ { 2 j } \left( e ^ { j * } \right) } { \partial q _ { j k l } } e ^ { j * } + \omega _ { 3 j } \left( r ^ { j * } \right) \frac { \partial r ^ { j * } } { \partial q _ { j k l } } + \frac { \partial \omega _ { 3 j } \left( r ^ { j * } \right) } { \partial q _ { j k l } } r ^ { j * } - \rho _ { 2 j k l } ^ { * } + \lambda _ { j } ^ { * } \right] \\ \times \left[ q _ { j k l } - q _ { j k l } ^ { * } \right] + \sum _ { i = 1 } ^ { I } \sum _ { j = 1 } ^ { J } \sum _ { l = 1 } ^ { 2 } \left[ \frac { \partial \hat { c } _ { i j l } \left( q _ { i j l } ^ { * } , \eta _ { i j l } ^ { * } \right) } { \partial \eta _ { i j l } } + \omega _ { 2 j } \left( e ^ { j * } \right) \frac { \partial e ^ { j * } } { \partial \eta _ { i j l } } + \frac { \partial \omega _ { 2 j } \left( e ^ { j * } \right) } { \partial \eta _ { i j l } } e ^ { j * } + \omega _ { 3 j } \left( r ^ { j * } \right) \frac { \partial r ^ { j * } } { \partial \eta _ { i j l } } + \frac { \partial \omega _ { 3 j } \left( r ^ { j * } \right) } { \partial \eta _ { i j l } } r ^ { j * } + \frac { \partial   b _ { i j l } (   [   [   ]   ]   )   )}{\partial   [   [   ]   ]   ]} \\ \times \left[   [   [   ]   ]   ] - n _ { i j l} ^ {*}   ] + \sum _ { j = 1 } ^ { J }   \sum _ { k = 1 } ^ { K }   \sum _ { l = 1 } ^ { 2}   [   [   [   ]   ]   ] - n _ { i j l} ^ {*}   ] + n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] \\ \times   [   [   [   ]   ]   ] - n _ { i j l} ^ {*}   ] +    [   [   [   ]   ]   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - n _ { i j l} ^ {*}   ] - m a x t h r a g e d o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h r o f t h s u p p e c t i o n d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d e f f o w e d & ( Q ^ {- 1}, Q ^ {- 3}, N ^ {- 1}, N ^ {- 3}, L) \\ & ( Q ^ {- 1}, Q ^ {- 3}, N ^ {- 1}, N ^ {- 3}, L) \\ & ( Q ^ {- 1}, Q ^ {- 3}, N ^ {- 1}, N ^ {- 3}, L) \\ & ( Q ^ {- 1}, Q ^ {- 3}, N ^ {- 1}, N ^ {- 3}, L) \\ & ( Q ^ {- 1}, Q ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Q ^ {- 1}, Q ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Q ^ {- 1}, Q ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Q ^ {- 1}, Q ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Q ^ {- 1}, Z ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1}, N ^ {- 4}, L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1} , N ^ {- 4} , L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1} , N ^ {- 4} , L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1} , N ^ {- 4} , L) \\ & ( Z ^ {- 4}, Z ^ {- 4}, N ^ {- 1} , N ^ {- 4} , L) \\ & ( Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z , Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Y = X , Y = Y , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y = W , Y = X , Y = Y , Y = Z , Y =W , Y = X , Y = Y , Y =Z , Y = W , Y =X , Y =Y , Y =Z , Y = W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =X , Y =Y , Y =Z , Y =W , Y =Z , Y =Y , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Z , Y =Y ,Y =X ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y =Y ,Y =Z ,Y= X <   |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X| > |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|>, |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|> |X|>< |content_end|>
$$

where $e ^ { j * } = e ^ { j } ( { Q ^ { 1 } } ^ { * } , { Q ^ { 3 } } ^ { * } , { \eta ^ { 1 } } ^ { * } , { \eta ^ { 3 } } ^ { * } )$ and $r ^ { j \ast } = r ^ { j } ( Q ^ { 1 ^ { \ast } } , Q ^ { 1 ^ { \ast } } , \eta ^ { 1 ^ { \ast } } , \eta ^ { 3 ^ { \ast } } )$

## References

[1] E. Ballestero, C. Romero, A theorem connecting utility function optimization and compromise programming, Operations Research Letters 10 (1991) 421–427.

[2] S.A. Batterman, M. Amann, Targeted acid rain strategies including uncertainty Jounral of Environmental Management 32 (1991) 57–72.

[3] M.S. Bazaraa, H.D. Sherali, C.M. Shetty, Nonlinear Programming: Theory and Algorithms, John Wiley & Sons, New York, 1993.

[4] C.B. Bhattacharya, S. Sen, Does doing good always lead to doing better? Consumer reactions to corporate social responsibility, Journal of Marketing Research 28 (2001) 225–243.

[5] C.B. Bhattacharya, S. Sen, When, why, and how consumers respond to social initiatives, California Management Review 47 (1) (2004) 9–24.

[6] J.M. Bloemhof-Ruwaard, P. Beek, L. Hordijk, L.N. van Wassenhove, Interactions between operational research and environmental management, European Journal of Operational Research 85 (1995) 229–243.

[7] E.H. Bowman, A risk/return paradox for strategic management, Sloan Management Review 21 (3) (1980) 17–31.

[8] A.J. Buck de, E.M.T. Hendrix, H.B. Schoorlemmer, Analyzing production and environmental risks in arable farming systems: a mathematical approach, European Journal of Operational Research 119 (1999) 416–426.

[9] A.B. Carroll, A three-dimensional conceptual model of corporate social performance, Academy of Management Review 4 (4) (1979) 497–505.

[10] A.B. Carroll, The pyramid of corporate social responsibility: toward the moral management of organizational stakeholders, Business Horizons 34 (4) (1991) 39–48.

[11] A.B. Carroll, Corporate social responsibility, Business and Society 38 (3) (1999) 268–295.

[12] C.R. Carter, M. Dresner, Environmental purchasing and supply management: crossfunctional development of grounded theory, Journal of Supply Chain Management 37 (3) (2001) 12–27.

[13] C.R. Carter, M.M. Jennings, Social responsibility and supply chain relationships, Transportation Research Part E 38E (1) (2002) 37–52.

[14] C.R. Carter, M.M. Jennings, Logistics social responsibility: an integrative framework, Journal of Business Logistics 23 (1) (2002) 145–180.

[15] C.R. Carter, M.M. Jennings, The role of purchasing in corporate social responsibility: a structural equation analysis, Journal of Business Logistics 25 (1) (2004) 145–186.

[16] C.R. Carter, R.J. Auskalnis, C.L. Ketchum, Purchasing from minority business enterprises: key success factors, Journal of Supply Chain Management 35 (1) (1999) 28–32.

[17] B. Chae, D. Paradice, J.F. Courtney, C.J. Cagle, Incorporating an ethical perspective into problem formulation: implications for decision support systems design, Decision Support Systems 40 (2005) 197–212.

[18] E.U. Choo, W.C. Wedley, Optimal criterion weights in repetitive multicriteria decision-making, The Journal of the Operational Research Society 36 (1985) 983–992.

[19] E.U. Choo, B. Schoner, W.C. Wedley, Interpretation of criteria weights in multicriteria decision making, Computers & Industrial Engineering 37 (1999) 527–541

[20] R. Clift, L. Wright, Relationships between environmental impacts and added value along the supply chain, Technological Forecasting and Social Change 65 (2000) 281-295

[21] J.F. Courtney, Decision making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31 (2001) 17–38.

[22] J. Cruz, Dynamics of supply chain networks with corporate social responsibility through integrated environmental decision-making, European Journal of Opera tional Research 184 (3) (2008) 1005–1031.

[23] M. Delmas, A. Terlaak, A framework for analyzing environmental voluntary agreements, California Management Review 43 (3) (2002) 44–63.

[24] J. Dong, A. Nagurney, Bicriteria decision making and <sup>fi</sup>nancial equilibrium: a variational inequality perspective, Computational Economics 17 (2001) 29–42.

[25] M. Emmelhainz, R. Adams, The apparel industry response to “sweatshop” concerns: a review and analysis of codes of conduct, The Journal of Supply Chain Management 35 (3) (1999) 51–57.

[26] T. Fabian, Supply chain management in an era of social and environment accountability, Sustainable Development International 2 (2000) 27–30.

[27] S. Feldman, P. Soyka, P. Ameer, Does improving a <sup>fi</sup>rm's environmental management system and environmental performance result in a higher stock price? Journal of Investing 6 (4) (1997) 87–97.

[28] P.C. Fishburn, Utility Theory for Decision Making, John Wiley & Sons, New York, 1970.

[29] R. Florida, Lean and green: the move to environmentally conscious manufacturing, California Management Review 39 (1) (1996) 80–105.

[30] C.J. Fombrun, Corporate reputations as economic asset, in: E. Freeman, J.S. Harrison (Eds.), The Blackwell Handbook of Strategic Management, Blackwell Publishers, Oxford, 2001, pp. 289–312.

[31] C.J. Fombrun, The leadership challenge: building resilient corporate reputations, in: J.P. Doh, S.A. Stumpf (Eds.), Handbook on responsible leadership and governance in global business, Edward Elgar, Cheltenham, 2005, pp. 54–68.

[32] C.J. Fombrun, N.A. Gardberg, M.L. Barnett, Opportunity platforms and safety nets: corporate citizenship and reputational risk, Business and Society Review 105 (1) (2000) 85–106.

[33] D. Gabay, H. Moulin, On the uniqueness and stability of Nash equilibria in noncooperative games, in: A. Bensoussan, P. Kleindorfer, C.S. Tapiero (Eds.), Applied Stochastic Control in Econometrics and Management Science, North-Holland, Amsterdam, The Netherlands, 1980, pp. 271–294.

[34] C. Geffen, S. Rothenberg, Suppliers and environmental innovation: the automotive paint process, International Journal of Operations & Production Management 20 (2) (2000) 166–186.

[35] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a macro prediction market, Decision Support Systems 42 (2006) 1944–1958.

[36] J. Hall, Environmental supply chain dynamics, Journal of Cleaner Production 8 (2000) 455–471.

[37] P.J. Haynes, M.M. Helms, An ethical framework for purchasing decisions, Management Decision 29 (1) (1991) 35–38.

[38] B.W. Husted, Risk management, real options, and corporate social responsibility, Journal of Business Ethics 60 (2005) 175–183.

[39] M.E. Johnson, Learning from toys: lessons in managing supply chain risk from toy industry, California Management Review 43 (2001) 106–130

[40] U. Jüuttner, H. Peck, M. Christopher, Supply chain risk management: outlining and agenda for future research, International Journal of Logistics: Research and Applications 6 (2003) 197–210.

[41] M.H. Karwan, J. Spronk, J. Wallenius (Eds.), Essays in Decision Making: A Volume in Honor of Stanley Zionts, SV, Berlin, Germany, 1997.

[42] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Cambridge University Press, Cambridge, England, 1993.

[43] D. Kinderlehrer, G. Stampacchia, An Introduction to Variational Inequalities and their Application, Academic Press, New York, 1980.

[44] A. King, M. Lenox, Lean and green? An empirical examination of the relationship between lean production and environmental performance, Production and Operations Management 10 (3) (2001) 244–256.

[45] S. Kitazawa, J. Sarkis, The relationship between ISO 14001 and continuous source reduction programs, International Journal of Operations & Production Management 20 (2) (2000) 225–248.

[46] R.D. Klassen, Just-in-time manufacturing and pollution prevention generate mutual bene<sup>fi</sup>ts in the furniture industry, Interfaces 30 (3) (2000) 95–106.

[47] R.D. Klassen, C.P. McLaughlin, The impact of environmental management on <sup>fi</sup>rm performance, Management Science 42 (1996) 1199–1214.

[48] P.R. Kleindorfer, E.M. Snir, Environmental information in supply-chain design and coordination, in: D.J. Richards, B.R. Allenby, W.D. Compton (Eds.), Information Systems and the Environment, National Academy of Engineering, 2001, pp. 115–138.

[49] A. Kolk, R.V. Tudder, The effectiveness of self-regulation: corporate codes of conduct and child labour, European Management Journa 20 (3) (2002) 260–271.

[50] G.M. Korpelevich, The extragradient method for <sup>fi</sup>nding saddle points and other problems, Matekon 13 (1977) 35–49.

[51] R. Lamming, J. Hampson, The environment as a supply chain management issue, British Journal of Management 7 (1996) S45–S62

[52] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decision Support Systems 42 (2006) 1641–1656.

[53] Y.J. Ma, Z. Fan, L. Huang, A subjective and objective integrated approach to determine attribute weights, European Journal of Operational Research 112 (1999) 397–404.

[54] A. Marcus, D. Geffen, K. Sexton, Reinventing Environmental Regulation: Lessons from Project XL, RFF (Resources for the Future) Press, Washington, D.C, 2002.

[55] P.R. Murphy, R.F. Poist, Socially responsible logistics: an exploratory study Transportation Journal 41 (4) (2002) 2335.

[56] A. Nagurney, Network Economics: A Variational Inequality Approach, Kluwer Academic Publishers. Dordrecht, The Netherlands. 1999

[57] A. Nagurney, L. Zhao, Networks and variational inequalities in the formulation and computation of market disequilibria: the case of direct demand functions, Transportation Science 27 (1993) 4-15

[58] A. Nagurney, J. Dong, Supernetworks: Decision-Making for the Information Age, Edward Elgar Publishers, Cheltenham, England, 2002.

[59] A. Nagurney, F. Toyasaki, Supply chain supernetworks and environmental criteria, Transportation Research D 8 (2003) 185–213.

[60] A. Nagurney, K. Ke, Financial networks with intermediation: risk management with variable weights, European Journal of Operational Research 172 (2006) 40–63.

[61] A. Nagurney, J. Dong, P.L. Mokhtarian, Multicriteria network equilibrium modeling with variable weights for decision-making in the information age with applications to telecommuting and teleshopping, Journal of Economic Dynamics and Control 26 (2002) 1629–1650.

[62] A. Nagurney, J. Loo, J. Dong, D. Zhang, Supply chain networks and electronic commerce: a theoretical perspective, Netnomics 4 (2002) 187–220.

[63] A. Nagurney, J. Cruz, J. Dong, D. Zhang, Supply chain networks, electronic commerce, and supply side and demand side risk, European Journal of Operational Research 164 (2005) 120–142.

[64] J.F. Nash, Equilibrium points in n-person games, Proceedings of the National Academy of Sciences 36 (1950) 48–49

[65] J.F. Nash, Noncooperative games, Annals of Mathematics 54 (1951) 286–298.

[66] A. Norrman, U. Jansson, Ericssons proactive supply chain risk management approach after a serious sub-supplier accident, International Journal of Physical Distribution and Logistics Management 34 (2004) 434–456

[67] M. Orlitzky, J.D. Benjamin, Corporate social responsibility and <sup>fi</sup>rm risk: a metaanalytic review, Business and Society 40 (4) (2001) 369–396.

[68] C. Parker, The Open Corporation, Cambridge University Press, Cambridge, UK, 2002.

[69] M. Porter, C. van der Linde, Green and competitive, Harvard Business Review (1995) 149–163 (September–October)

[70] Z. Qio, T. Prato, F. McCamley, Evaluating environmental risks using safety-<sup>fi</sup>rst constraints, American Journal of Agricultural Economics 83 (2001) 402–413.

[71] B. Quinn, E-System manages inventory to reduce risk, Pollution Engineering 31 (1999) 27–28.

[72] M.A. Razzaque, T.P. Hwee, Ethics and purchasing dilemma: a Singaporean view, Journal of Business Ethics 35 (4) (2002) 307–326.

[73] P. Rivoli, Labor standards in the global economy: issues for investors, Journal of Business Ethics 43 (3) (2003) 223–232

[74] S. Roberts, Supply chain speci<sup>fi</sup>c? Understanding the patchy success of ethical sourcing initiatives, Journal of Business Ethics 44 (2/3) (2003) 159–170.

[75] S. Rothenberg, Knowledge content and worker participation in environmental management at NUMMI, Journal of Management Studies 40 (7) (2003) 1783–1802.

[76] S. Rothenberg, F. Pil, J. Maxwell, Lean, green and the quest for superior environmental performance, Production and Operations Management 10 (3) (2001) 228–243.

[77] D. Simpson, Greening Beyond the Firm: Improving Environmental Performance Through the Supply Relationship, 2004 http://www.nzsses.org.nz/Conference/ Session5/54%20Simpson.pdf.

[78] D.L. Spar, L.T. La Mure, The power of activism: assessing the impact of NGOs on global business, California Management Review 45 (2003) 78–101.

[79] D. Swindley, UK retailers and global responsibility, The Service Industries Journal 10 (3) (1990) 589–598.

[80] UNCTAD, World Investment Report, Foreign Direct Investment and the Challenge of Development, Geneva, 1999.

[81] UNSRID, Regulating Business Via Multi-Stakeholder Initiatives: A Preliminary Assessment in Voluntary Approaches to Corporate Responsibility: Readings and Resource Guide NGLS Geneva. 2002

[82] S.L. Wartick, P.L. Coghran, The evolution of the corporate social performance model. Academy of Management Review 10 (4)(1985) 758–769.

[83] M. Weber, K. Borcherding, Behavioral influences on weight judgements in multiattribute decision making, European Journal of Operational Research 67 (1993) 1–12.

[84] D.J. Wood, Corporate social performance revisited, Academy of Management Review 16 (4) (1991) 691–718.

[85] P.L. Yu, Multiple-Criteria Decision Making Concepts, Techniques, and Extensions, Plenum Press, New York, 1985

[86] G.Y. Yu, A multiple criteria approach to choosing an ef<sup>fi</sup>cient stock portfolio at the Helsinki Stock Exchange, Journal of Euro-Asian Management 3 (1997) 53–85.

[87] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, New York, 1982.

Jose M. Cruz is an Assistant Professor of Operations and Information Management at School of Business at the University of Connecticut. His present research interests are corporate social responsibility and complex decision-making on network systems with a speci<sup>fi</sup>c focus on global issues. He is especially interested in international <sup>fi</sup>nancial networks, global supply chain networks, social and knowledge networks, electronic commerce and risk management. He has a PhD in Management Science from the University of Massachusetts, Amherst.
