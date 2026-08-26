---
otero_id: 11978
otero_key: "YRWVB83M"
title: "Cost and benefit analysis of authentication systems"
authors: "Kemal Altinkemer; Tawei Wang"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cost and bene<sup>fi</sup>t analysis of authentication systems

Kemal Altinkemer <sup>a,</sup>⁎, Tawei Wang <sup>b,</sup>⁎

<sup>a</sup> Krannert Graduate School of Management, Purdue University, 403 W. State Street, West Lafayette, IN 47907, United States

<sup>b</sup> Department and Graduate Institute of Accounting, College of Management, National Taiwan University, Taipei, 106 Taiwan

## a r t i c l e i n f o

Article history: Received 10 April 2009 Received in revised form 10 January 2011 Accepted 20 January 2011 Available online 31 January 2011

Keywords: Information security Authentication Biometric Two-factor authentication

## a b s t r a c t

This study investigates the key elements an online service or product provider needs to consider when adopting another single-factor or two-factor authentication system. We also uncover the conditions that make the new one-factor or two-factor authentication system more preferable. By using the probability of system failure, this study generalizes all possible combination of authentication systems into four different cases. This generalization allows us to compare different systems and to determine the key factors managers need to consider when adopting a new authentication system. The key factors are (1) additional implementation costs, (2) customer switching which is determined by the market share and customers preferences, and (3) expected losses when the new system fails. This study also suggests that if the provider chooses an expensive new system, the provider needs to have a larger market share to justify the spending. Also, regulators can encourage the adoption of a more secure authentication system by changing the penalty a <sup>fi</sup>rm faces when the system fails. Finally, it could also be preferable to have both one-factor and two-factor authentication systems depending on the customers' characteristics.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Authentication can be used to verify either the content of the message, the origin of the message, or the identity of the user [26,41]. Identity authentication focuses on the process of verifying a person's identity. In general, the information (or factors) people use to identify themselves is (1) something the user is. This is biometric information, such as <sup>fi</sup>ngerprints; (2) something the user has, such as an ID card; (3) something the user knows, such as a password [30]. In some situations, users have to provide two of the above information simultaneously, for instance, an Automatic Teller Machine (ATM) card and a Personal Identi<sup>fi</sup>cation Number (PIN). This is called two-factor authentication. Two-factor or multi-factor authentication, as the name suggests, uses more than one single piece of information when granting access right. By using more information, the authentication system could be more secure (e.g., [45]). Given that the new authentication system could be more secure and as the concerns about identity theft have increased its popularity [4], people start to propose the use of two-factor authentication systems in order to effectively distinguish imposters from genuine users. For example, the Federal Financial Institutions Examination Council (FFIEC) released guidance on authentication in Internet banking environment on October 12, 2005 [16]. This guidance asked all the regulated agencies, by the end of 2006, to conduct risk-based assessments and to develop security measures to reliably authenticate (i.e., two-factor or multi-factor authentication) customers remotely accessing their online <sup>fi</sup>nancial services

A multi-factor authentication system seems to be more secure but the <sup>fi</sup>rm might need to allocate more resources on implementations, such as software, hardware, and training [45]. From the customers' viewpoint, multi-factor authentication could be accompanied with the concerns about the use of additional information collected. The new interfaces, new devices, and the new authentication processes could also result in inconvenience of the new authentication system and a prolonged time needed to complete the transaction. All of the above issues could at the same time affect an online service or product provider's decision when implementing a new authentication system.

This paper focuses on the decision of implementing a new authentication system and addresses the following research questions. First, from an online service or product provider's perspective, what are the key elements it needs to consider when adopting another single-factor or two-factor authentication system? Second, what are the conditions that make the new one-factor or two-factor authentication system more preferable? Given that there are all kinds of authentication technologies, it is unrealistic to compare different authentication methods or to optimize the decision by considering all the possibilities. Therefore, in order to answer our research questions, we use a static model as a <sup>fi</sup>rst attempt to understand the decision of choosing authentication systems. In particular, this study <sup>fi</sup>rst generalizes all the authentication systems into two broad types. Based on the generalization, we compare the conditions that make the new authentication system more preferable regardless of the detail

Table 1

speci<sup>fi</sup>cation of the technology. These conditions allow us to uncover the rules that provide rationale for managers to choose authentication systems.

The remaining of the paper is organized as follows. Relevant literature on authentication and privacy are reviewed in Section 2. In Section 3, we propose a static model for one-factor and two-factor authentication systems. This model leads to our propositions and managerial implications in Section 4. We conclude with contributions, and possible avenues for future research in Section 5.

## 2. Literature review

There are two major streams of literature related to our research: authentication, and privacy in the context of authentication systems and privacy from an economic perspective.

## 2.1. Authentication

The literature on authentication has long been discussed from the technical perspective. For instance, Woo and Lam [46] and Dif<sup>fl</sup>e et al. [15] provide the basic authentication mechanisms and the goals of authentication. Other studies focus on the design of protocols (e.g., [1,40]) or ways to implement or improve authentication methods (e.g., [5,6,37]). However, studies about authentication from an economic perspective are limited. These studies are often embedded in the discussion of other issues. For example, Anderson [3] discusses the role of authentication in information security from an economic perspective. Also, authentication has also been discussed in internal control, EDP auditing, assurance, knowledge sharing as well as group decision literature (e.g., [19,27,39,42]). Different from previous literature, our study formally focuses on the authentication system decisions from an economic perspective and provides decision rules for managers.

## 2.2. Privacy in the context of authentication systems and privacy from an economic perspective

It is unavoidable to obtain users' personal identi<sup>fi</sup>able information when implementing an authentication system, such as names, addresses, purchasing history, or biometric images of an individual (e.g., [29,34]). Several studies have discussed the collection of personal identi<sup>fi</sup>able information and the techniques to preserve privacy in the context of authentication systems (e.g., [6,10,13,14,32]). Accordingly, this study also relates to, though not directly, the literature on privacy from an economic perspective. Privacy is de<sup>fi</sup>ned as the individual's ability to control the collection and use of personal information (e.g., [18,21,24,36,44]). Studies about privacy from an economic perspective include reviews on the economic analyses of privacy (e.g., [24]), how businesses use personal information to customize services and to discriminate consumers (e.g., [12,20,47]), and how business use personal information for promotions and cross market information (e.g., [2,22]). The violation of privacy depends on (1) whether consumers can control the amount and the depth of information collected, and (2) the knowledge of the collection and use of their personal information [11]. For instance, Hoffman et al. [23] show that about 95% of online users are reluctant to provide personal information to websites because of privacy concerns. In the context of authentication systems, the change in authentication level could imply the need for more information depending on the system a <sup>fi</sup>rm chooses and the amount of information that might lose once the system fails. The privacy concerns about providing personal identi<sup>fi</sup>able information could affect customers' willingness to use an authentication system which in turn affects a <sup>fi</sup>rm's decision on authentication systems. Therefore, the privacy concerns are involved in the selection process of authentication system alternatives.

## 3. Model

In this section, we <sup>fi</sup>rst present the basic settings for our analysis. Then the de<sup>fi</sup>nition and the probability of system failure under different authentication methods are discussed followed by the details of our models for one-factor and two-factor authentication systems. Finally, by comparing the expected costs and losses associated with different authentication systems, we show the conditions that make the new authentication system preferable.

## 3.1. Basic settings

We focus on one online service or product provider in this study. This provider currently has a market share of m in the service or product category it provides, where 0bmb1 (see Appendix A for variable de<sup>fi</sup>nitions). This market share m can also be interpreted as the total value the provider can get from the customers compared to other providers. In order to complete the transaction process, each of the providers' customers is required to provide a certain level (α, 0bα≤1) of personal information, such as name, address, and phone number. If the system fails, the product or service provider might need to compensate its consumers' losses and to pay a legal penalty or <sup>fi</sup>ne (L for both the compensation and penalties) for not abiding by the privacy commitment or regulations (e.g., [38]). The compensation of customers' losses and the penalties (L) increases as the number of customers that are affected (i.e., m) and the level of information the customers provide (i.e., α) increase.

The customers are categorized along two dimensions: privacy and convenience. The <sup>fi</sup>rst dimension is privacy sensitivity. A proportion of customers (ρ, $0 { \le } \rho { \le } 1 )$ are privacy sensitive in the market the provider faces. This portion of customers has more concerns about the information collected from them and the use of such information. Therefore, adopting another authentication system, a provider might attract some potential customers and lose some existing customers both because of the privacy concerns. The new system might protect the information better (e.g., [45]) and attract some potential customers. However, when the new system is breached, more information could be lost and some of the existing customers might choose not to continue subscribing or purchasing from the provider.

The second dimension is convenience sensitivity. A proportion of customers (δ, 0≤δ≤1) emphasize more on the convenience of the transaction such as the new interface and the new processes. After the provider switches to a new authentication system, the provider might lose a certain portion of existing customers because of the possible inconvenience, such as prolonged transaction time, caused by the new system. This categorization is illustrated in Table 1.

In this paper, system failure is de<sup>fi</sup>ned as any situation in which non-genuine users (e.g., hackers) are able to access to the information or genuine users are unable to access to the information because of the failure of the software or hardware, compatibility issue of the software or hardware, for example, or the successful action of the hackers. Based on the de<sup>fi</sup>nition, we discuss the probability of system failure for different authentication systems.

## 3.2. Probability of system failure

