---
otero_id: 28191
otero_key: "PPQBVQQB"
title: "Platform Competition Under Network Effects: Piggybacking and Optimal Subsidization"
authors: "Yifan Dou; D. J. Wu"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Note

# Platform Competition Under Network Effects: Piggybacking and Optimal Subsidization

Yifan Dou,<sup>a,</sup>\* D. J. Wu<sup>b</sup>

<sup>a</sup> School of Management, Fudan University, Shanghai 200433, China; <sup>b</sup> Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308

\*Corresponding author

Contact: yfdou@fudan.edu.cn, https://orcid.org/0000-0002-0516-3250 (YD); dj.wu@scheller.gatech.edu, https://orcid.org/0000-0002-7991-1127 (DJW)

Received:

Revised: March

Accepted:

Published Online in Articles in Advance: August 2, 2021

https://doi.org/10.1287/isre.2021.1017

Copyright:

Abstract. A repeated challenge in launching a two-sided market platform is how to ignite the cross-side network effects to jump-start adoption. Prior literature often addresses this issue by using pricing controls—a high price on one side to raise the margin and a low price on the other to attract users—or the “seesaw principle.” More recently, platforms are increasingly embracing nonpricing controls to accelerate user adoptions. Little is known, however, about the role of nonpricing controls and their interplay with pricing controls. In this research note, using a game-theoretic framework, we study “piggybacking”—that is, expanding the focal market to recruit exclusive users from external networks—as a new and nonpricing control to launch platforms in conjunction with pricing controls. We <sup>fi</sup>rst consider consumer-side piggybacking. In a standard “competitive bottlenecks” setting in which consumers single home and providers multihome, we provide a rich set of novel insights into strategies that platforms use to monetize exclusive access to external users with nontrivial characterizations of the interplay among piggybacking, cross-side network effects, and price competition. We identify necessary and suf<sup>fi</sup>cient conditions when piggybacking is pro<sup>fi</sup>t improving and when it leads to a prisoner’s dilemma, depending on the piggybacking cost and strengths of cross-side network effects. Among others, we show that, if the platforms’ equilibrium strategies were to subsidize consumers (when providerside network effects are stronger than consumer-side network effects), piggybacking may intensify rather than ease price competition. In contrast, if the platforms’ equilibrium strategies were to subsidize providers (when provider-side network effects are weaker than consumerside network effects), piggybacking may ease price competition. Interestingly, piggybacking reinforces the seesaw principle for the piggybacking platform. We provide a full characterization on such nontrivial equilibrium outcomes. We then consider provider-side piggybacking, and we show that the insights are qualitatively the same as consumer-side piggybacking except that the prisoner’s dilemma disappears if piggybacking providers multihome. Managerial implications for platform practitioners are also discussed.

History: Ravi Bapna, Senior Editor; Jianqing Chen, Associate Editor.

Funding: Yifan Dou acknowledges <sup>fi</sup>nancial support from the National Natural Science Foundation of China (NSFC) [Grants 71672042 and 71822201].

Keywords: analytical modeling economics of IS network effects piggybacking platform competition pricing subsidization

## 1. Introduction

As an increasing number of businesses (both physical and digital) search for multisided platform business models (i.e., intermediaries that connect two or more distinct groups of users and enable their direct interactions), the <sup>fi</sup>rst challenge is to determine the best way to expand the user base in view of the interdependence issue among different user groups. An optimal solution structure frequently reported in the two-sided platform literature is subsidizing one side and charging the other side to jump-start the platform’s adoption (e.g., Rochet and Tirole 2003, Parker and Van Alstyne 2005, Eisenmann et al. 2006, Bolt and Tieman 2008). This optimal structure has been generalized as the seesaw principle, which is characterized by charging a high price on one side to increase margins and a low price on the other side to attract users (Rochet and Tirole 2006). Subsidizing strategies are widely used in launching practical platforms. For example, Microsoft incurred a total loss of more than US\$4 billion in the <sup>fi</sup>rst four years after launching its Xbox gaming platform, primarily by allowing consumers to pay a market price below the manufacturing cost.<sup>1</sup>

In addition to using pricing controls, such as subsidies, platforms are increasingly embracing nonpricing controls to incentivize user adoptions. Examples include (a) offering <sup>fi</sup>rst-party contents to attract early adoptions (e.g., Hagiu and Spulber 2013), (b) building the market momentum (e.g., Gawer and Cusumano 2008), (c) adding initial developers to the software platform (e.g., Boudreau 2010), (d) attracting early users via single-sided features (e.g., Hagiu and Eisenmann 2007), and (e) integrating the user base with a complementary platform (e.g., Li and Agarwal 2016). We contribute to this literature by examining a new and nonpricing control that imports exclusive external user traf<sup>fi</sup>c. More speci<sup>fi</sup>cally, we analyze user traf<sup>fi</sup>c management in general and piggybacking (Parker et al. 2016) in particular. By reexamining a platform’s pricing/subsidizing decisions, we reveal a host of new insights into strategies that platforms use to monetize exclusive access to external users with more complex characterizations of the interplay among traf<sup>fi</sup>c management, cross-side network effects, and platform price competition.

In alignment with the literature, we de<sup>fi</sup>ne “piggybacking” as the ability of a platform to “connect with an existing user base from a different platform and stage the creation of value units to recruit those users to participate” (Parker et al. 2016, p. 91). A key piggybacking characterization that we focus on in this paper is the noncompetitive and exclusive access to external users. One example of platform piggybacking is the mobile payment platform war that took place in China in 2014. During the week of the Chinese lunar new year, Tencent’s WeChat Pay successfully acquired eight million new users by piggybacking on WeChat’s social media platform. The surge of WeChat Pay users was driven mostly by the “red envelope” feature released before New Year’s Eve. In China, a red envelope traditionally contains cash as a gift from elders or employers to children or employees, respectively, as a part of the New Year’s celebration. WeChat Pay migrated this idea to the mobile context by allowing users to send digital cash to participants in the mobile group chats. Not surprisingly, senders and receivers of the digital cash must become WeChat Pay users in the <sup>fi</sup>rst place to access the red envelope feature. In response, the rival mobile payment platform, Alibaba’s Alipay Mobile, carried out a similar initiative to recruit new adopters through Alibaba’s e-commerce websites (Taobao.com and Tmall.com). Note that the sources of the imported users for both We-Chat Pay and Alipay Mobile are exclusive; that is, We-Chat’s social media and Alibaba’s e-commerce websites are not accessible to each other. Another frequently used approach to access an external and noncompetitive pool of potential users is to form an exclusive alliance or partnership. For example, to compete with Uber, car-hailing platforms, including

Didi (from China), Lyft (from the United States), Grab (from Southeast Asia), and Ola (from India), permitted their users to access each other’s network, which essentially resulted in an anti-Uber alliance (Bhuiyan 2016). Through this alliance, a U.S. traveler in China can order Didi’s services directly from the Lyft app (but not from the Uber app). In this way, these platforms piggyback on each other to obtain new users who are not accessible to Uber.

Many examples of piggybacking also exist among start-up platforms (Parker et al. 2016) that tap into external networks to import early traf<sup>fi</sup>c rather than using subsidies alone to build an installed base from scratch. One such example is how YouTube piggybacked on Myspace (Parker et al. 2016). When it was founded in 2005, YouTube provided the video embedding tool for Myspace, which was then the world’s largest social networking platform. During that time, Myspace users immediately and unwittingly became YouTube viewers after watching or uploading video clips through the video tool developed by YouTube. In this way, YouTube acquired massive viewer traf<sup>fi</sup>c, which, in turn, attracted more video contributors and eventually helped YouTube outgrow its then competitor, Vimeo. Until Myspace blocked YouTube’s tool in 2006, between 60% and 70% of YouTube traf<sup>fi</sup>c originated from Myspace.<sup>2</sup> Similarly, Airbnb is a documented user of piggybacking and has used this strategy to boost its growth with a “publish on Craigslist” button. By clicking on this button, Airbnb hosts can immediately cross-post their Airbnb listings to Craigslist, and any Craigslist user responding to that listing is required to use Airbnb to reach the host.<sup>3</sup> Parker et al. (2016) characterize piggybacking as one of several “pull” strategies in which consumers are pulled by platforms from an external network to the focal network. For example, in the Myspace example, users from Myspace network were pulled into the YouTube network when they watched or uploaded 4 videos on Myspace.

Motivated by the increasing popularity of piggybacking among platform practitioners, we study two fundamental research questions in this note: How does piggybacking affect the platforms’ optimal pricing/subsidization strategy and pro<sup>fi</sup>ts? When should platforms engage in piggybacking? Our analytical model provides a general framework for studying platform competition in the presence of piggybacking. To the best of our knowledge, this paper is among the <sup>fi</sup>rst to formally study how piggybacking as a novel nonpricing control affects pricing controls in platform competition.

We <sup>fi</sup>rst consider consumer-side piggybacking. In a standard “competitive bottlenecks” setting in which consumers single home and providers multihome, we provide a rich set of novel insights into strategies that platforms use to monetize exclusive access to external users with nontrivial characterizations of the interplay among piggybacking, cross-side network effects, and price competition. We identify necessary and suf<sup>fi</sup>- cient conditions when piggybacking is pro<sup>fi</sup>t improving and when it leads to a prisoner’s dilemma (PD), depending on the piggybacking cost and strengths of cross-side network effects. Among others, we show that, if the platforms’ equilibrium strategies were to subsidize consumers (when provider-side network effects are stronger than consumer-side network effects), piggybacking may intensify rather than ease price competition. In contrast, if the platforms’ equilibrium strategies were to subsidize providers (when provider-side network effects are weaker than consumer-side network effects), piggybacking may ease price competition. Interestingly, piggybacking reinforces the seesaw principle for the piggybacking platform. We provide a full characterization on such nontrivial equilibrium outcomes. We then consider provider-side piggybacking, and we show that the insights are qualitatively the same as consumer-side piggybacking except that the prisoner’s dilemma disappears if piggybacking providers multihome.

The remainder of this paper is organized as follows. Section 2 reviews the related literature. Section 3 introduces our model. Section 4 reports our results. Section 5 examines the case of provider-side piggybacking. Section 6 outlines the managerial implications and concludes this note.

## 2. Related Literature

Our research builds mostly on two research streams. The <sup>fi</sup>rst stream of relevant literature focuses on launching a two-sided platform using pricing controls. Subsidizing one side of the market and charging the other is often suggested as the optimal solution structure (e.g., Bhargava and Sundaresan 2004, Wright 2004, Parker and Van Alstyne 2005, Rochet and Tirole 2006, Hagiu and Eisenmann 2007, Bolt and Tieman 2008, Hagiu 2009). For example, Parker and Van Alstyne (2005) recommend giving away free access/ products either to providers or consumers, depending on the cross-side elasticities. Rochet and Tirole (2006) introduce the seesaw principle, according to which a platform charges a high price on one side and a low price on the other. Thus, the seesaw principle is more general and includes subsidizing (charging belowcost prices) one side of the platform as a special case. Although both Parker and Van Alstyne (2005) and Rochet and Tirole (2006) assume that users single home, the seesaw principle is also shown to be optimal when users multihome (i.e., they can join both platforms). It is also a standard setting in two-sided market literature to consider competitive bottlenecks because of its practical importance (e.g., Armstrong

2006, Rochet and Tirole 2006, Economides and Tåg 2012, Hagiu and Hałaburda 2014). In this standard setting, Armstrong (2006) shows that the platform has monopoly power in providing access to the singlehoming side for the multihoming side, which leads to a higher price on the multihoming side. Hagiu and Hałaburda (2014) consider different types of user expectations when users join a platform. They show that platforms might be better off when users are less informed and, therefore, form their expectations passively. Our note follows this rich literature and uses a model of competitive bottlenecks as our model setting. We formally study how the strategic use of piggybacking, as a novel nonpricing control, affects pricing/subsidization controls in platform competition under network effects.

The second stream of relevant but rare literature examines the role of nonprice factors in platform competition as summarized in the Introduction. Particularly relevant to our model is the literature on installed base, which is de<sup>fi</sup>ned as the existing buyers using the same product or a compatible technology (Katz and Shapiro 1992). Among others, the literature shows that the installed base can (a) tilt the price structure to the bene<sup>fi</sup>t of sellers (Rochet and Tirole 2003), (b) foster the <sup>fi</sup>rst-mover advantage (e.g., Lee and Mendelson 2007), (c) affect the platform preannouncing strategy (Chellappa and Mukherjee 2021), and (d) motivate technology merger and acquisition (Wang and Hui 2017). Our model builds on this literature but with important differences. We explicitly model both consumer- and provider-side market expansion via piggybacking in a setting of competitive bottlenecks, which is understudied in the platform competition literature. Another novelty of our model is that we consider piggybacking as an endogenous decision by the platform to recruit exclusive external users in order to expand the focal market,<sup>5</sup> which, as we show in Section 4, can result in either positive or negative outcomes for platforms. We identify necessary and suf<sup>fi</sup>- cient conditions when piggybacking is desirable and when it leads to the prisoner’s dilemma. Interestingly, note that platform envelopment (Eisenmann et al. 2011, Li and Agarwal 2016) is a special case of piggybacking in which platforms piggybacking on their own installed base when entering into new markets (Fang et al. 2019). In sum, we contribute to the platform competition literature by considering piggybacking as a strategic choice variable and examine its interplay with pricing controls.

