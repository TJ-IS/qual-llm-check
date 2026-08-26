---
otero_id: 6104
otero_key: "NGH3CFX6"
title: "Advertising Strategies in Electronic Retailing: A Differential Games Approach"
authors: "Dengpan Liu; Subodha Kumar; Vijay S. Mookerjee"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0377"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/NGH3CFX6/fulltext/images/d6709ca0492335a3c2baf5e30ae23554b60d515b42f8f578b6a94a02817cdc51.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Advertising Strategies in Electronic Retailing: A Differential Games Approach

Dengpan Liu, Subodha Kumar, Vijay S. Mookerjee,

To cite this article:

Dengpan Liu, Subodha Kumar, Vijay S. Mookerjee, (2012) Advertising Strategies in Electronic Retailing: A Differential Games Approach. Information Systems Research 23(3-part-2):903-917. http://dx.doi.org/10.1287/isre.1110.0377

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/NGH3CFX6/fulltext/images/782966733404c8cc6933ff650f3f2cd662b68428b4722fa67831d26d0f28f719.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Advertising Strategies in Electronic Retailing: A Differential Games Approach

Dengpan Liu College of Business Administration, University of Alabama in Huntsville, Huntsville, Alabama 35899, dliu@iastate.edu

Subodha Kumar

Mays Business School, Texas A&M University, College Station, Texas 77843, subodha@tamu.edu

Vijay S. Mookerjee

School of Management, University of Texas at Dallas, Richardson, Texas 75080, vijaym@utdallas.edu

W<sup>e</sup> <sup>consider</sup> <sup>advertising</sup> <sup>problems</sup> <sup>under</sup> <sup>an</sup> <sup>information</sup> <sup>technology</sup> <sup>(IT)</sup> <sup>capacity</sup> <sup>constraint</sup> <sup>encountered</sup> by electronic retailers in a duopolistic setting. There is a considerable amount of literature on advertising games between firms, yet introducing an IT capacity constraint fundamentally changes this problem. In the presence of information processing constraints, although advertising may still cause a customer to switch, it may not result in a sale, i.e., the customer may be lost by both firms. This situation could occur when customers have a limited tolerance for processing delays and leave the website of a firm because of slow response. In such situations, attracting more traffic to a firm’s site (by increasing advertising expenditure) may not generate enough additional revenue to warrant this expenditure. We use a differential game formulation to obtain closedform solutions for the advertising effort over time in the presence of IT capacity constraints. Based on these solutions, we present several useful managerial insights.

Key words: IT capacity; advertising; optimal control theory; differential game; reneging; Nash equilibrium History: Senior Editor: Ram Gopal; Associate Editor: Karthik Kannan. This paper was received January 6, 2010, and was with the authors 6 months for 2 revisions. Published online in Articles in Advance September 15, 2011.

## 1. Introduction

As information technology (IT) matures and becomes an integral part of firm’s operations, its role in traditional business decisions needs to be reevaluated. This role is especially relevant for an online business when they are deciding on the optimal advertising expenditure. In this paper, we study the advertising effort for electronic retailers in a duopolistic setting.

## 1.1. Problem and Motivation

Over the last decade, the number of Internet users has increased by leaps and bounds, reaching 1.97 billion worldwide in June 2010—up from only 45 million in 1995 and 361 million in 2000 (Internet World Stats 2011). Following this rapid growth in Internet usage, the number of online shoppers has also risen dramatically. For example, more than 627 million people worldwide had shopped online by October 2005 (ACNielsen 2005). Furthermore, U.S. retail e-commerce sales grew 11% in 2009, reaching \$155.2 billion, and is expected to reach \$248.7 billion by 2014 (Mulpuru et al. 2010).

Commensurate with the increasing number of online shoppers has been an explosive growth in the number of electronic retailers worldwide (Monica 2005). An aspect of online shopping that is of interest here is the presence of processing delays at e-commerce sites. There are several potential causes of the delays associated with serving customers at an e-commerce site. Of these delays, there are some that are outside the control of the firm, e.g., the delay at the client end caused by a slow processor or network connection. The delays that can potentially be influenced by the firm’s decisions could be related to network delays caused by network devices, such as switches and routers, the network connecting to the server, or server delays caused by delays at the firm’s website (Datta et al. 2002, 2003). In this research, IT capacity refers to capacity that can be increased by the firm to reduce delays experienced by online shoppers.

There is considerable empirical evidence that processing delays indeed matter: online shoppers have been found to be very sensitive to processing delays at websites and are prone to abandon shopping if the processing speed is slow (Green 1999, Datta et al. 2003, Galletta et al. 2006). Websites with lower download delay typically have greater perceived success by site users (Palmer 2002). Around 69.4% of all potential online transactions are abandoned, and one of the biggest culprits is the poor response time associated with satisfying a request (Pastore 2001). Zona Research Study estimates that losses associated with response times of eight seconds or longer to be \$4.35 billion annually (Galletta et al. 2006), whereas the average response time for top 15 e-retailers in July 2005 was 20.16 seconds (Internet Retailer 2005). A survey shows that the consumers shopping via a broadband connection are even more impatient and will wait no more than four seconds for a Web page to render, and 33 percent of dissatisfied online shoppers attribute their dissatisfaction to the website being too slow (Jupiter Research 2006). A recent study finds that quoting the lowest price increased the overall satisfaction in only 5 percent of the top 100 online retail sites, but the site experience, especially performance, provided the biggest payback to retailers (Burns 2007).

The examples mentioned above seek to persuade the reader that information technology (IT) capacity could be a significant bottleneck in many e-commerce sites—sometimes the traffic arriving at the site may be too heavy for the installed level of IT capacity. Thus the goals of reducing delay and generating more traffic are usually in conflict with one another. More traffic can be generated through advertisement, but the higher traffic can slow down the site so that the conversion of arrivals to purchases may suffer (Jupiter Research 2006). Given that the IT capacity limitations can adversely affect the revenue of e-commerce firms (Karpinski 2000), electronic retailers must factor this constraint while choosing the optimal level of advertising. Most previous studies, however, have ignored the interaction between the IT capacity of a firm and the corresponding optimal advertising level.

## 1.2. Objective and Contributions

The goal of this paper is to optimize the advertising decisions of an electronic retailer for a given level of IT capacity in the context of a duopoly. In a typical e-commerce website, similar to a processor sharing system, the IT capacity constraint affects the processing time of requests customers submit (Mendelson 1985). This limited capacity could potentially lead to customers reneging and loss of revenue. To estimate this loss, we consider three possible outcomes of a customer’s visit (Tan and Mookerjee 2005). First, the customer may make a purchase. Second, the customer may browse the site, but at the end decide not to make a purchase because of reasons other than a slow response time. Finally, the customer may leave the website before the purchase decision because of slow response time.<sup>1</sup> In this paper, we focus on the third scenario, or customer reneging.

Several studies have shown that reducing the number of customer requests (for processing) has the single biggest impact on improving response time and reducing reneging (Rodier 2010, Souders 2007, Theurer 2006, Voigt 2002, Zensarteam 2010). If reneging is excessive, it may be better to reduce the level of advertising and divert some resources to improve response time. In the long run, both IT capacity and advertising could be simultaneously varied to address slow response time. However, in practice, IT capacity is not varied on a continuous basis because of both the relatively long lead time to procure hardware and the other technological constraints, such as the downtime incurred during an upgrade or the effort needed to test a newly upgraded site (Liu and Wee 2009). Therefore, in this study, we consider IT capacity to be fixed. Our main focus is to show that traditional advertising decisions dramatically change in the presence of IT constraints. Our model can always be re-solved if IT capacity is upgraded, but we acknowledge that not solving advertising and IT in a joint model is a limitation of this study. Section 5 provides some initial guidelines for solving such a (more general) model.

We consider IT capacity constraints at both firms and obtain optimal advertising paths (and the corresponding traffic) for the firms in equilibrium. We also analyze a situation where the IT capacities of the two firms are infinite (or unrestricted). This provides a benchmark in our study, because it corresponds to a traditional advertising problem where IT capacity constraints are ignored. Our analyses clearly demonstrate that, in the presence of IT capacity constraints, advertising strategies must be carefully managed by electronic retailers. Finally, we glean important managerial insights by studying the impact of different problem parameters on the optimal solution. To set up the dynamic model and validate our results with past studies, we begin with a monopoly case. However, our focus here is on the duopoly case.

The rest of the paper is organized as follows. In §2, we briefly review related work. In §3, we present and solve the monopoly case; §4 examines the duopoly case and discusses managerial implications. In §5, we conclude the paper and provide some directions for future research.

## 2. Literature Review

We review previous work in the following three streams that are relevant to this study: dynamic optimization of advertising effort, time sharing and customer impatience while shopping electronically, and relationship between advertising and IT capacity. In this section, we also differentiate our study from previous research and highlight its contributions.

## 2.1. Dynamic Optimization of Advertising Effort

The optimal planning of advertising effort has been widely studied in the marketing literature (see Sethi 1977a and Feichtinger et al. 1994 for extensive surveys on dynamic optimal control problems in advertising). Here we briefly discuss some of the relevant works.

The belief that advertising expenditures affect present and future demands for a product has led a number of economists to treat advertising as an investment in building advertisement capital, usually called goodwill. One of the earliest and most influential models in this regard is that of Nerlove and Arrow (1962), who optimize the advertising policy under dynamic conditions with the objective of maximizing profit. Several extensions of the Nerlove-Arrow model have also been studied in literature (Welam 1982, Rao 1985, Tapiero 1988, Erickson 2011).