We group all the authentication systems into three categories as mentioned in the Introduction, namely, (1) something the user has, (2) something the user knows and (3) something the user is (i.e., the biometric information) [30]. In the following paragraphs, we <sup>fi</sup>rst discuss one-factor authentication systems. Following that, we present the cases for two-factor authentication systems.

The categorization of customers.

<table><tr><td rowspan="4">Privacy sensitivity</td><td>High</td><td> $\rho(1-\delta)$ </td><td> $\rho\delta$ </td></tr><tr><td>Low</td><td> $(1-\rho)(1-\delta)$ </td><td> $(1-\rho)\delta$ </td></tr><tr><td></td><td>Low</td><td>High</td></tr><tr><td></td><td colspan="2">Convenience Sensitivity</td></tr></table>

a. Implementation Costs  
![](/api/attachments/YRWVB83M/fulltext/images/e35a470427ba01af1db99c6c98ae47c2c0197552d463be69d3c34544e910786e.jpg)  
c. Percentage of Convenient Sensitive Customers

b. Percentage of Privacy Sensitive Customers  
![](/api/attachments/YRWVB83M/fulltext/images/8f39799743e89877e0bd4ac7439694d9f51ab08e61f1958e754e0dfada5e7d81.jpg)

![](/api/attachments/YRWVB83M/fulltext/images/492ea5ea83cc6a6eb3bc5bebdeba4557c5201c1637b126c98e0ae4c03ca32fe4.jpg)

d. Market Share  
![](/api/attachments/YRWVB83M/fulltext/images/afd72751031f20283b74ccc9f4c8d96c345a57150f4ee1cdf36475eb8355c810.jpg)  
Fig. 1. The impact of four factors on authentication system decision.

When the information used for authentication is the information someone has, the one-factor authentication system can be regarded as a non-repairable system with one component. The reason is that, as an analogy to light bulbs, the longer the time we use a light bulb, the higher the chance that we need to replace it. In our context, this means that the longer the time we use a system, the larger the possibility that the system might encounter software or hardware problem due to compatibility issue, for example. Similarly, when the information used for authentication is the information someone knows, the one-factor authentication system can also be viewed as a non-repairable system with one component. The reason is that, the longer the time we use a system, the larger the possibility the password could be lost or detected, for instance. Nevertheless, when the user renews the password or upgrades the system, the system failure probability is reset to zero. In the following analyses, we consider the above two groups of authentication systems both as a non-repairable system with one component. Building on the concept of reliability analysis [43], the cumulative density function (CDF) of system failure of one nonrepairable component across the life span of the system t equals to 1− $e ^ { - ( t / \Lambda ) ^ { b } }$ where λ is the mean-time-to-failure and b is the change of failure rate. Given that there are all kinds of authentication systems within this category, in the following analysis, we do not pose any assumption on λ and b. The life span of the system t is later used to capture the different system failure probability over the life span of the system. This probability (i.e., $1 - e ^ { - \hat { ( } t / \Lambda ) ^ { b } } )$ only accounts for one part of the probability of system failure. According to our de<sup>fi</sup>nition of system failure, when an imposter uses the correct information and gains access right to the system should also be considered as system failure. For example, a hacker can obtain the correct login information through phishing. However, when the hacker enters this correct information, the authentication system allows the hacker to login and still functions correctly. Since the system functions correctly, the above probability $( \mathrm { i } . \mathrm { e } . , 1 - \stackrel { - } { e } ^ { - ( t / \lambda ) ^ { b } } )$ ) does not capture the situation when an imposter uses the correct information and gains access right to the system. In order to take into account this possibility, we also need to consider the hackers' successful actions. Given that the hacking technology is improving with time and the chance of getting the authentication information is also higher as time passes, the successful rate of the hackers' actions (denoted as H(t)) under different authentication methods should be an increasing function of time $( H ( t ) = \log ( t ) ) . ^ { 1 }$ Accordingly, the overall probability of system failure for one non-repairable component system (denote as $F _ { n } ( t )$ where the subscript n represents the one nonrepairable component) is thus assessed by both $1 - e ^ { - ( t / \Lambda ) ^ { b } }$ and $H _ { n } ( t )$ i.e., $F _ { n } ( t ) = ( \hat { 1 _ { \mathrm { } } } \bar { { } } \bar { { } } e ^ { - \bar { ( { } t / \Lambda ) ^ { b } } } ) + H _ { n } ( t ) - ( 1 - \bar { e ^ { - \bar { ( } t / \Lambda ) ^ { b } } } ) H _ { n } ( t )$ . Note that since the hackers' successful action could co-occur with software or hardware problems, we need to consider the probability when both occur. For example, the overall probability of system failure before time t is 75%, where 50% results from the system itself $( 1 - e ^ { - ( t / \Lambda ) ^ { b } } )$ ) and the other 50% results from hackers $\left( H _ { n } ( t ) \right)$

The other information that can be used for one-factor authentication systems is biometric information.<sup>2</sup> Similar to the above two types of authentication systems, the longer the time we use a biometric authentication system, the larger the possibility that the system might encounter software or hardware problem due to compatibility issue, for example. It seems that we can also consider the biometric authentication system as a non-repairable component system. However, biometric authentication systems are different from the systems using the information someone has and someone knows because of the following. Biometric authentication system measures an individual's physical or behavioral features based on the data stored, and then determines the identity of the user (e.g., [28]). Biometric systems use “scores” to show the similarity between a pattern and a biometric template (e.g., [7– 9,25,35]). If the score is higher than a certain pre-determined threshold, access right is granted. Depending on the threshold chosen, the impostor patterns can be falsely accepted by the system and some genuine patterns may be falsely rejected.<sup>3</sup> The access granting decision for biometric systems is not dichotomy anymore. In particular, a user can enter the correct information but is not able to get access to the system without any system problems which is different from the nonrepairable component systems. For example, for passwords, when a user mistypes the password or when the system is down, the user could not get access to the system. However, for <sup>fi</sup>ngerprints, for instance, a genuine user might still be blocked from the system just because of aging. Accordingly, we should consider a probability of false acceptance (FAR, ψ) and false rejection (FRR, φ) at any given time t based on the predetermined threshold $( { \overline { { s } } } ) . ^ { 4 }$ Once the specification is determined. the probability of system failure given the pre-determined threshold (s) across the life span of the system t (denote as $F _ { b i o } ( t ; \bar { s } )$ where the subscript bio represents the biometric system) is assessed by both 1− $( 1 - w _ { F R R } \varphi - w _ { F A R } \psi ) ^ { t } ( \mathrm { e . g . } , [ 3 3 ] )$ and $H _ { b i o } ( t ) ,$ , where $w _ { F R R }$ and $w _ { F A R }$ are the weights for false rejection rate and false acceptance rate respectively. These two weights are pre-determined by the provider at the time when it determines the speci<sup>fi</sup>cation of the system based on its own preferences. Speci<sup>fi</sup>cally, $F _ { b i o } ( t ; \bar { s } )$ equals $[ 1 - ( 1 - w _ { F R R } \varphi - w _ { F A R } \psi ) ^ { t } ] +$ $H _ { b i o } ( t ) - [ 1 - ( 1 - w _ { F R R } \varphi - w _ { F A R } \psi ) ^ { t } ] H _ { b i o } ( t )$ . As we de<sup>fi</sup>ned above, the false acceptance rate can also be viewed as part of the hacker's successful rate. That is, the hacker can either use wrong information (FAR) or correct information to get access to the system. However, the association between these two components does not affect our main results below

We consider two types of two-factor authentication systems: two non-repairable component system, and one biometric and one nonrepairable component system. Following the above discussion, when there are two independent non-repairable components, the probability of system failure across the life span of the system t (denote as $F _ { n n } ( t )$ where the subscript nn represents two non-repairable components) is assessed by both $\hat { 1 } - e ^ { - ( t / \hat { \lambda } _ { 1 } ) b _ { 1 } - ( t / \lambda _ { 2 } ) b _ { 2 } }$ and $H _ { n n } ( t )$ . There are two points worth noting. First, component 1 and component 2 can have different mean-time-to-failure $( \lambda _ { 1 }$ and $\lambda _ { 2 } )$ and have different change of failure rate $( b _ { 1 }$ and $b _ { 2 } )$ . In this case, although the conditions that make the new authentication system more preferable can be different, our unreported results show that the main propositions in the next section are the same. We also consider our model as time dependent and time independent in the following analysis and our results remain the same. Therefore, we choose not to have a detailed discussion of these two parameters and only present the analysis as time dependent in the analysis section. Second, these two components could also be dependent. When these two components are dependent, we reconsider the failure probability of one component given the other component has failed. Again, our main propositions in the following section remain similar. In the following analysis, we only show the case when the two components are independent.

The other type of two-factor authentication system uses both nonbiometric and biometric information. Based on our discussion above, the probability of system failure given the pre-determined threshold (s) across time t (denote as $F _ { n b i o } ( t ; \overline { { s } } )$ where nbio represents the system with one non-repairable component and one biometric component) is calculated by both $1 - e ^ { - \bar { ( } t / \Lambda ) ^ { b } } ( 1 - w _ { F R R } \varphi - w _ { F A R } \psi ) ^ { t }$ and $H _ { n b i o } ( t )$

## 3.3. Analysis

We start our analysis with the base case: the provider is now using the one non-repairable component authentication system and considers switching to another authentication system. To show the key elements the provider should consider, the following analyses focus on the expected costs and losses the provider faces when implementing an authentication system.

