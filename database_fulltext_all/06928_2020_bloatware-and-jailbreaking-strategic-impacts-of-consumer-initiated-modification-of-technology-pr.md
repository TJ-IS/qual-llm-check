---
otero_id: 6928
otero_key: "F5QYZMGH"
title: "Bloatware and Jailbreaking: Strategic Impacts of Consumer-Initiated Modification of Technology Products"
authors: "Hasan Cavusoglu; Huseyin Cavusoglu; Xianjun Geng"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0883"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/F5QYZMGH/fulltext/images/7fea8a2b15d1ea645bdd5f210a530680cf05bfc039c2e401fb68c4bb10fa92d7.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Bloatware and Jailbreaking: Strategic Impacts of Consumer-Initiated Modification of Technology Products

Hasan Cavusoglu, Huseyin Cavusoglu, Xianjun Geng

To cite this article: Hasan Cavusoglu, Huseyin Cavusoglu, Xianjun Geng (2020) Bloatware and Jailbreaking: Strategic Impacts of Consumer-Initiated Modification of Technology Products. Information Systems Research

Published online in Articles in Advance 16 Mar 2020

https://doi.org/10.1287/isre.2019.0883

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Bloatware and Jailbreaking: Strategic Impacts of Consumer-Initiated Modi<sup>fi</sup>cation of Technology Products

Hasan Cavusoglu,<sup>a</sup> Huseyin Cavusoglu,<sup>b</sup> Xianjun Geng<sup>c</sup>

<sup>a</sup> Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada; <sup>b</sup> Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>c</sup> A. B. Freeman School of Business, Tulane University, New Orleans, Louisiana 70118 Contact: cavusoglu@sauder.ubc.ca, https://orcid.org/0000-0001-9734-785X (HC); huseyin@utdallas.edu, https://orcid.org/0000-0002-7982-3602 (HC); xgeng1@tulane.edu, https://orcid.org/0000-0002-9915-7096 (XG)

Received: April 20, 2017 Revised: April 5, 2018; January 21, 2019 Accepted: February 4, 2019 Published Online in Articles in Advance: March 16, 2020

https://doi.org/10.1287/isre.2019.0883

Copyright: © 2020 INFORMS

Abstract. Many consumer electronics devices are sold bundled with unwanted applications— called bloatware—that provide an additional revenue stream to device manufacturers but deteriorate the value of purchased devices for consumers. Consumers, in response, find technical means to modify purchased devices—called jailbreaking—to remove those applica tions, thereby reducing the anticipated bloatware revenue for manufacturers. From the perspective of a monopolistic firm that manufactures a consumer electronic device and can preinstall a third-party app for a fee, we investigate whether bloatware inclusion is a viable strategy and how the firm should price its product with bloatware given that consumers can remove bloatware from the product after purchase. We show that it is not always optimal for the firm to sell a bloatware-included product. Furthermore, our analysis reveals that even if the firm can make it harder for consumers to jailbreak, the firm is not always better off by doing so. Consumers do not necessarily benefit from the reduced cost of jailbreaking either. Because the firm passes part of the bloatware revenue to consumers in the form of a lower price, whenever bloatware inclusion benefits the firm, consumers also benefit. Finally, we confirm that our results are robust to alternative modeling assumptions.

History: Yong Tan, Senior Editor; De Liu, Associate Editor Funding: X. Geng acknowledges support from the National Natural Science Foundation of China [Grants 71628205 and 71872144]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0883.

Keywords: bloatware • jailbreaking • rooting • pricing • economics of IS • game theor

## 1. Introduction

The last decade has witnessed an explosive growth in the variety of personal devices in the consumer electronics market. Notable examples include smartphones, tablets, laptops, and wearable gadgets. Consumers of all kinds enjoy many of these devices as part of their daily routine. Firms—including manufacturers and service providers—often preinstall software applications (apps in short) onto these devices before consumers purchase them. Such preinstalled apps are highly valuable to firms because they bring additional revenue (Richtel 2008). Consumers oftentimes, however, consider preinstalled apps a hindrance and refer to such preinstalled yet unrewarding apps on devices as bloatware or, sometimes in a more negative tone, crapware or junkware<sup>1</sup> (Pinola 2012, Newman 2014). Although the sales of personal computers (PCs) have long been subsidized by third-party apps, bloatware is becoming a more pervasive and prevalent issue for consumers in the era of smartphones (McDaniel 2012). Today, many handheld devices are loaded with apps that consumers “did not ask for, do not want, and can’t get rid of” (McDaniel 2012, p. 85).

Bloatware deteriorates consumer value in several ways. Bloatware occupies precious screen space and takes up storage space and yet is seldom used by consumers (Dent 2014). Bloatware can also result in excessive battery drain, unnecessary data usage, and performance reduction (Triggs 2014). Last but not least, bloatware can expose consumers to security and privacy risks (McDaniel 2012).

Although forcing products onto consumers is a phenomenon observed in a wide range of industries, and bloatware inclusion can be viewed as bundling, this paper recognizes a counter-bloatware dynamic that is unique to information technology products: consumer-initiated modification of product software with the purpose of removing the bloatware, commonly referred to as jailbreaking or rooting in the popular press (Dachis 2011). Broadly speaking, jailbreaking refers to actions taken by consumers to override the software constraints imposed by firms, usually by gaining a rootlevel access to the operating system of a device. It is estimated that 27.44% of Android users root their phones (Lucic 2014). Once users gain control of their devices, they can easily get rid of any app they do not wish to have. It is important to note that jailbreaking can benefit consumers in several ways. In addition to removing bloatware, users can install custom readonly memories or kernels to be able to further modify their devices (Thomas 2017). For instance, a jailbroken iPhone can run software not available for download in the Apple App Store. A rooted Android phone can have a user interface with custom features and better performance (Thomas 2017). We focus on the bloatware-removal benefit of jailbreaking in the base model of this paper. We then explicitly study other additional benefits of jailbreaking in a model extension.

Our research is motivated by the fact that, in practice, firms vary in their positions regarding bloatware. Samsung, manufacturer of the popular Galaxy series of phones, consistently preinstalls apps on its products despite consumers’ complaints that many of these apps are bloatware (Limer 2015). Lenovo, by contrast, publicly commits to minimal bloatware on its products (Brandom 2015). To our knowledge, no academic research that explains this wide heterogeneity of firm stances over bloatware exists. The possibility of jailbreaking (and the resulting removal of bloatware) further complicates the business value of bloatware: bloatware suppliers would be discouraged to pay a higher fee for preinstallation of their apps if there was a large-scale removal of their bloatware by customers (Yegulalp 2012). As a result, firms would not be able to earn this revenue from bloatware suppliers. In markets with shrinking margins such as in smartphone and PC markets, the extra revenue from bloatware often is the difference between profit and loss (McDaniel 2012, Spence 2015), thereby putting even more pressure on manufacturers to rely on ancillary means to extract revenue. Although there exists rich information on the technology side of bloatware and jailbreaking, little research exists that explores the economic consequences of bloatware removal through jailbreaking on firm strategy. Understanding the implications of bloatware removal by consumers is a matter of utmost importance for firms that are bundling or considering bundling their product with bloatware. Therefore, we study how consumer-initiated jailbreaking affects a firm’s bloatware inclusion and product pricing strategies.

