---
otero_id: 27490
otero_key: "RG3HSFC8"
title: "Complementary Online Services in Competitive Markets: Maintaining Profitability in the Presence of Network Effects1"
authors: "Hila Etzion; Min-Seok Pang"
year: "2014"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.1.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# COMPLEMENTARY ONLINE SERVICES IN COMPETITIVEMARKETS: MAINTAINING PROFITABILITY IN THEPRESENCE OF NETWORK EFFECTS<sup>1</sup>

Hila Etzion Department of Technology and Operations, Stephen M. Ross School of Business, University of Michigan, Ann Arbor, MI 48103 U.S.A. {etzionh@umich.edu}

Department of Information Systems and Operations Management, School of Management, George Mason University, Fairfax, VA 22030 U.S.A. {mpang2@gmu.edu}

A growing number of firms are strategically utilizing information technology and the Internet to provide online services to consumers who buy their products. Online services differ from traditional services because they often promote interactivity among users and exhibit positive network effects. While the service increases the value obtained by consumers, network effects are known to intensify price competition and thus may reduce firms’ profits. In this paper, we model the competition between two firms that sell a differentiated product when each firm can offer a complementary online service to its customers. We derive the market equilibrium and determine how firms should adjust their strategies to account for network effects. We find that when the service exhibits network effects, a firm’s decision whether or not to offer the service depends on both the competitor’s decision and the competitor’s service quality. When the service does not exhibit network effects, this is not the case. In addition, we show that a firm can benefit from the technological ability to offer the service, and from an increase in the strength of network effects or in the market size of the service, only when the value customers derive from the direct functionalities (those that do not rely on the network) of the service are sufficiently high. As a result, a firm’s investment in the direct functionalities of its service increases with the strength of network effects of the service as long as the marginal development cost is not too high. Finally, we show that inefficiencies in terms of the number of firms offering the service as well as the total number of service users may prevail.

Keywords: Online services, network effects, e-commerce, analytical modeling

## Introduction

In various industries, ranging from traditional manufacturing to high technology, the locus of competition has shifted from selling products to providing value-adding services. Such services can increase a firm’s revenue and allow it to achieve a competitive advantage (Allmendinger and Lombreglia 2005; Reinartz and Ulaga 2008; Suarez et al. 2013). In particular, recent advances in information and communication technologies, such as Web 2.0 and social technologies (Li and Bernoff 2008), enable firms to provide new types of valueadding services—such as blogs, online forums, peer-to-peer file sharing, and online gaming platforms—to their customers.

These online services differ from traditional services (e.g., maintenance, repair, and training services) because they promote relationship building and interactivity among users and thus exhibit positive network effects. That is, the value of the service to a user increases with the number of other people that subscribe to the service.

One notable type of online service that adds value to consumers who buy a firm’s product and exhibits positive network effects is online communities. For instance, Dell operates Dell Community (www.dell.com/community), which offers valuable complementary services to Dell’s customers. On this online community site, which consists of several online forums for the different product categories sold by Dell, customers can share product information and knowledge. HP offers similar online services to its customers with its Suggestions and Feedback Community, an HP Support Forum, and an HP Software Solutions Community. Oracle and IBM also operate online communities for users of their products. Nike operates Nike Plus (http://nikeplus.nike.com/ plus/), where runners can share their exercise experiences and challenge their peers for motivation.

Online services that complement a product are also typical in the PC and video games industry. Here we consider games that require consumers to purchase and install client software (the product) on their PC or console, and which can be played offline in a single-player mode. Playing offline, the consumer plays predefined scenarios against hypothetical competitors with artificial intelligence. Some of these games (e.g., the Starcraft and Warcraft series) are then complemented by an online service, which enables game owners to play in a multiplayer mode against remote players. For example, in May 2011, Activision (a leader in the computer games industry) announced its plans to launch a new online service called Call of Duty Elite that will complement its next major edition of the video game Call of Duty, which runs on consoles like the PlayStation®3 and Xbox 360 (Wingfield 2011). The service provides extra content that is not offered on game discs sold in stores. In addition, it will let Call of Duty players meet for online battles with other players.

Online gaming websites can also complement durable goods. For example, Ganz offers free access to the Webkinz World website to consumers who purchase its Webkinz plush toys. The website offers functionalities that can be valuable for the child even when no one else uses it (e.g., playing with his virtual pet), as well as interactive features such as chatting and playing with others. GLOBIO, Inc. sells puppets of wild animals and gives its customers free access to the WebWilds website where they can play games, watch videos, and connect with friends.

As can be seen from the above examples, online services can be used to complement both durable goods and information goods and, while there are many types of such services, we can identify a few common features. First, these services encourage interactivity among users and build on communities to create value. The Internet is thus an enabler of these services as it provides the perfect venue for consumers to connect. At an offline venue, the degree of interactivity would be limited. With that said, firms can also utilize the online service to provide content and offer functionalities that do not rely on users interactions. We refer to the value obtained from these latter functionalities as the direct or inherent value of the service. Second, while firms may incur fixed costs when developing the service, they also have provision costs that increase with the number of service users due to higher bandwidth and storage requirements. Finally, online services often add value to the firm’s customers but are not a necessity because the product is valuable to users even without the service. The latter might not be true when considering traditional services; for example, no one would buy a car that can never be serviced.

An important observation is that not all firms in a given industry choose to complement their products with an online service. For example, in the toys industry there are many firms that sell plush toys but do not offer a related website to their customers; however, Gantz and GLOBIO chose to develop and offer such a website. In the video games industry, some video games include online capabilities while others do not. For example, among the video games available for PlayStation 3 in the “shooter” category, Call of Duty, GoldenEye 007, and Unchartered 3 support online connectivity and have a multiplayer mode, while Hydrophobia Prophecy, Zombie Apocalypse, and Payday the Heist are games that do not come with such an option. Thus, examining competing games in the same gaming genre and for the same platform, we see that some vendors do not offer an online gaming service while others do. It is not clear when offering the service is the optimal strategy for a firm, how this decision depends on the strength of network effects, and whether the number of firms that offer the service in equilibrium is socially optimal.

In this paper, we consider an industry in which competing firms sell differentiated products and each firm can offer a complementary online service to consumers that buy its product. To the best of our knowledge, while previous work identifies cases in which network effects arise due to a postpurchase service (Katz and Shapiro 1985, 1986), our paper is the first to model the service offering separately from the product offering. We examine how the fact that the online service exhibits positive network effects may change the competitive outcome and whether, despite the fact that network effects are known to intensify price competition, a firm can benefit from service-related network effects. Specifically, we address the following research questions:

(1) When does a firm choose to offer the service?

(2) Can a firm benefit from the common technological ability to offer a service that exhibits network effects, or from an exogenous increase in the strength of the network effects?

(3) Is the number of firms offering the service socially optimal?

(4) How do investments in the service’s direct value to consumers depend on the strength of the network effects and on the development costs?

Our investigation generates several interesting results. First, we find that when the service exhibits network effects, a firm’s decision whether to offer the service depends on the competitor’s decision and on the competitor’s service quality. In addition, multiple equilibria, in terms of which firms offer the service, may prevail. In contrast, when the service does not exhibit network effects, each firm bases the decision whether to offer the service only on its own service quality, and there is a unique equilibrium. Second, our analysis demonstrates the importance of the service’s direct value (value that does not depend on the network of users) to consumers. Though many services can rely on communities to create value and may have significant network effects, we show that a firm can profit from offering the service, avoid being caught in a prisoner’s dilemma, and benefit from an exogenous increase in its service’s magnitude of network effects or in the market size only when its service’s direct value is high enough. In particular, if both firms offer the service and the direct value of the two offerings is similar, then the two firms are caught in a prisoner’s dilemma as both firms would be better off when neither offers the service. A prisoner dilemma situation does not happen in the absence of network effects. Third, we find that that the number of firms providing the service in equilibrium might be larger or smaller than is socially optimal. Finally, considering investments in the service’s direct value to customers, we find that a firm’s investment level may increase in its service’s strength of network effects, demonstrating that the two sources of value (network-based value and direct value) are often not substitutable. We also show that, surprisingly, a firm’s investment in the service’s direct value and the firm’s profit may increase in its marginal development cost.

The paper structure is as follows. We start with a review of the related literature. We then present our model, derive the market equilibrium, and examine how firms’ strategies are altered when the service exhibits network effects. Next, we discuss the relationship between network effects and firms’ profitability, and examine whether the number of firms offering the service in equilibrium is socially optimal. Finally, we explore how investments in the service’s direct functionalities depend on the strength of the network effects and on the marginal development cost. We conclude with a discussion of robustness of the results to key assumptions, and a summary of contributions and direction for future research.

## Literature Review

Our study contributes to the literature on competition in the presence of network effects. In this section, we review the related literature and explain how our paper differs from previous work in both its model setup and its research focus.

The majority of the studies on competition with network goods (i.e., goods that exhibit network effects) examine product compatibility and standardization (e.g., Farrell and Saloner 1986; Katz and Shapiro 1985; Lee and Mendelson 2007) or market entry (Cabral et al. 1999; Fudenberg and Tirole 2000; Katz and Shapiro 1992). A common finding in this literature is that network effects intensify price competition (Lee and Mendelson 2007; Navon et al. 1995), and thus firms are often better off making their products compatible to lessen competition (Lee and Mendelson 2007, 2008).

Katz and Shapiro (1985, 1986) recognized the case in which positive “consumption externalities” arise for the users of a durable good not from the product itself but from a related post-purchase service. However, the models presented in these two papers are general and do not capture the unique features of this case. Katz and Shapiro (1985) model an oligopoly in which each firm sets the production level of a homogenous good with network effects. Although the homogenous good can potentially be a bundle of a product and a related service, the model does not distinguish between the product and service in any manner. Specifically, Katz and Shapiro (1985) do not model the cost of offering the service (the production cost is normalized to zero), or the value of the service. They also do not model the firm’s decision whether to offer the service or sell only a product—in which case there will be no network effects. Similarly, the two-period duopoly model in Katz and Shaprio (1986) does not separate the sources of costs and benefits to product and service. It is also important to note that although Katz and Shapiro describe the phenomenon studied in this paper (firms sell a good with no network effects but also offer a service that does exhibit network effects), they do not study questions that are specific to this phenomenon. Instead, Katz and Shapiro (1985) compare the private and the social incentives to produce compatible products, while Katz and Shapiro (1986) examining whether or not the market achieves de facto standardization.

Lee and Mendelson (2007) model the competition between two firms selling a product with network effects in a market with two consumer segments. Consumers within each segment are homogenous, but the two segments may differ in their inherent product preferences. They find that under simultaneous entry customers are better off with incompatible products, while competing firms would often be better off making their products compatible to lessen the competitive effects of a network market. Lee and Mendelson (2008) examine the competition between a commercial firm and an open source product in the software industry and reach similar results. Li and Chen (2012) use the Hotelling setup (Hotelling 1929), with two sellers exogenously located at the end points, to model employees’ choices between two products in the presence of linear network effects. They examine whether it is optimal for the employer to commit to exclusive purchase, and whether it is optimal for the sellers to cooperate and invest in compatibility.

Navon et al. (1995) uses a typical Hotelling setup to model competition between two horizontally differentiated products with network effects. They investigate the impact of the stores’ exogenous locations on equilibrium prices, profits, and welfare. They conclude that when positive network effects are present, price competition is indeed fiercer and results in lower equilibrium prices; however, both brands remain in business rather than having a tipping equilibrium provided that the misfit cost is not too low. In addition, they show that an increase in the strength of the network effects would increase the profit of the larger store (the store that has a more central location on the line) if the two stores are differentiated enough, but would always decrease the profit of the smaller store. Thus, although network effects intensify price competition, the store with the better location may benefit from an increase in the strength of the network effects.

Our paper differs from previous work on competition in the presence of network effects because we model the case in which firms sell a product that does not exhibit network effects, and may offer their customers a complementary service that does exhibit such effects. In light of previous results, according to which network effects intensify competition, it is interesting to examine when a firm chooses to offer a service that imposes network effects in a market for a product with no network effects, and whether a firm can benefit from the technological progress that enables all firms in its industry to offer such services. In contrast to prior work, our model setup distinguishes between the different sources of value and cost (product and service), which allows us to examine a different set of research questions.

Although our model setup is similar to that in Navon et al., there are several key differences. First, we model the firms’ decision to offer the component that induces network effects (i.e., the service), and find the market equilibrium in terms of which firms offer the service. This was not done in Navon et al., or in any prior paper that examines competition with network effects. As a result, when analyzing the price competition we also examine the asymmetric case in which one firm offers a product with no network effects while the other offers a bundle (product and service) that displays network effects. Second, in Navon et al., the magnitude of the network effects is homogenous across competing products. To the best of our knowledge our paper is the first to consider the case in which the competing products may exhibit different magnitudes of network effects. This generalization allows us to examine asymmetric cases and to investigate how a change in a single firm’s strength of network effects impacts profits. Third, our model considers the marginal provision cost of the service and the marginal production cost of the product, and allows the latter to differ across firms. In contrast, in Navon et al., any cost is normalized to zero. Finally, in Naovn et al., a firm’s advantageous position (in terms of its location on the line) is exogenous. In contrast, we examine the case in which the value of the service’s direct functionalities is set endogenously.

Finally, in a related paper, Pang and Etzion (2012) consider a monopoly that sells a product and can offer a complementary service with network effects to its customers. They focus on the monopoly’s bundling decision, examining when the firm should bundle the service with the product and when it should sell it separately, or not sell it at all. In contrast, our focus is the competition between firms. We consider a duopoly and, assuming that the service would be bundled with the product in case it is offered, we examine whether firms benefit from the common ability to offer the service, and how profits are affected by the strength of the network effects. Our results stand in contrast to those derived for the monopoly in Pang and Etzion. While the monopoly always benefits from stronger network effects, we show that under competition, firms’ profits often drop as network effects intensify. In addition, while a monopoly would always offer the service if the marginal provision cost of the service is low enough, we show that in a duopoly this condition is not sufficient. In fact, we find that in a duopoly, even when there is no marginal cost for offering the service, in many cases neither firm offers the service in equilibrium.

## The Model

We consider a market with two competing firms, Firm A and Firm B, selling a differentiated product. There are M consumers in the market who are heterogeneous in terms of their product preferences, and each consumer is interested in purchasing at most one unit of the product. We assume that consumers’ product preferences are uniformly distributed along a unit line (Hotelling 1929), with Firm A’s product located at 0 and Firm B’s product located at 1. When a consumer buys a product that differs from his ideal product, he incurs a misfit cost, which is increasing in the distance between his ideal product and the product he buys. Thus, a consumer located at point x on the unit line obtains utility of V – tx when purchasing the product from Firm A, and utility of $V - t ( 1 - x )$ when purchasing the product from Firm B, where V is the maximum utility from the product sold by either firm, and t is the per-unit disutility cost from the misfit between the consumer’s ideal product and the product he considers purchasing.<sup>2</sup> The firms may differ in their product’s production cost; we denote Firm i’s unit production cost by $m _ { \mathrm { i } }$ and its cost advantage over firm $j \left( \mathrm { i . e , } m _ { \mathrm { j } } – m _ { \mathrm { i } } \right)$ by $\varDelta _ { \mathrm { i } }$

Each of the two firms has the technological ability to offer a complementary online service to its customers and needs to choose whether to do so. We consider the case in which a consumer obtains positive utility from using the service offered by Firm i only when he purchases the product sold by Firm i. That is, the service offered by Firm i is not beneficial to consumers who buy a product from Firm j. Although we acknowledge that this assumption might not hold for all types of product-related online services, our paper focuses on services for which it does.

A customer’s utility from a product that displays network effects is usually modeled as a function of the product’s inherent value and of the number of customers using the product (Ellison and Fudenberg 2000). In addition, many models consider the network effects to be linear in the size of the user-base (Fudenberg and Tirole 2000; Jing 2007; Katz and Shapiro 1986; Lee and Mendelson 2007; Li and Chen 2012; Navon et al. 1995). In this paper, we adopt a similar approach and model the value a consumer obtains from the service as an additive function of the value derived from the inherent functionalities of the service (functionalities that do not rely on other users) and the value derived from the service functionalities that rely on the network of service users. Specifically, we denote the inherent or direct value of Firm i’s service by $s _ { i } ,$ and allow firms to differ in the direct benefit of their service. In addition, if the service offered by Firm i exhibits positive network effects, then a customer of Firm i obtains utility $a _ { i } N _ { i }$ where $N _ { i }$ is the network size and $a _ { i }$ is the marginal network benefit. Thus, the parameter α represents the magnitude or strength of the network effects and we allow it to differ across the two service offerings. This is a generalization of previous models on competition with network effects (e.g., Lee and Mendelson 2007; Navon et al. 1995) in which the magnitude of network effects is the same across competing products. To summarize, the utility a Firm i’s customer obtains from the service offered by Firm i is given by

$$
s _ {i} + \alpha_ {i} N _ {i}\tag{1}
$$

When considering services with network effects, a larger network of users is more valuable than a smaller network of users. Thus, vertical differentiation is naturally built into the model, and the online service offered by the two firms can be vertically differentiated due to differences in the network size, the magnitude of network effects, and the value of the direct functionalities. For example, while the service of Firm A might have a higher direct value to consumers $( \mathrm { i } . \mathrm { e } _ { \cdot } , s _ { A } > s _ { B } )$ the service of Firm B might have stronger network effects $( a _ { A } > a _ { B } )$ or a larger network of users. In addition, when firms offer a bundle of product and service, the two bundles are still horizontally differentiated; that is, consumers’ preferences are still uniformly distributed between the two offerings as described above. We acknowledge that firms may also make their service offerings horizontally differentiated in different dimensions than the spatial differentiation considered in the product space; however, this is beyond the scope of this paper.

Finally, as the number of its service users increases, a firm needs to invest in upgrading its hardware and network infrastructure. Thus, the cost of offering the service increases with the number of users. We assume that the marginal cost of offering the service, $c ,$ is the same for both firms. This assumption is reasonable as hardware, bandwidth, processors, communication technology, etc. are commodities and available to all firms for the same or similar cost. Table 1 summarizes the notation used in the paper.

The time line of the game is as follows. First, the firms simultaneously choose whether to offer the service. Four market configurations are possible as a result of this first stage of the game. In the first configuration, labeled Case NN, both firms

<table><tr><td colspan="2">Table 1. Notation</td></tr><tr><td>M</td><td>The size of the market.</td></tr><tr><td>V</td><td>The inherent value of the product</td></tr><tr><td>t</td><td>Misfit cost per unit distance between product purchased and one desired.</td></tr><tr><td> $\alpha_{i}$ </td><td>The magnitude of network effects of the service of Firm i (i = A or B).</td></tr><tr><td> $s_{i}$ </td><td>The inherent value of the service of Firm i (i = A or B).</td></tr><tr><td> $m_{i}$ </td><td>The marginal production cost of Firm i (i = A or B).</td></tr><tr><td> $\Delta_{i}$ </td><td>Firm i&#x27;s cost advantage over firm j (i.e.,  $m_{j}-m_{i}$ )</td></tr><tr><td>c</td><td>The marginal cost for providing the service.</td></tr><tr><td> $p_{k}^{i}$ </td><td>The price of the product sold by Firm i when the firms choices regarding service provision are given by k, where k ∈ {NN, SN, NS,SS}.</td></tr><tr><td> $D_{k}^{i}$ </td><td>The demand for the product of Firm i when the choices regarding service provision are given by k.</td></tr><tr><td> $\pi_{k}^{i}$ </td><td>The profit of Firm i when choices regarding service provision are k.</td></tr></table>

Stage 1. The firms simultaneously decide whether to offer the service.

Stage 2. The firms observe the result of first stage of the game and set prices.

![](/api/attachments/RG3HSFC8/fulltext/images/19548873bcbfe5210f966a58658e413892a45f6ae32c8ae4fc8031e2f4407391.jpg)

sell only the product. In the second configuration, Case SN, and the third, Case NS, only Firm A or only Firm B, respectively, offer the service while the other firm sells only the product. Finally, in the fourth configuration, Case SS, both firms offer the service. Next, after observing the choices made in the first stage (firms make their service offerings public), the two firms simultaneously set their prices. Although firms offer the service “free of charge” to consumers buying their product, the price of the product clearly depends on whether the service is offered or not. Finally, in the third stage of the game, consumers observe the firms offerings and choose whether to buy a product and from which firm; decisions in this stage are made based on expected network sizes and prices. Figure 1 describes the time line of the game.

It is important to note that in the analysis we consider only parameter values for which in equilibrium (1) each firm has positive demand for its product, and (2) the market is covered.<sup>3</sup> We believe that such cases are of the highest interest as they represent real competition between the two firms. First, if only one firm has positive demand, then the other firm is in fact inactive. Although such a tipping equilibrium in which everyone buys the same product is likely to prevail in network markets for a homogenous good, this would not be the equilibrium outcome as long as the products are sufficiently differentiated (Li and Chen 2012; Navon et al. 1995). Second, if the market was not covered, then each firm would behave as a local monopoly and thus there would effectively be no competition. In this case, each firm would offer a bundle of product and service as long as the marginal cost of offering the service is low enough (Pang and Etzion 2012), and each firm’s profit would increase in the strength of the network effects.

## The Service Offering Decision

In this section, we derive under which conditions each firm would offer the service and compare the results when the service exhibits network effects with when it does not. We then examine the minimum level of direct value required for a service to be offered by a firm, and determine how this threshold level depends on the magnitude of network effects.

Table 2. The Equilibrium Prices for the Four Possible Market Configurations

<table><tr><td>Firm B Firm A</td><td>Only Product</td><td>Product + Service</td></tr><tr><td>Only Product</td><td> $p_{NN}^{A} = t + \frac{(2m_{A}+m_{b})}{3}$  $p_{NN}^{B} = t + \frac{(m_{A}+2m_{B})}{3}$ </td><td> $p_{NS}^{A} = \frac{3t+c-2\alpha_{B}M-s_{B}+2m_{A}+m_{B}}{3}$  $p_{NS}^{B} = \frac{3t+2c-\alpha_{B}M+s_{B}+2m_{B}+m_{A}}{3}$ </td></tr><tr><td>Product + Service</td><td> $p_{SN}^{A} = \frac{3t+2c-\alpha_{A}M+s_{A}+2m_{A}+m_{B}}{3}$  $p_{SN}^{B} = \frac{3t+2c-\alpha_{A}M-s_{A}+2m_{B}+m_{A}}{3}$ </td><td> $p_{SS}^{A} = \frac{3t-M(\alpha_{A}+2\alpha_{B})+s_{A}-s_{B}+3c+2m_{A}+m_{B}}{3}$  $p_{SS}^{A} = \frac{3t-M(2\alpha_{A}+\alpha_{B})+s_{B}-s_{A}+3c+2m_{B}+m_{A}}{3}$ </td></tr></table>

## Table 3. The Equilibrium Profits for the Four Possible Market Configurations

<table><tr><td>Firm A Firm B</td><td>Only Product</td><td>Product + Service</td></tr><tr><td>Only Product</td><td> $\pi_{NN}^{A} = \frac{M(3t+\Delta_{A})^{2}}{18t}$  $\pi_{NN}^{B} = \frac{M(3t+\Delta_{B})^{2}}{18t}$ </td><td> $\pi_{NS}^{A} = \frac{M(3t+c-2\alpha_{B}M-s_{B}+\Delta_{A})^{2}}{9(2t-\alpha_{B}N)}$  $\pi_{SS}^{B} = \frac{M(3t-c-\alpha_{B}M+s_{B}+\Delta_{B})^{2}}{9(2t-\alpha_{B}N)}$ </td></tr><tr><td>Product + Service</td><td> $\pi_{SN}^{A} = \frac{M(3t-c-\alpha_{A}M+s_{A}+\Delta_{A})^{2}}{9(2t-\alpha_{A}M)}$  $\pi_{SN}^{B} = \frac{M(3t+c-2\alpha_{A}M-s_{A}+\Delta_{B})^{2}}{9(2t-\alpha_{A}M)}$ </td><td> $\pi_{SS}^{A} = \frac{M(3t-M(\alpha_{A}+2\alpha_{B})+s_{A}-s_{B}+\Delta_{A})^{2}}{9(2t-M(\alpha_{A}+\alpha_{B}))}$  $\pi_{SS}^{B} = \frac{M(3t-M(\alpha_{B}+2\alpha_{A})+s_{B}-s_{A}+\Delta_{B})^{2}}{9(2t-M(\alpha_{A}+\alpha_{B}))}$ </td></tr></table>

To find the sub-perfect market equilibrium, we solved the above three-stages game backward. First, for each of the four possible subgames (SS, SN, NS, and NN), we derived each firm’s demand as a function of prices. Here, we used the concept of fulfilled expectation equilibrium in which the realized demand equals the expected network size (Katz and Shapiro 1985; Palma et al. 1999; Sundararajan 2003). Next, for each of the four subgames, given the derived demand functions, we find the Nash equilibrium in prices and the resulting profits as given in Tables 2 and 3 respectively. The detailed derivations of the equilibrium for the third and second stages of the game in the manner described here are provided in Appendix A. Finally, we solved the $2 \times 2$ payoff matrix given in Table 3 to determine the sub-perfect Nash equilibrium in the first stage of the game as specified in Proposition 1.

## Proposition 1. (Market Equilibrium)

i) Both firms offer the service. Case SS is an equilibrium iff (i.e., if and only if) $s _ { A } > X _ { A } s _ { B } + Y _ { A }$ and $s _ { B } > X _ { B } s _ { A } + Y _ { B } .$

