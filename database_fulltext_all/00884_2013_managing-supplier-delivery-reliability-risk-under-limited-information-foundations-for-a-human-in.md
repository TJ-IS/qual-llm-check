---
otero_id: 884
otero_key: "7CAEDNU8"
title: "Managing supplier delivery reliability risk under limited information: Foundations for a human-in-the-loop DSS"
authors: "Roberto Pinto; Tobias Mettler; Marco Taisch"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.033"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing supplier delivery reliability risk under limited information: Foundations for a human-in-the-loop DSS

Roberto Pinto <sup>a,</sup>⁎, Tobias Mettler <sup>b</sup>, Marco Taisch <sup>c</sup>

<sup>a</sup> CELS, Department of Engineering, University of Bergamo, Viale Marconi 5, 24044 Dalmine (BG), Italy

<sup>b</sup> Institute of Information Management, University of St. Gallen, Müller-Friedberg-Strasse 8, CH-9000 St. Gallen, Switzerland

<sup>c</sup> Department of Management, Economics and Industrial Engineering, Politecnico di Milano, Viale Lambruschini 4/b, 20156 Milano, Italy

## a r t i c l e i n f o

Article history: Received 23 November 2011 Received in revised form 26 July 2012 Accepted 21 October 2012 Available online 1 November 2012

Keywords: Delivery reliability Distribution-free Human-in-the-loop DSS Supply risk mitigation Limited information

## a b s t r a c t

The potential impact of suppliers' delivery reliability issues in many industries requires a proper decision support system (DSS) that allows decision makers to analyze and reduce the delay's detrimental effects. Despite the relevance of the topic, companies are often confronted with the lack of historical, quantitative data and knowledge about a supplier's performance (i.e., when selecting a new supplier). In this paper, we address the problem of the scarcity of quantitative data by considering and extending the human-in-the-loop DSS concept, which accounts for an expert's knowledge and experience. In our concept, a human expert is involved in making and revising data provided by a computational model, with the aim of supporting companies in making decisions when dealing with unreliable suppliers, in order to minimize the costs related to external discontinuities. To deal with scant quantitative data, we developed a distribution-free model. Our <sup>fi</sup>ndings positively support the distribution-free approach as an effective tool to be used when only a limited and perhaps unstructured base of data is available. The presented computational model aims at creating a solid foundation for developing a comprehensive human-in-the-loop decision support system.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Recently, delivery reliability has shifted from an order winner to an order quali<sup>fi</sup>er factor in many manufacturing and service industries [11], thanks to the wide diffusion and consolidation of operations paradigms, such as just-in-time and quick response distribution [7,26]. In extended, complex, and highly collaborative supply chains, suppliers' delivery reliability – a speci<sup>fi</sup>cally operational performance measure – is strongly affected by strategic and tactical decisions, such as selecting the “right” suppliers for conjoint design, development, manufacturing, and distribution. In fact, seeking the timeliness of all operations since the network design stage is of paramount importance when a large part of the production is outsourced. In this respect, suppliers are often perceived as a source of delay risk, affecting the company's delivery reliability either directly or indirectly [9,27].

The potential impact of the suppliers' delivery reliability problems in many production industries requires a proper decision support system (DSS) to help in analyzing and reducing the delay's detrimental effects. Such a support system must be able to deal with highly complex environments, where both qualitative and quantitative elements play a substantial role.

Nonetheless, considering the quantitative perspective, companies are often confronted with the lack of historical, quanti<sup>fi</sup>able data and information about a supplier's previous performance; thus, in today's volatile business environment decisions usually have to be based on incomplete or even non-existent information. Focusing on the delivery reliability dimension, for example, distributional information on the earlier delivery performance of a supplier may be limited or missing (i.e., in the case of a new supplier). Sometimes, such a lack of numerical data is compensated for by an educated guess of the mean and the variance of the data distribution. According to Moon and Yun [18], under these conditions the tendency is to use normal distribution in the computational models, even though such an assumption does not provide the best decision in cases when other probability distributions with the same mean and variance occur.

Furthermore, although DSS can assist decision makers in acquiring data, information, and knowledge regarding products, services, suppliers, and customers, not all of the possible factors behind an optimal decision can be algorithmically implemented, due to the complexity or the nature of the factors themselves. This aspect emphasizes the role and contribution of a human expert in integrating qualitative knowledge into the decision process.

Considering the relevance of the supplier's delivery reliability dimension and the scarcity of contributions to this topic, the purpose of this paper is to investigate the feasibility of an architecture for a DSS that supports decision makers in dealing with delivery delay risks when the available information about a supplier's performance is limited to the mean and the standard deviation (or their educated guess).

Speci<sup>fi</sup>cally, we strive to address the following research questions:

• How is it possible to mitigate the delay risk? How may computational models support the decision maker when no historical knowledge of the supplier's performance is available?

• How can the computational model developed for delay risk mitigation be implemented within a DSS and integrated with qualitative information?

We see our contribution as a possible foundation for developing a human-in-the-loop decision support system (HIL-DSS), allowing quantitative data to be complemented with qualitative information provided by a human expert. In order to answer the proposed research questions, the remainder of the paper is organized in <sup>fi</sup>ve sections: the next section explores the role of buffers in reducing delivery delays in manufacturing sectors. Then, we delineate the scenario in which we developed and tested the computational model. The computational results are discussed in the following section, along with an outline of the integration of qualitative information. Finally, we present our conclusions and recommendations for future research.

## 2. Background

The on-time delivery of products and services is still recognized as a key success factor for competition in many manufacturing and service <sup>fi</sup>rms [2,6,23]. Make-to-order (MTO) companies, in particular, are highly sensitive to potential problems that might in<sup>fl</sup>uence delivery reliability performance, as discussed in the next section.

## 2.1. The delivery delay domino effect

Delivery reliability issues might originate from internal problems, both in the production stage (i.e., machine breakdown, lack of human resources, workforce absenteeism, missing materials) and in the planning process (i.e., errors in planning and scheduling decisions, selection of an unreliable supplier), leading to shortages of the <sup>fi</sup>nal products and the impossibility of ful<sup>fi</sup>lling customer demand. Nonetheless, it is important to highlight that a company's delivery reliability is not an exclusively internally determined performance. In fact, in a multi-tiered supply chain, the performance of an actor almost inevitably impacts the performance of the following ones; for example, a delay in delivery from supplier A to company X might jeopardize the delivery reliability of X with respect to its customer E and, eventually, to its end customer F (Fig. 1). According to this “domino effect,” one's performance should contemplate his/her suppliers' performance.

