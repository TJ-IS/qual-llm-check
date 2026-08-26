---
otero_id: 7200
otero_key: "NN2HWKWC"
title: "Social Influence and Monetization of Freemium Social Games"
authors: "Bin Fang; Zhiqiang (Eric) Zheng; Qiang Ye; Paulo B. Goes"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1628878"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Social Influence and Monetization of Freemium Social Games

Bin FangBIN FANG, Zhiqiang (Eric) ZhengZHIQIANG (ERIC) ZHENG, Qiang YeQIANG YE & Paulo B. GoesPAULO B. GOES

To cite this article: Bin FangBIN FANG, Zhiqiang (Eric) ZhengZHIQIANG (ERIC) ZHENG, Qiang YeQIANG YE & Paulo B. GoesPAULO B. GOES (2019) Social Influence and Monetization of Freemium Social Games, Journal of Management Information Systems, 36:3, 730-754, DOI: 10.1080/07421222.2019.1628878

To link to this article: https://doi.org/10.1080/07421222.2019.1628878

![](/api/attachments/NN2HWKWC/fulltext/images/c13964c864ae8bf90ea44f315a09703b34675602918c928d06fd1bd64224cab1.jpg)

Published online: 04 Aug 2019.

![](/api/attachments/NN2HWKWC/fulltext/images/a4e7e8de45eccff35cfcd0a01561166ccbdabd3a30f5f671b44a544035062b5a.jpg)

Submit your article to this journal

![](/api/attachments/NN2HWKWC/fulltext/images/f2fac390452e563bb0984d6e5f2521f3f7945a9b917f5d760e23f571aa336cde.jpg)

View Crossmark data

# Social Influence and Monetization of Freemium Social Games

BIN FANG, ZHIQIANG (ERIC) ZHENG, QIANG YE, AND PAULO B. GOES

BIN FANG (fangbin@xmu.edu.cn) is an assistant professor in the Department of Management Science at School of Management, Xiamen University, China. He received his Ph.D. in Information Systems at Harbin Institute of Technology, China. Dr. Fang’s research interests include social networks, online market, and online user-generated content. His work has appeared in such journals as Decision Support Systems, Journal of Electronic Commerce Research, and Tourism Management.

ZHIQIANG (ERIC) ZHENG (ericz@utdallas.edu; corresponding author) is Ashbel Smith Professor in the Department of Information Systems and Operations Management at the Jindal School of Management, University of Texas at Dallas. His research interests focus on Business Analytics (fintech, healthcare analytics, and social media analytics). He is a senior editor at Information Systems Research. He has published in Information Systems Research, Management Science, MIS Quarterly, and Production and Operations Management, among others.

QIANG YE (yeqiang@hit.edu.cn) is a Professor of Information Systems in the Department of Management Science and Engineering and Dean at School of Management, Harbin Institute of Technology, where he received his Ph.D. in Information Systems. Dr. Ye’s research interests include electronic commerce, Internet finance, social networks, IT governance, and data mining. He has published in Information Systems Research, Production and Operations Management, and Decision Support Systems, among others. He serves as associate editor for Journal of Electronic Commerce Research and as area editor for Electronic Commerce Research and Applications.

PAULO B. GOES (pgoes@eller.arizona.edu) is the Dean, Halle Chair in Leadership, and Professor of Management Information Systems at the University of Arizona’s Eller College of Management. His research interests include information technology evaluation, electronic markets, online auctions, and technology infrastructure. He has published in Information Systems Research, Journal of Management Information Systems, Management Science, and MIS Quarterly, among others.

ABSTRACT: One fundamental economic challenge in social gaming is how to monetize players. We address this problem from the lens of social influence. Specifically, we examine how players’ paying behaviors in a social game are associated with their pure friends and Simmelian-tie friends. Analyzing a comprehensive social game dataset provided by Tencent.com, we find that the cohesion effect emanating from players’ direct connections in the social gaming network exhibits positive impacts on players’ willingness to pay. Surprisingly, the cohesion effect of pure friends is found to be significantly stronger than that of Simmelian-tie friends, contrary to the common findings in the literature. These new findings have direct implications for companies tasked with designing social games or gamification systems and, more broadly, to help better understand the mechanism behind the microscopic economic behavior of individuals in a virtual economy.

KEY WORDS AND PHRASES: online games, social games, freemium social gaming, player cohesion, Simmelian tie, online monetization.

## Introduction

The rapid worldwide growth of smart devices has catapulted online gaming into a major market which generated \$108.9 billion revenue in 2017 [42]. Over 40 percent of internet users now play some sort of online games [60]. Among these, social games, in which players interact with other players socially rather than play in solitude, have gained most popularity. Honor of Kings, the most popular mobile social gaming in China in 2017, is an example. The number of registered users has exceeded 200 million [35], and the game generated approximately \$150 million in revenue in the single month of June 2017 [16]. League of Legends also garnered similar level of revenues in 2017 [44].

Although there are some success stories in the online game industry, one common challenge that all gaming companies still grapple with is how to monetize their games, that is, how to entice more players to play and pay. Only 20 out of 10,000+ Facebook games attract more than one million active users [55]. Research shows that 85 percent of new players quit after the first day without paying anything [17]. To overcome these challenges, most games adopt a freemium (free + premium) business model [14], where the company offers a free but limited services to users, but then charges for premium services [3]. This strategy enables the company to acquire a large number of users in the beginning. However, how to entice them to pay for the premium services next becomes the critical success factor. Only a few players spend heavily in a game; for example, the legendary player with ID lllllll1 in the game, Legend, squandered more than five million dollars in total, whereas most players spend nothing. Yakuel [62] estimated that no more than 2 percent of players ever paid. How to engage players and subsequently make them spend money are imperative for a freemium social game.

This research seeks to unravel the factors influencing a player’s economic decision to pay from a social influence perspective. Social influence is an important force that affects both the individual and organization’s behavior. The individual level social influence appears in charitable giving [53], students’ academic achievement [38], and online rating [39, 54]. Social influence also affects firms’ behavior, such as the abandonment of organizational practices [24] and the splitting of stocks [31]. However, how social influence affects individual players’ paying decisions in a freemium social game environment remains under-researched. Social games present unique opportunities to study individuals’ social and economic behaviors in a closed-game society. Geng et al. [26] find that both direct and indirect friends have a significant influence on users’ repeat-purchase decisions. Shi et al. [51] observe that having more friends induces players to pay more. Zhang et al. [63] show that the impact of the number of friends is not monotonic: while having some friends initially increases a user’s spending, but having too many friends curbs it.

The literature on social influence identifies the cohesion effect as a fundamental driving force behind an actor’s behavior in a social network [12]. The cohesion effect refers to the impact of direct contacts in a social network [12, 19]. In this paper, we focus on the cohesion effect (or, intuitively, the peer effect exerted from the friends in the game in our context) and further differentiate the cohesion effect emanating from pure friends and the cohesion effect resulting from Simmelian-tie friends, where two friends share other common friends [32]. Methodologically, we examine the two types of network forces in a dynamic network setting.

Utilizing a unique and comprehensive dataset amassed by the social media leader, Tencent.com, in China, we analyze players’ economic behaviors empirically in one of the most popular mobile social games – RoyalSword. This is a multiplayer, role playing social game where players meet to make friends with others, fight against monsters, accomplish missions, buy or sell items in the market, and so forth. Gamers realize their economic value (to Tencent) by purchasing virtual goods such as precious stones, metals, and scribes, which are essential for players to enhance their chance of winning battles.

Our empirical analysis yields several key findings. First, cohesion (i.e., peer effect) exerts significant influence on players’ willingness to pay. Second, the magnitude of the cohesion effect resulting from pure friends is significantly larger than that which results from Simmelian-tie friends. Furthermore, the magnitude of the cohesion effect is different depending on the number of friends a player has: the effect of Simmelian-tie friends becomes closer to that of pure friends when the number of friends is small.

