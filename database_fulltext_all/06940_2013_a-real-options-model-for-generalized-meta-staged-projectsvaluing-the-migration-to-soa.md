---
otero_id: 6940
otero_key: "D9WXZPN3"
title: "A Real Options Model for Generalized Meta-Staged Projects—Valuing the Migration to SOA"
authors: "Suvankar Ghosh; Xiaolin Li"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0488"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/D9WXZPN3/fulltext/images/05d9f0c3ac92cbb7ffd6c320cabb511cfcec30d1e93ab0d71d4984cd0e285152.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Real Options Model for Generalized Meta-Staged Projects—Valuing the Migration to SOA

Suvankar Ghosh, Xiaolin Li

To cite this article:

Suvankar Ghosh, Xiaolin Li (2013) A Real Options Model for Generalized Meta-Staged Projects—Valuing the Migration to SOA. Information Systems Research 24(4):1011-1027. http://dx.doi.org/10.1287/isre.2013.0488

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/D9WXZPN3/fulltext/images/a0a34107d3705d13ed223a829556117fbbc283f64d1e1708d4cf61af999e532e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Real Options Model for Generalized Meta-Staged Projects—Valuing the Migration to SOA

Suvankar Ghosh

Department of Decision Sciences, Economics, and Information Systems, University of South Dakota, Vermillion, South Dakota 57069, Suvankar.Ghosh@usd.edu

Xiaolin Li

Department of E-Business and Technology Management, College of Business and Economics, Towson University, Towson, Maryland 21252, xli@towson.edu

his paper develops an innovative real options (RO) model for valuing multistage information technology (IT) projects that can be viewed as comprising meta stages. In RO literature, multistage investment programs have been treated as either interproject or intraproject programs, with intraproject programs being evaluated using nfold Geske compound options and interproject programs valued using the so-called “subsidy-to-exercise price” logic. Our innovative RO model integrates the Geske compound option model with the subsidy-to-exercise price approach to value sequential investment programs that are neither purely interproject nor purely intraproject in nature but are composed of meta-stages. A meta-stage as a whole can be considered an interproject stage resulting in cash flows, but internally it consists of several intraproject stages that do not result in cash flows. We show that a key problem in IT, which is migrating to a Service-Oriented Architecture (SOA) for integrating a firm’s many disparate applications, systems, data, and business processes, is best viewed as an investment program comprising meta-stages. Examining SOA migration from an RO lens is particularly apt at this time not only because of the importance of SOA but also because doubts have surfaced about the value of SOA. We illustrate our RO model by applying it to the simulated case of a firm migrating to SOA. We also develop a software tool based on the Mathematica<sup>™</sup> computational platform so that practitioners can easily apply our innovative options pricing model to determine the true value of SOA in their business contexts.

Key words: business value of IT; real options; economics of IS; service-oriented architecture (SOA); enterprise systems; analytical modeling

History: Anitesh Barua, Senior Editor; Sudip Bhattacharjee, Associate Editor. This paper was received on August 12, 2010, and was with the authors 9 months for 5 revisions. Published online in Articles in Advance July 24, 2013.

## 1. Introduction

Real options (RO) is increasingly being applied to value investments in information technology (Dos Santos 1991, Benaroch and Kauffman 2000, Bardhan et al. 2004, Benaroch et al. 2007) and in many other areas (Perlitz et al. 1999, Cassimon et al. 2004, Paxson 2007). From single-stage investment scenarios (Dos Santos 1991, Benaroch and Kauffman 2000), typically modeled using the Black-Scholes (Black and Scholes 1973) options pricing model or some variant thereof, the focus has been shifting to applying RO in more complex multistage investments (Bardhan et al. 2004, Cassimon et al. 2004, Benaroch et al. 2006). In RO literature, multistage investment programs have been viewed as comprising either intraproject or interproject stages (Benaroch et al. 2006). In a program with intraproject stages, the investments in the various stages do not result in cash inflows, and it is only after completing all the intraproject stages that a cash flow generating asset is acquired. In an interproject program, on the other hand, each of the intermediate investments leads to cash flows. The extant RO literature has not tackled the case of more complicated hybrid programs that have both interproject as well as intraproject characteristics. In this article, we introduce the notion of a generalized program consisting of meta stages where each meta-stage itself comprises several intraproject stages. A cash flow generating asset is created at the completion of each meta-stage but not when an intraproject stage within a metastage is completed. In §2, we build an RO model for valuing a generalized program with meta-stages and, later in the article, apply it to the important case of migrating a firm’s applications environment to a service-oriented architecture (SOA). We show in §3 that a firm’s migration to SOA can be viewed as an investment program comprising meta-stages and hence can be valued using our model.

Service-oriented architecture (SOA) is important to IT organizations because it holds the key to integrating a firm’s applications, systems, processes, and data—a problem that has plagued IT organizations for several decades (Erl 2006, Marks and Bell 2006). SOA envisages a firm’s portfolio of applications as comprising services callable over the Internet, which are referred to as Web Services (Erl 2006). Business applications expose key functionality and information as Web Services, thereby enabling the reuse of software components while achieving integration of data and applications across organizational and firm boundaries. Given the promise of Web Services and SOA, a curious thing appears to be happening on the road to the new world of SOA. For many organizations, it appears that SOA is a failure. In fact, the Burton Group, a respected analyst firm, declared “SOA is dead” in early 2009 (Krill 2009). Anne Thomas Manes, a research director at the Burton Group, said, “Once thought to be the savior of IT, SOA has turned into a great failed experiment—at least for most organizations” (Krill 2009). What is interesting is that amidst this gloom, there is still a large and very much pro-SOA camp out there. Evidence of this exists in the growing number of SOA success stories on the SOA.org web site<sup>1</sup> IDC, also a respected market research firm, disagrees with the Burton Group, stating that SOA is very much alive, and it is forecasting a 25% increase in SOA spending worldwide by 2013 (Nguyen 2010).

The importance of SOA to IT organizations makes it imperative to resolve the question of the real value of SOA to the business, particularly in the current climate of doubt about SOA’s true worth. Therefore, our article makes a timely contribution in developing a general RO model that can be used to value SOA. We describe the costs and benefits of SOA in §4, simulate the case of a representative firm migrating to SOA in §5, and finally value its SOA investment program in §6. Furthermore, we also develop and make available a general-purpose software tool in Appendix D (available as supplemental material at http://dx.doi.org/10.1287/isre.2013.0488) for valuing any arbitrary meta-staged program that runs on the Mathematica<sup>™</sup> platform, a widely used computational package. Therefore, in this article, we accomplish the following four main objectives: (1) introduce a new conceptual view of thinking about investment programs in terms of meta-stages, (2) advance the theoretical literature on RO models by developing a new type of model that leverages the best features of past RO models on multistage investments, (3) apply this innovative RO model to the very important case of

SOA migration, and (4) develop a general purpose software tool based on a widely used computational platform that enables practitioners to easily use our RO model not just in the SOA application but also in other investment programs that can be modeled as comprising meta-stages.

## 2. Integrating Compound and Nested Options for Generalized Programs

As indicated in §1, previous RO literature has treated multistage investment programs as either intraproject or interproject programs (Benaroch et al. 2006, Bardhan et al. 2004). We introduce the notion of a generalized investment program, which is neither purely interproject nor purely intraproject in nature but consists of meta-stages as shown in Figure 1. In this section, we develop a mathematical RO model for the valuation of meta-staged programs. A metastage consists of several stages of investment called intraproject stages, and as shown in Figure 1, the first meta-stage has $P _ { 1 }$ investments with the amounts of these investments being $K _ { 1 , 1 } , K _ { 1 , 2 } , \ldots , K _ { 1 , P _ { 1 } }$ made at times $t _ { 1 , 1 } , t _ { 1 , 2 } , \ldots , t _ { 1 , P _ { 1 } }$ , respectively.

Completing an intra-project stage does not lead to any cash inflows but finishing the entire meta-stage obtains for the firm a cash flow bearing asset and the option to build the next meta-stage. Any meta-stage could be abandoned in the middle by simply not making the next incremental intraproject stage investment. Abandoning a meta-stage terminates the remainder of the investment program. There are no salvage costs in the model, but the firm would still get the benefits of cash flow-generating assets acquired from previous meta-stages that have been fully built.

The option to build the next meta-stage is created by fully investing in the previous meta-stage and the value of this option is obtained by the n-fold Geske compound option model (Geske 1979, Cassimon et al. 2004). The Black-Scholes (1973) model, where there is exactly one future investment to be made, is simply a special case of the Geske compound option model. A key assumption made in the Geske or the Black-Scholes model is that the value of the asset acquired unfolds as a geometric Brownian motion (GBM) diffusion process. Although a small minority of RO models does consider other types of stochastic processes for the evolution of asset value, such as a jump-diffusion process (Pennings and Serreno 2010), the vast majority of RO continuous-time models for investments in IT and in many other areas assume the basic GBM diffusion process for asset value evolution. The GBM assumption is made by Cassimon et al. (2004) in new drug discovery, by Paxson (2007) in real estate investment, by Perlitz et al. (1999) in general R&D projects, by Jensen and Warren (2001) in

Figure 1 Generalized Program with Meta-Stages  
![](/api/attachments/D9WXZPN3/fulltext/images/8e098bbae6a27aeb77a06d1d4e8eafa3992a58c9af30a102a3a010867efbdb10.jpg)

R&D projects in the telecommunications industry, by Benaroch and Kauffman (2000) in electronic banking, by Bardhan et al. (2004) in deploying a portfolio of software applications in a utilities firm, and by Taudes (1998) in investing in a new version of the SAP enterprise resource planning (ERP) system. Consequently, we retain the GBM assumption for asset price evolution in our model.

For aggregating the values of the interproject stages, we use the subsidy-to-exercise price logic where the option value of a downstream stage serves to reduce the exercise price or investment cost of the previous enabling stage (Benaroch et al. 2006). Bardhan et al. (2004) have suggested using the socalled “added-value” logic for evaluating interproject programs where the option value of a downstream stage is simply added to the benefits of the previous stage that enabled it. However, Benaroch et al. (2006) have argued that the added-value logic could overvalue the investment program. Consequently, in our model for the generalized program where we leverage the best features of previous models, we use the subsidy-to-exercise price logic for incorporating the effect of a downstream meta-stage upon the previous enabling meta-stage.

2.1. Modeling Generalized Investment Programs The model for the generalized investment program is formally set up as follows:

M = number of meta-stages in the investment program;

P = number of intraproject stages in kth meta-stage; $K _ { k , i }$ = nonstochastic amount of the investment, or the exercise price, of the ith intraproject stage in the kth meta-stage;

$t _ { k , i }$ = time at which the ith intraproject stage investment in the kth meta-stage is made;

$V _ { k }$ = value of the cash flows from meta-stage k discounted to $t _ { k , P _ { k } }$ when the last intraproject investment in meta-stage k is made;

 = standard deviation in the rate of return from the asset acquired in meta-stage $k ;$

r = risk-free rate;

 = discount rate for risky cash flows, also the weighted average cost of capital (WACC).

We first focus on how to value a meta-stage that does not have a subsequent meta-stage, for example, the last meta-stage M does not have a subsequent meta-stage. We also show later that a given meta-stage that does have a subsequent meta-stage can be modeled as one without a subsequent metastage after suitably modifying the exercise prices of the intraproject stages in the given meta-stage. The n-fold Geske compound option model is used to value the option to build a meta-stage assuming that this meta-stage does not have a subsequent meta-stage. Let $C _ { n } ( V , t )$ be the value at time t of an n-fold Geske compound option on an underlying asset of value V at t with n remaining payments to acquire the asset. Then Equation (1a) gives the value of the option to build meta-stage k at time $t _ { k - 1 , P _ { k - } }$ of the creation of this option and also the time of the last intraproject investment in the previous meta-stage, assuming that meta-stage k does not have a subsequent meta-stage.

$$
\begin{array}{l} C _ {P _ {k}} \big (V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})}, t _ {k - 1, P _ {k - 1}} \big) \\ = V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})} N _ {P _ {k}} \big (a _ {k, 1}, a _ {k, 2}, \ldots , a _ {k, P _ {k}}; \Omega_ {k} ^ {P _ {k}} \big) \\ - \sum_ {i = 1} ^ {P _ {k}} K _ {k, i} e ^ {- r (t _ {k, i} - t _ {k - 1, P _ {k - 1}})} \\ \cdot N _ {i} \big (b _ {k, 1}, b _ {k, 2}, \ldots , b _ {k, i}; \Omega_ {k} ^ {i} \big) \end{array}\tag{1a}
$$

