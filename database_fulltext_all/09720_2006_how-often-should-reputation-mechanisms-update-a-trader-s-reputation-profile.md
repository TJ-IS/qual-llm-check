---
otero_id: 9720
otero_key: "8E6UKSBZ"
title: "How Often Should Reputation Mechanisms Update a Trader's Reputation Profile?"
authors: "Chrysanthos Dellarocas"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1060.0092"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/8E6UKSBZ/fulltext/images/c0e7925e47995715f73dc076f3c7af56f5a24953d2b51ee07528856f13df5077.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# How Often Should Reputation Mechanisms Update a Trader's Reputation Profile?

Chrysanthos Dellarocas,

## To cite this article:

Chrysanthos Dellarocas, (2006) How Often Should Reputation Mechanisms Update a Trader's Reputation Profile?. Information Systems Research 17(3):271-285. http://dx.doi.org/10.1287/isre.1060.0092

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2006, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/8E6UKSBZ/fulltext/images/d14661eb39e86b6f2df876c07e16450614f48e6d71ea4dc387d696b393321753.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# How Often Should Reputation Mechanisms Update a Trader’s Reputation Profile?

Chrysanthos Dellarocas

4341 Van Munching Hall, R. H. Smith School of Business, University of Maryland, College Park, Maryland 20742, cdell@rhsmith.umd.edu

eputation mechanisms have become an important component of electronic markets, helping to build trust and elicit cooperation among loosely connected and geographically dispersed economic agents. Understand ing the impact of different reputation mechanism design parameters on the resulting market efficiency has thus emerged as a question of theoretical and practical interest. Along these lines, this note studies the impact of the frequency of reputation profile updates on cooperation and efficiency. The principal finding is that, in trading settings with pure moral hazard and noisy ratings, if the per-period profit margin of cooperating sellers is sufficiently high, a mechanism that does not publish every single rating it receives but rather only updates a trader’s public reputation profile every k transactions with a summary statistic of a trader’s most recent k ratings can induce higher average levels of cooperation and market efficiency than a mechanism that publishes all ratings as soon as they are posted. This paper derives expressions for calculating the optimal profile updating interval k, discusses the implications of this finding for existing systems, such as eBay, and proposes alternative reputation mechanism architectures that attain higher maximum efficiency than the, currently popular, reputation mechanisms that publish summaries of a trader’s recent ratings.

Key words: electronic markets; reputation mechanisms; game theory

History: Sanjeev Dewan, Senior Editor; Michael D. Smith, Associate Editor. This paper was received on February 23, 2005, and was with the author 2 <sup>3</sup> months for 1 revision.

## 1. Introduction

Reputation mechanisms have become an important component of electronic markets, helping to build trust and elicit cooperation among loosely connected and geographically dispersed economic agents (Resnick et al. 2000, Dellarocas 2003). A number of well-known electronic markets, such as eBay, eLance, and Amazon Auctions, currently use reputation mechanisms as the primary method for eliciting honest behavior, and thus for facilitating efficient transactions among strangers over the Internet (Resnick and Zeckhauser 2002).

A typical reputation mechanism encourages traders to post feedback (consisting of numerical ratings and, in some cases, optional text comments) describing their experiences with their trading partner on a given transaction. Posted feedback is aggregated by the system and published as part of a trader’s reputation profile. This profile is visible to all community members who might consider doing business with that trader in the future. In a well-designed mechanism, reputation profiles act as a deterrent that elicits honest behavior without the need to resort to the legal system: if traders believe that the consequences (partial or total loss of future business) of receiving negative feedback will be sufficiently severe, they will forego the temptation to cheat and will behave honestly toward their partners.

Information technology has added a large degree of flexibility to the design of reputation mechanisms. Online mechanism designers can control a number of parameters that are difficult to influence in offline settings. Examples of such parameters include the granularity of solicited feedback (eBay allows traders to rate a transaction as positive, negative, or neutral, Amazon Auctions supports integer ratings from 1 to 5, other systems support even higher levels of detail), the amount and type of information included in a trader’s reputation profile (most systems publish the sum or arithmetic mean of all posted ratings, some systems highlight recent ratings, other systems provide access to a trader’s entire ratings history) as well as the frequency with which reputation profiles are updated with new information (most current systems make all new ratings publicly available as soon as they are posted). These parameters impact the consequences of a trader’s current behavior on the community’s perception of him in the future, and thus his incentives to engage in honest behavior. It is, therefore, important and timely to examine the impact of such design choices on trader behavior and market efficiency.

Along these lines, this note considers the impact of the frequency of reputation profile updates on cooperation and efficiency. I develop the main arguments by analyzing a market where a single seller offers goods (products or services) to a population of buyers and each transaction can result in either a high- or lowquality good. The probability of a high-quality outcome depends on the effort (high/low) exerted by the seller. Such effort is costly to the seller and unobservable to the buyer. In such a setting, the role of a reputation mechanism is to induce the seller to cooperate (i.e., to exert high effort) as often as possible.

The principal, and rather striking, result is that, if the per-period profit margin of cooperating sellers is sufficiently high, it is possible to increase the average levels of seller cooperation and market efficiency by reducing the frequency of reputation profile updates. Specifically, I show that a reputation mechanism that does not publish every single rating it receives but rather only updates a trader’s public reputation profile every k transactions with a summary statistic of a trader’s k most recent ratings can induce higher average levels of cooperation, higher seller profits, and higher buyer surplus than a mechanism that publishes all ratings as soon as they are posted to the system.

The intuition behind this result is related to the noisy nature of online feedback. In most practical settings, online ratings are imprecise indicators of a seller’s true behavior. Even cooperating sellers might occasionally receive negative ratings, either because a buyer behaves irrationally, or because the transaction leaves a buyer dissatisfied for reasons beyond the seller’s control (for example, because shipped items were damaged in the mail). Empirical results (Ba and

Pavlou 2002, Bajari and Hortacsu 2003, Cabral and Hortacsu 2004, Dewan and Hsu 2004, Lucking-Reiley et al. 2006, Resnick and Zeckhauser 2002) as well as our formal analysis later on in the note, show that buyers punish sellers whose reputation profile contains negative ratings by placing lower bids. The incidence of unfair negative ratings thus hurts market efficiency for two reasons: (1) unfair punishment directly reduces average seller payoffs and (2) because sellers understand that, even if they cooperate, there is still a possibility that they might be punished, the difference in expected future profits that sellers obtain by cooperating versus by cheating declines. This, in turn, reduces their incentives to cooperate.

Elementary probability shows that accumulating a number of ratings before updating a seller’s profile and posting a negative rating only if all accumulated ratings are negative reduces the probability that cooperating sellers will be unfairly punished, and thus the efficiency losses because of noise. At the same time, however, increasing the updating interval allows a seller to cheat for several periods before news of his behavior becomes public knowledge. This increases a seller’s temptation to cheat. For reputation to remain an effective deterrent, the difference in expected future profits when the seller cooperates versus when the seller cheats must be high enough to offset his increased temptation to cheat. This implies that, as the frequency of profile updates decreases, the minimum per-period profit margin that makes reputation an effective deterrent must increase. The resulting trade-off imposes a limit into how many periods can elapse between profile updates: the optimal updating interval is the maximum number of periods for which a cooperating seller’s per-period profit margin remains sufficiently high to make reputation an effective deterrent.

