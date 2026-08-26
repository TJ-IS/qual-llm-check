---
otero_id: 28513
otero_key: "JU4SZ2U4"
title: "Overcoming the Coordination Problem in New Marketplaces via Cryptographic Tokens"
authors: "Yannis Bakos; Hanna Halaburda"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1157"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Overcoming the Coordination Problem in New Marketplaces via Cryptographic Tokens

Yannis Bakos,<sup>a,</sup>\* Hanna Halaburda<sup>a</sup>

<sup>a</sup> Stern School of Business, New York University, New York, New York 10012 \*Corresponding author

Contact: bakos@stern.nyu.edu, https://orcid.org/0000-0001-6778-6587 (YB); hhalaburda@gmail.com (HH)

Received: Revised: Accepted: <sup>April 11, 2022</sup>Published Online in Articles in Advance: August 24, 2022

https://doi.org/10.1287/isre.2022.1157

Copyright:

Abstract. We study the use of platform-speci<sup>fi</sup>c tradable cryptographic tokens to solve the coordination problem that is common in adopting new marketplaces. We show that certain characteristics of platform-speci<sup>fi</sup>c tokens—speci<sup>fi</sup>cally, their tradability, the ability of the platform to commit both to accept and to require these tokens in the future, and the ability to commit to a price and/or quantity schedule—can help overcome the coordination problem and can support equilibria favorable to the new marketplace. Compared with other mechanisms in the literature to address the coordination problem—such as subsidies of early users and promises of refunds or buybacks if the platform fails—platform-speci<sup>fi</sup>c cryptographic tokens are less likely to favor established or larger <sup>fi</sup>rms with established reputations and <sup>fi</sup>nancial resources. We <sup>fi</sup>nd that tokens allow a marketplace to trade off future revenue for present revenue, which then can be used to address the coordination problem. On the other hand, the ability to trade out of the platform results in a smaller future network and lower total pro<sup>fi</sup>t. Thus, if the new marketplace is not facing capital constraints, then the most pro<sup>fi</sup>table strategy is the traditional strategy to subsidize adoption. If the new marketplace is capital-constrained, however, as is often the case for new entrants and unproven technology applications, tokens can offer an alternative that is increasingly attractive as the cost of capital increases.

History: This paper has been accepted for the Information Systems Research Special Section on Market Design and Analytics.

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.1157.

Keywords: adoption of new marketplaces economics of IS ICOs blockchain platform adoption network effects

## 1. Introduction

The coordination problem in platform adoption refers to situations where the existence of network effects results in multiple equilibria, yet the most ef<sup>fi</sup>cient equilibrium may not be adopted. For instance, two equilibria may exist: one where the platform is successfully adopted, and the second where adoption fails; whereas adoption could offer higher social surplus, there could be failure to adopt because the potential participants do not coordinate their adoption decisions and individually decide not to adopt. The coordination problem is recognized in the platforms literature as an important potential market failure (e.g., Katz and Shapiro 1986; Fudenberg and Tirole 2000; Caillaud and Jullien 2001; 2003; Halaburda et al. 2020), and its economic signi<sup>fi</sup>cance has increased in recent years due to the increasing role of platforms in the economy. The literature has proposed a variety of strategies for platforms to address the coordination problem, such as subsidizing early adopters, or promising refunds if the platform should fail; these strategies, however, favor established <sup>fi</sup>rms with <sup>fi</sup>nancial resources and vested reputation.

In this paper, we propose that platform-speci<sup>fi</sup>c cryptographic “utility” tokens—tokens issued on a blockchain that are required to access the services of a platform—can provide a strategy to overcome the coordination problem that does not favor established <sup>fi</sup>rms. We show that at the cost of lower total pro<sup>fi</sup>ts, these utility tokens may allow platforms to bring forward expected revenue from future periods, and thus may enable new platforms that lack reputation or access to capital to overcome the coordination problem and enter a new market, which in turn can be bene<sup>fi</sup>cial for innovation and competition. In that sense, platform-speci<sup>fi</sup>c cryptographic tokens issued on a blockchain can “democratize the marketplace” and potentially promote more innovation and experimentation in markets with strong network effects.

This intertemporal transfer of revenue is possible because platform-speci<sup>fi</sup>c cryptographic tokens allow the following: (a) ef<sup>fi</sup>cient trading of these tokens on existing or new markets; (b) a credible commitment that tokens will both provide future access to the platform and be required for such access; and (c) commitment to a quantity and/or price schedule for issuing these tokens. Similar to subsidies, the tradable utility tokens help internalize the externality that early users create for later users by addressing the coordination problem. In order to focus on this, we take development of the new marketplace as given, and we model how it can use a tradable utility token to address the coordination problem in fostering adoption by potential users.

Platform-speci<sup>fi</sup>c tokens are typically issued in initial coin offerings (ICOs), which have emerged in recent years as an enabling mechanism for a variety of digital platforms utilizing blockchain technology in areas like distributed <sup>fi</sup>le storage, digital advertising, reading of radiology images, music distribution, and so forth. The common perspective on ICOs is that they provide an alternative to more traditional funding sources for project development (Lyandres et al. 2018), such as angel investors, venture capitalists, or crowdfunding venues like Kickstarter, with their growth attributed to advantages such as lower friction, wider reach, or regulatory arbitrage.<sup>1</sup>

The idea of <sup>fi</sup>rm-speci<sup>fi</sup>c tokens or currencies is not new;<sup>2</sup> however, in the past, platforms have not been able to use such instruments to address the coordination problem because they have an ex post incentive to erode the value of tokens in future periods; this they can achieve by refusing to accept them, making them harder to transfer and trade, or allowing platform access without them.<sup>3</sup> Developments in blockchain technology, cryptocurrencies, and smart contracts, however, have dramatically increased the capabilities and reduced the cost of token issuance.<sup>4</sup> For instance, such tokens can use the well-developed tools provided by blockchains, such as Ethereum, which include smart contracts and token standards like ERC-20.<sup>5</sup> Alternatively, platforms can issue utility tokens on a new blockchain; for instance, Filecoin, a platform for decentralized peer-to-peer <sup>fi</sup>le storage, operates its own independent blockchain with a native cryptocurrency (FIL) that functions as a utility token providing access to the services of the platform. This choice is typically dictated by the functionality requirements of the platform.

By using tools such as smart contracts,<sup>6</sup> a platform issuing platform-speci<sup>fi</sup>c “utility” tokens can credibly and ef<sup>fi</sup>ciently commit to accepting the issued tokens in the future, to requiring these tokens for future access to the platform, and to follow a certain price and/or quantity schedule in the future. This is not feasible with corresponding conventional instruments, at least not for a new entrant lacking substantial <sup>fi</sup>nancial resources and a reputation. As a result, platformspeci<sup>fi</sup>c digital tokens can assure early buyers that the value of the tokens will not be unduly diluted in future periods and thus make it possible for the platform to use these tokens to address the coordination problem.

In addition, digital cryptographic tokens can take advantage of a substantial infrastructure for issuing and trading digital tokens. ICOs are typically implemented as the sale of tokens on existing “host” blockchains, such as ERC-20 tokens on Etherium, even if the issuing platform plans to operate an independent blockchain and its utility token will be native on that blockchain. The ICO takes place at a given point in time (typically determined by a certain block in the host blockchain) as a series of transactions where buyers send funds to a smart contract, which in turn sends them the purchased tokens. The issuing platform can use this smart contract to implement any number of mechanisms to match supply and demand for its tokens.

Typically, the ICO tokens will be listed on an exchange before the event and traded on an “as issued” basis, or will be issued in offerings where either the price or the quantity is set by the platform. These mechanisms are quite ef<sup>fi</sup>cient, as they have low trading frictions and allow the ICO information to reach most potential buyers using a variety of social media and online information sites. Based on this process, we assume in our analysis that a market-clearing equilibrium is reached that matches demand and supply for tokens.<sup>8</sup>

In practice, the most common ICO mechanism is a posted token price (possibly with a target revenue amount), and can vary in the time it takes—for example, in the case of the BAT token ICO, which was mostly completed in three blocks on the Ethereum chain and which lasted under a minute;<sup>9</sup> in the case of Filecoin’s FIL token, the ICO lasted about a month and utilized a complex price formula, with late buyers paying a higher price than early buyers.<sup>10</sup> Other ICOs let the price be determined through an auction of a given quantity of tokens or raise a given amount of revenue— for instance, the Gnosis ICO (GNO token) used a Dutch auction to raise its target revenue of 250,000 ETH in less than 15 minutes.<sup>11</sup> If a posted price ICO reveals an imbalance between supply and demand, then there are often additional offerings to alleviate that imbalance.

Once distributed via the ICO, tokens typically begin trading in exchanges that specialize in cryptocurrencies and tokens. There are hundreds of such exchanges, both traditional centralized ones that broker the transactions between buyers and sellers, such as Binance, Coinbase, Kraken, Bit<sup>fi</sup>nex, FTX, and so forth, or decentralized ones that allow peer-to-peer trading such as Uniswap, 0x, and Compound. Two important characteristics in the microstructure of these exchanges is that it is common for popular cryptographic tokens to be traded on many exchanges,<sup>12</sup> and these exchanges typically make public their entire order book, thus providing transparency and facilitating the assessment of liquidity away from the current price (i.e., the depth of the market).<sup>13</sup> For these reasons, we assume that subsequent trading of tokens also reaches a market-clearing equilibrium that matches supply and demand.<sup>14</sup>

Although tokens can help address the coordination problem, our analysis shows that if the new marketplace is not facing capital constraints, then it is more pro<sup>fi</sup>table to employ the traditional strategy of subsidizing adoption. If the new marketplace is capitalconstrained, however, then token issuance provides an alternative that is increasingly attractive as the cost of capital increases. With tokens, the new marketplace faces a reduced need to subsidize early adopters or may avoid such a subsidy altogether: the sale of tokens that allow future use of the platform—when such use will no longer be subsidized—provides a mechanism to trade off future revenue for present reving the coordination problem. In that sense, even pure utility tokens<sup>16</sup> have certain characteristics of equity: early adopters share the future gains if the platform succeeds and the tokens provide an alternative when more traditional <sup>fi</sup>nancing, such as venture capitalists or the capital markets, would be too costly or not available to the platform.

For instance, the decentralized <sup>fi</sup>le storage platform created by Filecoin requires a utility token (FIL) in order to utilize the platform, either to store one’s <sup>fi</sup>les (when FIL is used to pay for this service), or to make one’s disk space available for use by the platform (when FIL is used to post a bond, released when the information stored in that disk space is successfully retrieved by the platform). A user can participate in both of these capacities at the same time, and Filecoin’s model relies on having a large number of users and thus is strongly dependent on network effects. Without the FIL token, substantial subsidies might be required to solve the coordination problem and entice enough early users to join so that the platform could realize adequate network effects and bootstrap itself into a functional state. Our analysis shows that by allowing potential users to purchase digital tokens whose value would increase in the event the new platform succeeds, it might be possible to address the coordination problem without subsidies, which is what happened in Filecoin’s case. Since new marketplaces may <sup>fi</sup>nd it dif<sup>fi</sup>cult to raise capital from traditional sources due to the uncertainties of their coordination problem, issuing a utility token may provide a valuable alternative.<sup>17</sup>

After this introduction, the paper is organized as follows. Section 2 reviews the related literature. Section 3 introduces our setting, develops our model for platform adoption, and demonstrates the coordination problem. Section 4 solves for the equilibria when the platform employs tradable utility tokens and compares the resulting outcomes with the benchmark of strategies such as subsidies or buyback promises that do not depend on digital tokens. Section 5 compares the two regimes, and Section 6 discusses our results and offers concluding remarks. The Appendix provides a summary of our notation. Online Appendix A shows the analysis for the benchmark cases with no tokens, and the remaining online appendices contain proofs and certain extensions.

## 2. Related Literature

The multiplicity of equilibria and the corresponding coordination problem is a well-known issue for markets with network effects, going back to the seminal paper of Katz and Shapiro (1986). For instance, in a peer-to-peer marketplace with network effects, a user’s utility increases as more users join the marketplace. As a result, potential users want to join the same marketplace as other users, and thus multiple outcomes can constitute an equilibrium as long as potential users coordinate on the same one. Thus, a potential user may forgo joining an otherwise attractive network if he does not believe that other potential users will join as well, or the user may join a network he otherwise wouldn’t because he believes that will be the choice of other users.

The coordination problem faced by new marketplaces thus applies more generally to platforms, as they tend to be characterized by network effects. The economics literature has long recognized that platforms are strategic players and can use attractive pricing to overcome unfavorable beliefs when they try to entice potential users to adopt, or when they compete against other platforms (e.g., Caillaud and Jullien 2001; 2003; Hagiu and Spulber 2013). If the setting is dynamic, then a low or negative early price (i.e., a subsidy) is a frequently explored strategy to overcome the coordination problem (e.g., Halaburda et al. 2020).<sup>18</sup>

