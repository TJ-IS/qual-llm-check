---
otero_id: 4222
otero_key: "PEX6QUPH"
title: "Literature survey: Mathematical models in the analysis of durable goods with emphasis on information systems and operations management issues"
authors: "Ravi Mantena; Vera Tilson; Xiaobo Zheng"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Literature survey: Mathematical models in the analysis of durable goods with emphasis on information systems and operations management issues

Ravi Mantena, Vera Tilson ⁎, Xiaobo Zheng

William E. Simon Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, USA

a r t i c l e i n f o

Available online 25 January 2012

Keywords: Durable goods Literature survey

## a b s t r a c t

Durable goods account for a signi<sup>fi</sup>cant portion of the economy and have been of considerable interest to academic researchers, especially economists, over the last four decades. Given the importance of strategic issues concerning durable goods markets to IS and OM researchers, our objective is to present a broad perspective of the research in this <sup>fi</sup>eld that can serve as a starting point for their modeling efforts when analyzing these markets. Due to the complexity of these markets and the strategic interlinkage of decisions over time, a careful examination of the models is essential for the proper understanding and interpretation of the results from the literature. This paper provides a macro perspective of the research problems, a simple integrative framework for modeling durable goods, an introduction to the models and solution concepts commonly used in the literature, and a discussion of the primary results in the context of their modeling choices. Potentially interesting directions for future IS and OM research in this area are also identi<sup>fi</sup>ed.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Many physical and information goods are not consumed during use, but rather endure to be used repeatedly over an extended period (e.g., cars, aircraft, consumer electronics, and software). These durable goods are often big-ticket items, requiring considerable investment from both consumers and producers. They constitute a signi<sup>fi</sup>cant part of the economy, with annual consumer expenditures exceeding \$1 trillion. Therefore, understanding the functioning of markets for these goods and the incentives and actions of players in related industries is important to managers, regulators, and consumers. Not surprisingly, these markets have been studied extensively by economists over the last four decades. However, it is only recently that Information Systems and Operations Management researchers have really started paying attention to the durability of goods, the strategic behavior of consumers, and the resulting effects on strategic issues of interest to OM and IS. This is partly due to the complex, multifaceted nature of the modeling and analysis of these markets, which addresses consumers, value chains, and regulators, in addition to the producers and the products themselves. Existing literature uses differing modeling assumptions, arriving at a variety of <sup>fi</sup>ndings, sometimes seemingly contradictory. As the authors can attest from personal experience, this imposes a relatively large starting cost on those trying to understand this literature suf<sup>fi</sup>ciently to make, or evaluate, contributions to it.

Our primary goal in this paper is to provide an ef<sup>fi</sup>cient entry point for IS and OM scholars wishing to do analytical research on durable goods. The “big-picture” is presented in the form of an in<sup>fl</sup>uence diagram and a modeling framework that together explain how the different pieces are connected, and where a particular paper or research question <sup>fi</sup>ts. The presentation of the major themes and the various analytical approaches taken, along with an explication of sometimes seemingly contradictory results, should aid researchers new to durable goods to “hit the ground running.” We also present a concise, yet thorough, discussion of the major themes and approaches of particular interest to IS and OM researchers. We encourage scholars intending to do research on durable goods to read the entire paper. Those seeking a quick overview, say to review a paper on a related topic, can skip Sections 4 and 5 which discuss modeling and focus on Sections 6 and 7, which discuss the key strategic issues.

Durable goods raise many vital strategic questions for sellers, consumers, and regulators. The <sup>fi</sup>rst set of questions relates to issues of pricing and timing: How does durability affect a seller's pricing choices? How do the sellers' choices affect the timing of consumers' purchases? The second set concerns the choice of durability by producers, or in the case of information goods, the choices that producers make with regard to upgrades or planned obsolescence. The third set of issues relates to the design and coordination of distribution and supply channels. This includes the consideration of selling and leasing strategies, management of secondary markets, and the asymmetric information issues that these markets often raise. These issues are discussed in detail in Sections 6 and 7

We start by presenting an in<sup>fl</sup>uence diagram (Howard and Matheson [42]) that provides a high-level perspective of the decision problems that durable goods producers face (Fig. 1). These decisions are explored in detail in the rest of the paper. What the diagram makes particularly clear is that, in modeling demand, durable goods papers consider the in<sup>fl</sup>uence of multiple factors. While we have depicted the most common assumptions about which variables are strategic (in boxes) and which ones are exogenous (in triangles), clearly other variations are possible. For example, the evolution of service quality could be a decision made by the manufacturer through his choice of durability.

![](/api/attachments/PEX6QUPH/fulltext/images/3082e016ac791b548129923d141788a967808dc0c5b53b2ddec2248b42958456.jpg)  
Fig. 1. In<sup>fl</sup>uence diagram to model manufacturer pro<sup>fi</sup>t in production of durable goods.

While in<sup>fl</sup>uence diagrams are useful for representing the key variables and their inter-relationships, they are poor at representing the dynamics of the problem. However, dynamic aspects are very important in modeling durable goods, since the temporal pro<sup>fi</sup>le of the value provided to consumers and producers' decisions over time are interlinked. Nevertheless, Fig. 1 is a valuable tool for conceptualizing the set of relationships explored in a particular paper and identifying the assumptions made, explicitly or otherwise, about other potential variables. Thus it provides a framework for understanding the <sup>fi</sup>ndings across different streams of literature and for coping with the seeming contradictions among them.

While researchers from a variety of disciplines are interested in durable goods, the kinds of questions they ask, and, to some extent, the analytical approaches they take, are quite different. Economists, who have done much of the seminal work in the area, are primarily concerned with descriptive models that explain observed market outcomes and with questions of economic ef<sup>fi</sup>ciency. Economic ef<sup>fi</sup>ciency, or social optimality, means that the overall welfare, as measured by the sum of the producer's pro<sup>fi</sup>t and the consumer's surplus, is maximized. OM researchers focus largely on normative models related to manufacturers' decisions on production, capacity, inventory, and supply chains. New product introductions and the effect of digitization and the Internet on value chains have been the primary foci for IS researchers. Table 1 lists the primary research issues of interest to scholars in IS and OM and provides pointers to the sections in this paper that discuss the related literature and the relevant models, as well as providing links to salient references.

Given the size and diversity of the academic durable goods literature,<sup>1</sup> a comprehensive review is beyond the scope of this paper and is also not consistent with our goal of providing an ef<sup>fi</sup>cient entry point. Therefore instead of trying to be exhaustive, we have chosen papers based on their suitability at illustrating a particular modeling approach or explaining a particular strategic issue of interest to IS and OM audiences. Interested readers are referred to Waldman [76] and Orbach [58] for a more complete, non-mathematical review of the eco nomic literature on durable goods.

Fig. 1 also previews the paper's structure, with most of the subsections examining one of the variables (either the exogenous parameters or the strategic variables) presented in the diagram. Section 3 provides an integrated framework that translates key aspects of Fig. 1 into a simple, dynamic analytical setting, which is expanded on in Sections 4 and 5. Section 4 discusses the different approaches to modeling the evolution of service quality, while Section 5 discusses the modeling of consumer value for service streams and the resulting demand. Understanding these modeling approaches is important to gaining insight into the results obtained in the literature. Sections 6 and 7 discuss key strategic decisions concerning durable goods sellers that are of particular interest to IS and OM audiences. We conclude in Section 8 with a discussion of potential research directions of interest to IS and OM. First, however in Section 2, we discuss time inconsistency, a problem related to the dynamic nature of durable goods decisions and a key theme in the literature.

Primary research issues, pointers to sections, and key references

<table><tr><td>Research Issues</td><td>Sections in the paper</td><td>Models in the paper</td><td>Key references</td></tr><tr><td>Time inconsistency</td><td>2</td><td>3.2, 3.3</td><td>[4,12,13,16,17,24,26,28,29,45,47,54,65,68]</td></tr><tr><td>Pricing</td><td>6.1</td><td>3.3</td><td>[8,29,31,45,46,57,68]</td></tr><tr><td>Choice of production technology</td><td>6.2</td><td>3.3</td><td>[47]</td></tr><tr><td>Durability, planned obsolescence, and upgrading</td><td>6.3</td><td>3.1, 3.3, 4.1, 4.3</td><td>[1,17,21,22,30,34,35,48,49,52,65,66,70,72,75]</td></tr><tr><td>Leasing versus selling</td><td>7.1</td><td>3.1, 3.2, 3.3, 5.1, 5.2</td><td>[9,11,12,15,16,25,32,41,43,44,64,73,74,78]</td></tr><tr><td>Complementary goods markets</td><td>7.2</td><td>4.2, 4.4, 5.1, 5.2</td><td>[9,19,20,38,54,66,70]</td></tr><tr><td>Secondary markets</td><td>7.3</td><td>5.1, 5.2</td><td>[2,3,5,36,60,77]</td></tr><tr><td>Channel design</td><td>7.4</td><td>5.1, 5.2</td><td>[4,10,26,62,63,71]</td></tr></table>

## 2. Time inconsistency and the Coase conjecture

A recurrent theme in the durable goods literature is the problem of time inconsistency. This problem, along with its close cousin, the commitment problem, in<sup>fl</sup>uences much of the research in this area, and understanding it is critical to developing insight into the research motivations and results in the <sup>fi</sup>eld. Therefore, in this section, we provide a brief explanation of the problem, why it arises, and some approaches to getting around it.

Durable goods, by de<sup>fi</sup>nition, last for multiple time periods. A consumer who buys a durable product can continue to use it over time; hence a purchase in the present serves as a substitute for a purchase in the future (and vice versa). Economists refer to this as intertemporal substitution. The primary question facing a consumer, therefore, is when to purchase the product. In making this choice, rational consumers take into account not only the current price but also the potential future trajectory of prices. This, in turn, leads to the problem of time inconsistency, or dynamic inconsistency.

The problem was <sup>fi</sup>rst identi<sup>fi</sup>ed by Coase [24], who conjectured that the forward-looking nature of strategic consumers may imply that a monopoly producer of durable goods<sup>2</sup> cannot extract monopoly rents. To understand this, consider the simple setting of a monopolist selling a durable good that provides value over two periods. Assume a population of consumers who are heterogeneous in their willingness to pay for the product in a way that leads to the demand function $D ( p ) = 1 - p .$ . Without loss of generality, assume that the marginal cost of production is zero. A monopolist who wants to maximize his pro<sup>fi</sup>t, $\pi ( p ) = p D ( p )$ , selects the price $p ^ { * } = 1 / 2$ . Thus, all consumers who are willing to pay at least 1/2 for the good purchase the good and exit the market. In the second period, the DGM faces a different (residual) demand curve: $D _ { 2 } ( p ) = 1 / 2 - p ,$ since only the consumers whose willingness to pay is below 1/2 remain in the market. The DGM's pro<sup>fi</sup>t in the second period is maximized by selling goods to these consumers at price $p _ { 2 } ^ { * } = 1 / 4$

If the high-value consumers are rational and patient, they will anticipate the DGM's action and wait for prices to fall instead of buying in the <sup>fi</sup>rst period, thereby forcing the DGM to lower prices in the <sup>fi</sup>rst period itself. This implies that the DGM's pro<sup>fi</sup>ts will be lower than the standard monopoly pro<sup>fi</sup>ts. If the DGM were able to commit to not lowering prices in the future, consumers wouldn't wait in anticipation of lower prices, and the seller could recover the monopoly rents. However, such a commitment would be time inconsistent, i.e., it would not be consistent with a rational choice for the DGM in the future. A commitment that is time inconsistent is generally not credible, and the DGM's pricing <sup>fl</sup>exibility hurts him. In the extreme case, with in<sup>fi</sup>nitely durable products and rapid price adjustments, the Coase conjecture implies that the DGM will have to price at marginal cost and sell the economically ef<sup>fi</sup>cient quantity, much like a perfectly competitive <sup>fi</sup>rm. The Coase conjecture has been proved formally by Bulow [16], Stokey [68], and others. It has been shown that the severity of the time inconsistency problem depends on a number of factors, including the durability of the good [13,17], production capacity [13,16,68], characteristics of the production costs [29,45,47], consumer patience [68], and changes in how consumers value the product over time [12]. We will examine some of these in more detail in later sections.

