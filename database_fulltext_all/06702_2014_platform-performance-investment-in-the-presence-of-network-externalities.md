---
otero_id: 6702
otero_key: "RUUXVFBE"
title: "Platform Performance Investment in the Presence of Network Externalities"
authors: "Edward G. Anderson; Geoffrey G. Parker; Burcu Tan"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0505"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/RUUXVFBE/fulltext/images/8d2ae4b6ba8aab149c359875a9e4b2b24986704404d8c961b4516d8a23d3ff40.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Platform Performance Investment in the Presence of Network Externalities

Edward G. Anderson Jr., Geoffrey G. Parker, Burcu Tan

To cite this article:

Edward G. Anderson Jr., Geoffrey G. Parker, Burcu Tan (2014) Platform Performance Investment in the Presence of Network Externalities. Information Systems Research 25(1):152-172. http://dx.doi.org/10.1287/isre.2013.0505

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/RUUXVFBE/fulltext/images/1df2b74ff599ab3234d4e94967aa0a2dd8865fc0d9e61a9a6b0461a4e2550893.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Platform Performance Investment in the Presence of Network Externalities

Edward G. Anderson, Jr.

University of Texas, Austin, Texas 78712, edward.anderson@mccombs.utexas.edu

Geoffrey G. Parker, Burcu Tan

A. B. Freeman School of Business, Tulane University, New Orleans, Louisiana 70118 {gparker@tulane.edu, btan@tulane.edu}

a selling point for consumers, but in many cases it requires developers to make large investments to participate. Abstracting from an example drawn from the video game industry, we build a strategic model to investigate the trade-off between investing in high platform performance versus reducing investment in order to facilitate third party content development. We carry out a full analysis of three distinct settings: monopoly, price-setting duopoly, and price-taking duopoly. We provide insights on the optimum investment in platform performance and demonstrate how conventional wisdom about product development may be misleading in the presence of strong cross-network externalities. In particular, we show that, contrary to the conventional wisdom about “winner-take-all” markets, heavily investing in the core performance of a platform does not always yield a competitive edge. We characterize the conditions under which offering a platform with lower performance but greater availability of content can be a winning strategy.

Keywords: two-sided markets; network externality; product development; video game industry History: Chris Dellarocas, Senior Editor; Chris Forman, Associate Editor. This paper was received August 26, 2011, and was with the authors 15 months for 2 revisions. Published online in Articles in Advance December 4, 2013.

## 1. Introduction

Platforms are economically important and widely observed in modern economies. Thanks largely to technology improvements, platforms are becoming even more prevalent as traditional businesses such as the U.S. Postal Service reconceive themselves as platforms (Parker and Van Alstyne 2012). In creating strategies for platform markets, however, managers have typically relied on assumptions and paradigms that apply to businesses without network effects. As a result, they have made decisions in pricing, supply chain, product design, and strategy that do not match the economics of their changing industries. An important implication is that firms that pursue traditional “product” strategies are increasingly at a disadvantage compared to firms that pursue “platform” strategies that offer core products and services that can be extended by an ecosystem of developers (Cusumano 2010).

A key decision in platform design is the level of platform performance to invest in at each product development cycle. In some cases, such as cloud based server technology, higher performance comes at little or no cost to the development community, whereas in other cases, such as video game platforms, higher performance often requires developers to make large investments to participate. In this paper we ground our exploration of platform performance in the 60-billion-dollar video game industry, whose great size, competitiveness, and economic importance provide a good setting for close study. However, the insights we develop are applicable across a range of very different platforms, including, as we argue below, one of the military aircraft industry’s most successful platforms, the F-16.

In the seventh generation of game consoles (Nintendo Wii, PS3, and Xbox 360), the market leader Nintendo Wii is particularly noteworthy for its success. The Wii entered the market later than its competitors. In an industry with network effects such foot dragging can put the product at a significant disadvantage (Arthur 1989, Katz and Shapiro 1994). To make matters worse, the Wii’s processing capabilities and graphics fell substantially below the bar set by PS3 and Xbox 360 (Allen 2006). Nonetheless, the Wii quickly obtained the biggest installed base among the three (Figure 1).

In widespread speculation about this exceptional performance, many attributed the Wii’s success to its motion-sensitive remote control, Wii Remote, which created a unique and intuitive gaming experience particularly welcoming to novice gamers. Yet, although this novel technology accounts in part for the platform’s popularity, the remote cannot fully explain Nintendo Wii’s dominance, because for a long time most of the games developed for the Wii used the traditional joystick controls, not the motion-sensitive technology (Kim 2007, Wen 2007).

Figure 1 Seventh Generation Video Game Consoles Cumulative Sales  
![](/api/attachments/RUUXVFBE/fulltext/images/1b560af35d4c1da74893266fa0234700263aeaaa31280153ac24c99c78a17058.jpg)  
Note. Data taken from vgchartz.com.

Ironically, the Wii’s lower-tech platform gave it the advantage on both the development and the retail fronts: Microsoft and Sony had increased the performance of their platforms by almost an order of magnitude from the sixth generation. However, as performance increases, polygons per second increases, which raises the art costs. Indeed, a series of interviews conducted with game developers by Anderson and Parker (2008) indicated that a significant cost increase accompanied the introduction of the seventh generation game platforms, as one video game developer explained,

The driver [of cost increase] is the growth of [seventh] generation platforms because the possibilities are much more than they used to be, so a lot more resources are required.

In contrast, because its processing and graphical capabilities are not much different from sixth generation technology, developing games for the Wii turned out to be significantly cheaper than for other platforms (Leheng 2006, Sinclair 2006). As Brian Farrell, CEO of prominent game developer and publisher THQ Inc., points out, this economic wiggle room made the Wii platform attractive for game developers:

One of the things we like about the Wii is that development costs are nowhere near what they are on the PS3 and Xbox 360. (0 0 0) The Wii wasn’t a whole new programming environment. So we had a lot of tools and tech that work in that environment. So those costs could be as little as a third of the high-end next-gen titles. (Sinclair 2006).

As a result of these reduced development costs, Nintendo was able to guarantee some highly rated games such as Zelda2 Twilight Princess and WarioWare2 Smooth Moves right at the launch of the Wii (Wesley and Barczak 2010). Further, despite its late release, the Wii quickly secured more game titles than its competitors (VG Chartz Game Database 2009), playing on the industry truism that a diverse variety of game titles makes a game console more attractive in the eye of a gamer. In turn, a bigger installed base of gamers attracts game developers with the anticipation of higher sales, completing the virtuous cycle. These cross-network effects are critical determinants of the fate of a game console, and they have worked out quite favorably for the Wii.

To explore the reasons for the Wii’s market leadership in particular, and to suggest more general themes for technological strategy across platforms, this paper investigates an important factor in new product development: the choice between investing in platform performance or holding back investment to facilitate third party content development in markets that exhibit two-sided network externalities. Wii’s story reveals that even though superior performance such as improved graphics is a selling point for gamers, the level of technological complexity required for that virtuosity may increase game development costs and thus hinder game development efforts. One game developer in the aforementioned interviews (Anderson and Parker 2008) cited the steep learning curve that accompanies platform upgrades:

Hardware changes: Those years are horrendous for software developers in the game industry. We’ve got to learn a new set of capabilities. And, we’re still on the 12 month cycle. Every time there’s a new hardware generation, we have huge struggles making it work.

Indeed, at every new generation, the video game industry has pushed the performance frontier and the resulting hardware changes made content development more difficult.

Further, gamers may be less interested in seriously ramped-up graphics than the industry assumes (Sheffield 2008). Thus, console manufacturers who favor upgrading technology over facilitating third party content development may be overinvesting in the core performance of their platforms. Indeed, van der Rhee et al. (2007) suggest that steepening the performance treadmill is not always the best strategy in a competitive market. But how should a console manufacturer balance gamers’ preferences with game developers’ needs to fully benefit from cross-network externalities? In general, how should platform sponsors resolve this performance trade-off?

To gain intuition into platform development tradeoffs, we examine the choice of platform performance level to invest in at each product development cycle. We use the term “performance” to represent a vertically differentiated dimension of quality (Mussa and Rosen 1978). For video game consoles, better graphics and better processing capabilities imply higher performance. We characterize the investment decisions of platform sponsors in a context where higher performance makes third party content development more costly, either directly as we observe in video game platforms or indirectly through the draining of resources that could have been used to improve third party development capabilities. We carry out a full analysis of three distinct settings: monopoly, pricesetting duopoly, and price-taking duopoly. We provide insights on the optimum investment in platform performance in each context and show that conventional wisdom about product development may be misleading in the presence of strong cross-network externalities.

In particular, we characterize market attractiveness for developers in a monopolistic market and show that if it is high, the platform monopolist may be better off increasing investment in performance in the face of increasing end user interest in platform content, contrary to the intuition that performance should be cut back to attract more developers. We demonstrate that high performance and high price do not always go in tandem. For example, after increasing royalty rates, the monopolist may have to reduce the platform price even as she provides a higher performance platform if she is to attract enough end users to keep the developer community intact. For the price-taking duopoly, we characterize a platform market as content driven or performance driven and discuss how conventional wisdom could mislead a platform sponsor especially in content-driven markets. For instance, in a one-sided market if competition between two firms intensifies, investment likely will be directed to increasing the performance of the product. However, we show that in a content-driven two-sided market, platform sponsors may be better off decreasing investment in platform performance to provide greater content availability. Indeed, even when end users show increasing interest in platform performance, sponsors in a content-driven market gain an edge through less aggressive investment in platform performance. More important, we show that when platforms are price takers, a platform with inferior performance can still capture a bigger market share on both sides of the market, just as the Wii did. In other words, making the greatest investment in technology is not the only way to be the winning platform. In certain markets, particularly those with high end user interest in content availability, the key to success is in superior mobilization of third party developers.

Throughout the paper, we use the video game industry as a motivating example. Nonetheless, the model is applicable to other hardware/software platforms that exhibit cross-side network effects. For example, military aircraft are platform systems whose capabilities can be increased through the addition of third party systems such as avionics packages, engine upgrades, and external peripherals like attachment points for cruise missiles and reconnaissance cameras. A platform, such as the F-16, that has a robust community of developers can thrive long after the basic airframe has become obsolete (Tirpak 2007). Conversely, older aircraft platforms that do not support a robust supplier base face increasing cost and reduced performance (Jones and Zsidisin 2008). Similar to video games, however, new platform introductions can lead to significant problems for developers. For example, consider the development of “stealth” airframes that diffuse radar signals to make the aircraft harder to detect. Although end users value this technology, it causes significant expense for the developers of add-ons because they must follow new stealth design guidelines that have nothing to do with the plane’s added functionality. Because of this additional expense, fewer additional features are available at reasonable expense, so the total platform system appeals mainly to those end users who highly value the stealth technology.

The remainder of the paper proceeds as follows. Section 2 reviews the related literature. In §3, we develop a mathematical model of a platform monopolist who manages cross-network effects by optimizing platform performance and price. In §4 we build on the monopoly model to analyze two competing platforms. Specifically, §4.1 focuses on a price-setting (PS) duopoly whereas §4.2 analyzes an industry structure with price-taker platforms. We discuss the limitations of our model and its possible extensions in §5. Finally, §6 summarizes our results and concludes the paper.

## 2. Literature Review

The economic theory of two-sided markets (Parker and Van Alstyne 2000b, Rochet and Tirole 2003, Parker and Van Alstyne 2005) explores the unique features that set these markets apart from traditional products and services. In particular, two-sided markets exhibit a special form of indirect network effects (Katz and Shapiro 1985, Liebowitz and Margolis 1994) such that the number of users on one side of the market depends on the number of users on the other side. For example, video game developers will develop games only for platforms that have a sufficiently broad installed base of gamers. Likewise, all else being equal, gamers prefer platforms that provide a greater variety of games. These cross-side network effects allow a platform sponsor to subsidize one side of the market in order to attract the other side (Eisenmann et al. 2006).

The growing literature on two-sided markets has mostly focused on platform sponsors’ novel twosided pricing strategies (Parker and Van Alstyne 2000a, 2005; Armstrong 2006; Caillaud and Jullien 2003; Hagiu 2006; Rochet and Tirole 2003, 2006). Specifically, Parker and Van Alstyne (2000a, b, 2005) characterize the pricing structure of a monopolist platform and show that either side of the market may be subsidized depending on the relative network externality benefits. Rochet and Tirole (2003) develop two-sided pricing strategies for a wide range of governance structures including competing profit and nonprofit platforms. Similarly, Armstrong (2006) analyzes both monopolistic and competing platforms, and shows that the pricing structure depends on the relative strengths of cross-side network effects, the fee structure, and whether the agents are able to join more than one platform. All of these studies provide valuable insights on the role of pricing strategy in capturing demand on both sides of the market.

Relatively little work has been done to explore the use of nonprice controls in two-sided markets. Though a recent body of work discusses the nonprice levers platform sponsors can use to create more attractive bundles for end users (Gawer and

Cusumano 2002, Boudreau and Hagiu 2008, Parker and Van Alstyne 2013, Eisenmann et al. 2011), the role of platform characteristics such as platform features and performance has yet to be fully explored (Tiwana et al. 2010). Some of the few studies that address these product development issues in two-sided markets include Bhargava and Choudhary’s (2004) analysis of the product line design problem of an information intermediary. They show that when the buyers have constant marginal valuations for the service quality, versioning is optimal. In a study that is closer to this paper, Zhu and Iansiti (2011) consider two platforms, an incumbent and an entrant, competing on the basis of platform quality and installed base. The authors analyze a dynamic game and show that installed base does not necessarily present barriers to entry. Our paper, on the other hand, addresses product development in two-sided markets, with particular emphasis on the ways that investment in platform performance in the presence of cross-side network effects differs from product development strategies in the absence of these effects.

