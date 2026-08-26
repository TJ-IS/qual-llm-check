---
otero_id: 7738
otero_key: "54PX6ZEA"
title: "To outsource or not: The impact of information leakage risk on information security strategy"
authors: "Nan Feng; Yufan Chen; Haiyang Feng; Dahui Li; Minqiang Li"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103215"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

To Outsource or Not: The Impact of Information Leakage Risk on Information Security Strategy

Nan Feng, Yufan Chen, Haiyang Feng, Dahui Li, Minqiang Li

![](/api/attachments/54PX6ZEA/fulltext/images/d4d0fbc99bf5f369fba117743b889be43e9926b6b70ef9633e5f4cb7c387613e.jpg)

PII: S0378-7206(18)30702-X

DOI: https://doi.org/10.1016/j.im.2019.103215

Reference: INFMAN 103215

To appear in: Information & Management

Received Date: 27 August 2018

Revised Date: 1 October 2019

Accepted Date: 12 October 2019

Please cite this article as: Feng N, Chen Y, Feng H, Li D, Li M, To Outsource or Not: The Impact of Information Leakage Risk on Information Security Strategy, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103215

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# To Outsource or Not: The Impact of Information Leakage Risk on Information Security Strategy

Nan Feng <sup>a</sup>, Yufan Chen <sup>a</sup>, Haiyang Feng <sup>a</sup>, Dahui Li <sup>b</sup>, Minqiang Li <sup>a</sup>

<sup>a</sup> College of Management and Economics, Tianjin University, Tianjin 300072, P. R. China

<sup>b</sup> Labovitz School of Business and Economics, University of Minnesota Duluth, Duluth, MN

55812-2496, United States

\* Corresponding author at: College of Management and Economics, Tianjin University, 92

Weijin Road, Nankai District, Tianjin 300072, China. Tel.: +86-22-87371302.

E-mail addresses: fengnan@tju.edu.cn (N. Feng), cyf\_lana@tju.edu.cn (Y. Chen),

hyfeng@tju.edu.cn (H. Feng), dli@d.umn.edu (D. Li), mqli@tju.edu.cn (M. Li).

Abstract：Emerging studies advocate that firms shall completely outsource their information security for cost and technical advantages. However, the risk of information leakage in outsourcing to managed security service providers (MSSPs) is overlooked and poses a confidentiality threat. We develop analytical models to describe several strategies for firms to consider when they decide to outsource to MSSPs. Based on our results, we suggest partial outsourcing as an alternative strategy when the firm faces information leakage risk. Besides, we suggest that in-house information security strategy is the optimal solution when the risk of being attacked is low regardless of the risk of information leakage. We then extend scenarios to the competitive environment where firms that are in the same market are highly likely to choose the same strategy.

Keywords: information security strategy; managed security service; information leakage; partial outsourcing

## 1. Introduction

Increases in the scale, scope, and sophistication of information security breaches and hacker attacks lead firms to seek advanced security expertise and technologies to gain competitive advantage [1,2]. In addition to developing in-house information security capabilities, firms can outsource their information security to managed security service providers (MSSPs) who provide security services such as firewall, intrusion detection system (IDS), intrusion prevention system (IPS), virtual private network, security event monitoring, patch management and upgrade, security assessment and security audit, and emergency response. The market for managed security services (MSS) has grown multifold over the years. A 2017 survey by PwC (PricewaterhouseCoopers) suggests that nearly two-thirds of the responding firms worked with MSSPs to manage and enhance their cybersecurity.

Although information security is considered a critical business activity [3], firms, especially small- and mid-sized firms, outsource to MSSPs because the complexity and cost with in-house security development increase dramatically, and MSSPs have technological advantages in dealing with vulnerabilities and threats [4]. Nevertheless, whether MSSPs can meet client firms’ security requirements remains unclear. Introducing an MSSP in a firm’s business relationship may increase the uncertainty in the firm’s business operations and lead to failures in information protection [5]. Firms realize they have to absorb the monetary losses stemming from MSSPs. IBM (2016) reported that the average per capita cost of data breaches caused by third parties increased from \$158 to \$172 per record and that 25% of the data breaches were the result of human factors, including those of third parties. Therefore, the use of MSSPs may be jeopardized by information leakage.

Information leakage is “the intentional or unintentional disclosure of information to an actor that is not explicitly authorized to have access to the information” [6]. When a client firm outsources its information security, the MSSP may reveal the firm’s sensitive data or knowledge to outsiders. Even if the MSSP maintains a secure environment, information may leak due to technical failures, like misconfiguration, or that the MSSP sells a firm’s information for profit [7–9]. The underlying cause of the problem is the migration of the client firm’s information to the MSSP [10].

To understand what client firms think of the risk of information leakage by the MSSP, we conducted preliminary interviews with twelve firms across various industries. Seven firms highlighted the importance of information confidentiality and expressed concerns about data leaked through the MSSP. They also emphasized the significance of choosing a reliable MSSP.

In addition, five of the twelve firms identified information leakage risk as a key factor affecting their outsourcing decision to the MSSP. Two of the twelve firms claimed that they intended to protect core business operations in-house in case of information leakage. These findings confirm that information leakage is a major risk considered by a firm in the decision to outsource to an MSSP.

Knowing that an MSSP has both advantages and disadvantages, we investigate the role of information leakage in a client firm’s outsourcing decision-making process. One advantage for a firm to outsource information security is the potential low costs and technical advantages of the MSSP. On the other hand, the firm may develop in-house security protection for the fear of leaking data by an MSSP, especially for core business like enterprise resource planning and product development[11]. In addition, there may also be a mixture of the two strategies that balances the benefit and risk of outsourcing to an MSSP, which we call partial outsourcing. Therefore, the present study aims to answer the following two research questions: (1) How does the risk of information leakage affect a firm’s outsourcing decision? (2) Under what conditions should a firm adopt full, partial, or no outsourcing?

We build game theoretical models to describe how a firm decides between in-house security management and outsourcing to an MSSP. We also compare the utility that a firm could derive from different strategies. This study contributes to the extant theoretical studies of the economics of information security in two aspects. First, we consider partially outsourcing a firm’s information security and verify the feasibility of this strategy in an analytical model. Second, we advance the extant theoretical research on the economics of information security by first introducing information leakage to the models.

The structure of the paper is as follows. We review the literature in the next section and then present an analytic model by integrating the effect of information leakage on information security outsourcing. Next, we compare the trade-offs among different strategies. Further, we examine a firm’s optimal decision in a competitive environment. Finally, we discuss the findings and draw implications for future research and practice.

## 2. Literature Review

Prior literature has advocated the benefits of adopting MSS, including sharing security information and access to security-enabling resources and expertise [12]. The MSS approach enables a firm to internalize the externalities of information security investment and eliminate the inefficiencies of investment [13,14]. However, drawbacks are also considered such as interdependency risk [15], service quality uncertainty, and the MSSP’s bankruptcy risk [16].

Hui et al. [15] proposes that there is greater threat from hackers once an MSSP’s network demonstrates system interdependency. Ding et al. [16] reveals that the decision to outsource is relatively insensitive to the variation in service quality but highly sensitive to the risk of an MSSP’s bankruptcy. Moreover, Ding et al. [17] also examines the characteristics of optimal MSSP contracts with regard to moral hazards and concludes that optimal contracts are based on performance. The effects of transaction costs on an MSSP’s pricing strategies are also examined [18]. Lee et al. [19] proposes a multilateral contract that can solve the double moral hazard problem. Nevertheless, externality has a significant effect on outsourcing by either offering benefits or posing risks, depending on whether an MSSP develops positive or negative externality. Positive externality allows an MSSP to prevent recognized attacks using information obtained from other firms. However, there is also a negative externality when hackers target firms with lower security capabilities [20]. Furthermore, in a study of the scenario when competitors outsource to a single MSSP, Cezar et al. [21,22] suggests that competitive externality may lead to customer switching and that quality advantage is not a prerequisite for a firm to outsource security. Instead, a firm’s outsourcing decision is determined by the type (positive or negative) and the degree of externality.

To our best knowledge, we have not seen studies that examine information leakage as a major risk of information security outsourcing. The prior literature of general outsourcing suggests that outsourcing decisions carry the risk of information leakage, which leads to the firm’s core competencies being transferred to a wider industry context [8]. In terms of R&D outsourcing, Nimubona et al. [23] examines the impacts of involuntary information leakage on a firm’s profits and welfare. García-Vega and Huergo [24] proposes that technology leakage may amplify fixed transactions and that firms would be averse to outsource R&D performance [25]. For example, there may be a leakage of demand information to unintended recipients by using a common upstream supplier in a supply chain [26].

The literature on the technical issues of information leakage confirms that information leakage may happen during the process of detection and profiling [7,10,27,28]. The technologies used for supervising and detecting a firm’s traffic load on a network, such as deep packet inspection, allow an MSSP to access all communications between a client application and a server. Moreover, malicious insiders may configure the IDS to leak information [10]. The privacy leakage metric for IDS is based on the theory of quantitative information flow analysis [29,30] and Shannon entropy [28]. To quantify the loss of leakage under general conditions, the “M-Score” method reveals the amount and sensitivity of leaked data and identifiable factors of severity [31]. Vavilis, Petković, and Zannone [32] further considers the ability to identify the data subjects of leaked information.

In the outsourcing of information security, the risk of information leakage may be greater than that in any other types of outsourcing. In contrast to the aforementioned studies, this study focuses on a firm’s decision to outsource information security or to retain information security in-house by assessing the risk of information leakage. In addition, a firm can adopt a partial (or selective) outsourcing strategy, which is a combination of in-house development and full outsourcing. This implies that it is optional to choose some business processes to protect inhouse and outsource the rest of the processes. Shy et al. [33] analyzes the partial outsourcing strategy in product markets. As a mixture of in-house efforts and fee-for-service outsourcing, partial outsourcing could be a viable strategy under certain conditions [34]. It is suggested that partial outsourcing has a higher success rate than full outsourcing or total insourcing decisions for IT companies [35]. Wang et al. [36] finds three strategies that consider non-core business: full, partial, and no outsourcing. In the manufacturing industry, partial outsourcing is viable except for vertical integration and exclusive outsourcing.

The underlying market uncertainty also impacts the optimal proportion of outsourced production [37]. Choi [38] investigates outsourcing decisions under conditions of both certainty and uncertainty. The study determines that if external suppliers offer cost benefits, uncertainty costs in outsourcing ensure that partial outsourcing is optimal for risk-averse firms. In terms of market uncertainty, the proportion of outsourcing along with investment efficiency helps firms determine the timing of outsourcing [39]. In addition to partial outsourcing, Cho and Chan [11] categorizes a firm’s business operations into core and non-core. They find that cost advantages would promote outsourcing for non-core operations, whereas technology advantages would encourage outsourcing for core business operations.

In the information security literature, few have considered this type of outsourcing strategy. Cezar et al. [2] divides the protection system into two different but related functions, prevention and detection, to choose between using a single or two different MSSPs. In this scenario, we consider partial outsourcing strategy based on the division of core and non-core business operations and posit that the risk of information leakage varies for both core and non-core business. While core business is key to a firm’s competence, non-core business supports the firm’s operation and development. This distinction forms the basis for adopting a certain partial outsourcing strategy.

Game theory is generally applied in the outsourcing literature to understand the contract between a firm and an MSSP, which implies that it is a seller’s market where MSSPs govern the pricing and propose the contract. Under such an assumption, the prior literature mainly focuses on the MSSP’s decision-making and contract design by taking into account the MSSP’s characteristics such as cost efficiency, multiple clients, security externality, and system interdependency [15,19,20]. Several studies also review the firm-MSSP relationship from the firm’s perspective. When a firm has strong bargaining power or requires customized services, it will propose a contract. Cezar et al. [2] analyzes the need for outsourcing prevention and detection on different MSSPs. Ji et al. [40] indicates that a reward-based contract is better than a penalty-based contract regarding outsourcing activities such as profiling and monitoring. A penalty-based contract typically consists of a fixed service fee and penalty for degraded services [2,13,15,20,22,40–42], while a reward-based contract includes a service fee and a reward for successfully detecting an attack [2,40]. Cezar et al. [2] also proposes a penalty-and-reward contract by combining the penalty-based contract for prevention and the reward-based contract for detection when outsourcing to a single MSSP. In addition, a multilateral contract is an evolution of a penalty-based contract in which MSSPs are required to compensate firms for suffering a loss due to externality [19].

The above literature review suggests that information leakage is a main deterrence for outsourcing and that there may be a variation of outsourcing strategies considering the risk of information leakage.

## 3. A Firm’s Information Security Strategies

The present study considers that a firm chooses whether to outsource its information security or to use an in-house strategy. We start with an assessment of information systems risk to measure external threats and the value of information assets, which refer to resources that support and ensure a firm’s business operations, such as information, systems, networks, software, and hardware. We classify these assets as assets of core and non-core business operations. Therefore, a firm can choose from four types of information security strategies, which can be identified as (1) Strategy IN: developing security protection in-house; (2) Strategy ONC: outsourcing only non-core business and protecting core business in-house; (3) Strategy OC: outsourcing core business and protecting non-core business in-house; and (4) Strategy OF: outsourcing all businesses. Among these four types of security strategies, ONC and OC are partial outsourcing.

To describe a firm’s security environment, we model security attacks faced by the firm as follows. We assume that a firm faces a probability of hacker attacks at $p \in \left( 0 , 1 \right)$ . To seek protection from attacks, the firm develops a certain level of security quality $q _ { f }$ , which determines the firm’s ability to identify and prevent attacks. Similarly, if the firm decides to outsource information security, the MSSP should determine the level of security quality $q _ { m }$ during the contract period. Either $q _ { f }$ or $q _ { m }$ is $0 < q _ { f } , q _ { m } < 1$ . This study excludes situations where the firm takes no measures $( q _ { f } , q _ { m } = 0 )$ or it is protected against all threats $( q _ { f } , q _ { m } = 1 )$ ). Irrespective of whether the firm applies in-house strategy or outsources to an MSSP, there is a possibility of being attacked and incurring a certain loss. We calculate the probability that the loss occurs as $p \big ( 1 - q _ { j } \big )$ where $j \in \left\{ f , m \right\}$ represents either the firm or the MSSP. The value of the firm’s information assets is assessed as . Thus, the firm will incurv a loss of $p ( 1 - q _ { j } ) \nu$ .The quality of a security system determines the cost to be paid for security protection, representing a convex relationship between cost and security quality. Congruent with the Kai-Lung model [15], cost is expressed $\mathrm { a s } { \frac { 1 } { 2 } } c _ { j } q _ { j } ^ { 2 }$ , where $c _ { j }$ is a cost coefficient and $q _ { j }$ is security level.

