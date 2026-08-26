---
otero_id: 26724
otero_key: "68HZBXXK"
title: "Alternative Securities Trading Systems: Tests and Regulatory Implications of the Adoption of Technology"
authors: "Eric K. Clemons; Bruce W. Weber"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.2.163"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/68HZBXXK/fulltext/images/9c48f0dc1eb915b923ea8811345f0f36677c59717fc6039fdac5eacdf66b3965.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Alternative Securities Trading Systems: Tests and Regulatory Implications of the Adoption of Technology

Eric K. Clemons, Bruce W. Weber,

To cite this article:

Eric K. Clemons, Bruce W. Weber, (1996) Alternative Securities Trading Systems: Tests and Regulatory Implications of the Adoption of Technology. Information Systems Research 7(2):163-188. http://dx.doi.org/10.1287/isre.7.2.163

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/68HZBXXK/fulltext/images/031ef27457a826f8a0b9d28d535992c787694d2c941aea98ba53bc0c6e52ec73.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Alternative Securities Trading Systems: Tests and Regulatory Implications of the Adoption of Technology\*

Eric K. Clemons • Bruce W. Weber

Department of Operations and Information Management, Steinberg Hall-Dietrich Hall 1300, The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104-6366
clemons@wharton.upenn.edu

Department of Information Systems, Stern School of Business,
New York University, 44 West 4th Street, New York, New York 10012-1126
bweber@stern.nyu.edu

Reasons for the mixed reactions to today's electronic off-exchange trading systems are examined, and regulatory implications are explored. Information technology (IT) could provide more automated markets, which have lower costs. Yet for an electronic trading system to form a liquid and widely used market, a sufficient number of traders would need to make a transition away from established trading venues and to this alternative way of trading. This transition may not actually occur for a variety of reasons. Two tests are performed of the feasibility and the desirability of transitions to new markets. In the first test, traders in a series of economic experiments demonstrate an ability to make a transition and develop a critical mass of trading activity in a newly opened market. In the second test, simulation is used to compare the floor-based specialist auction in place in most U.S. stock exchanges today to a disintermediated alternative employing screen-based order matching. The results indicate that reducing the role of dealer-intermediaries can actually diminish important measures of market quality. Our findings suggest that the low trading volumes on many off-exchange systems do not result from traders' inability to break away from established trading floors. Rather, today's off-exchange trading systems are not uniformly superior to the trading mechanisms of traditional exchanges. Thus, regulatory actions favoring off-exchange trading systems are not warranted; but, improved designs for IT-based trading mechanisms are needed, and when these are available, they are likely to win significant trading volume from established exchanges.

(Electronic Markets; Trading Systems; Experimental Economics; Technology Adoption; Financial Market Simulation)

## 1. Introduction

There is considerable confusion among regulators and participants in the financial services industry about the potential impact that may be produced by electronic alternatives to established securities markets such as the New York Stock Exchange (NYSE). $^{1}$ Securities markets concentrate liquidity, thereby enabling buyers and sellers to meet and to transfer assets more quickly and more efficiently. While computerization has improved elements of information processing in markets, most trading mechanisms operate through a mix of automated and manual procedures. Information technology creates a range of new possibilities for the organization of securities markets (Garbade 1978, Schwartz 1991, Domowitz 1992), and can greatly facilitate access to prices and to the market itself. Although it would initially appear a matter of implementing appropriate market technology, there are unresolved issues about which market mechanism is superior (Beja and Hakannson 1979, Cohen et al. 1986, Stoll 1992).

Trading is a complex activity that defies simple approaches to automation, and traditional research methods of finance are not fully developed for identifying the consequences of implementing major financial information systems such as electronic stock markets. A possibility that is worrisome to regulators and investors is that a new electronic market may be preferable and socially desirable, but that the transition to such a system may be in some way blocked by the inertia from established markets. In this case—existence of a superior alternative but a stable equilibrium blocking the transition—regulatory policies may be needed to bring about a transition from the entrenched market to the alternative system. The resolution of these issues is clearly important to regulators, securities markets, and financial services firms.

This paper applies experimental economics and computer simulation to evaluate the impact of electronic trading systems that are poised to draw trading volume away from today's established securities markets. We perform tests on two necessary conditions for the successful adoption of an alternative trading system. First, traders today freely choose the market to which they send their orders; in the absence of regulatory intervention, it must be possible for a competing mechanism to draw trading volume away from an established market. Using experimental economics, we test whether subjects in a laboratory setting can collectively move their trading activity to a lower-cost, but initially illiquid, market. Second, it must be demonstrated that a proposed electronic market design does in fact improve recognized measures of market quality such as bid-ask spreads. $^{2}$ We test for market quality differences using simulation models of trading in a traditional market structure and in a prevalent electronic market system. Both conditions for adoption are investigated.

## 2. Barriers to Adoption of Electronic Trading Systems

Many different trading mechanisms are used in financial markets around the world to transform buy and sell orders into prices and executed trades. $^{3}$ Due to innovations in trading and communications systems, and in response to investor demand, securities can now be traded in multiple markets, and markets increasingly compete with one another to attract trading volumes. $^{4}$ Additionally, in recent years, established markets have begun to face competition for trading activity from several electronic trading alternatives. $^{5}$ However, alternative electronic trading systems that offer price discovery and automatic execution $^{6}$ of orders have not yet attracted much trading activity from major stock exchanges. Two hypotheses are tested in this paper for why liquidity has remained on established markets. $^{7}$ The first is that the initial illiquidity of a new market itself prevents the development of liquidity needed for transitions to alternative trading systems. The second is that alternative electronic markets do not improve market quality by lowering overall transactions costs. Either alone would be sufficient to explain the lack of adoption of alternative electronic trading mechanisms. However, it is useful to understand both in order to discern the sources of resistance and thus to determine appropriate strategies and regulatory policies.

## 2.1. Problem Background

The question of whether to move from traditional markets, such as the NYSE specialist market, to automatic trading systems is highly controversial. Of fundamental importance is the question of efficiency and social welfare: Is the service provided by a specialist-intermediary worth its cost? To critics, the NYSE specialists' revenues, which were \$437 million in 1992, \$566 million in 1993, and \$606 million in 1994 for the 40 NYSE specialist firms, represent a cost imposed on investors by the NYSE's market structure.

While exchanges have modernized, and systems have been implemented to speed the flow of trading orders and of market information, critical aspects of the trading process continue to require manual intervention and exchange personnel in most major securities markets. Causes for slow IT adoption are unclear and predictions made by experts over twenty years ago about the extent of automation in the securities markets of the future have proven overly optimistic. Proposals for "black box" trading to compete with and eventually displace established markets have languished. $^{8}$ Loosely based on the proposals, the National Securities Trading System (NSTS), an on-line order matching system running on a computer in New Jersey, was implemented by the Cincinnati Stock Exchange (CSE) in 1978. NSTS provided a means for CSE members to enter competing bids and offers to those available on the NYSE floor and to have those quotes available for electronic execution. Supporters expected that a considerable share of volume would occur through the system, but its share of the trading volume in the stocks it handled rose to 2.0%, but then fell to 0.6% by 1983. On the rare occasions when a CSE quote was better than that available on the NYSE the floor traders would match the CSE quote, but few orders were attracted to the CSE. Davis (1985) noted "the failure of the National Securities Trading System (NSTS) to capture more than a tiny portion of trading volume has undoubtedly been a profound disappointment to black-box [electronic market system] advocates."

Despite the perseverance of manual trading practices in major stock markets, there appear to be several advantages to screen-based market systems. Some observers believe that “in the long run, automated trading systems offer a richer mixture of the market information and the anonymity necessary for trading than either the crowd or the telephone” (Cohen, et al. 1986, p. 66). Screen markets can support 24-hour, global trading more easily. Such markets usually function without designated intermediaries, such as the NYSE specialist;

investors buy and sell directly with one another, avoiding specialists and their dealing margins. Floor markets require specialists or dealers, and the presence of a floor trading staff.

In evaluating traditional market structures, there are also issues of privilege and fairness because specialists have preferred access to information. They see the entire order book—i.e., the list of pending customer orders, including price and quantity—and they can gauge the relative strength of buying and selling interest. Traders off the NYSE floor see just the best buy and sell orders or quotes. Critics argue this is an unfair advantage, and that specialists can trade more intelligently than the rest of the market. $^{9}$ Proponents of the specialist system maintain that without this informational subsidy, specialists would not perform their price stabilization function, i.e., intervening in trading to stabilize prices when there is a temporary supply-demand imbalance. $^{10}$ Furthermore, specialist activities are closely monitored, and they are restricted from certain trading activities, and obligated to participate in other trades.

## 2.2. Research Hypotheses

This paper tests the validity of two hypotheses for why major markets have not lost much liquidity to electronic trading systems. The first hypothesis is that unaided transitions to alternative markets are not possible. Because of the risk of illiquidity away from the established market, $^{11}$ traders may be incapable of making a transition to an alternative market. That is, while transitions might be optimal if all traders simultaneously adopted the new market, any individual trader might experience losses if he or she adopts too early. If such transitions are unlikely, the prospects for the adoption of an advantageous trading system are weakened. This apparent contradiction between individuals' behavior in a group setting and their profit maximizing behavior if they could be certain of other individuals' behavior makes market transition questions particularly interesting to exchange officials, securities firms, and regulators. The evidence to date is that in cases where trading systems have competed with established markets, the established markets have typically retained the dominant share of trading, and the electronic market remained an illiquid alternative. As Amihud et al. (1985, p. 6) point out, "despite developments and the inherent power of electronic technology, traders have remained wary of operating in a computerized system, especially with regard to equity orders in the major trading arenas." The "central market defense," which maintains that liquid markets will attract trading simply because they are more liquid, appears to hold even in the presence of increasingly advanced market technology.

The second hypothesis is that alternative electronic markets are not desirable; i.e. they do not lead to improved market quality or lower overall transactions costs. As Amihud et al. (1985, p. 6) note, “given the economic complexities of trading, we have not yet learned how to best structure a computerized system.” Such systems are a significant departure from the microstructure of U.S. stockmarkets, but it remains an open question whether screen-based order matching systems can improve the quality of the market. It is possible that “competition in the free market might be relied on to bid away excess profits, but competition alone does not assure that the [securities trading] industry will ever achieve, or even evolve toward the most efficient competitive structure . . . we need discretionary planning [and] to get such planning we must look to the regulators” (ibid, p. 9). Industry-wide coordination efforts and regulatory intervention may be required to reach the most beneficial organization of securities trading.

Either of these two hypotheses is sufficient for explaining the slow adoption of electronic trading mechanisms. In two independent studies, using simulation and laboratory experimental economics, we test these explanations.

## 3. Laboratory Experiments on Transitions to Alternative Markets

