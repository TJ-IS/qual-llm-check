---
otero_id: 6722
otero_key: "8GXDM8C7"
title: "A Unified Economic Model of Standard Diffusion: The Impact of Standardization Cost, Network Effects, and Network Topology"
authors: "Tim Weitzel; Daniel Beimborn; Wolfgang König"
year: "2006"
journal: "MIS Quarterly"
doi: "10.2307/25148770"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/8GXDM8C7/fulltext/images/4b0ddd8718827f48f7e2359d53fe0e941de1a55eaf8e261a4b3ec4b060e1d09d.jpg)

A Unified Economic Model of Standard Diffusion: The Impact of Standardization Cost, Network Effects, and Network Topology
Author(s): Tim Weitzel, Daniel Beimborn and Wolfgang König
Source: MIS Quarterly, Vol. 30, Special Issue on Standard Making (Aug., 2006), pp. 489-514
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/25148770

Accessed: 20/09/2013 00:51

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A UNIFIED ECONOMIC MODEL OF STANDARD DIFFUSION: THE IMPACT OF STANDARDIZATION COST, NETWORK EFFECTS, AND NETWORK TOPOLOGY $^{1}$

By: Tim Weitzel
Department of Information Systems
Otto Friedrich University
Feldkirchenstrasse 21
96052 Bamberg
GERMANY
tim.weitzel@wiai.uni-bamberg.de

Daniel Beimborn
Institute of Information Systems
Johann Wolfgang Goethe University
Mertonstrasse 17
60054 Frankfurt am Main
GERMANY
beimborn@wiwi.uni-frankfurt.de

Wolfgang König
Institute of Information Systems
Johann Wolfgang Goethe University
Mertonstrasse 17
60054 Frankfurt am Main
GERMANY
wkoenig@wiwi.uni-frankfurt.de

## Abstract

This paper is motivated by the following question: What drives the diffusion of a communication standard and what results can we expect? Past literature provides many instructive but mostly unrelated answers. Frequent findings are startup problems, penguin effects, and tendencies toward monopoly. But substantial problems in applying the models to concrete standardization problems reveal that the dynamics are probably more complex. Not all networks are ultimately conquered by a single standard once it has attracted a certain number of users. And not all diffusion results are either complete or no standardization.

We address the question of the conditions of particular diffusion behaviors by developing a formal standardization model that captures all fragmented phenomena in a unified approach. Drawing from findings of other research, we incorporate the structure of the underlying user network as an important determinant for diffusion behaviors. The approach allows us to disclose varying conditions that generate frequently observed standardization behaviors as special parameter constellations of the model. Using equilibrium analysis and computer simulations we identify a standardization gap that reveals the magnitude of available standardization gains for individuals and the network as a whole. The analysis shows that network topology and density have a strong impact on standard diffusion and that the renowned tendency toward monopoly is far less common. We also report how the model can be used to solve corporate standardization problems.

Keywords: Standardization, diffusion, network effects, equilibrium, noncooperative games, topology, computational analysis, penguin effects

## Introduction

Standards play a prominent role in systems characterized by interaction, such as intranets, supply chains, or electronic markets. In information systems, communication standards provide for compatibility and are a prerequisite for collaboration benefits. The commonality property deriving from the need for compatibility is inherent in standards and implies a coordination problem: the standardization problem (Besen and Farrell 1994). The value of a standard to one user (person, business unit, firm, etc.) is dependent on others using it as well. Accordingly, understanding the dynamics behind the diffusion of standards is an important challenge for researchers as well as for professionals concerned with information technology governance, developing information infrastructures, and managing value chains. The growing literature on standards has provided valuable insights into many standardization topics such as startup problems and under-standardization.

Most contributions, though, analyze standardization problems solely from a vendor's perspective, focusing on pricing and communication strategies. Others address public policy and antitrust issues, because of the supposed necessity of monopolies and the associated risk of market power abuse. At the same time, research findings have remained fragmented and there is a lack of unified analysis of conditions that yield the examined phenomena. This weakens the applicability of the proposed models to real standardization problems. The main reason is an over-simplification of the analysis that neglects variance among standard user behaviors and too boldly generalizes network effects. This lack of concern for individual variance is reflected in models that represent utility $U_{i}$ from standardization to agent $i$ in the form $U_{i} = a_{i} + bn$ , where the benefits derive from a standalone effect $a_{i}$ and the network effect $bn$ in a network of $n$ agents (e.g., Matutes and Regibeau 1996).

But, in realistic standardization situations, not all agents gain an equal share (b) of network effects, nor do all of them interact with the same network (n). Instead, agents' local interactions with their partners (e.g., with few versus many versus all in a network of users) and the way they use standards (e.g., fully automated EDI versus form-based Web EDI [Beck and Weitzel 2005]) can determine the agents' standard decision. This claim is supported by findings from sociology and medicine, which both show that the diffusion of opinions or diseases depends on individuals' interaction patterns, or generally on the network topology (Coleman et al. 1957; Valente 1995). As a consequence, there is an incomplete understanding of the conditions that affect standard diffusion. Can we always expect IT standards to exhibit a strong propensity to monopolize? What impact does the structure of the user network have on standard diffusion, and what can standard users do to overcome inefficiencies of unfavorable standardizations? The lack of good answers to these questions poses a substantial challenge for scholars, managers, and policymakers in the IS field given that standards form an essential element of the communication infrastructure within and between firms as well as for societies. An insufficient understanding of conditions that affect standard diffusion will result not only in missed business opportunities (e.g., poor value-chain integration), but also lead to inefficient economic policies. To address these concerns we explore in this paper the following three research questions:

(1) What are causes of standardization problems, and how can their magnitude (available standardization gains) be operationalized?

(2) What impacts do variance in individual standardization costs and network effects have on standard diffusion?

(3) What are the impacts of network topologies on standard diffusion?

The goal of this paper is to unify micro effects (individual standardization decisions) and macro effects (network effects) into a singular formal model of standardization problems. The proposed model offers three contributions. First, the model consolidates isolated findings from the standardization literature into a unified model. Second, the model helps identify a standardization gap: the magnitude of available standardization advantages that have remained unrealized. Third, the model, by incorporating network topology and density into the analysis, takes into account standard users' network embeddedness.

Taken all together, these allow us to explain typical standardization problems and outcomes as specific diffusion patterns of the proposed model generated under certain conditions of standardization cost, network effects, and network topology. By doing so, the analysis reveals conditions under which startup problems, penguin effects, and monopoly tendencies emerge as special cases of standard diffusion with particular parameter constellations. We evaluate the magnitude of standardization gains, analyze when standard diffusion processes can result in monopolies (i.e., winner takes all), and probe how strongly the topology and the installed base impact diffusion outcomes. A computational analysis confirms propositions derived from the model associated with specific standardization situations.

The remainder of the paper is structured as follows. We start with a critical review of network effects by developing a standardization model that captures the interplay between individual decision-making and network behavior. The model is then used for game theory equilibrium analysis which demonstrates the existence of a standardization gap. We use computational analysis to show the dependence of the observed standard diffusion pattern on standardization cost, network effect, and network topology. This is followed by a discussion of practical implications of the outcomes for IT governance, and validity and limitations of the research. We conclude with implications for future research on IS-related standards.

## Review of Literature

## Standard Semantics

“Ironically, standards have not been completely standardized” (Hemenway 1975, P. 8). This famous quote describes nicely the bewildering variety of approaches to defining standards. In this work, standard is used to refer to any technology or product incorporating specifications that provide for compatibility. Many authors emphasize the importance of compatibility (Farrell and Saloner 1987) as a technological property of system components that enables them to “somehow go together” (Gabel 1991, p. 1) and makes them subject to a network effect. Hence, compatibility standards enable users “to participate in networks that allow them to share databases...exchange documents...or simply communicate directly” (Besen and Farrell 1994, p. 117). Standardization, according to the user perspective taken in this work, is defined as the implementation and use of a standard to interact with a communication partner. In contrast, the colloquial use of the term standard refers primarily either to the diffusion results of many individual standardization decisions or the success of a vendor’s penetration strategy.

## Network Effect Theory as Theoretical Foundation

The analysis of standardization problems is based primarily on the theory of positive network effects (Besen and Farrell 1994), which have been defined as “the change in the benefit, or surplus, that an agent derives from a good when the number of other agents consuming the same kind of good changes” (Liebowitz and Margolis 1995a, p. 2). The externality property implies coordination problems that are said to be endemic in high tech and software industries in particular (Westarp 2003). As demand-side economies of scale in the standard adoption, network effects make interdependent decisions of agents that could otherwise be autonomous. This creates a coordination problem often called the standardization problem (Besen and Farrell 1994, p. 118; Wiese 1990, p. 1). The first groundbreaking contributions to this relatively young research field stem from the early 1980s. Of course, there are earlier contributions in the field of standards (e.g., Gaillard 1934; Hemenway 1975; Rohlfs 1974), but it was not until about 20 years ago that standards emerged as a separate topic of research.

Direct network effects are described as the physical effects (Katz and Shapiro 1985, p. 424) of being able to exchange information (as with telephones), while indirect network effects arise from interdependencies in the consumption of complementary goods (Braunstein and White 1985; Church and Gandal 1992). Arthur (1983, 1989) shows that technologies subject to increasing returns exhibit multiple equilibria and will finally lock into a monopoly with one standard cornering the entire market. Since this standardization process is non-ergodic (or path dependent), the ultimate outcome is unpredictable. Analogously, Besen and Farrell (1994) show that “tippiness” is a typical characteristic in networks, describing that multiple incompatible technologies rarely coexist and that the switch to a single, leading standard occurs suddenly. An important distinction should be made between sponsored (actors holding property rights; capability of restraining the use of a standard) and unsponsored (no actors with proprietary interests) networks.

The theoretical bottom-line argument for standardization processes is that the discrepancy between private (individual) and collective (network wide) gains leads to coordination problems (possibly Pareto-inferior results). With incomplete information about other actors' preferences, excess inertia can occur, as no actor is willing to bear the disproportionate risk of being the first adopter of a standard and then becoming stranded in a small network if all others eventually decide in favor of another standard. This startup problem can prevent the adoption of any standard at all, even if it is preferred by everyone. Conversely, excess momentum is a possible outcome, for example, if a sponsoring firm uses low prices during early periods of diffusion (Farrell and Saloner 1986). In sponsored networks, the problem is attenuated since, for example, there is the possibility of internalizing the potential network gains by strategic inter-temporal pricing (Katz and Shapiro 1986). There are private incentives to providing networks that can overcome inertia problems; however, they do not guarantee social optimality per se.

