---
otero_id: 10856
otero_key: "DUP8PAM9"
title: "A decision support model for optimal timing of investments in information technology upgrades"
authors: "Nivedita Mukherji; Balaji Rajagopalan; Mohan Tanniru"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.02.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support model for optimal timing of investments in information technology upgrades

Nivedita Mukherji <sup>a</sup>, Balaji Rajagopalan <sup>b,⁎</sup>, Mohan Tanniru <sup>c</sup>

<sup>a</sup> Department of Economics, School of Business Administration, Oakland University, Rochester, MI 48309, United States <sup>b</sup> Department of Decision and Information Sciences, School of Business Administration, Oakland University, Rochester, MI 48309, United States <sup>c</sup> Department of Management Information Systems, Eller College of Management, University of Arizona, Tucson, AZ 85721, United States

Received 26 May 2003; received in revised form 16 February 2006; accepted 22 February 2006 Available online 19 April 2006

## Abstract

In an environment of continuous change, organizations are faced with the challenge of deciding when to invest in information technology upgrades. While investing frequently is costly and at times risky, waiting too long can lead to lost competitiveness. Further, investing at a given time can preclude a firm from taking advantage of better technologies in the future. In the context of software upgrades, this study proposes and illustrates a decision support model to determine the optimal timing and choice of upgrades. Analysis confirms that even if continuous upgrading is feasible, it is not an optimal strategy when adoption costs are significant. Simulations show that investments in upgrades are best made when the gap between new technology and current technology reaches a critical threshold. Among other factors, this threshold is influenced by technology cost, change management cost and opportunity cost.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Investment in IT upgrades; Technology adoption costs; Opportunity costs; Dynamic decision support model; Optimal timing of technology adoption

## 1. Introduction

In an environment of continuous technological change, organizations are frequently faced with the challenge of deciding when to invest in new and upgraded information technology (IT). Consider the releases of operating systems (OS) by Microsoft— Windows 95 in August 1995, Windows 98 in June 1998, Windows 98 Second edition in 1999, Windows ME and Windows 2000 in the year 2000 and

Windows XP in 2002. With this continuous stream of upgrade releases, individuals and organizations are faced with the decision to upgrade their OS. Typically, few would upgrade to a new version every time a release is announced; instead they would leapfrog to adopting a subsequent release [40]. Making such technology investments continuously (i.e., every time a new release of a technology is announced) can be very expensive.

While investing frequently is costly and at times risky, waiting too long can put an organization at the risk of losing first mover advantages associated with introducing competitive products and services. However, by waiting, the firm can purchase a superior technology than the one available now. Clearly, in this context, it is critical for a firm to determine whether it should incur the adoption costs now to take advantage of the productivity and competitiveness gains that the currently available new or upgraded technology provides or wait for a better technology. This study examines how a firm can determine this optimal interval between adoptions and thereby its optimal choice of technology.

The primary focus is on the case of software upgrade decisions. Cases of acquiring a technology for the first time are not considered. Unlike new technology adoption, in the case of upgrade the question is more of “when” to adopt than “whether” to adopt. Furthermore, in contrast to new technologies, the uncertainties associated with benefits and costs are relatively small in the case of upgrades. First time investments in new technologies have received a lot of attention in the literature and models like net present value and options based evaluation have been developed for decision support. On the other hand, few studies have focused on upgrade situations.

The choice of upgrade situations is motivated by several reasons. First, periodic upgrade investments are increasingly becoming a significant percentage of total IT budgets and hence, an area of utmost interest to researchers and technology managers. Second, organizations seem to time the upgrades rather arbitrarily without a systematic analysis. Third, even in the case of upgrades, where reasonably accurate predictions about technological change can be made, it is not clear how different costs involved with technology adoption affect the intervals (timing) at which adoption decisions are made. Finally, despite the importance of the topic it has remained largely unexplored. To this end, the objective of this research is twofold:

(1) To develop a decision support model to determine the optimal time and choice of upgrade investment, and

(2) To study the impact of various costs on the optimal upgrade time and upgrade choice.

It is worth noting that based on the type of technology under consideration, there can be substantial differences in factors that drive adoption decisions. For example, the primary driving force behind an upgrade decision might be lack of vendor support for one firm but compatibility with competitors' or users' software might be the critical factor for another. Clearly, these are opportunity costs associated with not adopting the upgrade and can be incorporated as such in decision support models.

A decision support model must include a consideration of the dynamic context to take full account of the impact of current upgrade decisions on future ones. In a competitive landscape, technological improvements occur rapidly and investing at a given time may preclude a firm from taking advantage of better technologies at a later date. Thus, adoption decisions must consider the future impact of current decisions.

Interestingly, widely applied investment evaluation methods in information systems (IS) research like net present value (NPV) do not take into account the dynamics discussed above as these methods do not consider the impact on future decisions. In the case of continuous upgrades, it is important for firms to decide the frequency at which its technology must be replaced. Thus, unlike other types of investment decisions, firms would benefit from a long term “plan” for investment in IT upgrades. Conducting disjoint static analysis ignores the element of inter-temporal interdependence of the investments—a critical consideration for technology upgrades.

To address the interdependent nature of the decisions, this study draws upon models that have specifically addressed this issue (for e.g., see [2,3,11]). [3] developed a model that examined the problem of technology adoption that allows the state of nature to change at a stochastic rate. They apply an impulsecontrol method to determine the intervals at which decisions are made. This framework is most suitable for this study since it has been developed to solve exactly the type of dynamic problem IT decision-makers face. That is, the framework allows us to examine how a firm should optimally spread its investment over time in an environment of continuous change.

Other dynamic models have been used to study technology adoption decisions. The applicability of alternative dynamic models, such as, options-pricing and the proposed model are, however, quite different. The main motivation for using options pricing in articles such as [4] is that the benefits from investment in the technology are uncertain. By using real options, a firm delays adoption to gather valuable information regarding the investment. The question addressed in this study is quite different. This study's model is applicable when uncertainties regarding benefits or costs are not the key factors. The main concern is that firms understand that adopting something new today implies that very soon an even better technology will become available. Should it wait for that better technology or adopt now? Should it adopt every time a new or upgraded technology is released? How do the different costs involved with adoption affect the adoption decision? These questions cannot be answered by options pricing type models. In fact, the impulse control model was developed to address exactly these questions.

