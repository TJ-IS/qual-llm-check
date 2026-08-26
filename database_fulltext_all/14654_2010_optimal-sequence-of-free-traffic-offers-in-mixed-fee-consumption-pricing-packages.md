---
otero_id: 14654
otero_key: "BWY25493"
title: "Optimal sequence of free traffic offers in mixed fee-consumption pricing packages"
authors: "Maurizio Naldi; Andrea Pacifici"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2010.08.030"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal sequence of free traf<sup>fi</sup>c offers in mixed fee-consumption pricing packages

Maurizio Naldi <sup>a,</sup>⁎, Andrea Pacifici <sup>b</sup>

<sup>a</sup> Dipartimento di Informatica, Sistemi e Produzione, Università di Roma “Tor Vergata”, Rome, Italy

<sup>b</sup> Dipartimento di Ingegneria dell'impresa, Università di Roma “Tor Vergata”, Rome, Italy

## a r t i c l e i n f o

Article history: Received 18 March 2009 Received in revised form 2 August 2010 Accepted 17 August 2010 Available online 24 August 2010

Keywords: Pricing Churn Customer management Telecommunications

## a b s t r a c t

Customer migration, a.k.a. churn, is a relevant phenomenon in the telecommunications sector. Service providers may limit the extent of churning by winning back leaving customers through better pricing packages. The proposal of a new pricing package and the subsequent acceptance/rejection decision by the customer trigger a back-and-forth interaction till either the customer accepts the proposal or the providers stop providing a new proposal. The case of a pricing scheme based both on a fee and on a consumption-based rate (with a free traf<sup>fi</sup>c level included in the bundle) is analysed, assuming that the customer's demand is statistically known and described by either the exponential or the Rayleigh probability distribution. The service provider may adjust its offer after the customer's rejection by increasing the amount of free traf<sup>fi</sup>c. For this scenario we provide: a) the stopping conditions for the maximum amount of free traf<sup>fi</sup>c; b) the optimal sequence of proposals (i.e., that maximizing the expected marginal pro<sup>fi</sup>t of the provider). The analysis is then briefly extended to the case of simultaneous updating of both the free traffic amount and the unit price.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The liberalization of telecommunications services has allowed the entry of a number of competing operators in the market. A natural consequence of the end of the monopolistic era is that users are allowed to migrate from an operator to another. Examples of services for which migration is quite a signi<sup>fi</sup>cant phenomenon are the following:

– Number portability;

– Carrier selection;

– ADSL subscription;

– LLU (local loop unbundling).

The phenomenon of customer migration is not new, having been studied in markets different than telecommunications, e.g., to evaluate the loyalty to a brand or a product and predict the probability of repeated purchases or the value of a current customer [8,12]. An alternative name for the phenomenon is provider switching, while the erosion of the customer base due to migration is named churn. The intensity by which customers migrate is typically represented by the churn rate, i.e., the proportion of customers that abandons their former operator within a given timeframe (typically one month or one year). Some data concerning the monthly churn rates are reported in Table 1 for a worldwide survey, con<sup>fi</sup>rming that operators may lose around a quarter of their customers per year [14].

Churning is quite a damaging phenomenon for the abandoned (losing) provider, due to the loss of the corresponding <sup>fl</sup>ow of revenues. Though the customer base may be maintained by the acquisition of new customers, service providers incur much higher expenses when attempting to win new customers than when retaining existing ones. Hence, providers prefer to reduce churn by trying to retain their prospective churners. Computer-assisted churn management systems have been devised for this purpose (see [6]). Essential features of such systems are: churn prediction and identi<sup>fi</sup>cation of potential churners; de<sup>fi</sup>nition and realization of retention actions towards prospective churners. These features allow to delineate a preventive strategy, whereby customers' dissatisfaction is dealt with prior to the appearance of the intention to migrate. However, if a customer has already asked to leave, the provider has to resort to a reactive strategy. The most relevant tool at the disposal of the provider to win back the customer is the rede<sup>fi</sup>nition of the pricing package in order to make it more attractive to the migrating customer. Such rede<sup>fi</sup>nition has to be customized for each customer and therefore represents an instance of differentiated pricing (see [5], where an auction-based mechanism is proposed to maximize revenues for a service provider facing different classes of customers who express individual pricing requirements and service levels needs). The rede<sup>fi</sup>nition can go through several stages, offering better and better packages (till the economic sustainability limit), should the customer refuse. So, we can imagine a back-and-forth interaction between the service provider and the customer, with the service provider offering a pricing package and the customer deciding whether to accept it or to refuse it, with the rejection leading to a new (and better) package, till the eventual acceptance by the customer or the stoppage of offers by the provider. When rede<sup>fi</sup>ning the pricing package, the provider has anyway to choose (possibly in an optimal way) the pricing parameters of the package.

Table 1  
Average monthly churn rates around the world [%].

<table><tr><td>Region</td><td>Q1 2005</td><td>Q1 2006</td></tr><tr><td>World</td><td>2.1</td><td>2.3</td></tr><tr><td>Africa</td><td>2.6</td><td>3.4</td></tr><tr><td>Americas</td><td>2.3</td><td>2.3</td></tr><tr><td>Asia and Pacific</td><td>2.0</td><td>2.3</td></tr><tr><td>Eastern Europe</td><td>2.5</td><td>2.9</td></tr><tr><td>Western Europe</td><td>1.9</td><td>1.9</td></tr><tr><td>Middle East</td><td>2.4</td><td>3.2</td></tr><tr><td>USA/Canada</td><td>2.0</td><td>1.9</td></tr></table>

In this paper we deal with this problem, namely the optimal rede<sup>fi</sup>nition of a parameter of the pricing package. We introduce a model both for the interaction between the provider and the customer, and for the customer's behaviour, and derive the optimal offer at each stage of the back-and-forth sequence of exchanges between the customer and the service provider. Optimality is to be meant as the maximization of the expected revenues. We develop our methodology in the context of the most widely deployed two-part tarif<sup>fi</sup>ng scheme (see Section 2), whose parameters are the unit price and a free traf<sup>fi</sup>c value, de<sup>fi</sup>ning two scenarios for the traf<sup>fi</sup>c generated by customers (see Section 3) and considering the reaction of customers, who can either accept or refuse the offer (see Section 5). In this context we <sup>fi</sup>rst consider a strategy consisting in updating the free traf<sup>fi</sup>c offer only (keeping the unit price <sup>fi</sup>xed), and provide: a) upper bounds for the amount of free traf<sup>fi</sup>c that the service provider can offer keeping positive pro<sup>fi</sup>ts, in Section 4; b) the optimal sequence of offers as that maximizing the expected pro<sup>fi</sup>ts at each stage, in Section 6. Numerical examples of such optimal sequences are then reported in Section 7 for some typical instances. In addition we consider in Section 8 a strategy that jointly optimizes both the unit price and the free traf<sup>fi</sup>c amount.

## 2. Pricing packages

A tool commonly employed by service providers to <sup>fi</sup>ght churn is the proper de<sup>fi</sup>nition of a pricing package attractive for the user. Prospective churners can in fact renege to migrate to a different provider if the prices proposed by their present provider appear to be convenient. It is therefore expected that any provider puts a lot of effort into the de<sup>fi</sup>nition of the pricing scheme, especially in reply to the declared intention of the customer to leave. In this section we describe a mixed fee-consumption pricing package in the context of the reactive strategy of the losing provider.

Pricing schemes employed in telecommunications services are typically built around two components: a <sup>fi</sup>xed fee and/or a variable portion related to service usage. The <sup>fi</sup>xed fee may include an amount of free traf<sup>fi</sup>c, while the price paid for the traf<sup>fi</sup>c exceeding the free level typically grows linearly with the traf<sup>fi</sup>c itself. Such two-part structures have been adopted for telephone services for a long time now, and multi-part schemes have also been proposed, where the rate used for pricing the excess traf<sup>fi</sup>c gets lower as the traf<sup>fi</sup>c grows (see, e.g., Section 9.5.2 of [13]). However, their adoption has been advocated for non telephone services as well, so that two-part structures appear as the most likely pricing scheme for integrated IP networks. In these hybrid schemes four components can be envisaged, representing respectively the <sup>fi</sup>xed part and three possible variable components [3]:

– Flat fee (e.g., per month);

– Unit price per minute (e.g., for voice or for real time and streaming services);

