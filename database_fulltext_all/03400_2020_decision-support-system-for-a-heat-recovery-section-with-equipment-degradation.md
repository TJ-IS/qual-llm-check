---
otero_id: 3400
otero_key: "PPEZNGRM"
title: "Decision support system for a heat-recovery section with equipment degradation"
authors: "Maria P. Marcos; José Luis Pitarch; César de Prada"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113380"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support system for a heat-recovery section with equipment degradation

![](/api/attachments/PPEZNGRM/fulltext/images/f32129853806797599e515a1790fcd8acb5271299ff8782178cde53c4ea00d7b.jpg)

Maria P. Marcos<sup>a,b,⁎</sup>, José Luis Pitarch<sup>b</sup>, César de Prada<sup>a,b</sup>

<sup>a</sup> Institute of Sustainable Processes (ISP), Universidad de Valladolid, Spain

<sup>b</sup> Systems Engineering and Automatic Control DPT, EII, Universidad de Valladolid, Address: C/Real de Burgos s/n, 47011 Valladolid, Spain

## A R T I C L E I N F O

Keywords: Mathematical modeling Maintenance decisions Heat recovery Real-time optimization Industrial DSS

## A B S T R A C T

In the framework of Industry 4.0, decision support systems (DSS) are an essential part in the process of converting information into managerial actions. This paper proposes a specific DSS to improve the daily operation of an industrial heat-recovery section (a network of heat exchangers) in a fiber-production factory. In this process, the aim is to optimize the resource utilization in real time while satisfying a set of production constraints. The operational decisions to be taken by the network operators is to set up the heat-source allocation to heat exchangers. Furthermore, the heat transfer decreases over time due to fouling in the exchangers, so an additiona decision to take is which exchanger to clean and when. The proposed model-based DSS builds upon a rigorous mathematical representation of the network, integrating continuous operation with the discrete decisions on maintenance. Then, a mixed-integer nonlinear optimization, solved in real time, drives the analysis and choice phases to fulfill product specifications according to an economic criterion. In this way, the proposed DSS not only provides the user with a right allocation of heat sources to exchangers. but also suggests which of them are potentially beneficial to be cleaned.

## 1. Introduction

Eficiency improvement in the process industry, i.e. reducing the global energy and resource consumption, can come from two main courses of action: replacing older plants, equipment or processes by more modern and eficient ones; or being more eficient with the current facilities by looking closer at the daily operation [1], instead of making larger investments with uncertain pay back horizons. Nowadays, however, decision-making is conceptually more complex than it was in the past, because the rapidly growing technology and commu nication systems have spawned a large number of alternatives from which a decision-maker can select from. Moreover, taking a wrong or suboptimal decision with the structural complexity of current problems often results in a magnification of costs along the products value chain [2].

To improve overall daily operation, taking into account real-time production constraints and the increasingly restrictive environmental regulation. optimization needs to be performed at different levels: control layer, real-time operation, as well as at the production and maintenance scheduling [3]. In particular, real-time optimization (RTO) searches for the best operation conditions in a mid-way between process control and production scheduling [4]. There are many examples in literature on the benefits of using an RTO scheme to facilitate the decision-making process [5–7]. These schemes are usually model based, so one important task is to develop a good mathematical model which represents the behavior of the actual system [8].

In this work we propose a model-based specific DSS [9] to support operators and plant managers on the daily management of an industrial heat-exchanger network (HEN) according to economic criteria. Many industrial factories have a heat-recovery section to reduce the overall energetic consumption. Usually these heat-recovery sections are formed by heat exchangers where some streams are heated using the waste heat of other process streams. Hence, the heat-recovery sections can save important amounts of money, so their eficiency is crucial. Consequently, many proposals/works reported in the literature focus on optimizing the design of these networks [10]. Nevertheless, over time, the operation conditions move away from the ones that the network has been designed for, causing that the network does not work in the best way anymore. Therefore, optimally operating the network day by day (i.e., setting the stream flows, heat sources, etc.) is key to keep its efficiency at the highest possible value. Moreover, here we also consider the most important issue in the operation of such kind of networks: the fouling efect. Fouling is the accumulation of unwanted deposits on the surfaces of a heat exchanger, thus increasing the resistance to heat transfer and, consequently, reducing its eficiency [11]. Consequently, the heat exchangers should be cleaned from time to time, even though cleaning tasks involve an economic cost. This kind of semi-structured problem is often too complex for a human operator/manager due to the large number of alternatives arising from such combinatorial problem.

For this DSS application, the developed DSS software system is an optimization-analysis model, proposed to run as an RTO. To develop this, we built a rigorous mathematical model, including both continuous and discrete variables, which serves to evaluate all possible operation alternatives with the current HEN layout. Moreover, specific domain knowledge is embedded in the form of grey-box models (firstprinciples based plus experimental equations) for the heat exchangers, that have been obtained using data reconciliation (to correct measurements and to estimate the heat-transfer coeficient) and constrained regression (to build up an experimental model for the heat-transfer coeficient) [12]. This model is the core of a mixed-integer economic optimization acting at the stage of choice. In this way, the developed DSS enables a quick reaction to disturbances or load changes. Furthermore, we extended the usual RTO formulation to include the discrete decisions on maintenance so that the DSS can also suggest which heat exchangers are more beneficial to clean at each execution.

Indeed, in the literature there are many examples of similar specific DSS concepts based on mathematical programming, not only in in dustrial applications [13] but also in other areas as medical routines [14], disaster response [15] or transportation [16].

As the proposed DSS software runs in an RTO fashion, it needs to be supplied continuously with plant data, so that it must be integrated with the information technology (IT) infrastructure of the plant. In this case, we make use of PIconnect [17], a Python interface to the OSIsoft Plant Information (PI) system [18], to access (and periodically update) the relevant data for the DSS to run the optimization. Nevertheless, despite proposing an RTO software, the loop cannot be fully closed, as perfectly processed plant-model information cannot be assured. Therefore, the human manager is still the one in charge of taking decisions based on expert knowledge, but now helped by the valuable suggestions provided by the DSS.

For this aim, the results obtained with the RTO need to be presented in a simple and understandable way to the human operators and plant managers. Consequently, friendly DSS interfaces, tailored to the end users' background and responsibility level (e.g. plant operators versus maintenance personnel or plant managers), need to be provided [19]. According to the plant-personnel preferences in this case, we designed a DSS interface in MS Excel which displays the important information and suggested actions computed by the Pyomo-coded optimization [20] in the backend. Moreover, this is a bi-level interface, where plant engineers have further access to modify some optimization parameters and model coeficients, that are not accessible for the operators.

These above mentioned aspects are developed with more detail in the next sections, organized as follows: Section 2 describes the industrial case study and analyzes the problem structure; specific domain knowledge on heat transfer is used together with machine learning in Section 3 to build grey-box models for heat exchangers; Section 4 formulates the mathematical optimization model, core of the DSS software system; Section 5 devotes to the rest of DSS components and implementation issues, whilst a preliminary evaluation of the developed DSS is discussed in Section 6. Finally, Section 7 summarizes important aspects and gives a brief perspective on the future steps.

## 2. Problem identification

The pulp&paper and cellulose-fiber production sectors implicate a series of mechanical and chemical processes. Some of them are energy and resource intensive, e.g. the spinning process where cellulose pulp is turned into fibers through an acid bath [13]. Therefore, heat-recovery systems become somehow mandatory in these plants in order to make use of the remaining heat present in waste streams, thus improving the overall energy and resource consumption.

![](/api/attachments/PPEZNGRM/fulltext/images/d4dda6a674bcbf42ef0103b767cbe2c0abf14c566449d06b801423952d3dfba1.jpg)  
Fig. 1. Diagram of the network layout. W are heat exchangers while S are heat sources. Green outlets from exchangers in Block 1 are the origin of the virtual source S2. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The industrial case study in this paper focuses on the recovery section of a spinning process in the largest EU man-made cellulose fiber producer, Lenzing AG. In this case, the HEN has to heat some acid streams (called product streams hereinafter) up to a desired temperature in order to be reintroduced in the spinning machines. The HEN consists of fifteen heat exchangers that should be able to reach such setpoints by using four heat sources: vapor condensates and waste waters that come from other parts of the plant. Nevertheless, the use of these sources in the HEN involves a cost (pumping and maintenance plus the shadow cost of utilization for other purposes).

