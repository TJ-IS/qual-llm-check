---
otero_id: 28610
otero_key: "VU7F9RF3"
title: "Player-vs.-Player Game Design and Pricing: A Tournament Design Perspective"
authors: "Haowen Deng; Yifan Dou; Zenan Wu; Cheng Zhang"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0258"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Player-vs.-Player Game Design and Pricing: A Tournament Design Perspective

Haowen Deng,<sup>a</sup> Yifan Dou,<sup>a</sup> Zenan Wu,<sup>b,</sup>\* Cheng Zhang<sup>a</sup>

<sup>a</sup> School of Management, Fudan University, Shanghai 200433, China; <sup>b</sup> School of Economics, Sustainability Research Institute, Peking University, Beijing 100871, China

\*Corresponding author

Contact: hwdeng20@fudan.edu.cn, https://orcid.org/0000-0001-5373-3003 (HD); yfdou@fudan.edu.cn, https://orcid.org/0000-0002-0516-3250 (YD); zenan@pku.edu.cn, https://orcid.org/0000-0001-6079-0778 (ZW); zhangche@fudan.edu.cn, https://orcid.org/0000-0002-8277-5138 (CZ)

Received: April 27, 2023 Revised: February 3, 2024; August 31, 2024 Accepted: September 18, 2024 Published Online in Articles in Advance: October 25, 2024

https://doi.org/10.1287/isre.2023.0258

Copyright: © 2024 INFORMS

Abstract. Player-versus-player (PvP) games often allow users to purchase superior virtual gears to increase their winning odds in battles against others. This game design, known as “pay to win,” generates substantial revenues from paying players, but it may also adversely affect the gaming experience of nonpaying players and lead to a decline in the game’s popularity. Game developers thus need to strike a balance between revenue and player participation. This paper develops a model to analyze optimal versioning and pricing strategies for PvP games. Building on the classic product line design framework with network effects, we allow a monopolistic game developer to strategically manipulate gameplay (dis-)advantages across different versions, which we refer to as tournament design, and this generates version-specific network effects. We characterize the developer’s optimal strategy and obtain the following insights. First, tournament design improves the developer’s flexibility in pricing and versioning, and it effectively mitigates the extent of product cannibalization. Second, tournament design enables the developer to monetize free players’ participation by offering multiple free versions, and a “freemium” strategy (i.e., the combination of a free-to-play model and a pay-to-win system) can arise in the optimum. Third, tournament design is particularly effective in increasing the developer’s profit when players are willing to play the game but are reluctant to pay. Fourth, tournament design leads to a Pareto improvement for both the developer and all players. The practical implications of these findings are also discussed.

History: Ravi Bapna, Senior Editor; Atanu Lahiri, Associate Editor.

Funding: This research was supported by the National Natural Science Foundation of China [Grants 72222002, 72173002, and 72033003]; the Research Seed Fund of the School of Economics, Peking University; the Wu Jiapei Foundation of the China Information Economics Society [Grants E21100383 and M22106023]; and the National Social Science Fund of China [Grant Major Project 21&ZD119]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0258.

Keywords: online games • tournament design • versioning • network effects

## 1. Introduction

Online gaming has grown exponentially in recent decades, and it has surpassed the movie and music industries combined in terms of profitability (Divers 2023).<sup>1</sup> Among online games, player-versus-player (PvP) games, in which gamers compete against other gamers, are a significant genre. Numerous PvP games adopt the “pay-towin” business model (Lelonek-Kuleta et al. 2021). Users play for free while having the option to pay for superior versions or advanced gears to improve their winning odds and gain an advantage over those playing for free (Guo et al. 2019, Meng et al. 2021). For instance, League of Legends has more than 150 avatars (called “champions”), and around 10% are free. Players can spend real cash on unlocking new champions to deepen their champion pool, which improves their versatility, their adaptability, and thus, their winning rates (Ekroslim 2024).

The pay-to-win practice has bred challenges for PvP game developers. First, pay-to-win is a double-edged sword because it monetizes paying players at the risk of alienating free players. Adopting pay-to-win generates a negative network effect—which can be strategically manipulated by the developer through game design— on free players’ gaming experience. Paying players competitive advantage, which affects their gaming experience, becomes less attractive if free players are handicapped excessively and leave the game. Second, using pay-to-win to encourage payment is challenging because of a prevailing resistance among players to purchase digital content (Wang et al. 2023). Consumers are willing to play video games, but they are reluctant to pay as underscored by numerous surveys conducted by app developers and service providers (Salehudin and Alpert 2022). It is reported that about 75% of Americans play games, with weekly playing hours steadily increasing from 12.7 in 2019 to 16.5 in 2021 on average (NPD 2021), but paying players account for only 2.2% (Sinclair 2014).

To investigate how game developers may overcome these challenges and configure the pay-to-win business model effectively, we need a model that (i) enables the design of game balance—which we refer to as tournament design and yields endogenous heterogeneous network effects—and (ii) captures the discrepancy between players’ willingness to play and willingness to pay. The traditional wisdom in the literature fails to provide a quick solution because these features have yet to be formally considered. Our paper aims to fill this void.

For example, prior studies on versioning with network effects typically abstract away consumer interaction and assume that the marginal network value from an additional user is exogenous and constant. Based on these premises, the literature advocates for the idea of a “freemium” strategy. Serve consumers with low willingness to pay an inferior free version and monetize their participation through the provision of a premium paid version that targets those with high willingness to pay (e.g., Gu et al. 2018, Meng et al. 2021).<sup>2</sup> In PvP games, players who use a free version would be worse off when the game developer adopts the pay-to-win business model because they would be at a disadvantage in a battle when their opponent uses a premium paid version. This important feature because of player interaction has not been incorporated in the classic versioning literature. It is a priori unclear whether the freemium strategy continues to be effective in the PvP context, in which the developer faces a fundamental trade-off between the gaming experience of free players and that of paying players (Wang et al. 2023).

This paper extends the classical literature on versioning with network effects (e.g., Bhargava and Choudhary 2008, Shi et al. 2019) by allowing the game developer to manipulate player interaction and thus, the network effects through tournament design. As is commonly assumed in the literature, the game developer can offer game versions with different stand-alone qualities (i.e., purely cosmetic virtual items with different levels of desirability in the PvP context). In addition, we allow the developer to manipulate the competitive balance of battles between players who select different versions. To capture players’ reluctance to pay, we assume that some players have a tight budget for the game.

Our analysis is not only relevant practically but also, theoretically interesting. First, the two design instruments differ in their nature. Choosing a quality level for a version is unidimensional, whereas designing the game balance requires tilting the winning rates of the version against all other versions and is inherently multidimensional. Solving for the developer’s optimal strategy profile is thus technically challenging. Second and importantly, because the developer can improve a player’s gaming experience by increasing the quality of a version and/or promising higher winning rates, it is intriguing to investigate how tournament design inter acts with quality design. Do they substitute or complement each other? Prior literature offers limited insights because it typically focuses on product design within a single dimension. We show that the answer to this question hinges crucially on players’ reluctance to pay. The two instruments are substitutes, and tournament design is unnecessary to achieve the maximum profit when all players have an adequate budget. However, they play complementary roles when a positive fraction of players has a tight budget for the game. That is, the optimum requires quality differentiation and manipulation of the winning rates.

Our analysis yields the following insights. First, tournament design expands the developer’s business toolbox and improves its flexibility in pricing and versioning (Proposition 3). This provides a rationale for the diverse game designs and pricing strategies observed in practice—in particular, the commonly adopted freemium business model. Second, tournament design enables the developer to segment free users and cater to their different preferences through the provision of multiple free versions (Proposition 4). This effectively monetizes their participation and drives the developer’s profitability. Third, as noted above, tournament design serves as a powerful tool to circumvent players’ financial limitations and address their reluctance to pay (Propositions 5 and 6). Game developers can thus counteract the negative impact of policies regarding payment restrictions on certain groups of players (e.g., underage players) to maintain profitability through tournament design. Finally, leveraging network effects through tournament design not only expands market reach, but also, it boosts developer profits and enhances player satisfaction (Proposition 7). These insights offer a fresh perspective for understanding the freemium and pay-to-win mechanisms, and they yield useful managerial implications for game developers’ balance between player monetization and their retention.

The remainder of the paper is organized as follows. Section 2 reviews the related literature. Section 3 introduces the model setup and illustrates the role of tournament design through a simple example. Section 4 characterizes the developer’s optimal strategy. Section 5 extends the model and provides further discussion of the implications of tournament design, and Section 6 concludes.

## 2. Related Literature

Our study is connected to four strands of the literature: (i) product line design and versioning, (ii) pricing strategy for information goods, (iii) tournament/ contest design, and (iv) video game design.

This paper contributes to the extensive product line design literature (Mussa and Rosen 1978, Maskin and Riley 1984, Moorthy 1984, Moorthy and Png 1992), especially regarding information goods with network effects (Shapiro and Varian 1999, Varian 2000, Bhargava and Choudhary 2008, Wu and Chen 2008). Prior studies focus on a unidimensional design problem and encompass aspects such as vertical differentiation (Jing 2007, Jones and Mendelson 2011, Wei and Nault 2013), horizontal differentiation (Choudhary 2010, Wei and Nault 2014), and product bundling (Bakos and Brynjolfsson 1999). Our research advances this literature by considering a multidimensional design problem. We examine a monopolistic firm’s strategy of offering products with two attributes—intrinsic qualities that provide stand-alone value for players and competitive advantages of the product over others—and their interplay. Design of the latter attribute has not been explored in the literature, and our study aims to fill this gap.

The second strand concerns firms’ pricing strategies for information goods (Wu et al. 2003, Chellappa and Shivendu 2005, Etzion and Pang 2014, Shivendu and Zhang 2015), with a focus on firms’ incentives to adopt a freemium model (Liu et al. 2014, Xu et al. 2018) and its variations (Dey et al. 2013, Dou et al. 2013, Niculescu and Wu 2014, Cheng et al. 2015). Providing a free version effectively expands the user base (Kumar 2014, Kamada and O<sup>¨</sup> ry 2020), but it also cannibalizes the sales of premium versions (Moorthy 1984, Desai 2001, Liu et al. 2014, Shi et al. 2019). Jing (2007) shows that for products that feature network effects, the market expansion effect tends to outweigh the cannibalization effect, and network effects reinforce the seller’s incentive to adopt the freemium strategy. Shi et al. (2019) further examine the role of heterogeneity in network effects among versions to identify the profitability of the freemium model.

We extend this strand of the literature in two respects. First, the network effects in these studies are exogenous and/or homogeneous for different versions, whereas they are endogenous in our model and can be manipulated by the game developer through tournament design. We show that tournament design enables the seller to generate and benefit from asymmetric network effects, which mitigate market cannibalization and render freemium an attractive strategy. Second, we formally model the difference between users’ willingness to play and willingness to pay, which is widely documented (Gallaugher et al. 2001, Wang et al. 2023) but rarely integrated into the analysis of the pricing of information goods. Our results highlight the role of tournament design in improving the developer’s flexibility in pricing and circumventing users’ financial limitations.

Our study also contributes to the economic literature on tournament/contest design (Lazear and Rosen 1981). The literature has highlighted the importance of various design instruments to tilt the balance of compe tition, such as favoritism (Epstein et al. 2011; Franke et al. 2013, 2014; Fu and Wu 2020), head starts (Kirkegaard 2012, Drugov and Ryvkin 2017), and bid caps (Che and Gale 1998, Gavious et al. 2002, Olszewski and Siegel 2019, Fu et al. 2023). Conventionally, a contest designer varies contestants’ relative standings through interventions based directly on their individual characteristics. In contrast, the competitive (dis-)advantages that players receive in our model depend on the ver sion that they select. To the best of our knowledge, our research is among the first to bridge the versioning literature and that on tournament design.

