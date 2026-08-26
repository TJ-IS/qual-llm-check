---
otero_id: 5638
otero_key: "BKX9BFEK"
title: "How much to spend on flexibility? Determining the value of information system flexibility"
authors: "Franz Schober; Judith Gebauer"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How much to spend on <sup>fl</sup>exibility? Determining the value of information system <sup>fl</sup>exibility

Franz Schober <sup>a</sup>, Judith Gebauer <sup>b,</sup>⁎

<sup>a</sup> Institute of General Economic Research, University of Freiburg, Germany

<sup>b</sup> Department of Information Systems and Operations Management, University of North Carolina Wilmington, 601 S. College Road, Wilmington, NC 28403-5611, USA

## a r t i c l e i n f o

Article history: Received 15 December 2009 Received in revised form 13 January 2011 Accepted 17 March 2011 Available online 25 March 2011

Keywords: Information system <sup>fl</sup>exibility Information system economics Risk analysis Decision tree analysis Real option analysis Simulation experiment

## a b s t r a c t

Upon the initiation of an information system (IS), decision makers typically have a choice between different levels of <sup>fl</sup>exibility, that is the extent to which the IS can be modi<sup>fi</sup>ed or upgraded during its subsequent lifetime. In the current paper, we regard IS <sup>fl</sup>exibility as an option that is available to the decision maker, and demonstrate several approaches to determine its value. Extending a previous theory of IS <sup>fl</sup>exibility, we calculate the value of <sup>fl</sup>exibility by applying decision tree analysis (DTA), real option analysis (ROA), and explicit risk assessment based on simulation experiments. We <sup>fi</sup>nd that the deterministic treatment of IS <sup>fl</sup>exibility tends to underestimate its value, whereas ROA can overestimate its value, in particular in low-risk situations. Our <sup>fi</sup>ndings highlight the need for the concrete measurement of IS <sup>fl</sup>exibility.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

In a world of increasing uncertainty, the ability to utilize resources in a <sup>fl</sup>exible way plays an important role for managerial decision making [14,20]. The need for <sup>fl</sup>exibility applies to many corporate assets, including capital investments [7,44]; employees and business partners [3]; organizational structures and processes [31,41]; and information systems (IS) [6,8]. The formulation and implementation of ef<sup>fi</sup>cient IS <sup>fl</sup>exibility strategies have become important aspects of risk management [33,35], whereby scholars have also analyzed the often contradictory effects of IS on organizational <sup>fl</sup>exibility and ef<sup>fi</sup>ciency [1,35], and on various aspects of usability [40]. In the current paper, we focus on the <sup>fl</sup>exibility of an information system (IS), as the extent to which the IS can be modi<sup>fi</sup>ed or upgraded during its entire lifetime following initiation. More speci<sup>fi</sup>cally, we are interested in assessing the value of IS <sup>fl</sup>exibility.

Upon the initiation of an IS, decision makers often have a choice between different levels of IS <sup>fl</sup>exibility, which means that <sup>fl</sup>exibility can be viewed as an option that is available to the decision maker. Even though there is some agreement that <sup>fl</sup>exibility adds to system complexity [17,34,40], and thus comes at a price [13,27], scholars of <sup>fl</sup>exibility typically focus on various attributes and design parameters of <sup>fl</sup>exible assets but are less concerned with the economics of <sup>fl</sup>exibility [36]. In contrast, questions regarding the economic value of <sup>fl</sup>exibility have been included in recent approaches of decision theory and <sup>fi</sup>nancial analysis but not necessarily IS.

Traditional methods to determine the value of an investment, such as net present value (NPV), are often based on discounted cash <sup>fl</sup>ow analysis (DCF) in a deterministic setting. If at all, risk is included in DCF models only indirectly via the selection of an appropriate discount rate for <sup>fi</sup>nancial assets. The risks associated with investment decisions in general, and investments in <sup>fl</sup>exible assets in particular are included in newer approaches, such as decision tree analysis (DTA), real options analysis (ROA), and explicit risk analysis via simulation experiments.

Scholars of DTA enumerate the various choices of an investment and the various corresponding environmental states to <sup>fi</sup>nd the optimal investment decision [9], whereby it is required to estimate the probabilities of occurrence for each environmental state. In contrast, scholars of ROA capture risk by constructing an equivalent set of options that ensure the same outcome for different environmental states. Called hedging, the technique does not require explicit probability estimates for the various environmental states [2,9,43]. As a general concept of investment evaluation, ROA has become an important lens to establish the value of <sup>fl</sup>exibility for organizations [10], business processes [5], and IS [4,15,16,26,37,39,42]. However, while there is agreement among scholars regarding the advantages of DTA and ROA over traditional approaches to evaluate <sup>fl</sup>exibility, concrete methods of how to determine the value of IS <sup>fl</sup>exibility in speci<sup>fi</sup>c cases are lacking, which is the focus of the current paper.

We build on previous research most notably a formal model to evaluate the impact of different IS <sup>fl</sup>exibility strategies on the cost ef<sup>fi</sup>ciency of business processes [19]. The model determined the costef<sup>fi</sup>cient mix of well-described IS <sup>fl</sup>exibility strategies for a speci<sup>fi</sup>c combination of business process characteristics. A follow-up case study identi<sup>fi</sup>ed a number of practical shortcomings of the original model [18] in particular associated with the characteristics of the IS development process and the dynamics of IS utilization [17,22]. These shortcomings will be addressed in our model formulation, however the main contribution of the current paper is the presentation and comparison of several speci<sup>fi</sup>c approaches to calculate the economic value of IS <sup>fl</sup>exibility. We emphasize <sup>fl</sup>exibility-to-change, that is the extent to which an IS can be modi<sup>fi</sup>ed and upgraded in response to future requirements [19].

In the following, we <sup>fi</sup>rst calculate the value of IS <sup>fl</sup>exibility for a deterministic base case [18,19]. We then relax the deterministic condition and introduce DTA and ROA for the case of uncertain business process loads (volume uncertainty). Subsequently, we include a number of additional stochastic parameters, as we demonstrate compound ROA and explicit risk assessment based on simulation experiments. After comparing the results of the different measurement techniques, we summarize our results and review the importance to determine the value of IS <sup>fl</sup>exibility in non-deterministic settings.

An earlier version of the current paper has been presented at the Americas Conference on Information Systems 2009 [38]. It differs from the current version particularly in the treatment of the simulation experiments where we now apply beta distributions for the model parameters instead of truncated normal distributions. The beta distributions are not only more appropriate from a theoretical point of view [25], but also yield in an interesting comparison with the results of ROA.

## 2. An economic model to assess the impact of IS <sup>fl</sup>exibility strategies on business process ef<sup>fi</sup>ciency

Many researchers before us have applied formal modeling approaches, including ROA, to the development and management of IS projects, and have considered various risk factors: for example, the authors of an early study suggested the use of ROA to evaluate IS projects, and applied their methodology to evaluate expansion strategy decisions in the context of electronic banking networks [4]. Others have studied the dynamics of grid computing from an economic perspective: to account for the large amount of uncertainty in prices and demand that is associated with the provision of grid computing services, the authors built their formal decision model on a combination of ROA and Monte Carlo simulation [47]. Yet another group of IS scholars developed and applied a methodology to support the selection of implementation strategies for IS infrastructure projects that is based on a combination of ROA and multi-attribute decision making using Dempster–Shafer belief functions [22]. In contrast with many other studies, the authors speci<sup>fi</sup>cally calculated the risks and bene<sup>fi</sup>ts for a representative case study. Bayesian belief networks have also been used to support IT implementation decisions, including “what-if” analyses [28]. Complementing the earlier research studies, we seek to specify the value of IS <sup>fl</sup>exibility in support of a particular business process.

## 2.1. Model overview

A business process is commonly viewed as a set of related activities designed to produce a speci<sup>fi</sup>c output, such as budget decision making, or procurement [12]. For our purpose, we conceptualize two structural layers of a business process: (1) “Process tasks” refer to the different functionalities that a business process implies, such as the purchase of of<sup>fi</sup>ce furniture, of<sup>fi</sup>ce material, or company cars in a general purchasing process. (2) “Process activities” correspond with a single event that occurs as part of the business process, such as a request to purchase a particular of<sup>fi</sup>ce chair.

