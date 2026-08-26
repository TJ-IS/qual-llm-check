---
otero_id: 26791
otero_key: "6E6WMGVM"
title: "Ownership and Investment in Electronic Networks"
authors: "J. Yannis Bakos; Barrie R. Nault"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.4.321"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [137.189.171.235] On: 20 September 2016, At: 18:36 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR Information Systems Research

# Information Systems Research

![](/api/attachments/6E6WMGVM/fulltext/images/97cde8ecfca88ef619b30cb3cf85e98a593f88a8ecbfa879dfc4f3c8d20b0c97.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Ownership and Investment in Electronic Networks

J. Yannis Bakos, Barrie R. Nault,

## To cite this article:

J. Yannis Bakos, Barrie R. Nault, (1997) Ownership and Investment in Electronic Networks. Information Systems Research 8(4):321-341. http://dx.doi.org/10.1287/isre.8.4.321

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6E6WMGVM/fulltext/images/366c6b6695f990daf85173673c7d8ed67dc78b05a3f66baa0e883f835781e009.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Ownership and Investment in Electronic Networks

J. Yannis Bakos • Barrie R. Nault

Center for Research on Information Technology and Organizations, Graduate School of Management, University of California, Irvine, California 92697

bakos@uci.edu

brnault@uci.edu

We employ the theory of incomplete contracts to examine the relationship between ownership and investment in electronic networks such as the Internet and interorganizational information systems. Electronic networks represent an institutional structure that has resulted from the introduction of information technology in industrial and consumer markets. Ownership of electronic networks is important because it affects the level of network-specific investments, which in turn determine the profitability, and in some cases the viability, of these networks. In our analysis we define an electronic network as a set of participants and a portfolio of assets. The salient concept in this perspective is the degree to which network participants are indispensable in making network assets productive. We derive three main results. First, if one or more assets are essential to all network participants, then all the assets should be owned together. Second, participants that are indispensable to an asset essential to all participants should own all network assets. Third and most important, in the absence of an indispensable participant, and as long as the cooperation of at least two participants is necessary to create value, sole ownership is never the best form of ownership for an electronic network. This latter result implies that as the leading network participants become more dispensable, we should see an evolution toward forms of joint ownership.

(Incomplete Contracts; Investment Externalities; Internet Ownership; Network Externalities; Network Investment; Network Ownership)

## 1. Introduction

Electronic networks, such as the Internet and interorganizational information systems (IOS), are becoming central in coordinating transactions between buyers and their suppliers, generating substantial economic benefits in the process (Bakos 1991). These networks represent an increasingly common institutional structure that has resulted from the widespread use of information technology (IT) in consumer and industrial markets. The Internet already provides content and communications to millions of individual and corporate users and is increasingly important in facilitating economic transactions. Other examples of electronic networks include value-added networks (AUCNET), centralized industry networks (ASAP Express, airline computer reservation systems (CRS), ATM networks), and electronic trading systems (NASDAQ, SEAQ).

## 1.1. Ownership in Electronic Networks

In this article we study the ownership structure of electronic networks, that is, whether these networks are owned by one or more buyers, suppliers, independent intermediaries, or some combination. An understanding of the role of ownership in electronic networks is important because the ownership structure determines the level of network investments, which in turn determine the functionality, the profitability, and, in some cases, the viability of these networks. Thus, the implications of alternative ownership structures are of particular interest to the participants in an electronic network, to potential competitors and to industry regulators.

The history of IOS amply illustrates the importance of ownership. Airline CRS were traditionally owned by individual airlines, with American and United dominating the market. Their competitors argued that these two airlines should be forced to divest their CRS, creating independent intermediaries and an ownership structure that would better serve competition, encouraging more efficient levels of investment and providing higher economic surplus. Similar ownership issues have arisen in the hospital supplies market, which in the 1980s was dominated by Baxter's ASAP system. The VHA group of hospitals attempted to introduce its own customer-owned system. Independent intermediaries have introduced systems in partnership with sellers, such as McDonnell Douglas with Abott Labs, and General Electric Information Systems Company (GEISCO) with Baxter. In both the airline and the hospital supplies markets there has been talk of introducing systems owned by a consortium of participants or moving existing systems to multi-party ownership, as is the case with United's Apollo CRS, which is now owned by Covia, a consortium of several airlines.

In the case of the Internet, the current ownership structure evolved from the ARPANET, a computer network that was developed in the late 1960s, which consisted of host computers linked through leased telephone lines. The ARPANET initially was a singly owned network, funded in its entirety by the Advanced Research Projects Agency (ARPA) of the U.S. Department of Defense. Presently, the Internet is characterized by a three-tiered hierarchy: the network backbone, the regional network operators and network service providers, and the user networks (campus networks). The components of each of these tiers are owned by hundreds or thousands of commercial, government, and end-user organizations, resulting in a highly distributed ownership structure.

We employ the Grossman, Hart, and Moore (Grossman and Hart 1986, Hart and Moore 1990) (hereafter GHM) theory of incomplete contracts to study the economic significance of ownership in electronic networks. Specifically, we model the impact of alternative ownership structures on the investments of individual network participants in network-specific assets, and their corresponding implications for economic efficiency. We begin by defining an electronic network as a portfolio of assets, and then specifying the ownership structure over these network assets. Given this ownership structure, we determine the participants' payoffs by a Shapley value division of the surplus generated by the "grand coalition" of all network participants. These payoffs, in turn, determine the participants' investment levels resulting from a noncooperative Nash equilibrium. In other words, network participants make investment decisions based on the payoffs they will receive under a given ownership structure. Our objective is to derive optimal ownership structures under specific interdependencies between network participants and assets.

Our analysis leads to three main results. First, if one or more assets are essential to all network participants, then all the assets should be owned together. Second, a single network participant that is indispensable to an asset essential to all participants should own all network assets. Third and most important, in the absence of an indispensable participant, and as long as the cooperation of at least two participants is necessary to create value, sole ownership is never the best form of ownership for an electronic network. This latter result implies that as the leading participants of electronic networks become more dispensable, we should see movement toward forms of joint ownership.

## 1.2. IT and Organizational Governance

Much research in the Information Systems literature studies the impact of IT on organizations and markets, and in particular whether IT promotes hierarchical governance mechanisms based on intrafirm control, or market-mediated mechanisms based on interfirm relationships. The primary attempts at analysis have employed transaction cost theory and agency theory, focusing on the nature of the contracting relationship between multiple parties.

The transaction cost approach has been employed to study the impact of IT on production costs, which presumably are lower in market settings, versus its impact on transaction costs, which can be lower in hierarchical settings. This has led to the conclusion that IT can lower both production and transaction costs, reducing the costs of both markets and hierarchies without universally favoring one of these governance mechanisms (Gurbaxani and Whang 1991). Others have argued, however, that these cost reductions favor markets over hierarchies (Malone et al. 1987). Approaches based on agency theory have focused on the tradeoff between information costs, which presumably are lower when decision rights are decentralized, and monitoring costs, which may be lower when decision rights are centralized. It has been argued that IT can lower both information costs and monitoring costs, with the overall impact on organizational governance mechanisms again inconclusive.

Although previous work has addressed the impact of IT on various organizational costs, an alternative approach is to study the impact of IT on the ownership of assets and the resulting incentives for investment. For instance, Brynjolfsson (1990, 1994) showed how the Hart and Moore (1990) (hereafter H&M) framework could be used to study ownership issues for information assets such as knowledge and intellectual capital. He analyzed a number of alternative organizational structures involving interactions among information assets and physical assets, and found that giving agents some ownership of the physical assets to which their information assets apply, yields the greatest incentives for investment across a variety of situations. He also found that centralized coordination typically implies that centralized asset ownership will be optimal. Alstyne et al. (1995) use the same framework to derive principles for data ownership. In this article and in our earlier work (Bakos and Nault 1992) we use the theory of incomplete contracts to study the relationship between the ownership structure of an electronic network and the incentives to invest in network-specific assets. This relationship is important because investment by network participants fundamentally determines the social and economic value of an electronic network.

Specifically, we define an electronic network as a set of participants and a portfolio of assets, and we develop a model of ownership and investment based on the H&M framework. In this setting, the ownership of system assets determines in part the ex-post distribution of payoffs among system participants, which in turn determines the ex-ante investment of these participants and the value created by the system. The model is closed in the sense that expectations about the payoffs that will be received by individual participants determine their corresponding investments. Certain concepts emerge as salient in this perspective; for instance, the ownership structure that yields the network with the highest economic value critically depends on the degree to which a participant is indispensable to network assets, and on the degree of economic interdependence among network participants. Our results specify two general cases where all assets should be owned together and a general condition under which sole ownership is dominated.

## 1.3. Incomplete Contracts, Asset Ownership, and Investment

Williamson (1975, 1985) points out that contractual arrangements between economic agents are rarely complete in the sense that they never need to be renegotiated, revised, or complemented; writing such complete contracts is costly and often infeasible. He offers a theory of firm boundaries by arguing that the cost of contracting, enforcing the contracts, and dealing with unforeseen contingencies varies depending on whether a market or hierarchical governance structure is employed. Grossman and Hart (1986) (hereafter G&H) suggest that the crucial difference between governance structures lies in their implied residual decision rights. They define ownership as the assumption of these rights, which determine the outcome under the uncovered contingencies of an incomplete contract. Hart and Moore (1988) sharpen Williamson's argument by pointing out that contracts may be incomplete because certain variables are nonverifiable by a third party such as an arbitrator or a court, even though they are observable by the parties entering into a relationship. Being "observable but nonverifiable" means that the parties cannot enter into a contract based on the outcome of these variables.

This inability to enter into complete contracts highlights the importance of ownership. Asset ownership according to G&H, and as used in our analysis, closely parallels the legal use of the term: ownership determines the disposition of an asset in contingencies not covered by a contract; i.e., the owner of an asset has the right to exclude other agents from using the asset, except to fulfill explicitly specified contractual obligations. This concept of ownership does not necessarily endow the owner with the residual income streams associated with the asset. Rather, these residual streams frequently accrue to asset owners because of their ability to maintain a strong bargaining position based on the right to exclude other agents. This differs from Williamson's (1985) view of ownership as the assignment of residual income streams in order to minimize the contracting complexities and reduce the transaction costs associated with employing the asset. Under both perspectives, however, the costs or unfeasibility of complete contracts is what makes ownership important: if the disposition of an asset could be contractually determined under all possible contingencies, then its ownership would be irrelevant.

The right to exclude other agents from using an asset allows the owner of the asset to extract rents from any agents who need access to this asset to produce economic value. G&H show that the need to divide the payoffs from an asset creates inefficiencies by inducing agents to make suboptimal investment decisions. H&M demonstrate that if investments are noncontractible and outcomes are nonverifiable, the inability to fully capture incremental payoffs in ex-post bargaining may lead to suboptimal levels of ex-ante investment. In particular, they show that when there are positive network externalities, positive marginal network externalities and positive investment externalities, and under certain rules for sharing the resulting economic surplus, all agents underinvest. To illustrate how the ownership structure can affect investments in an incomplete contracting setting, we refer the reader to the stylized numerical examples in Holmström and Tirole (1989).

This propensity to underinvest can become particularly problematic for electronic networks. These systems require substantial investments in specific assets such as information, expertise, training, and human capital, investments that typically are noncontractible and cannot be separated from the investing participant if that participant later becomes disenfranchised. These noncontractible investments are crucial (Bakos and

Brynjolfsson 1993), yet their value may be difficult to capture in ex-post bargaining, resulting in substantial underinvestment and reduced total welfare. An appropriate ownership structure can partially alleviate this problem by inducing key participants in electronic networks to make important noncontractible investments.

## 1.4. Overview

Section 1 consists of this introduction. Section 2 reviews the notation, assumptions and first proposition from H&M, interprets their framework in the context of an electronic network, and examines three of H&M's results with implications for electronic networks. Section 3 derives our main new results. Section 4 analyzes an in-depth example comparing ownership structures. Finally, Section 5 discusses the implications of our analysis and presents our conclusions.

## 2. System Ownership, Investment, and Welfare: H&M's Results Applied to Electronic Networks

## 2.1. Model Setting, Notation and Definitions

Adopting the notation of H&M, we consider a two-period setting (periods 0 and 1) consisting of a set S of I risk neutral network participants and a set A of N assets $a_{n}$ ( $n = 1, \ldots, N$ ) representing the IT components of an electronic network. At date 0, each agent i makes a network-specific investment $x_{i}$ . At date 1, production and trade take place. Investment $x_{i}$ affects i's productivity on date 1. Network returns depend on which agents join the network and on their levels of network-specific investment, such as training their staff to use the system, or expertise in implementing and operating the network infrastructure.

Investments $x_{i}$ are chosen noncooperatively by the network participants at date 0 and are too complex to be specified in a date 0 contract. The future is uncertain, so plans for date 1 trade cannot be included in a date 0 contract, either. As a result, multilateral bargaining takes place in period 1 to consummate trade and divide the payoffs derived by the network. We assume that the bargaining power of the parties determines the division of payoffs in date 1, and that this division is described by the Shapley value bargaining mechanism (Shapley 1953), which awards each participant an amount equal to that participant's incremental contribution to each potential coalition, multiplied by the probability of each such coalition occurring during the formation of the grand coalition. $^{1,2}$

We assume that costs and benefits are observable and can be measured in monetary terms, but are nonverifiable. In accordance with H&M, we assume that $x_{i} \in [0, \bar{x}_{i}]$ , where $\bar{x}_{i} \geq 0$ , i.e., there is a maximum feasible level of investment. $^{3}$ Furthermore, we assume that $x_{i}$ is specific to the network, i.e., it cannot create value unless i has access to at least some of the network assets in A. The cost of investment $x_{i}$ to participant i is denoted by $c_{i}(x_{i})$ .

Let $\mathbf{x} = (x_{1}, x_{2}, \ldots, x_{t})$ and let $\nu(S, A | \mathbf{x})$ be the value generated from a coalition S controlling assets A in period 1, assuming investments x in period 0. We denote by $\nu_{i}(S, A | \mathbf{x})$ the value generated by participant i, so that $\nu(S, A | \mathbf{x}) = \Sigma_{t \in S} \nu_{i}(S, A | \mathbf{x})$ . Finally, let the

$^{3}$ For investment in human capital, it is reasonable to assume a maximum level of investment, corresponding, for example, to an individual's maximum possible effort level.

marginal return on investment by network participant i, given S and A, be

$$
\frac {\partial}{\partial x _ {i}} \nu (S, A | \mathbf {x}) \equiv \nu^ {i} (S, A | \mathbf {x}).
$$

To determine the assets owned by a given coalition, we define a control (or ownership) structure $\alpha$ as a mapping $\alpha:S\to A$ , where $A\subseteq\underline{A}$ . Following H&M, a control structure must satisfy two properties: (1) any individual asset $a_{n}$ cannot be controlled by both a coalition S and its complement $\underline{S}\backslash S$ ; and (2) any asset controlled by a coalition must be controlled by all supersets of that coalition. Examples of control structures include a single participant owning the entire network, or a certain component of the network being controlled via majority vote by a subset of system participants, each of which own voting shares.

Let $B_{i}(\alpha \mid \mathbf{x})$ be agent $i$ 's Shapley value and $p(S)$ represent the probability that $i$ is in a random coalition $S$ . From the definition of the Shapley value it follows that

$$
B _ {t} ^ {\iota} (\alpha | \mathbf {x}) \equiv \frac {\partial}{\partial x _ {t}} B _ {t} (\alpha | \mathbf {x}) = \sum_ {S \mid t \in S} p (S) \nu^ {\iota} (S, \alpha (S) | \mathbf {x}),
$$

where

$$
p (S) = \frac {(s - 1) ! (I - S) !}{I !}.
$$

## 2.2. An Example: The Internet

In the context of the Internet, network participants are likely to be one of two general types: bandwidth providers and trading participants such as content providers. Telecommunications corporations or bandwidth resellers are examples of bandwidth providers and they contribute the switching, telecommunications and security assets necessary to operate a network. Their investments include investments in software necessary to manage the network for Internet access provision and protocols for carrying data traffic. Their investments in connectivity to other network participants, in directory services and in name management also affect the value generated by the network.

Customers, vendors, and intermediaries are examples of trading participants. Their Internet-specific assets include web page design and mechanisms for handling transactions over the World Wide Web. Their investments include increasing the attractiveness of their web sites, or facilitating the execution and increasing the security of Internet transactions for their goods and services.

We illustrate some of the general results of our analysis through a specific functional form tailored to the Internet. Let the value realized by network participant i be

$$
\nu_ {i} (S, A | \mathbf {x}) = \bigg (\sum_ {n \mid a _ {n} \in A} \lambda_ {i n} a _ {n} \bigg) \bigg (\sum_ {k \in S} \mu_ {i k} x _ {k} ^ {1 / 2} \bigg) x _ {i} ^ {1 / 2},
$$

where $x_{i}, a_{n}, \lambda_{m}$ , and $\mu_{ik} \geq 0$ . The parameter $\lambda_{in}$ scales the impact on i of network assets A, and $\mu_{ik}$ scales the impact on i of other agents' investments. We specify investment costs as

$$
c _ {i} (x _ {i}) = c (x _ {i}) = \frac {b}{(\bar {x} - x _ {i}) ^ {2}} - \frac {b}{\bar {x} ^ {2}},
$$

where $b > 0$ and $0 \leq x_{i} \leq \bar{x}$ .

For the Internet, this functional form reflects the fact that the value derived by each participant increases as more assets are added and as participants make larger investments. Thus, all potential participants find it favorable to join the Internet, which in the context of our model means that the “grand coalition” forms. The weights $\lambda_{in}$ and $\mu_{ik}$ reflect the fact that specific assets and investments have different value for different participants. For example, an asset $a_{n}$ representing a certain Internet site increases the Internet’s value to participant i by a quantity scaled by $\lambda_{in}$ , the marginal contribution of asset $a_{n}$ on i’s value. Additional investment by any other participant k further increases the value to i, and $\mu_{ik}$ represents the marginal contribution of k’s investment on i’s value. To illustrate, investment in improved traffic management software by a bandwidth provider k will create value for Internet participants; the actual benefits realized by a specific participant i will depend on the actual sites accessed by i (which will be included in the network assets A that i has access to), the relative value of these sites as reflected by $\lambda_{in}$ ’s, and the ability of k’s investment to relieve congestion problems faced by these sites, as reflected by $\mu_{ik}$ .

Metcalfe's Law, which states that the value of participating in a network grows as the square of the number of network participants, is sometimes used to explain the exponential growth patterns in electronic networks such as the Internet. Our functional form is a generalization of the value function implied by Metcalfe's Law: if we set all $\lambda_{ij}$ and $\mu_{ik}$ to 1, and all $x_{i}$ to $\hat{x}$ , we get

$$
\begin{array}{r l} \nu_ {t} & = n \hat {a} \hat {x} ^ {1 / 2} (n - 1) \hat {x} ^ {1 / 2} = n (n - 1) \hat {a} \hat {x} \\ & = K n (n - 1) = O (n ^ {2}), \end{array}
$$

where $K$ is a constant, $n = |S|$ and $O(n^2)$ is "on the order of $n^2$ ."

## 2.3. H&M Assumptions in the Context of Electronic Networks

We assume that Assumptions 1–6 of the H&M framework hold; these assumptions are discussed in Appendix 1 in the context of electronic networks. Assumptions 4, 5, and 6 are particularly important as they formalize positive externalities that characterize electronic networks. These externalities arise due to the synergies from larger numbers of participants, from higher levels of investment, and from cooperation through the network, $^{4}$ and we call them investment externalities, network externalities, and marginal network externalities, respectively. As shown in Appendix 1, our functional form representing the investment costs and network value of the Internet also satisfies H&M Assumptions 1 through 6, and thus the propositions in the following sections apply to it.

With most reasonable methods for dividing the surplus from the grand coalition, these three externalities being positive ensures that each potential participant is better off joining the grand coalition, and thus the grand coalition forms. As mentioned earlier, we follow H&M in assuming that the surplus created is allocated according to the participants' Shapley values. $^{5}$ Since network participants anticipate this division of payoffs, we examine what network investments result under alternative ownership structures, judged against first-best where a social planner dictates individual investments.

## 2.4. Underinvestment in Electronic Networks

The main result from H&M (their Proposition 1) is given below, stated in the context of electronic networks:

PROPOSITION 1 (H&M). Any ownership (control) structure results in underinvestment, relative to first-best, by each network participant. In addition, if the ownership structure changes so that each network participant's marginal return on investment increases, then equilibrium investment and social surplus increase as well.

The basis of Proposition 1 is the presence of network externalities and the inability of any party to fully capture the returns from its investment in the ensuing ex-post bargaining. Because of the anticipated inability to fully capture payoffs in ex-post bargaining, direct returns from investment to each participant do not fully reflect the impact of marginal network and investment externalities, and therefore are understated compared to the total returns to the grand coalition. Because individual investment decisions are based on each participant's private return on investment, all participants underinvest.

This underinvestment is due to the noncontractible and specific nature of investments and the nonverifiability of outcomes in this setting, which preclude efficient contracts and revelation mechanisms (Myerson 1982). Although Assumptions 1–6, which are necessary for the general proof of underinvestment, are quite restrictive, this outcome arises in a wide variety of settings that do not satisfy these assumptions. It is thus often the case that the need to commit to specific investments and the knowledge that part of the resulting rents will not be captured in the ex-post bargaining leads to underinvestment and a second-best outcome.

In our Internet functional form, Proposition 1 follows directly from the additive structure. The first-order condition characterizing each participant's investment decision is given by

$$
\begin{array}{l}\nu^{\prime}(S,A|\mathbf{x}) = \frac{\partial}{\partial x_{i}}  \nu_{i}(S,A|\mathbf{x}) + \sum_{\substack{l\in S\\ l\neq i}}\frac{\partial}{\partial x_{i}}  \nu_{l}(S,A|\mathbf{x})\\ = \bigg(\sum_{n  |  a_{n}\in A}  \lambda_{im}a_{n}\bigg)\bigg(\frac{1}{2}  x_{i}^{-1 / 2}\sum_{\substack{k\in S\\ k\neq i}}\mu_{ik}x_{k}^{1 / 2} + \mu_{it}\bigg)\\ \\ +\sum_{\substack{l\in S\\ l\neq i}}\bigg[\bigg(\sum_{n  |  a_{n}\in A}  \lambda_{im}a_{n}\bigg)\frac{1}{2} x_{i}^{-1 / 2}\mu_{il}x_{l}^{1 / 2}\bigg]\geq 0. \end{array}\tag{1}
$$

Investments are higher as assets or participants increase, because there are more terms in $\nu'(S, A|x)$ and these terms are nonnegative; thus first-best investments will be realized in a network encompassing all assets and participants. This functional form is particularly useful to illustrate the second part of Proposition 1: a change in ownership structure implies the given coalition has control over additional assets, for example, improved traffic management software. This new asset base increases each participant's investment directly through an additional asset $a_{n}$ , thereby adding terms to $\nu'(S, A|x)$ . For example, the value of improved traffic management software increases as the Internet grows, both directly by applying to a larger network, and indirectly through the larger investments induced from Internet participants as traffic management is improved.

Although it may be impossible to avoid underinvestment, the particular second-best outcome reached depends on the ownership structure for the assets, that is, how ownership of the constituent parts of the network is divided among the network participants. The question we address in the remainder of this article is which allocations of ownership for the network assets, such as ownership by a single system participant or joint ownership by some subset of system participants, maximize the total value of the network.

## 2.5. Ownership and Investment

The simplest case arises when only one network participant has to make an investment decision, and is addressed by H&M Proposition 2.

PROPOSITION 2 (H&M). If only one participant has an investment decision, that participant should own all assets A.

If only one participant (participant i) has a relevant network-specific investment, then we want to choose a control structure $\alpha$ that maximizes i's marginal return on investment. From Assumption 5, this is maximized by putting $\alpha(S) = \underline{A}$ for all S containing i. In other words, for every coalition S, any network asset $\alpha_{n}$ is controlled by S if and only if i belongs in S. Thus, i owns the entire network $\underline{A}$ .

It is straightforward to show that this proposition applies to our functional form for network value in

Equation (1): $\alpha(S) = \underline{A}$ maximizes the number of terms in the summations $\Sigma \lambda_{in} \alpha_{n}$ . The idea is simple: the best way to induce investment by a participant is to give that participant control of the network. This results in the best possible position in ex-post bargaining, providing the greatest ex-ante marginal incentive to invest. Thus, the relative importance of a participant's non-contractible investment is a key factor in determining that participant's ownership rights. Because the Internet is a distributed network, many participants have investment decisions and Proposition 2 does not apply. However, as we discuss in the conclusion, certain IOS have been historically characterized by single-agent investments.

## 2.6. Idiosyncratic Assets and Indispensable Participants

Following H&M, if some network asset affects the marginal productivity of only one participant, we call that asset idiosyncratic to the participant. In other words, the asset affects no other participant's marginal benefit: asset $a_{T}$ is idiosyncratic to agent i if for all agents j in any coalition S and for all sets A of assets containing $a_{T}$ , $\nu^{j}(S, A) = \nu^{j}(S, A \setminus \{a_{T}\})$ for all $j \neq i$ . Similarly, if some participant i has unique specific skills necessary to make asset $a_{T}$ operational, we characterize this participant as indispensable to $a_{T}$ . In other words, only coalitions including network participant i can derive value from this asset: agent i is indispensable to asset $a_{T}$ if for all agents j in any coalition S and for all sets A of assets containing $a_{T}$ , $\nu^{j}(S, A) = \nu^{j}(S, A \setminus \{a_{T}\})$ if $i \notin S$ . If an asset is idiosyncratic to a participant, then the participant is indispensable to that asset. Our Propositions 3 and 4 show what is necessary to operationalize these concepts in our functional form (all our proofs are contained in Appendix 2).

PROPOSITION 3 (Idiosyncratic Assets). In our functional form, asset $a_{T}$ is idiosyncratic to participant $i$ if and only if $\lambda_{jT} = \mu_{j}$ = 0 for $j \neq i$ .

PROPOSITION 4 (Indispensable Agents). In our functional form, participant i is indispensable to asset $a_{T}$ if and only if $\lambda_{jT} = 0$ for $j \neq i$ . In that case, participant i must be in any coalition that derives marginal benefit from asset $a_{T}$ .

For idiosyncratic assets in our functional form, asset $a_{T}$ affects only participant i's marginal productivity. These effects occur both directly (through the $\lambda_{iT}s$ ) and indirectly (through the $\mu_{jt}s$ ). Moreover, the conditions required for an asset to be idiosyncratic to a participant are more strict than those required for a participant to be indispensable to an asset: the indirect effect of $\mu_{ij} = 0$ for $j \neq i$ is required for idiosyncratic assets but is not required for indispensability. The condition for indispensable participants specifies that participant i is not in S.

Propositions 5 and 6 apply to all functional forms that satisfy Assumptions 1–6.

PROPOSITION 5 (H&M Proposition 5). If an asset is idiosyncratic to a participant, then the participant should own the asset.

For example, certain network participants may have developed customized network interfaces specific to their organizations, which are idiosyncratic in the sense that other network participants would not benefit from having access to them. According to Proposition 5, network participants should own their idiosyncratic components. An Internet example of an idiosyncratic asset is a firewall or a corporate intranet site restricted to internal use.

PROPOSITION 6 (H&M Proposition 6). If a participant is indispensable to an asset, then the participant should own the asset.

In an electronic network, a single participant may possess expertise necessary for the operation of the system. According to Proposition 6, that participant should own the entire network. Indispensability is closely related to asset specificity, a central concept in transaction cost theory: if an agent is indispensable to an asset, then the asset is specific to the agent. In other words, the value of the asset in its next best use by some other agent is zero. Proposition 6 also implies that the importance of a participant's noncontractible investment is only one force determining that participant's appropriate ownership rights. A second, possibly overriding force is the participant's importance as a coalition partner. Specifically, if a subset of participants has all the investment decisions, one cannot conclude that the ownership of assets should be concentrated only in this subset. In fact, if some participant outside the subset is indispensable, Proposition 6 implies that it is better to give all ownership rights to that participant. $^{4}$

Our functional form allows Proposition 6 to apply under weaker conditions that do not require participant i to be indispensable as defined in Proposition 4, but simply requires that the $\lambda_{iT}$ s be “small enough” relative to $\lambda_{iT}$ (proof is outlined in Appendix 2). This means that if some participant has unique skills related to a particular asset that can affect the productivity of this asset much more than the corresponding skills of other participants, then that participant should own the asset. For example, a participant may have developed a specialized search engine on the Internet. Although other Internet users can derive value from using this search engine and can affect its productivity by submitting proper listings of their private information, it likely that the impact of the developer’s investment will be much more significant, and thus the developer should own the search engine. Thus, our functional form allows participants to derive value from an asset or affect that asset’s marginal productivity, while still concluding that some other participant i should own the asset.

## 3. System Ownership, Investment, and Welfare: New Results

## 3.1. Essential Assets

If a participant cannot create any marginal value for the network without access to a certain asset, then we define the asset as essential to that participant: asset $a_{T}$ is essential to participant i if for all participants j in any coalition S and for all sets A of assets, $\nu'(S,A)=\nu'(S\setminus\{i\},A)$ if $a_{T}\notin A$ . For example, participants in an electronic network need access to the software that controls the operation of the network; this network control software is essential to all network since they cannot derive value from the network unless they belong to a coalition that controls this software. The sets of domain names and IP addresses is essential to the operation of the Internet, as the underlying communication protocols cannot function without access to these sets. Without such access the bandwidth providers could not provide—and the trading participants could not generate—value.

PROPOSITION 7 (Essential Assets). In our functional form, asset $a_{T}$ is essential to participant $i$ if and only if $\lambda_{m} = 0$ for $n \neq T$ and $\mu_{n} = 0$ for $j \neq i$ (i.e., iff participant $i$ cannot produce value without asset $a_{T}$ ).

Our functional form highlights the distinction between essential and idiosyncratic assets. With an asset essential to a participant, this functional form requires that the participant can generate value only through the essential asset. Conversely, with an idiosyncratic asset, this form restricts the direct effect of all other participant investments to be through assets other than the idiosyncratic asset. Both definitions require that the indirect effects through complementarities in marginal investment be zero.

As with Propositions 1, 2, 5, and 6, Proposition 8 and our remaining results apply to all functional forms satisfying Assumptions 1–6.

PROPOSITION 8. If one or more assets are essential to all participants, then all the assets should be owned or controlled together.

Proposition 8 implies that when certain assets are essential to all participants, then network ownership should be fully integrated, i.e., the same coalition should control all network assets. Thus, when an electronic network contains an essential asset, such as a central database or a switching component, common ownership of all network assets is optimal. According to Proposition 8, common ownership of the essential asset is not sufficient; all network assets should be owned and controlled together. This is an important implication of the H&M framework that applies to other settings as well; for example, Brynjolfsson (1994) derives a similar result for the ownership of organizational assets, when access to a central coordinator is essential to all agents. The following corollary follows directly:

COROLLARY 8.1. If at least one asset is essential to all participants, then nonintegrated ownership is dominated by full integration.

Corollary 8.1 rules out arrangements where although an essential asset such as the central system software is jointly owned, other network assets, such as on-premises equipment, are separately owned by individual participants. Stated differently, a necessary condition for nonintegrated ownership is that no assets are essential to all participants. This result is consistent with the formation of alliances among important network participants where the alliance owns all the network assets.

In the case of the Internet, where at its current stage of evolution a centralized ownership structure is infeasible as well as likely to be inefficient, Proposition 8 and Corollary 8.1 imply that essential assets should be avoided. Thus, multiple bandwidth providers, transmission and switching facilities ensure that no particular part of the Internet infrastructure becomes essential. Similarly, IP addresses are not treated as a single set (which would be an essential asset), but subsets of the address space are assigned to organizations, such as access providers, content providers, or individual users, that are responsible for the management of their allocated IP addresses.

PROPOSITION 9. If a participant is indispensable to an asset that is essential to all participants, then that participant should own all assets.

In this case asset $a_{T}$ must be controlled by any coalition for that coalition to be productive. Moreover, the coalition must contain participant i in order to make the asset productive. Because the only positive value coalitions are those that contain the essential asset and its indispensable participant, and because of superadditivity in assets (Assumption 5), all the assets should be owned by participant i.

For instance, an intermediary may be indispensable to the functioning of the central switching component of an intermediated network. $^{7}$ If the network cannot produce any value without its central switching asset, then this asset is essential to all network participants, and by Proposition 9, all network assets should be owned by the intermediary. $^{8}$ Indeed, we observe that single intermediaries tend to own their entire systems, even though they are only one of the participants that make network-specific investments, and may even not make the most important investments. Historically, the use of customized network switching software in most electronic networks reflected the fact that a single intermediary had the specific know-how in operating the software, and was thus indispensable to the entire network. As we argue later, expertise in operating network software has become more widespread and thus in the future no single participant may be indispensable to the operation of most networks. $^{9}$

Proposition 9 illustrates the dilemma faced by the privatization of InterNic, the joint venture between AT&T and Network Solutions responsible for the assignment and management of IP addresses and domain names on the Internet. In this capacity, InterNic has become indispensable to an essential asset. This could have allowed InterNic to hold up Internet participants, extracting rents at the expense of proper investment incentives for these participants. Because giving InterNic ownership of the entire Internet is neither feasible nor desirable, government ownership had been advocated as a solution that would avoid distorting proper incentives for investment. Although the U.S. government decided to exit a business in which it no longer enjoys a competitive advantage, these concerns were reflected in the multiyear contract under which the authority for domain name management was delegated to InterNic. As this contract is due to expire in 1998, efforts are underway to devise a scheme that allows multiple providers for the registration and management of domain names and IP addresses, and ensures that none of these providers becomes indispensable to this essential asset.

## 3.2. Mutually Important Network Participants

Participants in electronic networks frequently come together in a setting where no single participant has unique skills that are irreplaceable in developing and operating the network, and the cooperation of at least two participants, such as a customer and a supplier, is necessary in order to create value from the network. Although these participants may be heterogeneous in the sense that they may not all have equal marginal productivity, we call them mutually important in the sense that at least two must cooperate to derive value from the network, and no participants are indispensable to the entire network. In other words, asset impact on marginal productivity is dispersed and no single participants has the power to hold up the other network participant in ex-post bargaining. For example, mutually important participants provide a useful way to model certain aspects of the infrastructure and applications of the Internet.

Our functional form can easily accommodate this definition of mutually important participants: The participants to an electronic network with a central switching asset $a_{T}$ are mutually important iff:

(a) $\mu_{it} = 0$ for all participants $i$ (i.e., at least two participants must cooperate to create value);

(b) For each participant $i$ , $\lambda_{jT} > 0$ for some participant $j \neq i$ (i.e., no participants are indispensable to $a_T$ ).

The latter means that no participants have skills that are unique to particular assets.

To compare alternative ownership structures we begin by considering the polar cases of sole ownership by one participant versus joint ownership with equal voting shares by all participants. For simplicity, consider first the case of three network participants, $y_{1}$ , $y_{2}$ , and $y_{3}$ . Define $\hat{\alpha}$ as the control structure representing joint ownership of network assets, where participants hold equal voting rights and control is decided by majority rule. Define $\alpha$ as the control structure representing sole ownership by $y_{1}$ . Let $W(\mathbf{x}^{e}(\alpha))$ be the total network surplus from the equilibrium investment $\mathbf{x}^{e}(\alpha)$ under control structure $\alpha$ . The following proposition shows that in this case joint ownership yields greater network value and greater equilibrium investments than sole ownership.

PROPOSITION 10. In the case of three mutually important participants, network value and equilibrium investment is higher under joint ownership than under sole ownership, i.e., $W(\mathbf{x}^e(\hat{\alpha})) > W(\mathbf{x}^e(\alpha))$ and $\mathbf{x}^e(\hat{\alpha}) > \mathbf{x}^e(\alpha)$ .

In the case of three participants, joint ownership produces greater network value than sole ownership. This is due to the increased equilibrium investment by all participants: because there is an additional coalition (denoted by $S_{3}$ in the proof of Proposition 10) producing value under joint ownership compared to sole ownership, marginal returns on investment increase for participants $y_{2}$ and $y_{3}$ (because of positive marginal network externalities—Assumption 6), leading them to invest more. Because of the positive investment externalities (Assumption 4), $y_{1}$ also invests more, as the additional investment by $y_{2}$ and $y_{3}$ increases the marginal productivity of $y_{1}$ 's investment. The nondecreasing returns to investment (Assumption 2) and the fact that there is always underinvestment relative to the first-best (Proposition 1) guarantee that the increased investments produce higher network value and higher total payoffs for the grand coalition.

In general, joint ownership of network assets by all or by a subset of network participants neither dominates nor is dominated by sole ownership. This is because under joint ownership there are coalitions that have control but do not include all participants and under sole ownership there are coalitions that have control with less than half the participants. For the same reason, there is no general dominance result between joint ownership by all and joint ownership by a subset of network participants. Although sole ownership is optimal if one participant is indispensable, in the case of mutually important participants sole ownership is generally dominated by a form of joint ownership. We define unbalanced joint ownership (UJO) as the control structure where the participant with the largest controlling interest does not have sole control, but the coalition of this participant with any other participant has control. $^{10}$ Let this control structure be denoted by $\tilde{\alpha}$ . The following proposition shows that sole ownership is generally dominated by UJO.

PROPOSITION 11. With mutually important participants, network value and equilibrium investment is higher under UJO than under sole ownership.

Corollary 11.1 follows directly from Proposition 11.

COROLLARY 11.1. Unless some network participant is indispensable, in networks that derive their value from interorganizational efficiencies (i.e., from the cooperation of at least two participants) sole ownership is a dominated ownership structure.

Proposition 11 and Corollary 11.1 are important because they rule out sole ownership of network assets in the absence of an indispensable system participant. In this case, control should be vested in some form of joint ownership. This result is consistent with the evolution of Internet ownership. In the days of the ARPANET, the Internet's predecessor, no participant other than the U.S. government was willing to underwrite the heavy R&D necessary to develop essential network assets, such as the TCP/IP protocols. Thus, the U.S. government was indispensable to essential assets, and according to Propositions 6 and 8 it should own the entire network. As the commercial potential of networking technologies made nongovernment participants willing to invest, and as the growth of the Internet made it possible to bypass any single participant, there were no longer any indispensable participants. As predicted by Corollary 11.1, it was now optimal to move away from sole ownership.

## 4. An Illustration

In this section we illustrate the practical applicability of our approach by using the theory and the specialized functional form introduced in §2 and 3 to analyze security investments in a network with three network participants and four assets. Although this is a highly stylized example, it illustrates several features of investments in security, such as the diminishing returns as achieving higher security becomes increasingly difficult; the interdependence of security measures; and the externalities as the effectiveness of investments in any part of the network is affected by investments in other parts. Within the context of this example, we demonstrate how different ownership structures can be compared.

## 4.1. Setting, Notation, and Definitions

Consider a setting with three network participants, $y_{1}$ , $y_{2}$ , and $y_{3}$ , and four assets, $a_{1}$ , $a_{2}$ , $a_{3}$ , and $a_{N}$ . Assets $a_{1}$ , $a_{2}$ , and $a_{3}$ , the “user” assets, represent the software and hardware assets necessary to make a user site operational, such as server hardware and software and the network access hardware. Asset $a_{N}$ , the “network” asset, represents the network switches and associated software that enable the network to function. This setting is depicted in Figure 1.

Participant investments $x_{i}$ (i = 1, 2, 3) represent investments in increased security, as represented by the security performance of each participant's location as a fraction of "perfect" security (i.e., $0 \leq x_{i} \leq 1$ , where $x_{i} = 0$ represents no security at all, and $x_{i} = 1$ represents perfect security at site $y_{i}$ ). These levels of security can be achieved through expenses such as improvements in security procedures, investments in corporate firewalls, implementation of security standards such as public key encryption, and increased use of network security protocols. The ownership structure $\alpha$ determines whether each coalition S of participants ( $S \subseteq \{y_{1}, y_{2}, y_{3}\}$ ) owns or does not own asset $a_{i}$ (i = 1, 2, 3, N). Without loss of generality, we normalize the $a_{i}$ 's by setting $a_{i} = 1$ if coalition S owns asset $a_{i}$ , otherwise setting $a_{i} = 0$ . We assume the cost of investments in security by participant $y_{i}$ is

$$
c _ {i} (x _ {i}) = c (x _ {i}) = \frac {b}{(1 - x _ {i}) ^ {2}} - b.
$$

This cost function demonstrates the diminishing returns of security investments and the fact that one can never achieve a level of security better than 100%, and is also consistent with Assumption 1 (H&M). Investment payoffs are given by

$$
\begin{array}{c} \nu_ {i} (S, A | \mathbf {x}) = \gamma_ {i} (A) \sum_ {j = 1} ^ {3} \mu_ {i j} x _ {j} ^ {1 / 2} x _ {i} ^ {1 / 2}, \\ \text {where} \gamma_ {i} (A) = \sum_ {n | a _ {n} \in A} \lambda_ {i n} a _ {n}. \end{array}
$$

Interpretation of payoffs. Recall from our functional form that $\lambda_{in}$ scales the impact of asset $a_{n}$ on the payoffs realized by participant $y_{i}$ . If $y_{i}$ 's value is heavily influenced by access to asset $a_{1}$ , moderately influenced by access to the network asset $a_{N}$ , and is not influenced by access to the assets of other participants, then $\lambda_{11}$

Figure 1 Network with Three Participants and Four Assets.  
![](/api/attachments/6E6WMGVM/fulltext/images/5c3dae1ad405541e2300a189d3b7f2c09c45470710d15daa9a613476a0a8d82c.jpg)  
will be large, $\lambda_{1N}$ will have a medium value, while $\lambda_{12}$ and $\lambda_{13}$ will be very small or zero. For example, $y_{1}$ , $y_{2}$ and $y_{3}$ could be banks with local electronic assets $a_{u}$ , and $a_{N}$ could be a shared network asset for electronic funds transfers. If these banks do many local transactions, then $\lambda_{u}$ will be large. If $y_{1}$ and $y_{2}$ do business with each other, then $\lambda_{1N}$ , $\lambda_{2N}$ , $\lambda_{12}$ and $\lambda_{21}$ will be strictly positive. If banks $y_{1}$ and $y_{3}$ do no business with each other, then $\lambda_{13}$ and $\lambda_{31}$ could be very small or zero.

The $\mu_{ij}$ 's scale the impact of $y_{j}$ 's investment on the payoffs realized by $y_{i}$ . In our previous example, if bank $y_{1}$ 's customers visit $y_{2}$ 's territory and retrieve funds, $y_{2}$ 's investment in security affects $y_{1}$ 's payoffs, and thus $\mu_{12}$ is likely to be high. If few of bank $y_{2}$ 's customers reciprocate by visiting bank $y_{1}$ 's territory, then the impact of $y_{1}$ 's investment on $y_{2}$ is low, and the corresponding coefficient $\mu_{21}$ is likely to be small or zero.

Ownership Structures. The apparatus introduced so far allows us to compare the impact of alternative ownership structures on investments. Proposition 1 (H&M) states there will always be underinvestment, and thus if a given ownership structure results in higher investments, then it is more desirable as this guarantees higher private and social payoffs. To illustrate our approach, we consider the following five ownership possibilities in the above setting:

D: Decentralized ownership: In this structure, $y_{i}$ controls the corresponding asset $a_{i}$ , and simple majority is required to control $a_{N}$ .

DN: Decentralized ownership with consensus for the network asset: $y_{i}$ controls the corresponding asset $a_{i}$ , and all three participants must cooperate to control $a_{N}$ .

M: Majority rule over all assets: A simple majority

of participants is required to control any asset.

N: Consensus rule: All three participants must cooperate to control any asset.

$C_{1}$ : Centralized ownership by $y_{1}$ : Any coalition that includes $y_{1}$ controls all assets. $C_{2}$ and $C_{3}$ are similarly defined as centralized ownership by $y_{2}$ and $y_{3}$ , respectively.

For example, D and DN correspond to a setting where each participant is in charge of administering security procedures on its own site, but network standards are determined in a committee requiring either a simple majority (D) or consensus (DN) to implement a decision. M and N correspond to a setting where security requirements at each site, and network standards are decided in a committee requiring a simple majority or consensus for implementation. Under $C_{1}$ , $y_{1}$ is the dominant network participant and determines all security requirements and network standards.

## 4.2. Ownership Structures and Investment Levels

Having defined the possible ownership structures, we can now determine the relative investment levels. Because investment costs are the same across ownership structures, we need only compute the first order conditions (FOCs), $B_{i}^{t}(\alpha \mid \mathbf{x})$ (i = 1, 2, 3), for each ownership structure $\alpha$ . Since these FOCs determine the incentives for investment, an ownership structure that yields a set of FOCs that dominate the FOCs from a second ownership structure, will result in higher investments than the second ownership structure. The first order conditions for the different ownership structures are given in Appendix 3.

The decentralized ownership structure, D, weakly dominates decentralized ownership with consensus, DN, and the dominance is strict if

$$
\begin{array}{r l} & {\frac {1}{3} \lambda_ {1 N} a _ {N} [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ]} \\ & {+ \frac {1}{6} \lambda_ {2 N} a _ {N} (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) + \frac {1}{6} \lambda_ {3 N} a _ {N} (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) > 0} \end{array}
$$

(or the corresponding inequalities for $B_{2}^{2}$ or $B_{3}^{3}$ ). Moreover, the dominance becomes stronger as $a_{N}$ becomes important to more participants, i.e., as $\lambda_{iN}$ becomes large for all participants (i = 1, 2, 3). It can similarly be shown that majority rule, M, strictly dominates consensus, N. The consensus-based ownership structures are dominated by ownership structures that only require a majority to control assets, because the latter allow certain coalitions to control more assets. For example, decentralized ownership, D, allows coalitions other than the grand coalition to control the network asset $a_{N}$ .

Undominated Ownership Structures. We focus the remainder of this discussion on the undominated ownership structures, D, M, and $C_{i}$ (i = 1, 2, 3).

Let $\bar{B}_i^i$ denote the difference in incentives between majority rule M and decentralized ownership D, i.e., $\bar{B}_i^i = B_i^i (M|\mathbf{x}) - B_i^i (D|\mathbf{x})$ . This difference is:

$$
\begin{array}{r l} & {\bar {B} _ {1} ^ {1} = \left[ - \frac {1}{3} \lambda_ {1 1} a _ {1} + \frac {1}{6} \lambda_ {1 2} a _ {2} + \frac {1}{6} \lambda_ {1 3} a _ {3} \right]} \\ & {\qquad \cdot \left[ \mu_ {1 1} + \frac {1}{2} \Big (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2} \Big) x _ {1} ^ {- 1 / 2} \right]} \\ & {\qquad + \frac {1}{6} \lambda_ {2 3} a _ {3} \Big (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2} \Big) + \frac {1}{6} \lambda_ {3 2} a _ {2} \Big (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2} \Big),} \end{array}
$$

