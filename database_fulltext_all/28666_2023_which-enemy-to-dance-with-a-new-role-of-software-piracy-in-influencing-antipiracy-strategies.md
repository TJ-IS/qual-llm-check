---
otero_id: 28666
otero_key: "JHEBU7JZ"
title: "Which Enemy to Dance with? A New Role of Software Piracy in Influencing Antipiracy Strategies"
authors: "Can Sun; Yonghua Ji; Xianjun Geng"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1219"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Which Enemy to Dance with? A New Role of Software Piracy in Influencing Antipiracy Strategies

Can Sun,<sup>a</sup> Yonghua Ji,<sup>b,</sup>\* Xianjun Geng

<sup>a</sup> International Institute of Finance, School of Management, University of Science and Technology of China, Hefei 230026, China; <sup>b</sup> School of Business, University of Alberta, Edmonton, Alberta T6G 2R6, Canada; <sup>c</sup> A. B. Freeman School of Business, Tulane University, New Orleans, Louisiana 70118

\*Corresponding author

Contacts: suncan@ustc.edu.cn, https://orcid.org/0000-0002-2013-1740 (CS); yji@ualberta.ca, https://orcid.org/0000-0001-7507-8548 (YJ); xgeng1@tulane.edu, https://orcid.org/0000-0002-9915-7096 (XG)

Received: December 10, 202 Revised: May 3, 2022; January 10, 2023 Accepted: February 14, 2023 Published Online in Articles in Advance: April 3, 2023

https://doi.org/10.1287/isre.2023.1219

Copyright: © 2023 INFORMS

Abstract. Software piracy is a challenging issue faced by software firms and governments all over the world. To control software piracy, firms exert considerable effort in antipiracy measures. This paper uses game theoretical models to study how software firms should determine their antipiracy efforts and product prices. There are two unique aspects of our model. First, antipiracy efforts have both a direct effect and a cross effect on software piracy. Second, we capture two types of competitions when piracy exists: one between a legitimate product and its pirated counterpart, and the other between two pirated products. We find several interesting results. We show that due to pirated products’ buffer effect not studied before, eliminating piracy does not necessarily mean higher profit for firms. This reveals an unexplored advantage of desktop software comparing with Software as a Service (SaaS) that can totally eliminate piracy. Direct and cross effects have different impacts on firms decisions and profits. Opposite to what one might expect, when a firm’s antipiracy effort becomes more effective in increasing the cost of pirating its own product but not its competitor’s product, the firm becomes worse off under certain conditions. By contrast, if the antipiracy effort’s cross effect is higher, therefore increasing the cost of pirating its competitor’s product, a firm will always be better off. The managerial implication is that if a firm ignores the cross effect, it could underinvest in antipiracy effort, causing its profit to suffer.

History: Karthik Kannan, Senior Editor; Amit Mehra, Associate Editor

Funding: C. Sun’s research is supported by the National Natural Science Foundation of China [Grants 72201262, 71921001]

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.1219.

Keywords: piracy • direct effect • cross effect • network effect • SaaS

## 1. Introduction

Software piracy is a serious issue all over the world. A recent report (Spajic ´ 2023) shows that unlicensed software accounts for 37% of software installed on personal computers and that software piracy costs the software industry tens of billions of dollars annually. The readily available Internet technology also makes the sharing and accessing of pirated software easier. For example, pirated software can be easily downloaded from many websites or peer-to-peer (P2P) file-sharing networks. Consequently, software piracy can hurt innovation as software firms might not have enough incentive to develop new software.

With the development of cloud computing technology, software as a service (SaaS) has become more and more popular, such as the LaTex editor Overleaf and the customer relationship management software Salesforce. In this business model, SaaS companies deliver software solutions to clients online, so it is almost impossible to pirate software provided as SaaS version. Intuitively, we may expect that there is no software piracy anymore. However, many software firms still offer a traditional desktop version, making it a potential target of software piracy that costs the software industry billions of dollars each year. This leads to our first research question which has not been explored in the literature: is there any advantage of offering a desktop version in the context of software piracy?

Facing the threat of software piracy, instead of moving to SaaS version only, software firms take other antipiracy measures. Microsoft has investigated numerous cases of software piracy and filed lawsuits against organizations and individuals (Keizer 2016, Levy 2018, Speed 2020). Siemens NX, a maker of computer-aided design (CAD) software, captured the IP addresses of illegal users through an antipiracy mechanism embedded in its software and used court orders to seek damages (Crozier 2020). Autodesk, a competing maker of CAD software, also actively uses various antipiracy measures to protect its products (Swan 2019). Furthermore, software firms have influenced many governments to take legal action to reduce piracy. In the United States, people convicted of copyright infringements could be imprisoned for up to five years and fined up to \$250,000. Repeat offenders could be imprisoned for up to 10 years and held responsible for damages or lost profits up to \$150,000 per work (U.S. Copyright Office 2011). Australia has similar legal measures (Australia Copyright Act 1968).

Although many measures on piracy control have been studied and developed in the industry and the academic research, one characteristic of antipiracy effort has been ignored for a long time: a firm’s antipiracy effort not only increases the pirating cost of its software product, but also increases the pirating cost of its competitors’ products. The effect that a firm’s antipiracy effort increases the piracy cost of its own product is called the direct effect; the effect that its effort increases the piracy cost of both firms’ products is called the cross effect. The cross effect can be generated from several sources. For example, there is web crawling technology that uses artificial intelligence to search for infringing content across the web (Das 2021). When deployed by a firm, such technology could automatically detect large volumes of pirated content that could be related to its own product and its competitor’s product. When the detected information is used by copyright enforcement specialists to eliminate pirated content, the piracy of this firm’s product could decrease, showing the direct effect of the antipiracy effort. At the same time, the piracy of its competitor’s product could also decrease, illustrating the cross effect of the antipiracy effort. Another example of antipiracy efforts having both direct and cross effects occurs when a firm seeks to block piracy websites. Such efforts could shut down websites that only contain its own pirated products, as well as websites that pirate both its own and a competitor’s products. A third example appears when a firm lobbies law enforcement agencies to allocate more resources to investigating piracy. Then the firm’s effort can benefit itself and, in some cases, benefit its competitors as well.

The distinction between direct effect and cross effect leads to the second research question we explore in this paper: how do such direct and cross effects influence firms decisions and profits differently? To address our two research questions, we build an analytical model where two firms compete with each other through antipiracy efforts and prices; users will choose whether to buy or pirate these two firms’ products according to their utility.

To be consistent with practice and the literature, our model incorporates network effects that can be generated in several ways. For example, users can get help from other users around them more easily if more people use the same product. Also, a user can search on the Internet for help. If fewer people are using the product, it is less likely that a particular question has been answered on the Internet. Also, users often post their questions to online user forums to seek answers. There, a similar situ ation happens; if more people use this software, quick feedback is more likely. Another source of network effect is that when more coworkers use the same software, it is more likely that a user can share files with them directly. In summary, the utility of a software package will be higher when more people use it.

Our model differs from previous literature in two ways. First, it captures two types of competition when piracy exists: (1) the competition between a legitimate product and its pirated counterpart and (2) the competition between two pirated products. Previous works that model piracy with competition (Shy and Thisse 1999, Jain 2008) have not studied direct competition between a legitimate product and a pirated one, and the proportion of piracy demand is assumed to be given. In our model, a pirated product can seize more legitimate demand when the antipiracy effort is low. Second, we capture a phenomenon that has not been studied before: antipiracy effort can have both direct and cross effects in practice.

We obtained several interesting results. When the quality of pirated software is not so high compared with the legitimate version, software firms benefit from the existence of piracy in equilibrium. In other words, software firms could be worse off if they totally elimi nate piracy by using measures such as moving to the SaaS model only. This answers our first research question. With regard to the second research question, we find that the direct and cross effects of antipiracy effort could impact the firm’s profit differently. On the one hand, when the direct effect increases, that is, a firm is more efficient in combating the piracy of its own prod uct, the firm might not benefit from such an increase, and its profit could decrease instead. On the other hand, when the cross effect increases, making it more costly to pirate both a firm’s and its competitor’s products, each firm will always benefit. From the firm’s perspective, it is always better to have new antipiracy technology that targets both firms’ pirated products.

The rest of the paper is organized as follows. Section 2 reviews the related literature and Section 3 builds an analytical model. In Section 4, we analyze the model and obtain the main results of this paper. We study social welfare and consumer surplus in Section 5. In Section 6, we extend our model to the rational expectation case. We conclude the paper in Section 7.

## 2. Literature Review

Our paper mainly relates to digital piracy. We classify the related literature into three streams: piracy control, piracy impacts on product design, and positive effects of piracy.

The first stream of literature investigates how a firm can control piracy. Chen and Png (2003) explore how a monopolistic firm should set both prices and spending levels on detection when a government sets the cost of piracy. Sundararajan (2004) investigates how a firm should choose the optimal pricing schedules and technological deterrence level when piracy can be influenced by implementing digital rights management (DRM) systems. Jain (2008) finds that strong network effect intensity may lead to higher levels of copyright protection in some cases because stronger copyright enforcement can lead to reduced price competition. Harm and Oh (2017) investigate the dynamics of demand and supply of piracy since the early stages of digital music release. They find that controlling the demand for pirated products is as effective as controlling the supply of those products. Herings et al. (2017) use a dynamic stochastic model to determine the optimal pricing policy of music recordings when P2P file-sharing (piracy) exists. They find that if a music firm exerts a large effort to fully enforce intellectual property rights, then user surplus and total welfare decrease. Dey et al. (2019) use a simple economic model to discover the difference in impacts between supply-side enforcement and demand-side enforcement on innovation and social welfare. They find that, in the long run, supply-side enforcement will have a more desirable economic impact. Koh et al. (2019) investigate demand migration in the music industry. They find that the introduction of licensed digital downloads can weaken piracy, and the introduction of streaming music can further weaken piracy. Sivan et al. (2019) study whether removing infringing links can decrease the infringing content consumption. They find that more users would choose the legitimate content if the infringing links are removed, and the cost of discovering pirated content can affect user behavior to a large degree. Our paper differs from the above research in that we consider both the direct and cross effects of antipiracy effort that have different impacts on firms’ decisions and profits.

The second stream of literature studies the impact of piracy on product design and the range of offerings. Wu and Chen (2008) find that when there is no piracy, a single version is the optimal strategy for an information goods provider. However, when piracy exists, such providers tend to offer more than one version; this versioning strategy is an effective and profitable instrument to fight piracy under some conditions. August and Tunca (2008) consider whether a software firm should allow pirating users to update with security patches. They find that if the piracy tendency is low, then the firm’s software security patch restriction is optimal only when the piracy enforcement level is high. When patching costs are sufficiently low, an unrestricted patch release policy by the firm can maximize its profit. Johar et al. (2012) investigate a firm that gains profit through advertisements when providing content to users. The firm needs to determine two dimensions, the content quality and content distribution delay, in its content provision strategy. They find that when piracy exists, the firm should improve on at least one dimension of content provision. Lahiri and Dey (2013) find that when piracy enforcement is lower, a monopolist firm has more incentive to invest in quality in certain situations. Our paper focuses on the impact of piracy on pricing and antipiracy investment decisions. We find that firms can tolerate piracy in some cases because the existence of piracy can soften price competition and increase firm profits.