When a firm collaborates with an MSSP for its information security, a contract is signed. A bilateral refund type of contract is widely adopted in the information security industry. For example, IBM’s MSS charges its clients a fixed service fee for each period and pays a penalty when a firm suffers security breaches [43]. We assume service fee as ??and compensation ratio (“liability”) as $\beta \in \left[ 0 , 1 \right]$ in the contract based on the service level agreement. Compensation is simplified as the MSSP provides refunds based on a ratio. If the firm suffers a loss of duev to hacker attacks, the MSSP compensates the firm by $\beta \nu$

Selecting an outsourcing strategy implies that the firm must bear the loss resulting from $\mathbf { M S S P } ^ { \prime }$ s access to a firm’s information system might lead to a certain amount of leakage loss that is estimated by the unit loss of leakage and the importance of data leaked to competitors. If the MSSP adheres to the confidentiality agreement, there would be a minimal unit loss of leakage. The firm suffers a higher unit loss if there are errors resulting in unintentional $\mathrm { { _ { o r } } }$ intentional information disclosure. Parameter $d$ describes the ratio of the loss from leaked core information to that of non-core information. The information that contains knowledge of core business is more essential to the firm and more damaging when leaked. In particular, the possible loss from outsourcing core business is $\nu _ { c } d l$ and that of non-core business is $\nu _ { n c } l$

Table 1. Model Notation

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $v$ </td><td>Value of information assets that support the firm&#x27;s overall business operations ( $v > 0, v = v_c + v_{nc}$ )</td></tr><tr><td> $v_c$ </td><td>Value of information assets that support the firm&#x27;s core business operations</td></tr><tr><td> $v_{nc}$ </td><td>Value of information assets that support the firm&#x27;s non-core business operations</td></tr><tr><td> $p$ </td><td>Probability of a hacker attack ( $0 < p < 1$ )</td></tr><tr><td> $q_m$ </td><td>Security quality provided by the MSSP ( $0 < q_m < 1$ )</td></tr><tr><td> $q_m^i$ </td><td>Security quality provided by the MSSP in terms of core or non-core business operations ( $i \in \{c, nc\}$ ) ( $0 < q_m^i < 1$ )</td></tr><tr><td> $q_f$ </td><td>The firm&#x27;s security quality ( $0 < q_f < 1$ )</td></tr><tr><td> $q_f^i$ </td><td>The firm&#x27;s security quality to protect core or non-core business operations ( $i \in \{c, nc\}$ ) ( $0 < q_f^i < 1$ )</td></tr><tr><td> $c_m$ </td><td>Cost coefficient of the MSSP</td></tr><tr><td> $c_f$ </td><td>Cost coefficient of the firm</td></tr><tr><td> $F$ </td><td>Fixed fee paid by the firm to the MSSP in full outsourcing strategy</td></tr><tr><td> $F^i$ </td><td>Fixed fee paid by the firm to the MSSP when outsourcing only core or non-core business operations ( $i \in \{c, nc\}$ )</td></tr><tr><td> $\beta$ </td><td>Ratio of compensation paid by MSSP to the firm&#x27;s loss ( $0 < \beta < 1$ )</td></tr><tr><td> $\beta^i$ </td><td>Ratio of compensation paid by MSSP to the firm&#x27;s loss when outsourcing only core or non-core business operations ( $i \in \{c, nc\}$ ) ( $0 < \beta^i < 1$ )</td></tr><tr><td> $k$ </td><td>Coefficient between  $F(F^i)$  and  $\beta(\beta^i)$ </td></tr><tr><td> $l$ </td><td>Unit loss of information leakage when the firm outsources the security of non-core business ( $0 < l < 1$ )</td></tr><tr><td> $d$ </td><td>Ratio of unit loss of information leakage of core business to that of non-core business. ( $0 < dl < 1$ , represents the unit loss of leakage of core business)</td></tr></table>

Table 1 shows the variables included in the model with the following assumptions:

Assumption 1: $c _ { m } < c _ { f }$ ensures that when information security is outsourced to an MSSP, the firm will have a cost advantage.

Assumption 2: $0 < q _ { j } < 1 , 0 < q _ { j } ^ { i } < 1 ( i \in \{ c , n c \}$ represents core or non-core business operations; $j \in \left\{ f , m \right\} ,$ ) represents the firm and the MSSP ensures that the analysis will not reach a corner solution.

Assumption 3: $\beta = k F , \beta ^ { i } = k F ^ { i } ~ ( 0 < k < 1 , ~ i \in \{ c , n c \}$ represents core or non-core business operations) implies that compensation ratio has a linear correlation with service fee.

The more a firm pays, the higher the ratio of compensation refunded by the MSSP.

Assumption 4: $d > 1$ and $d l < 1$ implies that outsourcing of core business has a higher unit loss.

Subsequently, the firm’s utility can be determined for each of the four strategies.

## 3.1 In-house: Strategy IN

If the firm develops in-house security protection, the expected utility is as follows:

$$
u _ {i n - \square o u s e} = v \big [ 1 - p \big (1 - q _ {f} \big) \big ] - \frac {1}{2} c _ {f} q _ {f} ^ {2}.\tag{1}
$$

The first term represents the remaining value after a successful attack on the firm’s information assets. The second term represents the cost of investment incurred in security protection.

## 3.2 Full Outsourcing: Strategy OF

The contracting problem is modeled in line with Cezar et al. [2]. The sequence of events is as follows.

Stage 1. The firm decides to outsource information security and offers a penalty-based contract $\left[ F , \beta \right]$

Stage 2. If the MSSP accepts the contract, it provides security quality $q _ { m }$ ; otherwise, the game ends.

Stage 3. If security loss is realized, the MSSP pays compensation, calculated by $\beta$

expected payoff are determined as follows:

$$
u _ {f u l l} = v [ 1 - p (1 - q _ {m}) ] + v p (1 - q _ {m}) \beta - F - v _ {n c} l - v _ {c} d l,\tag{2}
$$

$$
\pi_ {f u l l} = F - v p (1 - q _ {m}) \beta - \frac {1}{2} c _ {m} q _ {m} ^ {2}.\tag{3}
$$

$u _ { f u l l }$ is the estimated compensation that the MSSP refunds if it fails to prevent the attack. $\nu _ { n c } l + \nu _ { c } d l$ represents the loss arising from information leakage. For $\pi _ { f u l l } .$ , the middle term is compensation. The last term is the cost that the MSSP incurs in security protection.

## 3.3 Partial Outsourcing: Strategy ONC and Strategy OC

Two specific strategies exist for partial outsourcing: outsourcing the information security of only non-core business and that of only core business.

If outsourcing only non-core business exists (i.e., Strategy ONC), the firm invests in core business to achieve security quality $q _ { f } ^ { c }$ and pays the MSSP to receive security quality $q _ { m } ^ { n c }$

The expected utility of the firm and the expected payoff for the MSSP are determined as follows:

$$
u _ {n o n - c o r e} = v _ {c} \big [ 1 - p \big (1 - q _ {f} ^ {c} \big) \big ] - \frac {1}{2} c _ {f} q _ {f} ^ {c 2} + v _ {n c} [ 1 - p (1 - q _ {m} ^ {n c}) ]
$$

$$
+ v _ {n c} p (1 - q _ {m} ^ {n c}) \beta^ {n c} - F ^ {n c} - v _ {n c} l,\tag{4}
$$

$$
\pi_ {n o n - c o r e} = F ^ {n c} - v _ {n c} p (1 - q _ {m} ^ {n c}) \beta^ {n c} - \frac {1}{2} c _ {m} q _ {m} ^ {n c 2}.\tag{5}
$$

The first term of $u _ { n o n - c o r e }$ represents the firm’s utility of in-house development for core business, and the second term is the firm’s utility of outsourcing non-core business. $\nu _ { n c } l$ represents the loss resulting from leaking non-core information. $\pi _ { n o n - c o r e }$ is the MSSP’s expected payoff when it only provides service for the firm’s non-core business.

Similarly, if the firm outsources only core business (i.e., Strategy OC), it invests in its noncore business to achieve security quality $q _ { f } ^ { n c }$ and pays the MSSP to receive security quality $q _ { m } ^ { c }$ . The firm’s utility and the MSSP’s payoff are as follows:

$$
u _ {c o r e} = v _ {n c} \big [ 1 - p \big (1 - q _ {f} ^ {n c} \big) \big ] - \frac {1}{2} c _ {f} q _ {f} ^ {n c ^ {2}} + v _ {c} [ 1 - p (1 - q _ {m} ^ {c}) ]
$$

$$
+ v _ {c} p (1 - q _ {m} ^ {c}) \beta^ {c} - F ^ {c} - v _ {c} d l,\tag{6}
$$

$$
\pi_ {f u l l} = F ^ {c} - v _ {c} p (1 - q _ {m} ^ {c}) \beta^ {c} - \frac {1}{2} c _ {m} q _ {m} ^ {c 2}.\tag{7}
$$

## 4. Model Analysis

## 4.1 In-house: Strategy IN

When a firm chooses to develop the in-house strategy, it selects an optimal $q _ { f } ^ { * }$ to maximize the utility, which can be expressed as

$$
\max _ {q _ {f}} u _ {i n - \square o u s e} = v \left[ 1 - p \left(1 - q _ {f}\right) \right] - \frac {1}{2} c _ {f} q _ {f} ^ {2}.\tag{8}
$$

Differentiating $u _ { i n - h o u s e }$ with respect to $q _ { f }$ , the optimal effort $q _ { f } ^ { * } = p \nu / c _ { f }$ is obtained. The firm’s best utility from in-house development is derived as

$$
u _ {i n - \square o u s e} ^ {*} = \frac {p ^ {2} v ^ {2}}{2 c _ {f}} + (1 - p) v.\tag{9}
$$

Lemma 1: The security quality of the firm linearly increases in the value of information assets but linearly decreases in the firm’s cost coefficient, that is, $\partial q _ { f } ^ { * } \big / \partial \nu > 0$ and $\partial { q } _ { f } ^ { * } / \partial { c } _ { f } > 0$

## 4.2 Full Outsourcing: Strategy OF

Backward induction is used to solve the firm’s contracting problem in section 3.2. In Stage 2 of the game, the MSSP determines its optimum quality by maximizing its profit $\pi _ { f u l l }$ . The

first derivative of $\pi _ { f u l l }$ with respect to $q _ { m }$ is

$$
\frac {\partial \pi_ {f u l l}}{\partial q _ {m}} = p v \beta - c _ {m} q _ {m},\tag{10}
$$

and quality is obtained as $\begin{array} { r } { q _ { f } ^ { * } = \frac { p v \beta } { c _ { m } } } \end{array}$ . In anticipation of how the MSSP decides its best response, the firm determines fixed service fee and compensation according to the linear relationship, both of which comprise the contract $\left[ F , \beta \right]$ in Stage 1 of the game.

The firm maximizes its anticipated utility by establishing the terms of the contract. By solving the problem

$$
\max _ {(F, q _ {m})} u _ {f u l l} = v [ 1 - p (1 - q _ {m}) ] + v p (1 - q _ {m}) \beta - F - v _ {n c} l - v _ {c} d l,\tag{11}
$$

the following solutions are obtained:

$$
q _ {m} ^ {*} = \frac {1}{2} \Big (1 - \frac {1}{k p v} + \frac {p v}{c _ {m}} \Big);\tag{12}
$$

$$
F ^ {*} = \frac {k p ^ {2} v ^ {2} - c _ {m} + k p v c _ {m}}{2 k ^ {2} p ^ {2} v ^ {2}}.\tag{13}
$$

Lemma 2: The security quality provided by the MSSP increases in the value of information assets but decreases in the ${ \bf M S S P } \mathrm { \ ' } _ { \mathrm { s } }$ cost coefficient, that is, $\partial q _ { m } ^ { * } / \partial \nu > 0$ and $\partial q _ { m } ^ { * } / \partial c _ { m } > 0$

Next, we examine the characteristics of service fee $F ^ { * }$ and compensation term $\beta ^ { * }$ Figure 1 illustrates how $F ^ { * }$ and $\beta ^ { * }$ vary with $p v ,$ , where $k = 0 . 2 , c _ { m } = 5 6$

![](/api/attachments/54PX6ZEA/fulltext/images/6dee38aaac40d6f6a87912b5efc5f35414c60a9cbd07641f42c86262e80efbef.jpg)

![](/api/attachments/54PX6ZEA/fulltext/images/d2a47fe683e83ca2de31c096fa3562926676e5fb3411727fbcef04b6de2d75be.jpg)  
Figure 1. Trend of variation $F ^ { * }$ and $\beta ^ { * }$

To estimate the trend of service fee $F ^ { * }$ , the following two cases must be considered: Case (i): when $0 < p v < \frac { 2 } { k } , \hat { \sigma } F ^ { * } / \hat { \sigma } p \nu > 0$ $F ^ { * }$ increases with an increase in $p \nu$ Case (ii): when $\scriptstyle p v > { \frac { 2 } { k } } , \ \partial F ^ { * } / \partial p \nu < 0$ $F ^ { * }$ decreases with an increase in $p \nu$

Based on Assumption 2, we limit $p \nu$ in $\begin{array} { r } { \left[ - \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } , \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } \right] } \end{array}$ Figure 1 shows that the curve first increases and then decreases.