with corresponding derivations for $\bar{B}_2^2$ and $\bar{B}_3^3$ .

If $\lambda_{12} + \lambda_{13} > \lambda_{11}$ , $\lambda_{21} + \lambda_{23} > \lambda_{22}$ and $\lambda_{31} + \lambda_{32} > \lambda_{33}$ , then M dominates D. In other words, if $y_2$ and $y_3$ can together get more marginal product out of $a_1$ than $y_1$ can, and similar conditions hold for $a_2$ and $a_3$ , then M dominates D. This is because decentralized ownership gives too much control to $y_t$ over $a_t$ in a situation where more than half of $a_t$ 's marginal product is realized by other participants. Alternatively, if $\lambda_{ij} = 0$ for $i = 1, 2, 3$ ; $j = 1, 2, 3, N$ ; and $i \neq j$ , then decentralized ownership dominates majority rule as only participant $y_t$ can get marginal product from asset $a_t$ .

Referring to our network security example, if the expertise needed to increase the security of the user assets is not specific to the corresponding participants, then majority rule would yield greater investments in security. This is because all coalitions with a majority of participants will get greater marginal product from each asset. Alternatively, if this expertise is specific to the participant corresponding to each asset, i.e., only $y_{i}$ can get marginal product from $a_{i}$ , then decentralized ownership would be optimal.

