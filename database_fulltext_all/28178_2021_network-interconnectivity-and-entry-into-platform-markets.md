---
otero_id: 28178
otero_key: "457KUVF4"
title: "Network Interconnectivity and Entry into Platform Markets"
authors: "Feng Zhu; Xinxin Li; Ehsan Valavi; Marco Iansiti"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Network Interconnectivity and Entry into Platform Markets

Feng Zhu,<sup>a</sup> Xinxin Li,<sup>b</sup> Ehsan Valavi,<sup>a</sup> Marco Iansiti<sup>a</sup>

<sup>a</sup> Harvard Business School, Harvard University, Boston, Massachusetts 02163; <sup>b</sup> School of Business, University of Connecticut, Storrs, Connecticut 06269

Contact: fzhu@hbs.edu, https://orcid.org/0000-0002-3034-6876 (FZ); xinxin.li@uconn.edu, https://orcid.org/0000-0002-0805-4228 (XL); evalavi@hbs.edu (EV); miansiti@hbs.edu (MI)

Received: March 19, 2019 Revised: December 11, 2019; November 21, 2020; January 20, 2021 Accepted: January 21, 202 Published Online in Articles in Advance: May 20, 2021

https://doi.org/10.1287/isre.2021.1010

Copyright: © 2021 INFORMS

Abstract. Digital technologies have led to the emergence of many platforms in our economy today. In certain platform networks, buyers in one market purchase services from providers in many other markets, whereas in others, buyers primarily purchase services from providers within the same market. Accordingly, network interconnectivity—which measures the degree to which consumers in one market purchase services from service providers in a different market—varies across different industries. We examine how network interconnectivity affects interactions between an incumbent platform serving multiple markets and an entrant platform seeking to enter one of these markets. Our model yields several interesting results. First, even if the entrant can advertise at no cost, it still may not want to make every user in a local market aware of its service, as doing so may trigger a competitive response from the incumbent. Second, having more mobile buyers, which increases interconnectivity between markets, can reduce the incumbent’s incentive to <sup>fi</sup>ght and, thus, increase the entrant’s incentive to expand. Third, stronger interconnectivity between markets may or may not make the incumbent more defensible: when advertising is not costly and mobile buyers consume in both their local markets and the markets they visit, a large number of mobile buyers will increase the entrant’s pro<sup>fi</sup>tability, thereby making it dif<sup>fi</sup>cult for the incumbent to deter entry. However, when advertising is costly or mobile buyers only consume in the markets they travel to, a large number of mobile buyers will help the incumbent deter entry. When advertising cost is at an intermediate level, the entrant prefers a market with moderate interconnectivity between markets. Fourth, we <sup>fi</sup>nd that even if advanced targeting technologies can enable the entrant to also advertise to mobile buyers, the entrant may choose not to do so in order to avoid triggering the incumbent’s competitive response. Finally, we <sup>fi</sup>nd that the presence of network effects is likely to decrease the entrant’s pro<sup>fi</sup>t. Our results offer managerial implications for platform <sup>fi</sup>rms and help understand their performance heterogeneity.

History: DJ Wu, Senior Editor; Hong Xu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1010.

Keywords: network interconnectivity platform competition market entry

## 1. Introduction

Digitalization has led to the emergence of numerous platforms in our economy today (Rochet and Tirole 2003, Iansiti and Levien 2004, Parker and Van Alstyne 2005). Examples of popular platforms include Uber in the transportation industry, Airbnb in the accommodation industry, Craigslist in the classi<sup>fi</sup>eds market, and Groupon in the local daily deals market. A growing body of literature on information systems attempts to understand the optimal strategies required for digital platforms to scale and compete. Scholars have examined a variety of issues, including optimal pricing (e.g., Parker and Van Alstyne 2005), interactions between competing platforms (e.g., Koh and Fichman 2014, Niculescu et al. 2018, Zhang et al. 2018), optimal business models (e.g., Chen et al. 2016, Parker et al. 2017, Tian et al. 2018), strategies to motivate third-party providers (e.g., Huang et al. 2019, Kuang et al. 2019), matching ef<sup>fi</sup>ciency between buyers and sellers (e.g., Hong and Pavlou 2017, Xu 2018), platforms’ investment decisions (e.g., Anderson et al. 2014), managing multigenerational platforms (e.g., Hann et al. 2016), and contractual relationships or tensions between platform owners and third-party providers (e.g., Huang et al. 2013, Hao et al. 2017, Li and Agarwal 2017).

Our study adds to this literature by examining how network characteristics affect the strategies and performance of competing platforms. All platforms exhibit two-sidedness in that they facilitate matching and transactions between consumers and service providers in their markets, but the interconnectivity of their businesses—which measures the degree to which consumers in one market purchase services from service providers in a different market—varies considerably across industries. For example, the network structure of Upwork, an online marketplace that connects millions of businesses with freelancers around the globe, exhibits high interconnectivities among different markets. In contrast, Uber’s network consists of local network clusters with some interconnectivity among them: riders transact with drivers in their own city and, except for frequent travelers, they care mostly about the local availability of Uber drivers. We observe similar local network clusters with some interconnectivity in group buying platforms such as Groupon, classi<sup>fi</sup>eds sites such as Craigslist, food delivery platforms such as Grubhub, restaurantreservation platforms such as OpenTable, and marketplaces that match freelance labor with local demand such as TaskRabbit, Instacart, and Rover.

The network interconnectivity of a platform market has important implications for the pro<sup>fi</sup>tability and defensibility of incumbent platforms. When the network is strongly interconnected, it is dif<sup>fi</sup>cult for a new entrant to compete, particularly when consumers in one local market mostly purchase services from other markets. A platform that enters one local market, for example, would waste a signi<sup>fi</sup>cant amount of marketing resources to build awareness among local consumers and service providers without generating a large number of transactions. Therefore, for a new platform, entry into highly interconnected markets is costly. In contrast, when consumers and service providers mostly transact within their local clusters, it is relatively easy for a new platform to enter, as it can specialize in one local cluster and build awareness from there. In the ride-sharing industry, many entrants have challenged market leaders in local markets. Fasten entered the Boston market in 2015 to compete with Uber and Lyft with a much smaller budget. In New York City, Juno and Via have been competing with Uber and Lyft for years, and Myle was launched recently. Uber also faced a wave of rivals in London, including Estonia’s Bolt, France’s Kapten, Israel’s Gett, and India’s Ola. Didi, the largest ridesharing company in China, constantly faced new entrants in multiple cities.

In this paper, we adopt a game-theoretical approach to examine how network interconnectivity affects competitive interactions between an incumbent platform and an entrant platform. The incumbent platform has an installed base of buyers and service providers in multiple local markets; the entrant is interested in entering one of these markets. To capture interconnectivity between local markets, we assume that some buyers are mobile: they travel between markets, purchasing services in each. In the <sup>fi</sup>rst stage, the entrant invests money to build brand awareness in one of these markets. In the second stage, the incumbent and the entrant set prices for buyers and wages for service providers in that market. In the third stage, buyers and service providers in that market choose one platform on which to conduct transactions.

Our model yields several interesting results. First, even if the entrant can advertise at no cost, it still may not want to make every user in a local market aware of its service, as doing so may trigger a competitive response from the incumbent. Second, having more mobile buyers, which increases interconnectivity between markets, can reduce the incumbent’s incentive to <sup>fi</sup>ght and, thus, increase the entrant’s incentive to expand. Third, stronger interconnectivity across markets may or may not make the incumbent more defensible. When advertising is not costly and mobile buyers consume in both their local markets and the markets they visit, a large number of mobile buyers (i.e., great interconnectivity) will increase the entrant’s pro<sup>fi</sup>tability, thereby making it dif<sup>fi</sup>cult for the incumbent to deter entry. This result is somewhat surprising: great interconnectivity is supposed to provide the entrant with disadvantage because it increases the size of the incumbent’s potential market while retaining the size of the entrant’s potential market. When advertising cost is at an intermediate level, the entrant prefers a market with moderate interconnectivity between markets. When advertising is costly or mobile buyers consume only in the markets they travel to, a large number of mobile buyers will help the incumbent deter entry. Fourth, we <sup>fi</sup>nd that even if advanced targeting technologies can enable the entrant to also advertise to mobile buyers, the entrant may choose not to do so to avoid triggering the incumbent’s competitive response. Finally, we <sup>fi</sup>nd evidence that the presence of network effects is likely to decrease the entrant’s pro<sup>fi</sup>t.

In the literature on platform strategies, our paper is closely related to the literature examining entry into platform markets. Studies have identi<sup>fi</sup>ed a number of factors that in<sup>fl</sup>uence the success or failure of entrants in platform markets, such as the strength of network effects (e.g., Zhu and Iansiti 2012, Niculescu et al. 2018), platform quality (e.g., Liebowitz 2002, Tellis et al. 2009), multihoming (e.g., Cennamo and Santalo 2013, Koh and Fichman 2014, Anderson et al. 2019), and exclusivity (e.g., Corts and Lederman 2009). All these studies assume a strongly interconnected network. As indicated in Afuah (2013), this assumption does not re<sup>fl</sup>ect the actual networks in most industries. Our study extends this literature by examining how network interconnectivity affects the strategies and performance of incumbents and entrants.

Broadly, our paper is related to competitive interactions between incumbents and entrants. Theoretical models in the literature focus on incumbent strategies such as capacity investment to deter or accommodate entry (e.g., Fudenberg and Tirole 1984, Tirole 1988). Empirical studies often <sup>fi</sup>nd that incumbent reactions to entrants are selective (e.g., Geroski 1995): whereas some incumbents choose to react to entrants aggressively, others do not appear to respond to entry. Studies have also shown that this variation in responses often depends on entrant characteristics, such as scale (e.g., Debruyne et al. 2002, Karakaya and Yannopoulos 2011). Our model <sup>fi</sup>nds support for these empirical results. Chen and Guo (2014) document a similar result regarding an entrant refraining from overadvertising to avoid competitive response from a competitor but in a very different setting. In their setting, a third-party seller sells the same product as a retail platform and the seller needs to decide how much to advertise through other channels, such as search engines and social media. Our paper differs from these studies by examining how network interconnectivity changes the incumbent’s incentives to react, the entrant’s incentives to advertise, and the entrant’s pro<sup>fi</sup>t. We show that buyers’ consumption behavior matters: when mobile buyers consume in local markets, greater network interconnectivity sometimes increases entrant pro<sup>fi</sup>ts; however, when they do not, greater network interconnectivity reduces entrant pro<sup>fi</sup>ts.

Our paper is also related to studies that examine how network structures affect product diffusion (e.g., Abrahamson and Rosenkopf 1997, Suarez 2005, Lee et al. 2006, Sundararajan 2007, Tucker 2008). These studies typically focus on social networks, like instant messaging platforms, and examine questions related to issues such as seeding within these networks (e.g., Galeotti and Goyal 2009, Manshadi et al. 2020), pricing policies to facilitate product diffusion (e.g., Campbell 2013, Leduc et al. 2017), network formation processes and how local network clustering leads to local bias (e.g., Lee et al. 2016), prediction accuracy (e.g., Qiu et al. 2014), and market segmentation (e.g., Banerji and Dutta 2009). These networks have more complicated connections because they depend on individuals’ own social networks and, consequently, these studies rely on simulations or descriptive results. We adopt a different perspective to focus on how interconnectivity between local markets affects market entry and derive closed-form solutions.

The remainder of this paper is organized as follows. In Section 2, we introduce the model and analyze the competitive interactions between an incumbent and an entrant. In Section 3, we examine extensions to our main models. In Section 4, we conclude by discussing the implications of our results and potential future research.

## 2. The Model

## 2.1. Model Setup

Assume that there are multiple local markets each with N buyers who are currently using the incumbent’s platform (denoted by I) for transactions. A fraction of buyers in each market are mobile—r percent of them travel between markets. Assume the movement is random, so that in equilibrium, in each market, rN buyers visit other markets and rN additional buyers come from other markets to make purchases. Hence, r measures the interconnectivity between these markets. Each mobile buyer places one order for the service in his local market and another order when he travels. For example, riders use ride-sharing services in their local markets; when they travel, they use ridesharing services in other markets.<sup>1</sup> Each service provider ful<sup>fi</sup>lls one order at most. To accommodate these mobile buyers, each market has 1  r N service providers. Table 1 provides a summary of the notation used in the main model.

Before an entrant (denoted by E) enters one of these markets, the incumbent serves the market as a monopoly and all the users (i.e., both service providers and buyers) are aware of the incumbent.<sup>2</sup> Neither the buyers nor the service providers are aware of the entrant, but the entrant can advertise to build awareness.

