---
otero_id: 15502
otero_key: "QHD2UJDW"
title: "Cloud Services vs. On-Premises Software: Competition Under Security Risk and Product Customization"
authors: "Zan Zhang; Guofang Nan; Yong Tan"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0919"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/QHD2UJDW/fulltext/images/42985695298041f7ce05b73dd343ce223a42492363e3fdd40b71ece42913c5f7.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Cloud Services vs. On-Premises Software: Competition Under Security Risk and Product Customization

Zan Zhang, Guofang Nan\*, Yong Tan

Zan Zhang, Guofang Nan\*, Yong Tan (2020) Cloud Services vs. On-Premises Software: Competition Under Security Risk and Product Customization. Information Systems Research

Published online in Articles in Advance 15 Jun 2020

https://doi.org/10.1287/isre.2019.0919

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Cloud Services vs. On-Premises Software: Competition Under Security Risk and Product Customization

Zan Zhang,<sup>a</sup> Guofang Nan,<sup>b,</sup>\* Yong Tan<sup>c</sup>

<sup>a</sup> School of Economics and Management, Beihang University, Beijing 100191, China; <sup>b</sup> College of Management and Economics, Tianjin University, Tianjin 300072, China; <sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195 \*Corresponding author

Contact: zanzhang@buaa.edu.cn, https://orcid.org/0000-0002-4911-1620 (ZZ); gfnan@tju.edu.cn, https://orcid.org/0000-0002-4911-1620 (GN); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT)

Received: October 7, 2016 Revised: September 30, 2017; November 1, 2018; May 1, 2019; October 9, 2019 Accepted: December 1, 2019 Published Online in Articles in Advance: June 15, 2020

https://doi.org/10.1287/isre.2019.0919

Copyright: © 2020 INFORMS

Abstract. Cloud computing services are transforming business and government at an ever-increasing rate. The associated security risk and low customization capability, however, create challenges for the adoption of cloud services. In this paper, we construct a game-theoretical model that involves two vendors—one that provides cloud service on a pay-per-use basis and the other that sells on-premises software at a one-time licensing fee—and consumers who are heterogeneous in their usage frequencies in an environment in which negative security externalities are present. We study the competitive implications of security risk and product customization capability on consumer purchase choice and vendors’ pricing and investment strategies. Although it is generally believed that cloud services are more vulnerable to security breaches, our results demonstrate that in high security-loss environments in which consumers incur a large loss per use if struck by attacks, using cloud service yields a lower average expected loss for consumers compared with on-premises software. By endogenizing vendors’ investment decisions on security and customization, our investigation highlights that in low-security-loss environments, the cloud vendor has no incentive to invest effort in reducing security risk, but the on-premises vendor will increase security investment when the probability of attacks on its product becomes higher. We also find that the on-premises vendor’s security and customization investments act as strategic substitutes in low-security-loss environments and, under certain conditions, complements in high-security-loss environments. We further examine welfare-maximizing security investments and find that the socially optimal investment requires greater effort to improve cloud security in low-security-loss environments and to improve on-premises software security in high-security-loss environments.

History: Saby Mitra, Senior Editor; Amit Mehra, Associate Editor. Funding: Financial support from the National Science Foundation of China [Grants 71471128, 71631003, and 71729001] is gratefully acknowledged. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0919.

Keywords: cloud security • software as a service • network economics • competitive strategies • investment decisions

## 1. Introduction

For at least a decade, there has been a tremendous increase in the implementation of cloud computing services. Cloud services are gaining popularity across a variety of industries for use with basic business support functions. According to research conducted by Forrester, the worldwide cloud computing market is anticipated to grow to \$191 billion by 2020, up from \$72 billion in 2014 (King 2014). Information technology (IT) spending is undergoing a shift from traditional sources, such as direct server and software license purchases, to cloud services. The shift in IT spending will continue, with Gartner’s predicting the transfer to hit \$1 trillion over the next several years (Babcock 2016).

Cloud computing is leveraged in a variety of service models—infrastructure as a service, platform as a service, and software as a service (SaaS). An International Data Corporation (IDC) report predicts that SaaS will remain the dominant model of cloud services, capturing more than half of all public cloud spending over the 2019–2023 period (IDC 2019). Under the payas-you-go pricing structure, cloud users pay only for the actual volume of resources consumed rather than a flat rate for a bundle of services that may not be fully used. Because of the on-demand feature and flexible pay-as-you-go mechanism, cloud services dramatically reduce the up-front IT expenses that may deter many clients from implementing on-premises software. In this paper, we concentrate on the SaaS business model of cloud services, which emerges as an alternative to traditional on-premises model and has become the most deployed cloud model for a wide range of collaborative and business applications. We compare the SaaS model with the on-premises model in a competitive environment in which negative security externalities are present.

For all their benefits, cloud services are not without their challenges. The primary concern about cloudbased solutions is security risks. The shared nature of cloud services introduces the possibility of new security breaches that can erase any gains made by the shift to the cloud. Consumers who move data to the cloud lose the ability to have physical access to the servers that host their information. Thus, potentially sensitive data are at risk for attack on the cloud vendors’ network. One example of cloud service vendors being compromised is Code Spaces, a former SaaS vendor that offered project management services. On June 17, 2014, a hacker accessed the company via the Amazon Elastic Compute Cloud control panel and later deleted data, backups, and machine configurations after Code Spaces refused to pay the large fee demanded to stop the attack (Constantin 2014). A recent example is the case of attacks on Microsoft Office 365. Variants of Cerber ransomware attacked Office 365 email users on June 22, 2016, and hit approximately 57% of organizations that use Office 365 (Landewe 2016).

In a multitenant cloud architecture in which numerous unrelated users are hosted on the same server, hackers can theoretically gain control of huge stores of information through a single attack (Sarno and Rodriguez 2011). With more users moving to the cloud and thereby storing more data on the same server, cloud vendors become more attractive targets to hackers than the majority of local single-user data centers. A Netskope study finds that the growing use of cloud services and the increase in storage of sensitive information lead to more security attacks in the cloud (Seals 2016). In addition to security risks, the multitenancy nature of cloud services makes it virtually impossible for vendors to maintain every piece of customization code tenant by tenant (Sun et al. 2008). Consumers who implement cloud-based solutions have very limited options for customization (Schneier 2015). Note that customization differs from configuration because the former involves sourcecode changes to create functionality that is beyond the configuration limit, whereas the latter does not. Although cloud services offer a considerable number of choices and many configuration options, they are limited in what users can do and may not support all the options required by users. They generally have to accept the product as provided and bear misfit costs for using a not-fully-customized product. A survey conducted by IDC shows that not having enough ability to customize is one of the significant challenges that cloud services face (Karanikas 2013).

The customization issue is less severe for onpremises software because the vendors can invest effort in offering a product with a higher customization capability. Although cloud services may be perceived as more vulnerable to cyberattack, on-premises software is not free from security risks in network environments. As its market coverage grows, on-premises software suffers from increased security risks because more customers would again increase the incentives of hackers who are incentivized by financial and political motivations. Attacks on local on-premises software generally occur because of the exploitable weaknesses and vulnerabilities in the product. Though vendor-supplied updates and patches are often made available to users before an attack occurs, studies show that even critical applications are often missed through either limited resources or lack of awareness. The 2017 Verizon Data Breach Investigations Report notes that 99.9% of the exploited vulnerabilities had been compromised more than a year after the associated common vulnerabilities and exposures were published (Verizon 2017).

In this paper, we examine software competition in the presence of security externalities that are endogenously determined by consumption choices. We focus on the competitive implications of security risks and product customization. In particular, we seek to answer the following research questions. First, how do the security risks affect consumer purchase behavior and vendor pricing? Are cloud services less secure than on-premises software? Second, what are the optimal levels of security and customization investments for vendors? How does security investment interact with customization investment? Third and finally, what are the socially optimal levels of security investment in the two products?

To address these questions, we develop a model in which two vendors, one offering cloud service under the pay-as-you-go pricing model and the other selling on-premises software under the perpetual licensing model, compete to serve a market of consumers who are heterogeneous in their usage frequencies. The products are exposed to higher security risks as the market coverage increases because of the security externalities. Consumers, if struck by attacks, incur economic losses that increase with their usage frequencies. We model the competition as a two-stage game in which the vendors decide the levels of investment in product security and customization in stage 1 and prices in stage 2. We investigate the implications of security risks and product customization in high- and low-security-loss environments. In highsecurity-loss environments, consumers incur large economic losses from being attacked. A good example is enterprise software, such as enterprise resourceplanning systems, customer relationship-management software, and accounting software. If hit by attacks, the businesses that use the enterprise systems are usually subject to substantial losses associated with loss of business, reputation, and sensitive information. In low-security-loss environments, consumers are subject to small economic losses. Examples include media player software, game applications, and productivity software. According to IBM’s 2019 Cost of a Data Breach Report, the global average cost of a security breach for companies is \$3.92 million in 2019 (IBM Security 2019). Healthcare companies have the highest costs, at \$6.45 million, which is 65% higher than average, followed by financial services companies at \$5.86 million and energy companies at \$5.60 million, whereas the companies in industries such as media, hospitality, and retail have lower costs, at about \$2 million.

