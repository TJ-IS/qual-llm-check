---
otero_id: 10678
otero_key: "VQZ5YDFG"
title: "Optimal Launch Timing of Bug Bounty Programs for Software Products under Different Licensing Models"
authors: "Nan Feng; Tianlu Zhou; Haiyang Feng; Minqiang Li"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00843"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Optimal Launch Timing of Bug Bounty Programs for Software Products under Different Licensing Models

Nan Feng , fengnan@tju.edu.cn

Tianlu Zhou , imis\_ztl@tju.edu.cn

Haiyang Feng , hyfeng@tju.edu.cn

Minqiang Li , mqli@tju.edu.cn

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Optimal Launch Timing of Bug Bounty Programs for Software Products under Different Licensing Models

Nan Feng,<sup>1</sup> Tianlu Zhou,<sup>2</sup> Haiyang Feng,<sup>3</sup> Minqiang Li<sup>4</sup>

<sup>1</sup>College of Management and Economics / Laboratory of Computation and Analytics of Complex Management Systems (CACMS), Tianjin University, China, fengnan@tju.edu.cn

<sup>2</sup>College of Management and Economics, Tianjin University, China, imis\_ztl@tju.edu.cn <sup>3</sup>College of Management and Economics, Tianjin University, China, hyfeng@tju.edu.cn <sup>4</sup>College of Management and Economics, Tianjin University, China, mqli@tju.edu.cn

## Abstract

An increasing number of software firms are utilizing bug bounty programs (BBPs) to detect bugs and enhance their product quality by leveraging the contributions of external ethical hackers. Although launching a BBP involves bounties as well as the costs of processing bug reports and fixing bugs, software firms can save failure costs and enjoy the benefits of greater user trust. The costs and benefits resulting from launching a BBP vary with launch timings and software licensing models. Hence, we investigate the optimal BBP launch strategies for software firms, using perpetual or subscription licensing models. Our findings reveal that under perpetual licensing, the firm has only two viable launch strategies: simultaneous launch, i.e., launching the software and the BBP simultaneously, and no launch. Under subscription licensing, however, delayed launch, i.e., launching the BBP later than the software release time, occurs as the optimal strategy when the failure cost is not high and the benefit of user trust is significant. Two distinct patterns in the relationship between the firm’s bug-fixing capability and its payoff are identified: a U-shaped pattern and an inverted U-shaped pattern. We uncover the conditions under which a firm should opt not to launch a BBP as its bug-fixing capability improves. This study offers insights into how firms can be motivated to launch BBPs to improve the overall reliability of their software.

Keywords: Bug Bounty Program, Launch Timing, Software Licensing Model, Ethical Hacker

Lior Fink was the accepting senior editor. This research article was submitted on May 31, 2023 and underwent two revisions. Haiyang Feng is the corresponding author.

## 1 Introduction

The ubiquity of the internet and related technologies has led to countless malicious cyberattacks and catastrophic economic losses. Furthermore, the COVID-19 pandemic compelled people to spend most of their time at home, significantly augmenting their reliance on internet communication and consequently escalating the frequency of cybersecurity incidents. The Cyber Division of the FBI receives up to 4,000 complaints about cyberattacks every day, a 400% increase above prepandemic levels (Miller, 2020). Thus, an ongoing challenge faced by firms and public-sector entities is how to mitigate the economic losses caused by cyberattacks, particularly given limited security budgets.

Recently, bug bounty programs (BBPs), which reward external ethical hackers for reporting valid software vulnerabilities, have gained popularity among software firms. Many well-known IT firms, including Microsoft, Tencent, Alibaba, and Facebook, have launched BBPs for various software products on bug bounty platforms (e.g., HackerOne). For instance, Microsoft has launched BBPs not only for consumer software, such as Microsoft 365, but also for industrial software, including Microsoft

Dynamics 365 and Azure cloud services (Microsoft, 2023). Mark Zuckerberg, the CEO of Facebook, emphasized the importance of BBPs, stating that “bounty programs are an important part of the security arsenal for hardening many systems” (Alfred, 2018).

Despite the merits of BBPs, many firms remain hesitant to implement such programs. The main reason is that after a BBP is launched, firms incur costs for processing bug reports and providing rewards for valid reports, which can become significant. Additionally, the rate of valid bug reports may be lower than anticipated. For instance, in 2022, Facebook paid more than US\$2 million to ethical hackers and issued bounties on approximately 750 valid reports out of 10,000 submissions, resulting in a 7.5% validity rate (Oren, 2022). Furthermore, firms make varying decisions regarding the timing of BBP launches. Microsoft, for instance, launched a BBP simultaneously with its operating system, Windows 10 (Microsoft, 2023). Grammarly, a firm that provides AI-powered writing assistant software, launched a BBP later than the software (HackerOne, 2023). Tencent also adopted a delayed launch strategy for its online meeting software (Tencent, 2020). When determining the launch time for a BBP, there are several essential trade-offs to consider. On the one hand, by launching a BBP and receiving bug reports early, the firm can reduce failure costs. On the other hand, an early BBP launch increases the bug bounty rewards as well as the cost of processing bug reports. Thus, the first research question we aim to address is: Under what conditions should a software firm launch a BBP, and what is the optimal launch time?

Firms that choose to launch BBPs offer hefty monetary rewards for detecting existing bugs (Culafi, 2021), conveying to users their high level of security responsibility and confidence in their software safety in the hope that users will be persuaded to purchase various software services. For example, OVHcloud, a cloud service provider, offers bug bounties as an added trust element for their customers (Levrard, 2020). In this paper, we refer to the benefits derived by a software firm from users’ increased trust resulting from a BBP as the benefit of trust. In practice, there is a natural difference between the benefit of trust gained through launching a BBP under different licensing models. Firms that offer software products via perpetual licensing (e.g., Office 2021) benefit from the increased trust only when consumers make one-time purchases. Subscription-based software products (e.g., Microsoft 365), however, can profit from the increased trust repeatedly because consumers make subscription renewal decisions and repeatedly purchase valueadded services. Therefore, software firms’ optimal launch strategies for BBPs may vary under different licensing models. Thus, the second research question of this study is: How does the licensing model impact the firm’s launch strategies for a BBP?

Although ethical hackers may report an enormous number of valid bug reports, many firms do not fix all reported bugs (e.g., Morris, 2020). The number of fixed bugs, which is also referred to as the firm’s bugfixing capability in this study, has a significant impact on running a BBP. For one thing, the lack of a bugfixing capability harms a BBP’s performance and results in only a small increase in software reliability. Another issue is that a low bug-fixing capability disappoints ethical hackers, causing some to refuse to engage with the firm. For example, Apple has a massive backlog of bugs that have not been fixed, which has discouraged some security researchers from pointing out flaws to the company (Albergotti, 2021). Hence, the final research question that we plan to address is: How does the bug-fixing capability affect the firm’s optimal BBP launch strategies, and what is the theoretically optimal bug-fixing capability?

We develop a continuous-time model to analyze the software firm’s optimal launch strategies for a BBP under subscription and perpetual licensing models. Our analytical results lead to several intriguing findings. First, under perpetual licensing, the firm should opt for one of two launch strategies, depending on the failure cost and benefit of trust. When either the failure cost or the benefit of trust is high, the firm should launch the software and the BBP simultaneously; otherwise, it should not launch the BBP. Second, a third launch strategy becomes viable under subscription licensing. The firm should launch the BBP after the software release when the failure cost is not high and the benefit of trust is significant. Finally, we identify two patterns (i.e., a U-shaped pattern and an inverted U-shaped pattern) in the impact of the bug-fixing capability on the firm’s payoff gained from launching the BBP. When the bug bounty reward is high, the impact of the bug-fixing capability on the firm’s payoff follows a U-shaped pattern, and the firm should opt to launch the BBP when the bug-fixing capability is either low or high. However, when the bug bounty reward is low, we observe an inverted U-shaped pattern. In this case, an excessively high bug-fixing capability incentivizes the firm to cancel the launch of a BBP. These findings have significant managerial implications for firms that aim to harness the expertise of ethical hackers to enhance the reliability of their consumer or industrial software products.

The remainder of this paper is organized as follows. The next section provides a review of the related literature. Section 3 presents a continuous-time model that captures the costs and benefits of launching BBPs for software firms. The optimal launch strategies of BBPs under the two licensing models are determined and compared in Section 4. Section 5 concerns a special case used to examine the impact of the bug-fixing capability on the launch strategies of BBPs. Finally, Section 6 provides a summary of the extensions, theoretical contributions, practical implications, and future research directions.

## 2 Literature Review

This study is related to four research streams that we review below. The first stream focuses on information security investments. Gordon and Loeb (2002) put forward a classical economic security model to investigate the optimal security investment level. Gal-Or and Ghose (2005) examined the competitive implications of sharing security information and investments in security technologies. They found that security technology investments and information sharing acted as “strategic complements” in equilibrium. Cavusoglu et al. (2008) and Huang and Behara (2013) considered how the hacking modes of hackers affected security investment strategies. Li et al. (2021) examined the effects of information security investments on organizational security breaches. In addition, some papers have explored how firms invest in security services, such as security outsourcing (Cezar et al., 2014; Feng et al., 2020; Wu et al., 2021) and cyberinsurance services (Zhao et al., 2013), to protect against security breaches and losses caused by external hackers. Our paper differs from this stream of literature by focusing on investments in BBPs to incentivize a large number of external ethical hackers to detect and report software bugs.

The second related stream of literature concerns BBPs. Most of the recent research has focused on BBPs’ performance (e.g., Maillart et al., 2017; Subramanian & Malladi, 2020; Walshe & Simpson, 2020; Aaltonen & Gao, 2021; Zhou & Hui, 2021; Zhou & Hui, 2022). For instance, Maillart et al. (2017) examined the strategic interactions among BBP managers and participants. They confirmed that the engagement of large crowds of researchers indeed benefits a BBP, whereas each security researcher can expect to discover only a bounded number of bugs. Zhou and Hui (2021) analyzed the economic, security, and social welfare implications of BBPs. They showed that BBPs are economically beneficial to launch under certain conditions and can enhance firms’ overall security. Further, some research has focused on the optimal policies to manage a BBP. In this regard, Zhao et al. (2017) introduced and examined policies of allocating hackers to different BBPs and incentivizing hackers to validate their bug reports before submitting them. In contrast to the existing literature, the present study takes a novel approach by investigating the optimal launch timing of BBPs under different software licensing models.

The third stream of literature focuses on how different software testing strategies improve software reliability. The majority of previous research in this stream has focused on the effects of internal testing on increasing software reliability (e.g., Dalal & Mallows, 1988; Ji et al., 2005; Arora et al., 2006; Kim et al., 2009; Jiang et al., 2012; Dey et al., 2015, Ghoshal et al., 2017). In addition, external testing, which is closely related to the present study, has been investigated. For instance, August and Marius (2013) analyzed the impact of user error reporting on software reliability and investigated the optimal timing of software releases. Jiang et al. (2017) considered reliability-related and market-related benefits to determine the optimal duration of public beta testing by developing a software reliability growth model. Mehra and Saha (2018) found that introducing public beta testing does not necessarily result in a higher-quality product. Unlike the testing methods considered in these prior studies (i.e., public beta testing or customer error reporting), our analysis focuses on the specific positive contributions and potential challenges posed by external ethical hackers in enhancing software reliability.

The fourth stream of relevant literature focuses on the comparison of subscription and perpetual licensing models. Prior studies have analyzed how to choose optimal software licensing models (Zhang & Seidmann, 2010; Li, 2017; Xin, 2020). Other studies have investigated the competition between firms under subscription licensing and perpetual licensing (Fan et al., 2009; Ma & Seidmann, 2015; Guo & Ma, 2018). Software quality under the two licensing models has also attracted the attention of researchers. For example, Choudhary (2007) finds that a vendor’s incentive to invest in quality under the software as a service (SaaS) model is higher than that under perpetual licensing. Choudhary and Zhang (2015) examine a vendor’s choice of when to release software and the proportion of software defects to fix. They found that SaaS vendors often release software earlier with more defects than on-premises software vendors. To the best of our knowledge, this is the first study to examine the optimal launch strategies of BBPs under the two different licensing models. We consider the fact that the software firm could gain greater user trust because of the launch of BBPs and capture the difference between the benefits of trust gained under subscription and perpetual licensing models.

## 3 Model

Consider a firm that supports a software service until time $T > 0$ . The firm determines the launch time of a BBP, denoted by $t _ { 0 } \in [ 0 , T ]$ . Beyond ??, the firm stops almost all software services, particularly software security patches. Microsoft, for instance, ended Windows XP support, including technical assistance and security updates, on April 8, 2014 (Hruska, 2019).

The motivation for ethical hackers to participate in BBPs is twofold: the bounty and the anticipated sense of accomplishment. Ethical hackers earn bug bounties directly by reporting valid (unique and replicable) bugs; we denote the reward for each valid bug report by $c _ { r }$ Ethical hackers also participate in BBPs to achieve a sense of accomplishment, gained from helping firms fix bugs and improve software reliability. A BBP with a lower bug-fixing rate is less likely to provide hackers with a sense of accomplishment. In practice, ethical hackers can track firms’ bug-fixing rate/capability by examining the status of their reported bugs or browsing hacker forums (e.g., Robinhouston, 2019) and may reject bug bounty offers when the software firms fail to patch bugs promptly (e.g., Sharma, 2021). Thus, if the software firm has the capability to fix more bugs per unit time, ethical hackers will achieve a greater sense of accomplishment. To capture these two motivations of ethical hackers, we assume that the payoff obtained by each ethical hacker from participating in the BBP, denoted by ??, increases with the bounty size $c _ { r }$ as well as the number of fixed bugs (per unit time), denoted by ??. Hence, we make the following assumption in this study.

$$
\text { Assumption   1: } \frac {\partial r}{\partial c _ {r}} > 0 \text { and } \frac {\partial r}{\partial f} > 0.
$$

Ethical hackers are heterogeneous in their opportunity costs of participating in the BBP. Some incur significant costs in testing software, while others expend considerable effort in editing readable bug reports. Thus, it is assumed that an ethical hacker’s opportunity cost of participating in the BBP, denoted by $c _ { h } ,$ follows a uniform distribution over [0, 1], that is, $c _ { h } { \sim } U [ 0 , 1 ]$ . In sum, the net payoff derived by an ethical hacker is formulated as:

$$
\pi_ {h} = r - c _ {h}.\tag{1}
$$

Let $\hat { c } _ { h }$ denote the marginal ethical hacker who is indifferent between participating in the BBP and not; thus, we have $\hat { c } _ { h } = r$ . As shown in Figure 1, any ethical hacker to the left of the indifferent hacker participates in the BBP, whereas anyone to the right does not.

In this study, we normalize the total number of potential ethical hackers to 1 and the number of participating ethical hackers is thus given by:<sup>1</sup>

$$
n _ {h} = \hat {c} _ {h}.\tag{2}
$$

