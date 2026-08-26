---
otero_id: 14164
otero_key: "J67AQM9Q"
title: "Optimal keyword auctions for optimal user experiences"
authors: "Jun Li; De Liu; Shulin Liu"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Jun Li <sup>a</sup>, De Liu <sup>b,</sup>⁎, Shulin Liu <sup>a</sup>

<sup>a</sup> School of International Trade and Economics, University of International Business and Economics, Beijing 100029, China <sup>b</sup> Gatton College of Business and Economics, University of Kentucky, Lexington, KY 40506, United States

a r t i c l e i n f o

Available online 8 November 2012

Keywords: Internet advertising Keyword auction Mechanism design User experience

## a b s t r a c t

Poor user experiences with search advertisements can lead to ad avoidance thus reduce search engine's long-term revenue. We capture the effect of negative user experiences on search engine's future revenue in a new variable called “shadow costs” and examine the optimal keyword auction mechanisms (KAMs) in a general model that takes into account advertiser-speci<sup>fi</sup>c and position-speci<sup>fi</sup>c shadow costs. We show that the optima KAMs can be implemented in an ex-post equilibrium with a “progressive second price” payment rule. Furthermore, under a few special but practically relevant cases, the optimal KAM takes the form of relatively simple scoring auctions. We show that minimum bids in these scoring auctions may be advertiser- or position-speci<sup>fi</sup>c and the allocation rule may or may not be greedy. Our results highlight impact of shadow costs on keyword auction designs and hold implications for search engines, advertisers, and internet users.

Published by Elsevier B.V.

## 1. Introduction

Keyword advertising, also known as sponsored search, is a form of advertising that appears on search engine result pages. According to a report commissioned by Interactive Advertising Bureau (IAB 2012) [24], in 2011 keyword advertising generated \$14.8 billion and accounted for 46.5% of the total Internet advertising revenue in the United States. Not surprisingly, given the economic signi<sup>fi</sup>cance of keyword advertising, academics have paid much attention to keyword auctions, a special auction mechanism for allocating keyword advertising slots. To participate in a keyword auction, say for phrase “hotels in Las Vegas”, each advertiser submits a cost-per-click (CPC) bid (e.g., \$1 per click) together with a clickable, text-based advertisement. All bids are collected and ranked, the highest ranked advertisements will automatically appear in the search result page, and advertisers will pay each time when their advertisements get clicked.

It is now well understood that to ensure advertising positions go to advertisers who value them the most, CPC bids should be weighted by click-through rates (CTRs) [4,17,28,30]. This weighting scheme, <sup>fi</sup>rst introduced by Google, promotes more relevant advertisements to top positions and provides strong incentives for advertisers to achieve and maintain high CTRs. However, high CTRs are not synonymous with good user experiences. Sometimes advertisers may pursue high CTRs at the cost of user experience and search engine's long run revenue [6].

Consider an example where an advertiser uses keyword advertisements to sell counterfeit goods. This advertiser may get clicks from many uninformed users, thus enjoy a high CTR; but after users <sup>fi</sup>nding out about the truth, they are likely more to avoid clicking keyword advertisements in the future — thus reducing search engines' long run revenue. In fact, bad user experiences can be caused by many other factors, including poor relevance between landing pages and advertisements, slow loading landing pages, lack of original content,<sup>1</sup> and offensive, fraudulent, or harmful content. Bad user experiences may also be caused by the way advertisements are placed on a page: intrusive or excessive advertisements may result in more clicks but also bad user experiences. Plenty of research has shown that poor user experiences can cause users to avoid advertisements or to develop negative associations toward advertised products [11,37]. Users will learn over time to tune out advertisements or advertising positions when they expect them to be useless, leading to so-called “ad blindness” [13,34].

Previous examples suggest that showing an advertisement may be costly to search engines after all, in the form of future revenue losses due to ad avoidance or “ad blindness.” However, existing research on keyword auction (e.g., [3,15,39]) and optimal keyword auction design (e.g., [18,25,28]) often makes a simplifying assumption that search engines incur zero cost to show an advertisement. To our knowledge, Abrams and Schwarz [1] are the <sup>fi</sup>rst to recognize such “hidden costs.” They argue that because a user's future propensity to click on ads is in<sup>fl</sup>uenced by his experience with past clicks, poor user experience poses a negative externality on the search engine in the form of reducing the future stream of revenue from a user by some amount.

This paper builds on and extends Abrams and Schwarz's work on hidden costs by proposing that search engines may incur a cost for showing an advertisement – in the sense of reduced future revenue stream – both before and after clicking, and the cost may be attributed to advertisers, positions, or both. Different from Abrams and Schwarz [1], we believe that bad user experiences, hence costs, can occur before clicking (e.g., by seeing an offensive ad) and because of advertising positions (e.g., an obstructive position). We collectively call such costs “shadow costs” for they are “shadow of the future” for search engines.<sup>2</sup>

The <sup>fi</sup>rst goal of this paper is to examine how to design optimal (i.e. revenue maximizing) keyword auction mechanisms (KAMs) in the presence of shadow costs. Speci<sup>fi</sup>cally, we are interested in the optimal way of incorporating shadow costs in keyword auction designs. Some efforts are already underway in keyword advertising practice. Search engines have recently incorporated shadow-cost related factors such as relevance and landing page quality in the calculation of “quality scores”, which are essentially a weighting factor for CPC bids.<sup>3</sup> Intuition suggests that this weighting scheme, while appropriate for incorporating CTRs in keyword auctions, may not be optimal for shadow costs. Hence, our <sup>fi</sup>rst goal is to derive the optimal mechanism for keyword advertising in the presence of shadow costs. Our goal is different from Abrams and Schwarz's [1], who focus on developing an efficient Generalized Second Price (GSP) auction [15].

Our second goal is to use shadow costs to explain several phenom enon in keyword auctions that are largely unaccounted for by existing models. First, we hope to explain why search engines sometimes choose not to <sup>fi</sup>ll a position, even when there is a demand for it. Moreover, why positions are sometimes <sup>fi</sup>lled in a non-greedy fashion, e.g., positions on the side of a page are in fact <sup>fi</sup>lled before positions on top of the page. Second, we hope to explain why it makes sense to impose advertiser-speci<sup>fi</sup>c or position-speci<sup>fi</sup>c minimum bids. In absence of shadow costs, as we show in this paper, the optimal minimum bid should be the same across advertisers and positions. But in practice, search engines impose different minimum bids for advertisers and require higher “quality scores” for positions on top of the page.

We note that it is not the goal of this paper to develop strategies for empirically estimating shadow costs, which is obviously an important task. While estimating shadow costs seems challenging, we believe it is still possible. Search engines already have some measures of the quality of advertiser's landing page, such as loading speed and ranking in organic search results. Using content analysis, search engines may also evaluate the relevance of a landing page to advertisements. Search engines can potentially extract user-experience indicators from user behavioral data or user feedback data. For example, one may identify unsatisfactory user experiences by mining the duration and pattern of search sessions. By relating user experience indicators to users' subsequent clicking behavior, search engines can evaluate the long run impact of bad user experiences, thus to infer shadow costs.

Our work consists of two parts. In the <sup>fi</sup>rst part, we characterize the optimal KAM in a general speci<sup>fi</sup>cation where CTRs and shadow costs can depend on both advertisements and positions. We <sup>fi</sup>rstly characterize the optimal KAMs in terms of the probabilities of assigning advertisers to each position and the expected payment by each advertiser. We then obtain a speci<sup>fi</sup>c optimal KAM and show that it is dominant-strategy incentive compatible. In the second part, we look for special cases in which the optimal allocation and payment rules are simple and deterministic. We examine three special cases: (I) without shadow cost, (II) with advertiser-speci<sup>fi</sup>c shadow cost, and (III) with both position-speci<sup>fi</sup>c and advertiserspeci<sup>fi</sup>c shadow costs. We use insights from these special cases to draw practical implications including designing optimal scoring rules and minimum bid policies.

Our research makes the following contributions. First, we add to the literature of keyword advertising by introducing the concept of shadow costs and evaluating its impact on optimal KAMs. We generalize the notion of hidden costs in the literature [1] and characterize the optimal KAMs with a general speci<sup>fi</sup>cation of click-through rates and shadow costs. We show that the optimal KAM can be implemented with a “progressive second price (PSP)” payment rule, one in which advertisers pay progressively higher marginal prices as they move to higher positions. We also show that the optimal KAMs can be implemented in a dominant-strategy equilibrium, i.e., one that does not depend on advertisers' belief about other advertisers' parameters. Second, we demonstrate the practical value of our framework by showing that the optimal KAMs can be implemented with relatively simple scoring auctions in special but relevant cases. By analyzing these scoring auctions, we provide several useful guidelines on optimal scoring rules and minimum bids.

The paper is structured as follows: next we discuss the related literature followed by a description of our model framework. In Section 4 we characterize the optimal KAMs under a general setting. In Section 5 we derive explicit KAMs under three special model speci<sup>fi</sup>cations. Finally, we discuss the implications of our <sup>fi</sup>ndings for search engines, advertisers, and Internet users and suggest a few future research directions.

## 2. Related research

Our research is related to a growing literature on keyword auctions. One stream of research focuses on characterizing the equilibria of keyword auctions. Edelman et al. [15] and Varian [39] independently characterize keyword auction as a generalized second price (GSP) auction, where each winner only needs to pay the minimum price to maintain his current position. They <sup>fi</sup>nd that the GSP auction has no truthtelling equilibrium, yet it is simple and generally generates higher equilibrium revenue than the classic Vickrey–Clarke–Groves (VCG) mechanism. Several papers have subsequently examined other properties of the GSP auction and its relationship with VCG [5,8,14,33]. Another stream of research focuses on the design of keyword auctions in terms of ranking rules [27,28,30,40] and minimum bids [29,38]. Chen et al. [10] treat keyword auctions as auctions of divisible goods and derive revenue-optimizing share structure. Liu and Viswanathan [29] and Dellarocas [12] study the choice of pricing schemes for keyword advertising. Liu and Viswanathan [29] and Zhu and Wilbur [44] examine the phenomenon of “hybrid auctions” in which advertisers are allowed to choose between CPC and CPM (cost per mille impression) bids. Several authors have examined advertising auctions in connection to product market competition [42] and organic listings [26,41]. Unlike previous papers that focus on a particular keyword auction design, we seek the optimal design of KAMs among all candidate mechanisms.

The empirical literature on keyword auctions is also growing. Zhang and Feng [43] document and explain the cyclical bidding patterns in keyword auctions. Animesh et al. [4] <sup>fi</sup>nd that the quality-weighted ranking used by Google can somewhat overcome the adverse selection problem in keyword auctions. Ghose and Yang [19] and Agarwal et al. [2] demonstrate the nontrivial relationship between positions of the advertisement, click-through rates, and advertisers' pro<sup>fi</sup>ts. Ostrovsky and Schwarz [38] <sup>fi</sup>nd in a large-scale <sup>fi</sup>eld experiment that introduction of theory-driven reserve prices can substantially enhance search engine's revenue. Goldfarb and Tucker [20] study how keyword advertising interacts with organic search and of<sup>fl</sup>ine advertising.

To our knowledge, only few papers have considered notions related to shadow costs. Gonen and Vassilvitskii [21] analyze the existence of a symmetric Nash equilibrium under GSP auctions when there is a position-speci<sup>fi</sup>c reserve price. They propose a “bi-ladder” auction for a truthful equilibrium to exist. Abrams and Schwarz [1] introduce an advertiser-speci<sup>fi</sup>c “hidden cost” under a GSP auction. They argue that by subtracting the hidden cost from bid, search engines can encourage advertisers to create user experience and maximize ef<sup>fi</sup>ciency. However, their “hidden costs” are advertiser-speci<sup>fi</sup>c but not position-speci<sup>fi</sup>c. They do not consider mechanisms other than GSP.

Athey and Ellison [6] examine a model that endogenizes search engine users' search costs. They show that with consumer search costs, search engines should optimally use reserve prices and CTR-weighted auctions may not be ef<sup>fi</sup>cient. Search cost can be viewed as a foundation for shadow costs because without search costs, users will always <sup>fi</sup>nd the best website and prior experiences do not matter. A few other papers have also examined search costs and their implications [9,41]. Our paper has signi<sup>fi</sup>cantly different goals from these papers.

Our research follows the theory of mechanism design, pioneered by Hurwicz [23], Myerson [36], and Harris and Raviv [22]. The literature of mechanism design asks how a principal can optimally allocate goods among agents who have private information on the valuation of goods. Myerson's [36] seminal work has laid the foundation for the mechanism design approach. He shows that a standard auction with a minimum bid is optimal for selling a single object under a range of settings. Many advances have since been made in the mechanism design literature, such as optimal mechanism for a multi-product monopolist with unit demand [22] and for homogeneous multi objects [31].

