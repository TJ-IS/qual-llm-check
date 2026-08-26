---
otero_id: 28360
otero_key: "UR5TSQG9"
title: "Development Trajectory of Blockchain Platforms: The Role of Multirole"
authors: "Tianyi Li; Xiaoquan (Michael) Zhang"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0243"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development Trajectory of Blockchain Platforms: The Role of Multirole

Tianyi Li,<sup>a</sup> Xiaoquan (Michael) Zhang<sup>a,b,</sup>\*

<sup>a</sup> Department of Decisions, Operations and Technology, CUHK Business School, Chinese University of Hong Kong, Shatin, Hong Kong, China; <sup>b</sup> Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing 100084, China \*Corresponding author

Contact: tianyi.li@cuhk.edu.hk, https://orcid.org/0000-0002-4654-9862 (TL); zhang@cuhk.edu.hk, https://orcid.org/0000-0003-0690-233 (X(M)Z)

Received: April 11, 2022 Revised: January 29, 2023; June 15, 2023 Accepted: July 29, 2023 Published Online in Articles in Advance: October 13, 2023

https://doi.org/10.1287/isre.2022.0243

Copyright: © 2023 INFORMS

Abstract. We develop a parametric model that investigates the development trajectories of blockchain platforms, accounting for the feedback between blockchains’ utility change and people’s adoption and abandonment behavior. A typical blockchain participant is considered to simultaneously play three roles on the platform, user, investor, and laborer, each contributing a unique element to blockchains’ multifaceted utility. The model predicts a three-phase development trajectory for blockchain platforms: a chaotic initial stage, a rapid growth stage, and a mature stage of stable market cycles. The roles have different functions at different developmental stages, and their interactions determine phase transitions. Th model was used to match 112 token price series, demonstrating robust performance across different fitting setups and outperforming existing models. The study identifies two temporal parameters—the time delay in quitting the platform and the holding time of the platform’s token—that significantly differentiate blockchains’ development trajectories. We also extend the model to study forking events, finding that fork launch time is more important than forking amplitude in influencing the main chain’s subsequent development and that forking can increase the exposure of the forked platform.

History: Yong Tan, Senior Editor; Yan Huang, Associate Editor. Funding: This work was supported by the Research Grants Council, University Grants Committee [Grants GRF 14500521, GRF 14501320, GRF 14503818, GRF 165052947, and TRS:T31-604/18-N]. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.0243.

Keywords: blockchain • digital platform • user participation • technology adoption • platform development

## 1. Introduction

Digital platforms rely on various mechanisms to increase adoption, gain market share, and maintain popularity (Dellarocas et al. 2007, Tiwana et al. 2010, Parker et al. 2016, Brynjolfsson et al. 2021). Understanding the growth of these platforms is critical to digital platform management, thus drawing considerable attention from academics. Traditional Bass diffusion models (Bass 1969, Mahajan et al. 1991) are not effective in capturing the complexity of today’s digital platform development. Whereas the Bass model is primarily based on “S-shaped” adoption and saturation, the development of new platforms follows more intricate patterns (Haki et al. 2020), necessitating consideration of the heterogeneous multiple roles and actions of platform adopters.

In this paper, we suggest analyzing platform development by considering the multiple roles performed by participants on the platform. For instance, on Wikipedia, a reader can also be a writer, moderator, administrator, or donor (Zhang and Zhu 2011, Zhang and Wang 2012, Xu and Zhang 2013); On Facebook, a user may derive multiple utilities from writing, liking, commenting, posting pictures, reading news, playing games, and organizing group activities (Claussen et al. 2013). Over time, different participation roles may have different effects on platform development. Without considering the multifaceted nature and role switching in platform participation, diffusion-based models can provide insufficient insights into complex platform growth dynamics.

We study platform growth in the context of blockchain platforms. We propose a novel parametric model to gain insight into the development trajectories of blockchain platforms, which have seen impressive growth within the past decade. This model distinguishes itself from existing platform development models by incorporating participants’ multiple roles as users, investors, and laborers. As a result, it provides a transparent, comprehensive analysis of blockchain platform development and its associated growth.

We present a representative three-phase development model for blockchain platforms, consisting of an initial chaotic stage of project launch, a rapid intermediate growth stage, and a mature stage of stable market cycles. Through analyzing the price histories of 112 blockchain tokens, our model outperforms alternative scaling models, including exponential, power-law, polynomial, and the netoid function, for network growth. We observe two temporal parameters that are effective categorizers of growth patterns: the time delay in quitting the platform and the holding time of the platform’s token. Additionally, our model is extended to analyze forking events on blockchains, which suggests that the launch time of the forking chain (i.e., the derivative) relative to the main chain’s (i.e., the forked platform’s) stage of development is more crucial than the amplitude of the forking event. Counterintuitively, forking events can be beneficial to the main chain, when those events increase exposure to the forked platform.

The rest of the paper is organized as follows. In Section 2, we introduce research background on blockchains, participants’ multiple roles, and technology adoption. We develop the model in Section 3 and discuss system parameters in Section 4. Analyzing model dynamics, we study platform’s development trajectories in Section 5. A representative three-phase development is analyzed, based on which we identify different modes of platforms lifespan and investigate the functions of key model parameters. In Section 6, we use the model to match a data set of 112 token price series. Fitting performance is anchored on scaling models (exponential, power-law, polynomial, the netoid function, exponential power-law) and evaluated with seven robustness checks. In Section 7, we extend the model to investigate forking events. The paper is summarized in Section 8. We conclude and point out limitations and future research directions. In Section 9, we revisit the overarching idea of platform participants multiroles and present the research outlook.

## 2. Background

## 2.1. The Setting: Blockchain

The emergence of blockchain technology has created a vibrant and rapidly growing industrial sector, with its invention of Bitcoin (Nakamoto 2008) and Ethereum (Wood 2014) sparking extensive attention, and creative minds using it to revolutionize various sectors, from healthcare (Mettler 2016), transportation (Yuan and Wang 2016), digital contents sharing (Sharples and Domingue 2016), to cloud data management (Zhu et al. 2019), supply chains (Min 2019), and energy (Andoni et al. 2019). It is particularly noteworthy in the financial sector (Tapscott and Tapscott 2016, Beck et al. 2017), where blockchains are at the forefront of FinTech (Zhang and Zhang 2015, Hendershott et al. 2021). This innovative technology has been likened to the milestone invention of TCP/IP protocol (Iansiti and Lakhani 2017) and is seen to have great potential when combined with Internet of Things (IoT) (Reyna et al. 2018) and artificial intelligence (AI) (Salah et al. 2019).

Despite the tremendous advances made in blockchain applications, academic research into blockchain as a novel type of digital platform is still in its early stages (Beck et al. 2017, Risius and Spohrer 2017). Most studies focus either on the technical aspects of this new online infrastructure or on its subordinate role as the founda tion for cryptocurrencies (Tschorsch and Scheuermann 2016, Altan et al. 2019).

As an important digital platform category (Tiwana et al. 2010, Parker et al. 2016), blockchain merits further examination in terms of its growth dynamics.

(1) Blockchain technology has seen a surge in popularity among market adventurers in a relatively short period of time, making it easier to conduct cross-sectional analysis. This is typically difficult because only a few members tend to compete in the same market and waves of innovation occur at different stages (Kanter 2006). Through studying the development trajectories of different blockchains, various modes of development can be identified, such as slow initial growth, rapid expansion of the adopter population with market fluctuations, recurrent upswings and downturns in market cycles, and a series of bubbles and crashes (ElBahrawy et al. 2017).

(2) Blockchain’s design facilitates the public availability of structured data that records the platform’s development history. These data are transparent, traceable, verifiable, and highly detailed, enabling researchers to study the intricate dynamics of technology adoption in greater depth. With a data set of high quality, we can gain a deeper understanding of the platforms’ competition and scalability (Constantinides et al. 2018).

(3) Inertia and time delay are key factors in the adoption of technology, and this is particularly evident in the blockchain space. Participants may switch back to banking payments after using bitcoins, but they are unlikely to abandon the platform abruptly due to their investment in tokens or mining, which have a fixed cost on hardware. Through the blockchain, we can directly and quantitatively analyze the inertia of platform adoption and abandonment, which reflects the behavioral constraints of online participants (Dong and Saha 1998) and the ability of digital platforms to sustain users’ repeated engagement (Constantinides et al. 2018, Chod et al. 2021), respectively.

(4) Blockchain technology can be used as an online labor platform (Berinsky et al. 2012), providing a unique opportunity to study the factors that influence platform development. Pricing strategies for online tasks (Chen and Horton 2016) on other labor platforms may also be applied to blockchain-based labor rewards. It is important to note that blockchain labor comes with both high rewards and high risks and may be more effective than other online labor platforms in reducing lower-quality entrepreneurial activities (Burtch et al. 2018).

(5) Studies on technology adoption have traditionally considered the complementarities and competition between technologies (Colombo and Mosconi 1995), such as how the diffusion of one technology may interact with other related technologies. However, the rapid diffusion of blockchain technology has largely eliminated the need to take other technologies into account when analyzing its adoption. This simplifies the process of studying blockchain adoption, allowing us to focus exclusively on blockchains.

## 2.2. Driver: Participants’ Multiple Roles

The diffusion of blockchain applications has been rapid and unstoppable (Queiroz and Wamba 2019). This rapid adoption can be understood from the traditional perspective of technology maturity and readiness (Wang et al. 2016), and with established models of technology acceptance (Dwivedi et al. 2019) or with new models capturing key aspects of blockchain’s functionalities (e.g., dynamic asset price model (Cong et al. 2021), gametheoretical model (Huberman et al. 2021)). Wong et al. (2020) provide a review of blockchain adoption models. Nevertheless, it is rare to see this level of hype among traditional platforms, and the adoption of blockchains captures the complex relationship between institutional, market, and technical factors (Bo¨hme et al. 2015).

Blockchain offers one critical feature to deepen our understanding of platform growth dynamics: It allows us to monitor the multiple roles of users. It is not difficult to imagine a software engineer who uses bitcoin to make payments on e-commerce websites and works as an Ethereum miner in his spare time. In addition, he may also choose to purchase more tokens as a means of investment. Indeed, intrinsic design features have made blockchains multifunctional, and the different roles that participants play in the chain enable different activities in the ecosystem. Essentially, this multirole feature allows blockchains to accumulate initiation from participants, which helps overcome the challenge of a cold start in network dynamics (Constantinides et al. 2018). The multifacet utility also underlines that the success of digital platforms does not solely rely on network effects but depends on quality factors that determine platforms functionalities (Tellis et al. 2009, Zhu and Zhang 2010), as is universal for technological artifacts (Roberts and Urban 1988, Hao et al. 2018).

Enabling participants’ multiple roles complements the interconnectivity of a digital platform with its locality. Participants can engage in both “non-local markets” (e.g., transact with and invest in different tokens) and “local markets” (e.g., mine the blocks of specific chains). This enhanced locality ensures that entrant platforms are not deterred by incumbents (Zhu et al. 2021), although it is never the case in the platform economy that the winner takes all (Cennamo and Santalo 2013). The juxtaposition of early-stage and later-stage platforms nevertheless poses a challenge to the generalizability of platform development models. Early-stage and later-stage development differ substantially in growth patterns (Zhu and Iansiti 2012) because of network effects (Niculescu et al. 2018) and the effect of multihoming (Anderson et al. 2019), and so on. An inclusive platform development model must therefore distinguish different development stages.

In this study, we build a differential equation model to study blockchain platform development trajectories (Yang et al. 2019). We consider blockchains’ utilities for adopters and construct a dynamic utility function, tak ing advantage of the solvability of compartment models and the comprehensibility of utility models (Han et al. 2016), particularly from the dynamic perspective (Geroski 2000). We capture three utility terms that correspond to the three roles that participants typically play on blockchains.

First, participants use blockchains to perform transactions. In their most common form, blockchain tokens often serve as a form of payment. Cryptocurrencies have proven to be too volatile to be used as a conventional currency (Yermack 2015), but the financial capabilities of blockchain technology have been widely recognized. Network effects are a key component of blockchain’s utility as a medium for transactions and interactions; as the population of a platform increases or decreases, the value of the associated token is correspondingly inflated or deflated.

Second, cryptocurrencies have become a popular asset class for individual investors, as evidenced by the proliferation of crypto transaction platforms (Burniske and Tatar 2018). Decentralization is a key factor driving market confidence, as crypto-networks provide an alternative to traditional financial systems (Risius and Spohrer 2017) and are thought to be the future of financing (Zheng et al. 2017).

Third, blockchains offer a unique opportunity for digital labor in the form of mining blocks. The broad access and constant availability of digital labor provide a way to incentivize early adopters, who are essential to the network’s expansion. Early adopters can earn token rewards through digital labor and may hold onto these tokens as an asset to generate future profits. This creates a financial incentive for them to remain in the network and help the platform’s growth.

The core design of enhanced digital labor accessibility facilitates the launching of blockchain platforms through ICO (initial coin offering) events (Howell et al. 2020, Chod and Lyandres 2021). These events can help ventures avoid coordination problems (Catalini and Gans 2018) by providing an advanced form of crowdfunding that lowers the bar for platform entrance, despite the danger of elevated market competition and new costs (Catalini and Gans 2020). Rewarding user engagement is a key factor in the long-term development of online platforms (Claussen et al. 2013), especially those enabling crowdfunding functions (Kim et al. 2022), although the effect is not always positive (Khern-am-nuai et al. 2018).

Additionally, enabling and encouraging labor may indicate that a platform’s third-party complementors, particularly multihoming complementors (Cennamo et al. 2018), can play a nontrivial role in its development and success (McIntyre and Srinivasan 2017).

## 2.3. Mechanism: Technology Adoption

Diffusion is a major factor in the adoption of technology (Besley and Case 1993, Jackson 2010, Newman 2010), with classic models demonstrating S-shaped patterns of adoption (Bass 1969, Geroski 2000). Word-of-mouth (WOM) is a common diffusion mechanism (Godes and Mayzlin 2004, Dellarocas et al. 2007, Adamopoulos et al. 2018), which leads to rapid early-stage growth and a gradual decrease in growth until adoption saturates (Brandyberry 2003). As the diffusion of new products and services has become increasingly complex and multifaceted (Peres et al. 2010), the S-curve lacks sufficient resolution to describe the development of adoption. Moreover, compared with the adoption of offline technologies, the adoption of digital technologies is faster, on a larger scale, but more transient (Ghobakhloo and Ching 2019). The proliferation of digital technologies and the ubiquity of platform-based markets have made it easier and less expensive to switch between services online (Zhu and Iansiti 2012).

The adoption of digital platforms themselves is even more complex. Critical dynamics such as bubbles (Martin and Ventura 2012) and oscillations (Anderson 2018) are not revealed by S-curves but play important roles during the development of digital platforms. Digital platform development is influenced by substantial network effects (Weitzel et al. 2006, Katona et al. 2011, Niculescu et al. 2018, Song et al. 2018): objective factors such as structures (Manshadi et al. 2020), conduct (Afuah 2013), and externalities of networks (Tucker 2008), and subjective factors such as seeding (Dou et al. 2013), pricing (Leduc et al. 2017), and social media (Luo et al. 2013) strategies complicate the adoption and abandonment of digital platforms. Models that recognize the interactions between multiple drivers of network development could reveal higher-order platform development patterns.

Technology adoption is also associated with substantial inertia. Structural inertia is prevalent in organizations (Hannan and Freeman 1984); inaction inertia is prominent in participants’ decision-making (Steiner et al. 2017), even in the highly rational stock market (Tykocinski et al. 2004). On digital platforms, there is great inertia both during the adoption of the platform $( \mathrm { e . g . , }$ , delay in action) and during its abandonment (e.g., cost of switching). These behavioral factors further complicate the diffusion dynamics and induce market cycles along with platform development. Arguably, the success of many digital platforms is due to their ability to create sufficient inertia for clients; conversely, the failure of platforms may be due to their failed attempts at creating user inertia. Inertia is an important component when model ing the oscillatory dynamics of platform development.

Models considering explicit network-connectivity information (e.g., network autocorrelation model (Fuji moto and Valente 2012), exponential random graph model (Robins et al. 2007)) are important tools when analyzing the specific diffusion pattern of individual networks (Zhang et al. 2018). Nevertheless, as connectivities are rapidly evolving on blockchain networks (Miller et al. 2015) and different blockchains feature different network topologies (Xiao et al. 2020), it is difficult to construct a connectivity-oriented model for blockchain platforms development that would have sufficient explanatory and prescriptive power across different platforms. In this study, we consider instead an intermediate model resolution and use a compartment model to specify platform adoption and abandonment, building on S-shaped dynamics while overlooking topology-induced dynamics. Model resolution is commensurate with the resolu tion of data and of policy analysis. We do not concern specific behavioral features that influence adopters’ decisions (Centola 2010). Methodologically, overlooking network-connectivity information dismisses the estimation of node- or edge-specific attributes (e.g., via Bayesian learning methods (Hao et al. 2018)), which otherwise may considerably enlarge models’ parameter space and substantially reduce models’ interpretability.