## 2. Literature Review

A critical issue in any IT investment evaluation, particularly true in the case of upgrades, is the timing of adoption. The investment decision, in upgrade situations, is usually less focused on the question of “whether” to acquire a technology or not but more on “when” to acquire it. Several studies in economics have examined the timing of adoption of new technologies. Some of the seminal studies include [20,21,32–34]. These studies highlight the role of competition between firms in the technology adoption and timing of adoption decisions. More competitive industries seem to adopt new technologies faster than others. A more recent study by [14] showed the importance of product market competition in the adoption decision of new technologies in the context of the airline industry.

Another issue of importance in adoption timing is the uncertainty associated with new technologies. The uncertainty may take various forms, ranging from uncertain benefits of new technologies to uncertainties regarding how soon it will become obsolete. Increased uncertainty often delays adoption. When firms have limited knowledge about the various features of a new technology or its ability to enhance productivity, by delaying adoption, a firm may be able to gain additional information. In this context [16,28,29,35,38] study the role of uncertainty in returns and costs in adoption decisions. While these articles did not study uncertainty in IT investments, others such as [9,12,19,26] did. They recognized that investments in IT have “option-like” characteristics. Building on this, [4] demonstrated the use of option pricing models, such as Black–Scholes, to study the timing of deployment of a particular service by a banking network. By delaying adoption, the firm gathers valuable information to reduce uncertainty.

In addition to gathering information regarding an uncertain investment, by delaying adoption, a firm may be able to either purchase an existing technology at a much lower price (particularly true in the case of hardware upgrades) or purchase a better technology. [7] studied the equipment replacement decision problem when successively improved machines become available over time with certainty. [31] proposes a dynamic programming approach to study the upgrade problem in the presence of technological uncertainty. [1,10,17,30] are examples of studies that illustrate using machine replacement decisions of single or multiple machines both in deterministic and stochastic models. It is important to note that in the case of upgrade situations there is relatively low uncertainty regarding the benefits as the firm already has experience with other versions of the technology.

In cases of both new investments and upgrades, the decision of whether to stay with the current technology or leapfrog is influenced, among other factors, by the competitiveness of the market in which the firm operates. Two complementary perspectives emerge from research examining the decision of a firm to invest in new technologies in the context of actions of other similar firms. One view is that of product market competition that shows increased competition reduces the time to adoption. The second view, based on research on network externalities, examines cooperation between firms in technology adoption. [13,22–24,37,8] highlighted the role of network externalities in adoption decisions. [25] provide empirical support for the network externality effect and [27] used network externality and switching costs (barrier) to explain why in certain industries firms may be reluctant to adopt a new and superior technology.

In sum, the literature on technology adoption decisions examines the role of factors such as competition, uncertainty, network externality, and price changes on adoption decisions by firms. However, sufficient attention has not been devoted to examine the impact of various costs on adoption timing of information technology upgrades.

## 3. Model description

This study considers the technology upgrade decision of a single firm. New upgrades appear at a steady, deterministic pace. For example, every year, output can be increased by 100,000 units by implementing upgrades to the technology in use. In such an environment of continuous improvement, unless a firm adopts new upgrades immediately upon release, the gap between the technology in use and the most advanced available increases continuously. The firm has three alternatives: (i) adopt new upgrades as they become available, (ii) wait and adopt at a later time, or (iii) never adopt upgrades. Generally, firms neither upgrade continuously nor do they completely refrain from doing so since the direct or opportunity cases become prohibitive. Thus, the first and third cases are rather unrealistic. Also in these two extreme cases, there is no need for a model to make upgrade decisions. Thus, the study's focus is primarily on the more interesting “wait and adopt later” case.

In addition to significant costs, adoption at the rate of release of new upgrades may not be optimal if the most recent release is not well suited for the firm. For example, new upgrades typically introduce new functionalities. These may not be productive for a firm if its other supporting software and hardware do not allow it to make use of these new features. It is also possible that even if the firm itself may gain by upgrading, the output format may be incompatible with other user applications. Thus, for a variety of reasons, the latest release may not be the most suitable level at which a firm would prefer to operate. However, assuming that all technologies change at a continuous rate, these incompatibility issues are likely to be transitory in nature. As new hardware and software become available, an upgrade that had compatibility problems earlier may become the preferred choice. If the firm does not upgrade, it would begin to incur costs related to forgone productivity gains and lost competitiveness.

The most suitable upgrade is defined to be the one which has the optimal combination of functionalities given other supporting software and hardware capabilities and the needs of the firm's customers. That is, it is possible that a firm by adopting a new technology produces a product that is incompatible with the technologies used by its customers. In that case even if the internal needs of the firm make adoption of the new technology optimal, the external demands may not. Thus, the most suitable technology is the one that has the optimal combination of functionalities given all the internal support and external needs. Further, it is assumed that due to releases of new upgrades and changes in supporting hardware, software, and user technologies, the gap between a firm's existing technology and the most suitable one for it widens over time if the firm does not adopt new upgrades. This gap is measured in terms of the productivity of the two technology levels. To illustrate, suppose the current technology allows a user to complete 250 operations per unit of time and the upgrade increases that to 350, then by staying with the older version, a firm gives up the opportunity to increase productivity of each user by 100 units per period. Assuming that both time and productivity are continuous variables and defining the difference between the technology used at any given time t and the most suitable available at that time t by x(t), it is assumed that

$$
\frac {\mathrm{d} x (t)}{\mathrm{d} t} = - g.\tag{1}
$$

Eq. (1) shows that by not increasing its technology level to the most suitable level, the firm incurs a productivity loss at a rate of $\cdot _ { g }$ per unit time. g gives the change in the productivity gap per unit of time. It is noted that, if the firm is using a version that is older than the most suitable technology available, $x ( t ) < 0 .$ . Conversely, if the firm uses a version that is higher than what is most suitable at that time, $x ( t ) { > } 0$ . This is likely to be the case when a firm adopts a new upgrade that it cannot take full advantage of given hardware and software constraints or its needs.

