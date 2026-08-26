---
otero_id: 19496
otero_key: "F7RED35K"
title: "Decision support for optimal scheduling of highway pavement preventive maintenance within resurfacing cycle"
authors: "Geoffrey Lamptey; Samuel Labi; Zongzhi Li"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for optimal scheduling of highway pavement preventive maintenance within resurfacing cycle ☆

Geoffrey Lamptey <sup>a</sup>, Samuel Labi <sup>b,</sup>⁎, Zongzhi Li <sup>c</sup>

<sup>a</sup> C3TS, PA., 901 Ponce de Leon Blvd, Ste 900, Coral Gables, FL 33134, USA

<sup>b</sup> Massachusetts Institute of Technology, E1-175, 77 Mass. Ave. Cambridge, MA 02139, USA

<sup>c</sup> Illinois Institute of Technology, Alumni Memorial Hall, Room 102A, 3201 So. Dearborn St., Chicago, IL 60616, USA

## a r t i c l e i n f o

Article history: Received 22 September 2007 Received in revised form 9 July 2008 Accepted 13 July 2008 Available online 17 July 2008

Keywords: Preventive maintenance Optimization Highway pavement Life-cycle costing

## a b s t r a c t

This paper presents a case study for optimizing decisions on the best combination of preventive maintenance (PM) treatments and timings to be applied in the resurfacing life-cycle (interval between resurfacing events), for a given highway pavement section. In the optimization procedure, the paper incorporates key infrastructure management concepts of treatment-speci<sup>fi</sup>c triggers, performance jump models, and performance trend models. Using a case study, the paper determines that optimization can be a viable tool to support scheduling decisions for highway preventive maintenance. Also, using sensitivity analysis, it is determined that changes in the resurfacing interval length and discount rate can in<sup>fl</sup>uence the choice of optimal PM schedule.

© 2008 Elsevier B.V. All rights reserved

## 1. Introduction

Preventive maintenance (PM) is increasingly being adopted by highway agencies. This practice is based on the premise that a highway asset should not be left to deteriorate up to the point were major rehabilitation is needed and that it can be bene<sup>fi</sup>cial to carry out PM in the period between major rehabilitation events. At the current time, PM planning and decision support is a critical issue as highway agencies grapple with the challenge of preserving national highway assets in the face of funding limitations, higher traf<sup>fi</sup>c loading, increased road–user expectations, and aging infrastructure.

As a <sup>fi</sup>tting prelude to this paper, it is essential to explain certain infrastructure management terms that are used in the paper. A rehabilitation life-cycle is the length of time between two consecutive rehabilitation events. At many agencies, resurfacing is a common form of rehabilitation. A pavement preventive maintenance treatment is an action that corrects minor defects, retards future deterioration, and maintains or improves the functional performance of a highway pavement without substantially increasing its structural capacity [22]. PM treatments range from relatively benign actions such as pothole patching, joint and bump grinding, etc., to shoulder-to-shoulder applications using thin bituminous coating (chip sealing, fog sealing, slurry sealing, etc.) or thick coats (such as thin hot mix asphalt (HMA) overlays, microsurfacing, etc.). Coats and overlays comprise bituminous material and aggregates that may be coarse, <sup>fi</sup>ne, or a combination thereof. A pavement family is a group of pavements that are similar in their attributes (such as surface type, design and construction features, functional class, loading levels, geographical location or climatic region, and other categorical attributes). Placing pavements into families helps pavement managers to make generally consistent management decisions for similar pavements. However, this does not obviate speci<sup>fi</sup>c actions to remedy unique and local problems for any speci<sup>fi</sup>c pavement section within a family. The following terms apply for each family and for each treatment applied to pavements in that family: a performance threshold is the minimum level of a performance at which the treatment is warranted; a performance jump is the sudden elevation of the pavement performance just after it receives a treatment; a performance trend model describes the level of performance at any given year after the treatment is applied; a PM schedule (also referred at some agencies as “PM strategy”, “PM program”, or “life cycle PM pro<sup>fi</sup>le”) is one that speci<sup>fi</sup>es application of a set of speci<sup>fi</sup>c preventive treatments and their respective timings in the interval between resurfacing events. The total cost of a PM schedule is the sum of the agency and user costs of its constituent treatments. The effectiveness or benefits of each constituent treatment is re<sup>fl</sup>ected in the jump in performance just after the treatment and the reduced rate of pavement deterioration subsequent to the treatment (manifested by a gentler slope of the performance curve). The overall bene<sup>fi</sup>t of a PM schedule (comprising multiple treatments) can therefore be measured in terms of the overall increase in pavement performance over the analysis period. This serves as a surrogate for the more visible bene<sup>fi</sup>ts of reduced costs of vehicle operations due to a smoother pavement. To avoid bias, it is useful to carry out this analysis for each of pre-de<sup>fi</sup>ned pavement families. For existing or new pavements in each pavement family, all possible alternative PM schedules (hereinafter referred to as candidates) can be established and the optimal schedule can be identi<sup>fi</sup>ed from such candidates. Also, for purposes of the present paper, “resurfacing” is de<sup>fi</sup>ned as a structural overlay of hot mix asphalt or Portland cement concrete exceeding 2-inch thickness. A life-cycle is herein de<sup>fi</sup>ned as the resurfacing interval, that is, the period of time between two consecutive treatments at least one of which is a resurfacing or higher treatment as shown in Fig. 1(a). As such, a resurfacing interval may be the period between a pavement re (construction) and subsequent resurfacing; the period between two resurfacings; or the period between resurfacing and a subsequent pavement reconstruction. Past studies have generally failed to draw a dichotomy between preventive and corrective maintenance. Unlike preventive maintenance treatments, corrective (or reactive) maintenance treatments are carried out to address speci<sup>fi</sup>c distresses as and when they occur and not in anticipation of distress, As such, they should be excluded from optimization formulations unless the formulation includes a function that predicts PM as a function of previous corrective maintenance. For this reason, corrective maintenance treatments are typically excluded from PM schedules.

As it is done for all facility preservation processes, it is necessary to plan PM activities in order to allocate future resources to meet any future need for this activity. The task of planning has generally been de<sup>fi</sup>ned as the process by which the long-term goals of an “agent” are translated into short-term tasks and objectives subject to the resource constraints facing the “agent”, and involves the generation of a sequence of temporally separated, inter-dependent decisions to be made over a period of time [5]. This is consistent with the problem faced by highway pavement engineers seeking the optimal mix of preservation treatments to apply over a given horizon period. The use of optimization in decision support systems (DSS) in sectors other than transportation has long been the subject of discussion in DSS literature [12,26,29,31]. Also, the conceptually-similar problem of selecting a portfolio of projects through decision support mechanisms in transportation has been discussed in the literature [8].

Fig. 1 presents a typical schematic for the application of pavement preservation treatments in general. During the reconstruction life cycle (period between construction events), major rehabilitation in the form of pavement resurfacing is periodically carried out to restore the structural integrity of the pavement system (Fig. 1(a)). Then, in the rehabilitation life cycle (interval between any two consecutive resurfacing events) the highway agency applies PM treatments to retard the onset of functional or structural distress and to correct minor surface defects (Fig. 1(b)). At many agencies, resurfacing is considered a standard way of pavement rehabilitation. Within the resurfacing life cycle (which is the focus of the present paper), the key question is: how does the agency decide on the most cost-effective mix of PM treatment types. In other words, which PM treatments should be carried out and in which years?