– Unit price per Mbyte (e.g., for <sup>fi</sup>le transfer and other elastic traf<sup>fi</sup>c streams);

– Unit price per event (e.g., per message).

Though per-event charging could represent the largest growing segment, the likely scheme is anyway of the mixed fee-consumption type, where the <sup>fi</sup>xed fee allows for a free amount of traf<sup>fi</sup>c (the traf<sup>fi</sup>c being measured in units depending on the pricing scheme, e.g., one of the three types listed above). In this paper we consider therefore that the customer's expenditure S over the billing period (e.g., a month) for a consumption x is given by the following expression (see Fig. 1):

$$
S = \left\{ \begin{array}{c l} d & \text {if} x \leq b \\ d + p (x - b) & \text {if} x > b \end{array} \right.\tag{1}
$$

where d is the fee for the billing period, b is the amount of free traf<sup>fi</sup>c that comes with the fee, and p is the rate (i.e., the unit price for the traf<sup>fi</sup>c exceeding b). The latter quantities represent the three leverages the provider can use to tailor the offer and attract the user. Though a complex strategy may rely on the simultaneous use of all the three factors, this can make comparisons between different offers dif<sup>fi</sup>cult for the customer and induce some confusion, which may in the end be counterproductive. In this paper we consider therefore a tarif<sup>fi</sup>ng scheme employing a single parameter, and focus on the proper choice of the free traf<sup>fi</sup>c level. In Section 8 we extend our analysis to the case where two parameters, namely the unit price and the free traf<sup>fi</sup>c level, may vary, and we provide sample results.

We illustrate <sup>fi</sup>rst the chain of events in the case of the strategy employing the free traf<sup>fi</sup>c as the only leverage. In reaction to a customer willing to leave, the provider may propose a new pricing package with a new, larger value of the free traf<sup>fi</sup>c level. The response of the customer is expected to be binary: either it accepts the proposal, and stays with its current provider, or refuses it. At this stage the provider may decide to go on and submit a new proposal with a larger free traf<sup>fi</sup>c level and again the customer may either accept or refuse. The whole process is therefore represented by a sequence of offers characterized by rising values of the traf<sup>fi</sup>c included in the <sup>fi</sup>xed fee $\{ b _ { 1 } , b _ { 2 } , . . . \} , \ b _ { j } > b _ { j - 1 } ( j = 2 , 3 , . . . )$ . The sequence of offers may be stopped at any time either by the customer, if it accepts the offer, or by the service provider, if it decides not to propose a new offer. The service provider may quit, e.g., because it deems the customer no longer pro<sup>fi</sup>table or because its con<sup>fi</sup>dence in the success of further counterproposals is very low.

![](/api/attachments/BWY25493/fulltext/images/a45ab3f4df664668b1308857b4aba86b67e1312f9e14d4082714fd628b9cd1f4.jpg)  
Fig. 1. The fee-consumption pricing package.

We may assume that the losing service provider doesn't know the alternative pricing package proposed to its customer by its competing provider. The natural problem for the losing provider, dealt with in this paper, is the proper de<sup>fi</sup>nition of the sequence of free traf<sup>fi</sup>c levels $b _ { j } .$

In the alternative strategy the provider updates at the same time the unit price and the free traf<sup>fi</sup>c offer. We have then a sequence of pairs $\{ ( b _ { 1 } , p _ { 1 } ) , ( b _ { 2 } , p _ { 2 } ) , \ldots \} , ( j = 2 , 3 , \ldots )$ . Each new offer has to be better than the previous one on the whole (i.e., leaving to savings for the customer), so that we cannot have at the same time $p _ { j } { > } p _ { j - 1 }$ and $b _ { j } < b _ { j - 1 } .$

The following sections from Section 3 throughout Section 7 refer to the strategy based on the free traf<sup>fi</sup>c only. The strategy that updates both variables in the pricing package, i.e., the unit price and the free traf<sup>fi</sup>c, is dealt with in Section 8.

## 3. Customer's traf<sup>fi</sup>c distribution

The revenues gained under the pricing package described by expr. (1) depend on the value of the traf<sup>fi</sup>c developed by the customer. Since that demand is random, its characterization by a probability density function is needed. Though in principle a characterization for the single customer could be considered, the amount of available statistical data would be quite low for the required accuracy. We assume therefore that, for the purpose of characterizing the traf<sup>fi</sup>c demand, customers are segmented into homogeneous classes. Classes may be de<sup>fi</sup>ned in various ways, e.g., through the average bill or by socio-demographic features. Here we do not enter into the details of possible classi<sup>fi</sup>cations, but assume that such classi<sup>fi</sup>cation is available together with the probability density function of the traf<sup>fi</sup>c demand for the class of interest. Very few works have appeared in the literature concerning the statistical characterization of customers' consumption levels over a billing period. National regulating authorities typically provide time series of the average bill for the whole population of customers (see, e.g., [1]). In some cases the most relevant percentiles of monthly or annual traf<sup>fi</sup>c volumes are also made public, as in the Australian market [10] or in Great Britain [9] for mobile customers.

In this paper we consider two alternative models for the probability density function of the traf<sup>fi</sup>c developed by the customer during a billing period: the exponential model and the Rayleigh one. Though the quantities envisaged to represent the consumption x in Section 2 (i.e., minutes, Mbytes, and events) are all discrete, we use two models for continuous variables; the values involved are in fact so large that we can neglect their granularity. The exponential distribution represents an extension of the well established hypothesis for the traf<sup>fi</sup>c intensity in the telephone network (Poisson model for the call interarrival times and exponential model for the call duration). Indicating by $\mu _ { X }$ the average traf<sup>fi</sup>c value, the probability density function for the traf<sup>fi</sup>c X is

$$
f _ {X} (x) = \frac {1}{\mu_ {X}} \exp \left(- \frac {x}{\mu_ {X}}\right).\tag{2}
$$

The alternative Rayleigh model assumes instead that the random traf<sup>fi</sup>c demand by a customer within a given class is somehow gathered around a central, most likely value. Its probability density function is

$$
f _ {X} (x) = \frac {\pi}{2} \cdot \frac {x}{\mu_ {X} ^ {2}} \exp \left(- \frac {\pi}{4} \cdot \frac {x ^ {2}}{\mu_ {X} ^ {2}}\right).\tag{3}
$$

Both models are represented for comparison in Fig. 2 for a sample value of the average traf<sup>fi</sup>c.

Though in both Eqs. (2) and (3) the expected value is represented as the constant $\mu _ { X } ,$ we consider in the following the general case where the expected value is a function of the free traf<sup>fi</sup>c level itself. In fact, it is reasonable to expect that, as the provider increases the amount of free traf<sup>fi</sup>c available to a customer, that customer will likewise increase its consumption. Hence, we expect the expected traf<sup>fi</sup>c volume $\mu _ { X }$ to be a growing function of the free traf<sup>fi</sup>c level b. Here we assume a linear relationship between these two quantities:

![](/api/attachments/BWY25493/fulltext/images/f50aa3fd35fef9fb01931077b6b3b92c6465db04344fd0c1f1686753dfa2394e.jpg)  
Fig. 2. Probability density functions $( \mu _ { X } = 1 0 0 )$

$$
\mu_ {X} = \mu_ {0} + \beta b,\tag{4}
$$

where $\mu _ { 0 }$ is the average traf<sup>fi</sup>c when the customers have to pay the unit price p for all the traf<sup>fi</sup>c they use, and β is the marginal increase in the expected traf<sup>fi</sup>c as a response to a unit increase of the free traf<sup>fi</sup>c level (we will refer to $\beta$ as the marginal consumption increase). The admissible range of values for $\beta$ is the <sup>fi</sup>eld of non-negative real numbers (β≥0), where $\beta = 0$ corresponds to the case of consumption unaffected by the level of free traf<sup>fi</sup>c, and $\beta { > } 0$ when the consumption increases as an effect of the offer of free traf<sup>fi</sup>c; we will refer to the latter case as the incentivized consumption (IC) case.

## 4. Service provider's pro<sup>fi</sup>t

The decision by the service provider to retain a customer is based on the expected pro<sup>fi</sup>tability of that customer. The service provider will put forward a new offer as long as the expected pro<sup>fi</sup>t (to be obtained from that customer) is positive, as determined by the expected consumption level and the prospective free traf<sup>fi</sup>c level. The decision as to the latter is therefore driven by the customer's pro<sup>fi</sup>tability. In this section we provide expressions for the service provider's pro<sup>fi</sup>t when the customer accepts the offer, and determine the conditions for pro<sup>fi</sup>tability.

In particular we consider the marginal pro<sup>fi</sup>t on a customer, i.e., the pro<sup>fi</sup>t to be gained by retaining that customer. That pro<sup>fi</sup>t is random, since it depends on the traf<sup>fi</sup>c generated by that customer. Recalling the pricing expression (1) we have the marginal pro<sup>fi</sup>t

$$
R = \left\{ \begin{array}{c l} d - c & \text {if} X \leq b \\ d - c + p (X - b) & \text {if} X > b \end{array} \right.,\tag{5}
$$

where c is the marginal cost related to the customer's retention, i.e., the sum of the contact cost for the retention procedure and of the operational cost incurred to serve that customer over the same period over which the revenues are computed. Sunk costs, such as the capital cost incurred in building the network are not to be considered in the decision to provide a new offer [4]. A suf<sup>fi</sup>cient condition for positive marginal pro<sup>fi</sup>t is that the fee is large enough to recoup the marginal cost, i.e., d Nc. However, if this condition is not satis<sup>fi</sup>ed, the provider can still attain a positive marginal pro<sup>fi</sup>t by relying on the consumption exceeding the free level. The expected marginal pro<sup>fi</sup>t is

$$
\mu_ {R} = E [ R ] = d - c + p \int_ {b} ^ {\infty} (x - b) f _ {X} (x) d x.\tag{6}
$$

For the exponential and Rayleigh traf<sup>fi</sup>c distributions de<sup>fi</sup>ned in Section 3 we have respectively

$$
\mu_ {R} = \mu_ {R} (b) = d - c + p \cdot \mu_ {X} \exp \left(- \frac {b}{\mu_ {X}}\right),\tag{7}
$$

$$
\mu_ {R} = \mu_ {R} (b) = d - c + 2 p \cdot \mu_ {X} \left[ 1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b}{\mu_ {X}}\right) \right],\tag{8}
$$

