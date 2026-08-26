---
otero_id: 5210
otero_key: "DK5EP8HT"
title: "Pricing digital content distribution over heterogeneous channels"
authors: "Yung-Ming Li"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.027"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Pricing digital content distribution over heterogeneous channels

Yung-Ming Li

Institute of Information Management, National Chiao Tung University, Hsinchu, 300, Taiwan

## a r t i c l e i n f o

Article history: Received 21 June 2008 Received in revised form 23 April 2010 Accepted 17 August 2010 Available online 22 September 2010

Keywords: Content distribution Peer-to-peer Competition and collaboration Network pricing IT investment

## a b s t r a c t

The paper considers the pricing and allocation issues of distributing digital contents via Web and P2P channels. Utilizing a game theoretic model, the allocation equilibrium with respect to various business goals is examined. We <sup>fi</sup>nd that the P2P channel is always under-utilized in an organization, and present an incentive scheme to achieve an ef<sup>fi</sup>cient channel con<sup>fi</sup>guration. Under a market structure with sequential moves, both channels set higher price and collect higher pro<sup>fi</sup>t. Particularly, the second mover enjoys higher price and market share. A provider with integrated channels will charge a higher price on the Web channel and the Web channel becomes under-utilized.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

With the arising phenomena of the Internet, people have signi<sup>fi</sup>cantly changed their communication behaviors, purchasing and entertaining habits, and information goods exchange activities, over the Web. Today, the Internet provides a convenient and low-cost channel by which to distribute a wide variety of information goods. Recently, AT&T intended to attract some of Akamai and Limelight's customers by moving further into the content delivery space with new partners, service offerings, and a \$70 million commitment to build out its content distribution channel [4]. Amazon also launched a content distribution service, CloudFront, in 2008 [19]. It gives developers and businesses an easy way to distribute contents to end users with high data transfer speed and low latency. Content delivery networks (CDNs), which duplicate contents over several servers to deal with the <sup>fl</sup>ash crowds, are used as distribution channels to push content closer to the end users [42]. The preliminary data shows that the worldwide CDN revenue will be a little more than \$400 million in 2008, and the worldwide video CDN revenue is expected to grow to more than \$1.4 billion by 2012 [60].

The dominant content distribution platforms are categorized as website-based and peer-to-peer (P2P) <sup>fi</sup>le sharing systems [64]. These systems serve the same role of distributing contents to users. Table 1 lists popularly commercialized content distribution channels. It is common for people to download contents through the above two important types of content distribution channels. For example, website-based content distribution channels, such as Akamai and LimeLight, have been serving the market for years. Besides, the iTune store has gained a pro<sup>fi</sup>table market share by providing online music downloading, and it is predicted to have one-quarter of worldwide music market by 2012 [2]. On the other hand, although P2P is not traditional content distribution technology, it is increasingly used to deliver content to end users. P2P <sup>fi</sup>le sharing networks, such as BitTorrent and KaZaA, are very popular and attract a great amount of usage [29]. For example, Warner Brothers sells and distributes movies and TV programs through BitTorrent [28]. According to <sup>fi</sup>le sharing research <sup>fi</sup>rm BigChampagne, despite the lawsuit against developers and consumers, P2P activity continued to rise throughout 2005, hitting record levels in December [5]. Besides, channel providers, Grid Networks and Raw<sup>fl</sup>ow, utilize P2P technologies to meet the service requirements of digital content distribution. There are also a few content distribution providers combing both website and P2P channels. For example, CDNetworks and Internap Network Services provide integrated distribution channels to serve the market. The evolution pattern of content distribution industry reveals that these two types of distribution platform coexist in the market and compete for the users. Some of the existing providers in the industry even moved between website and P2P distribution models. For instance, Joost was an Internet TV service created by the founders of Skype and KaZaA. During 2007–2008, it used P2P TV technology to distribute content. However, in December 2008, Joost announced that its service was moving to a website-only model and the P2P application will stop working [61].

From the viewpoint of channel providers, a centralized website channel provides several advantages such as easy central organizing and managing to content providers. However, when an abundant number of people simultaneously crowd on line, it inevitably leads to website overload and causes an Internet traf<sup>fi</sup>c jam. According to Zona Research, the amount of time taken for web pages to load is one of the most critical factors in determining the success of a site and the satisfaction of its users [8]. Many researchers have developed new technologies to solve this critical issue [23,65]. Contrary to a website channel, a P2P channel provides a more scalable distribution infrastructure via the pooling of bandwidth, storage, and computing resource of the peer nodes. However, P2P networks are often considered to be security threats for organizations, companies or plain users [68]. While there are several advantages, P2P networks are being seriously challenged over their insuf<sup>fi</sup>cient security design [17,69]. Therefore, users who are choosing a preferable channel to download the contents should take into account the abovementioned characteristics of technological differentiation and the corresponding bene<sup>fi</sup>ts and drawbacks of these two channels. As integrated channels would have the maximum optimal pro<sup>fi</sup>ts [40], the design of multichannel marketing strategies is gaining the attention [37].

Table 1  
Commercial content distribution channels.

<table><tr><td>Providers</td><td>Service/product</td><td>Distribution platform</td></tr><tr><td>Akamai</td><td>Electronic software delivery</td><td>Website</td></tr><tr><td>Limelight networks</td><td>Limelight DELIVER</td><td></td></tr><tr><td>Apple</td><td>ITune/iStore</td><td></td></tr><tr><td>Amazon</td><td>CloudFront</td><td></td></tr><tr><td>Grid Networks</td><td>GridCast</td><td>P2P</td></tr><tr><td>BitTorrent</td><td>BitTorrent DNA</td><td></td></tr><tr><td>RawFlow</td><td>UGB Platform</td><td></td></tr><tr><td>CDNetworks</td><td>Delivery Service</td><td>Integrated</td></tr><tr><td>Internap network services</td><td>CDN Service</td><td>(Website + P2P)</td></tr></table>

Extensive works have been conducted on the technological design and improvement of content distribution based on these two platforms [48–50,57]. However, little attention has been given to the business strategy development of content distribution channels (retailers) utilizing these heterogeneous distribution platforms and the discussions of integrated channels are relatively rare in the past literatures. In particular, how market interactions and technological parameters affect the business strategies of these two channels have not been systematically analyzed yet. Considering various market structures, this paper concentrates on the economic analysis of the coexisting content distribution channels and examines corresponding pricing and allocation strategies as well as technology investment in relation to the objectives of an organization: ef<sup>fi</sup>ciency and pro<sup>fi</sup>tability.

Utilizing a game theoretic model, we <sup>fi</sup>rst examine the selfselected equilibrium of the channel allocation and propose a pricing scheme to enforce an ef<sup>fi</sup>cient allocation con<sup>fi</sup>guration within an organization. The pricing scheme shows that the Web channel should be charged more, in order to recover the ef<sup>fi</sup>ciency loss due to the over-allocation phenomenon. We further investigate pricing strategies of these two distribution channels in a competitive market. We <sup>fi</sup>nd that the equilibrium pricing decision and allocation are quite sensitive to the decision sequence of the channel providers. A business environment with sequential decision structure will elevate the prices and pro<sup>fi</sup>ts of both channels. The leader channel loses market share because of charging a higher price, while the follower channel has the second mover advantage to both raise its price and enjoy higher demand. When both channels are integrated, the monopoly sets the price of a Web channel higher than a P2P channel's price and a Web channel becomes under-utilized.

This paper makes several signi<sup>fi</sup>cant contributions to supplement the research literatures of content distribution. First, it appropriately presents a model linking both main technological and economic characteristics of the Web and P2P content distribution channels. Second, it offers a new theoretical lens for studying the economic issues (incentive, pricing, and investment) about digital content distribution over heterogeneous channels. Third, it develops a new practical framework for the analysis of content distribution business models for the organizations with various business goals (pro<sup>fi</sup>tability and ef<sup>fi</sup>ciency). Fourth, we analyze the impact of market dimension and interactions, such as the order of the entrance to the market on the development of business strategy and resulting pro<sup>fi</sup>tability. And Fifth, it lays the groundwork for developing a management tool based on key system parameters (characteristics of network environment, such as market size, upload capacity, and security technology) to support strategic decision-making.

The remaining sections are organized as follows. Section 2 lists previous literatures related to digital content distribution. Section 3 introduces the model setting. In Section 4, we examine the channel allocation and pricing scheme in an organization. We analyze the competition and integration of channels in the market in Section 5. In Section 6, we discuss the impact of market size and channel interactions, as well as IT investment under various business situations. Section 7 concludes our <sup>fi</sup>ndings, presents managerial implication, and discusses future research directions.

## 2. Related literature

## 2.1. Digital content distribution

Digital content distribution on the Internet uses many different service architectures, ranging from centralized client/server platforms to fully distributed P2P systems. It is still in an early stage of development and its future evolution remains an open issue, and pricing content distribution channels is a relatively new and unexplored research area. Commercial distribution websites of digital content tend to provide high data quality and improve transfer security for their clients in order to increase their pro<sup>fi</sup>t and popularity [55], and they generally charge customers according to their traf<sup>fi</sup>c. Web content distribution mechanisms typically require vast investments of infrastructure [33]. In contrast, the P2P paradigm appears as an attractive alternative mechanism for large scale content distribution. With the superior scalable content distribution characteristic, P2P networks have become increasingly popular distribution channels, and the issues of supplier risks and business opportunities arising from the P2P service model have been analyzed [38]. P2P networks possess some nonfunctional characteristics, such as provisions for security, fairness, increased scalability, resource management, and organization capabilities [3]. Several researches have focused on comparing technological and managerial characteristics of both client/server and P2P channels and investigating the dramatic differentiation of content distribution [26,39].

## 2.2. Economic issues in content distribution

The economic aspects of the digital content distribution channel are closely related to the study of content distribution model, network pricing, incentive mechanism, as well as content and channel management. A few studies discuss the technological and economic characteristics of emerging P2P and traditional client/server distribution networks. For example, several researches have plunged into analyzing content distribution subjects related to the Web [7,52], and congestion is one of the key quality factors for developing the pricing strategy of Web-based content distribution services [43,46,47]. Priority pricing is also proposed for delay sensitive users as an online adaptive resource scheduling mechanism for managing real-time information services within organizations [35]. In addition, the issue of budgetary balance was also examined and it was suggested that netvalue maximization entails a budget de<sup>fi</sup>cit for the service facility [18]. Pricing schemes and incentive mechanisms are highly ranked in the realization of commercial P2P content distribution [62]. While Napster developed a working service model, it failed to adequately address two important economic constraints: pricing and participation incentives. This prevented their business model from being economically viable [29]. Free-riding phenomenon is an inherent problem due to the decentralized structure of P2P <sup>fi</sup>le sharing networks. Incentive mechanism design for inducing appropriate <sup>fi</sup>le sharing is a promising research topic and a number of works have been conducted on this issue [24,41]. Regarding digital channel management in the industry level, economic characteristics like pricing and QoS are included into the discussion of content distribution [27], and researches have been presented to discuss the economic related issues [39,66]. While the QoS can be interpreted in a different context, in general, one dimension of differentiation is evaluated.

The content providers face the question whether to adopt a centralized or a decentralized solution. The centralized approach is usually mentioned as a client/server system [10], while the decentralized system is implemented over a P2P network [56]. In this research, we model the quality differentiation between two heterogeneous digital channels (Web and P2P channels) from two salient perspectives— download delay and download security.

## 2.3. Multiple channel competition

There has been a number of literatures focused on the business strategy of multiple channels, including channel con<sup>fl</sup>ict and coordination [11], service competition [20,34], and channel distribution [9,36]. Since the availability of multiple channels has signi<sup>fi</sup>cant implications for the performance of consumer markets, distribution channels have been viewed as a strategic tool and channel design has been recognized as a key successful factor to competition [2,6]. Under this circumstance, many suppliers face a decision of whether to add a new channel to their existing channels. For example, whether to adopt a dual-channel with a retailer and an outlet store [16]. Channel competition also commonly occurs in a competing market. For example, Choi [14] compares Stackelberg and vertical Nash game settings in a duopolistic market. McGuire and Staelin [45] explain why a supplier uses an intermediary retailer. On the other hand, channel coordination can yield more pro<sup>fi</sup>ts to retailers, thus, channel con<sup>fl</sup>ict can be reduced [12]. Guardiola et al. [25] analyze supply chains by means of cooperative games.

While many channel competition issues in various business contexts have been studied, the competitive and cooperative interactions between content distribution channels utilizing heterogeneous technological platforms have not been systematically analyzed yet. Previous literature either studies the ef<sup>fi</sup>cient allocation or pricing problem within the same type of distribution channels. This research aims to show the channel competitive interaction between the centralized client–server structure and the decentralized P2P networks. The main objective of this paper differs by attempting to compare the allocation, pricing dynamics, and technology investment in website and P2P distribution channels under various market structures and organization missions.

## 3. The model

