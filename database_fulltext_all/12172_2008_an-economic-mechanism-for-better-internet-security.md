---
otero_id: 12172
otero_key: "H5FNPB6N"
title: "An economic mechanism for better Internet security"
authors: "Xia Zhao; Fang Fang; Andrew B. Whinston"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.02.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An economic mechanism for better Internet security

Xia Zhao <sup>a,</sup>⁎, Fang Fang <sup>b</sup>, Andrew B. Whinston <sup>c</sup>

<sup>a</sup> Tuck School of Business, Dartmouth College, Hanover, NH 03755, United States

<sup>b</sup> College of Business Administration, California State University at San Marcos, San Marcos, CA 92096, United States

<sup>c</sup> Red McCombs School of Business, University of Texas at Austin, Austin, TX 78712, United States

## a r t i c l e i n f o

Article history: Received 25 April 2007 Received in revised form 30 January 2008 Accepted 7 February 2008 Available online 10 March 2008

Keywords: Information Security Internet security Mechanism design Certificates Interdependent security

## a b s t r a c t

Our paper proposes a certi<sup>fi</sup>cation mechanism to align the incentives for Service Providers (SPs) to safeguard the Internet and protect their customers. The proposed mechanism certi<sup>fi</sup>es the capable SPs who are willing to be <sup>fi</sup>nancially accountable for damage caused by malicious traf<sup>fi</sup>c from their networks. Such a certi<sup>fi</sup>cation program provides a channel for certi<sup>fi</sup>ed SPs to signal their commitments to secure network communication to their customers and other certi<sup>fi</sup>ed SPs. We evaluate the ef<sup>fi</sup>ciency of the mechanism using a game-theoretic model. Our study provides an economic foundation and managerial guidance for improving Internet security.

Published by Elsevier B.V.

## 1. Introduction

Security problems, including spam and malware, plague the Internet to the point of distracting from productive use of the network. Technology is waging an admirable battle against these problems, but its solutions may not be suf<sup>fi</sup>cient by themselves to provide adequately secure environments. Fundamental issues with the design and interconnection policies of the Internet infrastructure contribute to the vulnerability to generation and dissemination of new attacks. Instead of relying exclusively on technology solutions in the context of the current policy framework, we consider a possible altered framework that could relate interconnection to security. Policy changes, rather than protocol changes, are considered.

The Internet can be viewed as an economic system besides being a set of technology components. Such a view focuses attention on the interdependence and incentives of participating economic agents, who include service providers, users, and purveyors of malware and spam. It has been recognized that Internet security problems can be understood in terms of economic concepts, such as externality, liability, and moral hazard [1,14,15,18]. While this is a useful insight, we need to go further and explore whether economic concepts can help us frame a pragmatic proposal to alleviate security problems by in<sup>fl</sup>uencing some of the economic factors that govern the actions and interdependence of the participants. Such a proposal may draw from public policy and law which have also dealt with the need to control socially harmful actions by some of the members of various communities.

In our proposal we recognize certain features of the Internet. As distinct from the legal approach to controlling crime, the information infrastructure has no clear delineation of jurisdiction, or corresponding enforcement powers. To illustrate by an analogy, with traditional criminal behavior such as bank theft, there are national laws that govern this behavior and associated police actions. Assigning the liability to the perpetrators and expecting the police to apprehend them are considered reasonable ways to reduce crime. Prosecution of a crime is focused on the perpetrator, precisely because the scope of jurisdiction and the powers of investigation, enforcement, veri<sup>fi</sup>cation and punishment are well de<sup>fi</sup>ned and can be vested into formal institutions and policies. With the Internet, the analogy is to view the crackers as the liable entity to be apprehended and punished. The analogy breaks down since the cracker could be in a foreign jurisdiction that does not recognize the laws of the country that suffered the attack of the crackers. Of course, this assumes that the crackers could be identi<sup>fi</sup>ed which could be impossible.

The natural assignment of liability to the perpetrators is not a practical way of looking at the Internet security problem. Instead we propose to consider the service provider (SP) as the entity to assume liability for the actions of its customers. Service providers are businesses or organizations who provide Internet access and related services to their customers or users. For example, Yahoo!, AOL, universities, government agencies and large companies. Since the SP itself does not carry out any attack, but only transports traf<sup>fi</sup>c from customers some of whom may be crackers, it appears unreasonable to place blame on SPs. It is common practice for public policy and law to make allowances for aspects of practical deployment of enforcement policies while formulating them. Accordingly, it may be seen that controls are sometimes applied at those nodes in organizational or community hierarchies which have the highest ability to in<sup>fl</sup>uence the targeted criminal activity.

It would also be reasonable to assume that SPs would not voluntarily accept such a status since they would not accept a liability for a criminal action that they did not commit. Thus we need to show that a case can be made for SPs to voluntarily accept liability. In other words, we need to show that SPs may <sup>fi</sup>nd it in their interest to subscribe to a framework that makes them responsible for security problems initiated by their customers. We denote the SPs that subscribe to the proposed policy framework as being “certi<sup>fi</sup>ed”.

To induce a SP to accept liability and thus to become certi<sup>fi</sup>ed, we propose that all of the certi<sup>fi</sup>ed SPs' traf<sup>fi</sup>c once identi<sup>fi</sup>ed be carried to other certi<sup>fi</sup>ed SPs without any additional reduction in performance for inbound <sup>fi</sup>ltering. In contrast, traf<sup>fi</sup>c from a non-certi<sup>fi</sup>ed SP may be blocked or signi<sup>fi</sup>cantly slowed down by certi<sup>fi</sup>ed SPs for careful screening. Thus customers of a certi<sup>fi</sup>ed SP would obtain better service quality compared to customers of a non-certi<sup>fi</sup>ed SP and should be willing to pay a higher price for the service. However, the value to customers of a certi<sup>fi</sup>ed SP depends, in general, on how many other SPs decide to become certi<sup>fi</sup>ed. Since certi<sup>fi</sup>cation brings with it the liability obligation, a SP has both the issue of how many other SPs, it believes, will choose certi<sup>fi</sup>cation and how capable it is in monitoring and detecting possible traf<sup>fi</sup>c from its customers that could result in costly penalties. The latter decision is a one based on private information that the SP possesses but the former information is a guess or a conjecture.

This is especially complex since each SP is facing the same conjectural decision and the result could easily lead to inconsistent results where SPs make conjectures about the composition of the certi<sup>fi</sup>ed group which turns out to be incorrect. Is there a possibility of a solution where the conjecture or expectation of the SPs are consistent and creates a subset of SPs that form a certi<sup>fi</sup>ed group and thus a viable and more secure environment within the Internet? The answer depends on the number of capable SPs and the number of users who could <sup>fi</sup>nancially appreciate the bene<sup>fi</sup>ts of a more secure Internet environment. So the challenge of voluntarily creating a collection of certi<sup>fi</sup>ed SPs with their associated customers is in the end an empirical issue. That is, we need to validate the conceptual framework by conducting experimental investigations into whether certi<sup>fi</sup>cation can attain suf<sup>fi</sup>cient critical mass to generate signi<sup>fi</sup>cant improvements for the certi<sup>fi</sup>ed providers and their customers, and that such gains are not offset by partial degradation of connectivity to the non-certi<sup>fi</sup>ed environment.

Our mechanism promotes the adoption of secure Border Gateway Protocols (BGPs) and minimizes the incidents of pre<sup>fi</sup>x hijacking attacks. BGP, by design, assumes that all SPs are benevolent and that SPs trust each other. If a cracker compromises a SP's router, he can make the router to advertise that he owns some IP addresses without being challenged by other routers. Such an attack is referred to as pre<sup>fi</sup>x hijacking or IP hijacking. By hijacking IP addresses, crackers can conduct malicious activities, such as sending spam, initiating DDoS attacks and intercepting traf<sup>fi</sup>c [3]. Researchers have proposed various secure BGP, such as S-BGP, soBGP, IRV and SPV to address pre<sup>fi</sup>x hijacking attacks [6,8,12,13,19]. However, adoption of secure BGP will happen only when there are enough adopters due to network externalities [5]. Our mechanism requires certi<sup>fi</sup>ed SPs to implement these protocols and hence facilitates the adoption of secure BGPs.

The proposed mechanism is also capable to identify competent SPs without implementing complicated reputation algorithms. Reputation systems have been suggested to help resolve the information asymmetry among communication parties over the Internet. A variety of reputation measurements have been proposed to evaluate each parties online activities. For example, the Cooperative Association for Internet Data Analysis (CAIDA) and RocketFeul aim to construct the topology maps of Internet infrastructure. The Spamhaus Block list and SenderCops maintain a realtime database of IP addresses of reported and veri<sup>fi</sup>ed spam sources; SenderBase monitors email traf<sup>fi</sup>c on the Internet and provides an accurate view of the sending patterns of mail senders. Different from these approaches, our mechanism induces SPs voluntarily to report their nature and consequently establishes a white list.

![](/api/attachments/H5FNPB6N/fulltext/images/1fea96b8a90c3e19a5eb8499f76261a52d29d654d23d93c4ef1864e249a562e0.jpg)  
Fig. 1. Internet traf<sup>fi</sup>c with protective practices vs. regulative practices.

![](/api/attachments/H5FNPB6N/fulltext/images/0454008a7d9b0ca48b450d770e16aedfa75b2b4318ec69b40d98ea92d9b60645.jpg)  
Fig. 2. The network with the certi<sup>fi</sup>cation mechanism.

To summarize, our approach is to assign liability to those SPs who in turn voluntarily accept it. For a SP that has accepted responsibility there is a strong incentive to monitor and also to write contracts with customers that hold them responsible both <sup>fi</sup>nancially and possibly in terms of reputation. Even without explicit liability, the approach induces SPs to monitor the behavior of their computing environments to ensure that it is not used explicitly or otherwise to cause damage.

## 1.1. Security practices

