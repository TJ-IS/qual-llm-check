---
otero_id: 7512
otero_key: "P8E6DJJ8"
title: "A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation"
authors: "Zhiling Guo; Gary J. Koehler; Andrew B. Whinston"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0366"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/P8E6DJJ8/fulltext/images/bf7282a2d451fbe2e7fc6c55670f536fc413f0c6e5549e7f04aa732cab410c40.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation

Zhiling Guo, Gary J. Koehler, Andrew B. Whinston,

To cite this article:

Zhiling Guo, Gary J. Koehler, Andrew B. Whinston, (2012) A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation. Information Systems Research 23(3-part-1):823-843. http://dx.doi.org/10.1287/ isre.1110.0366

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/P8E6DJJ8/fulltext/images/c3940d59b587ce384eab73bc3cb04dd30e12aea46a33e0918efc7203949fde9b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation

Zhiling Guo

Department of Information Systems, College of Business, City University of Hong Kong, Kowloon, Hong Kong, zhiling.guo@cityu.edu.hk

Gary J. Koehler

Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611, koehler@ufl.edu

Andrew B. Whinston

Department of Information, Risk, and Operations Management, McCombs School of Business, The University of Texas at Austin, Austin, Texas 78712, abw@uts.cc.utexas.edu

nline auction markets play increasingly important roles for resource allocations in distributed systems. This paper builds upon a market-based framework presented by Guo et al. (Guo, Z., G. J. Koehler, A. B. Whinston. 2007. A market-based optimization algorithm for distributed systems. Management Sci. 53(8) 1345–1458), where a distributed system optimization problem is solved by self-interested agents iteratively trading bundled resources in a double auction market run by a dealer. We extend this approach to a dynamic, asynchronous Internet market environment and investigate how various market design factors including dealer inventory policies, market communication patterns, and agent learning strategies affect the computational market efficiency, market liquidity, and implementation. We prove finite convergence to an optimal solution under these various schemes, where individual rational and budget-balanced trading leads to an efficient auction outcome. Empirical investigations further show that the algorithmic implementation is robust to a number of dealer and agent manipulations and scalable to larger sizes and more complicated bundle trading markets. Interest ingly, we find that, though both asynchronous communication and asymmetric market information negatively affect the speed of market convergence and lead to more agent welfare loss, agents’ ability to predict market prices has a positive effect on both. Contrary to conventional wisdom that a dealer’s intertemporal liquidity provisions improve market performance, we find that the dealer’s active market intervention may not be desirable in a simple market trading environment where an inherent market liquidity effect dominates, especially when the dealer owns a significant amount of resources. Different from the traditional market insight, our trading data suggest that high trading volume does not correlate to low price volatility and quicker price discovery.

Key words: electronic markets and auctions; electronic commerce; resource allocation; computational experiment; simulation

History: Ram Gopal, Senior Editor; Gediminas Adomavicius, Associate Editor. This paper was received on June 4, 2009, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance June 23, 2011, and updated January 5, 2012.

## 1. Introduction

The increasing use of the Internet as a standard computing platform has created many types of distributed systems within and across organizational boundaries. One example is a global hierarchical organization consisting of geographically distributed divisions. The central headquarters governs the total shared resources available to the whole organization (resources such as total computing capacity, storage space, inventory, and manpower). Division managers who have precise knowledge of local conditions run different plants possibly located in various countries. The central planner must decide on an allocation of the shared resources that will minimize the overall operating costs. However, division managers may not have incentives to truthfully share their private information about local plant operations (Ba et al. 2001a). As a result, an optimal centralized solution is simply impractical to attain under such conditions.

Recent trends in supply chains and e-marketplaces require distributed decision making in collaborative planning environments such as e-procurement and supply chain coordination (Albrecht 2009). Typical characteristics of such distributed systems include global goals that depend on some common activities of decentralized parties and unique problems with private objective functions that are managed locally. The need for disclosing potentially confidential information by decentralized parties, the conflict of central objectives with the incentives in decentralized entities, and the complex interaction among participating parties pose critical limitations in practical implementations for such intra- and interorganizational planning and coordination.

It has been widely recognized that such resource allocation challenges can be effectively handled by market mechanisms. Neoclassical economics theories such as the Walrasian general equilibrium model provide a theoretical foundation to study the exchange and allocation of resources in an economy. The first and second fundamental theorems of welfare economics state the conditions under which a Walrasian equilibrium (price equilibrium with transfers) leads to a Pareto optimal allocation (no alternative allocation that makes at least one individual better off without making any other individual worse off, or vice versa). These theorems offer a strong conceptual affirmation of the use of competitive markets in distributed resource allocation.

However, applying these theoretical results to practical market implementations has several important limitations (Mas-Colell et al. 1995, pp. 556–557). The most critical one is that a planning authority must have sufficiently good information. For example, the authority must know the statistical joint distribution of preferences, endowments, and other relevant characteristics of the agents. Perfectly observing each individual’s private characteristics is simply impractical. Secondly, the Pareto optimality properties of the neoclassical theories only imply the existence of competitive market equilibrium prices. Lack of understanding of the underlying dynamics that drive the equilibrium market prices is another obstacle for practical implementation of such markets. In this paper, we propose a market-based resource allocation mechanism that does not rely on complete information revelation from agents. We further develop a computational market model to study several key market design factors that affect the dynamic price formation process.

Market designs that take into account the relevant physical and economical aspects of the allocation problem belong to the general category of “smart market” design (see McCabe et al. 1991 for an overview). A smart market is a periodic auction that incorporates domain-specific constraints in the market clearing mechanism and is cleared by operations research techniques such as linear programming. Combinatorial auctions are smart markets in which goods are indivisible. Well-known examples include the Federal Communications Commission’s auction of radio spectrum licenses (Cramton 1997), sales of airport time slots (Rassenti et al. 1982), and allocation of delivery routes (Sheffi 2004). In such situations, bundle trading allows bidders to submit consolidated orders to sell/buy packages of assets when complementarities exist between different items. Combinatorial auctions are generally one-sided auctions in which the auctioneer acts as a seller and participants buy complementary assets from the auctioneer. Other smart markets for divisible goods such as electricity (Hogan et al. 1996), natural gas (McCabe et al. 1990), and water resources (Raffensperger et al. 2009) are becoming very important in environmental areas. Usually these markets are organized as two-sided auctions so that buyers and sellers can trade simultaneously in the exchange. However, typically only a single commodity is traded in such double auction markets.

In real world markets, energy exchanges such as electricity trading represent some of the most actively traded markets in the world. In the electricity market, complementarities arise between deliveries of electricity energy in consecutive periods because of startup and shutdown costs of power plants. To account for such complementarities, the European Energy Exchange organizes a system of interlinked, interdependent markets on which electricity can be traded with various time horizons. For example, in the day ahead auction, both hourly contracts and block contracts (a combination of consecutive hourly orders) for the respective next day can be traded.<sup>1</sup> The auctions can be described as multiunit, double-sided combinatorial auctions. Computational complexity and trade inefficiency are well-documented problems in such markets and are inherent in the combinatorial auction design. Despite its practical significance, integrating bundle trading within a double auction is a relatively unexplored research area, largely because of technical difficulties to elicit bidder preferences and handle trades.

Building on initial ideas by Fan et al. (2003) that extended an earlier effort by Ba et al. (2001b), Guo et al. (2007) propose a market-based optimization algorithm (forthwith, the bundle trading market framework or BTM for short) for optimizing distributed systems using independent, self-interested agents trading bundled resources in a double auction market run by a dealer. In their BTM framework, the dealer replaces the central authority and agents represent division managers or distributed entities. They model the distributed system as a decomposable linear program. The solution process iterates between a market matching problem managed by the dealer and bundle determination problems solved by agents. Guo et al. (2007) show theoretically that an overall optimal solution for the system can be obtained under an iterative, dynamic market trading algorithm in a finite number of trades. They further implement their algorithm in a synchronous, call market environment and sketch an asynchronous implementation. They show that their algorithm is robust against a number of agent strategic behaviors that merely slow down market convergence without affecting system optimality. Overall, the BTM framework presents a market paradigm that addresses price dynamics, incentive issues, and economic transactions of real-world, distributed decision-making situations more realistically than traditional decomposition approaches such as that of Dantzig and Wolfe (1960).

Although the BTM approach opens the door for studying market-based distributed optimization by allowing flexible bundle trading in double auction environments, the impacts resulting from the inclusion of many issues that arise in real market operations remain open research questions. On the fundamental level, communication delays because of the inherent latency of Internet technologies, heterogeneous participation decisions of agents,<sup>2</sup> and uncoordinated decision making among decentralized entities requires the algorithm to effectively handle asynchronous interaction between a dealer and distributed agents. How asynchronous communication and asymmetric information affect market performance is an important issue. Additionally, asynchronous communication inevitably leads to market liquidity concerns. Real-world stock exchanges (e.g., New York Stock Exchange (NYSE)) rely on market intermediaries to supply liquidity. Yet, it is unclear whether holding intertemporal inventory can facilitate real-time trades in computational markets trading complementary resources, or whether there is a preferable inventory policy to speed up market convergence. Furthermore, artificial trading agents are becoming more and more intelligent in terms of predicting market movement and reacting to market dynamics. Knowing how agent learning and predictions affect market design and algorithm convergence is of great practical importance. More importantly, a market mechanism must be robust against various types of agent strategic behaviors to avoid possible market failure. Finally, a market mechanism must be scalable to allow for flexible expansion to accommodate complex bundle trading among large numbers of agents. Therefore, designing an efficient market mechanism that can be implemented on an Internet platform is not a trivial issue. Market communication and information exchange patterns as well as strategic interaction among market participants including distributed agents and dealers may all have impacts on market performance.

In this paper, we expand the original BTM framework to address these realistic market design issues in an asynchronous implementation environment using an adapted iterative market algorithm. We aim to investigate how various market design factors including dealer inventory policies, market communication patterns, agent learning models, and bidding strategies affect computational market efficiency, market liquidity, and implementation. Specifically, this study complements the previous BTM framework in several ways, chiefly by enabling several characteristics used by actual agents in real-world decision making. First, we focus on the effect of market price forecasting on agent strategic bundle selection rather than just strategic underbidding as was studied in BTM. Second, in contrast to a passive dealer inventory policy studied by BTM, we explore active market intervention through the use of more sophisticated dealer inventory policies. Third, we explicitly take into account the effect of asynchronous communication and asymmetric information on market performance. We show that an extended framework that incorporates these aspects will successfully preserve all optimality and finite convergence properties. Through a controlled experiment involving 480 randomly generated market settings and 160 combinations of market treatments, we further evaluate the effects of various market design options on market performance.

There are several interesting findings. First, though both asynchronous communication and asymmetric information negatively affect the speed of market convergence and agent surplus, agents’ forecast learning has a positive effect. Second, in order to preserve auction efficiency, a hybrid model of call and continuous market design is necessary to prevent premature market closure if agents possess a forecast learning ability. Third, contrary to traditional financial market insights, we find that a dealer’s intertemporal liquidity provision may not be desirable, especially in markets that trade a small number of complementary assets and when the dealer owns significant amounts of resources. In addition, our trading data suggests that high trading volume does not correlate to low price volatility and quicker price discovery. Traditional financial market insights may not be directly applied and transferred to the BTM trading environment.

In §2, we briefly review related literature. In §3, we present the basic BTM framework. We describe the market environment, agent decision-making models, and the market clearing mechanism. In §4, we extend the market model to explore dealer active market intervention strategies and agent learning in an asynchronous implementation environment. We also theoretically justify these extensions of the adapted algorithm. Section 5 presents a computational study in a controlled experiment using large-scale simulation. Section 6 summarizes the main results. Section 7 provides additional experiments to allow for more agent strategies and randomization of factors. Section 8 concludes this study and outlines directions for future research. Some supporting materials and all proofs are provided in the online supplement.<sup>3</sup>

## 2. Literature Review

In operations research, distributed systems are modeled as decomposable linear programs (Bertsekas and Tsitsiklis 1997). For large-scale distributed systems, the Dantzig-Wolfe decomposition method (Dantzig and Wolfe 1960) is often viewed as a way to decompose a solution process by dividing the components into those independently solved by managers or by central planners. This is a price-directed decomposition where the central planner first sets the prices of shared resources, then division managers report to the central planner on how they would use the shared resources according to the prices. The central planner reassesses the prices based on the proposed resource usage plans and the process is repeated until an optimal solution to the overall problem is found. The fact that the managers need to report their detailed resource usage plan poses a significant information revelation challenge in any real-world implementation of this approach.

Guo et al. (2007) proposed the BTM framework to overcome this limitation. The BTM mechanism adopts a price-directed decomposition that only requires agents to bid bundled resources in a double auction environment and uses a market dealer to replace the central authority for the market coordination role. Because the closest market mechanism to BTM is a combinatorial exchange (albeit with discrete rather than continuous trade amounts) and the most widely studied markets are combinatorial auctions, we now briefly review literature on combinatorial exchanges, pricing mechanisms used in combinatorial auctions, and practical mechanism design challenges.

There has been extensive literature in auction theory and practical auction designs. A very popular and increasingly important auction type is the combinatorial exchange, which is a combinatorial double auction that brings together multiple buyers and sellers to trade multiple heterogeneous goods. It combines a double auction (McAfee 1992), where multiple buyers and sellers trade multiple units of an identical good, and a combinatorial auction (Cramton et al. 2006), where a single seller sells multiple heterogeneous items. Combinatorial auctions allow bids on combinations of items (bundles) because of the inherent complementarities between the items (Pekec and Rothkopf 2003).

