---
otero_id: 19894
otero_key: "F632PVBY"
title: "Heuristics and sensitivity analyses to guide replenishment decisions for red blood cells with random transfer"
authors: "Marilyn T. Lucas; David C. Novak; Kartikeya Puranam"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113685"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Heuristics and sensitivity analyses to guide replenishment decisions for red blood cells with random transfer

![](/api/attachments/F632PVBY/fulltext/images/f3381ecef3288729b3e83b7f93d9758ddd36bff2427603e8c54bd1e1f8d7556e.jpg)

Marilyn T. Lucas <sup>a,1</sup>, David C. Novak <sup>a,\*,1</sup>, Kartikeya Puranam <sup>b,1</sup>

<sup>a</sup> Grossman School of Business, University of Vermont, USA

<sup>b</sup> School of Business, Rutgers University Camden, USA

## A R T I C L E I N F O

Keywords: Perishable inventory Blood management Health care operations Supply chain Transfers Heuristic

## A B S T R A C T

While the transfer of blood is common in practice, research addressing replenishment strategies in the context of random or unscheduled transfers is scarce and the few papers that consider ordering policies with multiple independent sources of supply offer mathematically complex solution approaches that are difficult to implement in practice. There are no simple heuristic approaches to guide ordering decisions in these situations. In this paper, we introduce two near-optimal heuristics to guide replenishment decisions for the fixed lifetime perishable in ventory problem with random transfers. Much like the traditional base stock policy, the heuristics are straightforward to calculate and implement. The first heuristic (H1) employs a base stock policy using the convolution of demand and transfer distributions. The second heuristic (H2) emplovys a transfer adiusted base stock policy. We validate our heuristics using inventory-related cost components (i.e., order, holding, wastage, and underage costs) and demand and transfer distributions based on data provided by a large university medical center. Via simulation, we evaluate the performance of the heuristics by comparing the total costs obtained using each heuristic to the total costs obtained using the optimal ordering policy. Both heuristics perform quite well. We conduct a variety of sensitivity analyses considering the effects of different (1) levels of holding and stockout costs, as these costs are difficult to quantify and can vary dramatically, and (2) percentile transfer adjustments in H2. We observe that the H1 policy consistently results in slightly larger orders than the optimal policy, which leads to a slightly higher inventory, holding costs and wastage rates, vet slightly lower stockout costs. The H2 policy, on the other hand, consistently results in slightly smaller orders than the optimal policy, which leads to a slightly smaller inventory, lower holding costs and wastage rates, vet slightly higher stockout costs. To guide decision making, we discuss a number of management challenges that we encountered as part of this project and offer a five-step process to help decision makers with replenishment decisions.

## 1. Introduction

Blood products are perishable and must be discarded at the end of their useful lives. Their demand varies considerably in terms of quantity, frequency, and type, and effectively matching the demand and supply of blood products while simultaneously reducing both shortages and out dates is a challenging task. While the management of blood inventories is critical to successful healthcare operations, there are no universally accepted strategies and ordering policies can differ considerably from organization to organization. For example, while some organizations employ sophisticated policies derived from advanced analytics, many others use ad-hoc, often reactive, ordering practices that rely mostly on intuition. Operations research (OR) has contributed substantially to the development of decision support tools to guide replenishment policies for blood products, yet much of the research remains mathematically complex, with optimization models that are difficult to solve and solu tion procedures that are difficult to implement in practice. This makes informed ordering decisions quite challenging, and both academic scholars and healthcare providers have stressed the need for simplified, easy-to-implement ordering heuristics for blood products [1–5].

In this paper, we contribute to the healthcare management literature as well as the perishable inventory management literature by intro ducing two unique heuristic approaches for determining near-optimal blood ordering policies where the random transfer (or non-scheduled redistribution) of older red blood cell units (RBCs) from smaller lowerusage hospitals to a large high-usage blood bank (BB) occurs. In this context, a blood bank is a division of a hospital that is responsible for the ordering, storage, and testing of RBCs where transfer initiatives increase the probability that older RBCs will be used before they expire, therefore reducing waste. Although the transfer of RBCs is common practice in many healthcare networks (see [6–9], among others), research addressing replenishment strategies in the context of random transfers is scarce. The few articles that consider perishable inventory ordering policies with multiple independent sources of supply offer mathemati cally complex solution approaches that are difficult for hospital staff to implement in practice, as they are predicated on an in-depth under standing of perishable inventory management theory and dynamic programming (DP) models, and require advanced coding abilities [9]. At the same time, no simple heuristic approaches are available to guide ordering decisions in these situations. This research provides a theo retical contribution to the academic literature related to the fixed life time perishable inventory management problem while simultaneously answering the call for the development of easy-to-implement heuristics to guide ordering decisions.

Although the management of RBCs depends on other aspects of the blood supply chain (e.g. the collection, processing, and dissemination of blood products), we focus specifically on the ordering of RBCs from the perspective of a large BB within a regional healthcare market. Our contributions involve the reformulation of the analytical model pre sented in Puranam et al. [9] to provide the theoretical foundation for the development of our two novel ordering heuristics, where: (1) Heuristic 1 (H1) is a base stock policy calculated from the convolution of demand and transfer distributions, and (2) Heuristic 2 (H2) is a transfer adjusted base stock policy. We describe these novel heuristics as modified base stock policies. Like traditional base stock policies, they are straightfor ward to calculate and implement. We validate the heuristics using inventory-related cost components (i.e., order, holding, wastage, and underage costs) as well as demand and transfer data provided by a large university medical center. Via simulation, we then compare the total costs obtained from each heuristic to those obtained from a reformulated DP-based optimal ordering policy. Another contribution focuses on sensitivity analyses to guide decision-making under uncertainty, where we consider the effects of changing (a) holding and shortage costs, as these costs are difficult to quantify and can vary dramatically in practice, and (b) the percentile transfer adjustment applied to the base stock policy. These analyses offer useful insights into how hospitals might alter their standing ordering policies when expected holding or wastage costs are relatively high or low compared to baseline values. We use the sensitivity results to provide practical, easy-to-implement guidance to practitioners concerning blood replenishment decisions where random transfers occur.

## 1.1. Background

The University of Vermont’s Medical Center (UVM-MC) is the hub of a healthcare network that includes over 20 smaller hospitals and med icals centers throughout Vermont and upstate New York. Responsible for procuring, storing, and distributing the different types of RBCs needed to support a wide array of medical procedures, the UVM-MC BB orders RBCs directly from the American Red Cross (ARC) on a rolling standing order basis every day of the week - excluding Sundays. The order process is facilitated via an annual contractual agreement whereby the BB pro vides the ARC with annual demand projections for each blood type based on historical data. Purchase prices are then negotiated, at least in part, based on the volume of demand and expected quantity of blood ordered by the UVM-MC.

In general, the effective management of RBCs is a challenging task due to the large volume of blood passing through the BB, the perish ability of the product, and the uncertainty of demand for the different types of blood. This task is further complicated by the added uncertainty in supply created by the random transfer of RBCs and compounded by the shorter remaining shelf life of these units.<sup>2</sup> Although the random transfer of RBCs is less than ideal from an inventory management perspective, the UVM-MC considers the BB’s ability to accept these transfers an essential part of their overall service mission. The arrange ment allows the smaller, lower-volume organizations to stock a wider range of blood products and provides them with more flexibility with respect to their ordering practices since they do not have to assume the full risk associated with outdating, including the cost of disposal for units that expire. Based on available data, it is estimated that the RBC inventory at the UVM-MC BB is comprised of about 77% units supplied via standing order and 23% units supplied via transfer. Thus, nearly one out of every four units in inventory is supplied via transfer. The BB observes an average wastage rate of about 7%, which is notably highe than the average national level of 2.4%.

This research project has made it apparent that the BB at the UVM-MC does not utilize standardized decision support tools or advanced analytics to help with the management of its inventory and we have noted a number of shortcomings. First, the BB’s ability to collect, organize, and analyze demand and transfer data in real-time is limited. Second, the UVM-MC, like many not-for-profit hospitals, does not manage its inventory of RBCs by analyzing the traditional cost compo nents associated with perishable products (i.e. order, holding, wastage, and underage costs). As such, the management of blood products can differ significantly from other perishable inventory management prob lems where individual cost components are readily quantified and ordering decisions are based on clearly defined cost minimization and service level objectives. Third, the BB employs a “best effort” FIFO policy as opposed to a strict FIFO policy. The actual policy involves manually sorting and re-organizing units in three large refrigeration units on a daily basis. This approach, best characterized as reactive and riskaverse, is designed to achieve a 100% service level, which contributes to large inventories and wastage that exceed national averages. The challenges associated with balancing the trade-offs between reducing wastage costs and achieving higher service levels are well documented in the perishable inventory management literature [2,5,10].

In sum, the UVM-MC BB faces a complicated inventory management problem with conflicting objectives. On one hand, management seeks to minimize wastage while, on the other, they want to maintain a nearperfect service level. Thus, the BB is attempting to balance the service level and wastage tradeoff in a context where its ability to use data/ information is limited, holding and stockout costs are difficult to quantify, and where random transfers from smaller hospitals in the regional healthcare network commonly occur.

The remainder of the paper is structured as follows. In Section 2, we review literature addressing periodic review replenishment policies for the management of blood products and associated heuristic procedures. We provide a detailed discussion of the proposed heuristics in Section 3. In Section 4, we discuss the simulation analysis where we evaluate the performance of the two heuristics using empirical data. We then conduct extensive sensitivity analyses. We offer specific managerial insights and suggestions in Section 5. Conclusions and suggestions for future research are presented in Section 6.

## 2. Literature related to the management of blood inventory

The literature related to the perishable inventory problem is vast. As such, we limit our review to research on periodic review replenishment policies for a fixed lifetime perishable product, focusing on the man agement of blood products, as these papers are most relevant. Reviews of perishable (or deteriorating) inventory systems can be found in [10–15], among others. For an overview of blood inventory management, we refer readers to [16,17].

## 2.1. Modeling the perishable inventory management problem

The earliest work on inventory management for perishable products can be traced back to van Zyl [18]. It is, however, on the seminal work by Nahmias and Pierskalla [19] that much of the analytical research on this topic rests. The authors formulate the perishable inventory man agement problem as a DP, with a cost function that incorporates shortage, holding, ordering, and stockout costs, and describe the optimal ordering policy for a single perishable product with a lifetime of two periods. Building on Nahmias and Pierskalla [19], Fries [20] and Nah mias [21] then, independently, extend the two-period lifetime model to characterize the optimal ordering policy for a general lifetime of m pe riods $( \mathrm { i } . \mathrm { e } . , m > 2 )$ . Their models, which are similar in many aspects, differ in their treatment of shortage and wastage costs. Specifically, Fries [20] assumes lost sales, while Nahmias [21] assumes backlogging of unsatisfied demand. Fries [20] assumes that wastage costs are incurred in the period in which the items become outdated, while in Nahmias [21], wastage costs are incurred in the period the items are ordered. Nonetheless, both authors show that the optimal ordering policy is a function of the quantity and age composition of the inventory on hand. They also observe that (1) the optimal order quantity decreases by less than one unit for an increase in inventory of any age by one unit, and (2) changes in newer inventory (fresher products) have a greater impact on the order quantity than changes in older inventory (more dated prod ucts). These papers provide the theoretical foundation of our work.

## 2.2. Heuristic solutions to the perishable inventory problem

The findings from Fries [20] and Nahmias [21] make it clear that generalizing the two-period model to multiple periods where $m > 2$ drastically complicates the perishable inventory problem. Because of the multi-dimensional state vector required to track inventory units of each age, determining optimal policies becomes computationally challenging for large values of m. The added complexity due to the “curse of dimensionality” has led researchers to focus their efforts on finding approximate or heuristic policies to the m-period perishable inventory problem, and this is where our focus lies. Heuristic policies typically consist of simple rules derived from the simplification of the original model. Simplification occurs by modifying the cost structure of the problem, altering the process dynamics of the problem, or both [3]. Among the heuristic policies, the simplest is the base stock or critical number policy, which calls for a fixed order-up-to quantity (i.e., the amount ordered each period raises the total inventory to the same fixed level). This simple policy, which does not account for the age distribu tion of the units in inventory, is quite effective [3].

