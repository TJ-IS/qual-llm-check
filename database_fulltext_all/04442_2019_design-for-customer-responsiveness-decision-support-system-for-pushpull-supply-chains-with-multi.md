---
otero_id: 4442
otero_key: "DRARXFRX"
title: "Design for customer responsiveness: Decision support system for push–pull supply chains with multiple demand fulfillment points"
authors: "John W. Fowler; Seung-Hwan Kim; Dan L. Shunk"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113071"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design for customer responsiveness: Decision support system for push–pull supply chains with multiple demand fulfillment points

![](/api/attachments/DRARXFRX/fulltext/images/8b2391dd24fe59ed3ad0a11691cb8825c11993d47c9622f8bbecba879fc30966.jpg)

John W. Fowler<sup>a</sup>, Seung-Hwan Kim<sup>b,⁎</sup>, Dan L. Shunk<sup>c</sup>

<sup>a</sup> Department of Supply Chain Management, W. P. Carey School of Business, Arizona State University, Tempe, AZ 85287-5906, USA

<sup>b</sup> Department of Business Administration, Ajou University, Suwon 16499, South Korea

<sup>c</sup> School of Computing, Informatics, and Decision Systems Engineering, Arizona State University, Tempe, AZ 85287-5906, USA

## A R T I C L E I N F O

Keywords: Decision support system Supply chain design Customer Lead time management Push–pull control

## A B S T R A C T

A push–pull supply chain is a hybrid of “push” and “pull” supply chains where semi-finished products are produced by forecasts and “pushed” to a stock point, then are “pulled” by actual customer orders and go through remaining processes to be delivered. In order to design an efective push–pull supply chain, there are two critical issues in the decision making process: how to support decision makers to identify feasible locations for demand fulfillment points based on the product, process, and organizational form of a given enterprise, and how to support decision makers to improve the customer lead time management capability of a push–pull supply chain. In this study, we present a decision support system for designing a push–pull supply chain that 1) incorporates the product, process, and organizational form of a given enterprise; 2) leverages a new hybrid push–pull contro model, which enhances the customer lead time management capability; and 3) provides a decision support model that supports decision makers for performing scenario-based analysis in designing a push–pull supply chain. The numerical analysis exhibits how the proposed system can be implemented in the context of a semiconductor supply chain, and subsequently shows that our control model results in substantial improvement of customer lead time management capability over conventional push–pull supply chain designs without a significant inventory cost increase. Also, some experimental results are provided to support decision makers on how to make the transition from the conventional design to the proposed one.

## 1. Introduction

Traditionally, the design of a supply chain was categorized as either “push” or “pull.” While a “push supply chain” plans for products to be produced based on forecasts and to be stocked as finished goods inventories at the downstream end of a supply chain, a “pull supply chain” authorizes products to be produced only based on the actual customer orders with no finished product inventories. In terms of the trade-of between inventory cost and service cost, which is the key performance measure of a supply chain, a push supply chain is geared too much toward service cost, while a pull supply chain is aimed too much for inventory cost. For this reason, after going through a number of successes and failures, a hybrid strategy called the “push–pull supply chain” has emerged as a new supply chain paradigm [22]. A push–pull supply chain calls for making semi-finished products by push production mode and storing them in a stock location (“demand fulfillment point” in this paper) in the middle of a supply chain. Those semi-finished products are pulled by actual orders and go through the remaining processes to be delivered to the customers. It seeks the right balance between inventory cost and service cost, with the flexibility for customization. Recently, it has become a key process and implementation enabler for MC (mass customization) based supply chains [9,15,26].

Despite the growing importance, there have been only a few research works on supporting the decision-making process of the push–- pull supply chain design. Pagh and Cooper [25] presented four supply chain design strategies by applying “speculation” (similar to “push”) and “postponement” (similar to “pull”) to the manufacturing side and the logistics side of a supply chain. They suggested a decision support framework on how to choose the best fit among those four strategies based on the product, market, and manufacturing/logistics factors. Olhager [24] ofered four diferent push–pull supply chain design strategies by placing the demand fulfillment point in diferent locations. A qualitative decision model for selecting the right strategy was given depending on the product lead time to delivery lead time ratio and the relative demand volatility. Kim [16] proposed a conceptual decision framework for determining the demand fulfillment location in the context of a semiconductor supply chain, which was extended in Kim and Kim [17] by incorporating the stochastic settings of demand and lead times into the framework based on a discrete-event simulation study. The important finding among these studies was that they all yielded only qualitative and conceptual frameworks. It gave us the research motivation for developing an analytical and practical decision support system.

There are important challenges in improving the design process of a push–pull supply chain. First, since the location must be determined based on the product type, manufacturing process, and organizational form of a given enterprise [8,10,16,17], it is imperative to help the de cision makers identify feasible locations for demand fulfillment points in a given supply chain. For instance, even though the “die bank” (the stock location between the front end and the back end of a semiconductor supply chain) is the standard demand fulfillment point location for most semiconductor companies [2,21], several types of customized products must have another stock point prior to the die bank as their demand fulfillment point due to their unique customization processes. Also, regarding the organizational form of a company, OEM (Original Equipment Manufacturer) type organizations may not have a die bank in their supply chain at all because they perform only a certain portion of the entire processing stages in a semiconductor supply chain [16]. Second, there is an urgent need to provide the decision makers with a solution to enhance the customer lead time management capability of a push–pull supply chain. One of the key lingering questions surrounding a push–pull supply chain has been how capable it is in terms of sustaining acceptable responsiveness in managing customer lead times [2,18,34]. In order to emphasize the importance of managing customer lead times, Brown et al. [2] even argue that it is just not wise to use a push–pull supply chain when the proportion of customers requiring short lead times is large.

In this study, we present a decision support system for designing a push–pull supply chain that addresses the aforementioned challenges by extending the hybrid push–pull supply chain model first introduced in Kim et al. [18]. The main objectives of Kim et al. [18] were to in troduce the theoretical foundation and to show the improvement by the new model, which redesigned the material and information flows of a push–pull supply chain by incorporating multiple demand fulfillment points. We extend Kim et al. [18] in the following directions: First, a numerical procedure called “feasible candidate generation procedure” has been developed to identify feasible locations for demand fulfillment points in a push–pull supply chain based on the given product, process, and organizational form information. The model in Kim et al. [18] assumed all the available stock points were feasible for demand fulfill ment locations. Also, this procedure has enabled us to generate custo mized supply chain design alternatives with respect to the inputs selected by the decision makers, whereas Kim et al. [18] provided the predetermined design alternatives in the numerical study. Second, the production lead time in each stage is mathematically modeled as a function of the capacity limit and the input demand, whereas Kim et al. [18] hypothesized unlimited capacities for all production stages and used stationary probability distributions. This extension has allowed us to consider the congestion of customer orders under limited production capacity, which is one of the most significant elements in customer lead time management. In addition. we have incorporated the transportation times between stages into the lead time function, which were omitted in Kim et al. [18]. As a result, these improvements have made more accurate lead time related analyses possible since the capacities of production stages and transportation times play critical roles in fulfilling customer lead times. Lastly, we have performed additional analyses on how to make an efective transition from the conventional push–pull design to the proposed design, which was not investigated in Kim et al. [18]. This is an important managerial issue in practice because com panies may be able to add only a limited number of demand fulfillment points to their existing push–pull supply chain due to 1) their unique technical/geographical/logistical/resource constraints and 2) the possible concern of management that it can lead to a significant increase in inventory cost. We show that an efective strategy to add more fulfill ment points to a conventional push–pull supply chain is to start adding one from the closest inventory location to customers (i.e., finished goods stock point), then add more points one by one toward the up stream end of a supply chain. Also, we illustrate that the inventory cost increase due to additional fulfillment points is not significant and this increase is compensated by a substantial reduction in service cost.

The remainder of this paper is organized as follows: In the next section, the main components of the proposed decision support systems are explained. In Section 3, we present the feasible candidate generation procedure, which identifies feasible locations for demand fulfillment points. It is followed by Section 4, where the details of the control model are described. In Section 5, we demonstrate how the proposed decision support system can be implemented by using the decision support model in the context of a semiconductor supply chain. Section 6 concludes the paper with managerial implications and future research.

## 2. Main components of the decision support system

The proposed decision support system has three major components: 1) Feasible Candidate Generation Procedure which finds the feasible lo cations of demand fulfillment points for a given choice of product, process, and organizational form; 2) Control model for a Push–Pull Supply Chain with Multiple Demand Fulfillment Points, where customer orders for a product are fulfilled simultaneously at multiple semi-finished/finished inventory stock locations based on order lead time requirements; 3) Decision Support Model that supports decision makers for performing scenario-based analysis in designing an efective push–pull supply chain. Fig. 1 presents the overall framework of the proposed decision support system.

We initially determine two categories of supply chain inputs: 1) supply chain design inputs and 2) scenario generation inputs. The supply chain design inputs are product types, production stages, and organizational forms considered in a given supply chain. The scenario generation inputs include model parameters related to production/ transportation, customer related factors such as the penalty rate for not fulfilling the order lead time, the mean and standard deviation values of demand, and the discount rate for customers with infeasible lead time requirements in the lead time negotiation process. Next, the feasible candidate generation procedure identifies candidate locations for the given product types, production stages, and organizational forms. Then, those candidate locations are used to create mathematically formulated supply chain design alternatives by the control model. Lastly, the decision support model makes optimization runs under various input scenarios to support managerial decision making in the supply chain planning/design process.

## 3. Feasible candidate generation procedure

This procedure generates the candidate demand fulfillment points once the inputs for the product, process, and organizational form of a given enterprise are given. In Section 5, we show how this procedure can be used in designing a semiconductor supply chain.

Suppose there is a standard set of process stages in a supply chain with several options for its strategic organizational forms. For example, some products are to be produced 100% internally, whereas some production stages are to be outsourced for several products. Let $I = \{ i | i = 1 , 2 , \ldots , L \}$ be a set of the organizational form alternatives considered, $J = \{ j | j = 1 , 2 , \dots , M \}$ be a set of the products, and $K = \{ k | k = 0 , 1 , 2 , \ldots , N \}$ be a set of all the production stages in a supply chain where $k = 0$ represents the case when make-to-order production with 100% customization is employed. The feasible candidate generation procedure produces $Q _ { i j } ,$ the set of feasible stock loca tions for the fulfillment points, and ${ Q _ { i j } } ^ { * }$ , the resulting subsets of $Q _ { i j }$ that become the supply chain design alternatives for organizational form i and product j are:

![](/api/attachments/DRARXFRX/fulltext/images/6ddf8b06d0ad030a58ff4cd2c146ccb4d30b1435b1aa5209b0a49a789e43c571.jpg)  
Fig. 1. The proposed decision support system for designing a push-pull supply chain.

$$
Q _ {i j} = \left\{q _ {k} \mid \left[ \left(k \in A _ {i}\right) \cap \left(k \in B _ {j} ^ {c}\right) \right] \cup \left[ k = M i n _ {k \in A _ {i}} (k - 1) \right] \right\}
$$

$$
Q _ {i j} ^ {*} := \boldsymbol {P} (Q _ {i j}) \backslash \{\varnothing \}
$$

where $q _ { k }$ is the stock point after process stage $k , A _ { i }$ is the set of production stages included in organizational form i, B is the set of custo mization production stages for product $j , B _ { j } ^ { c }$ is the complement set of $B _ { j } ,$ and P(S) is the power set of S.

Kim [16] defines the standardization-customization boundary (SCB) of a product as the boundary between standardization processes and customization processes and states that the push–pull boundary (fulfillment point in our study) can only be placed within standardization processes. Therefore, if k ∈ B in our procedure, the corresponding stock point, $q _ { k } ,$ cannot be selected as a candidate location. The stepwise description of the procedure is presented below.

1. Define $I , J ,$ and K for a given supply chain.

2. Identify $A _ { i }$ and $B _ { j }$ based on the defined $I , J ,$ and K.

3. Find the set of feasible stock locations for the push–pull boundary and fulfillment points, $Q _ { i j } ,$ by identifying the production stages that are included in organizational form i and are not included among the customization stages for product j.

4. Add the immediate predecessor stock point of the first production stage in organizational form i, to $Q _ { i j } .$ The reasoning for this step is that we may have an input bufer for incoming semi-finished pro ducts before the first production stage of an organizational form and we may use it as a candidate location. Once it is completed, the resulting $Q _ { i j }$ must be reviewed by management to add or remove certain points based on the unique technical/geographical/logistic constraints of the organization.

5. The set of all subsets of $Q _ { i j } ,$ with the exclusion of the empty set, becomes ${ Q _ { i j } } ^ { * } { } ,$ , the set of candidate locations of the push–pull boundary and fulfillment points for organizational form i and product j.

In this procedure, we assume that the production stages for an organizational form cannot be selected in a disconnected manner; an organizational form is assumed to be a group of consecutive production stages. For example, if there are 4 production stages for a given supply chain and only production stages 2 and 4 are to be performed internally for an organizational form, it means you outsource the first stage, wait, receive the semi-finished products and process them in the second stage, send them to another company, wait, then receive them and process them again to send the finished products to customers. This type of back and forth movement between the main entity and the entities that perform the outsourced operations may cause a significant increase in lead time and also pose a risk of not receiving the products on time from one of the outsourcing companies. This is not in line with the key pursuing attribute of this study—responsiveness to customer lead time requirements.

To demonstrate how the procedure works, a simple illustrative example is given below. Let's assume that there is a supply chain with 4 main production stages. Fig. 2 shows the supply chain production stage and stock points.

If a management considers a business model where the production stage 1 (k = 1) is outsourced, and there are two products, with customization processes being $\mathtt { k } = 3 \& \ 4$ for product 1 and k = 4 for product 2, the candidate locations can be generated by following the procedure as below:

$$
\begin{array}{l} 1. I = \{i | i = 1 \}, J = \{j | j = 1, 2 \}, K = \{k | k = 0, 1, 2, 3, 4 \} \\ 2. A _ {1} = \{2, 3, 4 \}, B _ {1} = \{3, 4 \}, B _ {2} = \{4 \} \\ 3. Q _ {1 1} = \{q _ {2} \}, Q _ {1 2} = \{q _ {2}, q _ {3} \} \\ 4. Q _ {1 1} = \{q _ {2}, q _ {1} \}, Q _ {1 2} = \{q _ {2}, q _ {3}, q _ {1} \}, \text {assuming no more constraints.} \\ 5. Q _ {1 1} ^ {*} = \{(q _ {1}), (q _ {2}), (q _ {1}, q _ {2}) \}, Q _ {1 2} ^ {*} = \{(q _ {1}), (q _ {2}), (q _ {3}), (q _ {1}, q _ {2}), (q _ {1}, q _ {3}), (q _ {2}, q _ {3}), (q _ {1}, q _ {2}, q _ {3}) \} \end{array}
$$

As a result, there are three supply chain design alternatives for product 1 and seven alternatives for product 2 based on the given business model. Note that our strategy also covers conventional supply chain designs in the candidates since it is possible that the conventional ones are better under certain input scenarios. For instance, in the case of product 2, the first three are conventional push–pull designs with one push–pull boundary and no additional fulfillment points. The remaining four alternatives have the push–pull boundary at the first point with the successor points being additional fulfillment points.

Once the set of candidate locations for fulfillment points are finalized, the candidates become the inputs to the control model for gen erating mathematically formulated supply chain design alternatives. The control model is presented in the subsequent section.

## 4. Control mode

## 4.1. Mechanism of control model

The key diference between our control model and the conventional push–pull control is the order assignment process where customer orders for even one product can be assigned to diferent fulfillment points simultaneously based on their lead time requirements, in order to maximize the service level (There are some practices in industries where customer orders are fulfilled at diferent fulfillment locations based on the product, i.e., each product has one “predetermined” fulfillment location). The critical challenge of our control model is how to model the complicated chain reactions of replenishment orders that simultaneously occur at multiple fulfillment points, which is described in Section 3.

Consider a supply chain for organizational form i and product j. Let $\pmb { Q } \in { Q _ { i j } } ^ { * }$ as the set of feasible locations for a supply chain design alternative and $F _ { k }$ as the fulfillment point at $k \in Q , k = 1 , 2 , . . . , n \textrm { - } 1 ,$ , n. Fig. 3 shows the control mechanism. Push production is employed from the first production stage to the first fulfillment point, $F _ { 1 } ,$ where semifinished products are stored. After $F _ { 1 } ,$ pull production is triggered by the actual customer orders assigned to each $F _ { k } .$ . Therefore, $F _ { 1 }$ becomes the push–pull boundary of the given supply chain. Each order triggers each fulfillment point to initiate replenishment orders to the preceding fulfillment point every review period. This process continues up to $F _ { 1 }$

At each review period, an incoming customer order is assigned to the most appropriate fulfillment point based on its customer lead time requirement (CLR) and the expected remaining lead time from $F _ { k } .$ The expected remaining lead time from $F _ { k }$ is an estimate of the time from the moment a semi-finished product at $F _ { k }$ is picked up by a customer order to the moment it is finished and ready for the customer pick-up/ delivery. The expected remaining lead time from $F _ { k }$ is defined as $t _ { k } ( \alpha ) ,$ where t (α) is determined by ${ \mathfrak { a } } ,$ which is a percentile value of the convolution of all remaining stage's lead time distributions. For example, if $\mathrm { C L R } \ < \ t _ { n - 1 } ( \alpha )$ , the order is to be fulfilled at $F _ { n } ,$ if $t _ { n - 1 } ( \alpha ) < \mathrm { C L R } < t _ { n - 2 } ( \alpha )$ , it will be fulfilled at $F _ { n - 1 }$ . In Fig. 3, for instance, while orders with long CLRs can be fulfilled at $F _ { 1 } ,$ orders with very short CLRs must be fulfilled from $F _ { n } .$ As a result, this process can improve the on-time delivery rate since orders are assigned to fulfillment points with higher probabilities of meeting their CLRs.

α is a decision variable that controls the order assignment process based on the trade-of between inventory costs and service costs. When α approaches 0, $t _ { k } ( \alpha )$ values decrease and more orders will be pushed back toward the beginning of a supply chain, which means lower total inventory value in the supply chain. When α approaches 1, the value of t (α) increases and more orders will be fulfilled at locations close to the end of a supply chain. It means higher total inventory value but also higher responsiveness and service level. Therefore, the decision maker needs to choose the right value of α under given market/internal con ditions.

In the next section, we explain the structure of the control model where the subsets in $Q _ { i j } { } ^ { * }$ become the inputs for generating supply chain design alternatives.

## 4.2. Objective function

The objective of the control model is to find the optimal value of α and the fill rates of all fulfillment points, in order to minimize the supply chain total cost. For each subset of ${ Q _ { i j } } ^ { * }$ for a given product i, the objective function can be presented as follows:

<table><tr><td></td><td>k=1</td><td>k=2</td><td>k=3</td><td>k=4</td></tr><tr><td>q0</td><td>q1</td><td>q2</td><td>q3</td><td>q4</td></tr></table>

![](/api/attachments/DRARXFRX/fulltext/images/24cbfc8be58ca3b06fdbb526dea333097d496a440770c8c7b408076839c54210.jpg)  
Fig. 3. Mechanism of push-pull control with multiple fulfillment points (Modified from Kim et al. [18])

$$
\begin{array}{l} M i n _ {\alpha , R _ {k} | \forall k} \\ = h \sum_ {k = 1} ^ {n} (v _ {k}) E [ \varphi_ {k} ] + (b) (v _ {n}) \sum_ {k = 1} ^ {n} (p _ {k}) E [ \lambda ] [ 1 - E [ \vartheta_ {k} ] ] + X ^ {f} \\ (c) (v _ {n}) (p _ {n}) E [ \lambda ] F ^ {c l r} [ t _ {n} (\alpha) ] \end{array}\tag{1}
$$

where

$k = 1 , 2 , . . . , n { - 1 } , n ( k = 1$ is the first fulfillment point, $k = n$ is the closest fulfillment point to the end of supply chain).

α:Percentile value of the convolution of all the remaining stage's lead time distributions from a fulfillment point, decision variable

