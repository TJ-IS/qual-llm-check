---
otero_id: 20909
otero_key: "KH243HEM"
title: "Integrating real and financial options in demand-side electricity contracts"
authors: "Shmuel S. Oren"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00105-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating real and financial options in demand-side electricity contracts

Shmuel S. Oren<sup>)</sup>

Department of Industrial Engineering and Operations Research, UniÕersity of California at Berkeley, Berkeley, CA 94720, USA

## Abstract

In a competitive electricity market traditional demand-side management DSM options offering customers curtailableŽ . service at reduced rates are replaced by voluntary customer responses to electricity spot prices. In this new environment, customers wishing to ensure a fixed electricity price while taking advantage of their flexibility to curtail loads can do so by purchasing a forward electricity contract bundled with a financial option that provides a hedge against price risk and reflects the Areal optionsB available to the customer. This paper describes a particular financial instrument referred to as a Adouble-callB option and derives the value of that option under the assumption that forward electricity prices behave as a geometric Brownian motion process. It is shown that a forward contract bundled with an appropriate double-call option provides a APerfect hedgeB for customers, which can curtail loads in response to high spot prices and can mitigate their curtailment losses when the curtailment decision is made with sufficient lead time. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Electric power; Interruptible service; Early curtailment notification; Call options; Real options

## 1. Introduction

Interruptible<sup>r</sup>curtailable service contracts at reduced rates have been introduced by many electric utilities in the 1980s as part of numerous demand-side management programs DSM aimed at reducing theŽ . cost of electricity by taking advantage of customers flexibility to manage their load. These programs were designed to incent customers to reduce their load during shortages or system peaks as an alternative to costly spinning reserves and expansion of the generation capacity that would have been needed to serve the growing demand for electricity. Most interruptible service contracts offered alternative warning times. Tariff T-3 of Southern California Edison and Tariff E-20 of PG&E, for instance, offer higher discounts for shorter notification of an impending curtailment. A shorter warning requirement enables the utility to substitute interruptible load for spinning reserves and reduces its unit commitment cost. Consequently, a shorter warning time entitles the customer to a lower rate. From the customers’ point of view, earlier notification of an impending curtailment may mitigate the shortage costs e.g., by clos- Ž ing operation . A similar situation may exist with . respect to long-term supply contracts. In countries that heavily depend on hydro, such as New Zealand, there have been initiatives to develop approaches for early long-term notification say several months ofŽ . projected shortages due to low hydro reserves. With proper price incentives such early notification could motivate an aluminum smelter, for instance, to plan a seasonal shutdown.

A methodology for the design of priority service price schedules with an early notification option was described by Strauss and Oren 7 as an extension to<sup>w</sup> <sup>x</sup> the seminal work on priority service by Chao and Wilson 1 . With the advent of deregulation of the<sup>w</sup> <sup>x</sup> electric power industry in the US and around the world, quantity controls, such as curtailments, are being replaced by price signals provided by daily and hourly spot markets for electricity that have been established as part of the industry restructuring. In such markets, a customer can benefit from its flexibility by responding to the price signal and exercise its Areal optionB to reduce consumption when the price is high. Such an approach requires the customer to actively participate in the spot market. Customers that prefer to avoid the risk of price fluctuation can AhedgeB the price risk and secure a fixed price through forward purchases of power or bilateral contracts for differences CFD . The CFDŽ . are contracts that entitle<sup>r</sup>obligate the parties to receive<sup>r</sup>pay the difference between the spot price and an agreed upon fixed price with the net effect that the parties experience a fixed price of electricity while trading power at the spot prices for a detailedŽ explanation of CFDs and their use in the UK, see ENRON 3 . Simple hedges that ensure a fixed price<sup>w</sup> <sup>x</sup>. do not account for a customer’s flexibility and willingness to curtail its load when the spot price is high due to shortages or high demand. In the presence of a spot market, customers willing to exercise their curtailment option can sell their acquired power at the spot prices. However, if a customer wants to secure a fixed rebate for willingness to exercise voluntary curtailment, he<sup>r</sup>she can do so by selling back a call option on the power secured by the forward contract. The equivalence between interruptible service contracts and forward contracts bundled with a call option has been first described by Gedra <sup>w x</sup> <sup>w x</sup> 4 and in Gedra and Varaiya 5 . They show that a rational customer whose valuation of a MW h is V will self-select to sell a call option with strike price V and will curtail its load whenever the option is exercised, i.e, when the spot price exceeds the strike price V. Furthermore, the actuarial value of the call option equals to the corresponding interruptible rate discount.