Before investigating SPs' incentives to accept liability for security, we need to examine SPs' choices of security practices. We classify technologies and methods for SPs to control security into two categories, regulative practices and protective practices.

We refer to the set of technologies and methods for SPs to minimize the possibility of sending out malicious traf<sup>fi</sup>c as regulative practices, for example, the technologies used to monitor users and <sup>fi</sup>lter outgoing traf<sup>fi</sup>c. We refer to the set of technologies and methods for SPs to minimize the possibility of receiving malicious traf<sup>fi</sup>c as protective practices, for example, the technologies used to <sup>fi</sup>lter incoming traf<sup>fi</sup>c. Fig. 1 demonstrates the impact of protective and regulative practices on Internet traf<sup>fi</sup>c.

Regulative practices are considered, in general, more effective<sup>1</sup> than protective practices for three reasons. First, it is easier for SPs to perform regulative practices than protective practices because of information advantages. SPs have direct relationship with their customers and are able to acquire more information about their customers. For example, a SP can monitor its customers and recognize abnormal communication patterns. It can contact customers to detect third-party hacking. In contrast, it is very dif<sup>fi</sup>cult and costly for SPs to identify malicious traf<sup>fi</sup>c originating from other networks. Second, SPs have administrative powers. They can slow down a connection, quarantine zombie computers, or directly disconnect crackers, spammers or phishers. Finally, regulative practices alleviate network congestion by dropping malicious traf<sup>fi</sup>c before it passes through the Internet.

## 1.2. Certification mechanism

Currently, not all SPs are willing to assume the responsibility for security and deploy regulative practices to examine the traf<sup>fi</sup>c they are forwarding. SPs either take no security action or only deploy protective practices to improve local security<sup>2</sup>. By assigning liability, our certi<sup>fi</sup>cation mechanism can induce SPs to deploy regulative practices within the certi<sup>fi</sup>ed network and improve overall Internet security.

The certi<sup>fi</sup>cation mechanism includes three kinds of players, the certi<sup>fi</sup>cation provider, SPs and customers. They interact in two stages as follows.

In the <sup>fi</sup>rst stage—the subscription stage

• The certi<sup>fi</sup>cation provider determines a subscription fee for certi<sup>fi</sup>cation services;

• SPs voluntarily subscribe to certi<sup>fi</sup>cation services;

• The certi<sup>fi</sup>cation provider issues certi<sup>fi</sup>cates to subscribed SPs and maintains a list of certi<sup>fi</sup>ed SPs.

In the second stage—the communication stage

• SPs invest in security practices, determine customers Internet access fees and initiate network services;

• Certi<sup>fi</sup>ed SPs are required to compensate other certi<sup>fi</sup>ed SPs for damage caused by malicious traf<sup>fi</sup>c originating from their networks;

• Certi<sup>fi</sup>ed SPs are required to compensate their own customers for damage caused by malicious traf<sup>fi</sup>c regardless of its source.

Certi<sup>fi</sup>cates serve as informative signals in this mechanism. Certification status of a SP is publicly observable. For example, the certi<sup>fi</sup>cation provider maintains a list of certi<sup>fi</sup>ed SPs. Customers can learn a SP's commitment and capability by observing whether it is on the list. Certi<sup>fi</sup>cation technologies must guarantee authentication and non-repudiation. That is, certi<sup>fi</sup>ed SPs are con<sup>fi</sup>dent of identifying the source of the traf<sup>fi</sup>c; and certi<sup>fi</sup>ed SPs cannot deny the traf<sup>fi</sup>c that they send out or claim receiving traf<sup>fi</sup>c that they have never received. Candidate technologies which ful<sup>fi</sup>ll these characteristics of certi<sup>fi</sup>cation are Public/Private Key Infrastructure, such as digital signatures. The network with the certi<sup>fi</sup>cation mechanism is demonstrated in Fig. 2.

The certi<sup>fi</sup>cation provider plays a signi<sup>fi</sup>cant role in controlling Internet security in our mechanism. It motivates all certi<sup>fi</sup>ed SPs to watch the traf<sup>fi</sup>c sent to the Internet. It moderates and arbitrates disputes among SPs about the occurrence of security breaches and the subsequent compensation. In addition, the certi<sup>fi</sup>ed provider can share breach information among certi<sup>fi</sup>ed SPs, helping them prevent new breaches. For example, once compensation is transferred between certi<sup>fi</sup>ed SPs, the certi<sup>fi</sup>ed provider will solicit the detailed breach information and publicize it within the “certi<sup>fi</sup>ed network”.

We use a game-theoretic model to examine SPs' incentive and evaluate the ef<sup>fi</sup>ciency of the certi<sup>fi</sup>cation mechanism. In addition to the traditional screening and signaling mechanism, our model incorporates network externalities as an important feature of Internet communications. In traditional screening and signaling games, choices by players generally depend only on their own inherent characteristics. In our model, a SP's choice depends not only on its own characteristics but also the expected choices of other SPs. For example, when a SP decides whether to subscribe to certi<sup>fi</sup>cation services, it will also consider other SPs' expected subscription decisions, i.e., the expected number of SPs in the certi<sup>fi</sup>ed non-certi<sup>fi</sup>ed network and their types. As a result, the interdependency among the SPs' payoffs largely affects the equilibrium outcome the certi<sup>fi</sup>cation provider can induce.

The organization of this chapter is as follows. In Section 2, we review recent literature on information security. In Section 3, we outline a game-theoretic model and derive important conditions. In Section 4, we analyze strategies of various players and derive equilibria. System ef<sup>fi</sup>ciencies and the certi<sup>fi</sup>cation provider's pro<sup>fi</sup>t are also analyzed. Section 5 concludes the chapter with a discussion of implementation issues.

## 2. Literature review

As information security has been extensively studied from a technological perspective, there is an emerging body of literature exploring security issues from an economic perspective. Anderson and Moore [1] indicate that incentive misalignment signi<sup>fi</sup>cantly undermines information security and emphasize that incentives should be considered in security design. Varian [18] also points out that besides identifying weak points and indicating who might be in position to <sup>fi</sup>x them, a security analysis should further examine incentives of those who are responsible for security. Liability should be assigned to those who are best positioned to improve security. Lichtman and Posner [15] propose that holding ISPs liable or partially liable can help improve the ef<sup>fi</sup>ciency of security protection<sup>3</sup>. Parameswaran et al. [17] speci<sup>fi</sup>cally point out that SPs who provide direct Internet access to end users should protect their users and safeguard the overall network. This paper shares the view that SPs should be responsible for security and introduces incentives for them to achieve this goal.

This paper also connects to research exploring the optimal security investment. Gordon and Loeb [7] develop an economic model to study the optimal investment in information security. Huang et al. [9] further extend Gordon and Loeb's paper [7] and consider a security threat scenario where attacks from multiple agents occur simultaneously. Cavusoglu et al. [4] use a game-theoretical model to analyze the impact of IT security investment on manual monitoring, <sup>fi</sup>rewall and IDS con<sup>fi</sup>gurations considering the difference in costs. All these papers ignore the interdependency between individuals and organizations on the Internet and take a <sup>fi</sup>rm' risks as exogenously given.

The Internet risks and the incidents of security breaches are highly interdependent due to the global connectivity of the Internet. Kunreuther and Heal [14] demonstrate that <sup>fi</sup>rms fail to coordinate their security investment in the presence of interdependent risks. An entity will signi<sup>fi</sup>cantly underinvest if it believes that there are other weak nodes in the network, leading to an inef<sup>fi</sup>cient equilibrium. Ogut et al. [16] show that risk interdependency lowers <sup>fi</sup>rms' incentive to invest in security protection and buying insurance coverage. These papers capture the nature of Internet security and exhibit its impact on <sup>fi</sup>rms' decisions and market equilibria. However, eliminating the source of insecurity is generally not considered.

Researchers have started to examine the impact of various security mechanisms and policies on Internet security. Kannan and Telang [11] compare the social ef<sup>fi</sup>ciency of a CERT-type mechanism to that of a market-based mechanism on vulnerability disclosure. August and Tunca [2] compare the impact of different security policies on individual user's incentive to patch software taking account of patching costs and negative network externalities. Huang et al. [10] discuss the weaknesses of existing solutions to DDoS attacks and then propose two approaches to counter such attacks. In this study, we propose a novel economic mechanism, a certi<sup>fi</sup>cation mechanism, to enhance collaboration among SPs and eliminate sources of malicious activities.

![](/api/attachments/H5FNPB6N/fulltext/images/573f23aacf7fd054c4765b27e7c44c97bce88875ac0849729908fc48076d555a.jpg)  
Fig. 3. The timing of the dynamic game.

## 3. Certi<sup>fi</sup>cation mechanism and model

The certi<sup>fi</sup>cation mechanism aims to induce SPs to be responsible for security. They should protect their customers from security attacks as well as stop their customers from generating attacks. Consequently, the overall network security should be improved.

## 3.1. Model setup

We consider a classical network with N SPs. Each SP serves n customers. For notational simplicity, we de<sup>fi</sup>ne $M = N n ^ { 2 }$ . Let q denote the ratio of the potential malicious traf<sup>fi</sup>c volume to the regular traf<sup>fi</sup>c volume originating from a SP's network. $q \in \{ q _ { \mathrm { h } } , q _ { \mathrm { l } } \}$ , where subscripts h and l indicate the type of a SP. A SP is either of high-type (h) or low-type (l). Without loss of generality, we assume that users of high-type SPs generate less malicious traf<sup>fi</sup>c than those of low-type SPs, i.e. $q _ { \mathrm { h } } { < } q _ { \mathrm { l } }$ . A SP's type is only known by the SP itself. The common prior belief is that $\operatorname* { P r } ( q = q _ { \mathrm { h } } ) = \delta$