$R _ { k }$ : Fill rate of fulfillment point k $( F _ { k } ) _ { i }$ decision variable

E[φ ]:Expected inventory level at $F _ { k } ,$ , a function of α and the fill rates of all preceding fulfillment points

$E [ \vartheta _ { k } ]$ : Expected service level at $F _ { k , \mathbf { a } }$ function of α and the fill rates of all preceding fulfillment points

$X ^ { f } { : }$ Indicator variable, 1 if the last fulfillment point does not have finished product inventory, 0 otherwise

$F ^ { c l r } [ t _ { n } ( \alpha ) ]$ :Probability that an incoming order has a shorter CLR than the expected lead time from the last fulfillment point, where $F ^ { c l r } ( )$ is the cumulative probability distribution of CLR

h: Inventory holding cost rate

$\nu _ { k } \mathrm { : }$ Unit inventory value at fulfillment point k

b: Penalty rate for tardiness (failing on-time delivery)

$p _ { k } \dot { \cdot }$ : Proportion of total demand assigned to $F _ { k }$

E[λ] : Total demand per review time

c: Discount rate for lead time negotiation discount cost

The first term in (1) is the total expected inventory holding cost per time unit. Unit inventory holding cost is non-linear since $\nu _ { k }$ is higher as inventories are placed further down in the supply chain. The second term makes up the total expected tardiness cost per time unit. Unit tar diness cost is linear regardless of the fulfillment location because tar diness cost is defined as a percentage of $\nu _ { n } .$ The last term is the total expected lead time negotiation discount cost when the last fulfillment point does not have finished product inventory. It estimates the sales efort needed, in the form of a discount based on certain percentages of $\nu _ { n } ,$ to attract customers who have shorter CLR than $t _ { n } ( \alpha )$ , the expected lead time at the last fulfillment point. If we denote ω as the random variable that represents CLR and $\boldsymbol { F } ^ { c l r } ( )$ as the cumulative probability distribution of $\mathrm { C L R } ,$ then the probability that an incoming order has a shorter CLR than $t _ { n } ( \alpha )$ is obtained by $P [ \omega < t _ { n } ( \alpha ) ] = F ^ { c l r } [ t _ { n } ( \alpha ) ]$

Next, $E [ \varphi _ { k } ] _ { : }$ , the expected inventory level at fulfillment point $k ,$ can be presented as the following:

$$
E [ \varphi_ {k} ] = [ \{1 / 2 \sqrt {(2 / \pi)} \} l n \{R _ {k} / (1 - R _ {k}) \} ] \sqrt {V a r [ D _ {k} ^ {r l t} ]} + E [ \overline {{D _ {k}}} ] / 2
$$

where

$V a r [ D _ { k } ^ { ~ r l t } ]$ : Variance of replenishment lead time (RLT) demand of fulfillment point k

$\overline { { D _ { k } } } :$ : Efective demand at fulfillment point k. $\overline { { D _ { k } } }$ is the sum of assigned demand at fulfillment point k and the replenishment orders from all the successive fulfillment points.

E[φ ] is a function of α and the fill rates of all preceding fulfillment points. Once the values of the fill rates of all preceding fulfillment points and α are selected simultaneously by the search algorithm, the recursive chain reaction starts from $F _ { 1 } .$ . The RLT of $F _ { 1 }$ depends only on the expected value and the variance of the lead time between fulfillment point 1 and the beginning of the supply chain (which are obtained from (6) and $( 7 )$ in Section 4.3), and, the fill rate of $F _ { 1 } \ ( R _ { 1 } ) _ { : } $ , which is selected by the search algorithm. Then the expected value and variance of RLT at $F _ { \mathrm { 1 } } \mathrm { a r e }$ computed, which in turn enables the computation of expected waiting time at $F _ { 1 }$ for incoming replenishment orders. Based on these results, $E [ \varphi _ { 1 } ]$ is computed. From the next fulfillment point $\left( F _ { 2 } \right)$ until the last one (F ), each fulfillment point $F _ { k }$ needs the expected waiting time at the previous point, ${ \mathfrak { a } } ,$ and the fill rate $R _ { k }$ to compute the expected value and variance of RLT demand. Then E[φ ] can be computed. Therefore, we can see that $E [ \varphi _ { k } ]$ is a function of α and the fill rates of all preceding fulfillment points. Please refer to Kim et al. [18] for the details of the expected inventory level at fulfillment point k.

The expected service level at fulfillment point $k ,$ E[ϑ ], is the probability that the customer orders assigned to this point are fulfilled within $t _ { k } ( \alpha )$ , the expected remaining lead time from fulfillment point k. The expected service level is the multiplication of $R _ { k }$ and the probability that the sum of remaining processing time at $F _ { k }$ is less than $t _ { k } ( \alpha )$ when the demand is fulfilled from the on-hand inventory. When the demand is backordered, it is the multiplication of $( 1 - R _ { k } )$ and the probability that the sum of remaining processing time plus the waiting time is less than $t _ { k } ( \alpha ) .$ . If $F _ { n } ,$ the last fulfillment point, is a fulfillment point with finished products, then the expected service level becomes $R _ { n } ,$ the fill rate of $F _ { n } .$ . The expected service level at fulfillment point k can be expressed as follows:

(a) When $1 \le \mathbf { k } \le \mathbf { n }$ and $F _ { n } \ell$ does not have finished product inventories:

$$
\begin{array}{l} E \left[ \vartheta_ {k} \right] \\ = R _ {k} P \left[ \sum_ {j = k + 1} ^ {n} T _ {j} ^ {l t} \leq t _ {j} (\alpha) \right] + (1 - R _ {k}) P \left[ \left\{\sum_ {j = k + 1} ^ {n} T _ {j} ^ {l t} + E \left[ T _ {k - 1} ^ {w t} \mid U _ {k - 1} \right. \right. \right. \\ = 1 ] \Bigg \} \leq t _ {k} (\alpha) \Bigg ] \end{array}
$$

(b) When ${ \bf k } = { \bf n }$ and $F _ { n }$ has finished product inventories:

$$
E \left[ \vartheta_ {k} \right] = R _ {k}
$$

where

$T _ { j } ^ { l t . }$ : lead time between fulfillment point fulfillment point j and $j \ – l$ t (α): expected remaining lead time from fulfillment point k $\dot { T } _ { k } ^ { w t } \dot { : }$ waiting time at fulfillment point k $U _ { k } \colon \mathbf { \theta }$ 1 if there is a stock-out at fulfillment point k, 0 otherwise

The derivation of $T _ { j } ^ { \mathit { l t } }$ <sup>t</sup>, lead time between fulfillment point fulfillment point $j$ and $j \mathrm { - } 1$ , is presented in Section 4.3. For the details of E $[ T _ { k - 1 } { } ^ { w t } | U _ { k - 1 } = 1 ]$ , the expected waiting time at the previous stage due to a stock-out, please refer to Kim et al. [18].

In evaluating (1), the complicated chain reactions of replenishment orders that occur at multiple fulfillment points force the computation procedure of E[φ ] and $E [ \vartheta _ { k } ]$ to find all the optimal fill rate values simultaneously, which prevents finding closed form solutions using conventional mathematical programming techniques. Also, the scenarios used in the decision support model represent a stochastic context, which makes the use of a mathematical programming approach dificult. To surmount this challenge, we turn to metaheuristics as our solution methodology. Most related papers with similar objective function structure as ours, such as Lee and Billington [20], Cochran and Kim [3], and Corry and Kozan [5], find the optimal solutions by metaheuristics or other heuristic algorithms. We select simulated annealing (SA) in our research since it is more robust to various parameter settings and external factors than other metaheuristics [13,28,31,33], which is a key requirement for the diverse scenario analysis of the decision support model in our study.

In the next section, the lead time between two adjacent fulfillment points with limited capacity, which is the most important element of the model, is derived.

## 4.3. Lead time between adjacent fulfillment points

We define the lead time between two adjacent fulfillment points as the sum of the production lead time and the transportation time. This is the most critical element of the control model since lead time man agement capability is the main focus of this paper.

Let $T _ { k } ^ { p l t }$ be the production lead time of production stage k. $T _ { k } ^ { p l t }$ is defined as the sum of waiting time at the input queue before production starts, production cycle time, and downtime during the production cycle time. For now, we ignore the subscript k. The expected waiting time at the input queue is derived as follows: Let $Y _ { n }$ be the random demand at week $n ,$ which is normally distributed, $C _ { b }$ be the capacity of the production site, $X _ { n }$ be the unfulfilled demand at week n, and B be the bufer limit of the input queue. The unfulfilled demand at the beginning of week $n + 1$ can be expressed as below:

$$
X _ {n + 1} = \left\{ \begin{array}{l} 0 ; i f Y _ {n} + X _ {n} <   C _ {b} \\ Y _ {n} + X _ {n} - C _ {b}; o t h e r w i s e \end{array} \right\} = M a x \{0, Y _ {n} + X _ {n} - C _ {b} \}
$$

It can be seen that the stochastic process $\{ X _ { n } , n \geq 0 \}$ possesses the Markov property. Also, this process has a discrete parameter since the control model uses periodic review. The state space is discrete because the amount of demand in units is the state space. Therefore, the stochastic process $\{ X _ { n } , n \geq 0 \}$ can be modeled as a finite state discreteparameter Markov chain with the transitional probability matrix being built by evaluating the probability of having a certain amount of demand waiting in the input bufer at week's end. To find the steady state probability vector $\mathfrak { \pi } ^ { ' } = [ \pi _ { 0 } \mathfrak { \pi } _ { 1 } \mathfrak { \pi } _ { 2 } \dots \dots \pi _ { B } ]$ , we use the Grassman, Taksar, and Heyman (GTH) algorithm method [11]. This is a modification of the Gauss-Jordan method to find the steady state probabilities for irreducible finite state Markov chains to calculate $\pi .$

