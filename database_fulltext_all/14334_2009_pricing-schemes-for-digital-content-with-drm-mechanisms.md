---
otero_id: 14334
otero_key: "HPU74JPZ"
title: "Pricing schemes for digital content with DRM mechanisms"
authors: "Yung-Ming Li; Chia-Hao Lin"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.05.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pricing schemes for digital content with DRM mechanisms

Yung-Ming Li ⁎, Chia-Hao Lin

Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan

## a r t i c l e i n f o

Article history: Received 25 July 2008 Received in revised form 17 February 2009 Accepted 20 May 2009 Available online 6 June 2009

Keywords: Digital content Pricing scheme Digital Right Management System collaboration Content quality Network diffusion

## a b s t r a c t

In this paper, utilizing game-theoretic model, we examine the impact of collaborative structure, content quality, and network environment on the development of pricing scheme and DRM protection policy of digital content. DRM protection level decreases and pirating activities becomes relatively tolerable as the content provider and platform provider operate collaboratively. Depending on the market structure, higher content quality may strengthen or weaken the adoption of DRM. However, it would seem that, as the network environment becomes more decentralized and uncontrolled, weaker DRM protection should be a better strategy.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent decades, there has been a huge change in the use of digital content in our daily life. Traditionally, people accessed digital content through physical storage media such as tapes or CDs. But after 1990, we encountered another intense evolution in terms of the personal computer and the Internet. The diffusion of personal computers created a general platform for almost every digital content consumer in the world and the Internet linked them together. By means of the Internet, it is possible for anyone to acquire digital content anywhere and anytime, at no cost, so the Internet has gradually become our major portal of information. Transmitting digital content on the Internet (legally) also takes less time and money than producing and buying physical storage media.

A digital product is a bundle of properties or features comprised of information that is either digitized or produced electronically. The bundle may have other properties which are intangible and not solely information-based. Digital products can be reproduced without loss in pure digital form. They may serve a speci<sup>fi</sup>c purpose, are intended to be tradable or exchangeable and can satisfy a want or need [9,26,38,50]. The technological environment and economic factors increased the popularity of digital content. Today, our life is full of various digital products and content such as music and movies, which may be played on an Apple iPod or other platforms. There is no doubt that digital products and contents are already inseparable from our daily lives. Current research shows that over 90% of produced information is in a digital format [51]. Due to the large market and Internet environment, it is inevitable that we should consider the cost for <sup>fi</sup>rms and the convenience for consumers in the construction of an all new business model which could combine personal digital devices with the Internet for digital device manufacturers. For example, Apple iPod is a success ful product in the digital music player market. It does not connect to the Internet directly but by means of personal computers where digital content is downloaded. Both <sup>fi</sup>rms and consumers can renew the content of the digital devices circularly without extra physical storage media and content providers can reduce the cost of manufacturing and transportation.

However, the open standards of personal computers, <sup>fi</sup>le formats (for example, mp3, mpeg, wma,…etc.) and convenient Internet services such as P2P technology also mean that everyone can copy and share digital content stored in these formats easily. This encourages a lot of digital content consumers to acquire them from illegal sources, instead of buying content legally. Because of similar quality and ease of copy, a lot of consumers are attracted to piracy. Recently, even digital music sales doubled. The International Federation of the Phonographic Industry (IFPI) recorded that global music sales in both physical and online styles fell to US\$1.7 billion in 2006, an 11% reduction in volume [24]. The Motion Picture Association of America (MPAA) estimated that the major motion picture studios in the United States lost US\$2.3 billion due to the illegal Internet download in 2005 [11,12]. The behavior of digital content consumers has an adverse effect upon the revenue of the digital content providers. In addition to legal action, content providers have sought a technological solution called ‘digital right management’ (DRM) technology, a kind of server-sided software developed by digital content providers to prohibit illegal distribution of digital contents [5]. The DRM systems apply “rules” to content that are usually put in place to impose constraints on the use and distribution of digital goods. These rules may include copy protection to legal versions of digital content, a limit to the number of machines or number of times content could be used, how long this content could be used, etc [13]. Besides digital music, DRM protection is also imposed on other types of digital content such as copyrighted video games (e.g. Xbox 360 and PS3).

DRM can be implemented in platform (hardware, software player) or content. For example, PressPlay.com adopted Microsoft Windows Media DRM solution to set DRM on content, while MusicNet.com adopted RealNetworks Helix DRM solution to set DRM on platform rather than content. Table 1 lists a few of popularly practical DRM technologies. As we can observe, most of the listed DRM technologies are deployed on the content. In our research, we consider the content provider assigns the DRM level. This DRM approach is also exploited by iTune and many online video websites providing authorized video clips in windows media player <sup>fi</sup>les.

DRM technology can effectively restrict consumers' illegal behaviors; however, it also reduces the <sup>fl</sup>exibility of digital content and, so, lowers its corresponding value. Some people who support freeware or fair use of digital content consider DRM technology as “Digital Restriction Management” because they think that the basic rights of digital content consumers are being violated [5]. Appropriate DRM policy should well balance the inhibition of illegal pirating and the satisfaction of its consumers.

From the perspective of business operations, it is important for digital content providers to develop an appropriate DRM protection level and pricing strategy to maximize their pro<sup>fi</sup>t. As we can expect, these polices are closely associated with the market characteristics (the interactions of content provider, platform provider, and customers), content characteristic (the quality of the objective to be protected), and network environment (channel of piracy). From the perspective of business strategy development, the exploration of how these economic and technological characteristics affect the DRM adoption and the corresponding pro<sup>fi</sup>t of the players in the market of digital content is important and essential. In this paper, utilizing a game-theoretic model, we analyze the development of the pricing strategy and DRM policy of digital content and consider the characteristics of system collaboration, content quality, and network environment. Our developed model is generic and not limited to a speci<sup>fi</sup>c type of digital content and DRM systems. The main unique <sup>fi</sup>ndings of this study are as follows:

1. From the perspective of the content industry, we showed that as the content and platform <sup>fi</sup>rms are collaboratively operated, weaker DRM protection tends to be adopted and more piracy tolerated. If differentiated contents are offered in the market, the DRM protection level set by competing content providers is always higher than that set by a monopolistic content provider.

2. From the perspective of the content design, we found that the impact of content quality on the DRM policy would be positive or negative, depending on the market structure and the customer valuation function of the content with DRM.

3. From the perspective of the content distribution, contrary to our intuition, in collaborative market, as the network environment becomes decentralized and uncontrolled, the content provider always tends to adopt lower DRM protection levels.

The remainder of this paper is organized as follows. In the next section, we review existing literature related to this research. In

Practical DRM systems.

<table><tr><td>DRM systems</td><td>Developed by</td><td>Protection setting</td></tr><tr><td>DTCP</td><td>Intel, Sony, MEI, Toshiba, Hitachi</td><td>Content</td></tr><tr><td>CPRM/CPPM</td><td>Intel, IBM, MEI, Toshiba</td><td>Content</td></tr><tr><td>HDCP</td><td>Intel</td><td>Content</td></tr><tr><td>SmartRight</td><td>THOMSON, France</td><td>Content</td></tr><tr><td>Helix</td><td>RealNetworks</td><td>Platform</td></tr></table>

Section 3, we present an analytical model to examine the pricing and DRM strategies with respect to various market con<sup>fi</sup>gurations. Section 4 calibrates the impact of system collaboration, content quality and network environment on the equilibrium results. In Section 5, we illustrate and verify the analysis via speci<sup>fi</sup>c realization of the function of the model. Section 6 we develop an extended model for a market with two competing content providers. Section 7 discusses the managerial implications of the results to digital content markets. Finally, in Section 8, we summarize our <sup>fi</sup>ndings and suggest the directions for future research.

## 2. Related literature

## 2.1. DRM systems

Piracy of digital content is considered as a serious problem faced by content companies as it will reduce their commercial bene<sup>fi</sup>ts [33]. Digital content requires technical solutions to enforce rights management and Digital Rights Management (DRM) systems are considered as the potential solutions to this problem. Rights management generally refers to the problems of copyright protection and actual usage does not exceed what is authorized. A DRM system protects and enforces the rights associated with the usage of digital content [12, 13, 18, 23, 41]. The purpose for DRM is to ensure that access to protected content is allowable only under the conditions speci<sup>fi</sup>ed. A DRM system also prevents the creation of unauthorized copies and provides a mechanism by which copies can be detected and traced. Kwok showed that the required DRM capabilities contain: (1) rights speci<sup>fi</sup>cation and rights label management; (2) content protection, rights enforcement, and trusted rendering; (3) rights authorization; (4) rights tracking; and (5) security and commerce infrastructure [31].

In practice, a DRM system can be implemented in hardware, operating system, application, and content itself [2]. But, when talking about the players in a DRM system architecture, the content creator, content rights owner, content distributor are discussed whereas the role of playing platform (hardware or software) is usually omitted [1,36]. Any usage of the protected work requires the participation of some special hardware or software to determine which usages proceed and which are blocked [16,36]. There are a number of DRM solutions on the market. For example, Kwok et al. [32] implemented DRM based on the Internet Open Trading Protocol (IOTP) on electronic commerce transactions. Among these solutions, Microsoft's Windows Media Rights Manager (WMRM), IBM's Electronic Media Management System (EMMS), InterTrust's Rights|System, and RealNetworks's RealSystems Media Commerce Suite (RMCS) are amongst the most popular ones. In this research, we consider the content providers set the DRM system though we also discuss the scenario that DRM system may be implemented collaboratively according to some commercial agreement between the content and platform providers.

## 2.2. DRM economics

The DRM-related business strategies include access control [23,46] and distribution strategy [8,35,43]. DRM may facilitate the extension of monopoly pricing, decrease the amount of information available to potential consumers, diminish the number of positive externalities, and raise artistic and informational barriers [42]. Other economic issues in DRM, such as payment receiving [36], copyright [34], social welfare [37,48], network externality [10,49], protection level [54], and the impact of piracy [18], have been studied. In addition, prior works related to the impact of DRM on the consumer choice include the concern of privacy, the restriction and inconvenience incurred [15], the fair use issues [2], and the tradeoffs between purchasing and pirating [20,21].

DRM can act as versioning [7,45,53] or product differentiation tool [44] and is widely adopted in various industries. Product differentiation can be implemented by discriminated product quality and price. DRM differentiates quality of the content and pricing naturally becomes a strategic tool attached with it. A pirated product can be treated as a substitute of the original product with different quality. For traditional goods, higher protection level may lower the quality of the pirated products [22]. However, for digital goods, it may be comparable to the original one [47]. Prior works have indicated that the existence of piracy has important impact on pricing strategy of digital content [4,6,25]. Peitz and Waelbroeck [41] suggested that a <sup>fi</sup>rm can react to piracy in three different ways: no action if it is not a threat, reduces its price to attract users, or accommodate. Peitz [40] showed that under piracy protection, there exist two types of symmetric equilibrium: both <sup>fi</sup>rms price low to target low-value users, or both <sup>fi</sup>rms set price to sell only to the highvalue users.

The diffusion of digital contents is related to the ease of piracy, and both affect the pricing strategy [28]. The popularity of Napster, Gnutella, Freenet, and other P2P platforms has changed the means of digital content distribution and established the position of the P2P network for spreading digital contents [3]. The new Internet and P2P distribution channels enhanced the sales of digital-stored products of digital content publishers [19]. These researches pointed out the of network environment on the distribution of digital contents. The growth of these channels has strengthened the diffusion of both legal and illegal copies of digital contents at the same time. Intuitively, the existence of piracy should reduce demand and thus pro<sup>fi</sup>t [30]. However, Venkatesh et al. [52] suggested that an increase in the number of illegal copies can increase the demand for legal ones.

There have been a few of works on the market of digital content embedded with DRM. In these related prior researches, two markets are implicated in digital rights management: the market for platforms (players) and the market for content [39]. And, the consumers are divided in two groups- those who have the ability to pirate and those who do not [29]. The demand for the platform is derived from the demand for the content, and the budget constraint of consumer and the pricing of digital content would in<sup>fl</sup>uence the buying decision [17]. Recently, Jime´nez et al. [27] examined optimal strategy in decision support systems by a multi-attribute utility model. These market setting and utility approach are adopted in our model.