Our study also adds to the burgeoning literature on video game design. Chen et al. (2022) consider a model in which players have different skill levels and analyze how dynamic matchmaking affects players’ winning odds and their retention decision in PvP games. They show that incorporating a pay-to-win model shifts the skill distribution among players and can improve engagement when the majority of players are low skilled. Mai and Hu (2023) examine optimal strategies for pricing premium content and advertising in free-to-play games. They reveal an important trade-off between monetization and player retention. It is worth noting that the versioning decision in both studies is exogenous, whereas its endogenization is the focus of our paper.

## 3. Model and Preliminaries

This section presents the fundamentals of the model followed by a simple example that illustrates the role of tournament design.

## 3.1. Model Setup

A monopolistic developer offers a set of game versions, which we denote by ${ \bf \hat { \mathcal { K } } } : = \left\{ 1 , \ldots , K \right\}$ , with $K \geq 1$ . The intrinsic quality of each version $i \in \mathcal { K }$ is $s _ { i } \in [ \underline { { s } } , \overline { { s } } ] .$ , with $\overline { { s } } > \underline { { s } } > 0$ , and the price is $p _ { i } \geq 0$ . The quality bounds s and s, respectively, represent the minimum market requirement and the maximum quality achievable by the developer.<sup>3</sup> Given that online games are a typical information good, the production costs for each version are assumed to be negligible and normalized to zero (Shapiro and Varian 1999).

3.1.1. Player Preferences and Budget Constraints. Consider a unit mass of potential players. Each one demands no more than one copy of the game, and the outside option (i.e., being a nonbuyer) yields zero utility. Players are heterogeneous in two dimensions: (i) the marginal valuation of game quality, represented by $\theta \sim \Breve { \mathbf { U } } ( 0 , 1 )$ , and (ii) the budget allocated for game purchase, denoted by $m \in \{ \underline { m } , \overline { m } \} . ^ { 4 }$ The parameter θ influences a player’s willingness to play, whereas m determines their ability to pay. Among type θ players, a fraction $\beta \in ( 0 , 1 )$ faces a tight budget $m \geq 0 ,$ whereas the remainder has an adequate budget m, which 5 enables them to choose from all available versions. More formally, we assume throughout this paper that $m > \overline { { { s } } } + \overline { { { e } } } + \overline { { { v } } } ,$ , where e and v are introduced later. Note that the budget constraint becomes more restrictive with an increase in $\beta$ or a decrease in m. In what follows, we first proceed with the worst-case scenario of $\underline { m } = 0$ for the developer, in which budget-constrained players only consider playing if a free version is available. The scenario of $\underline { m } > 0$ will be analyzed in Section 5.3.

A player derives utility from two sources: (i) the joy of playing the game irrespective of the outcome of the $\mathrm { P v P }$ battles and (ii) the joy of winning (or the disutility of losing). Consider a type θ player who selects version $i \in K .$ . Building on the framework of Jing (2007), we assume that the first part of the utility is $\theta s _ { i } + Q e$ . The parameter e is a positive coefficient, and Q is the total installed base that measures the popularity of the game. The term $\theta s _ { i }$ stands for the stand-alone benefits derived from playing the game (i.e., the utility that a player derives from avatar customization and/or in-game skill development). The term Qe accounts for the network utility derived from player interactions (i.e., the utility that a player derives from forming friendships and socializing in the gaming community) (Mai and Hu 2023, Wang et al. 2023). A more popular game (i.e., a game with a larger total installed base Q) provides more opportunities for such interactions and enhances the overall gaming experience.

Further, the player derives an expected payoff $\omega _ { i }$ from competition, which can be either positive or negative and will be specified in detail below. Note that a player’s competitive outcome (e.g., winning percentage) in many PvP games is visible to peers (e.g., via the player leaderboard, as in Liu et al. 2013 and Tobon et al. 2020), which may affect the utility from winning or disutility from losing. To capture the idea that players are more sensitive to the outcome of competition in a popular game than in an outdated one, we posit that the second part of a player’s utility equates to $Q \omega _ { i } .$ . In Online Appendix D.2, we show that our conclusions remain intact if the multiplier $Q$ is dropped (e.g., if a player’s competitive performance cannot be observed by others) and the second part of player utility reduces to ω .

3.1.2. The PvP Game. We consider PvP games in which players engage in one-on-one battles. Players receive a utility $v > 0$ upon winning and incur a disutility $d > 0$ upon losing. For simplicity, we assume that matchups are determined through a random matching process from the entire player base, which ensures anonymity in opponent selection (Mai and Hu 2023).

With random matching, the probability of a player encountering an opponent with version j is $\mu _ { j } : = Q _ { j } / Q$ where $Q _ { j } \geq \bar { 0 }$ denotes the population of players using version j and $\begin{array} { r } { Q \equiv \sum _ { k \in \mathcal { K } } Q _ { k } } \end{array}$ is the total installed base. The probability of a version i player defeating a version j player is denoted by $\lambda _ { i j } : = ( 1 / 2 ) + t _ { i j } ,$ , where $t _ { i j } \in$ $[ - \hat { 1 } / \dot { 2 } , 1 / 2 ]$ reflects the competitive advantage of version i over version j and can be controlled by the game developer. The playing field is level if $t _ { i j } = 0 .$ , biased toward version i if $t _ { i j } > 0$ , and favors version j if $t _ { i j } < 0$

## 3.2. Preliminary Analysis and Assumption

We lay out some preliminaries and assumptions and formalize the developer’s design problem.

3.2.1. Players’ Willingness to Play and Pay. It follows immediately that the aforementioned expected payoff from competition for a player who chooses version $i \in \mathcal { K } ,$ , which depends on player composition $Q : = [ Q _ { 1 }$ $\ldots , Q _ { K } ] .$ , is

$$
\begin{array}{l}\omega_{i}(Q_{1},\ldots ,Q_{K}) = \sum_{j\in \mathcal{K}}\underbrace{\mu_{j}}_{\substack{\text{probability of playing}\\ \text{against a version} j\text{player}}}\\ \left(\underbrace{\lambda_{ij}}_{\substack{\text{probability of winning}\\ \text{a battle}}}\times v - \underbrace{(1 - \lambda_{ij})}_{\substack{\text{probability of losing}\\ \text{a battle}}}\times d\right)\\ = \frac{v - d}{2} +\frac{v + d}{Q}\times \sum_{j\in \mathcal{K}}t_{ij}Q_{j}. \end{array}
$$

A type θ player’s willingness to play for version i is then

$$
\begin{array}{l} \mathcal {W T P} _ {i} (\theta) := \underbrace {\theta s _ {i} + Q e} _ {\text {Joy of playing the game}} + \underbrace {Q \omega_ {i} (Q _ {1} , \ldots , Q _ {K})} _ {\text {Joy of winning the game}} \\ = \quad \theta s _ {i} + \left(e + \frac {v - d}{2}\right) Q + (v + d) \sum_ {j \in \mathcal {K}} t _ {i j} Q _ {j} \\ = \underbrace {\theta s _ {i}} _ {\text {base benefit of playing}} + \underbrace {\overline {{e}} Q} _ {\text {uniform network effect}} \\ + \underbrace {\overline {{v}} \sum_ {j \in \mathcal {K}   t _ {i j}} Q _ {j}} _ {\text {version - specific network effect}}, \end{array}\tag{1}
$$

where $\overline { { e } } : = e + ( ( v - d ) / 2 )$ and ${ \overline { { v } } } : = v + d .$ . The term $\overline { { e } } Q$ adheres to the conventional network effect (e.g., Fudenberg and Tirole 2000, Prasad et al. 2010, Cheng and Liu 2012), which depends on the total installed base but not on the version that a player selects. The term $\overline { { v } } \sum _ { j \in \mathcal { K } } t _ { i j } Q _ { j }$ introduces a nuanced network effect that results from battles between players, which depends on both player composition and the version that a player selects.

Central to our analysis is a player’s willingness to pay, which we define as the lower value of a player’s will ingness to play, as specified in Equation (1), and their budget for the game $m \in \{ \underline { { m } } , \overline { { m } } \}$ . More formally, a type θ player’s willingness to pay for version i is min{WT P<sub>i</sub>(θ), m}:

It is straightforward to verify that a player’s willingness to pay equals the player’s willingness to play, provided that m is sufficiently large. For a financially constrained player, the willingness to pay falls below the willingness to play, which potentially restrains the game’s profitability for the developer. The type θ player chooses the affordable version i that provides the highest net utility:<sup>6</sup>

$$
U _ {i} (\theta) := \mathcal {W T P} _ {i} (\theta) - p _ {i}.\tag{2}
$$

3.2.2. Timeline, Developer’s Problem, and Tournament Design. The timeline consists of two stages. In the first stage, the developer, anticipating players’ purchasing decisions, chooses the number of versions $K \bar { \in } \mathbb { N } ^ { + }$ . These versions are characterized by a triad of parameters: the intrinsic qualities $\pmb { s } : = \left[ s _ { 1 } , \ldots , s _ { K } \right]$ , the prices $p : = [ p _ { 1 } , \ldots ,$ $p _ { K } ]$ , and the following competitive balance matrix:

$$
\mathcal {T} := \left[ \begin{array}{c} \mathcal {T} _ {1} \\ \mathcal {T} _ {2} \\ \vdots \\ \mathcal {T} _ {K} \end{array} \right] \equiv \left[ \begin{array}{c c c c} t _ {1 1} & t _ {1 2} & \dots & t _ {1 K} \\ t _ {2 1} & t _ {2 2} & \dots & t _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ t _ {K 1} & t _ {K 1} & \dots & t _ {K K} \end{array} \right]
$$

$$
= \left[ \begin{array}{c c c c} 0 & - t _ {2 1} & \dots & - t _ {K 1} \\ t _ {2 1} & 0 & \dots & - t _ {K 2} \\ \vdots & \vdots & \ddots & \vdots \\ t _ {K 1} & t _ {K 2} & \dots & 0 \end{array} \right].
$$

The element $t _ { i j }$ in the above matrix $\tau$ controls the competitive balance in a battle between version i and version $j .$ The design of $\tau$ is referred to as tournament design. Note that for each battle, the winning probability from two sides sums to one $( \mathrm { i . e . , } \lambda _ { i j } + \lambda _ { j i } = 1 )$ , which implies that $t _ { i j } = - t _ { j i }$ and $t _ { i i } = 0$ for all $i , j \in \dot { \mathcal { K } } .$

In the second stage, players make their purchasing decisions given the developer’s strategy profile $\{ K , s ,$ $p , T \}$ . More specifically, players form a belief about all others’ equilibrium purchasing decisions—which is summarized by the player composition $Q \equiv [ Q _ { 1 } , \dots ,$ $Q _ { K } ]$ —and make purchasing decisions accordingly based on their budget. We assume that players are aware of the competitive advantage of each version at the time of purchase. This assumption is grounded in practicality because such information is typically readily accessible to players. Developers and third-party platforms often provide detailed descriptions for different versions of their products. For example, comprehensive data on tanks in the game World of Tanks can be accessed through its official database, Tankopedia (Wargaming 2024), or the third-party tool Tanks.GG (Tanks.GG 2024).