Because a direct economic consequence of jailbreaking is the loss of bloatware revenue for the firm, intuitively, a higher cost of jailbreaking for consumers is seemingly beneficial for firms that implement a bloatware strategy. Anecdotal evidence in practice, nevertheless, does not paint a consistent picture. Some firms in the smartphone industry adopt measures that artificially increase the technical difficulty of bloatware removal. For example, in the recent releases of the Galaxy S series, Samsung famously designated most of its preinstalled apps as nonremovable (Limer 2015). Some other firms, however, appeared more lenient (or even accommodative) to jailbreaking. HTC is publicly committed to unlocking bootloader for its recent phones (see http://www.htcdev.com/bootloader). The Nexus series phones and tablets, designed by Google and manufactured by various firms, often either directly offer root access to consumers or require only simple steps for jailbreaking. Given the inconsistent practices by firms adopting a bloatware strategy, it becomes crucial to study the relationship between difficulty in jailbreaking and firm profit Thus we ask whether a firm that adopts the bloatware strategy benefits from an increased cost of jailbreaking for consumers.

Consumers also have an influence on the cost of jailbreaking. In reality, consumers with technical skills frequently develop software exploits that circumvent restrictions imposed by firms. These jailbreaking techniques are subsequently shared with other consumers through platforms such as XDA Developers and You-Tube. There are also service companies, such as Best Buy Geek Squad, that can help consumers eliminate bloatware from their personal computers for a fee (Richtel 2008). Given consumer resentment at bloatware, it is understandable that consumer effort and market solutions are geared toward reducing the jailbreaking cost. Nevertheless, given the strategic actions of the firm that is aware of jailbreaking and has a pricing lever, is it true that a lower cost of jailbreaking always results in a higher consumer surplus?

Although adopting a bloatware strategy can be intuitively desirable for the firm because it brings additional revenue, it is less clear whether consumers actually benefit from this bloatware inclusion decision by the firm. Hence, the implication of bloatware on consumer surplus deserves investigation. Thus we ask how the firm’s decision on including bloatware in its product affects consumer surplus and whether both the firm and consumers benefit from the bloatware strategy.

To address all these questions, we develop a gametheoretical model to study the strategic interactions among three stakeholders: (1) the firm that manufactures a product, namely, an electronic device, that can add the bloatware into its product, (2) the bloatware supplier that is willing to pay the firm to preinstall its app as the bloatware, and (3) consumers who can purchase the product sold by the firm and also jailbreak it to remove the bloatware. We first analyze a benchmark scenario in which the firm sells a bloatware-free product. We next consider a scenario in which the firm sells a bloatware-included product, and consumers can remove the bloatware by jailbreaking the product at some cost. By comparing the findings between the two scenarios, we characterize the impacts of the bloatware-inclusion decision by the firm and bloatware-removal decision by consumers on stakeholders’ objectives and subsequently answer our key research questions.

Our results reveal that adding bloatware and selling the product with the bloatware can be worse for the firm than selling the product without the bloatware. Hence, it is not always in the best interest of the firm to adopt the bloatware strategy. Specifically, the firm is better off with bloatware if (1) the bloatware margin that the bloatware supplier earns, and therefore the bloatware fee that the firm can charge to the bloatware supplier, is sufficiently high, or (2) the bloatware margin is moderate, but jailbreaking for consumers is costly enough. Although adding the bloatware puts downward pressure on the retail price and the overall demand for the product in both of these cases, the firm ends up making more profit by selling the bloatware-included product because the reduction in the sales revenue is recouped though revenue from the bloatware fee.

We find that even if the firm is able to make it harder for consumers to jailbreak the product, it is not always in the interest of the firm to do so. In particular, we show that the firm actually benefits from lowering the cost of jailbreaking when the bloatware margin and the jailbreaking cost are low. Intuitively, a reduction in the jailbreaking cost increases the willingness to pay of consumers who jailbreak, which, in turn, allows the firm to strategically raise its price. When the jailbreaking cost is low, the further reduction in this cost increases the total consumer demand. Although the firm makes less revenue from the bloatware fee as fewer consumers keep the bloatware even if the overall demand goes up, the firm compensates the reduction in bloatware revenue with an increase in sales revenue when the bloatware margin is low.

Conventional wisdom suggests that a reduction in the jailbreaking cost leads to higher consumer surplus because it allows more customers to remove the unwanted software. Our analysis, nevertheless, shows that a reduction in the jailbreaking cost also changes the demand dynamics of consumers who would remove the bloatware and of those who would keep the bloatware, and the proportion of these two segments of consumers, consequently, affects the consumer surplus. In particular, we show that the bloatware margin plays a crucial role in determining the overall effect of the jailbreaking cost. When the margin is high, total consumer surplus always benefits from an increase in the jailbreaking cost. Even when the bloatware margin is low, total consumer surplus benefits from an increase in the jailbreaking cost if the jailbreaking cost is already large enough. This finding implies that consumers are not necessarily better off with a lower jailbreaking cost.

Our analysis unequivocally shows that bloatware inclusion, if preferred by the firm in equilibrium, is actually a good thing for consumers as well. This is because the firm adopts the bloatware strategy only when the bloatware margin is large enough. A large bloatware margin incentivizes the firm to significantly cut its price in order to gain more demand. We show that the benefit of a price cut for consumers overweighs the disutility from the bloatware (or the cost of bloatware removal), thus resulting in a net gain in overall consumer surplus.

Finally, we analyze four extensions to show the robustness of our findings to different modeling choices In the first extension, we assume that consumer product valuation and disutility from the bloatware are correlated. In the second extension, we consider heterogeneity in the cost of jailbreaking among consumers. We conclude that the qualitative nature of our results remains the same in both extensions. In the third extension, we consider that the firm endogenizes the jailbreaking cost. Using a numerical analysis, we show that there can be an interior solution for the optimal jailbreaking cost. Hence, the firm does not necessarily prefer a higher cost to jailbreak, which is consistent with our main finding in the base model, in which we assume an exogenous cost. In our last extension, we account for an additional benefit of jailbreaking apart from bloatware removal. We show that the key finding from our base model, that the firm adopts the bloat ware strategy if the bloatware margin is large enough, continues to hold.

The rest of this paper proceeds as follows. We briefly review the relevant literature in Section 2. We present our assumptions and describe our game and its timeline in Section 3. In Section 4, we analyze different game scenarios to characterize the impact of bloatware adoption by the firm and bloatware removal by some consumers on equilibrium strategies and outcomes. We analyze four extensions in Section 5 to show the robustness of our findings to alternative modeling assumptions. Finally, we conclude the paper with a discussion of implications and future research directions in Section 6.

## 2. Literature Review

Our paper adds to the literature on pricing of information goods. Research in this literature addresses a diverse set of topics, including congestion pricing (Dewan and Mendelson 1990, Westland 1992, Gupta et al. 1997), usage-based versus fixed pricing (Sundararajan 2004, Masuda and Whang 2006), horizontal product differentiation (Dewan et al. 2003, Choudhary 2009), and vertical product differentiation (Choudhary et al. 2005, Bhargava and Choudhary 2008, Chellappa and Mehra 2018). In particular, our research is closely related to the aforementioned research stream on vertical product differentiation as bloatware inclusion effectively reduces product quality. Our paper differs prominently from the prior studies on pricing of information goods in that we study jailbreaking, that is, consumer-initiated product modification, through which consumers can remove bloatware and thus improve product value. To our knowledge, this is the first paper that studies the impact of consumer-side product quality modification on the provisioning and pricing of technology products.

Bloatware differs from most information goods in that it negatively affects consumer value. As a result, a firm’s action of including bloatware in its product reduces its product value for consumers. In this regard, our paper is related to the literature on damaged goods. The seminal work by Deneckere and McAfee (1996) shows that it can be profitable for a firm to intentionally reduce the quality of some of its products even if such reduction does not bring any cost savings. Hahn (2006) extends the analysis to the case of durable products. Anderson and Dana (2009) extend the model to a generalized price discrimination setup. Our paper differs from this stream of research in that bloatware, although damaging to consumer value, directly benefits the firm. Consumers in our study can remove the bloatware through jailbreaking and hence reverse the damage imposed by the firm, which has not been considered in prior studies.

Including bloatware in the product is a form of bundling in that consumers have to buy the hardware device and the preinstalled bloatware together. There is a rich literature on monopolistic bundling in business and economics research (Adams and Yellen 1976; Schmalensee 1984; Geng et al. 2005, 2006; Basu and Vitharana 2009; Prasad et al. 2010; Bhargava 2012). The papers by Dewan and Freimer (2003) and Bhargava and Feng (2005), in particular, are related to our paper in that they also consider the possibility that the bundled products can impose disutility for some consumers. Our paper contributes to the bundling literature by considering the possibility of product unbundling at the consumer end; jailbreaking enables a consumer to unbundle the bloatware from an electronic device. To our knowledge, this is the first paper that studies the consequences of consumerinitiated unbundling on a firm’s bundling and pricing decisions.

Our study resembles the studies on patching software products because both the product with bloatware and software with security vulnerability are modified after purchase by the actions taken by consumers. Prior studies examined the issues related to how often to apply patches to remove software vulnerabilities (Cavusoglu et al. 2008) and whether users of pirated copies should be allowed to apply patches (August and Tunca 2008). Our research differs from this literature stream in the following ways. First, consumers can take an action to remove the bloatware on their own. However, software users require a patch release from the software vendor before modifying the product with the released patch. Second, applying patches does not reduce the value that the software vendor can derive from its product. Hence, the software vendor is not at odds with software users when it comes to patching. Yet removing the bloatware reduces the value that the firm can receive from the bloatware. Third, removing the bloatware is typically a one-time decision. However, software users are required to constantly update their products with newly released patches.

Finally, our research is related to the online advertising business that fuels the web ecosystem. Publishers provide content and services to online users by displaying ads. In a sense, an electronic product that contains bloatware in this study is similar to web content or service that tracks users and displays tar geted ads. Just as consumers can jailbreak the prod uct to remove the bloatware, online users can use blocking technologies to disrupt tracking online behavior and prevent downloading of ads. However, there are subtle differences. First, although publishers rely exclusively on the ad revenue because content is mostly provided free of charge, the main source of revenue for device manufacturers is product sales. Hence, the question of whether a publisher should track users and display ads does not arise, unlike the question of whether to adopt the bloatware strategy. Second, publishers can deny serving content to online users if they have detected blocking tools. In contrast, device manufacturers cannot sell products only to those who would not jailbreak the product because jailbreaking comes only after purchase. Third, ads are dynamically assigned to publishers based on the content of the publisher and the characteristics of online users. However, there is no such fine-grained mapping in the bloatware business because device manufacturers contract with bloatware suppliers to install the same apps in many copies of the device.

## 3. The Model

We consider a monopolistic firm selling a personal electronic device (e.g., a smartphone or a tablet) to consumers. The product may include bloatware—a preinstalled piece of software—that reduces the consumers’ valuation of the product. The bloatware that is bundled with the product provides or promotes the product or service of another firm, namely, a bloatware supplier. The description of the model along with the assumptions on the payoff functions and strategy sets of each player are provided next.

## 3.1. The Firm

The firm contemplates the possibility of selling its product with bloatware and therefore has two possible strategies: the bloatware strategy, under which the firm preinstalls the bloatware from the supplier into its product, and the bloatware-free strategy, under which the firm does not preinstall any bloatware. If the firm chooses the bloatware strategy, the supplier then pays the firm a bloatware fee σ per unit of the product sold for the inclusion of its app in the product. After the decision regarding the bloatware strategy, the firm next sets the retail price of the product p for consumers.

## 3.2. Consumers

There is a continuum of consumers with a mass normalized to 1. Consumers are heterogeneous in their valuation of the product. If the firm chooses the bloatware-free strategy and sets the retail price $p ,$ consumer utility from purchase is

$$
u - p,\tag{1}
$$

where consumer valuation of the product u is uniformly distributed on [0, U], and $\bar { U } > 0$ . The distribution for variable u captures the valuation heterogeneity among consumers. It is clear that a consumer chooses not to purchase the product if $u \leq p .$

If the firm chooses to include bloatware in its product, a consumer who purchases the product then suffers disutility v from the bloatware if the consumer does not remove the bloatware from the product after purchase. This disutility may come from degradation of performance (Keane 2015), reduced storage and screen space (Dent 2014), excessive battery drain and data usage (Triggs 2014), increased security and privacy risks (Rosenblatt 2015), and annoyance (Keane 2015). We assume that consumers are heterogeneous in disutility from the bloatware; that is, v is uniformly distributed on [0, V], and $V > 0 . ^ { 2 }$

Instead of bearing the disutility from using the product with the bloatware, a consumer can choose to remove the bloatware by jailbreaking the product.<sup>3</sup> In addition to do-it-yourself tools and tutorials available online for jailbreaking (Keane 2015), consumers can also use paid services to remove unwanted software cluttering their devices (Richtel 2008). The cost of effort to remove the bloatware is a positive constant e, where $e \leq V . ^ { 4 }$ We assume that the jailbreaking (or bloatware removal) cost is exogenous and the same across all consumers in the base model.<sup>5</sup> A prospective consumer thus trades off the disutility from the bloatware v against the jailbreaking cost e to decide whether to remove the bloatware or not. Consequently, under the bloatware strategy by the firm, consumer utility from purchase is

$$
u - p - \min \{v, e \}.\tag{2}
$$

## 3.3. The Bloatware Supplier

If the firm chooses to preinstall the bloatware, the supplier of the bloatware enjoys some benefit. The benefit for the supplier can arise from the usage of the app, including revenues generated from ads shown in the app or in-app purchases. The bloatware can also facilitate a discovery role. For instance, with the help of the bloatware, consumers can sign up for a new service or buy a new product. Consequently, we assume that the bloatware supplier benefits only from consumers who choose not to remove the bloatware Furthermore, we assume that the supplier generates revenue, namely, the bloatware margin w, from each customer who keeps the bloatware. If consumers differ in terms of the bloatware margin, w can be viewed as an average bloatware margin.

Although the bloatware supplier earns revenue only from those customers who purchase the product and do not remove its bloatware, the supplier has to pay the firm a bloatware fee σ for each product sold with the bloatware. This is because device manu facturers typically charge per bloatware installation, irrespective of whether some consumers may remove the bloatware after purchase (Samson 2015). Such a fee schedule is easy to operationalize and therefore to contract on. Furthermore, it eliminates the need for after-purchase monitoring of user behavior and hence solves the enforcement problem.

We assume that the firm in our model has the power to set the bloatware fee σ. Therefore, the bloatware supplier can only accept or reject the firm’s offer. If the supplier rejects the firm’s offer, the supplier has an outside option that is normalized to zero without the loss of generality. This setup regarding the power structure between the firm and the supplier is a reasonable reflection of the consumer electronics markets for smartphones, tablets, and computers: on the device manufacturing firm side, these markets are dominated by a handful of prominent firms, such as Apple and Samsung, that command their bargaining power; on the bloatware-supplier side, there are a vast number of bloatware suppliers who face stiff competition among themselves and thus are price takers rather than price setters. In the online supplement, we relax this assumption and consider two alternative industrial structures. In the first alternative, we assume that both the firm and the bloatware have some leverage to set the bloatware fee and therefore negotiate how to share the surplus generated by the bloatware via a Nash bargaining game (Nash 1950). In the second alternative, we consider that the firm installs the bloatware produced in house rather than procuring it from an outside supplier.

We summarize the notations used in our mode along with their definitions in Table 1.

The timing of the game is depicted in Figure 1. In stage 1, the firm decides on its strategy regarding the bloatware. If the firm chooses the bloatware strategy, it also sets the bloatware fee σ. The supplier can then accept or reject the offer. In stage 2, the firm sets its retail price p. In stage $^ { 3 , }$ consumers make their purchase decisions. Finally, if the firm preinstalled the bloatware in its products, in stage 4, the consumers who purchased the product decide whether to remove the bloatware by jailbreaking the device.

Table 1. Model Parameters and Decision Variables

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td> $\mu$ </td><td>Consumer valuation of the product without the bloatware, uniform on [0, U]</td></tr><tr><td>U</td><td>The upper bound of u</td></tr><tr><td>v</td><td>Consumer disutility from the bloatware, uniform on [0, V]</td></tr><tr><td>V</td><td>The upper bound of v</td></tr><tr><td>w</td><td>Bloatware margin that the supplier earns from each purchasing consumer who does not remove the bloatware</td></tr><tr><td>e</td><td>Cost of effort to remove the bloatware (i.e., cost of jailbreaking)</td></tr><tr><td>σ</td><td>Bloatware fee from the supplier to the firm for each product sold with bloatware</td></tr><tr><td> $p_{base}$ </td><td>Retail price of the bloatware-free product</td></tr><tr><td> $p_{bl}$ </td><td>Retail price of the bloatware-included product</td></tr><tr><td>c</td><td>Marginal cost of manufacturing the product</td></tr></table>

## 4. Results

In this section, we first analyze a model in which the firm sells the product without any bloatware in a benchmark scenario. We next examine the base model in which the firm preinstalls the bloatware and sells the bloatware-included product. After that, we compare and contrast the equilibrium strategies and outcomes in these two models to understand the implications of the bloatware-inclusion decision on the bloatware fee, retail price, and bloatware-removal decisions. Finally, we characterize the firm’s best strategy regarding the bloatware, that is, whether the firm should bundle its product with the bloatware.

## 4.1. Benchmark: The Bloatware-Free Strategy

We first solve the subgame in which the firm chooses the bloatware-free strategy; that is, the firm does not include the bloatware in the product. In this scenario, the firm knows that a consumer obtains a utility of $u - p _ { \mathrm { b a s e } }$ if the consumer purchases the product, where $p _ { \mathrm { b a s e } }$ denotes the retail price of the bloatwarefree product. Hence, only consumers with $u > p _ { b a s e }$ purchase the product. Knowing that, the firm maximizes the following profit expression in which c represents the marginal cost of production. We make a technical assumption $c < U$ to ensure that the firm does not make a loss:

$$
\Pi_ {\mathrm{base}} = (1 - p _ {\mathrm{base}} / U) (p _ {\mathrm{base}} - c).\tag{3}
$$

Maximizing this profit expression gives the equilibrium price presented in Lemma 1.

Lemma 1. When the firm sells its product without the bloatware, the firm charges the equilibrium retail price of $p _ { \mathrm { b a s e } } ^ { \ast } = ( U + c ) / 2$ and earns an optimal profit of $\dot { \Pi } _ { \mathrm { b a s e } } ^ { * } \dot { = }$ $( U - c ) ^ { 2 } / ( 4 U )$

All proofs are provided in the online appendix

## 4.2. The Bloatware Strategy

We next focus on the subgame in which the firm chooses the bloatware strategy; that is, the firm includes the bloatware in the product. We analyze this subgame using backward induction (see the game timeline in Figure 1). We assume (1) that $V < 2 ( U - c ) / 3$ to rule out the trivial corner solution in which consumers with high disutility from the bloatware do not buy the bloatware-included product even if the product is offered at the marginal cost and (2) that $w < U + c -$ $V / 2 \equiv w _ { \mathrm { m a x } }$ to rule out the trivial corner solution in which giving away the bloatware-included product free is possible. Note that these two technical assumptions are not restrictive because, in practice, consumers derive the majority of their utility from the product rather than from the bloatware; thus, U is usually much larger than V and w.

Figure 1. Sequence of Events  
![](/api/attachments/F5QYZMGH/fulltext/images/9f0e8b3b0a17d802a790271277f9fcf9aac8cb089339d46b3ac716def325276b.jpg)

In stage 4, the consumer who purchased the product removes the bloatware from the product at a cost e if the bloatware disutility is greater than the jailbreaking cost $( \mathrm { i } . \mathrm { e } . , v > e )$ or keeps the bloatware otherwise $( \mathrm { i } . \mathrm { e } . , \ v \leq e )$ . For ease of exposition, hereafter we refer to the former as a high-disutility consumer and the latter as a low-disutility consumer. Consequently, in stage 3, a high-disutility consumer anticipates a utility of $u - p _ { b l } - e$ if the consumer purchases and a low-disutility consumer anticipates a utility of $u - p _ { b l } - v$ if the consumer purchases, where $p _ { b l }$ represents the price of the bloatware-included product. Recall that u and v are uniformly distributed on [0, U] and [0, V], respectively; thus, the total demand of the product from the high-disutility consumers is

$$
\gamma_ {H} = \int_ {v = e} ^ {V} \int_ {u = p _ {b l} + e} ^ {U} \frac {1}{V U} d u d v = \left(1 - \frac {e}{V}\right) \left(1 - \frac {p _ {b l} + e}{U}\right),
$$

and the total demand from the low-disutility consumers is

$$
\gamma_ {L} = \int_ {v = 0} ^ {e} \int_ {u = p _ {b l} + v} ^ {U} \frac {1}{V U} d u d v = \frac {e}{V} \left(1 - \frac {p _ {b l}}{U} - \frac {e}{2 U}\right).
$$

In stage 2 and for any given bloatware fee σ that the supplier accepts, the firm chooses a retail price $p _ { b l }$ to maximize the following profit expression:

$$
\Pi_ {b l} = \big (p _ {b l} + \sigma - c \big) \big (\gamma_ {H} + \gamma_ {L} \big).\tag{4}
$$

The next lemma characterizes the firm’s optimal pricing decision in stage 2 under the bloatware strategy.

Lemma 2. When the firm sells its product with bloatware, for any given bloatware fee $\sigma ,$ the firm charges the equilibrium retail price of $\begin{array} { r } { p _ { b l } ^ { * } ( \sigma ) = \frac { 1 } { 2 } ( U + c ) - \frac { \sigma } { 2 } - \frac { e } { 2 } + \frac { e ^ { 2 } } { 4 V } . } \end{array}$

Recall that $e \leq V .$ . Therefore, a comparison of Lemmas 1 and 2 immediately reveals that $p _ { b l } ^ { \ast } ( \sigma ) < p _ { \mathrm { b a s e } } ^ { \ast }$ . That ${ \mathrm { i } } \mathbf { s } ,$ the firm charges a lower price when the product includes the bloatware. Two dynamics contribute to this result. First, the inclusion of bloatware brings additional revenue, namely, the bloatware fee σ per product sold, to the firm. In order to optimally boost demand to derive the highest profit, the firm passes part of this bloatware revenue $( \sigma / 2 )$ to consumers in the form of a price reduction. Second, the inclusion of bloatware directly reduces the consumer’s net utility and thus consumer demand. In response, the firm further cuts its price by $\textstyle { \frac { e } { 2 } } ( 1 - { \frac { e } { 2 V } } )$ to dampen this de mand reduction.

Given the bloatware strategy, in stage 1, the firm next has to determine the optimal bloatware fee $\sigma ^ { * }$ that the supplier is willing to accept. First note that the supplier’s profit is

$$
\Pi_ {\mathrm{supplier}} = w \gamma_ {L} - \sigma (\gamma_ {L} + \gamma_ {H}).\tag{5}
$$

The term $\sigma ( \gamma _ { L } + \gamma _ { H } )$ implies that the supplier has to pay the firm a bloatware fee for each product sold even though the supplier subsequently earns revenue only from low-disutility consumers who purchase the product and do not remove the bloatware, as represented by the term $w \gamma _ { L }$

In our base model, the firm has the power to act as the Stackelberg leader in setting the bloatware fee. Consequently, the firm proposes the highest possible fee conditional on that the supplier accepts it. Therefore, the optimal bloatware fee $\bar { \sigma } ^ { * }$ results in the supplier earning a zero profit.<sup>7</sup> Setting the profit expression in Equation (5) to zero leads to the next result.

For notational convenience, we define

$$
\Omega \equiv \sqrt {8 e (2 (U - c) V - e ^ {2}) w + (2 (U - c) V - 2 e (V + w) + e ^ {2}) ^ {2}}.
$$

Proposition 1. When the firm sells its product with the bloatware, the firm proposes a bloatware fee

$$
\sigma^ {*} = \left(\Omega - 2 (U - c - e) V + 2 e w - e ^ {2}\right) / (4 V)\tag{6}
$$

to the supplier, and the supplier accepts it. Then the firm sets the equilibrium retail price at

$$
p _ {b l} ^ {*} = \left(2 (3 U + c - 3 e) V - \Omega - 2 e w + 3 e ^ {2}\right) / (8 V)\tag{7}
$$

and earns an optimal profit of

$$
\Pi_ {b l} = \left(2 (U - c - e) V + \Omega + 2 e w + e ^ {2}\right) ^ {2} / (6 4 U V ^ {2}).\tag{8}
$$

As shown in the proof, given the earlier technical assumptions, both $\stackrel { \bullet } { \sigma } ^ { * }$ and $\dot { p } _ { b l } ^ { * }$ are nonnegative, and there are positive demands from both high- and lowdisutility consumers. Because of the convoluted term <sup>Ω</sup>, it is not immediately clear from Proposition 1 how the model parameters affect the retail price and the firm profit. We next present two corollaries that characterize the impact of bloatware on various outcomes.

Corollary 1. When the firm sells its product with the bloatware, the proposed bloatware fee is equal to the bloatware margin, that is, $\boldsymbol { \sigma } ^ { * } = w \mathrm { i f } \ e \stackrel { } { = } V ,$ , and is less than th bloatware margin, that is, $\sigma ^ { * } < w \mathrm { ~ } i f e < V$

Corollary 1 shows the relationship between the bloatware margin and the bloatware fee. When $e = V ,$ which is the extreme case in which the removal cost is prohibitively high for any consumer to jailbreak the product, consequently, bloatware removal never happens. In this case, every consumer who purchases the product generates a bloatware margin w for the supplier, which, in turn, allows the firm to completely extract this gain by setting the bloatware fee equal to the bloatware margin. When $e < V ,$ however, some consumers (namely, the high-disutility consumers with $v > e )$ remove the bloatware from the product; thus the bloatware supplier no longer receives a bloatware margin from these consumers. Consequently, the firm has to lower its bloatware fee (as compared with w) to ensure that the supplier does not face a negative profit and thus accepts the proposal.

Corollary 2. When the firm sells its product with the bloatware, (a) the retail price decreases in the bloatware margin w, and (b) the firm’s profit increases in the bloatware margin w.

Corollary 2(a) follows from Proposition 1. We can observe that $\begin{array} { r } { \frac { \partial p _ { b l } ^ { * } } { \partial w } = - \frac { 1 } { 2 } ( \frac { \partial \sigma ^ { * } } { \partial w } ) } \end{array}$ . This result implies that for each unit increase in the bloatware fee resulting from a higher bloatware margin, the firm strategically shares half of that gain with customers in the form of a reduced retail price. In other words, although the bloatware directly annoys consumers because of its disutility, the bloatware can indirectly benefit consumers because of its strategic impact on the price set by the firm.

Corollary 2(b) shows that a higher bloatware margin always benefits the firm. Although the firm strategically cuts the price of its product when the bloatware margin for the supplier increases to appeal to a larger market, the firm subsequently earns more revenue from bloatware because the bloatware fee increases with the bloatware margin. Hence, the increase in the revenue from the bloatware fee is more than the reduction in sales revenue, thereby resulting in a net profit gain for the firm.

## 4.3. Does a Higher Cost of Bloatware Remova Always Bene<sup>fi</sup>t the Firm?

The cost of jailbreaking to remove the bloatware often varies among products from different industries. For example, given the long tradition of offering a root access to consumers in the PC industry, it is often easier for consumers to remove bloatware from a PC than from a smartphone. Even among products within the same industry, the jailbreaking cost can vary significantly. For instance, within the smartphone industry, some firms, such as Apple, do not release the source code of its firmware, although firms on the Android platform all share the open Android source code. As a result, it is easier to develop bloatware-removal tools on the Android platform that can circumvent manufacturer restrictions. How does the magnitude of the removal cost affect firm pricing decision and the resulting profit? In particular, are firms always better off with a higher cost of jailbreaking? We next answer this focal question.

Proposition 2. When the firm sells its product with the bloatware, (a) the retail price decreases in the jailbreaking cost e, and (b) if $w \geq V ,$ , the firm profit increases in the jailbreaking cost e. $H _ { \mathit { 0 } } < w < \bar { V } ,$ , there exists ${ \hat { e } ( w ) \in ( 0 , V ) }$ such that the firm profit decreases in the jailbreaking cost e when $e < \hat { e } ( w )$ and increases when $e > \hat { e } ( w )$ .

Proposition 2 shows that the jailbreaking cost monotonically and negatively affects the retail price. Intuitively, an increase in the removal cost reduces the willingness to pay of consumers who choose to remove the bloatware, which, in turn, forces the firm to strategically lower its price to account for the reduction in the willingness to pay. More important, Proposition 2 reveals that the firm does not necessarily benefit from a higher jailbreaking cost. The firm’s profit can actually decrease in this cost. In fact, the magnitude of the bloatware margin w plays a critical role in determining how e influences the firm’s profit. To better understand this surprising result, it is useful to consider the impact of e on the various components of the firm’s profit. Given that the supplier makes zero profit in equilibrium, from Equations (4) and (5), the firm’s equilibrium profit can be rewritten as

$$
\Pi_ {b l} ^ {*} = \big (p _ {b l} ^ {*} - c \big) \big (\gamma_ {H} ^ {*} + \gamma_ {L} \big) + w \gamma_ {L} ^ {*},\tag{9}
$$

where $\gamma _ { L } ^ { * } ( \gamma _ { H } ^ { * } )$ represents the demand in equilibrium from low-disutility (high-disutility) consumers. The profit in Equation (9) consists of two components: the retail revenue that is generated from product sales $( p _ { b l } ^ { * } - c ) ( \gamma _ { H } ^ { * } + \gamma _ { L } ^ { * } )$ and the bloatware revenue that is generated from bloatware fee ${ w \gamma } _ { L } ^ { * }$ . We know that the margin of the retail revenue $( p _ { b l } ^ { * } - { c } )$ always decreases as jailbreaking gets costlier. In the proof of this proposition, we also show that the total consumer demand $( \gamma _ { H } ^ { * } + \gamma _ { L } ^ { * } )$ decreases in e when $e < \hat { e } ( w )$ and increases in e when $e > \hat { e } ( w )$ . Thus, both the margin $( \boldsymbol { p } _ { b l } ^ { * } - \boldsymbol { c } )$ and the demand $( \gamma _ { H } ^ { * } + \gamma _ { L } ^ { * } )$ of the retail revenue decrease, thereby leading to a reduction in the retail revenue when $e < \hat { e } ( w )$ . Furthermore, we observe that when the jailbreaking cost e increases, the demand from low-disutility consumers $\gamma _ { L } ^ { * }$ always increases because of the firm’s price reduction. As a result, the firm always makes more revenue from the bloatware fee as the jailbreaking cost increases, irrespective of the magnitude of the bloatware margin. However, the reduction in retail revenue cannot be recouped by the increase in bloatware revenue when the bloatware margin w is small, that is, $w < V ,$ Thus, the firm ends up making less profit as jailbreaking gets more costly for consumers when $e < \hat { e } ( w )$ and $w < V .$ . By contrast, even if the bloatware margin w is low, that $\mathrm { i } s , w < V ,$ because the demand $( \gamma _ { H } ^ { * } + \gamma _ { L } ^ { * } )$ increases with the removal cost when $e > \hat { e } \left( w \right)$ , the reduction of the retail revenue is less severe such that the increase in the bloatware revenue compensates this reduction. As a result, the firm makes more profit as jailbreaking gets more costly for consumers when $e > { \hat { e } } ( w )$ and $w < V$ . Finally, when the bloatware margin is sufficiently high, that is, $w > V ,$ , the firm always generates more revenue from the bloatware fee to compensate the drop in the retail revenue, irrespective of the magnitude of the removal cost. To sum up, in terms of the impact of the jailbreaking cost on the firm profit, although the current level of the jailbreaking cost plays a role in determining whether the firm profit is affected negatively or positively with a change in the jailbreaking cost when the bloatware margin w is small, the current level of the jailbreaking cost has no impact on the relationship between the firm’s profit and jailbreaking cost when the bloatware margin w is large.

Our base model treats the cost to remove bloatware as an exogenously given constant. In practice, however, firms may influence the magnitude of this cost through technological and economic means. For example, Samsung uses its proprietary security platform called Knox to lock down most of its mobile products. Knox makes jailbreaking both technically hard because it is baked deeply into device bootloaders and economically punishing because tampering with Knox voids Samsung’s warranty.<sup>8</sup> It is straightforward to extend Proposition 2 into the case of endogenous bloatware-removal cost as in the next corollary.

Corollary 3. Suppose that the jailbreaking cost to remove bloatware is an endogenous and costless choice of the firm. When the firm sells its product with the bloatware, (a) if $w > V / 2 ,$ , the firm should set the jailbreaking cost as high as possible, that is, $e ^ { * } = V ,$ , and (b) $i f w > V / 2 ,$ , the firm should set the jailbreaking cost as low as possible, that is, $e ^ { * } = 0$

Proposition 2 and Corollary 3 help us understand the diverse strategies of firms with respect to the cost of removing the bloatware and, more specifically, how their strategy is related to their respective bloatware margin. For example, Samsung, for many years, has been the top global smartphone manufacturer in terms of sales.<sup>9</sup> This strong market position affords Samsung the luxury to attract and selectively preinstall apps—including bloatware—that have high rather than low potential for generating revenue, that is, apps with high w rather than low w. Accordingly, Proposition 2 and Corollary 3 suggest that Samsung should make bloatware removal costlier. This is consistent with the observation that Samsung is one of the most aggressive device manufacturers in locking its device bootloaders and in restricting many preinstalled apps as nonremovable (Limer 2015). On the contrary, HTC has a much weaker market power, which, in turn, limits its ability to attract high-revenue apps for preinstallation (and its ability to extract revenue from the developers of the preinstalled apps). Having to work with suppliers with a small w, Proposition 2 suggests that HTC may not see a profit gain by increasing the cost of bloatware removal. Furthermore, and consistent with Corollary $^ { 3 , }$ HTC finds it optimal to take a stance to make jailbreaking easy on its devices: in fact, HTC explicitly provides official support for unlocking the bootloaders on all its devices (a free service offered directly by HTC at www.htcdev.com/bootloader).

In Corollary 3, we assume that it is costless for the firm to manipulate the jailbreaking cost. This is a reasonable approximation if the firm can easily deploy existing technological tools to lock its devices: in Samsung’s case, for example, Knox has already been developed as an overall security platform that can be relatively easily configured for various levels of device lockdown. In practice, however, there are also cases in which the manipulation of the jailbreaking cost is costly: it is reported that Apple invests in significant engineering effort to continuously fight against jailbreaking.<sup>10</sup> In the PC market, in which bloatware is traditionally easier to remove, PC manufacturers are reportedly taking deliberate steps to make bloatware harder to remove (Kingsley-Hugles 2018). In Section 5.3, we study a model extension in which we explicitly model costly manipulation of the jailbreaking cost.

## 4.4. Does the Firm Bene<sup>fi</sup>t from Bloatware Inclusion?

We next address whether the firm prefers selling the product with the bloatware or without the bloatware given that jailbreaking is possible. For notational convenience, define

$$
\tilde {e} (w) \equiv \frac V (U - c + 2 w) - \sqrt {\frac {V (V (U - c + 2 w) ^ {2}}{- 1 6 (U - c) (V - w) w)}}{4 w},
$$

which takes a value within $( 0 , V )$ if $V / 2 < w < V .$

Proposition 3. Given that consumers can jailbreak at a cost e, (a) $i f w \leq V / 2 ,$ , the firm makes less profit from selling the product with the bloatware than without the bloatware, (b) if $w \geq V ,$ , the firm makes more profit from selling the product with the bloatware than without the bloatware, and (c) if $V / 2 < w < V ,$ , the firm makes more profit from selling the product with the bloatware than without the bloatware if and only $i f e > \tilde { e } ( w )$

Proposition 3 is illustrated in Figure 2. Proposition 3 has several important implications. As part (a) of this proposition demonstrates, the firm is not necessarily better off with the bloatware strategy even if the firm has the power to set the bloatware fee to extract the full surplus from the bloatware supplier. The intuition behind this result is the following. The inclusion of the bloatware has two effects on the firm profit. The direct effect is that the firm earns revenue from a new source, that is, the bloatware fee, and this revenue gets more significant as the bloatware margin increases. The indirect effect, however, is that the firm has to lower the retail price, and yet this reduction cannot avoid the drop in the overall demand and therefore the retail revenue. When the bloatware margin is small, that is, $w \le V / 2$ (illustrated in Figure 2 when $V = 1$ and $w \leq 0 . 5 )$ , the indirect effect always dominates the direct effect, thus resulting in a net profit loss for the firm. For example, it was recently announced that OnePlus 6T will be sold without any bloatware.<sup>11</sup> This is consistent with our finding that a manufacturer that cannot attract lucrative bloatware suppliers because of a lack of market dominance may find it more profitable not to include bloatware in its product.

Figure 2. Comparing Firm Profits with and Without Bloatware (When $V = 1 , c = 0 ,$ and U 3)  
![](/api/attachments/F5QYZMGH/fulltext/images/038121863f1e1cc4cef7808ce0684806eea26a7e675ca454b59bc29dc56a0bd5.jpg)

In order for the firm to benefit from the bloatware, the necessary condition is that the margin for the supplier must be sufficiently large. Specifically, the bloatware supplier must earn revenue from each product sold more than the average consumer disutility from the bloatware, that is, $\bar { w } > V / 2$ . When the bloatware margin is very high, that $\mathrm { i } s , w \geq V ,$ , as in part (b) of this proposition (illustrated in Figure 2 when $V = 1 \ \mathrm { a n d } \ w \geq 1 )$ ), the direct effect on revenue gain from the bloatware fee strictly dominates the indirect effect on retail revenue loss regardless of how costly it is for consumers to remove the bloatware. When the bloatware margin is moderate, that is, $V / 2 < w < V$ as in part (c) of this proposition, jailbreaking cost e also plays a critical role in determining whether bloatware is profitable or not. Specifically, jailbreaking cost has to be large enough $( \mathrm { i . e . , ~ } e > \tilde { e } ( w ) )$ for bloatware inclusion to be profitable. This is illustrated by the middle strip of Figure 2 when $V = 1$ and $0 . 5 < w < 1$ The intuition comes directly from Proposition 2. Basically, we can verify that for any given $w , \tilde { e } ( w ) > \hat { e } ( w )$

