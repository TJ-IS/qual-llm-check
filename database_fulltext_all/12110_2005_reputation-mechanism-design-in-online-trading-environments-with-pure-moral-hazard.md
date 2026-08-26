---
otero_id: 12110
otero_key: "6CQX4NJT"
title: "Reputation Mechanism Design in Online Trading Environments with Pure Moral Hazard"
authors: "Chrysanthos Dellarocas"
year: "2005"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0054"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [69.166.47.134] On: 13 December 2014, At: 01:28 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## 6SR

![](/api/attachments/6CQX4NJT/fulltext/images/ce1674710a8f5490fdaf136b991d9a8a8409c4ca106d37d5390f0fd470c4eee3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Reputation Mechanism Design in Online Trading Environments with Pure Moral Hazard

Chrysanthos Dellarocas,

To cite this article:

Chrysanthos Dellarocas, (2005) Reputation Mechanism Design in Online Trading Environments with Pure Moral Hazard. Information Systems Research 16(2):209-230. http://dx.doi.org/10.1287/isre.1050.0054

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2005 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6CQX4NJT/fulltext/images/d62271749a839652ac04aaaf9a2439091570f1d5b849427ae373472e2faa5240.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Reputation Mechanism Design in Online Trading Environments with Pure Moral Hazard

Chrysanthos Dellarocas

R. H. Smith School of Business, University of Maryland, College Park, Maryland 20742, cdell@rhsmith.umd.edu

his paper offers a systematic exploration of reputation mechanism design in trading environments with opportunistic sellers of commonly known cost and ability parameters, imperfect monitoring of a seller’s actions, and two possible seller effort levels, one of which has no value to buyers. The objective of reputation mechanisms in such pure moral hazard settings is to induce sellers to exert high effort as often as possible. I study the impact of various mechanism parameters (such as the granularity of solicited feedback, the format of the public reputation profile, the policy regarding missing feedback, and the rules for admitting new sellers) on the resulting market efficiency. I find that maximum efficiency is bounded away from the hypothetical first best case where sellers can credibly precommit to full cooperation by a factor that is related to the probability that cooperating sellers may receive “unfair” bad ratings. Furthermore, maximum efficiency is independent of the length of past history summarized in a seller’s public reputation profile. I apply my framework to a simplified model of eBay’s feedback mechanism and conclude that, in pure moral hazard settings, eBay’s simple mechanism is capable of inducing the maximum theoretical efficiency independently of the number of recen ratings that are being summarized in a seller’s profile. I derive optimal policies for dealing with missing feedback and easy online identity changes. Finally, I show that if the number of buyers is large, the results obtained in the monopoly case are also approximately valid in settings where multiple sellers of different reputations simultaneously offer auctions for identical goods.

Key words: reputation mechanisms; moral hazard; online auctions; eBay

History: Tridas Mukhopadhayay and V. Sambamurthy, Senior Editors; Avi Seidmann, Associate Editor. This paper was with the author 9.6 months for 4 revisions.

## 1. Introduction

Reputation mechanisms are emerging as an important component of electronic markets, helping build trust and elicit cooperation among loosely connected and geographically dispersed economic agents (Resnick et al. 2000, Dellarocas 2003). For example, eBay’s feedback mechanism is the primary means through which eBay elicits honest behavior and thus facilitates transactions among strangers over the Internet (Resnick and Zeckhauser 2002). Several other communities also rely on reputation mechanisms to promote trust and cooperation. Examples include eLance (online community of freelance professionals), Slashdot (online discussion forum where reputation scores help prioritize and filter postings), and Epinions (online consumer report forum where user feedback helps evaluate the quality of product reviews).

The use of reputation as a basis for social control is arguably as old as society itself (Greif 1993, Klein

1997, Milgrom et al. 1990). Nevertheless, the advent of the Internet has added several new dimensions to this age-old concept. Most important among them is the ability to systematically control the type and volume of reputational information exchanged within online communities through the use of properly architected information systems (online reputation mediators). Reputation mediators control who can participate, what type of information is solicited from participants, how it is aggregated, and how it is made publicly available to other community members. They enable community operators to exercise precise control over a number of parameters that are difficult to influence in traditional settings. For example, reputation mediators can replace detailed reputation histories with a wide variety of summary statistics, apply filtering algorithms to eliminate outlier or suspect postings, control the initial state of a new member’s reputation profile, etc. These design choices, in turn, impact the perceptions and, ultimately, the actions of community members toward one another.

The potential to engineer desirable social outcomes through the introduction of carefully crafted information systems is opening a new chapter on the frontiers of information systems research. Further progress in this area requires a deeper understanding of the role of reputation mechanisms in various types of communities, a careful scoping of their design space, and theory-driven guidelines for selecting the most appropriate architecture for a given class of settings.

This paper offers a systematic exploration of reputation mechanism design in trading environments where trust issues are related to moral hazard (for example, bilateral exchange settings where the buyer pays first and the seller is then tempted to cheat). The objective of reputation mechanisms in such settings is to promote cooperative and honest behavior among self-interested economic agents. In contrast, in settings where trust issues are related to adverse selection, the role of reputation mechanisms is to help the community learn the (initially unknown) attributes of community members (such as their ability, honesty, etc.).

A fundamental distinction between the two kinds of settings is that, in the former, all community members are assumed to be equally capable of behaving in “good” and “bad” ways and will act in ways that maximize their individual payoffs, whereas in the latter, community members differ in “type” (e.g., some are intrinsically more capable or honest than others) and behave in ways that are constrained by their (initially privately known) type. In settings of the first kind, reputation mechanisms use the threat of future punishment (e.g., in the form of lower bids following the posting of a negative rating on a trader’s reputation profile) to induce cooperation. In contrast, in settings of the second kind, reputation mechanisms publish information accumulated from past transactions to promote learning. In common with other researchers (Kuwabara 2003), I will use the terms sanctioning and signaling to refer to these two roles of reputation mechanisms.

In many settings, both moral hazard and adverse selection considerations are simultaneously present: Players both behave strategically and differ in their intrinsic ability levels, cost structures, etc. (This makes their relative preferences for good and bad behavior a function of their type.) Reputation mechanisms then play both a sanctioning and a signaling role. Nevertheless, in most practical settings, one of the two roles is usually dominant. For example, Epinions and Amazon Reviews primarily serve a signaling role: They spread information about the (initially privately known, but relatively “fixed”) qualities of the products being reviewed. eBay, on the other hand, is an example of a reputation mechanism that primarily acts as a sanctioning device. eBay users do not rate sellers on the absolute quality of their products, but rather on how well they were able to deliver what was promised on the item description. The role of eBay’s reputation mechanism is to promote honest trade rather than to distinguish sellers who sell high-quality products from those who sell low-quality products.

In this paper, I restrict my attention to the extreme case where only moral hazard considerations are present.<sup>1</sup> I develop a model that aims to capture the essential properties of online auction marketplaces. I then consider a fairly general class of mechanisms and study the impact of various parameters (such as the granularity of solicited feedback, the amount of information published by the mechanism, the policy regarding missing feedback, and the rules for admitting new sellers) on the induced levels of cooperation and payoffs.

Section 2 of the paper introduces the model. Section 3 develops the basic intuitions by considering the simple class of binary mechanisms (mechanisms where buyers can only report the outcome of a transaction as “positive” or “negative”). The analysis derives two important results: First, in environments with imperfect monitoring, the maximum efficiency that is attainable through the use of reputation mechanisms is bounded away from the hypothetical firstbest case where sellers can credibly precommit to full cooperation by a factor that is related to the probability that cooperating sellers may receive “unfair” negative ratings. Second, in direct contrast to signaling reputation mechanisms, the maximum efficiency is independent of the length of past history summarized in a seller’s public reputation profile. The length of history affects the duration of punishment associated with a bad rating, but not the total amount of punishment, or the mechanism’s ability to distinguish a seller’s current action. I show that swifter punishment that lasts for fewer periods is preferable to more lenient punishment that lasts longer because it reduces the minimum stage-game profit margin required for the mechanism to be effective. Therefore, a mechanism that only publishes a player’s single most recent rating minimizes the profit margin requirement without sacrificing efficiency.

I apply the above results to a simplified model of eBay’s feedback mechanism. The principal conclusion is that in settings with pure moral hazard, eBay’s simple mechanism is capable of inducing the maximum efficiency attainable by any binary reputation mechanism independently of the amount of recent activity that is being summarized in the seller’s eBay feedback profile. Moreover, it allows traders to maximize their payoffs by relying on a simple stationary strategy according to which a seller’s expected probability of cooperation is a decreasing linear function of the sum of negative ratings in his current eBay “ID card.”

Section 4 extends the analysis to mechanisms that allow multiple buyer report types (for example, integer ratings between 1 and 5) or arbitrary user comments. I show that maximally efficient mechanisms can be constructed by designating a subset of those report types as “bad” reports and punishing the seller by the same amount whenever he receives any report whose type belongs to the “bad” set. Given a set of “bad” report types, the mechanism’s maximum efficiency is inversely proportional to the likelihood ratio of punishment if the seller cooperates versus if he cheats. Thus, the “bad” report set should be the subset of report types that minimizes the above likelihood ratio.

In settings where feedback submission is voluntary, I find that the optimal policy for dealing with missing feedback is to treat it as positive feedback. Moreover, in online settings where sellers can easily change identities, charging an entrance fee equal to the difference between the payoff of a seller with a clean record and the payoff of a seller with the worst possible reputation profile removes a seller’s temptation to change his identity following the receipt of a bad rating and thus maintains his incentives to cooperate.

Section 5 extends the analysis to settings where n sellers simultaneously offer auctions for units of an identical good to m unit-demand buyers. I show that as the number of buyers grows, the strategies and payoffs induced by a reputation mechanism converge to a strategy and payoff induced by the same mechanism in a monopoly setting with m/n buyers. Thus, all results obtained under the assumption of a monopolist seller are approximately valid in online auction settings where large numbers of buyers select among several simultaneous auctions for the same good by sellers of different reputations. Section 6 contains concluding remarks.

## 2. The Setting

The baseline setting involves a marketplace where, in each period, a monopolist long-run seller provides one unit of a product or a service (“good”) to one of multiple short-run buyers. Following receipt of payment, the seller can exert either high effort (“cooperate”) or low effort (“cheat”). The seller’s action affects the probability distribution of the good’s quality and thus its expected value to a buyer. The buyer privately observes the quality of the good delivered, but not the effort exerted by the seller. Moral hazard is introduced because high effort is costlier to the seller, who can reduce his costs by failing to exert high effort, providing the buyer with a good of lower expected value.

More formally, I analyze a setting with a monopolist seller who each period offers for sale a single unit of a good to m buyers.<sup>2</sup> Buyer i has expected valuation $w _ { i }$ for a good produced by a cooperating seller. The expected valuation of a good produced by a cheating seller is zero for all buyers. Thus, the seller will not attract any buyers unless he can credibly promise to cooperate with positive probability. Buyer lifetime is exactly one period, and in each period the m buyers are drawn from the same probability distribution, thus, buyer valuations are independent and identically distributed within and across periods. There are an infinite number of periods, and the seller has a period discount factor  reflecting the time value of money, or the probability that the game will end after each period. Seller effort costs c if the seller cooperates. The cost of cheating is normalized to zero. The seller’s objective is to maximize the present value of his payoffs over the entire span of the game, while the buyers’ objective is to maximize their short-term (stage-game) payoff.

In each period a mechanism is used to allocate the good among the m buyers by determining the buyer that receives the good and the price she pays to the seller. Without loss of generality, we assume that buyers are indexed according to their valuations $( w _ { 1 } \ge w _ { 2 } \ge \cdots \ge w _ { m } )$ . Furthermore, we assume that a second price Vickrey auction is used to award the good to the highest bidder. The winning bidder pays a price equal to the second-highest bid.

The only Nash equilibrium of the above setting is one where the seller will always cheat. Knowing this, no buyer will post a positive bid and no trade will ever take place. The objective of reputation mechanisms is to induce (at least partial) seller cooperation, and thus to facilitate profitable trade despite the seller’s short-term temptation to cheat.

A reputation mechanism allows each period’s buyer to report the quality of the good she received to the center. I assume that the mechanism allows the current buyer to submit one out of a finite set of possible reports $r \in \{ R _ { i } \mid i = 1 , \ldots , m \}$ , where reports indexed by a higher i indicate higher levels of buyer satisfaction.<sup>3</sup> Buyer reports are connected to seller actions through a conditional probability distribution preport <sub></sub> action that specifies the probability of a given type of report given the seller’s (hidden) action.<sup>4</sup> I assume that the conditional distribution p<sub>·  ·</sub> is exogenously given and depends on the set of

## Table 1 Stage-Game of Repeated Bilateral Exchange Game Studied in This Paper

1. The seller offers a single unit of a good, promising to exert high effort (as there is no demand for low effort).

2. The center publishes the seller’s current reputation profile x.

3. Buyers bid their expected valuations for the good in a second price Vickrey auction; the winning bidder pays the second-highest bid.

4. The seller decides whether to exert high effort at cost c, or low effort at cost 0.

5. The buyer receives the good, experiences its quality, and reports on the quality of the good received to the center. The center updates the reputation profile of the seller accordingly.

reports supported by the mechanism and the properties of the trader population. The center aggregates all past reports and publishes a reputation profile for the seller at the beginning of each period. The reputation profile can be the unabridged history of past reports, any truncation of that history, or any statistic derived from that history. Table 1 summarizes the resulting stage-game.

The above specification implicitly assumes that although buyers might make mistakes, they are not acting strategically: The conditional distribution of ratings given a seller’s action is, thus, independent of the seller’s current profile or the history of play. From a theoretical perspective, this can be weakly justified if we make the assumption that buyers only transact with a given seller once (a reasonable assumption in some large-scale electronic markets). Buyers are then indifferent between truthful reporting and untruthful reporting. Moreover, it is possible to devise a side payment mechanism that provides buyers with strict incentives to participate in the reputation mechanism as well as to rate truthfully (see Kandori and Matsushima 1998, Miller et al. 2002). Such a mechanism can be easily combined with the mechanism I present in this paper.

## 3. Binary Reputation Mechanisms

The basic intuitions of this paper can be derived by considering the class of binary reputation mechanisms, that is, mechanisms where buyers can only report the outcome of a transaction as “positive” (satisfactory) or “negative” (unsatisfactory). A binary reputation mechanism is characterized by its associated information structure preport action. I assume that both types of reports can occur with positive probability following both seller actions.<sup>5</sup> Specifically, I assume the following information structure:

$$
\begin{array}{c c} p (+ \mid c o o p) = 1 - \alpha , & p (- \mid c o o p) = \alpha , \\ p (+ \mid c h e a t) = 1 - \beta , & p (- \mid c h e a t) = \beta , \\ & 0 <   \alpha <   \beta <   1, \end{array}\tag{1}
$$

where <sub>+</sub>, <sub>−</sub> indicate a positive and negative report, respectively.

## 3.1. Upper Bounds on Mechanism Efficiency

Given the above information structure, the reputation mechanism designer’s problem focuses on deciding how to aggregate and publish buyer reports to maximize social welfare. The theory of repeated games provides powerful frameworks for answering such questions.

Let $s ( h , x ) \in [ 0 , 1 ]$ denote the seller’s strategy, equal to the probability that the seller will cooperate $( \mathrm { i . e . , }$ exert high effort) following receipt of payment if the private history of ${ \mathrm { p l a y } } ^ { 6 }$ is h and his public reputation profile at the beginning of the current period is equal to x. To simplify the analysis, I initially restrict seller strategies to public strategies, i.e., strategies $s ( x ) \in [ 0 , 1 ]$ that only depend on public information. I subsequently show that the seller can do no better by considering more complex strategies that are also conditioned on his private information.

Given their beliefs about the seller’s strategy sx, short-term buyers simply play the corresponding stage-game static best response. Because they compete with each other on a Vickrey auction, each buyer’s optimal action in each period is to bid an amount equal to her expected valuation $G _ { i } ( x ) = s ( x ) w _ { i }$ , resulting in expected auction revenue for that period $G ( x ) = s ( x ) \widehat { w } _ { 2 } ,$ , where $\widehat { w } _ { 2 }$ is the expected value of the second-highest bidder’s valuation of a cooperating seller’s output. The seller’s corresponding expected current period payoff is $h _ { s } ( x ) = G ( x ) ~ -$ $\begin{array} { r } { s ( x ) c = s ( x ) ( \widehat { w } _ { 2 } - c ) } \end{array}$ . The ex ante expected surplus for the winning bidder is $h _ { b } ( x ) = s ( x ) ( \widehat { w } _ { 1 } - \widehat { w } _ { 2 } )$ , where $\widehat { w } _ { 1 }$ is the expected value of the highest-bidder’s valuation of a cooperating seller’s output. Finally, the expected total surplus generated in the current period is equal to $h ( s ) = h _ { b } ( x ) + h _ { s } ( x ) = s ( x ) ( \widehat { w } _ { 1 } - c )$

If $\widehat { w } _ { 2 } > c ,$ , both seller profits and buyer surplus are proportional to sx: Higher levels of seller cooperation benefit all players. Therefore, an equilibrium strategy that maximizes the seller’s payoff also maximizes buyer surplus. In the rest of the paper, I can therefore focus without loss of generality on finding reputation mechanism designs that maximize the seller’s lifetime discounted payoff. For the same reason, I will be using the terms “seller payoffs” and “efficiency” interchangeably.

Each period the seller decides his level of effort after he receives payment. His decision problem is to select a strategy sx that maximizes the present value of his remaining discounted payoff. The seller’s remaining payoff at the time of effort selection is equal to

$$
U _ {c o o p} (x) = - c + \delta [ (1 - \alpha) V (x ^ {+} (x)) + \alpha V (x ^ {-} (x)) ]\tag{2}
$$

if the seller cooperates,

$$
U _ {c h e a t} (x) = \delta [ (1 - \beta) V (x ^ {+} (x)) + \beta V (x ^ {-} (x)) ]\tag{3}
$$

if the seller cheats, and

$$
U (x) = s (x) U _ {c o o p} (x) + [ 1 - s (x) ] U _ {c h e a t} (x)\tag{4}
$$

if he follows a mixed strategy. In the above equations $x ^ { + } ( x ) , x ^ { - } ( x )$ denote the seller’s new reputation profile following the receipt of a positive and negative rating, respectively, while $V ( x ) = G ( x ) + U ( x )$ denotes the seller’s expected future payoff at the beginning of a period where the seller’s profile is equal to x.

A strategy sx is an equilibrium strategy if and only if it satisfies the following incentive compatibility constraints for all $x ,$ given correct buyer beliefs:

$$
\begin{array}{r l} {s (x) = 0} & {\Rightarrow U _ {c o o p} (x) \leq U _ {c h e a t} (x),} \\ {0 <   s (x) <   1} & {\Rightarrow U _ {c o o p} (x) = U _ {c h e a t} (x),} \\ {s (x) = 1} & {\Rightarrow U _ {c o o p} (x) \geq U _ {c h e a t} (x).} \end{array}\tag{5}
$$

The form of the resulting equilibria depends on the format of the public reputation profile x and the transition functions $x ^ { + } ( x ) , x ^ { - } ( x )$ . The most general case is one where the reputation mechanism makes the entire past history of buyer reports publicly available to future buyers. A seller’s reputation profile x is then an ordered set of positive and negative reports, $x ^ { + } ( x ) =$ $( x , + )$ and $x ^ { - } ( x ) = ( x , - )$ . All equilibria of reputation mechanisms that publish truncations or statistics of the history of buyer reports are also equilibria of this more general setting (because, given the entire history, players can construct these truncations or statistics and condition their play on them). Our first result establishes upper bounds on the seller payoffs that are achievable in such a setting.

Proposition 1. Let $\rho = \widehat { w } _ { 2 } / c ; \rho$ is a measure of the expected stage-game profit margin of a fully cooperating seller.

1. The set of perfect public equilibrium payoffs<sup>7</sup> of a repeated game where the stage-game structure is described in Table 1, the reputation mechanism has information structure (1), and the entire history of past reports is available to buyers, is bounded above by

$$
\begin{array}{r l} & V ^ {*} = 0 \qquad i f \rho <   [ \beta + (1 - \delta) / \delta ] / (\beta - \alpha), \\ & V ^ {*} = \frac {1}{1 - \delta} \bigg (\widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha} \bigg) \\ & \qquad i f \rho \geq [ \beta + (1 - \delta) / \delta) / (\beta - \alpha). \end{array}
$$