Subsequent works by Nahmias [22–25] propose a number of good approximations for the determination of the critical number. For example, in Nahmias [22], the approximate ordering policies are based solely on the total number of units in the on-hand inventory in a particular period. The author proposes and evaluates three alternative classes of approximate ordering policies. The first two policies, a critical number policy and a linear policy, possess properties associated with the optimal DP-based solution described in Nahmias [21], while the third consists of a modified critical number policy, as suggested by Van Zyl [18]. The first two policies outperform the third; achieving results close to the optimal order quantities and costs for a wide range of problems. In a subsequent paper, Nahmias [23] proposes an upper bound (based only on the total inventory on hand) on the expected outdating cost and uses this bound to compute a myopic approximate critical number policy. For lifetimes of $m = 2$ and $m = 3 ,$ the author finds that, on average, the optimal order quantity is 3 to 5% lower than the optimal critical num ber, with total costs that are within 1% of those obtained with the optimal critical number policy. In Nahmias [22], the author compares the two perishable inventory models introduced in Fries [20] and Nahmias [21] with respect to the computation of the approximate critical number policy developed in Nahmias [23]. He shows that, by substituting a discounted underage cost into the DP suggested in Nah mias [21], the models in Fries [20] and Nahmias [21] are essentially equivalent and that the myopic critical number approximation devel oped in Nahmias [23] performs equally well for these two models.

In Nahmias [25], the author constructs a bound on the expected outdating function and uses an approximate transfer function in order to approximate the original m-period problem by a DP of reduced dimen sionality r. When r = 2, the approximation consists of solving a two-state DP with only new and old inventory. The author then compares the performance of this heuristic performance with that of the optimal policy and the myopic critical number approximation from Nahmias [23]. Other early works on finding a suitable form for approximate policies include Cohen [26] and Chazan and Gal [27]. Cohen [26] shows the existence of a stationary distribution for the vector of on-hand in ventories and then derives the optimal critical number policy for the m = 2 case. The proposed policy, however, only performs well for rela tively small values of m. Chazan and Gal [27] take a similar approach and develop improved bounds on expected outdating that is useful for large values of m.

Related work by Nandakumar and Morton [28] builds on properties identified in Nahmias [21] to derive near myopic heuristics. In the context of a FIFO inventory issuance and with no lead times, the authors first determine upper and lower bounds for the optimal order-up-to quantities, which are combined into a weighted average to construct a new heuristic. The performance of the weighted bound heuristic i compared to that of two other heuristics, including the critical number policy from Nahmias [23]. The authors find that their heuristic performs as well as the other approximate solution methods. They note that the performance of all three heuristics (1) improves as the product lifetime increases, (2) is dependent on the coefficient of variation of the demand distribution, and (3) is particularly sensitive to the magnitude of the wastage cost. More recently, Haijema and Minner [29] extend these bounds to more general settings with positive lead times and mixed inventory issuing.

Some approximate solutions have taken into account information about the age of the inventory. For example, Brodheim, et al. [30], who model the blood inventory problem as a Markov chain, simplify the structure of the m-period problem by focusing only on the quantity of new items arriving in the system. More recently, Broekmeulen and Van Donselaar [31] propose a modified base stock policy for the perishable inventory problem with batch ordering, positive lead times, and time varying demand that uses information about the age distribution of the inventory and the withdrawal behavior (LIFO vs. FIFO issuance). Duan and Liao [32], who propose another age-based replenishment policy that relies only partial information (i.e., an “old inventory” ratio) to assess the freshness of the entire inventory, show that these two agebased policies perform better than a base stock policy, leading to sub stantial cost reductions, especially in decentralized environments.

We list below a number of studies that investigate other aspects of perishable inventories. For example, Pierskalla and Roach [33] show that FIFO is the optimal issuing policy for the perishable inventory problem and studies with LIFO issuance have consequently been less common. In instances where users choose the products themselves (e.g., fresh produce in grocery stores) or when procedures require blood transfusions of the highest degree of freshness, LIFO issuance might be more appropriate. Cohen and Prastacos [34] develop a critical number policy for the perishable inventory problem characterized by LIFO issuance. The authors compare optimal policies and expected costs in FIFO and LIFO systems, and note that, while order-up-to levels under the two systems are not significantly affected, expected costs are signifi cantly higher for the LIFO issuing policy.

Most studies have also assumed single demand stream. Haijema, et al. [29,35], however, look at replenishment rules for the perishable inventory problem when there are two age-differentiated demand streams for blood products $( \mathrm { i . e . } ,$ , young versus old). Similarly, Deniz, et al. [36] investigate the joint perishable inventory issuance and replenishment problem under multiple age-differentiated demand streams. The authors evaluate the efficiency of base stock policies when inventory pooling via substitution is possible. In Haijema [37], the author introduces an optimal stock-age dependent disposal policy under (a) a base stock policy and under (b) optimal stock age dependent ordering; and compares the impact of these policies on costs, wastage, and stock outs. Civelek, et al. [1] develop a reduced state agedifferentiated heuristic for a perishable inventory with multiple de mand streams. They also allow for substitution in that unmet demand can be satisfied using the “closest age” platelets first. The authors conduct sensitivity on changes in the demand structure between young, mature, and old platelets. For a recent overview of stock-age dependent order policies, refer to Haijema and Minner [35].

Our review of approximate/heuristic solution procedures for perishable inventory problems shows that modified base stock policies have performed well in a variety of settings. We now turn to the review of the literature on perishable inventories in supply networks when transfers are allowed.

## 2.3. The transfer of blood

The development of optimal ordering policies has primarily focused on dyadic relationships consisting of a single organization and a single supplier; it typically does not account for network effects. While the dyadic relationship between a single supplier (or issuer) and a single user (where demand is satisfied) is essential in developing theoretical foundations for optimal ordering policies; in practice, blood inventory management does not occur in isolation. In fact, a number of studies document various initiatives that have been undertaken to redistribute blood among hospitals in an effort to reduce shortages and outdates.

The idea of collaboration through blood redistribution (or lateral blood transshipments, as also referred to in the literature, see $[ 5 , 8 , 3 8 ] )$ within a regional healthcare network, is not new. For example, Jennings [39] describes potential transshipment strategies at the regional level to avert shortages or outdates of blood products. Kendall and Lee [40] note that while blood redistribution occurs in many hospital networks, it tends to be ad hoc. As such, they propose a goal programming frame work to accommodate the trade-offs among the multiple goals and diverging priorities of the different players within a regional network. Prastacos and Brodheim [41] develop a decision support system, based on an optimizing algorithm, for regional blood management when blood redistribution among regional hospitals is allowed. Gregor et al. [42] compare, through a simulation analysis, the performance of two in ventory policies: one that allows hospitals to “return” excess inventory to the supplier, while the other allows frequent redistribution of blood between regional hospitals. The authors found that blood redistribution results in both lower wastage and lower shortages at the regional level.

In many studies, blood redistribution consists of a bi-directional flow between multiple parties and is viewed as an integral part of a planned inventory management strategy. For others, blood redistribution (or blood transfer) denotes specifically the unidirectional flow of older blood from smaller lower-usage hospitals to larger, higher usage ones (e. g., [6,7,43]). Random or unscheduled transfers, which are not under the control of the receiving entity, represent a random second source of supply and add another layer of complexity onto the blood inventory problem. As previously noted, the motivation for such transfers is that they will increase the likelihood of the older blood being used before it expires, thereby reducing waste. For example, Denesiuk, et al. [43] examine the design and implementation of a redistribution system for near-outdated blood from smaller, remote hospitals to a large, high usage hospital in Canada. However, this study is empirical in nature as opposed to analytical, and does not focus on the impact of transfers on optimal ordering policies. Blake, et al. [7] investigate the impact of reducing the shelf life of blood on emergency orders, wastage, and stockouts for a healthcare network in Quebec, Canada. The authors use historical data to simulate different issuance strategies $( \mathrm { i . e , }$ strict FIFO versus variations in FIFO) when blood less than ten days old can be transferred. Finally, Barty, et al. [6] report the outcomes of an evidencebased benchmarking program in Ontario, Canada where the trans shipment of older blood from lower usage hospitals to higher usage hospitals is standard practice.

Theoretical research on optimal replenishment policies and how they are affected by multiple independent sources of random supply is scarce.<sup>3</sup> Notable exceptions include the works by Puranam, et al. [9,44]. In [44], the authors expand the single-period newsvendor model to ac count for uncontrolled transfers that arrive independently from the blood supplied via the standard ordering process. They derive analytical results for the newsvendor model with random transfers for a variety of product demand/transfer distribution combinations. In [9], the authors build upon the seminal work of Nahmias and Pierskalla [19] by incor porating multiple sources of random supply resulting from the transfers of older blood. The authors propose a DP model to investigate the problem. They then compare the performance of their optimal DP-based policy to that of both the current ordering process in place at the large BB and a traditional base stock (BS) policy. Their results show that the DP-based policy yields significant cost savings while maintaining a service level of nearly 99.9% and reducing wastage. They also demon strate the traditional BS policy does not perform as well in situations where blood is randomly transferred. Thus, there is both practical and theoretical value in the development of efficient heuristics for the perishable inventory problem with random transfers. Note that in [9], the authors do not address the theoretical foundation for the develop ment of heuristic solutions to the perishable inventory problem with transfers or explore how different levels of holding or underage costs may affect ordering decisions. We examine these issues in this paper.

## 3. Development of heuristics

In this section, we highlight the theoretical foundations on which the optimal ordering policy for the fixed lifetime, perishable inventory problem with multiple independent sources of supply is based. Notably, we modify the Puranam et al. [9] model, by (1) altering the order in which the older blood is used $( \mathrm { i . e . , }$ , the issuance of blood), and (2) ac counting for perishability in the way the base stock policy is calculated. This allows us to develop two novel heuristics for addressing the fixed lifetime, perishable inventory problem with random transfers. In [9], the authors introduce a DP model to calculate optimal issuing policies where blood is supplied independently from one of two sources: (1) randomly via transfer, or (2) deterministically via order. Newly arriving blood received via order is assumed to have a lifetime of two periods $( \mathrm { i . e . , }$ $\ " \mathrm { \Omega } ^ { \mathrm { n e w } ^ { \mathrm { \prime \prime } } } )$ and transferred blood a lifetime of one period $( \mathrm { i . e . , \tilde { \Omega } ^ { o l d ^ { \prime \prime } } } ) ;$ this generalized lifetime assumption is similar to the assumptions employed in $[ 2 1 , 2 3 , 4 0 , 4 1 , 4 7 ]$ . We next discuss the modifications made to the cost functions and DP. The original formulations are presented in Appendix A. Notation is summarized in Table 1 below.

To derive our heuristics, we first alter the order in which the older blood is used $( \mathrm { i . e . } ,$ , from x to z to y in [9] to z to x to y here). Demand in any given period, $D _ { i s }$ is now satisfied according to the following:

1) Units are taken from newly arriving transfers, z

2) If or when z is exhausted, demand is satisfied from the current onhand inventory, x.

Table 1 Model notation.

<table><tr><td>Symbol</td><td>Interpretation</td></tr><tr><td>x</td><td>the number of RBC units in inventory at the beginning of each period</td></tr><tr><td>y</td><td>the number of RBC units ordered at the beginning of each period (arrive instantaneously)</td></tr><tr><td>z</td><td>actual number of RBC units transferred at the beginning of each period</td></tr><tr><td>Z</td><td>random variable representing transfers</td></tr><tr><td> $z_{max}$ </td><td>maximum number of RBC units transferred</td></tr><tr><td> $D_i$ </td><td>demand for blood in period i, where i = 1, 2BG</td></tr><tr><td>F(u)</td><td>cumulative density function for blood demand</td></tr><tr><td>f(u)</td><td>probability density function for blood demand</td></tr><tr><td> $μ_D$ </td><td>mean demand for blood (RBC units)</td></tr><tr><td> $σ_D$ </td><td>standard deviation of demand for blood (RBC units)</td></tr><tr><td>G(z)</td><td>cumulative density function for transferred blood</td></tr><tr><td>g(z)</td><td>probability density function for transferred blood</td></tr><tr><td> $μ_Z$ </td><td>mean number of RBC units transferred</td></tr><tr><td> $σ_Z$ </td><td>standard deviation of RBC units transferred</td></tr><tr><td> $c_o$ </td><td>per unit ordering cost</td></tr><tr><td> $c_h$ </td><td>per unit holding cost</td></tr><tr><td> $c_w$ </td><td>per unit wastage cost</td></tr><tr><td> $c_u$ </td><td>per unit stockout or underage cost</td></tr><tr><td> $Ω_1$ </td><td>wastage in order quantity, y</td></tr><tr><td> $Ω_2$ </td><td>wastage in transfer quantity, z</td></tr><tr><td> $W_n$ </td><td>expected total cost</td></tr><tr><td> $V_n$ </td><td>minimum of the expected total cost</td></tr><tr><td>α</td><td>discount factor</td></tr></table>

3) If or when both z and x are exhausted, demand is satisfied from newly arriving standing order units, y.