The effect of network externalities on R&D investment has long been studied in the economics literature with particular emphasis on compatibility and standardization (Katz and Shapiro 1985, 1986a, b, 1994; Farrell and Saloner 1985, 1986; Choi 1994; Kristiansen 1998). Yet this stream of research typically studies direct network effects, ignoring the strategic interactions with the developer side of the market. We also draw on a substantial body of product development research that investigates the role of product characteristics in one-sided markets. Marketing-based studies in this literature have extensively analyzed how to determine the target values of attributes of a product (reviewed by Green and Srinivasan 1990), and studies based on operations management (reviewed by Papalambros 1995) have focused on determining the design parameters that will optimize product performance (For a broader view of the product development research, we refer the reader to the survey papers in this area such as Krishnan and Ulrich 2001, and Shane and Ulrich 2004). Our paper brings together product development and two-sided markets literatures by analyzing a platform sponsor’s investment in platform performance as a nonprice control to “get the two sides on board.”

Finally, we draw on another burgeoning stream of research that empirically measures the size of indirect network effects, particularly in high-technology industries such as CD players (Basu et al. 2003, Gandal et al. 2000), video games (Clements and Ohashi 2005, Srinivasan and Venkatraman 2010, Gretz 2010), and personal digital assistants (Nair et al. 2004). Of perhaps greatest relevance to this paper is Nair et al. (2004), who look at the trade-off between improving hardware attributes and increasing software availability for PDAs. For example, they measure how many additional software titles would be needed to increase the installed base as much as a particular improvement in the hardware. Similarly, Gretz (2010) empirically measures the relative sensitivity of software availability to hardware quality and installed consumer base, finding the impact of the former to be larger. Our paper complements this stream of research by using an analytical model to characterize the equilibrium investment in hardware performance and to establish when to concentrate investments on third party development instead.

## 3. Monopoly

In this section, we develop and analyze the twosided market model that we use to analyze platform performance investment decisions in the presence of cross-network externalities. As discussed above, we develop model features using the video game industry as motivation, but the model is applicable to other industries in which platforms seek to attract an ecosystem of developers and where platforms must make investment decisions that take end users and developers’ preferences into account. In line with the previous literature on two-sided markets, we use the terms end user, content developer, and platform sponsor to correspond to gamers, game developers, and game console providers, respectively. Table 1 summarizes the notation used in the model.

Extending Parker and Van Alstyne (2005), we divide the value an end user obtains from purchasing a platform into three additive components: available content $( N _ { D } )$ , platform performance (), and the base value of the platform before add-ons (v). Each component has a certain weight in an end user’s decision. Let  be an end user’s utility from an additional unit of content and $\gamma$ be an end user’s utility from an additional unit of performance.<sup>1</sup>

We conceive of  inclusive of content price; that is $\alpha N _ { D }$ is the net benefit from content availability, where $N _ { D }$ is the number of developers that develop for the platform.

An alternate specification would model end user utility in a multiplicative form, as in Rochet and Tirole (2003). This model fits a setting of necessary complements such that a platform has no value in the absence of a developer community. However, in our setting and similar to Gawer and Cusumano (2008), Parker and Van Alstyne (2009), and Cusumano (2010), platforms offer users a core set of functions that can be extended by an ecosystem of developers. In the video game console context, core functionality provided by the platform includes features such as DVD playback and media streaming that may give some users enough utility to justify platform purchase even in the absence of developer content. Interestingly, from an optimization point of view, the additive and multiplicative forms are very similar because optimization of the multiplicative model takes place on log linear model elements. Parker and Van Alstyne (2005) show that the optimal price structure of a general demand model is identical for both additive and multiplicative specifications of a two-sided model.

We assume that end users differ in their marginal utility from the base value of the platform. In particular, each end user is characterized by her ${ \tilde { v } } ,$ utility from intrinsic value. Thus, the utility that an end user with intrinsic value v enjoys by purchasing the platform is given as

$$
U (v) = v + \alpha N _ {D} + \gamma \phi - p,\tag{1}
$$

where $p$ is the price of the platform. Note that under our assumptions $\phi = 0$ corresponds to the minimum level of platform performance that the market would bear.

Let $v ^ { * }$ be the end user who is indifferent between purchasing and not. By normalizing the opportunity cost to zero, $v ^ { * }$ is given by $v ^ { * } = p - \alpha N _ { D } - \gamma \phi$ . End users with $v \geq v ^ { * }$ will purchase the platform. If we assume that v is uniformly distributed over $[ 0 , V ] ,$ , we can calculate the participation rate of end users as $( V - v ^ { * } ) / V . ^ { 2 }$ We assume that there are $M _ { G }$ end users in the market. Thus, the number of end users that purchase the platform, $N _ { G }$ is given by

$$
N _ {G} (\phi , p, N _ {D}) = M _ {G} \frac {V + \alpha N _ {D} + \gamma \phi - p}{V}.\tag{2}
$$

Content developers are assumed to be profit maximizers. From each unit of content sold, a content developer earns $g$ but has to pay r as royalty to the platform sponsor, where $g > r .$ We assume that content developers have local monopolies for their titles and hence each set price at $g .$ Indeed, in the video game industry, games are sold at more or less the same price around the release date irrespective of the developer and the console they are developed for. Without loss of generality, we assume that end users purchase every unit of content developed for the platform;<sup>3</sup> thus the revenue of a content developer is given by $N _ { G } ( g - r )$

Table 1 Notation

<table><tr><td colspan="2">Decision variables</td></tr><tr><td> $\phi_i$ </td><td>Performance of platform i</td></tr><tr><td> $p_i$ </td><td>End user price of platform i</td></tr><tr><td colspan="2">Market primitives</td></tr><tr><td>α</td><td>End users&#x27; net utility from an additional unit of content available</td></tr><tr><td>γ</td><td>End users&#x27; utility from an additional unit of platform performance</td></tr><tr><td>V</td><td>Maximum standalone value for the platform</td></tr><tr><td> $M_G$ </td><td>Total number of end users in the market</td></tr><tr><td>r</td><td>Royalty per content sold</td></tr><tr><td>g</td><td>Content price (g &gt; r)</td></tr><tr><td>β</td><td>Content development cost per unit performance</td></tr><tr><td>F</td><td>Maximum fixed cost incurred by developers</td></tr><tr><td> $M_D$ </td><td>Total number of developers in the market</td></tr><tr><td>K</td><td>Platform development cost per unit performance squared</td></tr><tr><td>c</td><td>Marginal cost of platform production</td></tr><tr><td>t</td><td>Degree of platform differentiation on the end user market</td></tr><tr><td colspan="2">Derived quantities</td></tr><tr><td> $D_i$ </td><td>End user market share of platform i</td></tr><tr><td> $N_G^i$ </td><td>Number of end users that purchase platform i</td></tr><tr><td> $N_D^i$ </td><td>Number of developers that join platform i</td></tr><tr><td>L</td><td>Performance threshold level ( $L = F\gamma - M_D\beta(\alpha + r)$ )</td></tr><tr><td> $L_{PT}$ </td><td>Net value of platform performance for the price-taker platform ( $L_{PT} = F\gamma - M_D\alpha\beta$ )</td></tr><tr><td>A</td><td>Market attractiveness for developers ( $A = M_G(g - r)\gamma - V\beta$ )</td></tr><tr><td> $A_{PT}$ </td><td>Market attractiveness for developers under platform competition ( $A_{PT} = M_G(g - r)\gamma - t\beta$ )</td></tr><tr><td>χ</td><td>Market competitiveness ( $\chi = M_D M_G\alpha(g - r) - Ft$ )</td></tr></table>

Content developers incur a development cost that increases with the platform’s performance. This cost is modeled as $\beta \phi { \dot { + } } { \tilde { f } }$ , where $\beta$ is the cost of content development per unit performance. We assume that development cost varies from developer to developer as a result of differences in engineering efficiency. Specifically, while the performance dependent component $\beta \phi$ is the same across the developers, the fixed cost $\tilde { f }$ is assumed to be uniformly distributed on $[ 0 , F ] . ^ { 4 }$ Thus, by joining the platform, a content developer with fixed cost $f$ makes a profit of

$$
\Pi_ {D} (f) = N _ {G} (g - r) - \beta \phi - f.
$$

In addition to $f ,$ the cost of content development per unit performance, $\beta ,$ might differ from developer to developer. It would be straightforward to extend the current model by dividing developers into two types, high and low, where high type developers have a higher cost of content development per unit performance compared to the low type developers. However, the model insights do not change under this specification. Therefore, to keep the model parsimonious, we assume that developers have the same cost of content development per unit performance and aggregate developer heterogeneity in $f .$

By normalizing the opportunity cost to zero, the marginal developer $f ^ { * } ,$ who is indifferent between developing and not developing content for the platform is characterized by $f ^ {  } = N _ { G } ( g \mathrm { ~ - ~ } r ) \mathrm { ~ - ~ } \hat { \beta } \phi$ Accordingly, content developers with $f \leq f ^ { * }$ join the platform producing a participation rate of $f ^ { \ast } / F$ . Thus the number of content developers who join the platform is given by

$$
N _ {D} (\phi , p, N _ {G}) = \frac {M _ {D} (N _ {G} (g - r) - \beta \phi)}{F},
$$

(3)

where $M _ { D }$ is the total number of developers in the market. Solving (2) and (3) simultaneously for $N _ { D }$ and $N _ { G }$ yields the following market sizes as functions of the decisions variables:

$$
N _ {G} (\phi , p) = \frac {M _ {G} (\phi (F \gamma - M _ {D} \beta \alpha) + F (V - p))}{F V - M _ {D} M _ {G} (g - r) \alpha},\tag{4}
$$

$$
\begin{array}{l} N _ {D} (\phi , p) \\ = \frac {M _ {D} (M _ {G} (g - r) (V - p) + \phi (M _ {G} (g - r) \gamma - V \beta))}{F V - M _ {D} M _ {G} (g - r) \alpha}. \end{array}\tag{5}
$$

The platform enjoys two revenue streams: purchases of the platform by end users and royalties collected from content developers on each unit of content they sell to end users. The fixed cost of developing the platform is assumed to be a convex increasing function of platform performance given as $K \phi ^ { 2 }$ . For ease of exposition, the marginal cost of production, $c ,$ is assumed to be constant.<sup>5</sup> The platform monopolist chooses price $p$ and performance $\phi$ to maximize its profit. Accordingly, the decision problem is given by

$$
\begin{array}{l} \underset {\phi , p} {\text { maximize }} \Pi_ {m} (\phi , p) = (p - c) N _ {G} (\phi , p) \\ \qquad \qquad \qquad + r N _ {G} (\phi , p) N _ {D} (\phi , p) - K \phi^ {2}; \\ \text { s.t. } \phi \geq 0, \end{array}\tag{6}
$$

where $N _ { G } ( \phi , p )$ and $N _ { D } ( \phi , p )$ are given by (4) and (5), respectively. We introduce the following lemma to facilitate our analysis.

<sup>Lemma</sup> <sup>1.</sup> If the performance threshold $L = F \gamma -$ $M _ { D } \beta ( \alpha + r ) \geq 0 .$ , the platform monopolist chooses

$$
\begin{array}{c} \phi_ {m} ^ {*} = \frac {F M _ {G} (V - c) L}{4 F k (F V - M _ {D} M _ {G} (g - r) (\alpha + r)) - M _ {G} L ^ {2}} \\ p _ {m} ^ {*} = \left[ (V + c) (2 F k (F V - M _ {D} M _ {G} (g - r) \alpha) + M _ {D} M _ {G} r \beta \right. \\ \cdot (F \gamma - M _ {D} \beta \alpha)) - V M _ {D} M _ {G} r (4 F k (g - r) + M _ {D} r \beta^ {2}) \\ - c M _ {G} (F \gamma - M _ {D} \beta \alpha) ^ {2} ] \cdot \left[ 4 F k (F V - M _ {D} M _ {G} (g - r) \right. \\ \cdot (\alpha + r)) - M _ {G} L ^ {2} ] ^ {- 1}. \end{array}
$$

Otherwise, the monopolist chooses the minimum platform performance that the market would bear:

$$
\begin{array}{c} \phi_ {m} ^ {*} = 0 \\ p _ {m} ^ {*} = \frac {(V + c) (F V - M _ {D} M _ {G} (g - r) \alpha) - 2 V M _ {D} M _ {G} r (g - r)}{2 (F V - M _ {D} M _ {G} (g - r) (\alpha + r))}. \end{array}
$$

Lemma 1 states that the performance threshold level $L = F \gamma - M _ { D } \beta ( r + \alpha )$ must be positive to ensure a performance choice above the minimum level the market would bear. In other words, end users’ utility from platform performance must be relatively high or content development cost per unit performance must be relatively low for the monopolist to invest in platform performance. On the other hand, if end users tend to value content availability more than they value platform performance, or if content developers must incur a high content development cost per unit performance as well as a high royalty rate, a high platform performance is not valued in the two-sided market, leading the platform monopolist to provide the minimum platform performance.

The performance investment at equilibrium exhibits some compelling behavior that would not be observed in the absence of cross-side network effects. We collect some of these features in Proposition 1(i) and (ii) through comparative statics analysis. Proofs are provided in the appendix.

Proposition 1. <sub>Let</sub> $A = M _ { G } ( g - r ) \gamma - V \beta$ represent the market attractiveness for developers. Optimum performance choice $\phi _ { m } ^ { * }$ satisfies the following:

(i) $\phi _ { m } ^ { * }$ increases in end users’ utility from an additional unit of content available, , i $\bar { \cdot } A \geq \dot { M _ { G } } \dot { \beta } L ^ { 2 } / ( 4 F ^ { 2 } K )$

(ii) $\phi _ { m } ^ { * }$ increases in royalty rate, r, $i f ~ A \ge ( M _ { G } \beta L ^ { 2 } +$ 4F K ${ \breve { A _ { G } L ( \alpha + r ) ) } } / ( 4 F ^ { 2 } K )$