Following Jiang et al. (2017), we assume that every ethical hacker tests the software independently, and the average number of bug reports submitted by each ethical hacker (per unit time) is denoted by ??. Here, the total number of bug reports submitted by the participating ethical hacker per unit time can be written as $n _ { h } \theta$ . Only a proportion of these submitted reports are valid, and thus, we let ?? represent the validity rate of bug reports submitted by the ethical hackers. A larger number of participating ethical hackers with more submitted bug reports per unit time leads to a lower validity rate (that is, a higher repetition rate).

Therefore, we assume that the validity rate of bug reports $\xi$ decreases with $n _ { h }$ and $\theta ;$ that is:

Assumption 2: $\begin{array} { r } { \frac { \partial \xi } { \partial n _ { h } } < 0 \ : a n d \frac { \partial \xi } { \partial \theta } < 0 . } \end{array}$

For simplicity, all ethical hackers are assumed to make participation decisions at the BBP launch time $t _ { 0 }$ . We then denote the number of valid bugs reported by participating ethical hackers by time $t \in [ t _ { 0 } , T ]$ as $D ( t )$ and, following the setup in Choudhary (2007), assume that it increases linearly over detection time; that is:

$$
D (t) = n _ {h} \theta (t - t _ {0}) \xi .\tag{3}
$$

because the greater the number of hackers who join the BBP, the more valid reports that will be submitted. We thus assume that $D ( t )$ increases with the number of participating ethical hackers $\begin{array} { r } { n _ { h } \colon \frac { \partial D ( t ) } { \partial n _ { h } } > 0 } \end{array}$ . We assume the lifetimes of all bugs are mutually independent and normalize the total number of bugs in the software at its release time $( t = 0 )$ to be 1; thus, $0 \leq D ( t ) < 1$ . This is in line with the practice that the number of bugs in the software will never be zero. Further, recall that we denote the number of fixed bugs (per unit time) by $f .$ Because the firm may not have the capability to fix all the valid bugs reported by the hackers, we assume $f \leq$ $n _ { h } \theta \xi$ in this study.<sup>2</sup> Therefore, the number of bugs fixed by time $t \in [ t _ { 0 } , T ]$ is given by:

$$
I (t) = f (t - t _ {0}).\tag{4}
$$

To focus on the software firm’s decision to launch the BBP, we assume that the firm ceases its in-house detection at the software release time and that only the ethical hackers contribute to the software testing (e.g., August & Niculescu, 2013). Therefore, the number of unfixed bugs in the software at time ?? is given by 1 − ??(??).

On the user side, drawing from previous studies (e.g., Feng et al., 2020), we adopt a stylized two-period growth model. The cumulative number of software users at time ?? is defined by the following assumption:

Assumption 3:

$$
N (t) = \left\{ \begin{array}{l} \beta t, t \in [ 0, \tau_ {N} ], \\ \beta \tau_ {N}, t \in (\tau_ {N}, T ], \end{array} \right.\tag{5}
$$

where $\beta > 0$ is the number of new users acquired per unit time over $t \in [ 0 , \tau _ { N } ] . ^ { 3 }$ As illustrated in Figure 2, the evolution of existing users consists of two phases: the growth phase $( t \in [ 0 , \tau _ { N } ] )$ and the maturity phase $( t \in ( \tau _ { N } , T ] )$

![](/api/attachments/VQZ5YDFG/fulltext/images/a917e1849ab83228803714307474cf4a08e3d86b6276d1ce97487fe51766239d.jpg)  
Figure 1. Segmentation of Ethical Hackers

![](/api/attachments/VQZ5YDFG/fulltext/images/a40aed5e8626f93125d658dd696f68f88479c5f47881df4f1f897a4a656db04c.jpg)  
Figure 2. Number of Software Users as a Function of Time

Four types of costs relate to launching the BBP: the bug bounty reward, the processing cost of bug reports, the bug-fixing cost, and the failure cost. First, we assume that the bug bounty reward $c _ { r }$ is determined by the bug bounty platform and is fixed for each valid bug report while operating a BBP. This study assumes an exogenous bug reward because, in practice, most firms lack the capability to build their own security response center, and thus join bug bounty platforms to launch BBPs. Moreover, according to the reward policy of bug bounty platforms (e.g., Vulbox), firms are required to accept the minimum reward or a reward recommended by the bug bounty platform. Hence, the total bug bounty reward is given by:

$$
R = c _ {r} D (t).\tag{6}
$$

Second, the firm incurs the processing costs of bug reports associated with validating the existence of reported bugs and assessing the risk level of any flaw. In light of the basic laws of bug bounty platforms (e.g., HackerOne), we assume that the firm processes all bug reports. Thus, the total processing cost is given by:

$$
P = c _ {p} n _ {h} \theta (T - t _ {0}),\tag{7}
$$

where $c _ { p }$ denotes the processing cost per bug report.

Third, the firm incurs fixing costs to resolve valid bugs reported by ethical hackers. As it is increasingly difficult for the firm to fix more bugs, the average bugfixing cost (per unit time) $C _ { F }$ is, therefore, assumed to be a convex increasing function with respect to the number of fixed bugs (per unit time). Hence, we make the following assumption in this study:

Assumption 4: $\begin{array} { r } { \frac { \partial C _ { F } } { \partial f } > 0 \mathrm { ~ a n d } \frac { \partial ^ { 2 } C _ { F } } { \partial f ^ { 2 } } > 0 . } \end{array}$

Thus, the total bug-fixing cost is given by:

$$
F = C _ {F} (T - t _ {0}).\tag{8}
$$

Fourth, the firm incurs failure costs from exposing its users to defective software. Consistent with the literature (August & Niculescu, 2013), the failure cost is defined as the cost of recovering from software failures and providing compensation to all affected users to ensure that they will continue to use or repurchase this product. Let $c _ { g }$ denote the per-user failure cost incurred by each bug per unit time. Because any existing bug could be maliciously exploited and cause software failure, affecting all installed users at any time, the total failure cost is given by:

$$
G = \int_ {0} ^ {t _ {0}} c _ {g} N (t) d t + \int_ {t _ {0}} ^ {T} c _ {g} (1 - I (t)) N (t) d t.\tag{9}
$$

Further, releasing a BBP improves the firm’s reputation and enhances the users’ confidence in the product, which brings the benefit of trust to the firm. As discussed in the Introduction, there is a natural difference in the benefit of trust between the two software licensing models. For a firm that uses the perpetual licensing model, the benefit of trust results only from users’ one-time purchases during the user growth phase, which is referred to as the one-time benefit of trust in this study. Let $\gamma _ { p }$ denote the average benefit of trust incurred per user. The following assumption defines the total amount of benefit of trust under perpetual licensing.

Assumption 5: Under perpetual licensing, the total amount of benefit of trust increases linearly with the number of users. Thus, the total expected benefit of trust under perpetual licensing is given by:

$$
B _ {p} = \left\{ \begin{array}{c c} \int_ {t _ {0}} ^ {\tau_ {N}} \gamma_ {p} \beta d t, t _ {0} \in [ 0, \tau_ {N} ], \\ 0, & t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.\tag{10}
$$

Under subscription licensing, we assume that all installed users will continue to subscribe throughout the software service horizon. This assumption is reasonable because software products have zero marginal cost, enabling firms to set prices based on user valuations and ensure their continued subscription (e.g., Dou et al., 2017). Considering all kinds of user purchases, including initial purchases, subscription renewals, and value-added service purchases, the firm using subscription licensing model gains repeating benefits of trust after launching the BBP. Let $\gamma _ { s }$ denote the average benefit of trust incurred per user per unit time. The following assumption defines the total expected benefit of trust under subscription licensing.

Assumption 6: The total expected benefit of trust under subscription licensing is given by

$$
B _ {s} = \int_ {t _ {0}} ^ {T} \gamma_ {s} N (t) d t, t _ {0} \in [ 0, T ].\tag{11}
$$

Table 1 provides a summary of the notation used in this study. Following the framework provided in this section, the firm’s optimal launch time $( t _ { 0 } )$ of the BBP can be obtained by maximizing its total expected payoff as:

$$
\begin{array}{l} \max _ {t _ {0}} \Pi (t _ {0}) = B _ {i} - (R + P + F + G), i \in \\ \{s, p \} \qquad \text {s.t.} t _ {0} \in [ 0, T ], \end{array}\tag{12}
$$

where the subscripts $^ { 6 6 } s ^ { , 5 }$ and $" p "$ represent the subscription licensing and perpetual licensing model, respectively.

Table 1. Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>T</td><td>Software service length</td></tr><tr><td> $t_0$ </td><td>Launch time of the BBP,  $t_0 \in [0,T]$ </td></tr><tr><td> $\tau_N$ </td><td>Length of the user growth phase</td></tr><tr><td>r</td><td>Payoff obtained by an ethical hacker from participating in the BBP</td></tr><tr><td> $n_h$ </td><td>Number of ethical hackers participating in the BBP</td></tr><tr><td>θ</td><td>Average number of bug reports submitted by each ethical hacker per unit time</td></tr><tr><td>f</td><td>Number of fixed bugs per unit time</td></tr><tr><td>ξ</td><td>Validity rate of the bug reports</td></tr><tr><td>β</td><td>Number of new users per unit time during the growth phase</td></tr><tr><td>D(t)</td><td>Number of valid bugs reported by ethical hackers by time t (t ∈ [t0,T], D(t0) = 0, D(t) ∈ [0,1))</td></tr><tr><td>I(t)</td><td>Number of fixed bugs by time t (t ∈ [t0,T], I(t) ≤ D(t))</td></tr><tr><td>N(t)</td><td>Cumulative number of software users at time t (t ∈ [0,T])</td></tr><tr><td> $c_r$ </td><td>Bug bounty reward for each valid bug report</td></tr><tr><td> $c_p$ </td><td>Processing cost per bug report</td></tr><tr><td> $c_g$ </td><td>Average failure cost incurred by each user per unit time per bug</td></tr><tr><td> $C_F$ </td><td>Average fixing cost per unit time</td></tr><tr><td> $\gamma_s$ </td><td>Average benefit of trust gained from each user per unit time under subscription licensing</td></tr><tr><td> $\gamma_p$ </td><td>Average benefit of trust gained from each user under perpetual licensing</td></tr><tr><td>d</td><td>Invalidity coefficient of submitted bug reports</td></tr><tr><td>α</td><td>An ethical hacker&#x27;s payoff coefficient</td></tr><tr><td> $c_f$ </td><td>Fixing cost per unit of bug squared</td></tr></table>

## 4 Optimal BBP Launch Strategy

In this section, we examine and compare the optimal BBP launch timing under the perpetual and subscription licensing models.

## 4.1 Optimal Launch Time under Perpetual Licensing

We first solve the optimal launch time for the software firm using the perpetual licensing model. We define $\begin{array} { r } { A = C _ { F } + r \theta ( c _ { r } \xi + c _ { p } ) , c _ { g 1 } = \frac { 6 ( T A - \gamma _ { p } \beta \tau _ { N } ) } { \beta f \tau _ { N } \left( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } \right) } } \end{array}$ , and $\begin{array} { r } { \gamma _ { p 1 } = \frac { A T } { \xi \beta \tau _ { N } } . } \end{array}$ . By solving Equation (12) under perpetual licensing, we have Proposition 1.

Proposition 1: Under perpetual licensing,

i. when the benefit of trust is insignificant (i.e., $\gamma _ { p } \leq \gamma _ { p 1 } )$ e

a. if the failure cost is high $( \mathrm { i } . \mathrm { e } . , c _ { g } > c _ { g 1 } )$ the firm should launch the BBP and the software simultaneously $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = 0 )$ ;

b. otherwise, the firm should not launch the BBP $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = T )$

ii. when the benefit of trust is significant (i.e., $\gamma _ { p } > \gamma _ { p 1 } )$ , the firm should launch the BBP and the software simultaneously (i.e., $t _ { 0 } ^ { * } =$ 0).

Proposition 1 establishes a bug bounty launching rule for software firms that adopt the perpetual licensing model. As shown in Figure 3, when the benefit of trust is insignificant (i.e., $\gamma _ { p } \leq \gamma _ { p 1 } )$ , if the failure cost is high, the firm is better off launching a BBP at the software release time, which is referred to as the simultaneous launch strategy in this study. A high failure cost incentivizes the firm to detect and fix the bugs as early as possible; thus, the firm benefits from launching a BBP at the earliest moment. For instance, Microsoft’s Windows operating system, which is used throughout the world, carries a high failure cost and a relatively low benefit of trust. <sup>4</sup> To help offset the failure cost, Microsoft introduced Windows 10 and the BBP for it simultaneously (Microsoft, 2023).

When both the failure cost and the benefit of trust are low, launching a BBP is not profitable for the firm; that is, no launch strategy should be adopted by the software firm. MathWorks, for instance, did not launch a BBP for MATLAB, a programming and numeric computing software (MathWorks, 2023). A failure in MATLAB has little impact on users’ stored files or data, and MathWorks can assist users in recovering from a MATLAB failure at a low cost. MATLAB also obtains a low benefit of trust from launching the BBP because it is used mainly to solve mathematical problems and users are not highly concerned with its security and reliability. In line with our findings, not launching a BBP for MATLAB is the best strategy.

Proposition 1.ii indicates that if the benefit of trust is sufficiently high, the firm should launch the software and the BBP simultaneously. Clearly, if users are highly concerned about the reliability of the software, the BBP should be launched at the earliest possible time to ensure that the firm earns the highest one-time benefit of trust. Notably, under perpetual licensing, launching a BBP between 0 and T is not a viable strategy for the firm.

![](/api/attachments/VQZ5YDFG/fulltext/images/03d5cd0ead7280895493ffe1ecf6f5a32b4b979538f21e31588fcb600531e3fa.jpg)  
Figure 3. Optimal BBP Launch Strategy under Perpetual Licensing

Following Proposition 1, we examine how the software service length affects the optimal launch strategy, as summarized in Corollary 1.

Corollary 1: For the firm using the perpetual licensing model, as the software service length ?? increases,

i. when the benefit of trust is small $\mathrm { ( i . e . , } \gamma _ { p } <$ $\frac { A ( 3 T ^ { 2 } + \tau _ { N } ^ { 2 } ) } { 6 T \xi \beta \tau _ { N } } )$ , the firm has a greater incentive to choose simultaneous launch;

ii. however, when the benefit of trust is large $\begin{array} { r } { ( \mathrm { i . e . , } \gamma _ { p } \geq \frac { A ( 3 T ^ { 2 } + \tau _ { N } ^ { 2 } ) } { 6 T \xi \beta \tau _ { N } } ) . } \end{array}$ , the firm has a greater incentive to choose no launch.