The new issuance pattern captures a FIFO issuance policy as the age of the transferred blood, z, is the same as the age of the blood in on-hand inventory, x. While most costs remain unchanged from the original model, the assessment of the wastage costs is affected by the change in issuance. Wastage, as reflected by the variables $\Omega _ { 1 }$ (orders) and $\Omega _ { 2 }$ (transfers) respectively, is now calculated as:

$$
\begin{array}{r c l} \Omega_ {1} & = & \left\{y - \left[ D _ {2} + (D _ {1} - x - Z) ^ {+} \right] \right\} ^ {+} \\ \Omega_ {2} & = & \left[ Z - D _ {1} \right] ^ {+} \end{array}
$$

The change in the order of issuance in older blood allows for the development of a more mathematically sensible single-period cost function through the creation of a new random variable, $\widetilde { D } ,$ which is referred to as the apparent demand in period 1 and is defined as $\widetilde D = D _ { 1 }$ <sub>1</sub> − Z . Note that D <sup>̃</sup> has support on the interval $[ - z _ { m a x } , \infty )$ . By substituting the variable $\widetilde { D }$ for $D _ { 1 } - Z ,$ the wastage variables are then rewritten as:

$$
\begin{array}{r c l} \Omega_ {1} & = & \left\{y - \left[ D _ {2} + (\widetilde {D} - x) ^ {+} \right] \right\} ^ {+} \\ \Omega_ {2} & = & \left[ - \widetilde {D} \right] ^ {+} \end{array}
$$

We next present Theorem 1 and the supporting proof (please refer to Appendix B) to calculate the expected values of wastage in y and wastage in Z, where Δ(u) and δ(u) represent the cumulative and prob ability distribution functions of D <sup>̃</sup> respectively.

Theorem 1:

Let Ω and $\Omega _ { 2 }$ be random variables representing the wastage in the orders and transfers, respectively. Then,

$$
\begin{array}{l} E [ \Omega_ {1} ] = \int_ {o} ^ {y} \Delta (u + x) F (y - u) d u \\ E [ \Omega_ {2} ] = \int_ {- z _ {\max}} ^ {0} \Delta (t) d t \end{array}
$$

From Theorem 1, we derive the modified single period cost function shown in Eq. (1).

$$
\begin{array}{l} C (x, y) = c _ {o} y + c _ {h} \int_ {- z _ {\max}} ^ {x + y} (x + y - u) \delta (u) d u + c _ {u} \int_ {x + y} ^ {\infty} (u - x - y) \delta (u) d u \\ \qquad + c _ {w} \int_ {0} ^ {y} \Delta (\mathrm{u} + \mathrm{x}) \mathrm{F} (\mathrm{y} - \mathrm{u}) d u + c _ {w} \int_ {- z _ {\max}} ^ {0} \Delta (\mathrm{u}) d \mathrm{u}. \end{array}\tag{1}
$$

This leads to the modified DP model in $\operatorname { E q . } \left( 2 \right) .$ , where $W _ { n } ( x , y )$ is the expected total cost when y units are ordered given that x units are currently on hand. Let $V _ { n } ( x )$ be the minimum of the expected total cost when there are x units on-hand, $y _ { n } ( x )$ is the value of y that is the infimum of $W _ { n } ( x , y ) ,$ , and $\alpha < 1$ is the discount factor where the objective is to minimize the total discounted cost.

$$
V _ {n} (x) = W _ {n} \left(x, y _ {n} (x)\right) = \inf \left\{W _ {n} (x, y) \right\}\tag{2}
$$

where.

$$
W _ {n} (x, y) = C (x, y) + \alpha \int_ {- z _ {\max}} ^ {\infty} V _ {n - 1} (y - (u - x) ^ {+}) \delta (u) d u
$$

$W _ { n } ( x , y )$ is then further simplified as follows:

$$
W _ {n} (x, y) = C (x, y) + \alpha V _ {n - 1} (y) \Delta (x) + \alpha \int_ {x} ^ {\infty} V _ {n - 1} (x + y - u) \delta (u) d u
$$

We next present Theorem 2 (please refer to Appendix C for sup porting proof), which establishes the existence, uniqueness, and prop erties of the optimal order quantity in the multi-source environment with random transfers.

Theorem 2:

Via the proof in Appendix $\mathrm { C } ,$ we show that the optimal order quan tity, y (x), has the following properties:

$$
\begin{array}{l} - 1 \leq \frac {d y _ {n} (x)}{d x} \leq 0 \\ \lim _ {x \to \infty} y (x) = 0 \\ 1. \frac {d y _ {n} (x)}{d x} = - 1 \text { as } x \to \infty \end{array}
$$

In summary, we use Theorems 1, 2, and their supporting proofs to establish an upper bound for the order quantity that is foundational to both heuristics. We know that as x (units on hand) increases, we order fewer units of blood. From the literature, we know that the optimal policy for the non-perishable version of this problem is a critical number or base stock policy. Here, we find the smallest value of $x , ( x c )$ , for which it is optimal to order zero units $( { \mathrm { i . e . , } } y _ { n } ( x c ) = 0 )$ and use that value of x as the order-up-to level for the base stock policy as the starting point for both heuristics. This implies that:

$$
\begin{array}{l l l} y _ {n} (x) = & \underline {{x}} _ {c} - x & x \leq \underline {{x}} _ {c} \\ y _ {n} (x) = & 0 & x > \underline {{x}} _ {c} \end{array}
$$

As part of the proof of Theorem $^ { 2 , }$ we show that $\begin{array} { r } { \frac { \partial W _ { n } ( x , y ) } { \partial y } = 0 } \end{array}$ for $y =$ $y _ { n } ( x ) .$ . Consider the limit, $\begin{array} { r } { l i m \frac { \partial W _ { n } ( \overline { { x } } . y ) } { \partial y } , } \end{array}$ where x represents the value of x where it is optimal to order $t - z _ { m a x } .$ We set the base stock level $x c ,$ , by first finding the smallest value of x where it is optimal to order zero units of blood such that $y = 0$ . This implies that $x c = \overline { { x } } - z _ { m a x }$ using a base stock policy. The value of x is used to set the corresponding value of x c. By taking the limit $y  \ - \ z _ { m a x } ,$ we can simplify the partial derivative as shown in Eq. (3) where $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { ( c _ { h } + c _ { u } ) } \ast \ } \end{array}$

$$
\begin{array}{r l} \underset {y \to - z _ {\max}} {\text { lim }} \frac {\partial W _ {n} (\bar {x} , y)}{\partial y} & = [ c _ {o} (1 - \alpha) - c _ {u} ] + (c _ {h} + c _ {u}) \Delta (\bar {x} - z _ {\max}) = 0 \\ & \Longrightarrow \Delta (\bar {x} - z _ {\max}) = \phi \\ & \Longrightarrow \Delta \left(\underline {{x}} _ {c}\right) = \phi \\ & \Longrightarrow \underline {{x}} _ {c} = \Delta^ {- 1} (\phi) \end{array}\tag{3}
$$

We then use the critical ratio as defined by $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { ( c _ { h } + c _ { u } ) } } \end{array}$ in the development of both heuristics. We note that the proposed heuristics possess properties similar to those of the optimal DP-based order policy, as developed in Puranam et al. [9]. Designing heuristics with properties similar to those of the optimal ordering policy is an approach employed by Chazan and Gal [27], Cohen and Prastacos [34], Nahmias [3,23–25,48], and Nandakumar and Morton [28].

Heuristic 1:

Heuristic 1 (H1) employs a base stock policy that relies on the apparent demand (∆ demand of ${ \tilde { D } } ) ,$ , using the convolution of the demand and transfer distributions. In this case, the transfer distribution is directly accounted for in the calculation of the base stock policy. We construct the first heuristic as follows:

Step 1: Calculate the critical ratio $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { ( c _ { h } + c _ { u } ) } . } \end{array}$

Step 2: Calculate the base stock level as: $S ^ { * } = \Delta ^ { - 1 } ( \phi )$

Heuristic 2:

Heuristic 2 (H2) uses only the demand distribution to calculate the base stock policy. Thus, it is arguably more straightforward to imple ment in practice because the transfer distribution is not used in calcu lating the base stock. Rather, transfers are subtracted from the base stock policy to calculate the order quantity. The second heuristic represents a notable improvement over the modified base stock policy introduced in Puranam et al. [9] as it directly accounts for perishability when calcu lating the critical ratio.

H2 consists of the following steps. We first calculate the critical ratio and apply this value to the demand distribution to obtain a base stock level. We then adjust the base stock level downward by subtracting the mean transfer value to obtain the mean transfer adiusted base stock level.

As shown in Eq. (5), $\begin{array} { l } { \displaystyle { x c = \Delta ^ { - 1 } ( \phi ) \mathrm { o r } \Delta \biggl ( x c \biggr ) = \phi . } } \end{array}$ If we assume an upper limit of $z _ { m a x }$ (the maximum transfer value), we can rewrite this equation as:

$$
\begin{array}{c} \mathrm{P} \bigg (\mathrm{D-Z< } \underline {{x}} _ {c} \bigg) = \phi \\ \int_ {0} ^ {z _ {m a x}} P \bigg (D - z <   \underline {{x}} _ {c} \bigg) g (z) d z = \phi \end{array}
$$

$$
\begin{array}{r l} & \Longrightarrow \int_ {0} ^ {z _ {\max}} F \left(\underline {{x}} _ {c} + z\right) g (z) d z = \phi \\ & \Longrightarrow E _ {G} \left[ F \left(\underline {{x}} _ {c} + Z\right) \right] = \phi \end{array}
$$

Using the first order Taylor approximation of $F { \Biggl ( } x c + Z { \Biggr ) }$ at $Z = \mu _ { Z }$ gives us:

$$
\begin{array}{c} E _ {G} \left[ F \left(\underline {{x}} _ {c} + Z\right) \right] \approx E _ {G} \left[ F (x _ {c} + \mu_ {Z}) + F ^ {\prime} (x _ {c} + \mu_ {Z}) \left((x _ {c} + Z) - E [ x _ {c} + Z ] \right. \right] \\ = F (x _ {c} + \mu_ {Z}) + f (x _ {c} + \mu_ {Z}) (E [ x _ {c} + Z ] - E [ x _ {c} + Z ]) \\ = F (x _ {c} + \mu_ {Z}) \end{array}
$$

Replacing $E _ { G } \Bigg [ F \Bigg ( x ( x + Z \Bigg ) \Bigg ]$ with its approximation implies:

$$
\begin{array}{c} F (x _ {c} + \mu_ {Z}) = \phi \\ \Longrightarrow \underline {{x}} _ {c} + \mu_ {Z} = F ^ {- 1} (\phi) \\ \underline {{x}} _ {c} = F ^ {- 1} (\phi) - \mu_ {Z} \end{array}
$$

If x is optimal order quantity when the inventory level is $- z _ { m a x } ,$ then the order quantity when there are no items on hand $( \mathrm { i } . \mathrm { e } . , x = 0 )$ is given by $x c = F ^ { - 1 } ( \phi ) - \mu _ { Z }$ . We construct the second heuristic as follows:

Step 1: Calculate the critical ratio $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { ( c _ { h } + c _ { u } ) } } \end{array}$

Step 2: Find the base stock leve $S ^ { * } = F ^ { - 1 } ( \phi ) - \mu _ { Z } .$

In Step $^ { 2 , }$ we adjust the value of order-up-to level associated with the base stock policy by the mean of the transfer distribution. This is consistent with the findings in Puranam, et al. [44] for the single period model. In the next section, we compare the performance of the two heuristics to that of the optimal cost minimizing order policy.

## 4. Simulation analysis

To validate the heuristics, we develop a simulation to compare the costs obtained using our two heuristics to those obtained from using the modified DP presented in this paper. We use data provided by a large university medical center. The simulation involves 3000 unique repli cations. We use a discount factor of 0.99 and employ a variancereduction technique, which entails using the same set of random numbers to generate demand and transfer values to facilitate compari sons between the different ordering policies across different cost sce narios. The beginning inventory is assumed to be 40 units.<sup>4</sup> We then calculate each of the four inventory cost components $( \mathrm { i . e . , }$ , purchasing, holding, stockout, and wastage), the total average cost, the service level, and wastage rate assuming FIFO issuance.

## 4.1. Data

Sample data consist of all incoming units of A+ blood for a 17-month time period. A+ is the second most heavily demanded and transferred blood type, representing approximately 29% and 28% of the total blood supplied and transferred, respectively. Parameters for demand and transfer distributions are estimated using JMP Pro’s distribution fitting utility. Both demand and transfers are approximated by a beta distri bution, a statistically versatile distribution that can handle both posi tively and negatively skewed data. Demand for $\mathbf { A } +$ blood is characterized by a minimum of 66 and a maximum of 120 units, and shape parameters, $s _ { 1 } = 1 . 1 1 9 6$ and $s _ { 2 } = 1 . 6 4 9 1$ . Transfers are charac terized by a minimum of eight and a maximum of 37 units, and shape parameters, $s _ { 1 } = 2 . 2 8 2 7$ and $s _ { 2 } = 2 . 9 5 5 3$ as shown in Fig. 1. The mean demand is 87.73 units $( \mathrm { i . e . }$ , approximately the 40.4th percentile) and the mean transfer is 20.21 units (i.e., approximately 43.6th percentile).<sup>5</sup>

Based on input from the UVM-MC BB, we anchor our analyses on purchase, wastage costs, holding, and stockout costs of \$300, \$900, \$75, and \$6000 per unit, respectively. We refer to this cost scenario as the base case. Obtaining cost values for purchase and wastage costs from the BB was relatively straightforward. However, holding and stockout costs are not readily quantifiable and stockout costs, in particular, are subject to substantial variation. Holding cost estimates are based on Jones and Tuzel [49] and Richardson [50]. Stockout cost estimates reflect the undesirable consequences associated with running out of blood, from the need to expedite blood delivery to rescheduling medical procedures. Accordingly, we conduct sensitivity analyses varying both stockout and holding costs, while purchase and wastage costs remain constant. These analyses should prove quite useful in guiding decision-making in realworld situations where there is quite a bit of uncertainty surrounding the selection of representative holding and stockout cost values.

![](/api/attachments/F632PVBY/fulltext/images/9fd371d7d2c8eb6b3e78aa10b9b01ddd7383560e8f8cdda2b8618027d63ac794.jpg)  
Fig. 1. Demand and transfer distributions.

## 4.2. Base case results

In Table 2, we present the individual cost components, as well as the average service level and wastage for the base case scenario for both heuristics (H1 and H2) and the DP-based optimal policy. The average service level is a measure of the percentage of demand met. For example, a 99% service level means that, on average 99% of the demand for A+ blood is met using this policy. Wastage is a percentage measure of the RBCs discarded due to expiration. For example, a wastage rate of 1% means that, on average, 1% of RBC units expire before being used and must be discarded. A classic challenge in perishable inventory man agement involves the tradeoff between the cost of wastage and the holding cost and service level (i.e., holding larger levels of inventory typically leads to higher holding costs, better/higher service levels, at the expense of increased wastage).

In the base case scenario, the optimal policy and the H1 policy produce similar results across all four cost components. The H2 policy results in slightly smaller inventory, which leads to lower holding costs and wastage, yet slightly higher stockout costs.

## 4.3. Cost-based sensitivity results

We next examine the performance of the heuristics across 15 different cost scenarios, where we consider five different stockout cost values $( \mathrm { i . e } , c _ { u } = \ S 1 5 0 0 , \ S 3 0 0 0 , \ S 6 0 0 0 ,$ , \$9000, and \$12,000 per unit) and three different values of holding cost $( \mathrm { i . e . , } c _ { h } = \$ 3 7 .50, \ S 7 5$ , and \$112.5 per unit).<sup>6</sup> In Table $^ { 3 , }$ we report the percentage difference in the average total cost between each heuristic (H1 and H2) and the optimal solution. The results associated with the base case cost scenario (i.e., $c _ { u } = \$ 6000$ unit and $c _ { h } = \mathbb { s } 7 5 / \mathrm { u n i t } )$ are shaded.

Summary information.  
![](/api/attachments/F632PVBY/fulltext/images/982614d47f2530c17f88676ff6077ae6f9ea2afb4342c78252a86ef54e5b7bf2.jpg)

<table><tr><td rowspan="2"></td><td colspan="4">Percentage Breakdown of Total Ave. Cost</td><td rowspan="2">Ave. Service Level</td><td rowspan="2">Wastage</td></tr><tr><td>Ave. Purchase</td><td>Ave. Holding</td><td>Ave. Stockout</td><td>Ave. Wastage</td></tr><tr><td>Optimal Policy</td><td>88.0%</td><td>10.3%</td><td>1.0%</td><td>0.7%</td><td>99.95%</td><td>0.21%</td></tr><tr><td>H1</td><td>87.9%</td><td>10.3%</td><td>1.1%</td><td>0.7%</td><td>99.95%</td><td>0.22%</td></tr><tr><td>H2</td><td>87.6%</td><td>9.3%</td><td>2.6%</td><td>0.4%</td><td>99.88%</td><td>0.12%</td></tr></table>

Percentage difference in ave. total cost compared to optimal solution.

<table><tr><td></td><td></td><td> $c_u =$  $1500</td><td> $c_u =$  $3000</td><td> $c_u =$  $6000</td><td> $c_u =$  $9000</td><td> $c_u =$  $12,000</td></tr><tr><td> $c_h =$ </td><td>H1</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.2%</td><td>0.0%</td></tr><tr><td>$37.5</td><td>H2</td><td>0.0%</td><td>0.0%</td><td>0.3%</td><td>0.4%</td><td>0.9%</td></tr><tr><td rowspan="2"> $c_h = \$75$ </td><td>H1</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>H2</td><td>0.0%</td><td>0.1%</td><td>0.3%</td><td>0.5%</td><td>1.1%</td></tr><tr><td> $c_h =$ </td><td>H1</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>$112.5</td><td>H2</td><td>0.0%</td><td>0.1%</td><td>0.3%</td><td>0.6%</td><td>0.6%</td></tr></table>

When comparing the results from the base case, the average total costs associated with H1 not measurably different from the optimal policy $( \mathrm { i . e . , } 0 . 0 \% ) ;$ ; while the average total costs associated with H2 are 0.30% higher than the optimal policy.<sup>7</sup> Over the range of cost scenarios, the largest difference between the optimal solution and either of the heuristics is 0.2% for H1 and approximately 1% for H2. While the per formance of H1 varies as $c _ { u }$ and $c _ { h }$ change, there is no discernable pattern (see Fig. 2a). Notice, however, that the performance of H2 appears to begin to slowly deteriorate as $c _ { u }$ becomes larger for all holding cost values (see Fig. 2b). We next offer additional insights to inform decisionmaking by hospital staff.

## 4.4. Transfer adjustment-based sensitivity results (H2 only)

Recall that for H2, the base stock is calculated as $S ^ { * } = F ^ { - 1 } ( \phi ) - \mu _ { Z } ,$ where $\mu _ { Z }$ is the mean of the transfer distribution. We next examine the performance of H2 when transfer adjustments other than the mean are considered. As smaller percentile adjustments (i.e., 1%, 2%, etc.) equate to a fraction of a unit of blood in the case of A+ blood, we convert our percentile-based transfer adjustments to whole numbers and consider only every fifth percentile between 25% and 65%.<sup>8</sup> Note that as the range of transfers becomes larger, percentile adjustments become more granular regardless of blood type. Transfer-based adjustment sensitivity is not applicable to H1 because it uses a single distribution $( \mathrm { i . e . , }$ , the convolution of the demand and transfer distributions).

We report the percentage difference in the average total cost between the optimal solution and different transfer adjusted base stock policies in Table 4. We observe that changes in holding costs have less of an effect on performance than changes in stockout costs. As such, we report only changes in stockout costs, where the “best” adjusted variation of H2 is highlighted for each value of $c _ { u } .$ The mean adjusted H2 policy (which corresponds to H2(45%) in this case) performs well in all scenarios. These values are shown in bold print.

a) Performance of H1 as c<sub>u</sub> Increases  
![](/api/attachments/F632PVBY/fulltext/images/c3c73e08bd045ce9c1f9c761dc4b7cf880010f1631d4558adafdd50cadcad893.jpg)

b) Performance of H2 as c<sub>u</sub> Increases  
![](/api/attachments/F632PVBY/fulltext/images/1c9ecf3dfc2f3f3de5f63a511e5303f288fc06c6b62f0a7689316f2817fd502a.jpg)  
Fig. 2. Percentage difference in average total cost compared to optimal solution.

Table 4  
Percentile transfer adjustment in H2: percentage difference in average total cost compared to optimal solution.

<table><tr><td></td><td> $c_u = \$1,500$ </td><td> $c_u = \$3,000$ </td><td> $c_u = \$6,000$ </td><td> $c_u = \$9,000$ </td><td> $c_u = \$12,000$ </td></tr><tr><td>H2 (25%)</td><td>0.7%</td><td>0.9%</td><td>0.8%</td><td>0.4%</td><td>0.5%</td></tr><tr><td>H2 (30%)</td><td>0.4%</td><td>0.3%</td><td>0.2%</td><td>0.2%</td><td>0.0%</td></tr><tr><td>H2 (35%)</td><td>0.1%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>H2 (40%)</td><td>0.0%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>H2 (45%)</td><td>0.0%</td><td>0.1%</td><td>0.3%</td><td>0.5%</td><td>1.1%</td></tr><tr><td>H2 (50%)</td><td>0.2%</td><td>0.3%</td><td>1.3%</td><td>1.8%</td><td>1.9%</td></tr><tr><td>H2 (55%)</td><td>0.4%</td><td>1.1%</td><td>2.1%</td><td>2.9%</td><td>4.7%</td></tr><tr><td>H2 (60%)</td><td>1.1%</td><td>1.7%</td><td>3.1%</td><td>6.0%</td><td>6.6%</td></tr><tr><td>H2 (65%)</td><td>1.6%</td><td>3.4%</td><td>5.9%</td><td>8.8%</td><td>11.8%</td></tr></table>

![](/api/attachments/F632PVBY/fulltext/images/463ea22c86187bdc87021d99b1f89836ebb88b9d1f070575e4915a654edac114.jpg)  
Heuristic 2 (Transfer Adjustment Percentile) where H2 (45%) represents the Mean  
Fig. 3. Percentile transfer adjustment in H2: percentage difference in average total cost compared to optimal solution.

The transfer adjustments in the range of 25% to 50% deviate by less than 2% from the optimal solution for all values of $c _ { u } .$ Notice that the average total cost begins to deviate from the optimal DP-based policy as $c _ { u }$ increases. This is because larger percentile-based transfer adjustments result in a lower order quantity, increasing the risk of stocking out and the financial consequence of ordering too few units becomes more se vere. Note that, overall, the order quantities associated with the H2 policies are slightly lower than the optimal policy. This leads to lower holding costs and less wastage, yet higher stockout rates and corre spondingly higher stockout costs. This pattern is illustrated in Fig. 3 and is consistent for other holding cost values. As shown in Fig. 3, to reduce the risk of stocking out, it is better to err on the side of ordering more blood than ordering less when using H2.

The pattern observed in Table 2 holds across all cost scenarios – even using different combinations of values for $c _ { h }$ and $c _ { u } .$ That is, first, the H2 policy is more sensitive to changes in $c _ { u }$ than the H1 policy. Second, the H1 policy consistently results in slightly larger orders than the optimal policy and H2 consistently results in slightly smaller orders than the optimal policy. These results offer decision-makers insight into the tradeoff associated with using the more sensitive, yet easier to calculate H2 versus the less sensitive, more complex H1.

In Fig. 4, we plot the percentage breakdown of the average total cost by individual cost component (i.e., purchase, holding, stockout, and wastage). In the interest of space, we report only the base case value for $c _ { h } , \$ 75 ,$ /unit, noting that the trends pictured in Fig. 4 for $c _ { h } , = \$ 75$ /unit also hold for $c _ { h } = \$ 37 .50$ and \$112.50/unit.

a) Ave. Purchase Cost  
![](/api/attachments/F632PVBY/fulltext/images/53ecfc98e540970d1a867c7c86379f7d7002c7a78951f1419fe626b69d0b908d.jpg)

c) Ave. Stockout Cost  
![](/api/attachments/F632PVBY/fulltext/images/05f168cfebd103fe5917620950e8249b1b20521f31011974d98a465c91abe122.jpg)

## 5. Managerial insights and suggestions

An objective of this research is to provide decision support guidance to practitioners regarding ordering policies and inventory management of perishable RBCs. As noted in the Introduction, there is little guidance regarding ordering policies with random or unscheduled transfers, and implementing a DP model in practice is quite challenging, as the mathematical formulation of such models and their conversion into executable codes are complicated undertakings that require an advanced understanding of OR and programming. Our experience mir rors that of many OR researchers who observe that hospital adminis trators and staff do not necessarily have the expertise or time needed to develop and implement decision-support tools to guide these decisions. We reiterate the need for the development of easy-to-implement heu ristics to assist with the ordering process of perishable blood products by hospital staff called for by academics and practitioners alike [1–5].