where $G ( \cdot )$ is the normal cumulative distribution function, and the notation $\mu _ { R } ( b )$ highlights the dependence on the free traf<sup>fi</sup>c level. Though the above expressions are valid for any value of the free traf<sup>fi</sup>c level, we expect to have a limit value for it. In fact, the provider will keep on reiterating its retention effort by increasing the offered free level as long as $\begin{array} { r } { \mu _ { R } \ge 0 . } \end{array}$ . We can derive the maximum free traf<sup>fi</sup>c level that the provider will be willing to offer:

$$
b _ {\max} = \max \{b: \mu_ {R} (b) \geq 0 \}.\tag{9}
$$

For this derivation we consider <sup>fi</sup>rst the case when $\beta = 0$ and then $\beta { > } 0$

When the expected traf<sup>fi</sup>c value is not in<sup>fl</sup>uenced by the offered free traf<sup>fi</sup>c, $\mathrm { e . g . , } \beta \mathrm { = } 0$ and $\mu _ { X } = \mu _ { 0 }$ in expr. (4), we <sup>fi</sup>rst note that the marginal pro<sup>fi</sup>t is a decreasing function of the free traf<sup>fi</sup>c level. We can then obtain the maximum free level by equating to zero the expressions (7) and (8), respectively for the exponential and the Rayleigh case:

$$
b _ {\max} = \mu_ {0} \ln \left(\frac {p \cdot \mu_ {0}}{c - d}\right),\tag{10}
$$

$$
b _ {\max} = \sqrt {\frac {2}{\pi}} \mu_ {0} G ^ {- 1} \left(1 - \frac {c - d}{2 p \cdot \mu_ {0}}\right).\tag{11}
$$

In those expressions we note that there is a recurrent quantity that we can consider as a whole; namely we de<sup>fi</sup>ne the quantity

$$
\alpha = \frac {c - d}{p \cdot \mu_ {0}},\tag{12}
$$

which is the ratio of the traf<sup>fi</sup>c-independent net costs to the traf<sup>fi</sup>c dependent revenues if no free traf<sup>fi</sup>c is offered. In the following we will refer to it as the costs-to-potential revenues ratio for short. If we indicate the average revenues per user (if no free traf<sup>fi</sup>c were offered) by the established term $\begin{array} { r } { A R P U = d + p ^ { \cdot } \mu _ { 0 } , } \end{array}$ that ratio is related to the ARPU by the relationship

$$
\alpha = \left(1 + \frac {A R P U}{c - d}\right) ^ {- 1}.\tag{13}
$$

With the introduction of α the limit values of free traf<sup>fi</sup>c can be expressed respectively as

$$
b _ {\max} = \mu_ {0} \ln \left(\frac {1}{\alpha}\right),\tag{14}
$$

$$
b _ {\max} = \sqrt {\frac {2}{\pi}} \mu_ {0} G ^ {- 1} \left(1 - \frac {\alpha}{2}\right).\tag{15}
$$

These values represent therefore upper bounds for the sequence of free values mentioned in Section 2. In both cases, for them to exist, the following condition must hold

$$
p \cdot \mu_ {0} > c - d \Longleftrightarrow \alpha <   1.\tag{16}
$$

The presence of this condition is quite natural. It is tantamount to requiring that the current price is large enough to recover the net expenses $( c - d )$ if all the traf<sup>fi</sup>c is accounted for $( \mathrm { i } . \mathrm { e } . , b = 0 )$ . If that condition is not satis<sup>fi</sup>ed, no free traf<sup>fi</sup>c offer will be sustainable under current pricing.

We now turn to the more general case when $\beta { > } 0 .$ . We <sup>fi</sup>rst consider the exponential model for the traf<sup>fi</sup>c consumption. Having introduced the ratio α, we can rewrite the expression of the marginal pro<sup>fi</sup>t (Eq. (7)) as follows:

$$
\mu_ {R} = (c - d) \left[ \frac {1}{\alpha} \left(1 + \beta \frac {b}{\mu_ {0}}\right) \exp \left(- \frac {b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) - 1 \right],\tag{17}
$$

which is basically a function of α and of the ratio $b / \mu _ { 0 }$ . While in the no-IC case the marginal pro<sup>fi</sup>t decreased as the free traf<sup>fi</sup>c level was increased, here that may not be the case. In fact, in the IC case, when we increase the free traf<sup>fi</sup>c level b we have two contrasting effects on pro<sup>fi</sup>ts, which we may name as negative and positive feedbacks respectively. We have a negative feedback on pro<sup>fi</sup>ts, since the exemption level (i.e., the free traf<sup>fi</sup>c value, in turn representing the integration lower bound in expr. (6)) is raised. At the same time we have a positive feedback, since, when the average consumption is increased, a larger portion of the probability density function in that same expr. (6) falls within the integration domain. The net effect depends on the parameter values at hand. In Fig. 3 we can see some samples of the behaviour of the marginal pro<sup>fi</sup>t as a function of the normalized free traf<sup>fi</sup>c $b / \mu _ { 0 } ,$ , with the marginal consumption increase β as a parameter; the quantity on the Y axis is actually the marginal pro<sup>fi</sup>t normalized to the value it takes in the absence of free traf<sup>fi</sup>c $( b = 0 )$ . In that picture we see several possible types of behaviour: depending on the amount of free traf<sup>fi</sup>c, the pro<sup>fi</sup>t may decrease (as in the no-IC case) or increase.

In order to derive speci<sup>fi</sup>c results we consider the derivative of the pro<sup>fi</sup>t (Eq. (17)) with respect to the free traf<sup>fi</sup>c level b:

$$
\frac {\partial \mu_ {R}}{\partial b} = p \exp \left(- \frac {b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) \left[ \beta - \frac {1}{1 + \beta b / \mu_ {0}} \right].\tag{18}
$$

By simple manipulations of this expression we can classify the behaviour of the marginal pro<sup>fi</sup>t into three regions:

A. The marginal pro<sup>fi</sup>t is always positive and a growing function of the free traf<sup>fi</sup>c;

B. The marginal pro<sup>fi</sup>t is always positive but decays for large values of the free traf<sup>fi</sup>c;

C. The marginal pro<sup>fi</sup>t turns negative as we increase the free traf<sup>fi</sup>c.

In particular we see that the <sup>fi</sup>rst case (dominance of positive feedback) occurs when the marginal consumption increase is $\beta > 1 \colon$ increasing the free traf<sup>fi</sup>c spurs the customer to react by consuming even more than what would be compensated for by the free traf<sup>fi</sup>c offer. This would be a potentially unstable situation since the provider has the incentive to continuously increase its free traf<sup>fi</sup>c offer. However, we rapidly reach a region where the IC traf<sup>fi</sup>c consumption model $\left( \operatorname { E q . } \left( 4 \right) \right)$ is no longer valid, since the customer exhibits an intrinsic limit on its consumption capability, and in any case the law of diminishing returns would make its marginal utility negligible for high traf<sup>fi</sup>c consumption levels. Hence, in the following we do not consider this range of values for $\beta .$ Instead, if $\beta { < } 1$ , as reasonable, the marginal pro<sup>fi</sup>t reaches its minimum when the free traf<sup>fi</sup>c level has the following value:

![](/api/attachments/BWY25493/fulltext/images/b46e77f990fca8e0070bae4ed56d5a9e921b828ce7bfb873404ebafebe8a10de.jpg)  
Fig. 3. Marginal pro<sup>fi</sup>t under the exponential distribution.

$$
b = \frac {\mu_ {0}}{\beta} \left(\frac {1}{\beta} - 1\right).\tag{19}
$$

This limiting value marks the border between the downward and the upward branches of the marginal pro<sup>fi</sup>t curve for both cases B and C of the above classi<sup>fi</sup>cation. After normalizing it to the no-IC average traf<sup>fi</sup>c consumption $\mu _ { 0 } ,$ we show in Fig. 4 the free traf<sup>fi</sup>c providing the minimum pro<sup>fi</sup>t.

Turning back to the above classi<sup>fi</sup>cation, we are actually interested in examining the behaviour of the marginal pro<sup>fi</sup>t for quite low values of the marginal consumption increase $\beta ,$ since these are the most likely values to occur. In particular we want to explore Region C, where the marginal pro<sup>fi</sup>t may become negative, and locate the maximum free traf<sup>fi</sup>c the provider can offer to maintain a positive marginal pro<sup>fi</sup>t. We have then to determine the boundary of Region C. Since the minimum marginal pro<sup>fi</sup>t is a growing function of $\lvert \beta ,$ by decreasing β we lower the minimum marginal pro<sup>fi</sup>t, and the boundary between Regions B and C is represented by the value of β for which the minimum marginal pro<sup>fi</sup>t is null (Region C including all the $\beta$ values below that threshold). By inserting the minimum condition (Eq. (19)) in the marginal pro<sup>fi</sup>t expression (17), and zeroing the marginal pro<sup>fi</sup>t, we get the following equation whose solution provides us with the maximum value of $\dot { \boldsymbol { \beta } }$ for which we can still have negative pro<sup>fi</sup>ts:

$$
\beta e ^ {1 / \beta} = \frac {e}{\alpha}.\tag{20}
$$

This value of $\beta ,$ marking the boundary between Regions B and C is reported in Fig. 5 as a function of the α ratio between costs and potential revenues.

If we are operating in this stable region, which is the only one we consider of our interest in the following, we can derive the maximum free traf<sup>fi</sup>c, with the constraint that the marginal pro<sup>fi</sup>t is positive, by equating expr. (17) to zero. We obtain the trascendental equation

$$
1 + \beta \frac {b _ {\max}}{\mu_ {0}} = \alpha \exp \left(\frac {b _ {\max} / \mu_ {0}}{1 + \beta b _ {\max} / \mu_ {0}}\right),\tag{21}
$$

![](/api/attachments/BWY25493/fulltext/images/690381e3a524b4f88bee86491293ee2c9a241add4b04a7767455920dc42cf244.jpg)  
Fig. 4. Minimal-pro<sup>fi</sup>t free traf<sup>fi</sup>c under the exponential distribution.

![](/api/attachments/BWY25493/fulltext/images/a61572e81821b062d41b18dae8ea6e429f35306633fb870908abe51c2d2cadaf.jpg)  
Fig. 5. Maximum marginal consumption increase under the exponential distribution

whose solution is reported in Fig. 6. As expected, when costs erode a large portion of the potential revenues $( \mathrm { e . g . , } \alpha \mathrm { = } 0 . 9 )$ , there is little room for generous offers of free traf<sup>fi</sup>c (typically no more than 15% of the average consumption in the no-IC case). Instead, when the provider has large margins on revenues $( \mathrm { e . g . } , \alpha { = } 0 . 6 )$ , the free traf<sup>fi</sup>c that can be offered may even reach the average consumption $\mu _ { 0 } .$

We now consider the IC case when the user's consumption follows a Rayleigh distribution. For the Rayleigh case the expression (6) of the expected marginal pro<sup>fi</sup>t becomes

$$
\mu_ {R} = (c - d) \left\{\frac {2}{\alpha} \left(1 + \beta \frac {b}{\mu_ {0}}\right) \left[ 1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) \right] - 1 \right\}.\tag{22}
$$

The marginal pro<sup>fi</sup>t has the same behaviour as that depicted in Fig. 3 for the exponential case, and we can likewise identify the three Regions A, B, and C (just the last of which is actually of interest to us).

The maximum free traf<sup>fi</sup>c that can be offered in the Rayleigh case so that the pro<sup>fi</sup>t is still positive can be obtained numerically and is shown in Fig. 7. Though the trend is the same as that observed for the exponential case (compared with Fig. 6), we note that the admissible free traf<sup>fi</sup>c levels are slightly lower.

## 5. Estimation of acceptance probability

In addition to modelling the traf<sup>fi</sup>c demand by the customer, we must also consider its behaviour in response to the sequence of offers put forward by the provider. In the interaction scheme we have sketched in Section $^ { 2 , }$ the customer can reply to the provider's offer with the simple accept/reject decision. Hence, its behaviour can be summed up by the probability that it accepts the offer. In this section we propose a model for such probability.

![](/api/attachments/BWY25493/fulltext/images/7d8e4443e3e7d65dc37c921445541da679cb471e0d8e73791795b82ad2d0b93e.jpg)  
Fig. 6. Maximum free traf<sup>fi</sup>c under the exponential distribution.

![](/api/attachments/BWY25493/fulltext/images/ec6f41549f788b8f54ba8868ef182cf4b312169ee47197a2ca12784c8c8764ed.jpg)  
Fig. 7. Maximum free traf<sup>fi</sup>c under the Rayleigh distribution.

At the k-th offer we describe the event that the customer accepts by the indicator variable $Y _ { k } ,$ which takes the value 1 if the customer accepts and the value 0 otherwise. The acceptance probability $\mathbb { P } [ Y _ { k } = 1 ]$ is expected to be a growing function of the free traf<sup>fi</sup>c level b, since the larger the amount of free traf<sup>fi</sup>c the lower the overall expense for the customer. We can also expect that the relative value of b with respect to the mean traf<sup>fi</sup>c μ is of interest, rather than the absolute value of b. On this basis we assume that the probability that the customer accepts the k-th offer after having rejected the k-1-th one is

$$
\mathbb {P} \left[ Y _ {k} = 1 \right] = 1 - \exp \left(- \lambda b / \mu_ {X}\right),\tag{23}
$$

where λ is a parameter taking larger values when the customer is readier to accept the offer. The use of the exponential function is an established approach to model the relationship between the retention rate and the expense incurred in the retention effort [2]. Since our probability of acceptance is equivalent to the retention rate (the customer is retained if it accepts the offer) and the free traf<sup>fi</sup>c value may be considered a proxy for the retention expense (if the provider increases the free traf<sup>fi</sup>c volume it incurs a pro<sup>fi</sup>t loss), the exponential model is a valid model for the acceptance probability as well.

The correct value for λ can be estimated by examining the customers' responses to offers put forward so far. In fact, for any value b<sup>ˆ</sup> we can estimate the acceptance probability $\mathbb { P } \big [ Y _ { k } = 1 | b = \hat { b } \big ]$ by <sup>j</sup>computing the proportion of customers (within any given customer class) who have accepted the offer at b = b<sup>ˆ</sup> . If we perform such estimation for a number of instances of the free traf<sup>fi</sup>c level, we end up with a number of couples $( b , \mathbb { P } [ Y _ { k } = 1 ] )$ , which can be used to derive a best-<sup>fi</sup>t estimate of λ using the regression curve (Eq. (23)).

However, though an estimate of λ is obtained for any given customer class, we may take into account the behaviour of the individual customer by adaptively updating its value after the customer's response. It is reasonable to assume that the longer the streak of negative responses by the customer to the provider's offers, the harder the customer is to be retained. We can capture this issue by adopting a simple exponential smoothing scheme to forecast the correct value of λ to use in the next offer round [7]. In the general form of this scheme the value to use for λ after the k-th rejection is

$$
\lambda_ {k} = \gamma \lambda_ {k - 1} + (1 - \gamma) \lambda^ {*},\tag{24}
$$

where γ is the smoothing parameter in the (0,1) range and $\lambda ^ { * }$ is the value corresponding to rejection: the larger the smoothing parameter the softer the updating. A typical value is $\gamma = 0 . 8 . \ \mathsf { A s \ t o \ } \lambda ^ { * }$ , we can assume ${ \boldsymbol { \lambda } } ^ { * } = 0 ;$ in fact, inserting this value in Eq. (23) provides a null acceptance probability. Under this assumption the updating equation becomes

$$
\lambda_ {k} = \gamma^ {k} \lambda_ {0},\tag{25}
$$

where the initial value $\lambda _ { 0 }$ is obtained from the above described estimation procedure for the whole class.

Eventually, the combination of exprs. (23) and (25) provides the following adaptive estimate of the acceptance probability that can be exploited by the provider to formulate its next offer so to optimize its expected pro<sup>fi</sup>t

$$
\mathbb {P} [ Y _ {k} = 1 ] = 1 - \exp \left(- \gamma^ {k} \lambda_ {0} b / \mu_ {X}\right).\tag{26}
$$

## 6. Optimization of pro<sup>fi</sup>ts

The provider's problem is to set the optimal amount of free traf<sup>fi</sup>c it is going to offer to the customer. Here the optimal choice is the one maximizing the expected marginal pro<sup>fi</sup>t of the provider. The provider is then led to optimize its trade-off between potential pro<sup>fi</sup>t and acceptance probability: the lower is the free traf<sup>fi</sup>c offer the larger are the revenues but the smaller is the probability that the customer is going to accept. In order to compute the expected marginal pro<sup>fi</sup>t at the k-th stage of the sequence of offers, we have to perform a double expectance extraction, both with respect to the decision of the customer to accept and to the random traf<sup>fi</sup>c value that the customer will develop:

$$
\mu_ {R, k} = \mathbb {P} [ Y _ {k} = 1 ] \mu_ {R}.\tag{27}
$$

The optimal value of free traf<sup>fi</sup>c is then

$$
b _ {k} = b: \frac {\partial \mu_ {R , k}}{\partial b} = 0.\tag{28}
$$

Pro<sup>fi</sup>t expectations change as the sequence of offers progresses: after each rejection by the customer the expected acceptance probability is revised downward through the application of the exponential smoothing algorithm and the use of expr. (26). As a consequence, a new, larger amount of free traf<sup>fi</sup>c has to be offered to induce the customer into accepting the provider's proposal; its value is obtained by solving the resulting Eq. (28). In the following subsections we examine the solutions obtained for the two traf<sup>fi</sup>c scenarios of interest, i.e., the exponential and the Rayleigh probability distributions.

## 6.1. Exponential case

In this section we derive the optimization equation for the case where the traf<sup>fi</sup>c developed in a period is represented by an exponential distribution. We also prove that the solution to this equation (providing us with the optimal free traf<sup>fi</sup>c volume) exists and is unique, and further that the optimal sequence of offers so obtained is indeed a growing sequence.

We <sup>fi</sup>rst consider the case where the traf<sup>fi</sup>c consumption is independent of the free traf<sup>fi</sup>c level, i.e., β=0 in expr. (4). When the traf<sup>fi</sup>c distribution follows an exponential distribution we can replace, in the general expression of the marginal pro<sup>fi</sup>t (Eq. (27)), the expressions obtained for the acceptance probability (Eq. (26)) and for the marginal pro<sup>fi</sup>t under acceptance (Eq. (7)). The resulting expected marginal pro<sup>fi</sup>t is

$$
\mu_ {R, k} = \left[ 1 - \exp \left(- \frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {0}}\right) \right] \cdot \left[ d - c + p \cdot \mu_ {0} \exp \left(- \frac {b}{\mu_ {0}}\right) \right].\tag{29}
$$