In this paper, we study the coordination problem facing new marketplaces in the context of cryptographic tokens and ICOs. There is a rapidly growing literature on ICOs, but most of it is not concerned with their role in settings with network effects. For example, Howell et al. (2020) provide a comprehensive overview of ICOs characteristics, and investigate the relations between these characteristics and the success of ICOs. Chod and Lyandres (2021) consider agency problems that may arise when funding venture with tokens. Malinova and Park (2018) analyze optimal contact structure when funding venture with tokens. Lyandres et al. (2018) investigate the dynamics of token prices, and compare them to securities. Lee and Parlour (2022) show how ICO-issued tokens can result in more ef<sup>fi</sup>cient project funding than crowdsourcing by enabling ef<sup>fi</sup>cient secondary trading of funder rewards. Bakos and Halaburda (2019) illustrate how ICOs may help crowdsource certain aspects of due diligence when funding new projects.

There is also a nascent literature on cryptographic tokens in platform settings. Catalini and Gans (2018) focus on discovering demand. Sockin and Xiong (2020) and Cong et al. (2018) analyze the drivers of token prices. Gan et al. (2021a) consider ICOs as a form of crowdfunding backed by future assets like inventories and propose optimal ICO designs for both equity and utility tokens. Sockin and Xiong (2022) and Chod et al. (2022) study implications of platformspeci<sup>fi</sup>c cryptographic tokens for platform <sup>fi</sup>nancing and governance. Mayer (2019) analyzes a platform setting with risk-averse users, less-risk-averse speculators, and settings with varying volatility; although he recognizes the existence of multiple equilibria, he does not consider the coordination problem and focuses on the case of successful platform adoption. Gan et al. (2021b) study the implications of “uncapped” platform ICOs that do not restrict token supply as a funding mechanism; they focus on dilution risk and do not consider the coordination problem, assuming the platforms will be adopted.

Network effects are central in Sockin and Xiong (2020) and Cong et al. (2018). In these analyses, however, the platform is not a strategic player, and thus they do not address the question under what circumstances the platform would prefer to overcome the coordination problem by issuing a token rather than with a traditional user subsidy. Moreover, the coordination issue is not a problem in their settings, as these papers assume that in the case of multiple equilibria the users will coordinate on the ef<sup>fi</sup>cient equilibrium. Shakhnov and Zaccaria (2020) provide empirical evidence that ICOs are more likely in settings with value from network effects—but they also do not consider the coordination problem.

Catalini and Gans (2018) focus on the role of tokens in demand discovery, but they also discuss the possibility to use ICOs to address the coordination problem in a setting with network effects. In their model, tokens are auctioned off, as opposed to the platform setting the token price, as is the case in our setting. In their model, the auction process changes the adoption game from simultaneous to sequential, and, as a result, the ICO process can eliminate the coordination problem. The coordinating role of tokens in that setting depends on a large-enough stand-alone value of the product or service offered by the platform; and on the ex ante heterogeneity of users, which leads to sequential increase in demand. In their setting, tokens would not solve the coordination problem for ex ante homogeneous users or for pure network goods, that is, goods (or services) that have no value if no other user adopts.

Li and Mann (2017) consider how platform-speci<sup>fi</sup>c tokens help overcome the coordination problem in platform adoption by changing the timing of the game.<sup>19</sup> They consider a two-sided market with a single potential user on each side. The platform offers tokens to each side in turn, and purchase of a platform speci<sup>fi</sup>c token allows each side’s commitment to trade on the platform to be observed by the other side; this effectively transforms the setting into a sequential game and resolves the coordination problem for adoption across the two sides. For that mechanism to work, the platform must be able to separately target the potential users on each side. The coordination problem reappears within each side if there are multiple potential users for that side. In this case, Li and Mann (2017) implicitly follow the literature and assume the market coordinates on the ef<sup>fi</sup>cient equilibrium for each side when multiple equilibria are available.

Mechanisms like the ones in Catalini and Gans (2018) and Li and Mann (2017) illustrate an important aspect of tokens, namely, the ability to make token purchases (which, in the case of platform-speci<sup>fi</sup>c tokens, correspond to adoption decisions) observable by market participants—sometimes referred to as “transparency.” This transparency can affect the resulting equilibria by changing the information structure and therefore the sequence of moves, and this can eliminate the coordination problem in certain settings.

Our work is complementary to the aforementioned literature, as we focus on different characteristics of tokens—their tradability and supply commitment. We show that tradability makes tokens a valuable tool in overcoming coordination problem, even if the information about token purchases is missing or not reliable (i.e., they lack transparency). Distinguishing the impact of different features of cryptographic tokens, such as tradability and transparency, in addition to its theoretical interest can have practical implications. Since these tokens are programmable, it is possible to design them with customized features, and thus take advantage of an understanding of the contexts in which particular features are valuable, and the bene-<sup>fi</sup>ts they provide.

Furthermore, while some existing literature leverages the heterogeneity of potential users to transform platform adoption into a sequential game, our approach allows a new marketplace to overcome the coordination problem, even when potential users are exante identical and move simultaneously in response to its introduction. We <sup>fi</sup>nd that the coordination problem can be overcome because of the tradability of tokens even when direct subsidies are infeasible or too costly. Tokens offer the early potential users a stake in the success of the new marketplace and make it more attractive for them to join, and their joining makes it more likely for the marketplace to indeed succeed. We derive conditions under which the marketplace prefers to issue a tradable token to solve the coordination problem, and we show that under certain circumstances a traditional user subsidy may be more pro<sup>fi</sup>table for the platform than issuing tokens.

## 3. Model

## 3.1. Model Setup

We focus on overcoming the coordination problem for a new marketplace; as discussed above, this problem appears whenever the potential users make independent decisions on whether to join, which applies generally to new platforms that offer a good or service with network effects. We focus on cryptographic tokens as a strategy to address the coordination problem in adoption by potential users, and we compare the issuance of cryptographic tokens to traditional price-based strategy options such as subsidizing early adopters or buyback promise.

We consider a basic setting with a one-sided new marketplace (or platform) and network effects that may result in a coordination problem—an example would be a peer-to-peer marketplace like the Filecoin Network, where the participants may utilize or provide decentralized storage, or do both at the same time. We assume that the marketplace has already been developed or that we do not need to be concerned about development and implementation risk,<sup>20</sup> and we focus on whether it will succeed in being adopted by potential users that arrive in two periods, which we denote by t 1, 2. We use the terms “new marketplace” and “platform” interchangeably, as our setting and analysis equally apply to platforms with network effects that face a coordination problem.

In each period, $n _ { t }$ potential users arrive (t <sub>-</sub> 1, 2). Whereas these potential users are ex ante identical, they differ in terms of their realized utility from the new marketplace, which is determined by their type k. Users learn their type only after experiencing the marketplace for one period. The type k is distributed with a continuous probability density function g(k) on support A, B , with the corresponding utility $u _ { k } ( \omega )$ weakly decreasing in k for any marketplace size ω. The type distribution is the same for users that arrive in either period.<sup>21</sup>

Potential users that arrive in period 1 choose in each period between joining the platform and some outside option that we normalize at zero utility. If they join the platform in period 1, then they have the option to leave in period 2 after observing their realized utility from the platform and thus learning their type; they will do so if staying in the platform, for period 2 offers lower expected utility than their outside option. Potential users that arrive in period 2 can choose between joining the platform at t 2 and the zero-utility outside option.

The utility of potential users from joining the platform exhibits network effects that are concave in the size of the network; that is, for network sizes $\omega$ and $\omega ^ { \prime } ,$ if $\omega > \omega ^ { \prime } .$ , then $u _ { k } ( \omega ) > u _ { k } ( \omega ^ { \prime } )$ and $u _ { k } ( \omega + \omega ^ { \prime } ) <$ $u _ { k } ( \omega ) + u _ { k } ( \omega ^ { \prime } )$ for all types $k . ^ { 2 2 }$ Furthermore, to make the coordination problem nontrivial, we assume that $E _ { k } [ u _ { k } ( 0 ) ] < 0$ and $E _ { k } [ u _ { k } ( n _ { 1 } ) ] > 0 ;$ ; that is, joining an empty platform yields on expectation negative utility $( \mathrm { e . g . }$ , due to the adoption cost), and joining a successful platform yields on expectation positive utility.

Digital Tokens. To analyze the adoption of tokens in our setting, we assume that platform access requires possession of a digital token issued by the platform. Tokens can be purchased in each period, and they provide access to the platform for all remaining periods.<sup>23</sup> Importantly, tokens are transferable. Potential users that arrive in period 2, or arrived in period 1 but did not join the platform then, can join the platform at t <sub>-</sub> 2 by acquiring a token directly from the platform or by purchasing it from another user that acquired the token at t 1 and decides to exit the market at $t = 2 .$ Alternatively, these users can choose the zero-utility out side option for t 2.

The platform credibly commits that the digital tokens it issues will provide access to the platform in both peri ods, and also will be required for such access; it may also commit to speci<sup>fi</sup>c price or quantity schedules for the tokens. A key bene<sup>fi</sup>t of cryptographic utility tokens compared with similar contractual or marketing promises is that employing blockchain and smart contract technologies to issue the tokens and design the platform can assure the credibility and enforceability of these commitments.

## 3.2. The Coordination Problem

Multiple Equilibria. Due to the negative utility of joining an unsuccessful platform and the positive utility of joining a successful platform, a potential user wants to join if he believes that the other potential users will also join, and he does not want to join if he believes that others will not join. This results in multiple equilibria for a broad range of prices set by the platform: since potential users are ex ante identical in beliefs and utility, pure-strategy equilibria entail either all potential users deciding to join (which we term adopting) or deciding not to join (which we term not adopt ing).<sup>24</sup> We de<sup>fi</sup>ne a corresponding success variable $s _ { t } \in \{ 0 , 1 \}$ , with 0 denoting failed adoption and 1 denoting successful adoption.

The multiplicity of equilibria means that the equilibrium outcome depends on the beliefs of the potential users, which creates the associated coordination problem. This is a common result in platform adoption settings, such as format wars: if potential users believe that a particular format will win, then this belief will become a self-ful<sup>fi</sup>lling prophecy and the favored format will win, as no potential user wants to be stranded with the losing format (see, e.g., McIntyre 2009 for the BluRay vs. HD-DVD format war for high-de<sup>fi</sup>nition optical disks). These beliefs of potential users may be formed based on the history of successes and failures of a platform itself, the reputation of the platform developer, marketing of the platform, expert opinions, or other sources of information.<sup>25</sup>

Focality. In coordination games, players’ beliefs frequently result in one equilibrium being more salient than others, a concept known as focality (Schelling 1960). A focal point represents the equilibrium of a coordination game that the players tend to choose by default, in the absence of communication and only based on the features of the game. Focality has been used to address selection among the multiple possible equilibria in the context of platform adoption and platform competition (Fudenberg and Tirole 2000; Caillaud and Jullien 2001; 2003).<sup>26</sup> Like our setting, when a platform enters a market with network effects, frequently there are two equilibria for potential users: adopting or not adopting; in these cases, focality can help determine the resulting outcome.

Let $V ( s _ { t } )$ denote the expected bene<sup>fi</sup>t of joining the platform when the adoption success is $s _ { t } ,$ and consider the case where, like our setting, the utility of joining the platform when everyone else also adopts is positive, that is, $V ( 1 ) > 0$ , and the utility of joining when nobody else adopts be negative, that is, $V ( 0 ) < 0$ Unsurprisingly, the adoption outcome depends on the price the platform charges for access. At price $p \le V ( 0 )$ , it is a dominant strategy for all users to join, and thus adoption is assured. At price $p > V ( 1 )$ , it is a dominant strategy not to join, and thus adoption will fail. Any price p that falls between V(0) and V(1) generates two pure-strategy Nash equilibria: one in which all potential users adopt, and one in which no one adopts. Whether the platform is adopted depends on the price as well as the beliefs of the potential users.

If every user believes that all other users join at any price $p \leq V ( 1 )$ , then the platform will be adopted by all users even if it charges V(1). (This is equivalent to beliefs favorable toward platform adoption in Caillaud and Jullien 2001; 2003.) Conversely, if every user believes that no other users join at price $p > V ( 0 )$ , then the platform is not adopted by any user at price $p = V ( 0 ) + \epsilon ,$ , whereas it is adopted by all users when $p = V ( 0 )$ . (This is equivalent to beliefs unfavorable toward platform adoption in Caillaud and Jullien 2001; 2003.) In both these cases, at equilibrium, beliefs must be commonly known, as well as ful<sup>fi</sup>lled.<sup>27</sup>

