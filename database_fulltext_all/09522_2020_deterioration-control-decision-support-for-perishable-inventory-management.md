---
otero_id: 9522
otero_key: "2F2R648J"
title: "Deterioration control decision support for perishable inventory management"
authors: "Ya Yang; Huihui Chi; Wei Zhou; Tijun Fan; Selwyn Piramuthu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113308"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deterioration control decision support for perishable inventory management

Ya Yang<sup>a,c</sup>, Huihui Chi<sup>b</sup>, Wei Zhou<sup>b,d</sup>, Tijun Fan<sup>a,⁎</sup>, Selwyn Piramuthu<sup>e</sup>

<sup>a</sup> Department of Management Science and Engineering, East China University of Science and Technology, Shanghai, China

<sup>b</sup> Department of Information & Operations Management, ESCP Europe, Paris, France

<sup>c</sup> Department of Management Science and Engineering, Qinghai University, Xining, China

<sup>d</sup> Department of Transportation Engineering, Shanghai Jiaotong University, Shanghai, China

<sup>e</sup> Department of Information Systems & Operations Management, University of Florida, USA

## A R T I C L E I N F O

Keywords: Decision support Perishable inventory management Deterioration-dependent demand Controlled deterioration rate

## A B S T R A C T

Deterioration rate is an important characteristic of perishable products. While deterioration in perishables is unavoidable, there are proven ways to lower their deterioration rates. Deterioration rate is commonly treated as an exogenous parameter in extant inventory management literature. We define deterioration rate as one of the controllable variables and propose a novel freshness-preservation efort (FPE) indicator. We consider perishable inventory management with FPE for deterioration control decision support. Our results show that there exists an optimal order quantity that minimizes total cost for a controlled deterioration scenario. The optimal FPE in dicator value and the optimal order quantity are investigated through numerical analysis. We perform sensitivity analysis and conclude with related managerial implications.

## 1. Introduction

Perishable products have high and varying deterioration rates when passing through their logistics system. Agri-fresh product is a typical example of perishable product that includes fresh fruits, fresh vegetables, and fresh meat. Uncontrolled deterioration leads to excessive spoilage-related waste. The loss ratio due to deterioration of fresh produce is as high as 30% in many countries [7]. In China, the annua loss of agricultural products amounts to more than US\$43 billion, which is equivalent to the production output of 0.1 billion hectares of cultivated land (China Economic Information Daily 2016). Given the above, it has become critically important to investigate the business integrated decision support mechanisms to efectively and eficiently control deteriorations in perishables logistics systems.

Recent technological advances ofer emerging technologies that can be used to efectively measure and control deterioration rate [6,24,27]. In general, deterioration rate (DR) determines the percentage of un saleable perishable products due to spoilage, contamination, damage, and expiration [2]. The DR of a perishable product varies according to the preservation environment and the product's intrinsic characteristics. For example, the DR of fresh fruits varies according to the storage environment and handling procedures. Harvested persimmon starts to darken after two or three days when kept at room temperature, but its freshness can be prolonged with storage in a temperature-controlled refrigerated environment. Blackburn and Scudder [3] show that the quality of an agri-fresh product worsens with increasing storage temperature due to expedited deterioration. It has been shown that the DRs of most perishable products remain stable under steady ambient conditions and start to vary when storage temperature and/or humidity fluctuate.

Perishable product deterioration rate has related consequences. Insofar as the deterioration rate of a perishable product is directly related to its quality, it has a concomitant efect on its consumer demand. An important characteristic of the quality of agri-fresh product, for example, is its freshness. Freshness of an agri-fresh product is generally determined through its appearance as proxy by its consumers [17]. When faced with the decision to choose between two similar agri-fresh items at the same price, consumers are likely to choose the one that appears fresher. Unlike other types of perishable products, there is a direct relationship between perceived agri-fresh product freshness and its DR. As the DR directly afects the freshness of an agri-fresh product, the lower the rate, the higher the freshness and the longer the agri-fresh product remains fresh. Meanwhile, consumers' willingness to buy agrifresh products is also afected by the shelf stock levels [4,5,8,21,25]. Sales at the retail level is proportional to the displayed stock. With these additional visual facets of an agri-fresh product's freshness and stock, the demand pattern and therefore inventory management of agri-fresh products are necessarily diferent from that of other perishable products.

As the DR of a perishable product can be controlled through appropriate storage and handling conditions, it should be considered a decision variable when conditions allow. The optimal inventory policy can thus be managed based on both deterioration-control and freshness dependent demand information. We propose a novel freshness-preservation efort (FPE) indicator to facilitate deterioration rate control. Clearly, any given controlled storage condition comes with an associated cost. However, investment in appropriate equipment and labor to provide necessary handling and storage conditions pays of through reduced loss of agri-fresh products due to controlled deterioration rate. The increased investment cost for better inventory storage and handling is justified by the reduced deterioration rate of agri-fresh products. While loss control is an important goal in agri-fresh product inventory management, cost considerations are a top priority for real-world retail decision makers.

This study contributes to the perishable inventory management system literature by considering DR as a decision variable and its efects on quality indicator of perishable products, associated market response, and a variable freshness-prolonging (operating) cost. We assume that the price is fixed and demand depends on quality deterioration within a given period. We further assume that the deterioration rate is controllable by freshness-preservation technology and efort at a variable cost. We then model the perishable inventory decision support system with deterioration-controlled/freshness-dependent demand, quality indication, and controllable DR to analyze its dynamics with various scalable parameters. We analytically model this scenario and perform sensitivity analysis to generate associated managerial implications.

Another contribution of this study is in the consideration of perishable product demand as being quality (freshness)-dependent. Specifically, we consider quality as the time-integration of initial quality and deterioration. For example, an agri-fresh product with low deterioration rate that appears fresher and with more displayed stock will attract higher demand. To the best of our knowledge, no existing work has considered DR to simultaneously afect freshness-dependent and stock-dependent demand, although the later has been extensively studied.

Our paper also makes contributions that industry practitioners can use, such as valuable managerial insights that are based on real-world settings. The choice of parameters that include 1) the value of the perishable product, 2) holding cost with preservation efort, and 3) quality-sensitive demand are all very important for the practitioner to make not only the classical decision on order quantity, but also the decision on quality (deterioration rate) control. Our simulated numerical analyses illustrate the dynamics of decisions under various condi tions and parameter choices.

The remainder of the paper is organized as follows. We briefly re. view related extant literature in the next section. We then build a model in which demand depends on the deterioration rate, which can be controlled, and derive model properties in Section 3. We analyze the decision-making steps and put forward managerial implications based on some cases in Section 4. In Section 5, we present our results that were generated through numerical analysis and associated sensitivity analysis. We provide a summary of this paper and conclude in Section 6.

## 2. Related literature

Researchers have studied various facets of perishable inventory management over the past few decades, with specific emphasis on quality degradation of perishables over time. As in any inventory management modeling exercise, demand can be modeled as either deterministic or stochastic. In the early years of research on perishable inventory management, demand was usually assumed to be either uniform and known in advance or a function of time. With linear function hypothesis as the basis, Ali et al. [1] consider demand to be a trapezoidal function of time, and propose a logic-based approach to deal with a class of perishable product inventory problem that allows out-of-stock situations. Some published studies on perishable inventory management focus on stock-dependent demand. For example, Chakraborty et al. (2015) assume that demand depends on stock, and study multi-variety supply chain integration models in fuzzy random environments. Tiwari et al. [25] consider the inventory replenishment strategy of a two-tier warehouse with stock-dependent demand assumption. Piramuthu and Zhou [21] assume that demand for agricultural product inventory depends on alloted shelf space and in stantaneous product quality. Some studies assume that demand is influenced by product price [18]. As the field matured, researchers developed perishable inventory models with stochastic demand and demand as a function with known mean and standard deviation values. Kopach et al. [16] consider red blood cell inventory management under Poisson distributed demand with known mean. Similar assumptions about Poisson distributed demand also appear in Chen et al. [10]. Muriana [19] considers the impact of demand fluctuations on the in ventory of deteriorating products under stochastic demand assumption. She develops an EOQ model by setting the identified shelf-life period as an explicit parameter. However, very few studies consider demand as being related to the deterioration rate of the product. The reality is that some perishables such as agri-fresh products exhibit deterioration rate dependent demand due to their quality characteristics.

Deterioration rate is an important factor that describes the realistic features of perishable products. Ghare and Schrader [14] first establish a diferential equation by taking into account constant deterioration rate. Chan et al. [9] propose production-inventory models by considering a constant deterioration rate. Singh et al. [22] assume that the deterioration rate is constant, and develop an inventory model for a manager to manage two stores. Some studies assume that the deterioration rate changes with time or follows a given distribution. Covert and Philip [11] and Philip [20] extend Ghare and Schrader's model with two-parameter and three-parameter Weibull distribution deterioration rate. Tadikamalla [23] discuss the same model with no backlogging and assume that deterioration time follows the Gamma distribution. Heterogeneous product quality with deterioration rate at diferent temperatures and diferent stages is considered by De Keizer et al. [12]. Although it hasn't been mentioned in the perishable logistics management literature, in many practical situations practitioners have treated deterioration rate as controlled by various preservation technologies. We assume DR to be controllable and model it as a decision variable.

