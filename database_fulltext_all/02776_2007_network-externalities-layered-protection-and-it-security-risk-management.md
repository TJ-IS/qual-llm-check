---
otero_id: 2776
otero_key: "RFZJV4H8"
title: "Network externalities, layered protection and IT security risk management"
authors: "Wei T. Yue; Metin Çakanyıldırım; Young U. Ryu; Dengpan Liu"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.08.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2007) 1 – 16

www.elsevier.com/locate/dss

# Network externalities, layered protection and IT security risk management

Wei T. Yue <sup>a,⁎</sup>, Metin Çakanyıldırım <sup>a</sup>, Young U. Ryu <sup>a</sup>, Dengpan Liu <sup>b</sup>

<sup>a</sup> Department of Information Systems and Operations Management, School of Management, The University of Texas at Dallas, Richardson, Texas 75083-0688, USA

<sup>b</sup> Department of Economics and Information Systems, College of Administrative Science, University of Alabama in Huntsville, AL 35899, USA

Received 15 June 2005; received in revised form 26 July 2006; accepted 13 August 2006 Available online 13 October 2006

## Abstract

This paper considers two important issues related to security risk management. First, the presence of network externalities in security risks. Second, the distinction of general (network) and system-specific protection measures. We found the optimal allocation of security resources (investments) in protecting every system in an organization. The results show that the consideration of network externalities and layered protection changes the risk mitigation decisions significantly. In addition, accurate estimation of system risk plays a critical role in the success of risk management. Otherwise, the use of a uniform baseline protection approach may be more desirable when the misjudgment of relative system risks is likely to occur. © 2006 Elsevier B.V. All rights reserved.

Keywords: IT risk management; IT risk analysis; IT risk mitigation; Security investments; Security resource planning

## 1. Introduction

Increasingly, today's organizations rely on information technology (IT) in their daily operations. The increased reliance on information technology has reinforced the importance of IT security for organizations, especially when many surveys continue to show that organizations are susceptible to cyber attacks [10,28,27]. In facing the daunting task of protecting an array of information systems, there are different ways an organization can protect its systems. For example, utilizing security devices such as firewalls for perimeter defense; intrusion detection systems to monitor irregular network and system activities; access control system to facilitate access policy development and enforcement, etc. In addition, spending in training and awareness programs allows users to have better knowledge and higher vigilance towards system threats. All these measures can potentially help organizations to reduce security risks. However, before any protection decisions, it is essential that an organization first possess a clear understanding of their security risks. IT security risk management helps to achieve these goals. Its main activities involve identifying and classifying organizational IT security risks (.risk assessment), and identifying appropriate strategies to mitigate the risks (.risk mitigation). In general, IT risk management can be considered to be a critical prerequisite for sound security investment decisions.

To highlight the importance of IT security risk management, there are various guidelines and standards advocating and guiding such practices. The IT risk management guide by the National Institute of Standards and Technology (NIST) [30], the international standard in security management, British Standard BS7799:2, by the British Standards Institution (BSI), the Control Objectives for Information and related Technology (COBIT), by the IT Governance Institute, and the Enterprise Risk Management Framework sponsored by the Committee of sponsoring Organizations of the Treadway Commission (COSO). Recently, increasing emphasis on corporate accountability and privacy concerns in the form of laws and regulations (e.g. Sarbanes–Oxley Act (SOX) and Health Insurance Portability and Accountability Act (HIPPA), and Gramm–Leach–Bliley (GLBA) Act)<sup>1</sup> requires organizations to possess clear definitions on control measures, and provide guarantees on information assurance. The greater compliance requirements have made IT security risk management an increasingly indispensable responsibility for the IT managers.

While the managerial guidelines provide useful guidance for implementation, there is a lack of discussions regarding the key managerial components in the risk management process. In this paper, we examine two issues in the risk management process in greater details, i.e., the system interdependencies and layered protection strategies. Nowadays, with the greater interconnection and integration of IT infrastructure, system interdependencies is the norm. In the mean time, it also creates cascading effects (.negative externalities) in security risks. This occurs because a compromised system could continue to compromise another system, referred as .secondary or .subsequent attacks. Therefore, we should not overlook the fact that IT system can be an .object as well as a .subject of attack. Security practitioners have long stressed that IT assets are “as secure as the weakest link”. As we will discuss later, the weakest link often appears because system interdependency risks are not considered in risk assessment.

It is also important to note that the act of protection creates externalities effect. A successfully defended IT system prevents attackers/hackers from attacking the system as well as reduces the possibility of future attacks. Therefore, .where the protection measures are applied is crucial. Another vital question is .what has to be applied in order to achieve minimum risk. The current risk management guidelines often treat the two questions as separate decisions. That is, the relative risks of the different components in the IT infrastructure are first identified, and subsequently protection measures are developed from the highest value system to the lowest value system. This approach tends to treat security measures as system-specific and neglects the fact that protection measures could cover more than a single system. For example, network-based intrusion detection systems (IDS) and firewall are applied to protect many systems. In addition, these host-based and network-based technologies are often applied at the same time. This type of strategy, called the .defense in depth or layered protection strategy, is a common approach in many security problems. Without the distinction of “general” and “system-specific” protection measures, the risk mitigation process is likely to lack an organizational perspective.

It is often noted that risk management decisions are based on the assumptions made by the participants. The risks arising from system connectivity while acknowledged, often were not stressed in the guidelines because such risks may be difficult to estimate. Security investment decisions are made on a single system basis or single protection measure basis because it is more convenient to do so. Nevertheless, it is important for us to understand what are the implications of using those assumptions, and acknowledge their potential limitations. We intend to do so by studying the risk management practices following different assumptions on externalities and protection layers using different models. These models allow us to evaluate and contrast security investment decisions, achieved security levels, and risk reduction levels.

An important aspect of our study is to understand how security resources should be distributed across systems – .horizontally – as well as across protection layers — .vertically. Essentially, this is a resource allocation problem and it is unique in the security context. A proper use of security resources is important because recent industry surveys by.Information Security Magazine, .Information Week, and .Ernst and Young have found the lack of a security budget to be one of the main obstacles in achieving security [6,29,10]. In this paper, we solve a security resource allocation problem with nonlinear objective function. Our results show that the level of discrepancies between including and not including externalities in risk assessment depends on the secondary attack patterns. In addition, the weakest link scenario essentially demands a more uniform distribution of security resources in order to protect the different assets. In the presence of a layered protection strategy, greater emphasis is placed on the network protection measure and result in less resources are invested in system-specific protection.

The difficulty of estimating risk management parameters is another important issue considered in this paper. Given that risk assessment is still an imprecise science, the potential negative impacts of not estimating the initial risks properly are critical. An important managerial insight derived from our analysis is that a successful risk management exercise hinges on the proper ranking of system risks. Otherwise, naive baseline approach may generate better results.

Gordon and Loeb [12] was first to derive the optimal security investment level for a firm. Their work and subsequent literatures on the economics of IT security investment have focused on a single system or a single type of protection technology, in which the externalities and layered protection issues are not discussed [7,11,8]. This paper extends those work by formulating and solving the problem according to the risk management paradigm, therefore provides manager additional insights in how to obtain the optimal decisions. Second, we distinguish general (network) and system-specific protections in the risk management process. In doing so, we are able to discuss additional issues such as the impact of having internal and external attackers, and also show that security risk needs to be considered from the organizational perspective. Third, the effect of network externalities to risk assessment is shown. Fourth, we address the issues of uncertainty in the risk management process, i.e., the condition under which the baseline approach should be used.

The paper is organized as follows. Next section provides an overview on risk management. Section 3 considers three models dealing with network externalities and layer protection. In this section, we provide the solutions and discuss the managerial insights. Lastly, Section 4 concludes the paper.

## 2. Risk management and IT security investment

Recent surveys by .Information Security Magazine, Ernst and Young and .Information Week have stated that the lack of security budget is one of the main obstacles for firms to achieve desirable level of security protections [6,10,29]. Given such constraints, security resource planning, such as risk management, is important to ensure the limited organizational resource is applied effectively. In general, ITsecurity risk management has two important goals: i) to assess security risks and ii) to select protection measures to reduce security risks. The main activities include risk identification, risk analysis and risk control [36,30,2,26,4], where each involves a set of tasks as shown in Fig. 1. Essentially, risk management allows organizations to approach security in a more structured manner. It has been found that typically when security managers do not have a complete view about the security remedies, they would follow a structured security planning framework to reduce system risks [33].

The first step, risk identification, involves finding out IT asset values, potential threats and potential countermeasures. The second step deals with analyzing the potential security risks for individual systems, which includes the consideration of potential financial impacts when assets are compromised (sometimes referred as business impact analysis). Given that security risks is the product of probability of compromise and the expected losses, the likelihood of threat, vulnerability and the effectiveness of current counter-measures found in the first step are also used in computing the risks. At the conclusion of the risk identification and analysis steps, security managers should have good understanding about the security risks for individual systems, or the .risk profiles for the organization. One way to analysis the risk profiles is to study the transaction workflows of the organization [34].