The game proceeds as follows, as depicted in Figure 1. In the <sup>fi</sup>rst stage, the entrant invests to build brand awareness among users in the local market. Advertising is costly, and it costs the entrant L n to reach n potential users. The entrant decides on θ, a fraction of the potential users reached through advertising.<sup>3</sup> Because we have N buyers and 1 r N service providers, $n = \theta ( 2 N$ $+ ~ r N )$ . Following the literature (Thompson and Teng 1984, Tirole 1988, Esteves and Resende 2016, Jiang and Srinivasan 2016), we assume the advertising cost is a (weakly) increasing and convex function of n: $L ^ { ' } ( n ) \geq 0$ and $L ^ { ' \prime } ( n ) \geq 0$ . Note that even with digital technologies, it remains costly to build awareness. While certain platforms may be able to attract their <sup>fi</sup>rst tranche of customers relatively inexpensively, through word-ofmouth or other low-cost strategies, the cost typically begins escalating when the platform begins to look for new and somewhat different customers through search advertising, referral fees, and other marketing strategies (see, e.g., Dennis 2017). Consequently, many platforms exit the market after burning too much money on customer acquisition. In our model, we allow advertising cost to vary and examine its implications on platform strategies and performance. In the main model, we also assume that the entrant is not able to advertise to mobile buyers. We relax this assumption in an extension.

In the second stage, the incumbent sets the price to each buyer, denoted by $p _ { I } ,$ and the wage to each service provider, denoted by $w _ { I } ,$ in the local market. The entrant also sets the price for the service buyers, denoted by $p _ { E } ,$ and the wage for the service providers, denoted by w . Here, the subscript denotes the platform (I for incumbent and E for entrant). For example, Instacart, decides the prices for users and the wages for shoppers. Uber decides the rates for riders and the commissions it takes before passing on the revenue from riders to drivers, which effectively determines the wages for drivers. Consistent with the practice, we allow <sup>fi</sup>rms to set different prices and wages in different markets, but they do not price discriminate based on whether a buyer is local or mobile within a market. We denote each buyer’s willingness to pay for the service as v. Furthermore, we normalize the value of outside options to zero and the service providers’ marginal cost to zero.<sup>4</sup> Hence, without the entrant, as a monopoly, the incumbent will choose $p _ { I } = v$ and $w _ { I } = 0$

Table 1. Notation in the Main Model

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>N</td><td>Total number of local buyers</td></tr><tr><td>r</td><td>Proportion of buyers who are mobile and travel between markets,  $r \in [0,1]$ </td></tr><tr><td>n</td><td>Number of buyers and service providers (users) who are exposed to the entrant&#x27;s advertising</td></tr><tr><td>L(n)</td><td>Advertising cost for the entrant for reaching n buyers and service providers</td></tr><tr><td>k</td><td>Advertising cost parameter</td></tr><tr><td> $\theta$ </td><td>Proportion of users that the entrant targets for advertisement,  $\theta \in [0,1]$ </td></tr><tr><td> $\theta^{*}$ </td><td>Optimal proportion of potential users that the entrant targets for advertisement,  $\theta^{*} \in [0,1]$ </td></tr><tr><td>v</td><td>Buyer&#x27;s willingness to pay for the service</td></tr><tr><td>m</td><td>Maximum switching cost</td></tr><tr><td> $a_{i}$ </td><td>Switching cost for buyer i to adopt the entrant&#x27;s platform,  $a_{i} \sim Uni(0,m)$ </td></tr><tr><td> $c_{j}$ </td><td>Switching cost for service-provider j to adopt the entrant&#x27;s platform,  $c_{j} \sim Uni(0,m)$ </td></tr><tr><td> $a^{*}$ </td><td>The threshold at which buyers with lower switching cost will adopt the entrant&#x27;s platform.</td></tr><tr><td> $c^{*}$ </td><td>The threshold at which service providers with lower switching cost will adopt the entrant&#x27;s platform.</td></tr><tr><td> $N_{l}^{B}$ </td><td>Number of buyers who use platform l ∈ {I,E}</td></tr><tr><td> $N_{l}^{S}$ </td><td>Number of service providers who use platform l ∈ {I,E}</td></tr><tr><td> $U_{l,i}^{B}$ </td><td>Utility of buyer i who uses platform l ∈ {I,E}</td></tr><tr><td> $U_{lj}^{S}$ </td><td>Utility of service provider j who uses platform l ∈ {I,E}</td></tr><tr><td> $p_{l}$ </td><td>Price for buyers that is set by platform l ∈ {I,E}</td></tr><tr><td> $w_{l}$ </td><td>Wage for service providers that is set by platform l ∈ {I,E}</td></tr><tr><td> $\pi_{l}$ </td><td>Profit for platform l ∈ {I,E}</td></tr></table>

In the third stage, the rN mobile buyers from other markets arrive. Buyers and service providers choose one platform on which to conduct transactions. Mobile buyers are not exposed to the entrant’s advertisements and are, therefore, only aware of the incumbent. Hence, the entrant and the incumbent compete for buyers and service providers from the local market, but the mobile buyers will only use the incumbent platform.

The (1 θ) portion of users in the local market is only aware of the incumbent and will buy or provide the service on the incumbent platform as long as they receive a nonnegative utility from the incumbent. Speci<sup>fi</sup>cally, a buyer will buy the service as long as $p _ { I } \leq v _ { \cdot }$ , and a service provider will provide the service as long as $w _ { I } \geq 0$ Because $p _ { I } \leq v$ and $w _ { I } \geq 0$ always hold, these users will always use the incumbent’s platform.

The θ portion of users in the local market becomes aware of both the incumbent and the entrant and will remain with the incumbent’s platform unless the entrant provides a higher utility. If a user elects to switch to the entrant’s platform, there is a switching cost that varies across users. We denote this cost for a service provider i by $c _ { i } ,$ and for a buyer j by $a _ { j } .$ Similar to Ruiz-Aliseda $( 2 0 1 6 )$ , we assume that both $c _ { i }$ and $a _ { j }$ follow a uniform distribution between zero and $m ,$ where m captures the dif<sup>fi</sup>culty in switching to a new service in the market. To be consistent with real world scenarios, we assume that m is suf<sup>fi</sup>ciently large (i.e., there are some users whose switching cost is suf<sup>fi</sup>- ciently large) so that, in equilibrium, the entrant will not take away the entire segment of users who are aware of both platforms.<sup>5</sup>

Among the θ portion of service providers, a service provider, i, will choose the entrant if the utility from using the entrant’s platform $( U _ { E i } ^ { S } = w _ { E } - c _ { i } )$ is greater than the utility from using the incumbent’s platform $( U _ { I i } ^ { S } = w _ { I } )$ . Here, the subscript again denotes the platform (I for incumbent and E for entrant) and the superscript denotes the user (S for service provider and B for buyer). The solution to the equation $U _ { E i } ^ { S } = U _ { I i } ^ { S }$ is $c ^ { * } = w _ { E } - w _ { I }$ , describing the switching cost of the indifferent service provider. Thus, service providers with $c _ { i } < c ^ { * }$ will choose the entrant and those with $c _ { i } \geq c ^ { * }$ will choose the incumbent. Let $N _ { I } ^ { S }$ denote the number of service providers selecting the incumbent and $N _ { E } ^ { S }$ denote the number of service providers selecting the entrant. Then, we have the following two equations:

$$
N _ {I} ^ {S} = \bigg (1 - \frac {c ^ {*}}{m} \theta \bigg) (1 + r) N,\tag{1}
$$

Figure 1. Sequence of the Game

<table><tr><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td></tr><tr><td>The entrant invests to build brand awareness in the local market.</td><td>The incumbent and the entrant set prices to buyers and wages to service providers simultaneously.</td><td>Mobile buyers arrive. Buyers and service providers choose one platform on which to conduct transactions.</td></tr></table>

$$
N _ {E} ^ {S} = \frac {c ^ {*}}{m} \theta (1 + r) N.\tag{2}
$$

Similarly, a buyer, $j ,$ will choose the entrant if the utility from using the entrant’s platform $( U _ { E j } ^ { B } = v - p _ { E } - a _ { j } )$ is greater than the utility from using the incumbent’s platform $( U _ { I j } ^ { B } = v - p _ { I } )$ . The solution to the equation $U _ { E j } ^ { B } = U _ { I j } ^ { B }$ is $a ^ { * } = p _ { I } - p _ { E }$ . Thus, buyers with $a _ { j } < a ^ { * }$ will choose the entrant and those with $a _ { j } \geq a ^ { * }$ will choose the incumbent. Let $N _ { I } ^ { B }$ denote the number of service buyers selecting the incumbent and $N _ { E } ^ { B }$ denote the number of service buyers selecting the entrant. We obtain the following two equations:

$$
N _ {I} ^ {B} = \left(1 - \frac {a ^ {*}}{m} \theta + r\right) N,\tag{3}
$$

$$
N _ {E} ^ {B} = \frac {a ^ {*}}{m} \theta N.\tag{4}
$$

We can then derive the incumbent’s pro<sup>fi</sup>t, $\pi _ { I } ,$ and the entrant’s pro<sup>fi</sup>t, $\pi _ { E } ,$ , from the local market as follows:

$$
\pi_ {I} = \min \left(N _ {I} ^ {S}, N _ {I} ^ {B}\right) (p _ {I} - w _ {I}),\tag{5}
$$

$$
\pi_ {E} = \min \Big (N _ {E} ^ {S}, N _ {E} ^ {B} \Big) (p _ {E} - w _ {E}) - L \big (\theta (2 N + r N) \big).\tag{6}
$$

It is possible that under some prices and wages of the two platforms, the number of buyers is not the same as the number of service providers. In such cases, either some buyers’ orders are not ful<sup>fi</sup>lled, or some service providers will not serve any buyers and hence earn no income.

## 2.2. Equilibrium Analysis

We use backward induction to derive the equilibrium. Speci<sup>fi</sup>cally, we <sup>fi</sup>rst derive each platform’s optimal price and pro<sup>fi</sup>t given the entrant’s advertising decision and then solve for the entrant’s optimal advertising decision in the <sup>fi</sup>rst stage.

To derive each platform’s optimal price given the entrant’s advertising decision, we recognize that it is often dif<sup>fi</sup>cult to derive closed-form equilibrium solutions when we allow two competing platforms to set prices on both sides, especially when the platforms are heterogeneous. Prior studies have often had to make simplifying assumptions, such as a <sup>fi</sup>xed price (or royalty rate) on one-side of the market, symmetric pricing, or one platform being an open source platform and, thus, free $( \mathrm { e . g . }$ , Rochet and Tirole 2003, Economides and Katsamakas 2006, Casadesus-Masanell and Halaburda 2014, Adner et al. 2020). In this study, we take advantage of a market clearing condition to derive the optimal prices and wages for the two competing platforms. Speci<sup>fi</sup>- cally, we prove that, in equilibrium, the incumbent and the entrant will always choose their prices and wages so that the number of service providers using a platform equals the number of buyers using the same platform: $N _ { I } ^ { S } = N _ { I } ^ { B }$ and $N _ { E } ^ { S } = N _ { E } ^ { B }$ . Lemma 1 states this result (proofs of all lemmas and propositions for the main model are provided in the appendix).

Lemma 1. The incumbent and the entrant will set their prices and wages so that the number of service providers using a platform equals the number of buyers using the same platform.

The intuition for Lemma 1 is that if the numbers on the two sides are not balanced, a <sup>fi</sup>rm can adjust its price or wage to get rid of excess supply or demand to increase its pro<sup>fi</sup>tability. The lemma suggests that $a ^ { * } = ( 1 + r ) c ^ { * }$ . Hence, $( p _ { I } - p _ { E } ) = ( 1 + r ) ( w _ { E } - w _ { I } )$ . Thus, we can rewrite the pro<sup>fi</sup>t functions as follows:

$$
\pi_ {I} = \left(1 - \frac {p _ {I} - p _ {E}}{m} \theta + r\right) N \left(p _ {I} + \frac {p _ {I} - p _ {E}}{1 + r} - w _ {E}\right).\tag{7}
$$

$$
\pi_ {E} = \frac {p _ {I} - p _ {E}}{m} \theta N \left(p _ {E} - \frac {p _ {I} - p _ {E}}{1 + r} - w _ {I}\right) - L \left(\theta (2 N + r N)\right).\tag{8}
$$

We can then derive each platform’s optimal price and pro<sup>fi</sup>t, given the entrant’s advertising decision, as shown in Proposition 1.

Proposition 1. Given the entrant’s choice of advertising intensity θ, the optimal prices, number of buyers and service providers, and platform profits can be determined as follows:

$$
\mathrm{i.} \quad I f \quad 0 \leq \theta \leq m i n \left(\frac {2 m (2 + r)}{3 v}, 1\right), \quad t h e n \quad p _ {I} ^ {*} = v, \quad w _ {I} ^ {*} = 0,
$$

