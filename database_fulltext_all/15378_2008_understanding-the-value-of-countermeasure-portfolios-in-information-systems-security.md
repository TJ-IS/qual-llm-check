---
otero_id: 15378
otero_key: "ZBBMT9WC"
title: "Understanding the Value of Countermeasure Portfolios in Information Systems Security"
authors: "Ram L. Kumar; Sungjune Park; Chandrasekar Subramaniam"
year: "2008"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222250210"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding the Value of Countermeasure Portfolios in Information Systems Security

Ram L. Kumar , Sungjune Park & Chandrasekar Subramaniam

To cite this article: Ram L. Kumar , Sungjune Park & Chandrasekar Subramaniam (2008) Understanding the Value of Countermeasure Portfolios in Information Systems Security, Journal of Management Information Systems, 25:2, 241-280

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222250210

![](/api/attachments/ZBBMT9WC/fulltext/images/84a8f2748fc4623791e16d00976d4b14634196456a02e7ddc1dcb79183717a39.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/ZBBMT9WC/fulltext/images/1f9b6a4195b20589ec0e663a0d0118f14e070bdf7cec06b6397dccdb3c5a9d44.jpg)

Submit your article to this journal

![](/api/attachments/ZBBMT9WC/fulltext/images/9cfc1f54488700eed6d35b0c71f6aecf010d2fc78b0fdcc51c559e9af121769f.jpg)

Article views: 34

![](/api/attachments/ZBBMT9WC/fulltext/images/8824378c18503bc8c534a5cea120a866cb974ff24e4e2c3edc63fe416c41984a.jpg)

View related articles

![](/api/attachments/ZBBMT9WC/fulltext/images/06f567ca1dfe4ece132189f93b0550f853f2615a10fc79a59d50d33ed95f34c3.jpg)

Citing articles: 2 View citing articles

# Understanding the Value of Countermeasure Portfolios in Information Systems Security

Ram L. Kumar , Sun gjune Park , and Chandr asek ar Subr amani am

Ram L. Kumar is a Professor in Belk College of Business Administration, University of North Carolina at Charlotte. He received his Ph.D. in Information Systems from the University of Maryland. He worked for major multinational corporations such as Fujitsu before entering academics. His research has been funded by organizations such as the U.S. Department of Commerce, and organizations in the financial services and energy industries. His current research interests include techniques for evaluating and managing portfolios of IT investments, service science, and knowledge management. His research has been published in Communications of the ACM, Computers and Operations Research, Decision Sciences, Information Resource Management Journal, International Journal of Electronic Commerce, International Journal of Production Research, Journal of Management Information Systems, and others.

Sungjune Park is an Associate Professor in the Department of Business Information Systems and Operations Management at the University of North Carolina at Charlotte. He received his B.S. and M.S. in Management Science from the Korea Advanced Institute of Science and Technology, and his Ph.D. in Business Administration from the State University of New York at Buffalo. His research areas include neural networks applications in business, information security, digital piracy, and supply-chain management. His research has appeared in Data and Knowledge Engineering, Interna tional Journal of Production Research, Journal of Management Information Systems, OMEGA—The International Journal of Management Science, and others.

Chandr as ek ar Subr amaniam is an Assistant Professor in Information Systems at the University of North Carolina at Charlotte. He received his Ph.D. in Business Administration from the University of Illinois at Urbana–Champaign. His research interests include electronic commerce, IT value, information systems security, and open source software development. His research has appeared in Communications of the AIS, Deci sion Support Systems, International Journal of Electronic Commerce, and others.

Abs tr ac t: Organizations are faced with a variety of information security threats and implement several information system security countermeasures (ISSCs) to mitigate possible damage due to security attacks. These security countermeasures vary in their ability to deal with different types of security attacks and, hence, are implemented as a portfolio of ISSCs. A key challenge for organizations is to understand the economic consequences of security attacks relative to the ISSC portfolio implemented. This paper combines the risk analysis and disaster recovery perspectives to build an integrated simulation model of ISSC portfolio value. The model incorporates the characteristics of an ISSC portfolio relative to the threat and business environments and includes the type of attack, frequency of attacks, possible damage, and the extent and time of recovery from damage. The simulation experiments provide interesting insights into the interactions between ISSC portfolio components and characteristics of business and threat environments in determining portfolio value.

Key wor ds and phr as es : business value of IT, economics of IS security, information systems security, IT asset valuation.

Sec ur ity of infor mation s ys tems (IS) is a major concern for organizations. With more and more products and services offered online, there is a growing need for organizations to protect their information and IS from various security threats, including “cyber attacks.” Virus attacks, theft of information, and denial of service (DOS) attacks alone resulted in significant losses according to a recent Computer Security Institute (CSI) survey [17]. In response to these security threats, organizations implement several countermeasures designed to detect threats or minimize damage due to attacks. These countermeasures include antivirus software, firewalls, intrusion detection or prevention, and encryption. Organizations also engage in disaster recovery planning and implement countermeasures, including backups, redundant systems, or disaster recovery contracts with third parties who maintain sophisticated disaster recovery infrastructures, to recover from damage. The set of all countermeasures implemented by an organization can be viewed as an information systems security countermeasure (ISSC) portfolio, with each component of the portfolio interacting with other components dynamically.

A key challenge for organizations is to understand the economic consequences of security attacks relative to the portfolio of countermeasures implemented. These countermeasures should focus on ensuring business continuity despite attacks. These countermeasures, in turn, could be combinations of technologies and business processes. Prior research on IS security economics in management information systems (MIS) has emphasized countermeasures oriented toward threat detection and prevention (risk analysis) [36]. There has been limited research on disaster recovery. The stochastic dominance approach [29] has been used to study different contingency plans if a disaster occurs. To the best of our knowledge, there is no research on the economic benefits of portfolios of security countermeasures that considers threat detection and prevention as well as recovery from disasters concurrently.

The research objective in this paper is to develop a framework to systematically evaluate and understand the value of portfolios of different types of security countermeasures in the context of different threat and business environments. This paper contributes to the growing body of literature on IS security economics in the following ways:

1. It develops a simulation model that considers threat detection, prevention, and recovery from disasters in an integrated manner. Hence, the proposed model complements prior research that has focused either on threat detection and prevention or disaster recovery.

2. It uses a richer parameterization of the different factors that affect IS countermeasure portfolio value than prior research. Modeling this rich set of parameters and their interactions allows researchers and managers to better understand the interactions between business parameters, threat parameters, and countermeasure parameters.

3. B y using a simulation model based on a theory of financial asset valuation, it recognizes that the value of an ISSC portfolio is dynamic. This is consistent with prior MIS research that has emphasized the importance of studying IT investments as dynamically operating in the organizational and environmental contexts [13, 20, 28].

## Overview of IS Security Attacks and IS Security Countermeasures

IS have, by their ver y natur e, been vul ner abl e to misuse and abuse. Plans for disaster management and recovery (e.g., physical security, data backup procedures, and rollback of incomplete database transactions) have been a part of IS manager training. But, with the rapid growth of e-business and the use of the Internet to enable most business processes, organizations have been exposed to security attacks like never before and are increasingly incorporating ISSCs in their strategic IS plans [17].

A security threat is a condition of vulnerability that may lead to an IS being compromised. An attack is the materialization of a security threat or the exploitation of an IS security vulnerability [16].<sup>1</sup> A recent CSI study has identified different types of attacks on organizational IS, including viruses and worms, insider abuse of network access, laptop theft, DOS, system penetration, unauthorized access of IS resources or data, and theft of proprietary information [17]. Other studies have found that theft of proprietary/confidential information, virus, and DOS are the three most important security attacks [14, 15]. These security attacks result in serious negative effects on firms, including loss of confidential information, faulty decisions based on altered data, or loss of business from DOS [16].

There are many security technologies used as countermeasures to address the IS security threats. These include firewall, antivirus, encryption, and intrusion detection systems (IDS). Firewall and encryption protect organizations from information theft. An antivirus product may be combined with a comprehensive management solution, including automatic update and early warning services. An IDS monitors events occurring in a computer system or network and uses anomaly detection or misuse detection to analyze them for suspected intrusions. Anomaly detection builds profiles of normal activities and alerts when monitored activity deviates from normal. Misuse detection constructs patterns of known attacks and alerts when monitored activity matches known pattern [27]. The security technologies are constantly evolving in response to the ever-changing nature of the threats and the novel methods adopted by the threat agents.

Organizations may have multiple countermeasures in place (especially in high-threat environments) and be of the opinion that the weakest countermeasure determines how good the organization’s security is. However, when an organization implements a security portfolio to deal with the threats, the real benefits of the portfolio may not be limited by the weakest countermeasure. The interactions among the countermeasures may result in higher benefits. Conversely, the interactions could reduce the benefits obtainable from the strongest countermeasure. Further, and more important, the benefits of the countermeasures will depend on the business environment and the threat environment. Hence, there is a need to evaluate the benefits from any security portfolio using a comprehensive framework that includes characteristics of the countermeasures, the threats, and the business.

## Literature Review

Our r es earc h buil ds on two s tr eams of l iter atur e in the IS area. The first stream relates to the value of information technology (IT) investments. Studies that have analyzed the business value of IT in organizational contexts have emphasized that the extent of IT use and the context in which IT is used are major determinants of IT value [10, 13, 20]. Hence, it is important to consider the context in which ISSCs are used in order to determine their value.

Another literature stream relates to economic aspects of information security investments. Gordon and Loeb [16] consider an economic model that examines how the vulnerability of information and the potential loss from such vulnerability affect the optimal investment in security. They show that no information security may be justified for extremely high and extremely low levels of vulnerability [16]. An economic model of IDS by Cavusoglu et al. [5] shows that with an optimally configured IDS, the value from such a system is strictly nonnegative and this configuration always deters hackers. The optimal detection rate in this case depends not on the firm’s internal cost parameters, but on the external user parameters. Yue and Çakanyildirim [41] study the optimal mix of reactive and proactive responses in the context of intrusion prevention using an optimal control approach. They show how this optimal mix depends on the values of cost parameters and investigation rate parameters. Arora and Telang [2] illustrate that it is not necessarily beneficial to publicly announce security vulnerabilities. On one hand, public announcements increase pressure on organizations to release patches for security flaws. On the other hand, such announcements increase the arrival rate of attacks even after patches are announced. Other researchers [35] have emphasized the need for econometric modeling of factors that include arrival of attacks to an organization’s IT resources. An interesting stream of research on modeling the intent of attackers in the presence of different types of ISSCs [26, 27] is developing.

Rainer et al. [31] compare qualitative and quantitative methods of assessing risks to an organization’s IT assets and present a systematic approach to assessing risks. Research on the value of IS security recognizes that when using security countermeasures, organizations may have to consider trade-offs and conflicts among their security goals, and it is necessary to evaluate any security portfolio in terms of the corporate IS security priorities [16]. Sun et al. [36] present an information security risk assessment model that includes a more comprehensive definition of risk than prior research. Their model also facilitates modeling of subcomponents of risk and the impact of multiple countermeasures on a particular risk. Arora et al. [3] present a simple method of incrementally evaluating each security countermeasure that is added to the portfolio. They consider the pass-through rates of different countermeasures for each type of threat and emphasize the need for additional research that considers interactions between security countermeasures and threats, possibly based on simulation. Conrad [8] presents a Monte Carlo simulation to understand the value of an organization’s security investments but does not consider multiple security countermeasures and their efficacies for different threat types. In order to better understand the impact of an IS security portfolio, our paper proposes a model of ISSC value that considers the dynamic interactions among an organization’s business environment, threat environment, and characteristics of different types of ISSCs.

## Understanding Different Types of ISSCs and Their Contributions to Business Value

The “val ue” of an or ganization’s infor mation tec hnol ogy infrastructure and applications (ITIA) can be denoted by the net present value (NPV) generated by IT applications that the infrastructure supports [20]. The value of the infrastructure is affected not only by the type of ISSC but also by the manner in which it is used. An infrastructure supporting e-commerce sales transactions on the Web is more valuable when the number of users is high. The value of the organization’s infrastructure and applications varies over time, due to variations in factors such as number of users and number of transactions using it. Hence, we can model ITIA value (IV) as a function of usage (the number of transactions as well as the value of each transaction).