However, the models presented in the past research lack the part of the collaborative relationships of the platform and content providers and the impact of content and distribution channel on pricing strategy. In this paper, utilizing game-theoretic model, we systematically examine the impacts of collaborative structure, content quality, and network environment on the development of pricing scheme and DRM protection policy of digital content.

## 3. The model

We consider a digital content market which involves a content platform <sup>fi</sup>rm, content provider, and consumers where the number of consumers is denoted as $\eta _ { 0 } .$ Consumers can acquire a digital content by purchasing it from the distribution channel of the content provider or pirating the content from other channels such as P2P networks. If a customer chooses to own a legal copy of the digital content, he/she needs to pay a price $p _ { c } .$ . Note that the price could also be interpreted as the fee for paying the total amount of content a customer purchase. In order to play the digital content, all customers have to purchase a platform (e.g., iPod) with a price $p _ { h } ,$ where the purchase action is irrelevant to the source of digital content. The unit cost for a platform is $c _ { h } .$ The value of digital content $v ( q , \varepsilon )$ is associated with its content quality q and the DRM protection level ε applied on it. Content quality may be judged from technical aspect (such as recording quality) and/ or content aspect (such as musical intrinsic melody quality). While DRM protection is not always perfect and may still be defeated, higher protection level will increase the dif<sup>fi</sup>culty and the effort to pirate. The ratio of using an illegal copy of content decreases as the level of DRM protection increases. Since the pirated content has less limitation caused by the DRM protection, the level of DRM protection with a pirated content is assumed to have an exogenous value $\varepsilon _ { 0 }$ which is less than that of an original copy $( \mathrm { i } . \mathrm { e } . , 0 \le \varepsilon _ { 0 } \le \varepsilon )$ . In addition, we adopt a network diffusion function ψ(ω, ε) as the non-zero probability that a customer obtains an illegal copy from other channels. The network environment parameter ω indicates the ease at which customers can acquire illegal copy. For example, in a decentralized P2P <sup>fi</sup>le sharing network, the value of ω should be higher than that in a centrallygoverned network.

Customers have heterogeneous preferences on pirated content, thus re<sup>fl</sup>ecting the disutility of the illegal behavior (such as ethical self-regulation or criminal investigations executed by organizations). Individual sensitivity to this disutility (value discount) is denoted as parameter $\delta _ { i }$ and its value follows a uniform distribution on interval [0, 1]. A customer with a higher value of $\delta _ { i }$ is less sensitive to the disutility when he/she uses the pirated content. All parameters in our model are summarized in Table 2.

A typical user i may obtain the content by legal or illegal means, or do nothing; thus, the utility function of user i can be formulated as