To examine the feasibility of liquidity developing in an alternative trading mechanism, we use a series of laboratory decision-making experiments. Although automated markets are technically feasible, trading systems do not create markets or their liquidity; public buying and selling, and in some cases dealers or specialists, are required to create liquidity and a viable market. A study undertaken by the U.S. Congressional Office of Technology Assessment (OTA) in 1989, began with a strong presumption on the part of the OTA that historical precedent and central market advantages allowed established U.S. markets to retain the majority of trading volumes, and prevented superior off-exchange trading systems from attracting activity. Despite the perceived benefits of computerized markets, a transition to an alternative form of trading is not assured; the evidence is that such transitions in actual market settings are rare. $^{12}$ In many other cases, screen-based trading mechanisms that appeared to offer advantages were ignored by traders and remained illiquid. Ariel (1974) in the U.K. for screen-based order matching, and Intex (1984), a Bermuda-based automated futures exchange, are examples.

As the finance field has chronicled, the dominance of an established market, it appears, is capable of preventing new, potentially superior trading mechanisms from attracting a critical mass of activity. When traders face the risk of illiquidity in a new market they may not shift their trading there even if the new market offers lower trading costs. Total costs—trading cost plus market impact—may favor the established market. In particular, a new market will remain illiquid when traders conjecture that other traders are unlikely to switch their activities. To advocates of alternative, screen-based markets, traders often appear to be trapped in an inferior equilibrium, with the majority of trading activity remaining in an established, but antiquated marketplace. We examine this presumption in experiments that test whether traders in a group are capable of making a transition of their trading activity to a lower-cost alternative market without explicit direction or coordination. The concentration of all trading in the low-cost market is a Pareto preferred outcome, but achieving it is not certain. Because there can be multiple Nash equilibria, there is no clear prediction of the outcome of inter-market competition.

In order to derive results about choices between competing technologies with participation or network externalities (e.g., VHS versus Betamax video standards), economic theorists make strong assumptions about individual decision making and coordination. For instance, Katz and Shapiro (1986, p. 827) state:

"We assume that when there are multiple equilibria, consumers buying in the same period can coordinate their purchase decisions to choose the outcome that is Pareto preferred."

Experimental economists, who test such behavioral assumptions, find that Pareto preferred outcomes are rare in coordination problems. The nature of the problem posed by observable failure to coordinate is expressed by Straub (1995):

it is possible that the players may fail to obtain an equilibrium even if each player selects an action that supports an equilibrium because each player may choose an action that supports a different equilibrium. Even if the players coordinate their actions to implement a particular equilibrium, that equilibrium may yield all players lower payoffs than an alternative equilibrium. Even in the simplest games to exhibit multiple Nash equilibria (coordination problems and battle of the sexes) economists and game theorists have yet to reach consensus regarding the predicted outcome, and the solution to this problem has been elusive."

Thus, although payoff-dominated outcomes (i.e., inferior outcomes) are surprising, there is simply no a priori understanding that would allow prediction concerning the expected outcome of inter-market competition, or prediction of the outcome of competition among alternative equilibria. As the question of where trading will take place in the future becomes more important and as the technological possibilities grow more numerous and diverse, the ultimate determinants—individual but interdependent trader choices—need to be explored experimentally.

## 3.1. Experimental Design

Following Smith's principles (1982) for valid economic experimentation, we designed a laboratory experiment to test for liquidity transitions that may occur when an alternative trading mechanism competes with an established market. We conducted eight separate experiments, labelled Experiments 1–7 and Experiment T. In Experiments 1–7, subjects were undergraduate and graduate students at the University of Pennsylvania. Experiment T was an abbreviated experiment that was conducted with eight floor traders from New York Stock Exchange member firms. In all experiments, eight participants were randomly assigned to either be a buyer or a seller. There were four in each group. In a decision round, each trader decided how to divide 10 shares across two available markets. Submitted orders could be any integer between 0 and 10 but had to total to 10. The experiment was made up of two parts that each consisted of 12 rounds. Two sample rounds of trading were conducted prior to the experiment to ensure subjects understood their choice and the characteristics of the payoff they would receive. Once all traders correctly calculated the earnings from their choices in these example rounds, the experiment began. The experiment instructions and record sheets are included as an appendix.

The experimental sessions lasted about two hours, and depending on their trading performance, subjects earned between \$13 and \$29. The experimental design creates incentives comparable to those in actual securities markets. In each experiment, a trader handling an order needs to consider the impact his or her order will have on the price at which it executes, much as he or she would have to do with a large buy or sell order for real securities. When a trader chooses among multiple markets for real securities, the determinants of price are the balance of buying and selling interest in a market and the overall liquidity of a market. A market with an excess of supply (shares to sell) will see the price fall, lowering profits of sellers but raising profits of buyers, who have the opportunity to buy in a “buyers’ market.” Similarly, too many orders to buy will raise the price and lower buyers’ profits but raise sellers’ earnings. The magnitude of the price movement for a particular supply-demand imbalance is determined by the liquidity of the market. A more liquid market will dampen price movements, while in an illiquid market, prices may react strongly to even small order imbalances. The earnings functions in the experiments incorporate these factors that influence the profit from a trade in an actual securities market.

The treatment variable under experimenter control is the cost difference between the two markets. Differences in costs between the two markets lead to different profit potentials. The treatment variable is applied at two levels. In Experiments 1–4 and Experiment T, subjects can earn 40% higher profits and in Experiments 5–7 they can earn 10% higher profits. Market profitability for the traders is endogenously determined by the subjects' decisions about where to send their trading orders. The profitability of subjects' trading decisions thus includes costs (the treatment variable) and any costs imposed by the illiquidity of the markets that they send their orders to (determined by subject choices). The outcome variable is the division of trading volume between the two markets.

The game created by the payoff functions is a coordination game, which has multiple conjectural equilibria. Tacit coordination is necessary to achieve the preferred, "payoff-dominant" equilibrium. Any

Table 1 Example Earnings Calculation

In a round, if Market X has 30 shares to buy and 25 shares to sell, profits per share in Market X will be:

Buyers: 10¢ -60[(30 - 25)/(30 + 25)]¢ = 10¢ - 5 5¢ = 4.5¢

Sellers: $10\pmb{\varepsilon} + 30[(30 - 25) / (30 + 25)]\pmb{\varepsilon} = 10\pmb{\varepsilon} + 2.7\pmb{\varepsilon} = 12.7\pmb{\varepsilon}$

Profits per share in Market Y (10 shares to buy and 15 shares to sell) will be:

Buyers. $10\epsilon - 30[(10 - 15)/(10 + 15)]\epsilon = 10\epsilon + 6.0\epsilon = 16.0\epsilon$

Sellers: $10\pmb{\varepsilon} + 60[(10 - 15) / (10 + 15)]\pmb{\varepsilon} = 10\pmb{\varepsilon} - 12.0\pmb{\varepsilon} = -2.0\pmb{\varepsilon}$

Hence, a buyer that submitted 6 shares to Market X and 4 shares to Market Y will have earnings in the period of 6(4.5)€ + 4(16.0)€ = 27€ + 64€ = \$0.91

division of trading activity across the two markets (e.g., 60%-40%) is potentially a self-reinforcing Nash equilibrium. The optimal strategy for traders is to divide their orders in the same proportion as they conjecture that trading activity will be split across the two markets. If you believe one market will attract 60% of trading in a round, your best response is to submit 6 there and 4 to the other. Decisions are influenced by these conjectures and by the proportion of orders in the new market in the prior rounds of the experiment.

Part I. Subjects chose how to divide their order across two markets—Market X and Market Y—with the same earnings function:

Buyers' Profit per Share Market X

$$
= 1 0 \varphi - \Delta [ (B _ {x} - S _ {x}) / (B _ {x} + S _ {x}) ] \varphi ,
$$

Sellers' Profit per Share Market X

$$
= 1 0 \varphi + \Delta [ (B _ {x} - S _ {x}) / (B _ {x} + S _ {x}) ] \varphi ,
$$

Buyers' Profit per Share Market Y

$$
= 1 0 \varphi - \Delta [ (B _ {Y} - S _ {Y}) / (B _ {Y} + S _ {Y}) ] \varphi ,
$$