In general, IV can be modeled as a time-dependent variable that follows a stochastic process [20]. Let IV(t) be the NPV of the infrastructure and applications at time t. IV(t) varies over time due to changes in the usage of applications supported, addition of new applications, environmental factors such as the economy and competition, addition of new applications, and other factors.

The change in IV(t) can be conceptualized as being made up of three types of changes—drifts, jumps, and noise—and is modeled as a geometric Brownian motion with drift [20, 37]. Jump events could be positive (value enhancing) or negative (value decreasing). For example, threats such as virus attacks or DOS attacks cause negative jumps. Table 1 provides examples of both positive and negative jump events along with associated benefits and costs.

Figure 1 illustrates the variation of IV(t) resulting from the events such as those described in Table 1 for two infrastructures: an infrastructure with a basic ISSC portfolio (BISSC), and an infrastructure with an advanced ISSC portfolio (AISSC). An AISSC is assumed to provide greater protection from security threats (and hence greater value) than a BISSC. Both types of ISSCs have no effect on events 1 and 2 described in Table 1. However, for the security-related events (3, 4, and 5), an AISSC reduces the magnitude of the negative jumps. Thus, the value added by investing in an AISSC instead of a BISSC is the difference in areas between the two curves (AISSC and BISSC) for some planning horizon T.

Table 1. Illustrative Events Affecting Value of an IT Infrastructure

<table><tr><td></td><td>Jump event</td><td>Benefits</td><td>Costs</td></tr><tr><td>1</td><td>New application implementation</td><td>Value generated by the new application</td><td>Cost of installing the new application on the infrastructure</td></tr><tr><td>2</td><td>Application integration</td><td>Value generated by integration</td><td>Cost of integration</td></tr><tr><td>3</td><td>Denial of service attack</td><td></td><td>Loss in value due to business interruption</td></tr><tr><td>4</td><td>Virus attack</td><td></td><td>Cost of installing patches, downtime, additional user support</td></tr><tr><td>5</td><td>Theft of information</td><td></td><td>Loss in value due to business disruption, loss of current and future business, and potential liability claims</td></tr></table>

![](/api/attachments/ZBBMT9WC/fulltext/images/3aee40b8dee823d25091a10559a51d82b63aafa94a68d7a3c587610471692029.jpg)  
Figure 1. Increased Value Due to an Advanced ISSC (AISSC) Portfolio That Reduces the Magnitude of Negative Jump Events Compared to a Basic ISSC (BISSC) Portfolio

It is important to note that in Figure 1, we have assumed that the effect of the ISSC is to reduce the magnitude of negative jumps. In general, an ISSC can enhance infrastructure value in one or more of the following ways:

![](/api/attachments/ZBBMT9WC/fulltext/images/0e62a54fe96ee8081f40bc51dee4384851fc2992467be64d3b9d3e158d5d892a.jpg)  
Figure 2. Increased Value Due to an AISSC Portfolio That Reduces the Arrival Rate of Negative Events Compared to a BISSC Portfolio

![](/api/attachments/ZBBMT9WC/fulltext/images/7e5fd8ce0cb0059a9b428dce4aeeb82f22fffe3e42d02ed0583e513a8cebc25c.jpg)  
Figure 3. Increased Value Due to an AISSC That Increases the Recovery Rate and Magnitude of Recovery from Negative Events Compared to a BISSC

1. by decreasing the arrival rate of negative events (Figure 2),

2. by decreasing jump sizes for negative events,

3. by reducing the time to recover (or increasing the recovery rate) from negative events (Figure 3), and

4. by providing early warnings of possible security threats and thus increasing the time available to react to security attacks.

Having time to react to a security attack is useful for organizations as it can help them in preparing and prioritizing their security defenses [39]. Early warning, in turn, can result in reduced damage or faster recovery from damage.

Prior research on risk analysis has focused only on (1) and (2) while prior research on disaster recovery has considered (3) after a threat has occurred. The contribution of early warning (which is important for newer security technologies such as IDS) to the value of a security portfolio has not been considered in prior research. Also, these four factors have not been considered concurrently.

We can envisage the timeline from the occurrence of an attack to the time the system is fully recovered, as shown in Figure 4. The timeline is based on the notion that organizations focus on preventing attacks from occurring in the first place. Damage from attacks that have passed through the security defenses are then the focus of recovery. Each type of ISSC can have different types of effects on the attack–recovery timeline. Table 2 illustrates the types of effects that common types of ISSCs can have. It is important to note that these effects are meant to be illustrative and not exhaustive. It is also important to note that ISSCs are not limited to technology investments. They can also take the form of complementary investments in process improvements and training (such as disaster recovery processes and training). Individual countermeasures may have different effects and can be modeled by appropriate parameter values for the different effects.

As seen from Table 2, the interactions and interdependencies between threats, countermeasures, and business environments cannot be fully addressed by analytical models. Hence, we use a simulation-based approach to study ISSC portfolio value.

## Simulation Model

Our s imul ation model c aptur es the ISSC por tfol io val ue by including characteristics of the countermeasures, threats, and the business environment. The model incorporates the four types of effects (reducing the negative jumps, reducing the arrival rates of negative jumps, increasing the recovery rate, and providing early warning) discussed in the previous section.

## Simulation Variables and Parameters

The variables and parameters used in our simulation can be classified into three types: those that relate to the business environment, those that relate to the threat environment, and those that relate to ISSC portfolios. The description of the variables, their distributions, their justifications, and the parameters are given in Table 3.

The planning horizon or lifetime of an ISSC portfolio (T), which is our simulation period, drift rate (a), short-term noise representing volatility of IT infrastructure value $( d z _ { t } )$ , arrival rates of jumps $( \lambda _ { k } )$ , and jump magnitudes $( \mu _ { \boldsymbol { k } } , \sigma _ { \boldsymbol { k } } )$ are the parameters that relate to the business environment. Here $k \left( k = 1 , . . . , K \right)$ represents a business event (such as events 1 and 2 in Table 1).

Another set of parameters is related with attacks: frequency of attacks $( \lambda _ { _ j } )$ , magnitude of damage $( \mu _ { _ { j } } , \sigma _ { _ { j } } )$ , time required to recover from damage $j \left( \mu _ { \tau _ { j } } \right)$ , and magnitude of postrecovery damage $( \mathsf { p } _ { j } ^ { m } , \mathsf { p } _ { j } ^ { a } , \mathsf { p } _ { j } ^ { b } )$ in the absence of countermeasures. Here $j ( j =$ $1 , . . . , J )$ represents an attack type and $\boldsymbol { \rho } _ { j } ^ { m } , \boldsymbol { \rho } _ { j } ^ { a }$ , and $\boldsymbol { \rho } _ { j } ^ { b }$ refer to most likely, optimistic, and pessimistic estimates of the postrecovery damage from attack j (see Table 2). It is important to note that the values of these attack parameters are not independent of the business environment. We use the beta distribution for postrecovery damage $( { \boldsymbol { \rho } } _ { j } )$ in order to incorporate managers’ insights and experiences about their business environment. In general, the beta distribution is used in the absence of data and in distribution of a random proportion [21]. It is common practice for managers to obtain and use several points in a probability distribution via their judgmental assessment in order to estimate mean and variance [19]. The beta distribution with three estimates used in our study is also widely used in project management. The time required to recover from damage (t ) is assumed to follow an exponential distribution, which has been used to model disaster recovery times for computer and disk systems [9, 11].

![](/api/attachments/ZBBMT9WC/fulltext/images/b53aa4a664a611f07cc53c67935991a313a3d7fc326f742a70c8b73cc59663a1.jpg)  
Figure 4. Attack–Recovery Timeline

Table 2. Damage Mitigating Effects of Common ISSCs

<table><tr><td rowspan="2">Countermeasure</td><td colspan="4">Effects of countermeasure on</td></tr><tr><td>Attack arrival rate</td><td>Attack loss magnitude</td><td>Recovery magnitude</td><td>Recovery rate</td></tr><tr><td>Firewall</td><td>↓ (theft, DOS)</td><td>↓ (DOS)</td><td></td><td></td></tr><tr><td>Encryption</td><td></td><td>↓ (theft)</td><td>↑ (theft)</td><td>↑ (theft)</td></tr><tr><td>Intrusion detection system</td><td>↓ (theft, DOS)</td><td>↓ (theft)</td><td>↑ (theft, DOS, virus)</td><td>↑ (theft, DOS, virus)</td></tr><tr><td>Antivirus products/services</td><td>↓ (virus, theft)</td><td>↓ (virus)</td><td>↑ (virus)</td><td>↑ (virus)</td></tr><tr><td>Business continuity contract</td><td></td><td></td><td>↑ (theft, DOS, virus)</td><td>↑ (theft, DOS, virus)</td></tr><tr><td colspan="5">Notes: ↑ denotes a positive effect; ↓ denotes a negative effect</td></tr></table>

In addition to the environmental and threat parameters, the simulation requires countermeasure parameters for evaluation of ISSC portfolios. We define each countermeasure as a bundle of parameters: p, q, r, and s (matrices of countermeasure effectiveness). These parameters represent the countermeasures’ effectiveness on attack arrivals $( \boldsymbol { p } _ { } _ { i j } ^ { } )$ , on expected damage $( q _ { i j } ^ { a } , q _ { i j } ^ { b } , q _ { i j } ^ { m } )$ , on recovery time $( s _ { i j } ^ { a } , s _ { i j } ^ { b } , s _ { i j } ^ { m } )$ , and on recovery magnitude $( r _ { i j } ^ { a } , r _ { i j } ^ { b } , r _ { i j } ^ { m } )$ . Here $i ( i = 1 , . . . , I )$ represents a countermeasure. Since the effectiveness values of countermeasures are proportions, we assume that these parameters follow beta distributions as well. Commercially available IS security products $( \mathrm { e . g . }$ , a firewall or IDS) can be denoted by appropriate values of each parameter.

<sub>.</sub> <sub>Parameters</sub> U<sup>sed</sup> <sup>in</sup> <sup>the</sup> <sup>Sim</sup>

<table><tr><td>Type</td><td>Parameter</td><td>Random variable or underlying stochastic process</td><td>Distribution used in simulation model</td><td>Justification</td></tr><tr><td rowspan="5">Business environment</td><td>T: lifetime of ISSC; simulation period</td><td>Constant</td><td></td><td></td></tr><tr><td>α: drift rate</td><td>Constant</td><td></td><td></td></tr><tr><td>σz: instantaneous variance</td><td>dz, Weiner</td><td>Normal</td><td>Similar to prior research on IT value [1, 20]</td></tr><tr><td>λk: arrival rate of jump type k</td><td>Ak(t): Poisson</td><td>Exponential for interarrival time</td><td>Similar to prior research on IT value [1, 20]</td></tr><tr><td>μk, σk: scale and shape parameters of yk, lnyk ~ N(μk, σk2)</td><td>ak(t) = yk/IV(t)</td><td>Lognormal for yk</td><td>Similar to prior research on IT value [1, 20]</td></tr><tr><td rowspan="3">Threat environment</td><td>λj: arrival rate of threat type j</td><td>Tj(t): Poisson</td><td>Exponential</td><td>Commonly used in IS security and network traffic modeling</td></tr><tr><td>μj, σj: scale and shape parameters of xj, lnxj ~ N(μj, σj2)</td><td>θj(t) = (1 - xj)/IV(t)</td><td>Lognormal for xj</td><td>Similar to insurance literature on threats [22]</td></tr><tr><td>ρjm, ρja, ρbm: most likely, optimistic, and pessimistic estimates of postrecovery damage</td><td>ρj</td><td>Beta</td><td>Commonly used in risk analysis and project management when managerial estimates are needed in the absence of other information [19, 21]</td></tr></table>

