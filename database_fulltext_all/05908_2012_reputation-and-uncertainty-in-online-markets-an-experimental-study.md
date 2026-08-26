---
otero_id: 5908
otero_key: "PPFZEPSW"
title: "Reputation and Uncertainty in Online Markets: An Experimental Study"
authors: "Sarah C. Rice"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0362"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/PPFZEPSW/fulltext/images/ee7eb3935ddb622a9d2d7fd9682909c7bd253bd75884f5b8254b414dc9abb0e1.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Reputation and Uncertainty in Online Markets: An Experimental Study

Sarah C. Rice,

## To cite this article:

Sarah C. Rice, (2012) Reputation and Uncertainty in Online Markets: An Experimental Study. Information Systems Research 23(2):436-452. http://dx.doi.org/10.1287/isre.1110.0362

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PPFZEPSW/fulltext/images/5e40b4be22f5aa003c6417dfff00bfb6cb530aaef4dcd2c37bb2c1299bd10751.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Reputation and Uncertainty in Online Markets: An Experimental Study

Sarah C. Rice

School of Business, University of Connecticut, Storrs, Connecticut 06269, srice@business.uconn.edu

his paper employs a modified investment game to study how online reputation ratings are assigned, and Tthus how electronic reputations are formed in transactions where buyers and sellers interact anonymously. Of particular interest are the important questions of how online reputations evolve and how specific reputation information is interpreted by market participants. We vary the level of uncertainty in the transaction environment, and measure the effects of this manipulation on buyers’ trust and their subsequent rating behaviors. We distinguish between a reputation mechanism and specific reputation information, finding the former has an association with the overall decision of whether to transact in the marketplace, while the latter shows signif icance in purchase decisions regarding specific sellers. We also find that aggregate reputation information is weighted differently than singular reputation information. Finally, we show that when reputations are increasingly noisy, buyers are less likely to react negatively to poor ratings and are more likely to give sellers the benefit of the doubt when seemingly uncooperative outcomes occur.

Key words: reputation systems; online markets; experimental economics History: Alok Gupta, Senior Editor; Gautam Ray, Associate Editor. This paper was received on February 1, 2008, and was with the authors 14 months for 4 revisions. Published online in Articles in Advance September 15, 2011.

## 1. Introduction

Reputation is in itself only a farthing candle of a wavering and uncertain flame, and easily blown out; but, it is the light by which the world looks for and finds merit. —James Russell Lowell

One of the definitive characteristics of electronic markets is the information asymmetry that exists between buyers and sellers. Sellers have an information advantage over buyers, as only sellers know their type with certainty. In addition, buyers do not know the true quality of the goods and services offered, so they must trust sellers’ descriptions when making a purchase decision. Economic theory shows that the absence of an enforcement mechanism in markets with information asymmetry can lead to moral hazard problems and adverse selection. In extreme cases, this moral hazard and adverse selection can cause the dissolution of the market such that no transactions occur (Akerlof 1970).

A moral hazard problem arises when one party is exposed to less risk than the rest of the market, providing an opportunity to capitalize on this advantage at the expense of others. The moral hazard problem in online markets stems from the fact that buyers move first by sending payment to sellers before goods are shipped. Because buyers are the first movers in the online transaction, they bear the vast majority of the risk, while sellers, in turn, bear much less risk. As a result, sellers may try to exploit buyers’ position by delivering low-quality goods at high-quality prices, or by not shipping the good as promised.

To help address the information asymmetry in online markets, many e-commerce sites feature public online reputation systems. These systems allow trading partners to leave ratings and comments about prior transactions. The result is an electronic reputation system that evolves from third-party reporting, where individuals can access information about specific community members online. The hope is these electronic reputation systems can substitute for reputations that would otherwise be established through repeated interaction, providing incentives for buyers and sellers to cooperate in spite of the existing moral hazard problem.