In this paper, we extend the above results to account for the effect of early notification and introduce a new type of financial instruments that allows a customer to secure the benefit of its real option to curtail load and to commit to such curtailment early or late if properly incented.

## 2. Hedging price uncertainty with early and late curtailment options

Suppose that a customer has a shortage loss $\$ 1$ per MW h if curtailed close to delivery time, but a lower shortage cost of $\$ 1$ per MW h if a shut down is planned at an early date T prior to the physical delivery date. He<sup>r</sup>she could purchase a forward electricity supply contract and sell back an exotic call option, which can be executed at delivery time at strike price $V _ { 0 }$ or at time T before delivery at strike price $V _ { \mathrm { T } }$ . The premium received by the customer for that call lowers his<sup>r</sup>her cost of doing business while the exercise of the option will nullify the forward contract, forcing the customer to face spot prices when theses prices exceed the strike prices of the option. In these circumstances, however, since the spot price of electricity exceeds the customer’s willingness to pay for it, the customer will choose to curtail its load. Such a AperfectB hedging instrument could reduce a customer’s transaction costs and enables customers to divest their unwanted risk.

Fig. 1 below illustrates a contractual arrangement that can provide a perfect hedge for a customer who can mitigate shortage cost through early notification. In this arrangement, the customer purchases a forward contract and sells back a Adouble-callB option that can be exercised either at an early date T prior to delivery or at delivery time at two different strike prices. The customer can select the two strike prices, while the holder of the option decides if and when to exercise the call. An early exercise cancels the forward at time T prior to delivery and pays the early strike price, while exercise at delivery time cancels the forward and pays the late strike price. If the call is not exercised, the forward is settled through physical delivery.

The efficacy of a financial instrument in achieving allocated efficiency depends on its ability to induce customer and supplier choices that are consistent with the decisions that would have been taken by a benevolent central planner with perfect information. Fig. 2 illustrates the decision tree for a central planner with perfect information about customers shortage costs and forward electricity contracts.

![](/api/attachments/KH243HEM/fulltext/images/db9921fa07b811a535f220b7f12af0def5ef615baaa4cc40adcfd87a596af3f5.jpg)  
Fig. 1. Contractual obligations, payments and choices in a forward contract bundled with a double-call option.

At time T, the planner knows the early and late shortage costs $V _ { 0 }$ and $V _ { \mathrm { T } }$ , the forward price $f _ { \mathrm { T } }$ and the probability distribution $P r \{ f _ { 0 } | f _ { \mathrm { T } } \}$ over the forward price at delivery same as spot . The immediateŽ . decision is whether to curtail at the early date or wait. Ignoring sunk costs, early curtailment yields the value of the forward at delivery less the early shortage cost. Foregoing early curtailment presents a second decision whether to curtail at delivery or deliver. Economic efficiency dictates curtailment at delivery if and only if the spot price exceeds the shortage cost. Hence, the net value net of sunk costsŽ or sure gains of the second decision is the expected. value of max 0,<sup>w</sup> $f _ { 0 } - V _ { 0 } ] ,$ , which is the value at time T prior to delivery of a simple call option with strike price $V _ { 0 } { \mathrm { : } }$ , given the forward price $f _ { \mathrm { T } } , \mathrm { i } . \mathrm { e } . , C _ { \mathrm { T } } ( V _ { 0 } | f _ { \mathrm { T } } )$

![](/api/attachments/KH243HEM/fulltext/images/38e216f2938f0cc15b72327a1811e2aad6cf6442940075fa04668f4deaaf091e.jpg)  
Fig. 2. Decision tree at early date for central planner with perfect information.