The rising curve’s average rate of change is calculated at $\begin{array} { r } { r _ { u p } = \frac { 4 + c _ { m } k } { 1 6 + 4 c _ { m } k - 4 \sqrt { c _ { m } k ( 4 + c _ { m } k ) } } , } \end{array}$ which equals to the slope of the line from the critical point (where $\begin{array} { r } { p v = - \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } ) } \end{array}$ to the extreme point (where $\begin{array} { r } { p v = \frac { 2 } { k } ) } \end{array}$ . Similarly, we obtain the descending curve’s average rate of change at $r _ { d o w n } = \frac { 2 k \left[ \frac { 1 } { 8 } \binom { 4 } { m + \frac { 4 } { k } } - \frac { 2 c _ { m } } { c _ { m } k + \sqrt { c _ { m } k \left( 4 + c _ { m } k \right) } } \right] } { - 4 + c _ { m } k + \sqrt { c _ { m } k ( 4 + c _ { m } k ) } }$ . The mathematical result shows that $r _ { u p } >$ $r _ { d o w n }$ as well. When $c _ { m } k$ is high, we get $r _ { u p } \gg r _ { d o w n }$ and $\begin{array} { r } { - \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } < \frac { 2 } { k } \ll } \end{array}$ $\textstyle { \frac { c _ { m } } { 2 } } + { \frac { 1 } { 2 } } { \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } }$ . This implies that $F ^ { * }$ first increases rapidly with???? and then decreases much more smoothly, covering several conditions. According to Assumption 3, compensation term $\beta ^ { * }$ demonstrates a similar trend as that of $F ^ { * }$

Thus, the characteristics of the contract terms are demonstrated in Proposition 1.

Proposition 1:

(a) For values in $\begin{array} { r } { p \nu \in \left[ - \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } , \frac { 2 } { k } \right] . } \end{array}$ $F ^ { * }$ and $\beta ^ { * }$ increase in $p \nu$ at an average rate of $r _ { u p }$ , where $p \nu$ represents the estimated loss under no protection.

(b) For values in $\begin{array} { r } { p \nu \in \left[ \frac { 2 } { k } , \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { c _ { m } ( 4 + c _ { m } k ) } { k } } \right] , ~ F ^ { * } } \end{array}$ $\beta ^ { * }$ decrease in $p \nu$ at an average rate of $r _ { d o w n } ( r _ { u p } > r _ { d o w n } )$

Service fee and compensation ratio can initially increase rapidly and then gradually decrease with $p \nu$ , which represents the loss if assets are unprotected. When $p \nu$ is small and within a certain range, the firm is willing to pay more as the estimated loss increases in order to ensure that its assets are not excluded by the MSSP. There is an equivalent increase in compensation ratio due to the linear correlation. Service fee and compensation reduce gradually after the estimated loss reaches a certain value. Because of the increase in security quality as $p \nu$ attacks. Thus, it is acceptable for the firm to receive a lower proportion of compensation.

Past studies contend that outsourcing information security can provide better quality as well as cost savings. To verify the statement, we first compare the security quality of the two strategies and find that when $\begin{array} { r } { c _ { f } < \frac { 2 c _ { m } k p v ^ { 2 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } } . } \end{array}$ , the security quality of the firm’s own protection $q _ { f }$ is better than that of the MSSP. In contrast, outsourcing information security achieves a higher level of quality. Then, we compare the investment of both strategies. The optimal security quality is substituted into the cost function $\frac { 1 } { 2 } c _ { f } q _ { f } ^ { 2 }$ and compared with the optimal $F ^ { * }$ . When $c _ { f } < \frac { k p v ^ { 4 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } }$ , the service fee for outsourcing is lower than the cost of protecting information in-house; otherwise, the outsourcing strategy is expensive.

Proposition 2: A firm can achieve both cost and technical advantages (higher quality service) through outsourcing only when $c _ { m } < \frac { p \nu ^ { 2 } } { 2 } ~ \mathrm { a n d } ~ \frac { 2 c _ { m } k p \nu ^ { 2 } } { - c _ { m } + c _ { m } k p \nu + k p \nu ^ { 2 } } < c _ { f } <$ $\frac { k p \nu ^ { 4 } } { - c _ { m } + c _ { m } k p \nu + k p \nu ^ { 2 } }$

Outsourcing does not always lead to cost and technical advantages simultaneously. Low cost coefficient of the MSSP ensures a high security quality (proved by Lemma 2). A relatively large gap between the cost coefficient of the firm and that of the MSSP implies the benefit of cost saving through outsourcing. Moreover, a higher cost coefficient of the firm results in a decline in the firm’s security quality (proved by Lemma 1) and cost when the firm manages security in-house. The cost for in-house protection is calculated by $\frac { 1 } { 2 } c _ { f } q _ { f } ^ { 2 }$ and the result $\frac { p \nu ^ { 2 } } { c _ { f } }$ for the optimal situation is obtained. Quality declines faster than the increasing rate of $c _ { f } ,$ , thus reducing cost.

## 4.3 Partial Outsourcing: Strategy ONC and Strategy OC

A firm has two options when adopting a partial outsourcing strategy. First, the firm decides its security quality with regard to the value of assets to be protected in-house. The firm maximizes its expected utility of outsourcing by establishing terms in the contract. The problems are solved, respectively, as shown in the previous calculation of in-house and outsourcing strategies. The optimal value of each decision variable is shown in Table 2.

Table 2. Optimal Values of the Decision Variable

<table><tr><td rowspan="2">Choice of Strategy</td><td colspan="3">Optimal Value</td></tr><tr><td> $q_{f}^{i}$ </td><td> $q_{m}^{i}$ </td><td> $F^{i}$ </td></tr><tr><td>ONC</td><td> $\frac{pv_{c}}{c_{f}}$ </td><td> $\frac{1}{2}\left(1-\frac{1}{kpv_{nc}}+\frac{pv_{nc}}{c_{m}}\right)$ </td><td> $\frac{1}{2k}+\frac{(-1+kpv_{nc})c_{m}}{2k^{2}p^{2}v_{nc}^{2}}$ </td></tr><tr><td>OC</td><td> $\frac{pv_{nc}}{c_{f}}$ </td><td> $\frac{1}{2}\left(1-\frac{1}{kpv_{c}}+\frac{pv_{c}}{c_{m}}\right)$ </td><td> $\frac{1}{2k}+\frac{(-1+kpv_{c})c_{m}}{2k^{2}p^{2}v_{c}^{2}}$ </td></tr></table>

Based on Lemmas 1 and 2, $q _ { f } ^ { c }$ and $q _ { f } ^ { n c }$ are lower than $q _ { f } ^ { * }$ and $q _ { m } ^ { c } , \ q _ { m } ^ { n c }$ are lower than $q _ { m } ^ { * }$ . The following are several possibilities when comparing different security qualities:

For $q _ { f } ^ { * } > q _ { m } ^ { * }$ , there is $q _ { f } ^ { * } > q _ { m } ^ { c } , q _ { m } ^ { n c }$ . If the security quality of Strategy IN exceeds that of

Strategy OF, it $( q _ { f } ^ { * } )$ will be also higher than either security quality of the partial outsourcing strategies.

For $q _ { m } ^ { * } > q _ { f } ^ { * }$ , there is $q _ { m } ^ { * } > q _ { f } ^ { c } , q _ { f } ^ { n c }$ . If the security quality of Strategy OF exceeds that of Strategy IN, it $( q _ { m } ^ { * } )$ will be also higher than either security quality of the partial outsourcing strategies.

For $q _ { m } ^ { * } = q _ { f } ^ { * } , q _ { m } ^ { * } = q _ { f } ^ { * } > q _ { m } ^ { c } , q _ { m } ^ { n c } , q _ { f } ^ { c } , q _ { f } ^ { n c }$ : If the security quality of Strategy IN and Strategy OF are equal, $q _ { m } ^ { * } , q _ { f } ^ { * }$ will be the optimal security level of all strategies.

Therefore, the following can be proposed:

Proposition 3: The security quality of partial outsourcing is always lower than that of either in-house or full outsourcing.

Partial outsourcing compromises security quality to some extent. To achieve the maximum utility, lower quality would mitigate the cost, and the loss would be minimal because of the limited value of information assets. Security quality is critical to decision-making, especially for risk-averse firms that are inclined to choose either in-house or full outsourcing. National or regional mandatory standards for information security also require certain firms to consider security quality as a decision factor. If the firm adopts a partial outsourcing strategy to satisfy its requirements of high standards of both in-house and outsourced security, the firm should make a higher investment. For the in-house strategy, a higher investment decreases the firm’s utility. For the outsourcing strategy, mandatory security requirements increase the MSSP’s effort and lead outsourcing to be more beneficial because of superior cost efficiency [15]. Thus, a firm with mandatory security requirements tends to seek an MSSP for security protection.

The proofs of all the results are in the appendix.

## 5. The Firm’s Optimal Decision

The firm may need to establish the optimal security protection strategy to achieve the best utility. The optimal values are derived in the corresponding objective functions to obtain the information provided in Table 3. The proportion $\alpha$ is used to measure information assets that support the firm’s core business operations. In particular, the firm estimates its core assets at $\nu _ { c } = \alpha \nu$ and non-core assets at $v _ { n c } = ( 1 - \alpha ) v$ . Subsequently, the utilities of different strategies are compared to determine the superior and the inferior solutions.

Table 3. Best Utility of Different Strategies

<table><tr><td>Strategy</td><td>Firm&#x27;s Best Utility</td><td></td><td>Tab</td></tr><tr><td>IN</td><td></td><td> $\frac{p^{2}v^{2}}{2c_{f}} + (1 - p)v$ </td><td> $u_{in-□ouse}^{*}$ </td></tr></table>

$$
\left(1 - \frac {1}{2} p\right) v + \frac {p ^ {2} v ^ {2}}{4 c _ {m}} + \frac {(1 - k p v) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v ^ {2}} - v _ {c} d l - v _ {n c} l - \frac {1}{2 k}\tag{OF}
$$

$$
u _ {f u l l} ^ {*}
$$

$$
\frac {p ^ {2} v _ {c} ^ {2}}{2 c _ {f}} + (1 - p) v _ {c} + \left(1 - \frac {1}{2} p\right) v _ {n c} + \frac {p ^ {2} v _ {n c} ^ {2}}{4 c _ {m}} + \frac {(1 - k p v _ {n c}) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v _ {n c} ^ {2}}\tag{ONC}
$$

$$
- v _ {n c} l - \frac {1}{2 k}
$$

OC

$$
\frac {p ^ {2} v _ {n c} ^ {2}}{2 c _ {f}} + (1 - p) v _ {n c} + \left(1 - \frac {1}{2} p\right) v _ {c} + \frac {p ^ {2} v _ {c} ^ {2}}{4 c _ {m}} + \frac {(1 - k p v _ {c}) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v _ {c} ^ {2}}
$$

$$
- v _ {c} d l - \frac {1}{2 k}
$$

$$
u _ {c o r e} ^ {*}
$$

To decide the best strategy under a certain condition, the critical condition is established where the utilities of two different strategies are equal, which is expressed as an intersection of each strategy based on the value of unit loss of information leakage. The value of the intersection is provided in Table A.1 in the appendix.

Under the condition of $l _ { 2 4 } < l < l _ { 1 2 }$ , outsourcing of only non-core business has the highest utility, which implies that Strategy ONC is the best option. In addition, Strategy OC cannot be optimal. $l > l _ { 1 4 }$ indicates that Strategy IN is superior to Strategy OF. In this case, l also satisfies the condition of $l > l _ { 1 3 }$ , which implies that Strategy OC is worse than Strategy IN. Similarly, if $l _ { 3 4 } - l _ { 1 4 } > 0 , \ l _ { 3 4 } > l _ { 1 4 }$ . In other words, when Strategy IN is inferior to Strategy OF (i.e., $l < l _ { 1 4 } )$ , Strategy OC is also worse than Strategy OF (i.e., $l < l _ { 3 4 } )$ . Regardless of whether Strategy IN or Strategy OF is superior, Strategy OC is inferior to the better one of the former two (see the evidence in the appendix). Therefore, the following can be stated:

Proposition 4: Strategy ONC is superior when $l _ { 2 4 } < l < l _ { 1 2 }$ , whereas Strategy OC is a strictly dominating strategy.

When there is a high risk of information leakage, the firm prefers Strategy IN because the loss from information leakage exceeds the benefit from the MSSP’s cost advantage. In the case of a low risk of leakage, the firm tends to choose full outsourcing, which reduces the cost and achieves a higher level of security quality. With regard to medium-risk situations, outsourcing non-core business is the best choice. Outsourcing core business is always relatively the worst choice, because it is generally worse than either full outsourcing or in-house development.

![](/api/attachments/54PX6ZEA/fulltext/images/cb2c3925304fa10b2c1a51199bae36dbdb79f6f42b645b89db3abd7ea810ca60.jpg)  
Figure 2(a). Strategies reg. and pl

![](/api/attachments/54PX6ZEA/fulltext/images/fafe05cc3721d292572e56e5443575f69972ab71c73cdb1683241f2189ac2ed6.jpg)  
Figure 2(b). Strategies reg. ??and $c _ { m }$

![](/api/attachments/54PX6ZEA/fulltext/images/4d143a612108659e45a05b84ccaef645933d8a5ca4a5c515e07eda0f7b7536c0.jpg)  
Figure 2(c). Strategies reg. and l

Next, the optimal decision is discussed by adding another factor to the result. Figure 2 shows the strategies considering and ??, and l l $c _ { m }$ , and and l $\alpha$ . Figures 2(a)–2(c) illustrate a combination of the three security strategies: in-house, partial outsourcing, and full outsourcing.

Based on Figure 2(a), the risk of both hacker attack and information leakage is considered. A firm’s risk assessment should contain two parts: (1) quantifying the risk of being attacked and (2) evaluating the MSSP to estimate the risk of leakage. In the case of a low risk of attack, there is no need to use an MSSP. In-house security can keep the firm from information leakage risk and attack risk. In the case of a high risk of attack, the decision is more complex, and the importance of business information should be considered. Full outsourcing is the best choice when the firm faces a low risk of information leakage. However, as the risk of information leakage increases, the firm will choose more in-house protection. The optimal strategy will first change to Strategy ONC and then to Strategy IN.

Figure 2(b) implies that a firm should carefully defend core business when facing a medium risk of leakage. The difference between the security cost of the firm and that of the MSSP leads to a different strategy for non-core business. When cost advantage is minimal, the firm prefers to outsource information security of non-core business. In the case of a high cost coefficient, the ratio of compensation is high and even more than 1; thus, the firm benefits from the refund from the MSSP. Outsourcing of non-core business is not due to cost saving but rather the high refund that covers the loss.