Now let $\hat{B}_i^i$ denote the difference in incentives between the centralized and decentralized ownership structures $C_1$ and $D$ , i.e., $\hat{B}_i^i = B_i^i (C_1|\mathbf{x}) - B_i^i (D|\mathbf{x})$ .

These differences are:

$$
\begin{array}{r l} \hat {B} _ {1} ^ {1} = & \left[ \frac {1}{2} \lambda_ {1 2} a _ {2} + \frac {1}{2} \lambda_ {1 3} a _ {3} + \frac {1}{3} \lambda_ {1 N} a _ {N} \right] \\ & \cdot \left[ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} \right] \\ & + \frac {1}{3} \lambda_ {2 3} a _ {3} \Bigl (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2} \Bigr) \\ & + \frac {1}{3} \lambda_ {3 2} a _ {2} \Bigl (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2} \Bigr), \end{array}
$$

$$
\begin{array}{r l} \hat {B} _ {2} ^ {2} = & \frac {1}{3} \lambda_ {1 3} a _ {3} \bigg (\frac {1}{2} \mu_ {1 2} x _ {1} ^ {1 / 2} x _ {2} ^ {- 1 / 2} \bigg) \\ & - \bigg [ \frac {1}{2} \lambda_ {2 3} a _ {3} + \frac {1}{6} \lambda_ {2 N} a _ {N} \bigg ] \\ & \cdot \bigg [ \mu_ {2 2} + \frac {1}{2} (\mu_ {2 1} x _ {1} ^ {1 / 2} + \mu_ {2 3} x _ {3} ^ {1 / 2}) x _ {2} ^ {- 1 / 2} \bigg ] \\ & - \bigg [ \frac {1}{6} \lambda_ {3 2} a _ {2} + \frac {1}{6} \lambda_ {3 3} a _ {3} + \frac {1}{6} \lambda_ {3 N} a _ {N} \bigg ] \\ & \cdot \left(\frac {1}{2} \mu_ {3 2} x _ {3} ^ {1 / 2} x _ {2} ^ {- 1 / 2}\right), \end{array}
$$