Different from the Nerlove-Arrow model, a fairly large body of research does not explicitly make use of the idea of advertisement goodwill. Rather, the approach here is to exploit a closely related result found in empirical studies: the effect of advertising persists beyond the current period, but with diminishing returns (Vidale and Wolfe 1957, Telser 1962, Palda 1964). The earliest and perhaps the best known work in this direction is presented by Vidale and Wolfe (1957), who argue that the rate of change in sales depends on two effects: (i) increase in sales from advertising and (ii) loss of sales from forgetting. Sethi (1973) uses the optimal control theory to obtain an optimal advertising schedule for the Vidale-Wolfe model, whereas Sasieni (1971) uses a dynamic programming approach to characterize the optimal policy. Similar to the Nerlove-Arrow model, several extensions of the Vidale-Wolfe model have been studied (Sethi 1983, Sethi et al. 2008, He et al. 2009, Erickson 2009).

Ozga dynamics (Ozga 1960) is a system dynamics approach where the impact of advertising is affected by word of mouth effects. Gould (1970) obtains the single stable equilibrium for Ozga dynamics, Sethi (1979) shows the possibility of three equilibria in case of a linear objective function, and Feichtinger and Hartl (1986) obtain two equilibria for a nonlinear one.

Classical continuous-time models of advertising expenditure fall into the three categories (Feichtinger 1983): (i) spending occurs at a constant level, (ii) spending switches infinitely between several different levels, called chattering, and (iii) alternating between different spending levels with a finite frequency, called pulsing. There has been a great deal of interest in developing models with pulsing policies (e.g., Mahajan and Muller 1986, Feinberg 1992). This literature is inspired by the seminal work of Sasieni (1971), which studies a chattering policy.

Despite the large body of literature on dynamic optimization of advertising effort, there are some notable gaps. For example, Feichtinger et al. (1994) suggest that it is very important to build more realistic corporate models that consider the impact of other functional areas on the advertising decisions. In this direction, production and advertising decisions are considered simultaneously in several studies, e.g., see Thomas (1971), Welam (1977), Freeland (1980), Abad (1987), Sogomonian and Tang (1993), and Ulusoy and Yazgac (1995)—a detailed review on this literature is provided in Eliashberg and Steinberg (1993). The importance of more such models, interfacing advertising with other functional areas, has been highlighted in several other studies (e.g., Shapiro 1977, Abad 1982, Sethi and Zhang 1992, Dockner et al. 2000). In this paper, we intend to bridge this gap by considering the impact of IT capacity on the advertising decisions for an electronic retailer.

According to Sethi (1977a), another deficiency in extant advertising research is the paucity of studies that solve the problem completely to obtain an optimal solution. In other words, most of the research characterizes certain properties of the solution, rather than providing a closed-form solution. Here we present a closed-form solution to an advertising problem that arises in the context of electronic retailing and use this solution to derive important managerial insights.

Another important aspect of our study is the development of duopolistic model in a differential game setting. We next survey the state of research in this area and differentiate our work with the existing literature. One of the earliest models developed for a differential game in advertising is the duopoly extension of the Vidale-Wolfe model presented by Deal and Zionts (1973) and Deal (1979). Leitmann and Schmitendorf (1978) extend this model by considering a different system dynamics that is further extended by Feichtinger (1983), who uses a more generalized function of advertising effectiveness. Another influential model in this category is the Lanchester model, which can be interpreted as a competitive generalization of the Vidale-Wolfe model (Little 1979). It was introduced by Kimball (1957) based on Lanchester’s formulation of the problem of combat. Case (1979) offers an early analysis of the Lanchester model as an advertising differential game, and Sorger (1989) considers a modified version. For other studies based on the Lanchester model, the readers can refer to Erickson (1997), Fruchter and Kalish (1997), Fruchter (1999), Prasad and Sethi (2004), and Krishnamoorthy et al. (2010).

More detailed reviews of differential game models in advertising can be found in Erickson (1995), Dockner et al. (2000), and Erickson (2003). Our study contributes to the literature on duopolistic advertising literature by incorporating an IT capacity constraint that is shown to fundamentally alter the nature of the equilibrium.

## 2.2. Customer Impatience and IT Capacity

A distinguishing feature of our study is that IT capacity considerations lead to losses in the conversion of (impatient) visitors to purchasers at the electronic retailer’s website. A major cause of lost sales on an electronic retailer’s site is that the impatient buyers abandon shopping if the response time exceeds their tolerance for delay. This phenomenon has been studied extensively in the queuing area (e.g., Barrer 1957a, b; Ancker and Gafarian 1963a, b; Coffman et al. 1994; Whitt 1999). In this direction, Tan and Mookerjee (2005) derive an expression for the rate of loss of customers due to customers’ impatience. Recently, Liu et al. (2010) consider a linear cost (per unit time delay per user request) in order to model the lost revenue because of an unsatisfied visitor on a content delivery site.

To the best of our knowledge, only Tan and Mookerjee (2005) have jointly considered advertising and the IT capacity. However, their problem is static and is carried out in a monopolistic setting. The existence of two firms requires a game-theoretic framework, which makes this research fundamentally different from that of Tan and Mookerjee (2005). Moreover, we consider a dynamic model using an optimal control theory formulation as well as a differential game theory formulation in the case of a duopoly. In these models, we are able to consider the dynamic effect of the current state and decision on future states and decisions. An alternative to a dynamic model would be a myopic approach, where a static model is solved in each period based on the current state. However, the disadvantage of a myopic approach is that it does not effectively capture the dynamics of a system that evolves in time. For example, Vidale and Wolfe (1957) show that the loss of sales from forgetting at any instance depends on the arrival rate at that instance. A dynamic model can incorporate such an effect while optimizing the current and future decisions, but a myopic approach will likely be suboptimal because it would not consider the impact of the current decision on the future.

## 3. The Monopoly Case

As discussed earlier, we first consider a monopoly case to set up the model and validate our results with the past studies. We begin with some preliminaries and then present the solution.

## 3.1. Preliminaries

The basic setting of our model is as follows. The rate of advertising expenditure for an electronic retailer at time t is A4t5; this advertising effort translates into a certain level of traffic (or arrival rate) at the retailer’s website. Similar to previous studies, the firm’s advertising path is modeled as an optimal control problem, where A4t5 is the control. The objective in this problem is to maximize the total discounted profit. Next, we elaborate on two important factors in the model: (i) advertising response, and (ii) customer reneging.

3.1.1. Advertising Response. Advertising response deals with the relationship between the arrival rate and the advertising effort. As discussed earlier, several models proposed in the advertising literature allow one to express the arrival rate in terms of $A ( t )$ and other related factors. In this research, we consider the classic, widely used, Vidale-Wolfe model (Vidale and Wolfe 1957). In this model, the state variable ${ \boldsymbol x } ( t ) \in [ 0 , 1 ]$ represents the market share (i.e., the arrival rate as a fraction of the market potential or saturation level). For simplicity, the market potential in this model is usually normalized to one (Sethi 1973), and therefore we can also refer to x4t5 as the arrival rate. Recall that the rate of change in x4t5 in this model depends on two effects: (i) positive response to advertising that acts on the unsold portion of the market via the response coefficient $\beta _ { 0 } ,$ and (ii) loss of existing customers due to forgetting, obsolescence, etc., that acts via the decay coefficient $\beta _ { 1 }$ . Based on these, the system dynamics for the model can be written as Vidale and Wolfe (1957)

$$
\dot {x} (t) = \frac {d x (t)}{d t} = \beta_ {0} A (t) (1 - x (t)) - \beta_ {1} x (t), \quad x (0) = x _ {0},\tag{1}
$$

where $x _ { 0 }$ is the initial level of arrival rate (at time $t = 0 )$ . Because a firm does not have unlimited resources, the maximum allowable rate of advertising expenditure is defined as $A _ { \mathrm { m a x } }$ (Sethi 1973, Leitmann and Schmitendorf 1978). In other words, the control $A ( t ) \in [ 0 , A _ { \operatorname* { m a x } } ]$

3.1.2. Customer Reneging. On a typical e-commerce website, a new session (or connection) is opened for each entering customer and the available IT capacity is divided equally across the current number of active sessions. This type of time sharing is commonly referred to as processor sharing. The customers may be impatient and leave the site if the response time exceeds their waiting tolerance (Green 1999, Datta et al. 2003, Galletta et al. 2006)—a survey shows that the consumers shopping via a broadband connection will wait no more than four seconds for a web page to render (Jupiter Research 2006). Such loss of customers is usually referred to as reneging.

For a given IT capacity, the rate at which customers renege depends on the arrival rate and the delay tolerance of the customers as well as the processing time of their requests. In a typical e-commerce site, the IT capacity constraint represents the processing time of requests submitted by the customers (Mendelson 1985), which are handled using one or many web servers, the network connecting to the servers, network devices, and the network software. As discussed earlier, the IT capacity in this research refers to capacity that can be increased by an electronic retailer to reduce delays experienced by the customers. Hence, we use the processing rate $\mu$ to represent IT capacity—a higher value of $\mu$ reduces the time required to process a customer request.

