---
otero_id: 11666
otero_key: "WJFFCXU5"
title: "Optimal information security investment in a Healthcare Information Exchange: An economic analysis"
authors: "C. Derrick Huang; Ravi S. Behara; Jahyun Goo"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal information security investment in a Healthcare Information Exchange: An economic analysis

C. Derrick Huang ⁎, Ravi S. Behara, Jahyun Goo

Department of Information Technology & Operations Management, College of Business, Florida Atlantic University, Boca Raton, FL 33431, United States

## a r t i c l e i n f o

Article history: Received 6 March 2013 Received in revised form 11 September 2013 Accepted 25 October 2013 Available online 8 November 2013

Keywords: Healthcare Information Exchange Healthcare information technology Information security Optimal investment Scale free network

## a b s t r a c t

The complexity of the problem, the increasing security breaches, and the regulatory and <sup>fi</sup>nancial consequences of breached patient data highlight the fact that security of electronic patient information in Healthcare Information Exchanges (HIEs) is an organizational imperative and a research priority. This study applies classical economic decision analysis techniques and models the HIE based on its network characteristics to offer key insights into the issue of determining the optimal level of information security investment. We <sup>fi</sup>nd that for an organization in a HIE, only security events with the potential loss reaching some critical value are worth protecting, and organizations would only spend a fraction of the intrinsic security risk on protection measures. Even when business bene<sup>fi</sup>t from security investment exists, organizations in a HIE tend to invest based on risk reduction alone. The implications of such decisions made at the node level and the resulting built-in moral hazard at the HIE level is discussed.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The Health Information Technology for Economic and Clinical Health Act (HITECH Act), enacted as part of the American Recovery and Reinvestment Act (ARRA) of 2009, unleashed a major IT overhaul of the entire healthcare sector in the United States. Along with the promised bene<sup>fi</sup>ts, however, came the challenge of safeguarding patient information in the digital world [42]: In 2010 and 2011, based on the Department of Health and Human Services (HHS) mandated public noti<sup>fi</sup>cation of breaches involving 500 or more patient records, more than 16 million individuals have been affected by healthcare data breach [80]. In a benchmark study on patient privacy and data security [59], 28% of the respondents have no staff dedicated to managing data protection, while 35% have fewer than two such dedicated staff. It was estimated that data breaches of patient information cost healthcare organizations nearly \$6 billion annually, and that many breaches go undetected [59].

Healthcare organizations are just beginning to appreciate the scale and impact of the information security problem. Decision makers are faced with the multitude of technical and economic issues involved in securing their data and systems. This is further compounded by the fact that there are many health care providers and organizations, including some small, unsophisticated players, involved that handle, share, and coordinate care [42] via a Health Information Exchange (HIE), the electronic network for sharing health-related information among organizations according to nationally or regionally recognized standards. The complexity of the problem, the increasing security breaches, and the regulatory and <sup>fi</sup>nancial consequences of breached patient data, taken together, highlight the fact that security of electronic patient information in HIEs is an organizational imperative and a research priority [9]. Although recent research has shed light on the understanding of security risks in such a healthcare environment, it is limited when it comes to informing the responses by member organizations in a HIE to these risks. This paper represents an effort to address this research gap by examining a key aspect of the management of information security by an organization in a HIE, namely the decision on how much to invest to defend itself against such adversarial events, given the security risks that it faces.

Given that no organization can be completely secure without unlimited budget, it is important for an organization to know what the “right amount” of investment is, before it attempts to engage in defensive mechanisms. In this study, we address the question of optimal level of information security investment by an organization in a HIE, given the security threat it faces and the network environment it is in. We apply classical economic analysis to examine the interaction between the organizational investment decisions and the security risks, modeling the HIE based on its network characteristics with a priori network principles. Further, in addition to the common approach of treating security measures as risk-reduction mechanism, we also consider the business bene<sup>fi</sup>ts that security investment would bring to an organization and how they would affect the investment decision. As such, our study offers insight into how an organization in a HIE could manage its investment in information security based on a variety of threat environments and systems con<sup>fi</sup>gurations as well as the impact of individual investment decision on the HIE as a whole.

The remainder of this paper is organized as follows. The next Section 2 provides research background on HIE and its information security characteristics from existing literature. Next, a model is constructed to study information system security for an organization in a HIE network. We then use the model to derive the optimal investment based on risk reduction as well as business bene<sup>fi</sup>ts brought on by information security measures. Finally, we offer managerial insights and implications for future research based on our <sup>fi</sup>ndings.

## 2. Research background

## 2.1. Health Information Exchange

The term Health Information Exchange, or HIE, has emerged as the common description for systems that facilitate sharing of an individual's personal health records among healthcare service providers. Such a timely sharing of information is considered to be an important contributor to the improved quality and safety of care, while reducing delivery costs. It is estimated that a fully standardized HIE at the national level could yield a net bene<sup>fi</sup>t of over \$70 billion a year [70].

In the U.S., HIE depends on local and regional organizations that bring together stakeholders with healthcare data and set up joint infrastructure. Speci<sup>fi</sup>cally, the following network terms have been de<sup>fi</sup>ned by the National Alliance of Health Information Technology for the U.S. Federal Government [54]:

• Health Information Exchange (HIE): The electronic movement of health-related information among organizations according to nationally recognized standards.

• Health Information Organization (HIO): An organization that oversees and governs the exchange of health-related information among organizations according to nationally recognized standards.

• Regional Health Information Organization (RHIO): A health information organization that brings together health care stakeholders within a de<sup>fi</sup>ned geographic area and governs health information exchange among them for the purpose of improving health and care in that community.

Although HIE started early, the progress has been slow. A 2009 survey, for instance, found that most RHIOs focused only on exchanging test results as opposed to a comprehensive clinical data and suffered a fairly high failure rate of about 25% over the course of 18 months [2]. Along with costs, leadership, and interoperability, security and privacy concern is cited as a major barrier to the growth of HIE [15,26]. HIE participants have expressed discomfort with issues related to privacy, security, data ownership, data control, and liability [1]. Health Insurance Portability and Accountability Act (HIPAA) Privacy and Security Rules that have been in force to protect individually identi<sup>fi</sup>able health information have been adapted to individual electronic health records (EHR) at the provider's level, but HIEs poses new issues and involves organizations that were not contemplated at the time the rules were developed. HITECH Act requires HIEs to be subject to the breach noti<sup>fi</sup>cation rule as a business associate. This, along with other legal and contractual obligations, provides incentives to the organizations in a HIE to prevent and manage breach of their data and information systems [3]. However, with the ownership and the responsibility of HIE security unclear, further analysis and study of the security investment by organizations in a HIE are necessary.

## 2.2. Information security investment

For any organization, questions regarding information security investment can be summarized in three key issues: 1) the optimal amount of information security investment, 2) in what measures to invest, and 3) how to make the investment effective. Several research streams attempt to address these three issues independently.

The <sup>fi</sup>rst question of optimal level of information security investment is often addressed via the traditional decision analysis to compare the risk and return of investments. This approach, though widely adopted for evaluating IT investments, is complicated by the fact that the “return” of security investment does not usually come from increased revenues or decreased costs like other IT investments do, but from managing and reducing the security risks that an organization is facing [7,76]. Such risk analysis can be based on the measurement of security risk = (likelihood of loss event) ∗ (cost of loss event) [63] or more complex variations such as the value-at-risk approach [50,73]. Based on this formulation of risk, Gordon and Loeb [28] in their seminal paper analyze the economics of security investment for a risk-neutral organization by comparing the cost of the investment and the potential loss caused by possible security breaches. They <sup>fi</sup>nd that the optimal security investment would be far less than (with a theoretical maximum of less than 40% of) the potential loss if a security breach does happen, and that the optimal security investment does not necessarily increase with system vulnerability. In extending the Gordon and Loeb model, Huang et al. [38] adopt the expected utility theory to study the behavior of a risk-averse decision maker and <sup>fi</sup>nd that there exists a minimum potential loss for non-zero optimal information security investment; above that minimum, optimal investment increases with potential loss. In addition, contrary to the risk-neutral case, a risk-averse decision maker may continue to invest in information security until the spending is close to (but never exceeds) the potential loss.