$$
p _ {E} ^ {*} = \frac {(3 + r) v}{2 (2 + r)}, w _ {E} ^ {*} = \frac {v}{2 (2 + r)}, N _ {I} ^ {B *} = N _ {I} ^ {S *} = \frac {N (1 + r)}{2} \Big (2 - \frac {\theta v}{m (2 + r)} \Big),
$$

$$
N _ {E} ^ {B *} = N _ {E} ^ {S *} = \frac {N (1 + r) \theta v}{2 m (2 + r)}, \pi_ {I} ^ {*} (\theta) = \frac {N (1 + r) v}{2} \Big (2 - \frac {\theta v}{m (2 + r)} \Big), a n d
$$

$$
\pi_ {E} ^ {*} (\theta) = \frac {N (1 + r) \theta v ^ {2}}{4 m (2 + r)} - L \Bigl (\theta (2 N + r N) \Bigr).
$$

ii. If min $\textstyle \left( { \frac { 2 m ( 2 + r ) } { 3 v } } , 1 \right) < \theta \leq 1$ , then $\begin{array} { r } { p _ { I } ^ { * } = \frac { 2 ( 2 + r ) m } { 3 \theta } , w _ { I } ^ { * } = 0 . } \end{array}$ $\begin{array} { r } { p _ { E } ^ { * } = \frac { ( 3 + r ) m } { 3 \theta } , w _ { E } ^ { * } = \frac { m } { 3 \theta } , \ N _ { I } ^ { B ^ { * } } = N _ { I } ^ { S ^ { * } } = \frac { 2 N ( 1 + r ) } { 3 } , \ N _ { E } ^ { B ^ { * } } = N _ { E } ^ { S ^ { * } } = } \end{array}$ $\begin{array} { r } { \frac { N ( 1 + r ) } { 3 } , \pi _ { I } ^ { * } ( \theta ) = \frac { 4 N m ( 1 + r ) ( 2 + r ) } { 9 \theta } . } \end{array}$ , and $\begin{array} { r } { \pi _ { E } ^ { * } ( \theta ) = \frac { N m ( 1 + r ) ( 2 + r ) } { 9 \theta } } \end{array}$ $- L \Bigl ( \theta ( 2 N + r N ) \Bigr )$

When θ is smaller than a certain threshold $\begin{array} { r } { \left( m i n \left( \frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v } , 1 \right) \right) } \end{array}$ , we <sup>fi</sup>nd that the incumbent platform chooses not to respond to the entrant. It continues to charge the monopoly price, v, and offer the monopoly wage, zero, although its pro<sup>fi</sup>t does decrease as $\theta$ increases because it loses market share to the entrant. The entrant platform incentivizes some buyers and service providers to switch by charging a lower price and offering a higher wage.

The threshold for θ (weakly) increases with r because mobile buyers are only aware of the incumbent platform $( \mathrm { i . e . } ,$ , the incumbent platform has monopoly power over them) and their existence reduces the incumbent’s incentive to respond to the entrant. It is thus not surprising that the entrant can take advantage of this lack of incentive and increase its advertising intensity. The number of transactions hosted on the incumbent platform increases with r because of mobile buyers from other markets, even though the incumbent loses more transactions from local buyers to the entrant when r increases. The incumbent platform’s pro<sup>fi</sup>t increases with r because of the increase in transactions at the same monopoly price it charges. The number of transactions the entrant serves also increases with r because it can advertise more aggressively without triggering a competitive response from the incumbent. The entrant’s pro<sup>fi</sup>t increases with r without taking the advertising cost into account. If advertising cost increases signi<sup>fi</sup>cantly with $r ,$ the entrant’s pro<sup>fi</sup>t may decrease with $r ,$ a scenario which will be examined later.

When θ is larger than the threshold, however, the entrant platform has the potential to steal a large market share from the incumbent. The incumbent platform chooses to respond by lowering its price to buyers. The entrant platform thus lowers its price to buyers as well. Note that the wages offered by the entrant in this case decrease with θ. This is because even though advertising reaches many service providers, there is no demand for all the service providers because of the competitive response from the incumbent on the buyer side, thereby allowing the entrant to offer lower wages.

We again <sup>fi</sup>nd that because mobile buyers reduce the incumbent’s incentive to <sup>fi</sup>ght, both the incumbent and the entrant can charge (weakly) higher prices to buyers while maintaining the same wages as r increases. They both have more transactions when r increases. The incumbent’s pro<sup>fi</sup>t increases with $r ,$ whereas the entrant’s pro<sup>fi</sup>t increases with r when its advertising cost does not increase too much with r.

Note that when θ is larger than the threshold, as θ increases, the pro<sup>fi</sup>ts of both platforms decrease because of intense competition even without considering advertising cost. Thus, we expect the entrant’s optimal choice of $\theta$ to be no more than the threshold $\scriptstyle \left( m i n \left( { \frac { 2 m ( 2 \ + \ r ) } { 3 v } } , 1 \right) \right)$ ; that is, it is in the best interest of the entrant not to trigger the incumbent’s competitive response.

Corollary 1. The entrant’s optimal choice of advertising intensity θ always satisfies $\begin{array} { r } { \theta \leq m i n \left( \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } , \ 1 \right) } \end{array}$

The exact optimal level of θ for the entrant depends on the cost of advertising, $L ( n ) = L { \Big ( } \theta ( 2 N + r N ) { \Big ) }$ . Following the literature (e.g., Thompson and Teng 1984, Tirole 1988, Esteves and Resende 2016, Jiang and Srinivasan 2016), we assume a quadratic cost function, $L ( n ) = \ k n ^ { 2 } ,$ where $k \geq 0$ : A large k suggests that advertising is costly, whereas a small k suggests that it is inexpensive.<sup>6</sup>

Figure 2 illustrates how the entrant’s pro<sup>fi</sup>t changes with the choice of θ for different values of k. We notice that for a given level of $k ,$ the entrant’s pro<sup>fi</sup>t increases and then decreases with θ. Even if advertising has no cost $( \mathrm { i . e . , } k = 0 )$ , there is an optimal advertising level for the entrant. As k increases $( \mathrm { i . e . , }$ , advertising becomes more expensive), the optimal advertising intensity, $\theta ^ { * } ,$ decreases. However, the incumbent’s pro<sup>fi</sup>t always decreases with $\theta$ and is independent of k. The following proposition formalizes the relationship between the optimal advertising intensity, $\theta ^ { * }$ , and the value of k.

$$
\theta^ {*}
$$

Proposition 2. The optimal advertising intensity, θ<sup>∗</sup>, depends on the value $o f k \colon$ i. $\begin{array} { r } { I f k \ge m a x \left( \frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } } , \frac { ( 1 + r ) v ^ { 2 } } { 8 m N ( 2 + r ) ^ { 3 } } \right) , } \end{array}$ , then $\begin{array} { r } { \theta ^ { * } = \frac { ( 1 + r ) v ^ { 2 } } { 8 ( 2 + r ) ^ { 3 } k N m } , } \end{array}$ which decreases with r. The entrant’s profit $\begin{array} { r } { i s \frac { ( 1 + r ) ^ { 2 } v ^ { 4 } } { 6 4 k m ^ { 2 } \left( 2 + r \right) ^ { 4 } } } \end{array}$ and the incumbent’s profit is $\begin{array} { r } { \frac { N ( 1 + r ) v } { 2 } \left( 2 - \frac { ( 1 + r ) v ^ { 3 } } { 8 k N m ^ { 2 } \left( 2 + r \right) ^ { 4 } } \right) } \end{array}$ ii. If $\begin{array} { r } { 0 \leq k < m a x \left( \frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N \left( 2 + r \right) ^ { 4 } } , \frac { ( 1 + r ) v ^ { 2 } } { 8 m N \left( 2 + r \right) ^ { 3 } } \right) , } \end{array}$ , then $\theta ^ { * } = m i n$ $\begin{array} { r } { \left( \frac { 2 m ( 2 + r ) } { 3 v } , 1 \right) . } \end{array}$ , which weakly increases r. When $\frac { 2 m ( 2 + r ) } { 3 v }$ $< 1$ , the entrant’s profit is $\begin{array} { r } { \frac { N ( 1 + r ) v } { 6 } - \frac { 4 k N ^ { 2 } m ^ { 2 } ( 2 + r ) ^ { 4 } } { 9 v ^ { 2 } } } \end{array}$ and the incumbent’s profit is $\textstyle { \frac { 2 N v ( 1 + r ) } { 3 } } ,$ . When $\begin{array} { r } { \frac { 2 m ( 2 + r ) } { 3 v } \geq 1 } \end{array}$ , the $e n \mathrm { - }$ trant’s profit is $\frac { N ( 1 + r ) v ^ { 2 } - 4 k N ^ { 2 } m { ( 2 + r ) } ^ { 3 } } { 4 m ( 2 + r ) }$ and the incumbent’s profit $\begin{array} { r } { i s \frac { N ( 1 + r ) v } { 2 } \Big ( 2 - \frac { v } { m ( 2 + r ) } \Big ) } \end{array}$

We have two cases. When k is large, advertising is costly. In this case, the optimal advertising intensity is $\begin{array} { r } { \theta ^ { * } \leq m i n \Big ( \frac { 2 m ( 2 \ + \ r ) } { 3 v } , \ 1 \Big ) } \end{array}$ : The entrant and the incumbent have no strategic interactions with each other and the entrant’s optimal advertising intensity is determined by the marginal bene<sup>fi</sup>ts and marginal cost from reaching another user. Consequently, the entrant’s equilibrium pro<sup>fi</sup>t is independent of the market size,

Figure 2. (Color online) Firms’ Pro<sup>fi</sup>ts vs. Advertising Intensity θ  
![](/api/attachments/457KUVF4/fulltext/images/e9cf4136fbdf84b97e0cd15fc0def8c8660a9564d73a24307609fbcb48e83887.jpg)  
Note. The vertical lines indicate the optimal θ for each scenario.

N. This result also highlights the impact of network interconnectivity, independent of the market size.

When k is small, advertising is inexpensive, and the entrant platform thus has an incentive to increase advertising intensity θ. The entrant’s pro<sup>fi</sup>t increases with θ until $\begin{array} { r } { \theta = m i n \left( \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } , 1 \right) } \end{array}$ : When $\begin{array} { r } { \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } \geq 1 } \end{array}$ the entrant will advertise to everyone in the market. Otherwise, the entrant’s pro<sup>fi</sup>t <sup>fi</sup>rst increases as $\theta$ increases up to $\frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v }$ and then, because of the competitive response from the incumbent discussed in Corollary 1, decreases with θ afterward. Thus, the entrant will choose $\theta ^ { * } = \frac { 2 m ( 2 { \it \Delta \phi } + { \it \Delta \phi } r ) } { 3 v }$ . Note that the entrant’s optimal choice of $\theta$ is independent of market size N but increases with $r ,$ which again highlights that market size and network interconnectivity affect equilibrium outcomes differently.

The discussion above leads to the following corollary.

Corollary 2. Even if the advertising cost is zero $( i . e . , L ( n )$ 0 or $k = 0 )$ , the entrant will not necessarily advertise to the entire market but instead choose the optimal advertising intensity $\theta ^ { * } = \frac { 2 m ( 2 { \it \Delta \phi } + { \it \Delta \phi } r ) } { 3 v }$ when $\frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } < \dot { 1 }$

We then examine how the fraction of mobile buyers, $r ,$ affects the optimal θ and the platforms’ pro<sup>fi</sup>ts in the two cases in Proposition 2. Figure 3 illustrates the relationships under different values of k. When k is large (in Proposition 2i), advertising is costly. As r increases, the number of service providers, $( 1 + r ) N ,$ , increases in the market, but the number of buyers accessible to the entrant remains the same. Thus, the likelihood that advertising is wasted on some service providers without matched buyers also increases. With a large k, it is optimal for the entrant to reduce $\theta ^ { * }$ to reduce its advertising cost, $L \Bigl ( \theta ^ { * } \bigl ( 2 N + r N \bigr ) \Bigr )$ , even if a large r reduces the incumbent’s incentive to respond. This explains the declining curve in Figure $3 ( \mathrm { a } )$ for a large k $\mathbf { \bar { ( e . g . , } } k = 0 . 0 0 0 4 )$ . Because the entrant advertises to fewer buyers, the entrant’s pro<sup>fi</sup>t also decreases with $r ,$ as depicted in Figure 3(b) for $k = 0 . 0 0 0 4$

![](/api/attachments/457KUVF4/fulltext/images/0e9cd810c6495be4ea7e9a0c050ddd437739d8b1b4a2b610cdfddcf58cd5eb03.jpg)