The available heat sources are:

• Alkaline waste water, called S1 hereinafter, represented in purple in Fig. 1

Virtual heat source, composed by alkaline waste water (S1) that has already been used in an exchanger. It will be denoted by S2 hereinafter and represented by the green pipes in Fig. 1.

• Vapor condensate, called S3 hereinafter, represented in red in Fig. 1

• Acid waste water, called S4 hereinafter, represented in yellow in Fig. 1.

Note that, as these streams come from other processes and are shared among other parts of the plant, its availability is limited. Moreover, as each one has traces of diferent chemical components, we cannot mix them. Therefore, each heat exchanger can only be connected to one heat source at a time, despite most of them can be connected to more than one. Hence, the heat exchangers can be grouped in subsets, depending on their connectivity to sources, as Table 1 shows.

Note importantly that the amount of S1 that is currently used by the heat-exchangers of ℬ1, is the available S2 (see Fig. 1).

From the point of view of the heat-exchanger connections, we can divide the network into two groups. The first one involves the heat exchangers being connected in parallel, i.e. each one heats a diferent product and the heat sources feed these exchangers in parallel. These are the ones depicted in cyan in Fig. 1, i.e. the exchangers in ${ \mathcal { B } } 1 ,$ ℬ2 and ℬ3.

Table 1  
Allowed source connection to exchangers.

<table><tr><td>Block</td><td>Heat exchanger</td><td>Heat sources</td></tr><tr><td> $\mathcal{B}1$ </td><td>W1, W2, W3, W4, W5</td><td>S1</td></tr><tr><td> $\mathcal{B}2$ </td><td>W6, W7</td><td>S1, S3</td></tr><tr><td> $\mathcal{B}3$ </td><td>W8, W9, W10, W11</td><td>S1, S2, S3</td></tr><tr><td> $\mathcal{B}4$ </td><td>W12, W13</td><td>S3, S4</td></tr><tr><td> $\mathcal{B}5$ </td><td>W14, W15</td><td>S4</td></tr></table>

The other group is composed by the heat exchangers connected in series from the point of view of the product, i.e. the same product goes through all of them (represented in dark blue in Fig. 1). Hence, the temperature setpoint of the product has to be fulfilled only at the outlet of W15. Note that the S4 source circulates in series through these heat exchangers too, but backwards: first it goes to W15 and subsequently passes through W14, W13, and finally through W12. An important feature to take into account is that, as the product is connected in series, there is no need to use all the heat exchangers as long as the setpoint can be reached with just a few of them. If one heat exchanger of the chain is not used, it means that there is not any source passing through it, so there will not be heat transfer and, consequently, the outlet temperature of the product stream will be assumed the same that the one at its inlet. This operation mode is possible because at the source inlet of each heat exchanger there is a bypass valve that can only stand in two positions.

The eficiency of the heat exchangers depends on diferent factors. The most important ones are the transmission area (i.e. exchanger size) and the fouling state. This network uses plate-type heat exchangers, i.e. they are composed of many thin, slightly separated plates that have very large surface areas so that alternate fluids (hot and cold) flow between them to maximize the heat transfer. The total heat-transfer area in these heat exchangers depends on the number of plates. In ad dition, the heat exchangers sufer from fouling (see Fig. 2) that increases their thermal resistance, so that their eficiency progressively reduces over time. Consequently, more flow from the heat source is needed to reach the product setpoint. Eventually, the exchanger needs to be cleaned in order to recover its nominal eficiency. The scheduling of these maintenance tasks is currently done by the operators in a heuristic way, with a policy based just on cleaning the exchangers that have been in operation the longest first.

It is noteworthy that, although the decisions to take may be repetitive and are within a well-defined and stable context, achieving an eficient network operation is a semi-structured decision problem, because there are many decision alternatives regarding the network configuration and the cleaning policy (that are dificult to simultaneously manage by a human operator) and the implications of these are not well known, as prediction models for the heat transfer with fouling in the exchangers is not readily available. In such situation, usual multi attribute decision-making methods based on decision matrices, path weights or preference indexes [2] are hardly applicable. In addition, the economic criteria for choosing beyond mere feasibility is not fully clear as well.

![](/api/attachments/PPEZNGRM/fulltext/images/10ae5095cec2e239633dbad5742cf557bbc85d2d541060df5a7df133a93db8e0.jpg)  
Fig. 2. Depositions due to organic fouling on a plate heat exchanger.

## 3. Modeling the heat transfer

The heat transfer through a heat exchanger (Q′) can be computed by:

$$
Q ^ {\prime} = U \mathrm{ALMTD}\tag{1}
$$

where A is the total heat-transfer surface, LMTD is the logarithmic mean temperature diference between both inlet and outlet of the two streams through the heat exchanger, and U is the overall heat-transfer coeficient.

Once in operation, the U coeficient is the key variable from which the exchanger eficiency depends on. In the equipment sizing and design literature, usually this coeficient is treated as a constant parameter which depends on the constructive materials and on the desired nominal conditions of operation. Nevertheless, it is well known that it significantly varies from several factors, like the fluid speed through the heat-exchanger pipes [12]. As we aim to optimize the HEN in real time (deciding over the sources and flows), in this work we have developed a data-based model of $U ,$ computed using historical plant data of flows and temperatures in diferent operation conditions after a cleaning task.

## 3.1. Data reconciliation

The first step is performing a reconciliation [21] of the raw data collected from sensors using the basic first-principles laws (e.g., mass balances). Usually, raw plant data may present inconsistencies, for instance due to noisy or biased sensors. Therefore, it is necessary to correct the raw information before its further use in DSS's. The way to procedure is solving an optimization problem in which the objective function to minimize is the weighted sum of squares of the deviations between measured data with respect to their estimated $( \mathrm { i . e . , }$ , corrected) values, subject to the physical laws (process model) and other additional imposed relations [22].

In this case, the measured variables that we want to correct are the inlet and outlet temperatures of the product stream $( T \mathrm { i n } _ { c } , T \mathrm { o u t } _ { c } ) _ { \mathrm { : } }$ , of the heat source $( T \mathbf { i n } _ { s }$ , Tout ) and their respective flows $( F _ { c } , \ F _ { s } ) _ { }$ . Data reconciliation in this case is constrained to the energy balance in the heat exchanger (2) where, assuming that there is no heat loss to the ambient, the heat that the heat source gives has to be equal to the heat that the product gains. Both heat magnitudes can be computed using (3) where ρ and Cp are the density and the specific heat respectively, and ΔT is the diference between the inlet and the outlet flow temperatures.<sup>1</sup> Furthermore, the heat that the source gives is equal to the heat transferred across the exchanger (4).

$$
Q _ {s} = - Q _ {c}\tag{2}
$$

$$
Q _ {k} = F _ {k} \rho_ {k} \mathrm{Cp} _ {k} \Delta T _ {k} \quad \forall k \in \{s, c \}\tag{3}
$$

$$
Q ^ {\prime} = Q _ {s}\tag{4}
$$

As the actual value of U is not measurable in real time, this will become a decision variable to be estimated by data reconciliation.

From the analysis of the reconciliation results, we have realized the existence of an inconsistency provoked by the presence of a bypass valve after the location of the inlet product flowmeter, and that the heat-source flowmeter becomes saturated beyond a value. An example of these issues is shown in Fig. 3, where we compare the product flow data obtained from measurements with the values corrected by

![](/api/attachments/PPEZNGRM/fulltext/images/74742df110c4dea1fe7efe2cc4faf232f9aff8e96d8ac2bd35949610c707f982.jpg)  
Fig. 3. Comparison between the measured and corrected values for $F _ { c } .$