ii) Both firms offer only product. Case NN is an equilibrium iff $s _ { A } < s _ { A }$ and $s _ { B } < s _ { B } .$

iii) Only firm A offers a service. Case SN is an equilibrium iff $s _ { A } > s _ { A }$ and $s _ { B } < X _ { B } s _ { A } + Y _ { B } .$

iv) Only firm B offers a service. Case NS is an equilibrium iff $s _ { B } > s _ { B }$ and $s _ { { \scriptscriptstyle A } } < X _ { { \scriptscriptstyle A } } s _ { { \scriptscriptstyle B } } + Y _ { { \scriptscriptstyle A } } .$

Where

$$
X _ {i} = 1 \frac {\sqrt {2 t - M (\alpha_ {A} + \alpha_ {B})}}{\sqrt {2 t - \alpha_ {j} M}},
$$

$$
\begin{array}{c} Y _ {i} = \frac {(3 t - 2 \alpha_ {j} M + c - \Delta_ {i}) \sqrt {2 t - M (\alpha_ {A} + \alpha_ {B})}}{\sqrt {2 t - \alpha_ {j} M}} \\ - (3 t - M (\alpha_ {A} + \alpha_ {B} + \alpha_ {j}) + \Delta_ {i}), \end{array}
$$

$$
\begin{array}{c} \overline {{s}} _ {i} = \frac {(3 t + \Delta_ {i}) \sqrt {2 (2 t - \alpha_ {i} M)}}{2 \sqrt {t}} \\ - 3 t + \alpha_ {i} M + c - \Delta_ {i} (i, j = A o r B, i \neq j). \end{array}
$$

Proofs of all propositions are given in Appendix B.

Figure 2 exhibits the resulting market equilibrium in the $s _ { A } - s _ { B }$ space when $a _ { \scriptscriptstyle A } = a _ { \scriptscriptstyle B } > 0$ and $m _ { \mathrm { A } } { } ^ { = } m _ { \mathrm { B } }$ The lines d-e-f and g-e-h in Figure 2 indicate $s _ { { \scriptscriptstyle A } } = X _ { { \scriptscriptstyle A } } s _ { { \scriptscriptstyle B } } + Y _ { { \scriptscriptstyle A } }$ and $s _ { B } = X _ { B } s _ { A } + Y _ { B } ,$ respectively. In the region northeast of $f \mathrm { - } e \mathrm { - } h ,$ the inherent value of both online services $( s _ { A }$ and $s _ { B } )$ is sufficiently high that both firms operate the service in equilibrium. On the other hand, in the region $0 \cdot a \cdot b \cdot c .$ , both $s _ { A }$ and $s _ { B }$ are low (Proposition 1-(ii)), and thus neither firm offers the service. Southeast of the lines $c { - } b { - } g { - } e { - } h ,$ , the conditions from Proposition 1-(iii) hold and, therefore, there is an equilibrium in which only Firm A offers the service. Similarly, northwest of the lines $a { - } b { - } d { - } e { - } f ,$ there is an equilibrium in which only Firm B offers the service.

## Multiple Equilibria

We find that when both firms can offer a service that exhibits network effects, for a subset of the parameter values (in region $_ { b - d - e - g }$ in Figure 2), two equilibria are feasible: an equilibrium in which only Firm A offers the service and an equilibrium in which only Firm B offers the service. In this range of parameter values, each firm finds it optimal to offer the service only when the competitor is not doing so. As a result, equilibrium in which the firm with the lower quality of service (in terms of s $\operatorname { o r } \alpha _ { i } )$ offers the service, while the firm with the higher quality does not, may prevail. It is important to distinguish this multiple-equilibria result from the already known finding that in network markets multiple fulfilled expectations equilibria can emerge. The latter result is in regard to the consumers’ adoption decision showing that, given different consumer expectations, different equilibria can prevail in terms of which product consumers adopt (Katz and Shapiro 1985, 1986). In contrast, we show that there can be multiple equilibria in terms of which firm would offer the service.

While multiple equilibria can prevail when the two service offerings exhibit network effects, if at least one of the service offerings does not exhibit network effects, then only one equilibrium in terms of which of the two firms offer the service may prevail. When Firm i’s service does not exhibit network effects $( { a } _ { i } = 0 )$ , the expressions in Proposition 1 reduce to $\bar { s _ { i } } = c , X _ { i } = 0 .$ , and $Y _ { i } = c$ . Thus, Firm $i ^ { \circ } \mathrm { s }$ decision whether to offer the service or not becomes independent of the competitor’s decision and its service quality; instead it depends only on whether the value a consumer derives from Firm $i ^ { \circ } \mathrm { s }$ service (s<sub>i</sub>) exceeds the marginal service provision cost (c). This situation is exhibited in Figure 3, where $\mathfrak { a } _ { A } >$ 0 but $\boldsymbol { a } _ { B } \boldsymbol { = } 0$ , and is summarized in Corollary 1.

Corollary 1. When the service of Firm i does not exhibit network effects, Firm i offers the service if and only $i f s _ { i } > c$

The strategic implications of Proposition 1 and Corollary 1 are significant. If a firm’s service exhibits network effects, then the firm has to take into consideration the competitor’s service quality when determining whether to offer its service. This is not the case when the firm’s service does not exhibit network effects. The rational for the difference in results is as follows: When the service of Firm i exhibits network effects, the value a consumer derives from it depends on the number of other users, which in turn depends on whether the competing firm, Firm j, offers a service. Specifically, when the competing firm offers the service, Firm i’s network of service users is likely to be smaller than when the competing firm does not offer the service. In addition, as the competing firm’s service quality increases, the resulting network of Firm i would be smaller. Thus, whether the competitor offers a service and its service quality affect the value a consumer would derive from Firm i’s service, and thus may affect Firm $i ^ { \circ } \mathrm { s }$ decision whether to offer the service. This is not true when the service of Firm i does not exhibit network effects because then the value a consumer derives from it is $S _ { \mathrm { i } }$ regardless of the actions of Firm j.

## The Strength of Network Effects and the Offering Decision

Here we examine when the service would be offered in terms of the relationship between the service’s direct value (s ) and the strength of network effects $( a _ { i } )$ by examining how the thresholds for $S _ { \mathrm { i } }$ given in Proposition 1 $( \bar { s _ { i } }$ and $X _ { i } s _ { j } + Y _ { i } )$ change with $\alpha _ { i } .$ Taking derivatives of the expressions from Proposition 1, we find that the minimum value of ${ \bf \dot { \sigma } } _ { S _ { i } }$ at which Firm i would offer the service is first increasing in the service’s strength of network effects, and then decreasing in it. Specifically,

$$
\frac {\partial}{\partial \alpha_ {i}} \overline {{s}} _ {i} > 0 \mathrm{iff} \alpha_ {i} <   7 t / 8 M\tag{2}
$$

![](/api/attachments/RG3HSFC8/fulltext/images/9645d2aa42ec328d705574af5128d0ba93b461fdbb94764ee5057601c79c8e29.jpg)  
Figure 2. The Market Equilibrium in the $\odot$ Space for $\mathbf { z }$

![](/api/attachments/RG3HSFC8/fulltext/images/ecfb7b51e0346fb9a10d6cdbbcf448a4555e0a5721df3251f11805302e8490d0.jpg)  
Figure 3. The Market Equilibrium in the $\odot$ Space for α<sub>A</sub> > 0, α<sub>B</sub> = 0

Table 4. The Equilibrium Prices for the Four Possible Market Configurations

<table><tr><td>Firm A Firm B</td><td>Only Product</td><td>Product + Service</td><td rowspan="3">M = 200, v = 50t = 5, c = 3α = 0.015sA= 450, sB= 350mA=mB= 1</td></tr><tr><td>Only Product</td><td>500, 500</td><td>145, 645</td></tr><tr><td>Product + Service</td><td>788, 88</td><td>312, 112</td></tr></table>

