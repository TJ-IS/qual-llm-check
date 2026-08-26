---
otero_id: 5788
otero_key: "HQ737GJB"
title: "Managing Information Security Outsourcing in a Dynamic Cooperation Environment"
authors: "Yong Wu; Giri Kumar Tayi; Genzhong Feng; Richard Y. K. Fung"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00681"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2021

# Managing Information Security Outsourcing in a Dynamic Cooperation Environment

Yong Wu , wuyong@dhu.edu.cn

Giri Kumar Tayi , gtayi@albany.edu

Gengzhong Feng , gzfeng@mail.xjtu.edu.cn

Richard Y. K. Fung , richard.fung@friends.cityu.edu.hk

Follow this and additional works at: https://aisel.aisnet.org/jais

# Managing Information Security Outsourcing in a Dynamic Cooperation Environment

## Cover Page Footnote

To eficiently manage information security, firms typically outsource part of their security functions to a managed security service provider (MSSP) under a variety of contractual arrangements. Based on this practice, we study a business setting in which the management of security outsourcing depends on the security efforts of both the MSSP and its clients, taking into account that their allocation of efforts can change during the contract horizon. Since their efforts are private to each other, a double moral hazard (DMH) problem can arise with the use of bilateral refund contracts, which have been widely adopted in the MSSP industry. Moreover, both the high probability of undirected attacks and system interdependency can exacerbate the DMH problem. We propose two new types of contracts to solve this problem. One is a monitoring contract, in which a cyberinsurance firm monitors the security efforts of the MSSP and its clients. The other is a liability contract, in which both parties take full liability for breaches through rewarding clients who are well protected and penalizing clients who end up being breached by hackers. Our findings show that monitoring contracts can only solve the DMH problem when variable monitoring costs are negligible. Liability contracts can also solve the DMH problem and are worth implementing when an MSSP encounters (1) a high probability of undirected attack, (2) high system interdependency, (3) a long contract horizon, or (4) when both parties have nearly equal responsibility over the course of the contract horizon. We also compare the proposed contracts in two additional settings: when the MSSP has a spillover effect and when the MSSP serves three or more clients.

# Managing Information Security Outsourcing in a Dynamic Cooperation Environment

Yong Wu<sup>1</sup>, Giri Kumar Tayi<sup>2</sup>, Genzhong Feng<sup>3</sup>, Richard Y. K. Fung<sup>4</sup>

<sup>1</sup>Glorious Sun School of Business & Management, Donghua University, China, wuyong@dhu.edu.cn <sup>2</sup> School of Business, State University of New York at Albany, USA, gtayi@albany.edu <sup>3</sup> Corresponding author, School of Management, Xi’an Jiaotong University, China, gzfeng@mail.xjtu.edu.cn <sup>4</sup> School of Management, Xi’an Jiaotong University, China, richard.fung@friends.cityu.edu.hk

## Abstract

To efficiently manage information security, firms typically outsource part of their security functions to a managed security service provider (MSSP) under a variety of contractual arrangements. Based on this practice, we study a business setting in which the management of security outsourcing depends on the security efforts of both the MSSP and its clients, taking into account that their allocation of efforts can change during the contract horizon. Since their efforts are private to each other, a double moral hazard (DMH) problem can arise with the use of bilateral refund contracts, which have been widely adopted in the MSSP industry. Moreover, both the high probability of undirected attacks and system interdependency can exacerbate the DMH problem. We propose two new types of contracts to solve this problem. One is a monitoring contract, in which a cyberinsurance firm monitors the security efforts of the MSSP and its clients. The other is a liability contract, in which both parties take full liability for breaches through rewarding clients who are well protected and penalizing clients who end up being breached by hackers. Our findings show that monitoring contracts can only solve the DMH problem when variable monitoring costs are negligible. Liability contracts can also solve the DMH problem and are worth implementing when an MSSP encounters (1) a high probability of undirected attack, (2) high system interdependency, (3) a long contract horizon, or (4) when both parties have nearly equal responsibility over the course of the contract horizon. We also compare the proposed contracts in two additional settings: when the MSSP has a spillover effect and when the MSSP serves three or more clients.

Keywords: Information Security Outsourcing, Double Moral Hazard, Cyber-Insurance, Liability Contract

Kim Huat Goh was the accepting senior editor. This research article was submitted on January 14, 2020 and underwent two revisions.

## 1 Introduction

The frequent occurrence of cyberattacks and the increasing sophistication of technologies for information security have pushed many firms to outsource security protection to managed security service providers (MSSPs). The global managed security service market is expected to reach \$47.65 billion by 2023 (MarketsandMarkets, 2018), and a recent survey (pwc, 2017) shows that 62% of respondents use an MSSP to operate and enhance their cybersecurity programs.

Firms usually outsource only part of their security activities to an MSSP for the following reasons. First, outsourcing core information systems can lead to potential theft of proprietary information since the MSSP could misappropriate the information and sell it to competitors (Clemons & Aron, 2004). Second, the practice of outsourcing generally allows firms to focus on efficiently using their resources while paying an MSSP to perform functions they are less adept at (Rowe, 2007). For instance, firms often outsource prevention and detection functions to an MSSP and operate basic security fundamentals such as updating and employee education in-house (Vuorinen and Tetri 2012). Therefore, effective management of information security requires both the MSSP and its clients to cooperate under various contractual arrangements.

In practice, bilateral refund contracts (BRCs) have been widely adopted in the MSSP industry. BRCs determine the service fees that clients pay to an MSSP and the compensation that an MSSP must pay to clients if a breach occurs (Bryson, 2000). Like other outsourcing relationships, a double moral hazard (DMH) problem can arise in BRC contexts (Cooper & Ross, 1985) because the security quality depends on the security efforts of both the MSSP and its client, and neither party can verify how much effort the other party is devoting to this issue. For instance, in 2004, a payment processing company called CardSystems (CS) hired an MSSP named Savvis to assess and certify its compliance with credit card security regulations and CS developed its own security operations. One year later, CS suffered a data breach and more than 40 million credit card records were compromised (Zetter, 2009). Following the event, CS sued Savvis for not providing sufficient vulnerability assessment and compliance services, while Savvis sued CS for not investing enough in information security.

Unlike other types of outsourcing relationships, two distinctive characteristics of security outsourcing— hacker behavior, and system interdependency—have significant effects on contractual arrangements. Hacker behavior is usually segregated into two categories, undirected attacks and direct attacks, based on whether attacks are autonomous over the network (undirected attack) or have a specific target (direct attack) (Casey, 2003). Viruses, worms, and spam email are common undirected attacks, whereas denial of service, website defacement, and the purposeful penetration into a bank’s system are typical direct attacks. Compared to direct attacks, undirected attacks may be more massive and pervasive but are easier to address because they have a stable frequency and are prevented by MSSPs on a daily basis (pwc, 2017). System interdependency often emerges when clients’ systems are interdependent since security technologies adopted by an MSSP have similar vulnerabilities. Consequently, when hackers breach such vulnerabilities, a simultaneous breach may occur with other clients (Hui et al., 2012). System interdependency is more serious in the case of undirected attacks since undirected attacks make it easier to infect interconnected systems. For example, in 2010, the email provider Silverpop was breached by spammers. As an MSSP, Silverpop had adopted similar technologies with all its clients and many of its clients suffered serious data breaches (Charette, 2010).

Based on the above, we study security outsourcing management in a collaborative and dynamic setting. The collaboration between an MSSP and its clients is necessarily dynamic because the information security landscape is highly fluid and dynamic (Mookerjee et al., 2011). In our study, once an MSSP and its client sign a contract, they both need to devote efforts to security, and their security efforts may change, requiring interaction with each other throughout the contract duration. We demonstrate that BRCs can induce the DMH problem, which becomes severe when an MSSP faces either a high attack probability or high system interdependency. To address the DMH problem, we propose two new contract types according to project control (i.e., behavior control and outcome control) (Choudhury & Sabherwal, 2003). We analyze each contract type by answering the following four questions: (1) Can the proposed contract solve the DMH problem? (2) What is the operating mechanism underlying the proposed contract? (3) Is it easy to evaluate the compensation in the proposed contract following a breach? (4) Is the proposed contract worth implementing?

Based on behavior control, we propose the monitoring contract, in which the security efforts of both parties are monitored by a third-party agent that we refer to as the cyberinsurance firm. Monitoring efforts can eliminate information asymmetry (Hölmstrom, 1979); thus, we find that the monitoring contracts can solve the DMH problem when the variable monitoring costs are negligible. However, it is not easy to implement monitoring contracts since the compensation is affected by many factors. Based on outcome control, we propose the liability contract, in which the MSSP rewards clients who are well protected and penalizes clients who end up being breached by hackers. We find that the liability contract can also solve the DMH problem and is easy to implement. The operating mechanism of the liability contract is based on both the MSSP and clients being fully liable for security loss, including direct loss and indirect loss caused by system interdependency.

We compare the three contract types: the bilateral refund contract, the monitoring contract, and the liability contract. Our analysis indicates that the MSSP’s effort is U-shaped in terms of system interdependency, whereas the client’s effort is inversely U-shaped with BRCs because of the tradeoff between security risk and investment risk. However, intensified system interdependency causes both parties to increase their respective security efforts in the context of monitoring and liability contracts. Monitoring contracts are worth implementing when the fixed monitoring costs are low, while liability contracts are worth implementing when the MSSP faces high attack probabilities or high system interdependency, when the contract horizon is long, or when both parties have nearly equal responsibility. Finally, we extend our model to show that the two new contract types we propose are appropriate when the MSSP’s efforts have a spillover effect on clients or when the MSSP serves three or more clients.

The remainder of the paper is organized as follows. The next section reviews the related literature. Section 3 introduces the model and derives the benchmark efforts. Section 4 presents the analysis of the three contract types—the bilateral refund contract, the monitoring contract, and the liability contract. Section 5 compares the three contracts, and Section 6 extends the basic model. Managerial implications are discussed in Section 7.

## 2 Literature Review

Since security outsourcing as a strategy to manage information security is a recent development, the extant research devoted to this topic is limited. In their seminal paper, Ding et al. (2005) examine the optimal contract characteristics of an MSSP by considering moral hazard problems and reputation effects. Hui et al. (2012) examine how system interdependency would interact with a mandatory security requirement to affect the equilibrium behaviors of an MSSP and its clients. Zhao et al. (2013) examine three alternative risk management approaches and show that an MSSP serving multiple firms can internalize the externality of security investments. Cezar et al. (2014) classify the nature of the security function into two categories and propose a new contract to enhance the advantages offered by the complementarity between prevention and detection functions. Cezar et al. (2017) also explain firms’ decisions to outsource security based on interdependent risks and competitive externalities. These studies focus on the MSSP’s effort only and do not consider clients’ involvement and thus do not account for the client-side moral hazard problem associated with BRCs. However, since the outsourcing part of security activities is common in practice, the resulting DMH problem is a serious issue that needs to be considered.

Research in many domains has addressed the DMH problem that arises when two involved parties are not contractible. For example, in economics, Cooper and Ross (1985) discuss the optimal product warranty contract in the presence of double moral hazard and show that bilateral contracts do not lead to first-best outcomes. In operations management, Demirezen et al. (2016) study the relationship between clients and vendors in value co-creation environments and highlight the circumstances under which double moral hazard decreases the client’s overall value. In the information systems domain, Jayanth et al. (2011) study the double moral hazard problem that arises in the requirements assessment of software development and find that increasing the effectiveness of the feedback process for clients can mitigate the DMH problem.

Although the DMH problem has been widely discussed in the above domains, to the best of our knowledge, Lee et al. (2013) is the only other paper that discusses the DMH problem in the context of security outsourcing. However, our research differs from theirs in terms of three aspects: utility, variability, and operability. First, Lee et al. (2013) propose a new contract type to solve the DMH problem but do not consider the contract’s utility. By contrast, we not only consider a variety of contractual arrangements that could be implemented to solve the DMH problem, but also consider hacker behavior and compare the utility of two new contract types and offer guidance to security participants seeking the most beneficial type of contract. Second, Lee et al. (2013) develop a lumpsum, single-shot model, whereas we consider a dynamic model. If certain factors vary—for example, the MSSP enhances its ability by deploying newer protection technology while the contract is valid, the change is not incorporated into either party’s updated decisions in a static model. Our paper accounts for variability in effort since the security landscape continues to be highly fluid and dynamic (Mookerjee et al., 2011). Third, the contract terms proposed by Lee et al. (2013) depend on security externality, and both parties’ security efforts determine security externality. However, a basic assumption of DMH is that neither party understands the other’s security effort. Thus, the contract proposed by Lee et al. (2013) is challenging and difficult to implement. In contrast, the compensation coefficient proposed in this paper depends only on security interdependency, which can be estimated using past breach data. Thus, the new contract types proposed in this paper are operable.

Prior research has examined insurance as a risk management tool (Georges, 2013). For example, Ogut et al. (2005) use an economic model to discuss the impact of system interdependency on firms’ security investments and insurance coverage. They find that system interdependency reduces firms’ incentives to invest in security. Srinidhi et al. (2015) show that cyberinsurance reduces managers’ overinvestment in specific security-enhancing assets. Prior literature treats cyberinsurance as a supplementary strategy of security investments. In contrast, we segregate the insurance function of an MSSP to a cyberinsurance firm that can monitor and verify the security efforts of both an MSSP and its clients.

## 3 The Model

We consider an MSSP that provides some security functions to two homogeneous clients and is faced with the challenge of determining the optimal outsourcing contract. The MSSP can choose from three types of contract: the bilateral refund contract, the monitoring contract, or the liability contract. Irrespective of which contract type is chosen, both the MSSP and clients need to exert respective security efforts to improve security quality in a dynamic environment. We model the contracting problem as a differential game in which both parties are risk-neutral, and the total time horizon of the contract is denoted by ??.

We denote the security effort levels of the MSSP and client ?? at time ?? by $e _ { M i } ( t )$ and $e _ { F i } ( t )$ , respectively. <sup>1</sup> Gartner reports that a majority of initial security efforts involve basic infrastructure technologies (“keeping bad guys out” technologies) such as firewalls and antivirus with stable costs, and the subsequent focus of the effort shifts to “letting good guys $\mathrm { i n } ^ { \bar { , } \bar { , } }$ technologies such as authentication and access management, which require more investment in configuration and management (Wheatman et al., 2005, Gupta and Zhdanov, 2012). Thus, we assume that both parties’ security effort costs follow increasing convex functions, as outlined in the following assumption:<sup>2</sup>

Assumption 1: Both the MSSP’s and client’s security effort costs are increasing convex functions and are denoted by $\textstyle { \frac { 1 } { 2 } } C e _ { M i } ^ { 2 } ( t )$ and $\scriptstyle { \frac { 1 } { 2 } } C e _ { F i } ^ { 2 } ( t )$ , respectively, where ?? is a cost coefficient.