and

$$
\begin{array}{r l} \hat {B} _ {3} ^ {3} = & \frac {1}{6} \lambda_ {1 2} a _ {2} \biggl (\frac {1}{2} \mu_ {1 3} x _ {1} ^ {1 / 2} x _ {3} ^ {- 1 / 2} \biggr) \\ & - \biggl [ \frac {1}{6} \lambda_ {2 2} a _ {2} + \frac {1}{6} \lambda_ {2 3} a _ {3} + \frac {1}{6} \lambda_ {2 N} a _ {N} \biggr ] \\ & \cdot \biggl (\frac {1}{2} \mu_ {2 3} x _ {1} ^ {1 / 2} x _ {3} ^ {- 1 / 2} \biggr) \\ & - \biggl [ \frac {1}{2} \lambda_ {3 3} a _ {3} + \frac {1}{6} \lambda_ {3 N} a _ {N} \biggr ] \\ & \cdot \biggl [ \mu_ {3 3} + \frac {1}{2} (\mu_ {3 1} x _ {1} ^ {- 1 / 2} + \mu_ {3 2} x _ {2} ^ {1 / 2}) x _ {3} ^ {- 1 / 2} \biggr ]. \end{array}
$$

If $\mu_{11}, \mu_{12}, \mu_{13} \geq 0$ with at least one of the three strictly positive, and $\mu_{2i} = \mu_{3i} = 0$ for i = 1, 2, 3, then $C_{1}$ dominates D. Alternatively, if $\lambda_{11}, \lambda_{22}, \lambda_{33} > 0$ and either $\lambda_{12} = \lambda_{13} = \lambda_{1N} = \mu_{21} = \mu_{31} = 0$ or $\lambda_{12} = \lambda_{13} = \lambda_{1N} = \lambda_{23} = \lambda_{32} = 0$ , then D dominates $C_{1}.^{11}$