Several authors have applied the mechanism design approach to keyword auctions before us. Iyengar and Kumar [25] provide the <sup>fi</sup>rst analysis of optimal mechanism design in keyword auction settings. They characterize the optimal KAM under a setting where CTRs are both advertiser and position speci<sup>fi</sup>c. Garg and Narahari [18] obtain optimal KAMs under settings when advertisers have identical clickthrough rates and then compare the optimal KAM with GSP and VCG mechanisms. Feng [16] views keyword auctions as a problem of allocating multiple objects for which bidders have a common ranking but nonlinear utility. She shows that the optimal allocation may not be greedy. We also <sup>fi</sup>nd non-greedy optimal allocation in our paper but for entirely different reasons. None of existing mechanism design papers considers shadow costs.

## 3. The model setup

## 3.1. The keyword auction environment

In the keyword auction environment, n risk-neutral advertisers (bidders) compete for k positions at a risk-neutral search engine (auctioneer). Let $i { \in } N { = } \{ 1 , 2 , . . . , n \}$ index advertisers/advertisements and $j { \in } K { = } \{ 1 , 2 , . . . , k \}$ index positions. We follow the convention that a higher position has a smaller index number.

Advertiser i has an expected valuation v per click (valuation for short). We assume that $\nu _ { i }$ is independently drawn from $\left[ \begin{array} { l l } { \underline { { \boldsymbol { \nu } } } , } & { \bar { \boldsymbol { \nu } } } \end{array} \right]$ according to distribution $F _ { i } ( \cdot )$ <sup></sup>which has a strictly positive and continuously differentiable density $f _ { i } ( \cdot )$ . We also assume that the hazard rate of each distribution function, $f _ { i } ( \cdot ) / [ 1 - F _ { i } ( \cdot ) ] ,$ , is non-decreasing.

An advertisement's click-through rate (CTR) may depend on both advertisement and position. We denote α as the CTR of advertiser i at position j. We assume that the higher the position, the higher the $\mathrm { C T R } ^ { 4 }$ i.e.:

$$
\alpha_ {i 1} > \alpha_ {i 2} > \dots > \alpha_ {i k,} \forall i \in N.
$$

The risk-neutral search engine incurs a shadow cost by displaying advertisements. As discussed before, shadow cost is interpreted as the reduction in search engine's long-term revenue when advertisements cause unsatisfactory user experiences. Like click-through rates, shadow costs may depend on both advertisement and position. We denote $c _ { i j }$ as the shadow cost of displaying advertiser i at position j. Shadow costs can be negative, in which case an advertisement positively affects the search engine's long-term pro<sup>fi</sup>ts.

Consistent with the keyword auction practice, we assume that advertisers bid on CPC. Let $b _ { i }$ denote the CPC bid by advertiser i.

Let $\mathbf { v } = ( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n } ) ^ { \mathrm { T } }$ and $\mathbf { b } = ( b _ { 1 } , b _ { 2 } , . . . , b _ { n } ) ^ { \mathrm { T } }$ denote valuations and bids of all advertisers. Let $\mathbf { v } _ { - i }$ and $\mathbf { b } _ { - i }$ denote valuations and bids of all advertisers except i. We denote $\pmb { \alpha } _ { i } = ( \alpha _ { i 1 } , \alpha _ { i 2 } , . . . , \alpha _ { i k } )$ as advertiser i's CTRs at all positions and let $\mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } = ( \mathbf { \alpha } \mathbf { \alpha } \mathbf { \alpha } _ { 1 } , \mathbf { \alpha } \mathbf { \alpha } _ { 2 } , . . . , \mathbf { \alpha } \mathbf { \alpha } ) ^ { \mathrm { T } } .$ c and c are similarly de<sup>fi</sup>ned.

We make the following informational assumptions. The per-click valuation $\nu _ { i }$ is advertiser i's private information but the distribution functions $\{ F _ { i } ( \cdot ) \} _ { i \in N }$ are common knowledge. As in Liu and Chen [28], Iyengar and Kumar [25], and Liu et al. [30], an advertiser's clickthrough rate vector $\pmb { \alpha } _ { i }$ is known by the advertiser i and the search engine, but not by other advertisers. We also assume that only the search engine knows the shadow costs $\mathbf { c } _ { \cdot } ^ { 5 }$ Throughout the paper, we assume that valuations, CTRs, and shadow costs are independent.

## 3.2. The keyword auction mechanism

A keyword auction mechanism (KAM) consists two sets of rules: an allocation rule that determines how positions are allocated among advertisers, and a payment rule that determines how much they must pay. By the revelation principle [35], it is without loss of generality to focus on a set of direct mechanisms, i.e. mechanisms in which agents are simply asked to report their valuations.

## 3.2.1. The allocation rule

The assignment rule speci<sup>fi</sup>es the probabilities of assigning advertisers to positions. Denote $p _ { i j } ( \mathbf { b } | \mathbf { \alpha } \mathbf { \alpha } , \mathbf { c } ) \left( p _ { i j } ( \mathbf { b } ) \right.$ for short) as the probability of assigning advertiser i to position j given bids b, click-through rates α, and shadow costs c. Because an advertiser achieves different CTRs at different positions, the expected number of clicks an advertiser gets is

$$
p _ {i} (\mathbf {b}) = \sum_ {j = 1} ^ {k} \alpha_ {i j} p _ {i j} (\mathbf {b}).\tag{1}
$$

We call $p _ { i } ( \mathbf { b } )$ the total clicks assigned to advertiser i. The allocation rule p is a set of assignment probability functions

$$
\mathbf {p} = \left\{p _ {i j} (\mathbf {b}) \right\}
$$

that satis<sup>fi</sup>es the following feasibility conditions,

$$
\sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {b}) \leq 1, \forall j \in K\tag{2}
$$

$$
\sum_ {j = 1} ^ {k} p _ {i j} (\mathbf {b}) \leq 1, \forall i \in N.\tag{3}
$$

Conditions (2) and (3) require that, at any time, an advertiser can appear in at most one position and a position can be assigned to at most one advertiser.

## 3.2.2. The payment rule

A payment rule speci<sup>fi</sup>es the pay rates for advertisers. Denote $m _ { i j } ( { \bf b } | { \bf \alpha } , { \bf c } ) { \bf \beta } ( m _ { i j } ( { \bf b } )$ for short) as the CPC to be paid by advertiser i at position j, given bids b, CTRs α, and shadow costs c. The payment rule m is a set of pay rate functions:

$$
\mathbf {m} = \left\{m _ {i j} (\mathbf {b}) \right\}.
$$

An advertiser's total payment is the sum of the payments across all positions that she is possibly assigned to. Given the assignment probabilities $p _ { i j } ( \mathbf { b } )$ and pay rate functions $m _ { i j } ( { \bf { b } } )$ , an advertiser i's total payment is given by:

$$
m _ {i} (\mathbf {b}) = \sum_ {j = 1} ^ {k} \alpha_ {i j} p _ {i j} (\mathbf {b}) m _ {i j} (\mathbf {b}).\tag{4}
$$

By the above notations, we denote a KAM as $( \pmb { \mathrm { p } } , \pmb { \mathrm { m } } )$ . Because risk neutral advertisers only care about total clicks and total payment, we can also denote a KAM by $( \{ p _ { i j } ( \mathbf { b } ) \} , \{ m _ { i j } ( \mathbf { b } ) \} )$ .

The timeline of the game is as follows. First, the search engine announces the mechanism (p, m). Next valuations v, shadow costs c, and CTRs α are realized. Each advertiser i learns v and ${ \mathfrak { a } } _ { i } ,$ and the search engine learns c and α. Then, each advertiser i submits a bid b based on the advertiser's valuation v and CTR $\mathbf { \alpha } _ { \mathbf { \alpha } } \mathbf { \alpha } _ { \mathbf { \beta } }$ The search engine allocates the positions to advertisers based on bids b, CTRs $\pmb { \alpha } ,$ and shadow costs c by the allocation rule p and determines the total payment of each advertiser by the payment rule m.

Denote π $( b _ { i } \mid \nu _ { i } )$ as advertiser i's expected payoff if her valuation is $\nu _ { i }$ and she bids $b _ { i \cdot }$ We are interested in KAMs that are individually rational (IR) and incentive compatible (IC), which are de<sup>fi</sup>ned as follows:

De<sup>fi</sup>nition 1. IR: A KAM is individually rational if and only if

$$
\pi_ {i} (v _ {i} | v _ {i}) \geq 0, \forall v _ {i} \in [ \underline {{v}}, \bar {v} ].\tag{5}
$$

De<sup>fi</sup>nition 2. IC: A KAM is incentive compatible if and only if

$$
\pi_ {i} (v _ {i} | v _ {i}) \geq \pi_ {i} (b _ {i} | v _ {i}), \forall b _ {i} \in [ \underline {{v}}, \bar {v} ].\tag{6}
$$

Intuitively, IR requires any participating advertiser to have a nonnegative expected payoff and IC requires that all advertisers <sup>fi</sup>nd it optimal to report their true valuations.

De<sup>fi</sup>nition 3. Candidate mechanism: We call (p, m) a candidate mechanism if it is IR, IC, and satis<sup>fi</sup>es the feasibility constraints (2) and (3).

## 4. The optimal keyword auction mechanism

## 4.1. The candidate KAM

Our <sup>fi</sup>rst result characterizes the necessary and suf<sup>fi</sup>cient condi tions for a candidate mechanism.

Lemma 1. A KAM is a candidate mechanism if and only if the following conditions hold:

$$
\begin{array}{l} \text {(i)} \pi_ {i} (v _ {i} | v _ {i}) = \pi_ {i} (\underline {{v}} | \underline {{v}}) + \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} _ {i} (t) d t, \text {   where   } \bar {p} _ {i} (t) = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ p _ {i} \\ (t, \mathbf {v} _ {- i}) ]. \end{array}
$$

(ii) $\pi _ { i } { \left( \ \underline { { \nu } } \right| } \ \underline { { \nu } } ) { \geq } 0 ,$

(iii) $\bar { p } _ { i } ( t )$ <sup></sup>is non-decreasing in t,

<sup>ð Þ</sup>(iv) Conditions (2) and (3).

Proof. All the proofs are deferred to Appendix A.

In Lemma $1 , \bar { p } _ { i } ( t )$ denotes advertiser i's expected total clicks, taken over all positions and unknown parameters, including valuation, CTRs, and shadow costs of other advertisers. (iii) suggests that expected total clicks must be non-decreasing in the advertiser's valuation. (i) suggests that an advertiser's expected payoff is completed determined by $\pi _ { i } ( \underline { { \boldsymbol { \nu } } } | \underline { { \boldsymbol { \nu } } } )$ and $\bar { p } _ { i } ( t )$ . This important observation leads <sup> </sup>to the following result on the search engine's expected pro<sup>fi</sup>t.

Lemma 2. The search engine's expected profit under a candidate KAM is

$$
\pi_ {0} = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha}} E _ {\mathbf {v}} \left\{\sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} \alpha_ {i j} p _ {i j} (\mathbf {v}) \left[ v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})} - \frac {c _ {i j}}{\alpha_ {i j}} \right] \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}).\tag{7}
$$

The result in Lemma 2 suggests that the expected revenue of the search engine is completely determined by the allocation rule p and $\{ \pi _ { i } ( { \underline { { \nu } } } | { \underline { { \nu } } } ) \}$ . In other words, if two mechanisms result in the same allo-<sup> </sup>cation, they should generate identical expected revenues for the search engine. This result parallels the revenue equivalence theorem for single-object auctions [36]. The intuition for this result can be seen from Lemma 1(i): an advertiser's expected payment is completely determined by the allocation rule p and the expected payoffs of the lowest valuation advertisers, π<sub>i</sub> v v    . Therefore, the expected revenue of <sup> </sup>the search engine, which is the sum of expected payment from advertisers, is also completely determined by p and $\{ \pi _ { i } ( \underline { { \nu } } | \underline { { \nu } } ) \}$

## 4.2. The optimal KAM

Lemma 2 implies that a candidate KAM (p, m) is optimal if $\{ p _ { i j } ( \cdot ) \}$ and $\{ \pi _ { i } ( \underline { { \nu } } | \underline { { \nu } } ) \}$ maximize Eq. (7). To meet the IR condition, we must have π $\scriptstyle \mathbf { \bar { \alpha } } _ { i } ( \ \underline { { \boldsymbol { \nu } } } | \ \underline { { \boldsymbol { \nu } } } ) \geq 0 .$ . Because the choice of $\{ \pi _ { i } ( \underline { { \nu } } | \underline { { \nu } } ) \}$ does not affect the <sup> </sup>optimal choice of $\{ p _ { i j } ( \cdot ) \}$ , we optimally set $\pi _ { i } ( \underline { { \nu } } | \underline { { \nu } } ) = 0$ and choose p <sup></sup>according to the following optimization problem:

$$
\max _ {\mathbf {p}} \pi_ {0} = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha}} E _ {\mathbf {v}} \left\{\sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) \left[ \alpha_ {i j} \left(v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})}\right) - c _ {i j} \right] \right\} s. t. (i i i) a n d s (i v).\tag{OP}
$$

## Corollary 1. Characteristics of the optimal KAM

A candidate KAM $\left( \mathbf { p } , \mathbf { m } \right)$ is an optimal mechanism $i f \pi _ { i } { \big ( } \underline { { \nu } } | \underline { { \nu } } { \big ) } = 0$ and p solves (OP).

We denote

$$
J _ {i} (v _ {i}) = v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})}
$$

as advertiser i's virtual valuation and

$$
w _ {i j} (v _ {i}) = \alpha_ {i j} J _ {i} (v _ {i}) - c _ {i j}
$$

as the net worth of advertiser i at position j to the search engine. By the non-decreasing hazard rate assumption, $J _ { i } ( v _ { i } )$ and $w _ { i j } ( \nu _ { i } )$ are strictly increasing in $\nu _ { i \cdot }$

Corollary 1 implies that the optimal KAM maximizes total expected net worth of all advertisers at their assigned positions. This result is an extension of the optimal mechanism for a single object which maximizes the total expected virtual valuation [36]. In comparison, the net worth extends virtual valuation by incorporating CTRs as a multiplier and shadow costs as a reduction. More important, virtual valuation differs only across advertisers; but net worth differs across both advertisers and positions. These differences hold implications for the optimal mechanisms.

Built on Corollary 1, we now complete the characterization of the optimal KAM by deriving the optimal payment rules.

Theorem 1. If an allocation rule p solves (OP) and a payment rule m satisfies

$$
m _ {i} (b _ {i}, \mathbf {b} _ {- i}) = b _ {i} p _ {i} (b _ {i}, \mathbf {b} _ {- i}) - \int_ {\underline {{v}}} ^ {b _ {i}} p _ {i} (t, \mathbf {b} _ {- i}) d t, \quad \forall \mathbf {b}, \forall i \in N\tag{8}
$$

then (p, m) is an optimal KAM.

## 4.3. Dominant strategy incentive — compatible optimal KAM

Theorem 1 characterizes the optimal mechanisms in a Bayesian environment in terms of expected total clicks and total payments. Such mechanisms are not unique because multiple mechanisms can lead to the same expected revenue for the search engine and expected payoffs for advertisers. Bayesian mechanisms are sometimes criticized for being too weak because if the common knowledge assumption is violated (e.g., when players have different beliefs about valuation distribution), the allocation may be far from optimal. As a remedy, recent work emphasizes ex-post mechanisms, which require the decision of each player to be optimal against the strategies of other players, regardless of their realized types [7]. Ex-post mechanisms are “prior-free”, thus considered more robust for practical use.

In the following, we de<sup>fi</sup>ne a speci<sup>fi</sup>c optimal KAM and show that it is dominant strategy incentive compatible, thus an ex-post mechanism. We maintain that the search engine knows the distribution of valuations but do not require advertisers to have such knowledge.

Lemma 3. The allocation rule p solves (OP) if it solves

$$
\max _ {\mathbf {p}} \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) \left[ \alpha_ {i j} J _ {i} (v _ {i}) - c _ {i j} \right], s. t. (i v), \text { for   any } \mathbf {c}, \boldsymbol {\alpha}, \mathbf {v}.\tag{\( (OP') \}
$$

In the above, the allocation rule p optimizes (OP) point-wise. The allocation is chosen to maximize the total net worth of all advertisers for each given scenario (c, α, v). The above allocation rule is equivalent to an alternative allocation rule p based on reported values:

$$
\max _ {\mathbf {p}} \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {b}) \left[ \alpha_ {i j} J _ {i} (b _ {i}) - c _ {i j} \right], s. t. (i v), \text { for   any } \mathbf {c}, \boldsymbol {\alpha}, \mathbf {b}\tag{9}
$$

provided that advertisers report truthfully (which we will show in the next lemma).

We further denote $\varphi ( i ) \varphi ( i ) { \in } \{ 1 , 2 , . . . , n + k \}$ as the position assigned to advertiser i under the allocation rule (Eq. (9)). We say that an advertiser is assigned if $\varphi ( i ) \leq k$ and unassigned, otherwise.

When advertisers under-report their valuations, they may attain lower positions. We use $\left\{ \begin{array} { l } { \underline { { b } } _ { i j } } \end{array} \right\}$ to denote the minimum bids required <sup></sup>to attain these lower positions. Speci<sup>fi</sup>cally, for any position $j { \ge } \varphi ( i )$ let

$$
\underline {{b}} _ {i j} = \min \{t | \phi (i | (t, \mathbf {b} _ {- i})) \leq j \}
$$

be the minimal bid advertiser i must submit to win position j or higher given other advertisers' bids $\mathbf { b } _ { - i }$ and the allocation rule (Eq. (9)). Note that not all positions are attainable by i (for example, position j may be never assigned to i when the shadow cost $c _ { i j }$ is very large). When position j is unattainable for $i , \underline { { b } } _ { i j }$ is, by de<sup>fi</sup>nition, the same as the minimum bid for the position just above it $\underline { { b } } _ { i , j - 1 } .$ Clearly, by this de<sup>fi</sup>nition, $\underline { { b } } _ { i j }$ is non-decreasing as position j gets higher.

![](/api/attachments/J67AQM9Q/fulltext/images/1c3ed8886b2f04fa96b1588e79ec6cf1ecc9c2f3a1c44ace422155d91c585f2c.jpg)  
Fig. 1. Advertiser i's payment and payoff.

Now we de<sup>fi</sup>ne a payment rule m as follows:

$$
m _ {i} (\mathbf {b} | v _ {i}) = \left\{ \begin{array}{l l} \sum_ {s = \phi (i)} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s}, & \text { if   } i \text {   is   assigned } \\ 0, & \text { otherwise } \end{array} \right.\tag{10}
$$

where $\alpha _ { i , k + 1 } = 0$ . We graphically illustrate this payment rule in Fig. 1. Suppose there are a total of 8 positions and advertiser i is allocated to position 3 under truthful reporting. Intuitively, as advertiser i raises the bid from 0 to $\underline { { b } } _ { i 8 } ,$ i obtains position $8 , ^ { 6 }$ and i's total clicks increase from 0 to $\alpha _ { i 8 } .$ . For the additional clicks $\left( \alpha _ { i 8 } \right)$ ) received, advertiser i pays $\underline { { b } } _ { i 8 }$ per click. As advertiser i raises the bid to $\underline { { b } } _ { i 7 } ,$ i gains additional clicks $( \alpha _ { i 8 } - \alpha _ { i 7 } )$ and pays $\underline { { b } } _ { i 7 }$ for these additional clicks. As i reaches higher and higher positions, i pays progressively higher marginal prices for additional clicks i receives, hence we call this payment rule a progressive second price (PSP) rule.

Assume truthful bidding, the total valuation created by assigning advertiser i to position 3 is represented by area OABCO. The staircase curve (DEF) represents the marginal price paid by advertiser i as a function of i's total clicks. The advertiser pays the area below DEF and retains the area above.

It is easy to see from Fig. 1 that when i bids lower than v but higher than $\underline { { b } } _ { i 3 } ,$ the total payment and payoff remain the same. If i bids lower than $\underline { { b } } _ { i 3 } ,$ then i receives a strictly lower payoff. She is strictly worse off for obtaining position 2, as the additional payment $( \alpha _ { i 2 } - \alpha _ { i 3 } ) \underline { { b } } _ { i 2 }$ exceeds the additional valuation $( \alpha _ { i 2 } - \alpha _ { i 3 } ) \nu _ { i }$ . So every advertiser achieves maximal payoff with truthful bidding, regardless of their beliefs about valuations, CTRs, and shadow costs of other advertisers.

Lemma 4. Given the allocation rule $\left( \operatorname { E q . } \left( 9 \right) \right)$ and payment rule $\left( \operatorname { E q . } ( 1 0 ) \right)$ truthful bidding is a dominant strategy for any advertiser and any bids b , CTRs α and shadow costs c.

Theorem 2. Eqs. (9) and (10) define an optimal KAM that is dominant strategy incentive compatible.

Remark 1. Under the GSP payment rule, advertiser i's total payment would be $\alpha _ { i \phi ( i ) } \ b _ { i \phi ( i ) }$ . So if we <sup>fi</sup>x bids, an advertiser's PSP payment is lower than the GSP payment. This does not imply, however, that GSP generates higher revenue than a PSP mechanism. This is because the GSP payment rule does not induce truthful bidding and advertisers generally bid lower than their true valuations under GSP [15].

Remark 2. Because truthful bidding is a dominant strategy, advertisers' optimal bidding strategies are free of their priors on other advertisers' valuations, CTRs, and shadow costs. The expected revenue achieved by the KAM, however, depends on how accurately the search engine can estimate input parameters including CTRs, shadow costs, and distribution of valuations. More accurate estimates of these parameters can lead to higher realized valuation and higher expected revenue.

## 5. The optimal KAMs under special cases

By studying several special cases, we hope to achieve two goals: deriving an explicit allocation rule that is simple and deterministic and obtaining additional insights about the characteristics of the optimal KAM. There are two reasons to emphasize simplicity. First, as suggested by Milgrom [32], simplicity is highly valued in practical mechanism design. Second, speedy matching of advertisers and positions is crucial in real-time keyword auctions in which matching must be resolved in a fraction of a second. Throughout this section, we assume that

• (symmetric distribution) $J _ { i } ( \cdot ) { = } J ( \cdot )$

• (separable CTRs) $\alpha _ { i j } { = } \alpha _ { i } ^ { a } \alpha _ { j } ^ { p }$ , where $1 = \alpha _ { 1 } ^ { p } { \geq } \alpha _ { 2 } ^ { p } { \geq } \cdots { \geq } \alpha _ { k } ^ { p } { \geq } \alpha _ { k + 1 } ^ { p } =$ $\alpha _ { k + 2 } ^ { p } = \cdots \alpha _ { k + n } ^ { p } = 0$

• (separable shadow cost) $c _ { i j } = c _ { j } ^ { p } + \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a } .$

The <sup>fi</sup>rst assumption states that advertisers' valuations are drawn from the same distribution. This assumption is not essential for deriving explicit optimal allocation rules and payment rules. We make this assumption so that the scoring function is the same for every advertiser. The second assumption, known as the separability assumption of the CTRs [3,15,39], states that CTRs can be separated into an advertiser factor α<sup>a</sup> and a position factor $\alpha _ { j } ^ { p }$ (interpreted as the “prominence” of a position).

The third assumption states that shadow cost is separated into a position-specific (per-impression) component $C _ { \jmath } ^ { p }$ and an advertisementspecific (per-click) component c<sup>a</sup>. The former arises because position attributes such as location on a page, size, or background color affect the before-click user experience (e.g., top of the page positions are more intrusive). The latter arises because post-click user experience can be affected by advertiser-speci<sup>fi</sup>c factors such as the quality of landing page and website (e.g. a link farm or unoriginal content will invoke bad user experience).

The advertisement-speci<sup>fi</sup>c component $c _ { i } ^ { a }$ can in fact capture both before- and post-click bad user experiences imposed by an advertiser. To see, we can introduce an advertiser-speci<sup>fi</sup>c shadow cost component in the form of $\alpha _ { j } ^ { p } c _ { i } ^ { b e f o r e }$ and rede<sup>fi</sup>ne $c _ { i } ^ { \prime } = \frac { c _ { i } ^ { b e f o r e } } { \alpha _ { i } ^ { a } } + c _ { i }$ as the new advertiser-speci<sup>fi</sup>c per-click cost.

## De<sup>fi</sup>nition 4. Scoring mechanism

A KAM is a scoring mechanism if there exists a scoring function s: $N \to R ^ { 7 }$ such that a high-scored advertiser is allocated before a lowscored advertiser: i.e., for any $i , l { \in } N , s ( i ) > s ( l ) \Rightarrow \varphi ( i ) < \varphi ( l )$

## De<sup>fi</sup>nition 5. Greedy allocation

An allocation rule is greedy if it always <sup>fi</sup>lls position j before $j + 1$

The optimal KAM may not be greedy because if the shadow cost for a position is suf<sup>fi</sup>ciently high, it may be left empty while lower positions are <sup>fi</sup>lled (see Example 4). The optimal KAM may not be a scoring mechanism either — the following example shows that the highest position may not be <sup>fi</sup>lled by advertisers with the highest net worth.

Example 1. Suppose there are two positions and two advertisers. If $w _ { 1 1 } = 1 1 , w _ { 1 2 } = 7 , w _ { 2 1 } = 7$ , and $w _ { 2 2 } = 5 ,$ it is optimal to assign advertiser 1 to position 1 and advertiser 2 to position 2 with a total net worth of 16. If $w _ { 1 1 } = 8$ instead, the two advertisers are switched under the optimal allocation with a total net worth of 14.

Next we discuss three different cases based on assumptions about shadow costs

## 5.1. Case I. No shadow costs $( c _ { j } ^ { p } = c _ { i } ^ { a } = 0 )$

This is the case studied by most of the extant literature on keyword auctions. We use this case as a benchmark for our subsequent results. When shadow costs are absent and CTRs are separable, it is straightforward to show that the optimal KAM is a scoring mechanism with greedy allocation.

Theorem 3. Under assumption of no shadow costs, the optimal KAM is a greedy scoring mechanism with scoring function

$$
s ^ {\mathrm{I}} (i) = \alpha_ {i} ^ {a} J (v _ {i}).
$$

Specifically, in the optimal allocation, advertisers with positive s<sup>I</sup> scores are assigned by the descending order of their s<sup>I</sup> scores in a greedy fashion. The minimum bid r for all advertisers and positions is the solution to $J ( r ) { = } 0 $

By Theorem 3, the optimal allocation in this case involves <sup>fi</sup>lling the positions 1 to k in a greedy way by the order of $s ^ { \mathrm { I } }$ scores from high to low, until there are no more positions or no more advertisers with positive s<sup>I</sup> scores.

The necessary and suf<sup>fi</sup>cient condition for an advertiser to have a positive $s ^ { \mathrm { I } }$ score is that the advertiser's valuation must be greater than r. So the optimal KAM entails a same minimum bid (or reserve price) r for all bidders and positions, regardless the number of advertisers. This minimum bid does not depend on advertisers' CTRs either.

Example 2. Advertisers 1, 2, 3, and 4 compete for 3 advertisement positions. Let $F ( x ) = x , x { \in } [ 0 , 1 ]$ , then $J ( x ) = 2 x - 1$ . Moreover, $\nu _ { 1 } = 1 , \nu _ { 2 } =$ $0 . 9 , \nu _ { 3 } = 0 . 8 , \nu _ { 4 } = 0 . 3 , \alpha _ { 1 } ^ { p } = 1 , \alpha _ { 2 } ^ { p } = 0 . 8 , \alpha _ { 3 } ^ { p } = 0 . 2 , \alpha _ { 1 } ^ { a } = 0 . 2 , \alpha _ { 2 } ^ { a } = 0 . 4 , \alpha _ { 3 } ^ { a } = 1$ 0.1, α<sup>a</sup>=0.05. Then $s ^ { \mathrm { I } } ( i ) = \alpha _ { i } ^ { a } J ( \nu _ { i } ) = \alpha _ { i } ^ { a } [ 2 \nu _ { i } - 1 ]$ and the minimum bid is r=0.5. The optimal allocation and payments are calculated as follows. Note that $\underline { { b } } _ { i j }$ is calculated based on the de<sup>fi</sup>nition in Section 4.3. For example, it takes a minimum bid of 0.5, 0.575, and 0.75 for advertiser 2 to get positions 3, 2, and 1 respectively. So advertiser 2's CPC is calculated as $[ 0 . 5 \alpha _ { 3 } ^ { p } + 0 . 5 7 5 ( \alpha _ { 3 } ^ { p } - \alpha _ { 2 } ^ { p } ) + 0 . 7 5 ( \alpha _ { 1 } ^ { p } - \alpha _ { 2 } ^ { p } ) ] \alpha _ { 2 } ^ { a } / ( \alpha _ { 1 } ^ { p } \alpha _ { 2 } ^ { a } ) = 0 . 5 9 5 .$

<table><tr><td>Advertiser</td><td> $v_i$ </td><td> $J(v_i)$ </td><td> $\alpha_i^a$ </td><td> $s^1(i)$ </td><td>Position</td><td> $\underline{b}_{i1}$ </td><td> $\underline{b}_{i2}$ </td><td> $\underline{b}_{i3}$ </td><td>CPC</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0.2</td><td>0.2</td><td>2</td><td>/</td><td>0.65</td><td>0.5</td><td>0.6125</td></tr><tr><td>2</td><td>0.9</td><td>0.8</td><td>0.4</td><td>0.32</td><td>1</td><td>0.75</td><td>0.575</td><td>0.5</td><td>0.595</td></tr><tr><td>3</td><td>0.8</td><td>0.6</td><td>0.1</td><td>0.06</td><td>3</td><td>/</td><td>/</td><td>0.5</td><td>0.5</td></tr><tr><td>4</td><td>0.3</td><td>-0.4</td><td>0.05</td><td>-0.02</td><td>/</td><td>/</td><td>/</td><td>/</td><td>0</td></tr></table>

## 5.2. Case II. Shadow costs are advertiser-specific $( c _ { j } ^ { p } = 0 , c _ { i } ^ { a } > 0 )$

When there is only an advertiser-speci<sup>fi</sup>c cost, the shadow cost takes the form of $c _ { i j } { = } \alpha _ { i } ^ { a } \alpha _ { j } ^ { \bar { p } } c _ { i } ^ { a } .$ This case is most meaningful when the layout and format of advertisement positions are carefully designed to minimize intrusion and negative user experiences mainly come from “bad” advertisements

Theorem 4. Under the assumption $c _ { i j } = \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a } ,$ the optimal KAM is a greedy scoring mechanism with the following scoring function