The intuition for this result is as follows. BBPs are launched to save failure costs and earn the benefit of trust. Intuitively, the primary motivation for launching a BBP is to save failure costs when the benefit of trust is low, and more failure costs are saved as the service length grows. Hence, when the benefit of trust is relatively low, the firm is more incentivized to launch the BBP as the software service length increases. With an increasing benefit of trust, however, the main motivation for the firm to launch the BBP shifts from saving failure costs to earning greater benefits of trust from users. Given a fixed user growth period $\tau _ { N }$ , a longer software service length ?? implies a longer maturity period, during which the firm earns no benefit from the users’ increased trust resulting from the BBP. However, the firm is still burdened with the bounty, processing, and bug-fixing costs. Thus, as illustrated in Corollary 1.ii, the firm is less incentivized to launch the BBP as the software service length becomes longer.

## 4.2 Optimal Launch Time under Subscription Licensing

In this subsection, we investigate the optimal BBP launch time under the subscription licensing model. Solving Equation (12) under subscription licensing, we have the optimal BBP launch time, as given in Proposition 2. For convenience, we define $\gamma _ { s 1 } =$ $\begin{array} { r l r } & { \frac { A ( 3 T ^ { 2 } - 3 T \tau _ { N } + \tau _ { N } ^ { 2 } ) } { 6 \beta \tau _ { N } ( \mathrm { T } - \frac { 1 } { 2 } \tau _ { N } ) ^ { 2 } } , } & { c _ { g 2 } = \frac { 6 T A - 3 \gamma _ { S } \beta \tau _ { N } ( 2 T - \tau _ { N } ) } { \beta f \tau _ { N } ( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } ) } , } & { c _ { g 3 } = } \end{array}$ $\frac { A } { f \beta \tau _ { N } ( T - \frac 1 2 \tau _ { N } ) } ,$ , and $c _ { g 4 } > 0$ , satisfying

$$
\begin{array}{r l} & c _ {g 4} f \beta (3 (\gamma_ {s} A - c _ {g 4} f T C _ {F}) - \frac {1}{2} c _ {g 4} ^ {2} f ^ {2} \beta \tau_ {N} (\tau_ {N} ^ {2} - 3 T ^ {2})) + \\ & \beta^ {\frac {1}{2}} (\gamma_ {s} ^ {2} \beta - 2 c _ {g 4} f ^ {2} (A - c _ {g 4} f \beta \tau_ {N} (T - \frac {\tau_ {N}}{2}))) ^ {\frac {3}{2}} - \gamma_ {s} ^ {3} \beta^ {2} = 0. \end{array}
$$

Proposition 2: Under subscription licensing,

i. when the benefit of trust is insignificant (i.e., $\gamma _ { s } < \gamma _ { s 1 } )$

a. if the failure cost is high $( { \mathrm { i . e . , } } c _ { g } > c _ { g 2 } )$ the firm should launch the BBP and the software simultaneously $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = 0 ) ;$

b. otherwise, the firm should not launch the BBP $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = T )$

ii. when the benefit of trust is significant (i.e., $\gamma _ { s } \geq \gamma _ { s { 1 } } ) ,$

a. if the failure cost is relatively high $( \mathrm { i } . \mathrm { e } . , c _ { g } > c _ { g 3 } )$ , the firm should launch the BBP and the software simultaneously $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = 0 ) ;$

b. if the failure cost is moderate or small (i.e., ?????? $\{ c _ { g 4 } , 0 \} < c _ { g } \leq c _ { g 3 } ) ,$ the firm is better off launching a delayed BBP at

$$
t _ {0} ^ {*} = \frac {\gamma_ {s} \beta - \sqrt {\beta \left(\gamma_ {s} ^ {2} \beta - 2 c _ {g} f (A - c _ {g} \beta \tau_ {N} (T - \frac {1}{2} \tau_ {N}))\right)}}{c _ {g} \beta f},
$$

which falls into the market growth phase $( { \mathrm { i . e . , } } 0 < t _ { 0 } ^ { \ast } < \tau _ { N } ) ;$

c. otherwise, if the failure cost is small (i.e., $0 < c _ { g } \leq m a x \{ c _ { g 4 } , 0 \} )$ , the firm should not launch the BBP $( \mathrm { i } . \mathrm { e } . , t _ { 0 } ^ { * } = T ) . ^ { 5 }$

Figure 4 provides an illustration of the findings in Proposition 2. Proposition 2.i reveals that under subscription licensing, when the benefit of trust is relatively low $( \mathrm { i . e . , } \gamma _ { s } < \gamma _ { s 1 } )$ , the firm should choose the simultaneous launch strategy if the failure cost is high, and no launch if the failure cost is low. This result is qualitatively in line with that under the perpetual licensing model, as revealed in Proposition 1.i, although the threshold for $c _ { g }$ that distinguishes the two strategies is different in the two cases.

When the benefit of trust is relatively high, unlike the findings under the perpetual licensing model, the firm has three launch strategies available under subscription licensing. Note that simultaneous launch and no launch are still viable options in this case. When the failure cost is high, simultaneous launch is the optimal strategy because the primary incentive for the firm to launch a BBP is to identify and fix bugs, ultimately reducing failure costs. This is outlined in Proposition 2.ii(a). When the failure cost is sufficiently small, no launch is the best strategy as illustrated in Proposition 2.ii(c).

Notably, Proposition 2.ii(b) reveals a major finding of this study. Under subscription licensing, a delayed launch strategy, that is, launching the BBP after releasing the software, emerges as the best option for the firm when the failure cost is moderate or small and the benefit of trust is significant. However, as revealed in Proposition 1, the delayed launch strategy is not viable for the firms using perpetual licensing.

(?? = 1.5, ??<sub>??</sub> = 0.35, ?? = 0.5, ?? = 2, ??<sub>??</sub> = 35, ??<sub>??</sub> = 5, ?? = 0.75, ?? = 0.5, ??<sub>??</sub> = 10, ?? = 65)  
![](/api/attachments/VQZ5YDFG/fulltext/images/3238f57cbf089349fb2cf9cdc7e16761a228989f0bad6d39d3afdbd3e04142cb.jpg)  
Figure 4. Optimal BBP Launch Strategy under Subscription Licensing

The reasoning for this finding is as follows. When the failure cost is low, gaining a significant benefit of trust is the primary incentive for the firm to launch a BBP. Because of the one-time benefit of trust, under perpetual licensing, the firm should launch a BBP and the software simultaneously, as demonstrated in Proposition 1. Under subscription licensing, however, the on-demand feature allows the firm to enjoy a repeating benefit of trust during the BBP duration. The firm thus benefits from launching a BBP during the market growth phase, that is, $0 < t _ { 0 } ^ { * } < \tau _ { N }$ , when the failure cost is not high but the benefit of trust is significant. Therefore, it is the difference in the nature of the two licensing models (one-time purchase or repeated purchase) leads to the different launch decisions of the firms.

In line with this finding, the delayed launch strategy is commonly adopted in practice for subscription-based software products. For instance, Tencent Meeting, a subscription-based virtual meeting software, launched its BBP during its market growth stage (Tencent, 2020). Because the user frequently shares massive quantities of information through virtual meetings, trust is critical for virtual meeting software. In addition, because Tencent Meeting is not used by highly confidential businesses (e.g., banks, military institutions) and stores only a small quantity of user files, the failure cost for its users is considered to be relatively low. According to Proposition 2.ii(b), Tencent should adopt the delayed launch strategy for its virtual meeting software. Such a delayed launch strategy is also chosen by Grammarly, an AI-powered writing assistant software that benefits greatly from increased user trust but has a relatively low failure cost (HackerOne, 2023).

We also examine how various exogenous factors affect the optimal launch timing under delayed launch. First, as the user growth length $\tau _ { N }$ increases, the firm should launch the BBP earlier. Intuitively, given a fixed software service length $T ,$ , a longer $\tau _ { N }$ represents a shorter software maturity phase, during which the firm can earn the benefit of trust from all installed users. Therefore, the firm should launch its BBP earlier to gain a higher benefit of trust as $\tau _ { N }$ increases. In addition, when the bug bounty reward $c _ { r }$ increases, the firm should postpone the launch of the BBP. Note that the firm should choose the delayed launch only when the failure cost is low, implying that awarding a large number of bug reports to reduce the firm’s failure cost is not a profitable strategy. As a result, to avoid affording high bug bounty rewards, the firm should delay the launch of the BBP as $c _ { r }$ increases.

We next explore how the changes in software service length impact the optimal BBP launch strategy under subscription licensing.

Corollary 2: Under subscription licensing, as the software service length becomes longer, the firm has a greater incentive to launch a BBP or launch a BBP earlier (under delayed launch).

Corollary 2 demonstrates that unlike the firm that uses the perpetual licensing model, the firm that uses the subscription licensing model should always launch a BBP as the length of the software service increases. Again, the subscription licensing model enables the firm to earn a repeating benefit of trust. In this case, a longer software service horizon implies a higher total benefit of trust, encouraging the firm to launch a BBP.

![](/api/attachments/VQZ5YDFG/fulltext/images/959d010eaddeeb1f254ac60d4a1ce7d896da6c451190a1e8fcd4211a1bc99437.jpg)  
Figure 5. Two Stages of Improving Software Reliability through a BBP

Similarly, under delayed launch, the firm is better off launching the BBP earlier as the software service length increases. A longer service length indicates that the firm needs to afford higher failure costs (during the maturity phase). To reduce the failure costs in the prolonged market maturity phase, the firm benefits from launching an earlier BBP to detect and fix more bugs earlier. In addition, launching the BBP earlier enables the firm to enjoy a greater benefit of trust. Hence, the firm should launch the BBP earlier under a delayed launch strategy as the length of the software service increases.

## 5 Impacts of Bug-Fixing Capability

After launching a BBP, the reliability of the software is determined by the number of valid reports submitted by the ethical hackers in the detection stage and, more crucially, the number of bugs fixed by the firm in the bugfixing stage, as shown in Figure 5.

We analyze how the bug-fixing capability of the firm affects the BBP launch strategy under the two licensing models. To improve model tractability, following the three assumptions (i.e., Assumptions 1, 2, and 4) presented in Section 3, we define specific functional forms for (1) ethical hackers’ payoff (i.e., ?? ), (2) the validity rate of bug reports (i.e., ??), and (3) the bug-fixing cost per unit time (i.e., $C _ { F } )$

First, following Assumption 1, we define the payoff an ethical hacker gains from participating in the BBP as

$$
r = \alpha c _ {r} f,\tag{13}
$$

where ?? is the ethical hacker’s payoff coefficient.<sup>6</sup>

Second, according to Assumption 2, we define the validity rate of submitted bug reports as

$$
\xi = 1 - n _ {h} \theta d,\tag{14}
$$

where $\begin{array} { r } { d < \frac { 1 } { n _ { h } \theta } } \end{array}$ is the invalidity coefficient.<sup>7</sup>

Third, following Assumption 4, the bug-fixing cost per unit time is formulated as

$$
C _ {F} = c _ {f} f ^ {2},\tag{15}
$$

where $c _ { f }$ is the fixing cost per unit of bug squared.

To further investigate the optimal strategies for launching bug bounty programs, we consider two cases in the following: the case with exogenous bug-fixing capability and that with endogenous bug-fixing capability.

We first consider an exogenous number of fixed bugs per unit time (i.e., ??), which also represents the firm’s bugfixing capability. We examine the impact of the bugfixing capability on the firm’s payoff under simultaneous and delayed launch. Note that all threshold values are in Appendix A unless indicated otherwise.

Figures 6 and 7 reveal the significant impact of the bugfixing capability on the firm’s payoff under simultaneous and delayed launch. When the bug bounty reward is high, the relationship between the bug-fixing capability and the firm’s payoff follows a U-shaped pattern, while it follows an inverted U-shaped pattern when the reward is low. The reasoning behind this result is as follows. Note that increases in either bug bounty reward or bug-fixing capability attract ethical hackers to participate in BBPs. When the bug bounty reward is high, a large number of ethical hackers participate and submit numerous valid bug reports. A higher bug-fixing capability will further increase the number of participating ethical hackers. In this case, if the bug-fixing capability is low, an increase in it will lead to higher BBP-related costs (i.e., bug rewards, report-processing costs, and bug-fixing costs), while the failure cost decreases at a low rate.

π(0)  
![](/api/attachments/VQZ5YDFG/fulltext/images/958c0ccab81fd0a16744f2b8a935cba7717c836891cc2de26034ece6514c355a.jpg)  
a. Perpetual Licensing with $c _ { r } = 7$ (High bug bounty reward)

I(0)  
![](/api/attachments/VQZ5YDFG/fulltext/images/010ff6272b477c95769944f208d52434192a7e576610d50ac0ec2fa53c35c12f.jpg)

I(0)  
![](/api/attachments/VQZ5YDFG/fulltext/images/321dabc4db8dd2b11d0f5ccef62009942782a96bdffaaba1f8ccdb180ba1fa69.jpg)  
c. Subscription Licensing with $c _ { r } = 7$ (High bug bounty reward)

II(0)  
![](/api/attachments/VQZ5YDFG/fulltext/images/e120bf170e2ccc879243af64c6b028623d6ac7b0f176db07d40228d669781846.jpg)  
d. Subscription Licensing with $\mathbf { c } _ { r } = 3$ (Low bug bounty reward)  
(?? = 1.4, ??<sub>??</sub> = 0.58, ??<sub>??</sub> = 1, ?? = 0.5, ??<sub>??</sub> = 12, ??<sub>??</sub> = 1.15, ??<sub>??</sub> = 22, ?? = 40, ??<sub>??</sub> = ??<sub>??</sub> = 0.005, ?? = 2, ?? = 0.5)

Figure 6. Impact of f on the Firm’s Payoff under Simultaneous Launch  
I(t)  
![](/api/attachments/VQZ5YDFG/fulltext/images/aa87c3fa29191f9ce6aeef69b45b1936aadd8196f397a9614ac4608c52aed079.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/c4bba8f4e338e0f3c7960b86407de13ba67db1f5931195cf6aa92e7aae680666.jpg)  
(?? = 0.95, ??<sub>??</sub> = 0.75, ??<sub>??</sub> = 0.3, ?? = 0.5, ??<sub>??</sub> = 0.8, ??<sub>??</sub> = 0.175, ??<sub>??</sub> = 6.5, ?? = 18, ??<sub>??</sub> = 0.005, ?? = 2, ?? = 1)  
Figure 7. Impact of ?? on the Firm’s Payoff under Delayed Launch

Consequently, the firm’s payoff decreases as the bugfixing capability increases. However, when the bugfixing capability is high, a further increase in bugfixing capability leads to a greater number of fixed bugs per unit time, greatly reducing the failure cost and thus increasing the firm’s payoff. Hence, the impact of the bug-fixing capability on the firm’s payoff follows a U-shaped pattern when the reward is high, as shown in Figures 6a, 6c, and 7a.

In contrast, when the bug bounty reward is low, the impact of the bug-fixing capability on the firm’s payoff under simultaneous and delayed launch follows an inverted U-shaped pattern, as shown in Figures 6b, 6d, and 7b. A low bug bounty reward attracts only a small number of ethical hackers to report bugs, indicating that a relatively low failure cost could be saved. Although an improvement in bug-fixing capability attracts more ethical hackers and saves more failure costs, bug-fixing costs also improve super-linearly at the same time. As a result, when the bug bounty reward is low, as the bug-fixing capability improves, the total payoff of the firm first increases because of the savings in failure costs, and then decreases due to the superlinear increase in bug-fixing cost.