In line with previous research [18,19], we model a business process based on the following four parameters: Uncertainty (p), variability $( \boldsymbol { \mathsf { v } } ) ,$ , time-criticality (r), and load (S) (Fig. 1 and Appendix A). Uncertainty refers to the degree to which process tasks are structured and well-understood by the IS development team at the time of system initiation. Variability refers to the degree to which process activities are concentrated on the same process task. Time-criticality measures the share of time-critical process activities. Process load is a normalized factor that expresses the overall activity load of the business process. The shaded areas in Fig. 1 indicate the parts of the model that we focus on when discussing the value of IS <sup>fl</sup>exibility in the current paper.

The characteristics of the IS development process are summarized by the two parameters staging (q) and IS lifetime (T) [18]: Staging re<sup>fl</sup>ects the fact that an IS is often not put into operation all at once, but in consecutive stages. IS lifetime de<sup>fi</sup>nes the total lifetime of the IS in years. Each parameter is explained in more detail subsequently, see also [18] for a more in-depth discussion.

The variables $\mathbf { W } _ { 1 } ,$ $\mathsf { W } _ { 2 }$ and $\mathsf { W } _ { 3 }$ express the recommended mix of <sup>fl</sup>exibility strategies in response to the business process and IS development characteristics. With $\mathsf { W } _ { 1 } ,$ , we indicate the share of all process activities that utilize the functionality that is built into the IS upon its inception (<sup>fl</sup>exibility-to-use). Share $\mathsf { w } _ { 2 }$ refers to the activities that are handled by the IS after it has been modi<sup>fi</sup>ed or after a new functionality has been implemented at some time during its operational lifetime (<sup>fl</sup>exibility-to-change). Lastly, $\mathsf { W } _ { 3 }$ denotes the share of activities that are not processed by the IS under consideration, but by different means, such as manually or by a different IS (no usage of IS). The weights $\mathsf { W } _ { 1 } ,$ w<sub>2</sub> and $\mathsf { W } _ { 3 }$ are derived decision variables that are calculated by minimizing total costs (TCOST) over the lifetime of the system.

## 2.2. Investment decisions

We include in the model two investment decisions that have to be made before the IS under consideration becomes operational: The <sup>fi</sup>rst decision concerns the basic investment (ICOST) and determines the extent of functionality that is included in the IS upon its inception (<sup>fl</sup>exibility-to-use). The second decision concerns an additional investment (FCOST) in the IS infrastructure that allows for modi<sup>fi</sup>cation and upgrades during the operational lifetime of the IS (<sup>fl</sup>exibility-tochange). Alternatively, ICOST can be viewed as an investment into an “off the shelf” standard IS, whereas FCOST refers to an incremental, additional investment in the case that a custom-tailored and modi<sup>fi</sup>able IS is selected instead. The additional investment FCOST has an impact on the possibility of subsequent modi<sup>fi</sup>cations and upgrades of the IS.

ICOST is modeled as

$$
\mathrm{ICOST} = \{\mathrm{a} + \mathrm{bL} (\mathrm{x} _ {1}) (\mathrm{q} + (1 - \mathrm{q}) \mathrm{DC}) \} \mathrm{z},\tag{1}
$$

where a denotes <sup>fi</sup>xed development and purchase costs, and b denotes variable development and purchase costs for the case that all process activities that are expected to occur at the time of the investment decision are supported by the IS. In the model, we consider that for process activities that are expected to occur with low frequency, it may not be economical to include the corresponding process task in the IS. Instead, the small number of occurrences could be handled outside of the focal IS, be it manually or by using a different IS that is outside of the scope of the model.

The percentage of known process tasks that is included in the initial IS is expressed by $\operatorname { L } ( \mathbf { x } _ { 1 } )$ , where $\mathbf { X } _ { 1 }$ with $0 { \le } \mathbf { X } _ { 1 } { \le } 1$ is a decision variable that denotes the share of all process activities in association with tasks that are expected with certainty at the time of IS initialization, and that will be handled by the IS (note: $\mathbf { X } _ { 1 }$ relates to the number of activities and $\operatorname { L } ( \mathbf { x } _ { 1 } )$ to the number of corresponding tasks). $\mathrm { L } ( \mathbf { x } _ { 1 } )$ with $0 \leq \mathrm { L } ( \mathbf { x } _ { 1 } ) \leq 1$ measures the concentration of activities on certain tasks and can be expressed by the well-known

![](/api/attachments/BKX9BFEK/fulltext/images/4d0f32bce599d3d58f32dcb7ad6953c4d13c139d57134668f336b180b8d01d94.jpg)  
Fig. 1. Model overview (adapted from [19]).

Lorenz curve [30] (Fig. 2). The value of $\mathrm { L } ( \mathbf { x } _ { 1 } )$ determines the extent of <sup>fl</sup>exibility-to-use that is built into the IS from its very beginning.

A number of proposals exist for the analytical form of the Lorenz curve [32]. Following [19], we use the form

$$
L (x) = x ^ {\nu} \left(1 - (1 - x) ^ {1 - \nu}\right).\tag{2}
$$

The variability parameter v measures the concentration of process activities, with $0 \leq \mathsf { v } \leq 1$ . Values of v that are close to 0 describe business processes with little concentration, thus high levels of variability, whereas values of v that are close to 1 describe business processes with low levels of variability, where activities for a small number of process tasks dominate (Fig. 2).

Given the complexity that is typically associated with IS implementation, the assumption of a one-shot (“big bang”) implementation is not very realistic, even if all process tasks were known in advance [18,22,28]. In practice, IS management often prefers a “staged” implementation approach with a certain percentage q of the IS being implemented immediately and the rest $( 1 - { \mathfrak { q } } )$ being implemented subsequently during the system's lifetime. Among the reasons for a staged approach are resource constraints and lack of user readiness. In order to account for the dynamic effects of investment staging we include an average discount factor (DC). Assuming that the remaining investments are spread out evenly over the IS lifetime T in years, we apply the annuity method and set DC as

$$
D C = \left((1 + i) ^ {T} - 1\right) / \left(i (1 + i) ^ {T} T\right) f o r i > 0 a n d D C = 1 f o r i = 0,\tag{3}
$$

where i denotes the yearly discount rate ([11], p. 886).

For practical reasons, such as to produce meaningful model results even for extreme parameter constellations, we further include in Eq. (1) a binary variable z with z=1, if the IS is implemented at all, and $z = 0$ if not. The values for the decision variables $\mathbf { X } _ { 1 }$ and z are yet unknown and will be computed endogenously by the model.

The additional cost premium FCOST for providing <sup>fl</sup>exibility-to-change is modeled as

$$
F C O S T = c y,\tag{4}
$$

where y is a binary decision variable with $\tt y = 1$ , if <sup>fl</sup>exibility-tochange is provided, and $\mathsf { y } = 0 ,$ , if not. The parameter c denotes the value of the premium. Note that FCOST includes only the initial investment into <sup>fl</sup>exibility-to-change while the subsequent costs for modifying and upgrading the IS are measured by a separate model term UCOST, as described below. While c is a <sup>fi</sup>xed cost parameter for the moment, it will later be endogenously calculated as the “value of IS <sup>fl</sup>exibility”.

The costs UCOST to modify and upgrade the IS during its lifetime are modeled as

$$
U C O S T = e L (x _ {2}) D C.\tag{5}
$$

In Eq. (5), the decision variable ${ \tt X } _ { 2 }$ with $0 \le \mathbf { X } _ { 2 } \le 1$ denotes the share of process activities that are unknown at the time of ISinitiation, but that are supported by the IS after <sup>fl</sup>exibility-to-change is utilized. The parameter e denotes the costs for the case that all relevant process activities are included in the update (i.e., for ${ \bf x } _ { 2 } = 1 )$ . As in Eq. $( 1 ) , \mathrm { L } ( \mathbf { X } _ { 2 } )$ refers to the Lorenz curve, and describes the amount of functionality that is built into the IS after modi<sup>fi</sup>cation or upgrade, see Eq. (2) for $\mathbf { X } = \mathbf { X } _ { 2 } .$ . And as in Eq. (1), DC is the average yearly discount factor according to Eq. (3) that re<sup>fl</sup>ects the assumption that upgrades and modi<sup>fi</sup>cations are spread out evenly over the IS lifetime.