Therefore, the firm’s profit under the bloatware strategy increases when bloatware removal gets more costly because a large cost helps the firm lock in a large number of consumers who choose not to jailbreak. In other words, when the per-consumer bloatware margin is not very high, the firm has to prevent a large fraction of its purchasing consumers from jailbreaking so as to achieve a bloatware revenue large enough to compensate the retail revenue loss in order to benefit from the bloatware.

Proposition 3 is also consistent with our observations of the practices of Samsung (relatively high w as we argued earlier) and HTC (relatively low w). Samsung has long adopted the practice of aggressively preinstalling apps that consumers widely deem as bloatware in its devices (Limer 2015). HTC, on the contrary, has explicitly taken a stance to keep its devices relatively clean of bloatware, thus relying on less bloatware revenue (Simpson 2016).

## 4.5. Analysis of Consumer Surplus Under the Bloatware Strategy

In this section, we study consumer surplus to see how consumers are affected by the inclusion of bloatware in the product. We first assess the impact of a change in (1) the bloatware margin for the supplier and (2) the jailbreaking cost for customers, respectively, when the firm sells the bloatware-included product. We then examine how the firm’s decision on whether to include the bloatware affects the consumer surplus.

When the firm sells its product with the bloatware and consumers can jailbreak at a cost e, a highdisutility consumer purchases the product only if $u - p _ { b l } - e > 0 ,$ , and a low-disutility consumer purchases the product only if $u - p _ { b l } - v > 0$ . Therefore, total consumer surplus in equilibrium is

