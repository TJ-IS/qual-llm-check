---
otero_id: 7798
otero_key: "8FYJWDTU"
title: "When Hackers Talk: Managing Information Security Under Variable Attack Rates and Knowledge Dissemination"
authors: "Vijay Mookerjee; Radha Mookerjee; Alain Bensoussan; Wei T. Yue"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0341"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/8FYJWDTU/fulltext/images/8bedcca53c47ff0a801ac47e611d0a2972438339b84ffaf0d4dd7bfa695974de.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## When Hackers Talk: Managing Information Security Under Variable Attack Rates and Knowledge Dissemination

Vijay Mookerjee, Radha Mookerjee, Alain Bensoussan, Wei T. Yue,

## To cite this article:

Vijay Mookerjee, Radha Mookerjee, Alain Bensoussan, Wei T. Yue, (2011) When Hackers Talk: Managing Information Security Under Variable Attack Rates and Knowledge Dissemination. Information Systems Research 22(3):606-623. http:// dx.doi.org/10.1287/isre.1100.0341

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/8FYJWDTU/fulltext/images/fd833bfda942180e8c0de79b0da4d9f7bc0ef2fababee00a5f3deb3ec4fd1eb1.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# When Hackers Talk: Managing Information Security Under Variable Attack Rates and Knowledge Dissemination

Vijay Mookerjee, Radha Mookerjee, Alain Bensoussan School of Management, The University of Texas at Dallas, Richardson, Texas 75083, {vijaym@utdallas.edu, radham@utdallas.edu, alain.bensoussan@utdallas.edu}

Wei T. Yue

City University of Hong Kong, Kowloon Tong, Hong Kong, People’s Republic of China, weityue@cityu.edu.hk

his paper analyzes interactions between a firm that seeks to discriminate between normal users and hackers that try to penetrate and compromise the firm’s information assets. We develop an analytical model in which a variety of factors are balanced to best manage the detection component within information security management. The approach not only considers conventional factors such as detection rate and false-positive rate, but also factors associated with hacker behavior that occur in response to improvements in the detection system made by the firm. Detection can be improved by increasing the system’s discrimination ability (i.e., the ability to distinguish between attacks and normal usage) through the application of maintenance effort. The discrimination ability deteriorates over time due to changes in the environment. Also, there is the possibility of sudden shocks that can sharply degrade the discrimination ability. The firm’s cost increases as hackers become more knowledgeable by disseminating security knowledge within the hacker population. The problem is solved to reveal the presence of a steady-state solution in which the level of system discrimination ability and maintenance effort are held constant. We find an interesting result where, under certain conditions, hackers do not benefit from disseminating security knowledge among one another. In other situations, we find that hackers benefit because the firm must lower its detection rate in the presence of knowledge dissemination. Other insights into managing detection systems are provided. For example, the presence of security shocks can increase or decrease the optimal discrimination level as compared to the optimal level without shocks.

Key words: optimal security management; variable attack rates; hacker learning; security shocks History: Alok Gupta, Senior Editor; Giri Kumar Kayi, Associate Editor. This paper was received on February 12, 2009, and was with the authors 7 months for 4 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

The incidence of cyber attacks and information security breaches has become a major concern over the past few years. According to the U.S. Government Accounting Office (U.S. Govt. 2007), the annual losses from cyber attacks in the U.S. are in the range of \$50 billion to \$60 billion. These attacks have been directed at a wide variety of organizations, ranging from high-profile industries to prestigious universities. Present-day hackers are being increasingly motivated by financial gains rather than personal curiosity (Gordon et al. 2003, Evers 2005, Sophos 2008).

Information security is almost inseparable from information technology. It is a vital issue for firms that use the Internet to conduct business transactions because consumer perception of information security is known to affect online purchase behavior (Schlosser et al. 2006). In addition, information security is also crucial for firms that electronically store sensitive data related to customer profiles, sales forecasts, and technical expertise. Thus firms are becoming increasingly aware of the link between information security and the reputation of their brand (Ernst and Young 2008).

While managing information security for a firm could involve different tasks, such as prevention, detection, and response, our focus here is on the detection component of information security. A firm needs a detection system (e.g., firewalls, intrusion detection systems, etc.) to identify attack traffic that could originate from internal as well as external sources. In addition, the detection system must also allow normal traffic to pass through. The detection system’s ability to discriminate between attackers and normal users is referred to as its discrimination ability, best represented as a so-called Receiver Operating Characteristics curve, or ROC curve (see Figure 1). Such a curve plots the possible trade-offs that the detection system can achieve between its detection ability

Figure 1 Detection Systems with Different Discrimination Ability Systems with highest discrimination ability

![](/api/attachments/8FYJWDTU/fulltext/images/86333ef4346936a12e6a24df5b44bf1085aac227df2a07cf59f4f35d3be556f3.jpg)

and its false-positive rate; all points on a particular curve correspond to the same discrimination ability. A detection system that has a higher detection ability for the same false-positive rate is considered to possess higher discrimination ability.

The discrimination ability of a detection system could gradually deteriorate because of changes in the environment in which it operates (drift). Alternatively, there could also be events that abruptly degrade the discrimination ability (shocks). As the discrimination ability deteriorates, hackers could intensify attacks on the firm. In response, the firm needs to continuously expend effort to optimally maintain the detection system so as to balance the cost of maintaining the system with the cost of detection errors (classifying normal users as malicious and malicious users as normal). In Figure 1, deterioration causes a shift from a higher ROC curve to a lower one, whereas maintenance has the opposite effect. We next discuss factors affecting a firm’s detection system under two categories: (a) traffic conditions, (b) system degradation and maintenance.

## 1.1. Traffic Conditions

While the network traffic for a firm is of many types, it can be broadly divided into two types: normal and malicious. Normal traffic refers to legitimate users (customers, employees, etc.) who are authorized to access and use the firm’s information system resources in a variety of ways. If legitimate access is denied, it imposes costs on the firm by way of lost revenue opportunities or loss of productivity. Thus, normal traffic must be recognized as such and these users should be allowed to perform legitimate tasks. At the same time, malicious traffic must be detected and blocked. From password sniffing to DNS exploits, it is widely recognized that the heterogeneous nature of malicious (or hacker) traffic makes detection an especially challenging task. We consider two broad categories of hackers: (1) value-seeking, and (2) opportunistic. Value-seeking hackers are motivated by financial gains<sup>1</sup> and attack at a rate that depends on the detection system.<sup>2</sup> Everything else held equal, a weaker detection system (i.e., one where it is easier to escape detection) is preferred by valueseekers. Hacking traffic could also consist of opportunistic individuals who continually scan the Internet for suitable targets to attack, and hence, attack at a rate that is independent of the detection system. The total attack rate is given by the sum of the attack rates corresponding to value-seeking hackers and opportunistic hackers.

The variable attack rate feature of this study is motivated by the fact that value-seeking hackers choose to attack depending on the current level of the firm’s security. Arora et al. (2008), study the impact of disclosing vulnerability information and find an increase in the total number of attacks across firms, following the release of vulnerability information. The explanation they offer for this finding is that some firms do not promptly patch a recently announced vulnerability, and provide hackers with a window of opportunity to attack. This phenomenon has been observed in other works as well (Arbaugh et al. 2000).

We consider the attack rate experienced by a firm to be a result of the emergent behavior of a population of hackers that attack to serve individual interests, rather than those of the hacking community as a whole. That is, in this study, we consider a firm that is under threat from a population of individually motivated hackers, rather than one that is guarding itself against coordinated attacks (e.g., those carried out by a terrorist group). The difference, of course, is that members of a terrorist group may sacrifice individual interests to benefit the group as a whole. Individual hackers, on the other hand, attack based on their assessment of successfully compromising the firm’s security and possibly their personal value of escaping detection and penetrating the system. To allow our discussion to be general, the model in this paper is presented and analyzed without making any functional assumptions concerning the relationship between the system’s discrimination ability and the attack rate.

## 1.2. System Degradation and Maintenance

Previous studies have typically treated information security management decisions to be static despite the fact that the information security landscape continues to be as fluid and dynamic as ever.<sup>3</sup> Products provide some protection, but effective security processes that recognize and manage the inherent insecurity in products must be in place (Ulvila and Gaffney 2004). To capture such process aspects of security management, we allow the discrimination ability of a detection system to drift with time; this requires that effort be continuously spent to keep the discrimination ability at the desired level. We next provide some specific examples of detection system drift that arise from changes in the environment and from changes in hacker behavior.

Detection systems are usually designed so that they can be customized to fit the operating environment of the firm that deploys it (Cavusoglu et al. 2009). In addition, because many current detection systems (especially IDSs) are constructed by manual encoding of expert knowledge, changes to the system must be made to reflect new attack types or changed computing environments (Lee et al. 1999). These changes (or maintenance) are not a one-time activity but must be done periodically to reflect modified traffic patterns, the costs of misdetection and false-positive errors, as well as to introduce new rules and checks with a view to increasing the discrimination ability of detection (Crothers 2003, Scarfone and Mell 2007). Maintenance activities also include the tasks associated with installing and distributing updated versions of the detection software provided by vendors. Because the firm’s detection system operates in an application environment, changes in this environment can also impact the system’s discrimination ability. New features in a firm’s applications and services often generate modified information security requirements (Jones 2007). For instance, a change in business rules or processes might require the detection system to be modified; e.g., in an order-entry application, the addition of a new online payment module will likely generate a new set of security requirements. A detection system may also need to be modified because of hardware changes: e.g., addition of a new router, creation of a new subnetwork, addition of new servers, and so on. Finally, even though the current discrimination ability of the detection system may be acceptable to the firm, it may have to be enhanced to comply with industry standards; e.g., implementing Payment Card Industry (PCI) standards, requires frequent and regular updates to virus detection software (Imprivata 2007).