From a methodological point of view, the literature distinguishes various perspectives (David and Greenstein 1990;

<table><tr><td>Standard</td><td>Creation</td><td>Adoption (“Diffusion”)</td></tr><tr><td>Vendor (Government)</td><td>- Standards engineering- SDOs, consortia (ISO, W3C, etc.)- Action variable: Compatibility</td><td>- “Sponsored Networks” (proprietary/de jure standards)- Market power, pricing strategy, etc.- Action variable: Price, communication strategy, etc.</td></tr><tr><td>User</td><td>? (user participation at ISO, etc.)</td><td>- “Unsponsored Networks” (de facto standards)- Anticipation of network behavior- Action variable: Standardization</td></tr></table>

Figure 1. Research Strands

Yang 1997). Authors who use empirical approaches mainly try to prove the existence of network effects and estimate their values by using regression analysis to estimate the hedonic price function of network effect goods (Gandal 1994; Hartmann and Teece 1990). Theoretical approaches mostly employ equilibrium analysis to explain phenomena such as the startup problem (Besen and Farell 1994; Katz and Shapiro 1985; Oren and Smith 1981; Rohlfs 1974; 1994; Wiese 1990), market failure (Farrell and Saloner 1985, 1986; Katz and Shapiro 1986, 1992, 1994), tippiness of network effect markets (Arthur 1989, 1996; Besen and Farell 1994; Farrell and Saloner 1985; Katz and Shapiro 1994; Shapiro and Varian 1998), and path dependency (Arthur 1989; Besen and Farell 1994; Katz and Shapiro 1994; Liebowitz and Margolis 1995b). Other important issues include mix and match markets (Matutes and Regibeau 1988), different individual interests and their influence on participation in standardization processes (Jakobs et al. 1996), as well as antitrust and policy issues. As noted above, large areas of the literature are concerned with producer/vendor strategies. For software vendors, many competitive strategies have been proposed, including versioning, bundling (Bakos and Brynjolfsson 1999), strategic pricing, and second sourcing. Also, between vertically integrated markets, there is the typical vendor's question of whether to provide components compatible with those of other firms (Economides and White 1993), which means deciding between competing within or between standards (Besen and Farrell 1994).

## Identifying the Different Research Strands

Only recently have the scientific communities interested in standardization moved closer to establish a systematic view of the domain and to incorporate diverse research strands into a common view. Figure 1 systematizes distinctions between the different actors (vendors versus users) and the standard's lifecycle phase (develop versus use). The main difference in these situations is the respective action variables: while in the renowned battle for video systems, for example, producers could decide on technical (e.g., degree of compatibility with competitors) and business (e.g., penetration pricing, second sourcing) strategies, users were faced with the decision of which system to buy given expectations of future dispersion and availability of video tapes.

While this classification allows us to distinguish major strands in the argument, the coexistence of these groups over decades with little interaction is remarkable. Now a consensus is emerging that the main challenges are a stronger emphasis on the standards user as well as a better understanding of the economics of standards, that is, a managerial, business-oriented cost and benefit evaluation. This can offer insights into a variety of standardization motives and help one apply the findings to the real world. In the following section, a model is developed to address precisely this challenge.

## Theoretical Classification

While it is common in many markets that the buying decision of one consumer influences the decisions of others (e.g., bandwagon, snob, and Veblen effect are discussed broadly in the economic literature), a discussion has ensued lately whether ICT markets, in particular, are determined by strong network effects. By 1950, Leibenstein had already anticipated some elements of the problem, stating that demand curves are more elastic when consumers derive positive value from the increasing market size. The relevance of this standardization problem is thus fundamental in that it identifies the general coordination problem behind economic systems subject to demand-side positive externalities, of which ICT markets are a perfect example. From a theoretical perspective, a major challenge is to overcome limitations of theories that are rooted in neoclassical economics (as are most aspects of network effects theory: the notion of network effects is a utility-theoretical construction). The reason is that the existence of externalities disturbs automatic transmission from local to global efficiency. Externalities can make markets fail, which in turn keeps the pursuit of individual goals from adding up to a social optimum. A methodological step toward overcoming this problem is to study the entire dynamic system based on explicit local decision models and their interplay. Unfortunately, this implies that investigators must deal with substantial complexity, although computational research now offers a promising way to tackle this problem.

## Reconsidering Network Effect Theory

The growing literature on standards has contributed to identifying and understanding elementary phenomena associated with standards. At the same time, serious limitations of the power of many contributions—especially for the dynamic ICT markets—have become apparent (Liebowitz and Margolis 1999; Weitzel et al. 2000). The “scrupulous and implicit simplifications” (Wiese 1990, p. 101) of most network effect models make them essentially useless for deriving concrete managerial implications. For example, the prevailing propensity to monopolization (networks tipping into monopoly) cannot explain with the coexistence of different IT products, despite strong network effects (e.g., server market, EDI networks; Westarp 2003). Especially from a user’s perspective, there is a lack of solution strategies for using and dispersing standards within enterprises as well.

Still, this is a key CIO challenge. For instance, standardization as defined in this work is one of the main issues of the CIO group of Siemens, a multinational enterprise with more than 400,000 employees, which has specified standardization as the primary objective of IT governance. Another case is the staff division of a large global airline responsible for standardization within the firm as well as within the airline's major alliance network. Together with the authors, they searched for managerial help to establish internal document exchange standards (e.g., particular versions of MS Word) and provide consistent software versions throughout different business units to avoid substantial friction costs. It turned out that the models found in the literature provided general ideas on the system behavior to be expected (e.g., units do not standardize), but they could neither be applied to the concrete local problem (mostly because the models could not account for the individual cost, benefit, and interaction situation of the affected units) nor used to derive or evaluate solutions. One important reason for these problems and especially the probably strong overestimation of the tendency toward monopolies is the (mostly implicit) assumption of continuously increasing homogeneous network effects (Liebowitz and Margolis 1995b). Another reason is the non-consideration of the structural properties of networks, that is, neglecting individual relations between network agents and focusing on the overall network instead (Weitzel et al. 2003).

In medical research, important insights into the diffusion of diseases resulted from observing individual network neighborhoods. Also, in sociology, considering agents' network topology and the results of its impact, such as group membership, intra-group pressure, and opinion leadership (Coleman et al. 1957), could contribute greatly to explaining the diffusion of technological innovations. The marketing sciences have long emphasized the importance of individual relations among consumers (e.g., Goldenberg and Efroni 2001; Westarp 2003). Reingen and Kernan (1986, p. 371) suggest the use of "relational data [to] describe the emergent properties of connections between individuals (e.g., information flow linkages, friendship ties, etc.). They provide the foundation for a network analysis of those customers of a marketer who have been generated by interpersonal interaction." Similarly, drawing from social network analysis as well, Frenzen and Nakamoto (1993, p. 360) successfully apply a relational view to diffusion phenomena ("the effectiveness of word-of-mouth [WOM] as a means to disseminate information throughout a market") by crossing the micro- and macro- "levels of analysis so that the combined effect of individual and structural factors on the aggregate flow of WOM information in markets can be explored" (see also Westarp and Wendt 2000).

## Standardization Model

We now develop a standardization model to describe the strategic situations agents face when deciding on standards. The model can be used for assessing the extent of unexploited standardization gains in corporate standardization problems and is used later for simulation studies on standard diffusion. We address the issues raised earlier by explicitly modeling the individually available direct network effects and the evolving decision situation of network agents embedded in their local network structures. The appendix is a table that summarizes all of the variables and parameters explained in the following section.

## Standardization Costs and Benefits

The basic question underlying the user's standardization decision is whether the standardization costs exceed the benefits.

While standardization costs (i.e., the costs of standards adoption) are relatively easy to quantify ex ante, the benefits of using a standard often are even not quantifiable after the adoption. The common use of IT standards generally simplifies transactions carried out or eases the exchange of information between agents. While the use of standards can lead to direct savings due to cheaper and faster communication (Kleinemeyer 1998), standards often also induce more strategic benefits: avoiding media discontinuities, eliminating errors, and reducing time and costs. Potential benefits of using standards, apart from being able to reach more communication partners, include lower conversion and friction costs (Braunstein and White 1985; Thum 1995). In our standardization model, agents can represent single users or departments within a firm (firm-internal standardization) or different companies communicating with each other (vertical industry standards). The model is developed in a generic way; therefore, it can be applied to each of the investigation levels listed in Damsgaard and Lyytinen (1998), who made an empirical analysis on EDI diffusion on the macro (i.e., national) level, on the meso (i.e., industry) level, and on the micro level (i.e., within a firm). Our model, however, is not able to cover agents on the intra-firm and interfirm levels simultaneously.

## A Decentralized Standardization Model

Consider a network consisting of n agents. Let $E_{i}$ be the ex post standardization utility of agent i modeled as the excess of direct network effects $c_{ij}$ with partner j over standardization costs $K_{i}$ . According to the basic tradeoff described above, the individual (decentralized) standardization condition for agent i is $E_{i} > 0$ . In equation 1, the binary indicative variable $x_{j}$ takes on a value of 1 if agent (partner) j standardizes (else = 0).

(1)

$$
C E = \sum_ {i = 1} ^ {n} E _ {i}\tag{2}
$$

$$
E _ {i} = \sum_ {\stackrel {j = 1} {j \neq i}} ^ {n} c _ {i j} \cdot x _ {j} - K _ {i}
$$

To compare the decision quality in different networks, CE (coordination efficiency) denotes aggregate networkwide net benefits from standardization, that is, the horizontal aggregation of all individual benefits (equation 2) less all individual standardization costs. Since in realistic decision situations agents cannot rely on others standardizing, it is fundamental to anticipate the partners' standardization behavior. It is widely acknowledged in the literature that expectations play a crucial role in modeling standardization problems (Arthur

1989; Katz and Shapiro 1985, 1986). To model this anticipatory decision behavior, let $p_{ij}$ describe the probability with which agent $i$ believes that $j$ will standardize. To determine $p_{ij}$ it is assumed that agent $i$ knows agent $j$ 's standardization costs $K_j$ and the network effects directly associated with him (i.e., $c_{ij}$ and $c_{ji}$ ), as well as the number of $j$ 's communication partners (represented by $\phi(j)$ ) (i.e., $n-1$ in a full-density network). No further data, such as network effects between other agents, are available to the agents. This is a realistic proposition, and empirical research shows that these data are, in fact, usually available to the deciders.

(3)

The numerator in (equation 3) describes the first best net standardization benefits to j (best case). To estimate a partner's $E_{j}$ , actor i assumes known $c_{ji}$ to be representative for all other links of agent j. The denominator normalizes the fraction for nonnegative $K_{j}$ as a value from 0 to 1. If the fraction is negative, that is $c_{ji} \phi(j) < K_{j}$ , then $p_{ij} = 0$ holds.

$$
s. t. \quad c _ {i j}, c _ {j i} > 0 \quad \forall i, j \quad i \neq j
$$

$$
EXPECT\left[E_{i}\right] = \sum_{\substack{j = 1\\ j\neq i}}^{n}p_{ij}c_{ij} - K_{i}\quad \text{with}\quad p_{ij} = \frac{c_{ji}\phi(j) - K_{j}}{c_{ji}\phi(j)}
$$

## Centralized Coordination of Standardization Decisions

To compare individual and aggregate network utility, two coordination regimes are modeled. A decentrally coordinated network as developed above models individual agents' behavior prior to any possible coordination, that is, in the extreme case of no ex ante coordination or external force. In contrast and to benchmark the efficacy of solution strategies, a centrally coordinated network describes the maximum possible coordination quality, assuming perfect coordination (at no cost) by a central manager who can determine and implement the optimal result networkwide (Weitzel et al. 2003). The important difference is that the central decider striving to optimize an aggregate objective function can explicitly consider all network effects, while the individual agents act only to optimize the fraction that is relevant to them. Thus, the individual implications of standardization decisions are irrelevant from the centralized perspective.