However, beliefs other than the two types described above are possible at equilibrium. Speci<sup>fi</sup>cally, for any price $P \in \hat { [ V ( 0 ) , V ( 1 ) ] }$ , if every user believes that all other users join at price $p \leq P$ and no other user joins at price $p > P ,$ , then these beliefs are sustainable at equilibrium. Each user’s best response to such beliefs is to join the platform if the price is $p \leq P$ and not join if the price is $p > P ,$ and thus the beliefs are ful<sup>fi</sup>lled at equilibrium. As before, the beliefs need to be commonly known and they can be formed based on public signals, such as reviews on popular sites or advertising campaigns.

Such equilibrium beliefs with threshold $P \in [ V ( 0 ) ]$ V 1 are related to the concept of partial focality from Halaburda and Yehezkel (2016; 2019).<sup>28</sup> The parameter P is a proxy for the extent of focality of the adopting equilibrium. As P increases, adopting the platform is a more focal equilibrium. Conversely, as P decreases, adopting the platform is less focal. For ease of exposition and convenience of computation, it is useful to de<sup>fi</sup>ne $\begin{array} { r } { \alpha = \frac { P - V ( 0 ) } { V ( 1 ) - V ( 0 ) } \in [ 0 , 1 ] } \end{array}$ , which we call degree of focality.

For the extreme cases of $\alpha = 1$ and $\alpha = 0$ , we have full focality of adopt and not adopt respectively, as in the speci<sup>fi</sup>cations of Fudenberg and Tirole (2000) and Caillaud and Jullien (2001; 2003). As mentioned earlier, when the platform enjoys full focality of adopting equilibrium, all users join at any price $p \leq V ( 1 )$

Several papers on platform competition, such as Fudenberg and Tirole (2000), assume that the market will coordinate on the equilibrium with adoption, and thus the platform will enjoy full focality of adoption. This approach, however, essentially assumes away the coordination problem that platforms face. Instead, we use the concept of partial focality with a corresponding degree parameter $\alpha ,$ which allows us to do comparative statics with respect to this parameter. The resulting outcome for the platform can be determined by the focality of different adoption equilibria.

The focality of degree α can be interpreted as the ex ante con<sup>fi</sup>dence that the market places on the platform and consequently how appealing it needs to be to its potential users in order to overcome the coordination problem. The degree of focality may be higher for larger and well-established players entering new markets, and lower for unknown entrants with new technologies. Given that history may affect this trust, the degree of focality in the second period $( \alpha _ { 2 } )$ may be affected by the outcome of the <sup>fi</sup>rst period. Whereas for simplicity we assume that $\alpha _ { 2 }$ does not depend on the period 1 outcome, our results are not changed if we allow $\alpha _ { 2 }$ to be a function of success at $t = 1 ,$ , for example, $\alpha _ { 2 } ( s _ { 1 } = 1 ) > \alpha _ { 1 }$ if the platform succeeds in period 1 and $\alpha _ { 2 } ( s _ { 1 } = 0 ) < \alpha _ { 1 }$ if the platform fails in period 1.<sup>29</sup>

## 4. Coordination with Digital Tokens

We now analyze the use of digital tokens to address the coordination problem. We later compare the resulting outcomes with the benchmark case when no digital tokens are used, which is formally analyzed in Online Appendix A. As discussed more extensively in the introduction, we assume a market-clearing equilibrium matching the demand for tokens by potential users with the supply of tokens from either the platform (in the <sup>fi</sup>rst period) or both the platform and the exiting users (in the second period).

## 4.1. Timing of the Game

In each period $t = 1 , 2 ,$ there are $n _ { t }$ potential users that arrive to the market and can decide to join the platform in that period, a later period, or not at all. Upon joining the platform, users learn their type k and realize their utility. Let $\omega _ { t }$ denote the size of the network, that ${ \mathrm { i s } } ,$ users on the platform, in period t. Users who joined the platform in period 1 realize the utility $u _ { k } ( \omega _ { 1 } )$ , and subsequently may choose to leave the platform in period 2 or stay on.

In each period, the platform sells tokens that are required to access its services for the present and any future periods; users that acquire a token at t 1 can either use it to access the platform at $t = 2 ,$ or can sell that token to another potential user. Thus, potential users that wish to join the platform in the second period may acquire a token either directly from the platform, or from another user that decides to leave the platform. The detailed timeline and related agent decisions are shown in Figure 1. We use the superscript T to denote equilibrium variables when the platform uses tokens to overcome the coordination problem, and NT to denote equilibrium variables when no tokens are used and the platform relies on a subsidy in period 1—the comparative analysis for the NT case is presented in Online Appendix A.

The timing is as follows:

Period 1: $\mathrm { A t } \ t = 1 , n _ { 1 }$ potential users arrive to the market, the adopt focality is $\alpha _ { 1 } ,$ the platform offers tokens for sale at price $p _ { 1 } ,$ , and the potential users decide whether to buy a token and join the platform.<sup>30</sup> At the end of period 1, everybody observes whether the $n _ { 1 }$ potential users joined the platform, which determines the value of $s _ { 1 } \in$ $\{ 0 , 1 \}$ with a successful adoption denoted by $s _ { 1 } = 1$ . Users that joined the platform learn their type k and realize benefit $u _ { k } ( \omega _ { 1 } )$ from participating in the period 1 network.

Period 2: $\mathrm { A t } t = 2 , n _ { 2 }$ new potential users arrive to the market, the adopt focality is $\alpha _ { 2 } ,$ the platform releases $\tau _ { 2 }$ additional tokens to the market, users that joined at t 1 decide whether to stay for t 2 or leave the platform and sell their token to the new arrivals, and potential users without a token decide whether to buy a token and join the platform. At the end of period $^ { 2 , }$ users that joined the platform at $t = 2$ learn their type k and realize bene<sup>fi</sup>t $u _ { k } ( \omega _ { 2 } )$ from participating in the period 2 network; users of type k that stayed from the <sup>fi</sup>rst period also realize bene<sup>fi</sup>t $u _ { k } ( \omega _ { 2 } )$

Users that joined in period 1 decide whether to stay for period 2 based on their expected bene<sup>fi</sup>t from staying compared with the price at which they can sell their token. Users that do not have a token at the beginning of period 2 decide at what price they are willing to buy one based on the focality $\alpha _ { 2 } .$ . If period 1 adoption was successful, that is, $s _ { 1 } = 1$ , given <sup>fi</sup>rst- and second-period arrivals $n _ { 1 }$ and $n _ { 2 }$ and the number of tokens $\tau _ { 2 }$ offered by the platform in the second period, the demand for tokens will be either for all $n _ { 2 }$ new arrivals or for none, depending on the price $p _ { 2 } .$ The token supply in period 2 is determined by the tokens offered by the platform and the tokens for sale by exiting period 1 users, which in turn depends on $n _ { 1 } .$ . The market clears at price $p _ { 2 } ( \tau _ { 2 } | n _ { 1 } , n _ { 2 } )$ that matches token demand and supply.

Figure 1. (Color online) Game Timeline for Coordination with Digital Tokens  
![](/api/attachments/JU4SZ2U4/fulltext/images/b75da6aedd3cc5ac60e35bacd49cb1d1d4b7d7cac14eac96523e774a2a81063d.jpg)  
Note. Events in braces occur simultaneously.

The market-clearing price may be higher or lower than $p _ { 1 } ;$ early adopters that realize an unfavorable type $k ,$ and thus get low bene<sup>fi</sup>t from joining the platform, will sell their tokens in period 2 even if $p _ { 2 } ( \tau _ { 2 } | n _ { 1 } , n _ { 2 } ) < p _ { 1 }$ . Potential users in period 1 will purchase even if they expect the token price to decrease in period 2 because they expect to bene<sup>fi</sup>t from having joined the platform in the <sup>fi</sup>rst period. These users will exit and sell their token in period 2 if they realize an unfavorable type, and this possibility provides some insurance against a poor <sup>fi</sup>t with the platform.