Our analysis provides several interesting findings. Although cloud services are generally believed to be less secure than on-premises software, our results show that in high-security-loss environments, consumers incur a lower average expected loss from using cloud service than from using on-premises software because of the accompanying security externalities associated with product consumption One counterintuitive finding is that a decline in the probability of attacks on the cloud service reduces the cloud vendor’s profit by lowering its price in lowsecurity-loss environments, implying that the profitmaximizing cloud vendor may not always be incentivized to invest effort to improve cloud security. In contrast to the cloud vendor’s investment decision, the on-premises vendor will offer a more secure product or a product of higher customization capability when the probability of attacks on the onpremises software becomes higher. This result follows from the fact that a higher probability of attacks intensifies the marginal impact of security and customization investments on the on-premises vendor’s profit. Our results also show an increasing security effort invested by one vendor when the probability of attacks on the other vendor’s product increases. By examining the interaction between the on-premises vendor’s customization and security investments, our research finds that the two decision variables act as strategic substitutes in low-security-loss environments because increasing security investment reduces the marginal value of customization investment and vice versa. The two variables, however, can be complementary in high-security-loss environments if the probability of attacks on the on-premises software is high enough relative to the probability of attacks on the cloud service. Our analysis also finds that if the products are subject to the same level of attacks, the socially optimal level of security investment is higher for the cloud service in low-security-loss environments and for the on-premises software in high-security loss environments.

The rest of the paper is organized as follows. Section 2 provides a review of the related literature. Section 3 presents our model setup. The equilibrium results and analyses are discussed in Section 4. Section 5 concludes the paper with managerial implications and directions for future work.

## 2. Literature Review

Our paper is closely related to the literature on software security. August and Tunca (2006) analyze how patching rebates, mandates, and usage taxes can improve software security. They demonstrate that when the security risk and patching costs are high, a patching rebate dominates the other two policies. Building on the approach in August and Tunca (2006), August and Tunca (2011) investigate how security liability policies can be used to increase software security. Kim et al. (2011) study the impact of liability on a vendor’s decision in regard to software security quality and show that liability can lead to better se curity quality when consumers incur different levels of loss. Taking into account the benefits and costs of a diversification strategy, Chen et al. (2011) identify the conditions under which the diversification strategy alleviates security loss faced by a firm. Hui et al. (2013) investigate how the equilibrium behaviors of a se curity service vendor and its customers are affected by system interdependency risks and mandatory security requirements. One underlying assumption in these studies is that consumers’ losses caused by security breaches are not affected by the purchase behaviors of other individual users. In empirical research on software security, Mitra and Ransbotham (2015) analyze the effects of full and limited disclosures of vulnerability information on the diffusion of attacks and find that full disclosure accelerates the diffusion of attacks. Our paper contributes to this stream of literature by formally examining the security investment strategies of two software vendors in the presence of security externalities. Consumers incur different levels of losses associated with security attacks depending on the population of users who consume the same product, as well as their actua usage frequencies; that is, consumers with high usage frequencies are subject to higher security losses than those with low usage frequencies.

In the literature on software security, our paper is closest to that of August et al. (2014), because we both address security risk issues related to SaaS and onpremises software products from an economic perspective. August et al. (2014) concentrate on security diversification through versioning to explore the impacts of software diversity and version-specific security risks on market structure and vendor profit.

Our work differs from that of August et al. (2014) in several aspects. First, August et al. (2014) consider security issues in a monopoly setting in which a software vendor decides whether and how to version its product. By contrast, we consider security issues in a competitive setting in which one vendor sells onpremises software under a perpetual licensing model and the other vendor offers SaaS under the pay-asyou-go model. Second, August et al. (2014) quantify the risk-diversification benefits of versioning, whereas we investigate the strategic implications of competition in the product market on vendors’ security investment effort. Third, August et al. (2014) extend the baseline model to examine the interaction between the versioning decision and security investment. The goal of our research is to determine the vendors’ optimal investments in software security and customization and to explore how the market characteristics affect their decisions on product investment. By endogenizing vendors’ investment decisions, we can achieve a better understanding of how the competition influences consumers’ expected security losses and vendors’ effort in reducing security risks. In this aspect, our research is related to studies on investment in security and software vulnerability disclosure (e.g., Kannan and Telang 2005, Arora et al. 2008, Dey et al. 2014, Lee et al. 2016).

Our work adds to the research on SaaS. Choudhary (2007) shows that, in most cases, a software vendor invests more in product development under the SaaS model than under the perpetual licensing model. Fan et al. (2009) consider an SaaS vendor’s service operation costs and quality improvement and show that service costs may significantly affect an SaaS vendor’s competitiveness. Ma and Seidmann (2015) study competitive dynamics by examining users’ capacity management problems. Guo and Ma (2017) argue that an SaaS vendor’s competitiveness depends on its quality-improvement rate and the network effects. Most of these studies focus on SaaS subscriptionbased pricing and analyze the implications of SaaS quality improvement. Other interesting papers that consider the SaaS model include Chen and Wu (2013), Niculescu and Wu (2014), and Choudhary and Zhang (2015). Although the literature has examined various aspects of the SaaS model, limited work on the economic aspects of the SaaS model has investigated the inherent security risks. Our paper contributes to this stream of literature by examining the impact of security risks that stem from consumer behavior on the competition between SaaS and on-premises software. We compare the two products by allowing them to use different pricing schemes. We model heterogeneity among customers by having some customers who prefer the cloud vendor’s pay-as-you-go model and others who favor the on-premises vendor’s perpetual licensing model. In addition to the security risks and pricing scheme that differentiate the two vendors, we consider the on-premises vendor’s competitive advantage in product customization. To better understand how security issues affect the vendors’ investment decisions, we simplify the structure of cloud service and on-premises software and formulate a succinct model that abstracts away from product upgrade improvement and multiperiod pricing. This allows us to focus on the competitive implications of product customization and security risks.

Our work is also related to the literature on the leasing and selling of information goods. Many studies in this stream of literature have examined optimal pricing mechanisms, such as selling, subscription-based pricing, and differential pricing in a monopoly setting. Choudhary et al. (1998) analyze a software firm’s pricing choice of leasing and selling and find that renting is more profitable than selling Sundararajan (2004) studies fixed-fee and pay-peruse pricing for a monopoly and demonstrates that a mix of the two pricing schemes always improves profit. Balasubramanian et al. (2015) are among the few who analyze firms’ choice of pricing mechanisms in a competitive market. Our work differs in that we examine the competition between leasing and selling, concentrating on the characteristics of competition itself rather than on the vendors’ endogenous choice of pricing schemes.

## 3. Model

Consider a market with two vendors that offer differentiated products to consumers. Vendor L sells on premises software at a one-time perpetual license fee $p _ { L } ,$ , and vendor R offers cloud service remotely by charging a pay-per-use fee $p _ { R }$ that allows users to pay as they go (we use L/R to signify local/remote). We assume the marginal cost of reproduction to be zero. Vendor R incurs a marginal cost per transaction of serving each user, denoted by c. Consumers derive a utility-per-use u from consuming a product. Consumers are heterogeneous in their usage frequencies θ, which are distributed uniformly over 0,θ<sup>¯</sup> . Without loss of generality, we set θ<sup>¯</sup> 1. We normalize the total consumer mass to 1. The vendors know only the distribution but not the usage frequency of a particular consumer.

Consumers incur a misfit cost for using a product that does not perfectly meet their requirements. Because consumers experience misfit each time they use a product, the higher a consumer’s usage frequency, the higher is the misfit cost that the consumer incurs We denote θτ as the misfit cost borne by consumers with usage frequency θ, where τ measures the disutility per use caused by the misfit. In contrast to the cloud service’s limited options for customization, the on-premises vendor can provide a well-customized software product, which helps to lower consumers misfit costs. Let $\beta \in [ 0 , 1 ]$ denote the customization capability of the on-premises software. A large value of $\beta$ means a low misfit cost. The misfit cost that the consumer with usage frequency θ incurs for using the on-premises software of customization capability $\beta$ is $( { \bar { 1 } } - \beta ) \tau \theta$ . If $\beta = 1$ , the on-premises software fully meets users’ needs, and the users incur no misfit cost.

![](/api/attachments/QHD2UJDW/fulltext/images/904eb54c02831510f01b59c4db4e7b169bea8b6cbd369160c9bcf63ec958c9ca.jpg)  
Figure 1. Model Time Line

Consumers are also exposed to security risks that arise from attacks. Following August and Tunca (2006) and Greenemeier and Hoover (2007), we model these security risks with negative network externalities. Let $\varpi _ { i }$ be the probability of attacks occurring on product i $( i = L , \bar { R } )$ . Here $\varpi _ { L }$ and $\varpi _ { R }$ are assumed to be independent. We denote $\varpi _ { i } N _ { i }$ as the total probability of product i that has a proportion of users $N _ { i }$ being attacked. An interpretation of $\varpi _ { i } N _ { i }$ is the value that consumers of product i attach to the security externalities when the proportion of users is $N _ { i } .$ . If struck by security attacks, consumers incur economic losses that include data loss and potential loss of business, reputation, and trust. Let the parameter α specify the magnitude of consumers’ loss per use. The total loss that a consumer with usage frequency θ incurs from being attacked is denoted by θα; that is, consumers with high usage frequencies incur higher losses than those with low usage frequencies. The expected security loss borne by a consumer with usage frequency θ is then defined by $\theta \alpha \varpi _ { i } N _ { i } \ ( i = L , R )$ , which increases with the number of consumers who use the same product. This implies that consumers impose negative externalities on other individual users by increasing their expected security losses. Because of the security externalities, a consumer’s purchase decision affects the payoffs of other consumers through security losses.

## 3.1. Consumer Utility