Loch, Carr and Warkentin [18] found that according to MIS directors and security managers, natural disasters, accidental entry and destruction of data, and weak protection, ranked as the main threats for organizations. Vulnerabilities are often found in software and the daily execution of organizational activities.

![](/api/attachments/RFZJV4H8/fulltext/images/6a0a613c3a6bb60d69bc0c46be41a6820aa80a5098e1647ea5736352fc0b04e8.jpg)  
Fig. 1. Risk management process.

Currently, different quantitative and qualitative methodologies are proposed for IT security risks analysis. For instance, annualize loss expectancy (ALE) [36], the Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE) [2], stochastic dominance [26], LRAM [13], TOPM [4], fuzzy set theory approach [22,9], etc.

Once the security risks have been analyzed, the next stage involves selecting the best security measures for reducing risks. Nowadays, organizations apply prevention, detection and recovery-based techniques to mitigate risks [15]. Moreover, deterrence strategies are commonly used against internal attackers. In fact, deterrence strategies were found to be more effective than preventive measures before the growth of electronic commerce [32]. Others have viewed security protection from the perspectives of management, applications/technical and operations controls [1,23]. In order to reach the decision on what security measures are to be applied, security managers often need to conduct cost and benefit analysis as well as other types of feasibility analysis [36]. Conducting cost and benefit analysis requires sorting and matching different vulnerabilities and protection measures. Genetic algorithm has been used to find the vulnerability and protection sets to minimize costs [14].

In many aspects, IT risk management is similar to software risk management [19,20,5]. With regard to techniques, many of the concepts in software risk management can be applied to IT security risk management. For example, Anderson and Narasimhan [3] proposed the used of discriminant analysis to identify risk factors in software projects. In principle, the same method can be used to analyze the significance of individual threat and vulnerability factors (risk factors) so that the likelihood of successful attacks can be estimated. Some other studies address security risks management in a manner that is similar but with finer granularity; attack/privilege graphs techniques [17,24] are used to analyze the network risks of a given network topology with the intention of finding the best type of protection measure to be applied at the strategic network locations.

## 3. Model development

Our model can be viewed as an extension of Gordon and Loeb's model [12]. We assume that there are .m IT systems for a risk-neutral organization. The objective for the organization is to achieve minimum organizational risks by finding the optimal allocation of protection resources with a given budget resource $Q .$ Other previous research has considered single system risk minimization problem without budget constraint [7,11,8,12]. Similar to previous studies, our model treats the knowledge about system risk profiles and the expected performance of the security measures as input parameters. Therefore, the risk identification and assessment steps are completed at the time of making the security resource allocation decision. We assume that risk assessment can be done with or without taking the network externalities effect into consideration. Later on, we will address the issue of uncertainty in risk analysis.

There are two types of attackers. The first type of attacker needs to defeat both the general and systemspecific protection measures in order to compromise a system, while the second type of attacker only has to defeat the system-specific measure to compromise a system. Without loss of generality, we call them external and internal attackers. The distinction here is to address the fact that some attackers are located closer than others to the target systems. For instance, in many occasions the only means of protecting against internal attackers are the internal (system-specific) measures, while the general protection measure is used against attackers who are not tied to the target systems. In a way, the two types of attackers are synonymous with attackers coming from inside or outside the operation unit. That is, externa attackers have no access rights to ITsystems, while interna attackers have access rights. If we equate the operation unit to the entire organization, that would obviously make the general protection measure more like the perimeter defense measure. The distinction of attacker types is important here because the characteristics of the protection measures differ. On a side note, even though external attacks are commonly reported in the media, a recent Symantec Internet security threat report [16] found substantial internal threats.

System $i ( i { = } 1 , 2 , . . . , m )$ is assumed to have an initial vulnerability level $0 < V _ { i } \leq 1$ . When neither general measures nor system-specific measures are used to protect the systems, there is no distinction between external and internal attackers. There is a total of .N number of attack attempts over the given budget cycle. Out of all the attack attempts, $\theta \in [ 0 , 1 ]$ fraction belongs to external attacks. Among internal and external attacks, there is $\rho _ { i } \in [ 0 , 1 ]$ fraction of attacks on system .i.

