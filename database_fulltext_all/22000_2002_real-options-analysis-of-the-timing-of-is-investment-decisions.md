---
otero_id: 22000
otero_key: "EQFR77SW"
title: "Real options analysis of the timing of IS investment decisions"
authors: "John A. Campbell"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00101-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Real options analysis of the timing of IS investment decisions

John A. Campbell $^{*}$

School of Management, Faculty of Commerce and Management, Griffith University, Meadowbrook 4131, Australia
Received 20 November 2000; accepted 21 April 2001

## Abstract

Many information systems (IS) investments belong to a class of capital budgeting problem where there is an option: the investment may be made straight away or delayed for some period. A real options analysis could allow decision-makers to add value to these investment decisions by providing a framework that explicitly recognises uncertainty. This paper uses options pricing theory to determine the optimal timing of IS investments and to explore the effect of different investment review cycles. The findings provide support for the common industry practice of demanding short payback periods for IS investments. © 2002 Elsevier Science B.V. All rights reserved.

Keywords: Real options; IS investments; Investment timing

## 1. Introduction

Under conditions of uncertainty, investment flexibility is an important and valuable consideration. There is a growing view that the techniques used to evaluate financial options might be appropriate, in certain circumstances, for evaluating capital investments that have option like characteristics $[6,8,13,17,18]$ . These types of investment choices are often referred to as real options, as the investment opportunities typically involve real assets (information systems (IS), factories, new products, etc.) rather than paper-based assets (stocks, bonds, currencies, etc.).

For many approved capital projects there is often an option to delay the project start-up to a more suitable date if circumstances are not supportive. For example, management faced with implementing several large projects at the same time may opt for a staggered series of start-up dates to maximise resource availability and utilisation. This and other option-like characteristics are found in many IS projects. In recent times, strong arguments have been put forward for using options pricing theory to evaluate IS project investments (see, e.g. [3,4,9,20]). This literature advocates various innovative means of valuing investment flexibility using relevant aspects of options pricing theories. The range of investment options studied in this way are notably diverse and include growth, deferment, abandonment, switching inputs, altering operating scale, and phased research and development options.

One significant aspect of this research is the use of the real options approach to determine the optimal start-up date of IS investments. The common approach has been to determine the optimal time to begin the development of a project by deriving and analysing the value of waiting to invest $[1,11]$ . An alternative approach is to draw an analogy between the theoretical effect of stock dividends on the early exercise of an American style call option and the impact of investment deferral decisions on foregone project cash flow [7]. Although both approaches evaluate the opportunity cost of waiting to invest, the latter provides an explicit articulation of the investment decision criteria. This paper extends this work by using options pricing theory to assess the optimal timing of IS investments and the impact of different investment review cycles on the decision to invest.

## 2. Valuing IS investment options

Although several alternative options pricing techniques exist, the Black–Scholes model remains an accepted standard because of its computational simplicity and relative accuracy $[5]$ . The formula can easily be programmed into a computer or financial calculator and uses five readily obtainable input variables. This model has been shown to price European call options accurately when there are no dividends and more than 2 months to expiration $[19]$ . As a European call option can only be exercised when the option expires, its value is given by subtracting the expected present value of exercising the option from the expected terminal value of the underlying asset. That is

$$
C = V N (d _ {1}) - X \mathrm{e} ^ {- r T} N (d _ {2})\tag{1}
$$

where