A consumer with usage frequency θ experiences utility $U _ { L } = \theta u - p _ { L } - ( \bar { 1 - \beta } ) \tau \bar { \theta - } \theta \alpha \varpi _ { L } N _ { L }$ from buying vendor L’s on-premises software and $U _ { R } =$ $\theta ( u - p _ { R } ) - \tau \theta - \theta \alpha \varpi _ { R } N _ { R }$ from buying vendor R’s cloud service. This consumer prefers vendor L’s onpremises software over vendor R’s cloud service only if the incentive compatibility constraint $U _ { L } > U _ { R }$ is satisfied. Let $\theta _ { 1 }$ be the usage frequency of the marginal consumer who is indifferent between buying the two products. The consumers with usage frequencies

Stage 1 Vendor L decides the levels of product customization and security investments. Vendor R decides the level of cloud security investment.

higher than $\theta _ { 1 }$ buy the on-premises software as long as the individual rationality constraint $U _ { L } > 0$ is satisfied, and the consumers with usage frequencies lower than $\theta _ { 1 }$ pay for the cloud service based on their actual usage if $\dot { U _ { R } } \ge 0$ or abstain from the market if $U _ { R } < 0$

## 3.2. Vendors’ Customization and Security Investments

By investing in product customization, vendor L improves the customization capability of its on-premises software, thus reducing consumers’ misfit costs. Specifically, an investment of $\beta$ in customization yields a misfit cost reduction from τ to $( 1 - \beta ) \tau$ . The cost associated with customization investment is denoted by $G ( \beta )$ . Both vendors can invest to reduce the security risks associated with their offerings. To reduce the probability of security attacks from ϖ<sub>i</sub> to $\varpi _ { i } ( 1 - e _ { i } )$ a vendor must invest effort $C ( e _ { i } )$ , where $e _ { i } \in [ 0 , 1 ]$ . We assume that the cost functions $G ( \beta )$ and C<sub>(</sub>e<sub>i)</sub> are convex functions of $\beta$ and $e _ { i } ,$ respectively, $G ( 0 ) = 0 ,$ and $C ( 0 ) = 0$ . Similar to Laffont and Tirole (1993) and August et al. (2014), we assume that there exist constants $K _ { 1 }$ and $K _ { 2 }$ such that $C ^ { \prime \prime } ( e _ { i } ) > K _ { 1 }$ and $G ^ { ' \prime } ( \beta ) > K _ { 2 }$ . This cost structure assumption reflects the reality that it is extremely difficult to reduce the security risk to zero and to improve product custom ization capability to a level high enough that consumers’ needs are satisfied perfectly.

## 3.3. Timing of the Model

The timeline of this three-stage game is as follows. In stage 1, vendor L decides the levels of investments in software customization $\beta$ and security $e _ { L } ,$ , and vendor R decides the level of investment in cloud security $e _ { R } .$ In stage 2, after observing the first-stage investment decisions, vendor L sets a selling price $p _ { L } ,$ , and vendor R sets a pay-per-use fee $p _ { R } .$ . In stage $^ { 3 , }$ consumers make their purchase decisions. Figure 1 shows the timeline. Table 1 summarizes the notation used in the model.

## 4. Equilibrium Analysis

Consumers with low usage frequencies choose vendor R’s cloud service, and consumers with high usage frequencies purchase vendor $\mathrm { L } ^ { \prime } \mathrm { s }$ on-premises software (because $\partial U _ { L } ( \theta ) / \partial \theta > \partial U _ { R } ( \theta ) / \partial \theta )$ . The marginal consumer’s usage frequency $\theta _ { 1 }$ is obtained by solving $U _ { L } ( \theta _ { 1 } ) = U _ { R } \bar { ( } \theta _ { 1 } )$ . In equilibrium, vendor R serves

The vendors observe the firststage results of the game and simultaneously set their prices

Consumers observe the investment efforts and prices and then make purchase decisions.

Table 1. Notation

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\theta$ </td><td>Consumer usage frequency and  $\theta \sim U[0,1]$ </td></tr><tr><td> $u$ </td><td>Consumers&#x27; utility peruse</td></tr><tr><td> $\tau$ </td><td>Disutility per use caused by misfit</td></tr><tr><td> $\beta$ </td><td>Customization capability of the on-premises software</td></tr><tr><td> $c$ </td><td>Marginal service cost of the cloud vendor</td></tr><tr><td> $p_{L}$ </td><td>One-time fixed price of the on-premises software</td></tr><tr><td> $p_{R}$ </td><td>Pay-per-use fee of the cloud service</td></tr><tr><td> $\varpi_{i}$ </td><td>Probability that an attack occurs on product  $i (i = L,R)$ </td></tr><tr><td> $\alpha$ </td><td>Consumers&#x27; loss per use associated with security attacks</td></tr><tr><td> $N_{i}$ </td><td>Proportion of users of product  $i (i = L,R)$ </td></tr><tr><td> $e_{i}$ </td><td>Security effort invested by vendor  $i (i = L,R)$ </td></tr><tr><td> $C(e_{i})$ </td><td>Cost associated with security investment by vendor  $i (i = L,R)$ </td></tr><tr><td> $G(\beta)$ </td><td>Cost associated with vendor L&#x27;s customization investment</td></tr><tr><td> $\pi_{i}$ </td><td>Profit of vendor  $i (i = L,R)$ </td></tr></table>

consumers with usage frequencies in $[ 0 , \theta _ { 1 } ] ,$ , and vendor L serves consumers with usage frequencies in $[ \theta _ { 1 } , 1 ]$ The vendors maximize profit by choosing prices and investment effort. The profit functions for vendors L and R are given by

$$
\pi_ {L} (p _ {L}, \beta , e _ {L}) = p _ {L} (1 - \theta_ {1}) - G (\beta) - C (e _ {L}),\tag{1}
$$

$$
\pi_ {R} \left(p _ {R}, e _ {R}\right) = \int_ {0} ^ {\theta_ {1}} \left(p _ {R} - c\right) x \mathrm{d} x - C (e _ {R}).\tag{2}
$$

We use backward induction to solve the game, first by solving for the second-stage prices $p _ { L }$ and $p _ { R } , { \mathrm { g i v e n } }$ consumers’ purchase decisions in stage $^ { 3 , }$ and then for the first-stage investment levels $e _ { L } , \ e _ { R }$ , and $\beta ,$ conditional on the second-stage solutions. Following Kreps (1977) and Katz and Shapiro (1985), we employ the concept of fulfilled expectation equilibrium in which the actual network size is equal to the network’s expected size. Consumers base their purchase decisions on the expected network size. In equilibrium, consumers’ expectations of network size are fulfilled.

## 4.1. Second-Stage Analysis

4.1.1. Second-Stage Prices. Solving the game backward, we first derive the equilibrium prices and market shares in stage 2. Lemma 1 presents the secondstage equilibria in high-security-loss environments in which consumers incur large losses if struck by attacks $( \mathrm { i . e . , } \alpha$ is large) and in low-security-loss environments in which consumers are subject to small losses $( \mathrm { i . e . , }$ α is small). Because of the complexity of our model, it is intractable to derive the exact closedform expressions for the market outcomes. Thus, we use asymptotic analysis, which has been used in many studies (Laffont and Tirole 1988; Chesher 1989; MacLeod and Malcomson 1993; Muller 2000; August and Tunca 2006, 2011; August et al. 2014; Gabaix et al. 2016), to examine the market equilibrium in high- and low-security-loss environments. The asymptotic $\mathsf { a p - }$ proximations allow suppression of unimportant details without loss of mathematical rigor or precise results. Hereafter, for all lemma and proposition statements that cover high- (low-)security-loss environments, there exists $\underline { { \alpha } } \ \left( \bar { \alpha } \right)$ such that for all $\alpha > \underline { { { \alpha } } } \ ( \alpha < \bar { \alpha } )$ , the statements that cover high- (low-)security-loss environments hold. Technically, $\underline { { \alpha } } = \operatorname* { m a x } \{ \alpha _ { 1 } , \alpha _ { 2 } \}$ and $\bar { \alpha } =$ min $\{ \alpha _ { 1 } , \alpha _ { 2 } \}$ , where

$$
\begin{array}{r} \alpha_ {1} = \left(\varpi_ {L} (\beta \tau + p _ {R}) + 2 p _ {L} (\varpi_ {L} + \varpi_ {R}) \right. \\ \left. + 2 \sqrt {p _ {L} \varpi_ {L} (\varpi_ {L} + \varpi_ {R}) (\beta \tau + p _ {R}) + p _ {L} ^ {2} (\varpi_ {L} + \varpi_ {R}) ^ {2}}\right) / \varpi_ {L} ^ {2} \end{array}
$$

and $\alpha _ { 2 } = ( \beta \tau + p _ { R } ) / \varpi _ { L }$ . Because the closed-form expressions for $\underline { { \alpha } }$ and α¯ are difficult to obtain, we use numerical examples to illustrate the variations of $\underline { { \alpha } }$ and α¯ with respect to ϖ $( \varpi _ { L } = \varpi _ { R } = \varpi$ in this example). Figure $2 \bar { ( \mathsf { a } ) }$ shows that in high-security-loss environments, $\underline { { \alpha } }$ decreases with an increase in ϖ. When ϖ is very small, α declines rapidly with ϖ, and when ϖ becomes larger, α decreases slowly with it. The variation of $\bar { \alpha }$ in low-security-loss environments (see Figure 2(b)) is similar to that of $\underline { { \alpha } }$ in high-securityloss environments. Thus, there exists a wide range of α values for high-security-loss environments when ϖ is not too small and for low-security-loss environments when ϖ is small. This result is robust to different values of $\varpi _ { L }$ and $\varpi _ { R }$ and robust to a wide range of other parameter values.

Lemma 1. The second-stage market equilibrium exhibits the following properties:

a. For high-security-loss environments, the equilibrium prices and corresponding indifferent point are given by

$$
\begin{array}{r l} & p _ {L} ^ {*} = \frac {\varpi_ {L} (u - \tau + \tau \beta)}{\varpi_ {L} + \varpi_ {R}} - \frac {\alpha \varpi_ {L} ^ {2} \varpi_ {R}}{(\varpi_ {L} + \varpi_ {R}) ^ {2}}, \\ & p _ {R} ^ {*} = u - \tau - \frac {\alpha \varpi_ {L} \varpi_ {R}}{\varpi_ {L} + \varpi_ {R}}, a n d \\ & \theta_ {1} ^ {*} = \frac {\varpi_ {L}}{\varpi_ {L} + \varpi_ {R}}. \end{array}
$$

b. For low-security-loss environments, the equilibrium prices and corresponding indifferent point are given b

$$
\begin{array}{r l} & p _ {L} ^ {*} = \beta \tau + c + \frac {1}{8} \alpha (7 \varpi_ {R} - \varpi_ {L}) \\ & \qquad + \frac {\alpha^ {2} (\varpi_ {L} + 5 \varpi_ {R}) (1 1 \varpi_ {R} - 3 \varpi_ {L})}{3 2 (\beta \tau + c)} + O (\alpha^ {3}), \\ & p _ {R} ^ {*} = \beta \tau + 2 c + \alpha \varpi_ {R} + \frac {\alpha^ {2} (1 7 \varpi_ {R} ^ {2} - \varpi_ {L} ^ {2})}{8 (\beta \tau + c)} \\ & \qquad + O (\alpha^ {3}), a n d \\ & \theta_ {1} ^ {*} = \frac {1}{2} + \frac {\alpha (\varpi_ {L} + 5 \varpi_ {R})}{1 6 (\beta \tau + c)} \\ & \qquad + \frac {\alpha^ {2} (6 8 \varpi_ {L} \varpi_ {R} + 4 1 \varpi_ {R} ^ {2} - 3 \varpi_ {L} ^ {2})}{6 4 (\beta \tau + c) ^ {2}} + O (\alpha^ {3}). \end{array}
$$

Figure 2. Variations of α and α¯  
![](/api/attachments/QHD2UJDW/fulltext/images/d22eefa4355c313268b91050e6d6d82f20e5ee75349401f8e433fa3b17c86964.jpg)  
Note. $u = 5 ,$ , τ 1, $\beta = 0 . 2 ,$ , and $c = 0 . 2 .$

Proofs of all lemmas and propositions are presented in the online appendix.

Lemma 1 summarizes the market outcomes when the vendors engage solely in price competition. In high-security-loss environments, the two vendors coexist but do not compete directly with each other. Their market shares are determined by the probabilities of security attacks. The underlying rationale for this result is as follows: when faced with a very large economic loss associated with attacks, consumers care more about product security than about product customization capability, so the probabilities of attacks play a critical role in consumers’ purchase decisions. In such a case, all the consumers with usage frequencies lower than $\varpi _ { L } / ( \varpi _ { L } + \varpi _ { R } )$ will buy from the cloud vendor if their utilities from buying the cloud service are nonnegative. This enables the cloud vendor to price high enough to capture all consumer surplus without reducing its user population. This result is similar to that in Balasubramanian et al. (2015), which shows that when the consumers who pay a pay-per-use price incur a sufficiently high psychological cost, the pay-per-use provider sets the maximum price that it can charge, leaving its customers with no surplus. In another work that examines the competition between the usage-based and fixed-fee pricing schemes, Ma and Seidmann (2015) find that under certain conditions, the provider who uses the pay-as-you-go pricing would extract all consumer surplus at the equilibrium price. In lowsecurity-loss environments, our analysis reveals that the customization capability of the on-premises software mitigates price competition between the vendors.

Figures 3 and 4 illustrate the changes of profits and prices with respect to the probabilities of attacks $\varpi _ { L }$ and $\varpi _ { R }$ in high-security-loss environments. Figure $3 ( \mathrm { a } )$ shows that for a given $\varpi _ { R }$ , the on-premises vendor’s profit decreases with the probability of at tacks on its product $\varpi _ { L }$ . When $\varpi _ { L }$ and $\varpi _ { R }$ are very small, the on-premises vendor gains a very high profit. Although the on-premises vendor’s price increases in $\varpi _ { L }$ when $\varpi _ { R }$ is small (see Figure $4 ( \mathsf { a } ) )$ , the increased price is insufficient to make up for the decreased market share, resulting in a reduction in the vendor’s profit. Figure 3(b) shows that for a given $\varpi _ { L }$ the cloud vendor’s profit declines as the probability of attacks on the cloud service $\varpi _ { R }$ increases because the increased probability of attacks causes the cloud vendor to respond by cutting price, as illustrated in Figure 4(b).

![](/api/attachments/QHD2UJDW/fulltext/images/4d5561506f2a58953a94c7cf085004af4cb3e6a201974f51427fd88ca7da4e8d.jpg)

4.1.2. Average Expected Loss. With the equilibrium results in Lemma 1, we can examine consumers’ average expected loss. The average expected loss borne by on-premises users, denoted $A S L _ { L } ,$ and the average expected loss borne by cloud users, denoted $A S L _ { R } ,$ , are expressed as follows:

$$
A S L _ {L} = \frac {\int_ {\theta_ {1} ^ {*}} ^ {1} x \varpi_ {L} \alpha (1 - \theta_ {1} ^ {*}) \mathrm{d} x}{1 - \theta_ {1} ^ {*}} = \frac {1}{2} \varpi_ {L} \alpha (1 - \theta_ {1} ^ {* 2}),\tag{3}
$$

$$
A S L _ {R} = \frac {\int_ {0} ^ {\theta_ {1} ^ {*}} x \varpi_ {R} \alpha \theta_ {1} ^ {*} \mathrm{d} x}{\theta_ {1} ^ {*}} = \frac {1}{2} \varpi_ {R} \alpha \theta_ {1} ^ {* 2}.\tag{4}
$$

From Equations (3) and (4), we find that the average expected loss incurred by a consumer is determined by three factors: the expected loss per use $\varpi _ { i } \alpha _ { . }$ , the average usage frequency $( \mathrm { i . e . , } \theta _ { 1 } ^ { \ast } / 2$ for the cloud users and $( 1 + { \theta } _ { 1 } ^ { * } ) / 2$ for the on-premises users), and the market share of vendor $i \left( \mathrm { i . e . , } \theta _ { 1 } ^ { \ast } \right.$ for the cloud vendor and $1 - \theta _ { 1 } ^ { * }$ for the on-premises vendor). Increasing the value of any factor would lead to a higher average expected loss.

Figure 3. (Color online) Profits in High-Security-Loss Environments (a) On-premises vendor's profit  
![](/api/attachments/QHD2UJDW/fulltext/images/ceadc2e2cfc59be28e9e770184e5f2fc9db1c68932a4745a0dad71716b924018.jpg)  
Substituting the expressions of $\boldsymbol { \theta } _ { 1 } ^ { * }$ in Lemma 1 into Equations (3) and (4), we can compare the average expected losses borne by the cloud users and the onpremises users. It is interesting to explore whether the cloud service yields greater average expected loss than the on-premises software. Because the average expected loss reflects the negative externalities that arise from security attacks, we further analyze how the average expected loss changes with the probability of attacks. Intuitively, an increased probability of attacks, on the one hand, directly increases users average expected loss. On the other hand, the increased security risk indirectly reduces the average usage frequency because of the existence of security externalities, which, in turn, lowers the average expected loss. The two opposite impacts point to an interesting comparative statics result, as shown in Proposition 1.

Proposition 1 (Average Expected Loss).

a. In high-security-loss environments, the average expected loss incurred by cloud users is lower than that incurred by on-premises users; the cloud users’ average expected loss increases in $\varpi _ { R }$ when $\varpi _ { R } < \varpi _ { L } ,$ and the onpremises users’ average expected loss increases in $\varpi _ { L }$

b. In low-security-loss environments, when $\varpi _ { R } > 3 \varpi _ { L } ,$ the average expected loss incurred by cloud users is higher than that incurred by on-premises users; the on-premises users’ average expected loss increases in $\varpi _ { L }$ when $\varpi _ { L } <$ $6 ( \beta \tau + c ) / \alpha - 5 \varpi _ { R } / 2 ,$ , and the cloud users’ average $e x \mathrm { - }$ pected loss increases in $\varpi _ { R }$

Because of centralization, cloud services may be perceived as inherently more vulnerable to security breaches. Intuitively, then, the average expected loss would be higher for cloud users than for on-premises

![](/api/attachments/QHD2UJDW/fulltext/images/4dd6b06f9f51bad2db69057ecb5a478cd714ae8de43377134ac4b1a4bdd026ba.jpg)  
users. A counterintuitive finding in Proposition 1 is that in high-security-loss environments, consumers could expect a lower average expected loss from using the cloud service than from using the onpremises software. The result that cloud users may incur a higher average loss in low-security-loss environments can be explained as follows: when $\varpi _ { R }$ increases, the cloud vendor’s market share expands and the on-premises vendor’s shrinks, leading to an increase in the average expected loss for the cloud users and a decrease for the on-premises users because of the negative externalities. When $\varpi _ { R }$ increases to such a degree that it exceeds a threshold, the average expected loss borne by cloud users would be higher than that borne by on-premises users.

Proposition 1 also states that there exists a range of values of attack probability whereby consumers average expected loss declines. This result is an outcome of the accompanying security externalities associated with the consumption of a product. In high-security-loss environments, as $\varpi _ { R }$ increases, the user population of cloud services becomes more limited and, as a result, achieves greater security. Beyond a certain threshold, the negative impact of $\varpi _ { R }$ on cloud users’ average expected loss dominates the positive impact, resulting in a lower average expected loss. The same intuition applies to the reduction of average expected loss borne by on-premises users with $\varpi _ { L }$ in low-security-loss environments.

Although we have compared the average expected loss borne by cloud users with that borne by onpremises users, it remains unclear how the values of average expected loss associated with the two groups of users changes between high- and low-security loss environments. Because consumers are subject to a large loss per use from being attacked in high-securityloss environments, one might think that the average expected loss incurred by consumers in high-securityloss environments would be larger than that in lowsecurity-loss environments. Proposition 2, however, shows that this intuition is not accurate.

Figure 4. (Color online) Prices in High-Security-Loss Environments  
![](/api/attachments/QHD2UJDW/fulltext/images/b77c743d9ef7f1085dfa9187ec93e422f22077bae8aefc43e03d072752bdc2c5.jpg)  
Note. u 5, τ 1, α 25, β 0.2, and c 0.2 (for Figures 3 and 4).

## Proposition 2 (Comparison of Average Expected Losses).

a. For cloud users, when the probability of attacks on the cloud service is large enough, the average expected loss in high-security-loss environments may be lower than that in low-security-loss environments; otherwise, the average expected loss in high-security-loss environments is higher if the on-premises software has a sufficiently high customization capability.

b. For on-premises users, when the probability of attacks on the on-premises software is small enough, the average expected loss in high-security-loss environments is higher than that in low-security-loss environments; otherwise, the average expected loss in high-security-loss environments may be lower if the on-premises software has a sufficiently high customization capability.

Proposition 2 shows that it is likely that low-securityloss environments lead to a higher average expected loss for consumers. Note that when we say the average expected loss incurred in high-security-loss environments may be lower than that in low-security-loss environments, we mean that the maximum value of average expected loss in low-security-loss environments exceeds the minimum value of average expected loss in high-security-loss environments. Figure 5, (a) and (b), depicts, respectively, cloud users’ and on-premises users’ average expected losses in both low- and highsecurity-loss environments. When the cloud service is subject to a high level of attack $\varpi _ { R } ,$ cloud users may suffer a higher average expected loss in low-securityloss environments, as illustrated by the solid line in Figure 5(a). This result could be explained by how $\varpi _ { R }$ affects the average expected loss borne by cloud users. Recall from Proposition 1 that the cloud users average loss in low-security-loss environments monotonically increases in $\varpi _ { R }$ , but their average loss in high-security-loss environments increases only when $\varpi _ { R }$ is small. When $\varpi _ { R }$ increases and becomes large enough, low-security-loss environments lead to a higher average expected loss for cloud users. The dotted and dash-dotted lines in Figure 5(b) show that when the probability of attacks on the on-premises software $\varpi _ { L }$ is very small, on-premises users incur a lower average expected loss in low-security-loss environments than that in high-security-loss environments. When $\varpi _ { L }$ becomes larger, the comparison of average expected loss between high- and low-security-loss environments depends on the level of software customization capability $\beta ,$ as illustrated by the solid and dashed lines in Figure 5(b).

![](/api/attachments/QHD2UJDW/fulltext/images/e481f901abda4b7250f3a3713820491efed84d65a7525c09a14b6f256c6a501b.jpg)

## 4.2. First-Stage Investments in Security and Customization

Conditional on the second-stage equilibrium prices, the on-premises vendor determines the levels of cus tomization and security investments $\beta$ and $e _ { L } ,$ , and the cloud service vendor determines the security investment level $e _ { R }$ . Substituting $\varpi _ { i } ( 1 - e _ { i } )$ for $\varpi _ { i } ( i = L , R )$ into the second-stage prices given in Lemma 1 and subsequently into Equations (1) and (2), we obtain the vendors’ first-stage objective functions. Maximizing the objective functions and solving for $e _ { i }$ and $\beta$ yield the optimal investment levels, as given in Lemma 2. For convenience, the inverse marginal cost function of $G ^ { ' } ( \beta )$ is denoted as $g _ { \beta } \equiv ( G ^ { ' } ( \beta ) ) ^ { - 1 }$

