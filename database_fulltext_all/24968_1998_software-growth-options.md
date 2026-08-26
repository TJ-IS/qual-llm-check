---
otero_id: 24968
otero_key: "MZMED27A"
title: "Software Growth Options"
authors: "Alfred Taudes"
year: "1998"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1998.11518201"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Software Growth Options

## Alfred Taudes

To cite this article: Alfred Taudes (1998) Software Growth Options, Journal of Management Information Systems, 15:1, 165-185, DOI: 10.1080/07421222.1998.11518201

To link to this article: http://dx.doi.org/10.1080/07421222.1998.11518201

![](/api/attachments/MZMED27A/fulltext/images/65747eb31b18118970917cc277af28b09848b946f415aed6fca38ad5e3bb437e.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/MZMED27A/fulltext/images/f653bcf30242d5f17791ab6eac3a1700832c06292a34d4c59856c24afe31966b.jpg)

Submit your article to this journal ↗

![](/api/attachments/MZMED27A/fulltext/images/3f1e95a401f630e240c65ae9fe2285138deecb57dc6b06386824f04e85e5523b.jpg)

Article views: 1

![](/api/attachments/MZMED27A/fulltext/images/cbd25efbd221180c09b13767f2190db74a37330f878643471d51fe269ab17b2b.jpg)

View related articles ↗

![](/api/attachments/MZMED27A/fulltext/images/ed850a4a69b5ecde97405d8453d440e6692d9ca6970788206503c32d8dceb04e.jpg)

Citing articles: 3 View citing articles ↗

# Software Growth Options

ALFRED TAUDES

ALFRED TAUDES is Full Professor of Management Information Systems and Head of the Department of Industrial Information Processing at the Vienna University of Economics and Business Administration (WU). Currently he is visiting professor at the Institute of Policy and Planning Sciences of Tsukuba University. He holds a master's degree in MIS from Vienna University and a Ph.D. in business administration from the WU. Previously, he was Associate Professor of MIS at Münster University, Germany, and Full Professor of MIS at Augsburg and Essen Universities, Germany. He is the author or coauthor of several books and more than fifty articles on various aspects of MIS, among them papers in such journals as Applied Computer Science, European Journal of Operations Research, Information Management, Marketing Science, and International Journal of Marketing. Dr. Taudes has consulting experience in the design and implementation of DSS, manufacturing information systems, and the development of strategies for implementing standard software, which is also one of his current research interests.

ABSTRACT: Today's business environment is characterized by global competition and buyers' markets. Under such conditions, flexible response to changes in the environment is a key success factor for any firm. Consequently, there is increasing pressure for information systems to be readily adaptable to changing business processes. This paper investigates ways of introducing this aspect of IS extendability into quantitative IT investment decision models via the application of real options models. In particular, it examines methods for evaluating sequential exchange options in order to obtain estimates for the value of software growth options—that is, IS functions that are embedded in an IT platform and that can be employed once the particular base system is installed and their use is economically justified. On the basis of these models, we look at the determinants of the value of software growth options and draw general conclusions with regard to decision making in the field of IT investment.

KEY WORDS AND PHRASES: capital budgeting, cost/benefit analysis of information systems, MIS platforms, real options.

IN THE DESIGN STAGE OF AN INFORMATION SYSTEM (IS), one often encounters functional requirements whose implementation is not financially justified at the time but that may become useful in the future. Examples of such situations are:

1. Currently a company does business only in its home country. However, if its business should expand abroad, the IS installed must be able to handle different languages and currencies, new methods of payments, and so on.

2. A company produces several variants of a standard product. To use temporarily underutilized resources, management decides to rent out machinery and personnel to other manufacturing companies on an hourly basis. If this kind of business is added to the current manufacturing process, a new type of order entailing different costing and scheduling must be supported by the firm's production planning and control system.

3. Market pressure is growing to deliver customer-specific add-ons and modifications to standard products within a short time and at reasonable cost. If the number and impact of such customer-specific orders increase, a company's production planning and control system must be able efficiently to support a variety of bills of materials and work schedules, for example, via a bills of materials processor.

4. Instead of installing the latest release of SAP's mainframe system R/2, a firm considers migrating to the client/server version SAP R/3, as the new platform will permit easy adoption of novel software technologies such as EDI, workflow management, or document retrieval and archiving once these IS functions are required.

Intuitively, a knowledgeable systems analyst will not neglect such possible requirements but will take care that the existing IS can be easily enhanced in the directions indicated. Similarly, when judging the economic feasibility of an IS project or comparing alternative IS platforms for a given specification, one should evaluate the benefits achieved from such possibly needed IS functions.

Capital budgeting offers quantitative methods for such evaluation tasks. A standard capital budgeting technique is the net present value rule. It is based on the net present value (NPV), calculated as the discounted sum of net benefits minus the investment cost, and states that an investment should be undertaken if its NPV is positive and that, if various independent investment alternatives are compared, the project with the highest NPV should be selected. Net benefit/period, investment cost, and discount rate are assumed to be given as in other similar methods (see, e.g., [21, p. 24 ff.]).

Clearly, one can use the NPV method to evaluate the type of IS function presented above, if the future development is known for sure and the IS function's implementation date is fixed. Consider, for instance, the possibility of introducing EDI in example 4. If one assumes that the net benefit per electronic transaction is \$100, $^{1}$ and that the quantity of possible electronic transactions rises from \$500 by \$100 per year because of the increasing number of possible partners, the NPV for an immediate implementation based on an 8 percent risk-free interest rate and a ten-year planning horizon is given by:

$$
N P V = \sum_ {t = 0} ^ {1 0} \frac {5 0 , 0 0 0 + 1 0 , 0 0 0 t}{(1 + 0 . 0 8) ^ {t}} - I = 7 1 2, 3 7 3 - I.\tag{1}
$$

Thus, if the implementation cost I is less than \$712,373, the EDI function should be installed; otherwise it should not. Now assume that the increase in net benefit/year is not known for sure, but that there is a probability of 0.45 that the number of electronic transactions will decrease by \$100, for example, because the number of business partners using the same EDI format is decreasing. What value should we now consider for the EDI function? A natural choice would be an “expected NPV.” In our case, this value is given by $^{2}$

$$
E (N P V) = V - I = \sum_ {t = 0} ^ {1 0} \frac {5 0 , 0 0 0 + 1 , 0 0 0 t}{(1 + 0 . 1) ^ {t}} - I = 3 8 6, 2 6 4 - I,\tag{2}
$$

as the stochastic process describing the development of the net benefit/period is a random walk and thus the cumulative change in period t, t > 0 follows a binomial distribution with parameters $(nt, (p-q))$ , where n is the size of a move, p is the probability of an upward move, and q is the probability of a downward move.

Usually, the expected NPV is proposed to “save” the NPV formula for the case of investment under uncertainty. If in our case I > 386,264, the expected NPV rule suggests that the implementation of EDI should not be considered. There we have implicitly assumed that EDI is implemented immediately. However, if possible, a reasonable decision maker would rather wait with the investment to see if developments are favorable. If, for instance, I = 400,000 and one waits to see whether V = 80,000 in period 4, a positive expected NPV of 11,852 $\left[\Sigma_{t=4}^{10}(80,000 + 1,000t)/(1.1^{t}) - (400,000/1.08^{4})\right]$ is obtained.

