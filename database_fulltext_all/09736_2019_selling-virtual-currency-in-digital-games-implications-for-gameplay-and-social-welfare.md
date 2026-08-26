---
otero_id: 9736
otero_key: "YPPT6QFW"
title: "Selling Virtual Currency in Digital Games: Implications for Gameplay and Social Welfare"
authors: "Hong Guo; Lin Hao; Tridas Mukhopadhyay; Daewon Sun"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0812"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [141.2.140.67] On: 23 July 2019, At: 19:43 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/YPPT6QFW/fulltext/images/f471a598685b9e26e50fda2e76d0f70513f795f376477803230334c3cf971b73.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Selling Virtual Currency in Digital Games: Implications for Gameplay and Social Welfare

Hong Guo, Lin Hao, Tridas Mukhopadhyay, Daewon Sun

To cite this article: Hong Guo, Lin Hao, Tridas Mukhopadhyay, Daewon Sun (2019) Selling Virtual Currency in Digital Games: Implications for Gameplay and Social Welfare. Information Systems Research 30(2):430-446. https://doi.org/10.1287/isre.2018.0812

## Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Selling Virtual Currency in Digital Games: Implications for Gameplay and Social Welfare

Hong Guo,<sup>a</sup> Lin Hao,<sup>b</sup> Tridas Mukhopadhyay,<sup>c</sup> Daewon Sun

<sup>a</sup> Mendoza College of Business, University of Notre Dame, Notre Dame, Indiana 46556; <sup>b</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>c</sup> Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213 Contact: hguo@nd.edu, https://orcid.org/0000-0001-6028-8155 (HG); linhao@uw.edu (LH); tridas@cmu.edu, http://orcid.org/0000-0001-6691-9595 (TM); dsun@nd.edu (DS)

Received: November 27, 2014 Revised: March 17, 2016; November 15, 2017; July 11, 2018 Accepted: July 18, 2018 Published Online in Articles in Advance: June 5, 2019

https://doi.org/10.1287/isre.2018.0812

Copyright: © 2019 INFORMS

Abstract. Despite the growing popularity of in-game purchases of virtual currency in digital games, there is very limited formal research that studies this new business model. This paper builds on the neoclassical labor–leisure model to examine the impact of selling virtual currency on players’ gameplay behavior, game provider’s strategies, and social welfare. When the game provider offers virtual currency for sale, players have two options to obtain virtual currency— playing the game and purchasing virtual currency directly. We introduce a parameter—the enabling-power rate of virtual currency—to characterize the extent to which virtual currency generated in a unit of playing time can augment players production of gaming leisure. We find that selling virtual currency reduces the playing time for certain heavy players, whereas it boosts certain light players’ playing time. It may also lead to a larger player base allowing more people to enjoy the benefits of playing digital games when the enabling-power rate of virtual currency is sufficiently high. The game provider should charge a higher (lower) virtual currency price for a game with a relatively lower (higher) enabling-power rate of virtual currency. She should also set a higher (lower) ad level for a game with a relatively higher (lower) enabling-power rate if the game’s base valuation of gameplay, that is, the valuation of gameplay independent of virtual currency, is sufficiently low. Finally, we demonstrate that selling virtual currency could lead to a win–win–win situation for the game provider, players, and society as a whole. It will alleviate the conflict of interest between the provider’s goal of longer playing time to maximize her ad revenue from in-game ads and the social goal of reducing excessive gaming, especially for heavy players.

History: Sanjeev Dewan, Senior Editor; Bin Gu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2018.0812.

Keywords: digital games • virtual currency • free-to-play games • in-game purchases • social welfare

## Introduction

Digital games, including social games, mobile games, personal computer and console games, and massively multiplayer online games, have experienced remarkable growth in recent years, contributing \$11.7 billion to the U.S. gross domestic product in 2016 (Anderton 2017). According to the Entertainment Software Association, 59% of Americans play video games, and 51% of U.S. households own at least one device dedicated to game playing (Entertainment Software Association 2014). On average, U.S. gamers of age 13 or older spent 6.3 hours a week playing video games in 2013 (Nielsen 2014). Sensing its popularity, game providers have been experimenting and adopting various strategies to monetize their games. Beyond the traditional subscription fee and fixed fee models that have been used in the past decades (Sundararajan 2004, Zhang and Seidmann 2010), a new business model has recently become a common feature in digital games: selling virtual currency through in-game microtransactions. It allows players to spend real money to purchase virtual currency that can then be used to acquire virtual items to enhance their gaming experience. For example, in PopCap’s blockbuster game Plants vs. Zombies, a player can spend \$4.99 to purchase 10,000 coins,<sup>1</sup> which can then be used to buy various virtual items within the game such as power-ups or extra plants.

Game providers have found this new way of inducing players to spend money for digital games quite effective. According to SuperData Research (2013), a market in telligence firm on digital games, among the players who pay for content, the average spend is \$40 per player Such alluring spending on virtual currency has driven a growing number of game providers to provide their games completely free to play and rely on in-game purchases as their main new revenue source. For example, the top revenue-generating mobile game Cand Crush Saga is free to play and relies on money from selling virtual currency. It brought revenue of \$1.9 billion and profit of \$568 million annually to its maker King Digital Entertainment<sup>2</sup> (Solomon 2014). In-game virtual currency sales have become the second-largest source of revenue, second only to retail sales, and are still growing (Jenkins 2014). Free-to-play games with in-game purchases have become one of the popular business models together with other ways for monetizing free software applications such as free with advertising (Lin et al. 2012, Chen and Stallaert 2014) and feature-limited and time-limited freemiums (Niculescu and Wu 2014, Lee and Tan 2014).

Despite the fast-growing popularity of in-game purchases of virtual currency, there is very limited formal research that studies this new business model and its social impacts. Particularly, it remains an open question as to how offering virtual currency for sale alters players playing behavior such as their playing time. Additionally, game providers need to know how this new revenue model compares with the popular models they have widely adopted for monetizing their free-to-play games, for example, the ad-sponsored model. From the social perspective, although playing digital games can generate some benefits, for example, generating fun and entertainment, facilitating learning, fostering social connectivity, and deriving higher meaning and purpose (Trudeau 2010, McGonigal 2011, Guarini 2013), it may also lead to some detrimental effects of gaming, such as health risks, aggression, and even addiction, especially for those players with excessive game playing (Park 2014, Robertson 2014, Yousafzai et al. 2014). This paper aims to fill this research gap by analyzing virtual currency selling in digital games and its impact on players gameplay behavior, game provider’s strategies, and social welfare. Specifically, this paper addresses the following research questions: When provided with an option of purchasing virtual currency, how will players gameplay behavior such as their playing times change? How does a game provider’s strategies for virtual currency price and ad level depend on game characteristics? How does selling virtual currency affect consumer surplus and social welfare?

In this paper, we build on the neoclassical labor– leisure model to characterize a player’s choice of playing time. The labor–leisure model is well known for characterizing individuals’ time allocation between labor activities such as work and leisure activities such as swimming (Borjas 2012). Following the tradition of modeling information technology artifacts (Dewan and Kraemer 2000), our model treats gameplay as one special type of technology that individuals can use to transform leisure time into gaming leisure utility. Hence, each individual essentially allocates his total time among three types of activities: labor, gaming leisure, and nongaming leisure, based on the labor–leisure framework.

We model virtual currency as an instrument that increases the production of gaming leisure from gameplay; that is, it boosts a player’s gaming leisure utility per unit of playing time. For example, players can use virtual currency to purchase powerful virtual weapons allowing them to gain more gaming utility. Formally, we intro duce a parameter—the enabling-power rate of virtual currency—to characterize the extent the which virtual currency generated in a unit of playing time can augment players’ production of gaming leisure. If a game provider does not sell virtual currency in her<sup>3</sup> game, that is, in the nonselling case, players can earn virtual currency only through playing the game. In this case, the provider gets only a stream of in-game ad revenue, which she maximizes by choosing the optimal ad level. If a game provider sells virtual currency in her game, that is, in the selling case, players have two options to obtain virtual currency—by playing the game and by purchasing virtual currency directly. Correspondingly, the game provider chooses the optimal ad level as well as the optimal price for virtual currency to maximize her total revenue from both advertising and selling virtual currency.

We find that when the game provider sells virtua currency, the extreme players as well as some heavy players with very low opportunity cost of leisure who spend a disproportionate amount of time playing the game will choose not to purchase any virtual currency and will not reduce their playing time compared with the nonselling case. This is because the extreme players will play for an excessively long time because of their very low opportunity cost, and they are able to earn the virtual currency they need for gameplay entirely through playing time. However, selling virtual currency will induce some heavy players with relatively higher opportunity cost of leisure to reduce their playing time because they now have the option to purchase some virtual currency to achieve their desirable level of virtual currency instead of obtaining it through excessive playing, as in the nonselling case. Furthermore, selling virtual currency will make some light players with high opportunity cost increase their playing time. This is because now they can buy some virtual currency to enhance their gaming leisure production per unit of time. Thanks to this leisure-production-enhancing effect, selling virtual currency also leads to a larger player base, and more people can enjoy the many benefits from playing digital games, when the enabling-power rate of virtual currency is sufficiently high.

We find that the game provider’s optimal strategies for virtual currency price and ad level depend on two key game characteristics—the enabling-power rate of virtual currency and players’ base valuation of gameplay. When the provider sells virtual currency, she should charge a lower virtual currency price for a game with a relatively higher enabling-power rate of virtual currency, because of a stronger substitution effect between playing time and virtual currency purchases. She should also set a higher ad level for a game with a higher enabling-power rate if the base valuation of gameplay is sufficiently low.

Additionally, our results suggest that the introduction of the sale of virtual currency as a new revenue source not only benefits the game provider, but also increases consumer surplus and social welfare, resulting in a win–win–win situation for the game provider, players, and society as a whole. In the nonselling case, the provider relies on ad revenue only, and hence wants players to spend more time playing the game. Thus, the ad-sponsored model incentivizes the provider to ignore or even induce excessive gaming, addiction, and other negative effects of digital gaming. Our results show that offering virtual currency for sale reshapes the provider’s goal for longer playing time. Compared with the nonselling case, heavy players substitute their excessive playing time spent for gaining additional virtual currency by virtual currency purchases. Light players may also buy virtual currency to enhance their marginal benefit of gameplay and subsequently increase their playing time, resulting in both greater ad revenue and virtual currency revenue. In other words, the sale of virtual currency substitutes for ad revenue from heavy players, whereas it complements ad revenue from light players. It eventually leads to a higher total revenue, indicating that selling virtual currency alleviates the conflict of interest between the provider’s goal for longer playing time and the social goal of reducing excessive gaming, especially for heavy players.

