---
otero_id: 1276
otero_key: "VK2E82CQ"
title: "Decision support for the optimal allocation of security controls"
authors: "He Zhang; Kaushal Chari; Manish Agrawal"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

## Decision support for the optimal allocation of security controls

He Zhang, Kaushal Chari, Manish Agrawal

![](/api/attachments/VK2E82CQ/fulltext/images/27201efcd2153cc7abe8e95636c9b2fa17566ff86162ca111d36d6a46ac72db1.jpg)

PII: S0167-9236(18)30158-1

DOI: doi:10.1016/j.dss.2018.10.001

Reference: DECSUP 12993

To appear in: Decision Support Systems

Received date: 10 May 2018

Revised date: 2 October 2018

Accepted date: 3 October 2018

Please cite this article as: He Zhang, Kaushal Chari, Manish Agrawal , Decision support for the optimal allocation of security controls. Decsup (2018), doi:10.1016/ j.dss.2018.10.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# DECISION SUPPORT FOR THE OPTIMAL ALLOCATION OF SECURITY CONTROLS

He Zhang, Kaushal Chari and Manish Agrawal Muma College of Business, University of South Florida, Tampa, FL 33620 [hezhang, kchari, magrawal]@usf.edu

## Abstract

We present constrained optimization models that could be used in a decision support system for configuring security solutions for an information systems infrastructure. We begin with a deterministic model that uses security breach probabilities as parameters. Since security breach data is not easily available, breach probabilities are often estimated via surveys, which could lead to estimation errors. To develop robust solutions in the presence of estimation errors, we then present a stochastic optimization model that handles uncertainties in breach probability estimations. Our model solutions incorporate quantifiable security risk and business impact as the models are detailed enough to capture various categories of security attacks, and different levels of security protection and loss values for data and applications. We demonstrate the utility of our models by proposing security solutions for a realistic IT infrastructure using breach probability estimates derived from surveys.

Keywords: Design and evaluation of IT infrastructure, constrained optimization, stochastic programming, analytical modeling, decision support system, risk management, security breaches, security survey.

## 1. Introduction

Security breaches are now being reported almost routinely. Facebook just reported a security breach affecting 50 million users (Isaac and Frenkel 2018). In March 2018, the City of Atlanta became a victim of a ransomware attack (Blinder and Perlroth 2018). Other major security breach incidents include the data breach at Equifax that affected 147.9 million consumers (Clements 2018); the WannaCry

ransomware outbreak that infected more than 230,000 computers in 150 countries in 2017 (Bossert 2017); Yahoo breaches in 2016 affecting over a billion user accounts (Yahoo 2016); US Internal Revenue Service breach in 2017 compromising the data on approximately 100,000 taxpayers (Rappeport 2017); the breach at Home Depot, where credit card details were stolen using malware installed at cash registers (Lobosco 2014); the Target breach, affecting up to 70 million customers (Yang and Jayakumar 2014); and the breach at JP Morgan Chase, where hackers accessed personal information of bank cu ers (Goldstein et al. 2014). These breaches had negative consequences on victim compa s. For example, Target estimated a cost of \$148 million to its shareholders due to the data breach (Sharf 2014).

The 2016 US State of Cybercrime Survey of over 400 US organizations co-sponsored by PricewaterhouseCoopers, CSO magazine, CERT Division of Software Engineering Institute, and the United States Secret Service (PwC 2015) reveals some interesting statistics: 79% of respondents had detected a security incident in the most recent year and 76% of respondents were more concerned about cybersecurity threats in the current year compared to the previous year.

In response, organizations are increasing information security investments. Gartner estimates that global information security investments will rise from \$80 billion in 2016 to \$93 billion in 2018 (Gartner Research 2018). Notwithstanding these large investments, in the above US State of Cybercrime Survey, only 38% of respondents indicated prioritization of security investments based on risk and impact to business. This suggests that the majority of information security spending is not aligned with risks and impacts to business. Plausible reasons for this misalignment include: a) Lack of data to quantify cyber security risks (the Cybercrime survey reported that only 47% of organizations performed periodic risk assessments); b) Use of unscientific ad hoc approaches that do not take quantifiable risks into account while directing cybersecurity enhancing investments. Thus, while many organizations have been making large cybersecurity enhancing investments in response to various security threats as well as to comply with various regulations such as the Sarbanes-Oxley Act, they have been doing so mostly in the dark. The

# ACCEPTED MANUSCRIPT

goal of this research is to address this limitation by developing highly granular risk-based models as components of a decision support system for planning optimal cybersecurity enhancing investments.

This issue has attracted research attention. Early studies determined optimal security investments by assuming certain functional forms and associated parameter values to model risk components (Gordon and Loeb 2002; Yue et al. 2007). (Cavusoglu et al. 2005) used a game theoretic approach to determine the value of controls, but assumed risk parameters to be known. While the above papers present elegant models, their utility is limited by the accuracy of risk parameter estimates or the applicability of functional forms used. They do not directly address the problem of allocating specific security controls.

Research on determining the optimal allocation of security controls (also referred to as counter measures) is in the nascent stages. Sawik (2013) proposed a mixed-integer programming model using a conditional value at risk approach for optimal selection of countermeasures, given a set of potential threats and a set of available controls. Rakes et al. (2012) proposed an integer programming model for optimal allocation of counter measures for a given threat level profile. The approaches in both Sawik (2013) and Rakes et al. (2012) require enumerating all possible threats and estimating every counter measure’s effectiveness against each of the threats. This is usually not very practical to implement. Yeo et. al (2014) used a workflow based model for control assignment. However, all security attacks, their paths, as well as controls needed to counter these attacks need to be predetermined in order to use the workflow model. This may pose challenges in practice as attackers constantly discover new paths for security attacks.

Simulation based approaches available in the literature (Conrad 2005; Kumar et al. 2008; Wang et al. 2008), typically use synthetic data to evaluate security measures. These papers do not directly address the problem of optimal allocation of controls for an IT infrastructure, given risk and cost data.

In the current security environment, there has been considerable interest in developing decision support systems (DSS) to assist managers in optimizing security controls. Rees et al. (2011) propose a

# ACCEPTED MANUSCRIPT

DSS for computing the uncertain risk faced by an organization under cyber-attack. El-Gayar and Fritz (2010) present an architecture and design for a web-based multi-perspective decision support system and underlying multi-criteria decision framework for security decision making and planning. The DSS allows various stakeholders (e.g. IT and executives) to determine weights for different priorities at each stage of the decision-making process - asset identification, threat assessment and control selection. While useful, the granularity of the systems proposed in these papers needs to be improved for determining the optimum allocation of controls. Table 1 summarizes relevant work related to the allocation of security controls.

Table 1: Relevant prior work

<table><tr><td>Research</td><td>Description</td><td>Comments</td><td>Allocation of Specific Security Controls</td></tr><tr><td>(Gordon and Loeb 2002)</td><td>Analytical model to determine optimal information security investment</td><td>Determines the optimal investment in security, without identifying security controls</td><td>No</td></tr><tr><td>(Yue et al. 2007)</td><td>Optimal security investment for system-specific and general security measures</td><td>Determines the optimal investment in security, without identifying security controls</td><td>No</td></tr><tr><td>(Cavusoglu et al. 2005)</td><td>Game theoretic model to determine the value of intrusion detection systems</td><td>Assumes knowledge of the hacker's utility and costs of intrusion</td><td>No</td></tr><tr><td>(Rees et al. 2011)</td><td>Genetic algorithms and scenarios to select optimal set of controls</td><td>Assumes the availability of accurate estimates of control breach probabilities</td><td>Yes</td></tr><tr><td>(Rakes et al. 2012)</td><td>An integer programming model for optimal allocation of counter measures for a given threat level profile</td><td>Requires enumerating all possible threats as well as assumes the availability of accurate estimates of every control's effectiveness against each of the threats</td><td>Yes</td></tr><tr><td>(Sawik 2013)</td><td>Mixed integer programming model for the optimal selection of security controls</td><td>Requires enumerating all possible threats as well as assumes the availability of accurate estimates of every control's effectiveness against each of the threats</td><td>Yes</td></tr><tr><td>(Yeo et al. 2014)</td><td>Analytical model to determine optimal security control placement in business process workflow</td><td>Requires prior enumeration of all security incident patterns as inputs to a deterministic model</td><td>Yes</td></tr><tr><td>Current</td><td>Analytical models for the allocation of optimal set of security controls</td><td>Handles uncertainties in the estimates of threat survival in the presence of controls; does not require prior enumeration of all possible threats; explicitly models classes of breaches such as availability breaches</td><td>Yes</td></tr></table>

A challenge for the current research is that it is necessary to estimate breach probabilities to

determine the optimal allocation of controls. Breach probabilities in the presence of controls are not easily available. Instead, many studies estimate parameters such as bypass rates or component failure rates from sources such as historical data observed over a period of time (Arora et al. 2004), or vulnerability and/or patch release data stored in public databases (NIST 2008). Typically, this data is either sparse or has a lot of noise, and cannot be used to accurately assess the security risks of any given IT infrastructure, especially when the data gathering environment does not match the specific environment or configuration of the IT infrastructure.

In this paper, we explicitly incorporate breach probability estimates in an optimization model for allocating security controls in any given IT infrastructure with the goal of minimizing the sum of losses due to security breaches and the total cost of controls. Our model, which is highly granular, determines control allocations that are in alignment with risk and business impact. To account for the noise in model parameter estimates such as breach probabilities, we present a stochastic version of the optimization model that improves the robustness of the solutions by addressing uncertainties in breach probability estimates. This is a key contribution of this paper. The model is then applied to a realistic IT infrastructure, using probability estimates from a survey of security professionals. We conduct computational experiments to show how the model can be used to estimate optimal changes in security expenses. Finally, we present a high level DSS architecture for security planning based on our models.

This paper is organized as follows. In Section 2, we present optimization models for determining optimal allocation of security controls. In Section 3, we describe our approach for determining breach probabilities. We then present results from our computational experiments in Section 4. In Section 5, we present a high level DSS architecture for a system to support security planning. Conclusions are provided in Section 6. An appendix contains a description of the process used to determine a realistic IT

## 2. Models for Optimal Allocation of Controls

The allocation of controls is designed to prevent three types of security breaches described below.

## 2.1 Types of Security Breaches

The US Code Title 44, Chapter 35, Section 3542 (U.S. Code 2000) defines information security as protecting information and information systems from unauthorized access, use, disclosure, disruption, modification, or destruction in order to provide the following.