After the amount of investment is determined (by optimization, budget, or other constraints), an organization needs to decide what security measures to invest in. Often, selection of the right investments is aided by traditional management tools such as cost-bene<sup>fi</sup>t analysis [30] and <sup>fi</sup>nancial analyses based on such measures as return on investment (ROI), net present value (NPV), and internal rate of return (IRR) [14,29,35,60,67]. Studies have proposed other decision analysis methodologies for selecting the right security investments. For instance, analytic hierarchical process (AHP) employs pair-wise comparisons among different security technologies to determine the priority of implementation [13]. Arora et al. [10] propose to value security investments by associating bypass rate with each of the security technologies adopted at an organization. And Kumar et al. [46] propose a model to use NPV generated by each countermeasure to evaluate an information security portfolio. Alternatively, the issue of selecting and prioritizing security technologies can be treated as optimizing the allocation of the limited security investment. Taking such an approach, Viduto et al. [69] propose a risk assessment and optimization model for the selection of security countermeasures to minimize <sup>fi</sup>nancial costs and risks. Sawik [62] formulates the problem of selection of countermeasures based on their effectiveness, costs, and attack probabilities using a bi-objective trade-off model in a scenario-based analysis. He <sup>fi</sup>nds that the selected portfolio of security measures depends explicitly on preferred con<sup>fi</sup>dence level and cost-risk preference of the decision maker. Huang and Behara [37] propose an analytic model for security investment allocation that considers simultaneous attacks from multiple threat agents with distinct characteristics. Their analysis shows that an organization is better off allocating most or all of the investment to defending against one type of attack when its security budget is small. Further, an organization should focus on technologies against targeted attacks when its information systems are highly connected.

The third aspect of security investment is its performance. In addition to the common operational and procedural issues of technology deployment, an important issue for an effective security investment is its ability to con<sup>fi</sup>gure and adapt to the adversarial conditions that an organization faces, and game theory can be a useful tool for such consideration. From a methodological perspective, game theoretic approach is best suited for modeling the performance of a speci<sup>fi</sup>c security technology with limited rounds (often two or three) of actions and reactions by a limited number of players (often the organization and the attacker). Using this approach to evaluate intrusion detection systems (IDS),

Cavusoglu et al. [16] <sup>fi</sup>nd that investing in such a technology provides a positive return to an organization only when the detection rate is higher than a critical value determined by the utility parameters of the attacker. And when the IDS is con<sup>fi</sup>gurable, the optimal con<sup>fi</sup>guration is to set the detection rate to the ratio of the bene<sup>fi</sup>t and cost parameter of the attacker. They further expand the result to other information security technologies and propose a model for making strategic decision in information security using a game tree approach [16]. Managers can use this methodology, with their own parameters, to examine and evaluate various types of security measures they adopt.

So far, all the studies assume that the return on security investment for the organization is risk reduction alone. In the next section, we examine the possibility of other types of return that security investments might bring.

## 2.3. Business benefits of security investments

The traditional decision analysis in the last section compares the economic cost and bene<sup>fi</sup>t of information security investments, where the bene<sup>fi</sup>ts of such investments mainly come from the reduction of a <sup>fi</sup>rm's security risks. Recent studies, however, indicate that security investment in HIT not only reduces risks, but can also generate direct business bene<sup>fi</sup>ts. The key difference between risk reduction and direct business bene<sup>fi</sup>ts is that, while the former involves the avoidance of adversarial events that may happen in the future, the latter is a (positive) impact on the <sup>fi</sup>nancial results or general business operations of the host organization. Note that in almost all cases, companies invest in information security not because of its business bene<sup>fi</sup>ts alone. Rather, the main focus is likely to be risk reduction; business bene<sup>fi</sup>ts are usually of secondary value, albeit an important one in some cases.

Recent studies by both practitioners and academia shed light on the variety of ways that security investment enhances business values. The research conducted by the IT PCG (IT Policy Compliance Group) [39] shows that, in addition to the avoidance of expenses resulted from successful attacks, the <sup>fi</sup>nancial bene<sup>fi</sup>ts of spending money for information security are directly related to the maintenance of customer retention and market share. The study <sup>fi</sup>nds that <sup>fi</sup>nancial returns for security investments are positive for all size organizations across the industries and at all levels of maturity. Among academic studies, Jennex and Zyngier [40] <sup>fi</sup>nd that security is a key success factor for company's knowledge management process. From the real options perspective, Daneva [22] argues that information security provides the ability to launch value-added services for secure interactions with the suppliers or clients, thus creating growth opportunities for the organization. Further, IT security can enhance con<sup>fi</sup>dence in a <sup>fi</sup>rm's reputation and brand [24], and customers are more willing to buy from companies that can safely protect their data [72]. There are also unintended bene-<sup>fi</sup>ts. For example, there is evidence that a <sup>fi</sup>rm enjoys positive abnormal returns in its stock market value after the announcement of information security investment [18]; and certain measures originally implemented to enhance security may result in cost savings (such as single sign-on, as discussed in [81]).

Perhaps the most concrete and tangible business bene<sup>fi</sup>t of security investment is to play the role of business enabler. In a case study on a group of industrial <sup>fi</sup>rms, [81] <sup>fi</sup>nd that companies often must invest in information security at a certain level to be quali<sup>fi</sup>ed for new business associated with acquiring a new customer; further, to bid for certain projects, companies are subjected to a security audit to see whether their practices are acceptable. In the case of a healthcare organization in a HIE, it must meet information security standards to comply with HIPPA rules [48] in order to qualify for Medicaid and Medicare payments [36]. In both examples, security investments enable the companies to obtain more businesses, resulting direct business bene<sup>fi</sup>ts of higher revenues.

All these studies of information security investment, albeit extensive, have mostly been based on decision making at isolated nodes.

That is, the issue of networking environment that an organization is in is largely ignored. In the next section, we review those studies that examine information security among organizations in a network

## 2.4. Information Security in HIE-Like Environment

When organizations are interconnected as in a HIE, key components of risks—threats, vulnerabilities, potential losses, and so on—are no longer isolated to any individual organization. The threat to any given organization in an interconnected system could very well become threats to other member organizations; one organization's vulnerability can affect others' security; and a breach to one organization's system can result in subsequent losses at multiple organizations. Understanding the nature of how risks cascade is fundamental to the extended-enterprise view of information security. Studies of interconnected information security in the HIE-like environment, though rather limited, can be classi<sup>fi</sup>ed into three key categories: individual <sup>fi</sup>rms' security investments, security information sharing, and risk propagation in an interconnected system.

A <sup>fi</sup>rm's decision on information security investment can be different from individual decision-making when its risks are interconnected with those of other <sup>fi</sup>rms. Kunreuther and Heal [47], using a game-theoretic approach, show that <sup>fi</sup>rms with identical security pro<sup>fi</sup>le in a system of interdependent security would either all invest in equal amount of protection or none at all. Separately, Ogut and Menon [57] <sup>fi</sup>nd that the interdependency of risks reduces the <sup>fi</sup>rms' investment in information security to a level below optimum. However, when <sup>fi</sup>rms face liability in IT security—the breached <sup>fi</sup>rm has to pay others for collateral damages—they tend to over-invest above the optimal level. Consequently, the investment decision reached is almost always less optimal than that where all interconnected <sup>fi</sup>rms plan and optimize their information security investment jointly.

Another key aspect of interconnected systems is whether and when <sup>fi</sup>rms share security information. In general, security information sharing and investments in security technologies act as strategic complements, and incentives for sharing increase with <sup>fi</sup>rm size and level of competition [27]. It is also found that security information sharing can result in a reduction of security investment while leading to an increased level of information security [31]. However, Johnson and Dynes [43] demonstrate that information sharing in extended enterprises can lead to an inadvertent disclosure, amounting to a substantial threat and vulnerability to member <sup>fi</sup>rms. Two inter-organizational knowledge-sharing security models, one based on Lightweight Coordination Calculus [75] and the other an integrated model based on several organizational theories [65], are proposed, and it is shown that, using simulation, breach detection time signi<sup>fi</sup>cantly decreases when a large number of <sup>fi</sup>rms joined the sharing network [65].