## 2.3. Ongoing operations

While Eqs. (1)–(5) of the current model refer to investment decisions, the following Eqs. (6)–(8) refer to parameters and costs of ongoing operations. We distinguish IS operating costs OCOST that are associated with IS use, and manual costs MCOST that are associated with activities that are handled outside of the current IS (manually or by using different systems that are not considered here). To model the IS operating costs we use the parameters p as a measure for process uncertainty, and r as a measure for time-criticality.

However, before formulating the operating costs as such, we express the shares of the three different <sup>fl</sup>exibility strategies as

$$
w _ {1} = p x _ {1}; w _ {2} = (1 - p) x _ {2}; w _ {3} = 1 - w _ {1} - w _ {2}.\tag{6}
$$

The uncertainty parameter p with $0 { \le } \mathsf { p } { \le } 1$ is the probability that a process task can be foreseen and described at the time of IS initiation. The variables $\mathsf { W } _ { 1 } , \mathsf { W } _ { 2 }$ and $\mathsf { W } _ { 3 }$ in Eq. (6) are decision variables that are derived based on the primary decision variables $\mathbf { X } _ { 1 }$ and $\mathbf { X } _ { 2 }$ and the estimated parameter p. Following Eq. (6), the operating costs OCOST of the IS can be written as

$$
O C O S T = S d \left\{\left(q + (1 - q) L ^ {- 1} (0. 5)\right) w _ {1} + 0. 5 w _ {2} \right\} T D C.\tag{7}
$$

In Eq. (7), the parameter d is an estimate for the yearly operating costs if all process activities were handled by the system $( \mathrm { i } . \mathsf { e } . , \mathsf { w } _ { 3 } = 0 )$ These costs are multiplied by the shares of activities $\mathbf { W } _ { 1 }$ and $\mathsf { W } _ { 2 }$ that actually utilize the IS. Since we also assume that system additions, modi<sup>fi</sup>cations and upgrades are staged equally over the lifetime of the IS, half of the share $\mathsf { W } _ { 2 }$ is handled outside of the system, as the corresponding activities occur before the system has been modi<sup>fi</sup>ed or upgraded. For share $\mathbf { W } _ { 1 } ,$ , the list of activities that are supported by the IS and their variability according to the Lorenz curve are known in advance, which means that implementation priority can be given to tasks with higher frequency of occurrence. We consequently multiply $\mathbf { W } _ { 1 }$ with the inverse $\mathrm { L } ^ { - \bar { 1 } } ( 0 . 5 )$ , instead of 0.5 as in the case of w (see Fig. 2). The yearly operating costs are multiplied with the number of years T that depict the IS lifetime, and the average yearly discount factor DC according to Eq. (3). The scaling factor S with SN0 serves to evaluate different process load scenarios in the later part of the current paper. For the moment we assume the standardized factor ${ \sf S } = 1$

![](/api/attachments/BKX9BFEK/fulltext/images/3355c6df9560dc6eea853a98a52682b410c8dfd05c1b8965bba6eab89c9d12ab.jpg)  
Fig. 2. Lorenz curve.

In Eq. (8), the operating costs MCOST for activities that are performed outside of the IS are modeled similarly to Eq. (7) and include all of the remaining process activities. Here, the operating costs are multiplied by a yearly cost factor f that applies in cases where all process activities are performed outside of the IS $( \mathsf { w } _ { 3 } = 1 )$ . In addition, we include a percentage cost premium g that applies in cases where a share r of time-critical activities with $0 \leq \mathrm { r } \leq 1$ is processed outside of the IS, assuming that outside processing is less time-ef<sup>fi</sup>cient, and thus more expensive. We obtain

$$
M C O S T = S f (1 + r g) \left\{(1 - q) \left(1 - L ^ {- 1} (0. 5)\right) w _ {1} + 0. 5 w _ {2} + w _ {3} \right\} T D C.\tag{8}
$$

To ensure meaningful results, we add two logical constraints: First, for <sup>fl</sup>exibility-to-change to be applicable $\left( \mathbf { X } _ { 2 } > \mathbf { 0 } \right)$ , it has to be provided, which requires $\mathrm { y } = 1$ in Eq. (4). Therefore

$$
\mathrm{y} \geq x _ {2}.\tag{9}
$$

Second, for the system to be usable at all, that is ${ \bf x } _ { 1 } + { \bf x } _ { 2 } { > } 0$ , variable z in Eq. (1) has to be equal to 1. Therefore

$$
z \geq 0. 5 (x _ {1} + x _ {2}).\tag{10}
$$

Eq. (11) depicts the model's objective function as the minimum of the total costs over the entire lifetime of the IS. As TCOST joins the primary decision variables $\mathbf { X } _ { 1 } , \mathbf { X } _ { 2 } , \mathbf { y }$ and z, it provides the basis for the derived decision variables $\mathsf { W } _ { 1 } , \mathsf { W } _ { 2 }$ and ${ \bf W } _ { 3 } ;$

$$
T C O S T = \text { minimize } (I C O S T + F C O S T + U C O S T + O C O S T + M C O S T)\tag{11}
$$

subject to $0 \leq \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } \leq 1$ and $\mathsf { y } , z \in \{ 0 , 1 \}$

In mathematical terms, the model constitutes a small-scale, nonlinear, and mixed-integer program. Its solution is somewhat complicated, primarily due to the non-linear form of the Lorenz curve. But the model is robust in the sense that it produces plausible results for a wide range of parameter estimates within their feasible domain [19]. To solve the model for the applications in the remainder of the paper, we used the optimization software LINGO [29]

## 3. Computing the value of IS <sup>fl</sup>exibility

We are now ready to apply our model, and determine the value of IS <sup>fl</sup>exibility-to-change for a speci<sup>fi</sup>c numerical example. We <sup>fi</sup>rst assess the value of IS <sup>fl</sup>exibility in a deterministic scenario that corresponds with the traditional discounted cash <sup>fl</sup>ow (DCF) method. We then add stochastic elements and apply decision tree analysis (DTA) and real options analysis (ROA). Both DTA and ROA assume a risk-neutral decision maker, who bases decisions solely on average model outcomes and not on the speci<sup>fi</sup>c chances or risks inherent in the underlying complete probability distribution for the model outcomes [11,21,24,45]. Finally, we report the results of a risk analysis-based simulation experiment that makes explicit use of the full probability distribution and, thus, relaxes the assumption of risk-neutrality. The focus of our analysis is represented in Fig. 1 by the elements that are shaded in gray.

## 3.1. Numerical example

We <sup>fi</sup>rst introduce the numerical example that we use throughout the remainder of the paper. For demonstration purposes, the model parameters were selected in such a way that the model solution exhibits an interesting mix of <sup>fl</sup>exibility strategies (Fig. 1)<sup>1</sup>:

$$
\begin{array}{l} \text { Cost - related   parameters: } a = 1 0 0, b = 3 0 0, c = 5 0 (\text { later } c = 0), \\ d = 1 5 0, e = 3 0 0, f = 4 5 0, g = 0. 7 \text { and } i = 0. 0 5. \end{array}
$$

• Parameters that characterize the business process: $\begin{array} { r } { \mathsf { p } = 0 . 8 , \mathsf { v } = 0 . 6 , } \end{array}$ r=0.1 and S=1.

![](/api/attachments/BKX9BFEK/fulltext/images/44a098388b8a3dce453b7dce8688e847feb2ede1415e115f682de22e2e63d105.jpg)  
Fig. 3. Decision tree for non-deterministic business process load.

• Parameters depicting the IS development and implementation project and IS lifetime: ${ \tt q } = 0 . 5$ and $\mathrm { T } = 5 .$

We further assume that there exist no dependencies between these model parameters.

For this set of parameters the cost-minimal solution of the model is $\mathsf { w } _ { 1 } = 0 . 7 8$ $\mathsf { w } _ { 2 } = 0$ and $\mathsf { w } _ { 3 } = 0 . 2 2$ with $\mathrm { T C O S T } = 1 3 5 5 . 1$ . In other words, the model suggests that 78% of the process activities be supported by the IS using the <sup>fl</sup>exibility-to-use strategy, and 22% be handled outside of the IS. Flexibility-to-change is not included at all, resulting in ${ \bf x } _ { 2 } = \bf 0$ and $\begin{array} { r } { { \bf y } = \mathbf { 0 } , } \end{array}$ , and, as a consequence, $\mathsf { w } _ { 2 } = 0$ for the optimal solution.