The third stream of literature studies the positive effect of piracy on profit. Conner and Rumelt (1991) incorpo rate network effects into the model and examine piracy’s effect on a software firm’s profit. When more people use the software, either the legitimate or the pirated version, users can gain higher utility and are willing to pay more for the product. They find that if the network effect is large, then firms can benefit from piracy. Shy and Thisse (1999) extend the monopoly results of Conner and Rumelt (1991) to a duopoly framework. They show that software firms will allow piracy (i.e., not combat it intensely) to increase the market size. If network effects are strong, then firms can benefit from not exerting effort on antipiracy measures. Prasad and Mahajan (2003) shows that piracy can facilitate the diffusion of a firm’s product, so the firm should tolerate piracy early in prod uct introduction. Curien et al. (2004) find piracy has a positive effect through the sales of ancillary products. Ben-Shahar and Jacob (2004) shows that a firm may allow piracy to keep the market small for a potential entrant, so that the new entrant has no motivation to enter the market. Chellappa and Shivendu (2005) show that it is helpful for a firm to use piracy as a consumer sampling of the product. Tunca and Wu (2013) explore the effects of suing file-sharing P2P networks or users who share copyrighted material on the P2P network; such action can turn out to hurt legitimate firms which sell information goods. Kim et al. (2018) investigate piracy’s economic impact on the information goods sup ply chain. They find that a moderate level of piracy could positively impact the manufacturer’s and retailer’s prof its and increase user welfare. Lu et al. (2020) find that in the prerelease piracy case, although the word-of-mouth effect exists, piracy is associated with lower revenue, whereas postrelease piracy is associated with higher revenue. We contribute to this stream of research by con sidering an unexplored role of software piracy. In a duopoly setting where there is competition among two legitimate products and two pirated ones, we find that the existence of pirated products can reduce the intensity of competition and therefore increase each firm’s profit.

## 3. Model

We consider a one-period model where two software firms sell substitutable software, labeled as Product 1 and Product 2, respectively. These two firms are located at the endpoints of a unit Hotelling line. We assume that individual demand is uniformly distributed on the Hotelling line. Total demand is normalized to be one. Following the literature on information goods (Lahiri and Dey 2013, Chellappa and Mehra 2018), we assume the marginal cost of producing an extra copy of each product is zero. When a desktop version is offered, each product will have a pirated version. Table 1 contains the notation used in this paper.

## 3.1. Users’ Decision Making

As is usually done in the literature (Jain 2008, Geng and Shulman 2015, Xin and Choudhary 2019, Mehra et al. 2020), we make the following assumptions in the main model. First, we assume two firms are symmetric to simplify the analysis and rule out the possibility of the main results being caused by differences in firms’ characteristics such as quality or unfitness cost. We check the robustness of the model in Online Appendix P. There, we numerically investigate the case where two legitimate products have different qualities, and the main results still hold. Second, we assume full market coverage in our model so that we can study the impact of competition on firms’ decisions. Without full market coverage, two firms become local monopolists and the result is given in Lemma 1. Specifically, the quality of each product is assumed to be sufficiently large (Online

Table 1. Summary of Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td> $q$ </td><td>Quality of legitimate product</td></tr><tr><td> $\theta$ </td><td>Discount factor of pirated product relative to a legitimate Version</td></tr><tr><td> $k$ </td><td>Network effect intensity</td></tr><tr><td> $r$ </td><td>Coefficient of antipiracy effort cost</td></tr><tr><td> $x$ </td><td>A user&#x27;s location on the Hotelling line</td></tr><tr><td> $t$ </td><td>Unit mismatch cost</td></tr><tr><td> $a$ </td><td>Antipiracy effort&#x27;s direct effect efficiency</td></tr><tr><td> $b$ </td><td>Antipiracy effort&#x27;s cross effect efficiency</td></tr><tr><td> $\delta$ </td><td>Degree of overlapping between efforts</td></tr><tr><td colspan="2">Intermediate variables</td></tr><tr><td> $\pi_j$ </td><td>Profit of software firm  $j$  ( $j=1,2$  in this table)</td></tr><tr><td> $U_j$ </td><td>Users&#x27; utility of using  $j$ th legitimate product product</td></tr><tr><td> $U_{2+j}$ </td><td>Users&#x27; utility of using  $j$ th pirated software product</td></tr><tr><td> $D_j$ </td><td>Demand for legitimate product  $j$ </td></tr><tr><td> $D_{2+j}$ </td><td>Demand for pirated product  $j$ </td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $p_j$ </td><td>Price of product  $j$ </td></tr><tr><td> $e_j$ </td><td>Antipiracy effort exerted by software firm  $j$ </td></tr></table>

Appendix A formalizes this constraint on q together with other constraints for piracy to exist):

Assumption (Full Market Coverage). The product quality should not be too small, that is, $\begin{array} { r } { q > \frac { t - k } { 2 } . } \end{array}$

Under the assumption of full market coverage, a user can take one of the following four actions: buying Product 1 or 2 or pirating Product 1 or 2. For a user located at x, the utility of buying Product 1 is given by

$$
U _ {1} = q - t x + k (D _ {1} + D _ {3}) - p _ {1},\tag{1}
$$

where t is the unit mismatch cost and k is the network effect intensity. Also $D _ { 1 }$ and $D _ { 3 }$ are the demands for legitimate Product 1 and its pirated version, respectively. Similarly, the utility of buying Product 2 for a user located at x is given by

$$
U _ {2} = q - t (1 - x) + k (D _ {2} + D _ {4}) - p _ {2},\tag{2}
$$

where $D _ { 2 }$ and $D _ { 4 }$ are the demands for legitimate Product 2 and its pirated version, respectively.

We next model consumer utility of using the pirated products, starting with a survey finding that about 84% of respondents acknowledge the missing key features and functionality in pirated software (Microsoft 2012). In the case of Adobe Photoshop, a powerful photo editing software product, its pirated version does not have certain features such as the creative cloud one (Clipping Panda 2022). Another example is Grand Theft Auto (GTA) V, a popular video game. Comparing with the legitimate version, the pirated version misses the big YouTubers mod (Chakraborty 2021). Also, software firms constantly create new fea tures and add-ons for their products as upgrades. These upgrades might be available for legitimate versions only. For instance, Mathematica, a technical computing software product, has added more than 100 functions from version 12.2 to 12.3 and 117 new functions from version 12.3.1 to version 13 (Wolfram 2022). Adobe Photoshop has added new features and enhancements in the April 2022 release of Photoshop desktop (version 23.3; Adobe 2022). GTA V also got updates to “change physics, added new textures, and many more” (Chakraborty 2021, p. 1).

We can see from the previous examples that, compared with a user of a legitimate product, a user of its pirated version can only use a part of the product’s features. Then the quality of the pirated version and its network effect is discounted. Also, because software pirates, who use pirated software, do not have misfit cost for the features missing from a pirated version, the misfit cost is lower for pirated products. Furthermore, with the new updates mentioned previously, legitimate users need to learn these features, and their misfit cost increases. At the same time, a software pirate’s misfit cost does not change because the number of features in a pirated version remains the same.

For the previous two reasons, we discount a pirated version’s misfit cost in this work, as in the piracy literature such as Jain (2008). We use a single discount factor θ to represent the percentage of quality, mismatch cost, and network effect associated with the pirated products, relative to the legitimate version (our main results and insights would still apply with different discount factors). Accordingly, the utility of a user located at x who uses the pirated version of Product 1 is

$$
U _ {3} = \theta [ q - t x + k (D _ {1} + D _ {3}) ] - c _ {1} (e _ {1}, e _ {2}).\tag{3}
$$

In Equation (3), the term $c _ { 1 } ( e _ { 1 } , e _ { 2 } )$ represents the cost of using the pirated Product 1. This cost $c _ { 1 } ( e _ { 1 } , e _ { 2 } )$ is not only a function of Firm 1’s antipiracy effort $e _ { 1 }$ but also Firm $2 ^ { \prime } \mathrm { s }$ effort $e _ { 2 } .$ . The connection is due to a cross effect of antipiracy efforts: when Firm 2 exerts effort, the cost of using Firm 1’s pirated product will also increase, as discussed in detail in the introduction section. In particular, we assume a linear form

$$
c _ {1} (e _ {1}, e _ {2}) = (a + b) e _ {1} + (1 - \delta) b e _ {2}\tag{4}
$$

to simplify the model. In the cost function, a represents the direct effect of antipiracy effort that only increases the piracy cost of its own product. Parameter b represents the effect due to the part of the antipiracy effort that increases the piracy costs of both firms’ products. Parameter δ measures the degree of overlapping in antipiracy efforts between two firms. Then $( 1 - \delta ) b e _ { 2 }$ represents Firm 2’s antipiracy effort on the piracy cost of Firm 1’s product. The value of δ decreases when two firms target different areas of piracy activities to a higher degree. In this paper, we assume $0 \leq \delta < 1$

Similarly, the utility of a user located at x who uses the pirated version of Product 2 is given by

$$
U _ {4} = \theta [ q - t (1 - x) + k (D _ {2} + D _ {4}) ] - c _ {2} (e _ {1}, e _ {2}),\tag{5}
$$

where

$$
c _ {2} (e _ {1}, e _ {2}) = (1 - \delta) b e _ {1} + (a + b) e _ {2}.\tag{6}
$$

In Online Appendix ${ \mathrm { R } } ,$ we consider alternative cost functions $c _ { 1 } ( e _ { 1 } , e _ { 2 } ) = a e _ { 1 } + b e _ { 2 }$ and $c _ { 2 } ( e _ { 1 } , e _ { 2 } ) = b e _ { 1 } + a e _ { 2 }$ . We find that all results hold.

## 3.2. Firms’ Decision Making

The profits of the two firms are given by

$$
\pi_ {j} (p _ {j}, e _ {j}) = p _ {j} D _ {j} - r e _ {j} ^ {2}, j = 1, 2,\tag{7}
$$

where $p _ { j } , D _ { j } ,$ and $e _ { j }$ are, respectively, the price, demand, and antipiracy effort for Product $ j , j = 1 , 2$ . Each firm chooses a price and effort to maximize its profit. We assume that the cost of Firm $j ^ { \prime } \mathrm { s }$ effort is a quadratic function of effort, denoted as $r e _ { j } ^ { 2 }$ . This formulation captures the property that when the effort $e _ { j }$ increases, the cost will increase and the marginal cost of $e _ { j }$ will also increase. More specifically, as a firm puts more effort into developing an antipiracy system or shutting down software piracy websites, the antipiracy system becomes more sophisticated or more piracy websites have been shut down. Then it becomes more difficult to add new functionalities to the system or find additional piracy websites to shut down. The quadratic function is the simplest form to model the idea of a higher marginal cost of adding one additional functionality or shutting down one more piracy website when antipiracy effort is higher.