In fact, the essence of “flexibility” is the ability to change the “configuration” of the asset obtained through investment in response to unknown future events instead of following a policy fixed at the beginning of the planning horizon. Therefore, formula (2) yields only a lower bound for the value of an investment alternative with embedded flexibility if configuration changes are made in an optimal way. In such a case, the expected present value V of a project depends on the policy of change chosen, and the actions taken depend on the development of the environment. Actually, for the IS functions described above, the calculation in equation (2) will usually yield a negative expected NPV, as we assume that their “implementation at that time is not justified from a financial standpoint” and that the benefit of such an IS function lies in the possibility to implement it, if the environment develops in a certain way. Intuitively, a proper valuation method should therefore also give a positive value to IS functions present in an IS platform even if for the IS function the expected NPV is negative when calculated under the assumption that the IS function is to be implemented now.

In fact, the problems arising with the application of traditional capital budgeting methods in the IS field are not new. Based on an empirical survey of the usage of methods for capital budgeting in IS development, Tam [18], for instance, found that IT practitioners had problems when determining model parameters such as the time series of costs and revenues of an IS project or the appropriate discount rate for the NPV rule. Consequently, simple, static models are often preferred to the net present value rule, and important project decisions are based on intuition, experience, and rule of thumb rather than on quantitative analysis.

One reason for this lack of appraisal of quantitative methods for evaluating IS investments may be that traditional capital budgeting methods cannot adequately cope with the flexibility embedded in many investments in IS, as they are based on the assumption either that there is no flexibility or that the investment is reversible, that is, that it can somehow be undone and the expenditures recovered should the environment turn out to be worse than anticipated $[3, p. 6]$ . As the above examples show, in the case of IS there usually is the possibility to extend or to modify the system. Furthermore, investments in IS are largely irreversible: Investments in software development are sunk costs that cannot be retrieved if the software turns out to be unusable in the future. Similarly, contracts concluded in this field are usually worded in such a way that the usage fees for standard software cannot be regained if the requirements of the IS change during usage.

For this type of irreversible investment with flexibility, the “real options” literature (e.g., [20]) proposes that the traditional NPV should be expanded to a “strategic NPV” defined as:

$$
\begin{array}{l} \text { Expanded   (strategic)   NPV = passive   NPV   of   expected   cash   flows } \\ \quad + \text { value   of   options   from   active   management. } \end{array}\tag{3}
$$

In our application area, the first term refers to the difference between the discounted sum of net benefits generated by using the base configuration of the information system under study and its implementation cost, while the second term is the value of the possibility to introduce IS functions like those described at the beginning of this section when found beneficial. To evaluate these possibilities, we use the similarity of flexible IS usage and financial options: Financial options offer the holder the right to buy, sell, or exchange a financial asset under boundary conditions that, for instance, specify the period during which the right can be exercised or the relevant exercise price. Options need not be exercised. Real options, on the other hand, offer the owner of an asset with embedded flexibility the possibility—but not the obligation—of changing the asset’s configuration—in our case, by implementing additional IS functions.

Traditionally, real option models concentrate on flexibility in capital investments that produce or handle traded commodities such as oil or copper, $^{3}$ because in such a case the model's parameters can be determined easily. However, Trigeorgis recently proposed the application of real option methods to “information technology or other platform investments” as a direction for future research [20], and a number of papers with applications in other areas have appeared. $^{4}$ The only paper using real options for valuing IS projects known to the author is Dos Santos [4], who uses Margrabe's exchange option model (see [10]) to determine the second term in equation (3) for an IS project using a novel technology for testing purposes. Dos Santos states that such a project generates the option to use the new technique for future projects in case it turns out useful—for example, if it increases the NPV of future projects due to learning and experience. Dos Santos concludes that “The options pricing literature has developed a great deal over the past 15 years and numerous models have been developed for use in pricing different types of securities options. While this paper has showed [sic] how one such model can be used in evaluating new IT investments, the use of options pricing models to determine the value of other types of IT investments should be investigated. Such work will help put ‘justification’ tools that can be used to handle a wide variety of problems into the hands of knowledgeable investment evaluators.” Similarly, Tam [18] argues, “In recent years there has been a growing interest in using the option pricing framework to incorporate the option to delay an investment decision. This approach has tremendous ramifications, because the option to offer new services and to enter new markets is contingent on the decision of the initial investment. Very often, the opportunity to expand or develop new products is described as strategic and having an intangible payoff in the IS literature. The availability of a formal model derived from option pricing theory will provide a valuable means to quantify opportunities in a more explicit way.”

This paper starts with a formal description of the type of IS flexibility studied and the usage of option pricing methodology for its valuation. The benefit of the implementation of a flexible IS platform can be viewed as consisting of the benefit of the base configuration chosen and the value of the “software growth options” embedded—that is, the possibility of introducing new IS functions when it is economically feasible to do so. Subsequently, we shall look at analytical models for the valuation of various types of software growth options to obtain an estimate of the second term in equation (3). We shall also examine the implications of these methods for the dependence of the value of a software growth option on characteristics of the IS platform and the business environment and discuss the relevance of software growth options for IS investment decision making.

## Software Growth Options

## The IS Enhancement Process

WHEN CHECKING THE EXAMPLES GIVEN OF COMMON ELEMENTS, the following picture of flexible IS usage emerges (see figure 1):

\- The implementation of a base configuration is started at time $t_0$ . The implementation takes until time $t_1$ , provides a particular passive NPV as given in the first term of equation (3) and offers several software growth options, $^5$ such as the possibility to invoke an IS function after time $t_1$ . In the sequel, we deal with valuing one software growth option and then return to the valuation of several software growth options latter. In figure 1, $t_2$ was chosen as a suitable time to implement the IS function under consideration.

\- Depending on its nature, an IS function that forms a software growth option can be implemented at various times $t_2, t_3, \ldots$ , (“implementation decision points”) within a given planning horizon $T$ . Bookkeeping systems, for instance, are usually put into operation only at the start of a new fiscal year. Another type of restriction may be the fact that other IS functions must be available. An MIS, for instance, can only be used if systems that deliver operating data are installed.

\- The net benefit of an IS function that forms a software growth option in a particular period of a specified length is given by

![](/api/attachments/MZMED27A/fulltext/images/43aa07ea76d97b623a020b9da418b52c4b114d83d55444cf61afd6dc7d283095.jpg)  
Figure 1. Software Growth Option

$$
P _ {t} = N _ {t} (p - c) - K,\tag{4}
$$

where $N_{t}$ denotes the number of times the IS function is used during one period, $p$ the benefit/usage, $c$ the variable cost/usage, and $K$ the fixed cost per period. $p$ and $c$ are assumed to be given with $p > c$ ; $N_{t}$ varies stochastically. $p$ can be considered as cost savings and/or properly valued productivity gains, $c$ as operating cost. $K$ can be caused by periodic licensing fees and/or specialized supporting personnel that must be available regardless of the IS function's actual usage.

\- There is a cost of invoking the IS function that is the basis of the software growth option. It can be composed of the (re)programming effort, licensing fees, cost of additional hardware, parameterizing effort, and so on. The implementation cost can be fixed or it can vary stochastically, for example, due to unknown price reductions in the future. $^{6}$ In the case of deterministic implementation costs, we denote them by $F$ , otherwise by $I$ .

\- There may also be a cost $E$ for providing in the base configuration the basis for a later use of the IS function to be decided upon at a given time. If $E$ is not spent, the option to implement the IS function later is lost. An example could be the addition of functions to bookkeeping accounts with a view toward using them when the cost accounting module is introduced.

## Contingent Claims Analysis of Software Growth Options