By imposing the maximization condition (Eq. (28)) we end with a trascendental equation whose solution is the optimal free amount of traf<sup>fi</sup>c at the k-th offer

$$
W _ {k} (b _ {k}) = \gamma^ {k} \lambda_ {0} \left[ p + \frac {d - c}{\mu_ {0}} \exp (b _ {k} / \mu_ {0}) \right] - p \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0} b _ {k}}{\mu_ {0}}\right) - 1 \right] = 0.\tag{30}
$$

Though the solution has to be looked for numerically, the following theorem holds

Theorem 1. There always exists a value $b _ { k }$ in the range $0 < b < b _ { \mathrm { m a x } }$ such that $W _ { k } ( b _ { k } ) = 0$ . Moreover this value is unique.

Proof. We note that $W _ { k } ( \cdot )$ is a continuous function and gets oppositesign values at the extremes of the interval $( 0 ; b _ { \mathrm { m a x } } )$ . In fact

$$
\begin{array}{l} W _ {k} (0) = \gamma^ {k} \lambda_ {0} \left[ p + \frac {d - c}{\mu_ {0}} \right] > 0 \quad \text { due   to   condition(16), } \\ W _ {k} (b _ {\max}) = - p \left[ \exp \left(\frac {p \cdot \mu_ {0}}{c - d}\right) ^ {\gamma^ {k} \lambda_ {0}} - 1 \right] <   0. \end{array}\tag{31}
$$

Hence, by the intermediate value theorem we are sure of the existence of a solution to Eq. (30). In addition this solution is unique since the function $W _ { k } ( b )$ is monotone (its derivative is a strictly negative function) and hence, by the inverse function theorem, it is invertible so that there's a unique value $b _ { k }$ for which $W _ { k } ( b _ { k } ) = 0$ . □

We now turn to the nature of the sequence of values $\{ b _ { 1 } , b _ { 2 } , \ldots \}$ } we obtain by the repeated solution of the optimization equation. It is natural to expect that each offer is better for the user than the previous one, i.e., $b _ { k + 1 } > b _ { k } ,$ for $k \geq 1 { : }$ if the user were proposed an offer with a free traf<sup>fi</sup>c volume lower than the one it has just refused, the new offer would not make any sense.

Theorem 2. The sequence $\{ b _ { k } \}$ is an increasing function of k.

Proof. We may rewrite the optimization Eq. (30) in the following way

$$
A (b _ {k}) = B (k, b _ {k}),\tag{32}
$$

after de<sup>fi</sup>ning

$$
A (b) = 1 - \frac {c - d}{p \cdot \mu_ {0}} \exp \left(\frac {b}{\mu_ {0}}\right) \quad B (k, b) = \frac {1}{\gamma^ {k} \lambda_ {0}} \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {0}}\right) - 1 \right].\tag{33}
$$

Since A(b) is a monotone decreasing function of b and B(k,b) is instead a monotone increasing function of b, we have $b _ { k + 1 } > b _ { k }$ if $B ( k + 1 , b ) { < } B ( k , b )$ . We then have to prove that

$$
\frac {B (k + 1 , b)}{B (k , b)} = \frac {1}{\gamma} \cdot \frac {\exp \left(\frac {\gamma^ {k + 1} \lambda_ {0} b}{\mu_ {0}}\right) - 1}{\exp \left(\frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {0}}\right) - 1} <   1.\tag{34}
$$

Indeed, if we introduce the Taylor expansion for the exponential function, the ratio becomes

$$
\frac {B (k + 1 , b)}{B (k , b)} = \frac {1}{\gamma} \cdot \frac {\sum_ {j = 1} ^ {\infty} \left(\gamma^ {k + 1} \lambda_ {0} b / \mu_ {0}\right) ^ {j}}{\sum_ {j = 1} ^ {\infty} \left(\gamma^ {k} \lambda_ {0} b / \mu_ {0}\right) ^ {j}} = \frac {\sum_ {j = 1} ^ {\infty} (\lambda_ {0} b / \mu_ {0}) ^ {j} \gamma^ {j (k + 1)}}{\sum_ {j = 1} ^ {\infty} (\lambda_ {0} b / \mu_ {0}) ^ {j} \gamma^ {j k + 1}}.\tag{35}
$$

