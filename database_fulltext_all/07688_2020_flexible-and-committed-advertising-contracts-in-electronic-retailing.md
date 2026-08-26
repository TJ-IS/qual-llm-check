---
otero_id: 7688
otero_key: "JP324GCM"
title: "Flexible and Committed Advertising Contracts in Electronic Retailing"
authors: "Dengpan Liu; Subodha Kumar; Vijay S. Mookerjee"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0886"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/JP324GCM/fulltext/images/29d61196892888071c02faa3f049050500ae9d9356b5a2f91d52355c589cfcdc.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Flexible and Committed Advertising Contracts in Electronic Retailing

Dengpan Liu, Subodha Kumar, Vijay S. Mookerjee

To cite this article: Dengpan Liu, Subodha Kumar, Vijay S. Mookerjee (2020) Flexible and Committed Advertising Contracts in Electronic Retailing. Information Systems Research

Published online in Articles in Advance 04 Jun 2020

https://doi.org/10.1287/isre.2019.0886

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Flexible and Committed Advertising Contracts in Electronic Retailing

Dengpan Liu,<sup>a,</sup>\* Subodha Kumar,<sup>b</sup> Vijay S. Mookerjee<sup>c</sup>

<sup>a</sup> School of Economics and Management, Tsinghua University, 100084 Beijing, China; <sup>b</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122; <sup>c</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75083 \*Corresponding author

Contact: liudp@sem.tsinghua.edu.cn (DL); subodha@temple.edu (SK); vijaym@utdallas.edu (VSM)

Received: April 3, 2018 Revised: March 12, 2019 Accepted: July 24, 2019 Published Online in Articles in Advance: June 4, 2020

https://doi.org/10.1287/isre.2019.0886

Copyright: © 2020 INFORMS

Abstract. We use a differential games framework to study two modes of dynamic advertising competition, namely flexible (or closed loop) and committed (or open loop), be tween two e-retailers that compete for traffic. In closed-loop competition, the advertising contract allows firms to adjust their advertising levels during the advertising campaign. However, in open-loop competition, the contract requires the firms to commit upfront to an advertising plan (however, not necessarily one that advertises at a fixed rate). We ask the following question: Which contract (flexible or committed) is better for the firms (ad vertising agent)? We find that the firms advertise less and earn more under flexible contracts. As a result, the advertising agent earns less from the two firms under flexible contracts. Flexible and committed contracts become more interesting to study if opera tional considerations are included. These considerations arise from information technolog (IT) costs incurred to process the traffic that arrives at the e-retailers’ websites. Operationa considerations reduce the difference in advertising spending between the two contracts. Interestingly, to increase the revenue earned under flexible contracts, the advertising agent should offer such contracts at a price that is discounted relative to committed contracts. The discount exploits the force of competition and induces the firms to spend more on advertising. The optimal discount offered under a flexible contract decreases as the IT cost increases.

History: D. J. Wu, Senior Editor; Sameer Hasija, Associate Editor.

Funding: D. Liu’s research was supported in part by the National Natural Science Foundation of China [Grant 71490723].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0886.

Keywords: differential games • advertising competition • operational considerations • electronic retailing

## 1. Introduction

The past decade has witnessed a tremendous growth in electronic retailing. In 2016, U.S. retail e-commerce sales reached \$394.9 billion, an increase of 15.1% from 2015 (U.S. Census Bureau 2017). The growth of the e-retailing market is expected to continue for the foreseeable future. According to a report released by FTI Consulting, Inc., U.S. online retail sales will approach \$562 billion by 2020 (FTI Consulting 2016). With the growth of e-commerce activity, advertising competition among e-retailers has become more intense, as evidenced by the growing expenditure on internet advertising: The total spending on digital ads in the United States in 2015 reached \$59.6 billion, up 20.4% from 2014 (Interactive Advertising Bureau 2016).

e-Retailers often work with advertising agents (e.g., Google or Facebook) to launch their advertising campaigns. Many agents offer flexible advertising contracts wherein firms have the flexibility to adjust their level of advertising (e.g., impressions or clicks per day) during the advertising campaign. Some agents also offer committed contracts wherein firms do not have this flexibility. Such contracts require committed (or preplanned) advertising that can usually be purchased at a discounted rate (Kelley and Jugenheimer 2008). For example, some search engine advertising agents require that the firms commit upfront to certain advertising levels in order to get price breaks on certain types of ads (Lee and Seda 2009). As another example, Yelp requires that advertisers make a 12-month commitment in order to qualify for a reduced rate (Agarwal 2012). Note that a committed contract is one in which the agent needs to deliver a certain level of advertising that is based on a schedule specified at the start of the campaign. Thus, although the level of advertising can change during the campaign, the entire path must be specified upfront. In a flexible contract, no upfront schedule needs to be specified. Here the advertising level can be continuously adjusted (e.g., on a daily basis).

To obtain insights into the impact of the two types of advertising contracts, we study dynamic advertising competition between e-retailing firms using a differential games framework. Here we use closed-loop and open-loop differential games to model the competition involving flexible and committed contracts, respectively. The main question that we explore in this study is as follows: which mode of dynamic competition (flexible or committed) is better for the firms (advertising agents)? We also ask the following: how should the agent price flexible and committed contracts? In practice, advertising agents typically charge more (e.g., a higher price per impression) for a flexible advertising plan. At first blush, this practice seems reasonable because an additional convenience is being provided to the advertising firm in a flexible contract.

We also study operational implications that arise from information technology (IT) costs incurred to handle the incoming traffic generated by the advertising endeavors of firms. It is crucial for e-commerce firms to examine the operational implications of their advertising plans. If the traffic attracted to a firm’s website is not served with adequate capacity, then the average website delays would increase, leading to degraded service quality at the site. Clearly, the increased delays can hurt user experience and thus the profitability of the firm. However, Hoxmeier (2000) finds that, ceteris paribus, reducing delays at the website can directly improve customer satisfaction, which is, in turn, positively associated with profitability for most firms (Zhang and Pan 2009).

Given the importance of operational considerations (e.g., website delays), an e-retailing firm needs to carefully plan its activities pertaining to both demand generation (responsible for bringing traffic to the website) and demand fulfillment (responsible for adequately serving incoming traffic). Apparently, demand generation incurs advertising costs, and demand fulfillment incurs IT costs. From an e-retailer’s perspective, the choice between flexible and committed advertising contracts is complicated by operational considerations. We ask the following: how do operational considerations affect the profits earned by firms under flexible and committed contracts?

Several important findings emerge from our study. First, we find that firms are typically better off under flexible rather than committed contracts. Not surprisingly, however, the advertising agent prefers committed contracts. Second, the advantage (to firms) of flexible contracts decreases as IT becomes costlier. Third, despite offering more flexibility, agents should price flexible contracts lower than committed contracts. Here our findings challenge practice, where one observes that flexible contracts are usually priced higher. Fourth, our analysis shows that the optimal discount offered under a flexible contract should decrease as the IT cost increases.

The rest of this paper is organized as follows. In Section 2, we provide a review of the literature on related topics. In Section 3, we present important model notation and the basic assumptions of the study. In Section 4, we present a basic model where advertising efforts are chosen by firms under the assumption that the IT service quality is given. In Section 5, we study three extensions to the basic model. Section 6 concludes the paper and provides directions for fu ture research.

## 2. Literature Review

In this section, we survey the literature on the four critical aspects of our problem: differential games, advertising competition, operational (IT) factors, and pricing models in online advertising.

## 2.1. Differential Games

This approach has been widely used to study models of dynamic competition. The solutions of differential games models can be categorized as open loop or closed loop (feedback). In open-loop models, the control variable is only a function of time and not the state variable, whereas in closed-loop models, the control variable is a function of the state variable as well (Seth and Thompson 2000). Therefore, open-loop models are appropriate for solving planning problems, whereas closed-loop models can be used to model tactical or operational problems, where control can be adjusted in real time as a function of the realized value of the state variable.

In a closed-loop model, both players have the ability to observe the realized value of the state variable before choosing the value of the control variable. This ability can change the equilibrium solution even if the relationship between the state variable and the control is not inherently stochastic. This is so because, unlike an open-loop model, the strategy space in a closed-loop model permits a player to deviate from any committed (e.g., time-dependent) control strategy. Thus, the presence of strategic participants, rather than an inherently stochastic state variable, can be sufficient to create differences between open-loop and closed-loop equilibrium.

Deal and Zionts (1973) and Deal (1979) were among the first to develop differential games models in advertising. Feichtinger (1983) extended these models by considering a different system dynamics and using a generalized function of advertising effectiveness. Sorger (1989) studied both the open-loop and the feedback (closed-loop) advertising competitions, and derived noncooperative Nash equilibria in both competitions. Liu et al. (2012) incorporated an IT capacity constraint into duopolistic advertising differential games. Interested readers may refer to

Dockner et al. (2000) and Erickson (2003) for detailed reviews of differential games models in advertising.

One thing worth noting here is that it would not be possible to obtain some of the key findings of this paper with conventional static models. This is so because the static models, unlike a differential games model, are unable to capture the subtle difference between the flexible and committed competition.

## 2.2. Advertising Competition

There exists a large body of literature on duopolistic advertising competition. Deal (1979) and Erickson (1985) were among the earliest works to study advertising competition between two firms. It is worth noting that most of the papers in this stream of literature (Sorger 1989, Erickson 2003, Prasad and Sethi 2004, Naik et al. 2008, Liu et al. 2012) assume other marketing mix variables, such as price and quality, to be exogenous so as to focus only on the study of advertising competition.

In previous work on advertising competition, the study of Liu et al. (2012) is the one closest to our study in that it incorporates IT capacity in a setting of duopolistic advertising competition. However, our work differs from that of Liu et al. (2012) in several important aspects. First, Liu et al. (2012) studied competition under committed contracts but not flexible contracts. Second, Liu et al. (2012) only studied the problems of advertising firms and not those of advertising agents. In this study, we additionally examine how operational considerations affect the outcomes under flexible and committed contracts and use these results to find a differential pricing scheme that enables the advertising agent to maximize revenue.

## 2.3. Operational (IT) Factors