Similar to Tan and Mookerjee (2005), we make the following reasonable assumptions in our model regarding customer reneging. First, we assume that the customers arrive at the website according to a nonhomogeneous Poisson process with mean $x ( t )$ at time t, closely representing the situation in the realworld (Moe and Fader 2004). Next, it is assumed that the processing time required by each session has a generic distribution with mean $\overset { \cdot } { 1 } / \mu$ . The processing time for a session is the sum of the processing times across the requests generated during the session, where the number of requests in a session can be variable and each request can require different amounts of processing. Hence, a generic distribution for the session processing time provides robustness to our analysis. As discussed earlier, a customer reneges if he or she is not served within  time units of arrival; the random variable  is assumed to be exponentially distributed with a mean $1 / \nu ,$ where $\nu > 0$ represents the customer impatience level Ancker and Gafarian 1963a, b. Based on these assumptions, the rate of loss of customers $( \mathrm { i . e . }$ , the number of customers that renege per unit time) at time t has been shown to be (Tan and Mookerjee 2005)

$$
L (t) = \frac {\nu x (t)}{\mu - x (t) + \nu}.\tag{2}
$$

A system with the above model of loss can be stable only when the capacity is more than the arrival rate (Tan and Mookerjee 2005). Therefore, from Equation (2), the rate of loss of customers L4t5 is always positive.

We have summarized the details and definitions of model parameters and variables for the monopoly case in Table 1.

## 3.2. Advertising Model for Monopoly

In this problem, there is a trade-off between the increase in sales revenue due to advertising and the cost of advertising. The objective is to maximize the present value of a firm’s net profit stream over an infinite horizon, a widely studied objective in the advertising literature (Sethi 1977b, Feichtinger et al. 1994). Similar to other studies, we also introduce a continuous discount rate r in the objective function for future revenues and costs. For the system dynamics given in Equation (1) and the loss rate given in Equation (2), we model the advertising problem of an electronic retailer as an optimal control problem as follows:

Table 1 Model Parameters and Variables

<table><tr><td>Symbol</td><td>Definition</td><td>Remarks</td></tr><tr><td> $h$ </td><td>Session value for the firm</td><td>Dollars per customer served</td></tr><tr><td> $r$ </td><td>Continuous discount rate</td><td>Discounts the future streams of revenues and costs</td></tr><tr><td> $\beta_0$ </td><td>Advertising response coefficient</td><td>A higher value indicates that the same level of advertising attracts more customers</td></tr><tr><td> $\beta_1$ </td><td>Demand decay coefficient</td><td>The rate at which existing customers are lost due to forgetting, obsolescence, etc.</td></tr><tr><td> $x(t)$ </td><td>Arrival rate</td><td>State variable</td></tr><tr><td> $x_0$ </td><td>Initial level of arrival rate</td><td>Arrival rate at  $t = 0$ </td></tr><tr><td> $L(t)$ </td><td>Loss rate</td><td>The rate at which customers renege</td></tr><tr><td> $x_{eff}(t)$ </td><td>Effective arrival rate</td><td>Rate of customers that complete the transaction (or do not renege)</td></tr><tr><td> $\nu$ </td><td>Customer impatience level</td><td>A higher value implies that the customer is more impatient</td></tr><tr><td> $\mu$ </td><td>IT capacity (i.e., processing rate) for the firm</td><td>A higher value reduces the time to process a request</td></tr><tr><td> $A(t)$ </td><td>Advertising expenditure rate</td><td>Decision variable</td></tr><tr><td> $A_{\max}$ </td><td>Maximum allowable rate of advertising</td><td> $0 \leq A(t) \leq A_{\max}$ </td></tr><tr><td> $c$ </td><td>Subscript denoting the values in the finite IT capacity case</td><td></td></tr><tr><td> $u$ </td><td>Subscript denoting the values in the infinite IT capacity case</td><td></td></tr></table>

$$
\max _ {A (t)} \left\{\int_ {0} ^ {\infty} \left[ h \left(x (t) - \frac {x (t) \nu}{\mu - x (t) + \nu}\right) - A (t) \right] e ^ {- r t} d t \right\},\tag{3}
$$

with the following constraint: $0 \leq A ( t ) \leq A _ { \operatorname* { m a x } } .$

The advertising expenditure in the objective function is linear in the control, a feature of the model that is consistent with the models by Sasieni (1971), Sethi (1973), and Tapiero (1975). For notational convenience, we will suppress time (t) as an argument unless there is potential for confusion.

Before presenting the closed-form optimal solution for this problem (see Theorem 1), we define

$$
\hat {A} _ {c} = \frac {\beta_ {1} \hat {x} _ {c}}{\beta_ {0} (1 - \hat {x} _ {c})},\tag{4}
$$

where $\hat { x } _ { c } = x$ is obtained from the solution $\mathrm { o f } ^ { 2 }$

$$
h \bigg [ 1 - \frac {\nu (\mu + \nu)}{(\mu - x + \nu) ^ {2}} \bigg ] = \frac {\beta_ {1} + r (1 - x)}{\beta_ {0} (1 - x) ^ {2}}.\tag{5}
$$

We use ∧ to denote values in the singular region, i.e., $\hat { A } _ { c }$ is the advertising expenditure rate in the singular region and $\hat { x } _ { c }$ is the arrival rate in the singular region. Also, we use the subscripts c and u to denote the values in the finite IT capacity case and the unlimited (i.e., infinite) IT capacity case, respectively. Proofs for all the theorems are presented in the electronic companion.<sup>3</sup>

Theorem 1. <sub>When</sub> $\hat { x } _ { c } > 0$ and $\hat { A } _ { c } \leq A _ { \operatorname* { m a x } } ,$ the optimal solution to the problem with IT capacity constraints has two cases:<sup>4</sup>

$x _ { 0 } \leq \hat { x } _ { c } .$ . In this case, the optimal control is to use $A ^ { * } =$ $A _ { \mathrm { m a x } }$ (maximum advertising expenditure rate) until x increases from $x _ { 0 }$ to $\hat { x } _ { c } ,$ , and $\bar { \boldsymbol { A } } ^ { * } = \hat { \boldsymbol { A } } _ { c }$ afterward.

$x _ { 0 } > \hat { x } _ { c } .$ . In this case, the optimal control is to use $A ^ { * } = 0$ until x decreases from $x _ { 0 }$ to $\hat { x } _ { c } ,$ and $A ^ { * } = \hat { A } _ { c }$ afterward.

Figure 1 illustrates the two cases of the solution given in Theorem 1. Note that the second region in these figures (where $A ^ { * } = \hat { A } _ { c } )$ is referred to as the singular region, or the steady-state region. When the arrival rate reaches the steady state level $\hat { x } _ { c } ,$ the advertising expenditure rate stays at a constant level ensuring that the arrival rate also stays constant.

## 3.3. Discussions and Managerial Implications

We first examine how the singular levels of advertising expenditure rate $( \mathrm { i } . \mathrm { e } . , \ \hat { A } _ { c } ( t ) )$ , arrival rate $( \mathrm { i . e . , }$ $\hat { x } _ { c } ( t ) \bar { ) }$ , and effective arrival rate $( \mathrm { i . e . , ~ } \hat { x } _ { e f f } ( t ) )$ change with the IT capacity. Here, the effective arrival is defined as the rate of customers that complete the transaction (or do not renege), i.e., $\hat { x } _ { e f f } ( t ) \bar { = } \hat { x } _ { c } ( t ) -$ L4t5. Note that the revenue for an electronic retailer depends directly on the effective arrival rate.

<sup>Theorem</sup> <sup>2.</sup> The singular levels of advertising expenditure rate, arrival rate, and effective arrival rate increase with the IT capacity level $( i . e . , ~ \mu )$ . However, these values saturate as $\mu \stackrel { \cdot } {  } \infty . ^ { 5 }$ More specifically, the singular levels of arrival rate and advertising expenditure rate at $\mu \to \infty$ are

Figure 1 Solution Structure in Theorem 1  
![](/api/attachments/NGH3CFX6/fulltext/images/0e20f72cc5471ca797e3bc2af276f9c2a4f0a90369c2b0e82c59a000f6602659.jpg)

![](/api/attachments/NGH3CFX6/fulltext/images/c4f3fdeb8c10ca30df4bb44234c03d69a1ceed1942412e5b4581abc6d9511890.jpg)

$$
\begin{array}{r l} \hat {x} _ {u} = \max \bigg \{\frac {2 \beta_ {0} h - r - \sqrt {4 h \beta_ {0} \beta_ {1} + r ^ {2}}}{2 \beta_ {0} h}, 0 \bigg \} & a n d \\ \hat {A} _ {u} = \frac {\beta_ {1} \hat {x} _ {u}}{\beta_ {0} (1 - \hat {x} _ {u})}. \end{array}\tag{6}
$$

The above theorem suggests that it is optimal for a firm to operate at lower demand levels when the IT capacity is not high—an important result for managers. Next, we briefly discuss the solution during the transient phase (i.e., the solution before steady-state as described in Theorem 1). In this phase, when $\hat { x } _ { c } <$ $x _ { 0 } < \hat { x } _ { u } ,$ the solution is zero advertising for the finite IT capacity but maximum advertising for $\mu \to \infty$ . Moreover, because the singular arrival rate increases with the IT capacity level (as shown in Theorem 2), we have $\hat { x } _ { c } \le \hat { x } _ { u }$ . Therefore, we can also conclude that the steady-state region starts earlier (no later) for $\mu \to \infty$ (as compared with the case, when $\mu$ is finite) when $x _ { 0 } > \hat { x } _ { u } .$ In contrast, the stead-state region starts later (no earlier) for $\mu \to \infty$ when $x _ { 0 } < \hat { x } _ { c }$

In summary, our analysis shows that the optimal trajectory is significantly affected by the inclusion of IT capacity constraints in the optimization problem.