Since γb1 we have $\gamma ^ { j ( k + 1 ) } { < } \gamma ^ { ( j k + 1 ) }$ and the denominator of the ratio is term by term larger than the numerator, hence $B ( k + 1 , b ) { < } B ( k , b )$ and the theorem is proved. □

We now turn to the general case of traf<sup>fi</sup>c consumption dependent on the free traf<sup>fi</sup>c level. Here we have to replace, in the general expression of the marginal pro<sup>fi</sup>t (Eq. (27)), the same expression as before for the acceptance probability (Eq. (26)), but expr. (17) for the marginal pro<sup>fi</sup>t under acceptance in the incentivized consumption case. The resulting expected marginal pro<sup>fi</sup>t at the k-th stage is

$$
\mu_ {R, k} = (c - d) \left[ 1 - \exp \left(- \frac {\gamma^ {k} \lambda_ {0} b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) \right] \left[ \frac {1 + \beta b / \mu_ {0}}{\alpha} \exp \left(- \frac {b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) - 1 \right].\tag{36}
$$

Its maximization can be obtained numerically since the equation we get by zeroing its derivative is again trascendental (we introduce the normalized free traf<sup>fi</sup>c $z = b / \mu _ { 0 } ,$ , and the optimal normalized free traf<sup>fi</sup>c $z _ { k } = b _ { k } / \mu _ { 0 } )$ :

$$
W _ {k} \left(z _ {k}\right) = \gamma^ {k} \lambda_ {0} \left[ \frac {1}{\alpha} - \frac {\exp \left(- \frac {z _ {k}}{1 + \beta z _ {k}}\right)}{1 + \beta z _ {k}} \right] + \frac {1}{\alpha} \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0}}{1 + \beta z _ {k}}\right) - 1 \right] \left[ \beta - \frac {1}{1 + \beta z _ {k}} \right] = 0.\tag{37}
$$

We can likewise prove that the following theorem holds

Theorem 3. There always exists a value $b _ { k }$ in the range 0bbb∞ such that $W _ { k } ( b _ { k } ) = 0 .$ . Moreover this value is unique.

Proof. In fact, we note that $W _ { k } ( \cdot )$ is a monotone increasing function (as can be readily seen from the inspection of its components, which are all monotone increasing functions), and assumes the oppositesign values

$$
\begin{array}{l} W _ {k} (0) = \gamma^ {k} \lambda_ {0} \left[ \frac {1}{\alpha} - 1 \right] <   0 \\ \lim _ {z \to \infty} W _ {k} (z) = \frac {\beta}{\alpha} \left[ \exp \left(\gamma^ {k} \lambda_ {0} / \beta\right) - 1 \right] > 0. \end{array}\tag{38}
$$

Hence by the intermediate value theorem the function $W _ { k } ( \cdot )$ has a single zero in the [0,∞) range. □

6.2. Rayleigh case

Similarly to what we have done for the exponential case, we consider <sup>fi</sup>rst the $\beta = 0$ case, and derive the solution equation by recalling exprs. (23) and (6). The expected marginal pro<sup>fi</sup>t is now

$$
\mu_ {R, k} = \left[ 1 - \exp \left(- \frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {0}}\right) \right] \cdot \left\{d - c + p \cdot \mu_ {X} \left[ 1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b}{\mu_ {0}}\right) \right] \right\}.\tag{39}
$$

By zeroing its derivative with respect to the free traf<sup>fi</sup>c, we obtain the equation

$$
\gamma^ {k} \lambda_ {0} \left\{\frac {d - c}{\mu_ {0}} + 2 p \left[ 1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b _ {k}}{\mu_ {0}}\right) \right] \right\} = p \sqrt {2 \pi} g \left(\sqrt {\frac {\pi}{2}} \frac {b _ {k}}{\mu_ {0}}\right) \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0} b _ {k}}{\mu_ {0}}\right) - 1 \right],\tag{40}
$$

which has to be solved (again numerically) to obtain the optimal amount of free traf<sup>fi</sup>c.

Also in this case we can however prove the existence and uniqueness of the solution. We can rewrite the optimization condition expressed by Eq. (40) as $Z _ { k } ( b _ { k } ) = 0 ,$ , by introducing the function

$$
Z _ {k} (b) = \frac {1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b}{\mu_ {0}}\right)}{g \left(\sqrt {\frac {\pi}{2}} \frac {b}{\mu_ {0}}\right)} - \frac {\sqrt {\pi / 2}}{\gamma^ {k} \lambda_ {0}} \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {0}}\right) - 1 \right] - \frac {c - d}{p \cdot \mu_ {0}} \frac {1}{2 g \left(\sqrt {\frac {\pi}{2}} \frac {b}{\mu_ {0}}\right)}.\tag{41}
$$

and then prove the following theorem

Theorem 4. There always exists a value $b _ { k }$ in the range $0 < b < b _ { \mathrm { m a x } }$ such that $Z _ { k } ( b _ { k } ) = 0$ . Moreover this value is unique.

Proof. We start by identifying three terms in the function $Z _ { k } ( b _ { k } )$ . The <sup>fi</sup>rst one is the well known Mill's ratio (or, equivalently, the inverse of the hazard function for the normal distribution), which is a decreasing function of its argument (and hence of the free traf<sup>fi</sup>c level b) [11]. We can likewise recognize that the second and the third terms, inclusive of their minus sign, are strictly negative decreasing functions of b for $b \in \mathbb { R } _ { + }$ . On the whole $Z _ { k } ( b )$ is then a decreasing function of b in the region of interest $0 < b < b _ { \mathrm { m a x } } .$ . In addition we can see that this function takes on opposite signs at the two extremes of that region. In fact we have

$$
Z _ {k} (0) = \sqrt {\frac {\pi}{2}} \left(1 - \frac {c - d}{p \cdot \mu_ {0}}\right) > 0 \Longleftrightarrow p \cdot \mu_ {0} > c - d,\tag{42}
$$

which is identical to the condition expressed by Eq. (16) for the possibility of offering some free traf<sup>fi</sup>c. At the other end of the region, recalling the upper bound (Eq. (11)), we have instead

$$
Z _ {k} (b _ {\max}) = - \frac {\sqrt {\pi / 2}}{\gamma^ {k} \lambda_ {0}} \left[ \exp \left(\frac {\gamma^ {k} \lambda_ {0} b _ {\max}}{\mu_ {0}}\right) - 1 \right] <   0.\tag{43}
$$

Since $Z _ { k } ( 0 ) { > } 0$ and $Z _ { k } ( b _ { \operatorname* { m a x } } ) < 0$ , by the intermediate value theorem we are sure that $Z _ { k } ( b ) = 0$ for some $b { : } 0 { < } b { < } b _ { \mathrm { m a x } }$

In addition, since the three terms composing $Z _ { k } ( b )$ are continuous monotone functions, $Z _ { k } ( b )$ is itself a continuous monotone function and, by the inverse function theorem, is invertible so that the value of $b : Z _ { k } ( b ) = 0$ is unique. □

By combining exprs. (22) and (26) in expr. (27), in the incentivized consumption case the expected marginal pro<sup>fi</sup>t is instead

$$
\mu_ {R, k} = (c - d) \left[ 1 - \exp \left(- \frac {\gamma^ {k} \lambda_ {0} b}{\mu_ {X}}\right) \right] \left\{\frac {2}{\alpha} \left(1 + \beta \frac {b}{\mu_ {0}}\right) \left[ 1 - G \left(\sqrt {\frac {\pi}{2}} \frac {b / \mu_ {0}}{1 + \beta b / \mu_ {0}}\right) \right] - 1 \right\},\tag{44}
$$

whose maximization, providing the optimal free traf<sup>fi</sup>c level, is again to be obtained numerically.

## 7. Optimal sequences of offers

In this section we provide some numerical results obtained by applying the optimization procedure described in the previous section. In order to present the results in a parametrized way, we group some of the quantities appearing as a whole both in the maximum free levels of exprs. (10) and (11), and in the expected marginal pro<sup>fi</sup>ts to be maximized, by resorting to de<sup>fi</sup>nition (12). In addition, the free traf<sup>fi</sup>c offer is always expressed as a percentage of the average traf<sup>fi</sup>c $\mu _ { 0 }$ when $\beta = 0$ (the no-IC case). We analyse two issues:

1) how the free traf<sup>fi</sup>c offer increases over time as the provider gets the successive refusals by the customer;

2) how the costs-to potential revenues ratio impacts on the <sup>fi</sup>rst offer.

We report the results obtained for the following <sup>fi</sup>xed values of the other parameters:

– initial exponential parameter $\lambda _ { 0 } = 1 , 2 , 4 ;$

– exponential smoothing parameter $\gamma = 0 . 8 .$

With this choice of values for the initial exponential parameter the free traf<sup>fi</sup>c level offered to get a 50% probability of acceptance has to be respectively 69%, 35%, and 17% of the average traf<sup>fi</sup>c. Larger values of $\lambda _ { 0 }$ correspond to a user readier to accept the provider's offer.

![](/api/attachments/BWY25493/fulltext/images/d939a5e720543c040051e2e0c6789d13f02563cd1fff9782c7da282e2970bad9.jpg)  
Fig. 8. Optimal free traf<sup>fi</sup>c volume in the exponential case.

Following the same subdivision used in the previous section, we deal <sup>fi</sup>rst with the exponential case

## 7.1. Exponential case

As in the previous sections, we <sup>fi</sup>rst consider the case of traf<sup>fi</sup>c consumption independent of the free traf<sup>fi</sup>c offered by the provider. When the traf<sup>fi</sup>c volume follows an exponential distribution the sequence of optimal free traf<sup>fi</sup>c values progresses as shown in Fig. 8, where $\alpha { = } 0 . 6 .$ The offers are more generous as $\lambda _ { 0 }$ lowers, correctly re<sup>fl</sup>ecting the expectation that easier-to-catch customers don't need generous offers. However, the actual offer update appears to be very limited in extension: over 5 iterations of the offer the free traf<sup>fi</sup>c offered increases by 12.1% when the initial exponential parameter is $\lambda _ { 0 } = 4 ,$ but just by 3.1% when $\lambda _ { 0 } = 1$

Though all the <sup>fi</sup>gures shown in Fig. 8 lie around 20%, the free traf<sup>fi</sup>c volume heavily depends on the weight of net costs, i.e., α. In order to explore this relationship we compute the value of the optimal initial offer as α varies. In Fig. 9 we see that the <sup>fi</sup>rst offer gets very low as the pro<sup>fi</sup>t margin shrinks (as embodied by larger values of the costs-to-potential revenues ratio). When the net costs erode 90% of the potential revenues, the optimal free traf<sup>fi</sup>c gets down to roughly 5% of the average traf<sup>fi</sup>c volume, a scanty discount on the customer's bill. Here the impact of the initial exponential parameter becomes progressively negligible as the relative weight of costs grows.

We now draw the sequence of optimal offers when $\beta { > } 0 ,$ , namely $\beta = 0 . 1$ and $\beta = 0 . 3$ , which are two values well within the admissible range identi<sup>fi</sup>ed in Section $^ { 4 , }$ and $\alpha { = } 0 . 6 .$ The resulting curves are shown in Fig. 10.

![](/api/attachments/BWY25493/fulltext/images/da0accd3b8f686857bd21133feaeb5c665123b236da399469f65d70b434d050b.jpg)  
Fig. 9. Impact of the costs-to-revenues ratio.

![](/api/attachments/BWY25493/fulltext/images/daf5f22f9526b7e09737e43b4dcddbc9c09515c0fdb06266eb6842e946bf26c6.jpg)  
Fig. 10. Optimal free traf<sup>fi</sup>c volume in the exponential case $( \beta > 0 ) .$

A quick comparison with Fig. 8 reveals that the optimal free traf<sup>fi</sup>c is quite higher than when the customer's consumption is insensitive to the provider's offer. The escalation is faster for larger values of $\lambda _ { 0 }$ and of β.

## 7.2. Rayleigh case

We now consider the same scenarios for the Rayleigh case.

The curves pertaining to the no-IC case are shown in Figs. 11 and 12. $\mathsf { A } s$ the acceptance probability parameter varies, we observe a trend similar to the exponential case, though the free traf<sup>fi</sup>c levels are now slightly lower. The initial free traf<sup>fi</sup>c offer also exhibits the same dependence on the costs-to-potential revenues ratio, terminating at 5% when α=0.9. When βN0 (see Fig. 13), we observe again an increase in the optimal free traf<sup>fi</sup>c levels. However, the sequence of offers doesn't progress signi<sup>fi</sup>cantly when we have low values of the acceptance probability parameter $\lambda _ { 0 }$ and low values of the marginal consumption increase β at the same time.

## 8. Joint optimization of unit price and free traf<sup>fi</sup>c

In this section we consider the case when the unit price p and the free traf<sup>fi</sup>c b are updated simultaneously, at each new round of the sequence of offers. For this strategy we revise the expression of the marginal pro<sup>fi</sup>t and provide some sample results.

The results obtained so far have been derived under speci<sup>fi</sup>c assumptions on the consumer's behaviour: its average consumed traf<sup>fi</sup>c $\mu _ { X } ,$ as per expr. (4), and the probability that the customer will accept the new offer, as per expr. (23). In both cases those assumptions have been formulated for the strategy employing a single optimization variable, namely the free traf<sup>fi</sup>c amount. They need to be reformulated when the provider may change both the free traf<sup>fi</sup>c amount and the unit price at each round.

![](/api/attachments/BWY25493/fulltext/images/bb1f8c2a0b071172e7118b0e257b1c3d8a3ec61786a0ce046b864671d962a84a.jpg)  
Fig. 11. Optimal free traf<sup>fi</sup>c volume in the Rayleigh case

![](/api/attachments/BWY25493/fulltext/images/41d5b2f77f68ab5f72add7b87ad87c9ebe0850b1918282e8e507b26574a4e8b2.jpg)  
Fig. 12. Impact of the costs-to-revenues ratio in the Rayleigh case.

Let's consider <sup>fi</sup>rst the former quantity. According to expr. (4), the customer consumes more traf<sup>fi</sup>c as the free traf<sup>fi</sup>c grows. We can expect that the unit price has an opposite in<sup>fl</sup>uence: the higher the unit price the lower the traf<sup>fi</sup>c consumed by the customer. We can therefore explicit the in<sup>fl</sup>uence of the unit price in expr. (4) by introducing an inverse dependence on $p .$ We adopt the general expression

$$
\mu_ {X} = \mu_ {0} + \beta b p ^ {s},\tag{45}
$$

where sb0 is a parameter governing the intensity of the in<sup>fl</sup>uence of the unit price.

If we turn to the probability of accepting the offer, the dependence on the free traf<sup>fi</sup>c is embodied by expr. (23): the customer will be more likely to accept the new offer the larger the free traf<sup>fi</sup>c. In the strategy relying on the free traf<sup>fi</sup>c as the only leverage, the unit price did not change throughout the sequence of offers, and its effect was therefore accounted for in the λ parameter of expr. (23). However, when the new offer differs from the previous one for the unit price as well as for the amount of free traf<sup>fi</sup>c, we have to make that dependence explicit. We expect that the probability of acceptance will get lower as the unit price grows. We can include that inverse dependence in expr. (26) by modifying it as follows:

![](/api/attachments/BWY25493/fulltext/images/0b5d407417a6f9c49c6c39e661c7d59558074507ba02bf8dacc47b87966da358.jpg)  
Fig. 13. Optimal free traf<sup>fi</sup>c volume in the Rayleigh case (βN0).

![](/api/attachments/BWY25493/fulltext/images/c8991a66bf6bbfdbe0a29792fbb31cef235ac784cf188aeee56892a2be679849.jpg)  
Fig. 14. Optimal combination of unit price and free traf<sup>fi</sup>c volume in the exponential case.

$$
\mathbb {P} \left[ Y _ {k} = 1 \right] = 1 - \exp \left(- \gamma^ {k} \lambda_ {0} b / \left(p ^ {t} \mu_ {X}\right)\right)\tag{46}
$$

where tN0 is a parameter governing the intensity of the in<sup>fl</sup>uence of the unit price on the probability of acceptance.

When we introduce the modi<sup>fi</sup>ed expressions (45) and (46), respectively for the average traf<sup>fi</sup>c and the acceptance probability, the expected marginal pro<sup>fi</sup>t for the exponential distribution case becomes