IT service quality is an important component of demand fulfillment in e-retailing firms. The level of service quality depends on factors such as response time, quality of website design, informativeness of website content, etc. The impact of service quality on e-retailing firms’ profitability is twofold. On the one hand, service quality at e-commerce sites can positively influence the repurchase intention of consumers (Ganguly et al. 2010, Hu 2010, Kalia et al. 2016) and hence the revenue earned by the firm. Moreover, it has been reported that service quality has a significant impact on conversion rate of consumers. For instance, according to a study by Walmart, conversion rate at walmart.com can be expected to increase by 2% if the website loading time is reduced by 1 second (Bixby 2012). On the other hand, service businesses need to incur quality costs to ensure the quality of the services they provide (Pyzdek and Keller 2013), and the e-retailing business is no exception. Thus, e-retailing firms need to incur additional operational costs to ensure higher service quality. For example, when an e-retailing firm’s present infrastructure is under relatively heavy load, the firm may need to expand server capacity—which comes at an additional cost—to ensure an acceptable loading time at the site (Rodman 2013). As another example, the operational costs of customized e-commerce sites that are specifically optimized for customer engagement and interaction are significantly higher than those of e-commerce sites with no customization (DeLapp 2017).

## 2.4. Pricing Models in Online Advertising

There is extensive literature on pricing models in online advertising. For example, Moon and Kwon (2011) studied a pricing scheme wherein publishers allow advertisers to pay the minimum of cost per thousand impressions (CPM) and cost per click (CPC) fees. They find that the advertiser and the publisher can both be better off when signing an option contract under this pricing scheme. Using a principal agent framework, Asdemir et al. (2012) studied how the preference for a particular pricing model (CPC or CPM) is impacted by market conditions. More recently, Hu et al. (2016) used the economic framework of incentive contracts to investigate the trade-offs between choosing CPC and cost per action, both of which are performance-based advertising pricing models. According to their findings, the preferred choice of performance-based pricing models of publishers may differ from that of advertisers.

Most of this research on online advertising pricing models focuses on the study of either impression- or performance-based pricing models. To the best of our knowledge, to date, there is little work in this stream of research studying pricing models that are based on the flexibility of adjusting the level of advertising, especially in the context of dynamic competition between two advertisers. This work aims to fill this gap in the literature.

## 3. Notation and Basic Assumptions

We consider a duopolistic setting where two e-retailing firms (denoted by 1 and 2) are engaged in a dynamic advertising competition for customer traffic. Each firm generates traffic (or potential demand) through advertising and captures demand by providing a certain level of service quality that incurs IT costs. We first study a situation where service quality is exogenous, and firms only decide on their level of advertising spending. We later relax this assumption and examine the case where each firm needs to jointly choose its service quality and advertising level. The main parameters and control variables used in our model are summarized in Table 1.

Advertising effort can be considered to be an input in a production function for generating traffic (Sethi 1983). Following past studies (Case 1979, Sethi 1983, Sorger 1989), we model the advertising cost rate (dollars per unit time) as $k _ { i } A _ { i } ^ { 2 } .$ , where $A _ { i }$ is the advertising rate of firm i and $k _ { i } > 0$ is a scaling parameter. Without loss of generality, we normalize the total amount of traffic at the two firms per unit time to one. We denote by $h _ { i }$ the maximum possible session value of serving one customer at firm i. We denote the market (traffic) share of firm i at time t by $x _ { i } ( t ) , i = 1 , 2$ For convenience, let $x _ { 1 } = x$ and $x _ { 2 } = 1 - x , x \in [ 0 , 1 ]$

Table 1. Main Notation Used in the Paper

<table><tr><td>Parameters</td><td>Description</td></tr><tr><td> $h_i > 0$ </td><td>Session value (that is, the maximum possible value of serving one customer) at firm  $i, i = 1,2$ </td></tr><tr><td> $k_i > 0$ </td><td>The scaling parameter for the advertising efforts of firm  $i$ </td></tr><tr><td> $r_i \geq 0$ </td><td>The discount rate for firm  $i$ </td></tr><tr><td> $q_i \geq 0$ </td><td>IT service quality of firm  $i$ </td></tr><tr><td> $f(q)$ </td><td>The fixed IT cost for the service quality  $q$  irrespective of the traffic</td></tr><tr><td> $g(q)$ </td><td>The variable IT cost for the service quality  $q$  per unit traffic</td></tr><tr><td> $A_i(t)$ </td><td>The advertising rate of firm  $i$  at time  $t$  (control variables)</td></tr><tr><td> $x \in [0,1]$ </td><td>The market share of firm 1 (state variable)</td></tr></table>

We use $q _ { i } \geq 0$ to denote the quality of service (provided by IT) at firm i. Here IT service quality is measured by factors that improve conversion of traffic to sales (e.g., the response time, the quality of the website’s user interface, the informativeness of the website content, etc.). We define the realized session value of serving a customer at firm i as $\textstyle { \frac { q _ { i } } { 1 + q _ { i } } } h _ { i }$ . It is clear that the realized session value increases with $q _ { i } .$ . Specifically, the realized session value equals 0 when $q _ { i } = 0$ and $h _ { i }$ when $q _ { i }$ tends to infinity.

e-Retailers incur operational (IT) costs to handle the arriving traffic. The IT costs incurred by each firm include two components: (1) a cost $f ( q )$ that depends on the service quality but does not change with the traffic (e.g., website design cost, physical space, etc.) and (2) a variable cost per unit traffic $g ( q )$ . For tractability, we consider $f ( q ) = a q$ and $g ( q ) = b q$ , where a and b are both positive constants.<sup>1</sup> As we can see, both the fixed and variable costs are increasing functions of service quality q. Thus, ceteris paribus, firms with a higher service quality incur higher IT costs.

As discussed earlier, we consider two firms that are engaged in one of two modes of dynamic competition: committed advertising or flexible advertising. These two modes of competition are modeled using open- and closed-loop differential game frameworks, respectively. The open-loop contract is so constructed that the firms must commit to prespecified advertising trajectories. That is, the firms must plan their advertising trajectories before the start of the game and then stick to those committed trajectories throughout the planning horizon. Therefore, in committed advertising competition, a firm’s advertising rate (the control variable) at a given point in time only depends on time. In contrast, in flexible advertising competition, the advertising rate of a firm can be a function of its market share (the state variable) as well as time. In the following section, we investigate the equilibrium outcome of firms engaged in committed and flexible advertising competition.

## 4. Basic Model: Exogenous Service Quality

## 4.1. Committed Advertising Competition

Under committed advertising competition, each firm’s advertising spending is prespecified and only a function of time. This problem can be formulated as an open-loop differential game, as shown next:

$$
\begin{array}{l} \max _ {A _ {i} (t)} \bigg \{J _ {i} = \int_ {0} ^ {\infty} \bigg [ \frac {q _ {i}}{1 + q _ {i}} h _ {i} x _ {i} (t) - k _ {i} A _ {i} (t) ^ {2} \\ \qquad - \left(a q _ {i} + b q _ {i} x _ {i} (t)\right) \bigg ] e ^ {- r _ {i} t} d t \bigg \}, \quad i \in \{1, 2 \}, \end{array}\tag{1}
$$

where $x _ { 1 } = x$ and $x _ { 2 } = 1 - x .$ . The first term of the integrand is the rate of value derived from serving the arriving traffic of $x _ { i }$ at firm i. The second term is the rate of the advertising cost spent to generate the arriving traffic of $x _ { i } .$ . Finally, the third term is the IT capacity cost rate incurred to process the arriving traffic at firm i.

Similar to Sethi (1983) and Sorger (1989), we mode the state equation of the differential game as

$$
\begin{array}{l} \dot {x} (t) = \frac {d x (t)}{d t} = A _ {1} (t) \sqrt {1 - x (t)} - A _ {2} (t) \sqrt {x (t)}, \\ x (0) = x _ {0} \in [ 0, 1 ], \end{array}\tag{2}
$$

where $x _ { 0 }$ is the initial arriving traffic at firm 1. As shown in the state equation, the change rate of firm 1’s market share is positively affected by firm ${ 1 ^ { \prime } } \mathrm { s }$ advertising rate but negatively affected by firm $2 ^ { \prime } \mathrm { s }$ advertising rate.

As explained by Sethi (1983), the nonlinear effect in this state equation is a larger effect than that in the classical Vidale–Wolfe model (Vidale and Wolfe 1957) The larger effect can be explained in part by an additional process of word-of-mouth communication between the individuals making up the captured traffic and those making up the noncaptured traffic. Furthermore, Sorger (1989) provides several arguments in favor of this state equation. First, Sorger (1989) shows that this state equation is an approximation of the market share dynamics that combines “Lanchester-type” dynamics (Case 1979) with an “excess advertising” model. Sorger (1989) also shows that this state equation reflects the well-known S-shaped response function (Little 1979).

For notational convenience, let $\Gamma _ { i } = q _ { i } h _ { i } / ( 1 + q _ { i } ) - b q _ { i }$ Following Sorger (1989), we derive the equilibrium solution of the above-mentioned differential game and present it in Lemma 1. All the proofs of lemmas and propositions are relegated to the online appendix.

Lemma 1. A Nash equilibrium for committed advertising competition is

$$
A _ {i} = \epsilon_ {i} \sqrt {1 - x _ {i}} = \epsilon_ {i} \sqrt {x _ {j}}, \quad \{i, j \} = \{1, 2 \},
$$

where $( \epsilon _ { 1 } , \epsilon _ { 2 } )$ is the unique solution of

$$
r _ {i} \epsilon_ {i} + \frac {\epsilon_ {i} ^ {2}}{2} + \frac {\epsilon_ {i} \epsilon_ {j}}{2} - \frac {\Gamma_ {i}}{2 k _ {i}} = 0, \quad \{i, j \} = \{1, 2 \},\tag{3}
$$

satisfying $\epsilon _ { i } \ge 0 , i = 1 , 2$ . The state trajectory corresponding to this equilibrium is given by

$$
x (t) = \frac {\epsilon_ {1}}{\epsilon_ {1} + \epsilon_ {2}} + \left[ x _ {0} - \frac {\epsilon_ {1}}{\epsilon_ {1} + \epsilon_ {2}} \right] e ^ {- (\epsilon_ {1} + \epsilon_ {2}) t}.\tag{4}
$$