(iii) $\phi _ { m } ^ { * }$ always increases in end users’ utility from an additional unit of platform performance, $\gamma .$

(iv) $\phi _ { m } ^ { * }$ always decreases in content development cost per unit performance, $\beta .$

A useful construct to aid in understanding these results is the market attractiveness for developers measured by $A = M _ { G } ( g - r ) \gamma - V \beta$ . Market attractiveness for developers, $A ,$ is high if developer margin, $\boldsymbol { g } - \boldsymbol { r } ,$ is high or development cost per unit performance, $\beta ,$ is low. High end user utility from performance, , also increases the market attractiveness for developers, because with a high $\gamma ,$ the same level of performance attracts more end users, all else being equal. Thus, high A represents a developer-friendly market where high performance is valued.

When the end users’ utility from content availability increases, one would expect the platform monopolist to invest less in the performance of the platform so as to more content developers, which in turn attracts the end users. Proposition 1 part (i) shows that this response may not be ideal in a market characterized by high enough market attractiveness for developers (see Figure 2). In such markets, higher performance makes the platform significantly more attractive to end users, but does not increase the development cost for the developers too much because of the relatively low development cost per unit performance; hence the platform monopolist is better off increasing platform performance even when end users’ utility from content availability increases.

Part (ii) presents a similar result for the relation between the royalty rate and platform performance. When the developers have to pay a higher royalty rate, one would expect the optimum performance level to be lower so as to compensate for this increased fee. The top panel of Figure 3 represents this scenario. However we observe that if market attractiveness for developers is high enough, it may be optimal for the platform to instead increase performance. This strategy makes sense because, in such markets, it is possible to attract more end users by increasing platform performance, which in turn increases developers’ revenues to compensate for the higher costs associated with increased r and .

Interestingly, optimum price may move in the opposite direction from optimum performance when the royalty rate increases (Figure 3, middle panel). That is, price for the platform may go down even though platform performance increases. This decrease happens when market attractiveness for developers is high but  is not. In response to an increase in royalty rate, if  is not high enough, the platform monopolist should reduce the price even if she is providing a higher quality platform. The reason is that both higher royalty and higher performance deter developers, which in turn may reduce the end user demand. If the price is also increased, that can further deter the end users. Only in a market where the end users place a very high value on performance is it still optimum to increase the price in tandem with quality when royalty rate is increased (Figure 3, bottom panel).

Proposition 1 parts (iii) and (iv) are intuitive. If end users enjoy a higher utility from performance, the platform monopolist should invest more in platform performance. Even though a higher  increases developers’ costs, the higher customer demand it generates for the developers is enough to compensate for that loss. In contrast, if developers’ cost per unit performance increases, it is optimum to reduce the performance of the platform to induce developers to stay in the market. Even though a lower $\phi$ reduces the appeal of the platform for the end users, facilitating third party development compensates for that loss.

Figure 2 Depending on the Developer Community, the Platform’s Optimum Performance Level Can Increase or Decrease in End Users’ Preference for Content Availability  
![](/api/attachments/RUUXVFBE/fulltext/images/ae2f7ed5dc3e303e6b282a1b851fa6727b15596be385887ad4009b24ce4f29d7.jpg)

![](/api/attachments/RUUXVFBE/fulltext/images/af439a57fde304824849bd6995ecb9e931f6cc80a0f0f7e5bb3ec53de71f038c.jpg)  
Notes. $\beta = 0 . 0 0 5 , c = 0 . 2 , g = 1 , k = 2 , M _ { \delta } = 1 , M _ { D } = 1 , r = 0 . 0 1 , F = 2$ and V = 2. The left panel (high market attractiveness for developers) assumes  = 0046 with A = 004454. The right panel (low market attractiveness for developers) assumes  = 00001 with A = −0000901.

## 4. Competition

In this section, we study competition between two platforms, building on the model concepts developed in §3. We assume that content developers may choose to affiliate with more than one platform, or “multihome,” whereas end users purchase a single game console or “singlehome.” The assumption that content developers may multihome is based on the increase in the fraction of games that are released on more than one console, a trend that is anticipated to prevail as a result of the growing cost of game development (Corts and Lederman 2009). End users, in contrast, are assumed to singlehome because it is not very common to own more than one platform of the same generation. Further, it can be argued that as more developers produce multiplatform content, fewer end users will choose to multihome because the amount of content that is exclusive to a platform outside the end user’s access will be limited (Dutka 2009).

On the one hand, because they are able to multihome, content developers decide whether or not to join a platform independently from their participation decision for the other platform (ignoring any budget constraints). Thus, the developer demand is derived the same way as in §3:

$$
N _ {D} ^ {i} (\phi_ {i}, p _ {i}, \phi_ {- i}, p _ {- i}, N _ {G} ^ {i}, N _ {G} ^ {- i}) = \frac {M _ {D} (N _ {G} ^ {i} (g - r) - \beta \phi_ {i})}{F}.\tag{7}
$$

End users, on the other hand, must decide which platform to join, and thus create competition between the platforms to attract them. For ease of exposition, we assume that r and $g$ are the same for both platforms. Hence, the explicitly modeled dimensions of platform differentiation are platform performance $\phi _ { i }$ and end user price $p _ { i } \ ( i = 1 , 2 )$ . Depending on these attributes, platform i gets $N _ { G } ^ { i }$ end users and $N _ { D } ^ { i }$ developers 4i = 11 25. The prospect of these market sizes plays a major role in the platform choice of end users and content developers.

Similar to the monopoly model, end users gain utility from platform performance, content availability, and the standalone features of the platform. To differentiate agents, we assume that they have different preferences for each platform. These preferences can arise from multiple sources that include having a library of compatible content or belonging to a community that has adopted a specific platform. We substitute this distribution of preferences for the standalone heterogeneity in platform value in the monopoly model. In other words, keeping performance, price, and content availability the same, platforms would still have different appeals to each end user. Specifically, we use a common competitive market model, Hotelling’s linear city, to capture this effect. Individual end users have different tastes for the platform; these which are modeled as uniformly distributed along a unit interval and the platforms are located at the opposite ends of the interval. The higher the distance between an end user’s location and a platform, the bigger the disutility of unmatched preferences. Let t be the “transportation cost” parameter in the Hotelling model, which represents the degree of horizontal product differentiation between the platforms. Note that low t implies less product differentiation, and thus a higher degree of competition. Without loss of generality, assume that platform 1 is located at point 0, whereas platform 2 is located at point 1. Accordingly, the net utility from joining platform 1 for the end user x with taste $x \in [ 0 , 1 ]$ is $U _ { 1 } ( x ) = u _ { 1 } - t x ,$ where

Figure 3 Optimum Price and Performance Decisions May Move in Opposite Directions When Royalty Rate Changes  
![](/api/attachments/RUUXVFBE/fulltext/images/992446c9c7f1cbae04d0253cfc4cfdc8200f25659543f33975422bd4644fc0b9.jpg)  
Low market attractiveness for developers

![](/api/attachments/RUUXVFBE/fulltext/images/65cd9593920a88038360ea4600c4e94e9533c3aea447bf96684ced33af4b96a0.jpg)

![](/api/attachments/RUUXVFBE/fulltext/images/834ad35c1cc962a5698ae0bd7e2a4df09f12ec68ae68699969c12003deddd126.jpg)

![](/api/attachments/RUUXVFBE/fulltext/images/ab4ded2e05877dec9f075c4f3d64baa7c3da9bf5e3d6ec53dc29c6190f81bcf3.jpg)

High market attractiveness for developers, low -  
![](/api/attachments/RUUXVFBE/fulltext/images/09048b270cef3a761543369e975b0b7273b377b99b249e6bc7b3217e55d2c0d7.jpg)

![](/api/attachments/RUUXVFBE/fulltext/images/218b7553a356ad72ee999056d53cd9ac4dd1dd8b3ce85ebee5aee6c20c325e1a.jpg)  
High market attractiveness for developers, high -  
Notes.  = 0000011  = 00001, g = 003, c = 002, k = 2, M = 1, M = 1, F = 2 and V = 2. The upper panel assumes $\gamma = 0 . 0 0 1$ . The middle panel assumes  = 0088. The lower panel assumes  = 3.

$$
u _ {1} = v + \alpha N _ {D} ^ {1} + \gamma \phi_ {1} - p _ {1}.
$$

Note that the standalone value of the platform, v, is assumed to be the same across end users and across platforms.

By locating the marginal end user who is indifferent between the two platforms and using the fact that end users are uniformly distributed on a unit interval, the number of end users who join platform $i ( i = 1 , 2 )$ can be calculated as

$$
N _ {G} ^ {i} (\phi_ {i}, p _ {i}, \phi_ {- i}, p _ {- i}, N _ {D} ^ {i}, N _ {D} ^ {- i}) = M _ {G} \bigg (1 / 2 + \frac {u _ {i} - u _ {- i}}{2 t} \bigg).\tag{8}
$$

We substitute (7) into (8) to get

$$
\begin{array}{l} N _ {G} ^ {i} (\phi_ {i}, p _ {i}, \phi_ {- i}, p _ {- i}) \\ = \frac {M _ {G}}{2} \bigg (1 + \frac {(\phi_ {i} - \phi_ {- i}) (F \gamma - M _ {D} \alpha \beta) - F (p _ {i} - p _ {- i})}{F t - M _ {D} M _ {G} (g - r) \alpha} \bigg). \end{array}\tag{9}
$$

Further substituting (9) into (7), we get

$$
\begin{array}{l} N _ {D} ^ {i} (\phi_ {i}, p _ {i}, \phi_ {- i}, p _ {- i}) \\ = \frac {M _ {D} M _ {G} (g - r)}{2 F} \\ \cdot \left(1 + \frac {(\phi_ {i} - \phi_ {- i}) (F \gamma - M _ {D} \alpha \beta) - F (p _ {i} - p _ {- i})}{F t - M _ {D} M _ {G} (g - r) \alpha}\right) \\ - \frac {M _ {D} \beta \phi_ {i}}{F}. \end{array}\tag{10}
$$

Accordingly, platform sponsor $i ^ { \prime } \mathbf { s } \ ( i = 1 , 2 )$ decision problem is as follows:

$$
\begin{array}{r l} \underset {\phi_ {i}, p _ {i}} {\text { maximize }} & \Pi_ {i} (\phi_ {i}, p _ {i}; \phi_ {- i}, p _ {- i}) \\ & = (p _ {i} - c) N _ {G} ^ {i} + r N _ {G} ^ {i} N _ {D} ^ {i} - K \phi_ {i} ^ {2}; \\ \text { s.t. } & \phi_ {i} \geq 0, \end{array}\tag{11}
$$

where $N _ { G } ^ { i }$ and $N _ { D } ^ { i }$ are given by (9) and (10), respectively.

We assume that platforms enter the market simultaneously such that both platforms make their decisions without observing the competitor’s decisions. In §4.1 we analyze this decision problem, whereas in §4.2 we analyze an industry structure with price-taker platforms.

## 4.1. Price-Setting Duopoly

When two competing platform sponsors determine the end user price and the platform performance simultaneously, the price-setting equilibrium is symmetric with both platforms setting the end user price and platform performance specified in Lemma 2. Proofs and derivations appear in the appendix.

<sup>Lemma</sup> <sup>2.</sup> If the performance threshold $L = F \gamma -$ $M _ { D } \beta ( r + \alpha ) \stackrel { . } { \geq } 0 ,$ , platforms play the high performance equilibrium

$$
\begin{array}{c} \phi_ {P S} ^ {*} = \frac {M _ {G} L}{4 F K}, \\ p _ {P S} ^ {*} = c + t + \frac {M _ {D} r \beta}{F} \phi_ {P S} ^ {*} - \frac {M _ {D} M _ {G} (g - r) (\alpha + r)}{F}. \end{array}
$$

Otherwise, platforms play the low performance equilibrium:

$$
\phi_ {P S} ^ {*} = 0, \quad p _ {P S} ^ {*} = c + t - \frac {M _ {D} M _ {G} (g - r) (\alpha + r)}{F}.
$$

Note that the competing platforms change decisions at the same performance threshold as the monopolist: the average utility from performance  must exceed $M _ { D } \beta ( r + \alpha ) / F$ to make investment in performance attractive. Despite this remarkable similarity, the platform’s choice of performance in a competitive market differs from that of a monopolist in several ways. In particular, as shown in Corollary 1(i) and (ii), platform performance at equilibrium always decreases when end users’ utility from content,  or the royalty rate, r increases.

<sup>Corollary</sup> <sup>1.</sup> In a price-setting duopoly, the following holds for the platform performance at equilibrium:

(i) $\phi _ { P S } ^ { * }$ decreases with end users’ utility from an additional unit of content available, .

(ii) $\phi _ { P S } ^ { * }$ decreases with royalty rate, r.

(iii) $\phi _ { P S } ^ { * }$ increases with the end user utility from an additional unit of platform performance, $\gamma .$

(iv) $\phi _ { P S } ^ { * }$ decreases with content development cost per unit performance, $\beta .$

(v) $\phi _ { P S } ^ { * }$ does not depend on the intensity of competition in the end user market, t.

Although in certain markets a platform monopolist may find it profitable to increase platform performance when  increases, a price-setting platform under competition always adopts the more intuitive strategy and reduces performance investment. The intuitive strategy has merit: a lower $\phi$ implies lower development costs for both the platform and the developers. However, when competing platforms reduce  in response to an increase in $\alpha ,$ they end up aggressively cutting back the end user price in order to stay competitive as shown in Corollary 2. Ultimately this strategy competes away platform profits. In contrast, because the monopolist does not engage in a price war, she can allow an increase in platform performance to correspond to increasing profit. Indeed, Corollary 2 shows that the platform monopolist always increases her profit when end users’ utility from content availability increases, whereas in a duopoly, price competition always leaves platforms worse off.