2. The above bounds remain unchanged if the seller is allowed to condition his actions on both public information and private information not available to buyers $( e . g .$ , his past actions, past bid amounts, etc.) and the full set of sequential equilibria of the repeated game is considered.

Note that the maximum attainable payoff is strictly bounded away from the first-best payoff $V _ { f i r s t - b e s t } =$ $( \widehat { w } _ { 2 } - c ) / ( 1 - \delta )$ that would have been attainable in settings where sellers could credibly precommit to full cooperation. The following sections discuss two concrete implementations that achieve maximum efficiency and clarify the intuitions behind this result.

## 3.2. Efficient Implementation Using a Randomization Device

A simple way to implement an equilibrium that attains payoffs equal to the upper bound of Proposition 1 is through the use of a two-state randomization device.<sup>8</sup> The idea is that a seller’s public reputation profile can be in one of two states: a “good” state and a “bad” state. New sellers always start from the good state. Whenever a seller receives a positive rating, the center keeps his profile in the good state. Whenever he receives a negative rating, however, the center changes the seller’s profile to “bad” with probability $\pi .$ The following theorem shows that if $\rho$ is high enough,  can be chosen to construct an equilibrium where (i) the seller always cooperates as long as his profile is good, (ii) the seller always cheats (effectively placing himself out of the market) when his profile turns bad, and (iii) the seller’s lifetime discounted payoff is equal to the maximum achievable payoff V ∗ predicted by Proposition 1.

Proposition 2. 1. $I f \rho \ge ( \beta + ( 1 - \delta ) / \delta ) / ( \beta - \alpha )$ , then a randomization device with $\pi = ( 1 - \delta ) / \delta [ \rho ( \beta - \alpha ) - \beta ]$ induces the seller to cooperate as long as he remains in the “good” state. The present value of the seller’s discounted lifetime payoff in the “good” state is equal to

$$
V _ {g o o d} = V ^ {*} = \frac {1}{1 - \delta} \left(\widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha}\right).
$$

2. $I f \rho < ( \beta + ( 1 - \delta ) / \delta ) / ( \beta - \alpha )$ , then no randomization device can provide sufficient incentives for cooperation. The only equilibrium is one where the seller always cheats, no buyers submit bids, and $V _ { g o o d } = 0$

The above construction helps provide an intuitive understanding of the situation. Reputation mechanisms induce current cooperation using the threat of future punishment following bad news about the seller’s current behavior. In our setting, punishment is equal to the opportunity cost of foregone future profits when a seller’s profile turns bad (the seller then effectively gets expelled from the market). The probability of a profile state transition is proportional to times the probability of a negative rating. The latter is higher by   when the seller cheats. If  is set high enough so that the present value of the incremental opportunity cost associated with cheating exceeds the corresponding present gains $c ,$ rational sellers will find it preferable to cooperate. Thus, there is a threshold value $\pi _ { 0 }$ such that if we set $\pi \geq \pi _ { 0 } ,$ the seller will be induced to cooperate. Unfortunately, in the presence of imperfect monitoring, even cooperating sellers will eventually accumulate negative ratings and will transition to the bad state with positive probability . This property results in efficiency losses relative to the first-best case.<sup>9</sup> Lower values of  result in lower probabilities of “unfair” state transitions and, thus, in higher efficiency. To maximize efficiency, the mechanism designer’s objective should be to set equal to the minimum value that induces cooperation. This minimum value is just high enough to make the seller indifferent between cooperation and cheating. The resulting maximum efficiency is equal to the first-best payoff $V _ { f i r s t - b e s t } = ( \widehat { w } _ { 2 } - c ) / ( 1 - \delta )$ attainable in (hypothetical) settings where sellers can credibly precommit to full cooperation, minus a penalty term $\alpha c / ( 1 - \delta ) ( \beta - \alpha )$ associated with the mechanism’s less than perfect ability to distinguish the seller’s actions.

Because the mechanism does not punish sellers by levying actual penalties, but simply by triggering their exclusion from the market, the condition $\rho \ge ( \beta + ( 1 - \delta ) \delta ) / ( \beta - \alpha )$ expresses the fact that for the mechanism to provide sufficient incentives for cooperation, the stage-game profit margin of a cooperating seller must be high enough so that the present value of incremental future profits from cooperation (that the seller jeopardizes by cheating) is higher than the current gains from cheating. This condition limits the applicability of reputation mechanisms to settings where trusted sellers enjoy sufficiently high premiums (Klein and Leffler 1981, Shapiro 1983).

## 3.3. Efficient Implementation Using Summary Statistics

The use of a two-state randomization device has the undesirable property that cooperating sellers will eventually be expelled from the market with positive probability. Electronic markets might prefer to induce cooperation using measures of a less draconian nature. This section analyzes a reputation mechanism that publishes summary statistics of a seller’s recent ratings. This mechanism has practical interest because it resembles important aspects of the feedback mechanism used by eBay. I show that in settings with pure moral hazard, this mechanism can attain the theoretically maximum efficiency of Proposition 1 and has the desirable property that it allows sellers to remain on the market indefinitely. A striking corollary of my analysis is that maximum efficiency is independent of the amount of seller activity summarized in the seller’s public reputation profile. In fact, it turns out that summarizing fewer ratings broadens the range of settings where the mechanism can induce cooperation (because it places less-stringent minimum stage-game profit margin requirements). This result is in direct contrast to equivalent results associated with mechanisms whose primary objective is learning,<sup>10</sup> and shows that the optimal architectures of the two classes of mechanisms can be very different.

Our mechanism hides the seller’s detailed rating history from buyers; instead, at the beginning of each period it publishes the sum of positive and negative ratings posted for the seller in the most recent N transactions. N is a mechanism parameter chosen by the designer. A seller’s public reputation profile can then be modeled as a pair $p = ( z , N )$ , where N is the width of the time window and z is the sum of negative ratings accumulated in the most recent N transactions. If we ignore neutral ratings and interpret N as an estimate of the number of transactions performed by a seller during a six-month period, the above mechanism can be thought of as an abstract model of eBay’s “ID Card,” which summarizes ratings posted on a seller during the most recent six-month period.

If N remains constant for the duration of the game, a seller’s public reputation profile is completely characterized by the number of negative ratings z in the current “time window.” On the other hand, a seller’s private reputation profile (known to the center and the seller) is equal to an ordered list of length N , consisting of the N most recent positive and negative ratings in chronological order (earlier ratings first). If we assign the digit 1 to a positive rating and 0 to a negative rating, each of the $\bar { \boldsymbol { 2 } ^ { N } }$ possible private profiles can be mapped to an N -digit binary number x between 0 and $2 ^ { \bar { N } ^ { - } - 1 }$ (for example, if $N = 3 ,$ , then the profile $( + , - , + )$ maps to $x = 1 0 1 = 5 )$ . In the rest of the section, we will refer to x as the algebraic representation of the seller’s private reputation profile.

At the end of each period, the center deletes the first (earliest) rating from the seller’s private profile and appends the most recent rating at the end of the profile. Algebraically, this operation is equivalent to: (i) taking the $N - 1$ rightmost bits of the binary representation of the original x (they are equal to the remainder of the division of x by $\overset { \cdot } { 2 } ^ { N - 1 } ) .$ , (ii) multiplying them by 2 (this appends a zero at the end), and (iii) adding 1 if the most recent rating was positive (this changes the tail zero to one). The private profile transition functions can thus be written as