This paper proceeds as follows. In the next section, we review the relevant literature. In the following section, we propose a game-theoretical model to describe the market of digital games, which consists of a game provider and a mass of game players. We then analyze the game players’ gaming behavior and the corresponding game provider’s optimal strategies in two cases—with and without virtual currency for sale. Based on the analysis, we present our findings regarding the impact of selling virtual currency on consumer surplus and social welfare. Finally, we conclude with managerial insights and directions for future work.

## Literature Review

Our paper is mainly related to digital games and virtual item purchases and uses a modified neoclassical labor– leisure model. In this section, we review these three areas and point out our contributions to the existing literature.

## Digital Games

As noted by researchers (e.g., Webster and Martocchio 1993, Agarwal and Karahanna 2000, Finneran and Zhang 2005), there is very limited research on digital games. Early work in this area focused on computer games. There has been some research (e.g., Malone and Lepper

1987, Fabricatore et al. 2002) that examine why people enjoy playing computer games, and researchers found that computer games can provide different levels of fun by varying the difficulty levels of games. Some other researchers have studied how playing games can promote a state of heightened enjoyment. For example, Venkatesh (1999) found that a more enjoyable experience with a game-based training program may lead users to have favorable perceptions, and Liu et al. (2013) identified that competition is the key element of game design that should be incorporated into organizational activity games such as employee training games.

There has been a growing research interest in online digital games. Bartle (1996) identified four sources (acting, players, interacting, and world) of a player’s interest in a multi-user dungeon (MUD) and described that a player can see MUDs as games, pastimes, sports, or entertainments depending on the player’s characteristics in terms of the four sources. Hsu and Lu (2004) applied the technology acceptance model to explain why people play online games. By incorporating social influences and flow experiences, they found that social norms, attitude, and flow experience significantly affect intentions to play online games. Baek (2005) studied users preferences by measuring willingness to pay for online games and found that human-to-human interactivity is the most influential attribute.

Several papers have investigated motivations for playing multiplayer online games: Ryan et al. (2006) demonstrated that game enjoyment, autonomy, competence, and relatedness are important factors for intentions to play massively multiplayer online games (MMOGs). Yee (2006) showed that achievement, social, and immersion components are main reasons for playing massively multiplayer online role-playing games (MMORPGs). Chang et al. (2008) used the social identity theory and demonstrated that perceived enjoyment, reputation, and cohesion are significant factors for MMORPG players loyalty. To summarize, prior work has identified various factors that motivate players to play online digital games. Our paper extends the extant literature of digital games by analyzing the impact of a particular factor— selling virtual currency—on players’ gaming behavior (e.g., playing time). Although selling virtual currency has been widely adopted by practitioners in the digital gaming market, little theoretical work exists on this issue, and we intend to fill this gap.

## Virtual Item Purchases

There are a few papers that explain why people purchase virtual items with real money. Castronova (2006) conducted a cost–benefit analysis for real-money trading (RMT) among MMORPG players and found that RMT among players generates negative externalities. He demonstrated that buyers and sellers engaged in the RMT transactions may benefit from RMT, whereas other players and the game companies bear the cost. Manninen and Kujanpa¨a (¨ 2007) argued that virtual items in MMOGs have three values (achievement, social, and immersion values), and demonstrated that the motivational items of play could be a potential source of profit. Guo and Barnes (2007) explained why people buy virtual items by developing a model with a mixture of theories, including the theory of planned behavior, the technology acceptance model, trust theory, and the unified theory of acceptance and use of technology. Hamari and Lehdonvirta (2010) proposed that practitioners need to place more emphasis on marketing virtual goods for MMOGs because current marketing of virtual goods is short of their potential value.

Our work considers that the value of virtual currency, which can be used to obtain virtual items, lies in its effect of enhancing players’ production of gaming leisure from gameplay. We formulate its value in an economic utility function and then derive players’ purchasing behavior through their utility maximization. To our best knowledge, our paper is the first work that utilizes a formal economic model to characterize players’ purchasing behavior of virtual currency and demonstrate how it depends on factors such as the opportunity cost of leisure and enabling-power rate of virtual currency.

## Neoclassical Labor–Leisure Mode

Becker’s (1965) seminal analytical foundations have been widely used to study labor supply and allocation of time between labor and leisure (e.g., Heckman 1974, MaCurdy 1981, Moffitt 2002). A typical neoclassical labor–leisure model assumes that an individual has a fixed total time to be allocated between labor and leisure (Borjas 2012). Our model is based on the general framework of labor–leisure models. For example, there is a fixed total available time for each individual to allocate. In addition, our proposed model keeps the same setup for wage rate as in the neoclassical labor–leisure model and refers to it as the opportunity cost of leisure. However, our proposed model departs from the labor– leisure model by incorporating gameplay. Because we treat gameplay as a special type of technology that can transform part of the leisure time into gaming leisure utility, each individual, instead of allocating his fixed total time into labor and leisure activities only, now allocates his fixed total time among three types of activities: (1) the gaming leisure activity, that is, playing the digital game; (2) nongaming leisure activities, that is, other recreational activities like swimming; and (3) labor activities that generate nonrecreational benefits such as a salary.

The benefit of using such a modified labor–leisure model is the following. First, our study not only concerns whether an individual adopts a game or not, but also attempts to understand how much time he spends on gameplay, and how virtual currency selling affects that gameplay time. Hence, we believe a modified labor–leisure model is suitable to investigate this issue because of its capability to model time allocation among different activities. Second, the neoclassical labor–leisure framework enables our model to account for labor activities with wage rates. This makes our model suitable to draw conclusions on consumer surplus and social welfare.

In summary, we believe we are first to study the role of selling virtual currency in the context of free-to-play digital games. Using our new utility function for playing digital games inspired by the neoclassical labor–leisure model, we investigate the game provider’s strategies for virtual currency price and ad level, players’ optimal decisions on playing time and purchasing virtual currency, and overall social welfare implications.

## Modeling Framework

## Game Players’ Utility Function

We consider a game provider (hereafter called the “provider”) offering a digital game to a unit mass of game players (hereafter called the “players”) in the marketplace. We start with characterizing the players utility function. Building on the neoclassical labor– leisure model, we assume that a player’s utility comes from three types of activities: (1) the gaming leisure activity, that is, playing the digital game; (2) nongaming leisure activities, that is, other recreational activities like swimming; and (3) labor activities, which generate nonrecreational benefits such as a salary. We denote a player’s total available time by T, that is, the maximum amount of time he has for all three types of activities. We further denote the amount of time he allocates for the gaming leisure activity by t, for nongaming leisure activities by l, and for labor activities by h. Al notations are summarized in Table 1.

On the labor side, we posit that the utility generated by labor time h is θh, where θ denotes a player’s valuation of labor per unit of time. Parameter θ, which resembles the wage rate in the labor–leisure model, also represents the opportunity cost of leisure in our model. On the leisure side, the utility generated by total leisure time (including gaming leisure time t and nongaming leisure time l) is

$$
A t - \frac {t ^ {2}}{2} + a _ {l} l - \frac {l ^ {2}}{2} - \beta t l,
$$

in which both gaming leisure and nongaming leisure exhibit diminishing marginal returns. Parameter $\beta$ with $0 < \beta < 1$ characterizes the degree of substitutability between the two types of leisure activities. Keeping everything else equal, for a larger $\beta ,$ a higher valuation of gameplay A leads to a larger decrease in time allocated to nongaming leisure activities $l ,$ and a higher valuation of nongaming leisure $a _ { l }$ leads to a larger decrease in time allocated to gaming leisure activities t. Therefore, a player’s gross utility V is

Table 1. List of Notation

<table><tr><td colspan="2">Parameters</td></tr><tr><td> $\lambda$ </td><td>Enabling power of virtual currency per unit of playing time</td></tr><tr><td> $\theta$ </td><td>Opportunity cost of leisure</td></tr><tr><td> $a_t$ </td><td>Base valuation of gameplay</td></tr><tr><td> $a_l$ </td><td>Valuation of nongaming leisure</td></tr><tr><td> $w$ </td><td>Satiation point of virtual currency</td></tr><tr><td> $T$ </td><td>Total amount of time available</td></tr><tr><td> $\beta$ </td><td>Degree of substitutability between gaming and nongaming leisure activities</td></tr><tr><td> $c$ </td><td>Ad nuisance cost per ad level per unit of playing time</td></tr><tr><td> $r$ </td><td>Ad revenue rate per ad level per unit of playing time</td></tr><tr><td colspan="2">Variables</td></tr><tr><td> $p$ </td><td>Price per unit of virtual currency</td></tr><tr><td> $t$ </td><td>Amount of time allocated to gameplay</td></tr><tr><td> $g$ </td><td>Amount of virtual currency a player purchases</td></tr><tr><td> $l$ </td><td>Amount of time allocated to nongaming leisure activities</td></tr><tr><td> $h$ </td><td>Amount of time allocated to labor activities</td></tr><tr><td> $A$ </td><td>Valuation of gameplay</td></tr><tr><td> $V$ </td><td>Player&#x27;s gross utility</td></tr><tr><td> $U$ </td><td>Player&#x27;s net utility</td></tr><tr><td> $\pi$ </td><td>Provider&#x27;s profit</td></tr><tr><td> $CS$ </td><td>Consumer surplus</td></tr><tr><td> $SW$ </td><td>Social welfare</td></tr></table>

$$
V = \theta h + A t - \frac {t ^ {2}}{2} + a _ {l} l - \frac {l ^ {2}}{2} - \beta t l,
$$

with the time constraint $h + t + l \leq T$ and $h , t , l \geq 0 .$

When playing the game, players generate leisure utility through gaming activities such as winning a battle, advancing to the next level, decorating a virtual place, etc. Meanwhile, players also derive utility from a special type of goods—virtual currency. Virtual currency, which may take different forms in different games (e.g., coins, gems, gold), can be used to purchase virtual items that enhance a player’s leisure utility generation. Such enhancement on leisure utility generation is limited to the gameplay. For example, a powerful virtual weapon may boost a player’s leisure utility generation per unit of playing time, such that he may end up spending more time playing the game with the weapon. Also, the more time he spends in the game, the more utility he can derive from the powerful weapon. A virtual item is essentially an “enabler” of players’ gaming-leisure activity, and it in itself is of no value if the player does not play the game at all, and so is virtual currency.<sup>4</sup> Therefore, we posit that virtual currency contributes to a player’s valuation of gameplay A.

When the provider does not sell virtual currency (the nonselling case), virtual currency can be obtained only through playing the game. For example, after spending some playing time on winning a battle against virtual enemies, players gain not only a certain amount of excitement but also a certain amount of virtual currency. Specifically, for the nonselling case, we have

$$
A = a _ {t} + \lambda t.
$$

