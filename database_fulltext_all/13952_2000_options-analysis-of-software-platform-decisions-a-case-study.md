---
otero_id: 13952
otero_key: "J74E2F5A"
title: "Options Analysis of Software Platform Decisions:  A Case Study"
authors: "Alfred Taudes; Markus Feurstein; and; Mild"
year: "2000"
journal: "MIS Quarterly"
doi: "10.2307/3250937"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# OPTIONS ANALYSIS OF SOFTWARE PLATFORM DECISIONS: A CASE STUDY<sup>1</sup>

By: Alfred Taudes Department of Production Management Vienna University of Economics and Business Administration Pappenheimgasse 35/5 A-1200 Vienna AUSTRIA alfred.taudes@wu-wien.ac.at

Markus Feurstein<sup>2</sup> Department of Production Management Vienna University of Economics and Business Administration Pappenheimgasse 35/5 A-1200 Vienna AUSTRIA markus.feurstein@wu-wien.ac.at

Andreas Mild Department of Production Management Vienna University of Economics and Business Administration Pappenheimgasse 35/5 A-1200 Vienna AUSTRIA andreas.mild@wu-wien.ac.at

## Abstract

In recent years, the use of option pricing models to support IT investment decisions has been proposed in the MIS literature. In this paper, we discuss the practical advantages of such techniques for the selection of a software platform. First, we argue that traditional quantitative approaches to a cost-benefit analysis give only a partial picture of such decision situations: due to the long planning horizon required because of the time-consuming and resource-intensive implementation process, it is not possible to exactly predict which applications will, in fact, run on the system over time. Thus, the investor is faced with the problem of valuing “implementation opportunities.” We then compare different valuation techniques for this task and discuss their respective advantages and drawbacks. The practical advantages of employing such models are demonstrated by describing a real-life case study where option pricing models were used for deciding whether to continue employing SAP R/2 or to switch to SAP R/3.

Keywords: Software platform, strategic IS management, real options, cost-benefit analysis, SAP R/3, IS investment

ISRL Categories: EI0106, EF07

## Introduction

A software platform is a software package that enables the realization of application systems.

Examples of software platforms are operating systems, database systems, CASE environments, workflow/workgroup systems and general-purpose, customizable application packages such as SAP R/3 or ORACLE. Together with the hardware and the organizational knowledge about planning, designing, and operating application systems, the software platforms in use constitute a firm’s information technology infrastructure.

For the purpose of valuation, one should view a software platform as a bundle of functions that can serve as the basis of certain applications whose value changes over time. While this bundle of enabling functions cannot be adjusted in the short run, one can decide on the basket of applications to be developed, implemented, and operated on the basis of the respective costs and benefits then observed (see Weill 1993). In other words, software platforms do not directly generate value but they enable different value-generating applications to be implemented. The value of a software platform thus depends on the applications that can be implemented, i.e., its value mostly lies in the options it creates to build applications. Therefore, the valuation of software platforms is a more difficult task than the valuation of applications. It is important to view the enabling technologies—the platform and applications—separately: one platform can enable several applications, while one application may necessitate several platforms. Clearly, the broader the range of possible application portfolios, the more flexible the software platform. However, here one is confronted with irreversibility: the development and implementation costs are usually sunk in the sense that software development expenditures, license fees, or expenditures for external consulting services cannot be retrieved when the environment changes and applications can no longer be used without alterations. Timing the implementation of each application must therefore be well considered.

Approximately 35% to 40% of the total IT investment is dedicated to IT infrastructure (Weil 1993). Given this impact on a CIO’s budget and the far-reaching consequences of an incorrect platform decision, it is natural to ask what methods for determining the value of IT infrastructure are used in practice and how satisfied practitioners are with such approaches. Weill investigates these questions by examining the justification rationales used by the chief information officers for IT infrastructure investments in five large, profit-seeking firms mostly acting in the financial services sector. He finds that traditional methods of capital budgeting, such as the discounted cash flow/net present value (NPV) method, are not used. Similarly, Tam (1992) finds that IT practitioners have problems when determining model parameters, such as the time series of costs and revenues of an IS project, or the appropriate discount rate for the NPV model. Consequently, simple, static models are often preferred to the NPV model, and important project decisions are based rather on intuition, experience, and rule of thumb than on quantitative analysis (Tam 1992). There are two major reasons why NPV is not used in IT practice. First, managers intuitively think in terms of opportunities (options) (see Busby and Pitts 1997). However, options are not captured by the NPV analysis. Second, it is hard to find correct model parameters. Hence, it is rational not to invest much time in finding quantitative arguments for a model that is known to be wrong from the start. Parameter estimation for option analysis is even more involved than for NPV. However, option analysis captures and formalizes the managers’ intuition and thus it creates a disciplined decision making process (Amram et al. 1999).

The NPV method would be appropriate for valuing a particular application that is to remain unchanged over a given period of time; however, it is not clear how to deal with flexibility regarding the time to implement an application or to stop using or modifying it. One way to “save” the traditional NPV is to fix in advance a particular implementation policy and to calculate the expected NPV for the resulting application portfolio, i.e., to explicitly renounce flexibility. Some firms in Weill’s survey pursued such a strategy: in such firms “the IT department identifies a basket of business process applications that will aggregate enough benefits to justify the infrastructure investment.” Similarly, Hochstrasser (1994) states that the use of standard evaluation procedures for infrastructure is impossible due to the fact that applications for the new platform are still in early planning stages. Therefore, a medium-term business scenario of three to five years should be evaluated and IT infrastructure should be designed for supporting this scenario. Clearly, such an approach is satisfactory in a stable environment, but it can be quite misleading in an uncertain environment characterized by a high upward potential and a downward risk that is limited by the possibility of corrective actions (i.e., the refusal of implementation, stoping use, or software change). Due to this ability to react, the traditional expected NPV is a lower bound of the value of an application. In fact, even the possibility to implement an application whose current expected NPV is negative will have a positive value, because one can wait and face the implementation cost later on when the application’s value is positive.

Rules of thumb, such as “invest to keep up with the technology” or “invest if the competitors have been successful,” which also might be used to justify software platforms (Weill 1993), do not provide the decision maker with information about the impact of his decision on the firm’s value and, rather than yielding the best decision for the firm, they can be easily manipulated so as to accommodate personal or departmental goals. Also, treating “flexibility” as an “intangible benefit” to be measured on a rank scale via cost-benefit analysis as suggested by Buss (1983) does not provide the basis for maximizing the firm’s value. Furthermore, when applying cost-benefit analysis, one is confronted with a number of problematic, implicitly made assumptions such as full substitutability of criteria and uniform ordinal scales. Additionally, there is plenty of room for political processes as the scores and weights of the single criteria must be found subjectively.