Pricing a combinatorial double auction is very challenging, largely because of the inherent intractability of combinatorial auction pricing. Kothari et al. (2004) considered a very general type of multiunit, multi-item combinatorial exchange. Clearing such an exchange is intractable, so their paper focused on the special case where acceptance of partial bids is allowed. Xia et al. (2005) showed that a general combinatorial double auction can be reduced to a single-sided combinatorial auction problem (which is essentially a multidimensional knapsack problem). They further compared several solution approaches and found that the linear programming relaxation bounds dominate other methods. Their findings show the promise of linear programming models in solving complex combinatorial exchange problems.

A tractable, special case of the combinatorial exchange is the classical assignment problem that can be modeled as a two-sided market in which a set of individuals need to be matched with an equal number of positions. Shapley and Shubik (1972) showed that a competitive equilibrium exists and is efficient in the standard assignment problem. Bertsekas (1979, 1988) was the first to make an explicit connection between a primal-dual algorithm and auction mechanisms. The computational algorithms employ the well-known property of linear programming, where the dual problem provides market clearing prices for the resources used in the primal problem. The primal and dual solutions of the linear program coincide with the Walrasian equilibrium of allocations and prices.

In general, the existence of a pricing equilibrium is not always guaranteed in combinatorial markets with nonconvexities. Kelso and Crawford (1982) studied the package assignment model and derived sufficient conditions for the existence of the Walrasian equilibrium. Under linear programming characterization, Bikhchandani and Mamer (1997) established the necessary and sufficient conditions under which linear prices exist (i.e., prices of packages are the sum of the prices of the objects contained in it). In these works, the equivalence of linear programming solutions and pricing equilibrium remains.

The price paid by the winner in an auction can be interpreted as either a Walrasian price or a Vickrey-Clarke-Groves (VCG) payment. Walrasian prices and VCG payments only coincide in specialized cases such as the one-to-one assignment model (Leonard 1983) or the multi-item generalization of the assignment model (Demange et al. 1986). In combinatorial auctions, Walrasian prices and VCG payments typically differ. Bikhchandani and Ostroy (2002) considered nonlinear pricing functions (i.e., prices are nonadditive over objects) in a package assignment model consisting of multiple objects. They derived necessary and sufficient conditions under which the Vickrey payoff can be implemented as a truth-telling price equilibrium. The Vickrey-based payment scheme has received wide attention in the literature because it is efficient and strategyproof.

Though economists are interested in economic properties such as strategyproof behavior and direct implementation mechanisms, the main theoretical tool—the VCG mechanism—is computationally expensive and impractical (Rothkopf 2007). In the one-shot, sealed-bid combinatorial auction environment, every agent must provide complete information about his preferences to the mechanism. Preference elicitation from agents is proven to be too costly and demanding (Sandholm and Boutilier 2006). It is also well-known that the winner determination problem in combinatorial auctions is NP-hard (Rothkopf et al. 1998). The auctioneer must solve a sequence of NPhard optimization problems to compute the outcome. This is simply intractable. As such, both the computational complexity of the winner determination problem and the communication complexity of preference elicitation have emerged as key bottlenecks in any real-world deployment of combinatorial auctions.

The use of iterative mechanisms in auction design to minimize information revelation and agent computation is one important application in the algorithmic mechanism design literature (Nisan and Ronen 2001, Parkes and Ungar 2000). To handle the preference elicitation challenge in iterative combinatorial auctions, an important method employs primal-dual algorithms (Parkes 2006). Prices are interpreted as feasible dual solutions and the provisional allocation is interpreted as a feasible primal solution. Prices are adjusted iteratively until an optimal dual solution is found. Although the winner-determination problem is still NP-hard, the size of the problem in each round of iteration is considerably smaller than the overall problem. Recent progresses in dynamic combinatorial auction design include the ascending bid auction (Ausubel 2004) and iBundle (Parkes 1999), among others. Applying the linear programming primaldual algorithm to iterative auctions design, De Vries et al. (2007) showed that submodularity is sufficient and substitutability is essentially necessary for VCG implementation of the ascending auction for heterogeneous objects.

A number of information systems researchers are leading an effort to create innovative bundle market mechanisms that allow for more flexible expressions of bidder preferences. For example, a double auction mechanism has been proposed to trade bundled knowledge goods in distributed organizations (Ba et al. 2001b) and bundled network resources in decentralized supply chains (Fan et al. 2003). BTM expanded on ideas by Fan et al. (2003) to allow for flexible bundle composition. Their bundles consist of heterogeneous items and permit simultaneous submissions of buy and sell orders for those distinct items in one package.

In this paper, we aim to advance our understanding of the BTM market design in several dimensions characterized by asynchronous communication, agent learning, and the dealer’s active market intermediation. Because no pricing equilibrium can be guaranteed for indivisible goods, we assume divisible commodities as did BTM. Many real-world resource allocation problems have the divisibility nature, for example, the markets for admission control in telecommunications (Thomas et al. 2002), electricity (Hogan et al. 1996), natural gas (McCabe et al. 1990), and water resources (Raffensperger et al. 2009). Because we are interested in practical implementable market design, we focus on the class of linear pricing schemes. Because of easy implementation, linear prices are widely adopted in practical applications such as the FCC wireless spectrum auctions (Cramton et al. 2006, Chapter 3) and the European Energy Exchange (Meeus et al. 2009).

In addition to the guaranteed existence of linear pricing equilibrium, another important benefit of the divisibility assumption is that the BTM mechanism does not suffer the negative “impossibility” result in the mechanism design literature. The Myerson and Satterthwaite (1983) impossibility theorem asserts that it is impossible for an exchange to be efficient, have individual rationality, and be budget balanced. An immediate consequence of this result is that a mechanism designer can only hope to achieve at most two of the above properties even in a simple exchange environment in which buyers and sellers trade single units of the same good. This has lead to a class of mechanism design that focuses on asymptotical efficiency while maintaining individual rationality and budget-balanced conditions (see Chu 2009 double auction environments; Lubin et al. 2008 combinatorial exchanges).

The Myerson-Satterthwaite impossibility result does not affect the BTM trading mechanism because their trading environment is restricted to an indivisible unit of a commodity and the trading agents are ex ante identified as either buyer or seller with the seller owning the object. McAfee (1991) showed that in an environment with continuous quantities, it is possible to arrange efficient trades without breaking the individual rationality and budget-balanced conditions. He also observed that it is possible to arrange efficient trades in an environment of “hidden endowments,” where any agent may be either a buyer or seller depending on the realization of the privately observed information (price and quantity of the good already in the agent’s possession). Because the BTM model allows divisible quantity and their trading agents are not ex ante identified buyers and sellers, the BTM mechanism can achieve individual rationality, budget balance, and allocative efficiency simultaneously.

Because of the inherent complexity in designing flexible yet robust online auction mechanisms, incentive compatibility is usually unattainable and is therefore not imposed at design time. Researchers have sought alternative approaches to better understand complex market mechanisms. Scheffel et al. (2010) conducted a laboratory experiment using human subjects to compare trading strategies and auction outcomes in a number of iterative combinatorial auction formats proposed in the literature. Bichler et al. (2009) employed a computational analysis to study linear price iterative combinatorial auction formats. Gallien and Wein (2005) undertook numerical experiments simulating bidders’ interactions under certain behavior assumptions in a multiitem procurement auction. Adomavicius and Gupta (2005) provided real-time decision support tools to aid bidders’ evaluations in the iterative combinatorial auction process. They also used simulation to test their market implementation in a computational experiment setting. In line with these approaches to study complex market mechanisms, we employ numerical experiments to simulate dynamic market interactions and use computational methods to evaluate market performance.

## 3. The BTM Framework

In this section, we present the basic BTM framework that we use as a benchmark for our extended model. We then discuss the market environment, the iterative market procedure, and market properties. Please refer to the appendix for a complete summary of notation.

## 3.1. Problem Overview

Consider a distributed system consisting of k independent agents. The overall system (called the central problem) and individual agent problem (called the agent problem) can be expressed as the following linear programs. BTM assumes that the central problem has a bounded solution and is nondegenerate. BTM allows continuous trade amounts. This distinguishes it from the discrete markets where only integer number of units can be traded.

Central problem

$$
\begin{array}{l} Z (c) = \min _ {x _ {j} \geq 0} \sum_ {j = 1} ^ {k} d _ {j} ^ {\prime} x _ {j} \\ \text {s.t.} N _ {j} x _ {j} \leq n _ {j} j = 1, \ldots , k \\ \sum_ {j = 1} ^ {k} C _ {j} x _ {j} \leq c. \end{array}\tag{1}
$$

Agent problem $( j = 1 , \ldots , k )$

$$
\begin{array}{c} z _ {j} (c _ {j}) = \min _ {x _ {j} \geq 0} d _ {j} ^ {\prime} x _ {j} \\ \text { s.t. } N _ {j} x _ {j} \leq n _ {j} \\ C _ {j} x _ {j} \leq c _ {j}. \end{array}\tag{2}
$$

Here, $d _ { i } \in R ^ { b _ { j } }$ is a vector of agent $j ^ { \prime } \mathbf { s }$ cost, $x _ { i } \in R ^ { b _ { j } }$ are $b _ { j }$ -dimensional decision variables controlled by agent $j , \ N _ { j } \in R ^ { a _ { j } \times b _ { j } }$ and $C _ { j } \in R ^ { m \times b _ { j } }$ are activity matrices (where $a _ { j }$ and $b _ { j }$ are appropriately specified), $n _ { i } \in R ^ { a _ { j } }$ is the capacity vector of agent $j ^ { \prime } \mathbf { s }$ independent resources that are managed locally, and $c _ { j } \in R ^ { m }$ is agent $j ^ { \prime } \mathbf { s }$ vector of shared resources that can be exchanged with other agents. Denote agent $j ^ { \prime } \mathbf { s }$ minimal operating cost at the current resource level $c _ { j } \in R ^ { m }$ as $z _ { j } ( c _ { j } )$

Let $c \in R ^ { m }$ be a vector of the system’s total available joint capacity. Denote the minimal operating cost for the central problem as $Z ( c )$ . The central planner’s objective is to minimize the overall system operating cost subject to each individual agent’s operational constraints (the first set of constraints) and the total shared resources capacity constraints (the second set of constraints). However, the central planner does not have access to all the relevant information $( d _ { j } , n _ { j } , c _ { j } ,$ $N _ { j } , C _ { j } , \mathrm { f o r } j = 1 , \dots , k )$ for decision making so an optimal solution to the central problem cannot be directly calculated. The BTM objective is to use a marketbased resource allocation mechanism to coordinate decentralized decision making from agents so that an optimal solution to the central problem can be indirectly obtained through an iterative bidding process.

## 3.2. The Market Environment

The market economy consists of a dealer and k independent agents. Each agent who only has local perspective and knowledge can trade the shred resources $c _ { j }$ in a double auction market run by the dealer. The dealer sets the market prices to match trades. In the following, we describe agent decision making and the dealer’s market clearing policy.

3.2.1. Agent Bidding. In order to derive an agent’s best-response bidding strategy, we first give several basic definitions.

Definition 1 (Bundle). <sub>A</sub> <sub>bundle</sub> $w \in R ^ { m }$ is a vector of shared resources, where positive components in the bundle represent sell amounts and negative components represent buy amounts.

Agents can lower their operating costs by buying extra resources, or they can make a profit by selling some of their resources that might be more effectively used by other agents. Let $p \in \bar { R ^ { m } }$ be the current price vector for the shared resources. A rational agent’s bundle determination problem can be expressed as

$$
\begin{array}{l l} \min _ {x _ {j} \geq 0,   w} & d _ {j} ^ {\prime} x _ {j} + p ^ {\prime} w \\ \text {   st.   } & N _ {j} x _ {j} \leq n _ {j}, \\ & C _ {j} x _ {j} \leq c _ {j} + w. \end{array}\tag{3}
$$

Two types of bundles might result. A limited bundle $w _ { j } \in \bar { R } ^ { m }$ corresponds to an extreme point solution $( \bar { x } _ { j } ^ { \prime } , w _ { j } ^ { \prime } ) \in R ^ { b _ { j } + m }$ , and an unlimited bundle $u _ { i } \in R ^ { m }$ corresponds to an extreme ray solution $( \hat { x } _ { j } ^ { \prime } , \acute { u _ { j } ^ { \prime } } ) \in R ^ { b _ { j } + m }$ Note that a “no-trade” bundle zero is always feasible and has zero cost impact on the agent’s problem. The bundle valuation is defined as follows.

Definition 2 (Bundle Valuation). <sub>(a)</sub> <sub>The</sub> <sub>valua-</sub> tion of a limited bundle is defined as the total value that bundle $w _ { j }$ contributes to the objective change of the agent’s problem, $\mathbf { i . e . , } v _ { i } ( w _ { i } ) = z _ { i } ( c _ { i } ) - d _ { i } ^ { \prime } \bar { x } _ { i } ;$

(b) The valuation of an unlimited bundle is defined as the unit incremental value that $u _ { j }$ contributes to the objective change of the agent’s problem, i.e., $v _ { j } ( u _ { j } ) = - \dot { d } _ { j } ^ { \prime } \hat { x } _ { j }$