Combining Figures 6 and 7, we can conclude that under the U-shaped pattern, the firm benefits from launching a BBP when its bug-fixing capability is low or high, while under the inverted U-shaped pattern, the firm should opt to launch a BBP when its bug-fixing capability is relatively low. This finding holds great practical significance since it could assist bug bounty platforms in making informed decisions regarding how to regulate various types of software firms. Specifically, for software firms that offer high bug bounty rewards, bug bounty platforms should support them in maintaining either a high or low bug-fixing capability. A moderate bug-fixing capability could hinder their motivation to launch BBPs. However, for software firms that offer low bug bounty rewards, it is not advisable for the platform to require them to fix all reported bugs. The high cost associated with bug fixing may force these firms to exit the bug bounty platform.

Next, we examine the optimal BBP launch decisions with an endogenous number of fixed bugs (i.e., ??). After determining the BBP launch time, the firm decides the number of bugs fixed per unit time (that is, the bug-fixing capability). We solve the optimal bugfixing capability for software firms under perpetual and subscription models in Proposition 3.

Proposition 3: Under both licensing models, the optimal bug-fixing capability is:

$$
f ^ {*} = \left\{ \begin{array}{l l} \frac {\alpha c _ {r} \theta - 1}{\alpha^ {2} c _ {r} ^ {2} d \theta^ {2}}, & c _ {g} > c _ {g 5}, \\ f _ {1}, & c _ {g 6} <   c _ {g} \leq c _ {g 5}, \\ 0, & \text {otherwise.} \end{array} \right.
$$

where $f _ { 1 } =$

$$
\left\{ \begin{array}{l l} \frac {c _ {g} \beta (t _ {0} ^ {3} + 3 T ^ {2} \tau_ {N} - 3 t _ {0} \tau_ {N} (2 T - \tau_ {N})) - 6 \alpha \theta (c _ {p} + c _ {r}) (T - t _ {0})}{1 2 c _ {f} (T - t _ {0}) (c _ {f} - \alpha^ {2} c _ {r} d \theta^ {2})}, & t _ {0} \in [ 0, \tau_ {N}), \\ \frac {c _ {g} (T - t _ {0}) \beta \tau_ {N} - 2 \alpha (c _ {p} + c _ {r}) \theta}{4 c _ {f} - 4 \alpha^ {2} c _ {r} d \theta^ {2}}, & t _ {0} \in [ \tau_ {N}, T ]. \end{array} \right.
$$

Proposition 3 suggests that under both licensing models, the firm should choose the optimal bug-fixing capability in accordance with the failure cost. When the failure cost is high, it is more profitable for the firm to ensure that all reported bugs are fixed $( \mathrm { i } . \mathrm { e } . , f ^ { * } =$ $\frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } )$ . This finding is in line with industry practice. For example, according to HackerOne, software firms that launch a BBP with higher failure costs, such as PayPal, are more active in fixing reported bugs (HackerOne, 2023). When the failure cost is moderate, the firm should fix a proportion of reported bugs. If the failure cost is low, theoretically, the firm is better off not fixing any of the reported bugs.

To examine the optimal launch time of the BBP in the case with an endogenized bug-fixing capability, we substitute the optimal solutions in Proposition 3 into the payoff function of the firm (Equation 12). The following corollary depicts the conditions under which the firm prefers not to conduct bug fixing.

Corollary 3: When the failure cost is low (i.e., $c _ { g } <$ $c _ { g 6 } )$ , under both licensing models, the firm should launch the BBP but not fix bugs.

Based on Corollary 3, when the failure cost is low, the firm should launch the BBP but has no incentive to invest in bug-fixing. Thus, after perceiving the bugfixing efforts of the firm, the ethical hackers become unwilling to participate or report bugs to the firm. As a result, although the firm announces that it will reward ethical hackers for valid bug reports, the BBP cannot improve software reliability. In reality, such a phenomenon may exist, but its duration is short-lived due to the disclosure of ethical hackers and the supervision of the bug bounty platform. For instance, Zoom previously released a BBP that was criticized for not fixing bugs (Robinhouston, 2019; Tomaschek, 2019) and eventually revamped its BBP (Cimpanu, 2020). Thus, in the following analysis, we rule out this trivial case with zero bug-fixing capability. Numerical analysis is conducted to investigate the optimal BBP launch strategy under an endogenized bug-fixing capability. The main results are shown in Figure 8 and Observation 1.

Observation 1: Under the optimal bug-fixing capability, if the failure cost or the benefit of trust is high,

i. the firm using the perpetual licensing model should adopt a simultaneous launch strategy;

ii. the firm using the subscription licensing model should adopt a delayed or simultaneous launch strategy.

Observation 1 is qualitatively in line with Propositions 1 and 2; that is, under both licensing models, the firm should not launch the BBP when both the failure cost and benefit of trust are low. With an increase in the failure cost or the benefit of trust, under perpetual licensing, the firm should launch the BBP and the software at the same time, as shown in Figure 8a. Under subscription licensing, when the failure cost is not high but the benefit of trust is significant, delayed launch becomes the firm’s optimal launch strategy. Further, as the failure cost rises, the firm under subscription licensing should choose a simultaneous launch.

Simultaneous launch△ Delayed launchNo launch  
![](/api/attachments/VQZ5YDFG/fulltext/images/c95eac7aee2d907c1ce2cc0b0496d9a8d959a344a1edb445f0a73a044299be65.jpg)  
a. Perpetual licensing

![](/api/attachments/VQZ5YDFG/fulltext/images/49a0ebd37c7574ab581a4eec2bffe167cad750ff459fa1fe837cb55a6bde0bf0.jpg)  
(?? = 0.16, ??<sub>??</sub> = 0.15, ?? = 0.5, ?? = 2.05, ??<sub>??</sub> = 1.2, ??<sub>??</sub> = 0.5, ?? = 0.15, ??<sub>??</sub> = 4, ?? = 45)  
Figure 8. Optimal Launch Strategies under the Optimal Bug-fixing Capability

## 6 Extensions and Conclusions

## 6.1 Extensions

We develop three extension models in which our key assumptions are relaxed. Extension 1 assumes that the increased trust resulting from launching a BBP expands the total user size. Extension 2 considers the scenario where the number of participating ethical hackers changes over time. Following the setup in Olshavsky (1980), Extension 3 incorporates different user growth curves into the model. We verify that our main findings on the optimal BBP launch strategy remain qualitatively valid under these extensions. Further details regarding these extension models are provided in Appendix B.

## 6.2 Conclusion

This study contributes to the literature on the optimal launch strategy of BBPs for software firms. First, the study utilizes a software reliability growth model and user growth curve to depict the payoff of launching the BBP, which allows us to pinpoint the optimal BBP launch time. The analytical results show that if both the failure cost and the benefit of trust are high, firms should launch the software and the BBP simultaneously under both perpetual and subscription licensing models. When the failure cost is not high, depending on the benefit of trust, firms that adopt the subscription licensing model can choose their launch strategies between no launch and delayed launch, whereas firms that use the perpetual licensing model should opt for no launch or simultaneous launch.

In addition, we examine the effect of bug-fixing capability on the firm’s payoff obtained from launching the BBP. When the bug bounty reward is low, the impact of bug-fixing capability on the firm’s payoff takes an inverted U-shaped pattern, causing the firm with high bug-fixing capability to be less inclined to launch the BBP. Conversely, when the bug bounty reward is high, a U-shaped pattern emerges, indicating that the firm should opt to launch the BBP when its bug-fixing capability is either low or high. This finding improves the understanding of how to motivate firms to launch BBPs that increase software reliability and enable bug bounty platforms to regulate the market.

Our study provides several important managerial implications for software firms and bug bounty platforms. First, we determine the conditions under which software firms that use perpetual or subscription licensing models should launch a BBP. Specifically, software firms should take both the failure cost and the benefit of trust on an individual level associated with launching the BBP into account. Second, we uncover the disparities in launch strategies between firms using perpetual and subscription licensing models. Firms utilizing perpetual licensing face a binary choice: either launching the BBP and the software simultaneously or not launching at all. On the other hand, firms employing a subscription model enjoy the advantage of flexibility, as they can opt for a delayed launch strategy.

Third, we provide crucial managerial insights for bug bounty platforms on how to incentivize software firms to launch BBPs and improve software reliability. Our findings indicate that when the bug bounty reward is low, high bug-fixing capabilities discourage firms from launching BBPs under both licensing models. In this case, bug bounty platforms may consider easing the regulations for launching BBPs for these firms. When the bug bounty reward is high, the firm should launch the BBP when the bug-fixing capability is either low or high. In this case, bug bounty platforms could offer assistance to help firms improve their bugfixing capabilities and, in turn, motivate them to launch BBPs, improve software reliability, and provide more opportunities for ethical hackers to earn bug bounty rewards.

This study can be extended in several directions. First, this study adopts a stylized software reliability evolution model with growth and maturity phases. A possible future direction is to employ diffusion models to depict the evolution process. Second, our study investigates the optimal launch time of the BBP while considering only the contributions of external ethical hackers. An extension to our work can incorporate other testing methods (e.g., internal testing, beta testing) when determining the optimal launch timing of the BBP. Finally, future research could investigate the optimal BBP launch strategy under hybrid software licensing models.

## Acknowledgments

The authors would like to thank the senior editor, Fink Lior, the anonymous associate editor, and two reviewers for their insightful comments and suggestions. This work was supported by the National Natural Science Foundation of China (Grant Nos. 72231004, 72022012, 71871155, 72394373). Haiyang Feng is the corresponding author.

## References

Aaltonen, A., & Gao, Y. (2021). Does the outsider help? The impact of bug bounty programs on data breaches. SSRN. https://ssrn.com/ abstract=3908761

Albergotti, R. (2021). Apple pays hackers six figures to find bugs in its software. Then it sits on their findings. Washington Post. https://www. washingtonpost.com/technology/2021/09/09/a pple-bug-bounty/

Alfred, N. (2018). Facebook launches bug bounty program to report data thieves. Cnet. https://www.cnet.com/news/privacy/facebooklaunches-bug-bounty-program-to-report-datathieves/

Amer, M. (2019). Why Windows is so popular? Medium. https://medium.com/@Mohammed Amer/why-windows-is-so-popular-1ea19f00e738

Arora, A., Caulkins, J. P., & Telang, R. (2006). Research note—sell first, fix later: Impact of patching on software quality. Management Science, 52(3), 465-471.

August, T., & Niculescu, M. F. (2013). The influence of software process maturity and customer error reporting on software release and pricing. Management Science, 59(12), 2702-2726.

Cavusoglu, H., Raghunathan, S., & Yue, W. T. (2008). Decision-theoretic and game-theoretic approaches to it security investment. Journal of Management Information Systems, 25(2), 281- 304.

Cezar, A., Cavusoglu, H., & Raghunathan, S. (2014). Outsourcing information security: Contracting issues and security implications. Management Science, 60(3), 638-657.

Choudhary, V. (2007). Comparison of software quality under perpetual licensing and software as a service. Journal of Management Information Systems, 24(2), 141-165.

Choudhary, V., & Zhang, Z. (2015). Research note— patching the cloud: The impact of SaaS on patching strategy and the timing of software release. Information Systems Research, 26(4), 845-858.

Cimpanu, C. (2020). Zoom to revamp bug bounty program, bring in more security experts. ZDNet. https://www.zdnet.com/article/zoomto-revamp-bug-bounty-program-bring-inmore-security-experts

Culafi, A. (2021). Bug bounty programs in 2021: High payouts, higher stakes. TechTarget.

https://www.techtarget.com/searchsecurity/ne ws/252509175/Bug-bounty-programs-in-2021- High-payouts-higher-stakes

Dalal, S. R., & Mallows, C. L. (1988). When should one stop testing software? Journal of the American Statistical Association, 83(403), 872-879.

Dey, D., Lahiri, A., & Zhang, G., (2015). Optimal policies for security patch management. INFORMS Journal on Computing, 27(3), 462-477.

Dou, Y, Hu, Y. J., & Wu, D. J. (2017). Selling or leasing? Pricing information goods with depreciation of consumer valuation. Information Systems Research, 28(3), 585-602.

Fan, M., Kumar, S., & Whinston, A. B. (2009). Shortterm and long-term competition between providers of shrink-wrap software and software as a service. European Journal of Operational Research, 196(2), 661-671.

Feng, H., Jiang, Z., Li, M., & Feng, N. (2020). First-or second-mover advantage? The case of itenabled platform markets. MIS Quarterly, 44(3), 1107-1141.

Feng, N., Chen, Y., Feng, H., Li, D., & Li, M. (2020). To outsource or not: The impact of information leakage risk on information security strategy. Information & Management, 57(5), Article 103215.

Gal-Or, E., & Ghose, A. (2005). The economic incentives for sharing security information. Information Systems Research, 16(2), 186-208.

Ghoshal, A., Lahiri, A., & Dey, D. (2017). Drawing a line in the sand: Commitment problem in ending software support. MIS Quarterly, 41(4), 1227-1247.

Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. ACM Transactions on Information and System Security, 5(4), 438-457.

Guo, Z., & Ma, D. (2018). A model of competition between perpetual software and software as a service. MIS Quarterly, 42(1), 101-120.

HackerOne. (2023). How HackerOne helps the vulnerability management process. https:// www.hackerone.com/vulnerability-manage ment/how-hackerone-helps-vulnerabilitymanagement-process

HackerOne. (2023). The directory of disclosure bug bounty programs. https://hackerone.com/ directory/programs

Hruska, J. (2019). Microsoft Windows XP is finally dead, nearly 18 years post-launch. ExtremeTech. https://www.extremetech.com/

computing/289440-microsoft-XP-is-finallydead-nearly-18-years-post-launch

Huang, C.D., & Behara, R. S. (2013). Economics of information security investment in the case of concurrent heterogeneous attacks with budget constraints. International Journal of Production Economics, 141(1), 255-268.

Ji, Y., Mookerjee, V. S, & Sethi, S. P. (2005). Optimal software development: A control theoretic approach. Information Systems Research, 16(3), 292-306.

Jiang, Z., Sarkar, S., & Jacob, V. S. (2012). Postrelease testing and software release policy for enterprise-level systems. Information Systems Research, 23(3-part-1), 635-657.

Jiang, Z., Scheibe, K. P., Nilakanta, S., & Qu, X. (2017). The economics of public beta testing. Decision Sciences, 48(1), 150-175.

Kim, B. C., Chen, P. Y., & Mukhopadhyay, T. (2009). An economic analysis of the software market with a risk-sharing mechanism. International Journal of Electronic Commerce, 14(2), 7-40.

Levrard J. (2020). How cloud providers use bug bounty to increase customer trust categories. Yeswehack. https://blog.yeswehack.com/customer-stories/ how-cloud-providers-use-bug-bounty-to-increasecustomers-trust

Li, H., Yoo, S., & Kettinger, W. J. (2021). The roles of it strategies and security investments in reducing organizational security breaches. Journal of Management Information Systems, 38(1), 222-245.

Li, S., Cheng, H. K., Duan, Y., & Yang, Y. C. (2017). A study of enterprise software licensing models. Journal of Management Information Systems, 34(1), 177-205.

Ma, D., & Seidmann, A. (2015). Analyzing software as a service with per-transaction charges. Information Systems Research, 26(2), 360-378.

Maillart, T., Zhao, M., Grossklags, J., & Chuang, J. (2017). Given enough eyeballs, all bugs are shallow? Revisiting Eric Raymond with bug bounty programs. Journal of Cybersecurity, 3(2), 81-90.

MathWorks. (2023). Vulnerability disclosure policy for security researchers. https://www.math works.com/company/aboutus/policies\_stateme nts/vulnerability-disclosure-policy.html.

Mehra, A., & Saha, R. L. (2018). Utilizing public betas and free trials to launch a software product. Production and Operations Management, 27(11), 2025-2037.

Microsoft. (2023). Microsoft bug bounty program. https://www.microsoft.com/en-us/msrc/bounty

Miller, M. (2020). FBI sees spike in cyber-crime reports during coronavirus pandemic. The Hill. https://thehill.com/policy/cybersecurity/49319 8-fbi-sees-spike-in-cyber-crime-reportsduring-coronavirus-pandemic

Morris, D. Z. (2020). “Security Botox” or “Amazingly Successful”? Inside the battle to patch bug bounties’ biggest vulnerability. Fortune. https://fortune.com/2020/03/31/bugcrowdhackerone-bug-bounty-voatz/

Olshavsky, R. W. (1980). Time and the rate of adoption of innovations. Journal of Consumer Research, 6(4), 425-428.

Oren, N. (2022). Looking back at our bug bounty program in 2022. Meta. https://about.fb.com/ news/2022/12/metas-bug-bounty-program-2022/

Robinhouston. (2019). Zoom has been accused that it launched the fake BBP at the beginning. Hacker News. https://news.ycombinator.com/item?id= 20389812

Sharma, A. (2021). Researcher refuses Telegram’s bounty award, discloses auto-delete bug. Ars Technica. https://arstechnica.com/informationtechnology/2021/10/researcher-refusestelegrams-bounty-award-discloses-auto-deletebug/

Subramanian, H.C., & Malladi, S. (2020). Bug bounty marketplaces and enabling responsible vulnerability disclosure: An empirical analysis. Journal of Database Management, 31(1), 38- 63.

Tencent. (2020). Come dig a hole! Tencent launches million cash bug reward programs. DayDayNews. https://daydaynews.cc/en/tech nology/479769.html

Tomaschek, A. (2019). Opinion: Zoom’s handling of vulnerability disclosure highlights the dark side of bug bounty NDAs. ProPrivacy. https://proprivacy.com/privacy-news/darkside-of-bug-bountys

Walshe, T., & Simpson, A. (2020). An empirical study of bug bounty programs. Proceedings of IEEE 2nd International Workshop on Intelligent Bug Fixing.

Wu, Y., Tayi, G. K., Feng, G., & Fung, R. Y. (2021). Managing information security outsourcing in a dynamic cooperation environment. Journal of the Association for Information Systems, 22(3), 827-850.

Xin, M. (2020). The Impact of customer valuation uncertainty on software licensing. MIS Quarterly, 44(2), 561-603.

Zhang, J., & Seidmann, A. (2010). Perpetual versus subscription licensing under quality uncertainty and network externality effects. Journal of Management Information Systems, 27(1), 39- 68.

Zhao, M., Aron L., & Jens G. (2017). Devising effective policies for bug-bounty platforms and security vulnerability discovery. Journal of Information Policy, 7(1), 372-418.

Zhao, M., Grossklags, J., & Liu, P. (2015). An empirical study of web vulnerability discovery ecosystems. Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security.

Zhao, M., Laszka, A., Maillart, T., & Grossklags, J. (2016). Crowdsourced security vulnerability discovery: Modeling and organizing bug-

bounty programs. Proceedings of the HCOMP Workshop on Mathematical Foundations of Human Computation.

Zhao, X., Xue, L., & Whinston, A.B. (2013). Managing interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements. Journal of Management Information Systems, 30(1), 123-152.

Zhou, J., & Hui, K. L. (2021). Sleeping with the enemy: An economic and security analysis of bug bounty programs (HKUST Business School Research Paper No. 2021-038). SSRN. https://ssrn.com/abstract=3940307

Zhou, J., & Hui, K. L. (2022). Strategic interaction between crowd and in-house contributions: Evidence from the internet bug bounty program (HKUST Business School Research Paper No. 2022-055). SSRN. https://ssrn.com/abstract =4074182

## Appendix A: Proofs

## A1. Proof of Proposition 1

$$
\left\{ \begin{array}{l} \frac {1}{6} \beta \binom{f c _ {g} \left(t _ {0} ^ {3} + 3 T ^ {2} \tau_ {N} - \tau_ {N} ^ {3} - 3 t _ {0} \tau_ {N} (2 T - \tau_ {N})\right)}{- 3 c _ {g} \tau_ {N} (2 T - \tau_ {N}) - 6 \gamma_ {p} (t _ {0} - \tau_ {N})} + (t _ {0} - T) A, t _ {0} \in [ 0, \tau_ {N} ], \\ \frac {1}{2} \beta c _ {g} \tau_ {N} (f T ^ {2} + f t _ {0} ^ {2} - 2 T (1 + f t _ {0}) + \tau_ {N}) + (t _ {0} - T) A, \qquad \qquad t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

Note that we define $A = C _ { F } + r \theta ( c _ { r } \xi + c _ { p } )$ in the paper.

(a) When $t _ { 0 } \in [ 0 , \tau _ { N } ]$ , the first-order derivative of $\Pi ( t _ { 0 } )$ with respect to $t _ { 0 }$ is:

$$
\frac {\partial \Pi (t _ {0})}{\partial t _ {0}} = \frac {1}{2} f \beta c _ {g} (t _ {0} ^ {2} - 2 T \tau_ {N} + \tau_ {N} ^ {2}) + A - \beta \gamma_ {p}.
$$

Because $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } }$ is a quadratic function and the extremum of $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } }$ is $t _ { 0 } = 0$ , given $\begin{array} { r } { \frac { 1 } { 2 } f \beta c _ { g } > 0 , \frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } } \end{array}$ increases with $t _ { 0 }$ Therefore, the maximum total payoff equals Π(0) or $\Pi ( \tau _ { N } )$ when $t _ { 0 } \in [ 0 , \tau _ { N } ]$ . Comparing Π(0) with $\Pi ( \tau _ { N } )$ , we have $\Pi ( 0 ) - \Pi ( \tau _ { N } ) = \tau _ { N } ( \beta \gamma _ { p } + f \beta c _ { g } ( T - { \textstyle \frac { 2 } { 3 } } \tau _ { N } ) \tau _ { N } - A )$ . Then, $\Pi ( 0 ) \le \Pi ( \tau _ { N } )$ is equivalent to