According to Nieuwenhuysea and Vandaele [19], “it is desirable from the buyer's point of view that the arrival of the ordered material can be predicted as accurately as possible, such that the start times of the production runs can be planned with a high level of certainty, and rescheduling efforts (due to material arriving too early or too late) can be restricted to a minimum.” Such an aspiration is hardly achievable if delivery delays are not controlled from the beginning: in fact, if delivery reliability problems propagate through the supply chain without control, a short delay in the <sup>fi</sup>rst tier might result in a dramatic delay to the <sup>fi</sup>nal customers, leading to a kind of “reversed” bullwhip effect [14] from the upper links of the chain downstream to the <sup>fi</sup>nal links.

According to the scenario depicted in Fig. 1 and described above, in the rest of this paper we assume the perspective of company X, whose objective is to mitigate the effects of supplier delay.

## 2.2. Managing delivery delay risk: the role of buffers

Due to the potential impact of suppliers' delivery reliability problems, different countermeasures, such as process and product <sup>fl</sup>exibility, and redundancy and supplier collaboration, for example, can conceivably halt the propagation of delivery delays and reduce the consequent detrimental effects. In our research, we focus on the use of redundancy based on buffers, since they represent one of the most common backup solutions adopted by companies aiming at reducing the impact of delays in the inbound <sup>fl</sup>ows. Indeed, the “variability in a production system can be buffered by some combination of inventory, capacity, and time” [12]; such a variability buffer law is considered one of the pillars of risk management and, thus, adopted here. Moreover, buffers generally do not affect the inter-organizational supplier–buyer relationship (the supplier might not even know about the presence and the entity of the buffer at the customer's site); instead, they are meant to have a direct effect on the demand side, providing continuity of operations.

Perhaps one of the most intuitive forms of buffering is represented by inventory, but it is also possible to buffer the effect of delays by using time and capacity buffers, in order to ensure the continuation of the business and on-time delivery to customers [1,8,24,28].

Buffers represent a cost that must be carefully managed. Building a buffer generally involves an upfront payment for resources that might or might not be used in the future. Therefore, the entity (i.e., size) of the buffer must be consciously de<sup>fi</sup>ned, balancing the bene<sup>fi</sup>ts and drawbacks of buffers that are too large or too small.

![](/api/attachments/7CAEDNU8/fulltext/images/48575e80efa2636dfd67ded54f18225a48009d324ef02e6324323261290dd218.jpg)  
Fig. 1. Domino effect due to deliver reliability problems.

Dealing with buffer size decisions and costs related to delivery delay risks, the buyer could experience two different situations:

• the buyer has an extensive historical knowledge of the delivery reliability performance of a supplier; thus, he/she is able to quantify effectively the mean μ, the standard deviation σ, and a probability distribution of the delivery delay (either empirical or theoretical), and use this information to evaluate the buffer size and costs;

• the buyer does not have suf<sup>fi</sup>cient experience with the supplier, and is only able to guess the mean and the standard deviation, but not the probability distribution of the delivery delay. As underlined in [22], there may be various reasons for this: for example, the available sample of previous experience may be quite small, or there may be a reason to suspect that future performance will be described by a different distribution from that governing past history.

A suitable computational model, as shown in Section 3, can represent both situations. Nonetheless, we deem such a computational model to be only a portion of a potential support for decision makers. In fact, human experience and unstructured information may be substantially helpful in complementing the output of the computational models, which usually are, by their very nature, bound to quantitative, numeric data. Therefore, in the next section, we envision a more comprehensive perspective, where the model is framed in a structure encompassing other elements, such as qualitative information and human expertise.

## 3. A proposal for a HIL-DSS architecture

Quantitative information about cost and delivery performance is important, but they represent only the structured portion of the total information required to make robust decisions. To deal with this aspect, it is our ultimate goal to design an architecture for a human-in-the-loop decision support system (HIL-DSS) aimed at assisting decision makers in dealing with delivery delay risks through an appropriately sized buffer, when little information about delivery performance is available, and with the possibility of complementing quantitative information with qualitative, unstructured information.

The human-in-the-loop concept has its roots in virtual modeling and simulation (e.g., [3]), and typically refers to models, methods, and tools that require some kind of human interaction [20]. In the context of DSS, the <sup>fi</sup>rst architectural proposition of a HIL-DSS was recently provided by Subramania and Khare [25] to deal with a scenario where human experts, who are capable of learning and making decisions, may use limited or incomplete DSS (i.e., only quanti<sup>fi</sup>able factors are included, and there is little possibility that new information will be discovered and updated automatically) to make actionable decisions, but not blindly follow them. In other words, the humans can use their expertise on top of the DSS to make the <sup>fi</sup>nal decision. According to these authors [25], a HIL-DSS consists of four major elements (solid boxes in Fig. 2):

• Scenario: a representation of a speci<sup>fi</sup>c problem situation or potential use case for the DSS (e.g., an out-of-stock situation);

• Decision Support System: a computer-based system that helps humans to analyze and understand the situation better (e.g., software for business analytics). The DSS suggests the decisions to be made by analyzing the available quanti<sup>fi</sup>able factors;

• Subject matter expert: a human with in-depth knowledge of a particular domain, capable of reviewing the decisions made by the DSS and other human experts on a conditional basis, in order to recommend enhancements and improvements; and

• Human expert/decision maker: a human that develops and evaluates different solutions to a speci<sup>fi</sup>c problem, taking into consideration the decisions suggested by the DSS and leveraging his/her experience, therefore not relying entirely on the DSS outcomes.

![](/api/attachments/7CAEDNU8/fulltext/images/f6a3b8e926154016b5098a84b162b3dcf731cd170ea8123612a7b831f94b7f4e.jpg)  
Fig. 2. Architecture for a human-in-the-loop DSS.

In our view, and according to the context under investigation, such architecture can be complemented with some elements; hence, our understanding of a HIL-DSS extends the initially de<sup>fi</sup>ned architecture (dotted boxes in Fig. 2):

• Decision model: a model that forms the cornerstone of a DSS, typi cally formalized as a <sup>fi</sup>nite list of well-de<sup>fi</sup>ned instructions or rules. For our purpose, a model is a formal representation of a system, expressed by mathematical equations that allow for investigation and solution search leveraging the quantitative portion of available information (we refer to it as a “computational” or “quantitative model,” or simply “the model,” in the rest of the paper);