## 3.2. Value of IS flexibility for deterministic process loads

In the numerical example above, we set the initial investment in <sup>fl</sup>exibility-to-change as a parameter at $\mathtt { c } = 5 0 ( \mathtt { E q . } ( 4 ) )$ ), and found this initial value of c to exceed the level at which <sup>fl</sup>exibility-to-change enters the <sup>fi</sup>nal solution. For the remainder of our analysis, we treat <sup>fl</sup>exibility-to-change as a choice that is available to decision makers and focus on the implicit threshold value of <sup>fl</sup>exibility-of-change ${ \mathfrak { c } } ^ { * } ,$ below which an investment in <sup>fl</sup>exibility-to-change becomes cost-ef<sup>fi</sup>cient.

Had we insisted in an investment in <sup>fl</sup>exibility-to-change at a level of $c = 5 0 ,$ the result would have been TCOST=1374.7 and $\mathsf { w } _ { 1 } = 0 . 7 8 , \ \mathsf { w } _ { 2 } = 0 . 0 9$ and ${ \cal W } _ { 3 } = 0 . 1 3$ , a result that we obtain by including the constraint $\tt y = 1$ in the model. The cost difference is $1 3 7 4 . 7 - 1 , 3 5 5 . 1 = 1 9 . 6$ monetary units. In other words, had we been able to reduce the investment into <sup>fl</sup>exibility-to-change by that amount $( { \mathrm { c } } ^ { * } = 5 0 - 1 9 . 6 = 3 0 . 4 )$ , the investment would have been included in the optimal solution. In the following, we refer $\mathrm { t o ~ } \mathrm { c } ^ { \ast }$ as the value of IS <sup>fl</sup>exibility.

It is important to note that the value of $c ^ { * }$ is independent of the initial input $c = 5 0$ , because c cancels out when subtracting the difference between the solutions with and without <sup>fl</sup>exibility-tochange from c, as we did above. Without loss of generality, we therefore set ${ \mathfrak { c } } = 0 ,$ and run the model twice: In the <sup>fi</sup>rst run, <sup>fl</sup>exibility-to-change is excluded by setting ${ \bf x } _ { 2 } = { \bf 0 } ,$ , and the resulting solution of the model is denoted with TCNF (total costs with no <sup>fl</sup>exibility-to-change provided). In the second run, we solve the model without the restriction ${ \bf { X } } _ { 2 } = 0$ allowing for an investment in <sup>fl</sup>exibility-to-change to occur, if ef<sup>fi</sup>cient, and call the resulting solution TCF (total costs with <sup>fl</sup>exibility-to-change provided). Given that the <sup>fi</sup>rst result is derived under the additional constraint of ${ \bf { X } } _ { 2 } = 0$ (and as a consequence $\mathbf { y } = \mathbf { 0 } )$ , we always observe TCNF ≥TCF, whereby the difference equals the value of IS <sup>fl</sup>exibility $c ^ { * }$ :

$$
c ^ {*} = T C N F - T C F.\tag{12}
$$

For our numerical example, we obtain TCNF = 1355.1 and $\mathrm { T C F } = 1 3 2 4 . 7$ . Hence, $c ^ { * } = 3 0 . 4$ as before.

## 3.3. Value of IS flexibility for stochastic process loads

To extend the deterministic scenario above, we now discuss an exemplary situation of stochastic process load. Besides the process load that underlies the deterministic scenario (base load), we include two additional scenarios, namely an upward scenario and a downward scenario. Compared to the deterministic scenario, we assume a 40% increase in the number of process activities for the upward scenario (load up), and a 50% decrease in process activities for the downward scenario (load down).<sup>2</sup> Moreover, we assume proportional changes in the operating costs so that in Eqs. (7) and (8) the scaling factor S takes the values $ { \mathrm { S } } _ { \mathrm { u } } = 1 . 4$ in the upward scenario (load up), $\mathsf { S } _ { \mathsf { b } } = 1$ in the deterministic scenario (base load), and ${ \cal S } _ { \mathrm { d } } = 0 . 5$ in the downward scenario (load down). In the following, we determine the value of IS <sup>fl</sup>exibility for stochastic process loads <sup>fi</sup>rst based on decision tree analysis (DTA), and second based on real-option analysis (ROA).

## 3.3.1. Decision tree analysis (DTA)

To apply DTA, probabilities have to be determined for the occurrence of the base, upward, and downward scenarios, for example $\mathrm { P _ { b } } = 0 . 2 5 , \ \mathrm { P _ { u } } = 0 . 5 0$ and $\mathrm { P _ { d } } = 0 . 2 5$ . The results of the optimization model for the various scenarios are depicted on the right-hand leaves of the decision tree in Fig. 3. Assuming a risk-neutral decision maker, we can use the expected values of TCF and TCNF as the main decision criterion ([11], p. 53). In the case of investment in <sup>fl</sup>exibility-to-change, $\mathrm { E } ( \mathrm { T C F } ) = 0 . 2 5 \times 1 7 0 8 . 3 + 0 . 5 0 \times 1 3 2 4 . 7 + 0 . 2 5 \times 8 1 3 . 6 = 1 2 9 2 . 8 .$ Accordingly, E(TCNF)=1325.0. The expected value of IS <sup>fl</sup>exibility is then determined by the difference $c ^ { * } = \operatorname { E } ( \mathrm { T C N F } ) - \operatorname { E } ( \mathrm { T C F } ) = 3 2 . 2$ . This number is larger than for the deterministic base scenario, where $c ^ { * } = 3 0 . 4 ,$ , largely because of the fact that the positive cost impact of the <sup>fl</sup>exibility-to-change option is large in the upward scenario, but rather small in the downward scenario.

## 3.3.2. Real option analysis (ROA)

An alternative to DTA is real option analysis (ROA), where the investment into <sup>fl</sup>exibility-to-change at the time of IS initiation is regarded as the purchase of a call option [22] that can be “exercised” anytime during the system's lifetime by modifying or upgrading the IS. For ROA, the value of IS <sup>fl</sup>exibility corresponds with the call option price and is determined as follows:

Similar to the previous calculations, without the availability of <sup>fl</sup>exibility-to-change, the three process load scenarios result in $\mathrm { T C N F _ { b } } { = } 1 3 5 5 . 1 , \ \mathrm { T C N F _ { u } } { = } 1 7 7 0 . 3 ,$ , and $\mathrm { T C N F _ { d } } { = } 8 1 9 . 5 \ \mathrm { ( F i g . } \ 3 )$ . The ratios of the anticipated results for the base scenario, and for the upward (U) and downward (D) scenarios, respectively, are $\mathrm { U } = 1 7 7 0 . 3 /$ 1355.1=1.306 and $\mathrm { D } { = } 8 1 9 . 5 / 1 3 5 5 . 1 { = } 0 . 6 0 5 ( \mathrm { F i g . ~ } 4 )$

Once the option of <sup>fl</sup>exibility-to-change becomes available, we expect ${ \mathrm { c _ { u } } } ^ { * } { = } \mathrm { T C N F _ { u } } { - } \mathrm { T C F _ { u } } { = } 6 2 . 0$ in the upward scenario and $\mathrm { c _ { d } } ^ { * } { = } \mathrm { T C N F _ { d } - }$ $\mathrm { T C F _ { d } } = 5 . 9$ in the downward scenario. Obviously, the overall value of IS <sup>fl</sup>exibility $c ^ { * }$ must lie somewhere in between, as a weighted average of ${ \sf C } _ { \bf u } ^ { \mathrm { ~ * ~ } }$ and $\boldsymbol { \mathrm { C _ { d } } } ^ { * }$ . We apply <sup>fi</sup>nancial options analysis to determine appropriate weights for ${ \sf C } _ { \bf u } ^ { \mathrm { ~ * ~ } }$ and $\boldsymbol { \mathrm { C _ { d } } } ^ { * }$ :