$$
A \geq \beta \gamma_ {p} + c _ {g} \beta \tau_ {N} (T - \frac {2}{3} \tau_ {N}).\tag{A1}
$$

$\Pi ( 0 ) > \Pi ( \tau _ { N } )$ is equivalent to $A < \beta { \gamma } _ { p } + c _ { g } \beta { \tau } _ { N } ( T - { \textstyle { \frac { 2 } { 3 } } } \tau _ { N } )$ . Thus, when $t _ { 0 } \in [ 0 , \tau _ { N } ]$ , if $A \ge \beta \gamma _ { p } + c _ { g } \beta \tau _ { N } ( T - $ $\begin{array} { r } { \frac 2 3 \tau _ { N } \biggr ) , t _ { 0 } ^ { * } = \tau _ { N } } \end{array}$ ; otherwise, $t _ { 0 } ^ { * } = 0$

(b) When $t _ { 0 } \in [ \tau _ { N } , T ]$ , the first-order derivative of $\Pi ( t _ { 0 } )$ with respect to $t _ { 0 }$ is:

$$
\frac {\partial \Pi (t _ {0})}{\partial t _ {0}} = f \beta c _ {g} (t _ {0} - T) \tau_ {N} + A.
$$

Because $\mathit { f } \beta c _ { g } > 0 , \frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } }$ increases with $t _ { 0 } ;$ thus, the maximum total payoff equals Π(??) or $\Pi ( \tau _ { N } )$ when $t _ { 0 } \in ( \tau _ { N } , T ]$ Comparing Π(??) with $\Pi ( \tau _ { N } )$ , we have $\begin{array} { r } { \Pi ( T ) - \Pi ( \tau _ { N } ) = ( T - \tau _ { N } ) ( A - { \frac { 1 } { 2 } } c _ { g } f \beta \tau _ { N } ( T - \tau _ { N } ) ) } \end{array}$ . Then, $\Pi ( T ) < \Pi ( \tau _ { N } )$ is equivalent to

$$
A <   \frac {1}{2} c _ {g} f \beta \tau_ {N} (T - \tau_ {N}).\tag{A2}
$$

$\Pi ( T ) \geq \Pi ( \tau _ { N } )$ is equivalent to $\begin{array} { r } { A \ge \frac { 1 } { 2 } c _ { g } f \beta \tau _ { N } ( T - \tau _ { N } ) } \end{array}$ , then $t _ { 0 } ^ { * } = T$ . Thus, when $\begin{array} { r } { t _ { 0 } \in [ \tau _ { N } , T ] , \mathrm { i f } A < \frac { 1 } { 2 } c _ { g } f \beta \tau _ { N } ( T - } \end{array}$ $\tau _ { N } ) , t _ { 0 } ^ { * } = \tau _ { N } ;$ otherwise, $t _ { 0 } ^ { * } = T$

We next discuss the optimal launch time when combining the two cases: $t _ { 0 } \in [ 0 , \tau _ { N } ]$ and $t _ { 0 } \in [ \tau _ { N } , T ]$ . In this scenario, given $T \geq \tau _ { N }$ , Equations (A1) and (A2) are incompatible; therefore, $\tau _ { N }$ is not the optimal release time when $t _ { 0 } \in$ $[ 0 , T ]$ . Thus, we only need to compare Π(0) with Π(??): $\begin{array} { r } { \Pi ( T ) - \Pi ( 0 ) = T A - \frac { 1 } { \epsilon } c _ { g } \beta \tau _ { N } ( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } ) - \beta \tau _ { N } \gamma _ { p } . \ \Pi ( T ) \ge } \end{array}$ Π(0) is equivalent to $c _ { g } \leq c _ { g 1 }$ , where $\begin{array} { r } { c _ { g 1 } = \frac { 6 ( T A - \gamma _ { p } \beta \tau _ { N } ) } { \beta f \tau _ { N } \left( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } \right) } } \end{array}$ , and $\Pi ( T ) < \Pi ( 0 )$ is equivalent to $c _ { g } > c _ { g 1 }$

In addition, $\mathrm { i f } \gamma _ { p } > \gamma _ { p } .$ where $\begin{array} { r } { \gamma _ { p 1 } = \frac { A T } { \xi \beta \tau _ { N } } , c _ { g 1 } } \end{array}$ is negative. Because $c _ { g }$ is a non-negative term, $\gamma _ { p } > \gamma _ { p 1 }$ is a sufficient condition for $\Pi ( T ) < \Pi ( 0 )$

Overall, (1) if $\gamma _ { p } > \gamma _ { p 1 }$ , then $t _ { 0 } ^ { * } = 0 ; ( 2 )$ ) if $\gamma _ { p } \leq \gamma _ { p 1 }$ , when $c _ { g } > c _ { g 1 } , t _ { 0 } ^ { * } = 0$ ; when $c _ { g } \leq c _ { g 1 } , t _ { 0 } ^ { * } = T$

## A2. Proof of Corollary 1

The first-order derivative of threshold $\begin{array} { r } { c _ { g 1 } = \frac { 6 ( T A - \gamma _ { p } \beta \tau _ { N } ) } { \beta f \tau _ { N } \left( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } \right) } } \end{array}$ with respect to ?? is

$$
\frac {\partial c _ {g 1}}{\partial T} = \frac {6 (6 T \beta \gamma_ {p} \tau_ {N} - A (3 T ^ {2} + \tau_ {N} ^ {2}))}{f \beta \tau_ {N} (3 T ^ {2} - \tau_ {N} ^ {2}) ^ {2}}.
$$

If $\begin{array} { r } { \dot { \gamma } _ { p } < \frac { A ( 3 T ^ { 2 } + \tau _ { N } ^ { 2 } ) } { 6 T \xi \beta \tau _ { N } } , \frac { \partial c _ { g 1 } } { \partial T } < 0 \mathrm { , } } \end{array}$ ; otherwise, $\frac { \partial c _ { g 1 } } { \partial T } \geq 0$ . Note that $\begin{array} { r } { \frac { A ( 3 T ^ { 2 } + \tau _ { N } ^ { 2 } ) } { 6 T \xi \beta \tau _ { N } } < \gamma _ { p 1 } } \end{array}$

## A3. Proof of Proposition 2

Substituting Equations (6), (7), (8), (9), and (11) into Equation (12), we have the total payoff for the firm using the subscription licensing model:

$$
\Pi (t _ {0}) = \left\{ \begin{array}{l l} \left(\frac {1}{6} \beta (c _ {g} (f t _ {0} ^ {3} - 3 T (2 - f (T - 2 t _ {0})) \tau_ {N} + 3 (1 + f t _ {0}) \tau_ {N} ^ {2} - f \tau_ {N} ^ {3}) \right. \\ \qquad \left. - 3 \gamma_ {s} (t _ {0} ^ {2} - \tau_ {N} (2 T - \tau_ {N}))) + (t _ {0} - T) A \right. \\ \left(\frac {1}{2} \beta \tau_ {N} (2 (T - t _ {0}) \gamma_ {s} - c _ {g} (T (2 - f T) - f t _ {0} (2 T - t _ {0}) + \tau_ {N})) + (t _ {0} - T) A\right), t _ {0} \in [ 0, \tau_ {N} ], \end{array} \right.
$$

The first-order derivative of $\Pi ( t _ { 0 } )$ with respect to $t _ { 0 }$ is

$$
\frac {\partial \Pi (t _ {0})}{\partial t _ {0}} = \left\{ \begin{array}{l} \frac {1}{2} f \beta c _ {g} (t _ {0} ^ {2} - 2 T \tau_ {N} + \tau_ {N} ^ {2}) - \beta t _ {0} \gamma_ {s} + A, t _ {0} \in [ 0, \tau_ {N} ], \\ \beta \tau_ {N} \big (f c _ {g} (t _ {0} - T) + \gamma_ {s} \big) + A, \qquad \qquad t _ {0} \in [ \tau_ {N}, T ]. \end{array} \right.
$$

(a) When $t _ { 0 } \in [ 0 , \tau _ { N } ]$ , solving $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } = 0$ 9

(a-i) if $\beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \geq 0$ , the extremum of $\Pi ( t _ { 0 } )$ are $t _ { D } = \frac { \gamma _ { s } \beta - \sqrt { \beta \big ( \beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \big ) } } { c _ { g } \beta h }$ and $t _ { M } = \frac { \gamma _ { s } \beta + \sqrt { \beta \big ( \beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \big ) } } { c _ { a } \beta h }$ and $\begin{array} { r } { t _ { D } < t _ { M } . \mathrm { G i v e n } \frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } } \end{array}$ is a quadratic function of $t _ { 0 }$ and $\begin{array} { r } { { \frac { 1 } { 2 } } f \beta c _ { g } > 0 } \end{array}$ the $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } \leq 0$ if $t _ { 0 } \in [ t _ { D } , t _ { m } ]$ ; otherwise, if $t _ { 0 } < t _ { D }$ or $\begin{array} { r } { t _ { 0 } > t _ { M } , \frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } > 0 } \end{array}$ . Thus, in this case, $t _ { D }$ is the local maximum, and $t _ { M }$ is the local minimum of $\Pi ( t _ { 0 } )$