Investments in security measures reduce the likelihood of compromising systems. For example, against external attacks, investments of $x _ { i }$ in the system-specific protection and $y$ in the general protection measure reduce system $i \mathrm { \ ' } _ { \mathrm { S } }$ breach probability to $p ( x _ { i } , y ) \in [ 0 , 1 ]$ The same system-specific investment of $x _ { i }$ also reduces the breach probability to $q ( x _ { i } )$ against internal attacks. The breach probability functions $p ( x _ { i } , y )$ and $q ( x _ { i } )$ are assumed to be decreasing convex functions with investments. Previous experimental studies have found support for such an assumption [21]. This assumption is also consistent with previous work [12]. When there are zero investments in any security measures, vulnerability does not reduce and remains as an initial vulnerability. Furthermore, since absolute security is impossible, the only way to achieve it is when the security investment is infinity. The following summarizes the characteristics of the security measures.

Table 1 Definition of variables

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $V_{i} \in (0, 1], i \in \{1, ..., m\}$ </td><td>Initial vulnerability for system  $i$ </td></tr><tr><td> $N$ </td><td>Total number of attack incidents</td></tr><tr><td> $\theta \in [0, 1]$ </td><td>Fraction of external attacks</td></tr><tr><td> $\rho_{i} \in [0, 1], \sum_{i=1}^{m} \rho_{i} = 1$ </td><td>Fraction of attack incidents on system  $i$  out of all attacks</td></tr><tr><td> $y \in [0, Q]$ </td><td>Investment in general security measure</td></tr><tr><td> $x_{i} \in [0, Q]$ </td><td>Investment in system-specific security measure for system  $i$ </td></tr><tr><td> $p(x_{i}, y) \in [0, 1]$ </td><td>Probability of successful attack on system  $i$  from external attacks, given investment  $x_{i}$  and  $y$ </td></tr><tr><td> $q(x_{i}) \in [0, 1]$ </td><td>Probability of successful attack on system  $i$  from internal attacks, given investment  $x_{i}$ </td></tr><tr><td rowspan="2"> $S_{i} \overline{S}_{i}$ </td><td>Expected losses, given successful attack on system  $i$ </td></tr><tr><td>Total expected losses due to a successful attack on system  $i$ </td></tr><tr><td> $\phi_{ik} \in [0, 1], i \neq k$ </td><td>Expected probability of successful successive attacks from system  $i$  to system  $k$ </td></tr></table>

$$
\begin{array}{l} \text { A1. } 0 \leq p (x _ {i}, y) \leq 1; 0 \leq p (x _ {i}) \leq 1 \\ \text { A2. } p (x _ {i} = 0, y = 0) = V _ {i}; p (x _ {i}, y = 0) = q (x _ {i}); p (x _ {i}, y = \infty) \\ \quad = 0 \\ \text { A3. } q (x _ {i} = 0) = V _ {i}; q (x _ {i} = \infty) = 0 \\ \text { A4. } p _ {y} <   0, p _ {y y} > 0 ^ {2}; p _ {x _ {i}} <   0, p _ {x _ {i} x _ {i}} > 0 \\ \text { A5. } q _ {x _ {i}} <   0; q _ {x _ {i} x _ {i}} > 0 \end{array}
$$

In our formulation, all systems are connected to each other. A successful attack on system .i may incur total losses of $\overline { { S } } _ { i } ,$ where the total losses include losses occurred at system.i and the subsequently compromised systems. In general, losses incurred because of the breach of confidentiality, integrity, and availability of IT assets. Investment in security measures translates to the benefit of expected losses/risks reduction. The probability of successive attacks from.i to.k is represented by $\phi _ { i k } .$ . We will provide further explanation regarding this variable in the next subsection. To summarize, Table 1 lists the definitions of the variables.

The problem P1 is formulated as the optimization of the security investment allocation on general and systemspecific protection measures to maximize reduction in security risks. There is only one type of system-specific and general protection measure. Each system may be protected individually with a system-specific protection investment. The investment in the general protection measure reduces the security risks of.all systems. Later on we will relax this assumption in which the “general” protection measure only protects a number of systems.

Problem P1

$$
\begin{array}{l} b (\mathbf {x}, y) = \max N \sum_ {i = 1} ^ {m} \\ \rho_ {i} \big (\theta (V _ {i} - p (x _ {i}, y)) \overline {{S}} _ {i} + (1 - \theta) (V _ {i} - q (x _ {i})) \overline {{S}} _ {i} \big) \\ \text { subject   to } \sum_ {i = 1} ^ {m} x _ {i} + y \leq Q \\ x _ {i} \geq 0 \quad \text { for } i = 1, 2,..., m \\ y \geq 0. \end{array}
$$

## 3.1. Risk assessment: initial risks

Initial risks can be considered with or without network externalities. The initial risk for system .i can be written as

$$
N \rho_ {i} V _ {i} \bar {S} _ {i}\tag{1}
$$

The organization-wide initial risks to IT assets are

$$
N \sum_ {i = 1} ^ {m} \rho_ {i} V _ {i} \bar {S} _ {i}\tag{1'}
$$

With Network Externalities. When there is no interdependency, $\phi _ { i j } = 0 , \forall \ i , j .$ . Therefore,

$$
\bar {S} _ {i} = S _ {i}\tag{2}
$$

total expected losses upon a successful attack are formulated as Eq. (2). The initial system and organizational risks are again represented by Eqs. (1) and (1′).

With Network Externalities. In the presence of network externalities, the vulnerability of one system can have negative effects on other systems. The consideration of the network externalities allows us to consider the risks arise from secondary attacks. Similarly, a system's protection can positively affect other connected systems. There are different ways to model the propagation of attacks. When there are successive attacks, accounting for the total risks of one system includes considering the propagated risks. They can be accounted for either by including them in the system that.originates the attack or.receives the attack. In our formulation, we have chosen to adopt the first approach. Hence, when the propagation of attacks only occurs once from the original source, the expected losses for a system are represented by

$$
\overline {{S}} _ {i} = \left[ S _ {i} + \sum_ {k = 1 \atop k \neq i} ^ {n} \phi_ {i k} S _ {k} \right]\tag{3}
$$

If we relax the assumption and allow the attacker to subsequently attack from the second compromised system, the expected loss associated with the original attack on system .i is

$$
\bar {S} _ {i} = \left[ S _ {i} + \sum_ {\substack {k = 1 \\ k \neq i}} ^ {n} \phi_ {i k} \left(S _ {k} + \sum_ {\substack {l = 1 \\ l \neq i, k}} ^ {n} \phi_ {k l} S _ {l}\right) \right]\tag{4}
$$

The formulation can be extended to include further subsequent attacks from the 2nd, 3rd, etc., compromised systems. As for the initial risk to the system and organization, they are again represented by Eqs. (1) and $( 1 ^ { \prime } )$ , keeping in mind that .S<sup>¯</sup> now includes losses from propagated attacks. Note that when attacks propagate less than $m - 1$ time, the attack propagation trajectory becomes an issue. For example, all subsequent attacks from all systems can target the same system or different systems. We treat the knowledge about the subsequent target system and the probability of compromising as input given to the model.

To simplify our analysis, we assume that an attack only propagates once (i.e., an compromised system could lead to at most one other system to be compromised). This assumption does not change the observations derived from the following proposition.

Proposition 1. .Risk assessment without taking network externalities into consideration under-estimates the expected IT security risks for the organization.

Proof of proposition. The difference in initial risks with and without network externalities is: Eq. (1′) with the expected losses given by Eq. (3) minus Eq. (1′) with the expected losses given by Eq. $( 2 ) > 0 \mathrm { i f } \exists \phi _ { i k } > 0$ for. $k \neq i$ and. $k { = } 1 , 2 , . . . , m$ □

Proposition 1 is not surprising because the actual number of attacks to the IT assets for the organization increases when successive attacks are spawned from the original attacks. If we compare the two models with the same number of attacks, Proposition 2 is the result.

Proposition 2. .When the total numbers of attacks are equal for the two models, the organization-wide assessment of risks is lower, equal, or higher with network externalities than without externalities depending on

$$
\sum_{i = 1}^{m}\rho_{i}V_{i}\sum_{\substack{k = 1\\ k\neq i}}^{m}\phi_{ik}S_{k}\lessgtr \sum_{i = 1}^{m}\rho_{i}V_{i}S_{i}
$$

Proof of proposition. Since every system generates one additional attack when there are network externalities, there are 2.N instead of .N attacks without network externalities. Therefore, the difference in initial risks with or without network externalities with the same number of total attacks (denote as $b ^ { n } ( \mathbf { x } , y ) - 2 b ^ { g } ( \mathbf { x } , y ) )$ is $\begin{array} { r } { N \sum _ { i = 1 } ^ { m } \rho _ { i } V _ { i } \Biggl ( \sum _ { k \neq i } 1 \ \phi _ { i k } S _ { k } – S _ { i } \Biggr ) } \end{array}$ . From which we get

$$
\begin{array}{l} b ^ {n} (\mathbf {x}, y) - 2 b ^ {g} (\mathbf {x}, y) \lessapprox 0 \quad \text {iff} \quad \sum_ {i = 1} ^ {m} \rho_ {i} V _ {i} \sum_ {k = 1 \atop k \neq i} ^ {m} \phi_ {i k} S _ {k} \\ \lessapprox \sum_ {i = 1} ^ {m} \rho_ {i} V _ {i} S _ {i}. \end{array}
$$

Proposition 2 shows that when the aggregate expected risks from successive attacks is larger than the risks generated by the aggregate risks from the original attacks, the model without externalities under-estimates security risks. We may also see that security risks are estimated higher without considering externalities; when additional attacks from a compromised system is more difficult to succeed than direct attack. Although the results are derived using one successive attack, similar qualitative observations can be made with multiple successive attacks. This is because the subsequent risks can be written in one term whether there are 1 or many successive attacks.

Our formulation also gives rise to some conclusions regarding risk mitigation.

Proposition 3. .The risk mitigation approach that considers general and system-specific protection measures typically performs at least as good as the approach that only considers system-specific protection measures.

Proof of proposition. Since not considering general protection $y = 0$ is a special case of considering general protection $y ^ { * } \in [ 0 , \ Q ]$ , therefore considering it will yield optimal decisions at least as good $E [ b ( x _ { i } ^ { * } , y ^ { * } ) ] \ge$ $E [ b ( x _ { i } ^ { * } , y ) ] = 0$ □

Proposition 4. .The risk mitigation approach that considers general and system-specific protection measures, and isdonesequentiallyoneachsystem,performsworsethanthe approach that considers all systems at the same instance.

Proof of proposition. When only one system is considered at a time, any prior investment in general proection. $y ^ { \prime } \in [ 0$ , .Q] cannot be decreased when the subsequent systems are considered. Therefore, an approach that allows an increase or decrease in investment level $y ^ { * }$ when subsequent systems are considered can do no worse. □

The implication from the above propositions is that in the risk mitigation process, security managers should make a distinction between general and system-specific protection measures; and it is critical to consider risk mitigation strategies with all systems instead of one system at a time.

## 3.2. Risk mitigation: protection decisions

Determining the optimal distribution of resources requires additional definitions. For further analysis, we define the following breach probability function according to A1–A5. Similar breach probability function is used in Ref. [12].

$$
p (x _ {i}, y) = V _ {i} e ^ {- (\alpha x _ {i} + \beta y)}\tag{5}
$$

where $\alpha > 0$ and $\beta { > } 0$ , and

$$
q (x _ {i}) = V _ {i} e ^ {- \alpha x _ {i}}.\tag{6}
$$

Coefficients .α, .β represent factors that influence the effectiveness of the security measures. We first consider a special case in which closed form solutions are attainable. This will occur when there is equality in the budget constraint and all the systems have the same marginal returns for a given budget $\mathcal { Q } ,$ the optimal allocations of security resources across systems and between layers are

.Single-Tier Security Protection

Let $d _ { i } { = } N \rho _ { i } V _ { i } S _ { i }$

$$
x _ {i} ^ {s *} = \frac {1}{m} \left[ Q + \frac {1}{a} \sum_ {j = 1} ^ {m} \ln \left(\frac {d _ {i}}{d _ {j}}\right) \right]\tag{7}
$$

Two-Tier Security Protection

$$
x _ {i} ^ {n *} = \frac {1}{m} \left[ Q + \frac {1}{\alpha} \sum_ {j = 1} ^ {m} \ln \left(\frac {d _ {i}}{d _ {j}}\right) - \frac {1}{\beta} \ln \left(\frac {\theta (m \beta - \alpha)}{(1 - \theta) \alpha}\right) \right]\tag{8a}
$$

and

$$
y ^ {n *} = \frac {1}{\beta} \ln \left(\frac {\theta (m \beta - \alpha)}{(1 - \theta) \alpha}\right)\tag{8b}
$$

Note that two-tier protection without externalities requires $d _ { i }$ be replaced by $c _ { i } { = } N \rho _ { i } V _ { i } S _ { i }$

In cases where both types of security measures are considered, a fraction of the security resources is allocated to the general protection measure. The results show that to achieve optimal protection resource allocation, we need to consider multiple factors. First, the distribution of internal and external threats plays an important role in how to allocate the resources. The system-specific protection resources increase with the greater presence of internal attacks. Conversely, general protection increases with more external attacks. It is not surprising that we need to consider the profiles of the attacker, and in doing so, we also need to consider the effectiveness of the security measures. That is, .α and $\beta$ play important roles in reaching the decisions. For example, when the systemspecific protections are ineffective (due to say technical deficiencies or the requirement of flexible working environment), and internal threats are high, the optimal protection that is achieved may be by putting more protection resources into the general protection measure. By doing so, the protection focus shifts to curbing secondary attacks by preventing the original attacks.

The optimal solution also takes into account of other effects such as initial risk profiles of different systems, and the number of attacks suffered by the organization. Perhaps more importantly, the decisions depend on not just the initial risk value of a system but also the risks that it creates. Protection resources are allocated according to the relative risks of the systems in both the single-tier approach and two-tier approach; the consideration of secondary attacks could make a low value system to rank higher than a high value system in relative risks, and led to the low value system to receive higher level of protections.

Proposition 5. .Two-layer protection is always at least as good as one layer protection when the aggregation of effectiveness for the general measure is at least as good as the effectiveness for the system-specific measure $( m \beta > \alpha )$

We can also make some observations about how resources should be allocated from the results.

1) In the presence of the general protection measure, fewer security resources are allocated to systemspecific protection. The spread of resources among system-specific measures therefore is more even with general protection than without general protection.

2) When the risks generated by the successive attacks are equal among all systems, the spread of security resources among system-specific measures is more uniform with network externalities than without externalities.