The decision time sequence of firms in this model is as follows. In the first stage, both firms simultaneously decide their antipiracy efforts $e _ { 1 }$ and $e _ { 2 } .$ . In the second stage, both firms simultaneously decide the prices $p _ { 1 }$ and $p _ { 2 } .$ In the third stage, users choose which product to obtain and whether to buy or pirate it. We assume that antipiracy effort decisions are made before pricing decisions, because firms can easily adjust product prices but not antipiracy effort.

An explanation of the cost forms of software piracy and antipiracy effort is in order here. When software pirates use Firm 1’s pirated product for example, they incur the piracy cost $\bar { c } _ { 1 } ( e _ { 1 } , e _ { 2 } ) \bar { = } ( a + b ) e _ { 1 } + ( 1 - \bar { \delta } ) b e _ { 2 }$ given in Equation (4). Although the impacts of the antipiracy efforts $e _ { 1 }$ and $e _ { 2 }$ on piracy cost $c _ { 1 } ( e _ { 1 } , e _ { 2 } )$ are linear, their costs (see Equation $( \bar { 7 } ) ) , r e _ { i } ^ { 2 } , i = 1 , 2 ,$ , are not. Such a linear quadratic framework allows one to obtain interior solutions analytically and has also been used to model the impact of IT investment on product quality and produc tion cost (Demirhan et al. 2007, Xin and Choudhary 2019).

## 4. Analysis

In Section 4.1, we first characterize the conditions and outcomes of two Nash equilibria under the threat of piracy: four-product case and two-product case. Section 4.2 answers the question of why some software firms tolerate piracy even when they can eliminate piracy by providing a SaaS version only. Section 4.3 analyzes how parameters such as the direct and cross effects of antipiracy effort affect antipiracy efforts, product prices, and firm profits.

## 4.1. Nash Equilibria Under the Threat of Piracy

We first study one product’s case where a user chooses to pirate, buy, or not use the product based on the user’s mismatch cost (i.e., the location on the Hotelling line). This will serve as the basis of analysis in the two firm case. Lemma 1 describes the optimal choices when both a legitimate product and a pirated version exist (see the appendices for all the proofs of lemmas and propositions). We also depict the results of Lemma 1 graphically in Figure 1.

Lemma 1. For a product located at zero, users with low mismatch cost will buy the product, users with medium mismatch cost will pirate, and users with high mismatch cost will not use the product.

Figure 1. User Choices on the Hotelling Line  
![](/api/attachments/JHEBU7JZ/fulltext/images/20ff6e9a646ba86f7a9ccd098f6d441bb12fdb50d3577dad90969d545dba56c1.jpg)

The results of Lemma 1 are due to the difference in unit mismatch cost. The pirated product has a lower effective unit mismatch cost (represented by θt). Therefore, for a user whose ideal location (x) is further away from the location of the legitimate product, pirating the product is a better choice than buying because the reduction in mismatch cost (1 � θ)x is higher.

Next, we study the case of two symmetric firms with symmetric equilibria and full market coverage. We first investigate the case of competition among four products (two legitimate and two pirated products). Figure 2 depicts the user choices and user demand in this case.

We use backward induction to solve the Nash equilibrium according to the decision sequence given in Section 3.2. In Stage 3, users make their decisions to buy or pirate to maximize their utilities, as shown in Figure 2. Variables $x _ { 1 } , x _ { 2 } ,$ and $x _ { 3 }$ represent the indifference points. For a user located at $x _ { 1 } ,$ the utility $U _ { 1 }$ of using the legitimate Product 1, given by Equation (1), equals the utility $U _ { 3 }$ of pirating Product 1, given by Equation (3). That is,

$$
U _ {1} | _ {x = x _ {1}} = U _ {3} | _ {x = x _ {1}}.\tag{8}
$$

$\mathrm { A t } x = x _ { 3 } ,$ , the utility $U _ { 2 }$ of using the legitimate Product 2, given by Equation (2), equals the utility $U _ { 4 }$ of pirating Product 2, given by Equation (5). That is,

$$
U _ {2} | _ {x = x _ {3}} = U _ {4} | _ {x = x _ {3}}.\tag{9}
$$

At $x = x _ { 2 } ,$ , the utility $U _ { 3 }$ of pirating the legitimate Product 1 equals the utility $U _ { 4 }$ of pirating Product 2. That is,

$$
U _ {3} | _ {x = x _ {2}} = U _ {4} | _ {x = x _ {2}}.\tag{10}
$$

We also have $D _ { 1 } + D _ { 3 } = x _ { 2 } , D _ { 2 } + D _ { 4 } = 1 - x _ { 2 } , D _ { 1 } = x _ { 1 } ,$ and $D _ { 2 } = 1 - x _ { 3 }$ . Together with Equations (8)–(10), we can obtain $x _ { 1 } , x _ { 2 } ,$ , and $x _ { 3 } ,$ .

The firms’ decisions about $e _ { j }$ and $p _ { j } \ ( j = 1 , \ 2 )$ are made in the first and second stages to maximize their own profits, given by Equation (7). We can find the equilibrium solutions of $e _ { j } ^ { * }$ and $p _ { j } ^ { * }$ through backward induction. To ensure that the result is a Nash equilibrium, we need the following assumption (the expressions of $\theta _ { m }$ can be found in Online Appendix C).

Assumption (Large Discount Factor). The quality discount factor of pirated software θ is large enough: $\theta > \theta _ { m }$

We need this assumption for the following reason. When the quality discount factor θ is large enough, the pirated product will be attractive so that the case of four-product competition can exist. Otherwise, the pirated product is not attractive, and it is beneficial for a firm to lower its price and eliminate the demand for the pirated product while increasing the demand for the legitimate product.

We first present the Nash equilibrium of the fourproduct competition case, that is, demands for both legitimate and pirated products are positive.

Lemma 2 (Equilibria of Four-Product Competition). When the antipiracy effort cost r is large enough $( r \geq r _ { m } )$ , there is an equilibrium that has both legitimate and pirated products in the market. In this equilibrium, the product prices are

$$
p _ {1} = p _ {2} = p ^ {*} \equiv \frac {2 (1 - \theta) ^ {2} \theta r t (k + 2 q) (t - k)}{B};\tag{11}
$$

the antipiracy efforts are

$$
e _ {1} = e _ {2} = e ^ {*} \equiv - \frac {A (1 - \theta) (k + 2 q)}{2 B};\tag{12}
$$

the legitimate product demands are

$$
D _ {1} = D _ {2} = D ^ {*} \equiv \frac {2 (1 - \theta) \theta r (k + 2 q) (t - k)}{B};\tag{13}
$$

the pirated product demands are

$$
D _ {3} = D _ {4} = \frac {1}{2} - D ^ {*};\tag{14}
$$

and the profits are

$$
\pi_ {1} = \pi_ {2} = \pi^ {*} \equiv \frac {(1 - \theta) ^ {2} r (k + 2 q) ^ {2} (1 6 (1 - \theta) \theta^ {2} r t (t - k) ^ {2} - A ^ {2})}{4 B ^ {2}}.\tag{15}
$$

The expressions of A, B, and $r _ { m }$ are defined in Online Appendices A and C.

As we can see from Lemma 2, when the antipiracy effort cost r is large enough, piracy will exist because the antipiracy effort will not be too high, and therefore piracy cost is low enough. Next we consider the condition under which the antipiracy effort cost r is small enough. As we will see, this leads to a two-product competition case in which piracy is driven out of the market by firms (Figure 3). Let $x _ { 4 }$ be the indifference point such that the utilities of buying Product 1 and buying Product 2 for the user located at $x = x _ { 4 }$ are the same. That is,

Figure 2. Product Demands in the Case with Piracy  
![](/api/attachments/JHEBU7JZ/fulltext/images/c020fae1d1ef486a4d078e5a3e6c96d64eb01f7e04eec5026177f24aecf5df94.jpg)

$$
U _ {1} | _ {x = x _ {4}} = U _ {2} | _ {x = x _ {4}}.\tag{16}
$$

$\mathrm { A t }$ the same time, for a user to buy the product instead of pirating the product at the indifference point, we have

$$
U _ {1} | _ {x = x _ {4}} > U _ {3} | _ {x = x _ {4}}\tag{17}
$$

and

$$
U _ {4} | _ {x = x _ {4}} <   U _ {2} | _ {x = x _ {4}}.\tag{18}
$$

Then we have the following lemma regarding the equilibrium of two-product competition.

Lemma 3 (Equilibria of Two-Product Competition). When the cost of antipiracy effort is smal $\left( r < r _ { b } \right)$ , two-product competition without piracy reaches a stable equilibrium. We have the following two cases: Case 1 when the pirated product’s quality is small $\left( \theta < \theta _ { 1 } \right)$ , and Case 2 when the pirated product’s quality is not small $\left( \theta > \theta _ { 1 } \right)$ . In equilibrium, the product prices are $p _ { 1 } = p _ { 2 } = p _ { b } \equiv t - k ,$ the legitimate demands are $D _ { 1 } = D _ { 2 } = 1 / 2 ,$ , and the piracy demands are $D _ { 3 } = D _ { 4 } = 0$ . Also, in Case 1, the antipiracy efforts are $e _ { 1 } = e _ { 2 } = 0$ , and the product profits $\begin{array} { r } { \pi _ { 1 } = \pi _ { 2 } \equiv \pi _ { b } = \frac { t - k } { 2 } ; } \end{array}$ ; in Case 2, $\begin{array} { r } { e _ { 1 } = e _ { 2 } = \frac { ( 3 - \theta ) ( t - k ) - 2 ( 1 - \theta ) q } { 2 ( a + b ( 1 - \delta ) + b ) } } \end{array}$ and $\begin{array} { r } { \pi _ { 1 } = \pi _ { 2 } \equiv \pi _ { b } = \frac { t - k } { 2 } } \end{array}$ $\begin{array} { r l r } { - \frac { r ( ( 3 - \theta ) ( t - k ) - 2 ( 1 - \theta ) q ) ^ { 2 } } { 4 ( a + b ( 1 - \delta ) + b ) ^ { 2 } } } \end{array}$ . The expressions $\theta _ { 1 }$ and $r _ { b }$ are defined in Online Appendix D.

In Lemma 2, we see that firms will allow piracy if it is difficult to prevent it; that is, if the quality of the pirated product is high and the cost of preventing piracy is also high. By contrast, Lemma 3 shows that firms will choose to eliminate piracy if the effort cost r is small enough. However, when there is no piracy, the legitimate products may still face a threat from the pirated products. We find two possible equilibria of no piracy, one with antipiracy effort and the other without. In the first equilibrium, when the pirated product quality is small $\left( \theta < \theta _ { 1 } \right)$ , the pirated product is not so attractive. Even though firms do not exert antipiracy efforts, all users choose to purchase legitimate products. In the second equilibrium, when the pirated product quality is not too small $\left( \theta > \theta _ { 1 } \right)$ , if a firm does not exert antipiracy effort, some users wil choose the pirated products. The firms exert a sufficiently large antipiracy effort to prevent piracy in this equilibrium, leading to an interesting result: There is no piracy in the market, but the firms still exert antipiracy effort.