• (Preliminary) Decision: a <sup>fi</sup>rst solution or sample of solutions to a problem, proposed by the DSS according to the quantitative model. These solutions provide the basis for actions, or for further, more in-depth analysis of the scenario under investigation.

• Final decision: the de<sup>fi</sup>nitive decision made by the human expert decision maker as a result of the combination of qualitative information analysis, personal experience, and solutions proposed by the model. The <sup>fi</sup>nal decision typically forms the basis for further actions and it must not necessarily be equal to the preliminary, “computed” decision proposed by the DSS.

## 3.1. The role of the computational model

As illustrated in Fig. 2, a prominent role in the proposed architecture is played by the computational model. It aims to provide structured and quanti<sup>fi</sup>able results on which a decision maker can ground his/her decisions. Therefore, the effective design of this element of the architecture of a HIL-DSS is of paramount importance. For this reason, a substantial portion of this paper is devoted to the design, testing, and analysis of such a component.

The architecture of the HIL-DSS and model we present is particularly aimed at supporting purchasing decision makers who procure materials on an MTO basis, that is, components and materials that are ordered from suppliers after the customer order has been received. This is typical of costly components required by <sup>fi</sup>nal products that are characterized by uncertain demand. As compared to companies that procure materials in a pure Make-to-Stock (MTS) environment, MTO entails greater complexity, given that each order typically requires different amounts of processing work and/or different sequences of work centers [10].

Moreover, since providing customers with the right product or service on the agreed date has become a primary concern for many companies [26], the proposed model is speci<sup>fi</sup>cally oriented toward the time dimension of delivery reliability (i.e., delivery time reliabili-$\operatorname { t y } ) .$ . We assume that it is possible to buffer the suppliers delay to some extent, reducing the impact of de<sup>fi</sup>cient suppliers' delivery reliability. It is worth noticing at this point that, for our purposes, the term buffer does not necessarily refer to inventory uniquely. In fact, as noticed before, it is possible to buffer the effect of delays through other possible interventions, such as time buffers (i.e., including slack time in scheduling) and capacity buffers (i.e., extra capacity buffer, multiple sourcing, or backup suppliers). Therefore, even though our focus is mainly on an MTO production system, the models presented hereafter may be easily adapted to an MTS context.

## 4. Scenario descriptions and model development

In this section, we de<sup>fi</sup>ne the scenarios and respective models that form the cornerstone of the DSS. Each model is meant to provide the basis (referred to as the preliminary decision in the proposed architecture) for human experts to evaluate the expected costs related to suppliers' delivery reliability performance, taking two main components into account:

• the costs related to buffering the delay (i.e., to keep the inventory of incoming material, or to add slack to the production schedule); and

• the costs related to recovering from a disruption (i.e., halted production) caused by a delayed delivery.

Depending on the completeness and availability of the information, we designed two distinct computational models: the <sup>fi</sup>rst model assumes that knowledge about the probability distribution of the supplier's delivery performance is available (thus re<sup>fl</sup>ecting an ideal case, for comparison purposes); the second model does not rely upon any prior knowledge about the distribution of the delay (referred to as the distribution-free model in the rest of the paper).

## 4.1. Scenario assumptions

Consider the case of a company (referred to as the buyer in the following) that purchases a component for its manufacturing process. The component is deemed to be critical for the progress of the buyer's production, meaning that a disruption in the inbound <sup>fl</sup>ow might directly in<sup>fl</sup>uence the production process and the delivery reliability to the following link(s) in the supply chain. Thus, the buyer wants to de-<sup>fi</sup>ne the optimal size of the buffer to minimize the cost related to production discontinuities caused by the supplier's unreliability.

The buyer communicates a requested due date $\left( \tilde { d } \right)$ to the supplier, along with other requirements regarding component characteristics, quality, and so forth. We assume that early deliveries are forbidden, and we deem a supplier who delivers on the exact date agreed to with the customer as perfectly reliable. If requested, the supplier provides a price quotation Q along with the general agreement on the due date <sup>˜</sup>d<sup></sup> <sup></sup>.

Such a price Q actually represents only a portion of the real cost the buyer might bear if the delivery is not reliable. In fact, we can assume an extra cost $c _ { D }$ for each day of delay, given by the sum of many components, such as the cost of rescheduling, warehousing, expediting, and so forth, which can be attributed to the lack of reliability of the supplier. We refer to $c _ { D }$ as the delay recovery cost.

We further assume that it is possible to quantify $c _ { D } ,$ which depends eminently on the buyer's characteristics. For example, $c _ { D }$ might be set as equal to the penalty that the buyer's customer is charging for delayed delivery; in the automotive industry, it has been reported that Saturn levies <sup>fi</sup>nes of \$500 per minute against suppliers who cause production line stoppages [4] and that Chrysler <sup>fi</sup>nes suppliers \$32,000 per hour when an order is late [21].

To reduce the impact of the delay recovery cost $c _ { D } ,$ the buyer can rely on a buffer that provides a backup in case of late deliveries. In our case, a buffer is any form of safeguard that guarantees a certain level of robustness to the process. According to the unit of measure of the delay, buffers are expressed as days of coverage; thus, with a buffer of B days, an actual delivery date D in the time interval $\left\lceil \tilde { d } , \tilde { d } + B \right\rceil$ will not generate any extra cost $c _ { D } ,$ while for any delivery beyond $\tilde { d } + B$ the buyer bears an extra cost of $c _ { D }$ per day of delay (Fig. 3).

We assume it is possible to estimate the daily cost $c _ { B }$ for the buffer (a cost per day of coverage); thus, the decision of detaining a buffer of B days generates a cost $c _ { B } \cdot B ,$ regardless of the actual performance of the supplier. As shown in the following, the ratio ${ { C } _ { B } } \mathrm { ~ / ~ } { { { C } _ { D } } }$ plays an important role in the <sup>fi</sup>nal decision.

In the next subsections, we present the models under the known distribution of delays and under the distribution-free assumption. We then compare the two models to evaluate their effectiveness in case little information is available about the distribution of the delivery delays.

## 4.2. The model with known distribution

As previously stated, we focus on delivery time reliability; therefore, let x be a random variable representing the deviation of the actual delivery date D from the agreed delivery date <sup>˜</sup>d (that is, $x =$ $D - \tilde { d } )$ . Assuming that early deliveries are forbidden, x is bounded to x 0.

