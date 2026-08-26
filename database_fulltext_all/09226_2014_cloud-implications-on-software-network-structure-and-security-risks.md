---
otero_id: 9226
otero_key: "D28WAHAR"
title: "Cloud Implications on Software Network Structure and Security Risks"
authors: "Terrence August; Marius Florin Niculescu; Hyoduk Shin"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0527"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/D28WAHAR/fulltext/images/459de0486145494a877073cea529039c65b6b0eef6049fb37329adb99d1b7e6d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Cloud Implications on Software Network Structure and Security Risks

Terrence August, Marius Florin Niculescu, Hyoduk Shin

To cite this article:

Terrence August, Marius Florin Niculescu, Hyoduk Shin (2014) Cloud Implications on Software Network Structure and Security Risks. Information Systems Research 25(3):489-510. http://dx.doi.org/10.1287/isre.2014.0527

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/D28WAHAR/fulltext/images/79df4241f91eb83de2b1e641cf9dfba8ec18a2aa2438564ddbd92c427e864393.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Cloud Implications on Software Network Structure and Security Risks

Terrence August

Rady School of Management, University of California, San Diego, La Jolla, California 92093; and Korea University Business School, Seoul 136-701, Korea, taugust@ucsd.edu

Marius Florin Niculescu

Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308, marius.niculescu@scheller.gatech.edu

Hyoduk Shin

Rady School of Management, University of California, San Diego, La Jolla, California 92093, hdshin@ucsd.edu

y software vendors offering, via the cloud, software-as-a-service (SaaS) versions of traditionally on-premises application software, security risks associated with usage become more diversified. This can greatly increase the value associated with the software. In an environment where negative security externalities are present and users make complex consumption and patching decisions, we construct a model that clarifies whether and how SaaS versions should be offered by vendors. We find that the existence of version-specific security externalities is sufficient to warrant a versioned outcome, which has been shown to be suboptimal in the absence of security risks In high security-loss environments, we find that SaaS should be geared to the middle tier of the consumer market if patching costs and the quality of the SaaS offering are high, and geared to the lower tier otherwise. In the former case, when security risk associated with each version is endogenously determined by consumption choices, strategic interactions between the vendor and consumers may cause a higher tier consumer segment to prefer a lower inherent quality product. Relative to on-premises benchmarks, we find that software diversification leads to lower average security losses for users when patching costs are high. However, when patching costs are low, surprisingly, average security losses can increase as a result of SaaS offerings and lead to lower consumer surplus. We also investigate the vendor’s security investment decision and establish that, as the market becomes riskier, the vendor tends to increase investments in an on-premises version and decrease investments in a SaaS version. On the other hand, in low security-loss environments, we find that SaaS is optimally targeted to a lower tier of the consumer market, average security losses decrease, and consumer surplus increases as a result. Security investments increase for both software versions as risk increases in these environments.

Keywords: cloud computing; software-as-a-service; network economics; security; versioning; on-premises software History: Rahul Telang, Senior Editor; Karthik Kannan, Associate Editor. This paper was received on August 22, 2012, and was with the author(s) 8 months for 2 revision(s). Published online in Articles in Advance July 21, 2014.

## 1. Introduction

With broadband access becoming faster and more pervasive, there has been a shift back toward models where computing is centralized and accessed via thin clients. Both firms and governments are starting to implement cloud-based systems to support business processes and increase operational efficiency. For example, the U.S. government, which has an \$80 billion federal IT budget, has championed a Federal Cloud Computing Initiative to encourage agencies to move toward cloud computing solutions, supporting this transition with Apps.gov (Claburn 2009).<sup>1</sup> Gartner estimates that the cloud computing industry will grow to \$149 billion by 2015 (Kundra 2011). Vivek Kundra, former U.S. Chief Information Officer, also suggested that cloud computing will help increase productivity in healthcare, financial services, and education, pointing out that a 1% productivity increase in healthcare over the next 10 years represents \$300 billion in value (e.g., shifting electronic medical records to the cloud).

Cloud computing is not likely to be an end all solution. Rather, for many firms, it will become an increasingly important component of an overall IT strategy, augmenting the traditional models currently used (O’Neill 2011). Among the many opportunities for engagement, cloud computing can be leveraged across diverse service models: infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). Of particular interest to application software companies and the consumers of their products is the SaaS model.<sup>2</sup> This model has emerged from economic efficiency and to satisfy users’ additional preferences that their data and applications be ubiquitous. Over the last two decades, consumers have harnessed SaaS applications for personal email, online gaming, photo sharing, and social networking. Businesses are also using SaaS versions of productivity software, enterprise resource planning software, and more; according to a recent survey by InformationWeek, three quarters of the “companies using SaaS consider application services extremely or critically important to their organizations” (Biddick 2010). For example, to address these market needs, Microsoft has added Microsoft Office 365, a SaaS variant of its well known Microsoft Office suite, which offers enterprise browser-based Office Web Apps to its product portfolio (El Akkad 2011). Similarly, SAP offers SAP Business ByDesign, targeting this version to small businesses (Farber 2007).

When software vendors such as Microsoft and SAP offer SaaS versions of traditionally locally hosted software (often called on-premises because such software is installed on premises at the customer’s location), there are significant security risk implications. This versioning strategy greatly affects users’ incentives, which in turn determines how aggregate use is spread across the versions and to what extent users engage in secure behaviors such as patching. To better understand the impact of versioning on security risk, it is useful to first discuss the nature of attacks faced by application software products. Security attacks can be broadly categorized into two classes: directed (targeted) and undirected (nontargeted).<sup>3</sup> A directed attack occurs when a malicious actor expends effort in an attempt to compromise a specific target (Villeneuve 2011). An undirected attack typically involves self-propagating malware (e.g., a computer worm) designed to spread to and infect many vulnerable hosts, which are often running a common software application that contains an exploitable vulnerability.

Users and organizations are generally exposed to a wide range of directed and undirected attacks due to flaws in hardware and software technologies, poor configurations, and weaknesses in individual decision making. However, to isolate the differential impact on security risk associated with a software vendor offering distinct on-premises and SaaS versions of a software product, it is preferable to focus only on the attacks that specifically exploit vulnerabilities in the code of one of these two versions (essentially holding constant all other attacks unrelated to vulnerabilities in the variants of this product). With this lens, a directed attack refers to an attack explicitly directed toward a particular system running one of these versions and exploiting a vulnerability specific to the version. Similarly, an undirected attack indiscriminately exploits one of these versions on any system running a copy of the version’s software.

Focusing on a single software product and the idiosyncratic security risk stemming from each of its versions, the on-premises version has relatively higher undirected risk and the SaaS version has relatively higher directed risk. To see why, suppose SAP Business One (on-premises) contains vulnerability V1, SAP Business ByDesign (SaaS) contains vulnerability V2, and a firm is considering the risks associated with each version. If the firm, along with many other companies with similar needs, chooses to use SAP Business ByDesign, the firm is exposed to considerable directed risk. In particular, a directed attack on SAP’s systems (running Business ByDesign) that exploits vulnerability V2 enables a malicious attacker to affect many organizations all at once. On the other hand, if the firm uses SAP Business One, its exposure to directed risk is much lower; the attacker’s incentive to exploit vulnerability V1 on the firm’s system (running Business One) is reduced because it would only affect an individual organization. Instead, because on-premises versions such as Business One are often widely deployed on independent but interconnected systems, each containing vulnerability V1, a malicious hacker could inflict significantly more damage by using the same vulnerability to attack the entire network in one broad, undirected move, affecting many users.

Because of the large number of installations associated with on-premises software, a software vendor usually manages vulnerabilities by creating and distributing software patches to users. However, it has been historically difficult to incentivize users to patch their own installations when security patches are released. Thus, for on-premises offerings, the user network is characterized by a large number of widespread nodes where individual instances of the software are running with many remaining unpatched (Lemos 2004, Keizer 2008). Even six years after the Conficker worm first struck, the malicious program is still infecting computers (Robertson 2014). Poor user patching behavior increases the risk of other users and, as a result, reduces the value of the software vendor’s product. Code Red, SQL Slammer, Sasser, and Conficker are all examples of malware that spread across vulnerable software networks and caused sizable economic damage (Moore et al. 2002, Lemos 2003, Keizer 2004, Markoff 2009).<sup>4</sup> Microsoft’s webserver software, Internet Information Services (IIS), and its database management system, SQL Server, are examples of software products being compromised by these undirected attacks.

Because systems servicing large populations of consumers are attractive targets to hackers incentivized by economic and/or political motivations, SaaS versions have considerable exposure to directed risk as discussed above. Recently Adallom, a SaaS security company, observed an exploited vulnerability in Office 365’s token management that enables an attacker to steal a user’s token and thus the user’s access to the software (Messmer 2013, Liran 2013). Similarly, Office 365 also had a cross-site scripting vulnerability that would enable an attacker to gain administrator access to an organization’s Office 365 account and configuration (Lee 2014). In both cases, users can incur substantial economic losses from directed attacks on Microsoft’s systems to exploit vulnerabilities in the implementation of Office 365.

When a SaaS variant of an on-premises product is introduced into the market, the aggregate security risk can be affected in several ways. First, as discussed above, users of the SaaS version are exposed to significantly less product-specific undirected risk. Second, an increase in SaaS use helps reduce total risk by diversifying exposure across undirected and directed attacks and limiting the size of populations that malware can effectively target; this, in turn, may indirectly reduce the incentives of malware developers to target diversified software (Bain et al. 2002 and Kannan et al. 2013). Third, a software vendor who expands its product line to offer distinct SaaS and on-premises versions may further expand use through pricing, which indirectly affects security risk. Finally, such a product line expansion to include SaaS may act as a substitute to investments in making on-premises software products more secure.

In recent years, software companies have invested substantial resources in (i) developing SaaS versions of their existing, on-premises software products, and (ii) increasing the security of their on-premises products (Charney 2012). Because of inherent risk interdepencies, it is important for companies such as Microsoft to better understand how versioning and security are intimately related. For example, when Microsoft brought its SaaS service Office 365 to the market, it faced a challenging question of how to manage both Office 365 and its on-premises counterpart, Office, so as to cater to consumers’ heterogeneous preferences and harvest the risk diversification benefits that stem from having two versions with separate user populations. One question is which consumer segments should be the targeted users of the SaaS and on-premises versions. Given the strong market for Office 365, Microsoft may also have reconsidered whether its substantial investments in security are still necessary when its product line expands to achieve security through diversity.

Similar challenges are being faced by providers of enterprise application server software (e.g., Oracle WebLogic Server, IBM WebSphere, etc.), database management systems (e.g., Oracle Database, SQL Server, MySQL, etc.), and customer relationship management software (e.g., Microsoft Dynamics, SAP 360, Oracle CRM, etc.).<sup>5</sup> Because of differences in fixed development costs, business strategy, and individual expertise, not every on-premises software provider will find it economical to offer SaaS alternatives in addition to their traditional on-premises offerings. However, for the software vendors who are either already or in the process of providing both on-premises and SaaS solutions, better product design, consumer segment targeting, and pricing decisions can be made with an improved understanding of the security implications of this type of versioning.

In this paper, we study the security impact of an application software vendor’s versioning strategy to include a SaaS variant of its on-premises product. Several research goals drive our study. First, when both SaaS and on-premises offerings are available, we want to better understand how consumers separate across product variants to diversify security risk. Thus, we account for how directed and undirected attacks generate distinct security externalities under each paradigm. We then build a model that captures consumer incentives to use either variant recognizing that (i) users of the on-premises alternative who choose not to patch impose undirected risk on other users, and (ii) directed risk associated with the SaaS alternative is proportional to the size of the total consumer population who opt for the SaaS variant. With this model of consumer behavior, we fully characterize the equilibrium consumer market structure in which the idiosyncratic security externalities are endogenously determined by consumption choices.

Using this equilibrium characterization, a second research goal is to develop an understanding of how a software vendor approaches the versioning problem when the vendor has the potential to offer both SaaS and on-premises versions. The first question is whether a vendor should version its software or simply offer a single on-premises product. Second, we comment on which consumer market segments should be the intended users of each version if the vendor finds it optimal to pursue a versioning strategy. Because of the distinct security externalities, we study whether the vendor’s strategic behavior can yield unexpected strategies in the product differentiation and pricing problem.

A final research goal is to quantify the risk diversification benefits of a versioning strategy in this context. Using our framework, we compare measures of profitability, security losses, consumer surplus, and social welfare against benchmark measures stemming from a model of a single, on-premises product that faces only undirected security risk. Using these comparisons, we can clarify the risk environments under which versioning has greater potential. We can also show how a software vendor’s security investment decision interacts with the versioning strategy being used.

We then summarize the main findings of our study. One important implication highlighted by our model is that a software vendor may set prices to target an inherently lower quality SaaS product to consumers with higher valuations (i.e., types) than those who use a higher quality on-premises version. In a standard vertical product differentiation setting, the lower quality product typically serves consumers with low types. We demonstrate that strategic interactions between the software vendor and consumers can drive the opposite result where the vendor prices the SaaS product high so as to create a small SaaS user population, thus limiting the directed security risk associated with this product. By offering a lower inherent quality product but with better, endogenously-determined security properties at a higher price, the vendor makes its consumption incentive compatible for the higher type consumers who neither (i) find it cost effective to consume the higher inherent quality on-premises product in a patched state nor (ii) want to be exposed to the significant undirected risk associated with the on-premises product in an unpatched state.