This work contributes to the growing information systems literature on online reputation mechanisms. One stream of this literature conducts empirical and experimental studies of reputation mechanisms. A number of empirical studies have looked at the impact of a seller’s reputation on the probability of sale and auction closing prices on eBay (Ba and Pavlou 2002, Bajari and Hortacsu 2003, Cabral and Hortacsu 2004, Dewan and Hsu 2004, Lucking-Reiley et al. 2006, Resnick and Zeckhauser 2002). Other empirical studies have looked at the motivations for participation in reputation mechanisms (Dellarocas et al. 2003) and the relationship between a trader’s reputation and the probability of disputes (MacInnes et al. 2005). Experimental studies have looked at how the amount of information provided by a reputation mechanism affects cooperation (Keser 2003) and how cooperation levels induced by reputation mechanisms compare to those induced by stable partnerships (Bolton et al. 2004). Another stream of research focuses on analytical modeling of reputation mechanism design issues. The objective of that stream of research is to understand the limits of existing mechanisms and to propose improved architectures. Notable contributions include mechanisms for eliciting truthful feedback (Jurca and Faltings 2004, Miller et al. 2005), studies of the length of public history on the outcomes induced by a reputation mechanism (Dellarocas 2005, Fan et al. 2005), statistical techniques that reduce the impact of reputation mechanism manipulation (Dellarocas 2000), and distributed reputation mechanism architectures that do not require the presence of a trusted central repository of past ratings (Zacharia et al. 2000, Sen and Sajja 2002, Yu and Singh 2002). This paper falls within the stream of analytical reputation mechanism research. It is the first study that looks at the implications of the frequency of reputation profile updates on market efficiency.

The study of reputation mechanisms in settings with pure moral hazard has some similarities to the literature on sanctioning mechanisms in environments with imperfect monitoring. A common setting of such papers is an oligopoly cartel where firms collude (i.e., agree to restrict their individual production levels) but cannot directly observe the production levels of their competitors. Each firm is then tempted to increase its short-term profits by defecting from the agreed-upon production levels. Green and Porter (1984) show that, if the common price is a function of the sum of every firm’s production levels plus a random shock, firms can sustain collusion most of the time by reverting to price wars for a fixed number of periods if the common price falls below a critical level, irrespective of whether the price drop is due to somebody’s defection, or to noise. Other papers that analyze similar settings include Abreu et al. (1986), Fudenberg et al. (1994), and Tedeschi (1994). The mechanisms discussed in this paper are similar, in spirit, to the sanctioning mechanisms discussed in that literature, in that they sustain honest seller behavior most of the time by threatening to shift the seller to punishment states characterized by lower cooperation and lower profits, whenever the seller receives negative feedback. The contribution of this paper is the study of the implications of the frequency of information dissemination about the seller’s recent behavior, an aspect that has not been considered by any of the above-mentioned papers.

The rest of this paper is organized as follows. Section 2 introduces the model. Section 3 shows that the upper bounds of the seller payoff and buyer surplus that can be induced through the use of any reputation mechanism are monotonically increasing functions of the profile updating interval. It then discusses three concrete mechanism architectures that attain maximum payoffs equal to these bounds. Finally, §4 concludes and points to avenues for future research.

## 2. The Model

## 2.1. The Setting

The setting that forms the focus of this work involves a marketplace where, in each period, a monopolist long-run seller provides one unit of a product or a service (good) to one of multiple short-run buyers. Following receipt of payment, the seller can exert either high effort (cooperate) or low effort (cheat). The seller’s action affects the probability distribution of the good’s quality, and thus, its expected value to a buyer. The buyer observes the quality of the good delivered, but not the effort exerted by the seller. Moral hazard is introduced because high effort is costlier to the seller who can reduce his costs by failing to exert high effort, providing the buyer with a good of lower expected value.

More formally, I analyze a setting with a monopolist seller who each period offers for sale a single unit of a good to m buyers. Buyer j has expected valuation $w _ { j }$ for a good produced by a cooperating seller. The expected valuation of a good produced by a cheating seller is normalized to zero for all buyers. Under these assumptions the seller will not attract any buyers unless he can credibly promise to cooperate with positive probability. Buyer lifetime is exactly one period, and in each period, the m buyers are drawn from the same probability distribution; thus buyer valuations are independent and identically distributed within and across periods. There are an infinite number of periods, and the seller has a period discount factor  reflecting the time value of money, or the probability that the game will end after each period. Seller effort costs c if the seller cooperates. The cost of low effort is normalized to zero. The distribution of buyer valuations and the seller’s cost of effort are public knowledge.

In each period, a mechanism is used to allocate the good among the m buyers by determining the buyer who receives the good and the price she pays to the seller. Without loss of generality, we assume that buyers are indexed according to their valuations $( w _ { 1 } \ge$ $w _ { 2 } \geq \cdots \geq w _ { m } )$ . Furthermore, we assume that a second price Vickrey auction is used to award the good to the highest bidder. The winning bidder pays a price equal to the second highest bid.

In the above setting, the seller’s objective is to maximize the present value of his payoffs over the entire span of the game, while the buyers’ objective is to maximize their short-term (stage-game) payoff. It is easy to see that, in the absence of a sanctioning mechanism that induces seller effort (such as the legal system or a reputation mechanism), the only Nash equilibrium is one where the seller will always cheat. Knowing this and assuming that bids are binding, no buyer will post a positive bid, and thus no trade will ever occur.

My model attempts to capture the essential properties of markets with pure moral hazard. In such markets, there is no uncertainty regarding the seller’s type (adverse selection); cooperation is primarily compromised by postcontractual opportunism (moral hazard). Specifically, a key assumption of the model is that there is one type of seller whose parameters (cost of effort, probability of high and low outcomes given effort) are common knowledge. Whereas the use of the term seller effort in the model specification points to markets for services, if one thinks of seller effort as describing the wholesale price paid for an item by an online trader (or the opportunity cost of parting with an item that exists in the seller’s inventory), the model can also be used to describe certain auction-based retail product markets such as eBay. In such markets, it is plausible to assume that all sellers are equally capable of successfully fulfilling a transaction.<sup>1</sup> If we can also assume that sellers are rational (e.g., that there are no irrational sellers who always cheat or who always cooperate), then it is reasonable to assume that there exists no uncertainty about a seller’s type; the primary uncertainty is whether the seller will behave honestly (by sending the promised item) or not (by sending an item of inferior quality, or nothing).

## 2.2. Reputation Mechanisms

A reputation mechanism allows each period’s buyer to report her satisfaction with the transaction to a central authority (the center). I assume that the mechanism allows the current buyer to submit one out of a finite set of possible reports $r \in \{ R _ { i } \mid i = 1 , \ldots , m \} .$ , where reports indexed by a higher i indicate higher levels of buyer satisfaction.<sup>2</sup> Buyer reports are connected to seller actions through a commonly known conditional probability distribution prepor t <sub></sub> action that specifies the probability of a given type of report given the seller’s (hidden) action. I assume that the conditional distribution p<sub>·  ·</sub> is exogenously given and depends on the set of reports supported by the mechanism and the properties of the trader population. The center aggregates all past reports and publishes a reputation profile for the seller at the beginning of each period. The reputation profile can be the unabridged history of past reports or any (commonly known) function of that history.

The above specification implicitly assumes that, although buyers might make mistakes when reporting their satisfaction, they are not acting strategically: the conditional distribution of ratings given a seller’s action is, thus, independent of the seller’s current profile or the history of play. From a theoretical perspective, this can be weakly justified if we make the assumption that buyers only transact with a given seller once (a reasonable assumption in some largescale electronic markets). Buyers are then indifferent between truthful reporting and untruthful reporting. Moreover, it is possible to devise a side payment mechanism that provides buyers with strict incentives for truthtelling (Jurca and Faltings 2004, Miller et al. 2005). Such a mechanism can be easily combined with the mechanisms I present in this note.

Table 1 Stage Game of Repeated Bilateral Exchange Game Studied in This Work

<table><tr><td>Step</td><td>Procedure</td></tr><tr><td>1.</td><td>The seller offers a single unit of a good, promising to exert high effort (as there is no demand for low effort).</td></tr><tr><td>2.</td><td>The center publishes the seller&#x27;s current reputation profile x.</td></tr><tr><td>3.</td><td>Buyers bid their expected valuations for the good in a second price Vickrey auction; the winning bidder pays the second highest bid.</td></tr><tr><td>4.</td><td>The seller decides whether to exert high effort at cost c, or low effort at cost 0.</td></tr><tr><td>5.</td><td>The buyer receives the good, experiences its quality, and reports on the quality of the good received to the center. The center updates the reputation profile of the seller accordingly.</td></tr></table>