Let us assume that at the time of IS-initiation we were able to buy m options with a value of $c ^ { * }$ and potential pro<sup>fi</sup>ts ${ { \cal { C } } _ { \mathrm { { u } } } } ^ { * }$ and ${ \mathsf { C } } _ { \mathrm { d } } { } ^ { * }$ that hedge against unforeseen future process load variations. Hedging means that the <sup>fi</sup>nal costs of the base, upward and downward scenarios remain identical:

$$
T C N F _ {u} - m c _ {u} ^ {*} = T C N F _ {b} - m c ^ {*} a n d T C N F _ {d} - m c _ {d} ^ {*} = T C N F _ {b} - m c ^ {*}.\tag{13}
$$

Similar to our assumption for DTA, Eq. (13) indicates riskneutrality of the decision maker who has no a priori preference between the three scenarios ([11], p. 219). Solving Eq. (13) for the two unknown variables m and $c ^ { * }$ yields

$$
m = (T C N F _ {u} - T C N F _ {d}) / (c _ {u} ^ {*} - c _ {d} ^ {*})\tag{14}
$$

and

$$
\begin{array}{l} c ^ {*} = P c _ {u} ^ {*} + (1 - P) c _ {d} ^ {*} \text {   with   } P = (1 - D) / (U - D); (1 - P) = (U - 1) / (U - D) \\ \text { and } \quad U = T C N F _ {u} / T C N F _ {b}; D = T C N F _ {d} / T C N F _ {b}. \end{array}\tag{15}
$$

Eqs. (14) and (15) correspond with the well-known formulas of option price theory in the binomial form ([11], p. 219) with the exception that there is no time lag between base scenario, and upward and downward scenarios, respectively (all three scenarios relate to the same planning horizon). Hence, there is no need to include the risk-free interest rate in the formulas in order to account for time differences. Applied to our numerical example, Eqs. (14) and (15) result in $\mathrm { m } = ( 1 7 7 0 . 3 - 8 1 9 . 5 ) / ( 6 2 . 0 - 5 . 9 ) = 1 6 . 9 ~ \mathrm { a n d } ~ \mathrm { c } ^ { * } = \{ ( 1 -$ $0 . 6 0 5 ) / ( 1 . 3 0 6 - 0 . 6 0 5 ) \} \times 6 2 . 0 + \{ ( 1 . 3 0 6 - 1 ) / ( 1 . 3 0 6 - 0 . 6 0 5 ) \}$ $0 . 6 0 5 ) \} \times 5 . 9 = 0 . 5 6 3 \times 6 2 . 0 + 0 . 4 3 7 \times 5 . 9 = 3 7 . 5$ , The weights are P=0.563 and $1 - { \mathsf { P } } { = } 0 . 4 3 7 .$

In essence, ROA is based on a weighting scheme P and 1−P (called “hedging probabilities”) that is different from the weights $\mathrm { { P _ { u } , P _ { b } } }$ and $\mathrm { P _ { d } }$ that we used in DTA. Consequently, $c ^ { * }$ takes different values in ROA and in DTA. As an obvious advantage, ROA does not require the determination of explicit probabilities $\mathrm { { P _ { u } , P _ { b } } }$ and $\mathrm { P _ { d } } [ 9 , 4 3 ] ,$ . Instead, the weights are calculated endogenously by assuming a hedging strategy according to Eq. (13). We put all the weights on the upward and downward scenarios with the result that ROA results in higher values for ${ \mathfrak { c } } ^ { * } .$ . We address this aspect later in the context of compound ROA and the simulation experiments.

![](/api/attachments/BKX9BFEK/fulltext/images/8cd45da8c7857927ade0cdc9f7666c09c075b4e7e1a4d629ec5f16f7fce94bd0.jpg)  
Fig. 4. Interpretation as real option.

Table 1 shows ROA-based values of IS <sup>fl</sup>exibility that result for various combinations of upward and downward scenarios. We note that the value of IS <sup>fl</sup>exibility increases substantially with an increase in spread between base and upward scenarios. Table 1 also indicates that the model is robust in the sense that a large variation of the scaling factor S produces model outcomes that can be reasonably interpreted.

## 3.4. Extension of ROA to include multiple model parameters

So far, only one of the model parameters (process load S) has been applied in stochastic form. We are now ready to extend the analysis and apply stochastic forms to the remaining business process characteristics p (uncertainty), v (variability) and r (time-criticality) (Fig. $1 ) . ^ { 3 }$ Both, DTA and ROA can be applied to assess the value of <sup>fl</sup>exibility in this more complex situation. DTA, however, leads to a straight-forward explosion of the decision tree that requires numerous additional assumptions regarding the various probabilities of occurrence. Instead, we later go one step further and explore the full risk structure with appropriate simulation experiments that are based on complete probability functions for each of the four parameters and that also relax the assumption of risk neutrality. Therefore, we only apply ROA in a compound form (Fig. 5).

To calculate the value of IS <sup>fl</sup>exibility $c ^ { * }$ in compound ROA, the tree in Fig. 5 needs to be interpreted recursively from right to left. For instance, for the top-most path the value ${ \mathsf { C } } _ { \mathrm { L p v r } } { } ^ { * } = 4 3 . 0$ denotes the value of <sup>fl</sup>exibility if <sup>fl</sup>exibility-to-change were provided for the parameter constellation L=1.4, $\mathsf { p } = 0 . 9 , \mathsf { v } = 0 . 8$ and $\Gamma = 0 . 3$ , and is computed as the difference $\mathrm { c _ { L p v r } } ^ { * } { = } \mathrm { T C N F _ { L p v r } } { - } \mathrm { T C F _ { L p v r } }$ with the corresponding parameter settings in both model runs. Accordingly, ${ \mathsf { c } } _ { \mathrm { L p v r } } { } ^ { * } = 2 6 . 3$ is the value for the parameter constellation $\mathrm { L } = 1 . 4 ,$ $\mathsf { p } = 0 . 9 , \mathsf { v } = 0 . 8$ and r=0. In the next stage to the left, both values are consolidated using binomial ROA according to Eq. (15), resulting in ${ \mathsf { c } } _ { \mathrm { L p v } } { } ^ { * } = 3 1 . 9$ . For each consolidation step, TCNF of the base scenario for the corresponding model parameter is needed in order to calculate U, D and P in Eq. (15). The sequential application of binomial ROA continues until we obtain $c ^ { * } = 5 2 . 7$ in the <sup>fi</sup>nal stage of the analysis (Fig. 5, far left). The result is a compound value of IS <sup>fl</sup>exibility $c ^ { * } = 5 2 . 7$ that re<sup>fl</sup>ects the stochastic nature of all four process parameters.<sup>4</sup>

Table 1  
Value of IS Flexibility for different scenarios (ROA).

<table><tr><td colspan="2">Business process load scenario</td><td rowspan="2">Value of IS flexibility (c*)</td></tr><tr><td>Upward (%)</td><td>Downward (%)</td></tr><tr><td>+0</td><td>-0</td><td>30.4 (Base scenario)</td></tr><tr><td>+5</td><td>-5</td><td>30.6</td></tr><tr><td>+10</td><td>-10</td><td>30.8</td></tr><tr><td>+20</td><td>-20</td><td>31.8</td></tr><tr><td>+30</td><td>-30</td><td>33.5</td></tr><tr><td>+40</td><td>-40</td><td>36.0</td></tr><tr><td>+40</td><td>-50</td><td>37.5</td></tr><tr><td>+50</td><td>-50</td><td>39.1</td></tr><tr><td>+100</td><td>-50</td><td>45.7</td></tr><tr><td>+100</td><td>-70</td><td>53.1</td></tr><tr><td>+20</td><td>-50</td><td>34.1</td></tr><tr><td>+20</td><td>-70</td><td>35.8</td></tr></table>

3.5. Exploring the full risk structure with stochastic simulation (risk analysis)

Both DTA and ROA are based on the assumption that decision makers are risk-neutral, and therefore indifferent in their choice between the full risk-structure of the problem on the one hand and expected values on the other hand. In both methods of analysis, decisions are based on the expected values only. The assumption of risk-neutrality can be relaxed when considering the full risk structure of the decision problem, yet then requires information about the underlying probability functions.