(a-ii) If $\beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) < 0$ , then the quadratic function $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } \neq 0$ . Because $\begin{array} { r } { { \frac { 1 } { 2 } } f \beta c _ { g } > 0 } \end{array}$ , we have $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } > 0$ . Thus, $\Pi ( t _ { 0 } )$ increases with $t _ { 0 }$ and $t _ { 0 } ^ { * } = \tau _ { N }$

(b) When $\begin{array} { r } { t _ { 0 } \in [ \tau _ { N } , T ] , \frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } } \end{array}$ increases with $t _ { 0 }$ because $f c _ { g } \beta \tau _ { N } > 0$ . Thus, the optimal launch time is at the two ends of the feasible region for $t _ { 0 } { : } T$ and $\tau _ { N }$

We next discuss the optimal launch time when combining the above two cases: $t _ { 0 } \in [ 0 , \tau _ { N } ]$ and $t _ { 0 } \in [ \tau _ { N } , T ]$

(1) First, if $\beta \gamma _ { s } ^ { 2 } - f c _ { q } ( 2 A - f \beta c _ { q } ( 2 T - \tau _ { N } ) \tau _ { N } ) \geq 0$ , according to the analysis of $( \mathrm { a } \mathrm { - i } ) , t _ { D }$ is the local maximum and $t _ { M }$ is the local minimum of $\Pi ( t _ { 0 } )$ . In this scenario, $2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } < 0 \mathrm { o r } 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } \geq 0$ holds.

(1-i) $\mathrm { I f } 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } < 0 \colon$

$\beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \geq 0$ and $2 A - f \beta c _ { q } ( 2 T - \tau _ { N } ) \tau _ { N } < 0$ are equivalent to $c _ { g } > c _ { g 3 }$ , where $c _ { g 3 } =$ $\frac { \alpha } { f \beta \tau _ { N } \Big ( T - \frac { 1 } { 2 } \tau _ { N } \Big ) } .$ . In this case, we have $t _ { D } < 0$ . Based on the analysis of (a-i) and (b), under such conditions, when $t _ { 0 } \in$ $[ 0 , \tau _ { N } ]$ , the optimal launch time is either $t _ { 0 } = 0$ or $t _ { 0 } = \tau _ { N } ;$ ; when $t _ { 0 } \in [ \tau _ { N } , T ]$ , the optimal launch time is either $t _ { 0 } =$ ?? or $t _ { 0 } = \tau _ { N }$ . Comparing $\Pi ( 0 ) , \Pi ( \tau _ { N } )$ , and Π(??), we have $t _ { 0 } ^ { * } = 0 \mathrm { i f } c _ { g } > c _ { g 2 }$ , where $\begin{array} { r } { c _ { g 2 } = \frac { 6 T A - 3 \gamma _ { s } \beta \tau _ { N } ( 2 T - \tau _ { N } ) } { \beta f \tau _ { N } \left( 3 T ^ { 2 } - \tau _ { N } ^ { 2 } \right) } ; t _ { 0 } ^ { \ast } = } \end{array}$ ?? otherwise.

Recall that $2 A - f \beta c _ { q } ( 2 T - \tau _ { N } ) \tau _ { N } < 0$ is equivalent to $c _ { g } > c _ { g 3 }$ . We conclude that when $c _ { g } > c _ { g 3 } , \mathrm { i f } c _ { g } > c _ { g 2 }$ , then g $t _ { 0 } ^ { * } = 0$ ; when $c _ { g 3 } < c _ { g } \leq c _ { g 2 } , t _ { 0 } ^ { * } = T$ . Note that $c _ { g 2 } > c _ { g 3 }$ is equivalent to

$$
\gamma_ {s} <   \gamma_ {s 1},\tag{A3}
$$

where $\begin{array} { r } { \gamma _ { s 1 } = \frac { A ( 3 T ^ { 2 } - 3 T \tau _ { N } + \tau _ { N } ^ { 2 } ) } { 6 \beta \tau _ { N } ( \mathrm { T } - \frac { 1 } { 2 } \tau _ { N } ) ^ { 2 } } . } \end{array}$

(1-ii) $\mathrm { I f } 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } \geq 0 \colon$

$\beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \geq 0$ and $2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } \geq 0$ are equivalent to $c _ { g } \leq c _ { g 3 }$ and $\gamma _ { s } \geq$ $\sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } }$ . In this case, $0 \le t _ { D } \le \tau _ { N }$ or $\tau _ { N } < t _ { D }$ holds.

$$
(\mathbf {1} - \mathbf {i i} - \mathbf {A}) \text {   If   } 0 \leq t _ {D} \leq \tau_ {N}:
$$

$0 \le t _ { D } \le \tau _ { N }$ is equivalent to $\begin{array} { r } { \gamma _ { s } \geq \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } } \end{array}$ . In this scenario, we have $\tau _ { N } < t _ { M }$ and $\begin{array} { r } { \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } > } \end{array}$ $\begin{array} { r } { \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } . } \end{array}$ . According to the analysis of (a-i) and (b), in this case, due to $0 \le t _ { D } \le \tau _ { N } < t _ { M }$ , when $t _ { 0 } \in$ $[ 0 , \tau _ { N } ]$ , the optimal launch time is $t _ { 0 } ^ { * } = t _ { D }$ and $\Pi ( t _ { D } ) > \Pi ( t _ { 0 } )$ ; when $t _ { 0 } \in [ \tau _ { N } , T ]$ , the optimal launch time is either $t _ { 0 } ^ { * } = T \ \mathrm { o r } \ t _ { 0 } ^ { * } = \tau _ { N }$ . Thus, we compare $\Pi ( t _ { D } )$ with Π(??). $\Pi ( t _ { D } ) - \Pi ( T ) = 0$ is equivalent to

$$
c _ {g 4} f \beta \left(3 \big (\gamma_ {s} A - c _ {g 4} f T C _ {F} \big) - \frac {1}{2} c _ {g 4} ^ {2} f ^ {2} \beta \tau_ {N} (\tau_ {N} ^ {2} - 3 T ^ {2})\right) + \beta^ {\frac {1}{2}} \bigg (\gamma_ {s} ^ {2} \beta - 2 c _ {g 4} f ^ {2} \left(A - c _ {g 4} f \beta \tau_ {N} \left(T - \frac {\tau_ {N}}{2}\right)\right) \bigg) ^ {\frac {3}{2}} - \gamma_ {s} ^ {3} \beta^ {2} =
$$

0. We denote

$\begin{array} { r } { Q ( c _ { g } ) = c _ { g 4 } f \beta \left( 3 \left( \gamma _ { s } A - c _ { g 4 } f T C _ { F } \right) - \frac { 1 } { 2 } c _ { g 4 } ^ { 2 } f ^ { 2 } \beta \tau _ { N } ( \tau _ { N } ^ { 2 } - 3 T ^ { 2 } ) \right) + \beta ^ { \frac { 1 } { 2 } } \left( \gamma _ { s } ^ { 2 } \beta - 2 c _ { g 4 } f ^ { 2 } \left( A - c _ { g 4 } f \beta \tau _ { N } \left( T - \frac { \tau _ { N } } { 2 } \right) \right) \right) ^ { \frac { 3 } { 2 } } - } \end{array}$ $\gamma _ { s } ^ { ~ 3 } \beta ^ { 2 }$ . Substituting $c _ { g } = c _ { g 3 }$ and $\gamma _ { s } = \gamma _ { s 1 }$ into $Q ( c _ { g } )$ , we have $Q \left( c _ { g } \right) = 0$ . Given $0 \leq t _ { D } \leq \tau _ { N } < T$ , we have $\begin{array} { r } { \frac { \partial Q ( c _ { g } ) } { \partial c _ { g } } > } \end{array}$ 0 and $\frac { \partial Q ( c _ { g } ) } { \partial \gamma _ { s } } > 0$ ; thus, $Q ( c _ { g } )$ increases with either $c _ { g }$ and $\gamma _ { s }$ . Therefore, there exists a unique threshold $c _ { g 4 } > 0$ satisfying $Q \left( c _ { g 4 } \right) = 0$ and $c _ { g 4 }$ decreases with $\gamma _ { s }$ . We thus have that when $\gamma _ { s } \geq \gamma _ { s 1 }$ , then $c _ { g 3 } \geq c _ { g 4 }$

Recall that $0 \le t _ { D } \le \tau _ { N }$ is equivalent to $\begin{array} { r } { \gamma _ { s } \geq \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } } \end{array}$ , then $\gamma _ { s } > m a x \{ \gamma _ { s 1 } , \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } \}$ or $\begin{array} { r } { \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } \leq \gamma _ { s } \leq \gamma _ { s 1 } } \end{array}$ holds.

If $\begin{array} { r } { \gamma _ { s } > m a x \{ \gamma _ { s 1 } , \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } \} , \Pi ( t _ { D } ) > \Pi ( T ) } \end{array}$ is equivalent to ???? ${ \cdot \{ c _ { g 4 } , 0 \} } < c _ { g } \leq c _ { g 3 }$ ; thus, $t _ { 0 } ^ { * } = t _ { D } ; \Pi ( t _ { D } ) \le$ Π(??) is equivalent to $0 < c _ { g } \leq m a x \{ c _ { g 4 } , 0 \}$ and thus $t _ { 0 } ^ { * } = T$ . I $\begin{array} { r } { \cdot \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } \leq \gamma _ { s } \leq \gamma _ { s 1 } } \end{array}$ , we have $0 < c _ { g } \leq$ $m a x \{ c _ { g 4 } , 0 \}$ ; thus, $t _ { 0 } ^ { * } = T \left( \mathrm { i . e . , } \Pi ( t _ { D } ) \leq \Pi ( T ) \right)$ .

(1-ii-B) If $\tau _ { N } < t _ { D } \mathrm { : }$

$\tau _ { N } < t _ { D }$ is equivalent to $\begin{array} { r } { \gamma _ { s } \leq \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } } \end{array}$ . Recall that $\begin{array} { r } { \gamma _ { s } \geq \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } } \end{array}$ holds based on the analysis of (1-ii).

Therefore, if $\begin{array} { r } { \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } \leq \frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } } \mathrm { a n c } } \end{array}$ 1

$\begin{array} { r } { \gamma _ { s } \in \left[ \sqrt { \frac { f c _ { g } \left( 2 A - f \beta c _ { g } \left( 2 T - \tau _ { N } \right) \tau _ { N } \right) } { \beta } } , \frac { A - c _ { g } \beta \tau _ { N } f \left( T - \tau _ { N } \right) } { \beta \tau _ { N } } \right] } \end{array}$ , due to $\tau _ { N } < t _ { D }$ and the analysis of (a-i), when $t _ { 0 } \in [ 0 , \tau _ { N } ]$ , we have $\frac { \partial \Pi ( t _ { 0 } ) } { \partial t _ { 0 } } > 0$ . Thus $\Pi ( t _ { 0 } )$ increases with $t _ { 0 }$ and $t _ { 0 } ^ { * } = \tau _ { N }$ when $t _ { 0 } \in [ 0 , \tau _ { N } ]$ . In this case, based on the analysis of (b), we need only to compare Π(??) and $\Pi ( \tau _ { N } )$ , and we have $\Pi ( T ) > \Pi ( \tau _ { N } )$ ; thus $t _ { 0 } ^ { * } = T$ . If $\begin{array} { r } { \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } > } \end{array}$ $\frac { A - c _ { g } \beta \tau _ { N } f ( T - \tau _ { N } ) } { \beta \tau _ { N } }$ , then $\gamma _ { s } \in \varnothing$ , and $\tau _ { N } < t _ { D }$ does not hold.

Combining (1-ii-A) and (1-ii-B), we have that under $c _ { g } \leq c _ { g 3 }$ and $\begin{array} { r } { \gamma _ { s } \geq \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } } \end{array}$ , if $m a x \{ c _ { g 4 } , 0 \} <$ $c _ { g } \leq c _ { g 3 }$ , then $t _ { 0 } ^ { * } = t _ { D } ;$ otherwise, if $0 < c _ { g } < m a x \{ c _ { g 4 } , 0 \} , t _ { 0 } ^ { * } = T$

(2) Second, $\beta \gamma _ { s } ^ { 2 } - f c _ { g } \big ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } \big ) < 0$ is equivalent to $c _ { g } < c _ { g 3 }$ and $\begin{array} { r } { \gamma _ { s } < \sqrt { \frac { f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) } { \beta } } } \end{array}$ According to the analysis of (a-ii), $t _ { 0 } ^ { * } = \tau _ { N }$ when $t _ { 0 } \in [ 0 , \tau _ { N } ]$ . In this case, based on the analysis of (b), the maximum payoff is either Π(??) or $\Pi ( \tau _ { N } )$ , and we have $\Pi ( T ) > \Pi ( \tau _ { N } )$ ; thus, $t _ { 0 } ^ { * } = T$

Combining this result with (1-ii), we have that when $c _ { g } \leq c _ { g 3 } , \mathrm { i f } \ c _ { g } > m a x \{ c _ { g 4 } , 0 \}$ , then $t _ { 0 } ^ { * } = t _ { D } ;$ otherwise, if $0 <$ $c _ { g } < m a x \{ c _ { g 4 } , 0 \} , t _ { 0 } ^ { * } = T$ . Further, as stated in (1-i), when $c _ { g } > c _ { g 3 } , \mathrm { i f } c _ { g } > c _ { g 2 }$ , then $t _ { 0 } ^ { * } = 0 ; { \mathrm { i f ~ } } c _ { g 3 } < c _ { g } \leq c _ { g 2 } , t _ { 0 } ^ { * } =$ ??. In the meantime, $c _ { g 2 } > c _ { g 3 }$ when $\gamma _ { s } < \gamma _ { s 1 }$ and $c _ { g 3 } \geq c _ { g 4 }$ when $\gamma _ { s } \geq \gamma _ { s 1 }$ Accordingly, (1) when $\gamma _ { s } < \gamma _ { s 1 } , { \mathrm { i f } } c _ { g } > c _ { g 2 }$ , we have $t _ { 0 } ^ { * } = 0 ; \mathrm { i f } c _ { g } \le c _ { g 2 }$ , we have $t _ { 0 } ^ { * } = T ; ( 2 )$ ) when $\gamma _ { s } \geq \gamma _ { s 1 } , \mathrm { i f } c _ { g } >$ $c _ { g 3 }$ , we have $t _ { 0 } ^ { * } = 0 ;$ if ?????? $\{ c _ { g 4 } , 0 \} < c _ { g } \leq c _ { g 3 }$ , we have $t _ { 0 } ^ { * } = t _ { D } ; \mathrm { i f } \ 0 < c _ { g } \leq m a x \{ c _ { g 4 } , 0 \}$ , we have $t _ { 0 } ^ { * } = T$ Therefore, these complete the proof.