Unless the capacity is so high that the constraint is rendered nonbinding, the optimal adjustment in the trajectory is to reduce advertising efforts, by reducing the steady state level, by maintaining it at the maximum level for a shorter duration, or by prolonging the zero-effort period. This result is very pertinent for electronic retailers who must consider IT capacity limitations and curb their advertising to match the IT processing capabilities of the e-commerce site. This result is also consistent with that of Tan and Mookerjee (2005), who show that marketing will overspend on advertising when the two departments (IT and marketing) make decisions in an uncoordinated manner. In the next section, we turn our attention to the duopoly case which is the key focus of this paper.

## 4. Duopoly Case

In the monopoly case, the rate of change in the arrival rate of a firm depends only on its own advertising rate and the current arrival rate (see Equation (1)). However, in the presence of a second firm, this arrival rate is also affected by the advertising rate of the other firm. In this section, we model such a scenario and derive open-loop Nash equilibrium levels of advertising for the two firms.

In an open-loop strategy, the optimal control $( \mathrm { i . e . , }$ the optimal advertising rate in our problem) is determined as a function of time. This strategy has been widely studied in marketing and operations management literature. In the open-loop strategy, the firms choose their optimal path at the beginning of the game (at time zero) and commit to it for the entire duration of the game. A limitation of open-loop solution is that the firms may have an incentive to deviate to a different path at a future time if given such an opportunity. Another possible strategy is a feedback Nash strategy, where the optimal control is determined as a function of both the time and the state. In the presence of more than one firm, the feedback Nash strategy provides more general solutions because it allows firms to react to the current state. However, the feedback Nash strategy is more difficult to implement because the firms need to observe the state constantly and use it as an input to obtain the optimal control at any point in time (Dockner et al. 2000). In contrast, an open-loop strategy requires only the knowledge of current time to obtain the optimal control. Moreover, obtaining a feedback Nash strategy is usually quite difficult, and closed-form solutions are known for very few models (Dockner et al. 2000). Hence, we use an open-loop strategy in this paper and present a closed-form solution. Based on this solution, we are able to provide several useful managerial insights. Nonetheless, we acknowledge this as a limitation of the study and discuss this issue in $\ S 5 .$

Similar to the previous section, where an IT capacity constraint was enforced, we consider both firms with limited IT capacity. As discussed earlier, previous research on duopoly models of advertising do not consider IT capacity (Dockner et al. 2000, Erickson 2003). An important aspect of the limited IT capacity problem that distinguishes it from many past studies is that the actions of the two players no longer constitute a zero-sum game. With limited IT capacity, when customers are lost by one firm, an equal amount is not gained by the other firm, because these customers could once again renege because of slow processing.

## 4.1. Advertising Response Function

The problem studied here is a differential game with two players that are electronic retailers in the same market and sell the same (or a substitute) product. Similar to the monopoly case, the market potential is normalized to one. However, customers may renege from both firms because of IT capacity limitations. Hence, the market is not fully covered in our model. Here, the state variable ${ \boldsymbol { x } } ( t ) \in [ 0 , 1 ]$ represents the arrival rate of firm 1 at time t and $( 1 - x ( t ) )$ is the arrival rate of firm 2. The control $A _ { i } ( t )$ refers to adverting expenditure rate for firm i at time $t , i = 1 , 2 .$ Similarly, the other notations are also extended from the monopoly case, with subscript $^ { \prime \prime } i ^ { \prime \prime }$ for firm i.

For the duopoly case, we use the classical Lanchester model, which was introduced by Kimball (1957) based on Lanchester’s formulation of the problem of combat (Lanchester 1916). Case (1979) offers an early analysis of the Lanchester model as an advertising differential game. Since then, it has been studied by several researchers, as discussed in §2. An interesting aspect of the Lanchester model is that the gains and losses in sales are attributed directly to competitive advertising by the firms. The Lanchester model explicitly recognizes the dynamic nature of shifting market shares via changes in the advertising expenditure. The value of the Lanchester model is that it captures both the dynamic and the competitive aspects of markets.

The Lanchester model adopted by Case (1979) assumes that the market share of firm 1 is affected by two factors: (i) positive direct response to its own advertising (via the advertising response coefficient $\eta _ { 1 } ,$ which is also referred to as the advertising effectiveness) on the unsold portion of the market, and (ii) the loss of existing customers due to advertising from firm 2 (via the decay coefficient $\eta _ { 2 } )$ . Based on these, the system dynamics can be written as

$$
\dot {x} (t) = \frac {d x (t)}{d t} = (1 - x) \eta_ {1} A _ {1} - x \eta_ {2} A _ {2}, \quad x (0) = x _ {0},\tag{7}
$$

where $x _ { 0 }$ is the initial level of market share for firm 1 (at time $t = 0 )$ . The maximum allowable rate of advertising expenditure for each firm is defined as $A _ { \mathrm { m a x } } .$

Figure 2 Process of Arrival and Reneging in Duopoly at Time t  
![](/api/attachments/NGH3CFX6/fulltext/images/f4c2dc5c34b81be260b66283ecdcfbb57cb2e183dd8f1499b90328548ab0e25c.jpg)

Similar to the monopoly case, the customers renege from firm i at rate $\hat { L } _ { i } , \stackrel { \cdot } { i } = 1 , 2$ (see Equation (2)). Hence, the effective arrival rate (defined as the rate of customers that complete the transaction) for firms 1 and 2 can be written as $x _ { 1 e f f } = ( x - L _ { 1 } )$ and $x _ { 2 e f f } =$ $( ( 1 - x ) - L _ { 2 } )$ , respectively. Figure 2 illustrates this process of arrival and reneging at time t.

## 4.2. Advertising Model for Duopoly

In this section, we obtain the equilibrium advertising strategy of two firms when they have limited IT capacity. We restrict our analysis in this section to the steady-state component of the solution. Let the IT capacities (i.e., processing rates) for firms 1 and 2 be $\mu _ { 1 }$ and $\mu _ { 2 } ,$ respectively. Using the loss function given in Equation (2), the objective functions for firms 1 and 2 can be written as

$$
\begin{array}{c} \max _ {A _ {1} (t)} \bigg \{\int_ {0} ^ {\infty} \bigg [ h \bigg (x (t) - \frac {x (t) \nu}{\mu_ {1} - x (t) + \nu} \bigg) - A _ {1} (t) \bigg ] e ^ {- r t}   d t \bigg \}, \\ \max _ {A _ {2} (t)} \bigg \{\int_ {0} ^ {\infty} \bigg [ h \bigg (1 - x (t) - \frac {(1 - x (t)) \nu}{\mu_ {2} - (1 - x (t)) + \nu} \bigg) \\ - A _ {2} (t) \bigg ] e ^ {- r t}   d t \bigg \}. \end{array}
$$

Hence, the current-value Hamiltonians are

$$
\begin{array}{l} H _ {1} = \lambda_ {1} [ \eta_ {1} A _ {1} (1 - x) - \eta_ {2} A _ {2} x ] \\ \qquad + h \left(x - \frac {x \nu}{\mu_ {1} - x + \nu}\right) - A _ {1}, \quad \text { and } \\ H _ {2} = \lambda_ {2} [ \eta_ {1} A _ {1} (1 - x) - \eta_ {2} A _ {2} x ] \\ \qquad + h \left(1 - x - \frac {(1 - x) \nu}{\mu_ {2} - (1 - x) + \nu}\right) - A _ {2}, \end{array}
$$

where $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are the current-value adjoint variables for firms 1 and $^ { 2 , }$ respectively. We can rewrite the Hamiltonians as

$$
H _ {1} = - \lambda_ {1} \eta_ {2} A _ {2} x + h \left(x - \frac {\nu x}{\mu_ {1} - x + \nu}\right)\tag{8}
$$

$$
\begin{array}{c} + (H _ {1}) _ {A _ {1}} A _ {1}, \quad \text { and } \\ H _ {2} = \lambda_ {2} \eta_ {1} A _ {1} (1 - x) + h \bigg (1 - x - \frac {\nu (1 - x)}{\mu_ {2} - (1 - x) + \nu} \bigg) \\ + (H _ {2}) _ {A _ {2}} A _ {2}, \end{array}\tag{9}
$$

where

$$
\begin{array}{c} (H _ {1}) _ {A _ {1}} = \eta_ {1} \lambda_ {1} (1 - x) - 1 \quad \text { and } \\ (H _ {2}) _ {A _ {2}} = - \eta_ {2} \lambda_ {2} x - 1. \end{array}\tag{10}
$$

The Pontrayagin necessary conditions (Arrow and Kurz 1970) are

$$
\begin{array}{r l} \dot {\lambda} _ {1} = & \frac {d \lambda_ {1}}{d t} = r \lambda_ {1} - \frac {\partial H _ {1}}{\partial x} = r \lambda_ {1} - (- \eta_ {1} A _ {1} \lambda_ {1} - \eta_ {2} A _ {2} \lambda_ {1}) \\ & + \frac {h \nu (\mu_ {1} + \nu)}{(\mu_ {1} - x + \nu) ^ {2}} - h \end{array} \tag {1}\tag{11}
$$

$$
\begin{array}{c} \dot {\lambda} _ {2} = \frac {d \lambda_ {2}}{d t} = r \lambda_ {2} - \frac {\partial H _ {2}}{\partial x} = r \lambda_ {2} - (- \eta_ {1} A _ {1} \lambda_ {2} - \eta_ {2} A _ {2} \lambda_ {2}) \\ - \frac {h \nu (\mu_ {2} + \nu)}{(\mu_ {2} - (1 - x) + \nu) ^ {2}} + h. \end{array}\tag{12}
$$