$$
\begin{array}{l} \frac {\partial}{\partial \alpha_ {i}} (s _ {j} X _ {i} + Y _ {i}) > 0 \text {   iff   } \\ \alpha_ {i} <   \frac {(s _ {j} + t - c - \Delta_ {i}) (7 t - 4 \alpha_ {j} M - s _ {j} + c + \Delta_ {i})}{4 M (2 t - \alpha_ {j} M)} \end{array}\tag{3}
$$

We thus conclude that a firm should be cautious when the magnitude of network effects of its service intensifies. Surprisingly, such an exogenous change in the magnitude of network effects (perhaps due to consumers’ changing perceptions or needs), might make offering the service an unprofitable strategy. The firm might need to reinvest in improving its service’s direct functionalities, increasing its direct value to consumers, for offering the service to remain a profitable strategy. In contrast, in a monopoly setup, stronger network effects can only make the firm more likely to offer the service (Pang and Etzion 2012).

An increase in the magnitude of the network effects of a firm’s service increases the firm’s market share, but also intensifies the price competition. If the initial strength of network effects is not sufficiently high or the change is not large enough, the negative impact of the intensified price competition dominates, and thus the threshold level of direct functionalities at which the firm should offer the service increases. In contrast, when the strength of network effects is sufficiently high, further increases in it would expand the firm’s market share to such a degree that it would not only compensate for the lower price but would reduce the minimum level of direct value required so that offering the service would be profitable.

## Network Effects and Profitability

Given that the literature shows that network effects intensify price competition (e.g., Lee and Mendelson 2007; Navon et al. 1995), it is not clear whether firms benefit from the technological progress that enables them to offer services with network effects or from an increase in the magnitude of network effects. We address these questions next.

## Prisoner’s Dilemma

As expected, because of the intensified price competition, in many cases both firms are worse off due to the common technological progress that enables them to offer a service with network effects. Table 4, which lists the equilibrium profits for the four different market configurations, provides a numerical example in which this is so. Specifically, offering the service maximizes a firm’s profit regardless of the strategy chosen by the competing firm, and a prisoner’s dilemma prevails because the two firms’ profits in equilibrium $( \pi _ { S S } ^ { 4 } = 3 1 2 , \pi _ { S S } ^ { B } = 1 1 2 )$ are less than the profits when neither firm offers the service $( \pi _ { N N } ^ { A } = \pi _ { N N } ^ { B } = 5 0 0 )$ . Proposition 2 describes under which conditions a firm’s profit is lower when both firms offer the service than when neither does.

Proposition 2. (Prisoner’s Dilemma condition) When both firms offer the service, Firm i would be better off when neither offers it if and only if

$$
\begin{array}{r l} s _ {i} - s _ {j} <   M \left(\alpha_ {i} + 2 \alpha_ {j}\right) - 3 t - \Delta_ {i} + & \frac {\left(3 t + \Delta_ {i}\right) \sqrt {\left(2 t - M \left(\alpha_ {i} + \alpha_ {l}\right)\right)}}{\sqrt {2 t}} \\ i = \{A, B \} \text { and } j \neq i \end{array}\tag{4}
$$

According to Proposition $^ { 2 , }$ if both firms offer the service in equilibrium, then as long as neither firm has a significant advantage in the value consumers obtain from its service’s direct functionalities (i.e., as long as $\lvert s _ { i } - s _ { j } \rvert$ is small enough), both firms would be better off when neither offers the service. The firms are caught in a prisoner’s dilemma and the reduction in profits (compared to profits when neither firm offers the service) is caused by intensified price competition. However, if one firm has a significant advantage over the other $( \mathrm { i } . \mathsf { e } _ { . , s _ { i } }$ is large enough compared to s ), then that firm is better off when both firms offer the service than when neither does. Finally, when there are no network effects (i.e., when $a _ { i } = a _ { j } = 0 )$ , the right-hand side of Equation 4 becomes zero, and the firm that has the higher (lower) level of direct functionalities is always better off (worse off) when both offer the service compared to when neither does. Therefore, a prisoner’s dilemma does not occur when the service does not exhibit network effects.

## Network Effects and Profit

Here we examine whether a firm can benefit from an increase in the strength of network effects exhibited by its service, or from an increase in the market size M. At first look, either of these exogenous changes would lead to higher service valuation by the firm’s customers and thus potentially lead to higher gains for the firm. However, these changes also intensify price competition and thus it is not clear in advance whether the firm can benefit from them.

## Network Effects and Profits

From Table 2 we see that when both firms offer the service their prices decrease as the magnitude of network effects of either firm increases. We also see that the cross-effect is stronger; that is, Firm j’s price is more sensitive than Firm $i ^ { \circ } \mathrm { s }$ price to changes in $\boldsymbol { a } _ { i \cdot }$ In addition, when $a _ { i }$ increases, the market share of Firm i increases and that of Firm j decreases if and only if $s _ { i } - s _ { j } + t - M a _ { i } + \Delta _ { \mathrm { i } } > 0 ;$ the opposite holds otherwise. Thus, an increase in a firm’s strength of network effects does not necessarily increase its market share. If only Firm i offers the service, then again both firms have price decreases in the magnitude of network effects, with the cross effect being stronger. However, in this case, when the magnitude of network effects of Firm i’s service increases, its market share increases while its competitor’s share decreases. We conclude that although equilibrium prices decrease due to an increase in the magnitude of network effects, one of the firms would gain market share, which might lead to a higher profit. Proposition 3 describes the combined impact an exogenous change in the strength of network effects has on profits.

## Proposition 3. (Strength of network effects and profits)

i) If both firms offer the service in equilibrium, as $a _ { i }$ increases, Firm j’s profit always decreases while Firm i’s profit increases if and only if

$$
s _ {i} > s _ {j} + t - \alpha_ {i} M - \Delta_ {\mathrm{i}}\tag{5}
$$

ii) When only Firm i offers the service in equilibrium, as $a _ { i }$ increases, Firm j’s profit always decreases while Firm i’s profit increases if and only if

$$
s _ {i} > c + t - \alpha_ {i} M - \Delta_ {\mathrm{i}}\tag{6}
$$

iii) If both firms offer the service in equilibrium and $a _ { i } = a _ { j }$ $= a ,$ a common increase in the degree of network effects decreases both firms’ profits.

According to Proposition 3, a firm may benefit from an exogenous increase in the magnitude of network effects of its service, despite the intensification of price competition, if the value of the direct functionalities of its service is higher than a given threshold. The threshold value decreases in the firm’s cost advantage over the competitor $( \Delta _ { \mathrm { i } } )$ and in the firms magnitude of network effects. Thus, when both firms offer the service, even the firm with the lower direct value may benefit from an increase in its service’s strength of network effects; this happens if its marginal production cost is sufficiently lower than the competitor’s cost.

Finally, if both service offerings exhibit the same strength of network effects, a common increase in the strength of network effects due to an exogenous change would decrease both firms’ profits regardless of the levels of their service’s direct functionalities. This result contrasts with the result reported in Navon et al. (1995), according to which the firm with the better location may benefit from a common increase in the homogenous degree of network effects.

## Market Size and Profits

Proposition 4 describes how a firm’s profit changes due to an increase in market size, M.

## Proposition 4. (Market size and profits)

i) If both firms offer the service in equilibrium, then the profit of Firm i increases in the size of the market (M) if and only if

$$
\begin{array}{l} s _ {i} > s _ {j} + 6 M \alpha_ {j} + 3 M \alpha_ {i} \\ - 3 t - \frac {M ^ {2} (\alpha_ {i} + \alpha_ {j}) (\alpha_ {i} + 2 \alpha_ {j})}{t} - \Delta_ {i} \end{array}\tag{7}
$$

ii) If only Firm i offers the service, then Firm i’s profit increases in the size of the market (M) if and only if

$$
\begin{array}{c} s _ {i} > c + 3 M \alpha_ {i} - 3 t - \frac {\alpha_ {i} ^ {2} M ^ {2}}{t} - \Delta_ {i} \\ (i = A o r B) \end{array}\tag{8}
$$

It is easy to show that if the service does not exhibit network effects, the equilibrium prices and market shares are independent of the market size, M, and both profits increase in M due to an increase in the demand. In contrast, as stated in Proposition $^ { 4 , }$ when the service exhibits network effects, the equilibrium profits do not necessarily rise as the market size increases. When the service exhibits network effects, a firm can benefit from an increase in the market size only if the direct value users obtain from its service (s ) is high enough. In some cases, both profits will drop due to an increase in market size, while in other cases (depending on parameter values) one firm or even both will benefit from an increase in market size.

## Social Welfare

In this section, we examine whether the number of firms offering the service in equilibrium is socially optimal. In what follows, we state that the service is under-provided (over-provided) if the number of firms offering the service in equilibrium is smaller (larger) than the socially optimal number. Proposition 5 lists the conditions under which the service is under-provided or over-provided in the market when firms incur the same marginal production cost.

Proposition 5. (Social inefficiencies when $m _ { A } = m _ { B } )$

i) The service is under-provided iff $F ^ { A } ( s _ { A } , s _ { B } )$ and $F ^ { B } ( s _ { B } , s _ { A } )$ $> 0 .$ , and at least one of the following conditions hold:

$$
\begin{array}{l} \frac {2 c - \alpha_ {A} N}{2} <   s _ {A} <   s _ {B} X _ {A} + Y _ {A} \quad o r \\ \frac {2 c - \alpha_ {B} N}{2} <   s _ {B} <   s _ {A} X _ {B} + Y _ {B} \end{array}
$$

ii) The service is over-provided $i f f s _ { { \cal A } } > s _ { { \cal B } } X _ { { \cal A } } + Y _ { { \cal A } } , s _ { { \cal B } } > s _ { { \cal A } } X _ { { \cal B } }$ $+ \ Y _ { B } ,$ and at least one of the following conditions hold:

$$
F ^ {A} (s _ {A}, s _ {B}) <   0, o r F ^ {B} (s _ {B}, s _ {A}) <   0
$$

where

$$
\begin{array}{l}F ^ {i} \left(s _ {i}, s _ {j}\right) = S W _ {S S} - S W _ {i} =\\\frac {M}{9} \left(7 s _ {i} + s _ {j} M \left(5 \alpha_ {i} + \alpha_ {i}\right) + \frac {t \left(t - \alpha_ {i} M + s _ {j} - s _ {i}\right) ^ {2}}{\left(2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)\right) ^ {2}} + \right.\\\frac {\left(4 t - 5 \alpha_ {i} M + s _ {i} - 2 s _ {j}\right) \left(t - \alpha_ {i} M + s _ {i} - s _ {j}\right)}{2 t - m \left(\alpha_ {i} + \alpha_ {j}\right)} +\\\frac {\left(2 \alpha_ {i} M \left(c ^ {2} (2 t + s _ {i}) (t + s _ {i}) + c (1 3 t - 2 s _ {i})\right) - 8 \alpha_ {i} ^ {2} c M ^ {2} - t (9 t ^ {2} + 2 t (9 c + 7 s _ {i}) + 5 (s _ {i} - c) ^ {2})\right)}{(2 t - \alpha_ {i} M) ^ {2}}\left. \right)\end{array}
$$

$S W _ { s s }$ is social welfare when both firms offer service, and $S W _ { i }$ is social welfare when only Firm i offers the service.

Figure 4 displays the results from Proposition 5 when $2 c <$ $a _ { i } M$ for $i = A , B .$ . It shows which market configuration maximizes social welfare and when the service is under or over provided. If $2 c > a _ { i } M ,$ the only change to Figure 4 would be the addition of a range of $s _ { i } - s _ { j }$ values in which it is socially optimal that Firm i does not offer the service and in equilibrium indeed it does not offer it.

In the region labeled by A in Figure 4, $F ^ { A } ( s _ { A } , s _ { B } ) < 0 .$ and social welfare is maximized when only Firm A offers the service; in the region labeled $B , F ^ { B } ( s _ { B } , s _ { A } ) < 0$ , and social welfare is maximized when only Firm B offers the service; and in all the regions labeled $A + B ,$ social welfare is maximized when both firms offer the service. Thus, considering the equilibrium result reported in Figure 2, in Regions A and B we observe over-provision of the service (the two firms offer service in equilibrium while it is socially optimal that only one firm would), while when $s _ { { \scriptscriptstyle A } } < X _ { { \scriptscriptstyle A } } s _ { { \scriptscriptstyle B } } + Y _ { { \scriptscriptstyle A } } \mathrm { o r } s _ { { \scriptscriptstyle B } } < X _ { b } s _ { { \scriptscriptstyle A } } + Y _ { B } ,$ we observe under-provision (at most one firm offers the service while it is socially optimal that both would).

It is interesting that when both service offerings have a high direct value to consumers, we observe over-provision of the service. The reason is again network effects. Specifically, in regions A and B, both firms offer the service in equilibrium but price competition reduces the firms’ profits compared to the case in which only one firm offers the service. Price competition raises consumer surplus but the reduction in profits outweighs the increase in consumer surplus.

Although we examine whether the number of firms offering the service in equilibrium is socially optimal and not whether the number of service users is socially optimal, the two are closely related. First, if two firms offer the service while it is socially optimal that only one firm offers it, then the total number of service users in equilibrium, which is M given that the market is covered, is larger than is socially optimal. Second, if only one firm offers the service but it would be socially optimal for both to offer it, then in equilibrium less than M consumers use the service, while it would be socially optimal if all M would (although the M consumers would be divided between the two firms). To summarize, when we find that the number of firms providing the service in equilibrium is larger (smaller) than is socially optimal, necessarily the number of consumers using the service is also larger (smaller) than is socially optimal. We conclude that, supporting previous results regarding under-provision of products with network effects in a monopoly setup ( Katz and Shapiro 1994; Pang and Etzion 2012; Sundararajan 2004), under-provision of the service may prevail in a competitive setting. However, unlike in a monopoly setup, the service might also be overprovided. This can happen, surprisingly, when the inherent values of both service offerings $( s _ { A }$ and $s _ { B } )$ are high.

![](/api/attachments/RG3HSFC8/fulltext/images/9398091cd09aa08239bcf07bd4068a05d34c1c81482db4bdcf81e85058e22f06.jpg)  
Note: In the range labeled A (B), social welfare is maximized when only Firm A (B) offers service. In the ranges labeled $A + B ,$ social welfare is maximized when both firms offer the service

Figure 4. The Market Configuration that Maximizes Social Welfare, and the Type of Market Inefficiency

## Investments in Direct Functionalites

We show above that whether a firm can benefit from the technological progress that enables firms to offer a service with network effects, whether its profit increases in its service’s strength of network effects and in the market size, and whether it should offer the service depend heavily on the direct value users derive from its service. Thus, this section extends our base model so that each firm can endogenously set the direct value customers would obtain from its service by choosing how much to invest when developing the service. We then examine how the chosen level of direct functionalities depends on the magnitude of network effects and on the development cost.

The game described earlier is modified as follows: In the first stage of the game, each firm decides how much to invest in developing its service and as a result determines the direct value to consumers. The development cost, $C ( s _ { i } ) ,$ is assumed to be an increasing and convex function of $s _ { i } ,$ and for the analysis we set $C ( s _ { i } ) = c _ { i } s _ { i } ^ { 2 }$ where $c _ { i }$ indicates the development capability of Firm i. Firms can differ in their marginal development cost as some have an internal department of developers while others outsource the work, and even if both develop the service internally (or both outsource it) they may incur different cost structures. The firm with the lower $c _ { i }$ has the cost advantage. In the second stage, $s _ { A }$ and $s _ { B }$ are observed and both firms simultaneously decide whether to offer the service to consumers who buy their product. Prices are set in the third stage, and in the last stage of the game, consumers choose whether to buy a product and from which firm. For a given result of the first stage (i.e., for given values of ${ \dot { s } } _ { A }$ and $s _ { B } )$ , the following three stages are the same as the game described earlier. Thus, for each $( s _ { A } , s _ { B } )$ pair that can be chosen in the first stage of the game described here, the equilibrium is determined by Proposition 1, and the profit of Firm i is

$$
\pi^ {i} (s _ {A}, s _ {B}) = G ^ {i} (s _ {A}, s _ {B}) - c _ {i} s _ {i} ^ {2}\tag{9}
$$

where