Hsu et al. [15] consider investment in technology to reduce deterioration rate and present deteriorating inventory policies with optimal freshness preservation technology cost. Dye and Hsieh [13] explore the efect of investing in preservation technology to reduce deterioration rate by assuming that the cost of preservation technology is a function of the length of the replenishment cycle. Tsao [26] designs a supply chain for perishable items by considering trade credit and preservation eforts that directly afect deterioration rate of the perishables. How ever, the freshness preservation eforts are only assumed to lower deterioration rate without afecting demand. Cai et al. [7] study the coordination of a fresh product supply chain by proposing models that determine the best tradeof between associated costs and benefits, and consider the preservation efort with upper and lower bounds as a decision variable. Although Cai et al. [7] allude to the fact that freshness and demand are afected by eforts to keep the products fresh, they do not consider inventory management with controllable deterioration rate or freshness-dependent demand.

In summary, we study deterioration-controlled/freshness-dependent demand that extends the existing freshness-dependent and stockdependent demand based perishable management research by considering deterioration rate as one of the decision variables. Although deterioration rate has been commonly controlled in practice, it has not been studied in the perishable management literature.

## 3. Deterioration-controlled/quality-dependent perishable retailing model

## 3.1. Notation & assumptions

We consider a deterioration rate controllable perishable inventory system with quality-dependent demand. We minimize total cost based on adjustable deterioration rate and investigate its efects on other in ventory policy parameters that include order quantity and order period. We formulate the inventory management problem with the following notation in Table 1.

A represents the fixed ordering cost. A is a product-specific constant, so we assume that an order with a specific preserved product type involves higher ordering cost A. For example, some high value products are associated with high $A ,$ such as live lobster in the seafood sector. High A is generally associated with a higher $h _ { 0 } ,$ e.g., the highest possible efort to preserve live lobster vs packaged apple. We consider A a constant for a specific type of perishable product. Decision variable $h _ { \theta }$ represents the actual controllable holding cost with preservation, with the highest possible value to be $h _ { \theta } ~ < ~ h _ { 0 }$

This signifies that the maximum rational preservation efort of a retailer is pre-determined by the initial freshness of the products in each order. It involves the cost of using pre-allocated advanced preservation devices. Once the maximum capability of preservation $h _ { 0 }$ is fixed, the retailer must decide the operational preservation efort (h ) that corresponds to a controlled deterioration rate θ. Later, we define an indicator of freshness preservation efort (FPE) to be $\begin{array} { r } { \gamma = h _ { \theta } / h _ { 0 } , } \end{array}$ to simplify the calculation. The range of deterioration rate θ is from 0 to 1. When the deterioration rate is close to 0, h<sub>θ</sub> approaches the maximum preservation capacity $h _ { 0 } .$ The holding cost with preservation efort, $h _ { \theta } ,$ directly results in the expected deterioration rate by allocating required labor cost, equipment cost, and other operational costs. h represents the maximum possible efort of $h _ { \theta } , h _ { \theta } ~ < ~ h _ { 0 }$ . When $h _ { \theta }  h _ { 0 }$ the deterioration rate is minimized. Because $h _ { 0 }$ is the upper limit of $h _ { \theta } ,$ h represents the “maximum possible freshness preservation cost”. The deterioration rate is very low when the firm exercises full efort to preserve the product, such that $h _ { \theta }  h _ { 0 } .$ In this case, the product quality is maintained at its highest level. Because preservation involves the usage of storage devices, preservation equipment, more power consumption, and human labor, the holding cost is associated with the quality indicator. As a result, we assume both $h _ { \theta }$ and $h _ { 0 }$ to be cost per item unit, per time unit.

Q/T and θ are the decision variables that respectively represent the order quantity/period and controllable deterioration rate. We consider both market demand and inventory loss due to product deterioration. We assume that the deterioration rate θ is controlled by adjusting storage and preservation condition at a cost of $h _ { \theta } .$ For example, lower

## Table 1

Notation list.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\theta$ </td><td>deterioration rate.  $0 < \theta < 1$ </td></tr><tr><td> $Q$ </td><td>batch (order) quantity</td></tr><tr><td> $T$ </td><td>the time interval between two orders</td></tr><tr><td> $D_0$ </td><td>fixed demand rate</td></tr><tr><td> $D$ </td><td>total demand per time unit</td></tr><tr><td> $\beta$ </td><td>coefficient of change in demand caused by quality, demand-on-quality variable.  $\beta > 0$ </td></tr><tr><td> $I(t)$ </td><td>inventory level at time  $t$ </td></tr><tr><td> $A$ </td><td>fixed cost per order</td></tr><tr><td> $c$ </td><td>acquisition cost per unit</td></tr><tr><td> $h$ </td><td>constant holding cost per unit and per time unit</td></tr><tr><td> $h_0$ </td><td>maximum holding cost with preservation, per unit and per time unit</td></tr><tr><td> $h_\theta$ </td><td>controllable marginal holding cost with preservation.  $0 < h_\theta < h_0$ </td></tr><tr><td> $\gamma$ </td><td>freshness-preservation effort (FPE) indicator.  $\gamma = h_\theta/h_0, 0 < \gamma < 1$ </td></tr><tr><td> $\alpha$ </td><td>deterioration rate preservation factor,  $\alpha > 0$ </td></tr><tr><td> $TC$ </td><td>total cost per time unit</td></tr></table>

storage temperature with proper humidity control can slow down the degradation of an agri-fresh product through lowered deterioration rate. Diferent levels of θ are directly related to the controllable marginal holding cost $h _ { \theta } .$ Therefore, θ and $Q / T$ directly impact the global optimal inventory decision.

We assume that a batch of size Q is delivered at order placement time. The inventory level decreases only due to demand fulfillment and deterioration loss. We assume that shrinkage [28,29] is absent. When inventory level reaches zero, a new batch of size Q is ordered. As is common in related literature, we also assume the following: (1) replenishment rate is infinite and lead time is zero; (2) no shortages are allowed. With today's technologies, it is a realistic assumption as more and more retailers adopt RFID/IoT and sensor network that provide real-time shelf/inventory information to address out-of-stock situations, in addition to the provision of other valuable information/functions.

The marginal cost incurred to control the storage environmental condition is $h _ { \theta } \left( h _ { \theta } > 0 \right) . h _ { 0 }$ represents the maximum possible freshness preservation cost that also sets an upper limit on $h _ { \theta } .$ . Note that $h _ { 0 }$ represents the ideal situation where $h _ { \theta } \ < \ h _ { 0 } .$ Because the deterioration rate is an index ranging from 0 and 1, from the operational point of view, we propose a novel operable freshness-preservation efort (FPE) indicator, which is defined as $\gamma = h _ { \theta } / h _ { 0 }$ to facilitate deterioration rate control. The higher the $\gamma ,$ the lower the deterioration rate of the perishable product that results in keeping the product fresh for a longer time. Cai et al. [7] model the influence of freshness preservation efort on freshness as a Power Function. With the consideration that the deterioration rate and the freshness of agri-fresh product move in opposite directions, we model the controllable deterioration rate function as

$$
\theta = 1 - \gamma^ {\frac {1}{\alpha}}\tag{1}
$$

Here, α $( \alpha ~ > ~ 0 )$ is the relationship coeficient between deterioration rate and freshness preservation efort. The FPE indicator γ and the controllable marginal cost are represented respectively as given in Eqs. (2) and (3).

$$
\gamma = (1 - \theta) ^ {\alpha}\tag{2}
$$

$$
h _ {\theta} = h _ {0} (1 - \theta) ^ {\alpha}\tag{3}
$$

Eq. (2) implies that a decreasing deterioration rate in general requires an increasing freshness preservation efort cost. When the deterioration rate is minimized as $\theta  0 ,$ γ approaches 1 and $h _ { \theta }$ approaches $h _ { 0 } .$ Similarly, when the deterioration rate is maximized as $\theta  1$ 1, γ approaches 0 and $h _ { \theta }$ approaches 0.

We assume that demand depends on the perishable product quality, which in turn depends on its deterioration rate. This assumption is based on the observation that consumers are more likely to choose the freshest product available when they are ofered, at the same price, a choice among products that exhibit diferent freshness levels. A customer's willingness to buy agri-fresh products is also afected by shelf stock levels, as more displayed stock attracts more demand. Moreover, deterioration rate largely determines the shelf stock level since deteriorated products will likely be removed from the shelves. Thus, we formulate demand rate as

$$
D = D _ {0} - \beta \theta\tag{4}
$$