In this paper, we answer this call by developing and testing two ordering heuristics for the perishable inventory management problem with random transfers. Both heuristics perform well for different de mand and transfer patterns and over a wide range of cost parameters. We carefully lay out the theoretical justification for the heuristics and then conduct extensive sensitivity analyses focused on uncertainty regarding holding and underage costs. The primary managerial insight from our extensive sensitivity analyses is that using their own cost, demand, and transfer estimates, decision makers can implement an easyto-follow linear decision process derived from the simpler of our two heuristics - Heuristic 2 (H2), to determine near-optimal order quantities and keep inventory costs down. In our opinion, estimating the convo lution of demand and transfer distributions required to implement the H1 policy is a more complex undertaking. Thus, we recommend using H2. Recall from the previous section that, on average, the H2 policy resulted in slightly smaller orders than the optimal policy and was more sensitive to changes in $c _ { u }$ than the H1 policy. We next describe a five-step decision support/implementation process.

b) Ave. Holding Cost  
![](/api/attachments/F632PVBY/fulltext/images/2b3d5cfefc3ee5d1a3a8a85a8df8a73548eb336c4c844ee922f2ed04e7351b53.jpg)

d) Ave. Wastage Cost  
![](/api/attachments/F632PVBY/fulltext/images/9c349db93cec503d70b0608eca42c721e4a5b417b4a7a0ae377e32b66ebf4a9f.jpg)  
Fig. 4. Breakdown of average cost components.

## 5.1. A five-step linear decision process

1. Collect, organize, and analyze demand and transfer data.

a. Depending on the hospital and their experiences with data man agement and analytics, this may or may not be a challenge. In the case of the UVM-MC BB, this step will arguably be one of the biggest challenges in the implementation phase. While the aggregate number of RBC units received, successfully transfused, and discarded is reported on a monthly basis, the BB, because of a lack of IT infrastructure, expertise and time, is limited in its ability to organize (and store) data, derive basic descriptive statistics, and perform statistical analyses, such as daily/weekly usage or trend analyses by blood type. Access to such information would greatly help inform ordering decisions.

b. The Beta distribution, the versatile and flexible distribution we use in our simulation analysis, provides an accurate description of a wide range of demand and transfer patterns for the different types of RBCs.

c. Given the mean μ and variance $\sigma ^ { 2 }$ of the demand and transfer data (aggregated over two weeks), one can estimate the parameters s and $s _ { 2 }$ of the corresponding Beta distributions as follows:

$$
s _ {1} = \left(\frac {1 - \mu}{\sigma^ {2}} - \frac {1}{\mu}\right) \mu^ {2}
$$

$$
s _ {2} = s _ {1} \left(\frac {1}{\mu} - 1\right)
$$

d. One could rely on X and R-control charts to determine whether the underlying demand and transfer distributions have shifted over time. i. The parameters of the Beta distribution could be adjusted using the above formulas.

ii. A number of curve fitting software are also available to update the parameters of these Beta distributions. (For example, we used JMP Pro’s distribution fitting utility to fit data).

2. Estimate cost parameters.

a. Calculate the critical ratio $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { ( c _ { h } + c _ { u } ) } . } \end{array}$ , where α, the discount factor, accounts for the time value of money over multiple periods.

3. Find the base stock level $S ^ { * } = F ^ { - 1 } ( \phi )$

a. The base stock level is a function of cost parameters, a discount factor, and demand characteristics for RBCs. A formula in EXCEL can be used to determine the base stock level associated with these values.

4. Adjust (or decrease) the base stock level $s ^ { * }$ by the average transfer level = μ .

a. As $c _ { u }$ increases, this adjustment is reduced accordingly.

## 5.2. Estimating cost parameters

While it is universally understood that effective blood inventory management policies are predicated on informed tradeoffs between ordering, holding, underage, wastage costs, and performance objectives, it is often difficult for hospitals to quantify these costs [9,49,50]. We expect that hospitals will know the average purchase and disposal costs associated with RBCs with a high degree of certainty. In general, per holding costs for RBCs are not quantified because the cost consists of individual components that may not be tracked by hospitals and are often not itemized at the functional level. For example, holding costs are a function of the number of units on hand, the operational costs asso ciated with running the BB (electricity, water, overhead, etc.), and the time spent by staff on inventory management. Unless hospitals have the information needed to accurately estimate their per unit holding costs, we suggest relying on literature such as Jones and Tuzel [51] and Richardson [52].

Likewise, stockout costs are typically not quantified by hospitals. Clearly, this cost can be highly variable depending on the circumstance. For example, the consequence associated with postponing an elective or non-critical medical procedure is typically to reschedule the procedure. Rescheduling costs vary depending on the procedure being performed, the patient profile (overall health, weight, sex, age, etc.), and the makeup of the surgical team. Different medical procedures also vary with respect to the time requirements in the operating room and consist of different types of specialists, equipment, and support staff [53–55]. On the other hand, the consequence associated with postponing a timesensitive, life-or-death emergency procedure could be further deterio ration of the patient’s health or even death. These outcomes are not readily quantifiable, yet both are extremely undesirable. Some hospitals may be able rush order from blood suppliers in emergencies, while others may not be able to do so. We recommend that hospitals with more risk adverse profiles assume higher stockout costs.

## 5.3. Data management

Many hospitals have limited analytics and data management capa bilities and lack sophisticated decision-making tools to aid in the man agement of blood inventory. This perspective is supported in the available literature (i.e., there is a clear need for more advanced ana lytics and modeling capabilities with respect to blood management). However, we hesitate to say that our data management suggestions can be universally applied to all BBs. In this section, we describe our ob servations and offer management recommendations based on our experiences.

In working with data from the UVM-MC BB, we encountered a number of data and process issues that exacerbated inventory manage ment challenges. First, the raw data were not stored and managed in a way that was conducive to real-time decision making. Data were not stored in a database management system (DBMS). Rather, they were stored in a flat-file format in an Excel spreadsheet where each record represents an incoming unit of blood. As such, data were stored sequentially according to the time at which the RBC unit arrived into the BB inventory. Consequently, it was quite time consuming to organize the data in a manner that facilitated structured analyses. While basic searching and filtering could be performed in Excel, decision-makers could not query the data. From an operational standpoint, the BB staff examined the expiration date that was printed on each unit of blood each day. They then had to manually sort the units that were closest to expiration and move them to the front of the refrigerator. Second. date/ time fields were not formatted in a way that readily allowed for any time-based calculations such as the remaining shelf life of the RBC units currently held in inventory. For instance, producing a comprehensive list of all RBC units that are close to expiration by blood type at the beginning of each day or each week would be a manual undertaking. Third, although the BB reports the aggregate counts of the number of units received, successfully transfused, and discarded for each blood type on a monthly basis, there are no standard, structured analytics such as weekly usage or trend analyses. Thus, management cannot not readily generate visual representations such as histograms of the remaining shelf life for incoming units by blood type on a weekly basis. Finally, the internal source of demand for the units (i.e., the operational area or responsibility center within the hospital that requests and “checks out” each RBC unit) is not recorded. Thus, units are tracked in an ad-hoc as opposed to a systematic manner. As a result, summary statistics related to the demand for different blood types and the relationships between the supply and demand for the different blood types cannot be easily analyzed, although such information would greatly help inform daily ordering decisions and would likely reduce overall wastage.

## 6. Conclusions and future research

While the transfer of blood is common in many healthcare networks, research exploring optimal replenishment strategies with transfers is scarce. The few OR-based papers which consider ordering policies that address a random, second source of supply, propose mathematically complex solution approaches that may difficult for hospital staff to implement in practice, and there are no simple heuristic approaches are available to guide ordering decisions in these situations. Given the po tential high levels of uncertainty related to holding and wastage costs as well as demand, making informed blood replenishment decisions is inherently quite challenging. The ability for smaller, lower-usage hos pitals to transfer unused blood to larger, high-usage hospitals expands these challenges.

This research provides a theoretical contribution to the literature related to the fixed lifetime perishable inventory management problem, while simultaneously answering the call for the development of easy-toimplement heuristics to help guide decision-making by hospital staff [56]. In this paper, we introduce two near-optimal heuristics to guide replenishment decisions for the fixed lifetime perishable inventory problem with random or unscheduled transfers. Much like the tradi tional base stock policy, the heuristics are straightforward to calculate and implement. The first heuristic (H1) employs a base stock policy using the convolution of demand and transfer distributions. In the sec ond heuristic (H2), we calculate the critical ratio and apply this value to the demand distribution to obtain a base stock level. We then adjust that base stock level downward using the mean transfer value to obtain a transfer adjusted base stock policy. To validate our heuristics, we employ inventory-related cost components $( \mathrm { i . e . , }$ order, holding, wastage, and underage costs) and demand and transfer distributions based on empirical data provided by a large university medical center. Via simulation, we evaluate the performance of the heuristics by comparing the total costs obtained using each heuristic to the total costs obtained using the optimal ordering policy. We conduct a variety of sensitivity analyses to enhance decision-making by examining the effects of different levels of (1) holding and stockout costs, as these costs are difficult to quantify and can vary dramatically in practice, and of (2) different percentile transfer adjustments in H2. We find that both heu ristics perform very well when compared to the optimal DP-based so lution, and observe that the H1 policy consistently results in slightly larger orders than the optimal policy, which leads to a slightly higher inventory, holding costs and wastage rates, yet slightly lower stockout costs. The H2 policy, on the other hand, consistently results in slightly smaller orders than the optimal policy, which leads to a slightly smaller inventory, lower holding costs and wastage rates, yet slightly higher stockout costs.

Suggested future work involves investigating the flow of blood be tween the different organizations in a healthcare network. The extent to which the redistribution of blood affects inventory management de cisions and performance measures among the partners in the network is particularly interesting. Optimizing the management of blood at the network level could substantially reduce total costs, although this type of approach implies less control at the organizational level. Investigating the use of different replenishment policies for different blood types would also be interesting. A particularly valuable analysis could focus on the degree to which substitution affects demand for blood types such as O- and O+. Likewise, most replenishment policies are based on the FIFO issuance policy. While literature pertaining to the management of blood platelets considers situations where demand is satisfied from newer, fresher units (LIFO as opposed FIFO), this problem can be more complicated for RBCs where variations in issuance can result in different demand streams for each of the eight blood types.

Marilyn T. Lucas (Ph.D., University of Illinois at Urbana-Champaign) is an Associate Professor of Business Analytics in the Grossman School of Business Administration at the University of Ver mont. Her research interests include sustainable operations, healthcare operations and the marketing/operations interface. She has published her work in leading academic journals, including Management Science, Production and Operations Management, and European Journal of Opera tional Research.

David C. Novak (Ph.D., Virginia Tech) is a Professor of Business Analytics in the Grossman School Business at the University of Vermont. His research interests center on developing and applying innovative theoretical concepts and solution methods to real-world problems to gain unique and practical managerial insights. He is particularly inter ested in the overlaps between operations research, operations manage ment, logistics, spatial analysis, and complexity science.

Dr. Kartikeya Puranam (Ph.D., Rutgers University) is an Assistant Professor of Management at Rutgers School of Business- Camden. His research interests include bidding strategies in auctions, inventory management, Markov chains and Markov decision processes and supply chain management.

## Appendix A. Original formulations

There are x units on hand at the beginning of each period and the number of units ordered is $y ( x )$ . The demand for blood in each time period is independent with cumulative and density functions of F(u) and $f ( u )$ respectively, where $\mu _ { D }$ and $\sigma _ { D }$ are the mean and standard deviation of these random variables. Transferred blood is represented by the random variable $Z ,$ with cumulative and density functions G(z) and g(z), respectively, and a maximum transfer amount $z _ { m a x } .$ . Let μ and $\sigma _ { Z }$ represent the mean and standard deviation of these random variables, respectively. Demand is satisfied in any given period according to the following sequence:

1) Units are taken from the current inventory on-hand, x.

2) If or when x is exhausted, demand is satisfied from newly arriving transfers, z.

3) If or when both x and z are exhausted, demand is satisfied from newly arriving standing order units, $y .$

This pattern effectively captures a FIFO issuance policy. When new units arrive via standing order, the available inventory is $x + y + z$ and stockouts only occur if demand in the current period is greater than x $+ y + z .$ The variables $c _ { o } , c _ { h } , c _ { w } ,$ and $c _ { u }$ represent the per unit ordering, holding, wastage, and stockout (underage) costs, respectively