As discussed above, the improvement in the security quality of client ?? is a consequence of the collaborative work between the MSSP and client ??. In Varian (2004), system reliability is defined in the context of three prototypical cases: the total-effort case, the minimum effort case, and the maximum effort case. This paper follows most studies (such as Yue et al., 2007) in that we assume that client $i \mathbf { \ ' } _ { \mathbf { S } }$ security quality depends on the total efforts exerted by both parties and that these efforts allow improvements in security quality to accumulate over time (Srinidhi et al., 2015). Thus, we state the following assumption:

Assumption 2: Client $i ^ { \circ } \mathbf { s }$ instantaneous increase in security quality is $\dot { q } _ { i } ( t ) = \varepsilon ( \alpha e _ { F i } ( t ) + \beta e _ { M i } ( t ) )$ where $\alpha \left( \beta \right)$ is the output sensitivity of client ?? (the MSSP). Client ?? has the initial quality $q _ { 0 } .$

The positive parameter ?? needs to be sufficiently small such that client $i ^ { \prime } s$ security quality $q _ { i } ( t )$ always lies between 0 and $1 . ^ { 3 }$ The above assumption implies that the instantaneous increase in security quality is a sum of each party’s instantaneous effort multiplied by their respective output sensitivity. A party that has a higher output sensitivity implies that it can improve security quality more effectively. Thus, it is rational for both parties to align respective responsibility for the output of security quality according to their output sensitivities. Therefore, the output sensitivities ?? and $\beta$ , can also represent respective responsibility levels for the output of security quality. Output sensitivities are inherently difficult to determine and two methods are usually adopted to estimate them in practice. One involves using data from other business cases, including contracts between the MSSP and other industry peers; the other is evaluated by a third party such as an industry association, with the help of investment evaluation techniques such as return on investment (Dickson, 2018). Furthermore, a client has the initial security quality of $q _ { 0 }$ when neither an MSSP nor the client exerts security efforts.

A client’s system’s breach probability depends on both the system’s security quality and the probability of a hacker’s attack on the system. As noted above, compared to strategic attacks, undirected attacks may be more pervasive but they have a stable frequency and are prevented by MSSPs on a daily basis. Thus, this study focuses on undirected attacks and assumes that the probability of an undirected attack on a client is a constant $^ { a , }$ which lies between 0 and $1 . ^ { 4 }$ Therefore, the successful breach probability $p _ { i } ( t )$ of client ?? at time ?? is $a ( 1 -$ $q _ { i } ( t ) )$ .

A client will obtain an increasing nonnegative utility $V ( t )$ over time if no security breaches occur during the contract period; we assume the client’s initial utility is

<sup>4</sup> Since undirected attacks usually occur with a stable frequency and the period of information security outsourcing contract is usually not long, we assume the probability of undirected attack is a constant during the contract period. A more general model that the probability of undirected attack is a stochastic variable turns out to be analytically intractable.

zero. <sup>5</sup> An information system, such as a customer relationship management system, should be more valuable to firms over time if it continues to remain secure. When breached, a client would incur a direct loss, which we refer to as security loss ?? . The loss includes tangible costs such as revenue losses from the disruption of services and intangible costs such as reputation and consumer losses.

Beyond direct security losses to client ??, other clients may also suffer indirect losses caused by system interdependency. As noted above, system interdependency is caused when multiple clients adopt similar security technologies provided by the MSSP, resulting in hackers who are able to exploit the common vulnerability of the technology to attack all its clients. This scenario usually appears when an MSSP suffers undirected attacks, as shown in the real-world case of Silverpop, which was breached by spammers. Thus, we make the following assumption:

Assumption 3: If one client is compromised, the client incurs a loss of ?? and the other client incurs a loss of ????, where $\lambda \in [ 0 , 1 ]$ measures the degree of system interdependency and is determined by past breaches. Furthermore, the liability for a breach cannot be easily assigned to one party only.

The term ?? that lies between 0 and 1 implies that the loss caused by a direct breach is more than that caused by system interdependency. The Cardsystems case demonstrates that the liability for a breach cannot be easily assigned to one party only. Therefore, it is very hard to determine the degree of system interdependency after a breach occurs. In practice, ?? can be estimated using data from past breaches.<sup>6</sup>

The game between the MSSP and clients is a Stackelberg game, where the MSSP is the principal and includes two stages. In Stage 1, the MSSP offers a contract $( f _ { i } , \phi _ { i } )$ to client ??. Client ?? pays a service fee $f _ { i }$ to the MSSP, and the MSSP compensates the client with $\phi _ { i } L$ if the client suffers a breach, with $\phi _ { i }$ representing the compensation coefficient. In practice, the compensation is based on either the service fee or security loss. For example, the compensation that Verizon Business pays its clients depends on either the service fee or the extent of security loss.<sup>7</sup> This paper follows prior literature (e.g. Hui et al., 2012) in assuming that compensation depends on the extent of security loss. In addition, the MSSP needs to compensate client j with $\lambda \phi _ { j } L$ if client j suffers an indirect loss caused by system interdependency. In Stage 2, clients can accept or reject the contract. If client ?? rejects the contract, client i obtains the reservation utility $U _ { F }$ , and the MSSP obtains the reservation utility ${ U _ { M } } . ^ { 8 }$ If client ?? accepts the contract, the MSSP exerts $e _ { M i } ( t )$ , and client ?? exerts $e _ { F i } ( t )$ to improve client $i \mathbf { \ ' } _ { \mathbf { S } }$ security quality. Table 1 contains a list of the key notations used in the paper.

Table 1. Main Model Notations

<table><tr><td>Notations</td><td>Definition</td><td>Variable types</td></tr><tr><td> $T$ </td><td>Length of contract horizon</td><td></td></tr><tr><td> $e_{Mi}(t) (e_{Fi}(t))$ </td><td>The MSSP’s (client  $i$ &#x27;s) security effort at time  $t$ </td><td>Control variable</td></tr><tr><td> $\alpha (\beta)$ </td><td>Output sensitivity of the client (the MSSP)</td><td></td></tr><tr><td> $q_i(t)$ </td><td>Client  $i$ &#x27;s security quality at time  $t$ </td><td>State variable</td></tr><tr><td> $a$ </td><td>Probability of undirected attack on a client’s system</td><td></td></tr><tr><td> $L$ </td><td>Security loss</td><td></td></tr><tr><td> $\lambda$ </td><td>System interdependency</td><td></td></tr><tr><td> $f_i$ </td><td>Service fee</td><td>Decision variable</td></tr><tr><td> $\phi_i$ </td><td>Compensation coefficient under the BRC</td><td>Decision variable</td></tr></table>

the contract, the MSSP will offer the contract in which the system interdependency is the average of the past two breaches (that is, $\lambda = \frac { 1 } { 4 } \mathrm { \Omega }$ . Since a client may suffer many

## 3.1 Benchmark Case

We first analyze the benchmark case where we assume that there is no moral hazard occurrence because both the MSSP and the clients operate as one entity or as a single firm. The objective in this case is to maximize the summation of the expected payoffs of an MSSP and both clients. Through comparison with the benchmark case, we can compare the performance of the three contracts. The benchmark payoff and constraints can be expressed as follows:

$$
\max _ {e _ {F i} (t), e _ {M i} (t)} S W = 2 V (T) - \sum_ {i = 1} ^ {2}
$$

$$
\left. \int_ {0} ^ {T} \left[ p _ {i} (t) (1 + \lambda) L + \frac {1}{2} C e _ {F i} ^ {2} (t) + \frac {1}{2} C e _ {M i} ^ {2} (t) \right] d t \right\}\tag{1}
$$

$$
s. t. \dot {q} _ {i} (t) = \varepsilon (\alpha e _ {F i} (t) + \beta e _ {M i} (t)), i = 1, 2\tag{2}
$$

$$
e _ {F i} (t) \geq 0, e _ {M i} (t) \geq 0, i = 1, 2\tag{3}
$$

$$
S W \geq \underline {{U}} _ {M} + 2 \underline {{U}} _ {F}\tag{4}
$$

where $p _ { i } ( t ) = a ( 1 - q _ { i } ( t ) )$ . The objective function in Equation (1) is to maximize the total social welfare,<sup>( ( ), ( )U e t e t</sup>Fi Fi Mi which includes both clients’ nonnegative utilities $( V ( T ) )$ , the direct and indirect security loss $( p _ { i } ( t ) ( 1 +$ $\lambda ) L ) _ { ☉ }$ , and both parties’ effort costs $\begin{array} { r l } { \mathrm { ~ ( ~ } \frac { 1 } { 2 } C e _ { F i } ^ { 2 } ( t ) + } & { { } } \end{array}$ $\textstyle { \frac { 1 } { 2 } } C e _ { M i } ^ { 2 } ( t ) )$ . The constraint represented in Equation (2) describes how improvements in security quality accumulate over time. The constraint represented in Equation (3) states that neither party’s security effort can be negative. The constraint represented as Equation (4) indicates that both parties productively collaborate only if they can generate a combined value of social welfare that is larger than their total reservation utilities. The benchmark efforts can be expressed as follows:

Lemma 1: The benchmark security efforts of the client and the MSSP are $\begin{array} { r } { e _ { F } ^ { * } ( t ) = \frac { \sum _ { \ell } a L \alpha ( 1 + \lambda ) ( T - t ) } { C } } \end{array}$ and $\begin{array} { r } { e _ { M } ^ { * } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { C } . } \end{array}$

All proofs are in Appendix A. Lemma 1 indicates that both parties’ benchmark efforts depend only on their own output sensitivities and have nothing to do with the other party’s output sensitivity. This is because the benchmark setting treats both parties as a single firm, thereby eliminating moral hazard. As a result, both parties perform their respective duties and exert efforts in strict accordance with their respective output sensitivities.

## 4 Contractual Arrangements

This section analyzes the three contracts: the bilateral refund contract, the monitoring contract, and the liability contract, respectively.

## 4.1 Bilateral Refund Contract

The basic assumption of the benchmark case is to treat an MSSP and its clients as if they were aligned as a single firm, in which case each party’s efforts could be verified by the other. However, the goal of both parties is to maximize their own expected benefits under the <sup>( )]</sup>i <sup>t dt</sup>  BRC; thus, their effort levels are private and cannot be reciprocally verified. The expected payoffs for both parties under the BRC are as follows:

$$
U _ {M} (e _ {F 1} (t), e _ {F 2} (t), e _ {M 1} (t), e _ {M 2} (t)) =
$$

$$
\sum_ {i = 1} ^ {2} \left\{f _ {i} - \int_ {0} ^ {T} \left\{p _ {i} (t) \left(\phi_ {i} + \lambda \phi_ {3 - i}\right) L + \frac {1}{2} C e _ {M i} ^ {2} (t) \right\} d t \right\}\tag{5}
$$

$$
\begin{array}{l} U _ {F i} \left(e _ {F i} (t), e _ {M i} (t)\right) = V (T) - \\ \int_ {0} ^ {T} \left\{\left(p _ {i} (t) + \lambda p _ {3 - i} (t)\right) \left(1 - \phi_ {i}\right) L + \frac {1}{2} C e _ {F i} ^ {2} (t) \right\} d t - f _ {i} \end{array}\tag{6}
$$

where $p _ { i } ( t ) = a ( 1 - q _ { i } ( t ) ) , i = 1 , 2$ . An MSSP’s expected payoff under the BRC includes the service fee received from the client $( f _ { i } )$ , the compensation paid to both clients $p _ { i } ( t ) ( \phi _ { i } + \lambda \phi _ { 3 - i } ) L$ , and its effort cost $\textstyle ( { \frac { 1 } { 2 } } C e _ { M i } ^ { 2 } ( t ) )$ . Similarly, client i’s expected payoff includes its nonnegative utility $( V ( T ) )$ ), direct and indirect loss $\begin{array} { r } { \textbf { ( } ( p _ { i } ( t ) + \lambda p _ { 3 - i } ( t ) ) L \textbf { ) } } \end{array}$ , the $\mathrm { M S S P ^ { \circ } s }$ compensation $( ( p _ { i } ( t ) + \lambda p _ { 3 - i } ( t ) ) \phi _ { i } L )$ , and its effort cost $( \textstyle { \frac { 1 } { 2 } } C e _ { F i } ^ { 2 } ( t ) )$ ). Following the subgame perfect Nash equilibrium concept (Fudenberg & Tirole, 1991), we use backward induction to solve the problem. In Stage 2, both parties determine optimal security efforts by maximizing their own expected payoffs. We use ${ \hat { e } } _ { M i } ( t )$ and $\hat { e } _ { F i } ( t )$ to represent the MSSP’s and client $i \mathbf { \ ' } _ { \mathbf { S } }$ subgame perfect Nash equilibrium efforts. The problem faced by the MSSP in Stage 1 is presented in the proof of Lemma 2 in Appendix A. We give the optimal operating mechanism under the BRC directly:

Lemma 2: Under the bilateral refund contract, the MSSP charges the service fee $\hat { f } = V ( T ) - { \underline { { U } } } _ { F } -$ $\underline { { { a L \alpha ^ { 2 } T ( 1 + \lambda ) ^ { 2 } ( \overline { { { 1 } } } { { - q } _ { 0 } } ) } } } \perp$ ??<sup>2</sup>(1+??)<sup>2</sup>+??<sup>2</sup> ??<sup>2</sup>??<sup>2</sup>??<sup>2</sup>(1+??)<sup>2</sup>??<sup>3</sup>??<sup>2</sup>(??<sup>4</sup>(1+2??)+2??<sup>2</sup>(1+??)(??<sup>2</sup>(1+??)<sup>2</sup>−????<sup>2</sup>)) 6??(??<sup>2</sup>(1+??)<sup>2</sup>+??<sup>2</sup>)<sup>2</sup> and compensation coefficient $\begin{array} { r } { \hat { \phi } = \frac { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } - \lambda \alpha ^ { 2 } } { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } } } \end{array}$ The MSSP exerts effort $\hat { e } _ { M } ( t ) =$ $\varepsilon a L \beta ( 1 + \lambda ) ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } - \lambda \alpha ^ { 2 } ) ( T - t )$ and the client exerts $\overline { { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } }$ effort $\begin{array} { r } { \hat { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ^ { 3 } ( 1 + \lambda ) ( T - t ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } . } \end{array}$

Hereafter, we refer to ${ \hat { e } } _ { M } ( t )$ and $\hat { e } _ { F } ( t )$ as the MSSP’s and the client’s BRC efforts, respectively. We find that $\hat { e } _ { M } ( t ) < e _ { M } ^ { * } ( t )$ and $\hat { e } _ { F } ( t ) < e _ { F } ^ { * } ( t )$ , i.e., both parties’ BRC efforts are always weaker than their own benchmark efforts. Thus, a DMH problem arises under the BRC, leading to inefficiency in security efforts stemming from the free-rider problem (Roels et al., 2010). The BRC induces the DMH problem because compensation has different roles for incentivizing both parties, i.e., compensation simultaneously punishes the MSSP and rewards clients. If $\phi _ { i } = 1 , \hat { e } _ { M } ( t ) = e _ { M } ^ { * } ( t )$ and if $\phi _ { i } = - \lambda , \hat { e } _ { F } ( t ) = e _ { F } ^ { * } ( t )$ , then the party that takes full liability for the breach will exert the benchmark effort. Since the compensation coefficient lies between 0 and 1, the DMH problem always exists when executing BRCs.

Proposition 1: In the bilateral refund contract: (a) The DMH problem for one party will first become worse and will then be alleviated as its own output sensitivity increases, and (b) The DMH problem for both parties will become worse as the system interdependency or attack probability increases.

Proposition 1(a) shows that as one party’s output sensitivity increases, the gap between its own benchmark effort and the BRC effort first increases and then decreases. We find that both parties’ DMH problems are the worst when $\alpha = \beta ( 1 + \lambda )$ , i.e., when the output sensitivity of the MSSP is nearly equal to that of the client. In this case, both parties have nearly equal responsibility for improving security quality, and thus the most severe DMH problem arises. However, when one party takes on most of the responsibility, its BRC effort is nearly equal to its benchmark effort. Therefore, one party’s BRC effort is effective when it retains most of the responsibility in the collaboration and is ineffective when both parties assume nearly equal responsibility.

Proposition 1(b) indicates that as the system interdependency increases, the gap between both parties’ benchmark efforts and BRC efforts increases. Since the benchmark case treats the MSSP and clients as a single firm, both parties completely internalize the system interdependency. However, under the BRC, the MSSP internalizes the system interdependency directly and incompletely since its expected payoff is directly affected by the system interdependency. In contrast, the client internalizes the system interdependency indirectly and incompletely through the compensation offered by the MSSP. Thus, the DMH problem for both parties will become worse as the system interdependency increases.

Proposition 1(b) also shows that the gap between one party’s benchmark effort and BRC effort increases with the probability of undirected attacks. As discussed above, in the benchmark setting, the MSSP and clients perform their respective duties and jointly exert efforts commensurate with the attack probability. However, since both parties’ goal is to maximize their own expected payoffs under the BRC, although the effort under the BRC increases with the attack probability, the rate of increase of the benchmark effort also becomes greater. As a result, both parties’ DMH problem will become worse as the probability of undirected attacks increases.

## 4.2 The Monitoring Contract

Section 4.1 shows that both the MSSP and its clients suffer a DMH problem under the BRC. We thus propose two new contract types—the monitoring contract and the liability contract—to address the DMH problem according to the project control types. Project control is an effective contract design mechanism that integrates the respective capabilities of participants (Kirsch, 1997). Two types of controls have been commonly considered by the principal, i.e., behavior control and outcome control (Choudhury & Sabherwal, 2003).

In terms of behavior control, the principal can influence the project process by monitoring an agent’s behaviors and rewarding or penalizing the agent based on the level of effort (Choudhury & Sabherwal, 2003). As one form of behavior control, monitoring security efforts can eliminate information asymmetry between the MSSP and clients and solve the DMH problem. In effect, monitoring effort is sometimes necessary because information security may seem harmless or irrelevant when firms do not face imminent malicious attacks (Feng, et al. 2019). Although an MSSP can monitor clients’ efforts, since it is difficult for the MSSP to verify them, legal disputes between the MSSP and its clients may arise, as evidenced by the CardSystems/Savvis case. Thus, monitoring and verification processes might be better managed by a third party. In practice, cyberinsurance (CI) firms are actively used as thirdparty agents to mitigate firms’ exposure to financial distress resulting from security breaches (Srinidhi et al., 2015). CI firms are considered an effective incentive mechanism to enforce rational economic behavior across security stakeholders. CI firms can monitor both parties’ security efforts with the help of tools such as information technologies (IT), forensic audits, and regular meetings (Choudhury & Sabherwal, 2003). The 2015 value of the global standalone cyberinsurance market has been estimated at \$1.7 billion in annual gross written premiums (Aon Inpoint, 2017).

As the cyberinsurance market grows, the insurance function of the MSSP can be increasingly delegated to a third-party insurer, who can monitor and verify the efforts of both the MSSP and its clients. In practice, before issuing insurance policies, CI firms often formally audit clients to ensure that clients have appropriate security capabilities enabling them to take proper actions to protect themselves (Zhao et al., 2013). Thus, we assume that CI firms can monitor and regulate the efforts of both parties through insurance policies.

![](/api/attachments/HQ737GJB/fulltext/images/2eb71d2988d78b5776348eae7cc1d1ae4f32f2fc31d0551ac15e0b4e2d856f6a.jpg)  
Figure 1. The Relationship between the Cyberinsurance Firm, the MSSP, and Clients

As shown in Figure 1, the timing of events is as follows: (1) Clients pay an insurance premium $I _ { \scriptscriptstyle F }$ to the CI firm, and the CI firm offers a service fee $I _ { u }$ to the MSSP for providing security services to its clients. (2) The insurance policy stipulates that both the MSSP and its clients must make efforts to improve security. (3) If a client experiences a breach, the CI firm pays compensation $s _ { F } L$ to the client and charges the MSSP a penalty $s _ { { } _ { M } } L$ , where $s _ { F }$ and $s _ { M }$ are the compensation coefficient and penalty coefficient, respectively. Like in a BRC, the CI firm pays compensation $\lambda s _ { F } L$ to the client and charges the MSSP a penalty $\lambda s _ { { _ M } } L$ if a client suffers an indirect loss caused by system interdependency.

Despite the benefits, monitoring security efforts incurs some fixed and variable costs for the CI firm. As mentioned above, monitoring security efforts requires the deployment of tools such as IT, which imposes fixed costs on the CI firm. The variable costs increase with the agent’s effort since more effort requires more monitoring costs (Demirezen et al., 2016). Thus, we make the following assumption:<sup>9</sup>:

Assumption 4: When monitoring the MSSP and client i’s security effort, the cyberinsurance firm incurs a fixed cost $F _ { R i }$ and variable costs $\textstyle { \frac { 1 } { 2 } } C _ { R } e _ { F i } ^ { 2 } ( t )$ and $\textstyle { \frac { 1 } { 2 } } C _ { R } e _ { M i } ^ { 2 } ( t )$ based on the MSSP’s and client $i \mathit { \ ' } _ { S }$ security efforts, where $C _ { R }$ is the cost multiplier for monitoring security efforts.

Monitoring security efforts implies that the CI firm can set the MSSP and clients’ security efforts at levels that maximize the CI firm’s own excepted payoff. We use $\bar { e } _ { M } ( t )$ and $\bar { e } _ { F } ( t )$ to represent such levels of the MSSP’s and client i’s security efforts in Stage 2. The problem faced by the CI firm in Stage 1 is presented in the proof of Lemma 3 in Appendix A.

We now analyze the proposed monitoring contract by answering the following four questions: (1) Can the proposed contract solve the DMH problem? (2) What is the operating mechanism underlying the proposed contract? (3) Is it easy to evaluate the compensation in the proposed contract following a breach? (4) Is the proposed contract worth implementing? The following lemma answers the first and second questions:

Lemma 3: In equilibrium, the CI firm sets insurance premium and compensation to the client such that $I _ { F } ^ { * } + ( 1 - s _ { F } ^ { * } ) ( ( 1 - q _ { 0 } ) ( 1 + \lambda ) a L T -$ $\begin{array} { r } { \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } ( 1 + \lambda ) ^ { 2 } T ^ { 3 } ( \alpha ^ { 2 } + \beta ^ { 2 } ) } { 3 ( C + C _ { R } ) } ) = V ( T ) - U _ { F } - } \end{array}$ $\frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } ( 1 + \lambda ) ^ { 2 } T ^ { 3 } \alpha ^ { 2 } } { 6 ( C + C _ { R } ) ^ { 2 } }$ , and the client exerts effort $\begin{array} { r } { \bar { e } _ { F } ( t ) = \frac { \sum \cdots } { C + C _ { R } } } \end{array}$ . Meanwhile, the CI Firm sets service fee and penalty to the MSSP such that $2 I _ { M } ^ { * } - 2 s _ { M } ^ { * } ( ( 1 - q _ { 0 } ) ( 1 + \lambda ) a L T -$ $\begin{array} { r } { \frac { \varepsilon ^ { 2 } \overset { \cdots } { a ^ { 2 } } L ^ { 2 } ( 1 + \lambda ) ^ { 2 } T ^ { 3 } ( \alpha ^ { 2 } + \overset { \smile } { \beta ^ { 2 } } ) } { 3 ( C + C _ { R } ) } ) = \widehat { U } _ { M } + \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } ( 1 + \lambda ) ^ { 2 } T ^ { 3 } \alpha ^ { 2 } } { 3 ( C + C _ { R } ) ^ { 2 } } \quad , } \end{array}$ and the MSSP exerts effort $\begin{array} { r } { \bar { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { C + C _ { R } } . } \end{array}$ Four scenarios may occur when the CI firm monitors security efforts: (1) both parties exert the required effort; (2) only the MSSP exerts the required effort; (3)

only the client exerts the required effort; and (4) neither party exerts the required effort. Lemma 3 indicates that $\bar { e } _ { M } ( t )$ and $\bar { e } _ { F } ( t )$ are the subgame perfect equilibrium in the game. The subgame perfect equilibrium implies that the solution provides credible threats so that no player can benefit from deviating from the announced strategy (Sorger, 1989). Therefore, only the first scenario will occur, i.e., both parties exerting the effort required by the CI firm.

Based on Lemma 3, we find that when $C _ { R } = 0$ $\bar { e } _ { M } ( t ) = e _ { M } ^ { * } ( t )$ and $\bar { e } _ { F } ( t ) = e _ { F } ^ { * } ( t )$ . Thus, when the variable monitoring cost ${ \bf \Xi } ( C _ { R } )$ is negligible, both parties’ security efforts can achieve their respective benchmark efforts and the DMH problem can be solved. When $C _ { R }$ is not negligible, the CI firm’s variable cost of monitoring security efforts prevents both parties from setting a high level of security effort, thus, neither party’s security effort reaches their respective benchmark efforts.

We now answer the third question. Lemma 3 indicates that the compensation coefficient $( s _ { F } ^ { * } )$ and penalty coefficient $( s _ { M } ^ { * } )$ are decided by many parameters such as output sensitivity, system interdependency, attack probability, and the length of the contract horizon. Thus, the monitoring contract is challenging to implement and the CI firm must evaluate all these parameters before<sup>( ( ), ( ))</sup>Fi Fi Mi<sup>U e t e t =</sup> implementing the monitoring contract.

In conclusion, the proposed monitoring contract has two shortcomings. First, the monitoring contract can solve the DMH problem only when the variable monitoring cost is negligible. Second, it is challenging to evaluate the appropriate compensation and penalty in the case of a breach. Thus, both the high monitoring costs and the complex monitoring process may potentially impede the implementation of the proposed contract. An MSSP should offer an easily implementable contract that can solve the DMH problem without any constraints. We next turn our attention to the liability contract, which has the capacity to solve the problems associated with the other contract type.

## 4.3 The Liability Contract

In this section, we consider the liability contract, which is based on outcome control. In contrast to behavior control, outcome control mainly focuses on outsourcing engagement outputs and is indifferent to internal processes. The liability contract assumes that the MSSP compensates clients based on the outcome of security breaches, as described in the following assumption:

Assumption 5: Under the liability contract, client ?? pays a fixed fee ?? to the MSSP. A compensation combination $D = ( d _ { b b } , d _ { b n } , d _ { n b } )$ will be returned by the MSSP to the client, where the MSSP compensates each client ${ \bf d _ { \mathrm { { b b } } } }$ if both clients are breached, compensates the breached client ${ \bf d } _ { { \bf b } { \bf n } }$ and the unbreached client $d _ { n b }$ if only one client is breached. Further, the MSSP incurs a fixed implementation cost $C _ { V }$ to enforce the contract.

Assumption 5 requires the MSSP to differentiate breached clients and unbreached clients. In practice, three reasons can explain why breach events are public information (Lee et al., 2013). First, many firms in the United States are legally required to disclose security breaches to the public. Second, social word-of-mouth can spread breach information to the public. Third, firms may suffer continuous losses when breached; thus, firms have incentives to disclose breaches to their MSSP in a timely manner. Based on Assumption 5, the expected respective payoffs for the MSSP and client ?? are as follows:

$$
\begin{array}{l} U _ {M} \left(e _ {F 1} (t), e _ {F 2} (t), e _ {M 1} (t), e _ {M 2} (t)\right) = f _ {1} + f _ {2} - \\ \int_ {0} ^ {T} \left\{ \begin{array}{l} 2 p _ {1} (t) p _ {2} (t) d _ {b b} + p _ {1} (t) \left(1 - p _ {2} (t)\right) \left(d _ {b n} + d _ {n b}\right) \\ + \left(1 - p _ {1} (t)\right) p _ {2} (t) \left(d _ {n b} + d _ {b n}\right) + \frac {C}{2} \left(e _ {M 1} ^ {2} (t) + e _ {M 2} ^ {2} (t)\right) \end{array} \right\} d t - C _ {V}, \end{array}
$$

$$
\begin{array}{l} U _ {F i} \left(e _ {F i} (t), e _ {M i} (t)\right) = V (T) - f _ {i} - \\ \int_ {0} ^ {T} \left\{ \begin{array}{l} \left(p _ {i} (t) + \lambda p _ {3 - i} (t)\right) L - p _ {i} (t) p _ {3 - i} (t) d _ {b b} \\ - p _ {i} (t) \left(1 - p _ {3 - i} (t)\right) d _ {b n} - \left(1 - p _ {i} (t)\right) p _ {3 - i} (t) d _ {n b} + \frac {C}{2} e _ {F i} ^ {2} (t) \end{array} \right\} d t, \end{array} \tag {8}
$$

where $p _ { i } ( t ) = a ( 1 - q _ { i } ( t ) ) , i = 1 , 2$ . In the above Equations (7) and (8), $p _ { 1 } ( t ) p _ { 2 } ( t ) d _ { b b }$ represents the MSSP’s compensation to clients when both clients are breached, $p _ { 1 } ( t ) ( 1 - p _ { 2 } ( t ) ) d _ { b n }$ represents the MSSP’s compensation to the breached client when only one client is breached and $( 1 - p _ { 1 } ( t ) ) p _ { 2 } ( t ) d _ { n b }$ represents the MSSP’s compensation to the unbreached client when only one client is breached. The problem faced by the MSSP in Stage 1 is presented in the proof of Lemma 4 in Appendix A.

The following lemma characterizes the proposed contract:

Lemma 4: Under the liability contract, the MSSP sets the service fee $\begin{array} { r } { \tilde { f } = V ( T ) - { U _ { F } } - \frac { { { \varepsilon ^ { 2 } } { a ^ { 2 } } { L ^ { 2 } } ( 1 + \lambda ) ^ { 2 } { T ^ { 3 } } \alpha ^ { 2 } } } { 6 C } } \end{array}$ and the compensation combination $\widetilde D =$ $( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } )$ , where $\tilde { d } _ { b b } = ( 1 + \lambda ) L$ ${ \tilde { d } } _ { n b } =$ $( 1 + 2 \lambda ) L _ { \mathrm { ~ ~ } }$ , and $\tilde { d } _ { b n } = - \lambda L$ . The MSSP exerts effort $\begin{array} { r } { \tilde { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { c } } \end{array}$ and the client exerts effort $\begin{array} { r } { \tilde { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ( 1 + \lambda ) ( T - t ) } { C } , } \end{array}$

Lemma 4 answers the first question, indicating that both the MSSP and the client have incentives to exert benchmark efforts under the liability contract; thus the liability contract can eliminate both parties’ DMH problem without any conditions. The following proposition answers the second question:

Proposition 2: In a liability contract, if both clients are breached, the MSSP compensates each client with (1 + ??)?? . If only one client is breached, the breached client compensates the MSSP with ???? and the MSSP rewards the unbreached client with (1 + 2??)??.

Proposition 2 makes the operating mechanism behind the proposed contract clear. However, what we are interested in is how this operating mechanism can eliminate both parties’ DMH problem. We first analyze the client’s incentive. When client ?? is breached, it incurs a loss ?? and client ?? incurs an indirect loss ???? caused by the system interdependency. Under the BRC, client i’s expected payoff contains only its own expected loss but does not account for client j’s indirect loss. However, under the liability contract, client ?? takes full liability for the loss it causes, including its own security loss ?? and client j’s indirect loss ???? . Thus, when maximizing its own expected payoff, client ?? will try to reduce the likelihood of facing severe damage by investing more in its security effort. The magnitude of ???? ensures that client i’s increased security effort precisely matches its own benchmark effort.

Next, we analyze the MSSP’s incentive of exerting the benchmark effort under the liability contract. As evidenced by the proofs of Lemma 2 and Lemma 4, as the principal, the MSSP’s incentive is always to maximize social welfare, no matter what the contract type is. Thus, when the liability contract induces clients to exert the benchmark efforts, it is optimal for the MSSP to also exert its own benchmark effort to maximize social welfare. As discussed in Lemma 2, $\hat { e } _ { M } ( t ) = e _ { M } ^ { * } ( t )$ only when $\phi _ { i } = 1$ . Thus, to exert its benchmark effort, the MSSP needs to take full responsibility for the breach, i.e., the MSSP is penalized by (1 + ??)?? for each breach.

In conclusion, two scenarios occur under the liability contract. First, when client ?? is breached and client ?? is not, the MSSP is penalized by (1 + ??)?? and client i’s penalty is ???? for the breach. The total penalty (1 +

2??)?? is offered to client ??, and thus client j’s total loss is $- ( 1 + 2 \lambda ) L + \lambda L = - ( 1 + \lambda ) L$ . Thus, client ?? is rewarded (1 + ??)?? for suffering an indirect loss while keeping itself secure. We find that under the operating mechanism of the liability contract, the MSSP penalizes the breached client and rewards the unbreached client, thereby making the breached client “poorer” and the unbreached “richer.” Second, when both clients are breached, the MSSP’s penalty is 2(1 + ??)?? for the two breaches, client ?? is penalized by ???? for its breach and rewarded by (1 + 2??)?? for suffering an indirect loss. The same would be the case for client ??. As a result, the MSSP pays compensation (1 + ??)?? to each client when both clients are breached. Table 2 summarizes the penalties and rewards under all scenarios of the liability contract case.

We now answer the third question. Based on Lemma 4, we find the new compensation combination ??<sup>̃</sup> = $( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } )$ under the liability contract is only related to the system interdependency and security loss and has nothing to do with other parameters. As mentioned above, the system interdependency can be estimated using data from the past breaches. Thus, since it is easy to evaluate the compensation combination, the liability contract is easy to implement, which is an advantage compared to BRC and monitoring contracts.