where $D _ { 0 }$ is the fixed demand rate, $\beta \left( \beta > 0 \right)$ is the demand-on-quality variable, and $D = 0$ when $D _ { 0 } - \beta \theta \leq 0 .$

Customers perceive product quality as the result of a certain dete rioration rate. For example, once spots begin to appear on a banana, customers know that its deterioration rate is bound to increase soon thereafter. Similarly, once yellowing begins to appear on a broccoli top, its deterioration rate only increases from that point on. Secondly, for packaged agri-fresh products, customers subconsciously observe their quality from the stock display that is the direct time-integration of deterioration rate. As a result, demand can be expressed directly through the deterioration rate.

![](/api/attachments/2F2R648J/fulltext/images/a8b4f9654a2856f633e2bf3ce37c16028a58d8b1f11ae530edc061de1edd76f7.jpg)  
Fig. 1. Development of inventory level over time.

## 3.2. Model & properties

Fig. 1 shows the development of inventory level over time. The order quantity varies under diferent deterioration rate conditions. The inventory level decreases due to both demand and product deterioration in each order cycle. The diferential equation representing the in ventory level is given in Eq. (5).

$$
\frac {d I (t)}{d t} = - \theta I (t) - (D _ {0} - \beta \theta), 0 \leq t \leq T\tag{5}
$$

where the boundary conditions are $I ( 0 ) = Q$ and $I ( T ) = 0 { }$ . Solving Eq. (5) for inventory over time yields Eqs. (6) and (7).

$$
I (t) = \frac {D _ {0} - \beta \theta}{\theta} [ e ^ {\theta (T - t)} - 1 ], \quad 0 \leq t \leq T\tag{6}
$$

$$
Q = \frac {D _ {0} - \beta \theta}{\theta} (e ^ {\theta T} - 1)\tag{7}
$$

The total relevant cost per cycle consists of ordering cost $A ,$ holding cost $H C _ { \theta } ,$ and deterioration cost $D C _ { \theta }$ as listed in Table 2. In addition, we consider the following two parts of the perishable inventory holding cost. The first part is the constant holding cost, $h ,$ which includes physical storage cost and opportunity cost. The second part is the freshness preservation cost, $h _ { \theta } ,$ that is incurred to control the storage condition.

Both $H C _ { \theta }$ and $D C _ { \theta }$ benefit from smaller reorder quantities that correspond to high average ordering cost. The higher freshness preservation cost, due to lower deterioration rate, increases the constant holding cost and decreases $D C _ { \theta } .$ The total relevant inventory cost, $\mathrm { T C } ,$ is formulated as Eq. (8).

$$
\begin{array}{r l} {T C (\theta , T)} & {= \frac {A + H C _ {\vartheta} + D C _ {\vartheta}}{T}} \\ & {= \frac {A + c Q + [ h + h _ {0} (1 - \theta) ^ {\alpha} ] \int_ {0} ^ {T} I (t) d t}{T} - c (D _ {0} - \beta \theta)} \\ & {= \frac {A}{T} + \frac {1}{T} [ h + c \vartheta + h _ {0} (1 - \theta) ^ {\alpha} ] \bigg [ \frac {1}{\theta} (e ^ {\vartheta T} - 1) - T \bigg ] \frac {D _ {0} - \beta \theta}{\theta}} \end{array}\tag{8}
$$

We approximate the exponential function by the first three terms of the Taylor series and obtain Eq. (9).

$$
T C (\theta , T) = \frac {A}{T} + [ h + c \theta + h _ {0} (1 - \theta) ^ {\alpha} ] \frac {D _ {0} - \beta \theta}{2} T\tag{9}
$$

The necessary conditions $( \mathrm { N C } )$ for the total relevant cost in Eq. (9) to be minimum are $\begin{array} { r } { \frac { \partial T C ( \hat { \varrho } , T ) } { \partial \hat { \varrho } } = 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial T } = 0 } \end{array}$ as shown below.

Table 2  
Cost structure notation.

<table><tr><td>Notation</td><td>Formula</td><td>Description</td></tr><tr><td>A</td><td></td><td>Ordering cost</td></tr><tr><td> $HC_{\theta}$ </td><td> $= [h + h_0(1 - \theta)^{\alpha}] \int_0^T I(t)dt$ </td><td>Constant and marginal holding cost</td></tr><tr><td> $DC_{\theta}$ </td><td> $= c[Q - \int_0^T (D_0 - \beta\theta)dt]$ </td><td>Deterioration cost</td></tr></table>

$$
\frac {\partial T C}{\partial \theta} = \frac {T}{2} [ [ c - h _ {0} \alpha (1 - \theta) ^ {\alpha - 1} ] (D _ {0} - \beta \theta) - [ h + c \theta + h _ {0} (1 - \theta) ^ {\alpha} ] \beta ] = 0\tag{10}
$$

$$
\frac {\partial T C}{\partial T} = - \frac {A}{T ^ {2}} + [ h + c \theta + h _ {0} (1 - \theta) ^ {\alpha} ] \frac {D _ {0} - \beta \theta}{2} = 0\tag{11}
$$

For a fixed θ value, the optimal T value is determined by Eq. (11). Theorem 1. For any given $\theta \in ( 0 , 1 ) ,$ , the total cost is convex and attains its minimum at $T ^ { * } { } _ { ; }$ , where

$$
T ^ {*} = \sqrt {\frac {2 A}{[ h + c \theta + h _ {0} (1 - \theta) ^ {\alpha} ] (D _ {0} - \beta \theta)}}\tag{12}
$$

and the optimal order quantity is

$$
Q ^ {*} = \sqrt {\frac {2 A (D _ {0} - \beta \theta)}{h + c \theta + h _ {0} (1 - \theta) ^ {\alpha}}}\tag{13}
$$

the optimum minimum cost is

$$
T C ^ {*} = \sqrt {2 A [ h + c \theta + h _ {0} (1 - \theta) ^ {\alpha} ] (D _ {0} - \beta \theta)}\tag{14}
$$

$\begin{array} { r } { \operatorname { P r o o f . } \quad \operatorname { F o r } \quad \mathrm { a n y } \quad \mathrm { g i v e n } } \\ { T ^ { * } = \sqrt { \frac { 2 A } { [ h + c \theta + h _ { 0 } ( 1 - \theta ) ^ { \alpha } ] ( D _ { 0 } - \beta \theta ) } } } \end{array}$ can be solved according to Eq. (11). We $\theta \in ( 0 , 1 ) .$ , the optimal cycle time then derive the optimal order quantity as given in Eq. (13) with the substitution of $T ^ { * }$ in Eq. (7). Furthermore, we check the second derivative $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial T ^ { 2 } } = \frac { 2 A } { T ^ { 3 } } > 0 , } \end{array}$ which indicates that this point corresponds to the minimum of the total cost function. Hence, the optimal minimum cost $T C ^ { * }$ , which is shown in Eq. (14), can be derived after bringing $T ^ { * }$ back to Eq. (9).

The above analysis indicates that, for any given marginal holding cost related to freshness preservation, the order quantity $Q ^ { * }$ that minimizes the total cost not only exists but is also unique.

Theorem 2. For any given $T ,$ the $\theta \in ( 0 , 1 )$ )that satisfies $\sum _ { i = 0 } ^ { i = \alpha } b _ { i } \theta ^ { i } = 0$ and $\sum _ { . } ^ { i = \alpha } i b _ { i } \theta ^ { i - 1 } > 0$ , where $b _ { i } ( i = 0 , . . . , \alpha )$ are corresponding coeficients of =i 1 the $\theta ^ { i } ,$ , is the optimal solution that minimizes the total cost.

Proof. The first derivative of the cost function Eq. (10) with fixed $T$ can be written in the following form: $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial \theta } = T \bar { \sum } _ { i = 0 } ^ { i = \alpha } } \end{array}$ b <sup>i</sup> , where $b _ { i }$ $( i \ : = \ : 0 , . . . , \alpha )$ are corresponding coeficients of θ<sup>i</sup>. The optimal deterioration rate $\theta ^ { \ast } \left( \theta ^ { \ast } \in \left( 0 , 1 \right) \right)$ satisfies $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial \theta } = T \sum _ { i = 0 } ^ { i = \alpha } \ \hat { b } _ { i } \theta ^ { i } = 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } = T \sum _ { i = 1 } ^ { i = \alpha } i b _ { i } \theta ^ { i - 1 } > 0 } \end{array}$ . Since T is the cycle time, it must be nonnegative. So, we have $\sum _ { i = 0 } ^ { i = \alpha } b _ { i } \theta ^ { i } = 0 \mathrm { ~ a n d ~ } \sum _ { i = 1 } ^ { i = \alpha } i b _ { i } \theta ^ { i - 1 } > 0 .$

When the freshness-preservation effort is up, it lowers the deterioration rate, which in turn decreases costs associated with deterioration such as lower interest from consumers and ultimately the loss of the product. Such an efort necessarily increases the marginal holding cost and the total constant holding cost also increases due to the increased demand that is a direct result of lowered deterioration rate. This signifies that when the increased total holding cost is less than the decreased cost due to lower deterioration rate, the freshness preservation efort is cost-efective.