where

$$
\begin{array}{l} a _ {k, i} = \frac {\ln (V _ {k} e ^ {- \mu (t _ {k , P _ {k}} - t _ {k - 1 , P _ {k - 1}})} / V _ {k , i} ^ {*}) + r (t _ {k , i} - t _ {k - 1 , P _ {k - 1}})}{\sigma_ {k} \sqrt {t _ {k , i} - t _ {k - 1 , P _ {k - 1}}}} \\ \qquad + \frac {\sigma_ {k} \sqrt {t _ {k , i} - t _ {k - 1 , P _ {k - 1}}}}{2} \end{array}
$$

$$
\begin{array}{c} b _ {k, i} = \frac {\ln {(V _ {k} e ^ {- \mu (t _ {k , P _ {k}} - t _ {k - 1 , P _ {k - 1}})} / V _ {k , i} ^ {*}) + r (t _ {k , i} - t _ {k - 1 , P _ {k - 1}})}}{\sigma_ {k} \sqrt {t _ {k , i} - t _ {k - 1 , P _ {k - 1}}}} \\ - \frac {\sigma_ {k} \sqrt {t _ {k , i} - t _ {k - 1 , P _ {k - 1}}}}{2} \quad \text {for i = 1,2,\ldots,P_{k}} \end{array}
$$

N = the l-variate standard normal distribution whose correlation matrix is denoted as $\Omega _ { k } ^ { l }$ because its value depends on the meta-stage k. The elements of the correlation matrix $\Omega _ { k } ^ { l }$ are $( \omega _ { i j } ) _ { i , j = 1 , \dots , l }$ with $\{ \omega _ { i i } = 1 ,$ $\omega _ { i j } = \omega _ { j i } ,$ and $\omega _ { i j } = \sqrt { ( t _ { k , i } - t _ { k - 1 , P _ { k - 1 } } ) / ( t _ { k , j } - t _ { k - 1 , P _ { k - 1 } } ) }$ for $i < j \}$

$V _ { k , i } ^ { * } =$ the so-called “at-the-money” critical values in the $a _ { k , i }$ and $b _ { k , \imath }$ terms in Equation (1a). These values are found by solving the following nonlinear system of equations:

$$
\begin{array}{c} C _ {i} (V _ {k, P _ {k} - i} ^ {*}, t _ {k, P _ {k} - i}) = K _ {k, P _ {k} - i} \quad \text { for } i = 1, 2, \ldots , P _ {k} - 1 \\ V _ {k, P _ {k}} ^ {*} = K _ {k, P _ {k}} \end{array}\tag{1b}
$$

The value of the last meta-stage M, which does not have a subsequent meta-stage, at the time of completing the investments in meta-stage $M - 1$ is found by setting $k = M$ in Equations (1a) and (1b). The derivation of the n-fold Geske compound option formula (Equation 1a) is deemed to be outside the scope of this article, which is leveraging extant theory, albeit aggregating that theory in a new way. The interested reader is referred to the appendix of Cassimon et al. (2004) for an outline of the proof and to Thomassen and Van Wouwe (2001) for the details of the derivation of Equation (1a). The derivation of the n-fold Geske formula also clarifies how the subscripted a and b coefficients indicated above are involved in the Geske compound option formula.

In the subsidy-to-exercise price logic used for evaluating pure interproject programs, the option value of the next stage is used to reduce the exercise price or investment cost of the given stage that spawns that option. In this model of the generalized program, the subsidy $S _ { k }$ that a meta-stage k receives from its subsequent meta-stage is first used to effectively reduce or eliminate the cost of the last intraproject stage of the given meta-stage. $S _ { k }$ is defined as the option value on the next meta-stage evaluated at $t _ { k , P _ { k } }$ . If this subsidy exceeds the exercise price of the last intraproject stage, then it can effectively eliminate the exercise prices of several intraproject stages at the tail end of the given meta-stage. The number of such intraproject stages $g _ { k }$ at the tail end of a meta-stage k whose exercise prices are effectively eliminated as a result of the subsidy $S _ { k }$ is given by

$$
\text {   If   } S _ {k} <   K _ {k, P _ {k}} \quad \text {   then   } g _ {k} = 0 \quad \text {   else   }
$$

$g _ { k } = \operatorname* { m a x } \{ i + 1 \}$ with respect to $i ,$ where $P _ { k } - 1 \ge i \ge 0$

$$
\text { and } S _ {k} - \sum_ {j = 0} ^ {i} K _ {k, P _ {k} - j} e ^ {r (t _ {k, P _ {k}} - t _ {k, P _ {k} - j})} \geq 0.\tag{2}
$$

If after effectively eliminating the exercise prices of $g _ { k }$ intraproject stages at the trailing end of the given meta-stage k there is some subsidy left over, then that goes to reduce the exercise price of the intraproject stage $P _ { k } - g _ { k }$ from $K _ { k , P _ { k } - g _ { k } } \mathrm { ~ t o ~ } K _ { k , P _ { k } - g _ { k } } ^ { \prime }$ where

$$
\begin{array}{l} K _ {k, P _ {k} - g _ {k}} ^ {\prime} = K _ {k, P _ {k}} - S _ {k} \quad \text { if } g _ {k} = 0 \quad \text { and } \\ K _ {k, P _ {k} - g _ {k}} ^ {\prime} = K _ {k, P _ {k} - g _ {k}} - \left[ S _ {k} e ^ {- r (t _ {k, P _ {k}} - t _ {k, P _ {k} - g _ {k}})} \right. \\ \left. - \sum_ {j = 0} ^ {g _ {k} - 1} K _ {k, P _ {k} - j} e ^ {- r (t _ {k, P _ {k} - j} - t _ {k, P _ {k} - g _ {k}})} \right] \\ \text { if } P _ {k} > g _ {k} > 0. \end{array} \tag {3}
$$

It is possible for $g _ { k } = P _ { k }$ or for the subsidy received from the subsequent meta-stage to be large enough to effectively eliminate the exercise prices of all the intraproject stages in meta-stage k. We treat this as a special case where meta-stage k loses its “optionlike” characteristics. In general, the subsidy from the subsequent meta-stage will effectively eliminate the exercise prices of zero or more of the trailing intraproject stages of meta-stage k but not necessarily all of them. With $g _ { k }$ of the trailing intraproject stages effectively eliminated from meta-stage k, this meta-stage is now simply left with the first $P _ { k } - g _ { k }$ intraproject stages and with a modified exercise price for the $P _ { k } - g _ { k }$ th intraproject stage. The Geske compound option model can now be applied to find the option value of meta-stage k at $t _ { k - 1 , P _ { k - 1 } }$ when the previous meta-stage $k { - } 1$ is fully invested in. Hence, the option value of the modified meta-stage k at $t _ { k - 1 , P _ { k - 1 } }$ after considering the subsidy from the subsequent meta-stage is now given by

$$
\begin{array}{l} C _ {P _ {k} - g _ {k}} \left(V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})}, t _ {k - 1, P _ {k - 1}}\right) \\ = V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})} N _ {P _ {k} - g _ {k}} \left(a _ {k, 1}, a _ {k, 2}, \dots , a _ {k, P _ {k} - g _ {k}}; \Omega_ {k} ^ {P _ {k} - g _ {k}}\right) \\ - \sum_ {i = 1} ^ {P _ {k} - g _ {k}} K _ {k, i} ^ {\prime} e ^ {- r (t _ {k, i} - t _ {k - 1, P _ {k - 1}})} N _ {i} \left(b _ {k, 1} b _ {k, 2}, \dots , b _ {k, i}; \Omega_ {k} ^ {i}\right) \quad (4 a) \end{array}
$$

where

$K _ { k , i } ^ { \prime } = K _ { k , i } { \mathrm { ~ f o r ~ } } i = 1 , 2 , \ldots , P _ { k } - g _ { k } - 1$ and $K _ { k , P _ { k } - g _ { k } } ^ { \prime }$ is given by Equation (3).