reconciliation.

## 3.2. Regression models

Once reliable data and estimated values of U in diferent operation conditions are available, the aim is to find an experimental relationship (black-box model) $U = f ( F , T )$ . For this aim, we constrain f(⋅) to be a polynomial in its arguments, and we used SOS constrained regression [12] both to fit the data and to enforce coherent physical model responses. The best model obtained<sup>2</sup> is (5), a third-degree polynomial where U depends just on the flows, as the temperature influence has resulted to be negligible.

$$
U = \mathrm{a} _ {0} + \mathrm{a} _ {1} F _ {s} + \mathrm{a} _ {2} F _ {c} + \mathrm{a} _ {3} F _ {s} ^ {2} + \mathrm{a} _ {4} F _ {s} F _ {c} + \mathrm{a} _ {5} F _ {s} ^ {3}\tag{5}
$$

The model parameters $\theta = \{ { \tt a } _ { 0 } , { \tt a } _ { 1 } , { \tt a } _ { 2 } , { \tt a } _ { 3 } , { \tt a } _ { 4 } , { \tt a } _ { 5 } \}$ are independent of the operation conditions, but they depend on the heat-exchanger features. Hence, the exchangers have been grouped in three sets according to their sizes (small, medium and large heat-transfer areas) so that the procedure had to be repeated to get three diferent sets of values for the model parameters.

In order to give an insight of the goodness of fit, Fig. 4 shows some values of U estimated by data reconciliation and their corresponding ones predicted by (5), for a medium-size heat exchanger.

## 3.3. Fouling contribution

As mentioned in Section $^ { 2 , }$ the heat-transfer capacity of a heat exchanger is limited by the fouling. Therefore, as the regression models (5) have been fitted using data of clean heat exchangers, the actual U over time will always be below than the predicted one. To tackle this issue, we correct (5) with an additional term, $K ,$ that accounts for the state of fouling. Indeed, the state of fouling K can be monitored online by just comparing the actual heat transfer with the predicted by the “clean model” [23].

$$
U = \mathrm{a} _ {0} - K + \mathrm{a} _ {1} F _ {s} + \mathrm{a} _ {2} F _ {c} + \mathrm{a} _ {3} F _ {s} ^ {2} + \mathrm{a} _ {4} F _ {s} F _ {c} + \mathrm{a} _ {5} F _ {s} ^ {3}\tag{6}
$$

This way, we can not only predict the heat-transfer capacity due to the allocation decisions at each time instant, but we will also be able to provide suggestions on which heat exchangers are more beneficial to be cleaned according to an economic criterion, thus enriching the decision-making process. See next sections.

## 4. DSS software system

The core of the DSS is an optimization problem which decides the distribution of flows and the use of sources in the network in real time, fulfilling the product temperature setpoints at the lowest cost. Moreover, this basic outcome is also extended with the additional functionality of suggesting which heat exchangers are beneficial to be cleaned. In this regard, note that the proposed DSS will not address full maintenance scheduling over a time horizon [24]. The end decisions on maintenance scheduling also rely on the plant personnel, being the proposed DSS here just an additional support for them.

![](/api/attachments/PPEZNGRM/fulltext/images/cca1bedcac70a551b1465d0b15e359f96ba2961ddf2ef4ab21ec9c70b9ca4213.jpg)  
Fig. 4. Goodness of fit for U: estimated values by DR (blue) with their corresponding model predictions (red). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The optimization problem builds upon a mixed continuous-discrete mathematical model, which accounts for all allocation alternatives of the 4 diferent sources among the 15 heat exchangers, computing the outlet temperatures of all involved streams in each case. The following sets of entities and variables are previously defined to build such a model.

## 4.1. Sets and decision variables

The set $\mathcal { W }$ is defined to contain all heat exchangers. From the point of view of heat-sources connectivity in each heat exchanger, $\mathcal { W }$ has already been divided in five subsets $\mathcal { W } = \{ \mathcal { B } 1 \cup \mathcal { B } 2 \cup \mathcal { B } 3 \cup$ 4 5}, as Table 1 shows. However, $\mathcal { W }$ can also be split in other two diferent subsets, $\mathcal { W } = \{ \mathcal { W } _ { p } \cup \mathcal { W } _ { s } \} \colon \mathcal { W } _ { p }$ includes the heat exchangers with the products connected in parallel and $\mathcal { W } _ { s }$ lists those where the product flows in serial connection through them.

The set $\mathcal { S }$ gathers all the heat sources in the network. Note that we do not define a set for product streams, because they are fixed for each heat exchanger, so these are just input data for the optimization.

Three sets of decision variables are employed in the model:

$X _ { s , w } \colon$ Binary variables which, when active $( X _ { s , w } = 1 )$ , link the heat source s to the heat exchanger w.

$F _ { s , w } \colon$ Continuous variables belonging to $\mathbb { R } ^ { + }$ that set the flow of heat source s to heat exchanger w.

$Y _ { w } .$ Binary variables that activate $( Y _ { w } = 1 )$ or deactivate $( Y _ { w } = 0 )$ the cleaning in heat exchanger w.

## 4.2. Model constraints

The core of the HEN model are the constraints which describe the network operation. They are based on first principles and logic statements.

First, the total amount of heat source S2 depends on the amount of used S1 in the heat exchangers ℬ1 (see Fig. 1):

$$
\mathrm {F_ {T,S2}} = \sum_ {w} ^ {\mathcal {B} 1} F _ {\mathrm{S1}, w}\tag{7}
$$

Consequently, the inlet temperature of source S2 depends on the S1 temperatures at the outlet of exchangers ℬ1:

$$
T \mathrm{in} _ {\mathrm{S2}} = \frac {\sum_ {w} ^ {\mathcal {B} 1} T \mathrm{out} _ {\mathrm{S1} , w} F _ {\mathrm{S1} , w}}{\sum_ {w} ^ {\mathcal {B} 1} F _ {\mathrm{S1} , w}}\tag{8}
$$

Also, not all heat exchangers can be physically connected to all heat sources (just the ones described in Table 1), so there must be a constraint in the model that blocks the non-existent links from sources to heat exchangers, denoted by the set ℳ in (9).

![](/api/attachments/PPEZNGRM/fulltext/images/5dc50ed4f301ca6a32ec8798881c33fc17db65c74e39d3aaedc8aac3adf01d87.jpg)  
Fig. 5. Detail of the heat exchangers connected in series. Grey dots represent the location of the bypass valves.

$$
X _ {s, w} = 0 \forall s, w \in \mathcal {M}\tag{9}
$$

On the one hand, since the heat sources cannot be mixed, the heat exchangers can only use a single source (if any) at a time:

$$
\sum_ {s} ^ {\mathscr {S}} X _ {s, w} \leq 1 \forall w \in \mathscr {W}\tag{10}
$$

On the other hand, if a heat source is not connected to a heat ex changer, its flow is zero, otherwise it is bounded by an upper limit $\overline { { \mathrm { F } _ { w } } } ,$ as stated in (11).

$$
F _ {s, w} \leq \overline {{\mathrm{F} _ {w}}} X _ {s, w} \forall w \in \mathscr {W}\tag{11}
$$

The diferent connection possibilities of the heat source S4 in $\mathcal { W } _ { s }$ (as the bypass valves can switch between feeding the exchanger or not, see Fig. 5) are modeled by the following constraints.

Firstly, the S4 flow has to be the same in all connected heat exchangers. To state this constraint, we formulate the system of equations shown in (12), where M is a big enough value (for instance M can be set to three times the $\mathrm { F } _ { \mathrm { T } , S 4 }$ in (20)).

$$
\sum_ {w \neq \beta} ^ {\mathcal {W} _ {s}} F _ {\mathrm{S4}, w} \leq F _ {\mathrm{S4}, \beta} \sum_ {w \neq \beta} ^ {\mathcal {W} _ {s}} X _ {\mathrm{S4}, w} + M (1 - X _ {\mathrm{S4}, \beta}) \forall \beta \in \mathcal {W} _ {s}\tag{12}
$$