$$
\mu_ {R, k} = \mu_ {0} \left[ 1 - \exp \left(- \gamma^ {k} \lambda_ {0} \frac {z}{p ^ {t} \delta}\right) \right] \left[ - \alpha p + p \delta \exp \left(- \frac {z}{\delta}\right) \right],\tag{47}
$$

where we use the positions $z = b / \mu _ { 0 }$ for the normalized free traf<sup>fi</sup>c and $\begin{array} { r } { \delta = 1 + \beta p ^ { s } b / \mu _ { 0 } , } \end{array}$ for the sake of readability. For the Rayleigh case we have instead

$$
\mu_ {R, k} = \mu_ {0} \left[ 1 - \exp \left(- \gamma^ {k} \lambda_ {0} \frac {z}{p ^ {t} \delta}\right) \right] \left[ - \alpha p + 2 p \delta \left(1 - G \left(\sqrt {\frac {\pi}{2}} \frac {z}{\delta}\right)\right) \right].\tag{48}
$$

We report hereafter two sample optimal sequences of combinations of values for the normalized free traf<sup>fi</sup>c and the unit price, when $s = - 0 . 5$ and t=1 (i.e., we consider the probability of acceptance more sensitive to the unit price than the average traf<sup>fi</sup>c is). The values adopted for the other parameters are in line with what has been chosen for the cases reported in Section 7, namely $\beta = 0 . 3 , \gamma = 0 . 8 ,$ $\lambda _ { 0 } = 4 .$ . Given the trascendental nature of both exprs. (47) and (48), the optimization is carried out numerically. The results are reported in Figs. 14 and 15 respectively for the exponential and the Rayleigh cases. The offer is made more and more convenient for the customer in both optimization variables, i.e., the unit price gets lower and lower, and the free traf<sup>fi</sup>c keeps increasing, but the degree of change is quite different for the two variables. In fact, the unit price is signi<sup>fi</sup>cantly lowered with each offer updating: the overall variation over the <sup>fi</sup>rst <sup>fi</sup>ve rounds is roughly −28% for the exponential case (where at the fourth round the maximum sustainable free traf<sup>fi</sup>c and the minimum sustainable unit price are reached) and −21% for the Rayleigh case. Instead, the overall variation of the free traf<sup>fi</sup>c is quite negligible (roughly 1%). However, the initial free traf<sup>fi</sup>c offer is quite large. It appears that, when price is used as leverage in addition to the free traf<sup>fi</sup>c, the sequence of offers starts with a very large free traf<sup>fi</sup>c amount but proceeds with signi<sup>fi</sup>cant lowerings of the unit price.

![](/api/attachments/BWY25493/fulltext/images/841e6a26a3070b8572e8d17b47ed436cd6aa66becfdda1e656b1d761d3750199.jpg)  
Fig. 15. Optimal combination of unit price and free traf<sup>fi</sup>c volume in the Rayleigh case.

## 9. Conclusions

We have derived the optimal strategy for a losing provider to win back churning customers by acting on the tarif<sup>fi</sup>ng plan. The strategy has been derived for a tarif<sup>fi</sup>ng scheme where the service provider increases, at each offer round, the free traf<sup>fi</sup>c amount in response to the rejection of the previous offer by the customer. In Section 8 we brie<sup>fl</sup>y address the case where both the free traf<sup>fi</sup>c amount and the unit price are updated in response to a customer turndown. The interaction between the customer and the service provider is therefore a back-and-forth sequence of offers by the service providers and acceptance/rejection decisions by the customer. The strategy is optimal in the sense that it maximizes the expected revenues for the service provider. For the strategy relying on the free traf<sup>fi</sup>c amount only we have provided two results: a) upper bounds on offers; b) sequences of optimal offers. We have <sup>fi</sup>rst derived upper bounds for the free traf<sup>fi</sup>c level compatible with net positive pro<sup>fi</sup>ts. These upper bounds are to be used to mark the stop condition on the offer rede<sup>fi</sup>nition. Such upper bounds depend both on the pro<sup>fi</sup>t margins and on the marginal consumption increase (i.e., the consumption increase spurred by the increase in the free traf<sup>fi</sup>c offered within the pricing package). The upper bounds grow when the pro<sup>fi</sup>t margins are larger and when the marginal consumption increase is larger. Within the range dictated by such upper bound we have instead derived the optimal free traf<sup>fi</sup>c levels to be offered to the churning customer. These free traffic levels grow again with the marginal consumption increase. They are also larger when the customer's demand follows an exponential distribution rather than a Rayleigh one. Typical ranges for the free traf<sup>fi</sup>c levels are 20–30% of the average traf<sup>fi</sup>c consumption. In the strategy based on updating both the unit price and the free traffio amount, the sequence of offers starts with a very large free traf<sup>fi</sup>c amount but proceeds with signi<sup>fi</sup>cant lowerings of the unit price. The de<sup>fi</sup>nition of the optimal sequence of offers can be done of<sup>fl</sup>ine and applied as the interaction with the customer progresses and allows the service provider to take into account both the overall statistical behaviour of a class of customers and the behaviour of the individual customer, applying a differentiated pricing strategy.

## References

[1] Autorité de Régulation dés Communications électroniques et des Postes, Annual Report 2005, 2005.

[2] R. Blattberg, J. Deighton, Manage marketing by the customer equity test, Harvard Business Review (July–August 1996) 136–144.

[3] G. Davies, M. Hardt, F. Kelly, Come the revolution — network dimensioning, service costing and pricing in a packet switched environment, Telecommunications Policy 28 (2004) 391–412.

[4] M. Falkner, M. Devetsikiotis, I. Lambadaris, An overview of pricing concepts forbroadband IP networks, IEEE Communications Surveys (2000) 2–13 Second Quarter 2000.

[5] Y. Guan, W. Yang, H. Owen, D.M. Blough, A pricing approach for bandwidth allocation in differentiated service networks, Computers & Operations Research 35 (12) (December 2008) 3769–3786

[6] J. Hadden, A. Tiwari, R. Roy, D. Ruta, Computer assisted customer churn management: state-of-the-art and future trends, Computers & Operations Research 34 (10) (October 2007) 2902–2917.

[7] F.S. Hillier, G.J. Liebermann, Introduction to Operations Research, McGraw-Hill, New York, 2001.

[8] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[9] Ofcom. International benchmarking study of mobile services and dial-up PSTN Internet access, December 2000.

[10] E. Osiowy, P. Collins, Mobile telephony in Australia: measuring price change, Communications Research Forum, Canberra, October 2000, pp. 4–5.

[11] J.K. Patel, C.B. Read, Handbook of the Normal Distribution, Marcel Dekker, New York and Basel, 1982.

[12] P.C. Verhoef, B. Donkers, Predicting customer potential value an application in the insurance industry, Decision Support Systems 32 (2) (2001) 189–199.

[13] J.J. Wheatley, World Telecommunications Economics, IEE, London, 1999.

[14] K. Wieland, The customer retention challenge, Telecommunications 40 (10) (October 2006) 14–17.

Maurizio Naldi graduated cum laude in 1988 in Electronic Engineering at the University of Palermo and then received his Ph.D. in Telecommunications Engineering from the University of Rome “Tor Vergata”. After graduation he pursued an industrial career, <sup>fi</sup>rst at Selenia as a radar designer (1989–1991), and then in the Network Planning Departments of Italcable (1991–1994), Telecom Italia (1995–1998), and WIND (1998–2000) where he was appointed Head, Traf<sup>fi</sup>c Forecasting & Network Cost Evaluation Group. In the 1992–2000 period he was active in the standardization bodies (ETSI and ITU), in particular as Associate Rapporteur for Broadband Traf<sup>fi</sup>c Measurements and Models at ITU Study Group 2. Since 2000 he is with the University of Rome at Tor Vergata, where he is now an Aggregate Professor.

Andrea Paci<sup>fi</sup>ci is an Assistant Professor in operations research at the Engineering Faculty of the University of Rome Tor Vergata. He received a bachelor's degree in Information Engineering and a PhD in operations research both at the University of Rome ‘La Sapienza’. His research is mainly concerned with algorithms design and computational complexity characterisation for combinatorial optimisation problems with applications to scheduling, logistics, manufacturing, telecom and multi-agent systems.