We consider a digital supply chain in which consumers (or employees in an organization) can download the digital content (or information good) from two heterogeneous distribution channels: a dedicated website (Web channel) or a peer-to-peer network (P2Pchannel). The parameters used in the model are listed in Table $2 .$ Denote N as the potential market size; $\eta _ { 1 }$ and $\eta _ { 2 }$ are the total number of the Web channel customers and the P2P-channel customers respectively. The number of customers outside both channels is denoted as $\eta _ { 3 } ;$ that is, $\begin{array} { r } { N = \eta _ { 1 } + \eta _ { 2 } + \eta _ { 3 } . } \end{array}$ The capacity (bandwidth) of the Web channel is $b _ { 1 }$ bytes per second and average bandwidth of a typical peer node in the P2P networks is $b _ { 2 }$ bytes per second. In practice, we assume that the Web channel has higher capacity than peer nodes participating in the P2P-channel $( b _ { 1 } > b _ { 2 } )$ . For the sake of analytical convenience, the size of a typical content <sup>fi</sup>le is assumed to be f bytes.

Table 2  
Model parameters.

<table><tr><td>Parameters</td><td>Description</td></tr><tr><td> $N$ </td><td>Total number of potential users (potential market size)</td></tr><tr><td> $\eta_1; \eta_2$ </td><td>Demand of the web channel; Demand of the P2P-channel</td></tr><tr><td> $f$ </td><td>Size of a typical content file (bytes)</td></tr><tr><td> $b_1; b_2$ </td><td>Bandwidth capacity of the web channel; average bandwidth capacity of peer nodes (bytes/sec)</td></tr><tr><td> $\eta_1w_1; w_2$ </td><td>Average download delay of the web channel; average download delay of the P2P channel ( $w_1 = f/b_1$  and  $w_2 = f/b_2$ )</td></tr><tr><td> $\delta$ </td><td>P2P security level</td></tr><tr><td> $\theta_i$ </td><td>Individual sensitivity on the sharing cost (security risk) ( $\theta_i \sim U[0,1]$ )</td></tr><tr><td> $\beta_i$ </td><td>Individual valuation of the content.  $\beta_i = \beta_0 + \theta_i\beta$ , where  $\beta_0$  is basic value and  $\beta$  is individual perceived value</td></tr><tr><td> $p_1; p_2$ </td><td>Price of download service via the web channel; price of download service via the P2P-channel</td></tr><tr><td> $K_1(b_1); K_2(\delta)$ </td><td>Investment of website with capacity  $b_1$ ; investment of P2P technology with security level $\delta$ </td></tr><tr><td> $\mathcal{R}_1; \mathcal{R}_2$ </td><td>Revenue of the web channel; revenue of the P2P-channel</td></tr><tr><td> $\pi_1; \pi_2$ </td><td>Profit of the web channel; profit of the P2P-channel</td></tr></table>

Notation of superscript. e: free-access channels; w: ef<sup>fi</sup>cient channels; c: competing channels (simultaneous moves); $c _ { 1 2 } \colon$ competing channels (web channel as the <sup>fi</sup>rst mover); c : competing channels (P2P-channel as the <sup>fi</sup>rst mover); and m: collaborating channels.

## 3.1. Customer utility functions

In the model, we assume that a customer downloads a <sup>fi</sup>le and the digital contents downloaded from either channel are homogeneous. Multiple <sup>fi</sup>les can be viewed as a larger single <sup>fi</sup>le with the same size as the summation of the sizes of these smaller <sup>fi</sup>les. The waiting time of content download is assumed to be linear on the content size and also a linear function of the number of <sup>fi</sup>les with identical sizes [15]. However, customers face different opportunity costs (delay and security risk), depending on the channel chosen. A typical customer i faces heterogeneous sharing cost (security risk) $\theta _ { i } \delta$ if he/she downloads <sup>fi</sup>les through the P2P-channel, where the variable $\theta _ { i }$ stands for the individual sensitivity on the sharing cost, and is uniformly distributed with an interval [0,1]. A customer with higher value of $\theta _ { i }$ is more sensitive to this disutility. Parameter δ re<sup>fl</sup>ects the service quality level (i.e. security level) of a P2P channel. A higher value of δ indicates that a higher security risk may occur in <sup>fi</sup>le sharing activity. Notice that while there should be security risk from using the Web channel, the risk is signi<sup>fi</sup>cantly lower than that in a P2P channel because of centralized management and the identi<sup>fi</sup>able business reputation. For analytical convenience, we normalize the security cost of the Web channel to be zero and focus on the impact of P2P security risk. Inclusion of security cost of the Web channel only affects the quantitative degree of the results, however, it has no signi<sup>fi</sup>cant impact on the qualitative results.

Let $\beta _ { i }$ denote customer i's valuation on the content. Empirical evidences reveal that if a consumer has a higher valuation on the service, he/she tends to be more concerned on service quality [13,70]. Therefore, we formulate the valuation of a downloaded content for a typical customer i as $\beta _ { i } = \beta _ { 0 } + \beta \theta _ { i } ,$ , where $\beta _ { 0 } { \ge } 0$ is basic value attached to each customer and $\beta \theta _ { i } { \ge } 0$ is individual perceived values, which are heterogeneous on the customers. $p _ { 1 }$ and $p _ { 2 }$ signify the price of content downloaded from the Web channel and the P2P-channel, respectively. Notice that the price could be zero or negative in an organization context. Negative price implies that the organization encourage users to use some speci<sup>fi</sup>c type of content distribution channel by providing a reward mechanism. The utility of each customer with $\theta _ { i }$ is de<sup>fi</sup>ned by:

$U _ { i } = \left\{ \begin{array} { l l } { \beta _ { i } - \eta _ { 1 } w _ { 1 } - p _ { 1 } } \\ { \beta _ { i } - w _ { 2 } - \theta _ { i } \delta - p _ { 2 } } \end{array} \right.$ if download through the Web channel if download through the P2P channel <sup>;</sup>

ð<sup>1</sup>Þ

where $w _ { 1 } = \gamma f / b _ { 1 }$ and $w _ { 2 } = \gamma f / b _ { 2 }$ are the cost of waiting time in the Web channel and the P2P-channel, respectively, and parameter γ is the value of time. The delay cost function $\eta _ { 1 } w _ { 1 }$ considers the congestion externality faced by the customers of client/server based Web channel in which delay linearly increases with the number of the users as all the users are served by a dedicated server at the same time [30]. Notice that the forms of convex delay function on the demand pose no conceptual dif<sup>fi</sup>culty, but make the analysis less tractable because of the complexity in expressing the closed-form results. They affect the quantitative level (e.g. less Web channel users) but have no signi<sup>fi</sup>cant impact on the qualitative results.<sup>1</sup> Delay cost function $w _ { 2 }$ describes the scalability of the P2P-channel on the performance of download delay as effective supply of bandwidth capacity is scalable in relation to the demand of the download request. Since sharing cost (security risk) is an important factor in deciding whether to choose a P2P network as the distribution channel, we also assume that $\delta > w _ { 2 }$ to re<sup>fl</sup>ect that the security concern is signi<sup>fi</sup>cantly important relative to the <sup>fi</sup>le transfer performance between two peer nodes.

## 3.2. Channel demand functions

According to the content valuation function β , the Web channel is more preferable to the users who have a higher valuation on the content. Let $\widehat { \theta } _ { 1 }$ denote a customer type who is indifferent between buying (and downloading) from a P2P channel and not buying. Similarly, let $\widehat { \theta } _ { 2 }$ denote a customer type who is indifferent between purchasing from a Web channel and a P2P channel. The utility function implies that:

$$
\hat {\theta} _ {1} = \frac {w _ {2} + p _ {2} - \beta_ {0}}{\beta - \delta} \text { and } \hat {\theta} _ {2} = \frac {\eta_ {1} w _ {1} - w _ {2} + p _ {1} - p _ {2}}{\delta}.\tag{2}
$$

Therefore, all customer types indexed by $\theta _ { i } { \in } \Big [ \operatorname* { m a x } \Big ( \hat { \theta } _ { 1 } , 0 \Big ) , \hat { \theta } _ { 2 } \Big ]$ download from the P2P channel and all customers indexed by $\theta _ { i } { \in } \big \lceil \hat { \theta } _ { 2 } , 1 \big \rceil$ download from the website channel. Furthermore, the value of $\widehat { \theta } _ { 2 }$ reveals that the website channel can increase its market share by increasing its bandwidth capacity $b _ { 1 }$ since it reduces the expected delay, whereas the P2P channel can increase its market share by reducing δ to improve the sharing security. As the bandwidth capacity of end users increase (such as adopting broadband connection), the market share of the P2P channel will also increase. Consequently, according to the conditions:

$$
\begin{array}{l} \eta_ {1} = \big (1 - \hat {\theta} _ {2} \big) N,   \eta_ {2} = \big (\hat {\theta} _ {2} - \max \big (\hat {\theta} _ {1}, 0 \big) \big) N,   \eta_ {3} = \max \big (\hat {\theta} _ {1}, 0 \big) N, \\ \text { and }    \eta_ {1} + \eta_ {2} + \eta_ {3} = N, \end{array}
$$

the demand functions are written as:

$$
\begin{array}{l} \eta_ {1} = \frac {(w _ {2} + \delta - p _ {1} + p _ {2}) N}{N w _ {1} + \delta},   \eta_ {2} = N - \eta_ {1} - \eta_ {3}, \\ \eta_ {3} = \max \Big (\frac {(w _ {2} + p _ {2} - \beta_ {0}) N}{\beta - \delta}, 0 \Big) \end{array}\tag{3}
$$

## 4. Channels in the organization

With the development of digital device technology, almost all kinds of information can be stored in digital format. In addition, Internet and Web technology signi<sup>fi</sup>cantly diminish the cost of distributing the contents. We consider an organization in which both website and P2P channels are installed for software or digital content distribution. For example, while still maintaining the software download website, Microsoft also starts testing Avalanche peer-topeer content distribution platform to distribute beta software [51].

We <sup>fi</sup>rst investigate the equilibrium channel allocation without any price (or reward) scheme. Then, we compare them with the ef<sup>fi</sup>ciency (socially optimal) results. Finally, we discuss the incentive mechanism that an organization could adopt to enforce an ef<sup>fi</sup>cient channel allocation.

## 4.1. Self-selection equilibrium

In the absence of any pricing schemes on the channel services $( p _ { 1 } = p _ { 2 } = 0 )$ , the users self-select an appropriate channel in order to maximize its individual utility. From Eq. (3), the resulting equilibrium demand for each channel is given by:

$$
\eta_ {1} ^ {e} = \frac {N (w _ {2} + \delta)}{N w _ {1} + \delta},   \eta_ {2} ^ {e} = \left\{ \begin{array}{l l} \Big (\frac {N w _ {1} (\beta - \delta - w _ {2} + \beta_ {0}) - (\beta w _ {2} - \delta \beta_ {0})}{(\beta - \delta) (N w _ {1} + \delta)} \Big) N & \text {if} \beta_ {0} \leq w _ {2} \\ \frac {N (N w _ {1} - w _ {2})}{N w _ {1} + \delta} & \text {if} \beta_ {0} \geq w _ {2} \end{array} \right..\tag{4}
$$

The market share of each channel is obtained as:

$$
\begin{array}{l} s _ {1} ^ {e} = \frac {\eta_ {1} ^ {e}}{N} = \frac {w _ {2} + \delta}{N w _ {1} + \delta}, \\ s _ {2} ^ {e} = \frac {\eta_ {2} ^ {e}}{N} = \left\{ \begin{array}{l l} \frac {N w _ {1} (\beta - \delta - w _ {2} + \beta_ {0}) - (\beta w _ {2} - \delta \beta_ {0})}{(\beta - \delta) (N w _ {1} + \delta)} & \text {if} \beta_ {0} \leq w _ {2} \\ \frac {N w _ {1} - w _ {2}}{N w _ {1} + \delta} & \text {if} \beta_ {0} \geq w _ {2} \end{array} \right.. \end{array}\tag{5}
$$

We have the following proposition.<sup>2</sup>

## Proposition 1. Self-selection equilibrium

1. P2P-channel is only sustained if potential market size is sufficiently large. Formally, $\eta _ { 2 } ^ { e } > 0$ when $N > N ^ { e p }$

$$
\text { where } N ^ {e p} = \left\{ \begin{array}{l l} \frac {(\beta w _ {2} - \delta \beta_ {0})}{w _ {1} (\beta - \delta - w _ {2} + \beta_ {0})} & \text { if } \beta_ {0} \leq w _ {2} \\ b _ {1} / b _ {2} & \text { if } \beta_ {0} \geq w _ {2} \end{array} \right..
$$

2. The market share of the P2P- (Web-) channel increases (decreases) as potential market size increase; whereas the market sizes of both P2P and Web channels increase with potential market size.

3. The P2P- (Web-) channel has larger market size when N is larger (smaller) than a critical population size

$$
\hat {N} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (w _ {2} + \delta) + \beta w _ {2} - \delta \beta_ {0}}{w _ {1} (\beta - \delta - w _ {2} + \beta_ {0})} & \text { if } \beta_ {0} \leq w _ {2} \\ \frac {2 w _ {2} + \delta}{w _ {1}} & \text { if } \beta_ {0} \geq w _ {2} \end{array} \right..
$$

Proposition 1 reveals that the Web channel will dominate the P2Pchannel when the number of users is small and congestion is not a sensitive problem. However, as more users utilize the Web channel, congestion becomes more serious and some of its users are switching to the P2P-channel. As a result, the Web channel becomes less attractive and the P2P-channel enjoys its advantage of faster <sup>fi</sup>le transfer, as the total population is increasing. Notice that, although the P2P-channel becomes more attractive, some new users with strong adversity to the security risk choose the Web channel; therefore, the number of the Web channel users continuously increases as the user population grows. Since the increasing rate of new users is higher in relation to the P2Pchannel, the market size of the P2P-channel will exceed that of the Web channel when the total population is suf<sup>fi</sup>ciently high.

Fig. 1 shows the evolution of allocation between two heterogeneous channels as the total population grows. Initially, when the population size is quite small, the Web channel may serve all of the users. As the population size increases, it emerges that some users begin to use the P2P-channel and P2P <sup>fi</sup>le sharing activities. Because of the congestion effect, the P2P-channel becomes more favorable than the Web channel as the population increases. Finally, the P2P-channel dominates the Web channel with a greater market size.

For real cases, Internap initially provides the website-based content delivery service to its customers. However, as the number of users increases, the delivery performance becomes not as good as expected. In 2007, it served its customers with a new P2P-based delivery channel for a better service quality [71]. Besides, CDNetworks adopted a similar strategy to better serve its customers. In the beginning, the contents were located at dedicated websites, and the users downloaded what they liked directly from the websites. However, as the download congestion came with the growth of users, the performance became intolerable and the P2P-channel was adopted to overcome this problem.

## 4.2. Efficient channel allocation

In this subsection, we compare the self-selection equilibrium of channel allocation with the ef<sup>fi</sup>cient channel allocation. The ef<sup>fi</sup>ciency of channel allocation is measured by its social welfare, which is the sum of individual utilities less the overall investment of the Web channel's capacity and P2P security technology. In the following, we <sup>fi</sup>rst investigate the con<sup>fi</sup>guration of an ef<sup>fi</sup>cient (or socially optimal) channel allocation, which is the objective of a value-maximizing organization. Denote $K _ { 1 } ( b _ { 1 } )$ as the cost function of Web channel capacity, and $K _ { 2 } ( \delta )$ as the cost function of P2P security technology; $K _ { 1 }$ $\left( b _ { 1 } \right)$ is a linear function on bandwidth capacity $b _ { 1 } ,$ and $K _ { 2 } ( \delta )$ is a decreasingly convex function on security quality level δ. The overall value of the organization is de<sup>fi</sup>ned $\mathsf { a s } ^ { 3 } \colon$

$$
W = \sum_ {i = 1} ^ {N} U _ {i} - K _ {1} (b _ {1}) - K _ {2} (\delta).\tag{6}
$$

The ef<sup>fi</sup>cient choices of channel allocation can be found by solving the optimization problem:

$$
\begin{array}{l} \max _ {\eta_ {1}, \eta_ {2}} W = \eta_ {1} \Big (E \big (\beta_ {j} \big) - \eta_ {1} w _ {1} \Big) + \eta_ {2} (E (\beta_ {i}) - w _ {2} - E (\theta_ {i} \delta)) - K _ {1} (b _ {1}) - K _ {2} (\delta) \\ \text {s.t.} \eta_ {1} + \eta_ {2} + \eta_ {3} = N, \theta_ {i} \in U \Big [ \hat {\theta} _ {1}, \hat {\theta} _ {2} \Big ], \theta_ {j} \in U \Big [ \hat {\theta} _ {2}, 1 \Big ] \end{array}\tag{7}
$$

The resulting ef<sup>fi</sup>cient allocation for each channel is written as:

$$
\eta_ {1} ^ {w} = \frac {N (w _ {2} + \delta)}{2 N w _ {1} + \delta}, \eta_ {2} ^ {w} = \left\{ \begin{array}{l l} N \Big (\frac {2 N w _ {1} - w _ {2}}{2 N w _ {1} + \delta} - \frac {w _ {2} - \beta_ {0}}{\beta - \delta} \Big) & \text { if } \beta_ {0} \leq w _ {2} \\ \frac {N (2 N w _ {1} - w _ {2})}{2 N w _ {1} + \delta} & \text { if } \beta_ {0} \geq w _ {2} \end{array} \right..\tag{8}
$$

After comparing Eqs. (4) and (8), we present the following observations:

## Proposition 2. Efficient channel allocation

1. Free-access policy results in over-usage (under-usage) of the Web-(P2P-) channel, in comparison with the efficient channel allocation configuration.

![](/api/attachments/DK5EP8HT/fulltext/images/31f5e4345d2de3c42f489da0f2addfbbd5c3bffa8cc12347578d87f007e74648.jpg)  
Fig. 1. Evolution of channel allocation.

2. Closing the P2P-channel is efficient if the potential market size is too small. Formally, $\eta _ { 2 } ^ { w } { = } 0$ when $N { \le } N ^ { w p }$ , where

$$
N ^ {w p} = \left\{ \begin{array}{l l} \frac {(\beta w _ {2} - \delta \beta_ {0})}{2 w _ {1} (\beta - \delta - w _ {2} + \beta_ {0})} & \text { if } \beta_ {0} \leq w _ {2} \\ \frac {b _ {1}}{2 b _ {2}}, & \text { if } \beta_ {0} \geq w _ {2} \end{array} \right..
$$

Proposition 2 indicates that without any intervention from the organization, self-selection will result in an inef<sup>fi</sup>cient channel allocation, even though people recognize the congestion externality. The phenomenon of over-using congestible resources has been previously identi<sup>fi</sup>ed in the context of a single server based channel. Our results also show that a P2P channel could play a role in improving organization ef<sup>fi</sup>ciency only if the users of an organization are of suf<sup>fi</sup>ciently large numbers, even though some users have better utility in using a P2P-channel. Fig. 2 shows that equilibrium market share (in percentage) of a Web channel decreases as the population size increases; however, the level of self-selection is still higher than the ef<sup>fi</sup>ciency level.

In practice, Internap improves its content distribution ef<sup>fi</sup>ciency by a “best-of-both-worlds” combination [31]. When content download delay is below an acceptable threshold, peers become unavailable or drop off unexpectedly and all the contents are seamlessly downloaded from the Web channel. This architecture enables the users to gain potential bene<sup>fi</sup>ts from P2P distribution while maintaining an ef<sup>fi</sup>cient distribution performance.

![](/api/attachments/DK5EP8HT/fulltext/images/9cc36e8025dd0427a1bdbfa824de60d537e95a9edc1e2de55f5c49675f2634f5.jpg)  
Fig. 2. Ef<sup>fi</sup>cient Web channel allocation.

## 4.3. Efficient pricing scheme

In order to recover the ef<sup>fi</sup>ciency loss due to over (under)-usage of the Web- (P2P-) channel, an organization can develop appropriate discouraging (charging the Web channel users) or encouraging (rewarding the P2P-channel users) mechanism to enforce an ef<sup>fi</sup>cient channel allocation. The ef<sup>fi</sup>cient (socially optimal) pricing scheme should satisfy the following condition:

$$
\frac {N (w _ {2} + \delta)}{2 N w _ {1} + \delta} = \frac {N (\delta + w _ {2} - p _ {1} ^ {w} + p _ {2} ^ {w})}{N w _ {1} + \delta},\tag{9}
$$

or

$$
\triangle p ^ {w} = p _ {1} ^ {w} - p _ {2} ^ {w} = \frac {N w _ {1} (w _ {2} + \delta)}{2 N w _ {1} + \delta}.\tag{10}
$$

There are many ways to develop a pricing (rewarding) scheme when all users in an organization use the channels $( \beta _ { 0 } \ge w _ { 2 } )$ . In practice, for example, while keeping the P2P channel free-access, an organization may charge the Web channel users a $\mathsf { p r i c e } : p _ { 1 } ^ { w } = \Delta p ^ { w }$ Alternatively, an organization could adopt an encouraging mechanism which rewards P2P users with $p _ { 2 } ^ { w } { = } - \bar { \Delta } p ^ { w }$ but let the Web channel downloads free of charge. Or, an organization may charge a Web channel a higher price than it would a P2P channel. However, $p _ { 2 } ^ { w }$ must be zero when the organization are partially served $\left( \beta _ { 0 } \leq w _ { 2 } \right)$ , which can be observed from Eq. (8).

It is interesting to analyze the impact of system parameters on the resultant pricing scheme. Assume y is a system parameter and $S =$ $\{ N , \delta , b _ { 1 } , b _ { 2 } , f \}$ is the set of system parameters. Observing Eq. (10), we can easily verify that $\partial \Delta p ^ { w } / \partial y { > } 0$ , for $y \in \{ N , \delta , f \}$ and $\partial \bar { \Delta p ^ { w } } / \partial y { < } 0$ , for $y \in \{ b _ { 1 } , b _ { 2 } \}$

## Proposition 3. Efficient pricing scheme

1. An organization shall charge users a higher price for using the Web channel. Specifically, content distribution in an organization with two heterogeneous channels is efficient if their price levels are satisfactory (Eq. (10)).

2. Price disperse level of the Web- and P2P-channels increases with potential market size and file size, but decreases with P2P security quality and the capacities of both Web server and P2P users.

The intuition of Proposition 3 can be explained as follows. As the population size grows, the Web channel faces more serious congestion from new users. In order to inhibit the ef<sup>fi</sup>ciency loss from congestion, a high price strategy is essential to discourage the Web channel usage. As higher sharing cost in a P2P channel forces more users of the P2P-channel to switch to the Web channel, an organization will charge the users of the Web channel a higher price to discourage its usage. Similarly, when the performance of P2P <sup>fi</sup>le transfer is improved (larger peer capacity), fewer users will use the Web channel and the price will decline. Similarly, higher capacity for the Web channel can alleviate congestion externality and the price will naturally go down. Finally, while larger <sup>fi</sup>le size (for example, multimedia game or movie) increases download delay in both channels, the effect is more signi<sup>fi</sup>cant in a Web channel because of congestion externality. Consequently, the price rises.

## 5. Channels in the market

In this section, we examine the pricing schemes of content distribution channels operated by pro<sup>fi</sup>t-seeking <sup>fi</sup>rms. For example, iTune provides a website-based channel to sell licensed digital music, while Snocap uses a system of sound <sup>fi</sup>ngerprinting which allows songs traded over a P2P network. In contrast, CoopNet integrates both website and peer-to-peer channels for content distribution [53,54]. We <sup>fi</sup>rst investigate pricing competition between these two channels owned or operated by independent <sup>fi</sup>rms, and then we analyze the pricing strategy and pro<sup>fi</sup>tability when both channels are integrated. Notice that in the research, the channels in the market are actually the retailers utilizing differen technological distribution platforms. Therefore, the channels should pay their content sales to the content owners. While there exist variou types of business contract for content owners to collect revenue from the retailing channels, revenue sharing is the most popularly used one in the digital content industry [1]. For example, Apple entered into a revenue sharing agreement with <sup>fi</sup>ve of the major music labels: BMG, EMI Sony, Universal, and Warner. The impact of revenue sharing mechanism on the pricing schemes of distribution channels is discussed in Appendix A.

## 5.1. Pricing in competing channels

The business environment for the Web- and P2P- channels is largely determined by the timing to enter the market for these two players. We consider three cases of competition structure in non-cooperative pricing dynamics. In the <sup>fi</sup>rst case, both channels participate simultaneously in a Bertrand pricing competition game. The next two cases consider the business situation wherein one of them has the leadership of pricing decision and these two channels participate in a Stackelberg (leader–follower) pricing competition game [58,63].

## 5.1.1. Simultaneous pricing competition

Let us <sup>fi</sup>rst examine a simultaneous price competition between the Web channel and the P2P-channel. Denote π<sup>c</sup> $\left( \pi _ { 2 } ^ { c } \right)$ and p<sup>c</sup> $( p _ { 2 } ^ { c } )$ ) as the pro<sup>fi</sup>t function and the price of the Web- (P2P-) channel respectively. We have the following pro<sup>fi</sup>t functions:

$$
\pi_ {1} ^ {c} = p _ {1} ^ {c} \eta_ {1} ^ {c} - K _ {1} (b _ {1}) = p _ {1} ^ {c} \cdot \frac {N (\delta + w _ {2} - p _ {1} ^ {c} + p _ {2} ^ {c})}{N w _ {1} + \delta} - K _ {1} (b _ {1}),\tag{11}
$$

$$
\pi_ {2} ^ {c} = p _ {2} ^ {c} \eta_ {2} ^ {c} - K _ {2} (\delta),\tag{12}
$$

where η<sub>2</sub><sup>c</sup> is given by Eq. (3).

Firstly, for a fully served market in which all customers' content values are very high $( \widehat { \theta } _ { 1 } { < } 0 )$ , we can get the price response function of the Web- (P2P-) channel to the P2P- (Web-) channel's pricing decision by solving the <sup>fi</sup>rst order conditions, ∂π<sup>c</sup> $/ \partial p _ { 1 } ^ { c } = 0$ , and $\partial \pi _ { 2 } ^ { c } / \partial p _ { 2 } ^ { c } = 0 ;$

$$
p _ {1} ^ {c} = \frac {w _ {2} + \delta + p _ {2} ^ {c}}{2},   p _ {2} ^ {c} = \frac {N w _ {1} - w _ {2} + p _ {1} ^ {c}}{2}.\tag{13}
$$

Solving both equations simultaneously, we have the Nash equilibrium:

$$
p _ {1} ^ {c} = \frac {N w _ {1} + w _ {2} + 2 \delta}{3}, p _ {2} ^ {c} = \frac {2 N w _ {1} - w _ {2} + \delta}{3}.\tag{14}
$$

Next, for a partially served market $( { \hat { \theta } } _ { 1 } > 0 )$ , we can get another price response function of the Web- (P2P-) channel to the P2P- (Web-) channel's pricing decision:

$$
p _ {1} ^ {c} = \frac {\delta + w _ {2} + p _ {2} ^ {c}}{2},   p _ {2} ^ {c} = \frac {(\beta - \delta) (N w _ {1} - w _ {2} + p _ {1} ^ {c}) - (\delta + N w _ {1}) (w _ {2} - \beta_ {0})}{2 (\beta + N w _ {1})}.\tag{15}
$$

Solving both equations simultaneously, we have the Nash equilibrium:

$$
p _ {1} ^ {c} = \frac {(\beta - \delta) (N w _ {1} + w _ {2} + 2 \delta) + (2 \delta + w _ {2} + \beta_ {0}) (N w _ {1} + \delta)}{3 (\beta - \delta) + 4 (N w _ {1} + \delta)},\tag{16}
$$

$$
p _ {2} ^ {c} = \frac {(\beta - \delta) (2 N w _ {1} - w _ {2} + \delta) - 2 (w _ {2} - \beta_ {0}) (N w _ {1} + \delta)}{3 (\beta - \delta) + 4 (N w _ {1} + \delta)}.\tag{17}
$$

For a fully served market in which customers' content values are not very high $( { \underline { { \beta } } } _ { 0 } ^ { c } { < } \beta _ { 0 } { < } \overline { { \beta } } _ { 0 } ^ { c } )$ , we will have other different price response functions. $\overline { { \beta } } _ { 0 } ^ { c }$ and $\underline { { \beta } } _ { 0 } ^ { c }$ are the values of $\beta _ { 0 }$ derived from the equation $\hat { \theta } _ { 1 } = 0$ by using p<sup>c</sup> given by Eqs. (14) and (17), respectively. In this case, solving $\hat { \theta } _ { 1 } = 0$ yields P2P-channel's equilibrium price. Notice that the price response function of the Web channel to the P2P-channel's pricing decision in Eq. (13) is the same as that in Eq. (15). As a result, the Web channel's equilibrium price can be obtained from $p _ { 1 } ^ { c } = \frac { \delta + \hat { w _ { 2 } } + p _ { 2 } ^ { \check { c } } } { 2 }$ directly.

Finally, the equilibrium price levels under different scenarios can be expressed as follows.

$$
p _ {1} ^ {c} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (N w _ {1} + w _ {2} + 2 \delta) + (2 \delta + w _ {2} + \beta_ {0}) (\delta + N w _ {1})}{3 (\beta - \delta) + 4 (\delta + N w _ {1})} & \text {if} \beta_ {0} <   \underline {{\beta}} _ {0} ^ {c} \\ \frac {\delta + \beta_ {0}}{2} & \text {if} \underline {{\beta}} _ {0} ^ {c} \leq \beta_ {0} \leq \overline {{\beta}} _ {0} ^ {c} \\ \frac {N w _ {1} + w _ {2} + 2 \delta}{3} & \text {if} \beta_ {0} > \overline {{\beta}} _ {0} ^ {c} \end{array} \right.\tag{18}
$$

$$
p _ {2} ^ {c} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (2 N w _ {1} - w _ {2} + \delta) - 2 (w _ {2} - \beta_ {0}) (\delta + N w _ {1})}{3 (\beta - \delta) + 4 (\delta + N w _ {1})} & \text { if } \beta <   \underline {{\beta}} _ {0} ^ {c} \\ \beta_ {0} - w _ {2} & \text { if } \underline {{\beta}} _ {0} ^ {c} \leq \beta \leq \overline {{\beta}} _ {0} ^ {c} \\ \frac {2 N w _ {1} - w _ {2} + \delta}{3} & \text { if } \beta > \overline {{\beta}} _ {0} ^ {c}, \end{array} \right.\tag{19}
$$

$$
\text { where } \underline {{\beta}} _ {0} ^ {c} = \frac {(\beta - \delta) (2 N w _ {1} + 2 w _ {2} + \delta) + 2 w _ {2} (\delta + N w _ {1})}{3 (\beta - \delta) + 2 (\delta + N w _ {1})} \text { and } \overline {{\beta}} _ {0} ^ {c} = \frac {2 (N w _ {1} + w _ {2}) + \delta}{3}.
$$

5.1.2. Sequential pricing competition: Web channel as the leader

Suppose the Web channel makes the pricing decision before the P2P-channel does. Firstly, for the case $\widehat { \theta } _ { 1 } { < } 0$ , the P2P-channel makes a pricing decision after observing the decision of the Web channel. Thus, the best response function of the P2P-channel to the Web channel is the same as that developed from the case of simultaneous decision, i.e. $p _ { 2 } ^ { c _ { 1 2 } } = \left( N w _ { 1 } - w _ { 2 } + p _ { 1 } ^ { c _ { 1 2 } } \right) / 2 .$ . Utilizing a backward induction approach, the pro<sup>fi</sup>t function of the Web channel is obtained by plugging in the P2P-channel's response function $p _ { 1 } ^ { c _ { 1 2 } }$ <sup>2</sup>, and rewritten as:

$$
\pi_ {1} ^ {c _ {1 2}} - K _ {1} (b _ {1}) = p _ {1} ^ {c _ {1 2}} \cdot \frac {N (N w _ {1} + w _ {2} + 2 \delta - p _ {1} ^ {c _ {1 2}})}{2 (N w _ {1} + \delta)} - K _ {1} (b _ {1}).\tag{20}
$$

The <sup>fi</sup>rst order condition for the Web channel directly yields the subgame perfect Nash equilibrium results:

$$
p _ {1} ^ {c _ {1 2}} = \frac {N w _ {1} + w _ {2} + 2 \delta}{2}, p _ {2} ^ {c _ {1 2}} = \frac {3 N w _ {1} - w _ {2} + 2 \delta}{4}.\tag{21}
$$

Next, for the case $\widehat { \theta } _ { 1 } = 0$ , we can obtain two threshold values ${ \overline { { \beta } } } _ { 0 } ^ { c _ { 1 2 } }$ and $\underline { { \beta } } _ { 0 } ^ { c _ { 1 2 } }$ , where $\beta _ { 0 } ^ { c _ { 1 2 } } < \beta _ { 0 } < \overline { { \beta } } _ { 0 } ^ { c _ { 1 2 } }$ . As the P2P-channel makes the pricing decision after the Web channel does and whether the market is fully served by both channels completely depends on $p _ { 2 } ^ { c _ { 1 2 } }$ , we know when $\beta _ { 0 }$ is small $( \beta _ { 0 } ^ { c _ { 1 2 } } \leq \beta _ { 0 } \leq \beta _ { 0 } ^ { * } )$ , the Web channel has to tactfully set its price based on $p _ { 2 } ^ { c _ { 1 2 } } = \left( N w _ { 1 } - w _ { 2 } + p _ { 1 } ^ { c _ { 1 2 } } \right) / 2$ to ensure that the P2P-channel sets $p _ { 2 } ^ { c _ { 1 2 } } = \beta _ { 0 } - w _ { 2 } .$ . However, when $\beta _ { 0 }$ becomes larger $\displaystyle \big ( \beta _ { 0 } ^ { * } \leq \beta _ { 0 } < \overline { { \beta } } _ { 0 } ^ { c _ { 1 2 } } \big )$ , the Web channel can set its price directly according to its best response function to the P2P-channel $p _ { 1 } ^ { c } { = } \left( \delta { + } w _ { 2 } { + } p _ { 2 } ^ { c } \right) / 2$

Finally, by adopting the same approach in a simultaneous pricing competition to analyze the case $\hat { \theta } _ { 1 } > 0 ,$ , we have the equilibrium price levels given as follows.

$$
p _ {1} ^ {c _ {1 2}} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (N w _ {1} + w _ {2} + 2 \delta) + (2 \delta + w _ {2} + \beta_ {0}) (\delta + N w _ {1})}{3 (\beta - \delta) + 4 (\delta + N w _ {1})} & \text { if } \beta_ {0} \leq \underline {{\beta}} _ {0} ^ {c _ {1 2}} \\ 2 \beta_ {0} - w _ {2} - N w _ {1} & \text { if } \underline {{\beta}} _ {0} ^ {c _ {1 2}} \leq \beta_ {0} \leq \beta_ {0} ^ {*} \\ \frac {\delta + \beta_ {0}}{2} & \text { if } \beta_ {0} ^ {*} \leq \beta_ {0} <   \overline {{\beta}} _ {0} ^ {c _ {1 2}} \\ \frac {N w _ {1} + w _ {2} + 2 \delta}{2} & \text { if } \beta_ {0} > \overline {{\beta}} _ {0} ^ {c _ {1 2}} \end{array} \right.\tag{22}
$$

$$
\begin{array}{l} p _ {2} ^ {c _ {1 2}} = \left\{ \begin{array}{l l} A (\beta_ {0}) & \text {if} \beta_ {0} \leq \underline {{\beta}} _ {0} ^ {c _ {1 2}} \\ \beta_ {0} - w _ {2} & \text {if} \underline {{\beta}} _ {0} ^ {c _ {1 2}} \leq \beta_ {0} <   \overline {{\beta}} _ {0} ^ {c _ {1 2}} \\ \frac {3 N w _ {1} - w _ {2} + 2 \delta}{4} & \text {if} \beta_ {0} > \overline {{\beta}} _ {0} ^ {c _ {1 2}} \end{array} \right., \\ \text {where} \overline {{\beta}} _ {0} ^ {c _ {1 2}} = \frac {3 (N w _ {1} + w _ {2}) + 2 \delta}{4}, \beta_ {0} ^ {*} = \frac {\delta + 2 w _ {2} + 2 N w _ {1}}{3}, \text {and} \\ A (\beta_ {0}) = \frac {(\beta - \delta) ^ {2} (3 N w _ {1} - w _ {2} + 2 \delta) + (\beta - \delta) (\delta + N w _ {1}) (4 N w _ {1} - 5 w _ {2} + 2 \delta + 3 \beta_ {0}) - (4 w _ {2} - 4 \beta_ {0}) (\delta + N w _ {1}) ^ {2}}{(2 (\beta - \delta) + 2 (\delta + N w _ {1})) (2 (\beta - \delta) + 4 (\delta + N w _ {1}))}. \end{array}\tag{23}
$$

The value of $\underline { { \beta } } _ { 0 } ^ { c _ { 1 2 } }$ can be derived by solving the following equation:

$$
w _ {2} + A (\beta_ {0}) - \beta_ {0} = 0.\tag{24}
$$

5.1.3. Sequential pricing competition: P2P channel as the leader

We examine the case in which the P2P channel is the <sup>fi</sup>rst mover to decide the pricing strategy. Similarly, for the case $\widehat { \theta } _ { 1 } { < } 0 ,$ , we have the pro<sup>fi</sup>t function of the P2P-channel expressed as:

$$
\pi_ {2} ^ {c _ {2 1}} = p _ {2} ^ {c _ {2 1}} \cdot \frac {N (2 N w _ {1} - w _ {2} + \delta - p _ {2} ^ {c _ {2 1}})}{2 (N w _ {1} + \delta)} - K _ {2} (\delta),\tag{25}
$$

and we get the following equilibrium results:

$$
p _ {1} ^ {c _ {2 1}} = \frac {2 N w _ {1} + w _ {2} + 3 \delta}{4}, p _ {2} ^ {c _ {2 1}} = \frac {2 N w _ {1} - w _ {2} + \delta}{2};\tag{26}
$$

By adopting the same approach to analyze the cases, $\hat { \theta } _ { 1 } = 0$ and $\hat { \theta } _ { 1 } > 0$ , the equilibrium price levels are given as follows.

$$
p _ {1} ^ {c _ {2 1}} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (2 N w _ {1} + w _ {2} + 3 \delta) + (4 \delta + 2 w _ {2} + 2 \beta_ {0}) (\delta + N w _ {1})}{4 (\beta - \delta) + 8 (\delta + N w _ {1})} & \text { if } \beta_ {0} <   \underline {{\beta}} _ {0} ^ {c _ {2 1}} \\ \frac {\delta + \beta_ {0}}{2} & \text { if } \underline {{\beta}} _ {0} ^ {c _ {2 1}} \leq \beta_ {0} \leq \overline {{\beta}} _ {0} ^ {c _ {2 1}} \\ \frac {2 N w _ {1} + w _ {2} + 3 \delta}{4} & \text { if } \beta_ {0} > \overline {{\beta}} _ {0} ^ {c _ {2 1}} \end{array} \right.\tag{27}
$$

$$
p _ {2} ^ {c _ {2 1}} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (2 N w _ {1} - w _ {2} + \delta) - 2 (w _ {2} - \beta_ {0}) (\delta + N w _ {1})}{2 (\beta - \delta) + 4 (\delta + N w _ {1})} & \text { if } \beta_ {0} <   \underline {{\beta}} _ {0} ^ {c _ {2 1}} \\ \beta_ {0} - w _ {2} & \text { if } \underline {{\beta}} _ {0} ^ {c _ {2 1}} \leq \beta_ {0} \leq \overline {{\beta}} _ {0} ^ {c _ {2 1}} \\ \frac {2 N w _ {1} - w _ {2} + \delta}{2} & \text { if } \beta_ {0} > \overline {{\beta}} _ {0} ^ {c _ {2 1}}, \end{array} \right.\tag{28}
$$