## 5 Comparison of the Three Contract Types: Bilateral Refund, Monitoring, and Liability

For a deeper comparison of the three contract types, we conduct the comparative statics of output sensitivities and system interdependency among different contract types and identify the optimal contract choices for the principals. Table 3 lists the optimal security efforts for both the MSSP and the client in the benchmark case and the three contractual arrangements.

Table 2. Penalties and Rewards under all Scenarios of the Liability Contract Case

<table><tr><td></td><td colspan="3">Only client i is breached</td><td colspan="3">Only client j is breached</td><td colspan="3">Both clients are breached</td></tr><tr><td></td><td>Security loss</td><td>Penalty</td><td>Total loss</td><td>Security loss</td><td>Penalty</td><td>Total loss</td><td>Security loss</td><td>Penalty</td><td>Total loss</td></tr><tr><td>MSSP</td><td>0</td><td>(1+λ)L</td><td>(1+λ)L</td><td>0</td><td>(1+λ)L</td><td>(1+λ)L</td><td>0</td><td>2(1+λ)L</td><td>2(1+λ)L</td></tr><tr><td>Client i</td><td>L</td><td>λL</td><td>(1+λ)L</td><td>λL</td><td>-(1+2λ)L</td><td>-(1+λ)L</td><td>(1+λ)L</td><td>-(1+λ)L</td><td>0</td></tr><tr><td>Client j</td><td>λL</td><td>-(1+2λ)L</td><td>-(1+λ)L</td><td>L</td><td>λL</td><td>(1+λ)L</td><td>(1+λ)L</td><td>-(1+λ)L</td><td>0</td></tr></table>

