---
otero_id: 11338
otero_key: "VQGQTF34"
title: "Pure-Strategy Nash Equilibria of GSP Keyword Auction"
authors: "Linjing Li; Daniel Zeng; Huimin Zhao"
year: "2012"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00286"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 13 Issue 2

Article 2

2-27-2012

# Pure-Strategy Nash E quilibria of GSP K   eyword Auction

Linjing Li , linjing.li@ia.ac.cn

Daniel Zeng , dajun.zeng@ia.ac.cn

Huimin Zhao , hzhao@uwm.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Research Article

# Pure-Strategy Nash Equilibria of GSP Keyword Auction

Linjing Li State Key Laboratory of Management and Control for Complex Systems, China linjing.li@ia.ac.cn

Daniel Zeng State Key Laboratory of Management and Control for Complex Systems, China dajun.zeng@ia.ac.cn

Huimin Zhao University of Wisconsin-Milwaukee hzhao@uwm.edu

## Abstract

Despite the tremendous commercial success of generalized second-price (GSP) keyword auctions, it still remains a big challenge for an advertiser to formulate an effective bidding strategy. In this paper, we strive to bridge this gap by proposing a framework for studying pure-strategy Nash equilibria in GSP auctions. We first analyze the equilibrium bidding behaviors by investigating the properties and distribution of all pure-strategy Nash equilibria. Our analysis shows that the set of all pure-strategy Nash equilibria of a GSP auction can be partitioned into separate convex polyhedra based on the order of bids if the valuations of all advertisers are distinct. We further show that only the polyhedron that allocates slots efficiently is weakly stable, thus allowing all inefficient equilibria to be weeded out. We then propose a novel refinement method for identifying a set of equilibria named the stable Nash equilibrium set (STNE) and prove that STNE is either the same as or a proper subset of the set of the well-known symmetrical Nash equilibria. These findings free both auctioneers and advertisers from complicated strategic thinking. The revenue of a GSP auction on STNE is at least the same as that of the classical Vickrey-Clarke-Groves mechanism and can be used as a benchmark for evaluating other mechanisms. At the same time, STNE provides advertisers a simple yet effective and stable bidding strategy.

Keywords: Keyword Advertising, Stability, Generalized Second-Price, Sponsored Search, Nash Equilibrium.

# Pure-Strategy Nash Equilibria of GSP Keyword Auction

## 1. Introduction

Keyword advertising (also known as sponsored search advertising (SSA) or paid search) is currently the most prevailing online advertising instrument search engines provide. Advertisers submit advertisements (sponsored links) to a search engine and buy some keywords related to their advertisements. If one of these keywords matches a query of a search engine user, the search engine will show the corresponding advertisements along with the standard search result (also referred to as organic result or algorithmic result), usually in the right region of the search result page. If the user clicks on a link, the advertiser should pay a certain fee to the search engine for bringing this potential customer. This payment mode is called pay-per-click, while some traditional Internet advertisements, such as banner ads, are sold by pay-per-impression.

Keyword advertising is more targeted than traditional advertising forms such as television, radio, and newspaper because the click of a sponsored link exposes potential interest of the search engine user in the advertised products or services. Keyword advertising is now the fastest-growing sector in the Internet advertising market. In the US, keyword advertising constitutes the largest share of the entire Internet advertising market. The total revenue of the whole Internet advertising market in 2008 was \$23.4 billion, 45 percent of which came from keyword advertising; this percentage increased to 47 percent in 2009, according to IAB (2010). Keyword advertising also constituted the largest revenue share (56.9 percent) in China’s Internet advertising market in 2009, with a 38 percent increase over 2008, and reached RMB 7.01 billion in total (about \$1 billion), according to DCCI (2010). Meanwhile, keyword advertising is also currently the most important and fastest-growing revenue source for search engines. According to a Google financial report, keyword advertising took up about 97 percent of its total revenue in both 2008 and 2009 (Google, 2010a). In 2009, Baidu, the largest Chinese search engine, reported a total revenue of \$651.6 million, \$651.2 million of which came from keyword advertising (Baidu, 2010).

Keywords are sold through automatically conducted auctions. Two major keyword auction mechanisms have been used in the industry. Generalized first-price (GFP) is the original mechanism introduced by Goto.com in 1994 (renamed Overture in 1997 and then sold to Yahoo! in 2003). In a GFP auction, a bidder must pay the amount it has bid if its links are clicked. As the GFP mechanism is intrinsically unstable, bidders need to adjust their bids constantly (Edelman & Ostrovsky, 2007; Zhang & Feng, 2005). Now, generalized second-price (GSP) has become the dominant auction mechanism used by search engines, as well as some other types of IT companies. In a GSP auction, a bidder pays the bid of the bidder allocated just below it, rather than its own bid. However, almost all practical systems use a slightly modified GSP auction model. For example, Google uses the product of bid and quality score (Google, 2010b), while Yahoo! uses the product of bid and quality index (Yahoo!, 2010), to determine the allocation and payment. For more information about the history of SSA and GSP, please refer to Ghose and Yang (2009), Jansen and Mullen (2008), and Muthukrishnan (2008).

Despite the tremendous commercial success of the GSP auction, formulating an effective bidding strategy still poses serious challenges from the point of view of advertisers. In a static environment, an effective bidding strategy must form an equilibrium because, otherwise, bidders may have incentive to revise their bids. In a dynamic environment, while bidders can adjust their bids frequently to gain more profit, the space of dynamic strategies is too complex to assess the optimality or effectiveness of strategies in it. As a result, a typically used effective strategy-generating approach is to build dynamic strategy using static pure-strategy, such as the forward-looking strategy (myopic strategy or greedy strategy) studied in Bu, Deng, and Qi (2007, 2008), Cary et al. (2007), and Vorobeychik and Reeves (2008). At the same time, auctioneers find it difficult to evaluate the performance of the GSP mechanism because the revenue generated from the auction is evaluated at the equilibrium state in auction theory. In particular, if an auction mechanism has a dominant strategy equilibrium, the revenue at this dominant equilibrium can be used for revenue comparison with other mechanisms.

In a GSP auction, these challenges largely stem from the existence of an infinite number of purestrategy equilibria. Although several auctioneers and third-party companies (e.g., Keyword Country and adSage) provide various services and software tools to help advertisers make bidding decisions, most of these services or tools heavily rely on ad-hoc heuristics and human intelligence without a proper theoretical or computational foundation (Kitts & LeBlanc, 2004). In this paper, we address these challenges by analyzing all the pure-strategy Nash equilibria (PSNE) of a GSP auction with complete information and by proposing two dynamic refinements to weed out useless equilibria. We first characterize and identify all pure-strategy Nash equilibria of a GSP auction and analyze their distribution in the pure-strategy space. Our analysis shows that the set of all these equilibria can be partitioned into several distinct classes, each of which forms a convex polyhedron. Furthermore, these polyhedra are separately distributed in the pure-strategy space, if the valuations of all bidders are distinct.

Next, we propose a refinement concept, named “weak stability”, to weed out the inefficient equilibria. We find that only the polyhedron that allocates slots efficiently is weakly stable in repeated GSP auctions. We also propose a measure for quantifying the degree of instability of each equilibrium polyhedron.

Finally, we propose another powerful refinement concept, named “stability”, on the weakly stable polyhedron to further exclude remaining efficient but risk-dominated equilibria. We provide a method for finding the stable Nash equilibrium set (STNE) of a given GSP auction and relate STNE to the wellknown locally envy-free (LEF) and symmetric Nash equilibrium (SNE) (Edelman, Ostrovsky, & Schwarz, 2007; Varian, 2007, 2009). We show that STNE is either the same as or a proper subset of SNE/LEF. The revenue of a GSP auction on STNE is at least the same as that of the classical Vickrey-Clarke-Groves (VCG) mechanism (Clarke, 1971; Groves, 1973; Vickrey, 1961) and can be used as a benchmark for evaluating other mechanisms. At the same time, STNE provides advertisers with a simple yet effective and stable strategy.

The remainder of this paper is organized as follows. We first provide a review of related work in Section 2. We then lay out a formal specification of the GSP auction mechanism in Section 3. In the next three sections, we present our proposed analysis methodologies and discoveries: In Section 4, we show how to find and partition the set of all Nash equilibria; in Section 5, we describe how to weed out inefficient Nash equilibria; and in Section 6, we present our method for finding STNE. In Section 7, we discuss some implications of STNE for both auctioneers and bidders and the relationships between our proposed equilibrium refinements and major existing refinements. Finally, in Section 8, we summarize our major contributions and discuss some future research directions. Major proofs of theorems and propositions are available in the Appendix A.

## 2. Related Work

In general, there are two main lines of research on GSP auction. One focuses on designing bidding strategies for bidders. The other concentrates on designing optimal auction mechanisms (in terms of various criteria) for auctioneers. As our work is along the former line, we provide a review of related work below. Readers interested in the latter line are referred to the following papers. Iyengar (2006) discusses the conditions that an optimal keyword auction needs to satisfy. Garg, Narahari, and Reddy (2007) proposes the optimal auction mechanism for keyword selling. Feng, Shen, and Zhan (2007) and Feng (2008) format advertisement slots as ranked items and design mechanisms for auctioning them. Liu, Chen, and Whinston (2010) study the weighting mechanism. Athey and Nekipelov (2010) propose a structure model for SSA. Chen, Liu, and Whinston (2009) discuss the optimal share structure problem to maximize the revenue of search engines. See also Aggarwal, Goel, and Motwani (2006), Aggarwal and Hartline (2006), Animesh, Ramachandran, and Viswanathan (2010), and Goel and Munagala (2009) for other related studies along this line.

Through analyzing practical ranking data, Edelman and Ostrovsky (2007) find that strategic bidding behaviors exist in GSP auction. However, Edelman et al. (2007) proves that GSP auction has no dominant strategy and that “truth-telling” is not always a Nash equilibrium. Thus, advertisers do not have simple yet effective strategies (e.g., truth-telling or dominant strategy).

In the pure-strategy space, Milgrom (2010) proves that GSP auction is a tight simplification (with limited message space) of some second-price auctions. In order to reduce the complexity of analysis, LEF (Edelman et al., 2007) and SNE (Varian, 2007, 2009) have been proposed as refinements of Nash equilibrium. LEF and SNE are equivalent, easy to compute, and can explain certain bidding behaviors observed in Google’s AdWords system (Varian, 2007). Further, Börgers, Cox, Pesendorfer, and Petricek (2007) provide the existence conditions for SNE in a non-separated model and showed through a numerical example that inefficient Nash equilibrium exists in GSP auction. Thompson and Leyton-Brown (2008, 2009) consider the equilibrium-finding problem from the point of view of computing. They discretize the bids and view GSP auction as an action-graph game (AGG). With the help of this AGG, one can compare GSP auction with other auction mechanisms such as GFP (Jansen & Mullen, 2008) and VCG (Clarke, 1971; Groves, 1973; Leonard, 1983; Shapley & Shubik, 1972; Vickrey, 1961).

These studies address the existence of Nash equilibrium in GSP auction and provide some elementary refinements on the set of Nash equilibria. However, they have not yet found the entire set of Nash equilibria.

Animesh et al. (2010) study differentiation strategies in this competitive market. Bu et al. (2007, 2008), Cary et al. (2007), and Vorobeychik and Reeves (2008) study myopic strategy in repeated GSP auction, in which they assume a perfect information structure (i.e., the bidding vector is announced after each stage auction such that the optimal bid of an advertiser for the next round of auction can be calculated by fixing other advertisers’ bids). In parallel to these analyses of pure-strategy Nash equilibria (PSNE), some researchers analyze the Bayes Nash equilibrium (BNE) of GSP auction. Leme and Tardos (2010) studiy the price of anarchy for GSP auction under both PSNE and BNE. Lahaie (2006) and Varian (2007) provide some elementary treatments and note that it is difficult to obtain an analytical solution. Gomes and Sweeney (2009) provide an integral equation, which efficient symmetric BNEs need to satisfy. However, obtaining a close-form solution to this equation is difficult even in the simplest case (i.e., GSP auction with only two slots and two bidders).

## 3. Model Specification

In this section, we provide a formal specification of GSP auction. We formulate GSP auction as a static game with complete information. We then illustrate how to unify GSP auctions with and without quality score into a single mathematical model.

## 3.1. GSP Mechanism

There are bidders competing for a keyword. Let $\mathcal { N } = \left\{ 1 , 2 , \cdots , N \right\}$ denote the bidder set. The auctioneer provides advertising slots. Let $\mathcal { K } = \{ 1 , 2 , \cdots , K \}$ denote the slot set. We consider the problem of allocating the slots to the bidders. In practice, this problem is addressed by automatically conducted auctions, such as the keyword advertising systems of Google, Yahoo!, MS-Bing, and Baidu.

Let $b _ { i }$ denote the bid that bidder has submitted and $\pmb { b } = \ ( b _ { 1 } , b _ { 2 } , \cdots , b _ { N } )$ denote the bidding vector of the <sub>??</sub> bidders. All possible bidding vectors form a set <sub>ℬ</sub>, referred to as the pure-strategy space. Without any constraint, <sub>ℬ</sub> is identical to <sub>ℝ</sub><sup>??</sup>. However, in the real world, each bidder may have an upper bound on its bid.

The allocation of slots is based on the bidding vector . The most widely used auction mechanism is GSP, which is a multi-item extension of Vickrey’s second-price auction (Vickrey, 1961). Following conventions in the mechanism literature, we use $\mathcal { M } = ( \pi , p )$ to denote the GSP mechanism, where is the allocation rule and $p : \mathcal { K }  \mathbb { R } .$ is the payment rule. In GSP, a bidder who submits a larger bid is allocated to a higher slot; formally, <sub>∀??,</sub> $\beta \in { \mathcal { K } } , \alpha < \beta \to b _ { \pi _ { \alpha } } \geq b _ { \pi _ { \beta } }$ , where $\pi _ { \alpha }$ is a shorthand for . The price of slot is just the bid of the bidder allocated to slot , thus $p _ { \alpha } = b _ { \pi _ { \alpha + 1 } }$ , where $p _ { \alpha }$ is a shorthand for .

For the sake of convenience in subsequent discussions, let $\psi ( \cdot )$ denote the inverse of $\pi ( \cdot ) ;$ that is, $\psi _ { i }$ , a shorthand for $\psi ( i )$ , is the slot allocated to bidder . Let $\pi ( \mathcal { K } )$ denote the set of bidders who get a slot. All bidders in $\mathcal { N } / \pi ( \mathcal { K } )$ are lost in the auction. $\forall \beta > K , p _ { \beta } = 0$ , since bidders who do not get a slot do not need to pay. $\pi _ { K + 1 }$ is the bidder who loses in the auction with the highest lost bid, $b _ { \pi _ { K + 1 } } .$

## 3.2. Payoff Function

There are two types of valuation models of advertisers in the literature: slot-independent and slotdependent (Börgers et al., 2007). In this paper, we adopt the widely applied (e.g., Edelman et al., 2007; Lahaie, 2006; Varian, 2007, 2009) slot-independent valuation model for the following reasons. First, the potential profit to a specific advertiser is due to the action that a user takes on this advertiser’s webpage after clicking a sponsored link, rather than the click per se. Second, slot-independence leads to a quasilinear payoff function (see Equation 1 later), which makes the partitioning of the entire equilibrium space (discussed in Section 4) possible.