$$
G ^ {i} (s _ {_ A}, s _ {_ B}) = \left\{ \begin{array}{l l} \pi_ {_ {S N}} ^ {^ {i}} (s _ {_ A}, s _ {_ B}) & \text { if   both   choose   to   offer   the   service   in   the } 2 ^ {^ {n d}} \text { stage } \\ \pi_ {_ {N S}} ^ {^ {i}} (s _ {_ A}, s _ {_ B}) & \text { if   only   A   chooses   to   offer   the   service   in   the } 2 ^ {^ {n d}} \text { stage } \\ \pi_ {_ {N N}} ^ {^ {i}} (s _ {_ A}, s _ {_ B}) & \text { if   only   B   chooses   to   offer   the   service   in   the } 2 ^ {^ {n d}} \text { stage } \\ & \text { if   neither   chooses   to   offer   the   service   in   the } 2 ^ {^ {n d}} \text { stage } \end{array} \right.
$$

The expressions for $\pi _ { k } ^ { i }$ are given in Table 3.

In general, a firm might invest in developing the service in the first stage, incurring the fixed development cost, but after observing the competitor’s service quality in the second stage, it might decide not to offer the service. This is because in the second stage any development cost is sunk and the firm might expect a higher profit when not offering the service. However, this situation would not happen on the equilibrium path. Finally, in this section we focus on the firms marginal development costs, and thus we consider only the case in which the two firms have the same marginal production cost for the product $( \mathrm { i . e . , } m _ { \mathrm { A } } = m _ { \mathrm { B } } )$ . This assumption is often used in the literature (e.g., Lee and Mendelson 2007; Navon et al. 1995), and fits well when the product is an information good such as prepackaged software or a video game.

Table 5 displays the firms’ equilibrium investment choices, in terms of the value customers would obtain from the direct functionalities of the service, for each possible market configuration (NN, SN, NS, and SS). For example, Firm A sets $\begin{array} { r } { s _ { \scriptscriptstyle A } = \frac { M \left( 3 t - \alpha _ { \scriptscriptstyle A } M - c \right) } { 9 c _ { \scriptscriptstyle A } \left( 2 t - \alpha _ { \scriptscriptstyle A } M \right) - M } } \end{array}$ if it expects that Firm B will not offer the the service. The resulting matrix of profits, Table 6, was obtained by substituting the values of $\dot { s } _ { A }$ and $s _ { B }$ from Table 5 in the relevant profit expressions from Table 3 and subtracting the development cost.

With the payoff matrix of profits given in Table 6, we can numerically determine the market equilibrium, if such exists,<sup>4</sup> for any set of parameter values $( M , c , t , a _ { A } , a _ { B } , c _ { A } ,$ , and $c _ { B } )$ We do not derive an equivalent proposition to Proposition 1 as the inequalities would be too complex. Next, we examine how the equilibrium levels of direct values and the firms profits depend on the strength of network effects for a given market configuration. The results are given in Propositions 6 and 7 respectively, where we refer to the service’s direct value as the service’s quality.

Proposition 6. (network effects and the endogenous service quality)

i) If only Firm i offers the service, then the equilibrium level of its service quality (s ) increases in the magnitude of network effects (α<sub>i</sub>) iff c < t or c > t and $\begin{array} { r } { c _ { i } < \frac { M } { 9 \left( c - t \right) } } \end{array}$

ii) If both firms offer the service, the equilibrium level of Firm i’s service quality (s<sub>i</sub>):

a. Increases in its own magnitude of network effects $\begin{array} { r } { ( \alpha _ { i } ) i f f c _ { i } < \frac { c _ { j } M } { 2 M - 9 c _ { j } \left( t - \alpha _ { j } M \right) } . } \end{array}$

b. Increases in the competitors’ magnitude of network effects (α<sub>j</sub>) if and only $\begin{array} { r } { i f c _ { i } < \frac { 2 c _ { j } M } { M + 9 c _ { j } \left( t - \alpha _ { i } M \right) } \ ( i , j = A } \end{array}$ and $B , i \neq j )$

iii) If both firms offer the service and $a _ { i } = a _ { i } = a ,$ Firm i’s service quality increases in α if and only $ i f c _ { i } < c _ { j } ( i , j =$ A and B, i  j).

From Proposition 6, we learn that a firm that expects to be the only one providing the service and has a relatively low marginal provision cost $( \mathrm { i } . \mathrm { e } . , c < t )$ would invest more in its service’s direct functionalities when network effects are stronger. Even if the marginal service provision cost is high, the investment level increases in the strength of network effects as long as the marginal development cost is not too high (or alternatively the market size, M, is large enough). This indicates that the two types of functionalities (networkbased and direct) are often complementary rather than substitutes, and in markets with stronger network effects we should often expect to see higher levels of direct functionalities as well.

If Firm i expects the competitor to also provide the service, stronger network effects would lead to a higher service quality only when Firm i’s marginal development cost (c ) is sufficiently low, and the upper bound (for c ) is an increasing function of the competitor’s development cost, ${ c _ { \mathrm { j } } } ^ { 5 }$ Therefore, if the competitor’s marginal cost (c ) is low but $c _ { \mathrm { i } }$ is high, Firm i’s chosen level of service quality (s ) decreases in its own service’s strength of network effects. We conclude that when a firm has a development cost disadvantage, the two functionalities may become substitutable. Especially, when the magnitude of network effects is homogenous across products, the service quality of the firm with the lower (higher) marginal development cost increases (decreases) in the strength of the network effects. Next, Proposition 7 describes how profits change with the strength of network effects under endogenous service quality.

Proposition 7. (Network effects and profits under endogenous quality)

i) If only Firm i offers the service, its profit is decreasing in $a _ { i }$ if and only if

$$
\alpha_ {i} <   \frac {c + t}{M} - \frac {2}{9 c _ {i}} (i = A o r B).
$$

Table 5. The Equilibrium Service’s Direct Value for the Four Market Configurations

<table><tr><td>Firm A Firm B</td><td>Only Product</td><td>Product + Service</td></tr><tr><td>Only Product</td><td>N/A</td><td> $S_B = \frac{M(3t - \alpha_B M - c)}{9c_A(2t - \alpha_B M) - M}$ </td></tr><tr><td>Product + Service</td><td> $S_A = \frac{M(3t - \alpha_A M - c)}{9c_A(2t - \alpha_A M) - M}$ </td><td> $S_A = \frac{M(M - 9c_B t + c_B M(3\alpha_A + 6\alpha_B))}{3M(c_A + c_B) - 27c_A c_B(2t - M(\alpha_B + \alpha_A))}$  $S_B = \frac{M(M - 9c_A t + c_A M(6\alpha_A + 3\alpha_B))}{3M(c_A + c_B) - 27c_A c_B(2t - M(\alpha_B + \alpha_A))}$ </td></tr></table>

## Table 6. The Equilibrium Profits When the Service’s Direct Value is Endogenous

<table><tr><td>Firm A Firm B</td><td>Only Product</td><td>Product + Service</td></tr><tr><td>Only Product</td><td> $\pi_{NN}^{A} = 0.5Mt$  $\pi_{NN}^{B} = 0.5Mt$ </td><td> $\pi_{NS}^{A} = \frac{M(2t-\alpha_{B}M)(3c_{A}(3t-2\alpha_{B}M+c)-M)^{2}}{(9c_{B}(2t-\alpha_{B}M)-M)^{2}}$  $\pi_{NS}^{B} = \frac{9c_{B}^{2}M(2t-\alpha_{B}M)(3t-\alpha_{B}M-c)^{2}}{(9c_{B}(2t-\alpha_{B}M)-M)^{2}}$ </td></tr><tr><td>Product + Service</td><td> $\pi_{SN}^{A} = \frac{9c_{A}^{2}M(2t-\alpha_{A}M)(3t-\alpha_{A}M-c)^{2}}{(9c_{A}(2t-\alpha_{A}M)-M)^{2}}$  $\pi_{SN}^{B} = \frac{M(2t-\alpha_{A}M)(3c_{A}(3t-2\alpha_{A}M+c)-M)^{2}}{(9c_{A}(2t-\alpha_{A}M)-M)^{2}}$ </td><td> $\pi_{SS}^{A} = \frac{c_{A}M(9c_{A}(2t-M(\alpha_{B}+\alpha_{A}))-M)(M-3c_{B}(3t-M(\alpha_{A}+2\alpha_{B})))^{2}}{3(M(c_{A}+c_{B})-9c_{A}c_{B}(2t-M(\alpha_{B}+c_{A})))^{2}}$  $\pi_{SS}^{B} = \frac{c_{B}M(9c_{B}(2t-M(\alpha_{B}+\alpha_{A}))-M)(M-3c_{A}(3t-M(\alpha_{A}+2\alpha_{B})))^{2}}{3(M(c_{A}+c_{B})-9c_{A}c_{B}(2t-M(\alpha_{B}+c_{A})))^{2}}$ </td></tr></table>

ii) If both firms offer the service, the profit of Firm i decreases in $a _ { i }$ if

$$
\alpha_ {i} > \frac {1}{2 7} \left(\frac {3 6 t}{M} - 3 6 \alpha_ {j} - \left(\frac {2}{c _ {i}} + \frac {3}{c _ {j}}\right)\right) (i, j = A a n d B, i \neq j)
$$

iii) If both firms offer the service and $a _ { i } = a _ { i } = a ,$ then Firm i’s profit is an increasing function of α if and only $i f c _ { i } <$ U(c<sub>j</sub>) where

$$
U (c _ {j}) = \frac {2 c _ {j} M}{2 7 c _ {j} (t - \alpha M) - \sqrt {8 1 c _ {j} ^ {2} (t - \alpha M) ^ {2} + 3 6 c _ {j} M (t - \alpha M) - 4 M ^ {2}}} <   c _ {j}
$$

It is interesting to compare Proposition 7-(ii) to Proposition 3- (i). According to Proposition 3-(i), when both firms offer the service with given values of $s ,$ the profit of the firm with the higher direct value increases with its strength of network effects as long as the latter is large enough $( \mathrm { i . e . , } a _ { i } ) > \left( t - \right( s _ { i } -$ ${ \cal { s } } _ { j } ) ) / M )$ . Here we see that with endogenous values of s, this is no longer true. Specifically, when both firms offer the service, a firm’s profit decreases with its service’s strength of network effects when the latter is larger than a threshold value. Note that if the firm’s (or its competitors’) marginal development cost is low enough, then the firm’s profit is always decreasing with its service’s strength of network effects (i.e., the above threshold is negative). Thus, when considering endogenous service qualities, the likelihood that a firm would benefit from stronger network effects is smaller. The stronger network effects lead to higher service qualities (Proposition 6) and even fiercer price competition.

From Propositions 6 and 7, we learn that with low development costs, firms would invest more in the direct functionalities of services with strong network effects than in the direct functionalities of services with weak network effects. However, their profits in the former case are likely to be lower. Finally, Proposition 8 describes how the service’s direct value (quality) and the firm’s profit change with the marginal development cost.

Proposition 8. (Effect of marginal development costs on service quality and firm’s profit)

i) If only Firm i offers the service, the equilibrium level of service quality (s ) and Firm i’s profit decrease in $c _ { i }$ while the profit of Firm j increases in c .

ii) If both firms offer the service, the optimal level of service quality of Firm i (s ) and its profit increase in c and decrease in c (the development cost of the competitor).

When only Firm i offers the service, we find the expected result that Firm i’s service quality and profit both increase as its marginal development cost decreases (holding the strength of network effects constant). However, surprisingly, the opposite holds when both firms offer the service. That is, a firm actually chooses a lower service quality and gains lower equilibrium profit when its marginal development cost is lower. The rationale behind these counterintuitive results is as follows: As the marginal cost of Firm i decreases, if it were not taking the competitor reactions into consideration, it would indeed choose a higher service quality and expect a higher profit. However, taking the competitor’s reaction into consideration, the firm realizes that the latter would be more aggressive when its marginal development cost is low than when it is high. Thus, to mitigate the competition, the firm chooses a lower service quality and gains lower profit than when its marginal cost is high.

## Robustness

Here we discuss two modifications to the model. First, we consider nonlinear network effects and discuss how we expect the results to change. Second, we discuss the assumption that the degree of network effects is exogenous while the direct value of the service depends on the fixed cost incurred by the firm at development.

## Nonlinear Network Effects

Although many models assume linear network effects (e.g., Li and Chen 2012; Li and Mendelson 2007; Navon et al. 2005) that facilitate closed form solutions, a few papers consider models in which network effects are a general concave function of network size (e.g., Katz and Shaprio 1985). With such concave functions, the impact of an additional customer on the value obtained by any service user decreases in the network size.

If gaining another customer has a large impact on the value of the service to all other customers, the firms have a strong incentive to reduce prices. Thus, with concave network effects, we expect that for small potential markets (i.e., when M is small), the price competition would be more intense than is described here with linear network effects, and it would be even more difficult for firms to profit from offering services with network effects. In contrast, with large potential markets (i.e., when M is large), firms would find it easier to profit from offering the service when network effects are a concave function of network size than when network effects are linear in network size.

## Endogenous Degree of Network Effects

In the previous section, we considered the firm’s investment decision when developing the service, and assumed that while firms can control the service’s direct value (quality), the magnitude of network effects exhibited by the service is exogenous.

We acknowledge that in some cases, depending on the type of the service, firms can also control to some extent their service’s strength of network effects. In such cases, the more the firm invests in developing the service’s network-based functionalities, the higher the magnitude of network effects would be. To address this issue, we solved an alternative model in which, in addition to choosing the direct value of the service, each firm chooses whether to invest a high amount and achieve strong network effects or a low amount achieving weaker network effects. The results of this alternative model regarding the relationships between the endogenous degree of network effects and the endogenous direct value, and the relationships between the marginal development cost and profits, are similar to those presented here.

## Conclusions

Advances in technology, and especially the Internet, allow firms to deliver services that create value by enabling interactions between a firm’s customers, and exhibit positive network effects. However, since the literature indicates that network effects intensify price competition (e.g., Lee and Mendelson 2007; Navon et al. 1995), it is not clear whether a firm can benefit from the common ability to offer such services or whether a firm can benefit from stronger network effects.

While the literature examines product competition with network effects, this paper is the first to model the service offering decision separately from the product offering, and to consider specific service characteristics. Our model setup, therefore, allows us to examine whether firms benefit from offering a service that imposes network effects in a market for a product with no network effects. In addition, the model supports investigation of whether the value customers obtain from service functionalities that rely on the network and the value obtained from direct functionalities (independent of network size) should be treated as complements or substitutes. This information is crucial for firms who wish to understand how to balance these two different sources of value to consumers.

We show that, in many cases, firms are indeed caught in a prisoner’s dilemma. That is, offering the service is a dominant strategy regardless of the competitor’s action; however, each firm’s profit is lower when the industry has the ability to offer the service than when such ability did not exit. Yet, while such a prisoner’s dilemma may prevail, this is not always the case. Specifically, when the services are differentiated enough in the direct value they deliver to consumers, the firm that offers the higher direct value would have a higher profit when both firms offer the service than when both do not. We also show that a firm can benefit from an exogenous increase in the strength of network effects of its own service, even though such an increase would intensify price competition, as long as its service’s direct value is high enough. These results emphasize the importance of investing in the service’s direct functionalities even when (or especially when) it exhibits strong network effects.

Future work can examine a model with heterogeneous service valuations to determine how network effects change profitability when firms sell the service separately for a fee. When service is sold separately, some consumers can buy only the product and pay less than those who buy both product and service. In addition, this alternative model can be studied to determine how network effects influence the decision whether to sell a bundle or sell the service separately in a duopoly. While bundling increases a firm’s network, it also intensifies the price competition.

## References

Allmendinger, G., and Lombreglia, R. 2005. “Four Strategies for the Age of Smart Services,” Harvard Business Review (83:10), pp. 131-145.

Cabral, L. M. B., Salant, D. J., and Woroch, G. A. 1999. “Monopoly Pricing with Network Externalities,” International Journal of Industrial Organization (17:2), pp. 199-214.

Ellison, G., and Fudenberg, D. 2000. “The Neo-Luddite’s Lament: Excessive Upgrades in the Software Industry,” The RAND Journal of Economics (31:2), pp. 253-272.

Farrell, J., and Saloner, G. 1985. “Standardization, Compatibility, and Innovation,” The RAND Journal of Economics (16:1), pp. 70-83.

Fudenberg, D., and Tirole, J. 2000. “Pricing a Network Good to Deter Entry,” The Journal of Industrial Economics (48:4), pp. 373-390.

Hotelling, H. 1929. “Stability in Competition,” Economic Journal (39), pp. 41-57.

Jing, B. 2007. “Network Externalities and Market Segmentation in a Monopoly,” Economic Letters (95:1), pp. 7-13.

Katz, M. L., and Shapiro, C. 1985. “Network Externalities, Competition, and Compatibility,” American Economic Review (75:3), pp. 424-440.

Katz, M. L., and Shapiro, C. 1986. “Technology Adoption in the Presence of Network Externalities,” Journal of Political Economy (94:4), pp. 822-841.

Katz, M. L., and Shapiro, C. 1992. “Product Introduction with Network Externalities,” The Journal of Industrial Economics (40:1), pp. 55-83.