Table 3. Contract Comparison

<table><tr><td>Contract types</td><td>The MSSP&#x27;s security effort</td><td>The client&#x27;s security effort</td></tr><tr><td>Benchmark case</td><td> $e_{M}^{*}(t) = \frac{\varepsilon aL\beta(1 + \lambda)(T - t)}{C}$ </td><td> $e_{F}^{*}(t) = \frac{\varepsilon aL\alpha(1 + \lambda)(T - t)}{C}$ </td></tr><tr><td>Bilateral refund contract</td><td> $\hat{e}_{M}(t) = \frac{\varepsilon aL\beta(1 + \lambda)(\beta^{2}(1 + \lambda)^{2} - \lambda\alpha^{2})(T - t)}{C(\beta^{2}(1 + \lambda)^{2} + \alpha^{2})}$ </td><td> $\hat{e}_{F}(t) = \frac{\varepsilon aL\alpha^{3}(1 + \lambda)(T - t)}{C(\beta^{2}(1 + \lambda)^{2} + \alpha^{2})}$ </td></tr><tr><td>Monitoring contract</td><td> $\bar{e}_{M}(t) = \frac{\varepsilon aL\beta(1 + \lambda)(T - t)}{C + C_{R}}$ </td><td> $\bar{e}_{F}(t) = \frac{\varepsilon aL\alpha(1 + \lambda)(T - t)}{C + C_{R}}$ </td></tr><tr><td>Liability contract</td><td> $\tilde{e}_{M}(t) = \frac{\varepsilon aL\beta(1 + \lambda)(T - t)}{C}$ </td><td> $\tilde{e}_{F}(t) = \frac{\varepsilon aL\alpha(1 + \lambda)(T - t)}{C}$ </td></tr></table>

## 5.1 Comparative Statics

This section compares the impact of output sensitivity and system interdependency on both parties’ security efforts in terms of the three contract types.

Proposition 3: (a) Under the bilateral refund contract,

$$
\left\{ \begin{array}{l} \frac {\partial \hat {e} _ {M} (t)}{\partial \beta} > 0 \\ \frac {\partial \hat {e} _ {F} (t)}{\partial \beta} <   0 \end{array} \right. \mathrm{and} \left\{ \begin{array}{l} \frac {\partial \hat {e} _ {F} (t)}{\partial \alpha} > 0 \\ \frac {\partial \hat {e} _ {M} (t)}{\partial \alpha} <   0 \end{array} ; \right.
$$

and (b) under the monitoring and liability contracts,

$$
\left\{ \begin{array}{l} \frac {\partial e _ {M} (t)}{\partial \beta} > 0 \\ \frac {\partial e _ {F} (t)}{\partial \beta} = 0 \end{array} \right. \text {and} \left\{ \begin{array}{l} \frac {\partial e _ {F} (t)}{\partial \alpha} > 0 \\ \frac {\partial e _ {M} (t)}{\partial \alpha} = 0 \end{array} . \right.
$$

Proposition 3 shows the differences in how both parties’ output sensitivities affect their optimal security efforts in terms of the three contract types. Proposition 3(a) shows that, under the BRC, one party’s security effort increases with its own output sensitivity but decreases with the other’s, which captures the effort interaction between the MSSP and the client under the BRC. As the MSSP becomes more productive $( \mathrm { i . e . , } \beta$ increases) because of the adoption of new security technology, it would want the client firm to outsource more security functions to it. The MSSP would thus have an incentive to exert additional security efforts $( \mathrm { i . e . , ~ } \frac { \partial \hat { e } _ { M } ( t ) } { \partial \beta } > 0 )$ and reduce the client’s security efforts $( \mathrm { i . e . , } \frac { \partial \hat { e } _ { F } ( t ) } { \partial \beta } < 0 )$ , which can be achieved by increasing the compensation. Similarly, as the client’s output sensitivity increases (i.e., ?? increases), it is beneficial for the MSSP to decrease the optimal compensation to entice the client to devote more effort toward its own security $\begin{array} { r } { ( \mathrm { i . e . , } \frac { \partial \hat { e } _ { F } ( t ) } { \partial \alpha } > 0 ) } \end{array}$ so that the MSSP can accordingly decrease its own level of effort $( \mathrm { i . e . , } \frac { \partial \hat { e } _ { M } ( t ) } { \partial \alpha } < 0 )$

However, as stated above, both parties perform their respective duties and exert effort in strict accordance with their respective output sensitivities under the monitoring and liability contracts. As a result, one party’s security effort increases with its own output sensitivity but has nothing to do with the other party’s output sensitivity, as stated in Proposition 3(b).

Proposition 4: (a) Under the bilateral refund contract,

$$
\begin{array}{r l} & {\left\{ \begin{array}{l l} \frac {\partial \hat {e} _ {M} (t)}{\partial \lambda} <   0 \mathrm{when} \lambda <   \lambda_ {0} \\ \frac {\partial \hat {e} _ {M} (t)}{\partial \lambda} > 0 \mathrm{when} \lambda > \lambda_ {0} \end{array} \right.,} \\ & {\left\{ \begin{array}{l l} \frac {\partial \hat {e} _ {F} (t)}{\partial \lambda} > 0 \mathrm{when} \lambda <   \lambda_ {1} \\ \frac {\partial \hat {e} _ {F} (t)}{\partial \lambda} <   0 \mathrm{when} \lambda > \lambda_ {1} \end{array} , \left\{ \begin{array}{l l} \frac {\partial \hat {\phi}}{\partial \lambda} <   0 \mathrm{when} \lambda <   \lambda_ {1} \\ \frac {\partial \hat {\phi}}{\partial \lambda} > 0 \mathrm{when} \lambda > \lambda_ {1} \end{array} , \right. \right.} \\ & {\mathrm{where} \quad \frac {(1 + \lambda_ {0}) ^ {2}}{\sqrt {2 (1 + \lambda_ {0})} - 1} = \frac {\alpha^ {2}}{\beta^ {2}} \quad \mathrm{and} \quad \lambda_ {1} = \frac {\alpha - \beta}{\beta};} \end{array}
$$

and (b) under the monitoring contract and liability contract, both parties’ security efforts increase with ??.

One party always faces the trade-off between investment risk and security risk when making security decisions. Investment risk implies the risk of overspending on security, and security risk implies the risk of loss from security breaches (Wu et al., 2017). Higher system interdependency indicates a higher risk of loss faced by the client, which implies that a higher security risk is suffered by both parties. Thus, we can expect that with higher system interdependency, both the MSSP and the client would exert more security effort to reduce the security risk. However, Proposition 4 suggests that this intuition is not always correct under the BRC, but it is correct under the monitoring and liability contracts.

We first discuss the BRC. Proposition 4(a) shows that the MSSP’s effort is U-shaped in system interdependency. Two countervailing effects influence the MSSP’s incentive. First, a high investment risk caused by increasing effort costs discourages the MSSP from investing in security since the MSSP is concerned about overspending on security. Second, a high-security risk caused by intensified system interdependency forces the MSSP to increase its effort in order to reduce the probability of a breach and ensure that its client can access the reservation utility. When system interdependency is low, the MSSP’s security risk is relatively lower compared to investment risk; thus, the MSSP reduces its efforts in order to reduce the high investment risk $\mathrm { ( i . e . , } \frac { \partial \hat { e } _ { M } ( t ) } { \partial \lambda } <$ 0 ??ℎ???? $\lambda < \lambda _ { 0 } \quad )$ Conversely, when system interdependency becomes high, security risk is relatively higher than investment risk. As a result, the MSSP exerts more efforts to decrease the high security risk $\mathrm { ( i . e . , } \frac { \partial \hat { e } _ { M } ( t ) } { \partial \lambda } > 0$ ??ℎ???? $\lambda > \lambda _ { 0 } )$

Proposition 4(a) also shows that, unlike the MSSP, the client’s effort is inverse U-shaped in terms of system interdependency. A client’s effort can only improve its own security quality and does not affect other clients; thus, the client cannot directly reduce its own security risk caused by system interdependency. System interdependency affects the client’s effort through the MSSP’s compensation indirectly, which is also verified by the proof of Lemma 2 (i.e., $\hat { e } _ { F i } ( t ) =$ $\frac { \varepsilon a L \alpha ( 1 - \phi _ { i } ) ( \bar { T } - t ) } { C } \rangle$ ). To maximize its expected payoff, the client increases its effort to reduce expected loss when the MSSP decreases compensation and decreases its effort to save effort cost when the MSSP increases compensation. That is, the client’s effort follows an opposite pattern with the compensation. Thus, it is only necessary to explore the relationship between the compensation coefficient and system interdependency.

To understand the relationship between the compensation coefficient and system interdependency, we discuss the role of ?? in three situations: $\lambda \leq \lambda _ { 0 }$ $\lambda _ { 0 } < \lambda \leq \lambda _ { 1 }$ , and $\lambda > \lambda _ { 1 }$ . When ?? is at a low level $( \mathrm { i } . \mathrm { e } . , \lambda \leq \lambda _ { 0 } )$ , the MSSP faces a low security risk and thus decreases its effort, as a result, it is rational for the MSSP to decrease compensation to entice the client to exert more effort $\begin{array} { r } { ( \mathrm { i . e . , ~ } \frac { \partial \hat { \phi } } { \partial \lambda } < 0 , \frac { \partial \hat { e } _ { F } ( t ) } { \partial \lambda } > 0 } \end{array}$ when $\lambda <$ $\lambda _ { 0 } )$ . When ?? is at a moderate level (i.e., $\lambda _ { 0 } < \lambda \leq \lambda _ { 1 } )$

the MSSP begins to increase its effort. In this case, both the $\mathrm { M S S P ^ { \circ } s }$ security risk and investment risk increase. To maximize its expected payoff, the MSSP will reduce compensation, and the client will respond by increasing its effort (i.e., $\begin{array} { r } { \frac { \partial \widehat \phi } { \partial \lambda } < 0 , \frac { \partial \hat { e } _ { F } ( t ) } { \partial \lambda } > } \end{array}$ 0 when $\lambda _ { 0 } < \lambda < \lambda _ { 1 } )$ . Once ?? becomes high enough $( \mathrm { i . e . , } \lambda > \lambda _ { 1 } )$ , meaning that the security risk is also high enough, to ensure that the clients can access reservation utility, the MSSP must increase its effort at a faster rate and also increase compensation to make it attractive for clients to outsource their security functions, which in turn leads to the client decreasing its effort $\begin{array} { r } { ( \mathrm { i . e . , } \frac { \partial \hat { \phi } } { \partial \lambda } > 0 , \frac { \partial \hat { e } _ { F } ( t ) } { \partial \lambda } < 0 \mathrm { w h e n } \lambda > \lambda _ { 1 } ) } \end{array}$

Proposition 4(b) indicates that, in contrast to the BRC case, both parties’ security efforts increase with system interdependency under the monitoring and liability contracts. As mentioned above, both parties perform their respective duties and exert efforts in strict accordance with their respective responsibility under the monitoring and liability contracts. This suggests that the MSSP will not overspend on security efforts and thus will not face investment risk under these contracts. Higher system interdependency leads to a higher security risk, and thus the MSSP and the client must increase their security efforts to decrease the security risk.

Figure 2 shows that Proposition 4(a) results from the numerical analysis where $\alpha = 1 . 6 , \beta = 1 , a = 0 . 1 , C =$ $1 0 , \varepsilon = 0 . 1 , L = 2 0 0 , T = 1 0 , t = 5$ (The results are similar when these values are varied), and $\lambda _ { 0 } = 0 . 1 5$ $\lambda _ { 1 } = 0 . 6$ . Since $\phi \in ( 0 , 1 )$ , we magnify $\hat { \phi }$ five times to show the three relationships in one figure.

![](/api/attachments/HQ737GJB/fulltext/images/6c334edb78caa1aec24a85866f9cd734783168806b74f7cde05b431c5ffed7e9.jpg)  
Figure 2. Numerical Analysis of Proposition 4(a)

## 5.2 Choices for the Principals

This section analyzes the fourth question about the two new proposed contracts, i.e., Is the proposed contract worth implementing for the principal? We answer this question by comparing the above three contracts from the perspective of information security participants, including clients, the CI firm, and the MSSP. This analysis can guide practitioners in selecting the most beneficial contract while establishing a value cocreation environment. Since clients are not the principal in any of the three contract scenarios, they are not involved in choosing contracts and their expected payoff is always equal to their reservation utility. We now focus on the choice of the principals, i.e., the CI firm and the MSSP.

The CI firm has an incentive to implement the monitoring contract only when its expected payoff is positive. We state the CI firm’s expected payoff $\bar { U } _ { R } =$ $\frac { { \varepsilon } ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 2 } } { 3 } ( \frac { \alpha ^ { 2 } + \beta ^ { 2 } } { C + C _ { R } } - \frac { \beta ^ { 4 } ( 1 + \lambda ) ^ { 2 } + { \alpha } ^ { \dot { 2 } } ( \alpha ^ { 2 } + \beta ^ { 2 } ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } ) - F _ { R }$ . We offer the following proposition regarding the choices of the CI firm:

Proposition 5: The CI firm has the incentive to implement the monitoring contract only if the fixed monitoring cost is lower than a certain threshold, i.e., ??<sub>??</sub> < ??<sub>??0</sub> where $F _ { R 0 } =$ $\frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 2 } } { 3 } ( \frac { \ddot { \alpha } ^ { 2 } + \beta ^ { 2 } } { C + C _ { R } } - \frac { \beta ^ { 4 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ( \alpha ^ { 2 } + \beta ^ { 2 } ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } )$

Proposition 5 indicates that a high monitoring cost restrains the CI firm’s motive to implement the monitoring contract. Further, $F _ { R 0 }$ increases with attack probability, system interdependency, and time horizon. Thus, we can conclude that high system interdependency, a high probability of undirected attacks, or a long contract horizon enhances the incentive of the CI firm to implement the monitoring contract.

Indeed, the motivation for the CI firm to implement the proposed contract should be driven not only by achieving savings in monitoring costs through efficient use of IT but also by the realization that improving the trust between the CI firm and the MSSP (and clients) will result in greater acceptance of the monitoring contract. Prior literature has treated control and trust as a complementary relationship—that is, the more trust there is, the less need for control there is, and vice versa (Das & Teng, 1998). Thus, when the CI firm and the MSSP (and clients) have a high degree of trust based on their prior cooperation, the control cost of monitoring efforts is reduced, leading to the CI firm having a higher incentive to implement the monitoring contract.

We now focus on the choice of the MSSP by discussing the fourth question of the liability contract, i.e., is it worth implementing the liability contact for the MSSP? For the MSSP, there is no difference in expected payoff between the BRC and the monitoring contract. Thus, we only discuss the MSSP’s choice between the BRC and the liability contract.

An implication of Proposition 2 is that the liability contract makes the poorer client even “poorer” and the richer client even “richer.” Thus, before signing the liability contract, the MSSP should investigate clients’ attitudes toward the new contract and entice them to accept it. However, if breaches occur, the breached client may be reluctant to pay the penalty exacted by the MSSP, potentially leading the MSSP to sue the client. Therefore, we assume that the MSSP needs to expend a fixed implementation cost $C _ { V }$ to ensure that both players will abide by the liability contract. $C _ { V }$ may comprise investigation fees, legal fees, and so forth. For example, the Cardsystems/Savvis breach resulted in a lengthy and expensive legal battle (Zetter, 2009); MSSPs should seek to avoid such outcomes.

Proposition 6: The MSSP prefers the liability contract over the bilateral refund contract if the fixed implementation cost $C _ { V }$ is lower than a threshold, i.e., $C _ { V } < C _ { 0 } ,$ , where $\begin{array} { r } { C _ { 0 } = \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 4 } \alpha ^ { 2 } \beta ^ { 2 } } { 3 C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } . } \end{array}$

Viewed from the perspective of the MSSP, the liability contract dominates the BRC when the implementation cost of the liability contract is smaller than the threshold $C _ { 0 } . C _ { 0 }$ is the actual gap between the MSSP’s expected payoff under the liability contract and that under the BRC. Thus, even the fixed implementation cost $C _ { V }$ may not be easy to estimate because of the newness of the liability contract, we can explore the magnitude of $C _ { 0 }$ to help MSSPs choose a better contract form. We obtain the following two interesting insights through an analysis of the threshold.

First, $C _ { 0 }$ increases with attack probability, system interdependency, and time horizon. Thus, we can conclude that MSSPs prefer the liability contract over the BRC when they face high system interdependency, a high probability of undirected attack, or a long contract horizon.

Second, while keeping the total of both parties’ output sensitivities as a constant, $C _ { 0 }$ first increases and then decreases with either party’s output sensitivity. The setting that maintains the total of both parties’ output sensitivities as a constant and changes one party’s output sensitivity can be regarded as a responsibility assignment between the MSSP and the client. This insight indicates that the MSSP has an incentive to choose the liability contract when both parties have nearly equal responsibility for improving security quality. Proposition 1(a) indicates that both parties suffer the worst DMH problem when both parties have nearly equal responsibility, and thus the BRC performs worst in this case. However, there is no DMH problem under the liability contract. Thus, the MSSP would prefer the liability contract over the BRC when both parties have nearly equal responsibility for improving security quality.

Finally, we should note that to solve the DMH problem under the BRC, the CI firm must undertake monitoring costs under the monitoring contract and the MSSP must undertake implementation costs under the liability contract. Thus, under these two new contract types, social welfare will always be lower than that under the benchmark case because of the associated monitoring and implementation costs.

## 6 Extensions

To generalize the proposed contracts, we further extend the analysis of the basic model in two directions. First, we allow the $\mathrm { M S S P ^ { \circ } s }$ security efforts to have a spillover effect on the clients. Second, we allow the MSSP to serve three or more clients.

## 6.1 Spillover Effect of Security Efforts

Thus far, our model has assumed that an MSSP’s security efforts regarding different clients are independent of each other. However, an MSSP serving multiple clients can enhance its investment effectiveness by improving security technologies and implementation, thus benefitting all clients (Zhao et al., 2013). An MSSP’s effort in terms of a particular client may have a spillover effect on other clients and this beneficial effect is obvious when facing undirected attacks since undirected attacks may be more pervasive, massive, and easier to address. This section relaxes the assumption of independent effort to account for the spillover effect.

Assumption 6: Client i’s instantaneous increase in security quality is $\dot { q } _ { i } ( t ) = \varepsilon ( \alpha e _ { F i } ( t ) + \beta e _ { M i } ( t ) +$ $h \beta e _ { M ( 3 - i ) } ( t ) ) , i = 1 , 2$ , where h represents the spillover effect.

We omit the analysis and give the following Lemma directly:

Lemma 5: When considering the spillover effect,

(a) The benchmark efforts of the MSSP and the client are $\begin{array} { r } { e _ { M } ^ { \ast } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( 1 + h ) ( T - t ) } { C } \mathrm { a n d } e _ { F } ^ { \ast } ( t ) = } \end{array}$ $\frac { \varepsilon a L \alpha ( 1 + \lambda ) ( T - t ) } { C } ,$

(b) In the bilateral refund contract, the MSSP utilizes a compensation coefficient $\hat { \phi } =$ $\frac { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } ( 1 + h ) ^ { 2 } - \lambda \alpha ^ { 2 } } { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } ( 1 + h ) ^ { 2 } + \alpha ^ { 2 } }$ , and exerts effort $\hat { e } _ { M } ( t ) =$ $\dot { \varepsilon } a L \dot { \beta } ( 1 + \lambda ) ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } ( 1 + h ) ^ { 2 } - \lambda \alpha ^ { 2 } ) ( T - t )$ , the client exerts ??(??<sup>2</sup>(1+??)<sup>2</sup>(1+ℎ)<sup>2</sup>+??<sup>2</sup>) effort $\begin{array} { r } { \hat { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ^ { 3 } ( 1 + \lambda ) ( T - t ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } ( 1 + h ) ^ { 2 } + \alpha ^ { 2 } ) } ; } \end{array}$