The expected length of the input queue, $L ^ { q } ,$ can be obtained a $\textstyle \sum _ { j = 0 } ^ { B } ( \pi _ { j } * j )$ . Using Little's law, we calculate the expected waiting time at the input queue, $W ^ { q }$ as $\begin{array} { r } { W ^ { q } = \sum _ { i = 0 } ^ { B } { ( \pi _ { j } * j ) / \mu } } \end{array}$ where $\mu$ is the mean demand. Due to the input bufer limit, there can be instances where we have to reject incoming demands. The probability to reject incoming orders is $\begin{array} { r } { \dot { \sum _ { i = 0 } ^ { B } } \left\{ \pi _ { i } P [ \mu > B + C _ { b } - i ] \right\} } \end{array}$ }, and the resulting expected lost sales per week are $\textstyle \sum _ { i = 0 } ^ { B } \sum _ { d = 0 } ^ { \infty } \{ \pi _ { i } P [ \mu = B + C _ { b } - i + d ] d \}$ where d is an integer. Please refer to Grassman et al. [11] for more details.

Let $N ^ { d t }$ be the number of breakdowns during the production cycle time. $N ^ { d t }$ is assumed to be following a Poisson process with $d ^ { n }$ as the mean number of breakdowns per time unit. Also assume that the expected values and the variances of breakdown duration and the production cycle time under normal demand $( \mathrm { i } . \mathrm { e } . , \mu )$ are known. We show in Appendix A that the expected value of the production lead time and the variance of the production lead time can be obtained as follows:

$$
E \left[ T ^ {p l t} \right] = W ^ {q} + E \left[ T ^ {c t} \mid V ^ {i p} = \mu \right] + d ^ {n} E \left[ T ^ {c t} \mid V ^ {i p} = \mu \right] E \left[ T ^ {d t} \right]\tag{2}
$$

$$
V a r [ T ^ {p l t} ] = V a r [ T ^ {c t} \mid V ^ {i p} = \mu ] + d ^ {n} E [ T ^ {c t} \mid V ^ {i p} = \mu ] [ V a r [ T ^ {d t} ] + E [ T ^ {d t} ] ^ {2} ]\tag{3}
$$

where

$T ^ { p l t . }$ Production lead time of production stage k W<sup>q</sup>: Production lead time of production stage k $T ^ { c t . }$ Production cycle time $V ^ { \dot { \imath } p . }$ Input volume for production per week $d ^ { n } { \mathrm { : } }$ Mean number of breakdowns per time unit $T ^ { d t } \colon$ Duration of breakdown

The last component of the lead time between two adjacent fulfillment points is the transportation time. In general, there are two types of transportation time delays—time to ship and transit time. We model the time to ship, $T _ { \mathrm { ~ : ~ } } ^ { t s }$ , as an empirical discrete probability function and the transit time, $T ^ { t r } ,$ , as a probability density function. This approach is often used in third-party logistics [7]. For example, a company may have the probability of shipping the product on the first, second, or third day as (a)%, (b)%, and (1-a-b)%, respectively. The expected duration of the transportation link coming to the production stage, if it exists, can be defined as $\begin{array} { r } { E \left[ T ^ { t p } \right] = \sum _ { \forall i } j P \left[ T ^ { t s } \right] + E \left[ T ^ { t r } \right] } \end{array}$ . The expected value and variance of transportation time between fulfillment point $F _ { k - 1 }$ and $F _ { k }$ are:

$$
\operatorname{E} [ T _ {k} ^ {t p t} ] = \sum_ {k \in G _ {k}} L _ {k} E [ T _ {k} ^ {t p} ]\tag{4}
$$

$$
V a r [ T _ {k} ^ {t p t} ] = \sum_ {k \in G _ {k}} L _ {k} V a r [ T _ {k} ^ {t p} ]\tag{5}
$$

where

$T _ { k } { } ^ { t p } \colon$ Duration of transportation link coming to production stage k $T _ { k } { } ^ { t p t } \mathrm { : }$ Transportation time between fulfillment point $F _ { k - 1 }$ and $F _ { k }$ $L _ { k } \colon 1$ if a transportation link coming to production stage k exists, and 0 otherwise

$G _ { k } \mathrm { : }$ The set of production stages placed between $F _ { k - 1 }$ and $F _ { k }$

Finally, after reinserting subscript k to (2) and (3), with (4) and (5), the expected value and the variance of $T _ { k } ^ { \mathit { l t } } ,$ , the lead time between fulfillment point $F _ { k - 1 }$ and $F _ { k }$ , are:

$$
\begin{array}{r l} & E [ T _ {k} ^ {l t} ] = \sum_ {k \in G _ {k}} \{E [ T _ {k} ^ {p l t} ] \} + E [ T _ {k} ^ {t p t} ] \\ & = \sum_ {k \in G _ {k}} \{W _ {q} + E [ T _ {k} ^ {c t} \mid V _ {k} ^ {i p} = \overline {{D _ {k}}} ] + d _ {k} ^ {n} E [ T _ {k} ^ {c t} \mid V _ {k} ^ {i p} \\ & = \overline {{D _ {k}}} ] E [ T _ {k} ^ {d t} ] + L _ {k} E [ T _ {k} ^ {t p} ] \} \end{array}\tag{6}
$$

$$
\begin{array}{r l} & {V a r [ T _ {k} ^ {l t} ] = \sum_ {k \in G _ {k}} \{V a r [ T _ {k} ^ {p l t} ] \} + V a r [ T _ {k} ^ {t p t} ]} \\ & {= \sum_ {k \in G _ {k}} \{V a r [ T _ {k} ^ {c t} \mid V _ {k} ^ {i p} = \overline {{D _ {k}}} ] + d _ {k} ^ {n} E [ T _ {k} ^ {c t} \mid V _ {k} ^ {i p}} \\ & {= \overline {{D _ {k}}} ] [ V a r [ T _ {k} ^ {d t} ] + E [ T _ {k} ^ {d t} ] ^ {2} ] + L _ {k} V a r [ T _ {k} ^ {t p} ] \}} \end{array}\tag{7}
$$

## 5. Numerical analysis with decision support model

Semiconductor companies have been widely using the push–pull supply chain since it has been suggested as the best approach to overcome dificult market conditions [21]. The speed of breakthroughs in the age of the so called “fourth industrial revolution” is challenging the semiconductor industry to improve delivery/service speed and responsiveness of customer lead times instead of mainly creating value from functionality [1,27]. Improving the design of push-pull supply chains following our proposed decision support system, can therefore provide a theoretical and practical contribution to the semiconductor industry. We constructed this section based on the process described in Fig. 1. Section 5.1 corresponds to step 1 in Fig. 1 where the inputs for supply chain settings in the analysis are selected. In Section 5.2, “feasible candidate generation procedure” is applied to identify feasible locations for demand fulfillment points (step 2 in Fig. 1). Section 5.3 shows how the resulting supply chain design alternatives from Section 5.2 are analyzed in the experiments (steps 3 and 4 in Fig. 1). Section 5.4 discusses the results from the numerical analysis.

## 5.1. Selection of supply chain settings (step 1 of Fig. 1)

## 5.1.1. Supply chain design inputs—semiconductor products, processes, and organizational forms

Generally, semiconductor products are divided into three cate gories: standard general-purpose Integrated Circuit (IC), applicationspecific IC (ASIC), and application-specific standard parts (ASSP). A standard general-purpose IC is the most commonly used semiconductor product, such as memory and microprocessors. An ASIC is a customdesigned IC for a specific application. An ASSP is a type of ASIC chip that is designed as a generic device for a particular product family. An ASSP can be used by many diferent organizations, whereas an ASIC is used only by the company who designed the chip. The generalized summary of semiconductor products is provided in Table 1. In our analysis, we did not select Full Custom IC and Standard Cell/CBIC because all the processes are fully customized from the beginning, which means they cannot have any feasible locations for demand fulfillment points.

The semiconductor processes used in the analysis are explained next. A typical semiconductor supply chain has three main process stages: wafer fabrication, probe, and assembly and testing [2,21]. We assumed four locations for fulfillment point candidates. The lot bank (LB) stores “base-wafer inventory” (semi-finished wafers before being fabricated into diferent types of finished wafers) and is located between “foundry $\mathbf { f a b } ^ { * }$ and “metals $\mathbf { f a b } ^ { * }$ in the wafer fabrication stage [19]. The die bank (DB) is where fabricated and tested wafers are stored prior to the assembly and testing stage. The warehouse (WH) stores completed products after assembly and testing. The full-pull point (FP) is the fulfillment point representing the complete customized production. Based on these locations, the semiconductor supply chain in the analysis is divided into three production stages: Wafer Fab Front End (WFF, wafer fabrication processes before LB), Wafer Fab Back End (WFB, the wafer fabrication processes after LB and probe operation), and Assembly and Testing $( A \& T ,$ integrated circuit packaging and testing processes). Fig. 4 shows the process stages and fulfillment point locations with the flows of demand/replenishment orders/materials. It is very common in the semiconductor industry that A&T work is performed in East Asian countries. If this is the case, it can cause potentially large transportation costs and time delays. Therefore, the model included transportation links before and after A&T. We assume that all finished products are shipped to the central warehouse (WH) and subsequently distributed to the customer destinations.

Finally, the organizational forms considered are provided. Typical organizational forms of semiconductor companies are categorized as follows: Integrated Device Manufacturer (IDM), Fab-Lite, Fabless, Foundry, Outsourced Semiconductor Assembly and Test (OSAT), and Electronic Manufacturing Services (EMS) companies. IDMs (e.g., Intel, Samsung) are large firms that usually perform all of the production stages defined above. Fab-lites (e.g., Texas Instruments, Toshiba) usually outsource the wafer fabrication stages. Fabless companies (e.g., Xilinx, Qualcomm, Broadcom) do not own any production stages and focus on the R&D and marketing of products. Foundry companies (e.g., GlobalFoundries, TSMC) perform wafer fabrication stages only. OSAT companies (e.g., ChipPAC, Amkor) focus on the assembly and testing stage. EMS companies (e.g., Solectron, Flextronics) perform the assembly and testing stage and system set-up services. In our study, only IDM, Fab-lite, Fabless, and Foundry were considered since OSAT and EMS do not have any feasible locations for demand fulfillment points due to the nature of their businesses as subcontractors.

## 5.1.2. Scenario generation inputs

