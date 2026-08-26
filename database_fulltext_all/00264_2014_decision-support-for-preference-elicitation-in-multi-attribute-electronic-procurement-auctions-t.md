---
otero_id: 264
otero_key: "D32P8SVD"
title: "Decision support for preference elicitation in multi-attribute electronic procurement auctions through an agent-based intermediary"
authors: "Na Yang; Xiuwu Liao; Wayne Wei Huang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for preference elicitation in multi-attribute electronic procurement auctions through an agent-based intermediary

Na Yang <sup>a</sup>, Xiuwu Liao <sup>a,</sup>⁎, Wayne Wei Huang

<sup>a</sup> School of Management, The Key Lab of the Ministry of Education for Process Control & Efficiency Engineering, Xi'an Jiaotong University, Xi'an, PR China <sup>b</sup> Department of Management Information Systems, College of Business, Ohio University, Athens, OH, United States

## a r t i c l e i n f o

Article history: Received 18 July 2012 Received in revised form 5 April 2013 Accepted 20 August 2013 Available online 29 August 2013

Keywords: Electronic procurement Multi-criteria decision making Preference elicitation Disaggregation approach

## a b s t r a c t

Multi-attribute auctions have become increasingly popular in enterprise procurement. In the auctions, the elicitation of the preference of an auctioneer concerning multiple attributes is a central task in determining the winner(s). Considering the dif<sup>fi</sup>culty of explicit elicitation, a preference elicitation framework is proposed to assist the auctioneer in inferring his/her underlying preference model(s). The auctioneer is expected to provide the information of attribute weights, the holistic preference relations concerning a set of reference bids and the comparison information of intensities of preferences between some pairs of bids on all attributes and/or a particular attribute. Based on this information, a linear programming model is constructed to infer the preference model(s) of the auctioneer so that the estimations are as consistent as possible with the given preference statements. Furthermore, a method is also given to select a representative preference model from the set of compatible ones. The framework is implemented by an intelligent buyer agent called e-buyer which has <sup>fi</sup>ve main components, i.e., a semantic analyzer, a preference elicitation module, a bid evaluation module, a model base, and a database. The e-buyer is embedded into an auction intermediary, and the proposed preference elicitation models are stored in the model base. Several graphical user interfaces are also presented to visualize the future trading intermediaries. Finally, a numerical example is given to illustrate the framework and show the effectiveness of the preference elicitation models

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Given the remarkably rapid progress of internet technology and electronic commerce over the past decade, online auctions have become very popular venues for conducting business transactions [2,32]. In the business-to-business (B2B) domain in particular, the utilization of information technologies enables <sup>fi</sup>rms to employ a new tool, i.e., electronic procurement (e-procurement) auctions (also referred to as electronic reverse auctions) to increase the ef<sup>fi</sup>ciency of their procurement. For example, Procter & Gamble employed this new tool to conduct auctions for its suppliers. By March 2005, over a period of two and a half years, the company sourced over \$3 billion worth of supplies, with up to \$294.8 million (9.6%) saved because of advanced technologies [35]. Similarly, Motorola implemented an end-to-end internet sourcing platform by Emptoris in 2002. Motorola's sourcing of materials and services had reached \$16 billion by 2005, and savings amounted to \$600 million [29].

As extensively reported in the literature (e.g., [19,34,44,45]), cost savings always accompany the employment of e-procurement auctions. Generally, 10% to 40% of the negotiation and contracting costs could be saved through online bidding [19]. The reduction in cycle time that can be attributed to e-procurement auctions is another bene<sup>fi</sup>t that enables industrial buyers to improve their sourcing ef<sup>fi</sup>ciency. The entire negotiation process may last for several months in a traditional procurement event. By contrast, the duration of e-sourcing can be shortened to several weeks or even a couple of hours [35,45]. Moreover, suppliers can also bene<sup>fi</sup>t from the new mechanism in terms of an alternative distribution channel. A number of large industrial <sup>fi</sup>rms, such as Hewlett-Packard, Dell, General Electric, etc., have recently employed e-procurement auctions to purchase direct and indirect materials. With billions of dollars of transaction contracts being awarded every year, this <sup>fi</sup>eld continues to <sup>fl</sup>ourish.

In a Web-based procurement auction, a single buyer (auctioneer) procures items (goods or services) from numerous potential sellers (bidders), and the transaction usually occurs through an electronic auction (e-auction) intermediary operated by a third-party organization or by the buyer himself/herself. Each participator has to register with the intermediary and then apply for customer identi<sup>fi</sup>cation to gain access to the system. Auctions are then conducted by software agents that negotiate on behalf of the buyer and the suppliers. The entire procedure can be brie<sup>fl</sup>y described as follows: First, the buyer, as the leader in the procurement auction, speci<sup>fi</sup>es the requirements for the item to be purchased and the quali<sup>fi</sup>cation for the suppliers. Second, the trading intermediary generates the Request for Quotes and sends it to a number of quali<sup>fi</sup>ed suppliers. Third, seller agents help compose bids, and each bidder then submits a bid through the graphical user interface (GUI) before the deadline. Fourth, the trading intermediary determines a winning bid (or several winning bids) according to the pre-de<sup>fi</sup>ned scoring rule of the buyer and then prepares the corresponding procurement contract(s). Finally, the winning supplier(s) makes the actual delivery.

In the early development stages, almost all the procurement auctions were conducted in a simple descending price format. However, the price-only focus signi<sup>fi</sup>cantly limited the potential use of procurement auctions in practical applications, particularly in industries where suppliers varied considerably in terms of non-price dimensions, such as quality, brand, terms of warranty, etc. Consequently, a number of researchers began to consider auction mechanisms that would enable a buyer to negotiate with multiple suppliers over heterogeneous goods or services. In the literature, several terminologies have been used to describe such a procurement auction format, i.e., multi-dimensional [7,9,10,12], multi-issue [40,42], multicriteria [5,17], and multi-attribute auctions [6,36], where the most commonly used is “multi-attribute auctions.” Che <sup>fi</sup>rst proposed a two-dimensional (i.e., price and quality) auction for government procurement [12]. Branco extended the previous model by considering the correlation among the cost functions of sellers [10]. Subsequently, the domain was extensively studied by numerous scholars from different disciplines, such as economics [16,30,33], information systems [1,14,28,38], operation research, computer science, etc.

The winner determination problem (WDP) is a major concern in multi-attribute procurement auctions. Many scholars used scoring functions in their study to evaluate the bids submitted by bidders. However, it is usually dif<sup>fi</sup>cult for an auctioneer to give precisely all parameter values of the scoring function in practical implementation because of his/her cognitive limitation. Therefore, we propose a new preference elicitation framework, which is based on the aggregationdisaggregation paradigm [37], to assist the auctioneer in inferring his/her underlying preference model(s) from the preference information provided by himself/herself. The preference information can be either direct or indirect, depending whether the auctioneer speci<sup>fi</sup>es directly values of some parameters used in the preference model or whether he/she speci<sup>fi</sup>es some examples of holistic judgments from which compatible values of the parameters are induced [21]. Four types of information are expected to provide in the proposed framework, namely the information of attribute weights, the holistic preference relations concerning a set of reference bids and the comparison information of intensities of preferences between some pairs of reference bids on all attributes and/or a particular attri bute. The information of weights is direct, whereas the others are indirect. The reference bids can generally be derived from several sources as follows: (a) A set of <sup>fi</sup>ctitious actions, which should be easily judged by the auctioneer to express his/her preference [23]; (b) A subset of real commodities available in the current trading market. The items with different speci<sup>fi</sup>cations are actually potential choices for procurement in auctions; (c) The tentative bids from a pre-bidding stage. A pre-bidding stage can be designed before the formal negotiation process, and some tentative bids from potential suppliers then can be collected and utilized as reference bids; (d) Some historical bids stored in e-auction intermediaries. In the B2B domain, the industrial buyer always purchases the same item repetitively. Thus, a large amount of historical transaction data may help determine preference. The last of the abovementioned sources is quite suitable for Web-based transactions; therefore, the historical data are considered the primary source of reference bids in this study. Based on the information provided by the auctioneer, a linear programming model is constructed to infer the preference model(s) of the auctioneer so that the estimations are as consistent as possible with the given preference statements. Furthermore, a method is also given to select a representative preference model from the set of compatibles ones. An intelligent buyer agent is designed to implement the framework. It is comprised of <sup>fi</sup>ve functional components, i.e., a semantic analyzer, a preference elicitation module, a bid evaluation module, a model base, and a database. The buyer agent is embedded into an auction intermediary.

Some contributions of this paper are summarized as follows. (1) To the best of our knowledge, only Karakaya and Köksalan have studied the indirect preference elicitation in the <sup>fi</sup>eld of auctions [25]. In their setting an auctioneer is required to choose the most preferred bid(s) in each round so that his/her nonlinear utility function can be estimated from the information, while our framework uses the additive value function and requests an auctioneer to provide the four types of information mentioned above for inferring such a function. Moreover, we also give a reference ranking of the bids in each round to assist the auctioneer in submitting new preference information, which is not mentioned in [25]. (2) Like the traditional UTA method, our preference elicitation method also adopts the aggregation–disaggregation paradigm, and uses linear programming techniques to infer preference models which are as consistent as possible with the given information. It estimates the parameters by minimizing the maximum error, not the total error as in UTA. In case of a non-empty set of compatible value functions, traditional UTA method and one of its variants UTASTAR select a mean value function by conducting so-called post-optimality analysis [37], whereas our method aims at determining a representative function which emphasizes the advantages of some bids over the others if the auctioneer prefers the former ones, highlights the differences of intensities of preference among pairs of bids if the auctioneer assigns them with different degrees, and reduces the differences among pairs of bids with the same degree. (3) Prior research on solving WDPs or on eliciting preference of an auctioneer has seldom addressed the implementations of the proposed methods. In this article, an intelligent buyer agent is designed to implement the framework, and thus promotes the practical use of the proposed framework in real-world commerce.