## 3. Model Assumptions

Consider a duopoly between platforms A and B in a two-sided market connecting consumers (denoted by superscript c) and providers (denoted by superscript d). The consumers single home and the providers multihome $( \mathrm { i . e . , }$ competitive bottlenecks). Consumers consist of (a) those who are in the focal market (called “focal consumers”) and (b) those who are recruited from an external network as a result of piggybacking (called “piggybacking consumers”). We normalize the size of the mass of focal consumers as 1. Focal consumers are distributed along a Hotelling segment <sub>[</sub>0, 1<sub>]</sub> with density 1. We follow the literature (Armstrong 2006, Anderson et al. 2014, Hagiu and Hałaburda 2014) to assume that consumers are interested in joining at most one platform (i.e., consumers single home). Focal consumers located at $x \in [ 0 , 1 ]$ receive the following utility from adopting platforms A and B, respectively:

$$
\begin{array}{r} U _ {A} ^ {c} (x) = V - p _ {A} ^ {c} - t x + \beta N _ {A} ^ {d}, \\ U _ {B} ^ {c} (x) = V - p _ {B} ^ {c} - t (1 - x) + \beta N _ {B} ^ {d}, \end{array}\tag{1}
$$

where V represents the symmetric stand-alone value of adopting either platform A or B. Parameter $p _ { k } ^ { c }$ is the consumer-side fee to access platform $k \in \{ A , \dot { B } \} .$ respectively. The term tx $( t ( 1 - x ) )$ is the mis<sup>fi</sup>t cost for consumers at x to adopt platform A (B). The coef<sup>fi</sup>- cient t measures the degree of mis<sup>fi</sup>t between the platform and the consumers. Prior platform literature also interprets t as the “degree of differentiation” or “market power,” which describes the competitiveness of the market $( \mathrm { e . g . }$ , Armstrong 2006, p. 673; Anderson et al. 2014, p. 160). All else being equal, a higher t indicates that it is more dif<sup>fi</sup>cult for platforms to attract focal consumers via low prices or subsidies. The coef<sup>fi</sup>cient $\beta \ge 0$ represents the degree of consumer-side network effects. Parameter $N _ { k } ^ { d }$ is the number of providers in equilibrium who participate in platform $k \in \{ A , B \}$

Given these utility functions, the number of focal consumers adopting platform $k , N _ { k } ^ { c } ,$ can be obtained by solving the indifferent customer type xˆ , which satis<sup>fi</sup>es $U _ { A } ^ { c } ( \bar { { \hat { x } } } ) = U _ { B } ^ { c } ( \hat { x } )$ .

$$
\begin{array}{r} N _ {A} ^ {c} = \hat {x} = \frac {1}{2} - \frac {p _ {A} ^ {c} - p _ {B} ^ {c}}{2 t} + \frac {\beta (N _ {A} ^ {d} - N _ {B} ^ {d})}{2 t}, \\ N _ {B} ^ {c} = 1 - \hat {x} = \frac {1}{2} - \frac {p _ {B} ^ {c} - p _ {A} ^ {c}}{2 t} + \frac {\beta (N _ {B} ^ {d} - N _ {A} ^ {d})}{2 t}. \end{array}\tag{2}
$$

To expand its focal market, we assume each platform can import n additional consumers from a noncompetitive and external network if it engages in piggybacking (Parker et al. 2016); otherwise, $n = 0$

We assume $n \leq 1 / 2$ such that the overall population of piggybacking consumers does not exceed those in the focal market. Intuitively, this upper bound ensures that the entire population of piggybacking consumers from both platforms does not exceed 1, which is the size of the mass of the focal consumers. In other words, the focal market would not become a niche after the piggybacking consumers are imported. This is also in line with the extension in Rochet and Tirole (2003), in which they assume a small mass of buyers who are loyal to their platform. We assume a <sup>fi</sup>xed (at n) piggybacking traf<sup>fi</sup>c volume and a one-time acquisition cost $c _ { k }$ for platform k. For example, YouTube invested in developing the video embedding tool for Myspace (similarly, WeChat Pay developed the red envelope function). To capture platforms’ decisions about piggybacking, we use the following indicator function <sup>I</sup> :

$$
\mathbb {I} _ {k} = \left\{ \begin{array}{l l} 1, & \text { if   Platform   k   chooses   piggybacking }, \\ 0, & \text { otherwise }. \end{array} \right.\tag{3}
$$

Providers multihome under the competitive bottlenecks setting. This gives rise to the following demand function in equilibrium as in Hagiu and Hałaburda (2014):

$$
N _ {k} ^ {d} = \alpha (\mathbb {I} _ {k} n + N _ {k} ^ {c}) - p _ {k} ^ {d},\tag{4}
$$

where $\alpha \geq 0$ represents the degree of provider-side network effects. Equation (4) suggests that adoptions on the provider side are driven purely by consumer adoptions because a platform has no stand-alone value for providers if it has no consumers. Following the literature (e.g., Parker and Van Alstyne 2005, Armstrong 2006, Hagiu and Hałaburda 2014), we assume $\alpha + \beta \leq 2 { \sqrt { t } }$ (equivalently, $\alpha \leq 2 \sqrt { t } - \beta )$ for the pro<sup>fi</sup>t function to be well behaved.<sup>6</sup>

The timeline of events has three stages, which are illustrated in Figure 1. In stage 0, platforms face the trade-offs between the costs and bene<sup>fi</sup>ts of piggybacking. In stage 1, two platforms simultaneously announce their prices on both sides, and in stage 2, focal consumers choose to join either platform A or B. Each provider decides whether to participate in platform A, B, or both.

## 4. Analysis and Findings

Section 4.1 investigates the subgame perfect pricing equilibrium in stage 1. We split our discussion into three different scenarios, respectively: (1) no piggybacking, (2) symmetric piggybacking, and (3) asymmetric piggybacking (in which only one platform engages in piggybacking). As we show later in Section 4.2, each of these scenarios can constitute a Nash equilibrium (NE).

## 4.1. Pricing Equilibrium in Stage 1

In stage 1, given the stage 0 decision <sup>I</sup> , platform k determines the optimal prices on both sides simultaneously to maximize its overall pro<sup>fi</sup>t $\Pi _ { k }$ from both sides. A platform remains in the market if and only if (iff) there are adopting consumers and providers from the focal market in equilibrium. In other words, an equilibrium exists iff $N _ { k } ^ { c } \ge 0$ and $N _ { k } ^ { d } \ge 0$ for $k \in \{ A , B \}$

Figure 1. Event Timeline  
![](/api/attachments/PPQBVQQB/fulltext/images/de2fa4f245cad19d6b2acd52595021694133035b16ef99f945585d5f71f897c1.jpg)

Speci<sup>fi</sup>cally, platform $k ^ { \prime } s$ pro<sup>fi</sup>t-maximization problem is the following:

$$
\max _ {p _ {k} ^ {c}, p _ {k} ^ {d}} \Pi_ {k} = p _ {k} ^ {c} \big (\mathbb {I} _ {k} n + N _ {k} ^ {c} \big) + p _ {k} ^ {d} N _ {k} ^ {d} - \mathbb {I} _ {k} c _ {k},
$$

subject to $N _ { k } ^ { c } = \frac { 1 } { 2 } - \frac { p _ { k } ^ { c } - p _ { - k } ^ { c } } { 2 t } + \frac { \beta ( N _ { k } ^ { d } - N _ { - k } ^ { d } ) } { 2 t } ,$

$$
\begin{array}{r l} & N _ {- k} ^ {c} = \frac {1}{2} - \frac {p _ {- k} ^ {c} - p _ {k} ^ {c}}{2 t} + \frac {\beta (N _ {- k} ^ {d} - N _ {k} ^ {d})}{2 t}, \\ & N _ {k} ^ {d} = \alpha (N _ {k} ^ {c} + \mathbb {I} _ {k} n) - p _ {k} ^ {d}, \\ & N _ {- k} ^ {d} = \alpha (N _ {- k} ^ {c} + \mathbb {I} _ {- k} n) - p _ {- k} ^ {d}, \\ & N _ {k} ^ {c} \geq 0, N _ {k} ^ {d} \geq 0, \quad \alpha + \beta \leq 2 \sqrt {t}, \text {and} n \leq \frac {1}{2}. \end{array}\tag{5}
$$

The subscript –k represents the opponent’s platform for platform k. We summarize our key notation in Table 1.

4.1.1. No Piggybacking $( \mathbb { I } _ { A } = \mathbf { 0 } , \mathbb { I } _ { B } = \mathbf { 0 } )$ . We start with the benchmark case in which neither platform engages in piggybacking, that is, $\mathbb { I } _ { A } = \mathbb { I } _ { B } = 0$ . Lemma 1 replicates the prior literature with a similar setup in which piggybacking is not considered $( \mathrm { e . g . } ,$ , proposition 2 in Armstrong 2006, lemma 2 in Anderson et al. 2014, and section 4.1 in Hagiu and Hałaburda 2014). All proofs are available in the appendix.

Lemma 1. $T _ { 1 } = { \alpha } ( \alpha + 3 \beta ) / 4$ and $T _ { 2 } = ( \alpha ^ { 2 } + 6 \alpha \beta +$ $\beta ^ { 2 } ) / 4$ . When neither platform engages in piggybacking $( i . e . , \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 0 )$ , the equilibrium prices and profits are given by

$$
(p _ {A} ^ {c}) ^ {*} = (p _ {B} ^ {c}) ^ {*} = t - T _ {1}, (p _ {A} ^ {d}) ^ {*} = (p _ {B} ^ {d}) ^ {*} = \frac {\alpha - \beta}{4},
$$

$$
\left(\Pi_ {A}\right) ^ {*} = \left(\Pi_ {B}\right) ^ {*} = \frac {t}{2} - \frac {T _ {2}}{4}.
$$

The equilibrium market sizes are $\left( N _ { k } ^ { c } \right) ^ { * } = 1 / 2$ and $( N _ { k } ^ { d } ) ^ { * } = ( \stackrel { \cdot } { \alpha } + \beta ) / 4$

Corollary 1 follows immediately from Lemma 1.

Corollary 1. The necessary and sufficient conditions of platform subsidizing are

a. When $\beta \leq { \sqrt { t } } ,$ , there are three subcases:

1. For $\alpha \in [ 0 , \underline { { \alpha } } ( \beta ) )$ , subsidizing providers is optimal $( i . e . , ( p _ { k } ^ { d } ) ^ { * } < 0 ) .$

2. For $\alpha \doteq [ \underline { { \alpha } } ( \beta ) , \bar { \alpha } ( \beta ) ] .$ , subsidizing is suboptimal $( i . e . , ( p _ { k } ^ { c } ) ^ { * } \ge 0 , ( p _ { k } ^ { d } ) ^ { * } \ge 0 )$

3. For $\alpha > \bar { \alpha } ( \beta ) $ , subsidizing consumers is optimal ${ ( i . e . , ( p _ { k } ^ { c } ) } ^ { * } < 0 )$

b. When $\beta > { \sqrt { t } } ,$ for all feasible $\alpha ,$ subsidizing the provider is optimal (i.e., ${ ( p _ { k } ^ { d } ) } ^ { \ast } < 0 \}$ .

$$
H e r e, \underline {{\alpha}} (\beta) = \beta a n d \bar {\alpha} (\beta) = \left(\sqrt {1 6 t + 9 \beta^ {2} / 2} - 3 \beta\right) / 2.
$$

The key insights from Lemma 1 and Corollary 1 are the following. The conditions required for subsidizing to be optimal are driven by cross-side network effects. Given the consumer-side network effect $( \beta ) ,$ , subsidizing is optimal either when the provider-side network effect (α) is relatively small $( \mathrm { i . e . , }$ cases a.1 and b in Corollary 1) or relatively large $( \mathrm { i . e . , }$ case a.3 in Corollary 1). Otherwise, subsidizing is suboptimal (i.e., case a.2 in Corollary 1). Intuitively, in the former case, providers have relatively smaller incentives to participate; thus, attracting them with subsidies is necessary. In the latter case, the consumer side becomes overly competitive because of competitive bottlenecks, and subsidizing consumers is optimal because it incentivizes provider participation through crossside network effects. In general, Lemma 1 and Corollary 1 suggest that stronger network effects drive consumer-side prices $( \mathrm { i } . \mathrm { e } . , \bar { t } - T _ { 1 } )$ and platform pro<sup>fi</sup>ts (i.e., $t / 2 - T _ { 2 } / 4 )$ down, which serves as the starting point of our analysis of piggybacking.

4.1.2. Both Platforms Engage in Piggybacking $\mathbb { I } _ { A } = \mathbb { 1 } , \mathbb { I } _ { B } = \mathbb { 1 } )$ . When both platforms engage in $\mathrm { \ p i g g y - }$ backing, we show the equilibrium in Lemma 2.