Let $v _ { i }$ denote the average value of a single click on the sponsored link of bidder <sub>??</sub>. Without loss of generality, we let $v _ { 1 } > v _ { 2 } > \cdots > v _ { N }$ (if this does not hold, just re-index the bidders). Let $\pmb { v } = ( v _ { 1 } , v _ { 2 } , \cdots , v _ { N } )$ denote the valuation vector of all bidders. We consider <sub>??</sub> to be common knowledge, as bidders can estimate it from collected historical data (see, e.g., Börgers et al., 2007; Varian, 2007).

Let $c _ { i } ^ { \alpha }$ denote the click-through rate of bidder if its advertisement is allocated to slot , and $C =$ $\{ c _ { i } ^ { \alpha } | i \in \mathcal { N } , \alpha \in \mathcal { K } \}$ denote the set of all click-throughs. There are three kinds of click-through models – separated, non-separated, and cascade – in the literature. The most widely used is the separated model (Edelman et al., 2007; Lahaie, 2006; Varian, 2007), in which click-through is factorized into two independent components; that is, $c _ { i } ^ { \alpha } = \mu _ { i } \nu _ { \alpha }$ , where $\mu _ { i }$ is the click-through of bidder ’s advertisement and $\nu _ { \alpha }$ is the click-through of slot <sub>??</sub>. In the non-separated model, click-through does not have any form of factor decomposition (Börgers et al., 2007). In the cascade model, the click-through of an advertisement also depends on other advertisements (Aggarwal, Feldman, Muthukrishnan, & Pal 2008; Craswell, Zoeter, Taylor, & Ramsey, 2008; Kempe & Mahdian, 2008). In this paper, we adopt the widely used separated click-through model.

Since a higher slot tends to induce more clicks than a lower slot, we assume that $\nu _ { 1 } \geq \nu _ { 2 } \geq \cdots \geq \nu _ { K }$ This assumption can be found in many related studies, such as Edelman et al. (2007), Jansen and Mullen (2008), and Varian (2009). Some studies even enforce further restrictions on the model of clickthrough. For example, Feng, Bhargava, and Pennock (2007) use an exponential decay model, assuming $\begin{array} { r } { \nu _ { \alpha } = \frac { \nu _ { 1 } } { \delta \alpha - 1 } , \forall \alpha \in \mathcal { K } } \end{array}$ , with the constraint $\delta > 1$ , and suggested $\delta = 1 . 4 2 8$ based on actual data from Yahoo!, MSN, and AltaVista.

Let $\frac { c _ { i } ^ { \alpha } } { c _ { i } ^ { \alpha + 1 } } = \frac { \mu _ { i } \nu _ { \alpha } } { \mu _ { i } \nu _ { \alpha + 1 } } = \frac { \nu _ { \alpha } } { \nu _ { \alpha + 1 } } = \gamma _ { \alpha } , \forall \alpha = 1 , 2 , \cdots , K - 1$ , and $i \in \mathcal N$ . The payoff of bidder <sub>??</sub>, given the bidding vector <sub>??</sub>, is:

$$
u _ {i} (\boldsymbol {b}) = c _ {i} ^ {\psi_ {i}} \left(v _ {i} - p _ {\psi_ {i}}\right) = c _ {i} ^ {\psi_ {i}} \left(v _ {i} - b _ {\pi_ {\psi_ {i} + 1}}\right) = \mu_ {i} \nu_ {\psi_ {i}} \left(v _ {i} - b _ {\pi_ {\psi_ {i} + 1}}\right) (1).
$$

Further, let $\pmb { u } = ( u _ { 1 } , u _ { 2 } , \cdots , u _ { N } )$ denote the payoff vector of all bidders.

## 3.3. GSP Auction

With elements defined above, we specify GSP auction as the following tuple:

$$
(\mathcal {N}, \mathcal {K}, \mathcal {B}, \mathcal {M}, \mathcal {C}, \boldsymbol {v}, \boldsymbol {u})\tag{2).}
$$

As typical in existing GSP models (e.g., Edelman et al., 2007 and Varian, 2009), we assume that the reserve price is zero and that bidders are rational, risk neutral, and have no budget constraint.

Note that, in practical auctions, advertisers can specify and modify their daily budgets in this keyword advertising market. The existence of budget constraints may affect the bidding behaviors of advertisers and break the quasi-linear form of the payoff function, causing difficulty in the analysis of bidding strategy. To simplify analysis, we do not consider budget constraints in this paper. Despite this limitation, our analysis sheds light on further extensions accommodating such constraints. Also note that budget is also a major issue in the general auction theory (Krishna, 2002). In the context of keyword auctions, Aggarwal, Muthukrishnan, Pal, and Pal (2009) and Ashlagi, Braverman, Hassidim, Lavi, and Tennenholtz (2010) designed auction mechanisms to address this budget issue, as the design of the GSP mechanism does not take budget into consideration.

While we restrict our analysis to this specified GSP auction, it can be shown that the GSP auction with quality score, typically used in practical systems, can be transformed into this model. In the modified GSP auction with quality score, bidders are ranked according to $w _ { i } b _ { i }$ , where $w _ { i }$ is the quality score of bidder . We use the term “quality $\mathsf { s c o r e } ^ { \boldsymbol { \mathsf { \prime } } \boldsymbol { \mathsf { \prime } } }$ to refer to Google’s quality score (Google, 2010b) and Yahoo!’s quality index (Yahoo!, 2010), or any quantity of the same nature used by other search engines. Note that the quantity $w _ { i } b _ { i }$ is called bidder ’s revenue by Lahaie (2006) and Liu, Chen, and Whinston (2009), whereas the quality score they used is the click-through of bidder ’s advertisement. Although, search engines may consider additional factors, such as account performance and the quality of the landing page, when calculating the quality score (see, for example, Google, 2010b and Yahoo!, 2010). The modified allocation rule is $\textstyle { \bar { \pi } } : { \mathcal { K } } \to { \mathcal { N } }$ , such that $\forall \alpha , \beta \in { \mathcal { K } } , \alpha < \beta \to w _ { { \bar { \pi } } _ { \alpha } } b _ { { \bar { \pi } } _ { \alpha } } \geq w _ { { \bar { \pi } } _ { \alpha } } b _ { { \bar { \pi } } _ { \beta } }$ . The modified payment rule is $\bar { p } _ { \alpha } = \frac { w _ { \bar { \pi } _ { \alpha + 1 } } } { w _ { \bar { \pi } _ { \alpha } } } b _ { \bar { \pi } _ { \alpha + 1 } }$ . The modified GSP mechanism is $\bar { \mathcal { M } } = ( \bar { \pi } , \bar { p } )$ The assumption $v _ { 1 } \geq v _ { 2 } \geq \cdots \geq v _ { K }$ , which means that a higher slot tends to induce more clicks than a lower slot, is still valid.

The changes of allocation and payment will affect the payoffs of bidders. In the modified GSP auction, the payoff of bidder <sub>??</sub>, given the bidding vector <sub>??</sub>, is:

$$
\begin{array}{r l} & {\bar {u} _ {i} (\pmb {b}) = c _ {i} ^ {\alpha} (v _ {i} - p _ {\alpha})} \\ & {\qquad = c _ {i} ^ {\alpha} \left(v _ {i} - \frac {w _ {\overline {{\pi}} _ {\alpha + 1}}}{w _ {\overline {{\pi}} _ {\alpha}}} b _ {\overline {{\pi}} _ {\alpha + 1}}\right) = \frac {c _ {i} ^ {\alpha}}{w _ {\overline {{\pi}} _ {\alpha}}} \big (w _ {\overline {{\pi}} _ {\alpha}} v _ {i} - w _ {\overline {{\pi}} _ {\alpha + 1}} b _ {\overline {{\pi}} _ {\alpha + 1}} \big)} \\ & {\qquad = \frac {c _ {i} ^ {\alpha}}{w _ {i}} \big (w _ {i} v _ {i} - w _ {\overline {{\pi}} _ {\alpha + 1}} b _ {\overline {{\pi}} _ {\alpha + 1}} \big) (3),} \end{array}
$$

where $\alpha = \hat { \psi } _ { i } \left( \hat { \psi } \right.$ is the inverse of ) is the slot allocated to bidder . Let $\begin{array} { r } { \bar { c } _ { i } ^ { \alpha } = \frac { c _ { i } ^ { \alpha } } { w _ { i } } } \end{array}$ denote the modified click-through, $\bar { C } = \{ \bar { c } _ { i } ^ { \alpha } | i \in \mathcal { N } , \alpha \in \mathcal { K } \}$ denote the modified set of all click-throughs, $\bar { v } _ { i } = w _ { i } v _ { i }$ denote the modified value, $\overline { { \pmb { v } } } = ( \bar { v } _ { 1 } , \bar { v } _ { 2 } , \cdots , \bar { v } _ { N } )$ denote the modified valuation vector of all bidders, ${ \bar { b } } _ { i } = w _ { i } b _ { i }$ denote the modified bid, $\overline { { \pmb { b } } } = \left( \overline { { b } } _ { 1 } , \overline { { b } } _ { 2 } , \cdots , \overline { { b } } _ { N } \right)$ denote the modified bidding vector of all bidders, and � denote the modified bidding space. The payoff (3) can then be written as:

$$
\bar {u} _ {i} (\pmb {b}) = \bar {c} _ {i} ^ {\overline {{\psi}} _ {i}} \left(\bar {v} _ {i} - \bar {b} _ {\overline {{\pi}} _ {\overline {{\psi}} _ {i + 1}}}\right) (4).
$$

As this has the same form as Equation 1, the original GSP auction with quality score can be reformulated as the following new GSP auction without quality score.

$$
(\mathcal {N}, \mathcal {K}, \overline {{\mathcal {B}}}, \overline {{\mathcal {M}}}, \bar {\mathcal {C}}, \overline {{\boldsymbol {v}}}, \overline {{\boldsymbol {u}}}).
$$

With this reformulation, it is easy to extend our subsequent results obtained in GSP auction without quality score to GSP auction with quality score. However, this does not mean that these two kinds of auctions are equivalent in all aspects. Generally, search engines use “quality score” to increase their total revenues and improve user experiences (Balachander, Kannan, & Schwartz, 2009; Feng, Bhargava, et al., 2007; Lahaie, 2006; Liu et al., 2009).

## 4. Existence and Partitioning of Nash Equilibria

In this section, we first show the existence of Nash equilibria in the GSP auction. We then provide a method for finding and partitioning all Nash equilibria.

## 4.1. Existence of Nash Equilibrium

A bidding vector ${ \pmb { b } } ^ { \star }$ is a Nash equilibrium of the GSP auction (Model 2) if it satisfies the following conditions (Fudenberg & Tirole, 1991; Nash, 1950; Osborne & Rubinstein, 1994):

$$
\boldsymbol {b} _ {i} ^ {\star} \in \arg_ {b _ {i}} \max u _ {i} (\boldsymbol {b}), \forall i \in \mathcal {N} (5).
$$

At a Nash equilibrium, no bidder in $\pi ( \mathcal { K } )$ has incentive to raise or lower its slot, while no bidder in $\mathcal { N } \backslash \pi ( \mathcal { K } )$ has incentive to raise its bid to get a slot. These intuitions can be formulated as several inequalities.

First, the payoff of every bidder in $\pi ( \mathcal { K } )$ must be nonnegative, as otherwise it would be better off if it deviates to $\mathcal { N } \backslash \pi ( \mathcal { K } )$ ; that is:

$$
v _ {i} - b _ {\pi_ {\psi_ {i} + 1}} \geq 0, \forall i \in \pi (\mathcal {K}) (6).
$$

Second, every bidder in <sub>??(??)</sub> has no incentive to get a higher slot; that is:

$$
c _ {i} ^ {\psi_ {i}} \left(v _ {i} - b _ {\pi_ {\psi_ {i} + 1}}\right) \geq c _ {i} ^ {\alpha} \left(v _ {i} - b _ {\pi_ {\alpha}}\right), \forall i \in \pi (\mathcal {K}), 1 \leq \alpha \leq \psi_ {i} (7).
$$

Third, every bidder in $\pi ( \mathcal { K } )$ has no incentive to lower its slot; that is:

$$
c _ {i} ^ {\psi_ {i}} \left(v _ {i} - b _ {\pi_ {\psi_ {i + 1}}}\right) \geq c _ {i} ^ {\beta} \left(v _ {i} - b _ {\pi_ {\beta + 1}}\right), \forall i \in \pi (\mathcal {K}), \psi_ {i} <   \beta \leq K (8).
$$

Finally, for every bidder in $\mathcal { N } \backslash \pi ( \mathcal { K } )$ , payoff would be negative or still zero if it deviates to get a slot; that is:

$$
v _ {j} - b _ {\pi_ {\alpha}} \leq 0, \quad \forall i \in \mathcal {N} \backslash \pi (\mathcal {K}), \alpha \in \mathcal {K} (9).
$$

Inequality 9 is not needed if $N \leq K .$

In terms of mechanism design, Inequalities 6 and 9 are individual rational conditions. With these inequalities, the existence of Nash equilibrium of Model 2 is equivalent to the existence of a solution to the above inequalities. The following lemma guarantees the existence of at least one Nash equilibrium of Model 2.

Lemma 4.1. GSP auction (2) has at least one pure-strategy Nash equilibrium.

The proof of this lemma is straightforward. Model 2 satisfies the first assumption of Börgers et al. (2007), which guarantees the existence of at least one symmetric Nash equilibrium, while any symmetric Nash equilibrium is also a Nash equilibrium (Börgers et al., 2007; Varian, 2007, 2009).

In fact, the existence of at least one Nash equilibrium guaranteed by Lemma 4.1 is a weak statement, since the analyses of SNE by Varian (2007) and LEF by Edelman et al. (2007) shows that there exist an infinite number of Nash equilibria in GSP auction (see also Lahaie, 2006).

## 4.2. Partitioning of Equilibria

Model 2 defines a static game with complete information. In this section, we shall find all PSNE by partitioning the set of all pure-strategy Nash equilibria, denoted <sub>ℰ</sub>, into a finite number of equivalence classes.

All Inequalities 6–9 that a Nash equilibrium needs to satisfy are in the linear form. However, the problem of finding all Nash equilibria cannot be solved by employing solvers of linear inequalities, such as those described by Solodovnikov (1980), because the implicit allocation rule <sub>??</sub> is nonlinear. The same reason prevents the use of linear programming to find some special equilibria (e.g., the optimal bids).

In practical systems, the GSP allocation rule is typically realized through the following two steps:

1) Sort the bidders according to their bids in descending order.

2) Allocate the first slot to the first bidder, the second slot to the second bidder, and so on.

When there are ties among the bids, a tie-breaking mechanism is needed. Fortunately, tie breaking does not need to be considered in equilibrium bidding analysis if the valuations of all bidders are distinct, as stated in the following theorem.

Theorem 4.1. Suppose $v _ { 1 } > v _ { 2 } > \cdots > v _ { N } , \forall b \in \mathcal { B }$ . A necessary condition for b to be a Nash equilibrium in GSP auction (2) is:

$$
\bullet \text {   if   } N \leq K, b _ {\pi_ {1}} > b _ {\pi_ {2}} > \dots > b _ {\pi_ {N}};
$$

$$
\bullet i f N > K, b _ {\pi_ {1}} > b _ {\pi_ {2}} > \dots > b _ {\pi_ {K}} > b _ {\pi_ {K + 1}}.
$$

Theorem 4.1 indicates that a bidding vector with a tie in GSP auction is not a Nash equilibrium. With ties safely ignored, we can find all Nash equilibria in two steps. First, we define an equivalence relation on <sub>ℰ</sub> and partition into a finite number of equivalence classes according to this relation. Second, if each equivalence class happens to determine a unique allocation, we can substitute this allocation into Inequalities 6–9 and transform them into linear inequalities on bids (given that the allocation rule <sub>??</sub> is fixed). The inequality methods described by Solodovnikov (1980) can then be employed to compute all solutions. Note that linear programming techniques can be used to quickly determine whether feasible solutions exist. We now define one such equivalence relation, which provides a simple yet surprisingly powerful framework for both theoretical analysis and computation with respect to $G S P$ auction.

Definition 4.1. is a relation (also referred to as the “same-slot” relation) on such that <sup>1</sup><sub>,</sub> $\pmb { b } ^ { 2 } \in$ $\mathcal { E } , \pmb { b } ^ { 1 } \cong \pmb { b } ^ { 2 }  \forall i \in \mathcal { K } , \pi ^ { 1 } ( i ) = \pi ^ { 2 } \overset { . } { ( } i )$ , where $\pi ^ { 1 }$ and $\pi ^ { 2 }$ denote the allocations corresponding to ${ \pmb b } ^ { 1 }$ and $\pmb { b } ^ { 2 } .$ , respectively.

Figure 1 illustrates this relation and ties in a two-bidder case. Intuitively, this “same-slot” relation groups bidding vectors together as long as they deliver the same allocation. It is easy to show that this relation is an equivalence relation, as stated in the following proposition (proof is trivial and hence omitted).

Proposition 4.1. <sub>≅</sub> is an equivalence relation on <sub>ℰ</sub>.

Because an equivalence relation on a set can determine a unique partitioning of the set, we can partition into distinct equivalence classes based on . For $\pmb { b } \in \mathcal { E }$ , the equivalence class generated by is:

$$
\mathcal {E} _ {\boldsymbol {b}} = \left\{\widetilde {\boldsymbol {b}} \mid \widetilde {\boldsymbol {b}} \cong \boldsymbol {b}, \widetilde {\boldsymbol {b}} \in \mathcal {E} \right\} \tag {10}
$$

All equivalence classes of form the factor (quotient) set:

$$
\mathcal {E} / \cong = \{\mathcal {E} _ {\boldsymbol {b}} | \boldsymbol {b} \in \mathcal {E} \} = \{\mathcal {E} _ {0}, \mathcal {E} _ {1}, \dots , \mathcal {E} _ {M - 1} \} (1 1),
$$

where <sub>??</sub> is the number of equivalence classes. $\mathcal { E } _ { 0 }$ is a special and the most important equivalence class, in which the allocation is the identity mapping, i.e., $\overset { \cdot } { \pi } { } ^ { 0 } ( i ) = i , \forall i \in \mathcal { K }$ . It is obvious that only the Nash equilibria in $\mathcal { E } _ { 0 }$ are efficient and all others are inefficient.

![](/api/attachments/VQGQTF34/fulltext/images/6f198c6d146b4df0ca0aff9df29774a368d00941c4fd1b77bb49922661f62daf.jpg)  
Figure 1. An Illustration of the “Same-Slot” Relation

Note that we define the efficiency of an equilibrium in the sense that a bidder with a higher valuation is allocated to a higher slot. This is slightly different from the efficiency used in other papers, which maximizes the social welfare. However, in a GSP auction with quality score (Section 3.3), our definition is equivalent to the social welfare maximization definition, if click-through is employed as the quality score. In such a situation, the modified valuation of a bidder, say <sub>??</sub>, is $v _ { i } ^ { \prime } = \mu _ { i } v _ { i }$ , and equivalence class ${ \mathcal { E } } _ { 0 }$ includes all equilibria that allocate bidders according to the modified valuations (i.e., all equilibria that maximize the social welfare).

Consider an equivalence class $\mathcal { E } _ { m } .$ If a bidder, say , revises its bid (provided there is no change from other bidders) but the revised bidding vector is still in the same equivalence class ${ \mathcal { E } } _ { m }$ , this bid revision has no impact on the allocation and its payoff. As such, all equilibria in the same equivalence class are indifferent from this bidder’s point of view (unless other factors, such as risk, are considered). However, bidder ’s action affects (and can only affect) the payoff of the bidder allocated just above, say . A reduction (increase) of ’s bid will increase (reduce) ’s payoff.

As any equivalence class is defined by a series of linear inequalities, in terms of geometry, an equivalence class forms a convex polyhedron in $\mathcal { B } = \mathbb { R } _ { + } ^ { N }$ . As a non-empty convex polyhedron may be a point, line segment, rectangle, and so on, in a GSP auction, an infinite number of inefficient Nash equilibria may exist. Further, these polyhedra are distributed in the pure strategy space separately, since no two equivalence classes intersect each other. We provide an upper bound on the number of possible equivalence classes in the following theorem.

Theorem 4.2. In GSP auction, the number of equivalence classes is at most:

$$
\bullet N!, i f N \leq K;
$$

$$
\bullet N (K - 1)!, i f N > K.
$$

In general, this is not a tight upper bound, since only the numbers of bidders and slots are taken into consideration. For a specific GSP auction, the number of equivalence classes is dependent on the concrete values of bidder valuations and click-throughs and may be less than this upper bound. Furthermore, as we will show later, only $\mathcal { E } _ { 0 }$ is weakly stable in a dynamic environment. One (advertiser or search engine) can, therefore, just focus on the equilibria in this polyhedron, which can be efficiently obtained.

## 4.3. Example

We use a simple example with two bidders and two slots to illustrate our method for finding and partitioning PSNE. In this situation, there are at most two distinct allocations: $\pi ^ { 0 }$ and $\pi ^ { 1 }$ , where $\pi ^ { 0 }$ is the identity $( \mathrm { i . e . , ~ } \pi ^ { 0 } ( 1 ) = 1 , \pi ^ { 0 } ( 2 ) = 2 ~ )$ and $\pi ^ { 1 } ( 1 ) = 2 , \pi ^ { 1 } ( 2 ) = 1$ . The polyhedron corresponding to allocation $\pi ^ { 0 }$ is determined by the following three inequalities:

$$
\left\{ \begin{array}{c} b _ {1} > b _ {2} \\ b _ {1} \geq \left(1 - \frac {1}{\gamma_ {1}}\right) v _ {2} = k v _ {2} \\ b _ {2} \leq \left(1 - \frac {1}{\gamma_ {1}}\right) v _ {1} = k v _ {1} \end{array} \right.\tag{12),}
$$

where $\begin{array} { r } { k = 1 - \frac { 1 } { \gamma _ { 1 } } . } \end{array}$ . The polyhedron corresponding to $\pi ^ { 1 }$ is governed by:

$$
\left\{ \begin{array}{c} b _ {2} > b _ {1} \\ b _ {1} \leq \left(1 - \frac {1}{\gamma_ {1}}\right) v _ {2} = k v _ {2} \\ b _ {2} \geq \left(1 - \frac {1}{\gamma_ {1}}\right) v _ {1} = k v _ {1} \end{array} \right.\tag{13).}
$$

The distributions of these two polyhedra when $k v _ { 1 } > v _ { 2 }$ and $v _ { 2 } > k v _ { 1 }$ are illustrated in Figures 2a and 2b, respectively.

![](/api/attachments/VQGQTF34/fulltext/images/3c73b62f51d2fb214c503ab21feb011635d1ebfd3fc2ea0484918efbf0b1b24b.jpg)  
(a) $k v _ { 1 } > v _ { 2 }$

![](/api/attachments/VQGQTF34/fulltext/images/83a530f5f4e82bbb677e70961ff6bcd638693c3f982e90acd44a7816dbc1845b.jpg)  
(b) $v _ { 2 } > k v _ { 1 }$

## Figure 2. Equilibrium Polyhedra of GSP Auction with Two Slots and Two Bidders

In both figures, the shadowed regions ${ \mathcal { E } } _ { 0 }$ and ${ \mathcal { E } } _ { 1 }$ are polyhedra that correspond to $\pi ^ { 0 }$ and $\pi ^ { 1 }$ respectively. In $\mathcal { E } _ { 0 } ( \mathcal { E } _ { 1 } )$ , the bid of bidder 1 (bidder $^ { 2 ) }$ can be arbitrarily large, as indicted by the arrows in these two regions. In practice, however, no bidder will bid a very large value. Although doing so may guarantee a high slot, the risk of its opponent placing a very high bid is high as well. In fact, bidding above $k v _ { 1 }$ is weakly dominated for bidder 1. Suppose bidder 1 bids $k v _ { 1 }$ . If bidder 2 bids less than $k v _ { 1 } ,$ bidder 1 would get the first slot and receive a payoff more than $k v _ { 1 }$ . If bidder 2 bids more than $k v _ { 1 }$ , it would get the first slot and bidder 1 would receive a payoff $k v _ { 1 }$ . Now, suppose bidder 1 bids $b _ { 1 } > k v _ { 1 }$ . If bidder $^ 2$ bids $b _ { 2 } \in ( k v _ { 1 } , b _ { 1 } )$ , bidder 1 would still get the first slot, but the payoff is less than $k v _ { 1 }$

In $\mathcal { E } _ { 0 }$ , the payoffs of bidders 1 and 2 are $c _ { 1 } ^ { 1 } ( v _ { 1 } - b _ { 2 } ) \geq c _ { 1 } ^ { 1 } ( v _ { 1 } - k v _ { 1 } ) = c _ { 1 } ^ { 2 } v _ { 1 }$ and $c _ { 2 } ^ { 2 } v _ { 2 }$ , respectively. In $\mathcal { E } _ { 1 } ,$ the payoffs of bidders 1 and 2 are $c _ { 1 } ^ { 2 } v _ { 1 }$ and $c _ { 2 } ^ { 1 } ( v _ { 2 } - b _ { 1 } ) \geq c _ { 2 } ^ { 1 } ( v _ { 2 } - k v _ { 2 } ) = c _ { 2 } ^ { 2 } v _ { 2 }$ , respectively. So, bidder 1 prefers $\mathcal { E } _ { 0 } :$ , but bidder 2 prefers ${ \mathcal { E } } _ { 1 }$ . Therefore, bidder 1 will bid more than $k v _ { 2 }$ and bidder 2 will bid more than <sub>????</sub> . The resulting bidding vector is no longer a Nash equilibrium. After a period of bid revisions, the final bidding vector may be in either $\mathcal { E } _ { 0 }$ or ${ \mathcal { E } } _ { 1 }$ . We will introduce further refinement methods in the next two sections to determine exactly which equivalence class the final bidding vector belongs to.

Finally, we analyze the strategy of truth-telling. In Vickrey’s second-price auction with a single item, truth-telling is a weakly dominant strategy for every bidder (1961). In a GSP auction, truth-telling is not always a Nash equilibrium (an example is available in Edelman et al., 2007). Here, Figure 2 provides more informative results. If $k v _ { 1 } > v _ { 2 } ,$ , truth-telling is a Nash equilibrium (point in Figure 2a). Otherwise, truth-telling is not a Nash equilibrium, and bidder 1 has incentive to lower its bid (Point $D ^ { \prime }$ in Figure 2b).

## 5. Weeding Out Inefficient Equilibrium

In this section, we analyze bidding behaviors in the repeated version of Model 2 using a framework similar to the Cournot adjustments (Fudenberg & Levine, 1998) and prove that only equilibrium polyhedron $\mathcal { E } _ { 0 }$ is weakly stable. We consider an imperfect information structure, that is, after each stage auction, every bidder knows the allocation of this auction and the price it must pay, but not the prices of other slots except the one just above it (thus, the bidder allocated in slot <sub>??</sub> knows $b _ { \alpha }$ and $b _ { a + 1 } )$ . In practice, bids submitted in stage auctions are private information. Only the search engine knows the bids. To avoid potential legal issues, the search engine does not announce the bids after each stage auction.

## 5.1. Weakly Stable Nash Equilibrium Polyhedron

Definition 5.1. A pair of bidders and in a Nash equilibrium allocation is said to be an unstable factor, $i f v _ { i } > v _ { j } \ b u t \psi _ { i } > \psi _ { j }$

An unstable factor refers to a pair of bidders such that the one with higher valuation is actually allocated to a lower slot than its opponent. The existence of an unstable factor indicates the inefficiency of an allocation. Obviously, bidder <sub>??</sub> may get a higher payoff if it is allocated to <sub>??</sub>’s slot, but it must bid more than in order to get that slot. Doing so is profitless in a static GSP auction because their bids have already formed a Nash equilibrium. However, in a repeated GSP auction, as stated in the following theorem, bidder can realize its incentive, if is allocated just above it.

Theorem 5.1. In repeated GSP auction, if two bidders of an unstable factor are allocated to two neighboring slots, the bidder with higher valuation has incentive and is able to force its opponent to a lower slot. Afterward, it is impossible for the other bidder to reverse the order of their slots.

Bidder ’s behavior not only increases its utility in future auctions, but also eliminates an unstable factor in a Nash equilibrium. Bidder may declare that it would maintain a higher bid to guarantee a higher slot, but the above theorem shows that this is just an empty threat (Fudenberg & Tirole, 1991; Osborne & Rubinstein, 1994). In this sense, we say that this Nash equilibrium is unstable in a repeated GSP auction. That is why we call the pair <sub>??</sub> and <sub>??</sub> an “unstable factor”.

If bidders <sub>??</sub> and <sub>??</sub> $( v _ { i } > v _ { j } )$ of an unstable factor are not allocated to two neighboring slots, bidder <sub>??</sub> may not have a strategy to directly force to a lower slot by raising its bid. For example, suppose that another bidder <sub>??</sub>, with $v _ { k } > v _ { i } ,$ , is allocated between <sub>??</sub> and <sub>??</sub>. To force <sub>??</sub> to a lower slot, <sub>??</sub> must bid more than <sub>??</sub>, but doing so is profitless, and Theorem 5.1 shows that <sub>??</sub> may force <sub>??</sub> to a lower slot, leading to complicated bidding dynamics. However, <sub>??</sub> could just wait until <sub>??</sub> has raised its bid and forced <sub>??</sub> to a lower slot before raising its bid and forcing to an even lower slot. With this analysis, we are ready to define the weak stability of an equilibrium polyhedron.

Definition 5.2. An equilibrium polyhedron $\mathcal { E } _ { m } \in \mathcal { E } / \cong , m = 0 , 1 , 2 , \cdots , M - 1$ is said to be weakly stable if no Nash equilibrium in it has any unstable factor. Otherwise, $\mathcal { E } _ { m }$ is said to be unstable.