(A) Integrity: guarding against improper information modification or destruction that ensures information non-repudiation and authenticity;

(B) Confidentiality: preserving authorized restrictions on access and disclosure, including means for protecting personal privacy and proprietary information; and

(C) Availability: ensuring timely and reliable access to and use of information.

The models presented in Section 2.4 (deterministic) and Section 2.5 (stochastic) capture the losses associated with integrity, confidentiality and availability breaches.

An IT infrastructure typically consists of client machines, server hosts that run different server applications, storage devices to store databases, and a networking infrastructure to connect various devices. To increase availability or scalability, servers are replicated in server farms. Multiple types of transactions are typically initiated from client machines. To protect the IT infrastructure from integrity, confidentiality and availability breaches, various types of controls are used. These include perimeter routers, proxy servers and host specific controls such as host firewalls. Controls have overlapping coverages against security attacks, i.e., multiple controls can protect against some aspects of the same attack. The use of general controls such as perimeter routers, as well as host specific controls such as web server security modules and strong password policies, reduce the likelihood of breaches, but do not guarantee complete security. The failure probabilities of integrity, confidentiality and availability breaches depend on both the general controls as well as host specific controls. An optimal security control allocation model minimizes the costs of security controls and expected breach costs in the presence of these controls. The models developed in this paper account for these dependencies.

## 2.2 Notations

The notations used in our models are in Table 2.

Table 2: Notations

<table><tr><td colspan="2">Sets</td></tr><tr><td>T</td><td>Index set of transaction types</td></tr><tr><td>F</td><td>Index set of farms. A farm is a collection of computers running similar applications for load balancing and fault tolerance</td></tr><tr><td> $F_t$ </td><td>Index set of farms used in processing transaction  $t \in T$ </td></tr><tr><td> $N_f$ </td><td>Index set of nodes (i.e., computers) in farm  $f \in F$ </td></tr><tr><td>N</td><td>Index set of all nodes across various farms, i.e.,  $\bigcup_{f \in F} N_f$ </td></tr><tr><td>G</td><td>Index set of general security setting types based on one or more controls such as a perimeter router</td></tr><tr><td>S</td><td>Index set of host specific security setting types based on one or more controls such as a host-specific firewall</td></tr><tr><td colspan="2">Input Parameters</td></tr><tr><td> $t^a$ </td><td>Average time to restore the system due to an availability breach</td></tr><tr><td> $r^d_t$ </td><td>Desired transaction rate of transactions of type  $t \in T$  (in transactions per minute); this rate is achieved when the processing capacities of servers are optimally realized</td></tr><tr><td> $Q_p$ </td><td>Capacity of node p in transactions per minute</td></tr><tr><td> $\pi_{tf}$ </td><td>Number of sub-transactions spawned from a single transaction of type  $t \in T$  at farm  $f \in F$ </td></tr><tr><td> $c^l_t$ </td><td>Unit cost of transaction loss rate of transaction type  $t \in T$ , due to an availability breach</td></tr><tr><td> $c^g_i$ </td><td>Unit cost of general security setting of type  $i \in G$ </td></tr><tr><td> $C^{s}_{pj}$ </td><td>Unit cost of host specific security setting of type  $j \in S$  used at node p</td></tr><tr><td> $l^i_p$ </td><td>Average loss amount when there is an integrity breach of files at node p</td></tr><tr><td> $l^c_p$ </td><td>Average loss amount when there is a confidentiality breach of files at node p</td></tr><tr><td> $\gamma$ </td><td>An input parameter that represents the processing capacity of a farm in transactions/min</td></tr><tr><td colspan="2"> $\alpha_{c,m}, \alpha_{i,m},$  and  $\alpha_{a,m}$  are coefficients of expense terms in the  $m^{th}$  equations that are piecewise linear</td></tr></table>

ACCEPTED MANUSCRIPT

<table><tr><td>approximations of confidentiality, integrity and availability breach probabilities as functions of expense respectively</td></tr><tr><td> $\beta_{c,m}, \beta_{i,m}$ , and  $\beta_{a,m}$  are intercept terms in the  $m^{\text{th}}$  equations that are piecewise linear approximations of confidentiality, integrity and availability breach probabilities as functions of expense respectively</td></tr><tr><td> $\varepsilon_c, \varepsilon_b, \varepsilon_a$  are random errors for confidentiality, integrity and availability breach probability estimates respectively</td></tr><tr><td> $\xi$  is a vector of  $\varepsilon_c, \varepsilon_b, \varepsilon_a$ </td></tr><tr><td> $k_c, k_i$ , and  $k_a$  denote the number of piecewise linear approximation segments used for confidentiality, integrity and availability breach probabilities</td></tr><tr><td>Functions</td></tr><tr><td> $v^{a}_{p}([y_i]_{i \in G}, [z_{pj}]_j \in s)$ Probability of availability breach at node  $p$ , given  $p$  is shielded by controls  $[y_i]_{i \in G}$  and  $[z_{pj}]_j \in s$ ; For better readability  $v^{a}_{p}$  will be used without any parenthesis when necessary</td></tr><tr><td> $v^{i}_{p}([y_i]_{i \in G}, [z_{pj}]_j \in s)$ Probability of integrity breach at node  $p$ , given  $p$  is shielded by controls  $[y_i]_{i \in G}$  and  $[z_{pj}]_j \in s$ ; For better readability  $v^{a}_{p}$  will be used without any parenthesis when necessary</td></tr><tr><td> $v^{c}_{p}([y_i]_{i \in G}, [z_{pj}]_j \in s)$ Probability of confidentiality breach at node  $p$ , given  $p$  is shielded by controls  $[y_i]_{i \in G}$  and  $[z_{pj}]_j \in s$ ; For better readability  $v^{a}_{p}$  will be used without any parenthesis when necessary</td></tr><tr><td> $h^{p}_{f}(v^{a}_{p}, Q_{p})$ is a convex and monotonically non-decreasing function of  $v^{a}_{p}$  and  $Q_{p}$  used for computing the expected decrease in the processing capacity of farm  $f$  due to availability breach at node  $p$  in  $f$ </td></tr><tr><td> $g_{f}([v^{a}_{p}]_{p \in Nf}, [Q_{p}]_{p \in Nf})$ is a function to compute the expected transaction rate at farm  $f$ , given vectors  $[v^{a}_{p}]$  and  $[Q_{p}]$  for the nodes in  $f$ </td></tr><tr><td>Variables</td></tr><tr><td> $r^{e}_{t}$  Expected transaction rate of transactions of type  $t \in T$  (in transactions per minute)</td></tr><tr><td> $y_i = 1$  if general security setting of type  $i \in G$  used in the IT infrastructure; 0 otherwise</td></tr><tr><td> $z_{pj} = 1$  if host specific security setting of type  $j \in S$  used at node  $p$ ; 0 otherwise</td></tr><tr><td> $exp_p$  is the total expense related to security controls shielding node  $p$  and is given by  $\sum_{i \in G} c_i^g y_i + \sum_{j \in S} C_{pj}^s z_{pj}$ </td></tr><tr><td> $u^{c}_{p}$  and  $u^{i}_{p}$  are variables that represent the estimate of confidentiality and integrity breach probabilities from the piecewise linear approximations of confidentiality and integrity breach probabilities respectively</td></tr></table>

## 2.3 Modeling Overview

We make the following assumptions while developing our models. These assumptions make our models tractable with minimal loss of generality.

Assumption 1: All transaction types incur the same processing time at any host. Hence the processing capacity of computers is represented by the number of transactions per minute. This assumption can be easily relaxed by adding appropriate scaling factors based on actual transaction times of different transaction types, thereby making the model more detailed.

# ACCEPTED MANUSCRIPT

Assumption 2: For each node $p ,$ the breach probabilities $\nu _ { ~ p } ^ { a } ( [ y _ { i } ] _ { i } \in \cal G , ~ [ z _ { p j } ] _ { j } \in \cal S ) , ~ \nu _ { ~ p } ^ { i } ( [ y _ { i } ] _ { i } \in \it G , ~ [ z _ { p j } ] _ { j } \in \cal S )$ and $\nu _ { \ p } ^ { c } ( [ y _ { i } ] _ { i \in G } , [ z _ { p j } ] _ { j \in S } )$ are convex piecewise linear functions with respect to security settings $[ y _ { i } ] _ { i \in G }$ and $[ z _ { p j } ] _ { j \in S } .$ . We later provide empirical evidence to support diminishing returns for security expenses.

Assumption 3: The transaction rate function $g _ { f } ( [ \nu _ { ~ p } ^ { a } ] _ { p \in N f } , [ Q _ { p } ] _ { p \in N f } )$ is separable with respect to the breach probability $\nu _ { \ p } ^ { a } ,$ , i.e., ${ \bf g } _ { f } ( [ \nu _ { ~ p } ^ { a } ] _ { p \in N f } , [ Q _ { p } ] _ { p \in N f } ) \ = \ - \ \sum _ { p \in N _ { f } } h _ { f } ^ { p } \left( \nu _ { p } ^ { a } , Q _ { p } \right) + \gamma$

$\forall \ p \in N _ { f } ,$ given $Q _ { p } ,$ the function $h _ { f } ^ { p } ( \nu _ { p } ^ { a } , Q _ { p } )$ is a convex and monotonically non-decreasing function with respect to $\nu _ { ~ p , } ^ { a }$ <sub>,</sub> and $\gamma$ is a constant. Later, we show the detailed mapping of $h _ { f } ^ { p } ( \nu _ { p } ^ { a } , Q _ { p } )$ and $\gamma$ for our computational example, where $h _ { f } ^ { p } ( \nu _ { p } ^ { a } , Q _ { p } )$ computes the magnitude of expected reduction in the transaction rates of nodes in farm f due to availability breaches and $\gamma$ maps to the total installed processing capacity of the farm in terms of the total transaction rate. This provides a general method to model transaction rates as a monotonically non-increasing function of breach probabilities.

We now develop deterministic and stochastic models for security control allocation. Figure 1 gives a high level overview of our models and model transformations developed in sections 2.4 and 2.5.

## 2.4 Deterministic Model

We start with a deterministic model for allocating controls that minimizes the cost of controls and losses due to successful breaches. An optimal assignment of controls can be obtained by solving the following deterministic model.