From Equation (4), we can depict the trajectory of the arriving traffic at firm 1 as follows: if the initial market share of firm 1 is above a certain threshold $\begin{array} { r } { ( \mathrm { i . e . , } x _ { 0 } > \frac { \epsilon _ { 1 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } ) } \end{array}$ , then as time tends to infinity, the arriving traffic x will decrease asymptotically to $\begin{array} { r } { \frac { \epsilon _ { 1 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } . } \end{array}$ However, if the initial market share of firm 1 is below that threshold $\begin{array} { r } { ( \mathrm { i . e . , ~ } x _ { 0 } < \frac { \epsilon _ { 1 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } ) } \end{array}$ , then as time tends to infinity, the arriving traffic of x will increase asymptotically $\begin{array} { r } { \mathrm { t o } \frac { \epsilon _ { 1 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } . } \end{array}$ If the initial market share of firm 1 is equal to the threshold $\begin{array} { r } { ( \mathrm { i . e . , ~ } x _ { 0 } = \frac { \epsilon _ { 1 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } ) } \end{array}$ , then the arriving traffic of x will stay constant at $x _ { 0 }$ throughout the time period of the game. This result indicates that, in equilibrium, the market shares of firms 1 and 2 will eventually converge to the steady levels $\frac { \epsilon _ { 1 } } { \epsilon _ { 1 } { + } \epsilon _ { 2 } }$ and $\begin{array} { r } { \frac { \epsilon _ { 2 } } { \epsilon _ { 1 } + \epsilon _ { 2 } } , } \end{array}$ respectively.

## 4.2. Flexible Advertising Competition

In flexible advertising competition, a firm’s advertising rate (control variable $A _ { i } )$ is both a function of time (t) and the value of its market share $( x _ { i } )$ This problem can be formulated as a closed-loop differential game, as shown next:

$$
\begin{array}{c} \max _ {A _ {i} (x _ {i}, t)} \bigg \{J _ {i} = \int_ {0} ^ {\infty} \bigg [ \frac {q _ {i}}{1 + q _ {i}} h _ {i} x _ {i} - k _ {i} A _ {i} (x _ {i}, t) ^ {2} \\ - \big (a q _ {i} + b q _ {i} x _ {i} \big) \bigg ] e ^ {- r _ {i} t} d t \bigg \}, \quad i \in \{1, 2 \}, \end{array}\tag{5}
$$

where $x _ { 1 } = x$ and $x _ { 2 } = 1 - x .$

The state equation is the same as Equation (2). Following Sorger (1989), we derive the equilibrium solution of the closed-loop differential game and present it in Lemma 2.

Lemma 2. A Nash equilibrium for the flexible advertising competition is

$$
A _ {i} (x) = \eta_ {i} \sqrt {1 - x _ {i}} = \eta_ {i} \sqrt {x _ {j}}, \quad \{i, j \} = \{1, 2 \},
$$

where $( \eta _ { 1 } , \eta _ { 2 } )$ is the unique solution of

$$
r _ {i} \eta_ {i} + \frac {\eta_ {i} ^ {2}}{2} + \eta_ {i} \eta_ {j} - \frac {\Gamma_ {i}}{2 k _ {i}} = 0, \quad \{i, j \} = \{1, 2 \},\tag{6}
$$

satisfying $\eta _ { i } \geq 0 , i = 1 , 2 .$ . The state trajectory corresponding to this equilibrium is given by

$$
x (t) = \frac {\eta_ {1}}{\eta_ {1} + \eta_ {2}} + \left[ x _ {0} - \frac {\eta_ {1}}{\eta_ {1} + \eta_ {2}} \right] e ^ {- (\eta_ {1} + \eta_ {2}) t}.\tag{7}
$$

## 4.3. Comparison Between Committed and Flexible Advertising Competition

The following question naturally arises: which mode of competition, committed or flexible, is better for the firms? For tractability, we first explore this question under a symmetric setting where $x _ { 0 } = 0 . 5 , r _ { 1 } = r _ { 2 } = r ,$ $h _ { 1 } = h _ { 2 } = { \dot { h } } , q _ { 1 } = q _ { 2 } = q , k _ { 1 } \stackrel {  } { = } k _ { 2 } = k .$ . Under this setting, we have $\Gamma _ { 1 } = \Gamma _ { 2 } = \Gamma = q h / ( 1 + q ) - b q$

Under committed advertising competition, from (3), we solve the following equation:

$$
\epsilon^ {2} + r \epsilon - \Gamma / (2 k) = 0.\tag{8}
$$

Thus, we have

$$
\epsilon^ {*} = \frac {- r + \sqrt {r ^ {2} + 2 \Gamma / k}}{2}.\tag{9}
$$

Under this symmetric setting, we have $x = 1 / 2 ,$ , and the two firms have the same advertising rate $A ^ { c * } =$ $\epsilon ^ { * } / \sqrt { 2 }$ , where the superscript c stands for “committed.”

Under flexible advertising competition, from (6), we solve the following equation:

$$
3 \eta^ {2} / 2 + r \eta - \Gamma / (2 k) = 0.\tag{10}
$$

Thus, we have

$$
\eta^ {*} = \frac {- r + \sqrt {r ^ {2} + 3 \Gamma / k}}{3}.\tag{11}
$$

Under this symmetric setting, when the quality of service is given, we have $x = 1 / 2 ,$ , and the two firms have the same advertising rate $A ^ { f * } = \eta ^ { * } / \sqrt { 2 }$ , where the superscript f stands for “flexible.” We assume that $\Gamma = q \hat { h / ( 1 + q ) } \hat { - } b q > 0$ to avoid the trivial solution where $\epsilon ^ { * } = \eta ^ { * } = 0$

Given the same level of service quality being adopted in flexible and committed advertising competition, we can easily show that

$$
\epsilon^ {*} = \frac {- r + \sqrt {r ^ {2} + 2 \Gamma / k}}{2} > \eta^ {*} = \frac {- r + \sqrt {r ^ {2} + 3 \Gamma / k}}{3}.
$$

Note that the firms’ advertising rates in committed and flexible advertising competition are $A ^ { c * } = \epsilon ^ { * } / \sqrt { 2 }$ and $A ^ { f * } = \eta ^ { * } / \sqrt { 2 }$ , respectively. Also, when the service quality is given, the comparison of firms’ profits in these two modes of competition boils down to the comparison of firms’ advertising efforts. Thus, we have the following result.

Proposition 1. Under a symmetric setting, firms advertise less and earn more under a flexible contract than under a committed contract.

This proposition holds because the values of the advertisement efforts under flexible advertising competition are strictly lower than those under committed competition, whereas IT service costs as well as the revenues are the same. Under flexible advertising competition, the control variable is a function of the state variable, that is, market share. It should be noted that the advertising rate under flexible contracts converges to a steady value. However, the possibility of defecting from a committed value exists in the flexible strategy space. Hence, the advertising rates under the two modes of competition converge to different steady values. The flexibility of allowing the control variables to be adjusted based on the state (market share) allows the players to reduce the advertising effort while competing for traffic. The difference between the two modes of competition can also be understood by noting that in a flexible strategy space, the opponents in the game have the ability to retaliate in response to an increase in the advertising effort by a firm. By contrast, under committed advertising competition, the inability to adjust the control based on the state forces the firms to step up their planned advertising efforts chosen at the start of the game. In other words, flexible advertising competition naturally dampens the advertising arms race. Thus, under a symmetric setting, both firms are better off under flexible contracts. This result is interesting in the sense that it points out that the committed game may not be optimal from a social perspective (i.e., the sum of profits of the two firms). It is also worth noting that this result could not be obtained with conventional static models in which the difference between flexible and committed competition is not taken into consideration.

Another interesting question is as follows: how do IT costs affect the advantage (to firms) of flexible over committed contracts? We use $\Delta = \Pi _ { 1 } ^ { f } + \Pi _ { 2 } ^ { f } - ( \Pi _ { 1 } ^ { c } + \Pi _ { 2 } ^ { c } )$ to denote the advantage of flexible over committed advertising competition (i.e., the difference between the sum of the profits of the firms under flexible and committed advertising competition). $\mathrm { A s }$ shown in Proposition 1, we have $\Delta > 0$ . We can further show that $\begin{array} { r } { \frac { \partial \Delta } { \partial b } < 0 . } \end{array}$ . We summarize our findings in the following proposition.

Proposition 2. Under a symmetric setting, as operational costs increase (i.e., b increases), the relative advantage (to firms) of flexible over committed advertising competition decreases.

The intuition behind this finding is the following. Firms have a tendency to overadvertise in the presence of competition. Because an increase in operational costs acts to restrain the tendency of overadvertising, the advantage of flexible contracts to further restrain advertising aggression decreases. Another thing worth mentioning is that this result could not be obtained with conventional static models that are unable to capture the difference between flexible and committed competition.

An interesting question naturally arises: how does the advertising cost affect the advantage (to firms) of flexible over committed contracts? Because it is analytically intractable to find the sign of $\begin{array} { r } { \frac { \partial \Delta } { \partial k } , } \end{array}$ , we numerically examine how Δ changes with k. For this numerical study, we let $r = 0 . 2 , h = 1 , a = 0 . 2 5 , b = 0 . 1$

As shown in Figure 1, the difference in the profits of firms under the two modes of dynamic competition decreases with the advertising cost coefficient k. This is so because as k increases, the advertising competition between the two firms decreases. Thus, the difference in the profits of firms under the two modes of competition, which captures the advantage of flexible over committed competition, decreases.

## 4.4. Advertising Agent’s Problem

We consider an advertising agent (e.g., Facebook.com) that wishes to maximize the sum of the advertising revenues earned from the two e-retailing firms under a symmetric setting. As discussed earlier, firms advertise less and earn more under flexible advertising competition. Thus, from the standpoint of the advertising agent (e.g., Facebook.com), committed advertising competition is preferable because the advertising agent generates more revenue in this mode of competition. A question that naturally arises here is as follows: how can the advertising agent induce firms to choose committed contracts? The approach that we examine here is to use the price of advertising in such a way that each firm spends the same amount on advertising under both modes of competition (and thus each firm is indifferent between flexible and committed competition under a symmetric setting). Specifically, we change the advertising cost coefficient under flexible contracts from k to $k + \delta .$ . Here $\delta > 0$ means that an additional charge δ is imposed on flexi ble contracts, whereas $\delta < 0$ means that the advertising agent discounts the flexible contracts with δ . Thus, under flexible contracts, we have

Figure 1. Difference in Profits of Firms as a Function of the Advertising Cost Coefficient  
![](/api/attachments/JP324GCM/fulltext/images/159bad4a337dfb379d2c66996915d502b81aa150a6b1255369065a61e7f63514.jpg)

$$
\eta^ {*} = \frac {- r + \sqrt {r ^ {2} + 3 \Gamma / (k + \delta)}}{3}.
$$

The firms are indifferent between committed and flexible contracts when

$$
\begin{array}{c} k \bigg (\frac {- r + \sqrt {r ^ {2} + 2 \Gamma / k}}{2} \sqrt {1 - x} \bigg) ^ {2} \\ = (k + \delta) \left(\frac {- r + \sqrt {r ^ {2} + 3 \Gamma / (k + \delta)}}{3} \sqrt {1 - x}\right) ^ {2}, \end{array}
$$

which can be simplified to

$$
\frac {- r + \sqrt {r ^ {2} + 2 \Gamma / k}}{- r + \sqrt {r ^ {2} + 3 \Gamma / (k + \delta)}} = \frac {2 \sqrt {k + \delta}}{3 \sqrt {k}}.\tag{12}
$$

Let $\delta ^ { * }$ be the solution to this equation. With the additional charge $\delta ^ { * } ~ ( \mathrm { i . e . }$ , in addition to k) imposed on flexible contracts, firms will be indifferent between committed and flexible contracts. For convenience, we hereafter refer to $\delta ^ { * }$ as indifference point additional charge. At first blush, one would expect the advertising agent to charge more for flexible contracts (or, equivalently, discount committed contracts) so that the sum of the advertising revenues earned from the firms under the two contract categories becomes equal. However, our findings, as stated next, suggest otherwise.

Proposition 3. Considering the scenario where the advertising agent imposes an additional charge δ on flexible contracts, we have the following results:

• The indifference point additional charge is negative, that is, $\delta ^ { * } < 0$

$\bullet \ I f \delta < 0 , | \delta | < | \delta ^ { * } | , o r \delta \geq 0 ,$ , then firms earn more, and the sum of the advertising revenues earned from the firms is less in flexible than committed competition.

$I f \delta < 0 , | \delta | = | \delta ^ { * } |$ , then firms are indifferent between participating in flexible and committed competition, and the sum of the advertising revenues earned from the firm under the two advertising competition is equal.

$I f \delta < 0 , | \delta | > | \delta ^ { * } | .$ , then firms earn more in committed than flexible competition.

From this proposition, because firms would stay in the competition where they earn more, the advertising agent needs to discount flexible contracts with δ , where $\delta \leq \delta ^ { * } < 0$ (or, equivalently, $\lvert \delta \rvert \geq \lvert \delta ^ { * } \rvert$ and $\delta < 0 )$ in order to maximize the sum of the advertising revenues earned from the two firms. In other words the advertising agent needs to move to the regions depicted in the last two bullets of the preceding proposition. The explanation is as follows. Note that the firms advertise less under flexible contracts. With the discount, the firms advertise more, and hence, the advertising competition between the firms intensifies. As a result, the advantage of flexible contracts (in terms of restraining overspending) disappears, and the firms become indifferent between flexible and committed contracts when $| \delta | = | \delta ^ { * } |$ . As the discount increases further, the firms would stay in committed competition, and the sum of the advertising revenues earned from the two firms remains unchanged.

In practice, advertising agents usually do not discount flexible contracts.<sup>2</sup> Thus, our finding seems to be at odds with what we observe in practice. Not discounting flexible contracts makes sense when advertisers do not actively compete; however, when the competitive forces are significant, advertising agents should offer a price break for flexible advertising contracts.

In fact, the finding in Proposition 3 can be compared to the practice of a manufacturer offering a free product return policy to two competing retailers in order to intensify the competition among those retailers. Padmanabhan and Png (1997) study this practice and find that by offering a free return for a product with uncertain demand, the retailers order more from the manufacturer and reduce prices to sell the product. Despite incurring a cost to offer free returns, the manufacturer may benefit from the increased sales of the product.

The finding in Proposition 3 sends an important message to the advertising agents that their common practice of discounting committed contracts, which is equivalent to imposing an additional charge on flexible contracts, may not serve their best interests when the interfirm competition is taken into consideration. It is also worth noting that the finding in Proposition 3 could not be obtained with conventional static models in which the difference between flexible and committed competition is not captured.

Next, we numerically examine how the flexible contract discount changes with the operational cost. For this numerical study, we let $r = 0 . 2 , h = 1 , k = 3 ,$ $a = 0 . 2 5 ,$ and $q = 0 . 2$ . From Figure 2, we find that the flexible contract discount decreases with the operational cost coefficient b. This is so because an increase in b can help restrain the tendency toward overadvertising. Hence, the advantage of flexible contracts also decreases. As a result, a smaller discount is sufficient to make firms indifferent between flexible and committed contracts. Next, we examine how the discount changes with the service quality (q). Our finding is summarized in the following lemma.

Lemma 3. As the exogenous service quality increases, the advertising agent needs to offer a larger flexible contract discount.

As shown in Lemma 3, the flexible contract discount increases with service quality. The explanation is as follows. As service quality increases, the tendency to overadvertise intensifies. This is so because at a higher service quality, the marginal profit from additional traffic is also higher, thereby generating a greater incentive for firms to compete for traffic. Thus, at a higher value of q, the advantage of a flexible contract increases, and as a result, the advertising agent needs to offer a larger discount. With additional numerical studies, we have the following observation.

Observation 1. The flexible contract discount needed to offer increases with the session value as well as the advertising cost coefficient.

The reason that the needed flexible contract discount increases with the session value is as follows. As the session value increases, the marginal benefit of advertising increases, intensifying the competition between the firms. Hence, the advantage of flexible over committed contracts also increases. As a result, a larger discount is needed to make firms indifferent between flexible and committed contracts. The reason that the flexible contract discount increases with the advertising cost coefficient is as follows. As the advertising cost coefficient increases, the effect of the same amount of advertising discount decreases; thus, a larger discount is needed to make firms indifferent between flexible and committed contracts

## 5. Model Extensions

We divide the analysis in this section into three parts. In the first part, we examine the scenario in which each firm makes joint decisions on advertising rate and service quality. In the second part, we conduct numerical studies to check whether the insights that we obtain under symmetric settings can carry over to asymmetric settings. In the third part, we study a model extension wherein firms use asymmetric advertising strategies.

Figure 2. Flexible Contract Discount as a Function of the Marginal Operational Cost  
![](/api/attachments/JP324GCM/fulltext/images/cd651428f9fc60b91d5f4c5444c779b5ed0d598d4d9bcaccd51d133b05a504e3.jpg)

## 5.1. Joint Decisions on Advertising Rate and Service Quality

In this section, we assume that each firm jointly optimizes the advertising rate and the service quality. As before, the firms compete for traffic under committed or flexible contracts. Under committed advertising contracts, the following simultaneous game ensues:

$$
\begin{array}{c} \max _ {A _ {i} (t), q _ {i}} \bigg \{\int_ {0} ^ {\infty} \bigg [ \frac {q _ {i}}{1 + q _ {i}} h _ {i} x _ {i} - k _ {i} A _ {i} (t) ^ {2} \\ - \left(a q _ {i} + b q _ {i} x _ {i}\right) \bigg ] e ^ {- r _ {i} t} d t \bigg \}, \quad i \in \{1, 2 \}. \end{array}\tag{13}
$$

The state equation is the same as Equation (2).

From Lemma 1, substituting $A _ { i } ^ { * } = \epsilon _ { i } ^ { * } \sqrt { 1 - x _ { i } }$ into (13), we have

$$
\begin{array}{c} \max _ {q _ {i}} \Bigg \{\int_ {0} ^ {\infty} \bigg [ \frac {q _ {i}}{1 + q _ {i}} h _ {i} x _ {i} - k _ {i} \epsilon_ {i} ^ {2} (1 - x _ {i}) \\ - \left(a q _ {i} + b q _ {i} x _ {i}\right) \bigg ] e ^ {- r _ {i} t} d t \Bigg \}, \quad i \in \{1, 2 \}. \end{array}\tag{14}
$$

We obtain the profits of the firms as follows:

$$
\begin{array}{l} \Pi_ {i} = \left(\frac {q _ {i} h _ {i}}{1 + q _ {i}} - b q _ {i} + k _ {i} \epsilon_ {i} ^ {2}\right) \left(\frac {\epsilon_ {i}}{r _ {i} (\epsilon_ {1} + \epsilon_ {2})} + \frac {1}{r _ {i} + \epsilon_ {1} + \epsilon_ {2}} \right. \\ \left. \cdot \left(x _ {o i} - \frac {\epsilon_ {i}}{\epsilon_ {1} + \epsilon_ {2}}\right)\right) - \frac {k _ {i} \epsilon_ {i} ^ {2} + a q _ {i}}{r _ {i}}, \end{array}
$$

where $x _ { o 1 } = x _ { 0 }$ and $x _ { o 2 } = 1 - x _ { 0 }$

Taking the first-order derivative of $\Pi _ { i }$ with respect to $q _ { i } ,$ we have

$$
\frac {d \Pi_ {i}}{d q _ {i}} = \frac {\partial \Pi_ {i}}{\partial q _ {i}} + \frac {\partial \Pi_ {i}}{\partial \epsilon_ {i}} \frac {d \epsilon_ {i}}{d q _ {i}} + \frac {\partial \Pi_ {i}}{\partial \epsilon_ {j}} \frac {d \epsilon_ {j}}{d q _ {i}} = 0.\tag{15}
$$

After obtaining the expressions for $\frac { \partial \Pi _ { i } } { \partial q _ { i } } , \frac { \partial \Pi _ { i } } { \partial \epsilon _ { i } } , \frac { \partial \Pi _ { i } } { \partial \epsilon _ { j } }$ $\textstyle { \frac { d \epsilon _ { i } } { d q _ { i } } } , { \frac { d \epsilon _ { j } } { d q _ { i } } }$ and substituting them into (15), we then solve for $q _ { i } ^ { c * }$ . For tractability, we consider a symmetric setting where $x _ { 0 } = 0 . { \dot { 5 } } , r _ { 1 } = r _ { 2 } = r , h _ { 1 } = h _ { 2 } = h , k _ { 1 } =$ $k _ { 2 } = k$ . Under such a setting, x stays at $1 / 2 ,$ , and $\epsilon _ { 1 } =$ $\begin{array} { r } { \epsilon _ { 2 } = \epsilon = \frac { - r + \sqrt { r ^ { 2 } + 2 ( q h / ( 1 + q ) - b q ) / k } } { 2 } , } \end{array}$ . Thus, from (15), we have

$$
\begin{array}{c} {1 - \frac {2 a}{h / (1 + q) ^ {2} - b} + \left(\frac {q h}{1 + q} - b q - 2 k \epsilon (r + \epsilon)\right)} \\ {\cdot \frac {1}{2 k (r + \epsilon) (r + 2 \epsilon)} = 0.} \end{array}\tag{16}
$$

Note that because $\begin{array} { r } { \epsilon = \frac { - r + \sqrt { r ^ { 2 } + 2 ( q h / ( 1 + q ) - b q ) / k } } { 2 } . } \end{array}$ , we have $\begin{array} { r } { \frac { q h } { 1 + q } - b q - 2 k \epsilon ( r + \epsilon ) = 0 } \end{array}$ . Solving Equation (16), we obtain

$$
q ^ {c *} = \sqrt {\frac {h}{2 a + b}} - 1,\tag{17}
$$

where the superscript $c$ stands for committed advertising competition.

Under flexible advertising competition, we have the following simultaneous game:

$$
\begin{array}{c} \max _ {A _ {i} (x _ {i}, t), q _ {i}} \bigg \{J _ {i} = \int_ {0} ^ {\infty} \bigg [ \frac {q _ {i}}{1 + q _ {i}} h _ {i} x _ {i} - k _ {i} A _ {i} (x _ {i}, t) ^ {2} \\ - \big (a q _ {i} + b q _ {i} x _ {i} \big) \bigg ] e ^ {- r _ {i} t} d t \bigg \}, \quad i \in \{1, 2 \}. \end{array}\tag{18}
$$

As before, the evolution of the state is governed by Equation (2).

Following a similar procedure, under the symmetric setting, we can obtain $q ^ { f * }$ , where the superscript f stands for flexible advertising competition from the following equations:

$$
q = \sqrt {\frac {h}{2 a (r + \eta) (r + 3 \eta) / (r + 2 \eta) ^ {2} + b}} - 1,\tag{19}
$$

$$
\eta = \frac {- r + \sqrt {r ^ {2} + 3 (q h / (1 + q) - b q) / k}}{3}.\tag{20}
$$

From (17) and (19), we have the following lemma.

Lemma 4. Consider a symmetric setting where each firm jointly optimizes the advertising rate and the service quality • The service quality under flexible competition is higher than that under committed competition $( i . { \dot { e } } . , q ^ { f * } > q ^ { c * } )$

• The service quality under committed competition decreases with the operational cost coefficient b.

Under flexible contracts, the competition is less intense and the advertising effort spent by the firms is lower. This increases the marginal benefit of service quality. As a result, the optimal service quality under flexible contracts is set to a higher value. Lemma 4 also shows that the service quality under committed contracts decreases with b, which is self-explanatory, because b is the marginal cost of service quality.

5.1.1. Numerical Studies. Even for symmetric settings, additional analysis of the results does not easily lend itself to an analytical approach. Hence, we resort to numerical studies and obtain the following observations. For the numerical studies in this subsection, we keep $r = 0 . 2 , h = 2 , k = 3 , a = 0 . 1$ while varying the value of b from 0.01 to 0.1 with an increment of 0.01

Observation 2. The service quality chosen under flexible contracts decreases with the marginal operational cost (b).

As the marginal operational cost increases, the optimal service quality level naturally decreases. This result is in line with what we have found under committed contracts.

Observation 3. The advertising rate under both committed and flexible contracts decreases with the marginal operational cost (b). The advertising rate under committed contracts is higher than that under flexible contracts.

Under symmetric parameter settings, firm’s advertising rates under committed and flexible competition are $\Breve { A } ^ { c } = \epsilon ^ { * } / \sqrt { 2 }$ and $A ^ { f } = \eta ^ { * } / \sqrt { 2 }$ , respectively. Hence, a comparison of advertising rates is equivalent to comparing $\epsilon ^ { * }$ and $\eta ^ { * }$ , which, in turn, can be obtained from (9) and (11) with $q ^ { c * }$ and $q ^ { f * }$ , respectively. The result that firms advertise more under committed contracts is consistent with that in Proposition 1, wherein the service quality q is exogenous. The intuition for the advertising rate to decrease with b is that the higher operational cost results in the lower service quality, which, in turn, makes advertising less effective. The intuition for the advertising rate being higher for committed contracts is similar to the case of exogenous service quality. The ability of a firm to change its effort in a flexible contract restrains a firm’s tendency toward overadvertising in fear of retaliation by the other firm.

From (13) and (18), we obtain the total profits of each firm under committed and flexible contracts, respectively:

$$
\Pi^ {c *} = \frac {1}{r} \left(\frac {q ^ {c *} h}{2 (1 + q ^ {c *})} - \frac {1}{2} (\epsilon^ {*}) ^ {2} k - \left(a q ^ {c *} + \frac {b q ^ {c *}}{2}\right)\right),\tag{21}
$$

$$
\Pi^ {f *} = \frac {1}{r} \left(\frac {q ^ {f *} h}{2 (1 + q ^ {f *})} - \frac {1}{2} (\eta^ {*}) ^ {2} k - \left(a q ^ {f *} + \frac {b q ^ {f *}}{2}\right)\right).\tag{22}
$$

Additional numerical analysis reveals the following finding.

Observation 4. A firm’s profit in either mode of competition decreases with marginal operational cost (b). Furthermore, the firms are better off under flexible competition relative to committed competition, but the advantage of flexible over committed competition decreases as operational costs increase.

Similar to the result in Proposition 2, Observation 4 shows that as the marginal operational cost (b) increases, the advantage of flexible over committed contracts decreases. The intuition is that operational costs act as a mechanism to restrain a firm’s tendency toward overadvertising. As before, firms prefer flexible contracts, making the advertising agent worse off.

Our observations from numerical studies suggest that for comparative statics, endogenizing service quality does not change the qualitative nature of the results when compared with the case where the service quality was exogenous. Next, we investigate whether the endogenization of service quality would affect the pricing decisions of the advertising agent.

5.1.2. Pricing. Once again, we consider a price intervention by the advertising agent to recover any lost revenue. The order of the game is as follows:

1. The advertising agent announces the additional charge δ for flexible contracts.

2. Firms choose committed or flexible contracts and set the optimal service quality accordingly under the chosen contract.

The advertising agent needs to identify the optimal $\delta ^ { * }$ at which the advertising spending is highest, subject to the condition that the firms are not worse off under flexible contracts. The problem of identifying $\delta ^ { * }$ can be formulated as

$$
\begin{array}{r l} & {\delta^ {*} = \arg \max _ {\delta} (k + \delta) \bigl (A ^ {f} \bigr) ^ {2},} \\ & {\qquad \mathrm{s.t.} \Pi^ {f *} \bigl (k + \delta , q ^ {f *} \bigr) \geq \Pi^ {c *} \bigl (k, q ^ {c *} \bigr),} \end{array}\tag{23}
$$

where $\Pi ^ { c * }$ and $\Pi ^ { f * }$ can be obtained from (21) and (22), respectively. Here $\epsilon ^ { * }$ and $\eta ^ { * }$ in (21) and (22) can be calculated as follows:

$$
\epsilon^ {*} = \frac {- r + \sqrt {r ^ {2} + 2 \Gamma (q ^ {c *}) / k}}{2},\tag{24}
$$

$$
\eta^ {*} = \frac {- r + \sqrt {r ^ {2} + 3 \Gamma (q ^ {f *}) / (k + \delta)}}{3}.\tag{25}
$$

In these expressions, $q ^ { c * }$ can be obtained from (17), and with the flexible contract discount, $q ^ { f * }$ can be obtained from (19) and (25).

Additional numerical analysis reveals the following finding.

Observation 5. The advertising agent needs to discount the flexible contracts $\left( \mathrm { i . e . , } \delta ^ { \ast } < 0 \right)$ so as to ensure that the firms are indifferent between participating in flexible and committed competition.

This result is qualitatively in line with that in the basic model where service quality is exogenous. However, the amount of the discount that the agent needs to offer in this joint decision model can be different from that in the basic model. At the profit indifference point, the sum of the advertising revenues earned from the firms under flexible competition is still lower than that under committed competition However, as the discount increases even more, firms would be better off participating in the committed competition. By contrast, our finding in the basic model is slightly different. The indifference point for firms’ profits and that for advertising costs occur at the same value of δ. This is so because in the basic model we set the same values for $q$ in flexible and committed competition, and the only difference in comparison lies in the advertising costs, whereas in the joint decision model the optimal values of the service quality under the two modes of competition can be different from one another (the optimal service quality under flexible competition is set to a higher value than that under committed competition).

## 5.2. Asymmetric Firms

Here we make a comparison between flexible and committed competition under the general setting where the two firms can have asymmetric parameter values. Under the general setting, from (4), we have firms profits under committed competition as

$$
\begin{array}{r} \Pi_ {i, c, c} = \frac {1}{r _ {i}} \left(\frac {\epsilon_ {1} \Gamma_ {i}}{\epsilon_ {1} + \epsilon_ {2}} - k _ {i} \epsilon_ {i} ^ {2} \frac {\epsilon_ {2}}{\epsilon_ {1} + \epsilon_ {2}} - a q _ {i}\right) \\ + \frac {1}{r _ {i} + \epsilon_ {1} + \epsilon_ {2}} (\Gamma_ {i} + k _ {i} \epsilon_ {i} ^ {2}) (x _ {0} - \frac {\epsilon_ {1}}{\epsilon_ {1} + \epsilon_ {2}}). \end{array}\tag{26}
$$

Similarly, under the general setting, from (7), we have firms’ profits under flexible competition as

$$
\begin{array}{r l} & {\Pi_ {i, f, f} = \frac {1}{r _ {i}} \left(\frac {\eta_ {1} \Gamma_ {i}}{\eta_ {1} + \eta_ {2}} - k _ {i} \eta_ {i} ^ {2} \frac {\eta_ {2}}{\eta_ {1} + \eta_ {2}} - a q _ {i}\right)} \\ & {\qquad + \frac {1}{r _ {i} + \eta_ {1} + \eta_ {2}} \big (\Gamma_ {i} + k _ {i} \eta_ {i} ^ {2} \big) \Big (x _ {0} - \frac {\eta_ {1}}{\eta_ {1} + \eta_ {2}} \Big).} \end{array}\tag{27}
$$

Because the analytical comparison of firms’ profits under committed and flexible competition (as just shown) is not tractable, we need to resort to numerical analysis. Let $r _ { 1 } = 0 . 3 , r _ { 2 } = 0 . 4 , h _ { 1 } = 1 , h _ { 2 } = 2 ,$ $k _ { 1 } = 2 , k _ { 2 } = 3 , q _ { 1 } = 0 . 5 , q _ { 2 } = 0 . 6 , a = 0 . 1 , b = 0 . 0 5 , x _ { 0 } = 0 . 4 .$ We present firms’ profits in Table 2 (the higher values of the profits of a given firm in committed and flexible competition are in bold).

As shown in the table, the profits of firms 1 and 2 under committed competition are 0.1667 and 0.4164, respectively, whereas their profits under flexible competition are 0.1810 and 0.4279, respectively. Clearly, both firms are better off under flexible competition. We summarize these numerical findings in the following observation.

Observation 6. Under asymmetric settings, both firms can be better off under flexible competition.

Next, we would like to examine whether there exists a scenario where both firms are better off under committed competition compared with flexible competition. Unfortunately, with extensive numerical studies, we are unable to find any such instance.

Table 2. Both Firms Are Better Off Under Flexible Competition in the Asymmetric Setting

<table><tr><td>Firm</td><td>Committed</td><td>Flexible</td></tr><tr><td>Firm 1</td><td>0.1667</td><td>0.1810</td></tr><tr><td>Firm 2</td><td>0.4164</td><td>0.4279</td></tr></table>

Note. The higher values of the profits of a given firm in committed and flexible competition are in bold.

However, we are able to identify instances in which only one firm is better off under committed competition. For instance, consider the following parameter values: $r _ { 1 } = 0 . 3 , r _ { 2 } = 0 . 6 , h _ { 1 } = 1 , h _ { 2 } = 1 . 2 , k _ { 1 } = 2 , k _ { 2 } = 2 . 5 ,$ $q _ { 1 } = 0 . 1 , q _ { 2 } = 0 . 2 , a = 0 . 1 , b = 0 . 2 , x _ { 0 } = 0 . 3 .$ We present firms’ profits in Table 3. As shown in the table, the profits of firms 1 and 2 under committed competition are 0.0387 and 0.0478, respectively, whereas their profits under flexible competition are 0.0391 and 0.0476, respectively. That is, firm 1 is better off under flexible competition, whereas firm 2 is better off under committed competition. However, the sum of profits of the two firms under flexible competition is 0.0867, which is higher than the firms’ total profits (0.0865) under committed competition. Therefore, in this case, from a social perspective, the sum of profits of the two firms is still higher under flexible competition. We summarize this finding in the following observation.

Observation 7. Under asymmetric settings, it is possible that one firm is better off under committed competition, whereas the other firm is better off under flexible competition. However, from a social perspective (i.e., the sum of profits of the two firms), flexible competition is still the preferable choice.

Here we conclude that our earlier finding under symmetric settings that firms are better off under flexible competition still holds qualitatively under asym metric settings.

Additionally, we examine how operational costs affect the advantage of flexible over committed competition under asymmetric settings. Our numerical analysis reveals that as operational costs increase, the advantage of flexible over committed advertising competition decreases, which is in line with the result that we obtain under symmetric settings (see Proposition 2 in Section 4). We also examine the impact of firm asymmetry with respect to session value. To that end, we set $r _ { 1 } \stackrel { . } { = } r _ { 2 } = 0 . 3 , \stackrel { . } { q _ { 1 } } = q _ { 2 } = 0 . 1 , k _ { 1 } = k _ { 2 } = 2 ,$ $a = 0 . 1 , b = \ 0 . 2 , x _ { 0 } = 0 . 5 , h _ { 1 } = 1$ , and we vary the value of h from 1 to 3 with an increment of 0.2. Recall that we use Δ to denote the advantage of flexible over committed advertising competition (i.e., the differ ence between the sum of the profits of the firms under flexible and committed advertising competition). We depict Δ as a function of $h _ { 2 }$ in Figure 3. As we can see from the figure, as the session value of firm 2 increases, the difference in the sum of the profits of the two firms under the two modes of competition first increases and then decreases, peaking at $h _ { 2 } = 2 . 4$ . The impact of changing $h _ { 1 }$ (while keeping $h _ { 2 }$ fixed) would be similar.

Table 3. Sum of Profits of Firms Under the Asymmetric Setting

<table><tr><td></td><td>Committed</td><td>Flexible</td></tr><tr><td>Firm 1</td><td>0.0387</td><td>0.0391</td></tr><tr><td>Firm 2</td><td>0.0478</td><td>0.0476</td></tr><tr><td>Sum of profits</td><td>0.0865</td><td>0.0867</td></tr></table>

Note. The higher values of the profits of a given firm in committed and flexible competition are in bold

Figure 3. Difference in Profits of Firms Under Two Modes of Competition as a Function of $h _ { 2 }$  
![](/api/attachments/JP324GCM/fulltext/images/78eebf25d3c4880bd77713ebda8ce4cda1eedac59206f64970f331c1c737da71.jpg)

## 5.3. Competition with Asymmetric Advertising Strategies

So far we have studied the scenarios where both firms use the same advertising strategies $( \mathrm { i . e . , }$ either both choose committed advertising contracts or both choose flexible contracts). However, in practice, because of certain organizational constraints, firms may end up choosing asymmetric advertising strategies. Next, we examine how firms’ dynamic competition plays out under this situation. For tractability, we focus on the scenario where $q _ { i }$ is exogenous. Without loss of generality, we assume that firm 1 uses the flexible competition $( \mathrm { i . e . , }$ , closed-loop) strategy, whereas firm 2 uses the committed competition $( \mathrm { i . e . , }$ , open-loop) strategy. In such a case, the control variables of firms 1 and 2 are denoted by $A _ { 1 } ( x , t )$ and $A _ { 2 } ( t )$ , respectively. Following the analysis in Section 4.4, we change the advertising cost coefficient under flexible contracts from k to $k + \bar { \delta }$

The problems of firms 1 and 2, respectively, are

$$
\begin{array}{c} \max _ {A _ {1} (x, t)} \bigg \{J _ {1} = \int_ {0} ^ {\infty} \bigg [ \frac {q _ {1}}{1 + q _ {1}} h _ {1} x _ {1} - (k _ {1} + \delta) A _ {1} (x, t) ^ {2} \\ - \left(a q _ {1} + b q _ {1} x _ {1}\right) \bigg ] e ^ {- r _ {1} t} d t \bigg \}, \end{array}\tag{28}
$$

$$
\begin{array}{c} \max _ {A _ {2} (t)} \bigg \{J _ {2} = \int_ {0} ^ {\infty} \bigg [ \frac {q _ {2}}{1 + q _ {2}} h _ {2} x _ {2} - k _ {2} A _ {2} (t) ^ {2} \\ - \left(a q _ {2} + b q _ {2} x _ {2}\right) \bigg ] e ^ {- r _ {2} t} d t \bigg \}, \end{array}\tag{29}
$$

where $x _ { 1 } = x$ and $x _ { 2 } = 1 - x .$

The state equation of this differential game is

$$
\begin{array}{l} \dot {x} (t) = \frac {d x (t)}{d t} = A _ {1} (x, t) \sqrt {1 - x (t)} - A _ {2} (t) \sqrt {x (t)}, \\ x (0) = x _ {0} \in [ 0, 1 ], \end{array}\tag{30}
$$

where $x _ { 0 }$ is the initial arriving traffic at firm 1.

The results of this differential game are summarized in Lemma 5 below.

Lemma 5. A Nash equilibrium for this competition is

$$
A _ {i} = \xi_ {i} \sqrt {1 - x _ {i}} = \xi_ {i} \sqrt {x _ {j}}, \quad \{i, j \} = \{1, 2 \},
$$

where $\left( \xi _ { 1 } , \xi _ { 2 } \right)$ is the unique solution of

$$
r _ {1} \xi_ {1} + \frac {\xi_ {1} ^ {2}}{2} + \frac {\xi_ {1} \xi_ {2}}{2} - \frac {\Gamma_ {1}}{2 (k _ {1} + \delta)} = 0,\tag{31}
$$

$$
r _ {2} \xi_ {2} + \frac {\xi_ {2} ^ {2}}{2} + \xi_ {1} \xi_ {2} - \frac {\Gamma_ {2}}{2 k _ {2}} = 0;\tag{32}
$$

this satisfies $\xi _ { i } \ge 0 , \ i = 1 , 2$ . The state trajectory corresponding to this equilibrium is given by

$$
x (t) = \frac {\xi_ {1}}{\xi_ {1} + \xi_ {2}} + \left[ x _ {0} - \frac {\xi_ {1}}{\xi_ {1} + \xi_ {2}} \right] e ^ {- (\xi_ {1} + \xi_ {2}) t}.\tag{33}
$$

Following the analysis in the preceding subsection, under the symmetric setting where $x _ { 0 } = 0 . 5 ,$ $\begin{array} { r } { r _ { 1 } = r _ { 2 } = r , h _ { 1 } = h _ { 2 } = h , q _ { 1 } = q _ { 2 } = q , k _ { 1 } = k _ { 2 } = k , } \end{array}$ we have

$$
r \xi_ {1} + \frac {\xi_ {1} ^ {2}}{2} + \frac {\xi_ {1} \xi_ {2}}{2} - \frac {\Gamma}{2 (k + \delta)} = 0,\tag{34}
$$

$$
r \xi_ {2} + \frac {\xi_ {2} ^ {2}}{2} + \xi_ {1} \xi_ {2} - \frac {\Gamma}{2 k} = 0.\tag{35}
$$

Because the closed-form expression for $\xi _ { i } ^ { * }$ is not available, we need to numerically solve for $\boldsymbol { \xi } _ { i } ^ { * }$ . After it is solved, the total advertising cost $\textstyle \int _ { 0 } ^ { \infty } k A _ { i } ^ { 2 } e ^ { - r t } d t =$ $\begin{array} { r } { \int _ { 0 } ^ { \infty } k ( \xi _ { i } ^ { * } ) ^ { 2 } ( 1 - x ) e ^ { - r t } d t } \end{array}$ can be calculated as follows:

$$
\begin{array}{l} \left(k + \frac {1 - (- 1) ^ {i}}{2} \delta\right) \xi_ {i} ^ {2} \\ \cdot \left(\frac {\xi_ {1} + \xi_ {2} - \xi_ {i}}{r (\xi_ {1} + \xi_ {2})} - \left(x _ {0} - \frac {\xi_ {1}}{\xi_ {1} + \xi_ {2}}\right) \frac {(- 1) ^ {i + 1}}{\xi_ {1} + \xi_ {2} + r}\right). \end{array}
$$

Furthermore, we can calculate firms’ profits using the following formula:

$$
\begin{array}{l} \Pi_ {i} = \bigg (\Gamma + \bigg (k + \frac {1 - (- 1) ^ {i}}{2} \delta \bigg) \xi_ {i} ^ {2} \bigg) \bigg (\frac {\xi_ {i}}{r (\xi_ {1} + \xi_ {2})} \\ \qquad - \bigg (x _ {0} - \frac {\xi_ {1}}{\xi_ {1} + \xi_ {2}} \bigg) \frac {(- 1) ^ {i}}{\xi_ {1} + \xi_ {2} + r} \bigg) \\ \qquad - \frac {1}{r} \left(\bigg (k + \frac {1 - (- 1) ^ {i}}{2} \delta \bigg) \xi_ {i} ^ {2} + a q\right). \end{array}
$$

From (34) and (35), we have $\begin{array} { r } { r \xi _ { 1 } + \frac { \xi _ { 1 } ^ { 2 } } { 2 } = r \xi _ { 2 } + \frac { \xi _ { 2 } ^ { 2 } } { 2 } + \frac { \xi _ { 1 } \xi _ { 2 } } { 2 } } \end{array}$ when $\delta = 0$ , which indicates that $\xi _ { 1 } ^ { * } > \xi _ { 2 } ^ { * }$ when $\delta = 0$ This finding is summarized in the following lemma.

Lemma 6. Under symmetric settings, when there is no additional charge on flexible contracts $( i . e . , \delta = 0 )$ , we have the following results:

• The firm using flexible strategy advertises more than the one using committed strategy.

• The firm using flexible strategy advertises more than that under committed competition, whereas the firm using committed strategy advertises less than that under flexible competition.

Here the following interesting question naturally arises: is it possible for firms to use asymmetric advertising strategies in equilibrium? To explore this question, we examine a situation where the mode of advertising, committed or flexible, is chosen by each firm in equilibrium. The order of play is as follows:

1. The two firms simultaneously choose and commit themselves to either a committed (denoted by c) or a flexible (denoted by f ) advertising strategy.

2. Given their choice of mode of advertising, the firms determine their respective advertising rates in the differential game.

The solution process is in the reverse order, as is customary in backward induction. We first find the equilibrium profits of the two firms under four possible combinations of scenarios: $( f , f ) , ( c , f ) , ( f , c ) , \bar { ( } c , c )$ Then we find the equilibrium among these four scenarios. Because the profits of firms under $\left( c , f \right)$ and $( f , c )$ cannot be obtained analytically, we have to resort to numerical methods. Next, we illustrate an equilibrium outcome using the following numerical example. Letting $r = 0 . 2 , \dot { h = 1 } , k = 3 , q = \bar { 0 } . 1 , a = 0 . 2 5$ $b = 0 . { \overset { \cdot } { 0 } } 5 , x _ { 0 } = 0 . { \overset { \cdot } { 5 } } , \delta = - 1$ , we present firms’ profits in Table 4.

Table 4. Firms Choose the Mode of Flexible Advertising in Equilibrium

<table><tr><td></td><td colspan="2">Firm 2</td></tr><tr><td>Firm 1</td><td>Committed</td><td>Flexible</td></tr><tr><td>Committed</td><td>(0.0663, 0.0663)</td><td>(0.0490, 0.0826)</td></tr><tr><td>Flexible</td><td>(0.0826, 0.0490)</td><td>(0.0651, 0.0651)</td></tr></table>

Note. The higher values of the profits of a given firm in committed and flexible competition are in bold

As shown in the table, when the advertising agent discounts flexible contracts by one unit $( \mathrm { i } . \mathrm { e } . , \delta = - 1 )$ both firms end up using flexible advertising in equilibrium. Additional analysis reveals that under this parameter setting, the sum of the advertising revenues earned from the two firms reaches the highest value when they stay in equilibrium. Thus, the equilibrium is also the preferred outcome of the advertising agent. Next, we consider a scenario where the additiona charge on flexible contracts is one unit $( \mathrm { i . e . , ~ } \delta = 1 )$ whereas the values of other parameters remain the same as in the preceding example. We present firms profits in Table 5.

As shown in the table, when $\delta = 1 _ { \cdot }$ , firms end up staying in an equilibrium where they both use committed advertising, although they would earn more under flexible advertising. Additional analysis reveals that the sum of the advertising revenues earned from the two firms reaches the highest value when the firms stay in equilibrium. Based on this analysis, because the advertising revenues under the committed competition remain the same regardless of δ, it is better for the advertising agent to set the value of δ to <sup>−</sup>1 instead of 1.

Next, we set the values of δ and q to 0.6 and 0.2, respectively, while keeping the values of other parameters the same as in the preceding example. We present firms’ profits in Table 6.

As shown in the table, firms end up using asym metric advertising strategies (i.e., one firm uses committed advertising strategy, whereas the other firm uses flexible one) in equilibrium. Additional analysis reveals that the sum of the advertising revenues earned from the firms reaches the highest value when they both use committed advertising strategies.

Table 5. Firms Choose the Mode of Committed Advertising in Equilibrium

<table><tr><td></td><td colspan="2">Firm 2</td></tr><tr><td>Firm 1</td><td>Committed</td><td>Flexible</td></tr><tr><td>Committed</td><td>(0.0663, 0.0663)</td><td>(0.0765, 0.0633)</td></tr><tr><td>Flexible</td><td>(0.0633, 0.0765)</td><td>(0.0729, 0.0729)</td></tr></table>

Note. The higher values of the profits of a given firm in committed and flexible competition are in bold.

Table 6. Firms Choose the Mode of Asymmetric Advertising in Equilibrium

<table><tr><td></td><td colspan="2">Firm 2</td></tr><tr><td>Firm 1</td><td>Committed</td><td>Flexible</td></tr><tr><td>Committed</td><td>(0.0809, 0.0809)</td><td>(0.0965, 0.0821)</td></tr><tr><td>Flexible</td><td>(0.0821, 0.0965)</td><td>(0.0963, 0.0963)</td></tr></table>

Note. The higher values of the profits of a given firm in committed and flexible competition are in bold.

In sum, one of the four equilibrium outcomes $( { \mathrm { i . e . , } } ( c , c ) , ( f , f ) , ( c , f )$ , and $( f , c ) )$ ) may exist depending on the parameter values. To illustrate, we further depict the regions of the Nash equilibrium and the regions of the advertising strategy combination with the largest sum of advertising revenues in Figure $4 , \ ( \mathrm { a } )$ and (b), respectively. Here we vary the parameter value of δ from –1.5 to 1.5 and that of q from 0 to 0.25 while keeping the values of the other parameters unchanged $( r = \bar { 0 } . 2 , \bar { h } = 1 , k = 3 , a = 0 . 2 5 , b = \bar { 0 . 0 5 } , x _ { 0 } = 0 . 5 )$ . For convenience, we hereafter refer to the advertising strategy combinations $( c , f )$ and $( f , c )$ as asymmetric.

As shown in Figure 4(a), when the advertising agent discounts flexible contracts $( \mathrm { i . e . , } \delta < 0 )$ , the only possible equilibrium is $( f , f )$ . Additional analysis reveals that in certain regions of $( \delta , q ) , \delta < 0 , ( f , \dot { f } )$ is a prisoner’s dilemma equilibrium because the firms would earn more in $( c , c )$ . However, with an additional charge on flexible contracts $( \mathrm { i . e . , ~ } \delta > 0 )$ , as δ increases, the Nash equilibrium changes from $( f , f )$ to $( f , c )$ or $( c , f )$ and, ultimately, to $( c , c )$ . As shown in Figure 4, when $( c , c )$ is a Nash equilibrium, the sum of the advertising revenues earned from the firms under $( c , c )$ , which remains the same regardless of $\delta ,$ is the highest among all the advertising strategy combinations. However, for a given q, when $( f , f )$ is a Nash equilibrium, if the advertising discount is sufficiently large, the sum of the advertising revenues earned from the firms in $( f , f )$ would be the highest among all the advertising strategy combinations, including (c, c). Hence, it would be better for the advertising agent to set $\delta < 0 ,$ , where δ is sufficiently large, rather than to set $\delta > 0$ . Another interesting question naturally arises as follows: what is the optimal advertising discount that the advertising agent should offer to the firms under flexible contracts? In view of the analytical intractability, we address this question with numerical methods. In Figure 5, we vary the values of δ from <sup>−</sup>2.9999 to 1 and show the sum of the advertising revenues earned from the firms in $( c , c ) , ( c , f ) , ( f , c ) .$ and $( f , f )$

As shown in the figure, the sum of the advertising revenues in $( f , f )$ increases convexly with the amount of advertising discount as <sub>|</sub>δ<sub>|</sub> approaches k (i.e., as δ approaches $- k )$ , where the value of k is set to 3 in this analysis. Additionally, the sum of the advertising revenues when δ is close to –3 is significantly higher in $( f , f )$ than that in $( c , c )$ . Thus, for a given q, the best strategy for the advertising agent is to offer the firms under flexible contracts a discount that is close to the advertising cost coefficient k. In this way, the advertising competition between the firms under flexible contracts becomes extremely intense, leading to dramatically increased revenues for the advertising agent.

Next, we summarize our main findings in this section. First, the results that we obtain under the assumption that each firm jointly optimizes its advertising rate and service quality are qualitatively consistent with those under the assumption that firms service quality is exogenous. However, the amount of discount that the agent needs to offer in the former case can be different from that in the latter case. Second, the main analytical findings that we obtain under the symmetric parameter settings can also carry over to the scenario where the model parameter values are asymmetric. Third, we find that when the firms are allowed to compete with asymmetric advertising strategies, the firm using flexible strategy advertises more than the one using committed strategy, and the firms may adopt symmetric or asymmetric advertising strategies in equilibrium depending on the parameter values.

Figure 4. Nash Equilibrium and Advertising Strategy Combination with the Largest Sum of Advertising Revenues  
![](/api/attachments/JP324GCM/fulltext/images/128c97bd0eca7a1154278d9bc5b3d22ac9da9af893d84585f98077244608c0a3.jpg)  
(a) Nash Equilibrium

![](/api/attachments/JP324GCM/fulltext/images/9f90c8719cde50ac6e4f1bf8a8a584dbc94b62712ddb0dacfd467e5be480467b.jpg)  
(b) Advertising Revenue

Figure 5. Sum of Advertising Revenues Under Different Advertising Strategy Combinations  
![](/api/attachments/JP324GCM/fulltext/images/2b7afde807e04d3900f45bbce31369f9be88d421f02c0ceed9bdd63e70141c40.jpg)

## 6. Conclusions and Future Research Directions

Over the past decades, advertising competition among e-retailers has become more and more intense. When signing contracts for advertising campaigns, e-retailers are often faced with the following two options. One option is to sign flexible advertising contracts that would allow the e-retailer to continuously adjust their level of advertising during the campaign. The other one is to sign committed contracts that would disallow any adjustment by the e-retailers with respect to advertising during the campaign; thus, the e-retailers need to commit to the planned trajectory for advertising rates throughout the campaign. To study the performance of the e-retailers engaged in the dynamic advertising competition as well as the revenue of advertising agents under the two types of advertising contracts, we adopt a differential games framework. In particular, we use a closed-loop differential games framework to examine the performance of the firms engaged in flexible advertising competition and an open-loop framework for the firms engaged in committed advertising competition. Furthermore, we study how the consideration of IT operations affects the performance of firms under the two modes of dynamic advertising competition.

One of our main findings is that firms can be better off under flexible advertising competition. This is mainly because firms under flexible competition have the leverage of flexibility to adjust their advertising rates based on the realized market share during the competition, thereby reducing their advertising efforts. However, this leverage decreases as IT becomes more costly. The explanation for this result is as follows. Firms tend to overadvertise in the presence of competition. Flexible competition serves as a means for the firms to restrain their tendency toward overadvertising. Similarly, firms tend to advertise more conservatively when IT becomes more costly. Given that the firms’ tendency toward overadvertising is more restrained as IT becomes more costly, the benefit of flexibility (in flexible competition) becomes less pronounced.

However, because the revenue of the advertising agent equals the sum of the advertising spending of the e-retailers, the preferable choice of the agent is committed competition, which is clearly different from that of the e-retailers. To resolve such a conflict, we suggest that the advertising agent uses a differential pricing scheme under different modes of competition. At the first glance, one would think that the advertising agent needs to impose additional advertising charges on firms engaged in flexible competition so as to discourage them from engaging in such a competition. Interestingly, we find that this is not the case. To achieve its optimality, the advertising agent needs to offer discounts rather than impose additional charges to the firms engaged in flexible competition. This is mainly because the additional discounts offered to the firms under flexible competition can help step up the competition, thereby leading to higher advertising spending at each firm. Moreover, we find that the optimal discounts being offered under flexible competition decrease as operational costs increase. This is mainly because higher operational costs would help better restrain firms’ tendency toward overadvertising, thus reducing the difference in advertising spending between flexible and committed competition. As a result, the discounts needed to step up the advertising competition under flexible competition decrease.

In practice, our findings have important managerial implications for firms engaged in dynamic advertising competition. For e-retailing firms, we would recommend that they choose the flexible advertising contracts, which give them the flexibility of adjusting their advertising spending during the advertising campaign and make them better off. We also send a clear message to the e-retailers that their leverage of engaging in the flexible competition is contingent on the size of their operational costs. In particular, as the operational costs decrease, they should be more mindful of engaging in flexible competition. However, from the standpoint of advertising agents (e.g., Facebook.com), because firms’ advertising efforts are lower in flexible than committed competition, we would recommend that the advertising agents adopt differential pricing schemes (e.g., set different values for k) under the two modes of competition. In particular, the agents need to offer discounts to e-retailers signing flexible advertising contracts so as to step up the advertising competition. In addition, our findings also provide the advertising agents with guidance on how to determine the optimal value for the discounts to be offered.

Our study has several limitations. One limitation lies in the simplifying assumption of symmetric model parameters that we have made in order to obtain analytically tractable results. Another limitation is that we have modeled a scenario where there exists only one advertising agent. That is, we purposely leave out the issue of competition among advertising agents so as to focus on the analysis of advertising competition between e-retailers. There are many possible directions for future research. For example, it would be interesting to examine the equilibrium outcomes when firms service quality and their modes of dynamic competi tion are both endogenized. In addition, it would be interesting to examine the scenario where the competition among advertising agents is taken into consideration. Moreover, it is worth exploring firms’ equilibrium advertising strategies when they are engaged in dynamic competition in service quality.

## Acknowledgments

The authors thank the senior editor, the associate editor, and anonymous reviewers for their insightful comments and suggestions that have greatly improved the quality of this paper.

## Endnotes

<sup>1</sup> The key insights of our study remain the same with other reasonable functional forms for f q and g q .

<sup>2</sup> For example, some search engine advertising agents offer price breaks on certain types of ads in return for a committed level of advertising (Lee and Seda 2009).

## References

Agarwal R (2012) Yelp advertising is a rip-off for small advertisers. Accessed August 14, 2019, https://venturebeat.com/2012/02 06/yelp-advertising-is-a-rip-off-for-small-advertisers/.

Asdemir K, Kumar N, Jacob VS (2012) Pricing models for online advertising: CPM vs. CPC. Inform. Systems Res. 23(3):804–822

Bixby J (2012) 4 Awesome slides showing how page speed correlates to business metrics at walmart.com. Accessed August 14, 2019, http://www.webperformancetoday.com/2012/02/28/4-awesome -slides-showing-how-page-speed-correlates-to-business-metrics-at -walmart-com/.

Case J (1979) Economics and the Competitive Process (New York Uni versity Press, New York).

Deal KR (1979) Optimizing advertising expenditures in a dynamic duopoly. Oper. Res. 27(4):682–692.

Deal KR, Zionts S (1973) A differential games solution to the problem of determining the optimal timing of advertising expenditures. Proc. Second Annual Northeast Regional AIDS Conf., Kingston, RI (American Institute of Decision Sciences, Atlanta)

DeLapp D (2017) How much should website maintenance cost? 2017 Guide. Accessed August 14, 2019, https://maintaingo.com/how -much-should-website-maintenance-cost-2017-guide/.

Dockner E, Jorgensen S, Long NV, Sorger G (2000) Differential Games in Economics and Management Science (Cambridge University Press, Cambridge, UK).

Erickson GM (1985) A model of advertising competition. J. Marketing Res. 22(3):297–304.

Erickson GM (2003) Dynamic Models of Advertising Competition (Kluwer Academic Publishers, Norwell, MA).

Feichtinger G (1983) The Nash solution of an advertising differential game: Generalization of a model by Leitmann and Schmitendorf. IEEE Trans. Automatic Control 28(11):1044–1048.

FTI Consulting (2016) The U.S. online retail forecast: Omni-channel retailing challenged by its success. Accessed August 14, 2019, http://www.fticonsulting.com/\~/media/Files/us-files/insights reports/us-online-retail-forecast-2016.pdf.

Ganguly B, Dash SB, Cyr D, Head MM (2010) The effects of website design on purchase intention in online shopping: The mediat ing role of trust and the moderating role of culture. Internat. J. Electronic Bus. 8(4):302–330.

Hoxmeier JA, DiCesare C (2000) System response time and user satisfaction: An experimental study of browser-based applications. AMCIS 2000 Proc. (Association for Information Systems, Atlanta), 347.

Hu Y (2010) An investigation on the linkage between purchase intention and service quality in the e-commerce context. Proc. 2010 Internat. Conf. Innovative Comput. Comm. 2010 Asia-Pacific Conf. Inform. Tech. Ocean Engrg. (IEEE, Los Alamitos, CA), 304–307.

Hu Y, Shin J, Tang Z (2016) Incentive problems in performance-based online advertising: Cost-per-click vs. cost-per-action. Management Sci. 62(7):2022–2038.

Interactive Advertising Bureau (2016) IAB internet advertising rev enue report: 2015 Full year results. April, accessed August 14, 2019, http://www.iab.com/wp-content/uploads/2016/04/IAB \_Internet\_Advertising\_Revenue\_Report\_FY\_2015-final.pdf.

Kalia P, Arora DR, Kumalo S (2016) E-service quality, consumer satisfaction and future purchase intentions in e-retail. e-Service J. 10(1):24–41.

Kelley LD, Jugenheimer DW (2008) Advertising Media Workbook and Sourcebook (M. E. Sharpe, Inc., Armonk, NY).

Lee K, Seda C (2009) Search Engine Advertising: Buying Your Way to the Top to Increase Sales (New Riders, Berkeley, CA).

Little JDC (1979) Aggregate advertising models: The state of the art. Oper. Res. 27(4):629–667.

Liu D, Kumar S, Mookerjee V (2012) Advertising strategies in electronic retailing: A differential games approach. Inform. System Res. 23(3):903–917.

Moon Y, Kwon C (2011) Online advertisement service pricing and an option contract. Electronic Commerce Res. Appl. 10(1):38–48.

Naik PA, Prasad A, Sethi SP (2008) Building brand awareness in dynamic oligopoly markets. Management Sci. 54(1):129–138.

Padmanabhan V, Png IPL (1997) Manufacturer’s return policies and retail competition. Marketing Sci. 16(1):81–94.

Prasad A, Sethi SP (2004) Competitive advertising under uncertainty: A stochastic differential game approach. J. Optim. Theory Appl. 123(1):163–185.

Pyzdek T, Keller P (2013) The Handbook for Quality Managemen (McGraw-Hill Education, New York).

Sethi SP (1983) Deterministic and stochastic optimization of a dynamic advertising model. Optimal Control Appl. Methods 4(2): 179–184.

Sethi SP, Thompson GL (2000) Optimal Control Theory: Applications to Management Science and Economics (Kluwer Academic Publi shers, Boston).

Sorger G (1989) Competitive dynamic advertising: A modification of the case game. J. Econom. Dynam. Control 13(1):55–80.

U.S. Census Bureau (2017) Quarterly retail e-commerce sales: 4th quarter 2016. Accessed August 14, 2019, http://www.census .gov/retail/mrts/www/data/pdf/ec\_current.pdf.

Vidale ML, Wolfe HB (1957) An operations research study of sales response to advertising. Oper. Res. 5(3):370–381.

Rodman T (2013) ST. PATRICK’S DAY SMACKDOWN: Holding leprechauns’ feet to the fire for website speed and performance. Accessed August 14, 2019, http://www.yottaa.com/st-patrick-s -day-smackdown-holding-leprechauns-feet-to-the/

Zhang C, Pan F (2009) The impact of customer satisfaction on profitability: A study of state-owned enterprises in china. Service Sci. 1(1):21–30.