$$
U _ {i} = \left\{ \begin{array}{l l} v (q, \varepsilon) - p _ {c} - p _ {h} & \text { If   customer } i \text { purchases   the   content } \\ \delta_ {i} \cdot \psi (\omega , \varepsilon) \cdot v (q, \varepsilon_ {0}) - p _ {h} & \text { If   customer } i \text { pirates   the   content } \\ 0 & \text { If   customer } i \text { doesn't   buy   the   platform } \end{array} \right.\tag{1}
$$

Each customer chooses his/her best choice to maximize his/her individual utility. Note that if a user chooses to purchases the content, she de<sup>fi</sup>nitely can acquire the content, however, if she chooses to pirate the content, the probability to acquire the content is $\psi ( \omega , \varepsilon ) .$ Given the price of content and platform, the demand function of content is derived as follows.

$$
\eta = \left\{ \begin{array}{l l} \eta_ {0}, & p _ {c} + p _ {h} \leq \mathfrak {v} (q, \varepsilon) \text {   and   } p _ {c} <   \underline {{v}} \\ \hat {\delta} \cdot \eta_ {0}, & p _ {c} + p _ {h} \leq \mathfrak {v} (q, \varepsilon) \text {   and   } p _ {c} \geq \underline {{v}}, \\ 0, & p _ {c} + p _ {h} > \mathfrak {v} (q, \varepsilon), \end{array} \right.\tag{2}
$$

where $\begin{array} { r } { \underline { { \nu } } { = } v ( q , \varepsilon ) { - } \psi ( \omega , \underline { { \varepsilon } } ) \cdot v ( q , \varepsilon _ { 0 } ) \ \mathrm { a n d } \ \stackrel { \wedge } { \delta } \ = \ \frac { ( q , \varepsilon ) - p _ { c } } { \psi ( \omega , \varepsilon ) \cdot ( q , \varepsilon _ { 0 } ) } . } \end{array}$

<sup>ð Þ-ð Þ</sup>The consumer with δ̂ is indifferent to purchasing the digital content or pirating it. Customers with $\delta _ { i } \le \hat { \delta }$ ̂ will purchase the content;

Table 2 Model parameters.

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td> $\eta_0; \eta$ </td><td>Total number of consumers of the content; total number of consumers who purchases the content</td></tr><tr><td> $v(q, \varepsilon)$ </td><td>Valuation function of the digital content with content quality level  $q$  and DRM protection level  $\varepsilon. \partial v(q, \varepsilon)/q>0, \partial v(q, \varepsilon)/\varepsilon<0$ </td></tr><tr><td> $\psi(\omega, \varepsilon)$ </td><td>The probability to pirate the content when DRM protection level is  $\varepsilon$  and network environment parameter is  $\omega, 0 \leq \psi(\omega, \varepsilon) \leq 1, \partial \psi(\omega, \varepsilon)/\partial \varepsilon<0, \partial \psi(\omega, \varepsilon)/\partial \omega>0$ </td></tr><tr><td> $\delta_i$ </td><td>Discount of individual value on the illegal content,  $\delta_i \sim U[0,1]$ </td></tr><tr><td> $q$ </td><td>Content quality level</td></tr><tr><td> $c_h$ </td><td>Unit cost for a platform</td></tr><tr><td> $\varepsilon; \varepsilon_0$ </td><td>Original DRM protection level; DRM protection level of a pirated content</td></tr><tr><td> $p_c; p_h$ </td><td>Price of a content; price of a platform</td></tr></table>

however, customers with $\delta _ { i } > \mathfrak { F }$ will pirate the content because the risk of piracy is not serious for them. In order to increase the sales of legal content, one straightforward strategy is to sell the content at a lower price. Nevertheless, protection strategy has both positive and negative effects on promoting the sales of the legal digital content. First, digital content providers utilize DRM technology to cut down on the spread of piracy and so force more people to purchase legal content. However, the adoption of DRM protection also reduces the <sup>fl</sup>exibility of the digital content and results in a value decline of the content, which consequently decreases the sale amount of the content. Thus, developing appropriate pricing strategies and protection policies are essential for pro<sup>fi</sup>t-seeking platform <sup>fi</sup>rms and digital content providers. In the following sections, we will analyze these strategies under various market structures which are catalogued based on collaboration degree: the platform provider and digital content provider are fully independently operated, platform manufacturer and content provider are partially collaborative (jointly decide the DRM policy but independently decide the price level), and platform and content providers are merged completely into a single company (jointly decide all policies).

## 3.1. A market with completely independent providers

We shall <sup>fi</sup>rst consider a market structure where the platform <sup>fi</sup>rm and digital content provider in the digital content industry are independently operated. The time stages of the game are as follows. In the <sup>fi</sup>rst stage, the content provider decides on the DRM protection level ε and the price of the content $p _ { c } .$ In the second stage, the platform <sup>fi</sup>rm decides the price of the platform $p _ { h } .$ In the third stage, taking into account the prices and protection level, each customer then decides whether to purchase a platform or not. In buying the platform, he/she can decide to buy the content or pirate it. Note that while independent <sup>fi</sup>rms can move in any sequence, in this setup, we focus on that the content provider has market power and moves <sup>fi</sup>rst. The business environment evolves from the fact that each customer won't purchase the platform unless the content provider decides to offer speci<sup>fi</sup>c digital content supported by the machine. In other business scenarios: if the platform provider has higher market power and makes <sup>fi</sup>rst move, then the content provider will make no pro<sup>fi</sup>t and all users pirate; If content and platform providers make decision simultaneously, there exist in<sup>fi</sup>nite Nash equilibria. Thus, we focus on the one in which the content provider moves before the platform provider.

Using a backward induction approach, we shall <sup>fi</sup>rst examine the pricing strategy of the platform <sup>fi</sup>rm. Because digital content has a low marginal cost, for sake of convenience, we assume a zero marginal cost and revenue is equivalent to pro<sup>fi</sup>t. Since each customer has to buy a platform in order to use the digital content, the objective function of the platform <sup>fi</sup>rm is given by

$$
\max _ {p _ {h}} \pi_ {h} = (p _ {h} - c _ {h}) \cdot \eta_ {0} s. t. U _ {i} \geq 0.\tag{3}
$$

Because the digital content provider would stay out of the market when the constraint is violated, the platform <sup>fi</sup>rm has to consider the restriction. Consequently, each customer purchases the platform and then decides to buy the content or pirate it. Therefore, taking into account the price and the DRM protection level decided by the content provider, the best pricing strategy of the platform <sup>fi</sup>rm would be $p _ { h } ^ { * } = v ( q , \varepsilon ^ { * } ) - p _ { c } ^ { * }$ . Next, according to the price of the platform, the objective function of the digital content provider can be formulated as follows.

$$
\max _ {p _ {c}, \varepsilon} \pi_ {c} = p _ {c} \cdot \eta = p _ {c} \cdot \frac {\left(\mathbf {v} (q , \varepsilon) - p _ {c}\right) \cdot \eta_ {0}}{\psi (\boldsymbol {\omega} , \varepsilon) \cdot \mathbf {v} (q , \varepsilon_ {0})} s. t. \mathbf {v} (q, \varepsilon) - p _ {c} \geq 0.\tag{4}
$$

Similarly, the platform <sup>fi</sup>rm has an incentive to join the digital content market due to the constraint of (4). Because, according to economic literature, users prefer content with higher quality and less protection (with more rights to utilize the content), we assume that the bene<sup>fi</sup>cial function of digital content with DRM protection has the properties as follows.

$$
\begin{array}{l} \partial \mathfrak {v} (q, \varepsilon) / \partial q > 0, \quad \partial^ {2} \mathfrak {v} (q, \varepsilon) / \partial q ^ {2} \leq 0, \quad \partial \mathfrak {v} (q, \varepsilon) / \partial \varepsilon <   0 \\ \text { and } \quad \partial^ {2} \mathfrak {v} (q, \varepsilon) / \partial \varepsilon^ {2} \leq 0. \end{array}\tag{5}
$$

Furthermore, we assume that $v ( 0 , \varepsilon ) { \leq } 0$ because customers don't receive any bene<sup>fi</sup>t from content without value. On the other hand, rigid DRM protection reduces the possibility of customers acquiring illegal content from other channels, whereas a <sup>fi</sup>le-sharing network environment encourages piracy. Therefore, we assume that the diffusion function has properties as follows.

$$
\begin{array}{l} \partial \psi (\omega , \varepsilon) / \partial \varepsilon <   0, \quad \partial \psi (\omega , \varepsilon) / \partial \omega > 0, \quad \partial^ {2} \psi (\omega , \varepsilon) / \partial \varepsilon^ {2} \geq 0, \\ \text { and } \quad \partial^ {2} \psi (\omega , \varepsilon) / \partial \omega^ {2} \leq 0. \end{array}\tag{6}
$$

Lemma 1. (Optimal strategies in a market with completely independent providers)

If the digital content industry is operated by a completely independent platform firm and content provider,

(i) the optimal DRM protection level $\varepsilon _ { 1 } ^ { * }$ can be obtained by solving ${ \cal { I } } _ { 1 } = 0 ,$ where

$$
\Gamma_ {1} = \psi (\pmb {\omega}, \varepsilon) \cdot \frac {\partial \pmb {v} (\pmb {q} , \varepsilon)}{\partial \varepsilon} - \frac {1}{2} \cdot \pmb {v} (\pmb {q}, \varepsilon) \cdot \frac {\partial \psi (\pmb {\omega} , \varepsilon)}{\partial \varepsilon}.
$$

(ii) the digital content provider and platform firm charge the same prices. Formally, $p _ { c } ^ { * } = \operatorname* { m i n } ( v ( q , \varepsilon _ { 1 } ^ { * } ) / 2 , v ( q , \varepsilon _ { 1 } ^ { * } ) - c _ { h } )$ and $p _ { h } ^ { * } = \operatorname* { m a x } ( v ( q ,$ $\varepsilon _ { 1 } ^ { * } ) / 2 , c _ { \mathrm { h } } )$ , where $0 \leq c _ { h } \leq v ( q , \ \varepsilon _ { 1 } ^ { * } )$ . (All proof can be found in Appendix)

From Lemma 1, the demand for legal digital content and respective pro<sup>fi</sup>ts can be rewritten as follows:

$$
\eta^ {*} = \frac {v (q , \varepsilon_ {1} ^ {*}) \cdot \eta_ {0}}{2 \psi (\omega , \varepsilon_ {1} ^ {*}) \cdot v (q , \varepsilon_ {0})}, \pi_ {c} ^ {*} = \frac {v ^ {2} (q , \varepsilon_ {1} ^ {*}) \cdot \eta_ {0}}{4 \psi (\omega , \varepsilon_ {1} ^ {*}) \cdot v (q , \varepsilon_ {0})}, \pi_ {h} ^ {*} = \left(\frac {v (q , \varepsilon_ {1} ^ {*})}{2} - c _ {h}\right) \cdot \eta_ {0}.\tag{7}
$$

We <sup>fi</sup>nd that the adoption of a DRM mechanism will result in not only the reduction in the price of digital content but also in the price of the platform. The adoption of a DRM mechanism will always have a negative impact on the pro<sup>fi</sup>t of the platform <sup>fi</sup>rm because the platform <sup>fi</sup>rm needs to compensate for a portion of individual utility loss due to the inconvenience incurred by the DRM restriction. On the other hand, the platform <sup>fi</sup>rm is always better off if the content provider offers a higher quality of content because it increases the whole value of using the digital content. As a result, the customers are also willing to pay more for the platform when higher content quality is provided. Furthermore, the effect of content quality on the content provider's revenue is not monotonic although the price of content increases with its quality. This economics driving force for this quality effect will be analyzed and discussed in Section 4.2.

## 3.2. A market with providers collaborating on DRM policy

In this section, we further consider the same scenario in Subsection 3.1 except in this case the content provider and platform <sup>fi</sup>rm jointly decide the DRM protection level. In this new setup, the DRM protection level is agreeable to both sides in advance; in other words, both <sup>fi</sup>rms negotiate the DRM protection level before all stages for maximizing total pro<sup>fi</sup>t. In the process $\boldsymbol { \mathrm { o f } }$ negotiation, a side-payment (revenue sharing or compensation) mechanism is essential to encourage cooperation. The side payment is some kind of license fee paid to the content provider by the platform <sup>fi</sup>rm. For example, consumers buy iPod mp3 platforms from Apple and acquire new content which is provided by collaborated music companies from iTunes online music stores.

Thus, the objective function where both <sup>fi</sup>rms jointly decide the DRM protection level for maximizing total pro<sup>fi</sup>t is given by:

$$
\max _ {\varepsilon} \pi_ {c + h} = \left(\frac {p _ {c} \cdot (\mathfrak {v} (q , \varepsilon) - p _ {c})}{\psi (\omega , \varepsilon) \cdot \mathfrak {v} (q , \varepsilon_ {0})} + (p _ {h} - c _ {h})\right) \cdot \eta_ {0}.\tag{8}
$$

Lemma 2. (Optimal strategies in a market with <sup>fi</sup>rms collaborating on DRM policy)

If the industry is operated by collaborative content and platform providers,

(i) the optimal DRM protection level ε⁎ can be obtained by solving $\begin{array} { r l } & { \Gamma _ { 2 } { = } \overset { \cdot } { 0 } , w h e r e \Gamma _ { 2 } \overset { \cdot } { = } 2 \mathfrak { v } ( q , \varepsilon ) \cdot \psi ( \omega , \varepsilon ) \cdot \frac { \partial \mathfrak { v } ( q , \varepsilon ) } { \partial \varepsilon } - \mathfrak { v } ^ { 2 } ( q , \varepsilon ) \cdot \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \varepsilon } \ + } \\ & { 2 \psi ^ { 2 } ( \omega , \varepsilon ) \cdot \mathfrak { v } ( q , \varepsilon _ { 0 } ) \cdot \frac { \partial \mathfrak { v } ( q , \varepsilon ) } { \partial \varepsilon } . } \end{array}$

(ii) the digital content provider and platform firm charge the same prices. Formally, $\stackrel { \cdot } { p _ { c } ^ { * } } = \mathrm { m i n } ( v ( \stackrel { \cdot } { q } , \stackrel { \cdot } { \varepsilon _ { 1 } ^ { * } } ) / 2 , \stackrel { \cdot } { v } ( q , \stackrel { \varepsilon * } { \varepsilon _ { 1 } ^ { * } } ) - c _ { \mathrm { h } } )$ and $p _ { h } ^ { * } { = } \operatorname* { m a x } ( v ( q , \varepsilon _ { 1 } ^ { * } ) / 2 , c _ { h } )$

From Lemma 2, the demand for legal digital content and respective revenues are the same as Eq. (7) except where $\varepsilon _ { 1 } ^ { * }$ is substituted by ε⁎. The total revenue of a partially collaborating mode is higher than that gained in a competitive market.

## Lemma 3. (Maximal demand size of the digital content provider)

Given the price levels of the content and the platform, $p _ { c } ^ { * }$ and $p _ { h } ^ { * } ,$

(i) the maximal demand size of the digital content provider can be achieved by setting $\varepsilon = \hat { \varepsilon } _ { \eta }$ which is derived by solving ${ \varGamma } _ { \eta } = 0$ where $\begin{array} { r } { \begin{array} { r } { \boldsymbol { \Gamma } _ { \eta } = \psi ( \boldsymbol { \omega } , \varepsilon ) \cdot \frac { \partial { \bf v } ( \boldsymbol { q } , \varepsilon ) } { \partial \varepsilon } - { \bf v } ( \boldsymbol { q } , \varepsilon ) \cdot \frac { \partial \psi ( \boldsymbol { \omega } , \varepsilon ) } { \partial \varepsilon } . } \end{array} } \end{array}$

(ii) the sign of ∂η⁎/∂ε is the same as that $o f { \cal { T } } _ { \eta } ( \varepsilon )$

Form Lemma 3, we <sup>fi</sup>nd that when the DRM protection level is small $( \varepsilon < \hat { \varepsilon } _ { \eta } ) .$ , the positive effect of DRM (anti-pirating) can force customers to purchase legal content. However, if the DRM protection level is suf<sup>fi</sup>ciently high $( \varepsilon > \hat { \varepsilon } _ { \eta } )$ , the negative effect of DRM (in<sup>fl</sup>exibility) would result in what more people prefer, that is the acquisition of illegal digital content from other channels. In Section 4.1, we will show that the type of system con<sup>fi</sup>guration (market structure) plays an important role in the developing of DRM policy and of corresponding pricing strategies. We will also examine the implications of system collaboration within the digital content industry.

## 3.3. A market with completely integrated providers

In this scenario, the digital content provider and platform <sup>fi</sup>rm are completely integrated into a single company. For example, when we enjoy PlayStation 3 video games, the games and platforms are all provided by Sony Computer Entertainment Inc. This kind of market structure is not so common in the real world, because mastering different industries is dif<sup>fi</sup>cult for general <sup>fi</sup>rms. The objective function of the fully integrated <sup>fi</sup>rm for maximizing the total revenue is given by

$$
\max _ {\varepsilon , p _ {c}, p _ {h}} \pi_ {c + h} = \left(\frac {p _ {c} \cdot (\mathbf {v} (q , \varepsilon) - p _ {c})}{\psi (\boldsymbol {\omega} , \varepsilon) \cdot \mathbf {v} (q , \varepsilon_ {0})} + (p _ {h} - c _ {h})\right) \cdot \eta_ {0} s. t. U _ {i} \geq 0.\tag{9}
$$

Lemma 4. (Optimal strategies in a market with completely integrated providers)

If the industry is operated by a completely integrated provider,

(i) the DRM protection leve $\varepsilon ^ { * }$ is no more needed in the fully merged market structure. Formally, $\varepsilon ^ { * } = \varepsilon _ { 0 } .$

(ii) the integrated company charges the highest platform fee and distributes digital content freely. Formally, $p _ { c } ^ { * } = 0$ and $p _ { h } ^ { * } = \mathtt { m a x }$ $( v ( q , \varepsilon _ { 0 } ) , c _ { h } )$

The result shows that the integrated <sup>fi</sup>rm will take all of the revenue from platform selling. In this scenario, because each customer uses legal content without any fees, the DRM protection level is minimized for maximizing total revenue. That is, the fully integrated <sup>fi</sup>rm will sacri<sup>fi</sup>ce its content revenue but maximize its revenue from platform selling. Notice if $v ( q , \varepsilon _ { 0 } ) < c _ { h } ,$ then the market will fail as the platform is too expensive and no one will buy the platform to play digital content.

Compared with the channels of digital content, the cost of each customer acquiring an illegal platform is suf<sup>fi</sup>ciently high. For instance, each customer purchasing an illegal platform has to know how to maintain and upgrade the platform. Moreover, they cannot use customized online services which legal platforms can receive freely. In fact, from the viewpoint of switching cost, the fully integrating <sup>fi</sup>rm often uses free digital content as an incentive to boost sales in the short-run for raising its market share.

## 4. Analysis of pricing scheme and DRM policy

## 4.1. The impact of system collaboration

η⁎ denotes market share in a market with independent content and platform providers and $\eta _ { 2 } ^ { * }$ in a collaborative market. In this section, we examine DRM protection policies, market shares, and revenues as they relate to independent providers and to collaborating providers. Subsequently, we examine the managerial implications of the market integration.

## 4.1.1. DRM protection policy and demand

We <sup>fi</sup>rst compare the equilibrium DRM protection levels in these two markets. It is worth pointing out that $\boldsymbol { { \Gamma } } _ { 2 }$ and $\boldsymbol { { \Gamma } } _ { \eta }$ can be rewritten as follows:

$$
\Gamma_ {2} = 2 \boldsymbol {v} (\boldsymbol {q}, \varepsilon) \cdot \Gamma_ {1} + 2 \psi^ {2} (\boldsymbol {\omega}, \varepsilon) \cdot \boldsymbol {v} (\boldsymbol {q}, \varepsilon_ {0}) \cdot \frac {\partial \boldsymbol {v} (\boldsymbol {q} , \varepsilon)}{\partial \varepsilon}.\tag{10}
$$

$$
\Gamma_ {\eta} = \Gamma_ {1} - \frac {1}{2} \cdot \mathbf {v} (q, \varepsilon) \cdot \frac {\partial \psi (\pmb {\omega} , \varepsilon)}{\partial \varepsilon}.\tag{11}
$$

From Lemma 1 and Lemma 2, we know that $I _ { 1 } ( \varepsilon _ { 1 } ^ { * } ) { = } 0$ and $\begin{array} { r } { { \cal I } _ { 2 } ( \varepsilon _ { 2 } ^ { * } ) = 0 . } \end{array}$ Moreover, due to $\partial v ( q , \varepsilon ) / \partial \varepsilon < 0 ,$ , we <sup>fi</sup>nd the second term of $\mathsf { E q . } \left( 1 0 \right)$ is always negative. In other words, ${ \varGamma } _ { 2 } ( \varepsilon _ { 1 } ^ { * } ) { < } { \varGamma } _ { 1 } ( \varepsilon _ { 1 } ^ { * } ) { = } 0$ holds and it shows the relation $\varepsilon _ { 1 } ^ { * } { > } \varepsilon _ { 2 } ^ { * }$ . Similarly, because of ∂ψ(ω, ε)/∂εb0, we <sup>fi</sup>nd that the second term of Eq. (11) is always positive. That is, $T _ { \eta } ( \varepsilon _ { 1 } ^ { * } ) > \Gamma _ { 1 } ( \varepsilon _ { 1 } ^ { * } ) = 0$ holds and it shows the relation $\varepsilon _ { \eta } ^ { * } { > } \varepsilon _ { 1 } ^ { * }$ . The result reveals that system collaboration will weaken the adoption of DRM technology. Actually, less protection will lead to more pirating activities; however, it also enhances the value of the content. When all customers decide to purchase or pirate digital content, the collaborating <sup>fi</sup>rm can generate higher total revenue from selling platforms because the price of the platforms is proportional to the value of the content. Furthermore, from Lemma $^ { 3 , }$ since the market share of digital content is positively proportional to the level of DRM protection when the level of DRM protection is less than $\varepsilon _ { \eta } ^ { \ast } ,$ we know that $\eta _ { 2 } ^ { * } { < } \eta _ { 1 } ^ { * }$ because of $\varepsilon _ { \eta } ^ { * } { > } \varepsilon _ { 1 } ^ { * } { > } \varepsilon _ { 2 } ^ { * }$

## 4.1.2. Revenue of the content and platform providers

Because the revenue functions of the content provider in these two markets are identical, we know that the revenue of the content provider in the collaborative mode will decrease due to $\varepsilon _ { 2 } ^ { * } \neq \varepsilon _ { 1 } ^ { * } .$ However, adopting $\varepsilon _ { 2 } { ^ * }$ can enhance the value of the content and, moreover, the price of platform becomes positively proportional to the value of the content; thus, total revenue may be improved. Since the content provider in the collaborative mode would receive less revenue, the platform <sup>fi</sup>rm should compensate the content provider for the loss and decline of content sales.

## Proposition 1. (Effects of system collaboration)

The effects of system collaboration are summarized in Table 3. When the content provider and the platform firm operate collaboratively:

(i) Adoption of DRM protection will be weakened.

(ii) Both the price of content and platform will increase.

(iii) Sales and revenue of content will decline.

(iv) The collaborative company gains from the extra revenue by selling platform at a high price, which compensates for the loss in reduced content sales.

One of the most popular collaborating systems could be Apple's iPod platform and iTunes online music stores. iPod already has over half the share of the digital music playing platform market and the success of iPod has also accelerated the development of online music stores. Although Apple is not an original digital music provider, it plans to provide high quality (256 kbps) music without DRM protection for all songs from EMI in the online music stores. In addition, DRM-free music is \$1.29 per song. This is more expensive than an original one (\$0.99 per song). This industrial practice of providing music with weaker DRM protection and higher price in a collaborative system is consistent with our analytical results. The managerial implication indicates that while the digital content providers offer excellent content or services, they actually generate more revenue from other complementary sources rather than their contents. The increasing revenue is mainly gained from selling platforms or offering other new services.

## 4.2. The impact of content quality

In this section, we examine the impact of content quality on the level of DRM protection in both independent and collaborative market structures. We consider that a customer's valuation function is separable or non-separable; that $\mathrm { i } s , v ( q , \varepsilon ) = v _ { q } ( q ) + v _ { \varepsilon } ( \varepsilon ) \ \mathrm { o r } \ v ( q , \varepsilon ) = v _ { q }$ $( q ) \cdot v _ { \varepsilon } ( \varepsilon ) . \operatorname { I f } v ( q , \varepsilon )$ is separable, then the effects of content quality and DRM protection are independent, that is $\partial ^ { 2 } v ( q , \varepsilon ) / \partial q \partial \varepsilon = 0 . \operatorname { I f } v ( q , \varepsilon )$ is non-separable, these effects are correlated, that is, $\partial ^ { 2 } v ( q , \ \varepsilon ) /$ $\partial q \partial \varepsilon = \partial v _ { q } ( q ) / \partial _ { q } \cdot \partial v _ { \varepsilon } ( \varepsilon ) / \partial \varepsilon < 0 .$ . Based on the distinct valuation functions, the <sup>fi</sup>ndings are given by Proposition 2 as follows.

## Proposition 2. (Effects of content quality)

Case 1: If a customer's valuation function is separable $( i . e . , v ( q , \varepsilon ) =$ $v _ { q } ( q ) + v _ { \varepsilon } ( \varepsilon ) )$

(i) when the content provider and platform firm are independently operated, increasing content quality always results in stronger DRM protection.

(ii) when the content provider and platform firm are jointly operated, increasing content quality results in stronger (weaker) DRM protection when the content quality is sufficiently high (low).

Table 3  
Effects of system integration.

<table><tr><td></td><td> $\varepsilon^{*}$ </td><td> $p_{c}^{*}$ </td><td> $\eta^{*}$ </td><td> $\pi_{c}^{*}$ </td><td> $p_{h}^{*}$ </td><td> $\pi_{h}^{*}$ </td><td> $\pi_{c}^{*} + \pi_{h}^{*}$ </td></tr><tr><td>Integration</td><td>-</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+</td><td>+</td></tr></table>

Case 2: I f a customer's valuation function is non-separable $( i . e . , v ( q , \varepsilon ) =$ $v _ { q } ( q ) \cdot v _ { \varepsilon } ( \varepsilon ) )$ ,

(iii) when the content provider and platform firm are independently operated, the optimal level of DRM protection remains the same no matter how content quality changes,

(iv) when the content provider and platform firm are jointly operated, increasing content quality results in weaker DRM protection.

Proposition 2 indicates that the results are associated with the form of valuation function. If a customer's valuation function is separable, the analytical results are driven as follows: when the content provider raises content quality, the price of digital content also increases. Thus, customers planning to purchase legal copies of content may change their minds and acquire illegal copies of content from other channels due to the incentive that they could save a large amount of money in so doing. Consequently, the independent content provider exerts stronger DRM protection to inhibit such piracy. However, if the system is operated by a collaborative <sup>fi</sup>rm, both revenue from content and platform are considered. The marginal revenue of content sales (higher DRM protection to inhibit pirating) outweighs that of platform sales (less DRM protection to increase the price of the platform) and the collaborative <sup>fi</sup>rm would be better advised to adopt a stronger DRM protection policy as content quality becomes suf<sup>fi</sup>ciently high. On the contrary, when the content quality is low, the marginal revenue of selling platforms is higher than that of selling content; therefore, the collaborative <sup>fi</sup>rm prefers a weaker DRM protection level.

If the customer's valuation function is non-separable, in a market with independent content and platform providers, the effects of content quality on the optimal level of DRM protection (valuation reduction and pirate inhibition) is canceled off. That is, the DRM protection remains the same when the independent content provider changes content quality. However, if the system is operated by a collaborative <sup>fi</sup>rm, the marginal revenue of selling platforms is always higher than that of selling content when content provider offers contents with higher quality. As a result, DRM protection level becomes weaker.

For real cases, separable valuation function seems to be better justi-<sup>fi</sup>able, for example, high de<sup>fi</sup>nition movies stored in the newest storage media, Blu-ray Disc, are treated with the highest and most complex level of DRM protection. Many prestigious hardware manufactures and digital content providers ensure that DRM speci<sup>fi</sup>cations are stringently applied to this high quality media. Advanced Access Control System is embedded in it to ensure accurate key veri<sup>fi</sup>cation, player identi<sup>fi</sup>cation, and BD-ROM Mark copy protection. But lower de<sup>fi</sup>nition movies stored in traditional DVD format are only equipped with Content Scramble System which provides less DRM protection. The above real cases justify the result (i) in Proposition 2. On the other hand, the fact that Apple (a proprietary digital content and platform provider) provides higher quality (256 kbps) music without DRM protection but offers lower quality (192 kbps) music with the original “Fairplay” DRM protection [14] justi<sup>fi</sup>es the result (ii) in Proposition 2.

## 4.3. The impact of network diffusion

The recent emergence of network technologies, such as P2P networks, signi<sup>fi</sup>cantly facilitates the distribution of digital content. It is interesting to examine how a content provider reacts to an increasingly uncontrolled network environment where illegal content is easily acquired. High (Low) level ω indicates that the network environment has become more decentralized (centralized) and uncontrolled (supervisory). As in the previous section, we also consider the DRM policy in the independent and collaborative market structures under two different cases. In the <sup>fi</sup>rst case, the probability function that one pirates the digital content is separable $( \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) +$ $\psi _ { \varepsilon } ( \varepsilon ) )$ ). In the other case, the probability function is non-separable $( \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) \cdot \psi _ { \varepsilon } ( \varepsilon ) )$ . If $\psi ( \omega , \varepsilon )$ is separable, then the effects of network environment and DRM protection are independent, that is $\partial ^ { 2 } \psi ( \omega , \ \varepsilon ) / \partial \omega \partial \varepsilon = 0 .$ If $\psi ( \omega , \varepsilon )$ is non-separable, these effects are correlated, that is, $\partial ^ { 2 } \psi ( \omega , \varepsilon ) / \partial \omega \partial \varepsilon = \partial \psi _ { \omega } / \partial \boldsymbol { \omega } \cdot \partial \psi _ { \varepsilon } ( \varepsilon ) / \partial \varepsilon < 0$