As discussed earlier, although changes in productivity may occur at a steady rate, the firm may not upgrade to the most suitable level at the rate at which that level is changing. Due to cost considerations, it may prefer to upgrade after a minimum amount of time elapses after the last upgrade. Thus, the firm is assumed to upgrade its technology only at discrete intervals denoted by $t _ { i } , i \geq 1$ To determine these intervals, the various costs associated with the decision must be considered.

## 3.1. Costs of adoption and the optimization problem

The costs of adoption have two components: (i) the cost of purchasing the upgrade for all the necessary machines and (ii) the costs associated with installing, training, and transitioning people completely to the new technology. The cost of purchasing an upgraded version of the technology is assumed to be K. This is the total cost for the organization to purchase the upgrade. Thus, for a given size of the organization or number of machines that need to be upgraded, this value is assumed to be constant for all upgrades. Although in reality this may vary for different versions and in some cases may even decrease over time, a fixed value of K is assumed to keep the analysis more tractable.

In addition to this fixed cost, the firm is expected to incur change-management costs. These costs relate to the deployment of the upgrades, the training and learning costs associated with adoption, and any additional hardware and/or software purchases necessary to make full use of the new technology. Since retraining of workers takes time, it is assumed changemanagement cost is incurred over a span of some $n { > } 1$ periods, with the cost decreasing over time. In addition, the cost depends on how large the change is from the current to the new version and the ease with which the workers learn the new version. This captures the idea that when an upgrade is adopted and workers learn to use it, training adds to the current cost of adjustment. However, the knowledge and experience gained helps reduce the cost of future adoptions. Similarly, large changes require more training and adjustment than small changes. Training adds to individual's knowledge and reduces the amount of future training.

If an upgrade occurs at time $t _ { i } ,$ the changemanagement cost is incurred over the following n consecutive discrete intervals. Denoting the cost per interval by $c _ { j } ,$ where, $j = 1 , 2 , . . . n$ and assuming that the cost decreases over time, $0 { < } c _ { j } { < } c _ { j - 1 } , \forall j { \leq } n$ and $c _ { j } = 0$ $\forall j > n ,$ <sup>-</sup>the change-management cost is represented by:

$$
\sum_ {j = 1} ^ {n} c _ {j} u _ {i} \mathrm{e} ^ {- A u _ {i - 1} j}\tag{2}
$$

This expression shows that the cost is distributed over n periods, progressively decreasing over time. Further, the cost is higher if the current change to the upgrade is higher. However, as discussed above, larger changes make future change less costly. This is captured by discounting the current cost by the size of the previous change, $u _ { i - 1 }$ . The cost also shows that it decreases with <sup>-</sup>the interval $j . ~ A$ is a constant.

Summing the purchase cost of new technology and change-management cost, total cost of adoption is given by:

$$
K + \sum_ {j = 1} ^ {n} c _ {j} u _ {i} \mathrm{e} ^ {- A u _ {i - 1} j}\tag{3}
$$

If a firm chooses not to adopt the new technology, this cost is zero. However, in that case it must consider the opportunity cost of not using the most suitable upgrade. This lost opportunity may be in the form of lost revenue if the firm's competitors are using more advanced technology, or it may be in terms of lost opportunity to increase productivity. It may also mean the cost of continuing with a technology that is unsupported by the vendor, in case a firm decides to continue using a technology beyond the time for which vendor support is available. If a firm chooses to adopt a technology more advanced than the most suitable for its purpose, it may lose revenue due to factors such as incompatibility with other firms it interacts with, incompatibility with other hardware and software it uses and so on. If p and r are the per unit of productivity costs of not using the most suitable technology, the cost of $x \neq 0$ is given by:

$$
I (x (t)) = \left\{ \begin{array}{l} - p x (t), x (t) <   0 \\ r x (t), x (t) > 0 \end{array} \right.\tag{4}
$$

Thus, if the cost of lost competitiveness equals \$1.5 per operation between the current and most suitable technology levels and the most suitable technology can increase productivity by 100,000 operations, then by not adopting that technology the firms loses \$150,000. The interpretation of r parallels the interpretation of p.

In case a firm adopts no upgrades, its gap with the most suitable technology level will rise continuously and so will the cost $I ( x )$ . Over the infinite horizon, the firm continuously incurs the opportunity cost given by I $( x ( t ) )$ but incurs the adoption cost discussed above only at discrete intervals given by $t _ { i } ^ { \phantom { \dagger } } \mathbf { s } .$ . The firm's objective is to minimize the sum of this opportunity cost and the adoption cost by appropriately choosing the upgrade times, $t _ { i } { } ^ { \ ' } \mathbf { S }$ and selecting the levels of upgrades, $u _ { i } .$ . Using α as the discount factor, the firm's value function is represented as:

$$
\begin{array}{l} V (x) = \min _ {\left\{u _ {i}, t _ {i} \right\}} \left[ \int_ {0} ^ {\infty} I (x (t)) \mathrm{e} ^ {\alpha t} \mathrm{d} t \right. \\ \quad + \sum_ {i > 1} \left[ K + \sum_ {j = 1} ^ {n} c _ {j} u _ {i} \mathrm{e} ^ {A u _ {i - 1} j} \right] \mathrm{e} ^ {- \alpha t _ {i}} \end{array}\tag{5}
$$

subject to Eq. (1):

$$
\frac {\mathrm{d} x (t)}{\mathrm{d} t} = - g
$$

The solution to this optimization problem is discussed next.

## 3.2. Trigger-target solution

At any time t, the firm has two options: it can upgrade or postpone adoption to a later period: $t { + } t ^ { \prime } .$ . If it chooses to postpone till time $t { + } t ^ { \prime }$ (leapfrog) then the value function $V ( x )$ is bounded above by the cost of postponement:

$$
V (x) \leq \int_ {t} ^ {t + t ^ {\prime}} I (x (s)) \mathrm{e} ^ {- \alpha (s - t)} \mathrm{d} s + V (x (t + t ^ {\prime})) \mathrm{e} ^ {- \alpha t ^ {\prime}}\tag{6}
$$

If the firm chooses to adopt, the value function is bounded above by the cost of adoption:

$$
V (x) \leq \min _ {u} \left[ K + \sum_ {j = 1} ^ {n} c _ {j} u \mathrm{e} ^ {- A u j} + V (x + u) \right]\tag{7}
$$

Since $V ( x )$ is the optimal solution, one of the above inequalities will be satisfied with an equality.

Research has shown that solutions to problems of this nature follow a simple trigger-target rule. Existence of such solutions was proven by [11] and other examples of such problems can be found in [2,3,39] among others.

The trigger-target type of solution has the characteristic that no changes are made by the firm to its technology level until the difference between the technology in use and the most suitable level is less than a certain value, called the trigger. Once the difference hits the trigger value, τ, the firm purchases new technologies and brings the difference to some target value, T. Thus, the change u becomes $T - \tau .$

<sup>-</sup>Applying this rule, as long as the gap x is less than the trigger τ, no action is taken and Eq. (6) is satisfied with an equality. Once the gap equals the trigger $\tau ,$ the firm purchases an upgrade and increases the gap to T. In this case, Eq. (7) is satisfied with an equality. Finding the solutions to Eqs. (6) and (7) in these two cases yields the following solutions for τ and $T : ^ { 1 }$

$$
- (r T + p \tau) = K \alpha + \alpha (T - \tau) \sum_ {j = 1} ^ {n} c _ {j} \mathrm{e} ^ {- A j (T - \tau)}\tag{8}
$$

$$
\begin{array}{l} r + p = r \mathrm{e} ^ {\alpha T / g} + p \mathrm{e} ^ {\alpha \tau / g} - \alpha \sum_ {j = 1} ^ {n} c _ {j} \mathrm{e} ^ {- A j (T - \tau)} \\ \times [ A j (T - \tau) - 1 ] [ \mathrm{e} ^ {\alpha T / g} - \mathrm{e} ^ {\alpha \tau / g} ] \end{array}\tag{9}
$$

Since closed form solutions cannot be obtained, numerical simulations are conducted in the following section to gain insights into the solutions for the trigger and target.<sup>2</sup>

## 4. Numerical analysis and discussion

## 4.1. Overview of simulations

Simulations were conducted to arrive at numerical solutions and for analyzing the sensitivities of the results to changes in technology cost, change-management cost, and opportunity cost.<sup>3</sup> The choice of range of values for the parameters was based on typical upgrade scenarios examined, one of which is presented here.

Operating system upgrade data from Microsoft was used to create the scenarios.<sup>4</sup> Parameter values were chosen to encompass a range of values for operating system upgrade to Windows XP from a variety of environments including Windows 95, 98, and 2000 for 1000 personal computers.

In the Microsoft case, for example, the sum of IT benefits and business benefits represent opportunity costs $( p \cdot x )$ ; engineering, deployment, training and maintenance costs represent change management costs and direct investment in the technology is the cost of acquiring it (K). A productivity growth (g) of \$40,000 per year is used by averaging the benefits of a sequence of releases of the operating system. The discount rate (α) is fixed at 10% and r at 10 for all numerical analyses conducted. While the model description section of the article gives a general form in which change-management cost varies over the transition period, that is, $\textstyle \sum _ { j = 1 } ^ { n } c _ { j } u _ { i } \mathbf { e } ^ { - A u _ { i - 1 } j }$ with $0 { < } c _ { j } { < } c _ { j - 1 } , \forall j { \leq } n ,$ , where n denotes <sup>¼ -</sup>the number of periods over which the transition occurs, for the purpose of numerically analyzing the solutions of the model, it is necessary to specify how $c _ { j }$ changes as j changes. It is assumed that the change-management cost equals $\sum _ { j = 1 } ^ { 9 } \frac { 0 . 1 ^ { \mathrm { c } } } { j } u _ { i } \mathrm { e } ^ { - 0 . 0 0 0 0 1 u _ { i - 1 } j } .$ . For the simulations, c varies from $0 . 5 \mathrm { { ^ { J } _ { t o } } }$ 24 and p varies from 1 to 200.

Table 1 shows the results of simulation runs for variations in upgrade investment. Results from the proposed model support the proposition that an increase in technology costs will result in a larger adjustment. This larger adjustment or size of leapfrogging means the firm has to wait longer as a result of a decrease in the trigger τ and an increase in target (T) values.

## 2.1.1. Technology cost (K)

For example, as K changes from \$70,000 to \$2.99 million, the optimal time to upgrade increases from 2.26 years to 13.4 years. (The table presents only the time to upgrade $\overline { { \left( \frac { T - \tau } { g } \right) } }$ for clarity of exposition.) Although this means firms should wait six times longer, the increase in cost that brought about this change is almost 40-fold. Fig. 1a and b are used to get some insights into how optimal adoption time responds to changes in costs.

Fig. 1a plots the ratio of the percentage change in time to the percentage change in $K ,$ or the elasticity of time with respect to changes in K, against K. This graph shows that this ratio varies within a small range 0.4 to 0.55. That is, for every 1% increase in K, optimal time increases by 0.4% to 0.55% only, or, the percentage change in time is about half the percentage change in cost. In other words, time is inelastic to changes in K.

An alternative way of looking at the changes is to examine the impact on time as the proportion of K in total cost changes. Fig. 1b plots the ratio of the percentage change in time to the percentage change in the share of K in total upgrade-related costs (or the elasticity of time with respect to K's share in total upgrade costs) against the share of K in total cost. Observe from Table 1 that when K equals \$70,000 it is about 25% of the total cost and the percentage change in time equals 0.93% for a 1% increase in K's share in total cost. However, as K takes the majority of the upgrade related cost, for example 85% at \$2.99 million, time changes by 3.9% for a 1% increase in K's share in total cost.

Table 1  
Simulation results for impact of technology cost

<table><tr><td>Technology cost (K)</td><td>Optimal time to upgrade (OTU)</td><td>Percent change in optimal time to upgrade (PCOTU)</td><td>Elasticity of time w.r.t. K: PCOTU/(percent change in K)</td><td>K/total  $cost^a$ (PK)</td><td>Percent change in PK (PC-PK)</td><td>Elasticity of time w.r.t. K/total cost: PCOTU/PC-PK</td></tr><tr><td>50,000</td><td>1.941</td><td>0.000</td><td>Indeterminate</td><td>0.217</td><td>0.000</td><td>Indeterminate</td></tr><tr><td>70,000</td><td>2.262</td><td>16.544</td><td>0.414</td><td>0.255</td><td>17.725</td><td>0.933</td></tr><tr><td>90,000</td><td>2.535</td><td>12.098</td><td>0.423</td><td>0.287</td><td>12.563</td><td>0.963</td></tr><tr><td>110,000</td><td>2.777</td><td>9.547</td><td>0.430</td><td>0.315</td><td>9.627</td><td>0.992</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>510,000</td><td>5.623</td><td>1.896</td><td>0.465</td><td>0.571</td><td>1.276</td><td>1.485</td></tr><tr><td>530,000</td><td>5.725</td><td>1.826</td><td>0.466</td><td>0.578</td><td>1.211</td><td>1.508</td></tr><tr><td>550,000</td><td>5.826</td><td>1.760</td><td>0.466</td><td>0.585</td><td>1.150</td><td>1.530</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>1,010,000</td><td>7.796</td><td>0.981</td><td>0.485</td><td>0.691</td><td>0.485</td><td>2.024</td></tr><tr><td>1,030,000</td><td>7.871</td><td>0.963</td><td>0.486</td><td>0.694</td><td>0.471</td><td>2.045</td></tr><tr><td>1,050,000</td><td>7.946</td><td>0.945</td><td>0.487</td><td>0.697</td><td>0.458</td><td>2.066</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>1,510,000</td><td>9.516</td><td>0.674</td><td>0.502</td><td>0.755</td><td>0.266</td><td>2.533</td></tr><tr><td>1,530,000</td><td>9.580</td><td>0.666</td><td>0.502</td><td>0.757</td><td>0.261</td><td>2.553</td></tr><tr><td>1,550,000</td><td>9.643</td><td>0.658</td><td>0.503</td><td>0.759</td><td>0.256</td><td>2.573</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>2,030,000</td><td>11.069</td><td>0.514</td><td>0.516</td><td>0.797</td><td>0.169</td><td>3.048</td></tr><tr><td>2,050,000</td><td>11.125</td><td>0.509</td><td>0.517</td><td>0.798</td><td>0.166</td><td>3.067</td></tr><tr><td>2,070,000</td><td>11.181</td><td>0.505</td><td>0.517</td><td>0.799</td><td>0.164</td><td>3.087</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>2,510,000</td><td>12.370</td><td>0.424</td><td>0.528</td><td>0.824</td><td>0.121</td><td>3.516</td></tr><tr><td>2,530,000</td><td>12.422</td><td>0.421</td><td>0.529</td><td>0.825</td><td>0.119</td><td>3.535</td></tr><tr><td>2,550,000</td><td>12.474</td><td>0.418</td><td>0.529</td><td>0.826</td><td>0.118</td><td>3.554</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>2,970,000</td><td>13.535</td><td>0.365</td><td>0.539</td><td>0.844</td><td>0.092</td><td>3.960</td></tr><tr><td>2,990,000</td><td>13.583</td><td>0.3631</td><td>0.539</td><td>0.845</td><td>0.091</td><td>3.979</td></tr></table>

<sup>a</sup> Total cost = technology cost + change management cost.

It is also worth noting that Fig. 1b shows that the percentage change in time as a ratio of the percentage change in K's share of total cost is increasing at an increasing rate while the graph of the percentage change in time as ratio of the percentage change is K increases at a decreasing rate. Thus, even though the percentage change in time as a fraction of the percentage change in K does not change much as K changes, the percentage change in time is not only generally greater than the percentage change in K's share in total cost, the ratio increases at an increasing rate as K's share in total cost rises. To understand the impact of a change in K on time, it is then more instructive to examine how it changes with respect to the total upgrade cost. It is important to note that two firms incurring identical technology costs (K) and the same percentage changes in K would have different impacts on the optimal time to upgrade if the share of K in the total budget is not the same.

These results suggesting that organizations should wait longer as K increases are consistent with the [5] study that found lower upgrade investment costs led organizations to adopt early. This is also echoed by Til Lassance, Vice President of information systems at Heartland Financial USA Inc., as he points out that with an annual IT budget of about \$250,000 they could end up spending all of it on just the upgrades to Windows 2000 [36]. For the scenario described just the technology costs of upgrading is in the order of \$189,000. Indeed, for reasons of high costs of technology, companies like Heartland will in all likelihood delay the deployment of the upgrade.

If the cost of technology is very high (relative to the size of IT budget), the adoption time in some cases may be long enough to be beyond the foreseeable future and hence, the decision could be almost equivalent to not adopting. The DEC alpha processor is an example of such a scenario. When the promising alpha processor was put forth by DEC, few computer manufacturers were willing to invest in the retooling of the manufacturing facility at a cost of \$50 million as most of these facilities had installed bases for Intel and Motorola chips [18].

![](/api/attachments/DUP8PAM9/fulltext/images/9e6eb8c172e0a995f9908bd3c270fd359a7a03f7deef08293e0f4ae2d4817c38.jpg)

![](/api/attachments/DUP8PAM9/fulltext/images/60c84d780c23d9a000f228d4293a5f0112d5dc77b320bdfb814aa31828437c34.jpg)  
Fig. 1. Impact of cost technology (K) on optimal time to upgrade.

## 4.1.2. Change management costs

Table 2 shows the results of the simulation runs for various values of the change management costs. As the change management cost varies from about \$14,379 to \$942,000, the resulting adjustment is a change in the optimal time to adoption from 3.6 to 6.12years. It is clear that higher change management costs result in a longer wait to upgrade. This is consistent with [6] finding that high change management costs (specifically, training cost) can be a disincentive to switch or upgrade.

Fig. 2a shows that for every 1% increase in changemanagement cost, the percentage change in time varies from 0.01 to 0.43, with the percentage change in time increasing at a decreasing rate. Thus, like the change in K, time is inelastic to changes in change-management cost. Unlike K, however, the change occurs over a wider range: 0.01 to 0.4 compared to $K \mathbf { \vec { s } } \ 0 . 4$ to 0.55.

Plotting the elasticity to time with respect to change-management cost's share in total cost, or ratio of the percentage change in time to percentage change in share of change-management cost in total cost, Fig. 2b shows that when change-management cost is only about 9% of the total upgrade cost, a 1% increase in it causes an insignificant 0.01% increase in time. When the ratio rises to about 25% of the total cost, time increases by 0.08% in contrast to $K \mathrm { ~ s ~ } 0 . 9 3 \%$ for the same 1% increase in cost. However, at a higher share such as above 70%, time is elastic to changes in change-management cost's share in total cost. Comparing Tables 1 and 2, it can be concluded that overall, adoption time responds less to changes in change-management cost than it does to the direct investment cost.

## 4.1.3. Opportunity costs

Results shown in Table 3 clearly show that if an organization has a high opportunity cost associated with an upgrade it is of benefit to conduct the upgrade sooner. As reflected in the results, a change in the opportunity cost from about \$238,000 to \$443,600 causes a change in the optimal time to upgrade from 4.4 to 1.5years. This is strongly echoed by Nordstrom.com's Ornen's comment “Forget cost; think opportunity” with regards to the upgrade investment in Windows 2000 [15]. He further adds that the total cost of ownership may not hold as much weight as it did in the past as compared to the opportunity.

Table 2  
Simulation results for impact of change management cost

<table><tr><td>Change management cost (CMC)</td><td>Optimal time to upgrade (OTU)</td><td>Percent change in optimal time to upgrade (PCOTU)</td><td>Elasticity of time w.r.t. CMC: PCOTU/(percent change in CMC)</td><td>CMC/total cost (PCMC)</td><td>Percent change in CMC (PC-PCMC)</td><td>Elasticity of time w.r.t. CMC/total cost: PCOTU/PC-PCMC</td></tr><tr><td>14,379</td><td>3.578</td><td>0.000</td><td>Indeterminate</td><td>0.046</td><td>0.000</td><td>Indeterminate</td></tr><tr><td>28,955</td><td>3.613</td><td>0.996</td><td>0.010</td><td>0.088</td><td>92.450</td><td>0.011</td></tr><tr><td>43,733</td><td>3.650</td><td>1.006</td><td>0.020</td><td>0.127</td><td>44.543</td><td>0.023</td></tr><tr><td>58,716</td><td>3.687</td><td>1.016</td><td>0.030</td><td>0.164</td><td>28.653</td><td>0.035</td></tr><tr><td>73,909</td><td>3.725</td><td>1.027</td><td>0.040</td><td>0.198</td><td>20.760</td><td>0.049</td></tr><tr><td>89,315</td><td>3.763</td><td>1.037</td><td>0.050</td><td>0.229</td><td>16.063</td><td>0.065</td></tr><tr><td>104,939</td><td>3.803</td><td>1.047</td><td>0.060</td><td>0.259</td><td>12.960</td><td>0.081</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>256,004</td><td>4.195</td><td>1.136</td><td>0.152</td><td>0.460</td><td>4.022</td><td>0.282</td></tr><tr><td>274,020</td><td>4.243</td><td>1.145</td><td>0.163</td><td>0.477</td><td>3.678</td><td>0.311</td></tr><tr><td>292,295</td><td>4.292</td><td>1.154</td><td>0.173</td><td>0.493</td><td>3.378</td><td>0.342</td></tr><tr><td>310,833</td><td>4.342</td><td>1.162</td><td>0.183</td><td>0.509</td><td>3.115</td><td>0.373</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>511,207</td><td>4.894</td><td>1.233</td><td>0.284</td><td>0.630</td><td>1.607</td><td>0.767</td></tr><tr><td>532,784</td><td>4.955</td><td>1.238</td><td>0.293</td><td>0.640</td><td>1.520</td><td>0.814</td></tr><tr><td>554,645</td><td>5.016</td><td>1.242</td><td>0.303</td><td>0.649</td><td>1.440</td><td>0.863</td></tr><tr><td>576,790</td><td>5.079</td><td>1.247</td><td>0.312</td><td>0.658</td><td>1.366</td><td>0.913</td></tr><tr><td>599,219</td><td>5.142</td><td>1.250</td><td>0.322</td><td>0.666</td><td>1.297</td><td>0.964</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>813,641</td><td>5.755</td><td>1.262</td><td>0.399</td><td>0.731</td><td>0.851</td><td>1.482</td></tr><tr><td>838,823</td><td>5.828</td><td>1.260</td><td>0.407</td><td>0.737</td><td>0.815</td><td>1.546</td></tr><tr><td>864,266</td><td>5.901</td><td>1.259</td><td>0.415</td><td>0.742</td><td>0.782</td><td>1.611</td></tr><tr><td>889,965</td><td>5.975</td><td>1.257</td><td>0.423</td><td>0.748</td><td>0.750</td><td>1.676</td></tr><tr><td>915,917</td><td>6.050</td><td>1.254</td><td>0.430</td><td>0.753</td><td>0.719</td><td>1.743</td></tr><tr><td>942,118</td><td>6.126</td><td>1.251</td><td>0.437</td><td>0.758</td><td>0.691</td><td>1.811</td></tr></table>

Fig. 3a shows that a 1% increase in opportunity cost decreases optimal time by more than 1% throughout the range of costs considered. This is in contrast to the investment and change-management costs for which time was inelastic to changes in both. Thus, it might suggest that opportunity cost may exert more influence on time to adopt than the other two direct upgrade-related costs. However, as one looks at Fig. 3b, the percentage change in time as a fraction of the percentage change in opportunity cost as a share of upgrade cost, the sensitivity of time declines quite sharply. When opportunity cost is about 40% of the total upgrade related cost, a 1% increase in it drops adoption time by 1.15%, but when that ratio rises to about 99%, the percentage change in time drops to 0.86% for a 1% increase in opportunity cost's share. This is partly because the percentage change in upgrade cost for a 1% change in opportunity cost declines from 0.84 to 0.36.

## 5. Conclusions and areas for future research

The phenomenal rate at which new technology is available and the competitive business environment are putting increasing pressure on firms to make difficult upgrade decisions. Theoretically, upgrading technology every time a new version is released should keep firms at the cutting edge constantly. Practically, in an environment of continuous technological change, this is fraugh with difficulties of managing change. Analysis suggests that even if continuous upgrading is feasible, it is not an optimal strategy if the adoption costs are significant. Specifically, this study's findings support the idea that investments in upgrades are best made when the gap between the new technology and the one currently in use reaches a “critical” threshold. Among other factors, this threshold is influenced by technology cost, change management cost and opportunity cost.

One of the important implications of this study for practicing managers is that if organizations can set up a long-term plan to leapfrog (optimal/near optimal) it will result in better management of their resources and

b

Table 3  
a  
![](/api/attachments/DUP8PAM9/fulltext/images/92598e0177fea26a7708c37a42d8e86ea7536985dda701fae5415658aff4aaf6.jpg)

![](/api/attachments/DUP8PAM9/fulltext/images/1ae2837a8bc896e1068ef976d0eaeb77137f004789d3082c029d8a3158f4412f.jpg)  
Fig. 2. Impact of change management cost on optimal time to upgrade.

substantial cost savings. From a vendor's perspective— an understanding of the patterns of leapfrogging can help them time the release of new products and services to increase sales.

Like every research project, some of the assumptions made limit the generalizability of the results to all upgrade scenarios. In studying the impact of different costs, the model does not account for any uncertainty associated with new technologies (growth rate is assumed to be known and constant). In general, this is not a major concern as long as it is applied to upgrade situations with relatively low uncertainty. Also, it does not allow for prices of the same technology to fall over time. However, a quick look at the historical price information of software products indicates that there is little variation in price of upgrades even after the release of a newer version. Hardware costs on the other hand are more likely to go down and hence, the model in the current form is more suitable for software upgrades than hardware.

Simulation results for impact of opportunity cost

<table><tr><td>Opportunity cost (OC)</td><td>Optimal time to upgrade (OUT)</td><td>Percent change in optimal time to upgrade (PCOTU)</td><td>Elasticity of time w.r.t. OC: PCOTU/(percent change in OC)</td><td>OC/total cost (POC)</td><td>Percent change in OC (PC-POC)</td><td>Elasticity of time w.r.t. OC/total cost: PCOTU/PC-POC</td></tr><tr><td>215,822</td><td>5.76</td><td>0.00</td><td>Indeterminate</td><td>0.31</td><td>0.00</td><td>Indeterminate</td></tr><tr><td>237,793</td><td>4.37</td><td>-24.10</td><td>-2.37</td><td>0.38</td><td>20.52</td><td>-1.17</td></tr><tr><td>264,976</td><td>3.41</td><td>-21.97</td><td>-1.92</td><td>0.46</td><td>21.15</td><td>-1.04</td></tr><tr><td>297,261</td><td>2.74</td><td>-19.67</td><td>-1.61</td><td>0.55</td><td>20.75</td><td>-0.95</td></tr><tr><td>333,481</td><td>2.27</td><td>-17.33</td><td>-1.42</td><td>0.66</td><td>19.39</td><td>-0.89</td></tr><tr><td>371,626</td><td>1.93</td><td>-14.96</td><td>-1.31</td><td>0.77</td><td>17.25</td><td>-0.87</td></tr><tr><td>409,172</td><td>1.69</td><td>-12.55</td><td>-1.24</td><td>0.89</td><td>14.62</td><td>-0.86</td></tr><tr><td>443,604</td><td>1.51</td><td>-10.17</td><td>-1.21</td><td>0.99</td><td>11.80</td><td>-0.86</td></tr><tr><td>472,958</td><td>1.39</td><td>-7.90</td><td>-1.19</td><td>1.08</td><td>9.06</td><td>-0.87</td></tr><tr><td>496,119</td><td>1.31</td><td>-5.83</td><td>-1.19</td><td>1.15</td><td>6.59</td><td>-0.88</td></tr><tr><td>512,742</td><td>1.26</td><td>-4.00</td><td>-1.19</td><td>1.21</td><td>4.46</td><td>-0.90</td></tr></table>

a  
![](/api/attachments/DUP8PAM9/fulltext/images/646660d54708f866ce351b7b6a2a5b98d158177ad77d939c4d41b317e78b863e.jpg)

b  
![](/api/attachments/DUP8PAM9/fulltext/images/c64587551469df6eff05bcc0be916156a4538f0a8875c8845c70ea305dbd624b.jpg)  
Fig. 3. Impact of opportunity cost on optimal time to upgrade.

Furthermore, upgrade decisions are sometimes driven by some external factors like lack of vendor support of old technologies, application or platform upgrades made by clients. Although the study does not deal with such factors explicitly, in most cases these affect one of the costs discussed in the article. Consider, for example, the case of vendor driven upgrades that include SAP and EDI, among others. In the context of this model, this becomes part of the opportunity cost. If the loss of support involves a very high cost for the firm and outweighs its adoption costs, the optimal strategy will be to upgrade. Otherwise, the firm may choose to wait. Sometimes whether a firm would automatically upgrade when the vendor removes support or continue with an unsupported technology may well depend on the type of technology. Application software are upgraded more frequently than platforms and the duration of supports are also different. Removing support of platforms may adversely affect a very large number of users. Thus, for example, Microsoft would remove its support of older OS many years after its release. During that interval a number of upgraded OS may be available and a firm will face the problem of whether or not to upgrade and a model like the one proposed here will be useful to make that decision. On the other hand, some application software may become unsupported within 2years of its release. If the costs of adoption are not significant but the costs of loss of support are high, a firm may well adopt when the support is removed.

Another example of an external factor influencing the upgrade decision would be the firm's clients. For example, in a customer facing system, whether a firm has the most upgraded technology or not becomes evident to its clients using the system. Not upgrading in such instances may involve a very high opportunity cost and leapfrogging may not be the optimal strategy.

Again, if the adoption costs are not insignificant, the firm has to weigh these costs against the opportunity costs.

In addition, upgrading a particular application may be triggered by upgrade decisions of other software or hardware used. For example, if a firm that runs Windows 95 is compelled to upgrade some of its application software that require at least Windows 98, then the firm is forced to upgrade its operating system as it upgrades its application software. In this case, the decision to upgrade the application software should include the cost of upgrading the operating system as part of its adoption and change-management costs.

Thus, whether a firm is forced by a vendor to upgrade or by upgrades of other applications or platforms or by its customers, these seemingly external factors can be modelled in the opportunity or adoption costs considered in the study. In many cases, one of these costs may so overwhelmingly outweigh the other costs that there is no need to use a model to decide whether to upgrade or not. If that is not the case there remains the need to do a more systematic analysis and a model like the one proposed here can be useful.

Although the proposed model does not capture all factors that drive upgrade decisions, it does provide a framework to analyze how cost–benefit factors impact the frequency with which firms must invest in IT upgrades. It provides a normative basis to support upgrade decisions and is valuable in assessing the differential impact of the various cost factors on the decision to invest in upgrades.

## Acknowledgement

The authors thank the reviewers of the paper for many useful suggestions. The authors are responsible for any remaining errors.

## References

[1] Y. Balcer, S.A. Lippman, Technological expectations and adoption of improved technology, Journal of Economic Theory 34 (1984) 292–318.

[2] A. Bar-Ilan, Overdrafts and the demand for money, American Economic Review (1990) 1201–1216.

[3] A. Bar-Ilan, O. Maimon, An impulse-control method for investment decision in dynamic technology, Managerial and Decision Economics 14 (1993) 65–70.

[4] M. Benaroch, R.J. Kauffman, A case for using option pricing analysis to evaluate IT project investments, Information Systems Research 10 (1) (1999) 70–86.

[5] E. Bridges, A.T. Coughlan, S. Kalish, New technology adoption in an innovative market-place: micro- and macro-level decision

making models, International Journal of Forecasting 7 (1991) 257–270.

[6] G. Castner, C. Ferguson, The effect of transaction costs on the decision to replace to “off-the-shelf” software: the role of software diffusion and infusion, Information Systems Journal 10 (2000) 65–83.

[7] S. Chand, S. Sethi, Planning horizon procedures for machine replacement models with several possible replacement alternatives, Naval Research Logistics Quarterly 29 (1982) 483–493.

[8] J.P. Choi, Irreversible choice of uncertain technologies with network externalities, RAND Journal of Economics 25 (3) (1994) 382–401.

[9] K. Clemons, Evaluation of strategic investment in information technology, Communication of the ACM 34 (1) (1991) 22–36.

[10] M.A. Cohen, R.M. Halperin, Optimal Technology Choice in a Dynamic Stochastic Environment, 1986.

[11] G.M. Constantinides, S.F. Richard, Existence of optimal simple policies for discounted-cost inventory and cash management in continuous time, Operations Research 26 (1978) 620–636.

[12] B.L. Dos Santos, Justifying investment in new information technologies, Journal of MIS Research 7 (4) (1991) 71–89.

[13] J. Farrell, G. Saloner, Standardization, compatibility, and innovation, Rand Journal of Economics 16 (1) (1985) 70–83.

[14] R.K. Goel, D.P. Rich, On the adoption of new technologies, Applied Economics 29 (1997) 513–518.

[15] Information Week, Feb 14, 2000.

[16] R. Jensen, Adoption and diffusion of an innovation of uncertain profitability, Journal of Economic Theory 27 (1982) 182–193.

[17] P.C. Jones, J.L. Zydiak, W.J. Hopp, Parallel machine replacement, Naval Research Logistics 38 (1991) 351–365.

[18] P.C. Judge, A. Reinhardt, G. McWilliams, Why the fastest chip didn't win, Business Week (April 28 1997) 92–94.

[19] A. Kambil, C.J. Henderson, H. Mohsenzadeh, Strategic management of information technology: an options perspective, in: R.D. Banker, R.J. Kauffman, M.A. Mahmood (Eds.), Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage, Idea Group Publishing, Middletown, PA, 1993.

[20] M.I. Kamien, N.L. Schwartz, Timing of innovations under rivalry, Econometrica 40 (1) (1972) 43–60.

[21] M.I. Kamien, N.L. Schwartz, Potential rivalry, monopoly profits and the pace of inventive activity, Review of Economic Studies 45 (1978) 547–557.

[22] M. Katz, C. Shapiro, Network externalities, competition, and compatibility, American Economic Review 75 (3) (1985) 424–440.

[23] M. Katz, C. Shapiro, Technology adoption in the presence of network externalities, Journal of Political Economy 94 (4) (1986) 822–841.

[24] M. Katz, C. Shapiro, Product compatibility choice in a market with technological progress, Oxford Economic Studies 38 (1986) 146–165.

[25] R.J. Kauffman, J. McAndrews, Y. Wang, Opening the “Black Box” of network externalities in network adoption, Information Systems Research 11 (1) (2000) 61–82.

[26] R. Kumar, A note on project risk and option values of investment in information technologies, Journal of Management Information Systems 13 (1) (1996) 187–193.

[27] C.H. Loch, B.A. Huberman, A punctuated-equilibrium model of technology diffusion, Management Science 45 (2) (1999) 160–177.

[28] J.W. Mamer, K.F. McCardle, Uncertainty, competition and the adoption of new technology, Management Science 33 (2) (1987) 161–177.

[29] K.F. McCardle, Information acquisition and the adoption of new technology, Management Science 31 (11) (1985) 1372–1389.

[30] S. Nair, Modeling strategic investment decisions under sequential technological change, Management Science 41 (1995) 282–297.

[31] S. Rajagopalan, M.R. Singh, T.E. Morton, Capacity expansion and replacement in growing markets with uncertain technological breakthroughs, Management Science 44 (1) (1998) 12–30.

[32] J.F. Reinganum, Dynamic games of innovation, Journal of Economic Theory 25 (1981) 21–41.

[33] J.F. Reinganum, On the diffusion of new technology: a game theoretic approach, Review of Economic Studies 48 (1981) 395–405.

[34] J.F. Reinganum, A dynamic game of R&D: patent protection and competitive behavior, Econometrica 50 (3) (1982) 671–688.

[35] J.F. Reinganum, Technology adoption under imperfect information, Bell Journal of Economics 14 (1983) 57–69.

[36] A. Ricadela, A calculated decision, InformationWeek (2000 Feb 14) 22–24.

[37] C. Shapiro, H.R. Varian, Information Rules: A Strategic Guide to the Network Economy, Harvard Business School Press, Cambridge, MA, 1999.

[38] R. Stenbacka, M.M. Tombak, Strategic timing of adoption of new technologies under uncertainty, International Journal of Industrial Organization 12 (1994) 387–411.

[39] A. Sulem, A solvable one dimensional model of a diffusion inventory system, Mathematics of Operations Research 11 (1986) 125–133.

[40] A.M. Weiss, G. John, Leapfrogging behavior and the purchase of industrial innovations, Technical Working Study, vol. 89–110, Marketing Science Institute, Cambridge, MA, 1989.