The expected costs and losses (denoted as C) associated with the one non-repairable component authentication system can be expresses as the addition of the change in the customer base when the system fails and the expected losses when the system fails (the implementation costs is sunk here). The change in the customer base is the loss of customers due to the failure in terms of the value these customers can create (V) which equals the market share (m) times a percentage $( 0 \leq \varepsilon _ { 1 } \leq 1 )$ (see Appendix A for the de<sup>fi</sup>nition of ε ). The expected loss is the value the provider needs to compensate its customers and to settle possible lawsuits and penalty (L) once the system fails. This compensation and penalty should increase with the level of information users provide (α) and the market share (m). Speci<sup>fi</sup>cally, we assume that $L _ { n }$ equals $w _ { n 1 } \alpha + w _ { n 2 } m$ where $w _ { n 1 }$ and $w _ { n 2 }$ are the weight for each component. Formally,

$$
C _ {n} = F _ {n} (t) (V _ {n} + L _ {n})\tag{1}
$$

where the subscript n represents the one non-repairable component authentication system.

The <sup>fi</sup>rm now decides to use a new biometric authentication system to replace this current one non-repairable component authentication system, the associated expected costs and losses consist of four components. The <sup>fi</sup>rst component is the implementation costs (c). The second component re<sup>fl</sup>ects the net change of the customer base (denote as the subscript net\_bio in Eq. (2)) when the provider adopts the new system which is measured by the net value these customers can bring. The provider could lose some existing convenience sensitive customers because the inconvenience brought by the new system which equals the current market share (m) times a certain percentage $( 0 \le \varepsilon _ { 2 } \le 1 )$ ) of δ. At the same time, the provider might attract some potential privacy sensitive customers because of this possible safer new authentication system which is measured by the potential market share (1-m) times a certain percentage $\begin{array} { r } { ( 0 \leq \varepsilon _ { 3 } \leq 1 ) \ \mathrm { o f } \rho . } \end{array}$ . The last two terms again are the loss of customers after the system fails $( V _ { b i o } ,$ which equals the new market share after considering the net change of the customer base times a certain percentage $( 0 \leq \varepsilon _ { 4 } \leq 1 ) \ \mathrm { o f } \rho )$ and the expected losses $( L _ { b i o }$ equals $w _ { b i o 1 } \alpha + w _ { b i o 2 } m$ where $w _ { b i o 1 }$ and $w _ { b i o 2 }$ are the weight for each component) if the system fails which is similar to the base case. Accordingly,

$$
C _ {b i o} = c _ {b i o} + V _ {n e t \_ b i o} + F _ {b i o} (t; \bar {s}) (V _ {b i o} + L _ {b i o})\tag{2}
$$

where $V _ { n e t \_ b i o }$ equals m×ε<sub>2</sub> $\times \delta - ( 1 - m ) \times \varepsilon _ { 3 } \times \rho , \ V _ { b i o }$ equals [m− $m \times \varepsilon _ { 2 } \times \delta - ( 1 - m ) \times \varepsilon _ { 3 } \times \rho ] \times \varepsilon _ { 4 } \times \rho ,$ , and the subscript bio represents the biometric system.

In the same vein, if the <sup>fi</sup>rm decides to use a two non-repairable component authentication system or the combination of one nonrepairable component and one biometric component authentication system, the associated expected costs and losses again consist of four major components which are given in Eqs. (3) and (4) respectively.

$$
C _ {n n} = c _ {n n} + V _ {n e t \_ n n} + F _ {n n} (t) (V _ {n n} + L _ {n n})\tag{3}
$$

$$
C _ {n b i o} = c _ {n b i o} + V _ {n e t \_ n b i o} + F _ {n b i o} (t; \bar {s}) (V _ {n b i o} + L _ {n b i o})\tag{4}
$$

where the subscript nn (nbio) represents the two non-repairable component authentication system (the combination of one nonrepairable component and one biometric component authentication system) and the subscript net\_nn (net\_nbio) represents the net change of the customer base when the provider adopts the new system in terms of the value these customers can create. $V _ { n e t \_ n n }$ equals $m \times \varepsilon _ { 5 } \times \delta - ( 1 - m ) \times \varepsilon _ { 6 } \times \rho$ and $V _ { n e t \_ n b i o }$ equals $m \times \varepsilon _ { 8 } \times \delta - ( 1 -$ $m ) \times \varepsilon _ { 9 } \times \rho . \ V _ { n n }$ equals $\left[ m - m \times \varepsilon _ { 5 } \times \delta - \left( 1 - m \right) \times \varepsilon _ { 6 } \times \rho \right]$ ×ε ×ρ while $V _ { n b i o }$ equals $\left[ m - m \times \varepsilon _ { 8 } \times \delta - \left( 1 - m \right) \times \varepsilon _ { 9 } \times \rho \right] \times \varepsilon _ { 1 0 } \times \rho . ^ { 5 } L _ { n n }$ equals $w _ { n n 1 } \alpha + w _ { n n 2 } m$ where $w _ { n n 1 }$ and $w _ { n n 2 }$ are the weight for each component. $L _ { n b i o }$ equals $w _ { n b i o 1 } \alpha + w _ { n b i o 2 } m$ where $w _ { n b i o 1 }$ and $w _ { n b i o 2 }$ are the weight for each component.

In order to address our research question, we subtract Eq. (1) from Eqs. (2), (3), and (4) in order to understand the factors and the conditions that make the adoption worthwhile. The results are shown in Panel A, Panel B, and Panel C in Appendix B. Since one-factor and twofactor authentication systems are inherently different in terms of the calculation of the probability of system failure, we choose to focus on comparing one one-factor system with another one-factor system (subtract Eq. (1) from Eq. (2)) and to compare one two-factor with another two-factor system (subtract Eq. (3) from Eq. (4)). The comparison results given in Appendix B Panel A and Panel D demonstrate the conditions that a biometric system (or the system with one non-repairable component and one biometric component) is more preferable from <sup>fi</sup>ve different parameters: (1) additional implementation costs, (2) percentage of privacy sensitive customers, (3) percentage of convenience sensitive customers, (4) market share, and (5) the expected losses when the system fails. These conditions are discussed in the next section with managerial implications.

## 4. Managerial implications

The condition for additional implementation costs in Appendix B shows that the additional implementation costs of the new system have to be smaller than $F _ { n } ( t ) ( V _ { n } + L _ { n } ) - F _ { b i o } ( t ; \bar { s } ) ( V _ { b i o } + L _ { b i o } ) - V _ { n e t _ { h } i o }$ (or $V _ { n e t \_ n n } - V _ { n e t \_ n b i o } + F _ { n n } ( t ) ( V _ { n n } + L _ { n n } ) \_ - F _ { n b i o } ( t ; \bar { s } ) ( V _ { n b i o } + L _ { n b i o } )$ in the two factor case). The threshold re<sup>fl</sup>ects the following. Although the probability of system failure could be smaller for the new system (depending on the provider's choice and the CDF de<sup>fi</sup>ned earlier), the change in the customer base also plays an important role. The possible decrease in the probability of system failure might not be enough to justify the spending for the new systems. Speci<sup>fi</sup>cally, the implementation costs of the new system need to be balanced with the reduced losses as well as the net change of customer value. If the new system can attract more customers and reduce the losses at the same time, even the implementation costs is relatively higher, the new system is still more preferable. Fig. 1a illustrates that when all other factors are <sup>fi</sup>xed $( m = 0 . 5 , ~ \delta = 0 . 8 , ~ \rho = 0 . 8 , ~ \varepsilon _ { 5 } = \varepsilon _ { 6 } = \varepsilon _ { 7 } = \varepsilon _ { 8 } = \varepsilon _ { 9 } = \varepsilon _ { 1 0 } = 0 . 8 , ~ L _ { n n } =$ $L _ { n b i o } { = } 0 . 8 , c _ { n n } { = } 1 , F _ { n n } ( t ) = F _ { n b i o } ( t ; \bar { s } ) = 0 . 7 5 )$ , the higher the implementation cost, the less preferable a system is (the total expected costs and losses (C) is larger). For illustration purpose, the failure rate does not change with time and the hacker's successful rate is zero. However, the <sup>fi</sup>gure looks similar when we allow the failure to change and the hacker's successful rate to vary.

Second, in order to make the new system more preferable compared to the base case (i.e., compare two one-factor authentication systems), the percentage of privacy sensitive customers in the market the provider faces should be within $\frac { ^ { \prime } { - } Y - \sqrt { Y ^ { 2 } - 4 X Z } } { 2 X } \mathrm { a n d } \frac { - Y + \sqrt { Y ^ { 2 } - 4 X Z } } { 2 X }$ where $X = F _ { b i o } ( t ; \bar { s } ) ( 1 - m ) \varepsilon _ { 3 } \varepsilon _ { 4 } , ~ Y = F _ { b i o } ( t ; \bar { s } ) ( m \varepsilon _ { 4 } - m \delta \varepsilon _ { 2 } \varepsilon _ { 4 } ) + ( m - 1 ) \varepsilon _ { 3 , 0 }$ $Z = c _ { b i o } + m \delta \varepsilon _ { 2 } + F _ { b i o } ( t ; \overline { { s } } ) L _ { b i o } - F _ { n } ( t ) ( m \varepsilon _ { 1 } + L _ { n } ) ( \mathrm { o r } \quad X = F _ { n b i o } ( t ; \overline { { s } } )$ $( 1 - m ) \varepsilon _ { 9 } \varepsilon _ { 1 0 } - F _ { n n } ( t ) ( 1 - m ) \varepsilon _ { 6 } \varepsilon _ { 7 } , \qquad Y = F _ { n b i o } ( t ; \bar { s } ) ( m \varepsilon _ { 1 0 } - m \delta \varepsilon _ { 8 } \varepsilon _ { 1 0 } ) \ +$ $( 1 - m ) ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) - F _ { n n } ( t ) ( m \varepsilon _ { 7 } - m \delta \varepsilon _ { 5 } \varepsilon _ { 7 } ) , Z = c _ { n b i o } - c _ { n n } + m \delta ( \varepsilon _ { 8 } - \varepsilon _ { 5 } ) +$ $F _ { n b i o } ( t ; \bar { s } ) L _ { n b i o } { - } F _ { n n } ( t ) L _ { n n }$ for the two factor case). If the percentage of privacy sensitive customers is too low, the additional implementation costs and expected losses cannot be justi<sup>fi</sup>ed by the improved security level. For example, we observe that many online service or product providers only choose to have one-factor authentication system (the base case) because the transaction amount is generally small and the transaction frequency is generally low. The customers only need to provide the name and address to complete the transaction. In this case, a complicated authentication system is not necessary. The condition also suggests that the percentage of privacy sensitive customers should not be too high. This result seems to be counter intuitive at <sup>fi</sup>rst glance. If most of the customers care about whether the provided information is used properly, it seems that an authentication system with higher security level should <sup>fi</sup>t better with the customers' preference. However, when we investigate the conditions in detail, it seems that if most of the customers are privacy sensitive, the provider might be able to attract new customers by adopting the new authentication system but could lose more customers once the system fails. The loss of more customers could result from the loss of reputation and customers' expectations. Fig. 1b shows that when all other factors are <sup>fi</sup>xed $( m = 0 . 5 , \delta = 0 . 8 ,$ $\varepsilon _ { 5 } = \varepsilon _ { 6 } = \varepsilon _ { 8 } = \varepsilon _ { 9 } = \varepsilon _ { 1 0 } = 0 . 8 , \ \varepsilon _ { 7 } = 0 . 3 , \ L _ { n n } = L _ { n b i o } = 0 . 8 , \ c _ { n n } = c _ { n b i o } = 0 . 8 ,$ $F _ { n n } ( t ) = F _ { n b i o } ( t ; \bar { s } ) = 1 )$ , the one non-repairable component and one biometric system is more preferable when ρ is bigger than about 50% or smaller than 100%. Formally, we state our <sup>fi</sup>rst proposition.