These findings have direct implications for gaming companies in their efforts to better personalize their marketing promotions and design their games strategically. These implications are elaborated in the concluding section of the paper. Moreover, the applicability of our findings goes beyond games. Innovative applications using social games have been developed to solve large-scale complex science problems: for example, ESP Game for massive random images labeling [1], and Foldit for protein structure prediction problem solving [15]. Understanding players’ behaviors is also crucial for firms to design gamification features in crowdsourcing contests, complex business and science problems, and virtual economies [36]. Examples include Microsoft’s Ribbon Hero, which trains customers to use the newly designed ribbon features in Office 2007 and 2010 [37], and Adobe’s LevelUp for Photoshop to increase revenue [50].

We make two contributions in this paper. First, this study represents one of the first attempts to investigate the peer effect of Simmelian ties on consumers’ economic behavior in a freemium business model. Second, we differentiate the peer effect resulting from pure friends with that resulting from Simmelian-tie friends. The literature on the peer effect has primarily focused on the peer effect of friends in general (e.g., [11, 19, 21, 32, 33]), whereas we show in this paper that the two types of friends (pure and Simmelian-tie) generate different peer effects with different influences on players.

The rest of this paper begins by reviewing the specific online game that serves as our research context. The third section summarizes related literature and develops hypotheses, followed by our research model and our variable construction in the fourth section. The fifth section presents the econometric analyses and results. We conclude the paper in sixth and final section by revisiting the findings with discussions.

## Research Setting

The game we study is named RoyalSword, a mobile freemium social game released by Tencent on June 1, 2011. It gained 5 million active users within 4 months [56]. This game mainly targets mobile users, and Tencent offers a variety of mobile versions under different platforms, including iOS, Android, Symbian, and Java, as well as a web version for PC gamers. This game became one of the most lucrative mobile games in the world with a monthly revenue reaching more than \$3 million in April 2013, ranked sixth among all mobile games in China at that time [25]. According to the statistics by App Annie, daily downloading of this game ranked as high as thirteenth among all the games in the world during the period from September 1, 2012 to March 9, 2015.

RoyalSword avatarizes an unspecified ancient time of China, where avatars are impersonalized as swordsmen or knights. The game provides many gaming functions for players. The screenshots in Figure 1 depict how players socialize with others by making friends via clicking an “Add Friend” button (Figure 1a), by fighting against other players (Figure 1b) or fighting against monsters (Figure 1c), and so forth. As this game mainly caters to mobile players, it does not require much skill or agility in fighting. Unlike the real-time fighting system in World of Warcraft, RoyalSword applies the form of a “round” fighting system. Players have 30 seconds to select what they will do in the chosen round. In such a fighting system, the attacking and defense levels of the two avatars largely determine the result instead of skills of the two players.

Players seek to become more “powerful” in this virtual world, where power is measured by players’ attribute points, including attack power, health point, magic point, and so forth. Power also comes from players’ ranks in a reputation system based on the results of fights (Figure 1d). A player can easily track another player’s social status by visiting this reputation system.

![](/api/attachments/NN2HWKWC/fulltext/images/477b27a5ab303454e366d477c63bfb6e5d0a2f119ec8c0eb979ad8fbe5a9a96e.jpg)

![](/api/attachments/NN2HWKWC/fulltext/images/faf00ba097c1aed54b63e199ce45aeba9bc366cbf3a9db341403efa0147a9306.jpg)  
1b

1a  
![](/api/attachments/NN2HWKWC/fulltext/images/71f1bff44d2e17a4b14e0eb0ce8cc6e96fe0212ea2681c5f4e1fe32c598cc1fd.jpg)  
1c

![](/api/attachments/NN2HWKWC/fulltext/images/5ecda5b899e5b9ff1969791d28b7cf64cc0a9d0557dcdd849856f582376b9ef2.jpg)  
1d  
Figure 1. Screenshots of RoyalSword

Although this game is free for downloading and playing the basic features, it uses a freemium business model for the most advanced features. Players have to pay real money to buy virtual goods if they want to win more easily or advance more quickly. At RoyalSword, players need to buy virtual money named Xianyuan or Yuanbao from Tencent using real money (1 unit of Xianyuan or Yuanbao equals to 0.01 RMB). The only difference between Xianyuan and Yuanbao is that the former can be spent in both virtual shops created by Tencent and in the designated open markets in the game, while the latter can only be spent in virtual shops.

Players can spend their virtual money to buy precious items from the virtual shops or from other players through the designated open markets in the game. The designated open markets are similar to the C2C marketplaces, where some players can sell items obtained by winning battles against monsters. In these markets, the players could sell anything that is allowed to be sold at any price (some restricted items cannot be sold by individuals in the market). These items can improve the power of their weapons, strengthen the role itself, or implement such functions in the game as energy recovery, flash moving (to some places), and so forth. Meanwhile, virtual shops sell certain items which are helpful (but not necessary) to win fights that otherwise could not be obtained via winning fights. Usually, items sold in the virtual shops cannot be obtained in battles and, therefore, cannot be found in the designated open markets. If a player wants to upgrade her weapons, she has to purchase items both from the markets and the shops since the shops sell some reserved items that are not available in the open market. These are the only two ways players can spend virtual money.

## Hypothesis Development

A defining feature of a social game is role playing: players act in different roles within a (virtual) social network. For example, in World of Warcraft, players can join in guilds to jointly accomplish a mission; gamers at RoyalSword can form a temporary or permanent team to besiege a castle. Thus, every player is embedded in some kind of social network he chooses to join in. A player often needs to reference other players when making decisions. We are primarily interested in how social factors drive players to pay.

In his seminal work, Burt [12] identified a fundamental network force – cohesion – which determines how actors influence each other in a social network. Cohesion, also called social learning or peer effect (hereafter we use the cohesion effect and the peer effect interchangeably), focuses on influences between two directly connected neighbors in a social network. In a connected society, actors learn from their neighbors’ choices and tend to subsequently choose the same actions [5]. Players socialize with each other in a social game, effectively organizing themselves into social networks. A player’s behavior is thus influenced by other players in the network. We first investigate the cohesion effect within the friend network and then compare two types of cohesion effects resulting from pure friends and Simmelian-tie friends.

## Cohesion Effect

The behavior contagion theory prescribes how the cohesion effect (peer effect) from peers can occur among a circle of friends [2]. Friends are found to be one of the strongest external sources of contagion [29]; friends’ opinions are most credible [40]. Hence, an individual tends to comply with his peers’ behaviors [22, 64], since he trusts friends more than others. Friends’ preferences can even be more influential than an individual’s own preferences when it comes to decision making [43].

The cohesion effect not only exists in the real world but also in the virtual world. Facebook experimented with 61 million users and found that individuals’ behaviors of updating their Facebook pages were influenced by the sentiment of the messages received, and they in turn influenced their friends, and friends of friends, and so on [9]. Another experiment in Facebook suggests that the probability of a user giving a like to an update is significantly affected by his friends [20]. Similar behavior can be expected in a social game. Having friends who pay more and possess more virtual assets is likely to lure the focal player into paying more, especially when the possessions (e.g., arms and weapons) and attribute points of their friends are easily observable, as in games like RoyalSword. In order to catch up with their friends, players tend to pay to upgrade themselves. For example, a RoyalSword player posted a blog that recalled his experience of playing with friends and described how they ended up buying the same items from the game in tandem with each other.<sup>1</sup> Accordingly, we propose Hypothesis 1.

Hypothesis 1. A player’s willingness to pay is positively associated with his or her friends’ willingness to pay.

## Simmelian Ties

In a social network, there are 2 types of friendship: pure friends and friends with mutual friends. Pure friends refer to a pair that does not share common friends, while friends with mutual friends denote the pairs that share common friends. Figure 2 illustrates these 2 types: A and B are pure friends since they do not share any common friends in this network, while A and C are friends with a common friend D.

Two friends sharing a common friend form a closed triad, and each tie in the triad is called the Simmelian tie [32], as illustrated by the triad consisting of A, C and D in Figure 2. It is widely believed that a Simmelian tie is stronger than a regular tie (i.e., a pure friend) [32]. Trust between two actors in a Simmelian tie is reinforced, since each would feel the threat of being ostracized by the shared friend for untrustworthy behavior [13]. Simmelian-tie dyads are more likely to reach higher organizational culture agreement [33]. Also, compared to regular dyadic ties, Simmelian-tied team members are more capable of thwarting external competition [30]. In sum, the extant literature suggests that trust in Simmelian ties are stronger, thereby making the cohesion effect between two Simmelian-tie actors stronger. Accordingly, we propose Hypothesis 2a.