It can be realized intuitively that too frequent application of PM, while ensuring that pavement performance is consistently kept at high levels, is too costly and therefore may not be cost-effective. On the other hand, parsimonious application of PM, while offering bene<sup>fi</sup>ts of low agency cost and little workzone-related road–user disruptions, would lead to poor pavement performance thus violating minimum pavement performance standards and increasing user operating costs and user dissatisfaction. An optimal PM schedule, therefore, is one which presents a balance between the two extremes by providing the highest possible bene<sup>fi</sup>ts (in terms of pavement performance) at the least possible cost to the agency and user under given constraints. Decisions involving optimal combinations of PM treatment types and timings are therefore needed at a higher level of management to identify the most cost-effective mix of PM actions within the resurfacing life cycle and thus to justify PM investments.

![](/api/attachments/F7RED35K/fulltext/images/d6baa6cbb430bcc54640cd59a326e48b83a3a4072c1120c89f7034f480b12283.jpg)  
(a) For the Period between (Re)construction Events

![](/api/attachments/F7RED35K/fulltext/images/54c9cab63ffeae69f83c387c3f6f4f1c675fb05aa2f3a3057802aad12acc0d3f.jpg)  
(b) For the Period between Resurfacing Events  
Fig. 1. Schematic for pavement preservation scheduling for reconstruction and rehabilitation life cycles.

A review of available literature suggests that at the current time, PM scheduling decisions at most state highway agencies are established on the basis of engineers' subjective judgment and experience or/and historical practice [33] — a practice that may be de<sup>fi</sup>cient, unsystematic, and unable to yield consistent and rational PM decisions [15]. With the increasing availability of integrated pavement performance and contractual cost data in agencies' pavement databases [18], it is becoming increasingly feasible for agencies to investigate the cost and effectiveness of alternative PM practices in a more objective manner. That way, it is possible to identify and implement methodologies that yield cost-effective schedules for PM.

Optimal PM schedules are useful for pavement management decision-support because they can provide an indication of what preventive treatment is needed and when it is needed, and can thus help in estimating highway pavement monetary needs in the period between resurfacing events, in an optimal manner. Also, by adopting optimal PM practice, state highway agencies can expect the highest returns for each PM dollar invested in the period between resurfacing events. This way, decisions for such pavement investments can be made more cost-effective and defensible, and the use of taxpayer money in road preservation can be better justi<sup>fi</sup>ed.

This paper presents a case study for developing an optimizationbased DSS for highway pavement PM. The paper <sup>fi</sup>rst discusses existing decision support mechanisms for PM scheduling, identi<sup>fi</sup>es their shortcomings, and then presents an optimization-based approach for selecting optimal PM schedules. The case study is also used investigate the sensitivity of the optimal PM choice and other system outputs to changing levels of the decision support parameters.

## 2. Past and proposed approaches for pavement preventive maintenance scheduling

A review of available research publications shows that decision support for PM scheduling used in practice have been based either on the subjective judgments of pavement managers and engineers through questionnaire surveys, and/or historical data of past practice. The use of optimization-based PM decision support has seen little or no application speci<sup>fi</sup>cally in PM scheduling although optimization has been used in optimal control problems that involve resurfacing scheduling and also in generic maintenance practices. Each of the three approaches and supporting literature are herein discussed.

## 2.1. Questionnaire surveys

Questionnaire surveys solicit, for each pavement family, the expert opinions of pavement managers and engineers on best mix of PM treatments to be applied in the time interval between consecutive resurfacing events. Often, a necessary feature of such surveys is a speci<sup>fi</sup>cation of the treatment types and maximum time interval (or minimum levels of service, performance triggers or performance thresholds) at which the speci<sup>fi</sup>c PM treatments should be carried out. The triggers may be expressed in terms of aggregate measures of pavement performance (such as the International Roughness Index (IRI) or Present Serviceability Index (PSI)) or disaggregate measures (such as rutting, cracking, and faulting), or a combination of the two. At many agencies, decision criteria for PM treatments (treatment types, application intervals, and/or minimum thresholds) have evolved over many years of practice, and these expert opinions can be collated through questionnaire surveys. Details of a sample of such questionnaires can be found in the literature [15]. An advantage of questionnaire surveys is that advantage can be taken of the accumulated <sup>fi</sup>eld experience and expert knowledge of local pavement managers. Another advantage of this approach in establishing PM schedules is that it is useful at agencies that lack historical data on treatment application intervals or trigger values, or even where historical data are available, such data re<sup>fl</sup>ect past practice that may not be cost-effective. A disadvantage of the questionnaire survey approach is that the expert opinions are subjective and therefore the treatment types and timings suggested by the different pavement experts may exhibit signi<sup>fi</sup>cant variability and inconsistency. Another limitation is that it does not explicitly take advantage of any available data on key infrastructure management decision support parameters such as treatment performance jumps, application intervals, and/or post-treatment performance trends, that are increasingly being available at most highway agencies.

## 2.2. Historical pavement performance plots

Like questionnaire surveys, historical pavement performance plots can help in developing a PM schedule that is a re<sup>fl</sup>ection of, if not on the basis of, past practice. However, in this case, numerical data are involved so there is a smaller element of subjectivity. This approach involves plotting data on historical pavement performance and PM contracts over many years to determine the types of PM treatments that have been applied in the past, their application intervals, and the pavement performance at which they were applied, and then using such data to establish a PM scheduling decision support mechanism. This can be facilitated at highway agencies where speci<sup>fi</sup>c road sections in their pavement performance data<sup>fi</sup>les can be matched, using appropriate database tools, to corresponding sections in their contract data<sup>fi</sup>les. The use of historical data in establishing PM schedules (by specifying minimum-performance triggers or maximum application intervals for PM treatments) can offer a somewhat convenient way of continuing the past state of practice. However, the past state of practice may not necessarily be the most cost-effective, particularly when one recognizes that most past practice had been in<sup>fl</sup>uenced by factors as funding availability or political pressure rather than engineering or economic feasibility. For example, in times of a nationwide or statewide economic slump, an agency is more likely to adopt relatively parsimonious PM practices by using conservative trigger values or longer intervals of treatment application. On the other hand, in an auspicious economic climate, agencies are more likely to adopt relatively liberal PM practices. For these reasons, PM scheduling decision support mechanisms based solely on historical trigger values and application intervals may lead to inconsistent and indefensible pavement preservation decisions.

## 2.3. Optimization procedures