## Proposition 3. (Effects of network diffusion)

Case 1: If the probability function that one pirates the digital content is separable $( i . e . , \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) + \psi _ { \varepsilon } ( \varepsilon ) )$

(ii) the content provider in both market structures would adopt weaker DRM protection as the network environment becomes highly decentralized and uncontrolled.

Case 2: If the probability function that one pirates the digital content is non-separable $( i . e . , \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) \cdot \psi _ { \varepsilon } ( \varepsilon ) )$

(ii) the DRM policy adopted by the content provider in independent market structure remains unchanged as the network environment changes to become controlled or uncontrolled.

(iii) the content provider in a collaborative market structure will adopt weaker DRM protection as the network environment becomes highly decentralized and uncontrolled.

Proposition 3 reveals that in either diffusion function, the content provider would not adopt stronger DRM protection in reaction to the emergence of ef<sup>fi</sup>cient but uncontrollable distribution channels such as P2P networks. The reason for the counterintuitive <sup>fi</sup>nding is that the negative effect of DRM on the infeasibility of using content (as well as the reduction of the platform price in collaborative market structure) is higher than the bene<sup>fi</sup>t of DRM inhibiting piracy when the network environment becomes more decentralized and uncontrollable. If the probability function is non-separable, in a market with independent content and platform providers, the effects of network environment on the optimal level of DRM protection is canceled off and the DRM protection remains the same as the network environment evolve.

Several real cases also reveal that lots of content providers reduce DRM protection level in the open Internet world. As the Internet environment becoming free and decentralized gradually, the iTunes store, run by Apple, provided DRM-free music for people to purchase in 2007. One of Europe's largest online music retailers, Musicload.de, also announced to against strong DRM protection in 2007. The Canadian Broadcasting Corporation released a DRM-free version of its television program through BitTorrent in 2008.

## 5. Example

In this section, we illustrate optimal pricing and DRM policy using speci<sup>fi</sup>c function formulation which satis<sup>fi</sup>es the properties described in the model. Content valuation function $v ( q , \varepsilon )$ is formulated in an additive (separable) form while network diffusion ψ(ω, ε) is in a productive (non-separable) form:

$$
\left\{ \begin{array}{l} v (q, \varepsilon) = m a x (\theta q - \sigma_ {\varepsilon}, 0) \\ \psi (\omega , \varepsilon) = m i n (\omega / \varepsilon , 1) \end{array} \right., \text {   where   } \theta , \sigma > 0.\tag{12}
$$

Plugging $\operatorname { E q . }$ (12) into $\Gamma _ { 1 } ,$ we have the optimal content DRM protection level and prices in a market with completely independent providers:

$$
\varepsilon_ {1} ^ {*} = \frac {\theta q}{3 \sigma}, p _ {c} ^ {*} = p _ {h} ^ {*} = \frac {\theta q}{3}.\tag{13}
$$

Substituting $\varepsilon _ { 1 } { ^ * }$ into $\eta ^ { * }$ and $\pi _ { c } ^ { * } \left( \mathrm { E q . } \left( 7 \right) \right)$ , we obtain a sale amount and revenue of the digital contents.

$$
\eta^ {*} = \frac {\theta^ {2} q ^ {2} \eta_ {0}}{9 \omega \sigma (\theta q - \sigma \varepsilon_ {0})}, \pi_ {c} ^ {*} = \frac {\theta^ {3} q ^ {3} \eta_ {0}}{2 7 \omega \sigma (\theta q - \sigma \varepsilon_ {0})}.\tag{14}
$$

Similarly, we substitute the functions $v ( q , \varepsilon )$ and $\psi ( \omega , \varepsilon )$ described in Eq. (12) into equation $\boldsymbol { { \Gamma } } _ { 2 }$ to obtain the optimal content,

DRM protection level and price levels in a market with collaborative providers:

$$
\varepsilon_ {2} ^ {*} = \frac {2 \theta q - \sqrt {\theta^ {2} q ^ {2} + 6 \omega \sigma (\theta q - \sigma \varepsilon_ {0})}}{3 \sigma},\tag{15}
$$

$$
p _ {c} ^ {*} = \frac {\theta q + \sqrt {\theta^ {2} q ^ {2} + 6 \omega \sigma (\theta q - \sigma \varepsilon_ {0})}}{6}, p _ {h} ^ {*} = p _ {c} ^ {*}.
$$

Then, we get the sale amount and revenue of the content:

$$
\eta^ {*} = \left(\frac {\theta^ {2} q ^ {2} + \theta q \sqrt {\theta^ {2} q ^ {2} + 6 \omega \sigma (\theta q - \sigma_ {\varepsilon_ {0}})}}{1 8 \omega \sigma (\theta q - \sigma_ {\varepsilon_ {0}})} - \frac {1}{3}\right) \eta_ {0}.\tag{16}
$$

Next, the revenue of the collaborative content provider is obtained as:

$$
\pi_ {c} ^ {*} = \frac {\left(2 \theta^ {3} q ^ {3} + 2 \left(\theta^ {2} q ^ {2} - 3 \omega \sigma (\theta q - \sigma_ {\varepsilon_ {0}})\right) \sqrt {\theta^ {2} q ^ {2} + 6 \omega \sigma (\theta q - \sigma_ {\varepsilon_ {0}})}\right) \eta_ {0}}{1 0 8 \omega \sigma (\theta q - \sigma_ {\varepsilon_ {0}})}.\tag{17}
$$

## 5.1. Numerical results

Comparisons of the equilibrium results of these two market structures are shown in the following <sup>fi</sup>gures. Value of parameters σ and $\varepsilon _ { 0 }$ set as 0.9 and 0.9. Parameters $( p _ { c 1 } , \varepsilon _ { 1 } , \eta _ { c 1 } , \pi _ { c 1 } )$ represent the price of content, DRM protection level, content sale amount and revenue of the content in a market with independent providers and $( p _ { c 2 } , \varepsilon _ { 2 } , \eta _ { c 2 } ,$ π ) represent those in a collaborative market.

Figs. 1–4 (ω=0.45) show the results of numerical experiments on the parameter q. The argument from Proposition 1 states that system collaboration will result in higher price of content, weaker DRM protection, less sale amount and revenue of content. This is veri<sup>fi</sup>ed in the numerical examples. Fig. 1 shows the evidence of higher price in a collaborative market. Fig. 2 depicts the phenomenon that the effect of content quality on the DRM policy is not always positive when the providers operate collaboratively. The impact of content quality on DRM policy is opposite on these two market structures if quality is too low. From Fig. 3, we can also see that the impact of content quality on sale amount of the content is similar in two markets. The quality levels with minimum sale amount in both market structures are identical. Fig. 4 indicates that the quality level q̂, which has minimum revenue of content in a collaborative market, is higher than the one in an independent market.

Figs. 5–8 show the results of numerical experiments on the parameter ω. As Proposition 3 indicated, if the effects of network environment and DRM protection level on the diffusion of piracy are non-separable, the collaborative <sup>fi</sup>rms will adopt weaker DRM protection level and higher price as the network environment becomes more uncontrollable. But the independent <sup>fi</sup>rms will maintain the original price and DRM protection level as Figs. 5 and 6 showed. The above behaviors lead to widespread piracy and to less people purchasing legal versions of content. The sales and revenue will decrease as Figs. 7 and 8 showed.

![](/api/attachments/HPU74JPZ/fulltext/images/43200c1d157d6a896cb64014c84f5ccf48201a64c06f463c84f97e324a792cc8.jpg)  
Fig. 1. Impact of content quality on price levels

![](/api/attachments/HPU74JPZ/fulltext/images/f7c0f7d37e1ebfc4612f7a5c06b80775adc1b15b868e806b0c48325a87b4c50f.jpg)  
Fig. 2. Impact of content quality on DRM levels.

## 6. Extended model: a market with competing content providers

In this section, we extend the model to consider a market with two competing content providers. These two providers, identi<sup>fi</sup>ed as A and $B ,$ offer different types of content with DRM level $\varepsilon _ { A }$ and ε respectively. The price levels of these two types of content are $p _ { c _ { A } }$ and $p _ { c _ { B } \bullet }$ In the competition game, these two competing content providers decide the DRM levels simultaneously <sup>fi</sup>rst and then decide the price levels simultaneously after the DRM levels are observed.

Denote j as the content type offered by content provider $j , j \in \{ A , B \}$ }. The utility of typical customer i is represented as