$$
\text { where } \overline {{\beta}} _ {0} ^ {c _ {2 1}} = \frac {2 N w _ {1} + w _ {2} + \delta}{2} \text { and } \underline {{\beta}} _ {0} ^ {c _ {2 1}} = \frac {(\beta - \delta) (2 N w _ {1} + w _ {2} + \delta) + 2 (w _ {2} + \beta_ {0}) (\delta + N w _ {1})}{2 (\beta - \delta) + 4 (\delta + N w _ {1})}.
$$

## 5.1.4. Analysis of system and competition effects

We <sup>fi</sup>rst we examine the effects of system parameters (e.g. security quality and download capacity) on the equilibrium price, demand, and revenue levels. Then, we analyze the impact of competition structure on the equilibrium results.

5.1.4.1. Analysis of system effect. Examining the resulting price and pro<sup>fi</sup>t levels in various system parameter settings, we derive the following interesting observations.

## Proposition 4. Effect of system parameter in competing channels

1. When the market is fully (partially) served, both price and profit levels of the Web and P2P channels always increase (may decrease) as the P2P channel provides poorer quality of P2P security and/or the Web channel installs smaller sever capacity.

2. However, the impact of capacity of peer nodes on the two channels are opposite: higher speed of P2P file transfer will increase price and profit levels of the P2P channel service but decrease price and profit levels of the Web channel service.