We assume the availability of a time series of the previous delivery performance; such a time series is long enough to infer a delay probability distribution $f ( x )$ over a domain $S \mathbb { R } ^ { + }$ and the relative cumulative distribution function F(x). For the sake of tractability, we assume that F is continuous, non-decreasing, and differentiable, and $F ( 0 ) = F ^ { - 1 } ( 0 ) = 0$ . We also know the mean μ and the standard deviation σ of x.

We further assume that the delay distribution f does not depend on the lead times. This is a rather strong assumption in some cases; nonetheless, we can overcome this limitation by assuming the possibility of evaluating different delay distributions for different lead times; say, $f _ { i } ( x )$ is the delay probability distribution for an allowed lead time in the interval [l ;u ], with $\cap _ { i } [ l _ { i } ; u _ { i } ] = \emptyset$ and $\cup _ { i } [ l _ { i } ; u _ { i } ] = S .$

In the described context, the total cost C(⋅) borne by the buyer depends on the supplier's price $Q _ { \mathrm { { \ell } } }$ on the size of the buffer B, and on the delivery delay x. Formally, we can write:

$$
C (x, B) = Q + c _ {D} (x - B) ^ {+} + c _ {B} \cdot B\tag{1}
$$

![](/api/attachments/7CAEDNU8/fulltext/images/bd05b74d73329e95da8e69bd140aea21bbc39a559690744a00174df91f99d86b.jpg)  
Fig. 3. Emerging cost as a function of the delay.

where $( x - B ) ^ { + } = \operatorname* { m a x } ( x - B ; 0 )$ . In fact, the delay recovery cost c is incurred only in the case that the delay x is greater than the buffer B, and is zero otherwise. We also notice that the cost of the buffer is not dependent on the realized delay x: in fact, the cost $c _ { B } \cdot B$ can be considered a sunk cost since it is incurred before the actual delivery D. In this research, we consider no salvage value for unused buffer.

Thus, once the size of the buffer has been determined, the actual cost C(x,B) depends on the realized delay x, and on the size of the buffer B; the greater the buffer, the lower the risk of delay recovery costs but, at the same time, the higher the sunk cost related to the cost of the buffer. Since the delay is a stochastic variable, from the buyer's perspective the expected cost $E [ C ( x , B ) ]$ ] related to the supplier under analysis is expressed as:

$$
E [ C (x, B) ] = Q + c _ {D} \int_ {- \infty} ^ {+ \infty} (x - B) ^ {+} f (x) d x + c _ {B} \cdot B.\tag{2}
$$

Recalling that $\int _ { - \infty } ^ { + \infty } ( x - B ) ^ { + } f ( x ) d x = \int _ { B } ^ { + \infty } ( x - B ) f ( x ) d x$ , upon applying the Leibniz rule and imposing the partial derivative with respect to B equal to zero we have:

$$
\frac {\partial E [ C (x , B) ]}{\partial B} = - c _ {D} \int_ {B} ^ {+ \infty} f (x) d x + c _ {B} = - c _ {D} (1 - F (B)) + c _ {B};\tag{3}
$$

thus:

$$
B ^ {*} = F ^ {- 1} \left(1 - \frac {c _ {B}}{c _ {D}}\right) = F ^ {- 1} (1 - \beta).\tag{4}
$$

Therefore, the optimal size of the buffer, $B ^ { * } ,$ , is a function of the cumulative distribution F and the ratio $\begin{array} { r } { \beta = \frac { c _ { B } } { c _ { \mathrm { { r } } } } . } \end{array}$

From Eq. (4) we also know that $1 - \beta \stackrel { \triangledown } { \in } [ 0 ; 1 ] ;$ ; thus:

$$
0 \leq 1 - \frac {c _ {B}}{c _ {D}} \leq 1 \Rightarrow c _ {B} \leq c _ {D}\tag{5}
$$

being $c _ { B } > 0$ and $c _ { D } > 0$

The model is closely related to Scarf's model [22] and re<sup>fl</sup>ects the reality of delivery reliability risk under the following respects:

• When β→1 (that is, $c _ { D } \to c _ { B } )$ then $B ^ { * } \to F ^ { - 1 } ( 0 ) = 0$ . This is intuitively explained by the fact that when the delay recovery cost $c _ { D }$ is close to the cost of the buffer $c _ { B } ,$ it is convenient to adopt a reactive approach, where the company reacts to disruptions rather than preparing to avoid it by using buffers. In an extreme case, for $c _ { D } = c _ { B }$ it is not convenient at all to build a buffer, from a cost minimization perspective.

• When $c _ { D } \gg c _ { B }$ then $B ^ { * }$ tends to increase according to $F ^ { - 1 }$ . In fact, if the cost of the buffer is small, it is convenient to adopt a preventive approach, immobilizing some capital in building buffer rather than reacting to disruptions.

In the case of multiple suppliers, evaluating the cost $E [ C ( x , B ) ]$ for each supplier allows for ranking the different alternatives in the order of the increasing expected cost, thus selecting the most pro<sup>fi</sup>table one.

It is worth noticing once more that the model does not aim at eliminating the risk of a delay. In fact, in cases when the buffering supplier delay has an extremely high cost, the model suggests to undertake the risk of incurring the delay recovery cost rather than sustaining the buffer cost; $\operatorname { i f } c _ { B }$ is high, it might be better to risk paying a recovery cost $c _ { D } { ( \boldsymbol { x } { - } \boldsymbol { B } ^ { * } ) } ^ { + }$ rather than making a certain upfront payment of the sum $c _ { B } \cdot B ^ { * }$ . In this respect, $c _ { B } \cdot B ^ { * }$ can be viewed as the investment that minimizes the expected cost of the relationship with the given supplier.

In the next section, we elaborate on the model in order to relax the assumption of the known distribution of the delivery delays.

## 4.3. The distribution-free model

In this section, we consider the case where only the mean μ and the standard deviation σ of the delay variable x are known (or estimated), without any further assumptions on the distribution $F ,$ other than saying that it belongs to the class Γ of the cumulative distribution functions with mean μ and standard deviation σ. Since F is unknown, and adopting the normal distribution does not assure the best protection in the case that other distributions with the same mean and variance occur [18], we require the expected cost (Eq. (2)) to be minimized against the worst possible distribution in Γ.

The presented approach is based on the results provided by Scarf [22] in his original work about an inventory problem, which has been further re<sup>fi</sup>ned by other authors in different contexts (see, for example, [13,15,16]). Considering the expected cost model expressed in Eq. (2), according to the results reported in [5], we can write (see Appendix A):