There are two types of scenario generation inputs in the model: internal model parameters and external market/customer factors. Among the internal model parameters, the key cost parameters, such as the wafer cost after each production stage and the transportation costs before/after A&T stage, were selected by benchmarking the wafer cost model of the Competitive Semiconductor Manufacturing Program at University of California at Berkeley [4], whereas the key lead time parameters such as the mean cycle times for each production stage were benchmarked from Duarte et al. [6] and Brown et al. [2], which are based on real semiconductor datasets and cases. Some of the key benchmarks used in the analysis are presented in Table 2.

Table 1  
Categorization of semiconductor products. (Kim and Kim [17])

<table><tr><td colspan="2">Categories</td><td>Descriptions</td></tr><tr><td>Standard IC (integrated circuit)</td><td></td><td>Includes memory, microprocessor (micro component), DSP (Digital Signal Processor), analog, discrete, and optical semiconductors.</td></tr><tr><td rowspan="6">ASIC (application specific integrated circuit)</td><td>Full custom ASIC</td><td>The most costly chip and uses a custom-designed mask for every layer in the chip.</td></tr><tr><td>Standard cell or CBIC (cell based IC)</td><td>It is custom designed and then inserted into a library. Then used in the designs for various custom products</td></tr><tr><td>Structured ASIC</td><td>Contain blocks of logic (called tiles or modules) that have their transistors already wired together forming gates along with some combination of multiplexors, flip-flops, look up tables and the likes.</td></tr><tr><td>GA (gate array)/MGA (masked GA)</td><td>Partially finished with rows of the transistors and resistors built in but unconnected. Designers cannot change the transistor masks. The designer instead programs wiring and vias to implement the desired function.</td></tr><tr><td>PLD (programmable logic device)</td><td>A variety of off-the-shelf chips that are programmable and tested by the customers to perform various functions</td></tr><tr><td>FPGA (field programmable GA)</td><td>Another major off-the-shelf programmable logic chips that customers can perform simple functions while the customers of the PLDs can perform various functions.</td></tr><tr><td colspan="2">ASSP (application specific standard product)</td><td>An ASIC chip that is designed as a generic device for a particular market. Whereas an ASIC is typically used only by its creator, an ASSP is used by many different organizations.</td></tr></table>

![](/api/attachments/DRARXFRX/fulltext/images/21c68ec881566319d06d8393c227351e9e92e8ee022fccd47096ade93750758c.jpg)  
Fig. 4. Process stages and fulfillment point locations.

The external market/customer factors considered in our experi ments are Demand Variability (DV, by Coeficient of Variation [CV]), Customer Lead Time Variability (CLTV, by CV), Holding Cost rate (HC, by percent per year), Penalty rate for tardy orders (PNTY, by percent of finished product value), and Discount rate (DSC, by percent of finished product value), which is the rate for discounts given to customers who require shorter lead times than the expected remaining lead time from the last demand fulfillment point. While DV and CLTV may be determined case by case by the user, there exist some reasonable ranges for HC, PNTY, and DSC [12,29], which were referenced in the analysis. For these five factors, two levels of variability were set as in Table 3 in order to create the input scenarios by $\textbf { a } 2 ^ { \mathrm { k } }$ factorial design with $\mathbf { k } = 5 .$ We explain the details of the experimental design used in the analysis in Section 5.3.2.

## 5.2. Feasible candidate generation procedure (step 2 in Fig. 1)

On the basis of the supply chain design inputs selected in Section 5.1, the feasible candidate generation procedure presented in Section 3 is used to find the feasible locations for demand fulfillment points. By applying the customization processes of semiconductor products described in Kim [16], we can see that the customization areas of Structured ASIC and GA are WFB and A&T, and A&T for the other selected products. Let IDM (1), Fab-lite (2), Fabless (3), and Foundry (4) be the members of set $I = \{ i | i = 1 , 2 , 3 , 4 \}$ t. Also, WFF (1). WFB (2), A&T (3). and Full Pull production (0) are denoted as the members of set $K = \left\{ k \vert k = 0 , 1 , 2 , 3 \right\}$ with FP (0), LB (1), DB (2), and WH (3) being q , $q _ { 1 } , q _ { 2 } ,$ and $q _ { 3 } .$ . Let Structured ASIC, GA be product type 1 and the rest of the products be product type 2, thus $J = \{ j | j = 1 , 2 \}$ . By following this procedure, the step-by-step results are as follows:

$$
\begin{array}{l} 1. I = \{i | i = 1, 2, 3, 4 \}, J = \{j | j = 1, 2 \}, K = \{k | k = 0, 1, 2, 3 \} \\ 2. A _ {1} = \{0, 1, 2, 3 \}, A _ {2} = \{0, 3 \}, A _ {3} = \{0 \}, A _ {4} = \{0, 1, 2 \}, B _ {1} = \{2, 3 \}, \\ B _ {2} = \{\emptyset \} \end{array}
$$

$$
\begin{array}{c} 3. Q _ {1 1} = \{q _ {0}, q _ {1} \}, \quad Q _ {1 2} = \{q _ {0}, q _ {1}, q _ {2}, q _ {3} \}, \quad Q _ {2 1} = \{q _ {0} \}, \quad Q _ {2 2} = \{q _ {0}, q _ {3} \}, \\ Q _ {3 1} = \{q _ {0} \},   Q _ {3 2} = \{q _ {0} \},   Q _ {4 1} = \{q _ {0}, q _ {1} \},   Q _ {4 2} = \{q _ {0}, q _ {1}, q _ {2} \} \end{array}
$$

$4 . \ Q _ { 1 1 } = \{ q _ { 0 } , q _ { 1 } \} , \ Q _ { 1 2 } = \{ q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } \} , \ Q _ { 2 1 } = \{ q _ { 0 } \} , \ Q _ { 2 2 } = \{ q _ { 0 } , q _ { 2 } , q _ { 3 } \} ,$ $Q _ { 3 1 } = \{ q _ { 0 } \} , Q _ { 3 2 } = \{ q _ { 0 } , q _ { 3 } \} , Q _ { 4 1 } = \{ q _ { 0 } , q _ { 1 } \} , Q _ { 4 2 } = \{ q _ { 0 } , q _ { 1 } , q _ { 2 } \} ;$ ; In $Q _ { 3 2 } ,$ $q _ { 3 }$ is added because some Fabless companies control finished in ventories by themselves to fulfill customer orders.

$$
Q _ {1 1} ^ {*} = \{(q _ {0}), (q _ {1}), (q _ {0}, q _ {1}) \},
$$

![](/api/attachments/DRARXFRX/fulltext/images/e9b14581e27adba1809f36ad38ddcfd90806bb39f9a6e18836bd76c7a8d98f28.jpg)

The resulting feasible candidate locations are summarized in Fig. 5. The candidate locations provide hypothetical points to fulfill customer orders. For instance, even though using FP makes little sense for Standard IC from a practical point of view, if the CLR (Customer Lead time Requirement) associated with a particular order is long enough, we can use FP to fulfill that order to reduce inventory cost. Since we run scenarios with various CLRs, it is possible that some proportions of orders can be fulfilled at FP in our hypothetical study.

Using all the subsets in step 5 above, supply chain design alternatives are generated for all products and organizational forms. In this study, design alternatives are designated by the names of the fulfillment points used. For example, the design alternative FP, DB, & WH represents the one with the demand fulfillment points located at FP, DB, and WH. This is one of the 15 design alternatives of the IDM supply chain for Standard IC, PLD, FPGA, and $\mathsf { A S S P { \_ } l } _ { 0 } , q _ { 2 } , q _ { 3 } )$ in $Q _ { 1 2 } { ^ { * } }$

## 5.3. Setting up the analysis (including steps 3 and 4 in Fig. 1)

## 5.3.1. Design of experiments for the analysi

One of the main objectives of the decision support model is to identify the most efective supply chain design based on various combinations of market/customer factors. When there are multiple factors that afect the performance measure, the best approach is to conduct a factorial experiment in which all factors are varied together, instead of one at a time, since there may be interactions among the factors that can cause misleading conclusions [23]. The $2 ^ { k }$ factorial experiment is the most eficient and efective among the factorial experiments where all the possible combinations of factors are experimented at two levels. But the prerequisite of the $2 ^ { \mathrm { k } }$ factorial experiment is that each factor needs to show a linear relationship with the performance measure. Since our sensitivity analysis satisfied the linearity requirement, which is shown in Section 5.3.3, we implemented $2 ^ { 5 }$ factorial experiments by using the five external market/customer factors with two factor levels as in Table $^ { 3 , }$ , which resulted in 32 input scenarios in the analysis.

## 5.3.2. Sensitivity analysis for optimization parameters

Since we find the optimal values for the decision variables in each supply chain design alternative by the simulated annealing (SA)

Examples of key benchmarks for internal model parameters. Table 2

<table><tr><td colspan="6">Wafer cost after each process stage ($/wafer)</td></tr><tr><td>Blank wafer</td><td colspan="2">After WFF stage</td><td colspan="2">After WFB stage</td><td>After A&amp;T stage</td></tr><tr><td>200</td><td colspan="2">1100</td><td colspan="2">2100</td><td>3150</td></tr><tr><td colspan="6">Transportation cost</td></tr><tr><td rowspan="2"></td><td rowspan="2">Initiation cost ($)</td><td colspan="4">Cost per wafer ($), based on shipment size (S)</td></tr><tr><td>S &lt; 100</td><td>100 &lt; S &lt; 500</td><td>500 &lt; S &lt; 1000</td><td>S &gt; 1000</td></tr><tr><td>Wafer fab → A&amp;T</td><td>500</td><td>5</td><td>4</td><td>3</td><td>1</td></tr><tr><td>A&amp;T → WH</td><td>600</td><td>6</td><td>4.8</td><td>3.6</td><td>1.2</td></tr><tr><td colspan="6">Mean cycle times based on capacity loadings (wafer fab)</td></tr><tr><td>Capacity loading</td><td>0.4050</td><td colspan="2">0.6480</td><td>0.8100</td><td>0.9730</td></tr><tr><td>Mean cycle time (days)</td><td>18.80</td><td colspan="2">19.94</td><td>22.58</td><td>34.65</td></tr></table>

Table 3  
External market/customer factors and their levels (CV: coeficient of variation).