Although there is evidence showing reputation systems can induce cooperation in markets with information asymmetry (Ba and Pavlou 2002, Resnick and Zeckhauser 2002, Dellarocas 2005, Bolton et al. 2005), the incidence of online fraud remains relatively high. The most common instances of fraud occur in Internetbased auctions such as those hosted by eBay, Amazon Auctions, and Yahoo! Auctions. Although the growth in online auctions has been undeniable, the choice to do business in this arena is not without risk. The Federal Trade Commission in 2000 noted an “explosion” of Internet auction fraud cases (http://www.fbi.gov/ majcases/fraud/internetschemes.htm), and in 2007, the Federal Bureau of Investigation statistics show the highest sector of reported Internet fraud was Internet auction fraud. Furthermore, according to the National Consumer League, in 2007, approximately 13% of all Internet fraud was because of nonshipment or misrepresentation of goods (http://www.fraud.org/ internet/2007internet.pdf). Though many online auction sites use electronic reputation systems, the relatively high incidence of fraud indicates there is still much to be learned about how to effectively design and implement these systems.

We use experimental economics to address the important questions of how electronic reputations evolve and how different reputation information is used in online transaction decisions. Specifically, we ask: (1) How are reputation ratings assigned, and subsequently, how are reputations formed in online markets? Currently there is a body of literature discussing various effects of reputation and reputation systems, but this literature is silent regarding how reputation ratings are assigned, and thus how online reputations are formed. (2) What are the economic and behavioral effects of different reputation information? Empirical work is inconclusive in answering this question, perhaps because of confounding effects in field data. A laboratory experiment provides additional control to allow further insights into the effects of reputation information. (3) How does uncertainty in the transaction environment affect the functionality of the reputation system? We know there is uncertainty in online transactions; however, to date there is no work that explores the effect of this uncertainty on reputation formation and the use of reputation information in transaction decisions.

The market exchanges in this study are modeled after the investment game, which is a variation of the trust game (Berg et al. 1995). In our game, one player is given an endowment, which can be “invested” and sent to another player. This investment is increased by a designated amount, after which the second player decides how much to send back to the first player. In our reputation treatments, players are asked to rate their partner at the conclusion of the exchange. We also design a treatment to investigate the directional effects of uncertainty in this type of market. Specifically, we impose a setting where there is a 30% chance the amount returned by the second player can be intercepted and reduced to 0.<sup>1</sup> Under these conditions, when the first mover receives nothing in return, it is not known whether the outcome was intended by the second mover or if the amount returned was intercepted. This treatment allows us to assess the directional effects of uncertainty on reputation ratings, and the subsequent effects of “noisy” reputation information on transaction decisions.

Addressing the question of how reputation ratings are assigned, and subsequently, how reputation histories evolve, we find that when sellers failed to meet buyers’ expectations, poor ratings ensued. Good ratings were more likely when buyers’ expectations were exceeded. Exceptions to these findings were found in our treatments where additional uncertainty was imposed. When uncertainty was greater, buyers were more willing to exhibit trust than in settings without the imposed uncertainty. Specifically, we find that when subjects were uncertain about the intentions of their transaction partner, a negative outcome was less likely to be followed by a poor rating.

We distinguish between the reputation mechanism and the specific reputation information disseminated by the system, and find the presence of a reputation mechanism had a significant association with buyers’ decisions to engage in the transaction. We also find noteworthy differences regarding the interpretation and weighing of each type of reputation information. Without additional uncertainty, the aggregate of a seller’s good ratings had a positive association with the buyer’s investment decision, while a single good rating assigned in the prior round had no effect. We find that imposing uncertainty on the transaction environment moderated the negative effects of poor ratings on investment amounts, resulting in fewer poor ratings assigned to sellers when negative transaction outcomes ensued. This result suggests the possibility that buyers gave sellers the benefit of the doubt under conditions of greater uncertainty, and did not punish seemingly uncooperative outcomes when intentions could not be perfectly inferred.

The remainder of the paper proceeds as follows. First, is a discussion of the background and motivation for this study, followed by an explanation of the game, and the experimental design. Next, the hypotheses and results are discussed. The paper concludes with a summary of findings, limitations, and extensions.

## 2. Background and Motivation

## 2.1. Reputation Systems

Reputation can be defined as the conditional probability that an individual will behave in a certain manner (Kreps and Wilson 1982). One way for individuals to develop a reputation is to interact with each other repeatedly so that a transaction history evolves over time. From this first-hand experience, a reputation is established, by which potential transaction partners can derive a conditional expectation of an individual’s future behavior. However, in online transactions, it is likely that buyers and sellers may not interact with enough frequency for reputations to be established. In this type of setting, another way to facilitate reputation formation is via third-party reporting, a community enforcement mechanism where buyers and sellers report past actions of transaction partners (Ba 2001). The third-party reported information is aggregated and disseminated in an online format and is what comprises an electronic reputation system.

While electronic reputation systems function in a modern-day context, third-party reporting as an enforcement mechanism was also used in medieval communities, where word-of-mouth references helped facilitate economic and social activities. One relevant example is that of the Maghribi traders, a group of Eleventh-Century Mediterranean traders governed by a coalition structure. Traders sold their goods via overseas agents, allowing them to operate in a more diverse field and to use local expertise. These overseas agents conducted business with assets they did not own but rather were “lent” to them by the traders. In return, agents were responsible for sharing profits with the merchant who provided the assets. Although the information asymmetry between traders and agents left room for agents to exhibit opportunistic behavior, only a few incidents of misconduct have been documented (Grief 1993). The control mechanism in place was one of reputation built on trust and reciprocation; traders exhibited trust by lending capital to agents, and this trust was reciprocated when agents paid the trader a share of their earned profits. An agent who failed to reciprocate the traders’ trust acquired a reputation for being a cheater and faced the likely prospect of future unemployment. Grief (1993) notes that the actions of agents were imperfectly observable by traders, thus there was a positive probability that at some point, an honest agent could be considered a cheater. For example, if traders experienced unprofitable trade outcomes, it was possible they could have blamed the agents, perhaps believing they were pocketing a larger share of the profits. Given that traders only observed the outcomes of these transactions, blame could be placed regardless of whether it was truly the fault of the agent, or the result of some exogenous influence. Although anecdotal, Grief’s (1993) point raises the question as to how imperfectly observable actions impact a reputation, and the subsequent economic outcomes of the individual in question. One outcome might be, as Grief (1993) states, to assume the worst and punish the agent for what appears to be cheating behavior. The other option is to give the agent the benefit of the doubt and assume that the intent was not to cheat, thereby declining to punish what would otherwise be considered noncooperative behavior.

While agent reputations in the era of the Maghribi traders were created and disseminated via word of mouth, in the modern-day online business community, reputations can be created and disseminated via the Internet. An online reputation is a history of reported evaluations left by prior transaction partners, and this information is then disseminated to the community. Sites such as eBay assign buyers and sellers a reputation score tabulated from past ratings, and an individual’s reputation is a direct measure of the ratings assigned to him or her by other community members (Resnick and Zeckhauser 2002). By conducting a controlled study to gain understanding into how these ratings are assigned, we provide insight into how reputations are formed in online markets.

Third-party reputation formation is becoming an increasingly relevant factor in the functionality of online markets, and as such, has emerged as an important area of research. For example, an experiment by Bolton et al. (2004) investigates the effectiveness of third-party reporting in establishing credible reputations. They construct three markets: (1) a strangers market where players interact anonymously with no reputation building, (2) a feedback market where reputation is established based on the truthful reporting of individuals’ past actions, and (3) a partners market where the same two players are paired for the entire experiment. The study of Bolton et al. (2004) finds that efficiencies of trade, measured as the percentage of completed transactions, and social welfare were significantly higher in the feedback market than in the strangers market. The results of Bolton et al. (2004) support prior work by Schwartz et al. (2000), showing that although first-hand reputation building is preferred, reputations based on third-party reporting also have social and economic benefits.

Studies specifically focusing on electronic reputation systems show these mechanisms to be effective in building trust and cooperation in online communities (Resnick et al. 2000, Dellarocas 2003). Ba and Pavlou (2002) conclude that trust can be induced through eBay’s ratings system and show that when trust is enhanced, more profitable outcomes ensue. A field study by Lucking-Reiley (2000) investigates the determinants of price in online transactions and finds that sellers with poor feedback ratings receive lower rents. Resnick et al. (2006) conduct a series of field experiments to investigate the value of reputation on eBay and find that sellers with more established reputations receive higher profits than those with less established reputations. Work by Dellarocas (2003) models a reputation mechanism in a moral hazard setting and shows that ratings systems can induce cooperative outcomes between buyers and sellers. An empirical study by Kauffman and Wood (2005) examines factors that could explain individual-specific price variance for the same good, one of which is reputation. Additional empirical work shows that reputation systems can have positive effects on prices (Ba and Pavlou 2002, Melnick and Alm 2002, Dewan and Hsu 2004). For a more comprehensive list of empirical studies testing the economic effects of eBay’s reputation system, we direct the reader to Resnick et al. (2006).

## 2.2. Reputation Formation and Imperfect Information

Reputation formation has been studied in an offline context, but remains for the most part unexplored in the online medium. Marschak and Selten (1978) introduced the notion of reputation formation, disputing the game-theoretic backward induction prediction that a repeated play setting is merely a repetition of what would occur if only one interaction took place. They note that with repeated play, there might be incentives to act differently in earlier rounds, establishing a reputation for cooperation to reap economic benefits in subsequent rounds. Kreps et al. (1982) and Milgrom and Roberts (1982) each formalize game-theoretic models where reputation formation in finitely repeated games arises as a sequential equilibrium, where players form beliefs at each node of the decision tree and these beliefs motivate a strategic choice. Camerer and Weigelt (1988) study reputation formation in an experimental setting and find that observed play is consistent with a sequential equilibrium. Jung et al. (1994) also study reputation formation in an experimental setting, and establish that reputation formation is a factor in strategic outcomes. An experimental study by King (1996) explores how reputations for honesty in reporting can be established and sustained in a market setting. In his study, the buyer’s choice to trust the seller depends on whether the seller’s actions over time result in a reputation for honesty, or a reputation for cheating.

In stage games with perfect public monitoring, a steady-state outcome is the equilibrium where the player’s reputation converges to the Stackleberg type (Cripps et al. 2004, Dellarocas 2003). In reality, knowing buyer and seller types with certainty in an online setting is not realistic, as individual actions are not perfectly observable. For example, good types might behave as such and still receive a poor reputation score, even though their actions were honorable. Alternatively, bad types might receive a good reputation score in spite of the intent to cheat. Although online transactions are inherently noisy with respect to monitoring buyer and seller types, to date there is little work that specifically measures the effects of this uncertainty on the functionality of the reputation system, and on buyer and seller transaction decisions. As previously stated, Dellarocas (2003) models a reputation mechanism design with pure moral hazard under complete information. He shows that if there is no uncertainty about the seller’s type, an eBaytype reputation mechanism can induce maximum efficiency. However, if uncertainty about the seller’s type is imposed, these assumptions may not hold, implying that discerning the effects of uncertainty on a reputation system is a topic worth exploring. While the above literature shows that reputation systems can have positive associations with price, cooperation, trust, and strategic choice, there is still little guidance on how reputations evolve in an online context.

## 3. Experimental Design

The investment game in this experiment originates from the ultimatum game and the trust game, and was initially used by Berg et al. (1995) to study the effects of social history on trust and reciprocity. For ease of exposition, when describing the game and our experiment, players will be referred to as buyers and sellers. Our design adds to the investment game by incorporating an earlier action to each round of play. At the start of each round, sellers represent their “products” to buyers by filling out a nonbinding announcement, stating what would be returned for each given level of investment. This nonbinding announcement serves as a baseline for measuring trustworthy behavior and creates an ethical dilemma for sellers, forcing them to differentiate between what they claim they will return and their actual return decision. Next, buyers are given \$1 at the start of the game, and after being shown the nonbinding announcement, they decide how much of this \$1 to send to their paired seller. Buyers may send one of five amounts; \$0.00, \$0.25, \$0.50, \$0.75, or \$1.00. The amount sent is multiplied by 4, so the most sellers can receive is \$4.00 and the least they can receive is \$0.00. Upon receipt of the investment, sellers decide how much to return to buyers. In the treatments without reputation, the round ends when buyers are informed of their final returned amounts. In the treatments with reputation, buyers are asked to rate the transaction after its completion by assigning a rating of good, neutral, or poor.

The experiment was run in a repeated play setting, meaning the game was conducted over multiple rounds. Rather than set a finite end point to the experiment, the choice was made to incorporate a stochastic ending so subjects did not know for certain which was the final round of play. The point of this design choice was to mitigate possible end-game effects, where in the final round of the game, sellers have no incentive to cooperate, as reputation concerns no longer matter. The result is that in the final round, sellers would be more likely to “burn” their reputation by keeping all of the buyer’s investment and returning \$0.00. Realizing this to be the likely outcome, buyers would not invest in the final round and the second to last round would actually become the concluding round of play. In theory, sellers would employ the same strategy and burn their reputation in this new final round, so buyers again would not invest. If this pattern continued, eventually the entire game would unravel to the first round and no transactions would ever occur. Although this is an extreme outcome, we wanted to lessen the severity of an end game effect, so the final round of the experiment was determined by rolling a pair of dice after the tenth round. Subjects were informed that if either a 7 or 10 were rolled, the game ended, otherwise play continued to another round. Implementing this ending rule, where there was a 25% chance the game would terminate each time the dice were rolled, made it more difficult for subjects to condition their strategy on the final round.<sup>2</sup>

Our experiment generalizes to online transactions by incorporating the elements of trust, trustworthiness and reciprocity; all factors in an online transaction setting. The seller’s announcement equates to presenting a good or service to the buyer, to be delivered upon the buyer’s payment of a predesignated amount. After seeing this “product,” buyers must then trust sellers by sending payment for the good before receiving the item. Because the announcement is nonbinding, there exists the possibility that our sellers can cheat buyers and return amounts (ship products) that do not align with what they initially represented. Sellers have an opportunity to reciprocate trust, or they can choose to exploit buyers by either refusing to send the good (return \$0.00), or sending an inferior good (return less than promised).

To investigate the effects of uncertainty on the transaction outcome and the functionality of the reputation system, we conducted a manipulation where there was a 30% chance the amount sellers chose to return to buyers was intercepted and reduced to 0. While the possibility of interception was common knowledge, none of the subjects ever knew whether their return was actually intercepted. We chose not to disclose this information so that subjects could not calculate probabilities going forward.

The practical significance of this manipulation lies in the fact that online transactions exist in a setting where uncertainty is a factor. Intentions are inferred from outcomes, but for the most part, intentions of buyers and sellers are not perfectly known. For example, there might be multiple reasons buyers would experience a poor transaction outcome; they might be disappointed with the good, the shipping process, communication with the seller or the final purchase price. This unsatisfactory result might be because of the seller’s true intentions but could also be a mistake made by the buyer,<sup>3</sup> the seller or an external circumstance such as shipping error or technology failure. Understanding how uncertainty impacts the decision making of buyers and sellers could be useful in improving reputation mechanism design and is an important objective of this research.

While this is admittedly a highly structured experiment and not a field study set in the context of actual online transactions, the additional control provided by the laboratory allows us to carefully draw inferences about specific behaviors and outcomes in transactions, where buyers and sellers are connected only by the online medium. In an actual online environment, there are many competing factors that could confound measurement of trust and trustworthiness, including different valuations for the same good, different perceptions of quality and interactions with other bidders. From our results, we are able to provide insights into the behavioral and economic effects of our manipulations, thus supplementing findings from field studies that may not offer a high level of internal validity.

Figure 1 depicts the game sequence, indicating the specific manipulations for the treatments with reputation and those with interception.

The experiment was computerized so that subjects never interacted face to face, and at no time were they told the identity of the subject with whom they were paired.<sup>4</sup> Screen shots of what subjects saw in the experiment are included in the appendix. All subjects participating in the pilot studies and the full experiment were upper-level undergraduate and graduatelevel business students. Prior to implementing the full design, a pilot study testing the effects of the electronic reputation system was conducted. A second pilot study was run on a different subject group to test for comprehension of the experimental instructions. This pilot confirmed that subjects understood the subtleties of the manipulation and allowed us to focus on their responses to the experiment. None of the subjects who participated in the pilot studies participated in the main experiment.

Figure 1 Game Sequence  
![](/api/attachments/PPFZEPSW/fulltext/images/137337eee74043fd13dda4751e5f72b57f66b60beef9324c2abfc5a37eadd3f7.jpg)

A total of 90 students were recruited to participate in the full-scale experiment. Subjects required no special skills or prior experiences to participate. Because the experiment tested decision making that was not generalized to upper-level managerial settings, the choice to use students was appropriate. The design was between subjects, thus each subject participated in only one of the four treatments. Subjects first read a set of instructions detailing the implementation of the experiment and then were given a short quiz to test for comprehension. The experimenter led subjects through a series of training sessions, so that they became familiar with the software interface. Subjects were trained on both buyer and seller interfaces but were randomly assigned to one role at the start of the experiment, and they maintained that role throughout the experiment. Compensation for participation consisted of a \$6 show-up fee, in addition to the accumulated earnings from each round.<sup>5</sup>

## 4. Hypotheses Development

Our hypotheses development is presented in three sections, each relating to one of the three questions addressed in this study: (1) the economic and behavioral effects of online reputation systems, (2) the evolution of online reputations, and (3) the directional impact of uncertainty on the functionality of online reputation systems.

## 4.1. The Reputation Mechanism and Specific Reputation Information

A primary objective of this work is to distinguish between the effects of the reputation mechanism, or the electronic reputation system, and the specific reputation information provided by the system. The difference is subtle, yet important to note. A reputation system is a control mechanism that can enforce cooperation among market participants by providing incentives for buyers and sellers to maintain a good reputation. Alternatively, the information distributed by the reputation system is a potentially informative input to buyer and seller decision-making processes, as it can aid market participants in evaluating the probability of an individual’s future cooperation.

In markets where buyers and sellers are virtually anonymous, a reputation system establishes a control mechanism, such that market participants are more accountable for their actions than if no such system were implemented. Without a reputation mechanism in place, cooperative outcomes are less likely, as there are no long-term economic benefits to cooperation that offset the short-term gains from opportunism. A significant body of literature notes the cooperative effects of a reputation mechanism on buyer and seller decisions, showing that reputation systems can effectively mitigate moral hazard problems and promote cooperative behavior (Kreps et al. 1982, Milgrom and Roberts 1982, Kreps 1990, Lucking-Reiley 2000, Schwartz et al. 2000, Ba and Pavlou 2002, Resnick and Zeckhauser 2002, Dellarocas 2003, Dewan and Hsu 2004, Bolton et al. 2005, Cripps et al. 2005, Dellarocas 2005). Using backward induction to derive buyer and seller equilibrium behavior, we can gain further insight into the possible effects of a reputation mechanism in an online transaction setting. Consider our investment game: in a single-shot setting where only one transaction occurs, sellers do not have an incentive to cooperate, as there are no future economic benefits to doing so. Based on this incentive structure, a buyer’s optimal strategy is to choose not to invest. Simply put, theory predicts that in a single shot setting where there is no control mechanism in place, sellers will expropriate all buyer investments. As a result, a buyer’s best response is to never invest, and thus no transactions occur. In a repeated play setting, where buyers and sellers interact anonymously in each round, there is still no reputational incentive for sellers to cooperate. For this reason, the theoretical result shows that repeated anonymous transactions have the same equilibrium outcome as the single-shot game where no trade occurs.

In a repeated play setting where buyers and sellers remain in the same dyads over all rounds, reputations evolve as a result of first-hand experience. In this setting, the Nash equilibrium is one where sellers cooperate to establish a good reputation to reap the benefits of future play. Given that sellers have incentives to cooperate when their reputations are at stake, the buyers’ strategy is to invest a positive amount when they interact with the same seller repeatedly. When buyers and sellers do not interact repeatedly, but a perfectly informed reputation system is in place, the theoretical prediction should be the same; sellers cooperate to maintain a good reputation, and subsequently buyers invest. Accordingly, we expect buyer investments and seller return amounts to be higher in markets where a reputation mechanism is used.

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> The reputation system will have a positive association with buyers’ investment levels.

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> The reputation system will have a positive association with sellers’ return decisions.

In addition to hypothesizing the general effects of the reputation mechanism, we are also interested in the effects of the specific reputation information. This specific reputation information pertains to the actual ratings assigned to a particular individual, and provides buyers a way to assess the likelihood that a certain seller will cooperate. Work focusing on the effects of specific reputation ratings in economic transactions includes a field study by Lucking-Reiley (2000), exploring the determinants of pricing in online auctions. He finds that seller reputations have a measureable effect on pricing, and that a good seller reputation can generate a price premium. Resnick and Zeckhauser (2002) show slight support for the association between positive ratings and higher sale prices, as well as an association between negative ratings and lower sale prices. In the same vein, work by Melnik and Alm (2002) also shows that a seller’s reputation can have a positive impact on prices.

To summarize our setting, in equilibrium, sellers should bear costs for a poor reputation that exceed the benefits they could gain from opportunistic behavior. Likewise, sellers’ should be rewarded for good reputations, and these rewards should exceed the possible gains from opportunism (Shapiro 1983). Therefore we predict a negative association between poor ratings and buyer investments, and predict a positive association between good ratings and buyer investments.

<sup>Hypothesis</sup> <sup>3A</sup> <sup>(H3A).</sup> Sellers’ poor ratings will have a negative association with buyers’ investment levels.

<sup>Hypothesis</sup> <sup>3B</sup> <sup>(H3B).</sup> Sellers’ good ratings will have a positive association with buyers’ investment levels.

Interestingly, Resnick and Zeckhauser (2002) find that neutral ratings are more likely to be used for slightly problematic exchanges, such as when a product is satisfactory but does not exactly match its online description, or when shipping times are slow. Moreover, in eBay’s calculation of reputation scores neutral ratings hold no value. Because the assignment of a neutral rating is relatively ambiguous, we limit our hypotheses to only good and poor ratings.

## 4.2. Online Reputation Formation

An important aspect of this study is the investigation of how electronic reputations are formed in online market transactions. Specifically, we seek to understand what might prompt buyers to leave good versus poor ratings. Work by Bell (1985) on disappointment theory provides insight into our predicted outcomes. Disappointment theory states that decision makers under risk will form reference points and then evaluate outcomes according to these anchors. Disappointment is further defined as a psychological reaction to an outcome that does not meet a decision maker’s a priori expectation (Bell 1985), and is measured as the distance between the average expected outcome and the actual payoff. Conversely, outcomes that exceed the decision maker’s expectations are viewed positively, and the individual may experience elation as a result.

Disappointment theory evolved from studies exploring the effects of regret on risk attitude (Bell 1982, 1985; Loomes and Sugden 1982). Regret is defined as a psychological reaction to making a wrong decision, where “wrong” is evaluated by comparing the realized outcome with the payoff one could have received if he or she had made a different decision. In our experiment, the nonbinding announcement indicated by the seller at the start of the transaction sets the buyer’s reference point for a return amount. According to the theory, any return less than the promised amount could result in disappointment; therefore it is likely that a poor rating would be assigned when a buyer experiences disappointment and/or regret following the seller’s return. Conversely, if the seller’s return amount exceeds the buyer’s reference point, this would be viewed as a good outcome, in which case a positive rating should be more likely.

<sup>Hypothesis</sup> <sup>4A</sup> <sup>(H4A).</sup> Return amounts higher than promised will be associated with good ratings.

<sup>Hypothesis</sup> <sup>4B</sup> <sup>(H4B).</sup> Return amounts lower than promised will be associated with poor ratings.

4.3. Uncertainty in the Transaction Environment To address our research questions regarding the directional effect of uncertainty on the provision and use of reputation information, we incorporate a treatment, where additional noise is introduced into the transaction environment. Recall that in the treatments where additional uncertainty is imposed, the seller’s return choice may be intercepted by the experimenter and reduced to 0. This type of perturbation, where players’ actions can also be shown as mistakes, is often called a “trembling hand.” The trembling hand equilibrium was first specified analytically by Selten (1975) and assumes that players might play the off equilibrium strategy because of a “slip of the hand.” Prisoner’s dilemma games that incorporate trembling treatments into the design show that when players cannot infer the intentions of others with certainty, they will sometimes give each other the benefit of the doubt when noncooperative outcomes occur (Bendor et al. 1991, Sainty 1999). In the standard prisoner’s dilemma game, when one player knows the other has defected, the equilibrium response is for the second mover to also defect, following a tit-for-tat strategy. However, in a noisy prisoner’s dilemma game, if the second mover is uncertain as to whether the defection of the first mover was truly intended, that second mover may not always retaliate by defecting in kind. In addition, Fudenberg and Maskin (1990) show that an evolutionarily stable strategy of cooperation can occur if players believe there is a small probability others can make mistakes. Their results indicate that uncertainty regarding the alignment of outcomes versus intentions could impact cooperation and the intent to punish.

If one views online reputation ratings as reward or punishment for past behavior, the findings of Fudenberg and Maskin (1990) suggest that uncertainty may have an effect on the rating choice. Specifically, if intentions are uncertain, it is reasonable to expect that a punishment strategy might not always follow a poor outcome. Also, if it is known that reporting could be less accurate, then the reliability of a poor rating is drawn into question, as the possibility that an honest seller is assigned a poor rating becomes viable. We therefore predict that additional uncertainty imposed on the reputation system will render poor ratings less reliable on the margin, and thus their detrimental effect on investment amounts will be lessened. We also predict that there will be a lower incidence of poor ratings when interception is possible and intentions are not known with certainty.

<sup>Hypothesis</sup> <sup>5</sup> <sup>(H5).</sup> The possibility of interception will moderate the negative relationship between poor ratings and buyers’ investment amounts.

<sup>Hypothesis</sup> <sup>6</sup> <sup>(H6).</sup> The possibility of interception will have a negative effect on the number of poor ratings.

In summary, H1 and H2 relate to predictions about the reputation mechanism, and involve testing for treatment specific effects. Hypotheses H3A and H3B address the effects of reputation information and require tests that include specific reputation variables (good and poor ratings). Hypotheses H4A and H4B address the buyers’ rating decisions and assess what constitutes a good versus poor reputation score. Finally, H5 and H6 relate to the marginal effect of uncertainty on buyers’ investment choices and their rating decisions.

## 5. Analysis and Results

The first section of analyses (5.1) focuses on the effects of the reputation mechanism and specific reputation information on the transaction decisions of buyers and sellers. The second part of the analysis (5.2) turns to the reputation formation aspect of our study, investigating how ratings are assigned with and without the additional uncertainty imposed.

## 5.1. Buyer and Seller Transaction Decisions

Table 1 shows a comparison of means, along with the proportion of transactions initiated and completed, as a function of each of the four experimental treatments. Standard errors are reported in parentheses.

The comparisons in Table 1 show mean investments and mean returns were highest with a reputation mechanism in place, and without additional uncertainty imposed (RNI). Interestingly, this preliminary comparison shows no statistical difference in mean investment between the interception treatment with reputation (RI) and the interception treatment without reputation (NRI). It generally appears that even with the reputation system in place, when interception was possible, mean investments were lower. Table 1 also shows the mean proportions of initiated and completed transactions were highest in the two reputation treatments (RI, RNI).<sup>6</sup> This implies that buyers’ trust, exemplified by their willingness to transact, and sellers’ reciprocation of that trust, were each higher when a reputation mechanism was in place. These are simple univariate comparisons, however, which do not control for other associated factors. Accordingly, we base our formal inferences on the subsequent empirical tests.

Model 1 below tests the relationship between buyer investments and the reputation mechanism (H1), as well as seller-specific reputation information (H3A, H3B). The model also tests whether the imposed uncertainty influenced buyers’ investment choices, as a function of sellers’ prior ratings (H5). Because of the nonnormal distribution of the data, bootstrapping was used to obtain the coefficient estimates, standard errors, and p-values. We drew a sample of 596 observations with replacement, and repeated this process

Table 1 Descriptive Statistics by Treatment

<table><tr><td>Variable</td><td>Reputation no Interceptn (RNI)</td><td>Reputation with Interceptn (RI)</td><td>No reputation no Interceptn (NRNI)</td><td>No reputation with Interceptn (NRI)</td></tr><tr><td>Mean invested</td><td>$0.690(0.033)</td><td>$0.560(0.024)</td><td>$0.460(0.035)</td><td>$0.570(0.042)</td></tr><tr><td>Mean returned</td><td>$0.850(0.069)</td><td>$1.100(0.052)</td><td>$0.460(0.059)</td><td>$0.670(0.077)</td></tr><tr><td>Mean buyer profit</td><td>$1.410(0.050)</td><td>$1.290(0.037)</td><td>$1.010(0.058)</td><td>$1.110(0.044)</td></tr><tr><td>Mean seller profit</td><td>$1.670(0.090)</td><td>$1.370(0.066)</td><td>$1.360(0.112)</td><td>$1.590(0.133)</td></tr><tr><td>Mean ratio of return</td><td>1.390(0.015)</td><td>1.170(0.018)</td><td>0.530(0.022)</td><td>0.870(0.015)</td></tr><tr><td>Proportion of trustworthy returns</td><td>0.880(0.020)</td><td>0.830(0.030)</td><td>0.720(0.040)</td><td>0.610(0.040)</td></tr><tr><td>Proportion of initiated transactions</td><td>0.870(0.030)</td><td>0.850(0.030)</td><td>0.580(0.040)</td><td>0.740(0.040)</td></tr><tr><td>Proportion completed transactions</td><td>0.780(0.030)</td><td>0.640(0.020)</td><td>0.360(0.030)</td><td>0.440(0.040)</td></tr><tr><td>Subject count</td><td>22</td><td>22</td><td>24</td><td>22</td></tr><tr><td>Rounds</td><td>13</td><td>24</td><td>14</td><td>11</td></tr><tr><td>Observations</td><td>143</td><td>264</td><td>168</td><td>121</td></tr></table>

1,000 times to estimate the regression parameters. Because we structure each round of play as one unit of analysis, a random-effects model was specified to account for the likelihood of individual-specific correlated errors resulting from this design choice (Casari et al. 2007). In all models, subscript i indicates a specific seller, while subscript t indicates a specific round. All analysis was done using Stata 9.0.

Model 1: Bootstrapped Ordinary Least Squares (OLS) Regression of Buyer Investment

$$
\begin{array}{l} \text {Investment} _ {i, t} \\ = \beta_ {0} + \beta_ {1} \text {Intercptn} _ {i, t} + \beta_ {2} \text {Reputation} _ {i, t} \\ \quad + \beta_ {3} \text {Reputation} \times \text {Intercptn} _ {i, t} + \beta_ {4} \text {Profit Promise} _ {i, t} \\ \quad + \beta_ {5} \text {Round\_10 up} _ {i, t} + \beta_ {6} \text {Prior Return Amt} _ {i, t} \\ \quad + \beta_ {7} \text {Prior Good} _ {i, t} + \beta_ {8} \text {Prior Poor} _ {i, t} \\ \quad + \beta_ {9} \text {Intercptn} \times \text {Prior Good} _ {i, t} \\ \quad + \beta_ {1 0} \text {Intercptn} \times \text {Prior Poor} _ {i, t} + \beta_ {1 1} \text {Total Poor} _ {i, t} \\ \quad + \beta_ {1 2} \text {Total Good} _ {i, t} + \varepsilon_ {i, t}. \end{array} \tag {1}
$$

The Reputation variable is binary and indicates whether the reputation mechanism was present. It is coded as 1 if the buyer was asked to rate the transaction on its completion, and 0 otherwise. The Intercptn variable is also binary and indicates whether the sellers’ returns could be intercepted (1), or not (0). Reputation×Intercptn is the interaction term representing treatments where buyers were asked to rate sellers and interception was also possible.

To tease out the effects of specific reputation information, we include two different groups of reputation variables in our model. The variables Total Good and Total Poor represent the “aggregate rating” variables, and each indicates the total number of good and poor ratings in sellers’ reputation histories at the time of buyers’ investment decisions. We also include binary “single rating” variables, indicating whether the seller received a good or poor rating in the prior round. These instances are represented by the variables Prior Good and Prior Poor, respectively, and each is coded as 1 if true, and 0 otherwise. We interact the reputation variables with the interception treatment variable to test for moderating effects. The neutral rating is the reference group.

The rationale for partitioning the reputation information into aggregate versus single rating variables is based on work in behavioral finance, showing that investors may process and use information differently, depending on whether it is aggregated or more finely partitioned (Hirshleifer and Teoh 2003). This suggests that the reputation information in a seller’s rating history might be interpreted differently, depending on whether it is processed as an aggregate rating or a singular rating given in the most recent round. A reasonable distinction is that while the aggregate ratings provide a way to measure a seller’s performance over time, the rating from the prior round might provide information about a possible trend.

We conjecture that although sellers’ initial return announcements were nonbinding, this still may have had an effect on transaction decisions and should be controlled for. In theory, buyers should not invest if sellers promise a return equal to or less than the invested amount, as this means the buyer bears all the risk with no expectation of additional profits. We identify those instances where sellers promised a profitable return to buyers, meaning they promised to return amounts greater than what would be invested. If a profitable return is promised, we code these instances as 1, and 0 otherwise. This comprises the binary Profit Promise variable.

Although players are repaired after each round, thus making it unlikely the prior round outcome would be associated with a current partner, it is reasonable to assume that current round decisions would be influenced by prior experiences with other partners. We control for this with the Prior Return Amt variable, which is the amount returned to the buyer in the prior round. Although our design addresses the possibility of end-game effects, we still control for the possibility that investments might decrease markedly in the final round because incentives to cooperate are less salient. Round\_10up is binary, coded as 1 if the transaction occurs in round 10 or higher, and is 0 otherwise. Results are shown in Table 2.

Table 2 Results of Bootstrapped OLS Regression for Buyers’ Investment

<table><tr><td>Variable</td><td>E[sign]</td><td></td><td>Coefficient</td><td>P-value</td></tr><tr><td>Constant</td><td></td><td> $\beta_0$ </td><td>50.990(8.970)</td><td>0.000</td></tr><tr><td>Interceptn</td><td>+/-</td><td> $\beta_1$ </td><td>7.920(12.040)</td><td>0.111</td></tr><tr><td>Reputation</td><td>+</td><td> $\beta_2$ </td><td>11.910(11.210)</td><td>0.221</td></tr><tr><td>Reputation × Interceptn</td><td>+/-</td><td> $\beta_3$ </td><td>-14.020(15.020)</td><td>0.303</td></tr><tr><td>Profit Promise</td><td>-</td><td> $\beta_4$ </td><td>25.600(6.610)</td><td>0.001</td></tr><tr><td>Round_10up</td><td>+/-</td><td> $\beta_5$ </td><td>-15.100(2.930)</td><td>0.000</td></tr><tr><td>Prior Return Amt</td><td>+</td><td> $\beta_6$ </td><td>0.0260(0.024)</td><td>0.227</td></tr><tr><td>Prior Good</td><td>+</td><td> $\beta_7$ </td><td>1.6780(5.090)</td><td>0.862</td></tr><tr><td>Prior Poor</td><td>-</td><td> $\beta_8$ </td><td>-14.760(9.100)</td><td>0.069</td></tr><tr><td>Interceptn × Prior Good</td><td>+/-</td><td> $\beta_9$ </td><td>2.340(6.810)</td><td>0.654</td></tr><tr><td>Interceptn × Prior Poor</td><td>+</td><td> $\beta_{10}$ </td><td>19.120(9.610)</td><td>0.048</td></tr><tr><td>Total Poor</td><td>-</td><td> $\beta_{11}$ </td><td>-2.310(0.720)</td><td>0.000</td></tr><tr><td>Total Good</td><td>+</td><td> $\beta_{12}$ </td><td>4.700(0.970)</td><td>0.000</td></tr><tr><td>Observations</td><td></td><td></td><td>596</td><td></td></tr><tr><td> $R^2$ /Adjusted</td><td></td><td></td><td>0.260</td><td></td></tr></table>

Notes. Bootstrapped coefficients and p-values reported. Standard errors reported in parentheses.

Table 2 shows that overall the Reputation variable has no significant effect on buyer investment amounts, thus we do not find initial support for H1. We do see an association between buyer investments and some of the singular reputation information (i.e., Prior Poor and Interceptn × Prior Poor are significant), finding that when interception was possible, the negative impact of a prior poor rating was lessened. This result shows support for H5, which hypothesizes that the interception will moderate the negative relationship between poor ratings and buyer investments. Somewhat surprisingly, the overall effect of Prior Poor is positive $( \hat { \beta } _ { 8 } + \hat { \beta } _ { 1 0 } = 4 . 3 6$ cents), because the apparent willingness of buyers in the interception treatment to invest more when sellers had a poor rating in the preceding round. Although this result is somewhat counter intuitive, one possibility is that some buyers may have gambled on whether a seller would compensate for a poor rating received in the prior round. It is reasonable to think that a seller with reputation concerns might be more generous after receiving a poor rating, particularly if that poor rating was undeserved, to ensure a good rating in the current round. In contrast, the influence of Prior Good, with and without interception, was not significant. It is possible buyers’ reaction to a prior poor rating was accentuated by their concerns that the seller would take advantage of their risk position, and cheat them by returning less. Given that a prior poor rating could have affirmed these fears, skeptical buyers would have been more likely to consider a poor rating than a good rating in their investment decision.

Turning to the aggregate reputation information, we show that the total number of good ratings (Total Good) had a positive effect on the amount invested, while the total number of poor ratings (Total Poor) had a negative association. One interesting result is that the magnitude of the coefficient on the Total Good variable is approximately twice that of the Total Poor variable (4.70 versus −2.31). This could imply that, unlike the single reputation information, buyers weighted the total number of good ratings more heavily than the total number of poor ratings. This result has possible implications for reputation management strategies, implying that increasing the number of good ratings could potentially mitigate the negative effects of poor ratings.

To gain further insight into the interactions between the specific reputation information and the interception treatment, Figure 2 illustrates the impact of sellers’ reputation ratings from the prior round on buyers’ investments in the current round. The figure is constructed from the raw data and shows the average buyer investment (the y-axis) as a function of whether the seller received a poor rating in the prior round. Included is a comparison with the interception treatment to show how buyer responses to a poor rating were influenced by the additional uncertainty imposed (the x-axis).

Figure 2 Buyers’ Average Investment as a Function of Sellers’ Prior Poor Rating  
![](/api/attachments/PPFZEPSW/fulltext/images/1e1c4df9d4eed4d3cbe3ba3c3a4d5516e1285f2892c8fecc7413bb00c41bc9ab.jpg)

The graph shows that when interception was possible, a seller’s poor rating did not diminish mean investments as much as when the interception treatment was absent. This suggests an interaction effect between the poor rating and the amount of noise in the transaction environment, a relationship that is evident in Table 2.

Continuing the focus on buyers’ investment choices, Model 2 tests buyers’ decisions to initiate the transaction, which is indicated by the choice to invest any amount greater than 0. If the buyer invested \$0.00, we interpret this to mean that he or she did not want to engage the seller in that particular transaction. We specify the binary dependent variable as 1 if the buyer chose to invest a nonzero amount, and 0 otherwise. In contrast to Model 1, Model 2 includes the interaction variables Intercptn × Total Poor and Intercptn×Total Good. The model does not include the singular reputation variables (Prior Good, Prior Poor), as we expect buyers’ transaction decisions to be primarily based on sellers’ comprehensive reputation histories.

Model 2: Logistic Regression Analysis of Buyers’ Decision to Transact

$$
\begin{array}{l} \text {Logit} (\text {Transact} _ {i, t}) \\ = \beta_ {0} + \beta_ {1} \text {Intercptn} _ {i, t} + \beta_ {2} \text {Reputation} _ {i, t} \\ \quad + \beta_ {3} \text {Reputation} \times \text {Intercptn} _ {i, t} + \beta_ {4} \text {Profit Promise} _ {i, t} \\ \quad + \beta_ {5} \text {Round\_10up} _ {i, t} + \beta_ {6} \text {Total Poor} _ {i, t} + \beta_ {7} \text {Total Good} _ {i, t} \\ \quad + \beta_ {8} \text {Intercptn} \times \text {Total Poor} _ {i, t} + \beta_ {9} \text {Intercptn} \\ \quad \times \text {Total Good} _ {i, t} + \varepsilon_ {i, t}. \end{array} \tag {2}
$$

While Model 1 results showed the reputation system (Reputation) had no association with investment levels, leaving H1 unsupported, Model 2 results indicate that the reputation system had a positive association with buyers’ decisions to engage in the transaction. Results show that overall the reputation system increased the odds that buyers would initiate the transaction, suggesting that even a noisy reputation system can aid cooperation. This result does provide support for H1, which again, hypothesizes the reputation system will have a positive association with buyers’ investment levels. So while the reputation system has no association with incremental investment amounts (shown in Table 2 results), it does have a positive association with the choice to invest “something” versus “nothing.”

Figure 3 Average Proportion of Transactions as a Function of the Reputation System, with and Without Interception  
![](/api/attachments/PPFZEPSW/fulltext/images/4b5d572ef7108783b67999e5ef578565fafb34933da59c5a0dbfd2a8c35a6ef0.jpg)

Figure 3 provides greater insight into the interaction between the interception treatment and the reputation mechanism.<sup>7</sup> The x-axis indicates whether the reputation system was in effect, and the y-axis indicates the proportion of transactions initiated by buyers.

The graph shows that the reputation system increased the likelihood that buyers would initiate a transaction, while the difference with and without interception is negligible. Overall, the likelihood of buyers transacting was higher with the reputation system than without, regardless of whether additional uncertainty was imposed.

The results in Table 3, as well as the graphs constructed from the data in Figures 4(a) and 4(b) below, show that overall when interception was possible, the total number of poor ratings did not have a negative effect on the proportion of initiated transactions. Specifically, in treatments without additional uncertainty, buyers were less likely to transact when a seller had more poor ratings, supporting H3B. However, in the interception treatment, buyers appear to be more likely to give sellers the benefit of the doubt, and the proportion of initiated transactions is higher. It seems buyers may not have perceived poor ratings to be completely indicative of true behavior when it was unclear whether they were actually deserved. This result shows additional support for H5, indicating the interception did moderate the negative relationship between poor ratings and the investment decision. Results also show the total number of good ratings increased the odds of buyers initiating a transaction, indicating that buyers were generally more likely to trust those sellers who had a greater number of good ratings. This result shows additional support for H3A.

Table 3 Results of Logistic Regression for Buyers Decision to Transact

<table><tr><td>Variable</td><td></td><td>Odds</td><td>P-value</td></tr><tr><td>Interceptn</td><td> $\beta_1$ </td><td>1.77(1.00)</td><td>0.312</td></tr><tr><td>Reputation</td><td> $\beta_2$ </td><td>15.57(21.78)</td><td>0.050</td></tr><tr><td>Reputation × Interceptn</td><td> $\beta_3$ </td><td>0.08(0.13)</td><td>0.105</td></tr><tr><td>Profit Promise</td><td> $\beta_4$ </td><td>0.27(0.12)</td><td>0.002</td></tr><tr><td>Round_10up</td><td> $\beta_5$ </td><td>0.38(0.08)</td><td>0.000</td></tr><tr><td>Total Poor</td><td> $\beta_6$ </td><td>0.62(0.11)</td><td>0.008</td></tr><tr><td>Total Good</td><td> $\beta_7$ </td><td>0.93(0.21)</td><td>0.770</td></tr><tr><td>Interceptn × Total Poor</td><td> $\beta_8$ </td><td>1.43(0.27)</td><td>0.051</td></tr><tr><td>Interceptn × Total Good</td><td> $\beta_9$ </td><td>1.51(0.35)</td><td>0.072</td></tr><tr><td>Observations</td><td></td><td>596</td><td></td></tr><tr><td>Pseudo- $R^2$ </td><td></td><td>0.17</td><td></td></tr></table>

Notes. Odds calculated as exp4<sup>ˆ</sup> 5 are reported. Standard errors reported in parentheses.

The x-axis of the graphs in Figures 4(a) and 4(b) indicate whether the total proportion of good or poor ratings was below or above the mean proportion,<sup>8</sup> while the y-axis is the proportion of initiated transactions.

Figure 4(a) shows that a greater number of good ratings (x-axis) resulted in a higher instance of initiated transactions (y-axis), although this increase was less in cases where interception was possible. Figure 4(b) shows that without interception, more poor ratings lead to fewer initiated transactions, but this was not the case when interception was a factor. Specifically, Figure 4(b) shows that in the interception treatment, buyers did not react as negatively to sellers who had a greater number of poor ratings. Again, this illustrates that buyers may have given sellers with poor ratings the benefit of the doubt when it was less clear whether those ratings were truly warranted.

Figure 4(a)  
Average Proportion of Transactions as a Function of Total Number of Good Ratings  
![](/api/attachments/PPFZEPSW/fulltext/images/61e66973876eff0b1f8c6682d162912caf17e51fda18381cea4015b1f62cd46c.jpg)  
Indicates whether the proportion of total good ratings per transaction round are greater or less than the average

Figure 4(b) Average Proportion of Initiated Transactions as a Function of Total Number of Poor Ratings  
![](/api/attachments/PPFZEPSW/fulltext/images/218739f2d08a9fa38fd329f777f6c7e6c5c982cad1f965442dd835d15f458279.jpg)  
Indicates whether the proportion of total poor ratings per transaction round are greater or less than the average

Model 3 addresses whether sellers’ return choices were influenced by the reputation mechanism, specifically testing H2. We omitted those instances where buyers sent nothing, as this means that they did not initiate the transaction and by design, return amounts must be \$0.00. After eliminating these data, our number of observations was 446. Because of nonnormality of the data, we again estimated the empirical distributions for each of the OLS coefficients via bootstrapping. We drew a sample of 446 observations with replacement and repeated this 1,000 times to derive the regression parameters.

Model 3: Bootstrapped OLS Regression of Seller Returns

$$
\begin{array}{l} \text {Returned} _ {i, t} \\ = \beta_ {0} + \beta_ {1} \text {Intercptn} _ {i, t} + \beta_ {2} \text {Reputation} _ {i, t} \\ \quad + \beta_ {3} \text {Reputation} \times \text {Intercptn} _ {i, t} + \beta_ {4} \text {Round\_10up} _ {i, t} \\ \quad + \beta_ {5} \text {Invested} _ {i, t} + \varepsilon_ {i, t}. \end{array}\tag{3}
$$

Our results in Table 4 show that returns were higher with the reputation system (Reputation) employed and no interception (i.e., $\beta _ { 2 } = 3 0 . 4 8 ,$ , p-value = 00001), showing support for H2. Results also show that the amount invested by buyers (Invested) is significant and positive $( \mathrm { i . e . , ~ } \beta _ { 5 } = 1 . 3 8 , \ p \mathrm { - v a l u e = 0 . 0 0 0 ) }$ , indicating that reciprocation explains much of the sellers’ return decisions. This finding implies that when buyers invested larger amounts, sellers were more likely to positively reciprocate. Positive reciprocity can be defined as the impulse or the desire to be kind to those who have been kind to us (Fehr et al. 1997) and has been observed in trust games and gift exchange games (Fehr et al. 1997, Berg et al. 1995). Finding that sellers’ return behaviors are driven, in part, by the desire to reciprocate is consistent with prior studies, showing when first movers send greater amounts, they are rewarded with larger returns from second movers.

Table 4 Results of Bootstrapped OLS Regression for Sellers’ Return

<table><tr><td>Variable</td><td></td><td>Coefficient</td><td>P-value</td></tr><tr><td>Constant</td><td> $\beta_1$ </td><td>-13.94(8.47)</td><td>0.000</td></tr><tr><td>Intercptn</td><td> $\beta_2$ </td><td>4.64(15.50)</td><td>0.713</td></tr><tr><td>Reputation</td><td> $\beta_3$ </td><td>30.48(13.00)</td><td>0.001</td></tr><tr><td>Reputation × Intercptn</td><td> $\beta_4$ </td><td>-8.33(18.84)</td><td>0.844</td></tr><tr><td>Round_10up</td><td> $\beta_4$ </td><td>-7.08(5.55)</td><td>0.072</td></tr><tr><td>Invested</td><td> $\beta_5$ </td><td>1.38(0.12)</td><td>0.000</td></tr><tr><td>Observations</td><td></td><td>446</td><td>446</td></tr><tr><td> $R^2/Adjusted$ </td><td></td><td>0.38</td><td></td></tr></table>

Notes. Bootstrapped coefficients and p-values reported. Standard errors reported in parentheses.

Finally, we test whether the reputation system had an influence on sellers’ choice to return truthfully, in relation to the amounts they initially promised. We interpret a truthful return to mean the seller returned an amount equal to or greater than what was promised. The dependent variable TRU Return is binary, and is coded depending on whether the seller returned an amount greater than or equal to what was promised (1), or less than promised (0).

Model 4: Logistic Regression of Sellers’ Truthful Return

$$
\begin{array}{l} \text { Logit } (T R U \text { Return } _ {i, t}) \\ = \beta_ {0} + \beta_ {1} \text { Intercepttn } _ {i, t} + \beta_ {2} \text { Reputation } _ {i, t} \\ \quad + \beta_ {3} \text { Reputation } \times \text { Intercepttn } _ {i, t} + \beta_ {4} \text { Round\_10up } _ {i, t} \\ \quad + \beta_ {5} \text { Invested } _ {i, t} + \beta_ {6} \text { Total   Poor } _ {i, t} \\ \quad + \beta_ {7} \text { Total   Good } _ {i, t} + \varepsilon i, t. \end{array} \tag {4}
$$

Figure 5 Average Proportion of Greater or Equal Returns as a Function of the Reputation System, with and Without Interception  
![](/api/attachments/PPFZEPSW/fulltext/images/4ac4f01f67af761e4ed3da08aba67f1cf083cf2fe8271918488feef1d8af5462.jpg)

Results show the odds of a seller making a truthful return increased when the reputation system (Reputation) was present. This result provides additional support for H2, indicating the reputation system had a positive impact on seller return decisions. Figure 5 further illustrates the effect of the reputation system on trustworthy returns.

The graph shows that in cases with and without uncertainty, sellers were more likely to make trustworthy returns when the reputation system was in place; however, the difference in trustworthy returns between the interception and no interception treatments was negligible.

Table 5 also shows the aggregate reputation variables, Total Poor and Total Good, are significant in the predicted directions, suggesting aggregate reputation information may help buyers evaluate sellers’ propensity for a trustworthy return (or lack thereof). For each unit increase in the amount invested (Invested), the odds the seller would return an amount greater than promised is approximately 1. A plausible explanation is that often sellers promised buyers that if they invested the full amount (\$1), they would split the total profit to achieve a distributionally fair return (\$2). Therefore, in many cases when buyers invested the maximum amount possible, they received return amounts that were almost always equal to, but rarely more than, the split that was promised.

Table 5 Results Logistic Regression for Truthful Return

<table><tr><td>Variable</td><td></td><td>Odds</td><td>P-value</td></tr><tr><td>Interceptn</td><td> $\beta_1$ </td><td>2.450(0.810)</td><td>0.006</td></tr><tr><td>Reputation</td><td> $\beta_2$ </td><td>5.710(2.290)</td><td>0.001</td></tr><tr><td>Reputation × Interceptn</td><td> $\beta_3$ </td><td>0.430(0.230)</td><td>0.109</td></tr><tr><td>Round_10up</td><td> $\beta_4$ </td><td>0.730(0.210)</td><td>0.266</td></tr><tr><td>Invested</td><td> $\beta_5$ </td><td>0.970(0.003)</td><td>0.000</td></tr><tr><td>Total Poor</td><td> $\beta_6$ </td><td>0.830(0.040)</td><td>0.001</td></tr><tr><td>Total Good</td><td> $\beta_7$ </td><td>1.250(0.080)</td><td>0.001</td></tr><tr><td>Pseudo- $R^2$ </td><td></td><td>0.200</td><td></td></tr></table>

Notes. Odds calculated as exp4hat 5 are reported. Standard errors reported in parentheses.

## 5.2. Ratings and Reputation Formation

Model 5 addresses buyers rating decisions, and specifically tests H4A, H4B, and H6. The dependent variable Rate is specified at three levels depending on whether the rating assigned to the seller was good (3), neutral (2), or poor (1). The model is tested with an ordinal logistic regression. The neutral rating, and the instances where return amounts equal what was promised, are each specified as reference groups.

Model 5: Ordinal Logistic Regression of Buyers’ Rating Decision

$$
\begin{array}{l} \text { Ordinal   Logit } (R a t e _ {i, t}) \\ = \beta_ {0} + \beta_ {1} \text { Intercptn } _ {i, t} + \beta_ {2} \text { Return   Less } _ {i, t} \\ \quad + \beta_ {3} \text { Return   Greater } _ {i, t} + \beta_ {4} \text { Intercptn } \times \text { Return   Less } _ {i, t} \\ \quad + \beta_ {5} \text { Intercptn } \times \text { Return   Greater } _ {i, t} + \varepsilon_ {i, t}. \end{array} \tag {5}
$$

Additional variables for Model 5 are Return Less, indicating whether the seller returned less than promised, and Return Greater, indicating whether the seller returned more than promised. Both are binary and are coded as 1 if true, and 0 otherwise. Results in Table 6 show that without interception, when sellers made returns less than promised, they were more likely to receive a poor rating, relative to when interception was possible. To clarify, Figure 6 provides additional insight into the interaction effect between the interception and sellers truthful returns. The figure is calculated from the raw data and shows the likelihood of good and poor rating decisions as a function of seller returns.

Table 6 Results of Ordinal Logistic Regression for Ratings Assignment

<table><tr><td>Variable</td><td></td><td>Odds</td><td>P-value</td></tr><tr><td> $Intercptn$ </td><td> $\beta_1$ </td><td>2.51(0.54)</td><td>0.000</td></tr><tr><td>Return Less</td><td> $\beta_2$ </td><td>0.28(0.09)</td><td>0.000</td></tr><tr><td>Return Greater</td><td> $\beta_3$ </td><td>7.48(4.18)</td><td>0.000</td></tr><tr><td> $Intercptn \times Return Less$ </td><td> $\beta_4$ </td><td>2.46(1.09)</td><td>0.042</td></tr><tr><td> $Intercptn \times Return Greater$ </td><td> $\beta_5$ </td><td>0.90(0.70)</td><td>0.896</td></tr><tr><td>Observations</td><td></td><td>350</td><td></td></tr><tr><td> $Pseudo-R^2$ </td><td></td><td>0.15</td><td></td></tr></table>

Notes. Odds calculated as exp4<sup>ˆ</sup> 5 are reported. Standard errors reported in parentheses.

Figure 6 Likelihood of a Poor Rating When Return Is Less Than Promised  
![](/api/attachments/PPFZEPSW/fulltext/images/140375e27df52e56f8475fa0c183b50b5da819e84562eefc8b620ad5d51cb6b6.jpg)

Figure 6 suggests that buyers were less likely to punish sellers with a poor rating when interception was possible. Specifically, it seems that when additional uncertainty was imposed, some buyers who experienced low returns relative to the promise gave that seller the benefit of the doubt and did not always respond with a poor rating.

## 6. Discussion

This paper addresses three questions. The first asks how reputation ratings are assigned, and thus how reputations are formed, in online markets. We show that expectations and reference points may play a prominent role in rating behaviors; when expectations are not met, poor ratings ensue. However, we also show that in spite of unmet expectations, poor ratings may be less likely when buyers are not certain whether sellers intended the disappointing outcome. Next, we investigate the economic and behavioral effects of different reputation information. We find that the effects of the aggregate reputation ratings differ from the singular ratings. Aggregate ratings impacted buyers’ willingness to engage in the transaction, while single ratings were more relevant to buyers’ choices of how much to invest. We also find that a single poor rating is weighted differently than a single good rating, and poor ratings were less likely to be punished when intentions were not known with certainty. Third, we ask how uncertainty affects the functionality of the reputation system. We find an interaction between the type of reputation rating and the interception treatment. In particular, poor ratings had a less detrimental effect on buyers’ trust when additional uncertainty was imposed.

We inform practitioners by showing that while a less noisy reputation system is preferred, even with a

Shown to buyers

Shown to sellers

high level of noise, a reputation system can still provide benefits to cooperation. Noting the differences in how market participants perceive different types of reputation has implications for reputation management. Finding that a single poor rating in some cases is weighted more heavily than a single good rating, suggests a negative shock to a reputation may impact the trust of future buyers or clients more than a positive shock. Our findings also indicate that sellers may want to be aware of buyer expectations to secure a good rating. However, because this is a difficult if not impossible task, another option is for sellers to manage expectations by representing their product or service as accurately as possible. It does not benefit sellers to overstate the quality of their product, as their reputation will likely suffer when the lower quality good is received.

One limitation of this study is that experimental methods tend to impose a strictly controlled environment, and generalization of findings should be done with care. However, this limitation should also be viewed as a strength of the methodology. Using the laboratory to strip away many of the contextual cues that could influence behavior in a field setting allows us to isolate the individual’s decision-making behavior. Another limitation of this work is that simplifying assumptions were made about the transaction environment, and the threat of litigation to enforce cooperation is not considered. The experiment also does not account for the possibility of explanatory text accompanying ratings scores, which is becoming more common in electronic reputation systems and is a logical extension of this work.

Finally, if one’s goal were to make more comprehensive inferences about multiple levels of uncertainty, it would be necessary to extend our uncertainty treatment to include additional interception probabilities. Thus, one direct extension of this work is to further investigate the effects of different levels of noise on the reputation system. We impose a relatively high probability of interception to establish a directional effect of uncertainty. It could be beneficial to manipulate this probability of interception to determine if there is some acceptable level of noise where the benefits of good ratings are not decreased, but the benefits to cooperation remain. Such findings could be of interest to future reputation system maintenance and design.

## 7. Conclusion

Electronic commerce has become a mainstream business practice, yet the information asymmetry that exists between buyers and sellers in these markets implies participation is not without risk. The questions addressed in this study are designed to expose factors that impact the rating decisions of market participants, and the effects of uncertainty on these decisions. Understanding how reputation ratings are assigned provides insight into how buyer and seller actions might impact online reputations. To date, little attention has been given to the inherent uncertainty present in the online transaction environment, and its effect on the functionality of electronic reputation systems. Our study is one of the first to address this issue with a laboratory setting designed to approximate an online transaction. Finally, much of the work on online reputation systems is either theoretical or empirical, and game-theoretic experiments such as this one provide additional measures that contribute to the existing literature. We believe our findings are important to online mechanism design, while ultimately helping researchers and practitioners identify more precise ways of measuring, and accounting for, the economic value of a reputation system.

## Appendix. Experiment Screen Shots

Screen 1  
![](/api/attachments/PPFZEPSW/fulltext/images/0d6fe57079e14ec32f751109bf7c017bc92ea8cdc5e8d2e2d70009156db372ff.jpg)  
Note. The nonbinding announcement where sellers fill out their proposed return to buyers.

Screen 2  
![](/api/attachments/PPFZEPSW/fulltext/images/7470d19c573c38d316eb39a325ca522470e714cea3fd7ab2ea1d04b32b989bfa.jpg)  
Note. Buyer sees seller’s aggregate reputation score and round by round ratings then indicates how much they will invest.

Screen 3 Shown to sellers  
![](/api/attachments/PPFZEPSW/fulltext/images/c5c683f77b8f49c1f690ada68adf43de66b1bf13d08524c45c513589151c813b.jpg)  
Note. Seller sees how much the buyer has invested and then decides how much he would like to return to the buyer.

## Screen 4 Shown to buyers

![](/api/attachments/PPFZEPSW/fulltext/images/6d5b4f74ecc8b5b3667215d93481bc9324a79ad8fe5490bf836126e7887525b0.jpg)  
Note. Buyer sees the exchange history and their return from the seller. In both cases, the buyer is reminded that interception was possible when applicable by displaying the circled text only in those instances.

## Screen 5 Shown to sellers

![](/api/attachments/PPFZEPSW/fulltext/images/d30d6b9378002c24bf377b490a66b4a0e59204fdc8b026b6a5d68614636e99d3.jpg)  
Note. Sellers see the transaction history, their most recent reputation score, and their reputation history.

## References

Akerlof, G. 1970. The market for “lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3) 488–500.