<sup>Corollary</sup> <sup>2.</sup> In a symmetric duopoly, when end users’ utility from content availability, , increases a pricesetting platform always sets a lower end user price and obtains a lower profit, whereas a platform monopolist’s profit always increases in .

Finally, an interesting Corollary to Lemma 2 is that when the cost of development per unit performance $\beta$ increases, end user price $p _ { P S } ^ { * }$ may increase despite a decrease in platform performance, contrary to the natural intuition that high performance goes together with high price.

<sup>Corollary</sup> <sup>3.</sup> Consider a duopoly of price-setting platforms. When content development cost per unit performance, $\beta ,$ increases, platforms charge a higher end user price $p _ { P S } ^ { * }$ if $F \gamma - 2 M _ { D } ( \alpha + r ) \geq 0 .$ . As a result, the number of developers that join the platform, $N _ { D } ^ { * } ,$ goes down.

An increase in content development cost per unit performance deters content developers. To prevent that resistance, platforms adjust the performance level down; however, they cannot cut back performance sufficiently if average end user utility from performance, $\gamma$ is very high. As a result, developers face higher costs and fewer of them join the platform. In a market where platforms cannot adjust the royalty rate, this reduction in developer participation results in reduced revenues. To compensate for the lost revenue, platforms end up increasing the end user price.

## 4.2. Price-Taker Duopoly

In this section, we assume that game platforms are price takers (PT). In other words, platform sponsors commit to the end user price $p _ { i }$ in advance, which leaves platform performance as the only lever to capture demand on both sides of the market. Although in many industries platform sponsors would have the power to set the end user price, the price-taking assumption is consistent with empirical observation on game platforms (Thomke 1999). Following a multigeneration pattern, both Xbox 360 and PS3 (seventh generation) were sold at a loss at the beginning of their lifecycle (Boyer 2006, Hasseldahl 2005) and the simpler (sixth generation) Wii, which had already gone down the manufacturing learning curve, was sold nearly at cost (Schoenberger 2008). Because of the price sensitivity of gamers (Clements and Ohashi 2005, Chintagunta et al. 2009), computer game platforms are priced this way to maintain consumer side demand. Given significant manufacturing costs and price sensitivity, there can be minimal freedom to set the price.

We first analyze a benchmark case where platforms commit to the same end user price. Then, we provide some insights for the general case in which this assumption is relaxed.

4.2.1. Symmetric Platform Duopoly. In this section, we analyze two competing platforms that enter the market simultaneously and commit to the same end user platform price, that is, $p _ { 1 } = p _ { 2 } = p$ . In other words, we consider a duopolistic platform market where the two firms commit to equal prices and compete on performance. Accordingly, we obtain a symmetric equilibrium where both platform sponsors choose the following performance level and split the market equally:<sup>6</sup>

$$
\phi_ {1} = \phi_ {2} = \phi_ {P T} ^ {*} = \frac {F M _ {G} ((p - c) L _ {P T} + M _ {D} r A _ {P T})}{M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi},\tag{12}
$$

where $L _ { P T } = F \gamma - M _ { D } \alpha \beta , A _ { P T } = M _ { G } \gamma ( g - r ) - t \beta ,$ and $\chi = M _ { D } M _ { G } \alpha ( g - r ) - F t$

Similar to the performance threshold L seen in the monopoly and competitive price-setting sections, $L _ { P T }$ provides a measure of the net value of platform performance. When $L _ { P T }$ is negative, end users tend to value content availability more than they value platform performance, or content developers suffer from a high content development cost per unit performance. In these cases, a high platform performance is not valued in the market; hence the value of platform performance is low. Note that in this case $L < 0 ,$ implying that if the platforms were not constrained by price, they would set the platform performance at the minimum level the market bears (which we assume to be zero in our model). However, we see that sponsors will not necessarily lowball the performance investment when the performance decision is the main lever the platforms can use. Another important construct is $\chi ,$ the market competitiveness, which is a measure of the strength of competition relative to the strength of cross-side network effects. When $\chi$ is negative, there is not much competition between the two platforms in the end user market and the network effects are weak. A positive  implies a highly competitive market with significant network effects. Finally, similar to A described in $\ S 3 , A _ { P T }$ provides a measure of market attractiveness for developers under platform competition.

Lemma 3 (in Appendix A.3) shows that when $L _ { P T }$ and $\chi$ have the same sign, platforms have no other choice but to settle at the minimum performance level to secure market participation from developers. In other words, platforms adopt nontrivial performance strategies in two types of markets. In the first type, the content-driven market, the net value of platform performance is low, but market competitiveness is high. In other words, end users highly value content availability and the performance difference between the two platforms is less consequential for their decision. Further, it is a highly competitive market in which content developers face a high content development cost per unit performance. In the second type, the performance driven market, end users’ focus shifts to the performance of the platform. Additionally, the two platforms are differentiated enough to appeal to different segments of end users, thus alleviating the intensity of competition. For the video game industry, a content-driven market would be dominated by “casual gamers,” whereas a performance-driven market would be dominated by “hard-core gamers.” Even though both terms are loosely defined, it is generally assumed that hard-core gamers appreciate the graphical and processing capabilities of a game console far more than casual gamers. In contrast, casual gamers are typically interested in games that are quick to access, easy to learn, and that do not require gaming expertise or a regular time commitment to play (Casual Games Association 2007).

In the absence of pricing power, platforms must carefully manage their performance strategy to balance the cross-network effects. As a result, the performance investment at equilibrium presents some interesting features that we summarize in Proposition 2.

<sup>Proposition</sup> <sup>2.</sup> At equilibrium, the platform performance $\phi _ { P T } ^ { * }$ is

(i) decreasing in the end users’ average utility from platform performance, , when the net value of platform performance $L _ { P T }$ is negative and market competitiveness $\chi$ is positive;

(ii) decreasing in the degree of competition among the platforms in the end user market, when the net value $o f$ platform performance $L _ { P T }$ is negative and market competitiveness $\chi$ is positive;

(iii) increasing in the end users’ utility from content availability, $\alpha ,$ when market attractiveness for developers $A _ { P T }$ is positive.

In a one-sided market, if consumers highly value the performance of a product, competition will drive firms to offer higher performance. Proposition 2(i) shows that this relationship does not necessarily hold in two-sided markets. In particular, platform sponsors that are price constrained may choose to reduce their investment in platform performance in response to increasing end user utility from performance. The fundamental reason for this counterintuitive result is that platform performance and content availability act as substitutes for end users. Consider a highly competitive platform market characterized by end users with high preference for content availability and content developers with a high development cost per unit performance. To explain further, consider a content-driven market. In such a market, a platform sponsor might be better off decreasing investment in platform performance when end users’ utility from performance increases. Because content development cost per unit performance is high, a slight decrease in the platform’s performance may attract new content developers, which in turn attracts end users who enjoy a high utility from content availability.

Part (ii) presents a similar result for the relation between the degree of competition and platform performance. In the absence of cross-side network effects, if competition between two firms intensifies, a higher investment in performance is to be expected at equilibrium. However, in a two-sided market with priceconstrained platforms, performance decreases as the competitiveness in the end user market intensifies if market competitiveness is high but the net value of platform performance is low. Similar to part (i), this counterintuitive result stems from the substitution effect between content availability and platform performance. When the market value for platform performance is low, instead of providing a platform with higher performance in response to increasing competition, the platform sponsors may be better off investing slightly less in performance while getting content developers on board.

Table 2 Comparative Statics

<table><tr><td></td><td>Monopoly</td><td>Price-setting duopoly</td><td>Price-taking duopoly</td></tr><tr><td> $\alpha$ </td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td><td> $\phi^{*} \downarrow$ </td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td></tr><tr><td> $r$ </td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td><td> $\phi^{*} \downarrow$ </td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td></tr><tr><td> $\gamma$ </td><td> $\phi^{*} \uparrow$ </td><td> $\phi^{*} \uparrow$ </td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td></tr><tr><td> $t$ </td><td>N/A</td><td>No change</td><td> $\phi^{*} \uparrow$  or  $\downarrow$ </td></tr></table>

In part (iii), similar to Proposition 1 part (i), we show that a platform sponsor may be better off choosing a higher performance level when end users’ utility from content availability increases, despite the fact that higher performance makes it costly to develop content. This strategy is adopted when market attractiveness for developers is high.

Overall, Proposition 2 implies that a priceconstrained firm that ignores cross-side network effects may easily overinvest or underinvest in platform performance, especially in a content-driven market.

Table 2 summarizes the comparative static results for the three industry structures analyzed in this paper. A comparison of the price-setting and pricetaker duopolies shows that the counterintuitive effects of two-sidedness on platform development strategy are not observed once the platform sponsors have the degree of freedom to set the end user price in addition to the platform performance. The reason behind this is twofold. First, note that most of the counterintuitive effects in Proposition 2 are observed in a content-driven market, where $L _ { P T } = F \gamma - M _ { D } \alpha \beta \leq 0$ However, when $L _ { P T }$ is negative, so is L, implying that the price-setting platforms choose not to invest in platform performance above the minimum level dictated by the market (Lemma 2). Note that high performance is costly to the platform providers in two ways. The first cost comes from the fixed cost of developing the platform and the second comes from the risk of reduced participation from the developer side. Hence, in a content-driven market where the value of platform performance is low, the tendency to avoid investing in platform performance is intuitive. In the absence of a second leverage, though, pricetaker platforms are not always able to avoid investing in platform performance; thus, they carefully manage that investment to balance the cross-network effects, which results in counterintuitive strategies that are not adopted by price-setting platforms.

The second reason behind the differences between price-setting and price-taker equilibria stems from the curse of choice. In a competitive setting, the additional pricing power may trigger a price war that constrains the ability of platforms to adopt some counterintuitive yet profitable strategies. Proposition 3 provides an example for how the additional pricing power may be a drawback.

<sup>Proposition</sup> <sup>3.</sup> Consider two symmetric platforms simultaneously entering the market.

(i) If the end user utility from platform performance, , increases, the profit of a price-setting platform always decreases. However, the profit of a price-taker platform increases if the market is content driven.

(ii) If the degree of competition increases, the profit of a price-setting platform always decreases. However, the profit of a price-taker platform increases if the market is content driven.

In the presence of pricing power, if competition intensifies, platforms engage in a price war, which reduces profit. However, as shown in Proposition 2, price-taker platforms may respond to increasing competition by lowering the platform performance in a content-driven market. In this case, platform development costs go down and the platform becomes more attractive for developers with its low cost of content development. End users lose some utility because of the reduction in platform performance, yet this loss is compensated for by increased content availability. Hence, price-taker platforms may actually benefit from an increased degree of competition if the market is content driven. Similarly, an increase in end users’ utility from platform performance may benefit pricetaker platforms in a content-driven market, but such an increase in  never helps price-setting platforms.

4.2.2. Asymmetric Platform Duopoly. In this section, we relax the assumption that the two platforms commit to the same end user price. Given the additional complexity this entails, we explore the case through a numerical example and focus on what can happen given the right set of parameters.

An asymmetric duopoly includes a richer variety of market segmentation scenarios, some of which mimic the Wii’s success story. In particular, we observe that the platform with a lower investment in performance may be the market leader. Figure 4 represents two scenarios where platform 1 commits to a slightly lower end user price than platform 2. On the left panel, content development cost per unit performance is high. As a result, the markets represented on the left panel have a lower net value of platform performance, $L _ { P T } ,$ , compared to those in the right panel. The bottom right corners of both panels (region 1) show that when end user utility from platform performance () is very low and end user utility from content availability () is high, platform providers avoid investing in performance. The reason is that when  is high, it is critical to attract content developers, and in a market with low , an effective strategy to attract them is to indirectly reduce their development cost by choosing a low performance level. Note that this minimum-performance strategy has a limited appeal when the content development cost per unit performance is low (on the right panel). As end user utility from performance increases, platform providers have a stronger incentive to invest in platform performance. In region 2, platform 1 has a lower performance yet still captures a bigger market share on both sides of the market, similar to the Wii’s success story. Note that this result is most likely in a market characterized by a relatively low end user utility from platform performance. The “Xbox” region (region 4), on the other hand, shows where the more expensive and higher performance platform becomes the market leader, which requires a sufficiently high utility from platform performance. When end user utility from performance is neither low nor high, we may observe cases without a distinct market leader in the sense that none of the platforms capture a bigger share on both sides of the market. Specifically in region 3, the low-performance platform captures a bigger share of the developer market (by facilitating a low-cost development environment) whereas the high-performance platform captures a bigger share in the end user market (thanks to the appeal of high performance). This region becomes virtually invisible on the right panel because when the content development cost per performance is very low, the low-performance platform cannot provide the developers a cost saving that is big enough to offset the revenue disadvantage of having a smaller installed base in the end user market. Thus, on the right panel, we are more likely to observe cases where the high-performance platform becomes the market leader. Finally, as end user utility from performance and from content availability further increases, platforms engage in a performance war that drives down profits, as highlighted in Proposition 3 for the symmetric duopoly case. In region 5, the competitive pressure would drive the profits below zero, thus platforms do not enter the market. Note that this region is bigger on the right panel because when content development cost per performance is low, platforms have more room to increase performance without deterring developers, which results in a stronger performance war.

These market segmentation scenarios demonstrate that making the biggest investment in the platform technology does not necessarily bring market leadership. In content-driven markets, the key to capturing demand is to trigger third party development.

Figure 4 An Example of Market Segmentation for a Price-Taking Duopoly  
![](/api/attachments/RUUXVFBE/fulltext/images/1af66c9429751c26d10aaa9c4d7e284c3037f25dc62077ac9af67c81730d2539.jpg)  
High content development cost per performance