As only the Nash equilibrium in $\mathcal { E } _ { 0 }$ has no unstable factor, only $\mathcal { E } _ { 0 }$ is weakly stable, as stated in the following theorem, and is referred to as weakly stable Nash equilibrium polyhedron (WSNE).

Theorem 5.2. In repeated GSP auction with $K \geq 2$ and $N \geq 2 , { \mathcal { E } } _ { 0 }$ is the only weakly stable equilibrium polyhedron.

In an auction, all bidders want the top slot, but their abilities to accomplish this objective are different. Theorem 5.2 indicates that a bidder with a higher valuation can obtain a higher slot in the GSP auction. This theorem also reveals that GSP is an efficient auction mechanism in a dynamic environment.

The word “weakly” is used to depict the following situation: If a bidder knows that it is allocated to the right slot it can obtain according to Theorem 5.2, it will have no incentive to revise its bid because it cannot get a better slot. We call such a bidder a “lazy” one. $\forall b \in { \mathcal { E } } _ { 0 } .$ , all bidders are allocated to right slots. If all bidders are lazy, the bidding vector will fix at the current equilibrium point. That is why we use the term “weakly stable”.

The weak stability of $\mathcal { E } _ { 0 }$ can only guarantee the invariability of the outcome of slot allocation. It is still not necessary that the bidding vector will converge to a particular Nash equilibrium. Even in $\mathcal { E } _ { 0 } ,$ there is still some freedom for each bidder to choose a bid. At the same time, the weak stability of allocation does not mean that the payoff of a bidder is invariant across Nash equilibria in $\mathcal { E } _ { 0 }$ because the payoff of a bidder is strictly dependent on the bid of another bidder allocated just below, and this bid can vary across Nash equilibria.

As of the information requirement for the above analysis, only a bidder’s own price and bid (also the price of the bidder ranked just above) are needed to prove that only $\mathcal { E } _ { 0 }$ is weakly stable. Thus, the imperfect information structure assumed at the beginning of this section is sufficient. Note that there are also other analyses on the dynamic bidding strategy in a GSP auction (e.g., Bu et al., 2007, 2008; Cary et al., 2007; Vorobeychik & Reeves, 2008). These analyses assume incomplete but perfect information, whereas our analysis assumes complete but imperfect information. The perfect information assumption requires that the bidding vector be revealed after each stage auction; the complete information assumption requires the value vector to be common knowledge. However, neither assumption actually holds in a real GSP auction. Since revealing price-related information may cause legal issues, search engines do not announce the bids after each stage auction. The value per click is a bidder’s private information and cannot be acquired by others exactly.

## 5.2. Degree of Unstability

A Nash equilibrium in an unstable equilibrium polyhedron contains at least one unstable factor. Further, as the definition of equilibrium polyhedron guarantees that all Nash equilibria in the same polyhedron have the same number of unstable factors, this number can be used as a property to characterize the polyhedron.

Definition 5.3. The degree of unstability (DoU) of an equilibrium polyhedron ${ \mathcal { E } } _ { m }$ , denoted $\mathcal { O } ( \mathcal { E } _ { m } )$ , is defined as the number of unstable factors in each Nash equilibrium in $\mathcal { E } _ { m }$

Naturally, the DoU of ${ \mathcal { E } } _ { 0 }$ is zero, that is, $\mathcal { O } ( \mathcal { E } _ { 0 } ) = 0$ . The order of DoU induces a partial relation (called “more unstable $) \geq \mathsf { o n } \mathscr { E } / \cong$ , such that $\forall \mathcal { E } _ { m } , \mathcal { E } _ { n } , \in \mathcal { E } / \cong , \mathcal { E } _ { m } \succeq \mathcal { E } _ { n }  \mathcal { O } ( \mathcal { E } _ { m } ) \geq \mathcal { O } ( \mathcal { E } _ { n } )$ and after at most one elimination of a neighboring unstable factor, an equilibrium in $\mathcal { E } _ { m }$ jumps into $\mathcal { E } _ { n }$

Figure 3 illustrates the partial relation in three cases with two, three, and four bidders, respectively. In the two-bidder case (Figure 3a), as the DoU of $\mathcal { E } _ { 1 }$ is just one, one swap of slots is necessary and sufficient to eliminate the unstable factor and make the bids converge $\mathrm { t o } ~ \mathcal { E } _ { 0 }$ . In an auction with more bidders (e.g., Figures 3b and 3c), one elimination of the unstable factor may make the original Nash equilibrium converge to another unstable polyhedron with a DoU one less than the original polyhedron, rather than the stable polyhedron $\mathcal { E } _ { 0 } .$ . However, it will always converge to $\mathcal { E } _ { 0 }$ at the end. The Hasse diagram shows some possible paths by which an unstable Nash equilibrium converges to a weakly stable one, but the particular path that is realized is random and varies from one auction to another.

![](/api/attachments/VQGQTF34/fulltext/images/b60153965cb021717749dbbe6ac2bc0e59bcd8dd27c6dbbdb3c2fe22bad77d06.jpg)  
(a) Two bidders

![](/api/attachments/VQGQTF34/fulltext/images/fe19751d05d15bfca4a1811aa2f2820fd15a2ca75ff29a608d72d3c3dc3e7397.jpg)

(b) Three bidders  
![](/api/attachments/VQGQTF34/fulltext/images/a35ff90399a1f58245945f6b191b0b73c85f6ec4c0ac71b1ee1666f7629d5bb7.jpg)  
(c) Four bidders

Figure 3. Examples of Hasse diagraph of <sub>≺</sub>. (Each Vertex Denotes a Permutation Corresponding to an Equilibrium Polyhedron; For Example, 21 Represents the Polyhedron that Allocates Bidder 2 to Slot 1 and Bidder 1 to Slot 2. As a Convention, We Let DoU Increase Bottom-Up.)

## 5.3. Discussion: Is WSNE a Good Refinement?

In practice, not all bidders are lazy, as some of them may have incentive to obtain a higher slot. Even if a bidder is allocated to its right slot, when raising a bid and getting a higher slot is profitable, it might do so. Next, we use a simple example to illustrate why this is possible.

Figure 4 shows the bidding dynamics in a repeated GSP auction with two bidders and two slots. The bidding dynamics in non-Nash regions $( A - E )$ are as follows.

• <sub>??</sub> and <sub>??</sub>: Bidder 2 is allocated to slot 1 $( b _ { 2 } > b _ { 1 } )$ . Bidder 2 knows that bidder 1’s bid (i.e., bidder 2’s price) is larger than $k v _ { 2 }$ and has incentive to lower its bid, because its payoff is less than $c _ { 2 } ^ { 2 } v _ { 2 }$ in slot 1 and deviating to slot 2 would bring a larger payoff $c _ { 2 } ^ { 2 } v _ { 2 }$ . In region <sub>??</sub> and subregion $A _ { 1 }$ , bidder 1 has incentive to raise its bid up to $k v _ { 1 }$ , because it does not know bidder 2’s bid. If bidder 2’s bid is larger than $k v _ { 1 }$ , deviating to slot 1 is profitless for bidder 1, because its payoff in slot 1 would be less than its current payoff $c _ { 1 } ^ { 2 } v _ { 1 }$ . In subregion $A _ { 2 } ,$ bidder 1 has incentive to make a lower bid.

• : Bidder 1 is allocated to slot 1 $( b _ { 1 } > b _ { 2 } )$ . Bidder 1 has incentive to lower its bid. Bidder 2’s bid (i.e., bidder 1’s price) is larger than . Bidder 1’s current payoff is less than $c _ { 1 } ^ { 2 } v _ { 1 }$ Deviating to slot 2 would bring bidder 1 a higher payoff of $c _ { 1 } ^ { 2 } v _ { 1 }$ . Bidder 2 has no incentive to raise its bid, because it knows that bidder $\boldsymbol { 1 } \boldsymbol { \mathsf { s } }$ bid is larger than its own bid $b _ { 2 } > k v _ { 2 }$ . For bidder $^ { 2 , }$ deviating to slot 1 is profitless, because its payoff in slot 1 would be less than its current payoff $c _ { 2 } ^ { 2 } v _ { 2 }$ . However, bidder 2 has incentive to lower its bid, because it knows that bidder 1 would lower its bid to deviate to slot 2. It is profitless for bidder 2 to retain its current bid if bidder 1’s new bid is larger than $k v _ { 2 }$

• : Bidder 2 is allocated to slot $1 \ ( b _ { 2 } > b _ { 1 } )$ . Bidder 1 has incentive to raise its bid, but the optimal adjustment is unknown because it does not know bidder 2’s bid. Bidder 2 has incentive to raise its bid up to $k v _ { 1 }$ , because it knows that bidder 1 will raise its bid, and would raise the bid too to keep slot 1.

$D \colon$ Bidder 1 is allocated to slot $1 \ ( b _ { 1 } > b _ { 2 } )$ . Bidder 2 has incentive – without any risk – to raise its bid up to $k v _ { 2 }$ . It is profitable for bidder 2 if it gets the first slot with a price less than $k v _ { 2 }$ . Bidder 1 has incentive to raise its bid in order to keep slot 1 because it knows that bidder 2 will raise its bid.

![](/api/attachments/VQGQTF34/fulltext/images/57949bf0600bd88cb6e2446618dcfe790c1dc783e6b36a81f0084ca9913830fb.jpg)  
(a) $k v _ { 1 } > v _ { 2 }$

![](/api/attachments/VQGQTF34/fulltext/images/01a32ef2c89744025872b5679470153640f13b3ff30753984e04bce4a371eddc.jpg)  
(b) $v _ { 2 } > k v _ { 1 }$  
Figure 4. Bid Adjustments in a Repeated GSP Auction with Two Slots and Two Bidders. (<sub>??</sub> is Partitioned into Four Subsets, <sub>??</sub><sup>⋆</sup> , <sub>??</sub><sup>??</sup> , <sub>??</sub><sup>??</sup> , and <sub>??</sub><sup>??</sup>. Arrows Indicate Bid Revisions. Horizontal (Vertical) Arrows Represent Bidder 1’s (Bidder 2’s) Movements.)

In Nash equilibrium regions, unilateral bid revisions by either bidder do not increase payoff for that bidder directly, but may increase payoff in future auctions. The bidding dynamics in Nash equilibrium regions are as follows.

$\mathcal { E } _ { 1 } \mathrm { : }$ Bidder 1 has incentive to raise its bid (see Theorem 5.1).

• $\mathcal { E } _ { 0 } ^ { 1 }$ : Bidder 2 has incentive to raise its bid up to $k v _ { 2 }$ (same reasoning as that on region <sub>??</sub>).

$\mathcal { E } _ { 0 } ^ { 2 } \mathrm { : }$ Bidder 2 has incentive to raise its bid up to $k v _ { 2 }$ (same reasoning as that on region <sub>??</sub>). Bidder 1 has incentive to lower its bid to reduce the risk if bidder 2 bids more than $k v _ { 1 }$ $\mathcal { E } _ { 0 } ^ { 3 } \mathrm { . }$ : Bidder 1 has incentive to lower its bid to reduce the risk if bidder 2 bids more than $\mathfrak { c } v _ { 1 }$

• $\mathcal { E } _ { 0 } ^ { \star } \mathrm { : }$ No one has incentive to adjust bid.

As discussed above, rational bid revisions must follow the directions indicated by the arrows in various regions. For an arbitrary Nash equilibrium in $\mathcal { E } _ { 0 } ^ { \star }$ , if a perturbation forces it out of this region, following the directions indicated by the arrows, the bidding vector will eventually converge to $\mathcal { E } _ { 0 } ^ { \star }$ after several rational bid revisions.

According to the definition of SNE/LEF, it is easy to see that SNE/LEF is $\mathcal { E } _ { 0 } ^ { \star } \cup \mathcal { E } _ { 0 } ^ { 3 }$ . The stable set $\mathcal { E } _ { 0 } ^ { \star }$ (discussed in the next section) is only a subset of SNE/LEF. Thus, not all equilibria in SNE/LEF are stable in a dynamic environment.

## 6. Stable Nash Equilibrium Set

Since only $\mathcal { E } _ { 0 }$ is weakly stable, we only need to consider Nash equilibria in it. The previous example (Figure 4) shows that neither WSNE nor SNE/LEF is adequate for describing the bidding behaviors of a GSP auction in a dynamic environment. In this section, we propose the concept of stability and employ it to further refine WSNE and SNE/LEF. Stability is a widely used refinement in cybernetics and dynamic game, especially in evolutionary game theory and learning in game (Fudenberg & Levine, 1998). Its usage can be traced even back to Cournot’s duopoly game (Fudenberg & Tirole, 1991). We adopt this refinement to narrow the equilibrium set, in order to help advertisers bid in this market.

Definition 6.1. A subset <sub>??</sub> of $\mathcal { E } _ { 0 }$ is said to be a stable Nash equilibrium set (STNE), $i f \forall b \in \mathcal { A }$ and for arbitrary perturbation, which forces out of , the bidding vector will again form a Nash equilibrium in after a series of rational bid revisions.

Note that the stability considered here is about a subset of an equivalence polyhedron, while that typically considered in cybernetics and evolutionary game theory is about an individual equilibrium point. Furthermore, while system dynamics in cybernetics and evolutionary game theory is governed by differential/difference equation(s), the bidding dynamics concerned here are related to the rationality of bidders. Thus, only qualitative analysis is relevant, and such analysis is sufficient to determine the stability property of a Nash equilibrium polyhedron.

In $\mathcal { E } _ { 0 } { : }$ , the allocation of slots is efficient. As the allocation rule on ${ \mathcal { E } } _ { 0 }$ is the identity map, we will use $b _ { \alpha }$ to represent $b _ { \pi _ { \alpha } }$ in the following discussion for the sake of simplicity.

Consider the constraints of a Nash equilibrium on slots $\alpha - 1$ and . Because the bidder allocated to slot <sub>?? − 1</sub> does not have an incentive to lower its slot, we get:

$$
c _ {\alpha - 1} ^ {\alpha - 1} (v _ {\alpha - 1} - b _ {\alpha}) \geq c _ {a - 1} ^ {\alpha} (v _ {\alpha - 1} - b _ {\alpha + 1}) \Rightarrow b _ {\alpha} \leq \left(1 - \frac {1}{\gamma \alpha - 1}\right) v _ {\alpha - 1} + \frac {1}{\gamma \alpha - 1} b _ {\alpha + 1}\tag{14).}
$$

Similarly, because bidder <sub>??</sub> has no incentive to raise its slot, we get:

$$
c _ {\alpha} ^ {\alpha} (v _ {\alpha} - b _ {\alpha + 1}) \geq c _ {a} ^ {\alpha - 1} (v _ {\alpha} - b _ {\alpha - 1}) \Rightarrow b _ {\alpha - 1} \geq \left(1 - \frac {1}{\gamma \alpha - 1}\right) v _ {\alpha} + \frac {1}{\gamma \alpha - 1} b _ {\alpha + 1}\tag{15).}
$$