A recent stream of research advocates preserving the quantitative approach for valuing investments incorporating flexibility and is based on real options (for a survey of the relevant literature, see Trigeorgis 1995). Trigeorgis (1996) states that the failure of the traditional NPV model derives mainly from ignoring the value of active management in adapting to changing market conditions and proposes to expand the traditional NPV by a value of options from active management or by simply attributing an option value to value projects where opportunities for adaptation to a changing environment exist:

## Expanded NPV =

(1)

ordinary NPV of expected cash flows + value of options from active management

The prerequisite for this new development in capital budgeting is the option-like characteristic of flexibility in real assets. Consider, for instance, a European call option: it offers its holder the right, but not the obligation, to buy at maturity the underlying share of stock for a specified strike price (see Copeland, Weston 1992, p. 240 ff.). Similarly, an application that can be implemented on a specific software platform offers the firm the opportunity (but not the obligation) to obtain the benefits of the application (underlying asset) by investing a given implementation cost (strike price) at certain implementation decision points (maturity).

This paper aims at developing real option models in such a way that they become part of the managerial practice when making software platform decisions. Its main contribution is the description of a real-life case study that demonstrates the usage of option valuation methods for deciding between a further usage of SAP R/2 and the introduction of SAP R/3. Regarding the organization of the paper, we start by giving an overview of prior research on option valuation in IT. We then describe the methodology of option valuation of implementation opportunities where we examine the NPV method in opposition to two different option valuation techniques. The above-mentioned case study is presented in the fourth section. In the concluding sections, we summarize the present work and describe its implications for the MIS practice and research.

## Previous Work on Option Valuation in IT

A number of researchers have written on the use of option models in IT investment decision making. The pioneering work of DosSantos (1991) employs Margrabe’s exchange option model (Margrabe 1978) for valuing an IS project that uses a novel technology for testing. He argues that such a project, in case it turns out helpful—if it increases the NPV of future projects due to learning and experience—generates the option to use the new technique. Similarly, Kambil et al. (1993) use the Cox-Rubinstein (Cox and Rubinstein 1979) binomial option pricing model to determine whether or not a pilot project should be undertaken. As a real-world case, they study the improvement of business processes via hand-held computers in a large profit-seeking city hospital. They demonstrate that, while an NPV-based analysis of the whole project would suggest abandoning the idea, the option value of a smaller pilot project exceeds its cost so that it should be undertaken.

Both works consider dependencies between a pilot project and a follow-up project. For a software platform, several options usually are relevant; additional investments to keep options alive and several alternative implementation dates for applications are possible. In analogy to Kester’s (1984) “growth options” for firms (Kester 1984), Taudes (1998) investigates option models for evaluating “software growth options,” which are formed by IS functions present in a software system that can be used in applications brought into operation at certain implementation decision points when found beneficial. This work lays the foundation for valuing software platforms. However, Taudes does not differentiate between IS functions and value generating applications and no real world case is provided.

Sullivan et al. (1997) and Chalasani et al. (1998) argue that option models can provide a firmer foundation for software development decisionmaking heuristics. Using real options, they study the decision of whether software should be restructured to make it more flexible via information hiding (Sullivan et al. 1997) and to motivate software prototyping (Chalsani et al. 1998).

Benaroch and Kauffman (1999) investigate the problem of investment timing using the Black-Scholes and Cox-Rubinstein models in a realworld case study dealing with the development of point-of-sale(POS) debit services by the Yankee 24 shared electronic banking network of New England. In such situations, the question is not whether an investment should be undertaken or which out of several alternatives should be chosen, but when to exercise the option held, i.e., when to implement a particular IT solution. This necessitates a trade-off between the revenue lost by waiting and the possibility of a further increase in the system’s value. Benaroch and Kauffman motivate the usage of option pricing methods whether the underlying asset is traded or not by arguing that the market will correct under-investing due to an incorrect discounting rate with potential takeovers of the firm. In a follow-up paper, Benaroch and Kauffman (2000) state that the effect of an underlying asset that is not traded can be captured by introducing a convenience yield into the Black-Scholes formula (Trigeorgis 1996, p. 101). The convenience yield decreases the option value of an investment opportunity due to a project’s idiosyncratic risk. This factor is hard to measure. However, Benaroch and Kauffman (2000) show in a sensitivity analysis that, in their case the optimal timing did not depend on the particular value chosen for this parameter. Therefore, it seems to be appropriate to apply the Black-Scholes valuation for IS investment opportunities.

## Option Valuation of Implementation Opportunities

The most important type of flexibility offered by a software platform is the ability to decide whether or not to implement an application in the future. We, therefore, study the valuation of “implementation opportunities” using a specialized version of (1) that considers the value of a software platform to be given as:

NPV of fixed application portfolio +

(2)

option value of implementation opportunities

As a first step toward option valuation, one has to develop a quantitative model that describes the development of the value of the underlying asset over time. In our case, the value of the underlying asset of an implementation opportunity is the stream of future benefits that can be obtained by using the application under consideration. A number of different types of benefits of IT have been identified. The most common type of benefit is the decrease of the cost for executing a particular set of business processes either directly or by increasing productivity (see Hochstrasser 1994). A simple model of this effect is

$$
P _ {t} = N _ {t}. b\tag{3}
$$

$P _ { t } | \mathsf { s }$ the benefit of the application at time $t . N _ { t }$ is the number of times the activities, supported by the application, are performed at time t and b denotes the savings in process cost obtained when the application under study is implemented. Empirical support for such a model is provided in Mukhopadhyay et al. (1995), who study the benefits obtained at Chrysler by introducing EDI-based purchasing. They found that such an application saves time normally used for clerical work, such as document handling, and leads to cost savings in logistics. Furthermore, it turned out that the benefits/transaction as compared to a manual transaction are more or less fixed so that the tota benefit is proportional to EDI penetration. When (3) is applied in such a case, $N _ { t }$ represents the number of supportable external transactions and is largely determined by the number of business partners that adopt a compatible technology. In the case of applications that support internal transactions, $N _ { t }$ will mostly depend on the development of the firm’s sales.