In contrast, when k is small (in Proposition 2ii), $\theta ^ { * }$ (weakly) increases with r. This is because when advertising is inexpensive, the advertising wasted on unmatched service providers becomes a less signi<sup>fi</sup>cant issue and the entrant wants to take advantage of the incumbent’s disincentive to respond instead. Thus, we observe an increasing curve of $\theta ^ { * }$ in Figure 3(a) for a small k (e.g., $k = 0 )$ . The impact of r on the entrant’s pro<sup>fi</sup>t is also positive as long as $k$ is suf<sup>fi</sup>ciently small.<sup>7</sup> This result is consistent with Proposition 1, where we have shown that if the advertising cost is small for the entrant, the entrant’s pro<sup>fi</sup>t will increase with r regardless of θ. When we use $k$ to capture the cost of advertising, as long as $k$ is suf<sup>fi</sup>ciently small (e.g., $k = 0$ in Figure 3(b)), the entrant’s pro<sup>fi</sup>t increases with r. The result shows that when the incumbent has more captive buyers and, therefore, less incentive to <sup>fi</sup>ght, the entrant could be more pro<sup>fi</sup>table when advertising is not costly.

Note that the threshold of k, $\Big ( m a x \left( \frac { 3 v ^ { 3 } } { 3 2 N m ^ { 2 } ( 2 \ + \ r ) ^ { 3 } } , \frac { v ^ { 2 } } { 8 m N ( 2 \ + \ r ) ^ { 3 } } \right) \Big ) .$

below which the entrant’s pro<sup>fi</sup>t increases with $r ,$ is a decreasing function of r. Therefore, an intermediate value of k may begin from below the threshold when r is small, but then exceed the threshold as r increases. This implies that the equilibrium may switch between the two cases (where k falls above or below the threshold) as r changes. This explains why we may observe a nonmonotonic relationship between the optimal advertising intensity (θ<sup>∗</sup>) and r and the same for the relationship between the entrant’s pro<sup>fi</sup>t and $r ,$ as shown by the case of k 0.0002 in Figure 3, (a) and (b).

Figure 3. (Color online) The Entrant’s Optimal Advertising Intensity and Firms’ Pro<sup>fi</sup>ts Under Different Values of r  
(a)  
![](/api/attachments/457KUVF4/fulltext/images/cfc3126c9a05a1ec8a04bf8af4c26350a21499001548495d4164bd44ad8064b2.jpg)

(b)  
![](/api/attachments/457KUVF4/fulltext/images/cb5401d0a20123f16c7d505df9aa6873d8088f2b88bbe8c08c98c020b914e577.jpg)

(c)  
![](/api/attachments/457KUVF4/fulltext/images/7d3ca48fabfe79a041ff7a4a450c25746358baae84103c3ca22e283a4754ad7a.jpg)

Regardless of the value of $k ,$ the incumbent’s pro<sup>fi</sup>t always increases with $r ,$ because it has more captive buyers when r is larger (as illustrated in Figure 3(c)).

Below we summarize the relationship between the entrant’s advertising intensity and the fraction of mobile buyers in Corollary 3 and the relationship between the platform pro<sup>fi</sup>t and the fraction of mobile buyers in Proposition 3.

Corollary 3. When k is small, as the fraction of mobile buyers, r, increases, the entrant has incentive to advertise more (higher θ<sup>∗</sup>) until it reaches the entire market. Conversely, when k is large, as r increases, the entrant has incentive to reduce advertising (lower θ<sup>∗</sup>). For intermediate values of k, as r increases from zero, the optimal $\boldsymbol { \theta } ^ { * }$ increases with r first and then decreases with r.

Proposition 3. The incumbent’s profit always increases with the fraction of mobile buyers, r. How the fraction of mobile buyers, r, affects the entrant’s profit depends on the value of k. When k is small, the entrant’s profit increases with r, and conversely, when k is large, the entrant’s profit decreases with r. For intermediate values of k, as r increases from zero, the entrant’s profit increases with r first and then decreases with r.

The results suggest that under certain circumstances (e.g., when advertising is cheap), network interconnectivity, which does not in<sup>fl</sup>uence the size of the entrant’s potential demand in a single market but is supposed to bene<sup>fi</sup>t the incumbent that operates in multiple interconnected markets, may, in fact, encourage the entrant to enter the market and increase entrant pro<sup>fi</sup>t. In this case, a higher network interconnectivity will make it even more dif<sup>fi</sup>cult for an incumbent to deter entry. These results have important managerial implications for platform owners to understand their competitiveness in markets with a given level of market interconnectivity for resource planning and marketing strategy design, and for policy makers to take into account the network interconnectivity when considering the anticompetitive issues in platform markets. These results also have important implications for the entrant regarding the choice of market to enter when the fraction of incoming mobile buyers varies across markets; we will examine this further in the next section.

## 3. Extensions<sup>8</sup>

## 3.1. Heterogeneous Markets

In our main analysis, we assume that all markets are homogenous. Consequently, the entrant could begin by entering any one of these markets. If these markets have different fractions of mobile buyers visiting from other markets, assuming the entrant only has the budget to enter one market only, which market should the entrant choose to enter?

Suppose there are H markets. Let $r _ { h }$ be the fraction of mobile buyers coming into market h $( h = 1 , 2 , \ \dots \ ,$ H). Hence, market h has N local buyers, $( 1 + r _ { h } ) N$ service providers, and $r _ { h } N$ incoming mobile buyers. We obtain the following proposition.

Proposition 4. When k is small, the entrant should choose the market with the highest fraction of mobile buyers from other markets, r, to enter; when k is large, the entrant should choose the market with the lowest fraction of mobile buyers from other markets, r, to enter. For an intermediate value of k, the entrant 10 may choose a market where r is also intermediate.

The result echoes Proposition 3, where we <sup>fi</sup>nd that the entrant’s pro<sup>fi</sup>t increases with r when k is small, decreases with r when k is large, and has a nonmonotonic relationship with r for an intermediate value of k. Whereas Proposition 3 focuses on how the entrant’s pro<sup>fi</sup>t changes when r in a local market increases, this proposition extends our <sup>fi</sup>nding to how the entrant should choose a market among the markets that vary in the fraction of incoming mobile buyers. The proposition suggests that when the fraction of visitors is high, the incumbent is less likely to <sup>fi</sup>ght the entrant. At the same time, however, a high fraction of visitors means that a large fraction of the entrant’s advertising expenditure will be wasted on unmatched service providers. Hence, the entrant will <sup>fi</sup>nd such a market attractive when advertising is not costly. For example, if Google wants to offer ride-sharing services because it already has a larger number of users from its current services and can build awareness at a low cost (k is small), Google should start offering these services in large cities with a large fraction of visitors. However, a new startup, for which advertising is rather costly, should target small cities with a small fraction of visitors in order to improve advertising ef<sup>fi</sup>ciency.

## 3.2. The Incumbent Does Not Own the Entire Market

In our main model, we also assume that the incumbent owns the entire market (i.e., all potential buyers and service providers are aware of the incumbent) before the entrant emerges. In reality, it is possible that not every user in the local market is aware of the incumbent. Thus, it is possible for the entrant to attract users who are not aware of the incumbent. We consider this possibility in this extension. Assume the incumbent’s market share before the entrant arrives is $s ,$ where $0 <$ $s < 1$ . We then have the following proposition.

Proposition 5. The results from our main model are qualitatively the same when $s \geq \ { \frac { m ( 2 \ + \ r ) } { 2 m \ + \ m r \ + \ v \ + \ r v } } . \ I f \ s <$ $\frac { m ( 2 { \mathrm { ~ + ~ } } r ) } { 2 m { \mathrm { ~ + ~ } } m r { \mathrm { ~ + ~ } } v { \mathrm { ~ + ~ } } r v }$ , both platforms charge buyers $p _ { I } ^ { * } = p _ { E } ^ { * } = v$ and offer service providers $w _ { I } ^ { * } = \ w _ { E } ^ { * } = 0$

The results from the main model remain qualitatively the same as long as s is suf<sup>fi</sup>ciently large. But when s is below a certain threshold, the results differ from our main results. When the incumbent has a small share of the market, the entrant and the incumbent can effectively avoid direct competition by targeting different segments of that market. Hence, both will charge monopoly prices and offer monopoly wages, and no buyers and service providers will switch from the incumbent to the entrant.

## 3.3. Mobile Buyers Consume Only When They Travel

In our main model, mobile buyers purchase services in both their local markets and the markets they visit. This assumption <sup>fi</sup>ts with markets such as those in the ride-sharing industry, where riders hail cars in their own markets and also in other markets when they travel, or daily local deal markets, where consumers buy deals in their own markets and also in other markets when they travel. In this case, interconnectivity affects the size of the potential market for the incumbent but does not affect the size of the potential market for the entrant. Our main model thus enables us to examine the impact of market interconnectivity on the entrant independent of the market size effect. Interestingly, although the size of the potential market for the entrant is unchanged, its pro<sup>fi</sup>t may increase with the interconnectivity between markets. This possible pro<sup>fi</sup>t enhancement for the entrant, independent of the market size effect, is the most interesting result of our model and provides novel insights regarding the role of market interconnectivity in in<sup>fl</sup>uencing platform competition.

Although the assumption that mobile buyers purchase services in both their local markets and the markets they visit is consistent with the practice for many platforms, in this extension, we examine to what extent our results are affected by this assumption by looking at the scenario in which mobile buyers do not consume in their local markets. We obtain the following result under this assumption.

Proposition 6. The results from the main model are qualitatively the same when mobile buyers do not consume in their local markets, except that the entrant’s profit under the optimal θ always decreases with r.

Unlike in the main model, in this case, by assuming away local consumption, we keep the size of the potential market for the incumbent <sup>fi</sup>xed. The size of the potential market for the entrant, however, changes with interconnectivity: a larger fraction of mobile buyers will have fewer potential buyers for the entrant. The results suggest that the incumbent’s pro<sup>fi</sup>t always increases with $r ,$ irrespective of whether local consumption occurs. However, although the entrant can continue to take advantage of the incumbent’s disincentive to <sup>fi</sup>ght and advertise more aggressively, its demand decreases (i.e., the market size effect and interconnectivity effect take place jointly). Consequently, its pro<sup>fi</sup>t decreases with r. In the case of Airbnb, for example, travelers typically do not care about the number of hosts in their home cities; they care more about the number of hosts in the cities they wish to visit.<sup>11</sup> This result explains why it is more dif<sup>fi</sup>cult to challenge an incumbent platform like Airbnb for which local consumption occurs less frequently compared with one like Uber.

## 3.4. The Entrant Can Target Mobile Buyers

In the main model, we assume that the entrant is not able to advertise to mobile buyers. We make this assumption because mobile buyers often stay in the market they visit brie<sup>fl</sup>y. Even if the entrant is continuously advertising in that market, without suf<sup>fi</sup>cient exposure to its advertisement, a mobile buyer may not consider the entrant’s product. We now relax this assumption and assume that advanced targeting technologies can help the entrant identify mobile buyers and can advertise to them effectively. Let θ and $\theta _ { t }$ be the fractions of local and mobile users, respectively, that become aware of the entrant’s platform after the entrant’s advertising. The demand on the service provider side remains the same as in Equations (1) and (2). The demand on the buyer side becomes

$$
N _ {I} ^ {B} = \left(1 + r - \frac {a ^ {*}}{m} (\theta + \theta_ {t} r)\right) N,\tag{9}
$$

$$
N _ {E} ^ {B} = \frac {a ^ {*}}{m} (\theta + \theta_ {t} r) N.\tag{10}
$$

Note that local advertising and advertising to mobile buyers are different in that when advertising to local, the entrant advertises both to buyers and service providers, which helps balance demand and supply;

however, mobile users only include buyers and, thus, advertising targeted mobile buyers can target buyers only. Consequently, advertising to the two groups of users has different effects on the pricing strategies of the entrant and incumbent. In this case, we <sup>fi</sup>nd that the entrant may not want to advertise to the mobile buyers even if there is no cost of advertising, as summarized by the following proposition.

Proposition 7. Even if the cost of advertising is zero (i.e., $L ( n ) = 0 )$ , the entrant will not necessarily choose to advertise to mobile buyers even if it is able to, that $i s , \ \theta _ { t } { } ^ { * } = 0 \ i f$ $\begin{array} { r } { \frac { 2 m ( 2 + r ) } { 3 v } \leq 1 } \end{array}$