![](/api/attachments/RUUXVFBE/fulltext/images/a05d40db0e9306885a1d753a251f0b94c4cf6f66480ebead0c4ed77353904b4b.jpg)  
Low content development cost per performance  
Notes. $t = 0 . 5 , g = 0 . 2 , r = 0 . 1 , p _ { 1 } = 0 . 1 0 , p _ { 2 } = 0 . 1 5 , c = 0 . 0 5 , k = 5 , M _ { \delta } = 1 , M _ { o } = 1 , F = 1 . 5 , g = 0 . 0 0 2 , c = 0 . 0 0 2 , k = 1 . 5 , m _ { \delta } = 1 . 5 , r = 1 . 5 , m _ { \delta } = 1 \times 1 0 ^ { - 3 } )$ , and v = 0085. The left panel assumes  = 005. The right panel assumes $\beta = 0 . 0 2 5$ . Region 1: Both platforms set the minimum possible performance level (normalized to zero). Region 2: Low-performance, low-price platform captures a bigger share of the market on both sides. Region 3: Low-performance platform captures a bigger share in the developer market, whereas the high-performance platform captures a bigger share in the end user market. Region 4: High-performance, high-price platform captures a bigger market share on both sides. Region 5: Platforms do not enter the market because profits are negative.

## 5. Discussion and Limitations

The conventional wisdom for product markets is to heavily invest in core performance or features whenever the market demands it. However, in a two-sided platform market, our results show that high performance does not always produce a competitive edge. In content-driven markets, a lower performing platform can indeed become the market leader. Nintendo Wii’s success despite its low performance provides an example. The General Dynamics F-16, first introduced in 1976 and still widely used in the United States and around the world, provides a very different example of a lower-performance platform succeeding in a market characterized by complements.

Our model characterizes a content-driven market as one with low net value of performance and a high degree of competition between the platforms. In terms of end user preferences, this market condition places more emphasis on content availability and variety than on the core performance of the platform. For content developers, a content-driven market requires significantly higher development costs for high performance than lower performance platforms. As the video game industry expanded its target market beyond the “hard core gamers” to include more and more “casual gamers,” demand for better performance has been on the decline (Sheffield 2008, Wesley and Barczak 2010), triggering a shift to a content-driven market. In such an environment, a platform such as the Wii, which relies essentially on the previous generation technology, gains a competitive advantage in attracting game developers because of lower development costs. In a market where the games matter most, once the game developers are on board, so are the gamers.

It took the game industry some time to recognize that the average gamer does not necessarily ask for better graphics or better sound capabilities than what Nintendo Wii offers (Sheffield 2008). Indeed, there appears to be a temptation to overinvest in the gaming performance of a platform. The fundamental message this paper delivers is that firms must understand the competitive environment, the end user preferences, and the needs of the developer community when designing platforms for extensibility by third parties.

Following tradition in the two-sided market literature, we develop a stylized model to delineate a platform’s choice set. Such a research strategy requires a number of simplifications to permit analysis. Perhaps the most restrictive of our model simplifications is to assume that royalty is not a strategic variable. At first, this might seem a major flaw. Interestingly, however, many platforms adopt a common royalty (typically 30% on platforms such as Apple’s iTunes and approximately 20% on the major gaming console platforms). Thus, our assumption enjoys casual empirical support. To see whether there might be major findings left undiscovered, we solved the optimal couplet of performance and royalty in the monopoly case and obtained similar results. For example, we still observe that optimum platform performance may increase when end users’ utility from content availability increases. A thorough analysis of royalty as a strategic variable in conjunction with platform performance is left as future research that might focus on industries that vary royalty rates in response to market demands and competitive pressure.

Another important model simplification is that the end user market size is fixed in our analysis of competing platforms. This assumption is implicit in the Hotelling model, variants of which are frequently used in the two-sided markets literature (Parker and Van Alstyne 2000a, Armstrong 2002, Rochet and Tirole 2003, Armstrong 2006, Armstrong and Wright 2007, Anderson and Coate 2005, Kaiser and Wright 2006). Fixing the market size greatly simplifies the analysis but also presents a limitation because strategies that might expand or fail to attract the total market are not fully accounted for. To examine the robustness of our results with respect to this assumption, we used a modified version of the Hotelling model that includes “hinterlands” for each platform. The Hotelling model with hinterlands relaxes the fixed market size assumption by adding market expansion possibilities (e.g., Armstrong and Wright 2009). Although such a version of the model is intractable, numerical analysis shows that the key model results (directionality of platform performance decisions in response to changes in model primitives) are robust to this specification.

When modeling multihoming developers, we make a simplifying assumption that the cost of development is the same to both platforms; in other words, developers do not experience decreasing fixed cost when transplanting content to a different platform. Although this simplification is done for mathematical convenience, spreading fixed costs across both platforms does not change our results qualitatively. When platforms are symmetric, a developer who develops for one platform also develops for the other. Thus, if developers experience decreasing fixed cost when they multihome, in effect their overall fixed cost is reduced. This reduction would change the optimum levels of the decision variables, but it does not change the structure of the optimum strategy for platform performance.

We use an additive utility function when modeling end users’ utility from purchasing the platform. A limitation of this choice is that the marginal utility from content does not depend on platform performance. In other words, end users’ desire for content availability does not change as the platform performance increases. If the interaction between content availability and performance is strong, this could be a significant limitation. In our video-game setting, however, we would argue that the interaction effect between content availability and performance is not strong. A minor change (say 10%) in platform processing speed would not have much of an impact on a gamer’s desire for variety. If the interaction effect were factored into our model, then optimal values of the decision variables would change, but the core insights should hold so long as the magnitude of the interaction effect is small enough. Naturally, the highperformance strategy would become more appealing, but we would still observe markets where the low performance platform becomes the leader by virtue of facilitating a low-cost development environment.

Throughout the analysis we assume that content developers are able to multihome whereas end users choose to join a single platform. This framework fits the video game industry fairly well; however, it does not directly extend to markets where platforms make exclusivity deals with content developers. If each developer works exclusively for a particular platform, that is, if both sides of the market singlehome, then platform sponsors must compete in both sides of the market. This would make network effects even more critical. Our preliminary analysis of such a setting shows that the main results for the performance investment strategy such as the counterintuitive trends presented in Proposition 2 continue to hold. We suggest that a detailed comparison between the two frameworks is an area for future research.

Finally, we study single-period models of competition between platforms. Future work might analyze the sequential performance investment strategies of incumbents and entrants in a dynamic framework.

## 6. Conclusions

Platform development and design is a dimension of two-sided markets that has not been comprehensively addressed in the literature. Our goal in this paper is to make progress toward filling this gap. We explore the performance investment strategies of hardware/software platforms in a two-sided market. We focus on a platform sponsor’s trade-off between developing a high performance platform that matches end user preferences versus choosing not to satisfy those preferences in exchange for improved or less costly third party development capabilities. We show that conventional wisdom about product development decisions may be misleading in the presence of strong cross-network externalities.

We first characterize the monopoly case in order to develop the model and build intuition. We show that the platform monopolist may adjust performance upward even in the face of end users’ increasing preferences for content, suggesting that firms must carefully analyze the indirect feedback from the developer side to avoid making product development errors. In our analysis of competition, we divide markets into two types: content driven and performance driven. The market value of platform performance, as well as the degree of differentiation between the platforms, is low in the former and high in the latter. For price-taker platforms, conventional wisdom can be especially misleading in a content-driven market. In a one-sided market, for instance, if the degree of competition between firms increases, more aggressive investment in the performance of the product is to be expected. However, we show that in a content-driven market, platform sponsors are better off decreasing the investment in platform performance and providing greater content availability instead.

Finally, when platforms are price takers, a platform with lower performance can indeed become the market leader, as Nintendo Wii’s success against its high performance competitors Xbox360 and PS3 demonstrates. In other words, contrary to the conventional wisdom about “winner-take-all” markets, heavily investing in the core performance of a platform with strong cross-side network effects may not yield a competitive edge. Instead, acquiring a more complete understanding of both the end user market and the developer ecosystem is a necessity for firms to design winning platform strategies.

## Acknowledgments

This research was funded by the National Science Foundation under award SES-0925004.

## Appendix. Proofs

## A.1. Monopoly: Characterization

Optimum  and p satisfy the following first order conditions:

$$
\frac {\partial \Pi_ {m}}{\partial \phi} (\phi^ {*}, p ^ {*}) = \frac {\partial \Pi_ {m}}{\partial p} (\phi^ {*}, p ^ {*}) = 0.\tag{13}
$$

By solving (13) simultaneously, we obtain $\phi ^ { * }$ and $p ^ { * } .$ , given in Lemma 1. To ensure optimality, the following second order conditions must hold:

$$
\frac {\partial \Pi_ {m} ^ {2}}{\partial^ {2} p} = \frac {2 F M _ {G} (- F V + M _ {D} M _ {G} (g - r) (r + \alpha))}{(F V - M _ {D} M _ {G} (g - r) \alpha) ^ {2}} <   0\tag{14}
$$

$$
\begin{array}{l} \frac {\partial \Pi_ {m} ^ {2}}{\partial^ {2} \phi} \\ = - 2 K + \frac {2 M _ {D} M _ {G} r (F \gamma - M _ {D} \beta \alpha) (M _ {G} (g - r) \gamma - V \beta)}{(F V - M _ {D} M _ {G} (g - r) \alpha) ^ {2}} <   0 \end{array}\tag{15}
$$

det4Hessian5

$$
\begin{array}{l} = \frac {\partial \Pi_ {m} ^ {2}}{\partial^ {2} p} \frac {\partial \Pi_ {m} ^ {2}}{\partial^ {2} \phi} - \left(\frac {\partial \Pi_ {m}}{\partial p \partial \phi}\right) ^ {2} \\ = \frac {4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} L ^ {2}}{(F V - M _ {D} M _ {G} (g - r) \alpha) ^ {2}} > 0. \end{array}
$$

Note that (14) implies

(16)

$$
F V - M _ {D} M _ {G} (g - r) (r + \alpha) > 0,\tag{17}
$$

while (16) implies

$$
4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} L ^ {2} > 0.\tag{18}
$$

First, consider the interior solution $\phi ^ { * } > 0$ to the monopolist’s problem. We need to ensure $N _ { G } ^ { * } = N _ { G } ( \phi ^ { * } , p ^ { * } )$ and $\bar { N _ { D } ^ { * } } =$ $N _ { D } ( \phi ^ { * } , p ^ { * } )$ are positive at optimality:

$$
N _ {G} ^ {*} = \frac {2 F ^ {2} K M _ {G} (V - c)}{4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} L ^ {2}}\tag{19}
$$

$$
N _ {D} ^ {*} = \frac {M _ {D} M _ {G} (V - c) (2 F K (g - r) - \beta L)}{4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} L ^ {2}}.\tag{20}
$$

By (18), the denominator in (19) is positive; thus for $N _ { G } ^ { * } > 0 ,$ the following has to hold:

$$
V > c.\tag{21}
$$

Similarly, for $N _ { D } ^ { * } \geq 0 ,$ , the following must be true:

$$
2 F K (g - r) - \beta L \geq 0.\tag{22}
$$

By (21) and (18), we can deduce that $\phi ^ { * } \geq 0$ requires $L =$ $F \gamma - M _ { D } \beta ( \alpha + r ) \geq 0$

If $L < 0 ,$ then $\phi ^ { * } = 0$ and $p ^ { * } ( \phi ^ { * } = 0 )$ is given by

$$
p ^ {*} (\phi^ {*} = 0) = \frac {(V + c) (F V - M _ {D} M _ {G} \alpha (g - r)) - 2 V M _ {D} M _ {G} r (g - r)}{2 (F V - M _ {D} M _ {G} (g - r) (r + \alpha))}.
$$

In this case,

$$
\begin{array}{c} N _ {D} ^ {*} (\phi^ {*} = 0) = \frac {M _ {D} M _ {G} (g - r) (V - c)}{2 (F V - M _ {D} M _ {G} (g - r) (r + \alpha))}. \\ N _ {G} ^ {*} (\phi^ {*} = 0) = \frac {F M _ {G} (V - c)}{2 (F V - M _ {D} M _ {G} (g - r) (r + \alpha))}. \end{array}\tag{23}
$$

(24)

By (23) and (24), market participation when $\phi ^ { * } = 0$ requires $V > c$ . Thus, in $\ S 3 ,$ we assume (15), (17), (18), and (21) hold. For the interior solution $\phi > 0$ , we also assume (22) holds.

## A.2. Price-Setting Duopoly: Characterization

At equilibrium, 8<sup>∗</sup>1 <sup>∗</sup>1 p<sup>∗</sup>1 p<sup>∗</sup>9 satisfy the following first order conditions:

$$
\begin{array}{r l} \frac {\partial \Pi_ {1}}{\partial \phi_ {1}} (\phi_ {1} ^ {*}, p _ {1} ^ {*}; \phi_ {2} ^ {*}, p _ {2} ^ {*}) & = \frac {\partial \Pi_ {1}}{\partial p _ {1}} (\phi_ {1} ^ {*}, p _ {1} ^ {*}; \phi_ {2} ^ {*}, p _ {2} ^ {*}) = \frac {\partial \Pi_ {2}}{\partial \phi_ {2}} (\phi_ {2} ^ {*}, p _ {2} ^ {*}; \phi_ {1} ^ {*}, p _ {1} ^ {*}) \\ & = \frac {\partial \Pi_ {2}}{\partial p _ {2}} (\phi_ {2} ^ {*}, p _ {2} ^ {*}; \phi_ {1} ^ {*}, p _ {1} ^ {*}) = 0. \end{array} \tag {25}
$$

By solving (25) simultaneously, we obtain $\phi _ { P S } ^ { * }$ and $p _ { P S } ^ { * } ,$ given in Lemma 2. To ensure optimality, second order conditions require

$$
\frac {\partial^ {2} \Pi}{\partial p ^ {2}} = \frac {F M _ {G} (- 2 F t + M _ {D} M _ {G} (g - r) (r + 2 \alpha))}{2 (F t - M _ {D} M _ {G} (g - r) \alpha) ^ {2}} <   0\tag{26}
$$