$$
U _ {i} = \left\{ \begin{array}{l l} v _ {i} \big (q _ {j}, \varepsilon_ {j} \big) - p _ {c _ {j}} - p _ {h} & \text {   If   customer   } i \text {   purchases   the   content   } j \\ \delta_ {i} \cdot \psi \big (\omega , \varepsilon_ {j} \big) \cdot v _ {i} \big (q _ {j}, \varepsilon_ {0} \big) - p _ {h} & \text {   If   customer   } i \text {   pirates   the   content   } j \\ 0 & \text {   If   customer   } i \text {   doesn't   buy   the   platform } \end{array} \right..\tag{18}
$$

We assume $\eta _ { A }$ customers are A type customers who have higher preference to content A and $\eta _ { B }$ customers are B type customers who have higher preference to content B. For simplicity, the content value functions of these two types of customers are represented as ${ v _ { A } } ( { q } , \varepsilon )$

![](/api/attachments/HPU74JPZ/fulltext/images/98a1398bb7a24f15e6ebc60a74feb6691ec53145260c64e266957743c6f59ae4.jpg)  
Fig. 3. Impact of content quality on content sale amount.

![](/api/attachments/HPU74JPZ/fulltext/images/9a3db3f81823d101285482a9a363357a40b19e3817b2a07ed4099129314969d4.jpg)  
Fig. 4. Impact of content quality on revenue of content.

![](/api/attachments/HPU74JPZ/fulltext/images/1cb618a650c8d97d399fae5ac9eadae642f96504de015d91051057a749a5f667.jpg)  
Fig. 5. Impact of network on price levels.

![](/api/attachments/HPU74JPZ/fulltext/images/14811f0cac7d1cf3121bbdfb21efd0c27a02ab390cac2d364dd51d309472db4d.jpg)  
Fig. 6. Impact of network on DRM levels.

![](/api/attachments/HPU74JPZ/fulltext/images/7d571ed65a46ff2564c08b0e7faeee8526e30cd3548041a7ee28edd21327629c.jpg)  
Fig. 7. Impact of network on content sale amount.

![](/api/attachments/HPU74JPZ/fulltext/images/2d6e0adb34e9909d5d1d4dc98314a9c5ef1635ae59bec6e9bf54bb1984682e44.jpg)  
Fig. 8. Impact of network on revenue of content.

and $v _ { B } ( q , \varepsilon )$ , where $v _ { A } ( q _ { A } , \varepsilon _ { A } ) > v _ { A } ( q _ { B } , \varepsilon _ { B } )$ and ${ v _ { B } } ( q _ { B } , \varepsilon _ { B } ) > v _ { B } ( q _ { A } , \varepsilon _ { A } )$ The revenue functions for these two segmented markets are for mulated as

$$
\pi_ {A} (q, \varepsilon , p) = \frac {p (\upsilon_ {A} (q , \varepsilon) - p) \eta_ {A}}{\psi (\omega , \varepsilon) \cdot \upsilon_ {A} (q , \varepsilon_ {0})} \quad \mathrm{and} \quad \pi_ {B} (q, \varepsilon , p) = \frac {p (\upsilon_ {B} (q , \varepsilon) - p) \eta_ {B}}{\psi (\omega , \varepsilon) \cdot \upsilon_ {B} (q , \varepsilon_ {0})}.\tag{19}
$$

Denote ${ p _ { c _ { A } } } ^ { * }$ and ${ p _ { c _ { B } } } ^ { * }$ are undercut-proof equilibrium prices. The conditions that both competing content providers have no incentive to undercut its competitor's price are

$$
\begin{array}{l} \pi_ {A} \Big (q _ {A}, \varepsilon_ {A}, p _ {c _ {A}} ^ {*} \Big) \geq \pi_ {A} \Big (q _ {A}, \varepsilon_ {A}, p _ {c _ {B}} ^ {*} - \rho_ {B A} \Big) + \pi_ {B} \Big (q _ {A}, \varepsilon_ {A}, p _ {c _ {B}} ^ {*} - \rho_ {B A} \Big) \\ \pi_ {B} \Big (q _ {B}, \varepsilon_ {B}, p _ {c _ {B}} ^ {*} \Big) \geq \pi_ {A} \Big (q _ {B}, \varepsilon_ {B}, p _ {c _ {A}} ^ {*} - \rho_ {A B} \Big) + \pi_ {B} \Big (q _ {B}, \varepsilon_ {B}, p _ {c _ {A}} ^ {*} - \rho_ {A B} \Big), \end{array}\tag{and (20}
$$

where

$$
\begin{array}{r l} & {\rho_ {B A} = v _ {B} (q _ {B}, \varepsilon_ {B}) - v _ {B} (q _ {A}, \varepsilon_ {A}), \quad \rho_ {A B} = v _ {A} (q _ {A}, \varepsilon_ {A}) - v _ {A} (q _ {B}, \varepsilon_ {B});} \\ & {\rho_ {B A} ^ {0} = v _ {B} (q _ {B}, \varepsilon_ {0}) - v _ {A} (q _ {B}, \varepsilon_ {0}), \quad \rho_ {A B} ^ {0} = v _ {A} (q _ {A}, \varepsilon_ {0}) - v _ {B} (q _ {A}, \varepsilon_ {0}).} \end{array}
$$

Therefore, the objective functions of these two competing providers can be formulated as

$$
\max _ {\varepsilon_ {j}, p _ {j}} \pi_ {j} \left(q _ {j}, \varepsilon_ {j}, p _ {j}\right) \text {   s.t.   (20)   is   satisfied,   } j \in \{A, B \}.\tag{21}
$$

The generalized closed form solutions of the equilibrium price levels can be obtained by solving a quadratic equation but are cumbersome to express. In the following, we examine impact of competition on DRM and pricing strategies by considering the symmetric case in which the populations of these two customer groups and their disutility in using less preferable content are identical. By setting $\eta _ { A } = \eta _ { B } = \eta , v _ { A } ( q _ { A } , \varepsilon _ { A } ) =$ $v _ { B } ( q _ { B } , \varepsilon _ { B } ) , \rho _ { B A } = \rho _ { A B } = \rho _ { B A } ^ { 0 } = \rho _ { A B } ^ { 0 } = \rho _ { } $ , the symmetrical price levels can be obtained:

$$
p _ {c _ {j}} = \max \left(\frac {\left(v _ {0} v _ {\varepsilon} + 3 \rho v _ {0} - 2 \rho^ {2}\right) - \sqrt {\left(v _ {0} v _ {\varepsilon} + 3 \rho v _ {0} - 2 \rho^ {2}\right) ^ {2} + 4 v _ {0} \left(\rho^ {2} + \rho_ {\varepsilon} - \rho v _ {0} - 2 v _ {0} v _ {\varepsilon}\right) \rho}}{2 v _ {0}}, \frac {v _ {\varepsilon}}{2}\right),
$$

where

$$
v _ {0} = v _ {j} \left(q _ {j}, \varepsilon_ {0}\right), \quad v _ {\varepsilon} = v _ {j} \left(q _ {j}, \varepsilon_ {j}\right), \quad j \in \{A, B \}.\tag{22}
$$

DRM level ε and ε can be further derived by solving the following equations simultaneously:

$$
\begin{array}{c} \Gamma_ {c _ {j}} = \psi (\boldsymbol {\omega}, \varepsilon_ {j}) \bigg ((\mathsf {v} _ {\varepsilon} - 2 p _ {c _ {j}}) \frac {\partial p _ {c _ {j}}}{\partial \varepsilon_ {j}} + p _ {c _ {j}} \frac {\partial \mathsf {v} _ {\varepsilon}}{\partial \varepsilon_ {j}} \bigg) \\ - p _ {c _ {j}} (\mathsf {v} _ {\varepsilon} - p _ {c _ {j}}) \frac {\partial \psi (\boldsymbol {\omega} , \varepsilon_ {j})}{\partial \varepsilon_ {j}} = 0, j \in \{A, B \}. \end{array}\tag{23}
$$

## 6.1. Impact of heterogeneity

It can be easily veri<sup>fi</sup>ed that the price levels $p _ { c _ { i } } , j { \in } \{ A , B \}$ increase with the heterogeneity degree of the customers. As the pro<sup>fi</sup>t levels of content providers increase with the price, we know the pro<sup>fi</sup>t levels also increase with the heterogeneity degree of the customers. Notice that if the customers become homogeneous $( \mathrm { i } . \mathrm { e } . , \rho { = } 0 )$ on the content, then each competing provider will continuously undercut its opponent's price and <sup>fi</sup>nally sets its price to be zero $( p _ { c _ { A } } = p _ { c _ { B } } = 0 )$ and adopts DRM free policy $\left( \varepsilon _ { A } = \varepsilon _ { B } = \varepsilon _ { 0 } \right)$ . In this scenario, the platform provider gains all the value by setting the price to be $p _ { h } = v _ { j } ( q _ { j } , \varepsilon _ { 0 } )$ $j \in \{ A , B \}$

## 6.2. Impact of competition

We can further investigate the impact of competition on the adoption of DRM and pricing strategies by comparing the DRM and price levels in a competitive market with those in a monopolistic market. If these two types of content are offered by the same provider, the objective function of the monopolistic provider can be rewritten as

$$
\begin{array}{l} \max _ {\varepsilon_ {A}, p _ {A}, \varepsilon_ {B}, p _ {B}} \pi_ {A} (q _ {A}, \varepsilon_ {A}, p _ {A}) + \pi_ {B} (q _ {B}, \varepsilon_ {B}, p _ {B}) \\ \text { s.t. } v _ {A} (q _ {A}, \varepsilon_ {A}) - p _ {A} > v _ {A} (q _ {B}, \varepsilon_ {B}) - p _ {B} \text { and } v _ {B} (q _ {B}, \varepsilon_ {B}) - p _ {B} > v _ {B} (q _ {A}, \varepsilon_ {A}) - p _ {A}. \end{array}\tag{24}
$$

The constraints in Eq. (24) ensure the existence of segmented markets. In the symmetric case, both price levels are given by ${ p _ { c _ { A } } } ^ { m ^ { * } } \mathrm { = }$ $p _ { c _ { B } } ^ { m ^ { * } } = v _ { \varepsilon } / 2$ and DRM levels $\varepsilon _ { A } ^ { m ^ { * } }$ and $\varepsilon _ { B } ^ { m ^ { * } }$ are given by solving the following equations simultaneously.

$$
\Gamma_ {m _ {j}} = \psi (\omega , \varepsilon_ {j}) \cdot \frac {\partial v _ {\varepsilon}}{\partial \varepsilon_ {j}} - \frac {1}{2} \cdot v _ {\varepsilon} \cdot \frac {\partial \psi (\omega , \varepsilon_ {j})}{\partial \varepsilon_ {j}} = 0, j \in \{A, B \}.\tag{25}
$$

While the DRM and price levels in both market settings cannot be analytically compared because of the complexity in Eq. (23), our extensively numerical experiments (Figs. 9 and 10) show that the price (DRM) level in the competitive setting is always less (higher) than that in the monopolistic one. In addition, competing providers sell more contents but collect less revenue than a monopolistic provider does. As we can observe, the impact of content quality on the price and DRM strategies in both market structures are the same.

![](/api/attachments/HPU74JPZ/fulltext/images/07f45ad627fd65e1e85c4ec2d3a192e70884c2fa5fdd40d5371fc4735d51b5fe.jpg)  
Fig. 9. Impact of competition on price levels

![](/api/attachments/HPU74JPZ/fulltext/images/f34fcbe551c2cdd0dcb407cfe5e144a6b99c001267d730429b7a11a0ff1decb6.jpg)  
Fig. 10. Impact of competition on DRM levels.

## 7. Managerial implications

Our research provides useful insights for developing appropriate DRM and pricing strategies to enhance the pro<sup>fi</sup>t of a content provider. Speci<sup>fi</sup>cally, while implementing these strategies, the relation with platform, content quality, and network environment should be considered at the same time. To improve its pro<sup>fi</sup>tability, the content provider could choose to collaborate with other platform providers. However, DRM protection will be weakened to enhance the valuation of content and platform. As the revenue from selling content declines, the cooperation needs side-payment mechanisms (for example, revenue sharing agreement) in which the content provider received indirect revenue from the compensation from the platform providers. In practice, revenue sharing contract is popular in the content industry. For example, Apple's collaborative partners, such as EMI, Universal Music, Warner Music, and Sony BMG, usually charge them from US \$5 to \$8 royalty fees per customer to maintain the cooperative relationship.

From the standing point of platform providers, a platform is not limited to play speci<sup>fi</sup>c content (DRM protected or pirated), so their product strategy would be more agile than content providers. As for the marketing strategy, providing a bundle of both content and platform would make more pro<sup>fi</sup>t. The content and platform providers could focus on their core competence to provide better products. For the independent platform providers, the decision is whether to adopt strategic alignment with content providers. Nowadays there are many types of player manufacturers, such as stand-alone player manufacturers, software player manufacturers, cell phone manufacturers, and even GPS manufacturers. If the platform providers produce a software program rather than a hardware device, they could choose to make the platform universal or specialized. The universal one plays various contents regardless of DRM protected or pirated, whereas the specialized one can only be used on a speci<sup>fi</sup>c type or protection level of contents. The dedicated CODEC technology can be embedded in the software to help the integration of content and platform providers. Nevertheless, if there exist manufactures that do not share pro<sup>fi</sup>t with the content provider (or pirated software platform), the DRM level of the content will increase, but be still lower than that in a market with all independent providers because the content provider may not recover its pro<sup>fi</sup>t from contracted platform providers by implementing a DRM free policy. If there are two or more competing platform providers in the market, as we can expect, the platform price will drop, however, DRM protection and price levels of content will remain at the same levels.

Market structure also has signi<sup>fi</sup>cant impact on the development of content quality strategy. Our results indicate that pro<sup>fi</sup>t from selling content increases with content quality only when the quality is suf<sup>fi</sup>- ciently high. Otherwise, offering better content only results in higher loss. For an independent content provider, it is more pro<sup>fi</sup>table to provide content with extremely low or high quality. However, for a collaborated content provider, providing high quality content is always desirable since any pro<sup>fi</sup>t loss can be recovered from platform provider. Better content quality enhances the prices of content and platform. For an independent content provider, stronger DRM protection on the content with better quality is always bene<sup>fi</sup>cial. However, for a collaborated content provider, weaker DRM protection may be a better strategy if content quality is suf<sup>fi</sup>ciently low.

Decentralized network environment (such as P2P <sup>fi</sup>le sharing) has negative effect on content sale and corresponding revenue. No matter for independent or collaborated content providers, as the illegal distribution network become more uncontrollable, weakening DRM protection and improving the feasibility and price of the content is a better strategy. Thus, system collaboration becomes increasingly important as the emergence of advanced P2P distribution networks. Frequent reports reveal that DRM-free digital content has become more widespread in recent years. For example, major music companies, such as EMI and Universal Music Group, provide DRM free music to their collaborative partners.

## 8. Conclusion

In this paper, we analyze the pricing schemes and DRM protection policy with respect to different collaborative market structures. As the piracy is closely associated with the objects and the distribution channel, we also examine the impact of content quality and network effects on the development of strategies. Our analytical results are helpful to <sup>fi</sup>rms providing digital content products in so far as they may help them develop appropriate marketing and technology strategies.

Our results show that the adoption of DRM technology strengthens as the content and platform are offered by completely independent units. If both providers have a collaborative relationship, the providers tend to use less DRM protection on their content but tend to charge a higher price on it, which consequently results in a sale loss in the content segment. However, the collaborative system gains more from the increased revenue of the platform segment. Assuming that the effect of quality bene<sup>fi</sup>t and DRM infeasibility is separable, in a market with independent providers, the digital content provider will always adopt higher DRM protection levels on products to reduce the loss from piracy where higher quality content is provided. However, the effect of content quality on the DRM protection decision of a collaborative <sup>fi</sup>rm may be positive or negative, depending on the actual quality level. In both market structures, higher quality always results in higher price of the content and platform, therefore, the platform provider always bene<sup>fi</sup>ts as the content provider provides superior content quality. The impact of content quality on the sale amount of content is positive when content quality is suf<sup>fi</sup>ciently high but is negative if content quality is too low. The impact of content quality on revenue of content is similar in the two types of market structures. In addition, the level of network environment control also affects the variation of DRM protection level. When the effects of network environment and DRM protection level on diffusion of pirating are separable, both systems adopt weaker DRM protection as network environment becomes highly decentralized. However, when the two elements are non-separable, the DRM protection remains unchanged in independent system but weaker in collaborative systems. Finally, when there are two heterogeneous content offered in the market, the price level (DRM level) in a market with competing content providers is always less (higher) than that in a monopolistic market. In addition, competing providers sell more content but collect less revenue than a monopolistic provider does.

This study can be further extended in several directions. First, in this paper, the cost of developing different levels of DRM protection and content quality are not calculated in the decision process. In a short run, the costs of developing different level of DRM and content quality are treated as sunk costs. It will be interesting to consider a long run problem in which the costs of developing content quality and DRM technology should be considered in model. Second, currently, we consider the problem that the content provider offers the digital contents with only one DRM level. A potential avenue for future extension is to allow the content providers offered heterogeneous digital contents in which various DRM levels are leveraged. Third, the value transfer mechanism among collaborating players can be further examined. Bargaining mechanism design for the players in a coalition game, in the context of digital content market, is an interesting research avenue. Finally, as the results are mainly explored based on analytical models, further relevant empirical studies on the digital content with DRM are helpful for the validation of the analytical <sup>fi</sup>ndings.

## Appendix A

Proof of Lemma 1. The optimal price of a digital content p<sub>c</sub>⁎ can be derived by solving <sup>fi</sup>rst order condition ∂π ${ } _ { \circ } / \partial p _ { c } = 0 \ \mathrm { o r } \ p _ { c } ^ { * } = v ( q , \varepsilon ) / 2$ $\ A s \ p _ { h } ^ { * } { = } p _ { c } ^ { * } { \leq } v ( q , \varepsilon )$ and $p _ { h } ^ { * } \ge c _ { h } ,$ we have $p _ { h } ^ { * } { = } \operatorname* { m a x } ( v ( q , \varepsilon ^ { * } ) / 2 , c _ { h } )$ and $p _ { c } ^ { * } = \operatorname* { m i n } ( v ( q , \varepsilon ^ { * } ) / 2 , v ( q , \varepsilon ^ { * } ) - c _ { h } )$ . Plugging $p _ { c } ^ { * }$ into $\pi _ { c }$ and solving <sup>fi</sup>rst order condition ∂π $\partial \varepsilon = 0$ , the optimal level of DRM protection $\varepsilon _ { 1 } ^ { * }$ can be derived by solving ${ \cal { I } } _ { 1 } = 0$ , where $\boldsymbol { { \Gamma } } _ { 1 }$ is a reduced equation derived from $\partial \pi _ { c } / \partial \varepsilon$ □

Proof of Lemma 2. The proof is similar to Lemma 1. The only difference between Lemma 1 and Lemma 2 is the timing of setting optimal level of DRM protection. By backward induction approach, we solve $\pi _ { c + h } / \partial \varepsilon = 0$ at last. The optimal DRM protection level $\varepsilon _ { 2 } { ^ * }$ should satisfy the equation $\partial \pi _ { c + h } { \left/ { \partial \varepsilon } \right. } = 0 .$ . By proper substitution, the equation $\partial \pi _ { c + h } / \partial \varepsilon = 0$ can be determined by ${ \cal { I } } _ { 2 } = 0 \ $ , where $\boldsymbol { { \Gamma } } _ { 2 }$ is a reduced equation derived from $\partial \pi _ { c + h } / \partial \varepsilon$ □

Proof of Lemma 3. Because of $\partial ^ { 2 } \eta ^ { \ast } / \partial \varepsilon ^ { 2 } < 0$ , there exists a critical value $\hat { \boldsymbol { \varepsilon } } _ { \eta }$ such that $\partial \eta ^ { * } / \partial \varepsilon > 0$ for each $\varepsilon { < } \hat { \varepsilon } _ { \eta }$ and $\partial \eta ^ { * } / \partial \varepsilon < 0$ for each $\varepsilon { > } \hat { \varepsilon } _ { \eta } . \ \hat { \varepsilon } _ { \eta }$ is given by solving $\begin{array} { r } { { \cal I } _ { \eta } = 0 } \end{array}$ , where $\dot { I } _ { \eta }$ is a reduced equation derived from $\partial \eta ^ { * } / \partial \varepsilon$ □

Proof of Lemma 4. First, we investigate the case of $v ( q , \varepsilon ) - p _ { c } -$ $p _ { h } > 0$ . Because $\pi _ { c + h }$ can be enhanced by letting $p _ { h } = v ( q , \varepsilon ) - p _ { c }$ , we can reduce the search range of optimal solutions into $v ( q , \varepsilon ) - p _ { c } -$ $p _ { h } = 0 .$ . Therefore, this problem can be rewritten as follows:

max $\pi _ { c + h } = \eta _ { 0 } \Big \{ \overset { \wedge } { \delta } \cdot \mathbf { v } ( q , \varepsilon ) + \Big ( 1 - \overset { \wedge } { \delta } \Big ) p _ { h } - c _ { h } \Big \} \ : \mathsf { s . t . } \ : c _ { h } \le p _ { h } \le ( q , \varepsilon ) ,$ e;p<sub>h</sub> where $\stackrel { \wedge } { \delta } \in [ 0 , 1 ]$

It is obvious that $\pi _ { c + h }$ is the linear combination between max $( ( v ( q , \ \varepsilon ) - c _ { h } ) , \ 0 ) \eta _ { 0 }$ and max $( ( p _ { h } - c _ { h } ) , 0 ) \eta _ { 0 } ;$ thus, the maximum revenue is max $( ( v ( q , \varepsilon _ { 0 } ) - c _ { h } ) , 0 ) \eta _ { 0 }$ . We try to let $p _ { h } { = } \operatorname* { m a x } ( v ( q , \varepsilon _ { 0 } )$ c ) and then obtain $\pi _ { c + h } = \operatorname* { m a x } ( ( v ( q , \varepsilon _ { 0 } ) - c _ { h } ) , 0 ) \eta _ { 0 } .$ This completes the proof. □

Proof of Proposition 1. Proof is shown in Subsection 4.1.

Proof of Proposition 2. Case 1: Customer's valuation function is separable $( v ( q , \varepsilon ) = v _ { q } ( q ) + v _ { \varepsilon } ( \varepsilon ) )$ ). In an independent market structure, because the sign of $\partial \varepsilon _ { i } { ^ { * } } / \partial q$ is the same as that of $\partial { \cal {Gamma } } _ { i } / \partial q$ where $i = 1 , 2$ and $\begin{array} { r } { \frac { \partial \boldsymbol { r } _ { 1 } } { \partial \boldsymbol { q } } = \mathbf { \bar { \Pi } } - \frac { 1 } { 2 } \frac { \partial \mathbf { v } ( \boldsymbol { q } , \varepsilon ) } { \partial \boldsymbol { q } } \frac { \partial \psi ( \boldsymbol { \dot { \omega , \varepsilon } } ) } { \partial \varepsilon } > } \end{array}$ 0 holds, we know ∂ε⁎ $/ \partial q > 0$ . On the other hand, in a collaborative market structure, the sign of $\partial { \cal { T } } _ { 2 }$ $( \boldsymbol { q } , \varepsilon ) / \partial \boldsymbol { q }$ cannot be determined. However, $\partial { \cal { T } } _ { 2 } ( q , \varepsilon ) / \partial q$ is positive when q is suf<sup>fi</sup>ciently high but is negative when q is suf<sup>fi</sup>ciently low. This result can be proven as follows. First, because $\begin{array} { r } { \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial q } = \frac { \partial \mathbf { v } ( q , \varepsilon _ { 0 } ) } { \partial q } , \frac { \partial T _ { 2 } } { \partial q } } \end{array}$ can be rewritten as $\begin{array} { r } { \frac { \partial \varGamma _ { 2 } } { \partial q } = K \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial q } , } \end{array}$ , where K is given by ${ \cal T } _ { 1 } + 2 \psi ^ { 2 }$ $\begin{array} { r } { ( \omega , \varepsilon ) \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial \varepsilon } - \frac { 1 } { 2 } \mathbf { v } ( q , \varepsilon ) \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \varepsilon } . } \end{array}$ . Thus, we know that $\begin{array} { r } { \frac { \partial { \cal T } _ { 2 } } { \partial q } > 0 } \end{array}$ if $K > 0$ . Expanding $K ,$ we derive $\begin{array} { r } { \Big \{ \Big [ \psi ( \omega , \varepsilon ) + 2 \psi ^ { 2 } ( \omega , \varepsilon ) \Big ] \frac { \partial { \bf v } ( q , \varepsilon ) } { \partial \varepsilon } \Big \} ^ { * } - \Big \{ { \bf v } ( q , \varepsilon ) \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \varepsilon } \Big \} } \end{array}$ Its <sup>fi</sup>rst (negative) term is irrelevant to q, whereas its second (positive) term increases with q. Therefore, there exists q ̅ such that $\begin{array} { r } { \dot { \frac { \partial \varGamma _ { 2 } } { \partial a } } > \dot { 0 } } \end{array}$ for each $q \geq { \overline { { q } } } .$ Second, because of $\begin{array} { r } { \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial q } = \frac { \partial \mathbf { v } ( \mathbf { \dot { q } } , \varepsilon _ { 0 } ) } { \partial q } , } \end{array}$ $v ( 0 , \ \varepsilon ) { \leq } \tilde { 0 }$ , and $\begin{array} { r } { \frac { \partial \varGamma _ { 2 } } { \partial q } = \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial q } \varGamma _ { 1 } + \frac { \partial \varGamma _ { 1 } } { \partial q } \mathbf { v } ( q , \varepsilon ) + 2 \psi ^ { 2 } ( \omega , \varepsilon ) \cdot \left\{ \frac { \partial \mathbf { v } ( q , \varepsilon _ { 0 } ) } { \partial q } \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial \varepsilon } \right\} } \end{array}$ , we only investigate the sign o $\begin{array} { r } { \hat { [ \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial q } F , } } \end{array}$ where F is given by $\begin{array} { r } { r _ { 1 } + 2 \psi ^ { 2 } ( \pmb { \omega } , \varepsilon ) \cdot \frac { \partial \pmb { \mathrm { v } } ( \pmb { q } , \varepsilon ) } { \partial \varepsilon } . } \end{array}$ <sup>ð Þ -</sup>Its <sup>fi</sup>rst (positive) term decreases as q decreases, whereas its second (negative) term is irrelevant to q. Therefore, there exists q ̅such that $\scriptstyle { \frac { \partial I _ { 2 } } { \partial q } } < 0$ for each $q \leq { \overline { { q } } } .$

Case 2: Customer's valuation function is non-separable $( v ( q , \varepsilon ) =$ $v _ { q } ( q ) \cdot v _ { \varepsilon } ( \varepsilon ) )$

$\begin{array} { r } { \dot { \mathrm { B e c a u s e ~ o f } } \varGamma _ { 1 } ( q , \varepsilon _ { 1 } ^ { * } ) = \mathbf { v } _ { q } ( q ) \left[ \psi ( \omega , \varepsilon ) \cdot \frac { \partial \mathfrak { v } _ { \varepsilon } ( \varepsilon ) } { \partial \varepsilon } - \frac 1 2 \cdot \mathfrak { v } _ { \varepsilon } ( \varepsilon ) \cdot \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \varepsilon } \right] \mid _ { \varepsilon = \varepsilon _ { 1 } ^ { * } } = } \end{array}$ <sup>ð Þ ð Þ - - ð Þ- j</sup>0, we know that the optimal level of DRM protection is irrelevant to content quality. That is, the DRM protection remains the same when the independent content provider changes content quality. Furthermore, because of ${ \Gamma } _ { 2 } \left( { \boldsymbol { q } } , \varepsilon _ { 2 } ^ { * } \right) = { \mathbf { v } } _ { \boldsymbol { q } } ( \boldsymbol { q } ) \left| 2 { \cdot } { \mathbf { v } } _ { \varepsilon } ( \varepsilon ) { \Gamma } _ { 1 } ( \varepsilon ) + 2 \boldsymbol { \psi } ^ { 2 } ( \omega , \varepsilon ) { \cdot } { \mathbf { v } } ( \boldsymbol { q } , \varepsilon _ { 0 } ) \right.$ $\begin{array} { r } { \frac { \partial \mathbf { v } _ { \varepsilon } ( \varepsilon ) } { \partial \varepsilon } ] | _ { \varepsilon = \varepsilon _ { \gamma } ^ { * } } = 0 , } \end{array}$ , we know that $\Gamma _ { 2 } { < } 0$ <sup>Þ - ð Þ ð Þ ð Þ- ð Þ-</sup>when content quality increases. It <sup>j</sup>means that DRM protection level becomes weaker when collaborating content provider offers contents with higher quality. □

Proof of Proposition 3. Case 1: the probability function that one pirates the digital content is separable $( \mathrm { i . e . , ~ } \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) + \psi _ { \varepsilon } ( \varepsilon ) )$ Notice that $\begin{array} { r } { \frac { \partial { \cal T } _ { 1 } } { \partial \omega } = \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \omega } \cdot \frac { \partial { \bf v } ( q , \varepsilon ) } { \partial \varepsilon } - \frac { 1 } { 2 } \cdot { \bf v } ( q , \varepsilon ) \cdot \frac { \partial ^ { 2 } \psi ( \omega , \varepsilon ) } { \partial \varepsilon \partial \omega } } \end{array}$ . Hence, $\scriptstyle { \frac { \partial { \cal { T } } _ { 1 } } { \partial \omega } } < 0$ holds. Moreover, we have $\begin{array} { r } { \frac { \partial T _ { 2 } } { \partial \omega } = 2 ( q , \varepsilon ) \cdot \frac { \partial T _ { 1 } } { \partial \omega } + 4 \psi ( \omega , \varepsilon ) \cdot \frac { \partial \psi ( \omega , \varepsilon ) } { \partial \omega } \cdot \mathbf { v } ( q , \varepsilon _ { 0 } ) \cdot \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial \varepsilon } } \end{array}$ It is obvious that $\scriptstyle { \frac { \partial { \cal { F } } _ { 2 } } { \partial \omega } } < 0$