By using the equilibrium results from Lemma 2 and Lemma $^ { 3 , }$ we can obtain the conditions when the equi librium can switch from the four-product competition case to the two-product competition case. Consistent with previous works (Ortega 2000, Wang et al. 2019), we use Pareto improvement criteria to choose from candidate equilibria the one that makes both firms better off. The results are shown in the following proposition.

Proposition 1 (Equilibria Under Pareto Improvement Criteria). In the region where the pirated software quality is not so large $\left( \theta < \theta _ { n } \right) .$ , there is a threshold value $r _ { m } .$ When $r > r _ { m } ,$ , in equilibrium, legitimate products compete against their own pirated products and the equilibrium outcomes are described in Lemma 2. When $r \leq r _ { m } ,$ , in equilibrium, two legitimate products directly compete against each other, and the equilibrium outcomes are described in Lemma 3.

## 4.2. Impact of Piracy on Firm Profits

In this section, we compare the cases of offering desktop and SaaS versions and show a novel benefit of offering desktop software due to the existence of software piracy.

We first study the case where software firms provide the SaaS version only. To focus on the effect of piracy on firms’ decisions, we assume that comparing with the desktop version, there is no additional cost of providing the SaaS version. Also the software quality and consumer distribution are assumed to remain the same. Then under these assumptions, the difference between the desktop software case and the SaaS case is purely caused by the existence of piracy.

In the case of firms providing SaaS version only, piracy is eliminated from the market and two legitimate products compete against each other. We can derive firm profits and product prices in the following lemma. (When there is marginal cost of offering SaaS software, both firms increase equilibrium prices by the marginal cost and the profits remain the same.)

Lemma 4. In the SaaS model case, we have $p _ { 1 } = p _ { 2 } = t - k ,$ and $\begin{array} { r } { \pi _ { 1 } = \pi _ { 2 } = \frac { t - k } { 2 } } \end{array}$

By comparing a firm’s profit in the traditional desktop software case (Proposition 1) with that in the SaaS case (Lemma 4), we can obtain the condition when a firm will be better off when tolerating piracy in the following proposition.

Figure 3. User Demands in the Duopoly Case Without Piracy

<table><tr><td rowspan="2">Consumer choice:0</td><td colspan="2">Buy product 1</td><td colspan="2">Buy product 2</td></tr><tr><td>D1</td><td>x4</td><td>D2</td><td>1</td></tr></table>

Proposition 2. In the region where antipiracy cost is large $( r > r _ { m } )$ and pirated software quality is not so large $\left( \theta < \theta _ { 3 } \right)$ , firms benefit from tolerating piracy. The expressions $r _ { m }$ and $\theta _ { 3 }$ are defined in Online Appendices C and E.

Proposition 2 shows a surprising finding: tolerating piracy in certain situation can make firms better off; in such a situation, firms will not adopt the SaaS model. Figure 4 shows the relevant profits in Proposition 2. From the figure, we see that when piracy is tolerated $( r > r _ { m } ) .$ , firms’ profits are always higher than those in the no piracy case. We can explain the result from the role of a pirated product. Demand loss to a pirated product will hurt a firm less than the same amount of demand loss to a competitor will. The reason is that a firm can still benefit from the network effect due to the existence of the pirated product of its legitimate version, but it cannot benefit from its competitor’s network. Therefore, the competition between a legitimate product and its pirated version is not as intensive as the direct competition between two legitimate products. As a result, the existence of piracy mitigates product price competition and equilibrium prices increase (Figure 5). In other words, pirated products act as a buffer to mitigate the intensive direct competition between two legitimate products. The buffer effect shows that if the direct competition between firms is too intensive, firms may be better off by tolerating piracy to reduce the intensity of competition when a pirated product is not very attractive, that is, θ is not so large $\left( \theta < \theta _ { 3 } \right)$

Figure 4. (Color online) Impact of r on Firm Profits When θ is Not So Large $( k = 0 . 9 2 , \stackrel { \cdot } { q } = \frac { 1 } { 7 } , t = 1 , \theta = 0 . 5 5 , a = \frac { 1 } { 4 } , b = 2 ,$ δ � 0:05)  
![](/api/attachments/JHEBU7JZ/fulltext/images/eaa338315c71d1d817338bf5494ebcc0e7736d99f38edf2997eeb39c28fc9fe1.jpg)

Figure 5. (Color online) Impact of r on Firms’ Prices When θ is Not So Large $( k = 0 . 9 2 , \stackrel { \cdot } { q } = \frac { 1 } { 7 } , t = 1 , \theta = 0 . 5 5 , a = \frac { 1 } { 4 } , b = 2 ,$ $\delta = 0 . 0 5 )$  
![](/api/attachments/JHEBU7JZ/fulltext/images/c604cf2c0e679c37380806abd0428e6db3bb75fbf921ebf19fe5a7b320e36762.jpg)

When θ is large enough $\left( \theta \geq \theta _ { 3 } \right)$ , the competition between the pirated product and the legitimate product will be intensive. We find that the price in the four-product competition case is less than that in the two-product case. That is, piracy intensifies competition (Figure 6(a)). Then firms’ profits in the SaaS case are higher than those in the desktop case (Figure 6(b)). Therefore when a pirated product is attractive, firms have motivation to move from the desktop model to the SaaS model.

In appendices, we show that the buffer effect is robust to two model variants. In Online Appendix O, we study an asymmetric equilibrium where one firm chooses the desktop version, while the other chooses the SaaS version. We find that in this equilibrium, pirated software of the desktop version exists. In other words, piracy can still act as a buffer in this asymmetric equilibrium. In Online Appendix S, we numerically study the synergy effect of antipiracy efforts and our key finding of the buffer effect still exists.

Past research has studied the benefit of piracy from perspectives such as network effect (Conner and Rumelt 1991), reducing commercial piracy by allowing noncommercial piracy for personal use (Tunca and Wu 2013) and mitigating double marginalization within a supply chain (Kim et al. 2018). One contribution of our paper is that we discover a previously unexplored buffer mechanism brought by piracy.

To support this finding of the buffer effect, we have gathered several pieces of anecdotal evidence. Recall that, the relative quality of the pirated software is measured by how many functionalities it is missing as compared with the legitimate version: The more it is missing, the lower the quality of the pirated software. One strong piece of anecdotal evidence we find is a survey (Microsoft 2012) that finds that the vast majority of the respondents, about 84% to be exact, acknowledge that pirated software they use indeed misses key features and functionalities. This shows that the coexistence of legitimate and pirated versions of software (with low quality) is a rather common phenomenon for desktop software. In addition, previous examples in Section 3.1 illustrate that pirated software could miss key features: in the case of Adobe Photoshop, its pirated version does not have Creative Cloud, a key feature in this product (Clipping Panda 2022); in the case of GTA V, the pirated version misses the fan-favorite You-Tubers mods (Chakraborty 2021).

(b)  
Figure 6. (Color online) Impacts of r When θ is Large $( k = 0 . 9 2 , q = \textstyle { \frac { 1 } { 7 } } , t = 1 , \theta = 0 . 8 5 , a = \textstyle { \frac { 1 } { 4 } } , b = 2 , \delta = 0 . 0 5 )$  
(a)  
![](/api/attachments/JHEBU7JZ/fulltext/images/04162205676e3be409c2961e7f03d9a6617c48202ba6e406b8719e7184d01a4e.jpg)

![](/api/attachments/JHEBU7JZ/fulltext/images/682dfa0d18cc98398cb6a75c9dd0733032bd112face691b00755853d4d1a2afa.jpg)

## 4.3. Comparative Statics Analysis in the Case of Four-Product Competition

In this section, we analyze how the direct and cross effects of antipiracy effort and other parameters affect firms’ antipiracy efforts, prices, and profits. Because the case of no piracy is relatively straightforward, we will focus on the more interesting case in which piracy exists, that is, $r > r _ { m }$ and $\theta > \theta _ { m }$ according to Lemma 2. To simplify the discussion, we assume the effect cost r is sufficiently large for all propositions in this section.

With regard to the direct effect $a ,$ we have the following results.

Proposition 3. When the antipiracy effort cost r is large, the following hold:

(1) The antipiracy efforts increase with the direct effect a when k is small and decrease with a when k is large; that $i s ,$ there is a threshold value $\begin{array} { r } { k _ { 1 } \colon \frac { \partial e ^ { * } } { \partial a } > 0 } \end{array}$ for $0 < k < k _ { 1 }$ and $\frac { \partial e ^ { * } } { \partial a } <$ 0 for $k _ { 1 } < k < \overline { { k } }$

(2) The product prices increase with a when k is small and decrease with a when k is large; that is, there is a threshold value $\begin{array} { r } { k _ { 2 } { : } \frac { \partial p ^ { * } } { \partial a } > 0 f o r 0 < k < k _ { 2 } a n d \frac { \partial p ^ { * } } { \partial a } < 0 f o r k _ { 2 } < k < \overline { { k } } } \end{array}$

(3) The firm profits increase with a when k is small and decrease with a when k is large; that $i s ,$ there is a threshold value $\begin{array} { r } { k _ { 3 } ; \frac { \partial \pi ^ { * } } { \partial a } > 0 f o r 0 < k < k _ { 3 } \overline { { a n d \frac { \partial \pi ^ { * } } { \partial a } } } < 0 f o r k _ { 3 } < k < \overline { { k } } . } \end{array}$

We have $k _ { 1 } < k _ { 2 }$ and $k _ { 1 } < k _ { 3 }$ . The expressions of $k _ { 1 } , k _ { 2 } ,$ $k _ { 3 } ,$ and $\overline { { r } } _ { 1 }$ are defined in Online Appendix H.

We can understand the results of Proposition 3 through the effects of a pirated product. First, the competition between a pirated product and the corresponding legiti mate product reduces the demand for the legitimate product. This is the pirated product’s cannibalization effect. Second, the existence of the pirated product can increase the total demand, leading to an increase in network effects. We call this the demand expansion effect. When a firm exerts an antipiracy effort, it will weaken both the cannibalization and demand expansion effects (Figure 7) by reducing the utility of using this firm’s pirated product. Then the demand for this firm’s legitimate product increases. At the same time, this firm’s total demand decreases as some users switch from this firm’s pirated product to its competitor’s pirated product.

When the antipiracy effort’s direct effect a increases, the cannibalization effect decreases. Then the benefi of antipiracy effort increases for a fixed antipiracy effort. At the same time, the demand expansion effect also decreases, weakening the benefit of the antipiracy effort. On the one hand, in the region where the network effect intensity is small $( 0 < k < k _ { 1 } ) .$ , the reduction of cannibalization effect dominates that of demand expansion effect, causing the marginal benefit of antipiracy effort to increase. Thus, a firm will increase its antipiracy effort if the other firm’s effort remains the same. When the other firm’s antipiracy effort also increases as a increases, this firm’s total demand increases. As a result, this firm’s demand expansion effect increases, lessening the negative effect of its antipiracy effort and leading it to further increase its antipiracy effort. Therefore, both firms increase antipiracy efforts. On the other hand, when the network effect intensity is large $( k > k _ { 1 } )$ , if the direct effect a becomes stronger, the demand expansion effect decreases more than the cannibalization effect does. Then the marginal benefit of the antipiracy effort will be less than the marginal cost of the antipiracy effort, so both firms will decrease their antipiracy efforts.