Proposition 4 reveals an interesting phenomenon: when the demand is so strong such that the market is fully served $( \widehat { \theta } _ { 1 } { < } 0 )$ , competing channels have little incentive in improving their service quality. The driver of this occurrence can be explained as follows. As one of the competing channels offers worse service (P2P security quality or website capacity), the other channel will set a higher price in order to make a higher pro<sup>fi</sup>t. Accordingly, calculating that one's opponent will also adopt a higher price strategy, a channel raises its price as well. As a result, the revenue levels of both channels increase.

The intuition of Part 2 of Proposition 4 works as follows. In the model, as the users are assumed to have homogeneous sensitivity on the download delay, the P2P channel always bene<sup>fi</sup>ts from faster <sup>fi</sup>le transfer and sets a higher price, while the Web channel needs to cut its price to avoid losing customers. It is noteworthy that the divergent implications of Web and P2P capacities are mainly due to the distinguishing characteristic of a congestible Web channel and a scalable P2P channel. As the P2P channel bene<sup>fi</sup>ts from faster P2P <sup>fi</sup>le transfer but not higher quality of P2P security technology; instead of developing advanced <sup>fi</sup>le sharing security technology, it is suggested that the P2P channel develop appropriate incentive mechanisms to induce peer nodes to contribute larger bandwidth capacity.

If the market is partially served $( { \hat { \theta } } _ { 1 } { < } 0 ) ,$ , our numerical simulations reveal that better QoS (ie. higher Website capacity and better P2P security) still always results in lower price levels in both channels but the effect of QoS on revenue levels may be positive or negative. As the QoS of either channel is improved, both channels will cut its price and the demands of both channel increase. Fig. 3 demonstrates the negative effect of QoS on the price and Fig. 4 illustrates that the impact of QoS on the revenue of a channel is positive (negative) when the individual perceived values of content download are high (low) and could be non-monotonic. From another perspective, we can conclude that if QoS becomes lower, the service quality and price effects will force the demand to shrink (from a fully served market to become a partially served market) and the revenues of the channels are eventually reduced if the content value is not very high.

For a long time, Akamai holds market dominance in the content distribution industry. It charged a lot of money for delivering bits more reliably. However, with the emergence of competitors (such as Limelight), Akamai provides content delivery service with better quality but charges a lower price [21,44].

5.1.4.2. Analysis of competition effect. Comparing the results under various competition structures, we summarize a few interesting <sup>fi</sup>ndings as shown in Table 3.

## Proposition 5. Effect of competition structure

1. Compared to the results of simultaneous price competition, both channels set a higher price and collect a higher profit under sequential competition.

2. Compared to the results of simultaneous price competition, the demand of the leader channel decreases, whereas the demand of the follower channel increases.

3. A channel sets a higher price and makes less profit when it is the leader rather than the follower, under sequential competition.

What we have discovered from the equilibrium results is that both competing channels bene<sup>fi</sup>t from a market with sequential decisions, and being the second mover has superior advantages. The intuition concerning the results (Proposition 5) is described as follows. When the leader channel sets its price in the <sup>fi</sup>rst period, it predicts that the follower channel will slightly undercut its price in order to obtain a larger demand. The prediction puts pressure on the leader channel to maintain a high price in order to avoid having the follower channel set a very low demand. Hence, both channels set prices higher than the price level of simultaneous price competition. As a result, both channels make higher pro<sup>fi</sup>ts from setting higher prices. We can also observe that compared to price levels of simultaneous competition, the increase in price to the leader channel is larger than the increase in price to the follower channel That causes the demand of the leader channel to decrease, whereas the demand of the followei channel increases. Since the follower channel can set a slightly lower price than the leader channel to enlarge its demand, it makes higher pro<sup>fi</sup>t than it does from being a leader. Therefore, both competing channels prefer sequential price competition and wish its opponent to be the <sup>fi</sup>rst mover. That is, the second mover advantage phenomenon occurs under the scenario of sequential price competition.

Research had asserted that Internet <sup>fi</sup>rst mover advantages do exist, but companies seemed to overestimate their importance [59]. From the evolution patterns of content distribution evolution, for example, although the Web channel like Internap (1996) and Akamai (1998) was the <sup>fi</sup>rst mover, RawFlow (P2P-channel) was introduced in 2002. On the other hand, the P2P channel does not dominate the market as a follower Web channel like BitGravity (2006) sequentially emerged. This indicates that the potential follower advantages can still be recognized and exploited.

## 5.2. Pricing in collaborating channels

These two channels may collaborate (or be integrated) as a single channel provider or form a strategic alliance to maximize joint pro<sup>fi</sup>t. For example, advanced content distribution systems, such as DOH [32] and CoralCDN [22], have been developed to provide such integrated channels.

![](/api/attachments/DK5EP8HT/fulltext/images/684eb6b015e24cdf400168f152646636494352cd4a31646d9a2c75c420b991ef.jpg)  
Fig. 3. Impact of website capacity on price.

![](/api/attachments/DK5EP8HT/fulltext/images/5639549e9dc350acb3e105a4fc894c8007f53ba184d8b265db0c7d98b5f9597d.jpg)  
Fig. 4. Impact of website capacity on revenue.

VELOCIX provides Velocix software services to deliver contents via both Web and P2P channels [67]. Because the channels are collaboratively operated, price decisions of these two channels are simultaneously made by the joint unit. Notice that some revenue sharing contract between two channels should be applied if they are still independent business units but jointly operated. If the two channels belong to the same company and all the revenues are received by the monopolistic company. Thus, the pro<sup>fi</sup>t maximization problem is formulated as:

$$
\max _ {p _ {1} ^ {m}, p _ {2} ^ {m}} \pi^ {m} = p _ {1} ^ {m} \eta_ {1} + p _ {2} ^ {m} \eta_ {2} - K _ {1} (b _ {1}) - K _ {2} (\delta) \quad \text { s.t. } \eta_ {1} + \eta_ {2} \leq N.\tag{29}
$$

Solving the pro<sup>fi</sup>t maximization problem, we obtain the prices and demands of both channels:

$$
p _ {1} ^ {m} = \left\{ \begin{array}{l l} \frac {\beta_ {0} + \beta}{2} & \text {if} \beta_ {0} <   \beta - \delta + w _ {2} \\ \frac {2 \beta_ {0} + \delta - w _ {2}}{2} & \text {if} \beta_ {0} \geq \beta - \delta + w _ {2} \end{array} \right., p _ {2} ^ {m} = \left\{ \begin{array}{l l} \frac {\beta_ {0} + \beta - \delta - w _ {2}}{2} & \text {if} \beta_ {0} <   \beta - \delta + w _ {2} \\ \beta_ {0} - w _ {2} & \text {if} \beta_ {0} \geq \beta - \delta + w _ {2} \end{array} \right..\tag{30}
$$

$$
\eta_ {1} ^ {m} = \left(\frac {w _ {2} + \delta}{N w _ {1} + \delta}\right) \frac {N}{2}, \eta_ {2} ^ {m} = \left\{ \begin{array}{l l} \left(\frac {2 N w _ {1} + \delta - w _ {2}}{N w _ {1} + \delta} - \frac {\beta - \beta_ {0} - \delta + w _ {2}}{\beta - \delta}\right) \frac {N}{2} & \text {if} \beta_ {0} <   \beta - \delta + w _ {2} \\ \left(\frac {2 N w _ {1} + \delta - w _ {2}}{N w _ {1} + \delta}\right) \frac {N}{2} & \text {if} \beta_ {0} \geq \beta - \delta + w _ {2} \end{array} \right..\tag{31}
$$

Examining Eq. (30), we have the following <sup>fi</sup>ndings:

## Proposition 6. Collaborating channels

1. The price level of the Web channel is always higher than that of the P2P-channel.

2. Collaborating pricing will result in under-usage in the Web channel.

The intuition of Proposition 6.1 is the integrated providers can improve revenue by reducing the delay in Web channel which is a main disutility for download service. The integrated providers can set a higher price for Web channel service so as to improve delay performance. However, the price is increased highly and results in inef<sup>fi</sup>cient (under-utilized) Web channel allocation. The price offset between the two channels: $\Delta p ^ { m } \bar { = } p _ { 1 } ^ { m } - p _ { 2 } ^ { m } = \left( \delta + w _ { 2 } \right) / 2$ , indicates that the integrated <sup>fi</sup>rm sets a higher price level for the Web channel. Since $\Delta p ^ { m } { > } \Delta p ^ { w }$ , the price level of the Web channel is still too high, compared to the ef<sup>fi</sup>ciency price level. As a result, contrast to the result derived from free-access policy, the problem of under-usage in the Web channel occurs when two channels are priced by an integrated <sup>fi</sup>rm.

## 6. Implications to the market size, channel interactions, and IT investment

## 6.1. Impact of market size and channel interactions

Market size (or the population of users) plays an important role in determining the optimal pricing scheme and corresponding channel allocation distribution. $\Delta p = p _ { 1 } - p _ { 2 }$ can be used to compare the price levels of two channels and whether the allocation is ef<sup>fi</sup>cient. Let $\varDelta p _ { w }$ be the ef<sup>fi</sup>cient price disperse level. $\Delta p { < } \Delta p _ { w } \left( \Delta p > \Delta p _ { w } \right)$ indicates that the Web channel is over (under)-utilized as the number of the Web channel uses is larger (smaller) than the ef<sup>fi</sup>cient one. Fig. 5 shows that the ef<sup>fi</sup>cient price disperse level is always positive and increases with the number of users. It reveals that free-access always results in over-usage of a Web channel and congestion becomes intensi<sup>fi</sup>ed as the number of users increases; consequently, a higher price should be charged on the Web channel users to recover the ef<sup>fi</sup>ciency loss. In an integrated market, the price level of the Web channel is always higher than that of the P2P-channel, which indicates under-usage in the Web channel. However, their difference is irrelevant to the market size. For two competing providers, the price of the Web channel is higher only when the market size is small. As the market grows, the P2P-channel may charge a higher price. Notice that for simplicity, the competition case in Fig. 5 was depicted based on simultaneous competition. The numerical results for the cases of sequential moves are similar. From the perspective of ef<sup>fi</sup>ciency, when the market is small, the Web channel is under-utilized. As the market size keeps growing, the Web channel become over-utilized.

Table 3  
Comparison of equilibrium results under various competition structures.

<table><tr><td>Leadership</td><td>Price  $p_i$ </td><td>Demand  $\eta_i$ </td><td>Profit  $\pi_i$ </td></tr><tr><td>Web channel</td><td> $p_i^{C_{12}} \geq p_i^c, i = 1,2$ </td><td> $\eta_1^{C_{12}} \leq \eta_1^c, \eta_2^{C_{12}} \geq \eta_2^c, \eta_2^{C_{12}} \geq \eta_1^{C_{12}}$ </td><td> $\pi_i^{C_{12}} \geq \pi_i^c, i = 1,2$ </td></tr><tr><td>P2P-channel</td><td> $p_i^{C_{21}} \geq p_i^c, i = 1,2$ </td><td> $\eta_1^{C_{21}} \geq \eta_1^c, \eta_2^{C_{21}} \leq \eta_2^c, ^*$ </td><td> $\pi_i^{C_{21}} \geq \pi_i^c, i = 1,2$ </td></tr><tr><td rowspan="2">Summary</td><td> $p_1^{C_{12}} \geq p_1^{C_{21}} \geq p_1^c$ </td><td> $\eta_1^{C_{21}} \geq \eta_1^c \geq \eta_1^{C_{12}}$ </td><td> $\pi_1^{C_{21}} \geq \pi_1^{C_{12}} \geq \pi_1^c$ </td></tr><tr><td> $p_2^{C_{21}} \geq p_2^{C_{12}} \geq p_2^c$ </td><td> $\eta_2^{C_{12}} \geq \eta_2^c \geq \eta_2^{C_{21}}$ </td><td> $\pi_2^{C_{12}} \geq \pi_2^{C_{21}} \geq \pi_2^c$ </td></tr></table>

\*η<sub>1</sub><sup>c21</sup> ≥ η<sub>2</sub><sup>c21</sup> when β<sub>0</sub>≥β<sup>c21</sup> . The opposite holds true whenβ<sub>0</sub>≤β<sup>c21</sup> .

![](/api/attachments/DK5EP8HT/fulltext/images/5479163c9be9459c51f00adc878a273d45cc3009858a484552576ec006f6b4c6.jpg)  
Fig. 5. Impact of market size on pricing scheme.

Fig. 6 shows the equilibrium market share (in percentage) of the Web channel with respect to various competition structures. The second mover advantage in obtaining higher market share is veri<sup>fi</sup>ed. From the perspective of economic ef<sup>fi</sup>ciency, the Web channel as the <sup>fi</sup>rst (second) mover is superb when the number of users is large (small). That ${ \mathrm { i } } s ,$ a competition structure with sequential moves is better than one with simultaneous decision structure when the number of users is suf<sup>fi</sup>ciently small or large.

## 6.2. Investment of P2P security technology and website capacity

An organization can make appropriate investment in developing advanced P2P security technology or in installing high website capacity to improve its ef<sup>fi</sup>ciency or pro<sup>fi</sup>tability. In this subsection, we examine the impact of market competition on the selection of information technology investment (e.g. P2P security level and

![](/api/attachments/DK5EP8HT/fulltext/images/f4f51730f6b4bfa7063e3369630300fa8f5d4fd9b7385204416aaeda8dfa79ed.jpg)  
Fig. 6. Impact of market size on channel allocation.

Website capacity). Of course, the service quality to be offered to the customers (users) is determined by these infrastructure investments. As described above, the cost of website capacity is a linear function on the capacity with properties: $\partial K _ { 1 } ( b _ { 1 } ) / \partial b _ { 1 } > 0 , \partial ^ { 2 } K _ { 1 } ( b _ { 1 } ) / \partial b _ { 1 } ^ { 2 } = 0 ,$ , and $K _ { 1 } ( 0 ) = 0 ;$ the cost of P2P security technology investment is a decreasingly convex function on capacity with properties: $\partial K _ { 2 } ( \delta ) /$ $\partial \delta < 0 , \partial K _ { 2 } ( \delta ) / \partial \delta \geq 0 ,$ , and $K _ { 2 } ( 0 ) = \infty .$ . We denote $\delta ^ { \bar { m } } \left( \bar { \delta ^ { c } } \right)$ as the optimal P2P security level of the collaborating (competing) channels and $\delta ^ { w }$ as the ef<sup>fi</sup>cient P2P security level that maximizes the overall value of the organization. $b _ { 1 } ^ { m } ( b _ { 1 } ^ { c } )$ is the optimal capacity of the Web channel in collaborating (competing) channels and $b _ { 1 } ^ { w }$ the ef<sup>fi</sup>cient capacity of the Web channel.

## Proposition 7. IT investment in a fully served market

1. A P2P-channel under-invests its P2P security technology. Formally, $\delta ^ { w } < \delta ^ { m } = \delta ^ { c }$

2. The Web capacity in collaborating channels is higher than that in the competing channels $( b _ { 1 } ^ { m } { > } b _ { 1 } ^ { c } )$ ).

The intuition of Proposition 7 can be interpreted as follows. As in a fully served competing market, improving P2P security quality and Web capacity only deteriorates the pro<sup>fi</sup>t levels of both competing channels (Proposition 4), a P2P-channel (Web channel) will choose the quality level of security technology (bandwidth capacity level) as low as possible. Consequently, a P2P-channel under-invests its P2P security technology and the Web capacity in collaborating channels is higher than that in the competing channels. Notice that compared to the ef<sup>fi</sup>cient level, Web capacity in a competing or collaborating channel may be higher or lower, depending on the relative security cost. As discussed in Proposition 4, when the market is partially served, the channels' revenues may increase or decrease with the QoS levels. Therefore, the Web channel capacity in a competing setting could be higher or lower than that in the collaborating setting.

## 7. Concluding remarks

Website and P2P networks are two important channels for distributing digital content and information well. In this paper, we have developed economic (game theoretic) models to investigate the allocation and pricing schemes of these two channels under the business environment of an organization and duopolistic markets

## 7.1. Summary of findings

Our analytical results show that it will be ef<sup>fi</sup>cient to direct more users to use the P2P channel in the absence of any pricing scheme. In order to enforce an ef<sup>fi</sup>cient con<sup>fi</sup>guration of channel allocation, a service fee on the Web channel is suggested. In duopolistic markets in which channels are operated by independent <sup>fi</sup>rms, the equilibrium pricing decisions and resulting demand distributions are signi<sup>fi</sup>cantly associated to the decision sequence of both channels. Both channels in a competition structure with sequential decision will obtain higher pro<sup>fi</sup>t. The price levels of both channels rise; however, the channel with leadership in pricing decision obtains less market share than does the follower channel. In duopolistic markets, a Web channel may charge a higher or lower price level than a P2P-channel, depending on the business environment. If these two channels are integrated into a <sup>fi</sup>rm, the price of a Web channel will always be higher than that of a P2P channel. However, the price is too high, so the channel allocation is still inef<sup>fi</sup>cient due to under-usage of the Web channel. In addition, we <sup>fi</sup>nd the effect of system parameters (such as P2P security quality and Web channel's capacity) on the revenues of two competing channels may be positive or negative, depending on whether a market is partially or fully served.

In Table 4, we summarize the impact of the business situation (value-maximizing organization or pro<sup>fi</sup>t-seeking <sup>fi</sup>rms in various market structures) and system parameters (market size, capacity of Web channel and peer nodes, and P2P security quality) on the equilibrium price and revenue levels. ℜ<sub>1</sub><sup>c</sup>, ℜ<sub>1</sub><sup>m</sup> (ℜ<sub>2</sub><sup>c</sup>, ℜ<sub>2</sub><sup>m</sup>) are the revenues of the Web channel (P2P-channel) in competing and collaborating channels.

Table 4  
Impact of system parameters on price and pro<sup>fi</sup>t.

<table><tr><td rowspan="2">Parameters</td><td colspan="4">Web channel</td><td colspan="4">P2P-channel</td></tr><tr><td> $p_1^c$ </td><td> $p_1^m$ </td><td> $\mathcal{R}_1^c$ </td><td> $\mathcal{R}_1^m$ </td><td> $p_2^c$ </td><td> $p_2^m$ </td><td> $\mathcal{R}_2^c$ </td><td> $\mathcal{R}_2^m$ </td></tr><tr><td>Market size N</td><td>+</td><td>*</td><td>+</td><td>+</td><td>+</td><td>*</td><td>+</td><td>+</td></tr><tr><td>Web capacity  $b_1$ </td><td>-</td><td>*</td><td>(?,-)</td><td>+</td><td>-</td><td>*</td><td>-</td><td>-</td></tr><tr><td>Peer capacity  $b_2$ </td><td>-</td><td>(*,+)</td><td>-</td><td>-</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>P2P securityδ</td><td>+</td><td>(*,+)</td><td>+</td><td>+</td><td>(-,+ )</td><td>(-,* )</td><td>(?,+)</td><td>-</td></tr></table>

Notation. (partial market and full market); +: positive effect; −: negative effect; \*: no effects; and ?: uncertain.

## 7.2. Managerial and policy implications

Our analytical results provide a few useful insights for developing business strategy and operations policy in content distribution. For the ef<sup>fi</sup>ciency-seeking organizations, because the Web channel tends to be over-used, the organizations may discourage or limit the usage of the Web channel. For example, only the high secret or light digital content can be downloaded from the Web channel, whereas general documents or heavy content should be retrieved from the P2Pchannel. As we analyzed, the number of users is a critical factor that determines whether an organization should adopt a P2P channel or not. When the number of users in an organization is small, offering only the Web channel is a better policy for content distribution. Once the number of users is beyond a threshold, an organization may seriously consider installing a P2P-channel to alleviate the congestion of the Web channel and improve the overall ef<sup>fi</sup>ciency of content distribution.

For the channel providers in a competing market, because of the competition pressure, they should recognize the customers' valuation on content service in order to correctly estimate the demand, develop the appropriate pricing scheme, and rightly adjust their investment strategy. When the content is essential to the customers and the demand is very strong, they should consider a low service quality strategy to save the infrastructure investment cost. However, if the demand is weak, they may consider adopting a high service quality strategy to attract more customers. In addition, because of inherent disadvantage of the <sup>fi</sup>rst mover in price competition, the channel providers should try to be the follower and carefully observe their opponents' moves before making a price decision.

## Appendix A

## A1. Proof of Proposition 1

1. $\eta _ { 2 } ^ { e } { > } 0 \Longleftrightarrow N { > } N ^ { e p }$ , where $N ^ { e p } = \left\{ \begin{array} { l l } { \frac { ( \beta w _ { 2 } - \delta \beta _ { 0 } ) } { w _ { 1 } ( \beta - \delta - w _ { 2 } + \beta _ { 0 } ) } } & { \mathrm { i f ~ } \beta _ { 0 } \le w _ { 2 } } \\ { b _ { 1 } / b _ { 2 } } & { \mathrm { i f ~ } \beta _ { 0 } \ge w _ { 2 } } \end{array} \right. .$

2. $\partial \eta _ { 1 } ^ { e } / \partial N { > } 0 , \partial \eta _ { 2 } ^ { e } / \partial N { > } 0 , \partial s _ { 1 } ^ { e } / \partial N { < } 0 , \partial s _ { 2 } ^ { e } / \partial N { > } 0 .$

$$
3. \eta_ {1} ^ {e} \geq \eta_ {2} ^ {e} \Longleftrightarrow N > \hat {N}, \text {   where   } \hat {N} = \left\{ \begin{array}{l l} \frac {(\beta - \delta) (w _ {2} + \delta) + \beta w _ {2} - \delta \beta_ {0}}{w _ {1} (\beta - \delta - w _ {2} + \beta_ {0})} & \text { if } \beta_ {0} \leq w _ {2} \\ \frac {2 w _ {2} + \delta}{w _ {1}} & \text { if } \beta_ {0} \geq w _ {2} \end{array} \right..
$$

## A2. Proof of Proposition 2

1. The statement can be shown by verifying η<sub>1</sub><sup>w</sup> ${ < \eta } _ { 1 } ^ { e }$ and $\eta _ { 2 } ^ { w } { > } \eta _ { 2 } ^ { e }$

For a provider with integrated channels, the best pricing strategy is to segment the market by charging a higher price on the Web channel and a lower price on the P2P-channel. In this way, the customers with higher (lower) valuation on the content are willing to purchase the content from the Web channel (P2P-channel). In addition, if the provider wishes to reduce the price disperse between two channels, a critical way is to improve the P2P security quality.

## 7.3. Limitation and directions for future study

In our model, we assume that the content achieved from two channels is identical, while the valuation of the content is heterogeneous for all customers. For the sake of analysis, the valuation function of content is assumed to be positively associated with the P2P security quality. The correlation between service valuation and other dimensions of QoS could be further investigated. In addition, the heterogeneity of two channels is mainly differentiated based on the delay and security risk. Investigating the corresponding pricing strategies under other heterogeneous setting is a desirable future extension. In the research, we only consider the competition between two pure heterogeneous channels. However, the players in competitive market may include providers offering integrated channels. Besides the investigation of competition and integration between horizontal <sup>fi</sup>rms (channels), an interesting direction for future research is to study the business environment in which multiple content providers (owners) and channel providers participate in competition and integration games in vertical as well as horizontal dimensions. The impact of various types of business contract among these players on business strategy development is a promising research issue. Another venue is to analyze the pricing and channel allocation from a dynamic perspective, in which the time factor should be carefully considered. In the research, we do not examine the participation issues of a P2P channel. Free-riding problem and bandwidth capacity <sup>fl</sup>uctuation will make the P2P channel less preferable. Therefore, how to develop appropriate incentive mechanisms is an important issue. Finally, as the results are mainly explored based on analytical models, further relevant empirical studies on the digital contribution channels are helpful for the validation of the analytical <sup>fi</sup>ndings.

## Acknowledgements

The author would like to thank the four anonymous reviewers for their insightful comments and helpful suggestions. This research was supported by the National Science Council of Taiwan (Republic of China) under the grant NSC 95-2416-H-009-024.

2. The statement can be shown by solving $\widehat { \theta } _ { 1 } = \widehat { \theta } _ { 2 }$ when $\beta _ { 0 } \leq w _ { 2 }$ and $\eta _ { 2 } ^ { w } = 0$ when $\beta _ { 0 } \ge w _ { 2 }$

A3. Proof of Proposition 3

$$
1. \Delta p ^ {w} = p _ {1} ^ {w} - p _ {2} ^ {w} = \frac {N w _ {1} (w _ {2} + \delta)}{2 N w _ {1} + \delta} > 0.
$$

$$
2. \frac {\partial \Delta p ^ {w}}{\partial N} = \frac {w _ {1} \delta (w _ {2} + \delta)}{(2 N w _ {1} + \delta) ^ {2}} > 0; \frac {\partial \Delta p ^ {w}}{\partial \delta} = \frac {N w _ {1} (2 N w _ {1} - w _ {2})}{(2 N w _ {1} + \delta) ^ {2}} > 0;
$$

$$
\frac {\partial \Delta p ^ {w}}{\partial f} = \frac {N b _ {2} \gamma (2 N \gamma^ {2} f ^ {2} + 2 \gamma f b _ {1} \delta + b _ {1} b _ {2} \delta^ {2})}{(2 N b _ {2} \gamma f + b _ {1} b _ {2} \delta) ^ {2}} > 0;
$$

$$
\frac {\partial \Delta p ^ {w}}{\partial b _ {1}} = \frac {\partial \Delta p ^ {w}}{\partial w _ {1}}. \frac {\partial w _ {1}}{\partial b _ {1}} = \frac {N (w _ {2} + \delta) \delta}{(2 N w _ {1} + \delta) ^ {2}}. \left(\frac {- \gamma f}{b _ {1} ^ {2}}\right) <   0; \frac {\partial \Delta p ^ {w}}{\partial b _ {2}} = \frac {\partial \Delta p ^ {w}}{\partial w _ {2}} \frac {\partial w _ {2}}{\partial b _ {2}} = \frac {N w _ {1}}{2 N w _ {1} + \delta} \left(\frac {- \gamma f}{b _ {2} ^ {2}}\right) <   0
$$

A4. Proof of Proposition 4. For a fully served market $( \widehat { \theta } _ { 1 } { < } 0 )$ , we have

$$
\pi_ {1} ^ {c} = \frac {N (N w _ {1} + w _ {2} + 2 \delta) ^ {2}}{9 (N w _ {1} + \delta)} - K _ {1} (b _ {1}), \pi_ {2} ^ {c} = \frac {N (2 N w _ {1} - w _ {2} + \delta) ^ {2}}{9 (N w _ {1} + \delta)} - K _ {2} (\delta);
$$

$$
\pi_ {1} ^ {c _ {1 2}} = \frac {N (N w _ {1} + w _ {2} + 2 \delta) ^ {2}}{8 (N w _ {1} + \delta)} - K _ {1} (b _ {1}), \pi_ {2} ^ {c _ {1 2}} = \frac {N (3 N w _ {1} - w _ {2} + 2 \delta) ^ {2}}{1 6 (N w _ {1} + \delta)} - K _ {2} (\delta);
$$

$$
\pi_ {1} ^ {c _ {1 2}} = \frac {N (N w _ {1} + w _ {2} + 2 \delta) ^ {2}}{8 (N w _ {1} + \delta)} - K _ {1} (b _ {1}), \pi_ {2} ^ {c _ {1 2}} = \frac {N (3 N w _ {1} - w _ {2} + 2 \delta) ^ {2}}{1 6 (N w _ {1} + \delta)} - K _ {2} (\delta).
$$

It can be easily veri<sup>fi</sup>ed that

1. ∂π $/ \partial z { > } 0$ for ${ \pi } { \in } \{ \pi _ { 1 } ^ { c } , \pi _ { 2 } ^ { c } , \pi _ { 1 } ^ { c _ { 1 2 } } , \pi _ { 2 } ^ { c _ { 1 2 } } , \pi _ { 1 } ^ { c _ { 2 1 } } , \pi _ { 2 } ^ { c _ { 2 1 } } \}$ and $z { \in } \{ w _ { 1 } , \delta \}$

2. $\partial \pi _ { 1 } / \partial w _ { 2 } { > } 0$ and $\partial \pi _ { 2 } / \partial w _ { 2 } { < } 0$ for $\pi _ { 1 } { \in } \{ \pi _ { 1 } ^ { c } , \pi _ { 1 } ^ { c _ { 1 2 } } , \pi _ { 1 } ^ { c _ { 2 1 } } \}$ and $\pi _ { 2 } \in \{ \pi _ { 2 } ^ { c } , \pi _ { 2 } ^ { c _ { 1 2 } } , \pi _ { 2 } ^ { c _ { 2 1 } } \}$

For a partially market $( \widehat { \theta } _ { 1 } { < } 0 )$ , we illustrate the results by numerical examples (Figs. 3 and 4).

A5. Proof of Proposition 5. According to Eqs. (18), (19), (22), (23), (27), and (28), we can derive and compare the demand and pro<sup>fi</sup>t levels of the two channels under various market structures and have the results showed in Table 3. □

A6. Proof of Proposition 6. From Eq. (30), we have

$$
\Delta p ^ {m} = p _ {1} ^ {m} - p _ {2} ^ {m} = (\delta + w _ {2}) / 2; \partial \Delta p ^ {m} / \partial b _ {2} <   0.
$$

2. Since $\begin{array} { r } { \Delta p ^ { m } = \frac { \delta + w _ { 2 } } { 2 } > \frac { N w _ { 1 } ( w _ { 2 } \ + \ \delta ) } { 2 N w _ { 1 } \ + \ \delta } = \Delta p ^ { w } } \end{array}$ , we have $\eta _ { 1 } ^ { m } { < } \eta _ { 1 } ^ { w } .$

A7. Proof of Proposition 7. When the market is fully served $( \widehat { \theta } _ { 1 } { < } 0 )$ , from Proposition 4, we have $\partial \pi _ { 2 } ^ { c } / \partial \delta > 0$ and $\partial \pi _ { 1 } ^ { c } / \partial b _ { 1 } { < } 0 ,$ , which indicates IT investment will only decrease the revenue of each competing channel. The overall revenue of collaborating channels

$$
\mathfrak {R} ^ {\mathrm{m}} = \left\{ \begin{array}{l l} \frac {\beta_ {0} + \beta}{2} \Big (\frac {w _ {2} + \delta}{N w _ {1} + \delta} \Big) \frac {N}{2} + \frac {\beta_ {0} + \beta - \delta - w _ {2}}{2} \Big (\frac {2 N w _ {1} + \delta - w _ {2}}{N w _ {1} + \delta} - \frac {\beta - \beta_ {0} - \delta + w _ {2}}{\beta - \delta} \Big) \frac {N}{2} & \text {if} \beta_ {0} <   \beta - \delta + w _ {2} \\ \frac {2 \beta_ {0} + \delta - w _ {2}}{2} \Big (\frac {w _ {2} + \delta}{N w _ {1} + \delta} \Big) \frac {N}{2} + (\beta_ {0} - w _ {2}) \Big (\frac {2 N w _ {1} + \delta - w _ {2}}{N w _ {1} + \delta} \Big) \frac {N}{2} & \text {if} \beta_ {0} \geq \beta - \delta + w _ {2} \end{array} . \right.
$$

Because $\partial \mathcal { R } ^ { m } / \partial \delta { > } 0$ and $\partial \mathfrak { R } ^ { m } / \partial b _ { 1 }$ may be greater or less than 0, we have $\delta ^ { w } < \delta ^ { c } = \delta ^ { m }$ and $b _ { 1 } ^ { c } < b _ { 1 } ^ { m }$

## A8. The impact of convexity of delay function

We use a general convex form of the delay function to show that over-utilization of the Web channel always occurs. Firstly, we denote the delay function as $\eta _ { 1 } ^ { \alpha } w _ { 1 }$ , where $\alpha \ge 1$ . The demand of the Web channel becomes $\begin{array} { r } { \eta _ { 1 } = \left( 1 - \frac { \eta _ { 1 } ^ { \alpha } w _ { 1 } - w _ { 2 } \ + \ p _ { 1 } - p _ { 2 } } { \delta } \right) { N } } \end{array}$ y. The number of the Web channel users in self-selection equilibrium is given by solving equation

$$
\Big (\delta + N (\eta_ {1} ^ {e}) ^ {\alpha - 1} w _ {1} \Big) \eta_ {1} ^ {e} = (w _ {2} + \delta) N\tag{A1}
$$

As expected, convexity of delay function will result in less demand of the Web channe $( \mathrm { i } . \mathsf { e } . \eta _ { 1 } ^ { e } ( a = 1 ) { > } \eta _ { 1 } ^ { e } ( a { > } 1 ) )$

Next, the ef<sup>fi</sup>cient allocation con<sup>fi</sup>guration of the channels can be obtained by solving the following objective function.

$$
\max _ {\hat {\theta} _ {1}, \hat {\theta} _ {2}} W = N (1 - \hat {\theta} _ {2}) \left(\frac {\beta}{2} (1 + \hat {\theta} _ {2}) - N ^ {\alpha} (1 - \hat {\theta} _ {2}) ^ {\alpha} w _ {1}\right) + N (\hat {\theta} _ {2} - \hat {\theta} _ {1}) \left(\frac {(\beta - \delta)}{2} (\hat {\theta} _ {2} + \hat {\theta} _ {1}) - w _ {2}\right) + N (1 - \hat {\theta} _ {1}) \beta_ {0} \quad s. t. 0 <   \hat {\theta} _ {1} <   \hat {\theta} _ {2} <   1
$$

The ef<sup>fi</sup>cient number of the Web channel users η<sup>w</sup> is given by solving $\partial W / \partial { \hat { \theta } } _ { 2 }$ or equation

$$
\left(\delta + N (\alpha + 1) \left(\eta_ {1} ^ {w}\right) ^ {\alpha - 1} w _ {1}\right) \eta_ {1} ^ {w} = (w _ {2} + \delta) N\tag{A2}
$$

Comparing Eq. (A1) with $\operatorname { E q . }$ (A2), we can observe that $\eta _ { 1 } ^ { e } { > } \eta _ { 1 } ^ { w }$ always holds as long as αN0. That is over-utilization in the Web channel that always occurs whenever congestion externality exists in the Web channel. When the delay is more convex on the demand, both η<sup>e</sup> and η become smaller, but $\eta _ { 1 } ^ { e } { > } \eta _ { 1 } ^ { w }$ always holds.

## A9. Revenue sharing mechanism

Assume the revenue sharing rate (the percentage of revenue to be transferred from content retailers to a content owner) for the Web channe and the P2P channel are $\varphi _ { 1 }$ and $\varphi _ { 2 }$ respectively. $\varphi _ { 1 }$ and $\varphi _ { 2 }$ are determined by the relative bargaining power between the content owners and channel providers.

For competing channels, the pro<sup>fi</sup>t of these two competing channel providers becomes

$$
\pi_ {1} ^ {c} (\varphi_ {1} ^ {c}) = (1 - \varphi_ {1} ^ {c}) p _ {1} ^ {c} \eta_ {1} ^ {c} - K _ {1} (b _ {1}), \pi_ {2} ^ {c} (\varphi_ {2} ^ {c}) = (1 - \varphi_ {2} ^ {c}) p _ {2} ^ {c} \eta_ {2} ^ {c} - K _ {2} (\delta),
$$

and the pro<sup>fi</sup>t of the content owner can be formulated as

$$
\pi_ {0} ^ {c} (\varphi_ {1} ^ {c}, \varphi_ {2} ^ {c}) = \varphi_ {1} ^ {c} p _ {1} ^ {c} \eta_ {1} ^ {c} + \varphi_ {2} ^ {c} p _ {2} ^ {c} \eta_ {2} ^ {c} - K _ {0},
$$

where $K _ { 0 }$ is the <sup>fi</sup>xed cost for content creation.

If the content owner is monopolistic and has dominant bargaining power, then φ<sub>i</sub><sup>c\*</sup> are given by solving $\pi _ { i } ^ { c } ( \varphi _ { i } ^ { c } ) = 0$ , where $i { \in } \{ 1 , 2 \}$ . When only a single revenue sharing rate is adopted, we can obtain the rate as $\begin{array} { r } { \Phi _ { m } ^ { c ^ { * } } = \operatorname* { m i n } _ { i } \left( \Phi _ { i } ^ { c ^ { * } } \right) } \end{array}$

For the collaborating channels, only a single rate is used and the pro<sup>fi</sup>t the integrated channels is formulated as

$$
\pi^ {m} (\varphi^ {m}) = (1 - \varphi^ {m}) (p _ {1} ^ {m} \eta_ {1} + p _ {2} ^ {m} \eta_ {2}) - K _ {1} (b _ {1}) - K _ {2} (\delta).
$$

It is easy to observe that the resulting equilibrium pricing and demand levels of both two channels are the same as those shown in Subsections 5.1 and 5.2.

## References

[1] AFTRS, Business models for digital distribution 2008—research summary, web page: http://csb.aftrs.edu.au/download.cfm?DownloadFile=C43C1A11-145E-3FE8- 82A1723458459A77, accessed at: Aug 4. 2009.

[2] E. Anderson, G.S. Day, V.K. Rangan, Strategic channel design, Sloan Management Review 38 (4) (1997) 59–69.

[3] S. Androutsellis Theotokis, D. Spinellis, A survey of peer-to-peer content distribution technologies, ACM Computing Surveys 36 (4) (2004) 335–371.

[4] AT&T, AT&T Announces new digital media solutions portfolio to deliver and manage multimedia content for businesses worldwide, web page: http://www. att.com/gen/press-room?cdvn=news&newsarticleid=25853&pid=4800, accessed at: Mar 5, 2009.

[5] S. Aughton, P2P activity continues to <sup>fl</sup>ourish, web page: http://www.pcpro.co.uk/ news/82134/p2p-activity-continues-to-<sup>fl</sup>ourish.html, accessed at: Mar 5, 2009.

[6] S. Balasubramanian, Mail versus mall: a strategic analysis of competition between direct marketers and conventional retailers, Marketing Science 17 (3) (1998) 181–195.

[7] P. Barford, M. Crovella, Generating representative web workloads for network and server performance evaluation, ACM SIGMETRICS Performance Evaluation Review 26 (1) (1998) 151–160.

[8] T. Bektas, O. Oguz, I. Ouveysi, Designing cost-effective content distribution networks, Computers and Operations Research 34 (8) (2007) 2436–2449.

[9] F. Bernstein, J.S. Song, X. Zheng, Bricks-and-mortar vs. clicks-and-mortar: an equilibrium analysis, European Journal of Operational Research 187 (3) (2008) 671–690.

[10] J. Bockstedt, R.J. Kauffman, F.J. Riggins, The move to artist-led online music distribution: explaining structural changes in the digital music market, The 38th Annual Hawaji International Conference on System Sciences 2005

[11] J.R. Brown, R.F. Lusch, D.D. Muehling, Con<sup>fl</sup>ict and power-dependence relations in retailer–supplier channels, Journal of Retailing 59 (4) (1983) 53–80.

[12] G. Cachon, Supply chain coordination with contracts, Handbooks In Operations Research and Management Science 11. (2003) 229–340

[13] A. Caruana, A.H. Money, P.R. Berthon, Service quality and satisfaction—the moderating role of value, European Journal of Marketing 34 (11/12) (2000) 1338–1353.

[14] S.C. Choi, Price competition in a duopoly common retailer channel, Journal of Retailing 72 (2) (1996) 117–134.

[15] B.Y. Choi, S. Moon, Z.L. Zhang, K. Papagiannaki, C. Diot, Analysis of point-to-point packet delay in an operational network, Computer Networks 51 (13) (2007) 3812–3827.

[16] A.T. Coughlan, D.A. Soberman, Strategic segmentation using outlet malls, International Journal of Research in Marketing 22 (1) (2005) 61–86.

[17] N. Daswani, H. Garcia-Molina, B. Yang, Open problems in data-sharing peer-topeer systems, Lecture Notes in Computer Science (2003) 1–15.

[18] S. Dewan, H. Mendelson, User delay costs and internal pricing for a service facility Management Science (1990) 1502–1517.

[19] L. Dignan, Amazon launches CloudFront: content delivery network margins go kaboom, web page: http://blogs.zdnet.com/BTL/?p=10904/. Accessed at: Mar 5, 2009.

[20] A. Dumrongsiri, M. Fan, A. Jain, K. Moinzadeh, A supply chain model with direct and retail channels, European Journal of Operational Research 187 (3) (2008) 691–718.

[21] D. Farber, BitGravity challenges Akamai and Limelight, web page: http://blogs. zdnet.com/BTL/?p=6456&tag=rbxccnbzd1. accessed at: 26 Mar. 2009.

[22] M.J. Freedman, E. Freudenthal, D. Mazieres, Democratizing content publication with Coral, web page: http://www.usenix.org/publications/library/proceedings/ nsdi04/tech/full\_papers/freedman/freedman\_html/, accessed at: 11 Mar, 2009.

[23] S. Gadde. I. Chase, M. Rabinovich, Web caching and content distribution: a view from the interior, Computer Communications 24 (2) (2001) 222–231.

[24] D. Ghosal, B.K. Poon, K. Kong, P2P contracts: a framework for resource and service exchange, Future Generation Computer Systems 21 (3) (2005) 333–347.

[25] L.A. Guardiola, A. Meca, J. Timmer, Cooperation and pro<sup>fi</sup>t allocation in distribution chains, Decision Support Systems 44 (1) (2007) 17–27.

[26] K.P. Gummadi, R.J. Dunn, S. Saroiu, S.D. Gribble, H.M. Levy, J. Zahorjan, Measurement, modeling, and analysis of a peer-to-peer <sup>fi</sup>le-sharing workload, The 9th ACM Symposium on Operating Systems Principles, Bolton Landing, NY, USA, 2003.

[27] A. Gupta, D.O. Stahl, A.B. Whinston, The economics of network management, Communications of the ACM 42 (9) (1999) 57–63.

[28] B. Helm, BitTorrent goes Hollywood web page: http://www.businessweek.com/ technology/content/may2006/tc20060508\_693082.htm, accessed at: 20 Mar, 2009

[29] J. Hughes, K.R. Lang, R. Vragov, An analytical framework for evaluating peer-topeer business models, Electronic Commerce Research and Applications 7 (1) (2008) 105–118.

[30] C. Iheagwara, A. Blyth, The impact of security layering on end-to-end latency and system performance in switched and distributed e-business environments, Computer Networks 39 (6) (2002) 827–840.

[31] Internap, hybrid peer-to-peer (P2P) access, web page: http://www.internap.com cdn-services/deliver/p2p-access.html, accessed at: Mar 25, 2009

[32] J. Jernberg, V. Vlassov, A. Ghodsi, S. Haridi, DOH: a content delivery peer-to-peer network, Lecture Notes in Computer Science 4128 (2006) 1026–1038.

[33] T. Karagiannis, P. Rodriguez, K. Papagiannaki, Should internet service providers fear peer-assisted content distribution? The 5th ACM SIGCOMM Conference on Internet Measurement, USENIX Association Berkeley, CA, USA, 2005.

[34] J.B. Kim, A. Segev, A web services-enabled marketplace architecture for negotiation process management, Decision Support Systems 40 (1) (2005) 71–87.

[35] P. Konana, A. Gupta, A.B. Whinston, Integrating user preferences and real-time workload in information services, Information Systems Research 11 (2) (2000) 177–196.

[36] N. Kumar, R. Ruan, On manufacturers complementing the traditional retail channel with a direct online channel, Quantitative Marketing and Economics 4 (3) (2006) 289–323.

[37] V. Kumar, D. Shah, R. Venkatesan, Managing retailer pro<sup>fi</sup>tability—one customer at a time! Journal of Retailing 82 (4) (2006) 277–294.

[38] S.H. Kwok, K.R. Lang, K.Y. Tam, Peer-to-peer technology business and service models: risks and opportunities, Electronic Markets 12 (3) (2002) 175–183.

[39] K.R. Lang, R. Vragov, A pricing mechanism for digital content distribution over computer networks, Journal of Management Information Systems 22 (2) (2005) 121–139.

[40] R.R. Levary, R.G. Mathieu, Hybrid retail: integrating e-commerce and physical stores, Industrial Management 42 (5) (2000) 6–21.

[41] R.T.B. Ma, S.C.M. Lee, J.C.S. Lui, D.K.Y. Yau, Incentive and service differentiation in P2P networks: a game theoretic approach, IEEE/ACM Transactions on Networking 14 (5) (2006) 978–991.

[42] W.Y. Ma, B. Shen, J. Brassil, Content services network: the architecture and protocols International Workshop on Web Caching and Content Distribution, 2001.

[43] J.K. MacKie-Mason, H.R. Varian, Pricing congestible network resources, IEEE Journal on Selected Areas in Communications 13 (7) (1995) 1141–1149.

[45] T.W. McGuire, R. Staelin, An industry equilibrium analysis of downstream vertical integration, Marketing Science 2 (2) (1983) 161–191.

[46] L.W. McKnight, J. Boroumand, Pricing internet services: proposed improvements Computer 33 (3) (2000) 108–109.

[47] H. Mendelson, S. Whang, Optimal incentive-compatible priority pricing for the M/ M/1 queue, Operations Research (1990) 870–883.

[48] C. Mohan, Caching technologies for web applications, Very Large Data Bases Conference, Morgan Kaufmann Publishers Inc, San Francisco, CA, USA, 2001.

[49] B. Molina Moreno, C.E. Palau Salvador, M. Esteve Domingo, I. Alonso Pena, V. Ruiz Extremera On content delivery network implementation Computer Communications 29 (12) (2006) 2396–2412.

[50] J. Ni, D.H.K. Tsang, I.S.H. Yeung, X. Hei, Hierarchical content routing in large-scale multimedia content delivery network, IEEE International Conference on Communications, 2003, pp. 854–859.

[51] J. Niccolai, Microsoft readies BitTorrent alternative Avalanche technology could make it easier to distribute big <sup>fi</sup>les over the internet, IDG News Service, 2005.

[52] V.N. Padmanabhan, L. Qiu, The content and access dynamics of a busy web site: <sup>fi</sup>ndings and implications, The Conference on Applications, Technologies, Architectures, and Protocols for Computer Communication, ACM, New York, NY, USA, 2000.

[53] V.N. Padmanabhan, K. Sripanidkulchai, The case for cooperative networking, First International Workshop on Peer-to-Peer Systems, Springer, 2002.

[54] V.N. Padmanabhan, H.J. Wang, P.A. Chou, K. Sripanidkulchai, Distributing streaming media content using cooperative networking, International Workshop on Network and Operating Systems Support for Digital Audio and Video, ACM, New York, NY, USA, 2002.

[55] G. Pallis, A. Vakali, Insight and perspectives for content delivery networks, Communications of the ACM 49 (1) (2006) 101–106.

[56] M. Parameswaran, A. Susarla, A.B. Whinston, P2P networking: an information sharing alternative, Computer 34 (7) (2001) 31–38.

[57] M. Pathan, R. Buyya, J. Broberg, Internetworking of CDNs, Content Delivery Networks (2008) 389.

[58] J.S. Raju, A. Roy, Market information and <sup>fi</sup>rm performance, Management Science 46 (8) (2000) 1075–1084.

[59] S. Rangan, R. Adner, Pro<sup>fi</sup>ts and the internet: seven misconceptions, MIT Sloan Management Review 42 (4) (2001) 44.

[60] D. Rayburn, Worldwide video CDN revenue \$400 million in 08, grow to over \$1.4 billion by 2012, web page: http://blog.streamingmedia.com/ the\_business\_of\_online\_vi/2008/08/worldwide-video.html, accessed at: Mar 3, 2009.

[61] D. Reisinger, Daily tidbits: Joost kills software application, web page: http://news. cnet.com/8301-17939 109-10125447-2.html.accessed at: Mar 4 2009

[62] P. Rodriguez, S.M. Tan, C. Gkantsidis, On the feasibility of commercial, legal P2P content distribution, ACM SIGCOMM Computer Communication Review 36 (1) (2006) 75–78.

[63] A. Roy, D.M. Hanssens, J.S. Raju, Competitive pricing by a price leader, Management Science 40 (7) (1994) 809–823.

[64] S. Saroiu, K.P. Gummadi, R.J. Dunn, S.D. Gribble, H.M. Levy, An analysis of internet content delivery systems, ACM SIGOPS Operating Systems Review 36 (2002) 315–327.

[65] M. Sayal, Y. Breitbart, P. Scheuermann, R. Vingralek, Selection algorithms for replicated web servers, ACM SIGMETRICS Performance Evaluation Review 26 (3) (1998) 44–50.

[66] H. van den Berg, M. Mandjes, R. Nunez-Queija, Pricing and distributed QoS control for elastic network traf<sup>fi</sup>c, Operations Research Letters 35 (3) (2007) 297–307.

[67] L. Velocix Co, Providing robust and ef<sup>fi</sup>cient download services for software applications, upgrades and drivers, web page: http://www.cachelogic.com/ solutions\_software.php, accessed at: 11 Mar, 2009.

[68] V. Vlachos, S. Androutsellis-Theotokis, D. Spinellis, Security applications of peerto-peer networks, Computer Networks 45 (2) (2004) 195–205.

[69] D.S. Wallach, A survey of peer-to-peer security issues, Lecture Notes in Computer Science (2003) 42–57.

[70] Y. Wang, H.P. Lo, Y. Yang, An integrated framework for service quality, customer value, satisfaction: evidence from China's telecommunication industry, Information Systems Frontiers 6 (4) (2004) 325–340

[71] B. Wire Internap enhances industry-leading CDN with peer-to-peer (P2P). Web page: http://<sup>fi</sup>les.shareholder.com/downloads/INTERNAP/0x0x141191/239bf19d– 861c-48ff-bbd7–221ca958da15/272889.pdf, accessed at: 16 Mar, 2009.

![](/api/attachments/DK5EP8HT/fulltext/images/12862f7602776f5910468e977a331a3a8090b4ef616f1aed92ba92cef6430e3e.jpg)  
Yung-Ming Li is an Associate Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington, His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, European Journal of Operational Research, Decision Support Systems, Electronic Commerce Research and Applications, Computers in Human Behavior, International Conference on Information Systems (ICIS), and Workshop on Information Technology and Systems (WITS).