One possibility to evaluate software growth options is to apply the option pricing theory developed for the valuation of contingent claims to securities and other traded assets. The goal of such a valuation is to value a claim to a security—or, more generally, to an “underlying asset”—as if it were traded in a frictionless market $^{7}$ where there are no transaction costs or taxes, no restrictions on short sales, where full use of proceeds is allowed, all shares of all securities are infinitely divisible, and borrowing and lending at the same rate are unrestricted [21, p. 83]. These assumptions are reasonable for financial options but need critical assessment in the case of real options. In particular, the following four questions must be dealt with when applying the option pricing theory to capital investment:

\- What is the underlying asset and how is its value determined?

\- What kind of stochastic process is reasonable for describing the development of the value, and how can its parameters be estimated?

\- Can the “no arbitrage condition” used in deriving the value function of financial options be employed in the application area in question?

\- Are closed-form analytical expressions for the value function available, and what kind of restrictions must be placed on the general situation described above to permit their application?

For an option on a security, the value of the underlying asset is the price of the security continuously determined via trading. The value of a particular IS function is the expected present value of the net benefits/period generated by its usage according to equation (4) and, thus, must be estimated by management. It is therefore much more ambiguous than, say, a stock price.

Most option pricing formulas are based on the assumption that the value of the underlying asset follows a geometric Brownian motion. Hence, in our application context, one can assume that the net benefit per period P gained through the usage of an IS function follows a geometric Brownian motion; that is,

$$
d P = \alpha P d t + \sigma P d z,\tag{5}
$$

where $\alpha$ is the drift parameter, $\sigma$ the variance parameter, and $dz$ the increment of a Wiener process, that is $dz = \varepsilon_t\sqrt{dt}$ where $\varepsilon_{t}$ are serially uncorrelated, normally distributed random values with zero mean and unit standard deviation. In that case, the value of the IS function under study defined as the expected present value of the net benefits/period obtained through the IS function's usage is given by

$$
V = E \left[ \int_ {0} ^ {\infty} P _ {t} \exp^ {- \mu t} d t \right] = \frac {P _ {0}}{\mu - \alpha},\tag{6}
$$

that is, V also follows a geometric Brownian motion. There, $\mu$ is the risk-adjusted discount rate and $\mu > \alpha$ . Besides the fact that the value of an IS function is not revised continuously but at discrete times following the availability of new information to management, equation (5) implies that P is always greater than zero. Generally, this is only true if the fixed cost K in equation (4) can be neglected.

For traded assets, time-series data about the development of V can be used to estimate $\alpha$ and $\sigma$ . For our area of application, subjective estimates by management based, for example, on business process reengineering studies, experiences from similar projects, or the like must be used for parameter estimation. A suitable method for this task can be based on the fact that from equation (5) the percentage change of P follows a Brownian motion with drift, that is, $dP/P = \alpha dt + \sigma dz$ , so that the percentage change over any time interval $\Delta t$ is normally distributed with the expected value $\alpha\Delta t$ and variance $\sigma^{2}\Delta t$ . Thus, in view of equation (4), management will have to answer two questions regarding the development of P to obtain parameter estimates:

\- By what average percentage will the number of uses of the IS function under study grow in one period? The answer will provide an estimate for $\alpha$ .

\- Below which value $\gamma$ will the percentage change lie with a 95 percent probability? Due to the normal distribution, an estimate $^{9}$ for $\sigma^{2}$ will then be given by $[( \gamma - \alpha)/2]^{2}$ .

Critics of this method may argue that it is as undisciplined and unrepeatable as the less complex qualitative decision rules described in $[18]$ . However, to counter this argument we would stress that only the dynamics of the development of the net benefit/period are estimated subjectively. These estimates can be subjected to checks for their plausibility relative to other similar projects and, ex post, to the values actually observed. For instance, such an evaluation is not possible with an average “flexibility index” obtained from ordinally scaled judgments about this attribute $[1]$ . Furthermore, here “a rigorous option analysis will help management to identify the crucial variables and to see how the adoption and valuation decision are effected by risk, cash-flow projections, interest rates, and other important variables” $[16, p. 4]$ .

We return to our EDI example: One can obtain empirical evidence regarding size and determinants of the benefits of EDI from $[11]$ . Mukhopadhyay et al. analyze the impact of EDI at Chrysler based on data collected at the plant level from nine assembly facilities during the period 1981–90. They categorize the benefits detected into savings in:

\- Inventory holding cost: Due to increased accuracy of shipment information, buffer stocks can be decreased.

\- Obsolete inventory cost: For the same reason, write-offs of obsolete inventory can be reduced.

\- Transportation cost: Increased accuracy and long-term planning data permit better usage of truck capacity.

\- Premium freight: Because of reduced shortages, the number of emergency deliveries can be lowered.

\- Document handling cost: Thanks to electronic data interchange, a number of clerical tasks regarding data entry, document filing, and the like can be saved.

Mukhopadhyay et al. build econometric models where these variables are regressed against a measure of EDI penetration and several other factors such as parts' variety and model changes in order to isolate the effect of EDI. In general, Mukhopadhyay et al. find a significant and approximately linear dependence of the different types of cost savings described above and EDI penetration. This lends credibility to equation (4). No data regarding the type of stochastic process that describes the growth of EDI penetration are given, but when we look at the growth path of other products that exhibit network economies of scale like the Internet, for instance, it is plausible that in the growth phase the development of the number of uses of the IS function is characterized by a constant average growth rate. Nevertheless, more empirical work dealing with this and the other above described assumptions of the geometric Brownian motion model is needed: For instance, while it seems plausible that there are unbounded deviations from the mean percentage change in both directions, empirical tests of whether the normal distribution is a suitable model for the percentage change of P are necessary. Also, the effects of the approximation of the real-world discrete time process describing the development of P by the continuous time geometric Brownian motion model should be investigated.

Differential equations describing the movement of the option value as a function of the value of the underlying asset can be derived on the basis of the “no arbitrage condition,” which states that the value of an option must be set equal to the value of a replicating portfolio of a risk-free asset and the underlying asset that gives the same value as the option at the end of its exercise period, as otherwise risk-free profits—arbitrage opportunities—would be possible.

As, in our case, the underlying asset—the IS function under study or the right to use the particular IS function in the case of standard software—is not traded, this condition does not hold. However, it is possible to demonstrate that the results obtained via the no arbitrage condition also hold, if the value of the underlying asset is perfectly correlated with a traded “twin security” that can also be a possibly dynamic portfolio of traded assets. This condition is usually satisfied when flexibility is studied in assets producing standardized commodities like oil, minerals, and agricultural products where risk concerns the commodity price. Hence, it is not surprising that early adoptions of real option models occurred in this field. The second phase of application is characterized by works such as $[15]$ where well-traded but not standardized products, such as real estate, represent the area of interest. According to Sick $[16]$ , the final area of adoption of real option models is investment in totally new products where no historic data are available and the construction of a perfect twin security is not possible. This will usually be the case in our field of application where at least part of the risk cannot be hedged via a combination of traded assets. Typically, the technical risk or the risk of user acceptance is “private” rather than “diversible” risks. In such situations, decision analysis is a proper valuation method, as it aims at determining the subjective value of the decision maker $[17]$ . In particular, Smith and Nau $[17]$ propose a combination of decision analysis and option valuation techniques so that the opportunities to hedge via buying and selling securities are incorporated when folding back the decision tree. $^{10}$ While such an approach is clearly suitable for a detailed analysis, we stick to the “market valuation” approach as an approximation for several reasons:

\- Since, in our context, the value of the underlying asset can only be approximated, there is no point trying to be overly precise where the option value is concerned. $^{11}$

\- For a software vendor, who has to decide which IS functions to offer in a future release and who has no information about the subjective preferences of his or her potential customers, it makes sense to get an idea of the “market value” of a software growth option.

\- Closed-form analytical expressions permit a straightforward analysis of the sensitivity of the option value to variations in the parameters of the value function and may be familiar to the finance people who are in charge of project evaluation. Furthermore, with several judgments of $\gamma$ , one can build a 95 percent confidence interval of $\sigma^2$ and, hence, of the option value.

\- However, analytical formulas are only available for certain simplified situations that do not cover all the options present in real life. Nevertheless, often only a lower bound for the value of a software growth option is needed. Consider our example of the decision between R/2 and the introduction of R/3. In such a case, the relevant question is: “Is the value of the software growth options embedded in R/3 high enough to justify the higher implementation cost?” Thus, only a lower bound for the option value of EDI, workflow management, or document retrieval and archiving is needed.

## Valuation as a Sequential European Exchange Option

Consider an IS function that forms a software growth option and assume that in figure 1 there is only one implementation decision point: In $t_1$ the implementation of the base configuration is finished, and one can decide to spend preparation effort $E = qI$ , $q \geq 0$ , where $I$ denotes a random implementation cost that follows a geometric Brownian motion to obtain the opportunity to implement the IS function in $t_2$ . Clearly, until $t_1$ the usage of any IS function is not possible. Assume further that the IS function under study cannot be implemented before $t_2$ , even if business development since $t_0$ implies a significant number of function usages, for example, because the base configuration must be tested for a certain period of time and/or the IS function's invocation is tied to a particular date (e.g., to the end of a year).

In such a setting, the software growth option resembles a sequential (European $^{12}$ ) exchange option—in other words, together with the benefits of the base configuration, the user obtains the claim to the future net benefits of the usage of a particular IS function V (value of the underlying asset) via investing a certain amount E = qI at t1 and I (delivery asset) at time $t_{2}$ (exercise period). No “dividend payments,” that is, net benefits that the user of an implemented IS function obtains and the owner of an option on the IS function’s implementation misses, are lost since the IS function cannot be used earlier.

The value of such a sequential exchange option is derived in equation [2] as

$$
F _ {c} (V, I, q, t _ {1}, t _ {2}, \sigma^ {2}, \sigma_ {I} ^ {2}, \rho_ {V I}, r) =\tag{7}
$$

$$
V B \left(d _ {1} \left(\frac {R \exp^ {r t _ {1}}}{R ^ {*}}, t _ {1}\right), d _ {1} \left(R \exp^ {r t _ {2}}, t _ {2}\right)\right) -
$$

$$
I \exp^ {- r t _ {2}} B \left(d _ {2} \left(\frac {R \exp^ {r t _ {1}}}{R ^ {*}}, t _ {1}\right), d _ {2} \left(R \exp^ {r t _ {2}}, t _ {2}\right)\right) -
$$

$$
q I \exp^ {- r t _ {1}} N \left(d _ {2} \left(\frac {R \exp^ {r t _ {1}}}{R ^ {*}}, t _ {1}\right)\right),
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$t_2$ = implementation decision time;
</div>

where

$V =$ value of the IS function under study, expected present value of net benefits of usage;

I = cost of implementing the IS function under study, R = V/I;

$q =$ fraction of $I$ needed for implementation preparation;

$t_{1}$ = decision time for implementation preparation (start of productive use);

$R^{*} =$ value of $R$ above which the (simple) exchange option should be

acquired at $t_1$ obtained by solving

$$
F _ {M} (V, I, t _ {2} - t _ {1}, \sigma^ {2}, \sigma_ {I} ^ {2}, \rho_ {V I}, r) - E = 0 \mathrm{for} R,
$$

where $F_{M}$ is given by Margrabe's exchange option formula in equation (8) below;

$$
\sigma_ {2} ^ {t _ {2}}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\sigma^2 =$ instantaneous variance of $V$;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\sigma_I^2$ = instantaneous variance of $I$;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\rho_{VI} =$ correlation between $V$ and $I$;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$N(.)$  = cumulative standard normal distribution function;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$B(. , .) =$ bivariate cumulative standard normal distribution function with
</div>

$$
\sqrt {t _ {1} / t _ {2}}
$$

$$
d _ {1} (\theta , \tau) = (\ln \theta + \frac {1}{2} \omega^ {2} \tau) / \omega \sqrt {\tau};
$$

$d_{2}(\theta ,\tau) = d_{1}(\theta ,\tau) - \omega \sqrt{\tau};$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\omega^2 = \sigma^2 +\sigma_I^2 -2\sigma \sigma_I\rho_{VI}$ , instantaneous variance of $R$
</div>

```txt
r = risk-free interest rate.
```

From equation (7) the following sensitivity results can be derived [2]: Other factors being constant, the value of a software growth option is higher,

\- The higher the present value of net benefits $V$ ,

• The lower the implementation cost I,

\- The lower $q$ ,

\- The longer the option is held $(t_1, t_2)$ ,

• The higher the variance of $R(\omega^{2})$ ,

• The higher the risk-free interest rate r, and

• The lower the correlation $\rho_{VI}$

The first three results are obvious. The reason for an option value increasing in its exercise period and variance is that in such a case the chance of an increase in value rises, while the downward risk is limited by the possibility of not exercising the option. Because the implementation cost must be paid only when the IS function is activated, it constitutes a risk-free loan that earns a dividend r as long as it is not spent. Furthermore, the greater the correlation between V and I, the less likely it is that V will exceed I in $t_{2}$ and thus the lower the option value.

If there is no effort for implementation preparation, $q$ vanishes and equation (7) is reduced to Margrabe's exchange option [10]:

$$
F _ {M} (V, I, t _ {2}, \sigma^ {2}, \sigma_ {I} ^ {2}, \rho_ {V I}, r) =\tag{8}
$$

$$
V N \left(d _ {1} \left(R \exp^ {r t _ {2}}, t _ {2}\right)\right) - I \exp^ {- r t _ {2}} N \left(d _ {2} \left(R \exp^ {r t _ {2}}, t _ {2}\right)\right).
$$

Dos Santos $[4]^{13}$ proposed this model to quantify the value of the experience and knowhow gained via a first-step pilot project for subsequent projects; that is, in addition to the NPV directly attributable to the pilot project, the value of the option on further projects using the same technology is to be taken into account when deciding whether to undertake the pilot project.

If the implementation cost is also deterministic, the well-known call option model according to Black-Scholes emerges:

$$
F _ {B} (V, F, t _ {2}, r, \sigma^ {2}) =\tag{9}
$$

$$
V N \left(d _ {1} \left(\frac {V}{F \exp^ {- r t _ {2}}}, t _ {2}\right)\right) - F \exp^ {- r t _ {2}} N \left(d _ {2} \left(\frac {V}{F \exp^ {- r t _ {2}}}, t _ {2}\right)\right)
$$

If the implementation cost is deterministic but a deterministic effort for implementation preparation remains, Geske's formula for a compound option [6] is obtained:

(10)