Ba, S. 2001. Establishing online trust through a community responsibility system. Decision Support Systems 31(3) 323–336.

Ba, S., P. Pavlou. 2002. Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quart. 26(3) 243–268.

Bell, D. 1982. Regret in decision making under uncertainty. Oper. Res. 30(5) 961–981.

Bell, D. 1985. Putting a premium on regret. Management Sci. 31(1) 117–122.

Bendor, J., R. M. Kramer, S. Stout. 1991. When in doubt 0 0 0 cooperation in a noisy prisoner’s dilemma. J. Conflict Resolution 35(4) 691–719.

Berg, J., J. Dickhaut, K. McCabe. 1995. Trust, reciprocity, and social history. Games Econom. Behavior 10(1) 122–142.

Bolton, G., E. Katok, A. Ockenfels. 2004. How effective are electronic reputation mechanisms? Management Sci. 50(11) 1587–1602.

Bolton, G., E. Katok, A. Ockenfels. 2005. Cooperation among strangers with limited information about reputation. J. Public Econom. 89(8) 1457–1468.

Camerer, C., K. Weigelt. 1988. Experimental tests of a sequential equilibrium reputation model. Econometrica 56(1) 1–36.

Casari, M., J. C. Ham, J. H. Kagel. 2007. Selection bias, demographic effects, and ability effects in common value auction experiments. Amer. Econom. Rev. 97(4) 1278–1304.