Table 1 summarizes the stage game that results from integrating a reputation mechanism into the bilateral exchange game that forms the focus of this work.

## 2.3. Equilibrium Concepts

The objective of reputation mechanisms in settings with pure moral hazard is to induce (at least partial) seller cooperation, and thus to facilitate profitable trade despite the seller’s short-term temptation to cheat. They accomplish this objective by inducing equilibria where the presence of negative ratings in a seller’s profile shifts the seller to states of lower expected profitability. In such states, buyers (correctly at equilibrium) expect the seller to exert lower effort, and thus place lower bids. If the present value of profit losses that are associated with negative ratings is equal to or higher than the short-term gains from cheating the seller has an incentive to avoid getting negative ratings by exerting high effort.

Reputation mechanisms typically induce multiple equilibria. Their analysis has thus traditionally focused on deriving upper and/or lower bounds on equilibrium payoffs that can be induced by such mechanisms (see, for example, Fudenberg and Levine 1992, Cripps and Thomas 1995, Cripps et al. 1996).

Likewise, my objective is to explore how the maximum equilibrium payoffs that can be induced by a given reputation mechanism depend on the mechanism’s profile updating interval. I restrict my analysis to the subclass of binary reputation mechanisms; that is, to mechanisms where buyers can only report the outcome of a transaction as either positive (satisfactory) or negative (unsatisfactory).<sup>3</sup> I assume that both types of reports can occur with positive probability following both seller actions. This assumption intends to capture the idea that, even when a seller cooperates, it is still possible that he may get an occasional negative rating because of factors beyond his control (e.g., a shipped item was lost or damaged in the mail, the buyer misunderstood what the seller actually promised to deliver, etc.). Likewise, even when a seller cheats (e.g., sends a fake item), it is still possible that some buyers may end up satisfied (or might not notice the fraud before posting feedback), and thus that he may get an occasional positive rating. Specifically, I assume the following information structure:<sup>4</sup>

$$
\begin{array}{c c} p (+ \mid c o o p) = 1 - \alpha & p (- \mid c o o p) = \alpha \\ p (+ \mid c h e a t) = 1 - \beta & p (- \mid c h e a t) = \beta \\ & 0 <   \alpha <   \beta <   1, \end{array}\tag{1}
$$

where <sub>+</sub>, <sub>−</sub> indicate a positive and negative report, respectively.

The solution concept that I use in the subsequent analysis is the perfect public equilibrium (PPE) (Fudenberg and Levine 1994). A strategy for a longrun player is public if at each period it depends only on the publicly known information and not on any private information of that player. A PPE is a profile of public strategies such that, at every period and for every public history, these strategies are a Nash equilibrium from that date onward.

Consider a reputation mechanism that updates the seller’s reputation profile x every k periods $( k \geq 1 )$

Let $s ( x , i ) \in [ 0 , 1 ]$ denote the seller’s public strategy, equal to the probability that the seller will cooperate $( \mathrm { i . e . , }$ exert high effort) following receipt of payment if his public profile at the beginning of the current period is equal to x and $0 \leq i < k$ periods have elapsed since the most recent profile update (i is public knowledge). Given their beliefs about the seller’s strategy $s ( x , i )$ , short-term buyers simply play the corresponding stage-game static best response. Because they compete with each other on a Vickrey auction, each buyer’s optimal action in each period is to bid an amount equal to her expected valuation $G _ { j } ( x , i ) = s ( x , i ) w _ { j } ,$ resulting in expected auction revenue for that period $G ( x , i ) = s ( x , i ) \widehat { w } _ { 2 } .$ , where $\widehat { w } _ { 2 }$ is the expected value of the second highest bidder’s valuation of a cooperating seller’s output. The seller’s corresponding expected current period payoff is $u _ { s } ( x , i ) = G ( x , i ) - s ( x , i ) c = s ( x , i ) ( \widehat { w } _ { 2 } - c )$ . The ex ante expected surplus for the winning bidder is $u _ { b } ( x , i ) = s ( x , i ) ( \widehat { w } _ { 1 } - \widehat { w } _ { 2 } )$ , where $\widehat { w } _ { 1 }$ is the expected value of the highest bidder’s valuation of a cooperating seller’s output. Finally, the expected total surplus generated in the current period is equal to $u ( x , i ) =$ $u _ { b } ( x , i ) + u _ { s } ( x , i ) = s ( x , i ) ( \widehat { w } _ { 1 } - c )$

The seller will enter the market if and only if $\widehat { w } _ { 2 } \geq c .$ Observe that, if $\widehat { w } _ { 2 } \geq c ,$ both seller profits and buyer surplus are proportional to sx i: higher levels of seller cooperation benefit all players. Therefore, a public strategy that maximizes the seller’s payoff also maximizes buyer surplus, and thus social surplus (market efficiency). For that reason, in the rest of the note, we can focus without loss of generality on finding reputation mechanism designs and seller strategies that maximize the seller’s lifetime discounted payoff. For the same reason, I will be using the terms seller payoffs and efficiency interchangeably.

Throughout this paper, I am implicitly assuming that the reputation mechanism operator (the center) is a benevolent social planner whose objective is to maximize social welfare. In most real-life settings (e.g., eBay), the mechanism operator is a private for-profit entity that charges sellers and/or buyers a percentage of the price paid for each transaction. Given that higher cooperation results in higher expected auction revenue, a mechanism that maximizes social efficiency also maximizes the operator’s profits. Even in a for-profit scenario, the operator thus has an incentive to design a reputation mechanism that maximizes the seller’s average probability of cooperation.

## 2.4. Baseline Case

The baseline case is one where the reputation mechanism updates the seller’s public profile in every period with the latest rating posted by the most recent buyer (i.e., where $k = 1 )$ . This case corresponds to the current practice of most online reputation mechanisms and has been studied by Dellarocas (2005). It is instructive to review the essence of his results here. Let $\rho = \widehat { w } _ { 2 } / c ; \rho$ is a measure of the expected stage-game profit margin of a fully cooperating seller (strictly speaking, the profit margin is equal to $1 0 0 \times$ $( \rho - 1 ) )$ . Dellarocas (2005) shows that the set of PPE payoffs of a repeated game where the stagegame structure is described in Table 1, the reputation mechanism has information structure (1), and the entire history of past reports is available to buyers is bounded above by

$$
\begin{array}{l l} V ^ {*} = \frac {1}{1 - \delta} \left(\widehat {w} _ {2} - c - \frac {\alpha c}{\beta - \alpha}\right) & \text { if } \rho \geq \left(\beta + \frac {1 - \delta}{\delta}\right) / (\beta - \alpha) \\ V ^ {*} = 0 & \text { if } \rho <   \left(\beta + \frac {1 - \delta}{\delta}\right) / (\beta - \alpha). \end{array} \tag {2}\tag{2}
$$

Because all PPE that can be induced by reputation mechanisms that publish arbitrary (but commonly known) functions of the seller’s history of past reports can also be induced by a mechanism that publishes the seller’s entire history of past reports (because buyers can individually compute the relevant function and condition their actions on that function), the above equations express the maximum payoffs that can be induced by any reputation mechanism when k 1.