Hypothesis 2a. Simmelian ties’ impact is stronger than that of pure friends’ on a player’s willingness to pay.

The literature has mainly focused on the physical world context (e.g., firms or colleagues), assuming therein that Simmelian ties are strong ties. However, this may not always be the case in an online social network environment. Friendship in an online social network may be established merely based on some ad-hoc event, such as liking a user’s picture [7].

![](/api/attachments/NN2HWKWC/fulltext/images/a7f6986d43b2cdcffcf42543c6e5c7a79ba10168afd56865ce42180450eda0a2.jpg)  
Figure 2. An example of two friendship types

In online social gaming, a player may simply send a friend request to another player because of the latter’s beautiful virtual dress. When friendship is built on such a weak tie, individuals would not necessarily feel the anxiety of being ostracized. Similarly, the Simmelian tie formed in the online world may play a different role. For example, a Facebook field experiment demonstrates that the trust between Simmelian ties can be weaker than that of pure friend ties, especially for users who already have a large number of friends [7]. When mutual trust decreases in such cases, the peer effect of Simmelian ties is expected to weaken. Ugander et al. [57] provide evidence to support this point. They empirically analyzed the growth of Facebook and found ties with fewer common connections are associated with greater influence power on the adoption of Facebook [57]. Furthermore, an investigation on Twitter information sharing suggests that sharing common connections may negatively influence users’ decisions on sharing the information coming from their connections [48]. Therefore, pure friend ties and Simmelian ties might play quite different roles in the online context.

One of the possible reasons for the existing finding that pure friends are more important in the online context is that the pure friends are special friends, whereas when users are in a clique (i.e., a Simmelian tie), no one is really unique. The special nature of the bond between pure friends may arise from the fact that pure friends are not subject to competing Simmelian ties; thus, they can devote more time to the focal user and make this relationship special.<sup>2</sup> In other words, it could be that Simmelian-tie friends tend to be more well-connected, which renders the focal user less important to them. Consequently, we propose the alternative Hypothesis 2b.

Hypothesis 2b. Simmelian ties’ impact is weaker than that of pure friends’ on a player’s willingness to pay.

## Data and Method

## Big Gaming Data

We obtained the complete server log data for the game RoyalSword from Tencent directly. Tencent provided us with one month of data for November 2012 from its most representative server. As players cannot interact across servers, one server represents an isolated, independent small world. One month represents a sufficiently long time span in social gaming, as 90 percent of players do not last more than one month [17]. We processed the data day-by-day. This server contains 86,022 players who logged into the game at least once during the month of November. All players are included for analysis. Their average playing time during this month is 7,873 seconds (or 131.2 minutes). Among these players, 8,433 players (9.8 percent) spent money, at an average of 10.52 RMB (about 1.67 dollars). The highest spender spent 160,943.57 RMB (about \$25,000).

The raw server-log text files record the complete gaming activities of all the players, totaling more than 1 TB of data, with more than 30 billion data records. The data mainly consists of 4 parts: 1) transaction log, 2) game play log, 3) social networking log, and 4) game item consumption log. The transaction log records transaction time stamp, items bought/sold, buyer and seller ID, quantity and price of the transaction, and so forth. The game play log consists of three parts: mission accomplishment (e.g., conquering a castle), fights against other players, and fights against NPC (Non-Player Characters such as monsters in the game). These log files record the time stamp of the play, player ID, win/loss status, and consumption of gaming items in a battle. The social networking log tracks every single change in the network, such as the time of adding/deleting a friend. The game item consumption log records when and how an item was used, upgraded, or consumed for every player. We then processed these raw logfile data to construct our variables.

## Dependent Variable

A player’s monetary/economic value to Tencent, that is, how much this player has spent in this game, is our dependent variable. It is a direct measure of the player’s willingness to pay. We construct the player’s economic value by summing a player’s total spending in the game at the daily level from the transaction and item consumption logs.

## Social Network Variables

We construct the friend networks dynamically by each day. Players at RoyalSword can add or delete a friend at any day. We build the friend network based on the snapshot provided by the company on the first day of our observed data period (November 1, 2012). We then refer to the adding and deleting action logs to reproduce the dynamic friend network for each of the subsequent days.

The main set of network constructs we consider is cohesion. We simply average the economic value (i.e. how much an individual has paid to Tencent) of all the directly connected players in a network as cohesion. The cohesion variable is instantiated as the mean of friends’ daily economic values, that is, Cohesio $\begin{array} { r } { \begin{array} { r } { \boldsymbol { \eta } _ { i , t } = \frac { 1 } { | \boldsymbol { M } | } \sum _ { j \in \boldsymbol { M } } } \end{array} } \end{array}$ DailyEco<sub>j;t</sub>, where M is the set of player i’s friends at time t, and $D a i l y E c o _ { j , t }$ is the daily economic value of player j at time t. As we differentiate the two types of peer effects, pure friends and Simmelian-tie friends, we construct two different peer effects variables accordingly. The first one includes only friends without mutual friends, that is, pure friends (PFriend), while the other includes only Simmelian-tie friends (SFriend).

## Control Variables

The first set of control variables we consider include player-specific factors: earned virtual money, level, online time, and past spending behavior. Earned virtual money (EarnedVirMoney) is measured by a virtual currency in the game named Yinliang. Yinliang can only be earned by activities such as accomplishing missions or selling personal items. Officially, Yinliang cannot be bought directly using real money or other types of virtual money called Xianyuan or Yuanbao, which can only be earned by paying real money to Tencent. Online time measures the total time a player spent on this game up to that day (Online), and level denotes the level a player had reached at the end of a day (Level). Past spending behavior is measured by the cumulative economic value created (i.e., real money spent) by the player up to time t (CumuEco).

We also controlled centrality for the friend network. Centrality represents the prominence of an actor’s position in a social network. It plays an important role in many fields, for example, firm behavior in car dealer networks [18], adoption process of innovations [27]. We used degree centrality, which denotes the number of other nodes to which a given node is connected [23]. Table 1 provides a brief description of all these variables, and Figure 3 illustrates distribution of some selected variables. Table A1 in the Supplemental Material presents the descriptive statistics for these variables and Table A2 tabulates the correlation matrix.

## Research Model

Our econometric model is based on the two-regime network effects model with autocorrelation proposed by Doreian [19] as

$$
y _ {i, t} = \mathbf {X} _ {\mathbf {i}, \mathbf {t}} \beta + \rho_ {1} P F r i e n d _ {\mathbf {i}, t} + \rho_ {2} S F r i e n d _ {\mathbf {i}, t} + \varepsilon_ {i, t}\tag{1}
$$

Table 1. Description of Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>DailyEco $_{i,t}$ </td><td>Log transformed daily economic value of player i at time t.</td></tr><tr><td>PFriend $_{i,t}$ </td><td>Log transformed mean daily economic value of pure friends of player i at time t.</td></tr><tr><td>SFriend $_{i,t}$ </td><td>Log transformed mean daily economic value of Simmelian-tie friends of player i at time t.</td></tr><tr><td>Level $_{i,t}$ </td><td>Level of player i at time t.</td></tr><tr><td>EarnedVirMoney $_{i,t}$ </td><td>Log transformed virtual money possessed by player i at time t.</td></tr><tr><td>Online $_{i,t}$ </td><td>Log transformed daily online time for player i at time t.</td></tr><tr><td>CumuEco $_{i,t}$ </td><td>Log transformed cumulative economic value of player i at time t.</td></tr><tr><td>PFDegree $_{i,t}$ </td><td>Number of pure friends for player i at time t.</td></tr><tr><td>SFDegree $_{i,t}$ </td><td>Number of Simmelian tied friends for player i at time t.</td></tr></table>

![](/api/attachments/NN2HWKWC/fulltext/images/4cea3f085efb30e6fa8c84e3bcde69321b2f192cf97d45e493fce94743d6f5ef.jpg)  
3a

![](/api/attachments/NN2HWKWC/fulltext/images/facceef9f6650681caa3446d6d20e53e1a95ce81725adcaa04b228f85a64b7b2.jpg)  
3b