The $a _ { k , i }$ and $b _ { k , i }$ terms are computed by the same formulas for these terms as given in Equation (1a). The difference is that the values of the $V _ { k , i } ^ { * }$ terms involved in $a _ { k , i }$ and $b _ { k , \ast }$ change because they are now obtained from the following system of equations:

$$
\begin{array}{c} C _ {i} (V _ {k, P _ {k} - g _ {k} - i} ^ {*}, t _ {k, P _ {k} - g _ {k} - i}) = K _ {k, P _ {k} - g _ {k} - i} \\ \text { for } i = 1, 2, \ldots , P _ {k} - g _ {k} - 1 \\ V _ {k, P _ {k} - g _ {k}} ^ {*} = K _ {k, P _ {k} - g _ {k}} ^ {\prime} \end{array}\tag{4b}
$$

Equations (4a) and (4b) allow us to find the value of a meta-stage k considering the subsidy $S _ { k }$ received from the subsequent meta-stage $k + 1$ . In the subsidy-toexercise price logic, this option value of meta-stage k at $t _ { k - 1 , P _ { k - } }$ is then deemed available to subsidize the 1 exercise prices of the intraproject stages of meta-stage $k - 1 .$ , or

$$
S _ {k - 1} = C _ {P _ {k} - g _ {k}} \big (V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})}, t _ {k - 1, P _ {k - 1}} \big).\tag{4c}
$$

For the last meta-stage $M ,$ which has no subsequent stage, $S _ { M - 1 }$ is given by Equation (1a).

A special case arises when the subsidy $S _ { k }$ received by the meta-stage k from the subsequent meta-stage is large enough to defray the costs of all the intraproject stages of meta-stage $\begin{array} { r } { \dot { k } , } \end{array}$ such as when

$$
S _ {k} - \sum_ {j = 0} ^ {P _ {k} - 1} K _ {k, P _ {k} - j} e ^ {r (t _ {k, P _ {k}} - t _ {k, P _ {k} - j})} \geq 0\tag{5}
$$

In this case, meta-stage $k$ as seen from the vantage point of $t _ { k - 1 , P _ { k - 1 } }$ appears not as something with option-like characteristics but as a portfolio comprising the discounted value at $t _ { k - 1 , P _ { k - 1 } }$ of the cash flow generating asset of value $V _ { k }$ at $t _ { k , P _ { k } }$ and another component corresponding to the unused subsidy left after effectively eliminating the exercise prices of all the intraproject stages in meta-stage k. The value of the unused subsidy $\Delta S _ { k }$ discounted to $t _ { k - 1 , P _ { k - 1 } }$ is

$$
\begin{array}{l} \Delta S _ {k} = S _ {k} e ^ {- r (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})} \\ - \sum_ {j = 0} ^ {P _ {k} - 1} K _ {k, P _ {k} - j} e ^ {- r (t _ {k, P _ {k} - j} - t _ {k - 1, P _ {k - 1}})} \end{array}\tag{6}
$$

The value of meta-stage k including both components at $t _ { k - 1 , P _ { k - 1 } }$ is then given by Equation (7) and, in keeping with the subsidy logic, this is the subsidy $S _ { k - 1 }$ that meta-stage k provides to the meta-stage $k - 1$

$$
S _ {k - 1} = \Delta S _ {k} + V _ {k} e ^ {- \mu (t _ {k, P _ {k}} - t _ {k - 1, P _ {k - 1}})}\tag{7}
$$

Using Equations (4c) and (7), the value of a metastage with a subsequent meta-stage can be found at the time of completion of investment in the previous meta-stage. This value is the subsidy that a meta-stage provides to its previous meta-stage. Hence, starting from the last meta-stage whose value is found using Equation (1a), these procedures are repeatedly applied until the first meta-stage is reached. The value of the first meta-stage after it is suitably modified to incorporate the subsidy effect of its subsequent meta-stage then becomes the value of the generalized investment program. Because the investment program is triggered with the first investment of $K _ { 1 , 1 }$ made at $t _ { 1 , 1 } ,$ there are effectively $P _ { 1 } - g _ { 1 } - 1$ remaining intraproject stages looking forward from $t _ { 1 , 1 }$ after the subsidy from the subsequent meta-stage has been incorporated. The value of the investment program obtained using an options pricing logic is also referred to in RO literature as the strategic net present value (SNPV; Park and Herath 2000) of the program. Hence, the SNPV at $t _ { 1 , 1 } = 0$ of the generalized program with meta-stages is given by

$$
\mathrm{SNPV} = C _ {P _ {1} - g _ {1} - 1} \big (V _ {1} e ^ {- \mu (t _ {1, P _ {1}})}, 0 \big) - K _ {1, 1}.\tag{8}
$$

If the subsidy $S _ { 1 }$ received by the first meta-stage from the second meta-stage is sufficient to defray the costs of all the intraproject stages in the first metastage, then the SNPV of the investment program is simply

$$
\mathrm{SNPV} = V _ {1} e ^ {- \mu (t _ {1, P _ {1}})} + \Delta S _ {1},\tag{9}
$$

where $\Delta S _ { 1 }$ is obtained from Equation (6) after setting $k = 1$ and $t _ { 0 , P _ { 0 } } = 0 .$ . It should be noted that for the special case where $S _ { 1 }$ is sufficient to defray the costs of intraproject stages 2 through $P _ { 1 }$ in the first metastage and only partially the cost of the first intraproject stage in the first meta-stage, then $\Delta S _ { 1 }$ as found by Equation (6) is negative but this value can be used in Equation (9) to obtain the program SNPV.

## 2.2. Estimating 

Estimating $\sigma ,$ or the standard deviation in the returns from the underlying real asset acquired, is an admittedly difficult task and several approaches have been proposed in the literature for doing so (Benaroch and Kauffman 2000, Kogut and Kulatilaka 2001). We employ a heuristic procedure in estimating the volatility $\sigma _ { k }$ in the returns from the asset acquired at the end of a meta-stage k. First, optimistic, pessimistic, and likely values of cash flows stemming from the asset acquired are estimated. The likely cash flows are used to estimate the $V _ { k }$ term, or the value of the asset acquired upon the completion of the investment in meta-stage k at time $t _ { k , P _ { k } }$ , which is used in Equations (1a) and (4a) for computing the option value of the meta-stage at $t _ { k - 1 , P _ { k - 1 } }$ when this option is created. The pessimistic and optimistic cash flows are used to compute $V _ { k } ^ { \mathrm { o p t i m i s t i c } }$ and $V _ { k } ^ { \mathtt { p } }$ essimistic which are used to estimate $\sigma _ { k } ,$ , which is in turn involved in the $a _ { k , i }$ and $b _ { k , i }$ terms of the Geske compound option formula (Equations (1a) and (4a)). The heuristic makes use of the log-normal characteristics of a GBM. The GBM assumption, which results in a log-normal distribution of the terminal project value $V _ { T }$ at the end of an interval 601 T 7, is a common assumption made in continuous-time RO models in both single-stage scenarios (Dos Santos 1991, Benaroch and Kauffman 2000) and multistage scenarios (Taudes 1998, Cassimon et al. 2004, Bardhan et al. 2004, Benaroch et al. 2006, Paxson 2007).

If V evolves as a GBM over some time interval 601 T 7, then we have

$$
\ln \frac {V _ {T}}{V _ {0}} \sim \mathrm{N} \left(r T - \frac {\sigma^ {2} T}{2}, \sigma^ {2} T\right).\tag{10}
$$

Let time 0 be $t _ { k - 1 , P _ { k - 1 } }$ when the option on the kth meta-stage is created, or when the last intraproject stage investment is made in meta-stage $k - 1 .$ , and let time T be $t _ { k , P _ { k } }$ when the last intraproject stage investment in the kth meta-stage is made. Since ln $( V _ { T } / V _ { 0 } )$ is normally distributed, the probability is 95.5% that $\ln ( V _ { T } / V _ { 0 } )$ falls in an interval that is within $2 \sigma _ { \mathrm { { s } } } / \mathrm { T }$ of the mean. With the optimistic and pessimistic values of $V _ { T }$ being used to define the upper and lower ends of this interval, the volatility $\sigma _ { k }$ associated with the returns from the underlying asset is estimated by

$$
\sigma_ {k} = \frac {1}{4 \sqrt {t _ {k , P _ {k}} - t _ {k - 1 , P _ {k - 1}}}} \ln \frac {V _ {k} ^ {\text { optimistic }}}{V _ {k} ^ {\text { pessimistic }}}.\tag{11}
$$

For the first meta-stage, $t _ { k - 1 , P _ { k - 1 } }$ is simply equal to 0. Implicit in applying this heuristic is that meta-stage volatility does not change simply by elongating or compressing the time to complete the meta-stage. In other words, as the denominator of Equation (11) changes as the time to implement the meta-stage is compressed or elongated, the spread between the optimal and pessimistic meta-stage values at the time of the terminal investment in the meta-stage is assumed to adjust to offset the change in the denominator. We use this assumption that meta-stage volatilities are invariant to the length of time of the meta-stage later in §6 in our sensitivity analysis where we explore different project structures that compress or elongate the time to implement a meta-stage.

## 2.3. Mathematica<sup>™</sup> Algorithm for Valuing Meta-Staged Projects

We implement a recursive algorithm in the Mathematica<sup>™</sup> symbolic language for valuing a generalized investment program, which is flow charted in online Appendix C and specified in Appendix D. The algorithm can find the value of any generalized program comprising an arbitrary number of meta-stages and where each meta-stage itself can comprise an arbitrary number of intraproject stages. Given that Mathematica<sup>™</sup> and MATLAB<sup>™</sup> are the two most popular computational software packages, used in both industry as well as academia, our provision of an easy-to-use algorithm based on the Mathematica<sup>™</sup> platform will enable practitioners (and researchers) to model and value complicated multistaged investment programs. The seven procedures comprising the algorithm, InvestProgVal, SetTime-Origin, MetaStageVal, CompoundVal, GenPrevVStar, GenTauList, and GeskeFormula are given in online

Appendix D. They can be copied into a Mathematica<sup>™</sup> notebook file and run on any user’s Mathematica<sup>™</sup> installation. The user simply has to call the procedure InvestProgVal to find the value of any generalized investment program such as that shown in Figure 1. InvestProgVal is called as follows:

InvestProgVal ${ \mathrm { \Omega } } ^ { r } , \ \mu , \ \{ \sigma _ { 1 } , \ K _ { 1 , 1 } , \ K _ { 1 , 2 } , \ldots , K _ { 1 , P _ { 1 } } , \ V _ { 1 } , \ t _ { 1 , 1 } ,$ $\begin{array} { r } { { t _ { 1 , 2 } , \ldots , { \bf { t } } _ { 1 , P _ { 1 } } } \} , \{ \sigma _ { 2 } , { \bf { \phi } } K _ { 2 , 1 } , { \bf { \phi } } K _ { 2 , 2 } , \ldots , { \bf { \phi } } K _ { 2 , P _ { 2 } } , { \bf { \phi } } V _ { 2 } , { \bf { \phi } } t _ { 2 , 1 } , } \end{array}$ $\begin{array} { r } { t _ { 2 , 2 } , \ldots , \mathbf { t } _ { 2 , P _ { 2 } } \} , \ldots , \{ \sigma _ { M } , \ : K _ { M , 1 } , \ : K _ { M , 2 } , \ldots , K _ { M , P _ { M } } , \ : V _ { M } , } \end{array}$ $t _ { M , 1 } , \ t _ { M , 2 } , \ldots , \mathbf { t } _ { M , P _ { M } } \}$

After specifying general parameters such as the risk-free rate r and the WACC  for discounting risky project flows, the parameters of each meta-stage as defined earlier in §2.1 are specified as a Mathematica<sup>™</sup> list enclosed within the brackets { }. There are as many such meta-stage specification lists in the arguments list of InvestProgVal as there are meta-stages in the investment program. The flowchart in online Appendix C shows how the algorithm works.

## 3. Modeling SOA Implementation as a Generalized Program

As mentioned earlier in §1, SOA is essential to firms because it enables them to solve the vexing problem of integrating systems, applications, and data. The implementation of a full SOA environment, however, involves several major technologies, including an enterprise services bus (ESB), directory and governance service (DGS), data transformation and integration service (DTIS), adapters, business process management service (BPMS), and portals. These technologies and the role they play in the SOA environment are described in online Appendix A. Given the diversity of complex technologies involved, the build-out of the SOA infrastructure is best done in phases where in any given phase the organization deploys a major technology before moving on to the next. These SOA infrastructure technologies enable the development of two different kinds of applications: composition and orchestration applications. Composition applications are new applications that are built as compositions of existing Web Services such as those exposed through adapters together with any new Web Services developed. Composition applications typically leverage the services of the ESB, DTIS, DGS, and adapters, but they don’t require a BPMS. Orchestration applications leverage the infrastructure that has been put in place for composition applications but additionally need the facility of the BPMS for orchestrating processes and also a portal to engage humans as participants of operational business processes (Puschmann and Alt 2005).

Implementing SOA is generally done in two major phases—the first to deploy the infrastructure needed to build composition applications followed by that needed to build orchestration applications. Typically, a firm’s entry into building applications within an SOA framework is via composition rather than orchestration applications. This is because the SOA composition paradigm is quite similar to earlier concepts and architectures for component reuse developed in the 1990s such as the Common Object Request Broker Architecture, or CORBA, to develop integration standards (Vossen 1997). The orchestration of Web Services becomes a natural next step after the firm has gained expertise on developing applications as compositions of Web Services. Hence, the SOA implementation plan can be conceived of as a generalized project with two meta-stages as shown in Figure 2. The first meta-stage therefore consists of putting together the technology infrastructure elements needed to support the building of composition applications. These include investing in the ESB, DTIS, adapters, and DGS technologies starting with the initial investment in the ESB. The investment in the final intraproject stage of the DGS at $t _ { 1 , 4 }$ resulting in the completion of the first meta-stage allows the firm to build composition applications, and it starts doing so at some later point $t _ { 1 , 4 } ^ { \prime } .$

The completion of the investments in the first metastage also obtains for the firm the option to build the next meta-stage, which uses the first stage as its foundation and is composed of the investments in the BPMS and the portal. The completion of the second meta-stage obtains for the firm the ability to build orchestration applications, in addition to composition applications, which it starts doing from $t _ { 2 , 2 } ^ { \prime }$ onward. Although we recommend a two-meta-staged plan to implement SOA, that is not the only way for a company to migrate to SOA. Later in the sensitivity analysis, we discuss a 3-meta-stage migration plan to SOA in §6.1 and show that this can be easily handled by our RO model and the Mathematica<sup>™</sup> software tool we have built to evaluate generalized investment programs.

## 4. SOA Costs and Benefits—A Differential Analysis Approach

In developing the options pricing model (OPM) for SOA, we take a differential analysis approach in that the costs and benefits of building and deploying applications based on SOA are considered relative to the firm’s traditional or pre-SOA approach to building applications. The firm’s traditional approach could, for example, have involved building applications that have a client/server architecture. In this differential perspective on costs and benefits, SOA provides two major benefits relative to the traditional approach: (1) cost savings from improved IT productivity, and (2) enhanced business agility through increased IT agility. Since the model takes a differential perspective, it does not consider the direct business benefits of the new applications themselves such as in providing business automation or decision support. These benefits of the new applications are assumed to accrue to the firm regardless of whether the underlying architecture of the applications is traditional or SOA-based.

On a relative basis, a key advantage of the SOA approach is the heavy component reuse involved in building applications as compositions or orchestrations of Web Services resulting in time and cost compression in application development. Although the time and cost compression benefits of SOA are easier to measure, there are also intangible but no less real benefits in having a flexible IT asset that can enhance the agility of the business. Applications built using SOA can be quickly changed, thereby allowing rapid changes in business processes or in the way that business decisions are made. Furthermore, the

Figure 2 Meta-Stages in SOA Program  
![](/api/attachments/D9WXZPN3/fulltext/images/092494e89c4b6c7224f6772f536c3c68bb8780f4730d7518dd23ce9bafbb8b9f.jpg)

SOA infrastructure itself also allows applications to be built more quickly, again increasing the responsiveness of the business to a changing environment. Agile businesses appropriate rents by being quick to sense opportunities for competitive action, be it in introducing new products to fill emerging market needs, reconfiguring the network of partnerships to strengthen a firm’s market position, or leveraging technological innovations to restructure internal business processes for improved efficiency (Sambamurthy et al. 2003). Sambamurthy et al. (2003) have argued that IT plays a key role in enhancing business agility particularly in the three areas of customer, operational, and partner agility. Hence, a value must be assessed for IT’s contribution to business agility.

## 4.1. Estimating SOA Benefit Parameters—IT Productivity and Business Agility

We estimate the IT productivity benefit, or the cost savings in application development resulting from building applications as compositions or orchestrations of Web Services, by looking at public information available on the cost compression arising from application development using an SOA paradigm. OpenESB is an open-source project to build an ESB and other SOA technologies such as a DTIS, referred to as an Extract, Transform, and Load (ETL) Integrator. This open-source project reports that developing integration applications using ETL Integrator for deployment on the open-source ESB is two to five times cheaper than developing custom code.<sup>2</sup> We use this as a likely-to-optimistic range for the IT cost savings from developing SOA-based applications in our OPM. Our representative firm migrating to SOA, however, makes an allowance for the SOA naysayers camp by assuming that in the pessimistic scenario the cost savings benefit will be a tenth of that in the likely scenario.

The SOA infrastructure, together with a key set of Web Services (WS) composition and orchestration applications, provides the firm with a rich fabric of digital options (Sambamurthy et al. 2003), thus endowing the firm with business agility. Quantifying the value of IT is a difficult problem, and in this article we take the tack of looking at what some practitioners are saying about the value of business agility and the role that IT plays in it. An article at CIO.com, the online version of the highly-regarded practitioner magazine CIO, suggests that a company that is agile can improve its profits by 2%to 4% of revenue (Hugos 2007). This is also referred to as the “agility dividend.”

It must be recognized, of course, that it is not IT by itself that is creating this agility dividend. It is the employees who make decisions and perform actions on a daily basis for the firm, so it is their skills, knowledge, motivation, and training, together with the IT they use, that determine whether or not the firm quickly exploits its opportunities for competitive action. We use a simple formula (Equation (12)) for allocating the agility dividend between the IT asset and the employees, where the agility dividend attributed to IT specifically is given by

Agility Dividend from IT 4ADIT5

= <sup>-</sup>4% of Revenue Spent on IT5

$$
\left. \left/ (\% \text { of   Revenue   Spent   on   Employee   Salaries,   Benefits,   Training,   IT }) \right] \cdot (\text { Agility   Dividend }). \left. \right. \tag {12}
$$

According to Gartner, the average percentage of revenue spent by firms on IT is around 4% (Gartner 2009). Of course, the percentage of revenue spent on employee salaries, benefits, and training varies widely by the type of firm and the industry. In our model, we use 35% as the percentage of revenue spent on employee salaries, benefits, training, and IT. We thus obtain an agility dividend from IT (ADIT) that ranges from 0.2286% to 0.4572% of revenue with 0.2286% deemed a likely and 0.4572% an optimistic estimate of the ADIT. The pessimistic value for ADIT will again be assumed to be a tenth of the likely value, or 0.02286%. A firm using our OPM can of course replace any of the values used in our model such as the estimate of the agility dividend or the fraction thereof attributed to IT, or it can use the default values based on industry data that we have used.

The ADIT is deemed to be an estimate of the agility benefit stemming from the flexible SOA-based IT asset as a whole. This SOA-based IT asset, however, comprises both the SOA infrastructure, itself consisting of two meta-stages, and various WS applications layered on top of this infrastructure, and it is built over time. The ADIT is therefore further apportioned between the contributions of the infrastructure meta-stages and the applications themselves as the full, flexible SOA-based IT asset is built. As each major facet of the IT asset is built, be it an infrastructure meta-stage or a WS application, the model assumes that a pro-rated portion of the full ADIT is delivered to the firm at that time; this is referred to as the incremental agility dividend, or IAD, attributed to the major facet built. The firm thus enjoys less than the full ADIT as it is building up the complete SOA infrastructure and applications environment.

Let us assume that a firm needs to build N major WS applications to reach a fully built and flexible IT asset that can contribute the full ADIT to the firm. The IADs stemming from completing each major facet, such as a meta-stage of the SOA infrastructure or a

WS application, are given by Equations (13) and (14), respectively.