$$
\frac {\partial^ {2} \Pi}{\partial \phi^ {2}}
$$

$$
= - 2 K + \frac {M _ {D} M _ {G} r L _ {P T} (M _ {G} (g - r) (F \gamma + M _ {D} \alpha \beta) - 2 F t \beta)}{2 F (F t - M _ {D} M _ {G} (g - r) \alpha) ^ {2}} <   0\tag{27}
$$

$$
\begin{array}{r l} & {\frac {\partial^ {2} \Pi}{\partial p ^ {2}} \frac {\partial^ {2} \Pi}{\partial \phi^ {2}} - \left(\frac {\partial^ {2} \Pi}{\partial p \partial \phi}\right) ^ {2}} \\ & {\qquad = \left[ M _ {G} (4 F K (2 F t - M _ {D} M _ {G} (g - r) (r + 2 \alpha)) + M _ {D} M _ {G} r (L + L _ {P T}) \right.} \\ & {\qquad \left. \cdot \beta - M _ {G} L _ {P T} ^ {2}) \right] \cdot \left[ 4 (F t - M _ {D} M _ {G} (g - r) \alpha) ^ {2} \right] ^ {- 1} > 0, \qquad (2 8)} \end{array}
$$

where $L _ { P T } = F \gamma - M _ { D } \alpha \beta .$ Note that (26) puts a lower bound on t:

$$
t > \frac {M _ {D} M _ {G} (g - r) (r + 2 \alpha)}{2 F}.\tag{29}
$$

First consider the high equilibrium. The number of developers that join the platform must be nonnegative:

$$
N _ {D} ^ {*} = M _ {D} M _ {G} \frac {2 F K - \beta L}{4 F ^ {2} K} \geq 0.\tag{30}
$$

We assume that end user market is covered, which requires that the marginal end user has nonnegative utility. Accordingly, the following is the sufficient condition for market coverage:

$$
\begin{array}{l} U (x = 1 / 2) \\ \qquad = v - c - \frac {3}{2} t + \frac {M _ {G} (L ^ {2} + 2 M _ {D} F K (g - r) (2 r + 3 \alpha))}{4 F ^ {2} K} \geq 0. \end{array}
$$

This condition puts an upper bound on t. In particular,

$$
\frac {3}{2} t \leq v - c + \frac {M _ {G} (L ^ {2} + 2 M _ {D} F K (g - r) (2 r + 3 \alpha))}{4 F ^ {2} K}.\tag{31}
$$

For the low equilibrium with $\phi _ { P S } ^ { * } = 0 .$ , developer market size $N _ { D } ^ { * } { = } M _ { D } M _ { G } ( { \bar { g } } - r ) / ( 2 F )$ , which is always positive. End user market coverage requires

$$
U (x = 1 / 2) = v - c - \frac {3}{2} t + \frac {M _ {D} M _ {G} (g - r) (2 r + 3 \alpha)}{2 F} \geq 0.
$$

This condition puts an upper bound on t, given by

$$
\frac {3}{2} t \leq v - c + \frac {M _ {D} M _ {G} (g - r) (2 r + 3 \alpha)}{2 F}.\tag{32}
$$

Accordingly, throughout §4.1 we assume that (27)–(29) hold. Additionally, for the high equilibrium we assume (30), and (31) are satisfied. Similarly for the low equilibrium, we assume (32) is satisfied.

## A.3. Price-Taker Duopoly: Characterization

At equilibrium, $\{ \phi _ { 1 } ^ { * } , \phi _ { 2 } ^ { * } \}$ satisfy the following first order conditions:

$$
\frac {\partial \Pi_ {1}}{\partial \phi_ {1}} (\phi_ {1} ^ {*}; \phi_ {2} ^ {*}) = \frac {\partial \Pi_ {2}}{\partial \phi_ {2}} (\phi_ {2} ^ {*}; \phi_ {1} ^ {*}) = 0.\tag{33}
$$

By solving (33), we obtain $\phi _ { P T } ^ { * }$ as

$$
\phi_ {P T} ^ {*} = \frac {F M _ {G} [ (p - c) L _ {P T} + M _ {D} r (M _ {G} \gamma (g - r) - t \beta) ]}{M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi}.
$$

Sufficient conditions for optimality require the following derivative to be negative:

$$
\frac {\partial \Pi^ {2}}{\partial^ {2} \phi} = - 2 K + \frac {M _ {D} M _ {G} r L _ {P T} (\beta \chi + F (M _ {G} (g - r) \gamma - t \beta))}{2 F \chi^ {2}}.\tag{34}
$$

To satisfy the sufficient condition for optimality, K must be sufficiently high. In particular,

$$
K > \frac {M _ {D} M _ {G} r L _ {P T} (\beta \chi + F (M _ {G} (g - r) \gamma - t \beta))}{4 F \chi^ {2}}.\tag{35}
$$

Below, we derive the conditions necessary to ensure that $\phi _ { C } ^ { * } \geq 0 .$ We first divide the parameter space into the following regions:

Region 1: $L _ { P T } \geq 0 \ \mathrm { a n d } \ \chi < 0$

Region 2: $L _ { P T } < 0 \mathrm { ~ a n d ~ } \chi \geq 0$

Region 3: $L _ { P T } > 0 \mathrm { ~ a n d ~ } \chi > 0$

Region 4: $L _ { P T } < 0 \mathrm { ~ a n d ~ } \chi < 0 .$

Next, we show that $\phi _ { P T } ^ { * } = 0$ in region 3 and region 4 since under these cases the developer market share at equilibrium N <sup>∗</sup> becomes negative.

Lemma 3. $\phi _ { P T } ^ { * } = 0$ in region 3 and region 4.

<sup>Proof.</sup> We first show that in region 3 the developer market share becomes negative at equilibrium if $\phi ^ { * } > 0$ Consider a market where $\mathbf { \bar { \xi } } _ { L _ { P T } } = F \pmb { \gamma } - \mathbf { \bar { \xi } } _ { M _ { D } \alpha \beta } > 0$ and $\chi =$ $M _ { D } M _ { G } \alpha ( g - r ) - F t > 0 .$ . First note that $\chi > 0$ implies

$$
\begin{array}{c} M _ {G} (g - r) \gamma - t \beta > M _ {G} (g - r) \gamma - \frac {M _ {D} M _ {G} \alpha (g - r) \beta}{F} \\ = M _ {G} (g - r) \bigg (\gamma - \frac {M _ {D} \alpha \beta}{F} \bigg) > 0. \end{array}
$$

The last inequality follows from $L _ { P T } = F \gamma - M _ { D } \alpha \beta > 0$ Hence, the numerator of $\phi _ { C } ^ { * }$ is positive when $L _ { P T } > 0$ and $\chi > 0 .$ Accordingly, the condition $\phi _ { C } ^ { * } > 0$ requires

$$
M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi > 0.\tag{36}
$$

The following condition is necessary for developers to enter the market at equilibrium:

$$
N _ {D} ^ {*} = \frac {M _ {D}}{F} \left(\frac {M _ {G} (g - r)}{2} - \beta \phi_ {C} ^ {*}\right) \geq 0.\tag{37}
$$

We want to show that when $L _ { P T } > 0$ and $\chi > 0 , ( 3 7 )$ does not hold. Note that (37) implies

$$
\beta \bigg (\frac {F M _ {G} [ (p - c) L _ {P T} - M _ {D} r (t \beta - M _ {G} \gamma (g - r)) ]}{M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi} \bigg) \leq \frac {M _ {G} (g - r)}{2}.
$$

Since the denominator of the left-hand side is positive by (36), we can rewrite the above inequality as

$$
\begin{array}{l} \beta F M _ {G} [ (p - c) L _ {P T} - M _ {D} r (t \beta - M _ {G} \gamma (g - r)) ] \\ \qquad \leq M _ {D} M _ {G} ^ {2} r \beta L _ {P T} \frac {(g - r)}{2} - 2 K F \chi M _ {G} (g - r). \end{array}
$$

Eliminating $M _ { G }$ from both sides of the inequality and substituting $L _ { P T } = F \gamma - M _ { D } \alpha \beta ,$ , we get

$$
\begin{array}{r l} & {\beta F (p - c) L _ {P T} - \beta^ {2} F M _ {D} r t + \beta F M _ {D} r M _ {G} \gamma (g - r)} \\ & {\qquad \leq \beta F M _ {D} M _ {G} r \gamma \frac {(g - r)}{2} - M _ {D} ^ {2} M _ {G} r \beta^ {2} \alpha \frac {(g - r)}{2}} \\ & {\qquad - 2 K F \chi M _ {G} (g - r)} \\ & {\Leftrightarrow \beta F (p - c) L _ {P T} - \beta^ {2} F M _ {D} r t + \beta F M _ {D} M _ {G} r \frac {(g - r)}{2} \gamma} \\ & {\qquad + M _ {D} ^ {2} M _ {G} r \beta^ {2} \alpha \frac {(g - r)}{2} \leq - 2 K F \chi M _ {G} (g - r).} \end{array}
$$

The right-hand side of the last inequality is negative when $\chi \geq 0$ . Hence, the left-hand side has to be negative. We add and subtract the term $M _ { D } ^ { 2 } M _ { G } r \beta ^ { 2 } \alpha ( ( g - r ) / 2 )$ from the lefthand side to get

$$
\begin{array}{c} \beta F (p - c) L _ {P T} - \beta^ {2} F M _ {D} r t + \beta F M _ {D} M _ {G} r \frac {(g - r)}{2} \gamma \\ + M _ {D} ^ {2} M _ {G} r \beta^ {2} \alpha (g - r) - M _ {D} ^ {2} M _ {G} r \beta^ {2} \alpha \frac {(g - r)}{2}. \end{array}
$$

Rearranging the terms and substituting $\chi = M _ { D } M _ { G } ( g - r )$ $\alpha - { \cal F } t$ yields

$$
\begin{array}{l} \beta F (p - c) L _ {P T} + \beta^ {2} M _ {D} r \chi + \beta F M _ {D} M _ {G} r \frac {(g - r)}{2} \gamma \\ \qquad - M _ {D} ^ {2} M _ {G} r \beta^ {2} \alpha \frac {(g - r)}{2} \\ = \beta F (p - c) L _ {P T} + M _ {D} \beta^ {2} r \chi + \beta M _ {D} M _ {G} r \frac {(g - r)}{2} (F \gamma - M _ {D} \beta \alpha) \\ = \beta F (p - c) L _ {P T} + M _ {D} \beta^ {2} r \chi + \beta M _ {D} M _ {G} r \frac {(g - r)}{2} L _ {P T}. \end{array} \tag {38}
$$

If the sign of (38) is strictly positive, then (37) gives a contradiction. The first and the third term of (38) are positive since $L _ { P T } > ,$ , whereas the second term is positive since $\chi > 0 .$ This contradicts (37). Hence region 3 does not satisfy the individual rationality constraint for the developers if $\phi ^ { * } > 0 ,$ which implies $\phi _ { P T } ^ { * } = 0$ in region 3. The same result can be shown to hold for region 4 with a similar proof. <sup></sup>

Throughout §4.2.1, we focus on markets where platforms are not forced to settle down at the minimum performance level, i.e., markets with $\phi _ { P T } ^ { * } > 0$ . In other words, we focus on regions 1 and 2 meaning that the following holds:

$$
L _ {P T} \chi = (F \gamma - M _ {D} \alpha \beta) (M _ {D} M _ {G} \alpha (g - r) - F t) \leq 0.\tag{39}
$$

$_ { \mathrm { N e x t , } }$ we discuss restrictions on parameters in regions 1 and 2 so that all constraints $( \mathrm { i . e . , ~ } \phi _ { C } ^ { \ast } \ge 0 ,$ , second order conditions, gamer market coverage, developer individual rationality) hold.

To ensure $\phi _ { C } ^ { * } \ge 0$ in regions 1 and 2, the following has to hold:

$$
p - c \geq \frac {M _ {D} r (t \beta - M _ {G} \gamma (g - r))}{L _ {P T}}.\tag{40}
$$

Note that this condition does not necessarily require $p > c$ as the right-hand side can be negative.

To ensure $N _ { D } ^ { * } \geq 0 ,$ , the following has to hold:

$$
\begin{array}{c} N _ {D} ^ {*} = \frac {M _ {D} M _ {G} (g - r)}{2 F} \\ - \frac {M _ {D} M _ {G} (2 F M _ {D} \beta r A _ {P T} + 2 F \beta (p - c) L _ {P T})}{2 F (M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi)} \geq 0. \end{array}\tag{41}
$$

We assume that end user market is covered, which requires that the marginal end user has nonnegative utility. Accordingly, the following is the sufficient condition for market coverage:

$$
\begin{array}{l} U ^ {*} (x = 1 / 2) \\ = v + \frac {\alpha M _ {D}}{F} \left(\frac {M _ {G}}{2} (g - r) - \beta \phi_ {P T} ^ {*}\right) + \gamma \phi_ {P T} ^ {*} - p - \frac {t}{2} \geq 0. \end{array}\tag{42}
$$

For markets with $\phi _ { P T } ^ { * } > 0 ,$ which are the main focus of §4.2, we assume that the parameters satisfy (35), (39)–(42).

To confirm existence, it is easy to verify that the following parameter set in region 1 satisfies all the constraints (i.e., $\bar { \phi } _ { C } ^ { * } \ge 0 .$ , second order conditions, gamer market coverage, developer individual rationality):

$$
\begin{array}{l} \gamma = 1. 3, \quad \alpha = 0. 8 5, \quad \beta = 0. 5, \quad t = 0. 2 5, \quad g = 0. 3, \quad r = 0. 0 5, \\ p = 0. 0 2, \quad c = 0. 0 0 0 5, \quad K = 3, \quad M _ {D} = 1, \quad M _ {G} = 1, \quad F = 1. \end{array}
$$