Figure 7. Impact of Firm 1’s Antipiracy Effort on its Demand

<table><tr><td rowspan="2">Consumer choice:</td><td rowspan="2">0</td><td colspan="2">cannibalization effect weaken</td><td colspan="2">demand expansion effect weaken</td><td>1</td></tr><tr><td>D1</td><td>x1</td><td>D3</td><td>x2</td><td>D4</td></tr></table>

We can explain the effect of a on pricing through antipiracy effort. When k is small $\left( k < k _ { 1 } \right)$ ), the antipiracy effort increases as a increases. Then pirated products become less attractive than the legitimate products, and its cannibalization effect decreases, meaning that each firm can charge a higher price for its legitimate product. When k is not so large $\left( k _ { 1 } < k < k _ { 2 } \right)$ , an increase in a leads to a small decrease in antipiracy effort so that the piracy cost, represented by Equation (4), will still increase in this case, causing the pirated product to be less attractive. As a result, a firm could still charge a higher price as a increases. Finally, in the region where k is sufficiently large $( k > k _ { 2 } )$ , an increase in a will decrease the antipiracy effort significantly so that the antipiracy cost decreases. In this case, the pirated product becomes more attractive, and the cannibalization effect increases. Then a firm has to charge a lower price for the legitimate product.

To explain the impact of direct effect a on a firm’s profit in Proposition 3.3, in equilibrium, we have

$$
\begin{array}{c} \frac {\partial \pi_ {1} ^ {*}}{\partial a} = \frac {\partial \pi_ {1} (e _ {1} , e _ {2} , p _ {1} , p _ {2} , a)}{\partial e _ {2}} \frac {\partial e _ {2} ^ {*}}{\partial a} + \frac {\partial \pi_ {1} (e _ {1} , e _ {2} , p _ {1} , p _ {2} , a)}{\partial p _ {2}} \\ \frac {\partial p _ {2} ^ {*} (e _ {1} ^ {*} , e _ {2} ^ {*})}{\partial a} + \left(\frac {\partial \pi_ {1}}{\partial a}\right) _ {e _ {1}, e _ {2}, p _ {1}, p _ {2}.} \end{array}\tag{19}
$$

by applying the Envelope theorem in Firm 1’s case (Firm $2 ^ { \prime } \mathrm { s }$ case is the same by symmetry). As we can see from (19), the direct effect a has three effects on the profit: the indirect effect via changing the competi-� � tor’s antipiracy effort $\left( \frac { \partial \pi _ { 1 } } { \partial e _ { 2 } } \frac { \partial e _ { 2 } ^ { * } } { \partial a } \right)$ , the indirect effect via� � changing the competitor’s product price $\left( \frac { \partial \pi _ { 1 } } { \partial p _ { 2 } } \frac { \partial p _ { 2 } ^ { * } ( e _ { 1 } ^ { * } , e _ { 2 } ^ { * } ) } { \partial a } \right)$ and the direct effect on its own profit $\textstyle \left( { \frac { \partial \pi _ { 1 } } { \partial a } } \right)$ .

To determine the sign of the right-hand side of Equation (19), we first determine the signs of $\frac { \partial \pi _ { 1 } ( e _ { 1 } , e _ { 2 } , p _ { 1 } , \stackrel { \mathbf { 1 } } { p _ { 2 } } , a ) } { \partial e _ { \gamma } }$ and $\frac { \partial \pi _ { 1 } } { \partial p _ { 2 } }$ in equilibrium in the following lemma.

Lemma 5. A firm’s profit increases with its competitor’s antipiracy effort and does not change with the competitor’s product price. That $\begin{array} { r } { i s , \frac { \partial \pi _ { 1 } ( e _ { 1 } , e _ { 2 } , p _ { 1 } , p _ { 2 } , \stackrel { \smile } { a } ) } { \partial e _ { 2 } } > 0 a n d \frac { \partial \pi _ { 1 } } { \partial p _ { 2 } } = \stackrel { \cdot } { 0 } } \end{array}$

Lemma 5 can be understood as follows. From (10), we can see that Firm $1 ^ { \prime } \mathrm { s }$ total demand does not depend on Firm 2’s price $p _ { 2 }$ when antipiracy efforts are given. Then its profit is not affected by $\begin{array} { r } { p _ { 2 } ; \frac { \partial \pi _ { 1 } } { \partial p _ { 2 } } = 0 } \end{array}$ When Firm 2’s antipiracy effort $e _ { 2 }$ increases, Firm 1’s pirated product becomes more attractive relative to Firm $2 ^ { \prime } \mathrm { s }$ pirated product, leading to a stronger demand expansion effect: Firm 1’s total demand increases. At the same time, Firm 1’s legitimate demand increases because the cost of pirating Firm 1’s product increases as $e _ { 2 }$ increases. That is, the cannibalization effect be comes weaker. Therefore, Firm 1’s profit increases with Firm 2’s antipiracy effort $\textstyle \left( { \frac { \partial \pi _ { 1 } } { \partial e _ { 2 } } } > { \hat { 0 } } \right)$ . Because the firms’ antipiracy efforts increase with a when k is small and decrease with a when k is large (see Proposition 3.1), we can conclude that the indirect effect via chang-� � ing the competitor’s antipiracy effort $\left( \frac { \partial \pi _ { 1 } } { \partial e _ { 2 } } \frac { \partial e _ { 2 } ^ { * } } { \partial a } \right)$ will be positive if k is small $( k < k _ { 1 } )$ ) and negative if k is large $( k > k _ { 1 } )$ . When a increases, the cannibalization effect decreases, holding the antipiracy efforts and the legiti mate product prices constant. Then Firm 1’s profit increases. That is, the direct effect on Firm 1’s own profit is positive $\left( \left( { \frac { \partial \pi _ { 1 } } { \partial a } } \right) _ { e _ { 1 } , e _ { 2 } , p _ { 1 } , p _ { 2 } } > 0 \right)$

In summary, when k is small $\left( k < k _ { 1 } \right)$ , both the direct and indirect effects are positive. So Firm 1’s profit increases with $\begin{array} { r } { a \ \left( \frac { \partial \pi _ { 1 } ^ { * } } { \partial a } > 0 \right) } \end{array}$ . When k is not too large $\left( k _ { 1 } < k < k _ { 3 } \right)$ , the direct effect dominates the indirect� � effect and Firm 1’s profit still increases with a $\left( \frac { \partial \pi _ { 1 } ^ { * } } { \partial a } > 0 \right)$ However, if k is large enough $( k > k _ { 3 } )$ , the indirect effect dominates the direct effect, and Firm 1’s profit decreases� � with a $\left( \frac { \partial \pi _ { 1 } ^ { * } } { \partial a } < 0 \right)$

The managerial insight of this proposition is that antipiracy technology advancement (a increasing) does not necessarily benefit firms. For instance, better algorithms are being created to detect and gather information about piracy activity across the web (Das 2021). The algorithms make it more efficient for firms to control the piracy of their own products, that is, a increases. Intuitively, we may think that higher efficiency will benefit the firms. However, this is only true when the network effect intensity is small. If the network effect intensity is large, the improvement in piracy detection efficiency could harm the firm profits, contrary to common intuition.

The results of Propositions 2 and 3 have some similarity: both show that the improvement of technology may hurt the firms’ profits. However, their driving forces are different. In Proposition 2, technology advancement (e.g., the adoption of the SaaS model) could eliminate the buffer effect created by piracy, leading to more intensive competition between two firms. However, in Proposition 3, technology advancement (e.g., improvement in algorithms) could weaken the demand expansion effect in the case of a high network effect and make firms worse off.

We proceed to examine how the cross effect (b) and the degree of overlap between antipiracy efforts (δ) impact the firms’ antipiracy efforts, prices, and profits. We have the following proposition.

Proposition 4. When the cross effect (b) increases or the degree of overlapping between antipiracy efforts (δ) decreases,

(1) The firms’ antipiracy efforts increase, that is, $\begin{array} { r } { \frac { \partial e ^ { * } } { \partial b } > 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial e ^ { * } } { \partial \delta } < 0 ; } \end{array}$

(2) The product prices increase, that $\begin{array} { r } { i s , \frac { \partial p ^ { * } } { \partial b } > 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial p ^ { * } } { \partial \delta } < 0 ; } \end{array}$

(3) The firm profits increase, that is, $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial b } > 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial \pi ^ { * } } { \partial \delta } < 0 } \end{array}$

Comparing Proposition 3 with Proposition $^ { 4 , }$ we can see that antipiracy effort increases monotonically with b while it can decrease with a when k is large. To understand the difference between the effects of a and $b ,$ we need to look at the two effects of b. On the one hand, to Firm 1, an increase in b can increase the cost of pirating its legitimate software, an effect similar to a’s. According to Proposition 3, such an effect is positive when k is small and negative when k is large. On the other hand, an increase in b can also increase the cost of pirating Firm 2’s product, making Firm 1’s pirated product more attractive. As a result, Firm 1 has an incentive to increase antipiracy effort to gain from network effects. When the network effect intensity k is high, the positive effect of b on antipiracy effort caused by that incentive will be high and will dominate the negative effect of b on antipiracy effort due to the impact of b on the piracy cost of its own product. The overall effect of b on Firm 1’s antipiracy cost is positive when k is large. When k is small, both effects of b are positive, and the overall effect of b on antipiracy is positive. The same analysis holds for Firm 2’s antipiracy effort.

Because the antipiracy effort increases when b increases, pirated products become less attractive and legitimate products more attractive. Therefore, each firm can charge a higher price. Then we have Proposition 4.2. To explain the impact of the cross effect b on a firm’s profit, we can apply the Envelope theorem in Firm 1’s case in equilibrium (Firm 2’s case is the same by symmetry) and get the following equation similar to (19):

$$
\frac {\partial \pi_ {1} ^ {*}}{\partial b} = \frac {\partial \pi_ {1} (e _ {1} , e _ {2} , p _ {1} , p _ {2} , b)}{\partial e _ {2}} \frac {\partial e _ {2} ^ {*}}{\partial b} + \left(\frac {\partial \pi_ {1}}{\partial b}\right) _ {e _ {1}, e _ {2}, p _ {1}, p _ {2}}.\tag{20}
$$