Proposition 1. Other things being equal, a more secure (in terms of the probability of system failure) authentication system could attract new customers but lose more customers once the system fails when the percentage of privacy sensitive customers is larger than $- Y \dot { + } \sqrt { Y ^ { 2 } - 4 X Z }$ where $X = F _ { b i o } ( t ; \bar { s } ) ( 1 - m ) \varepsilon _ { 3 } \varepsilon _ { 4 } , Y = F _ { b i o } ( t ; \bar { s } ) ( m \varepsilon _ { 4 } -$ 2X m $\delta \varepsilon _ { 2 } \varepsilon _ { 4 } ) + ( m - 1 ) \varepsilon _ { 3 , } Z = c _ { b i o } + m \delta \varepsilon _ { 2 } + F _ { b i o } ( t ; \overline { { s } } ) L _ { b i o } - F _ { n } ( t ) ( m \varepsilon _ { 1 } + L _ { n } ) ( \mathrm { o r ~ }$ $X = F _ { n b i o } ( t ; \overline { { s } } ) ( 1 - m ) \varepsilon _ { 9 } \varepsilon _ { 1 0 } - F _ { n n } ( t ) ( 1 - m ) \varepsilon _ { 6 } \varepsilon _ { 7 } , Y = F _ { n b i o } ( t ; \overline { { s } } ) ( m \varepsilon _ { 1 0 } - m \delta \varepsilon _ { 8 } \varepsilon _ { 1 0 } ) \ +$ $( 1 - m ) ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) - F _ { n n } ( t ) ( m \varepsilon _ { 7 } - m \delta \varepsilon _ { 5 } \varepsilon _ { 7 } ) , Z = c _ { n b i o } - c _ { n n } + m \delta ( \varepsilon _ { 8 } - \varepsilon _ { 5 } ) \ +$ $F _ { n b i o } ( t ; \bar { s } ) L _ { n b i o } { - } F _ { n n } ( t ) L _ { n n }$ for the two factor case).

Third, as shown in Appendix B, the conditions for the percentage of convenience sensitive customers suggest are $\delta < \frac { ( 1 - m ) \overline { { { \mathsf { p e } } } } _ { 3 } \ + \ F _ { n } ( t ) ( m \varepsilon _ { 1 } \ + \ L _ { n } ) - c _ { b i o } - F _ { b i o } ( t ; \overline { { { \mathsf { s } } } } ) \big [ m \mathsf { p e } _ { 4 } \ + \ ( 1 - m ) \mathsf { \varepsilon } _ { 3 } \overline { { \varepsilon _ { 4 } \mathsf { p } } } ^ { 2 } \ + \ L _ { b i o } \big ] } { m \mathsf { c } _ { \circ } \lceil 1 - F \cdot \mathrm {  ~ \scriptstyle \gamma ~ } ( t \cdot \overline { { { \mathsf { s } } } } ) \mathsf { n c } _ { \circ } \ . \ \ \rfloor }$ mε<sub>2</sub> 1−F  t;s ρε<sub>4</sub> when comparing two one-factor authentication systems and c −c + 1−m ρ ε −ε −F t;s m + 1−m ρε ρε + L + F t m + 1−m ρε ρε + L m ε −ε + F t mρε ε −F t;s mρε ε when comparing two two-factor authentication systems. These conditions exist only when the expected costs and losses of the original system are larger than those for the new system before considering the impact of inconvenience. In other words, before we consider the impact of inconvenience, all the other expected costs and losses must be relatively smaller. If convenience is the main concern when deciding switching to the new authentication system, the provider should <sup>fi</sup>rst evaluate whether the new system could ful<sup>fi</sup>ll the needs of its potential customers, instead of the existing customers. Otherwise, the new system is not preferable and no need to consider the privacy issues. Fig. 1c illustrates this condition $( m = 0 . 5 , \rho = 0 . 8 ,$ $\varepsilon _ { 5 } = \varepsilon _ { 6 } = \varepsilon _ { 7 } = \varepsilon _ { 8 } = \varepsilon _ { 9 } = 0 . 8 , \varepsilon _ { 1 0 } = 0 . 5 , L _ { n n } = L _ { n b i o } = 0 . 8 , c _ { n n } = c _ { n b i o } = 0 . 8$ $F _ { n n } ( t ) = F _ { n b i o } ( t ; \bar { s } ) = 0 . 7 5 )$ . Accordingly,

Proposition 2. If the service or product provider operates in the market where convenience is the major issue, the provider should focus on whether the new system could satisfy the needs of potential customers before evaluating the impact of privacy when deciding adopting the new authentication system.