In the following, we present the results of a simulation experiment that we performed using full distribution functions for the parameters S, p, v and r instead of base, upward and downward scenarios alone. If we can assume that the upward and downward scenarios delineate strict boundaries, beyond which parameter values are practically impossible, and that the base case describes the most likely situation, then it is reasonable to use beta distributions with modes for the base scenario and end points for the upward and downward scenarios. In the absence of a pre-known distribution, beta distributions frequently serve as a reference in a wide range of situations where one only has information on the mode or mean and on two <sup>fi</sup>nite endpoints of a random variable [25]. Because of the <sup>fi</sup>nite boundaries, beta distributions ensure robustness in the sense that any random draw for a parameter produces reasonable model results, which would not happen for instance with the use of normal distributions. An alternative, namely truncated normal distributions that we have used previously [38], does not allow modeling skewed parameter distributions.

Fig. 6 depicts the density functions of three different beta distributions, where PAR stands for one of the following parameters: S, p, v, and r. The three density functions relate to identical modes and boundary scenario values, but differ with regards to the assumed standard deviation ${ \sigma } _ { \mathrm { P A R } } .$ . In addition to the three scenario values, the user consequently has to decide on $\mathbf { { O } } _ { \mathrm { { P A R } } }$ . The standard deviations in Fig. 6 correspond with the application of the 3-sigma rule (upper left), 2.5-sigma rule (upper right), and 2-sigma rule (bottom). For example, for the 2.5-sigma rule, the span $\mathrm { P A R } _ { \mathrm { u } } – \mathrm { P A R } _ { \mathrm { d } }$ is covered by 2 times $2 . 5 \mathrm { \sigma } _ { \mathrm { P A R } } = 5 \mathrm { \sigma } _ { \mathrm { P A R } }$

The analytical form of the beta density function $\mathrm { D } ( \mathbf { x } ) = \mathrm { B } ( \boldsymbol { \alpha } , \mathrm { \beta } ) ^ { - 1 } \mathbf { x } ^ { \alpha - 1 }$ $( 1 - \mathbf { x } ) ^ { \beta - }$ <sup>1</sup> with $\mathrm { P A R _ { d } \leq x \leq P A R _ { u } }$ depends on two parameters α and β. The term $\mathsf { B } ( \alpha , \beta )$ is the so-called beta function and is independent of x. The values α and β can be calculated from PAR and $\mathbf { { O } } _ { \mathrm { { P A R } } }$ as follows [46]:

$$
\left(P A R _ {b} - P A R _ {d}\right) / \left(P A R _ {u} - P A R _ {d}\right) = (a - 1) / (\alpha + \beta - 2)\tag{16}
$$

and

$$
\sigma_ {P A R} / (P A R _ {u} - P A R _ {d}) = \left((\alpha \beta) / \left((\alpha + \beta) ^ {2} (\alpha + \beta + 1)\right)\right) ^ {0. 5}.\tag{17}
$$

The right hand sides of Eqs. (16) and (17) describe the mode and the standard deviation in terms of α and β for the beta density function standardized to the unit interval $0 \leq \mathbf { X } \leq 1$

To conduct our simulation experiment, we drew 100 vectors (L, p, v and r) of beta-distributed parameters with modes and boundary values as in the previous section (Fig. 5) and we uniformly applied the 2.5-sigma-rule to all four parameters on the left side of Eq. $( 1 7 ) { : \mathbb { O } } _ { \mathrm { P A R } } /$ $( \mathrm { P A R _ { u } } - \mathrm { P A R _ { d } } ) = 1 / 5 . ^ { 5 }$ For each of the 100 samples we computed the corresponding value of IS <sup>fl</sup>exibility ${ \mathfrak { r } } ^ { * }$ based on Eq. $( 1 2 ) . ^ { 6 }$ Fig. 7 shows the resulting frequencies for the 100 values of IS <sup>fl</sup>exibility $c ^ { * }$

The results exhibit a mean value of IS <sup>fl</sup>exibility of 41.7 monetary units and a standard deviation of the mean of $3 0 . 5 / \surd 1 0 0 = 3 . 0 5 .$ . By cumulating the frequencies in Fig. 7 we can now explicitly assess the risk that is involved with an investment into <sup>fl</sup>exibility-to-change (Table 2). For instance, the probability that the value of IS <sup>fl</sup>exibility c\* is larger than 50 monetary units is 30%, and the probability that $c ^ { * }$ is larger than 70 monetary units is 20%. In addition, the simulation experiment reveals again that the computation of the value of IS <sup>fl</sup>exibility in the deterministic case $( \mathrm { c } ^ { * } = 3 0 . 4 )$ underestimates the economic bene<sup>fi</sup>ts of <sup>fl</sup>exibility-to-change.

We note that the results of the simulation experiment depend strongly on the chosen standard deviation $\mathbf { { { \sigma } } } _ { \mathbf { { { \mathrm { O } } } \mathbf { { { \mathit { P } } } \mathbf { { A R } } } } }$ in Eq. (17). Smaller standard deviations, such as in the 3-sigma case in Fig. 6 put less probability on the outer regions of the density function; larger standard deviations such as in the 2-sigma case put more probability on the outer regions. It is up to the decision maker to choose the standard deviation that best re<sup>fl</sup>ects the corresponding decision situation, a decision that can be supported graphically (Fig. 6).

Fig. 8 summarizes our <sup>fi</sup>ndings as it exhibits the mean values of <sup>fl</sup>exibilit $r c ^ { * }$ (solid line) plus and minus two standard deviations of the mean (dotted lines) for different sigma cases. For each case we ran a simulation experiment for a sample size of 100. Again, the same sigma-case was applied to all four model parameters. The “random case” in Fig. 8 relates to the largest possible spread of parameter values within its boundaries, namely an equal distribution between $\mathrm { P A R _ { d } }$ and $\mathrm { P A R } _ { \mathrm { u } } .$ . For the random case $\mathrm { { { \sigma _ { P A R } } / ( P A R _ { u } - P A R _ { d } ) } = 1 / 1 2 }$ for the left side of Eq. (17), which results in $\alpha = \beta = 1$ for the beta density function.

Interestingly, the comparatively high value of IS <sup>fl</sup>exibility that resulted from the application of the 2-sigma case for the simulation experiments $( \mathrm { c } ^ { * } = 5 1 . 1 )$ is very close to the result of the compound ROA that we performed earlier $( \mathrm { c } ^ { * } = 5 2 . 7 )$ ). We suggest that this <sup>fi</sup>nding re<sup>fl</sup>ects the fact that both methods put comparatively strong weight on the boundaries of the parameter intervals. Such an approach is justi<sup>fi</sup>ed in particular when parameter probabilities are not concentrated on the mode but spread within the parameter boundaries, which is typical for high-risk situations, such as beta distributions with large sigmas where only a few sigmas span the interval $( \mathrm { P A R _ { d } }$ and $\mathrm { P A R } _ { \mathrm { u } } )$ . In low-risk situations (small sigmas), ROA should therefore be applied with care as it might overestimate the value of IS <sup>fl</sup>exibility.

## 4. Conclusions

In this paper, we computed the value of information system (IS) <sup>fl</sup>exibility by building on and extending an earlier model [18,19]. Taking into consideration the stochastic nature of a <sup>fl</sup>exibility-related decision situation, we applied DTA, ROA, and risk analysis based on stochastic simulation experiments. Our <sup>fi</sup>ndings generally complement the results of earlier studies that have applied ROA in multi-parameter settings [22]. For the exemplary numerical example and its parameter constellation that we used throughout the paper our analyses show that a purely deterministic treatment (base scenario) can systematically underestimate the value of IS <sup>fl</sup>exibility when compared with a stochastic approach. This result re<sup>fl</sup>ects the asymmetric outcome that can often be observed in a stochastic environment: For instance, while the cost bene<sup>fi</sup>t of IS <sup>fl</sup>exibility-tochange in an upward load scenario may be substantial, the impact is often comparatively small in a downward load scenario. Therefore, we suggest that in order to avoid underestimating the value of IS <sup>fl</sup>exibility decision makers should include stochastic features into their analysis.

![](/api/attachments/BKX9BFEK/fulltext/images/d39ff292bf88677cad6d8fb6587f80fc91e26f0ad0038dc72c2a10466d4b9d1e.jpg)  
Fig. 5. Compound ROA, extended to multiple parameters.