A competitor’s price has no effect on one firm’s profit in equilibrium $\begin{array} { r } { ( \mathrm { i . e . , } \frac { \partial \pi _ { 1 } } { \partial p _ { 2 } } \mathrm { = } \frac { \partial \pi _ { 2 } } { \partial p _ { 1 } } = 0 ) } \end{array}$ , as we have seen before. The first term on the right-hand side of (20) is positive because $\frac { \partial e _ { 2 } ^ { * } } { \partial b } > 0$ according to Proposition 4.1 and $\begin{array} { r } { \frac { \partial \pi _ { 1 } } { \partial e _ { 2 } } > 0 } \end{array}$ according to Lemma 5. The second term $\left( \frac { \partial \pi _ { 1 } } { \partial b } \right) _ { e _ { 1 } , e _ { 2 } , p _ { 1 } , p _ { 2 } } ^ { - \hdots }$ , similar to $\left( \frac { \partial \pi _ { 1 } } { \partial a } \right) _ { e _ { 1 } , e _ { 2 } , p _ { 1 } , p _ { 2 } }$ , can also be shown to be positive. When the prices and efforts are fixed, an increase in b makes the cost of piracy higher. Then there will be less demand for the pirated products, and each firm’s profit should increase. Therefore, the overall effect of b on a firm’s profit is positive, that is, $\frac { \partial \pi _ { 1 } ^ { * } } { \partial b } > 0$ . The same is true for Firm 2.

When the degree of overlapping between efforts δ decreases, the marginal impact of Firm 1’s antipiracy effort $e _ { 1 }$ on the piracy cost of Firm $2 ^ { \prime } \mathrm { s }$ product, which is $( 1 - \delta ) l$ b from Equation (6), increases. Then, the marginal impact of $e _ { 1 }$ on the weakening of the demand expansion effect is reduced while that on the weakening of the cannibalization effect remains the same. As a result, the marginal benefit of antipiracy effort increases. Firm 1 will have an incentive to increase its antipiracy effort. By symmetry, Firm 2 will also do the same, resulting in each firm’s antipiracy effort increasing in equilibrium. Then we have $\begin{array} { r } { \frac { \partial e ^ { * } } { \partial \delta } { \dot { < } } 0 } \end{array}$ . When δ increases, antipiracy effort decreases and therefore the cost of piracy decreases, enhancing the cannibalization effect of pirated products on legitimate products. Then legitimate products become less attractive, and each firm charges a lower price, that $\mathrm { i s } , \frac { \partial p ^ { \ast } } { \partial \delta } < 0$

By applying the Envelope theorem to Firm 1’s profit in equilibrium with respect to $\delta ,$ , we have

$$
\frac {\partial \pi_ {1} ^ {*}}{\partial \delta} = \frac {\partial \pi_ {1} (e _ {1} , e _ {2} , p _ {1} , p _ {2} , \delta)}{\partial e _ {2}} \frac {\partial e _ {2} ^ {*}}{\partial \delta} + \left(\frac {\partial \pi_ {1}}{\partial \delta}\right) _ {e _ {1}, e _ {2}, p _ {1}, p _ {2}}.\tag{21}
$$

The first term on the right-hand side of (21) is negative because $\begin{array} { r } { \frac { \partial \pi _ { 1 } } { \partial e _ { 2 } } > 0 } \end{array}$ according to Lemma 5 and $\frac { \partial e _ { 2 } ^ { * } } { \partial \delta } < 0$ according Proposition 4.1. When δ decreases while holding equilibrium antipiracy efforts and prices constant, it is more costly to pirate. Then the demand for a legitimate product increases. As a result, the firm’s profit increases. That is, $\begin{array} { r } { \frac { \partial \pi _ { 1 } } { \partial \delta } < 0 } \end{array}$ in equilibrium. Therefore, the overall effect of δ on a firm’s profit is negative.

Proposition 4 shows an interesting result due to cross effect b. With the existence of a cross effect, one firm’s antipiracy effort can increase the cost of pirating its competitor’s product. From Proposition $^ { 4 , }$ we can see that a firm is willing to increase its antipiracy effort and help its competitor in controlling piracy because, in the end, both firms benefit. This result has a practical implication for software antipiracy. For example, piracy websites often have pirated software from competing firms. If a firm can reduce the piracy of its product by shutting down a piracy website that also hosts its competitor’s pirated product, it will be more motivated to ban the entire website instead of forcing the website to only remove the software pirated from this firm. By banning the entire website, one firm can make it more difficult to obtain both firms’ products, and the other firm can indirectly benefit.

To increase the cross effect, firms can reduce the duplication of antipiracy efforts by setting up an industrial alliance to coordinate their antipiracy efforts. For example, through coordination, one firm can focus on detecting piracy websites, and the other firm can lobby the law enforcement agencies to shut down such websites. Without such coordination, both firms could expend effort going after the same set of piracy websites and lobbying the same law enforcement agencies. This lack of coordination increases the value of $\delta ,$ and our model provides an analytical framework for understanding the benefit of coordination by reducing the duplication of efforts. Past studies on antipiracy (Jain 2008, Dey et al. 2019) have not considered the cross effect of antipiracy efforts. Firms using solutions of such models directly would under-invest in antipiracy efforts and achieve suboptimal results.

By comparing Proposition 3 and $^ { 4 , }$ we see that the direct effect and cross effect have different impacts on firms’ decisions and profits. An increase in the direct effect of antipiracy efforts may lead to a decrease in antipiracy efforts, product prices and profits, while an increase in the cross effect always leads to an increase in antipiracy efforts, product prices and profits. Therefore, an increase in the cross effect can always benefit these two firms while an increase in the direct effect may not. This answers our second research question raised in the Introduction.

We proceed to discuss the impacts of the network effect intensity k, as expressed in the following proposition.

Proposition 5. When the network effect intensity k increases, the following hold:

(1) If either the quality of the pirated product is small or the network effect intensity is large, then the antipiracy efforts decrease; otherwise, the antipiracy efforts increase. That is, when $\theta < \theta ^ { \prime }$ or $\begin{array} { r } { k _ { 4 } < k < \overline { { k } } , \frac { \partial \dot { e } ^ { \ast } } { \partial k } < \dot { 0 } ; } \end{array}$ otherwise, $\begin{array} { r } { \frac { \partial e ^ { * } } { \partial k } > 0 } \end{array}$

(2) The product prices increase, that $\begin{array} { r } { i s , \frac { \partial p ^ { * } } { \partial k } > 0 } \end{array}$

(3) The firm profits increase, that $\begin{array} { r } { i s , \frac { \partial \pi ^ { * } } { \partial k } > 0 } \end{array}$

The expressions of $\theta ^ { \prime } , k _ { 4 } ,$ and $\overline { { r } } _ { 4 }$ are defined in Online Appendix K.

We can understand Proposition 5.1 in the following way. On the one hand, when θ is small $\left( \theta < \theta ^ { \prime } \right)$ , the pirated product is not so attractive, and the piracy activity is already under control. If a firm exerts more effort as k increases, the cannibalization effect will not be weakened much, and the weakening of the demand expansion effect dominates the weakening of the cannibalization effect. Then a firm would be hurt by increasing its antipiracy effort, so the firm should exert less effort. When k is large $( k > k _ { 4 } )$ , the demand expansion effect is very sensitive to antipiracy effort. If a firm exerts more effort as k increases, the weakening of the demand expansion effect dominates the weakening of the cannibalization effect. Then, the firm would also be hurt. As a result, the firm should exert less effort when k increases. On the other hand, when θ is large and the network effect intensity is small, pirated products do not contribute much to the network effect of legitimate products. In this situation, if a firm exerts more effort as k increases, the weakening of the cannibalization effect dominates the weakening of the demand expansion effect, so the firm should exert more effort.

The past literature has shown that a stronger network effect commonly results in a weaker antipiracy effort because a firm wants to build a larger network due to a stronger network effect and tolerates the piracy more (Conner and Rumelt 1991, Shy and Thisse 1999, Tsai and Chiou 2012, Herings et al. 2017). In contrast, our result shows that if pirated products are very attractive relative to legitimate products and the network effect is not so high, a firm should increase its antipiracy effort to control piracy when the network effect increases. Our conclusion agrees with that of Jain (2008), who also showed that when the network effect increases, a firm may choose higher levels of copyright protection. However, the underlying mechanisms are different. In Jain (2008), in the presence of strong network effects, a firm can use stronger copyright enforcement to reduce direct price competition between legitimate products and charge a higher price. In our model, competition exists between a legitimate product and a pirated one, which leads to the cannibalization effect. In the region of high-quality pirated software and low network effect intensity, the cannibalization effect dominates the demand expansion effect. When the network effect intensity increases, a firm can increase its antipiracy effort to reduce the cannibalization effect. In other words, reducing the demand for pirated products in this case will benefit a firm.

Proposition 5.2 describes a combination of direct and indirect effects of network effect intensity k on the product price. When k increases, a legitimate user’s utility increases, given that the total demands are fixed in our (symmetric) model. Then one firm could increase its price if the antipiracy effort is fixed. We call it the direct effect of $k$ on $p .$ The network effect intensity k also has an indirect effect on price through antipiracy effort. When $k$ is small and the quality of the pirated product θ is large, a firm’s antipiracy effort increases with $k$ according to Proposition 5.1. Then this firm’s pirated product becomes less competitive, and this firm can charge a higher price. In this case, the indirect effect of k on $p$ is positive, and the combined effect of k on p is positive. When k is large or the quality of pirated product $\theta$ is small, a firm’s antipiracy effort decreases with k according to Proposition 5.1. This means we have a negative indirect effect.

Proposition 5.2 shows that the direct effect dominates the indirect effect, and the overall effect is still positive. That is, the price increases with the network effect intensity. Because a firm’s pricing power increases due to the increase in network effect intensity, its profit always increases correspondingly, as Proposition 5.3 shows.

Comparing the impacts of network effect intensity in the cases with piracy (Proposition 5) and without piracy (Lemma 4), we find that the impacts on profits are opposite. When there is no piracy in the market, the firm profits decrease with the network effect intensity. The intuition behind this result is that when the network effect intensity increases, the competition between the two legitimate products intensifies, making both firms worse off. However, when piracy exists, the firm profits increase with the network effect intensity. In this case, there is no direct competition between two legitimate products. In other words, pirated products act as a buffer, changing the result: When the network effect intensity increases, each firm raises its price and gains higher profit, as discussed previously.

## 5. Consumer Surplus and Social Welfare

In this section, we analyze consumer surplus and social welfare in the four-product and two-product competition cases. Following the literature (Banerjee 2003, Jain 2008, Dey et al. 2019), the consumer surplus consists of all legitimate users’ utilities and all software pirates utilities. We focus on comparing the case in which firms choose the desktop version and tolerate piracy (fourproduct competition) with the case in which firms adopt SaaS (SaaS case). If the firms choose the desktop version and do not tolerate piracy, the consumer surplus will be the same as in the SaaS case and the social welfare will be no larger than that in the SaaS case.

In the case when firms tolerate piracy, the consumer surplus is

$$
C S ^ {*} = 2 \left(\int_ {0} ^ {D _ {1}} U _ {1} d x + \int_ {D _ {1}} ^ {\frac {1}{2}} U _ {3} d x\right),\tag{22}
$$

where $D _ { 1 }$ is defined in Lemma 2; $U _ { 1 }$ and $U _ { 2 }$ are defined in (1) and (3). The social welfare is

$$
S W ^ {*} = C S ^ {*} + 2 \pi^ {*},\tag{23}
$$

where $\pi ^ { * }$ is defined in Lemma 2.

In the SaaS case, the consumer surplus is