$$
\begin{array}{c} F _ {G} (V, F, E, t _ {1}, t _ {2}, r, \sigma^ {2}) = \\ V B \left(d _ {1} \left(\frac {V}{V ^ {*} \exp^ {- r t _ {1}}}, t _ {1}\right), d _ {1} \left(\frac {V}{F \exp^ {- r t _ {2}}}, t _ {2}\right)\right) \\ F \exp^ {- r t _ {2}} B \left(d _ {2} \left(\frac {V}{V ^ {*} \exp^ {- r t _ {1}}}, t _ {1}\right), d _ {2} \left(\frac {V}{F \exp^ {- r t _ {2}}}, t _ {2}\right)\right) - \\ E \exp^ {- r t _ {1}} N \left(d _ {2} \left(\frac {V}{V ^ {*} \exp^ {- r t _ {1}}}, t _ {1}\right)\right), \end{array}
$$

where $V^{*}$ is the value of V above which the call option should be acquired at $t_{1}$ obtained by solving $F_{B}(V, F, t_{2} - t_{1}, r, \sigma^{2}) - E = 0$ for V, where $F_{B}$ is given by Black-Scholes' formula in equation (9) above.

Let us now apply this model to the option to implement EDI as given as example 4 in the motivating section. We make the following assumptions:

\- The net savings per transaction done via EDI are \$100 and the current usage level is 500 transactions per year. Fixed costs are negligible. Thus, the net benefit/period is \$50,000.

\- The number of EDI transactions rises by 10 percent a year on the average and the percentage change will lie below $0.1 + \sqrt{0.4}$ with a 95 percent probability so that $\sigma^2 = 20$ percent. Besides this basic scenario, alternative calculations for $\sigma^2 = 10$ percent and $\sigma^2 = 30$ percent are done.

\- The time needed for the installation of the base configuration is 1 year $t_1$ . $t_1$ also serves as decision time for the preparation of the implementation. The implementation decision point is year 3 ( $t_2 = 3$ ). Besides, alternative calculations for $t_{2} = 2$ and $t_{2} = 4$ will be done. The risk-free interest rate is 8 percent. The appropriate risk-adjusted rate of return is assumed to be 20 percent, so that, according to equation (6), the current value of the EDI function is $V_{0} = 50,000/(0.2 - 0.1) = \$500,000$ .

\- Estimates for the implementation effort are \$500,000, \$750,000, and \$1,000,000, respectively. For (7) and (10), a cost of 10 percent of $I(F)$ is required if implementation is prepared at $t_1$ . $I_0(F)$ will then be lowered by that amount to allow fair comparison between the various types of software growth options.

\- For equations (7) and (8) we use the same values for $\sigma^2$ and $\sigma^2_I$ and calculate (7) and (8) for correlation coefficients of 0.5, 0, and -0.5 in the case of $t_2 = 2$ , $t_2 = 3$ , and $t_2 = 4$ , respectively.

Table 1 gives a survey of the values of the EDI growth option thus resulting. There, both the values for $I_0(F)$ and the option values are given in percentages of $V_0$ . The overall picture emerging is quite surprising: Even though the implementation of EDI currently is not justified due to a nonpositive expected NPV, up to 71 percent (!) of the discounted sum of net benefits possible due to EDI usage, $^{14}$ that is, $0.71 \times 500,000 = \$355,000$ , can be added to the NPV of net benefits generated by using the base configuration, because it is possible to invoke EDI in period 4 if $V_4 > I_4$ . With regard to the influence of model parameters, the values calculated follow the sensitivity results given above: The later the implementation decision, the higher the volatility, and the lower the implementation cost, the higher the value of a software growth option. In general, only for rather short-lived implementation opportunities in stable environments that are highly unprofitable at the time when the decision of which base configuration to implement is made (e.g., in the case of $t_2 = 2$ , $\sigma^2 = 0.1$ , and $I_0 = 2 V_0$ ), the neglect of software growth options seems justified when calculating the NPV for IS usage.

As can be seen from the first half of Table 1, Margrabe's exchange option generates a higher value for a software growth option than the standard call option. While the values for these two option types are the same if $\rho = 0.5$ , in which case $\omega^2 = \sigma^2$ according to our assumptions, the exchange option turns out to be significantly more valuable, the larger the implementation decision time and the more negative the correlation between $V$ and $I$ . Furthermore, an exchange option's value turns out to be less sensitive to changes in $I_0$ : While the value of a call option drops from 0.51 to 0.31 by 39 percent if $F$ is doubled in the case of $t_2 = 4$ and $\sigma^2 = 0.3$ , the corresponding value of an exchange option only falls by 17 percent (from 0.71 to 0.59) if the implementation cost is negatively correlated with the value of EDI. In this case, \$295,000 can still be added to the passive NPV of the base configuration, even though the current implementation cost has risen from \$500,000 to \$1,000,000. We feel that, in our area of application, situations of the latter type will be common in view of falling implementation costs caused by economies of scale of software development, network economies of scale, or learning effects.

The positive effect of randomness of implementation cost can also be inferred by comparing the values obtained for Geske's and Carr's formulas given in the second half of Table 1. Again, they are the same for $\rho = 0.5$ , but then Carr's formula yields

Table 1. Value of EDI Growth Option

<table><tr><td colspan="10">Black-Scholes&#x27; formula</td></tr><tr><td></td><td colspan="3"> $t_2=2$ </td><td colspan="3"> $t_2=3$ </td><td colspan="3"> $t_2=4$ </td></tr><tr><td> $σ^2/F$ </td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td></tr><tr><td>10%</td><td>0.26</td><td>0.09</td><td>0.03</td><td>0.32</td><td>0.16</td><td>0.08</td><td>0.38</td><td>0.22</td><td>0.13</td></tr><tr><td>20%</td><td>0.31</td><td>0.16</td><td>0.09</td><td>0.39</td><td>0.26</td><td>0.16</td><td>0.45</td><td>0.32</td><td>0.23</td></tr><tr><td>30%</td><td>0.36</td><td>0.22</td><td>0.14</td><td>0.44</td><td>0.31</td><td>0.23</td><td>0.51</td><td>0.39</td><td>0.31</td></tr></table>

Margrabe's formula

<table><tr><td></td><td colspan="3"> $t_{2}=2,\rho=0.5$ </td><td colspan="3"> $t_{2}=3,\rho=0$ </td><td colspan="3"> $t_{2}=4,\rho=-0.5$ </td></tr><tr><td> $\sigma^{2}/I_{0}$ </td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td></tr><tr><td>10%</td><td>0.26</td><td>0.09</td><td>0.03</td><td>0.39</td><td>0.25</td><td>0.16</td><td>0.51</td><td>0.39</td><td>0.31</td></tr><tr><td>20%</td><td>0.31</td><td>0.16</td><td>0.09</td><td>0.49</td><td>0.37</td><td>0.29</td><td>0.63</td><td>0.54</td><td>0.48</td></tr><tr><td>30%</td><td>0.36</td><td>0.22</td><td>0.14</td><td>0.56</td><td>0.46</td><td>0.38</td><td>0.71</td><td>0.64</td><td>0.59</td></tr></table>

Geske's formula, $t_1 = 1$

<table><tr><td></td><td colspan="3"> $t_2=2$ </td><td colspan="3"> $t_2=3$ </td><td colspan="3"> $t_2=4$ </td></tr><tr><td> $σ^2/F$ </td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td></tr><tr><td>10%</td><td>0.22</td><td>0.06</td><td>0.01</td><td>0.28</td><td>0.09</td><td>0.03</td><td>0.33</td><td>0.14</td><td>0.05</td></tr><tr><td>20%</td><td>0.28</td><td>0.12</td><td>0.05</td><td>0.34</td><td>0.18</td><td>0.09</td><td>0.40</td><td>0.23</td><td>0.13</td></tr><tr><td>30%</td><td>0.32</td><td>0.17</td><td>0.09</td><td>0.39</td><td>0.24</td><td>0.14</td><td>0.45</td><td>0.30</td><td>0.20</td></tr></table>