(c) Under the monitoring contract, the MSSP exerts effort $\begin{array} { r } { \bar { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \bigcup ( 1 + h ) ( T - t ) } { C + C _ { B } } } \end{array}$ , and the client exerts effort $\begin{array} { r } { \bar { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ( \ddot { ( 1 + \lambda ) } ( T - t ) } { C + C _ { R } } ; } \end{array}$

(d) Under the liability contract, the compensation combination is $\widetilde { D } = ( \widetilde { d } _ { b b } , \widetilde { d } _ { b n } , \widetilde { d } _ { n b } )$ , where $\tilde { d } _ { b b } =$ $( 1 + \lambda ) L , \tilde { d } _ { n b } = ( 1 + 2 \lambda ) L$ , and $\tilde { d } _ { b n } = - \lambda L$ . The MSSP exerts effort $\begin{array} { r } { \tilde { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( 1 + h ) ( T - t ) } { c } } \end{array}$ and the client exerts effort $\begin{array} { r } { \tilde { e } _ { F } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { C } . } \end{array}$

The underlying insights of Lemma 5 are as follows. First, the spillover effect does not affect the client’s benchmark effort but improves the $\mathrm { M S S P ^ { \circ } s }$ benchmark effort. This is because we assume that only the $\mathrm { M S S P ^ { \circ } s }$ security effort has a spillover effect on security quality, which leads to an increase in security quality, and as a result, the MSSP can benefit from the spillover effect. Second, both parties’ new BRC efforts are still weaker than their own new benchmark efforts; that is, the DMH problem still arises under the BRC when considering the spillover effect, which is similar to Lemma 2. Third, under the monitoring contract, when the variable monitoring cost is negligible, both parties’ security efforts under the spillover effect can still achieve their new respective benchmark efforts and solve the DMH problem, similar to Lemma 3. Fourth, both the MSSP and the client exert benchmark efforts under the liability contract, which means that the liability contract still works and can eliminate both parties’ DMH problem when considering the spillover effect. Moreover, the compensation combination under the liability contract remains unchanged when considering the spillover effect. The operating mechanism of the liability contract forces both parties to take full liability for the breaches by penalizing the breached client and rewarding the unbreached client. Thus the compensation combination relies only on the security loss and system interdependency and has nothing to do with other factors such as the spillover effect.

## 6.2 The Case of Three or More Clients

In this section, we extend the model from two clients to three or more clients served by the MSSP. Here we focus on the liability contract. We omit analysis of the BRC and monitoring contracts for brevity because these contract types are similar to the liability contract in this case.

Assume that the MSSP serves ?? clients, where $N \geq 3$ Hackers attack ?? out of ?? clients during the contract period where $1 \leq k \leq N$ . When the MSSP serves two clients, we find that under the liability contract, if client ?? is breached, the MSSP incurs a penalty of $L + ( N -$ 1)???? for this breach, and client ?? has a penalty of (?? − 1)???? for this breach since it causes every client excluding client ?? to suffer a system interdependency loss. Thus, the total reward for the other $N - 1$ clients is $L + 2 ( N - 1 ) \lambda L , { \mathrm { i . e . } }$ , every client excluding client ?? obtains a reward $\frac { L + 2 ( N - 1 ) \bar { \lambda } L } { N - 1 }$ . Since ?? clients are breached, every un-breached client will be rewarded $\begin{array} { r } { k \frac { L + 2 ( N - 1 ) \lambda L } { N - 1 } } \end{array}$ , and the breached clients will be rewarded $k - 1$ times (client ?? will not be compensated by the MSSP when it suffers a breach itself), i.e., every breached client will obtain a reward $\begin{array} { r } { ( k - 1 ) \frac { L + 2 ( N - 1 ) \lambda \bar { L } } { N - 1 } . } \end{array}$ As mentioned before, since the breached client ?? has a penalty $( N - 1 ) \lambda L$ for its own breach and also obtains a reward of $\begin{array} { r } { ( k - 1 ) \frac { L + 2 ( N - 1 ) \lambda L } { N - 1 } } \end{array}$ , client $i \ ' \mathbf { s }$ total compensation offered by the MSSP is (?? − $\begin{array} { r } { 1 ) \frac { L + \overline { { 2 } } ( N - 1 ) \lambda L } { N - 1 } - ( N - 1 ) \lambda L = \frac { \overline { { ( k - 1 ) L } } } { N - 1 } + ( 2 k - N - 1 ) \lambda L } \end{array}$

Proposition 7: Under the liability contract, when the MSSP serves ?? clients, if ?? out of the ?? clients are breached during the contract period,

(a) if client ?? is not breached, the MSSP compensates client ?? with $k ( \frac { L } { N - 1 } + 2 \lambda L )$ ;

(b) if client ?? is breached, the MSSP compensates client ?? ??????ℎ $\begin{array} { r } { \frac { ( k - 1 ) L } { N - 1 } + ( 2 k - N - 1 ) \lambda L . } \end{array}$

Next, we verify whether efforts under the proposed contract can achieve benchmark efforts. Here we assume the probability that ?? out of ?? clients are breached during the contract horizon is $p _ { k } ( t ) = a ( 1 -$ $q _ { k } ( t ) )$ . Then the benchmark payoff is given by the following:

$$
\begin{array}{l} S W = N V (T) - \int_ {0} ^ {T} [ p _ {k} (t) k (1 + (N - 1) \lambda) L - \\ + \frac {N}{2} C e _ {F i} ^ {2} (t) + \frac {N}{2} C e _ {M i} ^ {2} (t) ] d t - C _ {V} \end{array}\tag{9}
$$

The expected payoffs for the MSSP and clients under the liability contract are given by the following:

$$
\begin{array}{l} U _ {M} = N f - \int_ {0} ^ {T} p _ {k} (t) \left\{k \left(\frac {(k - 1) L}{N - 1} + (2 k - N - 1) \lambda L\right) + \right. \\ \left. (N - k) k \left(\frac {L}{N - 1} + 2 \lambda L\right) + \frac {N}{2} C e _ {M} ^ {2} (t) \right\} d t - C _ {V} \end{array}\tag{10}
$$

$$
\begin{array}{l} U _ {F} = N V (T) + \int_ {0} ^ {T} [ p _ {k} (t) \\ \left\{ \begin{array}{l} - k (1 + (N - 1) \lambda) L + k (\frac {(k - 1) L}{N - 1} + (2 k - N - 1) \lambda L) \\ + (N - k) k (\frac {L}{N - 1} + 2 \lambda L) + \frac {N}{2} C e _ {F} ^ {2} (t) \end{array} \right\} ] d t - N f \end{array}\tag{11}
$$

We find that $\tilde { e } _ { M } ( t ) = e _ { M } ^ { * } ( t )$ and $\tilde { e } _ { F } ( t ) = e _ { F } ^ { * } ( t )$ , which is established under the contract in Proposition 7. Thus, the liability contract can be extended to the case in which an MSSP serves three or more clients.

## 7 Conclusion

This paper emphasizes that the management of information security outsourcing is usually undertaken in a dynamic cooperation environment. We construct a differential game framework, in which the task of improving security quality depends on the security efforts of both an MSSP and its clients; their allocation of efforts can change throughout the contract duration. Moreover, two distinctive characteristics of security outsourcing, hacker behavior and system interdependency, complicate the contractual arrangement between an MSSP and its clients. Considering these facts, we discuss various contractual arrangements and compare their performance against the benchmark solution, where an MSSP and its clients are vertically integrated.

We first discuss the bilateral refund contract, which is a widely adopted contractual type in the MSSP industry. We show that the BRC can induce a DMH problem since neither the MSSP nor its clients take full liability for breaches. We observe that either monitoring security efforts or making both parties take full liability can solve the DMH problem. Thus, we propose two new contract types. One is the monitoring contract, in which both the security efforts of the MSSP and clients are monitored by a cyberinsurance firm. The other is the liability contract, in which both parties take full liability for breaches by rewarding clients who are well protected and penalizing clients who are breached by hackers. We find that the DMH problem can be solved only when the variable monitoring cost is negligible under the monitoring contract, while it is fully solved without any conditions, under the liability contract.

We conduct further analysis by comparing the three contracts and find that the cyberinsurance firm has the incentive to implement a monitoring contract only when the fixed monitoring cost is low. In practice, a low <sup>( )</sup> M V<sup>Ce t dt C−</sup>  monitoring cost can be achieved not only by efficient use of IT tools but also by improving the trust between the CI firm and the MSSP (and clients). Analogously, the liability contract also worth implementing when the <sub></sub>implementation cost is low. As evidenced by the legal   <sub></sub>battle between Cardsystems and Savvis, implementation <sup></sup>costs can also involve investigation fees, legal fees, and so forth. We find that implementation costs are relatively low when the MSSP faces high system interdependency or a high probability of undirected attack, when the contract horizon is long, or when both parties have nearly equal responsibility during the contract duration. Also, we should note that the two proposed contracts are suitable for security outsourcing relationships in which security breaches can be observed (e.g., firms in the United States are legally required to disclose security breaches to the public) and the liability for these breaches cannot be easily assigned to any one party (e.g., the CardSystem/Savvis case).

This research can be extended in several directions based on the limitations identified here. First, beyond undirected attacks, strategic attacks in which hackers choose their efforts according to the quality of the system’s security quality would be a fruitful topic for future research. Second, the CI firm may have an incentive to deny that either party’s security effort has reached the required level in the monitoring contract case, and clients may have incentives to attack other clients when it is the sole victim of a breach under the liability contract. Issues related to incentives for the CI firm and clients to commit fraud could also be examined. Finally, instead of hiring a CI firm to monitor both parties, the MSSP and clients can monitor and verify each other’s security efforts by proposing an alternative contract that includes the mandatory sharing of their security efforts as an additional contract term. Future research could explore whether such an alternative contract would perform better than the monitoring contract.

## Acknowledgments

The authors thank the senior editor, Dr. Kim Huat Goh and the two anonymous reviewers who contributed valuable suggestions to improve the quality of this paper. This research was funded by the National Natural Science Foundation of China (Grants 71801035, 71572145, 71832001, 71801071), and the Fundamental Research Funds for the Central Universities.

## References

Aon Inpoint (2017). Global cyber market overview. http://www.aon.com/inpoint/bin/pdfs/whitepapers/Cyber.pdf

Bryson, N. (2000). Structuring IS outsourcing contracts for mutual gain: An approach to analyzing performance incentive schemes. Journal of the Association for Information Systems, 1(1), Article 9.

Casey, E. (2003). Determining intent: Opportunistic vs targeted attacks. Computer Fraud & Security, 4, 8-11.

Cezar, A., Cavusoglu, H. & Raghunathan, S. (2014). Outsourcing information security: Contracting issues and security implications. Management Science, 60(3), 638-657.

Cezar, A., Cavusoglu, H. & Raghunathan, S. (2017). Sourcing information security operations: The role of risk interdependency and competitive externality in outsourcing decisions. Production and Operations Management, 26(5), 860-879.

Charette, R. (2010). McDonald’s data breach: Supersized? IEEE Spectrum. https://spectrum. ieee.org/riskfactor/telecom/internet/mcdonalds -data-breach-supersized.

Choudhury, V. & Sabherwal, R. (2003). Portfolios of control in outsourced software development projects. Information Systems Research, 14(3), 291-314.

Clemons, E. & Aron, R. (2004). Maximize your outsourcing benefits through complexity arbitrage (Wharton School of Business working paper). http://citeseerx.ist.psu.edu/viewdoc/ download;jsessionid=8E7130FD324152C49B 7E93AE00672F41?doi=10.1.1.109.2624&rep= rep1&type=pdf

Cooper, R. & Ross, T. W. (1985). Product warranties and double moral hazard. The RAND Journal of Economics, 16(1), 103-113.

pwc (2017). Key findings from the Global State of Information Security Survey 2017. https://www.pwc.com/id/en/publications/assets /assurance/Risk%20Assurance/gsiss-2017- web.pdf

Das, T. K. & Teng, B. S. (1998). Between trust and control: developing confidence in partner cooperation in alliances. Academy of Management Review, 23(3), 491-512.

Demirezen, E. M., Kumar, S. & Shetty, B. (2016). Managing co-creation in information

technology projects: A differential games approach. Information Systems Research, 27(3), 517-537.

Dickson, S. (2018). How to measure the ROI of cybersecurity investments. https://www.itsp magazine.com/from-the-newsroom/how-tomeasure-the-roi-of-cybersecurity-investments.

Ding, W., Yurcik, W. & Yin, X. (2005). Outsourcing internet security: Economic analysis of incentives for managed security service providers. Proceedings of the Workshop on Internet and Network Economics (pp. 947-958).

Feng, G., J. Zhu, N. Wang and H. Liang (2019). How Paternalistic Leadership Influences IT Security Policy Compliance: The Mediating Role of the Social Bond. Journal of the Association for Information Systems, 20(11), 1650-1691.

Fershtman, C. (1987). Identification of classes of differential games for which the open loop is a degenerate feedback Nash equilibrium. Journal of Optimization Theory and Applications, 55(2), 217-231.

Fudenberg, D. & Tirole, J. (1991). Game theory. MIT Press.

Georges, D. (2013). Handbook of insurance. Springer.

Gupta, A. & Zhdanov, D. (2012). Growth and sustainability of managed security services networks: An economic perspective. Mis Quarterly, 36(4), 1109-1130.

Hölmstrom, B. (1979). Moral hazard and observability. The Bell Journal of Economics, 10(1), 74-91.

Hui, K. L., Hui, W. & Yue, W. T. (2012). Information security outsourcing with system interdependency and mandatory security requirement. Journal of Management Information Systems, 29(3), 117-155.

Jayanth, R., Jacob V. S., & S. Radhakrishnan (2011). Vendor and client interaction for requirements assessment in software development: Implications for feedback process. Information Systems Research 22(2): 289-305.

Kirsch, L.S. (1997). Portfolios of control modes and IS project management. Information Systems Research, 8(3), 215-239.

Lee, C.H., Geng, X.J. & Raghunathan, S. (2013). Contracting information security in the presence of double moral hazard. Information Systems Research, 24(2), 295-311.

MarketsandMarkets (2018). Managed security services market worth 47.65 billion USD by 2023. https://www.marketsandmarkets.com/PressRel eases/managed-security-services.asp.

Mookerjee, V., Mookerjee, R., Bensoussan, A. & Yue, W.T. (2011). When hackers talk: Managing information security under variable attack rates and knowledge dissemination. Information Systems Research, 22(3), 606-623.

Ogut, H., Menon, N. & Raghunathan, S. (2005). Cyber Insurance and IT security investment: Impact of interdependence risk. Proceedings of the Fourth Workshop on the Economics of Information Security.

Roels, G., Karmarkar, U. S. & Carr, S. (2010). Contracting for collaborative services. Management Science, 56(5), 849-863.

Rowe, B.R. (2007). Will outsourcing IT security lead to a higher social level of security? Proceedings of the Sixth Workshop on the Economics of Information Security.

Selten, R. (1975). Reexamination of the perfectness concept for equilibrium points in extensive games. International Journal of Game Theory, 4(1), 25-55.

Sorger, G. (1989). Competitive dynamic advertising: a modification of the case game. Journal of Economic Dynamics and Control, 13(1), 55-80.

Srinidhi, B., Yan, J. & Tayi, G. K. (2015). Allocation of resources to cyber-security: The effect of misalignment of interest between managers and investors. Decision Support Systems, 75, 49-62.

Varian, H. (2004). System reliability and free riding. In L. J. Camp, S. Lewis (eds.) Economics of information security (pp. 1-15). Springer.

Vuorinen, J., & Tetri, P. (2012). The order machine: The ontology of information security. Journal of the Association for Information Systems 13(9), 695-713.

Wheatman, V., Smith, B. S. N., Pescatore, J., Nicollet, M., Allan, A., & Mogull, R. (2005). What your organization should be spending for information security. Gartner Research. https://www.gartner.com/doc/474665?ref=mrk tg-srch.

Wu, Y., Fung, R. Y. K., Feng, G. & Wang, N. (2017). Decisions making in information security outsourcing: Impact of complementary and substitutable firms. Computers & Industrial Engineering, 110, 1-12.

Yue, W.T., Cakanyildirim, M., Ryu, Y.U. & Liu, D. (2007). Network externalities, layered protection and IT security risk management. Decision Support Systems, 44(1), 1-16.

Zetter, K. (2009). In legal first, data-breach suit targets auditor. https://www.wired.com/2009/06/ auditor-sued/.

Zhao, X., Xue, L. & Whinston, A.B. (2013). Managing Interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements. Journal of Management Information Systems, 30(1), 123- 152.

## Appendix A

## Proof of Lemma 2

The proof of Lemma 1 is an abbreviated version of that of Lemma 2. Hence, we omit the details of Lemma $1 \mathrm { { } } \mathrm { { } } \mathrm { { s } }$ proof for brevity, and only prove Lemma 2. In the bilateral refund contract (BRC), anticipating how both parties will determine their best response in effort, the MSSP solves the following problem in Stage 1:

$$
\max _ {f _ {1}, \phi_ {1}, f _ {2}, \phi_ {2}} U _ {M} (\hat {e} _ {F 1} (t), \hat {e} _ {F 2} (t), \hat {e} _ {M 1} (t), \hat {e} _ {M 2} (t))\tag{A1}
$$

$$
s. t. \hat {e} _ {F i} (t) \in \underset {e _ {F i} (t)} {\operatorname{argmax}} U _ {F i} (e _ {F i} (t), \hat {e} _ {F (3 - i)} (t), \hat {e} _ {M i} (t), \hat {e} _ {M (3 - i)} (t)), i = 1, 2\tag{A2}
$$

$$
(\hat {e} _ {M 1} (t), \hat {e} _ {M 2} (t)) \in \underset {(e _ {M 1} (t), e _ {M 2} (t))} {\text {argmax}} U _ {M} (\hat {e} _ {F 1} (t), \hat {e} _ {F 2} (t), e _ {M 1} (t), e _ {M 2} (t))\tag{A3}
$$

$$
U _ {F i} (\hat {e} _ {F i} (t), \hat {e} _ {F (3 - i)} (t), \hat {e} _ {M i} (t), \hat {e} _ {M (3 - i)} (t)) \geq U _ {F}, i = 1, 2\tag{A4}
$$

$$
U _ {M} (\hat {e} _ {F 1} (t), \hat {e} _ {F 2} (t), \hat {e} _ {M 1} (t), \hat {e} _ {M 2} (t)) \geq 2 \underline {{U}} _ {M}\tag{A5}
$$

$$
\dot {q} _ {i} (t) = \varepsilon (\alpha e _ {F i} (t) + \beta e _ {M i} (t)), i = 1, 2\tag{A6}
$$

$$
e _ {F i} (t) \geq 0, e _ {M i} (t) \geq 0, i = 1, 2\tag{A7}
$$

The MSSP’s objective is to maximize its own expected payoff by choosing two decision variables, $f$ and $\phi .$ . Note that the MSSP needs to decide two pair-wise contract terms since the number of clients, $N = 2$ . Here, the state variable $q _ { i }$ is the security quality of client ??, and control variables $e _ { M i }$ and $e _ { F i }$ represent the MSSP’s and client $i \mathbf { \ ' } _ { \mathbf { S } }$ effort levels, respectively. Constraints represented as equations (A2) and (A3) are client $i \ ' \mathbf { s }$ and the $\mathrm { M S S P ^ { \circ } s }$ incentive compatibility constraints, respectively. Constraints represented as equations (A4) and (A5) are both parties’ individual rationality constraints. Constraints represented as equations (A6) and (A7) are the same as Equations (3) and (4) in Section 3.1.

We first use Pontryagin’s maximum principle to drive the open-loop Nash equilibrium efforts in Stage 2 of the game. The Hamiltonian functions for the MSSP and clients are given by: $\begin{array} { r } { H _ { M } ( t ) = \sum _ { i = 1 } ^ { 2 } \left\{ - p _ { i } ( t ) ( \phi _ { i } + \lambda \phi _ { 3 - i } ) L - \right. } \end{array}$ $\begin{array} { r } { \frac { 1 } { 2 } C e _ { M i } ^ { 2 } ( t ) + \lambda _ { M i } \varepsilon ( \alpha e _ { F i } ( t ) + \beta e _ { M i } ( t ) ) \Big \} } \end{array}$ , and $\begin{array} { r } { H _ { F i } ( t ) = - ( p _ { i } ( t ) + \lambda p _ { 3 - i } ( t ) ) ( 1 - \phi _ { i } ) L - \frac { 1 } { 2 } C e _ { F i } ^ { 2 } ( t ) + \lambda _ { F i } \varepsilon ( \alpha e _ { F i } ( t ) + } \end{array}$ $\beta e _ { M i } ( t ) ) + \lambda _ { F i i } \varepsilon ( \alpha e _ { F ( 3 - i ) } ( t ) + \beta e _ { M ( 3 - i ) } ( t ) ) , i = 1 , 2$ , where $p _ { i } ( t ) = a ( 1 - q _ { i } ( t ) ) , i = 1 , 2$ . Here $\lambda _ { M i } , \lambda _ { F i }$ , and $\lambda _ { F i i }$ are shadow prices, we can interpret the six shadow prices as the marginal benefit of security quality at time $t . \lambda _ { M i } , \lambda _ { F i } ,$ and $\lambda _ { F i i }$ are given $\begin{array} { r } { \mathrm { y y } { \colon } \dot { \lambda } _ { M i } = - \frac { \partial H _ { M } ( t ) } { \partial q _ { i } ( t ) } = - a L ( \phi _ { i } + \lambda \phi _ { 3 - i } ) , \dot { \lambda } _ { F i } = - \frac { \partial H _ { F i } ( t ) } { \partial q _ { i } ( t ) } = - a L ( 1 - \phi _ { i } ) , } \end{array}$ , and $\begin{array} { r } { \dot { \lambda } _ { F i i } = - \frac { \partial H _ { F i } ( t ) } { \partial q _ { 3 - i } ( t ) } = } \end{array}$ $- \lambda a L ( 1 - \phi _ { i } )$ . Solving these differential equations with the boundary conditions $\lambda _ { M i } ( T ) = 0 , \ \lambda _ { F i } ( T ) = 0$ , and $\lambda _ { F i i } ( T ) = 0$ , we have $\lambda _ { M i } ( t ) = a L ( \phi _ { i } + \lambda \bar { \phi } _ { 3 - i } ) ( T - t ) , \lambda _ { F i } ( t ) = a \dot { L } ( 1 - \phi _ { i } ) ( T - t )$ , and $\lambda _ { F i i } ( t ) = \lambda a L ( 1 -$ $\phi _ { i } ) ( T - t )$

After substituting $\lambda _ { M i } , \lambda _ { F i }$ , and $\lambda _ { F i i }$ into the two Hamiltonian functions and getting the derivatives of the two functions with respect to the control variables $e _ { M i } ( t )$ and $e _ { F i } ( t )$ to be zero, we have:???? $L \beta ( \phi _ { i } + \lambda \phi _ { 3 - i } ) ( T - t ) - C e _ { M i } = 0$ and ${ \varepsilon } a L \alpha ( 1 - \phi _ { i } ) ( T - t ) - C e _ { F i } = 0$ . Solving the two equations we can obtain the open-loop Nash equilibrium efforts for the MSSP and clients: $\begin{array} { r } { \hat { e } _ { M i } ( t ) = \frac { \varepsilon a L \beta ( \phi _ { i } ^ { - } + \lambda \phi _ { 3 - i } ) ( T - t ) } { c } , \hat { e } _ { F i } ( t ) = \frac { \varepsilon a L \alpha ( 1 - \phi _ { i } ) ( T - t ) } { c } } \end{array}$ . Since the Hamiltonian functions are strictly concave, the second-order conditions for this differential game are also satisfied.

Now, we have obtained the open-loop Nash equilibrium efforts with Pontryagin’s maximum principle. Previous research has proven that if the Pontryagin type necessary conditions for the open-loop Nash equilibrium do not depend on the state variables, then the open-loop Nash equilibrium is a degenerate feedback Nash equilibrium (Fershtman, 1987). Thus, both parties’ equilibrium efforts are degenerate feedback Nash equilibrium solutions since effort trajectories do not dependent on the state variable $q ( t )$ . The feedback Nash equilibrium is subgame-perfect by construction (Selten, 1975); thus, we can conclude that both parties’ equilibrium efforts in $\mathrm { S t a g e } 2$ are the subgameperfect equilibrium, which can provide credible and efficient threats since no players can benefit from deviating from its announced strategy (Sorger, 1989).

With the subgame-perfect equilibrium, we now solve the two contract terms in Stage 1. We first solve the state variable $q _ { i } ( t )$ . Solving the differential equation $\dot { q } _ { i } ( t ) = \varepsilon ( \alpha e _ { F i } ( t ) + \beta e _ { M i } ( t ) )$ ) with boundary condition $q ( 0 ) = q _ { 0 }$ , we have $\begin{array} { r } { q _ { i } ( t ) = \frac { \varepsilon ^ { 2 } a L ( \beta ^ { 2 } ( \phi _ { i } + \lambda \phi _ { 3 - i } ) + \alpha ^ { 2 } ( 1 - \phi _ { i } ) ) } { C } ( T t - \frac { 1 } { 2 } t ^ { 2 } ) + q _ { 0 } } \end{array}$ . Next, since the MSSP acts as the principal, the MSSP has no incentive to leave both clients any value more than their reservation utilities. Thus, the MSSP makes both firms participation constraint binding. Hence, we have $\begin{array} { r } { f _ { i } = V ( T ) - \int _ { 0 } ^ { T } \left\{ ( p _ { i } + \lambda p _ { 3 - i } ) ( 1 - \phi _ { i } ) L + \frac { 1 } { 2 } C e _ { F i } ^ { 2 } ( t ) \right\} d t - U _ { F } } \end{array}$ Finally, after substituting the service fee $f _ { i } ,$ , the state variable security quality $q _ { i } ( t )$ , the MSSP’s effort $e _ { M i } ( t )$ , and clients’ efforts $e _ { F i } ( t )$ into the objective of the MSSP, we have

$$
(\hat {\phi} _ {1}, \hat {\phi} _ {2}) \in \underset {(\phi_ {1}, \phi_ {2})} {a r g m a x} U _ {M} = 2 V (T) - \sum_ {i = 1} ^ {2} \left\{\int_ {0} ^ {T} \frac {[ (1 - \frac {\varepsilon^ {2} a L (\beta^ {2} (\phi_ {i} + \lambda \phi_ {3 - i}) + \alpha^ {2} (1 - \phi_ {i}))}{C} (T t - \frac {1}{2} t ^ {2}) - q _ {0}) (1 + \lambda) a L}{+ \frac {C}{2} ((\frac {\varepsilon a L \alpha (1 - \phi_ {i}) (T - t)}{C}) ^ {2} + (\frac {\varepsilon a L \beta (\phi_ {i} + \lambda \phi_ {3 - i}) (T - t)}{C}) ^ {2}) ] d t} \right\} - 2 \underline {{U}} _ {F}.
$$

Note that, the above function can be written as $( \hat { \phi } _ { 1 } , \hat { \phi } _ { 2 } ) \in a r g m a x$ $U _ { M } \left( \cdot \right) = S W \left( \cdot \right) - 2 U _ { F }$ , where $S W ( \cdot )$ is the summation of the expected payoffs of the MSSP and both clients. Thus, the MSSP’s incentive in stage 1 is to choose an optimal compensation to maximize the total expected payoffs of both parties. Since clients’ reservation utilities are constants, the $\mathrm { M S S P ^ { \circ } s }$ objective is always to maximize social welfare. Taking the integrals and get the first-order condition with respect to $\phi _ { 1 }$ and $\phi _ { 2 }$ , we get the following equation: $\rho ^ { 2 } \lambda ^ { 2 } \phi _ { i } + \alpha ^ { 2 } \lambda + \bar { \alpha } ^ { 2 } \phi _ { i } - \beta ^ { 2 } \bar { \lambda } ^ { 2 } + 2 \beta ^ { 2 } \lambda \phi _ { 3 - i } -$ $2 \beta ^ { 2 } \lambda + \beta ^ { 2 } \phi _ { i } - \beta ^ { \hat { 2 } } = 0 , i \stackrel { . } { = } 1 , 2$ . Since both clients are homogeneous, we focus on the symmetric case. Solving the equations, we obtain $\begin{array} { r } { \hat { \phi } = \frac { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } - \lambda \alpha ^ { 2 } } { \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } } } \end{array}$ . Substituting $\hat { \phi }$ into the subgame-perfect equilibrium of the MSSP and clients, we have $\begin{array} { r } { \hat { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ^ { 3 } ( 1 + \lambda ) ( T - t ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } } \end{array}$ and $\begin{array} { r } { \hat { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } - \lambda \alpha ^ { 2 } ) ( T - t ) } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } } \end{array}$ . Since $e _ { F } ( t ) \geq 0$ and $e _ { M } ( t ) \geq 0$ , we have the following condition satisfies: $\beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } \ge \lambda \alpha ^ { 2 }$ . Substituting $\hat { \phi } , \hat { e } _ { M } ( t )$ , and $\hat { e } _ { F } ( t )$ into the service fee equation, we can obtain the service fee:

$$
\hat {f} = V (T) - \underline {{U}} _ {F} - \frac {a L \alpha^ {2} T (1 + \lambda) ^ {2} (1 - q _ {0})}{\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}} + \frac {\varepsilon^ {2} a ^ {2} L ^ {2} (1 + \lambda) ^ {2} T ^ {3} \alpha^ {2} (\alpha^ {4} (1 + 2 \lambda) + 2 \beta^ {2} (1 + \lambda) (\beta^ {2} (1 + \lambda) ^ {2} - \lambda \alpha^ {2}))}{6 C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}}. \text {Substituting} \hat {f}, \hat {\phi}, \hat {e} _ {M} (t)
$$

$\hat { e } _ { F } ( t )$ into (5) in Section 4.1, the MSSP’s expected payoff under the BRC is obtained: $\widehat { U } _ { M } = 2 V ( T ) - 2 a L T ( 1 +$ $\begin{array} { r } { \lambda ) ( 1 - q _ { 0 } ) + \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 2 } ( \beta ^ { 4 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 4 } + \alpha ^ { 2 } \beta ^ { 2 } ) } { 3 C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } - 2 U _ { F } } \end{array}$

Hence, Lemma 2 is proven.

## Proof of Proposition 1

Proposition 1(a):

$$
\frac {\partial (e _ {M} ^ {*} (t) - \hat {e} _ {M} (t))}{\partial \beta} = - \frac {\varepsilon a L \alpha^ {2} (1 + \lambda) ^ {2} (\beta^ {2} (1 + \lambda) ^ {2} - \alpha^ {2}) (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}}
$$