With (12) the model has the possibility of switching of any of the exchangers from W12 to W15, ensuring that the ones in operation get the right heat flow in series through them. An illustrative example is provided in Appendix A.

Secondly, the inlet temperatures for both product and heat source depend on the outlet of the previous heat exchanger in the direction of the stream. For the hot-stream side, note indeed that the inlet temperature will depend on the outlet of the previous but connected heat exchanger.

$$
\begin{array}{l} T \mathrm{in} _ {\mathrm{S4}, w} = \sum_ {j = \mathrm{W15}} ^ {w - 1} \left(T \mathrm{out} _ {\mathrm{S4}, j} X _ {\mathrm{S4}, j} \prod_ {j = \mathrm{W15}} ^ {w - 1} (1 - X _ {\mathrm{S4}, j + 1})\right) \\ \qquad + T \mathrm{in} _ {\mathrm{S4}, \mathrm{W15}} \prod_ {j = \mathrm{W15}} ^ {w - 1} (1 - X _ {\mathrm{S4}, j}) \forall w \in \mathscr {W} _ {s} \end{array}\tag{13}
$$

To clarify this last constraint the reader is referred to Appendix B. Finally, analogous to the DR in Section 3.1, this model enforces the energy balances in each heat exchanger, eqs. (1)–(4). Nevertheless, as now there may be more than one heat source able to feed an exchanger, these equations are expanded as follows:

$$
\sum_ {s \in \mathcal {S}} Q _ {s, w} = - Q _ {c, w} \forall w \in \mathcal {W}\tag{14}
$$

$$
Q _ {k, w} = F _ {k, w} \rho_ {k} \mathrm{Cp} _ {k} \Delta T _ {k, w} \forall k \in \{s, c \}\tag{15}
$$

$$
Q _ {s, w} = U _ {s, w} \mathrm{A} _ {w} \mathrm{LMTD} _ {s, w} \forall s \in \mathscr {S}, \forall w \in \mathscr {W}\tag{16}
$$

where the experimental expression for U obtained in Section 3.2 is recalled in (17) to compute Q for each heat exchanger. Note however that the fouling factor $K _ { w }$ is multiplied by $( 1 ~ - ~ Y _ { w } )$ in order to provide the model with the ability to choose between operating exchanger w with the actual eficiency or with the nominal one, as if it would be freshly clean. Moreover, in order to fulfill (14) when the source s is not used in exchanger w $( { \mathrm { i . e . } } Q _ { w , s } = 0 )$ , the term $( a _ { 0 } - K _ { w } ( 1 - Y _ { w } ) )$ ) is multiplied<sup>3</sup> by $X _ { s , w } .$ In this way, in combination with (11), the flow is also set to zero when $X _ { s , w } = 0 \mathrm  $ , thus forcing U and the heat transfer to be zero too.

$$
\begin{array}{r l} & U _ {s, w} = (\mathrm{a} _ {0, w} - K _ {w} (1 - Y _ {w})) X _ {s, w} + \mathrm{a} _ {1, w} F _ {s, w} + \mathrm{a} _ {2, w} F _ {c} + \mathrm{a} _ {3, w} F _ {s, w} ^ {2} \\ & \qquad + \mathrm{a} _ {4, w} F _ {s, w} F _ {c} + \mathrm{a} _ {5, w} F _ {s, w} ^ {3} \quad \forall s \in \mathcal {S}, \forall w \in \mathcal {W} \end{array}\tag{17}
$$

In this mathematical representation of the HEN, $\mathbf { A } , \mathsf { \Gamma } _ { 9 } , \mathbf { C p } ,$ , and $\overline { { \mathrm { F } _ { w } } } ,$ , as well as the coeficients a are known fixed values.

## 4.3. Operation constraints

In addition to the previous constraints that described the behavior of the HEN, there are also production goals to fulfill: the outlet product streams have to reach certain temperature setpoints, (18). These constraints will afect only the heat exchangers connected in parallel and the last heat exchanger in the chain of those connected in series.

$$
T o u t _ {c, w} \geq \mathrm{SP} _ {w} \forall w \in \mathscr {W} _ {\mathrm{p}} \cup \mathrm{W15}\tag{18}
$$

Moreover, the maximum flow available at the heat sources cannot be exceeded, (19). For the source S4, as it is connected in series, the flow in every exchanger has to be lower than the maximum available, (20).

$$
\begin{array}{l} \sum_ {w} ^ {\mathcal {W}} F _ {s, w} \leq \mathrm{F} _ {\mathrm{T}, s} \quad \forall   s \in \{\mathrm{S1}, \mathrm{S2}, \mathrm{S3} \} \\ F _ {\mathrm{S4}, w} \leq \mathrm{F} _ {\mathrm{T}, \mathrm{S4}} \quad \forall   w \in \mathcal {W} _ {s} \end{array}\tag{19}
$$

(20)

The values for $\mathrm { F } _ { c , w } , \mathsf { S P } _ { w } ,$ , Tin and $\mathrm { F } _ { \mathrm { T } , s }$ change over time, so they can be read from the information system of the factory in real time.

## 4.4. Objective function

The aim is to minimize the normalized cost of operation per time unit. This cost comes from the consumption of each source (i.e. the total used flow) times its price,<sup>4</sup> P . Note that, for the sources connected in parallel, the total flow is the sum of the flows used in each heat exchanger, J in (22), meanwhile for S4 the consumption is just the flow that goes through one of the connected exchangers. However, due to the fact that some of these heat exchangers could not be connected to S4, we will compute such flow via the dummy decision variable $F _ { S 4 } \in \mathbb { R } ^ { + }$ and the linear constraints (21), giving J in (22).

<table><tr><td></td><td>PRODUCT STREAMSFLOW, TEMPERATURES AND SETPOINT</td><td>HEAT SOURCES STREAMSFLOW AND TEMPERATURES</td><td colspan="2"></td></tr><tr><td>HEAT EXCHANGERS</td><td>DATA OBTAINED FROMTHE PI SYSTEM INBLUE,RESULTS OF THEOPTIMISATION IN BLACK(ORREDIF INFEASIBLE)</td><td>SELECTED SOURCEIN GREEN,FORBIDEN CONNECTIONSWITH A DASH</td><td>CLEANING SUGGESTION</td><td>OPERATION TIMEAND FOULINGOBTAINEDFROM THE PISYSTEM INBLUE</td></tr></table>

Fig. 6. Designed concept for the DSS dashboard, tailored to plant operators

$$
F _ {\mathrm{S} 4} \leq F _ {\mathrm{T}, \mathrm{S} 4}, \quad F _ {\mathrm{S} 4} \leq \sum_ {w \in \mathscr {W} _ {s}} F _ {\mathrm{S} 4, w}, \quad F _ {\mathrm{S} 4} \geq F _ {\mathrm{S} 4, w} \forall w \in \mathscr {W} _ {s}\tag{21}
$$

$$
J _ {\mathrm{p}} := \sum_ {s} ^ {\mathcal {S} \backslash \mathrm{S4}} \sum_ {w} ^ {\mathcal {W} _ {\mathrm{p}}} \mathrm{P} _ {s} F _ {s, w} J _ {\mathrm{s}} := \mathrm{P} _ {\mathrm{S4}} F _ {\mathrm{S4}}\tag{22}
$$

In addition, the objective function must also take into account the cost of the potential cleaning tasks to perform. However, the cleaning tasks have a fixed cost, $\mathrm { P _ { C } , }$ which must be normalized to be comparable with the operation cost of the HEN. Hence, $\mathrm { P _ { C } }$ is amortized over the operation time of the heat exchanger since its last cleaning, $t _ { w } .$ Thus, the normalized cost of the cleaning tasks will be:

$$
J _ {c l e a n} := \sum_ {w} ^ {\mathcal {W}} \frac {Y _ {w} \mathrm{P} _ {\mathrm{C}}}{t _ {w}}\tag{23}
$$