A customer enjoys communicating with other Internet users and dislikes receiving malicious traf<sup>fi</sup>c. A customer's average valuation of sending or receiving a unit of regular traf<sup>fi</sup>c is V. The expected loss of a customer from receiving a unit of malicious traf<sup>fi</sup>c is v. We normalize the expected volume of unidirectional Internet data stream between two customers to 1. If no service provider has deployed any security protection, a customer's expected utility can be expressed as $2 N n V - N n \nu ( \delta q _ { \mathrm { h } } + ( 1 - \delta ) q _ { \mathrm { l } } ) - p ,$ , where p is the <sup>fl</sup>at fee charged by the SP. It is worth noticing that a customer's utility is determined by the distribution of SPs' types in the network and independent of her own SP's type. This is because a customer's value of the network is determined by their overall risks of receiving malicious traf<sup>fi</sup>c, which can come from any other SP. This is known as the interdependency of communication networks.

SPs can choose to invest either protective practices or regulative practices, or both. By investing in protective practices, a SP can screen the inbound traf<sup>fi</sup>c and detect potential malicious traf<sup>fi</sup>c. The SP can choose the effectiveness of protective practices, which is measured by the probability to identify a unit of malicious traf<sup>fi</sup>c from inbound traf<sup>fi</sup>c $x _ { p } \in [ 0 , 1 ]$ , by incurring costs $C _ { p } ( x _ { p } ) .$ . Similarly, a SP can invest $C _ { r } ( x _ { \mathrm { r } } )$ to detect potential malicious traf<sup>fi</sup>c in outbound traf<sup>fi</sup>c with probability $x _ { \mathrm { r } } { \in } [ 0 . 1 ]$ . Both $C _ { p } ( x _ { p } )$ and $C _ { r } ( x _ { \mathrm { r } } )$ are increasing and convex. For mathematic tractability, we follow the literature and choose quadratic forms for the cost functions. That is, $\begin{array} { r } { C _ { p } ( x _ { p } ) = \frac { 1 } { 2 } \alpha _ { p } x _ { p } ^ { 2 } } \end{array}$ and $\begin{array} { r } { C _ { r } ( x _ { r } ) = \frac { 1 } { 2 } \alpha _ { r } x _ { r } ^ { 2 } } \end{array}$ . To characterize the fact that regulative practices are more effective than preventive practices, we assume that $\alpha _ { p } { > } \alpha _ { \mathrm { { r } } }$ In addition, we assume that the probability for regular traf<sup>fi</sup>c to be erroneously marked and discarded is 0.

The certi<sup>fi</sup>cation provider charges a subscription fee, t, for certi<sup>fi</sup>cation services to each SP. In order to stay certi<sup>fi</sup>ed, a SP must agree to compensate other certi<sup>fi</sup>ed SPs at the level of v per unit of malicious traf<sup>fi</sup>c originating from its own network. That is, it takes full responsibility of the loss generated by its users. It also agrees to compensate its customers at the level of v per unit of malicious traf<sup>fi</sup>c to cover their losses. The timeline of the game is shown in Fig. 3.

## 3.2. Conditions

The certi<sup>fi</sup>cation mechanism is designed to induce SPs to control malicious traf<sup>fi</sup>c. Such a mechanism is valuable when the following conditions hold. First, $2 M V { > } \alpha _ { p }$ (Condition 1). That is, the cost of security investments is not so high compared to the regular value of communication. Second, α ≥Mvq (Condition 2). Condition 2 states that security investments are costly so full detection of malicious traf<sup>fi</sup>c (i.e. x=1) is not desirable.

## 4. Analysis

In this section, we analyze strategies for both the SPs and the certi<sup>fi</sup>cation provider. Equilibrium outcomes are then identi<sup>fi</sup>ed and compared. We consider two cases: (i) a benchmark case without the certi<sup>fi</sup>cation mechanism and (ii) the case where the certi<sup>fi</sup>cation mechanism is deployed.

In the second case, we focus on the symmetric Perfect Bayesian Equilibrium where SPs with the same types will adopt the same strategies. We analyze the ranges of certi<sup>fi</sup>cation subscription fee t to support the following two possible outcomes: (1) a separating outcome that only hightype SPs subscribe to certi<sup>fi</sup>cation services and (2) a pooling outcome that all SPs subscribe to certi<sup>fi</sup>cation services<sup>4</sup>.

Given each level of subscription fees, a SP needs to decide the following four strategies:

1. the subscription strategy: whether to subscribe to certi-<sup>fi</sup>cation services;

2. the blocking strategy: whether to completely block the inbound traf<sup>fi</sup>c;

3. the pricing strategy: how much to price their services;

4. the investment strategy: whether to invest in protective and/or regulative practices and how much to invest.

The above strategies can be affected by the subscription fees charged by the certi<sup>fi</sup>cation provider. We then investigate the certi<sup>fi</sup>cation provider's pricing strategy and derive the equilibrium strategy for the certi<sup>fi</sup>cation provider. We also study the certi<sup>fi</sup>cation provider's pro<sup>fi</sup>tability.

## 4.1. Benchmark case

In the benchmark case, all the SPs will choose to invest in protective practices since only those practices have a direct impact on the SPs' quality of service and pro<sup>fi</sup>tability. In contrast, SPs will not deploy regulative practices because such practices bene<sup>fi</sup>t only the recipient customers who are mostly in other SPs' networks. The SP i charges a price $p _ { i } ^ { \mathrm { b } }$ up to a customer's willingness to pay:

$$
p _ {i} ^ {\mathrm{b}} = 2 N n V - N n v \left(1 - x _ {i p} ^ {\mathrm{b}}\right) E [ q ]\tag{1}
$$

Here superscript b refers to the benchmark case. The <sup>fi</sup>rst term on the right-hand-side of Eq. (1) is a customer's expected bene<sup>fi</sup>t from communicating with other Internet users. The second term represents a customer's expected loss caused by malicious traf<sup>fi</sup>c. x<sup>b</sup> represents the effectiveness of SP i's protective practices. A customer's expected value is independent of her SP's type, q . Rather, it is a parameter of the average type of all the SPs, E[q]. We can write down a SP's pro<sup>fi</sup>t as follows.

$$
\begin{array}{c} \pi_ {i} ^ {b} = p _ {i} ^ {b} n - C _ {p} \Big (x _ {i p} ^ {b} \Big) = 2 M V - M v \Big (1 - x _ {i p} ^ {b} \Big) E [ q ] \\ - \frac {1}{2} \alpha_ {p} \Big (x _ {i p} ^ {b} \Big) ^ {2} \end{array}\tag{2}
$$

Proposition 1 shows the SP's equilibrium strategies, and the pro<sup>fi</sup>t in the benchmark case.

Proposition 1. In the equilibrium of the benchmark case,

(1) a SP will invest in protective practices and the effectiveness is $\begin{array} { r } { x _ { i p } ^ { b } = \frac { 1 } { \alpha _ { n } } M v E [ q ] ; } \end{array}$

<sup>p</sup>(2) a SP charges its customers 2NnV NnvE q ${ \scriptstyle { \frac { 1 } { \alpha _ { n } } } } N ^ { 2 } n ^ { 3 } \nu ^ { 2 } { \mathrm { ( } } E [ q ] { \mathrm { ) } } ^ { 2 }$ for Internet services;

$$
(3) a S P ^ {\prime} s p r o f i t i s \pi_ {i} ^ {b} = 2 M V - M v E [ q ] + \frac {1}{2 \alpha_ {p}} (M v E [ q ]) ^ {2};
$$

Proof. Taking <sup>fi</sup>rst order derivative of Eq. (2), we can get $\begin{array} { r } { x _ { i p } ^ { b } = \frac { 1 } { \alpha _ { n } } M \nu E [ q ] } \end{array}$ . Condition 2 insures that this result falls in the interval (0,1). We can then obtain the optimal price p<sup>b</sup> and the SP's pro<sup>fi</sup>t π<sup>b</sup> by substitute $x _ { i p } ^ { b }$ into Eqs. (1) and (2). Condition (1) and (2) together ensure that the profit is positive. □

Proposition 1 shows that all the SPs will choose the same strategies and gain the same payoff, independent of their own types. In the following context, we suppress the subscript i and use x<sup>b</sup>, $p ^ { \mathrm { b } }$ , and $\pi ^ { \bar { \mathrm { b } } }$ to represent the SP's effectiveness of protective practices, prices, and pro<sup>fi</sup>ts, respectively, for the benchmark case.

In this case, no SP will invest in regulative practices. This is due to the public good nature of regulative practices. That is, investing in regulative practices will mainly reduce the other SPs' probability of receiving malicious traf<sup>fi</sup>c. Although all SPs suffer from the rampant malicious activities via the Internet, none has the incentive to eliminate the harmful code at its origin to bene<sup>fi</sup>t others. They only spend money to protect themselves.

## 4.2. The network with the certification mechanism

We now analyze the case where the certi<sup>fi</sup>cation mechanism is introduced. SPs decide whether to subscribe to certi<sup>fi</sup>cation services considering the bene<sup>fi</sup>t and the cost of following the rules speci<sup>fi</sup>ed by the certi<sup>fi</sup>cation provider. If they subscribe to certi<sup>fi</sup>cation services, they have to pay a subscription fee, t, and compensate for the loss caused by malicious traf<sup>fi</sup>c that they pass to their customers or other certi<sup>fi</sup>ed SPs. On the other hand, they can charge a higher price to their customers and solicit compensation whenever they are attacked by malicious traf<sup>fi</sup>c from other certi<sup>fi</sup>ed SPs.

## 4.2.1. Separating outcome