$\frac { \partial ( e _ { M } ^ { * } ( t ) - \hat { e } _ { M } ( t ) ) } { \partial \beta } > 0$ when $\begin{array} { r } { \beta < \frac { \alpha } { 1 + \lambda } , } \end{array}$ , and $\frac { \partial ( e _ { M } ^ { * } ( t ) - \hat { e } _ { M } ( t ) ) } { \partial \beta } \leq 0$ when $\begin{array} { r } { \beta \geq \frac { \alpha } { 1 + \lambda } . } \end{array}$ Thus, we can conclude that ?? first worsens then alleviates the MSSP’s DMH problem.

$$
\frac {\partial (e _ {F} ^ {*} (t) - \hat {e} _ {F} (t))}{\partial \alpha} = \frac {\varepsilon a L \beta^ {2} (1 + \lambda) ^ {3} (\beta^ {2} (1 + \lambda) ^ {2} - \alpha^ {2}) (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}}
$$

$\frac { \partial ( e _ { F } ^ { * } ( t ) - \hat { e } _ { F } ( t ) ) } { \partial \alpha } > 0$ when?? $< \beta ( 1 + \lambda )$ , and $\frac { \partial ( e _ { M } ^ { * } ( t ) - \hat { e } _ { M } ( t ) ) } { \partial \alpha } \leq 0$ when $\alpha \geq \beta ( 1 + \lambda )$ . Thus, we can conclude that ?? first worsens then alleviates the client’s DMH problem.

Proposition 1(b):

$$
\begin{array}{r l} & {\frac {\partial (e _ {M} ^ {*} (t) - \hat {e} _ {M} (t))}{\partial \lambda} = \frac {2 \varepsilon a L \alpha^ {2} \beta (1 + \lambda) (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}} > 0, \frac {\partial (e _ {F} ^ {*} (t) - \hat {e} _ {F} (t))}{\partial \lambda} = \frac {\varepsilon a L \alpha \beta^ {2} (1 + \lambda) ^ {2} (\beta^ {2} (1 + \lambda) ^ {2} + 3 \alpha^ {2}) (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}} > 0,} \\ & {\frac {\partial (e _ {M} ^ {*} (t) - \hat {e} _ {M} (t))}{\partial a} = \frac {\varepsilon L \alpha^ {2} \beta (1 + \lambda) ^ {2} (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}} > 0, \frac {\partial (e _ {F} ^ {*} (t) - \hat {e} _ {F} (t))}{\partial a} = \frac {\varepsilon L \alpha^ {2} \beta (1 + \lambda) ^ {3} (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}} > 0.} \end{array}
$$

## Proof of Lemma 3

The proof of Lemma 3 is similar to that of Lemma 2, and we only give a short proof here. Under the monitoring contract, the CI firm faces the following payoff maximization problem in Stage 1:

$$
\underset {I _ {F}, I _ {M}, S _ {F}, S _ {M}} {\max} U _ {R} = 2 I _ {F} - 2 I _ {M} + (s _ {M} - s _ {F}) \sum_ {i = 1} ^ {2} \left\{\int_ {0} ^ {T} \{p _ {i} (t) (1 + \lambda) L \} d t \right\} - \sum_ {i = 1} ^ {2} \left\{\int_ {0} ^ {T} \frac {C _ {R}}{2} (e _ {M i} ^ {2} (t) + e _ {F i} ^ {2} (t)) d t + F _ {R i} \right\}\tag{A8}
$$

$$
s. t. (\bar {e} _ {F 1} (t), \bar {e} _ {F 2} (t), \bar {e} _ {M 1} (t), \bar {e} _ {M 2} (t)) \in \underset {(e _ {F 1} (t), e _ {F 2} (t), e _ {M 1} (t), e _ {M 2} (t))} {\text {argmax}} U _ {R}\tag{A9}
$$

$$
U _ {M} = 2 I _ {M} - s _ {M} \sum_ {i = 1} ^ {2} \left\{\int_ {0} ^ {T} \{p _ {i} (t) (1 + \lambda) L \} d t \right\} - \sum_ {i = 1} ^ {2} \left\{\int_ {0} ^ {T} \frac {1}{2} C e _ {M i} ^ {2} (t) d t \right\} \geq \widehat {U} _ {M}\tag{A10}
$$

$$
U _ {F i} = V (T) - I _ {F} - (1 - s _ {F}) \int_ {0} ^ {T} \{(p _ {i} (t) + \lambda p _ {3 - i} (t)) L \} d t - \int_ {0} ^ {T} \left\{\frac {1}{2} C e _ {F i} ^ {2} (t) \right\} d t \geq U _ {F}, i = 1, 2\tag{A11}
$$

$$
\dot {q} _ {i} (t) = \varepsilon (\alpha e _ {F i} (t) + \beta e _ {M i} (t)), i = 1, 2\tag{A12}
$$

$$
e _ {F i} (t) \geq 0, e _ {M i} (t) \geq 0, i = 1, 2\tag{A13}
$$

where $p _ { i } ( t ) = a ( 1 - q _ { i } ( t ) ) , i = 1 , 2$ . The CI firm’s objective in equation (A8) is to maximize its own expected payoff, in which $2 I _ { F } - 2 I _ { M }$ represents the insurance premium charged from clients and the service fee paid to the MSSP, $\begin{array} { r l r } { } & { { } } & { ( s _ { M } - s _ { F } ) \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } \{ p _ { i } ( t ) ( 1 + \lambda ) L \} d t \right\} } \end{array}$ represents the CI firm’s penalty to the MSSP and the compensation to clients when a breach occurs, and $\begin{array} { r } { \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } \frac { C _ { R } } { 2 } ( e _ { M i } ^ { 2 } ( t ) + e _ { F i } ^ { 2 } ( t ) ) d t + F _ { R i } \right\} } \end{array}$ represents the CI firm’s fixed and variable monitoring costs. The constraint in equation (A9) is the CI firm’s incentive compatibility constraint. Constraints in equations (A10) and (A11) are the MSSP’s and client i’s individual rationality (IR) constraints, respectively. The term $\begin{array} { r } { { s _ { M } } \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } \{ p _ { i } ( t ) ( 1 + \lambda ) L \} d t \right\} } \end{array}$ in the MSSP’s IR constraint represents the CI firm’s penalty imposed on the MSSP, and the term $\begin{array} { r } { s _ { F } \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } \{ p _ { i } ( t ) ( 1 + \lambda ) L \} d t \right\} } \end{array}$ in the client i’s IR constraint represents the CI firm’s compensation to clients when a breach occurs.

As the principal, the CI firm will always set the insurance premium and the compensation such that the expected payoffs of clients are indifferent between their reservation utilities and taking the security contract. To attract the MSSP to use cyberinsurance, the CI firm needs to ensure that the $\mathrm { M S S P ^ { \circ } s }$ benefit under the monitoring contract is no less than that under the BRC. Thus, the CI firm will set the service fee and the penalty such that the expected profit of the MSSP is indifferent between that under the BRC and that under the monitoring contract.

Thus, after combining the expected payoffs of three parties, the Cyber-insurance Firm’s problem in the second stage becomes $\begin{array} { r } { m a x } \\ { e _ { F _ { 1 } , e _ { F 2 } , e _ { M 1 } , e _ { M 2 } } U _ { R } = - \widehat { U } _ { M } - 2 U _ { F } - \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } p _ { i } ( t ) ( 1 + \lambda ) L d t \right\} + 2 V ( T ) - \sum _ { i = 1 } ^ { 2 } \left\{ \int _ { 0 } ^ { T } \left\{ \frac { 1 } { 2 } ( C + C _ { R } ) ( e _ { F i } ^ { 2 } ( t ) +  \right\right.}.   \end{array}$ $e _ { M i } ^ { 2 } ( t ) ) \big \} d t - F _ { R i } \big \}$ . Solving the above problem, we have $\begin{array} { r } { \bar { e } _ { M } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { C + C _ { R } } \mathrm { a n d } \bar { e } _ { F } ( t ) = \frac { \varepsilon a L \alpha ( 1 + \lambda ) ( T - t ) } { C + C _ { R } } . } \end{array}$ . Taking both parties’ security efforts into their respective expected payoffs, we can obtain the relationship between the insurance premium (service fee) and the compensation (penalty).

## Proof of Lemma 4

Under the liability contract, the MSSP solves the following problem in Stage 1 of the game:

$$
\max _ {f _ {1}, D _ {1}, f _ {2}, D _ {2}} U _ {M} (\tilde {e} _ {F 1} (t), \tilde {e} _ {F 2} (t), \tilde {e} _ {M 1} (t), \tilde {e} _ {M 2} (t))\tag{A14}
$$

$$
s. t. \tilde {e} _ {F i} (t) \in \underset {e _ {F i} (t)} {\operatorname{argmax}} U _ {F i} (e _ {F i} (t), \tilde {e} _ {F (3 - i)} (t), \tilde {e} _ {M i} (t), \tilde {e} _ {M (3 - i)} (t)), i = 1, 2\tag{A15}
$$

$$
(\tilde {e} _ {M 1} (t), \tilde {e} _ {M 2} (t)) \in \underset {(e _ {M 1} (t), e _ {M 2} (t))} {\text {argmax}} U _ {M} (\tilde {e} _ {F 1} (t), \tilde {e} _ {F 2} (t), e _ {M 1} (t), e _ {M 2} (t))\tag{A16}
$$

$$
U _ {F i} (\tilde {e} _ {F i} (t), \tilde {e} _ {F (3 - i)} (t), \tilde {e} _ {M i} (t), \tilde {e} _ {M (3 - i)} (t)) \geq U _ {F}, i = 1, 2\tag{A17}
$$

$$
U _ {M} (\tilde {e} _ {F 1} (t), \tilde {e} _ {F 2} (t), \tilde {e} _ {M 1} (t), \tilde {e} _ {M 2} (t)) \geq 2 \underline {{U}} _ {M}\tag{A18}
$$

$$
\dot {q} _ {i} (t) = \varepsilon (\alpha e _ {F i} (t) + \beta e _ {M i} (t)), i = 1, 2\tag{A19}
$$

$$
e _ {F i} (t) \geq 0, e _ {M i} (t) \geq 0, i = 1, 2\tag{A20}
$$

All the above equations and constraints are similar to those given for the BRC case and available in the proof in Lemma 2, and hence we omit the details for brevity. As the principal, the MSSP will always propose a service fee such that clients are indifferent between their reservation utilities and taking the security contract. Thus, with the help of the service fee, the MSSP extracts all surplus from the collaboration, leaving clients only their reservation utilities. That means, no matter what the proposed compensation is, the MSSP’s incentive in Stage 1 is always to choose an optimal compensation to maximize the total expected payoffs of both parties. Since clients’ reservation utilities are constants, the MSSP’s objective is to maximize social welfare, as discussed in the Proof of Lemma 2.

Specifically, in our liability contract, the service fee will be $f = U _ { F i } ( 0 , \widetilde { D } , \widetilde { E } ) - U _ { F } . \ : U _ { F i } ( 0 , \widetilde { D } , \widetilde { E } )$ is client $i ^ { \mathbf { \gamma } } \mathbf { s }$ expected payoff given that the service fee proposed by the MSSP is zero, the compensation combination is $\widetilde { D } = ( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } )$

and both players’ equilibrium security efforts are $\tilde { E } = ( \tilde { e } _ { F i } ( t ) , \tilde { e } _ { F ( 3 - i ) } ( t ) , \tilde { e } _ { M i } ( t ) , \tilde { e } _ { M ( 3 - i ) } ( t ) )$ . Thus, the MSSP’s expected payoff is $U _ { M } = U _ { M } ( 0 , \widetilde { D } , \widetilde { E } ) + 2 f - C _ { V } = U _ { M } ( \cdot ) + U _ { F i } ( \cdot ) + U _ { F j } ( \cdot ) - 2 U _ { F } - C _ { V } = S W ( \cdot ) - 2 U _ { F } - C _ { V } = 0 .$ Since both $U _ { F }$ and $C _ { V }$ are constants, the $\mathrm { M S S P ^ { \circ } s }$ objective is to maximize $S W ( \cdot )$ . Therefore, if possible, the MSSP will propose any $\widetilde { D } = ( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } )$ that can reach the benchmark efforts. Our next focus is to find $\widetilde { D } = ( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } )$ so that $\tilde { e } _ { F } ( t ) = e _ { F } ^ { * } ( t )$ and $\tilde { e } _ { M } ( t ) = e _ { M } ^ { * } ( t )$

The Hamiltonian functions for the MSSP and clients under the liability contract are given by:

$$
\begin{array}{r l} & H _ {M} (t) = \left\{ \begin{array}{l} - 2 p _ {1} (t) p _ {2} (t) d _ {b b} - p _ {1} (t) (1 - p _ {2} (t)) (d _ {b n} + d _ {n b}) - (1 - p _ {1} (t)) p _ {2} (t) (d _ {n b} + d _ {b n}) \\ - \frac {C}{2} (e _ {M 1} ^ {2} (t) + e _ {M 2} ^ {2} (t)) + \lambda_ {M 1} \varepsilon (\alpha e _ {F 1} (t) + \beta e _ {M 1} (t)) + \lambda_ {M 2} \varepsilon (\alpha e _ {F 2} (t) + \beta e _ {M 2} (t)) \end{array} \right\} \mathrm{and} \\ & H _ {F i} (t) = \left\{ \begin{array}{l l} - (p _ {i} (t) + \lambda p _ {3 - i} (t)) L - p _ {i} (t) p _ {3 - i} (t) d _ {b b} - p _ {i} (t) (1 - p _ {3 - i} (t)) d _ {b n} - (1 - p _ {i} (t)) p _ {3 - i} (t) d _ {n b} \\ - \frac {C}{2} e _ {F i} ^ {2} (t) + \lambda_ {F i} \varepsilon (\alpha e _ {F i} (t) + \beta e _ {M i} (t)) + \lambda_ {F i i} \varepsilon (\alpha e _ {F (3 - i)} (t) + \beta e _ {M (3 - i)} (t)) \end{array} \right\}, \quad \mathrm{where} \\ & p _ {i} (t) = a (1 - q _ {i} (t)) a n d i = 1, 2. \end{array}
$$

The shadow prices $\lambda _ { M i } , \lambda _ { F i }$ , and $\lambda _ { F i i }$ are given by: $\begin{array} { r } { \dot { \lambda } _ { M i } = - \frac { \partial H _ { M } ( t ) } { \partial q _ { i } ( t ) } = 2 a p _ { 3 - i } ( t ) ( d _ { b n } + d _ { n b } - d _ { b b } ) - a ( d _ { b n } + } \end{array}$ $d _ { n b } )$ ,and $\begin{array} { r } { \dot { \lambda } _ { F i i } = - \frac { \partial H _ { F i } ( t ) } { \partial q _ { 3 - i } ( t ) } = a p _ { i } ( t ) ( d _ { b b } - d _ { b n } - d _ { n b } ) + a ( d _ { n b } - \lambda L ) } \end{array}$ . Solving these differential equations with boundary conditions $\lambda _ { M i } ( T ) = 0 , \lambda _ { F i } ( T ) = 0 , \mathrm { a n d } \lambda _ { F i i } ( T ) = 0$ , we have $\mathsf { \Pi } _ { \mathfrak { M } i } ( t ) = - ( 2 a p _ { 3 - i } ( t ) ( d _ { b n } + d _ { n b } - d _ { b b } ) +$ $a ( d _ { b n } + d _ { n b } ) ) ( T - t ) , \lambda _ { F i } ( t ) = ( a p _ { 3 - i } ( t ) ( d _ { b n } + d _ { n b } - d _ { b b } ) + a ( L - d _ { b n } ) ) ( T - t )$ , and $\lambda _ { F i i } ( t ) = ( a p _ { i } ( t ) ( d _ { b n } +$ $d _ { n b } - d _ { b b } ) + a ( \lambda L - d _ { n b } ) ) ( T - t )$