Lemma 2. When both platforms engage in piggybacking $( i . e . , \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 )$ , the equilibrium prices are given by

$$
\begin{array}{c} (p _ {A} ^ {c}) ^ {*} = (p _ {B} ^ {c}) ^ {*} = (1 + 2 n) (t - T _ {1}), (p _ {A} ^ {d}) ^ {*} = (p _ {B} ^ {d}) ^ {*} \\ = \frac {(1 + 2 n) (\alpha - \beta)}{4}. \end{array}
$$

Table 1. Summary of Key Notation

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $k$ </td><td>Platform index,  $k \in \{A,B\}$ </td></tr><tr><td> $t$ </td><td>Misfit cost,  $t > 0$ </td></tr><tr><td> $\beta(\alpha)$ </td><td>Degree of the consumer-side (provider-side) network effects,  $\alpha + \beta \leq 2\sqrt{t}$ </td></tr><tr><td> $p_{k}^{c}(p_{k}^{d})$ </td><td>Equilibrium price of platform  $k$  on the consumer (provider) side</td></tr><tr><td> $N_{k}^{c}(N_{k}^{d})$ </td><td>Number of consumers (providers) who adopt platform  $k$ ,  $N_{k}^{c}$ ,  $N_{k}^{d} \geq 0$ </td></tr><tr><td> $\Pi_{k}$ </td><td>Equilibrium profit of platform  $k$ </td></tr><tr><td> $\mathbb{I}_{k}$ </td><td>Platform  $k$ &#x27;s decision on piggybacking,  $\mathbb{I}_{k} = 1$  if platform  $k$  chooses piggybacking</td></tr><tr><td> $\mathbb{I}_{k}n$ </td><td>Population of piggybacking consumers on platform  $k$ ,  $n \in [0,\frac{1}{2}]$ </td></tr><tr><td> $c_{k}$ </td><td>Piggybacking cost for platform  $k$ ,  $c_{k} \geq 0$ </td></tr></table>

The equilibrium profits are $\Pi _ { k } ^ { * } = ( 1 + 2 n ) ^ { 2 } ( t / 2 -$ $T _ { 2 } / 4 )  – c _ { k } ,$ , and the equilibrium market sizes are $\left( N _ { k } ^ { c } \right) ^ { * } = \frac { 1 } { 2 }$ and $( N _ { k } ^ { d } ) ^ { * } = ( 1 + 2 n ) ( \alpha + \beta ) / 4$

Comparing Lemmas 1 and 2 reveals the following insights about piggybacking, benchmarked with no piggybacking. First, piggybacking helps speed the virtuous cycle between two sides of the market, leading to greater market sizes and higher revenue. Second, given our modeling setup, both the price and subsidy are scaled up by a factor of $( 1 + 2 n )$ when platforms choose piggybacking, indicating that piggybacking may or may not ease price competition. Speci<sup>fi</sup>cally, piggybacking intensi<sup>fi</sup>es rather than eases consumer-side (provider-side) price competition if $t < T _ { 1 }$ (respectively, $\alpha < \beta )$ . Finally, piggybacking reinforces the seesaw principle $( \mathrm { i . e . , }$ the price gap between two sides increases, compared with the no-piggybacking case) because

$$
\begin{array}{c} | (p _ {k} ^ {d}) ^ {*} - (p _ {k} ^ {c}) ^ {*} | = (1 + 2 n) \bigg | \frac {\alpha - \beta}{4} - (t - T _ {1}) \bigg | \\ > \bigg | \frac {\alpha - \beta}{4} - (t - T _ {1}) \bigg |. \end{array}
$$

4.1.3. Asymmetric Piggybacking $( \mathbb { I } _ { A } = \mathbb { 1 } , \mathbb { I } _ { B } = \mathbf { 0 } )$ . Next, we examine asymmetric piggybacking, a condition in which only one platform chooses piggybacking. Asymmetric piggybacking is often seen when one of the competing platforms is endowed with exclusive access to the external pool of potential users. For example, in our motivating example of the anti-Uber alliance, Uber could not access the external pools as its competitors did in each local market, such as China. Other examples include one platform that engages in platform envelopment or forms an exclusive business alliance. Without loss of generality, we consider the case in which platform A engages in piggybacking.

Unlike the previous cases, under asymmetric piggybacking, platform B faces the threat of being pushed

Lemma 3. When only platform A engages in piggybacking and both platforms stay in the market in equilibrium, Table 2 summarizes the equilibrium pricing strategies, market sizes, and profits.

out of the market. As shown in the proof of Lemma $^ { 3 , }$ platform B stays in the market either when (a) $\alpha <$ $\sqrt { 4 t + 3 \beta ^ { 2 } - 2 \beta }$ or (b) $\alpha \geq \sqrt { 4 t + 3 \beta ^ { 2 } - 2 \beta }$ and $n < \bar { n } =$ $\dot { 1 / } [ 2 ( T _ { 3 } - t ) ] - 1$ in which $\dot { T } _ { 3 } = ( \alpha ^ { 2 } + 4 \alpha \beta + \beta ^ { 2 } ) / 4$ . The implications are twofold. First, platform $\mathrm { A } ^ { \prime } \mathrm { s }$ piggybacking traf<sup>fi</sup>c generates not only consumer-side prof-${ \mathrm { i t } } ,$ but also provider-side participation. Both forces collectively reinforce platform $\mathrm { A } \hat { \prime } _ { \mathrm { S } }$ overall advantages, which eventually pushes platform B out of the market. Second, the threshold n¯ is monotonically decreasing in the strength of network effects, indicating that forced exit becomes more likely in a market with stronger cross-side network effects, resulting in a “winner takes $\mathrm { a l l ^ { \prime \prime } }$ outcome. This <sup>fi</sup>nding formalizes the intuitions reported in prior platform competition literature (e.g., Eisenmann et al. 2006).

As shown in Table 2, the equilibrium results are nontrivial under asymmetric piggybacking. Speci<sup>fi</sup>- cally, piggybacking may either enlarge or shrink the scale of price or subsidy in a nontrivial way, depending on the strengths of the cross-side network effects. Corollary 2 summarizes how platform $\mathrm { A } ^ { \prime } \mathrm { s }$ piggybacking affects the subsidizing/pricing strategies for both platforms.

Corollary 2. Table 3 summarizes the pricing impacts of asymmetric piggybacking. The regions in Table 3 are illustrated in Figure 2.

The insight into the subsidizing conditions from Table 3 is consistent with Lemmas 1 and 2 but explores deeper with comparative statics with respect to n. Given $\beta ,$ when α is relatively small (region I, corresponding to cases a.1 and b of Corollary 1), both platforms subsidize the provider side. The piggybacking traf<sup>fi</sup>c either intensi<sup>fi</sup>es the provider-side subsidy war between platforms (region I-1) or causes platforms to differentiate in pricing directions on both sides $( \mathrm { i . e . , }$ in region I-2, platform A expands the price/subsidy on both sides and platform B scales back on both sides). As α grows larger (regions II-1 and II-2, corresponding to case a.2 of Corollary 1), subsidizing is suboptimal because the strengths of network effects are relatively balanced on the two sides, and subsidizing either of them does not improve the overall pro<sup>fi</sup>t. Finally, for a very large α (region III, corresponding to case a.3 of Corollary 1), both platforms subsidize the consumer side. In this case, asymmetric piggybacking causes platforms to differentiate pricing directions on both sides. Finally, asymmetric piggybacking reinforces the seesaw principle for the piggybacking platform (i.e., platform A) because

Table 2. Equilibrium Results when Only Platform A Engages in Piggybacking

<table><tr><td></td><td>Market side</td><td>Platform A</td><td>Platform B</td></tr><tr><td rowspan="2">Pricing</td><td>Consumer</td><td> $(t - T_1)\left(1 + \frac{2(2t - T_3)}{3t - 2T_3} \times n\right)$ </td><td> $(t - T_1)\left(1 + \frac{2(t - T_3)}{3t - 2T_3} \times n\right)$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha - \beta}{4}\left(1 + \frac{2(2t - T_3)}{3t - 2T_3} \times n\right)$ </td><td> $\frac{\alpha - \beta}{4}\left(1 + \frac{2(t - T_3)}{3t - 2T_3} \times n\right)$ </td></tr><tr><td rowspan="2">Market size</td><td>Consumer</td><td> $\frac{1}{2} - \frac{t - T_3}{3t - 2T_3} \times n$ </td><td> $\frac{1}{2} + \frac{t - T_3}{3t - 2T_3} \times n$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha + \beta}{4}\left(1 + \frac{4(t - 2T_3)}{3t - 2T_3} \times n\right)$ </td><td> $\frac{\alpha + \beta}{4}\left(1 + \frac{2(t - 2T_3)}{3t - 2T_3} \times n\right)$ </td></tr><tr><td>Profit</td><td></td><td> $\frac{(2t - T_2)\left[3t - 2T_3 + 2(2t - T_3) \times n\right]^2}{4(3t - T_3)^2} - c_A$ </td><td> $\frac{(2t - T_2)\left[3t - 2T_3 + 2(t - T_3) \times n\right]^2}{4(3t - T_3)^2}$ </td></tr></table>

$$
\left| (p _ {A} ^ {d}) ^ {*} - (p _ {A} ^ {c}) ^ {*} \right| > \left| \alpha - \beta / 4 - (t - T _ {1}) \right|.
$$

In responding, the no-piggybacking platform $( \mathrm { i . e . , }$ platform B) shrinks its price gap between two sides if the strength of the provider-side network effect is relatively strong (i.e., $| ( p _ { B } ^ { d } ) ^ { * } - ( p _ { B } ^ { c } ) ^ { * } | < | ( \alpha - \beta ) / 4 - ( t - T _ { 1 } ) |$ if $\alpha > \sqrt { 4 t + 3 \beta ^ { 2 } } - 2 \beta )$ . Corollary 3 examines the pro<sup>fi</sup>t impacts under asymmetric piggybacking.

Corollary 3. The following hold true in equilibrium under asymmetric piggybacking:

a. Platform A’s profit is always increasing in n.

b. Platform B’s profit is increasing in n in region I-1 and decreasing otherwise.

c. The profit gap between the two platforms is increasing and convex in n.

We use Figure 3 to explain <sup>fi</sup>ndings from Corollary 3. Somewhat surprisingly, platform A’s piggybacking bene<sup>fi</sup>ts platform B in region I-1. In region I-1 (Figure 3(a)), both platforms commit to subsidizing the provider side (dashed curves below zero), which generates pro<sup>fi</sup>t indirectly from the consumer side (solid curves). As α increases to region I-2 (Figure 3(b)), Platform B scales back on both sides (solid and dashed curves in black), and platform A expands on both sides (solid and dashed curves in gray). Finally, as α increases to region III (Figure 3(c)), both platforms switch their strategies to subsidize consumers (solid curves move below zero in Figure 3(c)). Comparing Figure 3, (b) and (c), reveals that platform B has to retreat signi<sup>fi</sup>cantly on both sides in region III, which greatly undermines its pro<sup>fi</sup>t.

## 4.2. Piggybacking Decision in Stage 0

Next, we follow the backward induction to analyze the platforms’ strategic decisions about piggybacking in stage 0, in which platforms face the trade-offs between the costs and bene<sup>fi</sup>ts of piggybacking. Recall that we have assumed a <sup>fi</sup>xed (at n) piggybacking traf<sup>fi</sup>c volume and a one-time acquisition cost $c _ { k }$ for platform k. Proposition 1 characterizes the Nash equilibrium of the platforms’ piggybacking decision (i.e., to piggyback or not).

Proposition 1. Table 4 characterizes all NEs and their corresponding conditions.

Table 3. Comparative Statics on n when Only Platform A Engages in Piggybacking

<table><tr><td rowspan="2"></td><td colspan="2">Consumer side</td><td colspan="2">Provider side</td></tr><tr><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>Region I-1:a $\alpha < \alpha_1$ </td><td>Charge more</td><td>Charge more</td><td>Subsidize moreb</td><td>Subsidize more</td></tr><tr><td>Region I-2:  $\beta \geq \sqrt{\frac{2t}{3}}, \alpha \in [\alpha_1, \underline{\alpha})$ </td><td>Charge more</td><td>Charge less</td><td>Subsidize more</td><td>Subsidize less</td></tr><tr><td>Region II-1:c $\alpha \in [\underline{\alpha}, \alpha_2)$ </td><td>Charge more</td><td>Charge more</td><td>Charge more</td><td>Charge more</td></tr><tr><td>Region II-2:  $\beta < \sqrt{\frac{2t}{3}}, \alpha \in [\alpha_2, \bar{\alpha})$ </td><td>Charge more</td><td>Charge less</td><td>Charge more</td><td>Charge less</td></tr><tr><td>Region III:  $\alpha \geq \bar{\alpha}$ </td><td>Subsidize more</td><td>Subsidize less</td><td>Charge more</td><td>Charge less</td></tr></table>