$$
d _ {1} = \frac {\ln (V / X) + (r + 0 . 5 \sigma^ {2}) T}{\sigma \sqrt {T}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

and $N(\cdot)$ is the cumulative normal distribution function, V the value of the underlying asset, X the option exercise price, $\sigma$ the volatility, r the risk-free interest rate, T the option life

Unlike European call options, American call options can be exercised at any point in time for the life of the option. The Black–Scholes model can also be used to provide a reliable estimate of the value of an American call option, as long as there are no dividends paid during the life of the option $[10]$ . However, the valuation of an in-the-money American call option becomes problematic if the underlying asset pays a dividend, as it may be better for the option holder to exercise it immediately prior to the ex-dividend instant. The problem facing the American call option holder is depicted in Fig. 1. The option holder will obtain the cum-dividend value of the asset less the option exercise price if the option is exercised immediately prior to the dividend payment. However, if left unexercised, the dividend is forfeited and the value of the option is reduced.

![](/api/attachments/EQFR77SW/fulltext/images/730864b2793b8079bf0211c28b2b93d5fea22203bf8cca41a0c4010974f0e08e.jpg)  
Fig. 1. American call option price as a function of the ex-dividend value of the underlying asset.

$V_{t}^{*}$ is the critical ex-dividend asset value at which point the option holder is indifferent to exercising or continuing to hold the option. This indifference value is given by

$$
C (V _ {t} ^ {*}, T - t, X) = V _ {t} ^ {*} + D - X\tag{2}
$$

The two functions shown in Fig. 1, $V_{t} + D - X$ and $C(V_{t}, T - t, X)$ , intersect only if the ex-dividend decline in the asset price is more than the present value of the interest income that would be earned by deferring investment [2,21]. Therefore, an in-the-money cum-dividend American call option should only be exercised early when Eq. (3) is satisfied.

$$
D _ {t} > X [ 1 - \mathrm{e} ^ {- r (T - t)} ]\tag{3}
$$

The foregone free cash flows of an investment project are analogous to the dividends paid on a stock. Many organisations routinely review investment opportunities at discrete time intervals on a quarterly, 6-monthly, or yearly basis. If a project is deferred at one of these periodic reviews, the effect is to forfeit, at that instant, all project cash flows up to the next investment review. In this way, investment reviews have a similar effect on the value of an investment option as dividends have on the value of an American call option. However, unlike stock option holders, investment option holders have control over the size of foregone revenues through the choice of investment review frequency. Greater frequency will result in less foregone revenue between decision instances, while less frequent reviews will result in the forfeiting of larger amounts.

## 3. Modelling information technology investment options

Benaroch and Kauffman [2,3] use the example of an investment decision for identifying the most appropriate timing for the development and deployment of a point-of-sale debit card services system. In contrast, a hypothetical case of an investment in online logistics will be used to illustrate the concepts of real options as they relate to investment timing and the investment review cycle. $^{1}$ Online logistics can substantially reduce the costs associated with purchasing, storing, administrating and distributing inventory through better supply-chain management. Online logistics have enabled some organisations to reduce costs to such an extent that profit margins have almost doubled [12].

Human Systems Inc. (HUM) is a manufacturing organisation that has become aware of the merits of investment in online logistics because of the potential for large cost savings and the entry barriers such a system would create for new and existing competitors. While HUM could invest right away, it was also realised that the option to defer investment could allow the project start to be timed to maximise investment returns. HUM could defer investment, as there was no immediate competitive threat from any existing or potential competitor. While some savings would be given up, waiting before investing could yield additional benefits by providing time for rectifying some of the uncertainties about the project and the degree of organisational readiness. Therefore, the primary problem is to determine how long, if at all, HUM should defer investment in the online logistics project.

At each investment review, HUM can obtain the present value of all future cash flows (cost savings) by investing in the project. If it decides to defer investment, then all cost savings up to the next investment review date will be forfeited. Applying the same principles used to define Eq. (3), HUM should not invest in the project unless these foregone cash flows are more than the present value of the interest income that would be earned by deferring investment. The value of this interest income is the opportunity cost of giving up the option to defer project start-up. Consequently, the derivation of the optimal project start-up date requires a reconciliation of these two conditional expected values. Thus, an investment should not be made unless

$$
\mathrm{FC} _ {t} > X _ {t} [ 1 - \mathrm{e} ^ {- r (T - t)} ]\tag{4}
$$

where $FC_{t}$ is the present value of foregone cash flow from delaying investment, $X_{t}$ the discounted investment cost, T the maximum deferral period in years, t the length of the investment deferral period in years and r the annual risk free rate.

Table 1 shows the online logistics investment data and related assumptions based on a 6-monthly investment review cycle. An analysis of this data indicates that the optimal time to wait before investing in online logistics is approximately 3 years. Note that the present value of cost savings ( $A_{t}$ ) increases at each review for the first 2.5 years, indicating that early negative cash flow is more than compensated for by the present value of larger cash flow in later years.

Optimal project start-up based on 6-monthly investment reviews $^{4}$

<table><tr><td>t</td><td>0</td><td>0.5</td><td>1.0</td><td>1.5</td><td>2.0</td><td>2.5</td><td>3.0</td><td>3.5</td><td>4.0</td></tr><tr><td> $A_t$  (US$)</td><td>323233</td><td>342216</td><td>360083</td><td>376230</td><td>389207</td><td>395566</td><td>387166</td><td>344813</td><td>223295</td></tr><tr><td> $X_t$  (US$)</td><td>400000</td><td>393179</td><td>386473</td><td>379883</td><td>373404</td><td>367036</td><td>360777</td><td>354625</td><td>348577</td></tr><tr><td> $FC_t$  (US$)</td><td>-18983</td><td>-17867</td><td>-16147</td><td>-12977</td><td>-6359</td><td>8400</td><td>42353</td><td>121518</td><td>223295</td></tr><tr><td> $X_t[1 - e^{-r(T-t)}]$  (US$)</td><td>104993</td><td>94842</td><td>84342</td><td>73481</td><td>62246</td><td>50625</td><td>38603</td><td>26168</td><td>13305</td></tr><tr><td> $FC_t - X_t[1 - e^{-r(T-t)}]$  (US$)</td><td>-123976</td><td>-112709</td><td>-100489</td><td>-86458</td><td>-68605</td><td>-42225</td><td>3750</td><td>95350</td><td>209990</td></tr></table>

$^{a}$ Assumptions: The project is not in operation until 12 months after the project start-up date. The rate of inflation is 3.5%. Investment opportunities are reviewed every 6 months. A is the present value of cost savings less operational costs; X is the discounted cost of investment, $X_{0} = US\ 400,000$ ; FC is the foregone cash flow from delaying project start-up, $A_{t} - A_{t+0.5}$ ; $X_{t}[1 - e^{-r(T-t)}]$ is the interest income that would be earned by deferring project start-up; T is the maximum deferral period in years (5.5 years); t is the length of the investment deferral period in years; r is the annual risk free rate (7%).

Fig. 2 graphs the two investment decision variables over time. The graphing of these two functions better illustrates how optimal investment timing is determined by the size of foregone cash flow in comparison to the potential interest income that could be earned from investing in an alternative risk-free investment. The intersection of the two functions indicates when the project should proceed. From Fig. 2, this should occur a little before the 3-year deferment implied by a tabular representation of the data. However, if 6-monthly reviews are strictly adhered to, the optimal deferral period remains 3 years.

![](/api/attachments/EQFR77SW/fulltext/images/8404e142e824c046f7c90b354d5b91d4dfa6d1aa733cdd61854e8ce39f3957fc.jpg)  
Fig. 2. Interest income and foregone cash flow associated with a 6-monthly investment review cycle.

![](/api/attachments/EQFR77SW/fulltext/images/4a5287238b79dcd1f91dc337b8a53d7be0892ff6c87578610df73218a4e2a450.jpg)  
Fig. 3. Interest income and foregone cash flow associated with investment review frequency.

However, we need to assess the sensitivity of this result to the frequency that the investment opportunity is reviewed. As discussed earlier, the quantum of foregone cash flow is reduced or increased depending upon the length of time between reviews. Fig. 3 illustrates how different investment review cycles impact optimum investment timing by aggregating and interpolating the original 6-monthly data into different time-sets—monthly, quarterly, and yearly. It can be readily seen how less frequent investment reviews increase foregone cash flow. However, the investment review criterion is also shown to be remarkably robust when applied to this case data. The optimal time to invest is given by the first review where foregone cash flow during the next period is greater than the investment opportunity cost. This occurs after 3 years for the yearly and 6-monthly data, after 3 and a quarter years for the quarterly data, and some time after 3 and a half years for the monthly data. Despite these differences, the results must be interpreted cautiously as other cash flow series may produce different effects.

## 4. Modelling assumptions of investment timing options

Inputs for the timing method presented here are either directly observable or can be estimated with a reasonable level of confidence. For example, the inflation and risk-free interest rates are readily obtainable from market data. While estimates of project life, cash flow and investment value can be inferred from previous experience with similar projects or through the judicious use of expert opinion.

However, there are a number of more fundamental issues that threaten the validity of using options pricing theory to evaluate investment timing $[14]$ . These issues relate to assumptions about the characteristics and behaviour of the variables used to define options pricing models (see $[18]$ for an excellent discussion of appropriate option pricing models for different states of input variables).

As can be seen in Table 2, the characteristics of stock options are somewhat different to the characteristics of real investment options. In particular, there are important differences between project cash flows and stock dividends that need recognition. First, the timing and quantum of stock dividends are usually highly predictable, while project cash flows can be difficult to estimate accurately. Second, dividends always reduce the value of call stock options while forfeited project cash flows can be either negative or positive and, therefore, can either reduce or increase the value of an investment option.

Table 2  
Comparison between stock options and real investment option parameters

<table><tr><td>Option variables</td><td>Characteristics of stock options</td><td>Characteristics of investment options</td></tr><tr><td>Value of the underlying asset (V)</td><td>Stock price is set by a market and cannot be negative</td><td>Project value is not directly observable, can be negative, and is directly dependent on the present value of the net operating income or loss during the life of the projectProject values are more sensitive than stock prices to changes in interest rates</td></tr><tr><td>Exercise price (X)</td><td>A single known payment</td><td>An uncertain stream of payments over an extended time period</td></tr><tr><td>Volatility (σ)</td><td>Annualised standard deviation of stock price returnsVolatility can either increase or decrease during the life of the optionVolatility can be estimated using historical or implied variance data</td><td>Annualised standard deviation of project free cash flowVolatility tends to decrease during the life of the investment optionVolatility estimates can be derived from organisational project data, or from data from listed companies involved in similar project activities</td></tr><tr><td>Life of the option (T)</td><td>Finite and defined in advanceThe life of most stock options tend to be short to medium-term (&lt;2 years)</td><td>The life of an investment option is uncertainThe life of most investment options tend to be medium to long-term (2–5 years)The life of some investment options can be extended by modifying the project to suit emerging conditions</td></tr><tr><td>Risk-free interest rate (r)</td><td>An increase in interest rates reduces the present value of future dividends but increases the expected growth rate of the underlying assetThe value of a stock call options tend to increase as interest rates increase ([10], p. 153)</td><td>An increase in interest rates reduces the present value of future cash flows but increases the value of waiting to investBecause of the importance of interest rates in the calculation of project value, the value of investment options could be more sensitive than stock options to interest rate changes</td></tr><tr><td>Dividends (D)</td><td>Discrete dividend payments occurring at regular points in timeTiming and quantum is usually highly predictableDividends reduce the value of call stock options as they reduce the price of the underlying asset and are not paid to option holders</td><td>Continuous free cash flows foregone by delaying investmentTiming and quantum can be difficult to estimateProject cash-flows at any point in time can be either negative or positive and, therefore, can either reduce or increase the investment option value</td></tr></table>

Another concern is the specification of the life of an investment option. The time to expiration for most financial options is finite and fixed in advance. However, the life of an investment option can increase or decrease, depending on new technological developments or sudden changes in the competitive environment. An organisation may also seek to manage its investment options actively by pursuing strategies and supporting tactics aimed at maximising the value and useful life of investment options $[15,16]$ . Clearly, the optimal time to invest in a project is highly sensitive to the duration of the option. Substantial increases or decreases in the life of an investment option could significantly reduce accuracy when estimating the optimal time to invest.

The approach here has significant advantages over other valuation methods that are based on options pricing theory. First, the method does not require an estimation of the variance of future project cash flows. This is a major strength, as options pricing models are very sensitive to small changes in variance and it is often difficult to obtain reliable estimates of variance in real-world settings. A second advantage is that the investment timing decision criterion is easy to understand and requires little calculation. It provides practitioners and researchers with a useful tool for studying the timing of IS investment.

## 5. Discussion

A special feature of many IS investments is that there is often an option for the investment to be undertaken immediately or to be delayed, sometimes for several years. The problem, where a project may be delayed, is to quantify the waiting period that will maximise the value of the project. When considering information technology investments, managers should recognise that the characteristics of project flexibility are important and valuable considerations, particularly when there is a high degree of uncertainty about the investment outcome. While the initial net-present-value of many information technology projects can be negative, an option pricing approach can sometimes reveal a positive project valuation by recognising the value of investment flexibility. Discounted cash flow methods are highly dependent on the arbitrarily determined risk-adjusted discount rate applied to the project cash flows. In contrast, real option approaches avoid this difficulty by using risk-free interest rates that can be easily obtained from market data. Most importantly, the investment decision-making process is better informed by modelling project contingencies as real options with specific value characteristics that can be used to identify an optimal project start-up date.

Unlike other real option approaches, the method presented here seeks to exploit the certainty of early cash flows by providing a rationale for the early exercise of an investment option. The decision criterion has several implications for managers and researchers, some of which might appear on face value to be counter-intuitive. For example, it has long been accepted that many strategic investments are better undertaken sooner rather than later so that strategic impact is maximised. However, our model suggests that immediate investment is not always preferred. One testable implication is that highly agile organisations that continuously review their investment options should tend to defer projects for longer periods. This is because early investment will tend to reduce agility by limiting the range of future courses of action available to the organisation. Based on the study results, early investment should occur only when a project has a very-high positive cash flow immediately after system implementation. The method, therefore, emphasises the importance and value of strong early cash flow. This is an important feature, as these closer cash flow numbers will generally be more certain and, therefore, more predictable than later ones. This agrees with the common industry practice of demanding comparatively short pay back periods from IS investments.

Although the results were shown to be robust with respect to investment review frequency, further research is required to establish the generality of the approach. For example, the case data used here ignored the costs and savings associated with suspending or completely abandoning the project at some future date. Further, if project cash flow has high serial correlation and dependence on the start-up date itself, then a matrix of values might be needed.

## References

[1] M. Amram, N. Kulatilaka, Real Options: Managing Strategic Investment in an Uncertain World, Harvard University Press, Boston MA, 1999.

[2] G. Barone-Adesi, R.E. Whaley, The valuation of American call options and the expected ex-dividend stock price decline, Journal of Financial Economics 17, 1986, pp. 91–111.

[3] M. Benaroch, R.J. Kauffman, A case for using real options pricing analysis to evaluate information technology project investments, Information Systems Research 10 (1), 1999, pp. 70–86.

[4] M. Benaroch, R.J. Kauffman, Justifying electronic banking network expansion using real options analysis, MIS Quarterly 24 (2), 2000, pp. 197–225.

[5] F. Black, M. Scholes, The pricing of options and corporate liabilities, Journal of Political Economy 81, 1973, pp. 637–654.

[6] N.P. Bollen, Real options and product life cycles, Management Science 45 (5), 1999, pp. 670–684.

[7] J.A. Campbell, Identifying an optimal start-up date for information technology investments: a real options approach, Working Paper, Faculty of Commerce and Management, Griffith University, Australia, 2000.

[8] A.K. Dixit, R.S. Pindyck, The options approach to capital investment, Harvard Business Review 73 (3), 1995, pp. 105–115.

[9] T.W. Faulkner, Applying ‘options thinking’ to R&D valuation, Research Technology Management 39 (3), 1996, pp. 50–56.

[10] J.C. Hull, Options, Futures, and Other Derivative Securities, 2nd Edition, Prentice-Hall, Englewood Cliffs, NJ, 1993.

[11] N. Kulatilaka, The value of flexibility: a general model of real options, in: L. Trigeorgis (Ed.), Real Options in Capital

Investment: Models, Strategies, and Applications, Praeger, Westport, CT, 1995, pp. 121–132.

[12] P.G.W. Keen, IT's value in the chain, Computerworld 34 (7), 2000, pp. 48.

[13] R.L. Kumar, A note on project risk and option values of investment in information technologies, Journal of Management Information Systems 13 (1), 1996, pp. 187–193.

[14] D.M. Lander, G.E. Pinches, Challenges to the practical implementation of modelling and valuing real options, Quarterly Review of Economics & Finance 38, 1998, pp. 537–567.

[15] T.A. Luehrman, Investment opportunities as real options: getting started on the numbers, Harvard Business Review 76(4), 1998a, pp. 51–67.

[16] T.A. Luehrman, Strategy as a portfolio of real options, Harvard Business Review 76 (5), 1998b, pp. 89–99.

[17] C.S. Park, H.S.B. Herath, Exploiting uncertainty-investment opportunities as real options: a new way of thinking in engineering economics, The Engineering Economist 45 (1), 2000, pp. 1–36.

[18] M. Perlitz, T. Peske, R. Schrank, Real options valuation: the new frontier in R&D project evaluation, R&D Management 29 (3), 1999, pp. 255–269.

[19] P. Ritchken, Options: Theories, Strategy, and Applications, Scott Foresman, London, 1987.

[20] A. Taudes, M. Feurstein, A. Mild, Options analysis of software platform decisions: a case study, MIS Quarterly 24(2), 2000, pp. 227–243.

[21] R.E. Whaley, On the evaluation of American call options on stocks with known dividends, Journal of Financial Economics 9, 1981, pp. 207–211.

John A. Campbell is a Senior Lecturer in the School of Management, Griffith University, Australia. His publications include topics on business finance, asset valuation models, executive information systems, group support systems, organisational communication and strategic IT management. His current research interests are focused on strategies for managing networked organisations in changing marketplaces and include topics in electronic-commerce, computer mediated communication and virtual communities.