<table><tr><td>IADSOA Infrastructure Meta Stage</td></tr><tr><td>=(Investment in a Meta Stage) / (Total Investment in SOA infrastructure +N(Average Cost of WS application))·ADIT, (13)</td></tr><tr><td>IADWS application</td></tr><tr><td>=(Investment in SOA Application) / (Total Investment in SOA infrastructure +N(Average Cost of WS application))·ADIT. (14)</td></tr></table>

Although N in Equations (13) and (14) can be set by the firm, we recommend a default value of 8. The number 8 is recommended because a firm’s traditional ERP system generally has seven to eight major modules corresponding to different business functions and processes.

Since the IAD is a benefit occurring every year, the present value (PV) of this IAD annuity at the time when this annuity is created is found by discounting the IAD by the WACC (Equation (15)). Here the WACC is expressed as an annual rather than a continuously compounded rate. The time of creation of the IAD annuity for a meta-stage is assumed to be when the learnings from the last intraproject stage of that meta-stage have been fully absorbed and the building of WS applications associated with that meta-stage starts. The time of creation of the IAD annuity associated with any WS application, composition or orchestration, is when the development of that application has been completed. The present value of an IAD annuity discounted to the time of creation is

PV at creation of incremental agility dividend (IAD)

$$
\mathrm{annuity} _ {k} = \frac {\mathrm{IAD} _ {k}}{\mathrm{WACC}}\tag{15}
$$

where k = a major facet such as a SOA infrastructure meta-stage or a WS application.

## 4.2. Estimating SOA Cost Parameters

The relative cost of obtaining the IT productivity and business agility benefits of SOA is the additional investment in the SOA infrastructure elements such as the ESB, DTIS, adapters, DGS, BPMS, and portal, which is not necessary when applications are built the traditional way. We estimate the costs of these SOA infrastructure elements by looking at vendor price lists, consultant reports, and other industry information publicly available on the Internet. The IBM WebSphere<sup>3</sup> product family has a complete set of products corresponding to the various SOA infrastructure elements, and the WebSphere price list is used as a key source of information for defining the cost of the SOA infrastructure. The software license costs of the WebSphere products corresponding to the SOA infrastructure elements identified in online Appendix A are given in Table 1 (IBM 2010b). Also, as indicated in Table 1, IBM prices its software products according to processor value unit (PVU), which is a measure of the processing power of the server (IBM 2010a). Servers from IBM, HP, and Sun with a single processor core are typically rated as 100-PVU servers, whereas servers with a dual-core architecture are considered as having 200 PVUs.

Table 1 Costs of SOA Infrastructure Elements from IBM Price List

<table><tr><td>SOA infrastructure element</td><td>Product name</td><td>Software license cost</td></tr><tr><td rowspan="3">Enterprise services bus (ESB)</td><td>WebSphere ESB</td><td>$361/PVU*</td></tr><tr><td>WebSphere application server</td><td>$47.75/PVU</td></tr><tr><td>WebSphere MQ</td><td>$71/PVU</td></tr><tr><td>Data transformation and integration service (DTIS)</td><td>WebSphere data interchange</td><td>$1,030/PVU</td></tr><tr><td>Adapters</td><td>WebSphere SAP adapter</td><td>$165,000</td></tr><tr><td>Directory and governance service (DGS)</td><td>WebSphere service registry and repository</td><td>$593/PVU</td></tr><tr><td>Business process management service (BPMS)</td><td>WebSphere process server</td><td>$973/PVU</td></tr><tr><td rowspan="2">Portal</td><td>WebSphere portal server</td><td>$572/PVU</td></tr><tr><td>WebSphere portal extend</td><td>$1,500/PVU</td></tr></table>

<sup>∗</sup>PVU = processor value unit.

In some cases, deploying the infrastructure element in question may mean purchasing several different types of software licenses. For example, to set up an ESB environment, the firm needs to purchase a WebSphere MQ message broker license, which runs on a central server. In addition, a WebSphere ESB and a WebSphere Application Server license are required for each end system that will host Web Services. Similarly, setting up a fully functional portal environment requires both the Portal Server and the Portal Extend software licenses. In addition to the software licenses for the production environment, a WebSphere Application Server for Developers license has to be purchased at \$894 per developer building Web Services. Furthermore, for developers building orchestration applications to run on WebSphere Process Server, which is IBM’s BPMS offering, a WebSphere Integration Developer license has to be purchased at a cost of \$4,030 per developer.

## 5. A Simulated Case Study of SOA Migration

Using the RO model developed in §3 and the information on SOA costs and benefits in §4, we simulate the case of a mid-sized company with \$1 B in annual revenue implementing a sequential investment program to usher in SOA. Table 2 indicates the costs of each stage of the SOA investment program. We assume that dedicated servers are acquired for running infrastructure services such as the ESB message broker, DTIS, DGS, BPMS, and the portal. If an IBM Web-Sphere product is used to implement the infrastructure service, then a 200-PVU server is assumed to be acquired. The end systems on which Web Services are hosted are assumed to run on servers that already exist in the environment. It is further assumed in this scenario that 10 such end systems will host Web Services in the firm’s SOA environment.

A ballpark figure of 20% of the total solution cost per intraproject stage is used as the cost for external services and in-house personnel time for deploying the technology including training, installation, configuration, and optimization. This 20% is based on a report by Nucleus Research on deploying Hewlett Packard’s DGS solution called SOA Systinet at a major mobile phone retailer where 19% of the total cost of the solution went toward services and inhouse personnel time for deploying the technology (Nucleus Research 2008). For the adapters stage, since no infrastructure service such as a BPMS or DTIS is being deployed and personnel time for developing inhouse adapters is indicated as a separate line item, the allocation for external services is 10% of the total solution cost for that stage. The company has 20 application developers for whom development licenses are obtained for building Web Services as well as process orchestration applications that run on the BPMS.

Table 2 also indicates the times when the investments in various stages are made. The time elapsed between two consecutive investments is the interval during which the firm deploys and works with the technology to absorb it before making the decision on embarking on the next stage. This interval is generally two to three months except for the adapters stage, which because there is also parallel in-house development of adapters in addition to the acquisition of the WebSphere SAP/R3 adapter, takes a longer period of eight months in order to complete the development and absorption of this technology.

The firm builds four major WS applications, two composition and two orchestration, in a five-year window. The firm recognizes that it needs to build several more WS applications, assumed to be eight in all, or N = 8 in Equations (13) and (14), to develop a full SOA-based environment for supporting all the key business processes and functions of the firm. The firm is, however, seeking to justify its SOA investment on a mid-term planning horizon of four to five years because it does not have substantive visibility into its requirements and business conditions beyond that horizon. It also does want not to justify SOA solely on “strategic” grounds. Hence, only four WS applications about which there is tangible information in terms of the needs they are meeting are to be included in building the business case for SOA.

Table 2 Implementation Costs per Stage

<table><tr><td rowspan="2" colspan="2">Stage</td><td rowspan="3">Time t of Investing (years)</td><td colspan="6">Costs ($)</td></tr><tr><td colspan="2">Hardware</td><td colspan="2">Software</td><td rowspan="2">Services and in-house personnel ($)</td><td rowspan="2">Total (K$)</td></tr><tr><td>Meta</td><td>Intra-project</td><td>Item</td><td>Cost ($)</td><td>Item (N)*</td><td>Cost ($)</td></tr><tr><td rowspan="4">1</td><td rowspan="4">ESB</td><td rowspan="4">0</td><td rowspan="4">200-PVU server</td><td rowspan="4">20,000</td><td>WebSphere MQ (1)</td><td>14,200</td><td>115,233</td><td>576</td></tr><tr><td>WebSphere ESB (10)</td><td>361,100</td><td></td><td></td></tr><tr><td>WebSphere application server (10)</td><td>47,750</td><td></td><td></td></tr><tr><td>WebSphere application server for Developers (20)</td><td>17,880</td><td></td><td></td></tr><tr><td>1</td><td>DTIS</td><td>0.25</td><td rowspan="3">200-PVU server</td><td rowspan="3">20,000</td><td>WebSphere data interchange</td><td>206,000</td><td>56,500</td><td>283</td></tr><tr><td rowspan="2">1</td><td rowspan="2">Adapters</td><td rowspan="2">0.4167</td><td>WebSphere SAP adapter</td><td>165,000</td><td>46,111</td><td>461</td></tr><tr><td>In-house adapters</td><td>250,000</td><td></td><td></td></tr><tr><td>1</td><td>DGS</td><td>1.0833</td><td>Server for DGS</td><td>20,000</td><td>WebSphere service registry and repository</td><td>118,600</td><td>34,650</td><td>173</td></tr><tr><td rowspan="2">2</td><td rowspan="2">BPMS</td><td rowspan="2">1.5833</td><td rowspan="2">200-PVU server</td><td rowspan="2">20,000</td><td>WebSphere process server</td><td>194,600</td><td>73,800</td><td>369</td></tr><tr><td>WebSphere integration developer (20)</td><td>80,600</td><td></td><td></td></tr><tr><td rowspan="2">2</td><td rowspan="2">Portal</td><td rowspan="2">1.8333</td><td rowspan="2">200-PVU server</td><td rowspan="2">20,000</td><td>WebSphere portal</td><td>114,400</td><td>108,600</td><td>543</td></tr><tr><td>WebSphere portal extend</td><td>300,000</td><td></td><td></td></tr><tr><td colspan="8">Total program costs for building SOA infrastructure</td><td>2,405</td></tr></table>

<sup>∗</sup>N = Number of licenses where more than one is acquired.

Each application is assumed to take a team of 10 developers working for one year, and each developer’s loaded cost is \$120 K/year. Hence, each application costs \$1.2 M to build using the SOA approach, and this is also the average cost of a WS application to be used in Equations (13) and (14). However, building the application the SOA way is cheaper than the traditional way, with the proponents of SOA saying that it is two to five times cheaper. Hence, the cost savings in building the application the SOA way is assumed to be 4 times, 1 times, and 0.1 times the \$1.2 M cost of building the application using SOA under the optimistic, likely, and pessimistic scenarios, respectively. As mentioned earlier, we make the benefit in the pessimistic scenario a tenth of the benefit in the likely scenario to represent the naysayers in the SOA debate.