<sup>a</sup>α<sub>1 </sub> min<sub>(</sub>β, <sup></sup>4t <sub>+</sub> 3β<sup>2</sup> <sub>−</sub> 2β<sub>)</sub>.  
<sup>c</sup>α<sub>2 </sub> max<sub>(</sub>β, <sup></sup>4t <sub>+</sub> 3β<sup>2</sup> <sub>−</sub> 2β<sub>)</sub>.  
<sup>b</sup>The respective prices are negative (i.e., subsidizing) in the shaded cells.

Figure 2. Parameter Regions in Table 3  
![](/api/attachments/PPQBVQQB/fulltext/images/c87f9e214a79e570932fa4f3eeae40d22370a6ce7145fa5c586c7e2198937587.jpg)

Proposition 1 provides a rich set of novel insights into strategies that platforms use to monetize exclusive access to external users with nontrivial characterizations of the interplay among piggybacking, cross-side network effects, and price competition. To illustrate, consider the symmetric case with identical platforms (e.g., $c _ { A } = c _ { B } = c )$ . Figure 4 depicts a spectrum of equilibrium outcomes depending on the piggybacking cost (vertical axis) and strengths of cross-side network effects (horizontal axis).

First, moving vertically from high to low (the vertical arrow in Figure 4), piggybacking becomes optimal for both platforms when c is low, which is intuitive. However, perhaps more interesting is that, on the right-hand side (RHS) of Figure 4 on which α is relatively large (compared with $\beta ) _ { . }$ , even with identical platforms, the equilibrium could go across different outcomes as piggybacking cost c decreases: from no piggybacking to prisoner’s dilemma and, <sup>fi</sup>nally, to win–win (i.e., both piggyback with pro<sup>fi</sup>t improvement). Such nontrivial equilibrium outcomes are driven by the piggybacking cost and strengths of cross-side network effects. Strong network efforts (RHS of Figure 4) make the consumer side extremely competitive, which could lead to a PD, that is, a smaller pro<sup>fi</sup>t for both platforms compared with the cases of no piggybacking equilibrium or asymmetric equilibrium. The complex transition described becomes even more likely under a large $\beta ,$ in which case the areas of PD and asymmetric equilibrium in Figure 4 are enlarged.

Second, moving horizontally from left to right (the horizontal arrow in Figure $4 ) ,$ , the equilibrium outcomes may switch back and forth: from win–win, to prisoner’s dilemma, to asymmetric piggybacking, to no piggybacking, and interestingly back to asymmetric piggybacking. Intuitively, this switching behavior is due to decreasing pro<sup>fi</sup>t on the consumer side. As shown in Lemma 2, with or without piggybacking, a stronger level of cross-side network effects intensi<sup>fi</sup>es platform competition and undermines competing platforms’ pro<sup>fi</sup>ts. Our result extends the prior knowledge by showing that platforms can strategically balance between pro<sup>fi</sup>ts on two sides via piggybacking. When α is relatively small, that is, on the left-hand side of Figure ${ \dot { 4 } } , \quad$ piggybacking is desirable because it expands the focal market and increases the overall pro<sup>fi</sup>t. In this region, piggybacking complements provider-side subsidization. As α increases to the dark gray area along the horizontal arrow $\alpha \approx 0 . 9 3 )$ , the network effects undermine the consumer-side pro<sup>fi</sup>t, but piggybacking is needed by platforms to monetize the provider side. For an even larger α, which imposes a higher pricing pressure on the consumer side, piggybacking provides an opportunity for two identical platforms to differentiate (i.e., leading to an asymmetric outcome). These <sup>fi</sup>ndings are new to the literature. We summarize this insight in Corollary 4.

Figure 3. Pro<sup>fi</sup>t Impacts of Piggybacking in Regions when Subsidizing Is Optimal $( t = 1 , \beta = 0 . 9 )$  
(a)  
![](/api/attachments/PPQBVQQB/fulltext/images/d73746e66e27432810ba1717667aa9e9a5f918fbc32cc0524172018bd6fbc49e.jpg)

(b)  
![](/api/attachments/PPQBVQQB/fulltext/images/dd83859c6dd7d62726eff5f3cd48ff63cbd4e20c5e654eade42f4668dd89f0ab.jpg)

(c)  
![](/api/attachments/PPQBVQQB/fulltext/images/f3630b93ff196b003c33d8d3fe578e6f377aa1050a8f38d4bba23137bb8ce7ca.jpg)

Table 4. Equilibrium Results of Piggybacking Decisions

<table><tr><td></td><td>Region</td><td colspan="2"> $\{I_A I_B\}$ </td></tr><tr><td rowspan="5">Weak provider-side NE $(\alpha < \sqrt{4t + 3\beta^2} - 2\beta)$ </td><td> $c_k < \tilde{c}_1$ </td><td> $\{1, 1\}$ </td><td>Both</td></tr><tr><td> $c_B \geq \tilde{c}_1, c_A < \tilde{c}_2$ </td><td> $\{1, 0\}$ </td><td>Only platform A</td></tr><tr><td> $c_A \geq \tilde{c}_1, c_B < \tilde{c}_2$ </td><td> $\{0, 1\}$ </td><td>Only platform B</td></tr><tr><td>All other cases</td><td> $\{0, 0\}$ </td><td>Neither</td></tr><tr><td> $c_k < \tilde{c}_1$ </td><td> $\{1, 1\}$ </td><td>Both</td></tr><tr><td rowspan="4">Strong provider-side NE $(\alpha \geq \sqrt{4t + 3\beta^2} - 2\beta, n \leq \bar{n})$ </td><td> $c_k \geq \tilde{c}_2$ </td><td> $\{0, 0\}$ </td><td>Neither</td></tr><tr><td> $c_k \in [\tilde{c}_1, \tilde{c}_2)$ </td><td> $\{1, 0\}, \{0, 1\}$ </td><td>Either platform A or B</td></tr><tr><td>All other cases with  $c_A \geq c_B$ </td><td> $\{0, 1\}$ </td><td>Only platform B</td></tr><tr><td>All other cases with  $c_A < c_B$ </td><td> $\{1, 0\}$ </td><td>Only platform A</td></tr></table>

Note. Where c˜ <sup>n(</sup> <sup>)</sup> <sup>2t−T3</sup> <sup>(</sup> <sup>)</sup> <sup>2t−T2</sup> <sup>(</sup> <sup>)</sup> <sup>n(</sup> <sup>)+</sup> <sup>4t−3T1</sup> <sup>3t−2T1</sup> and c˜ <sup>n(</sup> <sup>)</sup> <sup>2t−T1</sup> <sup>(</sup> <sup>)</sup> <sup>2t−T3</sup> <sup>(</sup> <sup>)</sup> <sup>(</sup> <sup>)</sup> <sup>n+3</sup> <sup>t−(</sup> <sup>)</sup> <sup>n+2</sup> <sup>T1</sup> 3t 2T <sup>2</sup> 3t 2T <sup>2</sup>

Corollary 4. Denote $\tilde { c } _ { 3 } = n ( n + 1 ) ( 2 t - T _ { 2 } )$ . In equilibrium, the following hold $( \tilde { c } _ { 1 }$ is defined in Table 4):

a. If platforms subsidize the consumer side (region III in Figure 2), the piggybacking equilibrium $( \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 )$ is a prisoner’s dilemma i $\mathcal { f } c _ { k } \in \bar { ( c _ { 3 } , c _ { 1 } ) }$

b. If platforms subsidize the provider side (regions I-1 and I-2 in Figure 2), it is only in region I-2 $( \beta = \sqrt { 2 t / 3 } , \stackrel { \cdot } { \alpha } \in [ \alpha _ { 1 } , \beta ) )$ that the piggybacking equilibrium $( \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 )$ is a prisoner’s dilemma iff ${ \bf { \dot { \alpha } } } c _ { k } \in ( \tilde { c } _ { 3 } , \tilde { c } _ { 1 } )$

To understand Corollary 4, note from Lemma 2 that the parameter regions of $\{ \alpha , \beta \}$ for platform subsidization are not affected by piggybacking. According to Lemmas $1 { - } 3 ,$ subsidizing the multihoming side (i.e., providers) is optimal in regions I-1 and I-2, and subsidizing the single-homing side (i.e., consumers) is optimal when α is suf<sup>fi</sup>ciently large (region III). We illustrate these two regions in the shaded areas on both the left and right ends in Figure 4. The white region in between (in which the network effects are moderate on both sides) represents the region in which subsidizing is suboptimal. Therefore, Figure 4 provides a useful mapping of the interplay of the optimal subsidizing strategy and piggybacking. It shows clearly when piggybacking is pro<sup>fi</sup>t improving and when it leads to a PD. Further, Figure 4 and Proposition 1 also show that asymmetric piggybacking can constitute an equilibrium between symmetric platforms if the strength of the network effects is suf<sup>fi</sup>ciently large. However, such an asymmetric piggybacking equilibrium under symmetric platform competition does not arise as an equilibrium under alternative cost function.

Figure 4. (Color online) Nash Equilibria Under Symmetric Platform Competition $( t = 1 , n = 1 / 8 )$  
![](/api/attachments/PPQBVQQB/fulltext/images/1955f1c346a5bb6a4d5ac2b9678052b5a5a6917da9053cd1de51731584841f8f.jpg)

## 5. Provider-Side Piggybacking

In this section, we consider provider-side piggyback-$\mathrm { i n g . } ^ { 8 }$ For example, India’s largest local commerce marketplace, Justdial, was initially a phone directory service platform through which consumers could <sup>fi</sup>nd local service providers, such as barbers and <sup>fl</sup>orists. Justdial implemented piggybacking by borrowing provider information from the local yellow pages. When a consumer called in looking for a certain service provider, Justdial searched the yellow pages and passed on the lead to the service provider. In this way, some of the service providers were pulled into Justdial’s platform to eventually become paying subscribers (Parker et al. 2016).

Compared with consumer-side piggybacking, provider-side piggybacking has another layer of complication: focal providers are multihoming, but piggybacking providers may single home or multihome. For example, Airbnb offers Airbnb Plus service for homeowners, including professional photography, writing services, etc. In exchange, the listings of the same property on other booking websites must be removed.<sup>9</sup> To model piggybacking on the provider side, we modify the objective function as follows:

$$
\max _ {p _ {k} ^ {c}, p _ {k} ^ {d}} \Pi_ {k} = p _ {k} ^ {c} N _ {k} ^ {c} + p _ {k} ^ {d} (N _ {k} ^ {d} + \mathbb {I} _ {k} n + \mathbb {I} _ {m} \mathbb {I} _ {- k} n) - \mathbb {I} _ {k} c _ {k},\tag{6}
$$

in which $\mathbb { I } _ { m }$ equals one if the piggybacking providers are multihoming, and $\mathbb { I } _ { m }$ equals zero if they are single homing. The consumer-side network size can be shown as

$$
\begin{array}{l} N _ {k} ^ {c} = \frac {1}{2} - \frac {p _ {k} ^ {c} - p _ {- k} ^ {c}}{2 t} \\ \qquad + \frac {\beta \left[ (N _ {k} ^ {d} + \mathbb {I} _ {k} n + \mathbb {I} _ {m} \mathbb {I} _ {- k} n) - (N _ {- k} ^ {d} + \mathbb {I} _ {- k} n + \mathbb {I} _ {m} \mathbb {I} _ {k} n) \right]}{2 t}. \end{array}\tag{7}
$$

By solving platform $k ^ { \prime } s$ problem, we obtain the following equilibrium results.

Table 5. Equilibrium Prices when Both Platforms Engage in Provider-Side Piggybacking

<table><tr><td></td><td>Market side</td><td>Platform A/B</td></tr><tr><td rowspan="2"> $I_m = 1$ </td><td>Consumer</td><td> $t - T_1 - n\alpha$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha-\beta}{4} + n$ </td></tr><tr><td rowspan="2"> $I_m = 0$ </td><td>Consumer</td><td> $t - T_1 - \frac{n\alpha}{2}$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha-\beta}{4} + \frac{n}{2}$ </td></tr></table>

Lemma 4. The following holds true for provider-side piggybacking (coefficients $\phi _ { 1 }$ to $\phi _ { 4 }$ are defined in the appendix):

a. Table 5 gives the equilibrium prices if both platforms engage in piggybacking.

b. Table 6 gives the equilibrium prices if only platform A engages in piggybacking.