Parameter $a _ { t }$ is the base valuation of gameplay, that is, the valuation of gameplay independent of virtual currency. Parameter λ is the enabling power per unit of playing time (hereafter, “enabling-power rate”).<sup>5</sup> Thus, λt represents the additional valuation of gameplay enabled by a player’s virtual currency in possession, which is obtained only through playing the game in the nonselling case. Two factors contribute to the level of enabling-power rate λ. The first factor is the speed of virtual currency generation. The faster a player can gain virtual currency through playing the game, the higher the level of enabling-power rate λ. For example, in Grand Theft Auto V (GTA V), if the amount of virtual dollars players can earn increase from 200 to 300 virtual dollars per minute, then λ is higher. The second factor is the enabling power of a certain amount of virtual currency. The more utility a player can derive from a certain amount of virtual currency (through exchanging for virtual items), the higher the level of λ. In GTA V, for 100,000 virtual dollars, if a player can purchase an armored car rather than an outfit, then λ is higher. This is because vehicles and weapons are more essential than cosmetic items for the gaming experience in action/ adventure games.

When the provider does sell virtual currency (the selling case), a player has the option of purchasing virtual currency from the provider in addition to obtaining it through gameplay. Let $g$ be the amount of virtual currency that the player purchases. Then, for the selling case, we get

$$
A = a _ {t} + \lambda t + g.
$$

Furthermore, we use w to denote the satiation point of the additional valuation of gameplay enabled by a player’s virtual currency in possession, that is, λt for the nonselling case and $\lambda t + g$ for the selling case. Parameter w is a game characteristic, which is higher for games with more abundant in-game virtual items.

## Game Provider’s Decision Problem

When the provider does not sell virtual currency (the nonselling case), advertising is the sole revenue source for the provider. Suppose the provider sets the ad level at n. Consequently, consumers incur a nuisance cost of cnt, where c is the ad nuisance cost per ad level per unit of playing time (hereafter, “ad nuisance cost”). In real life, different ad nuisance costs may be associated with different games. For example, players are usually more annoyed by ads in intense action games (e.g., fighting games) than ads in casual games. In the nonselling case, an individual player’s net utility is $U = V - c n t$ , and he chooses playing time t to maximize his net utility U as follows:

$$
\max _ {t, l, h} U = \theta h + A t - \frac {t ^ {2}}{2} + a _ {l} l - \frac {l ^ {2}}{2} - \beta t l - c n t
$$

subject to $A = a _ { t } + \lambda t ,$

$$
t + l + h \leq T, t \geq 0, l \geq 0, \text { and } h \geq 0.
$$

We assume that players are heterogeneous in terms of their opportunity cost of leisure $\theta ,$ , which is uniformly distributed on $[ { \underline { { \dot { \theta } } } } , { \overline { { \theta } } } ]$ . The interval of $\left[ { \underline { { \theta } } } , { \overline { { \theta } } } \right]$ is assumed to be such that $0 < l ^ { * } ( \theta ) < T$ and $0 \dot { < } h ^ { \ast } ( \bar { \theta } ) < T$ for all $\theta \in \left[ \underline { { \theta } } , \overline { { \theta } } \right]$ . We further assume that $1 - 2 \lambda - \beta > 0$ to ensure that times spent on both gaming and nongaming leisure decrease with opportunity cost of leisure θ for all participating players, that is, all players who adopt the game. Practically, this assumption excludes games with an overly high λ and games with an overly high $\beta ,$ for example, virtual reality games where virtual items enhance players’ gameplay experience to such a great extent that players with a higher wage rate θ actually play longer. This assumption excludes such games with extreme gameplay experience. Let $t ( \theta )$ denote the playing time chosen by player $\theta ,$ and let r denote the ad revenue rate per ad level per unit of playing time. Then the provider’s profit maximization problem is

$$
\max _ {n} \pi = r n \int_ {\underline {{\theta}}} ^ {\overline {{\theta}}} t (\theta) d \theta
$$

subject to $n \geq 0 .$

In this case, the provider chooses ad level n to maximize her profit π.

In the selling case, the provider has two revenue sources: revenue from selling virtual currency and revenue from advertising. Suppose the provider charges the virtual currency at unit price $p .$ Then a player pays $p g$ in total if he purchases $g$ units of virtual currency. As a result, in the selling case, an individual player’s net utility is $U = V - c n t - p g$ and he chooses playing time t and purchase amount of virtual currency $g$ to maximize his net utility U as follows:

$$
\max _ {t, l, h, g} U = \theta h + A t - \frac {t ^ {2}}{2} + a _ {l} l - \frac {l ^ {2}}{2} - \beta t l - c n t - p g
$$

subject to $A = a _ { t } + \lambda t + g ,$

$$
t + l + h \leq T, t \geq 0, l \geq 0, h \geq 0, \mathrm{and} g \geq 0.
$$

Let $t ( \theta )$ and $g ( \theta )$ denote the playing time and the purchase amount of virtual currency chosen by player $\theta .$ Then the provider’s profit maximization problem is

$$
\max _ {p, n} \pi = p \int_ {\underline {{\theta}}} ^ {\overline {{\theta}}} g (\theta) d \theta + r   n \int_ {\underline {{\theta}}} ^ {\overline {{\theta}}} t (\theta) d \theta
$$

subject to $p { \geq } 0$ and $n \geq 0$

In this case, the provider chooses virtual currency price $p$ and ad level n to maximize her profit π.

It is worth mentioning that our paper focuses on investigating the impact of selling virtual currency. Therefore, we take game characteristics such as enablingpower rate λ as exogenously given. We aim to investigate how selling virtual currency affects games with different characteristics without taking game characteristics as decision variables because they are largely determined by factors outside our model, for example, the type of the game (role-playing games like Final Fantasy or puzzle games like Candy Crush).

## The Nonselling Case: Free-to-Play Games with No Virtual Currency for Sale

We start by analyzing the nonselling case as the benchmark case, that is, free-to-play games with no virtual currency for sale and advertising as the provider’s only revenue source. In the benchmark case, the players choose game playing time t, nongaming leisure time $l ,$ and work time h to maximize their utilities. Lemma 1 summarizes the optimal choices for the players. Proofs of lemmas and propositions are relegated to the online appendix.

Lemma 1 (Players’ Strategies with No Virtual Currency fo Sale). Given the provider’s choice of ad level $n ,$ there are two cases for players’ strategies:

Case L. When

$$
n <   \hat {n} = \frac {a _ {t} - \beta a _ {l}}{c} - \frac {w (1 - \lambda - \beta^ {2})}{\lambda c} - \frac {(1 - \beta) \underline {{\theta}}}{c},
$$

players can be divided into four segments:

• (Extreme-play segment) Players with

$$
\underline {{\theta}} \leq \theta <   \hat {\theta} _ {1} = \frac {a _ {t} - \beta a _ {l}}{1 - \beta} - \frac {w (1 - \lambda - \beta^ {2})}{\lambda (1 - \beta)} - \frac {c n}{1 - \beta}
$$

will play with

$$
t _ {E} = \frac {w + a _ {t} - \beta a _ {l} - c n}{1 - \beta^ {2}} - \frac {\theta}{1 + \beta}
$$

and

$$
l _ {E} = \frac {a _ {l} - \beta a _ {t} - \beta w + \beta c n}{1 - \beta^ {2}} - \frac {\theta}{1 + \beta}.
$$

• (Heavy-play segment) Players with

$$
\hat {\theta} _ {1} \leq \theta <   \hat {\theta} _ {2} = \frac {a _ {t} - \beta a _ {l}}{1 - \beta} - \frac {w (1 - 2 \lambda - \beta^ {2})}{\lambda (1 - \beta)} - \frac {c n}{1 - \beta}
$$

will play with $t _ { H } = { \frac { w } { \lambda } } a n d l _ { H } = a _ { l } - { \frac { \beta w } { \lambda } } - \theta .$

• (Light-play segment) Players with

$$
\hat {\theta} _ {2} \leq \theta <   \hat {\theta} _ {3} = \frac {a _ {t} - \beta a _ {l}}{1 - \beta} - \frac {c n}{1 - \beta}
$$

will play with

$$
t _ {L} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \theta - c n}{1 - 2 \lambda - \beta^ {2}}
$$

and

$$
l _ {L} = \frac {(1 - 2 \lambda) a _ {l} - \beta a _ {t} - (1 - 2 \lambda - \beta) \theta + \beta c n}{1 - 2 \lambda - \beta^ {2}}.
$$

• (Not-adopt segment) Players with $\hat { \theta } _ { 3 } \leq \theta \leq \overline { { \theta } }$ will not play with $t _ { N } = 0$ and $l _ { N } = a _ { l } - \theta .$

Case H. When $n \geq { \hat { n } } ,$ , players can be divided into three segments:

• (Heavy-play segment) Players with $\underline { { \theta } } \leq \theta < \hat { \theta } _ { 2 }$ will play with $\begin{array} { r } { t _ { H } = \frac { w } { \lambda } } \end{array}$ and $\begin{array} { r } { l _ { H } = a _ { l } - \frac { \beta w } { \lambda } - \theta . } \end{array}$

• (Light-play segment) Players with $\hat { \theta } _ { 2 } \leq \theta < \hat { \theta } _ { 3 }$ will play with

$$
t _ {L} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \theta - c n}{1 - 2 \lambda - \beta^ {2}}
$$

and

$$
l _ {L} = \frac {(1 - 2 \lambda) a _ {l} - \beta a _ {t} - (1 - 2 \lambda - \beta) \theta + \beta c n}{1 - 2 \lambda - \beta^ {2}}.
$$

• (Not-adopt segment) Players with $\hat { \theta } _ { 3 } \leq \theta \leq \overline { { \theta } }$ will not play with $t _ { N } = 0$ and $l _ { N } = a _ { l } - \theta$

Note that all players choose $h = T - t - l$ in all cases. As shown in Lemma 1, there are four possible player segments in term of their game playing time t: extremeplay, heavy-play, light-play, and not-adopt segments. A player’s game playing time t depends on his opportunity cost of leisure θ. Specifically, players whose opportunity cost of leisure θ is greater than threshold ${ \hat { \theta } } _ { 3 }$ will not adopt the game, as it is not worth their time to play. Among those players who do adopt $( \theta < \hat { \theta } _ { 3 } ) ,$ players with extremely low opportunity cost $( \theta < \hat { \theta } _ { 1 } )$ 1 play the game for an extremely long time, and this extreme play in turn generates more virtual currency than satiation point w. For the extreme players, any additional virtual currency earned beyond w would not provide any additional utility. However, these extreme players continue to play because they enjoy the game itself (captured by base valuation of gameplay a ). Players with moderately low opportunity cost $\begin{array} { r } { ( \hat { \theta } _ { 1 } \leq } \end{array}$ $\partial <  { \hat { \theta } } _ { 2 } )$ engage in heavy play—they play the game for a long period of time, which in turn generates just enough virtual currency to reach satiation point w. Players with a relatively higher opportunity cost $( \hat { \theta } _ { 2 } \leq$ $\ d \theta < \dot { \theta } _ { 3 } )$ engage in light play—they play for a shorter period of time and thus gain less virtual currency. The segmentation of players also depends on the provider’s choice of ad level n. When ad level n is lower than a threshold nˆ (Case L), all four player segments are present.