The remainder of this paper is organized as follows. In Section 2, we discuss the related literature. In Section 3, we propose a preference elicitation framework for multi-round, multi-attribute e-procurement auctions, and devise the architecture of an intelligent buyer agent to implement the framework. Section 4 is devoted to the underlying decision-making approach, including the required preference information and the models used to estimate the preference. Several GUIs are presented to depict our vision of how the preference information is obtained in an e-auction intermediary. We then exemplify the use of the framework and present the theoretical comparisons in Section 5. Finally, in Section 6, we conclude with the contributions of the paper and give some suggestions for future research.

## 2. Literature review

Two streams of literature are closely related to this work. The <sup>fi</sup>rst stream is the study of winner determination problems in multiattribute auctions. There is a large body of literature devoted to this <sup>fi</sup>eld [3,8,13,15,24,39]. The WDPs have been studied under various situations. Cheng presents a multi-attribute decision-making model for solving the WDP in sealed-bid reverse auction setting [15]. Beil and Wein study the determination of winner(s) in a multiround open-ascending auction mechanism [4]. They use an inverse optimization technique to learn the suppliers' cost functions from their bids, and then optimize the scoring rule which maximizes the auctioneer's utility to determine the winner. Bichler and Kalagnanam focus on the case that the total demand can be purchased from multiple suppliers (i.e., multiple sourcing) and the suppliers are allowed to submit con<sup>fi</sup>gurable offers [8]. Kameshwaran et al. analyze the WDPs in case of large-volume procurements with quantity discounts and business constraints [24]. Chen et al. consider the situation that the chosen supplier fails to accomplish the project, and they take into account a penalty payment in determining winner(s) [13]. In most of the above literature, a scoring rule is essential in evaluating the bids submitted by bidders, such as a weighted-sum value function in [8], a quasi-linear scoring function in [13], etc. However, the construction of such a scoring function has been scarcely studied.

The elicitation of an auctioneer's preference is a central task in constructing an appropriate scoring function, and correspondingly in solving WDPs [8,42]. Several approaches have been proposed to represent an auctioneer's preference over multiple attributes. Teich et al. suggest using an “auction owner speci<sup>fi</sup>ed path” method [40]. Bichler explicitly elicits an auctioneer's value function over multiple attributes [7]. Another approach is called “price out”, which converts all attributes, except for price and quantity, into monetary values [41,43]. Although the idea seems straightforward, the tasks of assessments are dif<sup>fi</sup>cult for an auctioneer because of his/her cognitive limitation. Furthermore, the capability of an arbitrarily determined scoring function to represent the true preference of the auctioneer may be questionable. As a response to the dif<sup>fi</sup>culty in explicit elicitation, indirect preference elicitation has emerged as an important research direction. To the best of our knowledge, only Karakaya and Köksalan have studied the indirect preference elicitation in auction <sup>fi</sup>eld. They develop an interactive approach for a multi-attribute, single-item, multi-round procurement auction mechanism. In their setting, the buyer is required to choose the most preferred bid(s) in each round so that the preference function can be estimated from it [25].

The second stream of work related to ours is the study of disaggregation paradigm in multi-criteria decision making (MCDM). “The philosophy of preference disaggregation in multicriteria analysis is to assess/ infer preference models from the given preferential structures” [23]. Ordinal regression techniques are typically used in the paradigm to induce compatible values of the preference model parameters from some reference examples based on a set of reference actions. Eliciting indirect preference demands less cognitive effort, hence, the paradigm has become increasingly popular. Several disaggregation methods have been proposed. UTA is the most representative example. It uses linear programming techniques to infer additive value functions so that the estimations are as consistent as possible with the given ranking on the reference set [37]. The method is then generalized by a new method called $\mathrm { U T A } ^ { \mathrm { G M \dot { S } } }$ in three aspects: the preference relations have the form of a partial preorder on a subset of reference alternatives, all compatible additive value functions are taken into account, and general non-decreasing marginal value functions instead of piecewise linear ones are considered [21]. Recently, GRIP further generalizes both two methods. It adopts all the features of UTA<sup>GMS</sup> and introduces additional preference information in the form of comparisons of intensities of preferences for pairs of bids on all attributes and/or a particular attribute [20].

Additionally, studies on decision support systems are also related to our work. The complexities associated with determining winner(s) in multi-attribute e-procurement auctions require the use of advanced decision support systems that enable an auctioneer to process multidimensional information. Talluri et al. have developed a decision support tool that utilizes a combination of data envelopment analysis and integer programming to assist buyers in determining winner(s) in a multi-sourcing, multi-attribute e-reverse auction [39]. Nevertheless, most studies on online auction systems remain focused on price-only auctions [11,22,27].

## 3. Preference elicitation framework

As Pekeč and Rothkopf state, iterative auctions are predominant in e-business [31]. The iterative format has several advantages. On one hand, it enables bidders to learn about their rivals' valuations and the auctioneer's preference through the bidding process, which may help them update their bids to be competitive in the next round; On the other hand, unlike one-shot auctions that require bidders to submit all bids only once, iterative ones enable bidders to submit a small number of bids in each round, thereby reducing the bid submission burden. Similarly, the WDP algorithm is conducted once in each round, thereby reducing the computation burden of the entire negotiation process. Thus we develop the preference elicitation framework based on such an auction format. The framework refers to the entire procedure including gathering the preference information, analyzing it, inferring the preference models, and interacting with the auctioneers. An intelligent buyer agent is designed to implement the framework. We use “human buyer” and “e-buyer” to distinguish between an auctioneer and his/her software agent. The architecture of the e-buyer is shown in Fig. 1.

An intelligent e-buyer consists of <sup>fi</sup>ve main components: a semantic analyzer, a preference elicitation module, a bid evaluation module, a model base, and a database. At the beginning of an auction, the human buyer is requested to provide a set of preference information. All the information is then analyzed by the semantic analyzer and subsequently converted into computer languages. The preference elicitation and bid evaluation modules are the core components; both play vital roles in implementing the decision support functionality of the e-buyer. Given some pre-speci<sup>fi</sup>ed algorithms stored in the model base, the preference elicitation module can infer the preference function of the human buyer from the inputs, and the function is then utilized by the bid evaluation module as a scoring rule to evaluate the bids submitted in each round. The newly obtained preference relations are then recorded in the database. Meanwhile, the human buyer and all seller agents are noti<sup>fi</sup>ed of the ranking of the bids and of the provisional winning bid(s), respectively. Based on these outputs, seller agents update their valuations, and the human buyer veri<sup>fi</sup>es whether the evaluations of the bids are consistent with his/her underlying preference. In the next round, the human buyer is allowed to provide some feedback to further re<sup>fi</sup>ne the estimated preference function. The auction <sup>fl</sup>ow diagram shown in Fig. 2 illustrates how the iterative auctions are conducted given the proposed elicitation framework. A test stage is designed in the auction process to test the performance of the estimation. Notice that every newly obtained function should be checked for I rounds, where I is a default value speci<sup>fi</sup>ed by the system and can be reset by human buyers. The auction process is summarized in Table 1.

## 4. Underlying decision-making method

The underlying method that infers the preference model of an auctioneer is presented in this section. Section 4.1 brie<sup>fl</sup>y describes the problem and introduces some main notations. In Section 4.2, we explain several types of preference information considered in the proposed framework and then present several GUIs to visualize the interactive e-auction intermediary. Mathematical programming models are developed in Section 4.3 to infer the preference model(s) that restores the information set provided by the auctioneer.

## 4.1. Problem statement and the main notation

The following notations apply to help describe the problem of preference elicitation:

## Notation

$G$ set of attributes, $\mathsf { G } = \{ g _ { 1 } , . . . , g _ { n } \}$ with $g _ { j } \in G$

$w _ { j }$ weight of attribute g<sub>j</sub>

$B ^ { t }$ set of bids submitted by all bidders in round t

$b _ { s } ^ { t }$ bid submitted by the bidder s in round $t , b _ { s } { ^ t } \in { \boldsymbol { B } } ^ { t }$

$B _ { r } ^ { t }$ set of reference bids in round $t , B _ { r } ^ { \ t } \subseteq B _ { r } ^ { \ t - 1 } \cup B ^ { t }$ with $ { b _ { i } } \in  { B _ { r } } ^ { t }$

$D _ { j }$ evaluation scale of attribute g<sub>j</sub>

$D$ bidding space for potential bidders, $\begin{array} { r } { D = \prod _ { j = 1 } ^ { n } D _ { j } } \end{array}$

$g _ { j } ( b _ { i } )$ evaluation of bid b on attribute $g _ { j } , g _ { j } ( b _ { i } ) \in D _ { j }$

$v _ { j } ( g _ { j } ( b _ { i } ) )$ marginal value of bid $b _ { i }$ on attribute $g _ { j } ,$ also denoted as $\nu _ { j } ( b _ { i } )$

![](/api/attachments/D32P8SVD/fulltext/images/e1947761b831c8c4005e85e6e24481474712b95b386d7b8bc0ca3e43fac6ad11.jpg)  
Fig. 1. Overall architecture of the intelligent e-buyer.

$V ( b _ { i } )$ global value of bid $b _ { i }$

$g _ { j ^ { * } }$ the least preferred evaluation prescribed by the auctioneer for attribute $g _ { j }$

${ g _ { j } } ^ { * }$ the most preferred evaluation prescribed by the auctioneer for attribute $g _ { j }$

$\alpha _ { j }$ number of characteristic points of attribute g<sub>j</sub> $\begin{array} { l } { { g _ { j } ^ { \ l } } ^ { l } } \\ { { \nu _ { j } } \left( g _ { j } ^ { \ l } \right) } \\ { I n f { \hat { o } ^ { t } } ^ { l } } \end{array}$ the lth least preferred characteristic point of attribute $g _ { j }$ marginal value with respect to ${ g _ { j } } ^ { l } ,$ , also denoted as $\nu _ { j } { } ^ { l }$ information set in round t