Problem P1: $Z _ { 1 } = \operatorname * { m i n } { \phantom { - } } \sum _ { t \in T } c _ { t } ^ { l } \left( r _ { t } ^ { d } - r _ { t } ^ { e } \right) t ^ { a } + \sum _ { p \in N } l _ { p } ^ { c } \nu _ { p } ^ { c } \left( \left[ y _ { i } \right] _ { i \in G } , \left[ z _ { p j } \right] _ { j \in S } \right) +$

$$
\sum_ {p \in N} l _ {p} ^ {i} v _ {p} ^ {i} \left(\left[ y _ {i} \right] _ {i \in G}, \left[ z _ {p j} \right] _ {j \in S}\right) + \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {p \in N} \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j}\tag{1}
$$

subject to

$$
\sum_ {t \in T} r _ {t} ^ {e} \pi_ {t f} \leq g _ {f} \left(\left[ v _ {p} ^ {a} \right] _ {p \in N _ {f}}, \left[ Q _ {p} \right] _ {p \in N _ {f}}\right) \forall f \in F\tag{2}
$$

$$
r _ {t} ^ {e} \leq r _ {t} ^ {d} \quad \forall t \in T\tag{3}
$$

$$
\sum_ {i \in G} y _ {i} = 1\tag{4}
$$

$$
\sum_ {j \in S} z _ {p j} = 1 \quad \forall p \in N\tag{5}
$$

$$
y _ {i} \in \{0, 1 \} \forall i \in G; z _ {p j} \in \{0, 1 \} \forall p \in N, j \in S; v _ {p} ^ {a}, v _ {p} ^ {i}, v _ {p} ^ {c} \geq 0 \forall p \in N
$$

$$
r _ {t} ^ {e} \geq 0 \forall t \in T\tag{6}
$$

The objective function (1) captures the tradeoffs between the losses due to security breaches and the cost of security settings consisting of one or more controls. These tradeoffs are enabled by the failure probabilities of breaches $\nu _ { { p } } ^ { a } , \nu _ { { p } } ^ { c } ,$ and $\nu _ { { p } } ^ { i }$ in the model, as they are determined by security expenses which in turn are determined by decision variables $y _ { i }$ and $z _ { p j } .$ The first three te ms in the objective function denote losses due to availability, confidentiality and integrity breaches respectively. The last two terms denote the cost of general as well as host-specific security settings respectively. Constraint (2) requires that server farms have adequate capacity to handle the expected transaction rate needs. Constraint (3) dictates that the expected transaction rate be less than or equal to the desired transaction rate for transactions of that type. The expected transaction rate is based on availability considerations (Highleyman et al. 2003), and is determined by $g _ { f } .$ , which is a function of the vectors of probabilities of failure due to availability breach $\nu _ { ~ p } ^ { a }$ and transaction processing capacities $Q _ { p } ,$ for nodes in $f .$ Constraint (4) requires that one general security setting be used, while constraint (5) requires that one security setting be used at any given host. A security setting refers to a specified combination of available controls. Note that the decision variables $y _ { i }$ and $z _ { p j }$ are binary integers. Security setting expenses are annualized and consist of depreciation and maintenance expenses. Breach probabilities $\nu _ { ~ p } ^ { a } , \nu _ { ~ p , } ^ { i } \nu _ { ~ p } ^ { c }$ are obtained through empirically determined functions, while the desired transaction rate, $r _ { { t } } ^ { d } \ge 0$ is exogenous to P1, and can be set to desired values that do not exceed the transaction processing capacity of a farm when availability breach probabilities are 0 as given by constraint (7).

$$
\sum_ {t \in T} r _ {t} ^ {e} \pi_ {t f} \leq g _ {f} \left(\left[ 0 \right] _ {p \in N _ {f}}, \left[ Q _ {p} \right] _ {p \in N _ {f}}\right) \quad \forall f \in F\tag{7}
$$

Figure 1: Models and Model Transformations  
Deterministic Model  
![](/api/attachments/VK2E82CQ/fulltext/images/5c0b4375406a4d4dc9aea403e617d278da75e9342738115baa326833e0fbeba1.jpg)

When the model is solved, the optimal security setting, which is an assignment of controls (such as firewalls, packet filtering routers, etc.), is determined such that the total cost is minimized. Figure 1 shows various model transformations.

In Problem P1 (1)-(6), the breach probabilities $\boldsymbol { \nu } _ { \ p } ^ { c } , \boldsymbol { \nu } _ { p } ^ { i }$ and $\nu _ { ~ p } ^ { a }$ are functions with respect to decision variables $y _ { i } ,$ and $z _ { p j } . \nu _ { { p } } ^ { c } , \nu _ { p } ^ { i }$ and $\nu _ { ~ p } ^ { a }$ are convex piecewise linear functions of total security expense for node $p .$ Note there are $k _ { c } , k _ { i } ,$ and $k _ { a }$ piecewise linear functions for confidentiality, integrity and availability breaches respectively.

$$
v _ {p} ^ {c} = \max _ {m = 1, \dots , k c} \left\{\alpha_ {c, m} \exp_ {p} + \beta_ {a, m} \right\} s\tag{8}
$$

$$
v _ {p} ^ {i} = \max _ {m = 1, \dots , k i} \left\{\alpha_ {i, m} \exp_ {p} + \beta_ {i, m} \right\}\tag{9}
$$

$$
v _ {p} ^ {a} = \max _ {m = 1, \dots , k a} \left\{\alpha_ {a, m} \exp_ {p} + \beta_ {a, m} \right\}\tag{10}
$$

Where $e x p _ { p }$ is the total cost of the general and specific security setting shielding node $p ,$ which is determined by $y _ { i } , i { \in } G , z _ { p j } , j { \in } S$ as:

$$
\exp_ {p} = \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} \quad \forall p \in N\tag{11}
$$

Per Assumption 2, the breach probabilities $\nu _ { ~ p } ^ { c } , \nu _ { ~ p } ^ { i }$ and $\nu _ { ~ p } ^ { a }$ can be modeled as non-increasing convex functions because of the diminishing returns. For computational modeling, we use piecewise linear convex functions to approximate these breach probabilities, since convex functions can be approximated to any accuracy by using piecewise linear convex functions. Based on Assumption 3 that assumes independence of availability breaches across nodes in a farm, we have

$$
g _ {f} \left(\left[ v _ {p} ^ {a} \right] _ {p \in N _ {f}}, \left[ Q _ {p} \right] _ {p \in N _ {f}}\right) = - \sum_ {p \in N _ {f}} q (Q _ {p}) v _ {p} ^ {a} + \gamma\tag{12}
$$

Where $q ( Q _ { p } )$ is a function of $Q _ { p }$ and $\gamma$ is a constant as specified previously. Note, $h _ { f } ^ { p } ( \nu _ { p } ^ { a } , Q _ { p } ) = q ( { \cal Q } _ { p } ) \nu _ { p } ^ { a } .$ Recall from Section 2.3, $h _ { f } ^ { p } ( \nu _ { p } ^ { a } , Q _ { p } )$ denotes the expected transaction processing capacity that is lost due to availability breaches at node $p$ of farm $f ,$ while $\gamma$ denotes the installed transaction processing capacity of f. Thus the left hand side of (12) denotes the expected transaction rate of f and is based on the assumption that the availability breaches in the nodes of f are independent of each other.

After incorporating (8)-(12) in P1, the problem transforms to P2.

$$
\text { P2: } Z _ {2} = \min \sum_ {t \in T} c _ {t} ^ {l} \left(r _ {t} ^ {d} - r _ {t} ^ {e}\right) t ^ {a} + \sum_ {p \in N} l _ {p} ^ {c} \max _ {m = 1, \dots , k _ {c}} \left\{\alpha_ {c, m} \exp_ {p} + \beta_ {c, m} \right\} +
$$

$$
\sum_ {p \in N} l _ {p} ^ {i} \max _ {m = 1, \dots , k _ {i}} \left\{\alpha_ {i, m} \exp_ {p} + \beta_ {i, m} \right\} + \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {p \in N} \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j}\tag{13}
$$

subject to

$$
\exp_ {p} = \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} \quad \forall p \in N\tag{14}
$$

$$
\sum_ {t \in T} r _ {t} ^ {e} \pi_ {t f} \leq - \sum_ {p \in N _ {f}} q (Q _ {p}) \max _ {m = 1, \dots , k _ {a}} \left\{\alpha_ {a, m} \exp_ {p} + \beta_ {a, m} \right\} + \gamma \quad \forall f \in F\tag{15}
$$

$$
r _ {t} ^ {e} \leq r _ {t} ^ {d} \quad \forall t \in T\tag{16}
$$

$$
\sum_ {i \in G} y _ {i} = 1\tag{17}
$$

$$
\sum_ {j \in S} z _ {p j} = 1 \quad \forall p \in N\tag{18}
$$

$$
y _ {i} \in \{0, 1 \} \forall i \in G; z _ {p j} \in \{0, 1 \} \forall p \in N, j \in S; r _ {t} ^ {e} \geq 0 \forall p \in N\tag{19}
$$

To transform P2 into a mixed linear integer programming problem in standard form, we apply standard techniques to transform nonlinear convex piecewise linear equations to linear constraints (Bertsimas and Tsitsiklis 1997). Thus, P2 can be rewritten as the following linear integer programming problem P21.

$$
\text { P21: } Z _ {2} = \sum_ {t \in T} c _ {t} ^ {l} \left(r _ {t} ^ {d} - r _ {t} ^ {e}\right) t ^ {a} + \sum_ {p \in N} l _ {p} ^ {c} u _ {p} ^ {c} + \sum_ {p \in N} l _ {p} ^ {i} u _ {p} ^ {i} + \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {p \in N} \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j}\tag{20}
$$

subject to

$$
u _ {p} ^ {c} \geq \alpha_ {c, m} \mathrm{exp} _ {p} + \beta_ {c, m}, m = 1, \ldots , k _ {c}\tag{21}
$$

$$
u _ {p} ^ {i} \geq \alpha_ {i, m} \exp_ {p} + \beta_ {i, m}, m = 1, \dots , k _ {i}\tag{22}
$$

$$
\exp_ {p} = \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} \quad \forall p \in N\tag{23}
$$

$$
\sum_ {t \in T} r _ {t} ^ {e} \pi_ {t f} \leq - \sum_ {p \in N _ {f}} q (Q _ {p}) \left(\alpha_ {a, m _ {p}} \exp_ {p} + \beta_ {a, m _ {p}}\right) + \gamma \quad \forall f \in F, m _ {p} = 1, \dots , k _ {a} \quad \forall p\tag{24}
$$