![](/api/attachments/NN2HWKWC/fulltext/images/4bbbb04ad111d6f32b53fc7626c843353a2865a387a2b3cef138d141ce2b8016.jpg)  
c3

![](/api/attachments/NN2HWKWC/fulltext/images/394867ac4dd43b83466fca54a9f38ce6607443f2ea2069eaff378ed8844ad458.jpg)  
d3

![](/api/attachments/NN2HWKWC/fulltext/images/7cc35da896789d2794a642e2cb555f2f89b74971739899f725389a0af2340da4.jpg)  
3e  
Figure 3. Distribution of selected variables

where y denotes the economic value of a gamer (i.e., how much he has paid at time t in the game); $P F r i e n d _ { i , t }$ represents the payment of player $i \ ' \mathrm { s }$ pure friends at time $t ;$ $S F r i e n d _ { i , t }$ represents the daily payment of player $i \mathbf { \ ' } _ { \mathbf { S } }$ Simmelian-tie friends at time t; and $\rho _ { I }$ and $\rho _ { 2 }$ are the two corresponding coefficients. <sup>X</sup> is a vector of control variables and $\varepsilon _ { i , t }$ is the random error term.

The unit of analysis of our panel data is player-day; that is, each player in a day consists of one observation. Observations for which the player was not online at $t \left( \mathrm { i . e . , } O n l i n e _ { \mathrm { i , t } } = 0 \right)$ were excluded, since we cannot observe the economic value or social influence of that player. Please note that although we exclude the players who did not show up at time t in our empirical analysis, they still remain in our variable construction. Take the friend peer effect, for example. The peer effect variable for player i at time t is the average of her friends’ economic value at time t. If player i does not show up at time t at all, this observation will not be (and should not be) included in the regression. However, if one of her friends does not show up at time $t ,$ the economic value of this friend at time t is set to zero when calculating the average.

It might be argued that self-selection bias can occur here since players with a certain level of economic value may self-select to play (or not play) games at time t or to make (or not to make) friends at t. To address such a concern, we apply the two-step panel data selection model proposed by Semykina and Wooldridge [49]. We construct the following three selection equations:

$$
s _ {i, t} ^ {1} = \theta_ {0} ^ {1} + \theta_ {1} ^ {1} \text { Level } _ {i, t} + \theta_ {2} ^ {1} \text { OnlineCumu } _ {i, t} + \theta_ {3} ^ {1} \text { EarnedVirMoney } _ {i, t} + v _ {i, t} ^ {1}\tag{2}
$$

$$
s _ {i, t} ^ {2} = \theta_ {0} ^ {2} + \theta_ {1} ^ {2} L e v e l _ {i, t} + \theta_ {2} ^ {2} O n l i n e C u m u _ {i, t} + \theta_ {3} ^ {2} E a r n e d V i r M o n e y _ {i, t} + v _ {i, t} ^ {2}\tag{3}
$$

$$
s _ {i, t} ^ {3} = \theta_ {0} ^ {3} + \theta_ {1} ^ {3} \text { Level } _ {i, t} + \theta_ {2} ^ {3} \text { OnlineCumu } _ {i, t - 1} + \theta_ {3} ^ {3} \text { weekend } _ {t} + v _ {i, t} ^ {3}\tag{4}
$$

where $s _ { i , t } ^ { 1 }$ denotes whether or not player i has pure friends at time t, and $s _ { i , t } ^ { 2 }$ denotes whether player i has Simmelian-tie friends at time t or not. There are three factors that we believe can influence whether the player has pure friends or Simmelian-tie friends: level (Level), cumulative online time (OnlineCumu), and virtual money earned (EarnedVirMoney). Level is important because it represents a player’s game experience, which will influence her friends’ decision making process [63]. Cumulative online time is important because the more time a player stays in the game the higher probability that she will make a friend. $s _ { i , t } ^ { 3 }$ represents whether player i plays game at time t. Cumulative online time is important here because it is a measure of players’ behavior in the past, and it is reasonable that such a behavioral pattern would be continued. The dummy variable weekend represents whether time t is weekend time. Players would have more time to relax during weekends. The observation period in our data does not include national holidays.

Following Semykina and Wooldridge [49], we estimate the above three selection equations separately for each period, that is, we ran 3 × 29 Probit models (the first period was dropped since there is no lagged term of online time). Inversed Mills ratios $( \lambda ^ { 1 } , \lambda ^ { 2 }$ , and $\lambda ^ { 3 } )$ were calculated according to the estimation results, and included in Equation (1) to address the selection bias. Accordingly, our final econometric model is:

$$
\begin{array}{l} D a i l y E c o _ {i, t} = \rho_ {1} P F r i e n d _ {i, t} + \rho_ {2} S F r i e n d _ {i, t} + \mathbf {X _ {i , t}} \beta + \alpha_ {1} \lambda_ {i, t} ^ {1} + \alpha_ {2} \lambda_ {i, t} ^ {2} + \alpha_ {3} \lambda_ {i, t} ^ {3} \\ + \varepsilon_ {i, t} \end{array}\tag{5}
$$

## Empirical Analysis

## Econometric Estimation

Several econometric issues need to be tackled with first before estimating Equation (5). We start with model specification. For each player, there might be unobserved individual-specific heterogeneity that could influence a player’s paying behavior but is unaccounted for. For instance, players’ income can be such an unobserved factor. This makes the fixed-effects model, which accounts for such time-invariant individual-specific effects, more appropriate. The Hausman test statistic rejects the random effects model (Hausman specification statistic $\chi _ { 1 2 } ^ { 2 } = 2 4 , 4 7 6 . 1 9$ , p-value < 0.001) and we thus adopt the fixed effects model.

Multicollinearity does not pose an issue here based on the variance inflation factors (VIF). The highest VIF is 2.198 (see the second column of Table A2 in the Supplemental Material), below the cutoff of 10, indicating no serious multicollinearity [61]. Table A2 in the online Supplemental Material reports the correlation matrix of the independent variables, which shows there is no high correlation among our variables.

We performed a modified Wald test to check the possible presence of heteroscedasticity. The result indicates the presence of heteroscedasticity in our model $\big ( \gamma _ { 5 9 3 8 } ^ { 2 } =$ 1.8e + 14, p-value < 0.001). Therefore, we applied the robust standard error [6].

Potential endogeneity can arise from our social influence variables. Endogeneity of social influence variables could lead to the reflection problem [41]. It can be argued that a high-valued player tends to have more social ties and hence simultaneity may inflict our cohesion variables. We constructed instrument variables (IV) for social influence variables to address this issue. Bramoullé et al. [10] proved theoretically and empirically that the behavior of friends’ friends of an actor who are not his direct friends could serve as good instruments of his friends’ behavior. Shriver et al. [52] also used the number of friend requests of an actor’s friends as an IV, and demonstrated its validity. Similarly, Oestreicher-Singer and Sundararajan [46] adopted characteristics of an $\mathrm { a c t o r } ^ { \bullet } \mathrm { s }$ secondary neighbors as IV of his neighbors.

Following this stream of literature, we propose the use of the average economic value of those friends’ friends who themselves are not the friends of a player as an IV for cohesion, that is, cohesion $\begin{array} { r } { i \nu _ { i } = \frac { 1 } { | M | } \sum _ { j \in M } \frac { 1 } { \left| P _ { j } \right| } \sum _ { k \in P _ { j } } D a i l y E c o _ { k } } \end{array}$ , where M is the set of player i’s neighbors, and $P _ { j }$ is the set of players belonging to the set of j’s neighbors but not in M. Cohesion of friends’ friends is clearly correlated with the friend’s economic value. However, the friends’ friends do not influence player i directly. Therefore, this serves as a good instrumental variable.

We then formally test the strength and exogeneity of these IVs. Angrist and Pischke [4] introduce the first-stage F and $\chi ^ { 2 }$ statistics for the identification of IV. All of the statistics are significant with $\mathsf { p } < 0 . 0 0 1$ , which suggests that these IVs are not weak. Additionally, the Cragg-Donald Wald F statistic for weak identification is 223.78, the Kleibergen-Paap Wald F statistic for weak identification is 224.38, and the Kleibergen-Paap LM statistic for under-identification is 428.51, all pointing to strong IV. Exogeneity of IVs is typically ensured through the over-identification test using the Hansen’s J statistic [28]. This statistic is 0.000, pointing to exogeneity of our IVs.