From Equations (8)–(10), we can see that the Hamiltonians are linear in the control variables. Therefore, we have the following bang-bang and singular solution form for $A _ { 1 }$ and $A _ { 2 } { \mathrm { : } }$

$$
\begin{array}{l} A _ {1} = \left\{ \begin{array}{l l} 0, & \text { if } (H _ {1}) _ {A _ {1}} <   0 \\ \text { To   be   determined }, & \text { if } (H _ {1}) _ {A _ {1}} = 0, \\ A _ {\max}, & \text { if } (H _ {1}) _ {A _ {1}} > 0 \end{array} \right. \\ A _ {2} = \left\{ \begin{array}{l l} 0, & \text { if } (H _ {2}) _ {A _ {2}} <   0 \\ \text { To   be   determined }, & \text { if } (H _ {2}) _ {A _ {2}} = 0 \\ A _ {\max}, & \text { if } (H _ {2}) _ {A _ {2}} > 0. \end{array} \right. \end{array}\tag{13}
$$

The singular region (given in Theorem 3 below) can now be derived from Equations (7)–(13) and the following conditions: $( H _ { i } ) _ { A _ { i } } = 0$ and $( \dot { H } _ { i } ) _ { A _ { i } } =$ $d ( H _ { i } ) _ { A _ { i } } / d t = \breve { 0 } , i = 1 , 2$

Theorem 3. <sub>When</sub> $0 \leq \hat { A } _ { 1 c } \leq A _ { \operatorname* { m a x } } , \ 0 \leq \hat { A } _ { 2 c } \leq A _ { \operatorname* { m a x } } ,$ and $0 < \hat { x } _ { 1 c } \le 1$ , the steady-state equilibrium strategy for the advertising problem with IT capacity constraints for duopoly case $i \bar { s } ^ { 6 }$

$$
A _ {1} ^ {*} = \hat {A} _ {1 c} = \frac {\eta_ {2}}{\eta_ {1}} h \hat {x} _ {1 c} ^ {2} \left(1 - \frac {\nu (\mu_ {2} + \nu)}{(\mu_ {2} - (1 - \hat {x} _ {1 c}) + \nu) ^ {2}}\right)
$$

$$
\begin{array}{r l r} & & {- \frac {r \hat {x} _ {1 c}}{\eta_ {1}}, \quad a n d} \\ & & {A _ {2} ^ {*} = \hat {A} _ {2 c} = \frac {\eta_ {1}}{\eta_ {2}} h (1 - \hat {x} _ {1 c}) ^ {2} \bigg (1 - \frac {\nu (\mu_ {1} + \nu)}{(\mu_ {1} - \hat {x} _ {1 c} + \nu) ^ {2}} \bigg)} \\ & & {- \frac {r (1 - \hat {x} _ {1 c})}{\eta_ {2}},} \end{array}\tag{14}
$$

where $\hat { x } _ { 1 c }$ is the arrival rate of firm 1 in the steady state, which is given by the solution of x in

$$
\begin{array}{c} \eta_ {2} x \bigg (1 - \frac {\nu (\mu_ {2} + \nu)}{(\mu_ {2} - (1 - x) + \nu) ^ {2}} \bigg) \\ - \eta_ {1} (1 - x) \bigg (1 - \frac {\nu (\mu_ {1} + \nu)}{(\mu_ {1} - x + \nu) ^ {2}} \bigg) = 0. \end{array}\tag{15}
$$

## 4.3. Discussion of the Duopoly Case

In this section, we present several important managerial insights based on the solution obtained for the duopoly case. We begin with studying the impact of the IT capacity level.

4.3.1. Impact of the IT Capacity Level. In the following theorem, we examine how the IT capacity level of one firm affects the solution in the singular region for both firms.

<sup>Theorem</sup> <sup>4.</sup> With an increase in the IT capacity level of one firm:

• The singular levels of arrival rate, effective arrival rate, and advertising expenditure rate for the same firm increase. However, these values saturate when the IT capacities are infinite $( i . e . , \mu _ { 1 } $  and $\mu _ { 2 } \to \infty )$ . More specifically, the singular levels of advertising expenditure rates and arrival rate at infinite IT capacity levels $a r e ^ { 7 }$

$$
\begin{array}{c} \hat {A} _ {1 u} = \hat {A} _ {2 u} = \frac {h \eta_ {1} \eta_ {2}}{(\eta_ {1} + \eta_ {2}) ^ {2}} - \frac {r}{\eta_ {1} + \eta_ {2}} \quad a n d \\ \hat {x} _ {1 u} = \frac {\eta_ {1}}{\eta_ {1} + \eta_ {2}}, r e s p e c t i v e l y. \end{array}\tag{16}
$$

• The singular levels of arrival rate and effective arrival rate of the other firm decrease.

• The singular level of advertising expenditure rate for the other firm may increase or decrease based on a given condition that is provided in the electronic companion.

Note that the advertising expenditure rate in the singular region becomes identical for the two firms when the IT capacities are infinite, whereas they are different when the IT capacities are limited. Also, the advertising expenditure rate of a firm decreases with a reduction in its IT capacity level. This result is intuitive: when the IT capacity is lower, the firms need to limit the arrival rate to reduce reneging, and they do so by lowering the advertising rate. Finally, we find that a change in IT capacity at one firm not only affects its own advertising effort and arrival rate, but also impacts these decisions for its competitor. These results highlight that competition for market share between two electronic retailers is mediated by IT factors, specifically the IT capacity installed at the two firms.

We refer to the dominance level of firm i (denoted by $\Delta _ { i } )$ as the difference between the arrival rate of firm i and that for the other firm. Hence, the dominance level of firm 1 is $\Delta _ { 1 } = \hat { x } _ { 1 c } - ( 1 - \hat { x } _ { 1 c } ) = 2 \hat { x } _ { 1 c } - 1$ Similarly, the dominance level of firm 2 is $\Delta _ { 2 } =$ $( 1 - \hat { x } _ { 1 c } ) ^ { \dot { } } - \hat { x } _ { 1 c } = 1 - 2 \hat { x } _ { 1 c }$ . The following result directly follows from Theorem 4.

<sup>Corollary</sup> <sup>1.</sup> The dominance level of a firm increases with its IT capacity level, given that the IT capacity level of its competitor is held constant.

Next, we study the impact of the IT capacity of a firm on the total effective arrival rate of the system, which is defined as $\begin{array} { r } { X _ { e f f } = \sum _ { i = 1 } ^ { 2 } \hat { x } _ { i , e f f } , } \end{array}$ where $\hat { x } _ { i , e f f }$ is the effective arrival rate of firm i in the singular region. When the IT capacity constraint is not considered in the traditional advertising problem, the loss of one firm is always the gain of the other; i.e., the fraction of customers served is always equal to one. However, this is not necessarily so in the presence of IT capacity constraints, because customers may renege. Hence, in this case, it is pertinent to analyze the total effective arrival rate of the system—the fraction of customers who finish transactions (or do not renege).

<sup>Theorem</sup> <sup>5.</sup> When the equilibrium arrival rate of firm i is greater than $\eta _ { i } / ( \eta _ { 1 } + \eta _ { 2 } )$ , the equilibrium effective arrival rate of the system $( i . e . , \ X _ { e f f } )$ increases with an increase in the IT capacity of firm $i , i = 1 , 2$ . However, when this condition is not satisfied, increasing the IT capacity of firm i may decrease the equilibrium effective arrival rate of the system.

This theorem presents an interesting and somewhat counterintuitive result that is contrary to general belief that an increase in IT capacity should always benefit customers. As shown in Theorem 4, it is indeed beneficial for a firm to increase its IT capacity. However, Theorem 5 shows that if the equilibrium arrival rate of a firm is below a certain threshold, increasing its IT capacity may negatively impact the equilibrium effective arrival rate of customers across the two firms. This result is illustrated in Figure 3 using an example. In this example, $\eta _ { 1 } = 0 . 5 , \ \eta _ { 2 } = 0 . 4 ,$ $\mu _ { 2 } = 3$ 1 and $\nu = 0 . 3$ . We can observe that although the equilibrium arrival rate of firm 1 is lower than the threshold $\eta _ { 1 } / ( \eta _ { 1 } + \eta _ { 2 } ) = 0 . 5 6$ , the equilibrium effective arrival rate of the system can increase or decrease; i.e., it can be nonmonotonic.

Figure 3 Impact of IT Capacity on Equilibrium Arrival Rates  
![](/api/attachments/NGH3CFX6/fulltext/images/721c0a3b862302f142ab94d69df271c38253b51cc8d2331f596b30d0883ac998.jpg)

The above result can be explained as follows. According to Theorem 4, whenever a firm increases its capacity, it advertises more in order to attract more customers from the other firm. This increased advertising has a greater impact on its equilibrium arrival rate when the equilibrium arrival rate of the firm is below a certain threshold (see Equation (7)). In that case, the equilibrium arrival rate increases rapidly with an increase in the capacity. Because of the fast increase in equilibrium arrival rate, the reneging rate also increases and the equilibrium effective arrival rate of the system may decrease. This may happen despite the fact that the reneging (or loss) rate at the other firm decreases. In contrast, when the equilibrium arrival rate of the firm is above this threshold, the equilibrium arrival rate increases slowly with an increase in the IT capacity and the equilibrium effective arrival rate of the system always increases.

Theorem 5 implies that increasing $\mu _ { 1 }$ may decrease $X _ { e f f }$ when $\hat { x } _ { 1 c } < \eta _ { 1 } / ( \eta _ { 1 } + \eta _ { 2 } )$ . Since the equilibrium arrival rate $\hat { x } _ { 1 c }$ is endogenous, we now analyze when this condition is satisfied. Our numerical study shows that $\hat { x } _ { 1 c } < \eta _ { 1 } / ( \eta _ { 1 } + \eta _ { 2 } )$ when both $\mu _ { 2 }$ and  are high. In summary, increasing the IT capacity of firm 1 may decrease the equilibrium effective arrival rate of the system when the customers are highly impatient and the IT capacity of firm 2 is high. Clearly, the reneging rate at firm 2 can be expected to be low when its IT capacity is high (see Theorem 4). In this case, when impatient customers are drawn away from firm 2 to firm 1 (by more advertising following an increase in IT capacity at firm 1), the increase in the reneging rate at firm 1 may not be compensated by the reduction in this rate at firm 2. Therefore, the equilibrium effective arrival rate of the system can decrease.

The main take-away from the above discussion is that without capacity constraints, there is no negative impact on consumers in the advertising game; each firm tries to attract more traffic, but at the end, each consumer is served by either of the two firms. However, when a similar advertising game is enacted in the presence of capacity constraints, the equilibrium levels of advertising could not only hurt the profits of the firms, but more capacity could reduce the equilibrium effective arrival rate of the system. In this scenario, a policy maker may want to intervene by introducing some mechanisms that ease wasteful advertising expenditures (e.g., by imposing a Pigovian tax).

Now we analyze how the effective arrival rate of the system changes when the problem is solved from the perspective of the social planner. The social planner optimizes the advertising rates of both firms with the objective of maximizing the sum of objective functions of two firms. In Figure 4, we compare the effective arrival rates of the system in the equilibrium solution and in the optimal solution. Clearly, this figure shows that the effective arrival rate of the system is lower in the equilibrium solution. Figure 4 also indicates that, in the optimal solution, the effective arrival rate of the system always increases with an increase in the IT capacity of firm 1. Hence, as mentioned earlier, a policy maker may want to intervene to ensure that an optimal or a near-optimal solution is achieved in the system.

4.3.2. Impact of the Advertising Effectiveness. Next, we study the impact of another important parameter on the advertising decision, namely, the advertising effectiveness.

<sup>Theorem</sup> <sup>6.</sup> With an increase in the advertising effectiveness of firm $i ~ ( i . e . , ~ \eta _ { i } )$ ):

• The singular levels of arrival rate and effective arrival rate of firm i increase.

• The singular levels of arrival rate and effective arrival rate of the other firm decrease.

• When the arrival rate of firm i is greater than $\eta _ { i } / ( \eta _ { 1 } + \eta _ { 2 } ) , i = 1 , 2 ,$ the total effective arrival rate of the system increases. Otherwise, the total effective arrival rate of the system decreases.

The first result in this theorem shows that the firm can attract more customers with an increase in its advertising effectiveness. Also, as shown in the second result, the gain of one firm results in the loss of the other firm (although the magnitudes of the quantities are not the same). The third result is interesting and is contrary to the general notion that an increase in effectiveness is always better. This is analogous to the result presented in Theorem 5 and can be explained in a similar manner.

Figure 4 Impact of IT Capacity on Effective Arrival Rate of the System  
![](/api/attachments/NGH3CFX6/fulltext/images/e971b070ce3fb1f8ba2e35d570a87a70fb7579999ae02c90da4654fce4fb2fce.jpg)

Because the marginal benefit of advertising increases with an increase in the advertising effectiveness, we would expect $A _ { i }$ to increase with $\eta _ { i }$ . However, when the marginal cost of advertising exceeds the marginal benefit, the firm will reduce its advertising level. Because of these two opposing effects, we find that the advertising expenditure rate does not increase monotonically with advertising effectiveness. This result is shown in Figure 5 using $\eta _ { 2 } = 0 . 4 , \mu _ { 1 } =$ $\mu _ { 2 } = 3 , \nu = 0 . 5 ,$ and $h = 1$

In this figure, the marginal benefit is more than the marginal cost of advertising when the advertising effectiveness is low, whereas the reverse is true at higher levels of advertising effectiveness. As a result, the advertising rate increases with the advertising effectiveness at the lower level of advertising effectiveness, whereas it decreases at the higher level of advertising effectiveness. Basically, the result can be explained in the following economic terms. When the effectiveness of a resource initially increases, more of it gets used because its marginal benefit continues to be higher than the cost. But as further use of it is made, diminishing returns set in, and its use begins to decrease in an optimal solution.

4.3.3. Impact of Customer Impatience. In this section, we numerically examine the impact of customer impatience on the singular levels of market share and advertising expenditure rates. Here, we use $\eta _ { 1 } = 0 . 5 , \ \eta _ { 2 } = 0 . 4 , \ \mu _ { 1 } = 3$ , and h = 1. Note that the advertising effectiveness is higher for firm 1 in this experiment, because $\eta _ { 1 } > \eta _ { 2 }$

First, in Figure $^ { 6 , }$ we analyze the impact of the impatience parameter and IT capacity levels on the dominance level of firm 1. Figure 6(a) shows that as customers become more impatient when firm 1 has higher (respectively, lower) IT capacity than firm 2, the dominance level (and the arrival rate) of firm 1 increases (respectively, decreases). Also, the arrival rate of both firms remains almost stable with a change in the impatience parameter when both firms have the same IT capacity level $( \mathrm { i . e . , ~ } \mu _ { 1 } = \mu _ { 2 } = 3 )$ . This result indicates that the higher capacity firm gains (in terms of both the arrival rate and the dominance level) when customers are more impatient. In Figure 6(b), we plot the dominance level of firm 1 in effective arrival rate, which is defined as $\Delta _ { 1 e f f } = \hat { x } _ { 1 e f f } -$ $\hat { x } _ { 2 e f f }$ . The results in this figure exhibit similar characteristics to those in Figure 6(a).

Figure 5 Impact of Advertising Effectiveness on the Singular Advertising Expenditure Rates  
![](/api/attachments/NGH3CFX6/fulltext/images/48e74bb3b23f8ee01432fcb13a3fc52267d786d6c3a921b245f32407a6d43a14.jpg)

Figure 6 Impact of Impatience Parameter on the Dominance Level  
![](/api/attachments/NGH3CFX6/fulltext/images/55671dd082f5a9df0ff1377413068fcf100586e9ba7dddc02a58ec7557437099.jpg)

(b) Dominance level in effective arrival rate  
![](/api/attachments/NGH3CFX6/fulltext/images/4ae12ecbf076565a2b6227dff30755ab34bb890359b66bcb4e2cff59ac0ceca3.jpg)

Further, in Figure $^ { 7 , }$ we analyze the impact of customer impatience on the effective arrival rates of the two firms. The results show that the effective arrival rates of both firms decrease as customers become more impatient. This result holds irrespective of the IT capacity levels of the firms. Observing the results of Figures 6(a) and 7 together, we can conclude that as the impatience level increases, the increase in reneging for the higher capacity firm is more than the increase in its arrival rate. Unless the possibility of market expansion is considered, in traditional advertising problems, the loss of one firm is always the gain of the other firm; $\mathrm { i . e . , }$ the total loss in the system is zero. In contrast, Figure 7 shows that there is a positive loss in the system (in terms of the number of customers finishing the transaction) in presence of the IT capacity constraint, because customers can renege. This is an important result for managers because it

## Figure 7 Impact of Impatience Parameter on Effective Arrival Rate

![](/api/attachments/NGH3CFX6/fulltext/images/e59080531dcc1fdccdefaa5b07ad7cb8eeb0113f6d7977a36dbb253828c8c054.jpg)

(b) Effective singular arrival rate of firm 2  
![](/api/attachments/NGH3CFX6/fulltext/images/a864af90a97d2bedfb9d1023387ee0fe886d59f4c15a4b7d74b7b714a53341dc.jpg)

highlights the significance of considering IT capacity constraints and customer behavior at e-commerce sites in what are traditionally considered to be pure marketing decisions.

In Figure $^ { 8 , }$ we set $\mu _ { 2 } = 2$ and examine how the impatience parameter impacts the steady-state advertising expenditure rates of both firms. It shows that when customers become more impatient, both firms reduce their advertising rates. Because reneging increases substantially with impatience (as discussed earlier) and one firm does not gain everything from the loss of the other firm, it is not advantageous for either firm to advertise more with an increase in the impatience level. We also note that the difference between the advertising expenditure rates of firms increases at higher impatience levels. This result indicates that when impatience levels are relatively high, the more effective and the higher capacity firm should advertise more as compared to the less effective and the lower capacity firm.

Figure 8 Impact of Impatience Parameter on the Singular Advertising Expenditure Rates  
![](/api/attachments/NGH3CFX6/fulltext/images/87489e11628700075943cb8666fbe1281e4e51aecd9579fd4ea33a9f3901cf61.jpg)

4.3.4. Impact of the Session Value. The impact of session value h is now presented in the following theorem.

<sup>Theorem</sup> <sup>7.</sup> The session value has no impact on the singular levels of arrival rates or the effective arrival rates. However, the advertising rates for both firms increase linearly with the session value.

Theorem 7 states that with an increase in the session value $h ,$ the advertising expenditures of both firms increase but their arrival rates remain unchanged. This result may seem counterintuitive at first glance but can be explained as follows. As the session value increases, it encourages both firms to advertise aggressively in an attempt to attract more customers. However, in equilibrium, although the arrival rates for either firm do not change, their advertising costs increase. In summary, an increase in session value triggers unhealthy advertising competition between the firms.

4.3.5. Symmetric Case. Next consider a symmetric case where $\eta _ { 1 } = \eta _ { 2 } = \eta$ and $\mu _ { 1 } = \mu _ { 2 } = \mu$ 0 In this case, we can easily derive from Equation (15) that $\hat { x } _ { 1 c } = 0 . 5 .$ . Hence, both firms have same market share in the singular region. Next, from Equation (14),

$$
A ^ {*} = A _ {1} ^ {*} = A _ {2} ^ {*} = \frac {h}{4} \left(1 - \frac {\nu (\mu + \nu)}{(\mu - 1 / 2 + \nu) ^ {2}}\right) - \frac {r}{2 \eta}.\tag{17}
$$

The key results for the symmetric case are summarized below.

<sup>Theorem</sup> <sup>8.</sup> In the symmetric case:

• The singular arrival rates for both firms are equal and independent of specific parameter values.

• The singular advertising rate increases with both the IT capacity level and the advertising effectiveness.

• The singular level of the total effective arrival rate increases with the IT capacity level and decreases with the impatience parameter.

Interestingly, as shown in Theorem 8, the arrival rates are independent of the specific parameters values, provided, of course, they are chosen to be symmetric. However, it is important to note that the effective arrival rate is still a function of the parameter values. It is instructive to compare the results for the symmetric case with those for the general case. First, the arrival rate increases with the IT capacity level, similar to that in Theorem 4. Next, Figure 5 shows that the advertising rate may increase or decrease with the advertising effectiveness. However, in the symmetric case, it is always increasing. This result indicates that in the symmetric case, the marginal benefit of increasing advertising (following an increase in the advertising effectiveness) is always more than its marginal cost.

We next present results pertaining to the total effective arrival rate of the system. Theorem 5 shows that the total effective arrival rate of the system may decrease with the IT capacity level of firm i when the arrival rate of firm i is less than $\eta _ { i } / ( \eta _ { 1 } + \eta _ { 2 } )$ . However, in the symmetric case, the arrival rate of each firm is equal to $\eta _ { i } / ( \eta _ { 1 } + \eta _ { 2 } )$ , and therefore the total effective arrival rate of the system always increases with the IT capacity level. Finally, similar to the general case (Figure 7), the total effective arrival rate of the system decreases with the impatience parameter.

## 5. Conclusions and Future Research Directions

With the fast growth of e-commerce businesses and their increasing dependence on information technology, it is important to reexamine traditional decisions (such as the advertising expenditure for a firm) in the context of the existing IT capacity. This issue has been considered important by several researchers and practitioners, yet little formal analysis has been conducted. Here we study this problem under a duopolistic setting and compare optimal advertising decisions over time with and without IT capacity constraints. Our analysis shows that traditional business decisions can change dramatically in the presence of such constraints.

In our study, the IT capacity (which by definition is always limited) results in a nonzero sum advertising game between two firms. The implication is that advertising expenditure can sometimes become wasteful if IT capacity considerations are not included in making advertising decisions. The relentless emphasis in current times on customer traffic at websites—and the corresponding advertising expenditure to make this happen—can therefore be misplaced unless IT capacity can match the traffic at the site. Often, however, advertising decisions are made locally; i.e., the marketing group makes these decisions without factoring IT capacity constraints. Hence, this study carries a pertinent message for many electronic retailers. The inclusion of IT capacity constraints limits the processing rates for all customers that arrive at the firm’s site. A direct impact of the IT capacity constraint is that it reduces the overall advertising effort. Thus, ignoring IT capacity constraints in advertising decisions can lead a firm to overadvertise.

A limitation of this research is that it considers IT capacity to be fixed. Hence, an important extension is to dynamically optimize the levels of both advertising and IT capacity. In such a problem, the optimal control formulation will include two control variables for each firm. Although the approach for solving such a joint formulation is similar to the one presented in this paper, it becomes very complex mathematically in both the monopolistic and the duopolistic settings. Hence, it may not be possible to obtain a closed-form solution for the joint problem, and one may need to restrict such a study to numerical analyses. A simpler approach to partially address the joint problem would be to treat IT capacity as a decision in stage 1 of the problem. Once the capacity decision is made, firms would choose their advertising levels in the next stage. This is very much in the spirit of Bertrand price competition with capacity constraints. However, even such a simple setting will require a game theoretic model for the IT decision.

Another limitation of this study is that we consider an open-loop strategy to solve the duopoly case. An interesting future research direction is to extend this study for the feedback Nash strategy. To solve for a feedback Nash strategy, the basic setup would be similar to that in the open-loop strategy. However, because the optimal control would become a function of both the state and the time in a feedback Nash strategy, the adjoint equation would become much more complicated, involving partial rather than total differential equations. Hence, it is usually very difficult to obtain closed-form solutions for a feedback Nash strategy, thus limiting deeper insights into the problem, especially, the use of comparative statics. For more details regarding solution approaches for feedback Nash strategies, the readers may refer to Dockner et al. (2000), Sethi and Thompson (2000), Sorger (1989), and Starr and Ho (1969). Finally, another possible future research direction is to study this problem in an oligopolistic setting. However, the analyses would be much more complex in that setting.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1110.0377.

## Acknowledgments

D. Liu is currently an Assistant Professor of Information Systems in the Department of Supply Chain and Information Systems at Iowa State University.

## References

Abad, P. L. 1982. An optimal control approach to marketingproduction planning. Optimal Control Appl. Methods 3(1) 1–13.

Abad, P. L. 1987. A hierarchical optimal control model for coordination of functional decisions in a firm. Eur. J. Oper. Res. 32 62–75.

ACNielsen. 2005. ACNielsen announces one-tenth of the world’s population shopping online: 627 million people have, including 325 million in the last month. ACNielsen Press Release (October 25). Accessed July 8, 2011, http://mynielsen.com/ news/2005127a.shtml.

Ancker, C. J., A. V. Gafarian. 1963a. Some queuing problems with balking and reneging—I. Oper. Res. 11(1) 88–100.

Ancker, C. J., A. V. Gafarian. 1963b. Some queuing problems with balking and reneging—II. Oper. Res. 11(6) 928–937.

Arrow, K. J., M. Kurz. 1970. Public Investment, the Rate of Return, and Optimal Fiscal Policy. The John Hopkins Press, Baltimore.

Barrer, D. Y. 1957a. Queuing with impatient customers and indifferent clerks. Oper. Res. 5(5) 644–649.

Barrer, D. Y. 1957b. Queuing with impatient customers and ordered service. Oper. Res. 5(5) 650–656.

Burns, E. 2007. Online retailers must adapt to earn customer satisfaction, survey finds. The ClickZ Network (June 5). Accessed July 8, 2011, http://clickz.com/showPage.html?page=3626073.

Case, J. H. 1979. Economics and the Competitive Process. New York University Press, New York.

Coffman, E. G., A. A. Puhalskii, M. I. Reiman, P. E. Wright. 1994. Processor-shared buffers with reneging. Performance Eval. 19 25–46.

Datta, A., K. Dutta, H. Thomas, D. VanderMeer. 2002. A proxybased approach for dynamic content acceleration on the WWW. Proc. 4th IEEE Internat. Workshop Adv. Issues of E-Commerce and Web-Based Inform. Systems, June 26–28, Newport Beach, California.

Datta, A., K. Dutta, H. Thomas, D. VanderMeer. 2003. World wide wait: A study of Internet scalability and cache-based approaches to alleviate it. Management Sci. 49(10) 1425–1444.

Deal, K. R. 1979. Optimizing advertising expenditures in a dynamic duopoly. Oper. Res. 27(4) 682–692.

Deal, K. R., S. Zionts. 1973. A differential games solution to the problem of determining the optimal timing of advertising expenditures. Proc. Second Annual Northeast Regional AIDS Conf., American Institute of Decision Sciences, Atlanta.

Dockner, E., S. Jorgensen, N. V. Long, G. Sorger. 2000. Differential Games in Economics and Management Science. Cambridge University Press, Cambridge, UK.

Eliashberg, J., R. Steinberg. 1993. Marketing-production joint decision-making. Handbook Oper. Res. Management Sci. 5 827–880.

Erickson, G. M. 1995. Differential game models of advertising competition. Eur. J. Oper. Res. 83 431–438.

Erickson, G. M. 1997. Dynamic conjectural variations in a Lanchester oligopoly. Management Sci. 43(11) 1603–1608.

Erickson, G. M. 2003. Dynamic Models of Advertising Competition. Kluwer Academic Publishers, Norwell.

Erickson, G. M. 2009. An oligopoly model of dynamic advertising competition. Eur. J. Oper. Res. 197(1) 374–388.

Erickson, G. M. 2011. A differential game model of the marketingoperations interface. Eur. J. Oper. Res. 211(2) 394–402.

Feichtinger, G. 1983. The Nash solution of an advertising differential game: Generalization of a model by Leitmann and Schmitendorf. IEEE Trans. Automatic Control AC 28(11) 1044–1048.

Feichtinger, G., R. F. Hartl. 1986. Optimale Kontrolle oekonomischer Prozesse—Anwendungen des Maximumprinzips in den Wirtschaftswissenschaften. Walter de Gruyter, Berlin.

Feichtinger, G., R. F. Hartl, S. P. Sethi. 1994. Dynamic optimal control models in advertising: Recent developments. Management Sci. 40(2) 195–226.

Feinberg, F. M. 1992. Pulsing policies for aggregate advertising models. Marketing Sci. 11(3) 221–234.

Freeland, J. R. 1980. Coordination strategies for production and marketing in a functionally decentralized firm. AIIE Trans. 12 126–132.

Fruchter, G. E. 1999. The many-player advertising game. Management Sci. 45(11) 1609–1611.

Fruchter, G. E., S. Kalish. 1997. Closed-loop advertising strategies in a duopoly. Management Sci. 43(1) 54–63.

Galletta, D. F., R. M. Henry, S. McCoy, P. Polak. 2006. When the wait isn’t so bad: The interacting effects of website delay, familiarity, and breadth. Inform. Systems Res. 17(1) 20–37.

Gould, J. P. 1970. Diffusion processes and optimal advertising policy. E. S. Phelps, G. C. Archibald, A. A. Alchian, eds. Microeconomic Foundation of Employment and Inflation Theory. W. W. Norton, New York, 338–368.

Green, H. 1999. The great yuletide shakeout: Online holiday shopping is set to explode, and pity the retailer who isn’t ready for it. Bus. Week (November 1), http://www.businessweek.com/ 1999/99\_44/b3653012.htm.

He, X., A. Prasad, S. P. Sethi. 2009. Cooperative advertising and pricing in a dynamic stochastic supply chain: Feedback stackelberg strategies. Production Oper. Management 18(1) 78–94.

Internet Retailer. 2005. Average response time for top 15 eretailers increases in July, Gomez says. (August 9), Accessed July 8, 2011. http://www.internetretailer.com/dailynews.asp ?id=15742.

Internet World Stats. 2011. Internet usage statistics—The Internet big picture. Accessed February 27, 2011, http://www .internetworldstats.com/stats.htm.

Jupiter Research. 2006. Retail web site performance: Consumer reaction to a poor online shopping experience. (June 1). Accessed July 8, 2011. http://www.akamai.com/dl/reports/ Site\_Abandonment\_Final\_Report.pdf.

Karpinski, R. 2000. E-retailers balance IT, marketing. InternetWeek 795 1.

Kimball, G. E. 1957. Some industrial applications of military operations research methods. Oper. Res. 5(2) 201–204.

Krishnamoorthy, A., A. Prasad, S. P. Sethi. 2010. Optimal pricing and advertising in a durable-good duopoly. Eur. J. Oper. Res. 200(2) 486–497.

Lanchester, F. W. 1916. Aircraft in Warfare: The Dawn of the Fourth Arm. Constable, London.

Leitmann, G., W. E. Schmitendorf. 1978. Profit maximization through advertising: A nonzero sum differential game approach. IEEE Trans. Automatic Control 23(4) 645–650.

Little, J. D. C. 1979. Aggregate advertising models: The state of the art. Oper. Res. 27(4) 629–667.

Liu, D., S. Sarkar, C. Sriskandarajah. 2010. Resource allocation policies for personalization in content delivery sites. Inform. Systems Res. 21(2) 227–248.

Liu, H., S. Wee. 2009. Web server farm in the cloud: Performance evaluation and dynamic architecture. Lecture Notes Comput. Sci. 5931 369–380.

Mahajan, V., E. Muller. 1986. Advertising pulsing policies for generating awareness for new products. Marketing Sci. 5(2) 89–111.

Mendelson, H. 1985. Pricing computer services: Queuing effects. Comm. ACM 28(3) 312–321.

Moe, W. W., P. S. Fader. 2004. Capturing evolving visit behavior in clickstream data. J. Interactive Marketing 18(1) 5–19.

Monica, P. R. 2005. Consumers keep on clicking: Stronger than expected 2Q results from Amazon is another good sign for e-commerce companies. CNN Money (July 26). Accessed July 8, 2011, http://money.cnn.com/2005/07/26/technology/ amazon\_analysis/index.htm.

Mulpuru, S., P. Hult, P. F. Evans, V. Sehgal, B. McGowan. 2010. US online retail forecast, 2009 to 2014. Forrester Res. (November 24). Accessed February 27, 2011, http://www .forrester.com/rb/Research/us\_online\_retail\_forecast,\_2009\_to \_2014/q/id/56551/t/2.

Nerlove, M., K. J. Arrow. 1962. Optimal advertising policy under dynamic conditions. Economica 29(114) 129–142.

Ozga, S. A. 1960. Imperfect markets through lack of knowledge. Quart. J. Econom. 74(1) 29–52.

Palda, K. S. 1964. The Measurement of Cumulative Advertising Effects. Prentice Hall, Upper Saddle River, NJ.

Palmer, J. W. 2002. Website usability, design, and performance metrics. Inform. Systems Res. 13(2) 151–167.

Pastore, M. 2001. E-tailers try to master the customer service thing. The ClickZ Network (November 19). Accessed July 8, 2011, http://www.clickz.com/showPage.html?page=926171.

Prasad, A., S. P. Sethi. 2004. Competitive advertising under uncertainty: A stochastic differential game approach. J. Optim. Theory Appl. 123(1) 163–185.

Rao, R. C. 1985. A note on optimal and near optimal price and advertising strategies. Management Sci. 31(3) 376–377.

Rodier, M. 2010. Market meltdown: Top online brokerages saw website response times dramatically slow down. Wall Street & Tech. (May 10). Accessed July 8, 2011, http://www .wallstreetandtech.com/it-infrastructure/showArticle.jhtml ?articleID=224701376.

Sasieni, M. W. 1971. Optimal advertising expenditure. Management Sci. 18(4) 64–72.

Sethi, S. P. 1973. Optimal control of Vidale-Wolf advertising model. Oper. Res. 21 998–1013.

Sethi, S. P. 1977a. Dynamic optimal control models in advertising: A survey. SIAM Rev. 19(4) 685–725.

Sethi, S. P. 1977b. Optimal advertising for the Nerlove-Arrow model under a budget constraint. Oper. Res. Quart. 28(3) 683–693.

Sethi, S. P. 1979. Optimal advertising policy with the contagion model. J. Optim. Theory Appl. 29(4) 615–627.

Sethi, S. P. 1983. Deterministic and stochastic optimization of a dynamic advertising model. Optimal Control Appl. Methods 4 179–184.

Sethi, S. P., G. L. Thompson. 2000. Optimal Control Theory: Applications to Management Science and Economics. Kluwer Academic Publishers, Boston.

Sethi, S. P., Q. Zhang. 1992. Multilevel hierarchical controls in dynamic stochastic marketing-production system. Proc. 31st IEEE Conf. Decision and Control, Tucson, AZ, 2090–2095.

Sethi, S. P., A. Prasad, X. He. 2008. Optimal advertising and pricing in a new-product adoption model. J. Optim. Theory Appl. 139(2) 351–360.

Shapiro, B. P. 1977. Can marketing and manufacturing coexist? Harvard Bus. Rev. (Sep.–Oct.) 104–112.

Sogomonian, A. G, C. S. Tang. 1993. A modeling framework for coordinating promotion and production decisions within a firm. Management Sci. 39(2) 191–203.

Sorger, G. 1989. Competitive dynamic advertising: A modification of the case game. J. Econom. Dynam. Control 13 55–80.

Souders, S. 2007. High performance web sites: Rule 1—Make fewer HTTP requests. Yahoo! Developer Network (April 3). Accessed July 8, 2011, http://developer.yahoo.com/blogs/ydn/ posts/2007/ 04/rule\_1\_make\_few/.

Starr, A. W, Y. C. Ho. 1969. Nonzero-sum differential games. J. Optim. Theory Appl. 3(3) 184–206.

Tan, Y., V. S. Mookerjee. 2005. Optimal spending allocation between advertising and information technology. Management Sci. 51(8) 1236–1249.

Tapiero, C. S. 1975. Random walk models of advertising, their diffusion approximation and hypothesis testing. Ann. Econom. Soc. Measurement 4 293–309.

Tapiero, C. S. 1988. Applied Stochastic Models and Control in Management. North-Holland, Amsterdam.

Telser, L. G. 1962. Advertising and cigarettes. J. Political Econom. 70(5) 471–499.

Theurer, T. 2006. Performance research, part 1: What the 80/20 rule tells us about reducing HTTP requests. Yahoo! User Interface Blog (November 28). Accessed July 8, 2011, http://www.yuiblog.com/blog/2006/11/28/performance-research -part-1/.

Thomas, J. 1971. Linear programming models for production— Advertising decisions. Management Sci. 17(8) B474–B484.

Ulusoy, G., T. Yazgac. 1995. Joint decision making for production and marketing. Internat. J. Production Res. 33(8) 2277–2293.

Vidale, M. L., H. B. Wolfe. 1957. An operations-research study of sales response to advertising. Oper. Res. 5(3) 370–381.

Voigt, T. 2002. Overload behaviour and protection of event-driven web servers. Lecture Notes Comput. Sci. 2376 147–157.

Welam, U. P. 1977. Synthesizing short run production and marketing decisions. AIIE Trans. 9 53–62.

Welam, U. P. 1982. Optimal and near optimal price and advertising strategies for finite and infinite horizons. Management Sci. 28(11) 1313–1327.

Whitt, W. 1999. Improving service by informing customers about anticipated delays. Management Sci. 45(2) 192–207.

Zensarteam. 2010. Best practices for speeding up your web site. Zensarteam’s Blog (September 22). Accessed July 8, 2011, http:// zensarteam.wordpress.com/2010/09/22/best-practices-for -speeding-up-your-web-site/.