$$
s ^ {\mathrm{II}} (i) = \alpha_ {i} ^ {a} \left[ J (v _ {i}) - c _ {i} ^ {a} \right].
$$

Specifically, in the optimal allocation, advertisers with positive $s ^ { \mathrm { I I } }$ scores are assigned by the descending order of their $s ^ { \mathrm { I I } }$ scores in a greedy fashion. The implied minimum bid for advertiser i is the solution to

$$
J (r _ {i}) - c _ {i} ^ {a} = 0.
$$

The optimal allocation is similar to that in Section 5.1: <sup>fi</sup>lling the positions 1 to k sequentially by the descending order of $s ^ { \mathrm { I I } }$ scores, until no more positions or no more advertisers with positive $s ^ { \mathrm { I I } }$ scores. The only difference lies in the scoring rule. Like in Section 5.1, the optimal KAM is a scoring mechanism with a greedy allocation rule.

Given the formula for $s ^ { \mathrm { I I } }$ scores, the minimum bid is a function of advertiser-speci<sup>fi</sup>c shadow cost c<sup>a</sup> but is not a function of position or advertisers' CTRs. an advertiser with a higher shadow cost must pay a higher minimum bid to be eligible.

Example 3. Continue with Example 2. Let $c _ { 1 } ^ { a } = 0 . 2 , c _ { 2 } ^ { a } = 0 . 5 , c _ { 3 } ^ { a } = 0 . 7 ,$ $c _ { 4 } ^ { a } = 0 . 3 .$ . Then $s ^ { \mathrm { I I } } ( i ) = \alpha _ { i } ^ { a } ~ [ J ( \nu _ { i } ) - \bar { c } _ { i } ^ { a } ] = \alpha _ { i } ^ { a } [ 2 \nu _ { i } - 1 - c _ { i } ^ { a } ]$ . The minimum bid for advertiser i is calculated as $r = ( 1 + c _ { i } ^ { a } ) / 2$ . The optimal allocation and payments are calculated as follows.

<table><tr><td>Advertiser</td><td> $v_i$ </td><td> $J(v_i)$ </td><td> $\alpha_i^a$ </td><td> $c_i^a$ </td><td> $s^{II}(i)$ </td><td>Position</td><td> $\underline{b}_{i1}$ </td><td> $\underline{b}_{i2}$ </td><td> $\underline{b}_{i3}$ </td><td>CPC</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0.2</td><td>0.2</td><td>0.16</td><td>1</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.66</td></tr><tr><td>2</td><td>0.9</td><td>0.8</td><td>0.4</td><td>0.5</td><td>0.12</td><td>2</td><td>/</td><td>0.75</td><td>0.75</td><td>0.75</td></tr><tr><td>3</td><td>0.8</td><td>0.6</td><td>0.1</td><td>0.7</td><td>-0.01</td><td>/</td><td>/</td><td>/</td><td>/</td><td>0</td></tr><tr><td>4</td><td>0.3</td><td>-0.4</td><td>0.05</td><td>0.3</td><td>-0.035</td><td>/</td><td>/</td><td>/</td><td>/</td><td>0</td></tr></table>

5.3. Case III. Shadow costs are advertisement- and position-specific $( c _ { j } ^ { p } > 0 , c _ { i } ^ { a } > 0 )$

When there are both an advertiser-speci<sup>fi</sup>c per-click cost and a position-speci<sup>fi</sup>c per-impression cost, the shadow cost takes the form of $c _ { i j } = c _ { j } ^ { p } + \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a } .$ This case accommodates the general case in which negative user experiences can come both from intrusive advertisement placement and from irrelevant or offensive content after a user clicks through an advertisement.

Theorem 5. Under the assumption $c _ { i j } = c _ { j } ^ { p } + \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a }$ the optimal KAM is a scoring mechanism with the following scoring function

$$
s ^ {\mathrm{III}} (i) = \alpha_ {i} ^ {a} \left[ J (v _ {i}) - c _ {i} ^ {a} \right].
$$

Advertisers whose $s ^ { \mathrm { I I I } }$ scores exceed $c _ { j } ^ { p } / \alpha _ { j } ^ { p }$ are assigned by the descending order of their $s ^ { \mathrm { I I I } }$ scores and the implied minimum bid for advertiser i at position j is the solution to

$$
\alpha_ {i} ^ {a} \left[ J (r _ {i j}) - c _ {i} ^ {a} \right] = \frac {c _ {j} ^ {p}}{\alpha_ {j} ^ {p}}.
$$

Moreover, $i f$

$$
\frac {c _ {1} ^ {p}}{\alpha_ {1} ^ {p}} \leq \frac {c _ {2} ^ {p}}{\alpha_ {2} ^ {p}} \leq \dots \leq \frac {c _ {k} ^ {p}}{\alpha_ {k} ^ {p}}\tag{11}
$$

then the optimal KAM is a greedy one, $\mathrm { i . e . , }$ advertisers who bid above minimum bids are assigned by the descending order of their $s ^ { \mathrm { I I I } }$ scores in a greedy fashion.

Theorem 5 maintains that advertisers are ranked by the descending order o $\operatorname { f } s ^ { \operatorname { I I I } }$ scores, as in case II. A position is <sup>fi</sup>lled only when there exists an advertiser whose s<sup>III</sup> score exceeds the position's per-click shadow cost. Because of position-speci<sup>fi</sup>c and advertiser-speci<sup>fi</sup>c shadow costs, the minimum bid may differ across advertisers and positions. An advertiser with a high click-through rate $\alpha _ { i } ^ { a }$ and low shadow cost $c _ { i } ^ { a }$ has a low minimum bid, whereas a position with a high shadow cost $c _ { j } ^ { p } / \alpha _ { j } ^ { p }$ requires a high minimum bid.

It should be note that positions may not be <sup>fi</sup>lled in a greedy fashion in this case, as illustrated by Example 4. A high position may be skipped in favor of low positions with lower per-click shadow costs. We show that the optimal allocation is guaranteed to be greedy under condition (11), which maintains that the per-click shadow cost does not decrease with position. That is, on a per-click basis, a lower position causes more harm to user experiences than a higher position. In general, we would expect the opposite to be true because users more likely click on advertisements at high positions by mistake.

Example 4. Continue with Example 3. Let $\frac { c _ { 1 } ^ { p } } { \alpha _ { 1 } ^ { p } } = 0 . 0 2 , \frac { c _ { 2 } ^ { p } } { \alpha _ { 2 } ^ { p } } = 0 . 1 3$ $\frac { c _ { 3 } ^ { p } } { \alpha _ { 3 } ^ { p } } = 0 . 0 4$ . Then $s ^ { \mathrm { I I I } } ( i ) = \alpha _ { i } ^ { a } \left[ J ( \nu _ { i } ) - c _ { i } ^ { a } \right] = \alpha _ { i } ^ { a } [ 2 \nu _ { i } - 1 \stackrel { . } { - } c _ { i } ^ { a } ]$ . The minimum bids for advertiser i at positions 1, 2, 3 are $( 1 + c _ { i } ^ { a } + 0 . 2 / \alpha _ { i } ^ { a } ) / 2$ $( 1 + c _ { i } ^ { a } + 1 . 3 / \alpha _ { i } ^ { a } ) / 2 ,$ , and $( 1 + c _ { i } ^ { a } + 0 . 4 / \alpha _ { i } ^ { a } ) / 2$ , respectively. In this case, position 2 is un<sup>fi</sup>lled due to a high per click shadow cost associated with position 2.