Subsequently, the optimal decision at time T prior to delivery is to curtail if $f _ { \mathrm { T } } > \overline { { k } } .$ , where $\bar { k } - V _ { \mathrm { T } } =$ $C _ { \mathrm { T } } ( V _ { 0 } | f _ { \mathrm { T } } = \overline { { k } } )$ . This result follows from an assumption that the forward price at any point in time equals the risk neutral expectation of the spot price at delivery this ignores interest and the spot and Ž . forward prices reflect a competitive market equilibrium. Thus, the threshold forward price for socially efficient early curtailment is the sum of the immediate shortage cost plus the value of the forgone late call option. If the forward price at time $T$ exceeds that threshold level, it is socially optimal to curtail service at that time. Fig. 3 illustrates the efficient rationing policy as a function of the foreword prices at the early and late dates and the combination of early and late shortage costs. Under optimal rationing, loads in the shaded area should be curtailed early, while those in the lined area should be curtailed at delivery time. As the early forward price increase, more load will be interrupted early in anticipation of a shortage reflected by these prices. Similarly, if the spot price at delivery is higher than more load with shortage cost below that price , it will be Ž . curtailed.

Let us now consider the exercise decision by the holder of a double-call option with strike price $k _ { \mathrm { T } }$ at time T and $k _ { 0 }$ at time of delivery. The decision tree for such a decision is identical to that shown in Fig. 2 with $V _ { \mathrm { T } }$ and $V _ { 0 }$ replaced by $k _ { \mathrm { T } }$ and $k _ { 0 } .$ . The corresponding optimal exercise decisions are, therefore, to exercise at delivery if $f _ { 0 } > k _ { 0 }$ and exercise at T prior to delivery if $f _ { \mathrm { T } } > \bar { k }$ , where $\bar { k } - k _ { \mathrm { T } } =$ $C _ { \mathrm { T } } ( k _ { 0 } | f _ { \mathrm { T } } = \overline { { k } } )$

The optimal exercise policy is illustrated in Fig. 4, showing the early and late exercise regions as a

![](/api/attachments/KH243HEM/fulltext/images/5093b01b05f1a20916c839e6b999b31d82b2e2a63a9e9974d30df5d2d54b7774.jpg)  
Fig. 3. Efficient rationing with perfect shortage cost information Ž for geometric Brownian motion with notification interÕal Õolatility $\sigma \sqrt { T } = 1 )$

function of the strike prices of the option and the forward prices at the early exercise date and at delivery. Note that while the spot price threshold level for late exercise of a double-call option equals the late strike price, the forward threshold value for early exercise depends on both strike prices and will always exceed the value of the early strike price thisŽ accounts for the value of the remaining option if the option is not exercised early ..

![](/api/attachments/KH243HEM/fulltext/images/e5e6960bf4fc02b54811756a21277f4cea967ccbc5846b544426f37574e71a5c.jpg)  
Late Strike Price (k)  
Fig. 4. Optimal exercise policy for a double-call option Ž for geometric Brownian motion with notification interÕal Õolatility $\sigma \sqrt { T } = 1 )$

![](/api/attachments/KH243HEM/fulltext/images/fafc034aac0d7ab159cf8685a91ae571cab6b50700cf5647ad6611aad5f1b202.jpg)  
Fig. 5. Customer self-selection of strike prices for double-call option.

## 3. Self-selection of the strike prices for a doublecall option

It is evident from the above analysis that the optimal exercise of a double-call option with strike prices $k _ { \mathrm { T } } = V _ { \mathrm { T } }$ and $k _ { 0 } = V _ { 0 }$ produces the same outcome as socially efficient curtailment of a load with early and late shortage costs $V _ { \mathrm { T } }$ and $V _ { 0 } .$ . In a competitive environment, however, shortage costs are customers’ private information. Thus, to achieve efficient curtailment through the exercise of double-call options, it is necessary that customers will find it advantageous to select strike prices that equal their privately known shortage costs. Fig. 5 illustrates the decision tree for a hedging customer with shortage costs $V _ { \mathrm { T } }$ and $V _ { 0 }$ having to select strike prices for a double-call option. The customer takes into consideration the market valuation of such options and the optimal exercise strategy. A speculator who can only sell the forward contract at the prevailing market prices but has no private value for the commodity will face the same decision tree as a hedger with the exception that $V _ { \mathrm { T } }$ and $V _ { 0 }$ are replaced with the foreword prices $f _ { \mathrm { T } }$ and $f _ { 0 }$ , respectively. Market efficiency, which precludes arbitrage gains, dictates that the expected gains of a speculator are zero for any selection of strike prices. This condition and the optimal exercise policy determine the value $\hat { C } _ { \mathrm { t } } ( k _ { \mathrm { T } }$ $k _ { 0 } | f _ { \mathrm { t } } )$ of the double-call option.