$$
r _ {t} ^ {e} \leq r _ {t} ^ {d} \quad \forall t \in T\tag{25}
$$

$$
\sum_ {i \in G} y _ {i} = 1\tag{26}
$$

$$
\sum_ {j \in S} z _ {p j} = 1 \quad \forall p \in N\tag{27}
$$

$$
y _ {i} \in \{0, 1 \} \forall i \in G; z _ {p j} \in \{0, 1 \} \forall p \in N, j \in S; r _ {t} ^ {e} \geq 0 \forall p \in N\tag{28}
$$

P21 is a mixed linear integer programming problem that can be solved using a solver such as CPLEX.

## 2.5 Stochastic Model with Uncertainty in Breach Probability Estimates

When there are uncertainties in breach probabilities, we can use a piecewise linear model to fit the survey data for breach probabilities as a function of control expenses. The uncertainty is modeled as a log-normal distributed random variable and the breach probabilities are modeled as the product of the random variable and the deterministic convex piecewise linear function in (8)-(10). The following expressions can be used to fit estimated breach probabilities as a function of control expenses:

$$
v _ {p} ^ {c} = \varepsilon_ {c} \cdot \max _ {m = 1, \dots , k c} \left\{\alpha_ {c, m} \exp_ {p} + \beta_ {c, m} \right\}\tag{29}
$$

$$
v _ {p} ^ {i} = \varepsilon_ {i} \cdot \max _ {m = 1, \dots , k i} \left\{\alpha_ {i, m} \exp_ {p} + \beta_ {i, m} \right\}\tag{30}
$$

$$
v _ {p} ^ {a} = \varepsilon_ {a} \cdot \max _ {m = 1, \dots , k a} \left\{\alpha_ {a, m} \exp_ {p} + \beta_ {a, m} \right\}\tag{31}
$$

Where the random errors $\mathcal { E } _ { c } , \mathcal { E } _ { i } , \mathcal { E } _ { a }$ are given as

$$
l n (\varepsilon_ {c}) \sim N (\mu_ {c}, \sigma_ {c} ^ {2}), l n (\varepsilon_ {i}) \sim N (\mu_ {i}, \sigma_ {i} ^ {2}), l n (\varepsilon_ {a}) \sim N (\mu_ {a}, \sigma_ {a} ^ {2})\tag{32}
$$

We use all other parameters from the deterministic model in the stochastic model. Consider the decision variables: $r ^ { e } { } _ { t } , y _ { i } , i \in G ,$ , and $\mathsf { z } _ { p j } , p \in N , j \in S .$ . The variables representing general and host-specific control settings y<sub>i</sub> and $z _ { p j }$ now have to be determined based on uncertain breach probabilities. However, the expected transaction rate of transaction of type $t , r _ { t } ^ { e } ,$ depends on the actual value of the breach probability $\nu _ { \ p } ^ { a } .$ To incorporate this, the control allocation model can be written as a two-stage stochastic programming problem as follows:

Stage 1:

$$
\mathrm{P} 3: Z _ {3} = \min _ {y _ {i}, z _ {p j}} \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {p \in N} \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} + \mathrm{E} _ {\xi} [ U (\mathbf {e x p}, \xi) ]\tag{33}
$$

subject to

$$
\exp_ {p} = \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} \quad \forall p \in N\tag{34}
$$

$$
\sum_ {i \in G} y _ {i} = 1\tag{35}
$$

$$
\sum_ {j \in S} z _ {p j} = 1 \quad \forall p \in N\tag{36}
$$

$$
y _ {i} \in \{0, 1 \} \forall i \in G; z _ {p j} \in \{0, 1 \} \forall p \in N, j \in S\tag{37}
$$

where exp is the vector of security control expenses associated with all the nodes and is given by $( \exp _ { p } ) _ { p \in }$ $N , \ \xi$ is the random error vector and is given by $( \varepsilon _ { c } , \varepsilon _ { i } , \varepsilon _ { a } ) ^ { T } , U ( \mathbf { e x p } , \boldsymbol { \xi } )$ is the business loss when control expense exp is used optimally, $\mathrm { E } _ { \xi } \left[ U ( \mathbf { e x p } , \xi ) \right]$ is the expectation of U(exp, $\xi )$ with respect to $\xi .$ We compute U(exp, $\xi )$ as the optimal value of the Stage 2 problem as follows:

Stage 2:

$$
U (\mathbf {e x p}, \xi) = \min _ {r _ {t \xi} ^ {e}} \sum_ {t \in T} c _ {t} ^ {l} \left(r _ {t} ^ {d} - r _ {t \xi} ^ {e}\right) t ^ {a} + \sum_ {p \in N} l _ {p} ^ {c} \varepsilon_ {c} u _ {p} ^ {c} + \sum_ {p \in N} l _ {p} ^ {i} \varepsilon_ {i} u _ {p} ^ {i}\tag{38}
$$

subject to:

$$
u _ {p} ^ {c} \geq \alpha_ {c, m} \exp_ {p} + \beta_ {c, m}, m = 1, \dots , k _ {c}\tag{39}
$$

$$
u _ {p} ^ {i} \geq \alpha_ {i, m} \mathrm{exp} _ {p} + \beta_ {i, m}, m = 1, \ldots , k _ {i}\tag{40}
$$

$$
\sum_ {t \in T} r _ {t \xi} ^ {e} \pi_ {t f} \leq - \sum_ {p \in N _ {f}} q (Q _ {p}) \varepsilon_ {a} \left(\alpha_ {a, m _ {p}} \exp_ {p} + \beta_ {a, m _ {p}}\right) + \gamma \quad \forall f \in F, m _ {p} = 1, \dots , k _ {a} \quad \forall p\tag{41}
$$

$$
r _ {t \xi} ^ {e} \leq r _ {t} ^ {d} \quad \forall t \in T\tag{42}
$$

$$
r _ {t \xi} ^ {e} \geq 0 \quad \forall t \in T\tag{43}
$$

Note that the second stage optimal objective value U(exp, $\xi )$ depends on both exp and the random error vector $\xi .$ Problem (33)-(43) follows a standard two-stage stochastic programming framework in which the first-stage decision variables y and z only depend on the expectation, while the second stage variable $\boldsymbol { r } _ { \ t } ^ { e }$ depends on the actual scenario of $\xi .$ Since $\varepsilon _ { c }$ and $\varepsilon _ { i }$ only appear in the objective function U(exp, $\xi )$ of the second-stage problem and not in the constraints, therefore the random variables $\varepsilon _ { c } , \varepsilon _ { i } ,$ and $\varepsilon _ { a }$ are separable and easy to solve. Thus, the above model can be written as P4:

$$
\mathrm{P} 4: Z _ {4} = \min _ {y _ {i}, z _ {p j}} + \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {p \in N} \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} + \sum_ {p \in N} l _ {p} ^ {c} \mathrm{E} \left[ \varepsilon_ {c} \right] u _ {p} ^ {c} + \sum_ {p \in N} l _ {p} ^ {i} \mathrm{E} \left[ \varepsilon_ {i} \right] u _ {p} ^ {i} + \mathrm{E} _ {\xi} [ V (\mathbf {e x p}, \xi) ]\tag{44}
$$

subject to

$$
u _ {p} ^ {c} \geq \alpha_ {c, m} \exp_ {p} + \beta_ {c, m}, m = 1, \dots , k _ {c}\tag{45}
$$

$$
u _ {p} ^ {i} \geq \alpha_ {i, m} \mathrm{exp} _ {p} + \beta_ {i, m}, m = 1, \ldots , k _ {i}\tag{46}
$$

$$
\exp_ {p} = \sum_ {i \in G} c _ {i} ^ {g} y _ {i} + \sum_ {j \in S} C _ {p j} ^ {s} z _ {p j} \quad \forall p \in N\tag{47}
$$

$$
\sum_ {i \in G} y _ {i} = 1\tag{48}
$$

$$
\sum_ {j \in S} z _ {p j} = 1 \quad \forall p \in N\tag{49}
$$

$$
y _ {i} \in \{0, 1 \} \forall i \in G; z _ {p j} \in \{0, 1 \} \forall p \in N, j \in S\tag{50}
$$

Where $\mathbf { e x p } = ( \exp _ { \mathsf { p } } ) _ { p \in N } , \boldsymbol { \xi } = ( \varepsilon _ { c } , \varepsilon _ { i } , \varepsilon _ { a } ) ^ { T }$ and V(exp, $\xi )$ is the optimal value of the Stage 2 problem.

$$
V (\mathbf {e x p}, \xi) = \min _ {r _ {t \xi} ^ {e}} \sum_ {t \in T} c _ {t} ^ {l} \left(r _ {t} ^ {d} - r _ {t \xi} ^ {e}\right) t ^ {a}\tag{51}
$$

subject to

$$
\sum_ {t \in T} r _ {t \xi} ^ {e} \pi_ {t f} \leq - \sum_ {p \in N _ {f}} q (Q _ {p}) \varepsilon_ {a} \left(\alpha_ {a, m _ {p}} \exp_ {p} + \beta_ {a, m _ {p}}\right) + \gamma \quad \forall f \in F, m _ {p} = 1, \dots , k _ {a} \quad \forall p\tag{52}
$$

$$
r _ {t \xi} ^ {e} \leq r _ {t} ^ {d} \quad \forall t \in T\tag{53}
$$

$$
r _ {t \xi} ^ {e} \geq 0 \quad \forall t \in T\tag{54}
$$

Figure 2 displays the flowchart for solving problem P4.  
Figure 2: Flow chart for solving P4  
![](/api/attachments/VK2E82CQ/fulltext/images/7015878bc2d5d79a88a731650e3487ac6753ab02b080d3409a25100c8bf521d9.jpg)

The two stage stochastic optimization problem P4 can be solved with the sample average approximation (SAA) method (Ruszczynski and Shapiro 2003). Initially, we plug the expectations of $\varepsilon _ { i }$ and $\varepsilon _ { c }$ in P4, obtained by taking means of respective distributions from the survey data. We then generate M random samples of $\varepsilon _ { a }$ according to its empirical distribution obtained from the data. The expectation in (44) is substituted by its sample average approximation. Phase 1 and all the Phase 2 problems (one for each instance out of M samples of $\varepsilon _ { a } )$ are combined as one single stochastic problem. This entails adding constraints (52)-(54) for each instance of the sample set to P4 (for a total of M instances), and replacing the last term in (44) with the sample average approximation, where $\sum _ { t \in T } c _ { t } ^ { l } \left( r _ { t } ^ { d } - r _ { t \xi } ^ { e } \right) t ^ { a }$ is added to the approximation expression, once each for the M instances (see box 3 of Figure 2). This extensive formulation is solved using a solver.