$$
\begin{array}{r} C S ^ {*} = \int_ {v = e} ^ {V} \int_ {u = p _ {b l} ^ {*} + e} ^ {U} \frac {u - p _ {b l} ^ {*} - e}{V U} d u d v \\ + \int_ {v = 0} ^ {e} \int_ {u = p _ {b l} ^ {*} + e} ^ {U} \frac {u - p _ {b l} ^ {*} - v}{V U} d u d v, \end{array}\tag{10}
$$

where the first (second) integration represents the sur plus for all high-disutility (low-disutility) consumers.

Proposition 4. When the firm sells its product with the bloatware and jailbreaking to remove the bloatware possible at a cost $e , ( \mathsf { a } )$ consumer surplus increases in the bloatware margin w, and (b) $i f w < V ,$ , there exists a unique $e ^ { C S } \in ( 0 , V )$ such that consumer surplus decreases in the jailbreaking cost $e f o r$ all $e < e ^ { C S }$ and increases in e for all $e > e ^ { C S }$ . If $w > V ,$ consumer surplus always increases in e.

When the bloatware margin w increases, the consumer surplus improves, as shown in Proposition 4(a) because the firm strategically cuts the price of its product (recall Corollary 2). This price reduction creates two effects that are both beneficial to consumers: first, each purchasing consumer keeps a larger surplus, and second, the total consumer demand increases, and therefore, more consumers purchase the product and enjoy some surplus.