In the following analysis, we use the no-arbitrage condition and the optimal exercise policy to prove that indeed it is optimal maximizes expected gainŽ . for a hedging customer to select strike prices that equal the corresponding curtailment costs and, hence, the optimal exercise of the call option will result in efficient curtailment.

The decision tree in Fig. 5 illustrates the strikeprice-selection decision faced by a hedger with early and late interruption losses of $V _ { \mathrm { T } }$ and $V _ { 0 } .$ . The expected hedging gains are, thus, given by:

$$
\begin{array}{l} B _ {t} \big (k _ {T}, k _ {0}; V _ {T}, V _ {0} | f _ {t} \big) = (  k _ {T} - V _ {T}) \mathrm{Pr} \big \{f _ {T} > \overline {{k}} | f _ {t} \big \} \\ \qquad + (  k _ {0} - V _ {0}) \mathrm{Pr} \big \{f _ {T} \leq \overline {{k}} | f _ {t} \big \} \\ \qquad \times \mathrm{Pr} \big \{f _ {0} > k _ {0} | f _ {t}, f _ {T} \leq \overline {{k}} \big \} \\ \qquad +   \hat {C} \big (  k _ {T}, k _ {0} | f _ {t} \big), \end{array}
$$

where $\bar { k }$ is defined in terms of the strike prices and the value of a simple call option by the equation: $\bar { k } - k _ { \mathrm { T } } - C _ { \mathrm { T } } ( k _ { 0 } | \bar { k } ) = 0$

The same tree will represent the decision of a speculator who has no private use for the commodity and, hence, values it at the respective spot prices $f _ { \mathrm { T } }$ and $f _ { 0 . }$ However, market efficiency no-arbitrageŽ gains dictates that the expected gains of the specula- . tor are zero for any strike prices, which implies:

$$
\begin{array}{l} 0 = \int_ {\bar {k}} ^ {\infty} (k _ {T} - f _ {T}) \mathrm{dPr} \{f _ {T} | f _ {t} \} \\ \quad + \int_ {0} ^ {\bar {k}} \left[ \int_ {k _ {0}} ^ {\infty} (k _ {0} - f _ {0}) \mathrm{dPr} \{f _ {0} | f _ {T} \} \right] \mathrm{dPr} \{f _ {T} | f _ {t} \} \\ \quad + \hat {C} (k _ {T}, k _ {0} | f _ {t}). \end{array}
$$

We can use the above equation to substitute for the value of the double call in the expression for hedging gains, resulting in:

$$
\begin{array}{l} B _ {t} \left(k _ {T}, k _ {0}; V _ {T}, V _ {0} \mid f _ {t}\right) \\ = \int_ {\bar {k}} ^ {\infty} \left(f _ {T} - V _ {T}\right) \mathrm{dPr} \left\{f _ {T} \mid f _ {t} \right\} \\ + \int_ {0} ^ {\bar {k}} \left[ \int_ {k _ {0}} ^ {\infty} \left(f _ {0} - V _ {0}\right) \mathrm{dPr} \left\{f _ {0} \mid f _ {T} \right\} \right] \mathrm{dPr} \left\{f _ {T} \mid f _ {t} \right\}. \end{array}
$$

The inner integral above can be expressed as:

$$
\begin{array}{l} \int_ {k _ {0}} ^ {\infty} (f _ {0} - V _ {0}) \mathrm{dPr} \bigl \{f _ {0} | f _ {T} \bigr \} \\ = C _ {T} \bigl (V _ {0} | f _ {T} \bigr) + \int_ {k _ {0}} ^ {V _ {0}} (f _ {0} - V _ {0}) \mathrm{dPr} \bigl \{f _ {0} | f _ {T} \bigr \}. \end{array}
$$