## Risk Assessment

To calibrate as well as assess the usefulness of our models, we estimated breach probabilities as a function of security control expenses using a survey and cost data for a representative IT infrastructure in Figure 3. This configuration was determined by a focus group of five IT security professionals, as being representative of a small to medium enterprise (SME) IT infrastructure for e-comm on the focus group can be found in the appendix. The IT infrastructure consists of the following: 1) a web server farm containing two web servers (1, 2), 2) an application server farm containing two application servers (3, 4), and 3) a database farm consisting of two database servers (5, 6). Client machines on the internet initiate transactions that are sent to the web server farm. Based on load-balancing considerations, a transaction is routed to an appropriate web server in the farm. For illustration purposes, there are two transaction types as follows: 1) Type 1: This transaction is captured by a client and sent to any of the two web servers, where it is processed, and the results sent back to the client; 2) Type 2: This transaction captured by a client machine, is sent to any of the two web servers, where the transaction spawns a subtransaction that is sent to one of the two application servers, where one database query is generated and sent to one of the database servers. The query result is then sent back from a database server to the application server, where additional business logic is executed and the result then sent to the web server, where further processing takes place, before results are sent back to the client. The two transaction flows are also illustrated in Figure 3, where A, B, C, D, and E are placeholders for security controls. The following network-level (i.e., general) controls were identified by the focus group and used in various feasible combinations (see Table 3) in the survey: network firewall, network ACL, HSRP, application gateway, and IDS/IPS. The host-level controls used in various feasible combinations in the survey were: host firewall and SSL. A survey instrument was sent to security professionals in our network for our

representative IT infrastructure. As per our request, the Information Systems Security Certification Consortium (ISC<sup>2</sup>), the organization that administers the CISSP certification also mailed the survey to current holders of the CISSP certification. Survey respondents estimated breach probabilities for various combination of controls that were placed at placeholders A, B, C, D, and E in the example configuration shown in Figure 3.

Figure 3: Example configuration  
![](/api/attachments/VK2E82CQ/fulltext/images/7e50ab00a7c90d70e935e6ed3d81eee930370e2e8c7c391a195e0407f4c14008.jpg)  
The following definition was included related to breach probability in the survey.

“Breach Probability: Proportion of attack incidences directed towards a host that are successful in causing a breach on that host. There are three breach probabilities- probability of confidentiality breach, probability of integrity breach and probability of availability breach. All breach probabilities are expressed as percentages.”

The definitions of confidentiality, integrity and available as stated in Section 2.1 were included in the survey. A total of 49 survey responses were obtained. The mean IT experience of the respondents was over 18 years, of which over 11 years were in information security, thereby indicating a high quality of the subject pool. For all feasible security control settings, security control expenses denoted by “expense” were estimated as described in the appendix and shown in Table 3. The average breach probabilities across all subjects for each control setting are also shown in Table 3.

Table 3: Average breach probabilities and control expenses

<table><tr><td>ID</td><td>Control Combination</td><td>Expense</td><td>Average Breach Probability Confidentiality (%)</td><td>Average Breach Probability Integrity (%)</td><td>Average Breach Probability Availability (%)</td></tr><tr><td>1</td><td>Network firewall + Host firewall</td><td>$21,314.00</td><td>33.92</td><td>32.66</td><td>32.9</td></tr><tr><td>2</td><td>Network firewall + Application gateway</td><td>$24,116.64</td><td>29.56</td><td>27.28</td><td>26.55</td></tr><tr><td>3</td><td>Network firewall + Secure Sockets Layer (SSL)</td><td>$16,086.73</td><td>31.63</td><td>31.92</td><td>32.39</td></tr><tr><td>4</td><td>Host firewalls + SSL</td><td>$10,514.33</td><td>35.24</td><td>36</td><td>36.37</td></tr><tr><td>5</td><td>Network Access Control List (ACL) + SSL</td><td>$6,779.71</td><td>38.54</td><td>40.35</td><td>39.92</td></tr><tr><td>6</td><td>Hot Standby Router Protocol (HSRP) + SSL</td><td>$11,692.77</td><td>51.97</td><td>49.34</td><td>48.76</td></tr><tr><td>7</td><td>Application Gateway + SSL</td><td>$13,316.97</td><td>36.97</td><td>37.53</td><td>37.76</td></tr><tr><td>8</td><td>Intrusion Detection System (IDS)/ Intrusion Prevention System(IPS) + SSL</td><td>$22,922.77</td><td>34.45</td><td>34.21</td><td>34.29</td></tr><tr><td>9</td><td>Network firewall + Host firewall + Network ACL</td><td>$25,450.18</td><td>27.21</td><td>24.16</td><td>24.32</td></tr><tr><td>10</td><td>Network firewall + Host firewall + Network ACL + HSRP</td><td>$34,499.42</td><td>22.08</td><td>18.55</td><td>17.84</td></tr><tr><td>11</td><td>Network firewall + Host firewall + Application gateway + Network ACL + HSRP + IDS/ IPS</td><td>$65,452.10</td><td>16.47</td><td>11.21</td><td>11.89</td></tr><tr><td>12</td><td>Network firewall + Host firewall + Application gateway + Network ACL +HSRP + IDS/ IPS + SSL</td><td>$68,095.63</td><td>9.29</td><td>8.63</td><td>10.95</td></tr></table>

The summary statistics of the data collected are provided in Table 4.

Table 4: Summary Statistics

<table><tr><td></td><td>N</td><td>Mean</td><td>SD</td></tr><tr><td>Log(price)</td><td>588</td><td>9.93</td><td>0.68</td></tr><tr><td>Log(confidentiality)</td><td>575</td><td>2.96</td><td>1.19</td></tr><tr><td>Log(integrity)</td><td>577</td><td>2.88</td><td>1.29</td></tr><tr><td>Log(availability)</td><td>565</td><td>2.97</td><td>1.2</td></tr></table>

Figure 4: Average and estimated confidentiality, integrity and availability breach probabilities

![](/api/attachments/VK2E82CQ/fulltext/images/e43d13a717c8928c6c827a57652032c7ae8dfbfb6a6b4ec8d62038cb15e310ae.jpg)  
a

![](/api/attachments/VK2E82CQ/fulltext/images/2b269da780877c89d958135584ca36d49b12e40e6dc4f1d818effb71dc7b1b3b.jpg)  
b

![](/api/attachments/VK2E82CQ/fulltext/images/654b1c42d5aed8b7274044c698f59c68977b02ffa3c015f955f716a8875ea5f1.jpg)  
c  
We estimated a convex piecewise linear form for breach probabilities as a function of control expenses as given by (8), (9) and (10). The number of segments used for the three cases was 2, i.e., $k _ { c } = k _ { i } = k _ { a } = 2$ based on the visual inspection of data. The coefficients were then estimated by using standard least square methods. The estimates are given as:

$$
\alpha_ {c, 1} = - 0. 7 0 1 9, \beta_ {c, 1} = 4 8. 4 3 9 2, \alpha_ {c, 2} = - 0. 2 6 3 8, \beta_ {c, 2} = 3 4. 7 1 8 9
$$

$$
\alpha_ {i, 1} = - 0. 8 0 4 9, \beta_ {i, 1} = 4 9. 8 9 4 5, \alpha_ {i, 2} = - 0. 2 6 4 5, \beta_ {i, 2} = 3 2. 5 6 3 4
$$

$$
\alpha_ {a, 1} = - 0. 7 5 7 5, \beta_ {a, 1} = 4 9. 0 7 2 4, \alpha_ {a, 2} = - 0. 1 6 5 6, \beta_ {a, 2} = 2 7. 6 9 7 6
$$

# ACCEPTED MANUSCRIPT

Plots of average breach probabilities of survey data and estimated breach probabilities from the quadratic functions are shown in Figure 4.

## 3. Computational Experiments

The representative example presented in Figure 3 was used as the context for the computational experiments. The overarching goal of the computational experiments was to demonstrate the utility of our optimization models. We executed the two models for the base case given by the following parameter values: T = {1, 2}; F = {1 (web server), 2 (application server), 3 (database server)}; $F _ { 1 } = \{ 1 , 2 \} , F _ { 2 } = \{ 1$ 2, 3}; $N _ { 1 } = \{ 1 , 2 \} , N _ { 2 } = \{ 3 , 4 \} , N _ { 3 } = \{ 5 , 6 \} ; \pi _ { 1 1 } = 1 ; \pi _ { 1 2 } = 1 , \pi _ { 1 3 } = 0 , \pi _ { 2 1 } = 1 , \pi _ { 2 2 } = 1 , \pi _ { 2 3 } = 1 ; t ^ { a } = 2 0 ; \mathbb { G } = 0 ,$ {1 (no control), 2 (network firewall), 3 (network ACL), 4 (HSRP), 5 (application gateway), 6 (IDS/IPS), 7 (network firewall + application gateway), 8 (network firewall +network ACL), 9 (network firewall +network ACL+HSRP), 10 (network firewall +network ACL+HSRP+ application gateway+ IDS/IPS) }; S = {1 (no control), 2 (host firewall), 3 (SSL), 4 (host firewall + SSL)}; $c _ { t } ^ { l } = 1 0 0$ t ; $c ^ { g } { } _ { 1 } = 0 ; c ^ { g } { } _ { 2 } =$ 13443.20, $c ^ { g } { } _ { 3 } = 4 1 3 6 . 1$ 8; $c ^ { g } { } _ { 4 } = 9 0 4 9 . 2 4 $ ; c<sup>g</sup><sub>5</sub> = 10673.4; $c ^ { g } { } _ { 6 } = 2 0 2 7 9 . 2 4$ ; c<sup>g</sup><sub>7</sub> = 24116.64; c<sup>g</sup><sub>8</sub> = 17579.38; $c ^ { g } { } _ { 9 } = 2 6 6 2 8 . 5 2$ ; c<sup>g</sup><sub>10</sub> = 57581.3; c<sup>s</sup><sub>p1</sub> = 0, c<sup>s</sup><sub>p2</sub> = 7870.80, $c _ { p 3 } ^ { s } = 2 6 4 3 . 5 3$ $c _ { p 4 } ^ { s } = 1 0 5 1 4 . 3 3$ p ; $l _ { p } ^ { i } { = } l _ { p } ^ { c } =$ 415000 p ; $Q _ { p } = 3 0 \ \forall p ; \ r _ { t } ^ { d } = 3 0$ t ; The average annual losses due to security breaches of \$415,000 was used as reported in a recent study (PwC 2014). The various costs related to control settings were determined as outlined in the appendix.