$$
E [ C (x, B) ] \leq Q + \frac {c _ {D}}{2} \left[ \sqrt {\sigma^ {2} + (B - \mu) ^ {2}} - (B - \mu) \right] + c _ {B} \cdot B.\tag{6}
$$

As it is possible to verify, the right part of Eq. (6) is convex in $B ,$ and represents an upper bound for the expected cost. Therefore, setting the derivative of the upper bound to zero and solving for B, we obtain the following rule:

$$
B ^ {*} = \left\{ \begin{array}{c l} \mu - \sigma \cdot \omega & \text { if } c _ {D} <   2 c _ {B} \\ \mu & \text { if } c _ {D} = 2 c _ {B} \\ \mu + \sigma \cdot \omega & \text { if } c _ {D} > 2 c _ {B} \end{array} \right.\tag{7}
$$

where

$$
\omega = \frac {\left| c _ {D} - 2 c _ {B} \right|}{2 \sqrt {c _ {B} \left(c _ {D} - c _ {B}\right)}}\tag{8}
$$

Eq. (7) further imposes the condition $c _ { D } > c _ { B } > 0 ,$ , and provides the value of $B ^ { * }$ that minimizes the upper bound of the expected total cost against the worst possible distribution of the delay x. We further discuss this result in the next section.

## 5. Results and discussion

We present and discuss some computational results comparing the distribution-free model against two of the most commonly used probability distributions: the normal distribution (which is the highest entropy distribution with given mean and standard deviation) and the uniform distribution (representing the case where the probability of occurrence of each delay is the same, thereby illustrating the most unpredictable situation).

In the following, we refer to three models: M1 (distribution-free), M2 (normal distribution as described in Section 4.2), and M3 (analogous to M2, but with uniform distribution).

Since in the M1 model we minimized the upper bound of the expected cost (and not the expected cost directly), we are interested in comparing the following two aspects of the models: i) the size of the buffer in each model as a function of $c _ { D }$ and $c _ { B } ,$ and ii) the actual costs obtained in simulated test instances.

## 5.1. The sizes of the buffers

As evidenced in the previous discussion, the size of the buffer B strongly depends on the mean μ, the standard deviation $\sigma ,$ the ratio $\beta ,$ and the probability distribution F. By comparing the size of the buffers provided by the different models M1, M2, and M3, under the same parameters (mean, standard deviation, and costs), we want to evaluate the extent of the difference among the results. Thus, we compared the sizes of the buffers provided by the three models according to changes in $\beta .$

Let us assume, for the sake of the example, $c _ { D } = 1 0 0 , \mu = 1 0$ , and $\sigma { = } 2 ,$ , and let us evaluate the size of the buffer in M1, M2, and M3 for different values o $\mu$ by varying $c _ { B } .$

Consistent with the result provided by Scarf [22], as is possible to see in Fig. 4, the size of the buffers of the distribution-free model and the normal model is close to each other for values of $\beta$ between 0.1 and 0.9. More precisely, in such a range the difference is less than 1%, as already reported in [17], where the authors pointed out the potential relation between the distribution-free model and the normal distribution model.

Greater differences are involved when considering model M3. Nonetheless, the maximum difference between M1 and M3 for values of β in the range [0.1, 0.9] is consistently below 7%.

We can observe that, for low values of β, model M1 involves a bigger buffer, while for higher values the distribution-free model is more willing than models M2 and M3 to take risks and react to disruptions, incurring delivery delay recovery costs. Therefore, in situations where distributional information on the previous delivery performance of a supplier is not known, and the objective is to minimize the expected cost, the optimal strategy is to emphasize risk adversity when $\beta { \leq } 0 . 1$ by detaining a bigger buffer; on the other hand, from a cost minimization point of view it is optimal to bear more risk when $\beta { \geq } 0 . 9$

This result is sound from a theoretical standpoint; however, it is necessary to assess the actual impact of the optimal strategy suggested by the distribution-free model when facing random delays. This aspect is addressed in the next section.

## 5.2. Expected cost comparison

The theoretically based results reported in Section 5.1 do not allow us to answer the following question: what is the expected result when the buffer size is evaluated with a distribution-free model, but the delays reveal afterwards to be normally (or uniformly) distributed?

To answer this question, we investigated the robustness of the distribution-free model by evaluating the cost of M1 when the delay is actually distributed as a normal or uniform random variable, and then compared the results against those provided by M2 and M3, respectively.

To this end, we randomly generated problem instances according to the following Monte Carlo-based testing framework; we describe the testing framework for the normal distribution, while the generalization to the uniform distribution is straightforward:

![](/api/attachments/7CAEDNU8/fulltext/images/10569f74f9086feb97612c036d8d46a69dbca8c05e0df0b2370532bdf62227b2.jpg)  
Fig. 4. Comparison of buffer sizes.

1) Set the value of the mean μ, the standard deviation σ, and the costs $c _ { B }$ and $c _ { D } .$ Set $F { = } \mathbb { N } ( \mu , \sigma )$ (normal distribution). $\mathsf { S e t } i = 1$

2) Evaluate the sizes of the buffers using M1 and M2.

3) Draw a random value x from the distribution $F ,$ representing the delivery delay in the ith random problem.

4) Evaluate and compare the cost $C ( x _ { i } , B ^ { h } )$ for the M1 and M2 models, where $B ^ { h }$ is the optimal buffer evaluated according to model $h { \in } \{ M 1 , M 2 \}$

5) Increment i by 1; repeat steps 3–5 1000 times.

The process is repeated for the different values of $c _ { B } ,$ in order to assess the model under different values of ratio $\beta$ (the same testing framework has been used to generate results in the case of uniformly distributed delays, substituting uniform distribution for normal distribution in step 1, and substituting M3 for M2 in steps 2 and 4).

This testing framework allows for evaluating the actual cost of the models when the delay is distributed according to a given probability distribution. To compare the results effectively, we de<sup>fi</sup>ned the following cost ratios:

$$
\begin{array}{l} \rho_ {i} ^ {N} = \frac {C (x _ {i} , B ^ {M 1})}{C (x _ {i} , B ^ {M 2})} \\ \rho_ {i} ^ {U} = \frac {C (x _ {i} , B ^ {M 1})}{C (x _ {i} , B ^ {M 3})}. \end{array}\tag{9}
$$

That is, $\rho _ { i } ^ { N }$ is the ratio of the cost of models M1 and M2 when the delay is actually distributed as a normal random variable, while $\rho _ { i } ^ { U }$ is the ratio of the cost of models M1 and M3 when the delay is actually distributed as a uniform random variable. Varying β by changing c we observe the results in Table 1 and Table 2, where some statistical measures of the cost ratios over 1000 runs are reported.