Corollary 5 examines pro<sup>fi</sup>t implications of our key interest.

Corollary 5. When piggybacking providers single home $( i . e . , \mathbb { I } _ { m } = 0 )$ , piggybacking equilibrium results in a prisoner’s dilemma $i f c _ { k } \in ( \tilde { c } _ { 4 } , \tilde { c } _ { 5 } )$ . Otherwise, when piggybacking providers multihome $( i . e . , \mathbb { I } _ { m } = 1 )$ , piggybacking is always profit-improving in equilibrium. Both $\tilde { c } _ { 4 }$ and $\tilde { c } _ { 5 }$ are defined in the appendix.

Lemma 4 and Corollary 5 show that the key insights derived from consumer-side piggybacking in Section 4 hold for provider-side piggybacking except that the prisoner’s dilemma disappears if piggybacking providers multihome. In particular, Lemma 4 suggests that the interplay between piggybacking and the seesaw principle is qualitatively similar between consumer- and provider-side piggybacking. Under provider-side piggybacking, $( p _ { A } ^ { d } ) ^ { * } - ( p _ { A } ^ { c } ) ^ { * } > ( \alpha - \beta ) / 4 -$ $\bar { ( } t - T _ { 1 } ) \mathrm { ~ i f ~ } ( \alpha - \bar { \beta } ) / 4 > ( t - T _ { 1 } ) . ^ { 1 0 }$ This indicates that the piggybacking platform (i.e., platform A) reinforces the seesaw principle as long as the consumer side is more competitive (i.e., $( \alpha - \beta ) / 4 > t - T _ { 1 } )$ . It can be inferred from Tables 5 and 6 that this observation is true for both symmetric and asymmetric piggybacking regardless of whether piggybacking providers multihome or single home. In responding, the nopiggybacking platform (i.e., platform B) shrinks the price gap between two sides $( ( p _ { B } ^ { d } ) ^ { * } - ( p _ { B } ^ { c } ) ^ { * } < ( \alpha - \beta ) / 4 -$ $( t - T _ { 1 } ) \mathrm { i f } n \le 2 ( 6 t - \alpha ^ { 2 } - 4 \alpha \beta - \beta ^ { 2 } ) / ( \alpha + \beta ) )$ ) if piggybacking providers single home.<sup>11</sup> This is also similar to our <sup>fi</sup>ndings in consumer-side piggybacking in Section 4.

Not surprisingly, when piggybacking providers multihome, the prisoner’s dilemma no longer exists because both platforms can happily receive a positive spillover from the rival, and the overall market is expanded. In contrast, if platforms can lock in their piggybacking providers, a prisoner’s dilemma is possible in equilibrium because of the same logic as discussed in Section 4, that is, piggybacking intensi<sup>fi</sup>es consumerside competition.

Table 6. Equilibrium Prices when Only Platform A Engages in Provider-Side Piggybacking

<table><tr><td></td><td>Market side</td><td>Platform A</td><td>Platform B</td></tr><tr><td rowspan="2"> $\mathbb{I}_{m} = 1$ </td><td>Consumer</td><td> $t - T_{1} - \frac{n\alpha}{2}$ </td><td> $t - T_{1} - \frac{n\alpha}{2}$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha-\beta}{4} + \frac{n}{2}$ </td><td> $\frac{\alpha-\beta}{4} + \frac{n}{2}$ </td></tr><tr><td rowspan="2"> $\mathbb{I}_{m} = 0$ </td><td>Consumer</td><td> $t - T_{1} + \phi_{1}n$ </td><td> $(t - T_{1})(1 + \phi_{2}n)$ </td></tr><tr><td>Provider</td><td> $\frac{\alpha-\beta}{4} + \phi_{3}n$ </td><td> $\frac{\alpha-\beta}{4}(1 + \phi_{4}n)$ </td></tr></table>

## 6. Discussions and Conclusion

Piggybacking, as perhaps the most prominent traf-<sup>fi</sup>c-based strategy, has become a critical competitive strategy among practical platforms. This paper formally explores the strategic implications of piggybacking and platform pricing/subsidization in a competitive setting with network effects. We discover regions in which piggybacking is desirable and for which platform (or both) and the region of the prisoner’s dilemma in which piggybacking could back<sup>fi</sup>re and undermine the platform’s pro<sup>fi</sup>t in the platform duopoly.

An important implication of our paper is that start-up platforms could employ nonpricing controls, such as piggybacking, to gain early advantages that are critical to platform growth. By piggybacking on Myspace to recruit users, YouTube quickly assumed the lead in the competition against its competitors and even pushed some similar video platforms out of the market. For example, Revver, the <sup>fi</sup>rst video website to monetize video content through advertising and share the revenue with video contributors (a business model similar to YouTube’s) was shut down in 2011.

Interestingly, piggybacking has been proactively embraced by many “mega” networks, which allow start-up platforms to connect with their vast network of consumers. A prominent example is WeChat. With more than 1.1 billion active monthly users and roughly 34% of Chinese data traf<sup>fi</sup>c, WeChat launched “miniprograms” in 2017, allowing third parties to develop the application as a WeChat built-in module that does not require downloading for use. An article from The New York Times describes miniprograms as providing “access where you can sell to any Chinese person with WeChat, which is basically everyone.”<sup>12</sup> For example, the startup platform Pinduoduo (PDD), established in 2015, used WeChat miniprograms to grow its user count by more than 440 million in 2018, which outnumbered JD.com during the same period and made PDD the second-largest e-commerce platform in China.<sup>13</sup> Other mega platforms worldwide are also following WeChat by creating new features similar to WeChat’s miniprograms. For example, the recently introduced WhatsApp Business—a platform that allows local businesses to provide information and communicate with their customers— bears a striking resemblance to WeChat’s miniprograms and has been gathering momentum in Mexico and India. As it becomes less costly for start-ups to import external traf<sup>fi</sup>c from these mega networks, the result from our paper raises the alarm that piggybacking might not always improve start-up performance. As Corollary 4 states, although the subsidizing strategy continues to hold in the presence of piggybacking, it could back<sup>fi</sup>re if the strength of cross-side network effects is stronger. Our note provides a useful framework to guide piggybacking strategies for start-ups.

Admittedly, there are limitations in our model. For example, providers may hesitate when considering joining more than one platform because of the potential multihoming costs. Our note has simpli<sup>fi</sup>ed this direction. Future research may consider looking into multihoming costs and decisions in the platform competition.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their constructive feedback throughout the review process. The authors also thank Edward Anderson, Hemant Bhargava, Yuxin Chen, Vidyanand Choudhary, Ming Fan, Xianjun Geng, Hanna Halaburda, Marius F. Niculescu, Geoffrey G. Parker, Jennifer Zhang, Juanjuan Zhang, and Feng Zhu, the seminar participants at the City University of Hong Kong, City University of New York, Harvard University, Lehigh University, National University of Singapore, Temple University, Tsinghua University, University of California at Irvine, University of North Texas, University of Texas at Austin, and University of Utah, as well the participants at the 2015 Workshop on Information Systems and Economics (WISE) at UT Dallas, the 2017 Platform Strategy Research Symposium at Boston University, the 2017 IN-FORMS Conference on Information Systems and Technology (CIST) in Houston, and the 2019 Theory in Economics of Information Systems (TEIS) Workshop in Vancouver, Canada, for their helpful comments and discussions.

## Appendix. Proofs

Proof of Lemma 1. The equilibrium conditions are

$$
{N _ {A} ^ {c}} = {\frac {1}{2} - \frac {p _ {A} ^ {c} - p _ {B} ^ {c}}{2 t} + \frac {\beta (N _ {A} ^ {d} - N _ {B} ^ {d})}{2 t},}
$$

$$
{N _ {B} ^ {c}} = {\frac {1}{2} - \frac {p _ {B} ^ {c} - p _ {A} ^ {c}}{2 t} + \frac {\beta (N _ {B} ^ {d} - N _ {A} ^ {d})}{2 t},}
$$

$$
{N _ {A} ^ {d}} = {\alpha N _ {A} ^ {c} - p _ {A} ^ {d}, \mathrm{and} N _ {B} ^ {d} = \alpha N _ {B} ^ {c} - p _ {B} ^ {d}.}
$$

Solving the system of equations gives the equilibrium market sizes.

$$
\begin{array}{r l} & N _ {A} ^ {c} = \frac {1}{2} + \frac {p _ {B} ^ {c} - p _ {A} ^ {c} + \beta (p _ {B} ^ {d} - p _ {A} ^ {d})}{2 (t - \alpha \beta)}, \\ & N _ {B} ^ {c} = \frac {1}{2} - \frac {p _ {B} ^ {c} - p _ {A} ^ {c} + \beta (p _ {B} ^ {d} - p _ {A} ^ {d})}{2 (t - \alpha \beta)}, \\ & N _ {A} ^ {d} = \frac {\alpha}{2} + \frac {\alpha [ p _ {B} ^ {c} - p _ {A} ^ {c} + \beta (p _ {A} ^ {d} + p _ {B} ^ {d}) ] - 2 t p _ {A} ^ {d}}{2 (t - \alpha \beta)}, \\ & N _ {B} ^ {d} = \frac {\alpha}{2} + \frac {\alpha [ p _ {A} ^ {c} - p _ {B} ^ {c} + \beta (p _ {A} ^ {d} + p _ {B} ^ {d}) ] - 2 t p _ {B} ^ {d}}{2 (t - \alpha \beta)}. \end{array}\tag{A.1}
$$

Insert Equation (A.1) into the objective functions in Equation (5). If we take platform A as an example, the pro<sup>fi</sup>t function is

$$
\begin{array}{r} \Pi_ {A} = - \frac {1}{2 (t - \alpha \beta)} \times (p _ {A} ^ {c}) ^ {2} + \left[ \frac {1}{2} - \frac {(\alpha + \beta) p _ {A} ^ {d} - p _ {B} ^ {c} - \beta p _ {B} ^ {d}}{2 (t - \alpha \beta)} \right] \times p _ {A} ^ {c} \\ + \alpha \left(\frac {1}{2} + \frac {p _ {B} ^ {c} + \beta p _ {B} ^ {d}}{2 (t - \alpha \beta)}\right) \times p _ {A} ^ {d} - \left(1 + \frac {t}{t - \alpha \beta}\right) \times (p _ {A} ^ {d}) ^ {2}. \end{array}
$$

Take the second-order derivatives of $p _ { A } ^ { c }$ and $p _ { A } ^ { d }$ . Respectively, we have

$$
\begin{array}{l} \frac {\partial^ {2} \Pi_ {A}}{\partial (p _ {A} ^ {c}) ^ {2}} = - \frac {1}{t - \alpha \beta} \leq 0, \\ \frac {\partial^ {2} \Pi_ {A}}{\partial (p _ {A} ^ {d}) ^ {2}} = - \bigg (1 + \frac {t}{t - \alpha \beta} \bigg) \leq 0. \end{array}
$$

The determinant of the Hessian matrix is

$$
\det (\mathbf {H} _ {p _ {A} ^ {c}, p _ {A} ^ {d}} (\Pi_ {A})) = \frac {8 t - \alpha^ {2} - 6 \alpha \beta - \beta^ {2}}{4 (t - \alpha \beta) ^ {2}},
$$