$$
\begin{array}{l} C (x, y) = c _ {o} y + c _ {h} \int_ {0} ^ {z _ {\max}} y F (x + z) g (z) d z + c _ {h} \int_ {0} ^ {z _ {\max}} \int_ {x + z} ^ {x + y + z} (x + y + z - u) f (u) d u g (z) d z + c _ {w} \int_ {0} ^ {z _ {\max}} \int_ {0} ^ {y} F (u + x + z) F (y - u) d u g (z) d z \\ \quad + c _ {w} \int_ {0} ^ {z _ {\max}} \int_ {0} ^ {z} F (x + z - u) d u g (z) d z + c _ {u} \int_ {0} ^ {z _ {\max}} \int_ {x + y + z} ^ {\infty} (u - (x + y + z)) f (u) d u g (z) d z \end{array}\tag{A1}
$$

Wastage cost is calculated as the sum of (a) the wastage in z, which is incurred in the current period, and (b) the expected wastage in $y ,$ which is incurred in the period in which the items are ordered. In other words, wastage in y is assessed when the order is placed, not when the wastage actually occurs (see Nahmias and Pierskalla, [19]).

The objective of the DP is to minimize the total discounted cost over a planning horizon of n time periods, where $W _ { n } ( x , y )$ is the expected total cost when y units are ordered given that x units are currently on hand. Let $V _ { n } ( x )$ be the minimum of the expected total cost that is the infimum of $W _ { n } ( x , y ) _ { ; }$ where $y _ { n } ( x )$ is the optimal order quantity. The objective function of the DP is shown in $\operatorname { E q . } \left( 2 \right)$ , where $\alpha < 1$ is the multi-period discount factor.

$$
V _ {n} (x) = W _ {n} \left(x, y _ {n} (x)\right) = \inf _ {y \in R ^ {+}} \left\{W _ {n} (x, y) \right\}\tag{A2}
$$

where.

$$
\begin{array}{l} W _ {n} (x, y) = C (x, y) + \alpha \int_ {0} ^ {z \max} \int_ {0} ^ {\infty} V _ {n - 1} (y - (\mu - x - z) ^ {+}) g (z) d z f (u) d u \\ W _ {n} (x, y) = C (x, y) + \alpha \int_ {0} ^ {z \max} V _ {n - 1} (y) F (x + z) g (z) d z + \alpha \int_ {0} ^ {z \max} \int_ {0} ^ {\infty} V _ {n - 1} (x + y + z - u) f (u) d u g (z) d z, \end{array}
$$

From Eq. (2), the authors prove in Puranam et al. [9] that the optimal order quantity $y _ { n } ( x )$ has the following properties:

$$
- 1 \leq \frac {d y _ {n} (x)}{d x} \leq 0
$$

$$
\lim _ {x \to \infty} y (x) = 0
$$

$$
\frac {d y _ {n} (x)}{d x} = - 1 \text {   as   } x \to \infty
$$

## Appendix B. Proof of Theorem 1

We know that $\Omega _ { 1 } = \left\{ y - \left[ D _ { 2 } + \left( \widetilde { D } - x \right) ^ { + } \right] \right\} ^ { + }$ . Because $W _ { 1 }$ is a positive random variable we will calculate $E [ \Omega _ { 1 } ] = \intop _ { 0 } ^ { \infty } P ( W _ { 1 } > t ) d t$ . Notice the

following:

$$
\begin{array}{l} P (\Omega_ {1} \leq t) = 0 \text {   if   } t <   0 \\ P (\Omega_ {1} \leq t) = 1 \text {   if   } t > y. \end{array}
$$

For $0 \le t \le y$ we calculate $P ( \Omega _ { 1 } \leq t )$ as follows:

$$
\begin{array}{l} P (\Omega_ {1} \leq t) = P \Big (\Omega_ {1} \leq t \cap \widetilde {D} <   x \Big) + P \Big (\Omega_ {1} \leq t \cap \widetilde {D} \geq x \Big) \\ = P (y - D _ {2} \leq t) P \Big (\widetilde {D} <   x \Big) + P \Big (x + y - D _ {2} - \widetilde {D} \leq t \cap \widetilde {D} \geq x \Big) \\ = P (D _ {2} > y - t) P \Big (\widetilde {D} <   x \Big) + \int_ {x} ^ {\infty} P (D _ {2} > x + y - u - t) \delta (u) d u \\ = (1 - F (y - t)) \Delta (x) + \int_ {x} ^ {\infty} (1 - F (x + y - u - t)) \delta (u) d u \\ = (1 - F (y - t)) \Delta (x) + (1 - \Delta (x)) - \int_ {x} ^ {\infty} F (x + y - u - t) \delta (u) d u = 1 - F (y - t) \Delta (x) - \int_ {x} ^ {x + y - t} F (x + y - u - t) \delta (u) d u \\ = 1 - F (y - t) \Delta (x) - \int_ {0} ^ {y - t} F (y - v - t) \delta (v + x) d v. \end{array}
$$

Applying integration by parts we have,

$$
= 1 - F (y - t) \Delta (x) + F (y - t) \Delta (x) - \int_ {0} ^ {y - t} f (y - v - t) \Delta (v + x) d v
$$

$$
= 1 - \int_ {0} ^ {y - t} f (y - u - t) \Delta (u + x) d u.
$$

This implies that,

$$
E [ \Omega_ {1} ] = \int_ {0} ^ {y} \int_ {0} ^ {y - t} f (y - u - t) \Delta (\mathrm{u} + \mathrm{x}) \mathrm{du} \mathrm{dt}
$$

$$
E [ \Omega_ {1} ] = \int_ {0} ^ {y} \Delta (u + x) F (y - u) d u.
$$

We know that $\Omega _ { 2 } = \left[ - \widetilde { D } \right] ^ { + }$ . We know that $\widetilde { D }$ has a domain of $[ - z _ { m a x } , \infty )$ and so $\left[ - \widetilde { D } \right] ^ { + }$ has a domain of $[ 0 , z _ { m a x } ]$ . For $0 \leq t \leq z _ { m a x }$ we have: P(Ω<sub>2</sub> ≤ t) = P − D<sup>̃ +</sup> ≤ t

$$
\begin{array}{l} = P \left(\left[ - \widetilde {D} \right] ^ {+} \leq t \cap \widetilde {D} <   0\right) + P \left(\left[ - \widetilde {D} \right] ^ {+} \leq t \cap \widetilde {D} \geq 0\right) \\ = P \left(- t <   \widetilde {D} <   0\right) + P (\widetilde {D} \geq 0) \\ = P \left(- t <   \widetilde {D} <   \infty\right) \\ = 1 - \Delta (- t) \\ \text { This   implies   that, } \end{array}
$$

$$
E [ \Omega_ {2} ] = \int_ {0} ^ {\infty} P (\Omega_ {2} > t) d t
$$

$$
= \int_ {0} ^ {z _ {\max}} \Delta (- t) d t
$$

$$
= \int_ {- z _ {m a x}} ^ {0} \Delta (t) d t
$$

This finishes the proof of Theorem 1.

## B.1. Proof of Theorem 2

Before presenting the proof of Theorem 2, we introduce the following terms:

$$
T _ {n} ^ {x} (x, y) = \frac {\partial W _ {n} (x , y)}{\partial x}
$$

$$
T _ {n} ^ {y} (x, y) = \frac {\partial W _ {n} (x , y)}{\partial y}
$$

$$
T _ {n} ^ {x x} (x, y) = \frac {\partial^ {2} W _ {n} (x , y)}{\partial x ^ {2}}
$$

$$
T _ {n} ^ {x x} (x, y) = \frac {\partial^ {2} W _ {n} (x , y)}{\partial y ^ {2}}
$$

As part of the proof of Theorem 2, we prove and use the following three relationships:

$$
- c _ {o} - c _ {w} \Delta (\mathrm{x}) \leq \mathrm{V} _ {\mathrm{k}} ^ {\prime} (\mathrm{x}) \leq 0 \forall \mathrm{x} \leq \underline {{\mathrm{x}}} _ {\mathrm{k}}
$$

$$
V _ {k} ^ {\prime} (x) = - c _ {o} \forall x \leq - z _ {m a x}
$$

$$
c _ {w} f (x) + \alpha V _ {k} ^ {\prime \prime} (x) \geq 0 \forall x \leq \underline {{x}} _ {k}
$$

The proof is by induction on k. Assume that $\begin{array} { r } { V _ { 0 } ( x ) = - c _ { o } x . } \end{array}$ This implies that any remaining or excess inventory can be salvaged at full price. For k = 1 we have the following:

$$
W _ {1} (x, y) = C (x, y) + \alpha V _ {0} (y) \Delta (x) + \alpha \int_ {x} ^ {\infty} V _ {0} (x + y - u) \delta (u) d u
$$

$$
T _ {1} ^ {\mathrm{y}} (x, y) = c _ {0} (1 - \alpha) - c _ {u} + \left(c _ {u} + c _ {h}\right) \Delta (\mathrm{x} + \mathrm{y}) + \mathfrak {c} _ {\mathrm{w}} \int_ {0} ^ {\mathrm{y}} \Delta (\mathrm{u} + \mathrm{x}) \mathrm{f} (\mathrm{y} - \mathrm{u}) \mathrm{du}
$$

$$
T _ {1} ^ {y y} (x, y) = \left(c _ {u} + c _ {h}\right) \delta (x + y) + c _ {w} \Delta (\mathrm{x}) \mathrm{f(y)} + \mathrm{c} _ {\mathrm{w}} \int_ {0} ^ {\mathrm{y}} \delta (\mathrm{x} + \mathrm{y} - \mathrm{u}) \mathrm{f(u)} \mathrm{du} > 0.
$$

Note that ${ T _ { 1 } } ^ { y } ( x , y ) { \big | } _ { y = 0 } = { T _ { 1 } } ^ { y } ( x , 0 ) = c _ { 0 } ( 1 - \alpha ) - c _ { u } + ( c _ { u } + c _ { h } ) \Delta ( x ) ,$ . Let x 1 be the solution to $T _ { 1 } { } ^ { y } ( x , 0 ) = 0 ,$ , i.e. $x 1 = \Delta ^ { - 1 } ( \phi )$ where, $\begin{array} { r } { \phi = \frac { c _ { u } - c _ { o } ( 1 - \alpha ) } { c _ { u } + c _ { h } } } \end{array}$ This implies the following:

$T _ { 1 } { } ^ { y } ( x , y )$ is a strictly increasing function of x which has a unique zero at $_ { x 1 }$

$T _ { 1 } { } ^ { y } ( x , y ) < 0$ for $x < x 1$ and $T _ { 1 } { } ^ { y } ( x , y ) > 0$ for $x > x 1$

$$
\lim _ {y \to \infty} T _ {1} ^ {y} (x, y) = c _ {0} (1 - \alpha) - c _ {u} + c _ {w} > 0.
$$