Following the literature (Katz and Shapiro 1985, Jing 2007), we adopt the fulfilled expectation equilibrium as the solution concept, which requires that the realized player composition coincides with players’ expectations prior to purchase. As is well known in the literature, multiple equilibria may exist in games with network effects. To proceed, we assume that the developer is restricted to choosing strategy profiles under which a stage 2 equilibrium exists and that the equilibrium most favorable to the developer is selected whenever multi ple equilibria exist.

In summary, the game developer decides on the strategy profile $\{ K , s , \check { p } , \mathcal { T } \}$ and earns profits $p _ { i } Q _ { i }$ from the provision of version i. Its profit-maximizing problem is thus formulated as follows:

$$
\max _ {\{K, s, p, \mathcal {T} \}} \Pi := \sum_ {i \in \mathcal {K}} p _ {i} Q _ {i}.
$$

To ensure that the role of winning/losing is not overshadowed by other elements in a player’s utility, we assume a moderate positive network effect e to guarantee that the market is not fully covered. Therefore, the developer needs to strike a balance between player monetization and participation. Further, we assume that $v$ and $d$ are sufficiently large to ensure that victories/ defeats in battles are important in shaping players decisions. More formally, the following assumption is imposed throughout our analysis.

Assumption 1. $\begin{array} { r } { 0 < \overline { { e } } \equiv e + \frac { v - d } { 2 } < \frac { s } { 2 } a n d \overline { { v } } \equiv v + d > \frac { 2 \overline { { s } } } { 1 - \beta } . } \end{array}$

## 3.3. An Illustrative Example

To elaborate on the role of tournament design most cleanly, we first present a simple setting in which all players have an adequate budget, and then, we intro-

3.3.1. Market Without Budget-Constrained Players. We start with a simple two-group example. Players have adequate budget (that is, $\beta = 0 ( \mathrm { i . e . }$ , their willingness to play and their willingness to pay coincide)) and differ only in the marginal valuation of the cosmetic quality $\theta \in \{ 0 . 2 , 1 \}$ , each of equal size. Further, quality takes binary values $s \in \{ 1 . 2 , 2 \}$ }, and we set $e = 0 . 5$ and $v =$ $d = 4$ . By Equation (2), a type θ player’s utility of selecting version $i \in \{ 1 , 2 \}$ is $\begin{array} { r } { \bar { U } _ { i } ( \theta ) \bar { = \theta _ { S _ { i } } } + Q / 2 + \bar { 8 } t _ { i j } Q _ { j } - p _ { i } } \end{array}$ with $j \neq i .$

We first present a benchmark fair game case $( t _ { i j } = 0 )$ The version-specific network effect $8 t _ { i j } Q _ { j }$ fades away, and the above utility simplifies to $\dot { U } _ { i } ( \dot { \boldsymbol { \theta } } ) = \theta s _ { i } + Q \dot { / } 2$ $- p _ { i } ,$ in line with the framework presented by Jing (2007). We deduce that the uniform network effect enables the developer to segment the market through vertical differentiation, and versioning is optimal. The developer offers two versions: a low-quality version 1 $( s _ { 1 } = 1 . \bar { 2 } )$ that targets group 1 players and a high-quality version $2 \left( s _ { 2 } = 2 \right)$ that targets group 2 players. The associated pricing scheme $( p _ { 1 } , p _ { 2 } ) = ( 0 . 7 4 , \bar { 1 } . 5 4 )$ results in an aggregate profit of 1.14, as shown in Figure 1(a). Under optimal pricing, group 1 players choose version 1, and group 2 players choose version 2. The developer collects all consumer surplus from group 1 players while leaving each group 2 player a positive surplus of 0.96.

Note that adopting a freemium strategy in the benchmark fair game case is suboptimal. To see this, suppose that the developer offers the low-quality version 1 for free (i.e., reduces its price from 0.74 to 0) and keeps the price of the high-quality version 2 unchanged. This not only leaves a positive surplus of 0.74 to group 1 players but also, renders the high-quality version 2 less appealing and causes cannibalization. In order to sell the high-quality version 2 to group 2 players, the developer has to reduce its price from 1.54 to 0.8, as depicted in Figure 1(b); otherwise, group 2 players would turn to version 1. Compared with the optimal pricing, as shown in Figure 1(a), the developer’s profit decreases as the prices of both products decrease by 0.74.

Next, consider the case in which the developer can manipulate the game balance. We show that tournament design helps overcome issues of cannibalization, and the freemium strategy can arise in the optimum. This involves a two-step adjustment to the suboptimal freemium strategy delineated in Figure 1(b). First, the developer modifies the winning probabilities in favor of players who select version 2 by setting $t _ { 2 1 } = 0 . 1 8 5$ , as shown in Figure 1(c). This reallocates a surplus of 0.74 from group 1 players to group 2 players, assuming that players’ purchasing behaviors remained unchanged. Second, to ensure that group 1 players have no incentives to turn to version 2, the developer raises the price of version 2 to 2.28, as depicted in Figure 1(d). Comparing panels (a) and (d) of Figure 1, this two-step adjustment enables the developer to earn the same amount of profits as in the benchmark fair game case without charging group 1 players, and a freemium strategy arises in the optimum. Note that profit cannot be further improved with tournament design because the total installed base has reached its maximum, in which case tilting competitive balance simply transfers winning rates and thus, utilities across versions.

Thus far, we have shown through a simple example without budget-constrained players that tournament design improves the developer’s flexibility in pricing and versioning. Note that such flexibility does not translate into additional profits. The maximum profit with tournament design equals that without tournament design. Next, we show that tournament design is a valuable addition to the toolkit for the developer and unlocks its profit potential in the presence of budgetconstrained players.

Figure 1. (Color online) Developer’s Strategy and Market Segmentation with or Without Tournament Design (β50)  
![](/api/attachments/VU7F9RF3/fulltext/images/a736b9ac62c2c092d42e4b2f6882b7ba583f227459c0f1f6fcc6eb4e7f02ad09.jpg)  
Notes. (a) Vertical differentiation (fair game). (b) Freemium and cannibalization (fair game). (c) Freemium with tournament design (step 1). (d) Freemium with tournament design (step 2).

Table 1. Market Segmentation with Tournament Design (β�0:1)

<table><tr><td>Players</td><td>Version selected</td><td>Price</td><td>Quality</td><td>Net utility</td></tr><tr><td>Group 1 with a tight budget</td><td>Low-quality free version</td><td>0</td><td>1.2</td><td>0</td></tr><tr><td>Group 2 with a tight budget</td><td>High-quality free version</td><td>0</td><td>2</td><td>0.96</td></tr><tr><td>Group 1 with an adequate budget</td><td>Low-quality paid version</td><td> $13/15 \approx 0.87$ </td><td>1.2</td><td>0</td></tr><tr><td>Group 2 with an adequate budget</td><td>High-quality paid version</td><td> $5/3 \approx 1.67$ </td><td>2</td><td>0.96</td></tr></table>

3.3.2. Market with Budget-Constrained Players. We continue with the previous setting except that we now assume that 10% of each group of players has a tight budget $( \mathrm { i . e . , } \beta = 0 . 1 )$ . First, consider the benchmark case without tournament design. By an argument similar to that laid out above, we can show that adopting a freemium strategy causes severe cannibalization and is suboptimal. Under the profit-maximizing strategy, the developer offers two versions: (i) a low-quality version $( s = 1 . { \overset { \vartriangle } { 2 } } )$ at a price of 0.69 that targets group 1 players and (ii) a high-quality version $( s = 2 )$ at a price of 1.49 that targets group 2 players. In the equilibrium, only players with an adequate budget are served, whereas those with a tight budget are not. This yields a profit of 0.981 $( = 0 . 6 \overset { \smile } { \boldsymbol { 9 } } \times ( 1 / 2 \stackrel { \smile } { \times } 9 0 \% ) + 1 . 4 9 \times \bar { ( 1 / 2 \times 9 0 \% ) } )$ ) for the developer.

Next, we show that tournament design enables the developer to earn strictly more profits. To see this, consider the following strategy profile (which is the profitmaximizing strategy profile for this example). Instead of two versions, the developer now offers four versions (see Table 1): (i) a free low-quality version $( s = 1 . 2 )$ that targets group 1 players with a tight budget, (ii) a highquality free version $( s = 2 )$ that targets group 2 players with a tight budget, (iii) a paid low-quality version $( s = 1 . 2 )$ at a price of $1 3 / 1 5 \approx 0 . 8 7$ that targets group 1 players with an adequate budget, and (iv) a paid highquality version $( s = 2 )$ at a price of $5 / 3 \approx 1 . { \bar { 6 7 } }$ that targets group 2 players with an adequate budget. The winning rates between versions $( \mathrm { i . e . , } \ \lambda _ { i j } )$ are specified in Table 2.