Figure 2 illustrates the differences between the two coordination regimes. Let us assume that agent 1 is an SME that considers joining the EDI network of firm 2. If the small firm (agent 1) decides in favor of implementing the EDI standard, it has to bear standardization costs of $K_{1}=10$ . If both agents standardize, the potential benefits are direct network effects of $c_{12}=9$ to firm 1 and of $c_{21}=30$ to firm 2. At aggregate standardization costs of 30 compared to network effects totaling 39, bilateral standardization is centrally beneficial. But from a decentralized perspective, firm 1 would not standardize, since the costs ( $K_{1}=10$ ) exceed the benefits ( $c_{12}=9$ ). Because in this case it has complete information, firm 2 also will not standardize.

![](/api/attachments/8GXDM8C7/fulltext/images/e2eb55c8944b8a43a747134a6a16d082017a555ab7c8b10c9c7b7b46b1c13874.jpg)  
Figure 2. Two-Agent Example

Increasing the number of agents results in a combinatorial problem, which can be solved by computing the following linear program, adapted from Buxmann (1996). The objective maximizes the difference of benefits and costs from standardization over the whole network of agents. $y_{ij}$ represents an additional (auxiliary) binary variable, which takes on a value of 0 if agents i and j standardize.

$$
\mathrm{CE} = \sum_ {i = 1} ^ {n} \sum_ {j = i + 1} ^ {n} \left(c _ {i j} + c _ {j i}\right) \cdot \left(1 - y _ {i j}\right) - \sum_ {i = 1} ^ {n} K _ {i} \cdot x _ {i} \rightarrow \max!
$$

s.t.

$$
\begin{array}{l l} x _ {i} + x _ {j} + y _ {i j} \leq 2 & \forall i, j \in \{1,..., n \}, i <   j \\ x _ {i} + y _ {i j} \geq 1 \quad x _ {j} + y _ {i j} \geq 1 & \forall i, j \in \{1,..., n \}, i <   j \\ y _ {i j} \geq 0 \quad y _ {i j} \leq 1 & \forall i, j \in \{1,..., n \}, i <   j \\ x _ {i} \geq 0 \quad x _ {i} \leq 1 & \forall i \in n \end{array}\tag{4.1-5}
$$

Although the problem implicitly contains binary variables, it could be shown that the structure of the constraints fulfills the condition of uni-modularity, leading to only integer solutions, although the variables are not restricted to integer values ex ante (Domschke and Wagner 2005).

The elementary discrepancy between centrally and decentrally coordinated standardization outcomes is found in most corporate standardization problems. It is analyzed in more detail in the analysis sections later in this paper.

## Modeling Multi-Standard Standardization Problems

The basic model is now extended to consider not only standardization yes/no decisions but also to include decisions between Q rivaling standards q. Equation 5 determines the expected utility of standardization (ex ante utility).

$$
EXPECT\left[E_{iq}\right] = \sum_{\substack{j = 1\\ j\neq i}}^{n}p_{ijq}\cdot c_{ij} - K_{iq} = \sum_{\substack{j = 1\\ j\neq i}}^{n}\left(\frac{c_{ji}\cdot\phi(j) - K_{jq}}{c_{ji}\cdot\phi(j)}\right)\cdot c_{ij} - K_{iq}\tag{5}
$$

Since standardization costs for different standards $K_{iq}$ are not necessarily identical, the individually expected values differ with regard to the respective standard choice. Real-life analogies include different legacy applications and data, switching costs, and so on. It is assumed that agents decide in favor of the standard offering the highest individual positive expected value. As can be seen in equation 5, potential benefits are independent of the technology. Thus, there is no difference regarding the benefits of alternative standards (e.g., cost savings if two partners use EDIFACT or ANSI ASC X12 to exchange data electronically). Nevertheless, standardization costs can vary between agents with regard to individual adaptation requirements. Other assumptions are possible, of course. See Weber (2000) for a critique of neglecting hierarchical dependencies between standards.

Individual ex post savings can now be determined according to equation 6.

$$
\begin{array}{l}E_{iq} = \sum_{\substack{j = 1\\ j\neq i}}^{n}\big(1 - y_{ij}\big)\cdot c_{ij} - \sum_{q = 1}^{Q}x_{iq}\cdot K_{iq}\\ s.t.: \sum_{q = 1}^{Q}x_{iq}\leq 1 \end{array} \quad E_{i} = \sum_{q = 1}^{Q}E_{iq}\tag{6}
$$

The binary variable $x_{iq}$ has the same properties as $x_{i}$ ; $x_{iq} = 1$ describes agent i implementing standard q, and $p_{ijq}$ represents the estimated probability from the perspective of agent i that agent j adopts standard q. $y_{ij}$ takes a value of zero if both agents, i and j, use the same standard. The side condition that users buy one or no standard is common in modeling standardization problems (Arthur 1989; Katz and Shapiro 1985; Westarp 2003) and could easily be relaxed. Extending the assumption implicit in large parts of the literature that agents can only decide once, we will focus on the possibility of reversible standard choice, that is, that an agent can switch to another standard if she considers this advantageous.

<table><tr><td colspan="3">Table 1. Payoff Matrix for the Basic Two-Player Standardization Game</td></tr><tr><td></td><td colspan="2">Player 2</td></tr><tr><td>Player 1</td><td> $S_{21}$ (no standardization)</td><td> $S_{22}$ (standardization)</td></tr><tr><td> $S_{11}$ (no standardization)</td><td>(0,0)</td><td>(0,- $K_2$ )</td></tr><tr><td> $S_{12}$ (standardization)</td><td>(- $K_1$ ,0)</td><td>( $c_{12}$ - $K_1$ ,  $c_{21}$ - $K_2$ )</td></tr></table>

the strategy combination that maximizes the sum of benefits is no Nash equilibrium.

## Equilibrium Analysis

## General Strategic Situations

Concerning the outcome of standardization games, the existence of multiple equilibria indicates that there can be inefficient results (Arthur 1989). It turns out that there are different strategic situations determining how difficult it is to reach desirable standardization results. For systematically disclosing these strategic standardization situations, we use noncooperative game theory in this section.

There are some basic games employed in game theory that are useful to understand the general dynamics of standardization problems. Strategic situations characterized by multiple Nash equilibria and synergies (i.e., mutual gains are possible) are called coordination games (Lewis 1969). There are “pure coordination” games in which players are indifferent concerning multiple equilibria as long as a common solution is found. In contrast, there are games in which the main goal of all the parties involved is a common solution, but there are “somewhat” diverging interests. Called a battle-of-the-sexes situation, this got its name from the strategic situation of a couple yearning for quality time together but disagreeing as to whether there is more quality in going together to a boxing match or the opera (Luce and Raiffa 1957). Table 2 provides an example. Since almost all models in the literature consider only positive network effects, most standardization problems have a battle-of-the-sexes structure (Farrell and Saloner 1988, p. 238), among them such famous cases as television standards (PAL, SECAM, NTSC) (Crane 1979) or AM stereo (Besen and Johnson 1986). In contrast, completely diverging coordination interests describe the situation in which choosing

## Equilibria in Standardization Games

## The Ballot Problem

Let us assume a one-period game with complete information, that is, complete multilateral knowledge of all payoff matrices (Harsanyi 1967, 1968a, 1968b). For a simple two-player standardization problem in which players decide whether to use a certain standard, Table 1 depicts the general payoff matrix according to our standardization model.

Let $s_{i1}$ describe the strategy “no standardization” and $s_{i2}$ “standardization” for player i. With two players, standardization is centrally advantageous if $(c_{12} + c_{21}) > (K_{1} + K_{2})$ , that is, if cumulative benefits are greater than cumulative standardization costs, while there are two Nash equilibria $((s_{11}, s_{21})$ and $(s_{12}, s_{22}))$ : bilateral nonstandardization and bilateral standardization. The centralized solution is always a Kaldor-Hicks optimum that defines the equilibrium with the maximum aggregate net benefits (Kaldor 1939). Thus, in decentralized networks, the suboptimal case of both players not standardizing is also an equilibrium (unlike in centrally coordinated networks).

In the case above, it seems likely that players will reach the mutually beneficial equilibrium $(s_{12}, s_{22})$ . However, if for both players network effects are greater than standardization costs, the situation becomes more complicated when choosing between two standards—as in the battle of the sexes (Table 2).

Here, both prefer a common standard but do not agree on which standard. Accordingly, it is possible that both agents fail to choose a common standard or choose no standard at all. When extending the strategic situation to a multi-period problem as in the following simulation analysis, a lack of standard adoption activities on the one hand could be explained by the fact that each player waits for the other's decision (excess inertia; Farrell and Saloner 1986). On the other hand, both players may want to make a first move to have the other follow. This is what happened when France and Germany decided on television standards. Both wanted a common standard, but Germany preferred PAL and France preferred SECAM. They moved simultaneously, each believing they were the first mover, in an effort to decide the game in their favor. As a consequence, the two countries still have different television systems. Generally, a strategic standardization situation characterized by multiple advantageous outcomes, which can, in principle, be solved by communication (coordination games), is called a ballot problem.

Table 2. Payoff Matrix for a Coordination Game with “Somewhat” Diverging Interests (Ballot Problem)

<table><tr><td></td><td colspan="3">Player 2</td></tr><tr><td>Player 1</td><td> $s_{21}$ (no standard)</td><td> $s_{22}$ (standard 1)</td><td> $s_{23}$ (standard 2)</td></tr><tr><td> $s_{11}$ (no standard)</td><td>(0, 0)</td><td>(0, -1)</td><td>(0, -2)</td></tr><tr><td> $s_{12}$ (standard 1)</td><td>(-1, 0)</td><td>(3, 2)</td><td>(-1, -2)</td></tr><tr><td> $s_{13}$ (standard 2)</td><td>(-2, 0)</td><td>(-2, -1)</td><td>(2, 3)</td></tr></table>

Table 3. Standardization Game of Figure 2 (Welfare Problem)

<table><tr><td></td><td colspan="2">Player 2</td></tr><tr><td>Player 1</td><td> $s_{21}$ (no standardization)</td><td> $s_{22}$ (standardization)</td></tr><tr><td> $s_{11}$ (no standardization)</td><td>(0, 0)</td><td>(0, -20)</td></tr><tr><td> $s_{12}$ (standardization)</td><td>(-10, 0)</td><td>(-1, 10)</td></tr></table>

## The Welfare Problem

There are also games in which centralized coordination results in standardization while decentralized coordination will never do $(c_{12}<K_{1}$ and $c_{21}>K_{2}$ while $K_{1}+K_{2}<c_{12}+c_{21}$ in Table 1). In this case standardization would never be the optimal strategy. Due to heterogeneous standard implementation costs resulting from different legacy worlds, few standardization problems are pure coordination games. There are many standardization problems in which communication or other rather simple designs might not solve the coordination problem and will not be able to overcome excess inertia (Farrell and Saloner 1986). This welfare problem scenario changes the situation described by a battle-of-the-sexes game to a game with totally diverging interest, since no satisfactory solution can be attained without redistributing standardization costs and/or benefits. Table 3 represents the welfare problem of the simple one-standard case in Figure 2.

## Solutions