The intuition behind the first observation stems from the use of the general protection measure generates higher marginal returns for high-risk systems than low-risk systems. As a result, the riskier systems receive fewer resources in system-specific protection than in the case where no general protection measure is used. The results can be shown by subtracting Eq. (7) from Eq. (8a).

This second observation is due to the fact that the consideration of network externalities changes the initial risk profiles. When the risk of successive attacks is presence and equal for all systems, the relative risk between a low-risk system and a high-risk system decreases. For instance, if $c _ { 1 } = 1$ and . $c _ { 2 } = 5$ , and the risk from successive attacks is 2, then $c _ { 2 } / c _ { 1 } = 5$ , and $d _ { 2 } /$ $d _ { 1 } = 2 . 3 3$ . From Eq. (7) or Eq. (8a), it can be seen that higher risk system receives less system-specific investments when network externalities is presence. This translates to more resources being devoted to the lowrisk systems. When we assume that high-risk systems are more likely to be subjected to successive attacks, this scenario clearly requires that low-risk systems to have higher probability of successful attack by the high-risk systems than vice versa in order for the-risk generated to be equal. However, as mentioned earlier, the trajectory of the successive attacks has to be given. Therefore, equal risks in successive attacks are a restrictive assumption and the above observation does not always hold. That is, the presence of externalities does not necessarily guarantee a more uniform distribution of resources.

## 3.3. General solutions

The general solution requires the consideration of zero protection for any system due to a limitation in resources. In this section, we show the general solution procedures for the problem.

Define $d _ { i } { = } N \rho _ { i } V _ { i } S _ { i } .$ Note that we can convert the benefits maximization problem P1 to a risks minimization problem P2.

Problem P2:

$$
\begin{array}{l} \min \sum_ {i = 1} ^ {m} d _ {i} \theta e ^ {- \alpha x _ {i} - \beta y} + d _ {i} (1 - \theta) e ^ {- \alpha x _ {i}} \\ \text { subject   to } \sum_ {i = 1} ^ {m} x _ {i} + y \leq Q \\ x _ {i} \geq 0 \quad \text { for } i = 1, 2,..., m \\ y \geq 0 \end{array}
$$

Since the objective function can be shown to be convex, P2 is a convex optimization problem with a nonlinear objective function and linear constraints. Thus, a solution to KKTconditions is the optimal solution. We also scale the problem such that $c _ { i } \alpha \geq 1 \Leftrightarrow$ ln $c _ { i } \alpha \geq 0$ . Construct the Lagrangian function:

$$
\begin{array}{l} L (x _ {i}, y, \mu_ {i}, \lambda , \gamma) = \sum_ {i = 1} ^ {m} d _ {i} \theta e ^ {- \alpha x _ {i} - \beta y} + \sum_ {i = 1} ^ {m} d _ {i} (1 - \theta) e ^ {- \alpha x _ {i}} \\ \quad + \lambda \left(\sum_ {i = 1} ^ {m} x _ {i} + y - Q\right) \\ \quad + \mu_ {i} \sum_ {i = 1} ^ {m} (- x _ {i}) + \gamma (- y) \end{array} \tag {1}\tag{9}
$$

.Single-tier Protection. With no general protection measure and externalities, problem P is simplified with $y = 0$ and $\boldsymbol { \overline { { S } } } _ { i } = \boldsymbol { S } _ { i }$ . Define $c _ { i } { = } N \rho _ { i } V _ { i } S _ { i }$ . The Kuhn–Tucker conditions for the single-tier protection problem are

$$
\partial L / \partial x _ {i} = - c _ {i} \alpha e ^ {- \alpha x _ {i}} + \lambda - \mu_ {i} = 0\tag{10}
$$

$$
\sum_ {i = 1} ^ {m} x _ {i} = Q, \quad x _ {i} \geq 0\tag{11}
$$

$$
\mu_ {i} \geq 0\tag{12}
$$

$$
\mu_ {i} (- x _ {i}) = 0
$$

From the individual conditions, we can derive

<sub>ð</sub><sup>13</sup><sub>Þ</sub>

(a.) $x _ { i } = \frac { 1 } { \alpha } \ln \frac { \alpha c _ { i } } { \lambda - \mu _ { i } }$ and the condition $\lambda \geq \mu _ { i }$ has to be satisfied. 1

$$
\begin{array}{l} \text {(b.) If x_{i} >0\Rightarrow\mu_{i} = 0 (by 13)\Rightarrow x_{i} = \frac {1}{\alpha}\ln\frac{\alpha c_{i}}{\lambda}}. \\ \text {If \mu_{i} >0\Rightarrow x_{i} = 0 (by 13)\Rightarrow \mu_{i} = \lambda - \alpha c_{i}.} \end{array}
$$

In order to determine the number of systems that require system-specific investment, let us first order $c _ { 1 } \geq c _ { 2 } \geq . . . \geq c _ { m }$ then by (b.), $x _ { 1 } \geq x _ { 2 } \geq . . . \geq x _ { m } , \ \mu _ { 1 } \leq$ $\mu _ { 2 } \leq \ldots \leq \mu _ { m } .$ Let $\overline { { m } } = \operatorname* { m i n } \{ i { : } x _ { i + 1 } { = } 0 , i { \geq } 1 \} . \operatorname { I f } x _ { m } { \geq } 0$ , then set $\bar { m } =$ $m + 1$

Using (b.), with $c _ { i } \geq c _ { i + 1 }$ , we get. $x _ { 1 } \ge x _ { 2 } \ge . . . \ge x _ { \overline { { { m } } } } > 0 =$ $x _ { \bar { m } + 1 } = . . . = x _ { m } , \mu _ { 1 } \leq \mu _ { 2 } . . . \leq \mu _ { \bar { m } } < 0 = \mu _ { \bar { m } + 1 } = . . . = \mu _ { m }$

All that remains is finding $m ^ { - }$ . For that purpose, define .λ for $1 \leq n \leq m$ ,

$$
\ln \lambda (n) := \frac {1}{n} \left(\sum_ {i = 1} ^ {n} \ln \alpha c _ {i} - \alpha Q\right)\tag{14}
$$

Since $c _ { i } \geq c _ { i + 1 }$ , we know ln $\lambda ( n )$ is decreasing in .n. Furthermore, $\begin{array} { r } { \frac { 1 } { \alpha } \ln \lambda ( 1 ) { \le } \frac { 1 } { \alpha } \ln \alpha c _ { 1 } } \end{array}$ . For $\overline { { m } } \geq 1$ , consider the following algorithm to find the number of systems to have system-specific protection ${ \overline { { m } } } ;$

The algorithm yields $\lambda = \lambda ( \overline { { m } } )$ . To solve the KKT set, we get

$$
\begin{array}{l} x _ {i} = \frac {1}{\alpha} (\ln \alpha c _ {i} - \ln \lambda), \quad \mu_ {i} = 0 \qquad \text { for } 1 \leq i \leq \bar {m} \\ \mu_ {i} = \lambda - \alpha c _ {i}, \quad x _ {i} = 0 \qquad \text { for } \bar {m} <   i \leq m \end{array}
$$

Two-tier Protection with Externalities. For the two-tier protection problem, the Kuhn–Tucker conditions are

$$
\frac {\partial L}{\partial x _ {i}} = - d _ {i} \theta \alpha e ^ {- \alpha x _ {i} - \beta y} - d _ {i} (1 - \theta) \alpha e ^ {- \alpha x _ {i}} + \lambda - \mu_ {i} = 0\tag{15}
$$

$$
\frac {\partial L}{\partial y} = - \sum_ {i = 1} ^ {m} d _ {i} \theta \beta e ^ {- \alpha x _ {i} - \beta y} + \lambda - \gamma = 0\tag{16}
$$

$$
\sum_ {i = 1} ^ {m} x _ {i} + y = Q, \quad \mathrm{x} _ {\mathrm{i}} \geq 0, \quad \mathrm{y} \geq 0\tag{17}
$$

$$
\mu_ {i} \geq 0, \quad \gamma \geq 0\tag{18}
$$

$$
\mu_ {i} (- x _ {i}) = 0, \quad \gamma (- \mathbf {y}) = 0\tag{19}
$$

Again, we can generate the following conditions