As we show in the main analysis, mobile buyers help deter the incumbent from <sup>fi</sup>ghting with the entrant. Hence, the entrant may not want to steal the mobile buyers from the incumbent even when it can target them and advertise to them at zero cost. The entrant is more likely to avoid advertising to the mobile segment when the value of these buyers to the incumbent is high (large v), the mobile segment is not large so the entrant does not lose a huge number of potential buyers (small r), and a small amount of advertising can steal a large number of mobile buyers away from the incumbent and thus trigger its response (small m). When the advertising cost for mobile buyers is higher than the cost for local users, the entrant will be even less likely to advertise to mobile buyers. The only situation in which the entrant will advertise to mobile buyers is when the entrant has advertised to all local buyers and has not triggered competitive responses from the incumbent, which is rarely observed in practice. Thus, Proposition 7 helps justify the assumption in our main model that mobile buyers are aware only of the incumbent.

## 3.5. The Presence of Network Effects

In our main model, we focus on matching between the buyers and service providers. Similar to other matching models $( \mathrm { e . g . } ,$ , Zhang et al. 2018), we do not model network effects. This approach enables us to separate the network-interconnectivity effect from the network effects, but network effects may have an impact on matching quality or speed. For example, in the case of ride-sharing services, a large number of drivers on a platform can reduce the wait time for riders. Similarly, a large number of riders reduces the idle time for drivers. In the accommodation market, a large number of hosts and travelers on a platform increase the likelihood that each traveler and each host is matched with a party close to his or her personal preference. To capture such bene<sup>fi</sup>ts, we add a utility component to capture the network effects in the buyers’ and service providers’ utility functions and allow this utility component to increase with the number of users on the other side of the same platform:

$$
U _ {I} ^ {B} = e N _ {I} ^ {S} + v - p _ {I},\tag{11}
$$

$$
U _ {E} ^ {B} = e N _ {E} ^ {S} + v - p _ {E} - a _ {i},\tag{12}
$$

$$
U _ {I} ^ {S} = e N _ {I} ^ {B} + w _ {I},\tag{13}
$$

$$
U _ {E} ^ {S} = e N _ {E} ^ {B} + w _ {E} - c _ {i}.\tag{14}
$$

Here, we use parameter $\textit { e } \ ( e \geq 0 )$ to capture the strength of network effects. We <sup>fi</sup>rst consider the case where e is small and both platform <sup>fi</sup>rms can coexist. To avoid multiple equilibria due to network effects, we assume e to be much smaller than the value of the transaction itself.<sup>12</sup> This assumption is reasonable because in such markets most bene<sup>fi</sup>ts to buyers or service providers come from the transaction itself. We <sup>fi</sup>nd our main results to be qualitatively unchanged, as summarized in the following proposition.

Proposition 8. The results from the main model are qualitatively the same in the presence of network effects when the strength of network effects is small.

We also examine how the strength of network effects affects the pro<sup>fi</sup>ts of both the entrant and incumbent. Given the computational complexity, we explore this effect as the strength of network effects, $e ,$ approaches zero. We <sup>fi</sup>nd that as long as m is suf<sup>fi</sup>ciently large $( \mathbf { e } . \mathbf { g } . , m > v )$ , because the incumbent has a larger market share, network effects make the incumbent more attractive to users, thereby reducing users’ tendencies to switch to the entrant. Hence, as the network effects become stronger, the entrant’s pro<sup>fi</sup>t decreases and the incumbent’s pro<sup>fi</sup>t increases.

When e is suf<sup>fi</sup>ciently large, we <sup>fi</sup>nd that the equilibrium in which the entrant has positive demand cannot be sustained and the incumbent becomes the monopoly. This result is expected because when network effects dominate pricing effects, if an entrant enters the market, the incumbent always has the incentive and is able to take advantage of its installed base advantage to drive the entrant out of the market.

Proposition 9. When network effects become sufficiently large, the incumbent can deter the entrant from entering the market and thereby monopolize the market.

## 3.6. Heterogeneous Switching Costs

In our model, we assume that buyers and service providers face the same switching costs. In practice, however, their switching costs may differ. For example, in the ride-sharing industry, riders only need to download a new app to switch to a different platform, whereas drivers may have to undergo background checks and veri<sup>fi</sup>cation processes to switch to a different platform. In order to investigate how heterogeneity in switching costs affects the platforms, we allow buyers’ switching cost to be uniformly distributed between zero and $m _ { b } ,$ and service providers’ switching costs to be uniformly distributed between zero and $m _ { s } .$ Then, we obtain the following proposition.

Proposition 10. When we allow buyers’ switching cost to be uniformly distributed between zero and $m _ { b }$ and service providers’ switching costs to be uniformly distributed between zero and $m _ { s } ,$ we have $\begin{array} { r } { \frac { \partial \pi _ { E } ^ { * } } { \partial m _ { b } } < \frac { \partial \pi _ { E } ^ { * } } { \partial m _ { s } } < 0 \ : a n d \frac { \partial \pi _ { I } ^ { * } } { \partial m _ { b } } \geq \frac { \partial \pi _ { I } ^ { * } } { \partial m _ { s } } \geq 0 . } \end{array}$

Proposition 10 suggests that an increase in switching costs on the buyer side harms the entrant or bene<sup>fi</sup>ts the incumbent more than the same increase on the service provider side. The intuition is that because of the existence of mobile buyers, we have more service providers than local buyers. Hence, the total number of transactions that the entrant platform serves depends largely on the number of buyers the entrant can incentivize to switch to the entrant platform. Thus, buyers’ switching cost affects <sup>fi</sup>rm pro<sup>fi</sup>ts more than that of service providers. Note that when the optimal θ, $\theta ^ { * }$ , reaches the threshold that is just high enough to not trigger the incumbent’s response, the incumbent’s pro<sup>fi</sup>t is independent of $m _ { b }$ and $m _ { s } .$ This explains why sometimes $\frac { \partial \pi _ { I } ^ { * } } { \partial m _ { b } } = \frac { \partial \pi _ { I } ^ { * } } { \partial m _ { s } } = 0$

## 4. Discussion and Conclusion

Extant studies in the platform strategy literature typically assume that each participant on one side of a market is (potentially) connected to every participant on the other side of the market. Our paper departs from this assumption to explore the impact of network interconnectivity on the defensibility of an incumbent with presence in multiple markets against an entrant that seeks to enter one of these markets.

As depicted in Figure 4, our model captures heterogeneous network interconnectivity across different industries, ranging from isolated network clusters $( r = 0 )$ to a fully connected network $( r = 1 )$ . Examples of isolated local clusters (i.e., no mobile buyers) include Handy, a marketplace for handyman services, and Instacart, a platform that matches consumers with grocery shoppers. In such markets, consumers only buy services in their local markets and do not typically use such services when they travel. Toward the other end of the spectrum, we have strongly connected networks. This is the case for Airbnb, a platform on which travelers transact mostly with hosts outside their local clusters, and Upwork, an online outsourcing marketplace, where any clients and freelancers can initiate projects. Between the two extreme scenarios, we have networks that consist of local clusters with moderate interconnectivity. In the case of Uber, Grubhub, and Groupon, consumers primarily use their services in their local clusters but also use such services when they travel.

We <sup>fi</sup>nd that the greater the interconnectivity, the lower the incumbent’s incentive to respond and, hence, the stronger the entrant’s incentive to reach more users in a local market. Whereas we <sup>fi</sup>nd that the incumbent’s pro<sup>fi</sup>t always increases with interconnectivity, the entrant’s pro<sup>fi</sup>t does not always decrease with interconnectivity. When advertising is inexpensive and mobile buyers consume in both their local markets and the markets they travel to, the high interconnectivity between markets also increases the entrant’s pro<sup>fi</sup>t, thereby making it dif<sup>fi</sup>cult for the incumbent to deter entry; on the other hand, when advertising is costly and/or mobile buyers consume only in the markets they travel to, high interconnectivity reduces the entrant’s pro<sup>fi</sup>t, thereby helping the incumbent deter entry. When the advertising cost is at an intermediate level, the entrant is more likely to survive under moderate interconnectivity between markets. We also extend our model to examine situations where markets are heterogeneous, the entrant is able to target mobile buyers, buyers and service providers have different switching costs, and network effects are present. Overall, these results help explain barriers to entry in platform markets and the resulting performance heterogeneity among platform <sup>fi</sup>rms in different markets.

Figure 4. Platform Markets with Different Degrees of Network Interconnectivity

<table><tr><td colspan="2">Isolated local clusters</td><td>Local clusters with interconnectivity</td><td>Strong connectivity</td></tr><tr><td colspan="2">0</td><td></td><td>1</td></tr><tr><td>Examples: Handy Instacart</td><td>Uber Grubhub Groupon</td><td>Airbnb Upwork</td><td></td></tr></table>

These results corroborate empirical observations of many platform markets. For example, we show that it is optimal for an entrant not to trigger incumbent responses. The founders of Fasten, an entrant into the ridesharing market in Boston, were very clear from the beginning that they did not want to trigger Uber’s response by strategically minimizing their advertising activities.<sup>13</sup> Fasten also chose not to target visitors in Boston: it did not advertise in Boston’s Logan Airport or in its South Station Bus Terminals. Indeed, although Fasten grew rapidly in Boston during the period 2015–2017, Uber and Lyft did not change their prices or wages to compete. As a counterexample, when Meituan—a major player in China’s online-to-of<sup>fl</sup>ine services such as food delivery, movie ticketing, and travel bookings—entered the ridesharing business, it was able to build awareness of its service at almost no cost through its existing app, which had an extensive user base. Meituan’s entry into the Shanghai ride-sharing market triggered strong responses from the incumbent, Didi, thereby leading to a subsidy war between the two companies. Meituan subsequently decided to halt ride-sharing expansion in China.

Our results also suggest that Airbnb’s and Booking.com’s business models are more defensible than Uber’s because most of their customers are travelers and do not use the services in their local markets as often, whereas Uber’s consumers primarily use its services in their local markets. The difference in defensibility is a key aspect for why Airbnb and Booking.com were able to achieve pro<sup>fi</sup>tability, whereas Uber has been hemorrhaging money.<sup>14</sup>

Our study offers important managerial implications for platform owners. We <sup>fi</sup>nd that an incumbent’s pro<sup>fi</sup>t increases with interconnectivity regardless of whether mobile buyers consume in local markets; thus, incumbent platforms should seek to build strong interconnectivity in their networks. In our model, the level of interconnectivity is given exogenously; however, in practice, how <sup>fi</sup>rms design their platforms can in<sup>fl</sup>uence interconnectivity. For example, although Craigslist is a local classi<sup>fi</sup>eds service, its housing and job services attract users from other markets. Our research suggests that such services are important sources of Craigslist’s sustainability, and, thus, Craigslist should strategically devote more resources to grow these services. As another example, many social networking platforms such as Facebook and WeChat allow companies or in<sup>fl</sup>uencers to create public accounts that any user can connect with. Such moves increase interconnectivity among their local network clusters.

Our research suggests that an entrant needs to conduct a thorough network analysis to understand the interconnectivity among different markets, the strength of network effects, the capability of its targeting technologies, and whether mobile users consume in their local markets. These factors, together with the cost of reaching users, can help inform the entrant’s location choice and how aggressively it should build awareness in a new market. The entrant needs to realize that even if advertising incurs little cost, it is not always optimal for it to advertise to every user. The entrant should advertise to the extent that it does not trigger competitive responses from the incumbent. Equally important, it is not always the case that an entrant should choose a market with low interconnectivity. When advertising is inexpensive and mobile buyers consume in local markets, it could be more pro<sup>fi</sup>table to enter a market with high interconnectivity.

Our research also offers important implications for policy makers. With the growing popularity of digital platforms, policy makers around the world are increasingly concerned about the market power of these platforms. Our research suggests that regulators should pay close attention to the network structures of these platform markets to improve their understanding of market competitiveness and entry barriers.

As one of the <sup>fi</sup>rst papers that explicitly models network interconnectivity of platform markets, our paper opens a new direction for future research on platform strategies. For example, our model focuses on an entrant’s entry strategy and only allows the incumbent to react through pricing. Future research could consider the incumbent’s perspective and examine other strategies for entry deterrence.

Our paper focuses on examining an entrant with limited resources (to overcome entry cost in each market) and an incumbent that already exists in many markets. Even if we allow the entrant to enter more than one market, as long as the number of markets the entrant can realistically enter is small compared with the total number of available markets available (which is true in most cases), our results would not change qualitatively because network interconnectivity (or awareness spillover) plays a rather minor role for the entrant relative to the incumbent. Take the Uber and Fasten cases as examples. Even if Fasten enters a second market, the number of Fasten users from that market to Boston is rather small compared with the number of Uber users from the hundreds of cities outside Boston to Boston. This also implies that Fasten’s advertising in the second market has little impact, relative to Uber, on the <sup>fi</sup>rst market that Fasten entered. Future research can extend our analysis to examine cases involving a resourceful entrant that can enter many markets at once, such as in the case of Uber versus Grab in Southeast Asia.