$$
x ^ {-} (x) = 2 (x \oplus 2 ^ {N - 1}), \qquad x ^ {+} (x) = 2 (x \oplus 2 ^ {N - 1}) + 1,
$$

where denotes the modulo (division remainder) operator. I will show that if the profit margin of a fully cooperating seller is sufficiently high, the above mechanism induces a perfect public equilibrium that attains the maximum efficiency predicted by Proposition 1.

Let us assume that the seller follows a public strat-$\mathrm { e g y } \ s = \{ s ( z ) \mid z = 0 , \ldots , N \}$ that only depends on the current number of negative ratings on his profile. His maximization problem then becomes

$$
V (x) = \max _ {s (z (x))} \left\{ \begin{array}{l l} s (z (x)) \widehat {w} _ {2} - c + \delta [ (1 - \alpha) V (2 (x \oplus 2 ^ {N - 1}) + 1) \\ \quad + \alpha V (2 (x \oplus 2 ^ {N - 1})) ] & \text { if } s (z (x)) > 0, \\ s (z (x)) \widehat {w} _ {2} + \delta [ (1 - \beta) V (2 (x \oplus 2 ^ {N - 1}) + 1) \\ \quad + \beta V (2 (x \oplus 2 ^ {N - 1})) ] & \text { if } s (z (x)) <   1, \end{array} \right.\tag{6}
$$

subject to the incentive compatibility constraints

$$
\begin{array}{l} s (z (x)) = 0 \\ \Rightarrow V (2 (x \oplus 2 ^ {N - 1}) + 1) - V (2 (x \oplus 2 ^ {N - 1})) \leq c / \delta (\beta - \alpha), \\ 0 <   s (z (x)) <   1 \\ \Rightarrow V (2 (x \oplus 2 ^ {N - 1}) + 1) - V (2 (x \oplus 2 ^ {N - 1})) = c / \delta (\beta - \alpha), \\ s (z (x)) = 1 \\ \Rightarrow V (2 (x \oplus 2 ^ {N - 1}) + 1) - V (2 (x \oplus 2 ^ {N - 1})) \geq c / \delta (\beta - \alpha), \end{array} \tag {7}\tag{7}
$$

for all $0 \leq x \leq 2 ^ { N } - 1$ . The following proposition holds:

Proposition 3. Consider a repeated game with the stage-game structure described in Table 1 and an eBaylike reputation mechanism with information structure (1). Each period, the mechanism publishes the sum of negative ratings received by the seller during the most recent N transactions.

1. If

$$
\rho = \frac {\widehat {w} _ {2}}{c} \geq \frac {N}{(\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i}},
$$

then there exists a perfect public equilibrium where

(a) The seller’s probability of cooperation is a decreasing linear function of the current number z of negative ratings in his profile

$$
s (z) = 1 - z \theta , \quad w h e r e \theta = \frac {c}{\widehat {w} _ {2} (\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i}},
$$

(b) The present value of the seller’s discounted lifetime payoff is maximized during periods when the seller has zero negative ratings in his profile; it is then equal to the maximum payoff

$$
V ^ {*} = \frac {1}{1 - \delta} \bigg (\widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha} \bigg)
$$

attainable by any reputation mechanism with information structure (1),

(c) The maximum attainable payoff is independent of the number N of transactions summarized in the seller’s public profile.

2. If

$$
\rho <   \frac {N}{(\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i}},
$$

then all PPE achieve seller payoffs strictly below $V ^ { * }$

Proposition 3 states that if  is large enough, eBay-like reputation mechanisms induce an equilibrium where buyers (correctly) expect the seller to cooperate fully as long as he has no negative ratings in his profile, and otherwise to follow a mixed strategy where the probability of cooperation is a decreasing linear function of the number of negative ratings in his profile. If sellers start the game with a “clean record” (zero negative ratings), this equilibrium achieves the maximum efficiency attainable by any reputation mechanism with information structure (1).

The main predictions of Proposition 3 are consistent with empirical evidence. Proposition 3 predicts that receipt of a negative rating induces the seller to reduce his average cooperation levels during the following N periods. This prediction has two empirically testable consequences: First, expecting lower average cooperation, buyers should post lower bids for sellers with more negative ratings in their profile. The majority of empirical studies on eBay have reported the presence of such a relationship.<sup>11</sup> Second, once a seller receives a negative rating, the rate of arrival of subsequent negative ratings should increase (if the seller reduces his effort following receipt of a negative rating, this increases the probability of another negative outcome). Cabral and Hortacsu (2004) have empirically verified the presence of this remarkable phenomenon on eBay.

In common with the two-state randomization device of §3.2, eBay-like reputation mechanisms elicit cooperation through the threat of punishment following a negative rating. Upon receipt of a negative rating, the randomization device either delivers “lethal” punishment (expulsion of the seller from the marketplace) or forgives the seller; eBay-like mechanisms, on the other hand, deliver a less-severe, per-period punishment that lasts for a finite number of periods. Every time the seller receives a negative rating, the anticipated probability of seller cooperation is reduced by an amount % for the N following cycles (the length of time it takes for the negative rating to propagate to the other end of the time window and be erased from the seller’s public profile). Given their anticipation, buyers lower their bids by $\theta w _ { i }$ during the following N -cycle period, reducing the present value of the seller’s expected revenues by $\begin{array} { r } { \sum _ { i = 1 } ^ { N } \delta ^ { i } \theta \widehat { w } _ { 2 } } \end{array}$

To induce cooperation, the opportunity cost of cheating must be greater than or equal to the gains from cheating. The opportunity cost of cheating is equal to the incremental probability of a negative rating induced by cheating behavior $( \beta - \alpha )$ , times the present value of lost profits $\sum _ { i = 1 } ^ { N } \delta ^ { i } \theta \widehat { w } _ { 2 }$ following a negative rating. The gains from cheating, on the other hand, are equal to c. To minimize efficiency losses due to negative ratings “unfairly” posted for cooperating sellers, the opportunity cost of a negative rating must be as low as possible. Maximum efficiency is attained when the opportunity cost of cheating is exactly equal to the present value of the gains from cheating. This happens when $\begin{array} { r } { \theta = c / \widehat { w } _ { 2 } ( \beta - \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i } } \end{array}$

Proposition 3 shows that eBay-like feedback mechanisms allow traders to maximize their payoffs by relying on simple stationary strategies of intuitive appeal; players need not even consider more complex strategies (or the possibility that other players may use such strategies). A further strength of the results is that they are robust to errors individual buyers may make in the calculation of sz as long as these errors are not systematic (i.e., as long as they are completely random with an expected value of zero).<sup>12</sup> These properties make eBay’s mechanism especially well suited to large-scale online-trading environments, as it allows even inexperienced traders to perform well by relying on simple, intuitive strategies.

An interesting corollary of Proposition 3 is that the maximum efficiency attainable by an eBay-like mechanism is independent of the number of ratings N that are included in the published summary statistic. This means that a mechanism that each period publishes only the outcome of a seller’s single most recent transaction N <sub>=</sub> 1 is capable of inducing the same average levels of cooperation and total surplus as more sophisticated mechanisms that summarize arbitrarily large numbers of recent transactions.

At first this result might seem counterintuitive. Common wisdom in decision theory suggests that more information leads to better outcomes (Blackwell 1951, 1953). The key to understanding the result lies in the distinction between the signaling and sanctioning roles of reputation mechanisms. Reputation mechanisms whose primary objective is signaling (such as Epinions and Amazon Reviews) improve market efficiency by enabling better consumer inferences based on past information about initially unknown but “fixed” product attributes. The efficiency of such mechanisms is related to the quality of the accumulated information à la Blackwell. Therefore, the larger the number of published reports, the better the outcomes. Sanctioning mechanisms, on the other hand, improve market efficiency by inducing higher cooperation levels through the threat of future punishment associated with spreading information about the outcome of the current transaction. Therefore, the efficiency of a sanctioning mechanism is related to the incremental present value of punishment associated with a “bad” action in the current transaction. In our setting, this value is independent of N and equal to the stage-game gains from cheating. The parameter N simply determines the number of “installments” during which the total punishment will be “paid.”<sup>13</sup> For that reason, mechanism efficiency is independent of the number of ratings N summarized in the seller’s public reputation profile.

A more subtle corollary of Proposition 3 is that, as N grows, the minimum stage-game cooperative profit margin $\rho = \widehat { w } _ { 2 } / c \geq N / ( \beta - \alpha ) \overline { { \sum _ { i = 1 } ^ { N } \delta ^ { i } } }$ that is required for the mechanism to attain maximum efficiency outcomes also grows.<sup>14</sup> To see why, observe that for the mechanism to attain maximum efficiency, it must be able to make sellers indifferent between cooperation and cheating even during periods when they are paying “punishment installments” for past negative ratings. During those periods, sellers are expected to cooperate with probability $1 - z \theta _ { \scriptscriptstyle \perp }$ , where z is the number of past negative ratings in their profile. Sellers will only be deterred from further cheating if it is possible to threaten them with a further drop in their expected probability of cooperation if they get another negative rating. However, this can only happen if $1 - ( z + 1 ) \theta \ge 0$ , that is, if it is possible to further reduce their expected probability of cooperation by % and still be left with a nonnegative number.<sup>15</sup>

The worst-case scenario arises in periods where the seller is “paying” for N past negative ratings (i.e., all N ratings in his public profile are negative). To deter a seller from cheating in such periods, it must be $1 - N \theta \geq 0$ (in the next cycle, one negative rating will disappear from the profile; if the seller receives a new negative, he will be left with N negatives once again) or, equivalently, $N \theta \widehat { w } _ { 2 } \leq \widehat { w } _ { 2 } ;$ The sum of the nominal values of all N punishment installments associated with a bad rating must be less than or equal to a fully cooperating seller’s expected auction revenue. Making an analogy with loans, recall that, given a fixed loan present value, the larger the number of payment installments N , the larger the sum of the nominal values of all installments (due to the impact of interest rates). Similarly, in our setting, given a fixed present value of punishment $c / ( \beta - \alpha )$ , the sum of the nominal values of punishment installments $N \theta \widehat { w } _ { 2 }$ increases with N . This means that for given $\alpha , \beta , c ,$ the higher the N , the higher the minimum $\widehat { w } _ { 2 }$ that satisfies the constraint $N \theta \widehat { w } _ { 2 } \leq \widehat { w } _ { 2 }$ . This, in turn, implies that as N grows, the minimum profit margin $\rho = \widehat { w } _ { 2 } / c$ that is needed for the reputation mechanism to induce maximum efficiency must also grow, making the mechanism applicable to fewer settings.

The conclusion of the above discussion is that the optimal design of sanctioning reputation mechanisms follows different principles to that of signaling reputation mechanisms. The length of time during which a rating persists in the seller’s reputation profile only affects the duration of punishment, and not the ability of the mechanism to distinguish between good and bad seller actions. Swifter punishment that lasts for fewer periods is preferable to more lenient punishment that lasts longer, because it reduces the minimum required profit margins. The analysis thus provides arguments for simpler mechanisms that publish only a seller’s very recent ratings.

## 3.4. Implications of Costless Identity Changes

In most online communities it is relatively easy for members to disappear from the community and reregister under a different online identity. Friedman and Resnick (2001) refer to this property as “cheap pseudonyms.” This property challenges the effectiveness of reputation mechanisms: Online community members can build a reputation, milk it by cheating other members, then disappear and reenter the community with a new identity and a clean record. I focus my attention on the extreme case where identity changes are cost free. The following results extend readily to settings where identity changes involve a small positive cost.

In our setting, the ability to costlessly change a player’s identity has a simple but disruptive effect: Rational sellers will disappear and reenter the community with a new identity whenever their reputation profile transitions to a state whose lifetime discounted payoff is lower than the payoff of the initial state of a new seller. This has particularly severe consequences in the case of the two-state randomization device (§3.2). If sellers can costlessly change their identity and reenter the market as soon as their profile transitions into the “bad” state, they have no incentive to avoid negative ratings. Therefore, sellers will always cheat, buyers will expect them to do so, and no trade will ever take place irrespective of the value of $\rho .$ Costless identity changes thus completely destroy the effectiveness of a two-state randomization device.

The only way to prevent sellers from changing their identities is to perturb the mechanism so that new sellers start the game from a state that has the lowest possible payoff among all states. Such a perturbation is not possible in the case of the two-state randomization device, because the state with the lowest payoff (the “bad” state) effectively excludes the seller from future participation in the market. In contrast, if $\rho$ is sufficiently high so that all states have positive payoffs, eBay-like mechanisms can be made robust to identity changes by charging sellers an entrance fee that makes a newcomer’s expected discounted lifetime payoff equal to the payoff of a seller with the “worst” possible reputation profile (i.e., a profile where all N recent ratings are negative). The following proposition provides the details.

Proposition 4. If

$$
\rho = \frac {\widehat {w} _ {2}}{c} > \frac {N}{(\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i}},
$$

then

1. An eBay-like reputation mechanism with information structure (1) can be made robust to costless identity changes by charging sellers an entrance fee equal to

$$
\left(\frac {N}{\delta (1 - \delta^ {N})} - \frac {1}{1 - \delta}\right) \frac {c}{\beta - \alpha}.
$$

This makes a new seller’s expected discounted lifetime payoff equal to the payoff of a seller whose reputation profile

has N negative ratings:

$$
\begin{array}{c} V _ {f r e e - i d s} (N) = \frac {1}{1 - \delta} \bigg (w - c - \frac {\alpha c}{\beta - \alpha} \bigg) \\ - \bigg (\frac {N}{\delta (1 - \delta^ {N})} - \frac {1}{1 - \delta} \bigg) \frac {c}{\beta - \alpha}. \end{array}
$$

2. New seller payoffs are inversely proportional to the number of ratings N summarized in the mechanism’s public reputation profile; they attain their maximum value for $N = 1$

$$
V _ {f r e e - i d s} (1) = \frac {1}{1 - \delta} \left(w _ {2} - c - \frac {\alpha c}{\beta - \alpha}\right) - \frac {c}{\delta (\beta - \alpha)}.
$$