A pure coordination game can be solved by “cheap talk” (Farrell 1987), that is, by simple communication—as in the prominent example of so-called breakfast cartels. This situation might be found when everyone profits from using the one available standard, or when different standards yield the same utility. Driving on the right side of the road is an example (Kindleberger 1983). In fact, this is the reason that “roundtables” are often used to coordinate standardization activities within large enterprises, taking advantage of their coordination game structure. However, Cooper et al. (1989) show that cheap talk might be advantageous even in battle-of-thesexes situations. For example, a large firm could announce a switch to a particular EDI standard, thereby creating a “focal point” for the situation in Table 2. This strategy of making one solution less likely is often analyzed in duopoly games. In the standardization literature, the respective vendor strategy is called predatory preannouncement (Farrell and Saloner 1986, p. 942).

For solving welfare problems, a redistribution of standardization costs and/or benefits is indispensable, making standardization beneficial for all parties involved by ex post establishing the strategic situation of a coordination problem. In EDI networks, for example, a large firm can let the SMEs share in its efficiency gains to help the smaller firms overcome the high standardization costs. This can take the form of direct subsidies from larger to smaller EDI-using firms (Beck and Weitzel 2005) or by the large firm providing skills and human resources to implement EDI solutions on the SMEs' side (Westarp 2003). A firm-internal example is the CIO sponsoring software for business units despite their autonomous IT budget.

We used a noncooperative game to represent the strategic ex ante decision situation of an individual agent as representing a pure standard user view. In contrast, in cooperative games, coalitions between the participating players are permitted and agents can make binding agreements that can help them overcome some of the inefficiencies. While noncooperative game theory deals mainly with the problem of predicting which allocation will result, cooperative game theory addresses whether a particular coalition will be formed and how coalitions will divide their value among the participating players. As we are interested in the allocation problem and as the noncooperative standardization game is the pure form of decentrally coordinated networks, we use the centralized (all possible coordination gains realized) and decentralized (no coordination gains realized) perspectives as two benchmarks. Understanding noncooperative standardization games is important as they are the starting point for possible cooperative solution designs. This is not to say that the non-cooperative situation fully characterizes the real-world standardization problem. Our aim is to analyze the dynamic interplay of standards value creation, that is, the interplay between micro effects (individual decision) and macro effects (network effects) associated with standards separate from possible coordination gains from explicit communication or contractual designs between players.

As discussed above, coalitions can be a simple solution to inefficient multiple equilibria in two-player games, especially when standardization benefits both parties. That is why we expect important contributions to standardization research from mechanism design/cooperative game theory. Also, in standardization problems with few players, local solutions based on side payments are conceivable. That being so, in all of the standardization problems with which the authors have been involved, all participating parties agreed to establish solutions based on side payments but then failed to adopt a common standard. The reason is that all side payment schemes presume a commonly agreed-upon assessment basis. As it turns out, disagreements on a “fair” sharing rule routinely exclude the actual closing of a side payment deal. From our insights into the allocation problem, we expect very interesting results from further research on the distribution problem. As part of a model based on cooperative game theory, we could already formally prove that only a proportional allocation of costs will regularly lead to stable coalitions. Still, a game theory experiment indicates that deciders are more likely to choose inefficient allocations (Beimborn et al. 2006).

As a result, we can summarize that in networks with decentralized coordination, there is a smaller propensity to standardize. We call the difference between the centralized and decentralized solution the standardization gap, operationalizing the magnitude of a standardization problem by showing the network effect benefits as yet unexploited.

In the following section, the simulations with more than two agents show this standardization gap, which can result either from a ballot problem or from a welfare problem. Relaxing the unrealistic assumption of complete information as in the precedent analysis certainly implies further efficiency losses and a substantial problem complexity. There is also the fact that agents in dynamic multi-period multi-standard games have evolving information sets resulting from the mutual feedback of individual standardization decisions and standardization profits determined by their partners' decisions in earlier periods.

## Analysis of General Standardization Dynamics

In this section, we use simulations to gain a better understanding of the dynamics of standardization. This work uses a numerical rather than analytical approach. Associated disadvantages such as smaller analytical transparency or results that cannot be presented in the form of an equation are compensated for by the ability to analyze more complex and dynamic structures and discrete choice scenarios.

As the simulations should remain as simple, comprehensible, and adaptable as possible, we chose a plain implementation of the formal model in Java rather than an agent-based platform (e.g., JADE). Also, we decided against the cellular automata common in marketing sciences (e.g., Goldenberg and Efroni 2001), because this method cannot represent sufficiently the structure of our model, especially the explicit definition of individual inter-actor information ( $c_{ij}$ ). Furthermore, our network-based approach is more intuitive and much better suited for investigating the influence of network density or specific network structures (e.g., supply chains). The use of a computational economics approach is discussed critically in a later section.

First, we use one-standard simulations, implementing the basic model (equation 3), to depict the standardization gap as the magnitude of unexploited standardization gains. Certain cost constellations are shown as preconditions for the well-known startup problem and penguin effect. The scope of analysis is then extended step by step. An analysis of multi-period, multi-player decisions between different standards (implementation of the multi-standard model presented in equations 5 and 6) reveals that many typical standardization outcomes, especially monopoly, depend on particular parameter constellations such as network topology and standardization costs.

## Simulation Design and Parameters

## Network Initialization and Simulation Pattern

All simulations were generated using Java 1.4 applications. An applet, for which one can freely define its parameters, is available at http://www.it-standards.de/network. Overall, networks are generated randomly and all agents are assigned individual standardization cost and benefit data according to the distribution parameters given in the following tables. Once the network is generated, all agents decide according to their decision functions outlined above (equation 3), reacting to the locally observable decisions of their network neighbors. More precisely, a network is first initialized, assigning approximately normally distributed random values to $K_{i} \sim ND(\mu((K), \sigma(K)))$ and $c_{ij} \sim ND(\mu(c), \sigma(c))$ (no cost values $\leq 0$ are used). Then the decentralized decisions evolve. In later periods ( $t > 1$ ), agents can reconsider their decisions not to standardize using additionally available information about their partners' decisions, or they can change the standard. A simulation run terminates after reaching a certain period $T$ (time horizon). The simulation process is repeated 50 times before altering particular parameters, such as mostly reducing $\mu(K)$ and then starting anew. In the following simulations, standardization costs are reduced from an initial $\mu(K) = 45,000$ to 0 by increments of 250. On average, the figures in this section each consist of about 4,500 simulation runs.

## Centralized Standardization as Benchmark

As an efficiency benchmark, the centralized solution is determined using the linear program introduced earlier (equation 4.1–5). Solving the linear program determines the optimal network configuration (which agent should adopt the standard) for gaining network-wide maximum net benefits from standardization.

Due to the computational complexity of this program, we limited the simulated networks to 35 agents (corresponding to 630 variables and 2,415 restrictions in the linear program). Other network sizes and distributions of cost and benefit values yielded analogous results. To solve the linear program, we used a freely available Java implementation of the Simplex algorithm from www.opsresearch.com.

## The Standardization Gap

One of the major findings that already abounds in game theory equilibrium analysis is the existence of a standardization gap: although there are considerable potential net benefits from standardization represented by the centralized solution $CE(z)$ (grey graph in Figure 3, computed by solving the linear program (equation 4)), these are not achieved (realistic decentralized solution $CE(dz)$ (equation 3), darker graph). Figure 3 shows the results from networks generated randomly according to the parameter values in Table 4. The net benefits from standardization for the entire network are graphed against decreasing expected values for standardization costs $\mu(K)$ on the abscissa. In this constellation, both coordination regimes generate identical results when standardization costs are either very high or very low relative to network effects. At intermediate values, the standardization gap appears.

In a centrally coordinated network, all agents standardize if $\mu(K) \leq 34{,}000$ . In a decentrally coordinated network, agents standardize much later, that is, only at significantly lower standardization costs do they consider standardizing to be an advantageous strategy. Uncertainty about their partners' standardization behavior and therefore their ability to reap network effects implies the startup problem. At lower K ( $19{,}000 \geq \mu(K) \geq 16{,}700$ ), a few agents decide in favor of standardizing, but their partners do not. This results in a negative lag of the decentralized graph. The perpendicular distance between CE(z) and CE(dz) (the standardization gap) quantifies the magnitude of the standardization problem.

The airline manager introduced earlier could identify a standardization gap for firm internal data exchange standards.

<table><tr><td colspan="7">Table 4. Simulation Parameters (Basic Standardization Problem)</td></tr><tr><td> $\mu(c) = 1,000$ </td><td> $\sigma(c) = 200$ </td><td> $\mu(K) = \text{var.}$ </td><td> $\sigma(K) = 1,000$ </td><td>n = 35</td><td>T = 1</td><td>Q = 1</td></tr></table>

![](/api/attachments/8GXDM8C7/fulltext/images/14e64cfa0f57417c8b5aae3117e47497e2484b645342ffb5fa4ee03ce665f8d4.jpg)  
Figure 3. The Standardization Gap

His standardization problem turned out to be a welfare problem since the business units had to pay the standardization costs while the accounting system did not provide any way of assigning decision-relevant benefits to those units standardizing. Solving the standardization problem means closing the gap. In the solution section, one possible approach for closing the standardization gap is described.

## The Penguin Effect

Uncertainty about other agents' preferences can result in excess inertia, since early adopters bear a disproportionate share of transient incompatibility costs (Farrell and Saloner 1986, p. 940).

Regardless of others' preferences, there is no incentive for any individual agent to get the bandwagon rolling. This phenomenon is often called the penguin effect: "Penguins who must enter the water to find food often delay doing so because they fear the presence of predators. Each would prefer some other penguin to test the waters first" (Farrell and Saloner 1986, p. 943). To analyze this fundamental dynamic phenomenon, we extend the scenario to $T = 50$ periods.

The early standardization of some few agents in the first period implies a net deterioration for them but, at the same time, reduces uncertainty for those waiting, who then follow. Figure 4 shows how the dynamic closes the standardization gap partly over time. In the upper diagram, the results of the decentralized solution are given for the first and last simulated period. In every run, the stationary state was reached within 50 periods and no further standardization activities could be recognized. In the lower diagram of Figure 4, the third dimension represents time (t) to show the dynamics of the penguin effect as the “speed” of the diffusion process toward network equilibrium (stability; i.e., all agents cease changing their decisions). The diffusion process comes quite near to the final result within the very first periods.

## Diffusion Paths in Multi-Standard Problems

We can now extend the analysis further to include the choice between alternative standards $Q = 4$ . This allows the analysis of monopoly tendencies in standardization problems. Intuitively, the problem becomes more complex and further dynamics appear. As soon as there is a choice, there will be agents preferring standard 1 to standard 2, and so on, and vice versa (for identical $\mu(K)$ for all q). In a multi-period, multi-standard scenario, and given that agents can revise their standard choice in each period if they consider it advantageous, there is an additional standardization gap for lower standardization costs (Figure 5).

![](/api/attachments/8GXDM8C7/fulltext/images/9b1a2b17cb33337d1bc3414e0be3736f0eeed8612f53faaa4b58f36cf0fb0752.jpg)

![](/api/attachments/8GXDM8C7/fulltext/images/c5bec8ea3ab519c696b7c2abbbed1f5eb0bab381a2342011c5d70950f401812e.jpg)