Case 2: the probability function that one pirates the digital content is non-separable $( \mathrm { i . e . , } \psi ( \omega , \varepsilon ) = \psi _ { \omega } ( \omega ) \cdot \psi _ { \varepsilon } ( \varepsilon ) )$

Because of $\begin{array} { r } { T _ { 1 } ( \varepsilon _ { 1 } ^ { * } ) = \psi _ { \omega } ( \omega ) \cdot \left| \psi _ { \varepsilon } ( \varepsilon ) \cdot \frac { \partial \mathbf { v } ( q , \varepsilon ) } { \partial \varepsilon } - \frac { 1 } { 2 } \cdot \mathbf { v } ( q , \varepsilon ) \cdot \frac { \partial \psi _ { \varepsilon } ( \varepsilon ) } { \partial \varepsilon } \right| | _ { \varepsilon = \varepsilon _ { 1 } ^ { * } } = } \end{array}$ <sup>ð Þ- ð Þ - - ð Þ - j 1</sup>0, we know that the optimal level of DRM protection is irrelevant to network environment. That is, the DRM protection remains the same when network environment changes. Furthermore, because $\mathfrak { o f } \ : T _ { 2 } ( \varepsilon _ { 2 } ^ { * } ) = 0$ a n d $\begin{array} { r } { \int _ { \circ } T _ { 2 } ( \varepsilon ) = \psi _ { \omega } ( \omega ) \big ( 2 \mathsf { v } ( q , \varepsilon ) \Big \{ \breve { \psi } _ { \varepsilon } ( \varepsilon ) \cdot \frac { \partial \mathsf { v } ( q , \varepsilon ) } { \partial \varepsilon } - \frac { \mathsf { v } ( q , \varepsilon ) } { 2 } \cdot \frac { \partial \psi _ { \varepsilon } ( \varepsilon ) } { \partial \varepsilon } \Big \} + \overline { { 2 \psi _ { \omega } ( \omega ) } } } \end{array}$ $\begin{array} { r } { ( \psi _ { \varepsilon } ( \varepsilon ) ) ^ { 2 } { \cdot } ( q , \varepsilon _ { 0 } ) { \cdot } ~ \frac { \partial \bar { \bf v } ( q , \varepsilon ) } { \partial \varepsilon } ) } \end{array}$ <sup>Þ ð Þ ð Þ -</sup>  <sup>- ð Þ -</sup>, we know that Γ (ε ⁎)b 0when ω increases. That is, the DRM policy becomes weaker in the collaborative market structure. □