## A4. Proof of Corollary 2

(a) Recall from Proposition 2.i, when $\gamma _ { s } < \gamma _ { s 1 }$ where $\begin{array} { r } { \gamma _ { s 1 } = \frac { A ( 3 T ^ { 2 } - 3 T \tau _ { N } + \tau _ { N } ^ { 2 } ) } { 6 \beta \tau _ { N } ( \mathrm { T } - \frac { 1 } { \gamma } \tau _ { N } ) ^ { 2 } } } \end{array}$ , we have $c _ { g 2 }$ as the threshold value to distinguish the two optimal launch strategies $( \mathrm { i . e . }$ ., simultaneous launch and no launch). Therefore, the first-order derivative of $c _ { g 2 }$ with respect to ?? is:

$$
\frac {\partial c _ {g 2}}{\partial T} = \frac {6 (3 T ^ {2} \beta \gamma_ {s} \tau_ {N} - (A + 3 T \beta \gamma_ {s}) \tau_ {N} ^ {2} + \beta \gamma_ {s} \tau_ {N} ^ {3} - 3 T ^ {2} A)}{f \beta \tau_ {N} (3 T ^ {2} - \tau_ {N} ^ {2}) ^ {2}}.
$$

Given $\gamma _ { s } < \gamma _ { s 1 }$ , we have $\frac { \partial c _ { g 2 } } { \partial T } < 0$

(b) When $\gamma _ { s } \geq \gamma _ { s 1 }$ , we have the threshold value $c _ { g 3 }$ , distinguishing the two optimal launch strategies $( \mathrm { i . e . }$ simultaneous launch and delayed launch).

(b-i) The first-order derivative of $c _ { g 3 }$ with respect to $T$ is:

$$
\frac {\partial c _ {g 3}}{\partial T} = \frac {- 4 A}{f \beta \tau_ {N} (2 T - \tau_ {N}) ^ {2}}.
$$

It is obvious that $\frac { \partial c _ { g 3 } } { \partial T } < 0$

$\frac { \mathrm { ( { \bf b } - i i ) } \quad \mathrm { T h e } \quad \mathrm { f i r s t - o r d e r } \quad \mathrm { d e r i v a t } } { \frac { \gamma _ { s } \beta - \sqrt { \beta \left( \beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \right) } } { c _ { g } \beta h } } )$ ive of optimal launch time $t _ { 0 } ^ { * }$ under delayed launch $\begin{array} { r l } { ( \mathrm { i . } \mathrm { e . , ~ } } & { { } t _ { 0 } ^ { \ast } = } \end{array}$ with respect to $T$ is:

$$
\frac {\partial t _ {0} ^ {*}}{\partial T} = \frac {- f \beta c _ {g} \tau_ {N}}{\sqrt {\beta (\beta \gamma_ {s} ^ {2} - f c _ {g} (2 A - f \beta c _ {g} (2 T - \tau_ {N}) \tau_ {N}))}}.
$$

Given $\begin{array} { r } { \sqrt { \beta \big ( \beta \gamma _ { s } ^ { 2 } - f c _ { g } ( 2 A - f \beta c _ { g } ( 2 T - \tau _ { N } ) \tau _ { N } ) \big ) } > 0 , \mathrm { w e ~ h a v e ~ } \frac { \partial t _ { 0 } ^ { * } } { \partial T } < 0 . } \end{array}$

## A5. Proof of Proposition 3

If the firm fixes all valid bugs reported by ethical hackers, we have $f = n _ { h } \theta \xi$ . Substituting Equations (13) and (14) into $f = n _ { h } \theta \xi$ , we have the maximum value of $f ,$ that is $\begin{array} { r } { f = \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } . } \end{array}$ . Thus, $\begin{array} { r } { f \in \left[ 0 , \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } \right] , } \end{array}$

Substituting Equations (13), (14) and (15) into Equation (12), we obtain $\Pi ( f , t _ { 0 } )$ . Under perpetual licensing, the firstorder derivative of $\Pi ( f , t _ { 0 } )$ with respect to ?? is

$$
\frac {\partial \Pi (f , t _ {0})}{\partial f} = \left\{ \begin{array}{l l} \binom{2 \big (d \alpha^ {2} \theta^ {2} c _ {r} ^ {3} - c _ {f} \big) (T - t _ {0}) f - \alpha \theta c _ {p} c _ {r} (T - t _ {0}) -}{\alpha \theta c _ {r} ^ {2} (T - t _ {0}) + \frac {1}{6} \beta c _ {g} \left(t _ {0} ^ {3} + 3 T ^ {2} \tau_ {N} - \tau_ {N} ^ {3} - 3 t _ {0} \tau_ {N} (2 T - \tau_ {N})\right)}, & t _ {0} \in [ 0, \tau_ {N} ], \\ (T - t _ {0}) \left(2 \big (d \alpha^ {2} \theta^ {2} c _ {r} ^ {3} - c _ {f} \big) f - \frac {1}{2} \big (2 \alpha \theta c _ {r} \big (c _ {p} + c _ {r} \big) - \beta c _ {g} (T - t _ {0}) \tau_ {N} \big)\right), & t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

(a) If $c _ { f } < d \alpha ^ { 2 } \theta ^ { 2 } c _ { r } ^ { 3 } , { \frac { \partial \Pi ( f , t _ { 0 } ) } { \partial f } }$ increases with ?? when $t _ { 0 } \in [ 0 , T ]$ . In this case, the optimal bug-fixing capability is either $\begin{array} { r } { f ^ { * } = 0 \ \mathrm { o r } \ f ^ { * } = { \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } } } \end{array}$ . Comparing $\Pi ( 0 , t _ { 0 } )$ with $\begin{array} { r } { \Pi \left( \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } , t _ { 0 } \right) , \Pi ( 0 , t _ { 0 } ) > \Pi \left( \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } , t _ { 0 } \right) } \end{array}$ is equivalent to $c _ { g } <$

$c _ { g a }$ , where $\begin{array} { r } { c _ { g a } = \left\{ \begin{array} { l l } { \frac { 6 ( d \alpha ^ { 2 } \theta ^ { 2 } \left( \alpha \theta c _ { p } + c _ { r } \right) - ( 1 - \alpha \theta ) c _ { f } ) ( T - t _ { 0 } ) } { d \alpha ^ { 2 } \beta \theta ^ { 2 } ( t _ { 0 } ^ { 3 } + 3 T ^ { 2 } \tau _ { N } - \tau _ { N } ^ { 3 } - 3 t _ { 0 } \tau _ { N } ( 2 T - \tau _ { N } ) ) } , t _ { 0 } \in [ 0 , \tau _ { N } ] , } \\ { \frac { 2 ( ( - 1 + \alpha \theta ) c _ { f } + d \alpha ^ { 2 } \theta ^ { 2 } ( \alpha \theta c _ { p } + c _ { r } ) ) } { d \alpha ^ { 2 } \beta \theta ^ { 2 } ( T - t _ { 0 } ) \tau _ { N } } , t _ { 0 } \in ( \tau _ { N } , T ] . } \end{array} \right. } \end{array}$ ; $\begin{array} { r } { \Pi ( 0 , t _ { 0 } ) \le \Pi \left( \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } , t _ { 0 } \right) } \end{array}$ is equivalent to $c _ { g } \geq$

$$
c _ {g a}.
$$

(b) When $c _ { f } \geq d \alpha ^ { 2 } \theta ^ { 2 } c _ { r } ^ { 3 } , \frac { \partial \Pi ( f , t _ { 0 } ) } { \partial f }$ decreases with ??. Solving $\begin{array} { r } { \frac { \partial \Pi ( f , t _ { 0 } ) } { \partial f } = 0 } \end{array}$ , we obtain the local maximum of $\Pi ( f , t _ { 0 } )$ and denote it as

$$
f _ {1} = \left\{ \begin{array}{c c} \frac {\beta c _ {g} (t _ {0} ^ {3} + 3 T ^ {2} \tau_ {N} - \tau_ {N} ^ {3} - 3 t _ {0} \tau_ {N} (2 T - \tau_ {N})) - 6 \alpha \theta c _ {r} (c _ {p} + c _ {r}) (T - t _ {0})}{1 2 (c _ {f} - d \alpha^ {2} \theta^ {2} c _ {r} ^ {3}) (T - t _ {0})}, & t _ {0} \in [ 0, \tau_ {N} ], \\ \frac {\beta c _ {g} (T - t _ {0}) \tau_ {N} - 2 \alpha \theta c _ {r} (c _ {p} + c _ {r})}{4 c _ {f} - 4 d \alpha^ {2} \theta^ {2} c _ {r} ^ {3}}, & t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

Recall that $\textstyle f \in \left[ 0 , { \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } } \right]$

(b-i) If $f _ { 1 } < 0$ , the optimal bug-fixing capability is $f ^ { * } = 0 . \ f _ { 1 } < 0$ is equivalent to $c _ { g } < c _ { g b }$ , where $c _ { g b } =$ $\left\{ \begin{array} { l l } { \frac { 6 \alpha \theta c _ { r } ( c _ { p } + c _ { r } ) ( T - t _ { 0 } ) } { \beta ( t _ { 0 } ^ { 3 } + 3 T ^ { 2 } \tau _ { N } - \tau _ { N } ^ { 3 } + 3 t _ { 0 } \tau _ { N } ( - 2 T + \tau _ { N } ) ) } , t _ { 0 } \in [ 0 , \tau _ { N } ] , } \\ { \frac { 2 \alpha \theta c _ { r } ( c _ { p } + c _ { r } ) } { \beta ( T - t _ { 0 } ) \tau _ { N } } , \quad \quad \quad \quad t _ { 0 } \in ( \tau _ { N } , T ] . } \end{array} \right.$

(b-ii) If $\begin{array} { r } { f _ { 1 } \in \left[ 0 , \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } \right] } \end{array}$ , the optimal bug-fixing capability is $\begin{array} { r } { f ^ { * } = f _ { 1 } . \ : f _ { 1 } \in \left[ 0 , \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } \right] } \end{array}$ is equivalent to $c _ { g b } \leq c _ { g } \leq$ $c _ { g c } , \quad$ where

$$
c _ {g c} = \left\{ \begin{array}{l l} \frac {6 (d \alpha^ {2} \theta^ {2} (2 + \alpha \theta (c _ {p} - c _ {r})) c _ {r} ^ {3} - 2 c _ {f} (1 - \alpha \theta c _ {r})) (T - t _ {0})}{d \alpha^ {2} \beta \theta^ {2} c _ {r} ^ {2} (t _ {0} ^ {3} + 3 T ^ {2} \tau_ {N} - \tau_ {N} ^ {3} + 3 t _ {0} \tau_ {N} (- 2 T + \tau_ {N}))}, & t _ {0} \in [ 0, \tau_ {N} ], \\ \frac {2 d \alpha^ {2} \theta^ {2} (2 + \alpha \theta (c _ {p} - c _ {r})) c _ {r} ^ {3} - 4 c _ {f} (1 - \alpha \theta c _ {r})}{d \alpha^ {2} \beta \theta^ {2} c _ {r} ^ {2} (T - t _ {0}) \tau_ {N}}, & t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

(b-iii) $\begin{array} { r } { \operatorname { I f } f _ { 1 } > \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } , } \end{array}$ the optimal bug-fixing capability is $\begin{array} { r } { f ^ { * } = \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } . f _ { 1 } > \frac { \alpha c _ { r } \theta - 1 } { \alpha ^ { 2 } c _ { r } ^ { 2 } d \theta ^ { 2 } } } \end{array}$ is equivalent to $c _ { g } > c _ { g c }$