Figure 2(c) shows that the optimal decision is always Strategy OF when the risk of information leakage is low enough. A reliable MSSP would attempt to maintain data under its control. Thus, outsourcing to an MSSP can yield the most utility. In contrast, when the risk is high, the optimal decision is always Strategy IN. In the case of a medium risk of information leakage, the firm should focus on securing core business. With the increase in the ratio of core assets, the optimal decision generally changes from Strategy OF to Strategy ONC, and finally, to Strategy IN. Therefore, some knowledge-based firms gradually change from outsourcing to in-house. A good example is the medical institution.

To summarize, a high risk of information leakage prompts the in-house strategy. A low risk stimulates the full outsourcing strategy. A medium risk may lead to the partial outsourcing strategy (Strategy ONC), especially when there is a high probability of hacker attacks or hidden cost advantages.

## 6. The Firms’ Optimal Decision in the Competitive Environment

This section extends the study to the firm’s optimal decision in the competitive environment where competition is considered a speculative risk [20]. Firms benefit from gaining competitors’ customers when competitors are attacked. Security-sensitive customers of a firm may switch from that firm if it does not protect the customers’ information to one that does. Therefore, information leakage is a factor that affects the competition among firms, especially when competing firms outsource to the same MSSP. The fact that the MSSP virtually connects competing firms’ systems together further increases a firm’s risk of data leakage to its competitors.

Though MSSPs should serve diverse clients, they usually focus on a particular industry and provide a particular service. Therefore, industrial guidelines often emphasize an MSSP’s focused industry as a factor for firms to consider before selecting the MSSP. An MSSP with similar clients has specialized expertise so that its client firms can benefit from the MSSP’s knowledge. However, the MSSP, being an “information sharing pool,” may allow one client firm’s leaked data to be collected by other clients. A firm may gain competitive advantages from receiving competitors’ information because such information is an important source of innovation [44].

This study considers the condition of only one MSSP and two firms. The strategic combinations of two firms include every possible combination of in-house, partial, and full outsourcing strategies. Because Strategy OC is always worse than others, it is not considered a possible choice. If a firm’s competitor adopts the in-house strategy, there will be no information leakage nor benefit availed from knowledge accumulation. If a firm’s competitor adopts the outsourcing strategy, the firm can fairly access leaked data. A shared MSSP may allow a firm to access all leaked data and absorb these data as its own knowledge, denoted as ??. In contrast, when the firm adopts the in-house strategy, it has a probability of $\theta$ to get its competitor’s leaked information. When both firms choose to outsource, the MSSP’s accumulated knowledge brings a positive externality ??, thus improving security quality, which is determined by the extent of outsourcing. For further investigation, two assumptions are added:

Assumption 5: $\begin{array} { r } { \varDelta ^ { s } = \left\{ \begin{array} { l l } { ( 1 - \alpha ) e } & { \mathrm { i f } \mathrm { S } = \mathrm { S t r a t e g y } 0 \mathrm { N C } } \\ { e } & { \mathrm { i f } \mathrm { S } = \mathrm { S t r a t e g y } 0 \mathrm { F } } \end{array} \right. } \end{array}$ , where $0 < 1 - \alpha < 1$ denotes the proportion of the value of non-core assets and ?? denotes the degree of positive externality. ?? indicates the competitor’s information strategy, where $\mathrm { ~ S ~ } \in \left\{ { \mathrm { S t r a t e g y ~ I N } } \right.$ ， Strategy ONC, Strategy OF}.

Assumption 6: $A ^ { S } = \left\{ \begin{array} { c c } { 0 } & { \mathrm { i f ~ S = S t r a t e g y ~ I N } } \\ { \eta v _ { n c } l } & { \mathrm { i f ~ S = S t r a t e g y ~ O N C } } \\ { \eta ( v _ { n c } l + v _ { c } d l ) } & { \mathrm { i f ~ S = S t r a t e g y ~ O F } } \end{array} \right.$ , where $0 < \eta < 1$

denotes the firm’s abortive capability to transform external information to internal value.

To explain the influence of externality, a general linear function is used in earlier studies (e.g., Hui et al. [15]; Lee et al. [19]). The firm’s security quality is expressed as $( 1 + \Delta ) { q } _ { m } ^ { * }$ Utilities of the three strategies are:

(a) In-house: Strategy IN

$$
\tilde {u} _ {i n - \square o u s e} = v \big [ 1 - p \big (1 - \tilde {q} _ {f} \big) \big ] - \frac {1}{2} c _ {f} \tilde {q} _ {f} ^ {2} + \theta A.\tag{14}
$$

(b) Partial Outsourcing: Strategy ONC

$$
\tilde {u} _ {n o n - c o r e} = v _ {c} \big [ 1 - p \big (1 - \tilde {q} _ {f} ^ {c} \big) \big ] - \frac {1}{2} c _ {f} \tilde {q} _ {f} ^ {c 2} + v _ {n c} [ 1 - p (1 - (1 + \varDelta) \tilde {q} _ {m} ^ {n c}) ]
$$

$$
+ v _ {n c} p [ 1 - (1 + \varDelta) \tilde {q} _ {m} ^ {n c} ] \tilde {\beta} ^ {n c} - \tilde {F} ^ {n c} - v _ {n c} l + A,\tag{15}
$$

$$
\tilde {\pi} _ {n o n - c o r e} = \tilde {F} ^ {n c} - v _ {n c} p [ 1 - (1 + \varDelta) \tilde {q} _ {m} ^ {n c} ] \tilde {\beta} ^ {n c} - \frac {1}{2} c _ {m} \tilde {q} _ {m} ^ {n c ^ {2}}.\tag{16}
$$

(c) Full Outsourcing: Strategy OF

??,

$$
\tilde {u} _ {f u l l} = v [ 1 - p (1 - (1 + \Delta) \tilde {q} _ {m}) ] + v p [ 1 - (1 + \Delta) \tilde {q} _ {m} ] \tilde {\beta} - \tilde {F} - v _ {n c} l - v _ {c} d l + \tag {17}
$$

$$
\tilde {\pi} _ {f u l l} = \tilde {F} - v p [ 1 - (1 + \varDelta) \tilde {q} _ {m} ] \tilde {\beta} - \frac {1}{2} c _ {m} \tilde {q} _ {m} ^ {2}.\tag{18}
$$

## 6.1 Impact of Knowledge Accumulation on Outsourcing

For the case of outsourcing, the firm’s contracting problem is solved using backward induction. The following solutions are obtained (Table 4).

Table 4. Optimal Values of the Decision Variable When Outsourcing

<table><tr><td colspan="3">Choice of optimal Value</td></tr><tr><td>Strategy</td><td> $\tilde{q}_{m}^{*}$ </td><td> $\tilde{F}^{*}$ </td></tr><tr><td>ONC</td><td> $\frac{kp^{2}v_{nc}^{2}(1+\Delta)^{2}+(-1+kpv_{nc})c_{m}}{2kpv_{nc}(1+\Delta)c_{m}}$ </td><td> $\frac{1}{2k}+\frac{(-1+kpv_{nc})c_{m}}{2k^{2}p^{2}v_{nc}^{2}(1+\Delta)^{2}}$ </td></tr><tr><td>OF</td><td> $\frac{kp^{2}v^{2}(1+\Delta)^{2}+(-1+kpv)c_{m}}{2kpv(1+\Delta)c_{m}}$ </td><td> $\frac{1}{2k}+\frac{(-1+kpv)c_{m}}{2k^{2}p^{2}v^{2}(1+\Delta)^{2}}$ </td></tr></table>

The solutions of Strategy ONC differ from those of Strategy OF only because of different values of $\nu _ { n c }$ and . Therefore, the solutions of Strategy OF are taken as examples to analyzev the influence of externality on security quality and service fee. The trend of the MSSP’s security quality, $\widetilde { q } _ { m } ^ { * } .$ , is divided into:

Case (i): when $0 < k p v < 1 , \ \partial \tilde { q } _ { m } ^ { * } / \partial \varDelta > 0$ and $\tilde { q } _ { m } ^ { * }$ increases in .

Case (ii): when ?????? > 1, $\partial \tilde { q } _ { m } ^ { * } / \partial \varDelta < 0 \ ( \partial \tilde { q } _ { m } ^ { * } / \partial \varDelta > 0 )$ and $\tilde { q } _ { m } ^ { * }$ decreases (increases) in provided that $\Delta < \Delta _ { \mathrm { o } } ( \varDelta > \varDelta _ { 0 } )$ $\Delta _ { 0 } \mathrm { = } - 1 + \frac { \sqrt { ( k p v - 1 ) k p ^ { 2 } v ^ { 2 } c _ { m } } } { k p ^ { 2 } v ^ { 2 } } .$

From the firm’s perspective, the actual security quality is

$$
\left(1 + \Delta\right) q _ {m} ^ {*} = \frac {k p ^ {2} v ^ {2} (1 + \Delta) ^ {2} + (- 1 + k p v) c _ {m}}{2 k p v c _ {m}}.\tag{19}
$$

Compared with the optimal value of security quality $q _ { m } ^ { * }$ in section 4, $( 1 + \varDelta ) \widetilde { q } _ { m } ^ { * } - q _ { m } ^ { * } =$ $\frac { k p ^ { 2 } \nu ^ { 2 } \left( 2 \Delta + \Delta ^ { 2 } \right) } { 2 k p \nu c _ { m } } > 0$ . The firm achieves higher security quality with a positive externality. The of externality increases, the firm gains better quality.

Similarly, the trend is obtained when analyzing service fee, ${ \widetilde { F } } ^ { * }$ . When $0 < k p v < 1$ $\frac { \partial \tilde { F } ^ { * } } { \partial \varDelta } > 0$ , and ${ \widetilde { F } } ^ { * }$ increases with an increase in $\varDelta ;$ when $\begin{array} { r } { k p v > 1 , \frac { \partial \tilde { F } ^ { * } } { \partial \varDelta } < 0 } \end{array}$ , and ${ \widetilde { F } } ^ { * }$ decreases with an increase in $\Delta$

## Proposition 5:

(a) The security quality of the MSSP, $\tilde { q } _ { m } ^ { * }$ , declines as externality intensifies if $\varDelta < \varDelta _ { 0 }$ , where

$\Delta _ { 0 } { = } - 1 + \frac { \sqrt { ( k p \nu - 1 ) k p ^ { 2 } \nu ^ { 2 } c _ { m } } } { k p ^ { 2 } \nu ^ { 2 } } . \widetilde { q } _ { m } ^ { * }$ increases as externality intensifies otherwise.

(b) The firm’s actual security quality, $( 1 + \varDelta ) \tilde { q } _ { m } ^ { * }$ , increases as externality intensifies.

(c) Service fee, ${ \widetilde { F } } ^ { * }$ increases (decreases) as externality intensifies, provided that $0 < k p \nu < 1$ $( k p \nu > 1 )$

The firm can benefit from the ${ \bf M S S P } \mathrm { \ ' } _ { \mathrm { s } }$ knowledge accumulation from multiple clients, which promotes service quality. Firms that suffer a small estimated loss under no protection should pay more to the MSSP for improving the service level with the increase of externality. The extra payment can be considered as the payment for the ${ \bf M S S P } ^ { \prime } { \bf s }$ effort in knowledge accumulation. In addition, firms with large networks and systems may reduce the service fee to the MSSP with the increase of externality. Under certain circumstances, the MSSP is allowed

## 6.2 Impact of Competition on Outsourcing

We assume that two firms have the same characteristics and utilities when choosing the same strategy. Solutions to the optimal utilities of the three strategies are:

$$
\tilde {u} _ {i n - \square o u s e} ^ {*} = u _ {i n - \square o u s e} ^ {*} + A = \frac {p ^ {2} v ^ {2}}{2 c _ {f}} + (1 - p) v + A;\tag{20}
$$

$$
\tilde {u} _ {n o n - c o r e} ^ {*} = (1 - p) v _ {c} + \frac {p ^ {2} v _ {c} ^ {2}}{2 c _ {f}} + \frac {p ^ {2} (1 + \varDelta) ^ {2} v _ {n c} ^ {2}}{4 c _ {m}} + \frac {c _ {m} (- 1 + k p v _ {n c}) ^ {2}}{4 k ^ {2} p ^ {2} (1 + \varDelta) ^ {2} v _ {n c} ^ {2}} - \frac {p v _ {n c}}{2} + 1 - \frac {1}{2 k} - v _ {n c} l + A;\tag{21}
$$

$$
\tilde {u} _ {f u l l} ^ {*} = \frac {p ^ {2} (1 + \varDelta) ^ {2} v ^ {2}}{4 c _ {m}} + \frac {c _ {m} (- 1 + k p v) ^ {2}}{4 k ^ {2} p ^ {2} (1 + \varDelta) ^ {2} v ^ {2}} - \frac {p v}{2} + 1 - \frac {1}{2 k} - v _ {n c} l - v _ {c} d l + A.\tag{22}
$$

A firm decides by considering the competitor’s possible strategies. The payoff matrix for the game is displayed in Table 5. The first (second) element in the ordered pair within each cell is the expected payoff to firm A (firm B).

Table 5. Normal Form of the Game

<table><tr><td rowspan="2">Firm A&#x27;s strategy</td><td colspan="3">Firm B&#x27;s strategy</td></tr><tr><td>IN</td><td>ONC</td><td>OF</td></tr><tr><td>IN</td><td> $\begin{array}{cc}A & B \\ (u_{in-house}, u_{in-house})\end{array}$ </td><td> $\begin{array}{cc}A & B \\ t_{in-house}, u_{non-core}\end{array}$ </td><td> $\begin{array}{cc}A & B \\ (u_{in-house}, u_{full})\end{array}$ </td></tr><tr><td>ONC</td><td> $\begin{array}{cc}A & B \\ (u_{non-core}, u_{in-house})\end{array}$ </td><td> $\begin{array}{cc}A & B \\ (u_{non-core}, u_{non-core})\end{array}$ </td><td> $\begin{array}{cc}A & B \\ (u_{non-core}, u_{full})\end{array}$ </td></tr><tr><td>OF</td><td> $\begin{array}{cc}A & B \\ (u_{full}, u_{in-house})\end{array}$ </td><td> $\begin{array}{cc}A & B \\ (u_{full}, u_{non-core})\end{array}$ </td><td> $\begin{array}{cc}A & B \\ (u_{full}, u_{full})\end{array}$ </td></tr></table>

The same method is used to calculate the intersections of each of the two strategies as highlighted in the last section. The results are provided in Table A.2 in the appendix.

Competitors are the same in every aspect; hence, the results for firm A are the same.

Considering the competition environment when deciding how to protect information security, competitors may consider a series of possible strategies:

## Proposition 6:

(a) Both competitors adopt the in-house strategy when $l > l _ { 1 2 }$ under the prerequisite of $l _ { 2 4 } <$ $l _ { 1 4 } < l _ { 1 2 }$ , or $l > l _ { 1 } .$ under the prerequisite of $l _ { 1 2 } < l _ { 1 4 } < l _ { 2 4 }$

(b) Both competitors outsource non-core business when $l _ { 2 4 } ^ { ^ { \prime } } < l < l _ { 1 2 }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { \prime } < { l _ { 1 4 } } ^ { \prime } < { l _ { 1 2 } } ^ { \prime }$

(c) Both competitors adopt the full outsourcing strategy when $l < { l _ { 2 4 } } ^ { \prime \prime }$ under the prerequisite of ${ l _ { 2 4 } } ^ { \prime \prime } < { l _ { 1 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime }$ , or $l < { l _ { 1 4 } } ^ { \prime \prime }$ under the prerequisite of ${ l _ { 1 2 } } ^ { \prime \prime } < { l _ { 1 4 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime \prime }$ <sub>24</sub><sup>′′</sup>.

(d) One competitor adopts the in-house strategy and the other outsources non-core business when ${ l _ { 1 } } _ { 2 } ^ { \prime } < l < { l _ { 1 } } _ { 2 }$ under the prerequisite of ${ l _ { 2 4 } } ^ { \prime } < { l _ { 1 4 } } ^ { \prime } < { l _ { 1 2 } } ^ { \prime } < l _ { 1 2 }$

(e) One competitor adopts the in-house strategy and the other chooses full outsourcing when ${ l _ { 1 4 } } ^ { \prime \prime } < l < l _ { 1 4 }$ under the prerequisite of ${ l _ { 1 } } _ { 2 } < { l _ { 1 } } _ { 4 } ^ { \prime \prime } < l _ { 1 4 } < l _ { 2 4 }$

(f) One competitor outsources non-core business and the other chooses full outsourcing when ${ l _ { 2 4 } } ^ { \prime \prime } < l < { l _ { 2 4 } } ^ { \prime }$ under the prerequisite of ${ l _ { 2 4 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime } < { l _ { 1 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime }$

The proofs are in the appendix.

## 7. Discussion

Prior studies assume that the MSSP has cost and technical advantages and suggest that firms receive better protection when outsourcing information security to the MSSP than when utilizing in-house development [15,22,40]. To represent the cost advantage of outsourcing, we follow the assumption that the MSSP has a lower cost coefficient than the firm does. We describe the security level of protection as security quality, which has the same characteristics consistent with prior studies [15]. Security quality increases with the firm’s asset value, and the probability of being attacked, as well, decreases with the cost coefficient, regardless of either in-house development or outsourcing (Lemma 1 and Lemma 2). This supports that the MSSP’s cost advantages lead to better protection when the firm decides to outsource.

We also adopt a slightly different perspective from prior studies when examining the payment to the MSSP. We find that the payment initially increases rapidly and then gradually decreases with the increase in the estimated loss under no protection (Proposition 1). The rapid increase suggests that firms may pay more to ensure that they would not be ignored by the

MSSP because the MSSP may give priority to firms that have significant losses once being attacked. With the increase in the estimated loss, there will be an improvement in security quality, which suggests that the firm does not have to pay more to the MSSP.

Then, we discuss the optimal decision for the firm to choose. We find that outsourcing to the MSSP to seek high quality service does not cut cost incurred to the firm under certain conditions (Proposition 2). This does not contradict the assumption that the MSSP has cost advantages, because cost increases convexly in the firm's security quality. When the firm has a high cost coefficient, it will reduce security quality to realize low cost, which is even lower than the payment to MSSP. In addition, a firm’s viable strategies are Strategy IN and Strategy OF from the point of security quality. When there is a distinct cost advantage between the firm and the MSSP, the security quality of Strategy OF exceeds that of Strategy IN, and the firm would prefer full outsourcing. Partial outsourcing is not an option because of low quality (Proposition 3).

A firm’s comprehensive consideration on information security strategy should be based on utility. From the perspective of risk assessment, Strategy ONC can be added as an option in addition to Strategy IN and Strategy OF. Firms should choose the in-house strategy in the environment where there is a high risk of leakage that includes leaking information or allowing other clients to access a client’s sensitive data. On the contrary, the ideal situation for a firm to choose full outsourcing is where the MSSP strictly adheres to the confidentiality agreement and manages all security issues. In addition, outsourcing non-core business can be adopted when the risk is medium. However, firms do not benefit from outsourcing their core business to get better protection from the MSSP (Proposition 4).

In addition to evaluating the MSSP, the loss of core information being leaked should also be estimated. Under the condition that core business occupies a large proportion of firm value, Strategy IN is the optimal choice, and Strategy ONC will not be adopted, even if the risk of leakage is assessed as medium because partial protection has the least security and results in lower utility than keeping all business protected in-house. Next, we add the risk of hacker attacks to the firm’s overall security risk. If the risk of hacker attacks is low, there seems no need to outsource to an MSSP, and in-house development can realize the optimal utility as well as eliminate the risk of information leakage. When the risk of attacks is high enough so that the firm has to adopt external security expertise, choosing from the three strategies can be determined by the degree of information leakage risk.

The role of information leakage in a firm’s decision-making is more evident when extending the study to the competitive environment. The MSSP that serves multiple client firms in the same industry contributes to improved security quality but has the risk of leaking a client’s data to other clients. Client firms tend to choose the same strategy when they cooperate with the same MSSP (Proposition 6). Extra benefits from externality are the same for the client firms, and the loss of leakage can be compensated by absorbing other client firms’ leaked information. It is feasible for firms to choose different strategies in a few cases. When one firm chooses the in-house strategy and the other adopts full outsourcing or partial outsourcing, the former firm benefits from the competitor’s leaked information, and the latter firm gains more utility benefit from the MSSP’s service. For similar reasons, one firm chooses partial outsourcing, and the other chooses full outsourcing in the case of a low risk of leakage. Though the former receives better security quality and suffers lower loss of leakage than the competitor does, the competitor enjoys cost advantage and a satisfying utility.

This study regards the effect of MSSPs’ knowledge accumulation as a type of externality [21,22]. In most cases, intensifying externality promotes MSSPs’ security quality and firms’ actual security quality. In certain special cases where an MSSP serves firms with high attack risks and externality is relatively low, intensifying externality increases the firms’ actual security quality and reduces the MSSP's security quality at the same time (Proposition 5). This indicates the situation of a low degree of knowledge sharing among client firms. Accumulated knowledge can strengthen MSSPs’ ability of monitoring network security situations. However, intensifying externality demands MSSPs provide higher security quality under other conditions (Proposition 5). This shows the effect of building interconnections among different client firms’ systems and networks, which makes information security more complex and forces MSSPs to make greater efforts to ensure secure information exchange and sharing [12].

## 8. Conclusions

## 8.1 Key Contributions

The study makes several contributions to the literature of information security strategies. First, we complement the prior literature that advocates the advantages of outsourcing to MSSPs. We find that there are certain conditions for client firms to receive these advantages. For example, we find that the service fee paid to MSSPs will first increase rapidly and then gradually decrease when the client firms’ estimated loss increases. In addition, client firms cannot always receive higher security quality and lower cost simultaneously in the case of outsourcing.

Second, we are one of the first to consider the nature of the business processes to be outsourced to MSSPs. We find that a partial outsourcing strategy that considers separate protections for core and non-core business always results in lower security quality than either in-house strategy or full outsourcing strategy will do. In addition, outsourcing non-core business can be feasible under certain conditions, but outsourcing core business is always an inferior strategy.

Third, being one of the first to consider the risk of information leakage during outsourcing, we show the conditions of when to choose each strategy. Firms can adopt the in-house strategy when facing a high risk of information leakage. MSSPs still have advantages when there is a low risk of information leakage. Outsourcing non-core business shows its effect on mitigating part of the loss of leakage and can be an alternative in medium-risk situations. In the competitive environment, we show that firms are highly likely to choose the same strategy as their competitors and consider information leakage in the decision. In addition, competitors adopt different strategies in a few cases. For firms that outsource to MSSPs, the loss from information leakage could be compensated by the cost saving of outsourcing. Meanwhile, competitors adopting high-cost in-house protection benefit from absorbing their leaked data. Therefore, competitors’ decisions slightly change the impact of information leakage risk on the firm.

## 8.2 Implications

We suggest that full outsourcing is not the best choice. Although MSSPs may provide better security quality than in-house protection, outsourcing to an MSSP may not always save cost. To save cost, the firm prefers to invest less in in-house security protection regardless of security quality. It’s essential to consider the risk of information leakage when considering outsourcing to MSSPs where there is a variation of outsourcing strategies in terms of information leakage risk. Full outsourcing is the optimal choice only when firms face a low risk of information leakage. In a medium-risk environment, outsourcing only non-core business will cut security cost and protect core business. Firms may not benefit from outsourcing their core business. Partial outsourcing leads to low quality of protection, and there are serious consequences for core information leakage.

Firms should first assess possible losses before outsourcing to MSSPs, which include the loss of attack and the loss of leakage. By estimating the effect of security measures, firms can assess residual risks once information security incidents occur. They need to calculate the loss of leakage by evaluating candidate MSSPs’ reputation, financial situation, and the capability of internal and external security management. Weighing the pros and cons, firms may ultimately give up using MSSPs because of the potential risk of confidentiality loss. This is especially trying for banks and financial institutions that may not outsource but develop their own security teams and directly invest in their own security protections. Moreover, although partial outsourcing is an alternative to reduce leakage loss, lower security protection in partial outsourcing is the distinct drawback.

From the ${ \bf { M S S P } } ^ { \prime } { \bf { s } }$ perspective, a reliable MSSP is attractive for client firms especially when the MSSP is focused on a certain industry. The MSSP shall realize that competitive client firms tend to choose the same strategy. However, the growth of the client firms’ networks raises requirements for the MSSP to improve internal management to maintain a secure environment.

## 8.3 Limitation and Future Research

In this study, we only discuss the outsourcing decision making of a risk-neutral firm. Based on the characteristics of security quality, we infer that risk-averse firms may not approach a partial outsourcing strategy. The limitation makes it a valuable extension to explore how risk aversion affects a firm’s decision or the optimum contract terms. In addition, we divide a firm's business into two separate parts in the framework of our model, core and non-core, and assume the two types of business are independent. It is possible to extend this assumption to take into account the connection between core and non-core business. Future research can analyze the interdependent risk between the two types of business and search for a better contract structure when selecting the partial outsourcing strategy.

## Appendix

## Proof of Lemma 1:

For in-house strategy, the first-order derivative for optimality utility is

$$
\frac {\partial u _ {i n - \square o u s e}}{\partial q _ {f}} = p v - c _ {f} q _ {f} = 0.\tag{A.1}
$$

We get

$$
q _ {f} ^ {*} = \frac {p v}{c _ {f}}.\tag{A.2}
$$

Therefore, $q _ { f } ^ { * }$ is proportional to ?? and inversely proportional to $c _ { f }$ .

## Proof of Lemma 2:

To maximizing ??, we calculate the following equation:

$$
\frac {\partial \pi_ {f u l l}}{\partial q _ {m}} = p v \beta - c _ {m} q _ {m} = 0.\tag{A.3}
$$

We get the MSSP's optimum quality:

$$
q _ {m} ^ {*} = \frac {p v \beta}{c _ {m}}.\tag{A.4}
$$

Then, we determine the contract term $[ F , \beta ]$ . Through Assumption 3, we transform $u _ { f u l l }$ to a function of ??.

$$
u _ {f u l l} = - F + v - p v + F k p v + \frac {F k (1 - F k) p ^ {2} v ^ {2}}{c _ {m}} - v _ {c} d l - v _ {n c} l.\tag{A.5}
$$

We get the optimal payment by calculating:

$$
\frac {\partial u _ {f u l l}}{\partial F} = - 1 + k p v + \frac {k (1 - 2 F k) p ^ {2} v ^ {2}}{c _ {m}} = 0.\tag{A.6}
$$

We get the optimum fee:

$$
F ^ {*} = \frac {k p ^ {2} v ^ {2} - c _ {m} + k p v c _ {m}}{2 k ^ {2} p ^ {2} v ^ {2}}.\tag{A.7}
$$

According to Assumption 3, we get the optimum compensation:

$$
\beta^ {*} = \frac {1}{2} \bigg (1 + \frac {- c _ {m} + k p v c _ {m}}{k p ^ {2} v ^ {2}} \bigg).\tag{A.8}
$$

Substituting $F ^ { * }$ , we obtain the MSSP's optimum quality:

$$
q _ {m} ^ {*} = \frac {1}{2} \Big (1 - \frac {1}{k p v} + \frac {p v}{c _ {m}} \Big),\tag{A.9}
$$

and the firm’s best utility when outsourcing its information security is:

$$
u _ {f u l l} ^ {*} = \frac {1}{4} \Bigl (- \frac {2}{k} + 4 v - 2 p v + \frac {p ^ {2} v ^ {2}}{c _ {m}} + \frac {(1 - k p v) ^ {2} c _ {m}}{k ^ {2} p ^ {2} v ^ {2}} - 4 v _ {c} d l - 4 v _ {n c} l \Bigr).\tag{A.10}
$$

In order to characterize $q _ { m } ^ { * }$ , the first-order derivative is:

$$
\frac {\partial q _ {m}}{\partial v} = \frac {1}{2} \left(\frac {1}{k p v ^ {2}} + \frac {p}{c _ {m}}\right) > 0\tag{A.11}
$$

$$
\frac {\partial q _ {m}}{\partial c _ {m}} = - \frac {p v}{2 c _ {m} ^ {2}} <   0\tag{A.12}
$$

In conclusion, $q _ { m } ^ { * }$ has a positive correlation with ?? and a negative correlation with $c _ { m } .$ Proof of Proposition 1:

To characterize $F ^ { * }$ , we calculate the first-order derivative of $F ^ { * }$ with ????:

$$
\frac {\partial F ^ {*}}{\partial p v} = - \frac {(2 - k p v) c _ {m}}{2 k ^ {2} p ^ {3} v ^ {3}} <   0\tag{A.13}
$$

When $\begin{array} { r } { 2 - k p v < 0 , \frac { \partial F ^ { * } } { \partial p v } < 0 , F ^ { * } } \end{array}$ $2 - k p v > 0$ $\frac { \partial \boldsymbol { F } ^ { * } } { \partial p { \boldsymbol { v } } } > \boldsymbol { 0 } , \ \boldsymbol { F } ^ { * }$ increases with ???? going up.

![](/api/attachments/54PX6ZEA/fulltext/images/8cc5c80ed6b4482ede3dcc571f249974f87a14af4a23750c6a427cd8de95f2fb.jpg)

Figure A.1. Trend of variation $F ^ { * }$

In Figure A.1, we show the coordinates of the three key points. To compare the slopes of the lines from the extreme point to the two critical points, we first calculate ?????? ?? and ?????? $\beta \mathbf { : }$ :

$$
\tan \alpha = \frac {\frac {1}{8} \left(c _ {m} + \frac {4}{k}\right)}{\frac {c _ {m}}{2} + \frac {2}{k} - \frac {1}{2} \sqrt {\frac {4 c _ {m} + c _ {m} ^ {2} k}{k}}} = \frac {4 + c _ {m} k}{1 6 + 4 c _ {m} k - 4 \sqrt {c _ {m} k (4 + c _ {m} k)}},\tag{A.14}
$$

$$
\tan \beta = \frac {\frac {1}{8 k} \left[ 4 + 5 c _ {m} k - 4 \sqrt {c _ {m} k (4 + c _ {m} k)} \right]}{\frac {c _ {m}}{2} - \frac {2}{k} + \frac {1}{2} \sqrt {\frac {4 c _ {m} + c _ {m} ^ {2} k}{k}}} = \frac {2 k \left[ \frac {1}{8} \left(c _ {m} + \frac {4}{k}\right) \right] - \frac {2 c _ {m}}{c _ {m} k + \sqrt {c _ {m} k (4 + c _ {m} k)}}}{- 4 + c _ {m} k + \sqrt {c _ {m} k (4 + c _ {m} k)}}.\tag{A.15}
$$

Then, we compare them by calculating the ratio of ?????? ?? to ?????? $\beta$ :

$$
\frac {\tan \alpha}{\tan \beta} = \frac {(4 + c _ {m} k) [ - 4 + c _ {m} k + \sqrt {c _ {m} k (4 + c _ {m} k)} ] [ c _ {m} k + \sqrt {c _ {m} k (4 + c _ {m} k)} ]}{- 4 (- 4 + 3 c _ {m} k) [ - 2 c _ {m} k + \sqrt {c _ {m} k (4 + c _ {m} k)} ]}.\tag{A.16}
$$

Due to $c _ { m } k \leq \sqrt { c _ { m } k ( 4 + c _ { m } k ) } \leq c _ { m } k + 2$ , we obtain:

$$
\frac {(4 + c _ {m} k) (- 2 + c _ {m} k)}{(c _ {m} k - 1 2)} \leq \frac {\tan \alpha}{\tan \beta} \leq \frac {(4 + c _ {m} k) (- 1 + c _ {m} k) (1 + c _ {m} k)}{(c _ {m} k - 1) ^ {2}}.\tag{A.17}
$$

Then, ?????? $\alpha > t a n \beta \mathrm { a n d } \frac { t a n \alpha } { t a n \beta }$ are of the same order of magnitude as $c _ { m } k$ $\mathrm { w h e n } c _ { m } k$ is high enough, we get ?????? $\alpha \gg t a n \beta$ and $\left| { \frac { c _ { m } } { 2 } } + { \frac { 1 } { 2 } } \sqrt { \frac { 4 c _ { m } + k c _ { m } ^ { 2 } } { k } } - { \frac { 2 } { k } } \right| \gg \left| { \frac { 2 } { k } } + { \frac { c _ { m } } { 2 } } - { \frac { 1 } { 2 } } \sqrt { \frac { 4 c _ { m } + k c _ { m } ^ { 2 } } { k } } \right|$

We conclude that, when $\begin{array} { r } { \frac { c _ { m } } { 2 } + \frac { 1 } { 2 } \sqrt { \frac { 4 c _ { m } + k c _ { m } ^ { 2 } } { k } } < p v < \frac { 2 } { k } , F ^ { * } } \end{array}$ first increases rapidly then decreases slowly with the increase of ????. According to Assumption 3, $\beta ^ { * }$ has the same trend as $F ^ { * }$

## Proof of Proposition 2:

Based on (A.2) and (A.9), we compare the optimal security quality of Strategy IN and $\begin{array} { r } { c _ { f } > \frac { 2 c _ { m } k p v ^ { 2 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } } , } \end{array}$ , outsourcing gets higher security quality, i.e., $q _ { m } ^ { * } > q _ { f } ^ { * }$ . Otherwise, outsourcing gets lower security quality.

The cost for in-house protection is ${ \textstyle \frac { 1 } { 2 } } c _ { f } q _ { f } ^ { 2 }$ . Based on (A.2), we calculate

$$
\frac {1}{2} c _ {f} q _ {f} ^ {* 2} = \frac {p v ^ {2}}{c _ {f}}.\tag{A.18}
$$

The cost for outsourcing is service fee, $F ,$ which has the optimal value calculated in (A.7). Then, we compare (A.18) with (A.7). We find that when $c _ { f } < \frac { k p v ^ { 4 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } } ;$ , outsourcing is cheaper than in-house security protection. Otherwise, outsourcing is more expensive.

To seek the condition that outsourcing can both cut cost and promote security quality, we get the intersection of the two intervals above. We find that only when $c _ { m } < { \frac { p v ^ { 2 } } { 2 } }$ , there is an intersection between $c _ { f } > \frac { 2 c _ { m } k p v ^ { 2 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } }$ and $c _ { f } < \frac { k p v ^ { 4 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } }$ . Therefore, under the condition of $c _ { m } < \frac { p \nu ^ { 2 } } { 2 }$ and $\frac { 2 c _ { m } k p v ^ { 2 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } } < c _ { f } < \frac { k p v ^ { 4 } } { - c _ { m } + c _ { m } k p v + k p v ^ { 2 } }$ , outsourcing has both cost and technical advantages.

As shown in Figure A.2, we illustrate the above analysis with numerical examples. The parameters are: $k = 0 . 2 , c _ { m } = 4 0 , p = 0 . 2 , v = 7 4$

![](/api/attachments/54PX6ZEA/fulltext/images/961b1893d76d06f7bd90470b47fa223631f660e2c5bf0c2fc6906f86de24195f.jpg)

Figure A.2 (a). Security Quality of Strategy IN and Strategy OF  
![](/api/attachments/54PX6ZEA/fulltext/images/17bfa84d742de716e8839321e51f6402c67e381ed7253690ab146c94c77eea0f.jpg)  
Figure A.2 (b). Cost of Strategy IN and Strategy OF

## Proof of Proposition 4:

We calculate the intersection of each strategy, and the results are in Table A.1. Table A.1. Critical Conditions for Different Strategies

<table><tr><td>Strategies</td><td>Critical Condition</td></tr><tr><td>{IN, ONC}</td><td> $l_{12} = \frac{1 + kpv(-1 + \alpha)}{2kv(-1 + \alpha)} - \frac{p^2v(1 + \alpha)}{2c_f} - \frac{p^2v(-1 + \alpha)}{4c_m}$ </td></tr><tr><td>{IN, OC}</td><td> $l_{13} = \frac{-1 + kpv\alpha}{2dkv\alpha} + \frac{p^2v(-2 + \alpha)}{2dc_f} + \frac{p^2v\alpha}{4dc_m} + \frac{(-1 + kpv\alpha)^2c_m}{4dk^2p^2v^3\alpha^3}$ </td></tr><tr><td>{IN, OF}</td><td> $l_{14} = \frac{-1 + kpv}{2kv(1 - \alpha + d\alpha)} - \frac{p^2v}{2(1 - \alpha + d\alpha)c_f} + \frac{p^2v}{4(1 - \alpha + d\alpha)c_m}$ </td></tr></table>

{ONC, OF}

$$
\begin{array}{c} \hline l _ {2 4} = \frac {p}{2 d} - \frac {p ^ {2} v \alpha}{2 d c _ {f}} - \frac {p ^ {2} v (- 2 + \alpha)}{4 d c _ {m}} + \frac {[ - 2 - 2 k p v (- 1 + \alpha) + \alpha ] c _ {m}}{4 d k ^ {2} p ^ {2} v ^ {3} (1 - \alpha) ^ {2}} \\ l _ {3 4} = \frac {p}{2} + \frac {p ^ {2} v (- 1 + \alpha)}{2 c _ {f}} + \frac {p ^ {2} v (1 + \alpha)}{4 c _ {m}} + \frac {(- 1 - \alpha + 2 k p v \alpha) c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} \alpha^ {2}} \end{array}\tag{{OC, OF}}
$$

We compare different intersections and discover that the relationships between $l _ { 1 3 }$ and $l _ { 1 4 } , \ l _ { 3 4 }$ and $l _ { 1 4 }$ are maintained even though the values of variables change. The proofs are as follows.

$$
\begin{array}{r l} & {l _ {1 4} - l _ {1 3} = \left[ \frac {- 1 + k p v}{2 k v (1 - \alpha + d \alpha)} - \frac {- 1 + k p v \alpha}{2 d k v \alpha} \right] + \left[ - \frac {p ^ {2} v}{2 (1 - \alpha + d \alpha) c _ {f}} - \frac {p ^ {2} v (- 2 + \alpha)}{2 d c _ {f}} \right]} \\ & {\quad + \left[ \frac {p ^ {2} v}{4 (1 - \alpha + d \alpha) c _ {m}} - \frac {p ^ {2} v \alpha}{4 d c _ {m}} \right] + \left[ \frac {(- 1 + k p v) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} (1 - \alpha + d \alpha)} - \frac {(- 1 + k p v \alpha) ^ {2} c _ {m}}{4 d k ^ {2} p ^ {2} v ^ {3} \alpha^ {3}} \right]} \\ & {\qquad = - \frac {(- 1 + \alpha) [ 1 + (- 1 + d) k p v \alpha ]}{2 d k v \alpha [ 1 + (- 1 + d) \alpha ]} - \frac {p ^ {2} v [ 2 + d (- 1 + \alpha) - \alpha ] (- 1 + \alpha)}{2 d [ 1 + (- 1 + d) \alpha ] c _ {f}} - \frac {p ^ {2} v (- 1 + \alpha) (d - \alpha + d \alpha)}{4 d [ 1 + (- 1 + d) \alpha ] c _ {m}} +} \\ & {\frac {(- 1 + k p v) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} \alpha^ {3} [ d + (- 1 + d) d \alpha ]}.} \end{array}
$$

As the value of each term is less than 0, we get $l _ { 1 4 } - l _ { 1 3 } > 0$ , which means if $l > l _ { 1 4 }$ then $l > l _ { 1 3 }$ . So, when Strategy IN is superior to Strategy $\mathrm { O F } ( \mathrm { i . e . , ~ } l > l _ { 1 4 } )$ , Strategy OC must be worse than Strategy IN (i.e., $l > l _ { 1 3 } )$ .

$$
\begin{array}{r l} & {l _ {3 4} - l _ {1 4} = \left[ \frac {p}{2} - \frac {- 1 + k p v}{2 k v (1 - \alpha + d \alpha)} \right] + \left[ \frac {p ^ {2} v (- 1 + \alpha)}{2 c _ {f}} + \frac {p ^ {2} v}{2 (1 - \alpha + d \alpha) c _ {f}} \right]} \\ & {\quad + \left[ \frac {p ^ {2} v (1 + \alpha)}{4 c _ {m}} - \frac {p ^ {2} v}{4 (1 - \alpha + d \alpha) c _ {m}} \right] + \left[ \frac {(- 1 - \alpha + 2 k p v \alpha) c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} \alpha^ {2}} - \frac {(- 1 + k p v) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} (1 - \alpha + d \alpha)} \right]} \\ & {\quad = \frac {1 + (- 1 + d) k p v \alpha}{2 k v [ 1 + (- 1 + d) \alpha ]} + \frac {p ^ {2} v \alpha [ 2 + d (- 1 + \alpha) - \alpha ]}{2 [ 1 + (- 1 + d) \alpha ] c _ {f}} + \frac {p ^ {2} v \alpha (d - \alpha + d \alpha)}{4 [ 1 + (- 1 + d) \alpha ] c _ {m}} - \frac {\left[ d \alpha (1 + \alpha - 2 k p v \alpha) + (- 1 + k p v \alpha) ^ {2} \right] c _ {m}}{4 k ^ {2} p ^ {2} v ^ {3} \alpha^ {2} [ 1 + (- 1 + d) \alpha ]}.} \end{array}
$$

In the same $l _ { 3 4 } - l _ { 1 4 } > 0$ . In other words, when Strategy IN is inferior to Strategy $\mathrm { O F } ( \mathrm { i . e . , } l < l _ { 1 4 } )$ OC is also worse than Strategy OF (i.e., $l < l _ { 3 4 } )$

Therefore, no matter which one of Strategy IN and Strategy OF is better, Strategy OC is always inferior.

## Proof of Proposition 5:

We solve the game in the competitive environment using backward induction.

For Strategy OF, to maximizing ??̃, we calculate the following equation:

$$
\frac {\partial \tilde {\pi} _ {f u l l}}{\partial \tilde {q} _ {m}} = p v \tilde {\beta} (1 + \varDelta) - c _ {m} \tilde {q} _ {m} = 0.\tag{A.19}
$$

We get the MSSP's optimum quality:

$$
\tilde {q} _ {m} ^ {*} = \frac {p v \widetilde {\beta} (1 + \varDelta)}{c _ {m}}.\tag{A.20}
$$

Then, we determine the contract term $\left[ { \widetilde { F } } , { \widetilde { \beta } } \right]$ . Through Assumption 3, we transform $u _ { f u l l }$ to a function of $\tilde { F }$ .

$$
\tilde {u} _ {f u l l} = - \tilde {F} + v - p v + \tilde {F} k p v + \frac {\tilde {F} k (1 - \tilde {F} k) p ^ {2} v ^ {2} (1 + \Delta)}{c _ {m}} - v _ {c} d l - v _ {n c} l + A. (A. 2 1)
$$

We get the optimal payment by calculating:

$$
\frac {\partial \widetilde {u} _ {f u l l}}{\partial \tilde {F}} = - 1 + k p v + \frac {k (1 - 2 \tilde {F} k) p ^ {2} v ^ {2} (1 + \varDelta)}{c _ {m}} = 0.\tag{A.22}
$$

We get the optimum fee:

$$
\tilde {F} ^ {*} = \frac {k p ^ {2} v ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v c _ {m}}{2 k ^ {2} p ^ {2} v ^ {2} (1 + \Delta) ^ {2}}.\tag{A.23}
$$

According to Assumption 3, we get the optimum compensation:

$$
\tilde {\beta} ^ {*} = \frac {1}{2} \bigg (1 + \frac {- c _ {m} + k p v c _ {m}}{k p ^ {2} v ^ {2} (1 + \Delta) ^ {2}} \bigg).\tag{A.24}
$$

Substituting $\tilde { \beta } ^ { * }$ in (A.20) and substituting ${ \widetilde { F } } ^ { * }$ in (A.21), we obtain the MSSP's optimum quality:

$$
\tilde {q} _ {m} ^ {*} = \frac {k p ^ {2} v ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v c _ {m}}{2 k p v (1 + \Delta) c _ {m}},\tag{A.25}
$$

and the firm’s best utility when outsourcing its information security is:

$$
\tilde {u} _ {f u l l} ^ {*} = \frac {p ^ {2} v ^ {2} (1 + \Delta) ^ {2}}{4 c _ {m}} + \frac {(1 - k p v) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v ^ {2} (1 + \Delta) ^ {2}} - \frac {p v}{2} + 1 - \frac {1}{2 k} - v _ {c} d l - v _ {n c} l + A.\tag{A.26}
$$

In order to characterize $\tilde { q } _ { m } ^ { * }$ , the first-order derivative is calculated as:

$$
\frac {\partial \tilde {q} _ {m} ^ {*}}{\partial \varDelta} = \frac {1}{2} \Big (\frac {1 - k p v}{k p v (1 + \varDelta) ^ {2}} + \frac {p v}{c _ {m}} \Big).\tag{A.27}
$$

When $\begin{array} { r } { 1 - k p v > 0 , \frac { \partial \tilde { q } _ { m } ^ { * } } { \partial { \varDelta } } > 0 } \end{array}$ where $\tilde { q } _ { m } ^ { * }$ increases with ?? going up. When $1 -$ $k p v < 0$ , cases divide into $\begin{array} { r } { \frac { \partial \tilde { q } _ { m } ^ { * } } { \partial \varDelta } < 0 } \end{array}$ if $\begin{array} { r } { \Delta _ { 0 } < - 1 + \frac { \sqrt { ( k p v - 1 ) k p ^ { 2 } v ^ { 2 } c _ { m } } } { k p ^ { 2 } v ^ { 2 } } } \end{array}$ ; and $\frac { \partial \tilde { q } _ { m } ^ { * } } { \partial \varDelta } > 0$ if $\Delta _ { 0 } > - 1 + \frac { \sqrt { ( k p v - 1 ) k p ^ { 2 } v ^ { 2 } c _ { m } } } { k p ^ { 2 } v ^ { 2 } } .$

From the firm’s point of view, the actual security quality is

$$
(1 + \varDelta) \tilde {q} _ {m} ^ {*} = \frac {k p ^ {2} v ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v c _ {m}}{2 k p v c _ {m}}.\tag{A.28}
$$

Comparing with the optimal security quality, $q _ { m } ^ { * } ,$ in section 4, we get $( 1 + \Delta ) \tilde { q } _ { m } ^ { * } - q _ { m } ^ { * } =$ $\frac { k p ^ { 2 } v ^ { 2 } \left( 2 \varDelta + \varDelta ^ { 2 } \right) } { 2 k p v c _ { m } } > 0$ . In addition, $\begin{array} { r } { \frac { \partial ( 1 + \varDelta ) \tilde { q } _ { m } ^ { * } } { \partial \varDelta } = \frac { k p ^ { 2 } v ^ { 2 } \left( 1 + \varDelta \right) } { k p v c _ { m } } > 0 } \end{array}$ , which indicates that the actual security quality that the firm obtains goes up if ?? increases.

In order to characterize ${ \widetilde { F } } ^ { * }$ , the first-order derivative calculation is

$$
\frac {\partial \tilde {F}}{\partial \Delta} = \frac {(1 - k p v) c _ {m}}{k ^ {2} p ^ {2} v ^ {2} (1 + \Delta) ^ {3}}.\tag{A.29}
$$

When $\begin{array} { r } { 1 - k p v < 0 , \frac { \partial \tilde { F } ^ { * } } { \partial \varDelta } < 0 , \tilde { F } ^ { * } } \end{array}$ decreases with ?? going up; when $1 - k p v > 0$ $\frac { \partial \tilde { F } ^ { * } } { \partial { \varDelta } } > 0 , \ \tilde { F } ^ { * }$ increases with ?? going up.

Using the same method, we get the solutions to strategy ONC as follows:

$$
F ^ {n c ^ {*}} = \frac {k p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v _ {n c} c _ {m}}{2 k ^ {2} p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2}}.\tag{A.30}
$$

$$
\tilde {\beta} ^ {n c ^ {*}} = \frac {k p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v _ {n c} c _ {m}}{2 k p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2}}.\tag{A.31}
$$