In this way, the economic objective function $J : = J _ { \mathrm { p } } + J _ { s } + J _ { c l e a n }$ (i.e. the total normalized cost) defines an instantaneous trade-of between operation and cleaning, where the cleaning cost is depreciated over time whilst the cost of operation progressively increases due to fouling (more heat flow is needed to reach the product temperature setpoints).

In summary, the optimization problem to be solved in real time is:

$$
\begin{array}{l l} \underset {F _ {\mathrm{S4}}, F _ {s, w}, X _ {s, w}, Y _ {w}} {\text {Minimize}} & J _ {\mathrm{p}} + J _ {\mathrm{s}} + J _ {\text {clean}} + \alpha \sum_ {w} ^ {\mathscr {W} _ {\mathrm{s}}} \sum_ {s} ^ {\mathscr {S}} X _ {s, w} \\ \text {subject to:} & \text {Modelconstraints(7) - (21)} \\ & F _ {\mathrm{S4}}, F _ {s, w} \in \mathbb {R} ^ {+}, X _ {s, w}, Y _ {w} \in \{0, 1 \} \end{array}\tag{24}
$$

Where we included an additional term in the objective function (α > 0 user-defined weight) to penalize the connection of serial heat exchangers if it is not strictly necessary to reach the product setpoints. In this way, α serves as a tuning parameter to control the nervousness [25] of the RTO solutions.

This optimization becomes a mixed-integer nonlinear programming (MINLP) problem. It involves 136 decision variables (75 binaries) and it is solved with the NLP-based branch-and-bound algorithm Bonmin [26]. It elapses about 120 s average in an Intel® Core™ i7–7700 work station to get a solution with zero relative gap. Therefore, as this RTO runs in an hourly basis (sensible frequency to account for realistic changes in setpoints or available source flows), the computational time does not represent a major issue.

Remark. Note that if the optimization sets $Y _ { w } = 1$ for some heat exchanger w, it is considered that such exchanger performs as fully clean by (17) and its corresponding costs of cleaning are included in the objective function by (23). This way, the designed DSS provides sug gestions for cleaning in real time, which aim to provide the best global economic tradeof.

## 5. DSS design & implementation

A DSS consists of three main components: a database which may contain data from various sources; the software system which contains the models used to analyze the data and to choose the best course of action, and a suitable interface to inform and to interact with the human user [9].

In our case, the data for analysis comes from two sources: the one from expert knowledge, more static with time, and directly reflected by the optimization model (e.g. physical laws, possible connections of heat sources to exchangers, etc.); and the operation data that changes over time (inlet stream temperatures, temperature setpoints, inlet flows, the state of fouling, prices, etc.). In Lenzing, these plant data are already recorded in real time by the OSIsoft PI system. Thus, we access them via PIconnect [17] in order to feed the DSS software system in real time, i.e., before each optimization run. As described in the previous section, the DSS software system solves the optimization problem (24) in real time. It has been coded in Pyomo-Python [20], a toolbox for eficient numerical optimization and control.

## 5.1. User interface

The DSS is completed with a user interface developed in MS Excel according to the end-user preferences. Its layout is designed to give a suitable overview with relevant information of the heat-recovery process during production. The operators and managers are supplied with the dashboard concept shown in Fig. 6, which displays both the computed optimal solution for the current time and the data used to obtain it.

The heat exchangers present in the network will be ordered in rows. Then, each column will represent the features of the heat-exchanger streams, which can be separated in four sections. The first column lists the heat exchangers while the second set of columns provides information about the cold streams to be heated: the flow, inlet temperature, setpoint to achieve and outlet temperature. The third section gives information about the heat sources with the suggested connections to exchangers (they will be highlighted in green, with a dash indicating an impossible connection between source and exchanger). The last columns devote to the cleaning suggestions: the operation time since last cleaning, the estimated state of fouling $K _ { w } ,$ and the recommended exchangers for cleaning (a green tick if the heat exchanger should be cleaned or a red cross otherwise).

Moreover, to clearly diferentiate the data read from the PI system from the results computed by the RTO, the first will be displayed in blue italics and the second one in black plain text. Furthermore, in the case that the optimization problem resulted infeasible by any reason (i.e. some heat exchangers would not fulfill the product temperature setpoints), the computed values below of the demanded temperature will be highlighted in red. With this visual design, the end user can quickly identify the recommendations given by the RTO and analyze them at a glance.

Fig. 7 depicts a schema of the proposed workflow, showing the interactions of information between the DSS components and end users. Only the plant engineers will have access to the backend (i.e. to the DSS software system) in case model parameters need to be updated, or some constraints need to be modified or added $( \mathbf { e . g . }$ to include a constraint to set up a minimum operation time before cleaning, or limiting the number of exchangers that can be cleaned at once).

![](/api/attachments/PPEZNGRM/fulltext/images/e39bd2e7d2a5e288687f19a29be7e018aaf5bd2b1335c6af3c94cf844ed47f7a.jpg)  
Fig. 7. Proposed workflow within the DSS components and the end users.

## 5.2. Implementation with the control system

The interface allows to interpret the given solution of the RTO, but the end user is who decides whether to follow the recommendations or not.

The DSS developed suggests the heat-source flows that have to feed each heat exchanger so that the product outlet temperatures would ideally reach the desired setpoints according to the model. However. note that heat-exchanger models in this work do not include dynamics, so the actual implementation must be performed by the existing tem perature distributed control system (DCS): PID loops that modify the heat source flow valves to reach the desired product temperature setpoints. This control system is necessary to correct the probable plant model mismatch in (24). Thus, the integration of the DSS recommendations with the existent DCS is as follows: the RTO computes feasible decisions (according to the model) regarding the allocation of sources to exchangers at minimum cost, such that this provides the PID controllers with reachable setpoints. Furthermore, as the temperature dynamics are usually slower than the fluid mechanics one, we propose a minor modification of the existent DCS to include a cascade-control structure, where the intern PID loop sets the flow of the heat source (good initial guess given by the DSS) and the external PID loop just modifies such flow setpoint if necessary to reach the temperature set point, thus compensating any small plant-model mismatch. In this way, the proposed implementation allows a faster response against operation changes in real time.

## 6. Preliminary evaluation

The following sections preliminarily evaluate the proposed DSS by presenting some numbers obtained from tests performed with actual historical data from the plant historian.

## 6.1. Example results

A snapshot of the designed visualization dashboard together with some illustrative values (real ones are omitted due to confidentiality) is depicted in Fig. 8. It gives an overview of the computed nearly-optimal solution with plant data sampled in a random time instant.

In such dataset the product flows ranged from 15 to 140 $m ^ { 3 } / h ,$ , their inlet temperatures from 17 to $4 7 ^ { \circ } \mathrm { C }$ and the setpoints to achieve were between 35 and 60 <sup>∘</sup>C. The inlet temperatures of the heat sources were

70<sup>∘</sup>C for S1, 75<sup>∘</sup>C for S3 and 85<sup>∘</sup>C for S4; and the availability of each one is 300 $m ^ { 3 } / h$ for S1 and S3, and 150 $m ^ { 3 } / h$ for S4. Data on the heattransfer areas, streams densities, specific-heat capacities and the prices of the heat sources are omitted due to confidentiality agreements with the company. $^ 5 \overline { { \mathrm { F } } } _ { w } = 3 0 0 m ^ { 3 } / h$ for all heat exchangers.

Unfortunately, since the fouling state was not monitored in the past, we do not have values for $K _ { w }$ recorded in the plant historian to test the DSS. Therefore, based on preliminary data monitoring of one exchanger, we found that a good enough initial approximation is to set $K _ { w }$ as the double of the operation time since last cleaning, $K _ { w } = 2 t _ { w } .$ Of course this rough approximation is just for evaluation purposes, and it will be replaced by actual data when the monitoring system will be fully implemented.