Fourth, the current market share of the provider must be larger than $\begin{array} { r } { c _ { b i o } - \mathsf { p g } _ { 3 } + F _ { b i o } ( t ; \overline { { s } } ) \mathsf { p } ^ { 2 } \mathsf { E } _ { 3 } \mathsf { E } _ { 4 } + F _ { b i o } ( t ; \overline { { s } } ) w _ { b i o 1 } \alpha - F _ { n } ( t ) w _ { n 1 } \alpha \qquad } \\ { F _ { b i o } ( t ; \overline { { s } } ) ( \mathsf { p } ^ { 2 } \mathsf { E } _ { 3 } \mathsf { E } _ { 4 } + \mathsf { p } \dot { \alpha } _ { 2 } \mathsf { E } _ { 4 } - \mathsf { p } \mathsf { E } _ { 4 } ) + F _ { n } ( t ) \mathsf { E } _ { 1 } - \hat { \delta } \mathsf { E } _ { 2 } - \mathsf { p } \mathsf { E } _ { 3 } - F _ { b i o } ( t ; \overline { { s } } ) w _ { b i o 2 } + F _ { n } ( t ) w _ { n 2 } } \end{array}$ (or larger than $\begin{array} { r l } & { \frac { c _ { n b i o } - c _ { n n } + \wp ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) - F _ { n n } ( t ) ( \rho ^ { 2 } \varepsilon _ { 6 } \varepsilon _ { 7 } + w _ { n n 1 } \alpha ) + F _ { n b i o } ( t ; \overbar { s } ) ( \rho ^ { 2 } \varepsilon _ { 9 } \varepsilon _ { 1 0 } + w _ { n b i o 1 } \alpha ) } { [ \rho ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) + \hat { \omega } ( \varepsilon _ { 5 } - \varepsilon _ { 8 } ) - F _ { n n } ( t ) \rho \varepsilon _ { 7 } ( \rho \varepsilon _ { 6 } + \hat { \omega } \varepsilon _ { 5 } - 1 ) + F _ { n b i o } ( t ; \overbar { s } ) ( \rho \varepsilon _ { 1 0 } ( \rho \varepsilon _ { 9 } + \hat { \omega } \varepsilon _ { 8 } - 1 ) ] } } \\ & { [ - F _ { n b i o } ( t ; \overbar { s } ) w _ { n b i o 2 } + F _ { n n } ( t ) w _ { n n 2 } \qquad } \end{array}$ for the two-factor case) for the new authentication system to be more preferable. The threshold for the market share that makes the new system more preferable increases as the additional implementation costs increase. The market share (or the value of the existing customers) should be large enough because this value determines the net value change from the customers after adopting the new authentication system which makes the new system more preferable. If the provider chooses a new system with the characteristics that are more expensive, the provider needs to have a larger market value of customers to justify the spending. This can be illustrated as in Fig. 1d $( c _ { n n } = c _ { n b i o } = 0 . 8 , \ \delta = 0 . 8 , \ \rho = 0 . 8 ,$ $\varepsilon _ { 5 } = \varepsilon _ { 6 } = \varepsilon _ { 7 } = \varepsilon _ { 8 } = 0 . 8 , \varepsilon _ { 9 } = \varepsilon _ { 1 0 } = 0 . 5 , L _ { n n } = L _ { n b i o } = 0 . 8 , F _ { n n } ( t ) =$ $F _ { n b i o } ( t ; \bar { s } ) = 0 . 7 5$ . However, in the real world cases, we do see that small market participants adopt the same new authentication system as the large market participants do. This seems to be contradicted with our result because the adoption of a new authentication system is not bene<sup>fi</sup>cial for small market participants. On the contrary, the conditions help explain this observation. These small market participants can in fact reduce the impact of the net change of customer value by adopting the same authentication system as the large market participants do especially when the majority of the customers are privacy sensitive. In this case, the customers do not have other alternatives of authentication systems among the providers. Therefore, the small market participants can justify the spending by the reduced out<sup>fl</sup>ow of customers toward other providers' new authentication system and the reduced probability of system failure especially when the adoption of authentication system is mandatory. Speci<sup>fi</sup>cally, when the adoption of two- or multi-factor authentication system is mandatory, small market participants can adopt the same system as the large market participants do. For example. when financial institutions adopt new authentication systems in response to FFIEC, they tend to choose those adopted by large <sup>fi</sup>nancial institutions. By doing so, they can not only ascertain their selection is acceptable by the regulator but also avoid possible losses from the switch in customers given similar institutions all adopt the same authentication system.

Proposition 3. Other things being equal, market participants with larger market share (larger than c ρε + F t; s ρ<sup>2</sup>ε ε + F t; s w α F t w α F t; s ρ<sup>2</sup> ε ε + ρδε ε −ρε + F t ε −δε −ρε −F t; s w + F t w (or larger than $\begin{array} { r l } & { c _ { n b i o } - c _ { n n } + \mathrm { p } ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) - F _ { n n } ( t ) \big ( \mathrm { \rho } ^ { 2 } \varepsilon _ { 6 } \varepsilon _ { 7 } + w _ { n n 1 } \alpha \big ) + F _ { n b i o } ( t ; \overline { { s } } ) \big ( \mathrm { \rho } ^ { 2 } \varepsilon _ { 9 } \varepsilon _ { 1 0 } + w _ { n b i o 1 } \alpha \big ) } \\ & { \left[ \mathrm { \rho } ( \varepsilon _ { 6 } - \varepsilon _ { 9 } ) + \hat { \mathrm { \rho } } ( \varepsilon _ { 5 } - \varepsilon _ { 8 } ) - F _ { n n } ( t ) ) \mathrm { e } \varepsilon _ { 7 } ( \mathrm { \rho } \varepsilon _ { 6 } + \hat { \mathrm { \delta } } \varepsilon _ { 5 } - 1 ) + F _ { n b i o } ( t ; \overline { { s } } ) \mathrm { \rho } \varepsilon _ { 1 0 } ( \mathrm { \rho } \varepsilon _ { 9 } + \hat { \mathrm { \delta } } \varepsilon _ { 8 } - 1 ) \right] } \\ & { - F _ { n b i o } ( t ; \overline { { s } } ) w _ { n b i o 2 } + F _ { n n } ( t ) w _ { n n 2 } } \end{array}$ for the two-factor case) can adopt the new authentication system by balancing the costs and expected losses with the net change of customer value.

Last, the expected losses resulting from the failure of the new authentication system should not exceed $F _ { n } ( t ) ( V _ { n } + L _ { n } ) { - } c _ { b i o } -$ $V _ { n e t _ { b } i o } - F _ { b i o } ( t ; \bar { s } ) V _ { b i o } ~ ( \mathrm { o r } ~ c _ { n n } - c _ { n b i o } ~ + ~ V _ { n e t _ { n } n } - V _ { n e t _ { n } b i o } - F _ { n b i o } ( t ; \bar { s } ) V _ { n b i o } ~ + ~$ $F _ { n n } ( t ) ( V _ { n n } + L _ { n n } )$ for the two-factor case) in order to make the new authentication system more preferable. If we plot the relation between the expected losses and the total expected costs and losses (C), the <sup>fi</sup>gure will be similar to Fig. 1a. This result, though seems obvious, has implication for public policies. In order to make the new system more preferable, one way is to relatively (comparing to the original system) lower the penalty and the compensation to customers associated with the new system once the new system fails. The other way is to relatively increase the penalty and the compensation to customers if the provider determines to keep the original authentication system. In other words, the providers could be penalized by implementing a less secure authentication system (in terms of the probability of system failure). By doing so, the relatively lowered penalty for the new system creates an environment where the new authentication is more attractive than the original one. The regulators could then force the provider to adopt a new system. Second, as mentioned earlier, the loss increases with the level of information the customers have to provide. If a <sup>fi</sup>rm needs to collect more additional information when implementing the new authentication system, other things being equal, the new system is less preferable. Formally,

Proposition 4. Other things being equal, by reducing the penalty associated with the new authentication system, the regulator is able to encourage the providers to adopt a more secure authentication system (in terms of the probability of system failure).

From the above propositions, we also notice that the composition of customers and the change in the customer base are important factors when determining authentication systems. This observation leads us to argue that an online service or product provider's does not necessarily have to choose either one-factor or two-factor authentication systems. Instead, it could have both at the same time depending on the customers' preferences and the nature of the service or product category. Speci<sup>fi</sup>cally, for different group of customers, the provider can implement different authentication systems in order to <sup>fi</sup>t the preferences of different group of customers.

## 5. Conclusions and discussion

This study compares the expected costs and losses of different authentication methods. The results show the key factors and several insights for online service or product providers when adopting a new authentication system. In order to make the new authentication system more preferable, the managers need to take into account the additional implementation costs, the current market share and the composition of customers. We show that if the provider chooses an expensive new system, the provider needs to have a larger market share to justify the spending. Also, the conditions demonstrate that government can encourage the use of a more secure authentication system by adjusting the penalty a <sup>fi</sup>rm faces when the system fails. Finally, it might be appropriate for a <sup>fi</sup>rm to implement both onefactor and two- or multi-factor authentication systems depending on the customers' preferences.

The contribution of this study can be two folds. First, this study adds to the literature on authentication systems. To the best knowledge of the authors, the paper is the <sup>fi</sup>rst paper attempting to understand the decision of authentication systems from an economic setting instead of proposing technical solutions. More importantly, this study demonstrates that all kinds of authentication systems can be modeled into two broad categories: non-repairable and biometric. Although the parameters associated with different technology solutions vary, this generalization allows us to analyze the decision without any concern about the complexity of various authentication systems which can also be used for future studies about authentication systems. Second, for managers, this study provides suggestions when considering adopting a new authentication system. As discussed in Section $^ { 4 , }$ all the elements need to be taken into account when determining whether the new system is worth engaging. More importantly, the rules we extract are general enough for managers to consider regarding various authentication systems. These general rules can also be used even for multi-factor authentication systems the <sup>fi</sup>rm might adopt in the future.

There are several possible future extensions. First, as mentioned in the text, we choose to address our research question in a more static

## Appendix A. Variable de<sup>fi</sup>nitions

setting. There is still room for modeling competitors using game theory setting and better capturing the effect of customer switching. Second, with the improvement of the technology and the standardization of the devices, the biometric authentication can have a totally different status, regardless of the accuracy, the costs and even the convenience. In the near future, it will be interesting to discuss speci<sup>fi</sup>cally on biometric systems in more detail and to consider two or more biometric components combined with each other. Third, we can address the authentication issue from the users' perspectives and investigate how users perceive different systems and what the impacts on their adoption behavior are. Finally, as mentioned in the Introduction of the paper, we do not investigate the optimal decision for one-factor and two-factor authentication systems given the complex nature of authentication system speci<sup>fi</sup>cations. Based on the results of the paper, one can extend to the optimal decision of authentication systems in the future.

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>m</td><td>The online service or product provider&#x27;s current market share which is defined between zero and one. It can be interpreted as the total value the provider can get from the customers comparing to other providers.</td></tr><tr><td>α</td><td>The percentage of information a customer needs to provide in order to complete the transaction which is defined between zero and one.</td></tr><tr><td>L</td><td>The compensation paid to customers or the legal penalty or fine when system fails.</td></tr><tr><td>ρ</td><td>Proportion of privacy sensitive customers which is defined between zero and one.</td></tr><tr><td>δ</td><td>Proportion of convenience sensitive customers which is defined between zero and one.</td></tr><tr><td>Fn(t)</td><td>The probability of system failure (CDF) of one non-repairable component across time t.</td></tr><tr><td>λ</td><td>Mean-time-to-failure.</td></tr><tr><td>b</td><td>Change of failure rate across time.</td></tr><tr><td>Fnn(t)</td><td>The probability of system failure (CDF) of two non-repairable component across time t.</td></tr><tr><td>ψ</td><td>False acceptance rate (FAR) of a biometric system which is determined by the selected threshold.</td></tr><tr><td>φ</td><td>False rejection rate (FRR) of a biometric system which is determined by the selected threshold.</td></tr><tr><td>s̄</td><td>The threshold for the biometric system.</td></tr><tr><td>Fbio(t;s̄)</td><td>The probability of system failure (CDF) of biometric system across time t.</td></tr><tr><td>wFRR</td><td>The weight for FRR when choosing biometric systems.</td></tr><tr><td>wFAR</td><td>The weight for FAR when choosing biometric systems.</td></tr><tr><td>Fnbio(t;s̄)</td><td>The probability of system failure (CDF) of one non-repairable component and one biometric component across time t.</td></tr><tr><td>w1, w2</td><td>The weights of α and m, respectively, for L.</td></tr><tr><td>C</td><td>The expected costs and losses.</td></tr><tr><td>c</td><td>Implementation costs of the system.</td></tr><tr><td>V</td><td>The loss of the value of customers as the system fails.</td></tr><tr><td>ε</td><td>The percentage change of customers, which depends on different systems. Therefore, we use ten different percentages for our analysis. ε1(ε4, ε7, ε10) represents the percentage of customer a provider could lose when system fails under the base case (the biometric system, two non-repairable component system, one non-repairable component and one biometric system). ε2(ε5, ε8) represents the percentage of convenient sensitive customer a provider could lose when adopting the biometric system (two non-repairable component system, one non-repairable component and one biometric component system). ε3(ε6, ε9) represents the percentage of privacy sensitive customer a provider could attract when adopting the biometric system (two non-repairable component system, one non-repairable component and one biometric component system).</td></tr></table>