We <sup>fi</sup>rst analyze a possible separating outcome where only high-type SPs will subscribe to the certi<sup>fi</sup>cation program. The overall network is separated into two subnetworks, a certi<sup>fi</sup>ed network composed of all the high-type SPs and a noncerti<sup>fi</sup>ed network composed of all the low-type SPs. In a Bayesian equilibrium, the public belief on which SPs will subscribe is aligned with their actual decisions. Therefore, the public belief is that all the high-type SPs subscribe and hence the size of the certi<sup>fi</sup>ed network is δN and the non-certi<sup>fi</sup>ed network is of size (1−δ)N. To prove that this is an equilibrium outcome, we only need to show that a high-type SP <sup>fi</sup>nds it more pro<sup>fi</sup>table to get certi<sup>fi</sup>ed and a low-type SP chooses not to get certi<sup>fi</sup>ed under such a belief system. We use the superscript cs to denote the strategies and payoffs of a certi<sup>fi</sup>ed SP in the separating outcome. In contrast, we use the superscript ns for the non-certi<sup>fi</sup>ed SPs in the separating outcome.

We <sup>fi</sup>rst look at the pro<sup>fi</sup>tability of a certi<sup>fi</sup>ed SP. Since the certi<sup>fi</sup>cation mechanism imposes accountability on participating SPs, a certi<sup>fi</sup>ed SP will invest in regulative practices to reduce the malicious traf<sup>fi</sup>c in its outbound traf<sup>fi</sup>c. It has no incentive to scrutinize the inbound traf<sup>fi</sup>c sent from other certi<sup>fi</sup>ed SPs since it can always be compensated in case malicious traf<sup>fi</sup>c is detected. Regarding inbound traf<sup>fi</sup>c from non-certi<sup>fi</sup>ed SPs, certi<sup>fi</sup>ed SPs can choose either to completely block it or to invest in protective practices to <sup>fi</sup>lter the inbound traf<sup>fi</sup>c. We use the subscript k for the blocking case and f for the <sup>fi</sup>ltering case.

Lemma 1. If a certified SP of typeq invests in protective practices to filter inbound traffic coming from noncertified SPs, the effectiveness of protective practices is $x _ { p f } ^ { c s } = \alpha _ { p } M \nu q _ { l } ( 1 - \delta )$

Proof. A customer's expected willingness to pay to a certi<sup>fi</sup>ed SP i is 2VNn since she enjoys the risk-free two-way communication with other customers in both certi<sup>fi</sup>ed and non-certi<sup>fi</sup>ed networks. Certi<sup>fi</sup>ed SP i 's pro<sup>fi</sup>t is therefore

$$
\begin{array}{c} \pi_ {i f} ^ {c s} = 2 M V - M v \Big [ \Big (1 - x _ {i r f} ^ {c s} \Big) q _ {i} \delta + \Big (1 - x _ {i p f} ^ {c s} \Big) q _ {l} (1 - \delta) \Big ] \\ - C _ {p} \Big (x _ {i p f} ^ {c s} \Big) - C _ {r} \Big (x _ {i r f} ^ {c s} \Big) - t. \end{array}
$$

Optimizing the certi<sup>fi</sup>ed SP's pro<sup>fi</sup>t with respect to the degree of protective practices $x _ { i \mathrm { p f } } ^ { \mathrm { c s } }$ yields $\begin{array} { r } { x _ { i p f } ^ { c s } = \frac { 1 } { \alpha _ { n } } M \nu q _ { l } ( 1 - \delta ) } \end{array}$ Since the investment is independent of the SP's type q , we suppress the subscript i. □

Lemma 2. In the separating outcome, a certified $S P$ of type $q _ { i }$ invests in regulative practices and the effectiveness is $\begin{array} { r } { x _ { i r } ^ { c s } = \frac { 1 } { \alpha _ { r } } M \nu \delta q _ { i } } \end{array}$

Proof. If a certi<sup>fi</sup>ed SP <sup>fi</sup>lters inbound traf<sup>fi</sup>c sent from the non-certi<sup>fi</sup>ed network, it will choose a level of regulative investment $x _ { i \mathrm { r f } } ^ { . \mathrm { c s } }$ to maximize its pro<sup>fi</sup>t π <sup>cs</sup> (see proof of Lemma 1 for the equation).

If the $\mathrm { S P }$ decides to block the inbound traf<sup>fi</sup>c instead, its customer can only enjoy one-way communication to the noncerti<sup>fi</sup>ed network and hence their willingness to pay is VNn(1+δ). Certi<sup>fi</sup>ed SP $i : s$ pro<sup>fi</sup>t is then $\pi _ { i \mathrm { k } } ^ { \mathrm { c s } } = M \bar { V } ( 1 + \delta ) - \bar { M } \nu ( 1 - x _ { i \mathrm { r k } } ^ { \mathrm { c s } } ) q _ { i } \delta -$ $C _ { r } \big ( x _ { i \mathrm { r k } } ^ { \mathrm { \ c s } } \big ) - t .$ . Taking the <sup>fi</sup>rst order derivative of the pro<sup>fi</sup>t $\pi _ { i \mathrm { f } } ^ { \mathrm { c s } }$ and $\pi _ { i \mathrm { k } } ^ { \mathrm { c s } }$ over x <sup>cs</sup> and x <sup>cs</sup> respectively yields the same optimal effectiveness $\begin{array} { r } { \pmb { \chi } _ { i n f } ^ { \mathrm { c s } } = \pmb { \chi } _ { i r k } ^ { \mathrm { c s } } = \frac { 1 } { \alpha _ { r } } M \nu q _ { i } \delta , } \end{array}$ . We therefore suppress the subscript k and f.

Based on the optimal security investments in Lemma 1 and 2, we can calculate the pro<sup>fi</sup>t for a certi<sup>fi</sup>ed SP who blocks non-certi<sup>fi</sup>ed inbound traf<sup>fi</sup>c as

$$
\pi_ {i \mathrm{k}} ^ {\mathrm{cs}} = M V (1 + \delta) - M v \delta q _ {i} + \frac {1}{2 \alpha_ {\mathrm{r}}} (M v \delta q _ {i}) ^ {2} - t.
$$

If the SP decides to <sup>fi</sup>lter the inbound non-certi<sup>fi</sup>ed traf<sup>fi</sup>c, the pro<sup>fi</sup>t is then

$$
\begin{array}{l} \pi_ {i f} ^ {c s} = 2 M V - M v \delta (q _ {i} - q _ {h}) - M E [ q ] \\ \qquad + \frac {1}{2 \alpha_ {r}} (M v \delta q _ {i}) ^ {2} + \frac {1}{2 \alpha_ {p}} (M v (1 - \delta) q _ {l}) ^ {2} - t. \end{array}
$$

Comparing $\pi _ { i \mathrm { k } } ^ { \mathrm { c s } }$ to $\pi _ { i \mathrm { f } } ^ { \mathrm { c s } } ,$ , we obtain the optimal blocking strategy as described in the following Proposition 2.

Proposition 2. A certified service provider with type $q _ { i }$ will completely block the inbound traffic from a non-certified $S P$ if $\begin{array} { r } { V < \dot { \nu q _ { l } } - \frac { ( \dot { 1 } - \delta ) M \nu ^ { 2 } q _ { l } ^ { 2 } } { 2  { \alpha } _ { n } } . } \end{array}$ Otherwise, it will allow inbound traffic and invest in filtering it.

Proof. Subtracting $\pi _ { i \mathrm { k } } ^ { \mathrm { c s } }$ from $\pi _ { i \mathrm { f } } ^ { \mathrm { c s } }$ yields the difference $\begin{array} { r } { M V ( 1 - \delta ) - M \nu q _ { l } ( \overline { { 1 } } - \delta ) + \frac { 1 } { 2 \nu _ { - } } ( M \nu q _ { l } ( 1 - \delta ) ) ^ { 2 } \ } \end{array}$ . Imposing the difference to be negative, we can <sup>fi</sup>nd the condition when blocking is preferred. □

Proposition 2 distinguishes the value of communication V as the major criterion that a certi<sup>fi</sup>ed $\mathrm { S P }$ evaluates to decide whether to block the inbound traf<sup>fi</sup>c sent from a non-certi<sup>fi</sup>ed network. As V increases, the customers in the certi<sup>fi</sup>ed network suffer more when the communication with the non-certi<sup>fi</sup>ed network is blocked. In addition, the certi<sup>fi</sup>ed SP is inclined to block the non-certi<sup>fi</sup>ed inbound traf<sup>fi</sup>c if protective practices become relatively more expensive (i.e. larger $\alpha _ { \mathrm { { p } } } ) _ { \mathrm { { r } } }$ , the customers' disutility of malicious traf<sup>fi</sup>c becomes larger (i.e. larger v), the expected probability of attacks from the non-certi<sup>fi</sup>ed network increases (i.e. larger $q _ { 1 } ) ,$ , or the size of the non-certi<sup>fi</sup>ed network gets smaller (i.e., larger $\delta ) .$ . Following Proposition 2, we can rewrite the pro<sup>fi</sup>t function for a certi<sup>fi</sup>ed SP as follows:

$$
\pi_ {i} ^ {\mathrm{cs}} = \left\{ \begin{array}{l l} \pi_ {i k} ^ {\mathrm{cs}} & \text {if V <   vq_{l} - \frac {(1 - \delta) Nn^{2} v^{2} q_{l} ^{2}}{2\alpha_{p}}} \\ \pi_ {i f} ^ {\mathrm{cs}} & \text {if V\geq vq_{l} - \frac {(1 - \delta) Nn^{2} v^{2} q_{l} ^{2}}{2\alpha_{p}}}. \end{array} \right.
$$

It is also worth noticing that both $x _ { i \mathrm { r k } } ^ { \mathrm { { c s } } }$ and $x _ { i \mathrm { r f } } ^ { . \mathrm { c } _ { 3 } }$ increase in $q _ { i \cdot }$ Moreover, $\pi _ { i \mathrm { k } } ^ { \mathrm { c s } }$ and $\pi _ { i \mathrm { f } } ^ { \mathrm { c s } }$ decrease in $q _ { i \cdot }$ If a low-type SP subscribes to the certi<sup>fi</sup>cation services, it has to invest more in regulative practices than a high-type SP does because it has more potential malicious traf<sup>fi</sup>c originating from its network and has to try harder to detect the malicious traf<sup>fi</sup>c. Even so, the pro<sup>fi</sup>t of a certi<sup>fi</sup>ed low-type SP is still lower than that of a certi<sup>fi</sup>ed high-type SP. This result indicates that low-type SPs are more reluctant in participating in the certi<sup>fi</sup>cation program and implies a possible separating outcome.

If a SP does not participate in the certi<sup>fi</sup>cation program, it is not responsible for malicious traf<sup>fi</sup>c sent from its network and hence has no incentive to scrutinize its outbound traf<sup>fi</sup>c. It will only invest in protective practices for its own customers. Depending on whether certi<sup>fi</sup>ed SPs block traf<sup>fi</sup>c originated from the non-certi<sup>fi</sup>ed network, the pro<sup>fi</sup>t of a non-certi<sup>fi</sup>ed provider varies. Let $K ^ { s }$ be the indication variable for whether the certi<sup>fi</sup>ed SPs adopt the blocking strategy:

$$
K ^ {s} = \left\{ \begin{array}{l l} 1 & \text { if } V <   v q _ {1} - \frac {(1 - \delta) N n ^ {2} v ^ {2} q _ {1} ^ {2}}{2 \alpha_ {p}} \\ 0 & \text { if } V \geq v q _ {1} - \frac {(1 - \delta) N n ^ {2} v ^ {2} q _ {1} ^ {2}}{2 \alpha_ {p}}. \end{array} \right.
$$

We are then able to write down the expected pro<sup>fi</sup>t of a non-certi<sup>fi</sup>ed ${ \sf S P }$ (indexed by j) as follows:

$$
\begin{array}{c} \pi_ {\mathrm{j}} ^ {\mathrm{ns}} = M V (2 - K ^ {\mathrm{s}} \cdot \delta) - M v \delta q _ {\mathrm{h}} \big (1 - x _ {\mathrm{hr}} ^ {\mathrm{cs}} \big) \\ - M v (1 - \delta) q _ {\mathrm{l}} \Big (1 - x _ {\mathrm{jp}} ^ {\mathrm{ns}} \Big) - C _ {p} \Big (x _ {\mathrm{jp}} ^ {\mathrm{ns}} \Big), \end{array}
$$

where $x _ { \mathrm { j p } } ^ { \mathrm { n s } }$ is the effectiveness of protective practices the $\mathsf { S P } j$ controls and $x _ { \mathrm { h r } } ^ { \mathrm { c s } }$ is the effectiveness of regulative practices a high-type certi<sup>fi</sup>ed SP controls. In the second term of the above equation, we observe that a certi<sup>fi</sup>ed SP's regulative investment $x _ { \mathrm { h r } } ^ { \mathrm { c s } }$ positively affects the non-certi<sup>fi</sup>ed $\mathsf { S P } ^ { \prime } s$ pro<sup>fi</sup>t (i.e. positive externalities). Namely, a non-certi<sup>fi</sup>ed SP receives less malicious traf<sup>fi</sup>c from the certi<sup>fi</sup>ed subnetwork. In addition, non-certi<sup>fi</sup>ed SPs indirectly bene<sup>fi</sup>t from certi<sup>fi</sup>ed SPs' investment by saving investment in protective practices. As shown in the following Lemma 3, the effectiveness of protective practices is lower compared to the benchmark case.

Lemma 3. In the separating equilibrium, $\begin{array} { r } { x _ { j p } ^ { n s } = \frac { 1 } { \alpha _ { p } } M \nu ( 1 - \delta ) q _ { l } } \end{array}$

Proof. Taking <sup>fi</sup>rst order derivative of $\overline { { \pi _ { \mathrm { j } } ^ { \mathrm { n s } } } }$ over $x _ { \mathrm { j p } } ^ { \mathrm { n s } }$ will yield this result. □

The subscription fee (i.e. t) charged by the certi<sup>fi</sup>cation provider plays an important role in supporting the separating outcome considered in this section because only the certi<sup>fi</sup>ed SPs incur such a cost and hence the fee level directly affects the $S \mathrm { P } s ^ { \prime }$ incentives of getting certi<sup>fi</sup>ed. In this section, we examine all the possible fees without considering the pro<sup>fi</sup>tability of the certi<sup>fi</sup>cation program. That is, we allow negative fees. In Section 4.2.4, we consider the pro<sup>fi</sup>tability of the certi<sup>fi</sup>cation provider and focus on positive fees only.

Proposition 3. When $\begin{array} { r } { V { < } \nu q _ { l } - \frac { ( 1 - \delta ) N n ^ { 2 } \nu ^ { 2 } q _ { l } ^ { 2 } } { 2 \gamma _ { r } } , } \end{array}$ , a separating equilibrium exists if the certification $f e e \overrightharpoon { t } { \in } ( t _ { k 1 } ^ { s } , t _ { k 2 } ^ { s } ] .$ . Otherwise, the range of fees that supports the separating equilibrium will be $( t _ { f l } ^ { s } ,$ $t _ { f 2 } ^ { s } l .$ . The value of $t _ { k 1 } ^ { s } , t _ { k 2 } ^ { s } , t _ { f l } ^ { s } , t _ { f 2 } ^ { s }$ are:

$$
\begin{array}{l} t _ {\mathrm{k} 1} ^ {s} = M (V - v q _ {\mathrm{l}}) (2 \delta - 1) + M v \delta q _ {\mathrm{h}} + \frac {(M v) ^ {2}}{2} \left[ \frac {\delta^ {2}}{\alpha_ {\mathrm{r}}} - \frac {(1 - \delta) ^ {2}}{\alpha_ {\mathrm{p}}} \right] q _ {\mathrm{l}} ^ {2} \\ - \frac {(M v) ^ {2} \delta^ {2}}{\alpha_ {\mathrm{r}}} q _ {\mathrm{h}} ^ {2} \end{array}
$$

$$
\begin{array}{l} t _ {\mathrm{k2}} ^ {s} = M V (2 \delta - 1) + M v (1 - \delta) q _ {\mathrm{l}} \\ \quad - \frac {(M v) ^ {2}}{2} \left[ \frac {(\delta q _ {\mathrm{h}}) ^ {2}}{\alpha_ {\mathrm{r}}} + \frac {((1 - \delta) q _ {\mathrm{l}}) ^ {2}}{\alpha_ {p}} \right] \end{array}
$$

$$
t _ {\mathrm{f} 1} ^ {\mathrm{s}} = - M v \delta (q _ {\mathrm{l}} - q _ {\mathrm{h}}) + \frac {(M v \delta) ^ {2}}{2 \alpha_ {\mathrm{r}}} \left[ q _ {\mathrm{l}} ^ {2} - 2 q _ {\mathrm{h}} ^ {2} \right]
$$

$$
t _ {f 2} ^ {s} = - \frac {(M v \delta q _ {h}) ^ {2}}{2 \alpha_ {r}}.
$$

Proof. To support the separating equilibrium, the subscription fee t needs to be set at such a level that only high-type SPs <sup>fi</sup>nd it pro<sup>fi</sup>table to participate. That is, ${ \pi } _ { i } ^ { \mathrm { c s } } ( { q } _ { \mathrm { h } } , t ) - { \pi } _ { i } ^ { \mathrm { n s } }$ $( q _ { \mathrm { h } } ) { \geq } 0$ (ICh-s) and $\pi _ { i } ^ { c s } ( q _ { 1 , } t ) - \pi _ { i } ^ { \mathrm n s } ( q _ { 1 } ) < 0$ (ICl-s) should hold simultaneously.

(a) When $\begin{array} { r } { V { < } \nu q _ { l } - \frac { ( 1 - \delta ) N n ^ { 2 } \nu ^ { 2 } q _ { l } ^ { 2 } } { 2 \nu } , } \end{array}$ (ICh-s) yields the condition that $\begin{array} { r } { t \leq t _ { k 2 } ^ { s } = M \dot { V ( } 2 \delta - 1 ) ^ { - \alpha _ { p } } + M \dot { \nu ( } 1 - \dot { \delta ) } \dot { q } _ { l } - \frac { ( M \nu ) ^ { 2 } } { 2 } \Big [ \frac { ( \delta q _ { h } ) ^ { 2 } } { \varkappa _ { * } } + \frac { ( ( 1 - \delta ) q _ { l } ) ^ { 2 } } { \varkappa _ { * } } \Big ] } \end{array}$ and (ICl-s) yields the condition that $\stackrel { \angle } { t } { > } t _ { k 1 } ^ { s } \stackrel { \alpha _ { r } } { = } M ( V \stackrel { \alpha _ { p } } { - } \nu q _ { l } ^ { \mathrm { - } } )$ $\begin{array} { r } { ( 2 \delta - 1 ) + M \nu \delta q _ { h } + \frac { ( M v ) ^ { 2 } } { 2 } \sqrt { \frac { \delta ^ { 2 } } { \alpha _ { r } } - \frac { ( 1 - \delta ) ^ { 2 } } { \alpha _ { n } } } \big | q _ { l } ^ { 2 } - \frac { \scriptscriptstyle  {  { n } } ^ { 2 } \delta ^ { 2 } } { \alpha _ { r } } q _ { h } ^ { 2 } . } \end{array}$ . Since $\begin{array} { r } { t _ { k 2 } ^ { s } - t _ { k 1 } ^ { s } = M \nu \delta ( q _ { l } - q _ { h } ^ { - } ) |  ^ { | \mathfrak { s } _ { r }  } - \frac { M \nu \delta } { \alpha _ { r } } \frac { q _ { l } + q _ { h } } { 2 } | > 0 , } \end{array}$ , we prove that a range exists.

(b) When $\begin{array} { r } { V { \geq } \nu q _ { l } - \frac { ( 1 - \delta ) N n ^ { 2 } \nu ^ { 2 } q _ { l } ^ { 2 } } { 2 x _ { p } } , ( I C h - S ) } \end{array}$ yields the condition that $\begin{array} { r } { t \leq t _ { f 2 } ^ { s } = - \frac { ( M v \delta q _ { h } ) ^ { 2 } } { 2 \alpha _ { r } } , } \end{array}$ and (ICl-s) yields condition that $t { > } t _ { f 1 } ^ { s } =$ $\begin{array} { r } { - M \nu \delta ( q _ { l } - q _ { h } ) + \frac { ( M \nu \delta ) ^ { 2 } } { 2 x _ { r } } [ q _ { l } ^ { 2 } - 2 q _ { h } ^ { 2 } ] } \end{array}$ . Since $t _ { f 2 } ^ { s } - t _ { f 1 } ^ { s } \ = M \nu \delta$ $\begin{array} { r } { ( q _ { l } - q _ { h } ) \left[ 1 - \frac { M \nu \delta } { \alpha _ { r } } \frac { q _ { l } + q _ { h } } { 2 } \right] > 0 , } \end{array}$ , we prove that a range exists.

In summary, no matter whether $\begin{array} { r } { V { < } \nu q _ { l } - \frac { ( 1 - \delta ) N n ^ { 2 } \nu ^ { 2 } q _ { l } ^ { 2 } } { 2  { \alpha } _ { n } } } \end{array}$ or not, a <sup>p</sup>subscription fee range always exists which supports the separating equilibrium. □

4.2.2. Pooling outcome: if all SPs get certified

If all SPs subscribe to certi<sup>fi</sup>cation services, they will all invest in regulative practices to control outbound traf<sup>fi</sup>c and they do not need to deploy protective practices to <sup>fi</sup>lter inbound traf<sup>fi</sup>c from other certi<sup>fi</sup>ed SPs. Lemma 4 gives certi<sup>fi</sup>ed SPs' optimal strategies in the pooling outcome.<sup>5</sup>

Lemma 4. In the pooling outcome where all SPs are certified, the optimal strategies of a certified SP of type q<sub>i</sub> are as follows:

(1) it only invests in regulative practices and the level of effectiveness is $\begin{array} { r } { x _ { i r } ^ { c p } = \frac { 1 } { \alpha } M \nu q _ { i } ; { ^ 6 } } \end{array}$

<sup>r</sup>(2) it charges 2VNn to its customers for Internet access services;

(3) its profit is $\begin{array} { r } { \pi _ { i } ^ { c p } = 2 M V - M \nu q _ { i } + \frac { 1 } { 2 x _ { r } } ( M \nu q _ { i } ) ^ { 2 } - t . } \end{array}$

Proof. In a pooling equilibrium where all SPs get certi<sup>fi</sup>ed, a customer is fully insured to enjoy two-way communication with all the other customers. Therefore, the SP will set price as 2VNn. Including security investment, a SP with type $q _ { i }$ gains pro<sup>fi</sup>t $\pi _ { i } ^ { \mathrm { { c p } } } = 2 M V - M \nu ( 1 - \chi _ { i \mathrm { r } } ^ { \mathrm { { c p } } } ) q _ { i } - C _ { \mathrm { r } } ( \chi _ { i \mathrm { r } } ^ { \mathrm { { c p } } } ) - t$ . Taking <sup>fi</sup>rst order derivative over $x _ { i \mathrm { r } } ^ { \mathrm { { c p } } }$ yields optimal effectiveness $\textstyle { \frac { 1 } { \alpha _ { r } } } M \nu q _ { i }$ . With $x _ { i \mathrm { r } } ^ { \mathrm { c p } } ,$ , we can obtain π<sup>cp</sup>. □

In this case, the size of the non-certi<sup>fi</sup>ed network diminishes to dimension 0, leaving only the certi<sup>fi</sup>ed network. All SPs take the responsibility for security and focus on the relatively more effective regulative practices. They are indifferent with whether to block or <sup>fi</sup>lter the traf<sup>fi</sup>c which is sent from the non-certi<sup>fi</sup>ed network because adopting either strategy yields the same expected payoff in equilibrium. In this paper, we assume that they block to induce stronger subscription incentives. Lemma 5 predicts the optimal strategies for a SP who deviates from equilibrium and stays non-certi<sup>fi</sup>ed.

Lemma 5. $I f a S P$ deviates from the pooling equilibrium and stays non-certified, it will invest in protective practices and the effective is $\textstyle x _ { p } ^ { n p } = { \frac { 1 } { \alpha _ { p } } } n ^ { 2 } \nu q _ { l }$ and its profit is

$$
\begin{array}{l} \pi_ {i} ^ {n p} = (M + n ^ {2}) V - M v E [ q ] + \frac {1}{\alpha_ {r}} \Big [ (1 - \delta) (M v q _ {l}) ^ {2} + \delta (M v q _ {h}) ^ {2} \Big ] \\ \qquad + \left[ \frac {1}{2 \alpha_ {p}} - \frac {N}{\alpha_ {r}} \right] n ^ {4} v ^ {2} q _ {l} ^ {2}. \end{array}
$$

Proof. The proof can be directly calculated based on the proof of Lemma 4. □

When N is large, M≫n<sup>2</sup>. We therefore can simplify $\pi _ { i } ^ { \mathrm { n p } }$ using an approximate form $\pi _ { i } ^ { n p } = M V - M v E [ q ] + \frac { 1 } { v _ { \cdot } } \big [ ( 1 - \delta ) ( M v q _ { l } ) ^ { 2 } +$ $\delta ( \bar { M } \nu q _ { h } ) ^ { 2 } ]$ <sup>r</sup>. In the pooling equilibrium, both high-type and lowtype SPs should <sup>fi</sup>nd it optimal to acquire a certi<sup>fi</sup>cation, compared to one's expected pro<sup>fi</sup>t when it deviates. The subscription fee needs to be low enough to support such an incentive, as described in the following Proposition 4.

Proposition 4. The pooling equilibrium holds when

$$
t \leq t ^ {p} = M V - M v \delta (q _ {l} - q _ {h}) - \frac {1}{\alpha_ {r}} \left[ \delta (M v q _ {h}) ^ {2} + \left(\frac {1}{2} - \delta\right) (M v q _ {l}) ^ {2} \right].
$$

Proof. In the pooling equilibrium, all the SPs should <sup>fi</sup>nd it optimal to subscribe to the certi<sup>fi</sup>cation program. Since $\pi _ { i } ^ { \mathrm { c p } }$ decreases as $q _ { i }$ increases, and $\pi _ { i } ^ { \mathrm { n p } }$ stays the same for both

□

types, we only need to compare $\pi _ { i } ^ { \mathrm { c p } }$ and $\pi _ { i } ^ { \mathrm { n p } }$ when $q _ { i } = q _ { \mathrm { l } } ,$ , which yields the upper bound for the subscription fee t. □

## 4.2.3. The efficiency of the certification mechanism

The role of the certi<sup>fi</sup>cation provider is to induce SPs to join in the certi<sup>fi</sup>ed network where each is responsible for the malicious traf<sup>fi</sup>c generated by its own users. The above section provides different ranges of subscription fees that support the separating and pooling equilibria. The certi<sup>fi</sup>cation provider can be a non-pro<sup>fi</sup>t organization whose best interest is to induce the more effective security practices. Or, the certi<sup>fi</sup>cation provider can be self-interested and set a fee to maximize its total revenue. In this section, we will analyze the ef<sup>fi</sup>ciency level of different equilibria. We then in Section 4.2.4 analyze the pro<sup>fi</sup>tability of the certi<sup>fi</sup>cation provider.

Since the regulative practices are more ef<sup>fi</sup>cient than the protective practices, we can conclude that a pooling outcome where both high-type and low-type SPs subscribe to the certi<sup>fi</sup>cation program would be the most ef<sup>fi</sup>cient outcome. Now we de<sup>fi</sup>ne the ef<sup>fi</sup>ciency level (E) as the total pro<sup>fi</sup>t (excluding the subscription fee) gained by all the SPs. Then E in different cases can be calculated as follows:

$$
E ^ {b} = N \pi^ {b} = 2 N M V - N M v E [ q ] + \frac {N}{2 \alpha_ {n}} (M v E [ q ]) ^ {2} \quad (\text { Benchmarkcase })
$$

$$
\begin{array}{l} E ^ {s} = \delta N (\pi_ {h} ^ {c s} + t ^ {s}) + (1 - \delta) N \pi_ {l} ^ {n s} \\ = 2 M N V - M N v E [ q ] + \frac {N}{2 \varepsilon_ {p}} (M v (1 - \delta) q _ {l}) ^ {2} + \frac {N}{\alpha_ {r}} \left[ 1 - \frac {\delta}{2} \right] (M v \delta q _ {h}) ^ {2} \\ - \delta (1 - \delta) N K ^ {s} \left[ 2 M V - M v q _ {l} + \frac {(1 - \delta)}{2 \varepsilon_ {p}} (M v q _ {l}) ^ {2} \right] \end{array}
$$

(Separatingoutcome)

$$
\begin{array}{l} E ^ {p} = \delta N \pi_ {h} ^ {c p} + (1 - \delta) N \pi_ {l} ^ {c p} + N t ^ {p} \\ = 2 M N V - M N v E [ q ] + \frac {N}{2 \varkappa_ {r}} \left[ \delta (M v q _ {h}) ^ {2} + (1 - \delta) (M v q _ {l}) ^ {2} \right] \\ \text {(Poolingoutcome)} \end{array}
$$

Proposition 5. Comparing $E ^ { b } , E ^ { s } ,$ , and $E ^ { p } ,$ , we have $E ^ { p } { > } E ^ { b } , E ^ { p } { > } E ^ { s }$ and $\begin{array} { r } { \operatorname* { l i m } _ { \delta \to 1 } E ^ { s } = E ^ { p } } \end{array}$

Proof. The result can be derived from direct comparisons of the formulae of E<sup>b</sup>, E<sup>s</sup>, and E<sup>p</sup>. □

The pooling outcome is always better than the other two outcomes. The separating equilibrium can be relatively ef<sup>fi</sup>cient when δ is large enough, that is, when most of the SPs are high-type SPs and the size of the non-certi<sup>fi</sup>ed network is relatively small. In today's networking environment, this is generally true.

## 4.2.4. Profitability of certification provider

The remaining question is “who should assume the role of a certi<sup>fi</sup>cation provide $\cdot ? "$ Or more importantly, “what is the certi<sup>fi</sup>cation provider's objective?” From a social ef<sup>fi</sup>ciency point of view, the certi<sup>fi</sup>cation provider should induce the most ef<sup>fi</sup>cient outcome (i.e. the pooling outcome) to create a safe Internet. However, if the certi<sup>fi</sup>cation provider is concerned about its own pro<sup>fi</sup>t (i.e. the total revenue collected by the subscription fee), then it may <sup>fi</sup>nd it more pro<sup>fi</sup>table to induce the separating outcome. We will analyze the certi<sup>fi</sup>cation provider’s choice of the subscription fee to maximize its pro<sup>fi</sup>t and consequent equilibria in this section.

If the certi<sup>fi</sup>cation provider attempts to maximize pro<sup>fi</sup>t, it will only set a positive subscription fee. Lemma 6 shows whether the upper bounds of the ranges described in Propositions 3 and 4 are positive.

Lemma 6. $t ^ { p }$ and $t _ { k 2 } ^ { s }$ are both positive, and $t _ { f 2 } ^ { s }$ is negative.

## Proof.

(1) We <sup>fi</sup>rst show that $t ^ { \mathrm { p } }$ is positive: substituting $\delta = 0$ and $\delta = 1$ to $t ^ { \mathrm { p } }$ respectively, we know that $t ^ { \mathrm { p } } ( \delta \mathbf { = } 0 ) \mathrm { > } 0$ and $t ^ { \mathrm { p } }$ $\left( \delta \mathrm { = } 1 \right) \mathrm { > } 0 .$ . In addition, $\begin{array} { r } { \frac { \overline { { d t ^ { p } } } } { d \delta } = \left\lceil \frac { M ^ { 2 } \nu ^ { 2 } ( q _ { 1 } + q _ { \mathrm { h } } ) } { \alpha _ { \mathrm { r } } } - 1 \right\rceil [ M \nu ( q _ { 1 } - q _ { \mathrm { h } } ) ] \mathrm { i s } } \end{array}$ not a function of δ. We then conclude that $t ^ { \mathrm { p } } { > } 0$ for all $\delta \in [ 0 , 1 ] .$

(2) Next, we show that $t _ { \mathrm { k } 2 } ^ { s } { > } 0$ (when $\begin{array} { r } { V { < } \nu q _ { l } - \frac { ( 1 - \delta ) N n ^ { 2 } \nu ^ { 2 } q _ { l } ^ { 2 } } { \nu \cdot n } \big ) ; } \end{array}$ since we have $M V { > } \frac { 1 } { 2 } \alpha _ { r } { > } \frac { 1 } { { 2 } _ { \times } } \big ( M v q _ { h } \big ) ^ { 2 }$ and $\begin{array} { r } { V { < } V \bar { q } _ { l } - \frac { ( 1 - \stackrel { \angle \alpha } { \delta } ) ^ { 2 } N n ^ { 2 } \nu ^ { 2 } \dot { q } _ { l } ^ { 2 } } { 2 \alpha _ { p } } , } \end{array}$ <sup>2</sup> <sup>2 r</sup>we can rearrange the terms of $t _ { \mathrm { k } 2 } ^ { s }$

$$
\begin{array}{c} t _ {\mathrm{k2}} ^ {s} = M V (2 \delta - 1) + M v (1 - \delta) q _ {\mathrm{l}} - \frac {(M v) ^ {2}}{2} \left[ \frac {(\delta q _ {\mathrm{h}}) ^ {2}}{\alpha_ {\mathrm{r}}} + \frac {((1 - \delta) q _ {\mathrm{l}}) ^ {2}}{\alpha_ {\mathrm{p}}} \right] \\ = M V \delta - \frac {1}{2 \pi_ {\mathrm{r}}} (M v \delta q _ {\mathrm{h}}) ^ {2} + (1 - \delta) \left[ M v q _ {\mathrm{l}} - M V - \frac {(1 - \delta) (M v q _ {\mathrm{l}}) ^ {2}}{2 \pi_ {\mathrm{p}}} \right] > 0. \end{array}
$$

(3) $t _ { \mathrm { f } 2 } ^ { s }$ is negative, which is straight-forward.

Based on the result of Lemma $6 ,$ we conclude that only a pooling equilibrium will be induced by the certi<sup>fi</sup>cation provider if $\begin{array} { r } { V { \geq } V q _ { l } - \frac { ( 1 - \delta ) M n ^ { 2 } \nu ^ { 2 } q _ { l } } { 2 x _ { n } } , } \end{array}$ . The maximal price that can be charged is $t ^ { \mathrm { p } }$ <sup>p</sup>and the total pro<sup>fi</sup>t is $t ^ { \mathrm { p } } { \cdot } N .$ If $\begin{array} { r } { \bar { V } { < } \nu q _ { l } - \frac { ( 1 - \delta ) M n ^ { 2 } \nu ^ { 2 } q _ { l } } { \nu } , } \end{array}$ the certi<sup>fi</sup>cation provider may choose to charge $t ^ { \mathrm { p } } \left( \mathrm { p r o f i t } ^ { \mathrm { \tiny { e p } } } { \cdot } N \right)$ or $t _ { \mathrm { k } 2 } ^ { s }$ (pro<sup>fi</sup>t $t _ { \mathrm { k } 2 } ^ { S } { \cdot } \delta N )$ depending which is more pro<sup>fi</sup>table.

Proposition 6. When $\begin{array} { r } { V { < } \nu q _ { l } - \frac { ( 1 - \delta ) M n ^ { 2 } \nu ^ { 2 } q _ { l } } { \nu } } \end{array}$ , there exist two critical values, $\delta _ { 1 }$ and $\delta _ { 2 }$ such that $0 { < } \delta _ { 1 } { < } \delta _ { 2 } { < } 1$ , and:

1) The certification provider sets $t = t ^ { p }$ and all the SPs will subscribe $i f \delta { \in } [ 0 , \delta _ { 1 } ) ;$

2) The certification provider sets $t = t _ { k 2 } ^ { s }$ and only high-type SPs will subscribe $i f \delta \in [ \delta _ { 2 } , 1 ) .$

Proof. De<sup>fi</sup>ne $\Pi ^ { \mathsf { p } } = t ^ { \mathsf { p } } N$ and $\Pi ^ { s } \substack { = t _ { \mathrm { k } 2 } ^ { s } \delta N }$ as the certi<sup>fi</sup>cation provider's pro<sup>fi</sup>t. Moreover, de<sup>fi</sup>ne $\begin{array} { r } { \Delta = \Pi ^ { \mathsf { p } } - \Pi ^ { \mathsf { s } } . } \end{array}$ . It can be shown that $\scriptstyle \operatorname* { l i m } _ { \delta \to - \infty } \varDelta < 0$ $\Delta ( \delta \mathbf { \varepsilon } = \mathbf { 0 } ) > 0$ $\Delta ( \delta \mathbf { \bar { \Gamma } } ^ { } ( \delta \mathbf { \bar { \Gamma } } ^ { } 1 ) < 0$ and lin $1 _ { \delta  + \infty } \Delta { > } 0$ <sup>lim</sup>. In addition, Δ is continuous in δ and the highest <sup>lim</sup>order is $\delta ^ { 3 } .$ . Hence, there exists only one $\bar { \delta } \in ( 0 , 1 )$ such that $\Delta ( \bar { \delta } ) { = } 0 . \mathrm { I f } \delta { \in } [ 0 , \bar { \delta } ) ,$ , then $\Delta ( \delta ) { > } 0$ and the pooling outcome is more pro<sup>fi</sup>table. If $\delta \in ( \bar { \delta } , 1 ]$ then $\Delta ( \delta ) { < } 0$ and the separating outcome is preferred.

In order to successfully induce the pooling (separating) outcome, we also need to have $t ^ { \mathrm { p } } { > } t _ { \mathrm { k } 2 } ^ { \mathrm { s } } \left( t ^ { \mathrm { p } } { < } t _ { \mathrm { k } 2 } ^ { \mathrm { s } } \right)$ . De<sup>fi</sup>ne $\Delta ^ { \prime } = t ^ { \mathrm { p } } - t _ { \mathrm { k } 2 } ^ { s } .$ We have that $\Delta ^ { \prime } ( \delta \mathbf { = } 0 ) { > } 0 , \Delta ^ { \prime } ( \delta \mathbf { = } 1 ) { < } 0$ , and $\Delta ^ { \prime }$ is strictly convex. Hence there exists a ${ \hat { \delta } } \in ( 0 , 1$ )such that $\Delta ^ { \prime } ( \hat { \delta } ) { = } 0$ . We can also conclude that $\widehat { \delta } { < } \bar { \delta }$ since $\Delta ( \hat { \delta } ) = t ^ { \mathrm { p } } ( \hat { \delta } ) N - t _ { \mathrm { k 2 } } ^ { \mathrm { s } } ( \hat { \delta } ) \cdot \delta N = N [ \Delta ^ { \prime } ( \hat { \delta } ) +$ $( 1 - \hat { \delta } ) { \cdot } t _ { \mathrm { k } 2 } ^ { s } ( \hat { \delta } ) ] = N { \cdot } ( 1 - \hat { \delta } ) { \cdot } t _ { \mathrm { k } 2 } ^ { s } ( \hat { \delta } ) > 0$ . De<sup>fi</sup>ne $\delta _ { 1 } = \widehat \delta$ and $\delta _ { 2 } = \bar { \delta }$ , we can̄ draw the conclusion of Proposition 6. When $\delta \in [ \hat { \delta } , \bar { \delta } ]$ , the certi<sup>fi</sup>cation provider may not be able to induce the more pro<sup>fi</sup>table pooling equilibrium since a separating equilibrium can also exists in that subscription fee range. □

Proposition 6 shows that the certi<sup>fi</sup>cation provider will induce the separating outcome only when the number of high-type SPs is large enough. Proposition 5 shows that the ef<sup>fi</sup>ciency level of the separating outcome is high if δ is large. Therefore, we believe a pro<sup>fi</sup>t-maximizing certi<sup>fi</sup>cation provider will still induce some level of ef<sup>fi</sup>ciency in our proposed structure.

## 5. Discussion and conclusion

This research examines the Internet architecture and address Internet security issues from an economic perspective. We propose a certi<sup>fi</sup>cation mechanism to induce SPs to exert collective efforts and improve Internet security. To be more speci<sup>fi</sup>c, the proposed mechanism provides certi<sup>fi</sup>ed SPs incentives to deploy regulative practices. We use a gametheoretic model to examine the ef<sup>fi</sup>ciency of our mechanism. The results show that our mechanism can increase the ef<sup>fi</sup>ciency for all the Internet Service Providers. By providing SPs with appropriate incentives, our mechanism can create a better communication environment over the Internet.

The challenging issue is, who should be the certification provider? The certi<sup>fi</sup>cation provider can be a non-pro<sup>fi</sup>t institution, such as Internet Corporation for Assigned Names and Numbers (ICANN). ICANN is a central authority with limited power in the essentially decentralized and neutral global network. However, its functions are restricted to running the addressing system, giving out blocks of unique identi<sup>fi</sup>ers to countries and private registries. Commentators have suggested ICANN should play an enhanced role in governing the unregulated Internet. By providing certi<sup>fi</sup>cation services, it introduces a soft regulation to the Internet, characterized by the fact that participation is voluntary, and participants choose their actions based on self-interest. The certi<sup>fi</sup>cation provider can also be a forpro<sup>fi</sup>t organization. The previous analysis examines the certi<sup>fi</sup>cation provider's pro<sup>fi</sup>t and discusses its impact on the overall ef<sup>fi</sup>ciency level.

One concern of our proposed mechanism is that if the certi<sup>fi</sup>ed network completely blocks inbound traf<sup>fi</sup>c sent from the non-certi<sup>fi</sup>ed network, then the overall network will suffer. Our result shows that blocking is an optimal strategy in the separating outcome only when the value of communication V is relatively low compared to the disutility caused by the malicious attack. In the pooling outcome, everyone will join the certi<sup>fi</sup>ed network and “blocking” is only a threat to those who deviate. Alternatively, we suggest the certi<sup>fi</sup>ed SPs consider strategies such as slowing down the incoming traf<sup>fi</sup>c sent from non-certi<sup>fi</sup>ed networks to deteriorate the noncerti<sup>fi</sup>ed SPs' payoff. However, due to the network interdependency, the certi<sup>fi</sup>ed SPs will also suffer from such a strategy. How to provide the certi<sup>fi</sup>ed SPs proper incentives to “punish” those non-certi<sup>fi</sup>ed ones deserves further study.

This paper characterizes the effectiveness of security practices using a single parameter, x, representing the false negative<sup>7</sup>. In most control settings, both false negatives and false positives are used to describe the effectiveness of security practices. Since regulative practices generally outperform protective practices in reducing errors, the analysis and results considering both false positive and false negative will be similar.

The implementation of the certi<sup>fi</sup>cation mechanism may generate extra overhead to identify the service providers certi<sup>fi</sup>cation status. We ignored such an impact in our model by assuming that the size of overhead is negligible compared to the regular traf<sup>fi</sup>c. In situations that the assumption does not hold, we suggest the certi<sup>fi</sup>cation provider to adjust the subscription fee to accommodate the overhead cost. Although the overhead will create a deadweight loss which reduces the value of the certi<sup>fi</sup>cation mechanism, the loss is inevitable as no security mechanism is free. Given the rising concerns on security, the overhead should not stop the implementation of the certi<sup>fi</sup>cation mechanism.

The main contribution of our paper is to propose a new incentive framework to the management of network security. Compared to the current Internet infrastructure which is open to everyone and consequently leaves everyone exposed to the security risks, our vision of the Internet is one where all the active parties (e.g. the service providers) should work collectively as a whole to detect potential security risks and eliminate the possible damage at the earliest stage. Our proposed framework also suggests possible exclusion of the incompetent service providers who cannot afford to make such an endeavor under certain conditions. Such a proposal may sound controversial from an idealistic point of view. However, it can induce those competent service providers to take more active actions in safeguarding the Internet, providing the individual users a worry-free environment. Our analytical results prove that the framework produces more ef<sup>fi</sup>ciency for Internet communication.

## Acknowledgements

We thank Dr. Manoj Parameswaran from the Department of Operations & Management Information Systems in Santa Clara University for his insightful comments, Dr. Ashish Arora from Carnegie Mellon University for suggesting us to clarify the novelty of our game-theoretic model, Dr. Ruhal Telang from Carnegie Mellon University for providing us helpful references. We also thank Dr. Vitaly Shmatikov, Dr. Benjamin J. Kuipers, Dr. Mohamed G. Gouda, and Dr. Lili Qiu from the Department of Computer Sciences at the University of Texas at Austin, Dr. Claire Vishik from Intel, John S. Quarterman from InternetPerils, Inc., as well as seminar participants at the University of Texas at Austin, the Fourth Workshop on eBusiness at Las Vegas, the Sixteen Workshop of Information Technologies and Systems at Milwaukee. We are responsible for all possible errors.

## References

[1] R. Anderson, T. Moore, The economics of information security, Science 314 (October 2006) 610–613.

[2] T. August, T. Tunca, Network software security and user incentive, Management Science 52 (11) (2006) 1703–1720.

[3] H. Ballani, P. Francis, X. Zhang, A study of pre<sup>fi</sup>x hijacking and interception of the Internet, Proceedings of ACM SIGCOMM 2007, August 2007.

[4] H. Cavusoglu, B. Mishra, S. Raghunathan, A model for evaluation IT security investments, Communications of the ACM 47 (7) (2004) 87–92.

[5] H. Chan, D. Dash, A. Perrig, H. Zhang, Modeling adaptability of secure BGP protocols. Proceedings of ACM SIGCOMM 2006. September 2006

[6] G. Goodell, W. Aiello, T. Grif<sup>fi</sup>n, J. Ioannidis, P. McDaniel, A. Rubin, Working around BGP: an incremental approach to improving security and accuracy in interdomain routing, Proceedings of Symposium on Network and Distributed System Security (NDSS'03), February 2003.

[7] L.A. Gordon, M.P. Loeb, The economics of information security investment, ACM Transactions on Information and System Security 5 (4) (2002) 438–457.

[8] Y.-C. Hu, A. Perrig, M. Sirbu, SPV: Secure patch vector routing for securing BGP, Proceedings of ACM SIGCOMM 2004, September 2004.

[9] C.D. Huang, Q. Hu, R. Behara, Economics of information security investment in the case of simultaneous attacks, Proceedings of the Workshop on the Economics of Information Security (WEIS2006), (Cambridge, UK, 2006.

[10] Y. Huang, X. Geng, A.B. Whinston, Defeating DDoS attacks by <sup>fi</sup>xing the incentive chain, ACM Transactions on Internet Technology 7 (2) (2007).

[11] K. Kannan, R. Telang, Market for software vulnerabilities? Think again”, Management Science 51 (5) (2005) 726–740.

[12] S. Kent, C. Lynn, J. Mikkelson, K. Seo, Secure border gateway protocol (S-BGP) — real world performance and deployment issues. Proceedings of the Network and distributed Systems Security Symposium (NDSS 2000), February 2000, pp. 103–116, San Diego, CA.

[13] S. Kent, C. Lynn, K. Seo, Security border gateway protocol (S-BGP), IEEE Journal of Selected Areas in communications 18 (4) (April 2000) 582–592.

[14] H. Kunreuther, G. Heal, Interdependent security, Journal of Risk and Uncertainty 26 (2/3) (2003) 231–249.

[15] D. Lichtman, E. Posner, Holding Internet Service Providers accountable, John M. Olin Law & Economics Working Paper No. 217, http://ssrn.com/ abstract\_id=573502, (2004).

[16] H. Ogut, N. Menon, S. Raghunathan, Cyber insurance and IT security investment: impact of interdependent risk. Proceedings of the Workshop on the Economics of Information Security (WEIS2005), Harvard University. Cambridge. MA. 2005

[17] M. Parameswaran, X. Zhao, A.B. Whinston, F. Fang, Reengineering the Internet for better security, IEEE Computer 40 (1) (2007) 40–44 (January 2007).

[18] H.R. Varian, H.R. Managing online security risks, NY Times, http://www. ischool.berkelev.edu/\~hal/people/hal/NYTimes/2000-06-01.html. (2000).

[19] R. White, Securing BGP through secure origin BGP, Technical Report, Cisco Internet Protocol Journal, September 2003.

Xia Zhao is a research fellow at the Tuck School of Business, Dartmouth College. Her research interests include electronic commerce, Internet security, and electronic communities. Zhao received her PhD in Information Systems from the University of Texas at Austin. Contact her at xia.zhao@dartmouth.edu.

Fang Fang is an assistant professor in the College of Business Administration at California State University San Marcos. Her research interests include knowledge markets, <sup>fi</sup>nancial markets, and network <sup>fi</sup>nance. Fang received her PhD in Information Systems from the University of Texas at Austin. Contact her at fangfang@csusm.edu.

Andrew B. Whinston is the Hugh Roy Cullen Centennial Chair Professor in Information Systems at the Graduate School of Business in the University of Texas at Austin, where he also teaches economics and computer science and directs the Center for Research in Electronic Commerce. His research interests include electronic commerce, knowledge management, online auctions, and <sup>fi</sup>nancial markets. Whinston received a PhD in management from Carnegie Mellon University. Contact him at abw@uts.cc.utexas.edu.