For comparison purposes, we first estimate 2 basic models to better understand the impact size of the variables of interest, as reported in Table 2. The first model includes only the control variables (column 1 of Table 2), while the second one encompasses all variables (column 2 of Table 2). We calculate the F-statistic value to formally compare the fit of these two models, and the results suggest a significant improvement of the model fit of the second model (F(2, 93064) = 1,938.83, p < 0.001).

## Results

In estimating the two-step selection model, we incorporated IVs to address endogeneity for these cohesion variables and applied robust standard errors. Table 3 reports these results.

Hypothesis H1 investigating the peer effect in the friend network is supported, since both coefficients PFriend and SFriend are positive and significant. This indicates that players’ economic values are positively influenced by their direct friends. More specifically, for each one percentage point of additional total economic value contributed by a player’s pure friends, the player’s own value rises by 2.294 percent (p < 0.01); for each one percentage point of additional total economic value contributed by his Simmelian-tie friends, the player’s own value rises by 0.858 percent (p < 0.01). Though these percentages seem to be small, we should not underestimate the actual economic impact. Given the \$3 million monthly revenue of the game [25], a one percentage point increase equals about \$30,000 in additional total revenue per month.

Table 2. Baseline Model and Full Models

<table><tr><td>DailyEco</td><td>(1)</td><td>(2)</td></tr><tr><td>PFriend</td><td></td><td>0.017(0.0033)***</td></tr><tr><td>SFriend</td><td></td><td>0.014(0.0033)***</td></tr><tr><td>EarnedVirMoney</td><td>0.052(0.0073)***</td><td>0.052(0.0073)***</td></tr><tr><td>Online</td><td>0.315(0.0088)***</td><td>0.311(0.0088)***</td></tr><tr><td>Level</td><td>-0.042(0.0065)***</td><td>-0.040(0.0065)***</td></tr><tr><td>PFDegree</td><td>-0.003(0.0023)</td><td>-0.005(0.0024)**</td></tr><tr><td>SFDegree</td><td>-0.001(0.0021)</td><td>-0.001(0.0021)</td></tr><tr><td>N</td><td>93,064</td><td>93,064</td></tr><tr><td>R2</td><td>0.024</td><td>0.025</td></tr><tr><td>AIC</td><td>397,177.8</td><td>397,126.9</td></tr><tr><td>BIC</td><td>397,225</td><td>397,193</td></tr><tr><td>F</td><td>263.299</td><td>190.663</td></tr></table>

\*\*\* $\mathfrak { p } < 0 . 0 1 . \ ^ { * * } \ \mathfrak { p } < 0 . 0 5 . \ ^ { * } \mathfrak { p } < 0 . 1$ . Robust standard errors are reported in parentheses.

Table 3. Main Model Results

<table><tr><td>DailyEco</td><td>Coefficients(Std. Err.)</td></tr><tr><td>PFriend</td><td>2.294(0.1235)***</td></tr><tr><td>SFriend</td><td>0.858(0.0946)***</td></tr><tr><td>Lag.DailyEco</td><td>0.056(0.0115)***</td></tr><tr><td>Lag.CumuEco</td><td>0.052(0.0147)***</td></tr><tr><td>EarnedVirMoney</td><td>-0.059(0.0171)***</td></tr><tr><td>Online</td><td>-0.084(0.0268)***</td></tr><tr><td>Level</td><td>0.146(0.0188)***</td></tr><tr><td>PFDegree</td><td>-0.211(0.0121)***</td></tr><tr><td>SFDegree</td><td>-0.039(0.0098)***</td></tr><tr><td>Inv. Mills ratio 1</td><td>-1.501(0.1380)***</td></tr><tr><td>Inv. Mills ratio 2</td><td>1.279(0.3468)***</td></tr><tr><td>Inv. Mills ratio 3</td><td>1.346(0.2196)***</td></tr><tr><td>N</td><td>89,413</td></tr><tr><td>AIC</td><td>567,655.8</td></tr><tr><td>BIC</td><td>567,768.6</td></tr><tr><td>F</td><td>79.330</td></tr><tr><td colspan="2">*** p &lt; 0.01. ** p &lt; 0.05. * p &lt; 0.1. Robust standard errors are reported in parentheses.</td></tr></table>

We applied the Wald $\chi ^ { 2 }$ test to contrast these two peer effects. The $\chi ^ { 2 } =$ 85.206 with $\mathsf { p } < 0 . 0 1$ suggests a significantly higher impact of the peer effect of the pure friends. Hence, H2b is supported, while H2a is not. This result is consistent with the work of Bapna et al. [7], which examined the trust factor of Facebook users and other prior related studies [48, 57]. This indicates that gaming companies need to pay more attention to players’ pure friends in their game design, rather than attending to Simmelian-tie friends, as the literature suggests. Companies should display the information of high-valued pure friends more saliently than that of Simmelian-tie friends.

## Robustness Checks

We conducted 2 robustness checks in this section.

## Two Stage Decision Model

Like any other freemium products, players in this game may first decide whether to pay, and if yes, then decide how much to pay. This forms a two-stage decision process. Since the dependent variable $D a i l y E c o _ { i , t }$ is a continuous variable with logarithmic transformation, a two-step Tobit model with fixed effects proposed by Kyriazidou [34] is most suited here to investigate players’ two-stage decision process, as shown in Equation (6). The Heckman two-step self-selection bias correction is also incorporated in this model, while the instrument variables are included through the control function approach (represented by $\mathbf { u _ { p f i e n d } }$ and $\mathbf { u _ { s f i r i e n d } } )$