By studying how the software vendor sets SaaS and on-premises product prices and the consumer market structures induced as a result, our findings contribute to a better understanding of digital goods versioning problems. We establish that even with uniformly distributed types and zero marginal costs (a case where the literature has established that vendors do not offer separate versions), a software vendor will find it optimal to version its product as long as each version has some idiosyncratic risk. Our finding remains valid even as the level of risk becomes small. Because the argument only requires that each version have minimal idiosyncratic risk (i.e., subtle differences between software versions), our finding offers some explanation of the many versions being offered by most software producers.

When comparing economic measures between the versioned (SaaS and on-premises) outcomes with those of a benchmark scenario (on-premises only), we highlight several interesting implications. First, we formally establish that average security losses per user can increase when a software vendor introduces a SaaS version in high security-loss environments. The risk diversification benefits are outweighed by the vendor’s pricing behavior with regard to inducing risky consumption. We also show that consumer surplus can decrease in these cases if the inherent quality of the SaaS alternative is sufficiently high. We demonstrate that these effects exist only in high security-loss environments. Thus, in low security-loss environments, security losses always decrease and consumer surplus always increases as a result of the vendor’s versioning decision. We also establish that the potential gains in profitability and social welfare relative to benchmarks stemming from a versioning strategy are much larger for high security-loss environments. In fact, in such environments, because of the software vendor’s strategic behavior with regard to how it targets its SaaS version to the various consumer market segments, we highlight an opportunity to increase social welfare if the vendor can be encouraged to target SaaS to higher consumer types in cases where it prefers its SaaS version to serve the lower tier of the consumer market.

## 2. Literature Review

Our paper bridges three distinct research areas from the literature on the economics of information systems, information security, and computer science. These three areas are the versioning of information goods, interdependent security risk, and software diversification, respectively. In this section, we describe the current research landscape in each of these areas and discuss in detail the contribution of our paper, which ties the areas together and advances our understanding of the interaction between SaaS versioning and security. We also discuss several papers that are connected to our work and study security and SaaS business models.

Versioning of information goods. Product differentiation is an important research topic in economics. Similarly, the information systems community actively studies the versioning of information goods. Given the ease with which information goods can be versioned and reproduced, digital content owners typically offer several versions of their content. This is readily evident in the software, movie, and music industries. When and how to version, pricing, and which consumer segments to target with each version are all relevant concerns. There is a rich stream of literature on these topics, examining how the versioning decision relates to cost-to-quality ratios, consumer heterogeneity, positive network effects, competition, asymmetric information, group tastes, and free disposal concerns (see, e.g., Bhargava and Choudhary 2001, 2008; Johnson and Myatt 2003; Jing 2007; Jones and Mendelson 2011; Wei and Nault 2011, 2014; Chellappa and Jia 2011; Chellappa and Mehra 2013; Niculescu and Wu 2014).

In this literature, a common concern is that when consumers are heterogeneous in their taste for quality, and this taste parameter is uniformly distributed, a software vendor will not find it optimal to version its product. This holds true for information goods where the marginal costs of reproduction are zero. Because such a result is not readily observed in practice, the papers listed above demonstrate conditions under which versioning is optimal by introducing realistic adaptations from this base model. We contribute to this understanding by examining how the software vendor reacts if each version of its product carries some idiosyncratic security risk that endogenously arises as a result of pricing and consumption behaviors in equilibrium. Using our model, we formally establish that even with uniformly distributed tastes and zero marginal costs, a software vendor will always find it optimal to version its product provided that each version has some idiosyncratic risk, even as this risk becomes negligible. Our finding is consistent with the nature of versions being offered by software providers that typically differ on various functionalities, and satisfies the criteria of minimal idiosyncratic risk. In this sense, one contribution of our paper is to demonstrate that security differences in product versions can swing the versioning decision.

Software diversity. Beyond this contribution to the versioning literature, one of the main goals of our paper is to show that for software exposed to security threats, versioning can have substantial implications for the equilibrium security levels faced by consumers. In this vein, our work connects to the literature on software diversity. There is considerable research on the risks of having an IT monoculture and on determining methods that can achieve diversity. IT monoculture refers to deploying similar systems running similar software (Lala and Schneider 2009). Both within and across organizations, a monoculture strategy reduces the cost of learning, management, configuration, and maintenance. However, similar systems share common vulnerabilities that put entire networks of systems running common software at risk from large scale attacks. In this literature, researchers have explored how to introduce artificial diversity via memory randomization (Forrest et al. 1997, Xu et al. 2003, Schneider and Birman 2009), additional redundancy with N -variant systems (Cox et al. 2006, Weatherwax et al. 2009, Gherbi et al. 2011) and, more recently, how diversity results from equilibrium actions in game-theoretic settings (Neti et al. 2012). In Chen et al. (2011), the authors are the first to construct a model that explores the trade-offs among increased security through software diversity, lost network effects, and economies of scale. They find that a firm can benefit more from diversification as software begins to use more standardized interfaces and when adapters and middleware are available to keep applications compatible.

An important consequence of the movement toward cloud-based SaaS offerings is that it can indirectly introduce diversity. For example, Microsoft Office 365 includes enterprise Office Web Apps; this is a virtual version of the most common Office tools such as Word, Excel, and PowerPoint. By providing both a typical on-premises version and a SaaS one, Microsoft achieves software diversity in its Office suite as a consequence of naturally catering to its heterogeneous customer preferences. With the current movement, there is a fitting opportunity to add to the discussion on software diversity by examining settings where consumer demands have driven the need for a particular type of diversity, which can then be leveraged as an opportunity to simultaneously improve security. Our paper contributes to this stream of literature by formally studying the impact of software diversity stemming from SaaS on the security risk properties of the network of users, as driven by benefits from use diversified across versions and changes in security behaviors (e.g., patching and security investment). We quantify these benefits by comparing measures of profitability, security losses, consumer surplus, and social welfare to analogous measures in benchmark scenarios in the absence of software diversity.

Interdependent security risk. A third stream of research closely related to our work centers on security interdependence. One particularly relevant type of interdependence relates to how users of software running on interconnected networks impose security externalities on one another through their usage choices and patching decisions. We examine the diversification benefits associated with having two separate types of risk, directed and undirected, noting that with undirected risk users typically make decisions on whether to patch their individual systems. Therefore, it is important for us to build on prior work that focuses specifically on the trade-off between patching and being exposed to undirected risk. In particular, we build on the foundational model in August and Tunca (2006) which captures how risk faced by unpatched users is related to the number of users who choose to be unpatched in equilibrium. August and Tunca (2006) focus on how patching rebates, mandates, and taxes can improve software security, whereas our research goals focus on security risk diversification through versioning. However, by extending the model in August and Tunca (2006), we can compare security properties of the risk-diversified network, when jointly offering SaaS and on-premises versions, to benchmarks from the base model.

While there are many other studies of the phenomena that involve interdependent security risks (e.g., Kunreuther and Heal 2003, Heal and Kunreuther 2007, August and Tunca 2008, Choi et al. 2010, August and Tunca 2011, Hui et al. 2013, Nochenson et al. 2014), we contribute to this literature by investigating how risk interdependence can be mitigated by designing product substitutes with separate, idiosyncratic risks and allowing users to make choices that endogenously determine the aggregate security risk on the network. Given the scale of economic damage associated with security attacks and the substantial investments in security being made by software providers (Judge 2002, Lewis and Baker 2013), our paper provides insights into the value of software versioning strategies for overall security. These insights are useful to software managers who (i) are making decisions about whether to offer SaaS variants of traditional software packages, and (ii) have also traditionally determined investment levels in product security of on-premises products, which can act as substitutes for versioning strategies for risk diversification. Thus, our research goals are unique, but clearly complement this body of knowledge which aims to put forth a better understanding of managing security risk in the presence of security externalities.

Our paper is related to the broad research area that examines the economics of information security.<sup>6</sup> We complement research streams on piracy (August and Tunca 2008, Lahiri 2012, Kannan et al. 2013), software liability (Cavusoglu et al. 2008; Kim et al. 2010, 2011; August and Tunca 2011), vulnerability disclosure (Cavusoglu et al. 2007, Arora et al. 2008, Choi et al. 2010), and markets for security (Kannan and Telang 2005, Dey et al. 2012, Ransbotham et al. 2012, Lee et al. 2013) which, similar to our work, all study particular facets of the security problem and recommend strategies to manage risk and improve the value derived from software.<sup>7</sup> Png and Wang (2009) examine the role of government in facilitating end-user precautions and enforcing laws against attackers, considering both directed and undirected attacks. In our model, we examine how a diversification strategy (releasing both SaaS and on-premises versions) affects directed and undirected attacks on product-specific vulnerabilities to analyze its aggregate impact on security risk.

Last, our work is related to several papers that study various aspects of SaaS versus on-premises business models. Choudhary (2007) examines how SaaS versus perpetual licensing affect a software vendor’s incentives to invest in quality. In a two-period model, he establishes that the vendor tends to invest more in quality under a SaaS scheme and that both profits and welfare increase as a result. Zhang and Seidmann (2010) study the licensing problem under network effects and quality uncertainty. They demonstrate that under strong network effects, hybrid models are favorable; in our work, we establish a similar result driven by security risk diversification benefits in contrast to multiperiod dynamics. Huang and Sundararajan (2005) take a more general approach to pricing to characterize optimal nonlinear prices of on-demand computing, while Ma and Seidmann (2014) study competition between various software providers. In our model, we simplify the structure of the SaaS and on-premises alternatives, using a static model that abstracts away from upgrade cycles and multiperiod pricing to elegantly capture software security risk concerns which are the focus of our paper.

## 3. Model Description

A vendor produces software and offers it to a continuum of consumers. The software can be made available in two formats: (i) as a product to be installed at the consumer’s location (on-premises), and (ii) as a service installed only on the vendor’s systems and accessible by users over the Internet (SaaS). SaaS versions of common software products (e.g., SAP Business ByDesign, Microsoft Office 365, and Microsoft Dynamics CRM On-Demand) are typically streamlined for easier use but include less functionality, require less setup, and offer less integration. In other words, a SaaS version consumer tends to forgo some flexibility in integration with business systems, in the ability to control data, and to manage upgrades (Chow et al. 2009). On the other hand, consumers can derive greater value through a more comprehensive integration with an on-premises version of software that is installed internally and can connect with other systems. Therefore, we model consumer valuations for the on-premises version to be uniformly distributed on ${ \mathcal { V } } \dot { = } [ 0 , 1 ]$ and assume that if a given consumer has valuation $v \in { \mathcal { V } }$ for the on-premises version, she has valuation v for the SaaS version where $0 < \delta < 1$

We assume that the software is used in a network setting, thereby exposing purchasing consumers to additional risk associated with the software’s use. This risk comes in the form of directed and undirected security attacks, which are both described in §1. We denote the probability that a directed attack occurs on the network with $0 < \pi _ { d } < 1$ (we use d to signify directed). Conditional on a directed attack having occurred on the network, we assume that the likelihood that any given network location (node) is victimized is proportional to the mass of consumers at that node (Greenemeier and Hoover 2007, Roy 2011). Therefore, the total likelihood of a node that services d consumers being attacked is $\pi _ { d } d $ Similarly, we denote the probability that a patchable security vulnerability arises in the software and that an undirected attack on that vulnerability occurs with $0 < \pi _ { u } < 1$ (we use u to signify undirected). Given the spreading mechanics of undirected security attacks such as worms, if the mass of the unpatched population in the network is $u ,$ the unconditional probability that the worm will attack an unpatched user’s system is given by $\boldsymbol { \pi } _ { u } \boldsymbol { u }$

Because the SaaS version is only installed at one node (on the vendor’s system), under the above model specification users of the SaaS version are primarily exposed to directed risk, which increases with the size of the total SaaS user population. In contrast, the on-premises version carries minimal directed risk because a given node is negligible compared to the size of the total number of on-premises nodes (a subset of the continuum V). However, because of the many widespread nodes running the on-premises product, this version is exposed to considerable undirected risk, which is proportional to the size of the user base that remains unpatched. In our model specification, we have attempted to maintain the simplest structure where the SaaS and on-premises versions face idiosyncratic security risks, each having a security externality dependent on user behavior. Such a structure will permit us to analytically explore the impact of versioning on security and produce clear insights.

If a user is struck by a directed or undirected security attack, one would expect that she suffers a loss positively correlated with her valuation. That is, consumers with high valuations will incur greater losses than consumers with lower valuations due to higher opportunity costs, higher criticality of data, and loss of business. For simplicity, we assume the correlation is of the first order, i.e., the loss that a consumer with valuation v incurs if she is hit by the attack is either v for an on-premises product or $\alpha \cdot \delta v$ for SaaS, where $\alpha > 0$ is a constant. Undirected attacks typically exploit known vulnerabilities for which a patch is already available, hence each consumer has an opportunity to patch in the face of this security risk.<sup>8</sup> If a consumer chooses to patch the software, she will incur an expected cost of patching denoted as $0 < c _ { p } < 1$ , which accounts for the money and effort that a consumer must exert to verify, test, and roll out patched versions of existing systems.

There are three decision periods. In the first, the vendor determines which versions of its software to release and sets a product price $p > 0$ for a single server license for its on-premises version and a service price $p _ { s } > 0$ for its SaaS version.<sup>9</sup> In the second period, given the price and security risk of each software offering, each consumer makes a decision whether to purchase the software as well as which version to purchase. Finally, in the third period, if a patchable security vulnerability has been discovered, each consumer who purchased the on-premises version determines whether to patch her own system. Subsequent to these decision periods, both directed and undirected attacks may occur on the network and consumers incur losses.