The first composition application begins three months after the last investment in meta-stage 1 at $t =$ 103333 years, and the second composition application is started three months after the completion of the first application. The development of orchestration applications follows a similar temporal pattern. The IT cost savings from developing applications using the SOA approach is assumed to occur as a balloon payment at the midpoint of the development time frame of the application. The firm uses an annual WACC of 18%, or, equivalently, 16.55%, assuming continuous compounding, to discount all benefits. With all these assumptions, the benefits from the SOA investment program are given in Table 3. The costs and benefits of SOA as described in this section define the base case in our analysis. Later in §6, we also perform various types of sensitivity analysis around the base case.

## 6. Results

Using Equation (11) and the cash flows in the pessimistic and optimistic scenarios as shown in Table 3, $\sigma _ { 1 }$ and $\sigma _ { 2 }$ are found to be 0.79 and 0.96. Now using the likely cash flows from Table 3, the present value $V _ { 2 }$ of the cash flows from meta-stage 2 at t = 108333 years when investing in meta-stage 2 is complete is found to be \$4,718 K. Similarly, $V _ { 1 }$ or the present value of the likely cash flows from metastage 1 at $t = 1 . 0 8 3 3$ years when the investments in meta-stage 1 have been completed is \$5,308 K. With a risk-free rate of 2% and a discount rate of 16.55% (continuous compounding), the value of the SOA investment program is then found using the Mathematica<sup>™</sup> algorithm by calling the InvestProgVal procedure as

InvestProgVal[0.02, 0.1655, {0.79, 576, 283, 461, 173, 5,308, 0, 0.25, 0.4167, 1.0833}, {0.96, 369, 543, 4,718, 1.5833, 1.8333}].

This evaluates to \$6,156 $\mathrm { K } ,$ or approximately \$6 M of net value. The Mathematica<sup>™</sup> algorithm in online Appendix D starts the evaluation from the last metastage, or meta-stage 2 in this case, and finds the value of this meta-stage using the formula of a twofold Geske compound option to be \$3,275 K. Online Appendix B provides further insight into the valuation of Geske compound options, which in general involves the solution of a system of nonlinear equations. The value of the second meta-stage of \$3,275 K is used toward subsidizing the cost of the intra-project stages in meta-stage 1, and the net value of the full SOA program is found to be \$6,156 K.

An IT project bringing about \$6 M of net value to a mid-sized company is a significant project, although perhaps of somewhat lesser import if viewed in purely economic terms than what one may have been led to believe based on the early hype around SOA and the claims for its galactic transformational impact. Still, this analysis shows that SOA is a bet that appears to be worth taking. Furthermore, because the option value of potential downstream investments, or the value of the compound option on meta-stage 2, provides a large enough subsidy to in effect eliminate all the exercise prices of the intraproject stages of the first meta-stage, it does buttress the argument about the strategic and long-term nature of the SOA investment, which is something its proponents had been claiming all along. Our model provides the economic basis for this strategic argument without resorting to nonquantitative argumentation. Furthermore, although the SNPV of the SOA program could have been increased if we had considered additional SOA projects over a 10- to 15-year time horizon, each with its IT cost savings and incremental additions to business agility, we have chosen to perform our analysis within a mid-term planning window of 4 to 5 years, which is more in keeping with the shorter time horizons of U.S. companies.

Table 3 Benefits per Meta-Stage for the Base Case

<table><tr><td rowspan="2">Meta-stage</td><td rowspan="2">Type of benefit</td><td rowspan="2">Time (years)</td><td colspan="3">Cash flow (K$)</td></tr><tr><td>Pessimistic</td><td>Likely</td><td>Optimistic</td></tr><tr><td rowspan="5">Meta-stage 1</td><td>PV of IAD annuity from meta-stage 1 infrastructure at annuity creation time</td><td>1.3333</td><td>158</td><td>1,579</td><td>3,158</td></tr><tr><td>IT cost savings in developing composition application 1</td><td>1.8333</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>2.3333</td><td>127</td><td>1,269</td><td>2,538</td></tr><tr><td>IT cost savings in developing composition application 2</td><td>3.0833</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>3.5833</td><td>127</td><td>1,269</td><td>2,538</td></tr><tr><td rowspan="5">Meta-stage 2</td><td>PV of IAD annuity from meta-stage 2 infrastructure at annuity creation time</td><td>2.0833</td><td>97</td><td>965</td><td>1,930</td></tr><tr><td>IT cost savings in developing orchestration application 1</td><td>2.5833</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from orchestration application 1 at annuity creation time</td><td>3.0833</td><td>127</td><td>1,269</td><td>2,538</td></tr><tr><td>IT cost savings in developing orchestration application 2</td><td>3.8333</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from orchestration application 2 at annuity creation time</td><td>4.3333</td><td>127</td><td>1,269</td><td>2,538</td></tr></table>

## 6.1. Sensitivity of SNPV to the Meta-Staged Structure of Investment Program

The two-meta-staged SOA program described in §3 is not the only way to migrate the firm’s IT environment to SOA. Our algorithm, which can evaluate an investment program with any number of meta-stages and any number of intraproject stages within a meta-stage, is useful in exploring different strategies for deploying SOA. To a certain extent, the deployment plan depends on the type of product offerings of the mix of vendors the firm is working with. IBM was chosen to build our simulated case not only because it is a leading vendor of hardware and software products and has a complete set of SOA products but also because it offered transparency into the pricing of its full range of products by placing its price list on its website (IBM 2010b). With many other IT vendors, access to pricing information is available only to existing or prospective customers. However, if a different mix of vendors was chosen, then the migration plan to SOA could be different. For example, if the firm chose the ESB product from Neudesic (2012), the intraproject stages of ESB and DGS deployment could conceivably be merged into one since the Neuron ESB product has much of the governance capabilities embedded into its ESB offering.

Without switching the costs in our simulated case to that of the offerings from other vendors, which is generally infeasible because of the pricing transparency issue, we can still easily simulate the effect of changing the meta-staged structure of the program by assuming we are able to obtain the ESB and the DGS as a single package priced at \$524 K including hardware, software, and services, which is about a 30% discount from the sum of the individual prices of the ESB and the DGS. We further assume that the deployment and assessment of this integrated ESB/DGS stage takes a total of four months as opposed to the six months, or three months each, that would have been necessary if the two stages were deployed sequentially, though not necessarily with one immediately following the other. We preserve other assumptions on the intervals between intraproject stages, interval between meta-stages, magnitudes of likely cash flows, and the timing of the cash flows relative to meta-stage completion times. Also, as noted towards the end of §2.2, volatility in returns is assumed invariant to changes in the meta-stage length of time, so they remain at 0.79 and 0.96 for the two meta-stages, respectively. Our valuation algorithm can now be invoked find the new SNPV of \$6,632 K by calling InvestProgVal as follows:

InvestProgVal[0.02, 0.1655, {0.79, 524, 283, 461, 5,309, 0, 0.3333, 0.5}, {0.96, 369, 543, 4,720, 1.4167, 1.6667}].

A different variation would be where the firm decides to treat the orchestration of business processes that involve humans as a separate stage in the evolution of SOA capability from that of the orchestration of business processes that involve only software and systems. Orchestrating across software systems needs the services of only a BPMS, whereas if humans were to be additionally involved in the business process then both a BPMS and a portal would be required because the human engages in the business process via the portal. BPMS-only orchestration applications can be viewed as supporting short-running processes whereas those involving human activity, such as a senior manger’s approval, are generally long-running processes as the transactions have to wait for the human’s involvement. In the new SOA migration plan, the firm after deploying the BPMS directly implements a short-running orchestration application without waiting for the portal stage to be built. If the option to deploy a portal is exercised, then the firm builds a long-running orchestration application leveraging the services of the portal. This migration plan essentially has three meta-stages, each of which leads to cash flows, with the last two meta-stages for the two different types of orchestration applications having one intraproject stage each.

With a meta-stage separation assumption of three months, the planned investment in the portal shifts to t = 200833 years, whereas all other investment times of the SOA infrastructure elements remain the same. The assumptions on the time separation of the WS applications are retained since these assumptions are driven by the availability of programmers and the

planning of a new application in a similar category after the completion of the previous application. In the three meta-stage program, work commences on the long-running orchestration application three months after completion of the short-running orchestration application. The two composition applications continue to be separated by three months. With these assumptions, the likely benefits per meta-stage are given in Table 4 and the meta-stage values $V _ { 1 } , \breve { V } _ { 2 } ,$ and $V _ { 3 }$ for the three stages are \$5,308 K, \$2,466 $\mathrm { K } ,$ and \$2,466 K, respectively. As noted previously, the optimistic and pessimistic estimates are adjusted so that the meta-stage volatilities don’t change under compression or elongation of a meta-stage. In this context, what used to be meta-stage 2 is essentially broken into meta-stages 2 and 3. Meta-stages 2 and 3 are still similar in type as they build the infrastructure for orchestration applications. Consequently, we assume that project volatilities for meta-stages 2 and 3 are both 0.96, which was the project volatility for the original meta-stage 2. Volatility for meta-stage 1 remains at 0.79. The SNPV of the modified 3-metastaged program is found using our general-purpose Mathematica<sup>™</sup> algorithm, which can be applied to any number of meta-stages. We now supply three different lists in the arguments list of InvestProgVal corresponding to the three meta-stages and find the new SNPV of \$6,499 K by calling the InvestProgVal procedure as

Table 4 Benefits per Meta-Stage with 3 Meta-Stages

<table><tr><td>Meta-stage</td><td>Type of benefit</td><td>Time (years)</td><td>Likely cash flow</td></tr><tr><td rowspan="5">Meta-stage 1</td><td>PV of IAD annuity from meta-stage 1 infrastructure at annuity creation time</td><td>1.3333</td><td>1,579</td></tr><tr><td>IT cost savings in developing composition application 1</td><td>1.8333</td><td>1,200</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>2.3333</td><td>1,269</td></tr><tr><td>IT cost savings in developing composition application 2</td><td>3.0833</td><td>1,200</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>3.5833</td><td>1,269</td></tr><tr><td rowspan="3">Meta-stage 2</td><td>PV of IAD annuity from meta-stage 2 infrastructure at annuity creation time</td><td>1.8333</td><td>390</td></tr><tr><td>IT cost savings in developing short-running orchestration application</td><td>2.3333</td><td>1,200</td></tr><tr><td>PV of IAD annuity from short-running orchestration application at annuity creation time</td><td>2.8333</td><td>1,269</td></tr><tr><td rowspan="3">Meta-stage 3</td><td>PV of IAD annuity from meta-stage 3 infrastructure at annuity creation time</td><td>2.3333</td><td>574</td></tr><tr><td>IT cost savings in developing long-running orchestration application</td><td>3.5833</td><td>1,200</td></tr><tr><td>PV of IAD annuity from long-running orchestration application at annuity creation time</td><td>4.0833</td><td>1,269</td></tr></table>