A centralized ownership structure dominates if the marginal contribution of any participant's investment to either of the noncontrolling participants is zero. That

$^{11}$ Notice that if $\lambda_{22} = \lambda_{33} = \lambda_{23} = \lambda_{32} = \lambda_{2N} = \lambda_{3N} = 0$ , then $C_{1}$ dominates D. Thus, a sufficient condition for $C_{1}$ to dominate D can be derived either from the relationships between assets and participants ( $\lambda'$ s), or from the relationships between cross-productivity of participant investments ( $\mu'$ s).

is, if there are no investment externalities to noncontrolling participants, then centralized ownership is better than decentralized ownership. Decentralized ownership is dominant over centralized control by $y_{1}$ , if $y_{1}$ 's value is not increased by the presence of other user or network assets and either $y_{1}$ 's investments do not contribute to the other participants' value, or there is no contribution of $a_{3}$ on $y_{2}$ 's value and vice versa.

Comparing $C_{1}$ and M, let $\tilde{B}_{t}^{i}$ denote the difference in incentives between these two ownership structures, i.e., $\tilde{B}_{t}^{i} = B_{t}^{i}(C_{1} | \mathbf{x}) - B_{t}^{i}(M | \mathbf{x})$ . These differences are:

$$
\begin{array}{r l} & {\tilde {B} _ {1} ^ {1} = \frac {1}{3} (\lambda_ {1 1} a _ {1} + \lambda_ {1 2} a _ {2} + \lambda_ {1 3} a _ {3} + \frac {1}{3} \lambda_ {1 N} a _ {N})} \\ & {\qquad \cdot \bigg [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} \bigg ],} \end{array}
$$

$$
\begin{array}{r l} \tilde {B} _ {2} ^ {2} = & - \frac {1}{6} [ \lambda_ {2 1} a _ {1} + \lambda_ {2 2} a _ {2} + \lambda_ {2 3} a _ {3} + \lambda_ {2 N} a _ {N} ] \\ & \cdot \left[ \mu_ {2 2} + \frac {1}{2} (\mu_ {2 1} x _ {1} ^ {1 / 2} + \mu_ {2 3} x _ {3} ^ {1 / 2}) x _ {2} ^ {- 1 / 2} \right] \\ & - \frac {1}{6} [ \lambda_ {3 1} a _ {1} + \lambda_ {3 2} a _ {2} + \lambda_ {3 3} a _ {3} + \lambda_ {3 N} a _ {N} ] \Bigl (\frac {1}{2} \mu_ {3 2} x _ {3} ^ {1 / 2} x _ {2} ^ {- 1 / 2} \Bigr), \end{array}
$$

$$
\begin{array}{r l} \tilde {B} _ {3} ^ {3} = & - \frac {1}{6} [ \lambda_ {2 1} a _ {1} + \lambda_ {2 2} a _ {2} + \lambda_ {2 3} a _ {3} + \lambda_ {2 N} a _ {N} ] \\ & \cdot \left(\frac {1}{2} \mu_ {2 3} x _ {1} ^ {1 / 2} x _ {3} ^ {- 1 / 2}\right) \\ & - \frac {1}{6} [ \lambda_ {3 1} a _ {1} + \lambda_ {3 2} a _ {2} + \lambda_ {3 3} a _ {3} + \lambda_ {3 N} a _ {N} ] \\ & \cdot \left[ \mu_ {3 3} + \frac {1}{2} (\mu_ {3 1} x _ {1} ^ {1 / 2} + \mu_ {3 2} x _ {2} ^ {1 / 2}) x _ {3} ^ {- 1 / 2} \right]. \end{array}
$$

If $\lambda_{1j} = 0 (j = 1,2,3,N)$ , or $\mu_{1i} = 0 (i = 1,2,3)$ , then M dominates $C_1$ . If $\lambda_{2j} = \lambda_{3j} = 0 (j = 1,2,3,N)$ or $\mu_{2i} = \mu_{3i} = 0 (i = 1,2,3)$ , then $C_1$ dominates M.

This comparison is the most extreme. Majority rule is guaranteed to dominate if either $y_{1}$ 's value is not affected by the presence of any assets, or if it is not affected at the margin by any participant's investment, including $y_{1}$ 's own investment. Centralized ownership is guaranteed to dominate only if either one of these conditions is true for the other participants.

## 4.3. Implications for Network Ownership

We have illustrated how in this stylized example certain ownership structures are suboptimal as they are strictly dominated, while the desirability of other ownership structures is determined by the specific characteristics of the underlying network setting. For example, asset control based on consensus rule is undesirable, as it results in lower overall investments in security. This suggests that de facto security standards are likely to attract more investment, and thus become more successful, than standards recommended by committees operating on consensus principles.

Similarly, when security in a network is determined by the security of its weakest link, this gives any participant that controls some network asset a “veto” on the effectiveness of security investments, effectively imposing a consensus control structure as far as security is concerned. Consequently such networks are likely to be characterized by lower investments in security than networks with centralized ownership. This provides a possible explanation for the lack of security investments in the public Internet infrastructure, compared to centrally owned value-added networks (VANs) or corporate networks.

## 5. Discussion and Conclusions

## 5.1. Externalities and Consolidation

If an industry is characterized by positive network, marginal network, and investment network externalities, then a single industry system maximizes total welfare. In other words, all firms in that industry should participate in a single system or coalition of systems. These positive externalities are common in electronic networks. As a result, recent years have seen significant consolidation among electronic networks, with many industries settling on a single system encompassing several firms with competing products and services. Even those industries that are not dominated by a single industry network have moved toward fewer systems. Examples include airline CRS, commercial fueling, automotive dismantlers, drugstore wholesaling, retail banking, and hospital suppliers. Positive externalities are also at the heart of the increasing movement toward using the Internet as the infrastructure underlying applications in these and several more areas.

The trend toward consolidation need not eliminate competition among systems. Competing subnetworks that are mutually interconnected and compatible may still emerge, as is the case with bank automated teller machine (ATM) networks. These compatibility features will help realize the positive network externalities, while competition can still take place based on dimensions such as price and service. The setting of our model and our use of the Shapley value mechanism are not directly applicable to this scenario of competing compatible subnetworks, however. It is possible, for example, that competition between compatible subnetworks creates more value than the grand coalition because of factors outside our model, such as fostering more innovation or avoiding diseconomies of scale in administration. Although our ownership results may still be applicable within individual subnetworks, this observation likely accounts for the emergence of competing electronic networks in several real world markets, instead of the “grand coalition” network that is optimal in our setting.

## 5.2. Network-Specific Investments

Once an electronic network emerges in an industry, the value produced depends on the incentives of individual participants to make specific investments in assets increasing the productivity of the network, such as network facilities, human capital or organizational processes. When network-specific investments cannot be efficiently contracted, the ownership of network assets determines the ex-post bargaining power of individual network participants, the corresponding division of the network payoffs, and the resulting ex-ante incentives to make noncontractible network specific investments. We have shown that the resulting second-best outcome is typically maximized under arrangements that give ownership of network assets to the participants that have the most important noncontractible investments. This is different from saying that the participants with the most important investments should own the network.

Investments in electronic networks are likely to be noncontractible, especially investments in human capital or organizational processes. In the case of ASAP Express, for example, complete contractual arrangements for investments in human capital or organizational processes would require: (1) specification of the appropriate level and type of investment for each hospital, hospital supplier, and intermediary participating in the system under all possible future states of the economy; (2) verification of which state of the economy actually occurred and what benefits the system participants realized as a result; and (3) the ability to monitor and verify ASAP-specific investments by each system participant. Not only it is unlikely that all contingencies required under condition (1) can be specified, but it is also improbable that a hospital or a hospital supplier would agree to the mechanisms necessary to implement conditions (2) and (3), as this would require disclosure and auditing of internal cost and investment records. For example, the reluctance of hospital suppliers to comply with condition (2) is demonstrated by their insistence to include in the design of ASAP Express controls that preclude any participating supplier, and especially Baxter, from accessing other suppliers' transactions on the system.

## 5.3. Dispensability

Proposition 5 suggests that participants to an electronic network should own the idiosyncratic parts of their corresponding networks, such as on-premises hardware and software, as long as these assets affect only their individual productivity. This may not have been the case historically because of the presence of intermediaries or system providers who were indispensable to the entire network, and thus owned all network assets. With increasing standardization and increasing sophistication on the part of network participants, however, we would expect intermediaries to lose some of their indispensability, as is clearly happening with the providers of Internet service and infrastructure. For instance, the network services provided at the communications interface are increasingly becoming standardized, and when sophisticated organizations purchase their on-premises systems they can often anticipate and specify the network services they will need, and choose among several providers in procuring these services. This may prevent intermediaries from being indispensable and may result in individual participants owning their idiosyncratic assets, much as the breakup of the Bell System's monopoly has led most customers to own their on-premises telecommunications hardware.