In this example, the results obtained prove that it is not necessary to operate with all the heat exchangers that are connected in series. With this data, the product temperature setpoint can be achieved by using just the first heat exchanger in the chain. With respect to the cleaning, the tool surprisingly suggests not to clean all the dirtiest heat exchangers (W2, W8, W7 and W14). Instead, the suggestion is to clean W7, W8 and W10, despite the source used in W8 and W10 is cost free. This can be explained however by the fact that the amount of S2 depends on the used S1 in ℬ1 so, at this point, it is more beneficial to clean these heat exchangers to fulfill the setpoints just using S2 instead of cleaning and switching one of them to S1.

## 6.2. Assessment over time

To test the consistency of the DSS solutions, i.e. to evaluate the socalled nervousness level, we rolled out the optimization of-line for several consecutive days, updating the input data with the current plant state in each run: each day the fouling state is updated according to the operation and the inlet stream temperatures vary with a maximum of 3<sup>∘</sup>C (i.e., to make the test reasonably demanding, we assume that the inlet temperature will be a random number between ± 3<sup>∘</sup>C). We assume that the cleaning tasks suggested are performed on the day, thus resetting the operation time and the fouling state for the next execution. Again, note that this is not a maintenance scheduling, which is out of the scope of this work, as there is not a single optimization for a set of days (time horizon), but several runs done sequentially, one per day. The evolution for fifteen consecutive days is shown in Fig. 9.

Note that the heat-sources allocation changes over time, clearly seen in blocks ℬ3 and ℬ4 where the heat source used in each heat exchanger needs to adapt to the operation conditions of the day. The most significant changes related to the solution nervousness are the ones observed in the heat exchangers connected in series, where the DSS changes not only the heat source but also the heat exchanger used. This is because the product heat demand in these exchangers is not high (usually due to a low input flow) in comparison with the total heating capacity of these 4 exchangers, so the optimization tries to switch between the less fouled ones in order to save a few m<sup>3</sup>/h of source usage. Nonetheless, this behavior, if unacceptable, can be easily attenuated by increasing the value of the tuning parameter α in (24).

<table><tr><td></td><td colspan="4">Product stream</td><td colspan="6">Hot source streams</td><td colspan="3"></td></tr><tr><td>HE</td><td>flow $(m^3/h)$ </td><td>inflow(°C)</td><td>outflow SP(°C)</td><td>outflow(°C)</td><td>S1 flow $(m^3/h)$ </td><td>S2 flow $(m^3/h)$ </td><td>S3 flow $(m^3/h)$ </td><td>S4 flow $(m^3/h)$ </td><td>inflow(°C)</td><td>outflow(°C)</td><td>Cleaning</td><td>Operationtime(days)</td><td>Fouling</td></tr><tr><td>W1</td><td>15</td><td>35.0</td><td>60.0</td><td>67.0</td><td>40.92</td><td>-</td><td>-</td><td>-</td><td>70.0</td><td>58.2</td><td>✕ 0</td><td>10.00</td><td>20.00</td></tr><tr><td>W2</td><td>60</td><td>25.0</td><td>40.0</td><td>40.7</td><td>36.29</td><td>-</td><td>-</td><td>-</td><td>70.0</td><td>43.9</td><td>✕ 0</td><td>15.00</td><td>30.00</td></tr><tr><td>W3</td><td>50</td><td>30.0</td><td>50.0</td><td>50.0</td><td>49.62</td><td>-</td><td>-</td><td>-</td><td>70.0</td><td>49.7</td><td>✕ 0</td><td>5.00</td><td>10.00</td></tr><tr><td>W4</td><td>140</td><td>47.0</td><td>55.0</td><td>55.0</td><td>54.43</td><td>-</td><td>-</td><td>-</td><td>70.0</td><td>49.3</td><td>✕ 0</td><td>0.00</td><td>0.00</td></tr><tr><td>W5</td><td>130</td><td>45.0</td><td>55.0</td><td>55.0</td><td>61.93</td><td>-</td><td>-</td><td>-</td><td>70.0</td><td>48.9</td><td>✕ 0</td><td>3.00</td><td>5.00</td></tr><tr><td>W6</td><td>50</td><td>45.0</td><td>60.0</td><td>60.0</td><td>0.00</td><td>-</td><td>32.27</td><td>-</td><td>75.0</td><td>51.6</td><td>✕ 0</td><td>3.00</td><td>6.00</td></tr><tr><td>W7</td><td>25</td><td>40.0</td><td>60.0</td><td>60.0</td><td>0.00</td><td>-</td><td>30.68</td><td>-</td><td>75.0</td><td>58.6</td><td>✕ 1</td><td>17.00</td><td>35.00</td></tr><tr><td>W8</td><td>60</td><td>20.0</td><td>40.0</td><td>40.0</td><td>0.00</td><td>131.67</td><td>0.00</td><td>-</td><td>50.0</td><td>40.9</td><td>✕ 1</td><td>22.00</td><td>45.00</td></tr><tr><td>W9</td><td>60</td><td>20.0</td><td>45.0</td><td>45.0</td><td>0.00</td><td>0.00</td><td>50.95</td><td>-</td><td>75.0</td><td>45.4</td><td>✕ 0</td><td>6.00</td><td>12.00</td></tr><tr><td>W10</td><td>60</td><td>25.0</td><td>40.0</td><td>40.0</td><td>0.00</td><td>76.58</td><td>0.00</td><td>-</td><td>50.0</td><td>38.2</td><td>✕ 1</td><td>12.00</td><td>25.00</td></tr><tr><td>W11</td><td>45</td><td>17.0</td><td>35.0</td><td>35.0</td><td>0.00</td><td>34.95</td><td>0.00</td><td>-</td><td>50.0</td><td>26.7</td><td>✕ 0</td><td>1.00</td><td>3.00</td></tr><tr><td>W12</td><td>50</td><td>25.0</td><td>-</td><td>45.0</td><td>-</td><td>-</td><td>21.86</td><td>0.00</td><td>75.0</td><td>29.0</td><td>✕ 0</td><td>12.00</td><td>24.00</td></tr><tr><td>W13</td><td>50</td><td>45.0</td><td>-</td><td>45.0</td><td>-</td><td>-</td><td>0.00</td><td>0.00</td><td>0.0</td><td>0.0</td><td>✕ 0</td><td>11.00</td><td>22.00</td></tr><tr><td>W14</td><td>50</td><td>45.0</td><td>-</td><td>45.0</td><td>-</td><td>-</td><td>-</td><td>0.00</td><td>0.0</td><td>0.0</td><td>✕ 0</td><td>18.00</td><td>36.00</td></tr><tr><td>W15</td><td>50</td><td>45.0</td><td>45.0</td><td>45.0</td><td>-</td><td>-</td><td>-</td><td>0.00</td><td>0.0</td><td>0.0</td><td>✕ 0</td><td>9.00</td><td>18.00</td></tr></table>

Fig. 8. Snapshot of the operator interface. Blue italics depict data read from the PI system. Results from the optimization (predicted outlet temperatures, heat-source flows and cleaning suggestions) are given in black plain text. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