For the special case where the strike prices match the interruption losses, we have:

$$
\begin{array}{l} B _ {t} \big (V _ {T}, V _ {0}; V _ {T}, V _ {0} | f _ {t} \big) = \int_ {\hat {k}} ^ {\infty} \big (f _ {T} - V _ {T} \big) \mathrm{dPr} \big \{f _ {T} | f _ {t} \big \} \\ + \int_ {0} ^ {\hat {k}} C _ {T} \big (V _ {0} | f _ {T} \big) \mathrm{dPr} \big \{f _ {T} | f _ {t} \big \}, \end{array}
$$

where $\hat { k }$ is defined by the equation:

$$
\hat {k} - V _ {T} - C _ {T} \left(V _ {0} | \hat {k}\right) = 0.
$$

Using the above expressions, we can now rewrite the hedging gains as:

$$
\begin{array}{l} B _ {t} \left(k _ {T}, k _ {0}; V _ {T}, V _ {0} \mid f _ {t}\right) \\ = B _ {t} \left(V _ {T}, V _ {0}; V _ {T}, V _ {0} \mid f _ {t}\right) - \int_ {\bar {k}} ^ {\hat {k}} \left[ (\hat {k} - f _ {T}) \right. \\ \left. - \left(C _ {T} \left(V _ {0} \mid \hat {k}\right) - C _ {T} \left(V _ {0} \mid f _ {T}\right)\right) \right] d \operatorname * {P r} \left\{f _ {T} \mid f _ {t} \right\} \\ + \int_ {0} ^ {\bar {k}} \left[ \int_ {k _ {0}} ^ {V _ {0}} \left(f _ {0} - V _ {0}\right) d \operatorname * {P r} \left\{f _ {0} \mid f _ {T} \right\} \right] d \operatorname * {P r} \left\{f _ {T} \mid f _ {t} \right\} \end{array}
$$

By mean value theorem:

$$
\begin{array}{c} \big (\hat {k} - f _ {T} \big) - \big (C _ {T} \big (V _ {0} | \hat {k} \big) - C _ {T} \big (V _ {0} | f _ {T} \big) \big) \\ = \big (\hat {k} - f _ {T} \big) \left[ 1 - \frac {\partial C _ {T} \big (V _ {0} | f \big)}{\partial f} \right] \end{array}
$$

for some $f \in \left[ f _ { T } , \hat { k } \right]$

But the term in the square bracket is nonnegative since the slope of a simple call price with respect to the spot price is never greater than AoneB . Hence, for $\tilde { k } \geq \overline { k }$ , the integrand in the first integral of the hedging benefit equation above is nonnegative sinceŽ $\hat { k } - \bar { f } _ { \mathrm { T } } \geq 0 )$ . For $\widehat { k } < \overline { { k } }$ , the integrand is negative but the sign of the integral is still positive due to the switched integration limits. Similarly, the second integral is negative since either the integrand is negative or the integration limits of the inner integral are switched. It follows that:

$$
B _ {t} \big (k _ {T}, k _ {0}; V _ {T}, V _ {0} | f _ {t} \big) \leq B _ {t} \big (V _ {T}, V _ {0}; V _ {T}, V _ {0} | f _ {t} \big)
$$

so the hedger’s gains are maximized by selecting early and late strike prices that match the early and late interruption costs, respectively.

## 4. Pricing of double-call options

Based on the optimal exercise policy and the no-arbitrage condition described above, we determine the value of the double-call option at any time t, as follows:

$$
\begin{array}{l l} \hat {C} _ {t} (k _ {T}, k _ {0} | f _ {t}) \\ = \left\{ \begin{array}{l l} C _ {t} (k _ {0} | f _ {t}) & \text { for   } t <   T \\ \max [ f _ {T} - k _ {T}, C _ {T} (k _ {0} | f _ {T}) ] & \text { for   } t = T \\ E \{\max [ f _ {T} - k _ {T}, C _ {T} (k _ {0} | f _ {T}) ] | f _ {t} \} & \text { for   } t > T \end{array} \right. \end{array}
$$

where the expectation is taken with respect to the risk neutral probabilities.

The value of the call option after the early exercise assuming it is still alive can be determined in aŽ . straight forward manner using the Black–Scholes formula assuming that the forward price follows aŽ geometric Brownian motion process . In the absence . of dividends this formula has the form see Cex andŽ Rubenstein 2 and Hull 6 :<sup>w x</sup> <sup>w x</sup>.

$$
C _ {t} \left(k _ {0} \mid f _ {t}\right) = f _ {t} N (x) - k _ {0} r ^ {- 1} N \left(x - \sigma \sqrt {t}\right),
$$

where:

$$
x = \frac {\log \left(f _ {t} / k _ {0} r ^ {- 1}\right)}{\sigma \sqrt {t}} + \frac {1}{2} \sigma \sqrt {t}.
$$

![](/api/attachments/KH243HEM/fulltext/images/948a7f61ee04e0497cfcf2ad6a2d895edaca44cf17618143fba73d97255620a6.jpg)  
Fig. 6. Value of late call option Ž for geometric Brownian motion with notification interÕal Õolatility $\sigma \sqrt { T } = 1 )$

In the above formula, r represents the interest rate and NŽ . is the cumulative of the standardized normal distribution zero mean and unit standardŽ deviation . For simplicity we will ignore the interest.

rate, i.e., assume i<sup>s</sup>1 in the subsequent discussion. Fig. 6 illustrates the value of the late option at various times expressed as multiples of the early exercise time Ž . T .

![](/api/attachments/KH243HEM/fulltext/images/b0836d06b0aa1842751735502364ff4d255a88a3ba1ad528212541d410713088.jpg)  
Forward price /Late strike price  
Fig. 7. Value of double-call option at the two exercise times Ž for geometric Brownian motion with notification interÕal Õolatility $\sigma \sqrt { T } = 1 )$

![](/api/attachments/KH243HEM/fulltext/images/71443846c2225ed53acc82208867be94b900be9df525691bfb50b0a6c916425a.jpg)  
Fig. 8. Effective early strike price as function of double-call strike prices and notification interval Ž for geometric Brownian motion with Õolatility <sup>s</sup> 1 ..

Because of the early exercise option, we are only interested in the value of the late option if the early option is not exercised, i.e., for $t \leq T$ . The payoff function of the early option at $t = T$ is the largest of the early option payoff or the late option value at that time. Fig. 7 below illustrates the payoffs of a double-call option at delivery time and at the early exercise time. $\mathrm {  ~ { \cal ~ A } ~ t ~ } \ t = 0 .$ , it is the payoff function max 0, <sup>w</sup> $f _ { 0 } - k _ { 0 } ] ,$ whereas at the early exercise date, it is given by max<sup>w</sup> $f _ { \mathrm { T } } - k _ { \mathrm { T } } , ~ C _ { \mathrm { T } } ( k _ { 0 } | f _ { \mathrm { T } } ) ]$ . The curvedŽ line in Fig. 7 represents the value of the late call option at the early exercise time..

Note that the exercise price of the early option ${ \overline { { k } } } ,$ which was defined earlier, is higher than the early strike price due to the residual value of the late option. We refer to this early exercise price as the effective early strike. Under the Black–Scholes model, $\bar { k } ( k _ { 0 } , k _ { \mathrm { T } } )$ can be calculated from the implicit equation:

![](/api/attachments/KH243HEM/fulltext/images/55d329cef68b65e6479d238e3d287c35b0d647963c9390c9705ec073784a77bc.jpg)  
Fig. 9. Decomposition of a double-call option prior to the early exercise.

![](/api/attachments/KH243HEM/fulltext/images/e61543767c8582532c9dfaeca031a18b52551194abd96b3e6607f1e9382e2eaf.jpg)  
Fig. 10. Value of double call prior to early exercise time Ž for geometric Brownian motion with Õolatility $\sigma = 1 )$