<table><tr><td colspan="7">Table 5. Simulation Parameters</td></tr><tr><td> $\mu(c) = 1,000$ </td><td> $\sigma(c) = 200$ </td><td> $\mu(K) = \text{var.}$ </td><td> $\sigma(K) = 1,000$ </td><td>n = 35</td><td>T = 50</td><td>Q = 4</td></tr></table>

![](/api/attachments/8GXDM8C7/fulltext/images/a781f9c991c3c8f114998ddcd870bf217cff3d2743b5c1e5a6c3bcc777dc6230.jpg)  
Figure 5. Multi-Period, Multi-Standard Problem, t = 50

As before, centralized solution quality can almost be attained in a range of $\mu(K)=(5,000;17,000)$ . But with lower standardization costs there is a surprising sudden decline of CE. This is more dramatic the more different standards are available. To explain this phenomenon, we investigate the adaptation process toward the equilibrium in more detail below.

In each diagram of Figure 6, we can see exemplary distributions $s(q)$ (i.e., the number of agents having adopted standard q) of the four standards $(q = 1 \ldots 4)$ in the whole set of 35 actors over time for a particular parameterization (different $\mu(K)$ , which are given above the diagrams). The processes are described from the top left to the bottom right.

1. No standardization: This case of no standardization activities is identical to the startup problem in the one-standard case.

2. Mixed solution: Partly standardized networks are quite scarce even for Q > 1.

3. Monopoly: Complete network-wide standardization with the same standard. This monopoly situation dominates parts of the $\mu(K)$ scale but, contrary to common belief, not its entirety, especially not at low standardization costs.

4. Oligopoly: Complete standardization with different technologies. The stable multiple standard equilibrium replaces the monopoly at lower standardization costs. With this cost constellation, even “weaker” standards can resist the battling out process of “stronger” standards.

5. Dynamic equilibrium: No stationary state, (some) agents change technologies in a stable and repeated rhythm. Dynamic equilibria are possible only at very low standardization costs as compared to the network effects. At $\mu(K)=1,000$ , about 5 percent of all networks show dynamic equilibria. Here, agents become “technology hoppers.” An example is a two-player network with one player expecting the other to adopt a certain technology. At the same time, the partner changes his standards choice to the former technology of his partner, and so on.

Figure 7 gives an overview of the relative frequency of the different processes depending on $\mu(K)$ (based on 4,800 simulation runs). Decreasing the level of $\mu(K)$ to values lower than 4,000 promotes oligopolies to surpass monopoly. Because individual differences become more important, the probability of standard changes declines. This explains the second standardization gap if multiple standards are present.

![](/api/attachments/8GXDM8C7/fulltext/images/23ed76c0f0cc8910dcb604a4babf67936c70417134b0b7be3f2e758b6d373718.jpg)  
Figure 6. Five Possible Diffusion Paths

![](/api/attachments/8GXDM8C7/fulltext/images/c6f137f1acb49493b78289048bea2bfc62e53d731e034f8550a438460a56ac4b.jpg)  
Figure 7. Relative Occurrence of the Different Process Patterns at Different $\mu(K)$

To summarize the findings so far, we can formulate the conditions for startup problems and “market failure” in the realistic case of reversible multi-period, multi-standard problems as a standardization dilemma: if standardization costs are (too) high, there is a startup problem; if they are (too) low, there will be inefficient multi-standard equilibria.

## The Impact of Network Topology and Density

So far, we have analyzed general dynamics in standardization problems assuming a full-density user network. Consistent with most models of the network effect literature, this implies that each agent has interaction links to all others. In the literature review, we argued that this simplification might be a special case of the many relational network structures determining standard diffusion. Hence, we now analyze the influence of network structure. To incorporate the structural elements of networks, we introduce a new parameter $V(0 < V \leq 1)$ describing network density. The simulations are repeated at different densities to reveal the impact of network density on the diffusion process. To account for the impact of network topology when altering density, we use two substantially different structures adapted from Westarp and Wendt (2000):

1. Random topology: With probability V, edges are assigned positive values $c_{ij} \sim ND(\mu(c), \sigma(c))$ .

2. Close topology: Agents are randomly assigned to geographic coordinates on a unit square (even distribution). This results in $n*(n-1)$ edges. The shortest $V*100\%$ of all inter-agent connections are assigned strictly positive values (as before $c_{ij} \sim ND(\mu(c), \sigma(c))$ ). As a result, decreasing V leads to (increasingly) isolated clusters in the network.

For equal values of V, both structures have (on average) the same number of edges. A decision to adopt a standard has a more indirect influence on other agents' decisions in close topologies. The reason is that, on average, the shortest path between two network nodes is longer: more dominoes have to fall. Westarp (2003) argues that electronic markets will tend to resemble the random type of structure (“click distances”) since we select our partners by criteria other than just geographical distance. In contrast, physical proximity (or face to face communication within rather than between project teams) is still a very important factor for selecting business partners. Therefore, a close topology with its clustering property describes a real-world network structure much better than does the random topology (Weitzel et al. 2003; Westarp 2003).

Figure 8 shows both topologies for different V to visualize the clustering. One-sided relations are of a lighter color. We can now analyze the impact of network topology and density on the distribution of the diffusion patterns. In Figure 9, the resulting diffusion paths are determined when reducing V from 1.00 to 0.01 in increments of 0.03 at average standardization costs of 14,000 (upper diagrams) and 2,000 (lower diagrams). As it turns out, in close topologies (right diagrams), agents begin standardizing at a substantially lower network density. The explanation is that in a clustering structure the probability is higher than, with the same absolute number of links, these links are mutual. A real-life analogy is stronger communication between members of the same business unit than with colleagues in other countries. At low standardization costs, the impact of topology and density appears in different results compared to the basic model as well as between the topologies. There are quite different diffusion pattern developments, leading to the equilibria shown in Figure 9 (which consists of a total of over 10 million decisions by agents in 2,100 simulation runs per scenario).

Now it becomes clear that Figure 7 is the special case of Figure 9. Thus, the diagrams in Figure 9 could be connected orthogonally to Figure 7 at $\mu(K)=14,000$ (upper diagrams of Figure 9) and $\mu(K)=2,000$ (lower diagrams) where density is V=1.00. At high standardization costs (Figure 9, upper diagrams), both topologies are essentially identical. If in contrast (lower diagrams) average standardization costs are so low that for V=1.00 oligopolies can be expected, reducing network density has different effects depending on the network structure. In random topologies, monopoly rapidly replaces oligopoly, because reducing communication links does not substantially change the internal structure of the network. Hence, the network effect influence decreases for constant standardization costs. This is different for close topologies. Here, reducing V leads to more and more isolated clusters within the network. For that reason, oligopolies can persist better and the occurrence of monopoly declines. A single standard (first mover), therefore, has less power when penetrating those parts of a network where there are few communication links. Overall, it appears that standard diffusion and especially monopolization tendencies can be explained only partly without considering network structure as a main determinant.

The diverging results for different topologies imply that topology should be explicitly taken into account when promoting standards diffusion. For example, SAP has addressed its different (and quite independent) clusters of customers (i.e., the different branches) by addressing their particular industry-specific needs. As a result, SAP could successfully establish a quasi-monopoly despite the fact that the market shows a close topology structure (Westarp 2003). In this context, Damsgaard and Lyytinen (1998) have proposed a network-based analysis for investigating the diffusion of EDI.

<table><tr><td colspan="8">Table 6. Simulation Parameters</td></tr><tr><td> $\mu(c) = 1,000$ </td><td> $\sigma(c) = 200$ </td><td> $\mu(K) = 14,000$ </td><td> $\sigma(K) = 1,000$ </td><td>n = 35</td><td>T = 50</td><td>V = var.</td><td>Q = 1</td></tr></table>

<table><tr><td></td><td>V = 1.0 (1190 edges)</td><td>V = 0.8 (952 edges)</td><td>V = 0.4 (476 edges)</td><td>V = 0.1 (119 edges)</td></tr><tr><td>random topology</td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/c13578c5eb0ad3d1387ff914eea41c66eae79d7b34c75549cbd11733399b5723.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/46e60163752eccda0824af6d3973fad73819b23b0e9ee358d3930d20df5a9ef4.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/60ddc1caaf76bcef9d6d7088a4191dcf4e87229d5e696383f8f105807f5db965.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/4d04f5550f789e23f32bcaf79cd8910305ab82c995f1d685eb101d24f4907772.jpg"/></td></tr><tr><td>close topology</td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/2d0fce7165210024eae24da983f088a2a33e1c84b5810bd46e724a13454476e3.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/a09635d84c6fa2ec0f4f0bf24b6dc7bc90efd2081c0ea3dc60ea1d223180db3c.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/9f87134a40a4a223d8ad6e0a6b0b8adff45b621f8f67f7dd2ff298cd57187a53.jpg"/></td><td><img src="/api/attachments/8GXDM8C7/fulltext/images/6f28e975bda48167d46e1385f0cce9aca580b8e8c525cf6dd55c583c5775748b.jpg"/></td></tr></table>

Figure 8. Close and Random Topology in a Network of n = 35

## Solutions to Standardization Problems

## Reallocation of Standardization Costs and Benefits

How can the model be used to deduce normative results for standardization problems? It was shown that inefficiencies in standardization problems (i.e., a standardization gap) could result from insufficient local information or communication (ballot problem) or from the fact that standardization is not desirable from an individual but only from a centralized perspective (welfare problem). The latter case typically is found in large enterprises where business units perceive no incentive to invest from their autonomous IT budgets into standardization if standardization benefits are not (cannot be) accredited to the particular unit and rather accrue “somewhere” in the enterprise (asymmetric standardization cost and benefit distribution). In this case, the agency problem of how to synchronize individual and aggregate objective functions arises. One classic solution is profit-sharing to redistribute the costs and benefits of standardization systematically (Varian 1994). In the notation of the model, each business unit exchanges $K_{i}$ and $c_{ij}$ for a share $\alpha$ of the centralized net solution, so that the individual objective function changes

from $\sum_{\substack{j = 1\\ j\neq i}}^{n}\frac{c_{ji}\phi(j) - K_j}{c_{ji}\phi(j)} c_{ij} - K_i$ to $\alpha \cdot \left(\sum_{i = 1}^{n}\sum_{j = 1}^{n}c_{ij} - \sum_{i = 1}^{n}K_i\right)$ .

<table><tr><td colspan="8">Table 7. Simulation Parameters</td></tr><tr><td> $\mu(c) = 1,000$ </td><td> $\sigma(c) = 200$ </td><td> $\mu(K) = 2,000; 14,000$ </td><td> $\sigma(K) = 1,000$ </td><td>n = 35</td><td>T = 50</td><td>V = var.</td><td>Q = 4</td></tr></table>

![](/api/attachments/8GXDM8C7/fulltext/images/4dea39be6ba7771885b7576b8ae5e4a2e1541e0488ffdfcc30da8879b040e6d2.jpg)

![](/api/attachments/8GXDM8C7/fulltext/images/fc3a06bab89b1432d9656ed37d4a2ca6b3d659fe70281ceecf66e70c30c83b02.jpg)

![](/api/attachments/8GXDM8C7/fulltext/images/8ecd7e17a3aa9c402f452373a0d245675a7964919f543ebf7c9200c88f0a8def.jpg)