## 4. Discussion on diferent α values

$\theta = 1 - \gamma ^ { \frac { 1 } { \alpha } }$ signifies that the deterioration rate is controlled not only by freshness-preservation efort but also by the deterioration rate pre servation factor. Note that under similar storage environments and the same preservation efort, the deterioration rates of diferent agri-fresh products will not be the same because of their diferent inherent perishability characteristics. Diferent agri-fresh products have diferent factor values. Deterioration rate is a decision variable in our model. For a given agri-fresh product (a given α), if the optimal deterioration rate is known, the freshness-preservation efort indicator for controlling the deterioration rate can be determined from Eq. (2).

For simplicity, we assume that the deterioration rate is almost 1 when we do nothing to preserve product freshness. Clearly, deterioration rates for diferent products are not the same even under the same freshness preservation condition. The relationship coeficient between deterioration rate and preservation efort takes diferent values for diferent products. For instance, with the same freshness preservation efort and the same preservation cost, the deterioration rate for bananas is diferent from the deterioration rate for apples. Table 3 illustrates this, where α is as in Eq. (1) and we set the FPE indicator at 0.5.

The higher the $\alpha ,$ the lower the deterioration rate as shown in Table 3. A perishable product with small α is more prone to spoilage. As a result, $0 ~ < ~ \alpha ~ < ~ 1$ represents scenarios where the perishable char acteristics are more salient than when $\alpha = 1$

Fig. 2 shows the efect of increasing α on optimal deterioration rate and optimal cycle time. As can be seen, a sudden change occurs at $\alpha = 1$ . We also observe that $\boldsymbol { \theta } ^ { * }$ and $T ^ { * }$ are very sensitive when $\alpha \ < \ 1$ and are gentle when $\alpha \ > \ 1$

To ensure the robustness of Eq. (1) and other expressions that are based on Eq. (1) against variations in α values, the range of α could be limited to $[ 1 , + \infty )$ . We therefore discuss the optimal deterioration rate only for $\alpha = 1$ and $\alpha > 1$ in the remainder of this paper. We conclude this section with some general managerial implications.

## 4.1. α = 1: Decision-making steps

The second derivative of total cost with respect to θ is

$$
\frac {\partial^ {2} T C (\theta , T)}{\partial \theta^ {2}} = \frac {T}{2} [ - 2 \beta c + 2 \beta h _ {0} \alpha (1 - \theta) ^ {\alpha - 1} + (D _ {0} - \beta \theta) h _ {0} \alpha (\alpha - 1) (1 - \theta) ^ {\alpha - 2} ]\tag{15}
$$

The complexity of the above expression renders it dificult to judge whether it is positive or negative. Note that when α = 1, Eq. (15) can be simplified to

$$
\frac {\partial^ {2} T C (\theta , T)}{\partial \theta^ {2}} = \frac {T}{2} [ 2 \beta (h _ {0} - c) ]\tag{16}
$$

The above expression allows for simpler evaluation of the optimal solution.

Theorem 3. When $\alpha = 1$ and $c \leqslant h _ { 0 } .$ , the optimal deterioration rate is $\theta ^ { * } \to 1$ , the corresponding optimal order quantity is $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A ( D _ { 0 } - \beta ) } { h + c } } } \end{array}$ , and the optimal cycle time is $\begin{array} { r } { T ^ { * } = \sqrt { \frac { 2 A } { ( h + c ) ( D _ { 0 } - \beta ) } } . } \end{array}$

Proof. When $\begin{array} { r l r } { \alpha } & { { } \quad = \quad } & { 1 , \quad \quad \frac { \partial T C } { \partial \theta } = \frac { T } { 2 } [ ( c - h _ { 0 } ) ( D _ { 0 } - \beta \theta ) - } \end{array}$ $\begin{array} { r } { ( h + c \theta + h _ { 0 } ( 1 - \theta ) ) \beta ] = \frac { T } { 2 } [ ( D _ { 0 } - 2 \beta \theta ) ( c - h _ { 0 } ) - \beta ( h + h _ { 0 } ) ] } \end{array}$ . Note that when $\begin{array} { r } { c \leqslant h _ { 0 } , \frac { \partial T C ( \theta , T ) } { \partial \theta } } \end{array}$ would always be negative, which signifies that the first derivative cannot be zero. Therefore. the total cost decreases with θ and its associated optimal fixed order quantity, $\theta ^ { * } \to 1$ . The best decision for the retailer is to do nothing to preserve the product. So, we have $h _ { \theta }  0 ,$ , the optimal FPE indicator $\gamma ^ { * }  0$ , with the corresponding optimal order quantity and cycle time respectively given by $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A ( D _ { 0 } - \beta ) } { h + c } } } \end{array}$ and $\begin{array} { r } { T ^ { * } = \sqrt { \frac { 2 A } { ( h + c ) ( D _ { 0 } - \beta ) } } } \end{array}$

Table 3  
Deterioration rates for diferent α.

<table><tr><td> $\alpha$ </td><td>...</td><td> $\frac{1}{3}$ </td><td> $\frac{1}{2}$ </td><td>1</td><td>2</td><td>3</td><td>...</td></tr><tr><td> $\theta$ </td><td>...</td><td>0.875</td><td>0.750</td><td>0.500</td><td>0.293</td><td>0.206</td><td>...</td></tr></table>

![](/api/attachments/2F2R648J/fulltext/images/a0c341d3aa2f1ec1627fd2daadba3bc33750f76c10986ccfd82b6b6924e0ae77.jpg)  
Fig. 2. Efect of increasing α on $\theta ^ { * }$ and $T ^ { * } .$

On the other hand, when $\alpha = 1$ and $c \ > \ h _ { 0 } ,$ the value of $\theta$ (recorded as $\theta _ { N C } )$ can be derived from Eq. (10):

$$
\theta_ {N C} = \frac {D _ {0}}{2 \beta} - \frac {h + h _ {0}}{2 (c - h _ {0})}\tag{17}
$$

With $\begin{array} { r } { \frac { \partial ^ { 2 } T C } { \partial \theta ^ { 2 } } = \frac { T } { 2 } [ 2 \beta ( h _ { 0 } - c ) ] < 0 . } \end{array}$ , the cost function follows a saddle face. It is easy to guess that the optimal deterioration rate will be 0 or 1. More specific analysis with $\alpha \ : = \ : 1$ as a simplified example is given below.

Here we let α = 1 and discuss diferent cases based on $c > h _ { 0 }$ when the deterioration rate boundary is considered.

Theorem 4. When $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 . } \end{array}$ , the optimal deterioration rate is ${ \theta } ^ { * }  0 ,$ , the corresponding optimal order quantity is $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A D _ { 0 } } { h + h _ { 0 } } } } \end{array}$ , and the optimal cycle time is $\begin{array} { r } { T ^ { * } = \sqrt { \frac { 2 A } { D _ { 0 } ( h + h _ { 0 } ) } } . } \end{array}$

Proof. $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 } \end{array}$ is beyond the deterioration rate range. Hence, the optimal solution can't equal $\theta _ { N C } ,$ and must be determined through other ways. We first focus on the partial derivative of the total cost function $\begin{array} { r } { \frac { \widehat { \partial T } C ( \theta , T ) } { \partial \theta } = \frac { T } { 2 } [ ( D _ { 0 } - 2 \beta \theta ) ( \widehat { c } - h _ { 0 } ) - \beta ( h + h _ { 0 } ) ] } \end{array}$ when $\alpha = 1$ , which indicates that the total cost function is a linear function of θ if quantity (cycle time) is determined. As a result, if the slope of this line is positive, then the optimal value is at ${ \theta } ^ { * }  0 ,$ , which is equivalen to $\gamma ^ { * }  1$ . Otherwise, the optimal value is at $\theta ^ { * } \to 1$ , which is equivalent to $\gamma ^ { * }  0$

Because $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 } \end{array}$ , we have $( D _ { 0 } - 2 \beta ) ( c - h _ { 0 } ) \geqslant \beta ( h + h _ { 0 } )$ . If we bring back T<sup>∗</sup> into Eq. (10), with $c \ > \ h _ { 0 }$ we observe that

$$
\frac {\partial T C (\theta , T ^ {*})}{\partial \theta} > \frac {T ^ {*}}{2} [ (D _ {0} - 2 \beta) (c - h _ {0}) - \beta (h + h _ {0}) ] \geqslant 0
$$

which implies that the slope is always positive. Therefore, the total cost increases with θ and its associated optimal fixed order quantity in this case, $\theta ^ { * } \to 0$ . The best decision for the retailer is to try the best preservation ability to keep the product fresh. So, we have $h _ { \theta }  h _ { 0 } ,$ then the FPE indicator is $\gamma ^ { * }  1$ . From Theorem 1, the corresponding optimal order quantity and optimal cycle time respectively are $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A D _ { 0 } } { h + h _ { 0 } } } } \end{array}$ and $\begin{array} { r } { T ^ { * } = \sqrt { \frac { 2 A } { D _ { 0 } ( h + h _ { 0 } ) } } . } \end{array}$