It can be verified that in the equilibrium, all players are served and optimally select the affordable version that the developer wants them to choose. For example, group 1 players with a tight budget—who do not value cosmetic quality as much as group 2 players—would opt for the low-quality free version rather than the high-quality free version because the former has highe winning rates (see the first two rows in Table 2). It is noteworthy that with tournament design, the developer is able to charge players a higher price. Consider, for example, group 1 players. They are charged a price of 0.69 without tournament design and a price of 0.87 with tournament design. These players are willing to pay more because (i) tournament design enables the developer to leverage network effects and increase the game’s popularity by including players with a tight budget and (ii) they receive a gameplay advantage over their budget-constrained opponents. This yields a profit of 1.14 $( = 1 3 / 1 5 \times ( 1 / 2 \stackrel { \cdot } { \times } 9 0 \% ) + 5 / 3 \times \stackrel { . } { ( } 1 / 2 \times$ $9 0 \% )$ , which is strictly higher than the maximum profit of 0.981 earned by the developer without tournament design.

## 4. Analysis and Results

In this section, we consider the fully fledged model and characterize the developer’s optimal strategy.<sup>8</sup> For expositional convenience, we call players with budget $\overline { { m } } > \overline { { s } } + \overline { { e } } + \overline { { v } }$ regular players and those with budget m � 0 free-only players. The former players constitute a fraction of $1 - \beta$ in the population, and the latter players constitute a fraction of $\beta .$ Note that the traditional versioning model (e.g., Jing 2007) is nested as a special case, in which $\beta$ approaches zero, in our setting.

We first simplify and reformulate the developer’s design problem. Fixing a developer’s strategy profile $\{ K , s , p , T \}$ , denote the sets of versions selected by freeonly and regular players in equilibrium by $\ = \kappa _ { \ / F }$ and $\displaystyle \mathcal { K } _ { R } ,$ respectively. Note that the versions contained in the set $\ = \kappa _ { \ / F }$ that target free-only players should all be free; otherwise, free-only players cannot afford them. Further, the prices of versions contained in the set $\displaystyle { \mathcal { K } } _ { R }$ that target regular players are not necessarily positive and can be zero (free versions are evidently affordable for regular players). The following lemma significantly simplifies the search for the developer’s optimal strategy.

Table 2. Winning Rates Chart

<table><tr><td></td><td>Low-quality free version, %</td><td>High-quality free version, %</td><td>Low-quality paid version, %</td><td>High-quality paid version, %</td></tr><tr><td>Low-quality free version</td><td>50</td><td>50</td><td>143/360 ≈ 39.72</td><td>143/360 ≈ 39.72</td></tr><tr><td>High-quality free version</td><td>50</td><td>50</td><td>103/360 ≈ 28.61</td><td>103/360 ≈ 28.61</td></tr><tr><td>Low-quality paid version</td><td>217/360 ≈ 60.28</td><td>257/360 ≈ 71.39</td><td>50</td><td>50</td></tr><tr><td>High-quality paid version</td><td>217/360 ≈ 60.28</td><td>257/360 ≈ 71.39</td><td>50</td><td>50</td></tr></table>

Note. This table presents the winning rates of each row version playing against different column versions

Lemma 1. The maximum profit can be achieved by a strategy profile $\{ K , s , p , T \}$ , wherein the versions chosen by the two groups of players in equilibrium are nonoverlapping $( i . e . , \bar { \mathcal { K } } _ { F } \cap \mathcal { K } _ { R } = \emptyset )$

By Lemma 1, one way to generate the maximum profit is to adopt strategies that lead to an equilibrium in which free-only and regular players do not have overlap in their choices of game versions. The proof of the lemma indicates that tournament design (i.e., the design of the competitive balance matrix $\check { \tau } )$ gives the developer flexibility in its strategy design. We might then conjecture that there exists an alternative profitmaximizing strategy under which some free-only and regular players select the same version. This possibility is confirmed later in Section 5.1.

Denote the number of versions chosen by free-only players by $\widehat { K } \geq 0$ . By Lemma 1, $K - { \widehat K } \geq 1$ gives the number of versions chosen by regular players. If freeonly players choose to participate $( \mathrm { i . e . , } \ \overset { \vartriangle } { K } \geq 1 )$ , we set $\mathcal { K } _ { F } \overset { \vartriangle } { = } \dot { \left\{ 1 , \dots , K \right\} }$ and ${ \mathcal { K } } _ { R } \stackrel { \bullet } { = } \{ \widehat { K } + \stackrel { \bullet } { 1 } , \ldots , \widehat { K } \}$ without loss of generality.<sup>9</sup>

By standard technique, we can show that players equilibrium purchasing decision can be characterized by a set of cutoffs $\pmb { \theta } : = [ ( \theta _ { 1 } , \varrho _ { - } , \varrho _ { \widehat { K } } ) , ( \theta _ { \widehat { K } + 1 } , \cdot \cdot . . , \theta _ { K } ) ]$ , with $0 \leq \theta _ { 1 } < \cdots < \theta _ { \widehat { \kappa } } < 1$ and $0 \leq \ddot { \theta } _ { \widehat { K } + 1 } < \cdots < \theta _ { K } < 1$ , as Figure 2 illustrates.<sup>10</sup> The equilibrium demand for each version is

$$
Q _ {i} = \left\{ \begin{array}{l l} \beta (\theta_ {i + 1} - \theta_ {i}), & i \in \mathcal {K} _ {F} \setminus \{\widehat {K} \}, \\ \beta (1 - \theta_ {\widehat {K}}), & i = \widehat {K}, \\ (1 - \beta) (\theta_ {i + 1} - \theta_ {i}), & i \in \mathcal {K} _ {R} \setminus \{K \}, \\ (1 - \beta) (1 - \theta_ {K}), & i = K. \end{array} \right.\tag{3}
$$

We can treat the equilibrium cutoffs as design variables and reformulate the developer’s design problem as follows. The developer chooses the total number of versions $K ,$ the number of versions that target free-only players ${ \widehat K } ,$ , the quality profile $s ,$ the set of equilibrium cutoffs $\mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } }$ the price schedule $^ { p , }$ , and the competitive bal ance matrix $\tau$ to solve the following optimization problem:<sup>11</sup>

$$
\max _ {\{(K, \widehat {K}), s, \pmb {\theta}, p, \mathcal {T} \}} \Pi \equiv \sum_ {i \in \mathcal {K}} p _ {i} Q _ {i},\tag{4}
$$

$$
\text { subject   to } \quad U _ {i} (\theta_ {i}) = U _ {i - 1} (\theta_ {i}), \forall i \in \mathcal {K} \setminus \{1, \widehat {K} + 1 \},\tag{5}
$$

$$
\max _ {i \in \mathcal {K} _ {R} \cup \{0 \}} U _ {i} (\theta) \geq U _ {j} (\theta), \forall j \in \mathcal {K} _ {F}, \theta \in [ 0, 1 ],\tag{6}
$$

$$
U _ {i} (\theta_ {i}) \geq 0, \text {   and   } U _ {i} (\theta_ {i}) \theta_ {i} = 0, i \in \{1, \widehat {K} + 1 \},\tag{7}
$$

$$
p _ {i} = 0, \forall i \in \mathcal {K} _ {F},\tag{8}
$$

$$
p _ {i} \geq 0, \forall i \in \mathcal {K} _ {R},\tag{9}
$$

$$
0 \leq \theta_ {1} <   \dots <   \theta_ {\widehat {K}} <   1 \text {   if   } \widehat {K} \geq 1 \text {   and   }
$$

$$
0 \leq \theta_ {\widehat {K} + 1} <   \dots <   \theta_ {K} <   1,\tag{10}
$$

$$
- \frac {1}{2} \leq t _ {i j} \leq \frac {1}{2}, \forall i \neq j, t _ {i i} = 0, \forall i \in \mathcal {K}.\tag{11}
$$

Constraint (11) sets the limit for tournament design, which requires that a player’s winning probability in a battle does not exceed one. Three constraints deserve attention. Constraint (5), the incentive compatibility (IC) constraint, mandates that players at the thresholds are indifferent between the two adjacent versions, which ensures that regular and free-only players choose within the choice sets $\displaystyle { \mathcal { K } } _ { R }$ and $\ = \kappa _ { \ / F } , \ =$ , respectively. Constraint (6) is the second IC constraint, which guarantees that regular players have no incentive to select a free version from $\ = \kappa _ { \ / F }$ that targets free-only players. Constraint (7) is the individual rationality constraint and requires that when the market for free-only (regular) players is not fully covered $( \mathrm { i . e . , }$ when $\theta _ { 1 } > 0 ( \bar { \theta _ { K + 1 } } > \bar { 0 ) ) }$ , players with the lowest threshold type $\theta _ { 1 } ( \theta _ { \widehat { K } + 1 } )$ should remain indifferent between buying version 1 (version $\widehat { K } )$ and opting out. The remaining constraints (i.e., Constraints (8), (9), and (10)) are regularity conditions for prices and equilibrium cutoffs.

Figure 2. (Color online) Players’ Equilibrium Purchasing Decision  
![](/api/attachments/VU7F9RF3/fulltext/images/7126d26fdb9456ebf5ff0b0012708b787c0bb48f9dd8d17c1296b4847fd1023a.jpg)

## 4.1. Developer’s Optimal Strategy Without Tournament Design

We first consider the benchmark fair game case $( \mathrm { i . e . , }$ $\mathcal { T } = \mathbf { 0 } )$ . A players’ net utility (2) reduces to

$$
U _ {i} (\theta) \equiv \mathcal {W T P} _ {i} (\theta) - p _ {i} = \theta s _ {i} + \overline {{e}} Q - p _ {i}.\tag{12}
$$

The optimal strategy (marked with superscript †) is given by the following proposition.<sup>12</sup>

Proposition 1 (Optimal Strategy Without Tournament Design). For the benchmark case without tournament design $( i . e . , T = \mathbf { 0 } )$ , it is optimal for the developer to offer two versions: (i) a low-quality version 1 with quality s and price $\underline { s } / 2$ and (ii) a high-quality version 2 with quality s and price $\overline { { s } } / 2$ . In the equilibrium, regular players with $\theta \in [ \theta _ { 1 } ^ { \dagger } , \theta _ { 2 } ^ { \dagger } )$ optimally choose version 1, and those with $\theta \in [ \theta _ { 2 } ^ { \dagger } , 1 ]$ choose version 2, where $\begin{array} { r } { \theta _ { 1 } ^ { \dagger } = 1 - \frac { s } { 2 [ \underline { { s } } - \overline { { e } } ( 1 - \beta ) ] } < \theta _ { 2 } ^ { \dagger } = \frac { \mathrm { 1 } } { 2 } } \end{array}$ : The maximum profit is

$$
\Pi^ {\dagger} = \frac {(1 - \beta) [ \underline {{s}} \overline {{s}} - \overline {{e}} (1 - \beta) (\overline {{s}} - \underline {{s}}) ]}{4 [ \underline {{s}} - \overline {{e}} (1 - \beta) ]}.
$$

Figure 3 illustrates the equilibrium in Proposition 1. The two versions are maximally differentiated in terms of quality s to minimize cannibalization. Note that the developer has no incentive to provide three or more versions because the introduction of a new version causes severe market cannibalization and reduces the developer’s profit. This observation is consistent with Jing (2007). Further, it is straightforward to verify that providing a single (paid) version to players generates a strictly lower profit for the developer. Therefore, two is the minimum and the unique number of versions without tournament design.

A closer look at the proposition yields the following corollary, which serves as a benchmark for the analysis when tournament design is allowed.

Corollary 1 (Equilibrium Properties Without Tournament Design). The equilibrium without tournament design (i.e., $\mathcal { T } = \mathbf { 0 } )$ has the following properties.

Figure 3. (Color online) Equilibrium Market Segmentation Without Tournament Design (Two Versions)  
![](/api/attachments/VU7F9RF3/fulltext/images/15556794b3333f3e61c9b57fc74bd39e7257a42b5234a944e7966395a1c7ba53.jpg)

i. (Suboptimality of freemium) The developer does not offer free versions $( i . e . , \stackrel { \wedge } { K } ^ { \dagger } = 0 )$ , and thus, free-only player are not served.

ii. (Impact of players’ budgets) The total installed base and the developer’s maximum profit $\Pi ^ { \dagger }$ decrease with the fraction of free-only players $\beta ( i . e . , \partial \Pi ^ { \dagger } / \partial \beta < 0 )$

Corollary 1(i) indicates that free-only players would be left out even with zero marginal cost, echoing the insights of Shi et al. (2019, proposition 1). This is attributed to the well-known cannibalization effect, whereby introducing a free version undermines the profit earned from others. The diminishing installed base, as noted in Corollary 1(ii), stems from the fact that the developer tends to decrease the market coverage for regular players $( \mathrm { i . e . , } ( 1 - \theta _ { 1 } ^ { \dagger } )$ is decreasing in $\beta )$ as the fraction of free-only players, $\beta ,$ becomes larger. This is because the developer is less motivated to leverage network effects. In summary, without tournament design, the presence of free-only players—or more broadly, the discrepancy between players’ willingness to play and their willingness to pay—undermines the developer’s profitability.

## 4.2. Developer’s Optimal Strategy with Tournament Design

Next, we allow the developer to manipulate the competitive balance matrix and characterize the optimal strategy. To prepare for the solution to the optimization problem laid out previously, we first solve for a relaxed problem without Constraints (6), (9), and (11) and obtain the following lemma. It can be verified that the optimal solution to the relaxed problem also solves the original problem. The following lemma simplifies the search for the competitive balance matrix T .

Lemma 2. Fixing an arbitrary profile $\{ ( K , \widehat { K } ) , s , \pmb { \theta } , p , T \}$ there exists an alternative profile $\{ ( K , \widehat { K } ) , s , \pmb { \theta } , p ^ { \sharp } , T ^ { \sharp } \}$ that satisfies all constraints in the relaxed problem and generates the same profit for the developer. Moreover, the competitive balance matrix $\dot { \tau } ^ { \sharp }$ satisfies the following.

i. Battles between players of paid versions are fair $( i . e . ,$ $t _ { i j } ^ { \natural } = 0 f o r a l l i , j \in \mathcal { K } _ { R } )$

ii. Battles between players of free versions are fair (i.e., ${ t } _ { i j } ^ { \natural } = 0 f o r a l l i , j \in \mathcal { K } _ { F } )$