Consumers collectively also have some influence over the jailbreaking cost. Popular jailbreaking/rooting tools and methods are often initiated at the consumer end of the market (either by tech-savvy individuals or by third-party businesses such as CyanogenMod that are more aligned with consumer interests than with manufacturer interests). A common objective of these tools is to ease the effort consumers exert in removing the bloatware; in other words, to reduce the jailbreaking cost. However, does a reduction in jailbreaking cost always result in a higher consumer surplus?

Proposition 4(b) reveals that it is not necessarily the case. The jailbreaking cost has a nonmonotonic impact on the consumer surplus. When the bloatware margin is low $( \mathrm { i } . \mathrm { e } . , w < V )$ , the consumer surplus (as a function of e) demonstrates a U-shaped behavior. That is, it decreases in e first when e is low and then increases later when e is high. To understand the intuition behind this result, we should consider the influence of the jailbreaking cost on the demand. When the jailbreaking cost increases, both segments of consumers enjoy a lower retail price. However, although the demand from low-disutility consumers increases with a price drop, the demand from high-disutility consumers decreases even with this price drop as they now have to incur a higher cost of jailbreaking. As a result, lowdisutility consumers experience a higher surplus, and high-disutility consumers enjoy a lower surplus. When the jailbreaking cost is low, the surplus drop from highdisutility consumers is greater than the surplus gain from low-disutility consumers; this is because a large fraction of the total demand originates from highdisutility consumers, and consequently, their (negative) influence on total surplus carries more weight. However, after the jailbreaking cost reaches a threshold e<sup>CS</sup>, surplus drop from high-disutility customers becomes less than surplus gain from low-disutility customers; this is because high-disutility customers no longer constitute a significant proportion of all purchasing consumers when the removal cost is already high and, therefore, cannot hurt consumer surplus as much as before. After this point, any further increase in the jailbreaking cost boosts total consumer surplus because of the positive influence of the low-disutility consumers. When the bloatware margin is high $( \mathrm { i } . \mathrm { e } . , w > V )$ , however, consumers overall always benefit from an increase in the jailbreaking cost. This is because a higher jailbreaking cost results not only in a lower equilibrium price (as explained before), but also a larger total demand (recall the discussion after Proposition 2).

Next, we analyze how the firm’s decision on whether to include bloatware affects consumer surplus.

Proposition 5. If the firm optimally adopts the bloatware strategy, consumers overall receive a higher surplus compared with the bloatware-free strategy.

Proposition 5 is very interesting because it unequivocally shows that the bloatware inclusion, if preferred by the firm in equilibrium, is actually a good thing for consumers as well. Note that this proposition does not imply that the bloatware strategy is unconditionally beneficial to consumers. It only shows that, whenever the firm is better off with adopting the bloatware strategy, consumers overall also benefit from the firm’s bloatware adoption decision. As illustrated in Figure 3, when the bloatware margin w is small, the bloatware strategy (the solid curve in the figure) can result in a lower consumer surplus than the bloatware-free strategy (the dashed line).

We can observe from Figure 3 that whenever the bloatware strategy hurts consumers overall (i.e., whenever the solid curve is below the dashed line), it also hurts the firm’s profit (i.e., the dotted line is below the dash-dotted line). Intuitively, the firm adopt the bloatware strategy only when the bloatware margin w is large enough (recall Proposition 3). But a large w also implies a large price cut, and thus more surplus, for consumers (recall Corollary 2). Proposition 5 shows that whenever w is large enough to trigger the firm to include the bloatware in its product, the bloatware margin w must also be large enough to benefit consumers overall (as compared with surplus under the bloatware-free strategy).

Proposition 5, although surprising on the first look, is actually consistent with what we observed in the Android device market. Despite the reputation of being heavily infested with bloatware, Samsung mobile devices have long been a consumer favorite in the marketplace, and Samsung has been a global leader in sales for years.<sup>12</sup> The large sales number of Samsung devices directly implies that consumers often discover the highest surplus for themselves by purchasing Samsung devices.

Note that although the overall consumer surplus improves, not all individual consumers benefit from the bloatware strategy. Consider a consumer with a large product valuation u (so that the consumer purchases the product regardless of the bloatware) and a large bloatware disutility v (so that the consumer always removes the bloatware). The consumer’s net utility from a product with (without) the bloatware is then $u - p _ { b l } ^ { * } \bar { - } e ( u - p _ { \mathrm { b a s e } } ^ { * } )$ . When w is not too large, $p _ { b l } ^ { * } + e > p _ { \mathrm { b a s e } } ^ { * } ;$ therefore, this consumer is worse off with the bloatware strategy.

Figure 3. Impact of Bloatware Margin w on Firm Profit and Consumer Surplus  
![](/api/attachments/F5QYZMGH/fulltext/images/bc54b2f221e21f87c4802006f09aaf288fb20705798b0497468f860483845f31.jpg)

## 5. Extensions

In this section, we extend our model in four directions by relaxing our basic assumptions. In the first extension, we consider the possibility of a correlation between product valuation and disutility from the bloatware. In the second extension, we consider heterogeneity in the jailbreaking cost among consumers. We show that the qualitative nature of our main result remains the same in both extensions. In the third extension, we consider that the firm endogenizes the jailbreaking cost. Finally, we extend our model to account for additional benefit of jailbreaking on top of the bloatware-removal benefit.

## 5.1. Correlation Between Consumer Product Valuation and Disutility from Bloatware

In our base model, we treated product valuation and bloatware disutility as two independent variables. One may argue that a customer who values the product more also incurs more disutility from the bloatware. This can be a reasonable argument because the customer who either uses a larger set of functions of the product and/or uses the product more frequently is likely to experience more inconvenience from the bloatware-included product. To accommodate this possibility, in this extension, we model the utility of a consumer type θ, uniformly distributed on [0, 1], who purchases the bloatware-included product as $\theta ( U \bar { \mathbf { \alpha } } - V ) - p _ { b l } .$ , where θU captures the consumer valuation for the product and $\theta V$ denotes the reduction in consumer utility because of the bloatware. Hence, unlike the base model, we assume that product valuation and bloatware disutility are perfectly correlated. Similar to the base model, a customer has an ability to remove the bloatware after purchase. If the consumer chooses to remove the bloatware, the consumer earns a utility of $\theta U - e - p _ { b l . }$ , where e is the cost of effort to remove the bloatware. All other model parameters remain the same as in the base model. We make two technical assumptions that are parallel to the technical assumptions made in Section 4 to eliminate trivial cases: (1) $c < U - V ;$ otherwise no one buys the product and keeps the bloatware even if the product is offered at the marginal cost $c ;$ and (2) $w < U - V + c ;$ otherwise giving away the bloatwareincluded product free is possible.

We next present the result regarding when to use the bloatware strategy in case of correlated product valuation and bloatware disutility, which is analogous to Proposition 3.