Theorem 5. When $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \leqslant 0 , } \end{array}$ , the optimal deterioration rate is $\theta ^ { * } \to 1$ , the corresponding optimal order quantity is $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A ( D _ { 0 } - \beta ) } { h + c } } } \end{array}$ \* 4 and the optimal cycle time is $\begin{array} { r } { T ^ { * } = \sqrt { \frac { 2 A } { ( h + c ) ( D _ { 0 } - \beta ) } } . } \end{array}$

Proof. With similar consideration as before, from $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \leqslant 0 } \end{array}$ we obtain $D _ { 0 } ( c \mathrm { ~ - ~ } h _ { 0 } ) \leqslant \beta ( h \mathrm { ~ + ~ } h _ { 0 } )$ . The partial derivative of total cost

$$
\frac {\partial T C (\theta , T ^ {*})}{\partial \theta} <   \frac {T ^ {*}}{2} [ D _ {0} (c - h _ {0}) - \beta (h + h _ {0}) ] \leqslant 0
$$

implies that the slope is always negative. Therefore, total cost decreases with θ and its associated optimal fixed order quantity in this case, $\theta ^ { * } \to$ 1. The best decision for the retailer is to do nothing to preserve the freshness of the product. So, we have $h _ { \theta }  0 ,$ , and the FPE indicator is $\gamma ^ { * }  0 .$ . From Theorem 1, the corresponding optimal order quantity and optimal cycle time respectively are $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A ( D _ { 0 } - \beta ) } { h + c } } } \end{array}$ and $\begin{array} { r } { T ^ { \ast } = \sqrt { \frac { 2 A } { ( h + c ) ( D _ { 0 } - \beta ) } } . } \end{array}$

The expressions for $T ^ { * }$ and $Q ^ { * }$ in Theorems 4 and 5 are similar to each other. The obvious diference is that the former has no deterioration cost term and the latter has no marginal holding cost term. Theorem 4 indicates that there exists a threshold condition, exceeding which the practitioner should exercise full efort to preserve the per ishable products in order to achieve minimum deterioration. It normally applies to high value products. Theorem 5 indicates the lower condition below which the practitioner should not try to preserve the product. It generally applies to low value products. This threshold condition. defined by Eq. (17). is therefore value-driven based on $D _ { 0 } , \beta ,$ $h , h _ { 0 }$ and c. It specifies several conditions that practitioners may use to derive insights. For example, when the fixed demand rate is very high $\begin{array} { r } { ( D _ { 0 } > \frac { 2 } { \beta } \bigg ( 1 + \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \bigg ) ) } \end{array}$ ), the total deterioration cost would be very high if preservation efort is not high. On the other hand, if $\begin{array} { r } { D _ { 0 } < \frac { h + h _ { 0 } } { \beta ( c - h _ { 0 } ) } } \end{array}$ , there is no need for preservation efort. This result is stated in Theorem 5.

Theorem 6. When $\begin{array} { r } { 0 < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 } \end{array}$

(1) $\begin{array} { r } { \theta _ { N C } = \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } , Q _ { N C } = \sqrt { \frac { 2 A \beta } { c - h _ { 0 } } } } \end{array}$ is not the global optimal so lution;

Proof. (1) When $\begin{array} { r } { 0 < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 } \end{array}$ , the necessary conditions for minimum total cost are $\begin{array} { r } { \widehat { \Theta } _ { N C } = \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } } \end{array}$ and $\begin{array} { r } { Q _ { N C } = \sqrt { \frac { 2 A \beta } { c - h _ { 0 } } } } \end{array}$ $\begin{array} { r } { \bigg ( T _ { N C } = \frac { 2 } { D _ { 0 } ( c - h _ { 0 } ) + \beta ( h + h _ { 0 } ) } \sqrt { 2 A \beta ( c - h _ { 0 } ) } \bigg ) } \end{array}$ . Furthermore, at $( \theta _ { N C } , Q _ { N C } /$ ${ \dot { T } } _ { N C } ) ,$ , a local minimum should satisfy the condition that the Hessian matrix

$$
[ H ] = \left[ \begin{array}{c c} \frac {\partial^ {2} T C (\theta , T)}{\partial \theta^ {2}} & \frac {\partial^ {2} T C (\theta , T)}{\partial \theta \partial T} \\ \frac {\partial^ {2} T C (\theta , T)}{\partial T \partial \theta} & \frac {\partial^ {2} T C (\theta , T)}{\partial T ^ {2}} \end{array} \right] _ {(\theta_ {N C}, T _ {N C})}
$$

is positive. Note that $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } \bigg | _ { ( \theta _ { N C } , T _ { N C } ) } = - T _ { N C } \beta ( c - h _ { 0 } ) < 0 , } \end{array}$ $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial T ^ { 2 } } \bigg | _ { ( \theta _ { N C } , T _ { N C } ) } = \frac { 2 A } { T _ { N C } ^ { 3 } } > 0 , } \end{array}$ , and the value of the Hessian matrix should be $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial T ^ { 2 } } - \left( \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta \partial T } \right) ^ { 2 } \bigg | _ { ( \theta _ { N C } , T _ { N C } ) } = , } \end{array}$ which indicates $- \frac { 1 } { \lambda } [ D _ { 0 } ( c - h _ { 0 } ) + \beta ( h + h _ { 0 } ) ] < 0$

that $( \theta _ { N C } , T _ { N C } / \dot { Q } _ { N C } )$ is a saddle point.

(2) From above proof we know that although T<sup>∗</sup> can be determined with a fixed $\theta ^ { * } , \theta ^ { * }$ can't equal $\theta _ { N C }$ because $\frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } < 0 . \theta _ { N C }$ is a maximum cost point. The farther away from this point, the smaller the total cost and the best deterioration rate must approach 0 or 1, i.e. $\gamma ^ { * }  1$ or $\gamma ^ { * }  0$

Theorem 6 considers the scenario that is in-between the two extreme conditions. The firm can choose the corresponding management procedure according to their actual management conditions. Theorem 6 shows that when $\begin{array} { r } { 0 < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 } \end{array}$ , there exist some points at which the total cost approaches its maximum with a fixed $\boldsymbol { Q } / T .$ TC increases with increasing θ when $\begin{array} { r } { \theta < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } ; } \end{array}$ TC decreases with increasing θ when $\begin{array} { r } { \theta > \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } . } \end{array}$ . Therefore, except $\begin{array} { r } { \theta _ { N C } = \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } , } \end{array}$ , there must be two equal total costs at two diferent θ. This signifies that sometimes we can reduce waste under the same controlled-cost requirements.

In summary, when $\alpha = 1$ and $c > h _ { 0 } ,$ the segmental optimal rate of deterioration that minimizes total cost is

$$
\theta^ {*} \to \left( \begin{array}{c c} 0 & \frac {D _ {0}}{2 \beta} - \frac {h + h _ {0}}{2 (c - h _ {0})} \geqslant 1 \\ 0 o r 1 & 0 <   \frac {D _ {0}}{2 \beta} - \frac {h + h _ {0}}{2 (c - h _ {0})} <   1 \\ 1 & \frac {D _ {0}}{2 \beta} - \frac {h + h _ {0}}{2 (c - h _ {0})} \leqslant 0 \end{array} \right)\tag{18}
$$

The above results can help a retailer with related decision support (Table 4) in three steps. In the first step, we compare the purchasing cost with the maximum holding cost that is related to freshness preservation. $\operatorname { I f } c \leqslant h _ { 0 } ,$ the optimal FPE indicator is 0. If $c > h _ { 0 } ,$ , we must examine the value of $\begin{array} { r } { \frac { \mathbf { \hat { D } } _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } } \end{array}$ , which is the second step. If $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 . } \end{array}$ , the optimal FPE indicator approaches 1; if $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \leqslant 0 . } \end{array}$ , the optimal FPE indicator is 0; $\begin{array} { r } { \mathbf { f } \mathbf { 0 } < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 _ { : } } \end{array}$ we move on to the third step. The third step involves further calculation of the total cost when $\theta  0 \mathrm { o r } \theta  1$ , and the retailer selects the lower value. In addition, we can simplify $T C _ { \theta \to 1 } ~ < ~ T C _ { \theta \to ( }$ <sub>0</sub> as $\begin{array} { r } { \frac { \beta } { D _ { 0 } } > \frac { c - h _ { 0 } } { c + h } } \end{array}$ and $T C _ { \theta  1 } \geqslant T C _ { \theta  0 }$ is equivalent $\begin{array} { r } { \mathbf { t o } \ \frac { \beta } { D _ { 0 } } \leqslant \frac { c - h _ { 0 } } { c + h } . } \end{array}$

As long as the optimal FPE indicator is 0, the corresponding optimal order quantity is $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A ( D _ { 0 } - \beta ) } { h + c } } } \end{array}$ and the minimum total cost is $T C ^ { * } = \sqrt { 2 A ( D _ { 0 } - \beta ) ( h + c ) }$ . When the optimal FPE indicator approaches $^ { 1 , }$ the corresponding optimal order quantity and minimum total cost respectively are $\begin{array} { r } { Q ^ { * } = \sqrt { \frac { 2 A D _ { 0 } } { h + h _ { 0 } } } } \end{array}$ and $T C ^ { * } = \sqrt { 2 A D _ { 0 } ( h + h _ { 0 } ) }$