In an exploration of dynamic inconsistency that predates Coase [24] and is not related to durable goods, Strotz [69] proposed that a rational decision-maker who recognizes dynamic inconsistency has two choices: The <sup>fi</sup>rst is pre-commitment to some future behavior by taking an action that excludes future options inconsistent with his present plans. The second is to select a current plan of action based on treating future behavior as a constraint, or, in other words, following a time-consistent policy. A pre-commitment by a DGM to not reduce future prices is generally treated in the literature as a strategy that is not credible. It is referred to as the commitment problem. However, Waldman [76] argues that such commitments may in fact be feasible under some circumstances, through strategies like favored-customer clauses (money-back guarantees in case of future price declines), limited-edition productions, and other possible contractual commitments. The problem may also be mitigated if the DGM can develop a reputation for not lowering prices.<sup>3</sup> Waldman [76] also points out that the commitment problem applies more broadly, extending beyond the pricing choices of the DGM to other strategic choices, such as product upgrades, R&D investments, etc.

In Section 3, we include a detailed discussion regarding the second strategy proposed by Strotz—following a time-consistent policy. In fact, a time-consistent equilibrium is a key solution concept in this literature. This is true even when the issue of time inconsistency is mitigated by <sup>fi</sup>nite durability of goods, limited production capacity, convex production costs, etc., and therefore we also discuss the related solution concepts in more detail.

## 3. An analytical framework for the dynamic modeling of durable goods

Durable goods produced at any point in time, survive and create value over multiple time periods. In Section 3.1, we discuss how durable goods can be modeled as streams of services providing revenues to producers over multiple periods. In Section 3.2, we use a simple twoperiod model to analyze the quantity choices of a DGM, use it to illustrate the derivation of a time-consistent policy using backward induction, and discuss the resulting implications. Finally, in Section 3.3, we discuss equilibrium solution concepts that have commonly been employed to analyze durable goods markets.

## 3.1. Modeling durable goods as service streams