Katz, M. L., and Shapiro, C. 1994. “Systems Competition and Network Effects,” Journal of Economic Perspectives (8:2), pp. 93-115.

Lee, D., and Mendelson, H. 2007. “Adoption of Information Technology Under Network Effects,” Information Systems Research (18:4), pp. 395-413.

Lee, D., and Mendelson, H. 2008. “Divide and Conquer: Competing with Free Technology Under Network Effects,” Production and Operations Management (17:1), pp. 12-28.

Li, C., and Bernoff, J. 2008. Groundswell: Winning in a World Transformed by Social Technologies, Boston: Harvard Business Press.

Li, X., and Chen. Y. 2012. “Corporate IT Standardization: Product Compatibility, Exclusive Purchase Commitment, and Competition Effects,” Information Systems Research (23:4), pp. 1158-1174.

Navon, A., Shy, O. and Thisse, J. 1995. “Product Differentiation in the Presence of Positive and Negative Network Effects,” Discussion Paper No. 1306, Centre for Economic Policy Research, London (http://econ.tau.ac.il/papers/phd/ Ami%20Navon%20Abstract.pdf).

Pang, M., and Etzion H. 2012. “Analyzing Pricing Strategies for Online Services with Network Effects,” Information Systems Research (23:4), pp. 1364-1377.

Palma, A., Leruth, L., and Regibeau, P. 1999. “Partial Compatibility with Network Externalities and Double Purchase,” Information Economics and Policy (11), pp. 209-227.

Reinartz, W., and Ulaga, W. 2008. “How to Sell Services More Profitably,” Harvard Business Review (86:5), pp. 90-96.

Suarez, F., Cusumano, M., and Kahl, S. 2013. “Services and the Business Models of Product Firms: An Empirical Analysis of the Software Industry,” Management Science (59:2),, pp. 420-435.

Sundararajan, A. 2003. “Network Effects, Nonlinear Pricing and Entry Deterrence,” Working Paper No. EC-03-17, Stern School

of Business, New York University (http://ssrn.com/ abstract= 292637).

Sundararajan, A. 2004. “Nonlinear Pricing and Type-Dependent Network Effects,” Economics Letters (83), pp. 107-113.

Wingfield, N. “Call of Duty Sets Sights on a Fee,” The Wall Street Journal, May 30, 2011.

## About the Authors

Hila Etzion is an assistant professor of Technology and Operations at the Ross School of Business, University of Michigan. She received a B.S. in Industrial Engineering and Management from the Technion in Israel, and a Ph.D. in Business Administration from the University of Rochester. Hila develops theoretical frameworks for evaluating the viability and the profitability of innovative strategies which utilize online selling. Her research interests include online auctions, managing multiple selling channels online, pricing strategies for online services, and the simultaneous management of offline and online selling channels. Her research has been published in leading journals such as Manufacturing & Service Operations Management, Production and Operations Management, and Information Systems Research.

Min-Seok Pang is an assistant professor of Information Systems at School of Management, George Mason University. He earned a B.S. in Industrial Engineering and an M.S. in Management from Korea Advanced Institute of Science and Technology (KAIST) and a Ph.D. in Business Administration from the University of Michigan. His research interests center around information and network economics and the business value of information technology, which studies how IT investments and resources affect organizational performance. Specifically, his interdisciplinary research examines how IT investments and resources affect performance and value of public sector organizations. His research appears in Information Systems Research and International Journal of Electronic Commerce.

# COMPLEMENTARY ONLINE SERVICES IN COMPETITIVEMARKETS: MAINTAINING PROFITABILITY IN THEPRESENCE OF NETWORK EFFECTS

Hila Etzion Department of Technology and Operations, Stephen M. Ross School of Business, University of Michigan, Ann Arbor, MI 48103 U.S.A. {etzionh@umich.edu}

Min-Seok Pang Department of Information Systems and Operations Management, School of Management, George Mason University, Fairfax, VA 22030 U.S.A. {mpang2@gmu.edu}

## Appendix A

## Derivations of Equilibrium Prices and Profits per Market Configuration

## Configuration

We derive the equilibrium in prices and demands given the choices of the two firms in the first stage of the game. We consider only cases in which (1) each firm has positive demand for its product, and (2) market is covered. The required conditions on the parameters values are given in the following assumption.

Assumption 1. Conditions for Spatial Competition in Equilibrium

(i) $2 t > M ( \alpha _ { \scriptscriptstyle A } + \alpha _ { \scriptscriptstyle B } ) .$ , where $a _ { i } = 0$ when firm i does not offer service

(A1)

$$
c - 3 t + \alpha_ {i} M - \Delta_ {i} <   s _ {i} <   3 t - 2 \alpha_ {i} M + c - \Delta_ {i} (i, j = A \text {   and   } B, i \neq j) \tag {ii}\tag{A2}
$$

$$
\text {(iii)} - 3 t + M \left(\alpha_ {i} + 2 \alpha_ {i}\right) - \Delta_ {i} <   s _ {i} - s _ {j} <   3 t - M \left(2 \alpha_ {i} + \alpha_ {j}\right) - \Delta_ {i}\tag{A3}
$$

(iv) |m<sub>i</sub> – m<sub>j</sub>| < 3t

$$
\text {(v)} \quad V > \max \left(\frac {3 t + m _ {A} + m _ {B}}{2}, V _ {S N}, V _ {N S}, V _ {S S}\right)\tag{A4}
$$

Assumption 1-(ii) ensures that an equilibrium in which both firms have positive demand prevails when only one of the firms offers the service (else, one firm would set a price to undercut the other and capture the entire market). Similarly, Assumption 1-(iii) ensures both firms have positive demand when both firms offer the service, and Assumption 1-(iv) ensures both firms have positive demand when both sell only the product. Assumption 1-(i) is necessary for the ranges given in Assumptions 1-(ii) and (iii) to be none empty, and is thus implied by the other two conditions. An identical assumption is set in Li and Chen (2012) (where M = 1 and θ denote the degree of network effects), who state: ${ ^ { \circ } \mathrm { I f } t } < \theta ,$ the network effects dominate employees’ preferences over product’s stand-alone value and employees will always purchase form one single seller.” As is shown below, given condition (i), all S.O.C are satisfied.

Finally, Assumption 1-(iv) ensures that the inherent value of the product, $V ,$ is sufficiently high so that the market for the product is covered by the two firms, whether both, neither, or only one firm offer the service.

## 1. Case NN: Both Firms Sell Only Product

When neither firm operates the service, the surplus a consumer obtains when buying the product sold by Firm A and the surplus from buying the product sold by Firm B, are given respectively by

$$
u _ {N N} ^ {A} = V - t x - p _ {N N} ^ {A}\tag{A5}
$$

$$
u _ {N N} ^ {B} = V - t (1 - x) - p _ {N N} ^ {B}\tag{A6}
$$

For spatial competition (the market is covered and the marginal customer has positive utility), it must be that $\begin{array} { r } { V > \frac { 3 t + m _ { A } + m _ { B } } { 2 } } \end{array}$ . It is easy to show that when this condition holds, in equilibrium th product price is

$$
p _ {N N} ^ {i} \stackrel {*} {=} \frac {3 t + 2 m _ {i} + m _ {j}}{3} (i, j = A \text {   and   } B, i \neq j)\tag{A7}
$$

The market share of Firm $i \ \mathrm { i s } \ \frac { M ( 3 t - m _ { i } + m _ { j } ) } { 6 t }$ , and its profit is given by

$$
\pi_ {N N} ^ {i} \stackrel {*} {=} \frac {M (3 y - m _ {i} + m _ {j}) ^ {2}}{1 8 t}\tag{A8}
$$

In this paper, we limit our attention to cases of spatial competition; that is, we assume $\begin{array} { r } { V > \frac { 3 t + m _ { A } + m _ { B } } { 2 } } \end{array}$ (see Assumption 1-(iv)).

## 2. Cases SN and NS: Only One Firm Offers a Service

Without loss of generality, we assume that only Firm A decided to offer a service to its customers. The solution when only Firm B offers the service can be derived in a similar manner.

When expected network size of firm A is $N _ { \mathrm { A } } ,$ the consumer surplus when buying from Firm $A , u _ { S N } ^ { A } ,$ and when buying from Firm B, $u _ { S N } ^ { B }$ are given by

$$
u _ {S N} ^ {A} = V - t x + s _ {A} N _ {A} - p _ {S N} ^ {A}\tag{A9}
$$

$$
u _ {S N} ^ {B} = V - t (1 - x) - p _ {S N} ^ {B}\tag{A10}
$$

The location of the customer who is indifferent between the two firms, denoted by $\hat { x }$ , is thus

$$
\hat {x} (N _ {A}) = \frac {t + \alpha_ {A} N _ {A} + s _ {A} - p _ {S N} ^ {A} + p _ {S N} ^ {B}}{2 t}\tag{A11}
$$

The demand for the product and service of Firm A, $D _ { S N } ^ { A } ,$ , given that consumers expect the number of service users to be $N _ { A } ,$ is given by $M \hat { x } \left( N _ { A } \right)$ In the fulfilled expectation equilibrium, we require that

$$
D _ {S N} ^ {A} = M \hat {\mathcal {X}} \left(D _ {S N} ^ {A}\right)\tag{A12}
$$

Solving the above equation for $D _ { S N } ^ { A } ,$ , we get

$$
D _ {S N} ^ {A} = \frac {M (t + s _ {A} - p _ {S N} ^ {A} + p _ {S N} ^ {B})}{2 t - \alpha_ {A} M}\tag{A13}
$$

Given our assumption that the market is covered, the demand for Product B is given by $D _ { S N } ^ { B } = M - D _ { S N } ^ { A } .$ . Finally, the profit functions of two firms are given by $\pi _ { S N } ^ { 4 } = D _ { S N } ^ { 4 } ( p _ { S N } ^ { A } - m _ { A } - c )$ and $\pi _ { N } ^ { B } = D _ { S N } ^ { B } ( p _ { S N } ^ { B } - m _ { B } )$

Solving the first-order conditions simultaneously (S.O.C requires $2 t > \alpha _ { A } M ,$ which is satisfied due to Assumption 1-(i)), we find that in equilibrium prices and profits are as follows:

$$
p _ {S N} ^ {A} ^ {*} = \frac {3 t - \alpha_ {A} M + s _ {A} + 2 c + 2 m _ {A} + m _ {B}}{3}, p _ {S N} ^ {B} ^ {*} = \frac {3 t - 2 \alpha_ {A} M - s _ {A} + c + m _ {A} + 2 m _ {B}}{3}\tag{A14}
$$

$$
\pi_ {S N} ^ {A} ^ {*} = \frac {M \left(3 t - c - \alpha_ {A} M + s _ {A} - m _ {A} + m _ {B}\right) ^ {2}}{9 (2 t - \alpha_ {A} M)}, \quad \pi_ {S N} ^ {B} ^ {*} = \frac {M \left(3 t + c - 2 \alpha_ {A} M - s _ {A} + m _ {A} + m _ {B}\right) ^ {2}}{9 (2 t - \alpha_ {A} M)}\tag{A15}
$$

At the above prices, the condition for both firms to have positive demand $( { \mathrm { i . e . , } } 0 < D _ { S N } ^ { i } < M$ for $i = A , B )$ is

$$
c - 3 t + \alpha_ {A} M - m _ {A} + m _ {B} <   s _ {A} <   3 t - 2 \alpha_ {A} M + c - m _ {A} + m _ {B}\tag{A16}
$$

To ensure spatial competition at the above prices, we need to find the surplus of the customer indifferent between the two products and require it to be positive. Doing so we get the following condition:

$$
V > V _ {S N} = \frac {(3 t - \alpha_ {A} M) (3 t + c - 2 \alpha_ {A} M - s _ {A} + m _ {A} - m _ {B}) - \alpha_ {A} m _ {B} M}{6 t - 3 \alpha_ {A} M}\tag{A17}
$$

## 3. Case SS: Both Firms Offer a Service

When both firms offer the service, the utility functions are given by

$$
u _ {S S} ^ {A} = V - t x + s _ {A} N _ {A} - p _ {S S} ^ {A}\tag{A18}
$$

$$
u _ {S S} ^ {B} = V - t (1 - x) + \mathrm{s} _ {\mathrm{B}} + \alpha_ {B} N _ {B} - p _ {S S} ^ {B}\tag{A19}
$$

The location of indifferent customer $\hat { x }$ is found by solving $u _ { S S } ^ { A } = u _ { S S } ^ { B }$ and is given by

$$
\hat {x} \big (N _ {A}, N _ {B} \big) = \frac {t + s _ {A} - s _ {B} + \alpha_ {A} N _ {A} - \alpha_ {B} N _ {B} - p _ {S S} ^ {A} + p _ {S S} ^ {B}}{2 t}\tag{A20}
$$

The demand for the product and service of Firm $A , D _ { S S } ^ { 4 }$ , given consumers expectations regarding network sizes, is $M \hat { x } ( N _ { A } , N _ { B } )$ , and the demand for the product and service of Firm B, $D _ { S S } ^ { B } ,$ given the assumption that the market is covered is $M - D _ { S S } ^ { 4 } .$ In the fulfilled expectation equilibrium, we require that

$$
D _ {S S} ^ {A} = M \hat {\mathcal {X}} \left(D _ {S S} ^ {A}, D _ {S S} ^ {B}\right) \quad \text { and } \quad D _ {S S} ^ {B} = M \big (1 - \hat {\mathcal {X}} \left(D _ {S S} ^ {A}, D _ {S S} ^ {B}\right) \big)\tag{A21}
$$

Solving the above two equations simultaneously for $D _ { S S } ^ { 4 }$ and $D _ { S S } ^ { B } ,$ we get

$$
D _ {S S} ^ {A} = \frac {M \left(t - \alpha_ {A} M + s _ {A} - s _ {B} - p _ {S S} ^ {A} + p _ {S S} ^ {B}\right)}{2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)}, D _ {S S} ^ {B} = \frac {N \left(t - \alpha_ {B} N + s _ {B} - s _ {A} - p _ {S S} ^ {A} + p _ {S S} ^ {B}\right)}{2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)}\tag{A22}
$$

The profit functions of the two firms are given by

$$
\pi_ {S S} ^ {i} = D _ {S S} ^ {i} (p _ {S S} ^ {i} - m _ {i} - c) (i = A \text { and } B)\tag{A23}
$$

Solving the first order conditions simultaneously (second order condition require $2 t > ( a _ { A } + a _ { B } ) M ,$ which is satisfied according to Assumption 1-(i)), we find the equilibrium prices

$$
p _ {S S} ^ {A} = \frac {1}{3} (s _ {A} - s _ {B} + 3 c + 3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + 2 m _ {A} + m _ {B})\tag{A24}
$$

$$
p _ {S S} ^ {B} = \frac {1}{3} \left(s _ {B} - s _ {A} + 3 c + 3 t - M \left(2 \alpha_ {A} + \alpha_ {B}\right) + m _ {A} + 2 m _ {B}\right)
$$

The profits at the optimal prices are given by

$$
\pi_ {S S} ^ {A} = \frac {M \left(3 t - M \left(\alpha_ {A} + 2 \alpha_ {B}\right) + s _ {A} - s _ {B} - m _ {A} + m _ {B}\right) ^ {2}}{9 \left(2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)\right)}, \quad \pi_ {S S} ^ {B} = \frac {M \left(3 t - M \left(2 \alpha_ {A} + \alpha_ {B}\right) + s _ {B} - s _ {A} + m _ {A} - m _ {B}\right) ^ {2}}{9 \left(2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)\right)}\tag{A25}
$$

The condition for both firms to have positive demand (i.e., the marginal customer’s location is interior) is

$$
- 3 t + M \left(\alpha_ {A} + 2 \alpha_ {B}\right) + m _ {A} - m _ {B} <   s _ {A} - s _ {B} <   3 t - M \left(2 \alpha_ {A} + \alpha_ {B}\right) + m _ {A} - m _ {B}\tag{A26}
$$

which also requires that

$$
2 t > M \left(\alpha_ {A} + \alpha_ {B}\right)\tag{A27}
$$

or else above range for $s _ { A } - s _ { B }$ values is empty. Finally, with the above prices, there is spatial completion if and only if

$$
V > V _ {S S} = C - \frac {1}{3} \left(2 s _ {A} + s _ {B} - 2 m _ {A} - m _ {B} - 5 t + M \left(3 \alpha_ {A} + 2 \alpha_ {B}\right)\right) + \frac {\left(t - \alpha_ {A} M\right) \left(s _ {B} - s _ {A} + t - \alpha_ {A} M + m _ {A} - m _ {B}\right)}{2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)}\tag{A28}
$$

## Appendix B

## Proofs

## Proof of Proposition 1