When $c \leqslant h _ { 0 } ,$ the optimal decision is to do nothing to preserve the freshness of the product. The reason is that the deterioration cost is lower than the maximum holding cost related to freshness preservation, so that the additional cost (for lowering deterioration rate) is not incurred when nothing is done to keep the product fresh. When measures are taken to preserve product freshness, the total cost will increase because the increased holding cost is more than the decreased deterioration cost. This phenomenon is also observed in real-life circumstances - if the product is really cheap, are we willing to spend more to preserve its freshness? When $c \ > \ h _ { 0 } ,$ the situation is more complex.

Table 4 shows that the key determinants for the retailer's decision are the relative values of c and $h _ { 0 } .$ . As a reflection of the maximum product freshness preservation capability, the value of $h _ { 0 }$ is afected by $A _ { \theta } .$ More investment brings better storage conditions, that is, larger $A _ { \theta }$ has the larger $h _ { 0 } .$ We assume that the ordering cost $A _ { \theta }$ is constant. We leave consideration of the impact of changing ordering cost and changing maximum product freshness preservation capability for a future study.

Decision-making steps $( \alpha = 1 ) .$

<table><tr><td colspan="6">Decision-making steps (d-1).</td></tr><tr><td>Step 1</td><td>c ≤h0</td><td>c &gt; h0</td><td></td><td></td><td></td></tr><tr><td>Step 2</td><td></td><td> $\frac{D_0}{2\beta} - \frac{h + h_0}{2(c - h_0)} \geqslant 1$ </td><td> $\frac{D_0}{2\beta} - \frac{h + h_0}{2(c - h_0)} \leqslant 0$ </td><td>0 &lt;  $\frac{D_0}{2\beta} - \frac{h + h_0}{2(c - h_0)} < 1$ </td><td></td></tr><tr><td>Step 3</td><td></td><td></td><td></td><td> $\frac{\beta}{D_0} > \frac{c - h_0}{c + h}$ </td><td> $\frac{\beta}{D_0} \leqslant \frac{c - h_0}{c + h}$ </td></tr><tr><td> $\gamma^*$ </td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr></table>

## 4.2. $\alpha \ > \ 1 ;$ Managerial implications

From our analysis above for the $\alpha = 1$ case, the best decision for the retailer is to either try their best or do nothing. When the perishable characteristics are more obvious $( 0 ~ < ~ \alpha ~ < ~ 1 )$ , it is clear that the best decision for the retailer is the same as that for the $\alpha = 1$ case.

When $\alpha \ > \ 1$ , from Theorem 2, the first derivative of the cost function Eq. (9) can be written in the following form: $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial \theta } = T \hat { \sum _ { i = 0 } ^ { i = \alpha } } b _ { i } \theta ^ { i } } \end{array}$ , where $b _ { i } ( i = 0 , . . . , \alpha )$ are corresponding coeficients of $\theta ^ { i } , \theta ^ { * }$ is the optimal solution when its value $( \theta ^ { * } \in ( 0 , 1 ) )$ is satisfied by $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial \theta } = T \sum _ { i = 0 } ^ { i = \alpha } b _ { i } \theta ^ { i } = 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } = T \sum _ { i = 1 } ^ { i = \alpha } i b _ { i } \theta ^ { i - 1 } > 0 } \end{array}$ We can bring $\boldsymbol { \theta } ^ { * }$ into Eq. (11) to derive the optimal order quantity/cycle time and the minimum total cost.

Managerial implications. Firstly, for any given $h _ { \theta } ,$ the optimal order quantity $\boldsymbol { Q } ^ { * }$ that minimizes the total cost exists and is unique. Secondly, if the products are more prone to deterioration $( 0 ~ < ~ \alpha \leqslant 1 )$ , the key to the decision include the magnitude of deterioration cost and maximum holding cost as related to product freshness preservation. For cheap and highly-perishable products, there is no need for freshness preservation; for expensive and highly-perishable products, the value o $\begin{array} { r } { \dot { \mathbf { \nabla } } \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } } \end{array}$ must be taken into account before making any decision. For agri-fresh products with shorter shelf-life, the retailer is better of either doing nothing or doing the best to preserve product freshness. Finally, for relatively low-perishable products $( \alpha > 1 )$ , the optimal FPE indicator and the optimal order quantity can be directly calculated.

## 5. Numerical examples & sensitivity analysis

We now illustrate the analysis developed in Section 4 through numerical examples for α = 1 and $\alpha \ > \ 1$ respectively with figures. We also conduct sensitivity analysis on the main parameters $A , \beta , h _ { 0 } , c ,$ h and present the results in Table 5. For the range of each variable, we randomly generate A, β, h, h , c with the following uniform distributions $A \sim U [ 1 0 , 1 0 0 ] , \beta \sim U [ 5 , 5 0 ] , h \sim U [ 1 , 2 5 ] , h _ { 0 } \sim U [ 5 , 3 0 ] , c \sim U$ $[ 5 , 3 0 ]$ and set $D _ { 0 } = 1 0 0$ for a type of product.

$$
5. 1. \alpha = 1
$$

We first let α = 1 and present a series of numerical examples based on Eq. (8) to illustrate the above analytical results and generate some interesting observations.

Table 5  
Sensitivity analysis based on diferent parameter values.

<table><tr><td>Parameter</td><td>Value</td><td> $\theta^{*}(0,1)$ </td><td> $\gamma^{*}(0,1)$ </td><td> $T^{*}(0,1)$ </td><td> $Q^{*}(0,\infty)$ </td><td> $TC^{*}(0,\infty)$ </td></tr><tr><td rowspan="5">A</td><td>90</td><td>0.733</td><td>0.071</td><td>0.339</td><td>30.1</td><td>510.4</td></tr><tr><td>70</td><td>0.742</td><td>0.067</td><td>0.301</td><td>26.5</td><td>447.9</td></tr><tr><td>50</td><td>0.753</td><td>0.061</td><td>0.257</td><td>22.3</td><td>376.4</td></tr><tr><td>30</td><td>0.767</td><td>0.054</td><td>0.202</td><td>17.2</td><td>289.4</td></tr><tr><td>10</td><td>0.787</td><td>0.045</td><td>0.119</td><td>9.9</td><td>165.2</td></tr><tr><td rowspan="5">β</td><td>45</td><td>1.000</td><td>0.000</td><td>0.288</td><td>17.5</td><td>330.9</td></tr><tr><td>35</td><td>0.887</td><td>0.013</td><td>0.269</td><td>20.1</td><td>357.2</td></tr><tr><td>25</td><td>0.753</td><td>0.061</td><td>0.257</td><td>22.3</td><td>376.4</td></tr><tr><td>15</td><td>0.666</td><td>0.112</td><td>0.248</td><td>23.6</td><td>391.7</td></tr><tr><td>5</td><td>0.596</td><td>0.163</td><td>0.241</td><td>24.6</td><td>404.8</td></tr><tr><td rowspan="5"> $h_0$ </td><td>28</td><td>0.894</td><td>0.011</td><td>0.253</td><td>21.2</td><td>380.7</td></tr><tr><td>23</td><td>0.869</td><td>0.017</td><td>0.254</td><td>21.4</td><td>379.9</td></tr><tr><td>18</td><td>0.828</td><td>0.030</td><td>0.255</td><td>21.7</td><td>378.7</td></tr><tr><td>13</td><td>0.753</td><td>0.061</td><td>0.257</td><td>22.3</td><td>376.4</td></tr><tr><td>8</td><td>0.566</td><td>0.188</td><td>0.264</td><td>23.8</td><td>370.2</td></tr><tr><td rowspan="5">c</td><td>26</td><td>0.153</td><td>0.717</td><td>0.218</td><td>21.2</td><td>455.2</td></tr><tr><td>21</td><td>0.352</td><td>0.420</td><td>0.223</td><td>20.9</td><td>441.9</td></tr><tr><td>16</td><td>0.541</td><td>0.211</td><td>0.234</td><td>21.1</td><td>418.5</td></tr><tr><td>11</td><td>0.719</td><td>0.079</td><td>0.252</td><td>22.0</td><td>384.5</td></tr><tr><td>6</td><td>0.885</td><td>0.013</td><td>0.284</td><td>24.0</td><td>338.5</td></tr><tr><td rowspan="5">h</td><td>21</td><td>0.914</td><td>0.007</td><td>0.195</td><td>16.0</td><td>498.0</td></tr><tr><td>16</td><td>0.848</td><td>0.023</td><td>0.213</td><td>17.8</td><td>455.8</td></tr><tr><td>11</td><td>0.787</td><td>0.045</td><td>0.238</td><td>20.3</td><td>408.3</td></tr><tr><td>6</td><td>0.731</td><td>0.072</td><td>0.274</td><td>23.9</td><td>353.2</td></tr><tr><td>1</td><td>0.680</td><td>0.102</td><td>0.336</td><td>30.1</td><td>286.4</td></tr></table>