<table><tr><td></td><td> $\mu_{\tau_j}$ : mean time required to recover from damage  $j$ </td><td> $\tau_j$ </td><td>Exponential</td><td>Similar to literature recovery from failure of computer systems and storage devices [9, 11, 38]</td></tr><tr><td rowspan="4">Countermeasure effectiveness</td><td> $p_{ij}$ : probability of not preventing a damage  $j$  with countermeasure  $i$ (i.e., ineffectiveness of counterrmeasure  $i$  on threat  $j$ )</td><td> $X(1 \text{ or } 0)$ </td><td>Bernoulli</td><td>Similar to other computer security literature (e.g., worms) [25]</td></tr><tr><td> $q_{ij}^m, q_{ij}^a, q_{ij}^b$ : most likely, optimistic, and pessimistic estimates of effect of countermeasure  $i$  on  $\theta$ </td><td> $q_{ij}$ </td><td>Beta</td><td>Similar to  $\rho_j^m, \rho_j^a, \rho_j^b$ </td></tr><tr><td> $r_{ij}^m, r_{ij}^a, r_{ij}^b$ : most likely, optimistic, and pessimistic estimates of effect of countermeasure  $i$  on  $\rho_j$ </td><td> $r_{ij}$ </td><td>Beta</td><td>Similar to  $\rho_j^m, \rho_j^a, \rho_j^b$ </td></tr><tr><td> $s_{ij}^m, s_{ij}^a, s_{ij}^b$ : most likely, optimistic, and pessimistic estimates of effect of countermeasure  $i$  on  $\tau_j$ </td><td> $s_{ij}$ </td><td>Beta</td><td>Similar to  $\rho_j^m, \rho_j^a, \rho_j^b$ </td></tr></table>

Figure 5 illustrates the different types of effects that an ISSC can have. In the absence of countermeasure i, an attack j could result in a damage of $\theta _ { j ^ { \prime } }$ . Once the damage has occurred, the recovery time, in the absence of any countermeasure, is denoted by $\tau _ { j } .$ In general, recovery from damage (indicated by solid inclined line BC) need not be complete and the value of $I V ( t )$ after recovery is $( 1 - \boldsymbol \rho _ { j } ) \boldsymbol \theta _ { j }$ in the absence of any countermeasure. The presence of the countermeasure could reduce damage to $q _ { i j } \theta _ { j } \left( \mathrm { A D } \right)$ . The countermeasure could also reduce recovery time from $\tau _ { j } ^ { \mathrm { \phantom { } } } \mathrm { t o } s _ { i j } ^ { \phantom { } } \tau _ { j } ^ { \mathrm { \phantom { } } } ( \mathrm { D E } )$ . Some countermeasures could reduce postrecovery damage from $\rho _ { j } q _ { i j } \theta _ { j } \mathrm { t o } \rho _ { j } r _ { i j } q _ { i j } \theta _ { j }$ . The dashed and dotted line (DF) shows the recovery path in the presence of a countermeasure. Early warning provided by some countermeasures is reflected in reduced recovery time and reduced damage after recovery.

One of the assumptions in our model is that the countermeasures in the security portfolio act in sequence while dealing with the attack. Only the attacks and the damage that escape the first countermeasure are faced by the following countermeasure in the portfolio. Thus, when there are multiple countermeasures deployed in a portfolio, the effects of the various countermeasure parameters are as follows.

The parameter $p _ { i j }$ represents the proportion of type j attacks that pass through countermeasure $j .$ For example, assume that there were 100 attacks of type $j$ and countermeasure 1 has a value of $p _ { _ { 1 j } } = 0 . 4$ . In this case, 40 percent of the attacks of type j (i.e., 40 attacks) will pass through countermeasure 1. Thus, countermeasure $2$ will face 40 attacks of type j. If countermeasure 2 has a value of $p _ { _ { 2 j } } { = } 0 . 3$ , then only 12 attacks of type $j \left( \mathrm { i . e . , } 0 . 3 * 4 0 \right)$ will pass through countermeasure 2. Thus, the overall pass-through rate of attack type j through countermeasures 1 and 2 is $p _ { 1 j } p _ { 2 j }$

The parameter $q _ { i j }$ of a countermeasure i represents the countermeasure’s capability to reduce the damage from $\boldsymbol { \theta } _ { { i } }$ to $q _ { i j } \theta _ { j }$ . Using the logic similar to the effects of $p _ { i j }$ , we can show that the net damage because of the presence of two countermeasures with $q _ { 1 j }$ and $q _ { 2 j }$ will be $q _ { 1 j } q _ { 2 j } \theta _ { j }$ . For example, suppose that a theft attack can cause a damage of \$10 million to the organization and that there are two countermeasures, IDS $( i = 1 )$ and encryption $( i = 2 )$ , used by the organization. Let us further suppose that $q _ { 1 j } = 0 . 2$ and $q _ { 2 i } = 0 . 3$ . According to our assumption of sequential processing of the attack, the IDS will provide us the early warning necessary to reduce the damage to 20 percent of the original damage (in the absence of IDS). The resultant damage is now \$2 million ${ { \left( { { q } _ { 1 j } } ^ { * } \right. } ^ { } }$ \$10 million). The encryption countermeasure is acting only on this damage. After applying the damage-reducing effects of encryption, the net damage is \$0.6 million (i.e., $q _ { 2 j }$ \* \$2 million or $q _ { 1 j } q _ { 2 j } \ast \$ 10$ million).

The recovery capabilities affect the postrecovery damage and recovery time after damage has been caused by an attack. In the absence of recovery capabilities provided by the countermeasures, the postrecovery damage due to an attack j will be $\boldsymbol { \rho } _ { j } \Pi _ { i } q _ { i j } \boldsymbol { \theta } _ { j }$ and the time to recover from the damage under normal circumstance will be $\tau _ { j } .$ . The damage recovery capability $r _ { i j }$ of countermeasure i will help reduce the damage to $r _ { i j } \mathsf { p } _ { j } \Pi _ { i } q _ { i j } \theta _ { j }$ The recovery time capability $s _ { i j }$ will reduce the net recovery time from $\boldsymbol { \tau } _ { \mathrm { { \scriptscriptstyle i } } }$ to $s _ { i j } \tau _ { i j } .$ . Consider the recovery process when there are two countermeasures $( i = 1 , 2 )$ in the portfolio (e.g., a backup system and an antivirus). Under our assumptions, the first countermeasure helps reduce the postrecovery damage from $r _ { j } \Pi _ { { i } } q _ { { i } { j } } \Theta _ { { j } } \tan { r _ { { 1 } { j } } } \mathsf { p } _ { j } \Pi _ { { i } } q _ { { i } { j } } \Theta _ { { j } }$ This is the damage faced by the second countermeasure, which further reduces the postrecovery damage to $r _ { 1 j } r _ { 2 j } \mathsf { p } _ { j } \Pi _ { i } q _ { i j } \mathsf { \theta } _ { j }$ . Suppose we have 100 files damaged due to a virus attack. Of the 100 damaged files, further suppose that we can recover 20 files without using any countermeasures (i.e., $\rho = 0 . 8 )$ . Hence, the postrecovery damage will be 80 damaged files. Now, using the backup countermeasure with $r _ { _ { 1 j } } = 0 . 4$ , we can recover 48 files resulting in postrecovery damage of 32 damaged files. The antivirus is now required only to recover these 32 damaged files. Assuming $r _ { _ { 2 j } } = 0 . 2 5$ for the antivirus, we can recover 24 of these 32 damaged files resulting in a net damage of eight files. Applying similar logic, the recovery time will be reduced by the first countermeasure from $\tau _ { j } \mathrm { t o } s _ { 1 j } \bar { \tau } _ { j }$ and reduced further by the second countermeasure to $s _ { 1 j } s _ { 2 j } \tau _ { j }$ . In general, for i countermeasures acting in sequence, the overall postrecovery damage from attack j is reduced to $\Pi _ { i } r _ { i j } \mathsf { p } _ { j } \Pi _ { i } q _ { i j } \theta$ and the magnitude of the recovery is $( 1 - \Pi _ { i } r _ { i j } { \mathsf p } _ { j } ) \Pi _ { i } q _ { i j } { \mathsf \theta } _ { j }$ The recovery time is reduced to $( \Pi s _ { i j } ) \tau _ { , }$ j

![](/api/attachments/ZBBMT9WC/fulltext/images/55216e21a9aa657b3d677850ccf869b3dce3c0b71410f8915a2b36b944bc3ca4.jpg)  
Figure 5. The Reduction in Recovery Time and the Net Damage Amount Due to Countermeasure i.

An object-oriented programming language (Java) is used in order to implement the model. Events such as jumps, damages, and recoveries are treated as objects with properties such as type, magnitude, and arrival time. Although the attack–recovery timeline conceptualized in Figure 4 illustrates various events, the events considered in the simulation are arrivals of damages resulting from arrivals of attacks and responses by the countermeasures. From the assumption that arrival process of attacks is a

Poisson process with $\lambda _ { { } _ { j } { } } ,$ we can derive that successful attacks that are not prevented by the countermeasures in the portfolio follow a Poisson process with $\lambda _ { _ j } ( \Pi _ { j } p _ { _ { i j } } )$ . Furthermore, arrivals of damages caused by successful attacks follow the same Poisson process with $\lambda _ { _ j } ( \Pi _ { j } p _ { _ i j } )$ because the departure process of M/G/1 queuing system is also a Poisson process [40]. Therefore, in our simulation model, although every event is triggered by the events of attack arrivals, the damage and recovery events are the only ones that cause changes in IV(t). Our simulation model can be used to track the value $I V ( t )$ over some time period or planning horizon T.

## The Value of an ISSC Portfolio

The value of an ISSC portfolio is conceptualized in our model as the IT infrastructure value with the security portfolio minus the IT infrastructure value without any security portfolio over a finite period of time. However, most IT infrastructures that organizations implement are bundled with some basic level of protection from IT security threats. For example, Windows operating systems come with built-in firewall and automatic updates for security patches. Major software applications are built with password protections and access controls. Most organizations have a basic level of virus protection. Given this situation, it is more meaningful to consider the valueadded by a security portfolio over the basic security technologies that organizations have. When a manager is making a decision about IS security investments, he or she is probably considering adding new security countermeasures to combine with the existing ones or adding more advanced capabilities to existing countermeasures. Thus, the additional value of an ITIA by using an AISSC, compared to a BISSC portfolio, is denoted by $\Delta I V$ and defined as

$$
\Delta I V = \frac {1}{T} \int_ {0} ^ {T} I V _ {(a d v)} (t) - I V _ {(b a s)} (t) d t.\tag{1}
$$

The simulation model is run by setting various values for the parameters in the business environment, threat environment, and the effectiveness of the countermeasures in different ISSC portfolios. Our focus in this paper is to illustrate the relationships between different types of parameters and ISSC portfolio value. Hence, we perform a set of experiments that are described in the following section. Our simulation model can be used to assess the value of a particular ISSC portfolio, to compare different ISSC portfolios, or to understand the impact of different types of parameters (business, threat, ISSC components) on portfolio value.

## Experiments and Results

The firs t exper iment is des igned to identify significant threat parameters to focus on in portfolio evaluations. The second experiment evaluates the value of different ISSC portfolios under various threat scenarios. Finally, experiment 3 studies the synergy due to interactions between different ISSC portfolio components and examines factors that affect this synergy. Appendix A summarizes the parameter values used in our simulation. In our experiments, common random numbers [21] are used so that each ISSC portfolio is subjected to the same pseudo-random conditions. This approach results in smaller variance and allows the use of fewer observations for statistical significance tests.

## Experiment 1: Identifying Significant Threat Parameters

In the first experiment, we hold the business environment constant and determine various threat environments as described below:

•	 We focus on two types of attacks (theft and DOS) and visualize two scenarios—a mild threat environment (considered as a base environment and labeled as M) and a fierce threat environment (labeled as F).