We also found that the value of IS <sup>fl</sup>exibility depends strongly on the selected measurement technique. While ROA in the applied form puts much distribution weight on the parameter boundaries, DTA and risk analysis via simulation experiments put more weight around the modal value of the distribution. We found ROA to overestimate the value of IS <sup>fl</sup>exibility in low-risk situations, yet to be an appropriate method to assess the value of IS <sup>fl</sup>exibility in high-risk situations.

Our analysis also showed ROA to be particularly attractive for two reasons. Compared to DTA, ROA requires less information from the decision maker because it does not need explicit estimates for the probabilities of different parameters, apart from upside and downside scenarios for the parameter values. While the determination of scenarios implicitly requires a likeliness assessment, a graphical presentation of different shapes of probability densities for the concerned parameter values (Fig. 6) can help the decision maker determine the appropriateness of ROA. A second attractive feature of ROA is the fact that it relies on the hedging principle which has widely been applied in business planning.

In the current paper, we used a speci<sup>fi</sup>c optimization model to compute the value of IS <sup>fl</sup>exibility, as a representative example for real life situations. For practical decision making the various model parameters have to be determined very carefully, possibly requiring

![](/api/attachments/BKX9BFEK/fulltext/images/7bd08cb83bf7d447b525c670df42c75ac68badf994b8fae111ab6a1863c9dfc5.jpg)  
Fig. 6. Beta density function, applied for 3-sigma rule (upper left), 2.5-sigma rule (upper right), and 2-sigma rule (bottom).

![](/api/attachments/BKX9BFEK/fulltext/images/745247698bf0b7c92876da7e884385804fb390a26540edb53b15d2b26df83927.jpg)  
Fig. 7. Distribution of the value of IS <sup>fl</sup>exibility.

Risk assessment of an investment in IS <sup>fl</sup>exibility.

<table><tr><td>Level</td><td>Probability that value of IS flexibility exceeds level</td></tr><tr><td>10</td><td>0.95</td></tr><tr><td>20</td><td>0.74</td></tr><tr><td>30</td><td>0.52</td></tr><tr><td>40</td><td>0.40</td></tr><tr><td>50</td><td>0.30</td></tr><tr><td>60</td><td>0.23</td></tr><tr><td>70</td><td>0.20</td></tr><tr><td>80</td><td>0.17</td></tr><tr><td>90</td><td>0.11</td></tr><tr><td>100</td><td>0.07</td></tr></table>

the development of additional estimation models. Our optimization model is tailored speci<sup>fi</sup>cally to IS in support of business processes. For other types of IS, different approaches may have to be applied. It should also be noted that the calculation of the value of <sup>fl</sup>exibility as proposed in this paper is independent of the chosen model, as long as the model provides TCF and TNCF as the two required inputs to Eq. (12) for different scenarios.

![](/api/attachments/BKX9BFEK/fulltext/images/08c38a2968788022ba8e66b6f9ddfbdc243b14de105b1d6426fd377d81763cbd.jpg)  
Fig. 8. Value of IS <sup>fl</sup>exibility for different sigma-cases.

## Appendix A. Modeling notation

<table><tr><td colspan="2">Decision variables (direct)</td></tr><tr><td>y</td><td>Binary variable with y = 1 if flexibility-to-change is provided, else y = 0</td></tr><tr><td>z</td><td>Binary variable with z = 1 if IS is implemented at all, else z = 0</td></tr><tr><td> $x_1$ </td><td>Share of process activities for tasks that are anticipated at the time of IS initiation and use flexibility-to-use</td></tr><tr><td> $x_2$ </td><td>Share of process activities for tasks that are not anticipated at the time of IS initiation and use flexibility-to-change</td></tr><tr><td colspan="2">Decision variables (derived)</td></tr><tr><td> $w_1$ </td><td>Share of total process activities performed based on flexibility-to-use</td></tr><tr><td> $w_2$ </td><td>Share of total process activities performed based on flexibility-to-change</td></tr><tr><td> $w_3$ </td><td>Share of total process activities performed based on manual operations</td></tr><tr><td colspan="2">Process and IS project characteristics</td></tr><tr><td>p</td><td>Probability that a process task is anticipated at the time of system initiation (measures process uncertainty)</td></tr><tr><td>P</td><td>Scenario probabilities (DTA) respectively hedging probability (ROA)</td></tr><tr><td>v</td><td>Curvature of the Lorenz curve (measures process variability)</td></tr><tr><td>L(x)</td><td>Functional value of the Lorenz curve with either  $x = x_1$  or  $x = x_2$ </td></tr><tr><td>r</td><td>Share of time-critical process tasks (measures time-criticality)</td></tr><tr><td>q</td><td>Percentage of the IS being implemented immediately</td></tr><tr><td>i</td><td>Yearly discount rate</td></tr><tr><td>T</td><td>IS lifetime in years</td></tr><tr><td>DC</td><td>Average discount factor reflecting equal cash flows (except initial investments) throughout the IS lifetime T</td></tr><tr><td colspan="2">Cost and value parameters</td></tr><tr><td>ICOST</td><td>Total investment in flexibility-to-use at the time of IS initiation</td></tr><tr><td>a</td><td>Base investment in flexibility-to-use at the time of IS initiation</td></tr><tr><td>b</td><td>Additional investment in flexibility-to-use, if all process tasks that are anticipated at the time of IS initiation were supported by the IS</td></tr><tr><td>FCOST</td><td>Actual investment in flexibility-to-change at the time of IS initiation</td></tr><tr><td>c</td><td>Investment in flexibility-to-change if provided (i.e., if y = 1)</td></tr><tr><td>OCOST</td><td>Actual system operating costs</td></tr><tr><td>d</td><td>System operating costs if all process activities were supported by the system</td></tr><tr><td>S</td><td>Process load scaling factor with S = 1 for the base scenario</td></tr><tr><td>UCOST</td><td>Actual system upgrade costs using the flexibility-to-change option provided</td></tr><tr><td>e</td><td>System upgrade costs if all process tasks that are not anticipated at the time of IS initiation were included in the upgrade</td></tr><tr><td>MCOST</td><td>Actual costs for manual operations</td></tr><tr><td>f</td><td>Manual operating costs if all process activities were performed manually</td></tr><tr><td>g</td><td>Cost markup for manually performing time-critical process activities</td></tr><tr><td>TCOST</td><td>Total costs over the entire lifetime of the system</td></tr><tr><td>TCF</td><td>Total costs with flexibility-to-change provided (y = 1)</td></tr><tr><td>TCNF</td><td>Total costs with flexibility-to-change not provided (y = 0)</td></tr><tr><td>c*</td><td>Value of IS flexibility</td></tr><tr><td>E</td><td>Expected value (for the stochastic cases)</td></tr></table>

## References

[1] B.R. Allen, A.C. Boynton, Information architecture: in search of ef<sup>fi</sup>cient <sup>fl</sup>exibility MIS Quarterly 15 (4) (1991).

[2] M. Amram, N. Kulatilaka, Real Options: Managing Strategic Options in an Uncertain World, Harvard Business School Press, Boston, Mass, 1999.

[3] H. Bahrami, S. Evans, Super-<sup>fl</sup>exibility for knowledge enterprises, A Toolkit for Dynamic Adaptation, 2nd edition, Springer, Berlin, Germany, 2010.

[4] M. Benaroch, R.J. Kauffman, A case for using real options pricing analysis to evaluate information technology project investments, Information Systems Research 10 (1) (1999).

[5] C. Billington, B. Jonson, A. Triantis, A real options perspective on supply chain management in high technology, Journal of Applied Corporate Finance 15 (2) (2002).

[6] T.A. Byrd, D.E. Turner, An exploratory examination of the relationships between <sup>fl</sup>exible IT infrastructure and competitive advantage, Information & Management 39 (1) (2001).

[7] B. Carlson, Flexibility and the theory of the <sup>fi</sup>rm, International Journal of Industrial Organization 7 (2) (1989).

[8] S.H. Chung, R.K. Rainer, B.R. Lewis, The impact of information technology infrastructure <sup>fl</sup>exibility on strategic alignment and applications implementation, Communications of the Association for Information Systems 11 (2003).