InvestProgVal[0.02, 0.1655, {0.79, 576, 283, 461, 173, 5,308, 0, 0.25, 0.4167, 1.0833}, {0.96, 369, 2,466, 1.5833}, {0.96, 543, 2,466, 2.0833}].

These two scenarios of different project structures with a different number of meta-stages or different number of intraproject stages in a meta-stage demonstrate the flexibility of our tool. This discussion is geared toward manifesting this flexibility rather than obtaining a general result on the best program structure. An organization applying our methodology and tool is expected to explore similar “what if” scenarios in its own business context to determine the best program structure for migrating to SOA.

## 6.2. Sensitivity of SOA Program SNPV to Volatility

Estimating the volatility $\sigma$ in the returns from the underlying assets has always been a matter of concern and debate in RO models (Kogut and Kulatilaka 2001, Benaroch and Kauffman 2000). We therefore test the sensitivity of the SOA program SNPV to changes in the values of $\sigma _ { 1 }$ and $\sigma _ { 2 }$ . We vary each volatility parameter over a range from a low value of 0.1 to a high of 5 and look at the percentage change in the SNPV of the SOA program relative to the SNPV obtained for the original $\sigma _ { 1 }$ and $\sigma _ { 2 }$ estimates of 0.79 and 0.96, respectively. This amounts to narrowing or widening the gap between the optimistic and pessimistic estimates of the benefits while keeping the likely estimates the same. Table 5 shows the percentage change in SNPV as the $\sigma _ { 1 }$ and $\sigma _ { 2 }$ values are varied. It is seen from Table 5 that $\sigma _ { 1 }$ has no effect on the SOA program SNPV. This is because the option value of the second meta-stage, which is used to subsidize the first meta-stage, is large enough over the entire range of variation of $\sigma _ { 2 }$ to effectively eliminate the exercise prices of the intraproject stages in the first meta-stage. It is also seen from Table 5 that a certain amount of estimation error in $\sigma _ { 2 }$ can be tolerated before the program SNPV begins to change appreciably.

Table 5 Response of SOA SNPV to Volatility

<table><tr><td></td><td colspan="3"> $\sigma_{1}$ </td></tr><tr><td> $\sigma_{2}$ </td><td>0.1 (%)</td><td>0.79 (%)</td><td>5 (%)</td></tr><tr><td>0.1</td><td>-0.10</td><td>-0.10</td><td>-0.10</td></tr><tr><td>0.5</td><td>-0.10</td><td>-0.10</td><td>-0.10</td></tr><tr><td>0.96</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2.5</td><td>5.15</td><td>5.15</td><td>5.15</td></tr><tr><td>5</td><td>12.47</td><td>12.47</td><td>12.47</td></tr></table>

## 6.3. Sensitivity of SNPV to Learning Curve Effects in SOA Build-Out

In §4.1, we had assumed a linear relationship between the extent of completion of the SOA infrastructure and applications environment and the extent of the IT-associated agility dividend, or ADIT, that flows from the completion of each major facet of the SOA infrastructure and applications environment. Each meta-stage or each WS application constitutes a major facet of the SOA infrastructure and applications environment. In this section we explore learning curve effects in the build-out of the SOA environment where the prorating of the ADIT to the SOA facets is smaller for facets completed earlier and larger for those completed later in the migration to SOA. As shown in Figure 3, we assume a nonlinear relationship between the fraction of completion of the SOA environment and the fraction of the ADIT that accrues to the firm upon reaching a major milestone in the SOA build-out such as the completion of a major facet. As the figure shows, there is initially a convex relationship that changes to a concave relationship between the fraction of ADIT that accrues to the firm and the fraction of the SOA environment built. This captures the standard form of the learning curve where initial benefits are low, then they begin to rise rapidly as the effects of learning are felt, and finally they reach a plateau (Stevenson 2009).

The initial convex portion of the learning curve before diminishing returns set in is modeled using a $y = c x ^ { 2 }$ form. This portion of the curve is assumed to encompass the facets being built in the migration plan under consideration. In order to isolate the effects of learning, we set c such that the cumulative fraction of ADIT accrued by the time the last facet in the migration plan is built is the same in the base linear and the nonlinear case. In other words, while the aggregate benefits associated with IT-driven agility have not been changed between the linear and nonlinear cases, their distribution over time has been changed to reflect learning. This assumption results in a value of c of 1.6662. The formulas for the incremental annual dividend (IAD) associated with each facet are now:

Figure 3 Learning-Curve Effects  
![](/api/attachments/D9WXZPN3/fulltext/images/5d30029ceba330c860d58ad1d0980dade91d31cff18480ddf9a59875a13b462b.jpg)

$$
\begin{array}{l} \mathrm{IAD} _ {\text {Facet} k} \\ = c \left\{\left[ (\text {Cumulative SOA Investment up to Facet} k) / (\text {Total Investment in SOA infrastructure} + N (\text {Average Cost of WS application})) \right] ^ {2} - \left[ (\text {Cumulative SOA Investment up to Facet} k - 1) / (\text {Total Investment in SOA infrastructure} + N (\text {Average Cost of WS application})) \right] ^ {2} \right\} \\ \cdot \text {ADIT}. \end{array} \tag {16a}
$$

For the first facet built, which is meta-stage 1,

$$
\begin{array}{r l} \mathrm{IAD} _ {\text { Meta   Stage   1 }} & = c \left[ (\text { Investment   in   Meta   Stage   1 }) / (\text { Total   Investment   in   SOA   infrastructure } + N \cdot (\text { Average   Cost   of   WS   application })) \right] ^ {2} \\ & \cdot \text { ADIT. } \end{array} \tag {16b}
$$

The benefits per meta-stage incorporating these learning curve effects now change from what was shown in Table 3 for the base linear case to those shown in Table 6. The chronological sequence of completion of the six key facets corresponding to the two meta-stages, two WS composition, and two WS orchestration applications is meta-stage 1, metastage 2, composition application 1, orchestration application 1, composition application $^ { 2 , }$ and orchestration application 2. We allow for the transference of learning in terms of making the corporation more agile between all of these facets. As can be seen from a comparison of Tables 3 and $^ { 6 , }$ the present values of the IAD annuities corresponding to the prorated agility dividends are smaller for the SOA facets built earlier in the migration sequence but greater for those that come later in the sequence when learning curve effects are considered. With these changes, $V _ { 1 }$ and $V _ { 2 }$ values become \$4,356 K and \$5,167 K. The fall of $V _ { 1 }$ and the rise of $V _ { 2 }$ relative to the linear base case is because in the presence of learning effects, the benefits in the earlier stages are smaller when the project is in learning mode and rise rapidly as the learning is absorbed. Given all these changes, we recalculate the volatilities ab initio using Equation (11) and find $\sigma _ { 1 }$ and $\sigma _ { 2 }$ to be 0.81 and 0.96, respectively. It is seen that the changes in volatilities are marginal. With these assumptions, the new value of SNPV of \$5,746 K is found using our tool by calling InvestProgVal as

Table 6 Benefits per Meta-Stage with Learning Curve Effects

<table><tr><td rowspan="2">Meta-stage</td><td rowspan="2">Type of benefit</td><td rowspan="2">Time (years)</td><td colspan="3">Cash flow (K$)</td></tr><tr><td>Pessimistic</td><td>Likely</td><td>Optimistic</td></tr><tr><td rowspan="5">Meta-stage 1</td><td>PV of IAD annuity from meta-stage 1 infrastructure at annuity creation time</td><td>1.3333</td><td>33</td><td>327</td><td>654</td></tr><tr><td>IT cost savings in developing composition application 1</td><td>1.8333</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>2.3333</td><td>106</td><td>1,059</td><td>2,118</td></tr><tr><td>IT cost savings in developing composition application 2</td><td>3.0833</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from composition application 1 at annuity creation time</td><td>3.5833</td><td>191</td><td>1,905</td><td>3,810</td></tr><tr><td rowspan="5">Meta-stage 2</td><td>PV of IAD annuity from meta-stage 2 infrastructure at annuity creation time</td><td>2.0833</td><td>52</td><td>522</td><td>1,044</td></tr><tr><td>IT cost savings in developing orchestration application 1</td><td>2.5833</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from orchestration application 1 at annuity creation time</td><td>3.0833</td><td>148</td><td>1,482</td><td>2,964</td></tr><tr><td>IT cost savings in developing orchestration application 2</td><td>3.8333</td><td>120</td><td>1,200</td><td>4,800</td></tr><tr><td>PV of IAD annuity from orchestration application 2 at annuity creation time</td><td>4.3333</td><td>233</td><td>2,328</td><td>4,656</td></tr></table>

InvestProgVal[0.02, 0.1655, {0.81, 576, 283, 461, 173, 4,356, 0, 0.25, 0.4167, 1.0833}, {0.96, 369, 543, 5,167, 1.5833, 1.8333}].

The reduction in the value of SNPV reflects a more realistic assumption on how quickly benefits from the agility dividend can be realized. The learning curve phenomenon essentially depresses benefits from the early stages of the build-out of the SOA infrastructure and loads them more toward the end of the investment horizon. Still, a payoff of about \$5.75 M continues to provide a solid case to start the migration toward SOA.

## 6.4. Sensitivity of SNPV and the Value of Abandonment Flexibility

RO theorists define the so-called value of managerial flexibility, which is the value associated with the flexibility that management has to change course as new information comes to light, as follows (Park and Herath 2000):

$$
\mathrm{SNPV} = \text { Passive   NPV }
$$

\+ Value of Managerial Flexibility0 (17)

In RO parlance, the traditional NPV or the NPV obtained assuming the investment program is fixed ex ante is simply referred to as the passive NPV. In the SOA context, the value of managerial flexibility essentially arises from the ability to abandon the build-out of the SOA infrastructure at any of the decision points in the program if subsequent information should prove the case for SOA to be largely unfounded. Using Equation (16) and the original costs, benefits, and $\sigma _ { 1 }$ and $\sigma _ { 2 }$ values, the value of abandonment flexibility is about 10% of the program SNPV of about \$6 M, which is a nontrivial fraction of the total value of the program.