Cripps, M., E. Dekel, W. Pesendorfer. 2005. Reputation with equal discounting in repeated games with strictly conflicting interests. J. Econom. Theory 121(2) 259–272.

Cripps, M., G. Mailath, L. Samuelson. 2004. Imperfect monitoring and impermanent reputations. Econometrica 72(2) 407–432.

Dellarocas, C. 2003. The digitization of word-of-mouth: Promise and challenges of online reputation mechanisms. Management Sci. 49(10) 1407–1424.

Dellarocas, C. 2005. Reputation mechanism design in online trading environments with pure moral hazard. Inform. Systems Res. 16(2) 209–230.

Dewan, S., V. Hsu. 2004. Adverse selection in electronic markets: Evidence from online stamp auctions. J. Indust. Econom. 52(4) 497–516.

Fehr, E., S. Gächter, G. Kirchsteiger. 1997. Reciprocity as a contract enforcement device: Experimental evidence. Econometrica 65(4) 833–860.

Fudenberg, D., E. Maskin. 1990. Evolution and cooperation in noisy repeated games. Amer. Econom. Rev. 80(2) 274–279.

Grief, A. 1993. Contract enforceability and economic institutions in early trade: The Maghribi traders’ coalition. Amer. Econom. Rev. 83(3) 525–548.