Next, we show that the lower bound given by Inequality 15 for slot (or bidder) $\alpha - 1$ is also a lower bound for slot <sub>??</sub>. To do so, we need to discuss the dynamic bidding behaviors of bidders <sub>??</sub> <sub>−</sub> <sub>1</sub> and $\alpha .$ Without loss of generality, we assume that the bid adjustments of these two bidders do not affect other bidders’ slots. Figure 5 illustrates the bidding dynamics of $\alpha - 1$ and <sub>??</sub> (<sub>ℰ</sub><sup>??</sup> has similar meaning as the $\mathcal { E } _ { 0 } ^ { \star }$ in Figure 4. We substitute the superscript $" \star "$ with $ { { ^ \circ } } \alpha ^ { \prime }$ to emphasize that we are discussing the bidding behaviors of bidders and $\alpha - 1 . )$ ) The figure appears similar to Figure 4 except that bid revisions are restricted to be within the rectangle $P _ { 1 } P _ { 2 } P _ { 3 } P _ { 4 }$ . If the bids of $\alpha - 1$ and <sub>??</sub> go out of this rectangle, other bidders may have incentive to change their slots, but the weak stability property of ${ \mathcal { E } } _ { 0 }$ guarantees that the bidding vector will come back to $\mathcal { E } _ { 0 }$ again. Therefore, restricting the bid revisions of $\alpha - 1$ and to the rectangle $P _ { 1 } P _ { 2 } P _ { 3 } P _ { 4 }$ is reasonable and can simplify the analysis. The actual values of $b ^ { L }$ and $b ^ { U }$ are not important, as we are only concerned with the bidding dynamics.

![](/api/attachments/VQGQTF34/fulltext/images/97623bdc85c83d2cf4ffe4ed6d6b877172a61ba620829dd5880b91c373ba50d0.jpg)  
Figure 5. Bid Adjustments of Bidders <sub>??</sub> <sub>−</sub> <sub>??</sub> and <sub>??</sub> in a Repeated GSP Auction

Using the same sort of analyses as that used in the previous example in Section 5.3, we can see that <sup>??</sup> is the stable region. After a period of dynamic adjustments, the bids of $\alpha - 1$ and <sub>??</sub> will converge to this region. Therefore, the lower bound given by Inequality 15 for $\alpha - 1$ is also a lower bound for .

Similarly, considering slots and $\alpha + 1$ , we can get another pair of bounds on :

$$
\tilde {b} _ {\alpha} \leq \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2}\tag{16),}
$$

$$
\tilde {b} _ {\alpha} \geq \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha + 1} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2}\tag{17).}
$$

By recursively using the above two pairs of bounds, we can get the bidding interval of bidder <sub>??</sub>. Suppose that $b _ { \alpha + 1 } ^ { U }$ and $b _ { \alpha + 1 } ^ { L }$ , upper and lower bounds of bidder $\alpha + 1$ , have been derived. Substituting these bounds into Inequalities 14 and 15, we get:

$$
b _ {\alpha} ^ {U _ {1}} = \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) v _ {\alpha - 1} + \frac {1}{\gamma_ {\alpha - 1}} b _ {\alpha + 1} ^ {U}\tag{18),}
$$

$$
b _ {\alpha} ^ {L _ {1}} = \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) v _ {\alpha} + \frac {1}{\gamma_ {\alpha - 1}} b _ {\alpha + 1} ^ {L}\tag{19).}
$$

Substituting them into Inequalities 16 and 17, we get:

$$
b _ {\alpha} ^ {U _ {2}} = \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2} ^ {U}\tag{20),}
$$

$$
b _ {\alpha} ^ {L _ {2}} = \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha + 1} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2} ^ {L}\tag{21).}
$$

The starting values for the above-described recursion are $b _ { K + 1 } ^ { U } = b _ { K + 1 } ^ { L } = v _ { K + 1 }$ , which follows the fact th at truth-telling is a weakly dominant strategy for the first excluded bidder (Varian, 2007; Vickrey, 1961).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
The game-theoretic implications of these four bounds are as follows.
• $b_{\alpha}^{L_1}$: If $\alpha$ bids less than this value, it would lose the opportunity to get slot $\alpha - 1$ with an increased payoff. This is also the lower bound of SNE/LEF.
• $b_{\alpha}^{L_2}$: If $\alpha$ bids less than this value, bidder $\alpha + 1$ may have incentive to deviate to slot $\alpha$.
• $b_{\alpha}^{U_1}$: If $\alpha$ bids more than this value, bidder $\alpha - 1$ may have incentive to lower its slot to $\alpha$, as otherwise its price would exceed the maximum threshold it can afford. This is also the upper bound of SNE/LEF and Nash equilibrium.
• $b_{\alpha}^{U_2}$: It is weakly dominated if $\alpha$ bids more than this value, as the higher bid does not bring a payoff to $\alpha$ and exposes $\alpha$ to a potential risk of losing the payoff.

Note that $b_{\alpha}^{L_2}$ and $b_{\alpha}^{U_1}$ are requirements of a Nash equilibrium, while $b_{\alpha}^{L_1}$ and $b_{\alpha}^{U_2}$ are results of rational reasoning or results of competitions. From the above discussion, it can be seen that $b_{\alpha}^{L_1}$ may be larger than $b_{\alpha}^{L_2}$ and $b_{\alpha}^{U_1}$ may be larger than $b_{\alpha}^{U_2}$. A sufficient condition guaranteeing this is $\gamma_1 \geq \gamma_2 \geq \cdots \geq \gamma_{K-1}$ (see Proposition 6.1 later). According to Equations 18–20, it is obvious that $b_{\alpha}^{U_1} &gt; b_{\alpha}^{L_1}$ and $b_{\alpha}^{U_2} &gt; b_{\alpha}^{L_2}$. In fact, $b_{\alpha}^{L_1}$ is not only the lower bound of $\alpha$ in SNE/LEF (Varian, 2007, 2009), but also the lower bound of STNE, as the following discussion will reveal (see Equations 23 and 25). Using these facts, we can get the bidding bounds of bidder $\alpha$ in the following two cases.

Case 1: $b_{\alpha}^{L_1} \leq b_{\alpha}^{U_2}$. It is obvious that the upper bound $b_{\alpha}^{U}$ is the minimum between $b_{\alpha}^{U_1}$ and $b_{\alpha}^{U_2}$, while the lower bound $b_{\alpha}^{L}$ is the maximum between $b_{\alpha}^{L_1}$ and $b_{\alpha}^{L_2}$; that is:

$b_{\alpha}^{U} = \min\{b_{\alpha}^{U_1}, b_{\alpha}^{U_2}\} = b_{\alpha}^{U_2} \quad (22),$ $b_{\alpha}^{L} = \max\{b_{\alpha}^{L_1}, b_{\alpha}^{L_2}\} = b_{\alpha}^{L_1} \quad (23).$

In this case, if bidding in the interval $[b_{\alpha}^L, b_{\alpha}^U]$, $\alpha$ can satisfy all four bounds (i.e., $b_{\alpha}^{L_1}, b_{\alpha}^{L_2}, b_{\alpha}^{U_1},$ and $b_{\alpha}^{U_2})$.

Case 2: $b_{\alpha}^{L_1} &gt; b_{\alpha}^{U_2}$. In this situation, at least one target cannot be realized, and bidding between $[b_{\alpha}^{U_2}, b_{\alpha}^{L_1}]$ is dominated since it breaks two bounds. So, there are two possible alternatives, $[b_{\alpha}^{L_1}, b_{\alpha}^{U_1}]$ and $[b_{\alpha}^{L_2}, b_{\alpha}^{U_2}]$. The former, which is the same as SNE/LEF, aims to obtain a potential payoff if bidder $\alpha - 1$ makes a mistake by placing a low bid, but runs the risk of a reduced payoff in case bidder $\alpha + 1$ raises its bid. The latter gives up the chance to obtain a potential payoff and focuses on maintaining the current payoff. However, the latter strategy is not stable (see Proposition 6.2 later). Thus, in Case 2, the former is the only, but unsatisfactory, choice; that is:

$b_{\alpha}^{U} = b_{\alpha}^{U_1} \quad (24),$ $b_{\alpha}^{L} = b_{\alpha}^{L_1} \quad (25).$

Proposition 6.1. If $\gamma_1 \geq \gamma_2 \geq \cdots \geq \gamma_{K-1}, b_{\alpha}^{L_1} \geq b_{\alpha}^{L_2}$ and $b_{\alpha}^{U_1} \geq b_{\alpha}^{U_2}.$

Proposition 6.2. If $b_{\alpha}^{L_1} &gt; b_{\alpha}^{U_2}, bidding in [b_{\alpha}^{L_2}, b_{\alpha}^{U_2}]$ is unstable.

As shown in Algorithm 1, because the value vector v and parameters $\gamma_1, \gamma_2, \cdots, \gamma_{K-1}$ are known to all bidders, by recursively using Formulae 18–25, every bidder can efficiently obtain all bidders' bidding intervals (the computational complexity of Algorithm 1 is linear with respect to the number of bidders, that is, O(N)). The STNE of a GSP auction can then be explicitly specified.

Journal of the Association for Information Systems Vol. 13 Issue 2 pp. 57-87 February 2012
</div>

```python
Input: K, N, γ, v

UB[1:N] = LB[1:N] = 0

For i = K + 1 To N

    UB[i] = LB[i] = v[i]

For i = K To 1

    upper1 = v[i - 1](1 - γ[i - 1]) + UB[i + 1]γ[i - 1]

    lower1 = v[i](1 - γ[i - 1]) + LB[i + 1]γ[i - 1]

    upper2 = v[i](1 - γ[i]) + UB[i + 2]γ[i]

    lower2 = v[i + 1](1 - γ[i]) + LB[i + 2]γ[i]

If lower1 ≤ upper2

    UB[i] = min{upper1, upper2}, LB[i] = max{lower1, lower2}

Else

    UB[i] = upper1, LB[i] = lower1

Output: UB, LB
```

## Algorithm 1. Computing STNE Bounds

## Define:

$$
\mathcal {D} _ {1} \triangleq [ b _ {1} ^ {L}, b _ {1} ^ {U} ] \times [ b _ {2} ^ {L}, b _ {2} ^ {U} ] \times \dots \times [ b _ {K} ^ {L}, b _ {K} ^ {U} ],
$$

$$
\mathcal {D} _ {2} \triangleq \{b | b _ {1} > b _ {2} > \dots > b _ {K} \},
$$

where $\mathcal { D } _ { 1 }$ is the Cartesian product of all bidders’ bidding intervals and is a finite cuboid and $\mathcal { D } _ { 2 }$ is the set of all efficient bidding vectors and is an infinite cone. The STNE can then be represented as:

$$
\mathcal {E} _ {0} ^ {\star} = \mathcal {D} _ {1} \cap \mathcal {D} _ {2} (2 6).
$$

If all bidders’ possible choices belong to Case 2, $\mathcal { E } _ { 0 } ^ { \star }$ is the same as SNE/LEF. Otherwise, $\mathcal { E } _ { 0 } ^ { \star }$ is just a proper subset of SNE/LEF.

## 7. Discussion and Implications

In this section, we discuss some implications of STNE to bidders and auctioneers. We also discuss the relationships between our proposed equilibrium refinements and major existing refinements.

## 7.1. Bidding Strategy

By employing Algorithm 1 (note that the value vector <sub>??</sub> and parameters $\gamma _ { 1 } , \gamma _ { 2 } , \cdots , \gamma _ { K - 1 }$ are common knowledge), the STNE bidding intervals of all advertisers can be efficiently calculated. A direct bidding strategy for an advertiser is simply to choose a bid from its own bidding interval. However, since some of the bidding intervals may overlap, even if every advertiser chooses a bid from its own interval, the bidding vector may not be a Nash equilibrium (region <sub>??</sub> in Figure 4 indicates this situation; this figure also shows that STNE, <sub>ℰ</sub><sup>⋆</sup>, exists even if some bidders’ bidding intervals overlap). Therefore, even if all advertisers use a stable strategy, there may be a period of bid revisions before the bidding vector converges into STNE. There are the following two possible situations.

• Non-overlapping: In this situation, an advertiser’s STNE bidding interval does not overlap with either that of the advertiser ranked just above or that of the one ranked just below. Thus, this advertiser can freely choose a bid in its STNE interval. In particular, it can choose from two special strategies: the upper bound and the lower bound of STNE. The upper bound strategy can help this advertiser decline the profit of the advertiser ranked just above. The lower bound strategy can reduce the loss in case the advertiser ranked just below mistakenly bids a large amount.

• Overlapping: In this situation, an advertiser’s STNE bidding interval overlaps with that of the advertiser ranked just above or that of the one ranked just below. If the advertiser chooses a bid in an overlapping zone, the outcome may not be a Nash equilibrium, and the advertiser may face some loss of revenue (as analyzed in the proof of Theorem 5.1). Therefore, the advertiser should bid in the remaining non-overlapping zone. It can still use the upper bound of this non-overlapping zone to cut the revenue of the advertiser ranked just above and use the lower bound to avoid potential risk in case the one ranked just below makes a mistake.

Note that, as Figure 4 shows, two bidders may have an identical upper bound ( ). If both bidders choose the identical upper bound as their strategies, the tie needs to be broken by the auctioneer. However, the tie-breaking rule is pre-determined by the auctioneer and is not part of a bidder’s bidding strategy.

## 7.2. Realizable Revenue

As the above discussion indicates, the bidding vector will form a Nash equilibrium in STNE after a period of bid revisions. As there still exists great freedom for a bidder to choose a bid, one still cannot predict exactly which Nash equilibrium in STNE will be the final outcome. However, no matter which stable Nash equilibrium is the final outcome, the revenue of the search engine on STNE is at least the same as that under VCG. Varian (2009) shows that the revenue on SNE/LEF is at least the same as that under VCG, and STNE is a subset of SNE. This is a good property to the search engine. On the other hand, while the minimal revenue on STNE equals that on SNE/LEF, the maximal revenue on STNE is less than that on SNE/LEF. Although this seems to be unfavorable to the search engine, we point out that the maximal revenue of SNE/LEF is attained at an unstable and risk-dominated equilibrium and, hence, has no practical value (i.e., it is not realizable). Therefore, managerially, we recommend the use of the maximal revenue on the STNE set rather than that on the SNE/LEF set as a benchmark for evaluating different auction mechanisms.

As to an advertiser, the price of a GSP auction on STNE is, thus, at least the same as that under VCG. This is, indeed, necessary because every bidder must bid truthfully in the VCG mechanism, but revealing this information may cause lots of problems (see Ausubel & Milgrom, 2006, & Rothkopf, 2007, for detailed discussions). However, in a GSP auction, every bidder is free to choose a preferred bid in its STNE bidding interval. Although it is somewhat expensive in comparison with VCG, the final outcome will be efficient, fair, and free from the problems associated with truth-telling.

## 7.3. Relationships with Other Equilibrium Concepts

As we have proved, in a dynamic environment, the polyhedron in which all equilibria are efficient is weakly stable, whereas all other polyhedra are unstable. We also find that the bidding vector will converge into STNE, which is a subset of the weakly stable polyhedron, after a series of rational bid revisions. Cary et al. (2007) and Vorobeychik and Reeves (2008) propose a greedy bidding strategy in a repeated GSP auction and found a specific point to which the bidding vector will converge under their balance strategy (Bu et al., 2008, report a similar result). However, they assumed a perfect information structure (i.e., the bidding vector is known to all bidders after each stage auction). In our treatment, we used an imperfect information structure. As a result, a set of equilibria, rather than a single equilibrium, can be used to interpret the final outcome.