$$
\begin{array}{l} \big (\bar {k} / k _ {0} \big) \big (1 - N (x) \big) + N \big (x - \sigma \sqrt {T} \big) = \big (k _ {T} / k _ {0} \big), \\ \text { where: } \end{array}
$$

$$
x = \frac {\log \left(\bar {k} / k _ {0}\right)}{\sigma \sqrt {T}} + \frac {1}{2} \sigma \sqrt {T}.
$$

Fig. 8 illustrates the above relationship between the effective early strike price and the two strike prices of the double-call option.

The valuation of the double-call option at times prior to the early exercise time is more involved and requires numerical integration or use of binomial trees. The calculation can be simplified by decomposing the double-call option into a regular call with strike price of $\bar { k }$ Ž . the effective early strike and an option on the late call option whose payoff function at time T is min $\dot { } c _ { \mathrm { t } } ( k _ { 0 } | f _ { \mathrm { T } } ) , \overline { { k } } - k _ { 0 } ]$ , The decomposition is illustrated in Fig. 9 below.

The value of the double-call option for $t > T$ can then be computed under the geometric Brownian Ž motion assumption as: .

$$
\begin{array}{l} \hat {C} _ {t} \big (k _ {T}, k _ {0} | f _ {t} \big) \\ = C _ {t - T} \big (\overline {{k}} | f _ {t} \big) + C _ {T} \big (k _ {0} | \overline {{k}} \big) \\ \qquad - \int_ {0} ^ {\overline {{k}}} \Big [ C _ {T} \big (k _ {0} | \overline {{k}} \big) - C _ {T} \big (k _ {0} | f _ {T} \big) \Big ] \mathrm{dPr} \big \{f _ {T} | f _ {t} \big \}. \end{array}
$$

Integrating by parts yields:

$$
\begin{array}{l} \hat {C} _ {t} (k _ {T}, k _ {0} | f _ {t}) = C _ {t - T} (\bar {k} | f _ {t}) + C _ {T} (k _ {0} | \bar {k}) \\ \qquad - \int_ {0} ^ {\bar {k}} \operatorname * {P r} \{f _ {T} | f _ {t} \} \frac {\partial C _ {T} (k _ {0} | f _ {T})}{\partial f _ {T}} \mathrm{d} f _ {T} \end{array}
$$

Assuming again that the forward price follows a geometric Brownian motion with expected return of 1, we have:

$$
\begin{array}{l} \operatorname * {P r} \bigl \{f _ {T} | f _ {t} \bigr \} = N \Bigg (\frac {\log (f _ {T} / f _ {t})}{\sigma \sqrt {t - T}} \Bigr) \quad \text { and } \\ \frac {\partial C _ {T} (k _ {0} | f _ {T})}{\partial f _ {T}} = N \Bigg (\frac {\log (f _ {T} / k _ {0})}{\sigma \sqrt {T}} + \frac {1}{2} \sigma \sqrt {T} \Bigg). \end{array}
$$

Let $y = \log { \left( f _ { \mathrm { T } } / k _ { 0 } \right) }$ We then obtain:

$$
\begin{array}{l} \hat {C} _ {t} (k _ {T}, k _ {0} | f _ {t}) = C _ {t - T} (\bar {k} | f _ {t}) + C _ {T} (k _ {0} | \bar {k}) \\ \qquad - k _ {0} \int_ {- \infty} ^ {\log (\bar {k} / k _ {0})} N \left(\frac {y - \log (f _ {t} / k _ {0})}{\sigma \sqrt {t - T}}\right) \\ \qquad \times N \left(\frac {y + (1 / 2) \sigma^ {2} T}{\sigma \sqrt {T}}\right) e ^ {y} d y \end{array}
$$

where $\overline { { k } } - k _ { \mathrm { T } } = C _ { \mathrm { T } } ( k _ { 0 } | \overline { { k } } )$ and $C _ { \mathrm { t } } ( k | f )$ is the value of a standard call without dividend or interest givenŽ . by the Black Scholes formula:

$$
C _ {t} (k | f) = f N (x) - k N (x - \sigma \sqrt {t}),
$$

where:

$$
x = \frac {\log (f _ {t} / k _ {0})}{\sigma \sqrt {t}} + \frac {1}{2} \sigma \sqrt {t}.
$$

In Fig. 10, we illustrate the price evolution of a double-call option for various values of t prior to the early exercise time when the forward price follows geometric Brownian motion. For illustrative purposes, we again assume notification interval volatility $\sigma \sqrt { T } = 1$ and early to late price strike ratio of $k _ { \mathrm { T } } / k _ { 0 } = 0 . 5$

## 5. Conclusion

In a competitive electricity market, financial instruments and derivatives based on underlying commodity futures will play an important role as means for risk management speculative investments and capital formation. Such instruments can also emulate traditional contracts between customers, utilities and independent power producers aimed at improving the efficiency of resource utilization. Custom design of financial instruments can be specifically targeted at implementing such contracts in a decentralized environment with independent decisions by buyers and sellers. Such targeted instruments reduce transaction costs and provide perfect hedging tools for buyers and sellers of electricity. However, while one could conceive of many exotic forms of options that would meet specific needs for hedging and speculation we should also emphasize the importance of standardization. No financial instrument can be viable without sufficient liquidity and proliferation of customized instruments may result in Athin marketsB with insufficient liquidity. It is not surprising, that only a small fraction of new futures and derivatives in stock and commodity markets develop sufficient liquidity to become viable. Finally, we like to emphasize that the pricing formulae derived in this paper are based on a geometric Brownian motion price model. Empirical evidence suggests that that model is inadequate as a representation of electricity spot price behavior. Our follow-up work on this topic will attempt to derive pricing formulas for the double-call option under more realistic price models that include mean reversion with stochastic jumps and regime switching.

## References

<sup>w</sup> <sup>x</sup> 1 H.P. Chao, R.B. Wilson, Priority service: pricing, investment and market organization, Am. Econ. Rev. 77 5 1987Ž . Ž . 899–916.

<sup>w</sup> <sup>x</sup> 2 J. Cox, M. Rubinstein, Options Markets,1985, Englewood Cliffs.

<sup>w</sup> <sup>x</sup> 3 ENRON, Managing Energy Risk, Chap. 11, The UK Electricity Market, Risk Publication, 104-112 Marylebone Lane, London W1M 5FU, 1995.

<sup>w</sup> <sup>x</sup> 4 T.W. Gedra, Optional Forward Contracts for Electric Power Service Contracts, PhD thesis, University of California, Berkeley, 1991.

<sup>w</sup> <sup>x</sup> 5 T.W. Gedra, P.P. Varaiya, Markets and Pricing for Interruptible Electric Power Transactions IEEE on Power Systems 92 WM 169-3 PWRS,1992.

<sup>w</sup> <sup>x</sup> 6 J. Hull, Options, Futures, and Other Derivative Securities, 2nd edn., 1993, Englewood Cliffs.

<sup>w</sup> <sup>x</sup> 7 T.P. Strauss, S.S. Oren, Priority pricing of interruptible electric power with an early notification option, Energy J. 14 2Ž . Ž .1993 175–195.

![](/api/attachments/KH243HEM/fulltext/images/ccbd61c316220a1efa61354a4a9af047f6241a3ac958bafae338b79e6e0eca19.jpg)

Dr. Shmuel S. Oren is a Professor of Industrial Engineering and Operations Research at the University of California at Berkeley and the former Chairman of that department. He is the Berkeley site director of PSerc, a multiuniversity Power Systems Research Center sponsored by the National Science Foundation and industry members. Prior to his current position, he was on the faculty of The Engineering Economic Systems Department at the Stanford University

and worked as a Research Scientist at the Xerox Palo Alto Research Center. He has served as a consultant to numerous private and public organizations and is currently a Senior Advisor to Hagler Bailly Consulting. His research and publications include numerical optimization, decentralization and coordination in complex systems, nonlinear pricing and the application of such pricing in the context of telecommunications and electric power, market design, auctions, financial engineering, transmission pricing, electricity market restructuring and other related topics. Dr. Oren holds BSc and MSc degrees in Mechanical Engineering from the Technion in Israel and MSc and PhD degrees in Engineering Economic Systems the from Stanford University.