iii. All paying players’ competitive advantages against any free player are identical $( i . e . , T _ { i } ^ { \natural } = T _ { j } ^ { \natural }$ for all $i , j \in \mathcal { K } _ { R } )$

By Lemma 2, the maximum profit can be achieved by multiple strategy profiles, which again, indicates the flexibility that the tournament design allows the developer, as in Lemma 1. The developer’s optimization over the competitive balance matrix $\tau$ can then be simplified to searching for the vector $\pmb { \tau } : = ( \tau _ { 1 } , \dots ,$ $\tau _ { \widehat { K } } )$ that generates the following competitive balance

matrix:

$$
\mathcal {T} := \left[ \begin{array}{c c c c c c} 0 & \dots & 0 & - \tau_ {1} & \dots & - \tau_ {1} \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & \dots & 0 & - \tau_ {\widehat {K}} & \dots & - \tau_ {\widehat {K}} \\ \hline \tau_ {1} & \dots & \tau_ {\widehat {K}} & 0 & \dots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \tau_ {1} & \dots & \tau_ {\widehat {K}} & 0 & \dots & 0 \end{array} \right],\tag{13}
$$

where the first $\widehat { K }$ rows represent the competitive advantages of the free versions and the remaining rows represent those of the paid versions. By Lemma $2 , ( \mathrm { i } )$ and (ii), the submatrix at the upper left and that at the bottom right are both zero matrices. Further, by Lemma 2(iii), the competitive advantages of all paid versions over free version $i \in \mathcal { K } _ { F }$ are identical and equal to $\tau _ { i } .$

The following proposition characterizes the optimal strategy profile (marked with the superscript \*) when the game developer incorporates tournament design into the strategy.

Proposition 2 (Optimal Strategy with Tournament Design). The maximum profit can be achieved by providing four versions: (i) a free and low-quality version 1 with quality $\underline { { s } } , ( \mathrm { i i } )$ a free and high-quality version 2 with quality s, (iii) a lowquality version 3 with quality $\underline { s }$ and positive price $p _ { 3 } ^ { * } =$ $\frac { ( \overline { { 1 } } - \beta ) \underline { { s } } ^ { 2 } + \beta \overline { { s } } \underline { { s } } - \beta \overline { { e } } ( \overline { { s } } - \underline { { s } } ) } { 2 ( 1 - \beta ) \underline { { s } } } .$ , and (iv) a high-quality version 4 with quality s and positive price $\begin{array} { r } { p _ { 4 } ^ { * } = \frac { \overline { { s } } _ { \underline { { s } } - \bar { \beta } \overline { { e } } ( \overline { { s } } - \underline { { s } } ) } } { 2 ( 1 - \beta ) \underline { { s } } } . } \end{array}$ . The associated competitive balance matrix is

$$
\mathcal {T} ^ {*} \equiv \left[ \begin{array}{c} \mathcal {T} _ {1} ^ {*} \\ \mathcal {T} _ {2} ^ {*} \\ \mathcal {T} _ {3} ^ {*} \\ \mathcal {T} _ {4} ^ {*} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & - \tau_ {1} ^ {*} & - \tau_ {1} ^ {*} \\ 0 & 0 & - \tau_ {2} ^ {*} & - \tau_ {2} ^ {*} \\ \tau_ {1} ^ {*} & \tau_ {2} ^ {*} & 0 & 0 \\ \tau_ {1} ^ {*} & \tau_ {2} ^ {*} & 0 & 0 \end{array} \right],
$$

where $\begin{array} { r } { \tau _ { 1 } ^ { * } = \frac { \underline { { s } } - \overline { { e } } } { \overline { { v } } ( 1 - \beta ) } } \end{array}$ and $\begin{array} { r } { \tau _ { 2 } ^ { * } = ( \overline { { s } } / \underline { { s } } ) \times \frac { \underline { { s } } - \overline { { e } } } { \overline { { v } } ( 1 - \beta ) } . } \end{array}$ . In the equilibrium, free-only players with $\theta \in \left[ \theta _ { 1 } ^ { * } , \theta _ { 2 } ^ { * } \right)$ optimally choose version 1, and those with $\theta \in [ \theta _ { 2 } ^ { * } , 1 ]$ choose version $^ { 2 , }$ where $\theta _ { 1 } ^ { * } =$ $\displaystyle \frac { \underline { { s } } - 2 \overline { { e } } } { 2 ( \underline { { s } } - \overline { { e } } ) }$ and $\begin{array} { r } { \theta _ { 2 } ^ { * } = \frac { 1 } { 2 } ; } \end{array}$ regular players with $\theta \in \left[ \theta _ { 3 } ^ { * } , \theta _ { 4 } ^ { * } \right)$ optimally choose version $^ { 3 , }$ and those with $\theta \in [ \theta _ { 4 } ^ { * } , 1 ]$ choose version $^ { 4 , }$ where $\begin{array} { r } { \theta _ { 3 } ^ { * } = \theta _ { 1 } ^ { * } = \frac { s - 2 \overline { { e } } } { 2 ( \underline { { s } } - \overline { { e } } ) } } \end{array}$ and $\begin{array} { r } { \theta _ { 4 } ^ { * } = \theta _ { 2 } ^ { * } = \frac { 1 } { 2 } . } \end{array}$ . The developer’s maximum profit is

$$
\Pi^ {*} = \frac {\overline {{s}} \underline {{s}} - \overline {{e}} (\overline {{s}} - \underline {{s}})}{4 (\underline {{s}} - \overline {{e}})}.\tag{14}
$$

Figure 4 illustrates the findings from Proposition $^ { 2 , }$ which suggest that the developer can maximize profits by segmenting the group of free-only players and the group of regular players simultaneously, each with two versions. Versions 1 and 2 are free versions that target free-only players, whereas versions 3 and 4 are paid versions that target regular players. Intuitively, segmenting each group with three or more versions causes severe market cannibalization and reduces the developer’s profit. Although both versions 1 and 2 are free, players have different preferences over them. Version 2 has higher quality, whereas version 1 has higher winning rates. By creating this trade-off, the developer can further segment free players. This enables the developer to better leverage network effects and extract more profits from regular players. It should be noted that four is not the minimum number of versions with tournament design. The number of versions can be reduced to three; more discussion will be provided in Section 5.1.

Figure 4. (Color online) Equilibrium Market Segmentation with Tournament Design (Four Versions)  
![](/api/attachments/VU7F9RF3/fulltext/images/a77ed7ec30665076c71174b7a0b4a880bb90f904f6d448eb6088f8084c4771ba.jpg)

A simple comparison between the profit established in Proposition 1 $( \mathrm { i . e . , } \Pi ^ { \dag } )$ and that established in Propo sition $\bar { 2 } ( \mathrm { i . e . , } \Pi ^ { * } )$ yields that $\Pi ^ { \dagger } \leq \Pi ^ { * }$ , where the inequal ity holds with equality if and only $\mathrm { i f } \ \beta = 0$ . This implies that the profit-maximizing equilibrium outcome can only be achieved by manipulating the competitive balance between versions if the market consists of budget constrained players $( \mathrm { i . e . , i f } \ \beta > 0 )$ ). When all players have an adequate budget, the flexibility in pricing and versioning that tournament design offers the developer cannot improve its profitability, as shown in the illustrative example in Section 3.3. This observation high lights the importance of tournament design in driving the developer’s profitability in the presence of budgetconstrained players.

Note that the competition between players who select different paid (free) versions is fair under the optimal strategy (i.e., $t _ { 1 2 } ^ { * } = t _ { 3 4 } ^ { * } = 0 )$ ; in contrast, the competitive balance goes against the free-version players when they are matched with one who selects a paid version $( \mathrm { i . e . , }$ $t _ { 1 3 } ^ { * } = t _ { 1 4 } ^ { * } = - \tau _ { 1 } ^ { * } < 0$ and $t _ { 2 3 } ^ { * } = t _ { 2 4 } ^ { * } = - \tau _ { 2 } ^ { * } < 0 )$ ). Here, $\tau _ { 1 } ^ { * }$ and $\tau _ { 2 } ^ { * }$ measure the degree of gameplay fairness. A larger $\tau _ { 1 } ^ { * }$ or $\tau _ { 2 } ^ { * }$ suggests a more pronounced imbalance in the competition between a player using the free version and the opponent using a paid version. The following result ensues.

Corollary 2 (The Value of Free-Only Players). As the frac tion of free-only players $\beta$ increases, the developer increase the winning rates of paying players $( i . e . , \ partial \tau _ { 1 } ^ { * } / \partial \beta > 0$ and $\partial \tau _ { 2 } ^ { * } / \partial \beta > 0 )$ and charges them higher prices $( i . e . , \partial p _ { 3 } ^ { * } / \partial \beta > 0$ and $\partial p _ { 4 } ^ { * } / \partial \beta > 0 )$ ).

Section 4.2 sheds light on the strategic value of freeonly players. Recall by Section 4.1 that free-only players are not served absent tournament design and thus, create zero value for the game developer. However, when tournament design is incorporated, they will be served and result in an increase in the game’s popularity. Therefore, the developer should take them into consideration when designing the strategy. Note that an increase in the fraction of free-only players $\beta$ triggers two effects. First, the probability of a free-only player who chooses free version 1 or 2 being matched with a regular player who selects paid version 3 or 4 is $1 - \beta .$ Therefore, ceteris paribus, an increase in β implies that a free-only player is less likely to engage in battles against a regular player, which increases the expected payoff. This leaves room for the developer to further adjust the competitive balance in favor of regular players—which is impossible without tournament design—and at the same time, keep free-only players. Second and analogously, the probability of a regular player with version 3 or 4 being matched with a free-only player who selects version 1 or 2 is $\beta .$ An increase in $\beta ,$ ceteris paribus, also increases regular players’ expected payoff. This allows the developer to charge higher prices for paid versions.

## 5. Extension, Discussion, and Implications

Our previous analysis paves the way for comparison of the developer’s optimal strategy with tournament design and that without tournament design. In this section, we extend the model and provide further discussion of the implications of tournament design.

## 5.1. Enhanced Flexibility in Pricing and Versioning

We first demonstrate that incorporating tournament design improves flexibility in pricing and versioning decisions for the game developer and expands the spectrum of optimal strategies. Put differently, when the game developer’s pricing and versioning decisions are restrained (e.g., because of “menu costs” or government intervention), the developer can redesign the game balance to generate the same amount of profits. Recall that Proposition 2 provides one strategy profile to generate the maximum profit. The following result confirms that the same profit can be achieved through an alternative strategy profile (marked with the superscript ∗∗).

Proposition 3 (Multiple Profit-Maximizing Strategies with Tournament Design). The maximum profit can be achieved by multiple strategy profiles, and they all lead to the same equilibrium market segmentation (i.e., the threshold type for regular players and those for free-only players are identi cal across all optimal strategy profiles) and the same equilib rium payoff to every player. In particular, the developer can offer three versions to obtain the same profit as in Proposition $2 \colon ( \mathrm { i } )$ a free low-quality version 1 with quality s, (ii) a free high-quality version 2 with quality s, and (iii) a high-quality version 3 with quality s and positive price $\begin{array} { r } { p _ { 3 } ^ { * * } = \frac { \overline { { s } } \underline { { s } } - \overline { { ( \overline { { s } } } - \underline { { s } } ) \overline { { e } } } ^ { * } } { 2 ( 1 - \beta ) ( \underline { { s } } - \overline { { e } } ) } . } \end{array}$ The associated competitive balance matrix is