![](/api/attachments/8GXDM8C7/fulltext/images/1643b7c32502e971d4bc1da202fc9805ac4c27da4cc34e032bb051b5ae05499b.jpg)

Figure 9. Distribution of Diffusion Processes at Different V

Theoretically, the solution guarantees a positive standardization return on investment (ROI) to all participating agents, making standardization a locally dominant solution. Unfortunately, this approach relies on rarely available accountable standardization benefits. As one project of the authors with a network of six banks showed, there are three main reasons why this approach is problematic. First, all agents feared that their contribution to the common solution was higher than the contribution of others (e.g., complaining about absolute versus relative network gains). The rejection of guaranteed improvements (i.e., failing to jointly solve the ballot problem) is an interesting instance of irrational decision behavior. Second, cost center structures can aggravate the problem because, by definition, they are not rewarded for benefits. This experience matches with Damsgaard and Lyytinen's conjecture, based on EDI case studies, that “subsidies are neither necessary nor sufficient to facilitate EDI diffusion” (2001, p. 206). Third, the approach relies on rarely available accountable standardization benefit data. At the same time, our model revealed a major benefit in practical application to an extent we did not expect. By modeling the actual standardization problem, all the managers affected became aware for the first time of the extent of their interrelatedness and, for the first time, everyone was talking about one common problem in a common language. In some sense, the network effects became visible and the model turned out to be not the solution but the prerequisite for a roundtable.

## Utilizing a Pre-Standardized Installed Base

The standardization manager of the airline introduced earlier had realized that he had to rule out a centralized approach. The reason was prohibitive controlling and monitoring costs and the acknowledgment that the globally distributed business units simply did not cooperate, despite theoretical hierarchical authority. In particular, aggressive waiting was an often-witnessed strategy used by units trying to avoid adopting a standard or upgrading to the universally required version of a technology. The airline had accepted internal and external standardization as a main challenge and considered only a largely decentralized approach to be promising.

We developed the idea that one possible way of shrinking the standardization gap is to try to identify certain parts of a network that can be used as a stepping stone to initiate further favorable diffusion processes. The plan was to take a limited number of business units and force them to standardize or subsidize their adoption activities, as it is also proceeded by industry associations in interorganizational standardization problems (e.g., in the case of EDI diffusion) (Damsgaard and Lyytinen 2001). To put it more simply: Which dominoes should be tipped to overcome the startup problem? We used our model to evaluate this strategy's chance of success. To capture the installed base, a new variable $B$ ( $0 \leq B \leq 1$ ) is introduced with $B > 0$ as the fraction of the network already using a standard. In addition, to guarantee formal homogeneity with the former simulations, a new period $t = 0$ is introduced during which the pre-standardization activities are supposed to have happened. The simulations comprise three scenarios with different values of $B$ , respectively: (I) the largest agents are pre-standardized, (II) random agents are pre-standardized, and (III) the smallest agents are pre-standardized with size(i) = $\sum_{\substack{j=1 \\ j \neq i}}^{n} c_{ij}$ . The scenarios were simula-

lated simultaneously to guarantee networks of identical cost structure for each run. For every new value of B, simulations were made using a different random seed. Figure 10 shows the section similar to the lower diagram of Figure 4. The legend lists the graphs in the same order as shown in the diagram (from left to right).