As we expected, observing Fig. 4, when $\beta = 0 . 5 ,$ , the result is not dependent upon the model used to size the buffer. On average, the performances of the models are comparable and testify to the robustness of the distribution-free model. Furthermore, the distributions of $\rho ^ { N }$ and $\rho ^ { U }$ are both right-skewed (with a few exceptions when the delays are normally distributed), indicating that the cost ratios are mainly concentrated on the left of the average.

## 5.3. Model integration

According to the architecture for a HIL-DSS presented in Fig. 2, the computational model discussed so far is meant as a building block of an articulated decision process; therefore, it requires to be seamlessly integrated into the decision <sup>fl</sup>ow, where human actors are actively involved in making decisions. The concrete integration is achieved in the “Human expert/decision maker” building block, where the preliminary decision (based on the quantitative results provided by the model) and the expert's experience and knowledge (mainly unstructured and qualitative) converge as input to determine the <sup>fi</sup>nal decision. In the investigated context and with the discussed objective, the human expert has to assess the results provided by the models critically, weighting the information that could not be algorithmically handled in the model.

Considering the delivery reliability problem, the expert has to deal with the following issues, which represent his/her contribution to overcoming the limited information that might be available for elaboration in the computational model:

• Input data reliability: the computational model is designed to deal with little information about the distribution of the delay, but assumes as known other data such as costs and, to some extent, the mean and standard deviation of the delays. Therefore, it is up to the expert to decide whether the assumed data are reliable in making a proper decision, or not. This aspect strengthens the centricity of the human expert in the HIL-DSS architecture. In the presented scenarios, the human expert has to de<sup>fi</sup>ne the costs $c _ { B }$ and $c _ { D } ,$ and their possible variation ranges. In this latter case, it is still up to the expert to vary the input data, running the model multiple times to perform a sensitivity analysis. The extent of the intervals in which the input data should vary is a critical decision that depends on the expert knowledge of the scenario he/she is dealing with.

Table 1  
Cost ratios when delays are normally distributed.

<table><tr><td> $\beta$ </td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td> $\min_{i}(\rho_{i}^{N})$ </td><td>0.896.</td><td>0.973</td><td>0.971</td><td>0.982</td><td>1.000</td><td>0.986</td><td>0.982</td><td>0.987</td><td>0.958</td></tr><tr><td> $\text{avg}(\rho_{i}^{N})$ </td><td>1.006</td><td>0.995</td><td>0.996</td><td>0.996</td><td>1.000</td><td>1.003</td><td>1.006</td><td>1.006</td><td>0.958</td></tr><tr><td> $\max_{i}(\rho_{i}^{N})$ </td><td>1.014</td><td>1.110</td><td>1.068</td><td>1.027</td><td>1.000</td><td>1.022</td><td>1.045</td><td>1.055</td><td>1.005</td></tr><tr><td> $\text{Std. dev}(\rho_{i}^{N})$ </td><td>0.024</td><td>0.042</td><td>0.035</td><td>0.018</td><td>0.000</td><td>0.015</td><td>0.026</td><td>0.026</td><td>0.014</td></tr><tr><td> $\text{Skewness}(\rho_{i}^{N})$ </td><td>-3.081</td><td>1.505</td><td>0.823</td><td>0.527</td><td>0.000</td><td>0.362</td><td>0.787</td><td>1.390</td><td>-2.535</td></tr></table>

• Contingent factors: even in those cases where the data are highly reliable and well representative of the past performance of a supplier, the expert may be aware of recent (or soon to come) events that may temporarily or permanently change the scenario, such as cost structure changes or supplier interventions to cut lead times, which are not yet re<sup>fl</sup>ected in the past data. This knowledge supports the evaluation of the solution and, in this case, the need to rerun the model for comparative purposes. Also in this case, the central role of the human expert is further emphasized.

• Alternative solutions other than buffers: sometimes, the result of the model and the sensitivity analysis may indicate unbearable cost levels. In this case, the expert should be able to devise alternative solutions that do not leverage on the buffer, such as changes in the process/product design, or changes in the supplier base, and so forth. The same statement can be made in case the expert acknowledges that a contingent factor becomes a structural factor (a permanent change), therefore requiring a different approach to the overall problem.

• Level of risk the decision maker is willing to take: each decision involves risk to some extent. The model can be used under different input data hypotheses, providing different solutions with a different degree of associated risk. Therefore, it is up to the expert to discern which one is the best, according to the level of risk he/she wants to take.

All of the elements discussed above, along with other, contextspeci<sup>fi</sup>c ones, may considerably in<sup>fl</sup>uence the <sup>fi</sup>nal decision about the buffer sizes, which not necessarily coincidences with the calculated results of the computational model.

## 6. Conclusions and future work

In order to deal with delivery delay risk mitigation in a context characterized by limited information, we developed two distinct computational models that form the algorithmic foundation for developing a new, or adapting an existing, DSS. However, besides this well-de<sup>fi</sup>ned logic, there is still a need for human involvement in evaluating the results provided by the decision models and effectively taking actions by adjusting, for instance, inventory control or negotiation strategies with particular suppliers. As stated by Subramania and Khare [25], this involvement is indispensable, since it “enables decisions to be based on experience and also factors which are nonquanti<sup>fi</sup>able that cannot be easily implemented algorithmically.” The results developed in this paper must therefore be applied in a HIL-DSS setting.

Table 2  
Cost ratios when delays are uniformly distributed

<table><tr><td> $\beta$ </td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td> $\min_{i}(\rho_{i}^{N})$ </td><td>0.987</td><td>0.918</td><td>0.920</td><td>0.950</td><td>1.000</td><td>0.960</td><td>0.950</td><td>0.961</td><td>0.995</td></tr><tr><td> $\text{avg}(\rho_{i}^{N})$ </td><td>0.997</td><td>0.994</td><td>0.995</td><td>0.995</td><td>1.000</td><td>1.012</td><td>1.025</td><td>1.028</td><td>1.003</td></tr><tr><td> $\max_{i}(\rho_{i}^{N})$ </td><td>1.120</td><td>1.326</td><td>1.187</td><td>1.075</td><td>1.000</td><td>1.066</td><td>1.142</td><td>1.198</td><td>1.047</td></tr><tr><td> $\text{Std. dev}(\rho_{i}^{N})$ </td><td>0.031</td><td>0.132</td><td>0.100</td><td>0.049</td><td>0.000</td><td>0.045</td><td>0.080</td><td>0.090</td><td>0.015</td></tr><tr><td> $\text{Skewness}(\rho_{i}^{N})$ </td><td>2.720</td><td>1.298</td><td>0.666</td><td>0.236</td><td>0.000</td><td>0.322</td><td>0.713</td><td>1.264</td><td>2.529</td></tr></table>