$$
\tilde {q} _ {m} ^ {n c ^ {*}} = \frac {k p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2} - c _ {m} + k p v c _ {m}}{2 k p v _ {n c} (1 + \Delta) c _ {m}},\tag{A.32}
$$

$$
\tilde {u} _ {n o n - c o r e} ^ {*} = \frac {p ^ {2} v _ {c} ^ {2}}{2 c _ {f}} + (1 - p) v _ {c} + \frac {p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2}}{4 c _ {m}} + \frac {(1 - k p v _ {n c}) ^ {2} c _ {m}}{4 k ^ {2} p ^ {2} v _ {n c} ^ {2} (1 + \Delta) ^ {2}} - \frac {p v _ {n c}}{2} + 1 - \frac {1}{2 k} - v _ {c} d l -
$$

$$
v _ {n c} l + A.\tag{A.33}
$$

The characteristics of the variables are the same as the results in Strategy OF.

## Proof of Proposition 6:

We calculate the intersections of two strategies, as shown in Table A.2. A’s strategy and B’s strategy) are used to simplify the status where firm A chooses A’s strategy and firm B chooses B’s strategy. For example, (IN, ONC) means firm A chooses Strategy IN, and firm B chooses Strategy ONC.

Table A.2. Intersections of Possible Strategies (Firm B)