which is always positive for $\begin{array} { r } { \alpha \leq 2 \sqrt { t } - \beta . } \end{array}$ It indicates that $\Pi _ { A }$ is jointly concave in $p _ { A } ^ { c }$ and $p _ { A } ^ { d }$ such that there is a unique pair of $\left\{ ( p _ { A } ^ { c } ) ^ { * } , ( p _ { A } ^ { d } ) ^ { * } \right\}$ that maximizes $\Pi _ { A } .$ . Similar results also apply to Π<sub>B</sub>. We can then solve the equilibrium by setting the <sup>fi</sup>rst-order derivatives at zero simultaneously.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {1}{2} + \frac {p _ {B} ^ {c} + \beta p _ {B} ^ {d} - \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {\alpha (t - \alpha \beta + p _ {B} ^ {c} + \beta p _ {B} ^ {d}) - (\alpha + \beta) p _ {A} ^ {c} - 2 (2 t - \alpha \beta) p _ {A} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {1}{2} + \frac {p _ {A} ^ {c} + \beta p _ {A} ^ {d} - \alpha \beta - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha (t - \alpha \beta + p _ {A} ^ {c} + \beta p _ {A} ^ {d}) - (\alpha + \beta) p _ {B} ^ {c} - 2 (2 t - \alpha \beta) p _ {B} ^ {d}}{2 (t - \alpha \beta)} = 0. \end{array}
$$

The solution to this system of equations gives the equilibrium prices in Lemma 1. The equilibrium pro<sup>fi</sup>ts and market sizes can be obtained by inserting the equilibrium prices back to Equations (A.1) and (5). w

Proof of Corollary 1.

a. The condition $\beta \leq { \sqrt { t } }$ is equivalent to $\beta \leq 2 \sqrt { \underline { { t } } } - \beta .$ . Then, it is possible that α $\in [ \beta , 2 \sqrt { t } - \beta ]$ exists when $\beta \leq { \sqrt { t } } .$

1. For $\alpha < \underline { { \alpha } } = \beta ,$ , it is trivial to see that $p _ { k } ^ { d } \dot { = } ( \alpha - \beta ) / 4 < 0 .$

2. For all $\alpha \in [ \beta , 2 \sqrt { t } - \beta ] , p _ { k } ^ { d } \geq 0$ always holds, indicating that subsidizing the provider side is not optimal. On the consumer side, $p _ { k } ^ { c } = \dot { t } - \alpha ( 3 \alpha + \beta ) / 4$ , which is a concave and quadratic function of $\alpha .$ Thus, to have $p _ { k } ^ { c }$ smaller than zero, we need α outside two roots to $p _ { k } ^ { c } ( \alpha ) \stackrel {  } { = } 0$ . Solving $t - \alpha ( 3 \alpha + \beta ) / 4 = 0 .$ , we obtain the following roots:

$$
\alpha_ {r 1} = - \frac {\sqrt {1 6 t + 9 \beta^ {2}} + 3 \beta}{2}, \alpha_ {r 2} = \frac {\sqrt {1 6 t + 9 \beta^ {2}} - 3 \beta}{2}.
$$

The <sup>fi</sup>rst (and the smaller) root is always negative. Given $\beta < { \sqrt { t } } ,$ , the second (and the larger) root is always greater than $\beta$ but smaller than $2 { \sqrt { t } } - { \dot { \beta } } .$ . Therefore, both $p _ { k } ^ { d }$ and $p _ { k } ^ { c }$ are nonnegative for $\alpha \in [ \beta , \alpha _ { r 2 } ]$

3. For $\alpha \in \overline { { ( \alpha _ { r 2 } , 2 \sqrt { t } - \beta ] } } ,$ , following the preceding discussion, we know that $p _ { k } ^ { c } < 0$

b. $\beta > \sqrt { t }$ . In this case, it is impossible to have any $\alpha \geq \beta .$ Thus, subsidizing providers is always optimal. w

Proof of Lemma 2. Following an approach similar to that in the proof of Lemma 1, we show that the pro<sup>fi</sup>t functions are jointly concave for prices on both sides, which implies a unique equilibrium. We can then solve the equilibrium by setting the <sup>fi</sup>rst-order derivatives at zero simultaneously.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {1}{2} + \frac {(2 t - \alpha \beta) n + p _ {B} ^ {c} + \beta p _ {B} ^ {d} - \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {\alpha [ \alpha (2 t - \alpha \beta) n + t - \alpha \beta + p _ {B} ^ {c} + \beta p _ {B} ^ {d} ] - (\alpha + \beta) p _ {A} ^ {c} - 2 (2 t - \alpha \beta) p _ {A} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {1}{2} + \frac {(2 t - \alpha \beta) n + p _ {A} ^ {c} + \beta p _ {A} ^ {d} - \alpha \beta - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha [ \alpha (2 t - \alpha \beta) n + t - \alpha \beta + p _ {A} ^ {c} + \beta p _ {A} ^ {d} ] - (\alpha + \beta) p _ {B} ^ {c} - 2 (2 t - \alpha \beta) p _ {B} ^ {d}}{2 (t - \alpha \beta)} = 0. \end{array}
$$

The solution to this system of equations gives the equilibrium result in Lemma $2 . \ \square$

Proof of Lemma 3. Our <sup>fi</sup>rst step is to con<sup>fi</sup>rm the no-exit condition for platform B. Under asymmetric piggybacking, the interior solution to the pricing equilibrium may not be feasible because the constraints of nonnegative market size could be violated. Therefore, we focus on the region in which the focal market share is nonnegative and rule out the infeasible cases.

We <sup>fi</sup>rst solve for interior equilibrium prices and reinsert them into Equation (A.1). With $\alpha < 2 { \sqrt { t } } - { \bar { \beta } } ,$ it can be shown that both $N _ { A } ^ { c }$ and $N _ { A } ^ { d }$ are always nonnegative. Thus, we only need to check the regions of $N _ { { R } } ^ { c } \geq 0$ and $N _ { B } ^ { d } \geq 0$

Region 1: $N _ { B } ^ { c } = ( \stackrel { \smile } { 1 + n } ) / 2 - \tilde { n t } / ( 6 t - \alpha ^ { 2 } - \bar { 4 } \alpha \beta - \beta ^ { 2 } ) \geq 0 .$ When $4 t - \alpha ^ { 2 } - 4 \alpha \beta - \beta ^ { 2 } \geq 0 .$ , <sup>Nc</sup> is nondecreasing in n and $N _ { B } ^ { c }$ is always positive. Otherwise, if $4 t - \alpha ^ { 2 } - 4 \alpha \beta - \beta ^ { 2 } <$ $0 , N _ { B } ^ { c }$ is decreasing in n and becomes negative at $n = 1 / 2$ . It implies that there is a threshold of n above which $N _ { B } ^ { c } < 0$

$$
\frac {1 + n}{2} - \frac {n t}{6 t - \alpha^ {2} - 4 \alpha \beta - \beta^ {2}} = 0 \rightarrow n = \frac {t}{2 (T _ {3} - t)} - 1.
$$

We denote $\bar { n } = t / ( 2 ( T _ { 3 } - t ) ) - 1$ . Therefore, when $t < T _ { 3 } .$ the equilibrium is not feasible if $n > \bar { n }$

Region 2: $N _ { B } ^ { d } = ( \alpha + \beta ) ( 1 + 2 n ( t - T _ { 3 } ) / ( 3 t - 2 T _ { 3 } ) ) / 4 \times n ] \ge 0 .$ Similarly, the exact same condition causes $N _ { B } ^ { d } < 0 .$ . Therefore, the interior equilibrium results are not feasible only when both $4 t - \alpha ^ { 2 } - 4 \alpha \beta - \beta ^ { 2 } < 0$ and $n > \bar { n }$ hold.

Given the condition that platform B stays in the market, when equilibrium exists, we can obtain the equilibrium prices in Table 2 by solving the following systems of <sup>fi</sup>rst or der condition (FOC) equations:

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = - \frac {p _ {A} ^ {c}}{t - \alpha \beta} + \left(\frac {1}{2} - \frac {(\alpha + \beta) p _ {A} ^ {d} - p _ {B} ^ {c} - \beta p _ {B} ^ {d} - (2 t - \alpha \beta) n}{2 (t - \alpha \beta)}\right) = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = - \left(1 + \frac {t}{t - \alpha \beta}\right) p _ {A} ^ {d} + \frac {\alpha [ p _ {B} ^ {c} + \beta p _ {B} ^ {d} + n (2 t - \alpha \beta) + (t - \alpha \beta) ] - (\alpha + \beta) p _ {A} ^ {c}}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = - \frac {p _ {B} ^ {c}}{t - \alpha \beta} + \left(\frac {1}{2} - \frac {(\alpha + \beta) p _ {B} ^ {d} - p _ {A} ^ {c} - \beta p _ {A} ^ {d} + \alpha \beta n}{2 (t - \alpha \beta)}\right) = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = - \left(1 + \frac {t}{t - \alpha \beta}\right) p _ {B} ^ {d} + \frac {\alpha [ p _ {A} ^ {c} + \beta p _ {A} ^ {d} + \alpha \beta n + (t - \alpha \beta) ] - (\alpha + \beta) p _ {B} ^ {c}}{2 (t - \alpha \beta)} = 0. \end{array}
$$

The equilibrium pro<sup>fi</sup>ts and market sizes can be obtained by inserting the equilibrium prices back into Equations (A.1) and (5). w

Proof of Corollary 2. First, note that, for all $n \leq 1 / 2$ that satisfy the no-exit conditions for platform B (see the proof of Lemma 3), it can be veri<sup>fi</sup>ed that the sign of the equilibrium prices are not affected. It implies that Corollary 1 holds true for both platforms under asymmetric piggybacking. Second, we can then de<sup>fi</sup>ne regions I-1 and I-2 (corresponding to cases a.1 and b in Corollary 1) and regions II-1 and II-2 (corresponding to cases a.2 in Corollary 1). Take the <sup>fi</sup>rst-order derivatives with respect to n in equilibrium prices, and we have

$$
\begin{array}{l} \frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} = \frac {2 (2 t - T _ {3}) (t - T _ {1})}{3 t - 2 T _ {3}}, \\ \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} = \frac {2 (t - T _ {3}) (t - T _ {1})}{3 t - 2 T _ {3}}, \\ \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} = \frac {(\alpha - \beta) (2 t - T _ {3})}{2 (3 t - 2 T _ {3})}, \\ \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} = \frac {(\alpha - \beta) (t - T _ {3})}{2 (3 t - 2 T _ {3})}. \end{array}
$$

Note that $3 t > 2 T _ { 3 }$ always holds for $\begin{array} { r } { \alpha < 2 \sqrt { t } - \beta . } \end{array}$ We go through each region to check the signs of the <sup>fi</sup>rst order derivatives. As suggested by Corollary 1, the signs of the price are determined by $( t - T _ { 1 } )$ and $( \alpha - \beta )$

<sub>•</sub> Region I-1: $t \geq T _ { 3 } \geq T _ { 1 } , \alpha < \beta .$ Then, we have

$$
\frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} <   0, \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} \geq 0, \text { and } \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} <   0.
$$

Region I-2: $t < T _ { 3 } , \alpha < \beta .$ . Then, we have

$$
\frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} <   0, \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} <   0, \mathrm{and} \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} \geq 0.
$$

<sub>•</sub> Region $\begin{array} { r } { \mathrm { I I } - 1 \colon t \geq T _ { 3 } \geq T _ { 1 } , \alpha \geq \beta . } \end{array}$ Then, we have

$$
\frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} \geq 0, \text { and } \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} \geq 0.
$$

<sub>•</sub> Region $\begin{array} { r } { \operatorname { I I - 2 : } t \in [ T _ { 1 } , T _ { 3 } ) , \alpha \geq \beta . } \end{array}$ Then, we have

$$
\frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} <   0, \mathrm{and} \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} <   0.
$$

<sub>•</sub> Region III: $t < T _ { 1 } , \alpha \geq \beta .$ . Then, we have

$$
\frac {\partial (p _ {A} ^ {c}) ^ {*}}{\partial n} <   0, \frac {\partial (p _ {A} ^ {d}) ^ {*}}{\partial n} \geq 0, \frac {\partial (p _ {B} ^ {c}) ^ {*}}{\partial n} > 0, \text { and } \frac {\partial (p _ {B} ^ {d}) ^ {*}}{\partial n} \leq 0.
$$

We summarize them in Table 3. w

Proof of Corollary 3. a. We take the <sup>fi</sup>rst and second order derivatives with respect to n in $\Pi _ { A } ^ { * }$

$$
\begin{array}{l} \frac {\partial (\Pi_ {A}) ^ {*}}{\partial n} = \frac {(2 t - T _ {3}) (2 t - T _ {2}) ((4 n + 3) t - 2 (n + 1) T _ {3})}{(3 t - 2 T _ {3}) ^ {2}}, \\ \frac {\partial^ {2} (\Pi_ {A}) ^ {*}}{\partial n ^ {2}} = \frac {2 (T _ {3} - 2 t) ^ {2} (2 t - T _ {2})}{(3 t - 2 T _ {3}) ^ {2}}. \end{array}
$$

When platform B stays in the market, $( 4 n + 3 ) t -$ $2 ( n + 1 ) \dot { T _ { 3 } } \geq 0$ always holds for all $n \leq 1 / 2$ . Therefore, both the <sup>fi</sup>rst and second order derivatives are nonnegative because $2 t - T _ { 2 } \geq 0$ always holds. It indicates that $\left( \Pi _ { A } \right) ^ { * }$ is increasing and convex in n.

b. Then, we take the <sup>fi</sup>rst and second order derivatives with respect to n in $\Pi _ { B } ^ { * }$

$$
\begin{array}{l} \frac {\partial (\Pi_ {B}) ^ {*}}{\partial n} = \frac {(t - T _ {3}) (2 t - T _ {2}) [ (2 n + 3) t - 2 (n + 1) T _ {3} ]}{(3 t - 2 T _ {3}) ^ {2}}, \\ \frac {\partial^ {2} (\Pi_ {B}) ^ {*}}{\partial n ^ {2}} = \frac {2 (t - T _ {3}) ^ {2} (2 t - T _ {2})}{(3 t - 2 T _ {3}) ^ {2}} > 0. \end{array}
$$