Similarly, the following parameter set in region 2 satisfies all constraints:

$$
\begin{array}{r l} & {\gamma = 0. 5, \quad \alpha = 2, \quad \beta = 0. 2 5, \quad t = 0. 2, \quad g = 0. 2 5, \quad r = 0. 0 5,} \\ & {p = 0. 4 5, \quad c = 0. 0 5, \quad K = 3, \quad M _ {D} = 2, \quad M _ {G} = 2, \quad F = 1.} \end{array}
$$

Finally, consider markets with $\phi _ { P T } ^ { * } = 0$ . In this case, developer market size is given by $N _ { D } ^ { * } { = } \bar { M } _ { D } M _ { G } ( g { - } r ) / ( 2 F )$ , which is always positive. The main constraint that needs to be satisfied is end user market coverage, which requires

$$
t + 2 p \leq \frac {M _ {D} M _ {G} (g - r) \alpha}{2 F}.\tag{43}
$$

## A.4. Proofs

Proof of Proposition 1. <sub>First</sub> <sub>note</sub> <sub>that</sub> <sub>when</sub> $L = F \gamma -$ $M _ { D } \beta ( \alpha + r ) \le 0 .$ , the platform monopolist chooses the minimum platform performance, which is assumed to be zero. In that case, equilibrium performance is insensitive to changes in market parameters as long as L stays negative. Thus, we analyze the case when $L > 0 \bar { . }$

(i) It suffices to check the sign of the following derivative:

$$
\begin{array}{l} \frac {\partial \phi_ {m} ^ {*}}{\partial \alpha} \\ = \frac {- F ^ {2} M _ {G} (V - c) (M _ {G} \beta L ^ {2} - 4 F ^ {2} K (M _ {G} (g - r) \gamma - V \beta))}{[ 4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} (F \gamma - M _ {D} \beta (\alpha + r)) ^ {2} ] ^ {2}}. \end{array}
$$

By $( 2 1 ) \ V > c .$ . Thus, it is easy to see that $\partial \phi _ { m } ^ { * } / \partial \alpha \geq 0 \mathrm { i f }$ $4 \bar { F } ^ { 2 } K ( M _ { G } ( g - r ) \gamma - V \beta ) - \bar { M _ { G } } \beta L ^ { 2 } = 4 F ^ { 2 } K A - \bar { M } _ { G } \beta L ^ { 2 } \geq 0$ Equivalently, $A \ge ( M _ { G } \beta L ^ { 2 } ) / ( 4 F ^ { 2 } K )$ , concluding the proof.

(ii) It suffices to check the sign of the following derivative:

$$
\begin{array}{r l} \frac {\partial \phi_ {m} ^ {*}}{\partial r} = & \left[ - F M _ {D} M _ {G} (V - c) (M _ {G} \beta L ^ {2} + 4 F K M _ {G} L (\alpha + r) \right. \\ & \left. - 4 F ^ {2} K (M _ {G} (g - r) \gamma - V \beta)) \right] \cdot \left\{[ 4 F K (F V - M _ {D} M _ {G} \right. \\ & \left. \cdot (g - r) (r + \alpha)) - M _ {G} (F \gamma - M _ {D} \beta (\alpha + r)) ^ {2} ] ^ {2} \right\} ^ {- 1}. \end{array}
$$

By (21) $V > c .$ . Thus, it is easy to see that $\partial \phi _ { m } ^ { * } / \partial r \geq 0$ if $4 F ^ { 2 } K ( M _ { G } ( g - r ) \gamma - V \beta ) - \dot { M } _ { G } \beta L ^ { 2 } - 4 F K M _ { G } L ( \alpha + r ) =$ $4 F ^ { 2 } K A - \bar { M } _ { G } \beta L ^ { 2 } - 4 F K M _ { G } L ( \alpha + \bar { r } ) \geq 0 .$ Equivalently, $A \geq$ $( M _ { G } \beta L ^ { 2 } + 4 F K M _ { G } L ( \alpha + r ) ) / ( 4 F ^ { 2 } K )$ concluding the proof. (iii) Let $B = 4 F K ( F V - M _ { D } M _ { G } ( g - r ) ( r + \bar { \alpha } ) ) + \bar { M } _ { G } ( F \gamma -$ $M _ { D } \beta ( \alpha + r ) ) ^ { 2 }$ . Note that by $( 1 7 ) , F V - M _ { D } M _ { G } ( g - r ) ( r + \alpha ) >$ 0. Thus $B > 0 .$ It suffices to check the sign of the following derivative:

$$
\begin{array}{r l} \frac {\partial \phi_ {m} ^ {*}}{\partial \gamma} = & (F ^ {2} M _ {G} (V - c) B) \cdot \left\{[ 4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} (F \gamma - M _ {D} \beta (\alpha + r)) ^ {2} ] ^ {2} \right\} ^ {- 1}. \end{array} \tag {44}
$$

By (21) $V > c .$ Thus, it is easy to see that $\partial \phi _ { m } ^ { * } / \partial \gamma$ is always positive.

(iv) It suffices to check the sign of the following derivative:

$$
\begin{array}{r l} \frac {\partial \phi_ {m} ^ {*}}{\partial \beta} = & (F M _ {D} M _ {G} (- V + c) B) \cdot \left\{\left[ 4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) \right. \right. \\ & \left. \left. - M _ {G} (F \gamma - M _ {D} \beta (\alpha + r)) ^ {2} \right] ^ {2} \right\} ^ {- 1}. \end{array} \tag {45}
$$

Since $V > c ,$ the derivative $\partial \phi _ { m } ^ { * } / \partial \beta$ is always negative. <sup></sup>

Proof of Corollary 1. <sub>First</sub> <sub>note</sub> <sub>that</sub> <sub>when</sub> $L = F \gamma -$ $M _ { D } \beta ( \alpha + r ) \le 0 .$ , both platforms choose the minimum platform performance that is assumed to be zero. In that case, equilibrium performance is insensitive to changes in market parameters as long as L stays negative. Thus, we analyze the case when $L > 0 ,$ , where $\overset { \cdot } { \phi _ { P S } ^ { * } } = \overset { \cdot } { M } _ { G } L / ( 4 F K )$

(i) It suffices to check the sign of the following derivative, which is trivially negative:

$$
\frac {\partial \phi_ {P S} ^ {*}}{\partial \alpha} = - \frac {M _ {D} M _ {G} \beta}{4 F K}.
$$

(ii) It suffices to check the sign of the following derivative, which is trivially negative:

$$
\frac {\partial \phi_ {P S} ^ {*}}{\partial r} = - \frac {M _ {D} M _ {G} \beta}{4 F K}.
$$

(iii) It suffices to check the sign of the following derivative, which is trivially positive:

$$
\frac {\partial \phi_ {P S} ^ {*}}{\partial \gamma} = \frac {M _ {G}}{4 K}.
$$

(iv) It suffices to check the sign of the following derivative, which is trivially negative:

$$
\frac {\partial \phi_ {P S} ^ {*}}{\partial \beta} = - \frac {M _ {D} M _ {G} (r + \alpha)}{4 F K}.
$$

(v) It is easy to see that $\partial \phi _ { P S } ^ { * } / \partial t = 0 . \quad \varTheta$

Proof of Corollary 2. <sub>First</sub> <sub>we</sub> <sub>show</sub> <sub>that</sub> $\partial p _ { P S } ^ { * } / \partial \alpha \leq 0 .$ which can easily be seen from the following derivative:

$$
\frac {\partial p _ {P S} ^ {*}}{\partial \alpha} = \left\{ \begin{array}{l l} \frac {- M _ {D} M _ {G} (4 F K (g - r) + M _ {D} r \beta^ {2})}{4 F ^ {2} K} & L \geq 0 \\ \frac {- M _ {D} M _ {G} (g - r)}{F} & L <   0. \end{array} \right.
$$

To compare the profits, we want to show that $\partial \Pi _ { m } ^ { * } / \partial \alpha \geq 0$ while ¡ç $\Gamma _ { P S } ^ { * } / \partial \alpha \leq 0 ;$

$$
\frac {\partial \Pi_ {m} ^ {*}}{\partial \alpha} = \left\{ \begin{array}{l l} \frac {2 F ^ {2} K M _ {D} M _ {G} ^ {2} (V - c) ^ {2} (2 F K (g - r) - \beta L)}{[ 4 F K (F V - M _ {D} M _ {G} (g - r) (r + \alpha)) - M _ {G} L ^ {2} ] ^ {2}} & L \geq 0 \\ \frac {F M _ {G} (V - c) ^ {2}}{4 (F V - M _ {D} M _ {G} (g - r) (r + \alpha))} & L <   0. \end{array} \right.
$$

By (22), 2F $\zeta ( g - r ) - \beta L \geq 0$ when $\phi _ { m } ^ { * } > 0$ . Thus, $\partial \Pi _ { m } ^ { * } / \partial \alpha \geq 0$ when $L \geq 0 .$ . By (17), $F V - M _ { D } M _ { G } ( g - r ) ( r + \alpha ) > 0 .$ . Thus, $\partial \Pi _ { m } ^ { * } / \partial \alpha > 0$ when $L < 0 { : }$

$$
\frac {\partial \Pi_ {P S} ^ {*}}{\partial \alpha} = \left\{ \begin{array}{l l} \frac {- M _ {D} M _ {\mathrm{G}} ^ {2} (4 F K (g - r) - \beta L)}{8 e ^ {2} F ^ {2} K} & L \geq 0 \\ \frac {- M _ {D} M _ {\mathrm{G}} ^ {2} (g - r)}{2 F} & L <   0. \end{array} \right.
$$

$\partial \Pi _ { P S } ^ { * } / \partial \alpha$ is trivially negative when $L < 0$ . By $( 3 0 ) , 2 F K ( g - r )$ $\ge \beta L$ , thus it is easy to see that $\partial \Pi _ { P S } ^ { * } / \partial \alpha \leq \mathrm { ~ \bar { 0 } ~ }$ completing the proof.

<sup>Proof</sup> <sup>of</sup> <sup>Corollary</sup> <sup>3.</sup> In Corollary 1, we have shown that $\phi _ { P S } ^ { * }$ decreases with $\beta .$ The following derivative trivially shows that $\partial p _ { P S } ^ { * } / \partial \beta \geq 0$ when $( F \gamma - 2 M _ { D } \beta ( \alpha + r ) ) \geq 0 { : }$

$$
\frac {\partial p _ {P S} ^ {*}}{\partial \beta} = \left\{ \begin{array}{l l} \frac {M _ {D} M _ {G} r (F \gamma - 2 M _ {D} \beta (\alpha + r))}{4 F ^ {2} K} & L \geq 0 \\ 0 & L <   0. \end{array} \right.\tag{46}
$$

Finally, we show that $N _ { D } ^ { * }$ decreases when $( F \gamma - 2 M _ { D } \beta$ $\left( \alpha + r ) \right) \geq 0 .$ , which can be seen easily from the following derivative:

$$
\frac {\partial N _ {D} ^ {*}}{\partial \beta} = \left\{ \begin{array}{l l} \frac {- M _ {D} M _ {G} (F \gamma - 2 M _ {D} \beta (\alpha + r))}{4 F ^ {2} K} & L \geq 0 \\ 0 & L <   0. \end{array} \right. \quad \square
$$

Proof of Proposition 2. <sub>First</sub> <sub>note</sub> <sub>that</sub> <sub>when</sub> $L _ { P T } \chi > 0 ,$ both platforms choose the minimum platform performance, which is assumed to be zero. In that case, equilibrium performance is insensitive to changes in market parameters as long as $L _ { P T } * \chi$ stays positive. Below, we analyze the nontrivial case where $\phi _ { P T } ^ { * } * > 0$

(i) It suffices to check the sign of the following derivative:

$$
\begin{array}{l} \frac {\partial \phi^ {*}}{\partial \gamma} \\ = \frac {- F M _ {G} \chi [ 4 F ^ {2} K (p - c) + M _ {D} M _ {G} r (4 F K (g - r) + M _ {D} r \beta^ {2}) ]}{(M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi) ^ {2}}. \end{array}\tag{47}
$$

It is easy to see that (47) is nonpositive if $\chi \geq 0 .$ . By Lemma $^ { 3 , }$ $\chi \geq 0$ also requires $L _ { P T } \leq 0$ concluding the proof.

(ii) Note that the degree of competition in a market increases when t, the product differentiation between the platforms, decreases. Hence, it suffices to confirm that $\phi ^ { * }$ may increase with t by checking the sign of the following derivative:

$$
\begin{array}{r l} \frac {\partial \phi^ {*}}{\partial t} = & \left\{- F M _ {G} L _ {P T} [ 4 F ^ {2} K (p - c) + M _ {D} M _ {G} r (4 F K (g - r)) \right. \\ & \left. + M _ {D} r \beta^ {2}) ] \right\} \cdot \left[ (M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi) ^ {2} \right] ^ {- 1}. \end{array} \tag {1}\tag{48}
$$

The denominator of (48) is trivially positive. The numerator is positive when $L _ { P T } \leq 0$ . By Lemma $3 , \ L _ { P T } \leq 0$ also requires $\chi \geq 0$ , concluding the proof. Hence, when $L _ { P T }$ is negative and $\chi$ is positive, platform performance decreases with increasing degree of competition.

(iii) It suffices to check the sign of the following derivative:

$$
\frac {\partial \phi^ {*}}{\partial g} = \frac {F M _ {D} M _ {\mathrm{G}} ^ {2} L _ {P T} [ 4 F K (r t + (p - c) \alpha) + M _ {D} M _ {\mathrm{G}} r ^ {2} \beta \gamma ]}{(M _ {D} M _ {\mathrm{G}} r \beta L _ {P T} - 4 K F \chi) ^ {2}}.\tag{49}
$$

The denominator of (49) is trivially positive. The numerator is negative if $L _ { P T } \leq 0 ,$ , in which case the optimal performance decreases with the game price g. By Lemma $^ { 3 , }$ $L _ { P T } \leq 0$ also requires $\chi \geq 0 ,$ , concluding the proof.

(iv) It suffices to check the sign of the following derivative:

$$
\begin{array}{r l} \frac {\partial \phi^ {*}}{\partial \alpha} = & \left\{F M _ {G} (M _ {G} (g - r) \gamma - t \beta) [ 4 F ^ {2} K (p - c) + M _ {D} M _ {G} r (4 F K \chi) ] \right\} \\ & \cdot (g - r) + M _ {D} r \beta^ {2}) ] \Big \} \cdot \left[ (M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi) ^ {2} \right] ^ {- 1}. \end{array}\tag{50}
$$

It is easy to see that (50) is nonnegative when $M _ { G } ( g - r ) \gamma -$ $t \beta \ge 0 . \dot { \mathrm { ~ \scriptsize ~ \sharp ~ } }$

Proof of Proposition 3. <sub>Let</sub> $\Pi _ { P S } ^ { * } \ = \ \Pi _ { P S } ( \phi _ { P S } ^ { * } , p _ { P S } ^ { * } ;$ $\phi _ { P S } ^ { * } , p _ { P S } ^ { * } )$ and $\Pi _ { P T } ^ { * } = \Pi _ { P T } ( \phi _ { P T } ^ { * } , p _ { P T } ^ { * } ; \phi _ { P T } ^ { * } , p _ { P T } ^ { * } )$

(i) We want to show $\partial \Pi _ { P S } ^ { * } / \partial \gamma \leq 0$ whereas in a contentdriven market $\partial \Pi _ { P T } ^ { * } / \partial \gamma \geq 0 .$ . It is easy to see that

$$
\frac {\partial \Pi_ {P S} ^ {*}}{\partial \gamma} = \left\{ \begin{array}{l l} \frac {- M _ {G} ^ {2} L}{8 F K} & L \geq 0 \\ 0 & L <   0, \end{array} \right.\tag{51}
$$

whereas

$$
\frac {\partial \Pi_ {P T} ^ {*}}{\partial \gamma} = \left\{ \begin{array}{l l} \left\{M _ {G} ^ {2} L _ {P T} \chi [ 4 F K (F (p - c) + M _ {D} M _ {G} r (g - r)) + M _ {D} ^ {2} \right. \\ \left. \cdot M _ {G} r ^ {2} \beta^ {2} ] ^ {2} \right\} \cdot \left[ 2 (M _ {D} M _ {G} r \beta L _ {P T} - 4 K F \chi) ^ {3} \right] ^ {- 1} \\ & \phi_ {P T} ^ {*} \geq 0 \\ 0 & \phi_ {P T} ^ {*} = 0. \end{array} \right.\tag{52}
$$

First note that platform profit is insensitive to changes in  if $\phi ^ { * } = 0$ . We analyze the case when $\phi _ { i } ^ { * } > 0 , i \in \{ P S , P T \}$ In a price-setting duopoly, it is easy to see that $\partial \pi ^ { P S } / \partial \gamma \leq 0$ In a price-taker duopoly, it is easy to see that $\partial \Pi _ { P T } ^ { * } / \partial \gamma \leq 0$ if the market is content driven; i.e., if $L _ { P T } \leq 0$ and $\chi \geq 0 ,$ meaning that platform profit increases when the end users’ utility from platform performance increases.

ii) First note that when t increases, the degree of competition is reduced. Thus we want to show $\bar { \partial } \Pi _ { P S } ^ { * } / \partial t \geq 0$ whereas in a content-driven market $\partial \Pi _ { P T } ^ { * } / \partial t \leq 0$ . It is easy to see that

$$
\frac {\partial \Pi_ {P S} ^ {*}}{\partial t} = \frac {M _ {G}}{2}\tag{53}
$$

$$
\frac {\partial \Pi_ {P T} ^ {*}}{\partial t} = \left\{ \begin{array}{l l} (M _ {G} ^ {2} L _ {P T} ^ {2} [ 4 F K (F (p - c) + M _ {D} M _ {G} r (g - r)) \\ \quad + M _ {D} ^ {2} M _ {G} r ^ {2} \beta^ {2} ] ^ {2}) \cdot (2 (M _ {D} M _ {G} r \beta L _ {P T} \\ \quad - 4 K F \chi) ^ {3}) ^ {- 1} & \phi_ {P T} ^ {*} \geq 0 \\ 0 & \phi_ {P T} ^ {*} = 0. \end{array} \right.\tag{54}
$$

Platform profit is insensitive to changes in t if $\phi ^ { * } = 0 .$ . We analyze the case when $\phi _ { i } ^ { * } > 0 , \ : i \in \{ P \bar { S } , P T \}$ . Trivially from (53), the profit of a price-setting platform always increases when t increases; in other words, when the degree of competition decreases. In a price-taker duopoly, it is easy to see that $\partial \Pi _ { P T } ^ { * } / \partial t \leq 0$ if the market is content driven, i.e., if $L _ { P T } \leq 0$ and $\chi \geq 0 ,$ , concluding the proof. <sup></sup>

## References

Allen D (2006) First look: Sony PS3 versus Nintendo Wii. PCWorld (Nov. 14), http://www.pcworld.com/article/127881/ article.html.

Anderson S, Coate S (2005) Market provision of broadcasting: A welfare analysis. Rev. Econom. Stud. 72:947–972.

Armstrong M (2002) The theory of access pricing and interconnection. Cave M, Majumdar S, Vogelsang I, eds. Handbook of Telecommunications Economics Vol. I (North Holland, Amsterdam), 295–384.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Armstrong M, Wright J (2007) Two-sided markets, competitive bottlenecks and exclusive contracts. Econom. Theory 32:353–380.

Armstrong M, Wright J (2009) Mobile call termination. Econom. J. 119:270–307.

Arthur B (1989) Competing technologies, increasing returns, and lock-in by historical events. Econom. J. 99(March):116–131.

Basu A, Mazumdar T, Raj SP (2003) Indirect network externality effects on product attributes. Marketing Sci. 22(2):209–221.

Bhargava HK, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Boudreau KJ, Hagiu A (2009) Platform rules: Multi-sided platforms as regulators. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar, London), 163–191.

Boyer B (2006) isuppli: PS3 sold at \$300 loss on hardware components. Retrieved November 16, 2006, http://www.gamasutra .com/php-bin/news\_index.php?story=1174.

Brooks FP (1975) The Mythical Man-Month, Vol. 79 (Addison-Wesley, Reading, MA).

Caillaud B, Jullien B (2003) Chicken and egg: Competition among intermediation service providers. RAND J. Econom. 34(2): 309–328.

Casual Games Association (2007) Casual Games Market Report 2007. Retrieved January 15, 2009, https://dl.dropboxusercontent .com/u/3698805/Reports/CasualGamesMarketReport-2007.pdf.

Chintagunta PK, Nair HS, Sukumar R (2009) Measuring marketingmix effects in the 32/64 bit video-game console market. J. Appl. Econometrics 24(3):421–445.

Choi JP (1994) Network externality, compatibility choice, and planned obsolescence. J. Indust. Econom. 42(2):167–182.

Clements MT, Ohashi H (2005) Indirect network effects and the product cycle: Video games in the U.S. J. Indust. Econom. 53(4):515–542.

Corts K, Lederman M (2009) Software exclusivity and the scope of indirect network effects in the U.S. home video game market. Internat. J. Indust. Organ. 27:121–136.

Cusumano M (2010) Technology strategy and management: the evolution of platform thinking. Comm. ACM 53(1):32–34.

de Froberville D (2008) Phone interview by Edward Anderson and Geoffrey Parker. Video game project management. November 28, 2008.

Dutka B (2009) Do multiplatform games affect console sales? PSXExtreme (June 4), http://www.psxextreme.com/feature/ 410.html.

Eisenmann TR, Parker G, Van Alstyne M (2006) Strategies for twosided markets. Harvard Bus. Rev. 84(10):92–101.

Eisenmann TR, Parker G, Van Alstyne M (2011) Platform envelopment. Strategic Management J. 32(12):1270–1285.

Farrell J, Saloner G (1985) Standardization, compatibility, and innovation. RAND J. Econom. 16:70–83.

Farrell J, Saloner G (1986) Installed base and compatibility: Innovation, product preannouncements, and predation. Amer. Econom. Rev. 76:940–955.

Gandal N, Kende M, Rob R (2000) The dynamics of technological adoption in hardware/software systems: The case of compact disc players. RAND J. Econom. 31(1):43–61.

Gawer A, Cusumano M (2002) Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation (Harvard Business School Publishing, Boston).

Gawer A, Cusumano MA (2008) How companies become platform leaders. MIT Sloan Management Rev. 49(2):28–35.

Green PE, Srinivasan V (1990) Conjoint analysis in marketing: New developments with implications for research and practice. J. Marketing 54(4):3–19.

Gretz R (2010) Hardware quality vs. network size in the home video game industry. J. Econom. Behav. Organ. 76:168–183.

Hagiu A (2006) Pricing and commitment by two-sided platforms. RAND J. Econom. 37(3):720–737.

Hasseldahl A (2005) Microsoft’s red-ink game. BusinessWeek.com (November 22), http://www.businessweek.com/technology/ content/nov2005/tc20051122\_410710.htm.

Jones SR, Zsidisin GA (2008) Performance implications of product life cycle extension: The case of the A-10 aircraft. J. Bus. Logist. 29(2):189–214.

Kaiser U, Wright J (2006) Price structure in two-sided markets: Evidence from the magazine industry. Internat. J. Indust. Organ. 24:1–28.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Katz ML, Shapiro C (1986a) Technology adoption in the presence of network externalities. J. Political Econom. 94:823–841.

Katz ML, Shapiro C (1986b) Product compatibility choice in a market with technological progress. Oxford Econom. Papers, Special Issue 38:146–165.

Katz ML, Shapiro C (1994) Systems competition and network effects. J. Econom. Perspect. 8(2):93–115.

Kim R (2007) Wii need more games. Developers push to meet demand on popular box. San Francisco Chronicle (May 18), http://www.sfgate.com/business/article/Wii-needs-more -games-Developers-push-to-meet-2593328.php.

Krishnan V, Ulrich KT (2001) Product development decisions: A review of the literature. Management Sci. 47(1):1–21.

Kristiansen EG (1998) R&D in the presence of network externalities: Timing and compatibility. RAND J. Econom. 29(3):531–547.

Leheng Q (2006) Wii development costs a quarter to half compared to PS3/360. TechGate (August 11), http://tech .commongate.com/.

Liebowitz SJ, Margolis SE (1994) Network externality: An uncommon tragedy. J. Econom. Perspect. 8(2):133–150.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18:301–317.

Nair H, Chintagunta P, Dube JP (2004) Empirical analysis of indirect network effects in the market for personal digital assistants. Quant. Marketing Econom. 2(1):23–58.

Parker G, Van Alstyne M (2000a) Information complements, substitutes, and strategic product design. Mimeo; Tulane University, LA; and University of Michigan, Ann Arbor.

Parker G, Van Alstyne M (2000b) Internetwork externalities and free information goods. Proc. 2nd ACM Conf. Electronic Commerce (ACM, New York), 107–116.

Parker G, Van Alstyne M (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parker G, Van Alstyne M (2009) Six challenges in platform licensing and open innovation. Comm. Amp; Strategies (74):17–36.

Parker G, Van Alstyne M (2012) A digital postal platform: Definitions and a roadmap. Technical report, MIT, Cambridge, MA.

Parker G, Van Alstyne M (2013) Innovation, openness and platform control (August 4), http://ssrn.com/abstract=1079712.

Papalambros PY (1995) Optimal design of mechanical engineering systems. J. Mech. Design 117(B):55–62.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Schoenberger CR (2008) Wii’s future in motion. Forbes (December 1), http://www.forbes.com/2008/11/28/nintendo-wii-wii2 -tech-personal-cz-cs-1201wii.html.

Shane SA, Ulrich KT (2004) Technological innovation, product development, and entrepreneurship in management science. Management Sci. 50(2):133–144.

Sheffield B (2008) The graphics plateau. Game Developer 15(7):2.

Sinclair B (2006) Wii dev costs fraction of PS3’s, 360’s. Gamespot (May 5), http://www.gamespot.com/.

Srinivasan A, Venkatraman N (2010) Indirect network effects and platform dominance in the video game industry: A network perspective. IIEE Trans. Engrg. Management 57(4):661–673.

Thomke S (1999) Project Dreamcast: Serious play at Sega Enterproses Ltd. (A). Harvard Business School, case study N9-600-028.

Tirpak JA (2007) Making the best of the fighter force. Air Force Magazine 90(3):40–45.

Tiwana A, Konsynski B, Bush A (2010) Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Internat. Statist. Rev. 21(4):675–687.

van der Rhee B, Schmidt G, Tsai W (2007) Steepen, maintain, or flatten the performance treadmill? Working paper, Nyenrode Business University, Breukelen, The Netherlands, David Eccles School of Business, University of Utah, Salt Lake City.

VG Chartz Game Database (2009) Video console market share. Retrieved January 15, 2009, http://www.vgchartz .com/gamedb/?name=&publisher=&platform=Wii&genre=& minSales=0&results=200.

Wen H (2007) Analyze this: Are game publishers late to the (Wii and DS) game? Gamasutra (June 23, 2013) http://www .gamasutra.com/view/feature/130086/analyze\_this\_are\_game \_publishers\_.php?print=1.

Wesley D, Barczak G (2010) Innovation and Marketing in the Video Game Industry: Avoiding the Performance Trap (Gower Publishing Ltd., UK).

Zhu F, Iansiti M (2011) Entry into platform-based markets. Strategic Management J. 33(1):88–106.