When ad level n goes beyond threshold nˆ (Case H), the extreme-play segment no longer exists.<sup>6</sup>

In the benchmark case, the provider only chooses ad level n to maximize her profit. We present the provider’s equilibrium ad level and her corresponding profit in Lemma 2.

Lemma 2 (Provider’s Equilibrium Ad Level and Pro<sup>fi</sup>t with No Virtual Currency for Sale). The provider’s equilibrium ad level and profit are as follows:

Case 1.

$$
n ^ {*} = n _ {1} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w}{3 c}
$$

and

$$
\pi^ {*} = \pi_ {1} ^ {B M} = \frac {2 r [ a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w ] ^ {3}}{2 7 (1 - \beta) ^ {2} (1 + \beta) c}
$$

when the base valuation of gameplay $a _ { t }$ is $h i g h ,$ , that $i s ,$

$$
a _ {t} \geq \hat {a} _ {t} = \beta a _ {l} + (1 - \beta) \underline {{\theta}} + \frac {w (3 - 2 \lambda - 3 \beta^ {2})}{2 \lambda}.
$$

Case 2.

$$
n ^ {*} = n _ {2} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}}}{2 c} - \frac {w (1 - 2 \lambda - \beta^ {2})}{4 \lambda c}
$$

and

$$
\pi^ {*} = \pi_ {2} ^ {B M} = \frac {r w [ 2 \lambda (a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w) + w (1 - \beta^ {2}) ] ^ {2}}{1 6 \lambda^ {3} (1 - \beta) c}
$$

when the base valuation of gameplay $a _ { t }$ is low, that is, $a _ { t } < \hat { a } _ { t }$ Furthermore, $n ^ { * }$ decreases with ad nuisance cost c in both cases, that is, $\begin{array} { r } { \frac { \partial n ^ { * } } { \partial c } < 0 ; n ^ { * } } \end{array}$ is not affected by enabling-power rate λ in Case 1, that $\begin{array} { r } { i s , \frac { \partial n _ { 1 } } { \partial \lambda } = 0 , } \end{array}$ ; and $n ^ { * }$ increases with λ in Case $2 ,$ that is, $\begin{array} { r } { \frac { \partial n _ { 2 } } { \partial \lambda } > 0 } \end{array}$

We know from Lemma 1 that the provider may adopt one of two ad level strategies: the low-ad strategy (Case L) or the high-ad strategy (Case H). The key difference between these two strategies is that no player chooses to engage in extreme play under the high-ad strategy because of the increased ad level n. Lemma 2 reveals that both the low-ad and high-ad strategies could be the equilibrium depending on base valuation of gameplay $a _ { t } .$ . Specifically, Case 1 (Case 2) in Lemma 2 corresponds to Case L (Case H) in Lemma 1. When ad level n increases, the ad revenue rate per unit of time (that is, r n) increases, but the total game playing time across all players decreases. When choosing her ad level, the provider evaluates the tradeoff between these two effects. For a game with a higher $a _ { t } ,$ playing time $t _ { E }$ for the extreme players is higher, and thus the ad revenue contribution from the extreme-play segment is more significant. Therefore, the provider is better off setting a relatively low ad level, that is, ${ n ^ { * } } = n _ { 1 } ,$ to keep these extreme players. However, for a game with a lower $a _ { t } ,$ the provider is better off setting a relatively high ad level, that $\begin{array} { r } { \mathbf { i s } , n ^ { * } = n _ { 2 } , } \end{array}$ to discourage players from extreme play, that ${ \mathrm { i s } } ,$ eliminating the extreme-play segment and focusing on earning a high margin from the participating players.

The comparative statics of the provider’s equilibrium ad level with respect to ad nuisance cost c suggests a lower ad level for a game with a higher ad nuisance cost. When ads cause more disutility to players, the totalplaying-time-reducing effect becomes stronger, leading to a lower ad level in equilibrium. The impact of enabling-power rate λ on the provider’s equilibrium ad level is more nuanced. To explain it, we need to first understand how enabling-power rate λ affects players playing time. On the one hand, a higher λ boosts a player’s marginal benefit of playing the game and thus tends to prolong his playing time. On the other hand, a higher λ helps a player to reach his desired level of virtual currency faster, reducing his playing time spent just for gaining additional virtual currency. According to Lemma 1, light players’ playing time is eventually increasing in $\lambda ,$ that is, $\begin{array} { r } { \frac { \partial t _ { L } } { \partial \lambda } > 0 , } \end{array}$ , indicating an overall stronger prolonging effect. Heavy players’ playing time, however, is eventually decreasing in $\lambda ,$ , that is, $\begin{array} { r } { \frac { \partial t _ { H } } { \partial \lambda } < 0 , } \end{array}$ indicating an overall stronger reducing effect.

When the base valuation of gameplay is low (i.e., Case 1), the market is populated with light players. Therefore, a higher enabling-power rate λ will increase the total playing time from the market, such that the provider raises ad level n to exploit it. When the base valuation is high (i.e., Case 2), there exist a significant number of heavy players in the market. When enabling-power rate λ increases, the augmentation of playing time of light players will be countervailed by the reduction of playing time of heavy players, resulting in an insignificant change of total playing time from the market. Therefore, the provider can no longer increase ad level n to exploit it.

## The Selling Case: Free-to-Play Games with Virtual Currency for Sale

In the selling case, the game provider relies on selling virtual currency as her second revenue source. When the provider offers virtual currency for sale, the timing of the game is as follows. In the first stage, the provider announces virtual currency price p and ad level n. In the second stage, each player decides how to allocate his time across gameplay, nongaming leisure, and work activities, including deciding whether to play the game. Those players who decide to play must also decide how much virtual currency to purchase. Note that a player may choose not to play the game at all, that $\mathrm { i s } , t ( \bar { \theta } ) \dot { = } 0$ Using backward induction, we first solve the player’s optimal choices of $t ( \theta ) , l ( \theta ) , h ( \theta ) .$ , and $g ( \theta ) ;$ we then solve for the game provider’s optimal strategies for virtual currency price and ad level.

In response to the provider’s decisions on virtual currency price p and ad level $n ,$ the players choose their playing time t, nongaming leisure time l, work time $h ,$ , and their purchase amount of virtual currency $g .$ . Proposition 1 summarizes the optimal choices for the players.

Proposition 1 (Players’ Strategies with Virtual Currency fo Sale). Given the provider’s choices of virtual currency price p and ad level n, there are six cases for players’ strategies:

• Case HL. When $p \ge \hat { p } _ { H } = \frac w \lambda$ and

$$
n <   \hat {n} = \frac {a _ {t} - \beta a _ {l}}{c} - \frac {w (1 - \lambda - \beta^ {2})}{\lambda c} - \frac {(1 - \beta) \underline {{\theta}}}{c},
$$

players can be divided into four segments—extreme pure play, heavy pure play, light pure play, and not adopt.

• Case ML. When

$$
\hat {p} _ {L} = \frac {w (1 - \lambda - \beta^ {2} - \sqrt {(1 - \beta^ {2}) (1 - 2 \lambda - \beta^ {2})})}{\lambda^ {2}} \leq p <   \hat {p} _ {H}
$$

and $n < { \hat { n } } ,$ , players can be divided into five segments—extreme pure play, heavy pure play, play and purchase, light pure play, and not adopt.

• Case LL. When $p < \hat { p } _ { L }$ and $n < { \hat { n } } ,$ , players can be divided into four segments—extreme pure play, heavy pure play, play and purchase, and not adopt.

• Case HH. When $p \ge \hat { p } _ { H }$ and $n \geq { \hat { n } } ,$ , players can be divided into three segments—heavy pure play, light pure play, and not adopt.

• Case MH. When $\hat { p } _ { L } \leq p < \hat { p } _ { H }$ and $n \geq { \hat { n } } ,$ , players can be divided into four segments—heavy pure play, play and purchase, light pure play, and not adopt.

• Case LH. When $p < \hat { p } _ { L }$ and $n \geq { \hat { n } } ,$ , players can be $d i -$ vided into three segments—heavy pure play, play and purchase, and not adopt.

Note that players’ choices of gameplay time $t ,$ nongaming leisure time $l ,$ and purchase amount of virtual currency $g$ in all five possible segments are presented in Table 2. Specific player segmentation in response to provider’s decisions is presented in Table 3. All players choose $h = T - t - l$ in all cases.

Compared with the nonselling case, Proposition 1 shows that when the provider offers virtual currency for sale, a new player segment emerges, that is, the playand-purchase segment. Players in this segment purchase virtual currency to enhance their gameplay. As a result, there are five possible player segments (extreme pure $\mathrm { \ p l a y } , ^ { 7 }$ heavy pure play, play and purchase, light pure play, and not adopt) and the corresponding player decisions are summarized in Table 2. Furthermore, Proposition 1 demonstrates that the players’ choices of game playing time t and purchase amount of virtual currency g depend on the provider’s choices (e.g., virtual currency price p and ad level n) as well as player-specific and game-specific characteristics (e.g., players’ opportunity cost of leisure θ and enabling-power rate λ).

Table 2. Strategies of Players in Five Possible Segments

<table><tr><td rowspan="2">Player segments</td><td colspan="3">Players&#x27; decisions</td></tr><tr><td>t</td><td>l</td><td>g</td></tr><tr><td>Extreme pure play</td><td> $t_E = \frac{w + a_t - \beta a_l - cn}{1 - \beta^2} - \frac{\theta}{1 + \beta}$ </td><td> $l_E = \frac{a_l - \beta a_t - \beta w + \beta cn}{1 - \beta^2} - \frac{\theta}{1 + \beta}$ </td><td> $g_E = 0$ </td></tr><tr><td>Heavy pure play</td><td> $t_H = \frac{w}{\lambda}$ </td><td> $l_H = a_l - \frac{\beta w}{\lambda} - \theta$ </td><td> $g_H = 0$ </td></tr><tr><td>Play and purchase</td><td> $t_P = \frac{a_t + \lambda p + w - \beta a_l - cn}{1 - \beta^2} - \frac{\theta}{1 + \beta}$ </td><td> $l_P = \frac{a_l - \beta (a_t + \lambda p + w) + \beta cn}{1 - \beta^2} - \frac{\theta}{1 + \beta}$ </td><td> $g_P = \frac{w(1 - \lambda - \beta^2) - \lambda (a_t + \lambda p - \beta a_l) + c\lambda n}{1 - \beta^2} + \frac{\lambda \theta}{1 + \beta}$ </td></tr><tr><td>Light pure play</td><td> $t_L = \frac{a_t - \beta a_l - (1 - \beta)\theta - cn}{1 - 2\lambda - \beta^2}$ </td><td> $l_L = \frac{(1 - 2\lambda)a_l - \beta a_t - (1 - 2\lambda - \beta)\theta + \beta cn}{1 - 2\lambda - \beta^2}$ </td><td> $g_L = 0$ </td></tr><tr><td>Not adopt</td><td> $t_N = 0$ </td><td> $l_N = a_l - \theta$ </td><td> $g_N = 0$ </td></tr></table>