Varian (2007, 2009) states that SNE is a good description of the bidding behaviors in Google’s AdWords system and provided some explanations for the upper and lower bounds for SNE. However, based on the above analysis, we can see that SNE is the result of rational bid revisions in a repeated GSP auction. Furthermore, SNE is not as powerful as STNE. Generally, SNE can be employed to describe the situation of Case 2 (discussed in Section 6), but is not a good equilibrium refinement for Case 1 because it contains some risk-dominated strategies. The relationships of these equilibrium concepts can be summarized as follows:

$$
\mathrm{PSNE} \supseteq \mathrm{WSNE} \supseteq \mathrm{SNE/LEF} \supseteq \mathrm{STNE}.
$$

We can also relate our results to the stable core of an assignment game (or more generally, the twosided matching game). Edelman et al. (2007) establishes the relationship between GSP auction and the assignment game studied by Shapley and Shubik (1972), and finds that each LEF induces a core price vector, and each core price vector can be implemented by a LEF. Our results show that STNE is a proper subset of SNE/LEF in Case 1 and, therefore, can only correspond to a subset of the stable core of an assignment game. The reason is that we take the risk of bidding into consideration, thus ruling out some risk-dominated strategies. The definition of stable core does not account for risk, especially in twosided matching games without payment from one side to the other; such as the marriage match game (Bikhchandani & Ostroy, 2006; Roth & Sotomayor, 1992). However, this is not really a surprising result, as Shapley and Shubik (1972) point out that the stable core contains not only all competitive outcomes but also other outcomes without a corresponding competitive implementation.

## 8. Conclusion

In this paper, we provide a comprehensive analysis of pure-strategy Nash equilibria of GSP auction in both static and dynamic environments. We make several original contributions. First, we find all the PSNE of a GSP auction. When using the “same-slot” relation defined on the entire space of PSNE, the nonlinear allocation rule in the definition of PSNE can be eliminated. Then, well-developed methods can be employed to find all PSNE. Generally, each equivalence class of PSNE under this same-slot relation is a convex polyhedron, and all polyhedra are distributed in the pure-strategy space separately, if valuations of all bidders are distinct. We also derive a general upper bound for the number of possible polyhedra.

Second, in order to weed out inefficient equilibria, we study the repeated version of a GSP auction. We propose weak stability and stability (similar to concepts used in cybernetics and evolutionary game theory) for equilibrium refinements. We prove that the polyhedron in which all equilibria are efficient is weakly stable, whereas all other polyhedra are unstable.

Third, we conclude that the bidding vector will converge into STNE after a series of rational bid revisions. We also find that SNE/LEF is a subset of the weakly stable polyhedron and that STNE is the same as or a proper subset of SNE/LEF. SNE/LEF may contain risk-dominated strategies, whereas STNE never does.

Our findings have important practical implications. We show that a GSP auction (with quality score) is a dynamic efficient mechanism, implying that it can maximize the social welfare of the advertising market. From the point of view of auctioneers (search engines), the revenue on STNE is at least the same as that under VCG, and auctioneers can use the STNE revenue as a benchmark for evaluating other auction mechanisms. From the point of view of advertisers, as the STNE bidding intervals can be calculated efficiently, our result provides them a simple yet effective and stable strategy. The outcome of the STNE bidding strategy is efficient and fair while exposing no secret information of advertisers.

Our work also opens avenues for further work, which may extend ours by relaxing the assumptions of complete information and budget-free. First, in practice, the valuation of a bidder is usually private information. A frequently used framework to deal with incomplete information is to assume the joint distribution of the valuations of all bidders to be common knowledge. Another possible approach is to develop valuation estimation algorithms based on both acquired historical data and the equilibrium structure. Second, the optimal bidding strategy for bidders under budget constraints is still open to investigation. A possible approach to deal with such constraints is to change the payoff from the expected profit to a function taking return-on-investment into account. Another direction for future work is to empirically validate our proposed refinement concepts, especially the STNE, with real keyword auction data. Currently, an apparent obstacle in this direction is the fact that past bidding behaviors observed at practical keyword auctions are not based on the equilibrium structure that we reveal in this paper or on our proposed refinements.

## Acknowledgements

The reported research is partially funded through CAS Grants #2F07C01, #2F09N05, and #2F09N06, and NNSFC Grants #60875049, #60921061, #70890084, #71025001, #71071152, and #71102117.

The authors would like to thank the anonymous reviewers for their helpful comments and suggestions.

## References

Aggarwal, G., Feldman, J., Muthukrishnan, S., & Pal, M. (2008). Sponsored search auctions with Markovian users. Proceedings of the ACM EC-08 Workshop on Ad Auctions, Chicago, IL.

Aggarwal, G., Goel, A., & Motwani, R. (2006). Truthful auctions for pricing search keywords. Proceedings of the 7th ACM Conference on Electronic Commerce, Ann Arbor, MI, 1-7.

Aggarwal, G., & Hartline, J. D. (2006). Knapsack auctions. Proceedings of the 17th Annual ACM-SIAM Symposium on Discrete Algorithm, Miami, FL, 1083-1092.

Aggarwal, G., Muthukrishnan, S., Pal, D., & Pal, M. (2009). General auction mechanism for search advertising. Proceedings of the 18th International Conference on World Wide Web, Madrid, Spain, 241-250.

Animesh, A., Ramachandran, V., & Viswanathan, S. (2010). Research note–quality uncertainty and the performance of online sponsored search markets: An empirical investigation. Information Systems Research, 21(1), 190-201.

Ashlagi, I., Braverman, M., Hassidim, A., Lavi, R., & Tennenholtz, M. (2010). Position auctions with budgets: Existence and uniqueness. The B.E. Journal of Theoretical Economics, 10(1), 1-30.

Athey, S., & Nekipelov, D. (2010). A structural model of sponsored search advertising auctions. Proceedings of the 6th Workshop on Ad Auctions, Cambridge, MA.

Ausubel, L. M., & Milgrom, P. (2006). The lovely but lonely Vickrey auction. In P. Cramton, Y. Shoham, & R. Steinberg (Eds.), Combinatorial auctions (pp. 17-40). Cambridge, MA: The MIT Press.

Baidu. (2010). Baidu announces fourth quarter and fiscal year 2009 results. Retrieved from http://phx.corporate-ir.net/External.File?item=UGFyZW50SUQ9MzEyMzd8Q2hpbGRJRD0t MXxUeXBlPTM=&t=1.

Balachander, S., Kannan, K., & Schwartz, D. G. (2009). A theoretical and empirical analysis of alternate auction policies for search advertisements. Review of Marketing Science, 7(1), 1-49.

Bikhchandani, S., & Ostroy, J. M. (2006). From the assignment model to combinatorial auctions. In P. Cramton, Y. Shoham, & R. Steinberg (Eds), Combinatorial Auctions (pp. 189-210). Cambridge, MA: The MIT Press.

Börgers, T., Cox, I., Pesendorfer, M., & Petricek, V. (2007). Equilibrium bids in sponsored search auctions: theory and evidence. Working Paper.

Bu, T.-M., Deng, X., & Qi, Q. (2007). Dynamics of strategic manipulation in AdWords auction. Proceedings of the 3rd Workshop on Sponsored Search Auctions, Banff, Canada.

Bu, T.-M., Deng, X., & Qi, Q. (2008). Forward looking Nash equilibrium for keyword auction. Information Processing Letters, 105(2), 41-46.

Cary, M., Das, A., Edelman, B., Giotis, I., Heimerl, K., Karlin, A. R., Mathieu, C., & Schwarz, M. (2007). Greedy bidding strategies for keyword auctions. Proceedings of the 8th ACM Conference on Electronic Commerce, San Diego, CA, 262-271.

Chen, J., Liu, D., & Whinston, A. B. (2009). Auctioning keywords in online search. Journal of Marketing, 73(4), 125–141.

Clarke, E. H. (1971). Multipart pricing of public goods. Public Choice, 11(1), 17-33.

Craswell, N., Zoeter, O., Taylor, M., & Ramsey, B. (2008). An experimental comparison of click position-bias models. Proceedings of 1st ACM Conference on Web Search and Web Data Mining, Stanford, CA, 87-94.

DCCI. (2010). Ten development trends of the online marketing market of China. Retrieved from http://www.zhanghangfeng.cn/post/2160.html.

Edelman, B., & Ostrovsky, M. (2007). Strategic bidder behavior in sponsored search auctions. Decision Support Systems, 43(1), 192-198.

Edelman, B., Ostrovsky, M., & Schwarz, M. (2007). Internet advertising and the generalized secondprice auction: Selling billions of dollars worth of keywords. American Economic Review, 97(1), 242-259.

Feng, J. (2008). Optimal mechanism for selling a set of commonly ranked objects. Marketing Science, 27(3), 501-512.

Feng, J., Bhargava, H. K., & Pennock, D. M. (2007). Implementing sponsored search in web search engines: Computational evaluation of alternative mechanisms. INFORMS Journal on Computing, 19(1), 137-148.

Feng, J., Shen, Z.-J. M., & Zhan, R. L. (2007). Ranked items auctions and online advertisement. Production and Operations Management, 16(4), 510-522.

Fudenberg, D., & Levine, D. K. (1998). The theory of learning in games. Cambridge, MA: The MIT Press.

Fudenberg, D., & Tirole, J. (1991). Game theory. Cambridge, MA: The MIT Press.

Garg, D., Narahari, Y., & Reddy, S. S. (2007). Design of an optimal auction for sponsored search auctions. Proceedings of the 9th IEEE International Conference on Ecommerce Technology and the 4th IEEE International Conference on Enterprise Computing, E-Commerce and E-Services, Tokyo, Japan.

Ghose, A., & Yang, S. (2009). An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Science, 55(10), 1605-1622.

Goel, A., & Munagala, K. (2009). Hybrid keyword search auctions. Proceedings of the 18th International Conference on World Wide Web, Madrid, Spain, 221-230.

Gomes, R. D., & Sweeney, K. S. (2009). Bayes-Nash equilibria of the generalized second price auction. Working Paper.

Google. (2010a). Google 2009 annual report. Retrieved from

Google. (2010b). What is the AdWords “quality score” and how is it calculated? Retrieved from http://adwords.google.com/support/aw/bin/answer.py?hl=en&answer=10215.

Groves, T. (1973). Incentives in teams. Econometrica, 41(4), 617-631.

IAB. (2010). Internet ad revenues reach record quarterly high of \$6.3 billion in Q4’ 09. Retrieved from http://www.iab.net/about the iab/recent press releases/press release archive/pressrelease/pr-040710.

Iyengar, G. (2006). Characterizing optimal keyword auctions. Proceedings of the 2nd Workshop on Sponsored Search Auctions, Ann Arbor, Michigan.

Jansen, B. J., & Mullen, T. (2008). Sponsored search: An overview of the concept, history, and technology. International Journal of Electronic Business, 6(2), 114-131.

Kempe, D., & Mahdian, M. (2008). A cascade model for externalities in sponsored search. Proceedings of the ACM EC-08 Workshop on Ad Auctions, Chicago, IL.

Kitts, B., & LeBlanc, B. J. (2004). Optimal bidding on keyword auctions. Electronic Markets, 14(3):186-201.

Krishna, V. (2002). Auction theory. Academic Press.

Lahaie, S. (2006). An analysis of alternative slot auction designs for sponsored search. Proceedings of the 7th ACM Conference on Electronic Commerce, Ann Arbor, MI, 218-227.

Leme, R. P., & Tardos, E. (2010). Pure and Bayes-Nash price of anarchy for generalized second price auction. Proceedings of the 51st Annual IEEE Symposium on Foundations of Computer Science, Las Vegas, NV, 735-744.

Leonard, H. B. (1983). Elicitation of honest preferences for the assignment of individuals to positions. The Journal of Political Economy, 91(3), 461-479.

Liu, D., Chen, J., & Whinston, A. B. (2009). Current issues in keyword auctions. In G. Adomavicius, & A. Gupta (Eds), Handbook of Information Systems: Business Computing (pp. 69-96). Bingley, UK: Emerald Group Publishing Limited.

Liu, D., Chen, J., & Whinston, A. B. (2010). Ex ante information and the design of keyword auctions. Information Systems Research, 21(1), 133-153.

Milgrom, P. (2010). Simplified mechanisms with an application to sponsored-search auctions. Games and Economic Behavior, 70(1), 62-70.

Muthukrishnan, S. (2008). Internet ad auctions: Insights and directions. Proceedings of the 35th International Colloquium on Automata, Languages and Programming (Part I), Reykjavik, Iceland.

Nash, J. F. (1950). Non-cooperative games. (Doctoral thesis, Princeton University).

Osborne, M. J., & Rubinstein, A. (1994). A course in game theory. Cambridge, MA: The MIT Press.

Roth, A. E., & Sotomayor, M. A. O. (1992). Two-sided matching: A study in game-theoretic modeling and analysis. Cambridge, MA: Cambridge University Press.

Rothkopf, M. H. (2007). Thirteen reasons why the Vickrey-Clarke-Groves process is not practical. Operations Research, 55(2), 191-197.

Shapley, L. S., & Shubik, M. (1972). The assignment game I: The core. International Journal of Game Theory, 1(1):111-130.

Solodovnikov, A. S. (1980). Systems of linear inequalities (English translation edition). Chicago, IL: University of Chicago Press.

Thompson, D. R. M., & Leyton-Brown, K. (2008). Tractable computational methods for finding Nash equilibria of perfect-information position auctions. Proceedings of the 9th ACM EC Workshop on Advertisement Auctions, Chicago, IL.

Thompson, D. R. M., & Leyton-Brown, K. (2009). Computational analysis of perfect-information position auctions. Proceedings of the 10th ACM Conference on Electronic Commerce, Stanford, CA, 51-60.

Varian, H. R. (2007). Position auctions. International Journal of Industrial Organization, 25(6),1163- 1178.

Varian, H. R. (2009). Online ad auctions. American Economic Review, 99(2), 430-434.

Vickrey, W. (1961). Counterspeculation, auctions, and competitive sealed tenders. Journal of Finance, 16(1), 8-37.

Vorobeychik, Y., & Reeves, D. M. (2008). Equilibrium analysis of dynamic bidding in sponsored search auctions. International Journal of Electronic Business, 6(2), 172-193.

Yahoo!. (2010). Ad quality and quality index. Retrieved from

Zhang, X., & Feng, J. (2005). Price cycles in online advertising auctions. Proceedings of the 26th International Conference on Information Systems, Las Vegas, NV.

http://help.yahoo.com/l/us/yahoo/ysm/sps/faqsall/faqs .html#quality index.

## Appendix A.

## Proof of Theorem 4.1.

Case 1: $N \leq K .$ . Suppose that bidding vector ${ \pmb { b } } ^ { \star }$ is a Nash equilibrium with $m \ge 2$ bidders who bid the same value <sup>⋆</sup>. According to the allocation rule of GSP auction mechanism, these bidders will be allocated to <sub>??</sub> contiguous slots with the same probability ${ \frac { 1 } { m } } .$ Denote these <sub>??</sub> slots as $s , s + 1 , \cdots , s +$ $m - 1 ( s \geq 1 , s + m - 1 \leq N )$