$$
C S _ {b} = 2 \int_ {0} ^ {1 / 2} U _ {1} d x,\tag{24}
$$

where $U _ { 1 }$ is defined in (1). The social welfare is

$$
S W _ {b} = C S _ {b} + 2 \pi_ {b},\tag{25}
$$

where $\pi _ { b }$ is defined in Lemma 4.

Then, we have the following results.

Proposition 6. Whenever the firms are better off tolerating piracy, that is, when antipiracy cost is large $( r > r _ { m } )$ and pirated software quality is not so large $\left( \theta < \theta _ { 3 } \right)$ , the social welfare and the consumer surplus will decrease.

The explanation of Proposition 6 is as follows. Because the price is the transfer payment between firms and users, it does not affect the social welfare. If we ignore the price, then in the four-product case, the legitimate users enjoy the same utility as the users in the SaaS case, whereas the software pirates have lower utility than the users in the SaaS case. At the same time, firms in the four-product case should exert effort, whereas firms in the SaaS case do not. Then, we conclude that the social welfare in the SaaS case is higher. When firms tolerate piracy, they earn higher profits, whereas the social welfare will always be worse off. Then, we can conclude that the consumer surplus will be worse off in this case.

## 6. Rational Expectation

In the main model, we study a full information case by assuming that all users know the amount of antipiracy effort from the two firms. In this section, we relax this assumption and assume that only some users know the amount of antipiracy effort. The other users are uninformed, but they have a rational belief about the firms’ antipiracy efforts. We denote $\beta$ as the proportion of informed users and $( 1 - \beta )$ the proportion of uninformed users. We solve this problem via backward induction. In Stage 2, both firms decide their product prices based on the firms’ antipiracy efforts and users’ beliefs about antipiracy efforts in Stage 1. In Stage 1, firms determine the antipiracy efforts by anticipating that the uninformed users’ belief will be consistent with the equilibrium antipiracy effort (Gao and $\mathrm { S u }$ 2017, Shulman and Geng 2019). In the following analysis, we focus on the case of four-product competition in which the demands for pirated products are positive and uninformed users can potentially play a role in the outcome of the game. Our analysis shows that our main results are robust with regard to the assumption that all users are informed.

## 6.1. Model Setup

For a user of type γ (an informed user has $\gamma = I$ and uninformed user $\gamma = U )$ located at x, the utility of buying Product j $( j \in \{ 1 , 2 \} )$ is given by

$$
U _ {1} ^ {\gamma} = q - t x + k \sum_ {\alpha \in \{I, U \}} (D _ {1} ^ {\alpha} + D _ {3} ^ {\alpha}) - p _ {1},\tag{26}
$$

and

$$
U _ {2} ^ {\gamma} = q - t (1 - x) + k \sum_ {\alpha \in \{I, U \}} (D _ {2} ^ {\alpha} + D _ {4} ^ {\alpha}) - p _ {2},\tag{27}
$$

where $D _ { j } ^ { I }$ and $D _ { j } ^ { U }$ are the demands for legitimate Product $j$ from informed and uninformed users, respectively;

and $D _ { j + 2 } ^ { I }$ and $D _ { j + 2 } ^ { U }$ are the demands for pirated Product j from informed and uninformed users, respectively. Here, $U _ { 1 } ^ { I } = U _ { 1 } ^ { U }$ and $U _ { 2 } ^ { I } = U _ { 2 } ^ { U }$ because the utility of buying a legitimate product is not affected by the antipiracy effort, and the informed and uninformed users derive the same amount of utility from buying the same legitimate product.

The utilities of an informed user pirating Products 1 and 2 are given, respectively, by

$$
U _ {3} ^ {I} = \theta \left[ q - t x + k \sum_ {\alpha \in \{I, U \}} (D _ {1} ^ {\alpha} + D _ {3} ^ {\alpha}) \right] - c _ {1} (e _ {1}, e _ {2})\tag{28}
$$

and

$$
U _ {4} ^ {I} = \theta \left[ q - t (1 - x) + k \sum_ {\alpha \in \{I, U \}} (D _ {2} ^ {\alpha} + D _ {4} ^ {\alpha}) \right] - c _ {2} (e _ {1}, e _ {2}),\tag{29}
$$

where $c _ { 1 } ( e _ { 1 } , e _ { 2 } ) = ( a + b ) e _ { 1 } + ( 1 - \delta ) b e _ { 2 }$ and $c _ { 2 } ( e _ { 1 } , e _ { 2 } ) =$ $( 1 - \delta ) b e _ { 1 } + ( a + b ) e _ { 2 }$

For an uniformed user who has an expectation of Firm i’s antipiracy effort ${ \hat { e } } _ { i } , i = 1 , 2 ,$ the utilities of pirating Products 1 and 2 are given by

$$
U _ {3} ^ {U} = \theta \left[ q - t x + k \sum_ {\alpha \in \{I, U \}} (D _ {1} ^ {\alpha} + D _ {3} ^ {\alpha}) \right] - c _ {1} (\hat {e} _ {1}, \hat {e} _ {2}),\tag{30}
$$

and

$$
U _ {4} ^ {U} = \theta \left[ q - t (1 - x) + k \sum_ {\alpha \in \{I, U \}} \left(D _ {2} ^ {\alpha} + D _ {4} ^ {\alpha}\right) \right] - c _ {2} (\hat {e} _ {1}, \hat {e} _ {2}),\tag{31}
$$

where $c _ { 1 } ( \hat { e } _ { 1 } , \hat { e } _ { 2 } ) = ( a + b ) \hat { e } _ { 1 } + ( 1 - \delta ) b \hat { e } _ { 2 }$ and $c _ { 2 } ( \hat { e } _ { 1 } , \hat { e } _ { 2 } ) =$ $( 1 - \delta ) b \hat { e } _ { 1 } + ( a + b ) \hat { e } _ { 2 }$

For a given user type $\alpha \in \{ I , U \}$ , define $x _ { 1 } ^ { \alpha } \left( x _ { 3 } ^ { \alpha } \right)$ as the Hotelling line location of such a user who is indifferent between purchasing and pirating Product 1 (Product $2 ) ; \ x _ { 2 } ^ { \alpha }$ is the location of such a user who is indifferent between pirating Product 1 and Product 2. Then, for $\alpha \in \{ I , U \}$ , we have

$$
U _ {1} ^ {\alpha} | _ {x = x _ {1} ^ {\alpha}} = U _ {3} ^ {\alpha} | _ {x = x _ {1} ^ {\alpha}},
$$

$$
U _ {2} ^ {\alpha} | _ {x = x _ {3} ^ {\alpha}} = U _ {4} ^ {\alpha} | _ {x = x _ {3} ^ {\alpha}},\tag{32}
$$

(33)

and

$$
U _ {3} ^ {\alpha} | _ {x = x _ {2} ^ {\alpha}} = U _ {4} ^ {\alpha} | _ {x = x _ {2} ^ {\alpha}}.\tag{34}
$$

The two firms’ profits are given by

$$
\pi_ {j} (p _ {j}, e _ {j}) = p _ {j} (D _ {j} ^ {I} + D _ {j} ^ {U}) - r e _ {j} ^ {2}, j = 1, 2.\tag{35}
$$

## 6.2. Results Under Rational Expectation

With backward induction, we can solve the game and prove the following lemma.

Lemma 6. In the equilibrium of the four-product competition, the product price, antipiracy effort, profit, and legitimate product demand in the rational expectation case can be obtained by replacing A with βA in Lemma 2.

We can see that when $\beta = 1 _ { \cdot }$ , that is, all users are informed of firms’ antipiracy efforts, the results of the rational expectation case become the same as those in the main model. By comparative statics analysis, we can find the impacts of $a , b , \delta ,$ and k on the firms’ antipiracy efforts, prices, and profits. We have the following proposition.

Proposition 7. In the equilibrium of the four-product com petition, the impacts of the direct effect a, cross effect $b ,$ degree of overlapping $\delta ,$ and network effect intensity k on price, effort, and profit have the same patterns as those in the main model, given in Propositions 3–5. However, the threshold values are different.

We also investigate the impact of the proportion of informed users $\beta ,$ obtaining the following proposition.

Proposition 8. When the proportion of informed users $\beta$ increases, the firms’ equilibrium antipiracy efforts, prices, and profits increase, that is, $\begin{array} { r } { \frac { \partial e ^ { * } } { \partial \beta } > 0 , \frac { \partial p ^ { * } } { \partial \beta } > 0 , \bar { a } n \bar { d } \frac { \partial \pi ^ { * } } { \partial \beta } > \dot { 0 } } \end{array}$

When more users are informed, the firms have higher motivation to exert antipiracy effort. Then, they can charge higher prices and earn higher profits. This proposition shows that it is important for firms to increase the awareness of antipiracy programs among the general population through education and marketing campaigns. Examples are Autodesk’s Genuine Autodesk Program on its website (Autodesk 2021) and Japan’s various popular antipiracy ads (Blaster 2020).

## 7. Conclusion

This paper analyzes the strategic interactions between legitimate products and their pirated versions in the presence of antipiracy effort’s direct and cross effects. We first study the conditions under which pirated products could be eliminated or tolerated by software firms under the threat of piracy. Our results show that when the quality of pirated software is not so large, the cost of antipiracy effort determines the structure of competition. When the cost of antipiracy effort is large, firms will tolerate the existence of pirated products, resulting in competition among four products: two legitimate products and their corresponding pirated products. When the antipiracy effort is not costly, in equilibrium there will be no piracy in the market, and only legitimate products compete against each other. In this case, a firm’s antipiracy effort depends on the quality of the pirated product. When the quality of the pirated product is small, the pirated product is not so attractive, so a firm does not need to exert antipiracy effort. Interestingly, when the pirated product quality is large, a firm has to exert antipiracy effort to prevent piracy, even though there is no piracy in the market.

We also find another surprising result when studying the impact of piracy on a firm’s profit. One might expect that a firm would be hurt under the threat of piracy. Our counter-intuitive result shows that a firm’s profit could increase when piracy exists, provided the pirated product quality is not large and the antipiracy cost is large. Our paper contributes to the software piracy literature by identifying the pirated product’s novel role of buffering in reducing the intensity of competition. Our result has important implications for software firms. When the pirated product is not very attractive, firms should tolerate piracy, because software piracy can mitigate the competition between two firms, even though their legitimate demand is cannibalized. In recent years, cloud computing has made the SaaS business model technically feasible. This new business model can eliminate piracy. However, our result shows that eliminating piracy does not necessarily mean higher profit due to the intensified competition between two legitimate products. In other words, there is an unexpected benefit of tolerating piracy under certain conditions.

Although piracy may boost firm profits, its impact on social welfare goes in an opposite direction. Specifically, we find that, whenever piracy increases firm profits, the social welfare decreases. Intuitively, piracy drags down the overall quality of the products in the market, and the firms need to invest in antipiracy efforts, consequently social welfare and consumer surplus hurt. The result has practical implication for the policy makers: policy makers can have stricter law enforcement and incentivize firms to eliminate piracy.