As summarized in Table 3 and illustrated in Figure 1, when the virtual currency price is too high $\mathrm { ( i . e . , } p \ge \hat { p } _ { H }$ in Cases HL and HH), none of the players in the market will purchase any virtual currency, and the resulting player segments are the same as those in the nonselling case.

through purely playing the game. The high opportunity cost outweighs the price of virtual currency, and, thus, these players choose to bear the cost of purchasing virtual currency rather than bear the cost of spending playing time to meet their needs for virtual currency. Interestingly, when opportunity cost θ further increases into the light-pure-play region, players stop purchasing virtual currency. This is because these players’ opportunity cost of leisure is very high, and, thus, they only play the game for a short period of time, which in turn reduces the benefit of obtaining virtual currency. As a result, this reduced benefit of virtual currency can no longer justify its price, and these players cease purchasing virtual currency. Eventually, when opportunity cost θ surpasses threshold ${ \hat { \theta } } _ { 3 } ,$ , players stop adopting the game

When virtual currency price reduces to the medium range (i.e., $\hat { p } _ { L } \leq p < \hat { p } _ { H }$ in Cases ML and MH), some players on the market start to purchase virtual currency. Because players in the extreme-pure-play and heavypure-play regions can generate enough virtual currency to reach satiation point w through purely playing the game, they do not have any incentive to purchase virtual currency. As opportunity cost θ increases into the playand-purchase region, players find it worthwhile to spend money to buy a certain amount of virtual currency to enhance their gameplay beyond what is obtained

When the virtual currency price further reduces from the medium range $( \hat { p } _ { L } \leq p \overset { \cdot } { < } \hat { p } _ { H } )$ to the low range $( \mathrm { i . e . , }$ $p < \hat { p } _ { L }$ in Cases LL and LH), more and more players in the light-pure-play region find it beneficial to pay for virtual currency because virtual currency is now less expensive. Thus, these players join the play-and-purchase region. Consequently, the light-pure-play region diminishes as the virtual currency price drops and eventually disappears.

Table 3. Player Segmentation in Response to Provider’s Decisions

<table><tr><td rowspan="2">Provider&#x27;s decisions</td><td colspan="5">Player segments</td></tr><tr><td>Extreme pure play with  $t_{E}, l_{E}$ , and  $g_{E}$ </td><td>Heavy pure play with  $t_{H}, l_{H}$ , and  $g_{H}$ </td><td>Play and purchase with  $t_{P}, l_{P}$ , and  $g_{P}$ </td><td>Light pure play with  $t_{L}, l_{L}$ , and  $g_{L}$ </td><td>Not adopt with  $t_{N}, l_{N}$ , and  $g_{N}$ </td></tr><tr><td>Case HL: high  $p (p \geq \hat{p}_{H})$ , low  $n (n < \hat{n})$ </td><td> $[\underline{\theta}, \hat{\theta}_{1})$ </td><td> $[\hat{\theta}_{1}, \hat{\theta}_{2})$ </td><td></td><td> $[\hat{\theta}_{2}, \hat{\theta}_{3})$ </td><td> $[\hat{\theta}_{3}, \overline{\theta}]$ </td></tr><tr><td>Case ML: medium  $p (\hat{p}_{L} \leq p < \hat{p}_{H})$ , low  $n (n < \hat{n})$ </td><td> $[\underline{\theta}, \hat{\theta}_{1})$ </td><td> $[\hat{\theta}_{1}, \hat{\theta}_{4})$ </td><td> $[\hat{\theta}_{4}, \hat{\theta}_{5})$ </td><td> $[\hat{\theta}_{5}, \hat{\theta}_{3})$ </td><td> $[\hat{\theta}_{3}, \overline{\theta}]$ </td></tr><tr><td>Case LL: low  $p (p < \hat{p}_{L})$ , low  $n (n < \hat{n})$ </td><td> $[\underline{\theta}, \hat{\theta}_{1})$ </td><td> $[\hat{\theta}_{1}, \hat{\theta}_{4})$ </td><td> $[\hat{\theta}_{4}, \hat{\theta}_{6})$ </td><td></td><td> $[\hat{\theta}_{6}, \overline{\theta}]$ </td></tr><tr><td>Case HH: high  $p (p \geq \hat{p}_{H})$ , high  $n (n \geq \hat{n})$ </td><td></td><td> $[\underline{\theta}, \hat{\theta}_{2})$ </td><td></td><td> $[\hat{\theta}_{2}, \hat{\theta}_{3})$ </td><td> $[\hat{\theta}_{3}, \overline{\theta}]$ </td></tr><tr><td>Case MH: medium  $p (\hat{p}_{L} \leq p < \hat{p}_{H})$ , high  $n (n \geq \hat{n})$ </td><td></td><td> $[\underline{\theta}, \hat{\theta}_{4})$ </td><td> $[\hat{\theta}_{4}, \hat{\theta}_{5})$ </td><td> $[\hat{\theta}_{5}, \hat{\theta}_{3})$ </td><td> $[\hat{\theta}_{3}, \overline{\theta}]$ </td></tr><tr><td>Case LH: low  $p (p < \hat{p}_{L})$ , high  $n (n \geq \hat{n})$ </td><td></td><td> $[\underline{\theta}, \hat{\theta}_{4})$ </td><td> $[\hat{\theta}_{4}, \hat{\theta}_{6})$ </td><td></td><td> $[\hat{\theta}_{6}, \overline{\theta}]$ </td></tr></table>

Note. Definitions of the thresholds for θ can be found in the online appendix.

Figure 1. Player Segments

<table><tr><td></td><td colspan="5">Low n (n &lt; n̂)</td><td colspan="4">High n (n ≥ n̂)</td></tr><tr><td rowspan="2">High p(p ≥ p̂H)</td><td>Extreme pure playt &gt; w/λg = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Light pure play0 &lt; t &lt; w/λg = 0</td><td>Not adoptt = 0g = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Light pure play0 &lt; t &lt; w/λg = 0</td><td>Not adoptt = 0g = 0</td><td></td><td></td></tr><tr><td>θ</td><td>θ1</td><td>θ2</td><td>θ3</td><td>θ</td><td>θ</td><td>θ2</td><td>θ3</td><td>θ</td></tr><tr><td rowspan="2">Medium p(p̂L ≤ p &lt; p̂H)</td><td>Extreme pure playt &gt; w/λg = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Play and purchase0 &lt; t &lt; w/λg &gt; 0</td><td>Light pure play0 &lt; t &lt; w/λg = 0</td><td>Not adoptt = 0g = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Play and purchase0 &lt; t &lt; w/λg &gt; 0</td><td>Light pure play0 &lt; t &lt; w/λg = 0</td><td>Not adoptt = 0g = 0</td></tr><tr><td>θ</td><td>θ1</td><td>θ4</td><td>θ5</td><td>θ3</td><td>θ</td><td>θ4</td><td>θ5</td><td>θ3</td></tr><tr><td rowspan="2">Low p(p &lt; p̂L)</td><td>Extreme pure playt &gt; w/λg = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Play and purchase0 &lt; t &lt; w/λg &gt; 0</td><td>Not adoptt = 0g = 0</td><td>Heavy pure playt = w/λg = 0</td><td>Play and purchase0 &lt; t &lt; w/λg &gt; 0</td><td>Not adoptt = 0g = 0</td><td></td><td></td></tr><tr><td>θ</td><td>θ1</td><td>θ4</td><td>θ6</td><td>θ</td><td>θ</td><td>θ4</td><td>θ6</td><td>θ</td></tr></table>

Next, we investigate some properties of the playand-purchase segment in Proposition 2.

Proposition 2 (Properties of the Play-and-Purchase Segment). The play-and-purchase segment has the following properties:

• For play-and-purchase players, playing time $t _ { P }$ and purchase amount of virtual currency g are substitutes, that $\begin{array} { r } { \dot { i } s , \frac { \partial t _ { P } } { \partial p } > 0 } \end{array}$ and $ { \frac { \partial g _ { P } } { \partial \theta } } > 0$

• When the enabling-power rate λ increases, play-andpurchase players play the game longer and purchase less virtual currency, that is, $\begin{array} { r } { \frac { \partial t _ { P } } { \partial \lambda } > 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial g _ { P } } { \partial \lambda } < 0 . } \end{array}$

• When the virtual currency price is low $( p < \hat { p } _ { L } ) ,$ , the market size increases with enabling-power rate λ, that $i s ,$ $\begin{array} { r } { \frac { \partial \hat { \theta } _ { 6 } } { \partial \lambda } > 0 . } \end{array}$ . When the virtual currency price is medium or high $( p \ge \hat { p } _ { L } ) ,$ , market size is not affected by $\lambda ,$ that $\begin{array} { r } { i s , \frac { \partial \hat { \theta } _ { 3 } } { \partial \lambda } = 0 } \end{array}$

For play-and-purchase players, there is an interesting substitution effect between their playing time $t _ { P }$ and purchase amount of virtual currency $g _ { P }$ (details shown in Table 2). When virtual currency becomes more expensive, the players will purchase less virtual currency and spend more time playing the game to gain the desirable amount of virtual currency. When the player’s opportunity cost θ becomes higher, the player will spend less time playing the game and purchase more virtual currency. A player’s utility comes from consuming two goods: playing time t at a cost of opportunity cost θ and purchase amount of virtual currency $g$ at a cost of price $p$ . The positive cross-price elasticities $\begin{array} { r } { \big ( \frac { \partial t _ { P } } { \partial p } > 0 } \end{array}$ and $\frac { \partial \bar { g } _ { P } } { \partial \theta } > 0 )$ demonstrate that playing time t and purchase amount of virtual currency $g$ are substitutes in our model.