Now, consider a bidder, say <sub>??</sub>, from these <sub>??</sub> bidders. Its current payoff is:

$$
\frac {1}{m} [ c _ {i} ^ {s} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + 1} (v _ {i} - b ^ {\star}) + \dots + c _ {i} ^ {s + m - 2} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + m - 1} (v _ {i} - p) ]\tag{27),}
$$

where $p = b _ { \pi _ { s + m } }$ is the bid just below $b ^ { \star } ,$ , and $v _ { i } - p > 0$ since $b ^ { \star }$ is a Nash equilibrium.

If bidder <sub>??</sub> raises bid slightly, it would be allocated to slot <sub>??</sub> and get a payoff:

$$
c _ {i} ^ {s} (v _ {i} - b ^ {\star})\tag{28).}
$$

Since ${ \pmb { b } } ^ { \star }$ is a Nash equilibrium, bidder <sub>??</sub> has no incentive to raise bid. In other words, Payoff 27 is larger than payoff (28); that is:

$$
\frac {1}{m} [ c _ {i} ^ {s} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + 1} (v _ {i} - b ^ {\star}) + \dots + c _ {i} ^ {s + m - 2} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + m - 1} (v _ {i} - p) ] \geq c _ {i} ^ {s} (v _ {i} - b ^ {\star})\tag{29).}
$$

Define $\begin{array} { r } { \bar { \delta } = \frac { c _ { i } ^ { s + m - 1 } } { ( m - 1 ) c _ { i } ^ { s } - \sum _ { t = s + 1 } ^ { s + m - 2 } c _ { i } ^ { t } } , } \end{array}$ the above inequality can then be simplified as:

$$
b ^ {\star} \geq v _ {i} - \bar {\delta} (v _ {i} - p)\tag{30).}
$$

Now, if bidder lowers bid slightly, it would be allocated to slot $s + m - 1$ and get a payoff:

$$
c _ {i} ^ {s + m - 1} (v _ {i} - p)\tag{31).}
$$

Again, Payoff 27 is larger than the above Payoff 31; that is,

$$
\frac {1}{m} [ c _ {i} ^ {s} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + 1} (v _ {i} - b ^ {\star}) + \dots + c _ {i} ^ {s + m - 2} (v _ {i} - b ^ {\star}) + c _ {i} ^ {s + m - 1} (v _ {i} - p) ] \geq c _ {i} ^ {s + m - 1} (v _ {i} - p)\tag{32).}
$$

Define $\begin{array} { r } { \underline { { \delta } } = \frac { ( m - 1 ) c _ { i } ^ { s + m - 1 } } { \sum _ { t = s } ^ { s + m - 2 } c _ { i } ^ { t } } = \frac { c _ { i } ^ { s + m - 1 } } { \sum _ { t = s } ^ { s + m - 2 } c _ { i } ^ { t } / ( m - 1 ) } , } \end{array}$ the above inequality can then be simplified as:

$$
b ^ {\star} \leq v _ {i} - \underline {{\delta}} (v _ {i} - p)\tag{33).}
$$

Define:

$$
\overline {{b _ {i}}} = v _ {i} - \overline {{\delta}} (v _ {i} - p),
$$

$$
\underline {{b _ {i}}} = v _ {i} - \underline {{\delta}} (v _ {i} - p),
$$

$$
\mathcal {D} _ {i} = \Big \{b | \overline {{b _ {\iota}}} \leq b \leq \underline {{b _ {i}}} \Big \}.
$$

According to the above analyses, $b ^ { \star } \in \mathcal { D } _ { i }$ . Next, we show that $\mathcal { D } _ { i } = \phi$

$$
\mathrm{If} m > 2
$$

$$
(m - 1) c _ {i} ^ {s} - \sum_ {t = s + 1} ^ {s + m - 2} c _ {i} ^ {t} = c _ {i} ^ {s} + (c _ {i} ^ {s} - c _ {i} ^ {s + 1}) + \dots + (c _ {i} ^ {s} - c _ {i} ^ {s + m - 2}) > c _ {i} ^ {s} > \sum_ {t = s} ^ {s + m - 2} c _ {i} ^ {t} / (m - 1).
$$

Thus, $\overline { { \delta } } < \underline { { \delta } }$ and $\overline { { b _ { i } } } > \underline { b } _ { i }$ . This implies that $\mathcal { D } _ { i } = \phi$ , contradicting the assumption made at the beginning.

If $\begin{array} { r } { m = 2 , \overline { { \delta } } < \underline { { \delta } } = \frac { c _ { i } ^ { s + 1 } } { c _ { i } ^ { s } } , \overline { { b _ { i } } } = \underline { { b _ { i } } } } \end{array}$ , and thus $\mathcal { D } _ { i } = \left\{ \overline { { b _ { i } } } \right\} , b ^ { \star } = \overline { { b _ { i } } }$ . For the other bidder, <sub>??</sub>, using the same analysis, we get that $\mathcal { D } _ { j } = \left\{ \overline { { b _ { j } } } \right\}$ and $b ^ { \star } = \overline { { b _ { j } } }$ . Since $v _ { i } \neq v _ { j } , \overline { { b _ { i } } } \neq \overline { { b _ { j } } }$ , which implies $b ^ { \star } \neq b ^ { \star }$ , a contradiction.

Case 2: $N > K$ . It has been proven in Case 1 that:

$$
b _ {\pi_ {1}} > b _ {\pi_ {2}} > \dots > b _ {\pi_ {K}}.
$$

Now, suppose that $b _ { \pi _ { K } } = b _ { \pi _ { K + 1 } } = b ^ { \star }$ and denote corresponding bidders as <sub>??</sub> and $j .$ The payoffs of these two bidders will be $\frac { 1 } { 2 } c _ { i } ^ { K } ( v _ { i } - b ^ { \star } )$ and $\begin{array} { r } { \frac { 1 } { 2 } c _ { j } ^ { K } \left( v _ { j } - b ^ { \star } \right) } \end{array}$ , respectively. If one bidder, say $i ,$ raises bid, it will be allocated to slot and receive a payoff $c _ { i } ^ { K } ( v _ { i } - b ^ { \star } )$ , which is larger than $\frac { 1 } { 2 } c _ { i } ^ { K } ( v _ { i } - b ^ { \star } )$ . Thus, bidder <sub>??</sub> has incentive to raise bid, contradicting the fact that $\pmb { b } ^ { \star }$ is a Nash equilibrium.

## Proof of Theorem 4.2.

Case 1: $N \leq K$ . The maximum number of equivalence classes is just the total number of permutations of bidders, i.e., .

Case $2 \colon N > K .$ . Let $\mathcal { N } _ { 1 }$ and $\mathcal { N } _ { 2 }$ be subsets of <sub>??</sub> consisting of the first <sub>??</sub> bidders and the remaining bidders, respectively.

First, consider the possible polyhedra that allocate all the slots to the bidders in $\mathcal { N } _ { 1 }$ . The total number of permutations of the bidders in $\mathcal { N } _ { 1 }$ is $K !$

Second, consider an allocation that allocates a slot to one bidder, say $j ,$ in $\mathcal { N } _ { 2 }$ . This forces another bidder, say , in $\mathcal { N } _ { 1 }$ to lose in the auction. Next, we prove that only slot is a possible choice for bidder .

At a Nash equilibrium, as bidder has no incentive to get a slot, the bid of every bidder who gets a slot must be above bidder ’s valuation, $v _ { i } .$ . Suppose that bidder is allocated to a slot other than . Bidder <sub>??</sub> will face a price $p \geq v _ { i }$ as there will be a bidder below it. Bidder <sub>??</sub> has incentive to deviate, since $v _ { i } \geq v _ { j }$ and, hence, its payoff is negative, contradicting the assumption. Therefore, only slot <sub>??</sub> is possible for bidder .

Using the same reasoning, we can prove that no more than one slot can be allocated to bidders in $\mathcal { N } _ { 2 }$ and that only bidder <sub>??</sub> can be forced out. The number of bidders in $\mathcal { N } _ { 2 }$ is $N - K ,$ and the number of permutations of the first $K - 1$ bidders is $( K - 1 ) !$ , so the total number of polyhedra that allocate a slot to a bidder in $\mathcal { N } _ { 2 } \mathrm { ~ i s ~ } ( N - K ) ( K - 1 ) !$

The total number of possible polyhedra in Case 2 is, therefore, $K ! + ( N - K ) ( K - 1 ) ! = K ! +$ $N ( K - 1 ) ! - K ( K - 1 ) ! \stackrel { } { = } N ( K - 1 ) !$

## Proof of Theorem 5.1.

Consider a neighboring unstable factor involving bidder <sub>??</sub> and <sub>??</sub>, where $v _ { i } > v _ { j } , \psi _ { j } = \alpha _ { : }$ , and $\psi _ { i } = \alpha +$ . The constraints for bidding vector as a Nash equilibrium on slots and $\alpha + 1$ are:

$$
c _ {j} ^ {a} \big (v _ {j} - b _ {i} \big) \geq c _ {j} ^ {a + 1} \big (v _ {j} - b _ {\pi_ {a + 2}} \big) \Rightarrow b _ {i} \leq \frac {c _ {j} ^ {a} - c _ {j} ^ {a + 1}}{c _ {j} ^ {a}} v _ {j} + \frac {c _ {j} ^ {a + 1}}{c _ {j} ^ {a}} b _ {\pi_ {a + 2}} = \Big (1 - \frac {1}{\gamma_ {\alpha}} \Big) v _ {j} + \frac {1}{\gamma_ {\alpha}} b _ {\pi_ {a + 2}} \triangleq \lambda_ {\alpha}\tag{34),}
$$

$$
c _ {i} ^ {a + 1} \big (v _ {i} - b _ {\pi_ {a + 2}} \big) \geq c _ {i} ^ {a} \big (v _ {i} - b _ {j} \big) \Rightarrow b _ {j} \geq \frac {c _ {i} ^ {a} - c _ {i} ^ {a + 1}}{c _ {i} ^ {a}} v _ {j} + \frac {c _ {i} ^ {a + 1}}{c _ {i} ^ {a}} b _ {\pi_ {a + 2}} = \Big (1 - \frac {1}{\gamma_ {\alpha}} \Big) v _ {i} + \frac {1}{\gamma_ {\alpha}} b _ {\pi_ {a + 2}} \triangleq \kappa_ {\alpha}\tag{35),}
$$

Since $v _ { j } < v _ { i } , \lambda _ { \alpha } < \kappa _ { \alpha }$

If bidders $j = \pi _ { \alpha }$ and $i = \pi _ { \alpha + 1 }$ are swapped while holding other bidders’ bids unchanged, the new Nash equilibrium conditions are

$$
c _ {i} ^ {a} (v _ {i} - b _ {j}) \geq c _ {i} ^ {a + 1} (v _ {i} - b _ {\pi_ {a + 2}}) \Rightarrow b _ {j} \leq \frac {c _ {i} ^ {a} - c _ {i} ^ {a + 1}}{c _ {i} ^ {a}} v _ {i} + \frac {c _ {i} ^ {a + 1}}{c _ {i} ^ {a}} b _ {\pi_ {a + 2}} = \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {i} + \frac {1}{\gamma_ {\alpha}} b _ {\pi_ {a + 2}} = \kappa_ {\alpha}\tag{36),}
$$

$$
c _ {j} ^ {a + 1} \big (v _ {j} - b _ {\pi_ {\alpha + 2}} \big) \geq c _ {j} ^ {a} \big (v _ {j} - b _ {i} \big) \Rightarrow b _ {i} \geq \frac {c _ {j} ^ {a} - c _ {j} ^ {a + 1}}{c _ {j} ^ {a}} v _ {i} + \frac {c _ {j} ^ {a + 1}}{c _ {j} ^ {a}} b _ {\pi_ {a + 2}} = \Big (1 - \frac {1}{\gamma_ {\alpha}} \Big) v _ {j} + \frac {1}{\gamma_ {\alpha}} b _ {\pi_ {a + 2}} = \lambda_ {\alpha}\tag{37).}
$$

Next, we show that bidder <sub>??</sub> has incentive to realize this swapping. The current payoff of bidder <sub>??</sub> is $f _ { 1 } = c _ { i } ^ { a + 1 } \big ( v _ { i } - b _ { \pi _ { \alpha + 2 } } \big )$ . After swapping, its payoff would be $f _ { 2 } = c _ { i } ^ { a } { \left( v _ { i } - b _ { j } \right) }$ . The minimum payoff after swapping would be $\underline { { f _ { 2 } } } = c _ { i } ^ { a } ( v _ { i } - \kappa _ { \alpha } )$ . since $\underline { { f _ { 2 } } } \geq f _ { 1 }$ (Inequality 36), bidder <sub>??</sub> has incentive to swap slots with bidder <sub>??</sub>.

For convenience, we temporarily assume that bidder knows $b _ { \pi _ { a + 2 } }$ . In this setting, the strategy for bidder to accomplish the above swapping is to raise bid to $\widehat { b } _ { i }$ such that $\lambda _ { \alpha } < \widehat { b } _ { i } < \kappa _ { \alpha }$ . However, to show the effectiveness of this strategy for bidder $i ,$ we still have to analyze bidder $j ^ { \prime } { \mathsf { s } }$ behaviors. Note that bidder has two options now: lower bid to slot $\alpha + 1$ or keep bid to maintain the current slot $\alpha .$ In slot $\alpha ,$ , the expected profit of bidder $j$ is $c _ { j } ^ { a } \big ( v _ { j } - \hat { b } _ { i } \big )$ , whereas in slot $\alpha + 1$ , the expected profit is $c _ { j } ^ { a + 1 } \big ( v _ { j } - b _ { \pi _ { \alpha + 2 } } \big )$ . Since $\widehat { b } _ { i } > \lambda _ { \alpha }$ , we have:

$$
c _ {j} ^ {a + 1} \big (v _ {j} - b _ {\pi_ {\alpha + 2}} \big) \leq c _ {j} ^ {a} \big (v _ {j} - \lambda_ {\alpha} \big)
$$

$= \ c _ { j } ^ { a } \left( v _ { j } - \left( 1 - { \textstyle \frac { 1 } { \gamma _ { \alpha } } } \right) v _ { j } - { \textstyle \frac { 1 } { \gamma _ { \alpha } } } b _ { \pi _ { a + 2 } } \right)$ [inequality (37)]

$$
= \frac {c _ {j} ^ {a}}{\gamma_ {\alpha}} \big (v _ {j} - b _ {\pi_ {\alpha + 2}} \big)
$$

$$
= c _ {j} ^ {a + 1} \big (v _ {j} - b _ {\pi_ {\alpha + 2}} \big)\tag{38).}
$$

Thus, bidder <sub>??</sub> cannot afford to maintain slot $\alpha ,$ and it is profitable for bidder <sub>??</sub> to deviate to slot $\alpha + 1$