In view of the shortcomings of the questionnaire survey and historical plot approaches for pavement PM decision-support, an optimization-based DSS could offer a relatively rational and consistent method for establishing project-level PM schedules in the periods between resurfacing events. A review of pavement preservation literature review showed that the theory of optimal control has been applied in pavement management albeit with an emphasis that is different from that of the present paper. First, for some of these past studies, the focus was mostly at the network level rather than at the project level. Secondly, for the few that dealt with project-level applications focused on optimizing the rehabilitation (rather than maintenance) actions in the interval between reconstruction events (rather than the interval between rehabilitation events). Examples of the above two categories of past studies include those that solved the optimal timing of pavement rehabilitations [19], established optimal pavement resurfacing timing using the incremental bene<sup>fi</sup>t-cost technique [27], developed optimal resurfacing policy in steady state problems [16], used trend-curve approximation methods to solve the problem of optimal timings and intensity of pavement resurfacing activities [32], or used the incremental bene<sup>fi</sup>t cost approach to determine the optimal amounts of maintenance over rehabilitation life cycle at network-level [13]. Also, a dynamic network-level model has been used to allocate pavement preservation resources across several facilities over multiple time periods while minimizing overall system performance under resource availability constraints [21]. Mixed integer mathematical models have been used to develop optimal scheduling decisions for long-term facility rehabilitation (resurfacing) and replacement [1,11]. Furthermore, past research has sought to optimize rehabilitation activities using multiplicative deterioration factors to describe the change of roughness over time [7] while other studies have used genetic algorithms to investigate the pavement maintenance and rehabilitation trade-off problem at the network-level [7,24]. Obviously, the focus of most past studies has been not on the types and timings of PM within resurfacing intervals but on the intensities and timings of resurfacing within (re)construction intervals or determining optimal maintenance need at a network level.

As mentioned in one instance in the preceding paragraph, even for the few past optimization studies that dealt with highway maintenance, the framework was mostly for the system level or network level [6,14,20] rather than for the project level. Also, in most past studies, all maintenance, not just maintenance of the preventive kind, was investigated [4,12,16], thus the explicit consideration was not given to that fact that we seek to optimize only what we can control. Unlike PM, corrective maintenance is carried out reactively rather than proactively and thus should appear implicitly or explicitly as an outcome and not as a decision input in the optimization process. Thus, it can be argued that it is more useful, from a practical standpoint, to carry out maintenance optimization solely on the basis of preventive maintenance decisions as explained in the present paper. In perhaps the only past optimization study that speci<sup>fi</sup>cally addressed preventive maintenance [14], the emphasis was not on which speci<sup>fi</sup>c maintenance treatment should be applied and in what year (as in the present paper), but what optimal amount should be spent on maintenance Furthermore, unlike past studies, the present paper explicitly incorporates the concepts of performance jump, treatment triggers, and also considers workzone and non workzone user costs. Also, a number of past studies have optimized decisions for selecting a single speci<sup>fi</sup>c rehabilitation and maintenance actions for a given pavement at a given time [9,17,34] but not over the entire life of the pavement section.

With the signing of the Intermodal Surface Transportation Act of 1991 and its subsequent successor bills, highway transportation agencies have been tasked with including preventive maintenance in their asset preservation practices. As such, the philosophy of pavement preservation has shifted to one that is based on the premise that overall life cycle costs can be reduced if preventive maintenance practices can be included in long-term preservation plans. In other words, the focus is now on preventive maintenance speci<sup>fi</sup>cally and not just maintenance. Also, the interest has shifted from PM amounts needed to speci<sup>fi</sup>c PM actions, on a project-by-project basis rather than at network level. In these respects, it can be argued that the anatomical structure and objectives of the highway pavement preservation optimization problems discussed in past studies is somewhat different from those addressed in this paper. The past studies, nevertheless, offered valuable insights for the present study and were therefore reviewed in detail.

## 3. Study methodology

The framework for the optimization-based DSS approach for PM scheduling in the interval between resurfacing events (Fig. 2) consists of the following steps. First, for the subject pavement section under investigation, its pavement family is identi<sup>fi</sup>ed. Then project-level input data, analysis period, and performance and budgetary constraints (if any) are obtained or established. Then all feasible alternative PM schedules over the analysis period are identi<sup>fi</sup>ed. These are the candidate schedules. In the next step, models are obtained for estimating the sudden jump in pavement performance after receiving a given treatment and also for tracking the trend of pavement performance after it has received the treatment. If these are not readily available, they can be developed fairly easily with data that are available in most agency databases. The performance jump and trend models enable determination of the overall effectiveness, or bene<sup>fi</sup>ts, of each PM schedule. Next, the total agency and user costs for each PM schedule are established by adding the costs of the constituent treatments. Finally, optimization is carried out to identify the most cost-effective PM schedule of the candidate schedules, under given performance (and possibly, budgetary) constraints. Each step is described herein.

## 3.1. Identification of pavement family and data collection

Most agencies group their pavement sections into families on the basis of pavement surface type, traf<sup>fi</sup>c, functional class, and other categorical attributes. Such grouping is particularly useful for the analysis because certain PM treatments, by policy, are not applied to pavements of certain families. For example, chip sealing is typically not carried out on pavements on Interstate routes or pavement with high traf<sup>fi</sup>c volume. It is therefore useful to start the analysis by identifying the pavement family to which the subject pavement section belongs.

3.2. Development of models for treatment performance trends and performance jump

PM treatment performance jump and trend models describe the sudden elevation of pavement performance and the pavement deterioration trend subsequent to a speci<sup>fi</sup>c treatment, respectively. Such models enable tracking of pavement performance at each year within the resurfacing interval, thus enabling the determination of treatment effectiveness which is a vital input for the optimization-based DSS.

## 3.3. Estimation of the agency and user costs of PM treatments

Key inputs in the optimization-based DSS methodology include the agency and user costs associated with each constituent treatment of a PM schedule, as discussed below.

## 3.3.1. Agency costs

These are contractual costs of the PM treatments. For each treatment type, the cost value represents an in<sup>fl</sup>ation-adjusted average over a 5-year period, expressed per lane-mile of pavement. The costs include material, labor, equipment, and all other costs associated with the contractual agreements. The total agency cost of a PM schedule is the sum of the costs of its constituent treatments.

## 3.3.2. Non workzone user costs

This refers to the user costs during the normal highway operations (non-workzone). For each candidate PM schedule, this cost can be estimated using models. Each PM schedule has it associated expected performance model (level of condition at each year of the schedule). Then using cost-condition models that exist in the literature [30], the user cost associated with each PM schedule can be determined. The cost associated with constant-speed vehicle operation is the only component of non-workzone user costs that can be considered in this analysis because it bears a direct relationship with the pavement performance and often adequately captures the differences in the associated nonworkzone user costs across the alternative PM schedules. At some agencies, this category of user cost is assumed to be negligible because their existing road performance are generally very good and thus only small increases in performance are possible in response to any treatment — therefore there are likely to be very little differences in vehicle operation cost across the different PM schedules of those agencies.

![](/api/attachments/F7RED35K/fulltext/images/f3281492bb58a7bdd0567dbb1fadc9950d1ead16d736e5e3bb95ee93ff77cf28.jpg)  
Fig. 2. Framework for an optimization-based DSS for optimal PM scheduling.

## 3.3.3. Workzone user costs

In order to carry out PM, agencies often need to establish highway work zones to protect the maintenance workers. These workzones incur signi<sup>fi</sup>cant cost to the highway user mostly in the form of delay (which is quanti<sup>fi</sup>able) and inconvenience (which is not quanti<sup>fi</sup>able). In the present paper, the steps used for computing workzone user delay cost, which are generally consistent with established procedures [33], are presented in Fig. 3.

3.4. The optimization problem (objective function, constraints, and decision variables)

## 3.4.1. Problem formulation

The optimization-based DSS model was formulated using mathematical programming. This procedure scans all candidate PM schedules and selects that which best satis<sup>fi</sup>es the objective function (minimal total agency and user costs) and pavement performance and budget constraints over the analysis period. The decision variables, which are discrete, are as follows: (i) which treatments should be carried out, and (ii) in which year should each treatment be carried out? The objective function is shown as $\operatorname { E q . } ( 1 )$ and the constraints are presented as Eqs. (2)–(5).