Thus, for all $x > x 1$ , it is optimal not to order anything and for $x < x$ 1it is optimal to order $y _ { 1 } ( x ) ,$ , where $y _ { 1 } ( x )$ is the solution to $T _ { 1 } { } ^ { y } ( x , y ) = 0$ We now calculate $V _ { 1 } { ' } ( x )$ as follows. By definition $T _ { n } { } ^ { y } ( x , y _ { 1 } ( x ) ) = 0$ . This implies that $\frac { d T _ { 1 } ^ { y } ( x . y _ { 1 } ( x ) ) } { d x } = 0$

$$
\frac {d T _ {1} ^ {\mathrm{y}} \left(x , y _ {1} (x)\right)}{d x} = 0 = \left(c _ {u} + c _ {h}\right) \delta \left(x + y _ {1} (x)\right) \left(1 + y _ {1} ^ {\prime} (x)\right) + c _ {w} y _ {1} ^ {\prime} (x) \Delta (\mathrm{x}) \mathrm{f} \left(\mathrm{y} _ {1} (\mathrm{x})\right) + \mathrm{c} _ {\mathrm{w}} \int_ {0} ^ {\mathrm{y} _ {1} (\mathrm{x})} \delta \left(\mathrm{x} + \mathrm{y} _ {1} (\mathrm{x}) - \mathrm{u}\right) \mathrm{f} (\mathrm{u}) \mathrm{du} \left(1 + \mathrm{y} _ {1} ^ {\prime} (\mathrm{x})\right)
$$

Solving for $y _ { 1 } ^ { \prime } ( x )$ we get $\begin{array} { r } { y _ { 1 } ^ { ' } ( x ) = - \frac { N } { D } } \end{array}$ where,

$$
N = \left(c _ {u} + c _ {h}\right) \delta \left(x + y _ {1} (x)\right) + c _ {w} \int_ {0} ^ {y _ {1} (x)} \delta \left(x + y _ {1} (x) - u\right) f (u) d u
$$

and

$$
D = N + c _ {w} \Delta (\mathrm{x}) \mathrm{f} \left(\mathrm{y} _ {1} (\mathrm{x})\right)
$$

Notice that $N > 0$ and $D > N .$ . We can now conclude, $\begin{array} { r } { - 1 \le \frac { d y _ { 1 } ( x ) } { d x } \le 0 } \end{array}$ . Further notice that the limit $\operatorname* { l i m } _ { x  \infty } y _ { 1 } ^ { ' } ( x ) = - 1$ because the difference $D - N =$ $c _ { w } \Delta ( x ) f ( y _ { 1 } ( x ) ) = 0 \ \mathrm { a s \ x ^ { . . . } } \mathrm { \infty }$ . This finishes the proof of statements (1)–(4) in Theorem 2 for the $n = 1 { \mathrm { ~ c a s e } }$ . We next prove statements $\left( \mathsf { A } \right) \mathsf { - } ( \mathbf { C } )$ $V _ { 1 } ^ { ' } ( x ) = T _ { 1 } ^ { x } ( x , y _ { 1 } ( x ) ) + T _ { n } ^ { y } ( x , y _ { 1 } ( x ) ) { y } _ { 1 } ^ { ' } ( x ) = T _ { 1 } ^ { x } ( x , y _ { 1 } ( x ) ) ,$

because $T _ { 1 } { } ^ { y } ( x , y _ { 1 } ( x ) ) = 0$ by definition.

$$
V _ {1} ^ {\prime} (x) = c _ {h} \Delta \left(\mathrm{x} + \mathrm{y} _ {1} (\mathrm{x})\right) - \mathrm{c} _ {\mathrm{u}} \left(1 - \Delta \left(\mathrm{x} + \mathrm{y} _ {1} (\mathrm{x})\right)\right) + \mathrm{c} _ {\mathrm{w}} \int_ {\mathrm{o}} ^ {\mathrm{y} _ {1} (\mathrm{x})} \delta (\mathrm{u} + \mathrm{x}) \mathrm{F} \left(\mathrm{y} _ {1} (\mathrm{x}) - \mathrm{u}\right) - \alpha \mathrm{c} _ {\mathrm{o}} (1 - \Delta (\mathrm{x}))
$$

Some of the above terms are similar to what we would see in $T _ { n } { } ^ { y } ( x , y ) | _ { y = y _ { 1 } ( x ) } .$ . Collecting such terms we have the following:

$$
V _ {1} ^ {\prime} (x) = T _ {1} ^ {y} (x, y) \left| _ {y = y _ {1} (x)} - c _ {o} (1 - \alpha \Delta (\mathrm{x})) - \mathrm{c} _ {\mathrm{w}} \Delta (\mathrm{x}) \mathrm{F} (\mathrm{y} _ {1} (\mathrm{x})) \right.
$$

$$
V _ {1} ^ {\prime} (x) = - c _ {o} (1 - \alpha \Delta (\mathrm{x})) - \mathrm{c} _ {\mathrm{w}} \Delta (\mathrm{x}) \mathrm{F} (\mathrm{y} _ {1} (\mathrm{x}))
$$

This implies that $- c _ { o } - c _ { w } \Delta ( x ) \le V _ { 1 } { ' } ( x ) \le 0$ . Also, $\mathrm { f o r } x \le - z _ { m a x }$ we have $\begin{array} { r } { V _ { 1 } { ' } ( x ) = - \ : c _ { o } . } \end{array}$ This proves the statements $\left( \mathsf { A } \right) \ – ( \mathsf { B } )$ . To prove statement (C) we first calculate $V _ { 1 } ^ { \prime \prime } ( x )$ .

$$
V _ {1} ^ {\prime \prime} (x) = \frac {d}{d x} \left(V _ {1} ^ {\prime} (x)\right)
$$

$$
= \frac {d}{d x} \left(- c _ {o} (1 - \alpha \Delta (\mathrm{x})) - \mathrm{c} _ {\mathrm{w}} \Delta (\mathrm{x}) \mathrm{F} \left(\mathrm{y} _ {1} (\mathrm{x})\right)\right)
$$

$$
= c _ {o} \alpha \delta (x) - c _ {w} \delta (x) F (y _ {1} (x)) - c _ {w} \Delta (\mathrm{x}) f (y _ {1} (\mathrm{x})) y _ {1} ^ {\prime} (\mathrm{x})
$$

We can use the expression for $V _ { 1 } { } ^ { \prime \prime } ( x )$ to show $c _ { w } f ( x ) + \alpha V _ { 1 } { } ^ { \prime \prime } ( x ) \geq 0 .$

This finishes the proof of the $k = 1$ case.

Assume that statements 1–4 and $( \mathsf { A } ) \mathsf { - } ( \mathsf { C } )$ are true for $k = 1 , \ldots , n - 1$ . We now show that the statements are true for $k = n .$ Consider the following equation.

$$
\begin{array}{l} W _ {n} (x, y) = C (x, y) + \alpha V _ {n - 1} (y) \Delta (x) + \alpha \int_ {x} ^ {\infty} V _ {n - 1} (x + y - u) \delta (u) d u \\ T _ {n} ^ {y} (x, y) = c _ {0} (1 - \alpha) - c _ {u} + (c _ {u} + c _ {h}) \Delta (x + y) + c _ {w} \int_ {0} ^ {y} \Delta (u + x) f (y - u) d u + \alpha V _ {n - 1} ^ {\prime} (y) \Delta (x) + \alpha \int_ {x} ^ {x + y + z _ {\max}} V _ {n - 1} ^ {\prime} (x + y - u) \delta (u) d u + \alpha c _ {0} \Delta (x + y + z _ {\max}) \\ T _ {n} ^ {y y} (x, y) = (c _ {u} + c _ {h}) \delta (x + y) + \left[ c _ {w} f (y) + \alpha V _ {n - 1} ^ {\prime \prime} (y) \right] \Delta (x) + \int_ {x} ^ {x + y + z _ {\max}} \left[ c _ {w} f (x + y - u) + \alpha V _ {n - 1} ^ {\prime \prime} (x + y - u) \right] \delta (u) d u. \end{array}
$$

This implies that $T _ { n } { } ^ { y y } ( x , y ) \geq 0$ because of statement (C). We now calculate

$$
\lim _ {y \rightarrow \infty} T _ {n} ^ {y} (x, y) = \left(c _ {o} + c _ {h} + c _ {w}\right) + \alpha \lim _ {y \rightarrow \infty} \left[ V _ {n - 1} ^ {\prime} (y) \Delta (\mathrm{x}) + \int_ {\mathrm{x}} ^ {\mathrm{x} + \mathrm{y} + \mathrm{z} _ {\max}} \mathrm{V} _ {\mathrm{n} - 1} ^ {\prime} (\mathrm{x} + \mathrm{y} - \mathrm{u}) \delta (\mathrm{u}) \mathrm{du} \right]
$$

$$
\geq \left(c _ {o} + c _ {h} + c _ {w}\right) - \alpha \lim _ {\mathrm{y} \rightarrow \infty} \left[\left(c _ {0} + c _ {w} \Delta (\mathrm{y})\right) \Delta (\mathrm{x}) + \int_ {\mathrm{x}} ^ {\mathrm{x} + \mathrm{y} + \mathrm{z} _ {\max}} \left(\mathrm{c} _ {0} + \mathrm{c} _ {\mathrm{w}} \Delta (\mathrm{x} + \mathrm{y} - \mathrm{u})\right) \delta (\mathrm{u}) \mathrm{du} \right]
$$

$$
= c _ {h} + (1 - \alpha) (c _ {o} + c _ {w}) \geq 0.
$$

Note that,

$$
\lim _ {y \rightarrow 0} T _ {n} ^ {y} (x, y) = c _ {0} \left(1 - \alpha \left(1 - \Delta \left(x + z _ {\max}\right)\right) - c _ {u} + \left(c _ {u} + c _ {h}\right) \Delta (x) + \alpha V _ {n - 1} ^ {\prime} (0) \Delta (x) + \int_ {x} ^ {x + z _ {\max}} V _ {n - 1} ^ {\prime} (x - u) \delta (u) d u = T _ {n} ^ {y} (x, 0) \right.
$$

Further note that,

$$
\frac {\partial T _ {n} ^ {y} (x , 0)}{\partial x} = \left(c _ {u} + c _ {h}\right) \delta (x) + \alpha \int_ {x} ^ {x + z _ {\max}} V _ {n - 1} ^ {\prime \prime} (x - u) \delta (u) d u \geq 0,
$$

because statement (C) implies that for $x < 0 , V _ { n - 1 } \prime \prime ( x - u ) \geq 0$ . Now, note that

$$
\lim _ {x \to - \infty} T _ {n} ^ {y} (x, 0) = c _ {o} (1 - \alpha) - c _ {u} \leq 0.
$$

We know that $T _ { n } { } ^ { y } ( x , 0 )$ is an increasing function of x that is negative at $x = ~ - \infty$ . This implies two possibilities. $T _ { n } ^ { y } ( x , 0 ) < 0 \forall x$

1. ∃x n $\ni T _ { n } ^ { y } \bigg ( { x n } , 0 \bigg ) = 0$ and $T _ { n } { } ^ { y } ( x , 0 ) > 0$ for x > x n.

In the first case set $x n = \infty$

Putting all the previous arguments together, we get the following:

• For x ≤ x n, $T _ { n } { } ^ { y } ( x , y )$ is a strictly increasing function of y which in strictly negative at y = 0 and strictly positive as $y  \infty$ . This implies that $\exists y _ { n } ( x ) \in$ $[ 0 , \infty )$ such that $T _ { n } { } ^ { y } ( x , y _ { n } ( x ) ) = 0 .$

• For $x > x n , T _ { n } ^ { y } ( x , y )$ is a strictly increasing function of y which in strictly positive at y = 0 and strictly positive as $y  \infty$ . This implies that $\nexists y _ { n } ( x ) \in$ $[ 0 , \infty )$ such that $T _ { n } { } ^ { y } ( x , y _ { n } ( x ) ) = 0 .$ . In this case we say that $y _ { n } ( x ) = 0 .$

We now calculate $V _ { n } ^ { \prime } ( x ) .$ . Notice that $T _ { n } { } ^ { y } ( x , y _ { n } ( x ) ) = 0$ by definition. This implies that $\begin{array} { r } { \frac { d T _ { n } ^ { y } ( x , y _ { 1 } ( x ) ) } { d x } = 0 } \end{array}$

$$
\frac {d T _ {n} ^ {\mathrm{y}} \left(x , y _ {n} (x)\right)}{d x} = 0 = \left(c _ {u} + c _ {h}\right) \delta \left(x + y _ {n} (x)\right) \left(1 + y _ {n} ^ {\prime} (x)\right) + c _ {\mathrm{w}} y _ {n} ^ {\prime} (x) \Delta (\mathrm{x}) \mathrm{f} \left(\mathrm{y} _ {\mathrm{n}} (\mathrm{x})\right) + \mathrm{c} _ {\mathrm{w}} \int_ {0} ^ {\mathrm{y} _ {\mathrm{n}} (\mathrm{x})} \delta \left(\mathrm{x} + \mathrm{y} _ {\mathrm{n}} (\mathrm{x}) - \mathrm{u}\right) \mathrm{f} (\mathrm{u}) \mathrm{du} \left(1 + \mathrm{y} _ {\mathrm{n}} ^ {\prime} (\mathrm{x})\right)
$$

Solving for $y _ { n } ^ { \prime } ( x )$ we get $\begin{array} { r } { y _ { n } ^ { ' } ( x ) = - \frac { N } { D } } \end{array}$ where,

$$
N = \left(c _ {u} + c _ {h}\right) \delta \left(x + y _ {n} (x)\right) + c _ {w} \int_ {0} ^ {y _ {n} (x)} \delta \left(x + y _ {n} (x) - u\right) f (u) d u
$$

and

$$
D = N + c _ {w} \Delta (\mathrm{x}) \mathrm{f} \left(\mathrm{y} _ {\mathrm{n}} (\mathrm{x})\right)
$$

Notice that $N > 0$ and $D > N .$ We can now conclude that $\begin{array} { r } { - 1 \le \frac { d y _ { n } ( x ) } { d x } \le 0 . } \end{array}$ . Further, notice that the limit $\operatorname* { l i m } _ { x  \infty } y _ { n } ^ { ' } ( x ) = - 1$ because the difference $D - N$ $= c _ { w } \Delta ( x ) f ( y _ { n } ( x ) ) = 0 \ \mathrm { a s \ x ^ { . . . } } \infty .$

This finishes the proof of statements (1)–(4) of the theorem.

Now we prove statements (A)-(C).

$$
V _ {n} ^ {\prime} (x) = T _ {n} ^ {x} (x, y _ {n} (x)) + T _ {n} ^ {y} (x, y _ {n} (x)) y _ {n} ^ {\prime} (x) = T _ {n} ^ {x} (x, y _ {n} (x)),
$$

because $T _ { n } { } ^ { y } ( x , y _ { n } ( x ) ) = 0$ by definition.

$$
V _ {n} ^ {\prime} (x) = c _ {h} \Delta \left(\mathrm{x} + \mathrm{y} _ {\mathrm{n}} (\mathrm{x})\right) - \mathrm{c} _ {\mathrm{u}} \left(1 - \Delta \left(\mathrm{x} + \mathrm{y} _ {\mathrm{n}} (\mathrm{x})\right)\right) + \mathrm{c} _ {\mathrm{w}} \int_ {\mathrm{o}} ^ {\mathrm{y} _ {\mathrm{n}} (\mathrm{x})} \delta (\mathrm{u} + \mathrm{x}) \mathrm{F} \left(\mathrm{y} _ {\mathrm{n}} (\mathrm{x}) - \mathrm{u}\right) + \alpha \int_ {\mathrm{x}} ^ {\infty} \mathrm{V} _ {\mathrm{n} - 1} ^ {\prime} (\mathrm{x} + \mathrm{y} - \mathrm{u}) \delta (\mathrm{u}) \mathrm{du}
$$

Some of the above terms are similar to what we would see in $T _ { n } { } ^ { y } ( x , y ) | _ { y = y _ { n } ( x ) } .$ Collecting terms, we have the following:

$$
V _ {n} ^ {\prime} (x) = - c _ {o} - c _ {w} \Delta (\mathrm{x}) \mathrm{F} \left(\mathrm{y} _ {1} (\mathrm{x})\right) - \alpha \mathrm{V} _ {\mathrm{n} - 1} ^ {\prime} \left(\mathrm{y} _ {\mathrm{n}} (\mathrm{x})\right) \Delta (\mathrm{x})
$$

Notice that $- V _ { n - 1 } { ' } ( y _ { n } ( x ) ) \geq 0$ from the induction assumption. This implies that $- c _ { o } - c _ { w } \Delta ( x ) \le V _ { n } { } ^ { \prime } ( x ) \le 0 .$ . Also, for $x \leq - z _ { m a x }$ we have $V _ { n } ^ { \mathbf { \alpha } \prime } ( x ) = \mathbf { \alpha } - \mathbf { \beta }$ $c _ { o } .$ This proves the statements (A)-(B). The proof of statement (C) follows along the same line as that of the k = 1 case and is omitted. This finishes the proof of Theorem 2.

## References

[1] I. Civelek, I. Karaesmen, A. Scheller-Wolf, Blood platelet inventory management with protection levels, Eur. J. Oper. Res. 243 (2015) 826–838.

[2] S. Nahmias, Perishable Inventory Systems (Series Vol. 160), Springer US, Springer Science+Business Media. LLC. 2011.

[3] S. Nahmias, Approximation techniques for several stochastic inventory models, Comput. Oper. Res. 8 (3) (1981) 141–158.

[4] E.A. Silver, Operations research in inventory management: a review and critique, Oper. Res. 29 (4) (1981) 628–645.

[5] S.H.W. Stanger, N. Yates, R. Wilding, S. Cotton, Blood inventory management: hospital best practice, Transfus. Med. Rev. 26 (2) (2012) 153–163.

[6] R.L. Barty, K. Gagliardi, W. Owens, D. Lauson, S. Scheurmann, Y. Liu, G. Wang, M. Pai, N.M. Heddle, A benchmarking program to reduce red blood cell outdating: implementation, evaluation, and a conceptual framework, Transfusion. 55 (2015) 1621–1627.

[7] J.T. Blake, M. Hardy, G. Delage, G. Myhal, D´ej\`a-vu all over again: using simulation to evaluate the impact of shorter shelf life for red blood cells at H´ema-Qu´ebec, Transfusion 53 (2013) 1544–1558.

[8] J.C. Lang, Blood bank inventory control with transshipments and substitutions, in: J.C. Lang (Ed.). Production and Inventory Management with Substitutions. Springer-Verlag. Berlin. Heidelberg. 2010. pp. 205–226.

[9] K. Puranam, D.C. Novak, M.T. Lucas, M. Fung, Managing blood inventory with multiple independent sources of supply. Eur. J. Oper, Res, 259 (2) (2017) 500–511.

[10] S. Nahmias, Perishable inventory theory: a review, Oper, Res, 30 (4) (1982 680–708.

[11] F. Raafat, Survey of literature on continuously deteriorating inventory models, J. Oper. Res, Soc, 42 (1) (1991) 27–37.

[12] I.z. Karaesmen, A. Scheller-Wolf, B. Deniz, Managing perishable and aging inventories: review and future research directions, in: K.G. Kempf, P. Keskinocak R. Uzsoy (Eds.), Planning production and inventories in the extended enterprise, Springer, Boston, MA, 2011, pp. 393–436.

[13] J. Beli¨en, H. Forc´e, Supply chain management of blood products: a literature review, Eur. J. Oper. Res. 217 (1) (2012) 1–16.

[14] M. Bakker, J. Riezebos, R.H. Teunter, Review of inventory systems with deterioration since 2001, Eur, J. Oper, Res, 221 (2) (2012) 275–284.

[15] L. Janssen, T. Claus, J. Sauer, Literature review of deteriorating inventory model by kev topics from 2012 to 2015, Int. J. Prod. Econ. 182 (2016) 86–112.

[16] G.P. Prastacos, Blood inventory management: an overview of theory and practice,

[17] W.P. Pierskalla, Supply chain Management of Blood Banks, in: M. Brandeau, E. Sainfort, W. Pierskalla (Eds.). Operations Research and Health Care: A Handbook of Methods and Applications, (Series Volume 70) vol. 2004, Springer US, Springer Sciences+Business Media New York 2004, pp. 103–145

[18] G.JJ. Van Zyl. Inventory Control for Perishable Commodities. Publisher not identified, 1964.

[19] S. Nahmias, W.P. Pierskalla, Optimal ordering policies for a product that perishes in two periods subject to stochastic demand, Naval Res. Logistics Quart. 20 (2) (1973) 207–229.

[20] B.E. Fries, Optimal ordering policy for a perishable commodity with fixed lifetime, Oper. Res. 23 (1) (1975) 46–61.

[21] S. Nahmias, Optimal ordering policies for perishable inventory – ii, Oper. Res. 23 (4) (1975) 735–749.

[22] S. Nahmias, A comparison of alternative approximations for ordering perishable

[23] S. Nahmias, Myopic approximations for the perishable inventory problem, Manag. Sc. 22 (9) (1976) 1002–1008.

[24] S. Nahmias, Comparison between two dynamic perishable inventory models, Oper. Res, 25 (1) (1977) 168–172

[25] S. Nahmias, Higher-order approximations for the perishable-inventory problem, Oper. Res. 25 (4) (1977) 630–640.

[26] M.A. Cohen, Analysis of single critical number ordering policies for perishable inventories, Oper. Res. 24 (4) (1976) 726–741.

[27] D. Chazan, S. Gal, A Markovian model for a perishable product inventory, Manag. Sc. 23 (5) (1977) 512–521

[28] P. Nandakumar, T.E. Morton, Near myopic heuristics for the fixed-life perishability problem, Manag, Sc, 39 (12) (1993) 490–1498.

[29] R. Haijema, S. Minner, Stock-level dependent ordering of perishables: a comparison of hybrid base-stock and constant order policies, Int. J. Prod. Econ. 181 (2016) 215–225.

[30] E. Brodheim, C. Derman, G. Prastacos, On the evaluation of a class of inventory policies for perishable products such as blood, Manag. Sc. 21 (11) (1975) 1320-1325.

[31] R.A. Broekmeulen, K.H. Van Donselaar, A heuristic to manage perishable inventory with batch ordering, positive lead-times, and time-varying demand, Comput. Oper. Res, 36 (11) (2009) 3013–3018

[32] Q. Duan, T.W. Liao, A new age-based replenishment policy for supply chain inventory optimization of highly perishable products, Int. J. Prod. Econ. 145 (2) (2013) 658–671.

[33] W.P. Pierskalla, C.D. Roach, Optimal issuing policies for perishable inventory, Manag, Sc. 18 (11) (1972) 603–614.

[34] M.A. Cohen, G.P. Prastacos, Critical number ordering policy for LIFO perishable inventory systems, Comput. Oper. Res. 8 (3) (1981) 185–195.

[35] R. Haijema, S. Minner, Improved ordering of perishables: the value of stock-age information, Int, J Prod. Econ, 209 (2019) 316–324

[36] B. Deniz, I. Karaesmen, A. Scheller-Wolf, Managing perishables with substitution: inventory issuance and replenishment heuristics, Manuf. Serv. Oper. Manag. 12 (2) (2010) 319–329.

[37] R. Haijema, Optimal ordering, issuance and disposal policies for inventory management of Perishable products. Int. J. Prod. Econ, 157 (2014) 158–169.

[38] C. Paterson, G. Kiesmüller, R. Teunter, K. Glazebrook, Inventory models with lateral transshipments: a review. Eur, J. Oper, Res, 210 (2) (2011) 125–136

[39] J.B. Jennings. Blood Bank inventory control, Manag, Sc. 19 (6) (1973) 637–645.

[40] K.E. Kendall. S.M. Lee, Formulating blood rotation policies with multiple

[41] G.P. Prastacos, E. Brodheim, A decision support system for regional blood management, Manag, Sc. 26 (5) (1980) 451–463.

[42] P.J. Gregor, R.N. Forthofer, A.S. Kapadia, An evaluation of inventory and transportation policies of a regional blood distribution system, Eur. J. Oper. Res. 10 (1) (1982) 106–113.

[43] L. Denesiuk, T. Richardson, S. Nahirniak, G. Clarke, Implementation of a redistribution system for near-outdate red blood cell units, Arch. Pathol. Lab. Med. 130 (8) (2006) 1178–1183

[44] K. Puranam, D.C. Novak, M. Lucas, Extending the newsvendor model to account for uncontrolled inventory transfers. Ann. Oper. Res. (2015) 1–14.

[45] G. Tagaras, D. Vlachos, A periodic review inventory system with emergency replenishments, Manag. Sc. 47 (3) (2001) 415–429.

[46] D. Zhou, L.C. Leung, W.P. Pierskalla, Inventory Management of Platelets in hospitals: optimal inventory policy for perishable products with regular and optional expedited replenishments, Manuf. Serv. Oper. Manag. 13 (4) (2011) 420–438.

[47] A. Federgruen, G. Prastacos, P.H. Zipkin, An allocation and distribution model for perishable products, Oper. Res. 34 (1) (1986) 75–82.

[49] L.C. Coelho, G. Laporte, Optimal joint replenishment, delivery and inventory management policies for perishable products, Comput. Oper. Res. 47 (2014) 42–52.

[48] S. Nahmias, On ordering perishable inventory when both demand and lifetime are random, Manag, Sc. 24 (1) (1977) 82–90.

[50] S.H.W. Stanger, N. Yates, R. Wilding, S. Cotton, Blood inventory management: hospital best practice, Transfus. Med. Rev. 26 (2) (2012) 153–163

[51] C.S. Jones, S. Tuzel, S, inventory investment and the cost of capital, J. Financ. Econ. 107 (3) (2013) 557–579.

[52] H. Richardson, Control your costs then cut them, Transp. Distrib. 36 (12) (1995) 94–96.

[53] C. McIntosh, F. Dexter, R.H. Epstein, The impact of service-specific staffing, case scheduling, turnovers, and first-case starts on anesthesia group and operating room productivity: a tutorial using data from an Australian hospital, Anesth. Analg. 103 (6) (2006) 1499–1516.

[54] F. Dexter, A. Macario, D.S. Cowen, Staffing and case scheduling for anesthesia in geographically dispersed locations outside of operating rooms, Curr. Opin. Anesthesiol. 19 (4) (2006) 453–458.

[55] M.H. Tsai, T.T. Huynh, M.W. Breidenstein, S.E. O’Donnell, J.M. Ehrenfeld, R. D. Urman, A system-wide approach to physician efficiency and utilization rates for non-operating room anesthesia sites, J. Med. Syst. 41 (7) (2017) 112.

[56] P. Ghandforoush, T.K. Sen, A DSS to manage platelet production supply chain for regional blood centers, Decis. Support. Syst. 50 (2010) 32–42.