Definition 3 (Utility). Given the current market price vector $p \in R ^ { m }$ , agent $j ^ { \prime } \mathbf { s }$ utility for trading a bundle $w \in R ^ { m }$ has the quasilinear form $U _ { j } ( w ) =$ $\boldsymbol { v } _ { j } ( \boldsymbol { w } ) - p ^ { \prime } \boldsymbol { w }$

This quasilinear utility function is a very common assumption in auction theory and mechanism design, which makes it straightforward to transfer utility across agents via side payments.

The following lemma shows that the agent’s bundle determination problem (3) corresponds to a bestresponse strategy in which an agent submits the most preferred bundle that maximizes his utility (all proofs of lemmas are in the online supplement).

Lemma 1 (Best-Response Strategy). <sub>In</sub> <sub>each</sub> <sub>round</sub> of the iterative auction, an agent follows a best-response strategy that is characterized by his bundle determination problem (3).

An agent can submit a limited bundle represented as a triple $[ w _ { j } , l _ { j } ( w _ { j } )$ 1 17, where $l _ { j } ( w _ { j } )$ is the limit price and 1 means the market deals only with unit limit quantities. Any nonnegative multiple of the limited bundle, $\lambda w _ { j } , \ \overset { \cdot } { \lambda } \in [ 0 , 1 ]$ , may be traded. An agent can also submit an unlimited bundle in the form $[ u _ { j } , l _ { j } ( u _ { j } ) , \infty ]$ , where  means that any nonnegative amount may be traded. Regardless of the bundle type, if $l _ { j } ( \dot { w } ) > 0 .$ , then the bundle order is interpreted as a buy. If $l _ { j } ( w ) < 0 ,$ , then it is interpreted as a sell. $l _ { j } ( w ) \dot { = } 0$ is referred to as either a buy or sell. When the limit price is equal to the bundle’s valuation, i.e., $l _ { j } ( w ) = \mathbf { \hat { v } } _ { j } ( w )$ , the pricing is interpreted as truthful pricing. Agents might bid according to their true valuation of the bundle, or they might bid strategically (bid higher or lower than their true valuation).

3.2.2. The Dealer’s Market Clearing Mechanism. The dealer accepts sealed bids from agents. She maintains an individual outstanding order book for each agent. The order book on agent j contains two order sets, $I _ { j }$ and $H _ { j } ,$ for limited and unlimited bundles, respectively. Orders for a specific agent are accumulated in the agent’s order book if no trade is executed for the agent. Any trade from the agent will clear his order book so all outstanding orders are removed.

The dealer trades on her own account. She has some initial resource endowment $c _ { 0 } \geq 0$ and corresponding cash endowment $e _ { 0 } ( c _ { 0 } )$ . Note that the accounting identity $\textstyle \sum _ { j = 1 } ^ { k } c _ { j } + c _ { 0 } \leq c$ holds. The dealer solves the following market matching problem to maximize the market trade surplus:

$$
\begin{array}{l} \max _ {y _ {j} ^ {i} \geq 0, t _ {j} ^ {h} \geq 0} \sum_ {j = 1} ^ {k} \bigg (\sum_ {i \in I _ {j}} l _ {j} (w _ {j} ^ {i}) y _ {j} ^ {i} + \sum_ {h \in H _ {j}} l _ {j} (u _ {j} ^ {h}) t _ {j} ^ {h} \bigg) \\ \text {st.} \sum_ {j = 1} ^ {k} \bigg (\sum_ {i \in I _ {j}} w _ {j} ^ {i} y _ {j} ^ {i} + \sum_ {h \in H _ {j}} u _ {j} ^ {h} t _ {j} ^ {h} \bigg) \leq c _ {0}, \\ \sum_ {i \in I _ {j}} y _ {j} ^ {i} \leq 1 \quad j = 1, \ldots , k. \end{array}\tag{4}
$$

The first set of constraints represents the market clearing conditions subject to the dealer’s available inventory $c _ { 0 } .$ The second set of constraints shows the different treatment for the two types of bundles. Though trades of unlimited bundles in set $H _ { j }$ are unrestricted, trades of the limited bundles are required to be convex combinations of bundles in set $I _ { j } .$ This constraint does not have the usual equality sign because there is an implicit “no-trade” bundle for each agent composed of zeros and priced at zero (recall, a zero bundle is always feasible to the agents’ bundle determination problem). The marketmatching problem always has a solution (e.g., all variables set to zero is a feasible solution).

If the market matching problem has nonzero solutions $y _ { j } ^ { i * }$ for $i \in I _ { j }$ and $t _ { j } ^ { h * }$ for $h \in H _ { j } ,$ then agent j will have traded $\begin{array} { r } { \boldsymbol { w _ { j } ^ { * } } = \sum _ { i \in I _ { i } } \boldsymbol { w _ { j } ^ { i } } \boldsymbol { y _ { j } ^ { i * } } + \sum _ { h \in H _ { i } } \boldsymbol { u _ { j } ^ { h } } \boldsymbol { t _ { j } ^ { h * } } } \end{array}$ . The market clearing prices $p \in R ^ { \acute { m } }$ are set as the dual prices from the first set of constraints of the market matching problem. We adopt a uniform price (all units for the same shared resource are bought or sold at the same market clearing price) and linear pricing rule (price for a bundle is the sum of prices for all components in the bundle). Thus, the payment for agent j on a trade w<sup>∗</sup> is $p ^ { \prime } w _ { j } ^ { \ast }$ . As a result, agent $j ^ { \prime } \mathbf { s }$ new values are $c _ { j } + w _ { j } ^ { \ast }$ for $j = 1 , \dots , k$ and the dealer ends with $c _ { 0 } - \textstyle \sum _ { j = 1 } ^ { k } w _ { j } ^ { * }$ . The dealer’s inventory level stays nonnegative and she retains excess resources resulting from unbalanced trades. Assume that the cash endowment for agent j at resource level $c _ { j }$ is $e _ { j } ( c _ { j } )$ The cash endowments are updated as $e _ { j } ( \overset { \cdot } { c } _ { j } + \overset { \cdot } { w _ { j } ^ { * } } ) =$ $e _ { j } ( c _ { j } ) - p ^ { \prime } w _ { j } ^ { \ast }$ for $j = 1 , \dots , k$ and $\begin{array} { r l } { e _ { 0 } ( c _ { 0 } - \sum _ { j = 1 } ^ { k } w _ { j } ^ { * } ) = } \end{array}$ $\begin{array} { r } { e _ { 0 } ( c _ { 0 } ) + \sum _ { j = 1 } ^ { k } p ^ { \prime } w _ { j } ^ { * } } \end{array}$

Definition 4 (Wealth). <sub>Given</sub> <sub>the</sub> <sub>cash</sub> <sub>endow-</sub> ment $e _ { j } ( c _ { j } )$ and the level of shared resources $c _ { j } ,$ agent $j ^ { \prime } \mathrm { s }$ wealth is $W _ { j } ( c _ { j } ) = e _ { j } ( c _ { j } ) - z _ { j } ( c _ { j } )$

Note that the negative sign on $z _ { j } ( c _ { j } )$ reflects cost minimization. Based on the above settlement rule, we can further show that an agent’s wealth after trading is no less than his wealth before trading, formally stated in Lemma 2.

Lemma 2 (Wealth Nondecreasing Trade). <sub>If</sub> <sub>agent</sub> <sub>j</sub> trades with $\boldsymbol { w } _ { j } ^ { * }$ , then her wealth after trading is nondecreasing, $i . e . , W _ { j } ( \overset { \prime } { c _ { j } } ) \leq W _ { j } ( c _ { j } + w _ { j } ^ { * } )$ .

## 3.3. The Market Dynamics

In the following, we describe the iterative market procedure in the context of this study, which is an extended form of the original BTM framework. We first explain the dynamic price discovery process. We then discuss some important market properties in the computational market environment.

3.3.1. The Iterative Market Procedure. In an exchange, trading takes place in trading sessions. The two types of trading sessions are call market and continuous market sessions (Harris 2002). In a call market, orders submitted to the system will be accumulated in the order book and processed simultaneously at periodic intervals. All agents trade at the same time when the market is called. In contrast, a continuous market arranges immediate execution as orders arrive. As orders arrive asynchronously, the market attempts to clear every time there are new orders. The BTM framework is designed as a hybrid form of continuous and call markets. The market starts as a continuous market and agents participate asynchronously. We only use a call market to restart trading after a trading halt in order to avoid premature market closure.

The market allocation is an iterative process. In each round, participating agents select resource bundles based on their currently available market prices<sup>4</sup> using the decision rule specified in (3) and then submit their bids. Upon receiving bids, the dealer solves the market matching problem (4). New market prices are discovered as the dual prices from the first set of constraints of the market matching problem. The dealer announces the current market prices. If there is a price change compared to the prior round, the next round begins. The market continues to operate as a continuous market. If the new prices repeat the prior round’s prices and the market is not operating as a call market yet, the dealer will initiate a market call. All agents are informed that this might be the last round of trading so new bids arrive synchronously, if there are any. If the new prices repeat the prior round’s prices and the market is already operating as a call market, the market closes. Figure 1 provides a sketch of the iterative market process. The actual implementation involves many more details that we will explain in §4.

3.3.2. An Overview of Market Properties. In auction market design, incentive compatibility, individual rationality, budget balance, allocative efficiency, and social welfare are important market properties. Because we do not impose truth revelation, agents may not bid truthfully in each round of the auction. However, an efficient auction outcome can be achieved by incremental revelation of agent preferences through the iterative trading process.

The BTM mechanism ensures individual rationality in the sense that each agent expects nonnegative gain from a trade. The market settlement ensures that any trade from the agent is wealth nondecreasing (Lemma 2).

In the traditional auction environment, the auctioneer is typically not considered a player of the mechanism. The failure of budget balance implies that the auctioneer earns negative revenues. Under the BTM framework, when the dealer adopts a passive inventory policy as in Guo et al. (2007), she earns nonnegative revenues. The Myerson-Satterthwaite impossibility result does not apply to our trading environment. When the dealer actively trades on her own account (as in this study), we treat the dealer as a player of the mechanism. Because all resources are exchanged among agents and the dealer via side payments in the system, the BTM mechanism is budget balanced.

Under the standard assumption of neoclassical economics that goods are continuously divisible, agents play the role of buyers or sellers in the market depending on their endowments and preferences. As seen in Lemma 1, agents maximize utility using a best-response strategy in each round of the market trading. Because no agent is interested in submitting any new bundles based on the market prices at the algorithm termination, no one is willing to give up resources in exchange for cash or to buy additional resource to lower operating costs. Therefore, the BTM mechanism terminates in competitive equilibriums where the final prices and allocation clear the market by equating marginal rates of substitution among agents.

Figure 1 A Simplified Flow Chart of the BTM Model  
![](/api/attachments/P8E6DJJ8/fulltext/images/423b12a03dfff6c99b3a2ba73ad27fbaf464c60e57bd10eb6f677a8b8b650ab9.jpg)

In auction, allocative efficiency is achieved when total value over all agents is maximized. Define agent $j ^ { \prime } \mathbf { s }$ aggregate trade of resources in round R as $\begin{array} { r } { \bar { w _ { j R } } = \sum _ { i = 1 } ^ { R } \bar { w _ { i j } ^ { * } } . } \end{array}$ , the sum of all traded resource bundles for agent j up to round R. We have the following lemma.

Lemma 3 (Allocative Efficiency). <sub>Given</sub> <sub>the</sub> <sub>ini-</sub> tial endowment of resources $c ^ { 0 } = ( c _ { 1 } ^ { 0 } , \ldots , c _ { k } ^ { 0 } )$ and the aggregated trade of resources $\bar { w } _ { R } = ( \bar { w } _ { 1 R } , \dots , \bar { w } _ { k R } )$ , an efficient allocation is achieved if and only if the following equality holds: $\textstyle \sum _ { j = 1 } ^ { k } z _ { j } ( c _ { j } ^ { 0 } + \bar { w } _ { j R } ) = Z ( c )$

We will show in §4.5 that, at algorithm termination, an optimal allocation to the central problem can be achieved so that the total operating cost of all agents is minimized; this equals to the central problem operating cost $Z ( c )$ . Therefore, the BTM mechanism guarantees full allocative efficiency. In any round of the auction, the degree of allocative efficiency is measured as the ratio of the total operating costs of all agents at the current resource levels to the overall operating cost in the central problem, i.e., $\textstyle \sum _ { j = 1 } ^ { k } z _ { j } ( c _ { j } ^ { 0 } + \bar { \bar { w } } _ { j R } ) / Z ( \bar { c } )$

Social welfare is measured by the total wealth from both agents and the dealer, i.e., $\textstyle \sum _ { j = 0 } ^ { k } W _ { j } ( c _ { j } ) =$ $\begin{array} { r } { \sum _ { j = 0 } ^ { k } e _ { j } ( c _ { j } ) - \sum _ { j = 1 } ^ { k } z _ { j } ( c _ { j } ) } \end{array}$ . Because the market is budget balanced, the final cash endowments in the system equal the total initial cash endowments, which are redistributed among agents and the dealer through bundle trading in the market. At the algorithm termination, the market achieves efficient allocation. The total operating cost of all agents is minimized and equals the central problem operating cost $Z ( c )$ . Therefore, the social welfare is maximized at the algorithm termination.

## 4. Model Extension and the Adapted Algorithm

Market performance is largely affected by the way trading is organized, including how the dealer performs market intermediation, how market information is accessed, and how orders are communicated. We incorporate these factors in an extended BTM model. We then detail an adapted, asynchronous implementation of the extended BTM algorithm. We further provide theoretical justifications for an efficient market design and convergence of the algorithm to a systemwide optimal solution.

## 4.1. The Dealer’s Market Intermediation

Although real-world exchanges such as the NYSE rely on market intermediaries to supply liquidity, it is unclear whether holding intertemporal inventory can facilitate real-time trades in the BTM environment. In market microstructure theory (O’Hara 1995), the dealer’s optimization problem has been studied from various aspects with inventory and pricing as the major concern. In inventory-based models, Amihud and Mendelson (1980) found that the dealer has a preferred inventory position. As the dealer finds her inventory departing from the preferred position, she moves prices to bring her position back. Based on this insight, we borrowed a term from the inventory management literature and designed the safety stock inventory policy. Under this, the dealer trades on her own account to maintain a certain level of predefined safety stock. Following a similar notion, the speculative price inventory model is a variation of the safety stock inventory model, where deviation of target price rather than target inventory triggers the dealer’s trading decisions. We describe the two inventory policies in detail next.

4.1.1. The Safety Stock (SS) Policy. Under the SS policy, the dealer maintains a safety stock level $s \in R ^ { m }$ Once any component of the dealer’s inventory level drops below the target level $( \mathrm { i . e . , } ( c _ { 0 } ) _ { j } < s _ { j } )$ , the dealer attempts to buy the difference from the market to restore her target inventory. This is accomplished by adding a buy order at the current market price of that item in the market matching problem. Let $1 _ { j }$ be the jth unit vector and $y _ { j }$ be the buy amount for the jth shared resource in the dealer’s account. The revised market matching problem is

$$
\begin{array}{l}\max_{\substack{y_{j}^{i}\geq 0,  t_{j}^{h}\geq 0,\\ y_{j}\geq 0}}\Big\{\sum_{j = 1}^{k}\bigg(\sum_{i\in I_{j}}l_{j}(w_{j}^{i})y_{j}^{i} + \sum_{h\in H_{j}}l_{j}(u_{j}^{h})t_{j}^{h}\bigg)\\ \quad +\sum_{(c_{0})_{j} <   s_{j}}p_{j}(s_{j} - (c_{0})_{j})y_{j}\Big\} \\ \text{s.t.}\sum_{j = 1}^{k}\bigg(\sum_{i\in I_{j}}w_{j}^{i}y_{j}^{i} + \sum_{h\in H_{j}}u_{j}^{h}t_{j}^{h}\bigg)\\ \quad +\sum_{(c_{0})_{j} <   s_{j}}(s_{j} - (c_{0})_{j})1_{j}y_{j}\leq c_{0} - \sum_{(c_{0})_{j} <   s_{j}}(c_{0})_{j}1_{j},\\ \sum_{i\in I_{j}}y_{j}^{i}\leq 1\quad j = 1,\ldots ,k,\\ \quad 0\leq y_{j}\leq 1\quad \text{for $j$ where $(c_0)_j <   s_j$.} \end{array}\tag{5}
$$

The objective maximizes the total market surplus from both agents and the dealer. The first set of market clearing constraints says that when the dealer submits buy orders for resources, the right-hand side dealer’s inventory for those resources are restricted to zero, which prevents the dealer from selling from her own inventory. The last set of constraints state that the dealer’s order fulfillment does not exceed the specified amount $s _ { j } - \left( c _ { 0 } \right) _ { i }$ .

4.1.2. The Speculative Price (SP) Policy. Under the SP policy, the dealer speculates on market prices. Let $r \in \bar { R } ^ { m }$ be her speculative price levels. Once the dealer observes that a resource price for item $j$ drops below $r _ { j } ~ ( \mathrm { i . e . } , ~ p _ { j } < r _ { j } )$ , she attempts to buy as much as possible from the market at current market price. She also attempts to sell as much as possible from her inventory as long as the current market price is greater than $r _ { j } ~ ( \mathrm { i . e . } , ~ p _ { j } > r _ { j } )$ . Let $q _ { j } ^ { b }$ and $q _ { j } ^ { s }$ be the buy and sell amounts, respectively, for the jth shared resource in the dealer’s account. The revised market matching problem is expressed in (6):

$$
\begin{array}{l}\max_{\substack{y_{j}^{i}\geq 0,  t_{j}^{h}\geq 0,\\ q_{j}^{b}\geq 0,  q_{j}^{s}\geq 0}}\Bigg\{\sum_{j = 1}^{k}\bigg(\sum_{i\in I_{j}}l_{j}(w_{j}^{i})y_{j}^{i} + \sum_{h\in H_{j}}l_{j}(u_{j}^{h})t_{j}^{h}\bigg)\\ \\ \quad +\sum_{p_{j} <   r_{j}}p_{j}q_{j}^{b} - \sum_{p_{j} > r_{j}}p_{j}q_{j}^{s}\Bigg\} \\ \text{s.t.}\sum_{j = 1}^{k}\bigg(\sum_{i\in I_{j}}w_{j}^{i}y_{j}^{i} + \sum_{h\in H_{j}}u_{j}^{h}t_{j}^{h}\bigg) + \sum_{p_{j} <   r_{j}}1_{j}q_{j}^{b}\\ \\ \quad -\sum_{p_{j} > r_{j}}1_{j}q_{j}^{s}\leq c_{0} - \sum_{p_{j} <   r_{j}}(c_{0})_{j}1_{j} - \sum_{p_{j} > r_{j}}(c_{0})_{j}1_{j},\\ \\ \sum_{i\in I_{j}}y_{j}^{i}\leq 1\quad j = 1,\ldots ,k,\\ \\ q_{j}^{s}\leq (c_{0})_{j}\quad \text{for $j$ where $p_j > r_j$.} \end{array}\tag{6}
$$

The overall objective is to maximize the total market surplus. Again, in the first set of constraints, a buy order for the jth shared resource restricts the right-hand side for the jth resource to be zero so that dealer cannot buy from her own inventory. The last constraint means that the sell amount cannot exceed the dealer’s available inventory. No short selling is allowed.

The SS and SP inventory policies allow the dealer to perform active market intervention. This is in direct contrast with the passive inventory policy stated in problem (4) and used in Guo et al. (2007), which we call the naïve inventory policy or NA policy. In reality, it is reasonable to assume that the dealer, who regulates market prices, has an informational advantage over agents. In order to understand the effect of differential information on market performance, we design two additional policies that we refer to as the full information safety stock (FISS) policy and the full information speculative price (FISP) policy, respectively. By full information, we mean that the dealer knows the true market prices for resources (using them within the SP policy and bidding the true market prices rather than buying at the current market prices in the SS policy). It is worth noting that both FISS and FISP are used to calibrate the value of true market information on the dealer’s market intermediation. Our algorithm does not rely on such knowledge to converge. All together, we have the following treatment for the dealer’s inventory policies: V ∈ 8NA1 SS1 SP1 FISS1 FISP9.

## 4.2. Agent Forecasting of Future Market Prices

In the iterative market trading framework, market performance is largely affected by agent bundle elicitation. This allows for many possible forms of agent strategic behavior in both bundle selection and bundle pricing. The original BTM model focused on agents underbidding resource bundles and assuming that the bundle selection followed problem (3), where an agent uses the most recently observed market price. We call this myopic learning (denoted as M). In this paper, we look at agent strategic bundle selection, where agents use forecasted market prices to determine their most preferred bundles. We denote the forecast learning as F .

In addition, the level of information transparency is a market design issue. One possible design is that market price information is restricted to participating agents. Agents who have asynchronous market interactions may get different real-time market prices. In this sense, they have asymmetric access (denoted as $A )$ to market information. Alternatively, market price information can be broadcast to all agents regardless of their asynchronous participation. In this case, agents have symmetric access (denoted as S) to market information. All together, we use the following treatment set to account for the four possible combinations: $L _ { j } \in \{ \mathrm { M A } , \mathrm { M S } , \mathrm { F S } , \mathrm { F A } \}$ . For example, MA can be read as myopic learning with asymmetric access to market information. When we give L without a subscript, we mean that all agents use the same learning strategy.

In designing the forecast learning model, we recognize that there are many types of forecasting techniques for time-series data, including moving average, exponential smoothing, regression, and autoregressive methods among others (Makridakis et al. 1983). Of these, an exponential weighted moving average (EWMA) learning model (Roberts 1959) is chosen because of its simplicity and tractability. More sophisticated methods are left for future study.

Let $\tilde { p } _ { j R }$ be agent $j ^ { \prime } \mathbf { s }$ forecasted market price in round $R$ and $\pi _ { j R }$ be agent $j ^ { \prime } \mathbf { s }$ observed market price. Set $\tilde { p } _ { j 0 } = \pi _ { 0 } ,$ where $\pi _ { 0 }$ is the initial market price vector. For $R \geq 1$ , the price forecast model is: $\bar { \tilde { p } } _ { j R } = \alpha \pi _ { j R } +$ $( 1 - \alpha ) \tilde { p } _ { j , R - 1 } ,$ where $0 < \alpha \leq 1$ is the smoothing constant. The smoothing constant  determines the rate at which older market prices enter into the forecast of the new market price. In the myopic learning models, we set $\alpha = 1$ so only the most recently acquired market price matters. In the EWMA forecast models, we use the smoothing constant $\alpha = 0 . 8$ , where relatively higher weight is given to the currently observed market price. Certainly we can treat the smoothing constant as a parameter rather than a constant. Initial pilot runs show that there was no significant difference between chosen parameter values in the range 60051 0097.

## 4.3. Asynchronous Communication

Because of a variety of reasons such as the inherent latency of Internet technology, the cost of frequent market participation, and the nature of uncoordinated decision making in distributed systems, traders would have different communication frequencies to interact with the market. Consequently, asynchronous communication may affect different sequences of order arrival that, in turn, may affect market convergence. We model the level of asynchronous communication as the probability of each agent’s participation in each round of market trading, denoted as $P _ { j } .$ We design four levels of asynchronous communication: $\check { P _ { j } } \in \{ 0 . 2 , 0 . 5 , 0 . 8 , 1 \}$ . For example, treatment $P _ { j } = 0 . 2$ models the most asynchronous communication scenario in which agent j has a 20% probability of communicating with the market in each round of market trading. When we give $P$ without a subscript, we mean that all agents use the same value. Thus, treatment $P = 1$ indicates that all agents participate in each round of market trading. This is the case studied by BTM.

## 4.4. Implementation of the Extended Market Model

There are several implementation challenges in terms of adapting the original BTM algorithm to the extended asynchronous market trading environment. First, we must avoid premature market closure risk (which leads to a suboptimal solution to the central problem). Second, we must ensure proper market closure without repeatedly exchanging the same sets of bundles among agents and the dealer with zero gains from trades (a cycling problem). We discuss our algorithmic treatment and theoretical justification to these nontrivial issues in the online supplement. In the following, we give several definitions and describe a complete implementation of the extended algorithm.

Definition 5 (Active/Inactive Trading). <sub>(a)</sub> <sub>In</sub> any round of market iteration, if an agent solves his bundle determination problem, the agent is active; otherwise, the agent is inactive.

(b) In any round of market iteration, if there are no new orders, we say the market is inactive; otherwise, we say the market is active.

(c) If there are positive market trades $( \mathrm { i . e . } $ , the market matching problem yields a nonzero solution) in a round, then we call it an active trading round.

Note that it is possible that an agent who solved his bundle determination problem in a round is not interested in submitting any new orders.

Definition $6$ (Value-Added/Nonvalue-Added <sup>Trading).</sup> In an active trading round, if the market surplus is nonzero, we call it value-added trading; otherwise, it is a nonvalue-added trading.

Definition 7 (Excluded List and Oscillation <sup>List).</sup> The excluded list contains the indices for all trading agents in a nonvalue-added trading round, and the oscillation list keeps track of the dealer’s inventory status in a nonvalue-added trading round.

The extended BTM algorithm can be implemented as follows.

Step 0 (Initialization). Initialize dealer $( j = 0 )$ and agent $( j = 1 , \ldots , k )$ , cash endowments $\boldsymbol { e } _ { j } ,$ and initial allocations $c _ { j } .$ . Initialize the market price vector $\pi _ { j } = 0 ,$ $j = 0 , \ldots , k$ . Select agents’ communication frequency $P _ { j } \in ( 0 , 1 ]$ and learning model $L _ { j } , \ j = 1 , \ldots , k$ . Select the dealer’s inventory policy V . Initialize the periodic contact cycle length $\bar { X . } ^ { \bar { 5 } }$

Set the outstanding limit and unlimited order books $I _ { j } = \mathcal { D }$ and $H _ { j } = \emptyset$ for agents $j = 1 , \ldots , k .$ . Set the nonparticipation tracking index for agent j as $T _ { j } = 0 ,$ , the total number of rounds as $R = 0$ , and the number of inactive rounds as $Q = 0 .$ . Set index sets $N e w = \emptyset$ and $T r a d e = \mathcal { O }$ to track agents who submit new bundles and who have positive market trades, respectively. Set the excluded agent list as Exclude =  and the dealer’s inventory oscillation list as InvOsc = .

Step 1 (Agent Bundle Selection). $R \gets R + 1$ . If agent j communicates with the dealer, then reset $T _ { j } = 0 ;$ otherwise, $T _ { j } \gets T _ { j } + 1 . \mathrm { ~ I f ~ } T _ { j } = X ,$ , then the dealer communicates the current market prices $\pi _ { j }  p ,$ , invites the agent to participate, and resets $T _ { j } = 0 ;$ otherwise, the dealer does nothing with the agent.

A participating agent j forecasts market prices $\tilde { p } _ { j R }$ based on his learning model $L _ { j } .$ Based on $\tilde { p } _ { j R } ,$ the agent solves his bundle determination problem. If there is a new bundle, then the dealer adds the new limited bundle orders $w _ { j }$ to $I _ { j }$ and the unlimited bundle orders $u _ { j }$ to $H _ { j } .$ . Then, the dealer adds index $j$ to set New.

If New $\neq \emptyset$ , then $Q = 0$ and go to step 2; otherwise, $Q  Q + 1$ . If $Q < 2 X$ , repeat step 1; otherwise, if $V \neq \mathrm { N A } ,$ V ← NA and go to step 2 and if $V { = } \mathrm { N A }$ then go to step 4.

Step 2 (Market Matching). If $c _ { 0 } \in$ InvOsc and New ⊆ Exclude, then $c _ { 0 }  0 .$ . Calculate $\mathrm { M A P N } _ { R } =$ $\begin{array} { r } { \frac { 1 } { 5 } \sum _ { t = R - 4 } ^ { R } \| p _ { t } - p _ { t - 1 } \| , R \ge 5 } \end{array}$ based on $\pi _ { 0 } .$ . If $\mathrm { M A P N } _ { R } < 1 , { } ^ { 6 }$ then set $V  \mathrm { N A }$ . The dealer solves the marketmatching problem defined by inventory policy V . Add agents who have positive market matches to set Trade. The dealer announces the shadow price p (the duals to the clearing constraints of the marketmatching problem) as the new market prices. The dealer saves the current prices $\pi _ { j }  p$ for $j = 0$ and $j \in N e w \cup T r a d e .$

If there is a nonzero solution to the marketmatching problem and the market surplus is nonzero, then reset $E x c l u d e = \emptyset$ . Also, $I n v O s c = \emptyset$ . Go to step 3.

If there is a nonzero solution to the marketmatching problem and the market surplus is zero, then add agents who are involved in the trade to Exclude and add $c _ { 0 }$ to InvOsc. If there is only one agent in the set Trade, then reset $N e w = \emptyset$ and $T r a d e = \mathcal { O }$ and go to step 1; otherwise, go to step 3.

If there is no market match, then reset $N e w = \emptyset$ and $T r a d e = \emptyset .$ . Go to step 1.

Step 3 (Market Settlement). Let w<sup>∗</sup> be the aggregate matched bundle for agent j. For $j \in T r a d e , c _ { j } \gets c _ { j } + w _ { j } ^ { * }$ and $e _ { j } \gets e _ { j } - p ^ { \prime } w _ { j } ^ { * }$ . The dealer updates $\textstyle c _ { 0 } \gets c - \sum _ { j = 1 } ^ { k } c _ { j }$ and $\begin{array} { r } { e _ { 0 } \gets e _ { 0 } + p ^ { \prime } \sum _ { j \in T r a d e } w _ { j } ^ { * } } \end{array}$ . Reset $I _ { j } = \mathcal { D }$ and $H _ { i } = \dot { \emptyset }$ for $j \in$ Trade. Reset $N e w = \emptyset$ and $T r a d e = \emptyset$ . Go to step 1.

Step 4 (Market Call). $R \gets R + 1$ . All agents use the current market price $\pi _ { 0 }$ for their bundle determination. If there are new orders, then the dealer is to add the new limited bundle orders $w _ { j }$ to $I _ { j }$ and unlimited bundle orders $u _ { j }$ to $H _ { j } ,$ add index j to set New, and reset $T _ { j } = 0$ for $j = 1 , \dots k$ . Then, $Q = 0$ and go to step 2; otherwise, stop.

## 4.5. Efficient Market Design

Under the assumptions of agent myopic learning and truthful pricing, the finite termination property at the system optimal solution was proved under the original BTM framework (Guo et al. 2007, Theorems 3 and 4). They also proposed an adaptation of their synchronous market model to an asynchronous environment (Guo et al. 2007, pp. 19–20). When incorporating asynchronous communication, agent learning strategies, and the dealer’s active market intervention, this section offers new insights about efficient market design under the extended market paradigm. The following corollaries are extensions to Theorems 3 and 4 in Guo et al. (2007), respectively, that we apply to the asynchronous BTM trading environment. Proofs are in the online supplement.

Corollary 1 (Finite Convergence). <sub>In</sub> <sub>the</sub> <sub>asyn-</sub> chronous BTM trading environment, if agents use a myopic learning strategy, then the continuous market converges to an optimal allocation in a finite number of trades. If agents use a forecast learning strategy, there exists a positive probability that a continuous market yields a suboptimal allocation. However, a combined form of continuous and call markets can preserve the finite convergence property.

Corollary 1 shows that agent learning strategies have important implications for efficient market design. Although a continuous market is sufficient for convergence and optimality under agent myopic learning, an efficient continuous market operation must be facilitated by the call market design when agents use a sophisticated learning strategy such as forecast learning. This treatment is similar to the practice that some stock markets such as NYSE use calls to restart their trading after a trading halt.

As to the impact of agent strategic behavior on market convergence, Guo et al. (2007) studied one special case where agents underbid for a preferred bundle. This study complements previous work by taking into account the strategic impact of bundle selection. Corollary 2 shows a market convergence property for the adapted BTM algorithm under the new conditions of asynchronous communication, the dealer’s active market intermediation, and agent strategic learning that we are exploring here.

Corollary 2 (Optimal Allocation). <sub>Regardless</sub> <sub>of</sub> agents’ strategic behavior in bundle pricing and bundle selection, the adapted BTM algorithm terminates in a finite number of trades with an optimal allocation.

In reality, strategic behavior by distributed agents cannot be prevented. Our mechanism is robust against agent strategic activities. This result shows the promise of using algorithmic market mechanisms to deal with such practical implementation challenges.

## 5. Market Experiment Design

In this section, we describe a controlled experiment aimed at understanding the fundamental effects of key market design factors on market operations. We first present our market treatments. We then detail our parametric choices and sample generation methods in our large-scale simulation.

## 5.1. Market Treatments

In the previous section, we discussed various types of dealer inventory policies, agent learning models, and market communication patterns. Additionally, the bundle trading market can be organized based on different initial market conditions. For example, in a distributed organizational setting, the central planner handles the procurement of new organizational resources and thus has the initial resource ownership. Double auction-based smart market applications, in contrast, do not have a centralized ownership of resources. Initially, the shared resources are randomly dispersed among the production agents. We study both possibilities of initial market configurations, denoted as the dealer’s initial resource ownership: $O \in \{ 0 , 1 \}$ . Here, O = 0 means the dealer does not hold any resources initially and $O = 1$ indicates that all resources are centralized at the beginning of the trading period. Table 1 summarizes the $2 \times 5 \times 4 \times 4 =$ 160 combinations of our market treatments.

Table 1 Computational Market Treatments

<table><tr><td>Market participants</td><td>Experimental design</td><td>Market treatments</td></tr><tr><td rowspan="2">Dealer</td><td>Initial resource ownership</td><td> $O \in \{0, 1\}$ </td></tr><tr><td>Market intermediation models</td><td> $V \in \{NA, SS, SP, FISS, FISP\}$ </td></tr><tr><td rowspan="2">Agents</td><td>Asynchronous communication</td><td> $P_j \in \{0.2, 0.5, 0.8, 1\}$ </td></tr><tr><td>Learning models</td><td> $L_j \in \{MA, MS, FS, FA\}$ </td></tr></table>

## 5.2. Parametric Choices

Corresponding to the above-mentioned design, policy parameters such as the preferred inventory level $s _ { j }$ and speculative prices $p _ { j }$ for each resource component $( j = 1 , \ldots , m )$ need to be defined for the dealer’s inventory strategy. For each individual inventory target $s _ { j } ,$ we assume that the dealer randomly selects a level between 5% and 20% of the total resource availability for that specific resource. If the dealer does not have any informational advantage, we arbitrarily select a speculation level not far from zero for each individual price target $p _ { j } ,$ i.e., a random number between 0.1 and 0.3. In the case that the dealer has an informational advantage, we set the price target as the equilibrium price for component j (i.e., the optimal dual values for the shared resource constraints in the central problem).

The parameter selections were made after various pilot runs. These design parameters had face validity as judged by an examination of our trading data. On average, the dealer switched her inventory policies at the time between 3.45% and 26.93% of the total market iteration is reached. At the point of switch, the dealer had accumulated between 88.17% and 99.91% of her total wealth. On average, between 50.88% and 96.25% of the total optimal objective had been achieved. This showed that the dealer’s switching strategy was generally effective.

## 5.3. Sample Generation

In a decentralized market environment, market performance is influenced by both the macrolevel market characteristics and the microlevel agent decisionmaking efficiency. Factors characterizing the market environment include the number of market participants k and the number of shared resources m. Factors describing agents’ internal decision-making complexity include the number of independent resources $a _ { j }$ that each agent manages and the number of activities $b _ { j }$ that are involved in the agent’s production. Following the experimental design principle (Friedman and Sunder 1994), we select two values for each factor representing small and large effects. This is deemed to be sufficient and Table 2 summarizes our design.

Following Guo et al. (2007), for each of the 16 scenarios resulting from the 4 factor combination, we generate 30 sets of distributed problems. We choose coefficients using a random sampling from a uniform distribution 6−11 57. This interval allows for both negative and positive coefficients. The specific numeric values for the lower and upper bounds as well as for each factor pair are set to ease our random generation of feasible linear programs. Other parametric choices do not affect the fundamental insights generated from this study. The 30 random problem instances for each factor combination allow for reliable statistical tests. This results in $2 \times 2 \times 2 \times 2 \times 3 0 = 4 8 0$ independent samples. Together with the 160 treatments, our simulation study has $4 8 0 \times 1 6 0 = 7 6 , 8 0 0$ observations to analyze the market operations. Each was processed using the new market framework.

Table 2 Design for Sample Generation

<table><tr><td>Market environment</td><td>Factors</td><td>Factorial design</td></tr><tr><td rowspan="2">Macrolevel (market)</td><td>Number of agents</td><td> $k \in \{10, 50\}$ </td></tr><tr><td>Number of shared resources</td><td> $m \in \{2, 8\}$ </td></tr><tr><td rowspan="2">Microlevel (agent)</td><td>Number of independent resources</td><td> $a_j \in \{2, 8\}$ </td></tr><tr><td>Number of activities</td><td> $b_j \in \{4, 8\}$ </td></tr></table>

## 6. Experimental Results

In this section, we first illustrate the market price dynamics and present summary statistics and test results from our computational data. We then focus on the impacts of key market design parameters on market performance as well as agents and the dealer’s wealth.

## 6.1. Price Dynamics

One important advantage of our computational experiment is the detailed level trading data that help us gain insights about market operation. Figure 2 compares the price discovery process in markets trading bundles of 2 shared resources with 10 agents and 50 agents, respectively. For illustration purposes, we only plot the price dynamics for the first resource under the naïve and safety stock inventory policies.

Illustration of price dynamics in a market with 10 agents  
![](/api/attachments/P8E6DJJ8/fulltext/images/665c2f8ca619a1ad4674790f8512f2f4b7ae0693743c1b9e54142c648d9e6d78.jpg)

## Figure 2 Market Price Dynamics Under the Naïve (NA) and Safety Stock (SS) Inventory Policies

Initially, the two shared resources are randomly dispersed among agents. The dealer does not have any initial inventory. The market starts with a trading price of zero for both resources. Agents independently communicate with the dealer with probability $P = 0 . 2 ,$ and agents use asymmetric myopic learning strategy.

We have the following observations. First, large price jumps are more likely to occur when the number of market participants is not large. Other things being equal, price changes will be much smoother when the number of market participants increases. Second, regardless of the number of market participants, prices fluctuate in a relatively large range at the beginning periods but then nonmonotonically converge to the equilibrium market price. Third, the dealer’s active trading on her own account $( \mathrm { e . g . }$ , SS policy) often leads to a higher price variation in comparison with the naïve inventory policy.

## 6.2. Summary Statistics

As discussed in §3.3.2, social welfare (total wealth of agents and the dealer) is maximized at the algorithm termination through redistribution of cash endowments and bundles of shared resources. Because the dealer is considered a player of the auction mechanism who trades on her own account and has no outside subsidies, the market is a zero sum game. We are interested in the division of wealth among agents and the dealer. To compare such a relative wealth effect, we define wealth ratio as total agent net wealth divided by total system gain. Agent net wealth is calculated as

From a market design perspective, three important market outcomes are of primary interest: the speed of price discovery, the market efficiency, and social welfare. In our iterative market mechanism, the number of market iterations is an effective measure of price discovery. Because our bundle auction market guarantees full allocative efficiency (Corollary 2), we focus on the distribution of social welfare under various scenarios.

Illustration of price dynamics in a market with 50 agents  
![](/api/attachments/P8E6DJJ8/fulltext/images/b2606eb9f0b353862e7bc90caf05ac2b3b0c6066c2359565ecb0d8e3b8f3fca2.jpg)

Table 3 Summary Statistics for O = 0 4O = 15: Market Performance and Wealth Effect

<table><tr><td rowspan="2">Inventory policy</td><td rowspan="2">Market scenario</td><td colspan="4">Panel (a) Mean number of iterations</td><td colspan="4">Panel (b) Mean wealth ratio</td></tr><tr><td>P=0.2</td><td>P=0.5</td><td>P=0.8</td><td>P=1</td><td>P=0.2</td><td>P=0.5</td><td>P=0.8</td><td>P=1</td></tr><tr><td rowspan="4">NA</td><td>k10m2</td><td>65.87(39.29)</td><td>42.77(27.52)</td><td>28.45(20.01)</td><td>23.35(16.74)</td><td>0.88(0.80)</td><td>0.92(0.79)</td><td>0.95(0.76)</td><td>0.97(0.74)</td></tr><tr><td>k10m8</td><td>288.06(94.70)</td><td>139.14(49.23)</td><td>101.49(31.19)</td><td>52.50(23.42)</td><td>0.63(0.76)</td><td>0.69(0.73)</td><td>0.75(0.72)</td><td>0.79(0.70)</td></tr><tr><td>k50m2</td><td>96.54(80.27)</td><td>55.66(45.18)</td><td>34.25(27.29)</td><td>25.93(20.87)</td><td>0.94(0.78)</td><td>0.97(0.75)</td><td>0.98(0.70)</td><td>0.98(0.68)</td></tr><tr><td>k50m8</td><td>302.98(221.82)</td><td>143.72(99.69)</td><td>81.35(49.79)</td><td>48.64(35.30)</td><td>0.82(0.65)</td><td>0.88(0.63)</td><td>0.92(0.59)</td><td>0.93(0.58)</td></tr><tr><td rowspan="4">SS</td><td>k10m2</td><td>67.47(41.92)</td><td>44.86(30.55)</td><td>31.37(23.93)</td><td>27.25(21.53)</td><td>1.05(0.82)</td><td>1.04(0.79)</td><td>1.06(0.76)</td><td>1.07(0.74)</td></tr><tr><td>k10m8</td><td>296.08(94.40)</td><td>155.40(54.40)</td><td>85.21(36.24)</td><td>78.49(29.55)</td><td>1.87(0.80)</td><td>1.05(0.78)</td><td>1.00(0.75)</td><td>0.98(0.72)</td></tr><tr><td>k50m2</td><td>98.77(86.46)</td><td>58.28(51.20)</td><td>37.50(34.84)</td><td>30.93(28.93)</td><td>1.11(0.83)</td><td>1.09(0.76)</td><td>1.10(0.72)</td><td>1.10(0.69)</td></tr><tr><td>k50m8</td><td>332.86(229.09)</td><td>143.73(99.50)</td><td>73.16(50.90)</td><td>53.97(36.79)</td><td>1.37(0.71)</td><td>1.06(0.66)</td><td>1.05(0.62)</td><td>1.04(0.60)</td></tr><tr><td rowspan="4">SP</td><td>k10m2</td><td>65.06(43.40)</td><td>41.96(31.88)</td><td>30.40(25.42)</td><td>25.81(23.25)</td><td>0.86(0.55)</td><td>0.90(0.53)</td><td>0.94(0.54)</td><td>0.97(0.56)</td></tr><tr><td>k10m8</td><td>285.00(108.27)</td><td>149.80(69.88)</td><td>92.93(45.93)</td><td>67.48(37.44)</td><td>0.73(0.75)</td><td>0.79(0.76)</td><td>0.84(0.78)</td><td>0.89(0.78)</td></tr><tr><td>k50m2</td><td>99.46(79.16)</td><td>54.63(46.85)</td><td>34.48(31.61)</td><td>27.73(26.34)</td><td>0.93(0.51)</td><td>0.96(0.47)</td><td>0.98(0.43)</td><td>0.98(0.42)</td></tr><tr><td>k50m8</td><td>309.55(228.11)</td><td>145.56(103.94)</td><td>74.10(55.16)</td><td>53.13(41.18)</td><td>0.87(0.64)</td><td>0.93(0.62)</td><td>0.96(0.61)</td><td>0.97(0.58)</td></tr><tr><td rowspan="4">FISS</td><td>k10m2</td><td>66.31(42.12)</td><td>42.46(30.86)</td><td>29.83(23.69)</td><td>25.62(21.69)</td><td>0.87(0.81)</td><td>0.93(0.80)</td><td>0.96(0.75)</td><td>0.98(0.74)</td></tr><tr><td>k10m8</td><td>281.89(88.60)</td><td>138.55(51.40)</td><td>75.03(33.35)</td><td>55.30(28.27)</td><td>0.73(0.76)</td><td>0.80(0.75)</td><td>0.86(0.73)</td><td>0.90(0.71)</td></tr><tr><td>k50m2</td><td>98.60(85.71)</td><td>56.51(52.00)</td><td>36.30(34.68)</td><td>28.30(28.02)</td><td>1.03(0.82)</td><td>1.01(0.77)</td><td>1.01(0.72)</td><td>1.00(0.69)</td></tr><tr><td>k50m8</td><td>302.35(215.81)</td><td>140.96(98.73)</td><td>70.29(49.04)</td><td>51.77(36.43)</td><td>0.98(0.68)</td><td>0.98(0.65)</td><td>0.98(0.61)</td><td>0.98(0.59)</td></tr><tr><td rowspan="4">FISP</td><td>k10m2</td><td>64.00(44.25)</td><td>42.51(33.13)</td><td>29.54(26.25)</td><td>25.30(23.84)</td><td>0.99(0.77)</td><td>1.01(0.78)</td><td>1.01(0.79)</td><td>1.01(0.79)</td></tr><tr><td>k10m8</td><td>291.88(98.93)</td><td>138.27(60.54)</td><td>83.40(40.14)</td><td>55.59(32.47)</td><td>0.76(0.78)</td><td>0.82(0.80)</td><td>0.86(0.82)</td><td>0.89(0.81)</td></tr><tr><td>k50m2</td><td>93.38(77.34)</td><td>54.79(47.58)</td><td>35.18(33.00)</td><td>28.02(27.90)</td><td>1.21(0.85)</td><td>1.18(0.82)</td><td>1.09(0.80)</td><td>1.09(0.79)</td></tr><tr><td>k50m8</td><td>304.24(225.95)</td><td>143.28(102.54)</td><td>74.25(54.60)</td><td>58.22(41.01)</td><td>0.99(0.74)</td><td>1.00(0.73)</td><td>0.99(0.71)</td><td>0.99(0.70)</td></tr></table>

Note. Data are averaged across four learning strategies.

the final wealth minus the initial cash endowment. The total system gain is the total reduction of operating costs from all agents. If the dealer earns zero wealth in the auction, then all system gains are allocated among agents. Thus, the wealth ratio would be one. If the dealer earns positive (negative) wealth in the auction, then the total agent net wealth would be less (more) than the total system gain. As a result, the wealth ratio would be less (greater) than one. In short, a higher wealth ratio implies higher agent surplus. We report the summary statistics for both the number of market iterations and the wealth ratio in Table 3.

As shown in panel (a) of Table 3, given a market scenario and the dealer’s inventory policy, more synchronized communication (higher P) leads to quicker market convergence. Moreover, both the number of market participants and the size of the trading bundle negatively impact market convergence. In a highly synchronized environment (e.g., P = 1) with a small number of agents (e.g., 10 agents) trading simple bundles (e.g., 2 shared resources), the average number of rounds for market convergence is as low as 16.74. When the market is highly asynchronous (e.g., P = 002) and relatively large (e.g., 50 agents) and complicated (e.g., 8 shared resources), the average number of rounds for convergence in the worst case is 332.86. This is not a computational burden for artificial traders. For example, the average computing time for the worst-case scenario is less than a second.

Table 4 Regression Model and Coefficient Estimates: Effects on Market Convergence

<table><tr><td rowspan="3">Model</td><td colspan="4">Dealer initial resources (O=0)</td><td colspan="4">Dealer initial resources (O=1)</td></tr><tr><td colspan="2">m=2</td><td colspan="2">m=8</td><td colspan="2">m=2</td><td colspan="2">m=8</td></tr><tr><td>k=10</td><td>k=50</td><td>k=10</td><td>k=50</td><td>k=10</td><td>k=50</td><td>k=10</td><td>k=50</td></tr><tr><td>Intercept</td><td>75.12***</td><td>118.07***</td><td>334.05***</td><td>406.58***</td><td>43.29***</td><td>96.20***</td><td>103.09***</td><td>272.66***</td></tr><tr><td>AsyCom</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $P_{0.5}-P_{0.2}$ </td><td>-22.97***</td><td>-40.82***</td><td>-151.15***</td><td>-186.05***</td><td>-11.40***</td><td>-33.23***</td><td>-39.89***</td><td>-123.28***</td></tr><tr><td> $P_{0.8}-P_{0.2}$ </td><td>-36.30***</td><td>-62.24***</td><td>-217.15***</td><td>-259.86***</td><td>-18.34***</td><td>-49.50***</td><td>-59.61***</td><td>-172.26***</td></tr><tr><td> $P_1-P_{0.2}$ </td><td>-40.82***</td><td>-69.27***</td><td>-237.13***</td><td>-281.49***</td><td>-20.78***</td><td>-55.38***</td><td>-66.75***</td><td>-186.02***</td></tr><tr><td>Inventory</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SS-NA</td><td>2.54***</td><td>3.50***</td><td>10.01***</td><td>3.08</td><td>3.59***</td><td>6.95***</td><td>4.01*</td><td>2.42</td></tr><tr><td>SP-NA</td><td>1.14***</td><td>1.03</td><td>4.88*</td><td>0.24</td><td>5.09***</td><td>2.59*</td><td>15.75***</td><td>5.44</td></tr><tr><td>FISS-NA</td><td>0.74</td><td>1.67</td><td>-0.40</td><td>-2.11</td><td>3.70***</td><td>6.70***</td><td>0.77</td><td>-1.65</td></tr><tr><td>FISP-NA</td><td>0.77</td><td>-0.91</td><td>1.18</td><td>1.80</td><td>5.98***</td><td>3.05*</td><td>8.39**</td><td>4.38</td></tr><tr><td>Learning</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MS-MA</td><td>-10.39***</td><td>-24.01***</td><td>-21.02***</td><td>-68.07***</td><td>-5.25***</td><td>-20.92***</td><td>-7.70***</td><td>-46.22***</td></tr><tr><td>FS-MA</td><td>-16.35***</td><td>-34.23***</td><td>-79.04***</td><td>-124.46***</td><td>-7.72***</td><td>-28.32***</td><td>-20.77***</td><td>-81.11***</td></tr><tr><td>FA-MA</td><td>-12.72***</td><td>-27.84***</td><td>-78.02***</td><td>-114.28***</td><td>-6.09***</td><td>-23.84***</td><td>-19.12***</td><td>-75.14***</td></tr><tr><td>R-square</td><td>0.65</td><td>0.54</td><td>0.55</td><td>0.50</td><td>0.19</td><td>0.26</td><td>0.16</td><td>0.25</td></tr></table>

<sup>∗</sup>p < 0005, <sup>∗∗</sup>p < 0001, and <sup>∗∗∗</sup>p < 00001.

Although our algorithm guarantees termination at the optimal resource allocation in a finite number of trades, actual traders may not be satisfied with just a promise of finiteness. For human traders, we suggest a pure call market design (P = 1) to synchronize market communication and reduce the total number of iterations. Alternatively, a market mechanism designer may trade off the allocative efficiency with the total number of rounds for convergence (i.e., terminate the market iteration when the allocative efficiency reaches a threshold level such as 98%). Our computational data suggested that agent trading in early rounds significantly contributes to the total allocative efficiency while trading in later rounds mainly fine-tunes the allocation to the market equilibrium. Thus, terminating the market process early may not result in unacceptable deviations from optimal.

When the dealer does not have initial resource ownership 4O = 05, data in panel (b) shows that the dealer generated positive profit under NA and SP while she earned negative net wealth under almost all instances of the SS inventory policy. This is mainly because the dealer’s objective was to maintain her target inventory levels without considering the prices she paid for the resources. Comparing FISS(FISP) with SS(SP), we see that the informational advantage helped increase the dealer’s wealth under the SS policy but did not seem helpful under the SP policy. The dealer also experienced profit loss under FISS and FISP in large markets with simple bundles being traded. Because a smaller wealth ratio implies lower agent welfare, we see that asynchronous communication will lead to more agent welfare loss. In contrast, when the dealer initially holds all shared resources 4O = 15, she earns positive profit under all five inventory policies. Moreover, the dealer earns higher profit when the market communication is more synchronized.

Finally, comparing O = 0 and O = 1, we see that the dealer’s inventory centralization has positive impacts on the market performance and the dealer’s wealth. For example, in the worst-case scenario k50m8 and P = 002, the market converged between 215.81 and 229.09 rounds when the dealer had all initial resources in contrast to the convergence range of 302.35 to 332.86 rounds when the initial resources were randomly allocated among agents. We further observe that, though the wealth ratio varied from 0.63 to 1.87 in initial random resource allocation, it varied from 0.42 to 0.85 when the dealer held all of the initial shared resources. On average, the dealer earns a higher profit when she initially owns all the shared resources.

## 6.3. Impact of Key Market Design Parameters on Market Performance

In order to understand the general effect of different market design options on market performance, we ran regression models at different levels of granularity under different scenarios of the initial resource allocation. The benchmark scenario is the asynchronous communication $( P = 0 . 2 )$ the naïve inventory policy $( V = \mathrm { { N A } ) }$ , and myopic learning with asymmetric access to information $\begin{array} { r } { ( \hat { L } = \mathbf { M } \mathbf { A } ) } \end{array}$ . Table 4 shows the intercept and coefficients from the model estimation.<sup>7</sup>

The overall regression model is highly significant and yields R-square values from 0.5 to 0.65 when the dealer does not hold initial resources and from 0.19 to 0.26 when the dealer has all of the initial resources. The coefficients for asynchronous communication and agent learning are highly significant at the 0.001 level and with the expected signs. For example, under $O = 0 ,$ , if the asynchronous communication level changes from $P = 0 . 2$ to $P = 1$ , on average, the number of iterations will increase by 40.82 rounds in the k10m2 market and by 281.49 rounds in the k50m8 market. The larger the bundle size, the more likely it is that market performance is negatively affected by asynchronous communication. Overall, higher levels of asynchronous communication (smaller P) monotonically degrade market performance under all scenarios.

Among the four learning models, we see that the biggest performance improvement was obtained under the FS method. For instance, under $O = 0 ,$ the change of agent learning model from MA to FS can, on average, increase the market performance by 16.35 rounds in the k10m2 market and by 124.46 rounds in the k50m8 market. It suggests that the ability to symmetrically access market information and actively predict market price movement can lead to better market performance. A practical significance of this finding is that the mechanism designer may consider increasing market information transparency and facilitate agent learning to mitigate the negative effect of asynchronous communication on market performance.

Although there is no significant performance difference between the naïve and other active inventory policies in large market trading complex bundles, the NA policy outperforms SS and SP policies when the market trades relatively simple bundles or when the number of agents is not large. This suggests that it may not be desirable for the dealer to perform active market intervention in relatively simple trading environments such as small numbers of bundles or market participants, especially when the dealer has the resource ownership.

In addition, the dealer’s informational advantage can mitigate the effect of delayed convergence in all market scenarios when O = 0. For example, in the market of 10 agents and 8 shared resources, the SS policy leads to an average 10 rounds delay in convergence but the FISS policy has the effect of speeding up convergence by 0.4 rounds. When O = 1, the dealer’s informational advantage can mitigate the effect of delayed convergence in markets trading complex bundles, but it has no effect in markets trading simple bundles. Overall, the effect of true market information on market performance is positive but does not seem statistically significant. However, the negative signs of the estimated coefficients show the potential that the dealer’s liquidity provision can improve market performance when the dealer has better market price information than agents.

We further conducted paired t-tests on the effect of dealer inventory policies on market performance under different levels of agent asynchronous communication and learning models. A representative scenario $L = \mathbf { M } \mathbf { A }$ is presented in Table 1 in the online supplement. There are several interesting observations. First, different inventory policies do not yield statistically significant market performance when the market communication is highly asymmetric and asynchronous (L = MA, $P = 0 . 2 , 0 . { \overset { \cdot } { 5 } } )$ . This is probably because of the difficulty of matching bundles when agents cannot coordinate the timing of their decision making to facilitate trades among themselves. Second, when the market is fully synchronized $( P = 1 )$ , we observe that the naïve inventory policy either outperformed or yielded a comparable performance versus other active inventory policies (statistically significant at 0.05 level). It seems to suggest that there is no need for the dealer to perform active market intervention because the synchronized market has an inherent market liquidity effect in bundle execution.

## 7. Extensions

In the previous section, we studied several key factors that affect market performance and the agent surplus under the controlled experiment design. In this section, we run additional experiments to allow for a number of extensions, including a test for agent strategy and randomization of factors. Our computational results suggest that all qualitative insights are still valid and that the market model can be generalized to more realistic market environments.

## 7.1. Strategic Bidding

As discussed earlier, agent strategic behaviors mainly fall into two general categories: strategic bundle selection and pricing. In our controlled experiment, strategic bundle selection was enabled by allowing agents to predict market price movement. In this section, we run additional experiments to allow for strategic bidding.

We start with the original problem structure that has 30 replications for 16 macro- and microlevel combinations (see Table 2). The test sample size is 480. We allow agents to randomly choose market communication frequency $P _ { j }$ and freely select a learning model $L _ { j } .$ We use three bidding strategies and the dealer’s five inventory policies as treatments. The total number of observations in this experiment is $4 8 0 \times 3 \times 5 = 7 , 2 0 0$ The three bidding strategies are: truthful bidding (TRUE), random bidding (RAN), and fixed percentage bidding (FIX). In the random bidding strategy, an agent bids any random value between the true bundle valuation and the lowest market acceptable price (the current winning bid price plus a small increment of epsilon). In the fixed percentage bidding strategy, we assume that the agent always bids at 80% of the acceptable bidding range (the interval between the lowest market acceptable price and the true valuation of the bundle). Table 5 summarizes the effects of different strategies on market performance and agent surplus.

Not surprisingly, the summarized data in panel (a) of Table 5 shows that the best market performance occurs when agents bid truthfully. The truthful strategy outperforms the fixed percentage bidding strategy, which outperforms the random bidding strategy. The effect of strategic pricing is consistent with the findings from the original Guo et al. (2007) study, which derived the same ranking of agent strategy and found that agent strategic pricing merely slowed the speed of market convergence without impacting the market finite convergence property. Our current study shows that strategic bundle selection is helpful but that strategic pricing definitely slows down market convergence.

Because the dealer earns positive profit if the wealth ratio is less than one, panel (b) shows that the dealer is always profitable under the naïve inventory policy but will incur some profit loss when adopting active inventory policies, especially when the number of market participants is large.

In order to see whether the dealer’s different inventory policies would have an effect on market liquidity, we performed several additional analyses detailed in the online supplement. In Table 2, we observe that both the dealer’s and the market total trading volume increase as either the number of market participants or the number of shared resources increases. Moreover, the effect of market size is larger than the effect of bundle complexity on market total trading volume.

Table 3 in the online supplement shows that market price variation is not statistically significant under different inventory policies regardless of agent bidding strategies. Although financial market theory suggests that high trading volume corresponds to low price volatility, this does not seem to be supported by our trading data. We also see that the dealer has actively traded in complex market environments without significantly improving market performance. This indicates that a dealer’s active intermediation does not necessarily lead to quicker price discovery. We caution the mechanism designer that traditional financial market insights may not be directly applied and transferred to the BTM trading environment.

## 7.2. Randomization

In this section, we further randomize our market experiment to reflect more realistic market participation. First, we allow agents to differ in their internal structures in terms of the number of independent resources $a _ { j }$ and the number of activities $b _ { j }$ to manage. Second, in addition to the market communication frequencies and learning strategies, agents may choose their own bidding strategies. In this randomized experiment, we still adopted the base macrolevel market design as in the controlled experiment (see Table 2). This resulted in four market configurations consisting of different numbers of agents and shared resources. Under each market scenario, we generated 120 random samples. The dealer’s inventory strategy was the only treatment. As a result, we had $4 \times 1 2 0 \times 5 = 2$ 1400 observations for a formal statistical test.

Table 5 Summary Statistics Under Different Bidding Strategies

<table><tr><td colspan="2">Market</td><td>Inventory policy</td><td colspan="3">Panel (a) Mean number of iterations</td><td colspan="3">Panel (b) Mean wealth ratio</td></tr><tr><td>k</td><td>m</td><td>V</td><td>TRUE</td><td>RAN</td><td>FIX</td><td>TRUE</td><td>RAN</td><td>FIX</td></tr><tr><td rowspan="10">10</td><td rowspan="5">2</td><td>NA</td><td>39.98</td><td>69.13</td><td>53.94</td><td>0.92</td><td>0.97</td><td>0.97</td></tr><tr><td>SS</td><td>43.19</td><td>170.22</td><td>57.58</td><td>1.04</td><td>1.18</td><td>1.37</td></tr><tr><td>SP</td><td>41.10</td><td>71.45</td><td>54.11</td><td>0.92</td><td>0.99</td><td>0.98</td></tr><tr><td>FISS</td><td>41.28</td><td>67.47</td><td>55.09</td><td>0.95</td><td>0.99</td><td>0.97</td></tr><tr><td>FISP</td><td>39.28</td><td>70.48</td><td>53.96</td><td>1.02</td><td>1.11</td><td>1.05</td></tr><tr><td rowspan="5">8</td><td>NA</td><td>113.21</td><td>249.23</td><td>132.73</td><td>0.71</td><td>0.89</td><td>0.85</td></tr><tr><td>SS</td><td>146.73</td><td>201.50</td><td>151.64</td><td>1.03</td><td>1.94</td><td>1.42</td></tr><tr><td>SP</td><td>147.23</td><td>217.14</td><td>142.23</td><td>0.80</td><td>0.96</td><td>0.94</td></tr><tr><td>FISS</td><td>119.99</td><td>182.54</td><td>146.11</td><td>0.83</td><td>0.96</td><td>0.92</td></tr><tr><td>FISP</td><td>127.58</td><td>304.87</td><td>142.21</td><td>0.81</td><td>0.99</td><td>0.96</td></tr><tr><td rowspan="10">50</td><td rowspan="5">2</td><td>NA</td><td>51.68</td><td>71.46</td><td>59.43</td><td>0.97</td><td>0.99</td><td>0.99</td></tr><tr><td>SS</td><td>55.70</td><td>70.39</td><td>64.79</td><td>1.09</td><td>1.14</td><td>1.12</td></tr><tr><td>SP</td><td>52.74</td><td>69.54</td><td>65.98</td><td>0.97</td><td>1.02</td><td>0.99</td></tr><tr><td>FISS</td><td>54.01</td><td>68.64</td><td>58.98</td><td>1.02</td><td>1.01</td><td>1.02</td></tr><tr><td>FISP</td><td>50.38</td><td>69.70</td><td>61.40</td><td>1.10</td><td>1.17</td><td>1.16</td></tr><tr><td rowspan="5">8</td><td>NA</td><td>129.63</td><td>207.85</td><td>161.46</td><td>0.90</td><td>0.96</td><td>0.95</td></tr><tr><td>SS</td><td>123.71</td><td>187.06</td><td>134.28</td><td>1.06</td><td>1.28</td><td>1.65</td></tr><tr><td>SP</td><td>126.85</td><td>153.95</td><td>133.39</td><td>0.94</td><td>1.03</td><td>1.03</td></tr><tr><td>FISS</td><td>122.79</td><td>306.56</td><td>123.00</td><td>0.98</td><td>1.02</td><td>1.02</td></tr><tr><td>FISP</td><td>121.55</td><td>162.61</td><td>159.61</td><td>1.00</td><td>1.05</td><td>1.07</td></tr></table>

Table 4 in the online supplement shows that bundle size or complexity has a major impact on market convergence. Furthermore, except for the safety stock inventory policy, all other inventory policies yielded quicker market convergence in larger markets when trading complex bundles. This suggests that our BTM framework is scalable to larger-sized auctions with larger-sized bundles.

## 8. Summary, Conclusions, and Future Research

This paper extends the original BTM framework to a more general, asynchronous market implementation environment. The new market model allows a dealer to perform active market intervention by adopting sophisticated inventory policies. We also incorporate individual agent learning so that each agent can form expectations of the market price movements. Under the extended framework, we theoretically justify finite convergence and optimality properties of the market. We further study how a number of key market design parameters including market communication and information exchange patterns, the intermediary’s role of liquidity provision, and agents’ responsive learning ability and strategic bidding could affect market performance. Understanding the joint impact of these factors on market performance appears vital to a real-world deployment of the proposed market framework in an asynchronous Internet environment.

Generally speaking, agents experience more welfare loss in more asynchronous market environments. Market performance is negatively affected by both asynchronous communication and market information asymmetry but is positively affected by agent learning. In terms of agent strategic behavior, we find that strategic bundle selection would speed up but strategic pricing would slow down market convergence.

Contrary to the conventional wisdom that a dealer’s intertemporal liquidity provision may improve market performance, we find that it is generally undesirable to perform active market intervention in simple market trading environments where an inherent market liquidity effect dominates, especially when the dealer has significant resource ownership. Moreover, the dealer’s initial resources centralization has positive impacts on the market performance and the dealer’s wealth. When deciding to adopt active market intermediation, the dealer tends to earn positive profit under the speculative price policy but negative profit under the safety stock policy. Though the effect is insignificant, our trading data also suggests that the dealer’s informational advantage has the potential to improve market performance and dealer profit under the safety stock policy.

Interestingly, we observe that, though bundle complexity has a bigger impact than market size on market convergence, market size has a larger effect than bundle complexity on trading volume. We further find that high trading volume does not correlate to low price volatility and quicker price discovery. Therefore, we caution the mechanism designer that traditional insights from financial market design may not be directly transferrable to the bundle trading market environment. This poses additional challenges for practical bundle trading, double auction market design.

Our major contribution of this study is an extended BTM mechanism in an asynchronous market environment characterized by asymmetric information, agent strategic trading, and a dealer’s active market intervention. We prove that the convergence of the proposed algorithm to an optimal solution leads to an efficient auction design. Our computational market simulation further shows that the algorithmic implementation is robust to a number of dealer and agent manipulations. The proposed framework provides flexibility, scalability, and robustness to Internet-based market implementations. It can extend the current market ability to more effectively handle sophisticated trades.

Our proposed BTM framework offers additional insights into existing market mechanism designs. For example, the proposed framework has the potential to improve upon currently active and heavily traded markets such as the European Energy Exchange by allowing for more flexible bundle combinations (e.g., specifying the sell and buy items in the same bundle), by relaxing the “fill-or-kill” constraint to divisible trades, and by the use of a market intermediary to supply liquidity.

Additionally, formal theories of organizational structure treat the organization as a mechanism to assemble costly acquired, distributed decisionrelevant information (Marschak 2006). As Internetoriented organizational models such as networked organizations and virtual organizations emerge, our findings shed new light on designing global information systems that not only facilitate the efficient allocation of key organizational resources but also enable such organizational structural changes. Our proposed approach provides a useful framework to address mechanism implementation challenges in formal models of distributed organization.

There are several limitations and possible extensions. We have not provided a formal analysis of how market makers should be compensated for taking on affirmative obligations to supply liquidity. In general, determining the optimal level of inventory provision or price speculation is hard, if not impossible, especially under a dynamic market trading environment like ours. In this research, we use random, predetermined, static inventory policies for the dealer. It would be interesting to see how the dealer could adjust her inventory policies as well as the preferred inventory positions as she updates her belief when more market information is available. This leaves questions on optimal dynamic liquidity provisions in computational market settings to future research.

As is typical in many studies, we do not consider transaction fees. An interesting question is whether a dealer would have an incentive to prolong the bidding process if transaction fees were charged. From Table 3, we see that agents generally incur more welfare loss if the market takes longer to converge. From the system optimization perspective, there still exist profitable trades if a dealer who does not engage in production intentionally holds some inventory. The dealer, instead, may incur a cost of holding inventory but may earn profit by charging transaction fees to agents. It is not clear whether the cost could be offset by the gain. How transaction fees would affect a dealer’s incentive to trade as well as affect market convergence is an interesting future research direction.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1110.0366.

## Appendix

## General model notation

c: Total available shared resources in the system

$j = 1 , \ldots , k \colon$ Index of agents

$\dot { d } _ { j } \in R ^ { b _ { j } }$ : Vector of agent j’s cost

$x _ { j } \in R ^ { b _ { j } } \colon b _ { j }$ -dimensional decision variables controlled by agent j

$N _ { j } \in R ^ { a _ { j } \times b _ { j } } , C _ { j } \in R ^ { m \times b _ { j } } \colon a _ { j } \times b _ { j }$ and m × b<sub>j</sub> activity matrices, respectively

n ∈ R<sup>aj</sup> : a -dimensional capacity vectors of agent j’s independent resources

$c _ { j } \in R ^ { m } \colon$ : m-dimensional vectors of agent j’s shared resources

e 4c 5: Agent j’s cash when his shared resource is $c _ { j }$

$z _ { j } ( c _ { j } ) { \mathrm { : } }$ : Agent j’s operating cost when his shared resource is $c _ { j }$

$W _ { j } ( c _ { j } ) = e _ { j } ^ { ' } ( c _ { j } ) - z _ { j } ( c _ { j } ) :$ : Agent j’s wealth when the shared resource is $c _ { j }$

w ∈ $R ^ { m } { : }$ m-dimensional bundle (a bundle containing m shared resources)

l 4w5: Agent j’s bidding price for bundle w

${ \dot { H } } _ { j } , I _ { j } { \mathrm { : } }$ Agent j’s limited and unlimited order sets, respectively

$w _ { i } ^ { i } \in R ^ { m } , i \in I _ { i } \colon$ Agent j’s ith limited bundle in the order set $\dot { I _ { j } }$

$u _ { i } ^ { \check { h } } \in R ^ { m } , h \in H _ { j }$ : Agent j’s hth unlimited bundle in the order set H

$\bar { w } _ { i R } \in R ^ { m } ;$ Aggregated trading bundles for agent j up to round R

$p \in R ^ { m } ;$ : m-dimensional prices for the shared resources

$\tilde { p } _ { j R } \in R ^ { m } ;$ Agent j’s forecasted market price in round R

$\vec { c _ { 0 } } \in R ^ { m }$ : m-dimensional vectors of the dealer’s inventory

$e _ { 0 } ( c _ { 0 } ) { : }$ : The dealer’s cash endowment when she owns $c _ { 0 }$ inventory

$s \in R ^ { m . } $ m-dimensional vector of the dealer’s safety stock level

$r \in { \cal R } ^ { m }$ : m-dimensional vector of the dealer’s speculative price level

## Experimental setting notation

k ∈ 8101 509: Number of agents

$m \in \{ 2 , 8 \}$ : Number of shared resources in a bundle (size of a bundle)

$a _ { j } \in \{ 2 , 8 \}$ : Agent j’s number of independent resources

$b _ { i } ^ { ' } \in \{ 4 , 8 \}$ : Agent j’s number of production activities

$\mathring { P _ { j } } \in \{ 0 . 2 , 0 . 5 , 0 . 8 ,$ 19: Agent j’s asynchronous communication level

$L _ { i } \in \{ \mathrm { M A } , \mathrm { M S } , \mathrm { F S } , \mathrm { F A } \} \colon$ Agent j’s learning model

$\begin{array} { r } { \dot { V } \in \{ \mathrm { N A } , \mathrm { S S } , \mathrm { S P } , \mathrm { F I S S } , } \end{array}$ FISP9: The dealer’s inventory policies (market intermediation models)

$O \in \{ 0 , 1 \} \mathrm { : }$ : The dealer’s resource ownership MAPN: Moving average price norm (to measure aggregate price variation)

X: The dealer’s periodic contact cycle length

## References

Adomavicius, G., A. Gupta. 2005. Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2) 169–185.

Albrecht, M. 2009. Supply chain coordination mechanisms: New approaches for collaborative planning. Lecture Notes in Economics and Mathematical Systems, 1st ed. Springer, New York.

Amihud, Y., H. Mendelson. 1980. Dealership market: Market making with inventory. J. Financial Econom. 8(1) 31–53.

Ausubel, L. M. 2004. An efficient ascending-bid auction for multiple objects. Amer. Econom. Rev. 94(5) 1452–1475.

Ba, S., J. Stallaert, A. B. Whinston. 2001a. Research commentary: Introducing a third dimension in information systems design— The case for incentive alignment. Inform. Systems Res. 12(3) 225–239.

Ba, S., J. Stallaert, A. B. Whinston. 2001b. Optimal investment in knowledge within a firm using a market mechanism. Management Sci. 47(9) 1203–1219.

Bertsekas, D. P. 1979. A distributed algorithm for the assignment problem. MIT Lab, Information and Decision Systems Report, Massachusetts Institute of Technology, Cambridge, MA.

Bertsekas, D. P. 1988. The auction algorithm: A distributed relaxation method for the assignment problem. Ann. Oper. Res. 14 105–123.

Bertsekas, D. P., J. N. Tsitsiklis. 1997. Introduction to Linear Optimization. Athena Scientific, Belmont, MA.

Bichler, M., P. Shabalin, A. Pikovsky. 2009. A computational analysis of linear price iterative combinatorial auction formats. Inform. Systems Res. 20(1) 33–59.

Bikhchandani, S., J. W. Mamer. 1997. Competitive equilibrium in an exchange economy with indivisibles. J. Econom. Theory 74(2) 385–413.

Bikhchandani, S., J. M. Ostroy. 2002. The package assignment model. J. Econom. Theory 107(2) 337–406.

Chu, L. Y. 2009. Truthful bundle/multiunit double auctions. Management Sci. 55(7) 1184–1198.

Cramton, P. 1997. The FCC spectrum auctions: An early assessment. J. Econom. Management Strategy 6(3) 431–495.

Cramton, P., Y. Shoham, R. Steinberg. 2006. Combinatorial Auctions. The MIT Press, Cambridge, MA.

Dantzig, G. B., P. Wolfe. 1960. The decomposition principle for linear programs. Oper. Res. 8(1) 101–111.

Demange, G., D. Gale, M. Sotomayor. 1986. Multi-item auctions. J. Political Econom. 94(4) 863–872.

De Vries, S., J. Schummer, R. Vohra. 2007. On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132(1) 95–118.

Fan, M., J. Stallaert, A. B. Whinston. 2003. Decentralized mechanism design for supply chain organizations using auction market. Inform. Systems Res. 14(1) 1–22.

Friedman, D., S. Sunder. 1994. Experimental Methods: A Premier for Economists. Cambridge University Press, Cambridge, UK.

Gallien, J., L. M. Wein. 2005. A smart market for industrial procurement with capacity constraints. Management Sci. 51(1) 76–91.

Guo, Z., G. J. Koehler, A. B. Whinston. 2007. A market-based optimization algorithm for distributed systems. Management Sci. 53(8) 1345–1358.

Harris, L. 2002. Trading and Exchanges: Market Microstructure for Practitioners. Oxford University Press, Oxford, UK.

Hogan, W. W., E. G. Read, B. J. Ring. 1996. Using mathematical programming for electricity spot pricing. Internat. Trans. Oper. Res. 3(3/4) 209–221.

Kelso, A. S., V. P. Crawford. 1982. Job matching, coalition formation, and gross substitutes. Econometrica 50(6) 1483–1504.

Kothari, A., T. Sandholm, S. Suri. 2004. Solving combinatorial exchanges: Optimality via a few partial bids. Proc. Third Internat. Joint Conf. Autonomous Agents and Multiagent Systems (AAMAS’04), Vol. 3, New York.

Leonard, H. B. 1983. Elicitation of honest preferences for the assignment of individuals to positions. J. Political Econom. 91(3) 461–479.

Lubin, B., A. I. Juda, R. Cavallo, S. Lahaie, J. Shneidman, D. C. Parkes. 2008. ICE: An expressive iterative combinatorial exchange. J. Artificial Intelligence Res. 33 33–77.

Makridakis, S. G., S. C. Wheelwright, V. E. McGee. 1983. Forecasting. John Wiley & Sons Inc., Hoboken, NJ.

Marschak, T. 2006. Organization structure. T. Hendershott, ed. Handbooks in Information Systems, Vol. 1. Elsevier, Amsterdam, 201–284.

Mas-Colell, A., M. D. Whinston, J. R. Green. 1995. Microeconomic Theory. Oxford University Press, Oxford, UK.

McAfee, R. P. 1991. Efficient allocation with continuous quantities. J. Econom. Theory 53(1) 51–74.

McAfee, R. P. 1992. A dominant strategy double auction. J. Econom. Theory 56(2) 434–450.

McCabe, K., S. Rassenti, V. Smith. 1990. Auction design for composite goods: The natural gas industry. J. Econom. Behav. Organ. 14(9) 127–149.

McCabe, K., S. Rassenti, V. Smith. 1991. Smart computer-assisted markets. Science 254(5031) 534–538.

Meeus, L., K. Verhaegen, R. Belmans. 2009. Block order restrictions in combinatorial electric energy auctions. Eur. J. Oper. Res. 196(3) 1202–1206.

Myerson, R. B., M. A. Satterthwaite. 1983. Efficient mechanisms for bilateral trading. J. Econom. Theory 29(2) 265–281.

Nisan, N., A. Ronen. 2001. Algorithmic mechanism design. Games Econom. Behav. 35(1/2) 166–196.

O’Hara, M. 1995. Market Microstructure Theory. Blackwell Publishing, Malden, MA.

Parkes, D. C. 1999. iBundle: An efficient ascending price bundle auction. Proc. ACM Conf. Electronic Commerce, ACM Press, New York, 148–157.

Parkes, D. C. 2006. Iterative combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions, Chapter 2. MIT Press, Cambridge, MA, 41–78.

Parkes, D. C., L. H. Ungar. 2000. Iterative combinational auctions: Theory and practice. 17th National Conf. Artificial Intelligence (AAAI), 74–81.

Pekec, A., M. H. Rothkopf. 2003. Combinatorial auction design. Management Sci. 49(11) 1485–1503.

Raffensperger, J. F., W. M. Mark, E. G. Read. 2009. A deterministic smart market model for ground water. Oper. Res. 57(6) 1333–1346.

Rassenti, S. J., V. L. Smith, R. L. Bluffing. 1982. A combinatorial auction mechanism for airport time slot allocation. Bell J. Econom. 13(2) 402–417.

Roberts, S. W. 1959. Control chart tests based on geometric moving averages. Technometrics 1 239–250.

Rothkopf, M. H. 2007. Thirteen reasons why the Vickrey-Clarke-Groves process is not practical. Oper. Res. 55(2) 191–197.

Rothkopf, M. H., A. Pekec, R. M. Harstad. 1998. Computationally manageable combinational auctions. Management Sci. 44(8) 1131–1147.

Sandholm, T., C. Boutilier. 2006. Preference elicitation in combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions, Chapter 10. MIT Press, Cambridge, MA.

Scheffel, T., A. Pikovsky, M. Bichler, K. Guler. 2010. An experimental comparison of linear and nonlinear price combinatorial auctions. Inform. Systems Res. 22(2) 346–368.

Shapley, L. S., M. Shubik. 1972. The assignment game I: The core. Internat. J. Game Theory 1(1) 111–130.

Sheffi, Y. 2004. Combinatorial auctions in the procurement of transportation services. Interfaces 34(4) 245–252.

Thomas, P., D. Teneketzis, J. K. Mackie-Mason. 2002. A marketbased approach to optimal resource allocation in integratedservices connection-oriented networks. Oper. Res. 50(4) 603–616.

Xia, M., J. Stallaert, A. B. Whinston. 2005. Solving the combinatorial double auction problem. Eur. J. Oper. Res. 164(1) 239–251.

## CORRECTION

In this article, “A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation” by Zhiling Guo, Gary J. Koehler, and Andrew B. Whinston (first published in Articles in Advance, June 23, 2011, Information Systems Research, DOI:10.1287/isre.1100.0366), the email addresses of Zhiling Guo and Gary J. Koehler were updated, respectively, to zhiling.guo@cityu.edu.hk and koehler@ufl.edu.