$$
\text { Carr's   formula, } t _ {1} = 1
$$

<table><tr><td></td><td colspan="3"> $t_{2}=2,\ \rho=0.5$ </td><td colspan="3"> $t_{2}=3,\ \rho=0$ </td><td colspan="3"> $t_{2}=4,\ \rho=-0.5$ </td></tr><tr><td> $\sigma^{2}/I_{0}$ </td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td></tr><tr><td>10%</td><td>0.22</td><td>0.06</td><td>0.01</td><td>0.34</td><td>0.18</td><td>0.09</td><td>0.45</td><td>0.30</td><td>0.20</td></tr><tr><td>20%</td><td>0.28</td><td>0.12</td><td>0.05</td><td>0.43</td><td>0.29</td><td>0.20</td><td>0.56</td><td>0.45</td><td>0.36</td></tr><tr><td>30%</td><td>0.32</td><td>0.17</td><td>0.09</td><td>0.50</td><td>0.37</td><td>0.29</td><td>0.64</td><td>0.54</td><td>0.47</td></tr></table>

higher values. In general, the values obtained are lower than those resulting from the respective model without implementation preparation effort owing to the need to spend E earlier. In addition to the values given in Table 1, information regarding the critical values $R^{*}$ and $V^{*}$ is obtained for these models. For instance, if for a compound option $\sigma^{2}=0.1$ and F=\$900,000, an implementation at $t_{2}=4$ should be considered only if the ratio of the value of EDI to the implementation cost is larger than 0.68 in $t_{1}$ . In such a case, the 100,000 preparation effort should be spent. This bound drops to 0.49 in the case of a sequential exchange option with the same parameter values and $\rho=-0.5$ .

The option pricing methods so far presented are based on the assumption that there is only one possible moment, $t_{2}$ , when the IS function under consideration can be invoked. In practice, though, there are often several opportunities to introduce a new IS function. With a six-year planning horizon, for example, there are five chances to implement a cost accounting system module, if the installation of the base configuration takes one year and the application of the cost accounting function can be started only at the beginning of a fiscal year. Furthermore, in that case, the benefit lost by waiting for another opportunity has to be taken into account—that is, after $t_{2}$ , the option becomes American.

As we argued that often only an approximate lower bound is interesting, one approach to this issue is to use equations (7) through (10) as lower bounds for the value of an option with several exercise periods. $^{15}$ The error due to such an approximation is discussed in [20]. The general result of this line of research is that the value of a combined option is the more additive in the values of the options combined, the more dissimilar their type, the more similar their exercise periods and the more dissimilar their exercise price. Moreover, the combined option value is more additive, if the exercise of one option does not preclude that of another. None of these conditions is met in our case. Generally, a software growth option is composed of several exchange options that have very similar exercise prices and different exercise periods and where the exercise of the first option “kills” all following ones; that is, once the IS function at the base of the software growth option is used, it cannot be used again. Thus, a good strategy for obtaining a conservative approximation for the value of a software growth option is to use equations (7) through (10) at the earliest implementation date possible. $^{16}$

## Valuation as a Pseudo-American Exchange Option

Another approach to approximately value a software growth option with several alternative implementation decision points is to assume that the IS function under consideration can be implemented at any time within a given planning horizon T, and to use the approximation via pseudo-American exchange options derived in [2]. A pseudo-American option assumes a constant dividend yield and that option can be exercised at fixed exercise times $t_{1}, t_{2}, \ldots, t_{n}$ within planning horizon T. If the option can be exercised only at T, its value is given as a European exchange option with dividend $\delta$ [2]:

$$
\begin{array}{r l} & F _ {A 1} (V, I, T, \sigma^ {2}, \sigma_ {I} ^ {2}, \rho_ {V I}, r, \delta) = \\ & V \exp^ {- \delta T} N (d _ {1} (R \exp^ {- (\delta - r) T}, T)) - I \exp^ {- r T} N (d _ {2} (R \exp^ {- (\delta - r) T}, T)). \end{array}\tag{11}
$$

If the option can only be exercised at T/2 or T, its value is given as follows [2]:

$$
F _ {A 2} (V, I, T, \sigma^ {2}, \sigma_ {I} ^ {2}, \rho_ {V I}, r, \delta) =\tag{12}
$$

$$
\begin{array}{l} V \exp^ {- \delta T} B (- d _ {1} \left(\frac {R \exp^ {- (\delta - r) T / 2}}{Q ^ {*}}, T / 2\right), d _ {1} (R \exp^ {- (\delta - r) T}, T)) - \\ I \exp^ {r T} B (- d _ {2} \left(\frac {R \exp^ {- (\delta - r) T / 2}}{Q ^ {*}}, T / 2\right), d _ {2} (R \exp^ {- (\delta - r) T}, T)) + \\ V \exp^ {- \delta T / 2} N (d _ {1} \left(\frac {R \exp^ {- (\delta - r) T / 2}}{Q ^ {*}}, T / 2\right)) - \\ I \exp^ {- r T / 2} N (d _ {2} \left(\frac {R \exp^ {- (\delta - r) T / 2}}{Q ^ {*}}, T / 2\right)), \end{array}
$$

where $Q^{*}$ is the value of R above which the exchange option with exercise date T should be acquired at T/2 obtained by solving $F_{AI}(V, I, T/2, \sigma^{2}, \sigma_{I}^{2}, \rho_{VI}, r, \delta) - V + I = 0$ for R, where $F_{AI}$ is given by the European exchange option with dividend formula in equation (11) and the correlation coefficient in $B(. , .)$ is $-\sqrt{0.5}$ .

The expression for an arbitrary number of implementation decision points derived in [2] involves expressions in normal distributions up to the order of n and, thus, is rather difficult to evaluate. However, Carr [2] gives the following approximation for the case $n \rightarrow \infty$ :

$$
F _ {A} \approx F _ {A 1} + \frac {1}{3} \left(F _ {A 2} - F _ {A 1}\right).\tag{13}
$$

Table 2 is a collection of the values so obtained for the approximation via a pseudo-American exchange option for our example with planning horizon T = 6 and $\rho = 0$ . As discussed in the previous section, in that example $\mu = 0.2$ and $\alpha = 0.1$ so that $\delta = 0.1$ , that is, in the first period, $0.1 \times \$500.000 = \$50.000$ can be obtained as the “dividend” for making 100 transactions via EDI, which is lost if one waits with the implementation of EDI until the next implementation decision point. Alternative computations are done for T = 5, $\delta = 0.18$ , $\rho = 0.5$ and T = 7, $\delta = 0.02$ , $\rho = -0.5$ .

When comparing Table 2 with the entries for Margrabe's exchange option in Table 1, we find that the estimate here obtained is lower for higher dividends, but higher if the difference between the risk-adjusted discount rate and average growth rate is small and the planning horizon is long. In addition to this information, the values computed for $Q^{*}$ indicate whether the IS function should be implemented at a particular implementation decision point or not. For instance, if $R$ exceeds 1.09 at $T / 2 = 2.5$ in the case of $T = 5$ , $\delta = 0.18$ , $\rho = 0.5$ and $V_{0} = I_{0}$ , it is better to implement the function to start collecting the dividend than to wait further. Because of the lower dividend, longer exercise time, and higher correlation, this bound increases to 4.16 if $T = 7$ , $\delta = 0.02$ , $\rho = -0.5$ for the decision point $T / 2 = 3.5$ .

## The Value of IS Flexibility

Typically, an IS platform will embed several software growth options: In example 4 of the motivating section, SAP R/3 provides for the flexible implementation of EDI, workflow management, and document retrieval and archiving. If the exercise of one software growth option does not influence the value of the other software growth options embedded, the value of IS flexibility as defined in the second term of equation (3) can be calculated as the sum of the values of the individual software growth options. An example of the violation of this property is a cost accounting system needing as its basis a bookkeeping system, where the latter is not implemented as a part of the base configuration but forms a software growth option of its own. If the aim is to find a conservative approximation for the value of IS flexibility, we propose to neglect software growth options that depend on the prior implementation of IS functions also forming a software growth option and to deal only with independent software growth options.

Table 2. Value of EDI Growth Option as a Pseudo-American Exchange Option

<table><tr><td></td><td colspan="3"> $T = 5, \delta = 0.18, \rho = 0.5$ </td><td colspan="3"> $T = 6, \delta = 0.1, \rho = 0$ </td><td colspan="3"> $T = 7, \delta = 0.02, \rho = -0.5$ </td></tr><tr><td> $\sigma^{2}/I_{0}$ </td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td><td>100%</td><td>150%</td><td>200%</td></tr><tr><td>10%</td><td>0.06</td><td>0.02</td><td>0.01</td><td>0.11</td><td>0.07</td><td>0.04</td><td>0.15</td><td>0.10</td><td>0.08</td></tr><tr><td>20%</td><td>0.15</td><td>0.09</td><td>0.06</td><td>0.31</td><td>0.25</td><td>0.22</td><td>0.53</td><td>0.48</td><td>0.44</td></tr><tr><td>30%</td><td>0.54</td><td>0.46</td><td>0.41</td><td>0.66</td><td>0.61</td><td>0.57</td><td>0.73</td><td>0.70</td><td>0.66</td></tr></table>

In fact, we feel that within a reasonable planning horizon such “second-order interactions” are seldom, as the basic IS functions will all be implemented as a part of the base configuration and the time horizon for the implementation of IS functions, which depend on IS functions forming a software growth option, usually lies outside the usual planning horizon of, say, ten years. Furthermore, reliable estimates for the parameters in equation (5) for IS functions, whose practical relevance lies several years ahead and whose implications for improving business processes currently are not well understood, seem very hard to obtain.

A theoretical rationale for our approach is the “diminishing marginal option effect” described by Trigeorgis [19], who states that the additional value of another embedded option decreases with the number of options present, so that “although a few particular options may have been neglected . . . the valuation as it is may still represent a close approximation to the true value, especially if the options that were included were selected so as to minimize their overlapping.”

Implications of Software Growth Options for IS Investment Decisions

## Selecting a Strategic IS Platform

THE NPV RULE STATES THAT AN IS PROJECT THAT YIELDS a negative NPV should not be undertaken. According to equation (3), a negative “passive” NPV can be outweighed by the value of the options embedded. Furthermore, the addition of the second term in equation (3) can change the ranking obtained via the “passive” NPVs when comparing alternative IS platforms.

Dos Santos [4] points out that one reason why an IS project with negative passive NPV should be pursued is to gain experience. The models presented indicate that there are other classes of IS projects with substantial option values too. In particular, the evaluation of software growth options is important for investments in novel IS platforms as, according to Buss [1], for such IS projects “the intangible benefits can be more important than the tangible ones. This is particularly true, for example, in the case of information processing software projects such as the conversion of operating systems, the design of data networks, and the creation of databases for multiple applications.”

An example of this type of IS project is the SAP R/2–R/3 decision described in example 4 of the motivating section, where the new platform offers opportunities for implementing EDI, workflow management, and document retrieval and archiving. To illustrate the importance of software growth options for such decisions, let us assume that the extension of the base configuration by these IS functions can be described by an exchange option where, for EDI, the assumptions made above with $t_{2}=4$ and $\rho=-0.5,\sigma^{2}=20$ percent, and $I_{0}=\1.000.000$ hold, for workflow management $t_{2}=4,N_{0}=100,p-c=\200,\alpha=15$ percent, $V_{0}=20,000/(0.2-0.15)=\400,000,\sigma^{2}=30$ percent, $\rho=-0.5$ and $I_{0}=\600,000$ , and for document retrieval and archiving $t_{2}=3,N_{0}=1,000,p-c=\100,\alpha=10$ percent, $V_{0}=100,000/(0.2-0.1)=\1.000,000,\sigma^{2}=10$ percent, $\rho=0$ , and $I_{0}=1,5V_{0}$ . In that case, the implementation of SAP R/3 can cost up to $0.48\times500,000+0.64\times400,000+0.25\times1.000,000=\746,000$ more than continuing to use SAP R/2 (see Table 1 for the respective option values).

## Justifying Strategic IS Investments

The importance of software growth options for strategic information systems $[12]$ is shown by the fact that, typically, the rationale of such systems is “the eroding status quo,” that is, in the current business environment they are not economically justified, but if the conditions change, for example, due to deregulation or the entrance of new competitors, they can bring many benefits. As, for example, Kester $[9]$ points out, in such situations it is important to act early, as the value of growth options can significantly decline the more obvious their value becomes to competitors who then may decide to exercise the option themselves and, thus, lower the option’s value. Hence, valuable opportunities are lost if the second term in equation $(3)$ is undervalued or neglected. Given the increasing volatility of the business environment and the strong dependence of the value of software growth options on the variance, considerations like those described here are of increasing importance for IS management.

## Another Argument in Support of General Standard Software

Another IS investment where software growth options play an important role is the decision to use either general standard software or software specifically designed for an industry. Often, the effort for implementing a general standard software package such as SAP R/3 will be greater than that for software designed for customized industry. A more general platform, however, will usually contain more software growth options, since it is based on the requirements and knowhow of a much wider user base. For instance, the IS functions mentioned in examples 1 to 3 in the motivating section may be present in a general standard software solution but not in software tailored to an industry's particular interests (examples 2 and 3) or in software developed to cover business transactions in the home country only (example 1). Valued via the methods described here, such software growth options will increase the “strategic” NPV of the general standard software alternative and can make it the platform selected even if its passive NPV is lower.

Assume, for instance, that both a general standard software solution's base configuration and software designed for business in the home country only meet the requirements to cover the current business processes (see example 1 of the motivating section). Because of a greater effort for parameterization, the cost for implementing the general standard software is \$1,000,000, -, while for the second type of software mentioned, that does not cover business with foreign countries, it amounts to \$900,000, -. If the number of transactions with foreign business partners is assumed to grow from 200 by 15 percent a year with $\sigma^{2}=30$ percent and $p-c=\$100$ , the current value of this IS function is given by $V_{0}=200,000/(0.2-0.15)=\$400,000$ . If the IS function is to be activated in two years, if the cost of a detailed analysis of the relevant business processes in question, of activating the appropriate parameters and of training the users concerned is \$360,000, and \$40,000 constitute the preparation effort in period 1, it is advisable to choose the more general platform since, in that case, the value of the software growth option is \$0.32 × 400,000 = \$128,000 (see Table 1, Geske's formula for $t_{1}=1$ , $t_{2}=2$ , $\sigma^{2}=30$ percent, $F=V_{0}$ ). This example shows that the implementation of general standard software can be economically indicated even if adopting the base configuration to meet the same requirements is more expensive than using an alternative with a lesser number of functions.