Hirshleifer, D., S. Teoh. 2003. Limited attention, information disclosure, and financial reporting. J. Accounting Econom. 36(1–3) 337–386.

Hoffman, E., K. McCabe, V. Smith. 1998. Behavioral foundations of reciprocity: Experimental economics and evolutionary psychology. Econom. Inquiry 36(3) 335–352.

Jung, Y., J. Kagel, D. Levin. 1994. On the existence of predatory pricing: An experimental study of reputation and entry deterrence in the chain store game. RAND J. Econom. 25(1) 72–93.

Kauffman, R., C. Wood. 2005. The effects of shilling on final bid prices in online auctions. Electronic Commerce Res. Appl. 4(1) 21–34.

King, R. 1996. Reputation formation of reliable reporting: An experimental investigation. Accounting Rev. 71(3) 375–396.

Kreps, D., R. Wilson. 1982. Reputation and imperfect information. J. Econom. Theory 27(2) 253–279.

Kreps, D., P. Milgrom, J. Roberts, R. Wilson. 1982. Rational cooperation in the finitely repeated prisoners’ dilemma. J. Econom. Theory 27(2) 245–252.

Loomes, G., R. Sugden. 1982. Regret theory: An alternative theory of rational choice under uncertainty. Econom. J. 92(368) 805–824.