Lastly, in an interconnected system, risks can propagate from one node (i.e., a <sup>fi</sup>rm's system) to another. Majority of the studies on risk propagation in an interconnected system adopt some sort of network topology—random networks, lattices, small-world networks, etc.—as well as one or more epidemic models—susceptible-infected-removal (SIR) and susceptible-infected-removal-susceptible (SIRS), for instance [32,33,49,66,77,78]. Keeling and Eames [45] provide an extensive review of these studies. These studies focus on building network epidemic models and examining their mathematical properties using simulation. Real-life applications of such models, however, are generally unavailable.

These studies extend the information security from nodal to network-based settings. It is important to model HIE based on its network characteristics in order to apply economic principles to the optimal level of security investment for its member organizations. In the next section, we attempt to establish such a model for HIE.

## 2.5. Characteristics of HIE-Like Networks

A HIE is a system through which many healthcare organizations share information. From a structural standpoint, it is a network of nodes, and the examination of its network topology is necessary to bridge the gap between nodal security investment (Section 2.2) and security issues in a network (Section 2.4) to study the information security investment by organizations in a HIE.

The simplest and most intuitive model of a network is the random graph, where all nodes connect to one another randomly without any particular order. However, many networks in the real world, although seemingly random, do not have randomly connected nodes [56]. In 1999, physicist Barabási and colleagues discover that, although the majority of the nodes have only limited number of links, a few of the nodes (called “hubs”) in the Worldwide Web have a large number of connections [11]. Such a network topology exhibits two signi<sup>fi</sup>cantly different properties compared to random graphs (see Fig. 1):

• The network “diameter,” de<sup>fi</sup>ned as the average number of connections between any two random nodes in the network, is quite small (for instance, the diameter of the World-Wide Web was calculated to be 19, a remarkably small number considering the fact that the Internet has hundreds of millions of nodes). This is sometimes known as the “small-world” network property [5].

• The connectivity follows a power law in the distribution of nodal connectedness. The probability that a node connects with k other nodes is roughly proportional to k<sup>−γ</sup>, where γ is between 2 and 3 for most networks [5,11]. Such connectivity does not change with the addition of new nodes (hence the name “scale-free network”).

In the ensuing years after Barabási's work, this “scale-free network” topology is found in a wide variety of real-world systems, ranging from the Internet [25,68], telephone graphs [4], and the power grid [74], to the network of citation [61] and collaborations in mathematics [34], to protein interaction [41] and human sexual contacts [52]. Similarly, in a HIE, the majority of the healthcare organizations connect only to their customers or patients and maybe a few other providers, while a few large hospitals, major healthcare insurance providers, and HIOs and/or RHIOs have direct connections to most nodal sites and thus act as hubs. We therefore submit that the network structure of a HIE can be best described by a scale-free network and its properties.

Member organizations of a HIE (and all other networks) often experience opportunistic (i.e., non-targeted, broad-based) attacks [19,23]. Because such attacks on one or more of the nodes get spread to other nodes in a HIE in a way similar to a disease spreading in a community, we can adopt the derivation of the spread of an epidemic event in a scale-free network to describe such attack propagation [20,58]. The rate of epidemic spreading, λ, is determined by $r ,$ the infection rate of a previously uninfected node if it is connected to an infected one, and $\delta ,$ the remediation rate of an infected node:

$$
\lambda = \frac {r}{\delta}.\tag{1}
$$

Let $P _ { k } ( t )$ denote the relative density of infected nodes with k connections—that is the probability that a node with k connections is infected—at time t. The mean <sup>fi</sup>eld rate equation gives [58]

$$
\frac {\partial P _ {k} (t)}{\partial t} = - P _ {k} (t) + \lambda k [ 1 - P _ {k} (t) ] \Theta (\lambda),\tag{2}
$$

where Θ(λ) is the probability that any given connection points to an infected node, which can be given in the lowest order of λ [20]:

$$
\Theta (\lambda) = \frac {e ^ {- \lambda n}}{\lambda n},\tag{3}
$$

where n is the minimum number of nodes available for connection in such a network. Solving for $P _ { k }$ in a steady state (i.e., $\partial P _ { k } ( t ) \Big / _ { \partial t } = 0 )$ , one gets

$$
P _ {k} = \frac {k \lambda \Theta (\lambda)}{1 + k \lambda \Theta (\lambda)}.\tag{4}
$$

Substituting Eq. (3) into Eq. (4) and averaging $P _ { k }$ over k, one gets the average infection probability [58]:

$$
P = c e ^ {- \frac {1}{\lambda n}},\tag{5}
$$

where c is a normalization constant. In other words, Eq. (5) gives the probability for any node in a HIE to be infected (i.e., successfully attacked) amid a security event.

## 3. HIE network model for information security investment

In this study, we follow the commonly adopted model [28,37,38] to examine the investment made by an organization in a HIE to protect against opportunistic (i.e., non-targeted, broad-based) attacks [19,23]. In this scenario, security adversaries generate attacks randomly and op portunistically on the information systems of a HIE; let η denote the probability that the information systems may be under attack. Whether such attacks are successful or not also depends on an information system's vulnerability, which is in turn determined by two internal factors. The system susceptibility, θ, is a direct result of the topology and connectivity of the organization's information systems: The more accessible and connected the systems, the more intrinsically susceptible they are to attacks. To protect against the system connectedness being exploited by threat agents, the organization invests w in security measures. (Table 1 summarizes all notations used in the models of this paper.) Note that for opportunistic attacks, η is the same for all nodes and is thus independent of the system susceptibility θ and the security investment w. The probability of a successful security attack is then a function of the behavior of the attack agents (as described by attack probability η) and the security property of the information systems (determined by the system susceptibility θ and investments in security measures w). In other words, the breach probability φ can be written as the following:

![](/api/attachments/WJFFCXU5/fulltext/images/3c9028b988e32b9b1d7edaf47b8357505d64011b315ea5e1313219c4d26e2477.jpg)  
Fig. 1. Randomly connected network (left) and scale-free network (right). Adapted from [79]

$$
\phi = \phi (\eta , \theta , w).\tag{6}
$$

For simplicity, we assume that θ is normalized such that $\theta \in [ 0 , 1 ] .$ Note that for any given system, the higher the security threat and the more susceptible to attacks, the higher the breach probability; that is, both $\begin{array} { r } { \frac { \partial \phi } { \partial n } \geq 0 } \end{array}$ and $\begin{array} { r } { | \frac { \partial \phi } { \partial \theta } \geq 0 . } \end{array}$ Further, since the effect of the security investment is to reduce the breach probability, we have

$$
\frac {\partial \phi}{\partial w} \leq 0.\tag{7}
$$

We also assume that this reduction is governed by the law of diminishing return, which implies that

$$
\frac {\partial^ {2} \phi}{\partial w ^ {2}} \geq 0.\tag{8}
$$

We further assume that when the <sup>fi</sup>rm does not make any security investment, the breach probability is solely determined by and can be described as a product of the threat and the intrinsic system vulnerability. In other words, $\varphi ( \eta , \theta , 0 ) = \eta \theta .$

Security threats create risks for an organization. A common de<sup>fi</sup>nition of risk is the combination of the likelihood and the consequence of a speci<sup>fi</sup>ed hazard being realized [12,44]. The security risk Ω an organization faces can therefore be written as [63]

$$
\Omega = \varphi S,\tag{9}
$$

where S is the potential economic loss caused by a security breach. Such losses may depend on the type of attacks and their impact on the organization but would be independent of the attack probability, system susceptibility, and security investment. When there is no security investment made, and the security risk the organization faces is

$$
\Omega_ {0} = \eta \theta S.\tag{10}
$$

To protect against the attacks, the organization makes investment w; the effect is a reduction in the breach probability such that the information security risks is reduced by $\Delta \Omega = \eta { \theta } \mathrm { S } - \varphi \mathrm { S } .$ In other words, the net value Π of the security investments would be

$$
\Pi (w) = (\eta \theta - \varphi) S - w.\tag{11}
$$

To further derive Eq. (11), we note that, as discussed in Section 2.4, HIE can be modeled as scale-free networks, and the organization's information systems can be represented as a node in such a network. As such, the effect of security investment w is in the reduction of the infection rate λ in Eq. (1). λ and w satisfy certain boundary conditions. First, without any security investment, the attack would be spread freely to the node in question; in other words, $\lambda = 1$ when $w = 0 .$ . Second, any <sup>fi</sup>nite security investments, no matter how large, would never be able to fully block all attacks; in other words, $\lambda \to 0$ only when w → . Without loss of generality, the relationship between security investment and infection rate can be expressed in the following manner to satisfy the above boundary conditions:

$$
\lambda \equiv \frac {1}{q w + 1},\tag{12}
$$

where $q ,$ normalized to between 0 and 1, is the impact factor of w: The higher the q, the greater the reduction of the infection rate for any given security investment w.

The next set of observations is on the system susceptibility θ. Note that since θ represents the connectivity of the information systems in question, θ would be strictly increasing in n, which represents the extent of connections in such a scale-free network. Further, when $n = 0 ,$ θ = 0. On the other hand, θ → 1 when $n \to \infty ;$ that is, the systems are highly susceptible to the epidemic, or security attacks in our case, when they are completely open. Without loss of generality, the following relationship between θ and n that satis<sup>fi</sup>es all the above conditions is assigned:

$$
\theta \equiv e ^ {- \frac {1}{n}}.\tag{13}
$$

Lastly, note that the level of threat from attacks is not explicitly considered in Eq. (5), which can be accounted for by multiplying Eq. (5) with the attack probability η. With this modi<sup>fi</sup>cation, Eqs. (11) and (12), and adjusting the normalization constant c in Eq. (5) to re<sup>fl</sup>ect the boundary condition $\phi ( \eta , \theta , 0 ) = \eta \theta ,$ one <sup>fi</sup>nds that the breach probability for an attack can be written as:

Summary of variables and functions.

<table><tr><td>Notation</td><td>Name</td><td>Definition</td><td>Key assumptions</td></tr><tr><td> $\theta$ </td><td>System susceptibility</td><td>How susceptible information system is to attacks; normalized to [0,1]</td><td>Intrinsic to information system&#x27;s connectedness, determined by organization&#x27;s requirement in a HIE.Independent of any security properties.</td></tr><tr><td> $\eta$ </td><td>Attack probability</td><td>Likelihood that an information system receives attack;  $\eta \in [0,1]$ </td><td>Exogenous to firm&#x27;s defensive activities.</td></tr><tr><td>w</td><td>Security investment</td><td>Organization&#x27;s investment made to protect against attacks</td><td>Initial security investment has to produce positive benefit.</td></tr><tr><td> $\varphi$ </td><td>Breach probability</td><td>Probability that an attack is successful against organization&#x27;s information system;  $\varphi \in [0,1]$ </td><td></td></tr><tr><td>S</td><td>Potential loss</td><td>Potential economic loss caused by a security breach from attack</td><td>Potential loss is independent of system susceptibility, attack probability, and security investment.</td></tr><tr><td> $\Omega$ </td><td>Security risk</td><td>Product of breach probability and potential loss</td><td> $\Omega_0 = \eta\theta S.$ </td></tr><tr><td>q</td><td>Security investment impact parameter</td><td>Measuring the effectiveness of security investment</td><td></td></tr><tr><td> $\Pi$ </td><td>Total value function</td><td></td><td></td></tr><tr><td>B</td><td>Business benefit function</td><td></td><td></td></tr></table>

$$
\phi = \eta \cdot P = \eta \cdot \left(e ^ {- 1 / _ {n}}\right) ^ {1 / _ {\lambda}} = \eta \theta^ {q w + 1}.\tag{14}
$$

Substituting Eq. (14) into Eq. (11) and rearranging the terms, one gets

$$
\Pi (w) = \eta \theta S \big (1 - \theta^ {q w} \big) - w,\tag{15}
$$

which is the base expression governing the net value of security investment amid targeted attacks.

We note an important boundary condition. Before an organization makes the <sup>fi</sup>rst ever security investment, it has to assume that such investment generates positive value. This has to be true, because otherwise no organizations would be making any information security investment initially. Such boundary condition can be expressed as

$$
\left. \frac {\partial \Pi (w)}{\partial w} \right| _ {w = 0} \geq 0.\tag{16}
$$

Substituting Eq. (14) into Eq. (15) and rearranging the terms, we get

$$
- \theta \ln \theta \geq \frac {1}{\eta q S}.\tag{17}
$$

## 4. Optimal security investment in HIE

The task of optimizing the security investments is to maximize their value by setting the <sup>fi</sup>rst-order partial differentiation of Π in Eq. (11) with respect to w to 0; that is,

$$
\frac {\partial \Pi}{\partial w} = - \frac {\partial \phi}{\partial w} S - 1 = 0,\tag{18}
$$

since both η and θ are independent of w. Note that this operation indeed yields maximum, not minimum, of Π:

$$
\frac {\partial^ {2} \Pi}{\partial w ^ {2}} = - \frac {\partial^ {2} \phi}{\partial w ^ {2}} S \leq 0,\tag{19}
$$

because of $\operatorname { E q . } \left( 8 \right)$ . From Eq. (14),

$$
\frac {\partial \phi}{\partial w} = \eta q (\ln \theta) \theta^ {q w + 1}.\tag{20}
$$

We substitute Eq. (20) into Eq. (18) and get the following:

$$
- 1 - \eta q (\ln \theta) S \theta^ {q w + 1} = 0.\tag{21}
$$

Rearranging terms, we get

$$
\theta^ {q w + 1} = - \frac {1}{\eta q (\ln \theta) S}.\tag{22}
$$

To solve for the optimal investment w\*, we take logarithm of base θ on both sides and rearrange terms:

$$
\begin{array}{l} w * = \frac {1}{q} \left[ \frac {\ln \left((- \eta q (\ln \theta) S) ^ {- 1}\right)}{\ln \theta} - 1 \right] \\ = - \left(\frac {1}{q \ln \theta}\right) \ln (- \eta q S \theta \ln \theta). \end{array}\tag{23}
$$

For w\* in Eq. (23) to be positive, the second logarithm has to be positive, since lnθ is negative. This means that its argument needs to be less than one:

$$
- \eta q S \theta \ln \theta \geq 1.\tag{24}
$$

This is indeed true, as required by the boundary condition in Eq. (17). Rearranging the terms in Eq. (24), we get

$$
S \geq \frac {1}{\eta q \theta (- \ln \theta)} \equiv \underline {{S}}.\tag{25}
$$

We de<sup>fi</sup>ne the right-hand side of Eq. (25) as the “critical security loss” S, which is always positive. Eq. (25) states that S has to be greater than $\underline { { \mathsf { S } } }$ in order for w\* in Eq. (23) to be positive. Hence we have

Lemma 1. For an organization in a HIE, the optimal investment for information security is positive only when the potential loss due to security breaches is larger than the critical security loss S.

Lemma 1 outlines the importance for an organization to examine its security characteristics carefully to avoid “over-investing” in security, because not all security problems are worth protecting. Based on Lemma 1, unless the potential loss from information security reaches the critical security loss S, as de<sup>fi</sup>ned in Eq. (25) the organization in a HIE is better off not investing in security at all. Note that $\underline { { \boldsymbol { S } } }$ is inversely correlated with η and is a decreasing function of θ; that is, the larger the attack probability and/or susceptibility is, the lower the critical security loss is, and the lower the threshold an organization faces in investing in information security.

We further examine the behavior of optimal investment in relationship with the potential loss. Differentiating Eq. (23) with respect to S and collecting terms, we get

$$
\frac {\partial w ^ {*}}{\partial S} = \frac {- 1}{S q \ln \theta} > 0,\tag{26}
$$

and

$$
\frac {\partial^ {2} w ^ {*}}{\partial S ^ {2}} = \frac {1}{S ^ {2} q \ln \theta} <   0,\tag{27}
$$

because lnθ is negative. Therefore, we have

Proposition 1. For an organization in a HIE, the optimal investment for in formation security is a strictly increasing concave function of the potential loss.

The interpretation of Proposition 1 is intuitive. An organization tends to invest more in information security when potential loss is higher because of the higher security risks. But such an increase in optimal investment is less than linear in S, because it is unlikely that any organization can keep increasing the security investment with higher potential loss. Fig. 2 illustrates how w\* varies with S.

To examine the relationship between optimal investment and system susceptibility, we differentiate w\* in Eq. (23) with respect to θ:

$$
\begin{array}{l} \frac {\partial w *}{\partial \theta} = \left(\frac {1}{q \ln \theta}\right) \ln (- \eta q S \theta \ln \theta) - \left(\frac {1}{q \ln \theta}\right) \ln (- \eta q S \theta \ln \theta) (- \eta q S \theta \ln \theta - \eta q S \ln \theta) \\ = - w * [ 1 + \eta q S (\theta + 1) \ln \theta ]. \end{array}\tag{28}
$$

Because $w ^ { * }$ is always positive, the sign of Eq. (28) is determined by the bracketed term. We <sup>fi</sup>rst observe that ηqS(θ + 1)lnθ is negative, since $\theta \in [ 0 , 1 ]$ ]. When S is large enough such that $\mid \eta q \mathsf { S } ( \theta + 1 ) \mathrm { l n } \theta \mid > 1$ for all $\theta \in \left[ 0 , 1 \right]$ , the bracketed term is always negative, and Eq. (28) is always positive. In other words, when S is large, optimal investment w\* increases with θ, the system susceptibility. But for small S, the value of θ determines the sign of the bracketed term. When θ is small, | lnθ | is large, | $\eta q \mathrm { S } ( \theta + 1 ) \mathrm { l n } \theta | > 1$ , and Eq. (28) is positive. But at some point when θ gets closer to 1, | lnθ | becomes small enough to make | ηqS(θ + 1)lnθ | smaller than 1, and as a result Eq. (28) turns negative. Therefore, with small S, $w ^ { * }$ is no longer a strictly increasing function of θ; rather, w\* peaks at some mid-range θ¸ and starts to decrease with increasing θ. These cases are illustrated in Fig. 3, and we have the following proposition:

![](/api/attachments/WJFFCXU5/fulltext/images/2a011853f604efca5ac29dad4beee2ab3b164a1fae947b9fe18cfb0491e6380d.jpg)  
Fig. 2. Optimal investment with respect to potential loss (for notations, see Table 1).

Proposition 2. For an organization in a HIE, the optimal investment for information security always increases with the system susceptibility when the potential loss is high. However, when the potential loss is small, the optimal level of investment decreases with system susceptibility when the susceptibility is large.

Proposition 2 can be interpreted as follows. When the potential loss is high, organizations are compelled to strengthen their security measures, particularly when their systems are open and susceptible to attacks. But when the potential loss is relatively small, the potential risk is small, and the incentive for the organization to invest in security becomes smaller when it is more costly to defend an increasingly open system. And the organization may decide not to invest in security at all when the systems are very susceptible to attacks, because the cost of security investment outweighs the risk. This poses an interesting moral hazard problem, in which the security risks are transferred from one organization to another in a HIE unintentionally (see Section 6 for more detailed discussion).

![](/api/attachments/WJFFCXU5/fulltext/images/9f0fa92b2ffd9e67a32bed002039ab8d3f3e0906d3483d559281357679416e6e.jpg)  
Fig. 3. Optimal investment with respect to systems susceptibility (for notations, see Table 1).