In addition to changes in the hardware or software environment, a detection system may also need to be maintained in response to changes in hacker behavior. In adversarial detection domains, such as SPAM filtering or intrusion detection, adversaries often adapt their attack behavior to changes in the detection system. Thus a firm’s detection system needs maintenance, often on a continuous basis. This is best illustrated by a hacker’s account of this dynamic nature: “if you stop (hacking), if you don’t do it for one week then things change, the network always changes. It changes very quickly and you have to keep up and you have to learn all the tricks by heart, the default passwords, the bugs you need 0 0 0” (Jordan and Taylor 1998, p. 766). In addition to continuous degradation, the system’s discrimination ability could also fall sharply and abruptly due to the arrival of a security shock, such as the release of a new worm or a virus. We will consider the impact of security shocks through a simulation experiment later in this paper.

Maintaining a detection system can be costly. Even for organizations with a relatively simple security environment, it is necessary to take the time to perform the analysis needed to determine whether and how hackers are trying to break in, or understand whether the latest worm is trying to exploit a newly announced vulnerability. For larger enterprises and government entities, this problem can get significantly worse. For instance, complex attack graphs need to be analyzed to study potential moves by hackers and the likelihood of a breach occurring at the various nodes in the firm’s network (Gupta and Winstead 2007). An important aspect of managing a detection system, however, is that while performing various maintenance activities, a firm needs to consider how these activities will impact hacker behavior. Specifically, our focus is on a specific aspect of hacker behavior, namely, the attack rate, or the number of hackers per unit time that attempt to penetrate the system. As discussed, the discrimination ability of the detection system (more specifically, its detection rate) could influence the attack rate.

## 1.3. Contribution and Results

The goal of managing a detection system is to reduce security threats while keeping maintenance costs low. Ultimately, therefore, a firm must strike a balance between the effort spent on improving discrimination ability and the increase in error costs that would result if these efforts were not made. The effort spent to improve system discrimination ability has its obvious associated cost (the cost of human expertise, technology costs, etc.). Also, it is important to consider the productivity of this effort, i.e., how the effort translates to higher discrimination ability. For example, the productivity of effort could change across different levels of discrimination ability and for different personnel and technology configurations. The other aspect of cost, namely, error cost, depends for a firm on the costs associated with wrongly treating a normal user as malicious (false-positive cost) and the costs associated with wrongly treating a malicious user as normal (false-negative or misdetection cost).

Our work extends the work on knowledge-based system design where problems arrive exogenously and need to be classified into one of two classes (Bensoussan et al. 2009, Yue and Cakanyildirim 2007). Instead, we focus on systems that operate under conditions where the adversary can modify her behavior depending on the state of the system. Previous work in this area includes designing detection systems that classify a user session as benign or malicious, taking into account that the adversary has an incentive to defeat the system (Boylu et al. 2010). A related area of work is to design learning algorithms that simulate the behavior of an adversary (Lowd and Meek 2004). In contrast, our focus here is to determine the optimal amount of effort that should be spent on maintenance over continuous time considering the fact that while the firm’s maintenance decisions influence the system’s current discrimination ability, these decisions could also affect the rate at which attack attempts are made on the system.

Unlike most previous research, the analysis presented here considers endogenous aspects of detection system management. The attack rate faced by the firm includes, via value-seeking hackers, an endogenous component that affects the firm’s optimal choice for the discrimination ability. Because of value-seeking hackers, the problem distinguishes itself from one of pure optimization where a firm guards itself against forces of nature that are indifferent to the firm’s ability to block attacks.

In §5, we analyze an extended model where the impact of hacker knowledge on detection system management is considered. Here, we examine the possibility of hackers who disseminate knowledge among one another to the detriment of the firm. The firm has the ability to suppress the diffusion of this knowledge (e.g., by threatening to prosecute hackers) as well as lower its impact by promptly addressing any vulnerabilities that are revealed. Knowledge dissemination increases the firm’s cost; more knowledgeable hackers not only increase error costs but can potentially increase maintenance costs as well.

Despite the complex nature of our model, we find results that are quite elegant and intuitive. An interesting result is the presence of a steady state solution, i.e., an optimal, steady level of effort together with a constant level of detection and false-positive rate. With knowledge dissemination, the firm’s steady level of effort can increase or decrease. Surprisingly, knowledge dissemination may, under certain conditions, work against the interests of the hacker community. The firm, however, is always worse off with knowledge dissemination. Numerical studies show that from the firm’s perspective, with an increase in normal user traffic, it is better to sacrifice detection ability to improve (i.e., lower) the false-positive rate. On the other hand, when hacker traffic increases as a proportion of the total traffic, the reverse is true.

In §2, we construct a basic model of detection system management (with no knowledge dissemination) and solve it to identify the effort strategies that are optimal under different conditions. In §3, we consider special forms for the attack rate and the error cost function. The results of our numerical studies are presented in §4. In this section, we numerically examine a different category of system deterioration where, in addition to continuous deterioration, there is the possibility of a sudden drop in system discrimination ability. In §5, we consider an extended model of detection system management where hackers disseminate knowledge to the detriment of the firm. In §6, we provide a discussion and summary of the work.

## 2. Basic Model and Solution

The model can be summarized as follows. Let x4t5 denote the system discrimination ability at time t. The expected error cost per event (normal or benign) associated with a system of discrimination ability x is denoted by $f ( \boldsymbol { x } ( \dot { t } ) )$ . It suffices to say that x4t5 is some (scalar) discrimination ability metric and f 4 · 5 is a cost function such that $f _ { x } ( x ) < { \dot { 0 } } ; { \mathrm { i . e } }$ ., the error cost rate decreases as the discrimination ability increases. Next, let u4t5 (the control) be the intensity of maintenance effort exerted at time t; the cost of this effort is k ·u4t5, where k is a constant that represents the cost of effort per unit time. To complete the description of the model, we note that the application of effort increases system discrimination ability, whereas external factors act to reduce system discrimination ability. The firm’s objective is to minimize the total cost (error cost plus maintenance effort cost) over an infinite time horizon taking into account the rate at which hackers attack the system.

In this section, we describe the mathematical details of the model and its solution. We begin this section by first describing the state equation and the objective function in the model. The state equation describes the manner in which the system responds to the control and the forces acting to reduce system discrimination ability. Table 1 contains a list of the key variables used in the paper. Some additional variables that will be used in the extended model considering hacker knowledge are included here.

Table 1 Model Notation

<table><tr><td>Notation</td><td>Definition</td><td>Unit</td></tr><tr><td colspan="3">Control variable</td></tr><tr><td> $u(t) \in [0, 1]$ </td><td>Intensity of effort exerted at time  $t$ </td><td>man-months per unit time</td></tr><tr><td colspan="3">State variable</td></tr><tr><td> $x, x(0) = x_0$ </td><td>System discrimination ability at time  $t$ </td><td>—</td></tr><tr><td colspan="3">State variable</td></tr><tr><td> $y, y(0) = y_0$ </td><td>Hacker knowledge at time  $t$ </td><td>—</td></tr><tr><td colspan="3">Decision variables</td></tr><tr><td> $\hat{x}$ </td><td>Steady-state system discrimination ability</td><td>—</td></tr><tr><td> $\hat{y}$ </td><td>Steady-state level of hacker knowledge</td><td>—</td></tr><tr><td> $\hat{u}$ </td><td>Steady-state maintenance effort</td><td>man-months per unit time</td></tr><tr><td colspan="3">Other definitions</td></tr><tr><td> $c_0$ </td><td>Effort coefficient</td><td> $(man-month)^{-1}$ </td></tr><tr><td> $c_1$ </td><td>Deterioration coefficient</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $c_2$ </td><td>Diffusion coefficient</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $c_3$ </td><td>Suppression coefficient</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $k$ </td><td>Cost of effort per unit time</td><td>dollars per man-month</td></tr><tr><td> $a$ </td><td>Technology effectiveness parameter</td><td>—</td></tr><tr><td> $\lambda_{1,2}$ </td><td>Adjoint variables</td><td>dollars</td></tr><tr><td> $\delta(x)$ </td><td>System deterioration function</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $H_0$ </td><td>Attack rate when all hackers attack</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $\gamma(x)$ </td><td>Attack rate by value-seeking hackers on a system of discrimination ability  $x$ </td><td> $(unit time)^{-1}$ </td></tr><tr><td> $\gamma_0$ </td><td>Attack rate by opportunistic hackers, a constant</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $n$ </td><td>Rate of benign traffic</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $\eta(x)$ </td><td>Total attack rate  $(= \gamma(x) + \gamma_0)$ </td><td> $(unit time)^{-1}$ </td></tr><tr><td> $m(x)$ </td><td>Total traffic rate  $(= \eta(x) + n)$ </td><td> $(unit time)^{-1}$ </td></tr><tr><td> $r$ </td><td>Discount rate</td><td> $(unit time)^{-1}$ </td></tr><tr><td> $f(x)$ </td><td>Expected cost incurred per case for a system of discrimination ability  $x$ </td><td>dollars per case</td></tr><tr><td> $g(x, p_f)$ </td><td>Expected cost per unit time incurred for  $x$  and  $p_f$ </td><td>dollars per unit time</td></tr></table>

## 2.1. The State Equation

The state (discrimination ability) of the system continuously reduces due to natural drift and improves as a result of maintenance effort. The rate at which discrimination ability deteriorates because of natural drift is given by $c _ { 1 } \delta ( x )$ , where $c _ { 1 }$ is the deterioration coefficient. The function $\delta ( x )$ captures the impact of the current discrimination ability on any further deterioration in this ability. We assume that $\delta ( 0 ) = 0$ to ensure that the deterioration rate becomes zero when the discrimination ability is zero; hence the discrimination ability never becomes negative. This is reasonable; a system with zero discrimination ability cannot degrade further.

To counter the deterioration in discrimination ability, the system needs to be maintained. The rate at which discrimination ability improves due to maintenance is proportional to the amount of effort exerted, $u ( t )$ , and the productivity of this effort measured by an effort coefficient, $c _ { 0 } .$ We further assume that the effort to improve discrimination ability exhibits diminishing returns. The improvement in system discrimination ability is written as below.<sup>4</sup>

$$
c _ {0} u (1 - x).
$$

Considering both effects (improvement and deterioration), the net rate of change in system discrimination ability is defined by the following state equation

$$
\dot {x} = c _ {0} u (1 - x) - c _ {1} \delta (x).\tag{1}
$$