Proposition 4 has a number of interesting implications. First, it establishes that costless identity changes impose an efficiency loss because new sellers have to “pay their dues” to be trusted to not disappear following the receipt of a bad rating.<sup>16</sup> Second, it shows that this efficiency loss grows with the number of ratings N summarized by the mechanism. The loss is minimized in the simplest case, where each period the mechanism publishes the rating of the immediately preceding transaction only $( N = 1 )$ . This result is remarkable. In §3.3, I have shown that the maximum efficiency of an eBay-like reputation mechanism is independent of the number of summarized ratings, and that, in fact, summarizing fewer ratings reduces the minimum stage-game profit margin that is required for the mechanism to achieve maximum efficiency. Proposition 4 strengthens this “simpleris-better” result even more: In environments where players can costlessly change their identities, reputation mechanisms that summarize fewer ratings induce strictly more efficient outcomes than mechanisms that summarize larger numbers of ratings.

I conclude this section by showing that in the presence of free identity changes, no reputation mechanism with information structure (1) can attain higher seller payoffs than an eBay-like mechanism with an entrance fee equal to $c / \delta ( \beta - \alpha )$ and $N = 1$ . Efficiency losses associated with easy name changes are thus inevitable, and a two-state, eBay-like reputation mechanism with an entrance fee constitutes the best possible solution.

Proposition 5. If $\rho > ( \beta + ( 1 - \delta ) / \delta ) / ( \beta - \alpha )$ and players can costlessly change identities, the set of sequential equilibrium seller payoffs of a repeated game where the stage-game structure is described in Table 1, the reputation mechanism has information structure (1), and the entire public history of buyer reports is available to short-run players is bounded above by

$$
V _ {f r e e - i d s} ^ {*} = \frac {1}{1 - \delta} \bigg (w _ {2} - c - \frac {\alpha c}{\beta - \alpha} \bigg) - \frac {c}{\delta (\beta - \alpha)}.
$$

## 4. Multivalued Reputation Mechanisms

This section extends the analysis to the general case where the mechanism supports arbitrary finite sets of report types. I also show how, in settings where feedback submission is voluntary, the optimal policy for treating missing feedback can be derived as a special case of the general problem of multivalued reputation mechanism design.

## 4.1. Upper Bounds on Mechanism Efficiency

The study of binary reputation mechanisms provided valuable intuitions that can help inform the analysis of the multivalued case. Recall that the power of a binary reputation mechanism relies on the presence of a $\mathrm { \dot { \Omega } } ^ { \prime \prime } { \mathrm { b a d } } ^ { \prime \prime }$ report type whose conditional probability of incidence is higher when the seller cheats  than when the seller cooperates . The mechanism punishes the seller every time a “bad” report is submitted by triggering a reduction of his expected future profits by a present amount $p .$ If the incremental probability of a “bad” report when the seller cheats $( \beta - \alpha )$ , times the present value of punishment $p$ is greater than or equal to the current gains from cheating c, then a rational seller will prefer to cooperate. The minimum present value of punishment that induces cooperation is equal to $p = c / ( \beta - \alpha )$ . Because reputation mechanisms do not levy explicit penalties, but simply trigger reductions of future profits, punishment cannot exceed the present value of profits from cooperation. This requires that the incremental probability of a “bad” report $( \beta - \alpha )$ be high enough to ensure that the minimum effective punishment is lower than the present value of profits from cooperation. The efficiency losses of the reputation mechanism relative to the first-best case are due to the less than perfect ability of the mechanism to determine a seller’s true action: Even cooperating sellers will occasionally receive bad reports and will thus be “unfairly” punished. The average per-period efficiency loss is equal to the conditional probability of a bad report if the seller cooperates  times the present value of punishment $c / ( \beta - \alpha )$ . For a fixed $^ { c , }$ this efficiency loss is proportional to the incremental probability of a bad report if the seller cheats, and inversely proportional to the probability of a bad report if the seller cooperates.

The same logic applies when the mechanism supports multiple report types or allows buyers to submit text comments.<sup>17</sup> The objective of the mechanism still is to deter the seller from choosing the “bad” action. Any report type, or subset of report types, whose cumulative conditional probability of incidence is higher when the seller cheats can be used as the mechanism’s “bad” report set B. The mechanism punishes the seller every time he receives a report that belongs to the “bad” set by an amount equal to the current gains from cheating over the incremental probability of incidence of a bad report if the seller cheats. To minimize efficiency losses, the “bad” report set must consist of report types whose cumulative conditional probability of incidence if the seller cooperates is as small as possible, and whose incremental probability of incidence if the seller cheats is as high as possible. The following proposition formalizes this intuition.

Proposition 6. The set of sequential equilibrium payoffs of a repeated game, where the stage-game structure is described in Table 1, the reputation mechanism supports a report set $R = \{ R _ { i } | i = 1 , \ldots , m \}$ with associated information structure $p ( R _ { i } \mid c o o p ) = \alpha _ { i } , p ( R _ { i } \mid c h e a t ) = \beta _ { i }$ , and the entire public history of buyer reports is available to shortrun players, is bounded above by

$$
V ^ {*} = \frac {1}{1 - \delta} \bigg (\widehat {w} _ {2} - c - \frac {a (B) c}{b (B) - a (B)} \bigg),
$$

where $\begin{array} { r } { a ( B ) = \sum _ { R _ { i } \in B } \alpha _ { i } , b ( B ) = \sum _ { R _ { i } \in B } \beta _ { i } . } \end{array}$ , and $B \subset R$ is the solution of the following constrained optimization problem:

$$
B = \underset {S \subset R, a (S) <   b (S)} {\arg \min} \frac {a (S)}{b (S)}\tag{8}
$$

$$
\text { subject   to } \quad \rho \geq \frac {b (B) + (1 - \delta) / \delta}{b (B) - a (B)}.
$$

If the above problem has no solution, then $V ^ { * } = 0$

According to Proposition $^ { 6 , }$ the $\boldsymbol { \omega } _ { \mathrm { b a d } ^ { \prime \prime } }$ report set B that maximizes efficiency is the subset of supported reports that minimizes the likelihood ratio of punishment $p ( R _ { i } \in { \cal B } \mid c o o p ) / p ( R _ { i } \in { \cal B } \mid$ cheat, while keeping the incremental probability of punishment $p ( R _ { i } \in \boldsymbol { B } \mid c h e a t ) - p ( R _ { i } \in \boldsymbol { B } \mid c o o p )$ high enough to ensure that the minimum present value of punishment that deters cheating is lower than the present value of future gains from cooperation.

Proposition 6 has a remarkable implication. It states that even if we allow buyers to use multiple types of ratings (for example, integer ratings between 1 and 5), or even to supply text comments to express their degree of satisfaction with a transaction, the most efficient way to interpret buyer reports is to classify them into exactly two categories (good/bad) and to treat report types within each category as equivalent (for example, interpret any rating equal to or less than 2 as bad and any rating higher than 2 as good, without attempting to make any further distinctions). Proposition 6 implies that this coarse-grained rule induces average levels of cooperation that are at least as high as those induced by more sophisticated rules that make finer distinctions among report types.<sup>18</sup>

The above analysis provides a basis for comparing the maximum efficiency of two reputation mechanisms that support different report sets. Specifically, the following corollary is an immediate consequence of Proposition 6:

Corollary 1. A reputation mechanism that supports a report set $R = \{ R _ { i } | i = 1 , \ldots , m \}$ with associated information structure $p ( R _ { i } \mid c o o p ) = \alpha _ { i } , p ( R _ { i } \mid c h e a t ) = \beta _ { i }$ induces higher maximum efficiency than a mechanism that supports a report set $R ^ { \prime } = \{ R _ { i } ^ { \prime } | i = 1 , \ldots , m ^ { \prime } \}$ with associated information structure $p ( R _ { i } ^ { \prime } \mid c o o p ) = \alpha _ { i } ^ { \prime } , p ( R _ { i } ^ { \prime } \mid c h e a t ) = \beta _ { i } ^ { \prime } ,$ if and only if

$$
\frac {a (B)}{b (B)} <   \frac {a ^ {\prime} (B ^ {\prime})}{b ^ {\prime} (B ^ {\prime})},
$$

where $\begin{array} { r } { a ( B ) \ = \ \sum _ { R _ { i } \in B } \alpha _ { i } , b ( B ) \ = \ \sum _ { R _ { i } \in B } \beta _ { i } , a ^ { \prime } ( B ^ { \prime } ) \ = \ } \end{array}$ $\begin{array} { r } { \sum _ { R _ { i } ^ { \prime } \in B ^ { \prime } } \alpha _ { i } ^ { \prime } , b ^ { \prime } ( B ^ { \prime } ) = \sum _ { R _ { i } ^ { \prime } \in B ^ { \prime } } \beta _ { i } ^ { \prime } , } \end{array}$ and $B \subset R , B ^ { \prime } \subset R ^ { \prime }$ solve

$$
\begin{array}{l l} B = \underset {S \subset R} {\arg \min} \frac {a (S)}{b (S)} & s. t. \rho \geq \frac {b (B) + (1 - \delta) / \delta}{b (B) - a (B)}, \\ B ^ {\prime} = \underset {S ^ {\prime} \subset R ^ {\prime}} {\arg \min} \frac {a (S ^ {\prime})}{b (S ^ {\prime})} & s. t. \rho \geq \frac {b ^ {\prime} (B ^ {\prime}) + (1 - \delta) / \delta}{b ^ {\prime} (B ^ {\prime}) - a ^ {\prime} (B ^ {\prime})}. \end{array}\tag{9}
$$

Corollary 1 provides a useful condition that can be used to determine whether, say, the multivalued reputation mechanism used by Amazon auctions induces higher cooperation levels than the binary mechanism used by eBay. Observe that the efficiency of a sanctioning reputation mechanism does not depend on the number of supported report types, but rather on its associated minimum likelihood ratio of punishment. It is, therefore, not always the case that replacing a coarse-grained report set with a finer-grained one will increase efficiency.

## 4.2. Application to the Study of Incomplete Feedback Submission

Most reputation mechanisms rely on voluntary feedback submission from users. Because this incurs a cost associated with accessing a website and filling the necessary feedback forms, in the absence of concrete incentives a fraction of users might submit no report to the system.<sup>19</sup> This section applies the results of the previous section to the study of equilibria induced by binary reputation mechanisms in the presence of incomplete reporting.

The key idea is that failure to provide feedback can be considered as a special type of buyer report. A binary reputation mechanism with incomplete feedback reporting can then be modeled as a reputation mechanism that supports a 3-valued report set $R = \{ + , - , \emptyset \}$ , where the symbols $+ , - , \emptyset$ denote positive, negative, and no report, respectively. Consider the base reputation mechanism described by information structure (1). Let $\eta _ { + } , ~ \eta _ { - }$ denote the (exogenously given) probabilities that a buyer who experiences a satisfactory and unsatisfactory transaction, respectively, will submit feedback to the system.<sup>20</sup> The perturbed mechanism can be described by a new conditional probability distribution:

$$
\begin{array}{c} p (+ \mid c o o p) = \eta_ {+} (1 - \alpha), \qquad p (- \mid c o o p) = \eta_ {-} \alpha , \\ p (\varnothing \mid c o o p) = 1 - \eta_ {+} (1 - \alpha) - \eta_ {-} \alpha , \\ p (+ \mid c h e a t) = \eta_ {+} (1 - \beta), \qquad p (- \mid c h e a t) = \eta_ {-} \beta , \\ p (\varnothing \mid c h e a t) = 1 - \eta_ {+} (1 - \beta) - \eta_ {-} \beta , \\ 0 <   \alpha <   \beta <   1. \end{array}\tag{10}
$$

The following proposition is the counterpart of Proposition 1 in the presence of incomplete reporting.

Proposition 7. The set of sequential equilibrium payoffs of a repeated game where the stage-game structure is described in Table 1, the reputation mechanism has information structure (10), and the entire public history of buyer reports is available to short-run players, is bounded above by

$$
V ^ {*} = 0 \quad i f \rho <   \left(\beta + \min \left(\frac {1}{\eta_ {+}}, \frac {1}{\eta_ {-}}\right) \frac {1 - \delta}{\delta}\right) \frac {1}{\beta - \alpha},
$$

$$
V ^ {*} = \frac {1}{1 - \delta} \left(\widehat {w} _ {2} - c - \left(\frac {1}{\eta_ {+}} - 1 + \alpha\right) \frac {c}{\beta - \alpha}\right)
$$

$$
i f \left(\beta + \frac {1 - \delta}{\eta_ {-} \delta}\right) \frac {1}{\beta - \alpha} > \rho \geq \left(\frac {1 - \eta_ {+} (1 - \beta)}{\eta_ {+}} + \frac {1 - \delta}{\eta_ {+} \delta}\right) \frac {1}{\beta - \alpha},
$$

$$
V ^ {*} = \frac {1}{1 - \delta} \left(\widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha}\right) \quad i f \rho \geq \left(\beta + \frac {1 - \delta}{\eta_ {-} \delta}\right) \frac {1}{\beta - \alpha}.
$$

We see that, for large $\rho ,$ incomplete feedback reporting does not change the maximum achievable payoff of a binary reputation mechanism. However, it increases the minimum stage-game profit margin that is required for the mechanism to induce cooperation. Incomplete reporting thus restricts the applicability of reputation mechanisms to environments with higher premiums for trust.

In the rest of the section, I will show that equilibria that achieve the maximum payoff prescribed by Proposition 7 can be constructed by augmenting the mechanisms of §§3.2 and 3.3 with a policy for treating missing feedback. There are two possible policies:

• Policy 1: Treat missing feedback as positive feedback.

• Policy 2: Treat missing feedback as negative feedback.

The following proposition compares the above policies in terms of the maximum seller payoffs achievable under each of them.