In our model, one buyer and one service provider are matched during each transaction. In other words, at a given time, a buyer cannot buy from multiple service providers (regardless of whether they are on the same platform or different ones), and a service provider cannot serve multiple buyers (regardless of whether these buyers are on the same or different platforms). This assumption matches with the ridessharing industry in that the same rider or the same driver does not show up in multiple cars at a time.<sup>15</sup> If we allow multiple transactions for each user, we may observe multihoming in that a rider may be matched to Uber drivers for certain transactions and Lyft drivers for other transactions. Future research can extend our model to incorporate multiple transactions for each user and allow buyers and service providers to multihome. In this case, the entrant needs to decide on the entry and advertising strategy based on how many transactions it expects to serve. Buyers and service providers will decide whether to adopt the entrant platform based on their switching costs and expected bene<sup>fi</sup>ts from future transactions. Although the game will be more complicated, we believe that our key insights would continue to hold. For example, in equilibrium, only the buyers and service providers with low switching cost will adopt the entrant platform to multihome. Incoming mobile buyers will continue to disincentivize the incumbent to respond in each period, which ultimately drives the impact of network interconnectivity on the entrant’s advertising strategy and pro<sup>fi</sup>tability, as illustrated in our model.

Furthermore, to focus on the impact of network interconnectivity, we abstract away many factors that could in<sup>fl</sup>uence competitive interactions between incumbents and entrants. For example, in the ride-sharing industry, riders may not care much about vehicle features. However, in the accommodation industry, travelers are likely to care about the features of properties, thereby making it easier for an entrant into the accommodation industry to differentiate itself from an incumbent and reducing the competitive intensity. In addition, because of tractability, we could not examine all possible parameter values after incorporating network effects into our main model. Future research could further explore how these factors affect competitive interactions.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their insightful comments and suggestions. This work also bene<sup>fi</sup>ted from the reviews and feedback from participants at the Conference on Information Systems and Technology, Platform Strategy Research Symposium, and ISOM Workshop at Emory University.

## Appendix

Proof of Lemma 1. Given the entrant’s prices, $p _ { E }$ and $w _ { E } ,$ the incumbent’s best response is always to choose $p _ { I }$ and $w _ { I } ,$ such that the number of service buyers equals the number of service providers on the incumbent’s platform. Otherwise, the incumbent can always increase its pro<sup>fi</sup>t by increasing $p _ { I }$ or decreasing w so that the pro<sup>fi</sup>t margin $( p _ { I } - w _ { I } )$ goes up without affecting the matched demand (i.e., min $( N _ { I } ^ { S } , ~ N _ { I } ^ { B } ) )$ . Similarly, given the incumbent’s prices, p<sub>I</sub> and $w _ { I } ,$ the entrant’s best response is always to choose p<sub>E</sub> and $w _ { E }$ , such that the number of service buyers equals the number of service providers on the entrant’s platform. w

Proof of Proposition 1. We <sup>fi</sup>rst solve for the optimal prices for the interior equilibrium, where $0 < a _ { i } ^ { * } < m .$ We <sup>fi</sup>rst con<sup>fi</sup>rm that the second-order derivatives are both negative: $\begin{array} { r } { \frac { \partial ^ { 2 } \pi _ { I } } { \partial p _ { I } ^ { 2 } } = \frac { \partial ^ { 2 } \pi _ { E } } { \partial p _ { E } ^ { 2 } } = - \frac { 2 N ( 1 + \frac { 1 } { 1 + r } ) \theta } { m } < 0 . } \end{array}$ . We then derive the <sup>fi</sup>rst-order conditions:

$$
\frac {\partial \pi_ {I}}{\partial p _ {I}} = N \left(2 + r + \frac {\left(p _ {E} (3 + r) - 2 p _ {I} (2 + r) + (1 + r) w _ {E}\right) \theta}{m (1 + r)}\right) = 0,\tag{A.1}
$$

$$
\frac {\partial \pi_ {E}}{\partial p _ {E}} = \frac {N (p _ {I} (3 + r) - 2 p _ {E} (2 + r) + (1 + r) w _ {I}) \theta}{m (1 + r)} = 0.\tag{A.2}
$$

We further obtain the following:

$$
p _ {I} = \frac {1}{2} \left(\frac {p _ {E} (3 + r) + (1 + r) w _ {E}}{2 + r} + \frac {m (1 + r)}{\theta}\right).\tag{A.3}
$$

$$
p _ {E} = \frac {(3 + r) p _ {I} + (1 + r) w _ {I}}{4 + 2 r}.\tag{A.4}
$$

Solving (A.3) and $( \mathrm { A } . 4 )$ along with $( p _ { I } - p _ { E } ) = ( 1 + r ) ( w _ { E } -$ w<sub>I)</sub> (according to Lemma 1), we obtain $p _ { I } ^ { * } = \frac { 2 m ( 2 ~ + ~ r ) } { 3 \theta } + w _ { I }$ $\begin{array} { r } { p _ { E } ^ { * } = \frac { m ( 3 { \mathrm { ~ + ~ } } r ) } { 3 \theta } + w _ { I } , } \end{array}$ and $\begin{array} { r } { w _ { E } ^ { * } = \frac { m } { 3 \theta } + w _ { I } } \end{array}$ . The number of buyers and service providers using each platform under the optimal prices are $N _ { I } ^ { B * } = N _ { I } ^ { S * } = \frac { 2 N ( 1 ~ + ~ r ) } { 3 }$ and $N _ { E } ^ { B * } = N _ { E } ^ { S * } = \frac { N ( 1 ~ + ~ r ) } { 3 } .$ The pro<sup>fi</sup>ts under the optimal prices are $\pi _ { I } ^ { * } ( \theta ) =$ 4mN 1 $\frac { + \textit { r } ) ( 2 \textit { + } \textit { r } ) } { 9 \theta }$ and $\begin{array} { r } { \pi _ { E } ^ { * } ( \theta ) = \frac { m N ( 1 ~ + ~ r ) ( 2 ~ + ~ r ) } { 9 \theta } - L \Big ( \theta ( 2 N + r N ) \Big ) } \end{array}$

For this interior equilibrium to hold, we need to ensure that the incumbent has no incentive to deviate from this equilibrium by charging such a high price $p _ { I } = v$ that no one from the overlapped market will transact on its platform but that it gets the most pro<sup>fi</sup>t from the users who are not aware of the entrant.<sup>16</sup> The highest possible deviation pro<sup>fi</sup>t the incumbent gets in this case is $( 1 - \theta + r ) N v ,$ whereas the incumbent’s equilibrium pro<sup>fi</sup>t is $\frac { 4 m N ( 1 ~ + ~ r ) ( 2 ~ + ~ r ) } { 9 \theta } .$ To guarantee that the latter is higher (i.e., $\frac { 4 m N ( 1 ~ + ~ r ) ( 2 ~ + ~ r ) } { 9 \theta } > ( 1 - \theta + r ) N v )$ for all values of $\theta ,$ we assume that $m > { \frac { 9 ( 1 \ + \ r ) v } { 1 6 ( 2 \ + \ r ) } } .$ . This condition also ensures that the incumbent will never completely give up the overlapped market—that is, the entrant will never have the entire overlapped market. This is quite realistic because, in practice, there are always users who have a suf<sup>fi</sup>ciently high switching cost such that they would rather remain with their current platform.

For this interior equilibrium to hold, we must also have $\begin{array} { r } { p _ { I } ^ { * } = \frac { 2 m ( 2 { \it \Delta \phi } + { \it \Delta \phi } r ) } { 3 \theta } + w _ { I } < v } \end{array}$ . Because the choice of $w _ { I }$ does not affect either platform’s pro<sup>fi</sup>t and any border solution is inferior to the interior solution, the incumbent has incentive to ensure that $p _ { I } ^ { * } < v$ holds as much as possible by setting $w _ { I } ^ { * } = 0 .$ . Consequently, $\begin{array} { r } { p _ { I } ^ { * } = \frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 \theta } , p _ { E } ^ { * } = \frac { m ( 3 \mathrm { ~ + ~ } r ) } { 3 \theta } . } \end{array}$ , and $\begin{array} { r } { w _ { E } ^ { * } = \frac { m } { 3 \theta } , } \end{array}$ and the condition $p _ { I } ^ { * } < v$ requires $\theta > \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v }$ When $\begin{array} { r } { \theta \leq \operatorname* { m i n } \left( \frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v } , 1 \right) } \end{array}$ , even with $w _ { I } ^ { * } = 0 ,$ , the optimal $p _ { I } ^ { * }$ cannot satisfy $p _ { I } ^ { * } < v .$ . Thus, the incumbent’s price is bounded at $p _ { I } ^ { * } = v$ to the buyers. Then, based on $\mathrm { ( A . 4 ) } ,$ $w _ { I } ^ { * } = 0$ and $p _ { I } - p _ { E } = ( 1 + r ) ( w _ { E } - w _ { I } ) .$ , we obtain $\begin{array} { r } { p _ { E } ^ { * } = \frac { ( 3 { \ + \ } r ) v } { 2 ( 2 { \ + \ r } ) } } \end{array}$ and $\begin{array} { r } { w _ { E } ^ { * } = \frac { v } { 2 ( 2 \ + \ r ) } . } \end{array}$ The numbers of buyers and service providers using each platform under the optimal prices are $\begin{array} { r } { N _ { I } ^ { B * } = N _ { I } ^ { S * } = \frac { N ( 1 ~ + ~ r ) } { 2 } \Big ( 2 - \frac { v \theta } { m ( 2 ~ + ~ r ) } \Big ) } \end{array}$ and $\begin{array} { r } { N _ { E } ^ { B * } = N _ { E } ^ { S * } = \frac { N ( 1 ~ + ~ r ) v \theta } { 2 m ( 2 ~ + ~ r ) } . } \end{array}$ The pro<sup>fi</sup>ts under the optimal prices are $\pi _ { I } ^ { * } ( \theta ) = { \frac { N ( 1 ~ + ~ r ) v } { 2 } }$ $\begin{array} { r } { \left( 2 - \frac { v \theta } { m ( 2 \ + \ r ) } \right) } \end{array}$ and $\begin{array} { r } { \pi _ { E } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - L ( \theta ( 2 N + r N ) ) } \end{array}$ . w Proof of Corollary 1. When $\begin{array} { r } { \theta > \frac { 2 m ( 2 { \it \Delta \phi } + { \it \Delta \phi } ^ { r } ) } { 3 v } , \quad \pi _ { \mathrm { E } } ^ { * } ( \theta ) = } \end{array}$ $\frac { m N ( 1 ~ + ~ r ) ( 2 ~ + ~ r ) } { 9 \theta } - L ( \theta ( 2 N + r N ) )$ , which decreases with θ.

Thus, the entrant never has the incentive to increase θ once $\theta > \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v }$ . Therefore, the optimal choice of θ always satis<sup>fi</sup>es $\begin{array} { r } { \theta \leq \operatorname* { m i n } \left( \frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v } , 1 \right) } \end{array}$ : w

Proof of Proposition 2. According to Corollary 1, the entrant always chooses $\begin{array} { r } { \theta \leq \operatorname* { m i n } { \left( \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } , 1 \right) } ; } \end{array}$ ; then, according to Proposition $\begin{array} { r } { 1 , \pi _ { I } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v } { 2 } \left( 2 - \frac { v \theta } { m ( 2 ~ + ~ r ) } \right) } \end{array}$ and $\pi _ { E } ^ { * } ( \theta ) =$ $\frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - L ( \theta ( 2 N + r N ) )$ Given $L ( n ) = \ k n ^ { 2 } , \quad \pi _ { E } ^ { * } ( \theta ) =$ $\frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - k N ^ { 2 } ( 2 + r ) ^ { 2 } \theta ^ { 2 }$ . We <sup>fi</sup>rst con<sup>fi</sup>rm that the secondorder derivative is negative: $\pi _ { E } ^ { * \prime \prime } ( \theta ) = - 2 k \ N ^ { 2 } ( 2 + r ) ^ { 2 } < 0$ Then, we derive the <sup>fi</sup>rst-order condition:

$$
\pi_ {E} ^ {* \prime} (\theta) = \frac {N (1 + r) v ^ {2} - 8 k N ^ {2} m (2 + r) ^ {3} \theta}{4 m (2 + r)} = 0.\tag{A.5}
$$

This yields

$$
\theta^ {*} = \frac {(1 + r) v ^ {2}}{8 k N m (2 + r) ^ {3}}.\tag{A.6}
$$