Minimize:

$$
\begin{array}{l} z = \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} X _ {s t} \left\{\left(\frac {1}{(1 + i) ^ {t}} (A C _ {s t} + \beta \cdot (U C _ {s t} + U C _ {N W Z _ {t}}))\right) - \left(\frac {1}{(1 + i) ^ {T}} \cdot R S V _ {s T}\right) \right\} \end{array}\tag{1}
$$

Subject to:

$$
\sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} X _ {s t} (A C _ {s t}) \leq B\tag{2}
$$

$$
\sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} X _ {s t} > 0\tag{3}
$$

$$
\left. \begin{array}{l} \mathrm{PC} _ {s t} \leq \mathrm{PC} _ {\text { maximum }}, \text { for   Surface   roughness } \\ \mathrm{PC} _ {s t} \leq \mathrm{PC} _ {\text { minimum }}, \text { for   Rutting   and   PCR } \end{array} \right\} \begin{array}{l} s = 1, 2, 3,..., S \\ t = 1, 2, 3,..., T \end{array}\tag{4}
$$

$$
X _ {s t} = \left\{ \begin{array}{l l} 1 & \text { if   treatment   } s \text {   is   selected   in   year   } t \\ 0 & \text { otherwise } \end{array} \right. \quad \begin{array}{l} s = 1, 2, 3, \ldots , S \\ t = 1, 2, 3, \ldots , T \end{array}\tag{5}
$$

## Where

S Number of feasible PM treatments

$T$ Analysis period, i.e., the resurfacing interval or period between successive resurfacing events

$I$ Discount rate,

$X _ { s t }$ Binary variable indicating whether or not treatment s is selected in year t,

$A C _ { s t }$ Agency costs for treatment s in year t

$U C _ { s t }$ Workzone user costs associated with treatment s in year t $U C _ { N W Z t }$ Non-workzone user cost in year t

$\mathsf { R S V } _ { s T }$ Remaining service life value of the pavement (on basis of agency and user costs) at the end of the analysis period T

$\beta$ Weight assigned to user cost to re<sup>fl</sup>ect its importance relative to agency cost (A beta value of 100% re<sup>fl</sup>ects a 1:1 relative weight of agency and user cost)

B Total budget for the pavement project or section over the entire analysis period T

$\mathsf { P C } _ { s t }$ Level of pavement performance or condition after treatment s is applied in year t,

$\mathsf { P C }$ <sub>min or max</sub> Trigger value or threshold pavement performance for treatment, and

Z Objective function value corresponding to the life cycle costs of the PM schedule representing the types of treatments selected and their optimal implementation years.

## 3.4.2. Explanation of the equations for the DSS model

The objective function of the optimization-based DSS model, represented by Eq. (1) minimizes the sum of discounted PM costs over the analysis period. The sum of PM costs comprises the agency costs, user costs, and their corresponding remaining service life values at the end of the analysis period. The costs are discounted to re<sup>fl</sup>ect the timevalue of money using the standard economic analysis relationship which is known as the Single Payment Present Worth Factor (SPPWF) and is given by: $\begin{array} { r l r } {  { \frac { 1 } { ( 1 + i ) ^ { t } } . } } \end{array}$ It is worth mentioning that other formulations of <sup>ð Þ</sup>the objective function could involve a multiple criteria formulation that includes other criteria such as maximizing some utility such as pavement performance or cost-effectiveness.

![](/api/attachments/F7RED35K/fulltext/images/8a379a2091abd8c85e171d21090fdfd88417b5a9c6fcf656ff5b1ca461716e08.jpg)  
Fig. 3. Steps for calculating workzone user costs of each PM treatment (adopted from [33])

The <sup>fi</sup>rst constraint, Eq. (2), speci<sup>fi</sup>es B is the total budget for PM allocated for the analysis period. However, in contrast to that at the network level, project-level management typically does not involve a budgetary constraint. In other words, budgets are typically drawn up for an overall network of projects in a given funding period (typically 1–3 years) but hardly for a single project over any period. However, a <sup>fl</sup>exible budgetary constraint has been included in this paper's optimization methodology for the rare case where a budget exists at project-level, such as a case where a dedicated fund is allocated to a speci<sup>fi</sup>c pavement section. In such cases, a candidate PM schedule is automatically excluded from consideration if its total agency cost exceeds the budget set aside over the analysis period for that speci<sup>fi</sup>c pavement section. So, for cases where no budgetary constraint exists, the user may simply set the budgetary limit B to in<sup>fi</sup>nity. The second constraint (Eq. (3)) speci<sup>fi</sup>es that at least one PM treatment should be selected within the resurfacing interval. Eq. (4), which is the pavement performance constraint, states that the average pavement performance within the resurfacing interval, in terms of each pavement performance indicator, should not fall above or below a certain level. For example, for indicators whose values increase with time such as surface roughness and rutting, an upper bound threshold is established, and for indicators whose values decrease with time such as pavement condition rating, a lower bound threshold is established.

Eq. (5) sets the decision variable $X _ { s t }$ as a binary variable — at any given year, treatment s is either carried out or not carried out.

The explicit choice of an appropriate beta weight to re<sup>fl</sup>ect the relative importance between agency and user costs has been the bane of many researchers in the past. A review of literature shows that many past researchers simply proceeded by simply adding agency to user costs (thus implicitly assigning a beta weight of 100, that is, 1:1 ratio of importance). Very few research studies have established weights of agency and user costs speci<sup>fi</sup>cally. For example, Patidar et al. [23] references a previous study that had established a ratio of “agency cost to user cost” weights as 1:0.6286. That would translate to a beta weight of 62.86%. For purposes of illustration, the present paper adopted the 1:1 weighting assumption. But we herein mention the issue to highlight the fact that the weight is not necessarily 100%. Highways agencies seeking to establish local values of beta could follow the steps presented in DSS literature. It is worth noting that different PM schedules have different constituent PM treatments and thus different agency and user costs. As such, changing the beta value can change the choice of the optimal PM schedule.

## 3.4.3. Problem size and model solution

After all the alternative PM schedules over the analysis period have been identi<sup>fi</sup>ed, the agency and user costs associated with each schedule are computed to obtain the overall life cycle cost associated with the schedule under consideration. The PM schedule that best satis<sup>fi</sup>es the objective function and constraints is then selected as the optimal solution. In the case study provided, there are three PM activities that could be carried out and each of these could be carried out in any year of the period between successive rehabilitation events, at any frequency over the analysis period. So for a 15-year period between rehabilitation events, for example, we have a large number of possibilities. In reality, a highway agency could have more than three standard preventive maintenance treatments for its pavements. Also, the speci<sup>fi</sup>ed or preferred period between successive rehabilitation events can be longer than 15 years. As such, the problem size could take very large dimensions.

Sensitivity analysis can be carried out to examine the in<sup>fl</sup>uence of incremental changes of the DSS parameters on the analysis outcomes such as the choice of optimal solution and the overall effectiveness (average pavement performance) over the analysis period. For purposes of the present paper, the solution algorithm was implemented using a customized computer code.

The optimization framework discussed above is consistent with state-of-the-art of optimization-oriented decision support described in past DSS research [28] where model-based decision support process has been sequenced as follows: formulation of a model in the form acceptable to a model solver, algorithmic solution of the model and “what-if” analyses and interpretation of a model solution or a set of solutions.

## 4. Case study implementation of the decision-support framework

The developed framework for determining optimal PM treatment types and respective timings within resurfacing life cycle is herein illustrated using a case study involving a 5-mile, 4-lane section of US-231 highway from MP 199.86 to MP 204.86 in the Tippecanoe county of Indiana. The resurfacing interval is the period between a proposed new construction involving “New Full Depth HMA Pavement” and a subsequent major resurfacing (Functional HMA Overlay). For the case study, the following PM treatments were considered: thin HMA overlay, micro-surfacing, and crack sealing. Three pavement performance indicators were used: pavement surface roughness in terms of the International Roughness Index (IRI); Pavement Condition Rating (PCR), which is on a 0–100 scale; and rutting which has a lower bound of 0 in.

## 4.1. Description of input data for the analysis

## 4.1.1. Discount rate

Each cost occurrence for each PM scheduling alternative was discounted to present worth. A discount rate of 4%, a rate that is consistent with FHWA recommendations [33] was used.

## 4.1.2. Traffic growth rate

The annual traf<sup>fi</sup>c growth rate of 1.55% was incorporated in order to take into consideration the possible increase in AADT (and hence the truck AADT) over the resurfacing interval. Eq. (6) was used to compute the total traf<sup>fi</sup>c growth factor over the analysis period.

$$
T R = (1 + r) ^ {t}\tag{6}
$$

where TR is the total growth factor at year t from the beginning of the analysis period, r is the annual growth rate (%), and t is the pavement age or the number of years since the resurfacing event.

## 4.1.3. Data for agency cost estimation

The estimated initial construction costs for the US-231 section from MP 199.86 to 204.86 was \$324,126 per lane-mile. Unit costs (\$ per lane-mile) of preventive treatments in Year 2000 constant dollars were as follows: Asphalt Crack Sealing — \$530.32; Microsurfacing — \$23,320; Thin HMA Overlay — \$62,753. The source of this data is a previous research study on pavement preservation costing [15].

## 4.1.4. Data for user cost estimation

The following data on the value of time and the workzone characteristics used for the estimation of user cost during workzone activities on the US-231 section, were used [8,9]: Value of Time (in Year 2000 constant dollars): Passenger Cars — \$14.02, Single Unit Trucks — \$23.37, Combination Trucks — \$23.37. Workzone characteristics assumed their typical values as follows: Workzone length — 1 mile sections, Workzone Speed — 25 mph, Workzone Capacity — 1,470 passenger cars per vehicle per lane. For each PM treatment in each PM schedule, highway workzone duration models developed from an earlier pavement preservation research project [15] were used to estimate the workzone duration on the basis of the contract length.

4.1.5. Other project-specific traffic data were as follows:

\- AADT (both directions) in construction year — 10,378, Single unit truck percentage — 5%, and Combination trucks percentage — 10%, Traf<sup>fi</sup>c growth rate — 1.55%.

\- Speed limit under non-workzone conditions — 40 mph

\- Free-<sup>fl</sup>ow capacity (veh/hour/lane) — 2047, Queue dissipation capacity (vphpl) — 1800.

\- A life cycle or time interval between the two rehabilitation events (construction of a new full-depth asphaltic concrete pavement and a subsequent resurfacing using a functional HMA overlay events) is a 30-year period.

## 4.2. Results of treatment effectiveness analysis

Table 1 presents the performance trend and performance jump model results for the thin HMA overlay and microsurfacing treatments. For the performance jump models developed, it was seen that the “initial” or pre-treatment pavement performance is a signi<sup>fi</sup>cant predictor of the pavement performance jump following the treatment application: for each PM treatment, the poorer the pre-treatment pavement performance of the pavement section, the higher the performance jump. This may be attributed to the assertion that there exists a certain effectiveness “ceiling” [18], i.e., a minimum IRI or RUT value or a maximum PCR value. As such, the further the pre-treatment pavement performance is from these ceilings, the greater the potential jump to the ceiling; and the closer pre-treatment pavement performance is from these ceilings, the smaller the potential jump to reach the ceiling. This is consistent with expectation and also consistent with <sup>fi</sup>ndings of past research [18,25,32]. These <sup>fi</sup>ndings are applicable to the range of initial performance of the pavement sections considered in this study.

For the treatment performance trends (Table 1), the developed models showed that the traf<sup>fi</sup>c loading and climatic severity are signi<sup>fi</sup>cant predictors of the pavement performance after the application of each of the PM treatments: the pavement performance deteriorates with accumulated freeze index and accumulated average annual daily truck traf<sup>fi</sup>c. This is consistent with expectation. The detailed results are shown for each pavement family studied.

## 4.3. Results of the optimization analysis

The results (Fig. 4) suggest that for a 30-year resurfacing interval, the recommended optimal PM schedule for the case study pavement section is as follows:

• Apply a Thin HMA Overlay 11 years after the initial construction,

• Apply a Microsurfacing 18 years after the initial construction.

Sensitivity analyses were carried out to evaluate the effect of resurfacing intervals and other key input variables on the choice of optimal PM schedule.

Treatment performance jumps and post-treatment deterioration trend

<table><tr><td colspan="7">Treatment performance and effectiveness attributes, by performance indicator and road class</td></tr><tr><td colspan="4">Performance (Deterioration) Trend</td><td colspan="3">Performance Jump</td></tr><tr><td rowspan="3"></td><td rowspan="2" colspan="3"> $=e^{(\beta_0+\beta_2 \cdot \text{CTAADT}+\beta_3 \cdot \text{CNDX})}$ </td><td> $PJ_{IRI}=\beta_0+\beta_1 \cdot IRI_{INI}^2$  $PJ_{RUT}=\beta_2+\beta_3 \cdot RUT_{INI}+\beta_4 \cdot RUT_{INI}^2$  $PJ_{PCR}=\beta_5+\beta_6 \cdot \ln(PCR_{INI})$ </td><td colspan="2">Thin HMA overlay</td></tr><tr><td> $PJ_{IRI}=\beta_0+e^{\beta_1*IR_{INI}}$  $PJ_{RUT}=\beta_2+\beta_3 \cdot RUT_{INI}^2$  $PJ_{PCR}=\beta_4+\beta_5 \cdot \ln(PCR_{INI})$ </td><td colspan="2">Micro-surfacing</td></tr><tr><td>Surfacing Roughness (IRI)</td><td>Rutting (RUT)</td><td>Pavement Condition Rating (PCR)</td><td>IRI</td><td>RUT</td><td>PCR</td></tr><tr><td rowspan="15">Thin HMA Overlay</td><td>Interstates</td><td>Interstates</td><td>All Classes</td><td>All Classes</td><td>All Classes</td><td>All Classes</td></tr><tr><td> $\beta_0=3.89421$ </td><td> $\beta_0=-2.80903$ </td><td> $\beta_0=4.59508$ </td><td> $\beta_0=48.6113$ </td><td> $\beta_2=0.164456$ </td><td> $\beta_5=312.393$ </td></tr><tr><td> $\beta_1=0.19541$ </td><td> $\beta_1=0.56123$ </td><td> $\beta_1=-0.031125$ </td><td> $\beta_1=0.00191$ </td><td> $\beta_3=-1.01808$ </td><td> $\beta_6=-68.1003$ </td></tr><tr><td> $\beta_2=4.89084$ </td><td> $\beta_2=3.69545$ </td><td> $\beta_2=-0.38430$ </td><td> $R^2=0.71$ </td><td> $\beta_4=3.86284$ </td><td> $R^2=0.54$ </td></tr><tr><td> $R^2=0.7$ </td><td></td><td> $R^2=0.53$ </td><td></td><td> $R^2=0.51$ </td><td></td></tr><tr><td>Non-Interstate NHS</td><td>Non-Interstates</td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_0=3.90121$ </td><td> $\beta_0=-2.50491$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_1=0.26817$ </td><td> $\beta_1=0.53949$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_2=5.33110$ </td><td> $\beta_2=4.27811$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $R^2=0.43$ </td><td> $R^2=0.49$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Non-NHS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_0=3.90121$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_1=0.26817$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\beta_2=5.33110$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $R^2=0.43$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">Micro-surfacing</td><td>All Classes</td><td>All Classes</td><td>All Classes</td><td>All Classes</td><td>All Classes</td><td>All Classes</td></tr><tr><td> $\beta_0=4.14001$ </td><td> $\beta_0=-5.23365$ </td><td> $\beta_0=4.57867$ </td><td> $\beta_0=11.4995$ </td><td> $\beta_2=0.03002$ </td><td> $\beta_5=277.285$ </td></tr><tr><td> $\beta_1=0.28832$ </td><td> $\beta_1=0.56963$ </td><td> $\beta_1=0.03012$ </td><td> $\beta_1=0.01874$ </td><td> $\beta_3=2.48055$ </td><td> $\beta_6=-49.1877$ </td></tr><tr><td> $\beta_2=7.05754$ </td><td> $\beta_2=4.56272$ </td><td> $\beta_2=-0.58413$ </td><td> $R^2=0.42$ </td><td> $R^2=0.52$ </td><td> $R^2=0.43$ </td></tr><tr><td> $R^2=0.56$ </td><td> $R^2=0.55$ </td><td> $R^2=0.60$ </td><td></td><td></td><td></td></tr></table>

Notes:  
PC — value of the pavement performance indicator (IRI, RUT or PCR) for a pavement section in a given year, CTAADT — cumulative average annual daily truck traf<sup>fi</sup>c (in millions) experienced by the pavement section from time of treatment to the given year, CNDX — cumulative annual freeze index (in thousands) experienced by the pavement section from time of treatment to the given year.  
PJ , PJ and PJ — Performance jump in terms of IRI, RUT and PCR respectively.  
IRI , RUT , and PCR — Pre-treatment levels of pavement roughness (IRI), rut depth (RUT) and pavement condition rating (PCR) respectively. $\beta _ { 0 } , . . . , \beta _ { N } .$ — estimated coef<sup>fi</sup>cients for the model variables.

<table><tr><td colspan="2">Parameters</td><td colspan="2">Summary</td></tr><tr><td>Resurfacing Interval</td><td>= 30 years</td><td>Year 11</td><td>- Carry out Thin HMA Overlay (1.5&quot;)</td></tr><tr><td>Discount Rate</td><td>= 4%</td><td rowspan="2">Year 24</td><td rowspan="2">- Carry out Microsurfacing</td></tr><tr><td>Traffic Growth Rate</td><td>= 1.55%</td></tr></table>

![](/api/attachments/F7RED35K/fulltext/images/13e7102e1aa72589cc3aac6e78f42fb08d5461fbd2185c9dea5b78a2119647e3.jpg)

![](/api/attachments/F7RED35K/fulltext/images/2b10d66a4e1362e6ffb6eac3976acaf5484485e1efeb3c5855797a9746d22c0b.jpg)

![](/api/attachments/F7RED35K/fulltext/images/2956ebbf057ef9108949d794beeee0b9fb722821ebc680e7ac854f609c5550b6.jpg)

<table><tr><td colspan="3">Summary of Costs</td></tr><tr><td>Item</td><td>Present Worth</td><td>EUAC</td></tr><tr><td>Agency Costs</td><td>$4,418,399.09</td><td>$255,516.46</td></tr><tr><td>User Costs</td><td>$8,113,903.02</td><td>$469,227.82</td></tr><tr><td>Total Costs</td><td>$12,532,302.11</td><td>$724,744.27</td></tr><tr><td colspan="3">Maximum IRI = 226.1 in/mileMaximum RUT = 0.79 inchesMinimum PCR = 82.56 units</td></tr></table>

Fig. 4. Optimal results for the case study.

## 4.4. Results of the sensitivity analysis

4.4.1. Effect of resurfacing interval on the choice of optimal PM schedule The objective of the present study is to determine optimal schedules for PM within resurfacing events and not to determine optimal resurfacing schedules within reconstruction events. However, results of the sensitivity analysis offers valuable insights that could probably aid in establishing recommendations for the latter. The optimization-based DSS procedure was repeated for various resurfacing intervals ranging from 20 to 35 years in 5-year increments. A discount rate of 4% and a traffic growth rate of 1.55% were used. The results showed that for the different resurfacing intervals, different solutions (optimal PM schedules) are obtained. For the 20-year resurfacing interval, it was determined that the optimal schedule is a Microsurfacing treatment after 11 years. For the 25-year resurfacing interval, the optimal schedule is a Thin HMA Overlay 11 years after initial construction. For the 30-year resurfacing interval, the recommended optimal PM schedule is a Thin HMA Overlay after 11 years and a Microsurfacing treatment in the 18th year. For the 35-year resurfacing interval, the optimal schedule is a Thin HMA Overlay after 11 years and Microsurfacing treatment in the 23rd and 30th years.

4.4.2. Effect of resurfacing interval on life-cycle cost of optimal PM schedule

Fig. 5a shows the sensitivity of life-cycle cost (agency and user costs) to the length of the resurfacing interval. Each data point in the plot corresponds to an optimal schedule, with its coordinates as the resurfacing interval and cost. The plots show that as the length of the resurfacing interval increases, the agency cost of the optimal PM schedule decreases, the user cost of the optimal PM schedule does not change signi<sup>fi</sup>cantly, and the total life cycle cost of the optimal PM schedule decreases. In other words, the optimal schedule for longer resurfacing intervals seem to have lower total cost than the optimal schedules for shorter resurfacing intervals. Therefore, on the basis of agency and user costs alone, this trend seems to suggest that the subsequent major resurfacing in the form of a functional or structural overlay could be deferred inde<sup>fi</sup>nitely. However, this conclusion is not necessarily valid if other performance criteria such as pavement performance are explicitly taken into consideration. This issue is investigated in the next section of this paper.

![](/api/attachments/F7RED35K/fulltext/images/7172da32a39400dc34f13b2bf069003b508d904cb3b0926b26e43db630b4562c.jpg)

![](/api/attachments/F7RED35K/fulltext/images/9348eff63ad56b8946198014f26e32d6e1e760a66134b85cc31634fd755074c2.jpg)

![](/api/attachments/F7RED35K/fulltext/images/1dd658571fd632cc5701522acbde3c706a1a757167adabc997027de74beaefcc.jpg)  
Fig. 5. Sensitivity analysis

## 4.4.3. Effect of resurfacing interval on pavement performance

A plot of the overall pavement performance associated with each optimal PM schedule and the resurfacing intervals (Fig. 5b) shows that that the optimal PM schedules for longer resurfacing intervals yield pavement performance that are signi<sup>fi</sup>cantly higher than those for shorter resurfacing intervals: the maximum pavement roughness decreases from 227 in./mi for a 20-year resurfacing interval to a minimum of 197 in./mi for a 25-year resurfacing interval and then increases to 241 in./mi for a 35-year resurfacing interval. For the various alternative sets of resurfacing interval and corresponding optimal PM policy, the best pavement performance is attained when the resurfacing interval is 25 years (Fig. 5b). This seems to suggest that for the family of road sections represented in the case study (that is,

Non-Interstate NHS Highways) the optimum time between construction and the <sup>fi</sup>rst resurfacing event is 25 years.

## 4.4.4. Effect of discount rate on the choice of optimal PM schedule

For different discount rates (2%, 4%, 6%, and 8%) optimal PM schedules were determined. The results showed that at low discount rates, increasing the discount rate did little to change the choice of PM schedule. However, at relatively higher discount rates, even marginal changes in the discount rate are found to cause signi<sup>fi</sup>cant shifts in the choice of optimal PM schedule.

Speci<sup>fi</sup>cally, it was shown that for discounts rates of 2% and 4%, the optimal PM schedule is a Thin HMA Overlay after 11 years and microsurfacing after 24 years after the initial construction. The scenario with a 6% discount rate yields a similar solution, the only difference being a deferment of the Microsurfacing treatment by one year. For an 8% discount rate, the optimal solution is to apply Microsurfacing treatments 10, 18 and 25 years after the initial construction.

A plot of life-cycle costs versus discount rate for each optimal PM schedule (Fig. 5c) shows that as discount rate increases, the agency cost component of life-cycle cost decreases gently while the user cost component declines rapidly. This observation suggests that compared to agency cost, user cost is more sensitive to changes in the discount rate. The net effect is that overall life cycle cost of the optimal PM schedule generally decreases with increasing discount rate.

## 5. Concluding remarks

This paper focused speci<sup>fi</sup>cally on preventive maintenance schedule optimization, in other words, selecting the best combination of preventive treatment types and timings over an analysis period. Using a case study, the paper demonstrated that optimization-based DSS is feasible for developing rational and consistent PM schedules in the interval between resurfacing events. In the case study, interesting relationships were observed: the length of resurfacing interval signi<sup>fi</sup>cantly affects the choice of optimal PM schedule and consequently, the pavement performance over its life-cycle. It was also observed that the optimal PM schedules for longer resurfacing intervals yield pavement performance that are signi<sup>fi</sup>cantly higher than those for shorter resurfacing intervals. Also, it was determined that the optimal PM schedule is in<sup>fl</sup>uenced by the discount rate used for the analysis. For lower discount rates, the choice of optimal PM schedule was fairly consistent across discount rate values. For higher discount rates, however, the choice of optimal schedule differs considerably with incremental changes in the discount rate. Furthermore, the study results seem to suggest that compared to agency costs, user costs are more sensitive to changes in the discount rate. As such, during data preparations analysis involving life-cycle costing, it may be worthwhile to develop appropriate discount rate probability distributions for use in the analysis, and also to pay greater attention to address issues of data accuracy and data variability of user cost variables.

There is an open forest of inquiry yet to be explored in this respect. First, future work could explore the extent of optimality to be gained by using of the optimization-based decision support system (OB-DSS) instead of the existing traditional approaches of expert judgment and historical plots. In other words, by how much (in terms of reduced agency cost or enhanced pavement performance) can the agency expect to gain by adopting the OB-DSS instead of the decisions based on purely expert knowledge only or historical practice only. Such validation of the OB-DSS could follow the recommendation made in past studies for DSS validation [3]. Future studies could also include the merging of the past experience and knowledge acquired by pavement experts over the years with optimization tools to yield PM schedules based on both knowledge management and optimization.

[6] FHWA, Highway economic requirements system (HERS), Technical Report, Federal Highway Administration, U.S. Department of Transportation, 2000.

In this respect, past research <sup>fi</sup>ndings for integrating decision support and knowledge management processes could be utilized [2,10]. Furthermore, the optimization problem for PM scheduling could be formulated and solved within the framework of a multiple criteria decision-making problem. To that end, the objective function could include other performance criteria such as pavement condition enhancement, facility vulnerability reduction, or network contribution effects, etc. Also, the constraints could be increased to include statements relating to the expanded list of performance measures. Finally, the PM treatments could be increased to cover a wider range of treatments actually used in practice, and this could be done separately for all types of highway pavements — <sup>fl</sup>exible, rigid, and composite.

## Acknowledgements

The authors of this paper are grateful to Kumares C. Sinha, Director of the Joint Transportation Research Program, which is administered by the Indiana Department of Transportation and Purdue University, for supporting the research project that spawned this work. The research presented in this paper is not a part of that project. The authors also acknowledge the assistance of various INDOT personnel in making data available and also in providing their perspectives on various aspects of the study.

The contents of this paper re<sup>fl</sup>ect the views of the authors, who are responsible for the facts and the accuracy of the data presented herein. The contents do not necessarily re<sup>fl</sup>ect the of<sup>fi</sup>cial views or policies of the Federal Highway Administration or the Indiana Department of Transportation, nor do the contents constitute a standard, speci<sup>fi</sup>cation, or regulation.

## References

[1] K.M. Al-Subhi, D.W. Johnston, F. Farid, A resource constrained capital budgeting model for bridge maintenance, rehabilitation and replacement, Transportation Research Record 1268 (1990).

[2] N. Bolloju, M. Khalifa, E. Turban, Integrating knowledge management into enterprise environments for the next generation decision support. Decision Support Systems, 33 (2002) 163–176.

[3] D. Borenstein, Towards a practical method to validate decision support systems, Decision Support Systems 23 (1998) 227–239.

[4] M.I. Darter, R.E. Smith, M.Y. Shahin, Use of life-cycle costing analysis as a basis for determining the cost-effectiveness of maintenance and rehabilitation treatments for developing a network level assignment procedure, Procs., North American Pavement Management Conference, Toronto. 1987

[5] S. Dutta, Decision support for planning, Decision Support Systems 12 (1994) 337–353.

[7] T.L. Friesz, J.E. Fernandez, A model of optimal transport maintenance with demand responsiveness, Transportation Research 13B (1979): T.F. Fwa, W.T. Chan, C.Y. Tan, Genetic algorithms programming of road management and rehabilitation, ASCE Journal of Transportation Engineering 122 (3) (1996).

[8] F. Ghasemzadeh, N.P. Archer, Project portfolio selection through decision support, Decision Support Systems 29 (2000) 73–88.

[9] R.G. Hicks, K. Dunn, J.S. Moulthrop, Framework for selecting effective preventive maintenance treatments for <sup>fl</sup>exible pavements, Transportation Research Record, Transportation Research Board, vol. 1597, National Research Council, Washington, D.C., 1997.

[10] C.W. Holsapple, Knowledge management support of decision making, Decision Support Systems 31 (2001) 1–3.

[11] T.L. Jacobs, Optimal long-term scheduling of bridge-deck replacement and rehabilitation, ASCE Journal of Transportation Engineering 118 (2) (1992)

[12] P. Korhonen, J. Wallenius, A multiple objective linear programming decision support system, Decision Support Systems 6 (1990) 243–251.

[13] S. Labi, K.C. Sinha, Life-cycle evaluation of pavement preventive maintenance, ASCE Journal of Transportation Engineering 131 (10) (2005) 744–751.

[14] S. Labi, K.C. Sinha, Effectiveness of maintenance and its impact on capital expenditures, JTRP Final Report, FHWA/IN/JTRP-2002/27, Purdue University, West Lafayette, Oct. 2002.

[15] G. Lamptey, Optimal Scheduling of Pavement PM using Life Cycle Cost Analysis, MS Thesis, Purdue University, West Lafayette, Indiana, (2004).

[16] Y. Li, S. Madanat, A steady-state solution for the optimal pavement resurfacing problem, Transportation Research, Part A 36 (2002).

[17], LP Mahoney NU. Ahmed RI. Iytton Optimization of pavement rehabilitation and maintenance by use of integer programming Transp. Res. Record vol, 674 1978.

[18] M. Markow, Life-cycle costs evaluations of effects of pavement maintenance, Transportation Research Record No. 1276, Transportation Research Board, Washing ton, D.C., 1991.

[19] M. Markow, W. Balta, Optimal rehabilitation frequencies for highway pavements, Transportation Research Record No. 1035, Transportation Research Board, National Research Council, Washington, D.C., 1985.

[20] G. Morcous, Z. Lounis, Maintenance optimization of infrastructure networks using genetic algorithms, Automation in Construction 14 (1) (2005) 129–142.

[21] K. Murakami, M.A. Turnquist, A dynamic model for scheduling maintenance of transportation facilities, Procs., Transportation Research Board 64th Annual Meeting, Washington, D.C., 1985.

[22] L.G. O'Brien, NCHRP synthesis of highway practice 153: evolution and bene<sup>fi</sup>ts of preventive maintenance strategies, Transp. Res. Board, National Research Council, Washington D.C. 1989

[23] V. Patidar, S. Labi, K.C. Sinha, P. Thompson, Multi-objective optimization for bridge management systems, NCHRP Report 590, Transportation Research Board, 2007.

[24] C. Pilson, R.W. Hudson, V. Anderson, Multi-objective optimization in pavement management using genetic algorithms and ef<sup>fi</sup>cient surfaces, Presented at Transportation Research Board 79th Annual Meeting, Washington. Washington D.C., 1999.

[25] A.S. Rajagopal, K.P. George, Pavement maintenance effectiveness, Transportation Research Record 1276 (1991).

[26] A. Roy, From what if to what's best in DSS, Decision Support Systems 3 (1987) 27–35

[27] M.Y. Shahin, S.D. Kohn, R.L. Lytton, M. McFarland, Pavement M&R budget optimization using the incremental bene<sup>fi</sup>t–cost technique, Procs., North American Pavement Management Conference, Toronto, Ontario, 1985.

[28] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[29] I.S. Singh, S. Sadagopan, A support system for optimization modelling, Decision Support Systems 3 (1987) 165–178.

[30] K.C. Sinha, S. Labi, Transportation Decision Making — Principles of Project Evaluation and Programming, Wiley and Sons, 2007, pp. 167–168.

[31] J. Siskos, D.K. Despotis, A DSS oriented method for multiobjective linear programming Problems, Decision Support Systems 5 (1989) 47–55.

[32] K. Tsunokawa, J.L. Schofer, Trend curve optimal control model for highway pavement maintenance: case study and evaluation, Transportation Research 28A (1994).

[33] J. Walls III, M. Smith, Life cycle cost analysis in pavement design — interim technical bulletin, Report No. FHWA-SA-98-079, Fed. Hwy. Admn. U.S. Department of Transportation, 1998.

[34] K.A. Zimmerman, ERES consultants, Inc., NCHRP synthesis of highway practice 222: pavement management methodologies to select projects and recommend preservation treatments, Transportation Research Board, National Research Council, Washington, D.C., 1995.

![](/api/attachments/F7RED35K/fulltext/images/e455a9ba012b4675e407486b9dd85bdbafcf93b12e58b4b3ca0e85ee700f7918.jpg)

Geoffrey Lamptey, P.E., is a Project Engineer working with C3TS, PA an engineering consulting <sup>fi</sup>rm in Coral Gables, Florida. He graduated from the University of Science and Technology, Kumasi, Ghana, with a B.S. Degree (Civil Engineering) in 2001. In 2004, he completed his M.S. Program (Transportation Infrastructure Systems) at School of Civil Engineering, Purdue University, West Lafayette, Indiana, USA. He has 5 years of active experience in the research and practice of civil and transportation engineering. He has recently been involved in the engineering analysis and design of complex highway interchange systems to ease the persistent congestion during peak hours in the Miami and Orlando areas in Florida. His research interests include pavement management, optimiza

tion of transportation infrastructure systems, traf<sup>fi</sup>c operations and the operational effect of geometric designs on high speed urban highways. He has published 7 papers in conference proceedings and journals such as the Journal of Transportation Engineering of the American Society of Civil Engineers (ASCE) and the Transportation Research Record of the Transportation Research Board (TRB).

![](/api/attachments/F7RED35K/fulltext/images/d6ce2c3f0b51cba18faa448b1ea513ba83086d789ccc0cf1bc3f1911debb5692.jpg)

Samuel Labi. Ph.D. is an Assistant Professor at Purdue University where he received his doctoral degree in 2001. His awards include the 2002 Milton Pikarski Award for best national Ph.D. dissertation in transportation engineering, the 2007 Mather Award for best paper in concrete materials awarded by the American Society of Testing and Materials and the 2008 Woods Award for the best paper in design and construction awarded by the Transportation Research Board. He has taught and carried out research in Massachusetts Institute of Technology's School of Civil and Environmental Engineering, and Center for Technology, Policy and Industrial Development as a visiting scholar. He is a member of the American Society of Civil Engineers, Institute of Transporta-

tion Engineers, American Planning Association, and the American Association for the Advancement of Sciences. Dr. Labi is the co-author of a book titled: Transportation Decision-making — Principles of Project Evaluation and Programming, published by Wiley and Sons. Also, he has also published over 50 articles in journals, conference proceedings, and book chapters.

![](/api/attachments/F7RED35K/fulltext/images/4b4d49b84549d7c6168360a78c472dfe9c7a214c395796d705f440272ac080e6.jpg)

Zongzhi Li, Ph.D., is an Assistant Professor in the Department of Civil, Architectural, and Environmental Engineering at Illinois Institute of Technology and is directing the Transportation Engineering Program and the Infrastructure Engineering and Management Program. He is a graduate of Purdue University (M.S.C.E., 2000; M.S.I.E., 2002; Ph.D., 2003). He authored or co-authored seven refereed technical publications and two refereed book chapters, and developed two software packages. He was recipient of the International Road Federation Fellowship in 1998 and the Charles V. Wootan Award by the U.S. Council of University Transportation Centers. He is a member of American Association of Engineering Education, American Railway Engineering and

Maintenance of Way Association, American Society of Civil Engineers, Institute of Transportation Engineers, and Institute for Operations Research and the Management Sciences.