Having obtained the equilibrium prices and profits in Appendix A (see also Tables 2 and 3 in the paper), we now derive the conditions for each possible market configuration to be an equilibrium. The conditions are derived as follows:

(i) Both firms offer the service in equilibrium if and only i $\mathrm { f } \pi _ { S S } ^ { A } > \pi _ { N S } ^ { A }$ and $\pi _ { S S } ^ { B } > \pi _ { S N } ^ { B }$

(ii) Both firms sell only product in equilibrium if and only $\mathrm { i f } \pi _ { N N } ^ { A } > \pi _ { S N } ^ { A }$ and $\pi _ { N N } ^ { B } > \pi _ { N S } ^ { B }$

(iii) Only Firm A offers a service in equilibrium if and only i $\mathrm { f } \pi _ { S N } ^ { A } > \pi _ { N N } ^ { A }$ and $\pi _ { S N } ^ { B } > \pi _ { S S } ^ { B }$

(iv) Only Firm B offers a service in equilibrium if and only if $\cdot _ {  { N S } } ^ { A } > \pi _ { S S } ^ { A }$ and $\pi _ { N S } ^ { B } > \pi _ { N N } ^ { B }$

## Equilibrium in Which Both Firms Sell the Service

In order for both Firm A and Firm B to offer the service in equilibrium, it must be that $\pi _ { S S } ^ { A } > \pi _ { N S } ^ { A }$ and $\pi _ { S S } ^ { B } > \pi _ { S N } ^ { B }$ , so that neither firm has incentive to deviate and not sell the service. These two conditions are given by

$$
s _ {i} > X _ {i} s _ {j} + Y _ {i} \text {   for   } (i = A, j = B) \text {   and   for   } (i = B, j = A)
$$

where $\begin{array} { r } { X _ { i } = 1 - \frac { \sqrt { 2 t - M ( \alpha _ { A } + \alpha _ { B } ) } } { \sqrt { 2 t - \alpha _ { j } M } } } \end{array}$

$$
\text { and } Y _ {i} = \frac {\left(3 t - 2 \alpha_ {j} M + c + m _ {i} - m _ {j}\right) \sqrt {2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)}}{\sqrt {2 t - \alpha_ {j} M}} - \left(3 t - M \left(\alpha_ {A} + \alpha_ {B} + \alpha_ {j}\right) - m _ {i} + m _ {j}\right).
$$

## Equilibrium in Which Neither Firm Sells the Service

An equilibrium in which neither firm provides the service exists if and only if $\pi _ { N N } ^ { A } > \pi _ { S N } ^ { A }$ and $\pi _ { N N } ^ { B } > \pi _ { N S } ^ { B }$ , so that neither firm has incentive to deviate and offer the service. From the profit expressions in Table 3, we find that $\pi _ { N N } ^ { A } > \pi _ { S N } ^ { A }$ if and only if

$$
s _ {A} <   \frac {\left(3 t - m _ {i} + m _ {j}\right) \sqrt {2 \left(2 t - \alpha_ {i} M\right)}}{2 \sqrt {t}} - 3 t + \alpha_ {i} M + c + m _ {i} - m _ {i}\tag{A29}
$$

We denote this upper bound by $\bar { s } _ { A } . \bar { s } _ { B }$ can be derived in a similar manner.

## Equilibrium in Which Only Firm A Sells the Service

The conditions under which there is an equilibrium in which only Firm A offers the service are $\mathrm { ( i ) } \pi _ { S N } ^ { B } > \pi _ { S S } ^ { B }$ and (ii) $\pi _ { S N } ^ { A } > \pi _ { N N } ^ { A }$ . Condition (i) implies that Firm B does not have an incentive to deviate and offer the service. Condition (ii) indicates that Firm A does not have an incentive to deviate and not offer the service. Condition (i) and (ii) translate to $s _ { B } { < } X _ { B } s _ { A } { + } Y _ { B }$ and $\mathbf { S } _ { A } > \bar { s } _ { A } .$ , respectively. The conditions under which an equilibrium in which only Firm B sells the service is feasible can be derived in a similar manner.

## Proof of Proposition 2

We derive the condition for $\pi _ { S S } ^ { i } < \pi _ { N N } ^ { i } .$

$\begin{array} { r } { \pi _ { S S } ^ { i } = \frac { M \left( 3 t - M \left( \alpha _ { i } + 2 \alpha _ { j } \right) + s _ { i } - s _ { j } - m _ { i } + m _ { j } \right) ^ { 2 } } { 9 \left( 2 t - M \left( \alpha _ { i } + \alpha _ { j } \right) \right) } } \end{array}$ , and given Assumption 1-(iii), we have $3 t \ - \ M ( { \alpha } _ { i } \ + \ 2 { \alpha } _ { j } ) \ + \ s _ { i } \ - \ s _ { j } \ + \ m _ { i } \ - \ m _ { j } \ > \ 0$ Thus $\begin{array} { r } { \pi _ { S S } ^ { i } = \frac { M \left( 3 t - M \left( \alpha _ { i } + 2 \alpha _ { j } \right) + s _ { i } - s _ { j } - m _ { i } + m _ { j } \right) ^ { 2 } } { 9 \left( 2 t - M \left( \alpha _ { i } + \alpha _ { j } \right) \right) } < \pi _ { N N } ^ { i } = \frac { M \left( 3 t - m _ { i } + m _ { j } \right) ^ { 2 } } { 1 8 t } } \end{array}$ If and only if

$$
\left(3 t - M \left(\alpha_ {i} + 2 \alpha_ {i}\right) + s _ {i} - s _ {j} - m _ {i} + m _ {j}\right) <   \frac {\left(3 t - m _ {i} + m _ {j}\right) \sqrt {2 \left(2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)\right)}}{2 \sqrt {t}}\tag{A30}
$$

Rearranging terms, we get

$$
s _ {i} - s _ {j} <   M \left(\alpha_ {i} + 2 \alpha_ {j}\right) + s _ {i} - s _ {j} + m _ {i} - m _ {j} + \frac {\left(3 t - m _ {i} + m _ {j}\right) \sqrt {\left(2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)\right)}}{\sqrt {2 t}}
$$

## Proof of Proposition 3

(i) We examine the derivative of the profit of Firm A, when both firms offer the service, with respect to the $\alpha _ { A }$

$$
\begin{array}{l} \frac {\partial}{\partial \alpha_ {A}} \pi_ {S S} ^ {A} = \frac {\partial}{\partial \alpha_ {A}} \frac {M \big (3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} - m _ {A} + m _ {B} \big) ^ {2}}{9 \big (2 t - M (\alpha_ {A} + \alpha_ {B}) \big) ^ {2}} \\ = - \frac {M ^ {2} \big (t - \alpha_ {A} M - s _ {A} + s _ {B} + m _ {A} - m _ {B} \big) \big (3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} - m _ {A} + m _ {B} \big)}{9 \big (2 t - M (\alpha_ {A} + \alpha_ {B}) \big) ^ {2}} \\ = - D _ {S S} ^ {A} \frac {M \big (t - \alpha_ {A} M - s _ {A} + s _ {B} + m _ {A} - m _ {B} \big)}{3 \big (2 t - M (\alpha_ {A} + \alpha_ {B}) \big)} \end{array}\tag{A31}
$$

The above is positive if and only if $\frac { M \big ( t - \alpha _ { _ { A } } M - s _ { _ { A } } + s _ { B } + m _ { _ { A } } - m _ { _ { B } } \big ) } { 3 \big ( 2 t - M \big ( \alpha _ { _ { A } } + \alpha _ { _ { B } } \big ) \big ) }$ is negative, which is equivalent to $s _ { { \scriptscriptstyle A } } > s _ { { \scriptscriptstyle B } } + t - \alpha _ { { \scriptscriptstyle A } } M + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } } .$ . This is the condition stated in Proposition 3-(i).

Next, we examine the derivative of the profit of Firm $A ,$ when both firms offer the service, with respect to the degree of network effects of Firm B.

$$
\begin{array}{l} \frac {\partial}{\partial \alpha_ {B}} \pi_ {S S} ^ {A} = \frac {\partial}{\partial \alpha_ {B}} \frac {M (3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} - m _ {A} + m _ {B}) ^ {2}}{9 (2 t - M (\alpha_ {A} + \alpha_ {B})) ^ {2}} \\ = - \frac {M ^ {2} (5 t - M (3 \alpha_ {A} + 2 \alpha_ {B}) - s _ {A} + s _ {B} + m _ {A} - m _ {B}) (3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} - m _ {A} + m _ {B})}{9 (2 t - M (\alpha_ {A} + \alpha_ {B})) ^ {2}} \\ = - D _ {S S} ^ {A} \frac {M (5 t - M (3 \alpha_ {A} + 2 \alpha_ {B}) - s _ {A} + s _ {B} + m _ {A} - m _ {B})}{3 (2 t - M (\alpha_ {A} + \alpha_ {B}))} \end{array}\tag{A32}
$$

The above is negative if and only $\begin{array} { r } { \mathrm { i f } \frac { M \left( 5 t - M \left( 3 \alpha _ { A } + 2 \alpha _ { B } \right) - s _ { A } + s _ { B } + m _ { A } - m _ { B } \right) } { 3 \left( 2 t - M \left( \alpha _ { A } + \alpha _ { B } \right) \right) } > 0 } \end{array}$ . By Assumption 1-i, $2 t > M ( { \alpha } _ { { \scriptscriptstyle A } } + { \alpha } _ { { \scriptscriptstyle B } } )$ . Thus, $\begin{array} { r } { \frac { \partial } { \partial \alpha _ { B } } \pi _ { S S } ^ { A } < 0 } \end{array}$ if and only i $\operatorname { f } s _ { A } - s _ { B } < 5 t - M ( 3 \alpha _ { A } + 2 \alpha _ { B } ) + m _ { A } - m _ { B } .$ In addition, due to Assumption 1-(i) we have

$$
\left(5 t - M \left(3 \alpha_ {A} + 2 \alpha_ {B}\right)\right) - \left(3 t - M \left(2 \alpha_ {A} + \alpha_ {B}\right)\right) = 2 t - M \left(\alpha_ {A} + \alpha_ {B}\right) > 0
$$

And due to Assumption 1-(ii) we have $s _ { { \scriptscriptstyle A } } - s _ { { \scriptscriptstyle B } } < 3 t - M ( 2 \alpha _ { { \scriptscriptstyle A } } + \alpha _ { { \scriptscriptstyle B } } ) + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } } .$ which leads to $\begin{array} { r } { s _ { A } - s _ { B } < 5 t - M ( 3 \alpha _ { A } + 2 \alpha _ { B } ) + m _ { A } - m _ { B } . } \end{array}$ . Therefore, $\textstyle \frac { \partial } { \partial \alpha _ { B } } \pi _ { S S } ^ { A }$ is always negative.

(ii) Suppose that in equilibrium Firm A offers the service and Firm B does not. Then, the derivative of Firm A’s profit with respect to $\alpha _ { A }$ is

$$
\begin{array}{r l} \frac {\partial}{\partial \alpha_ {A}} \pi_ {S N} ^ {A} & = \frac {\partial}{\partial \alpha_ {A}} \frac {M (3 t - c - \alpha_ {A} M + s _ {A} - m _ {A} + m _ {B}) ^ {2}}{9 (2 t - \alpha_ {A} M)} \\ & = \frac {M ^ {2} (- t + \alpha_ {A} M - c + s _ {A} - m _ {A} + m _ {B}) (3 t - \alpha_ {A} M - c + s _ {A} - m _ {A} + m _ {B})}{9 (2 t - \alpha_ {A} M) ^ {2}} \\ & = D _ {S N} ^ {A} \left(\frac {M (- t + \alpha_ {A} M - c + s _ {A} - m _ {A} + m _ {B})}{3 (2 t - \alpha_ {A} M)}\right) \end{array}\tag{A33}
$$

Given our assumption that both firms have positive product demands, which also requires $2 t { > } \alpha _ { \mathit { A } } M ,$ , we see that $\begin{array} { r } { \frac { \partial } { \partial \alpha _ { A } } \pi _ { S N } ^ { A } } \end{array}$ is positive if and only if $s _ { { \scriptscriptstyle A } } > t - \alpha _ { { \scriptscriptstyle A } } M + c + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } }$

Next we examine the derivative of the profit of Firm B:

$$
\begin{array}{c} \frac {\partial}{\partial \alpha_ {A}} \pi_ {S N} ^ {B} = \frac {\partial}{\partial \alpha_ {B}} \frac {M (3 t + c - 2 \alpha_ {A} M - s _ {A} + m _ {A} - m _ {B}) ^ {2}}{9 (2 t - \alpha_ {A} M)} \\ = \frac {M ^ {2} (- 5 t + 2 \alpha_ {A} M + c - s _ {A} + m _ {A} - m _ {B}) (3 t + c - 2 \alpha_ {A} M - s _ {A} + m _ {A} - m _ {B})}{9 (2 t - \alpha_ {A} M) ^ {2}} \\ = D _ {S N} ^ {B} \left(\frac {M (- 5 t + 2 \alpha_ {A} M + c - s _ {A} + m _ {A} - m _ {B})}{3 (2 t - \alpha_ {A} M)}\right) \end{array}\tag{A34}
$$

We see that $\begin{array} { r } { \frac { \partial } { \partial \alpha _ { \scriptscriptstyle A } } \pi _ { S N } ^ { B } } \end{array}$ is negative if and only if $\begin{array} { r } { \frac { M \left( - 5 t + 2 \alpha _ { _ { A } } M + c - s _ { _ { A } } + m _ { _ { A } } - m _ { _ { B } } \right) } { 3 \left( 2 t - \alpha _ { _ { A } } M \right) } < 0 } \end{array}$ . Given that $2 t > \alpha _ { _ A } M _ { _ { ☉ } }$ we find that Firm $B ^ { \prime } { \bf s }$ profit is decreasing in $\alpha _ { A }$ if and only if $s _ { { \scriptscriptstyle A } } > - 5 t + 2 \alpha _ { { \scriptscriptstyle A } } M + c + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } }$ . Furthermore,

$$
\left(- 5 t + 2 \alpha_ {A} M + c + m _ {A} - m _ {B}\right) - \bar {s} _ {A} = - \left(2 \left(2 t - \alpha_ {A} M\right) + \frac {\left(3 t - m _ {i} + m _ {j}\right) \sqrt {2 \left(2 t - \alpha_ {i} M\right)}}{2 \sqrt {t}}\right) <   0
$$

Thus, $\bar { s } _ { { \scriptscriptstyle A } } > - 5 t + 2 \alpha _ { { \scriptscriptstyle A } } M + c + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } }$ . We conclude that when Firm A offers the service in equilibrium (which implies $s _ { A } > \bar { s } _ { A }$ according to Proposition 1), it must be that $s _ { { \scriptscriptstyle A } } > - 5 t + 2 \alpha _ { { \scriptscriptstyle A } } M + c + m _ { { \scriptscriptstyle A } } - m _ { { \scriptscriptstyle B } } .$ and thus $\begin{array} { r } { \frac { \partial } { \partial \alpha _ { A } } \pi _ { S N } ^ { B } < 0 } \end{array}$

(iii) We examine the derivative of the profit of Firm A, when both firms offer the service, with respect to the common degree of network effects:

$$
\frac {\partial}{\partial \alpha} \pi_ {S S} ^ {A} = \frac {\partial}{\partial \alpha} \frac {M (3 (t - \alpha M) + (s _ {A} - s _ {B}) - m _ {A} + m _ {B}) ^ {2}}{1 8 (t - \alpha M)} = \frac {M ^ {2}}{1 8} \left(\frac {(s _ {A} - s _ {B} - m _ {A} + m _ {B}) ^ {2}}{(t - \alpha M) ^ {2}} - 9\right)\tag{A35}
$$

In equilibrium we have $\begin{array} { r } { D _ { S S } ^ { A } = \frac { 1 } { 6 } M \left( 3 + \frac { \left( s _ { A } - s _ { B } - m _ { A } + m _ { B } \right) } { t - \alpha M } \right) } \end{array}$ and $\begin{array} { r } { D _ { S S } ^ { B } = \frac { 1 } { 6 } M \left( 3 + \frac { \left( s _ { B } - s _ { A } + m _ { A } - m _ { B } \right) } { t - \alpha M } \right) } \end{array}$ . Under our assumption that Firm B has positive demand $\left( D _ { S S } ^ { B } > 0 \right)$ , it must be that $\frac { s _ { { } _ { A } } - s _ { { } _ { B } } - m _ { { } _ { A } } + m _ { { } _ { B } } } { t - o M } < 3$ . Thus,