## References

[1] A. Arnab, A. Hutchison, Digital rights management: an overview of current challenges and solutions, Information Security South Africa (ISSA), 2004.

[2] A. Arnab, A. Hutchison, Fairer usage contracts for DRM, ACM Workshop on Digital Rights Management (2005) 1–7.

[3] G. Arora, M. Hanneghan, M. Merabti, P2P commercial digital content exchange, Electronic Commerce Research and Applications 4 (2005) 250–263.

[4] S.H. Bae, J.P. Choi, A model of piracy, Information Economics and Policy 18 (3) (2006) 303–320.

[5] E. Becker, Digital rights management, Technological, economic, legal and political aspects, Springer, 2003.

[6] P. Belle<sup>fl</sup>amme, P.M. Picard. Competition over piratable goods. CORE Discussion Paper No 2004/55.

[7] O. Bomsel, A.G. Geffroy. Economic analysis of digital rights management systems (DRMS). Web Page: www.cerna.ensmp.fr/Documents/OB-AGG-EtudeDRM.pdf. Accessed at: Feb 14.2009.

[8] S.C. Cheung, H. Curreem, Rights protection for digital contents redistribution over the Internet, Computer Software and Applications Conference (2002) 105–110.

[9] S.Y. Choi, D.O. Stahl, A.B. Whinston, The economics of electronic commerce, Macmillan Technical Publishing, New York, 1997.

[10] K.R. Conner, R.P. Rumelt, Software piracy: an analysis of protection strategies, Management Science 37 (2) (1991) 125–139.

[11] L.E.K. Consulting. The cost of movie piracy. Web Page: http://www.mpaa.org leksummaryMPA%20revised.pdf. Accessed at: Feb 14,2009.

[12] C. Craig, R. Graham, Rights management in the digital world, Computer Law & Security Report 19 (5) (2003) 356–362.

[13] B. Dirk, T. Eisenbach, J. Feigenbaum, S. Shenker, Flexibility as an instrument in digital right management, 4th Workshop on the Economics of Information Security, 2005.

[14] J.H. Farr. What is fairplay? Web Page: http://www.applelinks.com/articles/2003/ 04/20030430002640.shtml. Accessed at: Sep. 26, 2007.

[15] J. Feigenbaum, M.J. Freedman, T. Sander, A. Shostack, Privacy engineering for digital rights management systems, Lecture Notes in Computer Science (2002) 76–105.

[16] E.W. Felten, A skeptical view of DRM and fair use, Communications of the ACM 46 (4) (2003) 56–59.

[17] M. Fetscherin, Economics of online music and consumer behavior, International Conference on Electronic Commerce (2006) 599–604.

[18] A. Gayer, O. Shy, Copyright protection and hardware taxation, Information Economics and Policy 15 (4) (2003) 467–483

[19] A. Gayer, O. Shy, Internet and peer-to-peer distributions in markets for digital products, Economics Letters 81 (2) (2003) 197–203.

[20] H.J. Holm, The computer generation's willingness to pay for originals when pirates are present: A cv study, School of Economics and Management, Lund University Lund, 2000.

[21] H.J. Holm, Can economic theory explain piracy behavior, Topics in Economic Analysis & Policy 3 (1) (2003) 1082.

[22] W. Hui, B. Yoo, K.Y. Tam, Economics of shareware: how do uncertainty and piracy affect shareware quality and brand premium? Decision Support Systems 44 (3) (2008) 580–594.

[23] R. Iannella, Open digital rights management, World Wide Web Consortium (W3C) DRM Workshop, 2001.

[24] IFPI. The recording industry in numbers. Web Page: http://87.84.226.196/mro/ publications/purchase\_publication.asp. Accessed at: Feb 14, 2009.

[25] J. Jaisingh, Impact of piracy on innovation at software <sup>fi</sup>rms and implications for piracy policy, Decision Support Systems 46 (3) (2008) 605–752.

[26] F. Jay, R. Mayer, IEEE standard glossary of software engineering terminology, IEEE Standard (1990) 610.612–1990.

[27] A. Jiménez, S. RíOs-Insua, A. Mateos, A decision support system for multiattribute utility evaluation based on imprecise assignments, Decision Support Systems 36 (1) (2003) 65–79.

[28] M. Khouja, M. Hadzikadic, H.K. Rajagopalan, L.S. Tsay, Application of complex adaptive systems to pricing of reproducible information goods, Decision Support Systems 44 (3) (2008) 725–739.

[29] S.P. King, R. Lampe, Network externalities and the myth of pro<sup>fi</sup>table piracy: Intellectual Property Research Institute of Australia, 2002.

[30] S.S.K. Kwan, J. Jaisingh, K.Y. Tam, Risk of using pirated software and its impact on software protection strategies, Decision Support Systems 45 (3) (2008) 504–516.

[31] S.H. Kwok, Digital rights management for the online music business, ACM SIGecom Exchanges 3 (3) (2002) 17–24.

[32] S.H. Kwok, S.C. Cheung, K.C. Wong, K.F. Tsang, S.M. Lui, K.Y. Tam, Integration of digital rights management into the internet open trading protocol, Decision Support Systems 34 (4) (2003) 413–425.

[33] S.H. Kwok, C.C. Yang, K.Y. Tam, J.S.W. Wong, SDMI-based rights management systems, Decision Support Systems 38 (1) (2004) 33–46.

[34] W.M. Landes, R.A. Posner, An economic analysis of copyright law, Journal of Legal Studies 18 (1989) 325

[35] J. Lee, S.O. Hwang, S.W. Jeong, K.S. Yoon, C.S. Park, J.C. Ryou, A DRM framework for distributing digital contents through the internet, ETRI Journal 25 (6) (2003) 423–436.

[36] Q. Liu, R. Safavi-Naini, N.P. Sheppard, Digital rights management for content distribution, Conferences in Research and Practice in Information Technology, 2003, pp. 49–58.

[37] I.E. Novos, M. Waldman, The effects of increased copyright protection: an analytic approach, The Journal of Political Economy 92 (2) (1984) 236.

[38] A. Oberweis, V. Pankratius, W. Stucky, Product lines for digital information products, Information Systems 32 (6) (2007) 909–939.

[39] Y. Park, S. Scotchmer, Digital rights management and the pricing of digital products, NBER Working Paper, 2005.

[40] M. Peitz, A strategic approach to software protection: comment, Journal of Economics & Management Strategy 13 (2) (2004) 371–374.

[41] M. Peitz, P. Waelbroeck, Piracy of digital products: a critical review of the theoretical literature, Information Economics and Policy 18 (4) (2006) 449–476.

[42] P. Petrick. Why DRM should be cause for concern: An economic and legal analysis of the effect of digital technology on the music industry. Berkman Center for Internet & Society at Harvard Law School, Research Publication n. 09/2004.

[43] G.P. Premkumar, Alternate distribution strategies for digital music, Communications of the ACM 46 (9) (2003) 89–95.

[44] A. Russ, Digital rights management overview, Security Essentials (2001) 1–11.

[45] E.M. Snir, The record industry in an era of <sup>fi</sup>le sharing: lessons from vertica differentiation, International Conference on Information Systems, 2003.

[46] L.S. Sobel, DRM as an enabler of business models: ISPs as digital retailers, Berkeley Technology Law Journal 18 (2003) 667.

[47] A. Sundararajan, Managing digital piracy: pricing, protection and welfare, Working Paper, 2003, pp. 1–39.

[48] L.N. Takeyama, The welfare implications of unauthorized reproduction of intellectual property in the presence of demand network externalities, Journal of Industrial Economics 42 (1994) 155.

[49] C.L. Tze, S. Poddar, Network externality and software piracy, Working paper, Singapore University, 2000, pp. 1–17.

[50] H.R. Varian, Markets for information goods, Monetary Policy in a World of Knowledge-Based Growth, Quality Change, and Uncertain Measurement, Palgrave Macmillan, , July 2001.

[51] H.R. Varian, Universal access to information, Communications of the ACM 48 (10) (2005) 65–66.

[52] D.L. Venkatesh, S. Srinivasan, S. Kumbhakar, Software piracy: estimation of lost sales and the impact on software diffusion, Journal of Marketing 59 (1995) 29–37.

[53] S. Wu, P. Chen, G. Anandalingam, Fighting information goods piracy with versioning, International Conference on Information Systems (2003) 617–621.

[54] K. Yoon, The optimal level of copyright protection, Information Economics and Policy 14 (3) (2002) 327–348.

![](/api/attachments/HPU74JPZ/fulltext/images/0863d714a8a0e3ffc343e39f1ef502596d6136e4ce85b24129959c1084ba3bf3.jpg)  
Yung-Ming Li is an Assistant Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include Peer-to-Peer networks. Internet economics. and business intelligence. His research has appeared in IEEE/ ACM Transactions on Networking, Electronic Commerce Research and Applications, International Conference on Information Systems (ICIS), and Workshop on Information Technology and Systems (WITS).

![](/api/attachments/HPU74JPZ/fulltext/images/4f07bcbd4e680f239e495151f615e1a5935bf4d262427433cde6ce3e161ee90e.jpg)  
Chia-Hao Lin received his M.S. degree from Institute of Information Management, National Chiao Tung University, Taiwan and B.S. degree in Management Information Systems from the National Chengchi University, Taiwan. His research interests focus on electronic commerce and digital content management.