$$
\mathcal {T} ^ {* *} = \left[ \begin{array}{c c c} 0 & 0 & - \tau_ {1} ^ {* *} \\ 0 & 0 & - \tau_ {2} ^ {* *} \\ \tau_ {1} ^ {* *} & \tau_ {2} ^ {* *} & 0 \end{array} \right],
$$

where $\begin{array} { r } { \tau _ { 1 } ^ { * * } = \frac { \underline { { s } } } { \overline { { v } } ( 1 - \beta ) } } \end{array}$ and $\begin{array} { r } { \tau _ { 2 } ^ { * * } = \frac { \overline { { s } } } { \overline { { v } } ( 1 - \beta ) } . } \end{array}$ In the equilibrium, both free-only and regular players with $\theta \in \left[ \theta _ { 1 } ^ { \ast } , \theta _ { 2 } ^ { \ast } \right)$ ) choose version 1, where $\theta _ { 1 } ^ { \bar { * } }$ and $\boldsymbol { \theta } _ { 2 } ^ { * }$ are defined in Proposition 2. Further, free-only players with $\theta \in \left[ \theta _ { 2 } ^ { * } , 1 \right]$ choose version 2, and regular players with $\theta \in [ \theta _ { 2 } ^ { * } , 1 ]$ choose version 3.

Figure 5 illustrates the alternative profit-maximizing strategy profile provided in Proposition 3. It is noteworthy that the properties stated in Lemmas 1 and $^ { 2 , }$ which Proposition 2 relies on, no longer hold. To see this, first note that the choice set of free-only players now overlaps with that of regular players. Free version 1 is selected by both free-only and regular players. Second, competition between regular players who choose different versions is no longer fair. The developer now tilts the competitive balance to favor version 3 players when they compete against version 1 players. Despite these differences, the optimal strategies established in Propositions 2 and 3 share the same insights. With tournament design, free-only players are crucial for the developer’s profitability and are served.

Proposition 3 suggests that tournament design fosters versatility in the developer’s pricing and versioning strategies, and thus, it provides a rationale for the diverse game designs and pricing strategies observed in practice. To illustrate the versatility more explicitly, consider regular players with $\theta \in \left[ \theta _ { 1 } ^ { \ast } , \theta _ { 2 } ^ { \ast } \right)$ . Under the strategy outlined in Proposition 2, they are charged positive price $p _ { 3 } ^ { * }$ and receive a gameplay advantage over players using a different version. Conversely, under the strategy stated in Proposition 3, they play for free but are at a disadvantage in competition.

Figure 5. (Color online) Equilibrium Market Segmentation with Tournament Design (Three Versions)  
![](/api/attachments/VU7F9RF3/fulltext/images/ecee2747d80dd07a904c0055029f66292f53ffcb7780a7dd3a315c365623aacc.jpg)

Proposition 3 also sheds light on the minimum number of versions with tournament design. To see this, recall that the threshold types for regular players and those for free-only players are identical across all profit-maximizing strategy profiles. Therefore, free-only players and regular players each buy two versions in the equilibrium under the developer’s optimal strategy profile. If the versions chosen by the two groups of players are nonoverlapping, the number of versions is four, as shown in Proposition 2. If they are partially overlapping, then the number of versions can be three, as demonstrated in Proposition 3. Indeed, three is the minimum number of versions and cannot be further reduced to two (offering a single version is clearly suboptimal). Otherwise, the choice set of free-only players completely overlaps with that of regular players. This indicates that both versions are priced at zero and result in zero profits for the developer.

## 5.2. Optimality of Freemium and Multiple Free Versions with Tournament Design

Despite the flexibility in versioning and pricing caused by tournament design, as shown in Proposition 3, the optimality of the freemium model and the provision of multiple free versions holds across all profit-maximizing strategies.

Proposition 4 (Optimality of Freemium and Multiple Free Versions). The freemium strategy, when integrated with tournament design, can be optimal. Meanwhile, offering a single free version is suboptimal, and the developer should provide multiple free versions, each distinct in terms of quality and competitive advantages.

Proposition 4 stands in stark contrast to Corollary 1(i), which establishes the suboptimality of freemium absent tournament design. As previously noted, although serving free-only players by providing a free version is costless and increases market demand—which enables the developer to leverage network effects and charge higher prices for paid versions—it also causes severe market cannibalization and generates a loss in sales. Corollary 1(i) indicates that the latter market cannibalization effect outweighs the former demand-boosting effect without tournament design, and it is suboptimal to adopt the freemium strategy. Proposition 4 suggests that the detrimental cannibalization effect can be mitigated once the developer is able to manipulate the competitive balance, which renders the freemium strategy optimal. This is because the game balance, when configured appropriately, plays a similar role of cross-subsidization. Recall the version-specific network effect $\overline { { v } } \sum _ { j \in \mathcal { K } } t _ { i j } Q _ { j }$ <sub>j</sub> in a player’s willingness to play for version i (see Equation (1)). With tournament design, the developer is able to vary the competitive balance $t _ { i j } .$ . Under the optimal strategy, the developer “taxes” (“subsidizes”) free-only (regular) players by decreasing (increasing) their winning rates, which leads to a decrease (increase) in their willingness to play.<sup>13</sup> This way, the developer can charge higher prices for paid versions in comparison with the case without tournament design.<sup>14</sup> In summary, deliberate tournament design and adjustments in prices effectively offset the loss in sales from market cannibalization caused by the release of free versions, and the freemium strategy arises in the optimum.

With tournament design, the developer can differentiate versions along three dimensions: quality $s _ { i } ,$ price $p _ { i } ,$ and the competitive (dis-)advantage over other versions $\mathcal { T } _ { i } \equiv \left[ t _ { i 1 } , \dots , t _ { i K } \right]$ . The additional design instrument renders multidimensional product differentiation and the provision of multiple free versions possible. By Proposition 4, the developer offers multiple free versions and creates the trade-off between cosmetic qual ity and winning rates to segment free-only players. Note that it is unnecessary in a setting in which playe heterogeneity in the budget for the game is removed (see, e.g., the illustrative example in Section 3.3). Further, it is impossible in a setting in which player heterogeneity in the marginal valuation of the quality θ dissolves because all players have the same preference for virtual cosmetic items and thus, the same prefer ence for different free versions.

Our finding echoes and complements recent studies on network effects and freemium. In particular, Shi et al. (2019) investigate whether network effects alone can justify the freemium model. They show that freemium is suboptimal with uniform network effects and can arise in the optimum when there exists sufficient heterogeneity/asymmetry in network effects across vertically differentiated products. The marginal network value in their model is exogenous, whereas it is endogenous in our model and can be manipulated through tournament design. Corollary 1(i) confirms their first result under the assumption of an exogenous and fair game, whereas Proposition 4 complements their second result by showing that offering multiple free versions can be the optimal business model when the developer has an instrument to endogenize the asymmetry in network effects.

5.2.1. Multiple Free Versions in Practice. Although the possibility of offering multiple free versions is rarely mentioned in the literature and seems impractical at first glance, it has become a standard practice in the gaming industry. Table 3 provides a list of games that offer multiple free versions. PvP games, such as Honor of Kings and Clash of Clans, endow free players with limited in-game currency. The currency can be used to purchase premium skins or high-performance heroes/ gears (Meng et al. 2021). Premium skins enhance the overall gaming experience, regardless of the outcomes of battles, whereas high-performance heroes/gears elevate players’ winning rates. This approach inherently generates multiple free versions because players allocate their provided currency in diverse ways. Players who demand more (e.g., possessing both premium skins and high-performance heroes/gears) and are willing to pay have the option to invest real money in exchange for additional in-game currency and become regular players in our model.

Table 3. Popular Free-to-Play Games That Offer Multiple Free Versions

<table><tr><td>PvP game</td><td>Revenue (B)</td><td>Trade-offs for free players</td></tr><tr><td>Honor of Kings</td><td>2.2</td><td>Limited heroes vs. skins</td></tr><tr><td>League of Legends</td><td>1.8</td><td>Limited heroes vs. champion skins</td></tr><tr><td>Wargaming</td><td>1.1</td><td>Limited war machines vs. skins</td></tr><tr><td>Clash of Clans</td><td>0.5</td><td>Limited armies vs. hero skins</td></tr><tr><td>Dota 2</td><td>0.3</td><td>Limited decision support vs. skins</td></tr><tr><td>Clash Royale</td><td>0.2</td><td>Limited cards vs. battle banners</td></tr><tr><td>CrossFire</td><td>0.2</td><td>Limited weapons vs. skins</td></tr><tr><td>Hearthstone</td><td>0.06</td><td>Limited cards vs. hero skins</td></tr></table>

Notes. Refer to Table 4 in Online Appendix E for sources. ${ \mathrm { B } } ,$ billion U.S. dollars.

## 5.3. Addressing Players’ Reluctance to Pay with Tournament Design

Next, we examine the role of players’ budget constraints—or more generally, their reluctance to pay—in shaping the market outcome and its impact on the developer’s profit. Recall from Section 3.1 that $\beta$ refers to the fraction of players with a tight budget and that m gives the maximum amount that they are able to pay. Therefore, players’ reluctance to pay becomes more significant as $\beta$ increases or m decreases. We first investigate the role of β. A closer look at Propositions 2 and 3 yields the following.

Proposition 5 (Addressing Players’ Reluctance to Pay with Tournament Design). With tournament design, the total installed base and the developer’s profit Π<sup>∗</sup> remain constant as the fraction of free-only players $\beta$ increases.

Recall from Corollary 1(ii) that the presence of freeonly players curbs the developer’s profitability without tournament design. In contrast, Proposition 5 shows that the developer’s profit Π<sup>∗</sup> remains constant with respect to $\beta .$ Put differently, the detrimental impact of players’ reluctance to pay on the developer’s profitability can be completely removed by tournament design. Although serving free-only players does not directly accrue to profits for the developer, it increases the total installed base and generates a positive network effect. The developer can attract budget-sensitive players with free versions and extract their surplus through the design of competitive balance. By Section 4.2, as $\beta$ increases, the developer tilts the competitive balance toward regular players and charges them higher prices.

Next, we extend the model to consider a small but positive budget $\underline { m } > 0$ for those free-only players. For ease of exposition, we refer to them as “reluctant” players. Recall $( \tau _ { 1 } ^ { * } , \tau _ { 2 } ^ { * } )$ and $( \theta _ { 1 } ^ { * } , \theta _ { 2 } ^ { * } )$ defined in Proposition 2. We obtain the following result.

Proposition 6 (Optimal Strategy with Tournament Design with Reluctant Players). The maximum profit that the developer can obtain is independent of m and equal to Π<sup>∗</sup>, as defined in Equation (14). Further, the profit can be achieved by offering four versions: (i) a low-quality version 1 with quality s and a price ${ \tilde { p } } \in [ 0 , \underline { { m } } ]$ , (ii) a high-quality version 2 with quality s and the same price ${ \tilde { p } } ,$ (iii) a low-quality version 3 with quality s and a price $\begin{array} { r } { \tilde { p } _ { 3 } = \frac { ( 1 - \beta ) \underline { { s } } ^ { 2 } + \beta \overline { { s } } \underline { { s } } - \beta \overline { { e } } ( \overline { { s } } - \underline { { s } } ) } { 2 ( 1 - \beta ) \underline { { s } } } - \frac { \beta \tilde { p } } { 1 - \beta } , } \end{array}$ and (iv) a high-quality version 4 with quality s and a price $\tilde { p } _ { 4 } =$ $\begin{array} { r } { \frac { \overline { { s } } \underline { { s } } - \beta \overline { { e } } ( \overline { { s } } - \underline { { s } } ) } { 2 ( 1 - \beta ) \underline { { s } } } - \frac { \dot { \beta } \tilde { p } } { 1 - \beta } . } \end{array}$ . The associated competitive balance matrix is