When platform B stays in the market, $( 2 n + 3 ) t -$ $2 ( n + 1 ) \bar { T _ { 3 } } \geq 0$ always holds for all $n \leq 1 / 2 .$ . Therefore, $\partial { ( \Pi _ { B } ) } ^ { * } / \partial n \geq 0$ iff $t - T _ { 3 } \geq 0 ,$ which is equivalent to $\alpha < \sqrt { 4 t + 3 \beta ^ { 2 } } - 2 \beta .$ The second order derivative is positive such that $\left( \Pi _ { B } \right) ^ { * }$ is convex in n.

c. The pro<sup>fi</sup>t gap between the two platforms is given by

$$
(\Pi_ {A}) ^ {*} - (\Pi_ {B}) ^ {*} = \frac {n (n + 1) t (2 t - T _ {2})}{3 t - 2 T _ {3}}.
$$

We take the <sup>fi</sup>rst and second order derivatives with respect to n.

$$
\begin{array}{l} \frac {\partial [ (\Pi_ {A}) ^ {*} - (\Pi_ {B}) ^ {*} ]}{\partial n} = \frac {(2 n + 1) t (2 t - T _ {2})}{3 t - 2 T _ {3}} > 0, \\ \frac {\partial^ {2} [ (\Pi_ {A}) ^ {*} - (\Pi_ {B}) ^ {*} ]}{\partial n ^ {2}} = \frac {2 t (2 t - T _ {2})}{3 t - T _ {3}} > 0. \end{array}
$$

Given that $2 t - T _ { 2 } , 3 t - 2 T _ { 3 } ,$ and $3 t - T _ { 3 }$ are all positive for $\begin{array} { r } { \alpha < 2 \sqrt { t } - \beta , } \end{array}$ the pro<sup>fi</sup>t gap is increasing and convex in n. w

Proof of Proposition 1. Without loss of generality, this proof focuses on the case in which $c _ { B } \geq c _ { A } ,$ the scenario in which $c _ { A } > c _ { B }$ is symmetric. Each platform faces a binary decision on whether to piggyback. The $2 \times 2$ possible outcomes are illustrated in Table A.1.

Table A.1. Illustration of the Platform Duopoly

<table><tr><td></td><td>Platform BNo Piggybacking</td><td>Platform BPiggybacking</td></tr><tr><td>Platform A No Piggybacking</td><td> $\Pi_A(0,0), \Pi_B(0,0)$ </td><td> $\Pi_A(0,1), \Pi_B(0,1)$ </td></tr><tr><td>Platform A No Piggybacking</td><td> $\Pi_A(1,0), \Pi_B(1,0)$ </td><td> $\Pi_A(1,1), \Pi_B(1,1)$ </td></tr></table>

Platform A’s pro<sup>fi</sup>t function under each outcome is given in Lemmas 1–3:

$$
\begin{array}{r l} & {\Pi_ {A} (0, 0) = \frac {1}{4} (2 t - T _ {2}),} \\ & {\Pi_ {A} (0, 1) = \frac {(2 t - T _ {2}) ((2 n + 3) t - 2 (n + 1) T _ {3}) ^ {2}}{4 (3 t - 2 T _ {3}) ^ {2}},} \\ & {\Pi_ {A} (1, 0) = \frac {(2 t - T _ {2}) ((4 n + 3) t - 2 (n + 1) T _ {3}) ^ {2}}{4 (3 t - 2 T _ {3}) ^ {2}} - c _ {A},} \\ & {\Pi_ {A} (1, 1) = \frac {1}{4} (2 n + 1) ^ {2} (2 t - T _ {2}) - c _ {A}.} \end{array}
$$

The pro<sup>fi</sup>t functions for platform B are symmetric. A Nash equilibrium exists if neither platform deviates from it. For example, for $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$ to be a Nash equilibrium, we need the following inequalities:

$$
\begin{array}{l} \Pi_ {A} (0, 0) <   \Pi_ {A} (1, 0) \Rightarrow c _ {A} <   \tilde {c} _ {2} \\ \qquad = \frac {n (2 t - T _ {1}) (2 t - T _ {3}) ((n + 3) t - (n + 2) T _ {1})}{(3 t - 2 T _ {3}) ^ {2}}; \\ \Pi_ {B} (1, 1) \leq \Pi_ {B} (1, 0) \Rightarrow c _ {B} \geq \tilde {c} _ {1} \\ \qquad = \frac {n (2 t - T _ {3}) (2 t - T _ {2}) (n (4 t - 3 T _ {1}) + 3 t - 2 T _ {1})}{(3 t - 2 T _ {3}) ^ {2}} \end{array}
$$

Under these conditions, neither platform deviates from $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$ . Using a similar approach, we can show the following conditions:

$$
\begin{array}{l} \text {a.} \{c _ {A} \geq \tilde {c} _ {2}, c _ {B} \geq \tilde {c} _ {2} \} \Rightarrow \{\mathbb {I} _ {A} = 0, \mathbb {I} _ {B} = 0 \}. \\ \text {b.} \{c _ {A} <   \tilde {c} _ {1}, c _ {B} <   \tilde {c} _ {1} \} \Rightarrow \{\mathbb {I} _ {A} = 1, \mathbb {I} _ {B} = 1 \}. \\ \text {c.} \{c _ {A} \geq \tilde {c} _ {1}, c _ {B} <   \tilde {c} _ {2} \} \Rightarrow \{\mathbb {I} _ {A} = 0, \mathbb {I} _ {B} = 1 \}. \end{array}
$$

The feasibility of the equilibrium now depends on the regions of $c _ { A }$ and $c _ { B } .$ For example, if $c _ { A } \geq \widetilde c _ { 1 }$ and $c _ { B } < \tilde { c } _ { 2 }$ do not coexist, then $\left\{ \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 1 \right\}$ is not a feasible equilibrium. To check the feasibility, we split the discussion into two cases: $t \geq T _ { 1 }$ and $t < T _ { 1 }$

Case 1: $t \geq T _ { 1 }$ . Under $t \ge T _ { 1 } , \tilde { c } _ { 1 } \ge \tilde { c } _ { 2 }$ always holds for all $\begin{array} { r } { n \leq \frac { 1 } { / } , } \end{array}$ which implies $\{ c _ { A } \ge \tilde { c } _ { 1 } , c _ { B } < \tilde { c } _ { 2 } \}$ is impossible. There are six subcases in total.

Subcase $1 - 1 \colon c _ { A } < \tilde { c } _ { 2 } \leq \tilde { c } _ { 1 }$ and $c _ { B } < \tilde { c } _ { 2 } \leq \tilde { c } _ { 1 }$ : This subcase satis<sup>fi</sup>es $\{ c _ { A } < \widetilde { c } _ { 1 } , c _ { B } < \widetilde { c } _ { 1 } \}$ , and the equilibrium is then $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$