To illustrate Proposition 6, we denote $c _ { g 5 } = \left\{ { c } _ { g a } , { c } _ { f } < d \alpha ^ { 2 } \theta ^ { 2 } c _ { r } ^ { 3 } \right. \mathrm { ~ a n d ~ } c _ { g 6 } = \left\{ { c } _ { g a } , { c } _ { f } < d \alpha ^ { 2 } \theta ^ { 2 } c _ { r } ^ { 3 } \right.$

## A6. Proof of Corollary 3

If $c _ { g } < c _ { g 6 }$ , according to Proposition 6, the optimal bug-fixing capability is $f ^ { * } = 0$ . Substituting $f ^ { * } = 0$ into $\Pi ( f , t _ { 0 } )$ under subscription licensing, the first-order derivative of $\Pi ( 0 , t _ { 0 } )$ with respect to $t _ { 0 }$ is

$$
\frac {\partial \Pi (0 , t _ {0})}{\partial t _ {0}} = \left\{ \begin{array}{l} - \beta t _ {0} \gamma_ {s}, t _ {0} \in [ 0, \tau_ {N} ], \\ - \beta \tau_ {N} \gamma_ {s}, t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

Under perpetual licensing, we have

$$
\frac {\partial \Pi (0 , t _ {0})}{\partial t _ {0}} = \left\{ \begin{array}{l} - \beta \gamma_ {p}, t _ {0} \in [ 0, \tau_ {N} ], \\ 0, \qquad t _ {0} \in (\tau_ {N}, T ]. \end{array} \right.
$$

It is obvious that $\begin{array} { r } { \frac { \partial \Pi ( 0 , t _ { 0 } ) } { \partial t _ { 0 } } \leq 0 } \end{array}$ holds under both licensing models. In this case, the firm should launch the BBP, and the optimal launch time is $t _ { 0 } ^ { * } = 0$

## Appendix B: Model Extensions

## B1. Extension 1: Expansion of Total User Size after Launching the BBP

In practice, the increased trust raised by a BBP might expand the total number of users. We thus assume the arrival rate of new users per unit time in the market growth phase increases to $\hat { \beta } ( \mathrm { i . e . , } \hat { \beta } > \beta )$ after the launch of the BBP. As illustrated in Figure B1, the cumulative number of users at time ?? is reformulated as

$$
N (t) = \left\{ \begin{array}{l l} \beta t, & t \in [ 0, t _ {0} ], \\ \beta t _ {0} + \hat {\beta} (t - t _ {0}), & t \in (t _ {0}, \tau_ {N} ], \\ \beta t _ {0} + \hat {\beta} (\tau_ {N} - t _ {0}), t \in (\tau_ {N}, T ]. \end{array} \right.\tag{B1}
$$

![](/api/attachments/VQZ5YDFG/fulltext/images/598275eebd50908017c5b11a205c1e7a0641b36fc332d4fecde00f5f0746a2d6.jpg)  
Figure B1. Number of Software Users when a BBP Expands User Size

In addition, the benefits of trust under perpetual and subscription licensing are, respectively, given by,

$$
\begin{array}{r l} & B _ {p} = \left\{ \begin{array}{c} \int_ {t _ {0}} ^ {\tau_ {N}} \gamma_ {p} \hat {\beta} d t, t _ {0} \in [ 0, \tau_ {N} ], \\ 0, \qquad t _ {0} \in (\tau_ {N}, T ], \end{array} \right. \\ & B _ {s} = \int_ {t _ {0}} ^ {T} \gamma_ {s} N (t) d t, t _ {0} \in [ 0, T ]. \end{array}\tag{B2}
$$

(B3)

Through numerical analysis, we find that under perpetual licensing, the firm is more likely to benefit from launching a BBP when the rate of user arrival $( { \hat { \beta } } )$ increases after the launch of a BBP, as shown in Figure B2a. Similarly, under subscription licensing, the firm tends to launch an earlier BBP as $\hat { \beta }$ increases, as illustrated in Figure B2b. Figure B3 demonstrates that our main findings in Propositions 1 and 2 regarding the optimal BBP launch strategy under both licensing models remain valid.

![](/api/attachments/VQZ5YDFG/fulltext/images/b22cbec465f9dd3fe78afae915c5d6753bbee8612746bb5fd99a6a23014f6176.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/ef84e42f9355245e92403f27b4bd550b2dc81f413d8ed237e1c4e58220d879aa.jpg)  
(?? = 4, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 0.4, ??<sub>??</sub> = 25, ??<sub>??</sub> = 5, ??<sub>??</sub> = 25, ??<sub>??</sub> = (?? = 0.75, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 0.8, ??<sub>??</sub> = 9, ??<sub>??</sub> = 3, ??<sub>??</sub> = 4, ??<sub>??</sub> = 6, ?? = 36, ?? = 0.7, ??<sub>??</sub> = 1, ?? = 0.14) 3, ?? = 36, ?? = 0.1, ?? = 3, ?? = 0.04)  
Figure B2. Impact of $\widehat { \pmb { \beta } }$ on the Optimal BBP Launch Strategy

Simultaneous launch△Delayed launchNo launch  
![](/api/attachments/VQZ5YDFG/fulltext/images/f9ddbf8fbf5b51808e67b5b72d1ad935b97281da5bb1dd3abd2ba26cc61d19a8.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/ee61f1ca1694abf3f1fdf72aec9c5501053a8d3981c855a1f98380bd61fcd4bb.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 3, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ??<sub>??</sub> = 5, ?? = 36, ??<sup>̂</sup> = 36.5, ?? = 0.1, ?? = 0.15)  
Figure B3. Optimal Launch Strategies of BBPs when a BBP Expands User Size

## B2. Extension 2: Number of Participating Ethical Hackers Changes over Time

In practice, the number of participating ethical hackers in a BBP may decrease over time because the detection of valid bugs becomes more difficult. We thus assume the number of participating ethical hackers at time $t \left( t \in [ t _ { 0 } , T ] \right)$ as

$$
n _ {h} (t) = n _ {h 1} - b (t - t _ {0}),\tag{B4}
$$

where $n _ { h 1 }$ represents the total number of participating ethical hackers and $n _ { h 1 } = \hat { c } _ { h }$ , and ?? is the number of ethical hackers quitting the BBP per unit time and $b T < n _ { h 1 }$

Considering the change in the number of participating ethical hackers over time, numerical experiments are conducted to examine the optimal launch strategies under the two licensing models and how the changes in ?? impact the optimal launch time of BBPs under perpetual licensing and subscription licensing. The results are shown in Figures B4 and B5. Figure B4 validates that when either the failure cost or the benefit of trust is high, under perpetual licensing, the firm should adopt a simultaneous launch strategy; under subscription licensing, the firm should adopt a delayed or simultaneous launch strategy. Overall, Figure B4 validates our main findings (e.g., Propositions 1 and 2).

As shown in Figure B5, with an increase in ??, the firm is more likely to benefit from launching the BBP under perpetual licensing, and, similarly, the firm should launch the BBP earlier under subscription licensing.

## OSimultaneous launch△Delayed launchNo launch

$$
c _ {g} \quad c _ {p} \tag {10}
$$

![](/api/attachments/VQZ5YDFG/fulltext/images/4aadf62204bef58c798a835c3cebdde721ca8ad5d2a65515977112e64e707114.jpg)

$$
(T = 0. 7 5, \tau_ {N} = 0. 5, b = 0. 5, n _ {h} = 1, \theta = 2, c _ {r} = 9, c _ {p} = 4, c _ {f} = 3, \beta = 3 6, \xi = 0. 5, f = 0. 1 4)
$$

Figure B4. Optimal Launch Strategies when the Number of Participating Ethical Hackers Changes over Time

![](/api/attachments/VQZ5YDFG/fulltext/images/b5f7f28503bbb02cc5ccff32bc30d8faebc1260cbca7837857da23e647bf4204.jpg)  
a. Perpetual Licensing  
(?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 1, ??<sub>ℎ</sub> = 0.8, ?? = 2.5, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ??<sub>??</sub> = 3, ?? = 36, ??<sub>??</sub> = 1, ?? = 0.5, ?? = 1)

![](/api/attachments/VQZ5YDFG/fulltext/images/c680e6535f4557558f5ae4d456fd4a4fd8bdbb191a83deffb50007d87d44f89c.jpg)  
b. Subscription Licensing  
(?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 1, ??<sub>ℎ</sub> = 0.8, ?? = 2.5, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ??<sub>??</sub> = 5, ?? = 36, ?? = 0.5, ??<sub>??</sub> = 1, ?? = 1)  
Figure B5. Optimal BBP Launch Time Versus ??

In addition, following the setup in Olshavsky (1980), we further assume the hacker growth model as an S-shaped growth curve with a bell-shaped growth rate:

$$
n _ {h} (t) = \frac {A}{1 + \mathrm{e} ^ {b - a (t - t _ {0})}}, t \in [ t _ {0}, T ],
$$

where $n _ { h } ( t )$ is the participating number of hackers at time ??, ?? is the ceiling number of ethical hackers, ?? is the constant of integration that positions the curve on the time scale, and ?? is the coefficient of hacker growth rate.

As shown in Figures B6 and B7, the numerical observations are still qualitatively consistent with our main findings revealed in Propositions 1 and 2.

![](/api/attachments/VQZ5YDFG/fulltext/images/681a6ef676d49dee69d75b178f2c228e5a71f28909d72da53ac7f9ff0b49f967.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/752f049a58d3b5b1f513635854ea05be999fb021a24a5b0948d7aa97aa164a28.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 5, ?? = 0.2, ?? = 0.5, ??<sub>??</sub> = 4, ?? = 0.1, ??<sub>??</sub> = 3, ?? = (?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 5, ?? = 0.2, ?? = 0.5, ??<sub>??</sub> = 4, ?? = 0.1, ??<sub>??</sub> = 3, ?? = 36, ??<sub>??</sub> = 0.1, ?? = 20, ?? = 3, ?? = 20 ) 36, ??<sub>??</sub> = 3, ?? = 20, ?? = 3, ?? = 20)

Figure B6. Optimal Launch Strategies of BBPs under Perpetual Licensing with S-Shaped Ethical Hacker Growth Model  
![](/api/attachments/VQZ5YDFG/fulltext/images/28de4c84b0672a00934298680515446fe59b46219b183cd58a952c03b4b584aa.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/a92f0d7e3dea78e997191fd9162cdf1a4b4f8f940a39f2c3d8ad72b3f4ca960c.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 5, ?? = 0.2, ?? = 0.5, ??<sub>??</sub> = 4, ?? = 0.1, ??<sub>??</sub> = 3, ?? = (?? = 0.75, ??<sub>??</sub> = 0.5, ??<sub>??</sub> = 5, ?? = 0.2, ?? = 0.5, ??<sub>??</sub> = 4, ?? = 0.1, ??<sub>??</sub> = 3, ?? = 36, ??<sub>??</sub> = 3, ?? = 20, ?? = 3, ?? = 20) 36, ??<sub>??</sub> = 1, ?? = 20, ?? = 3, ?? = 20)  
Figure B7. Optimal Launch Strategies of BBPs under Subscription Licensing with S-Shaped Ethical Hacker Growth Model

## B3. Extension 3: Different User Growth Models

## (1) S-Shaped User Growth Model

In this subsection, following the setup in Olshavsky (1980), we examine the model with an S-shaped growth curve and a bell-shaped growth rate, as given by,

$$
N (t) = \frac {\beta_ {a}}{1 + \mathrm{e} ^ {\beta_ {b} - \beta_ {c} t}}, t \in [ 0, T ]. (\mathrm{B5})
$$

where $N ( t )$ is the cumulative number of software users at time $t , \beta _ { a }$ is the ceiling number of software users, $\beta _ { b }$ is the constant of integration that positions the curve on the time scale, and $\beta _ { c }$ is the rate of user growth coefficient.

The benefits of trust under perpetual and subscription licensing are given by,

$$
\begin{array}{l} B _ {p} = \gamma_ {p} \big (N (T) - N (t _ {0}) \big), t _ {0} \in [ 0, T ], \\ B _ {s} = \int_ {t _ {0}} ^ {T} \gamma_ {s} N (t) d t, t _ {0} \in [ 0, T ]. \end{array}\tag{B6}
$$

(B7)

Numerical analysis validates that under both licensing models, the optimal launch timing becomes earlier as the benefit of trust or the failure cost increases, as shown in Figures B8 and B9. We also observe that under perpetual licensing, the firm should launch before a time when the user growth rate starts to increase rapidly, as shown in Figures B8a and B9a. However, the firm under subscription licensing could choose the launch time much later than the software release time, as shown in Figures B8b and B9b. These observations are qualitatively consistent with our main findings in Propositions 1 and 2.

## • Optimal Launch Time

![](/api/attachments/VQZ5YDFG/fulltext/images/5526a679b47ed6aaac41154883b71c76f8b91ee585e31a1bfb50be1499259769.jpg)

![](/api/attachments/VQZ5YDFG/fulltext/images/3b0cfb6c1918f5ffa5d4031c6b615c3414993696697c1788cd39a9f867e0ba20.jpg)  
Note: The optimal launch timing under perpetual licensing in Figure B9a is: $t _ { 0 } ^ { * } = 0 . 7 5$ when $c _ { g } = 0 . 0 1 ; t _ { 0 } ^ { * } = 0 . 1 3$ when $c _ { g } = 2 0 ; t _ { 0 } ^ { * } = 0 . 1$ when $c _ { g } = 5 0$ . The optimal launch timing under subscription licensing in Figure B9b is $t _ { 0 } ^ { * } = 0 . 7 5$ when $c _ { g } = 0 . 0 1 ; t _ { 0 } ^ { * } = 0 . 2 3$ when $c _ { g } = 2 2 ;$ $t _ { 0 } ^ { * } = 0$ when $c _ { g } = 5 0 . \mathrm { , }$ )

Figure B9. Optimal Launch Strategies under Different Failure Costs with S-Shaped User Growth Model

## (2) User Growth Model with an Attrition Rate under Subscription Licensing

Under subscription licensing, users have the option to exit the subscription if they do not find the software satisfying. Thus, in this subsection, we denote the attrition rate of installed users as $\beta _ { 1 }$ . Under subscription licensing, the cumulative number of software users at time ?? is thus given by

$$
N (t) = \left\{ \begin{array}{l l} \beta t - \beta_ {1} t, & t \in [ 0, \tau_ {N} ], \\ \beta \tau_ {N} - \beta_ {1} t, & t \in (\tau_ {N}, T ], \end{array} \right.
$$

where $N ( t ) \geq 0$

Numerical experiments are conducted to examine the optimal launch strategies and how the changes in $\beta _ { 1 }$ impact the optimal launch time of BBPs. Figure B10 demonstrates that our main findings in Proposition 2 remain valid. Figure B11 further shows that the firm should delay or cancel the launch of BBP as $\beta _ { 1 }$ increases.

![](/api/attachments/VQZ5YDFG/fulltext/images/d7a1bae3ce6683fdc04ce9932c6ed14b50f98c8c9e0d9ff4e172aff54b1e2340.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 4, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ?? = 1, ?? = 0.5, ??<sub>??</sub> = 2,

![](/api/attachments/VQZ5YDFG/fulltext/images/981562395f1cdb854d6b6056ef41a6571bf78325739d57d0bb00c775625fa7ad.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 4, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ?? = 1, ?? = 0.5, ??<sub>??</sub> = 1,  
Figure B10. Optimal Launch Strategies under Subscription Licensing with a User Attrition Rate

![](/api/attachments/VQZ5YDFG/fulltext/images/7a173c514b6bcc8323c0604942854db3879c957b8998d47b72310b9c81eb6d9d.jpg)  
(?? = 0.75, ??<sub>??</sub> = 0.5, ?? = 0.5, ?? = 4, ??<sub>??</sub> = 9, ??<sub>??</sub> = 4, ?? = 1, ?? = 0.5, ??<sub>??</sub> = 2, ??<sub>??</sub> = 1 ??<sub>??</sub> = 3, ?? = 36)  
Figure B11. Impact of $\beta _ { 1 }$ on the Optimal BBP Launch Strategy under Subscription Licensing

## About the Authors

Nan Feng is a professor of information management and management science at Tianjin University, China. He received his PhD degree in management science from Tianjin University in 2007. His current research interests include social media, the economics of information systems, information security, and business analytics. He has published in MIS Quarterly, Journal of the Association for Information Systems, Decision Support Systems, and Information & Management, among others.

Tianlu Zhou is a PhD candidate in the Department of Information Management and Management Science at the College of Management and Economics, Tianjin University. Her research interests include information security and business analytics. Her work has appeared in the proceedings of the International Conference on Information Systems (ICIS) and the Pacific Asia Conference on Information Systems (PACIS).

Haiyang Feng is a professor of information management and management science at the College of Management and Economics, Tianjin University, China. He received his PhD in management science from Tianjin University. His research interests include the economics of information systems, platform strategy, and business analytics. He has published in MIS Quarterly, Journal of the Association for Information Systems, International Journal of Electronic Commerce, and International Journal of Production Economics, among others.

Minqiang Li is a professor in the Department of Information Management and Management Science at Tianjin University, China. He received his doctoral degree in management sciences from Tianjin University. His research interests include management science and decision support, ICT strategy, e-commerce, data mining and business intelligence, and evolutionary computation. His papers have appeared in MIS Quarterly, Management Science, Journal of the Association for Information Systems, Journal of Management Information Systems, European Journal of Operational Research, and other venues.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