<table><tr><td>Day/ HE</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td></td></tr><tr><td rowspan="5">B1</td><td>W1</td><td>41.26</td><td>41.22</td><td>40.88</td><td>40.91</td><td>39.36</td><td>39.30</td><td>19.13</td><td>19.13</td><td>19.20</td><td>19.28</td><td>41.07</td><td>19.44</td><td>31.11</td><td>19.60</td><td>40.47</td></tr><tr><td>W2</td><td>37.30</td><td>36.88</td><td>35.57</td><td>35.31</td><td>38.96</td><td>39.00</td><td>32.49</td><td>32.59</td><td>32.68</td><td>32.77</td><td>39.63</td><td>32.96</td><td>33.06</td><td>33.16</td><td>37.20</td></tr><tr><td>W3</td><td>49.62</td><td>49.76</td><td>49.91</td><td>50.06</td><td>50.21</td><td>50.35</td><td>50.50</td><td>48.91</td><td>48.91</td><td>49.05</td><td>49.19</td><td>49.33</td><td>49.48</td><td>49.62</td><td>49.76</td></tr><tr><td>W4</td><td>54.43</td><td>54.47</td><td>54.52</td><td>54.56</td><td>54.61</td><td>54.65</td><td>54.70</td><td>54.74</td><td>54.79</td><td>54.84</td><td>54.88</td><td>54.93</td><td>54.98</td><td>55.03</td><td>55.08</td></tr><tr><td>W5</td><td>61.93</td><td>62.03</td><td>62.10</td><td>62.17</td><td>62.24</td><td>62.31</td><td>62.38</td><td>62.45</td><td>62.52</td><td>62.59</td><td>62.66</td><td>61.77</td><td>61.77</td><td>61.84</td><td>61.90</td></tr><tr><td rowspan="3">B2</td><td>W6</td><td>32.27</td><td>32.33</td><td>32.39</td><td>32.45</td><td>32.51</td><td>32.58</td><td>32.64</td><td>32.70</td><td>32.76</td><td>32.83</td><td>32.10</td><td>32.10</td><td>32.15</td><td>32.21</td><td>32.27</td></tr><tr><td>W7</td><td>30.68</td><td>30.68</td><td>30.79</td><td>30.90</td><td>31.02</td><td>31.13</td><td>31.25</td><td>31.36</td><td>31.48</td><td>31.60</td><td>31.72</td><td>30.68</td><td>30.68</td><td>30.79</td><td>30.90</td></tr><tr><td>W8</td><td>130.65</td><td>130.44</td><td>131.65</td><td>131.80</td><td>133.27</td><td>133.42</td><td>162.83</td><td>164.45</td><td>34.62</td><td>34.71</td><td>134.50</td><td>34.90</td><td>144.37</td><td>159.45</td><td>131.95</td></tr><tr><td rowspan="3">B3</td><td>W9</td><td>50.95</td><td>51.10</td><td>51.24</td><td>50.13</td><td>50.13</td><td>50.26</td><td>50.40</td><td>50.54</td><td>50.67</td><td>50.81</td><td>50.95</td><td>51.10</td><td>51.24</td><td>50.13</td><td>50.13</td></tr><tr><td>W10</td><td>79.06</td><td>79.08</td><td>76.33</td><td>76.16</td><td>76.87</td><td>76.93</td><td>24.52</td><td>24.59</td><td>102.85</td><td>102.49</td><td>77.41</td><td>102.63</td><td>86.03</td><td>24.98</td><td>76.47</td></tr><tr><td>W11</td><td>34.84</td><td>34.86</td><td>35.01</td><td>35.05</td><td>35.23</td><td>35.27</td><td>39.87</td><td>39.96</td><td>44.01</td><td>44.24</td><td>35.52</td><td>44.31</td><td>16.94</td><td>40.43</td><td>36.00</td></tr><tr><td rowspan="2">B4</td><td>W12</td><td>21.86</td><td>17.82</td><td></td><td></td><td></td><td>17.84</td><td>12.99</td><td></td><td></td><td>21.94</td><td></td><td>21.97</td><td>22.00</td><td>22.02</td><td>22.05</td></tr><tr><td>W13</td><td></td><td></td><td></td><td></td><td>21.85</td><td></td><td></td><td>16.32</td><td>17.85</td><td>21.93</td><td></td><td>17.89</td><td></td><td></td><td></td></tr><tr><td rowspan="2">B5</td><td>W14</td><td colspan="15"></td></tr><tr><td>W15</td><td></td><td>17.76</td><td></td><td></td><td>17.78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 9. Overview of the suggestions provided by the DSS during fifteen consecutive days. Cell colour indicates the heat source linked to the exchanger whilst colour intensity points the fouling state: the higher the intensity, the dirtier the exchanger. A sudden reduction in the intensity indicates a cleaning operation.

## 7. End remarks and further steps

In this work we addressed the problem of optimal operation of an industrial heat-recovery network taking into account the eficiency of the heat exchangers and the use of shared resources simultaneously. The key operational decisions are how to allocate and distribute the heat sources (utilities) among exchangers and to suggest whether a heat exchanger should be cleaned or not. The proposed solution is a specific DSS that keeps the human operator in the loop. This DSS is based on a rigorous mathematical model of the network which is the core of an

MINLP optimization accounting for the current production constraints and the equipment fouling states. The DSS can be fed in real time by the plant PI system, and presents the results of the optimization through a simple Excel interface, designed according to the operator visualization preferences. In this way, the proposed DSS will support the plant operators in such a complex decision-making process in real time, saving resources and reducing the personnel workload. This work is a proof that DSS's based on mathematical models and mixed-integer nonlinear optimization can unlock the potential benefits associated to complex combinatorial problems arising in the daily management of industrial sites.

The preliminary evaluation showed that the decisions proposed by the DSS outperformed those taken by the human operator. A relevant outcome from this evaluation is that the current cleaning policy of “dirtiest first” has been proven no to be the best in all cases. Indeed, knowing which heat exchanger should be cleaned for optimal economic performance is not an easy task, as it depends a lot on diferent interconnected factors. Hence, the proposed DSS not only improves the heatsource distribution. but also helps to configure the cleaning schedule

Nevertheless, this DSS just performs an instantaneous RTO which does not predict the future evolution of the fouling, so the proposed main tenance actions may be suboptimal in the long term. In return for this, our proposed RTO solution does not sufer from the always undesirable turnpike efect [27] typically arising in dynamic optimization and scheduling solutions over a finite future time horizon.

Another drawback of the proposed DSS is relative to the ease of adaptability and flexibility. Ideal DSS's should be formed of simpler pieces such that end users could be able to build and modify them easily. This does not mean that our proposed DSS is a rigid black box, but the complexity of the underlying model requires to be adapted by process experts with assistance from qualified engineers on mathema tical optimization.

Consequently, a future research can focus on: A) developing a components library with models for the individual equipment and a method to provide plug-and-play features to ease the inclusion and modification of the model constraints; and/or B) extending the problem formulation to include a prediction of the fouling dynamics over time, thus allowing the computation of a full production-maintenance schedule of the HEN over a suitable time horizon, a week for example. This last, however, requires a dynamic model to predict the fouling state with time and, possibly, with respect to the flows fed to the exchangers (decision variables). Furthermore, an estimation of the future operation conditions (heat source availability and product inlet temperatures) will be required too, but these estimations are uncertain over a large time horizon, so robust scheduling formulations are foreseen somehow mandatory. In any case, the computational complexity of this MINLP optimization problem will increase exponentially, so decomposition and convexification techniques will be required to cast the problem in a more tractable form.

## Funding

These results received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 723575 (CoPro) and from the Spanish MICIU with FEDER funds under project InCO4In (PGC2018–099312-B-C31). The first author thanks the European Social Fund and the "Consejería de Educación de la Junta de Castilla y León".

## Appendix A. Example of constraints (12)

Consider for instance that heat exchangers W12, W13 and W14 are connected but W15 is not. Then, by developing (12), the sum of W12 and W13 flows must be two times the W14 flow $( \beta = W 1 4 ) $ , the sum of W12 and W14 flows must be two times the W13 flow $( \beta = W 1 3 )$ , and the sum of W13 and W14 flows must be two times the W12 flow $( \beta = W 1 2 )$ , thus leading to the only possible solution of $F _ { S 4 , \mathrm { ~ W 1 2 } } = F _ { S 4 , \mathrm { W 1 3 } } = F _ { S 4 , \mathrm { W 1 4 } }$ . Meanwhile, the sum of W12, W13 and W14 flows is allowed to be a large number (β = W15).

## Appendix B. Example of constraints (13)

Eq. (B.1) below develops the case for the W13 inlet temperature, which depends on W14 using S4 as heat source. If not, it depends on W15 working with S4. Otherwise, the temperature will be directly the one at the source S4.