## Software Engineering for Adaptability

When IS users start to use equation (3) to evaluate IS platforms, IS vendors must also consider the possibilities of obtaining the highest possible value for the software growth options embedded in their systems. This clearly means abandoning programming according to customers' specifications and instead offering adaptable standard software packages. The design of such systems must take into account the findings described here: There must be a chance for the IS functions implemented as software growth options to be used in the near future (i.e., $N_{t}$ will grow fast, p is sufficiently high and c sufficiently low), and their implementation must be easy (i.e., $I_{0}(F)$ and E must be low). To support the process of selecting IS functions that can offer software growth options, it is paramount to keep in close contact with the users and to observe new developments, as “adaptivity is not a generic quality of a software system as a whole: Software systems are adaptable in specific, designated ways, if at all. Therefore, the adaptability must not only be explicitly engineered into the software, it must be engineered into the software in places where it will do the most good to the business” [5].

## Conclusions

WE HAVE PROPOSED THE USE OF OPTION PRICING FORMULAS to obtain an estimate for the value of flexibility of an IS platform. After describing an abstract version of the process of IS enhancement, we discussed the various assumptions of the option pricing models and the limitations of the real options approach in the context of IS investments. Then we introduced option pricing formulas for the valuation of various types of software growth options and studied the dependence of the value of a software growth option on parameters describing the IS platform and the business development.