[9] T.E. Copeland, P.T. Keenan, How much is <sup>fl</sup>exibility worth? McKinsey Quarterly 1998 (2) (1998).

[10] T. Copeland, J. Weiner, Proactive management of uncertainty, McKinsey Quarterly 1990 (4) (1990).

[11] T.E. Copeland, J.F. Weston, K. Shastri, Financial Theory and Corporate Policy, Pearson Addison, Boston, Mass., 2007.

[12] T. Davenport, Process Innovation: Reengineering Work through Information Technology, Harvard Business School Press, Boston, Mass., 2007.

[13] P.R. Duimering, F. Safayeni, L. Purdy, Integrated manufacturing: redesign the organization before implementing <sup>fl</sup>exible technology, Sloan Management Review 34 (4) (1993).

[14] J.S. Evans, Strategic <sup>fl</sup>exibility for high technology manoeuvres: a conceptual framework, Journal of Management Studies 28 (1) (1991).

[15] R.G. Fichman, Real Options and IT platform adoption: implications for theory and practice, Information Systems Research 15 (2) (2004).

[16] R.G. Fichman, M. Keil, A. Tiwana, Beyond valuation: ‘options thinking’ in IT project management, California Management Review 47 (2) (2005).

[17] M. Fowler, Patterns of Enterprise Application Architecture, Addison-Wesley, Boston, Mass., 2003.

[18] J. Gebauer, F. Lee, Enterprise system <sup>fl</sup>exibility and implementation strategies: aligning theory with evidence from a case study, Information Systems Management 25 (1) (2008).

[19] J. Gebauer, F. Schober, Information system <sup>fl</sup>exibility and the cost ef<sup>fi</sup>ciency of business processes, Journal of the Association for Information Systems 7 (3) (2006).

[20] P. Ghemawat, P. Del Sol, Commitment versus <sup>fl</sup>exibility? California Management Review 40 (4) (1998).

[21] C.M. Harvey, Structured prescriptive models of risk attitudes, Management Science 36 (12) (1990).

[22] C. Hilhorst, P. Ribbers, E. van Heck, M. Smits, Using Dempster–Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: a case study, Decision Support Systems 46 (1) (2008).

[23] F.S. Hillier, G.J. Lieberman, Introduction to Operations Research, 7th edition, McGraw-Hill Boston Mass. (1) (2003)

[24] J. Hull, Options, Futures, and Other Derivatives, 3rd edition, Prentice Hall, Upper Saddle River, NJ, 1997.

[25] D.L. Keefer, S.E. Bodily, Three-point approximations for continuous random variables, Management Science 29 (5) (1983).

[26] Y.J. Kim, G.L. Sanders, Strategic actions in information technology investment based on real option theory, Decision Support Systems 33 (1) (2002).

[27] L.L. Koste, M.K. Malhotra, A theoretical framework for analyzing the dimensions of manufacturing <sup>fl</sup>exibility, Journal of Operations Management 18 (1) (1999).

[28] E.J.M. Lauria, P.J. Duchessi, A Bayesian belief network for IT implementation decision support, Decision Support Systems 42 (3) (2006).

[29] LINDO, LINGO Version 8.0, LINDO Systems Inc, Chicago, Illinois, 2003.

[30] M.O. Lorenz, Methods of measuring the concentration of wealth, Publications of the American Statistical Association 9 (1905).

[31] K. Maier, Die Flexibilität betrieblicher Leistungsprozesse, Harri Deutsch, Frankfurt Germany, 1981.

[32] P. Ortega, G. Martin, A. Fernandez, M. Ladoux, A. Garcia, A new functional form for estimating Lorenz curves, Review of Income and Wealth 37 (4) (1991).

[33] R. Palanisamy, Sushil, Achieving organizational <sup>fl</sup>exibility and competitive advantage through information systems, Journal of Information & Knowledge Management 2 (3) (2003).

[34] R.S. Pressman, Software Engineering: A Practitioner's Approach, McGraw-Hill New York, 1982.

[35] D. Robey, M.-C. Boudreau, Accounting for the contradictory organizational consequences of information technology: theoretical directions and methodological implications, Information Systems Research 10 (2) (1999).

[36] J.H. Saleh, G. Mark, N.C. Jordan, Flexibility: a multi-disciplinary literature review and a research agenda for designing <sup>fl</sup>exible engineering systems, Journal of Engineering Design 20 (3) (2009).

[37] V. Sambamurthy, A. Bharadwaj, V. Grover, Shaping agility through digital options: reconceptualizing the role of information technology in contemporary <sup>fi</sup>rms, MIS Quarterly 27 (2) (2003).

[38] F. Schober, J. Gebauer, How much to spend on <sup>fl</sup>exiblility? Determining the value of information system <sup>fl</sup>exiblility, Americas Conference on Information Systems (AMCIS) 2009 Proceedings, Paper 193, 2009, 3 (accessed on April 9, 2011) http://aisel.aisnet.org/amcis2009/19.

[39] E.S. Schwartz, C. Zozaya-Gorostiza, Investment under uncertainty in information technology: acquisition and development projects, Management Science 49 (1) (2003).

[40] M.S. Silver, Systems that Support Decision Makers: Description and Analysis, Wiley & Sons, Chichester, UK, 1991.

[41] G. Stigler, Production and distribution in the short run, Journal of Political Economy 47 (3) (1939).

[42] P.P. Tallon, R.J. Kauffman, H.C. Lucas, A.B. Whinston, K. Zhu, Using real options analysis for evaluating uncertain investments in information technology: insights from the ICIS 2001 debate, Communications of the Association for Information Systems 9 (2002).

[43] L. Trigeorgis, Real options and interactions with <sup>fi</sup>nancial <sup>fl</sup>exibility, Financial Management 22 (3) (1993).

[44] R.J. Vokurka, S. O'Leary-Kelly, A review of empirical research on manufacturing <sup>fl</sup>exibility, Journal of Operations Management 18 (4) (2000).

[45] J. Von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, 2 ed., Princeton University Press, Princeton, NJ, 1947.

[46] E.W. Weisstein, Beta Distribution, MathWorld — a Wolfram Web Resource, http://mathworld.wolfram.com/BetaDistribution.html (accessed on October 23, 2009).

[47] J. Zhang, S. Bandyopadhyay, S. Piramuthu, Real option valuation on grid computing, Decision Support Systems 46 (1) (2008).

![](/api/attachments/BKX9BFEK/fulltext/images/fb40d6987db5bcbddf908481c8b7168841259e81e429625f1391f37cab31c694.jpg)

Franz Schober is Professor Emeritus of Information Systems at the University of Freiburg, Germany. He earned a master degree in mathematics as well as a Ph.D. and a habilitation degree in business administration, all from the University of Munich. Before joining university he worked for 22 years in the computer industry. His current research interests are located in the <sup>fi</sup>elds of decision support systems and strategic information management. The results of his research have predominantly been published in German scienti<sup>fi</sup>c journals such as Wirtschaftsinformatik, Informatik Forschung und Entwicklung, Schmalenbachs Zeitschrift für Betriebswirtschaftliche Forschung, Zeitschrift für Betriebswirtschaft, Zeitschrift für Planung und Unternehmenssteuerung, but more recently also in the Journal

of the Association for Information Systems.  
![](/api/attachments/BKX9BFEK/fulltext/images/dece8402646d6eeb1215a96eb6d166058836d494c2d5bd1cc673e62a070292e1.jpg)

Judith Gebauer is an Associate Professor of Information Systems at the University of North Carolina Wilmington. She holds both master and doctoral degrees from the University of Freiburg, Germany, and has held positions at the University of Illinois at Urbana-Champaign and at the University of California, Berkeley. Her research focuses on the design and management of business information systems and includes projects on the task-technology <sup>fi</sup>t of mobile information systems, information system <sup>fl</sup>exibility and the impact of information technology on product modularity. Her work has been published in such journals as Journal of Information Technology, Journal of the Association for Information Systems, Communications of the ACM, International Journal of Electronic

Commerce, Information Systems Management, Information Systems and e-Business Management, Electronic Markets, Information Technology and Management, Informatik Forschung und Entwicklung, and International Journal of Mobile Communications. For more information, please visit judithgebauer.com.