Each consumer makes a purchasing decision to buy the on-premises product version, OP, buy the SaaS version, SaaS, or not to buy either offering, N . Similarly, if a patchable vulnerability arises in the software, each user of the on-premises version makes a decision to patch, P , or not to patch, NP, her own system. If the consumer has chosen SaaS or $N ,$ she does not make a patching decision as in the on-premises case, which we denote by ND. We denote the consumer action space by $S = ( \{ O P \} \times \{ P , N P \} ) \cup ( \{ S a a S , N \} \times \{ N D \} )$ . Given prices, in a consumer market equilibrium each consumer maximizes her expected utility given the equilibrium strategies of all other consumers. For a strategy profile  2 $\mathcal { V } \to S ,$ the expected cost faced by the consumer with valuation v is then defined by

$$
C (v, \sigma) \triangleq \left\{ \begin{array}{l l} c _ {p}, & \text {if} \sigma (v) = (O P, P); \\ \pi_ {u} u (\sigma) \alpha v, & \text {if} \sigma (v) = (O P, N P); \\ \pi_ {d} d (\sigma) \alpha \delta v, & \text {if} \sigma (v) = (S a a S, N D); \\ 0, & \text {if} \sigma (v) = (N, N D), \end{array} \right.\tag{1}
$$

where the size of the unpatched user population of the on-premises version is given by

$$
u (\sigma) \triangleq \int_ {\mathcal {V}} \mathbb {1} _ {\{\sigma (v) = (O P, N P) \}} d v,\tag{2}
$$

and the size of the user population of the SaaS version (most vulnerable to a directed attack) is given by

$$
d (\sigma) \triangleq \int_ {\mathcal {V}} \mathbb {1} _ {\{\sigma (v) = (S a a S, N D) \}} d v,\tag{3}
$$

where $\mathbb { 1 } _ { \{ \cdot \} }$ is the indicator function. For expositional convenience, we also define the size of the patched population using the on-premises product as

$$
n (\sigma) \triangleq \int_ {\mathcal {V}} \mathbb {1} _ {\{\sigma (v) = (O P, P) \}} d v.\tag{4}
$$

Our main research goal is to assess the security impact that stems from risk diversification benefits associated with a software vendor’s versioning strategy as it extends into SaaS markets. To do so, we use the benchmark model from August and Tunca (2006) to compare security risk characteristics. In their model of undirected security risk, users make use and patching decisions, and the vendor sets the product price. In this paper, we model the on-premises software product so that it is consistent with August and Tunca (2006).<sup>10</sup> However, to study risk diversification in the context of SaaS versioning, we also model a SaaS version with its own idiosyncratic risk. This directed risk reflects a security externality that is structurally different and unique from the externality stemming from unpatched use of the on-premises version. By modeling both onpremises and SaaS versions with separate externalities, we analyze how versioning in this manner affects pricing and user incentives, which then determine the security characteristics of this more complex software network. Finally, by being consistent with prior work, when $\delta = 0$ , the SaaS version has no inherent value to users (in which case consumers purchase on-premises products or remain out of the market). Our model then collapses to August and Tunca (2006), which we will refer to as the benchmark case, i.e., having only an on-premises offering.

## 4. Consumer Choice and Vendor Profit Maximization

## 4.1. Consumer Market Equilibrium

To study the software vendor’s versioning problem and the subsequent security properties of the network, we first develop an understanding of how consumers strategically determine whether to adopt an on-premises product or a SaaS solution. In this section, we take prices as given and study the choice problem faced by consumers who strategically interact due to version-specific security externalities associated with each alternative. Holding all other consumers strategies fixed to $\sigma _ { - v } ,$ the consumer with valuation v determines her optimal action by solving the following maximization problem

$$
\begin{array}{c} \max _ {s \in S} \bigl \{(v - p) \cdot \mathbb {1} _ {\{s \in \{(O P, P), (O P, N P) \} \}} \\ + (\delta v - p _ {s}) \cdot \mathbb {1} _ {\{s = (S a a S, N D) \}} - C (v, \sigma) \bigr \}, \end{array}\tag{5}
$$

where the strategy profile $\sigma$ is composed of $\sigma _ { - v }$ (other consumers’ strategies) and the choice being made, i.e., $\sigma ( v ) = s$ . We denote her optimal action that solves (5) with $s ^ { * } ( v )$ . An equilibrium strategy profile $\sigma ^ { * }$ must satisfy $\sigma ^ { * } ( v ) = s ^ { * } \bar { ( v ) }$ for all $v \in { \mathcal { V } }$

In the following lemma, we provide a full characterization of equilibrium consumer behavior for all prices and exogenous security and quality parameters in our model.

<sup>Lemma</sup> <sup>1.</sup> Given on-premises product and SaaS prices, $p \in ( 0 , 1 )$ and $p _ { s } \in ( 0 , \delta )$ , respectively, and other parameters $c _ { p } , \pi _ { d } , \pi _ { u } ,$ , and , a unique equilibrium in the consumer market exists.<sup>11</sup> The equilibrium consumer strategy profile $\sigma ^ { * }$ is characterized by thresholds $v _ { d } , v _ { u } , v _ { p } \in [ 0 , 1 ]$ such that for $v \in \mathcal { V } ,$ , it satisfies either

$$
\sigma^ {*} (v) = \left\{ \begin{array}{l l} (O P, P), & \text {if v_{p} <   v\leq 1}; \\ (O P, N P), & \text {if v_{u} <   v\leq v_{p}}; \\ (S a a S, N D), & \text {if v_{d} <   v\leq v_{u}}; \\ (N, N D), & \text {if 0\leq v\leq v_{d}}, \end{array} \right.\tag{6}
$$

or

$$
\sigma^ {*} (v) = \left\{ \begin{array}{l l} (O P, P) & \text {if v_{p} <   v\leq 1}; \\ (S a a S, N D) & \text {if v_{d} <   v\leq v_{p}}; \\ (O P, N P) & \text {if v_{u} <   v\leq v_{d}}; \\ (N, N D) & \text {if 0\leq v\leq v_{u}}. \end{array} \right.\tag{7}
$$

Lemma 1 formally establishes that the consumer market exhibits a threshold structure.<sup>12</sup> Common to both possible equilibrium strategy profiles, as seen in (6) and $( 7 ) ,$ the consumers with highest valuations for the software choose the on-premises product and patch to avoid undirected security attacks in equilibrium. Thus, there is a patching threshold, denoted by $v _ { p } ,$ such that all consumers with valuations above this threshold value use this strategy, i.e., $\sigma ^ { * } ( v ) = ( O P , P )$ for all $v \geq v _ { p }$ . As motivated before, the on-premises product alternative carries the highest inherent quality; this reflects the ability of a consumer to more fully integrate this product with her own systems and take advantage of greater functionality. As a result, we would expect the equilibrium outcome to reflect that the highest valuation users prefer the on-premises product and fully protect their value by patching.

However, one relevant consequence of consumers’ strategic behavior highlighted by Lemma 1 concerns the effective quality ordering of the SaaS alternative and the on-premises software in an unpatched state. In particular, for the next consumer valuation interval directly below $v _ { p } ,$ either unpatched on-premises product users, who choose 4OP1 NP5, or SaaS users, who choose 4SaaS1 ND5, compose the subsequent lower set of valuations, corresponding to the strategy profiles in (6) and (7), respectively. Given that consumers inherently prefer the on-premises product to SaaS (because $v > \delta v )$ , it is more natural to think that the SaaS version would be consumed by the lowest consumer segment remaining in the user population as in (6).

The fact that there can exist a segment of consumers choosing 4SaaS1 ND5 in equilibrium and having higher valuations than consumers in a segment choosing 4OP1 NP5 as in (7) firmly demonstrates the role of idiosyncratic security externalities in shaping the equilibrium outcome. In this case, the effective quality of the SaaS version when adjusted for its exposure to directed security attacks, which is influenced by pricing and the number of users choosing the SaaS version, can actually be higher than the quality associated with using the on-premises version and not patching. For instance, higher valuation users may prefer slightly lower inherent quality software if it is used by very few users and is considerably more secure than higher inherent quality software with a large unpatched population and considerable undirected risk. Significantly, the effective quality of each product is endogenously determined by consumer behavior. Thus, it is the strategic interactions that drive the effective quality ordering found in (7). If the on-premises and SaaS versions did not have unique exposures to different risks, the higher consumer valuation segment would not, ordinarily, consume the lower inherent quality product.

Similar to our definition of the patching threshold $v _ { p } ,$ the SaaS threshold $v _ { d }$ marks the valuation above which (up to the next higher threshold) consumers prefer to use SaaS and tolerate exposure to directed security risk. Last, we denote the on-premises purchasing threshold with $v _ { u } ,$ which marks the valuation above which (again, up to the next higher threshold) consumers prefer to use the on-premises product and not patch in equilibrium. By not patching, these consumers will be exposed to undirected security risk. Because of the threshold structure presented in Lemma 1, there are three distinct consumer market segments represented in equilibrium as characterized by these intervals in the consumer valuation space. For convenience in exposition, we refer to these intervals as high tier, middle tier, and low tier, corresponding to $( v _ { p } , 1 ] , ( v _ { u } , v _ { p } ] ,$ and $( v _ { d } , v _ { u } ] ,$ respectively, for (6), and $( v _ { p } , 1 ] , ( v _ { d } , v _ { p } ) ,$ and $( v _ { u } , v _ { d } ] ,$ respectively, when the characterization in (7) arises in equilibrium. When only two consumer market segments arise in equilibrium $( \mathrm { i . e . } ,$ , when $v _ { p } = 1$ meaning no consumer prefers 4OP1 P 5 the other alternatives), we simply refer to the two ordered segments as high tier and low tier.

## 4.2. Vendor Profit Maximization

Next, we formally present the software vendor’s pricing problem and define measures of security losses, social welfare, and consumer surplus. Using the measures defined in (2)–(4), the vendor’s profit function can be written as follows:

$$
\Pi (p, p _ {s}) \triangleq p [ u (\sigma^ {*}) + n (\sigma^ {*}) ] + p _ {s} d (\sigma^ {*}),\tag{8}
$$

where the size of each population depends on the equilibrium strategy profile which, in turn, is a function of prices, i.e., $\sigma ^ { * } = \stackrel { \cdot } { \sigma ^ { * } } ( \cdot | p , p _ { s } ) . ^ { 1 3 }$ The vendor’s profit maximization problem can then be expressed as follows:

$$
\begin{array}{l l} \max _ {(p, p _ {s}) \in [ 0, 1 ] \times [ 0, \delta ]} & \Pi (p, p _ {s}) \\ \text {s.t.} & (v _ {d}, v _ {u}, v _ {p}) \text {are given by} \sigma^ {*} (\cdot | p, p _ {s}). \end{array}\tag{9}
$$

In addition to characterizing the optimal prices in (9) and the corresponding equilibrium consumer market structures under these prices, we also examine measures of security risk, consumer surplus, and social welfare for these outcomes.

To facilitate the ensuing discussion, under a set of prices $( p , p _ { s } )$ , we denote the total security losses as SL and define it as the sum of expected losses from undirected security attacks, directed security attacks, and patching costs under the equilibrium strategy profile $\sigma ^ { * } ( \cdot \mid p , p _ { s } )$ , i.e.,

$$
\begin{array}{l} S L \triangleq \int_ {\mathcal {V}} \mathbb {1} _ {\{\sigma^ {*} (v) = (O P, N P) \}} \pi_ {u} u (\sigma^ {*}) \alpha v   d v \\ \qquad + \int_ {\mathcal {V}} \mathbb {1} _ {\{\sigma^ {*} (v) = (S a a S, N D) \}} \pi_ {d} d (\sigma^ {*}) \alpha \delta v   d v + c _ {p} n (\sigma^ {*}). \end{array}\tag{10}
$$

Social welfare can then be measured as

$$
\begin{array}{r} W \triangleq \int_ {\mathcal {V}} \bigl [ \mathbb {1} _ {\{\sigma^ {*} (v) \in \{(O P, P), (O P, N P) \} \}} v \\ + \mathbb {1} _ {\{\sigma^ {*} (v) = (S a a S, N D) \}} \delta v \bigr ] d v - S L, \end{array}\tag{11}
$$

which is the difference between the aggregate value derived from the software and these losses. Finally, consumer surplus is defined by

$$
C S \triangleq W - \Pi (p, p _ {s}).\tag{12}
$$

For the benefit of the reader, we briefly outline how we will structure our presentation of results going forward. Using the equilibrium consumer market characterization above, in the next two sections we separately examine high security-loss environments (high ) and low security-loss environments (low ). As noted above, because of the complexity of the general characterization of the equilibrium, it is too extensive to fully include in the exposition. However, when focused on a high or low security-loss environment, this equilibrium characterization simplifies considerably. Thus, for each environment, we first present greater details on parameter boundaries of feasible regions. We then examine the vendor’s pricing problem and study its versioning decision. In light of the vendor’s optimal pricing and the associated consumer market outcome, we carefully examine how versioning affects security, consumer surplus, and social welfare, as determined by patching costs $( c _ { p } ) _ { \ l }$ , SaaS quality (), and the security loss factor (). As part of our analysis, we compare these outcomes with those obtained when only an on-premises solution is offered. We consider this to be the benchmark case. Finally, we conclude our study by examining how the software vendor’s security investment decisions interact with its versioning choice, which we present as an extension to our model.

## 5. High Security-Loss Environment

We begin by studying a high security-loss environment where consumers are subject to large economic losses if struck by security attacks. Specifically, in the loss model, the parameter  specifies the magnitude of loss correlation with valuation. In this section we examine the vendor’s problem when  is large. High securityloss environments are common and often reflect the reality of current network software security: Some users are patching their on-premises software installations when vulnerabilities arise to prevent potential security breaches; other users do not patch because of the associated costs. Enterprise software is typically classified as a high security-loss environment. This is why many organizations use a planned and systematic approach for deploying patches on such systems (Bloor 2003, Boulton 2013, Kash 2013). Similarly, SaaS providers of enterprise software are diligently addressing vulnerabilities to protect the interests of their customers (Branscombe 2012, Microsoft 2013). Microsoft IIS, Microsoft Dynamics, and SAP Business One are examples of enterprise software that businesses use and rely on for their dayto-day operations. When enterprise systems such as the above are successfully attacked and compromised, the affected businesses often incur large economic losses associated with lost sales, customer goodwill, reputation, IT human resources, and information (Lewis and Baker 2013).

First, following Lemma 1, we present a characterization of the three regions that can arise in the consumer market equilibrium when the security loss factor  becomes high.

Corollary 1 (Equilibrium Under High <sub></sub>). <sub>Given</sub> on-premises product and SaaS prices, $p \in ( 0 , 1 - c _ { p } )$ and $p _ { s } \in ( 0 , \delta )$ , respectively, and other parameters $c _ { p } , \pi _ { d } , \pi _ { u } ,$ and , the equilibrium consumer strategy profile $\sigma ^ { * }$ satisfies:

Region I (No SaaS). If $p _ { s } > \delta c _ { p } , p \leq p _ { s } / \delta - c _ { p } ,$ and $\alpha \geq \alpha _ { B } \triangleq c _ { p } ( 1 - c _ { p } ) / ( \pi _ { u } ( 1 - c _ { p } - p ) )$ , then $p < v _ { u } < v _ { p } < 1$ and $\sigma ^ { * }$ is given by either (6) with $v _ { d } = v _ { u } \ o r \ ( 7 )$ with $v _ { d } = v _ { p }$

Region II (SaaS for low tier). $I f p > \operatorname* { m a x } ( p _ { s } / \delta - c _ { p } , p _ { s } )$ and  ≥ max $\langle \alpha _ { E } \triangleq \delta ( p _ { s } - p \delta ) ^ { 2 } / ( \pi _ { u } p _ { s } ^ { 2 } ( ( p + c _ { p } ) \delta - p _ { s } ) ) , \hat { \alpha } _ { 1 } )$ where $\hat { \alpha } _ { 1 }$ is the unique root greater than $c _ { p } / \pi _ { u }$ that satisfies $g _ { 1 } ( \alpha ) = 0$ where

$$
\begin{array}{l} g _ {1} (\alpha) \triangleq \delta + \frac {c _ {p} \delta \pi_ {d}}{\pi_ {u}} \\ \qquad + \sqrt {\delta \bigg (4 p _ {s} \alpha \pi_ {d} + \frac {\delta (c _ {p} \pi_ {d} + \pi_ {u} - \alpha \pi_ {d} \pi_ {u}) ^ {2}}{\pi_ {u} ^ {2}} \bigg)} \\ \qquad - 2 (1 - c _ {p}) - \alpha \bigg (\delta \pi_ {d} + \frac {2 (p - p _ {s}) \pi_ {u}}{c _ {p} - \alpha \pi_ {u}} \bigg), \end{array}\tag{13}
$$

then $p _ { s } < v _ { d } < v _ { u } < v _ { p } < 1$ and $\sigma ^ { * }$ is given by (6).

Region III (SaaS for middle tier). $I f p _ { s } < \delta c _ { p } / ( 1 - \delta )$ $p _ { s } / \delta - c _ { p } < p \leq p _ { s } ,$ and

$$
\alpha \geq \max \left(\alpha_ {F} \triangleq \frac {c _ {p} (1 - \delta) ^ {2} \left(p - p _ {s} + c _ {p} \delta\right)}{\pi_ {u} \left(p - p _ {s} + c _ {p}\right) ^ {2} \left(\delta \left(p + c _ {p}\right) - p _ {s}\right)}, \hat {\alpha} _ {2}\right),
$$

where $\hat { \alpha } _ { 2 }$ is the unique positive root that satisfies $g _ { 2 } ( \alpha ) = 0$ where

$$
\begin{array}{c} g _ {2} (\alpha) \triangleq 1 - 2 (p + c _ {p} - p _ {s}) + \alpha \pi_ {u} - \frac {2 \delta \pi_ {d} \alpha (p - p _ {s})}{\Phi - \alpha \delta \pi_ {d}} \\ - \frac {\Phi \pi_ {u}}{\delta \pi_ {d}} - \sqrt {4 p \alpha \pi_ {u} + \left(1 - \alpha \pi_ {u} + \frac {\Phi \pi_ {u}}{\delta \pi_ {d}}\right) ^ {2}}, \end{array}\tag{14}
$$

and $\Phi \triangleq p - ( 1 - c _ { p } ) + ( \delta - p _ { s } )$ , then $p < v _ { u } < v _ { d } < v _ { p } < 1$ and $\sigma ^ { * }$ is given by $( 7 ) .$ .<sup>14</sup>

By Regions II and III of Corollary 1, when the use of SaaS arises in equilibrium, the threshold valuations satisfy $v _ { p } > v _ { u } > v _ { d }$ or $v _ { p } > v _ { d } > v _ { u } ,$ respectively. In the latter case, the SaaS alternative is preferred by the middle tier of the consumer market. Then, by (8), the vendor’s profit function in Region III can be expressed as follows:

$$
\Pi (p, p _ {s}) = p (1 - v _ {p} + v _ {d} - v _ {u}) + p _ {s} (v _ {p} - v _ {d}).\tag{15}
$$

We will subsequently refer to the prices that maximize (15), subject to the constraint that they induce a middletier SaaS consumer market structure, with $p ^ { M }$ and $p _ { s } ^ { M }$ . The corresponding profits are denoted by $\Pi ^ { M } \triangleq$ $\dot { \Pi } ( p ^ { M } , p _ { s } ^ { M } )$ . Similarly, by (10), security losses are now simplified to

$$
S L = \left[ \alpha (\pi_ {u} (v _ {d} - v _ {u}) (v _ {d} ^ {2} - v _ {u} ^ {2}) + \delta \pi_ {d} (v _ {p} - v _ {d}) (v _ {p} ^ {2} - v _ {d} ^ {2})) \right] / 2
$$

$$
+ c _ {p} (1 - v _ {p}),\tag{16}
$$

and social welfare can be expressed as follows:

$$
W = \big [ 1 - v _ {p} ^ {2} + v _ {d} ^ {2} - v _ {u} ^ {2} + \delta (v _ {p} ^ {2} - v _ {d} ^ {2}) - \alpha (\pi_ {u} (v _ {d} - v _ {u}) (v _ {d} ^ {2} - v _ {u} ^ {2})\tag{17}
$$

On the other hand, when the SaaS alternative is preferred by the lower tier of the market, i.e., $v _ { p } > v _ { u } >$ $v _ { d }$ as in Region II of Corollary 1, the vendor’s profit function can be expressed as follows:

$$
\Pi (p, p _ {s}) = p (1 - v _ {u}) + p _ {s} (v _ {u} - v _ {d}).\tag{18}
$$

Analogously, $p ^ { L }$ and $p _ { s } ^ { L }$ will denote the prices that maximize (18), constrained such that they induce a low-tier SaaS consumer market structure; the respective profits will be denoted by $\Pi ^ { L } \triangleq \Pi ( p ^ { L } , p _ { s } ^ { L } )$ . For this structure, the security losses and welfare are given by

$$
\begin{array}{l} S L = \left[ \alpha (\pi_ {u} (v _ {p} - v _ {u}) (v _ {p} ^ {2} - v _ {u} ^ {2}) + \delta \pi_ {d} (v _ {u} - v _ {d}) (v _ {u} ^ {2} - v _ {d} ^ {2})) \right] / 2 \\ + c _ {p} (1 - v _ {p}), \end{array} \tag {19}
$$

and

$$
\begin{array}{c} W = \big [ 1 - v _ {u} ^ {2} + \delta (v _ {u} ^ {2} - v _ {d} ^ {2}) - \alpha (\pi_ {u} (v _ {p} - v _ {u}) (v _ {p} ^ {2} - v _ {u} ^ {2}) \\ + \delta \pi_ {d} (v _ {u} - v _ {d}) (v _ {u} ^ {2} - v _ {d} ^ {2})) \big ] / 2 - c _ {p} (1 - v _ {p}), \end{array}\tag{20}
$$

respectively.

## 5.1. Versioning Strategy

<sup>Proposition</sup> <sup>1.</sup> For high security-loss environments,<sup>15</sup> (i) when patching costs and the SaaS alternative’s quality are both high, $i . e . , c _ { p } > 1 / 3$ and $\delta > ( 2 ( 1 - c _ { p } ) ) / ( 1 \dot { + } c _ { p } ) .$ , a software vendor can maximize profits by setting prices such that the middle tier of the consumer market prefers the SaaS offering; (ii) otherwise, the vendor sets prices so that the SaaS alternative is geared for the lower tier of the consumer market.

In high security-loss environments, there can be substantial consumer benefits associated with a reduction in the magnitude of security losses. When the consumer population is induced to separate use across on-premises and SaaS offerings, these losses are mitigated through diversification. Proposition 1 establishes that in these environments the vendor should version by setting prices such that all three user populations (patched on-premises users, unpatched on-premises users, and SaaS users) are represented in equilibrium. By inducing a population of SaaS users, the vendor has removed a large mass of potentially unpatched hosts from the network; because of patching costs, in the absence of a SaaS version, many of these users would not patch as on-premises product users. Thus, offering SaaS can help reduce the risk faced by remaining unpatched on-premises product users because, by (1) and (2), the risk these users face is proportional to the size of unpatched users population in equilibrium. Although the SaaS users do not bear undirected risk comparable to on-premises users, they now face considerable directed risk as a large node on the network. However, pricing the SaaS version to induce them to accept some directed risk helps diversify security risk within the network.

First, we discuss part (ii) of Proposition 1. When patching costs are small and security risk is large, consumers have strong incentives to patch when using on-premises software. In this case, the vendor can both charge a high price for its on-premises software and keep the security risk faced by unpatched onpremises users low because they remain a relatively small population within the network. This limits the impact of their security externality. Because of the vendor’s pricing power associated with on-premises software, it should set the price of its SaaS offering to prevent cannibalization but still serve the lower tier of the consumer market. Part (ii) of Proposition 1 is illustrated in panels (a) and (b) of Figure 1. Because $\delta = 0 . 8 0$ , the condition $\delta < 2 ( 1 - c _ { p } ) / ( 1 + c _ { p } )$ is satisfied whenever $c _ { p } < 3 / 7$ as indicated by the area labeled A in the figure. Within this area, the optimal prices are given by $p _ { s } ^ { L }$ and $p ^ { L } .$ , satisfying $p _ { s } ^ { L } < p ^ { L } ,$ , which gives rise to a low-tier SaaS structure characterized by $v _ { p } > v _ { u } > v _ { d }$ as is illustrated in panel (b) of Figure 1.

In area A of panel (a), as patching costs $( c _ { p } )$ increase, the price of the on-premises version $( p ^ { L } )$ decreases, but the price of the SaaS version $( p _ { s } ^ { L } )$ first decreases and then increases. To see why, first note that an increase in patching costs reduces the patching population of the on-premises version. Moreover, because of the negative security externalities associated with unpatched behavior, overall use will also decline, which reduces vendor profitability. In this case, the vendor must reduce $p ^ { \hat { L } }$ to help maintain a sizeable patching population, as well as to encourage unpatched on-premises users, who now face greater risk, to remain in the user population. However, under high security risk, the vendor also needs to throttle growth in the size of the risky populations as more users elect not to

(c) Optimal prices ( = 20)  
![](/api/attachments/D28WAHAR/fulltext/images/d6dbae4017674d3d0aafa9b679eb7cb507b291a462f7c5fb93b9ed0fb2b2aa5b.jpg)

![](/api/attachments/D28WAHAR/fulltext/images/6de015009743b214ac42a43b8cf6c02618f8e358ff1294ccc8d5195f5e874eed.jpg)  
Note. The other parameter values for all panels are  = 0080, $\pi _ { u } = 0 . 2 0 ,$ and $\pi _ { d } = 0 . 1 0 .$

## Figure 1 How Patching Costs Affect Pricing and on-Premises versus SaaS Usage

patch because of increased patching costs. To achieve this objective, the vendor must carefully adapt its SaaS price, $p _ { s } ^ { L } .$ . If it lowers $p _ { s } ^ { L } ,$ , more users at the lower end of the valuation space will become SaaS users. This increases the risk associated with SaaS and, in turn, provides disincentives for members of the larger on-premises unpatched population to switch to SaaS. As a result, both of these risky populations could grow substantially. Instead, the vendor must raise $p _ { s } ^ { L } .$ which prevents low valuation users from entering and leads to a comparatively smaller increase in the size of the risky populations, as in the right-hand portion of area A in Figure 1. However, when patching costs are low, as in the left-hand portion of area A in panel (a), or when security risk is still high but slightly lower as in panel (c) where $\alpha = 2 0$ , the impact of a slightly larger unpatched, on-premises user population and SaaS user population is not as detrimental. As a result, the vendor prefers to reduce $p _ { s } ^ { L }$ to provide incentives for users to diversify risky use across on-premises and SaaS versions.

Proposition 1 establishes that as patching costs increase, there exists a point at which the vendor alters his strategy, i.e., jumping up its SaaS price from $p _ { s } ^ { L }$ to $p _ { s } ^ { M } .$ , and jumping down its on-premises price from $p ^ { L }$ to $\bar { p ^ { M } }$ . This can be seen in panel (a) of Figure 1 as a move from area A (Region II in Corollary 1) to B (Region III in Corollary 1) for a security loss factor of $\alpha = 2 0 0$ . Similarly, in panel (c) of Figure 1, the same effect is shown as a shift from area C to D for a security loss factor one order smaller. At this point, due to substantial patching costs, even though the vendor lowers the on-premises product price, it will face a larger unpatched population and reduced use due to the negative externality these users impose. Although its SaaS product may have slightly lower base quality, when accounting for the security externalities, this may not be the case. This outcome is noteworthy because in typical product differentiation problems, the higher quality product is consumed by the higher value consumers, while the lower quality product is priced for the less quality-sensitive segment (see, e.g., Bhargava and Choudhary 2001, 2008; Johnson and Myatt 2003) Contributing to the versioning literature above, we establish a unique, inverse versioning result in the presence of two idiosyncratic security externalities; specifically, in our setting, the on-premises version is clearly assumed to be of higher quality (i.e., a type v consumer derives value v from the on-premises product and v from the SaaS product where $\delta < 1 )$ However, the security risk associated with each version is endogenously determined in equilibrium, being affected by vendor pricing and strategic consumption behavior. Here, we see that it is possible that the vendor will set prices to induce an outcome where the inherently lower quality SaaS version endogenously has higher effective quality. Specifically, as we cross the aforementioned boundary in patching costs, the vendor strategically prices its SaaS product at a higher level, i.e., it targets a smaller, higher-value population; this is accompanied by a smaller directed risk. Because users of the SaaS option are exposed to negligible undirected risk, the vendor’s pricing induces an outcome whereby medium valuation users will prefer the SaaS option over the lower value unpatched on-premises offering that faces considerable undirected security risk. In panel (b) of Figure 1, the area labeled B shows how the thresholds induced by its pricing flip to $v _ { p } > v _ { d } > v _ { u } ,$ leading to a middle-tier SaaS outcome; portion D of panel (d) is similar.

![](/api/attachments/D28WAHAR/fulltext/images/e6e91870d6cad4e571e0e2ba4215ccef7138d554e12a2175fd98979d15fd1b5a.jpg)

(d) Consumer threshold valuations ( = 20)  
![](/api/attachments/D28WAHAR/fulltext/images/ddfa0eca7d67fa0b9e7a705c15b8bdb28a82a1a74d221ab7cfbf17a80a3c9578.jpg)

One final point also illustrated in panels (c) and (d) of Figure 1 is another pricing strategy change at the junction between areas D and E. When the magnitude of security losses is not too high $( \mathrm { i } . \mathrm { e } . , \ \alpha = 2 0 )$ and patching costs increase to a larger level, the vendor is incentivized to significantly increase its on-premises product price to reduce the size of the purchasing onpremises population thus limiting the negative security externality to an extent wherein these consumers now have much reduced incentives to patch their products.

Rather than continuing to cut its on-premises price to ensure that a patching population exists to limit undirected security risk, a substantial price increase allows the vendor to serve only the highest valuation market with its on-premises product. Complementing this strategic price increase is a drop in its SaaS price to capture more of the market at the lower end. However, for any level of patching costs, as the security loss factor grows high enough, area E as depicted in Figure 1 disappears due to the large losses users incur when being unpatched; this is the essence of Proposition 1.

Having developed an understanding of the conditions under which the vendor targets its SaaS product to the middle and lower tiers of the consumer market, we next study how its versioning strategy affects social welfare. We aim to highlight which of the two consumer market characterizations that arise under optimal vendor pricing, as fully described in Proposition 1, is socially preferable. We also particularly identify regions in which welfare can be increased if the vendor were incentivized to induce the market outcome that goes against its preference.

<sup>Proposition</sup> <sup>2.</sup> For high security-loss environments, when patching costs are within an intermediate range and the SaaS alternative’s quality is high, i.e., $\underline { { c } } _ { p } < c _ { p } < 1 / 3$ and $\delta > \eta ,$ , social welfare can be increased if incentives are provided to encourage the software vendor to target its SaaS alternative to the middle tier rather than the lower tier of the consumer market. However, for most other levels of patching costs and SaaS quality, the vendor-preferred outcome is also better for welfare. Technically, there exist $\underline { { c } } _ { p } > ( 1 7 - 4 \sqrt { 1 5 } ) / 7$ and $\eta > ( 2 ( 7 - 1 4 c _ { p } + 3 c _ { p } ^ { 2 } ) ) / ( ( 7 - c _ { p } ) ( 1 + c _ { p } ) )$ such that

(i) If $\underline { { c } } _ { p } < c _ { p } < 1 / 3$ and $\delta > \eta ,$ , then $W | _ { p ^ { \ast } , p _ { s } ^ { \ast } } < W | _ { p ^ { M } , p _ { s } ^ { M } } ;$ (ii) If $\delta < ( 2 ( 7 - 1 4 c _ { p } + 3 c _ { p } ^ { 2 } ) ) / ( ( 7 - c _ { p } ) ( 1 + c _ { p } ) )$ , or $c _ { p } > 1 / 3$ and $\delta > ( 2 ( 1 - c _ { p } ) ) / ( 1 + c _ { p } )$ , then $W | _ { p ^ { * } , p _ { s } ^ { * } } =$ max $( W ^ { L } , W ^ { M } )$

where W <sup>L</sup> and $W ^ { M }$ denote the welfare associated with equilibrium outcomes in Regions II and III, respectively.<sup>16</sup>

Proposition 2 establishes that there exists an interval of patching costs where the vendor will prefer to induce a low-tier SaaS outcome characterized by $v _ { p } > v _ { u } > v _ { d }$ (Region II of Corollary 1) with its pricing, whereas social welfare would be strictly higher if it is priced at $p ^ { M }$ and $p _ { s } ^ { M }$ to induce the middle-tier SaaS, $v _ { p } > v _ { d } > v _ { u }$ (Region III of Corollary 1) consumer market outcome. The rationale here is that when the vendor adapts its strategy to target the SaaS offering to the middle tier of the consumer market, it effectively increases the size of the patched population by dropping the on-premises price and restricts the size of the SaaS user population by increasing the SaaS price. Combining these effects, the total security losses on the network are smaller which, in aggregate, leads to higher welfare, despite the negative impact of restricted use. Part (i) of Proposition 2 establishes that there exist intervals near the upper bound on patching costs and near the lower bound on the SaaS quality parameter where providing external incentives to the vendor and/or users may help encourage the socially-preferable outcome. However, part (ii) of the proposition also establishes that, in many cases, an outcome wherein the SaaS alternative is directed to the lower tier of the consumer market is also consistent with welfare considerations.

## 5.2. Comparison to Benchmark

In this section, we examine how a software vendor’s decision to release SaaS versions of its traditionally onpremises software product (as detailed in §5.1) affects profitability, social welfare, and the security properties of the network relative to benchmark outcomes where only an on-premises offering is made. Additionally, we study the impact of introducing SaaS on consumer surplus. For convenience, we use the subscript BM to denote that the measure is under the benchmark outcome where the on-premises version is the sole offering.

Lemma 2 (Benchmark Under High <sub></sub>). <sub>For</sub> <sub>high</sub> <sub>se-</sub> curity-loss environments without SaaS versioning $( i . e . ,$ $\delta = 0 )$ , under optimal pricing there always exists a positive mass of customers who prefer patching on-premises software 4OP 1 P ) and a positive mass of consumers who prefer to use on-premises software but not patch it 4OP1 NP5. The equilibrium purchasing and patching thresholds satisfy $0 < v _ { u } < v _ { p } < 1$

Lemma 2 shows that when the quality of the SaaS offering goes to zero, or equivalently SaaS is not offered, the vendor will set the on-premises price to induce both patched and unpatched populations in equilibrium. In a high security-loss environment, the unpatched population is exposed to significant undirected security risk and shrinks to help limit the security externality. The case where $\delta = 0$ is a special case where our model converges to the model in August and Tunca (2006), hence the equilibrium pricing and market structure characterization are both consistent. This case is an appropriate benchmark for comparison of economic and security measures when $\bar { \delta \mathbf { \bar { \Gamma } } } > 0$ and versioning occurs.<sup>17</sup>

First, we examine profitability and welfare comparisons with the benchmark solution. Proposition 1 establishes that, for high security-loss environments, the software vendor will release both alternatives and target the SaaS version to the middle tier when patching costs $( c _ { p } )$ are high; the SaaS version has similar quality (i.e., high ). In the following proposition, we demonstrate that a joint offering strategy substantially increases profits and social welfare. Furthermore, we characterize how $c _ { p } , \delta ,$ , and the likelihood of a directed attack on the SaaS offering $( \pi _ { d } )$ affect the extent to which the outcome of the joint offering improves these measures.

<sup>Proposition</sup> <sup>3.</sup> For high security-loss environments, both vendor profits and social welfare can increase substantially under a joint offering strategy. Both relative measures of improvement are increasing in patching costs and the quality of the SaaS version, but decreasing in the likelihood of directed attacks. Technically, there exists 1 $\kappa > 0$ such that for all $\alpha > \underline { { \omega } } .$

$$
\left| \frac {\Pi^ {*} - \Pi_ {\mathrm{BM}}}{\Pi_ {\mathrm{BM}}} - \frac {c _ {p} \delta}{\pi_ {d} \alpha (1 - c _ {p}) ^ {2}} \right| <   \frac {\kappa}{\alpha^ {2}}\tag{21}
$$

and

$$
\left| \frac {W ^ {*} - W _ {\mathrm{BM}}}{W _ {\mathrm{BM}}} - \frac {2 c _ {p} \delta}{3 \pi_ {d} \alpha (1 - c _ {p}) ^ {2}} \right| <   \frac {\kappa}{\alpha^ {2}}
$$

are satisfied.

(22)

Proposition 3 establishes that the introduction of a SaaS offering can result in substantial percentage increases in profits and social welfare. Examining the inequalities in (21) and (22), it is straightforward to see that both normalized measures decrease in $\pi _ { d }$ but increase in $c _ { p }$ and . A decrease in $\pi _ { d }$ corresponds to reduced directed security risk for consumers who use the SaaS alternative in equilibrium. In a similar vein, an increase in  also reflects a higher quality SaaS offering, which is beneficial to both vendor profitability and social welfare. On the other hand, for $c _ { p } ,$ the potential improvement associated with a SaaS release stems from consumers’ patching behavior of the on-premises solution. In particular, as patching costs increase, consumers find it incentive compatible to bear more undirected security risk rather than incurring these patching costs. Given the negative externalities unpatched users can inflict on the network, under these circumstances, introducing the SaaS alternative can have an even stronger effect by inducing consumers to split use across alternatives and diversify this security risk to include more directed risk (and less undirected risk).

Next, focusing on high security-loss environments, which have the greatest potential for improvement, we examine how introducing a SaaS alternative affects the security properties of the network as well as consumer surplus. By (10), we can define the average per-user security losses as follows:

$$
\widehat {S L} \triangleq \frac {S L}{u (\sigma^ {*}) + d (\sigma^ {*}) + n (\sigma^ {*})},\tag{23}
$$

which simplifies to either $S L / ( 1 - v _ { d } )$ or $S L / ( 1 - v _ { u } )$ in Regions II and III of Corollary 1, respectively.

<sup>Proposition</sup> <sup>4.</sup> When a SaaS version is introduced in high security-loss environments:

(i) The average security losses per user decrease under high patching costs, i.e., $c _ { p } \geq \delta / ( 4 - \delta )$ , but actually increase otherwise;

(ii) Despite the substantial increase in welfare stemming from a SaaS release, when patching costs are low, $i . e . ,$ $c _ { p } \leq 1 / 3 ,$ and the SaaS offering quality parameter satisfies $\delta > 2 - ( 6 4 c _ { p } ^ { 2 } \pi _ { d } ( 1 - c _ { p } ( 4 - c _ { p } ) ) ) / ( \pi _ { u } ( 1 + c _ { p } ) ^ { 4 } )$ , consumer surplus decreases in equilibrium.

Part (i) of Proposition 4 reveals an important insight: A vendor’s diversification of software use by offering both on-premises and SaaS versions can actually increase per-user security losses. One would expect that introducing a SaaS alternative would split the undirected risk being faced in the benchmark case into two smaller risks (undirected and directed), as a portion of the consumers adopt the SaaS alternative instead. However, part (i) of Proposition 4 establishes that a software vendor may influence use and patching behavior through pricing in such a way that the average security losses per user is higher in the joint offering.

In high security-loss environments, when SaaS is introduced, some consumers who would have elected to buy the on-premises product and remain unpatched, i.e., 4OP1 NP5, in the benchmark case now have incentives to switch to SaaS, i.e., 4SaaS1 ND5. Because this reduces the size of the unpatched population, consumers who were buying the on-premises product and patching, i.e., 4OP1 P 5, are no longer facing as large a negative externality. Therefore, they have overall reduced incentives to patch, and some of these consumers will now elect to remain unpatched. Also, because introduction of SaaS splits risk into undirected and directed types, some consumers who had opted out in the benchmark case will now become users. Thus, in comparison to the benchmark case, when both on-premises and SaaS versions are offered, overall use increases while overall patching decreases.

Part (i) of Proposition 4 establishes that when patching costs are small, the aforementioned cumulative effect of increased use and decreased patching associated with the introduction of SaaS results in higher average per-user security losses. When patching costs are small, the consumer market structure is already characterized by a large patching population in the benchmark case. The population of unpatched onpremises users is, by contrast, relatively small. Hence, when SaaS is introduced, although patching slightly decreases, the proportional increase in either unpatched or SaaS use is substantial. A relatively large increase in these two types of use, which are exposed to undirected and directed security risk, respectively, can lead to higher average security losses because of the accompanying negative externalities. On the other hand, when patching costs are large, the benchmark case is characterized by a small patching population and large unpatched population. In this case, aggregate SaaS and unpatched on-premises use still increases while patching decreases. However, the reduction in patching behavior has a relatively minor negative effect on an already substantial unpatched population. In contrast to the case above, the diversification benefits of splitting security risk into undirected and directed types now outweighs the minor increase in the externality. Thus, for large patching costs, per-user security losses decrease when SaaS is made available.

One might expect that consumer surplus would increase when a software vendor offers a menu of differentiated products with idiosyncratic security risks, but that is not always the case as we establish in part (ii) of Proposition 4. Because, surprisingly, average per-user security losses can increase when a software vendor introduces a SaaS version of its on-premises product, from a consumer perspective such a release may not necessarily be beneficial. Part (ii) of Proposition 4 suggests that for software with relatively lower patching costs (such as client applications), a vendor will release a SaaS version not for the benefits of reduced security risk but rather to expand its market at the lower end and price discriminate. The net effect of its joint offerings on consumer surplus is negative, which is partly driven by the increase in security losses formalized in part (i) of Proposition 4.

## 6. Low Security-Loss Environment

For additional insight into the overall security landscape, we next examine environments where consumers are subject to smaller economic losses associated with security attacks. Here we focus on a class where  is small, and study software applications belonging to this class such as client applications that are less mission critical to business operations. Some examples include anti-virus client software, media players, document readers, and perhaps even productivity software such as Microsoft Office 365. We take a similar approach to $\ S 5$ by further characterizing the consumer market equilibrium, which is simplified when considering only a low security-loss environment. Subsequently, we examine the vendor’s versioning decision and compare profitability, social welfare, security losses, and consumer surplus to the benchmark measures for this case.

As the security loss factor  decreases, users of on-premises software will find it better to assume undirected security risk than to incur patching costs. Thus, a patching population will not arise in equilibrium as is formalized in the following corollary.

Corollary 2 (Equilibrium Under Low <sub></sub>). <sub>Given</sub> on-premises and SaaS prices, $p \in ( 0 , 1 )$ and $p _ { s } \in ( 0 , \delta )$

respectively, and other parameters $c _ { p } , \pi _ { d } , \pi _ { u } ,$ and $\delta ,$ the equilibrium consumer strategy profile $\sigma ^ { * }$ satisfies:

Region I (No SaaS). $I f p \leq p _ { s } / \delta$ and  $: \leq \mathrm { m i n } ( \alpha _ { B } , \alpha _ { A } ) \overset { \Delta } { = }$ $\delta ( p _ { s } - p \delta ) / ( p _ { s } \pi _ { u } ( \delta - p _ { s } ) ) , \alpha _ { C } \dot { \stackrel { \Delta } { = } } ( 1 - p + p _ { s } - \delta ) ( p - p _ { s } + \delta ) /$ $( \pi _ { u } ( \delta - p _ { s } ) )$ , then $p < v _ { u } < 1$ and $\sigma ^ { * }$ is given by either (6) with $v _ { d } = v _ { u }$ and $v _ { p } = 1$ or (7) with $v _ { d } = v _ { p } = 1$

Region II (SaaS for low tier). $I f p _ { s } / \delta < ^ { \prime } p \leq 1 + p _ { s } - \delta$ and $\alpha \leq \hat { \alpha } _ { 1 } ,$ then $p _ { s } < v _ { d } < v _ { u } < 1$ and $\sigma ^ { * }$ is given by (6) with $v _ { p } = 1$

Region III (SaaS only). If $1 + p _ { s } - \delta < p$ and $\alpha \leq \alpha _ { D } \triangleq$ $( 1 - p + p _ { s } ) ( p - 1 - p _ { s } + \delta ) / ( \delta \pi _ { d } ( 1 - p ) )$ , then $p _ { s } < v _ { d } < 1$ and $\sigma ^ { * }$ is given by either (6) with $v _ { u } = v _ { p } = 1$ or (7) with $v _ { u } = v _ { d }$ and $v _ { p } = 1$

As can be seen in Corollary 2, in equilibrium, there are three possibilities for the consumer market structure: the on-premises version is preferred by all users and not patched (Region $\operatorname { I } ) ;$ higher valuation users prefer the on-premises version and do not patch while lower valuation users prefer SaaS (Region II); and finally all users prefer SaaS (Region III). Given this consumer market outcome, we next analyze the vendor’s versioning problem.

## 6.1. Versioning Strategy

As presented in Proposition 1, in high security-loss environments, the vendor has strong incentives to release a SaaS offering to change the structure of the network and reduce security risk by splitting the user population; this helps to limit both directed and undirected security attacks, which are influenced by total SaaS user and unpatched on-premises population sizes, respectively. In high security-loss environments, the margin for improvement is large. However, as the security loss factor decreases, the benefit of risk diversification becomes more limited. An open question in the literature is whether versioning makes sense in the presence of security externalities as their impact decreases.

<sup>Proposition</sup> <sup>5.</sup> In low security-loss environments,<sup>18</sup> a software vendor still prefers to offer both on-premises and SaaS versions of its software.

In contrast to Proposition 1, one might expect that as the security risk associated with software decreases a software vendor would shift toward a strategy where it prices its offerings in such a way that only the higher quality offering is consumed. This outcome would be consistent with the literature on versioning of information goods. Specifically, in the absence of unit costs and when consumer valuations (or quality sensitivities) are uniformly distributed, a monopolist with two different quality substitutes will price them such that only the high quality substitute is consumed in equilibrium. In other words, in such a case, the vendor will not version its product. Because versioning is frequently observed with information goods, the literature on versioning of information goods has worked to reconcile this inconsistency.

Proposition 5 examines this versioning issue from a security perspective. Specifically, in the absence of the negative security externalities present in our model, because consumers have uniform valuations and the SaaS offering has a quality reduction factor, consistent with the versioning literature, the vendor would optimally offer only the higher quality information good. However, when consumers of both versions are exposed to negative security externalities in the form of directed risk for the SaaS offering and undirected risk for the on-premises offering, Proposition 5 establishes that it is still optimal for the vendor to offer both versions even in low security-loss environments. In fact, as  diminishes, we analytically demonstrate that it is always profitable to introduce the SaaS offering. In our case, the fact that each product is exposed to a unique externality (directed or undirected risk) creates the separation necessary for versioning to become optimal. From a practical standpoint, this result provides another alternative explanation for the commonplace existence of multiple versions of software products: As long as the versions have some idiosyncratic risk stemming from their respective user populations, however small, it is profit-maximizing to set prices such that both versions are consumed in equilibrium.

## 6.2. Comparison to Benchmark

Analogous to §5.2, next we examine how a software vendor’s optimal decision to release a SaaS version of its product (as established in Proposition 5) affects profitability, social welfare, security losses, and consumer surplus in comparison to a benchmark. As before, for an appropriate benchmark, we use measures computed under the equilibrium solution to the case wherein  = 0, which is to say that the on-premises software is the sole offering. These benchmark measures then coincide with those computed in August and Tunca (2006).

Lemma 3 (Benchmark Under Low <sub></sub>). <sub>For</sub> <sub>low</sub> <sub>se-</sub> curity-loss environments without SaaS versioning (i.e., $\delta = \dot { 0 } )$ , under optimal pricing there is only a positive mass of customers who prefer not to patch on-premises software 4OP1 NP5 in equilibrium. The equilibrium purchasing and patching thresholds satisfy $0 < v _ { u } < v _ { p } = 1$

The benchmark equilibrium characterized in Lemma 3 is similar to the outcome that unfolds from Corollary 2 and Proposition 5 in that no consumer will find it optimal to patch her on-premises software in equilibrium. Thus, all users face some degree of undirected security risk even though it is low, while under the versioning outcome in Proposition $5 ,$ risk is diversified as users separate into on-premises and SaaS user populations. Next, we compare these two outcomes.<sup>19</sup>

For low security-loss environments, we characterize the relative benefit of introducing SaaS in the following proposition.

<sup>Proposition</sup> <sup>6.</sup> For low security-loss environments, introduction of a SaaS version will provide a limited increase in vendor profits and social welfare. Both relative measures of improvement are increasing in the quality of the SaaS version and the likelihood of undirected attacks. Technically, there exists 1¯ $\eta > 0$ such that for all $\alpha < \bar { \omega } ,$

$$
\left| \frac {\Pi^ {*} - \Pi_ {\mathrm{BM}}}{\Pi_ {\mathrm{BM}}} - \frac {\delta \pi_ {u} ^ {2} \alpha^ {2}}{1 6 (1 - \delta)} \right| <   \eta \alpha^ {3}\tag{24}
$$

and

$$
\left| \frac {W ^ {*} - W _ {\mathrm{BM}}}{W _ {\mathrm{BM}}} - \frac {5 \delta \pi_ {u} ^ {2} \alpha^ {2}}{4 8 (1 - \delta)} \right| <   \eta \alpha^ {3}\tag{25}
$$

are satisfied.

Although Proposition 5 demonstrates that a vendor should optimally release both on-premises and SaaS versions of its product in low security-risk environments, Proposition 6 suggests that the benefits stemming from diversification are much more limited in these environments. In contrast to Proposition 3, by comparing (21) and (24), the percentage increase in profits associated with releasing the SaaS alternative is an order of magnitude smaller. In this sense, security concerns alone may not justify the additional costs of managing two separate versions of the software.

The findings in Propositions 3 and 6 are illustrated in Figure 2. We depict three curves plotting the measure $( \Pi ^ { * } - \Pi _ { \mathrm { B M } } ) / \Pi _ { \mathrm { B M } }$ computed numerically under parameter sets A: $c _ { p } = 0 . 3 0$ $\pi _ { u } = 0 . 2 3$ , B: $\dot { c _ { p } ^ { \prime } } = 0 . 5 0$ $\pi _ { u } = 0 . 2 3$ , and C: $c _ { p } \overset { \cdot } { = } 0 . 3 0 , \pi _ { u } ^ { \prime } = 0 . 5 5 ,$ , respectively. As can be seen, near $\dot { \alpha } = 3 0$ , the percentage improvement in profits ranges from approximately 10%–30% under these parameter sets; however, near $\alpha = 1 / 3 0 ,$ , the percentage improvement is negligible. This is the essence of the two propositions, i.e., diversification of security risk by offering SaaS has much greater potential for moderate to high security-loss environments. Comparing curve B to A, one can see that an increase in patching costs from $c _ { p } = 0 . 3 0$ to $c _ { p } ^ { \prime } = 0 . 5 0$ can change the potential profit improvement of a SaaS release strategy substantially because of the poor patching behavior induced on the network at this higher cost level.<sup>20</sup> This characteristic is consistent with the results presented in Proposition 3, in particular from (21). Similarly, for lower $\alpha ,$ Proposition 6 and specifically (24) suggest that an increase in the likelihood of an undirected attack $( \pi _ { u } )$ will also increase the potential benefit of a diversification strategy. In Figure 2, we can see this effect by comparing curve C to A within the lower range of .

Figure 2 Percentage Increase in Vendor Profitability When a SaaS Version is Offered in Addition to an on-Premises Version of Software  
![](/api/attachments/D28WAHAR/fulltext/images/bdff2272121f718692c7c24e1b2376bd1ae74d6615b49f97fde3720e0ce35c1b.jpg)  
Notes. This percentage is plotted over a wide range of security-loss environments. Values for patching costs and undirected attack probabilities are listed on the plot. The other parameter values are $\delta = 0 .$ 080 and $\pi _ { d } = 0 . 1 0$

Next, we examine security losses and consumer surplus. In low security-loss environments, the effect of versioning on these two measures differs considerably from what we established for high security-loss environments.

<sup>Proposition</sup> <sup>7.</sup> When a SaaS version is introduced in low security-loss environments, the average security losses per user decrease and consumer surplus increases in equilibrium.

For high security-loss environments, in Proposition 4, we established that when patching costs are low, the average security losses per user actually increase when the vendor versions by introducing a SaaS solution. When potential security losses become limited, Proposition 7 formally establishes that a similar type of outcome cannot happen; that is, by offering a SaaS version in addition to an on-premises version, the vendor can effectively diversify the undirected risk under the benchmark case into two smaller risks of the undirected and directed variety, which reduces the average security losses. Because the potential security losses are inherently limited, the negative impact of a reduction in the patching population is smaller than the positive diversification effect. Moreover, the introduction of SaaS benefits consumers in terms of security risk considerations and differentiated pricing.

## 7. Extension: Security Investment

In this section, we study a setting where the software vendor can invest to increase the security of its SaaS and on-premises offerings. We assume the firm can invest effort levels $\epsilon _ { u } , \epsilon _ { d } \in [ 0 , 1 )$ to reduce the security risks associated with the on-premises and SaaS versions, respectively. $\mathbf { A } \mathbf { n }$ effort investment of $\epsilon _ { u }$ yields a risk reduction from $\pi _ { u }$ to $( 1 - \epsilon _ { u } ) \pi _ { u }$ . Similarly, $\epsilon _ { d }$ being exerted reduces $\pi _ { d }$ to $( 1 - \epsilon _ { d } ) \pi _ { d } .$ . Because $\epsilon _ { u }$ reduces the likelihood of a vulnerability in the on-premises product, it also reduces the expected patching cost from an initial value of $c _ { p }$ to $( 1 - \epsilon _ { u } ) c _ { p }$ . The respective costs associated with effort investments to improve security are denoted as $C _ { u } ( \epsilon _ { u } )$ and $C _ { d } ( \epsilon _ { d } )$ , where both cost functions are twice-differentiable, convex, increasing, and satisfy $C _ { u } ( 0 ) = C _ { d } ( 0 ) = C _ { u } ^ { \prime } ( 0 ) = C _ { d } ^ { \prime } ( 0 ) = 0$ . For technical reasons, we assume there exists a constant $\tau > 0$ such that $C _ { u } ^ { \prime \prime } ( \cdot ) , C _ { d } ^ { \prime \prime } ( \cdot ) > \tau$

As we have seen thus far, versioning is an effective way to achieve risk diversification. Hence, pricing SaaS and on-premises versions can also be used as a tool by the software vendor to influence consumption decisions toward profitable consumer market structures. In this extension, we aim to understand how the vendor’s additional ability to invest in the security of both products influences outcomes. In particular, we examine the interaction between the vendor’s versioning decision and security investments. In the following proposition, we first explore how the vendor’s security investments differ across high and low security-loss environments.

<sup>Proposition</sup> <sup>8.</sup> In low security-loss environments, the firm increases its security-improving investments for both on-premises and SaaS versions as risk increases in the market, $i . e . , \epsilon _ { u } ^ { \ast } ( \alpha )$ and $\epsilon _ { d } ^ { * } ( \alpha )$ are increasing in . However, in high security-loss environments, if the likelihood of an undirected attack relative to a directed attack, patching costs, and SaaS quality are all sufficiently high, the vendor increases security-improving efforts for the on-premises version and decreases efforts for the SaaS version as risk increases in the market. Technically, there exists $\hat { r } > 0$ such that $i f \pi _ { u } / \pi _ { d } > \hat { r } ,$ $c _ { p } > 1 / 2 , \tau > 1 / 2$ , and $\delta > \bar { \delta } \triangleq 2 ( 1 - c _ { p } ) / ( 1 + c _ { p } - 2 c _ { p } ^ { 2 } )$ are satisfied, then $\epsilon _ { u } ^ { * } ( \alpha )$ increases in  whereas $\epsilon _ { d } ^ { * } ( \dot { \alpha } )$ decreases in .

Figure 3 illustrates the results in Proposition 8 and the underlying intuition. In low security-loss environments, consumers tend to prefer a limited, undirected security risk rather than incurring the costs of patching. For this reason, the vendor does not need to increase security investment in the on-premises product with a goal of reducing the expected patching costs. However, it may invest effort in the on-premises product to slightly reduce the risk consumers face in equilibrium. Its incentives to invest in SaaS security are similar. Both equilibrium effort levels are illustrated in panel (b) of Figure 3 in the area labeled A. As  increases, the vendor increases both of its investment levels to throttle equilibrium risk; this can increase quickly because no one patches in equilibrium as illustrated in panel (a) of Figure 3 in area A.

In high security-loss environments, the vendor’s investment behavior differs substantially from that described above. Remarkably, its security investments in on-premises and SaaS versions diverge. Under potentially high security losses, consumers have much stronger incentives to patch and protect themselves if using the on-premises product. In fact, the vendor also wants to reduce the expected patching costs by increasing its effort to improve on-premises security. As we saw earlier in Proposition 1, under high patching costs and high SaaS quality, the vendor pursues a strategy wherein SaaS is targeted to the middle tier of the consumer market. An essential element of this strategy is that the vendor must limit equilibrium directed security risk such that the SaaS version is consumed by this middle tier segment. The vendor can accomplish this in two ways, i.e., investing in security of the SaaS product directly, or limiting the SaaS population to indirectly achieve greater security. As  increases, because of its strong incentives to invest in the on-premises product to reduce patching costs, high tier consumers shift toward patched, on-premises use away from SaaS. Because the SaaS population becomes more limited and achieves greater security as a result, the vendor can decrease its investment in SaaS product security to reduce costs. Its investment behavior is illustrated in area B of panel (b). Area B of panel (a) shows how the patching population increases while the SaaS population shrinks. The following result is connected to this discussion.

<sup>Proposition</sup> <sup>9.</sup> In high security-loss environments, when baseline consumer patching costs and SaaS quality are high, and the firm’s security-improving costs are sufficiently convex, the vendor invests greater effort in addressing on-premises product security than SaaS, i.e., $\epsilon _ { u } ^ { * }$ is greater than $\epsilon _ { d } ^ { * } ,$ while also targeting SaaS to the middle tier of the consumer market in equilibrium.

Proposition 9 formalizes our finding that the software vendor may continue to target its lower inherent quality SaaS product to the middle tier even when it can invest to improve security instead. Significantly, its behavior in this case hinges on the convexity of its investment costs not being too low. In the alternative case, the vendor would have incentives to make its on-premises product extremely secure, leading to a strategy wherein SaaS is geared to the lower tier of the market.

Figure 3 The Impact of Varying Security-Loss Environments on Security Investment and the Consumer Market  
![](/api/attachments/D28WAHAR/fulltext/images/9318c15bd0bd2d5629a97139c07bcb559e21d814c95da862555defbfd65b2139.jpg)

![](/api/attachments/D28WAHAR/fulltext/images/1af7fbd25280964ee5d6d3e994a29f40d81a7e163f313bd93b04714c847692b8.jpg)  
Notes. The parameter values are $\pi _ { u } = 0 . 2 , \pi _ { d } = 0 . 3 , c _ { p } = 0 . 5 ,$ , and $\delta = 0 . 9$ . For this numerical illustration, we use cost functions $C _ { u } ( \cdot ) = C _ { d } ( \cdot ) = C ( \epsilon ) =$ $( 1 / ( 1 - \epsilon ) - 1 ) ^ { 2 }$ which satisfy all technical conditions.

## 8. Concluding Remarks

In this paper, we explore how a vendor’s offering of on-premises and SaaS versions of application software affects users’ consumption incentives. In particular, we analytically demonstrate how users segment across products to manage the endogenously determined security externalities associated with unpatched onpremises behavior (undirected risk) and SaaS use (directed risk). Using our characterization of equilibrium consumer behavior, we rigorously study the software vendor’s versioning problem and reveal several interesting insights. First, the vendor is sometimes incentivized to market its lower inherent quality SaaS version to a higher valuation consumer segment than the segment to which it targets its higher inherent quality on-premises version. In this case, the vendor strategically sets a high SaaS price to reduce its use and the associated level of directed security risk such that it offers a more secure product, albeit with fewer features, to a more quality-sensitive consumer segment. Panel (a) of Table 1 illustrates that this result is obtained in high security-loss environments when patching costs are high and the inherent quality of the SaaS version is not too low, i.e., $\Pi ^ { M } > \dot { \Pi } ^ { L }$ in the cell corresponding to High $c _ { p } / \mathrm { H i g h } \ \delta$ . We also analytically establish that when patching costs are within an intermediate range and the inherent quality of the SaaS version is still reasonably close to its on-premises counterpart, the vendor will prefer to target its SaaS product to the low tier when it is advantageous to social welfare if it would instead target it to the middle tier; additional vendor incentives can lead to welfare-superior outcomes in this region. This result can be seen in the cell in panel (a) of Table 1 corresponding to Medium $c _ { p } / \mathrm { H i g } \bar { \mathrm { h } } \ \delta .$

In the versioning literature, for uniformly distributed consumer types and zero marginal costs, the standard result is that a software vendor will find it optimal to offer only its higher quality product to consumers. In our study, we formally demonstrate that because of risk diversification benefits, the vendor will always offer both versions of its product as long as the risks associated with each version are idiosyncratic. Interestingly, this versioning result holds even as the security risk becomes negligible. In panel (a) of Table 1, we indicate that for low security-loss environments, the software vendor always gears its SaaS version to the lower tier of the market, pricing its higher quality on-premises version to serve the higher tier. Because a patching population does not exist in equilibrium, we use $\Pi ^ { \breve { H } }$ and $W ^ { H }$ to refer to measures of profit and welfare if SaaS were targeted to the higher tier instead, which is shown to be a dominated strategy.

We compare economic measures (profitability, social welfare, security losses, and consumer surplus) under a versioning strategy against analogous measures in a benchmark case where the on-premises version is solely offered to consumers. We demonstrate that the potential improvement in profits and social welfare associated with a SaaS release and its corresponding security risk diversification are substantial in high security-loss environments, but more limited in the low security-loss environment. In spirit, introduction of a SaaS version with a different exposure to directed and undirected attacks than the on-premises version can help reduce the overall security risk to the network because of these diversification benefits. As can be seen in panel (b) of Table 1, for low security-loss environments and for high security-loss environments when patching costs are high, average per-user security losses indeed decline as a result of versioning. However, our study also highlights that because of opportunistic pricing by the vendor, the security risk diversification benefits are sometimes outweighed by market expansion, leading to higher average per-user security losses. This result can be seen in the cell corresponding to Low $c _ { p } / \mathrm { H i g h } \delta .$ In this case, introduction of a SaaS version can even lead to depressed consumer surplus as indicated in Table 1. For high security-loss environments, when the inherent quality of the SaaS offering and patching costs are low, with SaaS versioning average per-user security losses can go in either direction as is established in Proposition 4.

Table 1 Summary of Results on How SaaS Versions Are Targeted to Consumer Segments and How Measures of Average Per-User Security Losses and Consumer Surplus Compare to Benchmarks

<table><tr><td rowspan="3"></td><td colspan="3">(a)</td></tr><tr><td colspan="2">High security-loss environment</td><td>Low security-loss environment</td></tr><tr><td>Low δ</td><td>High δ</td><td>All δ</td></tr><tr><td>Low cp</td><td>ΠL &gt; ΠMW^L &gt; W^M</td><td>ΠL &gt; ΠMW^L &gt; W^M</td><td rowspan="3">ΠL &gt; ΠHW^L &gt; W^H</td></tr><tr><td>Medium cp</td><td rowspan="2">ΠL &gt; ΠMW^L &gt; W^M</td><td>ΠL &gt; ΠMW^M &gt; W^L</td></tr><tr><td>High cp</td><td>ΠM &gt; ΠLWM^M &gt; W^L</td></tr><tr><td colspan="4">(b)</td></tr><tr><td>Low cp</td><td> $\widehat{SL} \uparrow \downarrow, CS \uparrow$ </td><td> $\widehat{SL} \uparrow, CS \downarrow$ </td><td rowspan="2"> $\widehat{SL} \downarrow, CS \uparrow$ </td></tr><tr><td>High cp</td><td colspan="2"> $\widehat{SL} \downarrow, CS \uparrow$ </td></tr></table>

Notes. For the high security-loss environment columns, panel (a) summarizes profit and social welfare comparisons dependent on whether the SaaS version is priced to serve the low tier (superscript L) or the middle tier (superscript M). For the low security-loss environment column, because there are only two consumer segments in equilibrium, the comparisons involve the low tier and the high tier (superscript H). Panel (b) indicates whether average per-user security losses and consumer surplus increase or decrease under SaaS versioning.

In recent years, companies have invested millions to provide SaaS versions of on-premises application software. Our study focuses on the security benefits of SaaS offerings in terms of risk-mitigated versioning. Given our research goals, we abstract away from modeling concerns that are outside of our paper’s scope. For example, to implement SaaS alternatives in addition to their traditional on-premises offerings, software vendors would necessarily need to incur additional costs in practice. These costs would have a fairly large fixed-variable cost ratio. One potential future research trajectory is to develop a better understanding of why we observe the existence of vendors who do not offer both SaaS and on-premises versions (e.g., Salesforce.com). By understanding the vendor’s incentives outside of security concerns that underlie this type of behavior, we could also explore what leads to outcomes in a single market where competing firms each offer one version, SaaS or on-premises, and choose to differentiate themselves by specializing.

The benefits of cloud computing and, particularly, SaaS applications are driving businesses and governments to migrate many internally supported systems and software to the cloud. However, such a paradigm shift can have major consequences on security risks as consumers make choices on software deployment and protection. We hope that the model and insights presented in this paper provide a stepping stone toward a broader understanding of how security risk can be managed as cloud computing matures and becomes an integral part of IT strategies.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2014.0527.

## Acknowledgments

The authors thank Rahul Telang (the senior editor), the associate editor, and the anonymous reviewers for their helpful suggestions throughout the review process. The authors also thank Sridhar Narasimhan, D. J. Wu, Subodha Kumar, Ali Tafti, Ramnath Chellappa, the participants at the Conference on Information Systems and Technology 2012, INFORMS 2012 Annual Meeting, the Workshop on the Economics of Information Security 2013, as well as the participants in the research seminar at the University of California, Irvine for their helpful comments and discussions. This material is based on work partially supported by the National Science Foundation [Grant CNS-0954234].

## References

Anderson R (2001) Why information security is hard—An economic perspective. Proc. 17th Annual Comput. Security Appl. Conf. (IEEE Computer Soc., Washington, DC), 358–365.

Anderson R, Moore T (2006) The economics of information security. Science 314(5799):610–613.

Arora A, Telang R, Xu H (2008) Optimal policy for software vulnerability disclosure. Management Sci. 54(4):642–656.

August T, Tunca TI (2006) Network software security and user incentives. Management Sci. 52(11):1703–1720.

August T, Tunca TI (2008) Let the pirates patch? An economic analysis of software security patch restrictions. Inform. Systems Res. 19(1):48–70.

August T, Tunca TI (2011) Who should be responsible for software security? A comparative analysis of liability policies in network environments. Management Sci. 57(5):934–959.

Bain C, Faatz DB, Fayad A, Williams D (2002) Diversity as a defense strategy in information systems. Does evidence from previous events support such an approach? Proc. IFIP TC11/WG11.5 Fourth Working Conf. Integrity, Internal Control Security Inform. Systems: Connecting Governance Tech. (Kluwer, B.V., Deventer, The Netherlands), 77–94.

Beil D, Wan Z (2009) RFQ auctions with supplier qualification screening. Oper. Res. 57(4):934–949.

Bhargava HK, Choudhary V (2001) Information goods and vertical differentiation. J. Management Inform. Systems 18(2):89–106.

Bhargava HK, Choudhary V (2008) Research note: When is versioning optimal for information goods? Management Sci. 54(5):1029–1035.

Biddick M (2010) Why you need a SaaS strategy. InformationWeek (January). http://www.informationweek.com/cloud/software -as-a-service/why-you-need-a-saas-strategy/d/d-id/1086146?

Bloor B (2003) The patch problem: It’s costing your business real dollars. White paper, Baroudi Bloor, Arlington, MA. http://www .netsense.info/downloads/PatchProblemReport\_BaroudiBloor.pdf.

Boulton C (2013) American airlines outage likely caused by software quality issues. Wall Street Journal (April). http://blogs.wsj.com/ cio/2013/04/17/american-airlines-outage-likely-caused-by -software-quality-issues/.

Branscombe M (2012) Salesforce talks security: From passwords to animatronic ponies. ZDNet (September). http://www.zdnet.com/ salesforce-talks-security-from-passwords-to-animatronic -ponies-7000004454/.

Cavusoglu H, Cavusoglu H, Raghunathan S (2007) Efficiency of vulnerability disclosure mechanisms to disseminate vulnerability knowledge. IEEE Trans. Software Engrg. 33(3):171–185.

Cavusoglu H, Cavusoglu H, Zhang J (2008) Security patch management: Share the burden or share the damage? Management Sci. 54(4):657–670.

Charney S (2012) Trustworthy computing next. White paper, Microsoft. http://www.microsoft.com/en-us/download/ confirmation.aspx?id=29084.

Chellappa RK, Jia J (2011) Competition and versioning. Working paper, Emory University and Hong Kong University of Science and Technology.

Chellappa RK, Mehra A (2013) Versioning 2.0: A product line and pricing model for information goods under usage constraints and with R&D costs. Working paper, Emory University and Indian School of Business.

Chen P-Y, Kataria G, Krishnan R (2011) Correlated failures, diversification, and information security risk management. MIS Quart. 35(2):397–422.

Choi JP, Fershtman C, Gandal N (2010) Network security: Vulnerabilities and disclosure policy. J. Indust. Econom. 58(4):868–894.

Choudhary V (2007) Comparison of software quality under perpetual licensing and software as a service. J. Management Inform. Systems 24(2):141–165.

Chow R, Golle P, Jakobsson M, Shi E, Staddon J, Masuoka R, Molina J (2009) Controlling data in the cloud: Outsourcing computation without outsourcing control. Proc. 2009 ACM Workshop Cloud Comput. Security, CCSW’09 (ACM, New York), 85–90.

Claburn T (2009) Government embraces cloud computing, launches app store. InformationWeek (September). http://www .informationweek.com/cloud/government-embraces-cloud -computing-launches-app-store/d/d-id/1083137?

Cox B, Evans D, Filipi A, Rowanhill J, Hu W, Davidson J, Knight J, Nguyen-Tuong A, Hiser J (2006) N -variant systems: A secretless framework for security through diversity. Proc. 15th Conf. USENIX Security Sympos., USENIX-SS’06, Vol. 15 (USENIX Association, Berkeley, CA).

Dey D, Lahiri A, Zhang G (2012) Hacker behavior, network effects, and the security software market. J. Management Inform. Systems 29(2):77–108.

El Akkad O (2011) Microsoft wants you to rent an Office in the cloud. Globe and Mail (June). http://www.theglobeandmail.com/ technology/tech-news/microsoft-wants-you-to-rent-an-office -in-the-cloud/article584830.

Farber D (2007) SAP’s challenge to NetSuite, Workday and salesforce.com. ZDNet (September). http://www.zdnet.com/blog/btl/ saps-challenge-to-netsuite-workday-and-salesforce-com/6327.

Forrest S, Somayaji A, Ackley D (1997) Building diverse computer systems. Proc. 6th Workshop Hot Topics Operating Systems (HotOS-VI), HOTOS’97 (IEEE Computer Soc., Washington, DC), 67–72.

Gherbi A, Charpentier R, Couture M (2011) Software diversity for future systems security. CrossTalk 25(5):10–13.

Gordon LA, Loeb MP (2002) The economics of information security investment. ACM Trans. Inform. Syst. Secur. 5(November):438–457.

Greenemeier L, Hoover JN (2007) How does the hacker economy work? InformationWeek (February). http://www.informationweek .com/how-does-the-hacker-economy-work/d/d-id/1051843?

Grossklags J, Christin N, Chuang J (2008) Secure or insure?: A gametheoretic analysis of information security games. Proc. 17th Internat. Conf. World Wide Web, WWW’08 (ACM, New York), 209–218.

Heal G, Kunreuther H (2007) Modeling interdependent risks. Risk Anal. 27(3):621–634.

Huang K-W, Sundararajan A (2005) Pricing models for on-demand computing. Working paper, National University of Singapore and New York University. http://papers.ssrn.com/sol3/ papers.cfm?abstract\_id=1281329.

Hui KL, Hui W, Yue T (2013) Information security outsourcing with system interdependency and mandatory security requirement. J. Management Inform. Systems 29(3):117–156.

IBM (2008) IBM Internet security systems X-Force 2008 mid-year trend statistics. IBM Global Tech. Services. https://www-935.ibm .com/services/us/iss/xforce/midyearreport/xforce-midyear -report-2008.pdf.

Jing B (2007) Network externalities and market segmentation in a monopoly. Econom. Lett. 95(1):7–13.

Johnson JP, Myatt DP (2003) Multiproduct quality competition: Fighting brands and product line pruning. Amer. Econom. Rev. 93(3):748–774.

Johnson ME (2008) Managing Information Risk and the Economics of Security, 1st ed. (Springer, New York).

Jones R, Mendelson H (2011) Information goods vs. industrial goods: Cost structure and competition. Management Sci. 57(1):164–176.

Judge P (2002) Microsoft security push cost \$100 m for .Net server alone. ZDNet (July). http://www.zdnet.com/microsoft-security -push-cost-100m-for-net-server-alone-3002118314/.

Kannan K, Telang R (2005) Market for software vulnerabilities? Think again. Management Sci. 51(5):726–740.

Kannan K, Rahman MS, Tawarmalani M (2013) Economic and policy implications of restricted patch distribution. Working paper, Purdue University and University of Calgary.

Kash W (2013) Software patches eat government IT’s lunch. InformationWeek (September). http://www.darkreading.com/risk -management/software-patches-eat-government-its-lunch/d/ d-id/1111379.

Keizer G (2004) Sasser worm impacted businesses around the world. Network Comput. (May). http://www.networkcomputing.com/ careers-and-certifications/sasser-worm-impacted-businesses -around-the-world/d/d-id/1208406?

Keizer G (2008) Windows users indifferent to Microsoft patch alarm, says researcher. Computerworld (December). http://www .computerworld.com/s/article/9122599/Windows\_users \_indifferent\_to\_Microsoft\_patch\_alarm\_says\_researchers.

Kim BC, Chen P-Y, Mukhopadhyay T (2010) An economic analysis of the software market with a risk-sharing contract. Internat. J. Electronic Commerce 14(2):7–39.

Kim BC, Chen P-Y, Mukhopadhyay T (2011) The effect of liability and patch release on software security: The monopoly case. Production Oper. Management 20(4):603–617.

Kundra V (2011) Tight budget? Look to the “cloud.” New York Times (August). http://www.nytimes.com/2011/08/31/opinion/ tight-budget-look-to-the-cloud.html?\_r=0.

Kunreuther H, Heal G (2003) Interdependent security. J. Risk Uncertainty 26(2–3):231–249.

Laffont J-J, Tirole J (1988) The dynamics of incentive contracts. Econometrica 56(5):1153–1175.

Lahiri A (2012) Revisiting the incentive to tolerate illegal distribution of software products. Decision Support Systems 53(2):357–367.

Lala JH, Schneider FB (2009) IT monoculture security risks and defenses. IEEE Security Privacy 7(1):12–13.

Lee CH, Geng X, Raghunathan S (2013) Contracting information security in the presence of double moral hazard. Inform. Systems Res. 24(2):295–311.

Lee M (2014) Microsoft closes Office 365 admin access vulnerability. ZDNet (January). http://www.zdnet.com/microsoft-closes-office -365-admin-access-vulnerability-7000025369/.

Lemos R (2003) Slammer report: More headaches. ZDNet (February). http://www.zdnet.com/news/slammer-report-more -headaches/127449.

Lemos R (2004) MSBlast epidemic far larger than believed. CNET News.com (April). http://news.cnet.com/MSBlast-epidemic-far -larger-than-believed/2100-7349\_3-5184439.html.

Lewis JA, Baker S (2013) The economic impact of cybercrime and cyber espionage. Report, Center for Strategic and International Studies, Washington, DC.

Li L, McKelvey RD, Page T (1987) Optimal research for Cournot oligopolists. J. Econom. Theory 42(1):140–166.

Liran N (2013) Severe Office 365 token disclosure vulnerability— Research and analysis. Adallom. https://www.adallom.com/ blog/severe-office-365-token-disclosure-vulnerability-research -and-analysis/.

Ma D, Seidmann A (2014) Analyzing software-as-a-service with per-transaction charges. Working paper, Singapore Management University and University of Rochester.

MacLeod WB, Malcomson JM (1993) Investments, holdup, and the form of market contracts. Amer. Econom. Rev. 83(4):811–837.

Markoff J (2009) Defying experts, rogue computer code still lurks. New York Times (August). http://www.nytimes.com/2009/08/ 27/technology/27compute.html.

McBride S (2005) Zero day attack imminent. Computerworld (February). http://www.computerworld.com.au/article/1535/ zero\_day\_attack\_imminent/.

Mell P, Grance T (2011) The NIST definition of cloud computing. Computer Security Division, Information Technology Laboratory, National Institute of Standards and Technology, U.S. Department of Commerce. http://csrc.nist.gov/publications/nistpubs/800 -145/SP800-145.pdf.

Messmer E (2013) Identity-theft vulnerability fixed in Microsoft Office 365, says security firm. NetworkWorld (December). http://www.networkworld.com/article/2172555/network -security/identity-theft-vulnerability-fixed-in-microsoft-office -365–says-security-firm.html.

Microsoft (2013) Security in Office 365. White paper, http://www .microsoft.com/en-us/download/details.aspx?id=26552.

Moore D, Shannon C, Brown J (2002) Code-Red: A case study on the spread and victims of an Internet worm. Proc. Second ACM SIGCOMM Internet Measurement Workshop, Marseille, France, 273–284.

Muller HM (2000) Asymptotic efficiency in dynamic principal-agent problems. J. Econom. Theory 91(2):292–301.

Neti S, Somayaji A, Locasto ME (2012) Software diversity: Security, entropy and game theory. Proc. 7th USENIX Conf. Hot Topics Security, HotSec’12 (USENIX Association, Bellevue, WA), 5.

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: Implications for the software industry. Inform. Systems Res. 25(1):173–199.

Nochenson A, Grossklags J, Heimann CFL (2014) How loss profiles reveal behavioral biases in interdependent security decisions. Internat. J. Internet Tech. Secured Trans. Forthcoming.

O’Neill S (2011) Survey: Value of the cloud, telecommuting overstated. CIO (September). http://www.cio.com/article/2404707/ cloud-computing/survey–value-of-the-cloud–telecommuting -overstated.html.

Pesendorfer W, Swinkels JM (2000) Efficiency and information aggregation in auctions. Amer. Econom. Rev. 90(3):499–525.

Png IPL, Wang Q-H (2009) Information security: Facilitating user precautions vis-à-vis enforcement against attackers. J. Management Inform. Systems 26(2):97–121.

Ransbotham S, Mitra S, Ramsey J (2012) Are markets for vulnerabilities effective? MIS Quart. 36(1):43–64.

Robertson J (2014) Heartbleed fixes taking longer as websites plug gaps. Bloomberg.com (April). http://www.bloomberg.com/news/ 2014-04-14/heartbleed-fixes-taking-longer-as-websites-plug -gaps.html.

Roy D (2011) Data on sale. CIO.in 6(10):60–61.

Schneider FB, Birman KP (2009) The monoculture risk put into context. IEEE Security Privacy 7(1):14–17.

Vereshchagina G, Hopenhayn HA (2009) Risk taking by entrepreneurs. Amer. Econom. Rev. 99(5):1808–1830.

Villeneuve N (2011) Trends in targeted attacks. White paper. Trend Micro (October). http://www.trendmicro.com/cloud-content/ us/pdfs/security-intelligence/white-papers/wp\_trends-in -targeted-attacks.pdf.

Weatherwax E, Knight J, Nguyen-Tuong A (2009) A model of secretless security in N -variant systems. Proc. 39th Annual IEEE/IFIP Internat. Conf. Dependable Systems Networks, DSN’09 (IEEE Computer Soc., Washington, DC).

Wei X, Nault BR (2011) Vertically differentiated information goods: Monopoly power through versioning. Working paper, Fudan University and University of Calgary.

Wei X, Nault BR (2014) Monopoly versioning of information goods when consumers have group tastes. Production Oper. Management. 23(6):1067–1081.

Xu J, Kalbarczyk Z, Iyer RK (2003) Transparent runtime randomization for security. Proc. 22nd Sympos. Reliable Distributed Systems (SRDS 2003), SRDS 03 (IEEE Computer Soc., Washington, DC), 260–269.

Zhang JJ, Seidmann A (2010) Perpetual versus subscription licensing under quality uncertainty and network externality effects. J. Management Inform. Systems 27(1):39–68.