The capacities of the three farms were as follows:

$\boldsymbol { Q } _ { 1 } ^ { f }$ (webserver farm) = Q<sub>1</sub> + Q<sub>2</sub> = 60 transactions/minute

$\boldsymbol { Q } _ { 2 } ^ { f }$ (application server farm) = $Q _ { 3 } + Q _ { 4 } = 6 0$ transactions/minute

$\boldsymbol { Q } _ { 3 } ^ { f }$ (database farm) $= Q _ { 5 } + Q _ { 6 } = 6 0$ transactions/minute

The function $g _ { f } ( [ \nu _ { p } ^ { a } ] _ { p \in N f } , [ Q _ { p } ] _ { p \in N f } )$ for computing the expected transaction rate was computed as follows. For the database server farm, the following four states were possible for the two servers: (F, O), (O, F), (F, F), (O, O), where F is fail and O is OK state. The expected capacity of the webserver farm, which is dependent on the control assignments was given by $g _ { f } ( [ \nu ^ { a } { } _ { p } ] _ { p \in N f } , [ Q _ { p } ] _ { { } _ { p \in N f } } ) = { } \nu ^ { a } { } _ { 1 } { } ^ { * } ( I - \nu ^ { a } { } _ { 2 } ) ^ { * } Q _ { 2 } +$ $( 1 - \nu ^ { a } { } _ { 1 } ) ^ { * } \nu ^ { a } { } _ { 2 } { } ^ { * } Q _ { 1 } + \nu ^ { a } { } _ { 1 } { } ^ { * } \nu ^ { a } { } _ { 2 } { } ^ { * } 0 + ( 1 - \nu ^ { a } { } _ { 1 } ) ^ { * } ( 1 - \nu ^ { a } { } _ { 2 } ) ^ { * } ( Q _ { 1 } + Q _ { 2 } )$ , where $\nu _ { \mathrm { ~ 1 ~ } } ^ { a }$ and $\nu _ { \mathrm { ~ 2 ~ } } ^ { a }$ were the availability breach probabilities of the two webservers. It can be easily verified that $q ( Q _ { p } ) = Q _ { p }$ and $\gamma = \sum _ { p \in N _ { f } } Q _ { p }$ . Therefore

$$
g _ {f} ([ v _ {p} ^ {a} ] _ {p \in N f}, [ Q _ {p} ] _ {p \in N f}) = - \sum_ {p \in N _ {f}} Q _ {p} v _ {p} ^ {a} + \sum_ {p \in N _ {f}} Q _ {p}.
$$

The following equations were applied to the survey data in estimating the distribution of multiplicative errors $\mathcal { E } _ { c } , \mathcal { E } _ { i } ,$ and $\varepsilon _ { a \cdot }$

$$
\ln \left(v _ {p} ^ {c}\right) = \ln \left(\max _ {m = 1, \dots , k c} \left\{\alpha_ {c, m} \exp_ {p} + \beta_ {c, m} \right\}\right) + \ln \left(\varepsilon_ {c}\right)\tag{55}
$$

$$
l n (v _ {p} ^ {i}) = l n (\max _ {m = 1, \dots , k i} \{\alpha_ {i, m} \exp_ {p} + \beta_ {i, m} \}) + l n (\varepsilon_ {i})\tag{56}
$$

$$
\ln \left(v _ {p} ^ {a}\right) = \ln \left(\max _ {m = 1, \dots , k a} \left\{\alpha_ {a, m} \exp_ {p} + \beta_ {a, m} \right\}\right) + \ln \left(\varepsilon_ {a}\right)\tag{57}
$$

The normal Q-Q plots of $l n ( \varepsilon _ { c } )$ , ln(ε<sub>i</sub>), and $l n ( \varepsilon _ { a } )$ are shown in figures 5a-c.

Figure 5: Normal Q-Q Plots for $l n ( \varepsilon _ { c } ) , l n ( \varepsilon _ { i } ) , l n ( \varepsilon _ { a } )$  
![](/api/attachments/VK2E82CQ/fulltext/images/506893e7c6a49e7da8f900deecab99bf49a1f581b57bedef0b713dbc0a7e5527.jpg)  
a

![](/api/attachments/VK2E82CQ/fulltext/images/0fc50784380f95a9700a1c2ee8a81b5230a7c7ae4a479815b180557dfa61c198.jpg)  
b

![](/api/attachments/VK2E82CQ/fulltext/images/825980ccca18573b7c475d5ceeda9348053aeb95af6fc8930a4486dc585ac937.jpg)  
c  
We examined the Q-Q plots to evaluate the distribution and approximated the distributions of ln(ε<sub>c</sub>), $l n ( \varepsilon _ { i } ) .$ , and $l n ( \varepsilon _ { a } ) \mathrm { ~ a s ~ } l n ( \varepsilon _ { c } ) \sim N ( - 0 . 4 8 6 9 , 1 . 1 0 7 2 ^ { 2 } ) , l n ( \varepsilon _ { i } ) \sim N ( - 0 . 5 2 1 0 , 1 . 1 8 8 0 ^ { 2 } ) , l n ( \varepsilon _ { a } ) \sim - 0 . 4 5 0 7 , 1 . 1 1 1 6 ^ { 2 }$

Therefore, we had $\mathrm { E } \left[ \mathcal { E } _ { c } \right] = 1 . 1 3 4 2$ and $\operatorname { E } \left[ \mathcal { E } _ { i } \right] = 1 . 2 0 2 8$ . We used $l n ( \varepsilon _ { a } ) \sim \mathrm { N } ( - 0 . 4 5 0 7 , 1 . 1 1 1 6 ^ { 2 } )$ and a sample size of 100 for the phase 2 problem.

The models were solved using CPLEX. The optimal solution for the deterministic problem P2 was: $y _ { 1 }$ $= . . . = y _ { 9 } = 0 , y _ { 1 0 } = 1 , z _ { p 1 } = z _ { p 2 } = z _ { p 3 } = 0 , z _ { p 4 } = 1 \ \forall \ p _ { \in } N ,$ with expected transaction rates $r ^ { e } _ { 1 } = 3 0$ and $r _ { 2 } ^ { e } =$ 20.1474. The solution translated to the following configuration:

Location A: Network ACL + HSRP

Location B: Network firewall + Application gateway + IDS/IPS

Location C (On each host): Host firewall + SSL

Location D (On each host): Host firewall + SSL

Location E: (On each host): Host firewall + SSL

For the stochastic problem P4, with a sample size of 100, the optimal solution was: $y _ { 1 } = \ldots = y _ { 9 } = 0 , $ , y<sub>10</sub> $\begin{array} { r l } { } & { { } = 1 , z _ { p 1 } = z _ { p 2 } = z _ { p 3 } = 0 , z _ { p 4 } = 1 \ \forall \ p _ { \in } N . } \end{array}$ For each sample $\xi ,$ the corresponding expected transaction rates were $r _ { 1 \xi } ^ { e }$ and $r _ { 2 \xi } ^ { e } .$ The empirical distributions of random variables $r _ { 1 \xi } ^ { e }$ and $r _ { 2 \xi } ^ { e }$ are shown in Figure 6.

Figure 6: Empirical distributions of $r _ { 1 } ^ { e }$ and $r _ { 2 } ^ { e }$

![](/api/attachments/VK2E82CQ/fulltext/images/c24a02d73cb01d05b98dc62ad2e61d521422ae2a4982a475edac76f35d3de227.jpg)

![](/api/attachments/VK2E82CQ/fulltext/images/b1e858cddde4911640fcafdd32b8a65d039f3cc653953dd6568706a9d5deee35.jpg)

For the base case as represented by parameter values described above, both the deterministic model and the stochastic model generated the same security controls configuration. For the deterministic case, the expected transaction rate was: $r _ { 1 } ^ { e } = 3 0 , r _ { 2 } ^ { \ e } = 2 0 . 1 4 7 4$ . However, when there were errors in breach probability estimations, the expected transaction rates followed long-tail distributions, which implied that the actual transaction rates that could be realized had much lower values, i.e., as low as 11 for $r ^ { e } { } _ { I }$ . It implied that errors in breach probabilities had significant impact on both the expected loss and transaction rates.