2.2. The Basic Control Problem and Solution The basic control problem with no knowledge dissemination is given by

$$
\begin{array}{l} \min _ {u (t)} J = \int_ {0} ^ {\infty} (m (x) \cdot f (x) + k \cdot u) e ^ {- r t} d t, \\ \text { subject   to } \dot {x} = c _ {0} u (1 - x) - c _ {1} \delta (x), \\ 0 \leq u \leq 1, \\ x (0) = x _ {0}. \end{array}
$$

In the above equation, the objective J is to minimize the total discounted system cost (error cost plus the cost of effort) incurred. The state variable x is the discrimination ability and u denotes the intensity of effort or the control variable. The attack rate 4x5 is comprised of two components: $\gamma _ { 0 }$ is the attack rate associated with opportunistic hackers, and $\gamma ( \boldsymbol { x } )$ is the rate at which value-seeking hackers attack the system when its discrimination ability is $x . ^ { 5 }$ We therefore have $\eta ( x ) = \gamma _ { 0 } + \gamma ( x )$ . The total traffic arriving at the system is denoted by $m ( x ) = n + \eta ( x )$ , where n is the rate of normal traffic. For convenience we set $\phi ( x ) = m ( x ) f ( x )$ . The Hamiltonian of the control problem is

$$
H = \phi (x) + k \cdot u + \lambda (c _ {0} u (1 - x) - c _ {1} \delta (x)).\tag{2}
$$

The first two terms in Equation (2), $\phi ( x ) + k \cdot u$ represent the instantaneous system cost, while the third term represents the future cost of increasing system discrimination ability. We can interpret $\lambda ( t )$ as the marginal cost of system discrimination ability at time t. Because increasing system discrimination ability should reduce the total cost, we expect 4t5 to be negative.

Because the Hamiltonian is linear in $u ,$ the optimal control takes the following bang-bang and (a possible) singular form