At equilibrium, the platform sets a second-period token price $P _ { 2 } ^ { \hat { T } } ( s _ { 1 } = 1 | \alpha _ { 2 } , n _ { 1 } , \hat { n } _ { 2 } )$ that maximizes its revenue, up to the price threshold for adoption determined by the degree of focality $\alpha _ { 2 } ,$ as a higher price will result in failed period 2 adoption. If this threshold, and thus the maximum price $\hat { P } _ { 2 } ^ { T } ( s _ { 1 } = 1 | \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$ for successful period 2 adoption, is negative, which is allowed by our assumptions, then even though the platform was successful in the <sup>fi</sup>rst period, there will be no demand for tokens in the second period at a nonnegative price. Since the platform will not subsidize adoption in the second period, there will be no viable resale market, and in this case the platform will get no bene<sup>fi</sup>t from introducing tokens.

If period 1 adoption failed, that is, $s _ { 1 } = 0$ , then there are no tokens available for resale in period 2 and the equilibrium variables in the second period take the same values whether the platform addresses the coordination problem by issuing tokens or providing a subsidy.<sup>31</sup> This allows us to simplify the notation and use $P _ { 2 } ^ { T }$ to denote $P _ { 2 } ^ { T } ( s _ { 1 } = 1 | \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$

In the following analysis, we characterize settings with a potential resale market in period 2; then, for such settings, in Section $5 ,$ we compare using tokens to resolve the coordination problem to a <sup>fi</sup>rst-period subsidy.

## 4.2. Equilibrium with Tokens

We solve for the equilibrium using backward induction, starting with period 2. Given successful adoption in the <sup>fi</sup>rst period $( s _ { 1 } = 1 )$ , we consider how the market-clearing price changes as the platform increases the tokens $\tau _ { 2 }$ offered in period 2.

Some period 1 adopters after learning their type k may obtain a negative utility from staying in the platform even if the $n _ { 2 }$ new arrivals adopt, and thus prefer the zero-value outside option to staying in the platform for the second period. We denote the fraction of these period adopters by $\lambda ^ { N T }$ because they would also leave the network after the <sup>fi</sup>rst period in the setting without tokens, hence the superscript $N T . ^ { 3 2 }$ Leaving in the second period may be relatively more attractive with tradable tokens; thus, at least $\lambda ^ { N T } n _ { 1 }$ period 1 users will leave the platform in period $^ { 2 , }$ and the size of the network in the second period cannot be larger than $n _ { 2 } + \left( 1 - \lambda ^ { N T } \right) n _ { 1 }$ . If at $t = 2$ the platform issues new tokens $\tau _ { 2 } \leq n _ { 2 } - \lambda ^ { N T } n _ { 1 }$ and adoption succeeds, then the size of the network at $t = 2$ is limited to $n _ { 1 } + \tau _ { 2 }$ . If period 2 adoption fails, then there is no secondary market for tokens of the exiting users, $n _ { 1 } \lambda ^ { N T }$ period 1 users leave, and the resulting network size in the second period is $( 1 - \lambda ^ { N T } ) n _ { 1 }$ . Period 2 potential users are willing to join the platform by purchasing a token at price $p _ { 2 } \leq P _ { 2 } ( \tau _ { 2 } , s _ { 1 } = 1 \mid \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$ , where the price threshold depends on the availability of the new tokens:

$$
\begin{array}{l} P _ {2} (\tau_ {2}, s _ {1} = 1   |   \alpha_ {2}, n _ {1}, n _ {2}) \\ = \left\{ \begin{array}{l l} \alpha_ {2} E _ {k} [ u _ {k} (n _ {1} + \tau_ {2}) ] + (1 - \alpha_ {2}) E _ {k} [ u _ {k} (n _ {1} (1 - \lambda^ {0})) ], & \text {when} \tau_ {2} \leq n _ {2} - \lambda^ {N T} n _ {1}, \\ \alpha_ {2} E _ {k} [ u _ {k} (n _ {2} + n _ {1} (1 - \lambda^ {N T}) ] + (1 - \alpha_ {2}) E _ {k} [ u _ {k} (n _ {1} (1 - \lambda^ {0})) ], & \text {when} \tau_ {2} > n _ {2} - \lambda^ {N T} n _ {1}, \end{array} \right. \end{array}\tag{1}
$$

where $\lambda ^ { 0 }$ is the fraction of period 1 users that leave the platform if adoption in the second period fails, which is the same whether the platform issues tokens or not, as in that case no tokens are traded in period 2.

In order to improve readability and focus on the platform’s decision variable $\tau _ { 2 } ,$ in the rest of our analysis we omit from our notation the variables $\alpha _ { 2 } , n _ { 1 } ,$ and $n _ { 2 } ,$ as well as the condition $s _ { 1 } = 1$ , and we use $P _ { 2 } ( \tau _ { 2 } )$ and $p _ { 2 } ( \tau _ { 2 } )$ to denote $P _ { 2 } ( \tau _ { 2 } , s _ { 1 } = 1 | \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$ and $p _ { 2 } ( \tau _ { 2 } | n _ { 1 } , n _ { 2 } ) . ^ { 3 3 }$ All our results apply to a given setting with parameters $\left( n _ { 1 } , n _ { 2 } , \alpha _ { 1 } , \alpha _ { 2 } \right)$

If the platform offers for sale $\tau _ { 2 }$ tokens in period $^ { 2 , }$ then the market-clearing price $p _ { 2 } ( \tau _ { 2 } )$ is determined by the willingness to pay for a token of the new arrivals, and the willingness to sell of the period 1 users. For given $\tau _ { 2 } \geq 0$ and $_ { p _ { 2 } , }$ period 1 users with unfavorable enough type $k > k ( \tau _ { 2 } , p _ { 2 } )$ are willing to sell, where the threshold type $k ( \tau _ { 2 } , p _ { 2 } )$ <sub>)</sub> is characterized by<sup>34</sup>

$$
\begin{array}{r l} u _ {k (\tau_ {2}, p _ {2})} (n _ {1} + \tau_ {2}) = p _ {2} & \text {for} \tau_ {2} \leq n _ {2} - \lambda^ {N T} n _ {1}, \\ u _ {k (\tau_ {2}, p _ {2})} (n _ {2} + (1 - \lambda^ {N T}) n _ {1}) = p _ {2} & \text {for} \tau_ {2} > n _ {2} - \lambda^ {N T} n _ {1}. \end{array}\tag{2}
$$

Let $\begin{array} { r } { \lambda ( \tau _ { 2 } , p _ { 2 } ) = \int _ { k ( \tau _ { 2 } , p _ { 2 } ) } ^ { B } g ( k ) } \end{array}$ dk be the fraction of period 1 users with unfavorable-enough type so they prefer to sell; then, given $\tau _ { 2 } ,$ the additional supply of tokens at price $p _ { 2 }$ from the exiting period 1 users is $\lambda ( \tau _ { 2 } , p _ { 2 } ) n _ { 1 }$ Holding τ<sub>2</sub> constant and increasing $p _ { 2 }$ makes selling their token and leaving the platform attractive to a broade range of types; thus, $\lambda ( \tau _ { 2 } , p _ { 2 } )$ increases. Holding $p _ { 2 }$ constant and increasing τ makes staying in the platform relatively more attractive, and thus $\lambda ( \tau _ { 2 } , p _ { 2 } )$ decreases.

All $n _ { 2 }$ period 2 users will buy a token at price $p _ { 2 } \leq P _ { 2 } ( \tau _ { 2 } )$ . Since the platform offers $\tau _ { 2 }$ tokens, there is demand for $n _ { 2 } - \tau _ { 2 }$ tokens from the exiting period 1 users. The market-clearing price $p _ { 2 } ( \tau _ { 2 } )$ is the price at which the demand and supply on the secondary market match; the corresponding market-clearing condition is $\lambda ( \tau _ { 2 } , p _ { 2 } ( \tau _ { 2 } ) ) \cdot n _ { 1 } = n _ { 2 } - \tau _ { 2 } ,$ , with $p _ { 2 } ( \tau _ { 2 } ) \leq P _ { 2 } ( \tau _ { 2 } )$

If the above market-clearing condition results in a negative or zero token price for period 2, then there will be no viable resale market in period 2, and the platform will not bene<sup>fi</sup>t from issuing tokens. $\mathrm { W e }$ are thus interested in the conditions for a setting to support a viable resale market, that is, a strictly positive token price in the second period. It turns out that the equilibrium for the case without tokens allows us to characterize whether a viable resale market will exist in the case the platform issues tradable tokens. Speci<sup>fi</sup>- cally, it follows from Equations (1) and (2) that $\mathop { \mathrm { ~ \widehat { ~ } ~ } } { P _ { 2 } ^ { N T } } >$ 0 and $n _ { 2 } > n _ { 1 } \lambda ^ { N T }$ are necessary conditions for a viable resale market, where $P _ { 2 } ^ { N T }$ denotes the second-period price threshold in the equilibrium without tokens and successful adoption in period 1; that is, $s _ { 1 } = 1 . ^ { 3 5 }$ If $P _ { 2 } ^ { N T } > 0$ does not hold, then potential users arriving in period 2 are not willing to pay a positive price for access, and if $n _ { 2 } > n _ { 1 } \lambda ^ { N \widetilde { T } }$ does not hold, then the exiting users are not fully replaced by new arrivals, and thus supply of tokens would exceed demand at any positive price. We focus our analysis on settings with a potential resale market, $\scriptstyle \mathrm { a s } ,$ , otherwise, issuing tokens brings no bene<sup>fi</sup>t to the platform.<sup>36</sup>

Definition 1. A setting $( \alpha _ { 1 } , \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$ offers a potential resale market when $P _ { 2 } ^ { N T } > 0$ and $n _ { 2 } > \lambda ^ { N T } \dot { n _ { 1 } }$

The conditions for a viable resale market assure that the platform can offer a quantity of tokens $\tau _ { 2 }$ with $0 <$ $\tau _ { 2 } < n _ { 2 } - \lambda ^ { N T } n _ { 1 }$ and face a positive adoption threshold price $P ( \tau _ { 2 } ) > 0$ . If the platform offers a small-enough quantity of tokens $\tau _ { 2 }$ so that $\lambda ( \tau _ { 2 } , P _ { 2 } ( \tau _ { 2 } ) ) \cdot n _ { 1 } < n _ { 2 } - \tau _ { 2 } ,$ then the market-clearing price is $p _ { 2 } ( \tau _ { 2 } ) = P _ { 2 } ( \tau _ { 2 } )$ , the highest price that the new arrivals are willing to pay and still join. At this price, however, there are too few period 1 users willing to sell and some of the new potential users are left without a token. Thus, the platform will increase $\tau _ { 2 } ,$ which will also increase $P _ { 2 } ( \tau _ { 2 } )$ until $\lambda ( \tau _ { 2 } , P _ { 2 } ( \tau _ { 2 } ) ) \cdot n _ { 1 } = n _ { 2 } - \tau _ { 2 } ;$ call this quantity of tokens $\tau _ { 2 } ^ { m i n }$ . The platform will never <sup>fi</sup>nd it optimal to set $\tau _ { 2 }$ lower than $\tau _ { 2 } ^ { m i n }$

If the platform offers a larger quantity of tokens $\tau _ { 2 } > \tau _ { 2 } ^ { m i n } .$ , as $P _ { 2 } ( \tau _ { 2 } )$ increases, then the supply of tokens that period 1 users are willing to sell at $P _ { 2 } ( \tau _ { 2 } )$ outstrips the demand from the new arrivals; that is, $\lambda ( \tau _ { 2 } ,$ $P _ { 2 } ( \tau _ { 2 } ) ) n _ { 1 } > n _ { 2 } - \tau _ { 2 }$ . Excess supply and price competition among the period 1 users, with some willing to sell their token for a price close to zero, pushes the price down. The market-clearing condition $\lambda ( \tau _ { 2 } , p _ { 2 } ( \tau _ { 2 } ) ) n _ { 1 } = n _ { 2 } - \tau _ { 2 }$ then de<sup>fi</sup>nes $p _ { 2 } ( \tau _ { 2 } ) \stackrel { - } { < } P _ { 2 } ( \tau _ { 2 } )$ , which yields Lemma 1.

Lemma 1. In settings with a potential resale market and successful adoption in period 1 $( i . e . , \ s _ { 1 } = 1 ) , \ i f \ \tau _ { 2 } > \tau _ { 2 } ^ { m i n }$ , then $p _ { 2 } ( \tau _ { 2 } ) < \dot { P _ { 2 } } ( \tau _ { 2 } )$ , whereas $i f \tau _ { 2 } = \tau _ { 2 } ^ { m i n }$ , then $p _ { 2 } ( \tau _ { 2 } ) = P _ { 2 } ( \tau _ { 2 } )$

Proof: The proofs of all lemmas and propositions are in Online Appendix B.

Let τ<sup>Pmax</sup> $\tau _ { 2 } ^ { P m a x }$ be the quantity of tokens that maximizes the market-clearing price at $t = 2 ,$ , and let $\tau _ { 2 } ^ { \pi _ { 2 } m a x }$ be the quantity of tokens that maximizes the second-period pro<sup>fi</sup>t of the platform. Lemma 2 characterizes the relation between these values. Lemmas 1 and 2 will help establish the relative value of issuing tokens in Section 5.

Lemma 2. In settings with a potential resale market and successful adoption in period $1 ( i . e . , s _ { 1 } = 1 )$

$$
\tau_ {2} ^ {m i n} \leq \tau_ {2} ^ {P m a x} \leq \tau_ {2} ^ {\pi_ {2} m a x} <   n _ {2} - \lambda^ {N T} n _ {1}.
$$

In order to maximize its second-period pro<sup>fi</sup>t $, ^ { 3 7 }$ at equili brium the platform offers for sale $\tau _ { 2 } ^ { T } = \tau _ { 2 } ^ { \pi _ { 2 } m a x }$ tokens in period 2, and the market-clearing equilibrium price is

$$
p _ {2} ^ {T} \leq P _ {2} ^ {T} = \alpha_ {2} E _ {k} [ u _ {k} (n _ {1} + \tau_ {2} ^ {T}) ] + (1 - \alpha_ {2}) E _ {k} [ u _ {k} ((1 - \lambda^ {0}) n _ {1}) ].
$$

Thus, in period 2, the platform will offer fewer than $n _ { 2 } - \lambda ^ { N T } n _ { 1 } ^ { \mathbf { a } }$ tokens, so that it can achieve a positive market-clearing price $p _ { 2 } ^ { T } > 0$ . By the market-clearing condition, period 1 users with unfavorable-enough types $k < k ^ { \bar { T } }$ sell their tokens in the second period and leave the platform, where the threshold $k ^ { \bar { T } }$ is characterized by the condition $u _ { k ^ { T } } ( n _ { 1 } + \tau _ { 2 } ^ { T } ) = p _ { 2 } ^ { T }$ . Let $\boldsymbol { \lambda } ^ { T } =$ $\textstyle \int _ { k ^ { T } } ^ { B } g ( k )$ dk denote the fraction of period 1 adopters that sell their tokens in the second period and exit.

Now we can solve for the period 1 equilibrium focusing on settings that allow the platform to operate pro<sup>fi</sup>tably. Potential users that arrive in period 1 know that if the adoption fails in period 1, then it will also fail in period $\bar { 2 ; }$ and if it succeeds in period 1, then the platform will <sup>fi</sup>nd it optimal to set a price in period 2 that attracts the new potential users and thus succeeds as well.<sup>38</sup> They also know that, once they join and learn their type $k ,$ they will be able to sell their token for $p _ { 2 } ^ { T }$ at $t = 2$ and leave if that type is unfavorable enough, indicating a poor <sup>fi</sup>t with the platform.

The highest price that the platform can charge and attract users in period 1 is

$$
\begin{array}{c} P _ {1} ^ {T} (\alpha_ {1}, \alpha_ {2}, n _ {1}, n _ {2}) = \alpha_ {1} V ^ {T} (s _ {1} = 1 \mid \alpha_ {2}, n _ {1}, n _ {2}) \\ + (1 - \alpha_ {1}) V (s _ {1} = 0 \mid \alpha_ {2}, n _ {1}, n _ {2}). \end{array}
$$

All equilibrium values depend on the parameters of the setting, but, similarly to our analysis for period 2, we omit the variables $\alpha _ { 2 } , \ n _ { 1 } ,$ and $n _ { 2 }$ from our notation to improve readability, and we use $P _ { 1 } ^ { T } , V ^ { T } ( s _ { 1 } = 1 )$ and $V ( s _ { 1 } = 0 )$ to denote $P _ { 1 } ^ { T } ( \alpha _ { 1 } , \alpha _ { 2 } , n _ { 1 } , n _ { 2 } ) , \mathbf { \bar { \ } } V ^ { T } ( s _ { 1 } = 1 \mid \alpha _ { 2 } , n _ { 1 } $ $n _ { 2 } )$ and $V ( s _ { 1 } = 0 \mid \alpha _ { 2 } , n _ { 1 } , n _ { 2 } )$ . The expected individual bene<sup>fi</sup>t of joining the platform if the platform fails is $V ( s _ { 1 } = 0 ) = E _ { k } [ u _ { k } \bar { ( 0 ) } ] < \bar { 0 } _ { }$ , and the expected individual bene<sup>fi</sup>t of joining the platform if the platform succeeds is

$$
\begin{array}{l} V ^ {T} (s _ {1} = 1) = \int_ {A} ^ {k ^ {T}} [ u _ {k} (n _ {1}) + u _ {k} (n _ {1} + \tau_ {2} ^ {T}) ] g (k) d k \\ \qquad + \int_ {k ^ {T}} ^ {B} [ u _ {k} (n _ {1}) + p _ {2} ^ {T} ] g (k) d k > E _ {k} [ u _ {k} (n _ {1}) ] > 0. \end{array}
$$

At equilibrium, the platform charges in the <sup>fi</sup>rst period the highest price it can while achieving successful adoption; that is, $\dot { p } _ { 1 } ^ { T } = P _ { 1 } ^ { T }$ . Total platform pro<sup>fi</sup>t in the equilibrium with tokens is

$$
\Pi^ {T} = \max \{P _ {1} ^ {T} n _ {1} + p _ {2} ^ {T} \tau_ {2} ^ {T}, 0 \},
$$

as when $P _ { 1 } ^ { T } n _ { 1 } + p _ { 2 } ^ { T } \tau _ { 2 } ^ { T } < 0 _ $ , the platform does not enter the market.

## 5. Tokens vs. No Tokens

The coordination problem arises when potential users will not adopt the platform unless other potential users also adopt. If they all adopt, then the platform succeeds; otherwise, it fails. The main two solutions that have been proposed in the literature for a platform to address this problem are a buyback promise or a subsidy (e.g., Shapiro and Varian 1998, Evans et al. 2006).

Under a buyback promise, the platform sets a high upfront price, corresponding to the case where all potential users join the platform, and promises to reimburse these users in the future to re<sup>fl</sup>ect the actual level of adoption. This reimbursement may exceed the upfront price if failure of the platform results in negative utility for the adopters, as is the case in our model. As we show in Online Appendix A.1, the buyback promise offers the highest pro<sup>fi</sup>t independently of the focality of adoption, but it requires the platform to make a credible commitment to pay back the early users in the event of low or failed adoption. In that case, however, the platform has an incentive to renege on its buyback commitment.

The need for a credible buyback commitment would favor <sup>fi</sup>rms that enjoy reputation and <sup>fi</sup>nancial resources already earned in other markets, and thus this solution to the coordination problem would bene-<sup>fi</sup>t established <sup>fi</sup>rms over new entrants.<sup>39</sup> Notably, such buyback promises are rarely, if ever, observed in practice, which may indicate that even established <sup>fi</sup>rms <sup>fi</sup>nd it dif<sup>fi</sup>cult to credibly make such promises.

We thus assume that, in our setting, the platform cannot credibly commit to a buyback promise in the case of failed adoption. In the absence of tokens, the platform can address the coordination problem by subsidizing period 1 users, as this would not require a commitment to future actions.

In order to succeed in period 1, the platform must set a low-enough price (or high-enough subsidy) so that the potential users are induced to adopt, given the expected utility and the market bias in favor of adopting the platform as captured by the focality α. Even though users that join in period 1 are ex ante homogeneous, they differ ex post in how much they bene<sup>fi</sup>t from having joined the platform, and users with the least favorable types, who get the least bene-<sup>fi</sup>t from joining the platform, can leave the platform in period 2. If the platform succeeds in period 1, then it acquires a user base, a fraction of which will remain with the platform in period 2, thus making the platform more attractive for new potential users that arrive in period 2. As a result, the platform may face an easier coordination problem in period 2.<sup>40</sup>

Whereas subsidizing early users offers a solution to the coordination problem that does not require commitment to future actions, it requires up-front capital, which may be costly, favor established <sup>fi</sup>rms with deep pockets, and thus create barriers to entry. For the remainder of this section, we focus on the tradeoffs that a platform faces between subsidizing early users (formally analyzed in Online Appendix A.2) and issuing tokens in order to overcome the coordination problem and achieve successful adoption.

## 5.1. Impact of Introducing Tradable Tokens

Providing access through platform-speci<sup>fi</sup>c cryptographic tokens offers the platform new possibilities in terms of its entry and pricing strategy, which under certain conditions can be more attractive than available alternatives. Speci<sup>fi</sup>cally, the technology around smart contracts and blockchain-based cryptographic tokens allows the platform to credibly commit not only to accept but also to require these tokens for future access, to commit to a certain price and/or quantity schedule if desired, and to provide for ef<sup>fi</sup>- cient trading of the tokens. When used appropriately, these technical abilities can assure potential users in period 1 that if they join the platform and learn their type k, and they subsequently prefer to leave in period 2, then they will be able to sell their future access rights on favorable terms.

Without tradable access to the platform, users will leave only if they would obtain negative utility from staying in period 2. With tokens enabling ef<sup>fi</sup>cient resale of access, a positive token price makes leaving in period 2 more attractive but also makes more attractive adopting the platform in period 1. Lemma 3 shows that providing platform access via tradable tokens results in a larger fraction of period 1 users leaving in period 2:

Lemma 3. In settings with a potential resale market and successful adoption in period $\dot { \textbf { \textit { 1 } } } ( i . e . , \ s _ { 1 } = 1 )$ , more users leave in period 2 when tokens are used: $\lambda ^ { T } > \lambda ^ { N T }$

Since more period 1 users leave when they can resell their access, the platform will have a lower user base in period 2. Lemma 4 shows that, as a result, the platform needs to charge a lower price in period 2 when it employs tokens:

Lemma 4. In settings with a potential resale market and successful adoption in period 1 $( i . e . , \ s _ { 1 } = 1 )$ , the period 2 price for platform access is weakly lower with tokens: $\dot { p } _ { 2 } ^ { T } \le \dot { P } _ { 2 } ^ { N T }$

There are two reasons the price in period 2 is lower with tokens: First, the maximum price that the platform can charge and still have successful adoption, $P _ { 2 } ^ { T } ,$ depends on the value it offers potential participants when it is successful in period 2. In the setting with tokens, more users will leave per Lemma 3, and the platform’s period 2 network will be smaller, offering less utility to users that join, and thus reducing $P _ { 2 } ^ { T }$ . Second, without tokens, the platform will optimally set $p _ { 2 } ^ { N T }$ at $P _ { 2 } ^ { N T }$ , the maximum price that it can charge and still succeed in period $2 ;$ but in the case with tokens, the platform has less incentive to raise $p _ { 2 } ^ { T }$ all the way to $P _ { 2 } ^ { T }$ This is because as $p _ { 2 } ^ { T }$ increases, the fraction of users that leave in period 2 increases as well; as a result, new period 2 users buy more tokens from exiting period 1 users rather than the platform, which reduces the platform’s revenue in period 2.

Whereas the previous two lemmas imply that the platform earns higher period 2 revenue without tokens, issuing tradable tokens allows the platform to increase its period 1 revenue. This is because potential users in period 1 are willing pay a higher price to join the platform when they obtain a token that they can sell in period 2 if they decide to leave the platform. Thus, issuing tokens can allow the platform to overcome the coordination problem while increasing its period 1 revenue—at the cost of decreasing its period 2 revenue. It turns out that the revenue loss in period 2 is higher than the revenue gain in period 1, resulting in lower total pro<sup>fi</sup>ts, as shown in Proposition 1.

Proposition 1. In settings with a potential resale market, tokens allow for higher revenue in the first period, that $i s ,$ $n _ { 1 } P _ { 1 } ^ { T } > n _ { 1 } P _ { 1 } ^ { \check { N } T }$ , but total revenue for the platform across both periods is lower when it issues tokens, that is, $\Pi ^ { T } < \Pi ^ { N T }$

The platform sets the highest period 1 price that will overcome the coordination problem. When it employs tokens, the platform also indirectly sells in period 1 some of the access it will provide to the potential users that will arrive in period 2, as tokens can be resold to period 2 arrivals from period 1 adopters that leave the platform. Essentially, by issuing tokens, the platform gives early adopters an equity stake in the future success of the platform and shares part of the period 2 revenue with them. This increases period 1 revenue but decreases period 2 revenue and total revenue.

The network size is smaller in the second period with tokens, as more users leave given the ability to resell their token. This reduces period 2 network effects, results in a lower period 2 price, and is the reason that the platform cannot collect in period 1 all the revenue that is lost in period 2. Since total revenue is higher without tokens, in the absence of capital constraints, the platform will prefer to overcome the coordination problem by subsidizing period 1 users rather than by issuing tradable tokens. On the other hand, the ability to reduce or eliminate the need for a subsidy by issuing tradable tokens will be valuable to the platform if a subsidy is suf<sup>fi</sup>ciently costly or infeasible. As shown in Online Appendix D, Proposition 1 continues to hold if both the platform and the period 1 potential users discount the future at the same rate.

## 5.2. Costly Financing

An important case arises when the platform faces a coordination problem that it cannot overcome unless it subsidizes adoption, that is, sets a negative price in period 1. In that case, whereas per Proposition 1 the total revenue will be lower with tokens, the platform can still <sup>fi</sup>nd it optimal to overcome the coordination problem by issuing tradable tokens, because of the ability to move revenue from period 2 to period 1 and thus reduce or avoid the necessary subsidy. For instance, if $p _ { 1 } ^ { N T } < 0 < p _ { 1 } ^ { T }$ , then overcoming the coordination problem without tokens requires a subsidy in period 1, but the subsidy can be avoided by issuing tokens. If the platform faces capital constraints, or a negative price is otherwise not feasible,<sup>41</sup> employing tokens may be the preferred strategy.

Suppose, for instance, that $P _ { 1 } ^ { N \breve { T } } < 0 ,$ , that is, a subsidy $n _ { 1 } P _ { 1 } ^ { N T }$ is needed in period 1, and the platform faces a cost of capital $r > 0$ for this subsidy. This cost affects platform pro<sup>fi</sup>ts if it needs to offer a subsidy to overcome the coordination problem:

$$
\Pi^ {N T} (r) = (1 + r) n _ {1} P _ {1} ^ {N T} + n _ {2} P _ {2} ^ {N T} = \Pi^ {N T} + r n _ {1} P _ {1} ^ {N T} <   \Pi^ {N T}.
$$

Proposition 2 derives conditions under which the platform would <sup>fi</sup>nd it advantageous to issue tokens because of the cost of <sup>fi</sup>nancing a subsidy.

Proposition 2. In settings with a potential resale market, $i f P _ { 1 } ^ { \dot { N } T } < 0 < P _ { 1 } ^ { T }$ , then $\Pi ^ { T } > \Pi ^ { N T } ( r ) \dot { f } o r r > \bar { r }$ , where

$$
\bar {r} = \frac {n _ {1} (P _ {1} ^ {T} - P _ {1} ^ {N T}) + n _ {2} (p _ {2} ^ {T} - P _ {2} ^ {N T}) - \lambda^ {T} n _ {1} p _ {2} ^ {T}}{n _ {1} P _ {1} ^ {N T}} > 0.
$$

Proposition 2 shows that the platform prefers to use to kens rather than a subsidy to overcome the coordination problem if it faces a high-enough cost of capital. It follows that a more positive market bias toward the platform in period 1, captured by a higher focality α in favor of adopting, increases this threshold:

## Corollary 1. The threshold r is increasing with¯ $\alpha _ { 1 }$ .

Since the focus of our analysis is overcoming the coordination problem, $\alpha _ { 1 }$ and $\alpha _ { 2 }$ should get special attention, as they determine the severity of the coordination problem. Speci<sup>fi</sup>cally, lower $\alpha _ { 1 }$ and $\alpha _ { 2 }$ indicate that the coordination problem is more dif<sup>fi</sup>cult to overcome, as the market is tilted against adopting as the focal equilibrium.

As shown in Proposition 2, the platform prefers to use tokens rather than a subsidy to solve the coordination problem if its cost of capital is above a certain threshold. Corollary 1 shows that for lower values of $\alpha _ { 1 } ,$ this threshold is lower. For high $\alpha _ { 1 } ,$ , when the adopting strategy enjoys a high degree of focality at period 1 and the coordination problem is easier to overcome, capital must be more expensive to make tokens the preferred solution. But, as $\alpha _ { 1 }$ gets lower, that is, the market bias moves against adopting and the platform faces a coordination problem that is increasingly more costly to overcome, the subsidies needed for successful adoption become more expensive and issuing tradable tokens may be a better option, even for a relatively low cost of capital.

Figure 2 illustrates the results of Propositions 1 and $^ { 2 , }$ and shows comparative statics for the period 1 focality $\alpha _ { 1 }$ . As shown in Proposition 1, the platform pro<sup>fi</sup>t without tokens is higher than with tokens; that ${ \mathrm { i } } \mathbf { s } ,$ the $\Pi ^ { N T }$ line is above $\Pi ^ { T }$ . Both $\Pi ^ { T }$ and $\Pi ^ { N T }$ are increasing with $\alpha _ { 1 } ,$ , but $\Pi ^ { T }$ increases faster.

Figure 2. (Color online) Focality, First Period Price, and Total Platform Pro<sup>fi</sup>t  
![](/api/attachments/JU4SZ2U4/fulltext/images/2a82b6182702a225ef3dfca613902e57eb6cc446798bd7818f25bdf15eecb38c.jpg)  
Notes. The solid lines represent results of Proposition 1, and the dashed line represents Proposition 2. The shaded area shows the region where tokens enable the platform to avoid subsidies.

From Proposition 1, we know that $P _ { 1 } ^ { T }$ is above $P _ { 1 } ^ { N T }$ . The shaded region represents the area where $P _ { 1 } ^ { N T } <  \mathrm { \large { 0 } } < P _ { 1 } ^ { T }$ that is, the region where without tokens a subsidy is required in period 1, but with tokens the coordination problem is solved in the platform’s favor while it is able to charge a positive price for its tokens.

Both $P _ { 1 } ^ { T }$ and $\overset { \mathbf { \widehat { \mathbf { \phi } } } } { P } _ { 1 } ^ { N T }$ are increasing in $\alpha _ { 1 }$ as well, with $P _ { 1 } ^ { T }$ increasing faster. That means that, for lower $\alpha _ { 1 } ,$ a larger subsidy is required in period 1 to overcome the coordination problem.

As $\alpha _ { 1 }$ decreases, the cost of <sup>fi</sup>nancing the increasing subsidy in the absence of tokens outweighs the loss of total revenue resulting from issuing tokens; this corresponds to the dashed red line that shows the total platform pro<sup>fi</sup>ts adjusted for the cost of <sup>fi</sup>nancing the subsidy crossing below $\Pi ^ { T }$ . By Proposition 2, the two lines meet for such value of $\alpha _ { 1 }$ that ${ \hat { \bar { r } } } = r .$ . As the cost of capital r increases, the slope of the dashed line increases, and it crosses the $\dot { \Pi } ^ { T }$ line at higher $\alpha _ { 1 }$ values, which is captured by Corollary 1.

In summary, our analysis shows that issuing tradable tokens provides a new tool for solving the coordination problem for a platform in a setting with network effects, when a direct subsidy is either unde sirable or not feasible.

## 5.3. Tokens and Platform Incentive to Deviate

Platform-speci<sup>fi</sup>c tokens and currencies such as airline frequent <sup>fl</sup>ier miles or Facebook credits are not new (Gans and Halaburda 2015, Halaburda et al. 2022a). They have not been used to address the coordination problem, however, because typically the issuing platform has an ex post incentive to erode the token value in future periods, by either refusing to accept them, making them harder to transfer and trade, or by allowing platform access without them. This is because once the coordination problem has been resolved with successful adoption, outstanding tokens represent a liability to the platform.<sup>42</sup> As we have shown in our analysis, tradable tokens move revenue from the second period to <sup>fi</sup>rst but reduce both period 2 revenue and total revenue.

After the platform is successful in the <sup>fi</sup>rst period, that $\mathbf { i s } , s _ { 1 } = 1 ,$ it has an incentive to renege on the tradability of tokens; it could, for instance, restrict the functionality available to unregistered owners or outright refuse to accept their tokens. This would allow the platform to collect $p _ { 2 } ^ { N T } \cdot n _ { 2 } > p _ { 2 } ^ { T } \cdot \tau _ { 2 } ^ { \pi _ { 2 } m a x }$ after collecting the <sup>fi</sup>rst-period token revenues of $\mathbf { \bar { \rho } } p _ { 1 } ^ { T } \cdot n _ { 1 } > p _ { 1 } ^ { N T } \cdot n _ { 1 }$ . But knowing about this incentive to renege, the potential users in the <sup>fi</sup>rst period would not want to buy a token at a price higher than $p _ { 1 } ^ { N T }$ . In other words, the bene<sup>fi</sup>ts of the tradable tokens cannot be realized unless the tradability is supported by a credible commitment by the platform to accept traded tokens without friction.

Cryptographic utility tokens are different in this respect, as the underlying blockchain and/or smart contract technologies enable exactly this type of commitment. Platforms can be designed to guarantee that tokens will provide access in future periods and also be required for access, even when traded to a new owner; furthermore, such trading can be ef<sup>fi</sup>ciently supported on markets operated either by the issuer or a third-party exchange. These characteristics of platform-speci<sup>fi</sup>c digital tokens can assure early buyers that the value of the tokens will not be unduly diluted in future periods and thus make it possible for the platform to use these tokens to address the coordination problem.

## 6. Discussion

Much of the focus on ICOs has been in the context of using their proceeds as a primary or secondary source of funds for the development of digital platforms such as new electronic marketplaces. Several potential sources of value can be identi<sup>fi</sup>ed in this context, including allowing entrepreneurs to tap a source of <sup>fi</sup>nancing outside the traditional equity or debt channels, and the potential of a prospective platform to gauge demand for its services based on the demand for the digital tokens it issues.

Our paper contributes to this discussion by addressing an aspect frequently overlooked: the ability to issue tradable digital tokens required to access platform services can be used to help address the coordination problem in fostering adoption by potential users. It is certainly true that transferable participation rights could be issued and traded without blockchain and cryptographic token technology; however, the extraordinary reduction in the associated frictions, as well as the increase in functionality, awareness, popularity, and acceptance of these mechanisms, has resulted in a qualitative change that makes such mechanisms practical, and they are, in fact, enjoying rapid growth.

We employ a model that focuses on the coordination aspect of digital utility tokens issued by a new marketplace. To simplify the model, we assume the following:

(1) The new marketplace is already developed and thus there is no uncertainty about its technological risk; this is consistent with the increase in the fraction of platforms that have achieved “minimum viable product” (MVP) before having an ICO.

(2) There are two periods with arrival of early and late potential users, which captures the dynamic nature of new marketplace adoption, and the fact that the marketplaces may need to subsidize early users, but, if successful, are able to enjoy economic value in later periods.

(3) The potential users expected to arrive in each of the two periods, their utility from joining the new marketplace, and the favorability of the market toward the platform (captured by the focality α of adopting the platform) are common knowledge.

(4) Potential users that acquire a token in the <sup>fi</sup>rst period also join the marketplace; these users can stay for the second period as long as they keep their token, or they may exit in the second period and trade their token.

(5) Tokens can be ef<sup>fi</sup>ciently traded when issued and at resale, matching demand and supply and thus clearing the market, which re<sup>fl</sup>ects the extensive infrastructure that supports the issuance, distribution, and trading of cryptographic tokens.

We <sup>fi</sup>nd that cryptographic utility tokens can provide a novel mechanism to help solve the coordination problem faced by a new platform such as a new digital marketplace. This mechanism relies on the ef<sup>fi</sup> cient tradability and credible commitments made possible by the underlying blockchain and/or smart contracts technologies. It works by allowing early users to share the bene<sup>fi</sup>t of platform success, as they can sell their tokens at a higher price when the platform is successful. Early users essentially acquire an equity interest in the platform and thus become vested in its success. As a result, lower incentives are needed to get early users to adopt, reducing the cost of addressing the coordination problem.

Our main result is that tokens allow the platform to increase its revenue in period 1 at the cost of lower revenue in period 2 and lower total revenue. Whereas token sales to early adopters result in higher revenue in period 1, they are offset by loss of revenue in period 2, as these early adopters sell their tokens to future potential users. As more early users exit when they can sell their token, the period 2 network is smaller, and the reduced network effect is re<sup>fl</sup>ected in lowe total revenue for the platform. If the platform faces no <sup>fi</sup>nancial constraints, then traditional strategies to address the coordination problem (such as a subsidy for early users) will lead to higher total pro<sup>fi</sup>ts.

If, however, the platform is capital-constrained, then tokens provide a mechanism to avoid the cost of subsidizing period 1 users and thus <sup>fi</sup>nance the solution of the coordination problem faced by the platform. The bene<sup>fi</sup>t of issuing tokens increases when the platform is viewed by the market as riskier, or when its cost of capital is higher.

An important aspect of tokens is the ability to make token purchases (which in the case of platform-speci<sup>fi</sup>c tokens correspond to adoption decisions) observable by market participants. This transparency on the platform’s progress in recruiting participants can affect the resulting equilibria by changing the information structure and/or the sequence of moves in the adoption game, which in some settings can resolve the coordination problem. This mechanism, which has been studied in the literature, is distinct from the way tokens can help overcome the coordination problem in our setting, which follows from their tradability.

In our analysis, we assumed that the platform’s decision to issue tokens did not change the market’s perception of the platform, and thus did not affect the focality of adopting the platform in either period. If the mere fact of issuing tokens biases the market in favor of adopting the platform (e.g., because offering tokens in an ICO creates a favorable impression of the platform’s likely success or otherwise desirability), then this will provide still another reason why tokens can facilitate platform adoption.

Our setting was intended to simplify the analysis and emphasize the central focus of our model, which is using tokens to address the coordination problem of potential adopters. We explored the robustness of our results by relaxing several of our assumptions in the online appendices. In Online Appendix C, we allow for early potential adopters to have a different distribution of types than later adopters, for example, because early adopters could be more likely to have higher value for the services of the platform. In Online Appendix D, we allow for the platform and the potential users arriving in period 1 to discount the future in period 2. In Online Appendix E, we allow the platform to commit upfront to supply a certain quantity of tokens in the second period, as this is possible with cryptographic tokens and might lead to different token prices when the market clears. In Online Appendix F, we allow for investors that may acquire tokens with the intent to trade their tokens in the second period, rather than use them to join the platform, as such investors are common in some real-world ICOs. In Online Appendices G.1 and G.2, we allow uncertainty about the size of the market in the second period, for the cases without and with investors, respectively. In Online Appendix H, we allow the platform to restrict the number of tokens that it makes available in the <sup>fi</sup>rst period, as that could lead to more demand in the second period. We <sup>fi</sup>nd that, consistent with our main results, when a resale market for tokens can be sustained, employing tokens allows the platform to increase its <sup>fi</sup>rst period revenue at the cost of a lower second period, as well as total revenue.

Relaxing other aspects in our setting can lead to several extensions and variations to our work. For example, our setting can be extended to more than two periods. Another extension would be to allow for heterogeneity of the potential users in their focality parameter with respect to the platform and in their willingness to pay as a function of network size. It would also be interesting to combine the coordination features of our model with related work that considers the use of tokens as a means for <sup>fi</sup>nancing the development of a platform or to gauge the demand for its services, which would allow us to explore potential strategic interactions. Finally, whereas we analyzed one-sided platforms with our model, our approach can be used to study the use of tokens in resolving the coordination problem in two-sided or multisided platforms.

Another area for future research would be to consider competing platforms. If one of the platforms is an incumbent with an existing user base, then coordination is required for existing and new users to move to the new platform; the new platform may be able to use tokens to facilitate its entry. In the case of competing new platforms with similar functionality, potential users face a layered coordination problem: <sup>fi</sup>rst, they will only want to adopt if other users adopt; but, also, due to the network effects, if they do adopt, then they want to adopt the same platform as the other users. The platforms may compete by selling their respective tokens in the <sup>fi</sup>rst period below the price indicated in our analysis of the monopolistic case.<sup>43</sup> Whereas that would seem to make tokens less pro<sup>fi</sup>table, with competing platforms, the required subsidies would also need to be signi<sup>fi</sup>cantly larger, so issuing tokens may still be the preferred strategy for a platform facing a high cost of capital.

## Acknowledgments

The authors thank the special section editors, the associate editor, and the referees for their guidance and constructive comments. The authors also thank Guillaume Haeringer, Evgeny Lyandres, George Mailath, Rajiv Mukherjee, Ariel Pakes, Alessandro Pavan, Andrew Postlewaite, Maher Said, Larry White, Yaron Yehezkel, and participants of Friday Workshop at NYU Stern, of SIGBPS at ICIS 2019, of Paris Fintech Webinar, of Theory Seminar at University of Pennsylvania, and of WISE 2020, for helpful discussions and comments. Previous version of this paper circulated with the title “The Role of Cryptographic Tokens and ICOs in Fostering Platform Adoption.”

## Appendix. Summary of Notation

## Environment parameters

<table><tr><td> $t = 1,2$ </td><td>Time periods</td></tr><tr><td> $n_{t}$ </td><td>Number of potential users arriving in period  $t$ </td></tr><tr><td> $k$ </td><td>User type, affecting user’s utility</td></tr><tr><td> $g(k)$ </td><td>Probability density function of  $k$ </td></tr><tr><td> $[A,B]$ </td><td>Support of  $g(k)$ </td></tr><tr><td> $\alpha,\alpha_{t}$ </td><td>Degree of focality; in multiperiod environment, indexed by  $t$ </td></tr><tr><td> $u_{k}(\omega)$ </td><td>Utility of user with type  $k$  from participating in marketplace of size  $\omega$ </td></tr></table>

Market variables

<table><tr><td> $\omega, \omega', \omega_t$ </td><td>Size of the marketplace; in multiperiod environment indexed by  $t$ </td></tr><tr><td> $s_t = 0,1$ </td><td>Adoption success in period  $t$ , with 0 denoting failure and 1 success</td></tr><tr><td> $V(s_t)$ </td><td>The expected benefit of joining the platform when the adoption success is  $s_t$ </td></tr><tr><td> $p$ </td><td>Price for tokens or platform access</td></tr><tr><td> $P$ </td><td>Price threshold level under partial focality</td></tr><tr><td> $r$ </td><td>Per-unit cost of capital</td></tr><tr><td> $\bar{r}$ </td><td>Threshold cost of capital, above which issuing tokens is more profitable for the platform than subsidy</td></tr></table>

## Analysis of market forces in presence of tradable tokens

<table><tr><td> $k(\tau_{2},p_{2})$ </td><td>Marginal type of early adopter who sells his token given the price  $p_{2}$  and  $\tau_{2}$ </td></tr><tr><td> $\lambda(\tau_{2},p_{2})$ </td><td>Fraction of early adopters who leave in period 2 given the price  $p_{2}$  and  $\tau_{2}$ </td></tr><tr><td> $\tau_{2}$ </td><td>Number of tokens the platform releases period 2</td></tr><tr><td> $\tau_{2}^{min}$ </td><td>Minimum number of tokens the platform issues in the equilibrium with tokens</td></tr><tr><td> $\tau_{2}^{Pmax}$ </td><td>Number of tokens that maximizes the market price in  $t = 2$ </td></tr><tr><td> $\tau_{2}^{\pi_{2}max}$ </td><td>Number of tokens that maximizes the platform&#x27;s second-period profits</td></tr><tr><td> $p_{1}$ </td><td>Price of a token or access the platform sets for  $t = 1$ </td></tr><tr><td> $p_{2}(\tau_{2} | n_{1},n_{2}) \rightarrow p_{2}(\tau_{2})$ </td><td>Market price in  $t_{2}$  as a function of the number of tokens released by the platform,  $\tau_{2}$ , given the environmental variables  $n_{1}$  and  $n_{2}$ </td></tr><tr><td> $P_{2}(\tau_{2},s_{1}=1 | \alpha_{2},n_{1},n_{2}) \rightarrow P_{2}(\tau_{2})$ </td><td>Second-period price threshold if  $s_{1}=1$  as a function of  $\tau_{2}$ </td></tr></table>

## Equilibrium variables with tokens (superscripts T)

<table><tr><td> $k^{T}$ </td><td>Marginal type of early adopter who sells his token in  $t = 2$  in equilibrium with tokens</td></tr><tr><td> $\lambda^{T}$ </td><td>Fraction of early adopters leaving in period 2 in equilibrium with tokens, in case of successful adoption by new users in period 2</td></tr><tr><td> $\lambda^{0}$ </td><td>Fraction of early adopters leaving in period 2, in case of failed adoption by new arrivals in period 2 (the same in equilibrium with and without tokens)</td></tr><tr><td> $\tau_{2}^{T}$ </td><td>Number of tokens the platform releases in  $t = 2$ , after success in period 1, in equilibrium with tokens</td></tr><tr><td> $P_{2}^{T}(s_{1}=1 \mid \alpha_{2},n_{1},n_{2})\rightarrow P_{2}^{T}$ </td><td>Second-period price threshold given  $s_{1}=1$  in equilibrium with tokens</td></tr><tr><td> $p_{2}^{T}$ </td><td>Market-clearing price of a token in  $t = 2$ , after first-period successful adoption, in equilibrium with tokens</td></tr></table>

<table><tr><td> $P_{1}^{T}(\alpha_{1},\alpha_{2},n_{1},n_{2}) \rightarrow P_{1}^{T}$ </td><td>Price threshold level for  $t = 1$  in equilibrium with tokens, under environmental variables $n_{1},n_{2},\alpha_{1},\alpha_{2}$ </td></tr><tr><td> $V(s_{1}=0 \mid \alpha_{2},n_{1},n_{2}) \rightarrow V(s_{1}=0)$ </td><td>User’s expected benefit of joining the platform in  $t = 1$  if adoption fails in  $t = 1$  (the same in equilibrium with and without tokens)</td></tr><tr><td> $V^{T}(s_{1}=1 \mid \alpha_{2},n_{1},n_{2}) \rightarrow V^{T}(s_{1}=1)$ </td><td>User’s expected benefit of joining the platform in  $t = 1$  if adoption succeeds in  $t = 1$ </td></tr><tr><td> $p_{1}^{T}$ </td><td>Price of a token the platform sets for  $t = 1$  in equilibrium with tokens</td></tr><tr><td> $\Pi^{T}$ </td><td>Platform’s profit in equilibrium with tokens</td></tr></table>

## Equilibrium variables with no tokens (superscripts NT)

<table><tr><td> $k^{NT}$ </td><td>Marginal type of early adopter who leaves the platform in  $t = 2$  in equilibrium without tokens</td></tr><tr><td> $\lambda^{NT}$ </td><td>Fraction of early adopters leaving in period 2 in equilibrium without tokens</td></tr><tr><td> $p_{2}^{NT}$ </td><td>Price the platform sets in  $t = 2$ , after success in period 1, in equilibrium without tokens</td></tr><tr><td> $P_{2}^{NT}$ </td><td>Price threshold level for  $t = 2$ , after success in period 1, in equilibrium without tokens</td></tr><tr><td> $p_{1}^{NT}$ </td><td>Price the platform sets in  $t = 1$  in equilibrium without tokens</td></tr><tr><td> $P_{1}^{NT}$ </td><td>Price threshold level for  $t = 1$  in equilibrium without tokens</td></tr><tr><td> $\Pi^{NT}$ </td><td>Platform’s total profit in equilibrium without tokens</td></tr><tr><td> $\Pi^{NT}(r)$ </td><td>Platform’s total profit in equilibrium with subsidy (without tokens) under a positive cost of capital</td></tr></table>

## Endnotes

<sup>1</sup> An alternative view attributes the growth of ICOs prior to 2018 to their ability to in effect issue equity securities while sidestepping securities regulations, thereby avoiding the associated costs and in certain cases taking advantage of investors. This view is strength ened by the fact that after regulatory agencies in major markets (United States, Europe, and China) subjected a majority of such ICOs to regulatory oversight similar to traditional securities, there was a very substantial drop in the volume of ICOs in the second half of 2018 and into 2019 (ICO Bench 2020).

$^ 2 \mathrm { S e e } ,$ for instance, Halaburda et al. (2022a) for a review of local currencies such as BerkShares or Ithaca hours, and private platform currencies such as Facebook credits or Amazon coins, or the several web currencies started in the late 1990s such as Beenz and Flooz.

<sup>3</sup> Essentially, after taking advantage of the coordination benefit from the tokens and achieving successful adoption, outstanding tokens represent a liability that the platform has an incentive to depreciate.

<sup>4</sup> For an overview of the literature on how cryptocurrency technology is affecting economic forces, see Halaburda et al. (2022b).

<sup>5</sup> Ethereum has been the choice of about 90% of $\mathrm { I C O s } ,$ , including the majority of platforms issuing utility tokens, such as the EOS network (with the EOS token that was the largest ICO thus far with proceeds that exceeded \$4 billion), Chainlink (with the LINK token), Maker (with the MRK token), or Brave (with the BAT token) (ICO Bench 2020).

<sup>6</sup> Smart contracts provide for automated execution of certain programmed actions on a blockchain when certain conditions are satisfied, eliminating the possibility of reneging.

<sup>7</sup> At the time of the ICO, the platform’s independent blockchain typically is not functional, at least not beyond the proof-of-concept level that might be part of demonstrating its “minimum viable product.” The tokens purchased in the ICO are typically exchanged for native utility tokens once the platform’s blockchain becomes active.

The ICO process displays the three main factors in the literature that characterize efficient market clearing: (1) homogeneous tokens with low dealer or market-maker inventory risks (see, e.g., Garman 1976, Amihud and Mendelson 1986); (2) mechanisms with low trading frictions and transaction costs (see, e.g., Constantinides 1986, Vayanos 1998); and (3) low search costs to obtain market maker information (see, e.g., Duffie et al. 2005). Moreover, whereas there is evidence of attempted and possibly successful manipulation of crypto markets, for example, via self-trading (where colluding parties act as buyer and seller) or wash trades (buying and selling the same crypto assets), trading of major cryptographic assets is fairly liquid (see, e.g., Gandal et al. 2018, Aloosh and Li 2019, Cong et al. 2020, Amiram et al. 2021, and Lehar and Parlour 2021).

<sup>9</sup> See https://www.coindesk.com/markets/2017/05/31/35-millionin-30-seconds-token-sale-for-internet-browser-brave-sells-out/.

<sup>10</sup> See https://www.coindesk.com/markets/2017/09/07/257- million-filecoin-breaks-all-time-record-for-ico-funding/.

<sup>11</sup> See https://medium.com/blockchannel/a-look-at-the-gnosisdutch-auction-distribution-664920e19c8f.

<sup>12</sup> Websites like CoinMarketCap.com list the exchanges where each token is traded, lowering the search costs even for new tokens. For instance, according to CoinMarketCap.com, the Filecoin token FIL is traded in more than 100 exchanges.

<sup>13</sup> Westland (2021) has found that the transparency of the order book typical in crypto exchanges increases liquidity in the case of Bitcoin; whereas his approach requires quantities of data that are available only for major cryptocurrencies, most cryptographic assets, including the major utility tokens, seem to enjoy substantial liquidity, even in the presence of high volatility. Also, whereas the trading volumes of even the most popular utility tokens do not compare with Bitcoin (which was at more than \$20 billion in daily trading volume as of this writing in mid-January 2021), they can still be substantial, demonstrating a liquid market; FIL, for instance, recently traded more than 11 million tokens each day, for a daily trading volume of over \$320 million.

<sup>14</sup> The conditions of note 8 are also satisfied for subsequent trading of tokens.

15 Offering tokens that allow future use of the platform increases present revenue; however, these tokens are tradable and will compete against tokens issued by the platform in the future and thus will reduce future revenue. A similar trade-off between present and future revenue is found by Sockin and Xiong (2022) as a result of using tokens to commit the platform to a more user-centric future governance.

<sup>16</sup> This term is commonly used for tokens whose only use is to provide access to services of the platform.

<sup>17</sup> ICOs can provide capital for development of a new platform/ marketplace and also can help resolve the coordination problem after the platform is developed; in this paper, we focus on the second of these roles. The Filecoin case provides an appropriate example, as angel and early-stage VC investors provided adequate funds to develop a functional platform (Howell et al. 2020).

<sup>18</sup> The intertemporal price dependency in coordination settings has common aspects with the durable goods monopolist literature going back to Coase (1972), especially in the context of resale in a secondary market (Bulow 1982, Ghose et al. 2005). In the context of cryptographic tokens, their durable goods nature was already pointed out by Cong et al. (2018). Our analysis differs, however, by focusing on markets with network effects and, in particular, the coordination problem faced by new marketplaces and platforms in general.

<sup>19</sup> Li and Mann (2017) also consider how to sustain the value of tokens, which is outside the scope of our paper.

<sup>20</sup> Increasingly, ICOs take place after a platform has demonstrated at least a “minimum viable product” or MVP; according to ICO Bench (2020) that was true for 100% of the ICOs that they tracked in 2020–2021. Filecoin, for instance, had raised \$40 million from investors prior to its ICO and thus was able to demonstrate preliminary platform functionality (Howell et al. 2020).

<sup>21</sup> In Online Appendix C, we relax this assumption and show that our results still hold if we allow for different g k in each period.

<sup>22</sup> This assumption is appropriate for one-sided platforms, where the benefit for each participant of increasing network size is typically rapidly increasing in the beginning, and below a certain network size the platform may not even be viable; but as the network size continues to increase, this benefit typically tapers off. Filecoin, for instance, benefits from the law of large numbers to assure individual users that adequate storage will be available to meet their needs, and whereas this benefit grows with the size of the network, the returns are diminishing.

<sup>23</sup> Having tokens provide access for all remaining periods simplifies our analysis, however our results also apply to a setting where plat form participants need to use a new token in each period and tokens for both periods can be purchased by the early adopters upon arrival.

<sup>24</sup> The network effects in our setting are always positive; that is, there is no congestion. Therefore, partial adoption can only occur in equilibria with mixed strategies. In such an equilibrium, all users are indifferent between adopting and not adopting, given the price (p) and a fraction of users who join (q). This fraction q is a deterministic and increasing function of p, which means that if the platform sets a higher price, then there is a mixed-strategy equilibrium only if more users would join at the higher price.

<sup>25</sup> It is likely, for instance, that Sony’s desire to overcome the history of having lost the Betamax versus VHS format war and to avoid the reputation implications of another loss, contributed to its aggressive adoption strategy for the BluRay format, such as heavily subsidizing the inclusion of a BluRay drive in the PlayStation 3 game console in order to increase the number of consumer devices capable to play BluRay movies.

<sup>26</sup> The terminology in the platforms literature varies. Fudenberg and Tirole (2000) assume that in the presence of two equilibria, adopting and not adopting, the market will coordinate on adopting as the focal equilibrium—although they do not explicitly use the “focality” label. Caillaud and Jullien (2001; 2003) use “favorable beliefs” to denote a focal equilibrium with successful adoption, and “unfavorable” or “pessimistic beliefs” to denote a focal equilibrium without adoption.

<sup>27</sup> Game-theoretical analysis typically takes beliefs as given and is more concerned with what type of beliefs constitute equilibrium, rather than how the beliefs are formed. How do users arrive at the conviction that all other users will join at any price p V 1 , or conversely that no user will join at the same price? As mentioned ear lier, these beliefs may be formed based on the history of successes and failures of a platform itself, the reputation of the platform developer, marketing of the platform, expert opinions, or other sources of information.

<sup>28</sup> Halaburda and Yehezkel (2016) formally analyze and apply partial focality (calling it “coordination bias”) in a specific setting Halaburda and Yehezkel (2019) extend that formulation, introduce the term “partial focality,” which we use in this paper, and provide a more general formalization linked to the established concept of focal equilibrium.

<sup>29</sup> That is because the threshold and equilibrium prices for the case of $s _ { 1 } = 1$ stay as derived in Section 4.2, and when $s _ { 1 } = 0 ,$ , there is no role for tokens in period $^ { 2 , }$ as there are no exiting users that will be selling their tokens. In other words, the focality may be negatively affected if the platform fails in period 1, but that will not affect the comparison between using and not using tokens.

<sup>30</sup> This mechanism in our model reflects the most common ICO mechanism, namely, a posted token price, as described in the introduction

<sup>31</sup> If adoption failed in period 1, then there is no difference in providing access in period 2 by selling tokens or by setting a price to join the platform.

<sup>32</sup> The full derivation of $\lambda ^ { N T } , ~ P _ { 2 } ^ { N T }$ and other NT variables is in Online Appendix A.2.

<sup>33</sup> We can omit $s _ { 1 } = 1$ without ambiguity, as it is the focus of our analysis. If adoption fails in period 1 and $s _ { 1 } = 0 ,$ , then there is no secondary market for tokens in period $_ { 2 ; }$ the platform issues either $n _ { 1 } + n _ { 2 }$ tokens or no tokens in period 2, and the outcome is identical to selling access in a setting without tokens.

<sup>34</sup> The threshold $k ( \tau _ { 2 } , p _ { 2 } )$ also depends on n<sub>1</sub> and ${ \boldsymbol { n } } _ { 2 } ,$ which, as stated earlier, we omit from our notation, as they are fixed parameters of the setting.

<sup>35</sup> The full derivation of $P _ { 2 } ^ { N T }$ and the other variables for the case with no tokens is given in Online Appendix A.2.

<sup>36</sup> We analyze settings without a potential resale market in Online Appendix $G ,$ where we allow for uncertainty about the size of n<sub>2</sub>.

<sup>37</sup> We assume that the platform sets τ<sub>2</sub> at t <sub>-</sub> 2, and thus maximizes $t = 2 ,$ the second-period profits. Technology of cryptographic tokens allows the platform to commit to $\tau _ { 2 }$ at $t = 1$ . In the latter case, the platform would set $\tau _ { 2 }$ to maximize the overall profit Π. As we show in Online Appendix $\scriptstyle \mathrm { E , }$ whereas such commitment can increase the overall profits, it does not change any results presented in Section 5.

<sup>38</sup> As mentioned earlier, if the parameters of the setting do not sustain such dynamics, then there is no resale market for tokens, and issuing tokens cannot improve on the equilibrium with subsidy analyzed in Online Appendix A.2.

<sup>39</sup> There is an extensive literature on trust based on reputation or a brand (e.g., Nelson 1974, Kreps et al 1982, Maskin et al. 1994, Tadelis 1999, Bakos and Dellarocas 2011) or based on organizational size and incumbency $( \mathrm { e . g . } ,$ Holmstrom and Milgrom 1994, La Porta et al. 1997).

<sup>40</sup> The platform may also improve the market’s bias in its favor as a result of its period 1 success, that is, $\alpha _ { 2 }$ may be higher, which also makes the coordination problem in period 2 easier.

<sup>41</sup> Subsidies are often difficult to execute, for instance, because of costly administration or the need to limit abuse by potential users.

<sup>42</sup> Hagiu (2006) shows how the ability of a platform to commit to certain actions would expand its available pricing strategies and thus change the pricing game and the resulting equilibrium.

<sup>43</sup> Competition may drive the initial price of tokens to zero, which may be an explanation for recent “airdrops” of tokens for compet ing Decentralized Finance (DeFi) platforms.

## References

Aloosh A, Li J (2019), Direct evidence of bitcoin wash trading. Preprint, submitted June 3, https://dx.doi.org/10.2139/ssrn.3362153.

Amihud Y, Mendelson H (1986) Asset pricing and the bid-ask spread. J. Financial Econom. 17:223–249.

Amiram D, Lyandres E, Rabetti D (2021), Competition and product quality: Fake trading on crypto exchanges. Preprint, submitted January 12, https://dx.doi.org/10.2139/ssrn.3745617.

Bakos Y, Dellarocas C (2011) Cooperation without enforcement: A comparative analysis of litigation and online reputation as quality assurance mechanisms. Management Sci. 57(11):1944–1962.

Bakos Y, Halaburda H (2019) Funding new ventures with digital tokens: Due diligence and token tradability. Preprint, submitted March 7, https://dx.doi.org/10.2139/ssrn.3335650.

Bulow JI (1982) Durable-goods monopolists. J. Political Econom. 90(2): 314–332.

Catalini C, Gans J (2018) Initial coin offerings and the value of crypto tokens. Preprint, submitted March 13, https://dx.doi.org/ 10.2139/ssrn.3137213.

Caillaud B, Jullien B (2001) Competing cybermediaries. Eur. Econom. Rev. 45(4–6):797–808

Caillaud B, Jullien B (2003) Chicken and egg: Competition among intermediation service providers. RAND J. Econom. 34(2): 309–328.

Chod J, Lyandres E (2021) A theory of ICOs: Diversi<sup>fi</sup>cation, agency, and information asymmetry. Management Sci. 67(10):5969–5989.

Chod J, Trichakis N, Yang SA (2022) Platform Tokenization: Financing, Governance, and Moral Hazard. Management Sci., ePub ahead of print March 8, https://doi.org/10.1287/mnsc.2021.4225.

Coase R (1972) Durability and monopoly. J. Law Econom. 15(1):143–149.

Cong L, Li Y, Wang N (2018) Tokenomics: Dynamic adoption and valuation. Preprint, submitted July 30, https://dx.doi.org/10. 2139/ssrn.3222802.

Cong L, Li X, Tang K, Yang Y (2020) Crypto wash trading. Preprint, submitted March 2, https://doi.org/10.2139/ssrn.3530220.

Constantinides GM (1986) Capital market equilibrium with transac tion costs. J. Political Econom. 94:842–862.

Duf<sup>fi</sup>e D, Rleanu NG, Pedersen LH (2005) Over the counter markets. Econometrica 73(6):1815–1847.

Evans DS, Hagiu A, Schmalensee R (2006) Invisible Engines: How Software Platforms Drive Innovation and Transform Industries (MIT Press, Cambridge, MA).

Fudenberg D, Tirole J (2000) Pricing a network good to deter entry. J. Indust. Econom. 48(4):373–390.

Gan R, Tsoukalas G, Netessine S (2021a) Initial coin offerings, speculation, and asset tokenization. Management Sci. 67(2): 914–931.

Gan R, Tsoukalas G, Netessine S (2021b) To in<sup>fi</sup>nity and beyond: Financing platforms with uncapped crypto tokens. Preprint, submitted February 1, https://dx.doi.org/10.2139/ssrn.3776411.

Gandal N, Hamrick JT, Moore T, Oberman T (2018) Price manipulation in the Bitcoin ecosystem. J. Monetary Econom. 95: 86–96.

Gans J, Halaburda H (2015) Some economics of private digital currency. Goldfarb A, Greenstein S, Tucker C, eds. Economic Analysis of th Digital Economy (University of Chicago Press, Chicago).

Garman MB (1976) Market microstructure. J. Financial Econom. 3:257–275.

Ghose A, Telang R, Krishnan R (2005) J. Management Inform. Systems 22(2):91–120.

Hagiu A (2006) Pricing and commitment by two-sided platforms. RAND J. Econom. 37(3):720–737.

Hagiu A, Spulber D (2013) First-party content and coordination in two-sided markets. Management Sci. 59(4):933–949

Halaburda H, Yehezkel Y (2016) The role of coordination bias in platform competition. J. Econom. Management Strategy 25(2): 274–312.

Halaburda H, Yehezkel Y (2019) Focality advantage in platform competition. J. Econom. Management Strategy 28(1):49–59.

Halaburda H, Jullien B, Yehezkel Y (2020) Dynamic competition with network externalities: Why history matters. RAND J. Econom. 51(1):3–31.

Halaburda H, Sarvary M, Hearinger G (2022a) Beyond Bitcoin: The Economics of Digital Currencies and Blockchain Technologies, 2nd ed. (Palgrave Macmillan, New York).

Halaburda H, Hearinger G, Gans J, Gandal N (2022b) The microeconomics of cryptocurrencies. J. Econom. Lit. Forthcoming.

Holmstrom B, Milgrom P (1994) The <sup>fi</sup>rm as an incentive system. Amer. Econom. Rev. 84(4):972–991.

Howell S, Niessner M, Yermack D (2020) Initial coin offerings: Financing growth with cryptocurrency token sales. Rev. Financial Stud. 33(9):3925–3974.

ICO Bench (2020) ICO Stats and Facts. Accessed at https://icobench. com/stats on January 10, 2020.

Katz ML, Shapiro C (1986) Technology adoption in the presence of network externalities. J. Political Econom. 94(4):822–841.

Kreps DM, Milgrom P, Roberts J, Wilson R (1982) Rational coopera tion in the <sup>fi</sup>nitely repeated prisoners dilemma? J. Econom. Theory 27(2):245–252.

La Porta R, Lopez-de-Silanes F, Shleifer A, Vishny RW (1997) Trust in large organizations. Amer. Econom. Rev. 87(2):333–338.

Lee J, Parlour C (2022) Consumers as <sup>fi</sup>nanciers: Consumer surplus, crowdfunding, and initial coin offerings. Rev. Financial Stud. 35(3):1105–1140.

Lehar A, Parlour C (2021) Decentralized exchanges. Preprint, submit ted August 16, https://dx.doi.org/10.2139/ssrn.3905316.

Li J, Mann W (2017) Digital tokens and platform building. Preprint, submitted December 17, https://dx.doi.org/10.2139/ssrn.3088726.

Lyandres E, Palazzo B, Rabetti D (2018) Do tokens behave like securities? An anatomy of initial coin offerings. Preprint, sub mitted December 12, https://dx.doi.org/10.2139/ssrn.3287583.

Malinova K, Park A (2018) Tokenomics: When tokens beat equity. Preprint, submitted December 2, https://dx.doi.org/10.2139/ ssrn.3286825.

Maskin E, Fudenberg D, Levine D (1994) The folk theorem with imperfect public information. Econometrica 62(5):997–1039.

Mayer S (2019) Token-based platforms and speculators. Preprint, submitted October 28, https://dx.doi.org/10.2139/ssrn. 3471977.

McIntyre DA (2009) Failure to launch: HD-DVD. Time (May 14) http://content.time.com/time/specials/packages/article/0,28804, 1898610\_1898625\_1898629,00.html.

Nelson P (1974) Advertising as information. J. Political Econom. 82(4): 729–754.

Schelling T (1960) The Strategy of Conflict (Harvard University Press, Cambridge, MA).

Shakhnov K, Zaccaria L (2020) (R)evolution in entrepreneurial <sup>fi</sup>nance? The relationship between cryptocurrency and venture capital markets. Preprint, submitted June 12, https://dx.doi. org/10.2139/ssrn.3613261.

Shapiro C, Varian H (1998) Information Rules: A Strategic Guide to the Network Economy (Harvard Business School Press, Boston).

Sockin M, Xiong W (2020) A model of cryptocurrencies. Preprint, submitted March 9, https://ssrn.com/abstract=3550965.

Sockin M, Xiong W (2022) Decentralization through tokenization Preprint, submitted February 7, https://ssrn.com/abstract= 4028336.

Tadelis S (1999) What’s in a name? Reputation as a tradable asset Amer. Econom. Rev. 89(3):548–563.

Vayanos D (1998) Transaction costs and asset prices: A dynamic equilibrium model. Rev. Financial Stud. 11:1–58.

Westland JC (2021) Trade informativeness and liquidity in Bitcoin markets. PLoS One 16(8):e0255515.

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