Finally, we dealt with the implications of software growth options for investments in IS platforms, strategic information systems, and software engineering.

Further empirical work will be required to gain more insight into the various assumptions made and into their validity: For example, which are suitable stochastic processes for modeling the development of the net benefits obtained from IS usage? What kinds of risk arise and what hedging strategies are feasible? With regard to theoretical work, a closer study of the combination of decision analysis and option pricing described in $[17]$ and the development of models for the mixture of European and American exchange options would be interesting in our application context.

## NOTES

1. The net benefit could be the difference between savings in inventory, transportation, and document-handling cost and the cost of an electronic procedure. Estimating the benefit of EDI is addressed in more detail later.

2. According to the Capital Asset Pricing Model (CAPM), investors demand a risk premium for risky projects. The CAPM postulates that this risk premium is determined by the investment's systematic risk, measured by its volatility relative to the market times the expected market risk premium given by the difference between the expected return from the market portfolio and the risk-free interest rate. For the example in this paper, a risk premium of 2 percent is assumed, so that the appropriate discount rate is 10 percent (8 percent + 2 percent). For further details, see, e.g., [21, p. 40 ff.].

3. See, e.g., [8] for the valuation of options embedded in investments for oil search and refinery, and [3] for the treatment of flexibilities in the operation of oil tankers and copper mines.

4. See, e.g., [14] for the application of real option models for valuing R&D projects in electronics, [13] for the use of real options in justifying R&D projects in pharmaceutics, and [15] for the use of real options to estimate the value of options embedded in the possession of real estate from observed land prices.

5. In our fourth example, for instance, we identified EDI, work-flow management, and document retrieval and archiving as software growth options present in R/3 but not in R/2.

6. The case of an IS function present in the base configuration that can be changed to another IS function is also covered by this model; in such a case the implementation cost can be seen as the sum of the (deterministic) implementation effort and the (stochastic) value of the IS function of the base configuration to be exchanged.

7. This is consistent with using a risk-adjusted discount rate in an expected NPV calculation, as in equation (2).

8. However, this can also present a problem for financial options, as the stochastic process for $V$ often is nonstationary.

9. As is demonstrated in the following sections, only an estimate for $\sigma^{2}$ will be required. However, an estimate for $\alpha$ is needed to estimate $\sigma^{2}$ . Another method for estimating $\sigma^{2}$ for real options is described in [13], where the observed volatility of biotechnology stocks is used as a proxy measure for the volatility of R&D projects in pharmaceuticals.

10. Using (naive) decision tree analysis with a constant discount rate for option valuation is not appropriate, as the risk of an option changes over time and with changing values of the underlying asset (see, e.g., [8]).

11. See, e.g., [14] for a similar argument in the case of R&D projects in electronics.

12. An American type of option can be exercised at any time during its exercise period, while a European one only allows this at the end of the exercise period.

13. Contrary to Dos Santos, we assume that the money needed for the implementation in $t_{2}$ can be invested in a risk-free way to earn a dividend r in order to be able to make a fair comparison between the different option models presented.

14. This happens in the case of Margrabe's exchange option for parameter values $V_0 = I_0$ , $t_2 = 4$ , $\sigma^2 = 30$ percent and $\rho = -0.5$ .

as in the case of financial options. Kemna [8] advocates using the shortest possible exercise period; otherwise competitors could obtain the same option, enter the market, and, thus, lower the option's value.

## REFERENCES

1. Buss, M.D.J. How to rank computer projects. Harvard Business Review (January–February 1983), 118–125.

2. Carr P. The valuation of sequential exchange opportunities. Journal of Finance, 18, 5 (December 1988), 1235–1256.

3. Dixit, A.K., and Pindyck, R.S. Investment Under Uncertainty. Princeton, NJ: Princeton University Press, 1994.

4. Dos Santos, B.L. Justifying investments in new information technologies. Journal of Management Information Systems, 7, 4 (Spring 1991), 71–90.

5. Fayad, M., and Cline, M.P. Aspects of software adaptability. Communications of the ACM, 39, 10 (October 1996), 58–59.

6. Geske, R. The valuation of compound options. Journal of Financial Economics, 7 (1979), 63–81.

7. Geske, R., and Shastri, K. Valuation by approximation: a comparison of alternative option valuation techniques. Journal of Financial and Quantitative Analysis, 20, 1 (1985), 45–71.

8. Kemna, A.G.Z. Case studies on real options. Financial Management (Autumn 1993), 259–270.

9. Kester W.C. Today's options for tomorrow's growth. Harvard Business Review (March–April 1984), 153–161.

10. Margrabe W. The value of an option to exchange one asset for another. Journal of Finance, 33, 1 (March 1978), 177–186.

11. Mukhopadhyay, T.; Kekre, S.; and Kalathur, S. Business value of information technology: a study of electronic data interchange. MIS Quarterly (June 1995), 137–156.

12. Neumann, D. Strategic Information Systems. New York: Macmillan, 1994.

13. Nichols, N.A. The new pharmaceutical paradigm. Harvard Business Review, 72, 1 (1994), 89–105.

14. Pennings, E., and Lint, O. The option value of advanced R&D. European Journal of Operational Research, 103 (1997), 83–94.

15. Quigg, L. Empirical testing of real option-pricing models. Journal of Finance, 48, 2 (June 1993), 621–640.

16. Sick, G. Capital Budgeting with Real Options. Monograph Series in Finance and Economics. New York: Stern School of Business, New York University, Monograph 1989–3.

17. Smith, J.E., and Nau, R.F. Valuing risky projects: option pricing theory and decision analysis. Management Science, 41, 5 (May 1995), 795–816.

18. Tam, K.Y. Capital budgeting in information systems development. Information and Management, 23, 6 (December 1992), 345–357.

19. Trigeorgis, L. The nature of option interactions and the valuation of investments with multiple real options. Journal of Financial and Quantitative Analysis, 28, 1 (March 1993), 1–20.

20. Trigeorgis, L. Real options: an overview. In L. Trigeorgis (ed.), Real Options in Capital Investment—Models, Strategies and Applications. Westport, CT: Praeger, 1995, pp. 1–28.

21. Trigeorgis, L. Real Options—Managerial Flexibility and Strategy in Resource Allocation. Cambridge, MA: MIT Press, 1996.