$$
\begin{array}{l} \text { Sellers'   Profit   per   Share } _ {\text { Market   Y }} \\ = 1 0 \mathfrak {c} + \Delta [ (B _ {Y} - S _ {Y}) / (B _ {Y} + S _ {Y}) ] \mathfrak {c}, \end{array}
$$

where: $B =$ total quantity to buy in the market,

$S =$ total quantity to sell in the market.

For buyers: $\Delta = 60$ if $(B - S) > 0$ ,

i.e. order balance in sellers' favor $\Delta = 30$ otherwise,

For sellers: $\Delta = 60$ if $(B - S) < 0$ ,

i.e. order balance in buyers' favor $\Delta = 30$ otherwise.

Notice that the larger, more liquid market will have a greater value of $B + S$ , and thus will be less sensitive to order imbalances between buyers and sellers. Also, the coefficient $\Delta$ takes on a higher value when the imbalance is unfavorable to a trader. This reflects the asymmetric incentive structure under which most traders operate; they are paid a fraction of their trading profits as a bonus, but losses can result in job termination. $^{13}$ An example of the earnings calculations is presented in Table 1.

The difference between the two markets in the first part is that Market Y only open for trading if, after subjects have made their trading choices, a coin flip comes up heads. This indirectly represents the conditions that traders face when an organized securities market is first established, and, due to illiquidity, traders are not assured of execution of their orders.

The objective of the first part of the game is to expose traders to the risks of an illiquid market, and to establish an endogenous division of trading volume, with the majority of the volume naturally in Market X. This creates a subject determined division of trading volume into the two markets. Note that because there is a risk of Market

X being illiquid, not all of the trading in Part I gathers there.

Part II. At the start of the second part, an announcement is made that Market Y will no longer be subject to closures and that because of enhancements it can offer lower costs compared to Market X. The execution of submitted orders to the smaller market is no longer subject to a coin flip. These enhancements make Market Y a lower-cost alternative to Market X, which was the larger market in the final round of Part I; however at least initially Market X retains some activity. In Experiments 1–4 and Experiment T, Market Y's new earnings functions are:

Buyers' Profit per Share Market Y

$$
= 1 4 \varphi - \Delta [ (B _ {Y} - S _ {Y}) / (B _ {Y} + S _ {Y}) ] \varphi ,
$$

$$
\begin{array}{l} \text { Sellers'   Profit   per   Share } _ {\text { Market   Y }} \\ = 1 4 \mathfrak {c} + \Delta [ (B _ {Y} - S _ {Y}) / (B _ {Y} + S _ {Y}) ] \mathfrak {c}. \end{array}
$$

The variables—B, S, and $\Delta$ —are as indicated above. If all traders move their orders to Market Y, they can earn 40 per cent higher profits; thus, traders receive a substantial benefit if they are able to coordinate their market participation decisions and make a transition of liquidity to the new, more advantageous market. However, strategic uncertainty about how the other traders will react to the alternative market may lead traders to remain active in the more costly, but more liquid, established market. As in the first part, there is a substantial penalty expected for being in the illiquid market.

In Experiments 5–7, we test for the robustness of the experimental transitions by manipulating the treatment variable, the cost advantage of the smaller, alternative market. The advantage of the alternative market is reduced from 40 percent higher expected earnings to only 10 percent higher expected earnings. In Experiments 5–7, Market Y's earnings functions are:

$$
\begin{array}{l} \text {Buyers^{\prime} Profit per Share_{MarketY}} \\ = 1 1 \not \in - \Delta [ (B _ {\mathrm{Y}} - S _ {\mathrm{Y}}) / (B _ {\mathrm{Y}} + S _ {\mathrm{Y}}) ] \not \in , \\ \text {Sellers^{\prime} Profit per Share_{MarketY}} \\ = 1 1 \not \in + \Delta [ (B _ {\mathrm{Y}} - S _ {\mathrm{Y}}) / (B _ {\mathrm{Y}} + S _ {\mathrm{Y}}) ] \not \in . \end{array}
$$

## 3.2. Experimental Results

The graphs of Experiments 1–4 in Figure 1 illustrate that, with sufficient gains available (e.g., 40% greater profit potential) from an alternative trading mechanism, subjects appear able to move their trading activity and make transitions to a new alternative market.

The graphs of Experiments 5 to 7 in Figure 2 indicate that the relative advantage of the alternative market influenced the transition paths away from the established market. With only 10 percent higher expected earnings, the slopes of the transition paths were flatter and indicated a longer period until the alternative market captures a dominant share of trading volume. In Experiment 5, there was no statistically significant transition, and in Experiments 7, the transition was only significant at the 0.10 level. The relative advantage of the alternative influences the likelihood and speed of transitions; transitions seem less likely and less rapid when the relative benefit of the new market is smaller. For payoff improvements greater than a critical threshold, Pareto preferred expectations are fulfilled and the alternative market is able to overcome the “liquidity trap” and become the dominant trading mechanism. Below this threshold, the central market defense appears to hold.

The results indicate that the advantages of the alternative lead to gradual, but statistically significant, transitions of liquidity away from the established market. Although the traders' profits as a group are maximized by making an immediate and complete transition to Market Y, the extent of the strategic uncertainty leads to a fairly long period in which both markets are active. In only one case did the alternative market attract all of the trading activity within the 12 rounds. Adoption of the alternative market over time is modeled as an exponential time-series of the form:

$$
\text { Market   Share } _ {\text { Market   Y }} = 1 - A e ^ {- B t}
$$

For increasing market share, this functional form is non-negative and approaches one for large t (period number). The graphs in Figures 1 and 2 include the fitted curves of the time series model. Because the results and decision patterns of Experiment T are consistent with those observed with student subjects, we feel confident that the trials with student subjects are reliable indicators of practitioner behavior.

From Table 2, the t-statistics for B, the time-series coefficient, indicate the market share trends are different from zero at the 0.01 level of significance in all cases when the alternative market offered 40 percent higher

Figure 1 The Average Share of Trading Activity in Market Y in Part 1 Ranged from About 30% to 50% as Subjects Varied the Portion of Their Orders to the Two Markets. A Transition of Trading Activity Away from the Established Market X Occurs in Part 2 When Market Y Has a Cost Advantage  
Market Share of Market Y
(Alternative market offers 40% higher expected earnings)  
Experiment 1  
![](/api/attachments/68HZBXXK/fulltext/images/1cc181e432fc76558454c80a6f3a4c49c75c6bd7ee874d2ee7f4bf7ac64d76be.jpg)  
Experiment 3

Experiment 2  
![](/api/attachments/68HZBXXK/fulltext/images/f1acafe19e586612b87b284cf273c949ccfc6b88466e759da4615b23b12a7466.jpg)

![](/api/attachments/68HZBXXK/fulltext/images/9ad1a001df6f81abf289b3c8cf7cc1bce5903f4581b193a4987bd7df7be85f6d.jpg)

expected earnings. In two experiments, the last periods were not included in the model's estimation when these appeared to be outliers and the result of end game behavior, which is often observed in limited-horizon experimental research. Durbin-Watson test statistics are calculated, and provide no evidence of autocorrelated residuals or misspecification of the model. Table 2 lists the regression parameters.

Experiment 4  
![](/api/attachments/68HZBXXK/fulltext/images/7d963cd1e854eeb784894ca19f0f3f821beb0756db956f67848ac43c31cc9c19.jpg)

The graphs in Figures 1 and 2 illustrate the transitions of market share away from the relatively more costly market in the second part of experiments. The fitted curves of the time series models are included. The results of Experiments 1–4 indicate that with the introduction of a sufficiently advantageous alternative market, traders are capable of making a transition away from an established market.

Figure 2  
When the Relative Advantage of the Alternative Market Is Reduced, Transitions Are Less Likely and Less Rapid. Experiment T Was a Shortened Experiment and Was Conducted with Eight Floor Traders from New York Stock Exchange Member Firms. The Results and Decision Patterns Were Similar to Students  
Market Share of Market Y
(Alternative market offers 10% higher expected earnings)  
Experiment 5  
![](/api/attachments/68HZBXXK/fulltext/images/488055b0651cf523d99cfe37367d6ebcbb701fb26ddb660473c6687985802ba8.jpg)

Experiment 6  
![](/api/attachments/68HZBXXK/fulltext/images/63ae80d358762ade50f9eb241d2a961c38b1d53bb3adcee3bb37e93b52288af6.jpg)

Experiment 7  
![](/api/attachments/68HZBXXK/fulltext/images/e3051143f2e5cbaaf0db08410fb960da45dc32ce17d2021e19b5cb9e889fc2b6.jpg)  
Experiment T (40% Higher E(Earnings))

![](/api/attachments/68HZBXXK/fulltext/images/f8208c36339b0f6dd7add03b1f010f906db61f68fd0648343b9ed148e60f118d.jpg)

## 3.3. Summary

The experiments demonstrate the feasibility of movements of trading activity away from a larger, established market to a market that offers recognizable and sufficient cost advantages. Multiple equilibria exist when several markets compete for trading activity, and in the absence of a robust, theoretical economic prediction, we observed trader behavior in a controlled lab setting. Despite the initial liquidity advantage of one market, transitions to an alternative market occurred when the cost advantage was greater than a threshold value. The experimental results show that neither the assumption of realized rational expectations nor the central market defense provides an explanation for the slow adoption of alternative screen-based trading mechanisms. Our results suggest that a critical threshold exists and beyond this alternative markets overcome the “liquidity trap” and become the dominant trading mechanism. We do not know how the difficulty of achieving coordination scales up as the number of market participants increases; it is not clear how increasing participants from eight to several thousand would affect the rate of transition. However, our evidence suggests that sufficiently enhanced markets will succeed in attracting volume and liquidity away from established trading venues.

Table 2 Time Series Analysis: Transitions of Trading Activity

<table><tr><td rowspan="2">Experiment</td><td rowspan="2">Advantage of Alternative Mkt</td><td colspan="2">Coefficients</td><td rowspan="2"> $R^2$ </td><td rowspan="2">t-statistic</td><td rowspan="2">D-W Stat</td><td rowspan="2">No. Periods until E(Share) of Alternative Mkt &gt; 85%</td></tr><tr><td>A</td><td>B</td></tr><tr><td> $1^a$ </td><td>40%</td><td>0.373</td><td>0.086</td><td>52.4%</td><td>2 97#</td><td>0.96&amp;</td><td>11</td></tr><tr><td> $2^a$ </td><td>40%</td><td>0 506</td><td>0.203</td><td>90.7%</td><td>9 38#</td><td>1.75 $^{22}$ </td><td>6</td></tr><tr><td>3</td><td>40%</td><td>0.384</td><td>0 077</td><td>66.5%</td><td>4.46#</td><td>2.08 $^{22}$ </td><td>13</td></tr><tr><td>4</td><td>40%</td><td>0.408</td><td>0.044</td><td>52.2%</td><td>3 30#</td><td>1 55 $^{22}$ </td><td>23</td></tr><tr><td>5</td><td>10%</td><td>—</td><td>—</td><td>2.7%</td><td>Not Significant</td><td></td><td>—</td></tr><tr><td>6</td><td>10%</td><td>0.500</td><td>0.047</td><td>56.2%</td><td>3.58#</td><td>3 08&amp;</td><td>26</td></tr><tr><td>7</td><td>10%</td><td>0.504</td><td>0.030</td><td>24.0%</td><td>1 78*</td><td>1 80 $^{22}$ </td><td>41</td></tr><tr><td>NYSE Traders</td><td>40%</td><td>0.491</td><td>0.081</td><td>22.6%</td><td>0.94**</td><td>—</td><td>15</td></tr></table>

$^{a}$ = Twelfth period excluded from regression.  
& = Durbin-Watson test inconclusive at 0.01 level.  
\*\* = Significant at 0.20 level.  
# = Significant at 0 01 level.  
\* = Significant at 0 10 level.  
$^{6}$ = Durbin–Watson test. Cannot reject null hypothesis of nonautocorrelated residuals at 0.01 level.

The failure of current electronic alternatives to formal stock exchanges therefore should not be explained by a failure of traders to achieve a coordinated move to a sufficiently superior trading mechanism. Rather, an alternative explanation appears to be that today's alternatives are not yet seen by market participants as superior to existing markets. Additional factors could complicate actual traders' decisions, but this analysis—established markets will not remain more liquid simply because of an initial liquidity advantage—should continue to hold.

## 4. Simulation Modeling and Analysis of Alternative Market Designs

A second experimental methodology, simulation modeling, is used to examine the quality of disintermediated markets in order to assess if their limited adoption could be explained through market quality shortcomings. Simulation is used to extend analytical work by Amihud and Mendelson (1980), Ho and Macris (1985), and others, examining the relative performance of different securities market structures. The results of previous analyses provide significant insight into the determinants of market quality for the market structures examined, but are of limited use for comparing the alternative market structures available today. For instance, closed-form derivations of market characteristics have been kept tractable by making several restrictive assumptions; e.g., the specialist has been modeled as a monopoly market maker, or all orders have been restricted to be market orders of unit size, or trading was assumed to occur in batches at fixed points during the day (Garbade and Silber 1979, Mendelson 1987). In actual markets, however, the specialist faces competition from the orders of public investors, and trading in today's markets usually occurs continuously. Some of the market characteristics excluded in previous analytic approaches may be precisely those that strongly affect market quality, or that are of specific interest to market planners. By preserving those characteristics that we are trying to study and accommodating details of actual market mechanisms, simulation modeling can augment the results available from closed-form modeling, and can provide insight into market design choices that may strongly influence transactional characteristics and performance.

## 4.1. Comparing Market Mechanisms

Using simulation, we are able to compare detailed and realistic models of two prevalent trading mechanisms. The first market design considered is a disintermediated order matching market similar to the CATS (Computer-Assisted Trading System) trading system introduced in Toronto in 1977. CATS's automated order matching system is the most prevalent mechanism for electronic trading, and versions of CATS are now in use in stock markets in Tokyo, Paris, Brussels, and Madrid. The second market structure is a floor-based, intermediated market. Traditional trading floors have been favored by the U.S. stock exchanges, of which the best known is the NYSE. The NYSE operates a specialist auction market on its 37,000 square foot trading floor. While there are a number of alternatives to the NYSE and CATS trading mechanisms, these two provide an important comparison for proponents of floor-based and automated securities markets.

In both market designs, customers may submit either limit orders—requests to buy or sell a specified quantity at a specified limit price—or market orders, requests to buy or sell a specified quantity immediately at the best price currently available in the market. Limit orders are placed in a limit order book in price and time priority: the higher the bid price the customer is willing to pay to buy, the higher the order's placement in the book, and the lower the ask price the customer will accept to sell, the higher the priority. Equally priced bids and equally priced asks are placed in time-priority (FIFO) order. Because the limit price may not be reached in the market, execution of limit orders is uncertain. Market orders to buy will execute immediately against the first ask in the book, and market orders to sell will execute against the best bid in the book. When submitted, limit orders will attempt to match orders already in the book; for instance, if an investor is willing to bid at a price that is equal to or higher than the best ask, the two orders will execute at the ask price, and if an investor is asking a price lower than or equal to the best bid, the orders will execute at the bid price. Otherwise, if the new limit order cannot execute immediately, it is added to the book.

The first market design considered is electronic order matching through a screen-based consolidated limit order book (CLOB). The limit order book is open and visible to market participants, who can enter limit orders, or trade immediately by matching against existing orders. Fundamental to CATS and other order matching markets is that investors have full information access, and the market has no formal role for dealer intermediaries. Technology allows for the market to be “disintermediated,” which has consequences for its performance characteristics. Our model of a CLOB market will be described below.

The second market design is based on the dominant structure for securities trading in the U.S., a specialist floor auction market. On the New York Stock Exchange each stock has a single registered specialist, who maintains a limit order book and sets his or her own quotes. The specialist sees the entire order book, while traders off the NYSE floor see just the best buy and sell orders or quotes. Limit orders entered by investors at the same price as the specialist's bid or offer have priority and will execute first. The best bid and offer prices are disseminated off the floor, and orders are first exposed to the specialist, who arranges for their immediate execution or enters them into a limit order book for execution at a later time. The specialist also enforces rules in the auction and is prohibited from making destabilizing trades for his own account (e.g., the specialist cannot sell shares from his own position when the market is falling). These features are incorporated in our model of the specialist market trading mechanism.

Proponents of screen-based markets argue that by facilitating the disintermediation of trading, such systems will improve market quality. It is argued that without the necessity of paying the dealer's spread between bid and offer prices, investors will pay less to trade, more traders will be attracted, and higher market quality will result. $^{14}$ The competing hypothesis is that designated market makers, such as specialists on the New York Stock Exchange, improve the quality of the market at a cost less than the value of the service they provide. Intermediaries benefit investors by committing risk capital to the market and by buffering price movements, buying when there is a temporary excess of sell orders and selling when there is an excess of buy orders. The principal rule the specialist must observe is affirmative obligation, which requires the specialist to make bid and offer quotes when limit orders do not provide sufficient liquidity. Affirmative obligation is described in NYSE Rule 104.10(b):

In connection with the maintenance of a fair and orderly market, it is commonly desirable that a member acting as specialist engage to a reasonable degree under existing circumstances, in dealing for his or her own account when lack of price continuity, lack of depth, or disparity between supply and demand exists or is reasonably to be anticipated.

That is, the specialist is expected to buy when there is an excess of interest on the sell side, and sell when there is an excess on the buy side. Affirmative obligation, it is argued, stabilizes prices through the specialist's buying for or selling from their own inventory when order flows are temporarily imbalanced; e.g., under stochastic order arrivals, a number of sell orders may occur in a row without a change in fundamental value of the security having occurred, and the specialists' trades prevent this temporary imbalance from radically lowering the market price.

In the simulation experiments, the treatment variable under experimenter control is the presence or absence of the specialist intermediary. Outcome variables are measures of market quality such as bid-ask spreads, round-trip transactions costs, and length of delay before a limit order executes. We compare the two markets for a range of order flow conditions.

## 4.2. Components of the Market Models

In the simulation models of these two designs, several common assumptions are made about the arrival process of investors' orders, order size, elasticity and order placement strategies, price volatility, and the proportions of market and limit orders. The two simulation models were written in SimScript II.V from CACI Company, and contained about 2,500 lines of code in total. $^{15}$

Order Book. Both markets are based on an order book containing investors' orders ranked by price and time of arrival. In the specialist market, the order book also contains the specialist's bid and ask quotes ( $B_S$ and $A_S$ ). Figure 3 illustrates one possible state of the order book at some time during the trading day. The current highest bids to buy are at $32\frac{7}{8}$ for 5 units, and the lowest offers to sell are at $33\frac{1}{8}$ for 10 units. Thus, the bid-ask spread is currently \$0.25, or 0.76% of the share price.

Trade Prices. The state of the order book at the time of an order's arrival determines the trade price in both market structures. If a market order to sell 3 units arrives with the book as in Figure 3, the trade price for would be $32\frac{7}{8}$ , and the quantity available at the unchanged bid quote would be reduced to 2 units. If a sell order for 10 units arrives with the book as in Figure 3, the trade price for all 10 units would be $32\frac{3}{4}$ , and the two orders at $32\frac{7}{8}$ and the one at $32\frac{3}{4}$ would execute and be removed from the book. The specialist, who is bidding $32\frac{3}{4}$ , will not participate in the trade because public limit orders have priority over specialist quotes at the same price. If a sell order for 25 units arrives, the trade price would be determined by the limit price of the final bid on the book to execute. In this case, the two orders at $32\frac{7}{8}$ , the one at $32_{4}^{3}$ , the specialist, whose quote is good for 10 units, and 5 of the 15 units available at $32_{8}^{5}$ would execute. The trade price for all 25 units would be $32_{8}^{5}$ . For arriving orders larger than the quantity available at the bid or offer, the rules in the simulation for establishing trade prices are based on NYSE statutes and practices. Note that these rules reduce the risks associated with placing a limit order that improves on the best available bid or offer; in the example described above, the customers bidding $32_{4}^{3}$ and $32_{8}^{7}$ both purchase shares for the lower price of $32_{8}^{5}$ .

Figure 3 Example Order Book with Specialist Quotes ( $A_{s}$ and $B_{s}$ )

<table><tr><td colspan="5">Specialist-Auction MarketLimit Order Book</td></tr><tr><td colspan="2">Bids</td><td rowspan="2">Price(in eighths)</td><td colspan="2">Offers</td></tr><tr><td>Orders</td><td>Qty.</td><td>Orders</td><td>Qty.</td></tr><tr><td></td><td></td><td>33.3</td><td>10</td><td>3</td></tr><tr><td></td><td></td><td>33.2</td><td>5</td><td>1</td></tr><tr><td></td><td></td><td>33.1</td><td> $A_s$  10</td><td>2</td></tr><tr><td></td><td></td><td>33.0</td><td></td><td></td></tr><tr><td>2</td><td>5</td><td>32.7</td><td></td><td></td></tr><tr><td>1</td><td>5  $B_s$ </td><td>32.6</td><td></td><td></td></tr><tr><td>2</td><td>15</td><td>32.5</td><td></td><td></td></tr></table>

Fundamental Value Diffusion. The simulation follows a standard assumption in financial economics research: the natural logarithm of the equilibrium value evolves according to a continuous random walk without any drift in prices (Garbade and Silber 1979, Amihud and Mendelson 1987). That is, equilibrium price in the models is equally likely to either rise or to fall. The white noise term, $e_{t}$ , is normally distributed with variance linear in the time since the last sample point.

$\ln p_t^* = \ln p_{t - T}^* + e_t$

$$
\text { where } e _ {t} \sim N (0, T \sigma^ {2}) \Rightarrow p _ {t} ^ {*} \sim \mathrm{LN} (\ln p _ {t - T} ^ {*}, T \sigma^ {2}).
$$

Order Arrival. In the simulation, market supply and demand are price-dependent Poisson processes, which are positively and negatively sloped respectively in price. In this model, at a particular price, the buy and sell order interarrival times are exponentially distributed. The supply and demand structure follows closely those previously developed in the market microstructure literature (Garman 1976, Mendelson 1987). As illustrated in Figure 4, the buy and sell order arrival rates are step functions of the difference between the quoted price and the equilibrium value of the security. Buy and sell arrival rates are equal only at the equilibrium value, $p^{*}$ . Market participants other than the specialist have access to information about a security's value (e.g., greater research into the company's prospects). The specialist, however, can only infer $p^{*}$ from the book, and his or her inventory. A growing long position, for instance, may indicate that the market quotes are too high and that informed investors may be profiting by selling at these prices.

The following equations represent the price-dependent order arrival rates:

I. Demand/buy orders $D(p)$ :

$$
\lambda_ {B} (p, p _ {i} ^ {*}) = k _ {1} \quad \text { for } p \geq p _ {i} ^ {*},
$$

$$
\lambda_ {B} (p, p ^ {*}) = k _ {1} + k _ {2} [ p _ {t} ^ {*} - p ] \quad \text { for } p = p _ {t} ^ {*} - \alpha
$$

$$
\text { with } \alpha = \frac {1}{8}, \frac {1}{4}, \frac {3}{8}, \frac {1}{2}, \frac {5}{8}, \frac {3}{4}, \frac {7}{8}, 1, 1 \frac {1}{8}, \dots , \delta ,
$$

$$
\lambda_ {B} (p, p _ {t} ^ {*}) = k _ {1} + k _ {2} \delta \quad \text { for } p _ {t} ^ {*} - p > \delta ,
$$

II. Supply/sell orders $S(p)$ : $\lambda_{S}(p, p_{i}^{*}) = k_{i}$ for $p \leq p_{i}^{*}$ ,

$$
\lambda_ {S} (p, p ^ {*}) = k _ {1} + k _ {2} [ p - p _ {t} ^ {*} ] \quad \mathrm{for} p = p _ {t} ^ {*} + \alpha
$$

$$
\mathrm{with} \alpha = \frac {1}{8}, \frac {1}{4}, \frac {3}{8}, \frac {1}{2}, \frac {5}{8}, \frac {3}{4}, \frac {7}{8}, 1, 1 \frac {1}{8}, \dots , \delta ,
$$

$$
\lambda_ {S} (p, p _ {t} ^ {*}) = k _ {1} + k _ {2} \delta \quad \text { for } p - p _ {t} ^ {*} > \delta .
$$

Figure 4 Stochastic Purchase (Demand) and Sell (Supply) Order Arrival Rates for an Equilibrium Value of \$33.00. Order Intensity Increases for Buy Orders at Market Prices Lower than Equilibrium Value, and Decreases for Sell Orders. Order Intensity Increases for Sell Orders at Market Prices Higher than Equilibrium Value, and Decreases for Buy Orders

![](/api/attachments/68HZBXXK/fulltext/images/fe9a33a4814daa38d56f14602dfc2d45bf5ad37fa5d428e3c35fc65fcc30a206.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Table 3 Limit Order Prices in Simulation

<table><tr><td colspan="9">Probability Mass Function for Limit Order Prices around Equilibrium Value</td></tr><tr><td colspan="9">Dollar Amount:</td></tr><tr><td>above p* (sell orders)</td><td>1/8</td><td>1/4</td><td>3/8</td><td>1/2</td><td>5/8</td><td>3/4</td><td>1</td><td>1 1/4 1 1/2</td></tr><tr><td>below p* (buy orders)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Probability</td><td>10%</td><td>14%</td><td>14%</td><td>16%</td><td>16%</td><td>12%</td><td>8%</td><td>5% 5%</td></tr></table>

The constant $k_{1}$ reflects the proportion of arrivals that are market orders. The coefficient $k_{2}$ reflects the sensitivity of buyers and sellers to discrepancies between available prices and the equilibrium value, $p^{*}$ . The parameter, $\delta$ , is the range around the equilibrium value from which limit prices for limit orders are generated. At a price $p_{i}$ lower than the equilibrium value at the time, $p_{i}^{*}$ , the arrival rate of buy orders will exceed the rate of sell order arrivals. The resulting buy orders will exceed the quantity of sell orders for below-equilibrium values. The excess demand will cause prices to rise since, in expectation, orders will purchase from the low offer quotes, or add new, higher priced bid quotes. The order arrival model is symmetric, so that at market prices below $p^{*}$ , the arrival rate of buy orders will exceed that of sell orders by the same amount that the sell order arrival rate will exceed that for buy orders at market prices the same increment above $p^{*}$ .

Supply, Demand, and Elasticity. The order flow in the simulation is generated by simulated traders who are either potential buyers or sellers, bidding for, or offering, between one and twenty-five units of the security. Traders use either limit orders or market orders. Some limit orders will execute on arrival in the market if there is a suitable counterparty order. To obtain the probable prices of arriving limit orders, we surveyed three NYSE specialists. The survey asked for a breakdown by frequency of limit order prices for a stock that currently has a $32\frac{7}{8}$ bid quote and a $33\frac{1}{8}$ offer quote. For this scenario, sell limit orders are possible at \$33, $33\frac{1}{8}$ , $33\frac{1}{4}$ , $33\frac{3}{8}$ , etc., and buy limit orders are possible at \$33, $32\frac{7}{8}$ , $32\frac{3}{4}$ , etc. The average response converted into probability is shown in Table 3.

Order Size. Buy and sell orders submitted to the market vary in size from 1 to 25 units. This reflects a convenient normalization that is consistent with empirical data from the New York Stock Exchange's TORQ (Trades, Orders, Reports, and Quotes) database of 875,133 orders in 144 NYSE stocks between November 1990 and January 1991. The order size assumption in the simulation, and the empirically observable order sizes are detailed in Table 4.

The comparison of our models of CATS trading and specialist market trading is undertaken assuming the same conditions of order arrival.

## 4.3. Specialist Policies

In the simulation, the specialist's portfolio is assumed to consist of shares of a single stock, where $Q_t$ is the number of shares held by the specialist immediately after a trade at time $t$ is completed. The time since the last trade is $T$ . The position at time $t$ is summarized by the pair $(c_t, v_t)$ , where $c_t$ is cash on hand, and $v_t$ is the value of the shares held when marked to the current equilibrium value. Let $q_t$ be the specialist's total purchases (negative for net sales, and positive for net purchases) at price $p_t$ at time $t$ :

Share portfolio (no. of shares): $Q_{t} = Q_{t - T} + q_{t}$ ,

Cash (\$):

$$
c _ {t} = c _ {t - T} - q _ {t} p _ {t}.
$$

Table 4 Order Sizes in Simulation and from NYSE Data

<table><tr><td colspan="6">Probability Mass Function for Trading Order Size</td></tr><tr><td colspan="6">SIMULATION:</td></tr><tr><td>Order Size</td><td>1</td><td>3</td><td>5</td><td>10</td><td>25</td></tr><tr><td>Probability</td><td>50%</td><td>30%</td><td>10%</td><td>5%</td><td>5%</td></tr><tr><td>TORQ DATA Order Size</td><td>≤400 shares</td><td>401–1,000 shares</td><td>1,001–2,000 shares</td><td>2,001–5,000 shares</td><td>&gt;5,000 shares</td></tr><tr><td>Empirical Frequency</td><td>51%</td><td>26%</td><td>11%</td><td>9%</td><td>4%</td></tr></table>

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

The value of the specialist's position at any time is the number of shares multiplied by the current equilibrium value, $p_t^*$ .

$$
\text { Value   of   position } (\): v _ {t} = Q _ {t} p _ {t} ^ {*}.
$$

The specialist cannot directly observe the equilibrium price, and thus cannot use this price to adjust quotes; rather, the specialist follows an inventory-driven policy to set bid and ask quotes, and also strategically adjusts his quotes in response to limit orders on the book. In the simulation model, the policies used are consistent with the profit-maximizing specialist policies derived by Conroy and Winkler (1981, 1986). The specialist in the simulation also observes affirmative obligation and other NYSE rules such as public order priority. We also verified the model's specialist policies by reviewing a trace of the simulation's operations with three NYSE specialists. In addition, the simulation model of trading has been used by a London-based securities firm as a training tool for their dealers to learn how to manage positions under a range of trading conditions; it has been further verified and has received an enthusiastic response from the firm.

Dealers in financial markets generally maintain position limits (in dollars or shares) to constrain their maximum risk. A position limit reflects the amount of inventory a dealer is willing to hold in a particular instrument. Beyond the position limit, a dealer will adjust his bid and offer quotes in an effort to reduce the absolute size of the position. After preliminary analysis and discussions with NYSE specialists, we selected a position threshold of 25 units of the security as being consistent with the scale of order flow in the simulation. If the specialist is long or short more than 25, quotes are revised $\frac{1}{8}$ th downward or upward. Larger position limits led to specialist losses, because the quote revisions lagged too far behind changes in the fundamental value of the stock. Smaller position limits made the simulated specialist's quotes excessively sensitive to his position, and reduced the extent of specialist participation without contributing to profitability.

In the simulations, the specialist's spread was set between \$0.50 and \$2.50 (about 1.5% to 6.7% of the stock's price) depending on the proportion of limit orders used by customers. The specialist adjusts quotes using private information on the state of the limit order book. A "thicker" limit order book on either the bid or offer side results in the specialist raising his bid or lowering his offer, thus narrowing the spread to compete with limit orders. A thinner book with fewer limit orders causes the specialist to widen his spread. The inputs used led to model output that is consistent with actual NYSE market measures. While not an explicit design goal, the correspondence underscores the fit of the model's behavior with actual trading conditions. The specialist's participation on the NYSE was about $18.4\%$ of trading volume in 1992, and in the model, the specialist's participation averaged $23.5\%$ across the 12 experimental conditions examined. Other NYSE data that verifies the simulation model is the probability of a limit order executing is $60.0\%$ , which is similar to the $59.3\%$ average obtained in the simulations. Several attributes that are measurable in the model are not available for the actual NYSE market. For instance, we can track the round-trip transactions costs in the simulation, while this is unobservable in the actual market since it is not known whether a trade is opening an investment position or closing it.

## 4.4. Experimental Design

The analysis of the two markets is based on an experimental design using 12 sets of trading conditions. The $2 \times 4 \times 3$ factorial design compares the two markets under four different values for the ratio of limit to market orders, and under three different market activity levels (active, average, and inactive). Based on applicable measures of market performance we assessed the alternative designs. Limit orders are set to 45, 55, 65, and 75 percent of total order flow, with market orders from investors accounting for the other orders. $^{16}$ The initial equilibrium value is set to 33.00. The equilibrium price varies according to a random walk process thereafter with standard deviation of daily returns of 2.25%, or about the median volatility of stocks in the S&P500 index. We consider stocks with mean interarrival times between orders of 20 seconds (active), 4 minutes (average activity), and 20 minutes (inactive).

In the simulations, limit orders cancel after a fixed period of time. In an informal survey of NYSE specialists, we determined that limit order durations are inversely proportional to the trading activity in a stock; i.e., limit orders in less active stocks remain in the limit order book for a longer period before cancellation than those for active stocks. We use the average of the estimates provided to us by the specialists. Limit orders that remain unexecuted after 4 hours (active), 6.5 hours (average activity), and 19.5 hours (inactive) of trading time are canceled.

A change in a market's structure from a specialist-auction to a CATS market system would likely change the order submission choices of investors. However, even a simple model in which there is some adjustment of the order arrival process would rely on arbitrary assumptions of what that response would be. Instead of making these arbitrary assumptions on investor profit maximizing strategy under new market conditions, we attempt to determine how much change in individual investors' use of limit orders would be required—in aggregate—to achieve equivalent market quality after the removal of a specialist intermediary. We accomplish this through sensitivity analysis, varying the percentage of limit orders employed and observing measures of market quality, but without attempting to devise a model that would explain the change in individual behavior. $^{17}$ In assessing the two market structures, the simulation compares the markets across a range of investor strategies (i.e., limit orders making up 45%, 55%, 65%, and 75% of total order flow). In §4.6, we use sensitivity analysis to assess the necessary changes to the investor behavior for the two markets to have equivalent market quality measures.

## 4.5. Experimental Results

Table 5 presents the averages over eight runs of 12 sets of experiments. For each of three activity levels and each of four ratios of limit orders to market orders, observed measures of market quality are shown. In each cell, the results for order matching systems are presented above, and directly below is the corresponding measure for the specialist market under identical order flow conditions.

The results in Table 5 indicate the two trading structures have significantly different market quality characteristics under equivalent order flows. These differences are most pronounced when the percentage of limit orders is lowest. Figure 5 presents the averages of bid-ask spread of eight replications each covering 40,300, or 1,500 days of trading in a stock. A round-trip represents the act of buying and later selling during the 60 day period. Market quality as measured by bid-ask spreads is better in the specialist market although increased levels of limit order use reduce the relative disadvantage of order matching systems.

We noted that the change in the market's structure from a specialist-auction to a CATS market system would likely change the optimal order placement strategy for a rational investor. It would have been ideal if we were able to base the order flow model in our simulation on an optimal bidding strategy for competitive traders in a continuous double auction that was adjusted for the presence of a specialist and the state of the order book at any point in time. This could rely on individual investors income streams, budget constraints, and axioms of rational choice over stochastic payoffs. The tractability and computational problems would be immense, and would likely rely on numerous bold or inaccurate assumptions; moreover the actual behavior of investors would no doubt differ from these normative strategies in complex and unforeseen ways. We therefore do not attempt to develop two optimal strategies, nor do we presume that investors' strategies will not change. Rather, as noted above, we use sensitivity analysis to explore how much investor strategies would need to change to assure that the disintermediated CATS market has equivalent market quality. Holding our order flow assumptions constant, but varying the parameters, allows us to compare the two market structures. Figure 5 indicates that a sufficient increase in investors' use of limit orders leads to spreads that are nearly equal in the two market designs. As indicated, limit orders provide liquidity, and sufficient increases in their use may obviate the need for the specialist.

A round-trip transaction (abbreviated RT) using market orders pays a cost due to the spread between bid and offer prices, while a round-trip using limit orders realizes a gain from selling at the higher offer price and buying at the lower bid price. Limit orders, however, face the risk of not executing and the risk that the price will move adversely while they are on the book. Even with the same order arrival patterns, the two market structures perform differently. Figure 6 illustrates that round trip transactions costs for market orders are lower without a specialist only in the case of an inactive stock, and with limit orders making up 75% of the total order flow.

Table 5 Experimental Design and Average Measures of Market Quality
Two alternative market structures are compared under identical order flow conditions. Order matching system results are underlined and on the top of each cell, and specialist market results are below.

<table><tr><td colspan="2">Input Parameters:</td><td colspan="4">Active</td><td colspan="4">Average</td><td colspan="4">Inactive</td></tr><tr><td>Order arrival rate</td><td></td><td colspan="4">180 per hour</td><td colspan="4">20 per hour</td><td colspan="4">3 per hour</td></tr><tr><td>Number of days</td><td></td><td colspan="4">40</td><td colspan="4">300</td><td colspan="4">1,500</td></tr><tr><td>Orders</td><td></td><td colspan="4">46,800</td><td colspan="4">39,000</td><td colspan="4">29,250</td></tr><tr><td>Percent limit orders</td><td>45%</td><td>55%</td><td>65%</td><td>75%</td><td>45%</td><td>55%</td><td>65%</td><td>75%</td><td>45%</td><td>55%</td><td>65%</td><td>75%</td><td></td></tr><tr><td>Output Measures:(Avgs over 8 runs)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Bid-Ask Spread</td><td>5.26%</td><td>2.30%</td><td>1.41%</td><td>0.97%</td><td>6.68%</td><td>4.44%</td><td>2.53%</td><td>1.60%</td><td>8.08%</td><td>6.38%</td><td>4.57%</td><td>3.03%</td><td></td></tr><tr><td>1.46%</td><td>1.25%</td><td>1.19</td><td>0.91%</td><td>1.97%</td><td>1.88%</td><td>1.60%</td><td>1.44%</td><td>3.29%</td><td>3.22%</td><td>3.11%</td><td>2.59%</td><td></td></tr><tr><td>Round-trip Transactions Cost</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Market orders</td><td>5.1%</td><td>3.3%</td><td>2.1%</td><td>1.5%</td><td>6.0%</td><td>5.1%</td><td>3.7%</td><td>2.7%</td><td>6.8%</td><td>5.3%</td><td>4.2%</td><td>3.7%</td><td></td></tr><tr><td>2.2%</td><td>1.8%</td><td>1.7%</td><td>1.4%</td><td>3.3%</td><td>3.2%</td><td>2.6%</td><td>2.5%</td><td>4.7%</td><td>4.8%</td><td>4.3%</td><td>4.8%</td><td></td></tr><tr><td rowspan="2">Limit orders (Gain)</td><td>3.8%</td><td>3.1%</td><td>1.8%</td><td>1.1%</td><td>4.1%</td><td>3.7%</td><td>2.7%</td><td>1.7%</td><td>4.7%</td><td>4.3%</td><td>2.7%</td><td>2.3%</td><td></td></tr><tr><td>2.5%</td><td>1.8%</td><td>1.5%</td><td>1.0%</td><td>3.9%</td><td>3.1%</td><td>2.3%</td><td>1.7%</td><td>5.6%</td><td>4.3%</td><td>4.2%</td><td>2.5%</td><td></td></tr><tr><td rowspan="2">Probability limit order executes</td><td>93.1%</td><td>83.5%</td><td>61.9%</td><td>47.5%</td><td>81.7%</td><td>77.4%</td><td>65.1%</td><td>51.5%</td><td>77.0%</td><td>74.7%</td><td>67.0%</td><td>56.7%</td><td></td></tr><tr><td>72.4%</td><td>60.4%</td><td>55.3%</td><td>45.5</td><td>67.5%</td><td>62.1%</td><td>53.5%</td><td>48.8%</td><td>68.3%</td><td>63.8%</td><td>60.0%</td><td>53.4%</td><td></td></tr><tr><td rowspan="2">Percent market orders delayed</td><td>21.6%</td><td>1.5%</td><td>0.0%</td><td>0.0%</td><td>31.9%</td><td>172%</td><td>5.5%</td><td>1.7%</td><td>36.6%</td><td>25.5%</td><td>14.7%</td><td>6.9%</td><td></td></tr><tr><td>0.4%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>11.8%</td><td>5.8%</td><td>2.7%</td><td>1.4%</td><td>20.8%</td><td>14.6%</td><td>10.1%</td><td>5.9%</td><td></td></tr><tr><td rowspan="2">Percent time book has no public bid or no ask</td><td>34.7%</td><td>2.1%</td><td>0.0%</td><td>0.0%</td><td>52.0%</td><td>25.0%</td><td>7.1%</td><td>1.8%</td><td>63.0%</td><td>39.4%</td><td>20.3%</td><td>8.3%</td><td></td></tr><tr><td>0.2%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>7.5%</td><td>2.2%</td><td>0.4%</td><td>0.2%</td><td>14.9%</td><td>8.4%</td><td>4.2%</td><td>2.2%</td><td></td></tr><tr><td rowspan="2">Limit order wait(minutes)</td><td>39.1</td><td>58.1</td><td>107.3</td><td>143.0</td><td>145.5</td><td>156.9</td><td>193.5</td><td>236.0</td><td>520.0</td><td>530.3</td><td>590.5</td><td>674.6</td><td></td></tr><tr><td>86.9</td><td>112.4</td><td>122.9</td><td>147.7</td><td>182.2</td><td>193.6</td><td>221.0</td><td>241.2</td><td>545.2</td><td>578.1</td><td>619.1</td><td>688.8</td><td></td></tr></table>

In the simulations, as in actual markets, full trading costs are greater for orders of greater quantity. Traders often refer to the “market impact” of a large buy or sell order. A trader using a large market order to buy securities will pay a premium above the price at which a smaller order would trade. The premium compensates the counterparty to a large trade for the greater risk of the position they are left with. Large sellers, likewise, will receive a discounted price for their securities when they trade using market orders. In the models, market impact occurs when the quantity available at the bid or offer quote is insufficient. A large sell order, for instance, may trade against bids at successively lower prices. As Figure 7 illustrates, the simulation results show that adverse price movement—the buyer premium or seller discount—caused by a large trade is smaller in the simulated specialist market. For instance, under average order arrival conditions in the specialist market, the round-trip costs for an average size trade are just under 2.0% of the security's price, and for trades four times larger costs are 2.9%, while in the order

## Figure 5

Market Spreads (as a Percent of Price) for Markets with and Without a Specialist Are Compared for Three Different Levels of Order Intensity to Represent Stocks That Trade Actively, with Average Activity, and Inactively. Under All Conditions, the Participation of the Specialist Reduces Spreads Compared to the Disintermediated, Order Matching Market. The Specialist's Contribution to Market Quality is Greatest When the Percentage of Limit Orders Is Lowest, and Decreases as Investors' Use of Limit Orders Increases  
![](/api/attachments/68HZBXXK/fulltext/images/a91f6851b43e0fbcdad1f2506f70d53b4494d04152bb3ee18b8e84d6ef846b72.jpg)

matching market, costs are 2.9% for an average size trade and 4.3% for large trades. Costs and premiums shown are averages for 32 simulation runs with limit orders set to 45, 55, 65 and 75 percent (eight runs each).

## 4.6. Discussion

Significant differences exist between the performance measures of the market structures even when compared under identical conditions of order arrival. Critical market quality measures including market spreads, the cost of executing a round-trip transaction with market orders, and market impact of larger orders, are considerably improved by specialist participation. In addition, the execution of arriving orders is more likely to be delayed in the disintermediated order matching design. The simulation shows that the extent of these market quality differences, however, is a function of the trading conditions examined, in particular investors' use of limit orders.

Although limit order execution is probably improved in the disintermediated market design, this appears to be offset by a reduction in market quality for market orders. Without a specialist and without the specialist's quotes improving on the book orders, limit orders have a higher probability of executing, execute faster, and at a more advantageous price; not surprisingly, at least some of this benefit for users of limit orders comes from the fact that the specialist would otherwise be competing, and would be offering a better price to market orders. Those limit orders that are offering to buy too low, or sell too high, do not execute when the specialist is present; those orders that execute are those that are priced more fairly, and even these may now have to wait. Users of limit orders who price them least competitively will be disadvantaged by this competition from the specialist. Clearly, however, users of market orders benefit from specialists' participation. In addition, the intermediation of a specialist is shown to moderate the market impact of large trades.

The market quality differences detailed in Table 5 indicate that a dealer-intermediary earning positive profits improves market quality on several dimensions, and

Figure 6 Average Transactions Costs (as a Percent of Price) for Round-trip (RT, Purchase and Later Sale) Investments Made with Market Orders for a Market with and a Market Without a Specialist. The Costs of Market Orders Whose Executions are Delayed Are Increased 5 Percent; e.g., if the RT Cost is 3% Without Delay, then the RT Cost Will Be 8% if Either the Purchase or Sale is Delayed Because of Inadequate Quantities on the Order Book. Costs Are Compared for Three Different Levels of Order Intensity to Represent Stocks That Trade Actively, with Average Activity, and Inactively. Under Most Conditions, the Participation of the Specialist Reduces Transaction Costs. The Specialist's Contribution to Market Quality is Greatest When the Percentage of Limit Orders is Lowest, and Decrease as Investors' Use of Limit Orders Increases  
![](/api/attachments/68HZBXXK/fulltext/images/0d5c2505e3697a35840dd3313ef32bccb33ca8e5cdd0f981a54814e13322b71c.jpg)

Average Transactions Costs (as a Percent of Price) for the Average Trade Size (Dark Shaded), and Size Premiums (Added Cost for a Trade 4 Times Larger) for Round-trip Investments Made with Market Orders for Markets With, and Without a Specialist. Costs and Premiums Are Compared for Three Different Levels of Order Intensity Levels to Represent Stocks That Trade Actively, With Average Activity, and Inactively. The Specialist's Ability to Reduce Market Impact Is Greatest for More Actively Traded Shares  
![](/api/attachments/68HZBXXK/fulltext/images/8b9c4aea92f7c21de9621c924e9df0124a64f355782a56c2bd56e3ca1a8a5347.jpg)  
electronic market designs that eliminate or reduce the role of dealer-intermediaries may not in fact be in the best interests of all market participants. On the basis of the simulations, we can interpret activities of the specialist as lowering transactions costs for market orders, while reducing the probability of execution for limit orders that would otherwise opportunistically buy at low prices and sell at high prices when a temporary order imbalance exists. The specialist's participation also helps to maintain price continuity, so that trade-to-trade price fluctuations are reduced.

A sufficient increase in investors' use of limit orders can lead to spreads that are equal in the two market designs (see Figure 5). Hence, for order matching systems to provide comparable market quality, there needs to be dramatically increased use of patient, limit order trading strategies by investors. $^{18}$ Without a rise in such liquidity-providing limit orders, there is a strong argument for a special class of market participants—such as the specialist—with lower transactions costs, affirmative obligation, and some preferential access to information in the order book. The results here indicate that their participation adds liquidity and enhances market quality.

## 5. Contribution and Future Research Plan

The research employs two methodologies for analyzing the value and potential impact of electronic trading systems; its results have several significant policy implications. We examined the ability of experimental subjects, acting as traders, to coordinate their activity on a better market. We found that under experimental conditions that did not allow for direct communication between market participants, sufficiently attractive alternative markets are capable of drawing liquidity away from an established market. The comparison of a simulated specialist market with a simulation of the most prevalent electronic trading system revealed that the operations of a dealer-intermediary can enhance several measures of market quality. Together, these results imply that transitions to alternative trading mechanism are feasible, but that the electronic market design generally considered the best at present (an open limit order book with disintermediated order matching) is not uniformly preferable relative to the market structure in use on the major U.S. stock exchanges (specialist plus limit order book). The design of alternative electronic trading systems and accompanying alternative regimes for regulation of markets produce trade-offs among market participants. For instance, investors may have lower trading costs in a certain trading mechanism, but intermediaries' profits may fall. Patient investors that use limit orders to trade may prefer a particular market structure, while active investors that use market orders for trading immediacy may be better served in a market with greater levels of intermediation. Our results suggest that, at least in an experimental setting, when an electronic trading system does represent an improvement over the established market design, its adoption is unlikely to be hindered by traders' inability to coordinate their trading activities explicitly.

The experimental methods employed here provide insight into the evolution of competing markets, which in turn contributes insight into the appropriate regulatory response. Since traders apparently would be capable of moving to a more attractive, lower cost market despite its initial lack of liquidity, regulatory intervention to influence traders' choice and market technology is inappropriate at this time. In light of our findings, efforts should be made to evaluate other electronic market designs that could provide clear and demonstrable improvements in market quality. Hybrid designs have been proposed and are described in Amihud and Mendelson (1988) and Waters (1990). Suggestions have been made for integrated continuous and call auction trading, or competing market makers augmented by a consolidated limit order book, as is under consideration for the London stock market, or the addition of single-price crossing auctions in the market's off-hours, as recently introduced on the New York Stock Exchange.

While this research analyzes the effects of traditional dealer intermediaries, assessing the relative merits of traditional markets and electronic alternatives remains a complex issue. Effectively forecasting IT adoption in securities trading will remain difficult, but we have shown that experimental economics and discrete event computer simulation are valuable methodologies for assessing the impacts of IT on market participants. The implications of the work are significant to various stakeholders, including exchanges, their regulators, and trading systems developers. $^{15}$

$^{19}$ Invaluable advice on this research came from Colin Camerer, Jim Cochrane, Prem Jain, Steve Kimbrough, and Marc Knez. The work benefitted from presentations at the London Business School, University of Pittsburgh, New York University, and the International Conference on Information Systems (ICIS) The assistance of Terence Meehan, President of the NYSE Specialists Association, and Joel Hasbrouck, Professor of Finance at NYU and former NYSE Visiting Research Economist is gratefully acknowledged, as is the financial support of the Reginald H. Jones Center Project on Information Systems, Telecommunications, and Business Strategy at the Wharton School We would like to thank three anonymous reviewers for their contribution in improving the paper and its clarity.

## Appendix

## Experimental Instructions and Subject Record Sheets

## Introduction

Welcome. This is an experiment in market decision making. Various research sponsors have provided funds for this research. The instructions are straightforward and if you follow them carefully and make good decisions you can earn a considerable amount of money, which will be paid to you in cash

This experiment will consist of a series of decision making periods. In each period you will make choices separately and independently of the other participants. Payoffs will be made depending on your choice and the choices of the other participants

## General Instructions

Each of you have been randomly assigned to be a member of the buyer group or the seller group. Members of the buyer group have "BUYER" marked on their folders, and a number (for example BUYER 4). Each of you will be assigned a work place. You will communicate with the experimenter with messages, and I will be nearby to answer questions if they arise. You are asked not to discuss the experiment with the other traders.

In this experiment there will be two market games. Each game consists of 12 rounds. A round involves individual trading decisions made at the same time by each of the 4 buyers and 4 sellers. Based on your decision, and the decisions of others, you will have a profit or loss in that round. You will keep a record of your trading account and you will be paid based on the amount in your account at the end of the experiment

## Choices in Each Decision Round

Two markets are available in which you can buy or sell. In a round, each trader has an assigned quantity of 10 shares to buy or 10 shares to sell. This quantity can be divided across the two markets whatever way you feel is best. Choices can be any round number between 0 and 10, but the total must be 10

The markets are labeled X and Y. Trading decisions have an effect on prices in the two markets, and also have an effect on your earnings

## Earnings from Choices

Depending on the amounts to buy and to sell, a buyer's profit and a seller's profit are determined for each market. Profits for buyers and profits for sellers in a market may be different, and will vary based on the outcome:

\- If the quantity to buy and the quantity to sell in a market are the same, buyers and sellers submitting the same amount earn equal profits.

\- When more units are offered to sell than to buy, sellers earnings are reduced and buyers earn more

\- If there are more units to buy than to sell, buyers earnings are reduced and sellers earn more.

At the end of each round, the total quantities submitted to each market will be announced and you will calculate your earnings. The earning points are "Canadian" cents. For instance, "1.2" is \$0.01, and "120" is \$1.00.

## Specific Instructions for Sellers

You will be submitting quantities to sell to the market. Your earnings will be determined by your actions and the actions of the other traders. Your earnings are given by the following functions:

Market X:

Sellers Earnings per Share in Market X

$$
= 1 0 + A * (\text { Imbalance   in   Market } X)
$$

Market Y:

$$
\text { Sellers   Earnings   per   Share   in   Market   Y }
$$

$$
= 1 0 + A * (\text { Imbalance   in   Market   Y })
$$

where

$$
\text { Imbalance } = \frac {\text {(Shares to Buy - Shares to Sell)}}{\text { Total Shares in Market }}
$$

and A is 30 or 60 depending on the direction of the imbalance

$$
\text { if   the   Imbalance   is   greater   than   zero } \rightarrow A = 3 0
$$

or

if the Imbalance is less than zero → A = 60

Two numbers determine the earnings in a market. First the number of shares to buy minus the number of shares to sell, and second the total amount submitted to that market. Notice that:

\- because there are 40 shares to buy and 40 shares to sell in each round, the imbalance in one market must be the opposite of the imbalance in the other market, for example 2 and -2.

\- if shares to sell outnumber shares to buy in a market by more than $40\%$ the earnings for sellers in that market will be negative

All sellers have the same earnings function, and the buyers' profit function is the same except the sign in the second term is negative:

Buyers:

Buyers Earnings per Share in Market X or Y

$$
= 1 0 - A * (\text { Imbalance   in   Market } X \text { or } Y)
$$

and $A$ is 30 or 60 depending on the direction of the imbalance

if the imbalance is less than zero (i.e., there are more shares

to sell than shares to buy) → A = 30

or

if the imbalance is greater than zero → A = 60.

For buyers, if shares to buy outnumber shares to sell in a market, the buyers earnings in that market can be negative

Specific Instructions for Buyers

You will be submitting quantities to buy to the market. Your earnings will be determined by your actions and the actions of the other traders. Your earnings are given by the following functions:

Market X·

Buyers Earnings per Share in Market X

$$
= 1 0 - A * (\text { Imbalance   in   Market } X)
$$

Market Y.

Buyers Earnings per Share in Market Y

$$
= 1 0 - A * (\text { Imbalance   in   Market   Y })
$$

where.

$$
\text { Imbalance } = \frac {\text {(Shares to Buy - Shares to Sell)}}{\text { Total Shares in Market }}
$$

and A is 30 or 60 depending on the direction of the imbalance.

$$
\text { if   the   Imbalance   is   greater   than   zero } \to A = 6 0
$$

or

$$
\text { if   the   Imbalance   is   less   than   zero } \rightarrow A = 3 0
$$

Two numbers determine the earnings in a market. First the number of shares to buy minus the number of shares to sell, and second the total amount submitted to that market. Notice that

\- because there are 40 shares to buy and 40 shares to sell in each round, the imbalance in one market must be the opposite of the imbalance in the other market, for example 2 and -2

\- if shares to buy outnumber shares to sell in a market by more than $40\%$ the earnings for buyers in that market will be negative
All buyers have the same earnings function, and the sellers' profit function is the same except the sign in the second term is positive:

Sellers:

Sellers Earnings per Share in Market X or Y

$$
= 1 0 + A * (\text { Imbalance   in   Market   X   or   Y })
$$

and A is 30 or 60 depending on the direction of the imbalance: if the imbalance is less than zero (i.e., there are more shares

$$
\text { to   sell   than   shares   to   buy) } \rightarrow A = 6 0
$$

or

if the imbalance is greater than zero → A = 30

For sellers, if shares to sell outnumber shares to buy in a market, the sellers earnings in that market can be negative

The following example illustrates the use of your record sheet:

Example. Your choice is 3 to Market X and 7 to Market Y. In Market X, the buyers submit a total of 20 shares to buy, and sellers in total submit 15 shares to sell. The total imbalance in X is 20 - 15 = +5 (more shares to buy than to sell, so A = 30 for sellers and A = 60 for buyers), and the quantity in X is 35, so:

Seller Earnings per Share in Market X

$$
= 1 0 + 3 0 * (2 0 - 1 5) / 3 5 = 1 0 + 1 5 0 / 3 5 = 1 4. 2 9
$$

In Market Y, the buyers have submit a total of 20 shares to buy, and sellers in total have submit 25 shares to sell. The imbalance is -5 (more shares to sell than to buy and A = 60 for sellers), and

Seller Earnings per Share in Market Y

$$
\begin{array}{l} = 1 0 + A * (\text { Imbalance   in   Market } X) \\ = 1 0 + 6 0 * (2 0 - 2 5) / 4 5 = 1 0 - 3 0 0 / 4 5 = 3 3 3 \end{array}
$$

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Sample Record Sheet for Seller 0

<table><tr><td>Market</td><td>Your Choice:</td><td>B Total To Buy</td><td>S Total To Sell</td><td> $I = B - S$  Total Imbalance</td><td> $A = {30}_{t - 0}$  or  ${60}_{t - 0}$ </td><td> $Q = B + S$  Total Quantity</td><td> $P = {10} + A * I/Q$  Profit Per Share</td><td>P*X and P*Y Total Profit</td></tr><tr><td colspan="9">Period</td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Work Out the Total Profit in these Examples

Example 1. Your choice is 4 to Market X and 6 to Market Y. In Market X, the buyers submit a total of 8 shares to buy, and sellers in total submit 19 shares to sell. In Market Y, the buyers have submit a total of 32 shares to buy, and sellers in total have submit 21 shares to sell.

Example 2. Your choice is 0 to Market X and 10 to Market Y In Market X, the buyers submit a total of 6 shares to buy, and sellers in total submit 9 shares to sell In Market Y, the buyers have submit a total of 34 shares to buy, and sellers in total have submit 31 shares to sell

Sample Record Sheet for Seller 0

<table><tr><td>Market</td><td>Your Choice:</td><td>B Total To Buy</td><td>S Total To Sell</td><td> $I = B - S$  Total Imbalance</td><td> $A = {30}_{1 \leq 0}$  or  ${60}_{1 \leq 0}$ </td><td> $Q = B + S$  Total Quantity</td><td> $P = {10} + A * I/Q$  Profit Per Share</td><td>P*X and P*Y Total Profit</td></tr><tr><td colspan="9">Period</td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="9">Period:</td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Instructions for Game I

All traders have an assigned quantity of 10 shares to trade. The total number of shares in the market is 80. You are asked to decide what amount between 0 and 10 to submit to each of the markets. The earnings calculation is applied to each market separately according to the function at the top of your record sheet. Mark the separate amounts for Market X and Market Y on your record sheet. When you are ready, an experimenter will walk by to note your quantity.

Once all the choices are made, buyer and seller quantities for both markets in that round will be announced Market X is subject to “disruptions” and will only have a 50% chance of trades occurring in a particular round. An ordinary coin will be flipped, and heads will indicate that Market X is open Tails will mean that there is no trading in Market X, and earnings will be zero Market Y has no disruptions and trading will always occur.

Record Sheet For Seller \_\_\_\_

<table><tr><td colspan="9">Game I</td></tr><tr><td>Market</td><td>Your Choice:</td><td>B Total To Buy</td><td> $I = S$  Total To Sell</td><td> $A = B - S$  Total Imbalance</td><td> $Q = {30}_{I < 0}$  or  ${60}_{I - 0}$ </td><td> $P = B + S$  Total Quantity</td><td>P*X and 10 + A*I/Q Profit Per Share</td><td>P*Y Total Profit</td></tr><tr><td>Period</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>X:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Instructions for Game II

An alternative market, Market W, is now available that has lower transactions costs per share than Market X or Market Y. Earnings will be calculated on your record sheet in a similar way, except that Market W's earnings function is $14 + A \times I/Q$ for sellers and $14 - A \times I/Q$ for buyers, I and Q are determined by the orders submitted to Market W

The market that had the largest quantity in the last period of Game I—Market \_\_\_\_— has the same earnings function as before 10 ± A\*I/Q, where I and Q are determined by the orders submitted to this market. The smaller market at the end of Game I is no longer available

In Game II, you continue to divide your submission across the markets in any way you want. After everyone has made their choices, buyer and seller quantities for that round will be announced. Mark these on your record sheet, and determine your profits. The earnings calculation is applied to each market separately according to the functions given on your record sheet

Record Sheet For Seller \_\_\_\_

<table><tr><td colspan="9">Game II</td></tr><tr><td>Market</td><td>Your Choice:</td><td>B Total To Buy</td><td>S Total To Sell</td><td> $I = B - S$  Total Imbalance</td><td> $A = {30}_{l=0}$  or  ${60}_{l}$ </td><td> $Q = B + S$  Total Quantity</td><td> $P = {10} + A * I/Q$   ${14} + A * I/Q$  Profit/Shr</td><td>P* and P*W Total Profit</td></tr><tr><td>Period.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>W</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total:</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Total Earnings

<table><tr><td colspan="2">Game I</td></tr><tr><td>Periods 1–6</td><td>_</td></tr><tr><td>Periods 7–12</td><td>_</td></tr><tr><td>Sub-Total</td><td>_</td></tr><tr><td colspan="2">Game II</td></tr><tr><td>Periods 1–6</td><td>_</td></tr><tr><td>Periods 7–12</td><td>_</td></tr><tr><td>Sub-Total</td><td>_</td></tr><tr><td>Total</td><td>_</td></tr><tr><td colspan="2">Divide TOTAL by 120 and round up to nearest U.S. dollar (eg 1,820 is $15.17, which rounds to $16)</td></tr><tr><td>$ Total</td><td>_</td></tr></table>

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

## Questions

What did you feel was the likely difference in outcomes by submitting 10 shares to one market or 5 to both markets?

In Game I, how did you decide initially (Round 1) what amounts to submit to Market X and Market Y?

In Game II, how did you think the outcomes would change as a result of the different costs in the two markets?

## References

Amuhud, Y. and H. Mendelson, "An Integrated Computerized Trading System," in Y. Amuhud, T. Ho, and R. Schwartz (Eds), Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985

— and —, "Trading Mechanisms and Stock Returns An Empirical Investigation," J. Finance, 42 (1987), 533–553.

— and —, "Liquidity, Volatility and Exchange Automation," J Accounting, Auditing & Finance, Fall (1988), 369–395

—, T. Ho, and R. Schwartz, "Overview of the Changing Securities Markets," in Y. Amihud, T. Ho, and R. Schwartz (Eds), Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985.

Bakos, J. Y., "Information Links and Electronic Marketplaces: The Role of Interorganizational Information Systems in Vertical Markets," J. Management Information Systems, 8, 2 (1991), 31–52.

Black, F., "Toward a Fully Automated Exchange," Financial Analysts J., July–August (1971), 29–44, and November–December (1971), 25–29. Boston Globe, "NYSE Steps Toward 24-Hour Trading," September 9, 1990.

Box, G., W. Hunter, and J. Hunter, Statistics for Experimenters. Design, Analysis, and Model Building, Wiley, New York, 1978.

Clemons, E. and B. Weber, "London's Big Bang: A Case Study of Information Technology, Competitive Impact, and Organizational Change," J. Management Information Systems, 6, 4 (1990), 41–60.

Cohen, K., R. Conroy, and S. Maier, "Order Flow and the Quality of the Market," in Y. Amihud, T. Ho, and R. Schwartz (Eds.), Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985

—, S. Maier, R. Schwartz, and D Whitcomb, The Microstructure of Securities Markets, Prentice-Hall, Englewood Cliffs, NJ, 1986

Conroy, R. and R. Winkler, "Informational Differences Between Limit and Market Orders for a Market Maker," J. Financial and Quantitative Analysis, 16, 1981, 703–724

—— and ——, "Market Structure: The Specialist as Dealer and Broker," J. Banking and Finance, 10, 1986, 21–36.

Davis, J, "The Intermarket Trading System and the Cincinnati Experiment," in Y. Amuhud, T. Ho, and R. Schwartz (Eds.), Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985.

Domowitz, I., "Automating the Price Discovery Process: Some International Comparisons and Regulatory Implications," J. Financial Services Res., 6 (1993), 305–326.

Economides, N. and A. Siow, "The Division of Markets is Limited by the Extent of Liquidity (Spatial Competition with Externalities)," American Economic Review, 78, 1 (1988), 108–121.

Garbade, K., "The Effect of Interdealer Brokerage on the Transactional Characteristics of Dealer Markets," J. Business, 51, 3 (1978), 477–498 — and W. Silber, "Technology, Communication and the Performance of Financial Markets: 1840–1975," J Finance, 33, 3 (1978), 819–831

— and —, "Structural Organization of Secondary Markets: Clearing Frequency, Dealer Activity, and Liquidity Risk," J. Finance, 34, 3 (1979), 577–593.

Garman, M., "Market Microstructure," J. Financial Economics, 3 (1976), 257–275

Hakansson, N., A Beja, and J Kale, "On the Feasibility of Automated Market Making by a Programmed Specialist," J Finance, 40 (1985), 1–20

Hansell, S., "The Wild, Wired World of Electronic Exchanges," Institutional Investor, September (1989), 91–115

Ho, T and R Macris, "Dealer Market Structure and Performance," in Y Amihud, T. Ho, and R Schwartz, Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985

Katz, M and C Shapiro, "Technology Adoption in the Presence of Network Externalities," J. Political Economy, 94, 4 (1986), 822–841.

Keynes, J M, The General Theory of Employment, Interest, and Money, Harcourt, Brace & Co, New York, 1936.

Mendelson, H., "Random Competitive Exchange. Price Distributions and Gains from Trade," J. Economic Theory, 37 (1985), 254–280.

Mendelson, M., "From Automated Quotes to Automated Trading: Restructuring the Stock Market in the U.S," New York University Bulletins Nos. 80–82, 1972.

—, "Consolidation, Fragmentation, and Market Performance," J. Financial and Quantitative Analysis, 22 (1987), 189–207

New York Stock Exchange, Fact Books, 1989–1994

"NYSE·1989 and Beyond An Overview of an Academic Seminar," May 5, 1989, New York Stock Exchange

NYSE Research Department, Research correspondence, October 1990

Pagano, M., "Trading Volume and Asset Liquidity," Quarterly J. Economics, 104 (1989), 255–274

Peake, J., M. Mendelson, and R. Williams, Jr., "Toward a Modern Exchange: The Peake-Mendelson-Williams Proposal for an Electronically Assisted Auction Market," in E. Bloch and R. Schwartz (Eds), Impending Changes for Securities Markets—What Role for Exchanges?, JAI Press, Greenwich, CT, 1979.

Plott, C., "Rational Choice in Experimental Markets," J. Business, 59, 4, Part 2 (1986), S301–S327.

Schwartz, R., "An Electronic Call Market. Its Design and Desirability," in H. Lucas, Jr. and R. Schwartz (Eds.), The Challenge of Information Technology for the Securities Markets: Liquidity, Volatility, and Global Trading, Dow Jones-Irwin, Homewood, IL, 1989

Schwert, G. W., "Stock Market Volatility," NYSE Working Paper #89-02, December 1989.

Smith, V., "Microeconomic Systems as an Experimental Science," American Economic Review Proceedings, 1982, 923–955

Straub, P., "Risk Dominance and Coordination Failures in Static Games," Quarterly Review of Economics and Finance, 35, 4 (1995), 339–363.

Waters, R., "Rawlins Points to Hybrid System," Financial Times, October 2, 1990, 12

Weber, B., Information Technology and Securities Markets·Feasibility and Desirability of Alternative Electronic Trading Systems, unpublished dissertation, University of Pennsylvania, Philadelphia, PA, 1991

Williams, S., "The Evolving National Market System," in Y Amihud, T. Ho, and R. Schwartz (Eds.), Market Making and the Changing Structure of the Securities Industry, Lexington Books, Lexington, MA, 1985

Barrie R. Nault, Associate Editor. This paper was received on December 2, 1993, and has been with the authors 9 months for 3 revisions