Figure 5. Comparison of Average Expected Losses  
![](/api/attachments/QHD2UJDW/fulltext/images/732b5dabb9c15bb8da9fca37cae1c8bf36c7b6c75a61313ba9e94dd8872d9ec5.jpg)  
Note. $\eta _ { j } \ ( j = 1 , 2 , 3 )$ and $\beta _ { k } \ ( k = 1 , 2 , 3 , 4 )$ are given in the proof in the online appendix.

Lemma 2. Let $\hat { \varpi } _ { i } = \varpi _ { i } ( 1 - e _ { i } ^ { * } )$ for i L, R. Then

a. For low-security-loss environments, the cloud vendor’s optimal level of security investment is $e _ { R } ^ { * } = 0 ,$ , and the on-premises vendor’s optimal levels of security and customization investments $\boldsymbol { e } _ { L } ^ { * }$ and $\boldsymbol { \beta } ^ { * }$ are obtained by solving

$$
\frac {1}{8} \alpha \varpi_ {L} + \frac {\alpha^ {2} \varpi_ {L} (1 5 \varpi_ {R} + 7 \hat {\varpi} _ {L})}{6 4 (\beta^ {*} \tau + c)} + O (\alpha^ {3}) = C ^ {'} (e _ {L} ^ {*}) a n d
$$

$$
\frac {1}{2} \tau + \frac {\alpha^ {2} \tau \left(7 \hat {\varpi} _ {L} ^ {2} + 3 0 \hat {\varpi} _ {L} \varpi_ {R} - 1 8 5 \varpi_ {R} ^ {2}\right)}{1 2 8 \left(\beta^ {*} \tau + c\right) ^ {2}} + O \left(\alpha^ {3}\right) = G ^ {\prime} \left(\beta^ {*}\right).
$$

b. For high-security-loss environments, the on-premises vendor’s optimal level of customization investment is $\begin{array} { r } { \beta ^ { * } = g _ { \beta } ( \frac { \tau \hat { \varpi } _ { L } \hat { \varpi } _ { R } } { ( \hat { \varpi } _ { L } + \hat { \varpi } _ { R } ) ^ { 2 } } ) } \end{array}$ , and the vendors’ optimal levels of security investments $\boldsymbol { e } _ { L } ^ { * }$ and $e _ { R } ^ { * } ,$ , are obtained by solving

$$
\begin{array}{l} \frac {\hat {\varpi} _ {R} ^ {2} \varpi_ {L}}{(\hat {\varpi} _ {L} + \hat {\varpi} _ {R}) ^ {3}} \left((u - \tau + \tau \beta^ {*}) \left(\frac {\hat {\varpi} _ {L}}{\hat {\varpi} _ {R}} - 1\right) - \frac {\alpha \hat {\varpi} _ {L} (\hat {\varpi} _ {L} - 2 \hat {\varpi} _ {R})}{\hat {\varpi} _ {L} + \hat {\varpi} _ {R}}\right) \\ = C ^ {'} (e _ {L} ^ {*}) \end{array}
$$

and

$$
\frac {\hat {\varpi} _ {L} ^ {2} \varpi_ {R}}{(\hat {\varpi} _ {L} + \hat {\varpi} _ {R}) ^ {3}} \left(u - \tau - c + \frac {\alpha \hat {\varpi} _ {L} (\hat {\varpi} _ {L} - 2 \hat {\varpi} _ {R})}{2 (\hat {\varpi} _ {L} + \hat {\varpi} _ {R})}\right) = C ^ {'} (e _ {R} ^ {*}).
$$

Using the result of Lemma 2, we can explore the changes of the cloud vendor’s decision in regard to security investment when the on-premises vendor changes its software customization and security in vestments. The result is illustrated in Proposition 3.

Proposition 3 (Cloud Security Investment).

a. In low-security-loss environments, the cloud vendor invests no effort to improve cloud security.

b. In high-security-loss environments, (1) the cloud vendor’s optimal level of security investment is not affected by the on-premises vendor’s customization investment; (2) there exists a threshold $\xi _ { 1 } = ( 1 - e _ { L } ^ { * } ) / ( 1 - e _ { R } ^ { * } )$ such that

i. When $\varpi _ { R } / \varpi _ { L } < \xi _ { 1 } / 2$ , the cloud vendor’s security investment decreases with the on-premises vendor’s security investment if α is sufficiently large and increases if α is not so large;

ii. When $\varpi _ { R } / \varpi _ { L } > 2 \xi _ { 1 }$ , the cloud vendor’s security investment increases with the on-premises vendor’s security investment if α is sufficiently large and decreases if α is not so large; and

iii. When $\xi _ { 1 } / 2 < \varpi _ { R } / \varpi _ { L } < 2 \xi _ { 1 }$ , the cloud vendor’s security investment decreases with the on-premises vendor’s security investment.

An important insight in Proposition 3 is that the cloud vendor is seen to do better by not investing security-improving effort in low-security-loss environments. The reasoning is that a decline in the probability of attacks on the cloud service reduces the cloud vendor’s profit by lowering its price. When making purchase decisions in high-security-loss environments, consumers care more about security risks and vendors’ effort in improving security. In equilibrium, the cloud vendor’s price and market share hinge on the security risks associated with the products. Thus, the customization capability of the onpremises software does not affect the marginal value of cloud security investment on the cloud vendor’s profit. The cloud vendor’s security investment, however, varies nonmonotonically with its rival’s security investment. When the ratio $\varpi _ { R } / \varpi _ { L }$ is low, a large proportion of consumers will pay for the cloud service. In this case, if consumers face a sufficiently large loss per use, a higher security investment by the onpremises vendor will reduce the marginal benefit of security investment on the cloud vendor’s profit, leading to the cloud vendor lowering investment to reduce costs. In sharp contrast, if $\varpi _ { R } / \varpi _ { L }$ is high enough, under the condition of a large loss per use, the marginal value of cloud security investment increases with the on-premises vendor’s security investment, which encourages the cloud vendor to enhance investment when the on-premises vendor’s security investment increases.

Because the on-premises vendor could optimize investments in product customization as well as in security, we are interested in investigating how the on-premises vendor’s customization and security investments interact to influence consumers’ purchase choice. In the next proposition, we demonstrate that the interaction between the two investment variables differs between low- and high-securityloss environments.

Proposition 4 (Interaction of Security and Customization Investments).

a. In low-security-loss environments, the on-premises vendor’s customization and security investments act as substitutes.

b. In high-security-loss environments, the on-premises vendor’s customization and security investments act as complements if $\varpi _ { L } / \varpi _ { R } > ( 1 - e _ { R } ^ { * } ) \bar { / } ( 1 - e _ { L } ^ { * } )$ and substitutes otherwise.

In low-security-loss environments, a higher level of security investment dampens the on-premises vendor’s incentive to invest effort in improving product customization capability and vice versa. This is evident from the fact that $\partial ^ { 2 } \pi _ { L } / \partial \beta \partial e _ { L } < 0 ;$ that ${ \mathrm { i } } \mathbf { s } ,$ the increase in the on-premises vendor’s profit with increasing security investment is higher for lower levels of customization investment and vice versa. In other words, the marginal value of security (customization) investment on the on-premises vendor’s profit increases when the vendor’s investment in customization (security) decreases. In high-security-loss environments, however, the two variables can be complementary. When $\varpi _ { L } / \varpi _ { R }$ exceeds a threshold, a higher level of security (customization) investment intensifies the marginal impact of customization capability (security), leading to the vendor increasing investment in product customization (security).

Next, we consider the roles of misfit cost and security risk in influencing vendors’ investment effort. In high-security-loss environments, the misfit cost and security risk have a complicated relationship with vendors’ investment decisions. It is difficult to analytically determine how vendor’s investments vary with them; thus, we resort to numerical analyses, which are shown later in this paper. The following proposition focuses on the impact of misfit cost and security risk in low-security-loss environments.

Proposition 5 (Impact of Mis<sup>fi</sup>t Cost and Security Risk). In low-security-loss environments,

a. A higher misfit cost leads to a higher customization investment and a lower security investment by the onpremises vendor; and

b. A higher probability of attacks on the on-premises software increases the on-premises vendor’s investments in security and customization; a higher probability of attacks on the cloud service increases the on-premises vendor’s security investment but decreases the customization investment if the ratio $\varpi _ { L } / \varpi _ { R }$ is low.

When the misfit cost increases, the on-premises vendor is incentivized to offer a product of higher customization capability because the on-premises vendor’s competitive advantage in product customization becomes particularly prominent in low-security loss environments. Because of the substitution effect of the customization and security investments in lowsecurity-loss environments, an increase in misfit cost causes the on-premises vendor to reduce effort in improving security. One interesting finding in Proposition 5 is that the on-premises vendor will enhance its security investment when the probability of attacks on its rival’s product increases. The intuition behind this result lies in the difference between the vendors decisions in regard to security investment: in lowsecurity-loss environments, only the on-premises vendor will invest to improve product security. This provides an incentive for consumers to buy the more secure on-premises software. When the probability of attacks on the cloud service becomes increasingly high, the onpremises vendor must invest greater effort to throttle equilibrium security risk associated with its product Alternatively, the on-premises vendor can indirectly limit the negative externalities imposed by users by lowering its product customization capability.

We use Figures 6 and 7 to illustrate how the misfit cost and security risk affect vendors’ investments in high-security-loss environments. Figure 6 shows that the on-premises vendor’s customization investment $\boldsymbol { \beta } ^ { * }$ increases in the misfit cost $\tau ,$ but its security investment $\boldsymbol { e } _ { L } ^ { * }$ may increase or decrease in τ, which differs from the result in low-security-loss environments. Figure $7$ depicts the variation in vendors’ investments with respect to security risk in highsecurity-loss environments. In Figure 7, (a) and (b), we observe that the on-premises vendor’s security investment $\boldsymbol { e } _ { L } ^ { * }$ varies nonmonotonically with the probability of attacks on its product $\varpi _ { L }$ . This result may be explained by how $\varpi _ { L }$ affects the on-premises vendor’s profit in high-security-loss environments. When $\varpi _ { L }$ is small, an increase in $\varpi _ { L }$ intensifies the marginal impact of $\boldsymbol { e } _ { L } ^ { * }$ on the on-premises vendor’s profit, but when $\varpi _ { L }$ is high enough and further increases, the marginal value of $\boldsymbol { e } _ { L } ^ { * }$ on the vendor’s profit declines.

Figure 7, (c) and (d), shows the investment variations with the probability of attacks on the cloud services $\varpi _ { R } ,$ , from which we can see an increasing security investment $\boldsymbol { e } _ { L } ^ { * }$ by the on-premises vendor with an increase in $\varpi _ { R } .$ . A comparison of Figure 7, (a) and (b), with Figure 7, (c) and (d), reveals that an increased $\varpi _ { L }$ incentivizes the cloud vendor to improve security investment $e _ { R } ^ { * }$ (see Figure 7, (a) and (b)), but an increased $\varpi _ { R }$ dampens the cloud vendor’s incentive to invest in security (see Figure $^ { 7 , }$ (c) and (d)). This can be similarly explained by the impact of $\varpi _ { R }$ on market share and profit: an increase in ${ \varpi } _ { R } ,$ , on the one hand, limits the negative security externalities by reducing the cloud vendor’s market share and, on the other hand, causes a decrease in the vendor’s profit, which finally leads to the cloud vendor cutting security investment to reduce costs. Next, we consider how the on-premises vendor’s customization investment varies with the probability of attacks. When $\varpi _ { R }$ is small $( \mathrm { i . e . , ~ } \varpi _ { R } = 0 . 1 )$ , the customization investment $\boldsymbol { \beta } ^ { * }$ decreases in $\varpi _ { L }$ (see Figure $7 ( \mathrm { a } ) ) ;$ nevertheless, when $\varpi _ { R }$ is large $\displaystyle ( \mathrm { i } . \mathrm { e } . , \ \varpi _ { R } = 0 . 2 )$ , the customization investment $\beta ^ { ^ { * } }$ increases in $\varpi _ { L }$ for small values of $\varpi _ { L }$ (see Figure $7 ( \mathrm { b } ) )$ ). The variation of $\boldsymbol { \beta } ^ { * }$ with $\varpi _ { R }$ is analogous to that with $\varpi _ { L }$ (see Figure 7, (c) and (d)).

Figure 6. The Impact of Misfit Cost in High-Security-Loss Environments  
(a)  
![](/api/attachments/QHD2UJDW/fulltext/images/49d8c9a0cd3333544cdd6b987cc4ff78a45964fa94d7f5a1763f116ef6a7948f.jpg)  
Note. u 5, α 50, and c 0.05.

Figure 7, (e) and (f), illustrates the impact of consumers’ loss per use α. Combining Figure $7 ( \mathrm { e } )$ with Figure $7 ( \mathrm { f } )$ , we observe that the vendors’ decisions in regard to security investment diverge. When $\varpi _ { L } /$ ϖ<sub>R</sub> is small, an increased $\alpha$ diminishes the marginal value of the cloud vendor’s investment and improves the marginal value of the on-premises vendor’s investment, leading to a higher investment in the on-premises software $\boldsymbol { e } _ { L } ^ { * }$ and a lower investment in the cloud service $e _ { R } ^ { * } ,$ as illustrated in Figure $7 ( \mathrm { e } ) .$ Conversely, when $\varpi _ { L } / \varpi _ { R }$ is large, an increased α encourages the cloud vendor’s security investment $e _ { R } ^ { * }$ but discourages the on-premises vendor’s security investment $e _ { L } ^ { * } ,$ as illustrated in Figure 7(f).

## 4.3. Welfare-Maximizing Security Investment

Thus far we have examined the vendors’ investment decisions at the market equilibrium for the case in which both vendors engage in individual profit maximization. Next, we investigate the socially optimal levels of security investment in the on-premises software and the cloud service, denoted as $e _ { i } ^ { W } \in [ 0 , 1 ]$ by considering the customization capability of the on-premises software as an exogenous parameter. The marginal consumer $\boldsymbol { \theta } _ { 1 } ^ { * }$ could be obtained by substituting $\varpi _ { i } ( 1 - e _ { i } ^ { W } )$ for $\varpi _ { i }$ into the indifferent point given in Lemma 1. Focusing on a symmetric case where the probability of attacks on the two product is the same, that is, $\varpi _ { L } = \varpi _ { R } = \varpi _ { R }$ , social welfare can be written as follows:

(b)  
![](/api/attachments/QHD2UJDW/fulltext/images/da5e2a61ff4bcbecfe677a53f04aa08f799dec54e1a0b4331220e6426d4f036d.jpg)

![](/api/attachments/QHD2UJDW/fulltext/images/66c2824460d6bfc849f440c75f72b17651391921d49fc4f8c959683d7c7386e0.jpg)  
Figure 7. The Impact of Security Risk in High-Security-Loss Environments  
Note. u 5, α = 50 (for Figure 7, (a)–(d)), c 0.05, and τ 1.

Figure 8. Comparison of Security Investments  
![](/api/attachments/QHD2UJDW/fulltext/images/11287dacf3a520f4287d5b31ad317afa91488c989ef2f7d09d9906062c86948f.jpg)

![](/api/attachments/QHD2UJDW/fulltext/images/8fc6de99a2319d4876a65d462c7249fbb105652fa808047acbee83cc9322c485.jpg)  
Notes. u 5, $\varpi _ { L } = \varpi _ { R } = 0 . 1$ , β <sub>-</sub> 0.35, τ <sub>-</sub> 1, and $c = 0 . 2 .$ . For this numerical illustration, we use cost functions $G ( \cdot ) = C ( \cdot ) = C ( \upsilon ) =$ $( 1 / ( 1 - \upsilon ) - 1 ) ^ { 2 }$

$$
\begin{array}{l} S W (e _ {L} ^ {W}, e _ {R} ^ {W}) = \int_ {0} ^ {\theta_ {1} ^ {*}} x (u - \tau - \varpi (1 - e _ {R} ^ {W})   \alpha N _ {R}) \mathrm{d} x \\ \qquad + \int_ {\theta_ {1} ^ {*}} ^ {1} x (u - \tau (1 - \beta) - \varpi (1 - e _ {L} ^ {W})   \alpha N _ {L}) \\ \qquad - \int_ {0} ^ {\theta_ {1} ^ {*}} x c \mathrm{d} x - C (e _ {L} ^ {W}) - C (e _ {R} ^ {W}), \end{array}\tag{dx}
$$

(5)

where $N _ { R } = \theta _ { 1 } ^ { * }$ and $N _ { L } = 1 - \theta _ { 1 } ^ { * }$

Differentiating with respect to $e _ { L } ^ { W }$ and $e _ { R } ^ { W }$ yields the optimal security investments $e _ { L } ^ { W ^ { \ast } }$ and $e _ { R } ^ { W ^ { * } }$ <sup>\*</sup>. Lemma 3 presents social welfare-maximizing levels of security investment in high- and low-security-loss environments.

Lemma 3. The security investments under social welfare maximization exhibit the following properties:

a. For high-security-loss environments, social welfaremaximizing levels of security investment $e _ { L } ^ { W ^ { \ast } }$ and $e _ { R } ^ { W ^ { * } }$ <sup>\*</sup> are obtained by solving

$$
\begin{array}{r l r} & & {\frac {(1 - e _ {R} ^ {W *}) ^ {2}}{(2 - e _ {L} ^ {W *} - e _ {R} ^ {W *}) ^ {3}} \left(\frac {1}{2} \alpha \varpi (2 - e _ {L} ^ {W *} - e _ {R} ^ {W *}) \right.} \\ & & {\left. + \frac {(1 - e _ {L} ^ {W *}) (\beta \tau + c)}{1 - e _ {R} ^ {W *}}\right) = C ^ {\prime} (e _ {L} ^ {W *}) a n d} \\ & & {\frac {(1 - e _ {L} ^ {W *}) ^ {2}}{(2 - e _ {L} ^ {W *} - e _ {R} ^ {W *}) ^ {3}} \left(\frac {1}{2} \alpha \varpi (2 - e _ {L} ^ {W *} - e _ {R} ^ {W *}) - \beta \tau - c\right)} \\ & & {= C ^ {\prime} (e _ {R} ^ {W *}).} \end{array}
$$

b. For low-security-loss environments, social welfaremaximizing levels of security investment $e _ { L } ^ { W ^ { \ast } }$ and $e _ { R } ^ { \boldsymbol { W } ^ { * } }$ are obtained by solving

$$
\begin{array}{l} \frac {7}{3 2} \alpha \varpi - \frac {\alpha^ {2} \varpi^ {2} (3 1 (1 - e _ {L} ^ {W ^ {*}}) + 2 7 (1 - e _ {R} ^ {W ^ {*}}))}{2 5 6 (\beta \tau + c)} + \mathrm{O} (\alpha^ {3}) \\ = C ^ {'} (e _ {L} ^ {W ^ {*}}) a n d \\ \frac {7}{3 2} \alpha \varpi + \frac {\alpha^ {2} \varpi^ {2} (2 4 9 (1 - e _ {R} ^ {W ^ {*}}) - 2 7 (1 - e _ {L} ^ {W ^ {*}}))}{2 5 6 (\beta \tau + c)} + \mathrm{O} (\alpha^ {3}) \\ = C ^ {'} (e _ {R} ^ {W ^ {*}}). \end{array}
$$

A direct interpretation of the results in Lemma 3 is provided in Proposition $6 ,$ which summarizes the comparison of security investments in the cloud service and on-premises software under welfare maximization.

Proposition 6 (Welfare-Maximizing Levels of Security Investment). If the cloud service and on-premises software are subject to the same levels of attack, the socially optimal level of security investment is higher for the cloud service in low-security-loss environments and for the onpremises software in high-security-loss environments.

One implication highlighted in Proposition 6 is that in low-security-loss environments, we can expect a lower security risk of intrusion in the cloud service than in the on-premises software when a social planner sets risk-reduction factors. This result contrasts with that in Proposition $^ { 4 , }$ which shows that the cloud vendor does not invest to improve security in low-security-loss environments. This can be explained by recalling the different objectives of the social planner and individual vendors. While the individual vendor’s objective is to maximize its own profit by choosing security investment independently, the social planner aims to maximize the sum of the vendor and consumer surpluses. In high-securityloss environments, the maximizing social welfare yields a greater security-improving investment in the onpremises software than in the cloud service.

We use Figure 8 to illustrate the impact of consumers’ loss per use α and compare the optimal levels of security investment under welfare maximization with that under individual profit maximization. Figure 8(a) shows that in low-security-loss environments, the security investment in cloud service $e _ { R } ^ { W ^ { * } }$ is higher than that in on-premises software $e _ { I . } ^ { W ^ { * } }$ under welfare maximization. We also observe that $e _ { L } ^ { \breve { W } ^ { \ast } }$ first increases in α and then decreases in it. Under individual profit maximization, however, the cloud vendor exerts no effort in improving security, as illustrated by the dotted line in Figure 8(a), and the onpremises vendor’s security investment $\boldsymbol { e } _ { L } ^ { * }$ increases in $\alpha ,$ as illustrated by the dash-dotted line. In high-securityloss environments, we can see from Figure 8(b) that $e _ { L } ^ { W ^ { * } } > e _ { R } ^ { W ^ { * } }$ , implying that social welfare maximization results in greater effort in addressing on-premises security than in addressing cloud security. In contrast, when the individual vendors choose their own investment levels, the cloud service may be more secure than the on-premises software because the cloud vendor invests greater security-improving effort than the on-premises vendor, that is, $\displaystyle { \dot { e } } _ { R } ^ { * } > e _ { L } ^ { * }$

## 5. Implications and Conclusions

In this paper, we investigate vendors’ pricing and product security and customization investments in the presence of security externalities that are endogenously determined by consumption behavior. Intuitively, a larger market coverage and higher usage frequencies lead to a higher profit. A larger user population, however, also increases the incentives of hackers and, thus, the security risk exposure of users because of the negative externalities. A higher usage frequency further increases users’ security loss and misfit cost. The two impacts on consumer utility, in turn, lead to a reduction in vendors’ profitability. Our analyses provide a deep understanding of the competitive implications of security risks and product customization on vendors’ pricing and investment decisions.

We find that consumers suffer a lower average expected loss from using cloud services than from using on-premises software, especially in highsecurity-loss environments. This result mirrors the finding of Gartner that the idea of cloud services being less secure than on-premises solutions is more myth than reality (Conn 2014). The 2017 Cloud Security Report released by Alert Logic also shows that customers who opted for cloud-based solutions experienced 405 security attacks over the 18-month period, whereas the on-premises customers suffered 612, a 51% higher rate of attack escalations (Alert Logic 2017). When the probability of attacks on the cloud service is large enough, we find that the average expected loss borne by cloud users may be lower in high-security-loss environments than that in low-security-loss environments. For on-premises users, if the probability of attack on the on-premises software is sufficiently low, lowsecurity-loss environments create a lower average expected loss.

Interestingly, we find that an increase in the probability of attacks on a vendor’s product may not incentivize that vendor to increase effort in addressing security risk associated with its product, but an in crease in the probability of attack on the competing product can induce a higher level of security investment by that vendor. In low-security-loss environments, the cloud vendor becomes better off when the probability of attack on its network increases, gaining a higher price, larger market share, and eventually higher profit. In high-security-loss environments, the cloud vendor could price high enough to capture all consumer surplus. Under such circumstances, if the probability of attack on the cloud service is sufficiently low relative to the probability of attack on the on-premises software, the cloud vendor will increase its security-improving effort when consumers’ loss per use from being attacked becomes higher. This finding may help explain why the cloud vendors whose services access the users sensitive information, such as accounting and enterprise resource planning, make a large investment in security to protect their customers from any kind of security attack. We also demonstrate that the on premises vendor’s investment decision varies depending on the levels of consumer security loss. In low-security loss environments, an increase in customization investment reduces the on-premises vendor’s security investment, and vice versa, whereas under cer tain conditions in high-security-loss environments, an increase in customization investment induces a greater investment in the security of the on-premises software.

Our results have several implications. First, for customers who are particularly sensitive to the loss associated with security attacks, moving remotely to the cloud may be a better choice than using the local on-premises software. Second, cloud vendors do not necessarily benefit economically from investing in addressing cloud security, especially in low-securityloss environments, and the implications of security investment are different when consumers face different levels of security loss. On-premises vendors should strategically adjust their investment efforts in improving product customization capability and reducing security risk. In particular, the vendors should pay close attention to their product security when the level of attack on their rival’s product increases. A policy implication of our findings is that if the on-premises software and the cloud services face the same level of attack, a social planner should set a larger value of risk-reduction factor for the onpremises software in high-security-loss environments and for the cloud services in low-securityloss environments.

In this paper, we consider the competition between a pure cloud service vendor and a pure on-premises software vendor and focus on the SaaS business model of the cloud service. Although the SaaS applications have limited ability to customize, the private or hybrid cloud services allow users to customize according to their preferences. The trend toward customized cloud services continues to grow because of mainly security concerns (Steiner 2014). We study the game in a duopoly setting. A more realistic game would be to include more on-premises software vendors and more cloud vendors. The oligopoly model, however, presents analytics challenges, especially when the security risk is endogenously determined by strategic consumption behavior.

In recent years, many long-established on-premises software vendors have been offering cloud-based alternatives in addition to on-premises offerings. Some vendors, such as SAP, Oracle, and Microsoft, have embraced such a mixed strategy. An interesting direction of our research is to analyze competition outcomes and vendors’ strategies in the setting of a pure cloud vendor and a mixed on-premises vendor. Another area not considered in this paper is that of mediumsecurity-loss environments. Our modeling setup is suitable for exploring vendors’ pricing and investments strategies at all levels of security losses associated with attacks, but the asymptotic analysis used in this paper provides insights into vendors’ strategies in mainly high- and low-security-loss environments. The findings obtained in this work may not apply to medium-security-loss environments.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive comments throughout the review process.

## References

Alert Logic (2017) Alert Logic releases 2017 cloud security report. Press release, Alert Logic, Houston, Texas. Accessed February 5, 2020, https://www.alertlogic.com/press-releases/alert-logic-releases-2017-cloud-securitv-report/

Arora A, Telang R, Xu H (2008) Optimal policy for software vul nerability disclosure. Management Sci. 54(4):642–656.

August T, Tunca TI (2006) Network software security and user in centives. Management Sci. 52(11):1703–1720.

August T, Tunca TI (2011) Who should be responsible for software security? A comparative analysis of liability policies in network environments. Management Sci. 57(5):934–959.

August T, Niculescu MF, Shin H (2014) Cloud implications on software network structure and security risks. Inform. System Res. 25(3):489–510.

Babcock C (2016) Gartner sees \$1 trillion shift in IT spending to cloud. InformationWeek (July 25), http://www.informationweek.com/ cloud/infrastructure-as-a-service/gartner-sees-\$1-trillion-shift -in-it-spending-to-cloud/d/d-id/1326372.

Balasubramanian S, Bhattacharya S, Krishnan VV (2015) Pricing information goods: a strategic analysis of the selling and payper-use mechanisms. Marketing Sci. 34(2):218–234.

Chen PY, Kataria G, Krishnan R (2011) Correlated failures, di versification, and information security risk management. Management Inform. Systems Quart. 35(2):397–422.

Chen PY, Wu SY (2013) The impact and implications of ondemand services on market structure. Inform. Systems Res. 24(3):750–767.

Chesher A (1989) Hajek inequalities, measures of leverage and the size of heteroskedasticity robust wald tests. Econometrica 57(4): 971–977.

Choudhary V (2007) Comparison of software quality under perpetual licensing and software as a service. J. Management Inform. System 24(2):141–165.

Choudhary V, Zhang Z (2015) Research note—Patching the cloud: The impact of SaaS on patching strategy and the timing of software release. Inform. Systems Res. 26(4):845–858.

Choudhary V, Tomak K, Chaturvedi A (1998) Economic benefits of renting software. J. Organ. Comput. Electronic Commerce 8(4):277–305.

Conn S (2014) Gartner highlights the top 10 cloud myths. Gartner (October 28), https://www.gartner.com/en/newsroom/press -releases/2014-10-28-gartner-highlights-the-top-10-cloud-myths.

Constantin L (2014) Hacker puts “full redundancy” code-hosting firm out of business. PCWorld (June 19), https://www.pcworld.com article/2365602/hacker-puts-full-redundancy-codehosting -firm-out-of-business.html.

Dey D, Lahiri A, Zhang G (2014) Quality competition and market segmentation in the security software market. Management In form. Systems Quart. 38(2):589–606.

Fan M, Kumar S, Whinston AB (2009) Short-term and long-term competition between vendors of shrink-wrap software and software as a service. Eur. J. Oper. Res. 196(2):661–671.

Gabaix X, Laibson D, Li D, Li H, Resnick S, de Vries CG (2016) The impact of competition on prices with numerous firms. J. Econom. Theory 165:1–24.

Guo ZL, Ma D (2017) A model of competition between perpetual software and software as a service. Management Inform. Systems Quart. 42(1):101–120.

Greenemeier L, Hoover JN (2007) How does the hacker economy work? InformationWeek (February 9), https://www.informationweek.com how-does-the-hacker-economy-work/d/d-id/1051843

Hui KL, Hui W, Yue T (2013) Information security outsourcing with system interdependency and mandatory security requirement. J. Management Inform. Systems 29(3):117–156.

IBM Security (2019) 2019 Cost of a data breach report. Report, IBM, Armonk, NY.

IDC (2019) Worldwide public cloud services spending will more than double by 2023, according to IDC. Report, IDC, Framingham, MA.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Kannan K, Telang R (2005) Market for software vulnerabilities? Think again. Management Sci. 51(5):726–740

Karanika V (2013) The cloud, mobility. . . and beyond. Accessed Jan uary 28, 2019, https://www.cisco.com/c/dam/global/el\_gr assets/connect2013/pdfs/015\_idc\_evangelos\_karanikas.pdf.

Kim BC, Chen PY, Mukhopadhyay T (2011) The effect of liability and patch release on software security: The monopoly case. Production Oper. Management 20(4):603–617.

King R (2014) Forrester: public cloud market will reach \$191B by 2020. ZDNet (April 24), http://www.zdnet.com/article/forrester -public-cloud-market-will-reach-191b-by-2020/.

Kreps DM (1977) A note on fulfilled expectations equilibria. J. Econom. Theory 14(1):32–43.

Laffont J-J, Tirole J (1988) The dynamics of incentive contracts. Econometrica 56(5):1153–1175.

Laffont J-J, Tirole J (1993) A Theory of Incentives in Procurement and Regulation (MIT Press, Cambridge, MA).

Landewe M (2016) Widespread attack on Office 365 corporate users with zero-day ransomware virus. Avanan (June 27), https:/ www.avanan.com/blog/attack-on-office-365-corporate-users -with-zero-day-ransomware-virus.

Lee CH, Geng X, Raghunathan S (2016) Mandatory standards and organizational information security. Inform. Systems Res. 27(1): 70–86.

Ma D, Seidmann A (2015) Analyzing software as a service with per transaction charges. Inform. Systems Res. 26(2):360–378.

MacLeod WB, Malcomson JM (1993) Investments, holdup, and the form of market contracts. Amer. Econom. Rev. 83(4):811–837.

Mitra S, Ransbotham S (2015) Information disclosure and the diffusion of information security attacks. Inform. Systems Res. 26(3): 565–584.

Muller HM (2000) Asymptotic efficiency in dynamic principal-agen problems. J. Econom. Theory 91(2):292–301

Niculescu MF, Wu DJ (2014) Economics of free under perpetual licensing: implications for the software industry. Inform. System Res. 25(1):173–199.

Sarno D, Rodriguez S (2011) Hacker attacks show vulnerability of cloud computing. Los Angeles Times (June 17), http://articles.latimes.com 2011/jun/17/business/la-fi-cloud-security-20110617.

Schneier B (2015) Should companies do most of their computing in the cloud? (Part 1) (June 10), https://www.schneier.com/blog archives/2015/06/should\_companie.html.

Seals T (2016) Cloud service adoption leads to more data breaches. Infosecurity (October 14), https://www.infosecurity-magazine.com news/cloud-service-adoption-leads-data/.

Steiner P (2014) Customization is the name of the game in cloud com puting. Betanews (August 11), https://betanews.com/2014/08/11 customization-is-the-name-of-the-game-in-cloud-computing/.

Sun W, Zhang X, Guo CJ, Sun P, Su H (2008) Software as a service: Configuration and customization perspectives. Zhang LJ, Hofmann P, eds. 2008 IEEE Congress Services Part II (Services-2 2008) (IEEE Computer Society Press, Los Alamitos, CA), 18–25.

Sundararajan A (2004) Nonlinear pricing of information goods Management Sci. 50(12):1660–1673.

Verizon (2017) 2017 data breach investigations report. Report, Ver izon, New York.