In this sense, our architecture for a HIL-DSS extends the conceptualization discussed in [25] by explicitly differentiating between a decision model as a formalized representation of the problem-solving approach, a preliminary decision as suggested output from the DSS, and a final decision made by the human expert, who also takes external factors into account. Acknowledging the important role of a human expert within a HIL-DSS, we think that the developed algorithmic foundation presented in this paper is encouraging, as it builds a solid basis for decision making.

We advocate the following points as the main advantages of the proposed approach:

• Flexibility and robustness of the computational model: <sup>fl</sup>exibility is ensured by the possibility of applying the model to contexts with either a known or unknown probability distribution of the delay. The robustness is given by the assumptions underlying the distribution-free approach, where the results are formulated to provide the best solution against the worst situations among those characterized by a given mean and standard deviation.

• Fewness of input variables: the model requires the de<sup>fi</sup>nition (or estimation) of few input variables, such as the mean and average of previous delays (or an educated guess) and the costs c and c . This limited number of variables eases the implementation, run, and use of the model in a DSS.

• Integration of the computational model with subjective elements and expertise: a computational model encompassing all of the aspects that characterize reality is hardly achievable and manageable. To overcome this issue, the model is intended to be complemented with judgmental elements provided by a human expert. Therefore, the computational model provides data that can be used as input by the human decision maker in formulating a complex decision.

## 6.1. Potential limitations and proposed amendments

We identi<sup>fi</sup>ed two main limitations that affect the proposed architecture when dealing with real-life situations. In this section, we brie<sup>fl</sup>y discuss possible actions that can be undertaken in order to overcome the following limitations:

• One of the main issues arising in applying the proposed approach may be the de<sup>fi</sup>nition of the costs $c _ { B }$ and $c _ { D } ,$ which depend on the speci<sup>fi</sup>c context. Generally, only approximations are available, mainly because of the dif<sup>fi</sup>culties in recording actual costs; therefore, the quality of the solutions provided by the computational model is strongly correlated with the quality of the input data, as pointed out in Section 5.3. Nevertheless, this limitation of the quantitative model is compensated for by the presence of the human expert in the HIL-DSS, who may decide how to run the model multiple times for sensitivity analysis, overcoming this limitation.

• Another limitation is the necessity of expressing the buffer in terms of days of coverage, which depends upon the rate of consumption of the buffered resource. In this respect, problems may arise in volatile contexts, where the consumption of resources may vary in time, leading to potential problems (i.e., if the rate of resource consumption increases signi<sup>fi</sup>cantly, the buffer is depleted in advance with respect to expectations, exposing the company to stock-out situations). To tackle this issue, a viable option of extending the described approach may be the implementation of a scenario analysis support in the DSS, helping the human decision maker by providing results based on distinct scenarios, each characterized by different rates of consumption.

## 6.2. Future work directions

At the time of writing, a prototypical instantiation of the model has been developed to perform the analysis presented in this paper. Even though future work should be directed at developing usable versions for practical applications, thanks to the analytical procedure adopted in the development of the computational model, the results will not be dependent on the speci<sup>fi</sup>c implementation. The main differences, indeed, will be related mostly to the connection to the main sources of data (i.e., the company ERP) and the graphical user interface (GUI).

An interesting extension of this approach could be matching the calculated decisions and the estimated values by subject matter experts, in order to identify the potential root causes of striking differences in buffer sizing.

## Appendix A

Lemma.

$$
E [ C (x, B) ] \leq Q + \frac {c _ {D}}{2} \left[ \sqrt {\sigma^ {2} + (B - \mu) ^ {2}} - (B - \mu) \right] + c _ {B} \cdot B.\tag{A.1}
$$

Proof. We know that:

$$
E [ C (x, B) ] = E \left[ Q + c _ {D} (x - B) ^ {+} + c _ {B} \cdot B \right] = Q + c _ {B} \cdot B + c _ {D} \cdot E \left[ (x - B) ^ {+} \right] \tag {A.2}
$$

where $( x - B ) ^ { + } = \operatorname* { m a x } ( x - B ; 0 )$ . Therefore, we have to show that:

$$
E \left[ (x - B) ^ {+} \right] \leq \frac {1}{2} \left[ \sqrt {\sigma^ {2} + (B - \mu) ^ {2}} - (B - \mu) \right].\tag{A.3}
$$

To this end, notice that:

$$
(x - B) ^ {+} = \frac {| x - B | + (x - B)}{2}.\tag{A.4}
$$

According to the Cauchy–Schwarz inequality, we can state:

$$
E [ | x - B | ] \leq \left(E \left[ (x - B) ^ {2} \right]\right) ^ {\frac {1}{2}}.\tag{A.5}
$$

Expanding the term under square root we obtain:

$$
E \left[ x ^ {2} - 2 \cdot B \cdot x + B ^ {2} \right] = E \left[ x ^ {2} \right] - 2 \cdot B \cdot E [ x ] + B ^ {2}.\tag{A.6}
$$

Since by de<sup>fi</sup>nition:

$$
\begin{array}{l} E [ x ] = \mu \\ \sigma^ {2} = E \Big [ x ^ {2} \Big ] - E [ x ] ^ {2} \end{array}\tag{A.7}
$$

we can state:

$$
E \left[ (x - B) ^ {2} \right] = \sigma^ {2} + \mu^ {2} - 2 \cdot B \cdot \mu + B ^ {2} = \sigma^ {2} + (B - \mu) ^ {2}.\tag{A.8}
$$

Therefore, substituting Eq. A.8 in Eq. A.5:

$$
\mathrm{E} [ | x - B | ] \leq \left(\sigma^ {2} + (B - \mu) ^ {2}\right) ^ {\frac {1}{2}}
$$

and, <sup>fi</sup>nally, taking the expectation of Eq. A.4:

<sub>ð</sub>A:9<sub>Þ</sub>

$$
E \left[ (x - B) ^ {+} \right] \leq \frac {1}{2} \left[ \sqrt {\sigma^ {2} + (B - \mu) ^ {2}} - (B - \mu) \right]\tag{A.10}
$$