•	 Each threat parameter for the fierce threat environment is arrived at by multiplying the mild threat parameters (Appendix Table A1) by a fierceness factor $f .$ For example, we set the arrival rate $\lambda _ { _ j }$ of attack j to two values, $\lambda _ { _ { j ( \mathrm { M } ) } }$ and $\lambda _ { j ( \mathrm { F } ) }$ such that $\lambda _ { _ { j ( \mathrm { F } ) } } = f \lambda _ { _ { j ( \mathrm { M } ) } }$ . For f = 2, this implies that the expected arrivals of attack j in a fierce environment is twice the expected arrivals of attack j in the mild environment.

We have in total 256 combinations resulting from varying the four threat environment parameters $( \lambda _ { j } , \mu _ { j } , \rho _ { j } ^ { m } , \tau _ { j } )$ to two levels for each of the two threats, theft $( j = 1 )$ and DOS $( j = 2 )$ .

We use the simulation model to compare two types of ISSC portfolios for each threat environment: a BISSC portfolio and an AISSC portfolio, in which all the countermeasure parameters are made advanced. The values of the countermeasure parameters for the two types of ISSC portfolios are determined as follows:

$$
p _ {i j (a d v)} = \left\{ \begin{array}{l l} \eta_ {p} p _ {i j (b a s)} & \mathrm{if} p _ {i j (b a s)} <   1 \\ p _ {i j (b a s)} & \mathrm{if} p _ {i j (b a s)} = 1 \end{array} \right.
$$

$$
q _ {i j (a d v)} ^ {m} = \eta_ {q} q _ {i j (b a s)} ^ {m} + (1 - \eta_ {q}) q _ {i j (b a s)} ^ {a}
$$

$$
s _ {i j (a d v)} ^ {m} = \eta_ {s} s _ {i j (b a s)} ^ {m} + (1 - \eta_ {s}) s _ {i j (b a s)} ^ {a}
$$

$$
r _ {i j (a d v)} ^ {m} = \eta_ {r} r _ {i j (b a s)} ^ {m} + (1 - \eta_ {r}) r _ {i j (b a s)} ^ {a}.
$$

Each of our portfolios is modeled as a combination of four countermeasures— firewall, encryption, IDS, and antivirus. Here, h $( 0 \leq \mathfrak { n } \leq 1 )$ represents the relative advantage of the advanced countermeasure over a basic countermeasure for a given parameter. A lower value of h indicates a higher degree of effectiveness. In our experiments, hs are set at 0.5 for all parameters. We study the sensitivity of DIV to individual threat parameters keeping the business environment constant. From analysis of variance (ANOVA) results, we find that the two most significant threat parameters are $\lambda _ { _ j }$ and $\mu _ { j } ,$ and we focus on these parameters for experiment 2.

## Experiment 2: Evaluating Portfolios Under Different Threat Scenarios

In this experiment, we set the values for $\lambda _ { _ j }$ and $\mu _ { j }$ for theft (j = 1) and DOS (j = 2) to a mild (M) and fierce (F) value as specified in experiment 1. This gives us a total of 16 combinations of threat environment. For example, a threat environment MMFF represents mild theft arrivals, mild theft damages, fierce DOS arrivals, and fierce DOS damages and has the values $\lambda _ { _ { \mathrm { 1 ( M ) } } } , \mu _ { _ { \mathrm { 1 ( M ) } } } , \lambda _ { _ { 2 ( \mathrm { F } ) } } , \mu _ { _ { 2 ( \mathrm { F } ) } }$ . We create different ISSC portfolios made up of the four countermeasures—firewall, encryption, IDS, and antivirus—and two different capabilities for each countermeasure (i.e., advanced and basic). For example, one of the ISSC portfolios is BA , which represents a basic firewall, a basic encryption, an advanced IDS, and an advanced anti-virus. The value added by any portfolio is the difference between the value of the portfolio and the value of a BBBB portfolio as shown below:

$$
\Delta I V _ {(p o r t f o l i o)} = \frac {1}{T} \int_ {0} ^ {T} I V _ {(p o r t f o l i o)} (t) - I V _ {(\mathrm{BBBB})} (t) d t.\tag{2}
$$

This gives us 15 ISSC portfolios to experiment with. Thus, we have a $1 5 \times 1 6$ value matrix of the values of 15 ISSC portfolios under 16 threat combinations. In experiment 2, the business environment parameters are kept the same as in experiment 1.

While we normally expect that making a countermeasure advanced in an ISSC portfolio would increase DIV, it is possible for DIV to become negative under certain conditions. This effect is a function of the interactions of a countermeasure in the portfolio with another countermeasure and is enhanced by the frequency of arrival of threats. Appendix B provides an illustration of how negative DIV occurs and the conditions that result in negative DIV.

For each cell in the 15 × 16 value matrix of 15 ISSC portfolios, the simulation was replicated 20 times. ANOVA was used to analyze the main effects and interaction effects of countermeasures in determining the value added by a portfolio. The sample data were tested for normality and variance homogeneity. The data deviated from normality, and based on the data plot, it was decided to use logarithmic transformation. Due to the occurrence of some negative DIV values, a direct logarithmic transformation was not feasible.<sup>2</sup> The descriptive statistics showed a range from –4.29 to 29.85. Based on this data, it was decided to use the transformation ln(5 + DIV). This transformation helped to satisfy the normality and variance homogeneity conditions for use of ANOVA. Table 4 summarizes the descriptive statistics for experiment 2. The ANOVA results for the main and interaction effects of the countermeasures for different threat scenarios are summarized in Table 5. Each threat scenario represents a different threat environment (keeping the business environment constant) and is discussed below.

## Scenario 1: An Overall Mild Threat Environment (MMMM in Table 5)

In an environment where threats of both thefts and DOS are mild, each countermeasure by itself adds significant value to the portfolio though the level of significance of encryption is lower than the other countermeasures. Firewall and encryption do

## Underst andi g t he Val ue of Co unterm as ure Portflis in IS Sec urity

Table 4. Descriptive Statistics for Experiment 2

<table><tr><td></td><td>N</td><td>Range</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Value added (ΔIV)</td><td>4,800</td><td>34.145</td><td>-4.293</td><td>29.852</td><td>3.750</td><td>4.644</td></tr></table>

Table 5. Main and Interaction Effects of Countermeasures Under Different Threat Scenarios

<table><tr><td></td><td>MMMM</td><td>MMFF</td><td>FFMM</td><td>FFFF</td></tr><tr><td>Firewall (FW)</td><td>26.405***</td><td>146.431***</td><td>93.520***</td><td>119.867***</td></tr><tr><td>Encryption (Enc)</td><td>10.929**</td><td>16.858**</td><td>79.952***</td><td>49.753**</td></tr><tr><td>IDS</td><td>21.525***</td><td>102.333***</td><td>85.034***</td><td>94.820***</td></tr><tr><td>Antivirus (AV)</td><td>26.468***</td><td>25.506***</td><td>74.118***</td><td>59.284***</td></tr><tr><td>FW * Enc</td><td>3.684</td><td>7.173**</td><td>36.906***</td><td>15.451***</td></tr><tr><td>FW * IDS</td><td>8.201**</td><td>50.497***</td><td>35.831***</td><td>14.981***</td></tr><tr><td>FW * AV</td><td>2.538</td><td>5.043*</td><td>30.385***</td><td>10.386**</td></tr><tr><td>Enc * IDS</td><td>5.860*</td><td>15.979***</td><td>43.267***</td><td>21.572***</td></tr><tr><td>Enc * AV</td><td>3.788</td><td>6.505*</td><td>37.432***</td><td>14.981***</td></tr><tr><td>IDS * AV</td><td>3.285</td><td>7.251**</td><td>35.419***</td><td>14.763***</td></tr></table>

Notes: MMMM = mild theft and mild denial of service threat environment. MMFF = fierce denial of service and mild theft threat environment. FFMM = fierce theft and mild denial of service threat environment. FFFF = fierce theft and fierce denial of service threat environment. $^ { * * * } p \leq 0 . 0 0 1$ \*\* $p \leq 0 . 0 1 ; \ast p \leq 0 . 0 5 .$

not show significant interaction effects in a mild threat environment. IDS has some interaction effects with firewall $( p < 0 . 0 1 )$ and encryption countermeasures $( p < 0 . 0 5 )$ . In the case of antivirus, it does not have significant interaction effects with other countermeasures.

## Scenario 2: Fierce Denial of Service Threat Environment (MMFF in Table 5)

In an environment characterized by DOS attacks dominating other types of threats $( \mathrm { i . e . , } \lambda _ { _ { 2 ( \mathrm { F } ) } } \mathrm { a n d } \mu _ { _ { 2 ( \mathrm { F } ) } } )$ , firewall and IDS countermeasures that offer protection from DOS (see Table 5) are relatively much more important than other countermeasures in adding value. All two-way interactions become significant, though the level of significance varies. We also see that interaction effects of IDS with firewall and with encryption become more significant $( p < 0 . 0 0 1 )$ in this threat environment.

## Scenario 3: Fierce Theft Threat Environment (FFMM in Table 5)

In a threat environment characterized by attempted thefts dominating the other types of threats $( \mathrm { i . e . , } \lambda _ { _ \mathrm { 1 ( F ) } } \mathrm { a n d } \mu _ { _ { 1 ( F ) } } )$ , all the main effects and interaction effects are significant $( p < 0 . 0 0 1 )$ . Since this is a fierce theft scenario, each of these countermeasures protects from theft attacks as is expected (see Table 5) and contributes to DIV. Likewise, the significance of all two-way interaction effects shows that combining any pair of countermeasures will have synergistic effects toward DIV in a high-theft environment.<sup>3</sup>

## Scenario 4: An Overall Fierce Threat Environment (FFFF in Table 5)

In this scenario, as in the other three scenarios, all main effects are significant. Firewall and IDS account for the maximum variance in the value added by the portfolio, similar to the results from scenarios 1 and 2. But in contrast to scenario 1, all two-way interaction effects become significant here.

In summary, while evaluating portfolios and the usefulness of countermeasures, it is important to consider the type of security threats and the severity of each threat relative to other threats. For example, in the case of encryption, one would expect this countermeasure to be extremely important in fierce theft environments (scenarios 3 and 4). As expected, encryption is extremely useful in a scenario where theft is a dominant threat (column FFMM in Table 5). However, the usefulness of encryption (as measured by its significance level) in a fierce theft environment decreases when DOS threats are also fierce (column FFFF in Table 5) or when the relative importance of theft decreases compared to that of DOS.

It is interesting to note that the interaction effects become more significant as the threat environment becomes more fierce (scenarios 2, 3, 4). We further investigate these interactions between countermeasure parameters and the business and threat environment in experiment 3.

## Experiment 3: Evaluating Portfolio Effects

In experiment 3, we are interested in studying the nature of interactions between port folio components. In particular, while we expect that interactions between portfolio parameters will be nonlinear, we would like to understand the conditions under which there is a significant synergy between portfolio components.

Investing in a portfolio of multiple advanced countermeasure parameters could result in substantial additional value (high synergy) compared to stand-alone operations of these countermeasures, or marginal or no additional value (low synergy). This synergy, which we refer to as portfolio effect (PE), occurs due to nonlinear interactions between parameters.

For example, for a portfolio AB (which represents a portfolio with advanced $p ,$ q, r, and basic s) the portfolio effect $P E _ { \mathrm { ( A A A B ) } }$ is given as

$$
P E _ {(\mathrm{AAAB})} = \Delta I V _ {(\mathrm{AAAB})} - \Big (\Delta I V _ {(\mathrm{ABBB})} + \Delta I V _ {(\mathrm{BABB})} + \Delta I V _ {(\mathrm{BBAB})} \Big).\tag{3}
$$

PE is expected to be positive because the synergy due to nonlinear interactions is expected to make the value added by combined portfolio $( \mathrm { i . e . , } \Delta I V _ { _ { ( \mathrm { A A A B } ) } } )$ larger than the sum of the values added by individual countermeasures (i.e., $\Delta I V _ { _ { ( \mathrm { A B B B ) } } } + \Delta I V _ { _ { ( \mathrm { B A B B ) } } } +$ $\Delta I V _ { \mathrm { ( B B A B ) } } )$

In order to highlight the portfolio effects due to the countermeasure parameters, we vary the parameter values in the following way. For each countermeasure, we make only one countermeasure parameter advanced and keep the other parameters unchanged. Thus, the value $p _ { 1 j }$ is changed for the first countermeasure, $q _ { 2 j }$ is changed for the second countermeasure, $r _ { 3 j }$ is changed for the third countermeasure, and $s _ { 4 j }$ is changed for the fourth countermeasure (see Appendix Table A2).

We study the portfolio effects under different threat and business environments. We vary the threat environment by setting the fierceness factor f to different values between 1.0 and 2.0. Different business environments are considered by varying the parameters $\alpha , \lambda _ { { \scriptscriptstyle k } } , \mu _ { { \scriptscriptstyle k } } .$ . The business drift rate a is varied from 0.05 to 0.25. A multiplier between 1.0 and 2.0 is used to vary the levels of business jump arrivals $( \lambda _ { k } )$ and magnitudes (m ) from their basic values shown in Appendix Table A2.

In our analysis, we find that changing recovery time parameter (s) does not result in conclusive findings, which may be due to the negative effects that s sometimes has on the portfolio value. Hence, we focus on the threat parameters $p ,$ q, and r for a given business environment and exclude in our analysis all cases with advanced recovery parameter values (i.e., no portfolio ending with A). Surprisingly, we observe negative portfolio effects in some cases. Further analysis revealed the conditions under which PE becomes negative. It is important to note that negative portfolio effect is not the same as negative DIV of the portfolio. In order to illustrate negative portfolio effects, we present a simple example with three portfolios: AB (advanced $p ,$ basic $q )$ , BA (basic p, advanced $q )$ , and A (advanced p and $q )$ , whose effects on infrastructure value are shown in Figures 6, 7, and $^ { 8 , }$ , respectively. Consider the trajectory of $I V ( t )$ in an infrastructure with advanced $p$ (AB ) (Figure 6).<sup>4</sup> A business jump at $t = 0 . 5$ increases IV(0.5) from 100 to 110 million. A threat that causes a negative jump materializes at $t = 2$ . Having an advanced $p$ prevents this negative jump from reducing $I V ( t ) .$ , beyond $t = 2$ . The shaded region indicates the valued added by having an advanced $p \mathrm { . }$ —that is, $\Delta I V _ { \mathrm { A B } } .$ Figure 7 indicates a similar situation in the same infrastructure, assuming it only has an advanced $q .$ . The shaded region shows $\Delta I V _ { \mathrm { B A } }$ for this scenario. The value added by portfolio A is shown in Figure 8. From our definition of portfolio effects from Equation (3), the negative value is the double-shaded area in Figure 8 and indicates that the value added by portfolio A is less than the sum of the value added by portfolios AB and BA . This double-shaded area showing the negative PE depends, in part, on the business jump and will be greater for higher values of business jumps, ceteris paribus.

It is important to realize that countermeasure parameters p, q, and r act in sequence. Damage due to threats that pass through the ISSC portfolio with probability $p$ is reduced by the parameter q and recovered in part by the parameter r. Negative PE due to scenarios such as the one described in Figures $6 , 7 ;$ , and 8 are likely to result when there are very few threats and these threats are dealt with by countermeasure parameters that occur earlier in this sequential action of countermeasure parameters. These situations are more likely when very few threats pass through the first level of defense in the ISSC portfolio. The expected number of threats passing through the first level of defense in the ISSC portfolio and requiring action by subsequent ISSC parameters is given by $\lambda \boldsymbol { p } _ { i j }$ This is lower when $\lambda _ { _ j }$ is lower, such as in low-threat environments, other things remaining the same. This example focuses on $p$ and $q .$ However, similar effects can be observed in the case of interactions between other sequentially acting countermeasure parameters. The negative portfolio effect (i.e., negative PE term) can also be thought of as a measure of “overkill” of a portfolio. In low-threat environments, low arrival rates and low damages due to threats result in relatively few (or no) scenarios where multiple countermeasures act in concert to prevent, reduce, or recover quickly from damage. Conversely, high-threat environments increase the likelihood that threats are acted on by multiple countermeasure parameters, thus providing greater opportunities for high synergy between countermeasures.

![](/api/attachments/ZBBMT9WC/fulltext/images/664a985e573fa90af63908a41c1d29ef2ec1b0c969d2e2f41366c2207d6615b9.jpg)  
Figure 6. Value Added by Portfolio AB

![](/api/attachments/ZBBMT9WC/fulltext/images/b374c1a053ae46d04463d2b9a97573e490c4ad5c05a33d111eff80904819e966.jpg)  
Figure 7. Value Added by Portfolio BA

![](/api/attachments/ZBBMT9WC/fulltext/images/93fa85615c67e6232252a9179dd465b6d084d1bcc8d942ab52282cb935699926.jpg)  
Figure 8. Negative PE of Portfolio A

In all cases, the portfolio effects increase as the threat environment becomes fiercer, as shown in Figure 9. The rate of change in portfolio effect with respect to the change in the fierceness factor (slope) is dependent on the number and type of countermeasure parameters that are made advanced. For example, $P E _ { \mathrm { ( A A A B ) } }$ has the highest slope compared to other portfolios. For the parameter values in our experiment, making the parameter p advanced (protecting from threat arrivals) results in a higher slope than making other parameters advanced.

The portfolio effects are negative for low-threat environments (f = 1) and positive for high-threat environments (f = 2) as shown in Figures 10 and 11. As the business jumps multiplier (for arrivals and magnitudes) increases, we see that these positive and negative portfolio effects are amplified. Similarly, we observed that increasing the business drift rate (a) amplifies both positive and negative portfolio effects, though the amplification is significantly less than for business jumps.

Figures 12 and 13 capture the variation of portfolio effects by simultaneously varying business and threat environments. Both figures show how the amplification (change in slope) of portfolio effects due to business environment transitions from negative to positive as the threat environment becomes fierce. The results that we observe in Figures 9, 10, and 11 are shown to hold for a range of business and threat parameter values.<sup>5</sup> The results also show that higher business jump environments result in greater changes in the portfolio effects for a given change in threat fierceness factor.

## Discussion and Managerial Implications

When impl ementing s ec ur ity s ys tems and pol ic ies , organizations often believe that the value of their security infrastructure is only as strong as their weakest link. For example, even when the organization has the best firewall in place, a careless employee connecting a laptop with security vulnerability can harm the organization’s network.

![](/api/attachments/ZBBMT9WC/fulltext/images/33de62c86869a8300483e091c4652a4679fa95525e072edc9e350cfaf624da4f.jpg)  
Figure 9. Changes in Portfolio Effects Under Different Threat Environments

![](/api/attachments/ZBBMT9WC/fulltext/images/d6042e77bade4a86731dd38b9e0f8a6a771dae43e62eb88b3a4e9b674a299c71.jpg)  
Figure 10. Changes in Portfolio Effects Due to Business Jumps Under Mild Threat Environment (f = 1.0)

The probability of such a breach is considerably higher in a high-threat environment. However, the implications of the weakest link may be true in situations where the security infrastructure is focused on preventing intrusions and the value is determined by the extent to which the attacks are prevented. In our framework, when multiple countermeasures are implemented as a portfolio and act in sequence, the effects of attacks that pass through a weakest link can be mitigated by subsequent stronger countermeasures. The net effect is that the organization’s ITIA value is protected better by the portfolio of sequential countermeasures than by a single countermeasure. Our framework also emphasizes the need to evaluate the value of an ISSC portfolio in an integrated manner that considers the impact of intrusion prevention, damage reduction, and disaster recovery on IT infrastructures (DIV), in the context of business and threat environments, over a period of time.

![](/api/attachments/ZBBMT9WC/fulltext/images/d8923b60a41692e8f2d5d84846a5e22afc3443050b05fb05e387335c2ca0df52.jpg)  
Figure 11. Changes in Portfolio Effects Due to Business Jumps Under Fierce Threat Environment (f = 2.0)

![](/api/attachments/ZBBMT9WC/fulltext/images/d876b1d09e6934274c129aea709689c51eb0134d8a5aef01d32a6d2b9a9643ee.jpg)  
Figure 12. Portfolio Effects Under Various Business Jumps and Threat Environment

![](/api/attachments/ZBBMT9WC/fulltext/images/5ba393cc89913a52bbb4b23749c109e803c42f02d5284ce6a3c31ac4ad4d4baf.jpg)  
Figure 13. Portfolio Effects Under Various Business Drift and Threat Environments

## Discussion of Results

The results of our experiments demonstrate that the value of an ISSC portfolio to an organization depends on its business environment, threat environment, and characteristics of the ISSC portfolio. The parameters used in our research emphasize the fact that managers need to think in terms of the types of positive and negative jumps in a business environment, different types of threats, damage due to threats, recovery time from threats (and the value of advance warning), and the extent of recovery possible from different types of threats in order to understand the value of IS countermeasure portfolios. The set of parameters and interactions identified by our model is more comprehensive than existing research and forces managers to think about business, threat, and security technologies in evaluating ISSC portfolios. Experiment 3 illustrates the dynamic nature of interactions between portfolio, threat, and business parameters.

Evaluating ISSC portfolios involves identifying the most sensitive parameters, estimating these parameters, and assessing the values of different ISSC portfolios. Our first experiment could help managers identify the most significant parameters in order to focus their limited resources on better estimation of these important parameters. For example, a manager with an existing ISSC portfolio could vary threat environment parameters and perform sensitivity analysis of DIV to identify the most important threat parameters. Once these parameters are identified, the manager could then focus estimation efforts on these parameters in order to minimize the costs associated with parameter estimation. Having estimated these parameters, a manager could then use experiment 2 of our simulation model to assess the values of multiple candidate ISSC portfolios

Experiment 2 indicates that the main effects of countermeasures remain significant across different threat environments, but two-way interaction effects between countermeasures change from being insignificant to highly significant as threats become fiercer. This is an important result given that threat environments are becoming increasingly fierce [34]. For example, attacks against domain name system (DNS) servers have the potential to bring down these servers, thus affecting a large number of Web sites that depend on them for Internet address resolution [12]. In such a scenario, managers would gain additional value or synergies by implementing multiple countermeasures (e.g., IDS and firewall).

Experiment 3 highlights the importance of portfolio effects when evaluating ISSC portfolios. Suppose an organization already has a portfolio and is considering investment in an advanced capability of one of the countermeasures in the portfolio. Without knowing about the portfolio effects, the organization may compare the benefits of the advanced capability publicized by the vendor (net of costs) and make the decision to invest or not. However, due to portfolio effects, the actual benefits from using the advanced countermeasure may now be different in the presence of the other countermeasures in the portfolio, thus affecting the decision to invest in multiple advanced countermeasures.

From Figures 12 and 13, we see that for a given business environment, the change in portfolio effects for a given change in threat fierceness factor is smaller in a stable business environment (i.e., lower business jumps or drift) than in a more dynamic business environment (i.e., higher business jumps or drift). Thus, managers in organizations in rapidly changing business environments as indicated by higher business jump arrivals and magnitudes (e.g., a start-up organization with many new applications being added and with rapidly increasing transaction volume) should expect significant additional value from having multiple advanced countermeasure parameters.

## Illustrative Example of Portfolio Effects

Suppose an organization has a current ISSC portfolio represented by a set of countermeasure parameters $( p _ { 0 } , q _ { 0 } , r _ { 0 } , s _ { 0 } )$ and is considering candidate ISSC portfolios in which one or more of the countermeasure parameters are to be enhanced. The value added by each candidate portfolio represented by $( p , q , r , s )$ over the current portfolio is the portfolio value net of cost (PVNC) defined as follows:

$$
P V N C _ {(p, q, r, s)} = \frac {1}{T} \int_ {0} ^ {T} I V _ {(p, q, r, s)} (t) d t - \frac {1}{T} \int_ {0} ^ {T} I V _ {(p _ {0}, q _ {0}, r _ {0}, s _ {0})} (t) d t - C (p, q, r, s).\tag{4}
$$

Here, $\mathbf { C } ( \mathrm { p , q , r , s } )$ is the cost of switching from the portfolio $( p _ { 0 } , q _ { 0 } , r _ { 0 } , s _ { 0 } )$ to the candidate portfolio $( p , q , r , s )$ . Assume that the organization has hired a security consultant to assess the vulnerabilities in its existing ISSC portfolio and make recommendations for improvement. The security consultant recommends two candidate portfolios. The first candidate portfolio (P1) uses an advanced firewall system that can reduce the rate of successful attacks (p). Consultants, such as Atsec Information Security (www.atsec. com), assess and make recommendations for improving firewall effectiveness (i.e., decreasing p). The second candidate portfolio (P2) uses an advance IDS that improves p, q, r, and s parameters. In addition, a third portfolio (P3), which is a combination of advanced firewall and advanced IDS, can also be considered as a candidate portfolio. To illustrate the portfolio effects in this scenario, we use the countermeasure parameter values of $p , q , r ,$ and s given in Appendix Table A1 for the current portfolio. For the advanced firewall, the p values in Table A1 are halved. For the advanced IDS, the values of $p , q , r ,$ and basic s are half the corresponding values in Table A1. Table 6 shows the values for DIV of the three candidate portfolios P1, P2, and P3 under different threat scenarios using 50 replications.

Table 6. Evaluating Candidate Portfolios

<table><tr><td>Threat</td><td>ΔIV (P1)</td><td>ΔIV (P2)</td><td>ΔIV (P3)</td></tr><tr><td>Low ( $f = 0.5$ )</td><td>1.98</td><td>1.53</td><td>1.96</td></tr><tr><td>Mild ( $f = 1.0$ )</td><td>5.84</td><td>5.40</td><td>7.39</td></tr><tr><td>High ( $f = 2.0$ )</td><td>18.50</td><td>21.06</td><td>28.98</td></tr></table>

It is important to realize that the attractiveness of a particular portfolio depends on (1) the DIV value of the portfolio under a particular set of business and threat factors, and (2) the cost of the portfolio, which itself depends on a different set of factors, including competition among vendors and negotiating power of the organization. The best portfolio in terms of DIV value may no longer be the optimal choice when cost factors are considered. PVNC can be calculated using Equation (4) when cost data are available and used to compare portfolios. Managers must understand the sensitivity of portfolio value and the robustness of a particular portfolio choice to different parameters by examining different possible cost, business, and threat scenarios. Such an analysis is similar to experiment 3, and will help managers to identify the countermeasures that can significantly improve the ITIA value.

## Dependence Among Countermeasures

The discussion in our paper is general and does not differentiate between correlated and independent ISSC. However, our framework can easily incorporate both correlated and uncorrelated countermeasures. This section examines the implications of correlation (dependence) among countermeasures in our model by discussing an example involving two countermeasures and the parameter p.

Let us consider the case of two countermeasures CM1 and CM2. If CM1 and CM2 have similar capabilities to prevent attacks, because of overlapping signatures, then attacks of type j that evade CM1 are also likely to evade CM2. In other words, CM2s effectiveness in preventing threat j is lower in the presence of CM1 than if CM2 was acting alone. This lower effectiveness of CM2 due to its positive correlation with CM1 can be modeled by increasing $p _ { 1 j }$ for attack j. In the same way, if CM1 and CM2 have complementary capabilities to recognize and prevent attack, then CM2 can be considered to be negatively correlated with CM1. Hence, if CM1 prevents one type of attack, CM2 is more likely to prevent other types of attacks. The increased effectiveness of CM2 due to its negative correlation with CM1 can be modeled by decreasing $p _ { 1 j }$ for attack j. If CM1 and CM2 are uncorrelated in their attack recognition, $p _ { 1 j }$ and $p _ { 2 j }$ are specified independently. Each of the scenarios (positive correlation between CMI and CM2, negative correlation between CMI and CM2, and uncorrelated CM1 and CM2) described above can be considered as a separate ISSC portfolio whose behavior can be analyzed using our simulation model.

Table 7. Evaluating Candidate Portfolios with Correlated Countermeasures

<table><tr><td>Threat</td><td> $\Delta IV (P3)$ </td><td> $\Delta IV (P3_{pc})$ </td><td> $\Delta IV (P3_{nc})$ </td></tr><tr><td>Low ( $f = 0.5$ )</td><td>1.96</td><td>1.42</td><td>1.97</td></tr><tr><td>Mild ( $f = 1.0$ )</td><td>7.39</td><td>5.20</td><td>7.72</td></tr><tr><td>High ( $f = 2.0$ )</td><td>28.98</td><td>23.76</td><td>30.71</td></tr></table>

To illustrate, consider an example of a firewall and an IDS and the three types of correlations between their preventive capability (i.e., parameter $p _ { i j } ^ { \phantom { } }$ for DOS attacks to create three portfolios P3 (from Table 7), $\mathrm { P 3 } _ { \mathrm { p c } }$ , and $\mathrm { P 3 } _ { \mathrm { n c } }$ that correspond to three scenarios respectively: (1) no correlation between the firewall and the IDS, (2) IDS is less effective in the presence of the firewall, and (3) IDS is more effective in the presence of the firewall. If there is significant overlap in the signatures recognized by the firewall and the IDS (i.e., positive correlation), then Pr(passing through IDS | passed the firewall) > Pr(passing through IDS). When there are complementarities in the attack signatures recognized by the firewall and the IDS, then Pr(passing through IDS | passed the firewall) < Pr(passing through IDS). In our simulation, we retained the value of $p _ { 3 2 } = 0 . 2 5$ for P3. We used $p _ { 3 2 } = 0 . 9$ for $\mathrm { P 3 } _ { \mathrm { p c } }$ (to reflect reduced effectiveness from positive correlation) and ${ { p } _ { 3 2 } } \mathrm { { = } } 0 . 1$ for $\mathrm { P 3 } _ { \mathrm { n c } }$ (to reflect increased effectiveness due to negative correlation). Table 7 shows the resulting DIV values for three portfolios: P3, $\mathrm { P 3 } _ { \mathrm { p c } } ,$ and $\mathrm { P 3 } _ { \mathrm { n c } }$ discussed above.

As expected, positive (negative) correlation decreases (increases) DIV, and the magnitude of this decrease (increase) is higher in high-threat environments compared to low-threat environments. Equation (4) can be used to determine the best portfolio choice in different threat environments when portfolio costs are available. We do not attempt to illustrate this because choice of cost numbers would be arbitrary.

The above discussion can be generalized to other model parameters. Our model allows for correlation among different countermeasures through appropriate parameter values. However, estimation of correlated countermeasure parameters is not always easy (especially as the number of correlated parameters increases) since multiple conditional probabilities are involved and are likely to be situation specific.

## Estimation of Countermeasure Parameters

The following discussion illustrates that estimation of $p , q , r ,$ and s may be possible based on current industry practices and explains the relationship between the parameters required for the simulation model and industry practices based on other methods.

Estimation of pass-through rates (p) and reduction in damage $( q )$ due to a countermeasure is often done in industry. IT security consultants, such as Atsec Information Security, offer to analyze an existing countermeasure and improve pass-through rates (p). Pass-through rates have been used in evaluation of countermeasures [3, 31, 36]. Estimation of expected losses due to a threat in the presence of a countermeasure $( l _ { p } )$ and without a countermeasure $( l _ { _ w } )$ are part of industry practices for evaluating countermeasures [31, 36]. Reduction in damage from a threat to a countermeasure (q) can be calculated as $l _ { p } / l _ { w }$

Assume that the original ITIA value with 100 percent processing capability is $I V ( t )$ . The expected damage due to threat j is $\boldsymbol { \theta } _ { \boldsymbol { I } } { \cal I } ( t )$ . Given that $\rho _ { j }$ is the proportion of damage after recovery without any countermeasures, the net damage without countermeasures is $\mathsf { \rho } _ { j } \mathsf { \theta } _ { j } I V ( t )$ . Using a countermeasure i with recovery parameter $r _ { i j }$ results in a net damage of $r _ { i j } \mathsf { p } _ { j } \mathsf { \Theta } _ { j } I V ( t )$ . Assume that a disaster recovery contract specifies 80 percent recovery. Then,

$$
0. 8 = (I V (t) - r _ {i j} \rho_ {j} \theta_ {j} I V (t)) / I V (t) = (1 - r _ {i j} \rho_ {j} \theta_ {j}).\tag{5}
$$

Given that $\boldsymbol { \theta } _ { j }$ and $\rho _ { j }$ can be estimated as shown in Table 3, we can then estimate $r _ { i j }$ using Equation (4).

It is also important to note that organizations may specify the extent to which recovery is completed in terms of a physical resource, such as processing capacity, as part of disaster recovery planning. For example, a contract may specify 80 percent of processing capacity (servers) to be restored, meaning that they expect that ITIA value will be restored to some portion of its original value corresponding to 80 percent of its processing capacity at a particular point in time. We assume that managers could think about this relationship between processing capacity and $I V ( t )$ , and use this information in arriving at the value of processing capacity in a contract. Asking questions such as “does 80 percent processing capacity correspond to 75 or 80 or 85 percent of ITIA value?” will help mangers to think about this relationship. Equation (5) can be used with this assumption. While other, more sophisticated modeling may be possible, we believe this is a reasonable assumption that managers could follow.

The parameter s mirrors the concept of recovery time objective (RTO) (e.g., see [33]), which is well-established in disaster recovery contracts and is the ratio of recovery time with and without a countermeasure. Organizations currently plan disaster recovery countermeasures based on RTO. Hence, the idea of countermeasures reducing RTO (parameter s) is well accepted in industry.

## Model Assumptions, Validation, and Limitations

A major assumption of our model is the sequential and multiplicative nature of ISSC parameter interactions. Thus, when two ISSCs interact, their effect will be similar to a combined ISSC whose parameters are the product of the two ISSC parameters. We believe this is a reasonable assumption that is consistent with prior research on passthrough rates [3]. Our research extends the multiplicative effects to include multiple ISSC parameters, as discussed earlier in the Simulation Variables and Parameters section. Also, from a practical perspective, we increasingly see IS security products treated as suites that have capabilities of multiple countermeasures.

Simulation and statistical analysis using synthetic data, similar to this paper, has been used in other disciplines to study similar problems involving threats and countermeasures, such as rapidly evolving disaster response systems [7] and forest fire regimes [23]. It has been recognized that “simulation can fill an important gap between qualitative and empirical studies” [7, p. 311]. Simulation using synthetic data has also been used in other MIS studies where the underlying phenomenon is complex and real-world data are difficult to obtain, such as understanding the value of knowledge management [6], electronic markets [18], team processes [32], and others. Any simulation study runs the risk of simplifying or abstracting reality in order to better understand the underlying phenomenon and raises questions of external validity [30, 32]. The conclusions are limited by the choice of model parameters, distributions, and parameter values [32]. We believe that our choices of model variables, interrelationships, and distributions are sufficiently realistic (as justified in Table 2) and help to better specify and understand the interactions between ISSC portfolio components.

Model validation in the types of studies mentioned above involves justifying the assumed functional forms and distributions used for simulation parameters based on relevant theory or empirical evidence. The section on simulation variables and parameters and Table 2 provide such justifications. Also, performing ANOVA on simulated data is in some ways similar to performing ANOVA on a limited sample of real data. ANOVA results could in such cases be limited by sample characteristics such as whether the data are from one or multiple companies, industry, size, and so on. Even in contexts where real-world data are available, multiple studies are often required to confirm and generalize results. Our results could be considered one such study, which could be a candidate for confirmation using real data. Simulation allows for analysis using a wider range of parameter values than may be possible with real data.

It may be possible to build more sophisticated models to address some of the limitations of this study. For example, a model of IT infrastructure value can include different components of the security infrastructure at subnetwork levels. The assumption of linear recovery used for the purposes of our simulation can be relaxed. It may be possible to use other nonlinear forms of recovery parameters depending on the information available about the recovery capabilities of the countermeasure. We have assumed that countermeasures only impact the jump parameter of ITIA value. It may be possible to model the impact on the drift parameter as well. For example, sophisticated encryption may slow down information processing<sup>6</sup> and can be modeled as a reduction in the drift rate. Alternatively, we could assume that organizations spend more on the IT infrastructure to maintain information-processing performance, which can be incorporated in the model.

## Conclusions and Future Research

Or ganizations ar e incr easingl y dependent on IT . This increasing dependence, coupled with the increasing incidence of threats to IT infrastructures, has resulted in organizations making large IT security investments in a variety (portfolios) of ISSCs. While prior research has identified the need to evaluate and incrementally invest in different ISSC portfolio components, a systematic approach to understanding different ways in which ISSC portfolio components can add value to an organization’s IT infrastructure is lacking in the literature.

This paper makes several important contributions. It illustrates the need to consider the interactions between an organization’s business environment, threat environment, and characteristics (including sequence) of ISSCs in order to evaluate ISSC portfolios. While a general recognition of this need may have existed, prior research has not specifically identified and integrated characteristics of business, threat, and countermeasures that are important for understanding ISSC value. Prior research has either focused on risk analysis or disaster recovery. This paper integrates the risk analysis, disaster recovery, and countermeasure portfolio perspectives and presents a comprehensive set of parameters and model of their interactions.

This research improves the understanding of ISSC portfolio value in several ways. First, model variables and the simulation framework help researchers and managers better understand and articulate key uncertainties and relationships and pinpoint areas for information gathering. Such modeling has significant value even with synthetic data [24] since the model and variables help structure the debate about the value of ISSCs and open up the field for further exploration.

Second, this paper contributes to understanding interactions between countermeasures, which is an important but underresearched issue. Experiment 2 illustrates several interactions between multiple countermeasures. For example, it illustrates that the usefulness of a countermeasure depends on what other countermeasures are employed as well as the type of security threat and the severity of each threat relative to other threats.

Third, experiment 3 contributes to an improved understanding of the dynamics of the interactions between countermeasures, threat, and business environments. It illustrates the sensitivity of ISSC portfolio value to changes in countermeasure, business, and threat parameters. These results indicate that while individual countermeasures may be relatively unattractive, given their cost, it is possible for portfolios of countermeasures to be significantly more valuable compared to the sum of their costs.

Finally, the model presented in this paper can be viewed as a systematic approach to assessing ISSC portfolio value. While determining model parameter values could be difficult, we do not think approximate valuation is out of the question as discussed in the previous section. We hope our research will help guide researchers and managers in framing the problem and identifying areas for data collection. In addition, there is growing pressure due to legislative initiatives such as the Basel Committee recommendations for financial institutions to collect actual data on system-related factors that affect operational risk [4]. Organizations are beginning to collect such data. Hence, it is likely that estimating at least some of the model parameters identified by this paper is feasible. Examples of such future research include case studies to illustrate the applicability of such models to real-world situations.

Acknowledgments: This research was funded in part by a grant from Childress-Klein Inc. and the Belk College of Business, University of North Carolina–Charlotte. The authors are grateful to the editor and referees for comments that greatly improved the quality of the paper. They are also grateful to Tae-Sung Kim of Chungbuk National University, Korea, for his comments during the early stages of this research.

## Notes

1. In this paper, we use the terms threat and attack interchangeably. For our model, the relevant issues are whether a security attack is successful or not and the damage caused if the attack is successful.

2. Although having a negative DIV value is counterintuitive given that we use common random numbers, the simulation runs that generated negative DIV values were very rare (54 out of 4,800). Moreover, the average of those negative DIV values (–0.65) was relatively small as compared to the average (3.75). Hence, these rare observations neither alter our findings nor justify the use of the basic portfolio.

3. While we focused in this paper on two-way interactions, it is possible to study higherorder interactions in a similar manner.

4. We have not considered drift and noise terms in this example, for simplicity.

5. Portfolio effects increase as the threat environment becomes fiercer. Both positive and negative portfolio effects are amplified as the business jumps arrivals and magnitudes increase.

6. We thank the referees for pointing this out.

7. We thank the referees for helping us think through these conditions.

## Refer enc es

1. Antoniou, I.; Ivanov, V.V.; Ivanov, V.V.; and Zrelov, P.V. On a statistical model of network traffic. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 502, 2–3 (2003), 768–771.

2. Arora, A., and Telang, R. Economics of software vulnerability disclosure. IEEE Security and Privacy, 3, 1 (2005), 20–25.

3. Arora, A.; Hall, D.; Pinto, C.A.; Ramsey, D.; and Telang, R.A. Measuring the risk-based value of IT security solutions. IEEE IT Professional, 6, 6 (2004), 35–42.

4. Basel Committee on Banking Supervision. Observed range of practice in key elements of advanced measurement approaches (AMA). Bank for International Settlements, Basel, 2006 (available at www.bis.org/publ/bcbs131.pdf).

5. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The value of intrusion detection systems in information technology security architecture. Information Systems Research, 16, 1 (2005), 28–46.

6. Chen, A.N.K., and Edgington, T. Assessing value in organizational knowledge creation: Considerations for knowledge workers. MIS Quarterly, 29, 2 (2005), 279–309.

7. Comfort, L.K.; Ko, K.; and Zagorecki, A. Coordination in rapidly evolving disaster response systems: The role of information. American Behavioral Scientist, 48, 3 (2004), 295–313.

8. Conrad, J.R. Analyzing the risks of information security investments with Monte-Carlo simulations. Paper presented at the Fourth Workshop on Economics of Information Security, Harvard University, Cambridge, June 2–3, 2005 (available at http://infosecon.net/workshop/ pdf/13.pdf).

9. Copeland, G., and Keller, T. A Comparison of high-availability media recovery techniques. In J. Clifford, B. Lindsay, and D. Maier (eds.), Proceedings of the 1989 ACM SIGMOD International Conference on Management of Data. New York: ACM Press, 1989, pp. 98–109.

10. Devaraj, S., and Kohli, R. Impacts of information technology: Is actual usage the missing link? Management Science, 49, 3 (2003), 273–289.

11. Dudin, A.N., and Karolik, A.V. BMAP/SM/1 queue with Markovian input of disasters and non-instantaneous recovery. Performance Evaluation, 45, 1 (2001), 19–32.

12. Evers, J. DNS servers—An Internet Achilles’ heel. CNET News.com, 2005 (available at http://news.com.com/2100-7349\_3-5816061.html).

13. Fan, M.; Stallert, J.; and Whinston, A.B. The adoption and design methodologies for component-based enterprise systems. European Journal of Information Systems, 9, 1 (2000), 25–35.

14. Farahmand, F.; Navathe, S.B.; Sharp, G.P.; and Enslow, P.H. Managing vulnerabilities of information systems to security incidents. In N. Sadeh et al. (eds.), Proceedings of the Fifth International Conference on Electronic Commerce. New York, ACM Press, 2003, pp. 348–354.

15. Farahmand, F.; Navathe, S.B.; Sharp, G.P.; and Enslow, P.H. A management perspective on risk of security threats to information systems. Journal of Information Technology & Management, 6, 2–3 (2005), 203–225.

16. Gordon, L.A., and Loeb, M.P. The economics of information security investment. ACM Transactions on Information and System Security, 5, 2 (2002), 438–457.

17. Gordon, L.A.; Loeb, M.P.; Lucyshyn, W.; and Richardson, R. Eleventh annual CSI/FBI computer crime and security survey. Computer Security Institute, San Francisco, 2006.

18. Jones, J.L.; Easley, R.F.; and Koehler, G.J. Market segmentation within consolidated e-markets: A generalized combinatorial auction approach. Journal of Management Information Systems, 23, 1 (Summer 2006), 161–182.

19. Keefer, D.L., and Bodily, S.E. Three-point approximations for continuous random variables. Management Science, 29, 5 (1983), 595–609.

20. Kumar, R. A framework for assessing the business value of information technology infrastructures. Journal of Management Information Systems, 21, 2 (Fall 2004), 11–32.

21. Law, A.M., and Kelton, W.D. Simulation Modeling and Analysis, 3d ed. New York: McGraw-Hill, 2000.

22. Lawrence, R.J. Applications in economics and business. In E.L. Crow and K. Shimuzu (eds.), Lognormal Distributions: Theory and Applications. New York: Marcel Dekker, 1988, pp. 44–59.

23. Li, C.; Barclay, H.; Lui, J.; and Campbell, D. Simulation of historical and current fire regimes in central Saskatchewan. Forest Ecology and Management, 208, 1–3 (2005), 319–329.

24. Liberatore, M.; Hatchuel, A.; Weil, B.; and Stylianou, A. An organizational change perspective on modeling. European Journal of Operational Research, 125, 1 (2000), 184–194.

25. Lijenstan, M.; Nicol, D.; Berk, V.; and Gray, R.S. Simulating realistic network worm traffic for worm warning system design and testing. In S. Staniford and S. Savage (eds.), Proceedings of the 2003 ACM Workshop on Rapid Malcode. New York: ACM Press, 2003, pp. 24–33.

26. Liu, P.; Zang, W.; and Yu, M. Incentive-based modeling and inference of attacker intent, objectives, and strategies. ACM Transactions on Information System Security, 8, 1 (2005), 78–118.

27. Ning, P., and Xu, D. Hypothesizing and reasoning about attacks missed by intrusion detection systems. ACM Transactions on Information and System Security, 7, 4 (2004), 591–627.

28. Orlikowski, W.J., and Iacono, C.S. Research commentary: Desperately seeking the “IT” in IT research—A call to theorizing the IT artifact. Information Systems Research, 12, 2 (2001), 121–134.

29. Post, G.V., and Diltz, J.D. A stochastic dominance approach to risk analysis of computer systems. MIS Quarterly, 10, 4 (1986), 363–375.

30. Raghu, T.S.; Sen, P.K.; and Rao, H.R. Relative performance of incentive mechanisms: Computational modeling and simulation of delegated investment decisions. Management Science, 49, 2 (2003), 160–178.

31. Rainer, K.; Snyder, C.; and Carr, H. Risk analysis for information technology. Journal of Management Information Systems, 8, 1 (Summer 1991), 129–147.

32. Rao, H.R.; Chaudhury, A.; and Chakka, M. Modeling team processes: Issues and a specific example. Information Systems Research, 6, 3 (1995), 255–285.

33. Rennels, B. A practical guide to disaster recovery planning: The basics to getting started. White paper, Double-Take Software, Southboro, MA, March 2006 (available at www.blade. org/docs/wp/DR-Planning.pdf).

34. Rosencrance, L. “Brute force” attacks against SMBs on the rise. Computerworld, August 2, 2006 (available at www.computerworld.com/action/article.do?command=viewArticleBasic &articleId=9002162).

35. Schechter, S. Toward econometric models of the security risk from remote attacks. IEEE Security and Privacy, 3, 1 (2005), 40–44.

36. Sun, L.; Srivastava, R.; and Mock, T. An information systems security risk assessment model under the Dempster–Shafer theory of belief functions. Journal of Management Information Systems, 22, 4 (Spring 2006), 109–142.

37. Trigeorgis, L. Real Options: Managerial Flexibility and Strategy in Resource Allocation. Cambridge, MA: MIT Press, 1996.

38. Trivedi, K.S. Probability and Statistics with Reliability, Queuing and Computer Science Applications. New York: John Wiley and Sons, 2001.

39. Vijayan, J. Time is of the essence. Computerworld (March 21, 2005), 38.

40. Wolff, R.W. Poisson arrivals see time averages. Operations Research, 30, 2 (1982), 223–231.

41. Yue, W.T., and Çakanyildirim, M. Intrusion prevention in information systems: Reactive and proactive responses Journal of Management Information Systems, 24, 1 (Summer 2007), 329–353.

<sub>ed</sub> <sub>by</sub> <sub>[Laurentian</sub> <sub>University]</sub> <sub>at</sub> <sub>00:52</sub> <sub>17</sub> M

<table><tr><td colspan="3">Table A1. Parameter Values Used for Experiments 1 and 2</td></tr><tr><td>Type</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="8">Business environment (fixed)</td><td> $T$ </td><td>2 years</td></tr><tr><td> $\alpha$ </td><td>5 percent per year</td></tr><tr><td> $\sigma_z$ </td><td>2 percent per year</td></tr><tr><td> $IV(0)$ </td><td>$100 (million)</td></tr><tr><td> $k$ : jump type</td><td>1: new application,2: system integration,3: positive spike in demand,4: negative spike in demand</td></tr><tr><td> $\{ \lambda_k \}$ </td><td>{4, 10, 10, 7}</td></tr><tr><td> $\{ \mu_k \}$ </td><td>{ln(1.05), ln(1.02), ln(1.005), ln(0.995)}</td></tr><tr><td> $\{ \sigma_k \}$ </td><td>{0.01, 0.005, 0.002, 0.002}</td></tr><tr><td rowspan="8">Threat environment (fixed)</td><td> $j$ : threat type</td><td>1: Theft,2: Denial of service,3: Virus</td></tr><tr><td> $\{ \lambda_j \}$ </td><td>{600, 3, 35}</td></tr><tr><td> $\{ \mu_j \}$ </td><td>{ln(0.85), ln(0.99), ln(0.985)}</td></tr><tr><td> $\{ \sigma_j \}$ </td><td>{0.05, 0.005, 0.01}</td></tr><tr><td> $\{ \rho_j^m \}$ </td><td>{0.7, 0.5, 0.2}</td></tr><tr><td> $\{ \rho_j^a \}$ </td><td>{0.2, 0.2, 0.1}</td></tr><tr><td> $\{ \rho_j^b \}$ </td><td>{0.9, 0.9, 0.3}</td></tr><tr><td> $\{ \mu_{\tau_j} \}$ </td><td>{60, 10, 20}</td></tr><tr><td rowspan="5">Countermeasureeffectiveness(variable)</td><td>i: countermeasure (basic)</td><td>1: Firewall,2: Encryption,3: IDS,4: Antivirus</td></tr><tr><td> $p_{ij}$ </td><td> $\begin{pmatrix} 0.05 & 0.5 & 1.0 \\ 0.1 & 1.0 & 1.0 \\ 0.2 & 0.5 & 1.0 \\ 0.9 & 1.0 & 0.05 \end{pmatrix}$ </td></tr><tr><td> $q_{ij}^{m}, q_{ij}^{a}, q_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 0.7 & 1.0 \\ 0.7 & 1.0 & 1.0 \\ 0.5 & 1.0 & 1.0 \\ 1.0 & 1.0 & 0.4 \end{pmatrix}, \begin{pmatrix} 1.0 & 0.5 & 1.0 \\ 0.5 & 1.0 & 1.0 \\ 0.4 & 1.0 & 1.0 \\ 1.0 & 1.0 & 0.3 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.9 & 1.0 & 1.0 \\ 0.9 & 1.0 & 1.0 \\ 1.0 & 1.0 & 0.5 \end{pmatrix}$ </td></tr><tr><td> $r_{ij}^{m}, r_{ij}^{a}, r_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.6 & 1.0 & 1.0 \\ 0.8 & 0.6 & 0.8 \\ 1.0 & 1.0 & 0.3 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.4 & 1.0 & 1.0 \\ 0.6 & 0.4 & 0.7 \\ 1.0 & 1.0 & 0.15 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.9 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 0.5 \end{pmatrix}$ </td></tr><tr><td> $s_{ij}^{m}, s_{ij}^{a}, s_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.7 & 1.0 & 1.0 \\ 0.5 & 0.7 & 0.8 \\ 1.0 & 1.0 & 0.3 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.6 & 1.0 & 1.0 \\ 0.3 & 0.4 & 0.6 \\ 1.0 & 1.0 & 0.15 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.8 & 1.0 & 1.0 \\ 0.8 & 0.8 & 1.0 \\ 1.0 & 1.0 & 0.5 \end{pmatrix}$ </td></tr></table>

<table><tr><td colspan="3">Table A2. Parameter Values Used for the Sensitivity of Portfolio Effects</td></tr><tr><td>Type</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="8">Business environment (fixed)</td><td> $T$ </td><td>2 years</td></tr><tr><td> $\alpha$ </td><td>{5, 10, 15, 20, 25} percent per year for sensitivity</td></tr><tr><td> $\sigma_z$ </td><td>2 percent per year</td></tr><tr><td> $IV(0)$ </td><td>$100 (million)</td></tr><tr><td> $k$ : jump type</td><td>1, 2, 3, 4</td></tr><tr><td> $\{\lambda_k\}$ </td><td>{4, 15, 10, 7}</td></tr><tr><td> $\{\mu_k\}$ </td><td>{ln(1.05), ln(1.02), ln(1.0105), ln(0.995)}</td></tr><tr><td> $\{\sigma_k\}$ </td><td>{0.01, 0.005, 0.002, 0.002}</td></tr><tr><td rowspan="8">Threat environment (fixed)</td><td> $j$ : threat type</td><td>1, 2, 3</td></tr><tr><td> $\{\lambda_j\}$ </td><td>{300, 30, 60}</td></tr><tr><td> $\{\mu_j\}$ </td><td>{ln(0.90), ln(0.99), ln(0.98)}</td></tr><tr><td> $\{\sigma_j\}$ </td><td>{0.05, 0.005, 0.01}</td></tr><tr><td> $\{\rho_j^m\}$ </td><td>{0.3, 0.3, 0.3}</td></tr><tr><td> $\{\rho_j^a\}$ </td><td>{0.1, 0.1, 0.2}</td></tr><tr><td> $\{\rho_j^b\}$ </td><td>{0.5, 0.5, 0.5}</td></tr><tr><td> $\{\mu_{\tau_j}\}$ </td><td>{60, 10, 30}</td></tr></table>

<table><tr><td rowspan="5">Countermeasureeffectiveness (variable)</td><td>i: countermeasure (basic)</td><td>1: specialized for reducing damage arrival rates ( $p_{1j} \lambda_{j}$ )2: specialized for reducing damages ( $\theta_{j}$ )3: specialized for reducing postrecovery damages ( $\rho_{j}$ )4: specialized for reducing recovery time ( $\tau_{j}$ )</td></tr><tr><td> $p_{ij}$ </td><td> $\begin{pmatrix} 0.05 & 0.25 & 0.1 \\ 0.1 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}$ </td></tr><tr><td> $q_{ij}^{m}, q_{ij}^{a}, q_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.9 & 0.9 & 0.9 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 0.7 & 0.7 & 0.7 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}$ </td></tr><tr><td> $r_{ij}^{m}, r_{ij}^{a}, r_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 0.5 & 0.5 & 0.5 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 0.2 & 0.2 & 0.2 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}$ </td></tr><tr><td> $s_{ij}^{m}, s_{ij}^{a}, s_{ij}^{b}$ </td><td> $\begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 0.9 & 0.9 & 0.9 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 0.1 & 0.1 & 0.1 \end{pmatrix}, \begin{pmatrix} 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \\ 1.0 & 1.0 & 1.0 \end{pmatrix}$ </td></tr></table>

## Appendix B: Understanding Negative Incremental Portfolio Value (DIV)

The value added by an AISSC over a BISSC is affected not only by the impact of the countermeasure on the arrival rate of the threats $( \lambda _ { _ j } )$ and the magnitude of the loss due to a successful attack (mean loss of $\mu _ { _ j } )$ , but by its impact on the recovery time $( \tau _ { _ j } )$ . Consider an advanced countermeasure (A) and a basic countermeasure (B) that have the same parameter values for $p , q ,$ and r but differ in the time taken to recover from the loss (due to damage); that is, the countermeasures have different values of s. Figure B1 shows the changes in $I V ( t )$ for each countermeasure. Assume a damage caused by an attack at time $t _ { 0 }$ creates a drop in value of $d _ { 0 } ^ { \textrm { A } }$ , which is the same as $d _ { 0 } ^ { \textrm { B } }$ However, the recovery time $( t _ { \mathrm { A } } - t _ { 0 } )$ with advanced countermeasure is expected to be shorter than the recovery time $( t _ { \mathrm { B } } - t _ { 0 } )$ with basic countermeasure. Now suppose that a second damage occurs at time $t _ { 1 } \left( > t _ { 0 } \right)$ and this damage is not recovered by the countermeasures. $\mathrm { I f } t _ { _ { 1 } } < t _ { _ { \mathrm { B } } }$ but $t _ { \mathrm { 1 } } > t _ { \mathrm { A } }$ (i.e., the basic countermeasure is still recovering from the first damage while the advanced countermeasure has completed the recovery), then $d _ { 1 } ^ { \textrm { B } }$ is smaller than $d _ { \mathrm { _ 1 } } ^ { \mathrm { ~ A ~ } }$ . Due to the continuing recovery process by basic countermeasure, at some time $t ^ { * } ,$ , the loss recovered by countermeasure B will be greater than the loss recovered by countermeasure A. Therefore, at time $t _ { \mathrm { B } } .$ , we observe that $I V _ { \mathrm { A } } ( t _ { \mathrm { B } } ) | t _ { 1 } < t _ { \mathrm { B } }$ is less than $I V _ { \mathrm { B } } ( t _ { \mathrm { B } } ) | t _ { 1 } < t _ { \mathrm { B } } ,$ . This difference, if observed over the remaining lifetime of ISSC, may be enough to offset the benefit from using advanced countermeasure that is observed until $t ^ { * }$ .

If a new attack does not occur until the system has fully recovered from damage, then we will always have the value-added by an AISSC greater than the value-added by a BISSC. Hence, the results from experiment 2 show negative values for DIV in some cases (see Table 4), indicating that an AISSC that has faster recovery time $( s _ { i j } )$ may result in lower benefits than a BISSC.

The above scenario is just one illustration of having a negative DIV value, and other different scenarios are possible. It is important to realize that even though basic countermeasure portfolios are less effective (on average) than advanced countermeasure portfolios, there could be some (relatively rare) sample paths (using common random numbers) where the basic portfolio could be as effective as the advanced countermeasure portfolio.

After examining each case of negative DIV value, we find the following conditions<sup>7</sup> for having negative DIV values, under an advanced recovery scenario. For a particular sample path,

1. The basic portfolio has to be as effective as the advanced portfolio by having the same or close values for the number of successful attacks as well as for their corresponding damage amount and recovery amount.

2. The recovery time of the advanced portfolio has to be smaller than that of the basic portfolio, and there have to be at least two successful attacks in sequence where the second attack occurs before recovering from the first attack. The second attack has to be unrecoverable or its recovery amount has to be small enough to allow a crossover (as illustrated in Figure B1 with $t ^ { * } )$ .

![](/api/attachments/ZBBMT9WC/fulltext/images/10f419b488c422037600c04444de5efc7dec15ba5dd4fb6d1f2d26e0d6a95795.jpg)  
Figure B1. An Illustration of Possible Negative Effect of Having a Portfolio with Advanced Countermeasure

3. The recovery process of the first attack has to be independent of the second attack. This assumption indicates that the recovery from the first attack can continue after the second attack occurs.

For a potential real-world scenario, consider two different types of successful attacks occurring in sequence; for example, a DOS then a theft. One can imagine that a successful DOS attack decreases the value of ITIA and that the recovery from DOS can be expedited by an advanced portfolio. Given that the subsequent theft attack is unrecoverable, a slow recovery may result in a situation where unavailable ITIA due to partial recovery is not subject to the theft attack following the DOS attack. In this case, the recovery from DOS can still continue regardless of the damage from the theft attack.