Proposition 8. Let $V _ { 1 } ^ { * } , ~ V _ { 2 } ^ { * }$ be the maximum seller payoffs attainable in a repeated game where the stage-game structure is described in Table 1, the reputation mechanism is either a two-state randomization device or an eBaylike mechanism, the mechanism’s information structure is given by (10), and missing feedback is treated according to Policies 1 and 2, respectively. If

$$
\rho \geq \left(\beta + \left(\frac {1}{\eta_ {-}}\right) \frac {1 - \delta}{\delta}\right) / (\beta - \alpha),
$$

the following statement is true:

$V _ { 1 } ^ { * } = V ^ { * } \geq V _ { 2 } ^ { * }$ equality holds if and only if $\eta _ { + } = 1$

Proposition 8 shows that the most efficient policy for treating missing ratings is Policy 1, an “optimistic” policy that treats missing feedback as positive feedback (“no news is good news”). Pessimistic Policy 2 (“no news is bad news”) is strictly less efficient than Policy 1 if there is incomplete reporting of satisfactory outcomes $( \eta _ { + } < 1 )$ . To see the intuition behind this result, observe that if we consider missing ratings as a distinct report type, then treating them as negative ratings is equivalent to including them in the mechanism’s “bad” report set. If $\eta _ { + } < 1$ , some of the missing ratings correspond to satisfactory transactions (transactions that would have received positive feedback). Missing ratings thus constitute a more noisy statistic of a transaction’s outcome than negative ratings. Adding them into the “bad” report set then increases the probability that cooperating sellers will receive unfair punishment more than it decreases the probability that cheating sellers will escape punishment. This dilutes the ability of the mechanism to distinguish the seller’s action and reduces efficiency. Note that Proposition 8 holds irrespective of the relative magnitudes of $\eta _ { + }$ and $\eta _ { - }$

## 5. Multiple Sellers

All preceding results have been obtained under the assumption of a monopolist seller. This section generalizes the analysis to settings with multiple competing sellers.

Consider a setting where each period n identical sellers offer simultaneous auctions for a homogeneous good to m unit-demand buyers whose valuations are independently drawn from the same probability distribution. A reputation mechanism keeps track of everyone’s past ratings and publishes a reputation profile $x _ { k }$ for each seller $k = 1 , \dots , n .$ . Let x denote the vector that includes the reputation profiles of all sellers and $x _ { - k }$ the vector that includes the reputation profiles of every other seller except seller k.

Dellarocas (2004) derives the form of bidding equilibria in auction settings where n sellers of different reputations simultaneously offer auctions for a homogeneous good to m unit-demand bidders. In such settings bidders not only decide how much to bid, but also in which of the n available auctions to submit bids. Reputations are defined as the buyers commonly held subjective beliefs $s _ { k }$ that seller k will deliver his good. Dellarocas shows that in all bidding equilibria: (i) bidders scale their bids to seller k’s auction by an amount equal to the probability $s _ { k }$ that the seller will cooperate, (ii) bidders follow mixed auction selection strategies with the property that higher reputation sellers receive bids from higher-valuation buyers with higher probability, and (iii) sellers whose reputations are substantially below the average reputation of higher sellers receive no bids.

According to the above results, in simultaneous auction settings, the expected valuation of an auction’s second-highest bidder becomes a function $\widehat { w } _ { 2 } ( s _ { k } \mid x _ { - k } ) \mid s _ { - k } ( x ) )$ that is increasing in each seller’s own strategy, decreasing in every other seller’s strategy, and equal to zero for some strategy configurations. We focus our attention on symmetric perfect public equilibria where each seller’s strategy $s _ { k } ( x ) = s ( x _ { k } \mid x _ { - k } )$ depends only on the current state of his own and everybody else’s reputation profiles. In such equilibria, the expected valuation of an auction’s second-highest bidder also becomes a function $\widehat { w } _ { 2 } ( x _ { k } \mid x _ { - k } )$ of reputation profiles. Each seller’s optimization problem can then be expressed as

$$
= \max _ {s (x _ {k} | x _ {- k})} \left\{ \begin{array}{l l} s (x _ {k} \mid x _ {- k}) \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) - c \\ \quad + \delta \sum_ {x _ {- k} ^ {\prime}} p (x _ {- k} ^ {\prime} \mid x _ {k}, x _ {- k}) \\ \cdot [ (1 - \alpha) V (x ^ {+} (x _ {k}) \mid x _ {- k} ^ {\prime}) \\ \quad + \alpha V (x ^ {-} (x _ {k}) \mid x _ {- k} ^ {\prime}) ] \\ \text {   if   } \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) > 0 \text {   and   } s (x _ {k} \mid x _ {- k}) > 0, \\ 0 \quad \text {   otherwise }, \end{array} \right. \tag {(1)}\tag{11}
$$

subject to the incentive compatibility constraint

$$
\begin{array}{l} \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) > 0 \quad \text { and } \quad s (x _ {k} \mid x _ {- k}) > 0 \\ \Rightarrow \sum_ {x _ {- k} ^ {\prime}} p (x _ {- k} ^ {\prime} \mid x _ {k}, x _ {- k}) [ V (x ^ {+} (x _ {k}) \mid x _ {- k} ^ {\prime}) \\ \qquad - V (x ^ {-} (x _ {k}) \mid x _ {- k} ^ {\prime}) ] \geq c / \delta (\beta - \alpha). \end{array}\tag{12}
$$

Dellarocas (2004) derives an algorithm for computing $\widehat { w } _ { 2 } ( s _ { k } \vert x _ { - k } ) \vert s _ { - k } ( x ) )$ for any configuration of seller strategies. In general, $\widehat { w } _ { 2 } ( \cdot \mid \cdot )$ is a nonlinear function of strategies and, thus, the solution of (11) and (12) does not have a simple closed form. Nevertheless, the following two results show that the symmetric perfect public equilibria induced by reputation mechanisms in settings with competition have important relationships with their monopoly counterparts.

Definition. A finite-state reputation mechanism (FSRM) is a mechanism where the number of possible states of each seller’s reputation profile is finite. The two-state randomization device of §3.2 and the eBay-like mechanism of §3.3 are examples of FSRM.

The first result states that each seller’s expected payoffs induced by an FSRM in settings with competition (expectation is taken over every other seller’s reputation profile states) are equal to the payoffs induced by the same mechanism in some monopoly setting.

Proposition 9. Consider a symmetric PPE induced by an FSRM in a setting with multiple competing sellers. Let $V ( x _ { k } \mid x _ { - k } ) , s ( x _ { k } \mid x _ { - k } )$ denote each seller’s equilibrium payoff and strategy, respectively. Furthermore, let $\pi ( x _ { - k } \mid x _ { k } )$

be the conditional stationary probabilities that the profiles of other sellers will be in state $x _ { - k } . \ I f \ V ( x _ { k } \mid x _ { - k } ) > 0 \ f o r$ all $x _ { k } , x _ { - k } ,$ equilibrium seller payoffs $V ( x _ { k } \mid x _ { - k } )$ satisfy

$$
E _ {x _ {- k} | x _ {k}} [ V (x _ {k} \mid x _ {- k}) ] = V ^ {\prime} (x _ {k}),
$$

where $V ^ { \prime } ( x _ { k } )$ are the payoffs of a PPE induced by the same FSRM in a monopoly setting in which the expected secondhighest bidder’s valuation is equal to

$$
\widehat {w} _ {2} ^ {\prime} = \sum_ {x _ {- k}} \pi (x _ {- k} \mid \overline {{x}} _ {k}) s (\overline {{x}} _ {k} \mid x _ {- k}) \widehat {w} _ {2} (\overline {{x}} _ {k} \mid x _ {- k})\tag{13}
$$

and where $\overline { { x } } _ { k }$ is a profile state for which, in the monopoly case PPE, the seller cooperates with probability one.

The above proposition has important implications for comparing reputation mechanism performance in simultaneous auction settings. According to Corollary 1, in monopoly settings a mechanism’s maximum efficiency exclusively depends on the minimum likelihood ratio of punishment that is induced by that mechanism’s information structure. In simultaneous auction settings, a reputation mechanism’s maximum average efficiency also depends on that mechanism’s equivalent monopoly valuation w<sub></sub> given by Equation (13).

The second important result is that, in simultaneous auction settings with large numbers of buyers, the equilibria induced by reputation mechanisms become asymptotically independent of the reputation of competing sellers.

Proposition 10. In settings where n sellers with different reputations simultaneously offer sealed-bid, secondprice auctions for one unit of a homogeneous good to m unit-demand buyers, as the number of buyers grows to infinity, each seller’s strategy and payoffs converge to a strategy and payoffs induced by the same reputation mechanism in a monopoly setting with m/n buyers.

Proposition 10 implies that all results obtained under the assumption of a monopolist seller are also approximately valid in large-scale online auction settings where large numbers of buyers select among several simultaneous auctions for the same good by sellers of different reputations.

## 6. Concluding Remarks

This paper offers a theoretical analysis of reputation mechanism design in trading environments with pure moral hazard. In such environments there is no uncertainty about the intrinsic characteristics (ability, cost of effort) of a seller. Sellers are assumed to be opportunistic, capable of both cooperation or cheating, and behaving in ways that maximize their expected payoff. The objective of a reputation mechanism in such settings is to induce sellers to engage in cooperative behavior as often as possible. Such a use of reputation mechanisms is qualitatively distinct from the aggregation of consumer feedback for the purpose of informing a community about a product’s or firm’s (initially privately known, but fixed) quality attributes. Throughout the paper, I use the term sanctioning to refer to the former role of reputation mechanisms and signaling to refer to the latter.

My analysis derives several important results related to the optimal design of sanctioning reputation mechanisms. These results are often in sharp contrast with the results that apply to the design of signaling reputation mechanisms. One important message of the paper, therefore, is that there is no one-size-fits-all set of guidelines for reputation mechanism design. Online marketplace designers should be conscious of their mechanism’s primary objective (sanctioning or signaling) and carefully make design choices that maximize the resulting market efficiency, given that objective.

As an application of the general results, the paper offers a simplified model of eBay’s feedback mechanism. The analysis shows that if there is no uncertainty about the seller’s type, eBay’s mechanism, augmented with a summary of a seller’s sums of recent positive and negative ratings (such as an eBay member’s “ID card”), is capable of inducing the maximum possible efficiency. Moreover, it allows traders to maximize their payoffs by relying on a simple stationary strategy according to which a seller’s anticipated probability of cooperation in the current period is a decreasing linear function of the sum of negative ratings in his current eBay “ID card.” This property makes eBay’s mechanism especially well suited to large-scale online trading environments, as it allows even inexperienced traders to perform well by relying on simple, intuitive behavior rules.

In terms of future work, the analysis of this paper can be extended in a number of dimensions. First, I have assumed only two possible seller actions. An interesting extension is to consider environments with multiple, or continuous, seller actions. Second, my model does not cover multiple simultaneous auctions by the same seller. This occurs frequently on eBay and could allow an unscrupulous seller to build a reputation through a series of single, positive sales and then cheat on a large number of simultaneous sales. Most importantly, however, this paper assumes that the seller’s cost structure and conditional probabilities of outcomes given effort are known to buyers: In other words, buyers have no uncertainty about the “type” of seller they are facing. In many online environments it is plausible that there might be different seller types with different cost structures and/or conditional probabilities of outcomes, initially unknown to buyers. For example, in online marketplaces for professional services, such as eLance, professionals of varying (and privately known) ability levels advertise their services. In such settings, reputation mechanisms play a hybrid (signaling and sanctioning) role: In addition to eliciting “good conduct,” past feedback should, ideally, also help buyers learn something about the unknown properties (type) of the seller they are facing. The design principles of such hybrid reputation mechanisms constitute an intriguing area for future research.

## Acknowledgments

This material is based on work supported by the National Science Foundation under CAREER Grant 9984147. The author is grateful to Yannis Bakos, Erik Brynjolfsson, Jacques Crémer, Drew Fudenberg, Roy Radner, Jean Tirole, Dimitri Vayanos, and the participants of seminars at IDEI Toulouse, the London Business School, Massachusetts Institute of Technology, Stanford University, the University of Minnesota, and the University Pompeu Fabra in Barcelona for helpful comments.

## Appendix

Proof of Proposition 1. In their 1994 paper, Fudenberg and Levine introduced an algorithm (known as the maximal score method) for computing the limiting set of payoffs of perfect public equilibria of games with long-run and shortrun players. One class of games for which the maximal score method acquires a particularly simple form are games with a product structure. Such games have the property that there is a separate public signal for each long-run player that is independent of the signal for other long-run players and depends only on his own play and that of the shortrun players. According to this definition, all games with a single long-run player have a product structure.

Consider a game with a single long-run player and n short-run players. Denote by K the long-run player’s pure action set, -K the corresponding space of mixed actions, R the set of (publicly observable) stage-game outcomes, and B. $\Delta K \to { \bar { \Delta } } K _ { 1 } \times \cdots \times \Delta K _ { n }$ the correspondence that maps any mixed action profile for the long-run player to the corresponding static equilibria for the short-run players. Furthermore, let $h ( k , \kappa _ { S R } )$ denote the long-run player’s stage-game payoff and $p ( r \mid k , \kappa _ { S R } )$ denote the probability that the stage-game outcome will be $r \in R$ if the longrun player plays $k \in K$ and the short-run players play a mixed action $\kappa _ { S R } \in \mathbf { B } ( \kappa )$ for some $\kappa \in \Delta K$ . Let $\Pi ( \kappa _ { S R } )$ be the matrix with rows corresponding to actions $k ,$ columns to outcomes $r ,$ and with the $( k , \bar { r } )$ component equal to $p ( r | k , \kappa _ { S R } )$ . If a game has a product structure and, in addition, has the property that $\Pi ( \kappa _ { S R } )$ has full row rank $( \mathrm { i . e . , }$ rank equal to the number of the long-run player’s actions), then Fudenberg and Levine (1994) show that the maximum long-run player payoff v is the solution of the following linear programming problem:

$$
\begin{array}{l l} \underset {\kappa \in \Delta K,   u (r) \in \mathbb {R}} {\max} v \\ \text { subject   to } & v = h (k,   \kappa_ {S R}) + \delta \sum_ {r \in R} p (r \mid k,   \kappa_ {S R}) u (r) \\ & \text { for   } k \in K \text {   such   that   } \kappa (k) > 0, \\ & v \geq h (k,   \kappa_ {S R}) + \delta \sum_ {r \in R} p (r \mid k,   \kappa_ {S R}) u (r) \\ & \text { for   } k \in K \text {   such   that   } \kappa (k) = 0, \\ & v \geq u (r) \quad \text { for   } r \in R. \end{array}
$$

If, in addition, short-run player actions are observable, Theorem 5.2 of the same paper asserts that the set of sequential equilibrium payoffs is the same as the set of perfect public equilibrium payoffs. This set includes all equilibria where the seller conditions his actions on both public information and private information.

The bilateral exchange game that forms the basis of this paper has $K = \{ H , L \}$ (high effort, low effort), $R = \{ + , - \}$ (positive report, negative report), and mixed seller actions characterized by a probability $s \in [ 0 , 1 ]$ of playing H. The corresponding static best response of the short-run buyers is to bid amounts equal to $G _ { i } = s w _ { i }$ . This results in expected stage-game seller payoffs $h ( H , \kappa _ { S R } ) = s \widehat { w } _ { 2 } - c$ and $h ( \bar { L } , \kappa _ { S R } ) = s \bar { \widehat { w } } _ { 2 }$ . Finally,

$$
\Pi (\kappa_ {S R}) = \left[ \begin{array}{c c} p (+ | H, \kappa_ {S R}) & p (- | H, \kappa_ {S R}) \\ p (+ | L, \kappa_ {S R}) & p (- | L, \alpha_ {S R}) \end{array} \right] = \left[ \begin{array}{c c} 1 - \alpha & \alpha \\ 1 - \beta & \beta \end{array} \right].
$$

The above stage-game satisfies the full row rank condition (because Rank $\Pi ( \kappa _ { S R } ) = 2 )$ and has observable short-run player actions. According to the above, the maximum longrun player sequential equilibrium payoff v is the solution of the following linear programming problem:

max v s 01 u  u 

$$
\begin{array}{l l} \text {subject to} & v = s \widehat {w} _ {2} - c + \delta [ (1 - \alpha) u (+) + \alpha u (-) ] \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {for k = H and s > 0 ,} \\ & v \geq s \widehat {w} _ {2} - c + \delta [ (1 - \alpha) u (+) + \alpha u (-) ] \\ & \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {for k = H and s = 0 ,} \\ & v = s \widehat {w} _ {2} + \delta [ (1 - \beta) u (+) + \beta u (-) ] \\ & \qquad \qquad \qquad \qquad \qquad \text {for k = L and s <   1 ,} \\ & v \geq s \widehat {w} _ {2} + \delta [ (1 - \beta) u (+) + \beta u (-) ] \\ & \qquad \qquad \qquad \qquad \text {for k = L and s = 1 ,} \\ & v \geq u (+), \quad v \geq u (-). \end{array}
$$

In addition, intermediate payoffs must satisfy $u ( + ) \geq 0$ $u ( - ) \geq 0$ because no seller will stay in the game if he transitions to a state where the present value of future payoffs is negative.

For $\rho < ( \beta + ( 1 - \delta ) / \delta ) / ( \beta - \alpha )$ , the above problem has solution $v = 0 , \ s = 0 , \ u ( + ) = u ( - ) = 0 ,$ , whereas for $\rho \geq$ $( \beta + ( 1 - \delta ) / \delta ) / ( \beta - \alpha )$ , the solution becomes

$$
\begin{array}{c} v = \frac {1}{1 - \delta} \bigg [ \widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha} \bigg ], \\ s = 1, \\ u (+) = v, \\ u (-) = v - \frac {c}{\delta (\beta - \alpha)}. \quad \square \end{array}\tag{14}
$$

Proof of Proposition 2. The present value of a cooperating seller’s discounted payoff while the seller remains in the “good” state is described by the following Bellman equation:

$$
V _ {g o o d} = \widehat {w} _ {2} - c + \delta [ (1 - \alpha) V _ {g o o d} + \alpha [ (1 - \pi) V _ {g o o d} + \pi V _ {b a d} ] ],
$$

where $0 \leq \pi \leq 1 , \ : V _ { b a d } = 0$ . Rearranging, we get

$$
V _ {g o o d} = \frac {\widehat {w} _ {2} - c}{1 - \delta (1 - \alpha \pi)}.\tag{15}
$$

The above is maximized for  equal to the minimum value that induces cooperation. The seller will cooperate if and only if the following incentive compatibility constraint holds:

$$
\begin{array}{c} - c + \delta [ (1 - \alpha) V _ {g o o d} + \alpha (1 - \pi) V _ {g o o d} ] \\ \geq \delta [ (1 - \beta) V _ {g o o d} + \beta (1 - \pi) V _ {g o o d} ]. \end{array}
$$

The constraint implies $\pi \geq c / \delta ( \beta - \alpha ) V _ { g o o d }$ . Substituting $\pi =$ $c / \delta ( \beta - \alpha ) V _ { g o o d }$ into (15), we obtain

$$
\begin{array}{c} V _ {g o o d} = \frac {1}{1 - \delta} \biggl [ \widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha} \biggr ] \text {and} \\ \pi = (1 - \delta) / \delta [ \rho (\beta - \alpha) - \beta ]. \end{array}
$$

The requirement $0 \leq \pi \leq 1$ implies

$$
\rho \geq \left(\beta + \frac {1 - \delta}{\delta}\right) / (\beta - \alpha).
$$

For

$$
\rho <   \left(\beta + \frac {1 - \delta}{\delta}\right) / (\beta - \alpha),
$$

no $0 \leq \pi \leq 1$ can provide sufficient incentives for seller cooperation. The only equilibrium is one where the seller cheats, no buyers place bids, and $V _ { g o o d } = 0 .$ 

Proof of Proposition 3. I will assume that the seller follows a mixed strategy conditioned on the number of negative ratings z in his public reputation profile. Specifically, let

$$
s (z (x)) = 1 - z (x) \theta ,\tag{16}
$$

that is, the seller cooperates as long as there are no negative ratings in his profile and his probability of cooperation decreases by a fixed amount % with every additional negative rating on his public reputation profile. I will show that if $\rho = \widehat { w } _ { 2 } / c$ is sufficiently high, then there exists a % such that the above strategy constitutes an equilibrium strategy that achieves the maximum attainable payoff predicted by Proposition 1.

Let x be the algebraic representation of a seller’s private reputation profile that arises from mapping every positive report in his profile to the digit 1 and every negative report to the digit 0. For a mixed strategy, the incentive compatibility constraint (7) simplifies to

$$
V (2 (x \oplus 2 ^ {N - 1}) + 1) - V (2 (x \oplus 2 ^ {N - 1})) = c / \delta (\beta - \alpha),
$$

or, equivalently, to

$$
V (x) - V (x - 1) = c / \delta (\beta - \alpha) \quad \text { for   all   odd } x.\tag{17}
$$

For $0 < s ( z ( x ) ) \leq 1$ , the seller’s Bellman Equation (6) can be written as

$$
\begin{array}{l} V (x) = (1 - z (x) \theta) \widehat {w} _ {2} - c + \delta \big [ (1 - \alpha) V (2 (x \oplus 2 ^ {N - 1}) + 1) \\ \qquad + \alpha V (2 (x \oplus 2 ^ {N - 1})) \big ] \quad \text { for } 0 \leq x \leq 2 ^ {N} - 1. \end{array}\tag{18}
$$

In the rest of the proof, I will refer to the term $( 1 - z ( x ) \theta )$ $\widehat { w } _ { 2 } \ - \ c$ above as the stage-game payoff and to the term $\delta [ ( 1 - \alpha ) V ( 2 ( x \oplus 2 ^ { N - 1 } ) + 1 ) \stackrel { \sim } { + } \stackrel { \sim } { \alpha } V ( 2 ( x \stackrel { \sim } { \oplus } 2 ^ { N - 1 } ) ) ]$ as the continuation payoff. To show that strategy (16) is an equilibrium strategy, it suffices to show that there exists %, such that the solution $\{ V ( x ) \ | \ x = 0 , \ldots , 2 ^ { N } - 1 \}$ of the system of Bellman Equations (18) satisfies the incentive compatibility constraint (17) for all odd x. I proceed by deriving some key properties of the solution of Equation (18):

1. For all $x \ge 2 ^ { N - 1 }$ , states x and $x - 2 ^ { N - 1 }$ correspond to private profiles that differ from each other in the leading digit only (for example, for $N = 4 , { \mathrm { ~ i f ~ } } x = 1 5 = 1 1 1 1$ , then $x - 2 ^ { 3 } = \overset { \cdot } { 1 5 } - 8 = 7 = \overset { \cdot } { 0 1 1 1 } )$ ). Specifically, state x has a 1 and state $x - 2 ^ { N - 1 }$ has a 0 in that position. Thus, state $x - 2 ^ { N - 1 }$ has one more zero than state x (formally, $z ( x - 2 ^ { N - 1 } ) =$ $z ( x ) + 1 )$ . The stage-game payoffs of the two states thus differ by $\theta \widehat { w } _ { 2 }$ . Furthermore, ${ \stackrel { . } { x } } { \oplus { 2 ^ { N - 1 } } } = ( x - 2 ^ { N - 1 } ) \oplus 2 ^ { N - 1 }$ , which means that the continuation payoffs of states x and $x - 2 ^ { N - 1 }$ are identical. Intuitively, this situation arises because, following the current period, the leading digit on which the two states differ will be eliminated from the profile, and the rest of the two profiles are identical. By substituting the above into (18), we obtain

$$
V (x) - V (x - 2 ^ {N - 1}) = \theta \widehat {w} _ {2} \quad \text { for   all } x \geq 2 ^ {N - 1}.\tag{19}
$$

2. For all $x \ge 2 ^ { N - 1 } + 2 ^ { N - 2 } ,$ , states x and $x - 2 ^ { N - 2 }$ correspond to private profiles that differ from each other in the second digit from the left only. Specifically, state x has a 1 and state $\stackrel { \smile } { x } - 2 ^ { N - 2 }$ has a 0 in that position (for example, for $N = 4 , \mathrm { i f } \ x = 1 5 = 1 1 1 1$ , then $x - \hat { 2 ^ { N - 2 } } = 1 5 - 4 = 1 1 \overset { \cdot } { = } 1 0 1 1 )$ Thus, state $x - 2 ^ { N - 2 }$ has one more zero than state x (formally, $z ( x - 2 ^ { N - 2 } ) = z ( x ) + 1 )$ . The current-period payoffs of the two states thus differ by $\theta \widehat { w } _ { 2 }$ . Furthermore, $2 ( \dot { ( x - 2 ^ { N - 2 } ) }$ ① $2 ^ { N - 1 } ) = 2 ( x \oplus 2 ^ { N - 1 } ) - \bar { 2 } ^ { N - 1 } ,$ and thus, by Equation (19), $V ( 2 ( ( x - 2 ^ { N - 2 } ) \oplus 2 ^ { N - 1 } ) ) = V ( 2 ( x \oplus 2 ^ { N - 1 } ) ) - \mathsf { \bar { \theta } } \widehat { w } _ { 2 }$ . Substituting the above into (18), we obtain

$$
\begin{array}{c} V (x) - V (x - 2 ^ {N - 2}) = (1 + \delta) \theta \widehat {w} _ {2} \\ \text { for   all } x \geq 2 ^ {N - 1} + 2 ^ {N - 2}. \end{array}\tag{20}
$$

3. Continuing in this manner, one can show that for all $\textstyle x \geq \sum _ { i = 1 } ^ { k } 2 ^ { N - i }$ , states x and $x - 2 ^ { N - k }$ correspond to private profiles that differ from each other in the kth digit from the left only, and, furthermore, that

$$
V (x) - V (x - 2 ^ {N - k}) = \left(\sum_ {i = 0} ^ {k - 1} \delta^ {i}\right) \theta \widehat {w} _ {2} \quad \text { for   all } x \geq \sum_ {i = 1} ^ {k} 2 ^ {N - i}.\tag{21}
$$

4. For $k = N ,$ , the above condition becomes

$$
V (2 ^ {N} - 1) - V (2 ^ {N} - 2) = \left(\sum_ {i = 0} ^ {N - 1} \delta^ {i}\right) \theta \widehat {w} _ {2}.\tag{22}
$$

If we choose $\theta = c / \delta ( \beta - \alpha ) ( \sum _ { i = 0 } ^ { N - 1 } \delta ^ { i } ) \widehat { w } _ { 2 } = c / ( \beta - \alpha ) \ \times$ $\begin{array} { r } { \sum _ { i = 1 } ^ { N } \delta ^ { i } \widehat { w } _ { 2 } } \end{array}$ , then comparison of (17) and (22) shows that the solution of Bellman Equation (18) satisfies the incentive compatibility constraint (17) for $x = 2 ^ { N } - 1$ . By using Equation (21), one can show that the incentive compatibility constraint is also satisfied for all odd x. For example, to show that the incentive compatibility constraint is satisfied for $x = 2 ^ { N } - 3 ,$ , substitute $\dot { k } = N \dot { - } 1$ into Equation (21). The equation becomes $V ( 2 ^ { N } - 1 ) - V ( 2 ^ { N } - \hat { 3 } ) =$ $\begin{array} { r } { V ( 2 ^ { N } - 2 ) - V ( \dot { 2 } ^ { N } - 4 ) = ( \sum _ { i = 0 } ^ { N - 2 } \delta ^ { i } ) \dot { \theta } \widehat { w } _ { 2 } } \end{array}$ . Rearranging, we obtain $V ( 2 ^ { N } - 3 ) \ : - \ : V ( 2 ^ { N } - 4 ) = V ( 2 ^ { N } - 1 ) \ : - \ : V ( 2 ^ { N } - 2 )$ Because we have already established that $V ( 2 ^ { N } - 1 ) ~ - ~$ $V ( 2 ^ { N } - 2 ) = c / \delta ( \beta - \alpha ) .$ , this implies that $V ( 2 ^ { N } \mathrm { ~ - ~ } 3 ) \mathrm { ~ - ~ }$ $V ( 2 ^ { N } - 4 ) = c / \delta ( \beta - \alpha )$ , i.e., the incentive compatibility constraint holds for $x = 2 ^ { N } - 3$ . Substituting progressively lower values of k into Equation (21) and using a similar reasoning, we can show that the incentive compatibility constraint is satisfied for all odd x.