Lucking-Reiley, D. 2000. Auctions on the Internet: What’s being auctioned, and how? J. Indust. Econom. 48(3) 227–252.

Marschak, T., R. Selten. 1978. Restabilizing responses, inertia supergames and oligopolistic equilibria. Quart. J. Econom. 92(1) 71–93.

Melnik, M., J. Alm. 2002. Does a seller’s ecommerce reputation matter? Evidence from eBay auctions. J. Indust. Econom. 50(3) 337–349.

Milgrom, P., J. Roberts. 1982. Predation, reputation and entry deterrence. J. Econom. Theory 27(2) 280–312.

Resnick, P., R. Zeckhauser. 2002. Trust among strangers in Internet transactions: Empirical analysis of eBay’s reputation system. The Economics of the Internet and E-Commerce. JAI Press, Greenwich, CT, 127–157.

Resnick, P., K. Kuwabara, R. Zeckhauser, E. Friedman. 2000. Reputation systems. Comm. ACM 43(12) 45–48.

Resnick, P., R. Zeckhauser, J. Swanson, K. Lockwood. 2006. The value of reputation on eBay: A controlled experiment. Experiment. Econom. 9(2) 79–101.

Sainty, B. 1999. Achieving greater cooperation in a noisy prisoner’s dilemma: An experimental investigation. J. Econom. Behavior Organ. 39(4) 421–435.

Schwartz, S. T., R. A. Young, K. Zvinakis. 2000. Reputation without repeated interaction: A role for public disclosures. Rev. Accounting Stud. 5(4) 351–375.

Selten, R. 1975. A reexamination of the perfectness concept for equilibrium points in extensive games. Internat. J. Game Theory 4(1) 25–55.

Shapiro, C. 1983. Premiums for high quality products as returns to reputations. Quart. J. Econom. 98(4) 659–680.

Wolf, J., H. Arkes, W. Muhanna. 2008. The power of touch: An examination of the effect of duration of physical contact on the valuation of objects. Judgment Decision Making 3(6) 253–279.