## Appendix B. Conditions that make the new authentication system more preferable

Panel A. Adopt the Biometric System

1. Additional implementation costs:

$$
c _ {b i o} <   F _ {n} (t) (V _ {n} + L _ {n}) - F _ {b i o} (t; \bar {s}) (V _ {b i o} + L _ {b i o}) - V _ {n e t \_ b i o}
$$

$$
\text { if } F _ {n} (t) (V _ {n} + L _ {n}) - F _ {b i o} (t; \bar {s}) (V _ {b i o} + L _ {b i o}) - V _ {n e t \_ b i o} > 0
$$

2. Percentage of privacy sensitive customers:

$$
\frac {- Y - \sqrt {Y ^ {2} - 4 X Z}}{2 X} <   \rho <   \frac {- Y + \sqrt {Y ^ {2} - 4 X Z}}{2 X}
$$

$$
X = F _ {b i o} (t; \bar {s}) (1 - m) \varepsilon_ {3} \varepsilon_ {4}
$$

$$
Y = F _ {b i o} (t; \bar {s}) (m \varepsilon_ {4} - m \delta \varepsilon_ {2} \varepsilon_ {4}) + (m - 1) \varepsilon_ {3}
$$

$$
Z = c _ {b i o} + m \delta \varepsilon_ {2} + F _ {b i o} (t; \bar {s}) L _ {b i o} - F _ {n} (t) (m \varepsilon_ {1} + L _ {n})
$$

$$
\text { if } - Y + \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } - Y - \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0
$$

3. Percentage of convenience sensitive customers:

$$
\delta <   \frac {(1 - m) \rho \varepsilon_ {3} + F _ {n} (t) (m \varepsilon_ {1} + L _ {n}) - c _ {b i o} - F _ {b i o} (t ; \bar {s}) \left[ m \rho \varepsilon_ {4} + (1 - m) \varepsilon_ {3} \varepsilon_ {4} \rho^ {2} + L _ {b i o} \right]}{m \varepsilon_ {2} [ 1 - F _ {b i o} (t ; \bar {s}) \rho \varepsilon_ {4} ]}
$$

$$
\text { if } (1 - m) \rho \varepsilon_ {3} + F _ {n} (t) (m \varepsilon_ {1} + L _ {n}) - c _ {b i o} - F _ {b i o} (t; \bar {s}) \left[ m \rho \varepsilon_ {4} + (1 - m) \varepsilon_ {3} \varepsilon_ {4} \rho^ {2} + L _ {b i o} \right] > 0
$$

4. Market share:

$$
m > \frac {c _ {b i o} - \rho \varepsilon_ {3} + F _ {b i o} (t ; \bar {s}) \rho^ {2} \varepsilon_ {3} \varepsilon_ {4} + F _ {b i o} (t ; \bar {s}) w _ {b i o 1} \alpha - F _ {n} (t) w _ {n 1} \alpha}{F _ {b i o} (t ; \bar {s}) (\rho^ {2} \varepsilon_ {3} \varepsilon_ {4} + \rho \delta \varepsilon_ {2} \varepsilon_ {4} - \rho \varepsilon_ {4}) + F _ {n} (t) \varepsilon_ {1} - \delta \varepsilon_ {2} - \rho \varepsilon_ {3} - F _ {b i o} (t ; \bar {s}) w _ {b i o 2} + F _ {n} (t) w _ {n 2}}
$$

if both the denominator and nominator are positive or negative

5. Expected losses:

$$
F _ {b i o} (t; \overline {{s}}) L _ {b i o} <   F _ {n} (t) (V _ {n} + L _ {n}) - c _ {b i o} - V _ {n e t \_ b i o} - F _ {b i o} (t; \overline {{s}}) V _ {b i o}
$$

$$
\text { if } F _ {n} (t) (V _ {n} + L _ {n}) - c _ {b i o} - V _ {n e t \_ b i o} - F _ {b i o} (t; \bar {s}) V _ {b i o} > 0
$$

Panel B. Adopt the Two Non-Repairable Component Authentication System

1. Additional implementation costs:

$$
c _ {n n} <   F _ {n} (t) (V _ {n} + L _ {n}) - V _ {n e t \_ n n} - F _ {n n} (t) (V _ {n n} + L _ {n n})
$$

$$
\mathrm{if} F _ {n} (t) (V _ {n} + L _ {n}) - V _ {n e t \_ n n} - F _ {n n} (t) (V _ {n n} + L _ {n n}) > 0
$$

2. Percentage of privacy sensitive customers:

$$
\frac {- Y - \sqrt {Y ^ {2} - 4 X Z}}{2 X} <   \rho <   \frac {- Y + \sqrt {Y ^ {2} - 4 X Z}}{2 X}
$$

$$
X = F _ {n n} (t) (1 - m) \varepsilon_ {6} \varepsilon_ {7}
$$

$$
Y = F _ {n n} (t) (m \varepsilon_ {7} - m \delta \varepsilon_ {5} \varepsilon_ {7}) - (1 - m) \varepsilon_ {6}
$$

$$
Z = c _ {n n} + m \delta \varepsilon_ {5} + F _ {n n} (t) L _ {n n} - F _ {n} (t) (m \varepsilon_ {1} + L _ {n})
$$

$$
\text { if } - Y + \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } - Y - \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0
$$

3. Percentage of convenience sensitive customers:

$$
\delta <   \frac {- c _ {n n} + (1 - m) \rho \varepsilon_ {6} (1 - F _ {n n} (t) \rho \varepsilon_ {7}) - F _ {n n} (t) (m \rho \varepsilon_ {7} + L _ {n n}) + F _ {n} (t) (V _ {n} + L _ {n})}{m \varepsilon_ {5} (1 - F _ {n n} (t) \rho \varepsilon_ {7})}
$$

$$
\mathrm{if} - c _ {n n} + (1 - m) \rho \varepsilon_ {6} (1 - F _ {n n} (t) \rho \varepsilon_ {7}) - F _ {n n} (t) (m \rho \varepsilon_ {7} + L _ {n n}) + F _ {n} (t) (V _ {n} + L _ {n}) > 0
$$

4. Market share:

$$
m > \frac {c _ {n n} - \rho \varepsilon_ {6} + F _ {n n} (t) \rho^ {2} \varepsilon_ {6} \varepsilon_ {7} + F _ {n n} (t) w _ {n n 1} \alpha - F _ {n} (t) w _ {n 1} \alpha}{- \delta \varepsilon_ {5} - \rho \varepsilon_ {6} - F _ {n n} (t) (\rho \varepsilon_ {7} - \rho \delta \varepsilon_ {5} \varepsilon_ {7} - \rho^ {2} \varepsilon_ {6} \varepsilon_ {7}) - F _ {n} (t) \varepsilon_ {1} - F _ {n n} (t) w _ {n n 2} + F _ {n} (t) w _ {n 2}}
$$

if both the denominator and nominator are positive or negative

5. Expected losses:

$$
F _ {n n} (t) L _ {n n} <   F _ {n} (t) (V _ {n} + L _ {n}) - c _ {n n} - V _ {n e t \_ n n} - F _ {n n} (t) V _ {n n}
$$

$$
\mathrm{if} F _ {n} (t) (V _ {n} + L _ {n}) - c _ {n n} - V _ {n e t \_ n n} - F _ {n n} (t) V _ {n n} > 0
$$

Panel C. Adopt the one non-repairable component and one biometric authentication system

1. Additional implementation costs:

$$
c _ {n b i o} <   F _ {n} (t) \left(V _ {n} + L _ {n}\right) - V _ {\text {net} _ {n} b i o} - F _ {n b i o} (t; \bar {s}) \left(V _ {n b i o} + L _ {n b i o}\right)
$$

$$
\text { if } F _ {n} (t) \left(V _ {n} + L _ {n}\right) - V _ {\text { net } _ {n} \text { bio }} - F _ {\text { nbio }} (t; \bar {s}) \left(V _ {\text { nbio }} + L _ {\text { nbio }}\right) > 0
$$