<table><tr><td>Advertiser</td><td> $v_i$ </td><td> $J(v_i)$ </td><td> $\alpha_i^a$ </td><td> $c_i^a$ </td><td> $s^{III}(i)$ </td><td> $s^{III}(i)-c_j^p/\alpha_j^p$ </td><td>Position</td><td> $\underline{b}_{i1}$ </td><td> $\underline{b}_{i2}$ </td><td> $\underline{b}_{i3}$ </td><td>CPC</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0.2</td><td>0.2</td><td>0.16</td><td>0.14</td><td>1</td><td>0.9</td><td>0.9</td><td>0.7</td><td>0.86</td></tr><tr><td>2</td><td>0.9</td><td>0.8</td><td>0.4</td><td>0.5</td><td>0.12</td><td>0.08</td><td>3</td><td>/</td><td>/</td><td>0.8</td><td>0.8</td></tr><tr><td>3</td><td>0.8</td><td>0.6</td><td>0.1</td><td>0.7</td><td>-0.01</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td><td>0</td></tr><tr><td>4</td><td>0.3</td><td>-0.4</td><td>0.05</td><td>0.3</td><td>-0.035</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td><td>0</td></tr></table>

To summarize, all three special cases involve a scoring mechanism, but with different scoring rules and minimum bid policies. In the benchmark case (no shadow costs), the advertisers are ranked by virtual valuation CTR are eligible in the optimal allocation only if their virtual <sup></sup>valuations are positive. This implies a same minimum bid r for all advertisers and positions. In the second case with advertiser-speci<sup>fi</sup>c shadow costs, advertisers are ranked by (virtual valuation – shadow cost) CTR and assigned to positions in a greedy fashion. Advertisers are eligible in the optimal allocation only when their virtual valuations exceed shadow costs. This implies the optimal minimum bids are advertiser speci<sup>fi</sup>c but not position speci<sup>fi</sup>c (Theorem 4). In the third case with advertiser- and position-speci<sup>fi</sup>c shadow costs, advertisers are ranked the same way as the second case but may not be assigned in a greedy fashion — a position with high per-click shadow cost may be skipped in favor of lower positions with low per-click shadow cost. In this case, the net worth of an advertisement must exceed the shadow cost of a position to be eligible in the optimal allocation (Theorem 5). Therefore, the minimum bid is both advertiser-speci<sup>fi</sup>c and position-speci<sup>fi</sup>c. These results highlight the broad impact of shadow costs on the optimal keyword auction design and provide useful guidelines for practical keyword auction designs.

## 6. Discussion and conclusion

Search engines incur shadow costs when an advertisement negatively affects user experiences. We formulate keyword auction design as a mechanism design problem in which a search engine faces advertisers with private valuation per click, and CTRs and shadow costs differ across advertisers as well as positions. Our analysis on the optimal KAMs for the general setting and three special cases yield the following implications.

## 6.1. Implications for minimum bids

In the optimal auction literature, minimum bid exists to exclude bidders who have negative virtual valuation. In previous research on optimal KAMs [18,25], the optimal minimum bid exists purely for revenue considerations<sup>8</sup> and depends only on the distribution of valuations.

Our <sup>fi</sup>ndings for the case I (no shadow cost) are consistent with the previous papers: the optimal minimum bid is independent of advertiser's CTRs and exists only for revenue considerations. But with shadow costs (cases II and III), optimal minimum bids exist not only for revenue considerations but also for social welfare considerations — a socialwelfare maximizing allocation would exclude advertisers whose valuations are less than the shadow costs they create. Thus shadow costs provide a social-welfare justi<sup>fi</sup>cation for the use of minimum bids. More important, the existence of shadow costs explains why minimum bids needs to be advertiser- or position-speci<sup>fi</sup>c.

Our analyses of speci<sup>fi</sup>c cases suggest that minimum bid policies need careful design depending on the nature of shadow costs. When there are no shadow costs, the optimum bids should be the same across advertisers and positions and should be independent of number of bidders. When there are only advertiser-speci<sup>fi</sup>c shadow costs, the minimum bids are advertiser speci<sup>fi</sup>c but not position speci<sup>fi</sup>c. The minimum bids are not directly unrelated to advertisers' CTR. In contrast, when shadow costs have a position-speci<sup>fi</sup>c component, minimum bids are no longer independent of CTRs: advertisers who have high CTRs should have a smaller minimum bid. In this case, minimum bids are also position speci<sup>fi</sup>c. This <sup>fi</sup>nding provides theoretical guidelines on when minimum bids need to be position speci<sup>fi</sup>c and when it should depend on advertisers' CTRs.

## 6.2. Implications for the number of positions to fill

From the perspective of optimal KAMs, some positions may be optimally left un<sup>fi</sup>lled because no remaining advertisers can generate a positive net worth at these positions. When shadow costs consist of only an advertiser-speci<sup>fi</sup>c component, this usually means high positions are <sup>fi</sup>lled before low positions— i.e., a greedy allocation. However, when shadow cost consists of a position-speci<sup>fi</sup>c component, high positions may be left un<sup>fi</sup>lled. This <sup>fi</sup>nding provides theoretical justi<sup>fi</sup>cations for the observation that search engines sometimes show no on top of the search results but only on the right side. According to case III, this is because the positions on top have high shadow costs such that no advertiser has a virtual valuation exceeding the positionspeci<sup>fi</sup>c shadow costs. But advertisement may still show up the right side because the shadow costs for right side positions are lower. Our result resonates with the empirical observation by Goldfarb and Tucker [20] that it may be undesirable to advertise on the most intrusive positions in targeted Internet advertising.

## 6.3. Implications on how to incorporate shadow costs

At the beginning of the paper, we argue that user experience factors should be incorporated in keyword auctions. But how? Our results show that shadow costs enter the keyword auction through two main ways: scoring rules and minimum bids. Results in Case II suggest that the advertiser-speci<sup>fi</sup>c shadow cost should be incorporated in both the scoring rule and minimum bids. Speci<sup>fi</sup>cally, we need to subtract the advertiser-speci<sup>fi</sup>c shadow cost from the advertiser's scores and increase the minimum bid to compensate for the shadow cost imposed by the advertiser. In contrast, the position-speci<sup>fi</sup>c component only impact minimum bid policies — minimum bids should differ across positions to re<sup>fl</sup>ect the different shadow costs associated with each position.

It is also important to point out that shadow costs play a very different role in scoring rules and minimum bid policies than CTRs. Shadow costs should not enter scoring rules as a weighting factor as CTR does. Instead, (advertiser-speci<sup>fi</sup>c) shadow costs should be subtracted from advertisers' scores. Our proposed optimal mechanism differs from the prevailing model where factors related to shadow costs and CTRs are stuffed into a single weighting factor known as “quality score”. Furthermore, as we show through the three special cases, shadow costs, not CTRs, are the main reason for using advertiser- and position-speci<sup>fi</sup>c minimum bids.

6.4. Implications for search engines, advertisers, and consumers

Because our proposed mechanism penalizes advertisers with high shadow costs (and reward ones with negative shadow costs), advertisers have incentives to improve overall user experiences in the long run. For example, they can align advertisement better with the content of landing pages and optimize their sites for better user experience. Internet users are bene<sup>fi</sup>ciaries of our optimal keyword auction designs. In the short run, users are shielded from intrusive and excessive advertising and from “bad” advertisers. In the long run, because of advertisers' effort in improving customer experience, users will <sup>fi</sup>nd these advertisements more helpful. Search engines may suffer some short term revenue loss because of the exclusion of paying advertisers but they will bene<sup>fi</sup>t in the long run from improved user experiences.

## 6.5. Limitations and future research

To navigate the complexity of introducing shadow costs, we have made simplifying assumptions. For example, we assumed the risk neutrality of advertisers and the search engine and the independence between valuations, CTRs, and shadow costs. In the analysis of special cases, we make additional assumptions such as separable CTRs. While empirical evidence refutes the separablility assumption, our interaction with keyword advertising professionals suggests that the discrepancy may be tolerable in pursuit of theoretical results.

Additional research is needed to gain further insights on shadow costs. It is desirable to examine shadow costs from the social welfare point of view by incorporating users. Another potentially interesting extension is to examine how shadow costs interact with payment schemes, including CPC, CPM (cost-per mille-impressions), and cost-per-sale [29]. Our research also raises many interesting empirical questions. For example, how large are the shadow costs? How costly is it for search engines to ignore shadow costs? Finally, future research should examine shadow costs in other advertising formats and platforms, including display and mobile advertising.

As keyword advertising thrives in online and mobile environments, advertisers have learned to pro<sup>fi</sup>t from boosting CTRs sometimes at the cost of user experiences. It is therefore important to incorporate shadow costs into the next generation of keyword auction designs. We hope our analyses highlight the distinct issues created by shadow costs and bridge the gap between keyword auction theory and practice.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China under Grant No. 71171052.

## Appendix A

Proof of Lemma 1. Since advertiser i only knows i's valuation and CTRs, her expected payoff is

$$
\begin{array}{r l} & {\pi_ {i} (b _ {i} | v _ {i}) = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ v _ {i} p _ {i} (b _ {i}, \mathbf {v} _ {- i}) - m _ {i} (b _ {i}, \mathbf {v} _ {- i}) ]} \\ & {\qquad = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ b _ {i} p _ {i} (b _ {i}, \mathbf {v} _ {- i}) - m _ {i} (b _ {i}, \mathbf {v} _ {- i}) + (v _ {i} - b _ {i}) p _ {i} (b _ {i}, \mathbf {v} _ {- i}) ]} \\ & {\qquad = \pi_ {i} (b _ {i} | b _ {i}) + (v _ {i} - b _ {i}) \bar {p} _ {i} (b _ {i})} \end{array}\tag{A.1}
$$

where $\bar { p } _ { i } ( b _ { i } ) = E _ { \mathbf { c } } E _ { \mathbf { \alpha } _ { \mathbf { \alpha } _ { - i } } } E _ { \mathbf { v } _ { - i } } [ p _ { i } ( b _ { i } , \mathbf { v } _ { - i } ) ] .$

(if part) Suppose conditions (i)–(iv) hold, we show the mechanism is candidate one. Of course, the condition (iv) implies conditions (2) and (3) in the de<sup>fi</sup>nition of candidate KAM. By conditions (i) and (ii), we have

$$
\pi_ {i} (v _ {i} | v _ {i}) = \pi_ {i} (\underline {{v}} | \underline {{v}}) + \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} _ {i} (t) d t \geq \pi_ {i} (\underline {{v}} | \underline {{v}}) \geq 0
$$

So the individual rationality condition (5) is met. From Eq. (A.1), conditions (i) and (iii),

$$
\begin{array}{l} \pi_ {i} (v _ {i} | v _ {i}) - \pi_ {i} (b _ {i} | v _ {i}) = \pi_ {i} (v _ {i} | v _ {i}) - \pi_ {i} (b _ {i} | b _ {i}) - (v _ {i} - b _ {i}) \bar {p} _ {i} (b _ {i}) \\ \qquad = \int_ {b _ {i}} ^ {v _ {i}} \bar {p} _ {i} (t) d t - (v _ {i} - b _ {i}) \bar {p} _ {i} (b _ {i}) = \int_ {b _ {i}} ^ {v _ {i}} [ \bar {p} _ {i} (t) - \bar {p} _ {i} (b _ {i}) ] d t \geq 0 \end{array}
$$

where the <sup>fi</sup>rst equality is due to Eq. (A.1), the second is due to condition (i), and the inequality is due to condition (iii). Thus the incentive compatibility condition (6) is met. We conclude that the mechanism that meets conditions (i)–(iv) is feasible.

(only if part) Suppose a KAM is candidate one: we now show that it must satisfy conditions $( i ) - ( i v )$ . Obviously, when the individual rationality condition (5) and allocation constraints (2) and (3) hold, the conditions (ii) and (iv) must also hold.

Applying the incentive compatibility condition (6) and equality $\operatorname { E q . } \left( \mathrm { A . 1 } \right)$ , we have

$$
\begin{array}{l} \pi_ {i} (v _ {i} | v _ {i}) \geq \pi_ {i} (b _ {i} | v _ {i}) = \pi_ {i} (b _ {i} | b _ {i}) + (v _ {i} - b _ {i}) \bar {p} _ {i} (b _ {i}) \\ \text { i.e., } \\ \pi_ {i} (v _ {i} | v _ {i}) - \pi_ {i} (b _ {i} | b _ {i}) \geq (v _ {i} - b _ {i}) \bar {p} _ {i} (b _ {i}). \end{array}
$$