Drawing on the previous three aspects, this study fills in this research gap and constructs a transparent parametric model to study blockchain platform development.

## 3. Model

Suppose a blockchain platform has a participant population of $\eta = \eta ( t )$ . We consider that property f of the blockchain is characterized by its population at a specific time step. This is certainly a simplification; we would like to focus on participants’ population and ignore other dynamic factors that determine the property of a block chain, such as participants’ activity level, platform token’s transaction volume, and so on. Many such factors are essentially based on platform population, the dynamics of which is influenced by platform adoption; thus, at the ground level, $f = f ( \eta , t )$ . For example, per Metcalfe’s law (Metcalfe 1995), the value of the platform V(t) is proportional to the number of peer-to-peer interactions that it can potentially support on the network, that is, $V ( t ) \propto \eta ( t ) ^ { 2 }$

## 3.1. Multifaceted Utility of Blockchain

We construct a dynamic multifaceted utility function for ordinary blockchain participants, considering utility for a representative blockchain participant whose on-platform activities indicate platform-average conditions. We sepa rate the different roles participants play on blockchains, corresponding to the different activities they engage in. A typical participant on a blockchain (e.g., the bitcoin chain)

is primarily playing three distinct roles: user (e.g., using bitcoin as the transaction medium), investor (e.g., purchasing bitcoin as a digital asset), and laborer (e.g., mining bitcoin blocks to earn rewards). Besides these three roles, on a blockchain platform, participants play other roles such as developers, online service providers, or even founders/practitioners of subchain structures. These roles are relatively rare for ordinary participants. In a sense, these workloads could be viewed as engaging in different types of labor and can be included in the broad term “laborer.” Such core laborers are currently not scalable to the entire platform in most cases, and our notion of “laborer” attaches closely to “miner,”<sup>1</sup> although participants expect mining in the current form to represent an increasingly smaller proportion of crypto labor within the blockchain ecosystem (Truby 2018) due to its intensive energy consumption (Li et al. 2019).

There are blockchains that do not support the investor’s role (e.g., whose platform tokens are not freely transacted) or do not support the laborers’ role (e.g., where crypto-laboring is not scalable to general participants or when platforms are not using supporting consensus mechanisms). Our results are generalizable to the context when the three roles are all present. When there are more or fewer roles, the proposed methodology can be applied with modifications. We aim to provide a novel way of examining platform development trajectories, and in this sense, the model is not severely limited by the three captured functionalities. For example, emerging platforms that support nonfungible tokens (NFT) essentially support a fourth role for blockchain participants: as creators/performers. This points to an additional term, platform utility u, which can be potentially captured in an extended model.

Excluding the types of blockchain where the current three-component model may not directly apply leaves a majority of existing blockchain platforms as the target for modeling: as surveyed in Lashkari and Musilek (2021), among a panel of >100 blockchain platforms reviewed, at least 40% have tokens as digital assets/ cryptocurrency, and 38% are associated with scalable crypto-laboring, besides other means of realizing the investor’s role and the laborer’s role. On a larger scale, as of 2021, at least 45% of respondents stated that their companies were working on use cases based on blockchain technology (statista.com), and it is expected that a major part of blockchain adoption is associated with issuing tokens, under the estimate that almost 15% of U.S. individuals had conducted transfers into crypto accounts as of mid-2022 (jpmorganchase.com), and there are approximately 22,932 cryptocurrencies as of March 2023, with a total market capitalization of 1.1 trillion USD (coinmarketcap.com). Watch lists tracking up to the top 500 mineable tokens (e.g., coinlore.com) confirm that on a substantial proportion of blockchains, clear access to crypto labor is provided; such is the case for four of the top 10 cryptocurrencies.<sup>2</sup> Conversely, the possibility of a fourth role enabled by NFT, as mentioned previously, is currently limited to few platforms, where Ethereum is the dominant home of NFT activity and trading, making up 76% of all NFT volume.<sup>3</sup> These statistics underline the current model’s scope of application.

Formally, in the model, aggregate utility u evolves over time, collecting utilities from the three roles, each being a function of population η(t). Compositions of the three roles are characterized by coefficients $\alpha _ { 1 / 2 / 3 } \colon$

$$
u (\eta , t) = \alpha_ {1} u _ {u s e r} (\eta) + \alpha_ {2} u _ {i n v e s t o r} (\eta) + \alpha_ {3} u _ {l a b o r e r} (\eta).\tag{1}
$$

When any role is not supported on a certain platform, the corresponding composition is $\alpha = 0$ (Section 6.4.2). All three utility terms (and thus the aggregate utility u) have the U.S. dollar as the unit (Section 4). The three util ity terms are modeled as follows.

3.1.1. As a (Pure) User. Blockchains have both advantages and disadvantages over traditional digital platforms. They offer more transaction transparency and greater transaction freedom than traditional networks backed up by third parties. However, as is common for rapidly emerging technologies, blockchains suffer from a number of technology inefficiencies (i.e., “digital debts” (Ramasubbu and Kemerer 2016, Rolland et al. 2018)), such as slow operation or transaction unavailability, which is not rare on bitcoin. This tradeoff is captured by the CAP (consistency, availability, and partition tolerance) theorem (Brewer 2000): Blockchains sacrifice availability to maintain perfect consistency compared with traditional networks that highlight availability and thus do not support perfect consistency.

Blockchains also inherit the disadvantages of traditional platforms. For the ordinary user, the utility of the platform reaches its peak when the user maintains a certain number of online connections (e.g., contacts in the bitcoin wallet) and starts to decline when the user makes even more friends. This decline derives from the inconvenience induced by online traffic, such as misinformation (Del Vicario et al. 2016) and excessive usage (Spilkova et al. 2017), among various negative effects of social media (Siddiqui and Singh 2016). Before the peak, the utility curve as a function of the number of connections is close to an S-shape (Cong et al. 2021), growing quickly and gradually becoming saturated; beyond the peak, utility slowly drops toward a limit as the number of connections continues to accumulate.

Considering the existence of such an optimal usage utility, we model a blockchain’s usage utility by combining two logistic functions (i.e., the double logistic growth curve (Lipovetsky 2010)):

$$
u _ {u s e r} = \frac {h (\eta_ {i n d} ^ {o p t}) ^ {2}}{1 + q _ {1} e ^ {- \eta_ {i n d} / \eta_ {0} ^ {+}}} - \frac {\phi h (\eta_ {i n d} ^ {o p t}) ^ {2}}{1 + q _ {2} e ^ {- (\eta_ {i n d} - \eta_ {i n d} ^ {o p t}) / \eta_ {0} ^ {-}}}.\tag{2}
$$

Maximum utility is $h ( \eta _ { i n d } ^ { o p t } ) ^ { 2 }$ , where $\eta _ { i n d } ^ { o p t }$ is the optimal number of connections $\eta _ { i n d }$ for an average user and h is the coefficient. Following Metcalfe’s law (Metcalfe 1995), the use utility for an individual user is proportional to the number of possible interactions that can be made within the user’s community (i.e., the square of $\eta _ { i n d } ) ,$ , either between the user and a neighbor or between two neighbors in the user’s social circle. The latter case captures the indirect utility for the user that derives from the interactions of its neighbors. h is the unit utility generated per interaction (Section 4). Maximum utility drops by the fraction $\phi$ as $\eta _ { i n d }$ goes to infinity. $q _ { 1 } , q _ { 2 } , \eta _ { 0 } ^ { + / - }$ denote the shape of the logistic functions and are fixed at appropriate values.

The number of connections that an individual user has on the platform, $\eta _ { i n d } ,$ is linked to the entire user population η of the platform through the degree of separation (Newman 2010). Per the configuration model in graph theory (Bolloba´s 1980), the average number of l-hop friends of a node with average degree d is approximately d<sup>l</sup>. This translates to $\eta _ { i n d } ^ { l } = \eta$ and $\eta _ { i n d } = \eta ^ { 1 } \dot { / } l ,$ where l is the average degree of separation among all users on the platform. The degree of separation on social media platforms is around three to four (https:// research.fb.com/blog/2016/02/three-and-a-half-degreesof-separation/), and we use $l = 3$ in our model; this number may vary across platforms, but its effect is absorbed in h and $\gamma _ { 0 } ,$ thus we do not set l open as an extra parameter.

3.1.2. As an Investor. Participants purchase blockchain tokens and keep them as financial assets (e.g., bitcoin as the “digital gold”). We consider that the purchase decision is made at each time step t, with $\bar { P } ( t )$ dollars invested, assuming a fixed-interval (Kovalyov et al. 2007) investment scenario at first-order consistency. We assume a basic investment strategy: the investor holds each piece of investment for $t _ { p }$ time steps, so every invested dollar generates interest or suffers loss for exactly $t _ { p }$ periods. Correspondingly, at each time step, the investor collects revenues (positive or negative) from all previous $t _ { p }$ pieces of investment. In the main analysis, we consider a repeated investment with the same amount, $\begin{array} { r } { P ( t ) = P _ { c o n s t } , } \end{array}$ as the platform-average value for a representative participant (see Section 6.4.4 for dynamic $\bar { P ( t ) ) }$ )

For revenue, we assume that the price of the invested token at a certain time step is proportional to the power of the blockchain’s population at that time and inversely proportional to the power of the population at the time of purchase. This is consistent with the supply-demand logic of assets: Token value is inflated with an expanding network, while a shrinking network incurs price deflation. The power-law dependence of price on population also agrees with empirical evidence in financial markets (Lux and Alfarano 2016); however, there are certainly occasions where such dependence may not hold true $( \mathrm { e . g . }$ , stable coins (Mita et al. 2019), nonfungible tokens), and thus this price assumption may not fully apply. We set the power $\beta$ open rather than assuming it to be either linear $( \beta = 1 )$ or quadratic $( \beta = 2 ) ,$ ; this bears the cost of introducing an extra parameter, whereas results suggest that it is a contemplated treatment (see Section 6.3). We consider the opportunity cost of investing in tokens with a constant period interest rate $\epsilon > 0$ , a background interest level if blockchain investors put money into other projects instead. Overall, the utility of the investor role u<sub>investor</sub> is given by

$$
u _ {i n v e s t o r} = \sum_ {k = 1} ^ {t _ {p}} P (t - k) \left[ \left(\frac {\eta (t)}{\eta (t - k)}\right) ^ {\beta} - (1 + \epsilon) ^ {k} \right].\tag{3}
$$

We consider the interests generated from investment and do not count the principal $\textstyle \sum _ { k = 1 } ^ { t _ { p } } P ( t - k ) .$ ; this principal can be viewed as a fixed cost, a constant (because $P ( t ) = P _ { c o n s t } )$ to be dropped in the dynamic utility func tion. Write $\eta _ { t } - \eta _ { t - 1 } = \Delta \eta | _ { t - 1 }$ . Noting the relationship $\begin{array} { r } { \frac { \eta _ { t } } { \eta _ { t - t _ { p } } } = \frac { \eta _ { t } } { \eta _ { t - 1 } } \frac { \eta _ { t - 1 } } { \eta _ { t - 2 } } . . . \frac { \eta _ { t - t _ { p } + 1 } } { \eta _ { t - t _ { p } } } , } \end{array}$ , the positive condition for token investment at time t can be derived (see Online Appendix A for the derivation).

Proposition 1. The sufficient condition for positive invest ment utility at time t is

$$
u _ {i n v e s t o r} > 0 \Leftarrow \frac {\Delta \eta}{\eta} \bigg | _ {m i n} > (1 + \epsilon) ^ {1 / \beta} - 1 \underset {\epsilon \ll 1} {\sim} \frac {\epsilon}{\beta}.\tag{4}
$$