$$
\frac {\partial}{\partial \alpha} \pi_ {S S} ^ {A} = \frac {M ^ {2}}{1 8} \left(\frac {\left(s _ {A} - s _ {B} - m _ {A} + m _ {B}\right) ^ {2}}{(t - \alpha M) ^ {2}} - 9\right) <   0\tag{A36}
$$

Similarly, $\begin{array} { r } { \frac { \partial } { \partial \alpha } \pi _ { S S } ^ { B } } \end{array}$ is negative when both firms have positive product demand.

## Proof of Proposition 4

(i) We examine the derivative of Firm A’s profit, when both offer the service, with respect to M.

$$
\begin{array}{l} \frac {\partial}{\partial M} \pi_ {S S} ^ {A} = \frac {\partial}{\partial M} \frac {M \left(3 t - M \left(\alpha_ {A} + 2 \alpha_ {B}\right) + s _ {A} - s _ {B} - m _ {A} + m _ {B}\right) ^ {2}}{1 8 \left(t - M \left(\alpha_ {A} + \alpha_ {B}\right)\right)} \\ = D _ {S S} ^ {A} \left(\frac {2}{3} \left(\frac {t \left(s _ {A} - s _ {B} - m _ {A} + m _ {B} + 3 t - M \left(\alpha_ {A} + 2 \alpha_ {B}\right)\right)}{M \left(2 t - M \left(\alpha_ {A} + \alpha_ {B}\right)\right)} - \alpha_ {A} - 2 \alpha_ {B}\right)\right) \end{array}\tag{A37}
$$

Above is negative if and only if $\begin{array} { r l r } { \frac { t \left( s _ { A } - s _ { B } - m _ { A } + m _ { B } + 3 t - M \left( \alpha _ { A } + 2 \alpha _ { B } \right) \right) } { M \left( 2 t - M \left( \alpha _ { A } + \alpha _ { B } \right) \right) } - \alpha _ { A } - 2 \alpha _ { B } } & { { } } & { } \end{array}$ is negative, which is equivalent to

$$
s _ {A} - s _ {B} <   3 M \left(\alpha_ {A} + 2 \alpha_ {B}\right) - 3 t - \frac {M ^ {2} \left(\alpha_ {A} + \alpha_ {B}\right) \left(\alpha_ {A} + 2 \alpha_ {B}\right)}{t} + m _ {A} - m _ {B}\tag{A38}
$$

The RHS of A38 can be either negative or positive.

(ii) Suppose only Firm A offers the service.

$$
\begin{array}{c} \frac {\partial}{\partial M} \pi_ {S N} ^ {A} = \frac {\partial}{\partial M} \frac {M (3 t - \alpha_ {A} M + s _ {A} - c - m _ {A} + m _ {B}) ^ {2}}{9 (2 t - \alpha_ {A} M)} \\ = D _ {S N} ^ {A} \left(\frac {2 (\alpha_ {A} ^ {2} M ^ {2} - t (c - 3 t + 3 \alpha_ {A} M - s _ {A} + m _ {A} - m _ {B}))}{3 M (2 t - \alpha_ {A} M)}\right) \end{array}\tag{A39}
$$

The above is positive if and only if $\frac { 2 \big ( \alpha _ { A } ^ { 2 } M ^ { 2 } - t \big ( c - 3 t + 3 \alpha _ { A } M - s _ { A } + m _ { A } - m _ { B } \big ) \big ) } { 3 M \big ( 2 t - \alpha _ { A } M \big ) }$ is positive, which, given the assumption that $t > a _ { A } M ,$ is equivalent to

$$
s _ {A} > c - 3 t + 3 \alpha_ {A} M - \frac {\alpha_ {A} ^ {2} M ^ {2}}{t} + m _ {A} - m _ {B}\tag{A40}
$$

## Proof of Proposition 5

We start by deriving consumer surplus under each of the four possible market configurations (SS, NN, NS, and SN). Define $x _ { \mathrm { i n d i f } } i$ as the location of the consumer indifferent between buying the product from Firm A and buying from Firm B. Then, when both firms offer the service in equilibrium

$$
x _ {i n d i f} = \frac {3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} - m _ {A} + m _ {B}}{3 (2 t - M (\alpha_ {A} + \alpha_ {B}))}\tag{A41}
$$

When only Firm i sells the service, in equilibrium

$$
x _ {i n d i f} = \frac {3 t - c - \alpha_ {i} M + s _ {i} - m _ {i} + m _ {j}}{6 t - 3 \alpha_ {i} M}\tag{A42}
$$

Consumer surplus when Firm A sells the service and Firm B does not is given by

$$
\begin{array}{l} C S _ {A} = M \int_ {0} ^ {x _ {i n d i f}} \left(V - t x - p _ {S N} ^ {A} + s _ {A} + \alpha_ {A} M x _ {i n d i f}\right) d x + N \int_ {x _ {i n d i f}} ^ {1} \left(V - t (1 - x) - p _ {S N} ^ {B}\right) d x \\ = M \int_ {0} ^ {x _ {i n d i f}} \left(V - t x - \left(\frac {3 t + 2 c - \alpha_ {A} M + s _ {A} - m _ {A} + m _ {B}}{3}\right) + s _ {A} + \alpha M x _ {i n d i f}\right) d x + \\ M \int_ {x _ {i n d i f}} ^ {1} \left(V - t (1 - x) - \left(\frac {3 t + c - 2 \alpha_ {A} M - s _ {A} + m _ {A} - m _ {B}}{3}\right)\right) d x \\ = M V - \frac {M (5 t - 3 \alpha_ {A} M - 2 (s _ {A} - c - m _ {A} - m _ {B}))}{4} \\ + \frac {M (\alpha_ {A} M + 2 s _ {A} - 2 c - 2 m _ {A} - 2 m _ {B}) (2 t (s _ {A} - c + m _ {A} - m _ {B}) + \alpha_ {A} M (7 t - 3 \alpha_ {A} M))}{3 6 (2 t - \alpha_ {A} M) ^ {2}} \end{array}
$$

Similarly, consumer surplus when only Firm B sells the service is given by:

$$
\begin{array}{l} C S _ {B} = M V - \frac {M (5 t - 3 \alpha_ {B} M - 2 (s _ {B} - c - m _ {A} - m _ {B}))}{4} \\ + \frac {M (\alpha_ {B} M + 2 s _ {B} - 2 c - 2 m _ {A} - 2 m _ {B}) (2 t (s _ {B} - c - m _ {A} + m _ {B}) + \alpha_ {B} M (7 t - 3 \alpha_ {B} M))}{3 6 (2 t - \alpha_ {B} M) ^ {2}} \end{array}
$$

Consumer surplus when both firms offer the service is given by

$$
\begin{array}{l} C S _ {S S} = M \int_ {0} ^ {x _ {i n d i f}} \left(V - t x - \left(\frac {3 t - M (\alpha_ {A} + 2 \alpha_ {B}) + s _ {A} - s _ {B} + 3 c - m _ {A} + m _ {B}}{3}\right) + s _ {A} + \alpha_ {A} M x _ {i n d i f}\right) d x + \\ \quad M \int_ {x _ {i n d i f}} ^ {1} \left(V - t (1 - x) - \left(\frac {3 t - M (2 \alpha_ {A} + \alpha_ {B}) + s _ {B} - s _ {A} + 3 c + m _ {A} - m _ {B}}{3}\right) + s _ {B} + \alpha_ {B} M (1 - x _ {i n d i f})\right) d x \\ = M V + \frac {M (6 (2 s _ {A} + s _ {B}) - 1 8 c - 2 5 t + 6 M (3 \alpha_ {A} + 2 \alpha_ {B}) - 1 2 m _ {A} - 6 m _ {B})}{1 8} + \frac {2 M (2 t - 3 \alpha_ {A} M) (t - \alpha_ {A} M - s _ {A} + s _ {B} + m _ {A} - m _ {B})}{1 8 (2 t - M (\alpha_ {A} + \alpha_ {B}))} + \\ \frac {2 M t (t - \alpha_ {A} M - s _ {A} + s _ {B} + m _ {A} - m _ {B}) ^ {2}}{1 8 (2 t - m (\alpha_ {A} + \alpha_ {B})) ^ {2}} \end{array}
$$

Finally, consumer surplus when neither firm offers the service is given by:

$$
\begin{array}{l} C S _ {N N} = M \int_ {0} ^ {\frac {3 t - m _ {A} + m _ {B}}{6 t}} \left(V - t x - \frac {3 t + 2 m _ {A} + m _ {B}}{3}\right) d x + M \int_ {\frac {3 t - m _ {A} + m _ {B}}{6 t}} ^ {1} \left(V - t (1 - x) - \frac {3 t + m _ {A} + 2 m _ {B}}{3}\right) d x \\ = M V + \frac {M \left(\left(m _ {A} - m _ {B}\right) ^ {2} - 1 8 t \left(m _ {A} + m _ {B}\right) - 4 5 t ^ {2}\right)}{3 6 t} \end{array}
$$

We denote the social welfare when both firms offer service, $\pi _ { S S } ^ { A } + \pi _ { S S } ^ { B } + C S _ { S S } ,$ , by $S W _ { S S } ,$ the social welfare when neither firm offers service $\pi _ { N N } ^ { A } + \pi _ { N N } ^ { B } + C S _ { N N } , \mathrm { b y } S W _ { N N } ,$ , and the social welfare when only Firm i offers service by $S W _ { i }$ . The profit expressions are given in Table 3, and were derived in Appendix A.

$F ^ { i } ( s _ { i } , s _ { j } )$ is defined as the difference between social welfare when both firms offer service to social welfare when only Firm i offers service, specifically:

$$
\begin{array}{l}F ^ {i} \left(s _ {i}, s _ {j}\right) = S W _ {S S} - S W _ {i} =\\\frac {M}{9} \left(7 s _ {i} + s _ {j} + M \left(5 \alpha_ {i} + \alpha_ {j}\right) - 8 c - 7 \left(m _ {i} - m _ {i}\right) + \frac {t \left(t - \alpha_ {i} M + s _ {j} - s _ {i} + m _ {i} - m _ {j}\right) ^ {2}}{\left(2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)\right) ^ {2}} + \right.\\\frac {\left(4 t - 5 \alpha_ {i} M + 2 \left(s _ {j} - s _ {i} + m _ {i} - m _ {j}\right)\right) \left(t - \alpha_ {i} M - s _ {i} + s _ {j} + m _ {i} - m _ {j}\right)}{2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)} -\\\frac {2 \left(2 t + s _ {i} - c - m _ {i} - m _ {j}\right)\left(t + s _ {i} + c - m _ {i} + m _ {j}\right)}{2 t - \alpha_ {i} M} - \frac {t \left(c + m _ {i} - m _ {j} - s _ {i} - t\right) ^ {2}}{\left(2 t - \alpha_ {i} M\right) ^ {2}}\left. \right)\end{array}\tag{A43}
$$

Thus, when $F ^ { i } ( s _ { i } , s _ { j } ) < 0$ , social welfare when only Firm i offers the service exceeds social welfare when both firms offer the service.

Setting $m _ { i } = m _ { j } , F ^ { i } ( s _ { i } , s _ { j } )$ becomes

$$
\begin{array}{l} F ^ {i} \left(s _ {i}, s _ {j}\right) = \\ \frac {M}{9} \left(7 s _ {i} + s _ {j} + M \left(5 \alpha_ {i} + \alpha_ {j}\right) - 8 c + \frac {t \left(t - \alpha_ {j} M + s _ {j} - s _ {i}\right) ^ {2}}{\left(2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)\right) ^ {2}} + \frac {\left(4 t - 5 \alpha_ {i} M + 2 \left(s _ {j} - s _ {i}\right)\right) \left(t - \alpha_ {i} M - s _ {i} + s _ {j}\right)}{2 t - M \left(\alpha_ {i} + \alpha_ {j}\right)} - \right. \\ \left. \frac {2 (2 t + s _ {i} - c) (t + s _ {i} + c)}{2 t - \alpha_ {i} M} - \frac {t (c - s _ {i} - t) ^ {2}}{(2 t - \alpha_ {i} M) ^ {2}}\right) \end{array}
$$

When $m _ { A } = m _ { B } ,$ given the conditions on s specified in Assumption 1, we can show that $S W _ { A } > S W _ { N N }$ iff $\begin{array} { r } { s _ { A } > \frac { 2 c - \alpha _ { A } N } { 2 } } \end{array}$ . Similarly, $S W _ { B } > S W _ { N N }$ iff $\begin{array} { r } { s _ { B } > \frac { 2 c - \alpha _ { B } N } { 2 } } \end{array}$ . In addition, it is easy to show that $\frac { 2 c - \alpha _ { i } N } { 2 } < \overline { { S } } _ { i }$ . Thus, as long as in equilibrium at least one firm offers the service (i.e., at least one s<sub>i</sub> is larger than ${ \bar { s _ { i } } } )$ , we know that NN is not socially optimal. As long as $\begin{array} { r } { S _ { A } > \frac { 2 c - \alpha _ { A } N } { 2 } \mathrm { ~ o r ~ } S _ { B } > \frac { 2 c - \alpha _ { B } N } { 2 } } \end{array}$ (or both), social welfare when one firm offers service exceeds social welfare when neither offers, and thus social welfare is maximized when both offer service if and only $\mathrm { i f } \ F ^ { A } ( s _ { A } , s _ { B } ) >$ 0and $F ^ { B } ( s _ { A } , s _ { B } ) > 0$

Finally, when $\begin{array} { r } { s _ { A } < \frac { 2 c - \alpha _ { A } N } { 2 } } \end{array}$ and $\begin{array} { r } { s _ { B } < \frac { 2 c - \alpha _ { B } N } { 2 } } \end{array}$ , social welfare when neither firm offers service is larger than social welfare when only Firm A or only Firm B offers the service. In addition, when $\begin{array} { r } { S _ { A } < \frac { 2 c - \alpha _ { A } N } { 2 } , s _ { B } < \frac { 2 c - \alpha _ { B } N } { 2 } } \end{array}$ , and $c > \frac { \alpha _ { i } N } { 2 }$ , we find that $S W _ { S S } { < } S W _ { N N }$ . Finally, when $\begin{array} { r } { s _ { A } < \frac { 2 c - \alpha _ { A } N } { 2 } } \end{array}$ and $\begin{array} { r } { s _ { B } < \frac { 2 c - \alpha _ { B } N } { 2 } } \end{array}$ , in equilibrium, neither firm offers service $\begin{array} { r } { ( \mathrm { a s ~ } \frac { 2 c - \alpha _ { i } N } { 2 } < \overline { { S } } _ { i } ) } \end{array}$ . Thus the equilibrium is NN, which is also socially optimal. The rest is trivial based on the results from Proposition 1.

## Proof of Proposition 6

In the case in which firms choose the direct service quality (s<sub>i</sub>) endogenously, to ensure that the second-order conditions are met, the market is covered, and the two firms have positive demands, the following parameter assumptions are needed.

## Assumption 2.

(i) $t > \alpha _ { i } M ~ ( i = A \mathrm { \ a n d } B )$

(ii) $\begin{array} { r } { c _ { i } > \frac { M } { 1 8 \left( t - \alpha _ { i } M \right) } \ ( i = A \mathrm { ~ a n d } B ) } \end{array}$

(iii) $\begin{array} { r } { c _ { i } > \frac { M } { 3 \left( 3 t - 2 \alpha _ { i } M + c \right) } \ ( i = { \cal A } \mathrm { ~ a n d } { \cal B } ) } \end{array}$

(iv) $c < 3 t - \alpha _ { i } M \ ( i = A \mathrm { \ a n d } B )$

(v) $\begin{array} { r } { c _ { i } < \frac { M } { 9 \left( t - \alpha _ { o } M \right) } \ ( i = A \mathrm { ~ a n d } B ) } \end{array}$

(i) In Case SN,

$$
\frac {\partial}{\partial \alpha_ {A}} S _ {A} = \frac {M ^ {2} (M - 9 c _ {A} (c - t))}{(M - 9 c _ {A} (2 t - \alpha_ {A} M)) ^ {2}}
$$

This is positive if and only i $\mathrm { : ( i ) } c > $ and $\begin{array} { r } { c _ { \scriptscriptstyle A } < \frac { M } { 9 \left( c - t \right) } \mathrm { ~ o r ~ } ( \mathrm { i i } ) c < t \mathrm { a n d ~ } c _ { \scriptscriptstyle A } > \frac { M } { 9 \left( c - t \right) } } \end{array}$ . In the latter case, $\begin{array} { r } { \frac { M } { 9 ( c - t ) } < 0 } \end{array}$ and thus, when $c < t ,$ we have $\begin{array} { r } { \frac { \partial } { \partial \alpha _ { \scriptscriptstyle A } } s _ { \scriptscriptstyle A } > 0 } \end{array}$ for all positive $c _ { A }$ .

(ii) In Case SS,