$$
\begin{array}{l} \text {(a.)} x _ {i} = \frac {1}{\alpha} \ln \frac {\alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1)}{\lambda - \mu_ {i}}, \\ y = \frac {\frac {1}{\beta} \ln \sum_ {i} ^ {m} d _ {i} \beta \theta e ^ {- \alpha x i}}{\lambda - \gamma}, \end{array}
$$

and the conditions $\lambda \ge \mu _ { i } , \lambda \ge \gamma$ have to be satisfied.

$$
\begin{array}{l} \text {(b.) If} x _ {i} > 0 \Rightarrow \mu_ {i} = 0 (\text {by (19)}) \Rightarrow x _ {i} = \frac {1}{\alpha} \ln \frac {\alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1)}{\lambda}. \\ \quad \text {If} x _ {i} = 0 \Rightarrow \mu_ {i} > 0 (\text {by (19)}) \Rightarrow \mu_ {i} \\ \quad = \lambda - \alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1). \end{array}
$$

When $\gamma > 0 ,$ it has already been solved in the previous case because $y = 0$ . Without loss of generality, let $\begin{array} { r } { \gamma = 0 , y = \frac { 1 } { \beta } \ln \frac { \sum _ { i } ^ { m } \dot { d _ { i } } \beta \theta e ^ { - z x _ { i } } } { \lambda } } \end{array}$

We first order $d _ { 1 } \ge d _ { 2 } \ge . . . \ge d _ { m }$ then by $( \mathbf { b } . ) , x _ { 1 } \geq$ $x _ { 2 } \ge . . . \ge x _ { m } , ~ \mu _ { 1 } \le \mu _ { 2 } \le . . . \le \mu _ { m } .$ . With regard to general protection measure, the decision on general protection measure is first derived. From (b.), we get

$$
e ^ {- \beta y} = \frac {\alpha (1 - \theta)}{\theta (m \beta - \alpha)},\tag{20}
$$

and for $y { > } 0$ , ln $\cdot m \beta - \alpha ) >$ ln .α(1 −.θ) − ln .θ has to be satisfied.

In order to find the number of systems for systemspecific investment, let us define $\overline { { { m } } } = \operatorname* { m i n } \{ i { : } x _ { i + 1 } = 0 ;$

$i \ge 1 \} . \mathrm { I f } x _ { m } \ge 0$ , then set ${ \overline { { m } } } = m + 1$ . Therefore, with $d _ { i } \geq$ $d _ { i + 1 } , \ \mathrm { w e }$ get $x _ { 1 } \geq x _ { 2 } \geq . . . \geq x _ { \bar { m } } > 0 = x _ { \bar { m } + 1 } = . . . = x _ { m } ,$ $\mu _ { 1 } \leq \mu _ { 2 } \leq . . . \leq \mu _ { \bar { m } } < 0 = \mu _ { \bar { m } + 1 } = . . . = \mu _ { \mathrm { m } } . \mathrm { N e x t }$ , we define .λ for $1 \leq n \leq m$

$$
\ln \lambda (n) := \frac {1}{n} \left(\sum_ {i = 1} ^ {n} \ln \alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1) - \alpha (Q - y)\right)\tag{21}
$$

Since $d _ { i } \geq d _ { i + 1 }$ , we know ln. $\lambda ( n )$ is decreasing in $n .$ We know $\begin{array} { r } { \frac { 1 } { \alpha } \ln \lambda ( 1 ) \le \frac { 1 } { \alpha } \alpha \ln d _ { 1 } ( \theta e ^ { - \beta y } - \theta + 1 ) } \end{array}$ . For. $\overline { { m } } \geq 1$ , we use the same algorithm in Table 2 to find ${ \overline { { m } } } ,$ except now the If condition in step A is replaced by $\begin{array} { r } { \frac { 1 } { \gamma } \ln \lambda ( \overline { { m } } + 1 ) < \frac { 1 } { \gamma } \ln \alpha d _ { m + 1 } ( \theta e ^ { - \beta y } - \theta + 1 ) } \end{array}$

Once $\lambda = \lambda ( \overline { { m } } )$ has been determined, the solutions for KKT set are:

$$
\begin{array}{l} x _ {i} = \frac {1}{\alpha} (\ln \alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1) - \ln \lambda), \\ y = \frac {1}{\beta} \ln (\theta (m \beta - \alpha) / (1 - \theta) \alpha), \\ \mu_ {i} = 0 \qquad \text { for } 1 \leq i \leq \bar {m}, \quad x _ {i} = 0, \\ \mu_ {i} = \lambda - \alpha d _ {i} (\theta e ^ {- \beta y} - \theta + 1) \\ \text { for } \bar {m} <   i \leq m. \end{array}
$$

It is more difficult to derive the general solution; the budget constraint requires the check of enough resources are left for consumption. In solving the twotier problem, the benefits of applying general protection measure have to be first considered. Since we assume that the general measure protects all systems, this decision requires the comparison of the benefits derived from general and system-specific protection. If the general protection measure were to be applied, smaller budget is left for the system-specific protections. The procedure to determine system-specific protections is considered next. This process is similar in the one-tier and the two-tier approaches because both require relative system risks to be used to determine the appropriate investment levels. However, since part of the budget is spent if general protection were applied, system-specific protection will be less for the same system (say system .i) in the two-tier approach. Furthermore, some low-risk systems may not require additional protection with the presence of general protection.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 2
System count algorithm
Set  $\overline{m}=1, f=0$ 
Repeat until f=1 or  $\overline{m}&gt;m$ 
A: If  $\frac{1}{\alpha}\ln\lambda(\overline{m}+1)&lt;\frac{1}{2}\ln\alpha c_{\overline{m}}+1$ $\overline{m}=\overline{m}+1$ 
Else f=1
</div>

![](/api/attachments/RFZJV4H8/fulltext/images/4313cae156d5192833c0767ea626f20ee6b39f6798480da1643516a40832a28d.jpg)  
Fig. 2. Initial risk levels for system .i.

From the intuition generated from our solution, numerical examples were constructed using Matlab v6.5 to illustrate some of the relevant issues in risk management.

## 3.3.1. Numerical examples

In the numerical examples, we assume that an organization has 200 systems, and the distribution of system value can be ordered from high to low following a normally distributed function. It is not difficult to envision such a setup because an organization usually has system of different values. For example, the customer relationship management systems, online ordering servers, etc. would be the most critical systems for a Web retailer. Individual workstations in the organization would command lesser value. In addition, individual workstations can also come in different values. That is, a machine used by a senior manager may have more business secrets than average employee. We assume 3000 unit of resources are given, the organization suffers 100,000 attacks and 30% of the users are external users in the planning cycle. As in the previous subsections, we assume there is only one subsequent attack. Too many subsequent attacks could generate unrealistic scenarios, in which a system could be compromised multiple times from various other systems. The baseline case is: without externalities and layered protection. We compare the baseline case to the cases where layered protection is presence, and with or without network externalities. The case in which there is network externalities but no layered protection is not considered here because a more general case has been considered (with network externalities and layered protection).

For all of our examples, we use the following parameter values: $V _ { i } { = } 0 . 9 ,$ , for $i { = } 1 , 2 , . . . , m ; \theta { = } 0 . 3$ 2 $m = 2 0 0 , \ : N = 1 0 0 , 0 0 0 , \ : Q = 3 0 0 0 , \ : \alpha = 0 . 0 2 , \ : \beta = 0 . 0 1 , \ : \rho _ { i } =$ 1/200 for. $i { = } 1 , 2 , . . . , m . \ S _ { i }$ is generated using the normal density function .normpdf; $S _ { i } { = } n o r m p d f$ (i, 300, 100). The successive attack path and likelihood of those attacks to be successful are inputs to the model. To limit ourselves to a simple case, we assume that i) there is only one successive attack spawned from each successful external attack ii) the successive attack targets the lower value neighboring system (with systems sorted from highest to lowest value), and the lowest value system attacks the highest value system.