Proposition 6. When consumer product valuation and disutility from the bloatware are perfectly correlated, (a) if $\begin{array} { r } { e < \frac { ( U - \dot { V } + c ) V } { 2 ( U - V ) } , } \end{array}$ , the firm never prefers the bloatware strategy, and (b) $\begin{array} { r } { i f e > \frac { ( U - V + c ) V } { 2 ( U - V ) } , } \end{array}$ , the firm prefers the bloatware strategy if and only if $w > \frac { ( U - C ) ^ { \cdot } U V ( 2 e U - ( U + c + 2 e ) V + V ^ { 2 } ) - \Phi } { U ( 4 e ^ { 2 } U ( U - V ) - 8 e U V ( U - V ) - V ^ { 2 } ( c ^ { 2 } - 2 c U - U ( 3 U - 4 V ) ) } .$ , where

$$
\Phi \equiv \sqrt {\frac {(U - c) ^ {2} U (U - V) V ^ {2}}{\cdot (2 e U (U - c) + \big (c ^ {2} - U (2 e - U)) V + U V ^ {2} \big) ^ {2}}}.
$$

The firm chooses not to bundle its product with the bloatware when the jailbreaking cost is low $( \mathrm { i . e . , }$ $e < ( U - V + c ) V / ( 2 ( U - V ) ) )$ because the firm knows that every purchasing consumer removes the bloatware and the firm is not able to earn any revenue from it. Adding bloatware also forces the firm to charge a lower price. Therefore, the bloatware-free strategy dominates the bloatware strategy in this case. When the jailbreaking cost is high enough (i.e., $e > ( U -$ $V + c ) V / ( 2 ( U - V ) ) )$ , only high-type consumers, that is, those with $\theta > ( e / V )$ , remove the bloatware, and therefore, the bloatware strategy becomes feasible. However, in order for the bloatware strategy to generate more profit relative to the bloatware-free strategy, the bloatware margin must be sufficiently large. This is consistent with the result obtained from the base model reported in Proposition 3.

## 5.2. Heterogeneity in the Jailbreaking Cost Among Consumers

In our base model, we assumed that each consumer incurs the same jailbreaking cost when the consumer removes the bloatware from the product. However, the removal cost may also depend on the technical skill sets of the consumer in terms of jailbreaking the electronic device. It is possible that tech-savvy customers can easily remove the bloatware by themselves and, therefore, incur a lower cost than nontech-savvy customers, who may have to pay some amount to get outside help to do the same thing. In this extension, we relax the assumption that the jailbreaking cost among consumers is the same. Specifically, we consider two types of consumers who differ in terms of jailbreaking cost: tech-savvy and non-tech-savvy consumers. We assume that $1 - \beta$ fraction of consumers are tech savvy and incur $e _ { L }$ and $\beta$ fraction are non–tech savvy and incur $e _ { H }$ to remove the bloatware, where $e _ { L } < e _ { H } \leq V .$ . Without loss of generality, we further assume that $e _ { L } = 0$ . We keep the rest of the parameters the same. It is easy to verify that some non-tech-savvy consumers keep the bloatware and some other non-tech-savvy consumers remove the bloatware depending on the magnitude of their disutility in relation to the removal cost. By contrast, all tech-savvy consumers choose to remove the bloatware. Hence, unlike the base model, consumers’ best strategies regarding the bloatware-removal decision depend on their type.<sup>13</sup> The following result characterizes the region in which the bloatware strategy is more profitable compared with the bloatware-free strategy in case of heterogeneous jailbreaking cost.

Proposition 7. When consumers are heterogeneous in terms of the jailbreaking cost, the firm makes more profit with the bloatware strategy if and only if

$$
w > \frac {(U - c) (2 V - e _ {H}) V}{2 (U - c - e _ {H}) V + 2 \beta e _ {H} (2 V - e _ {H})}.\tag{11}
$$

Consistent with the base model in which jailbreaking cost is assumed to be the same across all consumers, the firm adopts the bloatware strategy only when the bloatware margin is sufficiently large. The threshold bloatware margin in Proposition $7$ is decreasing in the cost of jailbreaking among non-techsavvy consumers. Hence, the firm is more likely to adopt the bloatware strategy when non-tech-savvy consumers find it more difficult to get rid of the bloatware. This is because as the jailbreaking cost for non-tech-savvy consumers increases, a larger fraction of them prefers to keep the bloatware. This, in turn, allows the firm to charge a higher bloatware fee to the supplier, thereby enabling the firm to make more revenue from the bloatware. Our result implies that even if one group of consumers can costlessly remove the bloatware, the firm can still adopt the bloatware strategy as long as the bloatware margin is large enough. Hence, all consumers having to incur a cost to remove the bloatware is not a necessary condition for the firm to benefit from the bloatware strategy. In summary, modeling two types of users in terms of technical skills and therefore the jailbreaking cost does not change the qualitative nature of the main result reported in Proposition 3.

## 5.3. Endogenous Cost of Jailbreaking

In this section, we consider a model variant in which the firm, by exerting some effort, can influence the consumer-side cost of jailbreaking e under the bloatware strategy. That is, the choice of jailbreaking cost is assumed to be endogenous. Basically, we seek to determine the optimal level of jailbreaking cost from the perspective of the firm. In practice, firms are able to influence the magnitude of this cost through various technological or economic means. For example, some leading smartphone manufacturers, such as Apple and Samsung, do not offer customers root access to their devices, which is a striking departure from the common practice in the PC industry, in which consumers always have root access. As a result, it is harder for consumers to remove bloatware from root-locked smartphones than from PCs. Furthermore, some manufacturers even void their product warranties once the firmware in the product is tampered with (which is often necessary for jailbreaking). Hence, firms are using a variety of mechanisms to increase the cost of jailbreaking and thereby to deter bloatware removal.

Before we proceed, we want to note that our key findings in the base model are robust to this model variation. That is, Propositions 1–3 all hold regardless of whether e is exogenous or endogenous.

In practice, manipulation of the consumer-side jailbreaking cost is a costly activity. Significant research and development (R&D) in hardware and software design, including encryption, are necessary for effective lockdown of an electronic device against postsale tampering. For example, companies such as Apple invest in significant engineering effort to continuously fight against jailbreaking. Samsung puts its proprietary Knox security platform—a combination of dedicated security hardware and software—into most of its flagship cell phone products.

To illustrate the impact of costly firm-side effort on the firm’s choice of $e ,$ we conduct a numerical anal ysis. We model the firm-side effort as a one-time R&D cost $\beta e ^ { 2 }$ that takes place before the product goes to mass manufacturing. The convex form of this firmside cost function is also consistent with the extant literature and accounts for the fact that it is increasingly harder for a firm to develop mechanisms to deal with more sophisticated jailbreaking techniques, such as a dedicated encryption chip and customized lock on the bootloader. Figure 4 shows the relationship between the magnitude of $\beta$ and the firm’s optimal choice of the jailbreaking cost e when $w > V / 2 . ^ { \circ }$ 14

We can clearly observe from Figure 4 that when $\beta$ is small, the firm sets the maximum jailbreaking cost $( \mathrm { i . e . , } e = V )$ . However, when $\beta$ is large enough, the firm’s optimal choice of e becomes a decreasing function of $\beta$ and is an inner solution between zero and $V .$ Intuitively, this optimal choice of e balances the firm’s marginal gain from making jailbreaking difficult for consumers with the firm’s marginal cost of the effort $\beta e .$ . We replicated the numerical analysis with various combinations of parameter values, and the results are qualitatively similar to the figure. Hence, we can conclude that when setting the jailbreaking cost, it is possible that the firm can neither make jailbreaking effortless nor make it prohibitively difficult $( \mathrm { i . e . , }$ there can be an interior solution for the optimal level of jailbreaking cost).

## 5.4. Additional Jailbreaking Bene<sup>fi</sup>t

In our base model, we assume that the benefit of jailbreaking for consumers comes solely from bloatware removal. In practice, however, it is possible for jailbreaking to benefit consumers in more ways than bloatware removal.<sup>15</sup> For example, jailbreaking provides users with the freedom to flash a custom ROM, gain unrestricted control of their device settings, tweak hidden features based on their needs, block mobile ads, or install otherwise restricted apps (Gordon 2013, Thomas 2017). We study the consequences of an additional benefit of jailbreaking (on top of the bloatwareremoval benefit) in this section.

To do so, we extend our base model by introducing a new dimension of consumer heterogeneity: we assume that a λ proportion of consumers—called type-J consumers—receives an additional benefit J from jailbreaking on top of the bloatware-removal benefit; the remaining $1 - \lambda$ proportion of consumers—called type-N consumers—does not receive such an additional benefit. For example, some consumers enjoy tweaking hidden settings, and others are satisfied with the factory settings. Note that now consumers are differentiated on three dimensions: utility from product purchase (u), disutility from bloatware (v), and additional jailbreaking benefit $\left( J \thinspace \mathrm { o r } \thinspace 0 \right)$ . We assume that this last dimension of consumer heterogeneity is independent of the other two dimensions, which helps us isolate the role of this additional jailbreaking benefit in driving the new insights in this section.

![](/api/attachments/F5QYZMGH/fulltext/images/288185522a7f65db9de1ad97bebef8d0a154e2c8471a374b8b5a24abfeef3427.jpg)

We tighten our assumption (a) in the base model, that is, $\smile { < } 2 ( U - c ) / 3 ,$ , to a new one, $V < ( U - c ) / 2$ , to continue to rule out the trivial corner solution of high disutility consumers refusing to buy even a free product. We also assume that J cannot be too large, that is, $J < ( 2 V + e ) / 3 ,$ , to rule out the corner solution in which the firm sets a very high price that none of the type-N consumers purchase.

The solution to the benchmark—that is, the subgame in which the firm chooses the bloatware-free strategy—now depends on the relative sizes of this additional jailbreaking benefit J and the jailbreaking cost e. If $J \leq e ,$ the benchmark solution in our base model still holds. I $\begin{array} { r } { J > e , } \end{array}$ however, it is beneficial for type-J consumers to jailbreak a product even without any bloatware because doing so increases their utility by $J - e .$ . Consequently, the firm faces a new benchmark profit:

$$
\begin{array}{r l} \Pi_ {\text {base}} & = (p _ {\text {base}} - c) [ (1 - \lambda) (1 - p _ {\text {base}} / U) \\ & \quad + \lambda (1 - (p _ {\text {base}} - J + e) / U) ], \quad \text {if} J > e. \end{array}\tag{12}
$$

Lemma 3. Assume that some consumers gain an additional benefit J by jailbreaking the product. When the firm sells its product without the bloatware, the firm charges the equilibrium retail price of $p _ { \mathrm { b a s e } } ^ { \ast } = ( U \dot { + } c + \lambda ( J ^ { - } e ) ^ { + } ) / 2$ and earns an optimal profit of $\mathrm { \bar { I } _ { b a s e } ^ { * } } = ( U - c + \lambda ( J - e ) ^ { + } ) ^ { 2 } /$ 4U , where $( J - \dot { e } ) ^ { + } \dot { \triangleq } \operatorname* { m a x } \{ 0 , J - e \}$

This lemma shows that a high enough additional jailbreaking benefit results in a greater firm profit in the benchmark. This is intuitive because jailbreaking benefits type-J consumers even without any bloatware if $J > e ,$ and the firm extracts part of this benefit through a higher price.

We next study the subgame in which the firm includes the bloatware in the product. Now we need to consider four subgroups of demands:

• Total demand from type-N consumers with $v > e$ is $\begin{array} { r } { \gamma _ { N H } = ( 1 - \lambda ) ( 1 - \frac { e } { V } ) ( 1 - \frac { p _ { b l } + e } { U } ) } \end{array}$

• Total demand from type-N consumers with $v \leq e$ is $\begin{array} { r } { \gamma _ { N L } = ( 1 - \lambda ) \frac { e } { V } ( 1 - \frac { p _ { b l } } { U } - \frac { e } { 2 U } ) } \end{array}$

• Total demand from type-J consumers with $v >$ $\begin{array} { r } { e - J \mathrm { i s } \gamma _ { J H } = \lambda ( 1 - \frac { ( e - J ) ^ { + } } { V } ) ( 1 - \frac { \bar { p } _ { b l } + e - J } { U } ) } \end{array}$

• Total demand from type-J consumers with $v \leq$ $\begin{array} { r } { e - J { \mathrm { i s } } \ \gamma _ { J L } = \lambda { \frac { ( e - J ) ^ { + } } { V } } ( 1 - { \frac { p _ { b l } } { U } } - { \frac { \bar { e } - J } { 2 U } } ) } \end{array}$

Then we can write the firm and supplier profits as $\Pi _ { b l } = ( p _ { b l } + \sigma - c ) ( \gamma _ { N H } + \gamma _ { N L } + \gamma _ { I H } + \gamma _ { I L } )$ and $\mathrm { \bar { I } \Pi _ { s u p p l i e r } = }$ $w ( \gamma _ { N L } + \gamma _ { J L } ) - \sigma ( \gamma _ { N H } + \gamma _ { N L } + \dot { \gamma } _ { J H } + \dot { \gamma } _ { J L } ) .$ , respectively. We solve the model using backward induction. To keep the main text concise, we put the analytical details in the proof of the following proposition in the online appendix. For ease of exposition, define

$$
\hat {w} \triangleq \left\{ \begin{array}{l l} (U - c) V (2 e (V + J \lambda) - e ^ {2} \\ \quad - J (J + 2 V) \lambda) \\ \hline 2 \big (e (U - c + e) V - e ^ {3} - J ((U - c + J) V \\ - 3 e ^ {2} + e (J + 2 V)) \lambda + J ^ {2} (2 V - 2 e + J) \lambda^ {2} \big) \\ \frac {(U - c) V \big (2 e V - e ^ {2} (1 - \lambda) - 2 J V \lambda \big)}{2 e (1 - \lambda) \big (e V - e ^ {2} (1 - \lambda) + V (U - c - 2 J \lambda) \big)}, \text {if} J > e. \end{array} \right.\tag{13}
$$

We then have the following result.

Proposition 8. Assume that some consumers gain an additional benefit J by jailbreaking the product: $\left( \mathrm { a } \right) \dot { i } f w \ge \hat { w } ,$ , the firm adopts the bloatware strategy and receives a profit of $\begin{array} { r } { \dot { \Pi } _ { b l } ^ { * } = ( \dot { 2 } ( U - c - e ) V + R + 2 e w + e ^ { 2 } ) ^ { 2 } / ( 6 4 U V ^ { 2 } ) ; } \end{array}$ (b) otherwise, the firm adopts the bloatware-free strategy and receives a profit of $\Pi _ { \mathrm { b a s e } } ^ { * ^ { * } } = ( U - c + \lambda ( { \overset { . } { J } } - e ) ^ { + } ) ^ { 2 } / { \overset { . } { ( 4 U ) } }$

Term R is a complex expression that is defined in the proof of this proposition. In the special case of $J = 0 ,$ , R degenerates to $\Omega ,$ and this proposition degenerates to Proposition 3 in the base model.

Proposition 8 shows that the key message from our study, that the firm adopts the bloatware strategy only when the bloatware margin is sufficiently large (as in Proposition 3), continues to hold in this model extension with additional jailbreaking benefit.

We next study the impact of this additional jailbreaking benefit J on the firm’s profit. One might intuitively think that because a higher J always results in a (weakly) higher consumer utility, it would enable the firm to always extract a higher profit. The next proposition, however, show that a higher J does not always results in a higher firm profit.

Proposition 9. Assume that some consumers gain an additional benefit J by jailbreaking the product and $w > V .$ When the firm sells its product with the bloatware, the firm’s profit decreases in J i $ { \boldsymbol { \mathsf { c } } } _ { J } <  { \boldsymbol { e } }$ and increases in J $i f J > e$

This proposition shows that a higher additional jailbreaking benefit J actually hurts the firm’s profit as long as J is not large enough $( \mathrm { i . e . , } J < e )$ . To see the intuition, first notice that a higher J has two opposite effects on the firm’s profit. First, a higher J directly implies that type-J consumers value the product more if they jailbreak, and such increased consumer valu ation positively affects the firm’s profit; we call this the direct effect of the additional jailbreaking benefit Second, the more consumers jailbreak because of a higher J, the fewer consumers keep the bloatware, which generates less revenue from the bloatware for the firm; we call this the indirect effect of the additiona jailbreaking benefit. When J is relatively small, the direct effect is dominated by the indirect effect; thus, a higher J results in net profit loss for the firm. By contrast, when J is large enough $\left( \mathrm { i } . \mathrm { e } . , J > e \right)$ , the direct effect dominates the indirect effect; thus, a higher J results in a net profit gain for the firm.

Proposition 9 is illustrated in Figure 5(a). Note that there is a kink point at $J = e .$ . To see why, notice that type-J consumers contribute to the aforementioned indirect effect when $J < e ;$ that is, the higher $J { \mathrm { ~ i s } } ,$ the fewer type-J consumers choose to keep the bloatware. $\operatorname { A t } J = e ,$ , none of the type-J consumers choose to keep the bloatware, and thus, a further increase in J does not lead to any further uninstallation of the bloatware by type-J consumers; that is, the indirect effect no longer applies. This kink point in Figure $5 ( \mathrm { a } )$ reflects the fact that the aforementioned indirect effect applies to type-J consumers when $J < e$ but not when $J \geq e .$

When $w < V ,$ , an analytical result between firm profit and J is unavailable because of the highly compli cated profit expressions. We conducted an extensive numerical study under $w < V ,$ and the finding in Proposition 9 that the firm profit first decreases in J and then increases in J is robust. In addition, if w is small enough, it is possible that the firm’s profit does not always decrease in J when $J < e ,$ as illustrated by Figure 5(b). In this illustration with $e = 0 . 6 ,$ , the firm’s profit starts increasing after $J = 0 . 4 5 < 0 . 6$ . Intuitively, a small w means a weaker indirect effect, and thus, the direct effect may dominate the indirect effect even before all type-J consumers jailbreak.

In summary, we show that the findings in our base model are robust when we consider the additional benefit of jailbreaking on top of the bloatware-remova benefit. An important new finding in this section is that a higher additional jailbreaking benefit does not always translate into a higher firm profit: although additional jailbreaking benefit increases the firm’s product revenue, it also decreases the firm’s bloatware revenue, and their trade-off determines the net impact on the firm profit.

## 6. Conclusion

Whether to include bloatware in products is a crucial question to answer for many firms in the consumer electronics market. Some firms sell bloatware-included products, and others sell bloatware-free products.

Figure 5. Firm Profit as a Function of Additional Jailbreaking Benefit J (When $V = 0 . 8 , e = 0 . 6 , c = 0 , U = 3 . 2 ,$ , and $\lambda = 0 . 5 )$  
(a)  
![](/api/attachments/F5QYZMGH/fulltext/images/798eae72478401b4e8c0b1249a6e56962b8ebea6823a5cc083f2083c074c9877.jpg)  
Notes. (a) When $w > V$ (parameter value $w = 1 )$ . (b) When $w < V$ (parameter value $w = 0 . 5 )$ ).

(b)  
![](/api/attachments/F5QYZMGH/fulltext/images/8b557bcbea6b7e463818a65440cc7390c295456acf77022e531d1a34a027f77a.jpg)

From the vantage point of a monopolistic firm that can preinstall an app of a third party for a fee and sell the product bundled with bloatware to consumers, this paper investigates the bloatware-inclusion decision of the firm. Motivated by an increasing phenomenon of jailbreaking of electronic devices to remove unwanted applications that come with the devices, our gametheoretic model incorporates the ability of consumers to eliminate the bloatware after purchase by incurring some cost. Hence, a consumer is treated not only as a passive entity deciding whether to purchase the product but also as a strategic actor deciding whether to remove the bloatware if included in the product purchased. In response, in our model, the firm anticipates the possibility of jailbreaking by some purchasing consumers and the amount of bloatware fee that the bloatware supplier is willing to pay when deciding on the bloatware inclusion and the product pricing strategies.

When the firm sells the product with the bloatware, we find that the firm strategically reduces the price of its product for consumers and charges a bloatware fee that is not higher than the bloatware margin for the supplier. Despite the appeal of the bloatware strategy and the additional source of revenue that comes from the bloatware, our analysis reveals that selling the product bundled with bloatware can indeed be worse than selling the product free of bloatware. Specifically, when the bloatware margin for the supplier is not high enough, the firm’s best strategy is to sell a bloatware-free product. This is because when the bloatware margin is low, the bloatware fee that the supplier is willing to pay is also low. Consequently, the firm cannot recover the reduction in sales revenue because of the reduced price and reduced demand through the revenue from the bloatware fee.

We next turn our attention to the question of whether the firm should make jailbreaking harder for customers as the basic intuition would suggest.

We show, interestingly, that the firm does not always favor a higher cost of jailbreaking. In particular, when both the bloatware margin and the jailbreaking cost are low, the firm prefers even a lower cost of jailbreaking. This is because a lower jailbreaking cost allows the firm to make more profit by strategically increasing the price of the product and, at the same time, by expanding the consumer demand, even though the revenue from the bloatware shrinks. However, when the bloatware margin is sufficiently high, or the margin is low but the jailbreaking cost is high, the firm then prefers even a higher cost of jailbreaking for consumers. This is because the increased bloatware revenue resulting from an increased cost of jailbreaking compensates the reduction in sales revenue.

Although the basic intuition suggests that a reduction in the jailbreaking cost results in a higher consumer surplus because a lower cost makes it easier for more customers to remove the unwanted software, our results reveal that it is not always the case. We show that the reduction in the jailbreaking cost improves the consumer surplus only if both the bloatware margin and the jailbreaking cost are low. However, if the bloatware margin or the jailbreaking cost is high, consumers can actually benefit from an increase in the jailbreaking cost. This is because the surplus drop from consumers who incur a higher jailbreaking cost to remove the bloatware is completely washed away by the surplus gain from consumers who pay a lower price and keep the bloatware.

Finally, we show that when the firm prefers to adopt the bloatware strategy, consumers as a whole benefit from this decision. Because the firm always passes part of bloatware revenue to consumers in the form of a lower product price, a higher bloatware margin, which is a necessary condition for the firm to adopt the bloatware strategy, also implies a bigger price cut for consumers. As a result, whenever the firm optimally chooses to offer its product with the bloatware, this decision always leads to a win–win situation for the firm and consumers.

We also analyzed several extensions under different modeling assumptions to show the robustness of our results. Namely, we first assumed that the disutility from the bloatware depends on the product valuation. We then assumed that consumers are heterogeneous in terms of the cost of removing the bloatware. We concluded that qualitative nature of our results remains the same in both extensions. In the third extension, we assumed that the firm endogenizes the jailbreaking cost. We showed that the firm is not necessarily better off with a higher cost incurred by consumers to remove the bloatware even if the firm can optimally set the jailbreaking cost. Finally, in the fourth extension, we accounted for an additional benefit of jailbreaking on top of the bloatware-removal benefit. We showed that this additional benefit of jailbreaking increases the firm’s product revenue yet decreases its bloatware revenue; thus, the net profit impact depends on the trade-off of these two opposite effects.

Our study is not without limitations. We studied a monopolistic firm to provide insights into the bloatware-inclusion strategy. Future research can expand our model to a situation in which there is competition between firms for consumers in the market. Our model also assumed that the firm sells one kind of product: either a bloatware-free or a bloatwareincluded product. This assumption connects well with many business practices. For example, Samsung phones sold in the United States all come with roughly the same set of apps; all Samsung phones suffer from consumer criticism of too much bloatware. That being said, future research can investigate how offering both kinds of products—that is, bloatware-free and bloatware-included products—in the market can impact the firm’s pricing strategy and the resulting profit in addition to the impact on the consumer surplus. In the mobile industry, both device manufacturers and network carriers may install bloatware, and carriers consistently prefer device manufacturers to make jailbreaking difficult.<sup>16</sup> Future research can explore how the interplay between original equipment manufacturers and the carriers affects the bloatware strategy at different levels by incorporating device subsidies paid by carriers.

We believe that bloatware will be an even more controversial and important topic in the future as consumers increasingly adopt wearable technologies and connected devices, and their manufacturers can push for more bloatware. We hope that this work, with its limitations, paves the way for more research on this topic.

## Acknowledgments

The authors contributed equally to this manuscript. The authors are grateful for the valuable, clear, and constructive feedback from Senior Editor Yong Tan, the associate editor, and three anonymous reviewers.

## Endnotes

<sup>1</sup> Not all preinstalled apps are categorized as bloatware. Bloatware refers to unwanted apps only. Hence, programs that are perceived to be valuable by users, such as Adobe Reader, are not considered to be bloatware.

<sup>2</sup> In the base model, we assume that u and v are independent; in Section 5.1, we change the model setup to accommodate a possibility of correlation between product valuation and disutility from the bloatware.

<sup>3</sup> Although jailbreaking is usually necessary for bloatware removal, the latter is not the only benefit from the former. For example, some consumers jailbreak their devices to gain the capability to instal otherwise restricted apps. In Section 5.4, we explicitly account for such additional benefits of jailbreaking beyond bloatware removal.

<sup>4</sup> This assumption does not limit the generality of the model because any e > V results in the same consumer behavior of not removing the bloatware as e = V.

<sup>5</sup> We relax this assumption and consider heterogeneity among consumers in jailbreaking cost in Section 5.2.

<sup>6</sup> If the firm charges a fee for only consumers who do not remove the bloatware, the firm has to monitor the behavior of the customers after purchase. This is not practical and, therefore, not easily enforceable. Alternatively, the firm can rely on information shared by the supplier regarding bloatware usage. However, this information sharing is not credible because the supplier’s dominant strategy would be to overreport bloatware removal.

<sup>7</sup> Strictly speaking, the firm’s choice of σ should result in an infinitesimally small yet still positive profit for the supplier so that the supplier strictly prefers accepting the proposal

<sup>8</sup> “Samsung Knox: A Closer Look at Samsung’s Security Platform,” available at https://www.digit.in/mobile-phones/samsung-knox-a -closer-look-at-samsungs-security-platform-41257.html.

<sup>9</sup> “Samsung Tops Global Smartphone Market,” available at https:// www.gadgetsnow.com/tech-news/samsung-tops-global-smartphone -market-huawei-biggest-gainer-idc/articleshow/64014781.cms.

<sup>10</sup> “Apple to Actively Fight Against Jailbreaking,” available at http://www.iphoneness.com/news/apple-to-actively-fight-against -jailbreaking/.

<sup>11</sup> “The OnePlus 6T Will Be Sold by a U.S. Carrier, Surprisingly Without Bloatware,” available at https://www.forbes.com/sites bensin/2018/10/30/the-oneplus-6t-will-be-sold-by-a-u-s-carrier -surprisingly-without-bloatware/.

<sup>12</sup> http://gs.statcounter.com/vendor-market-share/mobile.

<sup>13</sup> The objective of using heterogeneous jailbreaking costs is to fix the equilibrium strategy of one group of consumers with regard to jailbreaking. Therefore, it is also possible to assume that 0 < e < V e so that non-tech-savvy consumers always keep the bloatware and tech-savvy consumers keep or remove the bloatware depending on their disutility and the jailbreaking cost. Solving the model with this assumption does not change the qualitative results reported in this extension.

## References

Adams WJ, Yellen JL (1976) Commodity bundling and the burden of monopoly. Quart. J. Econom. 90(3):475–498.

Anderson ET, Dana JD (2009) When is price discrimination profit able? Management Sci. 55(6):980–989.

August T, Tunca T (2008) Let the pirates patch? An economic analysis of software security patch restrictions. Inform. Systems Res. 19(1): 48–70.

Basu A, Vitharana P (2009) Impact of customer knowledge hetero geneity on bundling strategy. Marketing Sci. 28(4):792–801.

Bhargava HK (2012) Retailer-driven product bundling in a distri bution channel. Marketing Sci. 31(6):1014–1021.

Bhargava HK, Choudhary V (2008) Research note: When is ver sioning optimal for information goods? Management Sci. 54(5): 1029–1035.

Bhargava HK, Feng J (2005) America OnLine’s internet access service: How to deter unwanted customers. Electronic Commerce Res. Appl. 4(1):35–48.

Brandom R (2015) Lenovo promises less bloatware on its new computers. The Verge (February 27), https://www.theverge.com 2015/2/27/8120793/lenovo-bloatware-superfish-windows-10.

Cavusoglu H, Cavusoglu H, Zhang J (2008) Security patch management—Share the burden or share the damage? Man agement Sci. 54(1):657–670.

Chellappa RK, Mehra A (2018) Cost drivers of information versioning: Pricing and product line strategies for information goods. Management Sci. 64(5):2164–2180.

Choudhary V (2009) Use of pricing schemes for differentiating information goods. Inform. Systems Res. 21(1):78–92.

Choudhary V, Ghose A, Mukhopadhyay T, Rajan U (2005) Personalized pricing and quality differentiation. Management Sci. 51(7): 1120–1130.

Dachis A (2011) How to get the most out of your jailbroken iOS device. Lifehacker.com (March 14), https://lifehacker.com/how -to-get-the-most-out-of-your-jailbroken-ios-device-5781437.

Deneckere RJ, McAfee RP (1996) Damaged goods. J. Econom. Man agement Strategy 5(2):149–174.

Dent S (2014) Shocker! Nobody uses Samsung bloatware. Engadg et.com (April 23), https://www.engadget.com/2014/04/23 shocker-nobody-uses-samsung-bloatware.

Dewan R, Freimer M (2003) Consumers prefer bundled add-ins. J. Management Inform. Systems 20(2):101–113.

Dewan R, Jing B, Seidmann A (2003) Product customization and price competition on the internet. Management Sci. 49(8):1055–1070.

Dewan S, Mendelson H (1990) User delay costs and internal pricing for a service facility. Management Sci. 36(12):1502–1517.

Geng X, Stinchcombe MB, Whinston AB (2005) Bundling information goods of decreasing value. Management Sci. 51(4):662–667.

Geng X, Stinchcombe MB, Whinston AB (2006) Product bundling. Hendershott T, ed. Handbook of Economics and Information System (Elsevier, Amsterdam), 499–525.

Gordon W (2013) Top 10 reasons to root your Android phone. Life hacker.com (August 10), https://lifehacker.com/top-10-reasons-to -root-your-android-phone-1079161983.

Gupta A, Stahl D, Whinston AB (1997) A stochastic equilibrium model of internet pricing. J. Econom. Dynamics Control 21(4–5): 697–722.

Hahn J-H (2006) Damaged durable goods. RAND J. Econom. 37(1): 121–133.

Horowitz M (2015) Bloatware free Windows Computers. Computerworld (February 28), http://www.computerworld.com/article 2890512/bloatware-free-windows-computers.html.

Keane J (2015) Buying a PC this year? Here’s what you need to know about bloatware. Digital Trends (May 25), http://www.digitaltrends.com computing/the-state-of-pc-bloatware-in-2015/.

Kingsley-Hugles A (2018) Crapware: Why manufacturers install it, what you can do about it, and why it’s not going to go away. ZDNet (April 9), https://www.zdnet.com/article/crapware-wh -manufacturers-install-it-and-what-you-can-do-about-it/.

Limer E (2015) The Samsung Galaxy S6 has as much bloatware as ever. Gizmodo.com (March 26), https://gizmodo.com/the-samsung -galaxy-s6-has-as-much-bloatware-as-ever-1693717539.

Lucic K (2014) Over 27.44% users root their phone(s) in order to remove built-in apps, are you one of them? AndroidHeadlines, https://www.androidheadlines.com/2014/11/50-users-root -phones-order-remove-built-apps-one.html/

Masuda Y, Whang S (2006) On the optimality of fixed-up-to tariff for telecommunications service. Inform. Systems Res. 17(3): 247–253.

McDaniel P (2012) Bloatware comes to the smartphones. IEEE Se curity Privacy 10:4 85–87.

Nash J (1950) The bargaining problem. Econometrica 18(2):155–162

Newman J (2014) Friday rant: The ever-sorrier state of Android bloatware. Time.com (May 9), https://time.com/94646/android -bloatware/.

Pinola M (2012) Here’s all the crapware that comes with new Windows 8 PCs. ITworld.com (November 21), https://www.itworld.com article/2718342/here-s-all-the-crapware-that-comes-with -new-windows-8-pcs.html

Prasad A, Venkatesh R, Mahajan V (2010) Optimal bundling of technological products with network externality. Management Sci. 56(12):2224–2236.

Richtel M (2008) Industry rethinks moneymaking software practice New York Times (August 27), https://www.nytimes.com/2008 08/28/technology/28software.html.

Rosenblatt S (2015) Lenove’s Superfish security snafu blows up in its face. CNET (February 20), http://www.cnet.com/news/superfish -torments-lenovo-owners-with-more-than-adware/.

Samson J (2015) The future of bloatware, making a buck a phone. XDA Developers (August 24), http://www.xda-developers.com future-of-bloatware-digital-turbine/.

Schmalensee R (1984) Gaussian demand and commodity bundling J. Bus. 57(1):S211–S230.

Simpson C (2016) The HTC 10: A great camera, all metal, no bloatware. Gizmodo.com.au (April 12), https://www.gizmodo.com.au/2016 04/the-htc-10-a-great-camera-all-metal-no-bloatware/.

Spence E (2015) Bloatware ready to overpower Android Lollipop. Forbes Tech, https://www.forbes.com/sites/ewanspence/2015 03/08/crapware-to-infect-android/#6b2ae81a397f.

Sundararajan A (2004) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

Thomas D (2017) The 5 best phones for rooting & modding. Gadget Hacks (October 29), https://android.gadgethacks.com/how-to 5-best-phones-for-rooting-modding-0175988/.

Triggs R (2014) Named and shamed: The worst battery and per formance sapping apps. AndroidAuthority.com (November 6), https://www.androidauthority.com/worst-performance-sapping -apps-564689/.

Westland C (1992) Congestion and network externalities in the short run pricing of information system services. Management Sci. 38(7):992–1009.

Yegulalp S (2012) Crapware lives on Windows 8. InformationWeek.com (November 1), https://www.informationweek.com/crapware -lives-on-windows-8/d/d-id/1107182.