<table><tr><td>Factors\levels</td><td>High</td><td>Low</td></tr><tr><td>DV</td><td>N(1000, 800), CV = 0.8, in wafers</td><td>N(1000, 200), CV = 0.2, in wafers</td></tr><tr><td>CLTV</td><td>N(10, 8), CV = 0.8, in weeks</td><td>N(10,2), CV = 0.2, in weeks</td></tr><tr><td>HC</td><td>50% (per year)</td><td>33% (per year)</td></tr><tr><td>PNTY</td><td>25% (per product value)</td><td>10% (per product value)</td></tr><tr><td>DSC</td><td>25% (per product value)</td><td>10% (per product value)</td></tr></table>

algorithm in the decision support model, we first performed a sensitivity analysis on SA parameters. The key parameters in SA are the initial temperature $\left( \mathrm { T } _ { 0 } \right)$ and the cooling rate (δ) [14,30,32]. To find the appropriate parameter values, pilot tests were carried out using the most complicated design alternative (FP, LB, DB, & WH). Fig. 6 shows the outcome. The initial temperature did not have much impact on the total cost, but clearly impacted the solution time. We therefore selected an initial temperature of 10.00 because it provided the fastest solution time. Total cost was more strongly impacted by the cooling rate, where cost decreased as the cooling rate increased. Due to the jump in solution time that occurs at 0.9, we initially selected a cooling rate of 0.8 and then fine-tuned it to 0.78. Setting the cooling rate at 0.78 as opposed to 0.8 resulted in nearly a 40% decrease in solution time, while resulting in negligent cost increase. Table 4 shows the SA parameters selected in the analysis, based on the findings from the pilot tests.

## 5.3.3. Sensitivity analysis for external factor

Next, we performed the sensitivity analysis on the efects of the external market/customer factors. The main purpose was to see if there was a linear relationship between each factor and the objective function value since it was essential for the design of experiments in the analysis. We chose one conventional design alternative (DB, the most common design in the semiconductor industry) and one multi-point (proposed) design alternative (FP, LB, & DB). FP, LB, & DB was selected because we wanted a multi-point design that had the last fulfillment point at DB so that we could test discount cost in similar conditions (i.e., if the last fulfillment point is WH, there is no discount cost since we can deliver directly from the finished product inventory). Fig. 7 presents the results where CV stands for coeficient of variation.

Against DV (Demand Variability), both alternatives similarly re sponded to increasing DV. In HC (Holding Cost Rate) comparison, the cost was slightly higher for FP, LB, & DB due to more inventories at multiple inventory locations. Against CLTV (Customer Lead Time Variability), FP, LB, & DB showed less sensitivity. When CLTV increases, more customer orders with a large customer lead time can be generated and those orders are assigned to FP and LB. Because the inventory values at FP and LB are low, the overall cost of FP, LB, & DB can increase at a slower rate than DB. Regarding PNTY (Penalty Rate), the cost of FP, LB, & DB increased at a higher rate than DB. The orders assigned to FP and LB are further away from the customers and more likely to be late. Consequently, the cost can increase faster than DB as PNTY increases. In the DSC (Discount Rate) comparison, FP, LB, & DB showed less sensitivity. The possible reason is how the lead time is quoted to customers. In the proposed design, the lead time is quoted dynamically based on the current expected remaining lead time of the fulfillment point. In a conventional design, many companies give one predetermined quoted lead time to all customers. It can potentially cause more cases where the sales force has to provide discounts to make customers stay. Most importantly, we could observe a linear relationship between each factor and the objective function value for both design alternatives. It can be seen from Table 5 that the objective function values of these two designs have a strong positive linear relationship with all the external factors.

<table><tr><td>IDM</td><td>FP</td><td>LB</td><td>DB</td><td>WH</td></tr><tr><td>Prod.Stage Product</td><td>WFF</td><td>WFB</td><td>A&amp;T</td><td></td></tr><tr><td>Structured ASIC</td><td></td><td></td><td></td><td></td></tr><tr><td>GA</td><td></td><td></td><td></td><td></td></tr><tr><td>PLD</td><td></td><td></td><td></td><td></td></tr><tr><td>FPGA</td><td></td><td></td><td></td><td></td></tr><tr><td>ASSP</td><td></td><td></td><td></td><td></td></tr><tr><td>Standard IC</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Product\Prod.Stage</td><td>Outsourced Foundry</td><td>A&amp;T</td></tr><tr><td>Structured ASIC</td><td></td><td></td></tr><tr><td>GA</td><td></td><td></td></tr><tr><td>PLD</td><td></td><td></td></tr><tr><td>FPGA</td><td></td><td></td></tr><tr><td>ASSP</td><td></td><td></td></tr><tr><td>Standard IC</td><td></td><td></td></tr></table>

<table><tr><td>Product\Prod.Stage</td><td>Outsourced Foundry</td><td>Outsourced A&amp;T</td></tr><tr><td>Structured ASIC</td><td></td><td></td></tr><tr><td>GA</td><td></td><td></td></tr><tr><td>PLD</td><td></td><td></td></tr><tr><td>FPGA</td><td></td><td></td></tr><tr><td>ASSP</td><td></td><td></td></tr><tr><td>Standard IC</td><td></td><td></td></tr></table>

<table><tr><td>Foundry</td><td>FP</td><td>LB</td><td>DB</td></tr><tr><td>Product\Prod.Stage</td><td>WFF</td><td>WFB</td><td></td></tr><tr><td>Structured ASIC</td><td></td><td></td><td></td></tr><tr><td>GA</td><td></td><td></td><td></td></tr><tr><td>PLD</td><td></td><td></td><td></td></tr><tr><td>FPGA</td><td></td><td></td><td></td></tr><tr><td>ASSP</td><td></td><td></td><td></td></tr><tr><td>Standard IC</td><td></td><td></td><td></td></tr></table>

Fig. 5. Resulting feasible locations for fulfillment point.

![](/api/attachments/DRARXFRX/fulltext/images/597d24130d1daa1f4f918391a69eba67a77ddc206036440df3400f42428faeb2.jpg)

![](/api/attachments/DRARXFRX/fulltext/images/16162a62cce61949d2979b7ef1cab745c2a4259e4c6985b1cacef6e0008d2752.jpg)  
Fig. 6. Sensitivity analysis on SA parameters.

Simulated annealing parameters used in the analysis.

<table><tr><td>SA parameters</td><td>Descriptions</td></tr><tr><td>Initial temperature, T(0)</td><td>10.00</td></tr><tr><td>Cooling schedule</td><td>Proportional, T(t + 1) = 0.78 * T(t)</td></tr><tr><td>Number of iterations at each temperature</td><td>Maximum of 30 or number of success &gt;5</td></tr><tr><td>Stopping criterion</td><td>Maximum of 5000 function calls or the final temperature, T(f) &lt; 1.0</td></tr></table>

## 5.4. Results

To include all the possible design alternatives in the analysis, we considered the case in Fig. 5 where the organizational form is IDM and the products are PLD, FPGA, ASSP, and Standard IC. Table 6 presents the descriptive statistics of the results from the 32 input scenarios in our 2<sup>5</sup> factorial experiments.

## 5.4.1. Comparison of the proposed designs and the conventional designs

The first criterion used in the comparison of supply chain design alternatives is “robustness.” We defined robustness in our study as how much a supply chain design alternative is insensitive to the external factors (less variability). Since the objective function is cost, we also compared the cost-efectiveness of the design alternatives. Therefore, we looked for a design that resulted in a lower standard deviation and a lower mean value of cost. Fig. 8 shows the comparison of all design alternatives, where the ones toward the lower-left corner of the figure in dicate better robustness. It was found that the best design was FP, DB, & WH, with FP, LB, DB, & WH, DB & WH, LB, DB, & WH producing close results (the dotted circle in Fig. 8). It can be seen that those robust designs are all multi-point (proposed) designs. Another observation is that the worst three alternatives in the experiments (the dotted rectangle in Fig. 8) are FP & LB. LB, and FP. which have either FP or LB as the closest fulfillment point from the customers. It implies that there is a limitation on how far fulfillment points can be pushed back in a supply chain, which is consistent with Kim et al. [18].

Since our main purpose is to improve the customer responsiveness and customer lead time management capability of a push–pull supply chain, another set of experiments was performed on customer lead time requirement variability (CLTV) and demand variability (DV). CLTV and DV reflect how customers behave in the market. Also these factors can be associated with possible disrupting efects on a supply chain. To compare the performance against these external factors, the most commonly used design in the semiconductor industry (DB) and the best performed multi-point design (FP, DB, & WH) were selected. Fig. 9 illustrates the outcomes. Against the volatile behavior of customers (300% increases in CLTV and DV), FP, DB, & WH showed more robustness in both cases, particularly against CLTV.

![](/api/attachments/DRARXFRX/fulltext/images/05867638e6d0ebacd834a42cd88e96a0473eb2012144e89f02bd6621cfc17d77.jpg)

![](/api/attachments/DRARXFRX/fulltext/images/094390f6b1e738c882ce61bb15ff3621232d32aa33c0a2331fd51813528b06e5.jpg)

![](/api/attachments/DRARXFRX/fulltext/images/ec3e1788c9af45b3e5d5e8d8f54e46c4f10c66e9c5e704642d0695954d6a50f8.jpg)

![](/api/attachments/DRARXFRX/fulltext/images/a5ad0f5f23c4617489f90c8b1496ae03f86ede97451e4e0f63f6a82796503cdb.jpg)

![](/api/attachments/DRARXFRX/fulltext/images/aea617c257c033be419b6446ffcf687b0b400b451916e09078c2507bfcd16849.jpg)  
Fig. 7. Sensitivity analysis on external market/customer factors.

Correlation coeficient of objective function value and external factor for the designs.

<table><tr><td>Correlation coefficient with objective function value</td><td>DV</td><td>CLTV</td><td>HC</td><td>PNTY</td><td>DSC</td></tr><tr><td>Proposed design</td><td>0.99491</td><td>0.81176</td><td>0.99998</td><td>0.99965</td><td>0.97082</td></tr><tr><td>Conventional design</td><td>0.99283</td><td>0.87215</td><td>0.98967</td><td>0.99972</td><td>0.99591</td></tr></table>

## 5.4.2. Efective transition toward the proposed design from the conventional design