The distributed ownership structure of the Internet has been key to its flexibility and growth; it would be neither desirable nor feasible to centralize ownership of such a diverse network. In this context, the unparalleled success of the Internet has been assisted by the fact that its only essential assets seem to be its underlying standards. The only parties indispensable to these standards have been non-governmental and non-corporate bodies such as the Internet Engineering Task Force, which have successfully maintained behavior fitting a social planner maximizing social welfare rather than a self-interested economic agent.

The early single-ownership arrangements in IOS such as the SABRE CRS or the ASAP hospital supply system are consistent with the fact that the owners of such systems, American Airlines and the former American Hospital Supply Corporation (AHSC), were indispensable and the only participant with an investment decision in the early stages of IOS evolution. For example, AHSC had unique management, logistical, and IT skills that were indispensable to the creation of ASAP.

With ASAP Express, which offers multivendor capabilities and includes GEISCO as a participant with network expertise, Baxter is no longer likely to be the only indispensable participant. Other participants' network-specific investments are likely to be lower than first-best. For example, a hospital may underinvest in system-specific organizational processes to integrate ASAP Express into its operations, since part of the value created will be lost to Baxter, possibly through user fees or higher prices for the supplies purchased using the system. If this is the case, to maximize the total surplus ASAP Express should evolve towards some form of joint ownership.

A similar trend is demonstrated by the evolution of ownership in airline CRS. In the early days of CRS introduction, it was typical to find essential assets, such as the reservations software and the switching, network, and central database hardware, and an indispensable participant, typically the developer and operator of the system. From Propositions 6 and 8, the indispensable participant should own the entire system, as was the case, for example, with American Airlines owning SABRE. As the expertise necessary to operate a CRS becomes more broadly available, there may no longer be a single indispensable participant. Corollary 11.1 predicts that the optimal evolution in this case is a move to joint ownership, as has been the case with Covia's Apollo CRS where an alliance of key participants owns all system assets, including the equipment at the premises of individual travel agents.

Perhaps the most important contribution of our model is the prediction that the major force underlying the evolution of ownership structures is the indispensability of network participants. Thus, as historically leading network participants become less indispensable, their systems are likely to move towards some form of joint ownership. Our analysis shows that in this case cooperation in the form of joint ownership is economically efficient. System participants could continue to compete on attributes such as price and quality, while customers benefit from their increased investments in the system. Safeguards may be necessary, however, to assure that exploiting the benefits of joint ownership does not lead to collusion in other areas, and especially pricing. $^{12}$

## 5.4. Conclusions

In this article we used the theory of incomplete contracts to formalize the ownership of network assets in an electronic network. Following the H&M framework, we focused on modeling the importance of network-specific noncontractible investments. In our setting, positive externalities make the formation of a "grand coalition" desirable. The exact partition of the resulting surplus is sensitive to the assumed bargaining model and institutional arrangements; the basic results, however, are robust in most reasonable settings.

Direct application of H&M's propositions yielded the following results for an electronic network:

\- All network participants underinvest in network-specific capital.

\- If only one participant, for instance the intermediary, has a network-specific investment, then that participant should own all network assets.

\- If an asset such as a customized network interface is idiosyncratic to a network participant, then it should be owned by that participant. If a participant is indispensable to an asset, then the asset should be owned by that participant.

We also derived a new set of propositions that produced the following results:

\- If one or more assets are essential to all network participants, then all the assets should be owned together. Thus, if the centralized network software is an essential asset, then it should be owned together with all the peripheral assets. With at least one asset essential to all participants, full integration of ownership dominates the separate ownership of individual assets.

\- If a network participant is indispensable to an asset that is essential to all participants, then the indispensable participant should own all network assets. Thus, if only one participant has the expertise to operate the centralized network software, that participant should own all other network assets as well.

\- In the case of three mutually important network participants, joint ownership with equal shares dominates sole ownership as it results in higher network investments and total value. This is due to the marginal network externalities and the investment externalities.

\- With mutually important participants, unbalanced joint ownership dominates sole ownership. Therefore, in the absence of an indispensable network participant, and as long as value is created through interorganizational efficiencies (and thus requires the cooperation of at least two participants), the control structure should always be some form of joint ownership.

Our last result, in particular, gives predictive power to our analysis: as leading network participants become more dispensable, we should see an evolution toward networks that are controlled by some form of joint ownership.

Finally, we provided an easily interpretable functional form, tailored to the Internet, for expressing the value generated from a coalition of network participants. This functional form satisfies the general assumptions used by H&M, and we showed how it can accommodate H&M's definitions of an idiosyncratic asset and an indispensable participant, as well as our definitions of an essential asset and mutually important participants. We used this form in a setting with three participants, three site assets, and one network asset, to show how different ownership structures can be compared. Within this setting, we derived conditions under which either centralized, decentralized or majority rule ownership resulted in the highest participant investments.

We conclude by pointing out that the incomplete contracting framework employed here can be used for a normative analysis of ownership in a given electronic network, if the values of the alternative coalitions can be analytically specified or estimated in some other way. The methodology followed in the proofs of the propositions in §2 and 3 can be employed to compare alternative ownership structures, and thus determine the one that will result in the highest net surplus. Future research in this area should focus on the specification of system payoffs under different coalitions of network participants and different levels of network-specific investments. $^{13}$

$^{13}$ The authors gratefully acknowledge the helpful comments and suggestions of the Associate Editor and three anonymous referees, and the participants of the Third Workshop on Information Systems and Economics (1991) in New York City. Partial support for this research was provided to the first author by the National Science Foundation and to the second author by the Social Sciences and Humanities Research Council of Canada and the Natural Sciences and Engineering Research Council of Canada.

Appendix 1: H&M Assumptions in the Context of Electronic Networks

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ASSUMPTION 1 (H&amp;M).  
$c_{t}(x_{t}) \geq 0, c_{t}(0) = 0$ $c_{t}$ is twice differentiable  
If $\bar{x}_{t} &gt; 0$, then $c_{t}'(x_{t}) &gt; 0$ and $c_{t}''(x_{t}) &gt; 0$, with $\lim_{x_{t} \to 0} c_{t}'(x_{t}) = 0$ and $\lim_{x_{t} \to \bar{x}_{t}} c_{t}'(x_{t}) = \infty$.
</div>

This standard assumption states that the cost of investment is increasing and convex and ensures that optimal investment is interior where relevant.

ASSUMPTION 2 (H&M). For all A ⊆ A,

$\nu (\emptyset ,A|\mathbf{x}) = 0$ and $\nu (S,A|\mathbf{x})\geq 0$ for all $\mathbf{x}$

$\nu (S,A|\mathbf{x})$ is twice differentiable in $x_{\nu}$ ;

If $\bar{x}_i > 0$ , then $\nu^i(S, A \mid \mathbf{x}) \geq 0$ for $x_i \in (0, \bar{x}_i)$ ;

$\nu(S, A | x)$ is concave in $x_{i}$ .

Assumption 2 states that the value of a network with at least one participant is nonnegative and that positive investment in network-specific human capital yields nondecreasing, although diminishing, returns. This assumption ensures that network investments are valuable.

Assumption 3 (H&M).

$$
\nu^ {i} (S, A \mid \mathbf {x}) = 0 i f i \notin S, A \subseteq \underline {{A}}.
$$

Assumption 3 ensures that marginal investments by nonparticipants do not affect the value of the network, although they may

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 4, December 1997

enhance their own productivity. $^{14}$ For example, investments in networks not connected to the Internet are unlikely to affect the value generated by the Internet.

ASSUMPTION 4 (H&M).

$$
\frac {\partial}{\partial x _ {j}} \nu^ {i} (S, A | \mathbf {x}) \geq 0 \text {   for   all   } j \neq i, A \subseteq \underline {{A}}.
$$

This assumption provides for investment externalities, i.e., complementarities in marginal investments by different participants. As a result of these externalities, marginal network return on investment by any individual participant increases as investments by other participants increase. For example, when certain Internet bandwidth providers make a network-specific investment such as better routing software, the full benefit of this investment may not be realized until the new technology is adopted throughout the network. In such cases, investment by certain network participants raises the attractiveness of complementary investments by other participants.

ASSUMPTION 5 (H&M). For all subsets $S' \subseteq S$ and $A' \subseteq A \subseteq \underline{A}$ , $\nu(S, A | \mathbf{x}) \geq \nu(S', A' | \mathbf{x}) + \nu(S \setminus S', A \setminus A' | \mathbf{x})$

This assumption ensures network externalities, i.e., the increase in network value from the addition of one participant or asset is greater than the value of that participant or asset alone; in other words, network returns display superadditivity in the number of their participants and assets. In the Internet, interconnecting two computer networks increases their total value by allowing members of each network to access members of the other network. $^{14}$

ASSUMPTION 6 (H&M). For all subsets $S' \subseteq S$ and $A' \subseteq A \subseteq A \subseteq \underline{A}$ , $\nu'(S, A | \mathbf{x}) \geq \nu'(S', A' | \mathbf{x})$

This assumption provides for marginal network externalities, i.e., the marginal network return from investment by any individual participant increases with the number of participants and assets: there is marginal superadditivity in agents and assets. For instance, incremental investments in network expertise, know-how, or promotion have a larger payoff in a network with a larger number of participants or a larger number of assets. Because a larger system is more attractive, additional promotion will result in more new customers; similarly an improvement in network software and operations creates more value in a larger network. Thus, as the Internet grows, developing better network management software becomes more attractive, as its impact is leveraged over larger volumes of traffic.

ASSUMPTIONS 1–6 IN OUR FUNCTIONAL FORM. Assumption 1 is satisfied as

$$
c (0) = \frac {b}{\bar {x} ^ {2}} - \frac {b}{\bar {x} ^ {2}} = 0, c ^ {\prime} \left(x _ {t}\right) = \frac {2}{\left(\bar {x} - x _ {t}\right) ^ {3}} > 0 \quad \text { for } 0 \leq x _ {t} <   \bar {x},
$$

$^{14}$ We focus on network-specific investments whose returns cannot be realized unless the agent participates in the network. The inability to write complete contracts is less sanguine in the case of investments without high specificity to the network assets; the existence of alternative valuable uses for such investments allows the corresponding agents to fully realize their marginal returns, thus alleviating the underinvestment problem.

$^{15}$ This synergy is similar to the positive network externalities discussed by Katz and Shapiro (1985).

$c''(x_i) = 6 / (\bar{x} - x_i)^4 > 0$ , and at the limit as $x \to \bar{x}$ all derivatives of $c(x)$ go to infinity. Assumption 2 is satisfied from Equation (1), while

$$
\begin{array}{r l} \nu^ {i} (S, A | \mathbf {x}) = & - \frac {1}{4} x _ {i} ^ {- 3 / 2} \bigg (\sum_ {n | a _ {n} \in A} \lambda_ {i n} a _ {n} \bigg) \Bigg (\sum_ {\substack {k \in S \\ k \neq i}} \mu_ {i k} x _ {k} ^ {1 / 2} \Bigg) \\ & - \frac {1}{4} x _ {i} ^ {- 3 / 2} \sum_ {\substack {l \in S \\ l \neq i}} \bigg [ \bigg (\sum_ {n | a _ {n} \in A} \lambda_ {l n} a _ {n} \bigg) \mu_ {i l} x _ {l} ^ {1 / 2} \bigg ] \leq 0. \end{array}
$$

Assumption 3 is trivially satisfied because if $i \notin S$ , then $x_{i}$ does not appear in $\nu(S, A | \mathbf{x})$ . Assumption 4 is satisfied because if $j \in S$ ( $j \neq i$ ), then

$$
\begin{array}{r l} \frac {\partial}{\partial x _ {j}} \nu^ {\prime} (S, A | \mathbf {x}) & = \bigg (\sum_ {n \mid a _ {n} \in A} \lambda_ {i n} a _ {n} \bigg) \frac {1}{2} x _ {i} ^ {- 1 / 2} \mu_ {i j} x _ {i j} ^ {1 / 2} \\ & + \bigg (\sum_ {n \mid a _ {n} \in A} \lambda_ {j n} a _ {n} \bigg) \frac {1}{2} x _ {i} ^ {- 1 / 2} \mu_ {i j} x _ {j} ^ {1 / 2}, \end{array}
$$