Additionally, the play-and-purchase players’ choices of playing time $t _ { P }$ and purchase amount $g _ { P }$ also depend on enabling-power rate λ. For a game with a stronger enabling-power rate $\lambda ,$ the players tend to play the game for a longer period of time t and purchase less virtual currency g $( \textstyle { \frac { \partial t _ { P } } { \partial \lambda } } > 0$ and $\frac { \partial g _ { P } } { \partial \lambda } < 0 )$ ). This is because for a game with a higher $\lambda ,$ , players derive more utility from the virtual currency obtained per unit of playing time. This augmentation of the marginal benefit of playing the game leads to longer playing time. The prolonged gameplay leads to more virtual currency obtained through purely playing. Thus, the players will purchase less virtual currency because of the substitution effect between playing and purchasing. In the GTA V example, if the players can earn 300 (instead of 200) virtual dollars per minute or purchase an armored car (instead of an outfit), then our result suggests that players will play longer but purchase less virtual currency.

Besides the impact on the individual player’s playing time t and purchase amount $g ,$ enabling-power rate λ may also affect the number of players who play the game, that is, the market size. In general, a player will play the game—choosing a positive playing time—if his overall marginal benefit of gameplay is greater than a threshold. When the marginal benefit led by the base valuation of gameplay alone is insufficient to meet such threshold, he has two ways to boost it—purchasing virtual currency and earning virtual currency through playing time at enabling-power rate λ. Under a low price for virtual currency $( \mathrm { i } . \mathrm { e } . , p < \hat { p } _ { L } )$ , a marginal player will utilize both ways to eventually turn his overall marginal benefit greater than the threshold for playing the game. Note from Proposition 1 that the marginal players who are on the verge of not playing the game are play-and-purchase players when $p < \hat { p } _ { L }$ . Therefore, a higher enabling-power rate λ will reduce marginal players’ monetary payment for the virtual currency needed to boost their overall marginal benefit over the threshold. Hence, it will bring more marginal players, expanding the market size.

Under a high price for virtual currency $( \mathrm { i } . \mathrm { e } . , p > \hat { p } _ { L } ) ,$ purchasing virtual currency is still worth something (just not worth the required price)., such that a marginal player can rely on earning virtual currency through playing time to boost his gaming leisure. Nonetheless, although a higher enabling-power rate λ itself tends to augment the overall marginal benefit of gameplay, such augmentation is conditional on a player’s positive playing time by the definition the enabling-power rate, that $\mathrm { i } \mathbf { s } , A = a _ { t } + \lambda t$ . Hence, for a player who is just indifferent between playing and not playing the game, that is, $t ^ { * } = 0 ,$ , a higher enabling-power rate does not boost his overall marginal benefit of gameplay. Therefore, the market size is not affected by the enabling-power rate when the virtual currency price is sufficiently high.

Anticipating the players’ responses, the game provider decides virtual currency price p and ad level n to maximize her profit. Proposition 3 summarizes the provider’s equilibrium pricing and ad-level strategies as well as her corresponding profit.

Proposition 3 (Provider’s Equilibrium Virtual Currency Price, Ad Level, and Pro<sup>fi</sup>t with Virtual Currency for Sale). The provider’s equilibrium virtual currency price, ad level, and profit are as follows:

Case 1.

$$
\begin{array}{c} {p ^ {*} = p _ {1} = \frac {w (1 - \beta^ {2})}{8 \lambda^ {2}},} \\ {n ^ {*} = n _ {1} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w}{3 c},} \end{array}
$$

and

$$
\pi^ {*} = \pi_ {1} = \frac {w ^ {3} (1 - \beta) (1 + \beta) ^ {2}}{6 4 \lambda^ {3}} + \frac {2 r [ a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w ] ^ {3}}{2 7 (1 - \beta) ^ {2} (1 + \beta) c}
$$

when both the enabling-power rate λ and base valuation of gameplay a<sub>t</sub> are high, that is,

$$
\lambda \geq \hat {\lambda} = \frac {3 (1 - \beta^ {2})}{8},
$$

and

$$
a _ {t} \geq \hat {a} _ {t} = \beta a _ {l} + (1 - \beta) \underline {{\theta}} + \frac {w (3 - 2 \lambda - 3 \beta^ {2})}{2 \lambda}.
$$

Consequently, players can be divided into four segments— extreme pure play, heavy pure play, play and purchase, and not adopt.

Case 2.

$$
\begin{array}{l} p ^ {*} = p _ {1}, \\ n ^ {*} = n _ {2} = \frac {a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}}}{2 c} - \frac {w (1 - 2 \lambda - \beta^ {2})}{4 \lambda c}, \end{array}
$$

and

$$
\begin{array}{l} \pi^ {*} = \pi_ {2} = \frac {w ^ {3} (1 - \beta) (1 + \beta) ^ {2}}{6 4 \lambda^ {3}} \\ \qquad + \frac {r w [ 2 \lambda (a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w) + w (1 - \beta^ {2}) ] ^ {2}}{1 6 \lambda^ {3} (1 - \beta) c} \end{array}
$$

when λ is high and $a _ { t }$ is low, that $i s , \ \lambda \geq \hat { \lambda }$ and $a _ { t } < \hat { a } _ { t }$ Consequently, players can be divided into three segments— heavy pure play, play and purchase, and not adopt.

Case 3. $p ^ { * } = p _ { 2 } = \frac { w } { 3 \lambda } , n ^ { * } = n _ { 1 } ,$ , and

$$
\begin{array}{c} \pi^ {*} = \pi_ {3} = \frac {w ^ {3} [ 1 - \lambda - \beta^ {2} + \sqrt {(1 - \beta^ {2}) (1 - 2 \lambda - \beta^ {2})} ]}{2 7 \lambda^ {2} (1 - \beta)} \\ + \frac {2 r [ a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w ] ^ {3}}{2 7 (1 - \beta) ^ {2} (1 + \beta) c} \end{array}
$$

when λ is low and $a _ { t }$ is high, that is, $\lambda < \hat { \lambda }$ and $a _ { t } \geq \hat { a } _ { t }$ Consequently, players can be divided into five segments— extreme pure play, heavy pure play, play and purchase, light pure play, and not adopt.

Case 4. $p ^ { * } = p _ { 2 } , n ^ { * } = n _ { 2 } ,$ , and

$$
\begin{array}{r} \pi^ {*} = \pi_ {4} = \frac {w ^ {3} [ 1 - \lambda - \beta^ {2} + \sqrt {(1 - \beta^ {2}) (1 - 2 \lambda - \beta^ {2})} ]}{2 7 \lambda^ {2} (1 - \beta)} \\ + \frac {r w [ 2 \lambda (a _ {t} - \beta a _ {l} - (1 - \beta) \underline {{\theta}} + w) + w (1 - \beta^ {2}) ] ^ {2}}{1 6 \lambda^ {3} (1 - \beta) c} \end{array}
$$

when both λ and $a _ { t }$ are low, that is, $\lambda < \hat { \lambda }$ and $a _ { t } < \hat { a } _ { t }$ Consequently, players can be divided into four segments— heavy pure play, play and purchase, light pure play, and not adopt.

Proposition 3 and Table 4 reveal that the provider may adopt one of four strategies in equilibrium: a lowprice, low–ad level strategy (Case 1); a low-price, high– ad level strategy (Case 2), a high-price, low–ad level strategy (Case 3); or a high-price, high–ad level strategy (Case 4), depending on enabling-power rate λ and base valuation of gameplay $a _ { t } .$ These four strategies (Cases 1, 2, 3, and 4) in Proposition 3 correspond to Cases LL, LH, ML, and MH in Proposition 1, respectively. Note that setting the virtual currency price p to a very high value such that no player purchases virtual currency is never an equilibrium strategy, that is, neither Case HL nor Case HH in Proposition 1 is an equilibrium.

For a game with a relatively low enabling-power rate $\lambda ,$ we know from Proposition 2 that individual play-andpurchase players’ purchase amount is relatively high. To take advantage of this high individual demand for virtual currency, it is more profitable for the provider to charge a high p to extract more consumer surplus, even at the cost of limiting the size of the play-and-purchase segment. In contrast, for a game with a relatively high λ, it is more profitable for the provider to charge a low virtual currency price p to expand the play-and-purchase segment (to the extent of eliminating the light-pure-play segment). The provider’s ad-level strategy in the selling case is similar to that in the nonselling case. For a game with a high $a _ { t } ,$ the provider is better off setting a relatively low ad level, that is, $n ^ { * } = n _ { 1 }$ , to induce low–opportunity cost players to engage in extreme play. Otherwise, for a game with a low $a _ { t } ,$ the provider is better off setting a relatively high ad level, that is, $n ^ { * } = n _ { 2 }$ , to discourage players from extreme play.

Figure 2 illustrates the equilibrium player segmentation corresponding to the provider’s four equilibrium strategies. Compared with low–ad level strategies (Cases 1 and 3), under high–ad level strategies (Cases 2 and 4), no players engage in extreme play; that is, the extreme-pure-play segment disappears. Compared with high-price strategies (Cases 3 and 4), under lowprice strategies (Cases 1 and 2), no players engage in light play; that is, the light-pure-play segment disappears.

Next, we explore the properties of the provider’s equilibrium virtual currency price and ad level in Proposition 4.

Proposition 4 (Comparative Statics of Equilibrium Results with Selling Virtual Currency). The comparative statics of the provider’s equilibrium virtual currency price and ad level are as follows:

• Equilibrium virtual currency price $p ^ { * }$ is not affected by ad nuisance cost c, that is, $\begin{array} { r } { \frac { \partial p ^ { * } } { \partial c } = 0 , } \end{array}$ , and $p ^ { * }$ decreases with enabling-power rate λ, that $\dot { i } s , \frac { \partial p } { \partial \lambda } < 0$

• Equilibrium ad level n<sup>\*</sup> decreases with ad nuisance cost c in all cases, that is, $\textstyle { \frac { \partial n ^ { * } } { \partial c } } < 0 ; n ^ { * }$ is not affected by enablingpower rate λ in Cases 1 and 3, that $\begin{array} { r } { i s , \frac { \partial n _ { 1 } } { \partial \lambda } = 0 ; } \end{array}$ and n<sup>\*</sup> increases with λ in Cases 2 and 4, that is, $\begin{array} { r } { \frac { \partial n _ { 2 } } { \partial \lambda } > 0 } \end{array}$