Compared to the results without pre-standardization, introducing an installed base of B = 0.1 shifts the startup problem toward higher costs, while the shrinking of the standardization gap is surprisingly small. Considering that at B = 0.3, almost a third of the firm would have to be pre-standardized, which leads to the closing of about only 15 percent of the standardization gap (in the centralized solution the actors standardize at $\mu(K) < 34{,}000$ (Figure 3), in the decentralized solution at $\mu(K) < 18{,}000$ (Figure 10, right graph) and in the decentralized solution with B = 0.3 at $\mu(K) < 21{,}500$ (Figure 10, outer left graphs), the limited impact suggests that establishing an installed base to get some decentralized diffusion dynamics going is questionable. The finding that an installed base has a quite limited impact on the success of a standard supports the empirical findings of Hidding and Williams (2003), suggesting that there are no first-mover advantages in business-to-business information technology products. Nevertheless, one interesting finding of our analysis is that structure III dominates II, which dominates I. In other words, the worst idea is pre-standardizing big players. This is surprising at first, since conventional wisdom suggests that large players standardize first, causing the smaller remainder to follow. But here the logic is quite the opposite. Pre-standardizing the large players means that the remaining network is left with agents suffering from a worse benefit-cost ratio. They do not care about the size of installed base agents, because their $p_{ij}$ are 1 and, anyway, they must bear their own standardization costs. But if small agents are pre-standardized as an installed base, those left to decide are those with a higher propensity to standardize. As a result, large players will standardize at even higher $\mu(K)$ . Therefore, this phenomenon does not result from the structure of the installed base but rather from the structure of the rest of the network.

Applying these findings to problems of infrastructure subsidies and SME integration (e.g., trying to foster e-commerce) could be an interesting area of further research. Are there particular SMEs for which it is structurally more advantageous to subsidize?

Table 9 summarizes the main findings so far. In the next section, model validity and limitations to its applicability are critically discussed.

## Validation and Limitations of the Approach

## Validation

The model and the subsequent simulation analysis were used to reveal the conditions of standards diffusion patterns. The simulations proved our main hypotheses that startup problems and single-standard monopolies, in particular, are not as prevalent as would be expected from the literature and that structural network elements exert a substantial influence on standards diffusion. Using computer laboratories has great advantages, as this approach allows us to handle highly complex, dynamic, and discrete choice problems as well as the analysis of simultaneous parameter variations. Methodologically, this approach has been called the paradigm of agent-based computational economics (ACE) (Tesfatsion 2002, 2006). It is the computational study of economies modeled as evolving systems of autonomous interacting agents (Tesfatsion 2006).

<table><tr><td colspan="9">Table 8. Simulation Parameters</td></tr><tr><td> $\mu(c) = 1,000$ </td><td> $\sigma(c) = 200$ </td><td> $\mu(K) = \text{var.}$ </td><td> $\sigma(K) = 1,000$ </td><td>n = 35</td><td>T = 35</td><td>V = 1.0</td><td>B = 0.1; 0.2; 0.3</td><td>Q = 1</td></tr></table>

![](/api/attachments/8GXDM8C7/fulltext/images/fb1109223740c3df8534361574d5067cc2a951263d87a8b3a8e033d574690903.jpg)  
Figure 10. Different Installed Bases

As applied in this work, computational models allow one to analyze the impact of a variety of local and global influences on system behavior simultaneously in a way that is otherwise very difficult to accomplish. One principal concern of ACE researchers is to understand why certain global regularities have been observed to evolve and persist in “decentralized market economies despite the absence of top-down planning and control” and “to demonstrate constructively how global regularities might arise from the bottom up, through the repeated local interactions of autonomous agents” (Tesfatsion 2002b, p. 56). This methodological approach thus focuses on how structures emerge in decentralized networks rather than being explicitly planned and rationally implemented. But this comes with the requirement that simulation models must somehow be validated. The role of validation is to demonstrate that the model is a reasonable representation of the actual system. Drawing on Sargent (1998) and Naylor and Finger (1967), we use a three-stage validation approach.

(1) Conceptual model validity: Do model assumptions conform to theory and observations? This stage focuses on internal coherence in that causal relations are “reasonable” and fit with existing theory. The simulation model is a straight implementation of the analytical model that is based on network effect theory and fundamental assumptions of decision behavior (e.g., cost/utility comparison). Game theory equilibrium analysis has shown the general properties expected from the literature.

(2) Model verification: Is the implementation of the conceptual model correct? Besides structured walks through the program and test runs with extreme values, the simulation model has been implemented independently by three individuals, including one implementation in a different programming language. All yielded identical results.

(3) Operational validity: Are the simulation results reasonable and how do they fit the real world? The simulation results allow us to explain coherently many isolated findings in the literature, which indicates that the “model’s output behavior has the accuracy required for the model’s intended purpose over the domain of its intended applicability” (Sargent 1998, p. 125). Concerning external validity, applying the model to EDI diffusion in the United States and Germany resulted in a correct prediction of market structure (for empirical diffusion data on EDI, see Westarp 2003). The model was used successfully to capture and predict standardization problems and phenomena in the domains of mobile commerce, EDI and business-to-business integration, directory services, and Intranet planning.

<table><tr><td colspan="4">Table 9. Summary of Findings</td></tr><tr><td>Research Question</td><td>Reference</td><td>Answer</td><td>Implication</td></tr><tr><td>What are causes of standardization problems, and how can their magnitude—available standardization gains—be operationalized?</td><td>Arthur 1983, 1989; Besen and Farrell 1994; Braunstein and White 1985; Farrell and Saloner 1985, 1986, 1987; Gandal 1994; Hartmann and Teece 1990; Katz and Shapiro 1985, 1986, 1992, 1994; Kindleberger 1983; Leibenstein 1950</td><td>Asymmetry between individual and collective standardization gains; multiple equilibriaStandardization gap as difference between theoretical first-best and realistic second-best standardization outcome, determines maximum possible coordination gains</td><td>Depending on the situation, some available standardization gains can be internalized by communication (ballot problem → identify affected agents, arrange roundtable).Others require an explicit redistribution of standardization costs and benefits (welfare problem → side payments).Consortia could provide institutional settings for binding agreements between agents.</td></tr><tr><td>What impacts do variance in individual standardization costs and network effects have on standard diffusion?</td><td>Arthur 1983, 1989; David and Greenstein 1990; Farrell and Saloner 1985, 1986, 1987; Goldenberg and Efroni 2001; Katz and Shapiro 1985, 1986; Kindleberger 1983; Wiese 1990</td><td>Five possible diffusion pathsFor high and low standardization costs (as compared to network effects) monopoly outcome is quite rareUnfortunate decisions for agents in decentralized networks at low standardization costs</td><td>For high standardization costs (compared to network effects), standard adoption is less likely in decentrally coordinated networks (→ business units with autonomous IT/standardization budgets will often show aggressive waiting, i.e., refuse to adopt standards).Impact of installed base is rather low, especially at low standardization costs, first-mover advantage is limited (→ do not expect business units or supply chain partners to simply follow).The higher the number of standards to choose, the worse decentralized standardization decisions are at low standardization costs (→ at this constellation, decentralized coordination is not likely to result in one single data/document exchange format within a firm or among business partners).</td></tr><tr><td>What are the impacts of network topologies on standard diffusion?</td><td>Coleman et al. 1957; Damsgaard and Lytinen 1998; Goldenberg and Efroni 2001; Valente 1995; Westarp 2003; Westarp and Wendt 2000</td><td>Substantial topology impactMulti-standard diffusion outcomes are more likely in close (clustering) topologiesSimultaneous impact of network topology, density, and standardization costs on outcome</td><td>No domino effects in close topologies (→ following an analysis of network topology, appropriate strategies have to be chosen such as tackling each cluster separately by setting cluster-specific incentives; this is what SAP did with its ERP solution (Westarp 2003)).</td></tr></table>

## Limitations

Still, there is always the risk of idiosyncratic findings that preclude thorough generalization (Eisenhardt 1989). One substantial restriction is that, strictly speaking, the findings are limited to situations in which standard diffusion can be explained solely by direct network effects. Obviously, practical applications reveal that technology adoption is influenced strongly by nonrational factors. From a theoretical perspective, to consider in particular some of the largely neglected negative network effects would most probably influence the results. Among the reasons for negative network effects could be a loss of individuality (Thum 1995) and an associated decline in relative competitive position as proposed in some contexts by the resource-based view of IT. Exclusively modeling positive externalities favors coordination games, while allowing negative effects would increase the probability of games with completely diverging interests (dis-coordination games). Finally, an integration of the research strands in Figure 1 is necessary to incorporate the impact of vendor-side dynamic pricing strategies (Westarp 2003) and organizations developing and regulating standards.

While it is truly difficult to quantify the various benefits and costs associated with standards in general, there are domains that offer quite rich empirical grounds, especially EDI (Emmelhainz 1993). One study with Fortune 1000 enterprises from the United States reveals average standardization costs ( $K_i$ ) of \$457,000 and network effect benefits ( $\mathcal{E}_{ij}$ ) of \$3,218,000 (Westarp et al. 1999). Still, in many cases the data necessary for the model might be quite intricate to retrieve (e.g., due to secrecy concerns or large network size) or to specify (e.g., what are the network effect benefits of using a Web browser). Also, the accounting system asymmetry between hard costs and soft benefits is a similar problem that makes solving standardization problems difficult as there is the additional challenge of defining what the “corporate currency” for possible side payments could be. This is not a real limitation of the model but of the direct relevance of its results for corporate practice. The same accounts for particular governance and organizational structures (e.g., cost center organization prevents regular investment decisions), and power issues that are not addressed by our model but that certainly shape corporate standardization problems. Damsgaard and Lyytinen (2001), for example, find that “power dependencies between and within the institutional actors affect the speed and direction of the EDI diffusion process” (p. 204). While it is no problem to incorporate the result of many of these influences when modeling one particular standardization problem by restricting certain agents’ decisions (like in the installed base simulations by “forcing” some agents to standardize), these impacts would still not be part of the agents' objective function. That is why we expect substantial contributions to standardization research from cooperative and evolutionary game theory. Another limitation of the model, which was already mentioned, is the inability to simultaneously represent agents on different aggregate levels, for example, representing firms as deciders and their internal structure of autonomous deciders (firm-internal departments or single users) in the same model. To address many of these practical concerns, insights from the accounting and control literature could help in making standardization costs and benefits visible and thereby more relevant for decentralized corporate decisions. At the same time, this will make cooperative games to achieve centralized solution quality more likely. Another issue not considered in our model is the impact of standard vendor strategies and especially changing pricing strategies on decentralized standardization decisions. So far, the vendor side is held constant. To incorporate vendor decisions and to simultaneously analyze vendor and user decisions (right side of Figure 1), the standardization model could be merged with a vendor side model. See Weitzel et al. (2003) for a fusion of the basic model presented in this paper with the software vendor model of Westarp (2003).

## Conclusion

We used a unified analytical model and computer simulations to better understand the dynamics of standard diffusion. The paper makes three contributions to the literature: (1) it formulates a unified formal model of standardization situations, (2) it demonstrates and operationalizes the origins of user-side standardization problems in the standardization gap with the associated ballot and welfare problems, and (3) it formulates a way to introduce network topology into the analysis. With this model, we can identify cogently conditions under which many well-known standardization situations emerge. The analysis shows, in contrast to the past literature, that one-standard monopolies are anything but common. Especially in clustering topologies, monopolies can be expected to emerge only in high-density networks at relatively high standardization costs. Our studies discern a fundamental standardization dilemma: if standardization cost is (too) high, we face the startup problem; if it is (too) low, we will face inefficient multi-standard equilibria.

The proposed model proved to be sufficiently flexible in proposing and evaluating effective solution strategies for a variety of corporate standardization problems. Nevertheless, many challenges remain. One important implication is to encourage multidisciplinary research. There is a lot to be learned from economics, managerial accounting, and coordination theory about the quantification of network effects, strategies to solve the ballot and welfare problem, and rendering standardization benefits accounted and thereby tradable. The research paradigm of agent-based computational economics seems capable of coping with the complexities that arise when individual motives and decisions intertwine with network level behaviors. In addition, as ballot problems turned out to be more frequent than welfare problems, we expect more detailed contributions from research into the role of consortia for standards creation and, especially, diffusion.

In conclusion, we need research into areas that go beyond providing basic building blocks for articulating standardization problems. Ultimately, an integration of the multiple strands summarized in Figure 1 into a unified theory of standardization is desirable for analyzing simultaneously decentralized adoptions and the impacts of standard consortia and vendor-side strategies. For this, the ACE research approach seems promising.

## Acknowledgments

The authors would like to acknowledge the excellent direction and insights provided by the senior editor, Kalle Lyytinen, and the important contributions of the associate editor and the anonymous reviewers. We are also indebted to the German National Science Foundation (DFG) and the E-Finance Lab for their support.

## References

Arthur, W. B. “Competing Technologies, Increasing Returns, and Lock-in by Historical Events,” The Economic Journal (99:394), March 1989, pp. 116-131.

Arthur, W. B. “Competing Technologies and Lock-In by Historical Small Events: The Dynamics of Allocation under Increasing Returns,” Paper 43, Stanford Center for Economic Policy Research, Stanford, CA, 1983.

Arthur, W. B. “Increasing Returns and the New World of Business,” Harvard Business Review (74:4), July-August 1996, pp. 100-109.

Bakos, Y., and Brynjolfsson, E. “Bundling Information Goods: Pricing, Profits and Efficiency,” Management Science (45:12), December 1999, pp. 1613-1630.

Beck, R., and Weitzel, T. “Some Economics of Vertical Standards: Integrating SMEs in EDI Supply Chains,” Electronic Markets (14:4), 2005, pp. 313-322.

Beimborn, D., Lamberti, H.-J., and Weitzel, T. “Game Theoretical Analysis of Cooperative Sourcing Scenarios,” in Proceedings of the 39 $^{th}$ Hawaii International Conference on System

Sciences, IEEE Computer Society Press, Los Alamitos, CA, January 4-7, 2006.

Besen, S. M., and Farrell, J. “Choosing How to Compete: Strategies and Tactics in Standardization,” Journal of Economic Perspectives (8:2), Spring 1994, pp. 117-131.

Besen, S. M., and Johnson, L. L. “Compatibility Standards, Competition, and Innovation in the Broadcasting Industry,” R-3453-NSF, RAND Corporation, Santa Monica, CA, 1986.

Braunstein, Y. M., and White, L. J. “Setting Technical Compatibility Standards: An Economic Analysis,” Antitrust Bulletin (30:2), 1985, pp. 337-355.

Buxmann, P. Standardisierung betrieblicher Informationssysteme (Standardization of Business Information Systems), Gabler, Wiesbaden, Germany, 1996.

Church, J., and Gandal, N. “Network Effects, Software Provision, and Standardization,” Journal of Industrial Economics (40:1), March 1992, pp. 85-103.

Coleman, J. S., Menzel, H., and Katz, E. “The Diffusion of an Innovation among Physicians,” Sociometry (20:4), 1957, pp. 253-270.

Cooper, R., DeJong, D., Forsythe, R., and Ross, T. “Communication in the Battle of the Sexes Game: Some Empirical Results,” Rand Journal of Economics (20), 1989, pp. 568-587.

Crane, R. The Politics of International Standards: France and the Color TV War, Ablex, Norwood, NJ, 1979.

Damsgaard, J., and Lyytinen, K. “Contours of Diffusion of Electronic Data Interchange in Finland: Overcoming Technological Barriers and Collaborating to Make it Happen,” Journal of Strategic Information Systems (7:4), Winter 1998, pp. 275-297.

Damsgaard, J., and Lyytinen, K. “The Role of Intermediating Institutions in the Diffusion of Electronic Data Interchange (EDI): How Industry Associations Intervened in Denmark, Finland, and Hong Kong,” The Information Society (17:3), July-September 2001, pp. 195-210.

David, P. A., and Greenstein, S. “The Economics of Compatibility Standards: An Introduction to Recent Research,” Economics of Innovation and New Technology (1:1), 1990, pp. 3-41.

Domschke, W., and Wagner, B. “Models and Methods for Standardization Problems,” European Journal of Operational Research (162:3), May 2005, pp. 713-726.

Economides, N., and White, L. “One-Way Networks, Two-Way Networks, Compatibility, and Antitrust,” Discussion Paper EC-93-14, Stern School of Business, New York University, New York, 1993.

Eisenhardt, K. M. “Building Theories from Case Study Research,” Academy of Management Review (14:4), October 1989, pp. 532-550.

Emmelhainz, M. A. EDI: A Total Management Guide ( $2^{nd}$ ed.), Van Nostrand Reinhold, New York, 1993.

Farrell, J. “Cheap Talk, Coordination and Entry,” Rand Journal of Economics (18:1), Spring 1987, pp. 34-39.

Farrell, J., and Saloner, G. “Competition, Compatibility, and Standards: The Economics of Horses, Penguins, and Lemmings,” in Product Standardization and Competitive Strategy, H. L. Gabel (ed.), North-Holland, Amsterdam, 1987, pp. 1-21.

Farrell, J., and Saloner, G. “Coordination through Committees and Markets,” Rand Journal of Economics (19:2), Summer 1988, pp. 235-252.

Farrell, J., and Saloner, G. “Installed Base and Compatibility: Innovation, Product Preannouncements, and Predation,” The American Economic Review (76:5), December 1986, pp. 940-955.

Farrell, J., and Saloner, G. “Standardization, Compatibility, and Innovation,” Rand Journal of Economics (16:1), Spring 1985, pp. 70-83.

Frenzen, J., and Nakamoto, K. “Structure, Cooperation, and the Flow of Market Information,” Journal of Consumer Research (20:3), December 1993, pp. 360-75.

Gabel, H. L. Competitive Strategies for Product Standards: The Strategic Use of Compatibility Standards for Competitive Advantage, McGraw-Hill, London, 1991.

Gaillard, J. Industrial Standardization, its Principles and Applications, H. W. Wilson Co., New York, 1934.

Gandal, N. “Hedonic Price Indexes for Spreadsheets and Empirical Test for Network-Externalities,” Rand Journal of Economics (25:1), Spring 1994, pp. 160-170.

Goldenberg, J., and Efroni, S. “Using Cellular Automata Modeling of Emergence of Innovations,” Technological Forecasting and Social Change (68:3), November 2001, pp. 293-308.

Harsanyi, J. C. “Games with Incomplete Information Played by ‘Bayesian’ Players, Parts I-III. Part I: The Basic Model,” Management Science (14:3), November 1967, pp. 159-182.

Harsanyi, J. C. “Games with Incomplete Information Played by ‘Bayesian’ Players, Parts I-III. Part II: Bayesian Equilibrium Points,” Management Science (14:5), January 1968a, pp. 320-334.

Harsanyi, J. C. “Games with Incomplete Information Played by ‘Bayesian’ Players, Parts I-III. Part III: The Basic Probability Distribution of the Game, Management Science (14:7), March 1968b, pp. 486-502.

Hartmann, R. S., and Teece, D. J. “Product Emulation Strategies in the Presence of Reputation Effects and Network Externalities: Some Evidence from the Minicomputer Industry,” Economics of Innovation and New Technology (1:1/2), 1990, pp. 157-182.

Hemenway, D. Industry Wide Voluntary Product Standards, Ballinger, Cambridge, MA, 1975.

Hidding, G., and Williams, J. “Are There First-Mover Advantages in B2B eCommerce Technologies?” in Proceedings of the 36 $^{th}$ Hawaii International Conference on System Sciences, IEEE Computer Society Press, Los Alamitos, CA, January 6-9, 2003.

Jakobs, K., Procter, R., and Williams, R. “Users and Standardization: Worlds Apart? The Example of Electronic Mail,” StandardView (4:4), December 1996, pp. 183-191.

Kaldor, N. “Welfare Propositions of Economics and Interpersonal Comparisons of Utility,” Economic Journal (49:195), September 1939, pp. 549-552.

Katz, M. L., and Shapiro, C. “Network Externalities, Competition, and Compatibility,” The American Economic Review (75:3), June 1985, pp. 424-440.

Katz, M. L., and Shapiro, C. “Product Introduction with Network Externalities,” Journal of Industrial Economics (40:1), March 1992, pp. 55-83.

Katz, M. L., and Shapiro, C. “Systems Competition and Network Effects,” Journal of Economic Perspectives (8:2), Spring 1994, pp. 93-115.

Katz, M. L., and Shapiro, C. “Technology Adoption in the Presence of Network Externalities,” Journal of Political Economy (94:4), August 1986, pp. 822-841.

Kindleberger, C. P. “Standards as Public, Collective and Private Goods,” Kyklos—International Review for Social Sciences (36:3), Summer 1983, pp. 377-396.

Kleinemeyer, J. Standardisierung zwischen Kooperation und Wettbewerb (Standardization: Between Cooperation and Competition), Peter Lang, Frankfurt, Germany, 1998.

Leibenstein, H. “Bandwagon, Snob, and Veblen Effects in the Theory of Consumers Demand,” Quarterly Journal of Economics (64:2), May 1950, pp. 183-207.

Lewis, D. Convention: A Philosophical Study, Blackwell, Oxford, England, 1969.

Liebowitz, S. J., and Margolis, S. E. “Are Network Externalities a New Source of Market Failure?,” in Research in Law and Economics, Volume 17, R. O. Zerbe and W. Kovacic (eds), JAI Press, Greenwich, CT, 1995a, pp. 1-22.

Liebowitz, S. J., and Margolis, S. E. “Path Dependence, Lock-In, and History,” Journal of Law, Economics and Organization (11:1), April 1995b, pp. 205-226.

Liebowitz, S. J., and Margolis, S. E. Winners, Losers & Microsoft: Competition and Antitrust in High Technology, The Independent Institute, Oakland, CA, 1999.

Luce, R. D., and Raiffa, H. Games and Decisions: Introduction and Critical Survey, Dover Publications, New York, 1957.

Matutes, C., and Regibeau, P. “Mix and Match: Product Compatibility Without Network Externalites,” Rand Journal of Economics (19:2), Summer 1988, pp. 221-234.

Matutes, C., and Regibeau, P. “A Selective Review of the Economics of Standardization, Europe,” Journal of Political Economy (12:2), April 1996, pp. 183-209.

Naylor, T. H., and Finger, J. M. “Verification of Computer Simulation Models,” Management Science (14:2), October 1967, pp. B92-B101.

Oren, S. S., and Smith, S. A. “Critical Mass and Tariff Structure in Electronic Communications Markets,” Bell Journal of Economics (12:2), Autumn 1981, pp. 467-87.

Reingen, P. H., and Kernan, J. B. “Analysis of Referral Networks in Marketing: Methods and Illustration,” Journal of Marketing Research (23:4), August 1986, pp. 370-378.

Rohlfs, J. “A Theory of Interdependent Demand for a Communications Service,” Bell Journal of Economics (5:1), Spring 1974, pp. 16-37.

Sargent, R. “Verification and Validation of Simulation Models,” in Proceedings of the 30 $^{th}$ Winter Simulation Conference, IEEE Computer Society Press, Los Alamitos, CA, December 11-14, 1998, pp. 121-130.

Shapiro, C., and Varian, H. R. Information Rules: A Strategic Guide to Network Economy, McGraw-Hill, Boston, 1998.

Tesfatsion, L. “Agent-Based Computational Economics: Growing Economics from the Bottom Up,” Artificial Life (8:1), Winter 2002, pp. 55-82.

Tesfatsion, L. “Agent-Based Computational Economics: Growing Economies from the Bottom Up,” unpublished paper, April 2006 (available at http://www.econ.iastate.edu/tesfatsi/ace.htm).

Thum, M. Netzwerkeffekte, Standardisierung und staatlicher Regulierungsbedarf (Network Effects, Standardization, and Regulation), JCB Mohr, Tübingen, 1995.

Valente, T. W. Network Models of the Diffusion of Innovations, Hampton Press, Cresskill, NJ, 1995.

Varian, H. “A Solution to the Problem of Externalities When Agents Are Well-Informed,” American Economic Review (84:5), December 1994, pp. 1278-1293.

Weber, S. Information Technology in Supplier Networks: A Theoretical Approach to Decisions about Information Technology and Supplier Relationships, Physica, Frankfurt, Germany, 2000.

Weitzel, T., Wendt, O., and Westarp, F. v. “Reconsidering Network Effect Theory,” in ECIS 2000—A Cyberspace Odyssey, Proceedings of the 8 $^{th}$ European Conference on Information Systems, H. R. Hansen, M. Bichler, and M. Mahrer (eds.), Vienna, Austria, July 3-5, 2000, pp. 484-491.

Weitzel, T., Wendt, O., Westarp, F. v., and König, W. “Network Effects and Diffusion Theory—Extending Economic Network Analysis,” The International Journal of IT Standards & Standardization Research (1:2), July 2003, pp. 1-21.

Westarp, F. v. Modeling Software Markets: Empirical Analysis, Network Simulations, and Marketing Implications, Springer, New York, 2003.

Westarp, F. v., Buxmann, P., Weitzel, T., and König, W. “The Management of Software Standards in Enterprises—Report of an Empirical Study in Germany and the US,” Working Paper 1999-10, Institute of Information Systems, Johann Wolfgang Goethe University, Frankfurt, Germany, 1999.

Westarp, F. v., and Wendt, O. “Diffusion Follows Structure—A Network Model of the Software Market,” in Proceedings of the 33 $^{rd}$ Hawaii International Conference on System Sciences, IEEE Computer Society Press, Los Alamitos, CA, January 4-7, 2000.

Wiese, H. Netzeffekte und Kompatibilität—Eine theoretische und simulationsgeleitete Analyse zur Absatzpolitik für Netzeffekt-Güter (Network Effects and Compatibility—A Theoretical and Simulative Analysis of Marketing Policy for Network Effect Goods), Poeschel, Stuttgart, 1990.

Yang, Y. Essays on Network Effects, unpublished Ph.D. dissertation, Department of Economics, Utah State University, Logan, UT, 1997.

## About the Authors

Tim Weitzel is Professor of Information Systems at Bamberg University in Germany. He received his Ph.D. from Goethe University in Frankfurt, Germany, where he was head of a variety of research and consulting projects on standardization, e-business and e-recruiting. Tim is the author of over 60 reviewed articles and four books on standards, outsourcing, IT management and alignment, e-finance, and e-HR.

Daniel Beimborn graduated in Economics and Business Administration at Goethe University, Frankfurt, where he works as a research assistant at the Institute of Information Systems (www.is-frankfurt.de). He is member of the postgraduate program 492 "Enabling Technologies for Electronic Commerce" of the German Science Foundation (DFG). His research interests include business process outsourcing in financial industries, controlling and standardization of IS infrastructures and especially the impact of web services technologies on their design. More information about Daniel's work can be found at www.beimborn.de.

Wolfgang Koenig received his Ph.D. from Goethe University in Frankfurt in 1980 (“Hardware-Supported Parallelization of Information Systems”) and completed his habilitation thesis in 1985 (“Strategic Planning of the Information Systems Infrastructure”). After 6 years as a professor of Information Systems at the Koblenz School of Corporate Management, he became a professor of Information Systems at Frankfurt University, in the Economics and Business Administration Faculty. Wolfgang has been the chair of the E-Finance Laboratory Frankfurt am Main since 2003. He serves as editor-in-chief of the leading German IS journal Wirtschafts-informatik. His research interest is in standardization, networking, and e-finance.

## Appendix

## Description of Used Variables and Parameters

<table><tr><td></td><td>One-Standard Model</td><td>Multi-Standard Model</td></tr><tr><td>Number of agents</td><td colspan="2">n (agent index: i, j)</td></tr><tr><td>Simulation horizon</td><td colspan="2">T (period index: t)</td></tr><tr><td>Number of neighbors of agent i</td><td colspan="2"> $\phi(i)$ </td></tr><tr><td>Network density</td><td colspan="2">0 &lt; V ≤ 1</td></tr><tr><td>Normally distributed stochastic variable a (representing any stochastic variable) with expectation and standard deviation</td><td colspan="2">a ~ ND( $\mu(a), \sigma(a)$ )</td></tr><tr><td>Agent&#x27;s size</td><td colspan="2">size(i) =  $\sum_{\substack{j=1 \\ j \neq i}}^{n} c_{ij}$ </td></tr><tr><td>Number of standards</td><td>1</td><td>Q (standard index: q)</td></tr><tr><td>Standardization costs</td><td> $K_i$ </td><td> $K_{iq}$ </td></tr><tr><td>Net benefits from standardization per communication link</td><td colspan="2"> $c_{ij}$ </td></tr><tr><td>Standardization indicator (binary variable)</td><td> $x_i(x_i = 1 \text{ if standardized}, x_i \text{ else})$ </td><td> $x_{iq}(x_{iq} = 1 \text{ if adopted standard } q, x_{iq} = 0 \text{ else})$ </td></tr><tr><td>Auxiliary binary variable</td><td> $y_{ij} \left( y_{ij} = 1 - (x_i * x_j) \right)$ </td><td> $y_{ij} \left( y_{ij} = \min_{q} (1 - (x_{iq} * x_{jq})) \right)$ </td></tr><tr><td>Probability that neighbor j adopts the standard (q)</td><td> $p_{ij}$ </td><td> $p_{ijq}$ </td></tr><tr><td>Total individual benefits of standardization</td><td> $E_i = \sum_{\substack{j=1 \\ j \neq i}}^{n} c_{ij} \cdot x_j - K_i$ </td><td> $E_{iq} = \sum_{\substack{j=1 \\ j \neq i}}^{n} c_{ij} \cdot x_{jq} - K_{iq}$  $E_i = \sum_{q=1}^{Q} E_{iq}$ </td></tr><tr><td>Total network-wide net benefits of standardization</td><td> $CE = \sum_{i=1}^{n} E_i$ </td><td> $CE = \sum_{i=1}^{n} E_i = \sum_{q=1}^{Q} \sum_{i=1}^{n} E_{iq}$ </td></tr><tr><td>Pre-standardized fraction of the network</td><td>0 ≤ B ≤ 1</td><td></td></tr><tr><td>Number of agents having adopted standard q</td><td></td><td>s(q)</td></tr><tr><td>Results of centralized | decentralized solution</td><td colspan="2">z | dz</td></tr></table>