which is nonnegative for all $j \neq i$ and $A \subseteq T$ . Assumption 5 is satisfied because of the two-term cross products in the value function. In particular, $\nu(S, A | x)$ includes all terms in $\nu(S', A' | x)$ , all terms in $\nu(S \setminus S', A \setminus A' | x)$ , and in addition more non-negative cross products. Assumption 6 is satisfied because if $i \notin S'$ , then $\nu'(S', A' | x) = 0$ , and if $i \notin S$ , adding more agents to S or more assets to A increases the number of terms in the sums defining $\nu'(S, A | x)$ , all of which terms are nonnegative.

## Appendix 2: Proofs of Propositions

PROOF OF PROPOSITION 3. Consider agent $j \neq i$ . Then, using Equation (1), the difference in $\nu(S, A | \mathbf{x})$ when $a_T$ is removed from $A$ is

$$
\begin{array}{l}\lambda_{jT}a_{T}\Bigg(\frac{1}{2} x_{j}^{-1 / 2}\sum \liminfits_{\substack{k\in S\\ k\neq j}}\mu_{jk}x_{k}^{1 / 2} + \mu_{jj}\\ \\ +\Bigg(\sum \liminfits_{\substack{k\in S\\ k\neq j}}\lambda_{jT}a_{T}\Bigg)\frac{1}{2} x_{j}^{-1 / 2}\mu_{jk}x_{k}^{1 / 2}. \end{array}
$$

If $\lambda_{jT} = 0$ for $j \neq i$ , the first term is zero, while the second term reduces to $\lambda_{iT} a_T \frac{1}{2} x_j^{-1/2} \mu_j x_l^{1/2}$ ; this is also zero if $\mu_j = 0$ for $j \neq i$ .

PROOF OF PROPOSITION 4. Similar to the case of an idiosyncratic asset, for any agent $j \neq i$ , the difference in $\nu(S, A|x)$ when $a_T$ is removed from $A$ is

$$
\begin{array}{l}\lambda_{jT}a_{T}\Bigg(\frac{1}{2} x_{j}^{-1 / 2}\sum_{\substack{k\in S\\ k\neq j}}\mu_{jk}x_{k}^{1 / 2} + \mu_{jj}\\ \\ +\Bigg(\sum_{\substack{k\in S\\ k\neq j}}\lambda_{jT}a_{T}\Bigg)\frac{1}{2} x_{j}^{-1 / 2}\mu_{jk}x_{k}^{1 / 2}. \end{array}
$$

Since $i \notin S$ , however, both terms are zero if $\lambda_{iT} = 0$ for $j \neq i$ . PROOF OF PROPOSITION 6 when $\lambda_{iT}s$ are "Small Enough." Following H&M's proof of Proposition 6, suppose agent $i$ is indispensable to $a_T$ in the sense that $\lambda_{jT}$ is "small enough." Using our functional form, under H&M's control structure $\alpha$ agent $i$ does not own $a_T$ , but another control structure, H&M's $\hat{\alpha}$ , is the same as $\alpha$ except that agent $i$ does own $a_T$ . The change in marginal return on investment for some agent $j$ is

$$
\sum_{s\mid \begin{array}{c}l_{j}\in S\\ a_{T}\in \alpha (S) \end{array}}p(S)[\nu^{J}(S,A) - \nu^{J}(S,A\setminus \{a_{T}\}) ]\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text{$\mathcal{L}$}
$$

(from H&M, p. 1133). Using (A1), the first summation includes $\lambda_{iT}$ terms, whereas the second summation does not. Thus, if the $\lambda_{iT}$ 's are "small enough" relative to $\lambda_{iT}$ then the change in marginal return on investment is positive, and the proposition holds.

PROOF OF PROPOSITION 7.

$$
\begin{array}{r l} \nu (S, A | \mathbf {x}) & = \sum_ {l \in S} \nu_ {l} (S, A | \mathbf {x}) = \sum_ {l \in S / (i)} \nu_ {l} (S, A | \mathbf {x}) + \nu_ {l} (S, A | \mathbf {x}) \\ & = \sum_ {l \in S / (i)} \left[ \left(\sum_ {n | a _ {n} \in A} \lambda_ {l n} a _ {n}\right) \left(\sum_ {k \in S} \mu_ {l k} x _ {k} ^ {1 / 2}\right) x _ {l} ^ {1 / 2} \right] \\ & \quad + \left(\sum_ {n | a _ {n} \in A} \lambda_ {i n} a _ {n}\right) \left(\sum_ {k \in S} \mu_ {i k} x _ {k} ^ {1 / 2}\right) x _ {i} ^ {1 / 2} \\ & = \nu (S \setminus \{i \}, A | \mathbf {x}) + \sum_ {l \in S \setminus (i)} \left[ \left(\sum_ {n | a _ {n} \in A} \lambda_ {l n} a _ {n}\right) \mu_ {l i} x _ {l} ^ {1 / 2} x _ {i} ^ {1 / 2} \right] \\ & \quad + \left(\sum_ {n | a _ {n} \in A} \lambda_ {i n} a _ {n}\right) \left(\sum_ {k \in S} \mu_ {i k} x _ {k} ^ {1 / 2}\right) x _ {i} ^ {1 / 2}. \end{array}
$$

Thus the change in $\nu^{j}(S, A|x)$ when $i$ leaves coalition $S$ is

$$
\sum_ {n \mid a _ {n} \in A} \frac {1}{2} \lambda_ {j n} a _ {n} u _ {j i} x _ {i} ^ {1 / 2} x _ {j} ^ {- 1 / 2} + \sum_ {n \mid a _ {n} \in A} \frac {1}{2} \lambda_ {i n} a _ {n} u _ {i j} x _ {i} ^ {1 / 2} x _ {j} ^ {- 1 / 2},
$$

which is zero if $\lambda_{m} = 0$ for $n \neq T$ and $\mu_{\mu} = 0$ for $j \neq i$ .

PROOF OF PROPOSITION 8. If there is an asset that is essential to all agents, then every other asset is unproductive unless used together with the essential asset. H&M define two assets as (strictly) complementary if they are unproductive unless they are used together; it follows that all network assets are complementary to the essential asset. Complementary assets should be owned or controlled together from Proposition 8 in H&M. □

PROOF OF PROPOSITION 9. Let $a_T$ be the essential asset. Then $\nu'(S, A \setminus \{a_T\}) \equiv 0$ . If agent $i$ is also indispensable to asset $a_T$ , then (1) agent $i$ should also own asset $a_T$ from Proposition 6; and (2) $\nu'(S \setminus \{i\}, A) \equiv \nu'(S \setminus \{i\}, A \setminus \{a_T\}) \equiv 0$ . Thus no coalition can be worse off by giving agent $i$ control of all the assets.

PROOF OF PROPOSITION 10. Let

$$
x \equiv \mathbf {x} \equiv \left[ \begin{array}{c} x _ {y _ {1}} \\ x _ {y _ {2}} \\ x _ {y _ {3}} \end{array} \right].
$$

Observing that we require at least two participants to give the network additional value, the value of the different coalitions is given by the following:

<table><tr><td>Label</td><td>Coalition</td><td> $\nu(S, \hat{\alpha}(S)/|x)$ </td><td> $\nu(S, \alpha(S)|x)$ </td></tr><tr><td>S1</td><td>{y1, y2}</td><td>+</td><td>+</td></tr><tr><td>S2</td><td>{y1, y3}</td><td>+</td><td>+</td></tr><tr><td>S3</td><td>{y2, y3}</td><td>+</td><td>0</td></tr><tr><td> $\underline{S}$ </td><td>{y1, y2, y3}</td><td>+</td><td>+</td></tr></table>

Defining $g(x; \alpha)$ and $g(x; \hat{\alpha})$ as per proof of H&M Proposition 1, we get

$$
\begin{array}{r l} g (x; \hat {\alpha}) = & p (S _ {1}) \nu (S _ {1}, \hat {\alpha} (S _ {1}) | x) \\ & + p (S _ {2}) \nu (S _ {2}, \hat {\alpha} (S _ {2}) | x) \\ & + p (S _ {3}) \nu (S _ {3}, \hat {\alpha} (S _ {3}) | x) \\ & + p (\underline {{S}}) \nu (\underline {{S}}, \hat {\alpha} (\underline {{S}}) | x) - \sum_ {i = 1} ^ {3} (c _ {i} (x _ {i}) \end{array}
$$

and

$$
\begin{array}{l} g (x; \alpha) = p (S _ {1}) \nu (S _ {1}, \alpha (S _ {1}) | x) + p (S _ {2}) \nu (S _ {2}, \alpha (S _ {2}) | x) \\ \qquad + p (\underline {{S}}) \nu (\underline {{S}}, \alpha (\underline {{S}}) | x) - \sum_ {i = 1} ^ {3} c _ {i} (x _ {i}). \end{array}
$$

Thus,

$$
\begin{array}{r l} & {\nabla g (x, \hat {\alpha}) = \left[ \begin{array}{l} p (S _ {1}) \nu^ {\prime} (S _ {1}, \hat {\alpha} (S _ {1}) | x) + p (S _ {2}) \nu^ {\prime} (S _ {2}, \hat {\alpha} (S _ {2}) | x) + p (\underline {{S}}) \nu^ {\prime} (\underline {{S}}, \underline {{\hat {\alpha}}} (\underline {{S}}) | x) - c _ {y _ {1}} ^ {\prime} (x _ {y _ {1}})} \\ p (S _ {1}) \nu^ {\prime} (S _ {1}, \hat {\alpha} (S _ {1}) | x) + p (S _ {3}) \nu^ {\prime} (S _ {3}, \hat {\alpha} (S _ {3}) | x) + p (\underline {{S}}) \nu^ {\prime} (\underline {{S}}, \underline {{\hat {\alpha}}} (\underline {{S}}) | x) - c _ {y _ {2}} ^ {\prime} (x _ {y _ {2}}) \\ p (S _ {2}) \nu^ {\prime} (S _ {2}, \hat {\alpha} (S _ {2}) | x) + p (S _ {3}) \nu^ {\prime} (S _ {3}, \hat {\alpha} (S _ {3}) | x) + p (\underline {{S}}) \nu^ {\prime} (\underline {{S}}, \underline {{\hat {\alpha}}} (\underline {{S}}) | x) - c _ {y _ {3}} ^ {\prime} (x _ {y _ {3}}) \end{array} \right] \mathrm{and} \\ & {\nabla g (x, \alpha) = \left[ \begin{array}{l} p (S _ {1}) \nu^ {\prime} (S _ {1}, \alpha (S _ {1}) | x) + p (S _ {2}) \nu^ {\prime} (S _ {2}, \hat {\alpha} (S _ {2}) | x) + p (\underline {{S}}) \nu^ {\prime} (\underline {{S}}, \underline {{\hat {\alpha}}} (\underline {{S}}) | x) - c _ {y _ {1}} ^ {\prime} (x _ {y _ {i}})} \\ p (S _ {1}) \nu^ {\prime} (S _ {1}, \alpha (S _ {1}) | x) + p (S) \nu^ {\prime} (S, \alpha (\underline {{S}}) | x) - c _ {y _ {2}} ^ {\prime} (x _ {y _ {2}}) \\ p (S _ {2}) \nu^ {\prime} (S _ {2}, \alpha (S _ {2}) | x) + p (\underline {{S}}) \nu^ {\prime} (\underline {{S}}, \alpha (\underline {{S}}) | x) - c _ {y _ {3}} ^ {\prime} (x _ {y _ {3}}) \end{array} \right], \end{array}
$$

where $\nabla g(x; \alpha)$ is the vector of marginal returns on investment under ownership structure $\alpha$ . Therefore $\nabla g(x; \hat{\alpha}) > \nabla g(x; \alpha)$ , and from Proposition 1 of H&M we get $x^e(\hat{\alpha}) > x^e(\alpha)$ and $W(x^e(\hat{\alpha})) \geq W(x^e(\alpha))$ .

PROOF OF PROPOSITION 11. Define $\alpha$ and $\tilde{\alpha}$ as the control structures representing sole ownership and UJO, respectively. Let $y_{t}$ be the agent controlling the network under sole ownership and the participant with the largest controlling interest under UJO. Because by assumption coalitions with less than two agents have zero value, all coalitions with positive value under $\alpha$ also have positive value under $\hat{\alpha}$ . In addition, the coalition of all agents other than $y_{t}$ has positive value under $\tilde{\alpha}$ while it has zero value under $\alpha$ , i.e.,

$$
\nu (\underline {{{S}}} \backslash \{y _ {i} \}, \tilde {\alpha} (\underline {{{S}}} \backslash \{y _ {i} \}) | \mathbf {x}) > \nu (\underline {{{S}}} \backslash \{y _ {i} \}, \alpha (\underline {{{S}}} \backslash \{y _ {i} \}) | \mathbf {x}) = 0.
$$

Thus, $\nabla g(x; \tilde{\alpha}) > \nabla g(x; \alpha)$ and from Proposition 1 of H&M we get

$$
\mathbf {x} ^ {e} (\tilde {\alpha}) > \mathbf {x} ^ {e} (\alpha) \quad \text { and } \quad W (\mathbf {x} ^ {e} (\tilde {\alpha})) \geq W (\mathbf {x} ^ {e} (\alpha)). \tag * {\square}
$$

Appendix 3: First Order Conditions (FOCs) for Different Ownership Structures

Using the Shapley value for three participants we find that $p(\{y_1\}) = \frac{1}{3}, p(\{y_1, y_2\}) = \frac{1}{6}, p(\{y_1, y_3\}) = \frac{1}{6}$ and $p(\{y_1, y_2, y_3\}) = \frac{1}{3}$ , and thus

$$
\begin{array}{r l} B _ {1} ^ {1} (a \mid \mathbf {x}) = & [ \frac {1}{3} \gamma_ {1} (\{y _ {1} \}) + \frac {1}{6} \gamma_ {1} (\{y _ {1}, y _ {2} \}) \\ & + \frac {1}{6} \gamma_ {1} (\{y _ {1}, y _ {3} \}) + \frac {1}{3} \gamma_ {1} (\{y _ {1}, y _ {2}, y _ {3} \}) ] \\ & \cdot [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ] \\ & + [ \frac {1}{6} \gamma_ {2} (\{y _ {1}, y _ {2} \}) + \frac {1}{3} \gamma_ {2} (\{y _ {1}, y _ {2}, y _ {3} \}) ] (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) \\ & + [ \frac {1}{6} \gamma_ {3} (\{y _ {1}, y _ {3} \}) + \frac {1}{3} \gamma_ {3} (\{y _ {1}, y _ {2}, y _ {3} \}) ] (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \end{array}
$$

with corresponding results for $B_2^2 (\alpha | \mathbf{x})$ and $B_3^3 (\alpha | \mathbf{x})$ .

Deriving the first order conditions for the decentralized ownership structure D, we get:

$$
\begin{array}{r l} B _ {1} ^ {1} (D | \mathbf {x}) = & [ \frac {1}{3} \lambda_ {1 1} a _ {1} + \frac {1}{6} (\lambda_ {1 1} a _ {1} + \lambda_ {1 2} a _ {2} + \lambda_ {1 N} a _ {N}) \\ & + \frac {1}{6} (\lambda_ {1 1} a _ {1} + \lambda_ {1 3} a _ {3} + \lambda_ {1 N} a _ {N}) + \frac {1}{3} \gamma_ {1} (\underline {{S}}) ] \\ & \cdot [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} \\ & + [ \frac {1}{6} (\lambda_ {2 1} a _ {1} + \lambda_ {2 2} a _ {2} + \lambda_ {2 N} a _ {N}) + \frac {1}{3} \gamma_ {2} (\underline {{S}}) ] \\ & \cdot (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) + [ \frac {1}{6} (\lambda_ {3 1} a _ {1} + \lambda_ {3 3} a _ {3} + \lambda_ {3 N} a _ {N}) \\ & + \frac {1}{3} \gamma_ {3} (\underline {{S}}) ] (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \end{array}
$$

or

$$
\begin{array}{r l} B _ {1} ^ {1} (D | \mathbf {x}) = & [ \lambda_ {1 1} a _ {1} + \frac {1}{2} \lambda_ {1 2} a _ {2} + \frac {1}{2} \lambda_ {1 3} a _ {3} + \frac {2}{3} \lambda_ {1 N} a _ {N} ] \\ & [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ] \\ & + [ \frac {1}{2} \lambda_ {2 1} a _ {1} + \frac {1}{2} \lambda_ {2 2} a _ {2} + \frac {1}{3} \lambda_ {2 3} a _ {3} + \frac {1}{2} \lambda_ {2 N} a _ {N} ] \\ & (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) \\ & + [ \frac {1}{2} \lambda_ {3 1} a _ {1} + \frac {1}{3} \lambda_ {3 2} a _ {2} + \frac {1}{2} \lambda_ {3 3} a _ {3} + \frac {1}{2} \lambda_ {3 N} a _ {N} ] \\ & (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \end{array}
$$

with similar derivations for $B_2^2 (D|\mathbf{x})$ and $B_3^3 (D|\mathbf{x})$ .

Under DN (decentralized ownership with consensus for $a_{N}$ ) we get:

$$
\begin{array}{r l} B _ {1} ^ {1} (D N | \mathbf {x}) = & [ \lambda_ {1 1} a _ {1} + \frac {1}{2} \lambda_ {1 2} a _ {2} + \frac {1}{2} \lambda_ {1 3} a _ {3} + \frac {1}{3} \lambda_ {1 N} a _ {N} ] \\ & [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ] \\ & + [ \frac {1}{2} \lambda_ {2 1} a _ {1} + \frac {1}{2} \lambda_ {2 2} a _ {2} + \frac {1}{3} \lambda_ {2 3} a _ {3} + \frac {1}{3} \lambda_ {2 N} a _ {N} ] \\ & (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) \\ & + [ \frac {1}{2} \lambda_ {3 1} a _ {1} + \frac {1}{3} \lambda_ {3 2} a _ {2} + \frac {1}{2} \lambda_ {3 3} a _ {3} + \frac {1}{3} \lambda_ {3 N} a _ {N} ] \\ & (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \end{array}
$$

with corresponding expressions for $B_2^2 (DN|\mathbf{x})$ and $B_3^3 (DN|\mathbf{x})$ .

The first order conditions for majority rule, M, are

$$
\begin{array}{r l} B _ {1} ^ {1} (M | \mathbf {x}) & = \frac {2}{3} \gamma_ {1} (\underline {{S}}) [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ] \\ & + \frac {1}{2} \gamma_ {2} (\underline {{S}}) (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) + \frac {1}{2} \gamma_ {3} (\underline {{S}}) (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \end{array}
$$

with corresponding expressions for $B_2^2 (M|\mathbf{x})$ and $B_3^3 (M|\mathbf{x})$ .

The first order conditions for $C_{1}$ , centralized ownership by $y_{1}$ , are:

$$
\begin{array}{r l} B _ {1} ^ {1} (C _ {1} | \mathbf {x}) & = \gamma_ {1} (\underline {{S}}) [ \mu_ {1 1} + \frac {1}{2} (\mu_ {1 2} x _ {2} ^ {1 / 2} + \mu_ {1 3} x _ {3} ^ {1 / 2}) x _ {1} ^ {- 1 / 2} ] \\ & + \frac {1}{2} \gamma_ {2} (\underline {{S}}) (\frac {1}{2} \mu_ {2 1} x _ {2} ^ {1 / 2} x _ {1} ^ {- 1 / 2}) + \frac {1}{2} \gamma_ {3} (\underline {{S}}) (\frac {1}{2} \mu_ {3 1} x _ {3} ^ {1 / 2} x _ {1} ^ {- 1 / 2}), \\ B _ {2} ^ {2} (C _ {1} | \mathbf {x}) & = \frac {1}{2} \gamma_ {2} (\underline {{S}}) [ \mu_ {2 2} + \frac {1}{2} (\mu_ {2 1} x _ {1} ^ {1 / 2} + \mu_ {2 3} x _ {3} ^ {1 / 2}) x _ {2} ^ {- 1 / 2} ] \\ & + \frac {1}{2} \gamma_ {1} (\underline {{S}}) (\frac {1}{2} \mu_ {1 2} x _ {1} ^ {1 / 2} x _ {2} ^ {- 1 / 2}) + \frac {1}{3} \gamma_ {3} (\underline {{S}}) (\frac {1}{2} \mu_ {3 2} x _ {3} ^ {1 / 2} x _ {2} ^ {- 1 / 2}), \end{array}
$$

and,

$$
\begin{array}{r l} B _ {3} ^ {3} (C _ {1} | \mathbf {x}) & = \frac {1}{2} \gamma_ {3} (\underline {{S}}) [ \mu_ {3 3} + \frac {1}{2} (\mu_ {3 1} x _ {1} ^ {1 / 2} + \mu_ {3 2} x _ {2} ^ {1 / 2}) x _ {3} ^ {- 1 / 2} ] \\ & + \frac {1}{2} \gamma_ {1} (\underline {{S}}) (\frac {1}{2} \mu_ {1 3} x _ {1} ^ {1 / 2} x _ {3} ^ {- 1 / 2}) + \frac {1}{3} \gamma_ {2} (\underline {{S}}) (\frac {1}{2} \mu_ {2 3} x _ {2} ^ {1 / 2} x _ {3} ^ {- 1 / 2}). \end{array}
$$

## References

Alstyne, M. V., E. Brynjolfsson, and S. Madnick, "Why Not One Big

Database? Principles for Data Ownership," Decision Support Systems, 15 (1995), 267–284.

Bakos, J. Y., "Information Links and Electronic Marketplaces: Implications of Interorganizational Information Systems in Vertical Markets," J. Management Information Systems, 2 (1991), 31–52.

— and E. Brynjolfsson, "From Vendors to Partners: The Role of Information Technology and Incomplete Contracts in Buyer-Supplier Relationships," J. Organizational Computing, 10, (1993), 301–328.

— and B. R. Nault, Ownership in Electronic Networks, Working Paper Series, University of California, Irvine, 1992.

Brynjolfsson, E., Information Technology and the Reorganization of Work: Theory and Evidence, Unpublished Ph.D. Dissertation, MIT Sloan School of Management, Cambridge, MA, 1990.

——, "Information Assets, Technology, and Organization," Management Sci. 40, 12 (1994), 1645–1662.

Grossman, S. and O. Hart, "The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration," J. Political Economy, 94, 4 (1986), 691–719.

Gul, F., "Bargaining Foundations of Shapley Value," Econometrica, 57, 1 (1989), 81–95.

Gurbaxani, V. and S. Whang, "The Impact of Information Systems on Organizations and Markets," Comm. ACM, 34, 1 (1991), 59–73.

Hart, O. and J. Moore. "Incomplete Contracts and Renegotiation," Econometrica, 56, 4 (1988), 755–785.

— and —, "Property Rights and the Nature of the Firm," J. Political Economy, 98, 6 (1990), 1119–1158.

Holmström, B. R. and J. Tirole, "The Theory of the Firm," in R. Schmalansee and R. Willig (Eds.), Handbook of Industrial Organization Elsevier, Amsterdam, 1989.

Katz, M. L. and C. Shapiro, "Network Externalities, Competition and Compatibility," American Economic Rev. 75, 3 (1985), 424–440.

Malone, T. W., J. Yates, and R. I. Benjamin, "Electronic Markets and Electronic Hierarchies: Effects of Information Technology on Market Structure and Corporate Strategies," Comm. ACM, 30, 6 (1987), 484–497.

Myerson, R. B., "Optimal Coordination Mechanisms in the Principal-Agent Problems," J. Math. Economics, 10, (1982), 67–81.

——, Game Theory: Analysis of Conflict, Harvard University Press, Cambridge, MA, 1991.

Nault, B. R. and A. S. Dexter, "Adoption, Transfers and Incentives in a Franchise Network with Positive Externalities," Marketing Sci., 13, 4 (1994), 412–423.

Shapley, L. S., "A Value for n-Person Games," in H. W. Kuhn and A. W. Tucker (Eds.). Contributions to the Theory of Games Princeton University Press, Princeton, NJ, 1953.

Williamson, O. Markets and Hierarchies: Analysis and Antitrust Implications, The Free Press, New York, 1975.

Williamson, O. The Economic Institutions of Capitalism, Free Press, New York, 1985.

Haim Mendelson, Associate Editor. This paper was received on February 12, 1993, and has been with the authors 15 months for 5 revisions.