Turning to the process of actively managing the application portfolio, we assume that IT management determines the benefit of an application under consideration for implementation at the software platform being valued at a certain “implementation decision point” T and decides to implement the application under review when its value $V _ { T } ,$ defined as the current value of expected future benefits $P _ { t } , \ t \ > \ T ,$ exceeds the total cost of ownership I. We thus assume that implementation opportunities correspond to European options. One could also assume that $V _ { t }$ is continuously observed and that the application can be implemented anytime. This would lead to the valuation of American options, which are much harder to evaluate than European options. We feel that our formulation is more natural as the determination of benefits can involve considerable cost, and frequently applications can be implemented only at certain times, e.g., at the beginning of a fiscal year. The total cost of ownership I includes the cost of the implementation and the discounted sum of the operating cost. Typically, this will comprise the costs of software development and customizing, additional hardware, user training, organizational changes, coordination with business partners, telecommunication, license fees, support personnel, etc. If there is no uncertainty regarding the development of $P _ { t } ,$ one can determine at $t = 0$ $V _ { T }$ as the sum of $P _ { t } , t > \tau$ discounted by the riskless interest rate and then decide whether the application should be part of the application portfolio at time T. So, the benefit for the platform at time $t = 0$ is given by the difference between $V _ { T }$ and I discounted at the risk-free rate. This changes when the development of $P _ { t }$ cannot be predicted with certainty: in that case, one prefers to let the insecure future unfold and to postpone the implementation decision until T. Nevertheless, in order to decide upon the platform, one still needs to know the value of these future opportunities (options) at $t = 0$

The above problem can be subdivided in building a model describing the development of the value of the uncertain cash flow $V _ { T }$ and a method for valuing the implementation opportunity. In the option pricing literature, it is customary to assume that $V _ { t }$ follows a geometric Brownian motion, i.e., $d V _ { t } = V _ { t }$ (?dt + cdW), where ? is the growth rate, c the variance parameter, and dW the increment of a Wiener process (the continuous analog of serially uncorrelated normally distributed random variables with zero mean and unit standard deviation). In our context, this arises if $N _ { t }$ follows a geometric Brownian motion, b being constant. This implies that $P _ { t }$ and $V _ { t }$ follow a geometric Brownian motion, too. ? represents the rate at which the usage per period grows and c is the standard deviation of the normally distributed percentage change of $N _ { t } .$ A straightforward estimator for this parameter can so be based on the symmetry of the normal distribution and on the fact that 95% of the probability mass of a normally distributed random variable is within the 2c range.

In our context, empirical support for the assumption of a geometric Brownian motion is provided by the fact that implementation opportunities typically involve applications that are based on novel software techniques whose adoption is uncertain and/or that are designed to support new fields of business for the organization. In both cases, $N _ { t }$ is governed by a product diffusion process. A number of empirical studies show that until saturation a geometric Brownian motion is a good descriptor of this phenomenon (see Mahajan et al. [1993] for a survey; see Pfeiffer [1992] for modeling the diffusion of EDI). Note that, even though the geometric Brownian motion is a continuous-time model, it is not necessary to continuously measure the potential benefits of implementation opportunities. Rather, this has to be done only when deciding to implement the application under study. One can imagine that there are always events influencing $N _ { t } .$

Next, we value the implementation opportunity. Choosing a method implicitly determines assumptions regarding the time when the decision is made and how risk is priced. Here we will develop an NPV analysis and two option valuation methods for IT investment decisions. The NPV analysis will serve as a benchmark. The NPV method assumes that the decision to implement an application at time T is made at time $t = 0$ regardless of the value of the application at T. As far as risk is concerned, the NPV method uses a discount rate $\mu$ that equals the equilibrium expected rate of return on securities equivalent in risk to the project being valued. Usually, the Capital Asset Pricing Mode (CAPM) is employed to determine $\mu$ as the sum of the riskless interest rate r and a risk premium given as the market price of risk, i.e., the difference between the return of the market portfolio and $r ,$ and the correlation of the cash flow stream with the market portfolio (the project’s systematic risk “beta”). In our case, when employing the NPV paradigm, one could calculate the NPV of an application that can be implemented at T and decide whether it should be included in the application portfolio or permanently excluded depending on whether

$$
\begin{array}{l} N P V _ {1} = e ^ {(- \mu . T)} \cdot (E (V _ {t}) - I) > 0 \\ N P V _ {1} = e ^ {(- \mu . T)} \cdot (V _ {0} \cdot e ^ {(\alpha . T)} - I) \\ V _ {0} = N _ {0} \cdot b / (\mu - \alpha) \end{array}\tag{4}
$$

Keeping this decision open until T generates an implementation opportunity. Methods taking such opportunities (options) into account are based on decision trees. Since a rational decision maker wil not implement an application that has a negative value at time $\bar { T } \ ( \mathsf { i . e . } , \ V _ { \tau } - \ I < 0 )$ , the negative branches in the decision tree must be pruned. A generalization of NPV leads to a decision treebased NPV model $N P V _ { z } ,$ , i.e.,

$$
N P V _ {2} = e ^ {(- \mu . T)}. E (\max [ V _ {T} - I, 0 ])\tag{5}
$$

On the basis of some algebra, one finds (see the appendix) that:

$$
\begin{array}{l} N P V _ {2} = e ^ {- \mu . T}. (V _ {0}. e ^ {\alpha T}. N (d _ {1}) - I. N (d _ {2})) \\ d _ {1} = \frac {1}{\sigma \sqrt {T}} \left(\ln \left(\frac {V _ {0}}{I}\right) + \left(\alpha + \frac {1}{2} \sigma^ {2}\right). T\right) \\ d _ {2} = d _ {1} - \sigma \sqrt {T} \end{array}\tag{6}
$$