<table><tr><td>Strategies</td><td>Intersection</td></tr><tr><td>{(IN, IN),(IN, ONC)}</td><td> $l_{12} = \frac{1 + kpv(-1 + \alpha)}{2kv(-1 + \alpha)} - \frac{p^2v(1 + \alpha)}{2c_f} - \frac{p^2v(-1 + \alpha)}{4c_m}$  $-\frac{[1 + kpv(-1 + \alpha)]^2c_m}{4k^2p^2v^3(-1 + \alpha)^3}$ </td></tr><tr><td>{(IN, IN),(IN, OF)}</td><td> $l_{14} = \frac{-1 + kpv}{2kv(1 - \alpha + d\alpha)} - \frac{p^2v}{2(1 - \alpha + d\alpha)c_f}$  $+\frac{p^2v}{4(1 - \alpha + d\alpha)c_m} + \frac{(-1 + kpv)^2c_m}{4k^2p^2v^3(1 - \alpha + d\alpha)}$ </td></tr><tr><td>{(IN, ONC),(IN, OF)}</td><td> $l_{24} = \frac{p}{2d} - \frac{p^2v\alpha}{2dc_f} - \frac{p^2v(-2 + \alpha)}{4dc_m}$  $+\frac{[-2 - 2kpv(-1 + \alpha) + \alpha]c_m}{4dk^2p^2v^3(1 - \alpha)^2}$ </td></tr></table>

$$
l _ {1 2} ^ {\prime}
$$

$$
\begin{array}{r l} \frac {\{\mathrm{(ONC,IN)} , \mathrm{(ONC,ONC)} \}}{2 k + 2 k p (- 1 + \alpha) - \frac {2 p ^ {2} v ^ {2} (- 1 + \alpha^ {2})}{c _ {f}} - \frac {p ^ {2} v ^ {2} (- 1 + \alpha) ^ {2} [ 1 + e (1 - \alpha) ]}{c _ {m}}} & = \frac {4 v (- 1 + \alpha) [ 1 + \eta (- 1 + \theta) ]}{4 v (- 1 + \alpha) [ 1 + \eta (- 1 + \theta) ]}. \end{array}
$$

$$
l _ {1 4} ^ {\prime}\tag{\( \{(ONC, IN), \}
$$

(ONC, OF)}

$$
= \frac {- 2 p ^ {4} v ^ {4} (k + e k \alpha) ^ {2} c _ {m} + c _ {f} [ k p ^ {2} v ^ {2} (1 + e \alpha) ^ {2} + (- 1 + k p v) c _ {m} ] ^ {2}}{4 k ^ {2} p ^ {2} v ^ {3} [ 1 + e (1 - \alpha) ] ^ {2} [ 1 + \eta (- 1 + \theta) + \alpha (- 1 + d + \eta - \eta \theta) ] c _ {f} (1 + e (1 - \alpha))},\tag{{ONC ONC),}
$$

$$
\begin{array}{r} l _ {2 4} ^ {\prime} = \frac {p}{2 d} - \frac {p ^ {2} v \alpha}{2 d c _ {f}} - \frac {p ^ {2} v (- 2 + \alpha) [ 1 + e (1 - \alpha) ] ^ {2}}{4 d c _ {m}} \\ + \frac {[ - 2 - 2 k p v (- 1 + \alpha) + \alpha ] c _ {m}}{4 d k ^ {2} p ^ {2} v ^ {3} (1 - \alpha) ^ {2} [ 1 + e (1 - \alpha) ] ^ {2}} \end{array}\tag{ONC, OF)}}
$$

$$
l _ {1 2} ^ {\prime \prime}
$$

$$
\begin{array}{r l} \left\{\mathrm{(OF,IN),} \right. & = - \frac {2}{k} - 2 p v (- 1 + \alpha) + \frac {2 p ^ {2} v ^ {2} (- 1 + \alpha^ {2})}{c _ {f}} + \frac {(1 + e) ^ {2} p ^ {2} v ^ {2} (- 1 + \alpha) ^ {2}}{c _ {m}} \\ (\mathrm{OF,ONC}) \} & = \frac {4 v [ 1 - \alpha + \alpha \eta (1 - d) (- 1 + \theta) + \eta (- 1 + \alpha) ]}{4 v [ 1 - \alpha + \alpha \eta (1 - d) (- 1 + \theta) + \eta (- 1 + \alpha) ]}. \end{array}
$$

$$
l _ {1 4} ^ {\prime \prime}
$$

{(OF, IN),

$$
= \frac {- 2 k ^ {2} p ^ {4} v ^ {4} (1 + e) ^ {2} c _ {m} + c _ {f} [ k p ^ {2} v ^ {2} (1 + e) ^ {2} + (- 1 + k p v) c _ {m} ] ^ {2}}{4 k ^ {2} p ^ {2} v ^ {3} (1 + e) ^ {2} [ 1 + \alpha (- 1 + d) ] [ 1 + \eta (- 1 + \theta) ] c _ {f} c _ {m}}\tag{\(\mathrm{(OF,~OF)}\}\}
$$

{OF ONC),

$$
l _ {2 4} ^ {”} = \frac {p}{2 d} - \frac {p ^ {2} v \alpha}{2 d c _ {f}} - \frac {p ^ {2} v (- 2 + \alpha) (1 + e) ^ {2}}{4 d c _ {m}}
$$

(OF, OF)}

$$
+ \frac {[ - 2 - 2 k p v (- 1 + \alpha) + \alpha ] c _ {m}}{4 d k ^ {2} p ^ {2} v ^ {3} (1 - \alpha) ^ {2} (1 + e) ^ {2}}
$$

I． When Firm A chooses in-house protection, there are three choices for Firm B. According to Table A.2,

i. Firm B chooses in-house

a) when $l > l _ { 1 4 }$ , under the prerequisite of $l _ { 1 2 } < l _ { 1 4 } < l _ { 2 4 }$

b) when $l > l _ { 1 2 }$ , under the prerequisite of $l _ { 2 4 } < l _ { 1 4 } < l _ { 1 2 }$

ii. Firm B chooses to outsource only non-core business

a) when $l _ { 2 4 } < l < l _ { 1 2 }$ , under the prerequisite of $l _ { 2 4 } < l _ { 1 4 } < l _ { 1 2 }$

iii. Firm B chooses full outsourcing

a) when $l < l _ { 1 4 }$ , under the prerequisite of $l _ { 1 2 } < l _ { 1 4 } < l _ { 2 4 }$

b) when $l < l _ { 2 4 }$ , under the prerequisite of $l _ { 2 4 } < l _ { 1 4 } < l _ { 1 2 }$

II． When Firm A chooses to outsource only non-core business, there are three choices for Firm B. According to Table A.2,

i. Firm B chooses in-house