Proposition 4 shows that for a game with a stronger enabling-power rate λ, the provider should charge a lower virtual currency price p. When enabling-power rate λ is stronger, the supply of free virtual currency (through pure gameplay) increases. Consequently, the demand of virtual currency purchase decreases, resulting in a lower price. In other words, a higher λ drives the total demand of virtual currency to be more elastic, and thus the equilibrium virtual currency price is lower. This result is a consistent reflection of the substitution effect between t and $g .$ Enabling-power rate λ influences how close a substitute playing time t is to the purchase amount of virtual currency g. A higher λ makes playing time t a closer substitute, and consequently makes the demand of virtual currency more elastic, leading to a lower equilibrium price p. Proposition 4 also shows that the equilibrium virtual currency price is independent of c, the ad nuisance cost per ad level per unit of playing time. Essentially, what matters in the provider’s choices of p and n is the ad nuisance cost per unit of playing time (i.e., cn), which can be considered as the marginal cost of playing time t. For a game with a higher ad nuisance cost c, the provider has the capability to adjust ad level n to maintain the optimal level of cn. As a result, there is no need to adjust virtual currency price p for a higher c.

The comparative statics of the equilibrium ad level in the selling case are similar to those in the nonselling case. Our results suggest a low ad level for a game with a high ad nuisance cost (e.g., fighting games such as Mortal Kombat X) or a game with a high base value but a low enabling-power rate (e.g., strategy card games such as Plants vs. Zombies: Heroes).

## Impacts of Selling Virtual Currency: Comparison Between the Nonselling and Selling Cases

In this section, we study the impacts of selling virtua currency on gameplay, consumer surplus, and social welfare by comparing the selling virtual currency case to the benchmark nonselling case. Consumer surplus is the aggregate surplus of all participating consumers, that is, $\begin{array} { r } { C S = \int _ { \underline { { \theta } } } ^ { \overline { { \theta } } } U ( \theta ) d \theta } \end{array}$ . Social welfare is the sum of consumer surplus and the provider’s profit, that is, $S W = C S + \pi$ . Next, we present the impact of selling virtual currency on individual players’ playing time and market size in Proposition 5, and then consumer surplus and social welfare in Proposition 6.

Table 4. Provider’s Equilibrium Strategies Under Different Market Conditions

<table><tr><td rowspan="2">Enabling-power rate λ</td><td colspan="2">Base valuation of gameplay  $a_t$ </td></tr><tr><td>High  $a_t$ </td><td>Low  $a_t$ </td></tr><tr><td>High λ</td><td>Case 1: low-price, low-ad strategy;  $p^* = p_1$  and  $n^* = n_1$ </td><td>Case 2: low-price, high-ad strategy;  $p^* = p_1$  and  $n^* = n_2$ </td></tr><tr><td>Low λ</td><td>Case 3: high-price, low-ad strategy;  $p^* = p_2$  and  $n^* = n_1$ </td><td>Case 4: high-price, high-ad strategy;  $p^* = p_2$  and  $n^* = n_2$ </td></tr></table>

Figure 2. Equilibrium Player Segments  
![](/api/attachments/YPPT6QFW/fulltext/images/ab74d6a022d90fcf659e29fb3fff84d2e13fe675188b9b13f3e7806606c2e3f0.jpg)  
Notes. Thresholds with letters $E , H , P ,$ and L in the subscripts represent the upper bounds of θ for the extreme-pure-play, heavy-pure-play, playand-purchase, and light-pure-play segments, respectively. Numbers 1, 2, 3, and 4 in the subscripts of these thresholds correspond to the case numbers. Definitions of these thresholds for θ can be found in the online appendix.

Proposition 5 (Impacts of Selling Virtual Currency on Players’ Playing Time and Market Size).

• Selling virtual currency decreases the playing time for players with $\hat { \theta } _ { H i } < \theta < \tilde { \theta } _ { i }$ and increases the playing time for players with $\tilde { \theta } _ { i } < \theta < \hat { \theta } _ { P i }$ in all four cases $i = 1 , 2 , 3 ,$ , and 4.

• Selling virtual currency increases market size under low-price strategies (Cases 1 and 2) and does not change market size under high-price strategies (Cases 3 and 4).

Note that definitions of the thresholds for θ can be found in the online appendix.

Figure 3 illustrates the results of Proposition 5 by comparing the playing time between the selling case and the nonselling case for each individual player. This comparison reveals interesting differential impacts of selling virtual currency on different players. As shown in Figure 3, for players with low opportunity cost (all extreme players and some heavy players), playing time will remain the same regardless whether the provider offers virtual currency for sale or not.

For the players with moderate opportunity cost $( \hat { \theta } _ { H } < \theta < \hat { \theta } _ { P } ^ { \dot { } }$ in all four cases), offering virtual currency for sale may decrease or increase their playing time depending on their opportunity cost. In the nonselling case, participating players engage in pure play only When the provider offers virtual currency for sale, some of these pure-play players become play-and-purchase players. Compared with the pure-play players, the play-and-purchase players obtain their virtual currency partially from playing the game and partially from purchasing. As a result, when the opportunity cost increases, the playing-time-decreasing effect is stronger for the pure-play players than the play-and-purchase players. Additionally, the playing-time-decreasing effect in the nonselling case kicks in at a larger value of θ than in the selling case. This is because the playing-timedecreasing effect applies only to light-pure-play players and play-and-purchase players. Plus, the light-pure-play region in the nonselling case starts at a larger value of θ than the play-and-purchase region in the selling case because some heavy players with relatively higher θ in the nonselling case switch to the play-and-purchase re gion in the selling case. Therefore, when virtual currency becomes available for purchase, among the players with moderate opportunity cost $( { \bar { \theta } } _ { H } < \theta < { \hat { \theta } } _ { P }$ in all four cases), the players with relatively lower $\theta ( \hat { \theta } _ { H } < \theta < \tilde { \theta }$ in all four cases) play less, and the players with relatively higher $\theta { \bf \Psi } ( \tilde { \theta } < \grave { \theta } < \grave { \theta } _ { P }$ in all four cases) play more.

Case 1: high λ and high at (low-price, low-ad strategy)  
Figure 3. Players’ Playing Time in Equilibrium (Selling vs. Nonselling)  
![](/api/attachments/YPPT6QFW/fulltext/images/babc1d884412f5a343cdab3638bbcffeb89f157e8f3f65a66f2e3f6452530398.jpg)

![](/api/attachments/YPPT6QFW/fulltext/images/f0cc41cc731ba9b4521cc1fbf55a000f8d9bb67a6764e21439b8a8eb89f000be.jpg)  
Case 2: high λ and low at (low-price, high-ad strategy)

![](/api/attachments/YPPT6QFW/fulltext/images/5209b1f5d10e19a4eca1ab763a35e2186e1ca8b4b8b8fe8c45755671e98244e1.jpg)

![](/api/attachments/YPPT6QFW/fulltext/images/efd091cc93f400ab67f912536e4d70c76ca795c3bca7df313ed29bcbe49b766f.jpg)  
Notes. Solid lines correspond to the selling case, and dashed lines correspond to the nonselling case. Among the thresholds for θ, the ones with superscript BM correspond to the benchmark nonselling case, and the ones without superscripts correspond to the selling case. Thresholds with letters $E , { \dot { H } } , P ,$ and L in subscripts represent the upper bounds of θ for the extreme-pure-play, heavy-pure-play, play-and-purchase, and light pure-play segments, respectively. Threshold θ<sup>˜</sup> represents the play-and-purchase player in the selling case whose playing time is the same as in the nonselling case. Numbers 1, 2, 3, and 4 in the subscripts of these thresholds correspond to the case numbers. Definitions of these thresholds fo θ can be found in the online appendix.

For the players with high opportunity cost, selling the virtual currency may induce more of them to choose to play the game (in Cases 1 and 2), compared with the nonselling case, in which they would not even adopt. This is because for high–opportunity cost players, purchasing the virtual currency brings extra utility from virtual items and reduces the extra playing time, which eventually makes playing the game a better choice than not playing.

The above findings suggest that game providers should be aware of the differentiating impact of selling virtual currency on different player segments. For example, in Plants vs. Zombies, selling coins may not change the hardcore players’ gameplay time. However, some heavy players may play less and some light players may play more.

Proposition 6 (Impact of Selling Virtual Currency on Socia Welfare and Consumer Surplus). Selling virtual currency is welfare enhancing; that is, $S W { > } \overline { { S } } W ^ { B M }$ . Selling virtual currency also increases consumer surplus; that is, $C S > C S ^ { B M }$

Proposition 6 presents an important finding of our paper: the society as a whole will be better off if the game provider sells in-game virtual currency. The intuition of this welfare-enhancing effect of selling virtual currency is as follows. From Proposition 3, we know that the provider’s profit increases by selling virtual currency because the provider can exploit the players need for virtual currency at an appropriate price level and hence achieve a higher profit. This result has been supported by the fact that many top games in the Apple App Store are loaded with in-game purchase options for players to buy virtual currency using real money A more interesting finding lies on the players’ side. Proposition 6 shows that consumer surplus also increases when the provider offers virtual currency for sale. This is because although the players have to pay real money to purchase virtual currency, they also enjoy two benefits from purchased virtual currency: (a) the purchased virtual currency enhances the gameplay experience; (b) players are also able to save their playing time that would otherwise have been spent to obtain that virtual currency. The overall effect of purchasing virtual currency is positive because the reduced opportunity cost outweighs the price they pay, even as the price is set by a profit-maximizing monopolistic game provider. In summary, selling virtual currency results in a win–win–win situation, which benefits the game provider, players, and society as a whole.

## Concluding Remarks

Selling virtual currency through in-game microtransactions has become an important revenue source for firms in the digital gaming industry. This paper analyzes the impact of this new business model on players gaming behavior, the game provider’s strategies for virtual currency price and ad level, and social welfare. In our model, players vary in terms of their opportunity cost of leisure, and their gaming behavior is determined by their opportunity cost, the virtual currency price, the ad level, and related game characteristics. We derive the provider’s optimal strategies for virtual currency price and ad level, taking the virtual currency–related game characteristics as exogenously given. We analyze the impact of selling virtual currency on players’ gameplay behavior and social welfare by comparing the selling case to the nonselling benchmark case

Our findings have important managerial implications for the digital gaming industry. To realize the full potential and ensure long-term growth of in-game microtransactions, creative and ingenious game designs should be carefully aligned with the business strategies of the game provider. Specifically, our results suggest that the provider’s optimal strategies of virtual currency price and ad level critically depend on the enablingpower rate of virtual currency (i.e., how much players benefit from enhanced gameplay due to virtual currency generated per unit of playing time). Specifically, when the enabling-power rate is stronger, players have lower incentive to purchase virtual currency. Therefore, the provider should set a lower price to avoid losing too much demand. At the same time, the marginal benefit of playing the game increases, and thus the provider should set a higher ad level to take advantage of this boosted marginal benefit for players when the base valuation of gameplay is sufficiently low.