Similarly, by an exchange of $b _ { i }$ and $\nu _ { i } , \pi _ { i } ( b _ { i } | b _ { i } ) { - } \pi _ { i } ( \nu _ { i } | \nu _ { i } ) { \geq } ( b _ { i } { - } \nu _ { i } )$ $\bar { p } _ { i } ( \nu _ { i } )$ , i.e.,

$$
\pi_ {i} (v _ {i} | v _ {i}) - \pi_ {i} (b _ {i} | b _ {i}) \leq (v _ {i} - b _ {i}) \bar {p} _ {i} (v _ {i}).
$$

Therefore, $( \nu _ { i } - b _ { i } ) \bar { p } _ { i } ( b _ { i } ) { \le } \pi _ { i } ( \nu _ { i } | \nu _ { i } ) { - } \pi _ { i } ( b _ { i } | b _ { i } ) { \le } ( \nu _ { i } - b _ { i } ) \bar { p } _ { i } ( \nu _ { i } )$ . Hence the condition (iii) must hold. Furthermore, $\pi _ { i } ( \nu _ { i } | \nu _ { i } )$ is non-decreasing and continuous, thus $\pi _ { i } ( \nu _ { i } | \nu _ { i } )$ is absolutely continuous and $\frac { d \pi _ { i } ( \nu _ { i } | \nu _ { i } ) } { d \nu _ { i } } =$ $\bar { p } _ { i } ( \nu _ { i } )$ ; a:e: We conclude that condition (i) also holds. □

Proof of Lemma 2. When advertiser i bids truthfully, her expected payment is

$$
\begin{array}{l} \bar {m} _ {i} (v _ {i}) = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ m _ {i} (v _ {i}, \mathbf {v} _ {- i}) ] = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ v _ {i} p _ {i} (v _ {i}, \mathbf {v} _ {- i}) ] - \pi_ {i} (v _ {i} | v _ {i}) \\ \qquad = v _ {i} \bar {p} _ {i} (v _ {i}) - \pi_ {i} (v _ {i} | v _ {i}) = v _ {i} \bar {p} _ {i} (v _ {i}) - \pi_ {i} (\underline {{v}} | \underline {{v}}) - \int_ {v} ^ {v _ {i}} \bar {p} _ {i} (t) d t. \end{array}
$$

Then we have

$$
\begin{array}{l} R = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} E _ {v _ {i}} [ \bar {m} _ {i} (v _ {i}) ] \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} \left[ v _ {i} \bar {p} _ {i} (v _ {i}) - \pi_ {i} (\underline {{v}} | \underline {{v}}) - \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} _ {i} (t) d t \right] f _ {i} (v _ {i}) d v _ {i} \right\} \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} v _ {i} \bar {p} _ {i} (v _ {i}) f _ {i} (v _ {i}) d v _ {i} - \int_ {\underline {{v}}} ^ {\overline {{v}}} \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} _ {i} (t) d t f _ {i} (v _ {i}) d v _ {i} \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}) \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} v _ {i} \bar {p} _ {i} (v _ {i}) f _ {i} (v _ {i}) d v _ {i} - \int_ {\underline {{v}}} ^ {\overline {{v}}} [ 1 - F _ {i} (v _ {i}) ] \bar {p} _ {i} (v _ {i}) d v _ {i} \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}) \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} \left[ v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})} \right] \bar {p} _ {i} (v _ {i}) f _ {i} (v _ {i}) d v _ {i} \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}) \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} \left[ v _ { i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})} \right] E _ {\mathbf c} E _ {\alpha_ {- i}} E _ {\mathbf v _ {- i}} [ p _ {i} (v _ {i}, \mathbf v _ {- i}) ] f _ {i} (v _ {i}) d v _ {i} \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}) \\ = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} \left\{\int_ {\underline {{v}}} ^ {\overline {{v}}} \left[ v _ {\mathrm{i}} - \frac {1 - F _ {\mathrm{i}} (v _ {\mathrm{i}})}{f _ {\mathrm{i}} (v _ {\mathrm{i}})} \right] E _ {\mathbf c} E _ {\alpha_ {- i}} E _ {\mathbf v _ {- i}} \left[ \sum_ {\mathrm{j=1}} ^ {\mathrm{k}} \alpha_ {\mathrm{ij}} p _ {\mathrm{ij}} (\mathbf v) \right] f _ {\mathrm{i}} (v _ {\mathrm{i}}) d v _ {\mathrm{i}} \right\} - \sum_ {\mathrm{i=1}} ^ {\mathrm{n}} \pi_ {\mathrm{i}} (\underline {{v}} | \underline {{v}}) \\ = E _ {\mathbf c} E _ {\alpha} E _ {\mathbf v} \left\{\sum_ {\mathrm{j=1}} ^ {\mathrm{k}} \sum_ {\mathrm{i=1}} ^ {\mathrm{n}} \alpha_ {\mathrm{ij}} p _ {\mathrm{ij}} (\mathbf v) \left[ v _ {\mathrm{i}} - \frac {1 - F _ {\mathrm{i}} (v _ {\mathrm{i}})}{f _ {\mathrm{i}} (v _ {\mathrm{i}})} \right] \right\} - \sum_ {\mathrm{i=1}} ^ {\mathrm{n}} \pi_ {\mathrm{i}} (\underline {{v}} | \underline {{v}}). \end{array}
$$

where the fourth equality is an application of integration by parts, and the seventh equality is due to Eq. (1).

Because the search engine chooses the mechanism that maximizes expected pro<sup>fi</sup>t under all possible realizations of v, c, and α. For any given realization, when all advertisers report their true valuations, the search engine's total revenue is $\sum _ { i = 1 } ^ { n } m _ { i } ( \pmb { \mathbf { v } } )$ and total shadow cost is $\sum _ { j = 1 } ^ { k } \sum _ { i = 1 } ^ { n } p _ { i j } ( \pmb { \mathsf { v } } ) c _ { i j } .$ . So for all possible realizations the search engine's total expected revenue is $R = E _ { \mathbf { c } } E _ { \mathbf { \alpha } } E _ { \mathbf { v } } \left[ \sum _ { i = 1 } ^ { n } m _ { i } ( \mathbf { v } ) \right] = \sum _ { i = 1 } ^ { n } E _ { \nu _ { i } } E _ { \mathbf { \alpha } _ { i } } [ \bar { m } _ { i } ( \nu _ { i } ) ]$ and the total expected shadow cost is $C = E _ { \mathbf { c } } E _ { \mathbf { \boldsymbol { \alpha } } } E _ { \mathbf { \boldsymbol { \nu } } } \left[ \sum _ { j = 1 } ^ { k } \sum _ { i = 1 } ^ { n } p _ { i j } ( \mathbf { \boldsymbol { \mathbf { v } } } ) c _ { i j } \right]$ The search engine's total expected pro<sup>fi</sup>t is the total expected revenue minus the total expected shadow cost, i.e.,

$$
\begin{array}{l} \pi_ {0} = R - C = \sum_ {i = 1} ^ {n} E _ {\alpha_ {i}} E _ {v _ {i}} [ \bar {m} _ {i} (v _ {i}) ] - E _ {\mathbf {c}} E _ {\alpha} E _ {\mathbf {v}} \left[ \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) c _ {i j} \right] \\ = E _ {\mathbf {c}} E _ {\alpha} E _ {\mathbf {v}} \left\{\sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} \alpha_ {i j} p _ {i j} (\mathbf {v}) \left[ v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})} \right] \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}) \\ - E _ {\mathbf {c}} E _ {\alpha} E _ {\mathbf {v}} \left[ \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) c _ {i j} \right] \\ = E _ {\mathbf {c}} E _ {\alpha} E _ {\mathbf {v}} \left\{\left. \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} \alpha_ {i j} p _ {i j} (\mathbf {v}) \left[ v _ {i} - \frac {1 - F _ {i} (v _ {i})}{f _ {i} (v _ {i})} - \frac {c _ {i j}}{\alpha_ {i j}} \right] \right\} - \sum_ {i = 1} ^ {n} \pi_ {i} (\underline {{v}} | \underline {{v}}). \right. \end{array}
$$

Proof of Corollary 1. Omitted

Proof of Theorem 1. Denote $\bar { m } _ { i } ( b _ { i } ) = E _ { { \bf c } } E _ { { \bf \alpha } _ { - i } } E _ { { \bf v } _ { - i } } [ m _ { i } ( b _ { i } , { \bf v } _ { - i } ) ]$ be advertiser i's expected payment when her bid is $b _ { i }$

First we will show that bidding truthfully is a Bayesian Nash equilibrium. In fact, if all advertisers but i bid their true values $( \mathrm { i . e . , } \mathbf { b } _ { - i } \mathrm { = } \mathbf { v } _ { - i } )$ by (8), advertiser i's expected payment is $\bar { m } _ { i } ( b _ { i } ) = b _ { i } \bar { p } _ { i } ( b _ { i } ) - \int _ { \nu } ^ { b _ { i } } \bar { p } ( t ) d t$ Moreover, we have

$$
\begin{array}{l} \pi_ {i} (v _ {i} | v _ {i}) = E _ {\mathbf {c}} E _ {\boldsymbol {\alpha} _ {- i}} E _ {\mathbf {v} _ {- i}} [ v _ {i} p _ {i} (v _ {i}, \mathbf {v} _ {- i}) - m _ {i} (v _ {i}, \mathbf {v} _ {- i}) ] \\ = v _ {i} \bar {p} (v _ {i}) - \bar {m} _ {i} (v _ {i}) \\ = v _ {i} \bar {p} (v _ {i}) - \left[ v _ {i} \bar {p} _ {i} (v _ {i}) - \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} (t) d t \right] \\ = \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} (t) d t. \end{array}
$$

Then, advertiser i's expected payoff is

$$
\begin{array}{l} \pi_ {i} (b _ {i} | v _ {i}) = v _ {i} \bar {p} _ {i} (b _ {i}) - \bar {m} _ {i} (b _ {i}) \\ \qquad = v _ {i} \bar {p} (b _ {i}) - \left[ b _ {i} \bar {p} (b _ {i}) - \int_ {\underline {{v}}} ^ {b _ {i}} \bar {p} d t \right] \\ \qquad = (v _ {i} - b _ {i}) \bar {p} (b _ {i}) + \int_ {\underline {{v}}} ^ {b _ {i}} \bar {p} (t) d t \\ \qquad = \int_ {b _ {i}} ^ {v _ {i}} \bar {p} (b _ {i}) d t + \int_ {\underline {{v}}} ^ {b _ {i}} \bar {p} (t) d t \\ \qquad = \int_ {\underline {{v}}} ^ {v _ {i}} \bar {p} (t) d t + \int_ {b _ {i}} ^ {v _ {i}} [ \bar {p} (b _ {i}) - \bar {p} (t) ] d t \\ \qquad \leq \int_ {\underline {{v}}} ^ {\underline {{v}} _ {i}} \bar {p} (t) d t = \pi_ {i} (v _ {i} | v _ {i}) \end{array}
$$

and the equality holds if and only if $b _ { i } = v _ { i }$ by condition (iii). Therefore, advertiser i will bid i's true value v and i's expected payment is $\bar { m } _ { i } ( \nu _ { i } ) = \nu _ { i } \bar { p } ( \nu _ { i } ) - \int _ { \nu } ^ { \nu _ { i } } \bar { p } ( t ) d t$ . Since $\pi _ { i } ( \nu _ { i } | \nu _ { i } ) = \nu _ { i } \bar { p } ( \nu _ { i } ) { - } \bar { m } _ { i } ( \nu _ { i } ) = \int _ { \nu } ^ { \nu _ { i } }$ p t dt at the truthful equilibrium, thus $\pi _ { i } ( { \bf \nabla } \nu | { \bf \nabla } \nu ) = 0$ and $\pi _ { i } ( \nu _ { i } | \nu _ { i } ) = \pi _ { i } { \bigl ( } \underline { { \nu } } | \underline { { \nu } } { \bigr ) } -$ 十 $\int _ { \frac { \nu } { 2 } } ^ { \nu _ { i } } \bar { p } ( t ) d t$ . Therefore, this KAM meets the conditions (i) and (ii) in <sup></sup>Lemma 1. Because this KAM also satis<sup>fi</sup>es conditions (iii) and (iv) in Lemma 1 since p solves (OP), it is a candidate KAM. Finally, this KAM satis<sup>fi</sup>es the conditions of Corollary 1, so it is an optimal KAM. □