The expression $\frac { \Delta \eta } { \eta } \vert _ { m i n }$ is the minimum value of $\frac { \Delta \eta } { \eta }$ during past $t _ { p }$ periods. Conversely, the sufficient condition for negative investment utility is $\begin{array} { r } { u _ { i n v e s t o r } < 0 \Leftarrow \frac { \Delta \eta } { \eta } | _ { m a x } < } \end{array}$ $\begin{array} { r } { ( 1 + \epsilon ) ^ { 1 / \beta } - 1 \sim \frac { \epsilon } { \beta } } \end{array}$ : The blockchain always generates positive utility for investors if the minimum period-wise network expansion rate $\Big ( \frac { \Delta \eta } { \eta }$ in terms of user population increase in the past $t _ { p }$ periods is greater than the background interest rate ɛ divided by the constant $\beta ;$ the platform generates negative utility for investors if the maximum period-wise network expansion rate in the past $t _ { p }$ periods is smaller than ɛ divided by $\beta .$

3.1.3. As a Laborer. Similar to $P ( t ) ,$ , we assume that a representative blockchain participant conducts L(t) hours of labor within a time step (for those not engaged in crypto-laboring on a regular basis, their fluctuations average out at the representative participant). Keeping first-order consistency, the unit reward of laboring on the blockchain is assumed to be inversely proportional to the number of laborers and proportional to the reward of the unit block (Xue et al. 2021). For the unit block reward, most crypto projects provide a diminishing return as the number of blocks increases (Wang et al. 2019), suggesting an exponential decay (e.g., at bitcoin, block value is reduced by half roughly every four years; https://www.businessinsider.com/bitcoin-halving).<sup>4</sup>

We assume that an hour of labor initially generates revenue $w _ { m } \left( \mathbb { S } / h o u r \right)$ among a minimum population $\eta _ { m i n }$ (e.g., the small community of core members such as key developers). As network expands, the reward is diluted in inverse proportion to network size $\eta _ { t }$ . The associated labor cost is $w _ { 0 } \ ( \$ / h o u r )$ , for example, payment for electricity. Similar to token investment, token laboring is associated with a fixed cost $( \mathrm { e . g . } )$ , hardware) and a constant dropped in the dynamic utility function; we tested a linearly changing $w _ { 0 } ( t )$ in robustness tests, and results show that this time-dependence makes no impact on results. Overall, $u _ { l a b o r e r }$ is given by

$$
u _ {l a b o r e r} = L (t) \left(w _ {m} \frac {\eta_ {m i n}}{\eta_ {t}} e ^ {- t / t _ {0}} - w _ {0}\right).\tag{5}
$$

Similar to (4), the positive condition for laboring at time t can be derived.

Proposition 2. The condition for positive labor utility at time t is

$$
u _ {l a b o r e r} > 0 \Longleftrightarrow \eta_ {t} <   \eta_ {m i n} \frac {w _ {m}}{w _ {0}} e ^ {- t / t _ {0}}.\tag{6}
$$

Laboring on blockchains will be profitable when the population is below a certain threshold; the threshold lowers as time goes by due to the decaying return of unit block reward. Many blockchains claim to encourage subsequent laboring after the laboring population is saturated by offering various fees and bonuses (as is the case with bitcoin), which suggests extra terms for $u _ { l a b o r e r }$ . We exclude these terms, considering that currently most blockchains are not approaching a saturated labor population (Zheng et al. 2017).

## 3.2. Adoption of Blockchain

We model the adoption of blockchain with the SIS (susceptible-infected-susceptible) compartment model (Hethcote 1989), which embodies the WOM mechanism (Godes and Mayzlin 2004). The entire population N is divided into adopters (η) and nonadopters (ζ); $N = \eta + \zeta$ at all time steps. A nonadopter is attracted to the platform and becomes an adopter at rate $\gamma ^ { + } ;$ an adopter abandons the platform at rate $\gamma ^ { - } \colon$

$$
\left\{ \begin{array}{l} \frac {d \zeta}{d t} = - \gamma^ {+} \frac {\zeta \eta}{N} + \gamma^ {-} \eta \\ \frac {d \eta}{d t} = \gamma^ {+} \frac {\zeta \eta}{N} - \gamma^ {-} \eta \end{array} \right..\tag{7}
$$

SIS allows a previous adopter to adopt again after quitting the platform; we consider this to be more realistic than the SIR (susceptible-infected-recovered) model, in which case one cannot come back to the platform after quitting. Moreover, we assume that the entire population is constant, where a person is either an adopter or a nonadopter. To model more detailed adoption, it is possible to extend the adoption module, dividing the population into three compartments in an adoption chain (essentially an SEI (susceptible-exposed-infected) model): nonaccepters (of the blockchain technology), nonadopters (of the specific platform), and adopters (of the spe cific platform). This treatment asks for more parameters and the estimation of the overall market; tests suggest that switching to SEI has negligible effect on model dynamics, and we abandon this more complicated compartment structure.

Participants are attracted to a blockchain when they see the utility of the platform grow, and they leave the platform when they see its utility go down; platform utility embodies its perceived usefulness (as well as its perceived ease-of-use); thus, utility change is associated with adoption activities, adhering to the principle of the technology acceptance model (TAM) (Davis 1989) and the subsequent line of theories (Davis et al. 1989). Here we extrapolate the TAM at (+): adoption based on utility increase, to the inverse process at (�): abandonment based on utility decrease.

We assume that adoption is instantaneous, that is, driven by utility growth at the current period $\left( u _ { t } - u _ { t - 1 } \right)$ whereas abandonment is associated with inertia characterized by time delay τ (Karahanna et al. 1999), that is, driven by utility loss compared with the utility τ periods before $\left( u _ { t - \tau } - u _ { t } \right)$ . The idea is that participants tend to stay on the chain when they see a short-term utility reduction and only leave the network when they see a substantial loss that reverts the utility accumulated during the past τ periods. This inertia may derive from the sunk cost (e.g., mining hardware, token investment, social connections, time cost) or the switching cost (e.g., habituation, cognitive burden). The adoption rate and abandonment rate are thus given by

$$
\begin{array}{l} \gamma^ {+} = \left[ \log \left(\frac {M A X (u _ {t} - u _ {t - 1} , 0)}{\Delta u _ {0}} + 1\right) \right] ^ {K ^ {+}} \gamma_ {0} \\ \gamma^ {-} = \left[ \log \left(\frac {M A X (u _ {t - \tau} - u _ {t} , 0)}{\Delta u _ {0}} + 1\right) \right] ^ {K ^ {-}} \gamma_ {0}. \end{array}\tag{8}
$$

Because we separate the adoption route and the abandonment route, only the positive part of utility gain $u _ { t } - u _ { t - 1 }$ and loss $u _ { t - \tau } - u _ { t }$ determines the adoption/abandonment rate (via the MAX function). The adoption/abandonment rate has a slow-changing dependence on the rapid changing utility term; we take the logarithm of utility change (plus one in the logarithm to avoid negative values). $\gamma _ { 0 }$ is the base adoption/abandonment rate; $K ^ { + }$ and $K ^ { - }$ are exponents characterizing the asymmetric effects in technology adoption and abandonment (Oliveira and Martins 2011); $\Delta u _ { 0 }$ is a scaling constant. Essentially, $K ^ { + }$ and $K ^ { - }$ indicate the contagiousness of a platform: a large K indicates a fluctuating platform where a small change in utility results in a large user entrance or exit, while a small K corresponds to a situation where users are less sensitive to blockchain’s utility change when they adopt or abandon the platform.

We can solve the SIS model analytically (see Online Appendix $\mathrm { A } )$ . The following proposition aggregates Equation (7) as $\begin{array} { r } { \frac { d \eta } { d t } = ( \gamma ^ { + } - \gamma ^ { - } ) \eta - \frac { \gamma ^ { + } } { N } \eta ^ { 2 } } \end{array}$ , derive the condition for positive net adoption.

Proposition 3. The condition for positive net adoption of a blockchain platform is

$$
\frac {d \eta}{d t} > 0 \Longleftrightarrow \frac {\zeta}{N} > \frac {\gamma^ {-}}{\gamma^ {+}} \Longrightarrow \frac {\zeta}{N} > \frac {\left[ \log \left(\frac {M A X (u _ {t} - u _ {t - 1} , 0)}{\Delta u _ {0}} + 1\right) \right] ^ {K ^ {+}}}{\left[ \log \left(\frac {M A X (u _ {t - \tau} - u _ {t} , 0)}{\Delta u _ {0}} + 1\right) \right] ^ {K ^ {-}}}.\tag{9}
$$

Suppose that there is utility gain during the period $t - 1$ to t, that is, $\Delta u = u _ { t } - u _ { t - 1 } > 0$ . In this case, even if the current utility $u _ { t }$ is lower than previous level $u _ { t - \tau } ,$ platform still gains adoption as long as the long-term utility deficit $u _ { t - \tau } - u _ { t }$ is smaller than the current utility gain ∆u by a certain factor, which is determined by the proportion of nonadopters among the entire population, $\gtreqless$ (and sensitivities $K ^ { + } , K ^ { - } )$ . Conversely, suppose a utility loss during period t � 1 to $t ,$ that is, $\Delta u = u _ { t } - u _ { t - 1 } < 0$ . In this case, if the current utility $u _ { t }$ is still higher than the previous level $u _ { t - \tau }$ (by a certain factor), no net abandonment of the platform will take place. Only when the utility continues to decline will a net user decline be triggered. This discussion is almost exact when $K ^ { + } = K ^ { - }$ <sup>�</sup> and $\Delta u \ll \Delta u _ { 0 }$ It qualitatively holds true for more general cases.

As participants transition from $\eta$ back to $\zeta ,$ the utility u may increase due to the platform becoming less congested, potentially leading to a rise in both $u _ { u s e r }$ and $u _ { l a b o r e r } .$ Subsequently, as the ratio of $\zeta / N$ escalates, the condition for positive net adoption is reestablished, attracting participants back to the platform. This feedback mechanism, coordinating changes in platform utility and network size, propels the development of the blockchain. The overarching model is depicted in Figure 1.

## 4. Model Parameters

Model parameters are summarized in Table 1. We use one week as the time step. Parameters can be categorized as network-specific, global, or sensitivity parameters. Network-specific parameters have different values for different blockchain platforms. Global parameters have the same value for different blockchains; they characterize platforms’ general features. Their values are chosen based on real-world considerations and are fixed in empirical analysis, that is, serving as model constants. There are three sensitivity parameters in the model, $\beta , K ^ { + }$ , and $K ^ { - }$ . Different blockchain platforms may have different price $( \beta )$ and adoption/abandonment $( K ^ { + } , K ^ { - } )$ sensitivities; we vary these parameters in the empirical analysis.

• There are three parameters in the overall utility function u: $\alpha _ { 1 / 2 / 3 }$ . They are network-specific, indicating the role compositions of an average participant on a specific blockchain platform. In this study, the three role compositions are assumed to be constant across platform development; this time-invariant assumption is to be relaxed in future analysis with more granularity (see Section 8).

• There are eight parameters in usage utility $u _ { u s e r } .$ They specify the shape of the two logistic functions (Figure A1a in the online appendix). $q _ { 1 } , q _ { 2 } , \eta _ { 0 } ^ { + }$ , and $\eta _ { 0 } ^ { - }$ are constants. $\eta _ { i n d } ^ { o p t }$ is the optimal number of connections for an ordinary user. The number 500 is used, which is the average person’s number of acquaintances (de Sola Pool and Kochen 1978). A more conservative number, 150 (i.e., Dunbar’s number (Dunbar 1992)), derives from the human cognitive capacity to maintain close connections. The (optimal) number of connections in the digital space is, however, much larger than the (optimal) number of close friends, and 500 is a more appropriate number here. Unit utility h generated by each user–user interaction is a network-specific feature

## Figure 1. Model Summary

$$
\text { Multi - facet   utility } \quad u (t, \eta) = \alpha_ {1} u _ {\text { user }} + \alpha_ {2} u _ {\text { investor }} + \alpha_ {3} u _ {\text { laborer }}
$$

$$
\begin{array}{r l r} {u _ {u s e r}} & {= \frac {h (\eta_ {i n d} ^ {o p t}) ^ {2}}{1 + q _ {1} e ^ {- \eta_ {i n d} / \eta_ {0} ^ {+}}} - \frac {\phi h (\eta_ {i n d} ^ {o p t}) ^ {2}}{1 + q _ {2} e ^ {- (\eta_ {i n d} - \eta_ {i n d} ^ {o p t}) / \eta_ {0} ^ {-}}}} & {\eta_ {i n d} = \eta^ {1 / l} \qquad \mathrm{e.g.,transactions&connections}} \\ {u _ {i n v e s t o r}} & {= \sum_ {k = 1} ^ {t _ {p}} P _ {t - k} [ \left(\frac {\eta_ {t}}{\eta_ {t - k}}\right) ^ {\beta} - (1 + \varepsilon) ^ {k} ]} & {\mathrm{e.g.,tokeninvestment}} \\ {u _ {l a b o r e r}} & {= L _ {t} (w _ {m a x} \frac {\eta_ {m i n}}{\eta_ {t}} e ^ {- \frac {t}{t _ {0}}} - w _ {0})} & {\mathrm{e.g.,blockmining}} \end{array}
$$

Adoption

$$
\begin{array}{r l r l} \text {Non - adopters} & \xrightarrow {\gamma^ {+}} & \text {Adopters} \\ \zeta & \xleftarrow {\gamma^ {-}} & \eta \end{array} \quad \begin{array}{r l r l} \frac {d \zeta}{d t} & = - \gamma^ {+} \frac {\zeta \eta}{N} + \gamma^ {-} \eta & \gamma^ {+} & = [ \log (\frac {M A X (u _ {t} - u _ {t - 1} , 0)}{u _ {0}} + 1) ] ^ {K ^ {+}} \gamma_ {0} \\ \frac {d \eta}{d t} & = \gamma^ {+} \frac {\zeta \eta}{N} - \gamma^ {-} \eta & \gamma^ {-} & = [ \log (\frac {M A X (u _ {t - \tau} - u _ {t} , 0)}{u _ {0}} + 1) ] ^ {K ^ {-}} \gamma_ {0} \end{array}
$$

Table 1. Model Parameterization

<table><tr><td>Parameter</td><td>Unit</td><td>Type</td><td>Base value</td><td>Explanation</td></tr><tr><td colspan="5">Overall utility u</td></tr><tr><td> $\alpha_1$ </td><td>—</td><td>Network-specific</td><td>1/3</td><td>Coefficient of  $u_{user}$ </td></tr><tr><td> $\alpha_2$ </td><td>—</td><td>Network-specific</td><td>1/3</td><td>Coefficient of  $u_{investor}$ </td></tr><tr><td> $\alpha_3$ </td><td>—</td><td>Network-specific</td><td>1/3</td><td>Coefficient of  $u_{laborer}$ </td></tr><tr><td colspan="5">Utility  $u_{user}$ </td></tr><tr><td>h</td><td>\$/Participant $^{2}$ </td><td>Network-specific</td><td>0.1</td><td>Unit utility per interaction</td></tr><tr><td> $\phi$ </td><td>—</td><td>Constant</td><td>0.3</td><td>Maximum utility drop fraction</td></tr><tr><td> $q_1$ </td><td>—</td><td>Constant</td><td>1E3</td><td>Scaling constant in logistic function</td></tr><tr><td> $q_2$ </td><td>—</td><td>Constant</td><td>1E2</td><td>Scaling constant in logistic function</td></tr><tr><td> $\eta_{ind}^{opt}$ </td><td>Participants</td><td>Constant</td><td>500</td><td>Optimal connection number</td></tr><tr><td> $\eta_0^+$ </td><td>Participants</td><td>Constant</td><td>40</td><td>Scaling constant in logistic function</td></tr><tr><td> $\eta_0^-$ </td><td>Participants</td><td>Constant</td><td>300</td><td>Scaling constant in logistic function</td></tr><tr><td>l</td><td>—</td><td>Constant</td><td>3</td><td>Degree of separation on platform</td></tr><tr><td colspan="5">Utility  $u_{investor}$ </td></tr><tr><td> $t_p$ </td><td>Week</td><td>Network-specific</td><td>4</td><td>Average token-holding period</td></tr><tr><td> $P_{const}$ </td><td>$</td><td>Constant</td><td>1,000</td><td>Period investment amount</td></tr><tr><td> $\beta$ </td><td>—</td><td>Sensitivity</td><td>2</td><td>Sen. Of price to population</td></tr><tr><td> $\epsilon$ </td><td>—</td><td>Constant</td><td>2E-3</td><td>Background weekly interest rate</td></tr><tr><td colspan="5">Utility  $u_{laborer}$ </td></tr><tr><td> $L_{const}$ </td><td>Hour</td><td>Constant</td><td>168</td><td>Period laboring time</td></tr><tr><td> $w_m$ </td><td>\$/Hour</td><td>Network-specific</td><td>1e4</td><td>Undiluted hourly reward</td></tr><tr><td> $\eta_{min}$ </td><td>Participants</td><td>Constant</td><td>100</td><td>Minimum laborer population</td></tr><tr><td> $t_0$ </td><td>Week</td><td>Constant</td><td>300</td><td>Reward decaying time scale</td></tr><tr><td> $w_0$ </td><td>\$/Hour</td><td>Constant</td><td>0.5</td><td>Unit laboring cost</td></tr><tr><td colspan="5">Adoption</td></tr><tr><td>τ</td><td>Week</td><td>Network-specific</td><td>4</td><td>Time delay in quitting platform</td></tr><tr><td> $\gamma_0$ </td><td>1/week</td><td>Constant</td><td>0.1</td><td>Base adoption/abandonment rate</td></tr><tr><td> $K^+$ </td><td>—</td><td>Sensitivity</td><td>1</td><td>Sen. Of adoption to utility increase</td></tr><tr><td> $K^-$ </td><td>—</td><td>Sensitivity</td><td>0.3</td><td>Sen. Of abdmt. To utility decline</td></tr><tr><td> $\Delta u_0$ </td><td>$</td><td>Constant</td><td>10</td><td>Scaling constant for utility change</td></tr><tr><td>N</td><td>Participants</td><td>Constant</td><td>1e9</td><td>Overall population</td></tr></table>

Note. Sen, sensitivity; abdmt, abandonment.

of the blockchain. Its value depends on the particular service the blockchain is providing and on service quality. The base value is h � 0:1 dollar=participant<sup>2</sup>. The fraction $\phi$ of maximum use utility when the platform population approaches infinity is a global parameter applicable to different blockchains. Intrinsically, excessive online activities lead to a common utility decline on various platforms. We assume a 30% reduction of maximum use utility $( \phi = 0 . 3 ;$ Figure A1a in the online appendix). Finally, the degree of separation l on the platform is 3 (see Section 3.1.1). This corresponds to an optimal user population $\eta ^ { o p t } = ( \dot { \eta } _ { i n d } ^ { o p t } ) ^ { l } \sim$ 125 million, at which point the platform functions most efficiently (as of December 2021, there are \~100 million bitcoin owners; https://www.buybitcoinworldwide. com/how-many-bitcoin-users/).

• There are four parameters in investment utility $u _ { i n v e s t o r } . t _ { p }$ is an ordinary investor’s average tokenholding period, a network-specific parameter reflecting a token’s investment potential. Quality factors of the token-issuing blockchain affect participants’ decisions on token-holding time. However, a token’s investment potential deviates from the blockchain’s service potential and is in large part determined by the financial market. $t _ { p }$ and h thus characterize different network-specific features. We assume that an ordinary individual investor spends $P _ { c o n s t } = 1 , 0 0 0$ dollars every week. $\beta$ is the sensitivity of token price to platform population; its base value is two. ɛ is the background weekly interest rate, fixed at 0:2% (corresponding to a \~ 10% annual interest rate).

• There are five parameters in labor utility $u _ { l a b o r e r } .$ An ordinary individual laborer performs $L _ { c o n s t }$ hours of crypto labor every week. In the base case, the laborer uses one unit of hardware that runs at full power for a week, and $L _ { c o n s t } = 2 4 \times 7 = 1 6 8$ . The undiluted hourly reward $w _ { m }$ is specified by different blockchains (Figure A1c in the online appendix). This network-specific feature indicates the extent to which the platform encourages laboring activities. The base value of $w _ { m }$ is \$10,000/hour for each of $\eta _ { m i n } = 1 0 0$ core laborers, total ing \$1M/hour for the entire pool. For bitcoin, approximately 37.5 bitcoins are mined every hour (https:// www.quora.com/Is-there-any-limit-for-how-manybitcoins-can-be-mined-per-day). Multiply by approximately \$25,000 per coin (e.g., the price level in December 2020 and June 2022) and arrive at approximately \$1M/hour. There were around 1.5 million bitcoin miners (https://www.buybitcoinworldwide.com/how-manybitcoins-are-there/) in December 2021. The weekly mining reward of a unit of hardware is \$100–\$200, consistent with the result at $\begin{array} { r } { w _ { m } = \mathbb { \ S } 1 0 , 0 0 0 / \mathrm { h o u r } . } \end{array}$ . The decaying constant $t _ { 0 } = 3 0 0$ weeks (the block supply of bitcoin halves every four years or 208 weeks: $2 ^ { 1 / 2 0 8 } \sim e ^ { 1 / 3 0 0 } )$ . Hourly laboring cost $w _ { 0 }$ is \$0.5/hour (electricity price \~\$0.15/kwh, and a typical bitcoin mining hardware unit has 3 kwh power; https://cointelegraph.com/bitcoin-for-beginners/ how-to-mine-bitcoin-a-beginners-guide-to-mine-btc).

• There are six parameters in the adoption/ abandonment process. τ is network-specific, characterizing participants’ inertia on the particular platform. A large τ indicates that participants are willing to stay in the blockchain for a relatively long time in face of adversarial events. $\gamma _ { 0 }$ is the base adoption/abandonment rate, fixed at 0.1/week. $K ^ { + }$ and K<sup>�</sup> are the (asymmetric) sensitivities of platform adoption/abandonment to utility increase/decline. We consider the $K ^ { + } > K ^ { - }$ region, that is, the adoption of the platform due to utility inflation is more sensitive than abandonment due to utility deflation because abandoning online social interactions is often associated with external reasons (e.g., physical or mental health (Tromholt 2016)), aside from platformrelated reasons $( \mathrm { e . g . , a }$ decline in platform’s utility). The base values are $K ^ { + } = 1 , K ^ { - } = 0 . 3 . \mathrm { \bar { \ } } \Delta u _ { 0 }$ is the scaling constant for utility change across one period, fixed at \$10. N is overall population, fixed at ${ \boldsymbol { 1 0 } } ^ { 9 } { \boldsymbol { = } } 1$ billion participants.

Altogether, the model has seven network-specific parameters. Three coefficients $\alpha _ { 1 / 2 / 3 }$ characterize the relative strength of different roles of an average participant on a specific blockchain platform; base values are onethird for each. There is one network-specific parameter in each utility term. At use utility $u _ { u s e r } ,$ h characterizes platforms’ service function and service quality. At investment utility $u _ { i n v e s t o r } , t _ { p }$ characterizes the investment potential of platforms’ tokens. At labor utility $u _ { l a b o r e r } , w _ { m }$ characterizes platforms’ willingness to reward participants’ contributions. Each parameterizes one utility component of the blockchain. The final network-specific parameter τ in platform adoption characterizes participants’ inertia, indicating participants’ general attitudes toward the platform. Base values for these networkspecific parameters are determined (1) through appropriate simulation (e.g., for $\tau , t _ { p } )$ or (2) using bitcoin as the reference (e.g., for $w _ { m } )$

Sixteen global parameters are set at realistic values. These values ensure that three individual utility terms (each representing a dollar value generated per time step (week)) maintain a similar order of magnitude within the appropriate range, that is, $u _ { u s e r } \sim u _ { i n v e s t o r } \sim u _ { l a b o r e r }$ (Figure A1 in the online appendix, y axis; no utility term is entirely dominated by others, ensuring all three roles are effective). In our model, the dollar unit is a natural choice for investment and labor utility. Use utility is also converted into dollar values under the assumption that each interaction within the user’s community carries a uniform monetary value h. This uniform monetary value could be linked $^ { \mathrm { t o , } }$ for instance, a transaction fee, the exchange of goods and information, or profit generated from user interactions. In reality, model constants may vary across platforms and change over time; however, tests indicate that model remains robust in relation to these constants, and variations within the appropriate range are unlikely to significantly alter the system’s dynamics (refer to Section 8 for discussion).

Three sensitivity parameters are used to characterize the sensitivity of the token price to the platform population $( \beta ) ,$ , as well as the sensitivities of blockchain adoption/abandonment to changes in the platform’s utility $( K ^ { + } , K ^ { - } )$ . These parameters are dimensionless and do not correspond to empirical values. We adjust their values in the subsequent analyses.

## 5. Development Trajectory of Blockchain Platforms

Dynamics of individual model components demonstrate excellent model behavior (see Online Appendix C for details). We aggregate individual mechanisms and investigate the complete development trajectory of blockchain platforms. During the expansion or shrinkage of blockchain networks, platforms gain or lose population η in response to the change in platforms’ utility $u = \alpha _ { 1 } u _ { u s e r } +$ $\alpha _ { 2 } u _ { i n v e s t o r } + \alpha _ { 3 } u _ { l a b o r e r }$ . Then, u changes to the next level as population η grows or diminishes. This feedback between η and u drives systems’ dynamics.

## 5.1. Three-Phase Development

We first demonstrate the base-case development trajectory with parameter values in Table 1 (Figures 2 and 3). A platform’s complete development trajectory is divided into three phases. The two-phase transitions can be identified from the utility curve (Figure 2(a)–(c)) and the population curve (Figure 2(d)–(f)) and from the dynamics of adoption and abandonment rates $\gamma ^ { + } , \gamma ^ { - } \operatorname { ( F i g u r e } 3 )$ 1

5.1.1. Phase 1. In the first phase (Figure 2(a) and (d)), the platform has a small population η and grows slowly. Both $u _ { u s e r }$ and $u _ { i n v e s t o r }$ are trivial. Platform adoption is growing thanks to the high labor reward. Although $u _ { l a - }$ $b o r e r$ has been rapidly decreasing ever since the launch of the platform, due to time decay and dilution of laboring rewards, the declining adoption rate $\gamma ^ { + }$ is sufficient for keeping the growth momentum $( \mathrm { i . e . , }$ during Weeks 1–100) before leading to a slow decrease in population (i.e., after Week 100). The stable period 2 oscillation on the curve derives from the feedback between η and u: When η goes up, rewards are diluted, causing $u _ { l a b o r e r }$ to decline, and η goes down in response, which drives u up

Figure 2. (Color online) Base-Case Development Trajectory  
![](/api/attachments/UR5TSQG9/fulltext/images/de96716806bf932dd6a963f313649155a178d4e3bfee1e7c199f316913e0eefe.jpg)

(d)  
![](/api/attachments/UR5TSQG9/fulltext/images/19dfe9102ee9207f9853c20c7280bfc5b8d70d7e3c38935a864287bd4783dcbb.jpg)

(b)  
![](/api/attachments/UR5TSQG9/fulltext/images/635493a897355c0f2d3304ac17a8c7655d255db7276728d00edd6147dd9098be.jpg)

(e)  
![](/api/attachments/UR5TSQG9/fulltext/images/3ecd52dd52f5bcbf48bcddcf4149241798dee22a64f1c31f199794c6a1b15411.jpg)

(c)  
![](/api/attachments/UR5TSQG9/fulltext/images/b6ac6a7c478b28cb749ec33536df9d5ce20bf746322781fa7ea7ae4d84cefd38.jpg)

(f)  
![](/api/attachments/UR5TSQG9/fulltext/images/bf0007af192fe8dc966dd04114932c1da079b5ee1a2f25ad21890b3f6ff6a368.jpg)  
Notes. The complete trajectory is divided into three phases. Parts of utility curves (a–c) and population curves (d–f) overlap on the x axis, shown in different scales at different plots.

again; the envelope of the serrated curve indicates the development trajectory. This phase corresponds to the initial stage of a blockchain, where the newly launched platform is primarily maintained by a small circle of technology enthusiasts, each of whom contributes a great deal of labor.

Figure 3. (Color online) Adoption/Abandonment Rate $\gamma ^ { + / - }$ <sup>�</sup> of Base-Case Trajectory  
![](/api/attachments/UR5TSQG9/fulltext/images/2e891536335dabdd71211a0cdf629bca42c01ccdc6bf172a7cf2ae234c4e300b.jpg)  
Note. The three-phase development is driven by dynamics of $\gamma ^ { + / - }$

5.1.2. Phase 2. After a continued period of slow but stable development, the platform enters the second development stage (Figure 2(b) and (e)). Phase transition is triggered by the disruption of the period 2 cycle. Specifically, because of the $\stackrel { \cdot } { e } ^ { - t / t _ { 0 } }$ decay in $u _ { l a b o r e r } ,$ the system reaches a point where laboring is not sufficiently profitable, in which case abandonment is enlarged. This amplifies the scale of both adoption $\gamma ^ { + }$ and abandonment $\gamma ^ { - }$ (Figure 3) and thus the scale of the oscillation at η. Critically, the amplified oscillation of the adopter population brings $u _ { i n v e s t o r }$ into the discussion, as now there are greater opportunities for arbitrage. Once u<sub>investor</sub> becomes substantial, platform development is fasttracked, and population η grows across orders of magnitude in a short period of time. The growth is sustained by a few intermediate-range (e.g., around 15weeks) oscillations, modulated by investment period $t _ { p } ,$ and the platform population reaches higher and higher peaks by the end of each cycle. Such an accumulation of adopter base is explained by increased platform exposure, which attracts more and more participants to join the cycle between adopters and nonadopters. This phase corresponds to the fast-growing stage of a blockchain where the enabling of financial functions such as token investment greatly enhances the platform’s popularity and participants are attracted to it on a large scale.

5.1.3. Phase 3. During the development of Phase 2, as the adopter base $\eta$ continues to accumulate, use utility $u _ { u s e r }$ gradually becomes salient. A larger population leads to a higher usage utility and thus a higher overall utility $u ,$ which contributes to the adoption cycle and pushes it to higher amplitudes. As the peak u of each cycle becomes larger, peak $\eta$ ascends accordingly. This coordinated increase of peak u and peak η eventually stops when $\eta _ { i n d }$ (i.e., equal to $\eta ^ { 1 / l } )$ passes the optimal value for $u _ { u s e r } .$ The growth of u stops and $\eta$ does not reach an even higher peak. The system enters the third phase, where η and u oscillate in stable cycles (Figure $2 ( \mathrm { c } )$ and (f)), driven by cycled adoption-abandonment (Figure 3). At this stage, labor utility $u _ { l a b o r e r }$ is changing very slowly and has become trivial compared with $u _ { u s e r }$ and $u _ { i n v e s t o r } .$ Changes in $u _ { u s e r }$ and $u _ { i n v e s t o r }$ primarily determine the development cycle. Platform oscillates between having a peak investment utility and a peak usage utility, and between having a high and a low adoption level. The complete cycle has two distinct peaks, one higher and one lower (Figure 2(f)), corresponding to $\eta _ { i n d }$ lying on the two sides of the optimal value of $u _ { u s e r } .$ . This phase corresponds to a long-term market cycle after the platform becomes mature. Currently, few blockchain projects have entered this conceptual stage, and it is certainly the case that in the real world, this conceptual cycle will only continue within a limited time frame.

Overall, this three-phase trajectory illustrates the representative dynamics of a blockchain platform’s network development. It is in many ways consistent with realworld situations (see later). Across the three phases, the complete development curve closely resembles Gartner’s hype cycle (Linden and Fenn 2003), which qualitatively describes the life trajectory of emerging technologies/ industries. In this sense, the current study provides a quantitative system for reproducing Gartner’s cycle for a specific emerging industry: blockchains.

## 5.2. Modes of Development

By varying model parameters, we can investigate differ ent scenarios of platform development (Table 2). In all situations, role composition is fixed $( \alpha _ { 1 / 2 / 3 } = 1 / 3 ) ;$ ; we show the first 300weeks of each development trajectory, as in Figure 2(d).

Four combinations of $K ^ { + / - }$ are investigated (Figure 4) and compared with the base case. When $K ^ { + }$ is large, adoption rate $\gamma ^ { + }$ increases, and the adoption of the plat form gets faster, and vice versa. When $\bar { K } ^ { - }$ <sup>�</sup> is large, abandonment rate $\gamma ^ { - }$ increases and the platform loses more participants at each time step; the inverse is also true (see Online Appendix C for the dynamics of $\gamma ^ { + }$ and $\gamma ^ { - }$ in each scenario). Overall, the coeffect of $K ^ { + }$ and K<sup>�</sup> deter mines four typical modes of development.

• Mode I: When adoption and abandonment are both on a small scale $( \mathrm { i . e . , } K ^ { + } , K ^ { - }$ are both small), the network fails to trigger a proper growth pattern. The platform is not successfully launched and stays within the small initial community, whose size is in gradual decline.

• Mode II: When adoption and abandonment are in the appropriate range, platform undergoes the threephase development as in the base case. Initial network growth is sustained by the contribution of core participants, who conduct substantial labor. Entering the second stage, investment opportunities trigger rapid network growth, and platform sees a series of expanding adoption cycles, analogous to typical financial cycles (Lux 1998). When market cycles cease to expand, platform development reaches a (conceptual) stable state, iterating between the adoption by a small and a large fraction of the overall population.

Table 2. Investigated Scenarios of Platform Development

<table><tr><td>Parameter</td><td>Type</td><td>Base value</td><td>Scenario</td><td>Reference</td></tr><tr><td> $K^{+},K^{-}$ </td><td>Sensitivity</td><td>(1, 0.3)</td><td>(0.5, 0.3) (1.3, 0.6) (1.4, 0.2) (1.5, 0.9)</td><td>6.2.1, Figure 4</td></tr><tr><td> $\beta$ </td><td>Sensitivity</td><td>2</td><td>1, 3, 5, 7</td><td>6.2.2, Figure A5</td></tr><tr><td> $h,w_{m}$ </td><td>Network-specific</td><td>(0.1, 1e4)</td><td>(1, 1e4) (0.01, 1e4) (0.1, 1e3) (0.01, 1e5)</td><td>6.2.3, Figure A7</td></tr><tr><td> $t_{p}$ </td><td>Network-specific</td><td>4</td><td>2 to 11</td><td>6.2.4, Figure A9</td></tr><tr><td> $\tau$ </td><td>Network-specific</td><td>4</td><td>2 to 11</td><td>6.2.4, Figure A12</td></tr></table>

Figure 4. (Color online) Platform Development Scenarios Under Different $K ^ { + }$ and $K ^ { - }$  
![](/api/attachments/UR5TSQG9/fulltext/images/68cfaa22b47dbb9d25169a4ecca2691e915df7d2f95e1643f5218cadd0336627.jpg)

![](/api/attachments/UR5TSQG9/fulltext/images/5f0e77fbd9f16dfae7a43876adc136d7dc4bb0d9490a63d5eb222def95aead5d.jpg)

![](/api/attachments/UR5TSQG9/fulltext/images/c06bf9d6ea5f695e7a9e08aeeb1a8fd8aaa0740d9f41a8b2053772eed6782468.jpg)

(d)  
![](/api/attachments/UR5TSQG9/fulltext/images/db81f8fa6fd9e911d2914ac34fe770ae15dde54b5abae8e33e54c306488c7974.jpg)

(e)  
![](/api/attachments/UR5TSQG9/fulltext/images/85733da1fe84f583a6da35f5768281830fd7d2ed665491c560063331de2e9abf.jpg)

![](/api/attachments/UR5TSQG9/fulltext/images/4a02e54125e653d8a6e219ae6468cc86270899e2322c93a87759648afa93c7dc.jpg)  
(f)

(g)  
![](/api/attachments/UR5TSQG9/fulltext/images/b519d7dbba4350fbceb98eadc5816029752bdbb6c9196e964c5915de918263c8.jpg)

(h)  
![](/api/attachments/UR5TSQG9/fulltext/images/b5b538ae4e10021aded768c5deb98f3b9550a63426ef87cf739c40fa5b97af2c.jpg)  
Notes. (a)–(d) (K<sup>+</sup>, K<sup>�</sup>) � (0.5, 0.3), (1.3, 0.6), (1.4, 0.2), (1.5, 0.9). Other parameters take base values in Table 1. Four modes of development are exemplified (Modes I–IV).

• Mode III: When adoption is faster while abandonment is reduced $( \mathrm { i . e . , } ~ K ^ { + }$ is large and K<sup>�</sup> is small), the platform achieves full-scale adoption where the adopter pool is almost depleted. Unlike in Mode II, the stablestate adoption cycle now iterates between maintaining a large and a small number of adopters that are of the same order of magnitude. Along the envelope of cycles, the S-shape of the underlying SIS dynamics is recovered.

• Mode IV: When adoption and abandonment are both very fast $( \mathrm { i . e . , } K ^ { + }$ and K<sup>�</sup> are both large), the platform sees rapid growth and then a rapid and irreversible decline. The network fails in a short amount of time. This growth mode may correspond to the situation of scam blockchain projects, where the funds for tokens are cashed out quickly after the ICO event, a situation analogous to a failed IPO in traditional venture capital (Saboo et al. 2016).

These four modes of development generalize various platform development scenarios. The specific shape of a development trajectory, for example, in terms of the speed and timing of phase transitions, amplitude, duration of adoption cycles, and so on, is modulated by model parameters. Besides $K ^ { + / - }$ , network-specific parameters $h ,$ $w _ { m } , ~ t _ { p } ,$ and τ and sensitivity parameters $\beta$ are varied, whose effects on system dynamics are studied (Online Appendix C). All model parameters behave reasonably in simulations.

## 6. Empirical Study 6.1. Data

We use the model to match data series of real blockchains. The data set is the historical daily token price series of \~150 blockchain projects (source: https:// coinmarketcap.com; https://www.kraken.com/en-us/). The longest series dates back to 2013 and ends in 2019; most series are between 2016 and 2018. As a result, this data set is not influenced by COVID-19, which may introduce additional dynamics to the development of blockchains (Goodell and Goutte 2021). Because COVID 19 is a exogenous shock to the blockchain ecosystem, leaving its effect out allows us to examine a relatively $\prime \prime \mathrm { c l e a n ^ { \prime \prime } }$ system without getting the parameterization influenced by noises. After the COVID-19 pandemic, the Ukraine war and the Federal Reserve interest rate adjustments are also external forces that may contaminate the data parameterization process. We choose to examine the pre-COVID period to focus on our methodological contribution of considering participants’ multiple roles. From the data set, we select series longer than 20 weeks and having variance greater than 1 e-3. The cleaned data set consists of 112 tokens, issued by blockchains applied to various sectors (see data description in Online Appendix B).

Basic statistics of the data series are summarized in Table 3. The average start date and end date are November 2016 and October 2018, and the average series length is 706 days (\~ 100 weeks). Maximum and minimum prices range across several orders of magnitude, averaging at \$357.2 and \$3.25, respectively. Price variance ranges across 10 orders of magnitude, averaging at 1.1E+5. Within the series range, the maximum daily return is at least 20% and can go beyond 1,000% for some tokens and the minimum daily return ranges from �16% to �98%. The overall return of individual price series can be as large as $1 . 5 2 \times 1 0 ^ { 5 }$ times the value on the start date, and it is also likely that the price will lose 99% of its value by the end date. Maximum and minimum possible returns over the course are more exaggerated.

## 6.2. Fitting Setup

Price series are normalized to the [0, 1] interval. The time step is a week, and we use the weekly average of the daily series for fitting. Because the data do not include the complete token price history starting from the blockchains’ launch dates, we issue a long series in each forward run and calculate the smallest point-average misfit $\Delta _ { m i n }$ from comparing the data series with the portion of the model series that best matches the data. $\Delta _ { m i n }$ is the average point-wise square distance between the data series and the model series. We run a sufficiently long model series, using data series as the window to identify the portion of the model series that is the most similar to it. The same method is used in reference models and in our model. When matching model to data, the model series are also normalized into [0, 1], that is, the largest instance on the series is one. Normalization is conducted on the entire series; when a window of the model series is cut out, that partial series are not normalized into [0, 1] again. Renormalization on the partial series may enhance the fit to data, which lie in the [0, 1] interval; however, such a treatment may incur overfitting, while sacrificing the model’s explanatory power. We abandon this tailored normalization and keep a conservative fitting setup (see Figures A15–A21 in Online Appendix E). Consistent with the price’s power-law dependence on platform size (Equation 3), we obtain η(t) from the model and match price data with η<sup>β</sup> using the best-fit β.

For each data series, we fit (a subset of) networkspecific parameters $\alpha _ { 1 / 2 / 3 } , t _ { p } , \tau , h ,$ and $w _ { m }$ and sensitivities $\hat { \beta , } { K } ^ { + }$ , and K to find their best-fit values for the specific series. Unvaried parameters and varied parameters’ initial points use the base values in Table 1. Different initial points are tested, and fitting results remain largely consistent. Noninteger parameters are fitted together in the inner loop; we use the downhill simplex method (Press 1992) to conduct efficient fitting. Integer parameters τ and $t _ { p }$ are pulled out and fitted in the outer loop. Integer values are specified within a search range (e.g., τ and $t _ { p }$ both range from 1 to 12).

To anchor model performance, we use a panel of reference scaling to match the data: exponential $m _ { 1 } e ^ { m _ { 2 } t } .$ power-law ${ m } _ { 1 } t ^ { m _ { 2 } }$ , polynomial $\Sigma _ { l } m _ { l } t ^ { l }$ with order l, the netoid function for network growth $m _ { 1 } / ( 1 + e ^ { - m _ { 2 } ( t - m _ { 3 } ) } )$ (Zhang et al. 2015), which is related to Metcalfe’s law, as well as an exponential power-law function $m _ { 1 } e ^ { m _ { 2 } t ^ { m _ { 3 } } }$ adapted from the Alabi (2017) model for explaining blockchain network growth. For each reference model, scaling parameters m are fitted. The fitting setup is the same as for our model. Here, the exponential and power-law curves are used because they can indicate first-order growth patterns; polynomial curves are used because they are flexible in indicating oscillatory shapes when we continue increasing the polynomial order; the netoid function and exponential power-law curves are used as their descriptive capability is considered by existing studies. These references are fully explainable. Moreover, the S-shape, as can be supported by contagion models (e.g., SIS), is an apparent alternative that can be outperformed by our model trajectories.

Table 3. Statistics of Data Series

<table><tr><td></td><td>MAX</td><td>MIN</td><td>AVE(STD)</td></tr><tr><td>Start date</td><td>Oct 12, 2018</td><td>Apr 28, 2013</td><td>Nov 17, 2016</td></tr><tr><td>End date</td><td>Mar 11, 2019</td><td>Dec 12, 2017</td><td>Oct 28, 2018</td></tr><tr><td>Series length (day)</td><td>2144</td><td>149</td><td>706 (488.9)</td></tr><tr><td>Maximum price</td><td>$19,475.8</td><td>$0.145</td><td>$357.2 (1,929.8)</td></tr><tr><td>Minimum price</td><td>$77.4</td><td>$3E-6</td><td>$3.25 (12.4)</td></tr><tr><td>Price variance</td><td>1.1E+7</td><td>1.1E-3</td><td>1.1E+5 (1.07E+6)</td></tr><tr><td>Maximum daily return</td><td>1147%</td><td>20%</td><td>151% (1.92)</td></tr><tr><td>Minimum daily return</td><td>-16%</td><td>-98%</td><td>-43% (0.19)</td></tr><tr><td>Overall return (since start date)</td><td>1.52E+5</td><td>-0.99</td><td>1,431 (1.44E+4)</td></tr><tr><td>Maximum return (since start date)</td><td>3.42E+5</td><td>0</td><td>3.43E+3 (3.23E+4)</td></tr><tr><td>Minimum return (since start date)</td><td>0</td><td>-0.99</td><td>-0.60 (0.312)</td></tr></table>

Notes. Number of data series, 112. MAX, maximum; MIN, minimum; AVE, average; STD, standard deviation.

## 6.3. Results

We first consider an economical fitting setup where only τ and $t _ { p }$ are varied and the other parameters are fixed at base values. By only varying τ and $t _ { p } ,$ the model can already incorporate various development trajectories (Figures A9 and A12). This is also a fair comparison with exponential and power-law models, as only two parameters are fitted in both cases. We consider two setups with τ and $t _ { p }$ both in the range of 1–8 and 1–12, respectively (all data series are longer than 20 weeks, exceeding the upper search bound for $t _ { p }$ and τ).

Results favor our model (Figure 5; Table 4). The exponential, power-law, netoid function, and exponential power-law are not accurate enough for describing the data series. The order 4 polynomial model yields the best fitting performance among reference models, with five parameters being fitted. Further increasing the polynomial order does not improve the misfit. With only two temporal parameters τ and $t _ { p }$ fitted, our model outperforms all reference models. Average $\Delta _ { m i n } = 0 . 2 8 6$ when τ and $t _ { p }$ range from 1 to $^ { 8 , }$ and average $\Delta _ { m i n } = 0 . 2 5 6$ when τ and $t _ { p }$ range from 1 to $1 2 , \mathsf { a }$ 12% reduction compared with the best polynomial scaling. Besides having better fitting performance with a smaller parameter set, our model is explainable compared with descriptive scalings.

We then conduct a full-parameter fit where all seven network-specific parameters $\alpha _ { 1 / 2 / 3 } , t _ { p } , \tau , h ,$ and $w _ { m }$ and three sensitivities $\beta , \ K ^ { + } .$ , and $\dot { K } ^ { - }$ are fitted (as timeinvariants, considering that these parameters change little over time; see Section 8 for discussion). It is rather ambitious to use the root model to match the develop ment of more than 100 different blockchain projects, yet the results are encouraging. The average misfit is 0.0144, a 51% reduction from 0.0286 (see Online Appendix D for $\Delta _ { m i n }$ of each data series). For 112/112 series, the pointaverage misfit $\Delta _ { m i n }$ is less than 0.04, indicating that at each time step, model series and data series on average differ less than 0.2 within the [0, 1] interval, that is, < 20% difference across the entire series. For 90/112 series, $\Delta _ { m i n }$ is less than 0.0225, that $\mathrm { i s } , < 1 5 \%$ difference between model and data. For 45/112 series, $\Delta _ { m i n }$ is less than 0.01, that $\mathrm { i s } , < 1 0 \%$ difference between model and data. $\operatorname { A c - }$ ross the 112 blockchain platforms, the user’s role and the investor’s role are generally available to participants, as each platform maintains a specific use utility, and the existence of price series implies public token investment in the first place.<sup>5</sup> The laborer’s role, on the other hand, is not always possible, whose availability depends on blockchain’s design (e.g., the consensus mechanism). We separate those platforms providing clear access to crypto labor from those not (Online Appendix B) and see that, consistently, our model fits better to these laborer-role well-defined platforms (Figure 5, inset; full-parameter fit). Two groups of $\Delta _ { m i n }$ (red, black) have a p value of 2.22e-4 at the two-sample t test (Online Appendix G), suggesting strong difference.

Figure 5. (Color online) Model Fitting Performance  
![](/api/attachments/UR5TSQG9/fulltext/images/994dfd5358f510a923001e1ff594e2f0d3d70c2d137fab2ccf768ce9891c6f4d.jpg)  
Notes. With two temporal parameters τ and $t _ { p }$ fitted (search range, 1–12), our model outperforms exponential, power-law, polynomial (order l with l + 1 parameters fitted), the netoid function, and exponential power-law. Dashed lines show the average $\Delta _ { m i n }$ across all data series. Inset: model fits better to platforms with clear labor access (left half) where the laborer’s role is well defined; solid/dashed lines show the average/standard deviation of $\Delta _ { m i n } .$

Table 4. Fitting Performance of Reference Models and Our Model (Three Fitting Setups)

<table><tr><td>Model</td><td>Fitted parameter</td><td>Average  $\Delta_{min}$ </td></tr><tr><td>Exponential</td><td> $m_1, m_2$ </td><td>0.0545</td></tr><tr><td>Power law</td><td> $m_1, m_2$ </td><td>0.0432</td></tr><tr><td>Polynomial  $l = 2$ </td><td> $m_0$  to  $m_2$ </td><td>0.0306</td></tr><tr><td>Polynomial  $l = 3$ </td><td> $m_0$  to  $m_3$ </td><td>0.0295</td></tr><tr><td>Polynomial  $l = 4$ </td><td> $m_0$  to  $m_4$ </td><td>0.0292</td></tr><tr><td>Polynomial  $l = 5$ </td><td> $m_0$  to  $m_5$ </td><td>0.0328</td></tr><tr><td>Polynomial  $l = 6$ </td><td> $m_0$  to  $m_6$ </td><td>0.0351</td></tr><tr><td>Netoid</td><td> $m_1, m_2, m_3$ </td><td>0.0386</td></tr><tr><td>Expo-power law</td><td> $m_1, m_2, m_3$ </td><td>0.0380</td></tr><tr><td>Our model</td><td> $\tau, t_p$  [1,8]</td><td>0.0286</td></tr><tr><td>Our model</td><td> $\tau, t_p$  [1,12]</td><td>0.0256</td></tr><tr><td>Our model</td><td> $\tau, t_p$  [1,12],  $\alpha_1, \alpha_2, \alpha_3, \beta, K^+, K^-, h, w_m$ </td><td>0.0144</td></tr></table>

Best-fit parameter values for each series are plotted in Figure 6 (a small number of outliers are excluded from the plots; see Online Appendix D for detailed values). Average value across series (solid bar) and the standard deviation (dotted bar) are shown, against the base value (dash bar). Average compositions of the user’s role and the laborer’s role across platforms are slightly above onethird (Figure 6), and average composition of the investor’s role is close to one-third. The three coefficients $\alpha _ { 1 / 2 / 3 }$ fall within [0, 1] in most cases, and there is no instance where a role composition is one order of magnitude larger or smaller than the other two roles (Online Appendix D). This suggests that the three roles take effect simultaneously on most platforms.

β demonstrates large variance across different series, suggesting that different blockchains have different token price sensitivity to platform population. Adoption sensitivity $K ^ { + }$ also varies substantially compared with the relatively clustered abandonment sensitivity $K ^ { - }$ <sup>�</sup>. This suggests that participants are attracted to different block chains under varied considerations of platform utility but leave platforms for similar reasons. The result is consistent with our previous comment that we consider $K ^ { - }$ smaller than $K ^ { + }$ because quitting platforms is more often associated with external reasons (as many external reasons such as health concerns are universal for various platforms). As we match normalized series, h and $w _ { m }$ have small variances across different series, consistent with simulation results, because they both have little influence on the gen eral shape of the trajectory (Figure A7).

Figure 6. (Color online) Best-Fit Parameter Values for Each Data Series Under Full-Parameter Fit  
![](/api/attachments/UR5TSQG9/fulltext/images/dcf5ee3ecb820f67ca7d0468db2c7c62a7a2ce19e25f42ffd3337f7a13525082.jpg)  
Notes. The average value across all series (solid bar) and the standard deviation (dotted bar) are shown against the base value (dash bar). For each fitted parameter, a small number of outliers are excluded from the plot.

Best-fit values of τ and $t _ { p }$ (the last two columns in Figure 6) span the search range. τ and $t _ { p }$ suggest two dimensions to characterize blockchains (Figure 7). For example, participants may demonstrate large abandonment inertia τ on trusted platforms but have a short holding time $t _ { p }$ on tokens with high price volatility. Across 112 blockchains, participants demonstrate on average 5.7 weeks of delay when quitting the platform while holding a token on average 3.3 weeks before selling it off. These values do not deviate from empirical observations. For 83 of 112 instances, $t _ { p }$ is no more than $\tau ,$ that is, participants do not hold a token for a time longer than their stay on the platform. The rest $( t _ { p } > \tau )$ corresponds to the situation where participants are willing to hold the token as an investment even when they have already left the platform, which is likely to happen when the token is being heavily transacted in the market. From Figure 7, this list includes ripple, bitcoin-cash, binancecoin, and monaco, which arguably did have high transaction volume during the period 2015–2019. For only 11 of 112 instances, $t _ { p }$ is greater than τ + 2, suggesting that it is rare that participants become exceedingly speculative in token investment. Both bitcoin and Ethereum have a small $t _ { p } ,$ as many other well-known tokens do (especially during 2015–2019), including litecoin, eth-classic, stellar, and monero. A small $t _ { p }$ is consistent with the high transaction activities around these tokens. In general, most tokens are held for one to four weeks during one investment operation, indicating conformity at digital token investment. Participants’ inertia τ on different blockchains nevertheless demonstrates a large spread, reflecting varied attitudes toward different platforms. A wide distribution of τ reveals the diverse landscape of this new sector, in which an established characterization of successful platforms is yet to emerge. Nonetheless, it suggests that many well-known blockchains have τ at six or seven weeks, that is, participants will stay on the platform for around two months before making the decision to quit.

As examples, we show the fits to four series (bitcoin, eos, ardor, cryptonex) (Figure 8) that have different development trajectories and are fitted to different extents (see the complete list of fits in Online Appendix E). Estimation on these four platforms (lines 7, 16, 27, and 37 in Online Appendix D) agrees with simulation analysis (Section 5 and Online Appendix C) and with empirical evidence. Ardor, bitcoin, and eos reside in roughly the same parameter space except for τ and $t _ { p } .$ For bitcoin and ardor, model misfit $\Delta _ { m i n }$ is also similar. This agrees with these two tokens’ similar development histories (Online Appendix K), which demonstrate extraordinary similarity with the three-stage development established in this study (Section 5.1). During the observational period, ardor has descended from the initial peak, while bitcoin is on the way to descending from the peak; both experience subsequent after initial-peak growth (Online

Figure 7. (Color online) Best-Fit τ and $t _ { p }$ for Each Data Series Under Full-Parameter Fit  
![](/api/attachments/UR5TSQG9/fulltext/images/9c73d785316f3fb1229269fdd1aa5968d59eb8c753c3d1e81b9588b81450dd15.jpg)  
Notes. Dotted lines indicate $t _ { p } = \tau$ and $t _ { p } = \tau + 2 .$ For 83 of 112 instances, $t _ { p } \leq \tau ;$ 18 of 112 instances, $\tau < t _ { p } \leq \tau + 2 ; 1 1$ of 112 instances $t _ { p } > \tau + 2 .$

Figure 8. (Color online) Sample Fits to Token Price Series  
(a)  
![](/api/attachments/UR5TSQG9/fulltext/images/18b62695c0aef8c7d1cc1191569df5d7bb83fc964d2c0f52f23203b5233bc5e3.jpg)  
(c)

(b)  
![](/api/attachments/UR5TSQG9/fulltext/images/9eceb4fa5b3c184d62551f1d7681aa850d8018ee2587e78ccbc9050cdf07d249.jpg)

![](/api/attachments/UR5TSQG9/fulltext/images/1a9ae2240f11ca51bdb9eb3db585973b09c71ce41dc669b58fbe0fa19e79fa90.jpg)

(d)  
![](/api/attachments/UR5TSQG9/fulltext/images/da7a98cb573cf32d9836af06337c47f962361b60bc46e759c2e505d2e7bed0da.jpg)  
Notes. (a) Bitcoin. (b) Eos. (c) Ardor. (d) Cryptonex. Model series match data series to different extents (indicated by $\Delta _ { m i n } )$ . Dashed lines ar smoothed model series (smoothing window length s � 13).

Appendix K), consistent with model projection. For eos, longer τ and $t _ { p }$ are derived, compared with bitcoin and ardor. This suggests that participants have good faith in this platform and are willing to stay. Indeed, eos is deemed by many as a promising new-generation blockchain and enjoys significant market expectations. Finally, cryptonex maintains a different set of platform parameters; compared with ardor, bitcoin, and eos, it has smaller τ and $t _ { p }$ (indicating high turnover rate), smaller h and $w _ { m }$ (indicating reduced usage utility and laboring utility), larger $K ^ { + / - }$ (indicating high turnover rate), larger price sensitivity $\beta ,$ , and elevated investor composition $\alpha _ { 2 } .$ All these features agree with the nature of this platform: cryptonex itself is a p2p cryptocurrency exchange platform, and participants on it are engaged solely in high-volatility transactions. This distinction is correctly revealed at model estimation.

To account for the variation in fitting performance across platforms, we collected a panel of features of investigated tokens (83 of 112), including consensus mechanisms (PoW/PoS, or both), total token supply, ICO token supply, post ICO token supply conditions (remain/ increase/decrease), token percentage reserved for investors, initial token price, net hash per second, and fundraised (USD). We plot misfits of different tokens against these qualitative variables and look for patterns suggesting token features’ correlation with model fits (Online Appendix F). Results suggest that our model can produce better fits for blockchain platforms having a more diffusive nature; the correlation is nevertheless weak, and it is indiscreet to generalize without additional empirical evidence.

## 6.4. Robustness Checks

We conduct the following analysis to validate the robustness of the results (Table 5 and Online Appendix H).

6.4.1. Partial Fits. Three sensitivity parameters, $\beta , K ^ { + } .$ and $K ^ { - } ,$ , demonstrate large variance across data series compared with the other noninteger parameters $h , w _ { m } ,$ and $\alpha _ { 1 / 2 / 3 }$ (Figure 6). We test alternative fitting setups, varying these three parameters: (1) fit $\tau , t _ { p } ,$ and $\beta ; ( 2 )$ fit $\tau , \dot { t _ { p } } , \check { K ^ { + } }$ , and $K ^ { - } ; ( 3 )$ fit $\tau , t _ { p } ,$ and all three sensitivities $\beta , \dot { K } ^ { + }$ , and $K ^ { - }$ . Results (Table 5) suggest that the misfit is smallest when all three sensitivities are fitted; all partial fits have larger misfits compared with the fullparameter fit.

6.4.2. Deactivating Participants’ Roles. Our model considers three roles of blockchain participants; it is important to empirically validate that all three roles take effect in determining platforms’ development. We investigate model performance when one or two terms in the aggregate utility u are excluded. The coefficients are modified correspondingly. For example, when $u _ { i n v e s t o r }$ is excluded, we have $\alpha _ { 2 } = 0$ and $\alpha _ { 1 } = \alpha _ { 3 } = 1 / 2$ . Results show that data series are well fit only when all three roles are activated (Table 5). When $u _ { l a b o r e r }$ is shut down, misfit is increased by 4.3% (from 0.0256 to 0.0267), the smallest increase among the six alternatives. This is consistent with that (1) $u _ { l a b o r e r }$ plays a key role in determining the early-stage dynamics of platform development (Section 5.1), whereas the data set may not cover blockchains complete early-stage trajectory, (2) as mentioned, many platforms do not well support the laborer’s role, thus may be fitted reasonably with the other two roles taking place. Separating the misfits at platforms with and without clear access to crypto labor, under these incomplete fitting setups, confirms that our model fits better at three-role well-defined platforms (Online Appendix G). In general, these experiments confirm that all three roles (user, investor, and laborer) take effects in determining a blockchain platform’s development.

Table 5. Model Performance Under Different Fitting Setups

<table><tr><td>Fitting setup</td><td>Fitted parameter</td><td>Average Δmin</td><td>Reference</td></tr><tr><td>—</td><td>τ, tp [1,12]</td><td>0.0256</td><td></td></tr><tr><td>Full-parameter fit</td><td>τ, tp [1,12], α1, α2, α3, β, K+, K-, h, wm</td><td>0.0144</td><td></td></tr><tr><td>—</td><td>τ, tp [1,12], β</td><td>0.0179</td><td>6.4.1</td></tr><tr><td>—</td><td>τ, tp [1,12], K+, K-</td><td>0.0186</td><td>6.4.1</td></tr><tr><td>—</td><td>τ, tp [1,12], β, K+, K-</td><td>0.0153</td><td>6.4.1</td></tr><tr><td>uuser removed</td><td>τ, tp [1,12]</td><td>0.0330</td><td>6.4.2</td></tr><tr><td>uinvestor removed</td><td>τ, tp [1,12]</td><td>0.0383</td><td>6.4.2</td></tr><tr><td>ulaborer removed</td><td>τ, tp [1,12]</td><td>0.0267</td><td>6.4.2</td></tr><tr><td>uuser only</td><td>τ, tp [1,12]</td><td>0.0537</td><td>6.4.2</td></tr><tr><td>uinvestor only</td><td>τ, tp [1,12]</td><td>0.0328</td><td>6.4.2</td></tr><tr><td>ulaborer only</td><td>τ, tp [1,12]</td><td>0.0381</td><td>6.4.2</td></tr><tr><td>Dynamic P = Pconst + cp t</td><td>τ, tp [1,12], α1, α2, α3, β, K+, K-, h, wm, P0, cp</td><td>0.0175</td><td>6.4.4</td></tr><tr><td>Nonnegative utilities</td><td>τ, tp [1,12], α1, α2, α3, β, K+, K-, h, wm</td><td>0.0148</td><td>6.4.5</td></tr></table>

6.4.3. Forward Series Length. We test using q times the length of the data series as the length of the forward model series, that is, an instance-specific forward series length instead of a fixed forward series length $T _ { m a x } .$ Misfit is always reduced when $q$ increases, for all models (reference models and our model) and all fitting setups, since the probability of matching the data are increased when a longer model series is used as the background. Our model does not perform optimally when q is small; however, when q is set to a length comparable to the average instance-specific length across series, the model performs better (see Online Appendix H for details). Unlike the reference scalings that can take arbitrary shapes, our model’s dynamic trajectories are substantially constrained; a minimum forward length is required such that the three-phase trajectory can be sufficiently developed. For short data series, q times the series length may not be sufficient to fully release model dynamics. We thus only use the fixed length. In Online Appendix D, we report the results of combined lengths: the maximum of 500 weeks or three times the data length. This allows sufficient matching background for the 20 longest series exceeding 500/3 \~166 weeks. We experimented with different fixed lengths and decided that $T _ { m a x } = 5 0 0$ weeks is an appropriate number, within which timeframe the three-phase model dynamics can sufficiently develop (Figure 2). Further increasing the forward series length improves the model’s fitting performance only slightly even when the probability of matching the data is considerably increased.

6.4.4. Dynamic Investment Intensity P(t). For laborers, a constant L is valid, as laborers are expected to spend a certain amount of time each week on crypto labor. For investors, a constant weekly investment of $P$ may be less valid. First, as blockchains attract increasing attention, participants may invest more in tokens. Second, among the entire population on blockchains, the proportion of investors is growing over time, suggesting an increase in $\alpha _ { 3 } u _ { i n v e s t o r } ,$ , which can translate into an increase in P. We test a dynamic $P ( t ) = P _ { c o n s t } + c _ { p } t$ and add $P _ { c o n s t }$ and $c _ { p }$ to the fitted parameter set. It shows that this treatment does not improve results and leads to a higher misfit (0.0175 compared with 0.0144; Table 5) due to the failure from identifying the correct optimum in an amplified fitting space. The average fitted $P _ { c o n s t } { = } 1 { , } 0 5 4 { , } ~ c _ { p } = - 0 . 0 0 1 4$ (Figure 9). We thus drop the time-dependence term and keep $P { = } P _ { c o n s t } { = } 1 { , } 0 0 0$ to the first order.

6.4.5. Nonnegative Role Composition. For the main result, we adopt an unconstrained fitting setup where $\alpha _ { 1 }$ to $\alpha _ { 3 }$ are allowed to take negative values. A negative role composition indicates that this participant role may be dragging down the overall utility of the platform; with this role removed, the platform could become even more useful by only supporting the other functions. Results show that only 15 of 336 fitted $\alpha _ { 1 / 2 / 3 }$ are negative, suggesting that the situation of a “useless” role is rare (Online Appendix D). We test a constrained fitting setup where $\alpha _ { 1 }$ to $\alpha _ { 3 }$ are not allowed to take negative values. Results suggest that the overall misfit changes little (0.148 compared with 0.144; Table 5). The model’s performance is robust across this constraint.

Similarly, the other noninteger parameters are allowed to take negative values in the main result. There are 1, 0, 2, 10, and 3 negative instances out of 112 instances in the best-fit, on $\beta , K ^ { + } , K ^ { - } , h ,$ and $w _ { m } ,$ respectively (Online Appendix D). Adopting the nonnegative constraint does not change results and model performance.

Figure 9. (Color online) Best-Fit $P _ { c o n s t }$ and $c _ { p }$ for Each Data Series with Dynamic $P ( t ) = P _ { c o n s t } + c _ { p } t$  
(a)  
![](/api/attachments/UR5TSQG9/fulltext/images/f83e2fbee7d8d16100ad4623cd42d52ee237f46c85ee328e6ca2a2f0af97e712.jpg)

(b)  
![](/api/attachments/UR5TSQG9/fulltext/images/a9372c1fb28bcd23a7d1006b3770e494789991c4c42656ff6bb1cbd6fb3218ad.jpg)  
Notes. Average values across all series (solid bar) and the standard deviations (dotted bar) are shown against the base values (dash bar). One out lier excluded from the plot.

6.4.6. Alternative Misfit Function. In place of $\Delta _ { m i n } ,$ we test using one minus the (Pearson) correlation coefficient between the data series and the model series as the misfit function to be minimized in the fitting. The test results suggest that this is not a good measure of the overall distance between the model and the data. For example, we can generate two series from the same long-term trend, with Series 1 adding a small δ at each time step and Series 2 subtracting δ at each time step. In this case, although the two series are close, their correlation coefficient can be small or even negative, suggesting an invalid distance measure.

6.4.7. Smoothing. Our model series embodies the intrinsic period 2 oscillation originating from the utilityadoption feedback as well as other possible longer-period oscillations. We investigate model performance when the forward series is smoothed with window length s. s � 3 filters out the period 2 oscillation, and larger s further smooths the development curve. The test results suggest that increasing s to a certain level does enhance fitting performance (Online Appendix H), with s \~ 11 being the optimal smoothing window. We nevertheless report our results without smoothing, as the use of smoothing is artificial and undermines the model’s interpretability.

## 7. Model Extension: Forking

Forking is an infrequent yet impactful event on blockchains (Karame 2016, Constantinides et al. 2018). Accord ing to Wikipedia, forking on a blockchain is the process by which a blockchain is split into two distinct pathways. This event can either be a hard fork or a soft fork. Forking can be intentional, for example when it is used to introduce new features to a blockchain, or accidental when a technical vulnerability is exploited. At forking events, adversaries may exploit technical loopholes in protocols or other boundary resources (Karhu et al. 2018) to create side platforms from the main chain, often resulting in great utility loss for the main chain. Through our model, we are able to replicate and analyze these events.

We investigate the effect of hard fork (“fork” hereinafter) events on blockchain’s lifespan by considering events with varying launch dates and magnitudes. We denote a forking event as $F o r k ( \gamma , T _ { f o r k } )$ , which results in a one-time loss in utility u with amplitude γ (measured as a fraction of u) at time $T _ { f o r k }$ . Our base case (Figure 2) serves as the reference development trajectory.

Our analysis reveals that forking events launched at different stages of blockchain development have varying impacts on the platform (see Figures 10 and 11 and Online

Figure 10. (Color online) Forking Events (η Curve)  
(a)  
![](/api/attachments/UR5TSQG9/fulltext/images/23d8d4a17cc450ccc4adc41c1b5dd0e5381cddaa473d68a237f941257b9e5bdd.jpg)

(b)  
![](/api/attachments/UR5TSQG9/fulltext/images/bb8a26b4ceff7863a2d2ee7914ec5b3331600bfab575b6ea2605d9980f910679.jpg)

(c)  
![](/api/attachments/UR5TSQG9/fulltext/images/2306de4c21f9f39b57c2b729fa607c613b82c9a6361833936dbb81e01281524b.jpg)  
Notes. The development trajectory is shown before peak adoption (solid curve), as well as the ultimate adoption level after the system become stable (dotted line). We compare the effect of forking events at different magnitudes $( \gamma = 0 . 2 , 0 . 5 , 0 . 8 )$ on the base-case trajectory $\dot { ( \gamma } = 0 )$ . Forking is launched at (a) Week 15, (b) Week 100, or (c) Week 300. Magnified portions of (a) and (b) are shown in the insets.

Appendix I for forking events launched at other dates). Specifically, we considered forking events launched at Week 15, 100, and 300, with amplitude $\gamma = 0 . 2 , 0 . 5 , 0 . 8$

• When forking takes place during the early stage of the blockchain $( T _ { f o r k } = 1 5 )$ , the utility loss is soon recovered, after which the event does not cause visible damage to the chain (Figure 10(a), inset; Figure 11(a); also see Figures A23(a) and A24(a) in the online appendix). However, in the long run, the forked chain’s ultimate adoption level can be substantially different across different forking scenarios (Figure 10(a), dashed lines; unsurprisingly, it can also be similar across different scenarios; see Figure A23(a) in the online appendix). Counterintuitively, forking events on a minor or intermediate scale $( \gamma = 0 . 2 , 0 . 5 )$ can be beneficial to the main chain in the long term, although larger-scale forking $( \gamma = 0 . 8 )$ certainly harms the platform. This phenomenon of a small immediate effect but a significant long-term effect occurs due to the chaotic nature of the transition between Phase 1 and Phase 2 (Ott et al. 1990). In this region, the system state is particularly sensitive to any disturbance and even a slight variation can lead to completely different outcomes. The effects of an early-stage forking may be negligible in the short term and the blockchain can recover quickly; however, as more investors enter the platform, the impact of the earlier forking is amplified (Figure 11(a)). This chaotic nature of the consequence of forking is similar to what is observed in the real world: Forkings from a blockchain’s early stage can reveal their latent effects when the platform is becoming popular, particularly when its financial aspect is more evident.

• When forking occurs at the intermediate stage of the blockchain $( T _ { f o r k } = 1 0 0 )$ , the utility loss immediately affects the course of development (see Figures 10(b), inset and 11(b) and Figures A15(b) and A16(b) in the online appendix). In this case, forking events can be ben eficial for the main chain. Although the long-term adop tion level is only slightly impacted, forking accelerates platform development (Figure 10(b)). This is due to the utility oscillation created by the utility loss (Figure 11(b)), which exposes arbitrage opportunities that attract investors. As a result, Phase 2 is entered earlier as inves tors activate the platform, allowing the development to enter the fast lane. This is analogous to the real world, where forking events increase the exposure of the forked chain and bring the platform to the public, thus substantially accelerating platform development.

• When a fork occurs after the blockchain has matured $( T _ { f o r k } = 3 0 0 )$ , it causes minimal disruption to the platform and only slightly alters its future development trajectory (Figures 10(c) and 11(c); also see Figures $\mathsf { A } 2 3 ( \mathsf { c } )$ and A24(c) in the online appendix). This is true even for a large utility loss $( \gamma = 0 . \bar { 5 } \mathrm { { o r } } 0 . 8 )$ and can happen when the fork is launched at the trough (Figure 11(c)) or the peak (Figure A24(c) in the online appendix) of the utility cycle. This suggests that the late-stage oscillation sustained by $u _ { u s e r }$ and $u _ { i n v e s t o r }$ is not in the chaotic region and is instead characterized by two adoption states that serve as stable attractors. However, this is merely a conceptual projection of real-world situations, as most blockchain platforms are still far from reaching a stable development stage.

Figure 11. (Color online) Forking Events (u Curve)  
(a)  
![](/api/attachments/UR5TSQG9/fulltext/images/124fde30870f334c483864b5cfb39ac74faab61aa1258edc50c2cd6b9033b5dd.jpg)

(b)  
![](/api/attachments/UR5TSQG9/fulltext/images/ef2b56b85ca2284ec973aa5788e58509a625555812c114f3785fe86ed25f6fd7.jpg)

(c)  
![](/api/attachments/UR5TSQG9/fulltext/images/516161f090d95e1240400b8bdaf5df984e19097bd5b6a6063a1858c2f5263f0b.jpg)  
Notes. Platform utility dynamics are altered after the blockchain is forked. (a) Forking at Week 15. The subsequent transition from Phase 1 to Phase 2 is chaotic, which magnifies the effect of the earlier forking. (b) Forking at Week 100. The impact of forking takes place immediately; th platform enters Phase 2 development more quickly. (c) Forking at Week 300. The event has little influence on the platform’s subsequent develop ment. In $( \mathrm { c } ) , \gamma = 0 , \gamma = 0 . 2$ are overlapped by γ � 0:5.

Overall, our results show that the launch time of forking events is more important than their amplitude when it comes to the development trajectory of a forked chain. Forks taking place at different stages of blockchain’s development can have different impacts, with some being more beneficial in the long term than in the short term. Moreover, increased exposure of a forked platform to the public, in particular to investors, can bring positive effects to its subsequent development. Results on forking highlights the chaotic features of early-stage blockchain development, which are closely linked to the concept of path dependence (Pierson 2000). A small change in utility during platform’s early-stage development may have a considerable impact on its long-term trajectory. This effect may be hard to notice immediately, leading to a path-dependent development, but it will become more evident as the blockchain evolves and enters a new growth phase. Conversely, the development trajectory in the late stages of the process is usually quite stable, oscillating between high and low adoption states in accordance with the established market cycle.

Given the unpredictable nature of forking and the absence of counterfactual trajectories, it is challenging to empirically validate the model’s depiction of these events. However, significant hard fork events (Table $^ { 6 , }$ gathered from public information) suggest that the simulation results are qualitatively consistent with real-world situations to a promising degree. The 2016 Ethereum hard fork, which resulted in the creation of Ethereum Classic, occurred during the second stage of the main chain’s development, just as the project was approaching public crowdfunding. The outcome of the fork was a swift recovery with negligible short-term impact, but it provided a significant long-term boost for the main chain. In essence, the fork was highly beneficial to Ethereum, primarily by increasing its exposure to investment. In 2017, Bitcoin experienced two consecutive hard forks within a few months, leading to the creation of Bitcoin Cash and Bitcoin Gold. At this point, Bitcoin was already well established, with more than 5 years of history, and neither of the two hard forks caused significant damage or provided a substantial boost to the main chain, consistent with the simulation results. Bitcoin largely continued its development pattern. In contrast, shortly after its inception, Bitcoin Cash underwent a hard fork of its own, resulting in Bitcoin SV. Reflecting the simulation results, this early-stage fork caused noticeable harm to the main chain, with its token price remaining lower than the prefork value for most of the following two years.

Table 6. Important Blockchain Hard Fork Events

<table><tr><td>Time</td><td>Main chain</td><td>Derivative</td><td>Main chain launch time (as of token price listing)</td><td>Token price change (after six months)</td></tr><tr><td>2016.3</td><td>Ethereum</td><td>Ethereum classic</td><td>2014.7</td><td>700%</td></tr><tr><td>2017.8</td><td>Bitcoin</td><td>Bitcoin cash</td><td>2011.4</td><td>250%</td></tr><tr><td>2017.10</td><td>Bitcoin</td><td>Bitcoin gold</td><td>2011.4</td><td>200%</td></tr><tr><td>2018.11</td><td>Bitcoin cash</td><td>Bitcoin sv</td><td>2017.8</td><td>100%</td></tr></table>

Modeling the initiation and progression of forking events, the vulnerability of the main chain, and the subsequent development of the derivative chain, falls outside the scope of the current model. However, these empirical observations lend support to the model’s potential for describing hard forks during the development of a blockchain. The qualitative findings from the simulations align with real-world observations.

## 8. Concluding Remarks

We construct a parametric model to examine the developmental trajectory of blockchain platforms. We propose that the model’s dynamics are driven by the feedback between changes in the blockchain’s utility and the adoption/abandonment of the platform by its participants. We contend that it is crucial to consider the various roles that platform participants can assume when studying the development of blockchain platforms. In our model, a typical participant in a blockchain platform fulfills three roles: user, investor, and laborer. Each of these roles contributes to the multifaceted utility of the blockchain for the participant. Consequently, we perceive blockchain platforms as facilitating three primary functions: providing services for transactions and interactions, serving as a digital investment medium, and offering an online workspace for labor.

Rather than relying on a single role for adopters, this model offers a more comprehensive approach to understanding blockchain platform development trajectories. In the base case, a three-phase development trajectory is outlined that closely mirrors real-world scenarios. The roles of user, investor, and laborer are distinct, each playing an important part at different stages of platform develop ment. At the initial stage, a blockchain is sustained by the incentive of high rewards for labor, allowing the network to grow gradually. As the profitability of labor decreases, investors are drawn to the platform to take advantage of arbitrage opportunities, accelerating the growth of the platform. This growth reaches its peak when the utility of the blockchain stops increasing beyond the saturation point, and further increase in the adopter population decreases the quality of the platform’s service. This creates a stable market cycle, with the platform alternating between high and low utility and large and small adopter population. Through the specification of model parameters, various scenarios of blockchains lifespan patterns can be demonstrated.

A prevalent challenge for simulation models is the vast parameter space and unbounded model trajectories (Li and Dahleh 2020). To mitigate this, we have carefully constrained the parameter space. Global parameters are set to realistic values and treated as constants within the model. An extensive simulation is used to analyze the seven network-specific parameters and the three sensitivity parameters. The influence of these parameters on the model’s dynamics is evident, and the model trajectories remain comprehensible.

Our model exhibits superior fitting performance with an equal or fewer number of parameters compared with scaling models such as exponential, power-law, polynomial, netoid function, and exponential power-law. The fitting results are validated from various perspectives, and the model demonstrates consistent and robust per formance. We extend the model to study forking events, reiterating that model dynamics incorporate both chaotic features (during the Phase 1–Phase 2 transition) and a stable region (Phase 3). Our investigation further sug gests that the timing of a fork in relation to the develop ment stage of the forked chain is more influential on the main chain’s subsequent development than the magnitude of the forking event. Moreover, forking can be beneficial for blockchains by increasing the visibility of the forked platform. We also expand the model to address uncertainties in platform development (Online Appendix J), indicating that a platform’s growth is more sensitive to adoption than to abandonment, and that participants are more responsive to changes in a blockchain’s utility during adoption than during abandonment.

A key discovery of this study is the role of two temporal parameters, τ and $t _ { p } ,$ in differentiating the development trajectories of blockchain platforms. τ gauges the inertia of participants when leaving the platform, with a small value suggesting a lack of trust and a large value indicating a high switching cost. $t _ { p }$ reflects transaction speed and price volatility of platform tokens, with high/ low volatility and high/low transaction velocity resulting in a shorter/longer holding time. Empirical results have demonstrated the effectiveness of these two parameters in classifying blockchains.

## 8.1. Practical Insights

This model can be developed into a decision-support tool for various stakeholders, including token investors, blockchain entrepreneurs, and government agencies. By utilizing the model for exploratory analysis (e.g., simulation), explanatory analysis (e.g., estimation), or prescriptive analysis (e.g., prediction), these stakeholders can benefit from a helpful tool to aid in system design, targeted investment strategies, early-warning signal detection, and regulatory decisions.

(1) For platform participants. The framework can assist in making platform participation decisions, including strategies for token investment and crypto labor. Participants can forecast the profitability of their actions across different types of platforms and under varying market conditions.

(2) For platform owners. The framework functions as a quantitative diagnostic tool for healthy platform development. Owners can use the model to assess their platform’s appeal to participants, its resilience to short-term events, and its momentum for long-term development.

(3) For platform regulators. The framework is beneficial for analyzing interactions between the platform and its participants, detecting early warning signals, and making regulatory decisions. It aids in studying the coevolution of strategic customer participation and strategic platform development.

Although this model does not provide technical design parameters for building blockchain platforms, it does offer “observables” that are useful to regulators, economists, and market observers in assessing the state and development of platforms. These observables include $\alpha _ { 1 / 2 / 3 . }$ , which indicates the role composition of an average platform participant and reveals the intensity of different on-chain activities; $K ^ { + / - }$ , which indicates the volatility of platform diffusion, reflecting the platform’s popularity and participants’ attitudes; τ and $t _ { p } ,$ which indicate participants’ willingness to engage, denoting platform inertia and participants propensity for token investment; and $h , \ \beta ,$ and $w _ { m } ,$ which characterize the platform in each of its three functionalities.

## 8.2. Limitations and Future Directions

This study is limited in a number of ways. First, model parameters, in particular sensitivity parameters, could be further constrained based on empirical considerations. Additionally, it is possible that some model constants, such as the representative participant’s role composition $( \alpha _ { 1 / 2 / 3 } )$ , may be dynamic over the course of platform development, or change at different stages, thereby chal lenging the time-invariant assumption. To explore model’s parameter space, machine-learning methods could be employed, although this would likely increase com putation costs. Second, data used in this study is comprised of trajectories from well-performing blockchain platforms and is therefore not fully representative of the entire sector. Furthermore, the data set does not span the complete history of archived platforms. Price series are also indirect observations of development trajectories, and data from a variety of sources is needed to furthe validate the model. In particular, it is important to employ more recent data to investigate how much our results hold after COVID-19 when the landscape of cryptocurrencies has significantly changed and the booming of NFT has taken place. Third, while the SIS model cap tures the first-order dynamics of platform adoption, more detailed compartment models can be constructed to provide a higher resolution of adoption, albeit coming at the cost of an enlarged parameter space. Finally, the current utility function considers platform adoption from the perspective of a representative blockchain participant, which is consistent with the aggregate SIS compartment model. Alternative models could nonetheless consider individual decision making at adoption and role playing or use agent-based dynamics to simulate adoption/abandonment. This granular approach accounts for heterogeneity but will be computationally intensive and will reduce interpretability.

Currently, blockchain-related adversarial events such as collapse, failure, and forking are not standard components of the model. These unpredictable events, however, have been becoming increasingly common in recent years.<sup>6</sup> Our model is able to accommodate endogenous dynamics within the system (internal triggers of platform collapses tied to market development), but cannot process exogenous shocks to the system (technical glitches, community divisions, changes in domestic poli cies, and global financial market fluctuations). Predicting adversarial events is difficult, and modeling the socioeconomic backdrop that spawns these events exceeds the scope of current research capabilities.

There have been a few attempts to illustrate the model’s predictive capabilities: simulations have demonstrated the ability to reproduce forking events and trajectory analysis has shown that platform lifespans can be estimated with a given set of platform para meters. These approaches can be instrumental in diagnosing platform health through simulation, but the model has yet to be transferred to an early-warning system for real-time monitoring of blockchain platform development. This is a clear limitation of the model and a significant area of focus for future research.

Evidence, such as that presented in Table 6 and Online Appendix K, suggests that the three-stage platform development model established in this study closely resembles real-world situations, thus endorsing its effectiveness. However, the model is currently only qualitative in nature. While the stages are likely valid, the transition interval between stages and the amplitude of each stage may vary between platforms. In future work, it would be of great interest to quantify this staging and further enhance the practical utility of the model, for instance, by classifying platforms into Stages 1, 2, or 3. Moreover, as previously mentioned, the model’s inability to anticipate sudden collapses or forks (e.g., the LUNA event) renders it unsuitable for diagnosing unexpected events. Therefore, the efficacy of the current model should not be overestimated.

## 9. Outlook

## 9.1. Generic Growth, Acceleration, and Volume: Participant’s Multiple Roles Revisited

Reflecting on the three utility terms characterizing participants’ distinct roles on blockchains, we may derive a deeper understanding of the three roles.

• Utility from the user’s role— $- u _ { u s e r } .$ this determines the generic growth of a digital platform, characterizing the relationship between usage saturation and adoption saturation. This utility is applicable to a variety of platforms, not just blockchains.

• Utility from the investor’s role— $- u _ { i n v e s t o r } { : }$ this captures the acceleration of platforms’ development, where investment decisions are made based on the velocity of network growth. This utility can be applied to a variety of financial assets, not just digitized ones.

• Utility from the laborer’s role— $- u _ { l a b o r } .$ this depends on the volume of the blockchain, where service rewards are adjusted with respect to population. This utility triggers the launch of the platform and is a typical feature of blockchains. The reward structure of other online labor activities generally does not take global network volume into account.

Blockchains represent a unique type of digital platform due to the intricate division of labor among three distinct utilities, each playing a crucial role in platform’s development. The integration of these functionalities catalyzes the diversification and evolution of platforms. The notion that users drive growth, investors pursue acceleration, and laborers constitute volume may suggest a fundamental link to societal principles.

## Acknowledgments

The authors thank Christian Catalini at Massachusetts Institute of Technology Sloan for contributing to the idea of participant’s multirole and for the generous help at the early stage of this study and two reviewers and associate editor for the careful examination of the manuscript and the invaluable comments and suggestions that substantially improved the paper.

## Endnotes

<sup>1</sup> The initial meaning of “miner” applies to people conducting crypto labor in PoW systems, as in Bitcoin. For blockchains using more recent consensus mechanisms, such as various forms of PoS, people may not be “mining” as in PoW but conduct other digital labor (sometimes still termed as “mining”) to contribute to the sys tem. These labors are generally available to blockchain participants, whom we term as “laborers” with regard to this activity.

$^ 2 \mathrm { S e e }$ https://news.bitcoin.com/mineable-cryptocurrencies-are-farmore-valuable-than-non-mineable-coins.

<sup>3</sup> See https://www.forbes.com/sites/leeorshimron/2022/09/17.

4 These are clearly simplifying assumptions. In practice, labor reward values fluctuate with the token price, and rewards may adjust dynamically and consist of various components (e.g., transaction fees, access grants, governance bonuses), depending on the platform’s consensus mechanism and incentive structure. Here we use inverse proportion to keep first-order consistency.

$^ 5 \mathrm { I t }$ is worth noting that some platforms are cryptocurrency exchanges themselves, whose usage utility is substantially autocorrelated with token price and crypto market trends. Consistently, our model fits slightly worse to these cases (Online Appendix D) where the user’s role and the investor’s role can be confounded.

<sup>6</sup> See https://www.coingecko.com/research/publications/how-manycryptocurrencies-failed.

## References

Adamopoulos P, Ghose A, Todri V (2018) The impact of user personality traits on word of mouth: Text-mining social media platforms. Inform. Systems Res. 29(3):612–640.

Afuah A (2013) Are network effects really all about size? The role of structure and conduct. Strategic Management J. 34(3):257–273

Alabi K (2017) Digital blockchain networks appear to be following Metcalfe’s Law. Electronic Commerce Res. Appl. 24:23–29.

Altan A, Karasu S, Bekiros S (2019) Digital currency forecasting with chaotic meta-heuristic bio-inspired signal processing tech niques. Chaos Solitons Fractals 126:325–336.

Anderson PW (2018) The Economy as an Evolving Complex System (CRC Press, Boca Raton, FL).

Anderson SP, Foros Ø, Kind HJ (2019) The importance of consumer multihoming (joint purchases) for market performance: Merger and entry in media markets. J. Econom. Management Strategy 28(1):125–137.

Andoni M, Robu V, Flynn D, Abram S, Geach D, Jenkins D, Peter McCallum D, Peacock A (2019) Blockchain technology in the energy sector: A systematic review of challenges and opportunities. Renewable Sustainable Energy Rev. 100:143–174.

Bass FM (1969) A new product growth for model consumer durables. Management Sci. 15(5):215–227.

Beck R, Michel A, Rossi M, Thatcher JB (2017) Blockchain technol ogy in business and information systems research. Bus. Inform. Systems Engrg. 59(6):381–384.

Berinsky AJ, Huber GA, Lenz GS (2012) Evaluating online labo markets for experimental research: Amazon.com’s Mechanical Turk. Political Anal. 20(3):351–368.

Besley T, Case A (1993) Modeling technology adoption in develop ing countries. Amer. Econom. Rev. 83(2):396–402.

Bo¨hme R, Christin N, Edelman B, Moore T (2015) Bitcoin: Economics, technology, and governance. J. Econom. Perspective 29(2):213–238.

Bolloba´s B (1980) A probabilistic proof of an asymptotic formula for the number of labelled regular graphs. Eur. J. Combination 1(4):311–316.

Brandyberry AA (2003) Determinants of adoption for organisational innovations approaching saturation. Eur. J. Innovation Management 6(3):150–158.

Brewer EA (2000) Toward robust distributed systems, PODC (vol. 7), 343477–343502.

Brynjolfsson E, Wang C, Zhang X (2021) The economics of IT and digitization: Eight questions for research. Management Inform. Systems Quart. 45(1):473–477.

Burniske C, Tatar J (2018) Cryptoassets: The Innovative Investor’s Guide to Bitcoin and Beyond (McGraw Hill, New York).

Burtch G, Carnahan S, Greenwood BN (2018) Can you gig it? An empirical examination of the gig economy and entrepreneurial activity. Management Sci. 64(12):5497–5520.

Catalini C, Gans JS (2018) Initial coin offerings and the value of crypto tokens. NBER Working Paper No. w24418, National Bureau of Economic Research, Cambridge, MA.

Catalini C, Gans JS (2020) Some simple economics of the blockchain. Comm. ACM 63(7):80–90.

Cennamo C, Santalo J (2013) Platform competition: Strategic trade-offs in platform markets. Strategic Management J. 34(11):1331–1350.

Cennamo C, Ozalp H, Kretschmer T (2018) Platform architecture and quality trade-offs of multihoming complements. Inform. Systems Res. 29(2):461–478.

Centola D (2010) The spread of behavior in an online social network experiment. Science 329(5996):1194–1197.

Chen DL, Horton JJ (2016) Research note—Are online labor markets spot markets for tasks? A field experiment on the behavioral response to wage cuts. Inform. Systems Res. 27(2):403–423.

Chod J, Lyandres E (2021) A theory of ICOs: Diversification, agency, and information asymmetry. Management Sci. 67(10):5969–5989.

Chod J, Trichakis N, Yang SA (2021) Platform tokenization: Financing, governance, and moral hazard. Management Sci. 68(9):6411–6433.

Claussen J, Kretschmer T, Mayrhofer P (2013) The effects of rewarding user engagement: The case of Facebook apps. Inform. Sys tems Res. 24(1):186–200.

Colombo MG, Mosconi R (1995) Complementarity and cumulative learning effects in the early diffusion of multiple technologies. J. Industry Econom. 43(1):13–48.

Cong LW, Li Y, Wang N (2021) Tokenomics: Dynamic adoption and valuation. Rev. Financial Stud. 34(3):1105–1155.

Constantinides P, Henfridsson O, Parker G (2018) Introduction: Plat forms and infrastructures in the digital age. Inform. Systems Res. 29(2):381–400.

Davis FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. Management Inform. Systems Quart. 319–340.

Davis FD, Bagozzi RP, Warshaw PR (1989) User acceptance of computer technology: A comparison of two theoretical models. Management Sci. 35(8):982–1003.

de Sola Pool I, Kochen M (1978) Contacts and influence. Soc. Networks 1(1):5–51.

Del Vicario M, Bessi A, Zollo F, Petroni F, Scala A, Caldarelli G, Eugene Stanley H, Quattrociocchi W (2016) The spreading of misinforma tion online. Proc. National Acad. Sci. USA 113(3):554–559.

Dellarocas C, Zhang X, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):2–20.

Dong D, Saha A (1998) He came, he saw, (and) he waited: An empiri cal analysis of inertia in technology adoption. Appl. Econom. 30(7):893–905.

Dou Y, Niculescu MF, Wu DJ (2013) Engineering optimal network effects via social media features and seeding in markets for digital goods and services. Inform. Systems Res. 24(1):164–185.

Dunbar RI (1992) Neocortex size as a constraint on group size in primates. J. Human Evolution 22(6):469–493.

Dwivedi YK, Rana NP, Jeyaraj A, Clement M, Williams MD (2019) Re-examining the unified theory of acceptance and use of technology (UTAUT): Toward a revised theoretical model. Inform. Systems Frontiers 21(3):719–734.

ElBahrawy A, Alessandretti L, Kandler A, Pastor-Satorras R, Baronchelli A (2017) Evolutionary dynamics of the cryptocurrency market. Royal Soc. Open Sci. 4(11):170623.

Fujimoto K, Valente TW (2012) Social network influences on adolescent substance use: Disentangling structural equivalence from cohesion. Soc. Sci. Medicine 74(12):1952–1960.

Geroski PA (2000) Models of technology diffusion. Res. Polic 29(4–5):603–625.

Ghobakhloo M, Ching NT (2019) Adoption of digital technologies of smart manufacturing in SMEs. J. Industry Inform. Integration 16:100107.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Goodell JW, Goutte S (2021) Co-movement of COVID-19 and Bitcoin: Evidence from wavelet coherence analysis. Finance Res. Lett. 38:101625.

Haki K, Beese J, Aier S, Winter R (2020) The evolution of information systems architecture: An agent-based simulation model Management Inform. Systems Quart. 44(1):155–184.

Han SP, Park S, Oh W (2016) Mobile app analytics: A multipl discrete-continuous choice framework. Management. Inform. Systems Quart. 40(4):983–1008.

Hannan MT, Freeman J (1984) Structural inertia and organizational change. Amer. Sociol. Rev. 149–164.

Hao H, Padman R, Sun B, Telang R (2018) Quantifying the impact of social influence on the information technology implementation process by physicians: A hierarchical Bayesian learning approach. Inform. Systems Res. 29(1):25–41

Hendershott T, Zhang X, Zhao JL, Zheng Z (2021) FinTech as a game changer: Overview of research frontiers. Inform. Systems Res. 32(1):1–17.

Hethcote HW (1989) Three basic epidemiological models. Applied Math ematical Ecology (Springer Berlin Heidelberg, Berlin), 119–144.

Howell ST, Niessner M, Yermack D (2020) Initial coin offerings: Financing growth with cryptocurrency token sales. Rev. Financial. Stud. 33(9):3925–3974.

Huberman G, Leshno JD, Moallemi C (2021) Monopoly without a monopolist: An economic analysis of the bitcoin payment system. Rev. Econom. Stud. 88(6):3011–3040.

Iansiti M, Lakhani KR (2017) The truth about blockchain. Harvard Bus. Rev. 95(1):118–127.

Jackson MO (2010) Social and Economic Networks (Princeton University Press, Princeton, NJ).

Kanter RM (2006) Innovation: The classic traps. Harvard Bus. Rev 84(11):72–83.

Karahanna E, Straub DW, Chervany NL (1999) Information technology adoption across time: A cross-sectional comparison of preadoption and post-adoption beliefs. Management Inform. Systems Quart. 23(2):183–213.

Karame G (2016) On the security and scalability of bitcoin’s block chain. Proc. ACM SIGSAC Conf. on Comput. and Comm. Securit (Association for Computing Machinery, New York), 1861–1862.

Karhu K, Gustafsson R, Lyytinen K (2018) Exploiting and defending open digital platforms with boundary resources: Android’s five platform forks. Inform. Systems Res. 29(2): 479–497.

Katona Z, Zubcsek PP, Sarvary M (2011) Network effects and personal influences: The diffusion of an online social network. J. Marketing Res. 48(3):425–443.

Khern-am-nuai W, Kannan K, Ghasemkhani H (2018) Extrinsic vs. intrinsic rewards for contributing reviews in an online plat form. Inform. Systems Res. 29(4):871–892.

Kim K, Park J, Pan Y, Zhang K, Zhang X (2022) Risk disclosure in crowdfunding. Inform. Systems Res. 33(3):1023–1041.

Kovalyov MY, Ng CT, Cheng TE (2007) Fixed interval scheduling: Models, applications, computational complexity and algorithms. Eur. J. Oper. Res. 178(2):331–342.

Lashkari B, Musilek P (2021) A comprehensive review of blockchain consensus mechanisms. IEEE Access 9:43620–43652.

Leduc MV, Jackson MO, Johari R (2017) Pricing and referrals in dif fusion on networks. Games Econom. Behav. 104:568–594.

Li J, Li N, Peng J, Cui H, Wu Z (2019) Energy consumption of cryptocurrency mining: A study of electricity consumption in min ing cryptocurrencies. Energy 168:160–168.

Li T, Dahleh M (2020) Automation of data acquisition strategies in model calibration for system models: Sensor placement. Preprint, submitted June 5, https://dx.doi.org/10.2139/ssrn. 3619653.

Linden A, Fenn J (2003) Understanding Gartner’s hype cycles. Stra tegic Analysis Report No. R-20-1971. Gartner, Inc, 88, 1423.

Lipovetsky S (2010) Double logistic curve in regression modeling. J. Appl. Statist. 37(11):1785–1793.

Luo X, Zhang J, Duan W (2013) Social media and firm equity value. Inform. Systems Res. 24(1):146–163.

Lux T (1998) The socio-economic dynamics of speculative markets: Interacting agents, chaos, and the fat tails of return distribu tions. J. Econ. Behav. Organ. 33(2):143–165.

Lux T, Alfarano S (2016) Financial power laws: Empirical evidence, models, and mechanisms. Chaos Solitons Fractals 88:3–18.

Mahajan V, Muller E, Bass FM (1991) New product diffusion models in marketing: A review and directions for research. Diffusion of Technologies and Social Behavior (Springer, Berlin), 125–177.

Manshadi V, Misra S, Rodilitz S (2020) Diffusion in random networks: Impact of degree distribution. Oper. Res. 68(6):1722–1741.

Martin A, Ventura J (2012) Economic growth with bubbles. Amer. Econom. Rev. 102(6):3033–3058.

McIntyre DP, Srinivasan A (2017) Networks, platforms, and strategy: Emerging views and next steps. Strategic Management J. 38(1): 141–160.

Metcalfe B (1995) Metcalfe’s law: A network becomes more valuable as it reaches more users. Infoworld 17(40):53–53.

Mettler M (2016) Blockchain technology in healthcare: The revolution starts here. e-Health Networking, Applications and Services (IEEE, Piscataway, NJ), 1–3.

Miller A, Litton J, Pachulski A, Gupta N, Levin D, Spring N, Bhattacharjee B (2015) Discovering bitcoin’s public topology and influential nodes. https://www.cs.umd.edu/projects/coinscope/ coinscope.pdf.

Min H (2019) Blockchain technology for enhancing supply chain resilience. Bus. Horizons 62(1):35–45.

Mita M, Ito K, Ohsawa S, Tanaka H (2019) What is stablecoin?: A survey on price stabilization mechanisms for decentralized payment systems. 2019 8th International Congress on Advanced Applied Informatics (IIAI-AAI) (IEEE, Piscataway, NJ), 60–66.

Nakamoto S (2008) Bitcoin: A peer-to-peer electronic cash system. Decentralized business review.

Newman M (2010) Networks: An Introduction (Oxford University Press, Oxford, UK).

Niculescu MF, Wu DJ, Xu L (2018) Strategic intellectual property sharing: Competition on an open technology platform under network effects. Inform. Systems Res. 29(2):498–519.

Oliveira T, Martins MF (2011) Literature review of information technology adoption models at firm level. Electronic J. Inform. Systems Evaluation 14(1):110–121.

Ott E, Grebogi C, Yorke JA (1990) Controlling chaos. Phys. Rev. Lett 64(11):1196.

Parker GG, Van Alstyne MW, Choudary SP (2016) Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You (WW Norton & Company, New York).

Peres R, Muller E, Mahajan V (2010) Innovation diffusion and new product growth models: A critical review and research directions. Internat. J. Res. Marketing 27(2):91–106.

Pierson P (2000) Increasing returns, path dependence, and the study of politics. Amer. Political Sci. Rev. 94(2):251–267.

Press WH (1992) Downhill simplex method in multidimensions. Numerical recipes in C.

Queiroz MM, Wamba SF (2019) Blockchain adoption challenges in supply chain: An empirical investigation of the main drivers in India and the USA. Internat. J. Inform. Management 46:70–82.

Ramasubbu N, Kemerer CF (2016) Technical debt and the reliability of enterprise software systems: A competing risks analysis. Man agement Sci. 62(5):1487–1510.

Reyna A, Mart´ın C, Chen J, Soler E, D´ıaz M (2018) On blockchain and its integration with IoT. Challenges and opportunities. Future Generation Computer Systems 88:173–190.

Risius M, Spohrer K (2017) A blockchain research framework. Bus. Inform. Systems Engrg. 59(6):385–409.

Roberts JH, Urban GL (1988) Modeling multiattribute utility, risk, and belief dynamics for new consumer durable brand choice. Management Sci. 34(2):167–185.

Robins G, Pattison P, Kalish Y, Lusher D (2007) An introduction to exponential random graph (p\*) models for social networks. Soc. Networks 29(2):173–191.

Rolland KH, Mathiassen L, Rai A (2018) Managing digital platforms in user organizations: The interactions between digital options and digital debt. Inform. Systems Res. 29(2):419–443.

Saboo AR, Chakravarty A, Grewal R (2016) Organizational debut on the public stage: Marketing myopia and initial public offerings. Marketing Sci. 35(4):656–675.

Salah K, Rehman MHU, Nizamuddin N, Al-Fuqaha A (2019) Blockchain for AI: Review and open research challenges. IEEE Access 7:10127–10149.

Sharples M, Domingue J (2016) The blockchain and kudos: A distributed system for educational record, reputation and reward Proc. 11th Eur. Conf. on Tech. Enhanced Learn. (Springer International Publishing, New York), 490–496.

Siddiqui S, Singh T (2016) Social media its impact with positive and negative aspects. Internat. J. Comput. Appl. Tech. Res. 5(2):71–75.

Song P, Xue L, Rai A, Zhang C (2018) The ecosystem of software platform: A study of asymmetric cross-side network effects and plat form governance. Management Inform. Systems Quart. 42(1):121–142.

Spilkova J, Chomynova P, Csemy L (2017) Predictors of excessive use of social media and excessive online gaming in Czech teenagers. J. Behav. Addiction 6(4):611–619.

Steiner J, Stewart C, Mate˘jka F (2017) Rational inattention dynamics: Inertia and delay in decision-making. Econometrica 85(2):521–553.

Tapscott D, Tapscott A (2016) The impact of the blockchain goe beyond financial services. Harvard Bus. Rev. 10(7):2–5.

Tellis GJ, Yin E, Niraj R (2009) Does quality win? Network effects vs. quality in high-tech markets. J. Marketing Res. 46(2):135–149.

Tiwana A, Konsynski B, Bush AA (2010) Research commentary: Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Tromholt M (2016) The Facebook experiment: Quitting Facebook leads to higher levels of well-being. Cyberpsych. Behav. Soc. Net works 19(11):661–666.

Truby J (2018) Decarbonizing bitcoin: Law and policy choices for reducing the energy consumption of Blockchain technologies and digital currencies. Energy Res. Soc. Sci. 44:399–410.

Tschorsch F, Scheuermann B (2016) Bitcoin and beyond: A technical survey on decentralized digital currencies. IEEE Comm. Survey Tutor 18(3):2084–2123

Tucker C (2008) Identifying formal and informal influence in technology adoption with network externalities. Management Sci. 54(12):2024–2038.

Tykocinski O, Israel R, Pittman TS (2004) Inaction inertia in the stock market. J. Appl. Soc. Psych. 34(6):1166–1175.

Wang H, Chen K, Xu D (2016) A Maturity Model for Blockchain Adop tion (Springer, New York).

Wang W, Hoang DT, Hu P, Xiong Z, Niyato D, Wang P, Yonggang W, Dong IK (2019) A survey on consensus mechanisms and mining strategy management in blockchain networks. IEEE Access 7:22328–22370.

Weitzel T, Beimborn D, Ko¨nig W (2006) A unified economic model of standard diffusion: The impact of standardization cost, network effects, and network topology. Management Inform. Sys tems Quart. 30:489–514.

Wong LW, Tan GWH, Lee VH, Ooi KB, Sohal A (2020) Unearthing the determinants of Blockchain adoption in supply chain man agement. Internat. J. Production Res. 58(7):2100–2123.

Wood G (2014) Ethereum: A secure decentralised generalised trans action ledger. Ethereum project yellow paper 151:1–32.

Xiao Y, Zhang N, Lou W, Hou YT (2020) Modeling the impact of network connectivity on consensus security of proof-of-work blockchain. Proc. IEEE Conf. on Comput. Comm. (IEEE, Piscataway, NJ), 1648–1657.

Xu SX, Zhang X (2013) Impact of Wikipedia on market informa tion environment: Evidence on management disclosure and investor reaction. Management Inform. Systems Quart. 37(4): 1043–1068.

Xue G, Xu J, Wu H, Lu W, Xu L (2021) Incentive mechanism for rational miners in bitcoin mining pool. Inform. Systems Frontiers 23:317–327.

Yang M, Zheng Z, Mookerjee V (2019) Prescribing response strategies to manage customer opinions: A stochastic differential equation approach. Inform. Systems Res. 30(2):351–374.

Yermack D (2015) Is bitcoin a real currency? An economic appraisal. Handbook of Digital Currency (Elsevier, Amsterdam), 31–43.

Yuan Y, Wang FY (2016) Toward blockchain-based intelligent transportation systems. Proc. IEEE 19th Internat. Conf. on Intelligent Transportation Systems (IEEE, Piscataway, NJ), 2663–2668.

Zhang B, Pavlou PA, Krishnan R (2018) On direct vs. indirect peer influ ence in large social networks. Inform. Systems Res. 29(2):292–314.

Zhang X, Wang C (2012) Network positions and contributions to online public goods: The case of Chinese Wikipedia. J. Manage ment Inform. Systems 29(2):11–40.

Zhang X, Zhang L (2015) How does the internet affect the financial market? An equilibrium model of internet facilitated feedback trading. Management Inform. Systems Quart. 39(1):17–38.

Zhang X, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4): 1601–1615.

Zhang XZ, Liu JJ, Xu ZW (2015) Tencent and Facebook data validate Metcalfe’s law. J. Comput. Sci. Tech. 30(2):246–251.

Zheng Z, Xie S, Dai H, Chen X, Wang H (2017) An overview of blockchain technology: Architecture, consensus, and future trends. Proc IEEE Internat. Congress on Big Data (IEEE, Piscataway, NJ), 557–564.

Zhu F, Iansiti M (2012) Entry into platform-based markets. Strategic Management J. 33(1):88–106.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

Zhu F, Li X, Valavi E, Iansiti M (2021) Network interconnectivity and entry into platform markets. Inform. Systems Res. 32(3):1009–1024.

Zhu L, Wua Y, Gai K, Choo KR (2019) Controllable and trustworthy blockchain-based cloud data management. Future Generation Comput. Systems. 91:527–535.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