As mentioned earlier, SOA does have its fair share of skeptics. We therefore introduce a pessimism factor P to model the SOA investment decision as seen by those who have a darker outlook toward SOA. Although the representative user made an allowance for the possibility that SOA may not succeed by making the estimate of the benefits in the pessimistic scenario a tenth of that in the likely scenario, here we model users with an even darker outlook toward SOA by reducing the cash flow estimates in all three of the pessimistic, likely, and optimistic scenarios by this factor P . $P { \mathrm { ~ i s ~ } } \leq 1$ and it multiplies all cash flows in all the three scenarios shown in Table 3. P ranges from 1 to 0.5, with the lower end capturing the mood of users considerably less sanguine about SOA’s prospects and who estimate cash flows to be half of the original estimates in all three scenarios. As shown in Figure 4, over this range of values of P, SNPV decreases from about \$6 M to about \$2 M, and the value of abandonment flexibility rises from 10% to about 18% of total SNPV. SOA remains an IT project bringing net value in excess of \$2 M, given a near- to mid-term planning horizon for a mid-sized company over a wide range of assumptions of value and risk, which does provide a reasonably good case for embarking on SOA. What must not be ignored, however, particularly by those with a darker outlook towards SOA is that as much as 18% of program value is actually tied in with retaining the flexibility to abandon the program should the misgivings about SOA prove to be true.

Figure 4 Sensitivity of SNPV and Value of Abandonment Flexibility  
![](/api/attachments/D9WXZPN3/fulltext/images/2c75d5ce60c7e34b4ba9e047488e1e1e4b6f18c97b76d8409b327c731ff03320.jpg)

In other words, managers of the SOA program must eschew falling into the familiar trap where managers actually escalate their commitment to a failing course of action (Brockner 1992).

## 7. Conclusion

In this article, we first develop a new real options model for sequential investment programs that integrates the n-fold Geske compound option model (Geske 1979) for intraproject programs and the subsidy-to-exercise price model (Benaroch et al. 2006) for interproject programs. This new RO model can be used for valuing generalized investment programs comprising meta-stages. Such generalized programs have not been treated before in RO literature. A metastaged program is characterized as being interproject at the level of the meta-stage while being intraproject within a meta-stage. We develop a general formulation of this model so that it can be used by practitioners and researchers in many other contexts and not simply the one treated in this article. Furthermore, we provide an easy-to-use software tool, which can run on the widely used Mathematica<sup>™</sup> computational platform, for finding the value of any arbitrary investment program comprising meta-stages.

The second key contribution of this article is to apply this model to a firm’s migration to a serviceoriented architecture, where we show that a firm’s SOA investment strategy is essentially an instance of a generalized program and hence can be valued using our model. Implementing SOA is clearly one of the most important challenges facing IT organizations today, given the potential of SOA to integrate the systems, applications, data, and business processes not just within the four walls of the firm but also across the extended enterprise (Erl 2006). The current industry climate toward SOA is marked with considerable confusion because there continues to be a large constituency of SOA proponents citing superlative returns from SOA while at the same time there appears to be an emerging “SOA is dead” camp with several companies that are disenchanted with SOA and are even considering abandoning it altogether (Krill 2009). It is this type of uncertainty that makes this investment scenario particularly apt for examination using our innovative RO model.

Our RO model treats the migration to SOA as a sequential investment program comprising two metastages: one for creating the IT infrastructure necessary for building Web Services composition applications and a subsequent meta-stage for building Web Services orchestration applications, with the second meta-stage leveraging the technologies deployed in the first. We simulate the case of a company migrating to SOA to provide a step-by-step illustration of how firms can implement our model. Furthermore, to make our model as realistic as possible, the data for the model have been culled from vendors’ price lists, consultant reports, open-source projects, and industry consortium reports available on the Internet. We have also accommodated diversity in the views toward the value of SOA in the manner in which the pessimistic, likely, and optimistic cash flows from SOA were estimated and through introducing a pessimism factor to simulate how companies with a darker outlook toward SOA are potentially viewing this investment decision.

Our valuation model considers both the IT cost savings stemming from the reduced development times of building Web Services composition or orchestration applications as well as the benefits of business agility that are the consequence of having a flexible IT asset. The SOA infrastructure and applications environment provide the flexibility of quickly reconfiguring existing applications or putting together new ones in response to changing business conditions. SOA can thus be viewed as providing a rich fabric of digital options that Sambamurthy et al. (2003) saw as endowing the firm with business agility. We demonstrate that under a wide range of assumptions of benefits and volatilities in the returns from the investment, SOA would be deemed a reasonably good bet to make because it is an IT project that results in \$2 M to \$6 M of net value to a mid-sized firm depending on the assumptions made. Furthermore, this value of SOA was assessed while remaining within a near- to midterm planning framework. This estimate provides a more sober and realistic view of the value of SOA as compared to what the early hype around SOA might have led one to believe, but overall it is supportive of SOA. The assumption that the stochastic nature of the SOA value process follows a GBM, which is the standard assumption made in RO models for the asset value process, is debatable; we acknowledge that this is an area that could benefit from future research.

Finally, we note that our innovative RO model for meta-staged investment programs and the Mathematica<sup>™</sup> tool we provide to the community of practitioners and researchers are completely general methodologies and tools that can be applied to evaluate any generalized investment program, not just the SOA application treated in this article.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2013.0488.

## Acknowledgments

The authors gratefully acknowledge the many constructive suggestions of the senior editor, associate editor, and two anonymous reviewers.

## References

Bardhan I, Bagchi S, Sougstad R (2004) Prioritizing a portfolio of information technology investment projects. J. Management Inform. Systems 21(2):33–70.

Benaroch M, Kauffman RJ (2000) Justifying electronic banking network expansion using real options analysis. MIS Quart. 24(2):197–225.

Benaroch M, Shah S, Jeffery M (2006) On the valuation of multistage information technology investments embedding nested real options. J. Management Inform. Systems 23(1):239–261.

Benaroch M, Jeffery M, Kauffman RJ, Shah S (2007) Option-based risk management: A field study of sequential information technology investment decisions. J. Management Inform. Systems 24(2):103–140.

Black F, Scholes M (1973) The pricing of options and corporate liabilities. J. Political Econom. 81(3):637–654.

Brockner J (1992) Escalation of commitment to a failing course of action: Toward theoretical progress. Acad. Management Rev. 17(1):39–61.

Cassimon D, Engelen PJ, Thomassen L, Van Wouwe M (2004) The valuation of a NDA using a 6-fold compound option. Res. Policy 33(1):41–51.

Dos Santos B (1991) Justifying investment in new information technologies. J. Management Inform. Systems 7(4):71–89.

Erl T (2006) Service-Oriented Architecture (SOA): Concepts, Technology, and Design (Pearson/Prentice Hall, Upper Saddle River, NJ).

Gartner (2009) IT key metrics data. Retrieved May 2, 2011, http:// www.gartner.com/technology/consulting/key\_metrics\_data.jsp#.

Geske R (1979) The valuation of compound options. J. Financial Econom. 7(1):63–81.

Hugos M (2007) A formula to measure business agility. CIO (March), http://advice.cio.com/a-formula-to-measure-business -agility?page=0%2C0.

IBM (2010a) PVU licensing for distributed software. Retrieved May 20, 2010, http://www-01.ibm.com/software/lotus/passport advantage/pvu\_licensing\_for\_customers.html.

IBM (2010b) Software online catalog Retrieved July 4, 2010, http:// www-01.ibm.com/software/info/app/ecatalog/.

Jensen K, Warren P (2001) The use of options theory to value research in the service sector. R&D Management 31(2):173–180.

Kogut B, Kulatilaka N (2001) Capabilities as real options. Organ. Sci. 12(6):744–758.

Krill P (2009) SOA gets an obituary. Infoworld (January 5), http:// www.infoworld.com/t/architecture/soa-gets-obituary-469.

Marks EA, Bell M (2006) Service Oriented Architecture—A Planning and Implementation Guide for Business and Technology (John Wiley and Sons, Hoboken, NJ).

Neudesic (2012) Neuron ESB. Retrieved June 2, 2010, http://products .neudesic.com/.

Nguyen A (2010) SOA is not dead, says IDC. NetworkWorld (March 25), http://www.networkworld.com/news/2010/ 032510-soa-is-not-dead-says.html.

Nucleus Research (2008) ROI case study—HP SOA Systinet. Available online at http://h20195.www2.hp.com/v2/GetPDF.aspx/ 4AA2-7330ENW.pdf. Retrieved January 2, 2010.

Park CS, Herath HSB (2000) Exploiting uncertainty—Investment opportunities as real options: A new way of thinking in engineering economics. Engrg. Economist 45(1):1–35.

Paxson DA (2007) Sequential American exchange property options. J. Real Estate Financial Econom. 34:135–157.

Pennings E, Serreno L (2010) A model for evaluating pharmaceutical investment opportunities under technical and economic uncertainties. ERIM Report Series ERS-2010-009-STR, Rotterdam, The Netherlands. Available online at http://hdl.handle .net/1765/18211.

Perlitz M, Peske T, Schrank R (1999) Real options valuation: The new frontier in R&D project evaluation? R&D Management 29(3):255–269.

Puschmann T, Alt R (2005) Developing an integration architecture for process portals. Eur. J. Inform. Systems 14(2):121–134.

Sambamurthy V, Bharadwaj A, Grover V (2003) Shaping agility through digital options: Reconceptualizing the role of information technology in contemporary firms. MIS Quart. 27(2): 237–263.

Stevenson WJ (2009) Operations Management, 10th ed. (McGraw-Hill Irwin, New York).

Taudes A (1998) Software growth options. J. Management Inform. Systems 15(1):165–185.

Thomassen L, Van Wouwe M (2001) The n-fold compound option. Research Paper 2001–041, Department of Mathematics and Statistics, University of Antwerp, Belgium.

Vossen G (1997) The CORBA specification for cooperation in heterogeneous information systems. Kandzia P, Klusch M, eds. Lecture Notes in Computer Science (Springer, Heidelberg, Germany), 101–115.