In terms of the probability of successfully attacking another system, again there are many possibilities. There are two potential cases: i) high value systems have higher chances of successfully attacking another system $( { \phi _ { i } { = } S _ { i } } / { \sum { S _ { j } } }$ label H in Fig. 2) or ii) vice versa $( ( \phi _ { i } { = } S _ { i } ^ { - 1 } /$ $\sum S _ { i } ^ { - 1 }$ ; label L in Fig. 2). For our analysis, we assume the H case for initial risks with externalities.

The reduced security risk levels after security investment are shown in Fig. 3. The figure shows that the risk levels are the lowest without general protection and externalities, which can be attributed by risks generated from externalities that are not accounted for (as seen in Fig. 2). In terms of the use of general protection, they provide a blanket protection effect and result in lower risks for all systems. It is interesting to note that even with higher initial risks due to externalities, low-risk systems are better protected using layered protection. That highlights the fact that when externalities are realized, the “weakest link” problem is addressed by the layered approach.

![](/api/attachments/RFZJV4H8/fulltext/images/ebfe152ae8b05274056a564ef0e1733df46409fd83f3dba9a6f6f9f84c2d75ba.jpg)  
Fig. 3. Risk levels after investment.

![](/api/attachments/RFZJV4H8/fulltext/images/9bb06548d903d4716f316868c04ff29de7cf70c6f0a29d4df784803acddd5df7.jpg)  
Fig. 4. Risk reduced (%) after investment.

When we normalize the protection benefits brought by security investment (Fig. 4), improvements due to protection are spread more evenly when network externalities are not taken into consideration (Fig. 4). This is supported by a more uniform investment pattern across the systems (Fig. 5). Essentially, there is a lower percentage of improvements over high-risk systems, but a higher percentage of improvements over low-risk systems. When the general protection measure is introduced, the resources of the system-specific protection become less evenly distributed. After the general protection investment has been implemented, the remaining resources (minus the general protection investment), are then allocated from high-risk to lowrisk systems. The results indicate that the solution to eliminating the “weakest link” may not lie with more evenly spread system-specific investments, but rather with the consideration of the general protection measure.

![](/api/attachments/RFZJV4H8/fulltext/images/fe0a42a6a875d1a748bd38bff648c5789d5cce1be98436b5b6a95ac6379ce79e.jpg)  
Fig. 5. Investment levels for system .i.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Cluster count algorithm

Set q=0, f=0
Repeat until f=1 or  $q\hat{m}\geq m$ 
    Solve  $x^{*}$ ,  $y^{*}$ ,  $\mu^{*}$ ,  $\gamma^{*}$  using  $m=\hat{m}$  on Eq. (20).  $y_{i}=y^{*}$  for  $i\leq q\hat{m}$ ,
0 otherwise
Resort  $d_{i}(\theta e^{-\beta yi}-\theta+1)$  before solving for Eq. (21)
If  $L^{*}(q)&lt;L^{*}(q-1)$ $q=q+1$ 
Else f=1
</div>

## 3.3.2. Two-tier cluster protection

The discussion in the previous sections assumes the general protection measure protects all systems. In practice, the general protection measure may be limited by the number of systems it can cover. Moreover, it is likely that the effectiveness of the measure will decrease with the number of systems covered. In this section, we assume the number of systems covered to be an exogenous number $\scriptstyle { \hat { m } } = 1 0$

The procedure for finding the solution is similar to the two-tier protection problem, except that now an iterative process is required to find the optimal number of cluster protection (.q). Table 3 shows the algorithm used to determine .q and it is found that the optimal solution yields 12 clusters of general protection $( q = 1 2 )$ .

We compare the implications of the cluster general protection case to when there is and there is no general protection. We have seen that the presence of general protection measures will shift some of the resources from protecting high-risk systems to low-risk systems. When the general measure has limitations, we observe the same trend. However, now that the general protection measure has become more expensive, the shift has become more significant and not all low-risk systems will be protected, as shown in Figs. 6 and 7, thus leaving less protection for high-risk systems.

Here, we demonstrate that a restricted form of general protection again protects the low-risk systems in order to account for the “weakest link”, however, because the protection becomes more expensive, the lowest risks systems may not be protected.

## 3.3.3. Uncertainty

One of the major difficulties in conducting risk management is accurately estimating the breach probability and loss values. This is due to the fact that there are a great deal of uncertainties surrounding the factors that influence security risks. Even when risk can be estimated accurately, the risk management process can be exhaustive in time and effort. In facing uncertainty, many organizations follow the practices of other organizations or baseline recommendations (such as NIST's recommendation [31]). These two approaches are especially effective when there is no concrete information on security profiles and protection effectiveness.

![](/api/attachments/RFZJV4H8/fulltext/images/272ce0d95b96b0a3b4842f1651505c3d722aff214bfef0621a3cbc40c8d0b2e3.jpg)  
Fig. 6. Investment levels for system .i.

In this section, we compare the decision to use baseline cases to the security resource allocation model described in previous sections.<sup>3</sup> In the baseline case, all systems receive equal protection. In the other case, the investment decisions are made using our two-layer model with predicted values. The actual risks scenario can turn out to be either the best or the worse case scenario due to errors in estimating risks. For the best case scenario, the actual risk is lower than expected. On the other hand, the worse case scenario occurs when the actual risk is higher than expected. If the risks are as expected, we call it the predicted case. The risk profiles for the three cases are presented in Fig. 8. We isolated the uncertainty factor to breach probability on successive attack $( \phi _ { i j } )$ . In the best case, . $\phi _ { i j }$ are 100% better than the predicted case, while in the worse case scenario, $\phi _ { i j }$ are 100% worse than the predicted case.

The decisions are made either using the predicted values or the baseline values. When the actual outcome is the worse case scenario, Fig. 9 presents the system risks after investment levels for the respective decision models. The optimal values (based on the actual risk profiles) are also shown for comparison. The figure shows that the majority of the higher risk systems are under-protected using the two approaches, with baseline case under-investing more for highest risks systems. Using the predicted value is likely to yield better results because high-risk systems are protected to a greater degree.

![](/api/attachments/RFZJV4H8/fulltext/images/b7430359e57f3782f2b16ea0bd8d704297595d4e97213342ed68986c8da12687.jpg)  
Fig. 7. Risk reduced (%) after investment.

When the actual scenario turns out to be the best case scenario, some of the medium-risk systems are incorrectly assessed as high-risk systems (Fig. 8). This is due to our assumption that a system tends to attack another system that has comparable risks; therefore, the prediction errors turn out to be larger for higher risk systems. The outcome of over-estimating the risks, as shown in Fig. 10, is that the resource allocation decision is distorted and results in some relevant systems being protected more and the less relevant systems are protected less using the predicted values. When the baseline case values are used, the high- and medium-risk systems are underprotected and low-risk systems over-protected. Because the difference between baseline investment levels and optimal investment levels is less significant compared to using the predicted values, the aggregated system risks using the baseline case values in the best case scenario yields better results; see Table 4.

![](/api/attachments/RFZJV4H8/fulltext/images/900736592cadf0f397348e403a2944dae668bce31de12f5d24129ffc7374ae84.jpg)  
Fig. 8. Initial risk levels for system .i.

![](/api/attachments/RFZJV4H8/fulltext/images/4b2cc5a7b0746a1dd8f0eca6046272a6aaf92e3bf25f4e0424fd4b545f8c0588.jpg)  
Fig. 9. Worse case scenario: risk levels after investments for system.i.

This example shows that the robustness of the risk analysis process is critical. We have shown that an example of it is better to under-estimate risks than overestimate risks for high-risk systems. The main reason is the protection priorities are not distorted when risks are under-estimated. Therefore, sometimes a lack of confidence in risk assessment, especially in terms of relative system risks, warrants a simpler uniform protection of systems. This also points to a greater emphasis on using the general protection measure because this practice reduces the errors made in relative system-specific investments, as less resources are devoted to system-specific protection.

![](/api/attachments/RFZJV4H8/fulltext/images/4dcdadbc68f75f7bbf0c7b0a226e334a39d742de15aa68414db7279ccaaeb2eb.jpg)  
Fig. 10. Best case scenario: risk levels after investments for system .i.

Table 4  
Aggregate organizational risk levels after investments

<table><tr><td></td><td>Baseline values</td><td>Predicted values</td><td>Optimal values</td></tr><tr><td>Best case scenario</td><td>3042.4</td><td>3048.7</td><td>3039.5</td></tr><tr><td>Worse case scenario</td><td>4786.8</td><td>4701.9</td><td>3765.8</td></tr></table>

In this subsection, numerical examples are used to show different managerial insights of our models. Risk management guides typically do not consider the issues of network externalities and layered protection in details. We see that the consideration of network externalities increase an organization's estimation of risks. The use of general protection results in more equal distribution of security protection. In return, high-risk systems receive less allocation of resources. Furthermore, we discuss how to allocate resources to general protection measure when it only protects a limited number of systems. In this case, it gives more even protection to the systems than the no general protection case, but some low-risk systems are not protected due to lack of resources. Lastly, when the actual risks are less than predicted, improper estimation of system risks could result in worse outcome than using the baseline approach. This shows how risk assessment plays a critical role in risk mitigation.

## 4. Conclusion and limitations

Computer security risk management is a critical process in protecting the information assets of an organization. The main contributions of the risk management exercise are the determination of security risks of systems and the development of a protection strategy to reduce the risks. In this paper we make a distinction on protection types in the risk management procedure. We often heard that information security is an embodiment including computer security and network security. From our analysis, the distinction of system protection and general protection clearly makes a difference in how security risks are reduced. Using the layered protection approach is shown to reduce security risks more. This result indicates that the risk management paradigm should further classify different types of protection so that more effective strategies can be formulated.

We also study the impact of considering network externalities in risk assessment. We often realized breaches occur on a single system but have no way of knowing how much information were compromised. This is because systems are connected so attacks may propagate. The consideration of network externalities would then changes the protection mind set. ITsecurity risk management should include more discussions about the externalities effect. For example, one could include specifications on network architecture, access control models used, and so on. Those discussions, even in general settings, would provide closer estimates to the actual risks.

It is also important to point out that risk management is not a magical process; it requires accurate security assessment. While it falls outside the scope of this paper, we would like to stress that the estimation of security risks has known to be a difficult process confronted with many practical uncertainties. We have illustrated that the use of baseline approaches may generate better results when the system risks cannot be ranked properly. The research in information security is inherently difficult due to the sensitivity nature of the subject, which provides obstacles to empirically evaluate the issues. In that respect, our models provide a good qualitative overview and summary to the topic. As firms continue to have better grasps and confidence about their estimations of security risks, the value of our model becomes more apparent.

Although it closely resembles reality, the stylized models provided here require further refinements for practical implementations. One limitation is that our simulations are not conducted with real data. However, getting real data in the information security area is generally difficult. Other extensions to this research may include designing practical solutions in risk allocation, in which a more diverse range of protection measures and complex network settings have to be considered. In addition, issues related to threat and vulnerability analysis are not formally modelled here. One could incorporate attacker behaviors into the model, with complete or incomplete information, to account for the threat elements in the risk management problem. The discussion of vulnerabilities would likely involve IT systems vendors, as many of today's vulnerabilities are tied to software vulnerabilities. As a result, it is necessary to include the IT systems vendors into the model to address the issues.

## Appendix A. Single-tier Protection

Now we show that this solution satisfies KKT.

For condition (10): For $1 \leq i \leq m \colon$ Since $\mu _ { i } { = } 0 , \left( i \right)$ reduces to $- c _ { i } \alpha e ^ { - \alpha x i } + \lambda = 0$ , which is solved by $\begin{array} { r } { x _ { i } = \frac { 1 } { \alpha } ( \ln \alpha c _ { i } - \ln \lambda ) } \end{array}$

For. ${ \overline { { m } } } < i \leq m ;$ : Since. $x _ { i } { = } 0 , ( i )$ reduces $\tan \alpha c _ { i } + \lambda - \mu _ { i } =$ 0, which is the definition of $\mu _ { i } .$

For condition (11): By Eq. $\begin{array} { r } { ( 1 4 ) , \sum _ { i = 1 } ^ { m } x _ { i } = \sum _ { i = 1 } ^ { \overline { { m } } } x _ { i } = } \end{array}$ $\begin{array} { r } { \sum _ { i = 1 } ^ { \overline { m } } \bigl ( \frac { 1 } { \alpha } \left( \ln { \alpha c _ { i } - \ln \lambda } \right) \bigr ) = \frac { 1 } { \alpha } \left( \sum _ { i = 1 } ^ { \overline { m } } \ln { \alpha c _ { i } - \mathrm { \Large ~ \dot ~ m } } \right( \frac { 1 } { \overline { m } } \sum _ { i = 1 } ^ { \overline { m } } \mathrm { l i } \mathrm { \AA } \alpha c _ { i } - } \end{array}$ $\alpha Q ) ) = Q$

Since. $x _ { \overline { { m } } } \leq x _ { i }$ for. $i \geq m ,$ , we show $x _ { \mathit { m } } = 0$ to conclude $x _ { i } \geq 0$ for $i \leq m$ . By the $ { \mathrm { ^ 6 6 } } _ { 1 1 }  { \mathrm { ^ 5 } }$ condition in the algorithm $\begin{array} { r } { \frac 1 \times \ln \lambda ( \bar { m } ) < \frac { 1 } { \alpha } \ln \alpha c _ { \bar { m } } \Rightarrow x _ { i } = \frac { 1 } { \alpha } \ln \alpha c _ { m } - \frac { 1 } { \alpha } \ln \lambda > 0 } \end{array}$ . For $i >$ ${ \bar { m } } ,$ by our choice $x _ { i } = 0$

For condition (12): For $1 \leq i \leq \bar { m } , \mu _ { i } = 0$ by our choice. For $\overline { { m } } \leq i \leq m , \mu _ { i } = \lambda - \alpha c _ { i }$ . Since $\mu _ { i } \geq \mu _ { \overline { { m } } + 1 }$ for every $i > m$ , we show $\mu _ { \overline { { { m } } } + 1 } \geq 0$ to conclude $\mu _ { i } \geq 0$ for $i >$ $\overline { { m } } .$

By the $ { \mathrm { ^ 6 _ { i } } }  { \mathrm { f } } ^ { \flat }$ condition in the algorithm $\scriptstyle { \frac { 1 } { \alpha } } \ln \lambda$ $( \bar { m } + 1 ) { \geq } \frac { 1 } { \alpha } \ln { \alpha } c _ { \overline { { m } } + 1 }$

$$
\lambda (\bar {m} + 1) \leq \lambda (\bar {m})
$$

$$
\frac {1}{\alpha} \ln \lambda (\bar {m}) \geq \frac {1}{\alpha} \ln \alpha c _ {\bar {m} + 1} \Rightarrow \mu_ {\bar {m} + 1} = \lambda - \alpha c _ {\bar {m} + 1} \geq 0
$$

For condition (13): This condition is trivially satisfied by the definition of $x _ { i }$ and $\mu _ { i }$

## Appendix B. Two-tier Protection

Now we show that this solution satisfies KKT.

For condition (15): For $1 \leq i \leq m \colon$ Since $\mu _ { i } { = } 0$ , Eq. (15) reduces $\mathrm { t o } - \alpha d _ { i } ( \theta e ^ { - \beta \nu } - \theta + 1 ) e ^ { - \alpha x i } + \lambda { = } 0$ , which is solved by $\begin{array} { r } { x _ { i } = \frac { 1 } { \alpha } ( \ln \alpha d _ { i } ( \theta e ^ { - \beta y } - \theta + 1 ) - \ln \lambda ) } \end{array}$

For $\overline { { m } } < i \leq m$ : Since $x _ { i } { = } 0 ,$ , Eq. (15) reduces $\mathrm { t o } - d _ { i }$ $\theta \alpha e ^ { - \beta y } - d _ { i } ( 1 - \theta ) \alpha + \lambda - \mu _ { i } = 0$ , which is the definition of $\mu _ { i }$

For condition (16): For $1 \leq i \leq m \colon$ , Eq. (16) reduces $\begin{array} { r } { \mathfrak { i } \mathfrak { o } \ - \sum _ { i = 1 } ^ { \overline { { m } } } d _ { i } \theta \beta e ^ { - \alpha x _ { i } - \beta y } + \lambda = 0 } \end{array}$ , which is solved by $\begin{array} { r } { y = \frac { 1 } { \beta } \ln \frac { \theta ( \overline { { m } } \beta - \alpha ) } { \alpha ( 1 - \theta ) } . } \end{array}$

For $\textstyle { \overline { { m } } } < i \leq m ;$ Since $x _ { _ i } { = } 0$ , Eq. (16) reduces to $\textstyle - \sum _ { i = 1 } ^ { \overline { { m } } } d _ { i } \theta \beta e ^ { - \beta y } + \lambda$ , which is the definition of .λ For condition (17): By Eq. $\begin{array} { r } { ( 2 1 ) , \sum _ { i = 1 } ^ { m } x _ { i } = \sum _ { i = 1 } ^ { \overline { { m } } } x _ { i } = } \end{array}$ $\textstyle \sum _ { i = 1 } ^ { \overline { { m } } } { \frac { 1 } { \alpha } }$ lnad<sub>i</sub> $( \theta e ^ { - \beta y } - \theta + 1 ) - \mathrm { l n } \lambda ) { \mathrm { ~ \bar { ~ } { ~ = ~ } ~ } } \textstyle { \frac { 1 } { \gamma } } \left( \sum _ { i = 1 } ^ { \overrightarrow { m } } \mathrm { l n } \alpha d _ { i } \right.$ $\begin{array} { r } { \overline { { ( \theta } } \dot { e } ^ { - \widehat { \beta } y } - \theta + 1 ) - \overline { { m } } \left( \frac { 1 } { \overline { { m } } } \sum _ { i = 1 } ^ { \overline { { m } } } \right. } \end{array}$ lnad $( \theta e ^ { - \beta \hat { y } } - \theta + 1 ) - \alpha$ $\left( Q - y ) \right) = Q - y$

Since $x _ { m } \leq x _ { i }$ for $i \geq m ,$ , we show $x _ { \overline { { { m } } } } \geq 0$ to conclude $x _ { i } \geq 0$ for $i \leq m$ . By the $\mathrm { ^ { 6 6 } _ { 1 1 } ^ { 4 9 } }$ condition in the $\mathrm { { a l g o - } }$ rithm $\begin{array} { r } { \frac { 1 } { \alpha } \ln \lambda ( \overline { { m } } ) < \frac { \mathrm { i } } { \alpha } \ln \alpha d _ { \overline { { m } } } ( \theta e ^ { - \beta y } - \theta + 1 ) \Rightarrow x _ { i } = \frac { \mathrm { i } } { \alpha } ( \ln \dot { \alpha } d _ { m } } \end{array}$ $( \theta e ^ { - \beta y } - \bar { \theta } + 1 ) - \ln \lambda ) ^ { \circ } > 0$

For $i > m ,$ by our choice $x _ { i } = 0$

For condition (18): For $1 \leq i \leq \overline { { m } } , \mu _ { i } = 0$ by our choice.

For $\overline { { m } } \leq i \leq m , \mu _ { i } = \lambda - \alpha d _ { i } \left( \theta e ^ { - \beta \nu } - \theta + 1 \right)$ . Since $\mu _ { i } \geq$ $\mu _ { \overline { { { m } } } + 1 }$ for every $i > m ,$ we show $\mu _ { \overline { { { m } } } + 1 } \geq 0$ to conclude. $\mu _ { i } { \geq } 0$ for $\mathrm { i } > \overline { { m } } .$

By the $\mathrm { ^ { 6 6 } i f } \ ^ { \mathrm { , s } }$ condition in the algorithm ${ \frac { 1 } { \alpha } } \ln \lambda ( { \overline { { m } } } +$ $\begin{array} { r } { 1 ) { \geq } \Big ( \frac { 1 } { \alpha } \ln \alpha d _ { \overline { { m } } + 1 } ( \theta e ^ { - \beta y } - \theta + 1 ) \Big ) } \end{array}$

Combining with $\lambda ( \bar { m } + 1 ) \quad \lambda ( \bar { m } )$ , we obtain, $\begin{array} { r } { \frac { 1 } { x } \ln \lambda ( \overline { { m } } ) { \geq } \frac { 1 } { x } \ln { \alpha } d _ { \overline { { m } } } + 1 ( \theta e ^ { - \beta y } - \theta + 1 ) { \Rightarrow } \mu _ { \overline { { m } } + 1 } = } \end{array}$ $\ddot { \lambda } { - } \alpha d _ { \overline { { { m } } } { + } 1 } ~ ( \ddot { \theta } e ^ { - \beta y } { - } \theta + 1 ) { \geq } 0$

For condition (19): This condition is trivially satisfied by the definition of $x _ { i }$ and $\mu _ { i } ; \boldsymbol { y }$ and . $\gamma$ .

## References

[1] M. Alavi, I.R. Weiss, Managing the risks associated with enduser computing, Journal of Management Information Systems 2 (3) (1985–1986) 5–20.

[2] C. Alberts, A. Dorofee, Managing information security risks: the OCTAVE approach, Pearson Education, Inc., Upper Saddle River, New Jersey, 2002.

[3] J. Anderson, R. Narasimhan, Assessing project implementation risk: a methodological approach, Management Science 25 (6) (1979) 512–521.

[4] K.P. Badenhorst, J.H.P. Eloff, The effect of intrusion detection management methods on the return on investment, Computers & Security 13 (5) (1994) 411–435.

[5] R.L. Baskerville, J. Stage, Controlling prototype development through risk analysis, MIS Quarterly 20 (4) (1996) 481–501.

[6] A. Briney, 2001 industry survey, Information Security Magazine, 2001, pp. 34–46.

[7] H. Cavusoglu, S. Raghunathan, Configuration of detection software: a comparison of decision and game theory approaches, Decision Analysis 1 (3) (2004) 131–148.

[8] H. Cavusoglu, B. Mishra, S. Raghunathan, Optimal design of information technology security architecture, Proceedings of the Twenty-Third International Conference on Information Systems, Barcelona, Spain, 2002, pp. 749–756.

[9] W.G. de Ru, J.H.P. Eloff, Risk analysis modelling with the use of fuzzy logic, Computers & Security 15 (3) (1996) 239–248.

[10] Ernst, Young, Global information security survey 2003, Ernst & Young LLP, White Paper, 2003.

[11] J.E. Gaffney Jr., J.W. Ulvila, A decision analysis method for evaluating computer intrusion detection systems, Decision Analysis 1 (1) (2004) 39–54.

[12] L.A. Gordon, M.P. Loeb, The economics of information security investment, ACM Transactions on Information and System Security 5 (4) (2002) 438–457.

[13] S.B. Guarro, Principles and procedures of the lram approach to information systems risk analysis and management, Computer & Security 6 (6) (1987) 493–504.

[14] M. Gupta, J. Rees, A. Chaturvedi, J. Chi, Matching information security vulnerabilities to organizational security profiles: a genetic algorithm approach, Decision Support Systems 41 (3) (2006) 592–603.

[15] J.T. Hamill, R.F. Deckro, J.M. Kloeber Jr., Evaluating information assurance strategies, Decision Sopport Systems, 39 (3) (2005) 463–484.

[16] M. Higgins, Symantec Internet security threat report: attack trends for Q3 and Q4 2002, Symantec Corporation, 2003 February.

[17] S. Jha, O. Sheyner, J. Wing, Two formal analyses of attack graphs, Computer Security Foundations Workshops, Cape Breton, Nova Scotia, Canada, 2002, pp. 49–63.

[18] K.D. Loch, H.H. Carr, M.E. Warkentin, Threats to information systems: today's reality, yesterday's understanding, MIS Quarterly 16 (2) (1992) 173–186.

[19] K. Lyytinen, L. Mathiassen, J. Ropponen, Attention shaping and software risk — a categorical analysis of four classical risk management approaches, Information Systems Research 9 (3) (1998) 233–255.

[20] F.W. McFarlan, Portfolio approach to information systems, Harvard Business Review 59 (5) (1981) 142–150.

[21] S.D. Moitra, S.L. Konda, The survivability of network systems: an empirical analysis, Carnegie Mellon University, 2000 SEI/ CERT Report CMU/SEI-2000-TR-021.

[22] E.W.T. Ngai, F.K.T. Wat, Dominance approach to risk analysis of computer systems, Decision Support Systems 37 (4) (2004) 485–500.

[23] NIST, An introduction to computer security: the NIST handbook, National Institute of Standards and Technology (NIST), Technology Administration, U.S. Department of Commerce, Specia Publication 800-12, 1995.

[24] R. Ortalo, Y. Deswarte, M. Kaaniche, Experimenting with quantitative evaluation tools for monitoring operational security, IEEE Transactions on Software Engineering 25 (5) (1999) 633–650.

[25] R.R. Panko, Corporate computer and network security, Pearson Education, Inc., Upper Saddle River, New Jersey, 2004.

[26] G.V. Post, J.D. Diltz, Dominance approach to risk analysis of computer systems, MIS Quarterly 10 (4) (1986) 363–375.

[27] PriceWaterhouseCoopers, Information security breaches survey 2004, Department of Trade and Industry (DTI), United Kingdom, 2004 Technical Report.

[28] R. Richardson, 2003 CSI/FBI computer crime and security survey, Computer Security Journal (2003) Tech. Rep.

[29] T. Stein, Security gets top-level attention, Optimize, 23 September, 2003.

[30] G. Stoneburner, A. Goguen, A. Feringa, Risk management guide for information technology systems, National Institute of Standards and Technology (NIST), Technology Administration, U.S. Department of Commerce, Special Publication 800-30, 2002.

[31] G. Stoneburner, C. Hayden, A. Feringa, Engineering principles for information technology security (a baseline for achieving security), revision a, National Institute of Standards and Technology (NIST), Technology Administration, U.S. Department of Commerce, Special Publication 800-27, 2004.

[32] D.W. Straub, Effective is security: an empirical study, Information Systems Research 1 (3) (1990) 255–276.

[33] D.W. Straub, R.J. Welke, Coping with systems risk: security planning models for management decision-making, MIS Quarterly 22 (4) (1998) 441–469.

[34] G.B. Tanna, M. Gupta, H.R. Rao, S. Upadhyaya, Information assurance metric development framework for electronic bill presentment and payment systems using transaction and workflow analysis, Decision Support Systems 41 (1) (2005) 242–261.

[35] M. Thurman, Stepping up to Sarbanes-Oxley, Computer World, http://www.computerworld.com/securitytopics/security/story/ 0,10 801,89306,00.html. 2004.

[36] M.E. Whitman, H.J. Mattord, Management of information security, Course Technology, Thompson, Boston, Massachusetts, 2004.

Wei T. Yue is an assistant professor of management information systems at the University of Texas at Dallas. He received his Ph.D. in management information systems from Purdue University. He is a member of Informs and AIS. His research interests include information security, systems configuration and maintanance, and data mining.

Metin Çakanyıldırım is currently an associate professor at the School of Management at the University of Texas at Dallas. He received his B.S. in Industrial Engineering from Bilkent University, Turkey, his M.S. in Management Science from University of Waterloo, Canada and his Ph.D. in Operations Research from Cornell University. He is a member of Informs, POMS and IIE. His research interests include inventory and capacity management, risk management and information security.

Young U. Ryu received his Ph.D. in management science and information systems from the University of Texas, Austin, in 1992. Since 1992, he has been affiliated with the Department of Information Systems and Operations Management, School of Management, University of Texas, Dallas, where he is currently Associate Professor. His main interests of study include logic modeling, data mining, database, and information security.

Dr. Dengpan Liu is an assistant professor of management information systems at the University of Alabama in Huntsville. He received his Ph.D. in MIS from the University of Texas at Dallas in August, 2006. He also has an M.S. in computer science from UTD and a B.S. in material science and engineering from the University of Science and Technology of China. His main research interests include information security, software development, and E-commerce.