Because $s ( z ) = 1 - z \theta$ represent probabilities, it must be $1 - z \theta \geq 0$ for all z N . This requires that $\theta \leq 1 / N _ { \cdot }$ , or, equivalently, that $\begin{array} { r } { \rho = \widehat { w } _ { 2 } / c \geq N / ( \beta - \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i } . } \end{array}$

To summarize, if $\rho = \widehat { w } _ { 2 } / c \geq N / ( \bar { \beta } - \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i } ,$ I have shown that there exists an equilibrium where the seller conditions his probability of cooperation on the number of negative ratings in his current profile according to the formula $\begin{array} { r } { s ( z ( x ) ) = 1 - z ( x ) \theta , \theta = c / ( \hat { \beta ^ { - } } \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i } \widehat { w } _ { 2 } . } \end{array}$ . The seller’s maximum attainable payoff occurs when $x = 2 ^ { N } - 1$ , i.e., when the seller has no negative ratings in his profile. From (18) and (17) we obtain

$$
V (2 ^ {N} - 1) = \frac {1}{1 - \delta} \left[ \widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha} \right] = V ^ {*}.
$$

To show that for $\rho < N / ( \beta - \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i }$ all public perfect equilibria (PPE) attain efficiency lower than $V ^ { * }$ , by Proposition 1 it suffices to show that for such $\rho$ there can be no PPE that attains maximum efficiency equal to $V ^ { * }$ . The sketch of the argument is as follows: Assume a general PPE where $\mathfrak { s } ( z ) \geq \mathbf { \bar { 0 } } , \ z = 0 , \dots , N$ . First, by examining Bellman Equation (18), we see that the only way to attain $V ( 2 ^ { N } - 1 ) \stackrel { - } { = } V ^ { * }$ is if (i) $s ( z = 0 ) = 1 ,$ , and (ii) the incentive compatibility constraint $V ( 2 ^ { N } - 1 ) - V ( 2 ^ { N } - 2 ) \ge c / \delta ( \beta - \alpha )$ holds with equality for $x = 2 ^ { N } - 1$ . Second, by applying the reasoning Steps 1–4 above for arbitrary $s ( z )$ , we derive the constraint $\begin{array} { r } { V ( \dot { 2 } ^ { N } - 1 ) - V ( 2 ^ { N } - 2 ) = \sum _ { i = 0 } ^ { \check { N } - 1 } \dot { \delta } ^ { i } ( s ( 0 ) - s ( 1 ) ) \widehat w _ { 2 } , } \end{array}$ equivalent to Equation (22). Together with the above, this implies that $s ( 1 ) = 1 - \theta .$ . Continuing in this manner for lower values of x, we show that the only PPE that attains $V ( 2 ^ { N } - 1 ) = V ^ { * }$ must have $s ( z ) = 1 - z \theta \geq 0 , z = 0 , \ldots , N .$ . Such an equilibrium cannot exist when $\rho < N / ( \beta - \alpha ) \sum _ { i = 1 } ^ { N } \delta ^ { i }$ , because then sz will become negative for high z, which contradicts our assumption. <sup></sup>

Proof of Proposition 4. To discourage identity changes, the entrance fee must make a new seller’s expected discounted lifetime payoff smaller than or equal to the payoff of any intermediate state. From the proof of Proposition 3 (Equation (21)) we have established that the presence of a negative rating in the kth position (from the left) of a seller’s private profile reduces his remaining discounted lifetime payoff, relative to a state where there is no negative rating in that position, by an amount equal to $\textstyle \sum _ { i = 0 } ^ { k - 1 } \delta ^ { i } \theta \widehat { w } _ { 2 }$ . Therefore, the intermediate state with the lowest payoff is a state where the seller’s private profile contains negative ratings in all N positions. The payoff difference between that state and a state where the seller’s private profile contains no

negative ratings is equal to

$$
\begin{array}{c} \sum_ {k = 1} ^ {N} \sum_ {i = 0} ^ {k - 1} \delta^ {i} \theta \widehat {w} _ {2} = \frac {\sum_ {k = 1} ^ {N} \sum_ {i = 0} ^ {k - 1} \delta^ {i}}{\sum_ {i = 1} ^ {N} \delta^ {i}} \frac {c}{\beta - \alpha} \\ = \bigg (\frac {N}{\delta (1 - \delta^ {N})} - \frac {1}{1 - \delta} \bigg) \frac {c}{\beta - \alpha}. \end{array}
$$

If we assume that new sellers start with a clean profile and we set the entrance fee $f$ equal to the above payoff difference, their expected discounted lifetime payoff will be equal to

$$
\begin{array}{l} V _ {f r e e - i d s} (N) = V (x = 2 ^ {N} - 1) - f \\ \qquad = \frac {1}{1 - \delta} \bigg (w - c - \frac {\alpha c}{\beta - \alpha} \bigg) \\ \qquad - \bigg (\frac {N}{\delta (1 - \delta^ {N})} - \frac {1}{1 - \delta} \bigg) \frac {c}{\beta - \alpha} \\ \qquad = V (x = 0). \end{array}
$$

Because N grows faster than $1 - \delta ^ { N }$ (for $\delta < 1 .$ , it is $( 1 - \delta ^ { N + 1 } ) - ( \bar { 1 } - \delta ^ { N } ) < 1 )$ , the entrance fee f and associated payoff losses grow with N . They attain their minimum value for $N = 1$ . For $N = 1$ , the entrance fee becomes equal to $c / \delta ( \beta - \alpha )$ . 

Proof of Proposition 5. The proof is similar to the proof of Proposition 1 and makes use of Fudenberg and Levine’s (1994) maximal score method. The basic difference is that the assumption of costless identity changes requires that the payoffs of intermediate states of the game are at least as high as the payoffs of the initial state (otherwise, whenever players are faced with the prospect of entering such states, they will simply disappear and restart the game under a different identity). The constraint $v \geq u ( r )$ for $r \in R$ of the linear programming problem of Proposition 1 must thus be replaced with the constraint $v \leq u ( r )$ for $r \in R .$ 

Proof of Proposition 6. The proof is analogous to the proof of Proposition 1 and makes use of Fudenberg and Levine’s (1994) maximal score method. The corresponding linear programming problem in the case where there are multiple possible buyer reports is

$$
\begin{array}{l} \max _ {s \in [ 0, 1 ], u (R _ {i})} v \\ \text { subject   to } v = s \widehat {w} _ {2} - c + \delta \sum_ {i = 1} ^ {m} \alpha_ {i} u (R _ {i}) \quad \text { for } s > 0, \\ v \geq s \widehat {w} _ {2} - c + \delta \sum_ {i = 1} ^ {m} \alpha_ {i} u (R _ {i}) \quad \text { for } s = 0, \\ v = s \widehat {w} _ {2} + \delta \sum_ {i = 1} ^ {m} \beta_ {i} u (R _ {i}) \quad \text { for } s <   1, \\ v \geq s \widehat {w} _ {2} + \delta \sum_ {i = 1} ^ {m} \beta_ {i} u (R _ {i}) \quad \text { for } s = 1, \\ v \geq u (R _ {i}) \geq 0. \end{array}\tag{23}
$$

By referring to Proposition 1, we can see that one solution that satisfies the constraints of the problem (but that is not necessarily optimal) can be constructed by splitting the set of report types into two subsets, a bad set $B \subset R$ and a good set $G = R - B ,$ and constraining the continuation payoffs $u ( R _ { i } )$ so that the payoffs associated with any report that belongs to the same subset are equal. The problem then reduces to that of calculating the maximum efficiency of a binary reputation mechanism where the equivalent of the parameter pair $\alpha , \beta$ is the pair $a ( B ) , b ( B )$ , defined by $a ( B ) =$ $\begin{array} { r } { \sum _ { R _ { i } \in B } \alpha _ { i } , b ( B ) = \sum _ { R _ { i } \in B } \beta _ { i } } \end{array}$ . The solution of this problem is an exact counterpart of Equation (14):

$$
\begin{array}{c} v ^ {*} = \frac {1}{1 - \delta} \bigg [ \widehat {w} _ {2} - c - \frac {a (B) c}{b (B) - a (B)} \bigg ], \\ s = 1, \\ u (R _ {i}) = v ^ {*}, \quad R _ {i} \in B, \\ u (R _ {j}) = v ^ {*} - \frac {c}{\delta (b (B) - a (B))}, \quad R _ {j} \in R - B, \end{array}\tag{24}
$$

if $\rho \ge ( b ( B ) + ( 1 - \delta ) / \delta ) / ( b ( B ) - a ( B ) )$ , and $v ^ { * } = 0$ otherwise.

The above solution corresponds to an equilibrium where the seller is punished by an amount $c / \delta ( b ( B ) - a ( B ) )$ every time he receives any report whose type belongs to the set B (and is not punished otherwise). The set B that maximizes the resulting payoff $v ^ { * }$ is the subset of R that minimizes the quantity $a ( B ) / ( b ( B ) - a ( B ) )$ , or equivalently, the likelihood ratio of punishment $a ( B ) / b ( B )$

I will now show that we cannot improve upon the above solution by more fine-grained punishment rules that split report types into more than two subsets (e.g., good, bad, and “intermediate” reports) and administer different levels of punishment when the seller receives a report that belongs to each subset. Observe that the optimization problem (23) reduces to choosing continuation payoffs $v \geq u ( R _ { i } ) \geq 0$ that maximize

$$
v = \widehat {w} _ {2} - c + \delta \sum_ {i = 1} ^ {m} \alpha_ {i} u (R _ {i})\tag{25}
$$

subject to the incentive compatibility constraint

$$
\delta \sum_ {i = 1} ^ {m} (\alpha_ {i} - \beta_ {i}) u (R _ {i}) = c.\tag{26}
$$

Consider a partition of the set of report types R into three subsets: Good report types G with corresponding continuation payoffs $u ( R _ { i } \mid R _ { i } \in G ) = v ,$ , bad report types B with continuation payoffs $u ( R _ { i } \mid R _ { i } \in B ) = v ^ { \prime } < v ,$ and intermediate report types I with continuation payoffs $u ( R _ { i } \mid R _ { i } \in$ $I ) = v ^ { \prime \prime } < v .$ As before, let $\begin{array} { r } { a ( B ) = \sum _ { R _ { i } \in B } \alpha _ { i } , \ b ( B ) = \sum _ { R _ { i } \in B } \beta _ { i } } \end{array}$

Equation (26) can be rewritten as

$$
\begin{array}{r l} & {\delta \bigg (\sum_ {i | R _ {i} \in G} (\alpha_ {i} - \beta_ {i}) v + \sum_ {i | R _ {i} \in I} (\alpha_ {i} - \beta_ {i}) v ^ {\prime \prime} + (a (B) - b (B)) v ^ {\prime} \bigg)} \\ & {\qquad = \delta (b (B) - a (B)) (\hat {v} - v ^ {\prime}) = c,} \end{array}
$$

where

$$
\hat {v} = \left(\sum_ {i | R _ {i} \in G} (\alpha_ {i} - \beta_ {i}) v + \sum_ {i | R _ {i} \in I} (\alpha_ {i} - \beta_ {i}) v ^ {\prime \prime}\right) / \sum_ {i | R _ {i} \in G \cup I} (\alpha_ {i} - \beta_ {i}) <   v
$$

and

$$
\sum_ {i | R _ {i} \in G \cup I} (\alpha_ {i} - \beta_ {i}) = (1 - a (B)) - (1 - b (B)) = b (B) - a (B).
$$

The above equation gives $v ^ { \prime } = \hat { v } - c / \delta ( b ( B ) - a ( B ) )$ , which shows that $\dot { v ^ { \prime } }$ grows with v<sub></sub>. Therefore, if we replace the continuation payoff $v ^ { \prime \prime }$ associated with the intermediate report types with the payoff v associated with good report types (effectively collapsing the distinction of report types into good and bad only), then the bad report continuation payoff $v ^ { \prime }$ that satisfies the incentive compatibility constraint (26) grows, and, therefore, the value of the objective function (25) also grows because the continuation payoffs of all states are greater than or equal to the corresponding continuation payoffs of the original solution. Therefore, any equilibrium that involves more than two sets of continuation payoffs associated with different report types is dominated by an equilibrium where “intermediate” report types are considered as good report types. The maximum payoff (24) that is attainable by considering two sets of continuation payoffs (the payoff that arises when we choose the bad report set so that the likelihood ratio $a ( B ) / b ( B )$ is minimized) is thus the maximum payoff attainable by any public perfect equilibrium of the game (and, by Theorem 5.2 of Fudenberg and Levine 1994, by any sequential equilibrium of the game). <sup></sup>

Proof of Proposition 7. The proof is an application of Proposition 6 in the special case where the mechanism’s information structure is given by (10). The three cases of the resulting expression arise as follows:

For $B = \{ + , - , \emptyset \}$ , the set of nonempty proper subsets $S \subset$ R and their associated probabilities of incidence $a ( S )$ , bS is summarized below:

<table><tr><td> $S_i$ </td><td> $a(S_i)$ </td><td> $b(S_i)$ </td><td> $b(S_i) - a(S_i)$ </td></tr><tr><td> $S_1 = \{+\}$ </td><td> $\eta_+(1-\alpha)$ </td><td> $\eta_+(1-\beta)$ </td><td> $\eta_+(\alpha-\beta)$ </td></tr><tr><td> $S_2 = \{-\}$ </td><td> $\eta_-\alpha$ </td><td> $\eta_-\beta$ </td><td> $\eta_-(\beta-\alpha)$ </td></tr><tr><td> $S_3 = \{\varnothing\}$ </td><td> $(1-\eta_*)(1-\alpha) + (1-\eta_-)\alpha$ </td><td> $(1-\eta_*)(1-\beta) + (1-\eta_-)\beta$ </td><td> $(\eta_+ - \eta_-)(\beta - \alpha)$ </td></tr><tr><td> $S_4 = \{+, \varnothing\}$ </td><td> $1-\eta_-\alpha$ </td><td> $1-\eta_-\beta$ </td><td> $\eta_-(\alpha-\beta)$ </td></tr><tr><td> $S_5 = \{+, -\}$ </td><td> $\eta_+(1-\alpha) + \eta_-\alpha$ </td><td> $\eta_+(1-\beta) + \eta_-\beta$ </td><td> $(\eta_- - \eta_+(\beta-\alpha)$ </td></tr><tr><td> $S_6 = \{-, \varnothing\}$ </td><td> $1-\eta_+(1-\alpha)$ </td><td> $1-\eta_+(1-\beta)$ </td><td> $\eta_+(\beta-\alpha)$ </td></tr></table>

Define

$$
l _ {i} = a (S _ {i}) / b (S _ {i}) \quad \text { and } \quad \underline {{\rho}} _ {i} = \left(b (S _ {i}) + \frac {1 - \delta}{\delta}\right) \bigg / (b (S _ {i}) - a (S _ {i})).
$$

It is easy to see that if $l _ { i } < l _ { j }$ and $b ( S _ { i } ) - a ( S _ { i } ) > b ( S _ { j } ) - a ( S _ { j } )$ then $\underline { { \rho } } _ { i } < \underline { { \rho } } _ { j } . \mathrm { ~ I ~ }$ will now proceed to solve the constrained optimization problem (8) for the above set of parameters:

1. Subsets $S _ { 1 }$ and $S _ { 4 }$ are eliminated from further consideration because, for $\alpha < \beta ,$ it is $b ( S _ { i } ) < a ( S _ { i } )$

2. If $\eta _ { + } > \eta _ { - }$ , then subset $S _ { 5 }$ is likewise eliminated. From among the remaining three subsets, $l _ { 2 } \leq l _ { 6 } \leq l _ { 3 }$ . Furthermore, the minimum required stage-game profit margins satisfy $\varrho _ { 3 } \geq \varrho _ { 6 }$ . In addition, if $\eta _ { + }$ is sufficiently higher than ) , it is also $\underline { { \rho } } _ { 2 } \geq \underline { { \rho } } _ { 6 }$ . These relationships imply that (i) if $\rho \ge \underline { { \rho } } _ { 2 } ,$ then the mechanism’s maximum efficiency is detemined by the likelihood ratio $l _ { 2 } ; ~ ( \mathrm { i i } )$ if $\underline { { \rho } } _ { 2 } > \rho \geq \underline { { \rho } } _ { 6 } ,$ then the mechanism’s maximum efficiency is determined by the likelihood ratio $l _ { 6 } ;$ and (iii) if $\rho < \underline { { \rho } } _ { 6 } ,$ then the constrained optimization problem that specifies the mechanism’s efficiency has no solution, hence $\bar { V } ^ { * } = 0 .$

3. If $\eta _ { + } < \eta _ { - }$ , then subset $S _ { 3 }$ is likewise eliminated. From among the remaining three subsets, $l _ { 2 } \leq l _ { 6 }$ (equality iff $\eta _ { + } = 1 )$ and $l _ { 2 } \leq l _ { 5 }$ (equality iff $\eta _ { + } = 0 )$ . Furthermore, the minimum required stage-game profit margins satisfy $\rho _ { 2 } \leq$ $\underline { { \rho } } _ { 6 }$ and $\underline { { \rho } } _ { 2 } \leq \underline { { \rho } } _ { 5 }$ . These relationships imply that (i) if $\rho \geq \underline { { \rho } } _ { 2 } ,$ then the mechanism’s maximum efficiency is determined by the likelihood ratio $l _ { 2 } ,$ and (ii) if $\rho < \underline { { \rho } } _ { 2 } ,$ then the constrained optimization problem that specifies the mechanism’s efficiency has no solution, hence $V ^ { * } = 0$

If we replace the corresponding algebraic expressions for $l _ { 2 }$ and $l _ { 6 }$ into (8), we obtain the expressions listed in Proposition 7. <sup></sup>

Proof of Proposition 8. From Corollary 1, comparison of the maximum efficiency of two reputation mechanisms reduces to the comparison of their corresponding likelihood ratios of punishment. Binary reputation mechanisms augmented with Policies 1 and 2 are equivalent to 3-valued reputation mechanisms with bad report sets equal to $B _ { 1 } = \{ - \}$ and $B _ { 2 } = \{ - , \emptyset \} ,$ respectively. Given information structure (10), the corresponding likelihood ratios of punishment can be constructed by observing that

$$
\begin{array}{l l} a (B _ {1}) = \eta_ {-} \alpha , & a (B _ {2}) = 1 - \eta_ {+} (1 - \alpha), \\ b (B _ {1}) = \eta_ {-} \beta , & b (B _ {2}) = 1 - \eta_ {+} (1 - \beta). \end{array}
$$

Therefore,

$$
l _ {1} = \frac {a (B _ {1})}{b (B _ {1})} = \frac {\alpha}{\beta}, \quad l _ {2} = \frac {a (B _ {2})}{b (B _ {2})} = \frac {1 - \eta_ {+} (1 - \alpha)}{1 - \eta_ {+} (1 - \beta)}.
$$

It is easy to see that $l _ { 1 } \leq l _ { 2 }$ with equality if and only if $\eta _ { + } = 1$ . According to Corollary 1, this implies that the maximum efficiencies induced by the two mechanisms satisfy $V _ { 1 } ^ { * } \geq V _ { 2 } ^ { * }$ with equality if and only if $\eta _ { + } = 1$ . Finally, because the likelihood ratio $l _ { 1 }$ is equal to the likelihood ratio of punishment in the baseline case where all buyers submit feedback, from Corollary 1 it follows that $V _ { 1 } ^ { * } \stackrel { \cdot } { = } V ^ { * }$ 

Proof of Proposition 9. In the case of a monopolist seller, all nonzero states of a PPE satisfy

$$
V ^ {\prime} (x) = \max _ {s ^ {\prime} (x)} s ^ {\prime} (x) \widehat {w} _ {2} ^ {\prime} - c + \delta [ (1 - \alpha) V ^ {\prime} (x ^ {+} (x)) + \alpha V ^ {\prime} (x ^ {-} (x)) ],\tag{27}
$$

subject to the incentive compatibility constraints

$$
V ^ {\prime} (x ^ {+} (x)) - V ^ {\prime} (x ^ {-} (x)) \geq c / \delta (\beta - \alpha).\tag{28}
$$

In the case of competing sellers of different reputations, if $V ( x _ { k } \mid x _ { - k } ) > 0 ,$ , the corresponding equations are

$$
\begin{array}{l} V (x _ {k} \mid x _ {- k}) = \max _ {s (x _ {k} \mid x _ {- k})} s (x _ {k} \mid x _ {- k}) \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) - c \\ + \delta \sum_ {x _ {- k} ^ {\prime}} p (x _ {- k} ^ {\prime} \mid x _ {k}, x _ {- k}) [ (1 - \alpha) V (x ^ {+} (x _ {k}) \mid x _ {- k} ^ {\prime}) \\ + \alpha V (x ^ {-} (x _ {k}) \mid x _ {- k} ^ {\prime}) ], \end{array} \tag {29}\tag{29}
$$

$$
\sum_ {x _ {- k} ^ {\prime}} p (x _ {- k} ^ {\prime} \mid x _ {k}, x _ {- k}) [ V (x ^ {+} (x _ {k}) \mid x _ {- k} ^ {\prime}) - V (x ^ {-} (x _ {k}) \mid x _ {- k} ^ {\prime}) ]
$$

$$
\geq c / \delta (\beta - \alpha).\tag{30}
$$

Let $\pi ( x _ { - k } \mid x _ { k } )$ denote the conditional stationary probabilities that the profiles of other sellers will be in state $x _ { - k } ,$ From the definition of stationary probabilities of Markov chains, it is $\begin{array} { r } { \pi ( x _ { - k } ^ { \prime } \mid x _ { k } ) = \sum _ { x _ { - k } } p ( x _ { - k } ^ { ' } \mid x _ { k } , x _ { - k } ) \pi ( x _ { - k } \mid x _ { k } ) } \end{array}$ Finally, let

$$
E V (x _ {k}) = E _ {x _ {- k} | x _ {k}} [ V (x _ {k} \mid x _ {- k}) ] = \sum_ {x _ {- k}} \pi (x _ {- k} \mid x _ {k}) V (x _ {k} \mid x _ {- k}).
$$

Substituting into the above equations, we obtain

$$
\begin{array}{c} E V (x _ {k}) = \sum_ {x _ {- k}} \pi (x _ {- k} \mid x _ {k}) s (x _ {k} \mid x _ {- k}) \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) - c \\ + \delta [ (1 - \alpha) E V (x ^ {+} (x _ {k})) + \alpha E V (x ^ {-} (x _ {k})) ], \\ E V (x ^ {+} (x _ {k})) - E V (x ^ {-} (x _ {k})) \geq c / \delta (\beta - \alpha). \end{array}\tag{31}
$$

Comparing (27) and (28) with (31), we conclude that a symmetric PPE with seller payoffs $V ( x _ { k } \mid x _ { - k } )$ maps to a monopoly PPE with seller payoffs that satisfy $E V ( x _ { k } ) =$ $V ^ { \prime } ( x _ { k } )$ and, in addition,

$$
s ^ {\prime} (x _ {k}) \widehat {w} _ {2} ^ {\prime} = \sum_ {x _ {- k}} \pi (x _ {- k} \mid x _ {k}) s (x _ {k} \mid x _ {- k}) \widehat {w} _ {2} (x _ {k} \mid x _ {- k}) \quad \text { for   all } x _ {k}.\tag{32}
$$

Finally, if $\overline { { x } } _ { k }$ is a state where $s ^ { \prime } ( \overline { { x } } _ { k } ) = 1 .$ , Equation (32) can be rewritten simply as

$$
\widehat {w} _ {2} ^ {\prime} = \sum_ {x _ {- k}} \pi (x _ {- k} \mid \bar {x} _ {k}) s (\bar {x} _ {k} \mid x _ {- k}) \widehat {w} _ {2} (\bar {x} _ {k} \mid x _ {- k}). \quad \square
$$

Proof of Proposition 10. The result is a straightforward consequence of Corollary 2 of Dellarocas (2004). <sup></sup>

## References

Anderson, E. W. 1998. Customer satisfaction and word of mouth. J. Service 1(1) 5–17.

Blackwell, D. A. 1951. Comparison of experiments. Proc. 2nd Berkeley Sympos. Math. Statist. Probab., University of California Press, Berkeley, CA, 93–102.

Blackwell, D. 1953. Equivalent comparison of experiments. Ann. Math. Statist. 24 265–272.

Cabral, L., A. Hortacsu. 2004. The dynamics of seller reputation: Theory and evidence from eBay. Working Paper W10363, National Bureau of Economic Research. http://ssrn.com/ abstract=516704.

Dellarocas, C. 2003. The digitization of word-of-mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10) 1407–1424.

Dellarocas, C. 2004. Simultaneous auctions of imperfect substitute goods by sellers of different reputations. Working paper, University of Maryland, College Park, MD.

Dellarocas, C., M. Fan, C. Wood. 2003. Self-interest, reciprocity, and participation in online reputation systems. Workshop in Information Systems and Economics (WISE), Seattle, WA.

Dewatripont, M., I. Jewitt, J. Tirole. 1999. The economics of career concerns, part I: Comparing information structures. Rev. Econom. Stud. 66(1) 183–198.

Friedman, E., P. Resnick. 2001. The social cost of cheap pseudonyms. J. Econom. Management Strategy 10(1) 173–199.

Fudenberg, D., D. K. Levine. 1994. Efficiency and observability with long-run and short-run players. J. Econom. Theory 62 103–135.

Green, E. J., R. H. Porter. 1984. Noncooperative collusion under imperfect price information. Econometrica 52 87–100.

Greif, A. 1993. Contract enforceability and economic institutions in early trade: The Maghribi traders’ coalition. Amer. Econom. Rev. 83 525–548.

Kandori, M., H. Matsushima. 1998. Private observation, communication and collusion. Econometrica 66(3) 627–652.

Klein, B., K. Leffler. 1981. The role of market forces in assuring contractual performance. J. Political Econom. 89(4) 615–641.

Klein, D., ed. 1997. Reputation: Studies in the Voluntary Elicitation of Good Conduct. University of Michigan Press, Ann Arbor, MI.

Kuwabara, K. 2003. Decomposing reputation effects: Sanctioning or signaling? Working paper.

Milgrom, P. R., D. North, B. R. Weingast. 1990. The role of institutions in the revival of trade: The law merchant, private judges, and the champagne fairs. Econom. Politics 2 1–23.

Miller, N., P. Resnick, R. Zeckhauser. 2002. Eliciting honest feedback in electronic markets. Research Working Paper RWP02- 039, Harvard Kennedy School, MA.

Resnick, P., R. Zeckhauser. 2002. Trust among strangers in Internet transactions: Empirical analysis of eBay’s reputation system. Michael R. Baye, ed. The Economics of the Internet and E-Commerce. Advances in Applied Microeconomics, Vol. 11. JAI Press, Greenwich, CT.

Resnick, P., R. Zeckhauser, E. Friedman, K. Kuwabara. 2000. Reputation systems. Comm. ACM 43(12) 45–48.

Shapiro, C. 1983. Premiums for high quality products as returns to reputations. Quart. J. Econom. 98(4) 659–680.