$$
\left\{ \begin{array}{c} d _ {i, t} = 1 \bigl \{\eta_ {i} + \gamma_ {1} O n l i n e _ {i, t} + \gamma_ {2} C u m u E c o _ {i, t - 1} + \pi_ {i, t} \geq 0 \bigr \} \\ (y _ {i, t} | d _ {i, t} = 1) = \rho_ {1} P F r i e n d _ {i, t} + \rho_ {2} S F r i e n d _ {i, t} + X _ {i, t} \beta + \alpha_ {1} \lambda_ {i, t} ^ {1} + \alpha_ {2} \lambda_ {i, t} ^ {2} + \alpha_ {3} \lambda_ {i, t} ^ {3} + \varepsilon_ {i, t} \end{array} \right.\tag{6}
$$

The results presented in Table 4 are largely consistent with our main results reported in Table 3. The hypothesis of the peer effect in the friend network (H1) is supported, as both the coefficients of PFriend and SFriend are significantly positive. Furthermore, Simmelian-tie peer effect is weaker than the pure-friend peer effect, since the coefficient of PFriend is significantly larger than SFriend $( \chi ^ { 2 }$ is 235.086 with $\mathsf { p } < 0 . 0 1 )$ . Therefore, all conclusions in our paper still hold under the two-stage decision specification.

## Interaction between Payment and Friend Making

Although the reflection problem is partially addressed by our instrument variable estimation, there could still be potential simultaneity between friendship formation and players’ purchase behaviors. It is possible that players who spend more could attract more friends, since these rich players tend to be more powerful. Having rich friends would be helpful for players to accomplish missions and win battles. Therefore, players might have more friends if they spend more. To address this possible simultaneity, a panel vector autoregressive model is applied. Table 5 presents the results for the model with one-period lag terms of both players’ daily spending and their degrees.<sup>3</sup> As the table shows, all of the results are qualitatively consistent. The results show that there is no correlation between players’ spending in the game and their friend degree in the next period as shown in the insignificant coefficient of Lag.DailyEco in the second equation.

## Additional Tests

## Heterogeneity

We argued that it is relatively easy for players to establish friendships with others in online social gaming, which leads to the result that the peer effect of pure friends is stronger than that of Simmelian-tie friends. To further unravel the underlying mechanism, we explore the influence of heterogeneity of friends across the population. In online social gaming, some users carefully select which players to make friends with, while others select friends more casually. As a result, the latter ones tend to have more friends and in turn a higher probability of having Simmelian-tie friends. To investigate this possibility, we divide the population into two subsamples based on the friend degree on the last day of our study period. If a player’s friend degree is smaller than the mean degree, she is classified into the low friend degree group; otherwise, she is classified into the high friend degree group. We run our model again for these 2 groups, respectively, and the results are reported in Table 6.

Table 4. Two-step Tobit Regression with Fixed Effect

<table><tr><td>DailyEco</td><td>Coefficients(Std. Err.)</td></tr><tr><td>PFriend</td><td>3.138(0.0843)***</td></tr><tr><td>SFriend</td><td>1.309(0.0844)***</td></tr><tr><td>Lag.DailyEco</td><td>-0.412(0.0096)***</td></tr><tr><td>Lag.CumuEco</td><td>0.092(0.0294)***</td></tr><tr><td>EarnedVirMoney</td><td>-0.096(0.0122)***</td></tr><tr><td>Online</td><td>-0.370(0.0316)***</td></tr><tr><td>Level</td><td>0.221(0.0205)***</td></tr><tr><td>PFDegree</td><td>-0.271(0.0085)***</td></tr><tr><td>SFDegree</td><td>-0.064(0.0088)***</td></tr><tr><td> $u_{pfriend}$ </td><td>-3.143(0.0842)***</td></tr><tr><td> $u_{sfriend}$ </td><td>-1.310(0.0845)***</td></tr><tr><td>Inv. Mills ratio 1</td><td>-2.649(0.1707)***</td></tr><tr><td>Inv. Mills ratio 2</td><td>0.851(0.4311)**</td></tr><tr><td>Inv. Mills ratio 3</td><td>2.191(0.2965)***</td></tr><tr><td>N</td><td>9112</td></tr><tr><td>AIC</td><td>35815.153</td></tr><tr><td>BIC</td><td>35921.913</td></tr><tr><td>F</td><td>459.228</td></tr></table>

\*\*\* $\mathsf { p } < 0 . 0 1$ . \*\* p < 0.05. \* p < 0.1. Standard errors are reported in parentheses.

Table 5. Panel VAR Results

<table><tr><td colspan="2">DailyEco</td></tr><tr><td>Lag.DailyEco</td><td>0.161(0.0072)***</td></tr><tr><td>Lag.Degree</td><td>-0.086(0.0093)***</td></tr><tr><td colspan="2">Degree</td></tr><tr><td>Lag.DailyEco</td><td>0.011(0.0530)</td></tr><tr><td>Lag.Degree</td><td>0.927(0.0790)***</td></tr><tr><td>Obs.</td><td>430,194</td></tr><tr><td colspan="2">*** p &lt; 0.01. ** p &lt; 0.05. * p &lt; 0.1. Robust standard errors are reported in parentheses.</td></tr></table>

According to the results, both H1 and H2b are still supported, as shown by the positive and significant coefficients for both social influence variables (PFriends and SFriend). We also perform the Wald test to compare the two groups, as shown in Table 7. Although the results are largely consistent with our main results in Table 3, there are some new findings.

The difference between the peer effect of pure friends and Simmelian-tie friends in the high degree group becomes much larger: 3.446 (3.322/0.964) in the high degree group versus 1.485 (0.674/0.454) in the low degree group and 2.674 (2.294/ 0.858) overall. Figure 4 depicts the influence power of all the three types of social influences. The results indicate that players with a higher friend degree tend to pay more attention to their pure friends than they do to their Simmelian-tie friends, and this difference is less pronounced for players with low friend degree. This new finding provides further evidence to support our conjecture that players with a larger number of friends are less worried about being ostracized and thus are less subject to the influence of Simmelian-tie friends.

Table 6. Results for Low and High Friend Degree Players

<table><tr><td></td><td>(1)</td><td>(2)</td></tr><tr><td>DailyEco</td><td>Low friend degree</td><td>High friend degree</td></tr><tr><td>PFriend</td><td>0.678(0.0913)***</td><td>3.322(0.211)***</td></tr><tr><td>SFriend</td><td>0.454(0.0800)***</td><td>0.964(0.150)***</td></tr><tr><td>Lag.DailyEco</td><td>0.0650(0.0213)***</td><td>0.0267(0.0162)*</td></tr><tr><td>Lag.CumuEco</td><td>-0.164(0.0230)***</td><td>0.123(0.0218)***</td></tr><tr><td>EarnedVirMoney</td><td>-0.0256(0.0207)</td><td>-0.0798(0.0247)***</td></tr><tr><td>Online</td><td>0.0459(0.0201)**</td><td>-0.181(0.0435)***</td></tr><tr><td>Level</td><td>0.0636(0.0211)***</td><td>0.169(0.0275)***</td></tr><tr><td>PFDegree</td><td>-0.126(0.0172)***</td><td>-0.277(0.0187)***</td></tr><tr><td>SFDegree</td><td>-0.0888(0.0190)***</td><td>-0.0299(0.0147)**</td></tr><tr><td>Inv. Mills ratio 1</td><td>-0.497(0.134)***</td><td>-1.891(0.208)***</td></tr><tr><td>Inv. Mills ratio 2</td><td>0.763(0.310)**</td><td>1.043(0.532)*</td></tr><tr><td>Inv. Mills ratio 3</td><td>0.492(0.175)***</td><td>1.959(0.352)***</td></tr><tr><td>N</td><td>15,945</td><td>73,468</td></tr><tr><td>AIC</td><td>72,668.2</td><td>511,434.0</td></tr><tr><td>BIC</td><td>72,760.3</td><td>511,544.5</td></tr><tr><td>F</td><td>25.23</td><td>47.20</td></tr></table>

\*\*\* p < 0.01. \*\* p < 0.05. \* p < 0.1. Robust standard errors are reported in parentheses.

Table 7. Wald Tests for Two-group Comparison

<table><tr><td></td><td>Wald tests</td></tr><tr><td>Low group</td><td>3.405***</td></tr><tr><td>High group</td><td>82.962***</td></tr><tr><td colspan="2">*** p &lt; 0.01. ** p &lt; 0.05. * p &lt; 0.1.</td></tr></table>

## Nature of Influence Power

Interaction between actors is essential for social influence to occur; e.g., influence occurs when talking with each other, working in the same room, or living nearby. Hence, one possible explanation of why the influence power of Simmelian-tie friends is smaller than what has been suggested by the literature may be due to the reduced physical interaction between friends in a virtual gaming world. We further perform an analysis on the interaction intensity between friends to investigate this. Although we do not directly observe the data on interactions, we are able to infer it from how much time two players are both playing the game at the same time by examining their login and logout time logs. Time played together serves as a good necessary proxy of interactions, since any kinds of interactions in the game must meet the precondition that they both are playing the game at the same time.

We only investigate the change of co-playing time before and after Simmelian ties are established. Figure 5 illustrates an example of Simmelian-tie establishment. In this triad, the solid lines represent existing connections, while the dashed line denotes the connection to be established. We explore how co-playing time between A and B will change with the emergence of the A-C connection.

![](/api/attachments/NN2HWKWC/fulltext/images/8deb5ba9bfa9af040ebdc77169374084b27d9e44d1cb525fb434beb211417a3c.jpg)  
Figure 4. Influence power across groups

The analysis is performed at the dyad-day level. To eliminate the influence of play time variance, we calculate the ratio of co-play time as the dependent variable:

$$
\text { coplay\_raio } _ {i, j, t} = \left. \text { coplay\_time } _ {i, j, t} \right| _ {\text { online } _ {i, t}}
$$

where i indexes player i (A in the example), j is player j, coplay time<sub>i;j;t</sub> means total time that both i and j are online at day t. The model is:

$$
c o p l a y \_ r a i o _ {i, j, t} = \alpha_ {i} + \beta_ {1} T r i a d _ {i, j, t} + \beta_ {2} F D a y s _ {i, j, k, t} + \beta_ {3} F D a y s _ {i, j, k, t} ^ {2} + \varepsilon_ {i, t}\tag{7}
$$

where Triad indicates whether the triad has been formed (0 for not formed, 1 for formed); FDays measures days elapsed since the connection A-B and B-C were established. FDays is included since individuals tend to favor new friends more than old friends [58]. Individual fixed effects are also incorporated into this analysis, with robust standard errors factored in, as reported in Table 8.

According to the table, the co-playing time ratio between A and B significantly drops when the connection between A and C is established (coef. = −0.001, p-value < 0.01). This indicates that players are more willing to interact with their new friends but not with the extant friends to maintain the connection. Therefore, the establishment of Simmelian-ties tends to reduce the interaction between players, and as a result, the influence power of these ties decreases in tandem.

## Conclusion and Discussion

It is of central interest to any gaming company to enhance the monetary value of a player. Our study addresses the critical monetization problem in freemium social games from the social influence perspective. Our analysis based on a big social gaming dataset yields two sets of key findings. First, cohesion is a critical network force driving players to pay. We found that players with more paying pure-friends or Simmelian-tie friends tend to pay more. Second, peer effect of pure friends is much stronger than that of Simmelian-tie friends. However, when a player only has a small number of friends, the peer effect of Simmelian-tie friends turns close to that of pure friends.

![](/api/attachments/NN2HWKWC/fulltext/images/740d67198f3690ef77204679c5966f6f49102ce9c4f394dfef81803d006297ce.jpg)  
Figure 5. An example of Simmelian ties establishment

Table 8. Change of Co-playing Time Ratio

<table><tr><td>Coplay_ratio</td><td>Coefficients(Std. Err.)</td></tr><tr><td>Triad</td><td>-0.001(0.0002)***</td></tr><tr><td>FDays</td><td>-0.001(0.0000)***</td></tr><tr><td> $FDays^2$ </td><td>0.000(0.0000)***</td></tr><tr><td>Lag. Coplay_ratio</td><td>0.705(0.0029)***</td></tr><tr><td>Constant</td><td>0.105(0.0010)***</td></tr><tr><td>N</td><td>1,563,870</td></tr><tr><td>AIC</td><td>-6.80e+06</td></tr><tr><td>BIC</td><td>-6.80e+06</td></tr><tr><td>F</td><td>22,706.788</td></tr><tr><td colspan="2">*** p &lt; 0.01. ** p &lt; 0.05. * p &lt; 0.1. Robust standard errors are reported in parentheses.</td></tr></table>

Our results yield direct implications for the gaming company. This study provides guidance to gaming companies on smart social game design, for example, designing a personalized game experience for individual players. A social game named Jianghu (released in May 2014) started to personalize missions for each individual player and recommend friends to a player by analyzing his own experiences and behaviors [47]. For example, when a new player starts to play the game, she typically would seek some senior players to be her friends (or tutors) to help play the game. This is a golden time for the company to recommend other players to her. Currently the company mainly recommends candidate friends based on players’ skills, experience and gaming behaviors. Our results suggest that under the goal of monetizing players, the company should also consider players’ payment history in recommending friends and also pay attention to whether the candidate friend already shared common friends with the focal player, in a Simmelian-tie sense.

Surprisingly, our comparative results between the pure friends and Simmelian-ties suggest that the company should place a higher value on a player’s pure friends. This is contrary to the common findings in the literature, which suggests a stronger effect of Simmelian-tie friends. Our analyses demonstrate that it is likely caused by the reduction of co-play time after being Simmelian ties. The social gaming company could use this information to design a better marketing strategy. For instance, in a push promotion campaign, the company should push more aggressively the information of a player’s pure friends, provided they are payers already. Conversely, the company should be careful in recommending players to be friends to prevent players forming Simmelian ties.

In addition, our results on the heterogeneity of low friend degree players and high friend degree players suggest that the company should differentiate between these 2 types of players. The company should push consumption information of both the Simmelian-tie friends and pure friends only to the low friend degree players, while pushing pure friends’ information more to the high friend degree players.

More broadly, there are also implications for policy makers in a virtual economy. User engagement is the most crucial consideration in a virtual economy, while payment is one of the most important types of user engagement. According to our results, the virtual economy could utilize the social network of users to better engage users. However, a dense (highly connected network) may not always be good. Our results show that having too many friends may curb users’ engagement, especially with regard to willingness to pay. Therefore, gaming platforms should be careful in stipulating gaming policies on social networking. They may need to limit the number of friends for each user when the friend network is too dense, and when possible, limit the chance for players to have Simmelian ties.

The increasingly popular freemium and gamification business models can also benefit from this research. It is customary for social games to provide free and premium gaming features. How many free features to include so as to entice customers to pay for premium features is the key success factor for a freemium business model [45]. Our findings suggest that friends’ adoption of advanced features would increase the focal user’s likelihood to pay, consistent with the literature [8]. Gamification refers to the use of game thinking and game mechanisms in a non-game context to engage users into solving problems, such as designing the Windows Phone 7 operating system at Microsoft [59]. Our results suggest that pure friends exert the most influence in the context of online gaming. This informs a gamification designer to whom to reach out to incentivize players.

## Funding

The authors acknowledge support from the National Natural Science Foundation of China (Grant No. 71701177, 71850013, 71490724, 71532004, 91746103, and 71572166).

## NOTES

1 http://ng.d.cn/qqyujiantianya/news/detail\_328803\_1.html

2 We show how this pans out in our context using a dyad level analysis in Empirical Analysis Nature of Influence Power section.

3 We also tried 2-period lag and the results qualitatively do not change.

## REFERENCE

1. Ahn, L.V. Games with a purpose. Computer, 39, 6 (2006), 92–94.

2. Ali, M.M.; and Dwyer, D.S. Social network effects in alcohol consumption among adolescents. Addictive Behaviors, 35, 4 (2010), 337–342.

3. Anderson, C. Free: The Future of a Radical Price. Hypersion,Connecticut, 2009.

4. Angrist, J.D.; and Pischke, J.-S. Mostly Harmless Econometrics: An Empiricist’s Companion. Princeton University Press,New Jersey, 2009.

5. Bala, V.; and Goyal, S. Learning from neighbours. Review of Economic Studies, 65 (1998), 595–621.

6. Baltagi, B.H.; Bresson, G.; and Pirotte, A. Joint LM test for homoskedasticity in a one-way error component model. Journal of Econometrics, 134, 2 (2006), 401–417.

7. Bapna, R.; Gupta, A.; Rice, S.; and Sundararajan, A. Trust and the strength of ties in online social networks: An exploratory field experiment. MIS Quarterly, 41, 1 (2017), 115–130.

8. Bapna, R.; and Umyarov, A. Do Your online friends make you pay? A randomized field Experiment On Peer Influence In Online Social Networks. Management Science, 61, 8 (2015), 1902-1920.

9. Bond, R.M.; Fariss, C.J.; Jones, J.J.; Kramer, A.D.; Marlow, C.; Settle, J.E.; and Fowler, J.H. A 61-million-person Experiment in Social Influence and Political Mobilization. Nature, 489, 7415 (2012), 295–298.

10. Bramoullé, Y.; Djebbari, H.; and Fortin, B. Identification of peer effects through social networks. Journal of Econometrics, 150, 1 (2009), 41–55.

11. Burkhardt, M.E. Social interation effects following a technological change: A longitudinal investigation. Academy of Management Journal, 37, 4 (1994), 869–898.

12. Burt, R.S. Social contagion and innovation: Cohesion versus structural equivalence. American Journal of Sociology, 92, 6 (1987), 1287–1335.

13. Burt, R.S. Structural Holes: The Social Structure of Competition. Cambridge, MA: Harvard University Press, 1992.

14. Chanye. Companies could Develop Subscription-based Games and Freemium Games in the Same Time. Chanye.18183.com, 2014.

15. Cooper, S.; Khatib, F.; Treuille, A.; Barbero, J.; Lee, J.; Beenen, M.; Leaver-Fay, A.; Baker, D.; Popovic, Z.; and Players, F. Predicting protein structures with a multiplayer online game. Nature, 466, 7307 (2010), 756–760.

16. Cowley, R. Honor of Kings was the top grossing mobile game worldwide in June 2017. PocketGamer, 2017. http://www.pocketgamer.biz/news/66265/superdata-researchworldwide-grossing-ranks-june-2017/

17. Curtis, T. Most New Social Game Players Quit after just One Day. GAMASUTRA, 2012. http://www.gamasutra.com/view/news/179704/Most\_new\_social\_game\_players\_quit\_after\_ just\_one\_day.php#.UICEQml26Rm

18. Dong, M.C.; Liu, Z.; Yu, Y.; and Zheng, J.-H. Opportunism in distribution networks: The role of network embeddedness and dependence. Production and Operations Management, 24, 10 (2015), 1657-1670.

19. Doreian, P. Two regimes of network autocorrelation. In, Kochen, M., (ed.), The Small World. Norwood, NJ: Ablex, 1989, pp. 280–295.

20. Egebark, J.; and Ekström, M. Like what you like or like what others like? Conformity and peer effects on Facebook. Working Paper, Research Institute of Industrial Economics, Stockholm, 2011, pp. 1–26.

21. Ehrhardt, G.; Marsili, M.; and Vega-Redondo, F. Diffusion and growth in an evolving network. International Journal of Game Theory, 34, 3 (2006), 383–397.

22. Ennett, S.T.; and Bauman, K.E. The contribution of influence and selection to adolescent peer group homogeneity: The case of adolescent cigarette smoking. Journal of Personality and Social Psychology, 67, 4 (1994), 653–663.

23. Freeman, L.C. Centrality in social networks: Conceptual clarification. Social Networks, 1, 3 (1979), 215–239.

24. Gaba, V.; and Dokko, G. Learning to let go: Social influence, learning, and the abandonment of corporate venture capital practices. Strategic Management Journal, 37, 8 (2016), 1558–1577.

25. GameBus. Monthly Revenue of Mobile Games in China. QQ Games, 2013.

26. Geng, R.; Chen, X.; Zhang, B.; Cai, S.; and Zhang; C. Social contagion and diffusion: Modeling the direct and indirect peer influences on repeat-purchase in online freemium games. Pacific Asia Conference on Information Systems, Singapore, 2015, pp. 224.

27. Goldenberg, J.; Han, S.; Lehmann, D.R.; and Hong, J.W. The role of hubs in the adoption process. Journal of Marketing, 73, March (2009), 1–13.

28. Hansen, L.P. Large sample properties of generalized method of moments estimators. Econometrica, 50, 4 (1982), 1029–1054.

29. Haythornthwaite, C. Social network analysis: An approach and technique for the study of information exchange. Library & Information Science Research, 18, 323–342 (1996).

30. Jayaraj, S.; Doerfel, M.L.; and Williams, T. Clique to win? Impact of Simmelian ties on collaborative project performance. Academy of Management Proceedings, 2017, pp. 14525.

31. Kaustia, M.; and Rantala, V. Social learning and corporate peer effects. Journal of Financial Economics, 117, 3 (2015), 653–669.

32. Krackhardt, D. The ties that torture: Simmelian tie analysis in organizations. Research in the Sociology of Organizations, 16(1999), 183–210.

33. Krackhardt, D.; and Kilduff, M. Structure, culture and Simmelian ties in entrepreneurial firms. Social Networks, 24(2002), 279–290.

34. Kyriazidou, E. Estimation of a panel data sample selection model. Econometrica, 65, 6 (1997), 1335–1364.

35. Lee, A. Here’s Why Tencent’s Honour of Kings has 200 Million Players. SouthChinaMorningPost, 2017.

36. Liu, D.; Santhanam, R.; and Webster, J. Toward meaningful engagement: A framework for design and research of gamified information systems. MIS Quarterly, 41, 4 (2017), 1011–1034.

37. Lopez, J. Microsoft Unveils Ribbon Hero 2.0. Gamification, 2011. http://www.gamifi cation.co/2011/04/26/microsoft-ribbon/

38. Lu, F.; and Anderson, M.L. Peer effects in microenvironments: The benefits of homogeneous classroom groups. Journal of Labor Economics, 33, 1 (2015), 91–122.

39. Ma, X.; Khansa, L.; Deng, Y.; and Kim, S.S. Impact of prior reviews on the subsequent review process in reputation systems. Journal of Management Information Systems, 30, 3 (2013), 279–310.

40. Mangleburg, T.F.; Doney, P.M.; and Bristol, T. Shopping with friends and teens susceptibility to peer influence. Journal of Retailing, 80, 2 (2004), 101–116.

41. Manski, C.F. Identification of endogenous social effects: The reflection problem. Review of Economic Studies, 60(1993), 531–542.

42. McDonald, E. Global Games Market Report. Newzoo, 2017. https://newzoo.com solutions/standard/market-forecasts/global-games-market-report/

43. Moschis, G.P.; and Moore, R.L. Decision making among the young: A socialization perspective. Journal of Consumer Research, 6, 2 (1979), 101–112.

44. Moyen, M. Tencent’s “Honor of Kings” will cannibalize international sales of “League of Legends.” Seeking Alpha, 2017. https://seekingalpha.com/article/4102304-tencentshonor-kings-will-cannibalize-international-sales-league-legend

45. Niculescu, M.F.; and Wu, D.J. Economics of free under perpetual licensing: Implications for the software industry. Information Systems Research, 25, 1 (2014), 173–199.

46. Oestreicher-Singer, G.; and Sundararajan, A. The visible hand? Demand effects of recommendation networks in electronic markets. Management Science, 58, 11 (2012), 1963-1981.

47. PCgames. Eight Smart Functions: The Jianghu. In, Yangdenghua, (ed.): PC Games, 2014. http://wangyou.pcgames.com.cn/386/3865073\_all.html

48. Peng, J.; Agarwal, A.; Hosanagar, K.; and Iyengar, R. Network overlap and content sharing on social media platforms. Journal of Marketing Research, 55, 4 (2018), 571–585.

49. Semykina, A.; and Wooldridge, J.M. Estimating panel data models in the presence of endogeneity and selection. Journal of Econometrics, 157, 2 (2010), 375–380.

50. Shein, E. Game over for Gamification?: CMO, 2012. http://www.cmo.com/features/ articles/2012/10/24/game-over-for-gamification.html#gs.7PrOOWg

51. Shi, S.W.; Xia, M.; and Huang, Y. From minnows to whales: An empirical study of purchase behavior in freemium social games. International Journal of Electronic Commerce, 20, 2 (2015), 177–207.

52. Shriver, S.K.; Nair, H.S.; and Hofstetter, R. Social ties and user-generated content: Evidence from an online social network. Management Science, 59, 6 (2013), 1425–1443.

53. Smith, S.; Windmeijer, F.; and Wright, E. Peer effects in charitable giving: evidence from the (running) field. The Economic Journal, 125, June (2013), 1053–1071.

54. Sridhar, S.; and Srinivasan, R. Social influence effects in online product ratings. Journal of Marketing, 76, September (2012), 70–88.

55. Sujka, S. Top 10 Secrets of Success for Social Games – by GameDuell Co-Founder Michael Kalkowski. Social Games Observer, 2011. http://www.socialgamesobserver.com/ top-10-success-social-games-5400

56. Tencent. RoyalSword Achieved 5 Million Monthly Active Players. Tencent Tech, 2011. http://tech.qq.com/a/20111029/000106.html

57. Ugander, J.; Backstrom, L.; Marlow, C.; and Kleinberg, J. Structural diversity in social contagion. Proceedings of the National Academy of Sciences, 109, 16 (2012), 5962–5966.

58. Wang, C.A.; Zhang, X.M.; and Hann, I.-H. Socially Nudged: A quasi-experimental study of friends’ social influence in online product ratings. Information Systems Research, 29, 3 (2018), 525–777.

59. Wikipedia. Gamification. Wikipedia, 2014. http://en.wikipedia.org/wiki/Gamification 60. Wood, L. Global Online Gaming Market 2014. Research and Markets, 2014. http:// www.prnewswire.com/news-releases/global-online-gaming-market-2014-247149631.html

61. Wooldridge, J.M. Introductory Econometrics: A Modern Approach. Canada: South-Western Cengage Learning, 2006.

62. Yakuel, P. Online Casinos vs. Social Casino Games. Optimove Blog, 2013. http:// www.optimove.com/blog/online-casinos-vs-social-casino-games

63. Zhang, C.; Phang, C.W.; Wu, Q.; and Luo, X. Nonlinear effects of social connections and interactions on individual goal attainment and spending: Evidences from online gaming markets. Journal of Marketing, 81, 6 (2017), 132–155.

64. Zimmerman, D.J. Peer effects in academic outcomes: Evidence from a natural experiment. The Review of Economics and Statistics, 85, 1 (2003), 9–23.