$$
\tilde {\mathcal {T}} = \left[ \begin{array}{c c c c} 0 & 0 & - \tau_ {1} ^ {*} + \Delta_ {\tau} & - \tau_ {1} ^ {*} + \Delta_ {\tau} \\ 0 & 0 & - \tau_ {2} ^ {*} + \Delta_ {\tau} & - \tau_ {2} ^ {*} + \Delta_ {\tau} \\ \tau_ {1} ^ {*} - \Delta_ {\tau} & \tau_ {2} ^ {*} - \Delta_ {\tau} & 0 & 0 \\ \tau_ {1} ^ {*} - \Delta_ {\tau} & \tau_ {2} ^ {*} - \Delta_ {\tau} & 0 & 0 \end{array} \right],
$$

where $\begin{array} { r } { \Delta _ { \tau } = \frac { 2 \widetilde { p } ( \underline { { s } } - \overline { { e } } ) } { \underline { { s } } \overline { { v } } ( 1 - \beta ) } . } \end{array}$ . In the equilibrium, reluctant players with $\theta \in [ \theta _ { 1 } ^ { * } , \theta _ { 2 } ^ { * } )$ optimally choose version 1, and those with $\theta \in$ $[ \theta _ { 2 } ^ { * } , 1 ]$ choose version 2; regular players with $\theta \in \left[ \theta _ { 1 } ^ { * } , \theta _ { 2 } ^ { * } \right)$ optimally choose version 3, and those with $\theta \in [ \theta _ { 2 } ^ { * } , 1 ]$ choose version 4.

By Proposition $^ { 6 , }$ when reluctant players have a positive budget m, multiple pricing strategies generate the same maximum profit. In particular, the developer can charge any price below their budget (i.e., $\tilde { p } \in [ 0 , \underline { { m } } ] )$ given that the developer can redesign the competitive balance matrix $\tilde { \tau }$ . This observation again demonstrates the flexibility in pricing that tournament design grants the developer, as discussed in Section 5.1. Two remarks are in order. First, the developer does not earn additional profits from the relaxation of players’ budget constraint (i.e., an increase in m). This highlights and reaffirms the role of tournament design in addressing players’ reluctance to pay, which also demonstrates the robustness of our main results. Second and importantly, the profit-maximizing freemium strategy profile outlined in Proposition 2 in the case of $\underline { m } = 0$ remains optimal in the case of $\underline { m } > 0$ . This suggests that the optimality of offering free versions that we established in Section 4 is not driven by the assumption of $\underline { m } = 0$

Propositions 5 and 6 yield useful implications for the regulation of the online gaming industry. These results suggest that policies regarding payment restrictions on certain groups of players (e.g., underage players) might fail to work in the long run because game developers can attract nonpaying participation via free versions and derive value through tournament design. Consequently, regulators should consider alternative strategies, such as imposing limits on playing time, to effectively address gaming addiction if necessary.

## 5.4. Market Expansion and Win-Win Outcomes

Last, we investigate the welfare consequences of tournament design. Comparing Proposition 1 with Propositions 2 and 3 yields the following.

Proposition 7 (Win-Win). Compared with the benchmark fair game case $( \mathcal { T } = \mathbf { 0 } )$ , tournament design results in a winwin outcome. The developer’s profit increases, and every player’s surplus also (weakly) increases.

Proposition 7 indicates that tournament design results in a Pareto improvement. It is not surprising that the developer’s profit increases when in-game competition is allowed to be biased. However, it is somewhat striking that adding a design instrument to the developer’s toolbox also benefits players with low winning rates. In fact, Proposition 7 states an even stronger result, whereby every player is (weakly) better off, as visualized by Figure 6.

The intuition is as follows. First, tournament design allows the developer to capitalize more effectively on network effects, which thereby results in market expansion. Certain free-only players (i.e., those with $\theta \in [ \bar { \theta _ { 1 } ^ { * } } , 1 ] .$ as depicted in Figure $6 ( \mathsf { a } ) )$ and regular players $( \mathrm { i . e . } ,$ , those with $\mathbf { \hat { \theta } } \in [ \theta _ { 3 } ^ { * } , \theta _ { 1 } ^ { \dagger } ]$ , as shown in Figure 6(b)) are left out without tournament design, whereas they are served by the developer when tournament design is incorporated. $\mathrm { A s }$ these players choose to participate, their surplus increases unambiguously. Second, under tournament design, the developer charges higher prices (see footnote 14), which potentially reduce the welfare of regula players who participate without tournament design (i.e., those with $\boldsymbol { \theta } \dot { \in } [ \boldsymbol { \theta } _ { 1 } ^ { \dagger } , \dot { 1 } ]$ in Figure 6(b)). Nevertheless, they gain more from victories—thanks to the increase in winning rates set by the developer—with tournament design. These two effects completely offset each other under the developer’s optimal strategy. Note that these regular players also benefit from market expansion. As a result, their welfare also increases.

![](/api/attachments/VU7F9RF3/fulltext/images/799166b1c5ea4c18e03e75fd42e62a4b0b96b82cc99afb6b2262a0374c616656.jpg)  
Figure 6. (Color online) Player Surplus with or Without Tournament Design

## 6. Concluding Remarks

Although the online gaming industry is the secondlargest source of revenue (following digital advertising) in e-commerce, it remains largely unexplored in the literature. Following burgeoning research on the metaverse, this paper studies a novel aspect of manage ment in a virtual world: the interplay between game design and its pricing. A game developer is able to modify and control game settings that are traditionally unchangeable in the nonvirtual world, such as game balance in the PvP battles considered in this paper.