Two observations are particularly noteworthy: First, the maximum PPE seller payoff that can be induced through the use of a reputation mechanism is strictly lower than the first-best payoff $V _ { f i r s t b e s t } = ( \widehat { w } _ { 2 } - c ) / ( 1 -$  that can be achieved in a (hypothetical) setting where a seller could credibly precommit to full cooperation. This efficiency loss is because of the fact that reputation mechanisms induce seller effort by threatening to shift the seller to states of lower profitability whenever negative outcomes occur. In such states, buyers (correctly) expect the seller to exert lower effort, and thus place lower bids. Our model assumes that, because of noise, even a fully cooperating seller will receive negative ratings with positive probability . Therefore, such lower profitability states will be reached with virtual certainty, reducing the seller’s expected lifetime payoff (and also reducing buyer surplus and social efficiency). The average per-period efficiency loss is equal to the probability of receiving an unfair negative rating times the present value of future losses associated with a negative rating.

Second, the maximum payoff obtains only when the expected per-period profit margin of a cooperating seller ( ) is above a threshold. The intuition behind this result is based on the observation that the maximum punishment that a reputation mechanism can impose to a seller is total exclusion from the market (and thus, loss of future profits). For reputation to induce cooperation, the seller’s profit margin must be high enough so that the present value of future profits obtained through cooperation (that the seller jeopardizes if he cheats) is sufficiently high to offset the short-term gains from cheating. The lower the minimum effective profit margin, the wider the range of settings where the mechanism can induce maximum efficiency. In settings where the actual profit margin of cooperating sellers is below the minimum, reputation mechanisms fail to induce any cooperation.

The basic conclusion of the preceding discussion is that, to increase efficiency, reputation mechanisms must find ways to minimize the probability of unfair punishment of cooperating sellers without substantially increasing the present value of the gains from cheating. The following section shows that, under certain conditions, both objectives can be accomplished by reducing the frequency of reputation profile updates.

## 3. Increasing Efficiency by Reducing the Frequency of Reputation Profile Updates

This section shows that the minimum efficiency loss and, in some cases, the minimum effective profit margin of a reputation mechanism can be decreased by reducing the frequency with which a trader’s reputation profile is updated with newly posted ratings. The remarkable conclusion is that publishing less current information about a trader’s recent behavior can sometimes induce higher levels of cooperation and market efficiency.

## 3.1. Two-State Randomization Mechanisms with Infrequent Updating

I introduce the main ideas by analyzing a simple but effective reputation mechanism architecture called a two-state randomization mechanism with k-period updating interval (k-2SRM). A k-2SRM is characterized by a binary reputation profile that each period can be either in the good state or in the bad state. Sellers always start the game from the good state. Every k periods, the mechanism updates the seller’s profile according to the following rule: If fewer than l of the ratings received in the most recent k periods $( 1 \leq l \leq$ k are negative, then the center keeps the seller’s profile in the good state. Otherwise, the center changes the seller’s profile to bad with punishment probability $\pi _ { k } .$ Once the seller’s profile becomes bad, it stays bad permanently.

In the baseline case where $k = 1 .$ , Dellarocas (2005) has shown that, if $\rho$ is sufficiently high, there exists a punishment probability $0 < \pi _ { 1 } \leq 1$ for which we can construct a PPE with the following properties: (i) the seller always cooperates as long as his profile is good, (ii) the seller always cheats (effectively placing himself out of the market) when his profile turns bad, and (iii) the seller’s lifetime discounted payoff is equal to the maximum payoff $V ^ { * }$ of Equation (2). The following proposition extends this result and characterizes some of the equilibria that can be induced by a k-2SRM for arbitrary updating intervals k.

Proposition 1.<sup>5</sup> The following statements characterize the PPE induced by a k-2SRM:

(1) A profile updating rule that induces maximum efficiency is one where $l = k \colon$ at the end of each k-period block the center keeps the seller’s profile in the good state as long as he has received at least one good rating in that block; the center changes the seller’s profile to bad with probability $\pi _ { k }$ if and only if all k ratings are negative.

(2) Let

$$
\rho_ {k} ^ {2 S R M} = 1 + (1 - \delta) \bigg [ \frac {1}{1 - \delta^ {k}} + (\alpha \delta) ^ {- k} \bigg ] \frac {\alpha}{\beta - \alpha}
$$

<sup>5</sup> All proofs are contained in an online appendix to this paper that is available on the Information Systems Research website (http://isr. pubs.informs.org/ecompanion.html).

If $\rho \geq \rho _ { k } ^ { 2 S R M }$ , then there exists an equilibrium where a k-2SRM with $l = k$ and punishment probability

$$
\pi_ {k} ^ {*} = \frac {1 - \delta}{\alpha^ {k - 1} \delta^ {k} \left[ \alpha \delta \frac {1 - \delta^ {k - 1}}{1 - \delta^ {k}} + \rho (\beta - \alpha) - \beta \right]}\tag{3}
$$

induces the seller to cooperate as long as his profile remains in the good state and to cheat as soon as his profile transitions to the bad state. The present value of the seller’s discounted lifetime payoff during periods when his profile is in the good state is equal to

$$
V _ {k} ^ {*} = \frac {\widehat {w} _ {2} - c}{1 - \delta} - \frac {1}{1 - \delta^ {k}} \frac {\alpha c}{\beta - \alpha}.\tag{4}
$$

(3) Let

$$
\rho_ {k, i} ^ {2 S R M} = 1 + (1 - \delta) \frac {\alpha}{\beta - \alpha} \frac {\delta^ {i}}{\delta^ {i} - \delta^ {k}} \left(1 + \alpha^ {i} \frac {1 - \delta^ {k}}{(\alpha \delta) ^ {k}}\right).
$$

If $\rho \ge \rho _ { k , i } ^ { 2 S R M }$ for some integer $0 \leq i \leq k - 1$ , then there exists an equilibrium where a k-2SRM with $l = k$ and

$$
\pi_ {k, i} ^ {*} = c \bigg / \left(\delta^ {k - i} (\beta - \alpha) \alpha^ {k - i - 1} \left(\frac {\delta^ {i} - \delta^ {k}}{1 - \delta^ {k}} \frac {\widehat {w} _ {2} - c}{1 - \delta} \right. \right.
$$

$$
- \left. \delta^ {i} \frac {\alpha c}{(1 - \delta^ {k}) (\beta - \alpha)}\right)\tag{5}
$$

induces the seller to (i) cheat in the first i periods and to cooperate in the remaining $k - i$ periods of each period block when his profile is in the good state and (ii) always cheat as soon as his profile transitions to the bad state. The present value of the seller’s discounted lifetime payoff at the beginning of blocks when his profile is in the good state is equal to

$$
V _ {k, i} ^ {*} = \frac {\delta^ {i} - \delta^ {k}}{1 - \delta^ {k}} \frac {\widehat {w} _ {2} - c}{1 - \delta} - \delta^ {i} \frac {\alpha c}{(1 - \delta^ {k}) (\beta - \alpha)}.\tag{6}
$$

(4) If $\rho < \rho _ { k , i } ^ { 2 S R M }$ for all integers $0 \leq i \leq k - 1$ , then the only equilibrium is one where the seller always cheats and $V _ { k } ^ { * } = 0$

(5) If $\rho \geq \rho _ { k , i } ^ { 2 S R M }$ for $i \in I \subseteq \{ 0 , \ldots , k - 1 \}$ , then the seller’s discounted lifetime payoff $V _ { k , i } ^ { * }$ is a monotonically decreasing function of the degree of partial cheating $i \in I$ and attains its maximum value for $i _ { 0 } = \operatorname* { m i n } \{ i \in I \}$ . To maximize efficiency, the center should therefore choose the $\pi _ { k , } ^ { * }$ i that corresponds to the minimum i for which $\rho \ge \rho _ { k , i } ^ { 2 S R M }$

Proposition 1 implies that, if the profit margin of a cooperating seller is sufficiently high, a k-2SRM can induce at least partial seller cooperation in the unsanctioned state. Furthermore, if the profit margin is high enough to sustain full cooperation in the unsanctioned state (i.e., if $\rho \ge \rho _ { k , 0 } ^ { 2 S R M } )$ , the full cooperation equilibrium induces higher efficiency than any feasible partial cooperation equilibrium.

Note that Proposition 1 only establishes existence of a specific set of equilibria. In the baseline case where $k = 1$ , it has been shown (Dellarocas 2005) that these equilibria attain the maximum payoffs that can be induced in this setting through the use of any reputation mechanism. The following proposition shows that this property holds for all $k \geq 1$

Proposition 2. The set of PPE seller payoffs of a repeated game, where (i) the stage-game structure is described in Table 1, (ii) the reputation mechanism has information structure (1), (iii) the center updates a seller’s public profile every k periods using the following updating rule: if all ratings received in the last k periods are negative, then declare the outcome of the last k-period block as negative; otherwise, declare the outcome of the last kperiod block as positive, and (iv) the entire history of past k-period outcomes is available to buyers, is bounded above by

$$
V _ {k} ^ {*} = \frac {\delta^ {i _ {0}} - \delta^ {k}}{1 - \delta^ {k}} \frac {\widehat {w} _ {2} - c}{1 - \delta} - \delta^ {i _ {0}} \frac {\alpha c}{(1 - \delta^ {k}) (\beta - \alpha)},\tag{7}
$$

where $i _ { 0 } = \operatorname* { m i n } \{ i \in \{ 0 , \dots , k - 1 \} \mid \rho \geq \rho _ { k , i } ^ { 2 S R M } \} .$ . If $\rho <$ $\rho _ { k , i } ^ { 2 S R M }$ for all integers $0 \leq i \leq k - 1$ , then $V _ { k } ^ { * } = 0$

Comparing Equations (6) and (7) and noticing that, for $i = \stackrel { \bullet } { 0 } , \rho _ { k , 0 } ^ { 2 S R M } = \rho _ { k } ^ { 2 S R M }$ and Equations (5) and (6) reduce to (3) and (4), respectively, produces the following result:

Corollary 1. The equilibria of Proposition 1 attain the maximum efficiency that can be induced through the use of any reputation mechanism.

In the rest of the section, I will focus my attention on settings where full cooperation equilibria are sustainable (i.e., where $\rho \ge \rho _ { k , 0 } ^ { \mathrm { m i n } } \equiv \rho _ { k } ^ { \mathrm { m i n } } )$ . Observe that, for $k \geq 1 , 1 / ( 1 - \delta ^ { k } )$ is a monotonically decreasing function of k. It follows from (4) and (7) that $V _ { k } ^ { * }$ monotonically increases with k. One of the main results of this work immediately follows:

Corollary 2. In settings with pure moral hazard and for sufficiently high per-period profit margins of cooperating sellers $( \rho )$ , the maximum efficiency that is attainable through the use of any reputation mechanism is a monotonically increasing function of the seller’s profile updating interval k.

Figure 1 Maximum Seller Payoff Attainable Through the Use of Any Reputation Mechanism as a Function of the Profile Updating Interval $\mathrm { ~  ~ { ~ \langle ~ } ~ } ( \alpha = 0 . 1 , \beta = 0 . 9 , \delta = 0 . 9 9 , \widehat { W } _ { 2 } = 2 , c = 1 )$  
![](/api/attachments/8E6UKSBZ/fulltext/images/c28ed30a674d7ba2ecc646a84f8103f71bdb328cec39397c4c83888329fe3159.jpg)  
Note. The hypothetical first-best seller payoff $V _ { \mathit { t i r s t b e s t } } ^ { * } = ( \widehat { W } _ { 2 } - c ) / ( 1 - \delta )$ is also plotted for comparison.

Figure 1 plots $V _ { k } ^ { * }$ as a function of k for a representative set of parameter values. Remarkably, less $f r e \mathrm { - }$ quent publication of new information regarding the seller’s recent behavior increases seller payoffs (and thus market efficiency). To understand the intuition behind this result, recall from §2.4 that the source of inefficiency in environments with noisy feedback is the fact that even cooperating sellers will occasionally receive unfair negative ratings and will, therefore, be punished with positive probability. Increasing the profile updating interval to k periods and (probabilistically) punishing the seller only if he receives negative ratings in all k periods reduces the probability of unfair negative outcomes from  to $\hat { \alpha ^ { k } }$ , and thus reduces the mechanism’s efficiency loss because of noise. This observation also helps explain why the most lenient profile updating rule (forgive the seller if he obtains at least one positive rating in a k-period block and only consider punishment if all k ratings are negative) is also the most efficient one.

The updating interval k cannot be increased indefinitely. The longer the interval between profile updates, the higher the present value of the profit $\textstyle \sum _ { i = 0 } ^ { \cdot } \delta ^ { i } c = ( ( 1 - { \overset { \sim } { \delta } } ^ { k } ) / ( 1 - \delta ) ) c$ that a cheating seller can realize before information about his behavior becomes public (and the farther away the adverse consequences of such information). To induce the seller to cooperate, the difference between the expected present value of punishment associated with cheating versus the corresponding value associated with cooperation must be increased accordingly. Because punishment for cheating consists of expelling the seller from the market with probability $\pi _ { k }$ , the maximum possible punishment value is equal to the present value of future profits from cooperation. This, in turn, is a function of the seller’s stage-game profit margin from cooperation $\rho = \widehat { w } _ { 2 } / c$ . One therefore expects that, the longer the interval k between profile updates, the higher the minimum profit margin that is required to sustain incentives for cooperation. This imposes a limit on how much k can be increased. The optimal k is the highest integer for which the per-period profit margin of cooperating sellers $( \rho )$ is greater than or equal to the minimum profit margin that is required to sustain incentives for cooperation through the use of the reputation mechanism of interest. For example, in the context of k-2SRM, the following corollary is an immediate consequence of the preceding discussion and Proposition 1:

Corollary 3. The profile updating interval that maximizes the efficiency attainable by a k-2SRM is the highest integer k for which $\rho \ge \rho _ { k } ^ { 2 S R M }$

The relationship between the minimum effective profit margin $\rho _ { k } ^ { 2 S R \bar { M } } = 1 + ( 1 - \delta ) [ 1 / ( 1 - \delta ^ { k } ) + ( \alpha \delta ) ^ { - k } ] \alpha /$ $( \beta - \alpha )$ that is needed to sustain cooperation in a k-2SRM and the reputation mechanism’s updating interval k depends on the properties of the function $f ( k ) = 1 / ( 1 - \delta ^ { k } ) + ( \alpha \delta ) ^ { - k }$ . It is easy to show that lim $\mathfrak { r } _ { k \to \infty } f ( k ) = \infty$ . As expected, as the updating interval k grows, the minimum profit margin that is required to sustain cooperation goes to infinity. Furthermore, $\textstyle \operatorname* { l i m } _ { k \to 0 + } f ( k ) = \infty$ $\begin{array} { r } { \operatorname* { l i m } _ { k \to 0 + } f ^ { \prime } ( k ) = - \infty , } \end{array}$ , and $f ^ { \prime \prime } ( k ) \geq 0$ for all $k \geq 0$ . Therefore, $f ( k )$ has a minimum at $k ^ { * } > 0$ . This, in turn, implies that there exists a region $[ 0 , k ^ { * } ]$ where the minimum effective profit margin $\rho _ { k } ^ { 2 S R M }$ declines as the updating interval k grows. From the first-order condition, $k ^ { * }$ must solve

$$
\left. \frac {\partial f (k)}{\partial k} \right| _ {k = k ^ {*}} = 0, \quad \text { which   is   equivalent   to }
$$

$$
\alpha^ {k ^ {*}} \left(\frac {\delta^ {k ^ {*}}}{1 - \delta^ {k ^ {*}}}\right) ^ {2} = 1 + \frac {\log \alpha}{\log \delta}.\tag{8}
$$

Figure 2 Minimum Profit Margin $\rho _ { k } ^ { 2 S R M }$ Required for Attaining Maximum Efficiency Through the Use of a k 2SRM as a Function of the Updating Interval k  099  
![](/api/attachments/8E6UKSBZ/fulltext/images/298b96c7b6eb93ca821924c894676f1d958feae5d582e6145323b5a21acc0e70.jpg)  
Some algebraic manipulation reveals that $\partial k ^ { * } / \partial \alpha >$ 0 and $\partial k ^ { * } / \partial \delta > 0$ . The value of $k ^ { * }$ that minimizes the profit margin requirement is, thus, higher in settings where ratings are noisy ( is large) and/or where sellers have long-term horizons and transact frequently ( is close to 1). Figure 2 plots $\rho _ { k } ^ { 2 S R M }$ for some representative parameter pairs. Remarkably, there exist parameter ranges where increasing the updating interval k above 1 both increases efficiency (by Corollary 2) and decreases the minimum profit margin that is needed for the reputation mechanism to be effective (and thus increases the applicability of the mechanism in a wider range of markets). The intuition behind this result is that, in settings where ratings are noisy or where sellers do not discount the future very much, increasing k above 1 decreases the mechanism efficiency loss (and thus increases the expected present value of future gains from cooperation that the seller jeopardizes by cheating) by an amount that is higher than the corresponding increase in the present gains from cheating. The net effect is to lower the minimum profit margin above which the threat of expulsion from the market becomes an effective deterrent.

## 3.2. Infrequent Updating of eBay-Like Mechanisms

The preceding analysis shows that k-2SRM constitute an optimal reputation mechanism architecture in settings with pure moral hazard. Nevertheless, the practical implementation of such mechanisms in online markets faces several challenges. First, in settings with noise, cooperating sellers will eventually be expelled from a k-2SRM market with positive probability. Even though, in theory, this property does not make risk-neutral sellers worse off relative to any other reputation-mediated market (in terms of their ex ante average discounted lifetime payoff), the psychological impact of irreversible unfair punishment may deter sellers from joining such markets. Second, and perhaps more important, k-2SRM break down in settings where sellers can easily change identities. Easy identity changes constitute an important concern in many online settings (Friedman and Resnick 2001). If sellers can disappear and reenter the market with a new identity as soon as their profile transitions into the bad state, they have no incentive to avoid negative ratings. Therefore, sellers will always cheat, buyers will expect them to do so, and no trade will ever occur irrespective of the value of $\rho .$

Most existing reputation mechanisms prominently publish summary statistics of a trader’s recent ratings. For example, the most visually prominent component of eBay’s feedback mechanism is a table that lists the sum of positive, negative, and neutral ratings received by a trader during the most recent 12-month period. In addition to being fairer to cooperating sellers (unfair negative ratings because of noise will eventually be erased from a seller’s profile and thus will only affect his profits for a finite number of periods), eBay-like mechanisms are better able to cope with easy identity changes. Specifically, in settings where traders can easily change identities, eBay-like mechanisms can still elicit cooperation if the center initializes the reputation profile of new sellers at the lowest payoff state $( \mathrm { i . e . , }$ if new sellers start the game with a profile that is seemingly full of negative ratings). Traders then have to pay their dues before they clean their name and transition to states of higher payoffs. Because traders understand that if they change their identity, they will have to pay their dues again, this approach deters them from doing so (Dellarocas 2005).<sup>6</sup>

This section studies the impact of infrequent updating on eBay-like mechanisms. Consider the following perturbation of the eBay-like mechanism presented in Dellarocas (2005): Instead of publishing the sum of positive and negative ratings posted for the seller in the N most recent transactions, the mechanism updates the seller’s profile only once every k periods and publishes the sum of outcomes of the N most recent k-period blocks. A block outcome is considered positive if the seller has received at least one positive rating in the k periods that comprise that block and negative if the seller has received no positive ratings in these k periods. In the rest of this paper, I will refer to this mechanism as a k-eBay-like mechanism.

The following proposition shows that, if is high enough, there exist PPE where the efficiency induced through the use of a k-eBay-like mechanism increases with the updating interval k.

Proposition 3. Consider a repeated game whose stagegame structure is described in Table 1 and a k-eBay-like mechanism with information structure (1). At the beginning of each period, the mechanism publishes the sum of negative outcomes in the N most recent completed k-period blocks. An outcome is considered negative if and only if all k ratings within its associated k-period block are negative. Let N

$$
\rho_ {k} ^ {E B A Y} = \frac {N}{\alpha^ {k - 1} (\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i k}}.
$$

The following statements are true:

(1) If $\rho \ge \rho _ { k } ^ { E B A Y }$ , then there exists a PPE where

(a) the seller cooperates with probability one during all periods of a k-period block except the first one; the seller’s probability of cooperation during the first period of each block is a decreasing linear function of the current number z of negative ratings in his profile

$$
\begin{array}{c} S (z, i) = \left\{ \begin{array}{l l} 1 - z \theta & \text {if} i = 0 \\ 1 & \text {if} i > 0 \end{array} \right., \\ w h e r e \theta = \frac {c}{\alpha^ {k - 1} (\beta - \alpha) \sum_ {i = 1} ^ {N} \delta^ {i k} \widehat {w} _ {2}} \end{array}
$$

(b) the present value of the seller’s discounted lifetime payoff is maximized during periods when the seller has no negative ratings in his profile; it is then equal to

$$
V _ {k} ^ {*} = \frac {\widehat {w} _ {2} - c}{1 - \delta} - \frac {1}{1 - \delta^ {k}} \frac {\alpha c}{\beta - \alpha}.
$$

(2) If $\rho < \rho _ { k } ^ { E B A Y }$ , then all PPE achieve seller payoffs strictly below $V _ { k } ^ { * }$ .

Proposition 3 shows that reducing the updating frequency of eBay-like reputation profiles increases the maximum efficiency. The intuition is similar to that behind Proposition 1: evaluating a seller on the basis of multiple transaction outcomes reduces the probability that cooperating sellers will be unfairly punished, and thus the probability that they will spuriously transition to states of lower average cooperation. At the same time, less frequent profile updating increases the seller’s temptation to cheat, and thus requires higher per-period profit margins to make the threat of reduced future profits an effective deterrent to cheating.

A comparison of Propositions 1 and 3 reveals that, although the maximum PPE payoffs that can be induced through the use of k-2SRM and k-eBay-like mechanisms are identical, the minimum per-period profit margin of cooperating sellers that is required to attain these payoffs is always substantially higher in the case of k-eBay-like mechanisms. From the expression of $\rho _ { k } ^ { E B A Y }$ , it is easy to see that each unit increases in k multiplies $\rho _ { k } ^ { E B A Y }$ by a factor of $1 / ( \alpha \delta ^ { i } )$ . On the other hand, Figure 2 shows that, for small k, increases in k have a much less dramatic impact on $\rho _ { k } ^ { 2 S R M }$

The reason behind the difference is that k-eBay-like mechanisms offer less flexibility in punishing sellers who receive negative ratings. To see why, consider the simplest possible k-eBay-like mechanism: a mechanism that only publishes a seller’s single most recent k-period outcome (this mechanism is a special case of the above specification for $N = 1 )$ . A seller’s profile in such a mechanism can only be in two states: good (most recent k-period outcome was positive) or bad (most recent k-period outcome was negative). Let

$$
\psi (s) = \left\{ \begin{array}{l l} 1 & \text { if } s > 0 \\ 0 & \text { if } s = 0 \end{array} \right..
$$

Then $\begin{array} { r } { \Psi ( z ) = \sum _ { i = 0 } ^ { k - 1 } { \psi } ( s ( z , i ) ) } \end{array}$ denotes the number of periods within each block where the seller cooperates with positive probability. The probability that a seller who cooperates during $\Psi ( z )$ periods of a k-period block (and cheats during the remaining periods) will receive negative ratings in all k periods is equal to $\alpha ^ { \Psi ( z ( x ) ) } \beta ^ { k - \Psi ( z ( x ) ) }$ . The seller’s value function is equal $\mathrm { t o } ^ { 7 }$

$$
\begin{array}{c} V (x) = \sum_ {i = 0} ^ {k - 1} \delta^ {i} [ s (z (x), i) \widehat {w} _ {2} - \psi (s (z (x), i)) c ] \\ + \delta^ {k} [ (1 - \alpha^ {\Psi (z (x))} \beta^ {k - \Psi (z (x))}) V (g o o d) \\ + \alpha^ {\Psi (z (x))} \beta^ {k - \Psi (z (x))} V (b a d) ] \\ x \in \{g o o d, b a d \} \end{array}\tag{9}
$$

subject to the following incentive compatibility constraints:

$$
\begin{array}{l} s (z (x), i) <   1 \Rightarrow V (g o o d) - V (b a d) \\ \qquad \qquad \qquad \leq c / \delta^ {k - i} \alpha^ {\Psi (z (x)) - 1} \beta^ {k - \Psi (z (x))} (\beta - \alpha) \end{array}
$$

$$
\begin{array}{c} s (z (x), i) > 0 \Rightarrow V (g o o d) - V (b a d) \\ \qquad \qquad \qquad \qquad \qquad \qquad \geq c / \delta^ {k - i} \alpha^ {\Psi (z (x)) - 1} \beta^ {k - \Psi (z (x))} (\beta - \alpha). \end{array}\tag{10}
$$

Equilibria that achieve maximum efficiency $V ( g o o d ) =$ $V _ { k } ^ { * }$ require that sellers cooperate with probability 1 on all k periods of blocks during which their profile is in the good state. Because a seller’s temptation to cheat is highest during the first period of each block (when the consequences of cheating are farther away), for a seller to cooperate during all k periods of a block, the difference $V ( g o o d ) - V ( b a d )$ must be high enough to make him at least indifferent between cooperation and cheating during the first period of each block and to make cooperation strictly preferable to cheating during later periods of a block.

The only way that $V ( g o o d ) > V ( b a d )$ is if the seller receives lower auction revenue during periods in which his profile is in the bad state. This, in turn, will only happen if buyers believe that the seller will cooperate with lower probability during such period blocks and ${ \mathrm { i f } } ,$ at equilibrium, it is rational for the seller to behave in this way, given the buyers’ beliefs. Observe, however, that because the mechanism has no memory, the seller’s incentive compatibility constraint during the bad state is also dictated by the difference between the payoffs of the good and the bad state. We have already established that the difference $V ( g o o d ) - V ( b a d )$ must be high enough to make sellers at least indifferent between cooperation and cheating during the first period of each block and to make cooperation strictly preferable to cheating during later periods of a block. However this, in turn, means that the difference in seller behavior between the good and the bad state can only be during the first period of a k-period block. Irrespective of their profile state, in all equilibria that attain efficiency $V _ { k } ^ { * } ,$ , sellers will cooperate with probability 1 during the last $k - 1$ periods of all blocks. Therefore, k-eBay-like mechanisms can only credibly punish a seller by threatening to lower his payoff during the first period of a k-period block. As $k$ grows, the gains from cheating grow accordingly, while punishment must still be restricted to one period. The only way that the threat of a single-period punishment can offset the gains from k-period cheating is if the single-period profit margin is very high.

The argument gets more convoluted for mechanisms that summarize more ratings $( \mathrm { i . e . , }$ when $N > 1 )$ but the resulting intuition remains the same: To attain maximum efficiency, equilibria induced by k-eBaylike mechanisms require that the seller cooperates during the last $k - 1$ periods of a block irrespective of his profile state.<sup>8</sup> A seller’s profile state only affects his behavior during the first period of a block, and thus, irrespective of the length of each block, punishment for bad outcomes must be restricted to lowering the seller’s revenue during one period. In conclusion, even though it is theoretically possible to increase the maximum efficiency of an eBay-like mechanism by reducing the frequency of profile updates, in practice, this would only be feasible in settings with very high seller profit margins.

## 3.3. Sticky Binary Reputation Mechanisms with Infrequent Updating

The past two sections have shown that the maximum efficiency that can be induced through k-2SRM and k-eBay-like mechanisms increases as the profile updating interval increases. However, both mechanisms have shortcomings that challenge the application of this idea in real-world settings. k-2SRM break down in settings where sellers can easily change identities. On the other hand, for all $k > 1 .$ , k-eBay-like mechanisms can attain the maximum efficiency only if the per-period profit margin of cooperating sellers is very high; this precludes the use of infrequent updating in most eBay-like markets.

This section proposes a novel reputation mechanism architecture that combines the best aspects of k-2SRM and k-eBay-like mechanisms. The new mechanism has minimum effective profit margin requirements that are only marginally higher to those of k-2SRM. At the same time, it can induce cooperation in settings where easy identity changes are possible. For reasons that will become apparent below, I will refer to this mechanism as a sticky binary reputation mechanism (SBRM) with infrequent updating (k-SBRM).

A k-SBRM is characterized by a binary reputation profile that each period can be either in the good state or in the bad state. The mechanism’s profile transition rules can be summarized as follows:

• When the seller’s profile is in the good state, the mechanism performs profile updates every k periods using the following rule: if at least one rating received in the last k periods is positive, then the seller’s profile remains in the good state; otherwise the seller’s profile transitions to the bad state.

• When the seller’s profile is in the bad state, the mechanism performs profile updates every single period as follows: if the most recent rating is negative, the seller’s profile stays in the bad state; if the most recent rating is positive, the seller’s profile reverts to the good state with transition probability $0 \leq \tau \leq 1$ and stays negative with probability 1 4. (Once in the bad state, the seller’s profile thus becomes sticky.)

The following proposition characterizes some key PPE that can be induced through the use of a k-SBRM.

Proposition 4. Consider a repeated game whose stagegame structure is described in Table 1 and a k-SBRM with information structure (1) and transition probability $\tau _ { k } =$ $( \dot { \alpha } \delta ) ^ { k - 1 }$ . Let

$$
\rho_ {k} ^ {S B R M} = \frac {1 + \frac {\alpha (1 - \delta)}{(\alpha \delta) ^ {k}} - \alpha \delta \frac {1 - \delta^ {k - 1}}{1 - \delta^ {k}}}{\beta - \alpha}.
$$

(1) $I f \rho \geq \rho _ { k } ^ { S B R M } .$ , then there exists a PPE where the seller cooperates with probability one during periods where his profile is in the good state and with probability

$$
s _ {k} ^ {-} = 1 - \frac {1 + \frac {\alpha (1 - \delta)}{(\alpha \delta) ^ {k}} - \alpha \delta \frac {1 - \delta^ {k - 1}}{1 - \delta^ {k}}}{\rho (\beta - \alpha)}
$$

during periods where his profile is in the bad state.

(2) The present value of the seller’s discounted lifetime payoff is maximized immediately following updates that leave his profile in the good state; it is then equal to

$$
V _ {k} ^ {*} = \frac {\widehat {w} _ {2} - c}{1 - \delta} - \frac {1}{1 - \delta^ {k}} \frac {\alpha c}{\beta - \alpha}.
$$

Proposition 4, in conjuction with Proposition 2, implies that a k-SBRM with transition probability $\tau _ { k } =$ $( \alpha \bar { \delta } ) ^ { k - 1 }$ can induce equilibria that attain the maximum PPE payoff that can be induced by any reputation mechanism with infrequent updating. Furthermore, the minimum per-period profit margin of cooperating sellers that is required for such equilibria to obtain is substantially lower than the corresponding minimum profit margin of k-eBay-like mechanisms, and almost as low as that of k-2SRM. Finally, k-SBRM are robust to easy identity changes. In environments where sellers can easily disappear and reappear with a new identity, the center simply needs to initialize the reputation profile of new sellers at the bad state. New sellers then have to pay their dues by enduring an initial phase of lower profitability before they transition to the good state. This makes it unattractive for them to change their identity at any point because they would then have to pay their dues again.

The intuition behind the lower profit margin requirements of k-SBRM is the fact that they allow more flexible punishment. k-SBRM induce full cooperation in the good state by threatening to lower the seller’s profits in every period of the bad state. Furthermore, the stickiness of the bad state means that, once there, the seller will find it difficult to revert back to the good state. Both of these properties help make the prospect of transitioning to the bad state sufficiently unattractive to the seller to deter cheating, even for relatively small profit margins.

The practical implementation of a k-SBRM requires estimation of seller parameters  and  by the mechanism designer for the purpose of properly setting the transition probability $\tau _ { k } = ( \alpha \delta ) ^ { k - }$ −<sup>1</sup>. There are several methods for accomplishing this. For example, the mechanism designer can perform field experiments to estimate , i.e., create one or more seller accounts (that are indistinguishable to genuine seller accounts but are, in reality, operated by the mechanism designer) and start selling products (always behaving honestly, of course). The percentage of negative ratings that these accounts accumulate after a sufficiently large number of transactions can serve as an estimate of . A reasonable estimate of the discount factor  in our setting would be $\delta = [ 1 / ( 1 + r d / 3 6 5 ) ] \times p ,$ , where r is the annualized interest rate, d is the expected number of days between consecutive transactions of the same seller, and p is the probability that the seller will exit the market at the end of the current period. Of the above three quantities, r is public knowledge, d can be estimated from the seller’s past history, and p can be estimated from the behavior of other sellers with similar characteristics.

## 4. Concluding Remarks

This work examines how the frequency of online reputation profile updates impacts the resulting trader behavior and market efficiency. Most existing reputation mechanisms update user profiles as soon as new ratings are posted to the system. The main result of this work challenges this practice as it shows that, under certain conditions, cooperation and efficiency can be increased by reducing the frequency of profile updates.

This paper’s principal finding is that reputation mechanisms can induce higher cooperation and efficiency if, instead of publishing new ratings as soon as they are received, they only update a trader’s public reputation profile every k transactions with a summary statistic of a trader’s last k ratings. In settings with noise, infrequent updating increases efficiency because it decreases the adverse consequence of spurious negative ratings. At the same time, however, infrequent updating increases a seller’s short-term profits from cheating and thus the minimum future punishment threat that can sustain cooperation. On eBay-like mechanisms, this second effect causes the minimum effective seller profit margin to substantially increase with k. The applicability of infrequent updating on eBay-like mechanisms is, thus, limited to items with very high profit margins. In contrast, our analysis finds that less frequent updating of twostate randomization mechanisms (2SRMs) and SBRMs can sometimes both increase efficiency and decrease the minimum effective profit margin. sticky binary reputation mechanisms (SBRMs) have the additional advantage that they can sustain cooperation even in environments where sellers can easily change identities, and are thus better suited to online environments.

In terms of future work, the analysis of this paper can be extended in a number of directions. First, I have looked at a setting with only two possible seller actions. An interesting extension is to consider environments with multiple or continuous seller actions. Second, I have assumed a monopolist seller. Dellarocas (2005) shows that, in simultaneous auction settings with a large number of buyers, the equilibria induced by reputation mechanisms become asymptotically independent of the reputation of competing sellers. This, in turn, implies that all results obtained under the assumption of a monopolist seller are also approximately valid in large-scale online auction settings where large numbers of buyers select among several simultaneous auctions for the same good by sellers of different reputations. The usefulness of infrequent updating in competitive settings with small numbers of buyers is not covered by this result, and thus would be a worthwhile avenue for future research. Third, I have assumed that seller costs and conditional probabilities of outcomes given effort are completely known to buyers. In some online environments, it is plausible that there might be different seller types with different cost structures and/or conditional probabilities of outcomes initially unknown to buyers. For example, in online marketplaces for professional services, such as eLance.com, professionals of varying (and privately known) ability levels advertise their services. In such settings, reputation mechanisms play a hybrid (discipline and learning) role: in addition to eliciting good conduct, past feedback should ideally also help buyers learn something about the unknown properties (type) of the seller they are facing. The design principles of such hybrid reputation mechanisms constitute an intriguing area for future research.

## Acknowledgments

This material is based on work supported by the National Science Foundation under CAREER Grant 9984147. The author is grateful to Drew Fudenberg and David Levine for helpful comments.

## References

Abreu, D., D. Pearce, E. Stacchetti. 1986. Optimal cartel equilibria with imperfect monitoring. J. Econom. Theory 39 251–269.

Ba, S., P. Pavlou. 2002. Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quart. 26(3) 243–268.

Bajari, P., A. Hortacsu. 2003. Winner’s curse, reserve prices and endogenous entry: Empirical insights from eBay auctions. RAND J. Econom. 34(2) 329–355.

Bolton, G. E., E. Katok, A. Ockenfels. 2004. How effective are online reputation mechanisms? An experimental investigation. Management Sci. 50(11) 1587–1602.

Cabral, L., A. Hortacsu. 2004. The dynamics of seller reputation: Theory and evidence from eBay. NBER Working Paper W10363, Cambridge, MA.

Cripps, M., J. Thomas. 1995. Reputation and commitment in twoperson repeated games without discounting. Econometrica 63 1401–1419.

Cripps, M., K. Schmidt, J. Thomas. 1996. Reputation in perturbed repeated games. J. Econom. Theory 69 387–410.

Dellarocas, C. 2000. Immunizing online reputation reporting systems against unfair ratings and discriminatory behavior. Proc. 2nd ACM Conf. Electronic Commerce. Association for Computing Machinery, Minneapolis, MN, 150–157.

Dellarocas, C. 2003. The digitization of word-of-mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10) 1407–1424.

Dellarocas, C. 2005. Reputation mechanism design in online trading environments with pure moral hazard. Inform. Systems Res. 16(2) 209–230.

Dellarocas, C., M. Fan, C. Wood. 2003. Self-interest, reciprocity, and participation in online reputation systems. 2003 Workshop Inform. Systems Econom. WISE, Seattle, WA.

Dewan S., V. Hsu. 2004. Adverse selection in electronic markets: Evidence from online stamp auctions. J. Indust. Econom. 52(4) 497–516.

Fan, M., Y. Tan, A. B. Whinston. 2005. Evaluation and design of online cooperative feedback mechanisms for reputation management. IEEE Trans. Knowledge Data Engrg. 17(3) 244–254.

Friedman, E., P. Resnick. 2001. The social cost of cheap pseudonyms. J. Econom. Management Strategy 10(1) 173–199.

Fudenberg, D., D. K. Levine. 1992. Maintaining a reputation when strategies are imperfectly observed. Rev. Econom. Stud. 59(3) 561–579.

Fudenberg, D., D. K. Levine. 1994. Efficiency and observability with long-run and short-run players. J. Econom. Theory 62 103–135.

Fudenberg, D., D. K. Levine, E. Maskin. 1994. The folk theorem with imperfect public information. Econometrica 62(5) 997–1039.

Green, E. J., R. H. Porter. 1984. Noncooperative collusion under imperfect price information. Econometrica 52 87–100.

Jurca, R., B. Faltings. 2004. CONFESS: Eliciting honest feedback without independent verification authorities. Sixth Internat. Workshop Agent Mediated Electronic Commerce AMEC VI 2004, New York, 59–72.

Keser, C. 2003. Experimental games for the design of reputation management systems. IBM Systems J. 42(3) 498–506.

Lucking-Reiley, D., D. Bryan, N. Prasad, D. Reeves. 2006. Pennies from eBay: The determinants of price in online auctions. J. Indust. Econom. Forthcoming.

MacInnes, I., Y. Li, W. Yurcik. 2005. Reputation and dispute in eBay transactions. J. Electronic Commerce 10(1) 27–54.

Miller, N., P. Resnick, R. Zeckhauser. 2005. Eliciting honest feed back: The peer-prediction method. Management Sci. 51(9) 1359– 1373.

Resnick, P., R. Zeckhauser. 2002. Trust among strangers in Internet transactions: Empirical analysis of eBay’s reputation system. M. R. Baye, ed. The Economics of the Internet and E-Commerce. Advances in Applied Microeconomics, Vol. 11. JAI Press, Amsterdam, The Netherlands.

Resnick, P., R. Zeckhauser, E. Friedman, K. Kuwabara. 2000. Reputation systems. Comm. ACM 43(12) 45–48.

Sen, S., N. Sajja. 2002. Robustness of reputation-based trust: Boolean case. Proc. First Internat. Joint Conf. Autonomous Agents and Multiagent Systems. Association for Computing Machinery, Bologna, Italy, 288–293.

Tedeschi, P. 1994. Cartels with homogeneous and differentiated products and imperfect monitoring. Internat. Econom. Rev. 35(3) 635–656.

Yu, B., M. Singh. 2002. An evidential model of distributed reputation management. Proc. 1st Internat. Joint Conf. Autonomous Agents Multiagent Systems. Association for Computing Machinery, Bologna, Italy, 294–301.

Zacharia, G., A. Moukas, P. Maes. 2000. Collaborative reputation mechanisms in electronic marketplaces. Decision Support Systems 29(4) 371–388.