Because the optimal choice of θ is bounded by $\theta \leq$ $\frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v }$ and $\theta \leq 1$ , we compare $\frac { ( 1 \ + \ r ) { { v } ^ { 2 } } } { 8 k { { N m } ( 2 \ + \ r ) } ^ { 3 } }$ with the two bounds and obtain $\frac { ( 1 ~ + ~ r ) v ^ { 2 } } { 8 k N m ( 2 ~ + ~ r ) ^ { 3 } } \leq \frac { 2 m ( 2 ~ + ~ r ) } { 3 v }$ if $ { k } \geq \frac { 3 ( 1 + r ) { v } ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } }$ and $\frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 k N m { ( 2 \ + \ r ) } ^ { 3 } } \leq 1$ if $\overset { } { \underset { } { k } } \geq \frac { ( 1 \ + \ { r } ) { { v } ^ { 2 } } } { 8 m { { N } { ( 2 \ + \ r ) } ^ { 3 } } }$ : Thus, we derive the following two cases:

i When $\begin{array} { r } { k \ge m a x \biggl ( \frac { 3 ( 1 \ + \ r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \ + \ r ) ^ { 4 } } , \frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 m N ( 2 \ + \ r ) ^ { 3 } } \biggr ) . } \end{array}$ , both $\frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 k N m ( 2 \ + \ r ) ^ { 3 } } \leq$ $\frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v }$ and $\frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 k N m ( 2 \ + \ r ) ^ { 3 } } \leq 1$ hold. Then $\begin{array} { r } { \theta ^ { * } = \frac { ( 1 { \ } + { \ r } ) v ^ { 2 } } { 8 k N m ( 2 { \ } + { \ r } ) ^ { 3 } } , } \end{array}$ and it is easy to verify that $\begin{array} { r } { \frac { \partial \theta ^ { * } } { \partial r } < 0 } \end{array}$ . By replacing θ with $\frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 k N m { ( 2 \ + \ r ) } ^ { 3 } }$ in $\begin{array} { r } { \pi _ { I } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v } { 2 } \Big ( 2 - \frac { v \theta } { m ( 2 ~ + ~ r ) } \Big ) } \end{array}$ and $\begin{array} { r } { \pi _ { E } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - L \left( 2 N \Big ( \theta + \frac { \theta r } { 2 } \Big ) \right) . } \end{array}$ we obtain $\pi _ { I } ^ { * } =$ $\frac { N ( 1 ~ + ~ r ) v } { 2 } \left( 2 - \frac { ( 1 ~ + ~ r ) v ^ { 3 } } { 8 k N m ^ { 2 } ( 2 ~ + ~ r ) ^ { 4 } } \right)$ and $\begin{array} { r } { \pi _ { E } ^ { * } = \frac { ( 1 ~ + ~ r ) ^ { 2 } v ^ { 4 } } { 6 4 k m ^ { 2 } ( 2 ~ + ~ r ) ^ { 4 } } . } \end{array}$

ii When $\begin{array} { r } { k < m a x \left( \frac { 3 ( 1 \ + \ r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \ + \ r ) ^ { 4 } } , \frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 m N ( 2 \ + \ r ) ^ { 3 } } \right) , } \end{array}$ , either $\begin{array} { r } { \frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 k N m \left( 2 + r \right) ^ { 3 } } \le \ } \end{array}$ $\begin{array} { r } { \frac { 2 m ( 2 { \it \Delta \phi } + { \it \Delta \phi } r ) } { 3 v } \mathrm { o r } \frac { ( 1 { \it \Delta \phi } + { \it \Delta \phi } r ) v ^ { 2 } } { 8 k N m ( 2 { \it \Delta \phi } + { \it \Delta \phi } r ) ^ { 3 } } \leq 1 } \end{array}$ does not hold. Then $\theta ^ { * } =$ $m i n \Big ( \frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } , 1 \Big ) _ { \mathrm { - } }$ and it is easy to verify that $\begin{array} { r } { \frac { \partial \theta ^ { * } } { \partial r } \geq 0 . } \end{array}$ When $\frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } < 1 .$ , by replacing θ with $\frac { 2 m ( 2 \mathrm { ~ + ~ } r ) } { 3 v }$ in $\begin{array} { r } { \pi _ { I } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v } { 2 } \Big ( 2 - \frac { v \theta } { m ( 2 ~ + ~ r ) } \Big ) } \end{array}$ and $\begin{array} { r } { \pi _ { E } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - } \end{array}$ $\begin{array} { r } { L \Big ( 2 N \Big ( \theta + \frac { \theta r } { 2 } \Big ) \Big ) . } \end{array}$ , we obtain $\pi _ { I } ^ { * } = \frac { 2 N v ( 1 ~ + ~ r ) } { 3 }$ and $\pi _ { E } ^ { * } =$ $\frac { N ( 1 ~ + ~ r ) v } { 6 } - ~ \frac { 4 k N ^ { 2 } m ^ { 2 } ( 2 ~ + ~ r ) ^ { 4 } } { 9 v ^ { 2 } }$ . When $\frac { 2 m ( 2 { \bf \alpha } + { \bf \beta } r ) } { 3 v } \ge 1 ,$ , by replacing θ with 1 in $\begin{array} { r } { \pi _ { I } ^ { * } ( \theta ) = \frac { N ( 1 ~ + ~ r ) v } { 2 } \left( 2 - \frac { v \theta } { m ( 2 ~ + ~ r ) } \right) } \end{array}$ and $\pi _ { E } ^ { * } ( \theta ) =$ $\frac { N ( 1 ~ + ~ r ) v ^ { 2 } \theta } { 4 m ( 2 ~ + ~ r ) } - L \Big ( 2 N \Big ( \theta + \frac { \theta r } { 2 } \Big ) \Big )$ we obtain $\pi _ { I } ^ { * } = \frac { N ( 1 ~ + ~ r ) v } { 2 }$ $\begin{array} { r } { \left( \mathrm { 2 } - \frac { v } { m ( 2 \mathrm { ~ + ~ } r ) } \right) \mathrm { a n d ~ } \pi _ { E } ^ { \ast } = \frac { N ( 1 \mathrm { ~ + ~ } r ) v ^ { 2 } - 4 k N ^ { 2 } m ( 2 \mathrm { ~ + ~ } r ) ^ { 3 } } { 4 m ( 2 \mathrm { ~ + ~ } r ) } \cdot \quad \bigsqcup } \end{array}$

Proof of Corollary 2. If $k = 0 ,$ , according to Proposition 2 $\mathrm { i i } , \theta ^ { * } = { \frac { 2 m ( 2 { \theta } + { \Gamma } r ) } { 3 v } }$ when $\frac { 2 m ( 2 { \mathrm { ~ + ~ } } r ) } { 3 v } < 1$ . w

Proof of Corollary 3. In Proposition $2 , \ \frac { \partial \theta ^ { * } } { \partial r } < 0$ in part i and $\frac { { \partial \theta } ^ { * } } { { \partial r } } \geq 0$ in part ii. Because $\begin{array} { r } { m a x { \left( \frac { 3 ( 1 \ + \ { \bar { \ r } } ) { \bar { v } } ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \ + \ r ) ^ { 4 } } , \frac { ( 1 \ + \ r ) v ^ { 2 } } { 8 m N ( 2 \ + \ r ) ^ { 3 } } \right) } } \end{array}$ is a decreasing function of $r ,$ for intermediate values of $k ,$ as r increases, the region can shift from ii to i. So when $\begin{array} { r } { k < m a x \left( \frac { 3 ( 1 \mathrm { ~ + ~ } r _ { m a x } ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \mathrm { ~ + ~ } r _ { m a x } ) ^ { 4 } } , \frac { ( 1 \mathrm { ~ + ~ } r _ { m a x } ) v ^ { 2 } } { 8 m N ( 2 \mathrm { ~ + ~ } r _ { m a x } ) ^ { 3 } } \right) , \frac { \partial \theta ^ { * } } { \partial r } \geq 0 . } \end{array}$ . When k max $\displaystyle { \left( \frac { 3 ( 1 ~ + ~ r _ { m i n } ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 ~ + ~ r _ { m i n } ) ^ { 4 } } , \frac { ( 1 ~ + r _ { m i n } ) v ^ { 2 } } { 8 m N ( 2 ~ + ~ r _ { m i n } ) ^ { 3 } } \right) } , ~ \frac { \partial \theta ^ { * } } { \partial r } < 0 .$ . And when $\begin{array} { r } { m a x \Big ( \frac { 3 ( 1 + r _ { m a x } ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \mathrm { \ } + \ r _ { m a x } ) ^ { 4 } } , \frac { ( 1 \mathrm { \ } + \ r _ { m a x } ) v ^ { 2 } } { 8 m N ( 2 \mathrm { \ } + \ r _ { m a x } ) ^ { 3 } } \Big ) \leq k < m a x \Big ( \frac { 3 ( 1 \mathrm { \ } + \ r _ { m i n } ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 \mathrm { \ } + \ r _ { m i n } ) ^ { 4 } } , \frac { ( 1 \mathrm { \ } + \ r _ { m a x } ) v ^ { 2 } } { 8 m N ( 2 \mathrm { \ } + \ r _ { m a x } ) ^ { 3 } } \Big ) } \end{array}$ $\frac { ( 1 \ + r _ { m i n } ) v ^ { 2 } } { 8 m N ( 2 \ + \ r _ { m i n } ) ^ { 3 } } \biggl ) ,$ , as r increases from zero, the optimal $\boldsymbol { \theta ^ { * } }$ increases with r <sup>fi</sup>rst and then decreases with r: w

Proof of Proposition 3. From Proposition 2, it is easy to verify that $\frac { \partial \pi _ { I } ^ { * } } { \partial r } > 0$ in both parts i and ii and $\frac { \partial \pi _ { E } ^ { * } } { \partial r } < 0$ in part i. To examine $\frac { \partial \pi _ { E } ^ { * } } { \partial r }$ in part ii, we consider the following two cases:

1. When $\frac { 2 m ( 2 + r ) } { 3 v } < 1$ , max $\begin{array} { r } { \left( \frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } } , \frac { ( 1 + r ) v ^ { 2 } } { 8 m N ( 2 + r ) ^ { 3 } } \right) = \frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } } . } \end{array}$ In this case, $\begin{array} { r } { \frac { \partial \pi _ { E } ^ { * } } { \partial r } > 0 \mathrm { ~ i f ~ } k < \frac { 3 v ^ { 3 } } { 3 2 m ^ { 2 } N \left( 2 + r \right) ^ { 3 } } . } \end{array}$ Because $\frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } }$ decreases with $r ,$ for intermediate values of $k ,$ as r increases, the region can shift from ii to i. So when $\begin{array} { r } { k < \frac { 3 v ^ { 3 } } { 3 2 m ^ { 2 } N ( 2 + r _ { m a x } ) ^ { 3 } } , \frac { \partial \theta ^ { * } } { \partial r } > 0 . } \end{array}$ When $\begin{array} { r } { k \geq \frac { 3 v ^ { 3 } } { 3 2 m ^ { 2 } N ( 2 + r _ { m i n } ) ^ { 3 } } , \ \frac { \partial \theta ^ { * } } { \partial r } < 0 . } \end{array}$ And when $\begin{array} { r } { \frac { 3 v ^ { 3 } } { 3 2 m ^ { 2 } N \left( 2 + r _ { m a x } \right) ^ { 3 } } \leq k < } \end{array}$ $\frac { 3 v ^ { 3 } } { 3 2 m ^ { 2 } N \left( 2 + r _ { m i n } \right) ^ { 3 } } ,$ as r increases from zero, $\pi _ { E } ^ { * }$ increases with r <sup>fi</sup>rst and then decreases with r.

2. When $\begin{array} { r } { \frac { 2 m ( 2 + r ) } { 3 v } \geq 1 , m a x \Big ( \frac { 3 ( 1 + r ) v ^ { 3 } } { 1 6 m ^ { 2 } N ( 2 + r ) ^ { 4 } } , \frac { ( 1 + r ) v ^ { 2 } } { 8 m N ( 2 + r ) ^ { 3 } } \Big ) = \frac { ( 1 + r ) v ^ { 2 } } { 8 m N ( 2 + r ) ^ { 3 } } . } \end{array}$ In this case, $\begin{array} { r } { \frac { \partial \pi _ { E } ^ { * } } { \partial r } > 0 \ i f \ k < \frac { v ^ { 2 } } { 8 m N \left( 2 + r \right) ^ { 3 } } } \end{array}$ . Because $\frac { ( 1 + r ) v ^ { 2 } } { 8 m N ( 2 + r ) ^ { 3 } }$ decreases with r, for intermediate values of $k ,$ as r increases, the region can shift from ii to i. So when $\begin{array} { r } { k < \frac { v ^ { 2 } } { 8 m N \left( 2 + r _ { m a x } \right) ^ { 3 } } , \ \frac { \partial \theta ^ { * } } { \partial r } > 0 } \end{array}$ . When $\begin{array} { r } { k \geq \frac { v ^ { 2 } } { 8 m N ( 2 + r _ { m i n } ) ^ { 3 } } , \frac { \partial \theta ^ { * } } { \partial r } < 0 } \end{array}$ . And when $\begin{array} { r } { \frac { v ^ { 2 } } { 8 m N ( 2 + r _ { m a x } ) ^ { 3 } } \leq k < \frac { v ^ { 2 } } { 8 m N ( 2 + r _ { m i n } ) ^ { 3 } } , } \end{array}$ as r increases from zero, $\pi _ { E } ^ { * }$ increases with r <sup>fi</sup>rst and then decreases with r. w