$$
T \mathrm{in} _ {\mathrm{S4}, W 1 3} = T \mathrm{out} _ {\mathrm{S4}, W 1 4} X _ {\mathrm{S4}, W 1 4} + T \mathrm{out} _ {\mathrm{S4}, W 1 5} X _ {\mathrm{S4}, w 1 5} (1 - X _ {\mathrm{S4}, W 1 4}) + T \mathrm{in} _ {\mathrm{S4}, W 1 5} (1 - X _ {\mathrm{S4}, W 1 5}) (1 - X _ {\mathrm{S4}, W 1 4})\tag{B.1}
$$

## References

[1] S. Krämer, S. Engell, Resource Eficiency of Processing Plants: Monitoring and Improvement, John Wiley & Sons, 2017.

[2] M. Rashidi, M. Ghodrat, B. Samali, M. Mohammadi, Decision support systems, in: M. Pomfyova (Ed.), Management of Information Systems, IntechOpen, Rijeka, 2018(Ch. 2).

[3] S. Engell, I. Harjunkoski, Optimal operation: scheduling, advanced control and thei integration, Comput. Chem. Eng. 47 (2012) 121–133.

[4] C. de Prada, J.L. Pitarch, Real-Time Optimization (RTO) Systems, John Wiley &

[5] A. Galan, C. de Prada, G. Gutierrez, D. Sarabia, I.E. Grossmann, R. Gonzalez, Implementation of RTO in a large hydrogen network considering uncertainty, Optim. Eng. (2019) 1–30.

[6] J. Han, G.S. Forman. A. Elgowainy. H. Cai, M. Wang, V.B. DiVita, A comparative assessment of resource efficiency in petroleum refining. Fuel 157 (2015) 292–298

[7] M.P. Marcos, J.L. Pitarch, C. de Prada, C. Jasch, Modelling and real-time optimisation of an industrial cooling-water network. 2018 22nd International Conference on System Theory, Control and Computing (ICSTCC), 2018, pp. 591–596.

[8] C. de Prada, D. Sarabia, G. Gutierrez, E. Gomez, S. Marmol, M. Sola, C. Pascual, R. Gonzalez, Integration of RTO and MPC in the hydrogen network of a petrol re finery, Processes 5 (1) (2017).

[9] R.H. Sprague, H.J. Watson, Decision Support Systems: Putting Theory into Practice (1986).

[10] K. Thulukkanam, Heat Exchanger Design Handbook, CRC press, 2013.

[11] T.R. Bott, Fouling of Heat Exchangers, Elsevier, 1995.

[12] J.L. Pitarch, A. Sala, C. de Prada, A systematic grey-box modeling methodology vi data reconciliation and SOS constrained regression, Processes 7 (3) (2019).

[13] M. Kalliski, J.L. Pitarch, C. Jasch, C. de Prada, Support to decision-making in a network of industrial evaporators, RIAI Rev. Iberoam. Autom. Inform. Ind. 16 (1) (2019) 26–35.

[14] A. Kandakoglu, A. Sauré, W. Michalowski, M. Aquino, J. Graham, B. McCormick, A decision support system for home dialysis visit scheduling and nurse routing. Decision Support Systems, 2019, p. 113224.

[15] F. Caydur, A. Sebatli, A decision support tool for allocating temporary-disaster-re-

[16] G. Erdoğan, N. Stylianou, C. Vasilakis, An open source decision support system for facility location analysis, Decis, Support, Syst, 125 (2019) 113116

[17] H. Van den Berg, PIconnect 0.8.0, pypi.org/project/PIconnect, (2020).

[18] OSISoft, OSISoft PI system, URL, 2020. www.osisoft.com/pi-system/.

[19] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Greenwood Publishing Group, 2002.

[20] W.E. Hart, C.D. Laird, J.-P. Watson, D.L. Woodruf, G.A. Hackebeil, B.L. Nicholson, J.D. Siirola, Pyomo–Optimization Modeling in Python, 2nd ed., vol. 67, Springer Science & Business Media, 2017.

[21] M. Leibman, T. Edgar, L. Lasdon, Eficient data reconciliation and estimation for dynamic processes using nonlinear programming techniques, Comput. Chem, Eng 16 (10) (1992) 963–986

[22] D. Sarabia, C. de Prada, E. Gómez, G. Gutierrez, S. Cristea, M. Sola, R. Gonzalez. Data reconciliation and optimal management of hydrogen networks in a petrol refinery, Control. Eng, Pract. 20 (4) (2012) 343–354.

[23] Lenzing, D2.5 Final Report on Equipment Degradation Modelling, Outcomes of the CoPro Project, URL, 2019. www.spire2030.eu/copro.

[24] C.G. Palacín, J.L. Pitarch, C. Jasch, C.A. Méndez, C. de Prada, Robust integrated production-maintenance scheduling for an evaporation network, Comput. Chem. Eng. 110 (2018) 140–151.

[25] G. Dalle Ave, M. Alici, I. Harjunkoski, S. Engell, An explicit online resource-task network scheduling formulation to avoid scheduling nervousness, in: A.A. Kiss, E. Zondervan, R. Lakerveld, L. Özkan (Eds.), 29th European Symposium on Computer Aided Process Engineering, Elsevier, 2019, pp. 61–66 Vol. 46 of Computer Aided Chemical Engineering.

[26] P. Bonami, L.T. Biegler, A.R. Conn, G. Cornuéjols, I.E. Grossmann, C.D. Laird, J. Lee, A. Lodi, F. Margot, N. Sawaya, et al., An algorithmic framework for convex mixed integer nonlinear programs, Discret. Optim. 5 (2) (2008) 186–204.

[27] D.A. Carlson, A. Haurie, Infinite Horizon Optimal Control: Theory and Applications,

María P. Marcos is currently Ph. D. student at the University of Valladolid. Her research interests include modeling and optimization of process systems. She holds a M.Sc. Degree in Processes and Industrial Systems Engineering from the University of Valladolid (2017) and an Engineer's Degree in Chemical Engineering from the University of Alicante (2016). As predoctoral researcher, she participates in several national and international compe titive research projects with public funding.

José Luis Pitarch received the M.Sc. degree in Industrial Engineering with honors in 2008 at Jaume I University of Castellón (Spain). Then, after a short period in industry with BP Oil Refinery of Castellón as process control engineer in 2009, he moved back to academia and he received the M.Sc. degree in 2010 and the Ph.D. degree in Control Engineering in 2013, both from the Polytechnical University of Valencia (Spain). Currently he's with the University of Valladolid (Spain), with the Systems Engineering and Control Department as postdoc researcher. He coauthored 28 conference papers, 13 indexed (JCR) journal papers, a book and three book chapters. His main research interests include (but not limited to) process control & real-time optimization, production-maintenance scheduling, grey-box and fuzzy modeling, data-reconciliation, stability analysis and disturbance-invariant control of nonlinear systems. He currently coordinates the Spanish Modeling, Simulation and Optimization group, and he is member of the directive board of the Spanish IFAC Committee of Automation (CEA)

César De Prada graduated in Physics (electronics) in 1973 and then obtain his PhD at the University of Valladolid (Spain). He became full professor in 1987 in the Autonomous University of Barcelona and then, he moved to the University of Valladolid joining th

Systems Engineering and Automatic Control Department, that he has headed several times. Prof. De Prada has been President of the Spanish association of Automatica (CEA). From 1999 to 2004 he was appointed manager for the National Research Program in Industrial Production and Design of the Spanish Ministry of Science and Technology. He has received the ISA-Spain Prize to the best professional in 2008 and the national prize of Automatica in 2016. He has also been research visitor in the Warren Spring Lab. (UK) and in the universities of Bradford, UMIST and Carnagie-Mellon. His research activity has been developed through more than 80 research proiects and contracts, as well as with the participation in several European and Latin-american programs. His research interest is focused on Process Systems Engineering and, in particular, scheduling, advanced control in large-scale systems, process modeling, simulation and economic optimization considering uncertainty, hybrid and nonlinear dynamics. He is author in more than 145 journal papers and book chapters, more than 260 international conference papers and he has supervised 30 Ph.D. theses in the topic.