2. Percentage of privacy sensitive customers:

$$
\frac {- Y - \sqrt {Y ^ {2} - 4 X Z}}{2 X} <   \rho <   \frac {- Y + \sqrt {Y ^ {2} - 4 X Z}}{2 X}
$$

$$
X = F _ {n b i o} (t; \bar {s}) (1 - m) \varepsilon_ {9} \varepsilon_ {1 0}
$$

$$
Y = F _ {n b i o} (t; \bar {s}) (m \varepsilon_ {1 0} - m \delta \varepsilon_ {8} \varepsilon_ {1 0}) - (1 - m) \varepsilon_ {9}
$$

$$
Z = c _ {n b i o} + m \delta \varepsilon_ {8} + F _ {n b i o} (t; \bar {s}) L _ {b i o} - F _ {n} (t) (m \varepsilon_ {1} + L _ {n})
$$

$$
\text { if } - Y + \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } - Y - \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0
$$

3. Percentage of convenience sensitive customers:

$$
\delta <   \frac {- c _ {n b i o} + (1 - m) \rho \varepsilon_ {9} (1 - F _ {n b i o} (t ; \bar {s}) \rho \varepsilon_ {1 0}) - F _ {n b i o} (t ; \bar {s}) (m \rho \varepsilon_ {1 0} + L _ {n b i o}) + F _ {n} (t) (V _ {n} + L _ {n})}{m \varepsilon_ {8} (1 - F _ {n b i o} (t ; \bar {s}) \rho \varepsilon_ {1 0})}
$$

$$
\text { if } - c _ {n b i o} + (1 - m) \rho \varepsilon_ {9} (1 - F _ {n b i o} (t; \bar {s}) \rho \varepsilon_ {1 0}) - F _ {n b i o} (t; \bar {s}) (m \rho \varepsilon_ {1 0} + L _ {n b i o}) + F _ {n} (t) (V _ {n} + L _ {n}) > 0
$$

4. Market share:

$$
m > \frac {c _ {n b i o} - \rho \varepsilon_ {9} + F _ {n b i o} (t ; \bar {s}) \rho^ {2} \varepsilon_ {9} \varepsilon_ {1 0} + F _ {n b i o} (t ; \bar {s}) w _ {n b i o 1} \alpha - F _ {n} (t) w _ {n 1} \alpha}{- \delta \varepsilon_ {8} - \rho \varepsilon_ {9} - F _ {n b i o} (t ; \bar {s}) (\rho \varepsilon_ {1 0} - \delta \rho \varepsilon_ {8} \varepsilon_ {1 0} - \rho^ {2} \varepsilon_ {9} \varepsilon_ {1 0}) + F _ {n} (t) \varepsilon_ {1} - F _ {n b i o} (t ; \bar {s}) w _ {n b i o 2} + F _ {n} (t) w _ {n 2}}
$$

if both the denominator and nominator are positive or negative

5. Expected losses:

$$
F _ {n b i o} (t; \bar {s}) L _ {n b i o} <   F _ {n} (t) (V _ {n} + L _ {n}) - c _ {n b i o} - V _ {n e t \_ b i o} - F _ {n b i o} (t; \bar {s}) V _ {n b i o}
$$

$$
\text { if } F _ {n} (t) (V _ {n} + L _ {n}) - c _ {n b i o} - V _ {n e t \_ b i o} - F _ {n b i o} (t; \bar {s}) V _ {n b i o} > 0
$$

Panel D. Compare two non-repairable component system to one non-repairable component and one biometric authentication system (conditions when one non-repairable component and one biometric system is more preferable)

1. Additional implementation costs:

$$
c _ {n b i o} - c _ {n n} <   V _ {n e t \_ n n} - V _ {n e t \_ n b i o} + F _ {n n} (t) (V _ {n n} + L _ {n n}) - F _ {n b i o} (t; \bar {s}) (V _ {n b i o} + L _ {n b i o})
$$

$$
\text { if } V _ {n e t \_ n n} - V _ {n e t \_ n b i o} + F _ {n n} (t) (V _ {n n} + L _ {n n}) - F _ {n b i o} (t; \bar {s}) (V _ {n b i o} + L _ {n b i o}) > 0
$$

2. Percentage of privacy sensitive customers:

$$
\frac {- Y - \sqrt {Y ^ {2} - 4 X Z}}{2 X} <   \rho <   \frac {- Y + \sqrt {Y ^ {2} - 4 X Z}}{2 X}
$$

$$
X = F _ {n b i o} (t; \bar {s}) (1 - m) \varepsilon_ {9} \varepsilon_ {1 0} - F _ {n n} (t) (1 - m) \varepsilon_ {6} \varepsilon_ {7}
$$

$$
\begin{array}{c} Y = F _ {n b i o} (t; \bar {s}) (m \varepsilon_ {1 0} - m \delta \varepsilon_ {8} \varepsilon_ {1 0}) + (1 - m) (\varepsilon_ {6} - \varepsilon_ {9}) - F _ {n n} (t) \\ (m \varepsilon_ {7} - m \delta \varepsilon_ {5} \varepsilon_ {7}) \end{array}
$$

$$
Z = c _ {n b i o} - c _ {n n} + m \delta (\varepsilon_ {8} - \varepsilon_ {5}) + F _ {n b i o} (t; \overline {{s}}) L _ {n b i o} - F _ {n n} (t) L _ {n n}
$$

$$
\text { if } - Y + \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } - Y - \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0 \text { and } \sqrt {Y ^ {2} - 4 X Z} > 0
$$

3. Percentage of convenience sensitive customers:

$$
\delta <   \frac {c _ {n n} - c _ {n b i o} + (1 - m) \rho (\varepsilon_ {9} - \varepsilon_ {6}) - F _ {n b i o} (t ; \bar {s}) [ (m + (1 - m) \rho \varepsilon_ {9}) \rho \varepsilon_ {1 0} + L _ {n b i o} ]}{m (\varepsilon_ {8} - \varepsilon_ {5}) + F _ {n n} (t) m \rho \varepsilon_ {5} \varepsilon_ {7} - F _ {n b i o} (t ; \bar {s}) m \rho \varepsilon_ {8} \varepsilon_ {1 0}} + \frac {F _ {n n} (t) [ (m + (1 - m) \rho \varepsilon_ {6}) \rho \varepsilon_ {7} + L _ {n n} ]}{m (\varepsilon_ {8} - \varepsilon_ {5}) + F _ {n n} (t) m \rho \varepsilon_ {5} \varepsilon_ {7} - F _ {n b i o} (t ; \bar {s}) m \rho \varepsilon_ {8} \varepsilon_ {1 0}}
$$

$$
\mathrm{if} c _ {n n} - c _ {n b i o} + (1 - m) \rho (\varepsilon_ {9} - \varepsilon_ {6}) - F _ {n b i o} (t; \bar {s}) [ (m + (1 - m) \rho \varepsilon_ {9}) \rho \varepsilon_ {1 0} + L _ {n b i o} ] + F _ {n n} (t) [ (m + (1 - m) \rho \varepsilon_ {6}) \rho \varepsilon_ {7} + L _ {n n} ] > 0
$$

4. Market share:

$$
m > \frac {c _ {n b i o} - c _ {n n} + \rho (\varepsilon_ {6} - \varepsilon_ {9}) - F _ {n n} (t) \left(\rho^ {2} \varepsilon_ {6} \varepsilon_ {7} + w _ {n n 1} \alpha\right) + F _ {n b i o} (t ; \bar {s}) \left(\rho^ {2} \varepsilon_ {9} \varepsilon_ {1 0} + w _ {n b i o 1} \alpha\right)}{\left[ \begin{array}{l} \rho (\varepsilon_ {6} - \varepsilon_ {9}) + \delta (\varepsilon_ {5} - \varepsilon_ {8}) - F _ {n n} (t) \rho \varepsilon_ {7} (\rho \varepsilon_ {6} + \delta \varepsilon_ {5} - 1) + F _ {n b i o} (t ; \bar {s}) \rho \varepsilon_ {1 0} (\rho \varepsilon_ {9} + \delta \varepsilon_ {8} - 1) \\ - F _ {n b i o} (t ; \bar {s}) w _ {n b i o 2} + F _ {n n} (t) w _ {n n 2} \end{array} \right]}
$$

if both the denominator and nominator are positive or negative

5. Expected losses:

$$
F _ {n b i o} (t; \bar {s}) L _ {n b i o} <   c _ {n n} - c _ {n b i o} + V _ {n e t \_ n n} - V _ {n e t \_ n b i o} - F _ {n b i o} (t; \bar {s}) V _ {n b i o} + F _ {n n} (t) (V _ {n n} + L _ {n n})
$$

$$
\text { if } c _ {n n} - c _ {n b i o} + V _ {n e t \_ n n} - V _ {n e t \_ n b i o} - F _ {n b i o} (t; \bar {s}) V _ {n b i o} + F _ {n n} (t) \quad (V _ {n n} + L _ {n n}) > 0
$$

## References

[1] B. Aboba, L. Blunk, J. Vollbrecht, J. Carlson, H. Levkowetz, Extensible Authentication Protocol (EPA), The Internet Engineering Task Force-Request for Comments 2004.

[2] M.T. Akçura, K. Srinivasan, Research note: customer intimacy and cross-selling strategy, Management Science 51 (6) (2005) 1007–1012.

[3] R. Anderson, Why information security is hard — an economic perspective, Computer Security Applications Conference, New Orleans, Louisiana, 2001.