where N(.) denotes the cumulative standard normal distribution function. Clearly, the value of the extended NPV will always exceed the ordinary NPV, since we have introduced the possibility not to invest in the project after observing the state of the world at time $T .$ This difference will increase with increasing variance. Thus, while the value of the underlying asset will decrease with growing systematic risk, the value of the corresponding option increases with augmenting uncertainty. The problem with this approach is that $\mu \mathrm { i n }$ (6) has to be different from that in (4), as the correlation of $V _ { t }$ with the market portfolio differs from the correlation of ma $\varsigma [ V _ { T } - I , O I$ . In fact, if $V _ { t }$ has a constant $\mu ,$ the expected rate of return for ma $\langle \boldsymbol { N } _ { \tau } - \boldsymbol { I } , \boldsymbol { O } \boldsymbol { J }$ will not be constant, but rather it will fluctuate with movements of $V _ { t }$ and time, among other factors (see Trigeorgis 1996, p. 391).

An alternative approach that avoids such complications is based on the assumption that perfect financial markets are arbitrage-free in the sense that no investor can make a profit without taking some risk or expending some capital. Such gains could be made if an option were priced differently than a portfolio consisting of the underlying asset and a riskless security with the amounts being continuously adjusted so that the value of the portfolio replicates the value of the option. This consideration can be made the starting point of valuing max $\langle N _ { \tau } - I , O I$ and results in the Black-Scholes formula (Black and Scholes 1973):

$$
B S = V _ {0} N (d _ {1}) - I e ^ {- r T} N (d _ {2})\tag{7}
$$

where

$$
\boldsymbol {d} _ {1} = \frac {1}{\sigma \sqrt {T}} \left(\ln \left(\frac {V _ {0}}{I}\right) + \left(r + \frac {1}{2} \sigma^ {2}\right). T\right)
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

Although structurally quite similar to $N P V _ { z } ,$ BS contains fewer parameters that are easier to determine, i.e., ? is absent and instead of W there appears the riskless interest rate r. However, in our case, the underlying asset is not traded. To be able to use (7), one thus assumes that a “twin security” exists as a continuously adjusted portfolio of traded securities that perfectly replicates $V _ { t } .$ This is not unproblematic, as IT projects often also show idiosyncratic risks such as the technical risk regarding the feasibility of the enabling technology in the proposed area of application or an organizational risk in that the organizational changes required cannot be achieved due to resistance by the staff. It is implausible that such risks are priced by the financial market.

In fact, the Black-Scholes serves as a lower bound if several alternative implementation decision points T are possible. In that case, the implementation opportunity resembles an European call option with several exercise periods. Trigeorgis (1993) uses numeric methods to determine the value of such “compound options” and finds that the error made by using (7) with the earliest implementation decision time is small as the different options compounded are very similar and all further options are killed once an option is exercised.

Thus, it can be seen that both (6) and (7) have deficiencies in our area of application. We, therefore, suggest using both methods to increase the reliability of the valuation procedure.

## Case Study: Continuing with R/2 or Switching to R/3

Models (4) through (7) have been applied in a reallife software platform decision. The project was carried out at a central European company manufacturing auto parts and arms with about 1,500 persons employed in several facilities. The core competence of this firm is the production of specialized parts in small lot sizes so that priority is given to cost control rather than to the development of new products. Consequently, the management style is top-down, the organizational structure hierarchical. The company is a long-term SAP R/2 user on a traditional mainframe with mostly terminals and a few PCs connected. The modules in use covered book-keeping, costaccounting, materials management, and production planning and control. The firm’s problem was to decide whether the R/2 platform should be upgraded and used in coming years or whether it should be abandoned in favor of R/3. At the beginning of the decision-making process, the different stakeholders were in total disagreement: the users were satisfied with the functionality of the current system and did not wish a risky and time-consuming transition, especially as the company was forced to undergo severe cost-cutting measures. The IT department, on the other hand, argued that SAP R/3 was the technologically superior platform that would allow them to better meet future demands. The CFO wished the advantages that would possibly be gained to be quantified. He was unable to assess the value of having a “technologically better” software platform and was afraid that IT just wanted a new, expensive toy. Also, he had to justify the investment vis-à-vis the owners of the company, who viewed IT not as a core competence of the company but rather as a necessary tool whose costs had to be kept low.

To start with, a comparison of traditional NPVs based on the company-wide risk-adjusted discount rate of $\mu = 2 0 \%$ (corresponding to the suggestion made for “new products” in Brealey and Myers [1996, p. 206]) prescribed for IT projects was done. Table 1 depicts a summary of the outcome of this analysis where, for privacy reasons, the figures have been modified for this presentation.

The rationale given for the above entries was as follows:

The costs of hardware, software, and training were obtained by comparing different external offers.

A two-month external training session for the staff was assumed involving explicit costs of SAP and UNIX courses and opportunity cost for non-productive staff during the training session.

<table><tr><td colspan="2">Table 1. Cost-Benefit Analysis of SAP R/3</td></tr><tr><td>Investment Cost (R/3)</td><td>PV</td></tr><tr><td>Server cost</td><td>200,000</td></tr><tr><td>Desktop cost</td><td>225,000</td></tr><tr><td>Training effort (IT department)</td><td>90,851</td></tr><tr><td>Training effort (other)</td><td>615,319</td></tr><tr><td>Platform adoption</td><td>576,667</td></tr><tr><td>License cost</td><td>150,000</td></tr><tr><td>Maintenance</td><td>45,000</td></tr><tr><td>Total</td><td>1,857,837</td></tr><tr><td colspan="2">Benefits</td></tr><tr><td>Server maintenance</td><td>200,000</td></tr><tr><td>Operating effort</td><td>335,398</td></tr><tr><td>User productivity</td><td>906,000</td></tr><tr><td>Total</td><td>1,441,398</td></tr><tr><td colspan="2"></td></tr><tr><td>Net present value</td><td>-$416,500</td></tr></table>

Training costs for other employees were calculated in the same way assuming a oneweek external training that would cover only the direct use of SAP R/3.

The platform adoption cost was obtained by comparing the offer from an external consultant with internal estimates and checking it against published SAP case stories.

Benefits regarding the server cost result from ending the operation of the former mainframe.

No more operator night shifts will be required with the new system so that one less employee will be needed at the IT department.

During the first two years, the IT department would be fully occupied with realizing a stable implementation of the current application portfolio on the new platform so that no fixed plans for installing further applications were made. Thus, for the users, no productivity gains except those due to a more intuitive and user-oriented interface could be attributed to R/3. The increase in user productivity, hence, was calculated assuming a 2% time saving effect over a period of 10 years, which, due to the learning and training time needed, should be reached two years after implementation. Presuming an annual salary of \$80,000, this leads to savings of \$120,000 after the first year of operation and of \$240,000 after the second year.

On the basis of Table 1, R/3 should have been rejected, as the investment has a negative NPV of about \$420,000. Nevertheless, the CFO felt that this traditional analysis neglected the IT department’s argument concerning the possibility to implement novel applications, i.e., that the consideration of the second term in (2) would change the ranking of the competing software platforms.

When applying option thinking to such a situation, the first step to be taken is the identification of new enabling functions provided by the SAP R/3 software platform versus R/2 and to decide which applications based on these functions might be beneficial within a reasonable time horizon. This step is of great practical value as it leads to an objective and structured way of discussing such projects. It can be accomplished by comparing the existing platform specifications plus the known future functions with the firm’s information needs. In our case study, the users and the IT department were informed about the possibilities offered by an EDI interface, by workflow and document management systems, and by the Internet as a tool for doing business. Subsequently, in a brainstorming session, a number of novel applications were discussed that could be implemented after the two year stabilization phase, provided the transaction volume would then be sufficient. The implementation opportunities found were:

• EDI-based purchasing

• EDI-based invoicing

• Workflow for sales

• Engineering document handling

• World wide web based e-commerce system

For each of these implementation opportunities, the parameters for calculating the option values were estimated by a team consisting of corporate planning, accounting, and IT personnel, members of the projected user group and consultants. In order to obtain the parameter values, the following questions had to be answered (see the respective parameter in brackets):

What does the firm gain when supporting a task in such a way? [b]

How many tasks could the firm support with this type of application today? [N ]

• By what percentage will this number rise by the end of one year? [?]

In which range will that percentage then lie? [c]

When can the application be implemented at the earliest? [T]

• What is the total cost of ownership? [I]

The results are presented in Table 2:

Determining T, I, and $N _ { o }$ was rather straightforward. T was set according to the capacities and implementation plans of the IT department and the projected availability of suitable software. I was found by studying product prices and obtaining estimates for implementation and operating costs. For the EDI-based components, $N _ { o }$ was determined by checking the number of orders per year sent to customers and suppliers who already had a suitable EDI interface. Workflow for sales $N _ { o }$ was obtained by analyzing the number of documents handled in a typical sales transaction multiplied by the number of transactions per year. Similarly, $N _ { o }$ for the engineering document handling application was estimated. $N _ { o }$ for the world wide web application was found by asking customers in an empirical survey whether they would be willing to order their products via the Internet.

Estimating the other parameters was not as easy. For the EDI components, estimates for ? were obtained by checking the customers’ and suppliers’ past rate of adopting EDI and verified by asking them about their EDI-related IT plans. Then, different scenarios regarding the adoption were created and the variance was computed using the percentile estimation for the normal distribution. For the workflow and document handling components, Corporate Planning provided different scenarios regarding the development of the firm’s sales. Here, the growth rate and variance obtained were directly applied to the number of internal transactions in sales and development, as each sale triggered a constant average number of internal process steps. Estimates for the web components ? and c were gathered using market research data regarding the growth rate of e-commerce systems. The savings in logistics and productivity gains per usage b were calculated by valuing a cautious estimate of the time gained via accompanying business process reengineering multiplied by average salaries.

The next step was the calculation via (4) of the current $V _ { o }$ value of the applications described above

On the basis of the values in Table 3, the three different methods for the valuation of these applications developed in the previous section were applied:

<table><tr><td colspan="7">Table 2. Data for Option Valuation</td></tr><tr><td>Implementation Opportunity</td><td>b</td><td> $N_0$ </td><td>α</td><td>σ</td><td>T</td><td>I</td></tr><tr><td>EDI-based purchasing</td><td>100</td><td>100</td><td>8%</td><td>35%</td><td>4</td><td>$50,000</td></tr><tr><td>EDI-based invoicing</td><td>100</td><td>100</td><td>7%</td><td>30%</td><td>2</td><td>$200,000</td></tr><tr><td>Workflow for sales</td><td>70</td><td>150</td><td>5%</td><td>45%</td><td>4</td><td>$100,000</td></tr><tr><td>Engineering document handling</td><td>90</td><td>300</td><td>7%</td><td>35%</td><td>3</td><td>$300,000</td></tr><tr><td>World wide web based e-commerce system</td><td>150</td><td>250</td><td>15%</td><td>80%</td><td>5</td><td>$1,500,000</td></tr></table>

<table><tr><td colspan="3">Table 3. Current Value of Applications</td></tr><tr><td>Implementation Opportunity</td><td> $N_0 \cdot b$ </td><td> $V_0$ </td></tr><tr><td>EDI-based purchasing</td><td>10,000</td><td>95,000</td></tr><tr><td>EDI-based invoicing</td><td>10,000</td><td>87,000</td></tr><tr><td>Workflow for sales</td><td>10,500</td><td>79,000</td></tr><tr><td>Engineering document handling</td><td>27,000</td><td>235,000</td></tr><tr><td>World wide web based e-commerce system</td><td>37,500</td><td>880,000</td></tr></table>

<table><tr><td colspan="5">Table 4. Comparison of NPV1, NPV2, and Black-Scholes Option Values</td></tr><tr><td>Implementation Opportunity</td><td>NPV1</td><td>NPV2</td><td>BS</td><td>ΔNPV2/BS</td></tr><tr><td>EDI-based purchasing</td><td>38,000</td><td>39,200</td><td>57,400</td><td>46%</td></tr><tr><td>EDI-based invoicing</td><td>0</td><td>900</td><td>1,000</td><td>11%</td></tr><tr><td>Workflow for sales</td><td>0</td><td>15,400</td><td>27,200</td><td>77%</td></tr><tr><td>Engineering document handling</td><td>0</td><td>37,400</td><td>50,200</td><td>34%</td></tr><tr><td>World wide web based e-commerce system</td><td>110,000</td><td>470,000</td><td>514,000</td><td>9%</td></tr><tr><td>Total</td><td>148,000</td><td>562,900</td><td>649,800</td><td>16%</td></tr></table>

${ \mathsf { N P V } } _ { 1 }$ analysis (4);

an extended version of the NPV analysis, where the possibility not to install the applications is taken into account denoted as ${ \mathsf { N P V } } _ { 2 }$ (6), where the same discount rate was used as in (4);

the option value based on the Black-Scholes formula for valuing an European call option (7).

The different results based on $r = 6 \%$ are shown in Table 4.

To understand the differences, recall the implicitly underlying assumptions for each of the three methods. The NPV method assumes an implementation of the application at time T—obtaining the benefits and paying investment cost regardless of the observed realization of $V _ { T } .$ It should be noted that these assumptions do not coincide with the real setting, because an application will not be implemented if it turns out not to be profitable at time T. Only EDI-based purchasing and the world wide web based ecommerce system show a positive value. However, the NPV of both applications amounting to \$148,000 is not sufficient to justify the implementation of R/3. In contrast, the two other evaluation methods show positive values for all implementation opportunities. The total values of \$562,900 and \$649,800 respectively exceed the negative passive NPV based on a fixed application portfolio of the R/3 platform and lead to a quantitative justification of the decision to switch platforms. Table 4 also indicates that, although ${ \mathsf { N P V } } _ { 2 }$ and the Black-Scholes formula are based on different assumptions, they show a difference of only 16%, which increases the credibility of the result as both methods indicate that SAP R/3 should be preferred regardless of the assumptions made about the proper incorporation of risk. In fact, (4) can be seen as a cautious estimate of the option value, since the discount rate of the value is used even though the downside risk is limited. Benaroch and Kaufmann (2000) achieve a similar effect by setting a high convenience yield in their modified Black-Scholes model. Incidentally, note that it is possible to sum the values of different implementation opportunities to obtain the second term in (2) only if the respective applications can be implemented independently from each other, i.e., if it is not the case that one application can be implemented only if another one is already in use. In our opinion, in practice this usually occurs within a reasonable planning horizon, as it is very hard to get reliable estimates for (3) for applications whose implementation has to be decided upon in the distant future and whose feasibility is contingent on other applications that perhaps will not be implemented.

The first versions of the models based on the estimates summarized in Table 2 were met with considerable skepticism by the CFO who questioned a number of assumptions made, especially where b, ?, and c where concerned, and suspected “wishful thinking by the IT department.” To increase the validity of such estimates and management’s confidence in the valuation procedure, a substantive number of sensitivity analyses were done to check the dependence of the decision when parameter settings where changed within plausible ranges. This was done using benchmarks via direct industry contacts, the consultants’ know-how accumulated in similar projects, and findings in the relevant literature. Similarly to Benaroch and Kaufmann (2000), we found that in this case the partial derivatives derived from (4) and (7) were of limited usefulness for the sensitivity analyses undertaken as they provide information only on the effect of the change of one parameter in the vicinity of the current value that is directly used in the formula. As an example of the sensitivity analyses done, an analysis of the effects of a change of the estimated variance and of the implementation decision point for the "EDI-based purchasing" application is described in Table 5.

From Table 5 it can be seen that, with a rise in uncertainty, $N P V _ { 2 }$ and BS increase, while $N P V _ { \uparrow }$ stays constant. If W would be corrected because of a higher c, the NPV would even decrease. The increasing values reflect the higher upside potential while the downside risk does not lower the value due to freedom of choice in implementing the application under consideration. Similarly, a change in the number of periods until the application can be implemented lowers the NPV of the application as the time value of money decreases. The option values increase due to the fact that the more periods considered, the higher the upward potential while the downward risk is limited.

<table><tr><td colspan="13">Table 5. Different Scenarios for the Implementation Opportunity EDI-Based Purchasing</td></tr><tr><td></td><td colspan="3">T = 3</td><td colspan="3">T = 4</td><td colspan="3">T = 5</td><td colspan="3">T = 6</td></tr><tr><td></td><td>NPV1</td><td>NPV2</td><td>BS</td><td>NPV1</td><td>NPV2</td><td>BS</td><td>NPV1</td><td>NPV2</td><td>BS</td><td>NPV1</td><td>NPV2</td><td>BS</td></tr><tr><td>σ = 15%</td><td>40,300</td><td>40,300</td><td>52,900</td><td>38,200</td><td>38,200</td><td>55,300</td><td>36,000</td><td>36,000</td><td>57,600</td><td>33,700</td><td>33,700</td><td>59,700</td></tr><tr><td>σ = 25%</td><td>40,300</td><td>40,400</td><td>53,200</td><td>38,200</td><td>38,400</td><td>55,800</td><td>36,000</td><td>36,200</td><td>58,200</td><td>33,700</td><td>33,900</td><td>60,400</td></tr><tr><td>σ = 35%</td><td>40,300</td><td>41,100</td><td>54,500</td><td>38,200</td><td>39,200</td><td>57,400</td><td>36,000</td><td>37,100</td><td>60,100</td><td>33,700</td><td>34,800</td><td>62,500</td></tr><tr><td>σ = 45%</td><td>40,300</td><td>42,500</td><td>56,500</td><td>38,200</td><td>40,600</td><td>59,900</td><td>36,000</td><td>38,500</td><td>62,900</td><td>33,700</td><td>36,100</td><td>65,500</td></tr><tr><td>σ = 55%</td><td>40,300</td><td>44,100</td><td>59,000</td><td>38,200</td><td>42,300</td><td>62,800</td><td>36,000</td><td>40,100</td><td>66,000</td><td>33,700</td><td>37,700</td><td>68,900</td></tr></table>

The above analyses convinced the CFO that the decision in favor of SAP R/3 was robust within a plausible range of parameters. However, he still worried about how to control the investment decision. When using the NPV method, investment control is a rather straightforward task: the forecasted cash flows must be compared with the actual ones as reported in the accounting system. When employing an option-based model, there is no direct analog of the option value computed with figures in the accounting system, and even if the software platform decision was right, it might happen that none of the implementation opportunities is used later on in case the uncertain environment develops in a specific fashion. One, thus, has to employ a control method that conforms to the different framing of the problem, i.e., that checks whether the decision tree was set up properly and whether the models describing the development of the value of the underlying asset were correct. More precisely, for our case, this means that at each implementation decision point T, one should check whether the implementation opportunity is in fact present for SAP R/3 and not for SAP R/2, and that in the course of determining V and I one should verify whether, on the basis of the data so far observed, the parameter estimates were reasonable.

## Implications

Let us summarize the main implications of option thinking in the case presented as follows: Even though the initial set of applications run under SAP R/3 was the same as the set used under SAP R/2, the additional opportunities to introduce applications based on EDI, workflow management, document management, and e-commerce justified the introduction of SAP R/3 as shown via different valuation models for a range of parameter values. This convinced the CFO and the users that switching to SAP R/3 was to the advantage of the firm as the higher implementation cost could be related to higher future benefits and the additional value provided by SAP R/3 could be plausibly and objectively explained. In fact, the company currently is at T = 2, implementing the two EDIbased applications and starting an e-commerce application, because the implementation of SAP R/3 and the stabilization phase of the initial application portfolio turned out to be less timeconsuming than expected when making the software platform decision and the parameter estimates used proved very conservative.

The method discussed stresses that software platforms derive a substantial part of their benefits from implementation opportunities. In contrast to NPV analysis, where the higher uncertainty of possible future implementation possibilities is punished, it is recognized that a higher uncertainty leads to higher potential benefits while, due to a given flexibility, possible unfavorable developments do not entail losses. The fact that opportunities can be quantified monetarily is often hard to explain to management. This problem can be summarized in the following question regarding the e-commerce system: "You actually expected a cash flow of 110,000 and valued it with 514,000. Why?” The appropriate answer is: In the expected NPV calculation, it is assumed that the e-commerce system will be implemented at time T regardless of the information available at that time. The option approach, in contrast, assumes that the e-commerce system will only be implemented if the expected value at time T is positive. Therefore, in the options approach, the negative branches are pruned since no rational decision maker would support such a decision. Therefore, the value of 110,000 is not the expected value of the project in the presence of flexibility.

Fixing the value of these implementation possibilities provides a clear structure for determining the value of “long-run potential” in the decision process. It also gives users a concrete idea of what applications they can expect from a particular alternative. Unlike flexibility indices or similar measures, which cannot be directly related to implementation costs, the result of the valuation procedure is measured along the same scale as such costs. A clear method for deriving the value of a software platform from the basic assumptions is shown. Plausibility can be backed using hard data from accounting and benchmarks obtained with other projects and/or results published in the literature.

However, a number of problems inherent to optionbased software platform valuation arose: Option models make specific assumptions regarding the incorporation of risk, which is problematic in our area of application. Furthermore, additional parameters, namely <sup>c</sup> and T, have to be estimated. While the latter task turned out to be quite straightforward, it is difficult to obtain reliable estimates of the variance. Reliability checks based on the use of models built on different assumptions and sensitivity analyses should, therefore, be conducted. While in our case study it was found that the preference ranking of the software platforms under consideration turned out to be robust to changes in model assumptions and parameter values within reasonable bounds, it is unclear what conclusions should be drawn from an analysis where this is not the case (for similar findings, see Benaroch and Kaufmann 2000).

Controlling investment is more difficult. Whereas in the case of the NPV method it is sufficient to compare forecasted expected cash flows with those observed, here one must check whether the decision tree was set up correctly and whether the parameter estimates proved reasonable in view of the business process data observed. If this is not done and/or if there is no clear responsibility for exercising the options identified, project advocates have an incentive to overstate the value of implementation opportunities, as they do not have to be implemented if the future turns out unfavorable. In our case study, most of the option value comes from the e-commerce system. Therefore, the risk mainly depends on this particular application. The total risk would be reduced if the portfolio of the applications were more balanced. Under the assumption of independent applications, risk would be minimal with a balanced portfolio of applications.

## Conclusions

In this paper, we have presented a methodology for valuing implementation opportunities provided by a software platform and demonstrated the advantages of applying this approach to support the selection of such a platform. Using a real-life case study concerned with the decision of whether to continue using SAP R/2 or switching to SAP R/3, we have shown that this method can lead to a better-structured decision process, to an improved integration of users, and to a more objective and controllable way of arriving at a decision.

The conclusions from this work for MIS practice answer a number of questions frequently posed with regard to software platform selection:

Can the NPV method be used for software platform valuation? One can use the NPV method for those applications sure to be implemented on that particular platform. However, the value determined in such a way is too low if it is possible to postpone the implementation decision so as to learn more about the development of the benefits of an application, since this limits the downward risk.

Can option valuation models be used, even though benefits of applications are not traded in perfect financial markets and model parameters cannot be estimated on the basis of past prices? In our area of application, the goal of option valuation is different from that of the valuation of financial options. While the latter is the determination of an option price in view of arbitrage opportunities, the former is the selection of the software platform providing the highest value. Thus, as long as this preference ranking does not change, one can live with imprecise parameter values and competing model assumptions. To check the robustness of the ranking, various models should be applied and sensitivity analyses conducted. In our case study, the framing of the problem as a decision tree turned out to be decisive, whereas the method used for option valuation and parameter estimation was less critical, i.e., “option thinking” was important and precise valuation was a secondary issue.

How can an option-based investment decision be controlled? Controlling investment in optionbased decisions must focus on the issue of whether the decision tree was set up properly and the models describing the development of the value of the implementation opportunity were correct rather than on the comparison of projected and observed cash flows as in the case of the NPV method. The right software platform decision does not imply that all applications identified as implementation opportunities are actually implemented.

As the results presented here are based on only one case, it is clearly too early to view our statements as generally acceptable. A number of questions still remain unanswered and research in this direction would certainly represent a fruitfu area of investigation. From the authors’ point of view, the following issues appear to be particularly interesting:

The development of option valuation models with limited possibilities of hedging: in fact, in the case study presented, most of the parameter values are derived from sales development. Given the relation between sales and profit and postulating “fundamentally oriented” investors, it seems possible to use the firm’s stock for hedging in the case of a valuation based on the Black-Scholes model (for a similar argument, see Benaroch and Kaufmann 2000). Such a model could remedy the deficiencies of models (4) and (7) and allow the use of financial market data for parameter estimation.

The empirical investigation of the statistical properties of the development of benefits of applications in order to broaden the support for the geometric Brownian motion model or to study other, possibly more suitable, models.

Improvement of methods for estimating parameters: in particular, more general guidelines could make the application of the option valuation of software platforms less timeconsuming and more reliable.

## Acknowledgements

The authors would like to thank the two anonymous referees for their valuable comments and suggestions.

## References

Amram M., Kulatilaka, N., and Henderson, J. "Taking an Option on It", CIO (12:17), 1999, pp. 46-52.

Benaroch M., and Kauffman R. J. “A Case for Using Option Pricing Analysis to Evaluate Information Technology Project Investments,” Information Systems Research (10:10), 1999, pp. 70-86.

Benaroch M., and Kauffmann R. J. "Justifying Electronic Network Expansion Using Real Option Analysis," MIS Quarterly (24:2), June 2000, pp. 197-225.

Black, F., and Scholes, M. "The Pricing of Options and Corporate Liabilities,” Journal of Political Economy (81), 1973, pp. 637-659.

Brealey, R. A., and Myers S. C. Principles of Corporate Finance, McGraw-Hill, New York, 1996.

Busby, J. S., and Pitts, C. G. C. “Real Options in Practice: An Exploratory Survey of How Finance Officers Deal with Flexibility in Capital Appraisal,” Management Accounting Research (8:2), 1997, pp. 169-186.

Buss, M. D. J. “How to Rank Computer Projects,” Harvard Business Review, January-February 1983, pp. 118-125.

Chalsani P., Jha S., and Sullivan K. “An Options Approach to Software Prototyping,” Technical Report, Carnegie Mellon University, Computer Science Department, February 1998.

Copeland, T. E. J., and Weston F. Financial Theory and Corporate Policy (3<sup>rd</sup> ed.), Addison-Wesley, Reading, MA, 1992.

Cox, J., Ross, S., and Rubinstein, M. “Option Pricing: A Simplified Approach,” Journal of Financial Economics (6), September 1979, pp. 229-263.

DosSantos, B. L. “Justifying Investments in New Information Technologies,” Journal of Management Information Systems (7:4), Spring 1991, pp. 71-90.

Hochstrasser, B. "Justifying IT Investments,” in The Evaluation of Information Systems Investments, L. Willcocks (ed.), Chapman & Hall, London, 1994, pp. 151-169.

Kambil, A., Henderson, J., and Mohsenzadeh, H. “Strategic Management of Information Technology Investments: An Option Perspective,” in Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage R. D. Banker, R. J. Kauffman, and M. A. Mahmood (eds.), Idea Publishing Group, Harrisburg, PA, 1993, pp. 161-178.

Kester, W. C. “Today's Options for Tomorrow's Growth,” Harvard Business Review (62), March-April 1984, pp. 153-161.

Mahajan, V., Muller, E., and Bass, F. “New Product Diffusion Models,” in Handbook of Opera-

tions Research and Management Science, J. Eliashberg (ed.), Elsevier Science Publishers, Amsterdam, 1993, pp. 349-408.

Margrabe, W. “The Value of an Option to Exchange One Asset for Another,” Journal of Finance (33:1), March 1978, pp. 177-186.

Mukhopadhyay, T., Kekre, S., and Kalathur, S. “Business Value of Information Technology: A Study of Electronic Data Interchange” MIS Quarterly (19:2), June 1995, pp. 137-156.

Pfeiffer, H. K. C. The Diffusion of Electronic Data Interchange, Physica, Heidelberg, Germany, 1992.

Sullivan, K., Chalsani, P., and Jha, S. “Software Design Decisions as Real Options,” Technical Report, Carnegie Mellon University, Computer Science Department, June 1997.

Tam, K. Y. “Capital Budgeting in Information Systems Development” Information & Management (23:6), December 1992, pp. 345-357.

Taudes, A. “Software Growth Options,” Journal of Management Information Systems (15:1), 1998, pp. 165-185.

Trigeorgis, L. “The Nature of Option Interactions and the Valuation of Investments with Multiple Real Options,” Journal of Financial and Quantitative Analysis (28:1), March 1993, pp. 1-20.

Trigeorgis, L. “Real Options: An Overview,” in Real Options in Capital Investment: Models, Strategies and Applications, L. Trigeorgis (ed.), Praeger, Westport, CT, 1995, pp. 1-28.

Trigeorgis, L. Real Options: Managerial Flexibility and Strategy in Resource Allocation, MIT Press, Cambridge, MA, 1996.

Weill, P. “The Role and Value of Information Technology Infrastructure: Some Empirical Observations,” in Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage, R. D. Banker, R. J. Kauffman, M. A. Mahmood (eds.), Idea Publishing Group, Harrisburg, PA, 1993, pp. 547-572.

## About the Authors

Alfred Taudes is professor of Management Information Systems and Head of the Department of Production Management at the Vienna University of Economics and Business Administration (WU). He holds a Master's degree in MIS from Vienna University and a Ph.D. in Business Administration from the WU. He was an associate professor of MIS at Münster University, Germany, worked as professor of MIS at Augsburg University and Essen University, Germany, and as a visiting professor at the Institute of Policy and Planning Sciences of Tsukuba University, Japan. He has co-authored several books and more than 50 articles on various aspects of MIS, which have appeared in journals such as Journal of Management Information Systems, Applied Computer Science, European Journal of Operations Research, Information Management, Marketing Science, and International Journal of Marketing. He has consulting experience in the design and implementation of DSS, in manufacturing information systems, and in the development of strategies for implementing standard software, which is also one of his current research interests.

Markus Feurstein is a research assistant at the Department of Production Management at Vienna University of Economics and Business Administration (WU). He holds a Master's degree in Physics from the University of Vienna and a Ph.D. in Theoretical Physics from the Vienna University of Technology. He has co-authored more than 30 articles on Lattice Gauge theory, biophysics, market research, and real options.

Andreas Mild is assistant professor at the Department of Production Management at Vienna University of Economics and Business Administration (WU). He holds a Master's degree in Business Administration from the WU and a technical college degree in Mechanical Engineering. One of his current research interests is the development of evaluation models for information technology using real options.

## Appendix

## Mathematical Appendix

We derive an explicit formula for the extended ${ \mathsf { N P V } } _ { 2 }$ . We compute $E ( \boldsymbol { \mathrm { m a x } } [ V _ { \tau } - I , O ] )$ . We can then write

$$
V _ {T} = V _ {0}. e ^ {\tilde {\alpha}. T + \sigma . \sqrt {T}. z}
$$

where $\tilde { \alpha } = \alpha - \frac { \sigma ^ { 2 } } { 2 }$ and z is a standardized normal variable.

The expected value becomes

$$
\int_ {z _ {0} \sqrt {2 \pi}} ^ {\infty} \frac {1}{(V _ {0} . e ^ {\tilde {\alpha} . T + \sigma . \sqrt {T} . z} - I). e ^ {\frac {z ^ {2}}{2}} d z} = \frac {1}{\sqrt {2 \pi}} \int_ {z _ {0}} ^ {\infty} (V _ {0}. e ^ {\tilde {\alpha}. T + \sigma . \sqrt {T}. z}). e ^ {\frac {z ^ {2}}{2}} d z - \frac {I}{\sqrt {2 \pi}} \int_ {z _ {0}} ^ {\infty} e ^ {\frac {z ^ {2}}{2}} d z
$$

with the lower bound of the integral

$$
z _ {0} = \frac {\ln \left(\frac {I}{V _ {0}}\right) - \tilde {a} . T}{\sigma \sqrt {T}}
$$

In the first term of the expected value, we complete the square in the exponent to obtain

$$
\frac {V _ {0} \cdot e ^ {\bar {\alpha} \cdot T}}{\sqrt {2 \pi}} \int_ {z _ {0}} ^ {\infty} (e ^ {\sigma \cdot \sqrt {T} \cdot z}) \cdot e ^ {\frac {z ^ {2}}{2}} d z = \frac {V _ {0} \cdot e ^ {\alpha \cdot T}}{\sqrt {2 \pi}} \int_ {z _ {0}} ^ {\infty} e ^ {\frac {1}{2} (z - \sigma \sqrt {T}) ^ {2}} d z = V _ {0} \cdot e ^ {\alpha \cdot T}. N (- z _ {0} + \sigma \sqrt {T})
$$

where $\mathsf { N } ( . )$ denotes the cumulative standard normal distribution.

The second term can be written in terms of the standard normal distribution $I . N ( - z _ { o } )$

Finally, the extended ${ \mathsf { N P V } }$ is given by

$$
N P V _ {2} = e ^ {- \mu T}. (V _ {0}. e ^ {\alpha T}. N (d _ {1}) - I. N (d _ {2}))
$$

$$
\boldsymbol {d} _ {1} = \frac {1}{\sigma \sqrt {T}} \left(\ln \left(\frac {V _ {0}}{I}\right) + \left(\alpha + \frac {1}{2} \sigma^ {2}\right). T\right)
$$

$$
\textbf {d} _ {2} = \textbf {d} _ {1} - \sigma \sqrt {T}
$$