In this section, we specify a basic modeling framework that clearly captures the multi-period nature of durable goods and provides a foundation for systematically exploring the modeling approaches found in the literature. Let T be the time domain of the model and S be the space of feasible service qualities. Early durable goods models such as [48,72], and [17] assumed that a good can provide only two levels of service, say 0 or 1. When a good is functioning, its service quality is 1; when it is not functioning, it is $0 , \ s _ { 0 } \ S = \{ 0 , 1 \}$ in this case. More generally, let $s ( \cdot ) { : } T {  } S$ represent the quality of service provided by one unit of a durable good at time t. Let $\bar { Q ( \cdot ) } : T {  } \mathbb { R } _ { + } ^ { \# S }$ <sup>ð Þ þ</sup>represent the total number of units available at time t, providing various levels of service in S, i.e., Q(⋅) provides the stock of durable goods available in the market at time t. Finally, let q(s,t) be the number of units providing service s that are offered by the seller at time t. Note that Q(t) includes all units available in the market at time t, including q(s, t).

Focusing, for the moment, on the problem from the perspective of a durable goods seller (as in Fig. 1), let r(⋅) denote the market rents<sup>4</sup> at time t, from offering a product of quality s, given a certain stock in the market. These rents naturally depend on the quality itself but can more generally depend on the availability of substitute products, the characteristics of the population, etc. The total discounted seller rents associated with a product whose quality of service evolves according to s(t) is then given by

$$
R = \sum_ {t \in T} \gamma^ {t} r (s (t), Q (t), t) q (s (t), t)\tag{1}
$$

where γ is the seller's discount factor. An expression similar to Eq. (1) can be speci<sup>fi</sup>ed from a consumer perspective, where we replace the supply quantity with the consumption quantity and the rent function with a value function.

Modeling a producer's durable goods problem as presented in Eq. (1) requires modeling domains S and T, functions s(⋅), r(⋅), and $Q ( \cdot )$ , the relationships between them, and the decisions of the manufacturer and the consumers. In the next two sections of the paper, we will build on this basic modeling framework and present more detailed discussions of the different models of durable good quality, value, and demand analyzed in the literature. But, before doing so, it will be instructive to look at a simple two-period example that illustrates the basic features of the framework and the solution concept used to specify the outcomes. This is done in the next subsection.

## 3.2. Deriving a time-consistent policy in a simple two-period model

The following example is based on [16]. Consider a durable good that provides perfect quality for two periods and perishes thereafter, $\mathrm { i . e . }$ , here, $T = \{ 1 , 2 \}$ and $S = \{ 0 , 1 \}$ . Let γ represent the discount factor that is common to both the DGM and the consumers, with $0 < \gamma \leq 1$ For simplicity, assume that the production cost is normalized to zero.

The DGM chooses the quantities of durable goods to sell in each of the two periods. Let $q _ { 1 }$ and $q _ { 2 }$ be the quantities chosen in periods 1 and 2 respectively. In the context of the framework presented in the previous section, Q(t) is the total number of units available at time t, and we therefore have $Q ( 1 ) = q _ { 1 }$ and $Q ( 2 ) = q _ { 1 } + q _ { 2 } .$ . Let $r ( Q ) = 1 - Q$ be the per-period inverse demand curve for the durable good. In the <sup>fi</sup>rst period, the consumers' willingness to pay re<sup>fl</sup>ects not only their value from use in the <sup>fi</sup>rst period but also the continued value (either through use or through sale in a secondary market) that they can obtain in the second period. Therefore, the amount charged for the goods sold in the <sup>fi</sup>rst period is given by $p _ { 1 } = r ( q _ { 1 } ) + \gamma r ( q _ { 1 } + q _ { 2 } )$ , while the second period's price is $p _ { 2 } = r ( q _ { 1 } + q _ { 2 } )$ . The DGM's total discounted pro<sup>fi</sup>t over the two periods can be written as $\pi ( q _ { 1 } , q _ { 2 } ) = q _ { 1 } p _ { 1 } + \gamma q _ { 2 } p _ { 2 }$ . The DGM's decision problem is to pick nonnegative $q _ { 1 }$ and $q _ { 2 }$ to maximize the overall discounted pro<sup>fi</sup>t.

If the DGM were able to commit to values of $q _ { 1 }$ and $q _ { 2 }$ at the start, then he would select $q _ { 1 } = 1 / 2$ and $q _ { 2 } = 0$ , since that maximizes the overall pro<sup>fi</sup>t. Following such a policy would result in the <sup>fi</sup>rst period price $p _ { 1 } = ( 1 + \gamma ) / 2$ and a total pro<sup>fi</sup>t of $\pi _ { M } ^ { * } = ( 1 + \gamma ) / 4$ . However, as discussed in Section 2, the DGM will not be able to credibly commit to the second period quantity in advance.

Quantities $q _ { 1 }$ and $q _ { 2 }$ must be determined under the assumption that the DGM serves the residual demand in the second period with a quantity that is optimal for that demand, i.e., the DGM's secondperiod choice is time consistent. A time-consistent policy is found using backward induction (giving a sub-game perfect equilibrium). The DGM's second-period pro<sup>fi</sup>t is maximized by $q _ { 2 } ^ { * } ( q _ { 1 } ) = ( 1 - q _ { 1 } ) /$ 2. Thus the second period pro<sup>fi</sup>t can be expressed as a function of the <sup>fi</sup>rst period decision $q _ { 1 } \colon \pi _ { 2 } ^ { * } ( q _ { 1 } ) = ( 1 - q _ { 1 } ) ^ { 2 } / 4$ . The total discounted pro<sup>fi</sup>t for the DGM who decides on quantity $q _ { 1 }$ in the <sup>fi</sup>rst period and acts optimally in the second period can then be written as $\pi _ { C } ( q _ { 1 } ) =$ $q _ { 1 } p _ { 1 } + \gamma \pi _ { 2 } ^ { * } ( q _ { 1 } )$ . Solving the optimization problem yields $q _ { 1 } ^ { * } = 1 / ( 2 +$ $\gamma / 2 )$ , which in turn implies that $q _ { 2 } ^ { * } = ( 1 + \gamma / 2 ) / ( 4 + \gamma )$ . The corresponding <sup>fi</sup>rst and second period prices are $p _ { 1 } = ( 1 + \gamma / 2 ) ^ { 2 } / ( 2 + \gamma / 2 )$ $p _ { 2 } { = } p _ { 1 } / ( 2 + \gamma )$ , and the overall discounted pro<sup>fi</sup>t of the DGM is $\pi _ { C } { } ^ { * } = ( 1 + \gamma ) / 4 - \gamma / [ 4 ( 4 + \gamma ) ]$ . The difference in pro<sup>fi</sup>ts $\pi _ { M } ^ { * }$ and π\* illustrates the loss in monopoly rents due to the commitment problem faced by the DGM. Note that, under the time-consistent policy, $p _ { 1 } > p _ { 2 }$ , implying that a “price-skimming” strategy is optimal for the DGM.

Coase [24] suggested that leasing, rather than selling, durable goods, could help avoid the commitment problem. It is easy to see that here. In the leasing case, the DGM's second-period problem can be formulated as selecting $Q ( 2 )$ to maximize $Q ( 2 ) r ( Q ( 2 ) )$ subject to $Q ( 2 ) \geq q _ { 1 }$ , as opposed to <sup>fi</sup>nding $q _ { 2 }$ maximizing q r(Q(2)), which is the case in selling.

Since the DGM retains ownership of the goods and his task of choosing lease prices is essentially identical to that of a non-durable goods monopolist (since no goods are carried over by the consumers from period 1 to period $^ { 2 ) , }$ the DGM makes the same pro<sup>fi</sup>ts as a regular monopolist. The basic intuition is that short-term leases imply that consumers stay in the market instead of exiting it—essentially converting a durable good into a consumable service. Retaining ownership of the product also enables the DGM to make a credible commitment about the total quantity of goods available on the market and reduce future competition from used goods.

## 3.3. Equilibrium concepts

The great majority of durable goods papers (e.g., [11,12,16,17,25, 27,39]) <sup>fi</sup>nd an equilibrium time-consistent strategy using backward induction in a two-period model, as was illustrated in Section 3.2. In the example, an aggregate inverse demand function modeled the reaction of consumers. More recent work derives aggregate demand based on the actions of individual consumers who decide when to buy a good and of what quality. Although individual consumers choose among multiple strategies, the consumers are not strategic in the same sense as the manufacturer. Consumers are followers; the manufacturer makes a decision with regard to strategic variables (normally, production and pricing), and consumers respond.

Multi-period durable goods models are also generally characterized as equilibrium models, and the solution concept used is known as Rational Expectations Equilibrium (REE), or Fulfilled Expectations Equilibrium (FEE). Stokey in [68] describes REE in the durable goods context $\mathtt { a s } ^ { \ast } \mathtt { a }$ pair of functions, one describing how buyers' expectations are formed and one describing the monopolist's sales strategy, that jointly have the following two properties: (1) the seller's strategy maximizes the present discounted value of pro<sup>fi</sup>ts, given the expectation function of buyers; and (2) buyers' expectations are ful<sup>fi</sup>lled along the realized path of production.” In any REE, expectations are ful<sup>fi</sup>lled along the equilibrium path, but they may not be ful<sup>fi</sup>lled if an event were to cause a perturbation away from the equilibrium path. The events could be exogenous shocks or a seller's deviation from original policy. If a seller's decision trajectory at an initial time is not optimal at a subsequent time, that seller has the incentive to deviate to another decision trajectory that maximizes the present discounted value of pro<sup>fi</sup>ts, given current conditions and buyers' expectations. In this case, the policy announced at the earlier time is said to be time inconsistent.

Stokey further discusses the concept of Perfect Rational Expectations Equilibrium (PREE), which requires that the seller maximize the present discounted value of pro<sup>fi</sup>ts in every contingency given that buyers' expectations are ful<sup>fi</sup>lled along the realized path of production from that date on. In essence, PREE ensures that a seller's decision trajectory announced in any contingency is time consistent. Thus, PREE resembles the concept of sub-game perfect equilibrium (SPE).

Another common solution concept, a Markov perfect equilibrium (MPE), is a sub-game perfect equilibrium in Markov strategies [51]. A player using a Markov strategy conditions his actions only on the state in the current period. In <sup>fi</sup>nite horizon games, with consumers and the DGM making alternate moves, the existence of a unique MPE is guaranteed under very mild assumptions. For the in<sup>fi</sup>nite horizon case, an MPE may not exist or may not be unique. However, Maskin and Tirole [51] point out that “MPE is often quite successful in eliminating or reducing a large multiplicity of equilibria in dynamic games, and thus in enhancing the predictive power of the model.” The concept of MPE is often used in econometric research, e.g., [53,56,67], etc. Huang et al. [43] use the solution concept of MPE in an analytical model to examine the production and pricing problem of a monopoly manufacturer of <sup>fi</sup>nitely durable goods over an in<sup>fi</sup>nite horizon.

## 4. Modeling evolution of service quality

Sections 4 and 5 discuss the treatment of parts of the modeling framework in the literature, starting with a discussion of modeling quality and durability.

The simplest, and a quite common, assumption in the literature is to consider goods as being in<sup>fi</sup>nitely durable. This implies that their quality stays constant over time, over the in<sup>fi</sup>nite horizon. However, when durable goods are not in<sup>fi</sup>nitely durable, their quality can vary over time or with use. Because quality depreciation and potential replacement sales mitigate a seller's commitment problem, they have a bearing on the seller's strategic choices. In this section, we describe the common approaches to modeling durable good quality over time and discuss some other attributes that relate to a more general notion of quality.

## 4.1. Durable good quality over time

A two-quality model of deterministic deterioration is particularly analytically tractable and hence common in the durable goods literature. For example, in the one-hoss shay model in [48] and [72], all goods fail after serving for a deterministic time period τ. Eq. (2) below describes the one-hoss shay model with $s _ { i } ( t )$ denoting the quality at time t of a good manufactured in period t .

$$
s _ {i} (t) = \left\{ \begin{array}{l l} 1 & t _ {i} \leq t \leq t _ {i} + \tau \\ 0 & o t h e r w i s e \end{array} \right.\tag{2}
$$

In a standard two-period model, new goods function at level 1, used or old goods function at some level ${ \bf \Phi } _ { \nu } \in ( 0 , 1 )$ , and after two periods their quality level drops to 0. So $S = \{ 0 , { \scriptscriptstyle \mathrm { { \scriptscriptstyle \Omega } } } 1 \}$ . Presented in Eq. (3), the model is used in [60,73], and many others.

$$
s _ {i} (t) = \left\{ \begin{array}{l l} 1 & t = t _ {i} \\ \text {   } \quad & t = t _ {i} + 1 \\ 0 & t > t _ {i} + 1 \text {   or   } t <   t _ {i} \end{array} \right.\tag{3}
$$

Epple and Zelenitz [32] use a variation on Eq. (3) assuming that leased goods deteriorate differently than sold goods. Denoting utilization mode with u, they model service quality with Eq. (4). A similar model is used in $[ 2 7 ] ,$ where goods produced in the same period deteriorate if they are sold to consumers but do not deteriorate if they are stored by the producer. In [62], used cars from rental companies deteriorate differently than cars used by retail consumers.

$$
s _ {i} (t, u) = \left\{ \begin{array}{c c} 1 & t = t _ {i} \\ _ {\triangle_ {u}} & t = t _ {i} + 1 \\ 0 & t > t _ {i} + 1 \text {or} t <   t _ {i} \end{array} \right.\tag{4}
$$

A deterministic continuous-time model is also often used to model deterioration due to use or obsolescence due to exogenous technological progress. Mehra and Seidmann [52] model software obsolescence using Eq. (5) with $g ( x ; d ) = \mathfrak { m a x } \{ 0 , 1 - d x \}$ , where d is an exogenous <sup>ð Þ ¼ f g</sup>parameter modeling the rate of obsolescence. More generally $g :$ $\mathbb { R } _ { + } \to [ 0 , 1 ]$ in Eq. (5) is assumed to be non-increasing in its arguments, <sup>þ ½ -</sup>and d can be an endogenous variable representing the producer's decision about built-in quality.

$$
s _ {i} (t) = \left\{ \begin{array}{c c} g (t - t _ {i}; d) & t \geq t _ {i} \\ 0 & t <   t _ {i} \end{array} \right.\tag{5}
$$

While deterministic models are the most common, the quality or durability of a good is often uncertain, and in some contexts, this uncertainty needs to be explicitly considered. In [72], Swan used a simple model of probabilistic deterioration to investigate a manufacturer's decision about built-in deterioration rate d. A product described by Eq. (6) is either as good as new, or does not work at all. The probability of breakage is described by a distribution function $G ( \cdot )$ , decreasing in both of its arguments.

$$
P r \{\tilde {s} _ {i} (t) = _ {\Delta} \} = \left\{ \begin{array}{c c} G (t - t _ {i}; d) & _ {\Delta} = 1, t \geq t _ {i} \\ 1 - G (t - t _ {i}; d) & _ {\Delta} = 0, t \geq t _ {i} \\ 1 & _ {\Delta} = 0, t <   t _ {i} \\ 0 & o t h e r w i s e \end{array} \right.\tag{6}
$$

In some cases, it is more appropriate to focus on improvement over time rather than deterioration. In modeling products under sequential innovation, Dhebar [28] assumes that the quality of service <sup>fl</sup>ow is a function of the time when the product was manufactured, as modeled by Eq. (7). Although a common assumption in such models is that the later the date of manufacture, the higher the quality: $t _ { L } \leq t _ { H } =  { s } _ { L } \leq  { s } _ { H } ,$ other variations do exist. More generally, the quality could be based on an endogenous investment decision made by the manufacturer.

$$
s _ {i} (t) = \left\{ \begin{array}{l l} s _ {i} & t \geq t _ {i} \\ 0 & t <   t _ {i} \end{array} \right.\tag{7}
$$

## 4.2. Aftermarket maintenance

In some durable goods settings, quality can be an endogenous choice of consumers based on their investment in maintenance. A number of papers have examined consumer and producer decisions in this regard. Rust [64] de<sup>fi</sup>nes a transition probability function to model how the quality of a durable good evolves over time, based on the amount of maintenance received. Schmalensee [66], Su [70], and Morita and Waldman [54] assume that deterioration is deterministic, but they make it dependent on the level of maintenance. Let d be the deterioration rate chosen by the producer and μ be the maintenance expenditure by the user. Assuming that the product is new at time $t = 0 ,$ , its quality evolution is modeled by the differential equation (8).

$$
s ^ {\prime} (t) = h (d, \mu , s (t)), \frac {\partial h}{\partial d} \leq 0, \frac {\partial h}{\partial \mu} \geq 0\tag{8}
$$

Generally $h ( d , \mu , s ( t ) )$ is such that $s ^ { \prime } ( t )$ is negative, but a lower built-in deterioration rate and larger maintenance expenditure lead to slower deterioration. In [70] and [54], initial quality also slows down deterioration, so that $\frac { \partial h } { \partial s ( 0 ) } { \geq } 0$ . More detailed discussion regarding aftermarket <sup>ð Þ</sup>maintenance is included in Section 7.2.

## 4.3. Network effects

An important attribute of many durable technology products (especially information goods) is the presence of network effects. In this case, a consumer's value depends not only on the quality of the goods but also on the number of adopters. For example, Zhang and Seidmann [78] consider a software product with versions indexed by i. The total number of adopters of version i at time t is $Q _ { t } ^ { i } .$ Versions of software that are compatible with version i at time t are the set $K _ { t \cdot } ^ { i }$ Consumers value two attributes of the good: its own quality s and the size of its network. The quality of service provided by the software product's version i at time t can then be thought of as a twodimensional attribute:

$$
\boldsymbol {s} = \left\{s _ {i}, \sum_ {k \in {} _ {t} ^ {i}} Q _ {t} ^ {k} \right\}.\tag{9}
$$

The sellers in many of these cases can choose whether the newer version of the software is backward compatible or forward compatible with the other versions. The compatibility choice, in turn, affects the network effects enjoyed by adopters of existing and new versions.

Some products, such as luxury goods, may have negative network effects. People seeking exclusivity would prefer a small user base for the product [1]. Eq. (9) is still applicable in these circumstances.

## 4.4. Complementary products

Many durable goods are used in conjunction with other (often non-durable) complementary products or services. For example, printers need ink/toner cartridges, game consoles need games, computing devices need application software, automobiles need periodic service, etc. Complementary goods or services can be provided by the manufacturer itself or by other producers. This fact can complicate the manufacturer's decisions, but also enlarge the set of available strategies for extracting rents. For example, it may be possible for the DGM to monopolize the market for the complementary goods. In [9], Bhaskaran and Gilbert examine how the need for complementary products affects a DGM's decisions of whether to sell or lease its product. Similar to Eq. (9), their model of quality of service provided by the good at time t is two-dimensional $\pmb { s } = \{ s , m \}$ . A consumer's utility in this case is affected not only by the durable good's own quality s but also by the number of complementary goods, m. More broadly, positive network effects can also be thought of as complementarities, as can the need for aftermarket service. We discuss the <sup>fi</sup>ndings related to complementary products and aftermarkets in Section 7.2.

## 5. Modeling consumer valuation and demand

Demand for durable goods can either be modeled at the aggregate market level or the individual consumer level. While the early literature largely used aggregate models, recent work has focused more closely on consumer heterogeneity and individual choice, aggregating these choices into market-demand curves. Aggregate demand models (e.g., [13,72]) generally relate the sale or lease price of a product to the total volume of the service available and its quality, using a reduced form demand function. A good example is Bulow's [16] twoperiod model, which we analyzed in simpli<sup>fi</sup>ed form in Section 3.2 where the demand at a point in time is speci<sup>fi</sup>ed as a function of the existing durable-goods stock. In this section, we'll describe individual consumer utility and discuss how individual choice is aggregated into a market-demand curve. We also provide an illustration by deriving the aggregate demand for a software product subject to network effects.

## 5.1. Individual utility and choice

Demand for durable goods is shaped by both consumer characteristics and product characteristics. To account for differences in consumer characteristics such as income, gender, etc., consumers are typically modeled to have heterogeneous reservation values for the products. These reservation values are captured by a consumer's type $\theta \in \Theta .$ . The value that a consumer of type θ places on using a service of quality s for a single period in period t is given by $\nu ( s , \theta , t )$ Consumers are typically assumed to use no more than a single unit of a good in any period.

Models of consumers' willingness to pay generally follow the classic value heterogeneity models of [55] and [50]. It is usually assumed that all consumers are willing to pay more for a higher-quality good than for a lower-quality good. Further, it is assumed that consumers of higher type place higher value on goods of all qualities. An additional assumption that high-type consumers have higher marginal value for quality than lower-type consumers allows for consumer segmentation:

$$
\theta_ {L} \leq \theta_ {H}, s _ {L} \leq s _ {H} \Rightarrow v (s _ {H}, \theta_ {L}) - v (s _ {L}, \theta_ {L}) \leq v (s _ {H}, \theta_ {H}) - v (s _ {L}, \theta_ {H}).\tag{10}
$$

A common form of the value function satisfying these conditions, used for example in [27,73], and numerous others, is

$$
v (s, \theta) = v _ {0} s \theta\tag{11}
$$

where $\boldsymbol { v } _ { 0 }$ is some non-negative constant.

When consumers' perceived quality is a function of several complementary attributes, as in Eq. (9), models of willingness to pay still satisfy the above conditions, with $S _ { L }$ and $s _ { H }$ ordered using product ordering on S. For instance, Gilbert and Jonnalagedda [38] model the willingness to pay in the presence of complementary goods as

$$
v (\mathbf {s}, \theta) = v (\{s, m \}, \theta) = v _ {0} s \theta m - \alpha m ^ {2}\tag{12}
$$

where α is a non-negative constant, modeling decreasing marginal value of additional complementary products.

A similar treatment of consumer heterogeneity is used in [78] for durable goods with network effects as described in Eq. (9). Taking the consumer type into account, the utility becomes:

$$
v (s _ {i}, \theta , t) = v _ {0} s _ {i}   \theta + \xi \sum_ {k \in K _ {t} ^ {i}} Q _ {t} ^ {k}.\tag{13}
$$

The constant ξ models the intensity of network effects. The larger the value of $\displaystyle { \xi , }$ the more important is the network effect as compared to the inherent quality of the good. The above formulation of network effects uses an “additive” speci<sup>fi</sup>cation in which a consumer's network bene<sup>fi</sup>t is independent of his valuation for the base good. An alternative “multiplicative” formulation, where the network bene<sup>fi</sup>t also depends on type $\theta ,$ may be more natural in some cases where consumers with a higher “inherent” value for a product also place a greater value on network bene<sup>fi</sup>ts (for example, [30]).

Demand uncertainty can be easily accommodated in this model. For instance, Desai et al. [27] incorporate uncertainty by modeling the coef<sup>fi</sup>cient $\boldsymbol { v } _ { 0 }$ in Eq. (11) as a random value:

$$
v (s, \theta) = \tilde {v} _ {0} s \theta .\tag{14}
$$

Their objective is to capture the news-vendor-like character of the model. The manufacturer must make decisions on how many goods to produce before demand is known.

Pesendorfer in [59] explains fashion cycles using a matching model of consumer utility to add network effects. Consumers derive value from being matched with other consumers, with this value depending on their type (and the type to which they are matched). The numbers of each type of consumers adopting the product determine the matching probability and hence lead to network effects.

Consumers' choice is then derived from these value functions. For consumer $\theta ,$ let the use of the stream of services ${ } _ { \mathrm { { } } \mathrm { { } } } ( t )$ provided by a durable good, be associated with a stream of payments $p _ { _ { \cdot } } ( \theta )$ . Note that it is possible that p (θ), the stream of payments made by the consumer, is not equal to the stream of payments received by the producer, since consumers could be acquiring the use of goods through different means as well as incurring transaction costs. It is generally assumed that consumers select ${ } _ { \mathcal { ( t ) } }$ to maximize their discounted net surplus:

$$
\max _ {\Delta (t)} \sum_ {t \in \mathcal {T}} \left(\gamma_ {\theta}\right) ^ {t} \left(v (\Delta (t), \theta , t) - p _ {\Delta} (\theta , t)\right)\tag{15}
$$

where p (θ,t) is the payment at time t from the stream p (θ). This then is the consumer analog of the seller objective function we presented in Eq. (1) in Section 3.1. Typically, it is assumed that $\textstyle v ( s , \theta , t )$ does not change with time, and so the value function simpli<sup>fi</sup>es to $\boldsymbol { \nu } ( s , \boldsymbol { \theta } )$ In <sup>fi</sup>nite horizon models, when the consumer's optimal strategy is computed using backward recursion, salvage value is commonly set to 0, irrespective of the quality of the good (see [27] for an example).

If uncertainty in value is modeled, then typically it is assumed that consumers are risk-neutral and Eq. (15) is replaced with

$$
\max _ {\Delta (t)} E \left[ \sum_ {t \in \mathcal {T}} \left(\gamma_ {\theta}\right) ^ {t} \left(v (\Delta (t), \theta , t) - p _ {\Delta} (\theta , t)\right) \right].\tag{16}
$$

## 5.2. Aggregating individual choice to derive demand

To specify market demand at time $t ,$ it is assumed that the size of the consumer population is $\mathcal { P } ( t )$ and that consumer types are distributed in the population according to the density function $f ( \theta )$ . Most commonly, $f ( \theta )$ is assumed to be uniform, and $\mathcal { P } ( t )$ is assumed to either be constant or increasing. $\operatorname { L e t } _ { \searrow \theta } ( t )$ maximize the surplus of consumer θ at time t and de<sup>fi</sup>ne indicator function $I ( \varsigma , t , \theta )$ such that

$$
I (\varsigma , t, \theta) = \left\{ \begin{array}{l l} 1 & \varsigma = _ {\Delta_ {\theta}} ^ {*} (t) \\ 0 & o t h e r w i s e \end{array} \right..\tag{17}
$$

The number of consumers that use good of quality ς in period t is then found by aggregating the consumers' choices:

$$
D (\varsigma , t) = \mathcal {P} (t) \int_ {\theta \in \Theta} I (\varsigma , t, \theta) f (\theta) d \theta .\tag{18}
$$

When a durable good of a single quality is offered, and it has in<sup>fi</sup>- nite durability, demand in a period is purely determined by when particular consumers choose to buy. When the service quality depreciates with age, products of different vintages can coexist in the market, usually resulting in market segmentation. Consumers with higher willingness to pay use higher-quality products, while consumers with lower willingness to pay use lower-quality ones. As products deteriorate, consumers may sell (or buy) lower-quality goods in a secondary market; care must be taken to appropriately re<sup>fl</sup>ect this in the sellers' pro<sup>fi</sup>t function. For example, in the in<sup>fi</sup>nite-horizon model in [43], with the quality of goods evolving according to Eq. (3) in the MPE, consumers with highest willingness to pay use new goods every period; lower-type consumers alternate between using new and old goods; consumers of the still lower type always use old goods; and those with the lowest willingness to pay use nothing at all.

## 5.3. Example: derivation of aggregate demand for a software product with network effects

As an illustration of the demand modeling discussed above, consider the case of a monopoly software vendor that sells software to a group of heterogeneous consumers. Consider a two-period setting, and assume that the software displays network effects. Let the initial version of the software have quality $s _ { 1 } ,$ , and assume that the vendor invests in R&D to improve software quality to $s _ { 2 }$ in the second period, where $s _ { 2 } > s _ { 1 } .$ . Let Eq. (13) model a consumer's value from using the software for one period, with $\scriptstyle v _ { 0 } = 1$ . Recall that $\boldsymbol { Q } _ { t } ^ { i }$ is the number of consumers who own version s at time t. Assume backward compatibility between versions, so that $K _ { 1 } ^ { 1 } = K _ { 2 } ^ { 1 } = \{ 1 \}$ , and $K _ { 2 } ^ { 2 } = \{ 1 , 2 \}$ where $K _ { t } ^ { i }$ is the set of software versions that are compatible with version i at time t.

A consumer has two choices in the <sup>fi</sup>rst period: to buy the software or not. In the second period, those who bought in the <sup>fi</sup>rst period could either upgrade to the newer version or retain their old version. Those who did not buy in the <sup>fi</sup>rst period could either purchase the new version or remain inactive. Thus consumers can be thought of as obtaining one of four possible two-period bundles: $b _ { 4 } = \{ 1 , 2 \}$ with value $\nu ( s _ { 1 } , \theta , 1 ) + \gamma _ { \theta } \nu ( s _ { 2 } , \theta , 2 ) ; \ b _ { 3 } = \{ 1 , 1 \}$ with value $\nu ( s _ { 1 } , \theta , 1 ) + \gamma _ { \theta } \nu ( s _ { 1 } , \theta , 2 ) ; \ b _ { 2 } = \{ 0 , 2 \}$ with value $\gamma _ { \theta } \nu ( s _ { 2 } , \theta , 2 ) ;$ ; and $b _ { 1 } =$ {0,0} with value of 0. We'll assume that $\gamma _ { \theta } = \gamma$ for all .

Let us introduce an ordering on the bundles such that $b _ { 4 } > b _ { 3 } > b _ { 2 } > b _ { 1 }$ . Let $w ( b , \theta )$ represent the value of bundle b for customer θ, and $p ( b )$ be a consumer's total discounted cost of acquiring bundle b. We'll assume that the parameters of the value function $\nu ( \cdot )$ are such that consumers of higher types maximize their surplus by purchasing higher bundles. By setting $p ( b )$ as an appropriate increasing function, the seller will be able to maximize pro<sup>fi</sup>ts through second-degree price discrimination. Let θ denote a consumer who is indifferent between bundles $b _ { i }$ and $b _ { i + 1 } ,$ that is, for consumer $\theta _ { i } ,$ , the following equality holds: $w ( b _ { i + 1 } , \theta _ { i } ) - w ( b _ { i } , \theta _ { i } ) = p ( b _ { i + 1 } ) - p ( b _ { i } )$

We then have:

$$
\begin{array}{l} \theta_ {1} = \frac {p (b _ {2}) - \gamma \xi \left(Q _ {2} ^ {1} + Q _ {2} ^ {2}\right)}{\gamma s _ {2}}; \theta_ {2} = \frac {p (b _ {3}) - p (b _ {2}) + \xi \left(\gamma Q _ {2} ^ {2} - Q _ {1} ^ {1}\right)}{(1 + \gamma) s _ {1} - \gamma s _ {2}}; \\ \theta_ {3} = \frac {p (b _ {4}) - p (b _ {3}) - \gamma \xi Q _ {2} ^ {2}}{\gamma (s _ {2} - s _ {1})}. \end{array}\tag{19}
$$

We assume that consumer types are distributed on the interval $\theta \in \left[ \theta _ { 0 } , \theta _ { 4 } \right]$ , so that consumers in the interval $[ \theta _ { i - 1 } , \theta _ { i } )$ purchase bundle $b _ { i }$ where $i { \in } \{ 1 , 2 , 3 , 4 \}$ . To simplify further, we set $\theta _ { 0 } = 0 , \theta _ { 4 } = 1$ and assign consumer $\theta _ { 4 }$ to purchase the same bundle as $\theta _ { 3 } .$ Assuming uniform distribution of consumer types, $Q _ { t } ^ { i } ,$ the number of consumers who own version s<sub>i</sub> at time t, is given by

$$
Q _ {1} ^ {1} = 1 - \theta_ {2}; Q _ {2} ^ {1} = \theta_ {3} - \theta_ {2}; Q _ {2} ^ {2} = 1 - \theta_ {1} - Q _ {2} ^ {1}.\tag{20}
$$

Combining Eqs. (19) and (20), we solve for $\theta _ { 1 } , \theta _ { 2 } ,$ , and $\theta _ { 3 }$ in terms of $p ( b _ { 2 } ) , p ( b _ { 3 } )$ and $p ( b _ { 4 } )$ . Next, we <sup>fi</sup>nd the inverse demand function, where $D _ { i } { = } \theta _ { i } { - } \theta _ { i }$ denotes consumer demand for bundle $b _ { i } \mathrm { : }$ :

$$
\begin{array}{c} \left[ \begin{array}{c} p (b _ {4}) \\ p (b _ {3}) \\ p (b _ {2}) \end{array} \right] = \left[ \begin{array}{c} s _ {1} + \gamma s _ {2} \\ (1 + \gamma) s _ {1} \\ \gamma s _ {2} \end{array} \right] \\ - \left[ \begin{array}{c c c} s _ {1} - \xi + \gamma (s _ {2} - \xi) & (1 + \gamma) (s _ {1} - \xi) & \gamma (s _ {2} - \xi) \\ (1 + \gamma) s _ {1} - \xi & (1 + \gamma) (s _ {1} - \xi) & \gamma s _ {2} \\ \gamma (s _ {2} - \xi) & \gamma (s _ {2} - \xi) & \gamma (s _ {2} - \xi) \end{array} \right] \left[ \begin{array}{c} D _ {4} \\ D _ {3} \\ D _ {2} \end{array} \right]. \end{array}\tag{21}
$$

The manufacturer's decision problem can now be stated as selecting non-negative quantities $D _ { 4 } , D _ { 3 } ,$ and $D _ { 2 } ,$ which maximize the discounted two-period pro<sup>fi</sup>t, subject to $D _ { 2 } + D _ { 3 } + D _ { 4 } \leq 1$ . Inability to commit to second-period decisions at the beginning of period one would create additional constraints for the second-period optimization.

## 6. Strategic issues related to choice of prices, durability, and new product introduction

Having discussed modeling of the key elements of durable goods markets in the previous two sections, we now turn to the most important strategic issues facing players in these markets, especially those that are of interest to researchers in IS and OM. We brie<sup>fl</sup>y describe each of the issues, discuss some important results, and connect them back to the discussion in the last few sections to highlight the analytical approach and provide intuition behind these results. In the current section, we focus on strategic decisions at the <sup>fi</sup>rm level, while the next section will discuss issues at the level of the broader supply ecosystem.

## 6.1. Decisions on pricing and production over time

Pricing decisions for durable goods are complicated by the fact that prices over time are dynamically interconnected. Durable goods sellers not only need to consider the problem of equating marginal costs to current marginal revenue, but the anticipated effect of their choices on future marginal bene<sup>fi</sup>ts and costs as well. This implies that they have to think in terms of a dynamic price policy over the life cycle of the product, rather than a single price for the current period. Numerous factors, such as consumer behavior, demand patterns, technology evolution and R&D, the cost structure, cannibalization from secondary markets, control of aftermarkets, etc. can in<sup>fl</sup>uence the dynamic pricing policy and add to its complexity.

There is a rich tradition of dynamic pricing analysis in the OM literature. A good early example is Kalish [46], who studies the durable goods pricing problem in a diffusion context (Bass [7]), where the total stock (sales) of the durable good evolves over time, based on the pricing policy, word of mouth, and a saturation effect in the market. Pricing decisions over time are interlinked for a number of reasons. Demand in the current period affects future pro<sup>fi</sup>ts by in<sup>fl</sup>uencing future demand (through word of mouth and saturation effects) as well as future costs (through learning effects). The optimal dynamic pricing policy is determined by a complex interplay between these factors and can follow different trajectories. The most common optimal policy involves a price-skimming strategy on the part of the seller, although low introductory prices coupled with non-monotonic price trajectories may be optimal when the positive diffusion and learning effects are particularly strong.

Despite this rich dynamic pricing tradition, until recently, very little attention has been paid by OM researchers to the strategic purchasing behavior of consumers. Indeed Kalish [46] and most others (see Elmaghraby and Keskinocak [31] for a review of this literature) assume that consumers behave myopically. A myopic consumer makes a purchase decision based solely on current price and value, without considering future prices or product evolution. Strategic consumers, however, take these explicitly into account. As illustrated in Section 3.2, this signi<sup>fi</sup>cantly affects sellers' pricing strategies and market outcomes. Given their focus on incentives and strategic behavior, it is not surprising that economists were the <sup>fi</sup>rst to extensively study the dynamic pricing problems with strategic consumers.

Section 2 described the economic consequences of forwardlooking consumers, as <sup>fi</sup>rst discussed in Coase [24]. The strongest form of the Coase conjecture applies to an in<sup>fi</sup>nitely durable good, produced at a constant marginal cost, in a situation where price changes (and production) can be accomplished instantaneously [68]. In this case, the DGM is forced to sell the product at a price equal to what would be charged in a competitive market. Stokey [68], however, points out that a monopolistic seller can maintain some degree of commitment and therefore recover some pricing power if the time interval between price changes is positive. In a discrete <sup>fi</sup>nite-horizon setting, Besanko and Whinston [8] studied the optimal pricing policy of a DGM in the presence of rational, intertemporal utility maximizing consumers. They found that price skimming continues to be optimal even with strategic consumers. However, prices are lower than with myopic consumers. This <sup>fi</sup>nding is echoed in much of the literature.

A DGM's pricing and production decisions are also strongly in<sup>fl</sup>uenced by the production cost structure. One explanation for decreasing prices of durable goods, especially of IT products, is the decreasing marginal cost of production over time, either through scale or learning effects or through exogenous improvements in production technology. In the presence of declining costs, consumers' expectations of price declines are further strengthened, thereby expediting the convergence to competitive prices. Olsen [57] considers a model where production costs decrease over time due to learning by doing, so that marginal production cost is decreasing in Q(t), the cumulative production quantity. Olsen establishes the existence of a stationary equilibrium with a

DGM charging competitive prices in every time period. For the opposite case, Kahn [45] examines the monopoly production decisions in the case of increasing (quadratic) costs. Using a continuous time model of an in<sup>fi</sup>nitely durable good and assuming linear demand, Kahn shows that the DGM will spread production over time. While the total quantity produced by the DGM will eventually converge to the competitive quantity, the DGM will make positive pro<sup>fi</sup>ts and the quantity produced in each period will be less than that of a competitive producer. Driskill [29] extended Kahn's analysis by allowing the good to depreciate and showed that the monopoly production in this case will not converge to the competitive quantity, even in the steady state.

Pricing choices of durable-goods producers are further complicated by the need to simultaneously price older and newer versions of their products. This is particularly true for IT products, especially software, where older versions coexist in the market with newer versions for an extended period of time. We will discuss this issue in more detail in Section 6.3.

## 6.2. Choice of production technology

As seen in the previous subsection, cost of production is a crucial factor that affects strategic decisions of manufacturers. The great majority of the existing durable goods literature assumes negligible <sup>fi</sup>xed costs and constant variable costs. Examples include [8,16,17,24,60,68], and [40]. However, such an assumption can be an oversimpli<sup>fi</sup>cation. In some durable goods industries, e.g., software, the initial investment in R&D is signi<sup>fi</sup>cant, while the variable cost of production is negligible. Fixed initial development and capital costs are also non-negligible in most other durable goods. Further, marginal costs themselves often change with production quantity and time. An interesting question, especially from an operations perspective, is whether a DGM would deliberately choose a less ef<sup>fi</sup>cient technology, one with a higher average cost at the level of production, over an available alternative. Such a choice does not make sense for a monopolist producing non-durable goods, who faces a static problem. However, for a DGM faced with consumers with perfect foresight, such a choice might serve as a means to credibly commit to a lower level of output, thus mitigating the Coase problem (see for instance, Bulow [16]). Examples of such behavior are an artist destroying a printing plate, so that no more prints can be produced, or a luxury automobile producer making handmade cars instead of using mass-production techniques [47].

Choosing an inef<sup>fi</sup>cient technology can only be credible if consumers are not aware of the existence of more ef<sup>fi</sup>cient technologies or if switching from one technology to another is very costly. If the switch to a more-ef<sup>fi</sup>cient technology can be made at relatively low cost, then rational consumers will expect the DGM to switch to this more-ef<sup>fi</sup>cient technology in the future, eroding the credibility of its commitment. Given this lack of commitment power, it is not optimal for the DGM to adopt the inef<sup>fi</sup>cient technology in the <sup>fi</sup>rst place. Karp and Perloff [47] show this in a model with two different production technologies, both of which exhibit increasing marginal costs. They further show that if the buyers are only aware of the technology chosen by the DGM and not the other one (at least so long as the DGM's choices seem to be consistent with the publicly known technology), the DGM may <sup>fi</sup>rst adopt the less ef<sup>fi</sup>cient technology and keep the more ef<sup>fi</sup>cient technology a secret before switching to it at a later time.

## 6.3. Durability, planned obsolescence, and upgrading

Another important strategic variable that a durable goods seller controls is product durability, or the evolution of its service quality. The choice of durability by a DGM, and its economic optimality, was a signi<sup>fi</sup>cant theme in some of the earliest literature in this area. The general result is that a DGM chooses durability that is lower than the social optimum (see, for instance, [17] and [48]). That is, the goods break down or deteriorate in quality faster than the economically ef<sup>fi</sup>cient rate. This is because limiting durability is a way for the DGM to both mitigate the time-inconsistency problem and reduce competition (from older units) in the future by reducing their value.

To study the seller's choice of durability, [16,17,48,72], and [70] model variable production costs as a function of the product's built-in durability. In one of the earliest studies, Swan [72] analyzes the durability choices of a monopoly producer using two different models of durability. The <sup>fi</sup>rst one is the one-hoss shay model described in Eq. (2), where all goods fail after serving perfectly for a deterministic time period τ. Swan assumes that the variable cost of production c(τ) is increasing in the level of durability τ. The second model considers probabilistic deterioration of the durable product as described in Eq. (6). The variable production cost is assumed to be decreasing in the built-in deterioration rate d. Based on an analysis of these models, Swan found that a DGM makes ef<sup>fi</sup>cient choices, i.e., he chooses the same level of durability as a competitive producer. However, Bulow [17] later pointed out a <sup>fl</sup>aw in Swan's analysis, which relied on the DGM using strategies that were time-inconsistent. Limiting the DGM to time-consistent strategies, Bulow found that the DGM generally chose a lower level of durability than a competitive producer.

Schmalensee [66] and Su [70] consider maintenance choices as modeled in $\operatorname { E q . }$ (8). Consumer cost of maintenance, μ(d,t), is assumed to be increasing in both the product's age, t, and the built-in deterioration rate d. Both [66] and [70] conclude that the choices of durability and maintenance are linked to the market channel used by the seller. When the good is leased, the DGM internalizes the maintenance costs, and hence has an incentive to minimize the total cost (production and maintenance costs). When the good is sold, the seller generally chooses a higher deterioration rate, and consumers choose a higher level of maintenance. This latter situation is less economically ef<sup>fi</sup>cient.

An issue closely related to the choice of durability is that of the rate of introduction of new products. While introducing new products does not have a direct effect on the physical durability of existing products, it can potentially make the existing stock obsolete, i.e. make them less desirable. Thus we can make a distinction between physical obsolescence, which relates to a loss in functionality (the traditional notion of durability), and economic obsolescence, which is largely induced by the seller through the introduction of a newer version. A good example is the textbook market, where frequent introductions of newer editions obsolete used books. Such obsolescence is especially important in the case of IT products such as software and hardware, where their natural functional life typically far exceeds their actual usage. Older versions of the products are deliberately made obsolete through the introduction of newer versions that are not forward compatible with older versions.

The rapid progress in information technology over the last few decades and the frequent introduction of new and updated versions of products have drawn researchers' attention to the optimality of such planned obsolescence strategies. As discussed above, DGMs generally have an incentive to limit durability. With economic obsolescence, this takes the form of excessive upgrades and new product introductions as compared with the social optimum (for examples, see [21,30,65], and [76]). It is interesting to note that this happens despite the fact that consumers anticipate such upgrades and resist buying of the older version to some extent. This causes DGMs to lower prices in the initial period in an attempt to expand the market. However, the demand is still lower than the normal monopoly demand because the seller cannot credibly commit to curb its enthusiasm for upgrades.

Sankaranarayanan [65] proposes a solution to this commitment problem, called a Free New Version Rights (NVR) warranty. An NVR warranty provides consumers with the right to receive upgrades for free, thereby eliminating the commitment problem. The effect is similar to money-back guarantees (in the case of a future price drop) discussed in earlier literature.

The strategy of planned obsolescence is especially attractive to sellers of products that have strong network effects. Ellison and

Fudenberg [30] point out that consumer heterogeneity in the valuation of network effects provides the seller with added incentives for excessive upgrades beyond those driven by the usual commitment problem. Choi [21] introduces the possibility of price discrimination between new and existing customers (essentially providing a discount on upgrades) in a model with incompatible upgrades and network effects. He <sup>fi</sup>nds that, in the absence of price discrimination, a DGM has a low incentive to provide products in the initial period since rational consumers resist purchases in anticipation of the incompatible upgrades. Similar under-consumption in the <sup>fi</sup>rst period is also found in Levinthal and Purohit [49], who obtain the result even without incompatibility issues and network effects when the improvement of the new version over the old is suf<sup>fi</sup>ciently large. To mitigate the problem of under-consumption of the initial versions of product, Levinthal and Purohit [49] propose a buyback strategy, which results in higher pro<sup>fi</sup>ts. This is similar to the NVR warranty discussed earlier. Fudenberg and Tirole [35] provide a more thorough analysis of the pricing of newer generations of a durable good when facing anonymous, semianonymous, and identi<sup>fi</sup>able consumers and argue that price discrimination is an effective way to extract pro<sup>fi</sup>t in the presence of time inconsistency.

Departing from the usual results, Fishman and Rob [34] show that if the DGM is able neither to exercise planned obsolescence nor give discounts to repeat consumers, the investment in R&D is too low as compared with the social optimum. The DGM's R&D investment also depends on whether he sells or leases the product. Waldman [75] <sup>fi</sup>nds that time inconsistency causes a selling DGM to invest excessively in R&D and suggests that renting eliminates this problem, causing the excess investment to disappear. However, higher investments in R&D are optimal if it is desirable to completely eliminate the market for the older goods and move everyone to the upgrade through an appropriate leasing strategy. Choudhary [22] <sup>fi</sup>nds a similar result while comparing the leasing/selling strategies of a software monopolist and <sup>fi</sup>nds that the monopolist has a higher incentive to invest in quality improvements under leasing, since that enables him to move customers to the newer version more quickly.

Introduction of a new version of software is often characterized by signi<sup>fi</sup>cant R&D costs, while marginal production costs are negligible in comparison. Mehra and Seidmann in [52] investigate the optimal time interval between software upgrades using the obsolescence model described in Eq. (5). They focus on the trade-offs between two different costs. A shorter development time for the new version increases costs required to do “project crashing,” whereas a longer development time results in increased obsolescence and R&D costs. The potential market size is assumed to increase with each new version and asymptotically reach an exogenous upper limit. The overall <sup>fi</sup>xed development cost as a function of time is modeled as $C ( T ) =$ $C _ { R } T + C _ { c } / T ,$ where $C _ { c }$ and $C _ { R }$ are coef<sup>fi</sup>cients capturing the effects of crashing and increased obsolescence respectively. Mehra and Seidmann [52] <sup>fi</sup>nd that the pro<sup>fi</sup>t-maximizing time interval between versions increases as the market matures.

## 7. Strategic issues related to distribution and support

Having focused largely on the seller's choices in isolation in the previous section, we now turn our attention to the distribution strategies used by the seller and the seller's interactions with other market and supply chain participants. We'll start with a detailed comparison of the leasing and selling options and then consider the control of complementary goods markets and secondary markets. Finally, we will discuss channel design and the role of intermediaries.

## 7.1. Leasing versus selling directly to consumers

Another important conjecture, due to Coase [24], is that the problem of time inconsistency can be remedied if a DGM leases the product instead of selling it, as described in Section 3.2. Retaining ownership of the goods enables the DGM to internalize the externalities associated with future price drops, durability choices, and secondary markets. To compare the selling and leasing options, the selling price of a durable good can be modeled as a discounted sum of lease prices over the lifetime of the good:

$$
p _ {i} (t) = \sum_ {\tau = t} ^ {\infty} \gamma^ {\tau - t} r (s _ {i} (\tau), Q (\tau), \tau).\tag{22}
$$

Such a formulation might initially suggest that a producer should be indifferent between leasing and selling. Indeed, when a secondary market exists, consumers could create self-replicated leases by buying new goods from the producer and selling and buying used goods on the secondary market. However, the equality in Eq. (22) may not hold, due to a variety of frictions in the marketplace; thus one of these strategies may dominate the other. As shown in Section 3.2 (based on an example from [16]), when continued production increases total supply (i.e., previously produced goods do not stop functioning), leasing and selling lead to different production decisions, resulting in leasing being more pro<sup>fi</sup>table for a DGM. Indeed, the optimality of leasing is a common result in the literature, although leasing may not be feasible for all durable goods.

There is also empirical evidence that in many industries, even when leasing appears to be feasible, the practice of selling seems to dominate leasing. The question then arises as to what features of these industries and/or their products may be the drivers of such choice. Bucovetsky and Chilton [15] explore the strategic implications of leasing and selling in<sup>fi</sup>nitely durable goods and suggest that selling (or selling combined with leasing) is a strategy that can deter competitor entry. Their twoperiod model considers Cournot competition between the incumbent and the new entrant in the second period. Selling durable goods in the <sup>fi</sup>rst period increases the stock of goods in the second period, forcing the incumbent to be more aggressive in the second period. Bhatt [11] introduces demand uncertainty into the formulation and posits differences in risk-aversion between buyers and sellers. Bhatt shows that if a manufacturer is more risk-averse than consumers, the manufacturer prefers sales to leasing. Biehl [12] also considers demand uncertainty, where buyer valuation of a good can change stochastically, arguing that selling might dominate leasing when the consumer valuations change over time.

Epple and Zelenitz [32] show that selling may be preferred to leasing when leased goods deteriorate differently than sold goods. Rust [64] proposes that preference for selling over leasing is due to the existence of moral hazard problems in leasing contracts, whereby the producer is not able to incentivize renters to adequately maintain their units. Interestingly, Hendel and Lizzeri [41] <sup>fi</sup>nd that DGMs prefer leasing to selling because leasing alleviates the problem of information asymmetry in the second-hand market (as in Akerlof's paper [2]), while selling does not.

In some markets, leasing and selling coexist. Desai and Purohit [25] analyze how the leasing and selling decisions are affected by the presence of competition. They build a two-period setting in which two competing <sup>fi</sup>rms choose their actions simultaneously in each of the two periods. In the <sup>fi</sup>rst period, both <sup>fi</sup>rms choose the production quantities and percentages to lease. In the second period, both choose the production quantity for the second period. The demand is derived from individual valuations using the ideas discussed in Section 5. They <sup>fi</sup>nd that the fraction of leasing decreases as competition increases. They also <sup>fi</sup>nd that the proportion of leasing increases with product durability. In a setting where usage of durable goods requires access to complements created by another producer, Bhaskaran and Gilbert [9] <sup>fi</sup>nd that leasing and selling coexist, since selling encourages a larger supply of the complementary product. Huang et al. [43] explain the coexistence of selling and leasing through the introduction of economies of scale in selling used goods. In their model, selling used goods on the second-hand market is more expensive for retail consumers than for manufacturers. Leasing and selling facilitates second-degree price discrimination where the manufacturer leases the goods to the consumers with high willingness to pay and sells it to those with lower willingness to pay.

Information goods, especially software, are distributed using a number of strategies. Most mass-marketed software products, such as Microsoft Windows and Of<sup>fi</sup>ce, are distributed through perpetual licenses. These typically provide consumers the right to inde<sup>fi</sup>nite use of the software, and in that sense are similar to selling. Security software, mathematical software, and many databases are commonly licensed for use for a limited period of time only, usually a year. This subscription license strategy is similar to leasing. An extension of this leasing strategy that is gaining popularity is Software as a Service (SaaS), or cloud computing, wherein the seller not only provides access to the software but bundles it with use of the necessary complementary products such as hardware, storage, and support, typically accessed via the Internet. This is also sometimes referred to as pay-per-use. Secondary market is often not a feature of software products, while network effect normally is (see Varian [74]).

Choudhary et al. [23] explore the bene<sup>fi</sup>ts of leasing in a software market with delayed network effects. In their two-period model, leasing in the <sup>fi</sup>rst period expands the size of the user base, thereby increasing the network effect and consequently pro<sup>fi</sup>tability in the second period. Leasing can also improve pro<sup>fi</sup>tability in the presence of software piracy as shown by Jiang et al. [44]. In the case of piracy, the producer in essence is not a monopolist, since there are other sellers for the substitute product. Zhang and Seidmann [78] examine hybrid leasing and selling strategies for a monopoly software producer. They assume that the producer does not have a commitment problem and that there is no second-hand market for used software, but owners of the old software version can buy the new version at a discount (upgrade pricing). Zhang and Seidmann show that a hybrid strategy can be used for second-degree price discrimination. Furthermore, they consider two drivers of the licensing policy: the strength of the network effects and the uncertainty about the quality of the improved version produced in the second period. They show that leasing increases with increased uncertainty about the quality of the future version, but strong network effects increase the importance of sales.

## 7.2. Control of aftermarket complements and maintenance

Compatible complementary goods and services such as consumable supplies, maintenance, and replacement parts are a key component of the value proposition for many durable goods. Markets for these goods and services are referred to as aftermarkets, and their control is an important strategic consideration for DGMs. An important decision in this regard is whether or not to attempt to monopolize the aftermarket. One way a DGM can monopolize the aftermarket is by speci<sup>fi</sup>cally designing the durable goods to be compatible only with complementary goods or supplies offered by the manufacturer. Given the durable investment in the primary good, the buyers are effectively “locked-in” to the seller.<sup>5</sup>

There is a tradeoff in pursuing an aftermarket monopolization strategy. On the one hand, locking out competitors enables the DGM to extract additional surplus from the sale of complementary goods. On the other hand, consumers' willingness to pay for the durable good itself is adversely affected by their fear of lock-in. Gilbert and

Jonnalagedda [38] analyze the conditions under which a DGM should monopolize the complementary goods market and <sup>fi</sup>nd a relationship with consumer heterogeneity over complementary good values. With homogenous consumers, monopolization is not optimal. As consumer heterogeneity increases, aftermarket monopolization becomes the optimal strategy. To parameterize consumer heterogeneity, they model the distribution of consumer types using a uniform distribution over $\theta \in [ 1 - \delta , 1 + \delta ]$ , where the magnitude of δ captures the degree of consumer heterogeneity.

The intuition behind their result is that control of the aftermarket provides the DGM with an effective price discrimination tool, with higher-value consumers demanding larger quantities of the aftermarket products. Thus, the DGM can avoid the Coase problem to some extent by selling the durable good at a low price while making most of his rents from the tied aftermarket products. The low price takes away the incentive for consumers to postpone purchases in anticipation of a future price drop.

When the complementary good is itself a durable good with periodic upgrades, the seller of the primary durable good has a larger incentive to monopolize the aftermarket. Even when consumers are homogenous, Carlton and Waldman [19] show that monopolizing the complementary good market in the <sup>fi</sup>rst period can help the DGM of an essential primary durable good capture pro<sup>fi</sup>ts associated with upgrade sales of complementary goods in the second period, especially when the complementary goods offered by alternative producers are superior. Control of durable complementary goods through compatibility choices is also bene<sup>fi</sup>cial to sellers of the primary durable good, since consumer investments in compatible durable complements create switching costs for them. For instance, consumers' investments in compatible application software create a switching cost in migrating to a different operating platform, thereby increasing the pricing power of the platform producer.

The question of aftermarket monopolization has also been examined from a social perspective, especially in the context of maintenance as an aftermarket offering (e.g., [20,54,66,70]). In these papers, the interaction between the seller and consumers is generally modeled as a two-stage game where the seller <sup>fi</sup>rst chooses durability and prices for the new product sale and/or lease and maintenance. Consumers then buy or lease the new product and decide how much maintenance to purchase. The maintenance market could be competitive ([66] and [70]) or be solely monopolized by the seller ([54] and [20]). With a competitive maintenance sector, the broad result is that when the DGM sells the product, consumers spend inef<sup>fi</sup>ciently high amounts on maintenance as compared to the social optimum. This is because the DGM cannot pro<sup>fi</sup>t in the competitive maintenance market, and hence sells the durable good at a price higher than marginal costs. This causes the consumers to overspend on maintenance, seeking to prolong the use of their product rather than to buy a replacement product, a strategy that could be more ef<sup>fi</sup>cient from a social perspective. This inef<sup>fi</sup>ciency can be eliminated if the producer monopolizes the aftermarket for maintenance or leases the product instead of selling it. Leasing can, however, create moral hazard problems if the consumer (rather than the seller who retains ownership of the product) has to pay for maintenance.

## 7.3. Secondary markets and adverse selection

Given their extended durability, many used durable goods such as cars, appliances, and books are traded on secondary markets.<sup>6</sup> While the quality of new products can often be readily gauged by consumers, the quality of used products can vary greatly and may be dif<sup>fi</sup>cult or costly to assess. This leads to information asymmetry; the sellers know the quality better than the buyers do. In a seminal paper, Akerlof [2] linked this information asymmetry to the problem of adverse selection and consequent market inef<sup>fi</sup>ciency. With adverse selection, goods of lower quality tend to crowd out goods of higher quality and, without credible quality signals (such as warranties, certi<sup>fi</sup>cations, or reputation), the level of trade is suboptimal.

Secondary markets can be bene<sup>fi</sup>cial to DGMs since the option to sell a used good increases the value of the new good to consumers. However, they also create an alternative channel for the distribution of durable goods, thereby leading to increased competition and further complicating the pricing decisions of sellers. This sometimes provides an incentive for DGMs to try to control, and in some cases even monopolize, the secondary markets for their products. Bulow [16], Stokey [68], and other early papers considered the existence of secondary markets but did not speci<sup>fi</sup>cally focus on the interaction between the two markets. Instead, they speci<sup>fi</sup>ed reduced form inverse demand functions that depended on the stock of durable goods of different vintages available in the market. Later research extended this to study individual purchase and trading behaviors, resulting in the allocation of consumers into distinct segments that bought either new or used goods (e.g., Porter and Sattler [60]). The growing popularity of Internet-based secondary markets, such as eBay and Amazon, has made this an active area of research for IS researchers interested in channel choice, market ef<sup>fi</sup>ciency, and its impact on the pro<sup>fi</sup>tability of new goods (e.g., [36,77]).

Given their popularity and promise of ef<sup>fi</sup>ciency, it is natural to consider the impact of electronic secondary markets on producer and consumer surpluses. Arunkundram and Sundararajan [3] show, using a simple one-period model, that these secondary markets are generally bene<sup>fi</sup>cial to both producers and consumers. The availability of ef<sup>fi</sup>cient secondary markets enables high value consumers to dispose of used (quality deteriorated) products in the secondary market and trade up to new ones, while consumers with lower valuations, who would otherwise have been priced out of the market, gain access to the used goods. Some empirical evidence for this is provided by Ghose et al. [37] in the context of the used-book market on Amazon.

Other studies such as Ghose et al. [36] and Yin et al. [77], while generally supporting these <sup>fi</sup>ndings, highlight the effect of control on pro<sup>fi</sup>tability and product upgrades. When the producer of the durable good does not control the secondary market for the good (as is true of most Internet-based secondary markets), incentive misalignment between the primary producer and the intermediary who controls the secondary market might make these markets less attractive to the producers. Yin et al. [77] <sup>fi</sup>nd that when an intermediary controls the secondary market, a DGM upgrades products less frequently than in a purely peer-to-peer secondary market.

While secondary markets have traditionally been of rather limited interest to researchers in OM, the recent emphasis on sustainability and the accompanying issues related to reverse logistics and remanufacturing (also called closed-loop manufacturing) have brought some focus to the problem. Re-manufacturing introduces a new source of competition for a DGM and further complicates its choices with respect to durability and product design. See [5] for reviews of this literature, which is still evolving.

## 7.4. Channel design and the role of intermediaries

Intermediaries play an important role in many durable goods markets. For instance, in the automobile market, vehicles are distributed to consumers through numerous dealerships and rental agencies, giving rise to a multi-echelon supply chain. Supply chain performance and, in particular, contracts that coordinate supply chains and allow for arbitrary division of pro<sup>fi</sup>ts have been of signi<sup>fi</sup>cant interest to the OM community (see Cachon [18]). Of particular interest in the durable goods literature is the notion that independent supply chain intermediaries can help a DGM mitigate the commitment problem.

Desai et al. [26] suggest that strategic decentralization through the addition of a retailer in the distribution channel can help DGMs mitigate problems related to time inconsistency. They consider a two-period setting, where a DGM sells durable goods through a retailer using a two-part contract. Desai et al. identify a strategy that solves both the channel coordination and the time inconsistency problems. In this strategy, at the beginning of the <sup>fi</sup>rst period, the DGM writes a contract with the retailer specifying a <sup>fi</sup>xed fee and wholesale prices covering both periods. This explicit contracting enables the seller to get around the commitment problem. The wholesale price set by the DGM is higher than marginal cost in both periods (unlike in the case of nondurable goods). By committing contractually not only to a speci<sup>fi</sup>c <sup>fi</sup>xed fee but also to speci<sup>fi</sup>c wholesale prices, the manufacturer induces the retailer to choose the same quantities as a leasing DGM. Su and Zhang [71] arrive at a similar conclusion with respect to the DGM's ability to indirectly commit through a decentralized supply chain. Arya and Mittendorf [4] extend Desai et al. [26] to an n-period setting without explicit retailer contracts and show that the arrangement can still mitigate the commitment problem, due to increased wholesale prices arising from double marginalization.

Researchers have also examined how leasing and selling choices are affected by intermediaries. Bhaskaran and Gilbert [10] in extending [61] consider a setting in which a DGM can reach the end consumers through multiple channels. They use a two-period model where goods do not deteriorate. The DGM can lease products to a dealer (or a group of competitive dealers), who then lease the product to the end consumers. The DGM can alternatively sell the products to a dealer (or a group of dealers) who can choose between selling and leasing the products to end consumers. Bhaskaran and Gilbert show that when the DGM uses competitive dealers, the DGM prefers leasing to sales. In the case of a single dealer, the DGM prefers to sell to the dealer who then tends to choose to lease to end consumers. Leasing mitigates time-inconsistency, but selling mitigates the effect of double marginalization.

Purohit and Staelin [63], and Purohit [62] examine how the presence of intermediaries and the used goods market affects durable goods supply chains. They analyze the historical interactions in the automobile rental and retail markets in a setting with a two-echelon supply chain consisting of a DGM, a rental agency, a dealer, and two independent consumer groups that only rent and purchase respectively. Rental agencies keep used cars in the separate channel con<sup>fi</sup>guration. Overlapping channel con<sup>fi</sup>guration allows rental agencies to sell used rental cars in the retail market. In the buyback channel con<sup>fi</sup>guration, the manufacturer buys back used cars from rental agencies and sells them to dealers who then sell them in the retail market. Purohit et al. <sup>fi</sup>nd that the DGM's pro<sup>fi</sup>t is highest under the overlapping channel structure due to competition between the rental agency and the dealer. They also posit that the buyback channel could increase channel ef<sup>fi</sup>- ciency by reducing con<sup>fl</sup>ict between the rental agency and the dealer.

## 8. Discussion: future research directions

The past decade has seen a growing interest by the OM and IS communities in understanding how producers of durable goods (including information goods) are affected by consumers' strategic behaviors. Much of the relevant early model-based research was done by economists, and we have reviewed the most common models and results in this literature. Much of this work sought to explain key tradeoffs in the strategies pursued by producers and evaluate the impact of their strategies on social welfare.

Many results and recommendations in the literature are quite sensitive to the underlying assumptions. For example, an early conjecture that a DGM will pursue leasing rather than selling has held up under some assumptions, but mixed selling and leasing strategies have been shown to be superior in other circumstances ([9,15,43]). A particularly troubling fact is that the vast majority of model-based durable goods research assumes that the producer is a monopolist. Even though monopoly analysis can produce valuable insights [76], and many durable goods markets have dominant players, clearly the robustness of the results and their applicability to real-world contexts will be enhanced signi<sup>fi</sup>cantly through a systematic consideration of the effects of competition. The paucity of such work hints at the challenges in incorporating it as well as the importance of the contribution represented by overcoming these challenges. While a strong focus on monopoly situations might be understandable for economists focusing on legal, antitrust, and policy considerations, it is much more limiting when studying issues of interest to IS and OM scholars, such as inventory, product development, and channel considerations.

Another aspect that has received little attention in the durable goods literature is demand uncertainty. There is clear empirical evidence [6] that economic volatility affects consumer demand. Many durable goods are <sup>fi</sup>nitely durable and are made to stock rather than made to order. For producers who deal with replacement sales, technical obsolescence, strategic consumers, or economic uncertainty, it is important to understand which inventory, pricing, and production strategies should be pursued to maximize pro<sup>fi</sup>ts over extended time horizons and to manage the accompanying risk. OM and IS scholars, with their deep training in formulating and analyzing dynamic stochastic models, are particularly well equipped to take on this challenge.

The interaction between DGMs and complementary goods manufacturers is another area of immense promise, especially when one goes beyond the narrow area of pricing power and rent extraction. Most durable goods, especially information goods, operate in ecosystems with large numbers of complements. How then should producers of different complements ef<sup>fi</sup>ciently coordinate innovation to maximize overall system value? For instance, is it more ef<sup>fi</sup>cient for a single player to control upgrades across system components or is it better to facilitate this through explicit or implicit market relationships? The question takes on added signi<sup>fi</sup>cance in the context of the developing ecosystems for mobile technology and cloud computing.

An extensive OM supply chain literature (see Cachon [18]) has studied contracts between wholesalers and retailers that coordinate the supply chain from a pro<sup>fi</sup>t/ef<sup>fi</sup>ciency perspective. However, very few of these speci<sup>fi</sup>cally consider durable goods or strategic consumers. We believe there are extensive opportunities for future work in this area. To start with, it will be very instructive to document the nature of these contracts in durable goods markets and how they differ from those described in the more traditional literature. Further the contracts can be examined more carefully to understand which aspects of them are designed to solve durable-good-speci<sup>fi</sup>c problems, such as the various commitment problems or aftermarket control.

To our knowledge, empirical examinations of durable goods markets are scarce in the OM and IS <sup>fi</sup>elds. The little work that has been done has focused on validating some of the assumptions in this literature, such as consumer foresight [53] and the existence of network effects [14]. However, there has been a recent trend of adopting empirical studies in OM research, especially in marketing-adjacent studies. Recent articles by Ghose et al. [36], Yin et al. [77], and others have included empirical studies to support their theoretical results. Additional empirical studies are needed to understand consumer behavior better and verify earlier theoretical results, e.g., to understand drivers of consumers' preferences for leasing versus buying and to test results, such as the frequency of product upgrades and the consequences of aftermarket monopolization. Such questions present particularly promising opportunities for cross-disciplinary empirical work.

## References

[1] V. Agrawal, S. Kavadias, B. Toktay, Design and introduction of conspicuous durable products, Working Paper, Georgia Institute of Technology, 2009.

[2] G. Akerlof, The market for ‘lemons’: quality uncertainty and the market mechanism, Ouarterly Journal of Economics 84 (3) (1970) 488–500

[3] R. Arunkundram, A. Sundararajan, An economic analysis of electronic secondary markets: installed base, technology, durability and <sup>fi</sup>rm pro<sup>fi</sup>tability, Decision Support Systems 24 (1) (1998) 3–16.

[4] A. Arya, B. Mittendorf, Bene<sup>fi</sup>ts of channel discord in the sale of durable goods, Marketing Science 25 (1) (2006) 91–96.

[5] A. Atasu, V. Guide Jr., L. Wassenhove, Product reuse economics in closed loop supply chain research, Production and Operations Management 17 (5) (2008) 483–496.

[6] W.B. Barrett, M.B. Slovin, Economic volatility and the demand for consumer durables, Applied Economics 20 (6) (1988) 731–738.

[7] F.M. Bass, A new product growth for model consumer durables, Management Science 15 (5) (1969) 215–227.

[8] D. Besanko, W.L. Winston, Optimal price skimming by a monopolist facing rational consumers, Management Science 36 (5) (1990) 555–567.

[10] S.R. Bhaskaran, S.M. Gilbert, Implications of channel structure for leasing or selling durable goods, Marketing Science 28 (5) (2009) 918–934.

[11] S. Bhatt, Demand uncertainty in a durable goods monopoly, International Journal of Industrial Organization 7 (3) (1989) 341–355.

[12] A.R. Biehl, Durable-goods monopoly with stochastic values, The RAND Journal of Economics 32 (3) (2001) 565–577.

[13] E.W. Bond, L. Samuelson, Durable good monopolies with rational expectations and replacement sales, The RAND Journal of Economics 15 (3) (1984) 336–345.

[14] E. Brynjolfsson, C.F. Kemerer, Network externalities in microcomputer software: an econometric analysis of the spreadsheet market, Management Science 42 (12) (1996) 1627–1647.

[15] S. Bucovetsky, J. Chilton, Concurrent renting and selling in a durable-goods monopoly under threat of entry, The Rand Journal of Economics 17 (2) (1986) 261–275.

[16] J. Bulow, Durable-goods monopolists, Journal of Political Economy 90 (2) (1982) 314–332.

[17] J. Bulow, An economic theory of planned obsolescence, Quarterly Journal of Economics 101 (4) (1986) 729–750.

[18] G.P. Cachon, Supply chain coordination with contracts, Handbooks in operations research and management science, 11, 2003, pp. 229–340.

[19] D.W. Carlton, M. Waldman, Tying, Upgrades, and Switching Costs in Durable-Goods Markets, National Bureau of Economic Research, Cambridge, Mass., USA, 2005.

[20] D.W. Carlton, M. Waldman, Competition, monopoly, and aftermarkets, Journal of Law, Economics, and Organization 26 (1) (2009) 54–91.

[21] J.P. Choi, Network externality, compatibility, and planned obsolescence, The Journal of Industrial Economics 42 (2) (1994) 167–182.

[22] V. Choudhary, Comparison of software quality under perpetual licensing and software as a service, Journal of Management Information Systems 24 (2) (2007) 141–165.

[23] V. Choudhary, K. Tomak, A. Chaturvedi, Economic bene<sup>fi</sup>ts of renting software, Journal of Organizational Computing and Electronic Commerce 8 (4) (1998) 277–305.

[24] R.H. Coase, Durability and monopoly, Journal of Law and Economics 15 (1) (1972) 143–149.

[25] P.S. Desai, D. Purohit, Competition in durable goods markets: the strategic consequences of leasing and selling, Marketing Science 18 (1) (1999) 42–58.

[26] P.S. Desai, O. Koenigsberg, D. Purohit, Strategic decentralization and channel coordination, Quantitative Marketing and Economics 2 (1) (2004) 5–22.

[27] P.S. Desai, O. Koenigsberg, D. Purohit, Research note—the role of production lead time and demand uncertainty in marketing durable goods, Management Science 53 (1) (2007) 150–158.

[28] A. Dhebar, Durable-goods monopolists, rational consumers, and improving products, Marketing Science 13 (1) (1994) 100–120.

[29] R. Driskill, Durable goods monopoly, increasing marginal cost and depreciation, Economica 64 (253) (1997) 137–154.

[30] G. Ellison, D. Fudenberg, The neo-Luddite's lament: excessive upgrades in the software industry, The Rand Journal of Economics 31 (2) (2000) 253–272.

[31] W. Elmaghraby, P. Keskinocak, Dynamic pricing in the presence of inventory con siderations: research overview, current practices, and future directions, Management Science 49 (10) (2003) 1287–1309.

[32] D. Epple, A. Zelenitz, Consumer durables: product characteristics and marketing policies, Southern Economic Journal 44 (2) (1977) 277–287.

[33] J. Farrell, P. Klemperer, Coordination and lock-in: competition with switching costs and network effects, Handbook of industrial organization, 3, 2007, pp. 1967–2072.

[34] A. Fishman, R. Rob, Product innovation by a durable-good monopoly, The RAND Journal of Economics 31 (2) (2000) 237–252.

[35] D. Fudenberg, J. Tirole, Upgrades, tradeins, and buybacks, The Rand Journal of Economics 29 (2) (1998) 235–258.

[36] A. Ghose, R. Telang, R. Krishnan, Effect of electronic secondary markets on the supply chain, Journal of Management Information Systems 22 (2) (2005) 91-120

[37] A. Ghose, M.D. Smith, R. Telang, Internet exchanges for used books: an empirical analysis of product cannibalization and welfare impact, Information Systems Research 17 (1) (2006) 3–19.

[38] S.M. Gilbert, S. Jonnalagedda, Durable Products, Time Inconsistency, and Lock-In, 2010.

[39] G.E. Goering, Durability choice under demand uncertainty, Economica 60 (240) (1993) 397–411.

[40] G.E. Goering, M.K. Pippenger, Dynamic consistency and monopoly, Atlantic Economic Journal 31 (2) (2003) 188–194.

[41] I. Hendel, A. Lizzeri, The role of leasing under adverse selection, Journal of Political Economy 110 (1) (2002) 113–143.

[42] R.A. Howard, J.E. Matheson, In<sup>fl</sup>uence diagrams, Readings on the Principles and Applications of Decision Analysis, 2, 1981, pp. 721–762.

[43] S. Huang, Y. Yang, K. Anderson, A theory of <sup>fi</sup>nitely durable goods monopoly with used-goods market and transaction costs, Management Science 47 (11) (2001) 1515–1532.

[44] B. Jiang, P.-Y. Chen, T. Mukhopadhyay, Software licensing: pay-per-use versus perpetual, Working Paper, Tepper School of Business, Carnegie Mellon University, 2007.

[45] C. Kahn, The durable goods monopolist and consistency with increasing costs, Econometrica 54 (2) (1986) 275–294.

[46] S. Kalish, Monopolist pricing with dynamic demand and production cost, Marketing Science 2 (2) (1983) 135–159.

[47] L. Karp, J. Perloff, The optimal suppression of a low-cost technology by a durablegood monopoly, The Rand Journal of Economics 27 (2) (1996) 346–364.

[48] D. Levhari, T.N. Srinivasan, Durability of consumption goods: competition vs. monopoly, The American Economic Review 59 (1) (1969) 102–107.

[49] D.A. Levinthal, D. Purohit, Durable goods and product obsolescence, Marketing Science 8 (1) (1989) 35–56.

[50] E. Maskin, J. Riley, Monopoly with incomplete information, The Rand Journal of Economics 15 (2) (1984) 171–196.

[51] E. Maskin, J. Tirole, Markov perfect equilibrium, I: observable actions, Journal of Economic Theory 100 (2) (2001) 191–219.

[52] A. Mehra, A. Seidmann, Optimal timing of upgrades over a software product's life cycle, Working Paper, Simon Graduate School of Business, University of Rochester, 2008.

[53] O. Melnikov, Demand for differentiated durable products: the case of the U.S. computer printer industry, Working Paper, Yale University, 2001.

[54] H. Morita, M. Waldman, Durable goods, monopoly maintenance, and time inconsistency, Journal of Economics and Management Strategy 13 (2) (2004) 273–302.

[55] M. Mussa, S. Rosen, Monopoly and product quality, Journal of Economic Theory 18 (2) (1978) 301–317.

[56] H. Nair, Intertemporal price discirmination with forward-looking consumers: application to the US market for console video-games, Quantitative Marketing and Economics 5 (3) (2007) 239–292.

[57] T. Olsen, Durable goods monopoly, learning by doing and the Coase conjecture, European Economic Review 36 (1) (1992) 157–177.

[58] B.Y. Orbach, The durapolist puzzle: monopoly power in durable-goods markets, Yale Journal on Regulation 21 (1) (2004) 67–119.

[59] W. Pesendorfer, Design innovation and fashion cycles, The American Economic Review 85 (4) (1995) 771–792.

[60] R.H. Porter, P. Sattler, Patterns of trade in the market for used durables: theory and evidence, NBER Working Paper, 1999, p. W7149.

[61] D. Purohit, Marketing channels and the durable goods monopolist: renting versus selling reconsidered, Journal of Economics and Management Strategy 4 (1) (1995) 69–84.

[62] D. Purohit, Dual distribution channels: the competition between rental agencies and dealers, Marketing Science 16 (3)(1997) 228–245

[63] D. Purohit, R. Staelin, Rentals, sales, and buybacks: managing secondary distribution channels, Journal of Marketing Research 31 (3) (1994) 325–338.

[64] J. Rust, When is it optimal to kill off the market for used durable goods? Econometrica: Journal of the Econometric Society 54 (1) (1986) 65–86.

[65] R. Sankaranarayanan, Innovation and the durable goods monopolist: the optimality of frequent new-version releases, Marketing Science 26 (6) (2007) 774–791.

[66] R. Schmalensee, Market structure, durability, and maintenance effort, The Review of Economic Studies 41 (2) (1974) 277–287.

[67] I. Song, P.K. Chintagunta, A micromodel of new product adoption with heterogeneous and forward-looking consumers: application to the digital camera category, Quantitative Marketing and Economics 1 (4) (2003) 371–407.

[68] N.L. Stokey, Rational expectations and durable goods pricing, Bell Journal of Eco nomics 12 (1) (1981) 112–128

[69] R. Strotz, Myopia and inconsistency in dynamic utility maximization, The Review of Economic Studies 23 (3) (1955) 165–180.

[70] T. Su, Durability of consumption goods reconsidered, The American Economic Review 65 (1) (1975) 148–157.

[71] X. Su, F. Zhang, Strategic customer behavior, commitment, and supply chain performance, Management Science 54 (10) (2008) 1759–1773.

[72] P. Swan, Durability of consumption goods, The American Economic Review 60 (5) (1970) 884–894.

[73] V. Tilson, Y. Wang, W. Yang, Channel strategies for durable goods: coexistence of selling and leasing to individual and corporate consumers, SSRN eLibrary, 2007.

[74] H.R. Varian, Buying, sharing and renting information goods, The Journal of Industrial Economics 48 (4) (2000) 473–488.

[75] M. Waldman, Planned obsolescence and the R&D decision, The Rand Journal of Economics 27 (3) (1996) 583–595.

[76] M. Waldman, Durable goods theory for real world markets, Journal of Economic Perspectives 17 (1) (2003) 131–154.

[77] S. Yin, et al., Durable products with multiple used goods markets: product upgrade and retail pricing implications, Marketing Science 29 (3) (2010) 540–560.

[78] J. Zhang, A. Seidmann, Perpetual versus subscription licensing under quality uncertainty and network externality effects, Journal of Management Information Systems 27 (1) (2010) 39–68.

Ravi Mantena is an Assistant Professor of Computers and Information Systems at the Simon School, University of Rochester. His research studies the economics of technolog markets.

Vera Tilson is an Assistant Professor at the Simon Graduate School of Business, Univer sity of Rochester. Her research interests include decision making models in operations management and healthcare.

Xiaobo Zheng is a Ph.D. Candidate in Operations Management at the Simon Graduate School of Business, University of Rochester. His research interests include supply chain management, decision making models and queueing systems.