Our results show that offering virtual currency for sale has a heterogeneous treatment effect over players playing time. Specifically, for the extreme players who spend an extraordinary amount of time playing the game, their playing time are not affected with the option to buy virtual currency. However, selling virtual currency shortens some heavy players’ playing time, as they do not need to spend an excessive amount of playing time to gain virtual currency. Meanwhile, selling virtual currency also boosts some light players’ playing time because of the enhanced gameplay enabled by purchased virtual currency. Finally, some nonadopters in the nonselling case may start to play the game once the game provider sells virtual currency. To summarize, selling virtual currency depolarizes the distribution of players’ playing time. These results serve as theoretical predictions that empirical researchers can utilize to build hypotheses concerning players’ playing behavior.

Finally, we conclude that offering in-game purchases of virtual currency as a new business model benefits society as a whole. In real life, the social planner could be a government agency such as the Federal Trade Commission in the United States. The interests of the social planner and the game provider may not always align with each other. Game providers often want to prolong players’ playing time as much as possible because longer playing time creates more advertising revenues, stronger network effects, etc. However, the social planner also considers the potential social impact due to excessive gameplay. Severe social costs may be incurred by excessive online game playing such as students quitting school and weakened family relationships and friendships (Zhan and Chan 2012). Indeed, the gaming industry is constantly under the regulatory radar. Many governments have introduced game-rating sys tems to reduce the chance of inappropriate gaming content reaching young players. Many governments have in troduced game-rating systems, such as the Pan European Game Information, to reduce the chance of inappropriate gaming content reaching young players. Organizations such as the Interactive Software Federation of Europe and Entertainment Software Rating Board were founded to regulate game content. However, few governments have acted on regulating online addictive gameplay behavior. According to Zhan and Chan (2012), China has developed new regulations to reduce online game addiction, which require game providers to monitor players’ playing time. If a player’s playing time exceeds a threshold, the system will restrict the player from playing the game for a period of time. Our findings suggest that regulators of the gaming industry should be less concerned about the risk of excessive gameplay for games that sell virtual currency compared with ones that do not. This is because selling virtual currency will lead to a reduction of heavy players’ playing time without compromising the provider’s profit; a reduction of playing time is mostly at odds with the provider’s profit when the game does not sell virtual currency and generates revenue only through in-game ads.

Finally, our work has some limitations. For example, our model does not consider the effect of network externality. An interesting direction for future research is incorporating the effect of network externality, because many of the popular digital games exhibit network externality. Our current analysis shows that sell ing virtual currency would increase the market size (i.e., number of participating players) under the lowprice strategy and not affect market size under the highprice strategy. For a game that exhibits strong network externality, increased market size would further increase individual players’ utilities in the selling case compared with the nonselling case. Hence, we believe the presence of network externality would make selling virtual currency more favorable. We also think that incorporating the potential competition among games that are free to play with virtual currency available for purchase is an important and fruitful future research topic. Another limitation of our paper is that we do not model the trading of virtual currency among game players. Nowadays, game players in some digital games, for example, Second Life, can buy virtual currency from not only the game provider but also from other players. As our model focuses on the implications of virtual currency on gameplay and social welfare, we leave the study of the between-player trading for future research.

## Acknowledgments

All the authors contributed equally and are listed in the alphabetical order. The authors thank the senior editor, the associate editor, and the three anonymous reviewers for con structive feedback on this manuscript.

## Endnotes

<sup>1</sup> In-game virtual currency studied in this paper is different from digital currency such as Bitcoin, which is a software-based online payment system serving as an alternative to traditional online payment systems such as credit cards.

<sup>2</sup> In February 2016, King was acquired by Activision Blizzard for \$5.9 billion.

<sup>3</sup> In this paper, we refer to the game provider as “she” and a player as “he.”

<sup>4</sup> In this paper, we do not consider the trading value of virtual currency; that is, people can sell/exchange their virtual currency on a market.

<sup>5</sup> In our main model, we assume that players have a homogenous and time-invariant enabling-power rate. In reality, this enabling-power rate could be both heterogeneous across players and time variant because sophisticated players may know how to gain and utilize virtual currency more efficiently than new players. In the online appendix, we conduct numerical analyses to examine the impact of such player heterogeneity in enabling-power rate λ and demonstrate our main results still hold after incorporating player heterogeneity in λ.

<sup>6</sup> In this paper, we do not consider cases where the ad level is so high that no players engage in heavy play or light play, that is, the heavy-play or light-play segment no longer exists. In real life, heavy players and light players are observed for most games.

<sup>7</sup> We refer to the extreme-play, heavy-play, and light-play segments as pure-play segments to distinguish them from the play-and-purchase segment.

## References

Agarwal R, Karahanna E (2000) Time flies when you’re having fun: Cognitive absorption and beliefs about information technology usage. MIS Quart. 24(4):665–694.

Anderton K (2017) The business of video games: A multi billion dol lar industry. Forbes (April 29), https://www.forbes.com/sites/ kevinanderton/2017/04/29/the-business-of-video-games-a -multi-billion-dollar-industry-infographic/#3236f6706d27.

Baek S (2005) Exploring customer preferences for online games. Internat. J. Advanced Media Comm. 1(1):26–40.

Bartle R (1996) Hearts, clubs, diamonds, spades: Players who sui MUDs. J. MUD Res. 1(1):19.

Becker GS (1965) A theory of the allocation of time. Econom. J. 75(299): 493–517.

Borjas GJ (2012) Labor Economics, 6th ed. (McGraw-Hill Education, New York).

Castronova E (2006) A cost-benefit analysis of real-money trade in the products of synthetic economies. Digital Policy, Regulation Governance 8(6):51–68.

Chang KT, Koh AT, Low BY, Onghanseng DJS, Tanoto K, Thuong TST (2008) Why I love this online game: The MMORPG sticki ness factor. Proc. 29th Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta), Paper 88.

Chen J, Stallaert J (2014) An economic analysis of online advertising using behavioral targeting. MIS Quart. 38(2):429–449.

Dewan S, Kraemer KL (2000) Information technology and productivity: Evidence from country-level data. Management Sci. 46(4): 548–562.

Entertainment Software Association (2014) Essential facts about the computer and video game industry. Accessed November 29, 2018, http://www.theesa.com/about-esa/essential-facts-compute -video-game-industry/.

Fabricatore C, Nussbaum M, Rosas R (2002) Playability in action videogames: A qualitative design model. Human–Comput. In teraction 17(4):311–368.

Finneran CM, Zhang P (2005) Flow in computer-mediated environments: Promises and challenges. Comm. Assoc. Inform. Systems 15:82–101.

Guarini D (2013) 9 ways video games can actually be good for you. Huffington Post (November 7), https://www.huffingtonpost.com 2013/11/07/video-games-good-for-us\_n\_4164723.html

Guo Y, Barnes S (2007) Why people buy virtual items in virtual worlds with real money. ACM SIGMIS Database 38(4):69–76.

Hamari J, Lehdonvirta V (2010) Game design as marketing: How game mechanics create demand for virtual goods. Internat. J. Bus. Sci. Appl. Management 5(1):14–29.

Heckman J (1974) Life cycle consumption and labor supply: An explanation of the relationship between income and con sumption over the life cycle. Amer. Econom. Rev. 64(1):188–194.

Hsu C, Lu H (2004) Why do people play on-line games? An extended TAM with social influences and flow experience. Inform. Management 41(7):853–868.

Jenkins D (2014) How microtransactions conquered the video games industry. Metro (January 28), https://metro.co.uk/2014/01/28 like-taking-sweets-from-a-gamer-the-numbers-behind-the-hugel -popular-apps-4279836/.

Lee Y, Tan Y (2014) Effects of different types of free trials and ratings in sampling of consumer software: An empirical study. J. Man agement Inform. Systems 30(3):213–246.

Lin M, Ke X, Whinston AB (2012) Vertical differentiation and a comparison of online advertising models. J. Management Inform. Systems 29(1):195–236.

Liu D, Li X, Santhanam R (2013) Digital games and beyond: What happens when players compete? MIS Quart. 37(1):111–124.

MaCurdy TE (1981) An empirical model of labor supply in a life-cycle setting. J. Political Econom. 89(6):1059–1085.

Malone TW, Lepper MR (1987) Making learning fun: A taxonomy of intrinsic motivations for learning. Snow RE, Farr MJ, eds. Ap titude, Learning, and Instruction, Vol. 3: Conative and Affective Process Analyses (Lawrence Erlbaum, Hillsdale, NJ), 223–253.

Manninen T, Kujanpa¨a T (2007) The value of virtual assets¨ —The role of game characters in MMOGs. Internat. J. Bus. Sci. Appl. Man agement 2(1):21–33.

McGonigal J (2011) Reality is Broken: Why Games Make Us Better and How They Can Change the World (Penguin Press, New York).

Moffitt RA (2002) Welfare programs and labor supply. Handbook of Public Economics, vol. 4 (Elsevier, Amsterdam).

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Nielsen (2014) Multi-platform gaming: For the win! Nielsen Newswire (May 27), https://www.nielsen.com/us/en/insights/news/2014 multi-platform-gaming-for-the-win.html.

Park A (2014) Little by little, violent video games make us more aggressive. Time (March 24), http://time.com/34075/how-violent -video-games-change-kids-attitudes-about-aggression/.

Robertson A (2014) Is my child spending too much time playing video games? Guardian (June 5), https://www.theguardian.com technology/2014/jun/05/is-my-child-spending-too-much-time -playing-video-games.

Ryan RM, Rigby CS, Przybylski A (2006) The motivational pull of video games: A self-determination theory approach. Motivation Emotion 30(4):344–360.

Solomon J (2014) Candy Crush maker prices IPO. CNNMoney (March 25), https://money.cnn.com/2014/03/25/investing king-digital-ipo/index.html.

Sundararajan A (2004) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

SuperData Research (2013) Free-to-play online games market. Accessed June 2017, http://www.superdataresearch.com/market-data/online -games-research/.

Trudeau M (2010) Video games boost brain power, multitasking skills Morning Edition (December 20), https://www.npr.org/2010/12 20/132077565/video-games-boost-brain-power-multitasking-skills.

Venkatesh V (1999) Creation of favorable user perceptions: Exploring the role of intrinsic motivation. MIS Quart. 23(2):239–260.

Webster J, Martocchio JJ (1993) Turning work into play: Implications for microcomputer software training. J. Management 19(1):127–146.

Yee N (2006) Motivations for play in online games. Cyberpsych. Behav 9(6):772–775.

Yousafzai S, Hussain Z, Griffiths M (2014) Social responsibility in online videogaming: What should the videogame industry do? Addiction Res. Theory 22(3):181–185.

Zhan JD, Chan HC (2012) Government regulation of online game addiction. Comm. Assoc. Inform. Systems 30:13.

Zhang J, Seidmann A (2010) Perpetual vs. subscription licensing un der quality uncertainty and network externality effects. J. Management Inform. Systems 27(1):39–68.