Subcase $\lfloor - 2 \colon c _ { A } < \tilde { c } _ { 2 } \leq \tilde { c } _ { 1 }$ and $\tilde { c } _ { 2 } \leq c _ { B } < \tilde { c } _ { 1 } :$ : This subcase satis<sup>fi</sup>es $\{ c _ { A } < \widetilde { c } _ { 1 } , c _ { B } < \widetilde { c } _ { 1 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$

Subcase $1 { - } 3 \colon c _ { A } < \tilde { c } _ { 2 } \leq \tilde { c } _ { 1 }$ and $\tilde { c } _ { 1 } \leq c _ { B } \colon$ This subcase satis<sup>fi</sup>es $\{ c _ { A } < \widetilde { c } _ { 2 } , \widetilde { c } _ { 1 } \leq c _ { B } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$

Subcase 1-4: $\tilde { c } _ { 2 } \leq c _ { A } < \tilde { c } _ { 1 }$ and $\tilde { c } _ { 2 } \leq c _ { B } < \tilde { c } _ { 1 } ;$ : This subcase satis<sup>fi</sup>es both $\{ c _ { A } < \widetilde { c } _ { 1 } , c _ { B } < \widetilde { c } _ { 1 } \}$ and $\{ c _ { A } \ge \tilde { c } _ { 2 } , c _ { B } \ge \tilde { c } _ { 2 } \}$ . However, both platforms are better off with $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$ . Applying the Pareto principle, the feasible equilibrium is $\left\{ \mathbb { I } _ { A } ^ { \smile } = 1 , \mathbb { I } _ { B } = 1 \right\}$

Subcase 1-5: $\tilde { c } _ { 2 } \leq c _ { A } < \tilde { c } _ { 1 }$ and $\tilde { c } _ { 1 } \leq c _ { B } \colon$ This subcase satis<sup>fi</sup>es $\{ c _ { A } \ge \tilde { c } _ { 2 } , c _ { B } \ge \tilde { c } _ { 2 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 0 \right\}$

Subcase $1 \ – 6 \colon \tilde { c } _ { 2 } \leq \tilde { c } _ { 1 } \leq c _ { A }$ and $\tilde { c } _ { 2 } \leq \tilde { c } _ { 1 } \leq c _ { B } \colon$ This subcase satis<sup>fi</sup>es $\left\{ c _ { A } \ge \tilde { c } _ { 2 } , c _ { B } \ge \tilde { c } _ { 2 } \right\}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 0 \right\}$ Case $2 \colon t < T _ { 1 }$ . Under $t < T _ { 1 } , \tilde { c } _ { 1 } < \tilde { c } _ { 2 }$ always holds for all $\begin{array} { r } { n \leq \frac { 1 } { 2 } . } \end{array}$ There are six subcases.

Subcase $2 \ – 1 \colon c _ { A } < \tilde { c } _ { 1 } \leq \tilde { c } _ { 2 }$ and $c _ { B } < \widetilde { c } _ { 1 } \le \widetilde { c } _ { 2 } ;$ : This subcase satis<sup>fi</sup>es $\{ c _ { A } < \widetilde { c } _ { 1 } , c _ { B } < \widetilde { c } _ { 1 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$

Subcase $2 { - } 2 \colon c _ { A } < \tilde { c } _ { 1 } \leq \tilde { c } _ { 2 }$ and $\tilde { c } _ { 1 } \leq c _ { B } < \tilde { c } _ { 2 } \colon$ This subcase satis<sup>fi</sup>es $\{ c _ { A } < \tilde { c } _ { 2 } , c _ { B } \geq \tilde { c } _ { 1 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$

Subcase $2 \ – 3 \colon c _ { A } < \tilde { c } _ { 1 } \leq \tilde { c } _ { 2 }$ and $\tilde { c } _ { 1 } < \tilde { c } _ { 2 } \leq c _ { B } :$ This subcase satis<sup>fi</sup>es $\{ c _ { A } < \tilde { c } _ { 2 } , c _ { B } \geq \tilde { c } _ { 1 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$

Subcase 2-4: $\tilde { c } _ { 1 } \leq c _ { A } < \tilde { c } _ { 2 }$ and $\tilde { c } _ { 1 } \leq c _ { B } < \tilde { c } _ { 2 } \colon$ This subscase satis<sup>fi</sup>es both $\left\{ c _ { A } < \tilde { c } _ { 2 } , c _ { B } \geq \tilde { c } _ { 1 } \right\}$ and $\left\{ c _ { A } \ge c _ { 1 } , c _ { B } < c _ { 2 } \right\}$ . There are two possible pure-strategy Nash equilibria.

Subcase $2 { - } 5 \colon \tilde { c } _ { 1 } \leq c _ { A } < \tilde { c } _ { 2 }$ and $\tilde { c } _ { 1 } < \tilde { c } _ { 2 } \leq c _ { B } \colon$ This subcase satis<sup>fi</sup>es $\{ c _ { A } < \widetilde { c } _ { 2 } , c _ { B } \geq \widetilde { c } _ { 2 } \} ,$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 0 \right\}$

Subcase $2 \ – 6 \colon \tilde { c } _ { 1 } \leq \tilde { c } _ { 2 } \leq c _ { A }$ and $\tilde { c } _ { 1 } < \tilde { c } _ { 2 } \leq c _ { B } \colon$ This subcase satis<sup>fi</sup>es $\{ c _ { A } \ge \tilde { c } _ { 2 } , c _ { B } \ge \tilde { c } _ { 2 } \}$ , and the equilibrium is $\left\{ \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 0 \right\}$

Proposition 1 can be obtained by summarizing this analysis. w

Proof of Corollary 4. We identify a prisoner’s dilemma by two conditions. First, piggybacking is the dominating strategy for both platforms. Second, both platforms can be better off if they choose not to piggyback simultaneously. Note

$$
\alpha \geq \sqrt {4 t + 3 \beta^ {2}} -
$$

$$
2 \beta , c _ {A} <   \tilde {c} _ {1}
$$

$$
c _ {B} <   \tilde {c} _ {1}
$$

$$
\left\{\mathbb {I} _ {A} = 1, \mathbb {I} _ {B} = 1 \right\}
$$

If the two platforms choose a different strategy, the payoffs are $\{ \Pi _ { A } ( 0 , \bar { 0 } ) , \Pi _ { B } ( 0 , 0 ) \}$ . For platform $k \in \{ A , B \bar  \}$ , we have

$$
\Pi_ {k} (0, 0) - \Pi_ {k} (1, 1) = c _ {k} - n (n + 1) (2 t - T _ {2}).
$$

Note that $\tilde { c } _ { 3 } = n ( n + 1 ) ( 2 t - T _ { 2 } )$ . Platforms are better off by switching from $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$ to $\left\{ \mathbb { I } _ { A } = 0 , \mathbb { I } _ { B } = 0 \right\}$ when $c _ { k } \geq \tilde { c } _ { 3 }$ . In other words, for $c _ { k } \in ( \widetilde { c } _ { 3 } , \widetilde { c } _ { 1 } )$ , the Nash equilibrium $\left\{ \mathbb { I } _ { A } = 1 , \mathbb { I } _ { B } = 1 \right\}$ is a prisoners’ dilemma. Further, it can be shown that $\tilde { c } _ { 3 } < \tilde { c } _ { 1 }$ holds iff $\alpha \geq { \sqrt { 4 t + 3 \beta ^ { 2 } } } - 2 \beta ~ { \mathrm { ( i . e . } } ,$ regions I-$2 , \ \Pi { - } 2 , \ \Pi \Pi )$ . Given that the necessary and suf<sup>fi</sup>cient condition for subsidizing consumers is $\alpha \geq \bar { \alpha } ( \mathrm { i . e . }$ , region III), which implies that $\tilde { c } _ { 3 } < \tilde { c } _ { 1 }$ always holds if platforms subsidize consumers (i.e., the only overlapping region, region III), it proves Corollary 4a. Corollary 4b can be shown in a similar way for region I-2. w

Proof of Lemma 4. a. When both platforms engage in piggybacking, it can be veri<sup>fi</sup>ed again that a symmetric and unique equilibrium exists. Solving the following FOCs gives the equilibrium prices under multihoming piggybacking providers.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {- \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d} + p _ {B} ^ {c} + \beta p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {- (\alpha + \beta) p _ {A} ^ {c} + p _ {A} ^ {d} (2 \alpha \beta - 4 t) + \alpha \left(p _ {B} ^ {c} + \beta p _ {B} ^ {d}\right) + (\alpha + 4 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {- \alpha \beta + p _ {A} ^ {c} + \beta p _ {A} ^ {d} - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha p _ {A} ^ {c} + \alpha \beta p _ {A} ^ {d} - (\alpha + \beta) p _ {B} ^ {c} + 2 \alpha \beta p _ {B} ^ {d} - 4 t p _ {B} ^ {d} + (\alpha + 4 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0. \end{array}
$$

Similarly, solving the following FOCs gives the equilibrium prices under single-homing piggybacking providers.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {- \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d} + p _ {B} ^ {c} + \beta p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {- (\alpha + \beta) p _ {A} ^ {c} + p _ {A} ^ {d} (2 \alpha \beta - 4 t) + \alpha \left(p _ {B} ^ {c} + \beta p _ {B} ^ {d}\right) + (\alpha + 2 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {- \alpha \beta + p _ {A} ^ {c} + \beta p _ {A} ^ {d} - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha p _ {A} ^ {c} + \alpha \beta p _ {A} ^ {d} - (\alpha + \beta) p _ {B} ^ {c} + 2 \alpha \beta p _ {B} ^ {d} - 4 t p _ {B} ^ {d} + (\alpha + 2 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0. \end{array}
$$

b. When platform A alone engages in piggybacking, we focus on the nontrivial cases in which both platforms remain in the market. A symmetric and unique equilibrium exists. Solving the following FOCs gives the equilibrium prices under multihoming piggybacking providers.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {- \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d} + p _ {B} ^ {c} + \beta p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {- (\alpha + \beta) p _ {A} ^ {c} + p _ {A} ^ {d} (2 \alpha \beta - 4 t) + \alpha \left(p _ {B} ^ {c} + \beta p _ {B} ^ {d}\right) + (\alpha + 2 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {- \alpha \beta + p _ {A} ^ {c} + \beta p _ {A} ^ {d} - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d} + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha p _ {A} ^ {c} + \alpha \beta p _ {A} ^ {d} - (\alpha + \beta) p _ {B} ^ {c} + 2 \alpha \beta p _ {B} ^ {d} - 4 t p _ {B} ^ {d} + (\alpha + 2 n) (t - \alpha \beta)}{2 (t - \alpha \beta)} = 0. \end{array}
$$

Solving the following FOCs gives the equilibrium prices under single-homing piggybacking providers.

$$
\begin{array}{l} \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {c}} = \frac {- \alpha \beta - 2 p _ {A} ^ {c} - (\alpha + \beta) p _ {A} ^ {d} + p _ {B} ^ {c} + \beta p _ {B} ^ {d} + \beta n + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {A}}{\partial p _ {A} ^ {d}} = \frac {- (\alpha + \beta) p _ {A} ^ {c} + p _ {A} ^ {d} (2 \alpha \beta - 4 t) + \alpha (p _ {B} ^ {c} + \beta p _ {B} ^ {d}) - \alpha \beta (\alpha + n) + t (\alpha + 2 n)}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {c}} = \frac {p _ {A} ^ {c} + \beta p _ {A} ^ {d} - 2 p _ {B} ^ {c} - (\alpha + \beta) p _ {B} ^ {d} - \beta (\alpha + n) + t}{2 (t - \alpha \beta)} = 0, \\ \frac {\partial \Pi_ {B}}{\partial p _ {B} ^ {d}} = \frac {\alpha (p _ {A} ^ {c} + \beta p _ {A} ^ {d} - \beta (\alpha + n) + t) - (\alpha + \beta) p _ {B} ^ {c} + 2 p _ {B} ^ {d} (\alpha \beta - 2 t)}{2 (t - \alpha \beta)} = 0. \end{array}
$$

We de<sup>fi</sup>ne the following parameters:

$$
\begin{array}{l} \phi_ {1} = \frac {1}{4} \Bigg (\alpha - \frac {2 \left(\alpha^ {3} + 4 \alpha^ {2} \beta - 7 \alpha t + 2 \beta t\right)}{\alpha^ {2} + 4 \alpha \beta + \beta^ {2} - 6 t} \Bigg), \\ \phi_ {2} = \frac {(\alpha + \beta) (\alpha (\alpha + 3 \beta) - 4 t)}{\alpha (\alpha + 3 \beta) \left(\alpha^ {2} + 4 \alpha \beta + \beta^ {2} - 6 t\right)}, \\ \phi_ {3} = \frac {1}{4} \Bigg (3 - \frac {2 (\alpha (\alpha + 2 \beta) - 3 t)}{\alpha^ {2} + 4 \alpha \beta + \beta^ {2} - 6 t} \Bigg), \\ \phi_ {4} = \frac {\alpha + \beta}{4 \left(\alpha^ {2} + 4 \alpha \beta + \beta^ {2} - 6 t\right)}, \end{array}
$$

which are coef<sup>fi</sup>cients as shown in Table 6. w

Proof of Corollary 5. This proof follows steps similar to those in the proof of Corollary 4. We need to ensure that piggybacking is a dominating strategy although platforms are both better off without piggybacking. Solving all these conditions shows that a prisoner’s dilemma exists:

$$
\tilde {c} _ {4} = \frac {n ^ {2}}{4} \leq c _ {k} \leq \frac {n ^ {2}}{4} + \frac {1}{4} (2 t - T _ {2}) - \frac {(2 t - T _ {2}) (4 T _ {3} + n (\alpha + \beta) - 6 t) ^ {2}}{1 6 (2 T _ {2} - 3 t) ^ {2}} = \tilde {c} _ {5}.
$$

Note that these conditions are possible only for single-homing piggybacking providers and $n \leq 1 / 2$ . w

## Endnotes

<sup>1</sup> Please see https://venturebeat.com/2011/11/15/the-making-ofthe-xbox-part-2/.

<sup>2</sup> Please see https://techcrunch.com/2006/09/12/myspace-wedont-need-web-20/.

<sup>3</sup> Please see https://hbswk.hbs.edu/item/how-uber-airbnb-andetsy-attracted-their-<sup>fi</sup>rst-1-000-customers.

<sup>4</sup> For a more detailed review of piggybacking in platform practice, see Parker et al. (2016).

<sup>5</sup> In order to focus on our contribution on platform competition, in the spirit of a research note, we have compressed our literature review, and in particular, we have departed from the advertising literature as advertising is rarely studied in the platform competition literature (e.g., Rochet and Tirole 2003, Armstrong 2006). Although related, advertising is also not the same as piggybacking. For example, platform envelopment strategy (Eisenmann et al. 2011, Li and Agarwal 2016) is piggybacking (Fang et al. 2019) but not advertising. In any case, we leave advertising as an exciting future research opportunity as it can also poach consumers from the rival’s focal market. This direction is not piggybacking and, thus, is beyond the scope of this note.

<sup>6</sup> This assumption simply bounds the strength of the network effects. Similar assumptions are standard in the platform literature (e.g., see corollary 1 in Parker and Van Alstyne (2005) and equation 8 in Armstrong (2006)); otherwise, the optimal platform prices extend to in<sup>fi</sup>nity, which is trivial and not interesting.

<sup>7</sup> Proof omitted because of space constraints but available upon request.

<sup>8</sup> We thank an anonymous reviewer for this suggestion.

<sup>9</sup> Please see https://www.airbnb.com/help/article/2518/whyshould-i-agree-to-list-my-place-only-with-airbnb-plus.

<sup>10</sup> This can be shown by comparing platform A’s optimal prices in Tables 5 and 6.

<sup>11</sup> This can be shown by comparing platform B’s optimal prices in Table 6 when $\mathbb { I } _ { m } = 0 .$

<sup>12</sup> Please see https://www.nytimes.com/interactive/2019/11/13/ magazine/internet-china-wechat.html.

<sup>13</sup> Please see https://hbsp.harvard.edu/product/620040-PDF-ENG?Ntt=pinduoduo&itemFindingMethod=Search.

## References

Anderson E, Parker G, Tan B (2014) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25(1):152–172.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Bhargava H, Sundaresan S (2004) Computing as utility: Managing availability, commitment, and pricing through contingent bid auctions. J. Management Inform. Systems 21(2):201–227.

Bhuiyan J (2016) The global anti-Uber alliance just launched its newest international product. Vox (June 1), https://www.vox.com/ 2016/6/1/11820682/lyft-grab-antiuber-alliance-crossbookingsoutheastasia-us-uber.

Bolt W, Tieman A (2008) Heavily skewed pricing in two-sided markets. Internat. J. Indust. Organ. 26(5):1250–1255.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10):1849–1872.

Chellappa RK, Mukherjee R (2021) Platform preannouncement strategies: The strategic role of information in two-sided markets competition. Management Sci. 67(3):1527–1545.

Economides N, Tåg J (2012) Network neutrality on the internet: A two-sided market analysis. Inform. Econom. Policy 24(2):91–104.

Eisenmann T, Parker G, Van Alstyne M (2006) Strategies for twosided markets. Harvard Bus. Rev. 84(10):92–102.

Eisenmann T, Parker G, Van Alstyne M (2011) Platform envelopment. Strategic Management J. 32(12):1270–1285.

Fang TP, Wu A, Clough DR (2019) Hatching the platform ecosystem: Mobilizing complementors by creating social foci. Working paper, Wharton Business School, Philadelphia.

Gawer A, Cusumano M (2008) How companies become platform leaders. MIT Sloan Management Rev. 49(2):28–35.

Hagiu A (2009) Two-sided platforms: Product variety and pricing structures. J. Econom. Management Strategy 18(4):1011–1043.

Hagiu A, Eisenmann T (2007) A staged solution to the catch-22. Harvard Bus. Rev. 85(11):25–26.

Hagiu A, Hałaburda H (2014) Information and two-sided platform pro<sup>fi</sup>ts. Internat. J. Indust. Organ. 34:25–35.

Hagiu A, Spulber D (2013) First-party content and coordination in two-sided markets. Management Sci. 59(4):933–949.

Katz ML, Shapiro C (1992) Product introduction with network externalities. J. Indust. Econom. 40(1):55–83.

Lee D, Mendelson H (2007) Adoption of information technology under network effects. Inform. Systems Res. 18(4):395–413.

Li Z, Agarwal A (2016) Platform integration and demand spillovers in complementary markets: Evidence from

Facebook’s integration of Instagram. Management Sci. 63(10): 3438–3458.

Parker G, Van Alstyne M (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parker G, Van Alstyne M, Choudhary S (2016) Platform Revolution: How Network Markets Are Transforming the Economy and How to Make Them Work for You (W. W. Norton & Company, New York).

Rochet J, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet J, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Wang Q, Hui K (2017) Technology mergers and acquisitions in the presence of an installed base: A strategic analysis. Inform. Systems Res. 28(1):46–63.

Wright J (2004) One-sided logic in two-sided markets. Rev. Network Econom. 3(1):44–64.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