## Endnotes

<sup>1</sup> We consider the scenario in which mobile buyers do not consume in their local markets in an extension.

<sup>2</sup> This assumption is relaxed in an extension of the model in which not all buyers and sellers are aware of the incumbent.

<sup>3</sup> Our results continue to hold qualitatively if the performance of the entrant’s advertising level is uncertain (i.e., when the entrant decides $\theta ,$ the fraction of potential users reached through advertising becomes $\theta + \varepsilon ,$ where ε is a random variable).

<sup>4</sup> If we allow the marginal cost to be a positive constant, then the equilibrium service prices will increase by this constant.

<sup>5</sup> Mathematically, this assumption requires that the distribution of the switching cost be sufficiently sparse, that is, $m > { \frac { 9 ( 1 + r ) v } { 1 6 ( 2 + r ) } } .$

<sup>6</sup> If there is no cost for the entrant to reach its fans, we can modify the cost function to be $L ( n ) = k ( \operatorname* { m a x } ( n - z , 0 ) ) ^ { 2 }$ , where z is the total number of fans. Our results hold qualitatively.

<sup>7</sup> When $\begin{array} { r } { \frac { 2 m ( 2 + r ) } { 3 v } < 1 , \ \theta ^ { * } = \frac { 2 m ( 2 + r ) } { 3 v } } \end{array}$ and the entrant’s profit increases with $r ,$ as long as $\begin{array} { r } { k < \frac { 3 v ^ { \frac { 1 } { 3 } } } { 3 2 N m ^ { 2 } \left( 2 + r \right) ^ { 3 } } } \end{array}$ . When $\begin{array} { r } { \frac { 2 m ( 2 + r ) } { 3 v } \ge 1 , \theta ^ { * } = 1 \ } \end{array}$ and the entrant’s profit increases with $r ,$ as long as $\begin{array} { r } { k < \frac { v ^ { 2 } } { 8 m N \left( 2 + r \right) ^ { 3 } } } \end{array}$

<sup>8</sup> In the extensions, we make a similar assumption as in the main model that m is sufficiently large so that, in equilibrium, the entrant will not take away the entire segment of users who are aware of both platforms. Because the condition changes in different extensions, for consistency, we use the most restrictive condition, m > ${ 3 v / 5 } ,$ , in all extensions. This approach does not affect the key insights drawn from different extensions.

<sup>10</sup> The thresholds for k are provided in the online appendix. We also explored heterogeneous market sizes. As indicated by Proposition 2, when k is sufficiently large, market sizes will not affect the entrant’s profit. When k is small, if market size is sufficiently large for a certain market, the fraction of mobile buyers (r) will have a negligible effect and, thus, the entrant should simply choose the largest market to enter; otherwise, the entrant’s choice will depend on both r and N.

<sup>11</sup> Residents in a city occasionally do use Airbnb for local getaways (this demand has been particularly strong during the COVID-19 pandemic).

<sup>12</sup> Mathematically, we require e < min $\left( { \frac { v } { 2 N } } , \quad { \frac { m } { 4 N } } \right)$

<sup>13</sup> Based on the authors’ interviews with the founders.

<sup>14</sup> See, for example, Dickey (2019), Franklin (2019), and https:// www.macrotrends.net/stocks/charts/BKNG/booking-holdings/grossprofit (accessed October 2019).

<sup>15</sup> This assumption applies to Airbnb as well if we assume that each host has one room to offer at a time and if we treat each host with multiple rooms to offer as multiple service providers.

<sup>16</sup> This deviation is not adequately captured by the optimization process above because its calculation automatically assigns a negative profit to the overlapped market $\mathrm { i f } \ p _ { I } - p _ { E } > m$

## References

Abrahamson E, Rosenkopf L (1997) Social network effects on the extent of innovation diffusion: A computer simulation. Organ. Sci. 8(3):289–309.

Adner R, Chen J, Zhu F (2020) Frenemies in platform markets: Heterogeneous pro<sup>fi</sup>t foci as drivers of compatibility decisions. Management Sci. 66(6):2432–2451.

Afuah A (2013) Are network effects really all about size? The role of structure and conduct. Strategic Management J. 34(3):257–273.

Anderson SP, Foros Ø, Kind HJ (2019) The importance of consumer multihoming (joint purchases) for market performance: Mergers and entry in media markets. J. Econom. Management Strategy 28(1):125–137.

Anderson EG, Parker GG, Tan B (2014) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25(1):152-172

Banerji A, Dutta B (2009) Local network externalities and market segmentation. Internat. J. Indust. Organ. 27(5):605–614.

Campbell A (2013) Word-of-mouth communication and percolation in social networks. Amer. Econom. Rev. 103(6):2466–2498.

Casadesus-Masanell R, Halaburda H (2014) When does a platform create value by limiting choice? J. Econom. Management Strategy 23(2):259–293.

Cennamo C, Santalo J (2013) Platform competition: Strategic trade-offs in platform markets. Strategic Management J. 34(11):1331–1350.

Chen J, Guo Z (2014) New media advertising and retail platform openness. Preprint, submitted August 1, http://dx.doi.org/10 .2139/ssrn.2694073

Chen J, Fan M, Li M (2016) Advertising vs. brokerage model for online trading platforms. MIS Quart. 40(3):575–596.

Corts KS, Lederman M (2009) Software exclusivity and the scope of indirect network effects in the U.S. home video game market. Internat. J. Indust. Organ. 27(2):121–136.

Debruyne M, Moenaertb R, Grif<sup>fi</sup>nc A, Hartd S, Hultinke EJ, Robben H (2002) The impact of new product launch strategies on competitive reaction in industrial markets. J. Product Innovation Management 19(2):159–170.

Dennis S (2017) Unsustainable customer acquisition costs make much of ecommerce pro<sup>fi</sup>t proof. Forbes (August 31). https://www ,forbes.com/sites/stevendennis/2017/08/31/unsustainable -customer-acquisition-costs-make-much-of-ecommerce-pro<sup>fi</sup>t -proof/.

Dickey MR (2019) Ahead of IPO, Airbnb achieves pro<sup>fi</sup>tability for second year in a row. TechCrunch (January 15), https:// techcrunch.com/2019/01/15/ahead-of-ipo-airbnb-achieves -pro<sup>fi</sup>tability-for-second-year-in-a-row/

Economides N, Katsamakas E (2006) Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Sci. 52(7):1057–1071.

Esteves RB, Resende J (2016) Competitive targeted advertising with price discrimination. Marketing Sci. 35(4):576–587.

Franklin J (2019) Uber unveils IPO with warning it may never make a pro<sup>fi</sup>t. Reuters (April 11), https://www.reuters.com/article/usuber-ipo/uber-unveils-ipo-with-warning-it-may-never-make-a -pro<sup>fi</sup>t-idUSKCN1RN2SK.

Fudenberg D, Tirole J (1984) The fat-cat effect, the puppy-dog ploy, and the lean and hungry look. Amer. Econom. Rev. 74(2):361–366.

Galeotti A, Goyal S (2009) In<sup>fl</sup>uencing the in<sup>fl</sup>uencers: A theory of strategic diffusion. RAND J. Econom. 40(3):509–532.

Geroski PA (1995) What do we know about entry? Internat. J. Indust. Organ. 13(4):421–440.

Hann IH, Koh B, Niculescu MF (2016) The double-edged sword of backward compatibility: The adoption of multigenerational platforms in the presence of intergenerational services. Inform. Systems. Res. 27(1):112–130.

Hao L, Guo H, Easley RF (2017) A mobile platform’s inapp advertising contract under agency pricing for app sales. Production Oper. Management 26(2):189–202.

Hong Y, Pavlou PA (2017) On buyer selection of service providers in online outsourcing platforms for IT services. Inform. Systems Res. 28(3):547–562.

Huang P, Ceccagnoli M, Forman C, Wu DJ (2013) Appropriability mechanisms and the platform partnership decision: Evidence from enterprise software. Management Sci. 59(1):102–121.

Huang N, Burtch G, Gu B, Hong Y, Liang C, Wang K, Fu D, Yang B (2019) Motivating user-generated content with performance feedback: Evidence from randomized <sup>fi</sup>eld experiments. Management Sci. 65(1):327–345.

Iansiti M, Levien R (2004) The Keystone Advantage: What the New Dynamics of Business Ecosystems Mean for Strategy, Innovation, and Sustainability (Harvard Business School Press, Boston).

Jiang B, Srinivasan K (2016) Pricing and persuasive advertising in a differentiated market. Marketing Lett. 27(3):579–588.

Karakaya F, Yannopoulos P (2011) Impact of market entrant characteristics on incumbent reactions to market entry. J. Strategic Marketing 19(2):171–185.

Koh TK, Fichman M (2014) Multihoming users’ preferences for twosided exchange networks. MIS Quart. 38(4):977–996.

Kuang L, Huang N, Hong Y, Yan Z (2019) Spillover effects of <sup>fi</sup>nancial incentives on non-incentivized user engagement: Evidence from an online knowledge exchange platform. J. Management Inform. Systems 36(1):289–320.

Leduc MV, Jackson MO, Johari R (2017) Pricing and referrals in diffusion on networks. Games Econom. Behav. 104(July):568–594.

Lee E, Lee J, Lee J (2006) Reconsideration of the winner-take-all hy pothesis: Complex networks and local bias. Management Sci. 52(12):1838–1848.

Lee GM, Qiu L, Whinston AB (2016) A friend like me: Modeling network formation in a location-based social network. J. Management Inform. Systems 33(4):1008–1033.

Li Z, Agarwal A (2017) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s integration of Instagram. Management Sci. 63(10):3438–3458.

Liebowitz S (2002) Re-Thinking the Network Economy: The True Forces That Drive the Digital Marketplace (Amacom, New York).

Manshadi V, Misra S, Rodilitz S (2020) Diffusion in random networks: Impact of degree distribution. Oper. Res. 68(6): 1722–1741.

Niculescu MF, Wu DJ, Xu L (2018) Strategic intellectual property sharing: Competition on an open technology platform under network effects. Inform. Systems Res. 29(2):498–519.

Parker G, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10): 1494–1504.

Parker G, Van Alstyne MW, Jiang X (2017) Platform ecosystems: How developers invert the <sup>fi</sup>rm. MIS Quart. 41(1):255–266.

Qiu L, Rui H, Whinston AB (2014) The impact of social network structures on prediction market accuracy in the presence of insider information. J. Management Inform. Systems 31(1):145–172.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Ruiz-Aliseda F (2016) When do switching costs make markets more or less competitive? Internat. J. Indust. Organ. 47:121–151.

Suarez F (2005) Network effects revisited: The role of strong ties on technology selection. Acad. Management J. 48(4):710–720.

Sundararajan A (2007) Local network effects and complex network structure. B.E. J. Theoret. Econom. 7(1):1–37.

Tellis GJ, Yin E, Niraj R (2009) Does quality win? Network effects vs. quality in high-tech markets. J. Marketing Res. 46(2):135–149.

Thompson GL, Teng JT (1984) Optimal pricing and advertising policies for new product oligopoly models. Marketing Sci. 3(2):148–168.

Tian L, Vakharia AJ, Tan Y, Xu Y, (2018) Marketplace, reseller, or hybrid: A strategic analysis of an emerging e-commerce model. Production Oper. Management 27(8):1595–1610.

Tirole J (1988) The Theory of Industrial Organization (MIT Press, Cambridge, MA).

Tucker C (2008) Identifying formal and informal in<sup>fl</sup>uence in technology adoption with network externalities. Management Sci. 54(12):2024–2038.

Xu H (2018) Is more information better? An economic analysis of group-buying platforms. J. Assoc. Inform. Systems 19(11):1130–1144

Zhang C, Chen J, Raghunathan S (2018) Platform competition in ride sharing economy. Working paper, University of Texas at Dallas, Richardson, TX

Zhu F, Iansiti M (2012) Entry into platform-based markets. Strategic Management J. 33(1):88–106.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