Figure A.1 shows a possible adjustment that accomplishes this swap. Bidder <sub>??</sub> raises bid to $\widehat { b } _ { i }$ and the bidding vector moves to point A. Since bidder <sub>??</sub> knows the value of $\widehat { b } _ { i }$ (its price), it chooses a bid less than ${ \widehat { b } } _ { i } ,$ causing the bidding vector to move to point B (in general, we cannot predict the locations of points A and B accurately). No matter where A and B are, bidder obtains slot with an increased profit.

In the preceding analysis, we temporarily assumed that bidder knows $b _ { \pi _ { \alpha + 2 } }$ . However, as the information structure adopted in this paper does not allow bidder <sub>??</sub> to directly know $b _ { \pi _ { \alpha + 2 } }$ , bidder <sub>??</sub> needs to convey such information to bidder <sub>??</sub>. A possible strategy for bidder <sub>??</sub> is to lower its bid to $\overline { { b } } = b _ { \pi _ { \alpha + 2 } } + \epsilon ( \epsilon > 0 )$ , allowing bidder <sub>??</sub> to infer that $b _ { \pi _ { \alpha + 2 } } < \overline { { b } }$ (as <sub>??</sub> is bidder $j ^ { \prime } { \mathsf { s } }$ new price). Next, bidder <sub>??</sub> raises bid to $b _ { \epsilon }$ to force bidder <sub>??</sub> to lower slot. The expected profit of bidder <sub>??</sub> would be $c _ { j } ^ { a } \big ( v _ { j } - b _ { \epsilon } \big )$ in slot or $c _ { j } ^ { \bar { a } + 1 } \big ( v _ { j } - b _ { \pi _ { \alpha + 2 } } \big )$ in slot $\alpha + 1$ . Although bidder <sub>??</sub> does not know $b _ { \pi _ { \alpha + 2 } }$ exactly, it can infer that:

$$
c _ {j} ^ {a + 1} \big (v _ {j} - b _ {\pi_ {\alpha + 2}} \big) > c _ {j} ^ {a + 1} \big (v _ {j} - \overline {{b}} \big).
$$

Thus, to force bidder <sub>??</sub> to lower slot, bidder <sub>??</sub>’s new bid $b _ { \epsilon }$ should satisfy:

$$
c _ {j} ^ {a + 1} \big (v _ {j} - \overline {{b}} \big) \geq c _ {j} ^ {a} \big (v _ {j} - b _ {\epsilon} \big).
$$

Solving this inequality, we get bidder <sub>??</sub>’s new bid:

$$
b _ {\epsilon} \geq \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {j} + \frac {1}{\gamma_ {\alpha}} \overline {{b}}
$$

$$
= \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {j} + \frac {1}{\gamma_ {\alpha}} b _ {\pi_ {\alpha + 2}} + \frac {1}{\gamma_ {\alpha}} \epsilon
$$

$$
= \lambda_ {\alpha} + \frac {1}{\gamma_ {\alpha}} \epsilon .
$$

![](/api/attachments/VQGQTF34/fulltext/images/269d3ec06bfb1d74088f85c1ec66b320eaf33216f7b02c5fa85ff0dc3a47b84a.jpg)

## Figure A-1. Slot Swapping of Bidders <sub>??</sub> and <sub>??</sub>

To make the strategy effective, $b _ { \epsilon }$ must be less than $\kappa _ { \alpha } ,$ , i.e., $\lambda _ { \alpha } + \frac { 1 } { \gamma _ { \alpha } } \epsilon \leq b _ { \epsilon } \leq \kappa _ { \alpha }$ , and, hence:

$$
\epsilon \leq (\gamma_ {\alpha} - 1) (v _ {i} - v _ {j}).
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
In summary, the strategy of bidder i is as follows:
• Choose a positive quantity  $\epsilon$  such that  $\epsilon &lt; (\gamma_{\alpha} - 1)(v_{i} - v_{j})$  and  $\epsilon &lt; b_{i} - b_{\pi_{\alpha+2}}$ , and lower bid to  $\overline{b} = b_{\pi_{\alpha+2}} + \epsilon$ ;
• Then, raise bid to  $b_{\epsilon}$  such that  $\lambda_{\alpha} + \frac{1}{\gamma_{\alpha}}\epsilon &lt; b_{\epsilon} &lt; \kappa_{\alpha}$ .
In the following, we prove that the inverse procedure is impossible. Note that both bidders i and j know  $b_{\pi_{\alpha+2}}$  in this situation. It can be seen, following the same reasoning, bidder j also has incentive to swap slots with bidder i. The strategy it can use is to raise bid too. Suppose that the bidding vector forms an equilibrium with  $b_{i} &gt; b_{j}$  and satisfies Inequalities 36 and 37. We show that this is impossible in the following two possible cases.
Case 1:  $\lambda_{\alpha} \leq b_{i} \leq \kappa_{\alpha}(b_{i} \geq \lambda_{\alpha}$  is due to Inequality 37.
In this case, to obtain slot  $\alpha$ , bidder j can choose a bid  $\hat{b}_{j} \geq b_{i}$  to get slot  $\alpha$  directly or choose a bid  $\hat{b}_{j} &lt; b_{i}$  to force bidder i to lower bid to slot  $\alpha + 1$ . First, the conditions of Nash Equilibrium 36 and 37 guarantee that the latter strategy (i.e., forcing bidder i to lower bid to slot  $\alpha + 1$ ) is infeasible (see also Figure A.1). Second, the former strategy (i.e., choosing a bid  $\hat{b}_{j} \geq b_{i}$  to get slot  $\alpha$  directly) does not work either. Note that, if bidder j applies this strategy, the expected profit of j obtained in slot  $\alpha$  is  $c_{j}^{a}(v_{j} - b_{i})$ , whereas that in slot  $\alpha + 1$  is again  $c_{j}^{a+1}(v_{j} - b_{\pi_{\alpha+2}})$ . Since  $b_{i} \geq \lambda_{\alpha}$ , we have  $c_{j}^{a}(v_{j} - b_{i}) \leq c_{j}^{a+1}(v_{j} - b_{\pi_{\alpha+2}})$  (similar to the deduction of inequality (38)); hence bidder j cannot afford to maintain slot  $\alpha$ , i.e., bidder i does not need to adjust its bid, whereas bidder j will find that it is not profitable to raise its bid to  $\hat{b}_{j} \geq b_{i}$ .
Case 2:  $b_{i} &gt; \kappa_{\alpha}$ . In this situation, bidder j has two strategies to choose from.
In one strategy, bidder j raises bid  $\hat{b}_{j}$  to at least  $b_{i}$  (bidder j can accomplish this by increasing its bid with a small increment  $\epsilon &gt; 0$ , successively). Since  $\hat{b}_{j} &gt; b_{i}$ , bidder j gets slot  $\alpha$ , directly. The profit bidder j would receive is  $c_{j}^{a}(v_{j} - b_{i})$ . Since  $b_{i} &gt; \kappa_{\alpha} &gt; \lambda_{\alpha}$ , the same reasoning employed in Case 1 shows that bidder j cannot afford to maintain slot  $\alpha$ .
In the other strategy, bidder j maintains slot  $\alpha + 1$  while raising its bid to reduce bidder i's profit. To force bidder i to lower slot,  $\hat{b}_{j}$  should be larger than  $\lambda_{\alpha}$  (Inequality 36). In this situation, bidder i needs to lower its slot and has two strategies: (1) lower its bid into the interval ( $\lambda_{\alpha}, \kappa_{\alpha}$ ) and (2) choose a bid  $\hat{b}_{i}$  in the interval ( $\kappa_{\alpha}, \hat{b}_{j}$ ). If bidder i uses the former strategy, inequality (38) guarantees that bidder j will lower its bid to get slot  $\alpha + 1$ . If bidder i chooses the latter strategy, bidder j can then choose a bid  $\lambda_{\alpha} &lt; \hat{b}_{j}' &lt; \hat{b}_{i}$  and continue to cut bidder i's profit, forcing bidder i to face the same issue it faced at the beginning. As the former strategy dominates the latter one, bidder i can simply adopt the former strategy at the very beginning and force bidder j to lower its slot to  $\alpha + 1$ .
Through the above reasoning, we have shown that bidder j cannot maintain slot  $\alpha$  stably, whereas bidder i can accomplish this objective.
Journal of the Association for Information Systems Vol. 13 Issue 2 pp. 57-87 February 2012
</div>

Proof of Proposition 6.1.

$$
b _ {\alpha} ^ {U _ {1}} - b _ {\alpha} ^ {U _ {2}} = \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) (v _ {\alpha - 1} - v _ {\alpha}) - \frac {1}{\gamma_ {\alpha - 1}} (v _ {\alpha} - b _ {\alpha + 1} ^ {U}) + \frac {1}{\gamma_ {\alpha}} (v _ {\alpha} - b _ {\alpha + 2} ^ {U}).
$$

Since $\begin{array} { r } { \gamma _ { \alpha - 1 } \geq \gamma _ { \alpha } , - \frac { 1 } { \gamma _ { \alpha - 1 } } \geq - \frac { 1 } { \gamma _ { \alpha } } , } \end{array}$ and hence:

$$
b _ {\alpha} ^ {U _ {1}} - b _ {\alpha} ^ {U _ {2}} \geq \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) (v _ {\alpha - 1} - v _ {\alpha}) - \frac {1}{\gamma_ {\alpha}} (v _ {\alpha} - b _ {\alpha + 1} ^ {U}) + \frac {1}{\gamma_ {\alpha}} (v _ {\alpha} - b _ {\alpha + 2} ^ {U})
$$

$$
= \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) (v _ {\alpha - 1} - v _ {\alpha}) + \frac {1}{\gamma_ {\alpha}} (b _ {\alpha + 1} ^ {U} - b _ {\alpha + 2} ^ {U}).
$$

Since $b _ { \alpha + 1 } > b _ { \alpha + 2 } ( \forall b \in \mathrm { S T N E } ) , b _ { \alpha + 1 } ^ { U } \geq b _ { \alpha + 2 } ^ { U } ,$ , and hence $b _ { \alpha } ^ { U _ { 1 } } \geq b _ { \alpha } ^ { U _ { 2 } }$

The proof of $b _ { \alpha } ^ { L _ { 1 } } \geq b _ { \alpha } ^ { L _ { 2 } }$ is similar.

Proof of Proposition 6.2.

Suppose bidder <sub>??</sub> plays the latter strategy; that is:

$$
\left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha + 1} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2} ^ {L} \leq b _ {\alpha} \leq \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha} + \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2} ^ {U}\tag{39).}
$$

Bidder $\alpha - 1$ could be in Case 1 or 2. Suppose it is in Case 2 and plays the latter strategy; that is:

$$
\left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) v _ {\alpha} + \frac {1}{\gamma_ {\alpha - 1}} b _ {\alpha + 1} ^ {L} \leq b _ {\alpha - 1} \leq \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) v _ {\alpha - 1} + \frac {1}{\gamma_ {\alpha - 1}} b _ {\alpha + 1} ^ {U}\tag{40).}
$$

Consider bidder <sub>??</sub> <sub>−</sub> <sub>2</sub>. Its current payoff per click is:

$$
v _ {\alpha - 2} - b _ {\alpha - 1} \leq v _ {\alpha - 2} - \left(1 - \frac {1}{\gamma_ {\alpha - 1}}\right) v _ {\alpha} - \frac {1}{\gamma_ {\alpha - 1}} b _ {\alpha + 1} ^ {L}\tag{41}
$$

$$
= v _ {\alpha - 2} - v _ {\alpha} + \frac {1}{\gamma_ {\alpha - 1}} (v _ {\alpha} - b _ {\alpha + 1} ^ {L}).
$$

If bidder $\alpha - 2$ is allocated to slot $\alpha - 1$ , its payoff per click will be:

$$
v _ {\alpha - 2} - b _ {\alpha} \geq v _ {\alpha - 2} - \left(1 - \frac {1}{\gamma_ {\alpha}}\right) v _ {\alpha} - \frac {1}{\gamma_ {\alpha}} b _ {\alpha + 2} ^ {U}\tag{42}
$$

$$
= v _ {\alpha - 2} - v _ {\alpha} + \frac {1}{\gamma_ {\alpha}} (v _ {\alpha} - b _ {\alpha + 2} ^ {U}).
$$

Since $b _ { \alpha } ^ { L _ { 1 } } > b _ { \alpha } ^ { U _ { 2 } }$ , we get:

$$
\frac {1}{\gamma_ {\alpha - 1}} (v _ {\alpha} - b _ {\alpha + 1} ^ {L}) <   \frac {1}{\gamma_ {\alpha}} (v _ {\alpha} - b _ {\alpha + 2} ^ {U})\tag{43).}
$$

Combining inequalities (41)-(43), we have $v _ { \alpha - 2 } - b _ { \alpha - 1 } < v _ { \alpha - 2 } - b _ { \alpha }$ . Therefore, bidder $\alpha - 2$ has incentive to deviate to slot <sub>?? − 1</sub>.

Otherwise, if <sub>??</sub> <sub>−</sub> <sub>1</sub> is in Case 1 or is in Case 2 and plays the former strategy, with the same reasoning, we can see that bidder $\alpha - 2$ has incentive to deviate to slot <sub>?? − 1</sub>.

## About the Authors

Linjing LI received the B.Eng. degree in electrical engineering and automation and the M.Eng. degree in control theory and control engineering both from Harbin Institute of Technology, Harbin, China, and the Ph.D. degree in computer applications from the Graduate University of the Chinese Academy of Sciences, Beijing, China. He is currently an Assistant Professor with the State Key Laboratory of Management and Control for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China. His research interests include game theory, mechanism design, auction theory, and machine learning.

Daniel ZENG received the M.S. and Ph.D. degrees in industrial administration from Carnegie Mellon University and the B.S. degree in economics and operations research from the University of Science and Technology of China, Hefei, China. He is a Research Professor at the Institute of Automation in the Chinese Academy of Sciences and a Professor and Eller Fellow in the Department of Management Information Systems at the University of Arizona. His research interests include intelligence and security informatics, infectious disease informatics, social computing, recommender systems, software agents, and applied operations research and game theory. He has published one monograph and more than 200 peer-reviewed articles. He has also co-edited 15 books and proceedings, and chaired many conferences including the IEEE International Conference on Intelligence and Security Informatics (ISI), the Biosurveillance and Biosecurity Workshop (BioSecure), and the International Workshop on Social Computing (SOCO). His research has been mainly funded by the U.S. NSF, the NNSF of China, the Chinese Academy of Sciences, U.S. DHS, and MOST and MOH of China.

Huimin ZHAO is an Associate Professor of Information Technology Management at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee. He earned his Ph.D. in MIS from The University of Arizona. His current research interests are in the areas of data mining and social computing. His research has been published in several journals, including Communications of the ACM; IEEE Transactions on Knowledge and Data Engineering; IEEE Transactions on Systems, Man, and Cybernetics; Information Systems; Data and Knowledge Engineering; Journal of Management Information Systems; Journal of the Association for Information Systems; and Decision Support Systems. He serves on the editorial review board of the Journal of Database Management and as the treasurer of the INFORMS College on Artificial Intelligence. He served as a co-chair of the 19th Workshop on Information Technologies and Systems in 2009 and a co-chair of the 5th INFORMS Workshop on Data Mining and Health Informatics in 2010.