Building on the classic product line design framework a \` la Mussa and Rosen (1978), we characterize the optimal strategy for the game developer (Propositions 1 and 2). Our analysis yields several key insights. (i) Tournament design endows the developer with greater flexibility in both pricing and versioning (Proposition 3), and it provides a rationale for various video game designs and pricing strategies observed in the industry. (ii) Under certain conditions, a freemium business model is optimal, and tournament design facilitates user segmentation by offering multiple free versions (Proposition 4), which is commonly observed in the gaming industry. (iii) Tournament design is an effective tool for circumventing players’ financial limitations, and it increases the developer’s profitability when some players are reluctant to pay (Propositions 5 and 6). (iv) By capitalizing on network effects, tournament design not only broadens market reach but also increases both developer profits and player welfare (Proposition 7).

(a)  
Notes. (a) Free-only players. (b) Regular players.  
(b)  
![](/api/attachments/VU7F9RF3/fulltext/images/347656f67b39cd07c15699adbe82c2418ba9a7529cd57bd2ea20e5b9f1ec33f1.jpg)

It is worth noting that the role of tournament design is accentuated in the presence of players’ budget heterogeneity. To see this, it is useful to revisit the polar case in which the proportion of budget-constrained players approaches zero. As shown in the illustrative example in Section 3.3, tournament design still offers flexibility in pricing and versioning, and the maximum profit can be achieved by multiple strategies, including the freemium business model. However, a closer look at Propositions 1 and 2 suggests that the maximum profit with tournament design is the same as that without absent budget-constrained players. That is, despite the improved flexibility, tournament design is a substitute for quality design, and it is unnecessary in order to achieve the maximum profit as its role in addressing players’ reluctance to pay dissolves. Further, it can be verified that the market size and players’ surplus remain unchanged when tournament design is allowed because the developer can no longer leverage network effects through the inclusion of players with a tight budget (because there exists no such player). In contrast, when the market consists of a positive proportion of budget-constrained players (i.e., β > 0), our analysis shows that tournament design and quality design are complementary. Profit maximization requires both quality differentiation and tilting the playing field.

Our study contributes to the literature in three ways. First, prior work, as highlighted by Jing (2007), Cheng et al. (2015), and Shi et al. (2019), posits that providing free versions to attract users is lucrative in the presence of network effects. Our findings advance the literature by showing that an important premise of the practice of offering free versions is the firm’s ability to generate heterogeneous network effects in its product design, and tournament design is an effective tool within the context of the gaming industry to generate such heterogeneity. Importantly, tournament design enables the developer to create a trade-off between quality and winning rates by offering multiple free versions, which segments free users and effectively monetizes their participation.

Second, we explicitly model players’ reluctance to pay—a crucial yet often overlooked aspect in the literature—as the gap between players’ willingness to play and their willingness to pay. We show that tournament design strictly increases the developer’s profit whenever such divergence exists (i.e., when β > 0), and the incremental profits from tournament design increase as the fraction of reluctant players β increases. Our results also provide a rationale for the prevalent industry practice of managing free players, such as offering multiple free versions, as evidenced in Table 3.

Third, our study sheds new light on versioning and freemium strategies within the context of PvP games, wherein players’ gaming experience and utilities are naturally intertwined through competition (Liu et al. 2013, Nikolakaki et al. 2020). Conventional wisdom holds that the profitability of both versioning and freemium strategies is constrained by product cannibalization (Moorthy 1984, Desai 2001). We elaborate on how tournament design in PvP games can be coupled with the game developer’s versioning and pricing strategies to mitigate the cannibalization effect and how it renders the freemium strategy a lucrative and successful business model in the PvP gaming context.

This paper is an early foray into research on PvP games. There are ample possibilities for future studies. First, we can extend our model to allow for multiple developers and explore the impact of market competition. Second, previous studies have pointed out that segmenting or screening contestants according to their skill levels can increase their willingness to play (Liu et al. 2007, 2013). It would be fruitful to extend ou model to allow heterogeneous skill levels (i.e., different abilities to win using the same version) and endogenize the matching mechanism (Chen et al. 2022). Third, this paper assumes that players are fully rational and can accurately compare different game versions. Such rationality substantially simplifies our analysis, but it might not apply universally to every player. It would be intriguing to reinvestigate this issue from a behavioral perspective of bounded rationality. We leave the exploration of these possibilities to future research.

## Acknowledgments

The authors are grateful to senior editor Ravi Bapna, associate editor Atanu Lahiri, and three anonymous reviewers for detailed comments that significantly improved the article. The authors also thank Ruiqi Li, Hexin Wu, and Zeyu Xing for excellent research assistance.

## Endnotes

<sup>1</sup> According to Hadji-Vasilev (2023), the gaming industry is the biggest revenue source among various digital media sectors, and it gen erated an estimated \$178.2 billion in revenue worldwide in 2021.

<sup>2</sup> To our knowledge, the term “freemium” appears in at least two strands of the literature. The first builds on the static product line design framework a \` la Mussa and Rosen (1978) to investigate a firm’s pricing and versioning decisions (e.g., Cheng et al. 2015, Lahiri and Dey 2018) and includes studies within the context of video games (e.g., Guo et al. 2019, Meng et al. 2021). In these studies, freemium refers to the strategy whereby the firm offers multipl differentiated products on the market, with some priced at zero.

The second adopts a dynamic perspective and interprets freemium as moving consumers from free to fee, where the free offering is a teaser for other paid goods or services (e.g., Niculescu and Wu 2014, Aral and Dhillon 2021, Pattabhiramaiah et al. 2022). Given that our analysis builds on the product line design framework, we adopt the first perspective of freemium.

<sup>3</sup> In the ever-evolving gaming industry, standards from a decade ago seem archaic today. Pixelated graphics have been replaced by crisp high-resolution visuals enriched with intricate textures and advanced effects, and players thus require a higher-quality video game.

<sup>4</sup> For simplicity and clarity, we assume binary budget levels in the main text. In Online Appendix D.1, we generalize the model to allow for continuous budget levels and characterize the developer’s profit-maximizing strategy profile.

<sup>5</sup> The analyses can be applied to the scenario in which all players have an adequate budget by setting β to zero.

<sup>6</sup> We denote the outside option as version 0, which yields zero (net) utility.

<sup>7</sup> Step-by-step derivations of the developer’s strategy profile are provided in Online Appendix B.

<sup>8</sup> All proofs are collected in Online Appendix C.

<sup>9</sup> In the case in which free-only players are excluded from the market (i.e., $\widehat { K } = 0 )$ , we set $\ = \mathcal { K } _ { \ / F } = \emptyset$ and $\mathcal { K } _ { R } = \{ 1 , \ldots , K \}$

<sup>10</sup> Let $\theta _ { \widehat { K } } = 1$ if free-only players are excluded from the market (i.e., $\mathrm { i f } \ \widehat { K } = 0 )$

<sup>11</sup> Denote the utility of being a nonplayer as $U _ { 0 } ( \theta ) : = 0$ for all $\begin{array} { r } { \theta \in [ 0 , 1 ] . \operatorname { L e t } \theta _ { K + 1 } : = \dot { 1 } } \end{array}$ for notational convenience.

<sup>12</sup> Throughout this paper, we use superscripts to indicate different scenarios or settings (e.g., with or without tournament design) and subscripts to indicate different versions of the game.

<sup>13</sup> More formally, it can be verified from Proposition 2 that $\overline { { v } } \sum _ { j \in \mathcal { K } } t _ { i j } Q _ { j } < 0$ for the two free versions $i \in \mathcal { K } _ { F }$ and $\bar { v } \mathrm { { } } \bar { \sum } _ { j \in \mathcal { K } } t _ { i j } Q _ { j } > 0$ for the two paid versions $i \in \mathcal { K } _ { R }$

<sup>14</sup> A simple comparison between the prices in Propositions 1 and 2 yields $p _ { 3 } ^ { * } > \underline { { s } } / 2$ and $p _ { 4 } ^ { * } > \overline { { s } } / 2$

## References

Aral S, Dhillon PS (2021) Digital paywall design: Implications for con tent demand and subscriptions. Management Sci. 67(4):2381–2402

Bakos Y, Brynjolfsson E (1999) Bundling information goods: Pricing, profits, and efficiency. Management Sci. 45(12):1613–1630.

Bhargava HK, Choudhary V (2008) Research note: When is versioning optimal for information goods? Management Sci. 54(5):1029–1035.

Che YK, Gale IL (1998) Caps on political lobbying. Amer. Econom. Rev. 88(3):643–651.

Chellappa RK, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4):400–417.

Chen M, Elmachtoub AN, Lei X (2022) Matchmaking strategies for maximizing player engagement in video games. Proc. 23rd ACM Conf. Econom. Comput. (ACM, New York), 1040.

Cheng HK, Liu Y (2012) Optimal software free trial strategy: The impact of network externalities and consumer uncertainty. Inform. Systems Res. 23(2):488–504.

Cheng HK, Li S, Liu Y (2015) Optimal software free trial strategy: Limited version, time-locked, or hybrid? Production Oper. Man agement 24(3):504–517.

Choudhary V (2010) Use of pricing schemes for differentiating infor mation goods. Inform. Systems Res. 21(1):78–92.

Desai PS (2001) Quality segmentation in spatial markets: When does cannibalization affect product line design? Marketing Sci. 20(3): 265–283.

Dey D, Lahiri A, Liu D (2013) Consumer learning and time-locked trials of software products. J. Management Inform. Systems 30(2):239–268.

Divers G (2023) Gaming industry dominates as the highest-grossing entertainment industry. Gamerhub (January 24), https://gamer hub.co.uk/gaming-industry-dominates-as-the-highest-grossing entertainment-industry/.

Dou Y, Niculescu MF, Wu DJ (2013) Engineering optimal network effects via social media features and seeding in markets for dig ital goods and services. Inform. Systems Res. 24(1):164–185.

Drugov M, Ryvkin D (2017) Biased contests for symmetric players. Games Econom. Behav. 103:116–144.

Ekroslim (2024) Free champion rotation. Accessed July 30, 2024, https://leagueoflegends.fandom.com/wiki/Free\_champion\_ rotation.

Epstein GS, Mealem Y, Nitzan S (2011) Political culture and discrimination in contests. J. Public Econom. 95(1):88–93.

Etzion H, Pang MS (2014) Complementary online services in competitive markets: Maintaining profitability in the presence of network effects. MIS Quart. 38(1):231–248.

Franke J, Kanzow C, Leininger W, Schwartz A (2013) Effort maximization in asymmetric contest games with heterogeneous contestants. Econom. Theory 52(2):589–630.

Franke J, Kanzow C, Leininger W, Schwartz A (2014) Lottery vs. allpay auction contests: A revenue dominance theorem. Games Econom. Behav. 83:116–126.

Fu Q, Wu Z (2020) On the optimal design of biased contests. Theoret Econom. 15(4):1435–1470.

Fu Q, Wu Z, Zhu Y (2023) Bid caps in noisy contests. Amer. Econom. J. Microeconomics 15(3):426–473.

Fudenberg D, Tirole J (2000) Pricing a network good to deter entry J. Indust. Econom. 48(4):373–390.

Gallaugher JM, Auger P, BarNir A (2001) Revenue streams and digital content providers: An empirical investigation. Inform. Management 38(7):473–485.

Gavious A, Moldovanu B, Sela A (2002) Bid costs and endogenous bid caps. RAND J. Econom. 33(4):709–722.

Gu X, Kannan P, Ma L (2018) Selling the premium in freemium. J. Marketing 82(6):10–27.

Guo H, Hao L, Mukhopadhyay T, Sun D (2019) Selling virtual currency in digital games: Implications for gameplay and social welfare. Inform. Systems Res. 30(2):430–446.

Hadji-Vasilev A (2023) 23 online gaming statistics, facts & trends for 2023. Cloudwards.net. Accessed July 30, 2024, https://www. cloudwards.net/online-gaming-statistics/.

Jing B (2007) Network externalities and market segmentation in a monopoly. Econom. Lett. 95(1):7–13.

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1):164–176.

Kamada Y, O<sup>¨</sup> ry A (2020) Contracting with word-of-mouth management. Management Sci. 66(11):5094–5107.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Kirkegaard R (2012) Favoritism in asymmetric contests: Head starts and handicaps. Games Econom. Behav. 76(1):226–248.

Kumar V (2014) Making “freemium” work. Harvard Bus. Rev. 92(5): 27–29.

Lahiri A, Dey D (2018) Versioning and information dissemination A new perspective. Inform. Systems Res. 29(4):965–983.

Lazear E, Rosen S (1981) Rank-order tournaments as optimum labor contracts. J. Political Econom. 89(5):841–864.

Lelonek-Kuleta B, Bartczuk RP, Wiechetek M (2021) Pay for play— Behavioural patterns of pay-to-win gaming. Comput. Human Behav, 115:106592

Liu CZ, Au YA, Choi HS (2014) Effects of freemium strategy in the mobile app market: An empirical study of Google Play. J. Man agement Inform. Systems 31(3):326–354.

Liu D, Geng X, Whinston AB (2007) Optimal design of consumer contests. J. Marketing 71(4):140–155.

Liu D, Li X, Santhanam R (2013) Digital games and beyond: What happens when players compete? MIS Quart. 37(1):111–124.

Mai Y, Hu B (2023) Optimizing free-to-play multiplayer games with premium subscription. Management Sci. 69(6):3437–3456.

Maskin E, Riley J (1984) Monopoly with incomplete information. RAND J. Econom. 15(2):171–196.

Meng Z, Hao L, Tan Y (2021) Freemium pricing in digital games with virtual currency. Inform. Systems Res. 32(2):481–496.

Moorthy KS (1984) Market segmentation, self-selection, and product line design. Marketing Sci. 3(4):288–307.

Moorthy KS, Png IP (1992) Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3): 345–359.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Nikolakaki SM, Dibie O, Beirami A, Peterson N, Aghdaie N, Zaman K (2020) Competitive balance in team sports games. IEEE Conf. Games (Institute of Electrical and Electronics Engineers, Piscataway, NJ), 526–533.

NPD (2021) Time spent playing video games continues to rise. Marketing Charts (October 26), https://www.marketingcharts.com/ demographics-and-audiences-118663.

Olszewski W, Siegel R (2019) Bid caps in large contests. Games Econom. Behav. 115:101–112.

Pattabhiramaiah A, Overby E, Xu L (2022) Spillovers from online engagement: How a newspaper subscriber s activation of digital paywall access affects her retention and subscription reve nue. Management Sci. 68(5):3528–3548.

Prasad A, Venkatesh R, Mahajan V (2010) Optimal bundling of tech nological products with network externality. Management Sci. 56(12):2224–2236.

Salehudin I, Alpert F (2022) To pay or not to pay: Understanding mobile game app users’ unwillingness to pay for in-app pur chases. J. Res. Interactive Marketing 16(4):633–647.

Shapiro C, Varian HR (1999) Information Rules: A Strategic Guide to the Network Economy (Harvard Business Press, Boston).

Shi ZJ, Zhang K, Srinivasan K (2019) Freemium as an optimal strategy for market dominant firms. Marketing Sci. 38(1):150–169.

Shivendu S, Zhang Z (2015) Versioning in the software industry: Heterogeneous disutility from underprovisioning of functional ity. Inform. Systems Res. 26(4):731–753.

Sinclair B (2014) Only 2.2% of free-to-play users ever pay. GamesIndustry.biz (April 9), https://www.gamesindustry.biz/only-2-2- percent-of-free-to-play-users-ever-pay-report.

Tanks. GG (2024) All Tanks information of WOT. Accessed July 30, 2024, https://tanks.gg/list.

Tobon S, Ruiz-Alba JL, Garc´ıa-Madariaga J (2020) Gamification and online consumer decisions: Is the game over? Decision Support Systems 128:113167.

Varian HR (2000) Versioning information goods. Kahin B, Varian HR, eds. Internet Publishing and Beyond: The Economics of Digital Information and Intellectual Property (MIT Press, Cambridge, MA), 190–202.

Wang L, Lowry PB, Luo X, Li H (2023) Moving consumers from free to fee in platform-based markets: An empirical study of multiplayer online battle area games. Inform. Systems Res. 34(1): 275–296.

Wargaming (2024) Tankopedia: Reviews, comparison and collections of combat vehicles. World of Tanks. Accessed July 30, 2024, https://worldoftanks.com/en/tankopedia/#wot&w\_m=tanks.

Wei XD, Nault BR (2013) Experience information goods: Version-toupgrade. Decision Support Systems 56:494–501.

Wei X, Nault BR (2014) Monopoly versioning of information goods when consumers have group tastes. Production Oper. Management 23(6):1067–1081.

Wu Sy, Chen Py (2008) Versioning and piracy control for digital information goods. Oper. Res. 56(1):157–172.

Wu Sy, Chen PY, Anandalingam G (2003) Fighting information good piracy with versioning. Proc. 24th Internat. Conf. Inform. Systems (Association for Information Systems, Seattle).

Xu B, Yao Z, Tang P (2018) Pricing strategies for information pro ducts with network effects and complementary services in a duopolistic market. Internat. J. Production Res. 56(12):4243–4263.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