we complete the proof.

## References

[1] M. Caputo, Uncertainty, <sup>fl</sup>exibility and buffers in the management of the <sup>fi</sup>rm operating system, Production Planning and Control 7 (5) (1996) 518–528

[2] Y.S. Chang, J.K. Lee, Case-based modi<sup>fi</sup>cation for optimization agents: AGENT-OPT, Decision Support Systems 36 (4) (2004) 355–370.

[3] M.L. Cummings, The need for command and control instant message adaptive interfaces: lessons learned from tactical Tomahawk human-in-the-loop simula tions, Cyberpsychology & Behavior 7 (6) (2004) 653–661.

[4] P. Frame, Saturn to <sup>fi</sup>ne suppliers \$500/minute for delays, Automotive News 21 (12) (1992) 36.

[5] G. Gallego, I. Moon, The distribution free newsboy problem: review and extensions, The Journal of the Operational Research Society 44 (8) (1993) 825–834.

[6] A. Gunasekaran, C. Patel, E. Tirtiroglu, Performance measures and metrics in a supply chain environment, International Journal of Operations & Production Management 21 (1/2) (2001) 71–87.

[7] V. Hill, T.E. Vollmann, Reducing vendor delivery uncertainties in a JIT environment, Journal of Operations Management 5 (4) (1986) 381–392.

[8] Y. Hung, C. Chang, Determining safety stocks for production planning in uncertain manufacturing, International Journal of Production Economics 58 (2) (1999) 199–208.

[9] V.R. Kannan, K.C. Tan, Supplier selection and assessment: their impact on business performance, Journal of Supply Chain Management 38 (4) (2002) 11–21.

[10] B. Kingsman, L. Hendry, A. Mercer, A.D. Souza, Responding to customer enquiries in make-to-order companies: problems and solutions, International Journal of Production Economics 46–47 (1) (1996) 219–231.

[11] D. Krause, T. Scannell, R. Calantone, A structural analysis of the effectiveness of buying <sup>fi</sup>rms: strategies to improve supplier performance, Decision Sciences 31 (1) (2000) 33–55.

[12] L. Lapide, How buffers can mitigate risk, Supply Chain Management Review 4 (2008) 6–7.

[13] Lee, S. Hsu, The effect of advertising on the distribution-free newsboy problem, International Journal of Production Economics 129 (1) (2011) 217–224.

[14] H.L. Lee, V. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review 38 (3) (1997) 93–102

[15] R. Lin, W.T. Chouhuang, G.K. Yang, C. Tung, An improved algorithm for the minimax distribution-free inventory model with incident-oriented shortage costs, Operations Research Letters 35 (2) (2007) 232–234.

[16] I. Moon, S. Choi, The distribution free newsboy problem with balking, Journal of the Operational Research Society 46 (4) (1995) 537–542.

[17] I. Moon, S. Choi, Distribution free procedures for make-to-order (MTO), make-in-advance (MIA), and composite policies, International Journal of Production Economics 48 (1) (1997) 21–28.

[18] I. Moon, W. Yun, The distribution free job control problem, Computers and Industrial Engineering 32 (1) (1997) 109–113.

[19] I.V. Nieuwenhuysea, N. Vandaele, The impact of delivery lot splitting on delivery reliability in a two-stage supply chain, International Journal of Production Economics 104 (2) (2006) 694–708

[20] R. Parasuraman, T.B. Sheridan, C.D. Wickens, A model for types and levels of human interaction with automation, IEEE Transactions on Systems, Man, and Cybernetics 30 (3) (1997) 286–297.

[21] R. Russell, B. Taylor, Operations Management: Focusing on Quality and Competi tiveness, Prentice-Hall, New York, 1998.

[22] H.E. Scarf, A min–max solution of an inventory problem, in: K. Arrow, S. Karlin, H.E. Scarf (Eds.), Studies in the Mathematical Theory of Inventory and Production, Stanford University Press, Stanford, 1958, pp. 201–209.

[23] G.J. Stalk, T.M. Hout, Competing Against Time: How Time-based Competition is Reshaping Global Markets, Free Press, New York, 1990.

[24] K. Stecke, S. Kumar, Sources of supply chain disruptions, factors that breed vulnerability, and mitigating strategies, Journal of Marketing Channels 16 (3) (2009) 193–226.

[25] H.S. Subramania, V.R. Khare, Pattern classi<sup>fi</sup>cation driven enhancements for human-in-the-loop decision support systems, Decision Support Systems 50 (2) (2011) 460–468.

[26] T.L. Urban, Establishing delivery guarantee policies, European Journal of Operational Research 196 (3) (2009) 959–967.

[27] R. Verma, M.E. Pullman, An analysis of the supplier selection process, Omega 36 (6) (1998) 739–750.

[28] G.A. Zsidisin, A. Panelli, R. Upton, Purchasing organization involvement in risk assessments, contingency plans, and risk management: an exploratory study, Supply Chain Management: An International Journal 5 (4) (2000) 187–197.

Roberto Pinto is an Assistant Professor at the University of Bergamo. He graduated in Management Engineering from the Politecnico di Milano, and received his PhD in Design and Management of Integrated Production-Logistics Systems at the University of Brescia. He has published three books and more than 20 papers in international journals and conference proceedings. His current research interests focus on the logistics and supply chain management area, with speci<sup>fi</sup>c activities devoted to the supply chain risk management <sup>fi</sup>eld and supply chain performance and analytics.

Tobias Mettler is a project manager at the Institute of Information Management at the University of St. Gallen where he is leading the Competence Center Health Network Engineering. His research interests are in the area of design science research, systems analysis, business models, and electronic healthcare. He is actively involved in several national and international research projects related to the transformation of the healthcare industry. He received his degree in Information and Technology Management and PhD in Management of the University of St. Gallen.

Marco Taisch is a Full-Time Professor of Advanced Manufacturing Systems at Politecnico di Milano. He has been the Director of the Executive MBA and the full-time International MBA of the School of Management of Politecnico di Milano. His current research interests are in the area of operations and supply chain management, with particular focus on design and management of intelligent production systems, sustainable and energy-ef<sup>fi</sup>cient manufacturing and industrial services. He has published four books and more than 115 papers in international journals and conference proceedings. He took part in national and international funded projects. He is a member of the IEEE Engineering Management Society, IEEE Man, Systems and Cybernetics Society and senior member of the IIE Institute of Industrial Engineers. He chairs the IFIP Working Group 5.7 on Advances in Production Management Systems since 2007.