Another contribution of this paper mentioned in Section 1 is that we provide the decision maker with an efective strategy on how to make the transition toward the proposed design from the conventional push–pull design. Since the decision makers may have to face implementation issues when they plan to change their supply chain designs, it is possible that the number of fulfillment points to be added can be less than the recommended number due to the unique technical/ geographical/logistical/resource constraints of a given enterprise. The outcome of the analysis is presented in Fig. 10.

Fig. 10 shows the situation where we want to add one more fulfillment point to a conventional design with DB. Based on our experiments (the mean cost of 32 scenarios), placing a fulfillment point closer to customers (at WH) improved the performance (A2 in Fig. 10-(a)), whereas placing it further from customers (at LB) resulted in a worse performance (A1 in Fig. 10-(a)). Now examine the case of a conventional design with LB, instead of DB. First, using FP (pull production for orders with very long CLRs) in addition to LB (B1 in Fig. 10-(b)) barely improved the performance. Placing a fulfillment point at DB, which is closer to customers than LB, shows reasonable improvement (B2 in Fig. 10-(b)). Placing it at WH, which is closer to customers than DB, moves the cost further toward the lower-left corner (B3 in Fig. 10-(b)), showing much more improvement. We can still improve more if two additional fulfillment points are allowed, by using the recommended

Table 6  
Descriptive statistics from $2 ^ { 5 }$ factorial experiments.

<table><tr><td rowspan="2">Supply chain design</td><td rowspan="2">Mean</td><td colspan="3">Objective function value (cost in $)</td></tr><tr><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>WH</td><td>194,123.18</td><td>50,173.18</td><td>133,503.30</td><td>289,147.49</td></tr><tr><td>DB</td><td>199,574.00</td><td>101,864.23</td><td>64,739.04</td><td>461,552.91</td></tr><tr><td>LB</td><td>355,707.59</td><td>158,016.70</td><td>178,263.48</td><td>784,461.79</td></tr><tr><td>FP</td><td>416,477.35</td><td>177,964.76</td><td>256,363.29</td><td>789,113.33</td></tr><tr><td>DB &amp; WH</td><td>117,729.43</td><td>36,830.87</td><td>57,018.70</td><td>195,525.37</td></tr><tr><td>LB &amp; WH</td><td>165,442.92</td><td>51,562.91</td><td>98,158.32</td><td>283,653.52</td></tr><tr><td>FP &amp; WH</td><td>180,067.21</td><td>52,415.93</td><td>105,119.53</td><td>289,103.03</td></tr><tr><td>FP &amp; DB</td><td>199,998.29</td><td>96,949.07</td><td>67,832.03</td><td>464,992.70</td></tr><tr><td>FP &amp; LB</td><td>346,368.81</td><td>157,132.36</td><td>172,566.04</td><td>784,411.16</td></tr><tr><td>LB &amp; DB</td><td>217,667.49</td><td>119,254.46</td><td>64,473.37</td><td>477,159.13</td></tr><tr><td>FP, DB &amp; WH</td><td>112,052.21</td><td>35,067.51</td><td>55,796.12</td><td>188,745.03</td></tr><tr><td>FP,LB &amp; WH</td><td>162,787.21</td><td>53,110.84</td><td>92,911.45</td><td>283,406.17</td></tr><tr><td>FP,LB &amp; DB</td><td>178,383.20</td><td>88,856.38</td><td>60,282.35</td><td>372,254.85</td></tr><tr><td>LB, DB &amp; WH</td><td>115,628.06</td><td>40,526.82</td><td>53,460.42</td><td>197,979.75</td></tr><tr><td>FP,LB,DB &amp; WH</td><td>112,957.33</td><td>38,494.92</td><td>53,848.22</td><td>186,803.08</td></tr></table>

Bold data indicates the best results.

design (B4 in Fig. 10-(b)). These results demonstrate an important managerial implication: it may be beneficial for a given supply chain to place additional fulfillment points one by one starting at the closest location to customers toward the beginning of a supply chain. Also, it shows that maintaining a certain level of finished-goods inventories in addition to the existing fulfillment point can enhance the robustness of a push–pull supply chain, which coincides with the result of the Xilinx supply chain case study [2].

Regarding the possible concern of management that the proposed design can lead to a significant increase in inventory cost, Table 7 shows that there is a relatively small increase in inventory cost compared to the considerable reduction in order tardiness cost and lead time negotiation discount cost.

## 6. Conclusions and future research

In this study, we present a decision support system for designing a push–pull supply chain that can integrate the product, process, and organizational form of a given enterprise. Also, using the improved push–pull control model, we show that the model can enhance the customer lead time management capability of a push–pull supply chain.

Our analytical results yield several managerial implications in designing push–pull supply chains. First, managers need to investigate the current location of the push–pull boundary carefully when unexpected market or supply chain disruptions occur since it may influence how far the push–pull boundary can be pushed back. In our experiments, pushing back the fulfillment point beyond DB caused an explosion in service costs. We also find an interesting insight on how to move toward

![](/api/attachments/DRARXFRX/fulltext/images/135667f8a910505c8d1af8cf1632b925d99716f39981e392eadee61c9e2f03ad.jpg)  
Fig. 8. Comparison of all supply chain design alternatives.

![](/api/attachments/DRARXFRX/fulltext/images/71c26b97079efe8a9219346fab76fcfc72f5acb4d3ad73a0602fbba45102decd.jpg)  
Fig. 9. Comparison against disrupting customer behaviors.

![](/api/attachments/DRARXFRX/fulltext/images/dfde49d51e8a1373f478b61a04590a0345667bac070c4f4daf9b6e30e3e82e64.jpg)  
(a) Adding an Inventory Point to DB

![](/api/attachments/DRARXFRX/fulltext/images/fa74c86d6665d55095930f61299e68ef7ac2dbae7f8edad845440d38d4952f5e.jpg)  
(b) Adding Inventory Points to LB  
Fig. 10. Placing additional fulfillment points to conventional push-pull designs.

Table 7  
Overall cost breakdown of proposed designs and conventional designs.

<table><tr><td>Design of the supply chain</td><td>Expected lead time negotiation discount cost</td><td>Expected order tardiness cost</td><td>Expected inventory cost</td></tr><tr><td>Conventional designs</td><td>$ 103,219.66</td><td>$104,979.57</td><td>$ 50,058.05</td></tr><tr><td>Multi-point (proposed) designs</td><td>$ 31,679.35</td><td>$ 63,325.58</td><td>$ 62,351.81</td></tr></table>

the proposed supply chain design from the conventional one. This is an important managerial issue since companies may be able to add only a limited number of fulfillment points due to their unique constraints of supply chains. We show that an efective way to add more fulfillment points to a conventional push–pull supply chain is to start adding one from the closest inventory location to customers, and then to add more points toward the beginning of a supply chain. In addition, we find that including a finished-goods inventory point in the fulfillment point selection can make a more significant improvement.

There are some limitations in our work that present opportunities for future research. First, developing a model that can describe multiple value streams being converged and diverged through the push–pull boundary will be a meaningful extension. Also, adding an auxiliary order-shifting algorithm, where orders can be assigned to another downstream fulfillment point if that point has too much excess inventory, can improve the current control model. Another limitation is the lack of lead time negotiation elements in the model. An interdisciplinary research with the sales function where the model can provide upper limits (or lower limits) on the lead time negotiation based on the input market factors might be fruitful.

## Appendix A. The expected value and the variance of production lead time

Let $W ^ { q } , T ^ { c t } , V ^ { i p } , N ^ { d t }$ , and $T ^ { d t }$ denote the expected waiting time at the input queue (which is already defined on Page 14), the random variables for the production cycle time, the input volume for production per week, the number of breakdowns during the production cycle time, and the duration of breakdown, respectively. Also let the expected values and the variances of $T ^ { d t }$ and the expected values and the variances of $T ^ { c t }$ under normal demand $( \mathrm { i } . \mathrm { e } . , \mu )$ be known. $N ^ { d t }$ is assumed to be following a Poisson process with $d ^ { n }$ as the mean number of breakdowns per time unit. The expected value of production lead time, $E [ T ^ { p l t } ]$ , can be obtained as follows:

$$
E \left[ T ^ {p l t} \right] = W ^ {q} + E _ {V ^ {i p}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p} \right] \right]\tag{A1}
$$

$$
E \left[ T ^ {p l t} \mid V ^ {i p} \right] = E _ {N ^ {d t}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] \right]\tag{A2}
$$

$$
E \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] = E \left[ T ^ {c t} \mid V ^ {i p} \right] + N ^ {d t} E \left[ T ^ {d t} \right]\tag{A3}
$$

And if we denote $\operatorname { E } [ N ^ { d t } ]$ as the expected number of breakdowns during the expected production cycle time under the normal demand, from (A3) we can get:

$$
E _ {N ^ {d t}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] \right] = E \left[ T ^ {c t} \mid V ^ {i p} \right] + E \left[ N ^ {d t} \right] E \left[ T ^ {d t} \right] = E \left[ T ^ {c t} \mid V ^ {i p} \right] + d ^ {n} E \left[ T ^ {c t} \mid V ^ {i p} \right] E \left[ T ^ {d t} \right]\tag{A4}
$$

From (A2) and (A4),

$$
E _ {V ^ {i p}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p} \right] \right] = E \left[ T ^ {c t} \mid V ^ {i p} = E \left[ V ^ {i p} \right] \right] + d ^ {n} E \left[ T ^ {c t} \mid V ^ {i p} = E \left[ V ^ {i p} \right] \right] E \left[ T ^ {d t} \mid V ^ {i p} \right]\tag{A5}
$$

$$
\text { Since } E [ V ^ {i p} ] = \mu , \text { the   expected   value   of   production   lead   time   is   obtained   by   (A1)   and   (A5): }
$$

$$
E [ T ^ {p l t} ] = W ^ {q} + E [ T ^ {c t} \mid V ^ {i p} = \mu ] + d ^ {n} E [ T ^ {c t} \mid V ^ {i p} = \mu ] E [ T ^ {d t} ]\tag{A6}
$$

Next, the variance of the production lead time can be obtained as follows:

$$
V a r \left[ T ^ {p l t} \right] = E _ {V ^ {i p}} \left[ V a r \left[ T ^ {p l t} \mid V ^ {i p} \right] \right] + V a r _ {V ^ {i p}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p} \right] \right]
$$

$$
V a r \left[ T ^ {p l t} \mid V ^ {i p} \right] = E _ {N ^ {d t}} \left[ V a r \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] \right] + V a r _ {N ^ {d t}} \left[ E \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] \right]
$$

$$
V a r \left[ T ^ {p l t} \mid V ^ {i p}, N ^ {d t} \right] = V a r \left[ T ^ {c t} \mid V ^ {i p} \right] + N ^ {d t} V a r \left[ T ^ {d t} \right]\tag{A7}
$$

From (A3) and (A7) we get:

$$
\operatorname{Var} \left[ T ^ {p l t} \mid V ^ {i p} \right] = \operatorname{Var} \left[ T ^ {c t} \mid V ^ {i p} \right] + E \left[ N ^ {d t} \right] \operatorname{Var} \left[ T ^ {d t} \right] + E \left[ T ^ {d t} \right] ^ {2} \operatorname{Var} \left[ N ^ {d t} \right]
$$

From (A2) and (A4),

$$
E [ T ^ {p l t} \mid V ^ {i p} ] = E [ T ^ {c t} \mid V ^ {i p} ] + d ^ {n} E [ T ^ {c t} ] E [ T ^ {d t} ]
$$

$$
\begin{array}{r l} & {\therefore V a r [ T ^ {p l t} ] = E _ {V ^ {i p}} [ V a r [ T ^ {c t} \mid V ^ {i p} ] + E [ N _ {d t} ] V a r [ T ^ {d t} ] + E [ T ^ {d t} ] ^ {2} V a r [ N ^ {d t} ] ]} \\ & {\quad + V a r _ {V ^ {i p}} [ E [ T ^ {c t} \mid V ^ {i p} ] + d ^ {n} E [ T ^ {c t} ] E [ T ^ {d t} ] ]} \\ & {\quad = E _ {V ^ {i p}} [ V a r [ T ^ {c t} \mid V ^ {i p} ] ] + E [ N ^ {d t} ] V a r [ T ^ {d t} ] + E [ T ^ {d t} ] ^ {2} V a r [ N ^ {d t} ]} \end{array}
$$

Since $N ^ { d t }$ follows a Poisson process, $V a r [ N ^ { d t } ] = E [ N ^ { d t } ]$ .Also $E [ V ^ { \dot { p } } ] = \mu .$ . Therefore, we can obtain the variance of the production lead time as follows:

$$
\boldsymbol {V a r} \left[ T ^ {p l t} \right] = \boldsymbol {V a r} \left[ T ^ {c t} \mid V ^ {i p} = \mu \right] + \boldsymbol {E} \left[ N ^ {d t} \right] \left[ \boldsymbol {V a r} \left[ T ^ {d t} \right] + \boldsymbol {E} \left[ T ^ {d t} \right] ^ {2} \right]
$$

$$
= \operatorname{Var} \left[ T ^ {c t} \mid V ^ {i p} = \mu \right] + d ^ {n} E \left[ T ^ {c t} \mid V ^ {i p} = \mu \right] \left[ \operatorname{Var} \left[ T ^ {d t} \right] + E \left[ T ^ {d t} \right] ^ {2} \right]
$$

## References

[1] Accenture, Semiconductor supply chains: an urgent need for change, https://www. accenture com/us-en/ acnmedia/Accenture/Conversion-Assets/DotCom. Documents/Global/PDF/Technology\_2/Accenture-Semiconductor-Supply-Chains-An-Urgent-Need-For-Change.pdf/, (2017) , Accessed date: 18 June 2012.

[2] A.O. Brown, H.L. Lee, R. Petrakian, Xilinx improves its semiconductor supply chain using product and process postponement, Interfaces 30 (4) (2000) 65–80.

[3] J.K. Cochran, S. Kim, Optimum junction point location and inventory levels in serial push/pull production systems, International Journal of Production Research 36 (4) (1998) 1141–1155.

[4] Competitive Semiconductor Manufacturing Program, Wafer Fab Cost Model, University of California at Berkeley, 2004 Available from: https://microlab. berkeley.edu/csm/ , Accessed date: 10 August 2011.

[5] Paul Corry, E. Kozan, Meta-heuristics for a complex push-pull production system, Journal of Intelligent Manufacturing 15 (3) (2004) 381–393.

[6] B.M. Duarte, J. Fowler, K. Knutson, E. Gel, D. Shunk, A compact abstraction of manufacturing nodes in a supply network, International Journal of Simulation and Process Modelling 3 (3) (2007) 115–126.

[7] T. Duong, Simulation of Semiconductor Supply Networks, M.S. Thesis Arizona State University, 2003.

[8] C.H. Fine, Clockspeed: Winning Industry Control in the Age of Temporary Advantage, Perseus Books, Cambridge, 1998.

[9] F.S. Fogliatto, G.J. Da Silveira, D. Borenstein, The mass customization decade: an updated review of the literature, International Journal of Production Economics 138 (1) (2012) 14–25

[10] FSA (Fabless Semiconductor Association) and Lions Peak, LLC, Efective management of outsourced operations: contending with the new dynamics and volatility ir the electronics supply chain. FSA Research Report (2003).

[111 W.K. Grassman. M. Taksar. D. Heyman. Regenerative analysis and steady-state distributions for Markoy chains, Operations Research 33 (5) (1985) 1107–1116.

[12] M.G. Hegedus, W. Hopp, Due date setting with supply constraints in systems using MRP, Computers & Industrial Engineering 39 (3–4) (2001) 293–305

[13] A. Jaszkiewicz, Genetic local search for multi-objective combinatorial optimization, European Journal of Operational Research 137 (2002) 50–71.

[14] V. Jayaraman, A. Ross, A simulated annealing methodology to distribution network design and management, European Journal of Operational Research 144 (3) (2003) 629-645.

[15] P. Jonsson, L.K. Ivert, Improving performance with sophisticated master productior scheduling. International Journal of Production Economics 168 (2015) 118–130

[16] J.I. Kim, Strategic positioning of decoupling points on the semiconductor supply chain, Journal of the Korean Society of Supply Chain Management 6 (1) (2006) 79-93.

[17] J.I. Kim, S.H. Kim, Positioning a decoupling point in a semiconductor supply chain under demand and lead time uncertainty, International Journal of Advanced Logistics 1 (2) (2012) 33–47.

[18] S.H. Kim, J.W. Fowler, D.L. Shunk, M.E. Pfund, Improving the push–pull strategy in a serial supply chain by a hybrid push–pull control with multiple pulling points, International Journal of Production Research 50 (19) (2012) 5651–5668

[19] R. Leachman, Production planning and scheduling practices across the semiconductor industry, Competitive Semiconductor Manufacturing Program Report, University of California at Berkelev. 1994

[20] H.L. Lee, C. Billington, Material management in decentralized supply chains,

Operations Research 41 (5) (1993) 835–848.

[21] Y.H. Lee, Supply chain model for the semiconductor industry of global market Journal of Systems Integration 10 (2001) 189–206.

[22] D.S. Levi, P. Kaminsky, E. Levi, Designing and Managing the Supply Chain: Concepts, Strategies, and Case Studies, McGraw-Hill, 2003.

[23] D.C. Montgomery, Design and Analysis of Experiments, 8th edition, Joh Wiley and Sons, 2013.

[24] J. Olhager, Strategic positioning of the order penetration point, Internationa Journal of Production Economics 85 (3) (2003) 319–329

[25] J.D. Pagh, M. Cooper, Supply chain postponement and speculation strategies: how to choose the right strategy, Journal of Business Logistics 19 (2) (1998) 13.

[26] M. Rudberg, J. Wikner, Mass customization in terms of the customer order decoupling point. Production Planning and Control 15 (4) (2004) 445–458.

[27] K. Schwab. The Fourth Industrial Revolution, Crown Business. 2017.

[28] M. Sinclair. Comparison of the performance of modern heuristics for combinatoria optimization on real data, Computers and Operations Research 20 (1993) 687–695.

[29] SRI International, Global Impacts of FedEx in the New Economy, Technical Report, (2001).

[30] P.J. Van Laarhoven, E. Aarts, J. Lenstra, Job shop scheduling by simulated an nealing, Operations Research 40 (1) (1992) 113–125.

[31] C. Voudouris, E. Tsang, Guided local search and its application to the traveling salesman problem, European Journal of Operational Research 113 (1999) 469–499.

[32] D. Weyland, Simulated annealing, its parameter settings and the longest common subsequence problem, Proceedings of the 10th Annual Conference on Genetic and Evolutionary Computation (ACM) (2008) 803–810.

[33] M. Yagiura, T. Ibaraki, On metaheuristic algorithms for combinatorial optimization problems, Systems and Computers in Japan 32 (2001) 3–25.

[34] B. Yang, N. Burns, C. Backhouse, An empirical investigation into the barriers to postponement, International Journal of Production Research 43 (5) (2005) 991-1005

John W. Fowler is the Motorola Professor of Supply Chain Management in the W.P Carey School of Business at Arizona State University. He served as the department chair of supply chain management from 2011–2016. Prior to that, he was the Avnet Professor of Industrial Engineering at ASU. His research interests include supply chain management, discrete event simulation, deterministic scheduling, and multi-criteria decision making.

Seung-Hwan Kim is an associate professor of operations management in the department of Business Administration at Ajou University. Before joining Ajou University, he was a visiting assistant professor in the department of Business Administration at University of Illinois at Urbana-Champaign. He also worked as a business analyst in Amkor Technology, Chandler, AZ. His primary research interests include supply chain modeling and design, decision support systems for supply chain design, push-pull systems, and healthcare management.

Dan L. Shunk is a professor in the Industrial Engineering department at Arizona State University. He also is the PIMSA Chair at CETYS University in Baja, Calif., and an adjunct professor at the Polytechnic University of Milan in Como, Italy. He is the former director of the CIM Systems Research Center, which won the Society of Manufacturing Engineers (SME) LEAD Award as the best CIM research center in the world in 1990. He is currently pursuing research into global new product development, model-based enterprises and global supply network integration.