$$
\frac {\partial}{\partial \alpha_ {A}} S _ {A} = \frac {c _ {B} M ^ {2} \left(c _ {B} M - c _ {A} (2 M - 9 c _ {B} (t - \alpha_ {A} M))\right)}{\left(M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B}))\right) ^ {2}}
$$

By Assumption 2-(v), $2 M - 9 c _ { B } ( t - \alpha _ { B } M ) = M + \left( M - 9 c _ { B } \left( t - \alpha _ { B } M \right) \right)$ . Therefore, $\frac { \partial } { \partial \alpha _ { \scriptscriptstyle A } } S _ { \scriptscriptstyle A } > 0$ if and only if $\begin{array} { r } { c _ { A } < \frac { c _ { B } M } { 2 M - 9 c _ { B } \left( t - \alpha _ { B } M \right) } } \end{array}$

$$
\frac {\partial}{\partial \alpha_ {B}} S _ {A} = \frac {c _ {B} M ^ {2} \left(2 c _ {B} M - c _ {A} (M + 9 c _ {B} (t - \alpha_ {A} M))\right)}{\left(M \left(c _ {A} + c _ {B}\right) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B}))\right) ^ {2}}
$$

This is positive if and only if $\begin{array} { r } { c _ { A } < \frac { 2 c _ { B } M } { M + 9 c _ { B } \left( t - \alpha _ { A } M \right) } } \end{array}$

(iii) When $a _ { \scriptscriptstyle A } = a _ { \scriptscriptstyle B } = a ,$ , the optimal direct value is $\begin{array} { r } { { { S } _ { { A } } } = \frac { { { M } \left( { { M } - 9 { { c } _ { B } } \left( t - \alpha { { M } } \right) } \right) } } { { { M } \left( { { { c } _ { A } } + { { c } _ { B } } } \right) - 1 8 { { c } _ { A } } { { c } _ { B } } \left( t - \alpha { { M } } \right) } } } \end{array}$ . Then

$$
\frac {\partial}{\partial \alpha} S _ {A} = \frac {3 c _ {B} M ^ {2} (c _ {B} - c _ {A})}{(M (c _ {A} + c _ {B}) - 1 8 c _ {A} c _ {B} (t - \alpha M)) ^ {2}}
$$

which is positive if any only $\operatorname { i f } c _ { A } < c _ { B } .$

## Proof of Proposition 7

(i) In Case SN,

$$
\begin{array}{c} \frac {\partial}{\partial \alpha_ {A}}   \pi_ {S N} ^ {A} = \frac {\partial}{\partial \alpha_ {A}} \bigg (\frac {3 c _ {A} M (3 t - \alpha_ {A} M - c) ^ {2}}{9 c _ {A} (2 t - \alpha_ {A} M) - M} \bigg) = \frac {c _ {A} M ^ {2} (3 t - \alpha_ {A} M) (2 M - 9 c _ {A} (t - \alpha_ {A} M + c))}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {2}} \\ = D _ {S N} ^ {A}   \frac {M (2 M - 2 c _ {A} (t - \alpha_ {A} M + c))}{3 (9 c _ {A} (2 t - \alpha_ {A} M) - M)} \end{array}
$$

We can show that $D _ { S N } ^ { A }$ is positive by Assumption 2 and $9 c _ { \scriptscriptstyle A } ( 2 t - \alpha _ { \scriptscriptstyle A } M ) - M > 0$ by Assumption 2-(ii). Thus, $\partial { \big / } { \partial { \big / } } { \pi _ { S N } ^ { A } } > 0$ if and only if 2M $- 9 c _ { A } ( t - \alpha _ { A } M + c ) > 0$ , which is equivalent to $\textstyle \mathcal { K } _ { A } > \frac { c + t } { M } - \frac { 2 } { 9 c _ { A } }$

(ii)

$$
\begin{array}{c} \frac {\partial}{\partial \alpha_ {A}} \boldsymbol {\pi} ^ {A} = - \frac {2 c _ {A} ^ {2} c _ {B} M ^ {2} \big (9 c _ {A} \big (2 t - M (\alpha_ {A} + \alpha_ {B}) \big) - M \big) \big (M - 9 c _ {B} + c _ {B} M (3 \alpha_ {A} + 6 \alpha_ {B}) \big) ^ {2}}{9 \big (M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B})) \big) ^ {2}} \\ - \frac {3 c _ {A} M ^ {2} \big (M - 9 c _ {B} t + c _ {B} M (3 \alpha_ {A} + 6 \alpha_ {B}) \big) \big (M (3 c _ {A} + 2 c _ {B}) - 9 c _ {A} c _ {B} (7 t - M (3 \alpha_ {A} + 4 \alpha_ {B})) \big)}{9 \big (M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B})) \big) ^ {2}} \end{array}
$$

The first term of $\scriptstyle { \frac { \partial } { \partial \alpha _ { 4 } } } \pi ^ { A }$ is negative because $9 c _ { A } \big ( 2 t - M ( \alpha _ { A } + \alpha _ { B } ) \big ) - M > 0$ and $M ( c _ { A } + c _ { B } ) - 9 c _ { A } c _ { B } \big ( 2 t - M ( \alpha _ { A } + \alpha _ { B } ) \big ) > 0$ by Assumption 2-(ii) and (v). Also by Assumption 2-(iv), $M - 9 c _ { B } + c _ { B } M ( 3 a _ { A } + 6 a _ { B } ) > 0$ . Thus, the second term is negative if

$$
M \left(3 c _ {A} + 2 c _ {B}\right) - 9 c _ {A} c _ {B} \left(7 t - M \left(3 \alpha_ {A} + 4 \alpha_ {B}\right)\right) > 0
$$

which is equivalent to $\begin{array} { r } { \alpha _ { A } > \frac { 1 } { 2 7 } \Big ( \frac { 3 6 t } { M } - 3 6 \alpha _ { B } - \left( \frac { 2 } { c _ { A } } + \frac { 3 } { c _ { B } } \right) \Big ) } \end{array}$

(iii) When $a _ { \scriptscriptstyle A } = a _ { \scriptscriptstyle B } = a$ and both firms offer the service,

$$
\begin{array}{l} \pi^ {A} = \frac {c _ {A} M (1 8 c _ {A} (t - \alpha M) - M) (M - 9 c _ {B} (t - \alpha M)) ^ {2}}{9 (M (c _ {A} + c _ {B}) - 1 8 c _ {A} c _ {B} (t - \alpha M)) ^ {2}} \\ \frac {\partial}{\partial \alpha} \pi^ {A} = D ^ {A} \frac {2 M (- c _ {A} ^ {2} (2 M ^ {2} (M - 9 c _ {B} (t - \alpha M)) + (1 8 c _ {B} (t - \alpha M) - M) + 2 7 c _ {A} c _ {B} ^ {2} M (t - \alpha M) - 2 c _ {B} ^ {2} M ^ {2}))}{9 (M (c _ {A} + c _ {B}) - 1 8 c _ {A} c _ {B} (t - \alpha M)) ^ {2}} \end{array}
$$

Therefore $\textstyle { \frac { \partial } { \partial \alpha } } \pi ^ { A } > 0$ if and only i $^ { \circ } - c _ { ^ { \prime } } ^ { 2 } \big ( 2 M ^ { 2 } \big ( M - 9 c _ { ^ { B } } \big ( t - \omega M ) \big ) + \big ( 1 8 c _ { ^ B } \big ( t - \omega M \big ) - M \big ) \big ) + 2 7 c _ { ^ A } c _ { ^ B } ^ { 2 } M \big ( t - \omega M \big ) - 2 c _ { ^ B } ^ { 2 } M ^ { 2 } > 0$ . As the coefficient of $c _ { A } ^ { 2 }$ is negative by Assumption 2-(ii) and $\begin{array} { r } { ( \mathbf { v } ) , \frac { \partial } { \partial \alpha } \pi ^ { \mathcal { A } } > 0 } \end{array}$ if and only if

$$
\frac {2 c _ {B} M}{2 7 c _ {B} (t - \alpha M) + \sqrt {8 1 c _ {B} ^ {2} (t - \alpha M) ^ {2} + 3 6 c _ {B} M (t - \alpha M) - 4 M ^ {2}}} <   c _ {A} <   \frac {2 c _ {B} M}{2 7 c _ {B} (t - \alpha M) - \sqrt {8 1 c _ {B} ^ {2} (t - \alpha M) ^ {2} + 3 6 c _ {B} M (t - \alpha M) - 4 M ^ {2}}}
$$

However, when $\begin{array} { r } { c _ { A } = \frac { M } { 1 8 \left( t - \alpha M \right) } } \end{array}$ (the lower bound of $\dot { \boldsymbol { c } } _ { A }$ given by Assumption 2-ii), $\begin{array} { r } { \frac { \ d } { \ d x } \pi ^ { A } = D _ { A } \frac { M ^ { 3 } \left( M - 9 c _ { B } \left( t - \alpha M \right) \right) } { 1 4 5 8 \left( M \left( c _ { A } + c _ { B } \right) - 1 8 c _ { A } c _ { B } \left( t - \alpha M \right) \right) ^ { 2 } } > 0 } \end{array}$ by Assumption 2-(iv). Also, if $c _ { A } = c _ { B }$ then $\begin{array} { r } { \frac { \partial } { \partial \alpha } \pi ^ { A } = D _ { A } \frac { - 4 c _ { B } ^ { 2 } \left( M - 9 c _ { B } \left( t - \alpha M \right) \right) ^ { 2 } } { 9 \left( M \left( c _ { A } + c _ { B } \right) - 1 8 c _ { A } c _ { B } \left( t - \alpha M \right) \right) ^ { 2 } } < 0 } \end{array}$

Therefore, $\textstyle { \frac { \partial } { \partial \alpha } } \pi ^ { A } > 0$ if and only if $\begin{array} { r } { c _ { A } < \frac { 2 c _ { B } M } { 2 7 c _ { B } \left( t - \alpha M \right) - \sqrt { 8 1 c _ { B } ^ { 2 } \left( t - \alpha M \right) ^ { 2 } + 3 6 c _ { B } M \left( t - \alpha N \right) - 4 M ^ { 2 } } } < c _ { B } } \end{array}$

## Proof of Proposition 8

(i) For example, in Case SN,

$$
\begin{array}{l} \frac {\partial}{\partial c _ {A}} s _ {S N} ^ {A} = \frac {\partial}{\partial c _ {A}} \frac {M (3 t - \alpha_ {A} M - c)}{9 c _ {A} (2 t - \alpha_ {A} M) - M} = - \frac {9 M (2 t - \alpha_ {A} M) (3 t - \alpha_ {A} M - c)}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {2}} = - D _ {S N} ^ {A} \frac {3 (2 t - \alpha_ {A} M)}{c _ {A} (9 c _ {A} (2 t - \alpha_ {A} M) - M)} <   0 \\ \frac {\partial}{\partial c _ {A}} \pi_ {S N} ^ {A} = \frac {\partial}{\partial c _ {A}} \left(\frac {c _ {A} M (3 t - \alpha_ {A} M - c) ^ {2}}{9 c _ {A} (2 t - \alpha_ {A} M) - M}\right) = - \frac {M ^ {2} (3 t - \alpha_ {A} M - c) ^ {2}}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {2}} <   0 \\ \frac {\partial}{\partial c _ {A}} \pi_ {S N} ^ {B} = \frac {\partial}{\partial c _ {A}} \left(\frac {M (2 t - \alpha_ {A} M) (3 c _ {A} (3 t - 2 \alpha_ {A} M + c) - M) ^ {2}}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {2}}\right) \\ = \frac {6 M ^ {2} (2 t - \alpha_ {A} M) (3 t - \alpha_ {A} M - c) (3 c _ {A} (3 t - 2 \alpha_ {A} M + c) - M)}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {3}} = D _ {S N} ^ {B} \left(\frac {6 M (2 t - \alpha_ {A} M) (3 t - \alpha_ {A} M - c)}{(9 c _ {A} (2 t - \alpha_ {A} M) - M) ^ {2}}\right) \end{array}
$$

In $\begin{array} { r } { \frac { \partial } { \partial c _ { \scriptscriptstyle A } } \pi _ { S N } ^ { B } , 3 t - \alpha _ { \scriptscriptstyle A } M - c > 0 } \end{array}$ by Assumption 2-(iv). Thus, $\begin{array} { r } { \frac { \partial } { \partial c _ { \mathcal { A } } } \pi _ { S N } ^ { B } > 0 } \end{array}$

(ii) When both firms offer the service,

$$
\begin{array}{c} \frac {\partial}{\partial c _ {A}} s ^ {A} = \frac {\partial}{\partial c _ {A}} \frac {M (M - 9 c _ {B} t + c _ {B} M (3 \alpha_ {A} + 6 \alpha_ {B}))}{3 M (c _ {A} + c _ {B}) - 2 7 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B}))} \\ = \frac {M ^ {2} (M - 9 c _ {B} t + c _ {B} M (3 \alpha_ {A} + 6 \alpha_ {B})) (9 c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B})) - M)}{3 (M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B})) ^ {2}} \end{array}
$$

By Assumption 2-(ii) and (v), the numerator of $\begin{array} { r } { \frac { \partial } { \partial c _ { A } } \boldsymbol { S } ^ { A } } \end{array}$ is positive. Thus, $\begin{array} { r } { \frac { \partial } { \partial c _ { A } } s ^ { A } > 0 } \end{array}$

$$
\begin{array}{c} \frac {\partial}{\partial c _ {A}} \pi^ {A} = \frac {\partial}{\partial c _ {A}} \Bigg (\frac {c _ {A} M \big (9 c _ {A} \big (2 t - M \big (\alpha_ {A} + \alpha_ {B} \big) \big) - M \big) \big (M - 9 c _ {B} t + c _ {B} M \big (3 \alpha_ {A} + 6 \alpha_ {B} \big) \big) ^ {2}}{9 \big (M \big (c _ {A} + c _ {B} \big) - 9 c _ {A} c _ {B} \big (2 t - M \big (\alpha_ {A} + \alpha_ {B} \big) \big) \big) ^ {2}} \Bigg) \\ = \frac {M ^ {2} \big (M - 9 c _ {B} t + c _ {B} M \big (3 \alpha_ {A} + 6 \alpha_ {B} \big) \big) ^ {2} \big (c _ {A} M + c _ {B} \big (9 c _ {A} \big (2 t - M \big (\alpha_ {A} + \alpha_ {B} \big) \big) - M \big) \big)}{9 \big (M \big (c _ {A} + c _ {B} \big) - 9 c _ {A} c _ {B} \big (2 t - M \big (\alpha_ {A} + \alpha_ {B} \big) \big) \big) ^ {3}} \end{array}
$$

$c _ { \scriptscriptstyle A } M + c _ { \scriptscriptstyle B } \big ( 9 c _ { \scriptscriptstyle A } \big ( 2 t - M \big ( \alpha _ { \scriptscriptstyle A } + \alpha _ { \scriptscriptstyle B } \big ) \big ) - M \big )$ is positive by Assumption 2-(ii). Thus, $\begin{array} { r } { \frac { \partial } { \partial c _ { A } } \pi ^ { A } > 0 } \end{array}$

$$
\frac {\partial}{\partial c _ {B}} S ^ {A} = - \frac {M (M - 9 c _ {A} t + c _ {A} M (6 \alpha_ {A} + 3 \alpha_ {B}))}{3 (M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B}))) ^ {2}}
$$

The numerator of $\begin{array} { r } { \frac { \partial } { \partial { c _ { B } } } { S } ^ { A } } \end{array}$ is positive by Assumption 2-(v). Thus, $\begin{array} { r } { \frac { \partial } { \partial c _ { B } } s ^ { A } < 0 } \end{array}$

$$
\frac {\partial}{\partial c _ {B}} \pi^ {A} = - \frac {2 c _ {A} M ^ {2} (M - 9 c _ {A} t + c _ {A} M (6 \alpha_ {A} + 3 \alpha_ {B})) (M - 9 c _ {B} t + c _ {B} M (3 \alpha_ {A} + 6 \alpha_ {B})) (9 c _ {A} (2 t - M (\alpha_ {A} + \alpha_ {B})) - M)}{9 (M (c _ {A} + c _ {B}) - 9 c _ {A} c _ {B} (2 t - M (\alpha_ {A} + \alpha_ {B}))) ^ {3}}
$$

Similarly, by Assumption 2-(ii) and (v), the numerator and denominator are positive. Thus, $\begin{array} { r } { \frac { \partial } { \partial c _ { B } } \pi ^ { A } < 0 } \end{array}$

## Reference

Li, X., and Chen. Y. 2012. “Corporate IT Standardization: Product Compatibility, Exclusive Purchase Commitment, and Competition Effects,” Information Systems Research (23:4), pp. 1158-1174.