![](/api/attachments/2F2R648J/fulltext/images/65cb0ea4ada90f7623ae1f02bdd7006bbadd4711b887a5862d5a0f0f80bec099.jpg)  
Fig. 3. Total cost with parameters θ and $T \left( c \leqslant h _ { 0 } \right)$

For the example given in $\mathrm { F i g } . 3 ( c \leqslant h _ { 0 } ) .$ , the total cost decreases with increasing $\theta ,$ so the best choice for a retailer is to not take any freshness preserving measures, which means $\gamma ^ { * }  0 ( \theta ^ { * }  1 )$

We derive three sets of data subject to $c \ > \ h _ { 0 } ,$ as illustrated in ${ \mathrm { F i g s . ~ } } 4 ,$ 5 and 6. In Fig. 4, the total cost increases with increasing θ and its associated optimal fixed cycle time when $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 . } \end{array}$ , so try the best available preservation means to keep products fresh is the optimal decision for a retailer. I.e., let $h _ { \theta } \to h _ { 0 } ( \gamma ^ { \ast } \to 1 )$ , then $\theta ^ { * } \to 0 . { \mathrm { ~ F i g } } .$ . 5 shows the case of $\begin{array} { r } { \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \leqslant 0 } \end{array}$ . As seen in Theorem $^ { 5 , }$ we just store the agri-fresh product as usual without any attempt at freshness preservation. Here, $\gamma ^ { * }  0 , \theta ^ { * }  1$ . When $\begin{array} { r } { 0 < \frac { D _ { 0 } } { 2 \beta } - \frac { \hat { h } + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 } \end{array}$ , the total cost will reach its maximum when $\theta = \theta _ { N C }$ as can be seen in Fig. 6. In this case, the farther away from this point, the lower the cost. The retailer can compare the cost when $\theta \ : = \ : 1$ and when $\theta \ : = \ : 0$ to make decisions.

$$
5. 2. \alpha > 1
$$

As the case $0 ~ < ~ \alpha ~ < ~ 1$ is similar to the case $\alpha = 1 _ { \cdot }$ , we skip the numerical example part for $0 ~ < ~ \alpha ~ < ~ 1$

For the case $\alpha \ > \ 1$ , we provide the following two numerical examples.

![](/api/attachments/2F2R648J/fulltext/images/4092b57c848f962321b9dae186d82af6ae96ce479fe92164401057af48f5e939.jpg)  
Fig. 4. Total cost with parameters θ and $\begin{array} { r } { T ( c > h _ { 0 } , \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \geqslant 1 ) . } \end{array}$

![](/api/attachments/2F2R648J/fulltext/images/fb3321b6616dae86ce28acca06a43d204ac201dad5666f16cbba9f6bdf147ac1.jpg)  
Fig. 5. Total cost with parameters θ and $\begin{array} { r } { T \left( c > h _ { 0 } , \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } \leqslant 0 \right) . } \end{array}$

Example (1): Let $\alpha = 3 , D _ { 0 } = 1 0 0 , A = 5 0 , \beta = 2 5 , c = 1 0 , h = 8 ,$ $h _ { 0 } = 1 3 .$ . Since $\begin{array} { r } { \frac { \partial T C ( \theta , T ) } { \partial \theta } \approx 0 \mathrm { ~ a n d ~ } \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } \approx 1 1 3 4 T > 0 } \end{array}$ with $\theta ^ { * } = 0 . 6 2 2$ we have $T ^ { * } = 0 . 3 , \mathbf { \tilde { Q } } ^ { * } = 2 3 . 8 ,$ , TC<sup>∗</sup> = 355.0 from Theorem 2 as shown in Fig. 7.

Example (2): Let $\alpha = 5 , D _ { 0 } = 1 0 0 , A = 2 0 , \beta = 2 4 , c = 1 5 , h = 1 0 ,$ $h _ { 0 } = 8 .$ Since ${ \frac { \partial T C ( { \boldsymbol { \theta } } , T ) } { z _ { \infty } } } \approx 0$ and $\begin{array} { r } { \frac { \partial ^ { 2 } T C ( \theta , T ) } { \partial \theta ^ { 2 } } \approx 2 7 2 5 T > 0 } \end{array}$ with $\theta ^ { * } = 0 . 2 7 7 ,$ ∂θ then we have $T ^ { * } ~ \stackrel { \smile } { = } ~ 0 . 2 , Q ^ { * } = 1 5 . 4 , T C ^ { * } = 2 4 2 . 4$ . The figure for this example is similar to Fig. 7.

## 5.3. Sensitivity analysis

Next, we perform sensitivity analysis by changing one parameter at a time and keeping the remaining parameters at their original values $( A = 5 0 , \beta = 2 5 , c = 1 0 , h _ { 0 } = 1 3$ and $h \ : = \ : 8 )$ . We summarize the results for the case of $\alpha = 2$ in Table 5.

We observe the following based on the sensitivity analysis results as shown in Table 5.

(1) Change in A clearly afects $Q ^ { * } ;$ changes in $\beta ,$ h and c have more influence on $\theta ^ { * } ;$ change in h has an impact on both $\boldsymbol { \theta } ^ { * }$ and $Q ^ { * }$ .

(2) When the value of parameter A decreases and the value of parameter h increases, the optimal order quantity $Q ^ { * }$ decreases. When the value of parameters $\beta , h _ { 0 } ,$ h decrease and the value of parameter c increases, the optimal FPE indicator $\gamma ^ { * }$ increases.

(3) When the value of parameter A increases, the value of $T ^ { * } , Q ^ { * }$ , and $T C ^ { * }$ increase due to the fact that increased ordering cost needs more time to ofset. Increase in held inventory increases the total cost.

![](/api/attachments/2F2R648J/fulltext/images/86cf2b39318ba7348f5b142f0df23211527c024ed16317a1a2c4b588b1c1ab4b.jpg)

![](/api/attachments/2F2R648J/fulltext/images/f232527451a6ad0defdec3529cafad28f285a2a5b87655e5ac76c561fbe6231a.jpg)  
Fig. 7. Total cost with parameters θ and T.

(4) A change in parameter $\beta$ directly changes the demand rate. So, when the value of parameter $\beta$ decreases, the demand rate increases. Note that more demand needs to be satisfied under lower deterioration rate. Thus, higher holding cost (related and unrelated to freshness preservation) increases the total cost.

(5) When the value of parameter $h _ { 0 }$ decreases and c increases, the optimal FPE indicator will increase. The lower the parameter $h _ { 0 }$ value, the higher the ratio of controllable preservation cost to maximum preservation cost at the same freshness preservation level. The higher the parameter $c ,$ the more the retailer is willing to take measures to keep the product fresh due to the higher purchasing cost. Therefore, the FPE indicator becomes larger. Then, the in crease in procurement cost and preservation cost leads to a higher total cost.

(6) When the value of parameter h decreases, we increase the freshness preservation cost to lower the deterioration rate. Although the preservation cost increases, the decrease in holding cost and deterioration-related cost efectively reduces the total cost.

Our results can be briefly summarized as follows. Increase in $T ^ { * }$ could be caused by increasing A and $\beta$ or decreasing $h _ { 0 } , \ c$ and h. Similarly, an increase in $Q ^ { * }$ could be caused by increasing A or decreasin $\xi \beta , h _ { 0 } ,$ c and h. An increase in $\gamma ^ { * }$ could be caused by increasing A and c or decreasing $\beta ,$ h , and h. An increase in $\boldsymbol { \theta } ^ { * }$ could be caused by increasing $\beta , h _ { 0 }$ and h or decreasing A and $c , \mathsf { A } \mathsf { n }$ increase in $T C ^ { * }$ could be caused by increasing A, h , c and h or decreasing $\beta .$ Change in h has the least serious influence on the optimal cost among those parameters, while change in A has the most serious influence, which can be seen from the ratio of change in each parameter on change in each optimal result (elasticity).

![](/api/attachments/2F2R648J/fulltext/images/f97a1e9da1690825c90bee260e6485e3d6a3140864150353ed6b81547ce1a035.jpg)  
Fig. 6. Total cost with parameters θ and $\begin{array} { r } { T \Big ( c > h _ { 0 } , 0 < \frac { D _ { 0 } } { 2 \beta } - \frac { h + h _ { 0 } } { 2 ( c - h _ { 0 } ) } < 1 \Big ) . } \end{array}$