We then performed additional computational experiments to test the robustness of the two models. Results obtained by varying average loss amount due to integrity and confidentiality breach incidents $( l _ { p } ^ { i }$ and $l _ { \textsc { p } } ^ { c }$ , while keeping all parameters the same as in the base case (including loss due to availability) for the deterministic as well as stochastic models are shown in Table 5. It can be seen that when the loss from integrity and confidentiality security breaches was low, the optimal policy was not to invest in any security controls in the case of the deterministic model. However, because of availability breaches that could lead to transaction rates as low as 11 (Figure 6), the stochastic model assigned security controls when integrity and confidentiality losses were low. At the other extreme, when the loss from security breaches was very high, then the optimal policy was to fully protect the IT infrastructure with all available controls. We also report the Loss Avoidance Percentage (see Table 5). This is given by (Unprotected Cost – Optimal Cost Protected)/Unprotected Cost, expressed as a percentage. For the deterministic case, the Optimal Cost Protected is given by the optimal value of (20), while for the stochastic case, the Optimal Cost Protected is given by the optimal value of (44). The Unprotected Cost is the total cost when no controls are assigned. Table 5 shows that the level of protection increases as the average loss amounts for confidentiality and integrity breaches increase, causing the Loss Avoidance Percentage to increase. This suggests that greater benefits are derived with increased protection, as costs from breaches increase.

# ACCEPTED MANUSCRIPT

To verify the robustness of the stochastic approach to noise, we used 110%, 120%, 130%, 140%, 150% of the standard deviation of the log-normal distribution described in (32) to check for the effects of noise in the probability estimations. For all five values, the optimal control configurations do not change across all the loss values $( l _ { p } ^ { c } , l _ { p } ^ { i } )$ in Table 5.

Table 5: Sensitivity Analysis for both the Deterministic and Stochastic Model

<table><tr><td>Average confidentiality and integrity breach loss amounts ( $l^c_p$ ,  $l^i_p$ )</td><td>Optimal Control Configuration (Deterministic)</td><td>Optimal Control Configuration (Stochastic)</td><td>Annual Optimal Security Expense($) (Deterministic)</td><td>Annual Optimal Security Expense ($) (Stochastic)</td><td>Loss Avoidance Percentage (Deterministic)</td><td>Loss Avoidance Percentage (Stochastic)</td></tr><tr><td>(100, 100)</td><td>General Controls: NoneAt every host: None( $y_1 = 1$ ,  $y_2 = \cdots = y_{10} = 0$ ,  $z_{p1} = 1$ , $z_{p2} = z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>General Controls: Network firewall +Network ACL+HSRPAt every host: None( $y_1 = \cdots = y_8 = 0$ ,  $y_9 = 1$ ,  $y_{10} = 0$ ,  $z_{p1} = 1$ ,  $z_{p2} = z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>$0</td><td>$26,628.52</td><td>0%</td><td>0.95%</td></tr><tr><td>(1000, 1000)</td><td>General Controls: NoneAt every host: None( $y_1 = 1$ ,  $y_2 = \cdots = y_{10} = 0$ ,  $z_{p1} = 1$ ,  $z_{p2} = z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>General Controls: Network firewall +Network ACL+HSRPAt every host: None( $y_1 = \cdots = y_8 = 0$ ,  $y_9 = 1$ ,  $y_{10} = 0$ ,  $z_{p1} = 1$ ,  $z_{p2}= z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>$0</td><td>$26,628.52</td><td>0%</td><td>4.36%</td></tr><tr><td>(10000, 10000)</td><td>General Controls: Network firewall +Network ACL+HSRPAt every host: None $y_1 = \cdots y_8 = 0$ ,  $y_9 = 1$ ,  $y_{10} = 0$ ,  $z_{p1} = 1$ ,  $z_{p2} = z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>General Controls: Network firewall +Network ACL+HSRPAt every host: None $y_1 = \cdots y_8 = 0$ ,  $y_9 = 1$ ,  $y_{10} = 0$ ,  $z_{p1} = 1$ ,  $z_{p2} = z_{p3} = z_{p4} = 0$ ,  $\forall p$ )</td><td>$26,628.52</td><td>$26,628.52</td><td>18.33%</td><td>21.16%</td></tr><tr><td>(50000, 50000)</td><td>General Controls: Network firewall +Network ACL+HSRP+ Application gateway+ IDS/IPSAt every host: None $(y_1 = \cdots y_9 = 0,y_{10} = 1, z_{p1} = 1,z_{p2} = z_{p3} = z_{p4} = 0,\forall p)$ </td><td>General Controls: Network firewall +Network ACL+HSRP+ Application gateway+ IDS/IPSAt every host: None $(y_1 = \cdots y_9 = 0,y_{10} = 1, z_{p1} = 1,z_{p2} = z_{p3} = z_{p4} = 0,\forall p)$ </td><td>$57,581.30</td><td>$57,581.30</td><td>46.50%</td><td>48.80%</td></tr><tr><td>(100000,100000)</td><td>General Controls:Network firewall+NetworkACL+HSRP+Application gateway+IDS/IPSAt every host: None $(y_1 = \cdots = y_9 = 0,y_{10} = 1, z_{p1} = 1,z_{p2} = z_{p3} = z_{p4} = 0,\forall p)$ </td><td>General Controls:Network firewall+Network ACL+HSRP+Application gateway+IDS/IPSAt every host: None $(y_1 = \cdots = y_9 = 0,y_{10} = 1, z_{p1} = 1,z_{p2} = z_{p3} = z_{p4} = 0,\forall p)$ </td><td>$57,581.30</td><td>$57,581.30</td><td>53.85%</td><td>55.16%</td></tr><tr><td>(415000,415000)</td><td>General Controls:Network firewall+NetworkACL+HSRP+Application gateway+IDS/IPSAt every host: Hostfirewall + SSL $(y_1 = \cdots = y_9 = 0,y_{10} = 1, , , z_{p1} =z_{p2} = z_{p3} = 0,z_{p4} = 1 \forall p)$ </td><td>General Controls:Network firewall+Network ACL+HSRP+Application gateway+IDS/IPSAt every host: Hostfirewall + SSL $(y_1 = \cdots = y_9 = 0,y_{10} = 1, , , z_{p1} = z_{p2} =z_{p3} = 0, z_{p4} = 1 \forall p)$ </td><td>$120,667.28</td><td>$120,667.28</td><td>63.45%</td><td>64.22%</td></tr><tr><td>(500000,500000)</td><td>General Controls:Network firewall+NetworkACL+HSRP+Application gateway+IDS/IPSAt every host: Hostfirewall + SSL $(y_1 = \cdots = y_9 = 0,y_{10} = 1, , , z_{p1} =z_{p2} = z_{p3} = 0,z_{p4} = 1 \forall p)$ </td><td>General Controls:Network firewall +Network ACL+HSRP+Application gateway+IDS/IPSAt every host: Hostfirewall + SSL $(y_1 = \cdots = y_9 = 0,y_{10} = 1, , , z_{p1} = z_{p2} =z_{p3} = 0, z_{p4} = 1 \forall p)$ </td><td>$120,667.28</td><td>$12O,667.28</td><td>64.26%</td><td>64.91%</td></tr></table>

With regards to the run-time performance of our approach, the CPU time taken to solve a deterministic model instance was 0.0468s, while the CPU time taken to solve a stochastic model instance was 0.9048s on a machine with the following specs: Intel(R) Core(TM) i7-3770 CPU @3.40GHz. We also solved larger problem instances. For a problem with 6 farms and 4 servers per farm, leading to 24 servers, and with 6 different transaction types, the CPU times on the same computation platform for deterministic model instances ranged from 0.0156s to 0.608s, and from 0.0377s to 1.3884s for the stochastic model. This demonstrates the utility of our approach in solving larger problems.

## 5. DSS Architecture

The DSS envisioned to support security planning is a tool that hides all the complexities of the optimization models that form the inner core of the DSS, while providing a user-friendly graphical user interface to enable non-technical users to easily interact with the system. The DSS is also envisioned to be a self-contained system that provides all the necessary functionality to support activities during the entire life-cycle of models such as model data collection, model instance creation, model execution, model solution, and model maintenance (Krishnan and Chari 2000). A high level logical architecture of the DSS for security planning is shown in Figure 7.

The various components of the DSS are as follows:

Controls Library: This a repository of various security controls such as specific firewall components, various security software versions, router models, etc. Breach probabilities as well as costs associated with various controls are captured in the controls library. Since the blocking probabilities of controls are not additive due to overlapping coverages of controls, preconfigured control compositions representing various security settings are also stored along with their aggregate breach probabilities. The controls library could be accessed by a graphical user interface that enables users to treat controls as well as control compositions as high level objects that have properties.

IT Components Library: This is a repository of various common IT hardware and software platforms such as Windows 8 workstation, specific network switch models etc. Using the various components from this library, a user could configure the IT infrastructure in the DSS that mirrors the actual setup that the user is trying to protect.

## ACCEPTED MANUSCRIPT

![](/api/attachments/VK2E82CQ/fulltext/images/abf2e1d5f06bf91c6069936ffd3c22d7394d7592e8dd950d733f1c1ef952baeb.jpg)  
Figure 7: Logical Architecture of DSS

Graphical Editor: This component allows users to build an IT infrastructure by dropping and interconnecting component objects in a canvas. Component objects are drawn from the controls library and the IT components library. The editor can implement various composition rules to ensure that the IT infrastructure composed is valid. Research is available in the literature on building optimization models using graphical objects (Chari and Sen 1997; Jones 1990).

User Interface: The user interface supports all the interactions between a user and the system during the various phases of the model life cycle. The various tasks supported include inputting controls and other IT components related data to the libraries, supporting user interactions with the graphical editor to create a model instance, invoking a solver to execute a model instance, supporting user interactions to conduct sensitivity analysis of model solutions, and providing support for model instance revision or update. The user interface is graphical with drag and drop capabilities to enable users to compose an IT infrastructure graphically.

Model Generator: This component takes the IT infrastructure configuration and coverts it into a nonlinear integer programming model instance in a format that can be executed by a solver such as CPLEX, LINGO, etc. An example of a model generator converting graphical models into solver executable model representation can be found in (Chari and Sen 1998).

Solver: A solver such as CPLEX or LINGO generates an optimal allocation of controls by solving the model presented by the model generator.

## 6. Conclusions

We presented generalizable models for incorporating survey estimates on probabilities in determining optimal allocations for security controls to protect an information systems infrastructure. Our models are very general and can be customized for any specific IT environment, and to our knowledge, are the only models available in the information security risk literature that integrate risks associated with availability, confidentiality and integrity in allocating controls. Our first model, a deterministic optimization model for control selection can be applied when accurate estimates of breach probabilities are available. However, since, security breach data is not easily available, breach probabilities are often estimated via surveys, which could lead to estimation errors. To identify optimal allocations in the presence of these errors, we use a stochastic optimization model that handles uncertainties in breach probability estimations. To our knowledge, this is a key contribution to the literature.

To test our models, we collected security breach probability data estimates from a survey of IT/security professionals, and then using a least square error minimizing approach, determined piecewise linear functions that captured the relationships between security breach probabilities and security expenses. It should be noted that there are very few models available in the literature for control assignment that are grounded in real world data. This research attempted to overcome this limitation in the field by gathering empirical data from security experts for assessing risks.

We performed computational experiments to demonstrate the robustness of our deterministic as well as stochastic models. As the average loss amount of security breaches decreased, the optimal security expenses also decreased. Finally, we presented a high level architecture for a DSS tool for security planning. This architecture enables the DSS to be used by non-technical users for security planning.

For the future, this research can be extended in many directions. First, a more granular model could be developed to capture differences in transaction times and differential loss values within each breach category. Second, efforts could be made in developing approaches that combine surveys and publicly available archival data to estimate breach probabilities with a high degree of accuracy. Third, efforts could be undertaken to build a prototype for decision support system for security planning based on the proposed architecture.

## 7. References

Arora, A., Hall, D., Pinto, C. A., Ramsey, D., and Telang, R. 2004 "Measuring the Risk-Based Value of IT Security Solutions " IEEE IT Professional (6:6), pp 35-42.

Bertsimas, D., and Tsitsiklis, J. N. 1997 Introduction to Linear Optimization Athena Scientific.

Blinder, A., and Perlroth, N. 2018 "A cyberattack hobbles Atlanta, and security experts shudder," in: New York Times.https://www.nytimes.com/2018/03/27/us/cyberattackatlanta-ransomware.html

BLS 2015 "Occupational outlook handbook: Network and computer system administrators."http://www.bls.gov/ooh/Computer-and-Information-Technology/Network-and-computer-systems-administrators.htm

Bossert, T. P. 2017 "It’s Official: North Korea Is Behind WannaCry," in: Wall Street Journal, Dow Jones, New York.https://www.wsj.com/articles/its-official-north-korea-is-behindwannacry-1513642537 (accessed August 2018)

Cavusoglu, H., Mishra, B., and Raghunathan, S. 2005 "The value of intrusion detection systems in information technology security architecture," Information Systems Research (16:1), pp 28-46.

Chari, K., and Sen, T. K. 1997 "An Integrated Modeling System for Structured Modeling Using Model Graphs," INFORMS Journal on Computing (9:4), pp 397-416.

Chari, K., and Sen, T. K. 1998 "An Implementation of a Graph-Based Modeling System for Structured Modeling (GBMS/SM)," Decision Support Systems (22:2), pp 103-120.

Clements, N. 2018 "Equifax's Enormous Data Breach Just Got Even Bigger," in: Forbes.https://www.forbes.com/sites/nickclements/2018/03/05/equifaxs-enormous-databreach-just-got-even-bigger/#5a1c6c9253bc

too."http://money.cnn.com/2014/11/06/technology/security/home-depot-breach-emails NIST 2008 "National Vulnerability Database."http://nvd.nist.gov/

## ACCEPTED MANUSCRIPT

Conrad, J. R. 2005 "Analyzing the risks of information security investments with Monte-Carlo simulations.," in: Fourth Workshop on Economics of Information Security, Boston, MA, p. 5

El-Gayar, O. F., and Fritz, B. D. 2010 "A web-based multi-perspective decision support system for information security planning," Decision Support Systems (50:1), pp 43-54.

Gartner Research "Gartner Says Worldwide Information Security Spending Will Grow 7 Percent to Reach \$86.4 Billion in 2017."https://www.gartner.com/newsroom/id/3784965

Goldstein, M., Perlroth, N., and Corkery, M. 2014 "Neglected Server Provided Entry for JPMorgan Hackers," in: New York Times

Gordon, L. A., and Loeb, M. P. 2002 "The economics of information security investment," ACM Transactions on Information and System Security (5:4), pp 438-457.

Highleyman, B., Holenstein, P. J., and Holenstein, B. 2003 Breaking the Availability Barrier: Survivable Systems for Enterprise Computing 1 Books Library.

Isaac, M., and Frenkel, S. 2018 "Facebook secuirty breach exposes accounts of 50 million users," in: The New York Times

Jones, C. V. 1990 "An introduction to graph based modeling systems: Part I. Overview," ORSA (2:2), pp 136-151.

Krishnan, R., and Chari, K. 2000 "Model management: survey, future research directions and a bibliography," The Interactive Transactions of OR/MS (3:1).

Krueger, R. A., and Casey, M. A. 2008 Focus Groups: A Practical Guide for Applied Research Sage publications.

Kumar, R. L., Park, S., and Subramaniam, C. 2008 "Understanding the Value of Countermeasure Portfolios in Information Systems Security," Journal of Management Information Systems (25:2), pp 241-279.

PwC "State of Cybercrime,"

PwC "State of Cybercrime."http://www.pwc.com/us/en/increasing-iteffectiveness/publications/assets/2015-us-cybercrime-survey.pdf

Rakes, T. R., Deane, J. K., and Rees, L. P. 2012 "IT security planning under uncertainity for high-impact events," Omega (40), pp 79-88.

Rappeport, A. 2017 "Up to 100,000 Taxpayers Compromised in Fafsa Tool Breach, I.R.S. Says," in: New York Timees

Rees, L. P., Deane J.K., Rakes, T.R. and Baker W.H. 2011 "Decision support for cybersecurity risk planning," Decision Support Systems (51:3), pp 493-505.

Ruszczynski, A., and Shapiro, A. 2003 (ed.)^(eds.) Stochastic Programming. Handbooks in Operations Research and Management Science, North-Holland, Amsterdam.

Sawik, T. 2013 "Selection of optimal countermeasure portfolio in IT security planning," Decision Support Systems (55:1), pp 156-164.

Sharf, S. 2014 "Target shares tumble as retailer reveals cost of data breach," in: Forbes U.S. Code 2000 "U.S. Code," in: 44.http://www.gpoaccess.gov/uscode/

Wang, J., Chaudhury, A., and Rao, H. R. 2008 "A value-at-risk approach to information security investment," Information Systems Research (19:1), pp 106-120.

## Yahoo "Yahoo security

notice."https://help.yahoo.com/kb/account/SLN27925.html?impressions=true

Yang, J. L., and Jayakumar, A. 2014 "Target says up to 70 million more customers were hit by December data breach," in: The Washington Post

Yeo, M. L., Rolland, E., Ulmer, J. R., and Patterson, R. A. 2014 "Risk mitigation decisions for IT security," ACM Transactions on Management Information Systems (5:1), pp 1-21.

Yue, W. T., Cakanyildirim, M., Ryu, Y. U., and Liu, D. 2007 "Network externalities, layered protection and IT security risk management," Decision Support Systems (44), pp 1-16.

## Appendix: Cost and Probability Estimates

We used a focus group to develop the reference configuration as well as identify controls for this research. We then used a survey of industry professionals to obtain estimates of breach probabilities.

## Focus Group

We followed the procedure recommended by Krueger et al. (2008) to conduct our focus group. Leadership contacts in the local offices of 7-8 large organizations ith over 1,000 employees, were requested to nominate a senior member of their IT security team to participate in the focus group. Five members participated in the focus group. Participants had self-rated work experience of 15 – 30 years, of which 9 – 15 years were in IT security. All but one focus group participant had the CISSP certification, and all participants had some information security related credentials. Participants represented finance, telecom, consulting and higher education sectors. The focus group lasted over 3 hours.

A script was followed during the focus group. To initiate the discussion, participants listed the most important threats facing their respective organizations. The participants then architected a representative web application that could be used for the research, and identified the important controls for protecting it. The concept of common controls emerged during the discussion of security controls. Common controls were items such as training and patch management that affect all controls. In our survey, these were labeled as security best practices and respondents reported whether or not each of the best practices were assumed to be implemented. Finally, the focus group participants discussed a representative configuration including specific model numbers, for each security control identified by them.

Subsequent to the focus group, we obtained the price information for each security control from the vendor price lists for our academic institution. Annualized costs were obtained by adding hardware costs and annual maintenance costs. To obtain expected equipment lifetimes and annual personnel costs associated with hardware maintenance, we polled the focus group members a few days after the focus group meeting. Hardware costs were depreciated linearly over their expected lifetime to obtain estimates of annualized hardware costs for each control.

Maintenance costs were composed of personnel costs and hardware maintenance agreement costs. Hardware maintenance agreements were a fixed 5% for all state institutions in our state and we used this statistic as our estimate of annual hardware maintenance costs. To obtain estimates of personnel costs associated with maintenance, we polled the focus group membe or maintenance effort estimates associated with each control. Personnel salaries were obtained from the Bureau of Labor Statistics (BLS 2015). Multiplying salaries with mean estimates of annual efforts gave us the annual personnel costs associated with maintenance. These cost estimates have been included in our model.

## Survey

Once the reference architecture and controls were identified by the focus group of experts, estimates of breach probabilities in the presence of different controls were obtained from a survey of industry professionals. These surveys were completed using two methods. We attended industry conferences within our local area and solicited responses from attendees. We also requested $\mathrm { I S C } ^ { 2 }$ to mail the survey to the current holders of the CISSP certification. Through these efforts, 49 survey responses were obtained. We believe the low response rate is due to the length of the survey (approximately 30 minutes to complete). However, the responses were of high quality. The mean IT experience of the respondents was over 18 years, of which over 11 were in information security.

![](/api/attachments/VK2E82CQ/fulltext/images/61263a44f7e3cfb62de05b5381469c6cd7a85d3c7d51400cce6d960caa1e221e.jpg)  
Programming.

He Zhang is an assistant professor in the Information Systems and Decision Sciences department in the Muma College of Business at the University of South Florida. His research interests include healthcare information management, Big Data, and production and inventory management. Zhang’s research has been published in journals including Mathematical Programming and he has presented his research at the International Conference on Stochastic

![](/api/attachments/VK2E82CQ/fulltext/images/04980e52635aff4aa023b307114e6b3efd77efbbf40b5abd7d3d155182a476d9.jpg)

Kaushal Chari is a professor in the Information Systems and Decision Sciences department in the Muma College of Business at the University of South Florida. His research interests are in software engineering, business intelligence and distributed systems. He is interested in applying quantitative as well as intelligent techniques to address problems related to IT systems, software development and business process management. Chari's work has been

published in a variety of academic journals, including Decision Support Systems, Management Science, Information Systems Research, INFORMS Journal on Computing, and IEEE Transactions on Software Engineering. Chari served as the associate editor of MIS for Interfaces journal from 2002-2010, and as the vice chair of the INFORMS Information Systems Society from 2007 – 2009. He is the co-winner of the 2009 Design Science Award from INFORMS Information Systems Society.

![](/api/attachments/VK2E82CQ/fulltext/images/ba9afb912cb918a6788b0ea90670ae9a72551604584b4cda52b88a5e788b3887.jpg)

Manish Agrawal is a professor in the Information Systems and Decision Sciences department in the Muma College of Business at the University of South Florida. His research interests are in extreme event response, social media analytics, decision fusion, and software quality. His work has been published in Decision Support Systems, Management Science, MIS Quarterly, INFORMS Journal on Computing, Journal of Management Information

Systems, IEEE Transactions on Software Engineering, and the Journal of Organizational Computing and Electronic Commerce. His research and teaching have been funded by the US National Science Foundation, and the US Department of Justice.

# ACCEPTED MANUSCRIPT

## Highlights

Information security investments are becoming an increasingly dominant part of IT and corporate spending. Yet, there is limited guidance on optimal allocation of these investments. This paper develops a stochastic optimization model for the optimal allocation of information security controls that incorporates uncertainties in vulnerability assessments. The utility of the model is demonstrated for a realistic IT infrastructure.