Finally, to further examine the property of w\*, we rearrange Eq. (23) with Eq. (10) to get

$$
w * = \frac {\Omega_ {0} \ln y}{y},\tag{29}
$$

where y is de<sup>fi</sup>ned as

$$
y \equiv - \eta q S \theta \ln \theta .\tag{30}
$$

To <sup>fi</sup>nd the maximum of w\*, we take the <sup>fi</sup>rst derivative with respect to y and set it to zero:

$$
\frac {d w *}{d y} = \Omega_ {0} \frac {1 - \ln y}{y ^ {2}} = 0,\tag{31}
$$

Solving for y on the right hand side, we get lny = 1, or $y = e ,$ the natural exponent. Applying this condition to Eq. (29), we get

$$
w * \leq \frac {\Omega_ {0} \ln e}{e} = \frac {\Omega_ {0}}{e}.\tag{32}
$$

Hence the following proposition:

Proposition 3. The optimal security investment for an organization in a HIE will never exceed e<sup>−</sup> $^ { - 1 } \varOmega _ { 0 } ,$ where $\varOmega _ { 0 }$ is the security risk without any security investment.

Proposition 3 places an upper limit on the organization's level of security investment: The organization will not invest more than $\mathbf { e } ^ { - 1 } \Omega _ { 0 }$ to mitigate the security risk of $\Omega _ { 0 } .$ Any investment above that amount would be deemed not optimal. This is a somewhat surprising result, given that the organization is making decision strictly based on the costs and bene<sup>fi</sup>ts of the investment (that is, the decision is risk neutral.) It is likely that the highly uncertain nature of information security events limit the appetite for optimal level of investment.

## 5. Business bene<sup>fi</sup>ts of security investment

To extend the existing research stream to consider the business bene<sup>fi</sup>ts discussed in Section 2.3 as the basis for security investment, we posit that, in addition to reducing security risks, the security investment S also generate direct business bene<sup>fi</sup>ts for the organization, be they competitive advantage, regulation compliance, reputation, or some other form. Let $B = B ( w )$ denotes such business bene<sup>fi</sup>ts as a result of the organization's information security.

The function B has to satisfy a few boundary conditions. First, because such business bene<sup>fi</sup>ts are completely derived from security investment, $B ( 0 ) = 0$ . Also, there is a <sup>fi</sup>nite limit of business bene<sup>fi</sup>ts that can be achieved no matter how much investment is made to protect its information security:

<sub>ð</sub><sup>33</sup><sub>Þ</sub>

Intuitively, B should be an increasing function of security investment with diminishing importance. In other words,

$$
\frac {\partial B}{\partial w} \geq 0, \frac {\partial^ {2} B}{\partial w ^ {2}} \leq 0.\tag{34}
$$

With B, the net value Π of the security investments in Eq. (10) can be modi<sup>fi</sup>ed as follows:

$$
\Pi (w) = B + (\eta \theta - \phi) S - w.\tag{35}
$$

With the addition of the business bene<sup>fi</sup>ts function, Eq. (35) represents the total business value of information security investment. To <sup>fi</sup>nd the optimal level of investment, one can set the derivative of Eq. (35) with respect to w to zero:

$$
\left. \frac {\partial \Pi}{\partial w} \right| _ {w = w *} = B ^ {\prime} - \eta q (\ln \theta) S \theta^ {q w * + 1} - 1 = 0.\tag{36}
$$