Proof of Lemma 3. We will show p satis<sup>fi</sup>es condition (iii) and thus p solves (OP). Consider valuation vectors $\mathbf { v } = ( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n } ) ^ { \mathrm { T } }$ and ${ \bf { v } } ^ { \prime } =$ $( \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { i - 1 } , \nu _ { i } + \varepsilon , . . . , \nu _ { n } ) ^ { \mathrm { T } }$ , for any ε>0. Let ${ \bf P } = \{ p _ { i j } ( { \bf v } ) \}$ and ${ \bf P } ^ { \prime } = \{ p _ { i j } ( { \bf v } ^ { \prime } ) \}$ be optimal allocation under v and v′ respectively. Let $w _ { i } ( { \pmb v } , { \pmb P } ) = \sum _ { j = 1 } ^ { k } p _ { i j } ( { \pmb v } ) \big [ \alpha _ { i j } J _ { i } ( \nu _ { i } ) - c _ { i j } \big ]$ is the total net worth of advertiser i and $w _ { - i } ( \pmb { \mathsf { v } } , \pmb { \mathsf { P } } ) = \sum _ { k \neq i } ^ { n } w _ { k } ( \pmb { \mathsf { v } } , \pmb { \mathsf { P } } )$ represent the total net worth of advertisers other than $i . \mathrm { ~ } w _ { i } (  { \mathbf { v } } ,  { \mathbf { P } } ^ { \prime } )$ and $w _ { - i } ( { \bf v } , { \bf P } ^ { \prime } )$ are similar for allocation P′. Since P and P′ are optimal under v and v′ respectively, we have

$$
\begin{array}{l} w _ {- i} (\mathbf {v}, \mathbf {P}) + w _ {i} (\mathbf {v}, \mathbf {P}) \geq w _ {- i} (\mathbf {v}, \mathbf {P} ^ {\prime}) + w _ {i} (\mathbf {v}, \mathbf {P} ^ {\prime}) \\ w _ {- i} (\mathbf {v} ^ {\prime}, \mathbf {P} ^ {\prime}) + w _ {i} (\mathbf {v} ^ {\prime}, \mathbf {P} ^ {\prime}) \geq w _ {- i} (\mathbf {v} ^ {\prime}, \mathbf {P}) + w _ {i} (\mathbf {v} ^ {\prime}, \mathbf {P}). \end{array}
$$

Noticing that if we hold the allocation constant, the total net worth of advertisers other than i is the same under v and v′, i.e., $w _ { - i } ( { \bf u } , { \bf P } ) =$ $w _ { - i } ( \pmb { \nu } ^ { \prime } , \pmb { \mathrm { \pmb { P } } } )$ andw ${ \bf \nabla } _ { - i } ( { \bf v } , { \bf P } ^ { \prime } ) = w _ { - i } ( { \bf v } ^ { \prime } , { \bf P } ^ { \prime } )$ <sup>ð Þ ¼</sup>. So we combine the two inequalities as

$$
w _ {i} (\mathbf {v}, \mathbf {P}) + w _ {i} (\mathbf {v} ^ {\prime}, \mathbf {P} ^ {\prime}) \geq w _ {i} (\mathbf {v} ^ {\prime}, \mathbf {P}) + w _ {i} (\mathbf {v}, \mathbf {P} ^ {\prime})
$$

Substituting w $\mathbf { \bar { v } } , \mathbf { P } ) - w _ { i } ( \mathbf { v } ^ { \prime } , \mathbf { P } ^ { \prime } ) = [ J _ { i } ( { \nu } _ { i } ) - J _ { i } ( { \nu } _ { i } + \varepsilon ) ] p _ { i } ( \mathbf { v } )$ and w<sub>i</sub>(v, $\mathbf { P } ^ { \prime } ) - w _ { i } ( \mathbf { v } ^ { \prime } , \mathbf { P } ^ { \prime } ) = \left[ J _ { i } ( \nu _ { i } ) - J _ { i } ( \nu _ { i } + \varepsilon ) \right] p _ { i } ( \mathbf { v } ^ { \prime } )$ , we have

$$
\left[ J _ {i} \left(v _ {i}\right) - J _ {i} \left(v _ {i} + \varepsilon\right) \right] p _ {i} (\mathbf {v}) \geq \left[ J _ {i} \left(v _ {i}\right) - J _ {i} \left(v _ {i} + \varepsilon\right) \right] p _ {i} \left(\mathbf {v} ^ {\prime}\right).
$$

Since $J _ { i } ( \nu _ { i } ) { < } J _ { i } ( \nu _ { i } + \varepsilon )$ , we must have $p _ { i } ( \mathbf { v } ) { \leq } p _ { i } ( \mathbf { v } ^ { \prime } )$ , which implies <sup>ð Þ</sup>that p satis<sup>fi</sup>es (iii). Moreover, p satis<sup>fi</sup>es (iv) by the de<sup>fi</sup>nition of $( \mathrm { O P ^ { \prime } } ) .$ So p solves (OP). □

Proof of Lemma 4. Denote $h _ { i } ( b _ { i } | { \bf b } _ { - i } , { \bf c } , { \bf \alpha \alpha } )$ as advertiser i's net payoff under bids b , shadow costs c, and CTRs α. By the de<sup>fi</sup>nition of dominant strategy incentive-compatible equilibrium [7], it is suf<sup>fi</sup>cient to show that $h _ { i } ( \nu _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha } ) \geq h _ { i } ( b _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha } )$ for any bid vector b .

$\mathrm { I f } \nu _ { i } \le b _ { i k } , h _ { i } ( \nu _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha } ) = 0$ and we can easily show that $h _ { i } ( \nu _ { i } | \mathbf { b } _ { - i } , \mathbf { c } _ { i }$ $\pmb { \alpha } ) \geq h _ { i } ( b _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \pmb { \alpha } )$ . In fact, if $b _ { i } < b _ { i k }$ then the bidder remains unassigned and gets a zero payoff. I $\dot { \boldsymbol { b } } _ { i } > b _ { i k } ,$ then the bidder is assigned but earns a negative net payoff, because the marginal price is at least $\underline { { b } } _ { i k }$

I $\mathrm { f } \ v _ { i } > b _ { i k } ,$ and the bidder will get position l if she bids truthfully, we can show $h _ { i } ( \nu _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha } ) \geq h _ { i } ( b _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha } )$ as follows. If $\underline { { b } } _ { i , l - 1 } > b _ { i } \geq \underline { { b } } _ { i l } ,$ then she gets the same position l, and $h _ { i } ( \nu _ { i } | \mathbf { b } _ { - i } , \mathbf { c } , \mathbf { \alpha \alpha \alpha } ) = h _ { i } ( b _ { i } | \mathbf { b } _ { - i } , \mathbf { \alpha \mathbf { c } }$ α). I $\lceil b _ { i } > \underline { { b } } _ { i l - 1 }$ , and she gets a higher position m $( m < l ) ,$ , then

$$
\begin{array}{l} h _ {i} (b _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) = v _ {i} \alpha_ {i m} - \sum_ {s = m} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \\ = v _ {i} \alpha_ {i l} + (v _ {i} \alpha_ {i m} - v _ {i} \alpha_ {i l}) - \sum_ {s = m} ^ {s = l - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \\ - \sum_ {s = l} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} = \left[ v _ {i} \alpha_ {i l} - \sum_ {s = l} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \right] \\ + \left[ (v _ {i} \alpha_ {i m} - v _ {i} \alpha_ {i l}) - \sum_ {s = m} ^ {s = l - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \right] \\ = h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) + \left[ \sum_ {s = m} ^ {l - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) v _ {i} - \sum_ {s = m} ^ {s = l - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \right] \\ = h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) + \sum_ {s = m} ^ {l - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) (v _ {i} - \underline {{b}} _ {i s}) <   h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) \end{array}
$$

where the inequality holds because $b _ { i s } \ge v _ { i }$ for $s { < } l .$

If b b $: b _ { i l }$ then she gets a lower position m (m>l) then

$$
\begin{array}{l} h _ {i} (b _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) = v _ {i} \alpha_ {i m} - \sum_ {s = m} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} = v _ {i} \alpha_ {i l} - (v _ {i} \alpha_ {i l} - v _ {i} \alpha_ {i m}) \\ \quad + \sum_ {s = l} ^ {s = m - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} - \sum_ {s = l} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \\ = \left[ v _ {i} \alpha_ {i l} - \sum_ {s = l} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \right] \\ \quad + \left[ \sum_ {s = l} ^ {s = m - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} - (\alpha_ {i l} - \alpha_ {i m}) v _ {i} \right] \\ = h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) \\ \quad + \left[ \sum_ {s = l} ^ {s = m - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} - \sum_ {s = l} ^ {s = m - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) v _ {i} \right] \\ = h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) + \sum_ {s = l} ^ {s = m - 1} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) (b _ {i s} - v _ {i}) \\ <   h _ {i} (v _ {i} | \mathbf {b} _ {- i}, \mathbf {c}, \boldsymbol {\alpha}) \end{array}
$$

where the inequality holds because $\underline { { b } } _ { i s } < \nu _ { i }$ for $s { > } l .$

Proof of Theorem 2. By Lemma 4, the KAM de<sup>fi</sup>ned by Eqs. (9) and (10) is dominant strategy incentive compatible. Next we will show this KAM is optimal by showing the allocation and payment rules satisfy conditions in Theorem 1.

Firstly, under truthful bidding, Eq. (9) is the same as (OP′), thus, by Lemma 3, the allocation rule de<sup>fi</sup>ned by Eq. (9) solves (OP).

Secondly, by Theorem 1, under truthful bidding, the total payment from advertiser i is,

$$
\begin{array}{c} m _ {i} (\mathbf {v}) = v _ {i} p _ {i} (v _ {i}, \mathbf {v} _ {- i}) - \int_ {\underline {{v}}} ^ {v _ {i}} p _ {i} (t, \mathbf {v} _ {- i}) d t \\ = v _ {i} \alpha_ {i, \phi (i)} - \int_ {\underline {{v}}} ^ {v _ {i}} p _ {i} (t, \mathbf {v} _ {- i}) d t. \end{array}
$$

If the advertiser is unassigned, the above is zero, which coincides with Eq. (10). Suppose the advertiser is assigned. Recall that $\underline { { b } } _ { i j }$ is non-increasing with j. When advertiser i bids between $[ ~ \underline { { { b } } } _ { i s } , ~ \underline { { { b } } } _ { i , s - 1 } ] ,$ for some $s { > } \varphi ( i )$ , she will obtain position s. Therefore,

$$
\begin{array}{l} \int_ {\underline {{v}}} ^ {v _ {i}} p _ {i} (t, \mathbf {v} _ {- i}) d t = \int_ {\underline {{b}} _ {i, \varphi (i)}} ^ {v _ {i}} p _ {i} (t, \mathbf {v} _ {- i}) d t + \int_ {\underline {{b}} _ {i, \varphi (i) + 1}} ^ {\underline {{b}} _ {i, \varphi (i)}} p _ {i} (t, \mathbf {v} _ {- i}) d t + \dots \\ \qquad + \int_ {\underline {{b}} _ {i, k}} ^ {\underline {{b}} _ {i, k - 1}} p _ {i} (t, \mathbf {v} _ {- i}) d t + \int_ {\underline {{v}}} ^ {\underline {{b}} _ {i, k}} p _ {i} (t, \mathbf {v} _ {- i}) d t \\ \qquad = \alpha_ {i, \phi (i)} \left(v _ {i} - \underline {{b}} _ {i, \varphi (i)}\right) + \alpha_ {i, \varphi (i) + 1} \left(\underline {{b}} _ {i, \varphi (i)} - \underline {{b}} _ {i, \varphi (i) + 1}\right) + \dots \\ \qquad + \alpha_ {i k} \left(b _ {i, k - 1} - b _ {i k}\right) + 0 \\ \qquad = \alpha_ {i, \phi (i)} v _ {i} - \sum_ {s = \phi (i)} ^ {k} \left(\alpha_ {i s} - \alpha_ {i, s + 1}\right) \underline {{b}} _ {i s} \end{array}
$$

where $\alpha _ { i , k + 1 } = 0$ . So we get $m _ { i } ( \pmb { v } ) = \sum _ { s = \phi ( i ) } ^ { k } \left( \alpha _ { i s } - \alpha _ { i , s + 1 } \right) \underline { { b } } _ { i s }$ , which coin-<sup>¼ ð Þ</sup>cides with payment rule de<sup>fi</sup>ned in Eq. (10) with truthful bidding. □ Proof of Theorem 3. Omitted. Please refer to the proof of Theorem 4 for an example.

Proof of Theorem 4. Under assumption that $c _ { i j } { = } \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a }$ , (OP′) becomes