## 6. Conclusion

The integration of perishable product quality indicator, market response, and inventory management plays an important role in today's perishables retailing industry. We investigate the phenomenon in which, for a given fixed price, consumers are more likely to buy higher quality (less deteriorated) and more stocked perishable products.

This study contributes to the perishable inventory management system literature by considering DR as a decision variable and its efects on quality indicator of perishable products, associated market response, and a variable freshness-prolonging (operating) cost. We assume that the price is fixed and demand depends on quality deterioration within a given period. We further assume that the deterioration rate is controllable by freshness-preservation technology and efort at a variable cost. We then model the perishable inventory decision support system with deterioration-controlled/freshness-dependent demand, quality indication, and controllable DR to analyze its dynamics with various scalable parameters. We analytically model this scenario and perform sensitivity analysis to generate associated managerial implications. Another main contribution of this research is considering demand of retailing perishable products as quality (freshness) dependent. Specifically, we consider quality as time-integration of initial quality and deterioration, i.e., an agri-fresh product with low deterioration rate that appears fresher and more displayed stock will attract higher demand. To the best of our knowledge, no existing work has considered DR to simultaneously afect freshness-dependent and stock-dependent demand, although the later has been extensively studied.

In summary, the proposed perishable inventory management problems is established by assuming a fixed periodic price and demand that depend on the extent of deteriorated quality of perishable products. We propose a quality indicator and assume that deterioration rate can be controlled by adjusting the handling and storage conditions at a vari able cost. We model this perishable inventory management problem with quality indicator and controllable deterioration rate with freshness-stock-dependant demand. We then analyze its dynamics with various scalable parameters. For highly perishable agri-fresh products, the key to the decision includes the magnitude of deterioration cost and maximum holding cost as related to product freshness preservation. We derive the best decision-making steps and suggest that there is no need for freshness preservation in the management of the cheap and highly perishable products. Under certain conditions. product wastage can be reduced with the same controlled-cost requirements as in the management of the expensive and highly-perishable products. For low perishable products, the unique optimal FPE indicator and the optimal order quantity can be directly calculated. We illustrate our analytical results with sensitivity analysis and conclude by providing related managerial implications. Results from this study can be used to support perishable inventory management decisions with the consideration of quality-dependent demand.

Future research can be extended to investigating the various conditions under which deterioration rate may change and its functional link to the quality indictor. For example, the relationships among deteriorate-rate, quality-indication, and freshness-dependent demand may be diferent for blood bank product as compared to that for agrifresh produce. Integrating the number of facings with the facing quality can be another immediate extension of this study.

## Acknowledgements

This research was supported by the National Natural Science Foundation of China (71972071, 71431004) and the Fundamental Research Funds for the Central Universities.

## References

[1] S.S. Ali, J. Madaan, F.T. Chan, S. Kannan, Inventory management of perishable products: a time decay linked logistic approach, Int. J. Prod. Res. 51 (13) (2013) 3864–3879.

[2] M. Bakker, J. Riezebos, R.H. Teunter, Review of inventory systems with deterioratio since 2001, Eur, J. Oper, Res, 221 (2) (2012) 275–284.

[3] J. Blackburn, G. Scudder, Supply chain strategies for perishable products: the case of fresh produce, Prod. Oper. Manag. 18 (2) (2009) 129–137.

[4] I. Bose, S. Yan, The green potential of RFID projects: a case-based analysis, IEEE IT Prof. 13 (1) (2011) 41–47 (January-February).

[5] I. Bose, R. Pal, Auto-ID: Managing anything, anytime, anywhere in the supply chain, Comm. ACM 48 (8) (2005) 100–106 (August).

[6] I. Bose, A.K.H. Lui, E.W.T. Ngai, The impact of RFID adoption on the market value of firms: an empirical analysis, J. Organ. Comput. Electron. Commer. 21 (4) (2011) 268–294.

[7] X. Cai, J. Chen, Y. Xiao, X. Xu, Optimization and coordination of fresh product suppl chains with freshness-keeping efort, Prod. Oper. Manag. 19 (3) (2010) 261–278.

[8] D. Chakraborty, D.K. Jana, T.K. Roy, Multi-item integrated supply chain model for deteriorating items with stock dependent demand under fuzzy random and bifuzzy en: vironments, Comput. Ind. Eng. 88 (2015) 166–180.

[9] C.K. Chan, W.H. Wong, A. Langevin, Y.C.E. Lee, An integrated production-inventory model for deteriorating items with consideration of optimal production rate and dete rioration during delivery, Int. J. Prod. Econ. 189 (2017) 1–13.

[10] J. Chen, M. Dong, Y. Rong, L. Yang, Dynamic pricing for deteriorating products with menu cost, Omega 75 (2018) 13–26.

[11] R.P. Covert, G.C. Philip, An EOQ model for items with Weibull distribution deterioration, AIIE Trans. 5 (4) (1973) 323–326.

[12] M. De Keizer, R. Akkerman, M. Grunow, J.M. Bloemhof, R. Haijema, J.G. van der Vorst, Logistics network design for perishable products with heterogeneous quality decay, Eur. J. Oper. Res. 262 (2) (2017) 535–549.

[13] C.Y. Dye, T.P. Hsieh, An optimal replenishment policy for deteriorating items with effective investment in preservation technology, Eur. J. Oper. Res. 218 (1) (2012) 106–112.

[14] P.M. Ghare, G.F. Schrader, A model for exponentially decaying inventory, J. Ind. Eng. 14 (5) (1963) 238–243.

[15] P.H. Hsu, H.M. Wee, H.M. Teng, Preservation technology investment for deteriorating inventory, Int. J. Prod, Econ, 124 (2) (2010) 388–394.

[16] R. Kopach, B. BalcoÅlu, M. Carter, Tutorial on constructing a red blood cell inventory management system with two demand rates, Eur. J. Oper. Res. 185 (3) (2008) 1051-1059.

[17] E.J. Lodree, B.M. Uzochukwu, Production planning for a deteriorating item with stochastic demand and consumer choice, Int. J. Prod. Econ. 116 (2) (2008) 219–232.

[18] R. Maihami, I.N. Kamalabadi, Joint pricing and inventory control for non-instantaneous deteriorating items with partial backlogging and time and price dependent demand, Int. J Prod Econ 136 (1) (2012) 116–122

[19] C. Muriana. An EOO model for perishable products with fixed shelf life under stochastic demand conditions, Eur. J. Oper. Res. 255 (2) (2016) 388–396.

[20] G.C. Philip, A generalized EOQ model for items with Weibull distribution deterioration, AIIE Trans. 6 (2) (1974) 159–162.

[21] S. Piramuthu, W. Zhou, RFID and perishable inventory management with shelf-space and freshness dependent demand Int. J Prod Econ 144 (2) (2013) 635–640

[22] S.R. Singh, N. Kumar, R. Kumari, An inventory model for deteriorating items with shortages and stock-dependent demand under inflation for two-shops under one man agement, Opsearch 47 (4) (2010) 311–329.

[23] P R. Tadikamalla An EOO inventory model for items with gamma distributed dete rioration, AIIE Trans, 10 (1) (1978) 100–103

[24] M. Thibaud, H. Chi, W. Zhou, S. Piramuthu, Internet of things in high-risk environment, health and safety (EHS) industries: a comprehensive review, Decis. Support. Syst. 108 (2018) 79–95 (April).

[25] S. Tiwari, C.K. Jaggi, A.K. Bhunia, A.A. Shaikh, M. Goh, Two-warehouse inventory model for non-instantaneous deteriorating items with stock-dependent demand and inflation using particle swarm optimization Ann Oper, Res 254 (1–2) (2017) 401–423

[26] Y.C. Tsao, Designing a supply chain network for deteriorating inventory under preservation efort and trade credits, Int. J. Prod. Res. 54 (13) (2016) 3837–3851.

[27] Y.-J. Tu. W. Zhou, S. Piramuthu. A novel means to address RFID tag/item separation ir supply chains, Decis. Support, Syst. 115 (2018) 13–23 (November).

[28] W. Zhou, S. Piramuthu, Efects of ticket-switching on inventory management: actual vs. information system-based data, Decis. Support. Syst. 77 (2015) 31–40 (September).

[29] W. Zhou, S. Piramuthu, Efect of ticket-switching on inventory and shelf-space allocation, Decis, Support, Syst, 69 (2015) 31–39 (January)

Ya Yang is with the Department of Management Science and Engineering, East China University of Science and Technology, Shanghai, China as well as the Department of Management Science and Engineering, Oinghai University. Xining, China.

Huihui Chi is a PhD candidate at ESCP Europe-Paris.

Wei Zhou is Professor of Information Systems at ESCP Europe-Paris.

Tijun Fan is Professor in the Department of Management Science and Engineering, East China University of Science and Technology, Shanghai, China.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida.