where $\begin{array} { r } { B ^ { ' } \equiv \frac { \partial B } { \partial w } \big | _ { w = w * } } \end{array}$ , the derivative of B at the point of $w ^ { * } .$ Note that because of Eq. $\begin{array} { r } { ( 3 4 ) , \frac { \partial ^ { 2 } \varPi } { \partial w ^ { 2 } } \leq 0 } \end{array}$ , and $w ^ { * }$ is indeed the solution that maximizes Π. Because no a priori principle governs the functional form of B (and thus B′), we would not be able to analytically derive the exact solution of $w ^ { * } .$ . Instead, we proceed to examine the effect of the addition of B′ on w\*. Rewriting Eq. (36), we get

$$
w * = \left(\frac {1}{q \ln \theta}\right) \ln \left(\frac {B ^ {\prime} - 1}{\eta q S \theta \ln \theta}\right).\tag{37}
$$

For optimal investment to exist, the argument of the main logarithmic function on the right-hand side needs to be positive. But since lnθ is negative, we have

B<sup>′</sup>b1:

<sub>ð</sub><sup>38</sup><sub>Þ</sub>

In other words, the slope of B is less than one, or the increase in B is less than the increase in w, at w\*. Since both B and w are continuous and twice differentiable, this result holds in the vicinity of w\*. Thus we have the following proposition:

Proposition 4. Around the optimal level of security investment, investing more does not bring about equivalent increase in business benefits.

Proposition 4 states that the organization would not see dollar-fordollar return on business bene<sup>fi</sup>ts when making security investments. This is understandable, since part of the value of the security investment comes from the reduction of risks (see Eq. (35)). But because we know that the optimal investment is only a fraction of the security risk (Proposition 3) and does not result in fully equivalent business bene<sup>fi</sup>ts (Proposition 4), it is likely that the risk reduction still dominates the business bene<sup>fi</sup>t when the organization considers its level of security investment.

Although no a priori principles can be used to derive the functional form of B, a closer look at its property helps to interpret its impact on security investment decisions. In many, if not most, cases, certain type and/or level of security investment gives rise to a distinctive business bene<sup>fi</sup>t. For instance, speci<sup>fi</sup>c security measures are required for any healthcare organization to be HiPPA compliant and, with that, attain the business bene<sup>fi</sup>t of avoiding HIPPA-related penalties. Mathematically, such “on–off” behavior is best represented by a step function, where the investment—denoted by w —made to satisfy those measures represents the point of discontinuity for the bene<sup>fi</sup>t function to go from zero to full HIPPA compliance. (In modeling, it is customary to simulate a step function with a twice-differentiable S-curve—typical candidates are logistic, Fisher-Pry, or Gompertz.) When the bene<sup>fi</sup>t function B is represented by a step function (or a series of step functions) of w, $\begin{array} { r } { \frac { \partial B } { \partial w } = 0 } \end{array}$ for all w except at w<sub>b</sub>, where ${ \frac { \partial B } { \partial w } } \longrightarrow \infty .$ Because the number of points of discontinuity is <sup>fi</sup>nite (one in the case of a single step function), the probability of $w ^ { * } = w _ { b }$ is in<sup>fi</sup>nitesimal, and the probability of $\begin{array} { r } { B ^ { \prime } \equiv \frac { \partial B } { \partial w } | _ { w = w * } = 0 } \end{array}$ approaches 1. Therefore, when B is a step function, $B ^ { \prime } = 0 , \bar { \mathrm { E q . } } ( \ddot { 3 } 7 )$ reverts back to Eq. (23), and we have the following:

Proposition 5. The optimal level of security investment that maximizes the net benefit to an organization in a HIE is the same with or without the inclusion of step-function-like business benefits as benefits

Despite its simple math derivations, Proposition 5 offers important practical implications. When $w ^ { * } > w _ { b } ,$ the organization making the optimal level of security investment will be able to attain the business bene<sup>fi</sup>t of such an investment. However, when $w ^ { * } < w _ { b } ,$ meaning that the security investment for obtaining the business bene<sup>fi</sup>t is higher than the “optimal” level derived from Eq. (37), the organization making such optimal investment would miss out on the potential business bene<sup>fi</sup>ts of security investment, no matter how large they are. This can particularly become an issue in HIEs, where “collective” business bene<sup>fi</sup>ts are sought. We will discuss this further in the next section.

## 6. Discussion

The National Institute for Standards and Technology (NIST) has provided a de<sup>fi</sup>nitive set of guidelines for managing information security risk, which includes framing risk, assessing risk, responding to risk and monitoring risk [55]. NIST recommends that speci<sup>fi</sup>c risk factors be monitored continuously so as to know when they reach unacceptable levels and cross an organization's risk tolerance. This is an explicit recognition that a theoretical “risk neutral” posture is not the reality in organizational information security. As such, it aligns with Lemma 1, which states that the potential loss from an information security breach should be above a critical loss threshold (i.e. risk tolerance level) to trigger security investments, as well as Proposition 1, which implies that when the potential loss due to a risk is high, organizations are compelled to invest in information security.

Cost has been identi<sup>fi</sup>ed as a constraint to HIE growth [1,26]. Healthcare service providers are just emerging from electronic healthcare record (EHR) technology implementations. While much of the technology costs were reimbursed by the federal government based on the Center of Medicare and Medicaid Services' mandate of Meaningful Use [17], the need for robust communication between EHRs in a HIE network now requires additional interoperability and interface features that were not part of Stage 1 and Stage 2 Meaningful Use, resulting in an additional cost in the EHR implementation to service providers. It is in this context that the limit to security investment described in Proposition 3 takes on an additional signi<sup>fi</sup>cance. It is important for an organization to understand its intrinsic security risk (Ω ) in its consideration of joining a HIE because of the potential cost impact in addition to the implementation of EHR.

Unlike a single monolithic organization making information security investment decisions, members make decisions that may impact the HIE as a whole and/or other organizations. In most or all cases currently, the security investment decisions in a HIE are uncoordinated—that is, each member organization of a HIE makes its own investment in information security based on its thresholds of risk tolerances (Lemma 1) and maximum optimal level of investment (Proposition 3). Issues may arise when all responses to information security are made at the node level and in relative isolation from the network; most individual members do not understand the additional risks encumbered by connectivity in an exchange. For instance, there could be a tendency for the individual or group physician practices in a HIE to underplay the risk since they perceive themselves as “too small to be attacked.” In particular, Proposition 2 implies that when these practices deem their potential losses to be relatively low, the optimal security investment tends to stay low, even when the system susceptible is high (Fig. 3). But by doing so in a connected network such as HIEs, they inadvertently create a “weak link” that has now increased the risk for all other members, leading to shifting the “burden” to others in the same HIE. But in turn, larger organizations in a HIE, such as hospitals, tend to invest more in information security due to the perceived higher risks, thus protecting the smaller establishment in the same network. Such an intrinsic “moral hazard” in a networking environment is real and cannot be ignored [51,76]. A possible resolution to such a moral hazard would require central coordination of investments made by all organizations in the HIE, which can be a dif<sup>fi</sup>cult task.

According to Proposition 5, organizations tend to invest in information security based on risk reduction alone, since it is highly unlikely that the investment necessary to obtain business bene<sup>fi</sup>ts will coincide with the optimal level of investment to minimize risks. In a HIE, in addition to HIPPA compliance [48], the main business bene<sup>fi</sup>t from security investment for all members would be the ability to securely share patient information for better clinical and operational decision making [64]. For large organizations such as the hospitals, the optimal investment is likely to be higher than the level required to obtain such business bene<sup>fi</sup>ts, because their potential loss (thus perceived security risk) is high. However, in the case of smaller providers such as physician practices, it is highly unlikely that their optimal investment would reach the level necessary to capture the business bene<sup>fi</sup>t from the HIE they belong to. The result is that larger member organizations invest enough for all to enjoy the business bene<sup>fi</sup>t that a HIE brings, while smaller providers “underinvest” and cover their own risks. And such a built-in moral hazard would prevent some service providers to invest for the bene<sup>fi</sup>t of the HIE as a whole and may create security holes that impact other organizations in the same HIE. A possible remedy could be an associated payment system on top of the individual security investment for the protection of the overall HIE security that accurately re<sup>fl</sup>ects the bene<sup>fi</sup>t received by each member [3].

Security investment is not fungible in today's investment environment. It is always dif<sup>fi</sup>cult to analyze the value of an investment that is geared towards something not happening, causing an unclear return on investment. It is also dif<sup>fi</sup>cult to relate the value of a security investment for business growth, as stated in Proposition 4. But this limitation would be changing in the coming years, when optimum level of investment for regulatory compliance and penalty avoidance can be made because the availability of secure information exchange in a HIE becomes a business requirement. It would then be possible to build a more traditional return-on-investment case for security investment.

## 7. Conclusion

This study adopts a network-based approach to examine the economics of information security for organizations in a HIE. Our model is based on a priori principles that govern the HIE-like network, and we take into account both risk reduction and business bene<sup>fi</sup>t as values of information security investment. Our results offer extensive insights into how these organizations should make optimal investment decisions. In particular, we show that, although organizations tend to invest more with higher potential loss due to security, investment is only triggered when such potential loss reaches a threshold level. And in a HIE, smaller organizations tend to “underinvest” due to the lower security risks to their own practice, shifting the burden of protecting the network as a whole to larger organizations.

This research, like all studies, has its limitations. As with all analytics, the assumptions we adopt in the mathematical models are unavoidably a simpli<sup>fi</sup>ed representation of reality. For instance, all parameters adopted in the mathematical models are assumed to be well behaved, that is, continuous and twice differentiable. Likewise, certain boundary conditions, such as extremely large expected losses, are excluded to preserve the integrity of the models. And possible relationships among variables could be further explored and modeled, such as the association of attack probability η and security investment w (although it has been shown that a <sup>fi</sup>rm's security investment, often unknown to outside attackers, may not have much of an impact on the external threat [21]).

In the future, it would be useful to relax some of the limitations posed by the mathematically modeling. It should also be noted that, in recent literature, critics of the scale-free networks have argued that the physical structure of the Internet, with its router-based architecture, does not follow the power law connectedness [6,71]. However, because HIE is a sharing network among organizational information systems, not a separate physical architecture, scale-free network remains the most commonly accepted theory for explaining its topological characteristics [8,53].

This study points to a few future research directions. Future studies can couple the mathematical modeling technique with other methodologies, such as qualitative case study or action research, to extend the usefulness and applicability of optimal information security investment, particularly in the case of business bene<sup>fi</sup>ts. As discussed above, these results are optimized for investment decision making at the organizational level but may bring about sub-optimal result for the HIE as a whole. In particular, such nodal optimizations lead to built-in moral hazard, where the smaller providers tend to underinvest from the perspective of the HIE for minimizing risk propagation and obtaining business bene<sup>fi</sup>ts for all HIE members. A natural extension to this study would be to examine the economics of information security for the whole HIE as one scalefree network. The result of such a whole network approach can lead to a coordinated HIE security investment scheme to address the risk mismatch among HIE member and the resulting intrinsic moral hazard.

## References

[1] J. Adler-Milstein, Bates, Paperless healthcare: progress and challenges of an IT-enabled healthcare system, Business Horizon 53 (2010) 119–130.

[2] J. Adler-Milstein, D.W. Bates, A.K. Jha, U.S. regional health information organizations: progress and challenges, Health Affairs 28 (2) (2009) 483–492.

[3] AHIMA/HIMSS, The Privacy and Security Gaps in Health Information Exchange, White Paper by the AHIMA/HIMSS HIE Privacy and Security Joint Work group, 2011.

[4] W. Aiello, F. Chung, L. Lu, A random graph model for massive graphs, Proceedings of the 32nd Annual ACM Symposium on Theory of Computing, New York, 2000, pp. 171–180.

[5] R. Albert, H. Jeong, A.-L. Barabási, Diameter of the world-wide web, Nature 401 (1999) 130–131.

[6] D. Alderson, L. Li, W. Wallinger, J.C. Doyle, Understanding internet topology: principles, models, and validation, IEEE/ACM Transactions on Networking 13 (6) (2005) 1205-1218

[7] S. Alter, S. Sherer, A general, but readily adaptable model of information system risk, Communications of the AIS 14 (1) (2004) 1–28.

[8] R. Anderson, T. Moore, The economics of information security, Science 314 (2006) 610-613.

[9] A. Appari, M.E. Johnson, Information security and privacy in healthcare: current state of research, International Journal of Internet and Enterprise Management 6 (4) (2010) 279–314.

[10] A. Arora, D. Hall, C.A. Pinto, D. Ramsey, R. Telang, Measuring the risk-based value of IT security solutions, IT Professional 6 (6) (2004) 35–42.

[11] A.-L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[12] R.S. Behara, S. Bhattacharva, Process-centric risk management framework for information security, in: H. Chen, T.S. Raghu, R. Ramesh, A. Vinze, D. Zeng (Eds.), National Security, Elsevier, The Netherlands, 2007, pp. 349–366.

[13] L.D. Bodin, L.A. Gordon, M.P. Loeb, Evaluating information security investments using the analytic hierarchy process, Communications of the ACM 48 (2) (2005) 79–83.

[14] R. Bojanc, B.J. Blazic, Towards a standard approach for quantifying an ICT security investment, Computer Standards & Interface 30 (2008) 216–222.

[15] P. Carter, C. Lemery, D. Mikels, R. Bowen, B. Hjort, Privacy and security in health information exchange, Journal of AHIMA 77 (10) (2006) 64A-C

[16] H. Cavusoglu, B. Mishra, S. Raghunathan, The value of intrusion detection systems in information technology security architecture, Information Systems Research 16 (1) (2005) 28–46.

[17] Center for Medicare and Medicaid Services (CMS), Stage 1 vs. stage 2 comparison table for eligible hospitals and CAHs, available at http://www.cms. gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms/Downloads/ Stage1ysStage2CompTablesforHospitals.pdf 2012

[18] S. Chai, M. Kim, H.R. Rao, Form's information security investment decisions: stock market evidence of investors' behavior, Decision Support Systems 50 (2011) 651–661.

[19] M. Collins, C. Gates, G. Kataria, A model for opportunistic network exploits: the case of P2P worms, Fifth Workshop on Economics of Information Security, Cambridge, England, 2006.

[20] D.B. Chang, C.S. Young, Infection dynamics on the internet, Computers & Security 24 (2005) 280–286.

[21] D. Cremonini, M. Nizovtsev, Understanding and in<sup>fl</sup>uencing attackers' decisions: implications for security investment strategies, Fifth Workshop on Economics of Information Security, Cambridge, England 2006

[22] M. Daneva, Applying real options thinking to information security in networked organizations, CTIT Technical Report TR-CTIT-06-11, Centre for Telematics and Information Technology, University of Twente, The Netherlands, 2006.

[23] Dhanjani, Hacking: The Next Generation, O'Reiley Media, 2009.

[24] Emory Univesity, Why IT Security Can Instil Con<sup>fi</sup>dence in a Company's Reputation and Brand, Knowledge @ Emory, 2007. (http://knowledge.emory.edu/article.cfm? articleid=1075s).

[25] M. Faloutsos, P. Faloutsos, C. Faloutsos, On power–law relationships of the internet topology, ACM SIGCOMM Computer Communication Review 29 (4) (1999) 251–262.

[26] P. Fntaine, S.E. Ross, T. Zink, L.M. Schilling, Systematic review of health information exchange in primary care practices, Journal of the American Board of Family Medicine 23 (5) (2010) 655–670.

[27] E. Gal-Or, A. Ghose, The economic incentives for sharing security information, Information Systems Research 16 (2) (2005) 186–208.

[28] L.A. Gordon, M.P. Loeb, The economics of information security investment, ACM Transactions on Information and Systems Security 5 (4) (2002) 438–457.

[29] L.A. Gordon, M.P. Loeb, Return on information security investments: myths vs. realities, Strategic Finance 84 (5) (2002) 26–31.

[30] L.A. Gordon, M.P. Loeb, Managing Cybersecurity Resources: A Cost-Bene<sup>fi</sup>t Analysis, McGraw-Hill, Inc., 2006

[31] L.A. Gordon, M.P. Loeb, W. Lucyshyn, Sharing information on computer systems security: an economic analysis, Journal of Accounting and Public Policy 22 (2003) 461-485.

[32] C. Grif<sup>fi</sup>n, R. Brooks, A note on the spread of worms in scale-free networks, IEEE Transactions on Systems Man and Cybernetics Part B 36 (1) (2006) 198–202.

[33] T. Gross, C.J. Dommar D'Lima, B. Blasius, Epidemic dynamics on an adaptive network, Physical Review Letters 96 (2006) 208701.

[34] W. Grossman, P.D.F. Ion, On a portion of the well-known collaboration graph Congressus Numerantium 108 (1995) 129–131.

[35] M. Gupta, S. Banerjee, M. Agrawal, H.R. Rao, A framework for security analysis of internet technology components enabling globally distributed workplaces, ACM Transactions on Internet Technology 8 (4) (2008) 17:2–17:38.

[36] HHS (Department of Health and Human Services), HIPPA Security Series, 1. Security 101 for Covered Entities, accessed at http://www.hhs.gov/ocr/privacy/hipaa/ administrative/securityrule/security101.pdf2007.

[37] C.D. Huang, R.S. Behara, Economics of information security investment in the case of simultaneous attacks, International Journal of Production Economics 141 (1) (2013) 255–268.

[38] C.D. Huang, Q. Hu, R.S. Behara, Economics of information security investment in the case of simultaneous attacks, International Journal of Production Economics 114 (2) (2008) 793–804.

[39] IT PCG (IT Policy Compliance Group), The <sup>fi</sup>nancial bene<sup>fi</sup>ts of spend on security, accessed at http://www.itpolicycompliance.com/wp-content/uploads/2013/02/ The-Financial-Bene<sup>fi</sup>ts-of-Spend-on-Security-Overview.pdf2012.

[40] M.E. Jennex, S. Zyngier, Security as a contributor to knowledge management success, Information Systems Frontier 9 (2007) 493–504.

[41] H. Jeong, S. Mason, A.-L. Barabasi, Z.N. Oltival, Lethality and centrality in protein networks Nature 411 (2001) 41–42

[42] M.E. Johnson, Health-care industry: heal thyself, Wall Street Journal (September 26 2011). http://online.wsi.com/news/articles/SB10001424053111904716604576 542380296355702

[43] M.E. Johnson, S. Dynes, Inadvertent disclosure—information leaks in the extended enterprise, Sixth Workshop on the Economics of Information Security, Pittsburgh, Penn, June 7-8 2007.

[44] R. Kaas, M. Gavaerts, J. Phaene, M. Dennit, Modern Actuarial Risk Theory, Kluwer Academic Publishers, Boston, Mass., 2001

[45] M.J. Keeling, K.T.D. Eames, Networks and Epidemic Models, Journal of the Royal Society Interface 2 (2005) 295–307.

[46] R.L. Kumar, S. Park, C. Subramniam, Understanding the value of countermeasure portfolios in information security, Journal of Management Information Systems 25 (20) (2008) 241–279.

[47] H. Kunreuther, G. Heal, Interdependent security, Journal of Risk and Uncertainty 26 (2/3) (2003) 231–249.

[48] J. Kwon, M.E. Johnson, Security practices and regulatory compliance in the healthcare industry, Journal of American Medical Informatics Association 20 (2013) 44–51.

[49] Y.C. Lai, Z. Liu, N. Ye, Infection dynamics on growing networks, International Journal of Modern Physics B 17 (22,23,24) (2003) 4045–4061.

[50] Y.J. Lee, R.J. Kauffman, R. Sougstad, Pro<sup>fi</sup>t-maximizing form investments in customer information security, 51 (2011) 904–920.

[51] C.H. Lee, X. Geng, S. Raghunathan, Contracting Information Security in the Presence of Double Moral Hazard, Information Systems Research 24 (2) (June 2013) 295–311.

[52] F. Liljeros, C.R. Edling, L.A.N. Amaral, H.E. Stanley, Y. Aberg, The web of human sexual contact Nature 411 (2001).907–908

[53] S. Nagaraja, R. Anderson, The topology of covert con<sup>fl</sup>ict, Computer Laboratory Technical Report UCAM-CL-TR-637 University of Cambridge 2005.

[54] National Alliance for Health Information Technology, Report to the Of<sup>fi</sup>ce of the National Coordinator for Health IT on De<sup>fi</sup>ning Key Health Information Technology Terms. April 2008.

[55] National Institute of Standards and Technology, Managing security risk: organization, mission, and information system view, NIST Special Publication 800-39, U.S. Department of Commerce, 2011.

[56] M.E.J. Newman, The structure and function of complex networks, SIAM Review 45 (2) (2003) 167–256.

[57] H. Ogut, N. Menon, Cyber insurance and IT security investment: impact of interdependent risk, Fourth Workshop on the Economics of Information Security, Cambridge, Mass, June 2-3 2005.

[58] R. Pastor-Satorras, A. Vespignani, Epidemic spreading in scale-free networks, Physical Review Letters 86 (14) (2001) 3200–3203.

[59] Ponemon Institute, Benchmark study on patient privacy and data security, http://www2.idexpertscorp.com/resources/healthcare/healthcare-articleswhitepapers/ponemon-benchmark-study-on-patient-data-security-practices/? utm\_source=Ponemon%2BRedirect&utm\_medium=Online&utm\_campaign= Ponemon%2BRedirect/. November 2010(accessed 4 April 2011).

[60] S. Pursor, A Practical Guide to Managing Information Security, Artech House, 2004.

[61] S. Redner, How popular is your paper? An empirical study of the citation distribution, European Physics Journal B 23 (1998) 267–271.

[62] T. Sawik, Selection of optimal countermeasure portfolio in IT security planning, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.01.001.

[63] S.E. Schechter, Toward econometric models of the security risk from remote attacks, IEEE Security & Privacy 3 (1) (2005) 40–44.

[64] J. Song, F.M. Zahedi, Trust in health infomediaries, Decision Support Systems 43 (2007) 390–407.

[65] D.S. Soper, H. Demirkan, M. Goul, An interorganizational knowledge sharing security model with breach propagation detection, Information Systems Frontier 9 (2007) 469–479.

[66] M.M. Telo da Gama, A. Nunes, Epidemics in small world networks, European Physical Journal B 50 (2006) 205–208.

[67] T. Tsiakis, G. Stephanides, The economic approach of information security, Computer & Security 24 (2005) 105–108.

[68] A. Vazquz, M. Boguna, Y. Moreno, R. Pastor-Satorras, A. Vespignani, Topology and correlations in structured scale-free networks, Physical Review E 67 (2003) 046111.

[69] V. Viduto, C. Maple, W. Huang, D. Lopez-Perez, A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem, 53 (2012) 599–610.

[70] J. Walker, E. Pan, D. Johnston, J. Adler-Milstein, D.W. Bates, B. Middleton, The value of health care information exchange and interoperability, Health Affairs, Supplemental Web Exclusive, 2005, (W5-10-W5-18).

[71] W. Wallinger, R. Govindan, S. Jamin, V. Paxson, S. Shenker, Scaling phenomena in the internet: critically examining criticality, Proceedings of National Academy of Science 99 (1) (2000) 2573–2580.

[72] I Wang How may IT security affect competitive advantage? The Fourth ABIT Annual Meeting, Monroeville, Pennsylvania, 2004.

[73] J. Wang, A. Chaudhury, H.R. Rao, A value-at-risk approach to information security investment, Information Systems Research 19 (1) (2008) 106–120.

[74] D.J. Watts, S.H. Strogatz, Collective dynamics of “small-world” networks, Nature 393 (1998) 440-442

[75] L. Xiao, B. Hu, M. Croitoru, P. Lewis, S. Dasmahapatra, A knowledgeable security model for distributed health information systems, Computer & Security 29 (2010) 331–349.

[76] W.T. Yue, M. Cakanyildirim, Y.U. Ryu, D. Liu, Network externalities, layered protection and IT security risk management, Decision Support Systems 44 (2007) 1–16.

[77] T. Zhou, Z. Fu, B. Wang, Epidemics on complex networks, Progress in Natural Science 16 (5) (2006) 452-457

[78] T. Zhou, J.G. Liu, W.J. Bai, G.C. Chen, B. Wang, Behaviors of susceptible-infected epidemics on scale-free networks with identical infectivity. Physical Review E 74 (2006) 056109.

[79] R. Albert, H. Jeong, A.L. Barabási, Error and Attack Tolerance of Complex Networks Nature 406 (2000) 378–382.

[80] Kaufman Rossin & Co, Hitech Act Three Years Later: Are Health Records Safe? White paper Series (2012)(Kaufman Russin & Co., 2012).

[81] S. Dynes, H. Brechbühl, M.E. Johnson, Information Security in the Extended Enterprise: Some Initial Results from a Field Study of an Industrial Firm, Fourth Workshop on Economics of Information Security, June 2–3, 2005, Cambridge, Mass, United States, 2005.

C. Derrick Huang is an Associate Professor at the Department of Information Technology and Operations Management, College of Business, Florida Atlantic University. Previously, as a practitioner, he held executive-level positions in the area of marketing and strategic planning in a number of high-tech companies. Dr. Huang's research interest lies in the business value and strategic impact of information technology in organizations, and his current focus is on the economics of information security investments, risk management of information systems, and healthcare IT. His work has been published in leading journals such as Decision Sciences Journal, Decision Support Systems, International Journal of Production Economics, Communications of the AIS, Information Systems Management, and Information Systems Frontier. He holds Ph.D. from Harvard University.

Ravi S. Behara is an Associate Professor in the Department of Information Technology & Operations Management in the College of Business at Florida Atlantic University. His current research interests include health care operations and service analytics He has published a variety of articles on service operations in academic journals, including International Journal of Operations and Production Management and International Journal of Production Economics and in research books such as Handbooks in Information Systems and Advances in Patient Safety. Dr. Behara's consulting assignments include the creation of a new service development methodology for a large U.S. financial services organization. He also worked as an electrical engineer in the construction of large multinational power plants projects in India and Saudi Arabia. He holds a Ph.D. in Service Operations Management from Manchester Metropolitan University, UK, and a B.E. in Electrical Engineering from The Indian Institute of Science.

Jahyun Goo is an associate professor of MIS at the Florida Atlantic University. His active research areas are IS sourcing, IT management and strategy, interorganizational relationships, healthcare IT, and IS Security. His papers have been published in MIS Quarterly, Decision Sciences, Decision Support Systems, Information Systems Journal, and Information Systems Frontier, among others. Dr. Goo has presented his research at the premier IS conferences. His work has recognized from the conferences and publishers as best or outstanding paper awards. He has served for major journals as either a reviewer or a coordinating editor. He holds Ph.D. in MIS from the State University of New York at Buffalo.