$$
\max _ {\mathbf {p}} \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) \alpha_ {j} ^ {p} \left\{\alpha_ {i} ^ {a} \left[ J (v _ {i}) - c _ {i} ^ {a} \right] \right\}, \text { s.t. } (i v), \text { for   any } \mathbf {c}, \boldsymbol {\alpha}, \mathbf {v}\tag{\( (OP''') \}
$$

To see that the greedy scoring mechanism is optimal, we note that according to $( \mathsf { O P } ^ { \prime \prime } ) , \mathrm { i f } s ^ { \mathrm { I I } } ( i ) { < } 0$ , it is never optimal to assign i to any position. In the mean time, it is never optimal to leave position j empty if there exists some unassigned advertiser i such that $\begin{array} { r } { \hat { s } ^ { \mathrm { I I } } ( i ) > 0 . \mathrm { A l s o } , } \end{array}$ it is obviously never optimal to <sup>fi</sup>ll position $j ( \le k )$ while $j - 1$ is empty. Now, suppose $s ^ { \mathrm { I I } } ( i ) { > } s ^ { \mathrm { I I } } ( l )$ for some advertisers i and l. For any positions $j { < } s ,$ , we have $\alpha _ { j } ^ { p } s ^ { \mathrm { I I } } ( i ) + \alpha _ { s } ^ { p } s ^ { \mathrm { I I } } ( l ) \geq \alpha _ { s } ^ { p } s ^ { \mathrm { I I } } ( i ) + \alpha _ { j } ^ { p } s ^ { \mathrm { I I } } ( l )$ . So it is never optimal to assign advertiser l before advertiser i. The above arguments suggest that the allocation function stated in Theorem 4 is optimal. □

Proof of Theorem 5. Under the assumption $c _ { i j } = c _ { j } ^ { p } + \alpha _ { i } ^ { a } \alpha _ { j } ^ { p } c _ { i } ^ { a }$ , (OP′) becomes

$$
\max _ {\mathbf {p}} \sum_ {j = 1} ^ {k} \sum_ {i = 1} ^ {n} p _ {i j} (\mathbf {v}) \alpha_ {j} ^ {p} \left\{\alpha_ {i} ^ {a} \left[ J (v _ {i}) - c _ {i} ^ {a} \right] - \frac {c _ {j} ^ {p}}{\alpha_ {j} ^ {p}} \right\}, \quad s. t. (i v), \text {   for   any   } \mathbf {c}, \boldsymbol {\alpha}, \mathbf {v}.\tag{\( (OP''' ) \}
$$

We <sup>fi</sup>rst show that the optimal KAM is a scoring mechanism. Specifically, we <sup>fi</sup>rst note that, according to (OP‴), $\mathrm { f } s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j } ^ { p } } { \alpha _ { i } ^ { p } } { < } 0 ,$ , it is never optimal to assign i to position j. In the meantime, it is never optimal to leave position j empty if there exists some unassigned advertiser i such that $s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } { > } 0 .$ If there are two advertisers i and l with $s ^ { \mathrm { I I I } } ( i ) > s ^ { \mathrm { I I I } } ( l ) > 0$ , then for any $s { > } j ,$ α<sup>p</sup> $\left[ s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } \right] + \alpha _ { s } ^ { p } \left[ s ^ { \mathrm { I I I } } ( l ) - \frac { c _ { s } ^ { p } } { \alpha _ { s } ^ { p } } \right] \geq$ $\alpha _ { s } ^ { p } \bigg [ s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { s } ^ { p } } { \alpha _ { s } ^ { p } } \bigg ] + \alpha _ { j } ^ { p } \bigg [ s ^ { \mathrm { I I I } } ( l ) - \frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } \bigg ]$ (note that $\alpha _ { j } ^ { p } { \geq } { \alpha _ { s } ^ { p } } { \geq } 0$ and the equality only holds when $\alpha _ { j } ^ { p } { = } \alpha _ { k } ^ { p } { = } 0 \mathrm { o r } j { > } k )$ . Therefore, like in Theorem 4, it is never optimal to place advertiser l before advertiser i. The above arguments suggest that the scoring rule and minimum bid policy stated in Theorem 5 are optimal.

We now show that the optimal allocation rule is greedy under Eq. (10). If $s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } > 0 ,$ it is never optimal to assign advertiser i to position j+1 while j is empty. This is because α<sup>p</sup> $\left( s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } \right) >$ $\alpha _ { j + 1 } ^ { p } \left( s ^ { \mathrm { I I I } } ( i ) - \frac { c _ { j + 1 } ^ { p } } { \alpha _ { j + 1 } ^ { p } } \right)$ note that α<sub>j</sub><sup>p</sup> > α<sub>j+1</sub><sup>p</sup> and $\frac { c _ { j } ^ { p } } { \alpha _ { j } ^ { p } } \leq \frac { c _ { j + 1 } ^ { p } } { \alpha _ { j + 1 } ^ { p } } \bigg )$ □

## References

[1] Z. Abrams, M. Schwarz, Ad auction design and user experience, Applied Economics Research Bulletin (2008) 98–105 (Special issue).

[2] A. Agarwal, K. Hosanagar, M.D. Smith, Location, location, location: an analysis of pro<sup>fi</sup>tability of position in online advertising markets, Journal of Marketing Research 48 (6) (2011) 1057–1073.

[3] G. Aggarwal, A. Goel, R. Motwani, Truthful auctions for pricing search keywords, in: Proceedings of the 7th ACM conference on Electronic commerce, ACM Press, New York, New York, USA, 2006, pp. 1–7.

[4] A. Animesh, V. Ramachandran, S. Viswanathan, Quality uncertainty and the performance of online sponsored search markets: an empirical investigation, Information Systems Research 21 (1) (2010) 190–201

[5] I. Ashlagi, D. Monderer, M. Tennenholtz, Mediators in position auctions, Games and Economic Behavior 61 (7) (2009) 2–21.

[6] S. Athey, G. Ellison, Position auction with consumer search, Quarterly Journal of Economics 126 (3) (2011) 1213–1270.

[7] D. Bergemann, S. Morris, Robust mechanism design, Econometrica 73 (6) (2005) 1771-1813

[8] T.-M. Bu, X. Deng, Q. Qi, Forward looking Nash equilibrium for keyword auction, Information Processing Letters 105 (2) (2008) 41–46.

[9] Y. Chen, C. He, Paid placement: advertising and search on the internet, NET Institute Working Paper No, 06–02, 2006.

[10] J. Chen, D. Liu, A.B. Whinston, Auctioning keywords in online search, Journal of Marketing 73 (4) (2009) 125–141.

[11] C.-H. Cho, H.J. Cheon, Why do people avoid advertising on the internet? Journal of Advertising 33 (4) (2004) 89–97.

[12] C. Dellarocas, Double marginalization in performance-based advertising: implications and solutions, Management Science 58 (2012) 1178–1195.

[13] X. Drèze, F.X. Hussherr, Internet advertising: is anybody watching? Journal of Interactive Marketing 17 (4) (2003) 8–23.

[14] B. Edelman, M. Schwarz, Optimal auction design and equilibrium selection in sponsored search auctions, American Economic Review 100 (2) (2010) 597–602.

[15] B. Edelman, M. Ostrovsky, M. Schwarz, Internet advertising and the generalized second-price auction: selling billions of dollars worth of keywords, American Economic Review 97 (1) (2007) 242–259.

[16] J. Feng, Optimal mechanism for selling a set of commonly ranked objects, Marketing Science 27 (3) (2008) 501–512.

[17] J. Feng, H. Bhargava, D. Pennock, Implementing sponsored search in Web search engines: computational evaluation of alternative mechanisms, INFORMS Journal on Computing 19 (1) (2007) 137–148.

[18] D. Garg, Y. Narahari, An optimal mechanism for sponsored search auctions on the web and comparison with other mechanisms, IEEE Transactions on Automation Science and Engineering 6 (4) (2009) 641–657.

[19] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Management Science 55 (10) (2009) 1605–1622.

[20] A. Goldfarb, C. Tucker, Online display advertising: targeting and obtrusiveness Marketing Science 30 (3) (2011) 389–404.

[21] R. Gonen, S. Vassilvitskii, Sponsored search auctions with reserve prices: going beyond separability, Internet and Network Economics 5385 (2008) 597–608.

[22] M. Harris, A. Raviv, A theory of monopoly pricing schemes with demand uncertainty, American Economic Review 71 (3) (1981) 347–365.

[23] L. Hurwicz, The design of mechanisms for resource allocation, American Economic Review 63 (2) (1973) 1–30.

[24] IAB, IAB internet advertising revenue report — 2011 full year results, http:// www.iab.net/media/<sup>fi</sup>le/IAB\_Internet\_Advertising\_Revenue\_Report\_FY\_2011. pdf 2012.

[25] G. Iyengar, A. Kumar, Characterizing optimal keyword auctions, in: Second Workshop on Sponsored Search Auctions, Citeseer, Ann Arbor, Michigan, 2006

[26] Z. Katona, M. Sarvary, The race for sponsored links: bidding patterns for search advertising, Marketing Science 29 (2) (2010) 199–215.

[27] S. Lahaie, D.M. Pennock, Revenue analysis of a family of ranking rules for keyword auctions, in: Proceedings of the 8th ACM conference on Electronic commerce, ACM, New York, NY, 2007.

[28] D. Liu, J. Chen, Designing online auctions with past performance information, Decision Support Systems 42 (3) (2006) 1307–1320.

[29] D. Liu, S. Viswanathan, Information asymmetry and hybrid advertising, Working paper, 2011.

[30] D. Liu, J. Chen, A.B. Whinston, Ex-ante information and the design of keyword auctions, Information Systems Research 21 (1) (2010) 133–153.

[31] E. Maskin, J. Riley, Optimal multi-unit auctions, in: The Economics of Missing Markets, Information, and Games, Oxford University Press, Oxford, New York, Toronto and Melbourne, 1989

[32] P. Milgrom, Putting auction theories to work, Cambridge University Press Cambridge, UK., 2004

[33] P. Milgrom. Simplified mechanisms with an application to sponsored-search auctions, Games and Economic Behavior 70 (1) (2010) 62–70.

[34] J. Müller, D. Wilmsmann, J. Exeler, M. Buzeck, A. Schmidt, T. Jay, A. Krüger, Display blindness: the effect of expectations on attention towards digital signage, Pervasive Computing, Lecture Notes in Computer Science 5538 (2009) 1–8.

[35] R.B. Myerson, Incentive compatibility and the bargaining problem, Econometrica 47 (1) (1979) 61–73.

[36] R.B. Myerson, Optimal auction design, Mathematics of Operations Research 6 (1) (1981) 58–73.

[37] Y. Nam, K.H. Kwon, S. Lee, Does it really matter that people zip through ads? Testing the effectiveness of simultaneous presentation advertising in an IDTV environment, Cyberpsychology, Behavior and Social Networking 13 (2) (2010) 225–229.

[38] M. Ostrovsky, M. Schwarz, Reserve prices in internet advertising auctions: a <sup>fi</sup>eld experiment, Stanford University Graduate School of Business Research Paper No. 2054, 2009.

[39] H.R. Varian, Position auctions, International Journal of Industrial Organization 25 (6) (2007) 1163–1178.

[40] T.A. Weber, Z. Zheng, A model of search intermediaries and paid referrals, Information Systems Research 18 (4) (2007) 414–436.

[41] L. Xu, J. Chen, A. Whinston, Oligopolistic pricing with online search, Journal of Management Information System 27 (3) (2011) 111–141.

[42] L. Xu, J. Chen, A. Whinston, Price competition and endogenous valuation in search advertising, Journal of Marketing Research 48 (3) (2011) 566–586

[43] X. Zhang, J. Feng, Cyclical bid adjustments in search-engine advertising, Management Science 57 (9) (2011) 1703–1719.

[44] Y. Zhu, K.C. Wilbur, Hybrid advertising auctions, Marketing Science 30 (2) (2010) 249–273.

Jun Li received his Ph.D. in Quantitative Economics in 2012 from the University of International Business and Economics. His research interests lie in auction theory and its applications, mechanism design with applications to Internet advertising. His work is published in Economics Letters, and Journal of Management Sciences in China, among others.

De Liu is an associate professor in the Gatton College of Business and Economics at the University of Kentucky. He received his Ph.D. in Management Science and Information Systems in 2004 from the University of Texas at Austin. His research interests lie in the design and analysis of internet-based auctions, contests, and other mechanisms with applications to Internet advertising, digital gaming, and enterprise content management. His work has appeared in Information Systems Research, Journal of Marketing and Decision Support Systems.

Shulin Liu is a professor in the School of International Trade and Economics at the University of International Business and Economics (Beijing). He received his Ph.D. in Management Science in 1997 from the Beijing University of Aeronautics and Astronautics. His research interests lie in competitive bidding and auction. His work is published in Economics Letters, Computational Economics, and Journal of System Science and Complexity, among others.