After substituting $\lambda _ { M i } , \lambda _ { F i } .$ , and $\lambda _ { F i i }$ into the two Hamiltonian functions and getting the derivatives of the two functions with respect to the control variables to be zero, we have: $\therefore \varepsilon \beta ( T - t ) a [ 2 a ( 1 - q _ { 3 - i } ( t ) ) ( d _ { b b } - d _ { b n } - d _ { n b } ) + d _ { b n } +$ $d _ { n b } ] ( T - t ) - C e _ { M i } ( t ) = 0$ and $\varepsilon \alpha [ a ^ { 2 } q _ { 3 - i } ( t ) ( d _ { b b } - d _ { b n } - d _ { n b } ) + a ( L - a d _ { b b } + a d _ { b n } + a d _ { n b } - d _ { b n } ) ] ( T - t ) -$ $C e _ { F i } ( t ) = 0$ . Solving the two equations can obtain the open-loop Nash equilibrium effort levels for the MSSP and clients: $\begin{array} { r } { \tilde { e } _ { M i } ( t ) = - \frac { \varepsilon \bar { \beta } a ( a ( q _ { 3 - i } ( t ) - \bar { 1 } ) ( d _ { b b } - d _ { b n } - d _ { n b } ) - d _ { b n } - d _ { n b } ) ( \bar { T } - t ) } { c } } \end{array}$ , and $\begin{array} { r } { \tilde { e } _ { F i } ( t ) = \frac { \tilde { \varepsilon } \alpha a ( a ( q _ { 3 - i } ( t ) - 1 ) ( d _ { b b } - d _ { b n } - d _ { n b } ) + L - d _ { b n } ) ( T - t ) } { r } } \end{array}$ ?? ??

Since the Hamiltonian functions are strictly concave, the second-order conditions for this differential game are also satisfied.

The only $D = ( d _ { b b } , d _ { b n } , d _ { n b } )$ that can make the efforts under the liability contract equals the benchmark efforts regardless of the value of $q _ { 3 - i } ( t )$ satisfies the following three equations: $d _ { b b } - d _ { b n } - d _ { n b } = 0 , d _ { b n } + d _ { n b } = ( 1 + \lambda ) L$ and $L - d _ { b n } = ( 1 + \lambda ) L$ . The solutions are $d _ { b b } = ( 1 + \lambda ) L , d _ { n b } = ( 1 + 2 \lambda ) L , d _ { b n } = - \lambda L$

Thus, we obtain that $\begin{array} { r } { \tilde { e } _ { M } ( t ) = e _ { M } ^ { * } ( t ) = \frac { \varepsilon a L \beta ( 1 + \lambda ) ( T - t ) } { C } } \end{array}$ and $\begin{array} { r } { \tilde { e } _ { F } ( t ) = e _ { F } ^ { * } ( t ) = \frac { \varepsilon a L \alpha ( 1 + \lambda ) ( T - t ) } { C } } \end{array}$ . Substituting $\widetilde D =$ $( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } ) , \tilde { e } _ { F } ( t )$ , and $\tilde { e } _ { M } ( t )$ into the service fee equation, we can obtain the service fee under the liability contract: $\begin{array} { r } { \tilde { f } = V ( T ) - U _ { F } - \int _ { 0 } ^ { T } \frac { 1 } { 2 } C e _ { F } ^ { * 2 } ( t ) d t = V ( T ) - \frac { \{ { a } ^ { 2 } { a } ^ { 2 } L ^ { 2 } ( 1 + \lambda ) ^ { 2 } T ^ { 3 } \alpha ^ { 2 } } } { 6 C }  \end{array}$ . Substituting $\tilde { f } , \widetilde { D } = ( \tilde { d } _ { b b } , \tilde { d } _ { b n } , \tilde { d } _ { n b } ) , \tilde { e } _ { F } ( t )$ , and $\tilde { e } _ { M } ( t )$ into (7) in Section $4 . 3 ,$ the MSSP’s expected payoff under the liability contract is obtained: $\widetilde { U } _ { M } = 2 V ( T ) -$ $\begin{array} { r } { 2 a L T ( 1 + \lambda ) ( 1 - q _ { 0 } ) + \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 2 } ( \alpha ^ { 2 } + \beta ^ { 2 } ) } { 3 C } - 2 \underline { { U } } _ { F } - C _ { V } } \end{array}$

Hence, Lemma 4 is proven.

## Proof of Proposition 3

$$
\begin{array}{r l} & {\mathrm{Proposition3(a):}} \\ & {\frac {\partial \hat {e} _ {M i} (t)}{\partial \beta} = \frac {\varepsilon L (1 + \lambda) (T - t) (\alpha^ {2} \varphi [ \beta^ {2} (1 + \lambda) ^ {2} (3 + \lambda) - \lambda \alpha^ {2} \varphi ] + \beta^ {4} (1 + \lambda) ^ {4})}{\varphi C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) ^ {2}} > 0, \quad \frac {\partial \hat {e} _ {F i} (t)}{\partial \beta} = - \frac {2 \varepsilon L \alpha^ {3} \beta \varphi (1 + \lambda) ^ {3} (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) ^ {2}} <   0, \quad \frac {\partial \hat {\phi} _ {i}}{\partial \beta} =} \\ & {\frac {2 \alpha^ {2} \varphi \beta (1 + \lambda) ^ {3}}{(\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) ^ {2}} > 0;} \\ & {\frac {\partial \hat {e} _ {M i} (t)}{\partial \alpha} = - \frac {2 \varepsilon L \alpha \beta^ {3} (1 + \lambda) ^ {4} (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) ^ {2}} <   0, \frac {\partial \hat {e} _ {F i} (t)}{\partial \alpha} = \frac {\varepsilon L \alpha^ {2} \varphi (1 + \lambda) (3 \beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) (T - t)}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi)} > 0, \frac {\partial \hat {\phi} _ {i}}{\partial \alpha} = - \frac {2 \alpha \varphi \beta^ {2} (1 + \lambda) ^ {3}}{(\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2} \varphi) ^ {2}} <   0.} \end{array}
$$

Proposition 3(b):

It is easy to prove that under the monitoring contract and liability contract, $\begin{array} { r } { \frac { \partial e _ { M } ( t ) } { \partial \beta } > 0 , \frac { \partial e _ { F } ( t ) } { \partial \beta } = 0 \mathrm { a n d } \frac { \partial e _ { F } ( t ) } { \partial \alpha } > 0 } \end{array}$ $\begin{array} { r } { \frac { \partial e _ { M } ( t ) } { \partial \alpha } = 0 . } \end{array}$

## Proof of Proposition 4:

## Proposition 4(a):

$\begin{array} { r } { \frac { \partial \hat { e } _ { M } ( t ) } { \partial \lambda } = \frac { \varepsilon a L \beta ( T - t ) [ \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } + \sqrt { 2 ( 1 + \lambda ) } \alpha ^ { 2 } ] [ \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } - \sqrt { 2 ( 1 + \lambda ) } \alpha ^ { 2 } ] } { C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) ^ { 2 } } } \end{array}$ , when $\begin{array} { r } { \frac { ( 1 + \lambda ) ^ { 2 } } { \sqrt { 2 ( 1 + \lambda ) } - 1 } < \frac { \alpha ^ { 2 } } { \beta ^ { 2 } } , \frac { \partial \hat { e } _ { M i } ( t ) } { \partial \lambda } < 0 } \end{array}$ ; when $\begin{array} { r } { \frac { ( 1 + \lambda ) ^ { 2 } } { \sqrt { 2 ( 1 + \lambda ) } - 1 } > \frac { \alpha ^ { 2 } } { \beta ^ { 2 } } , \frac { \partial \hat { e } _ { M i } ( t ) } { \partial \lambda } > 0 } \end{array}$ . Let $\begin{array} { r } { f = \frac { ( 1 + \lambda ) ^ { 2 } } { \sqrt { 2 ( 1 + \lambda ) } - 1 } , \frac { \partial f } { \partial \lambda } = \frac { ( 1 + \lambda ) ^ { 2 } ( 3 ( 1 + \lambda ) - 2 \sqrt { 2 ( 1 + \lambda ) } ) } { ( \sqrt { 2 ( 1 + \lambda ) } - 1 ) ^ { 2 } \sqrt { 2 ( 1 + \lambda ) } } } \end{array}$ , since $3 x - 2 \sqrt { 2 x } > 0 ( x = 1 + \lambda )$ is always established when $x \ge 1$ , we have $\begin{array} { r } { \frac { \partial f } { \partial \lambda } > 0 . } \end{array}$ . Thus, the $\mathrm { M S S P ^ { \circ } s }$ effort first decreases then increases with system interdependency.

$$
\frac {\partial \hat {e} _ {F} (t)}{\partial \lambda} = - \frac {\varepsilon a L \alpha^ {3} (T - t) (\beta^ {2} (1 + \lambda) ^ {2} - \alpha^ {2})}{C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}}, \frac {\partial \hat {e} _ {F} (t)}{\partial \lambda} > 0 \mathrm{when} \lambda <   \frac {\alpha - \beta}{\beta}, \mathrm{and} \frac {\partial \hat {e} _ {F} (t)}{\partial \lambda} \leq 0 \mathrm{when} \lambda \geq \frac {\alpha - \beta}{\beta}.
$$

$$
\frac {\partial \widehat {\phi}}{\partial \lambda} = \frac {\alpha^ {2} (\beta^ {2} (1 + \lambda) ^ {2} - \alpha^ {2})}{(\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2}) ^ {2}}, \frac {\partial \widehat {\phi}}{\partial \lambda} <   0 \mathrm{when} \lambda <   \frac {\alpha - \beta}{\beta}, \mathrm{and} \frac {\partial \widehat {\phi}}{\partial \lambda} > 0 \mathrm{when} \lambda > \frac {\alpha - \beta}{\beta}.
$$

Proposition 4(b):

It is easy to prove that under the monitoring contract and liability contract, $\begin{array} { r } { \frac { \partial e _ { M } ( t ) } { \partial \lambda } > 0 \mathrm { ~ a n d } \frac { \partial e _ { F } ( t ) } { \partial \lambda } > 0 } \end{array}$

## Proof of Proposition 6:

According to Lemma 2, the MSSP’s expected payoff under the BRC is

$$
\widehat {U} _ {M} = 2 V (T) - 2 a L T (1 + \lambda) (1 - q _ {0}) + \frac {\varepsilon^ {2} a ^ {2} L ^ {2} T ^ {3} (1 + \lambda) ^ {2} (\beta^ {4} (1 + \lambda) ^ {2} + \alpha^ {4} + \alpha^ {2} \beta^ {2})}{3 C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2})} - 2 \underline {{U}} _ {F}.
$$

According to Lemma 4, the MSSP’s expected payoff under the liability contract is

$$
\widetilde {U} _ {M} = 2 V (T) - 2 a L T (1 + \lambda) (1 - q _ {0}) + \frac {\varepsilon^ {2} a ^ {2} L ^ {2} T ^ {3} (1 + \lambda) ^ {2} (\alpha^ {2} + \beta^ {2})}{3 C} - 2 \underline {{U}} _ {F} - C _ {V}.
$$

$$
\widetilde {U} _ {M} - \widehat {U} _ {M} = \frac {\varepsilon^ {2} a ^ {2} L ^ {2} T ^ {3} (1 + \lambda) ^ {4} \alpha^ {2} \beta^ {2}}{3 C (\beta^ {2} (1 + \lambda) ^ {2} + \alpha^ {2})} - C _ {V}.
$$

Thus $\widetilde { U } _ { M } > \widehat { U } _ { M }$ when $C _ { V } < C _ { 0 }$ , where $\begin{array} { r } { C _ { 0 } = \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 4 } \alpha ^ { 2 } \beta ^ { 2 } } { 3 C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + \alpha ^ { 2 } ) } . } \end{array}$

It is straightforward to find that $\begin{array} { r } { \frac { \partial C _ { 0 } } { \partial a } > 0 , \frac { \partial C _ { 0 } } { \partial \lambda } > 0 , a n d \frac { \partial C _ { 0 } } { \partial T } > 0 . } \end{array}$

In addition, keeping $\alpha + \beta = m$ , then $\begin{array} { r } { C _ { 0 } = \frac { \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 4 } ( m - \beta ) ^ { 2 } \beta ^ { 2 } } { 3 C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + ( m - \beta ) ^ { 2 } ) } \frac { \partial C _ { 0 } } { \partial \beta } = - \frac { 2 \varepsilon ^ { 2 } a ^ { 2 } L ^ { 2 } T ^ { 3 } ( 1 + \lambda ) ^ { 4 } ( m - \beta ) \beta ( \beta ^ { 3 } ( 1 + \lambda ) ^ { 2 } - ( m - \beta ) ^ { 3 } ) } { 3 C ( \beta ^ { 2 } ( 1 + \lambda ) ^ { 2 } + ( m - \beta ) ^ { 2 } ) ^ { 2 } } . } \end{array}$

Thus when $\begin{array} { r } { \beta < \frac { \theta m } { 1 + \theta } \frac { \partial C _ { 0 } } { \partial \beta } > 0 } \end{array}$ , and when $\begin{array} { r } { \beta > \frac { \theta m } { 1 + \theta } , \frac { \partial C _ { 0 } } { \partial \beta } < 0 } \end{array}$ , where $\begin{array} { r } { \theta = ( \frac { 1 } { ( 1 + \lambda ) ^ { 2 } } ) ^ { \frac { 1 } { 3 } } . } \end{array}$

Similar, when $\begin{array} { r } { \alpha < \frac { \theta m } { 1 + \theta } , \frac { \partial C _ { 0 } } { \partial \alpha } > 0 } \end{array}$ , and when $\begin{array} { r } { \alpha > \frac { \theta m } { 1 + \theta } , \frac { \partial C _ { 0 } } { \partial \alpha } < 0 } \end{array}$ , where $\theta = ( 1 + \lambda ) ^ { \frac { 2 } { 3 } } ,$

## About the Authors

Yong Wu is an assistant professor at Glorious Sun School of Business & Management at Donghua University in China. He obtained his Ph.D. from both City University of Hong Kong and Xi’an Jiaotong University. His research interests include information security economics, game theory, and information systems outsourcing. He has published research articles in journals such as Journal of the Operational Research Society, Decision analysis, Computers & Industrial Engineering, and Expert Systems with Applications.

Giri Kumar Tayi is a professor of management science and information systems at the State University of New York at Albany. He obtained his Ph.D. from Carnegie Mellon University and his research and teaching interests are interdisciplinary and span the fields of information systems, operations management, and operations research. His papers have appeared in Operations Research, Information Systems Research, Management Science, MIS Quarterly, IEEE Transactions, Networks, Naval Research Logistics, EJOR, Journal of Combinatorial Optimization, INFORMS Journal of Computing, Journal of Computer Security, Quantitative Marketing and Economics, Journal of Operations Management, Government Information Quarterly, Communications of the ACM, and elsewhere.

Gengzhong Feng is a professor of information management and e-business in the School of Management, Xi’an Jiaotong University, P. R. of China. He obtained a B.S. in computer science in 1987, an M.S. in systems engineering in 1990, and a Ph.D. in management engineering in 1993, all from Xi’an Jiaotong University of China. His research interests include logistics and supply chain management, information system management, big data, and information quality. His research has been published in the journals such as Journal of the Association for Information Systems, European Journal of Operational Research, Omega-International Journal of Management Science, International Journal of Production Research, Journal of the Operational Research Society, Computers & Industrial Engineering, Expert Systems with Applications and elsewhere.

Richard Y. K. Fung holds a B.Sc.(Hons) in production engineering and master of philosophy (M.Phil.) degree in manufacturing resource planning both from the Aston University in Birmingham, UK. Subsequently, he received his Ph.D. in customer requirements management from Loughborough University, UK. Prof. Fung worked in the industry for over 15 years in various capacities including product development, production planning and control, design and implementation of management information systems, and management consulting. After returning to Hong Kong, he taught at City University of Hong Kong for over 30 years. During this period, Prof. Fung also held concurrent roles as the director of the Laboratory of Enterprise Knowledge Integration & Transfer, and the deputy director of the Co operative Education Centre, serving the industry and the community through various organizations, professional institutions, and learned societies. Prof. Fung’s academic and research specialties include knowledge management, quality management, customer requirements analysis, quality function deployment, supply chain and cold chain logistics, maritime & aviation management, healthcare management, systems security, business continuity management, and the development and implementation of IT and artificial intelligence solutions for industry.

Copyright © 2021 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org