When piracy exists, we find that the direct and cross effects of antipiracy effort have different impacts on firms’ antipiracy efforts and their profits. First, we may expect that a firm would always benefit from a larger direct effect of antipiracy effort, but this is not always true. As the direct effect increases, the firm profits, antipiracy efforts, and product prices increase when the network effect intensity is small and decrease when the network effect intensity is large. The reason is that when the network effect intensity is large, the pirated product’s demand expansion effect becomes more important. If the direct effect increases, the reduction of demand expansion effect dominates that of the cannibalization effect. Then, firms have to tolerate piracy more in a competitive market. As a result, they decrease their antipiracy effort and prices. Therefore, their profits are hurt by an increase in the direct effect of antipiracy effort.

As the cross effect of antipiracy effort increases, antipiracy efforts, product prices, and firm profits always increase. The explanation is that an increase in the cross effect can increase not only the direct cost of pirating a firm’s legitimate software, but also the cost of pirating its competitor’s product, causing both pirated products to be less attractive. Then, firms do not have to tolerate piracy as much and can increase antipiracy efforts and prices. Therefore the firm profits increase. There is an important implication from our results. The past literature has not considered the cross-effect of antipiracy effort. If firms ignore that cross effect, they could underinvest in antipiracy effort and gain less profit.

When the degree of overlap between antipiracy efforts increases, the effect of a firm’s antipiracy effort on the cost of pirating its competitor’s product decreases. Then, the firm is less willing to exert antipiracy effort. Otherwise, if the firm chose to increase its antipiracy effort, its pirated product would become less attractive relative to its competitor’s pirated product, and it could hurt itself. Therefore, when the degree of overlapping increases, each firm decreases antipiracy effort and reduces its product price. As a result, their profits decrease. A practical implication is that to improve profits, firms can set up an industrial alliance to help coordinate antipiracy efforts so that they can increase the cross effect and reduce the duplication of efforts. For example, the aforementioned software firms such as Microsoft, Adobe, and Autodesk have set up an alliance The Software Alliance (BSA) to “promote legal software use” (BSA 2022). BSA has partnered with key stakeholders around the world and launched various compliance programs to raise awareness of the risks of using pirated software and enhance end-user enforcement. When doing so, BSA strategically chooses programs that optimize results and increase revenue for member firms.

From the discussion of direct and cross effects, we can gain interesting insights with regard to the efficiency of antipiracy effort. If an increase in the efficiency of antipiracy effort only increases the cost of pirating its own product (i.e., if the direct effect increases), the firm does not always benefit. However, if an increase in that efficiency increases the costs of pirating both firms’ products (i.e., if the cross effect increases or the degree of effort overlap decreases), then firms should always increase their antipiracy efforts and gain from an increase in efficiency.

We also find that when the network effect intensity increases, the equilibrium antipiracy effort increases for high piracy-product quality and low network effect intensity. Although similar results appear in the literature, our contribution in this paper is the discovery of a different mechanism. In our model, firms increase antipiracy efforts to reduce the cannibalization effect brought by pirated products. In the case that both firms adopt SaaS models and piracy does not exist, a firm’s profit decreases due to more intense competition caused by higher network effect intensity. However, when piracy does occur, a firm’s profit increases with the network effect intensity due to the existence of pirated products as a buffer between the two legitimate products.

We now discuss avenues for future work. In our model, we assume that the quality of software products is fixed. It will be interesting to study the interaction between investment in software quality and antipiracy effort. In a competitive environment, could a higher efficiency in software development lead to lower software protection to attract users and a lower profit, contrary to what one might expect? One could also study the case where firms invest in antipiracy efforts sequentially in a leader-follower game. In such a game, a follower might be able to reduce the duplication of effort after observing the leader’s antipiracy effort. Thus, it is worth studying whether a firm might benefit more by waiting for the other to take antipiracy measures first. In addition, one can consider an extension where there is uncertainty in the outcome of antipiracy efforts. For example, as a firm exerts effort in developing new antipiracy technology, the effectiveness of such technology could be quite uncertain. In such a situation, one can study whether firms should coordinate in developing such technology while competing on pricing.

## Acknowledgments

The authors thank the editors and anonymous referees for comments that have helped improve the paper. The authors contributed equally to this paper.

## References

Adobe (2022) Feature summary—Photoshop desktop (April 2022 release). Accessed March 14, 2023, https://helpx.adobe.com photoshop/using/whats-new/2022-2.html#other-enhancements.

August T, Tunca TI (2008) Let the pirates patch? An economic analysis of software security patch restrictions. Inform. Systems Res. 19(1):48–70.

Australia Copyright Act 1968 Copyright act 1968. http://www. comlaw.gov.au/Details/C2014C00291.

Autodesk (2021) Genuine Autodesk. https://www.autodesk.com genuine/overview.

Banerjee DS (2003) Software piracy: A strategic analysis and polic instruments. Internat. J. Industrial Organ. 21(1):97–127.

Ben-Shahar D, Jacob A (2004) Selective enforcement of copyright as an optimal monopolistic behavior. Contributions Econom. Anal. Policy 3(1):18.

Blaster M (2020) Japan’s favorite anti-piracy ads are back with an action-packed reboot after six-year break. https://bit.ly/3a2gnal.

BSA (2022) About BSA. https://www.bsa.org/about-bsa.

Chakraborty A (2021) 5 biggest differences between GTA 5 cracked vs GTA 5 original. https://paidforarticles.com/5-biggest-differencesbetween-gta-5-cracked-vs-gta-5-original-61138

Chellappa RK, Mehra A (2018) Cost drivers of versioning: Pricing and product line strategies for information goods. Management Sci. 64(5):2164–2180.

Chellappa RK, Shivendu S (2005) Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4):400–417.

Chen Yn, Png I (2003) Information goods pricing and copyright enforcement: Welfare analysis. Inform. Systems Res. 14(1):107–123.

Clipping Panda (2022) Adobe Photoshop crack 2022. https:// clippingpanda.com/adobe-photoshop-crack-2022/.

Conner KR, Rumelt RP (1991) Software piracy: An analysis of protection strategies. Management Sci. 37(2):125–139.

Crozier R (2020) Siemens chases telstra customers over alleged cracked software use. https://bit.ly/3sjY33g.

Curien N, Laffond G, Laine ´ J, Moreau F (2004) Toward a New Busi ness Model for the Music Industry: Accommodating Piracy Throug Ancillary Products (Laboratoire d’e´conome´trie, Conservatoire National des Arts et Me´tiers, Paris).

Das S (2021) Indian ethical hacker Manan Shah develops world’s first AI-powered solutions to combat online piracy. https://bit. ly/3tFoyR2.

Demirhan D, Jacob VS, Raghunathan S (2007) Strategic IT investments: The impact of switching cost and declining IT cost. Man agement Sci. 53(2):208–226.

Dey D, Kim A, Lahiri A (2019) Online piracy and the “longer arm” of enforcement. Management Sci. 65(3):1173–1190.

Gao F, Su X (2017) Omnichannel retail operations with buy-online and-pick-up-in-store. Management Sci. 63(8):2478–2492

Geng X, Shulman JD (2015) How costs and heterogeneous consumer price sensitivity interact with add-on pricing. Production Oper. Management 24(12):1870–1882.

Harm IH, Oh JH (2017) Combating prerelease piracy: Modeling the effects of antipiracy measures in p2p networks. INFORMS J. Comput. 29(1):92–107.

Herings JJ, Peeters R, Yang MS (2017) Piracy on the Internet: Accommodate it or fight it? A dynamic approach. Eur. J. Oper. Res. 266(1):1–12.

Jain S (2008) Digital piracy: A competitive analysis. Marketing Sci 27(4):610–626

Johar M, Kumar N, Mookerjee V (2012) Content provision strategies in the presence of content piracy. Inform. Systems Res. 23(3-part-2): 960–975.

Keizer G (2016) Microsoft steps up legal pressure against Windows 10 pirates. https://tinyurl.com/ycpe4zaw.

Kim A, Lahiri A, Dey D (2018) The ‘Invisible Hand’ of piracy: An economic analysis of the information-goods supply chain. Man agement Inform. Systems Quart. 42(4):1117–1141.

Koh B, Hann IH, Raghunathan S (2019) Digitization of music: Consumer adoption amidst piracy, unbundling, and rebundling. Management Inform. Systems Quart. 43(1):23–45.

Lahiri A, Dey D (2013) Effects of piracy on quality of information goods. Management Sci. 59(1):245–264.

Levy N (2018) Microsoft sues ‘prolific distributor’ of pirated office and windows software. https://bit.ly/2NNQHWR.

Lu S, Wang XS, Bendle N (2020) Does piracy create online word of mouth? An empirical analysis in the movie industry. Management Sci. 66(5):2140–2162

Mehra A, Sajeesh S, Voleti S (2020) Impact of reference prices on product positioning and profits. Production Oper. Management 29(4): 882–892.

Microsoft (2012) Risks and hazards of pirated Windows server https://tinyurl.com/msrv9h23.

Ortega J (2000) Pareto-improving immigration in an economy with equilibrium unemployment. Econom. J. (London) 110(460):92–112.

Prasad A, Mahajan V (2003) How many pirates should a software firm tolerate? An analysis of piracy protection on the diffusion of software. Internat. J. Res. Marketing 20(4):337–353.

Shulman JD, Geng X (2019) Does it pay to shroud in-app purchas prices? Inform. Systems Res. 30(3):856–871.

Shy O, Thisse JF (1999) A strategic approach to software protection. J. Econom. Management Strategy. 8(2):163–190.

Sivan L, Smith MD, Telang R (2019) Do search engines influence media piracy? Evidence from a randomized field study. Man agement Inform. Systems Quart. 43(4):1143–1154.

Spajic ´ DJ (2023) Piracy is back: Piracy statistics for 2022. https:// dataprot.net/statistics/piracy-statistics/.

Speed R (2020) Microsoft sues Florida reseller it alleges sold ‘black market access devices’ allowing unlocking of office 365. https:/ bit.ly/3lQuWCj.

Sundararajan A (2004) Managing digital piracy: Pricing and protec tion. Inform. Systems Res. 15(3):287–308.

Swan KJ (2019) Autodesk audits: How did Autodesk know to audit you and what to do now? https://bit.ly/3lQ419Y.

Tsai MF, Chiou JR (2012) Counterfeiting, enforcement and social welfare. J. Econom. 107(1):1–21.

Tunca TI, Wu Q (2013) Fighting fire with fire: Commercial piracy and the role of file sharing on copyright protection policy for digital goods. Inform. Systems Res. 24(2):436–453.

U.S. Copyright Office (2011) Copyright law of the United States. http://www.copyright.gov/title17/.

Wang J, Cui S, Wang Z (2019) Equilibrium strategies in M/M/1 pri ority queues with balking. Production Oper. Management 28(1): 43–62.

Wolfram (2022) Mathematica quick revision history. https://www wolfram.com/mathematica/quick-revision-history.html.

Wu Sy, Chen Py (2008) Versioning and piracy control for digital information goods. Oper. Res. 56(1):157–172.

Xin M, Choudhary V (2019) IT investment under competition: The role of implementation failure. Management Sci. 65(4):1909–1925.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