[4] K. Baum, Identity theft, U.S. Department of Justice, 2004.

[5] A. Bhargav-Spantzel, A. Squicciarini, E. Bertino, Establishing and protecting digital identity in federation systems, Journal of Computer Security 13 (3) (2006) 269–300.

[6] A. Bhargav-Spantzel, A. Squicciarini, E. Bertino, Privacy preserving multi-factor authentication with biometrics, Conference on Computer and Communications Security Proceedings of the Second ACM Workshop on Digital Identity Management (2006) 63–72

[7] BioID.com, About FAR, FRR, and EERRetrieved July 8, 2006, from, http://www. bioid.com/sdk/docs/About\_EER.htm2004.

[8] C. Braghin, Biometric authentication, Department of Computer Science, University of Helsinki, 2001, Retrieved July 8, 2006, from, http://www.avanti.ltol.org.

[9] Biometrics Bromba, Biometric FAQRetrieved July 9, 2006, from, http://bromba com/faq/biofaq.htm2006.

[10] J. Camenisch, A. Lysyanskaya, Ef<sup>fi</sup>cient non-transferable anonymous multi-show credential system with optional anonymity revocation, in: B. P<sup>fi</sup>tzmann (Ed.), Advances in Cryptology — EUROCRYPT 2001 (Santa Barbara California 2001) 2001.

[11] E.M. Caudill, P.E. Murphy, Consumer online privacy: legal and ethical issues, Journal of Public Policy and Marketing 19 (1) (2000) 7–19.

[12] Y. Chen, G. Iyer, Consumer addressability and customized pricing, Marketing Science 21 (2) (2002) 197–208.

[13] G.I. Davida, Y. Frankel, B.J. Matt, 1998 on enabling secure applications through offline biometric identi<sup>fi</sup>cation, Proceedings of the 1998 IEEE Symposium of Privacy and Security, 1998, pp. 148–157.

[14] R. Dhamija, J.D. Tygar, The battle against phishing: dynamic security skins, Proceedings of the 2005 Symposium on Usable Privacy and Security (SOUPS '05), 2005, pp. 77–88.

[15] W. Diffle, P.C. van Oorschot. M.I. Wiener. Authentication and authenticated key exchanges designs, Codes and Cryptography 2 (2) (1992) 357–390.

[16] FFIEC. FFIEC releases guidance on authentication in internet banking environment, Federal Financial Institutions Examination Council, 20058 8 Retrieved July 8, 2006, from. http://www.ffiec.goy/press/pr101205.htm.

[17] FindBiometrics.com, Convenience ys. security: how well do biometrics work-Retrieved July 8, 2006, from, http://www.<sup>fi</sup>ndbiometrics.com/Pages/feature% 20articles/convenience.html2006.

[18] E.R. Foxman, P. Kilcoyne, Information technology, marketing practice, and consumer privacy: ethical issues, Journal of Public Policy and Marketing 12 (1) (1993) 106–119.

[19] B. Gavish, J.H. Gerdes Jr., Anonymous mechanisms in group decision support systems communication, Decision Support Systems 23 (1998) 297–328.

[20] A. Ghose, P.Y. Chen, Personalization vs. privacy: <sup>fi</sup>rm policies, business pro<sup>fi</sup>ts and social welfare, working paper, GSIA, Carnegie Mellon University, 2003.

[21] C. Goodwin, Privacy: recognition of a consumer right, Journal of Public Policy and Marketing 10 (1) (1991) 149–166.

[22] I. H. Hann, K. L. Hui, T. S. Lee and I. P. L. Png, Consumer Privacy and Marketing Avoidance Unpublished manuscript, Department of Information Systems, National University of Singapore (2005).

[23] D.L. Hoffman, T.P. Novak, M. Peralta, Building consumer trust online, Communications of the ACM 42 (4) (1999) 80–85.

[24] K. Hui, I.P.L. Png, The economics of privacy, in: T. Hendershott (Ed.), Handbook of Information Systems and Economics, 471–493, Elsevier, Oxford, UK, 2005.

[25] A.K. Jain, A.R. Ross, S. Prabhakar, An introduction to biometric recognition, IEEE Transactions on Circuits and Systems for Video Technology 14 (1) (2004) 4–20.

[26] A. Liebl, Authentication in distributed systems: a bibliography, ACM SIGOPS, Operating Systems Review 27 (4) (1993) 31–41.

[27] K. Mohan, R. Jain, B. Ramesh, Knowledge networking to support medical new product development, Decision Support Systems 43 (2007) 1255–1273.

[28] B. Ngugi, M. Tremaine, P. Tarasewich, Biometric Keypads: Improving Accuracy through Optimal PIN Selection, Decision Support Systems 50 (4) (2011) 769–776.

[29] G. Nowak, J. Phelps, Understanding privacy concerns, Journal of Direct Marketing 6 (4) (1992) 28–39.

[30] L. O'Gorman, Comparing passwords, tokens, and biometrics for user authentication, Proceedings of the IEEE 91 (12) (2003) 2021–2040.

[31] R.R. Panko, Corporate computer and network security, Prentice-Hall, New Jersey, 2003.

[32] A. Perrig, J. Stankovic, D. Wagner, Security in wireless sensor networks, Communications of the ACM 47 (6) (2004) 53–57

[33] N. Poh, S. Bengio, J. Korczak, A multi-sample multi-source model for biometric authentication, Proceedings of 2002 12th IEEE Workshop on Neural Networks for Signal Processing, 2002, pp. 375–384.

[34] M. Rejman-Greene, Privacy issues in the application of biometrics: an European perspective, in: J.L. Wayman, A.K. Jain, D. Maltoni, D. Maio (Eds.), Biometric Systems: Technology, Design and Performance Evaluation, Sprinter, New York, 2005, pp. 335–359.

[35] A.A. Ross, K. Nandakumar, A.K. Jain, Handbook of multibiometrics, Sprinter, New York, 2006.

[36] G.J. Stigler, An introduction to privacy in economics and politics, Journal of Legal Studies 9 (4) (1980) 623–644.

[37] Y. Sutcu, H.T. Sencar, N. Memon, Authentication/protocols: a secure biometric authentication scheme based on robust hashing, Proceedings of the 7th Workshop on Multimedia and Security (MM&Sec '05), 2005, pp. 111–116.

[38] Z. Tang, J.Y. Hu, M.D. Smith, Gaining trust through online privacy protection: selfregulation, mandatory standards, or caveat emptor, Journal of Management Information Systems 24 (4) (2008) 153–173.

[39] G.B. Tanna, M. Gupta, H.R. Rao, S. Upadhyaya, Information assurance metric development framework for electronic bill presentment and payment systems using transaction and work<sup>fl</sup>ow analysis, Decision Support Systems 41 (2005) 242–261.

[40] J.J. Tardo, K. Alagappan, SPX: global authentication using public key certi<sup>fi</sup>cates Proceedings of IEEE Symposium on Research in Security and Privacy (1991) 232–244.

[41] J. Wang, R. Chen, T. Herath, H.R. Rao, Visual e-mail authentication and identi<sup>fi</sup>cation services: an investigation of the effects on e-mail use, Decision Support Systems 48 (2009) 92–102.

[42] R. Webber, EDP auditing — conceptual foundations and practice, McGraw-Hill, New York, 2001.

[43] WeiBull.com, Analysis reference: reliability, availability, and optimization, ReliaSoft's eTextbook, 2003.

[45] S. H. Wildstrom, New Weapons to Stop Identity Thieves, Business Week (May) (2005) 24.

[44] A. Westin, Privacy and freedom, Atheneum, New York, 1967.

[46] T.Y.C. Woo, S.S. Lam, Authentication for distributed systems, Computer 25 (1) (1992) 39–52.

[47] H.R. Varian, Price discrimination and social welfare, American Economic Review 75 (4) (1985) 870–875.

[48] Y.W. Yun, The ‘123’ of biometric technology, Synthesis Journal (2002) 83–96

Kemal Altinkemer is an Associate Professor at the Krannert Graduate School of Management at Purdue University. He was a Guest Editor in Telecommunication Systems, Information Technology and Management and ECRA. He is an Associate Editor in seven journals. His research interests are in design and analysis of computer networks, infrastructure development, distribution of priorities by using pricing as a tool, infrastructure for E-commerce and pricing of information goods, bidding with intelligent software agents, strategy from Brickandmortar to Clickandmortar business model. He has publications in Operations Research, Operations Research Letters, Management Science, INFORMS Journal on Computing, Transportation Science, EJOR, Computers and OR, Annals of Operations Research, and various conference proceedings.

Tawei Wang is currently an Assistant Professor of Accounting at National Taiwan University. He is a Certi<sup>fi</sup>ed Public Accountant in Taiwan and a Certi<sup>fi</sup>ed Internal Auditor. He received his Ph.D. from Krannert Graduate School of Management, Purdue University. His research interests are information security, IT management, and mandatory and voluntary disclosures. His papers have appeared in several leading conferences and journals including Americas Conference on Information Systems, Paci<sup>fi</sup>c Asia Conference on Information Systems, Workshop on e-Business, Workshop on the Economics of Information Security, Workshop on Information Systems and Economics, Annual Meeting of the Academy of Management, INFORMS, and Decision Support Systems. He has received several awards and honors, including the Krannert Distinguished Teaching Award, the Krannert Outstanding Teaching Award, Purdue Graduate Student Award for Outstanding Teaching, the Purdue Research Foundation Summer Research Grant, and the Bilsland Dissertation Fellowship.