$A d d ^ { t }$ information set newly provided in round t

$R e { \nu } ^ { t }$ information set revised in round $t , \mathsf { R e v } ^ { t } \subset I n f o ^ { t - 1 }$

$V ^ { t }$ preference model inferred in round t

![](/api/attachments/D32P8SVD/fulltext/images/31dee462e83c68816e2682aa414920311bbdc3ebd6d491feef7a4561563f2000.jpg)  
Fig. 2. Auction <sup>fl</sup>ow diagram.

Negotiation process with the proposed framework

<table><tr><td>Negotiation process</td><td>Description</td></tr><tr><td>Step 1</td><td>The auctioneer initiates a multi-attribute procurement auction, which mainly includes defining a set of attributes and prescribing the bidding space. The round counter is set at  $t = 0$ </td></tr><tr><td>Step 2</td><td>The auctioneer submits an initial set of reference bids and provides some preference statements to express his/her actual evaluation of the bids. Details of the preference statements are discussed further in Section 4.2</td></tr><tr><td>Step 3</td><td>The semantic analyzer processes all inputs. It translates the semantic expressions into computer languages</td></tr><tr><td>Step 4</td><td>Using the preference elicitation algorithms (the details are explained in Section 4.3), the preference elicitation module is implemented to infer the preference model of the auctioneer from his/her preference statements. The test counter is reset at  $k = 1$ </td></tr><tr><td>Step 5</td><td>If the stopping rule of the auction has been met, the entire negotiation process ends; otherwise, Step 6 is executed</td></tr><tr><td>Step 6</td><td>The auction proceeds to the next round, i.e.,  $t = t + 1$ . Bidders place new bids according to the current provisional winning bid(s). Some bidders may remain in the auction, whereas others may quit</td></tr><tr><td>Step 7</td><td>All the bids submitted in round  $t$  are assessed using the current scoring rule, i.e., the preference model estimated in the last round. The auctioneer is then informed of the complete preorder, and the bidders are informed of the provisional winning bid(s)</td></tr><tr><td>Step 8</td><td>If  $k < I$ , which means that the estimated preference model should be further tested, Step 9 is executed; otherwise, the process is repeated from Step 5</td></tr><tr><td>Step 9</td><td>The auctioneer is asked whether he/she agrees with the ranking of the bids. If the results are deemed satisfactory, Step 10 is executed; otherwise, Step 11 is executed</td></tr><tr><td>Step 10</td><td> $k = k + 1$ , i.e., the estimated preference model is accepted by the human buyer temporarily; thus, the test stage proceeds to the next round. The process is then repeated from Step 5</td></tr><tr><td>Step 11</td><td>The auctioneer can revise some unacceptable preference relations, add new information, or delete controversial information to constitute a new information set for the subsequent time inference. Then, Step 3 is repeated</td></tr></table>

In multi-attribute e-procurement auctions, the auctioneer evaluates the offers submitted by bidders based on a family of attributes G. Without loss of generality, we assume that the greater $g _ { j } ( b _ { i } )$ , the better bid $b _ { i }$ on attribute $g _ { j }$ for all $j = 1 , . . . , n .$ . The actual preference model of the auctioneer is used as the scoring rule to determine a winner. We assume the preference model adopted in this study is an additive value function. Such model is the most important decision model within multi-attribute utility theory (MAUT) [21] and is commonly used in studies on multi-attribute auctions (e.g. [8,36]). The function is expressed in the following form:

$$
V (b _ {i}) = \sum_ {j = 1} ^ {n} v _ {j} \left(g _ {j} (b _ {i})\right)
$$

subject to normalization constraints:

$$
\left\{ \begin{array}{l} v _ {j} \Big (g _ {j *} \Big) = 0 \qquad \forall j = 1,..., n \\ \sum_ {j = 1} ^ {n} v _ {j} \Big (g _ {j} ^ {*} \Big) = 1 \end{array} \right.,\tag{1}
$$

Hereafter, we use $\nu _ { j } ( b _ { i } )$ instead of $v _ { j } ( g _ { j } ( b _ { i } ) )$ to simplify notation. An alternative way of representing the same preference model is in the form of a weighted-sum value function as follows:

V b<sub>i</sub>  <sup>Xn</sup> w <sub>j</sub> v <sub>j</sub> b<sub>i</sub> ; where $\widehat { \nu } _ { j } \Big ( g _ { j * } \Big ) = 0 , \widehat { \nu } _ { j } \Big ( g _ { j } ^ { * } \Big ) = 1 , w _ { j } \mathop { \geq } 0$ for all $j = 1 , . . . , n ,$ ; and $\sum _ { j = 1 } ^ { n } w _ { j } = 1$ 1 and 2 are equal if $w _ { j } = { \nu _ { j } } { \left( { { g _ { j } } ^ { * } } \right) } , j = 1 , . . . , n$

2

In the proposed framework, the preference model is inferred from a set of preference information provided by the auctioneer. The auctioneer is requested to provide a set of reference bids $B _ { r } { } ^ { 0 }$ and information $I n f { \hat { o } } ^ { \hat { 0 } }$ in the initial stage, and he/she is allowed to enrich the information during the auction process in an incremental way such that ${ B _ { r } } ^ { t } \subseteq { B _ { r } } ^ { t - 1 } \{$ ∪B<sup>t</sup> and $I n f o ^ { t } = ( I n f o ^ { t - 1 } \backslash { \mathsf { R e } } \nu ^ { t } ) \cup A d d ^ { t } .$ . Thus, the preference model V<sup>t</sup> can be inferred gradually to represent the auctioneer's underlying preference. Speci<sup>fi</sup>cally, a set of values $\nu _ { j } \left( g _ { j } ^ { \ l } \right)$ (hereafter $\nu _ { j } { } ^ { l } )$ for all $j = 1 , . . . ,$ n and $l = 1 , . . . , \alpha _ { j }$ are estimated to achieve V<sup>t</sup>. For qualitative attributes (e.g., warranty years and color) with discrete evaluations, $\alpha _ { j }$ denotes the number of evaluations and $g _ { j } ^ { \ l } \ , \ l = 1 , . . . , \alpha _ { j }$ represents the lth least preferred evaluation. For quantitative attributes (e.g., price) with continuous values, we select α characteristic points for each attribute g by dividing $D _ { j }$ into $\alpha _ { j } – 1$ equal sub-intervals such that there is at least one reference bid belonging into each interval [18,37]. The breakpoints are computed by the formulas:

$$
g _ {j} ^ {l} = g _ {j *} + (l - 1) \cdot \left(g _ {j} ^ {*} - g _ {j *}\right) / (\alpha_ {j} - 1) \forall j = 1, \dots , n, l = 1, \dots , \alpha_ {j}\tag{3}
$$

Thus the marginal value function $\nu _ { j } ( \cdot )$ is de<sup>fi</sup>ned by the values at the characteristic points. Marginal values $v _ { j } ( b _ { i } )$ for such quantitative attributes $g _ { j } \in G$ are approximated by a piecewise linear modeling approach.

$$
\begin{array}{l} v _ {j} (b _ {i}) = v _ {j} ^ {l} + \left(v _ {j} ^ {l + 1} - v _ {j} ^ {l}\right) \\ \quad \cdot \left(g _ {j} (b _ {i}) - g _ {j} ^ {l}\right) / \left(g _ {j} ^ {l + 1} - g _ {j} ^ {l}\right), \text { for } g _ {j} (b _ {i}) \in \left[ g _ {j} ^ {l}, g _ {j} ^ {l + 1} \right] \end{array}\tag{4}
$$

## 4.2. Preference information in the framework

Four types of preference information are considered in our approach.

## I. Information of attribute weights

Despite dif<sup>fi</sup>culty in determining the precise weights, the auctioneer may be able to provide incomplete information on them. $C = \{ w \in W \}$ $A w \geq h \}$ is de<sup>fi</sup>ned as the set of vectors of weights satisfying linear inequalities in the form of $A w \geq h$ , where $A = [ a _ { i j } ] _ { m \times n } , m$ denotes the number of constraints on the vectors of weights, $\bar { h } = [ h _ { 1 } , \cdots , h _ { m } ] ^ { \mathrm { T } } \in R ^ { m }$ and $W = \{ w _ { j } | w _ { j } > 0$ for all $j = 1 , . . . , n , \sum _ { j } ^ { n } = _ { 1 } w _ { j } = 1 \}$ . Generally, <sup>fi</sup>ve common forms of linear inequalities included in C are [26]: for j ≠ j', (1) A weak ranking: $\lbrace w _ { j } \geq w _ { j } \rbrace ; \ ( 2 )$ A strict ranking: $\{ w _ { j } - w _ { j ^ { \prime } } \geq \gamma \} , \gamma > 0 ; ( 3 )$ A ranking of differences: $\{ w _ { j } - w _ { j } \} \ge w _ { h } -$ w }, for $j ^ { \prime } \neq h \neq h ^ { \prime } ; ( 4 )$ A ranking with multiples: $\{ \dot { w } _ { j } \ge \lambda w _ { j } \}$ $0 \leq \lambda \leq 1 ; ( 5 )$ An interval form: $\{ \beta _ { j } { } ^ { - } \leq w _ { j } \leq \beta _ { j } { } ^ { + } \} , 0 \leq \beta _ { j } { } ^ { - } \leq \bar { \beta } _ { j } { } ^ { + } \leq 1$

## II. Holistic preference relations on two reference bids

The information is in the following forms, for $b _ { i } , b _ { k } { \in } B _ { r } { } ^ { t } ;$

$b _ { i } \succ _ { t } b _ { k } { \Longleftrightarrow } \mathrm { B i d } \ b _ { i }$ is preferred to $b _ { k }$ in round t, or $b _ { i } \sim \mathbf { \delta } _ { t } b _ { k } { \Longleftrightarrow \operatorname { B i d } \ : b _ { i } }$ is indifferent to $b _ { k }$ in round t.

III. Comparison information on the intensities of preferences for pairs of bids on all attributes

A set of linguistic categories ${ \cal S } = \{ S ^ { 1 } , . . . , S ^ { L } \}$ with $S ^ { g } \in S$ is prede<sup>fi</sup>ned by the auctioneer, where $S ^ { 1 }$ describes the most intensive differences in preferences between pairs of reference bids and $S ^ { L }$ denotes the least intensive ones. Hence, they can express their attitudes toward preference intensities in the following way, for $b _ { i }$ $b _ { k } { \in } B _ { r } ^ { \ t } , S ^ { g } \in S ;$

$\Delta ( b _ { i } , b _ { k } ) \in \varsigma ^ { g } \Longleftrightarrow$ The preference o $\mathbf { \dot { \nabla } } b _ { i }$ over $b _ { k }$ is classi<sup>fi</sup>ed into the gth intensive category in round t.

IV. Comparison information on the intensities of preferences for pairs of bids on a particular attribute

Similar to Type III, a set of ordered linguistic categories $S _ { j } =$ $\big \{ S _ { j } { } ^ { 1 } , . . . , S _ { j } { } ^ { L _ { j } } \big \}$ with $S _ { j } { } ^ { g } \in S _ { j }$ is de<sup>fi</sup>ned for each attribute g<sub>j</sub>.

一 $\mathrm { \dot { ~ } o r ~ } g _ { j } \in \dot { G } , b _ { i } , b _ { k } \in \dot { B _ { r } } ^ { t } , \dot { S } _ { j } { ^ { g } } \in S _ { j } ; \Delta _ { j } ( b _ { i } , b _ { k } ) \in _ { t } S _ { j } { ^ { g } }$ ⇔ The local preference of $b _ { i }$ over $b _ { k }$ <sup>ð Þ</sup>concerning attribute g is classi<sup>fi</sup>ed into the gth intensive category in round t.

All four types of information are obtained through GUIs in e-auction intermediaries. As shown in Fig. 3, two types of relations, i.e., preference and indifference, are identi<sup>fi</sup>ed by the auctioneer to declare his/her holistic preferences (Type II). All previously submitted reference bids are presented on the Web page to facilitate selection. The submissions will be presented in the message box as pieces of semantic information. Any information in the box can be modi<sup>fi</sup>ed or deleted by the auctioneer. Generally, the more useful the information, the more consistent the preference model that is inferred. Consequently, the auctioneer is encouraged to provide as much information as he/she can.

How the intermediary gathers Type III Information is illustrated in Fig. 4. A slider is created on the Web page for the auctioneer to re<sup>fi</sup>ne further his/her preference stated in the last step. The option of three degrees is moderate for an auctioneer expressing his/her preference intensities and is thus assigned as the system default. The scale of the slider will change if another option (two or four terms) is selected by the auctioneer.

Similarly, the GUI for collecting the Type IV information is demonstrated in Fig. 5. The attributes involved in local comparisons can be selected from a drop-down list.

The information set can be updated through such interactive GUIs in each round, as discussed in Section 4.1. However, two cases of modi<sup>fi</sup>cation are forbidden in our method to maintain the stability of an auction. First, once the provisional winning bid is announced its status should not be changed by the auctioneer. Second, the information that has been accepted by the auctioneer should not be denied in the subsequent auction process. To illustrate, we suppose that bidders offer bids a, b, c, and d in a round, and according to the current scoring function the ranking is $a \succ b \succ c \succ d$ . If the preference relations do not coincide with the auctioneer's judgments, they are allowed to be modi<sup>fi</sup>ed. For example, the auctioneer can change the ranking to $a \succ c \succ b \succ d .$ Any revision will be accepted as long as the provisional winning bid a is still the most preferred among the bids. The relations such as $a \succ c , c \succ b$ and b ≻ d are con<sup>fi</sup>rmed by the auctioneer and should be no longer modi<sup>fi</sup>ed in the subsequent auction.

## 4.3. Preference elicitation module

The preference elicitation module is the core of the intelligent e-buyer. In each round after the preference statements are processed by the semantic analyzer, this module will be triggered to produce a preference model $V ^ { t }$ that restores the information set Info<sup>t</sup>. Motivated by the philosophy of preference disaggregation, preference elicitation models are proposed in this section to infer V<sup>t</sup>. On the basis of the addi tive preference model (1) and the linear interpolation (4), global value of each reference bid $b _ { i } , b _ { i } { \in } B _ { r } { } ^ { t }$ is expressed in terms of values ${ \nu _ { j } } ^ { l } .$ . Each value $\nu _ { j } { } ^ { l }$ is inferred so that the estimations are as consistent as possible with the given information. Speci<sup>fi</sup>cally, values are estimated by a linear programming model LP1 with an objective function indicating the maximum estimation error σ. The notation t is used to indicate rounds.

![](/api/attachments/D32P8SVD/fulltext/images/fd72aad2840d9697b41abcd703fd6dcc7e417b13cd23cb1a769c34fa9d224eab.jpg)  
Fig. 3. Declaration of holistic preference information in an e-auction intermediary.

![](/api/attachments/D32P8SVD/fulltext/images/a4a5d90b97ea44988aa112af09566e4774bdc18ac43d719a1cbae1898bff639c.jpg)  
Fig. 4. Statement of intensities of preferences over pairs of bids in an e-auction intermediary.

![](/api/attachments/D32P8SVD/fulltext/images/3c414fb36c161d4bb4fe54b6971e283a04a42ae955a245170ffd7a4210596074.jpg)  
Fig. 5. Statement of intensities of preferences over pairs of bids on a certain attribute in an e-auction intermediary.

LP1<sup>t</sup> : Min σ

5

$$
s. t. A \cdot \left[ v _ {1} (g _ {1} ^ {*}),..., v _ {n} (g _ {n} ^ {*}) \right] ^ {\mathrm{T}} \geq h\tag{6}
$$

$$
V (b _ {i}) + \sigma \geq V (b _ {k}) + \varepsilon \quad \forall b _ {i} \succ_ {t} b _ {k}\tag{7}
$$

$$
V (b _ {i}) - V (b _ {k}) \leq \mu + \sigma , \quad V (b _ {k}) - V (b _ {i}) \leq \mu + \sigma \quad \forall b _ {i} \sim_ {t} b _ {k}\tag{8}
$$

$$
V (b _ {i}) - V (b _ {k}) + \sigma \geq V \left(b _ {p}\right) - V \left(b _ {q}\right) + \varepsilon \quad \forall \Delta (b _ {i}, b _ {k}) \in_ {t} S ^ {g},\tag{9}
$$

$$
\forall \Delta (b _ {p}, b _ {q}) \in_ {t} S ^ {g ^ {\prime}}, g <   g ^ {\prime}\tag{10}
$$

$$
\forall \Delta_ {j} (b _ {p}, b _ {q}) \in_ {t} S _ {j} ^ {g ^ {\prime}}, g <   g ^ {\prime}
$$

$$
v _ {j} ^ {l + 1} - v _ {j} ^ {l} \geq 0 \quad \forall j = 1, \dots , n; l = 1, \dots , \alpha_ {j} - 1\tag{11}
$$

$$
v _ {j} \left(g _ {j *}\right) = 0 \quad \forall j = 1, \dots , n\tag{12}
$$

$$
\sum_ {j = 1} ^ {n} v _ {j} \left(g _ {j} ^ {*}\right) = 1\tag{13}
$$

Semantic expressions of four types of information described in Section 4.2 are represented as linear inequalities in Eqs. (6)–(10), respectively. A small positive constant ε is used to ensure the strict inequalities in constraints (7), (9) and (10). μ is a predetermined threshold below which the auctioneer deems that two bids are indifferent. The constraint (11), i.e., the non-decreasing constraint, dictates that an improvement of evaluations on attribute g should not deteriorate the perceived marginal value of the auctioneer. Constraints (12) and (13) are normalization constraints. If the optimal objective value $\sigma ^ { * } > 0 ,$ , there is no preference model compatible with the given preference statements. The auctioneer is required to modify his/her inputs. If $\sigma ^ { * } \leq 0 ,$ , there exists at least one compatible preference model. In case of non-uniqueness a representative one is selected by means of LP2 and LP3 so that it emphasizes the advantages of some bids over the others if the auctioneer prefers the former ones, highlights the differences of intensities of preferences among pairs of bids if the auctioneer assigns them in different categories, and reduces the differences among pairs of bids which are assigned to the same category.

LP2<sup>t</sup> : Max δ

14

s.t. constraints (6), (11)–(13)

$$
V (b _ {i}) \geq V (b _ {k}) + \delta \quad \forall b _ {i} \succ_ {t} b _ {k}\tag{15}
$$

$$
V (b _ {i}) - V (b _ {k}) \leq \mu , \quad V (b _ {k}) - V (b _ {i}) \leq \mu \quad \forall b _ {i} \sim_ {t} b _ {k}\tag{16}
$$

$$
V (b _ {i}) - V (b _ {k}) \geq V \left(b _ {p}\right) - V \left(b _ {q}\right) + \delta \quad \forall \Delta (b _ {i}, b _ {k}) \in_ {t} S ^ {g},
$$

$$
\forall \Delta (b _ {p}, b _ {q}) \in_ {t} S ^ {g ^ {\prime}}, g <   g ^ {\prime}\tag{17}
$$

$$
v _ {j} (b _ {i}) - v _ {j} (b _ {k}) \geq v _ {j} \left(b _ {p}\right) - v _ {j} \left(b _ {q}\right) + \delta \quad \forall \Delta_ {j} (b _ {i}, b _ {k}) \in_ {t} S _ {j} ^ {\mathrm{g}},\tag{18}
$$

$$
\forall \Delta_ {j} (b _ {p}, b _ {q}) \in_ {t} S _ {j} ^ {g ^ {\prime}}, g <   g ^ {\prime}
$$

LP3<sup>t</sup> : Min θ

19

s.t. constraints (6), (11)–(13), (15)–(18)

$$
\begin{array}{l} [ V (b _ {i}) - V (b _ {k}) ] - [ V (b _ {i ^ {\prime}}) - V (b _ {k ^ {\prime}}) ] \leq \theta , \quad [ V (b _ {i ^ {\prime}}) - V (b _ {k ^ {\prime}}) ] - [ V (b _ {i}) - V (b _ {k}) ] \leq \theta \\ \forall \Delta (b _ {i}, b _ {k}), \Delta (b _ {i ^ {\prime}}, b _ {k ^ {\prime}}) \in_ {t} S ^ {g} \end{array}\tag{20}
$$

$$
[ v _ {j} (b _ {i}) - v _ {j} (b _ {k}) ] - [ v _ {j} (b _ {i ^ {\prime}}) - v _ {j} (b _ {k ^ {\prime}}) ] \leq \theta , [ v _ {j} (b _ {i ^ {\prime}}) - v _ {j} (b _ {k ^ {\prime}}) ] - [ v _ {j} (b _ {i}) - v _ {j} (b _ {k}) ] \leq \theta
$$

$$
\forall \Delta_ {j} (b _ {i}, b _ {k}), \Delta_ {j} (b _ {i ^ {\prime}}, b _ {k ^ {\prime}}) \in_ {t} S _ {j} ^ {g}\tag{21}
$$

$$
\delta \geq (1 - \rho) \cdot \delta^ {*}\tag{22}
$$

The notation δ is the minimum difference regarding information II, III and IV, and θ is the maximum difference between pairs of bids that belong to the same category. The optimal objective value $\delta ^ { * }$ is worsened by a speci<sup>fi</sup>ed proportion ρ so that there would be a space for the optimization conducted with regard to LP3.

In case of a large number of attributes and characteristic points, new variables $u _ { j l }$ can be introduced to cut the number of monotonicity constraints (11) as well as the number of decision variables [37], where $u _ { j l }$ for all $j = 1 , . . . , n$ and $l = 1 , . . . , \alpha _ { j } - 1$ represent the differences between the marginal values of two consecutive characteristic points,

$$
u _ {j l} = v _ {j} ^ {l + 1} - v _ {j} ^ {l} \quad \forall j = 1, \dots , n; l = 1, \dots , \alpha_ {j} - 1.\tag{23}
$$

## 5. Numerical example and theoretical comparisons

## 5.1. Illustrative example

## 5.1.1. Auction setting

We consider that an enterprise wants to purchase some personal computers through an e-procurement auction, where a buyer agent on behalf of the enterprise (i.e. the auctioneer) negotiates with several seller agents over numerous bids described by four attributes: price (g ), central processing unit (CPU) performance (g ), memory (g ), and hard disk capacity (g ). Among the set of attributes, price is a quantitative attribute, whereas the others are all qualitative. CPU type is used to measure the performance of a CPU in this example. In the initial phase, the auctioneer de<sup>fi</sup>nes the evaluation scale for each attribute to prescribe the bidding space for potential sellers. The evaluations are listed as follows:

Price: $D _ { 1 } = [ { g _ { 1 } } ^ { * } = \yen 300 0 , { g _ { 1 ^ { * } } } = \yen 45000 0 ]$

CPU performance:

$$
\begin{array}{l} D _ {2} = \left\{g _ {2 *} = g _ {2} ^ {1} = ^ {\prime} \text { level   2   of   Core   2   Duo   E5   series } ^ {\prime}, \right. \\ g _ {2} ^ {2} = ^ {\prime} \text { level   2   of   Core   2   Duo   E6   series } ^ {\prime}, \\ g _ {2} ^ {*} = g _ {2} ^ {3} = ^ {\prime} \text { level   2   of   Core   2   Duo   E7   series } ^ {\prime} \}; \end{array}
$$

<sup>•</sup> Memory capability: $D _ { 3 } = \left\{ g _ { 3 * } = g _ { 3 } { } ^ { 1 } = { } ^ { \prime } 1 \mathrm { G } ^ { \prime } ,  { g _ { 3 } } { } ^ { * } = { } ^ { g _ { 3 } } { } ^ { 2 } = { } ^ { \prime } 2 \mathrm { G } ^ { \prime } \right\}$

Initial reference bids in Round 0.

<table><tr><td>Bid</td><td>Price</td><td>CPU performance</td><td>Memory capacity</td><td>Hard disk capacity</td><td>T_Score</td></tr><tr><td> $b_{1}$ </td><td>4.850</td><td>E7 series</td><td>2G</td><td>320G</td><td>0.754440</td></tr><tr><td> $b_{2}$ </td><td>3.200</td><td>E5 series</td><td>1G</td><td>320G</td><td>0.440174</td></tr><tr><td> $b_{3}$ </td><td>3.965</td><td>E5 series</td><td>2G</td><td>250G</td><td>0.569688</td></tr><tr><td> $b_{4}$ </td><td>4.380</td><td>E6 series</td><td>2G</td><td>250G</td><td>0.658063</td></tr><tr><td> $b_{5}$ </td><td>3.660</td><td>E6 series</td><td>1G</td><td>320G</td><td>0.569687</td></tr></table>

• Hard disk capability:

$$
D _ {4} = \left\{g _ {4 *} = g _ {4} ^ {1} = ^ {\prime} 1 6 0 G ^ {\prime}, g _ {4} ^ {2} = ^ {\prime} 2 5 0 G ^ {\prime}, g _ {4} ^ {*} = g _ {4} ^ {3} = ^ {\prime} 3 2 0 G ^ {\prime} \right\}
$$

## 5.1.2. Preference elicitation

Before the formal negotiation, the auctioneer is asked to provide a set of reference bids. The bids are given in Table 2.

According to the policy that we explained in Section 4.1, the evaluation scale of price is divided into <sup>fi</sup>ve sub-intervals $( \mathrm { i } . \mathrm { e } . , \alpha _ { 1 } = 6 )$ . The endpoints are computed by the formula (3). In this example we assume that the auctioneer's true preference function $V ^ { T r u e }$ is as follows. The parameter values of all four attributes are generated in such a pattern that the increment of the perceived marginal value of the auctioneer is diminishing with the same improvement in attribute values corresponding to the characteristic points.

$$
\bullet \overline {{v}} _ {1} (b _ {i}) = \left\{ \begin{array}{l l} - 0. 0 2 1 0 2 2 5 \cdot g _ {1} (b _ {i}) + 0. 3 4 2 4 2 1 5 & g _ {1} (b _ {i}) \in [ 3. 0, 3. 4) \\ - 0. 1 0 0 3 0 2 5 \cdot g _ {1} (b _ {i}) + 0. 6 1 1 9 7 3 5 & g _ {1} (b _ {i}) \in [ 3. 4, 3. 8) \\ - 0. 1 4 7 3 5 2 5 \cdot g _ {1} (b _ {i}) + 0. 7 9 0 7 6 3 5 & g _ {1} (b _ {i}) \in [ 3. 8, 4. 2); \\ - 0. 2 0 4 4 1 2 5 \cdot g _ {1} (b _ {i}) + 1. 0 3 0 4 1 5 5 & g _ {1} (b _ {i}) \in [ 4. 2, 4. 6) \\ - 0. 2 2 5 2 9 5 0 \cdot g _ {1} (b _ {i}) + 1. 1 2 6 4 7 5 0 & g _ {1} (b _ {i}) \in [ 4. 6, 5. 0 ] \end{array} \right.
$$

$$
\bullet \quad \overline {{v}} _ {2} ^ {1} = 0, \quad \overline {{v}} _ {2} ^ {2} = 0. 1 5 9 7 9 7, \quad \overline {{v}} _ {2} ^ {3} = 0. 2 8 8 0 2 7;
$$

$$
\bullet \quad \overline {{v}} _ {3} ^ {1} = 0, \quad \overline {{v}} _ {3} ^ {2} = 0. 2 6 7 5 9 5;
$$

$$
\bullet \quad \overline {{v}} _ {4} ^ {1} = 0, \quad \overline {{v}} _ {4} ^ {2} = 0. 0 9 5 5 8 2, \quad \overline {{v}} _ {4} ^ {3} = 0. 1 6 5 0 2 4.
$$

Attribute values of price are measured in thousand yuan. The score of each bid with respect to the true preference model is reported under “T\_Score” column in Table 2. All the numerical values are rounded off to six decimal places in this example. The process of preference elicitation is illustrated subsequently.

5.1.2.1. Round 0 (t = 0). A set of preference information on the reference bids is requested to specify preference. Although the auctioneer does not know the precise parameter values of the true preference model, he/she evaluates the performance of a bid according to his/her underlying value system. The information set $I n f o ^ { 0 }$ is comprised of four types of information.

$\mathrm { I . ~ } w _ { 3 } > w _ { 4 } \mathrm { , ~ } w _ { 2 } \geq w _ { 1 } \mathrm { , ~ } w _ { 2 } - w _ { 4 } \geq 0 . 1$

$$
\bullet \quad \text { II. } b _ {1} \succ_ {0} b _ {2}, b _ {1} \succ_ {0} b _ {3}, b _ {1} \succ_ {0} b _ {4}, b _ {3} \succ_ {0} b _ {2}, b _ {3} \sim_ {0} b _ {5}, b _ {4} \succ_ {0} b _ {2};
$$

$$
\bullet \quad \text { III. } \Delta (b _ {1}, b _ {2}) \in {} _ {0} S ^ {1}, \Delta (b _ {1}, b _ {3}) \in {} _ {0} S ^ {2}, \Delta (b _ {1}, b _ {4}) \in {} _ {0} S ^ {3}, \Delta (b _ {3}, b _ {2}) \in {} _ {0} S ^ {3};
$$

$$
\text {IV.} \Delta_ {1} (b _ {5}, b _ {1}) \in_ {0} S _ {1} ^ {1}, \Delta_ {1} (b _ {2}, b _ {4}) \in_ {0} S _ {1} ^ {2}, \Delta_ {1} (b _ {3}, b _ {1}) \in_ {0} S _ {1} ^ {2}, \Delta_ {1} (b _ {2}, b _ {3}) \in_ {0} S _ {1} ^ {3},
$$

$$
\Delta_ {1} (b _ {4}, b _ {1}) \in_ {0} S _ {1} ^ {3}, \Delta_ {2} (b _ {4}, b _ {3}) \in_ {0} S _ {2} ^ {1}, \Delta_ {2} (b _ {1}, b _ {4}) \in_ {0} S _ {2} ^ {2}.
$$

The information of weights is incomplete and the others are provided on a subset of the reference bids and attributes. After the preference statements are submitted, the semantic analyzer is triggered to analyze the information and then transform all semantic statements into mathematical linear inequalities (Section 4.3). All information is transmitted to the preference elicitation module, and the preference elicitation algorithm from the model base infers the parameters of the preference model(s) of the auctioneer (with ε = 0.001, $\mu = 0 . 0 0 0 0 1$ and $\rho =$

Table 4  
Inferred marginal values in Round 0.

<table><tr><td>Price</td><td>CPU performance</td><td>Memory capacity</td><td>Hard disk capacity</td></tr><tr><td> $v_{1}^{1}=0$ </td><td> $v_{2}^{1}=0$ </td><td> $v_{3}^{1}=0$ </td><td> $v_{4}^{1}=0$ </td></tr><tr><td> $v_{1}^{2}=0.030658$ </td><td> $v_{2}^{2}=0.174007$ </td><td> $v_{3}^{2}=0.349490$ </td><td> $v_{4}^{2}=0$ </td></tr><tr><td> $v_{1}^{3}=0.102185$ </td><td> $v_{2}^{3}=0.289514$ </td><td></td><td> $v_{4}^{3}=0.116992$ </td></tr><tr><td> $v_{1}^{4}=0.244005$ </td><td></td><td></td><td></td></tr><tr><td> $v_{1}^{5}=0.244005$ </td><td></td><td></td><td></td></tr><tr><td> $v_{1}^{6}=0.244005$ </td><td></td><td></td><td></td></tr></table>

0.1). The result is presented in Table 3. Notice that only the marginal values of the characteristic points of price are given in the table, and the piecewise linear marginal value function of price can be completely de<sup>fi</sup>ned by these values.

5.1.2.2. Round $1 ( t = 1 ) .$ . After an auction is published in the eintermediary, potential sellers submit their bids if they are interested in the transaction. We suppose that four sellers (i.e., bidders) participate in Round 1, and each of them submits one bid until the deadline of this round. At the end of Round 1, the bid evaluation module is implemented to assess the bids. According to the scoring function $V ^ { 0 }$ inferred in the last round, the estimated score of each bid is presented in Table 4 under ${ } ^ { \mathfrak { u } } \mathrm { E } \_ S \mathrm { c o r e } ^ { \mathfrak { n } }$ column. The provisional winner is highlighted in bold.

The human buyer is informed of the ranking of the bids $b _ { 2 } { } ^ { 1 } { > } b _ { 1 } { } ^ { 1 } { > }$ $b _ { 4 } { } ^ { 1 } { > } b _ { 3 } { } ^ { 1 }$ (perhaps by e-mail or telephone in practice). He/she deems that the estimations are unsatisfactory, thus he/she modi<sup>fi</sup>es some preference relations and provides new information in line with his/her underlying preference.

$$
\begin{array}{c} A d d ^ {1} = \{b _ {2} ^ {1} \succ_ {1} b _ {4} ^ {1} \succ_ {1} b _ {3} ^ {1} \succ_ {1} b _ {1} ^ {1}, \Delta (b _ {2} ^ {1}, b _ {1} ^ {1}) \in_ {1} S ^ {2}, \Delta (b _ {2} ^ {1}, b _ {3} ^ {1}) \in_ {1} S ^ {3}, \Delta_ {1} (b _ {3} ^ {1}, b _ {2} ^ {1}) \in_ {1} S _ {1} ^ {1}, \\ \Delta_ {1} (b _ {1} ^ {1}, b _ {4} ^ {1}) \in_ {1} S _ {1} ^ {2}, \Delta_ {4} (b _ {2} ^ {1}, b _ {1} ^ {1}) \in_ {1} S _ {4} ^ {1}, \Delta_ {4} (b _ {3} ^ {1}, b _ {2} ^ {1}) \in_ {1} S _ {4} ^ {2} \} \end{array}
$$

As in Round 0, the semantic analyzer processes all the information and adds the new preference statements $\lambda d d ^ { 1 }$ into $I n f o ^ { 0 }$ to constitute the new information set, $I n f o ^ { 1 }$ , in Round 1. From the information set the scoring function $V ^ { 1 }$ can be estimated.

5.1.2.3. Rounds 2 to $\bar { \mathsf { p } } ( t = 2 { - } 5 )$ . Subsequently, the losing sellers update their submissions according to the provisional winning bid(s). Likewise, their bids are evaluated by the temporary scoring rule in each round. If the human buyer decides that the results are unsatisfactory, he/she can provide some feedback. The bids from Rounds 2 to 5 and the feedback obtained in each round are summarized in Table 5.

The effectiveness of the estimated scoring function is tested iteration by iteration. In Round 5, the auctioneer <sup>fi</sup>nally decides that the ranking obtained through the scoring rule are perfectly consistent with his/her subjective judgments (Table 5). We set the number of test rounds to $I = 2$ in this example to simplify illustration. That is, once a scoring function is accepted by the human buyer, it does no longer needs to be tested and can then be utilized as the rule that perfectly re<sup>fl</sup>ects the attitude of the auctioneer in the subsequent negotiation process.

## 5.1.3. Analysis of the results

The preference model estimated in each round is reported in Table 6. To facilitate comparison, we also display the true preference in the table. The changes of the marginal values of the attributes are clearly shown in Fig. 6. As observed, when the auctioneer gradually updates the information set the marginal values of all four attributes change signi<sup>fi</sup>cantly in the <sup>fi</sup>rst several rounds. This situation occurs because of the de<sup>fi</sup>ciency in information at the beginning of the elicitation. More precisely, although the estimated marginal values are compatible with the sample information, they are inconsistent with the underlying preference model of the auctioneer. Hence, slight variations in the information set may result in signi<sup>fi</sup>cant changes in the estimations. After several rounds of inference, the solutions change slightly and gradually approach the true preference of the auctioneer.

Bids in Round 1.

<table><tr><td>Bid</td><td>Price</td><td>CPU performance</td><td>Memory capacity</td><td>Hard disk capacity</td><td>T_Score</td><td>E_Score</td></tr><tr><td> $b_{1}^{1}$ </td><td>3.280</td><td>E5 series</td><td>2G</td><td>160G</td><td>0.541063</td><td>0.593495</td></tr><tr><td> $b_{2}^{1}$ </td><td>4.780</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.700769</td><td>0.655865</td></tr><tr><td> $b_{3}^{1}$ </td><td>3.500</td><td>E6 series</td><td>1G</td><td>320G</td><td>0.585736</td><td>0.535004</td></tr><tr><td> $b_{4}^{1}$ </td><td>4.550</td><td>E6 series</td><td>2G</td><td>250G</td><td>0.623313</td><td>0.563096</td></tr></table>

Table 5  
Bids and feedback in Rounds 2 to 5.

<table><tr><td>Round</td><td>Bid</td><td> $g_1$ </td><td> $g_2$ </td><td> $g_3$ </td><td> $g_4$ </td><td>T_Score</td><td>E_Score</td><td>Feedbacks</td></tr><tr><td rowspan="4">2</td><td> $b_1^2$ </td><td>3.800</td><td>E7 series</td><td>1G</td><td>250G</td><td>0.614433</td><td>0.622269</td><td rowspan="4"> $b_3^2 \succ_2 b_4^2 \succ_2 b_2^2 \succ_2 b_1^2, \Delta(b_3^2, b_1^2) \in_2 S^2, \Delta_1(b_4^2, b_3^2) \in_2 S_1^3$ </td></tr><tr><td> $b_2^2$ </td><td>4.780</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.700769</td><td>0.735681</td></tr><tr><td> $b_3^2$ </td><td>4.180</td><td>E6 series</td><td>2G</td><td>320G</td><td>0.767246</td><td>0.743523</td></tr><tr><td> $b_4^2$ </td><td>3.100</td><td>E7 series</td><td>1G</td><td>320G</td><td>0.730303</td><td>0.714762</td></tr><tr><td rowspan="4">3</td><td> $b_1^3$ </td><td>4.200</td><td>E7 series</td><td>2G</td><td>160G</td><td>0.727505</td><td>0.717355</td><td rowspan="4"> $b_4^3 \succ_3 b_3^3 \succ_3 b_2^3 \sim_3 b_1^3$ </td></tr><tr><td> $b_2^3$ </td><td>4.380</td><td>E6 series</td><td>2G</td><td>320G</td><td>0.727505</td><td>0.728813</td></tr><tr><td> $b_3^3$ </td><td>4.180</td><td>E6 series</td><td>2G</td><td>320G</td><td>0.767246</td><td>0.764615</td></tr><tr><td> $b_4^3$ </td><td>4.300</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.802646</td><td>0.799962</td></tr><tr><td rowspan="4">4</td><td> $b_1^4$ </td><td>3.835</td><td>E6 series</td><td>2G</td><td>320G</td><td>0.818083</td><td>0.802066</td><td rowspan="4"> $b_3^4 \succ_4 b_1^4 \succ_4 b_4^4 \succ_4 b_2^4$ </td></tr><tr><td> $b_2^4$ </td><td>4.050</td><td>E6 series</td><td>2G</td><td>320G</td><td>0.786402</td><td>0.777777</td></tr><tr><td> $b_3^4$ </td><td>4.120</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.834875</td><td>0.831208</td></tr><tr><td> $b_4^4$ </td><td>4.300</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.802646</td><td>0.802691</td></tr><tr><td rowspan="4">5</td><td> $b_1^5$ </td><td>3.400</td><td>E7 series</td><td>2G</td><td>160G</td><td>0.826567</td><td>0.829949</td><td rowspan="4">/</td></tr><tr><td> $b_2^5$ </td><td>3.400</td><td>E6 series</td><td>2G</td><td>250G</td><td>0.793919</td><td>0.795979</td></tr><tr><td> $b_3^5$ </td><td>4.120</td><td>E7 series</td><td>2G</td><td>250G</td><td>0.834875</td><td>0.836688</td></tr><tr><td> $b_4^5$ </td><td>4.600</td><td>E7 series</td><td>2G</td><td>320G</td><td>0.810764</td><td>0.814309</td></tr></table>

To evaluate the performance of the proposed preference elicitation model, we introduce two performance measures as follows.

$$
d ^ {t} = \sqrt {\sum_ {j = 1} ^ {n} \sum_ {l = 1} ^ {\alpha_ {j}} \left(v _ {j} ^ {l} (t) - \overline {{v}} _ {j} ^ {l}\right) ^ {2}},\tag{24}
$$

$$
\eta^ {t} = \max _ {j, l} \left(| v _ {j} ^ {l} (t) - v _ {j} ^ {l} (t - 1) | / v _ {j} ^ {l} (t - 1) \cdot 100 \% \right),\tag{25}
$$

Where ${ \nu _ { j } } ^ { l } ( t )$ denotes the marginal values estimated in round t. d<sup>t</sup> is the Euclidean distance between the scoring function V<sup>t</sup> and the true preference model $V ^ { T r u e }$ . It is used to measure the similarity between the estimations and the true preferences. η<sup>t</sup> denotes the maximum deviation of marginal value from it obtained in the last round, which measures the difference of estimations between two consecutive rounds t and t−1. The values of the measures are reported in Table 7. As can be seen from the table, the deviation is large in the <sup>fi</sup>rst several rounds and <sup>fi</sup>nally reduces to 5.645664%, a small value, in Round 4, which implies that after several rounds of inference the solutions converge at a relatively stable level. The argument is also demonstrated by the other performance measure dt. The numerical values of dt become smaller and smaller during the process of preference elicitation, which shows that the estimations approach to the true preferences gradually.

## 5.2. Theoretical comparisons with existing methods

We present a theoretical comparison of our framework with existing researches in terms of four dimensions, namely scoring function, preference elicitation framework, models and implementation architecture.

Scoring functions estimated in Round 0 to 4.

<table><tr><td></td><td>Round 0</td><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>True preference model</td></tr><tr><td> $v_{1}^{1}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{1}^{2}$ </td><td>0.030658</td><td>0.115206</td><td>0.096417</td><td>0.095301</td><td>0.090264</td><td>0.090118</td></tr><tr><td> $v_{1}^{3}$ </td><td>0.102185</td><td>0.115206</td><td>0.170872</td><td>0.173221</td><td>0.170963</td><td>0.171883</td></tr><tr><td> $v_{1}^{4}$ </td><td>0.244005</td><td>0.235188</td><td>0.216814</td><td>0.218410</td><td>0.230741</td><td>0.230824</td></tr><tr><td> $v_{1}^{5}$ </td><td>0.244005</td><td>0.262070</td><td>0.267573</td><td>0.270733</td><td>0.271140</td><td>0.270945</td></tr><tr><td> $v_{1}^{6}$ </td><td>0.244005</td><td>0.262070</td><td>0.283017</td><td>0.285501</td><td>0.275956</td><td>0.279354</td></tr><tr><td> $v_{2}^{1}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{2}^{2}$ </td><td>0.174007</td><td>0.160734</td><td>0.157479</td><td>0.161567</td><td>0.160398</td><td>0.159797</td></tr><tr><td> $v_{2}^{3}$ </td><td>0.289514</td><td>0.276346</td><td>0.283017</td><td>0.288456</td><td>0.289328</td><td>0.288027</td></tr><tr><td> $v_{3}^{1}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{3}^{2}$ </td><td>0.349490</td><td>0.285238</td><td>0.263465</td><td>0.264080</td><td>0.269480</td><td>0.267595</td></tr><tr><td> $v_{4}^{1}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{4}^{2}$ </td><td>0</td><td>0.110734</td><td>0.101221</td><td>0.096413</td><td>0.094961</td><td>0.095582</td></tr><tr><td> $v_{4}^{3}$ </td><td>0.116992</td><td>0.176346</td><td>0.170501</td><td>0.161963</td><td>0.165235</td><td>0.165024</td></tr></table>

Scoring function: Traditional WDP methods refer to those that mainly focus on analyzing WDPs under various scenarios (e.g. [8,24]). They typically use preference aggregation models and require the auctioneer to specify the parameter values directly. Weighted-sum utility functions are the most commonly used scoring functions in this <sup>fi</sup>eld. Our framework, UTA methods and the method proposed in [25] are focus on the inference of such a preference aggregation model. They are all proposed on the principle of preference disaggregation. The method in [25] requires the auctioneer to select the most preferred bid(s), and thus utilize the information to estimate the trade-off weights of a nonlinear utility function. Our framework considers both direct and indirect information which have proposed in traditional WDP methods and UTA methods. It uses the additive value function in the settings of the disaggregation paradigm, as it has been adopted in UTA methods. Speci<sup>fi</sup>cally, marginal value functions are approximated by a piecewise linear modeling approach.

Preference elicitation framework: Preference disaggregation paradigm provides a generic framework for inferring the preference model through the analysis of the global judgment of the decision maker. UTA methods are “considered as the main initiatives and the most representative examples of preference disaggregation theory” [37]. Karakaya and Köksalan develop an interactive approach to estimate the preference function of the auctioneer from his/her past preferences [25]. To our knowledge their study is the only one which involves indirect preference elicitation in auction <sup>fi</sup>eld. As their setting, our framework integrates the process of preference elicitation with the negotiation process of auction. However, we also provide decision support for the auctioneer when he/she is requested to provide new preference information.

Models: Karakaya and Köksalan use a nonlinear programming to estimate the parameters of the utility function. They maximize the minimum difference to obtain a big separation between the estimated utilities of the selected preferred bid(s) and the other ones. The UTA method uses a linear programming model to infer the additive value function(s) which is as consistent as possible with the given information. Speci<sup>fi</sup>cally, such a function is inferred by minimizing the total error. Our approach also adopts linear programming techniques. The consistent parameters of the preference model(s) are estimated by minimizing the maximum estimation error. Moreover, unlike the postoptimality analysis used in the traditional UTA method and one of its variants UTASTAR, a new method is proposed to determine a representative preference model from the set of compatible ones.

Implementation architecture: Unlike other studies that emphasize solely on the methods to infer an auctioneer's preference model(s), our framework also puts forward an intelligent e-buyer for the purpose of promoting the practical use of the proposed approach in real-world commerce.

![](/api/attachments/D32P8SVD/fulltext/images/9859290f308a8cb423db0518fdebe2b262046d39ab673704e70c5c84f635196d.jpg)  
(a) Price

![](/api/attachments/D32P8SVD/fulltext/images/4439237e03b53b17e778b1a0a15db3920347fb6823057d6d24a3f88ff3c074c1.jpg)  
(b) CPU performance

![](/api/attachments/D32P8SVD/fulltext/images/29244e0a227362bb65e6c9c8ab6769ebec36a9f3b7b426347117e7c952abdb6c.jpg)  
(c) Memory capacity

![](/api/attachments/D32P8SVD/fulltext/images/6b94bf2af1e56ff158dddc67303be38eb3e4dc0fdee51c050b18221ddd369f20.jpg)  
(d) Hard disk capacity  
Fig. 6. Changes in the marginal value functions of four attributes with the incremental information set.

## 6. Conclusions

Auctions have played a very important role in commerce, which increasingly utilizes the Web as a medium. Thus, e-procurement auctions, as a transaction mode that bene<sup>fi</sup>ts both the buyer and the suppliers, have attracted an increasing number of <sup>fi</sup>rms to procure items online. However, little attention has been given in the literature to the provision of decision support for participators in the case of e-procurement auctions with multiple attributes. A central task in these multi-attribute auctions is to elicit the scoring function of the buyer, as represented by his/her preference. Therefore, we propose a preference elicitation approach and design an interactive buyer agent to implement it for an iterative multi-attribute procurement auction.

Realizing the dif<sup>fi</sup>culty of explicit elicitation in practice, we adopt a disaggregation approach to infer the preference model(s) of an auctioneer from a set of preference information. Aiming to extract as much information as possible from the auctioneer, we consider four types of information in the framework. The preference model(s) is inferred by linear programming techniques so that the estimations are as consistent as possible with the given information. In case of non-uniqueness we also propose a new method to select a representative preference model from among the set of compatible ones.

Table 7  
Performance measures in Round 0 to 4.

<table><tr><td>Performance measure</td><td>Round 0</td><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td></tr><tr><td> $d^{t}$ </td><td>0.169989</td><td>0.071025</td><td>0.019263</td><td>0.015695</td><td>0.004301</td></tr><tr><td> $\eta^{t}(\%)$ </td><td>/</td><td>275.777254</td><td>48.318923</td><td>5.007356</td><td>5.645664</td></tr></table>

The entire procedure is performed through an agent-based intermediary architecture, which includes <sup>fi</sup>ve main parts, i.e., a semantic analyzer, a preference elicitation module, a bid evaluation module, a model base, and a database. The functional components work together to elicit the underlying scoring rule of the human buyer. We exemplify the entire process of eliciting the preference model of an auctioneer with an application wherein personal computers are procured. The results indicate that our method is capable of inferring the true preference model from a set of preference statements.

The proposed framework can be further extended in the future. First, given the subjective nature of human thinking, other information formats might be offered by the auctioneer. Thus, the preference elicitation model could be improved to enable it to deal with all possible formats. Second, providing decision support for both the auctioneer and the suppliers in the proposed iterative framework may be another interesting extension of this study. Moreover, when the bids and the attributes increase rapidly, the setting with large scale data should be researched further in the future.

## Acknowledgment

The research is supported by the National Natural Science Foundation of China (#71071124). The authors also acknowledge the reviewers for their valuable comments and suggestions.

## References

[1] G. Adomavicius, A. Gupta, P. Sanyal, Effect of information feedback on the outcomes and dynamics of multisourcing multiattribute procurement auctions. Journal of Management Information Systems 28 (4) (2012) 199–229

[2] G. Anandalingam, R.W. Day, S. Raghavan, The landscape of electronic market design, Management Science 51 (3) (2005) 316–327

[3] J. Asker, E. Cantillon, Properties of scoring auctions, The RAND Journal of Economics 39 (1) (2008) 69–85.

[4] D.R. Beil, L.M. Wein, An inverse-optimization-based auction mechanism to support a multiattribute RFQ process, Management Science 49 (11) (2003) 1529–1545.

[5] M.J. Bellosta, S. Kornman, D. Vanderpooten, A uni<sup>fi</sup>ed framework for multiple criteria auction mechanisms, Web Intelligence and Agent Systems 6 (4) (2008) 401–419.

[6] M. Bichler, An experimental analysis of multi-attribute auctions, Decision Support Systems 29 (3) (2000) 249–268.

[7] M. Bichler, The future of eMarket—multidimensional market mechanisms, Cambridge University Press, Cambridge, UK, 2001.

[8] M. Bichler, J. Kalagnanam, Con<sup>fi</sup>gurable offers and winner determination in multi-attribute auctions, European Journal of Operational Research 160 (2) (2005) 380–394.

[9] B. Blau, T. Conte, C. van Dinther, A multidimensional procurement auction for trading composite services, Electronic Commerce Research and Applications 9 (5) (2010) 460–472.

[10] F. Branco, The design of multidimensional auctions, The RAND Journal of Economics 28 (1) (1997) 63–81.

[11] G.G. Cai, Y. Chen, X. Gong, Design of online auctions: proxy versus non-proxy settings, Decision Support Systems 52 (2) (2012) 384–394.

[12] Y.K. Che, Design competition through multidimensional auctions, The RAND Journal of Economics 24 (4) (1993) 668–680

[13] J.Q. Chen, L.Z. Xu, A. Whinston, Managing project failure risk through contingent contracts in procurement auctions, Decision Analysis 7 (1) (2010) 23–39.

[14] C.H. Chen-Ritzo, T.P. Harrison, A.M. Kwasnica, D.J. Thomas, Better, faster, cheaper: An experimental analysis of a multiattribute reverse auction mechanism with restricted information feedback, Management Science 51 (12) (2005) 1753–1762.

[15] C.B. Cheng, Solving a sealed-bid reverse auction problem by multiple-criterion decision-making methods, Computers and Mathematics with Applications 56 (12) (2008) 3261–3274.

[16] E. David, R. Azoulay-Schwartz, S. Kraus, Bidding in sealed-bid and English multiattribute auctions, Decision Support Systems 42 (2) (2006) 527–556.

[17] Y. De Smet, Multi-criteria auctions without full comparability of bids, European Journal of Operational Research 177 (3) (2007) 1433–1452.

[18] M. Doumpos, C. Zopounidis, Developing sorting models using preference disaggregation analysis: an experimental investigation, European Journal of Operational Research 154 (3) (2004) 585–598.

[19] W. Elmaghraby, Auctions within e-sourcing events, Production and Operations Management 16 (4) (2007) 409–422.

[20] J.R. Figueira, S. Greco, R. Słowiński, Building a set of additive value functions representing a reference preorder and intensities of preference: GRIP method, European Journal of Operational Research 195 (2) (2009) 460–486.

[21] S. Greco, V. Mousseau, R. Slowinski, Ordinal regression revisited: Multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 416–436.

[22] D.G. Gregg, S. Walczak, Auction Advisor: an agent-based online-auction decision support system, Decision Support Systems 41 (2) (2006) 449–471.

[23] E. Jacquet-Lagrèze, Y. Siskos, Preference disaggregation: 20 years of MCDA experience, European Journal of Operational Research 130 (2) (2001) 233–245.

[24] S. Kameshwaran, Y. Narahari, C.H. Rosa, Multiattribute electronic procurement using goal programming, European Journal of Operational Research 179 (2) (2007) 518-536.

[25] G. Karakaya, M. Köksalan, An interactive approach for multi-attribute auctions, Decision Support Systems 51 (2) (2011) 299–306.

[26] X.W. Liao, F. Zhang, G.M. Dong, Study on consistency and redundancy of incomplete information, Systems Engineering - Theory & Practice 27 (10) (2007) 104–109.

[27] C. Lin, S. Chen, Y. Chu, Automatic price negotiation on the web: an agent-based web application using fuzzy expert system, Expert Systems with Applications 38 (5) (2011) 5090–5100.

[28] D. Liu, J.Q. Chen, A.B. Whinston, Ex ante information and the design of keyword auctions, Information Systems Research 21 (1) (2010) 133–153.

[29] T. Metty, R. Harlan, Q. Samelson, T. Moore, T. Morris, R. Sorensen, A. Schneur, O. Raskina, R. Schneur, J. Kanner, K. Potts, J. Robbins, Reinventing the supplier negotiation process at Motorola, Interfaces 35 (1) (2005) 7–23.

[30] D.C. Parkes, J. Kalagnanam, Models for iterative multiattribute procurement auctions, Management Science 51 (3) (2005) 435–451.

[31] A. Pekeč, M.H. Rothkopf, Combinatorial auction design, Management Science 49 (11) (2003) 1485–1503.

[32] E.J. Pinker, A. Seidmann, Y. Vakrat, Managing online auctions: current business and research issues, Management Science 49 (11) (2003) 1457–1484

[33] A.K. Ray, M. Jenamani, P.K.J. Mohapatra, An ef<sup>fi</sup>cient reverse auction mechanism for limited supplier base, Electronic Commerce Research and Applications 10 (2) (2011) 170–182.

[34] M.H. Rothkopf, A.B. Whinston, On e-auctions for procurement operations, Production and Operations Management 16 (4) (2007) 404–408.

[35] T. Sandholm, D. Levine, M. Concordia, P. Martyn, R. Hughes, J. Jacobs, D. Begg, Changing the game in strategic sourcing at Procter&Gamble: expressive competition enabled by optimization, Interfaces 36 (1) (2006) 55–68.

[36] J. Simon, F. Melese, A multiattribute sealed-bid procurement auction with multiple budgets for government vendor selection, Decision Analysis 8 (3) (2011) 170–179.

[37] Y. Siskos, V. Grigoroudis, N. Matsatsinis, UTA methods, in: J. Figueira, S. Greco, M. Ehrgott (Eds.), Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, New York, 2005, pp. 297–343.

[38] S. Strecker, Information revelation in multi-attribute English auctions: a laboratory study, Decision Support Systems 49 (3) (2010) 272–280.

[39] S. Talluri, R. Narasimhan, S. Viswanathan, Information technologies for procurement decisions: a decision support system for multi-attribute e-reverse auctions, International Journal of Production Research 45 (11) (2007) 2615–2628.

[40] J.E. Teich, H. Wallenius, J. Wallenius, Multiple-issue auction and market algorithms for the world wide web, Decision Support Systems 26 (1) (1999) 49–66.

[41] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, Designing electronic auctions: an Internet-based hybrid procedure combining aspects of negotiations and auctions, Electronic Commerce Research 1 (3) (2001) 301–314.

[42] J.E. Teich, H. Wallenius, J. Wallenius, O.R. Koppius, Emerging multiple issue e-auctions, European Journal of Operational Research 159 (1) (2004) 1–16

[43] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multi-attribute e-auction mechanism for procurement: theoretical foundations, European Journal of Operational Research 175 (1) (2006) 90–100

[44] T.I. Tunca, S.A. Zenios, Supply auctions and relational contracts for procurement, Manufacturing Service Operation Management 8 (1) (2006) 43–67.

[45] T.I. Tunca, Q. Wu, Multiple sourcing and procurement process selection with bidding events, Management Science 55 (5) (2009) 763–780.

Na Yang has received a Bachelor degree in Management from Chongqing University in 2009. She is a Ph.D candidate at School of Management of Xi'an Jiaotong University. Her research interests concern online auctions and multi-criteria decision-making

Xiuwu Liao received a Master degree in 1989 and a Doctor degree in 2002 from Dalian University of Technology. He has been a professor at School of Mangement of Xi'an Jiaotong University since 2007. He is a member of International Information Systems Society in China an evaluation expert of National Natural Science Foundation of China and Doctoral Fund of Ministry of Education of China, and a reviewer of Information Sciences, Expert Systems, Computers & Operations Research,etc. His area of expertise covers multi-criteria decision making, e-auctions and IT outsourcing. He has published more than 90 refereed research papers in journals and conference proceedings, including Annals of Operations Research, Decision Support systems, Information Systems, etc.

Wayne Wei Huang is a Fellow of Harvard University's Kennedy School and professor of Information Systems at the College of Business, Ohio University. He has worked as a faculty (or a visiting faculty) in research universities worldwide, including Australia (University of New South Wales), Hong Kong, Singapore, China, and the United States (Harvard University) He has published more than 120 refereed research papers in international journals, book chapters, and conference proceedings, including some leading international MIS/IS journals such as IEEE Transactions on Systems, Man, and Cybernetics; Journal of Management Information Systems, MIS Quarterly, Communications of ACM, IEEE Transactions on Professional Communication, Information & Management, Decision Support Systems, ACM Transaction on Information Technology, and European Journal of Information Systems.