$$
u (t) = \left\{ \begin{array}{l l} 1 & H _ {u} <   0, \\ \text { to   be   determined } & H _ {u} = 0, \\ 0 & H _ {u} > 0, \end{array} \right.\tag{3}
$$

where $H _ { u } = k + \lambda c _ { 0 } ( 1 - x )$ . When $H _ { u }$ is negative, we exert full effort $( u = 1 )$ , and when $H _ { u }$ is positive, we exert zero effort $( u = 0 )$ . When $H _ { u } = 0$ and stays at this value, an intermediate level of effort $0 < u \overset { \cdot } { < } 1$ is exerted. This phase is referred to as singular. In the current problem, we show that the singular region has the additional property that the values of the control and the state variables are constant in this region. Thus, the singular region exhibits a steady-state property. The necessary conditions for the singular region are discussed in the next subsection.

## 2.3. Steady-State Analysis

The adjoint equation is $- \dot { \lambda } + \lambda r = \partial H / \partial x ;$

$$
\dot {\lambda} = \phi^ {\prime} (x) + \lambda (c _ {0} u + r + c _ {1} \delta^ {\prime} (x)),\tag{4}
$$

$$
\dot {x} = c _ {0} u (1 - x) - c _ {1} \delta (x),\tag{5}
$$

$$
\dot {H} _ {u} = \dot {\lambda} c _ {0} (1 - x) - \lambda c _ {0} \dot {x}.\tag{6}
$$

Substituting (4) and (5) in (6), and using the fact that $\dot { H _ { u } } = 0$ and $H _ { u } = 0$ in the singular region, we get the steady-state equation

$$
\phi^ {\prime} (x) = - \frac {k}{c _ {0} (1 - x)} \left(\frac {c _ {1} w (x)}{1 - x} + r\right).\tag{7}
$$

In (7), $w ( x ) = \delta ( x ) + ( 1 - x ) \delta ^ { \prime } ( x )$ . We can solve the above equation for ${ \hat { x } } ,$ a constant. Having obtained the value of xˆ, we use ${ \dot { x } } = 0$ in the singular region to get uˆ:

$$
\hat {u} = \frac {c _ {1} \delta (\hat {x})}{c _ {0} (1 - \hat {x})}.\tag{8}
$$

Equation (8) indicates that, like the steady-state level of system discrimination ability, the level of effort in the singular region 4u5ˆ is also constant. The following proposition describes the optimal control policy.<sup>6</sup>

<sup>Proposition</sup> <sup>1.</sup> The structure of the optimal policy can be characterized as below:

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 1 & x (t) <   \hat {x}, \\ \hat {u} & x (t) = \hat {x}, \\ 0 & x (t) > \hat {x}, \end{array} \right.
$$

where the steady-state system discrimination ability 4x5ˆ is obtained by solving Equation (7) and the steady-state level of effort 4u5ˆ is given by Equation (8).

The above proposition states that if the starting discrimination ability $x _ { 0 } > \hat { x } ,$ , then the optimal policy is to use $u = 0$ until the discrimination ability degrades to xˆ. Otherwise, if $x _ { 0 } < \hat { x }$ , then $u = 1$ until the discrimination ability improves to xˆ. The steady state is a preferred state in the problem (as opposed to the initial transient state), and the goal in the transient state is to achieve the steady state as quickly as possible. Thus if the initial discrimination ability is too high (from the perspective of the trade-off between error cost and the cost of effort), this ability is allowed to deteriorate rapidly (by applying zero effort, $u = 0 )$ until the discrimination ability reaches the value of xˆ. When the initial ability is too low, maximum effort of $u = 1$ is applied to quickly achieve the steady-state level of discrimination ability. Figure 2 shows the evolution of the system state under the optimal policy.

## 2.4. Optimal Policy Under Two Variations of the Problem

We next discuss the structure of the optimal policy under two different variations of the problem: (1) when the planning horizon is finite, and (2) when certain system parameters are time-varying quantities, rather than constants.

Figure 2 State Evolution Under Optimal Policy  
![](/api/attachments/8FYJWDTU/fulltext/images/2dccc76279bbf0fd0021a5616455c62cbfa88a9880ad65c9f1a099fa0645ae52.jpg)  
2.4.1. Finite Horizon. An infinite horizon problem that has been considered so far is a reasonable approximation if the parameters of the problem can be expected to stay the same for a relatively long period, $\mathrm { i . e . , }$ for several years. On the other hand, a finite horizon may be more appropriate to use when the firm has a short planning horizon and needs to re-solve the problem periodically. It can be shown that the existing structure of the optimal policy remains optimal; the only difference is that for a finite planning horizon, the system must come out of steady state before the end of the horizon. After coming out of steady state, because there is no salvage value of the discrimination ability at the end of the horizon, the value of the control must be zero. For the full characterization of the policy, it is necessary to specify the starting point and the ending point of steady state. These points in time can be found as follows. Since we know the value of the state variable at the start of the problem and the value of the control variable for the period before steady state is reached, the state equation can be solved to find the time it takes for the state variable to reach the steady-state value $( x ( \tau ) = \hat { x } ,$ , where  is the point in time that marks the start of steady state). To solve for the point in time that marks the end of steady state, it is necessary to use the adjoint equation. Here, the starting value (but not the time) for the adjoint variable is known, namely, the value of $\lambda ( \theta ) = { \hat { \lambda } } ,$ , where  is the point in time where the steady state ends. The transversality condition requires that the ending value of the adjoint variable must be zero; $\mathrm { i . e . , ~ } \lambda ( T ) \overset { \cdot } { = } 0 .$ , where T is the planning horizon. Using these facts, the value of the point in time at which steady state must end can be found. To summarize, the solution to the finite planning horizon version of the problem typically has an additional third component that describes the optimal

control: a period for which $u = 0$ that begins at the end of the steady-state interval and continues until the end of the planning horizon.

2.4.2. Time-Varying Parameters. When the parameters of the problem are time-dependent quantities (in addition to a finite planning horizon), it can be shown that the solution to the problem no longer possesses a steady-state component (see the online appendix). Despite this, it is still possible to find that the optimal control takes on an interior value that changes with time, following a so-called singular arc in optimal control terminology. The presence of a singular arc requires that the derivative with respect to time of $H _ { u }$ (or $\dot { H } _ { u } )$ can be zero for an interval of time. Since $\dot { H _ { u } }$ is also a function of time, it follows that for $\dot { H } _ { u } = 0$ the values of the control, state, and adjoint variables change with time during this interval. Hence, the possibility of a steady-state solution can be ruled out. It some cases it is possible that the functional forms that describe the time-varying problem parameters are such that a singular solution is not possible. In such cases, there are only two remaining possibilities for the optimal control: (a) $u = 1$ followed by $u = 0$ , and (b) $u = 0$ throughout. The case for $u = 0$ followed by $u = 1$ can be ruled out since the control must end with zero.

A special case of time-varying parameters is when the proportion of hacker types changes with time. When this happens, the objective function becomes an explicit function of time. The details of the solution to this case are presented in the online appendix. As mentioned before, when the problem has a finite horizon there are typically three regions in the optimal solution. In the first region, we get a bang-bang solution $( \mathrm { i . e . , 0 }$ or 1) depending on a criterion $\sigma ( x , t )$ that can be calculated using the initial state $( x = x _ { 0 } )$ and $t = 0$ . The solution of this problem in the first region is as follows:

$$
u (t) = \left\{ \begin{array}{l l} 0 & \sigma (x _ {0}, 0) > 0, \\ 1 & \sigma (x _ {0}, 0) <   0. \end{array} \right.
$$

Following the first region, we typically enter a singular region in which the state variable, control variable, and adjoint variable all change with time. The third and last region of the solution consists of an interval where the control is set to zero $( u = 0 )$ . While the optimal solution structure of this problem can be characterized as above, the exact details of the solution can only be found by numerical search. Such a search procedure is described in the online appendix. We next revert to the original problem with constant parameters and an infinite planning horizon. In addition, we consider a special version of the general control problem described in this section that affords a deeper level of analysis.

## 3. Special Functional Forms

In this section, we develop and present some special forms of the firm’s cost function 44x55, the attack rate 44x55, and the relationship between the system discrimination ability x and the rate of system deterioration 44x55. The purpose is to illustrate the results of the previous section in the context of some realistic situations. Specifically, we are interested in providing examples of realistic scenarios where hacker incentives combine with system characteristics to result in the different outcomes predicted by the analysis in the previous section. We begin by presenting a plausible form for the relationship between the discrimination ability of the system $x ,$ the false-positive rate $p _ { f }$ , and the detection rate $p _ { d } .$

## 3.1. Measuring System Performance

The detection rate and the false-positive rate of a detection system can be associated with one another and with the system discrimination ability using the system’s receiver operating characteristics (or ROC) curve. The ROC curve is plotted for a given value of x and a constant a that represents how difficult it is to discriminate between normal traffic and malicious traffic. The following functional form for the ROC curve is used:

$$
p _ {d} = x ^ {a} p _ {f} ^ {a} + (1 - x ^ {a}) p _ {f}.\tag{9}
$$

We make the following observations concerning the functional form in (9):

1. $p _ { d } = 0$ when $p _ { f } = 0 ; p _ { d } = 1$ when $p _ { f } = 1$

2. When $x = 0$ the diagnostic system classifies randomly, $\mathfrak { i } . \mathbf { e } . , p _ { d } = p _ { f } .$

3. $p _ { d } = p _ { f } ^ { a }$ when $x = 1 .$ , where $0 \leq a \leq 0 . 5 ,$ is a technology effectiveness parameter. A lower value of a corresponds to superior technology.

4. $p _ { d }$ is increasing and concave in both its arguments:

(a) $\partial p _ { d } / \partial p _ { f } > 0 ; \partial ^ { 2 } p _ { d } / \partial p _ { f } ^ { 2 } < 0 ,$

$$
(\mathsf {b}) \partial p _ {d} / \partial x > 0; \partial^ {2} p _ {d} / \partial x ^ {2} <   0.
$$

Property 1 is a standard property associated with ROC curves: no positive event will be correctly classified if all cases are classified as negative, and no negative event will be correctly classified if all cases are classified as positive. When $x = 0$ , the ROC curve is a 45<sup></sup> straight line implying that the diagnostic system classifies randomly. From Property 2 and Property 3 we note that $p _ { d }$ is a convex combination of $p _ { f } ^ { a }$ and $p _ { f } ;$ i.e., the value of $p _ { d }$ lies between $p _ { f }$ and $p _ { f } ^ { a }$ . Hence, the best true-positive rate $( p _ { d } )$ that can be achieved for a given false-positive rate $\left( p _ { f } \right)$ is when $x = 1$ . Property 4 suggests that higher true-positive rates can be obtained either at the cost of higher false-positive rates or by increasing discrimination ability.

Our discussion so far has considered the attack rate 4x5 as a function of the system discrimination ability x. To develop a functional form for the attack rate, we begin by deriving a form where hackers are sensitive to the detection rate $p _ { d }$ of the system which, in turn, is a function of the system discrimination ability x and the false-positive rate $p _ { f }$ . We next propose forms for the attack rate considering a heterogeneous hacker population and use these forms to derive the cost function $g ( x , p _ { f } )$ . This cost function is analyzed under these different attack forms to verify that it possesses the properties needed to guarantee the optimality of the control characterized by Proposition 1.

## 3.2. Hacker Types

As mentioned before, we consider two categories of hackers: value-seeking and opportunistic. Opportunistic hackers attack at a rate that is independent of the detection rate of the system, while value-seeking hackers attack at a rate that reduces with the detection rate of the system.

3.2.1. Value-Seekers. We consider a situation where a system is attacked at a rate that reduces with the detection rate. In addition to the detection rates, the attack rate depends on the benefits to the hacker to penetrate the system and the costs of being detected. Detection costs could represent the possible legal ramifications resulting from detection as well as the resources spent to launch the attack. An attack will be detected by the system with probability $p _ { d }$ resulting in a cost of $c _ { h }$ to the hacker, or can go undetected with probability $( 1 - p _ { d } )$ , leading to a benefit $c _ { p }$ to the hacker. A value-seeking hacker will attack only if the expected benefit is greater than the expected cost:

$$
c _ {p} \cdot (1 - p _ {d}) - c _ {h} \cdot p _ {d} > 0.
$$

We consider a heterogeneous, value-seeking hacker population of size $H _ { v }$ where the costs and benefits of hacking are uniformly distributed as $c _ { h } \sim$ $U ( 0 , 2 \beta )$ and $c _ { p } \sim U ( 0 , 2 \alpha )$ . For convenience, denote $\epsilon = { p _ { d } } / { ( 1 - p _ { d } ) }$ and $\omega = \alpha / \beta$ . A necessary condition for a hacker to attack is $c _ { p } > \epsilon c _ { h }$

We first consider a case where the benefits of hacking are sufficiently high relative to the cost, $2 \alpha > 2 \epsilon \beta$ or $\omega > \epsilon .$ . This corresponds to a situation that may be common in the current-day legislative environment; it is typically difficult to legally prosecute an attacker, although it may be possible to detect the attack and prevent penetration. Using the above, the proportion of the hacker population that will choose to attack a system with a detection rate of $p _ { d }$ is given by

$$
\frac {1}{4 \alpha \beta} \int_ {0} ^ {2 \beta} \int_ {c _ {h} \epsilon} ^ {2 \alpha} d c _ {h} d c _ {p}.
$$

Thus the attack rate from value-seeking hackers is given by

$$
H _ {v} \left(1 - \frac {\epsilon}{2 \omega}\right),\tag{10}
$$

where $H _ { v }$ is the total number of value-seekers in the hacker population. Otherwise, if $\omega < \epsilon ,$ the attack rate can be easily written as

$$
H _ {v} \left(\frac {\omega}{2 \epsilon}\right).\tag{11}
$$

3.2.2. Consolidated Attack Rate. The consolidated attack rate, $\eta ( p _ { d } )$ , is comprised of opportunistic hackers and value-seeking hackers. As before, let opportunistic hackers attack at a constant rate that is independent of the security level. For a hacker population size of $H _ { 0 } ,$ , let us assume that a fraction $q _ { v }$ are value-seeking; $( 1 - q _ { v } )$ are opportunistic. Then (for $\omega > \epsilon )$ , using (10) the consolidated attack rate is given by

$$
\eta (p _ {d}) = (1 - q _ {v}) H _ {0} + q _ {v} H _ {0} \left(1 - \frac {\epsilon}{2 \omega}\right).\tag{12}
$$

Otherwise, if $\omega < \epsilon ,$ the expression for the attack rate corresponding to value-seeking hackers will have to be appropriately modified as discussed earlier. When $\omega = \epsilon ,$ the two expressions are identical, implying that the attack rate (and its derivative with respect to the detection rate) is continuous in the detection rate.

## 3.3. The Cost Function

Generally speaking, a firm’s error cost $g ( x , p _ { f } )$ should depend on the attack rate $\eta ( p _ { d } )$ , the rate of normal traffic n, the system’s detection rate $( p _ { d } )$ , and the falsepositive rate $\dot { ( \boldsymbol { p } _ { f } ) }$ . The other component of cost is, of course, the cost of the effort spent to maintain the system $( k u )$ . The error cost can be expressed as a function of the discrimination ability alone by optimizing the false-positive rate for a given value of x.

We first derive the expected cost function $g ( x , p _ { f } )$ per unit time for the ROC curve in (9) and an attack rate and normal rate denoted by $\eta ( p _ { d } )$ and $n ,$ respectively. The two types of error costs associated with the use of a detection system are false-negative $\left( c _ { m } \right)$ and false-positive $( c _ { f } )$ . Let $p _ { d } = R ( x , p _ { f } )$ be the detection rate for a system of discrimination ability level x and a false-positive rate $p _ { f }$ . The expected error cost per unit time can be written as follows:

$$
g (x, p _ {f}) = n c _ {f} p _ {f} + c _ {m} \eta (p _ {d}) (1 - p _ {d}).\tag{13}
$$

For an optimally configured system, we have $d g / d p _ { f } = 0$ . An optimally configured system is one where the false-positive rate and the detection rate have been set to make an optimal trade-off between the two error costs. The properties of the cost function needed for optimality (i.e., convex and decreasing in x) are discussed in the online appendix.

## 3.4. Model of System Deterioration

We consider a situation where the current discrimination ability can play a role on the rate a system deteriorates over time: $\delta ( x ) = x e ^ { - \alpha _ { 0 } x }$ . In this form, a system that classifies randomly $( x = 0 )$ cannot degrade further. This is reasonable because when $x = 0$ , there are no rules in the system to learn; the ROC curve for the system reduces to $p _ { d } = p _ { f }$ . This is equivalent to a classifier that randomly classifies a proportion of incoming cases as malicious (based on the prior probability of this class) and the remaining cases as benign. A higher value of $\alpha _ { 0 }$ (a robustness coefficient) makes the system deteriorate slowly. When the robustness coefficient is sufficiently high, $\delta ( x )$ becomes nonmonotonic; $\mathrm { i . e . , }$ the rate of deterioration increases with x at first, but as x is increased beyond a point the rate decreases. For a very high value of $\alpha _ { 0 } ,$ the deterioration rate becomes close to zero at high values of $x ,$ implying that as the system becomes perfect (x approaches 1), it cannot be affected by the passage of time. If $\alpha _ { 0 } < 0 ,$ , we have a brittle system that deteriorates faster as its discrimination ability increases. Thus by controlling $\alpha _ { 0 } ,$ , we can cover a wide variety of cases.

## 4. Numerical Study

In this section, we report the results of an extensive set of experiments designed to explore the impact of the various model parameters on the performance variables in steady state: detection rate $( \hat { p } _ { d } )$ , false-positive rate $( \hat { p } _ { f } )$ , and the rate of system cost $( \phi ( \hat { x } ) + k \hat { u } )$ . The different model parameters can be categorized in four groups. $T r a f f i c$ parameters are comprised of the normal traffic rate 4n5, maximum attack rate $( H _ { 0 } )$ , and the proportion of value-seeking hackers $( q _ { v } )$ . Effort parameters consist of the cost of expertise associated with maintenance effort 4k5, the productivity of this effort in its ability to increase discrimination ability, namely, the effort coefficient $( c _ { 0 } )$ , and the technology effectiveness parameter 4a5. Error cost parameters are associated with the costs of the two kinds of errors: false-positive $( c _ { f } )$ , and false-negative $\left( c _ { m } \right)$ Finally, system deterioration parameters are associated with factors that measure how easy it is for the discrimination ability to decrease: deterioration coefficient $\left( c _ { 1 } \right)$ and the robustness coefficient $\left( \alpha _ { 0 } \right)$ . The impact of each of these parameters on the performance variables of interest is investigated below.

$$
\begin{array}{r l} & {\underbrace {\hat {p} _ {d} , \hat {p} _ {f} , (\phi (\hat {x}) + k \hat {u})} _ {\text {Performance}}} \\ & {\Rightarrow \underbrace {n , H _ {0} , q _ {v}} _ {\text {Traffic}} \underbrace {c _ {0} , a , k} _ {\text {Effort}} \underbrace {c _ {f} , c _ {m}} _ {\text {Error}} \underbrace {c _ {1} , \alpha_ {0}} _ {\text {Deterioration}}} \end{array}
$$

Table 2 Baseline Parameter Values

<table><tr><td>Parameter</td><td>Baseline value</td></tr><tr><td>Robustness coefficient ( $\alpha_0$ )</td><td>2</td></tr><tr><td>Deterioration coefficient ( $c_1$ )</td><td>1</td></tr><tr><td>Cost of effort (k)</td><td>2,000</td></tr><tr><td>Proportion of value-seeking hackers ( $q_v$ )</td><td>0.9</td></tr><tr><td>Technology effectiveness parameter (a)</td><td>0.15</td></tr><tr><td>Cost of false-negative ( $c_m$ )</td><td>150</td></tr><tr><td>Arrival rate of normal traffic (n)</td><td>300,000</td></tr><tr><td>Maximum rate of attack traffic ( $H_0$ )</td><td>15,000</td></tr><tr><td>Effort coefficient ( $c_0$ )</td><td>2</td></tr><tr><td>Discount rate (r)</td><td>0.05</td></tr><tr><td>Cost of false-positive ( $c_f$ )</td><td>10</td></tr></table>

## 4.1. Baseline Parameter Values

Table 2 lists the baseline (or default) values used in the numerical experiments. We use a baseline value of 0.15 for the technology parameter $^ { a , }$ a moderate value because this value can range between 0 and 0.5. A smaller value represents a system with superior technology. To provide some context, we imagine that we start with a random classifier $( x _ { 0 } = 0 )$ and apply full effort for a certain period of time to raise the system discrimination ability to the maximum possible value. Because we are developing the system, we can imagine that there is no drift and hence the state equation during the development period is $\dot { x } = c _ { 0 } u ( 1 - x )$ For $c _ { 0 } = 2 ,$ , if we begin with a random classifier, it will take approximately 1.5 months to achieve a system to reach a discrimination ability of 0.95. To provide some sense of how the system would deteriorate, a value of $c _ { 1 } = 1$ and $\alpha _ { 0 } = 2$ implies that a perfect classifier $( x = 1 )$ will take approximately three months to drift to half its initial discrimination ability, if left without any maintenance.

The cost of error could vary from one situation to another. However, it is reasonable to assume that it would cost more per month for the firm to operate a random classifier than it would cost to employ an expert for one month. We use an arrival rate of 300,000 arrivals of normal visitors per month (based upon traffic data at some actual financial and e-commerce sites; see www.trafficestimate.com), and the following values for the classification cost parameters: $c _ { m } = 1 \bar { 5 } 0 ; c _ { f } = 1 0$ . These values are chosen such that it is 15 times costlier to let a malicious event go undetected than it is to classify a benign event as malicious.

In reporting the numerical results, unless noted, we use normalized total cost (normalized to a positive value between zero and one) to enable us to depict the different outcome variables in a single figure.

## 4.2. Traffic Conditions

Figure 3 shows the firm’s optimal response to changes in the volume of normal traffic. When normal traffic arriving at the firm increases, the detection rate is lowered. Despite this, the effort is higher, implying that more of the resources are directed toward lowering the false-positive rate. Thus the false-positive rate is lowered at the expense of the detection rate. The normalized cost increases with the normal traffic because there are more cases to classify as malicious or benign. When the hacker traffic to the firm increases, the situation reverses (see Figure 4). Here, it becomes important to focus on blocking hacking attempts. Thus the detection rate increases with hacking traffic. To achieve this, the discrimination ability and the corresponding effort is increased. Note that the false-positive rate is sacrificed to achieve higher detection ability, exactly the reverse of what was done when normal traffic was increased. In Figure 5 we investigate how the characteristics of the hacker population affects the firm’s various outcomes at their optimal levels. As seen in Figure 5, as more hackers are opportunistic (i.e., hackers attack without considering the detection rate of the system), the focus of the effort is on improving the detection rate at the expense of the false-positive rate.

Figure 3 Impact of Normal Traffic  
![](/api/attachments/8FYJWDTU/fulltext/images/dc3dc8a9455db26800121e7b8f77c174c8b9741fe0e7169a186a9bde8a5a04b4.jpg)

## 4.3. Error Costs

In Figure 6 we investigate the impact of the ratio of the false-negative to the false-positive cost. When the false-negative cost (or misdetection cost) increases, the firm should pay closer attention to the detection rate even at the expense of worsening (i.e., increasing) the false-positive rate. As shown in the figure, the total normalized cost increases with the error cost ratio. The attack rate experienced by the firm is influenced in an intuitive manner (not shown): as the detection rate increases, the attack rate decreases.

Figure 4 Impact of Hacker Population Size  
![](/api/attachments/8FYJWDTU/fulltext/images/5959437708578a215f3798564a2edeccb2263135e92b4de5f17ec8ded5643dba.jpg)

![](/api/attachments/8FYJWDTU/fulltext/images/ecbce86a297b69ffbc0168847dc7d40992ed37807a0a362927b37664ec66412e.jpg)

## 4.4. System Deterioration

Figure 7 shows the impact of an increase in system degradation from an increase in the deterioration coefficient. The discrimination ability (not shown) and detection rate decrease when the deterioration coefficient is increased. The other outcomes $( p _ { f }$ and cost) also worsen as the deterioration coefficient increases. The impact of the system robustness parameter $\left( \alpha _ { 0 } \right)$ on different outcome measures is intuitive (not shown). As the robustness coefficient becomes higher, the negative forces of system deterioration weaken. Hence the various outcomes improve.

## 4.5. Changing Hacker Proportions

We consider a situation where hackers convert from being opportunistic to being value-seeking over a finite planning horizon. For contrast, we also depict the baseline case where the hacker type proportions remain constant during this interval. When the hacker type proportions are constant, there is a steadystate region in the solution where the discrimination ability and the maintenance effort are constant. On the other hand, when these proportions change, the steady-state solution is replaced by a singular solution where the discrimination ability and maintenance effort change with time. We consider two cases of changing hacker types. First, we consider a case where opportunistic hackers attack at a very low rate; hence, as opportunistic hackers become value seeking ones, the total attack rate increases. A low attack rate by opportunistic hackers may correspond to a situation where the firm has not been “discovered” by opportunistic hackers, but as these hackers become value seeking, they become aware of the firm’s assets. Figures 8 and 9 show the behavior of the optimal policy when hacker types change over time. The case of constant hacker type proportions is indicated by the index c whereas the case of time-varying proportions is indexed by t. As can be seen in these figures, both the discrimination ability and the maintenance effort increase during the singular region to accommodate the increasing attack rate due to hacker type conversion. Figures 10 and 11 show the opposite; here we consider a case where opportunistic hackers attack the firm at a high rate (the firm is an attractive target), but as these hackers become value seeking, they attack at a rate that is sensitive to the firm’s detection ability. The net effect is that the attack rate decreases due to hacker type conversion. As expected, both the discrimination ability and the maintenance effort can be reduced to take advantage of the lower attack rate.

Figure 6 Impact of Error Cost Ratio  
![](/api/attachments/8FYJWDTU/fulltext/images/1af7fe188e271b6bdcdd4b93b4c167e76e41b046ebab3a99cdb32ab097daf4ed.jpg)

Figure 7 Impact of Deterioration  
![](/api/attachments/8FYJWDTU/fulltext/images/86bbcaa618dc6d255b6eb1148ad26112418d6a00a09de0cc2f2bd746d3ffe9be.jpg)

Figure 8 Increasing Attack Rate due to Changing Hacker Types: Discrimination Ability  
![](/api/attachments/8FYJWDTU/fulltext/images/308d045f6bcd19dc2bab8d93cd2d09e1e6e19acc2a8b983c1716f9e86fa69571.jpg)

Figure 9 Increasing Attack Rate Due to Changing Hacker Types: Maintenance Effort  
![](/api/attachments/8FYJWDTU/fulltext/images/6f6c89efab281a59da98565add445de2a7682303e6489ab38e5376e366d9fdba.jpg)

We also consider a case where the conversion of hacker types exhibits an asymptotic behavior. That is, to begin with, the hacker type proportions change more rapidly with time, but then this rate of change diminishes and the hacker type proportions almost become constant. Figures 12 and 13 depict how the optimal discrimination ability and maintenance effort change in response to the above asymptotic timedependent hacker proportions. Here, it is interesting to find that the optimal solutions for discrimination ability and maintenance effort also show an asymptotic behavior.

## 4.6. Cost-Quality Trade-Offs

Table 3 depicts various scenarios that illustrate costquality trade-offs. The parameters k (cost parameter) and a (technology effectiveness parameter) can be varied to study optimal choices that a manager can make.

Figure 10 Decreasing Attack Rate Because of Changing Hacker Types: Discrimination Ability  
![](/api/attachments/8FYJWDTU/fulltext/images/c543bfeec8d22ebcac4fecf2b199ac5867546cf7f4f9b6d18d6baa7dcf2eb0a1.jpg)

Figure 11 Decreasing Attack Rate Because of Changing Hacker Types: Maintenance Effort  
![](/api/attachments/8FYJWDTU/fulltext/images/b300c47f5dc44145cb7589937e6725de167a28b2dbc38386d8f89f6d3c31e649.jpg)

The value of k drives the cost of maintenance effort and is related to the technology being deployed. The value of a represents the effectiveness of the technology, i.e., the classification ability of the detection system. With a higher value of $k ,$ one can obtain more effective technology (low a) and thus lower the effort and (sometimes) the total cost. In Table 3 the value of k is varied to improve the value of a. Starting from a low value of the cost of effort 4k5, we observe that the total cost can be lower at a higher value of the cost of effort but improved technology (see scenario 5, for example). This experiment provides managers with a way to study the trade-offs between the effectiveness of technology employed and the total cost (error plus maintenance cost) of operating the detection system.

## 4.7. Managing Effort Under System Shocks

So far, we have considered a fall in system discrimination ability that is continuous. However, it is possible that sudden shocks in discrimination ability occur; e.g., a new security threat, such as the spread of a worm, or a new vulnerability in a widely used operating system, could occur suddenly. We next study the steady state behavior of system discrimination ability in the presence of sudden shocks. A shock in discrimination ability is assumed to arrive following a Poisson process with mean . The magnitude of the shock 45 follows an arbitrary distribution j45. A shock of magnitude $\zeta$ results in a fall in system discrimination ability given by the relationship below. The exponent  modulates the impact of the shock on the system discrimination ability. A high value of  corresponds to a system that is more vulnerable to shock.

Figure 12 Asymptotic Change in Hacker Types: Discrimination Ability  
![](/api/attachments/8FYJWDTU/fulltext/images/a4220845dd98b3575a8e800c6ed1aa46d2c191eb42c7602724079197455dca10.jpg)

Figure 13 Asymptotic Change in Hacker Types: Maintenance Effort  
![](/api/attachments/8FYJWDTU/fulltext/images/7b230ecaecd12a2fadbb288fe049965f52314a33bda67ae41d106b50eb18aa04.jpg)

$$
x ^ {\prime} = x e ^ {- \gamma \zeta}.
$$

In the above, x and x<sup>0</sup> are the values of discrimination ability before and after a shock.

Figure 14 shows a sample evolution of the state of the system (discrimination ability) in the presence of security shocks. In this example, the initial state has a higher discrimination ability than the steady-state level. Hence, the system is allowed to deteriorate with zero effort. However, before achieving steady state a shock arrives that drops the discrimination ability to a value below the steady-state level. Hence, full effort is applied to increase the ability to the steady-state level. Then the steady-state level of effort is used until the next shock and so on.

To evaluate the system cost in the presence of shocks, we construct the following simulation experiment. A certain constant value of the discrimination ability is picked and a series of shocks is simulated on the system. The system cost is then measured over an interval of time that corresponds to a given number of shocks and the discrimination ability that provides the lowest value of system cost is noted. This value of the discrimination ability (called the golden mean in optimal control theory terminology) is compared with the optimal steady-state level of the discrimination ability 4x5ˆ found without considering shocks.

Table 3 Cost-Quality Trade-Offs

<table><tr><td>Scenario</td><td>a</td><td>k (in 1,000 s)</td><td>Pd</td><td>Pf</td><td>Cost</td></tr><tr><td>1</td><td>0.2</td><td>50</td><td>0.6292</td><td>0.112</td><td>1,000,312</td></tr><tr><td>2</td><td>0.15</td><td>75</td><td>0.6795</td><td>0.091</td><td>813,151.1</td></tr><tr><td>3</td><td>0.14</td><td>100</td><td>0.6881</td><td>0.086</td><td>781,979.7</td></tr><tr><td>4</td><td>0.13</td><td>150</td><td>0.6956</td><td>0.081</td><td>758,294.4</td></tr><tr><td>5</td><td>0.12</td><td>225</td><td>0.7028</td><td>0.076</td><td>736,628.6</td></tr><tr><td>6</td><td>0.115</td><td>325</td><td>0.7034</td><td>0.074</td><td>741,653.9</td></tr><tr><td>7</td><td>0.11</td><td>475</td><td>0.701</td><td>0.071</td><td>752,088.3</td></tr><tr><td>8</td><td>0.105</td><td>675</td><td>0.6976</td><td>0.068</td><td>763,267.3</td></tr><tr><td>9</td><td>0.1</td><td>925</td><td>0.6944</td><td>0.066</td><td>772,228.5</td></tr><tr><td>10</td><td>0.095</td><td>1,200</td><td>0.6911</td><td>0.063</td><td>773,971.6</td></tr></table>

Figure 14 Evolution of System State with Shocks  
![](/api/attachments/8FYJWDTU/fulltext/images/575df3590de9ea4eab4e669b2576ca304b3e52327f299fd0c10ad0c52d1200f7.jpg)

If the golden mean is higher than the steady-state level, then firms must exert more effort to keep system discrimination ability at this elevated level. Thus the expenditure on the detection system (i.e., total cost minus error cost) must be higher in the presence of shocks. On the other hand, if the golden mean is lower in the presence of shocks, it implies that firms would be able to lower their security expenditure, but increase error costs.

Figure 15 shows the impact of shocks with magnitude (i.e., the variable ) uniformly distributed between zero and a maximum value. The dotted line represents the optimal value of the steady-state discrimination ability with no shocks. The “+” symbols represent optimal values for the discrimination ability in the presence of shocks (i.e., the golden mean). The golden mean values are obtained from a simulation experiment where different choices for the discrimination ability are used and the one that minimizes the total system cost (error cost plus the effort cost) in the presence of shocks is chosen. We allow the system to accumulate costs for a very large number of shocks (= 500; the golden mean converges well below this number). Figure 15 shows that if the shocks of high magnitude are expected, then it is better to operate the detection system at a lower level (i.e., the golden mean is lower) than when there are no shocks. This result can be explained by the fact that once a shock is experienced, it takes a relatively high amount of effort to bring it back to a high level of discrimination ability. This high effort is required for two reasons: (1) the drop in discrimination ability following a shock of a given magnitude is more when the initial discrimination ability is higher, and (2) effort has diminishing returns at higher levels of discrimination ability. Thus, with shocks of high magnitude, it is better to operate at lower levels of discrimination ability. This result reflects a trade-off between the effort cost 4ku5ˆ and the misclassification error cost $( \phi ( x ) )$ 5 that is accumulated for a given number of shocks. While holding the system at a lower level of discrimination ability requires less effort, it also incurs higher error costs. However, the high magnitude of shocks tilts the balance in favor of reducing the cost of effort at the expense of increasing error cost. Figure 16 shows that the trade-off between the effort cost and the error cost can go the opposite way (i.e., the golden mean could be higher). Here we depict the impact of the shock mean arrival rate 45 on the discrimination ability. When shocks are of relatively small magnitude, but occur more frequently, it is better to hold the golden mean at a level that is higher than the optimal steadystate level when there are no shocks. Here, the balance shifts in favor of lowering the error cost (higher discrimination ability) but increasing the effort cost.

Figure 15 Impact of Maximum Shock Magnitude  
![](/api/attachments/8FYJWDTU/fulltext/images/cc7d9870b826c7dfbbdd61484f9b6bc4b034c3fb8645fb6fc2f84745af31d1dd.jpg)

Figure 16 Impact of Shock Arrival Rate  
![](/api/attachments/8FYJWDTU/fulltext/images/ef46ce5790782328ac05947d49f91083e7809466b1625bf2b5b1159db887079f.jpg)

## 5. Hacker Knowledge Dissemination

We present a simple model of hacker knowledge dissemination and study how the firm should optimally manage its effort to account for and suppress the dissemination of knowledge among hackers. A big difference between crime committed in the real world versus cyber crime is that hacking knowledge can easily be shared online. On the other hand, in the physical world, dissemination of knowledge by crooks may often be restricted by physical constraints. When cyber crime knowledge is disseminated (e.g., in hacker sites, blogs, etc.), it increases a firm’s costs since hackers with more knowledge can inflict greater damage. The shared knowledge could be specific to a particular firm or generic, i.e., the knowledge could be valuable for many firms. For example, generic information includes methods to evade detection, scripts, and even the tools needed to attack, whereas specific knowledge could correspond to passwords or a particular vulnerability in the firm’s detection system. Of the two, a firm could potentially influence both the impact of and the spread of firm-specific knowledge. The impact of firm-specific vulnerabilities could be controlled by monitoring discussions at hacker sites where such vulnerabilities are discussed and then promptly maintaining the system to address the vulnerability. The spread of generic knowledge may be harder to control but, to some extent, the firm may be able to slow down the dissemination of such knowledge by threatening to prosecute hackers that appear to be spreading the knowledge.

Knowledgeable hackers may be able to exploit a particular vulnerability that exists in an operating system or application. In addition, they may specifically target a firm using the special knowledge they possess, e.g., some private information that improves their chances of escaping detection, such as an accidentally revealed security procedure, or an eavesdropped password that was obtained from an insecure electronic exchange. Such knowledge may also have been obtained through network probes and other socially engineered attacks (Mitnick and Simon 2002).

## 5.1. Control Problem with Hacker Knowledge

Let y4t5, normalized between zero and one, represent the level of knowledge (both specific and general) in the hacker community. As hacker knowledge increases, the firm’s rate of cost increases given by y, where  represents a cost coefficient that captures the extent of damage that more knowledgeable hackers can inflict on the firm. The impact of maintenance effort on the change in hacker knowledge and the spread of this knowledge in the hacker community is captured by the following equation:

$$
\dot {y} = c _ {2} y (1 - y) - c _ {3} y u.
$$

The above model of hacker knowledge consists of a positive term $( c _ { 2 } y ( 1 - y ) )$ that captures the diffusion of knowledge in the hacker community. The coefficient $c _ { 2 }$ represents a knowledge diffusion coefficient that corresponds to the efficiency with which hackers disseminate information that helps them escape detection. The negative term represents the influence the firm can exert over the firm-specific knowledge of hackers. The coefficient $\displaystyle c _ { 3 } ,$ a suppression coefficient, represents the ability the firm has to suppress (or lessen the impact of) any specific knowledge hackers can obtain about its detection system. Based on the above, the new control problem with hacker knowledge can be expressed as follows:

$$
\begin{array}{r l} \min _ {u (t)} & K = \int_ {0} ^ {\infty} (\phi (x) + k \cdot u + \psi y) e ^ {- r t}   d t, \\ \text { subject   to } & \dot {x} = c _ {0} u (1 - x) - c _ {1} \delta (x), \\ & \dot {y} = c _ {2} y (1 - y) - c _ {3} y u, \\ & 0 \leq u \leq 1, \\ & x (0) = x _ {0}, \\ & y (0) = y _ {0}. \end{array}
$$

When $c _ { 3 } = 0 ,$ , the control has no impact on hacker knowledge and in steady state the value of $\hat { y }$ must equal 1. The instantaneous value function then reduces to the earlier problem without hacker knowledge because the term $\psi y = \psi$ is a constant and can be dropped from the optimization. Similarly, the problem is unchanged if $c _ { 2 } = 0$ because the steady-state value of hacker knowledge is zero. Finally, if there is no impact of hacker knowledge on the firm’s cost, i.e., if $\psi = 0 .$ , the problem remains unchanged. We therefore focus on the case where $c _ { 2 } , c _ { 3 } > 0 , \psi > 0 ,$ and analyze the impact of hacker knowledge on the steady-state behavior of the new system. The results from this analysis are summarized below.

<sup>Proposition</sup> <sup>2.</sup> The steady-state system discrimination ability 4x5ˆ in the presence of hacker knowledge is obtained by solving the equation

$$
\phi^ {\prime} (x) = \frac {(c _ {1} w (x) + r (1 - x))}{c _ {0} (- 1 + x) ^ {2}} (- k + \Omega),
$$

where

$$
\Omega = \frac {c _ {3} \psi (c _ {1} c _ {3} \delta (x) + c _ {0} c _ {2} (- 1 + x))}{c _ {2} (c _ {1} c _ {3} \delta (x) + c _ {0} (c _ {2} + r) (- 1 + x))}.
$$

The level of steady-state maintenance effort 4u5ˆ is given by

$$
\hat {u} = \frac {c _ {1} \delta (\hat {x})}{c _ {0} (1 - \hat {x})}.
$$

The corresponding steady-state level of hacker knowledge 4y5ˆ is given by

$$
\hat {y} = 1 - \frac {c _ {3} \hat {u}}{c _ {2}}.
$$

The proof is similar to the one provided in the appendix for Proposition 1. To provide an intuitive sense, we first write the Hamiltonian of the new problem as

$$
\begin{array}{c} H = \phi (x) + \psi y + k u + \lambda_ {1} (c _ {0} u (1 - x) - c _ {1} \delta (x)) \\ + \lambda_ {2} (c _ {2} y (1 - y) - c _ {3} y u). \end{array}
$$

Therefore,

$$
H _ {u} = k + \lambda_ {1} c _ {0} (1 - x) - \lambda_ {2} c _ {3} y.
$$

The set of equations that characterize steady state are, $\begin{array} { r } { \dot { x } = 0 , \dot { y } = \mathbf { 0 } , \dot { \lambda } _ { 1 } = 0 , \dot { \lambda } _ { 2 } = 0 , H _ { u } = 0 , } \end{array}$ and $\dot { H } _ { u } = 0$ Of these, the last equation is not useful as it results in an identity. Using the first five equations we can obtain steady-state solutions for the system discrimination ability 4x5ˆ , hacker knowledge $\dot { ( \hat { y } ) }$ , maintenance effort 4u5ˆ , and the two adjoint variables $( \hat { \lambda } _ { 1 } , \hat { \lambda } _ { 2 } )$

The two adjoint variables are given by

$$
\begin{array}{c} \hat {\lambda} _ {1} = \frac {f ^ {\prime} (\hat {x})}{r + c _ {0} \hat {u} + c _ {1} \delta^ {\prime} (\hat {x})}, \\ \hat {\lambda} _ {2} = \frac {\psi}{r + c _ {3} \hat {u} - c _ {2} (1 - \hat {y})}. \end{array}
$$

## 5.2. Study of Proposition 2

5.2.1. Transient Policy. We will henceforth focus on the steady-state result. However, it is necessary to show the existence of a feasible transient policy that achieves steady state. The optimal transient policy for the two state variable problems is a complex issue and not considered here. A feasible transient policy is as follows. Start with an arbitrary setting where $x ( 0 ) = x _ { 0 }$ and $y ( 0 ) = y _ { 0 } > 0 ,$ , and exert effort to take the value of the system discrimination ability to xˆ. For this, set $u = 1 , \ \mathrm { i f } x ( 0 ) < \hat { x } , \ u = 0 ,$ otherwise. Once the steady-state level xˆ is reached, exert a steady level of effort given by uˆ. At this point, the value of hacker knowledge $( y ( t ) )$ could be either less than or greater than the steady-state level yˆ. However, since a steady level of effort is being exerted, hacker knowledge must change at a rate given by $\dot { y } = c _ { 3 } y ( \hat { y } - y )$ This value of y˙ can be easily obtained by substituting the steady-state level of uˆ in the state equation for $y . \ \mathrm { I f } \ \hat { y } > y .$ , then the value of $y ( t )$ must increase; else it must decrease. Thus, either way, the value of $y ( t )$ must eventually settle at yˆ, and we will have achieved steady state in both state variables. This state of the system must continue perpetually unless the system receives shocks, an issue we studied earlier.

5.2.2. Do Hackers Benefit from Knowledge Dissemination? To study this question, we analyze the impact of knowledge dissemination on the steadystate discrimination ability that is chosen by the firm. The impact is described in Theorem 1 below.

Theorem 1. <sub>When</sub> $\Omega > 0 ,$ the steady-state level $o f$ system discrimination ability decreases if hackers stop knowledge dissemination. Conversely, when $\Omega < 0 ,$ the steady-state discrimination ability increases if hackers stop dissemination. The sign of ì is given by

$$
\Omega <   0:
$$

$$
1 - \frac {c _ {1} c _ {3} \delta (x)}{c _ {0} c _ {2}} <   x <   1 - \frac {c _ {1} c _ {3} \delta (x)}{c _ {0} (c _ {2} + r)};
$$

$$
\Omega > 0:
$$

$$
\left(x <   1 - \frac {c _ {1} c _ {3} \delta (x)}{c _ {0} c _ {2}}\right) \quad o r \quad \left(x > 1 - \frac {c _ {1} c _ {3} \delta (x)}{c _ {0} (c _ {2} + r)}\right).
$$

<sup>Proof.</sup> See the online appendix.

The above theorem has a nice interpretation. With knowledge dissemination, the term ì plays a role similar to the cost of maintenance effort 4k5 in the objective function; the new effective cost becomes $k - \Omega$ (see Proposition 2). Clearly, when the cost of maintenance effort increases, the steady-state level of discrimination ability must decrease; otherwise this value must increase. Theorem 1 implies that if the discrimination ability is very low or very high, ì is positive and discontinuing the dissemination of knowledge will benefit hackers; i.e., the discrimination ability will fall. Thus, hackers will face a weaker system (a lower value of xˆ) if they discontinue knowledge dissemination. For intermediate values of xˆ hackers face a stronger system if they discontinue knowledge dissemination. This result suggests that, over time, hackers may become reluctant to share knowledge for very weak or very strong detection systems but will do so when the detection system is of moderate strength. Of course, these claims only apply to firm-specific security knowledge, whose dissemination firms may be more successful at suppressing. Hackers always benefit from disseminating generic security knowledge.

Figure 17 provides a numerical simulation to illustrate the result in Theorem 1. In this experiment, we vary the value of the cost of effort 4k5 to obtain the different scenarios shown in Figure 17. Here, it is clear that for $\Omega < 0 ,$ x(KD) (discrimination ability with knowledge dissemination) is higher than x(NKD) (discrimination ability with no knowledge dissemination). When $\Omega > 0$ , the reverse is true.

The impact of knowledge dissemination on the steady-state level of effort can be described in the corollary below.

<sup>Corollary</sup> <sup>1.</sup> The steady-state level of effort changes in the same direction as the steady-state discrimination ability. Thus $i f \Omega > 0 ,$ the effort decreases; else $i f \Omega < 0$ the effort increases.

In Proposition 2, we showed that $\hat { u } = c _ { 1 } \delta ( \hat { x } ) /$ $\left( c _ { 0 } ( 1 - \hat { x } ) \right)$ 5. Thus $d \hat { u } / d \hat { x } = ( c _ { 1 } / c _ { 0 } ) ( w ( \hat { x } ) / ( 1 - \hat { x } ) ^ { 2 } )$ , where $w ( x ) = \delta ( x ) + ( 1 - x ) \delta ^ { \prime } ( x )$ . The interpretation of $w ( x )$ has to do with the nature of system deterioration. A positive value of w4x5 implies that the deterioration function $\delta ( x )$ is either increasing in $x \_ \mathrm { o r }$ decreasing slowly in $x .$ Note that if $\delta ( x )$ increases in $x ,$ we are dealing with a system that deteriorates more rapidly at higher levels of discrimination ability. When $\delta ( x )$ decreases slowly in $x ,$ it implies that the system deteriorates at a slower rate when the discrimination ability is higher. A negative value of $w ( x )$ implies that the system deteriorates much slower at higher levels of x. In addition $w ( x ) < 0$ also implies that higher levels of xˆ can be achieved with less effort uˆ. However, we expect the opposite, so we do not consider the case where $w ( x ) < 0$ . Hence, if $\Omega > 0$ , the effort is higher with knowledge dissemination; else if $\Omega < 0 ,$ it is lower.

Figure 17 Impact of Knowledge Dissemination  
![](/api/attachments/8FYJWDTU/fulltext/images/7ca0a7f6b1ff28d1ef3cbc351771cd7afd2113ddaba24aba973ccb69376e2c4e.jpg)

The main value of the analysis in this section is that in certain cases, the firm need not be concerned about the spread of firm-specific knowledge because hackers would have no incentive to disseminate such knowledge. This would lower the firm’s monitoring costs as well as the legal costs associated with prosecuting hackers. Of course, when the parameters of the problem are such that hackers do not benefit from disseminating firm-specific knowledge (the criterion ì is positive), the firm benefits from hackers recognizing that it is against their interests to spread firm-specific knowledge. Any action, therefore, that the firm can take to signal this fact would be advantageous.

## 6. Summary and Conclusion

Table 4 provides a summary of the results. The parameter being varied is shown on the vertical axis and the impact of increasing the value of this parameter is shown on several outcome variables on the horizontal axis. Some remarks are in order. As normal traffic 4n5 increases, all the outcomes worsen except for the false-positive rate. Increasing the hacker traffic has an opposite effect (as compared to n) on the detection rate and the false-positive rate. Increasing (or worsening) the technology parameter 4a5 degrades all the outcome variables as does increasing the cost of effort 4k5. Thus a trade-off between the cost of effort and the effectiveness of the technology is indicated. Increasing the cost of a false-negative with respect to the cost of a false-positive causes an increase in the detection rate at the expense of the false-positive rate. Finally, the deterioration parameter $\left( c _ { 1 } \right)$ and the robustness coefficient $\left( \alpha _ { 0 } \right)$ are clearly shown to be opposing forces with respect to the various outcome variables.

Table 4 Summary of Results

<table><tr><td></td><td>n</td><td>H0</td><td> $q_v$ </td><td> $c_0$ </td><td>a</td><td>k</td><td>cm/cf</td><td> $c_1$ </td><td> $α_0$ </td></tr><tr><td>Detection rate</td><td>-</td><td>+</td><td>-</td><td>+</td><td>-</td><td>-</td><td>+</td><td>-</td><td>+</td></tr><tr><td>False-positive rate</td><td>-</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>-</td><td>+</td><td>-</td></tr><tr><td>Cost</td><td>+</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+</td><td>+</td><td>+</td><td>-</td></tr><tr><td>Effort</td><td>+</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+</td><td>+</td><td>+</td><td>-</td></tr><tr><td>Hacker traffic</td><td>+</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+</td><td>-</td><td>+</td><td>-</td></tr></table>

The model and the results in this paper indicate that managing the detection component of information security requires an approach that is beyond a simple cost optimization of the detection rate and the false-positive rate of the system. These configuration decisions impact the incentives of hackers to attack the system. Hence, choosing the correct configuration (detection and false-positive rate) depends on the characteristics of the hacker population. For example, when normal traffic increases as a proportion of the total traffic, more effort is needed to maintain the system. More importantly, this effort must be directed toward lowering the false-positive rate rather than increasing the detection ability. The exact reverse holds when hackers increase as a proportion of the total traffic: while effort still increases, detection ability becomes the more important concern. When a detection system is subject to sudden shocks in the security level, the optimal decision can be to lower the security level (when the shock magnitude is high but the shocks are infrequent) or to increase it (when the shocks are frequent). Hackers always hurt the firm (increase cost) by disseminating knowledge. However, they could sometimes benefit (for very weak and very strong detection systems) by not disseminating knowledge.

An aspect of the model in this paper is that we consider the detection system to deteriorate over time. This implication is that if left without maintenance, attacks on the system can be expected to become more successful over time. Another way to interpret this modeling choice is that hackers change their attack characteristics over time: specifically, they discover novel methods of compromising the system. In reality, both effects could occur simultaneously: the hackers could attack the system in new ways and the system could get weaker (if left without maintenance). While the model in this paper did not explicitly consider how hacker attack methods change with time (except of course, that the attack rates change with time), the presence of system deterioration in the model is an aggregate way of capturing the changing characteristics of hackers and the system over time. In the future, it would be interesting to separate these two effects and explicitly study their individual and joint impacts.

## 6.1. Conclusions

We set ourselves the task of determining the optimal maintenance effort and configuration of a detection system over time. The main parameters in the model are the traffic conditions, the productivity and cost of maintenance effort, error costs, and the drift and dissemination coefficients. The objective is to optimize the effort applied to maintain the system. The effort affects the discrimination ability which, in turn, affects the detection rate and the false-positive rate of the system. The hacker traffic arriving at the firm has an endogenous component; value seeking hackers attack at a rate that is affected by the system’s detection ability.

We showed that the resulting control problem exhibits a steady-state solution where the values of effort and discrimination ability are constant in the optimal solution. The corresponding levels of the detection rate and the false-positive rate are also constant. The act of disseminating knowledge by hackers has interesting consequences. With dissemination, the total cost to the firm (error cost plus maintenance cost) always increases. Thus the firm is always worse off after dissemination. However, hackers may be better off or worse off, depending on the sign of the criterion $\Omega ( x )$ evaluated at the steady-state level of discrimination ability after dissemination.

In conclusion, managing detection systems is a multidimensional task with dynamic and endogenous features. Maintenance effort must be focused on the correct aspect of the problem considering future impacts and after accounting for the attack behavior of hackers. The firm needs to choose the discrimination ability (via the application of effort), detection rate and false-positive rate of the detection system so as to achieve a balance between the attack rate that is experienced, the learning ability of hackers (if they disseminate knowledge) and the costs of falsepositive and false-negative errors as well as the cost of maintaining the system.

An extension to the model in this study is one where the ability of hackers to disseminate knowledge depends on the attack rate. That is, if more hackers attack, then there is more knowledge to disseminate. To accommodate this feature, the state equation in the current model will need to be modified to include a term for the attack rate, $\eta ( p _ { d } )$ . Thus the detection ability $p _ { d }$ will have to be treated as another control variable, i.e., in addition to the control variable for the intensity of effort, u. Solving the new problem will be more challenging since it will require the joint optimization of two controls, u4t5 and $p _ { d } ( t )$ . Another extension is to consider situations where hackers collaborate in an attempt to penetrate the security defenses of a firm. When hackers collaborate, their actions can be considered strategic, thus suggesting a differential games framework.

## 7. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## References

Arbaugh, W., W. Fithen, J. McHugh. 2000. Windows of vulnerability: A case study analysis. Computer 33(3) 52–59.

Arora, A., R. Telang, H. Xu. 2008. Optimal policy for software vulnerability disclosure. Management Sci. 54(4) 642–656.

Bensoussan, A., R. Mookerjee, V. Mookerjee, W. Yue. 2009. Maintaining diagnositic knowledge-based systems, a control theoretic approach. Management Sci. 55(2) 294–310.

Boylu, F., H. Aytug, G. Koehler. 2010. Induction over strategic agents. Inform. Systems Res. 21(1) 170–189.

Cavusoglu, H., S. Raghunathan, H. Cavusoglu. 2009. Configuration of and interaction between information security technologies: The case of firewalls and intrusion detection systems. Inform. Systems Res. 20(2) 198–217.

Crothers, T. 2003. Implementing Intrusion Detection Systems: A Hands-On Guide for Securing the Network. Wiley Publishing, Indianapolis.

Ernst & Young. 2008. Moving beyond compliance. Ernst & Young’s 2008 global information security survey. Technical report. Ernst & Young. http://www.ey.com/Global/assets.nsf/ International/TSRS\_Global\_Information\_Security\_Survey\_2008/ \$file/TSRS\_Global\_Information\_Security\_Survey\_2008.pdf.

Evers, J. 2005. Hacking for dollars. CNET News. http://news .cnet.com/Hacking-for-dollars/2100-7349\_3-5772238.html.

Gordon, L. A., M. P. Loeb, W. Lucyshyn. 2003. Sharing information on computer systems security: An economic analysis. J. Accounting Public Policy 22 461–485.

Gupta, S., J. Winstead. 2007. Using attack graphs to design systems. IEEE Security Privacy 5(4) 80–83.

Imprivata. 2007. PCI data security standard. Imprivata. http:// www.computerworld.com/pdfs/Imprivita\_A\_Pathway\_to \_PCI\_Compliance.pdf.

Jones, A. 2007. Convergence. Inform. Security Tech. Rep. 12 69–110.

Jordan, T., P. Taylor. 1998. A sociology of hackers. Sociol. Rev. 46(4) 757–780.

Lee, W., S. Stolfo, K. Mok. 1999. A data mining framework for building intrusion detection models. IEEE Sympos. Security and Privacy 01–20. IEEE Conference Proceedings, Oakland, CA.

Lowd, A., C. Meek. 2004. Adversarial classification. Proc. 2004 Internat. Sympos. Knowledge Discovery and Data Mining (KDD 2004). Seattle, WA.

McClure, S., J. Scambray, G. Kurtz. 2005. Hacking Exposed: Network Security Secrets and Solutions. McGraw-Hill, Emeryville, CA.

Mitnick, K., W. Simon. 2002. The Art of Deception. Wiley Publishing, Indianapolis.

Scarfone, K., P. Mell. 2007. Guide to intrusion detection and prevention systems (idps). Special Publication 800-30, National Institute of Standards and Technology (NIST), Technology Administration, U.S. Department of Commerce, http:// csrc.nist.gov/publications/nistpubs/800-94/SP800-94.pdf.

Schlosser, A. E., T. B. White, S. M. Lloyd. 2006. Converting website visitors into buyers: How website investment increases consumer trusting beliefs and online purchase intentions. J. Marketing 70 133–148.

Sophos. 2008. Sophos security threat report 2008. Technical report. http://www.rsaconference.com/uploadedFiles/RSA365/Security \_Topics/Hackers\_and\_Threats/White\_Papers/Sophos/sophos -security-report-08.pdf.

Ulvila, J., J. Gaffney, Jr. 2004. A decision analysis method for evaluating computer intrusion detection systems. Decision Anal. 1(1) 35–50.

United States Government Accountability Office (U.S. Govt.). 2007. Personal information: Data breaches are frequent, but evidence of resulting identity theft is limited; however, the full extent is unknown. Technical report, http://www .gao.gov/new.items/d07737.pdf.

Yue, W., M. Cakanyildirim. 2007. Intrusion prevention in information systems: Reactive and proactive response. J. Management Inform. Systems 24(1) 329–353.

Zeller, T. 2005. Black market in stolen credit card data thrives on Internet. New York Times. http://www.nytimes.com/2005/06/ 21/technology/21data.html.