a) when $l > { l _ { 1 4 } } ^ { ' }$ , under the prerequisite of ${ l _ { 1 2 } } ^ { ' } < { l _ { 1 4 } } ^ { ' } < l _ { 2 4 }$

b) when $l > { l _ { 1 2 } } ^ { \prime }$ , under the prerequisite of $l _ { 2 4 } ^ { ^ { \prime } } < l _ { 1 4 } ^ { ^ { \prime } } < l _ { 1 2 } ^ { ^ { \prime } }$

ii. Firm B chooses to outsource only non-core business

a) when ${ l _ { 2 4 } } ^ { \prime } < l < { l _ { 1 2 } } ^ { \prime }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { ' } < { l _ { 1 4 } } ^ { ' } < l _ { 1 2 }$

iii. Firm B choose full outsourcing

a) when $l < { l _ { 1 4 } } ^ { \prime }$ , under the prerequisite of $l _ { 1 2 } ^ { ^ { \prime } } < l _ { 1 4 } ^ { ^ { \prime } } < l _ { 2 4 } ^ { ^ { \prime } }$

b) when $l < { l _ { 2 4 } } ^ { \prime }$ , under the prerequisite of $l _ { 2 4 } ^ { ^ { \prime } } < l _ { 1 4 } ^ { ^ { \prime } } < l _ { 1 2 } ^ { ^ { \prime } }$

III． When Firm A chooses full outsourcing, there are three choices for Firm B.

i. Firm B chooses in-house

a) when $l > { l _ { 1 4 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 2 } } ^ { ^ { \prime \prime } } < { l _ { 1 4 } } ^ { ^ { \prime \prime } } < { l _ { 2 4 } } ^ { ^ { \prime \prime } }$

b) when $l > { l _ { 1 2 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 2 } } ^ { ^ { \prime \prime } }$

c) when ${ l _ { 1 4 } } ^ { \prime \prime } < l < { l _ { 1 2 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 4 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime } .$

ii. Firm B chooses to outsource only non-core business

a) when $l > l _ { 2 4 } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 2 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime \prime } < { l _ { 1 4 } } ^ { \prime \prime } ,$

b) when ${ l _ { 2 4 } } ^ { \prime \prime } < l < { l _ { 1 2 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { \prime \prime } < { l _ { 1 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime }$

c) when $l > { l _ { 1 2 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 4 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime }$

iii. Firm B chooses full outsourcing

a) when $l < l _ { 2 4 } ^ { \prime \prime }$ <sup>′</sup>, under the prerequisite of ${ l _ { 1 2 } } ^ { ^ { \prime \prime } } < { l _ { 2 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 4 } } ^ { ^ { \prime \prime } }$

b) when $l < { l _ { 1 4 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 2 } } ^ { ^ { \prime \prime } } < { l _ { 1 4 } } ^ { ^ { \prime \prime } } < { l _ { 2 4 } } ^ { ^ { \prime \prime } }$

c) when $l < l _ { 2 4 } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 2 } } ^ { ^ { \prime \prime } }$

d) when $l < { l _ { 1 4 } } ^ { \prime \prime }$ , under the prerequisite of ${ l _ { 1 4 } } ^ { ^ { \prime \prime } } < { l _ { 2 4 } } ^ { ^ { \prime \prime } } < { l _ { 1 2 } } ^ { ^ { \prime \prime } }$

Similarly, the possible situations for Firm A are the same as the situations we list above.

To sum up, considering the competition factor when making the decision of how to protect information security, here are a series of possible strategy pairs for competitors:

(a) Both competitors adopt the in-house strategy under the condition given in (I-i);

(b) Both competitors outsource non-core business under the condition given in (II-ii);

(c) Both competitors adopt the full outsourcing strategy under the condition given in (III-iii);

(d) One competitor adopts the in-house strategy and the other chooses to outsource non-core business when ${ l _ { 1 2 } } ^ { \prime } < l < { l _ { 1 2 } }$ , under the prerequisite of ${ l _ { 2 4 } } ^ { ' } < { l _ { 1 4 } } ^ { ' } < { l _ { 1 2 } } ^ { ' } < l _ { 1 2 }$ ;

(e) One competitor adopts the in-house strategy and the other chooses full outsourcing when ${ l _ { 1 4 } } ^ { \prime \prime } < l < { l _ { 1 4 } }$ , under the prerequisite of ${ l _ { 1 2 } } < { l _ { 1 4 } } ^ { \prime \prime } < l _ { 1 4 } < l _ { 2 4 }$ ;

(f) One competitor chooses to outsource non-core business and the other chooses full

outsourcing when ${ l _ { 2 4 } } ^ { \prime \prime } < l < { l _ { 2 4 } } ^ { \prime }$ under the prerequisite of ${ l _ { 2 4 } } ^ { \prime \prime } < { l _ { 2 4 } } ^ { \prime } < { l _ { 1 4 } } ^ { \prime \prime } < { l _ { 1 2 } } ^ { \prime \prime }$

## References

[1] Q.J. Yeh, J.T. Chang, Threats and countermeasures for information system security: A crossindustry study, Inform Manag, 44 (2007) 480-491.

[2] A. Cezar, H. Cavusoglu, S. Raghunathan, Outsourcing information security: Contracting issues and security implications, Manag Sci, 60 (2014) 638-657.

[3] Silversky, The business value of managed security Services, White Paper, SilverSky, 2015.

[4] SilverSky, What to look for in a managed security service provider, White Paper, SilverSky, 2014.

[5] G. Dhillon, R. Syed, F.D. Sá-Soares, Information security concerns in IT outsourcing: Identifying (in) congruence between clients and vendors, Inform Manag, 54 (2017) 452-464.

[6] CWE-200: Information Leak (Information Disclosure). From Common Weakness

[7] R.C. Jammalamadaka, R. Gamboni, S. Mehrotra, K. Seamons, N. Venkatasubramanian, A middleware approach for outsourcing data securely, Comput Secur, 32 (2013) 252-266.

[8] A. Hoecht, P. Trott, Outsourcing, information leakage and the risk of losing technologybased competencies, Eur Bus Rev, 18 (2006) 395-412.

[9] N. Feng, Z. Su, D. Li, C. Zheng, M. Li, Effects of review spam in a firm-initiated virtual brand community: Evidence from smartphone customers, Inform Manag, 55 (2018) 1061-1070.

[10] N. Ulltveit-Moe, A roadmap towards improving managed security services from a privacy perspective, Ethics Inform Tech, 16 (2014) 227-240.

[11] V. Cho, A. Chan, An integrative framework of comparing SaaS adoption for core and noncore business operations: An empirical study on Hong Kong industries, Inform Syst Front, 17 (2015) 1-16.

[12] A. Gupta, D. Zhdanov, Growth and sustainability of managed security services networks: An economic perspective, MIS Quarterly, 36 (2012) 1109-1130.

[13] X. Zhao, L. Xue, A.B. Whinston, Managing interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements, J Manag Inform Syst, 30 (2013) 123-152.

[14] N. Feng, M. Wang, M. Li, D. Li, Effect of security investment strategy on the business value of managed security service providers, Electron Commerce Res Appl, 35 (2019) DOI: 10.1016/j.elerap.2019.100843.

[15] K.-L. Hui, W. Hui, W.T. Yue, Information security outsourcing with system interdependency and mandatory security requirement, J Manag Inform Syst, 29 (2012) 117-156.

[16] D. Wen, W. Yurcik, Economics of internet security outsourcing: Simulation results based on the Schneier Model, in: Workshop on the Economics of Securing the Information Infrastructure (WESII), Washington DC, 2006, pp. 23--24.

[17] D. Wen, W. Yurcik, X. Yin, Outsourcing internet security: Economic analysis of incentives for managed security service providers, in: International Workshop on Internet and Network Economics, Springer, Berlin, Heidelberg, 2005, pp. 947-958.

[18] D. Wen, W. Yurcik, Outsourcing internet security: The effect of transaction costs on managed service providers, in: International Conference on Telecommunication Systems Modeling and Analysis, Dallas, TX, 2005.

[19] C.H. Lee, X. Geng, S. Raghunathan, Contracting information security in the presence of double moral hazard, Inform Syst Res, 24 (2013) 295-311.

[20] Y. Wu, R.Y.K. Fung, G. Feng, N. Wang, Decisions making in information security outsourcing: impact of complementary and substitutable firms, Comput Ind Eng, 110 (2017).

[21] A. Cezar, H. Cavusoglu, S. Raghunathan, Competition, speculative risks, and IT security outsourcing, In: Moore T., Pym D., Ioannidis C. (eds) Economics of Information Security and Privacy. Springer, Boston, MA. https://doi.org/10.1007/978-1-4419-6967-5\_15.

[22] A. Cezar, H. Cavusoglu, S. Raghunathan, Sourcing information security operations: The role of risk interdependency and competitive externality in outsourcing decisions, Prod Oper Manag, 26 (2017) 860-879.

[23] A.D. Nimubona, H. Benchekroun, Environmental R&D in the presence of an eco-industry, Environ Model Assess, 20 (2015) 491-507.

[24] M. García-Vega, E. Huergo, Determinants of international R&D outsourcing: The role of trade, Rev Dev Econ, 15 (2011) 93–107.

[25] K.H. Tan, W.P. Wong, L. Chung, Information and knowledge leakage in supply chain, Inform Syst Front, 18 (2016) 621-638.

[26] K.S. Anand, M. Goyal, Strategic information management under leakage in a supply chain, Manag Sci, 55 (2009) 438-452.

[27] N. Metoui, M. Bezzi and A. Armando, Risk-Based Privacy-Aware Access Control for Threat Detection Systems, In: Hameurlain A., Küng J., Wagner R., Dang T., Thoai N. (eds) Transactions on Large-Scale Data- and Knowledge-Centered Systems XXXVI. Lecture Notes in Computer Science, vol 10720, (2017).

[28] N. Ulltveit-Moe, V.A. Oleshchuk, A composite privacy leakage indicator, Wireless Pers

Commun, 61.3 (2011) https://doi.org/10.1007/s11277-011-0383-7.

[29] G. Smith, Quantifying information flow using min-entropy, in: Eighth International Conference on Quantitative Evaluation of Systems, 2011, pp. 159-167.

[30] G. Smith, On the foundations of quantitative information flow, in: International Conference on Foundations of Software Science and Computational Structures: 2009, pp. 288-302.

[31] A. Harel, A. Shabtai, L. Rokach, Y. Elovici, M-Score: A misuseability weight measure, IEEE Transactions on Dependable & Secure Computing, 9 (2012) 414-428.

[32] S. Vavilis, M. Petković, N. Zannone, Data leakage quantification, In: Atluri V., Pernul G. (eds) Data and Applications Security and Privacy XXVIII. Lecture Notes in Computer Science, vol 8566, (2014).

[33] O. Shy, R. Stenbacka, Partial outsourcing, monitoring cost, and market structure, Canadian

[34] J. Coolidge, D. Ilic, G. Kisunko, Small businesses in South Africa: Who outsources tax compliance work and why? The World Bank, (2009).

[35] M.C. Lacity, L.P. Willcocks, An empirical investigation of information technology sourcing practices: Lessons from experience, MIS Quarterly, 22 (1998) 363-408.

[36] L.M. Wang, L.W. Liu, Y.J. Wang, Capacity decisions and supply price games under flexibility of backward integration, Int J Prod Econ, 110 (2007) 85-96.

[37] L.H.R. Alvarez, R. Stenbacka, Partial outsourcing: A real options perspective, IntJ Ind Organ, 25 (2007) 91-102.

[38] E.K. Choi, To outsource or not to outsource in an integrated world, Int Rev Econ Finance, 16 (2007) 521-527.

[39] Y. Moon, Efforts and efficiency in partial outsourcing and investment timing strategy under market uncertainty, Comput Ind Eng, 59 (2010) 24-33.

[40] Y. Ji, S. Kumar, V. Mookerjee, When being hot is not cool: Monitoring hot lists for information security, Inform Syst Res, 27 (2016) 897-918.

[41] J. Chen, L. Xu, A.B. Whinston, Managing project failure risk through contingent contracts in procurement auctions, Decis Anal, 7 (2009) 23-39.

[42] J. Chen, Q. Zhu, Security as a service for cloud-enabled internet of controlled things under advanced persistent threats: A contract design approach, IEEE Transactions on Information Forensics & Security, 12 (2017) 2736-2750.

[43] IBM, IBM managed security services for security event and log management. http://www-935.ibm.com/services/us/igs/ pdf-iss-contracts/ireland-7808-00.pdf, 2015.

[44] N. Feng, H. J. Wang, M. Li, A Security Risk Analysis Model for Information Systems:

Causal Relationships of Risk Factors and Vulnerability Propagation Analysis, Information Sciences, 256 (2014) 57-73.

## Biography

NAN FENG is a professor of Information Management and Management Science at the College of Management and Economics, Tianjin University, China. He received his Ph.D. in Management Science from Tianjin University in 2007. His current research interests include economics of information systems, information security, and business analytics. He has published in MIS Quarterly, Information & Management, Electronic Commerce Research and Applications, Enterprise Information Systems, among others.

YUFAN CHEN is a master candidate at the College of Management and Economics, Tianjin University, China. Her research interest is information security economics.

HAIYANG FENG is an assistant professor of Information Management at the College of Management and Economics, Tianjin University, China. He received his Ph.D. in Management Science from Tianjin University. His current research interests include economics of information systems, platform strategy, and business analytics. His papers have been published in academic journals, including MIS Quarterly, International Journal of Production Economics, Computers & Industrial Engineering, Computers & Operations Research, and Soft Computing.

DAHUI LI is a professor of MIS at the University of Minnesota Duluth, communities, and technology innovation. His papers have been published in the Communications of the ACM, Decision Sciences, Decision Support Systems, Information & Management, Journal of the Association for Information Systems, Journal of Product Innovation Management, and elsewhere.

MINQIANG LI is currently a professor of Information Management at the College of Management and Economics, Tianjin University, China. His major research interests include management science and decision support, IT strategy, and electronic commerce. He has published papers in academic journals and conferences, such as the MIS Quarterly, European Journal of Operational Research, Journal of Evolutionary Economics, Information Sciences, IEEE Transactions on Neural Networks and Learning Systems, and elsewhere.
