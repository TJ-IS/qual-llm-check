---
otero_id: 13456
otero_key: "7CNHPCN5"
title: "A risk oriented model to assess strategic decisions in new product development projects"
authors: "F. Marmier; D. Gourc; F. Laarz"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A risk oriented model to assess strategic decisions in new product development projects

F. Marmier ⁎, D. Gourc, F. Laarz

Toulouse University - Mines Albi - Industrial Engineering Laboratory, 81013 Albi, France

## a r t i c l e i n f o

Article history: Received 25 April 2012 Received in revised form 3 April 2013 Accepted 9 May 2013 Available online xxxx

Keywords: Decision support system Project planning Project variant Risk management Scenarios Treatment strategy

## a b s t r a c t

The project management team has to respect contractual commitments, in terms of deadlines and budgets, that are often two antagonistic objectives. At the same time, the market becomes more and more demanding as far as costs and delays are concerned while expecting a high quality level. Then, the project management team has to continuously consider novelty and a risk management strategy in order to determine the best balance between bene<sup>fi</sup>ts and risks. Based on the principles of a synchronized process between risk management and project management, and on the concepts of risk scenario, we propose a decision-making tool to help the project manager choose the best way to improve project success rate while controlling the level of risks. As a <sup>fi</sup>nding, the project manager would be able to evaluate and compare different novelties or development strategies taking into account their repercussions on potential risks and risk treatment strategies. Finally, a case study in the aerospace industry and speci<sup>fi</sup>cally on satellite integration and tests is developed to validate this approach.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In the current context of market globalization, and in order to increase their competitiveness, companies have to offer innovative products. They also have to change their ways of production to improve their pro<sup>fi</sup>tability and reactivity. More and more companies use project management tools and methods for managing their innovations, to ensure a better product quality, better deadlines and lower costs. In this context, particular attention is paid to project management methods by decision-makers and academics.

Every project type faces risks, whatever the size or topic concerned. Several characteristics of the project such as the innovation level, high constraints, multinational and political stakeholders, changing environment,… can increase the project risk level. Therefore, the project manager must <sup>fi</sup>nd a compromise to make sure the novelty rate achievable. To reduce the level of risk, the resources used must then be adequate to the ambition. Professional organizations as well as standard bodies have produced guides and books on project management and good practice for several years [15,16,29]. These reference framework documents present the process required for management. Turner [31] proposes a review of progress on the global project management body of knowledge. He states that, even if the internal breakdowns may not be always appropriate, the guide to the PMBoK contains the core elements used by all project managers. The following dimensions are systematically mentioned in the reference framework documents: integration, scope, time, cost, quality, human resources, communication, risk and procurement management.

In the context of a project, and especially in a competitive market, the manager has to continually change his response to risks in order to increase the success rate. He has to take into consideration the set of potential risks before the launching of the project, as well as when running the project. The manager has to evaluate different developments of the project when choosing between exclusive technological novelties for a product. The risk treatment strategy must take into account the repercussion of the novelty on the set of potential risks, to keep the project on budget and on time. Therefore risks have to be correctly evaluated and the strategies correctly chosen to obtain a realistic estimate (cost/duration) of the project.

This paper is speci<sup>fi</sup>cally interested in approaches that take risks into account in managing projects. These approaches aim to anticipate potential phenomena and to measure their possible consequences on the project life or objectives. In the case when the objectives seem to be reachable, the manager pilots the project by selecting the appropriate risk treatment strategies. If the objectives are not reachable, the approach helps identify the elements of the target that have to be renegotiated (cost, time or technical speci<sup>fi</sup>cation).

In the <sup>fi</sup>rst section, we present a literature survey on risk management methodologies, which shows the diversity of the existing approaches; some are dedicated to speci<sup>fi</sup>c domains while others are generic. We illustrate the evaluation problem of the in<sup>fl</sup>uence of risk on project schedule. In the second section we describe our methodology, that deals with the dif<sup>fi</sup>culty of choosing development strategies and/or treatment strategies in a technological innovation context facing potential risks. Finally a case study from the aerospace industry is detailed, we discuss the results obtained and present our conclusions to this research work.

## 2. Literature

## 2.1. Dealing with project risk management

In the literature, the risk management methodologies refer to a standard process presenting the well-known steps: risk identi<sup>fi</sup>cation, risk evaluation and quanti<sup>fi</sup>cation, risk mitigation for treatment and/or impact minimization and risk monitoring [1,8,17,29]. Tixier et al. [30] propose a classi<sup>fi</sup>cation of 62 existing approaches. They sort methods as being deterministic and/or probabilistic, but also qualitative or quantitative.

In a project context corresponding to this work, a risk occurrence may introduce in a project: (1) the modi<sup>fi</sup>cation of existing tasks related to the risk in<sup>fl</sup>uence on duration or cost and (2) the modi<sup>fi</sup>cation of the project structure by treatment strategies (treatment actions are represented by new tasks in the planning). This therefore impacts project planning: cost and duration. The speci<sup>fi</sup>cities of the project context are: the notion of uniqueness (there is no recurrence in the projects), the notion of limited horizon (there are different milestones and contractual commitments), and the notion of a multi-expertise environment (numerous actors with different skills, perceptions and points of view working together). Uniqueness leads to use methods, such as the brainstorming, that are based on the expertise (very limited returns of experience and very few databases are available). The fact that time is limited forces the use of simple methods. Finally, the high number of actors implies that the model must share the information and help obtain a consensus.

Several academic research works propose methods to complement the different phases of the previously presented global approaches, such as the optimization of different criteria during the schedule or after the identi<sup>fi</sup>cation phase. As an example, Kiliç et al. [19] propose an approach to solve a bi-objective optimization problem where the makespan (or project duration) and the total cost both have to be minimized. Different preventive strategies are possible for each risk and a multi-objective genetic algorithm is used to generate a set of pareto optimal solutions. Van de Vonder et al. [32] are interested in generating robust projects by inserting buffers in the project schedule. Using heuristics, their approach aims to minimize project duration and maximize project robustness, which are antagonistic objectives. Depending on the project characteristics, this strategy can be an interesting way to increase solution stability.

In parallel to these global approaches, several authors propose methodologies to manage the risk in projects. Gourc [14] proposes a reading grid of the risk management approaches following two families: the symptomatic approach and the analytic approach. The <sup>fi</sup>rst group of approach, called risk-uncertainty, is associated with approaches where project risk management is transformed into project uncertainty management [33]. The second approach family considers risk as an event that can affect the achievement of the project objectives [3]. According to ISO-Guide73 [18], “Risk can be de<sup>fi</sup>ned as the combination of the probability of an event and its consequences”. Risk is described as an event, which has occurrence characteristics (potentiality to occur) and consequence characteristics on the project objectives (impact in the event of occurrence). Nguyen et al. [25] propose ProRisk, which can model and evaluate the impact of risks on the project cost and the schedule cost. They de<sup>fi</sup>ne the concepts of risk scenario, treatment scenario and project scenario. This project management approach uses synchronized processes of project schedule and risk management [28]. Fang and Marle [12] proposed a simulation-based model to evaluate risks and then to support project managers in making decisions regarding risk response actions. The model integrates the risks and their interactions. The risk interactions are represented by a risk structured matrix [21]. This allows the risk network structure to be described. On that basis the decision maker can be supported in selecting an optimal risk treatment plan considering interactions between risks [13]. They investigate the dif<sup>fi</sup>culty of choosing which action should be carried out to deal with the risk, where there is a known budget constraint. Thus, we notice that these models lead to choices being made. Consequently, the whole decision problem becomes an issue.

## 2.2. The decision process in project risk management

Risks are intrinsic in new product development (NPD) in all industries [20]. Thus <sup>fi</sup>rms need to take initiatives to reduce risks that are related with NPD. The risk management framework should integrate the three most important risk factors that affect NPD performance: technology, marketing, and organization [11]. However, in such an innovation context, it remains dif<sup>fi</sup>cult to acquire knowledge about the sources of uncertainty to decide the way of reducing the risk of failure of the project or resulting product and manage ef<sup>fi</sup>ciently NPD risk [7]. In NPD management, decision-makers have to choose exclusively one orientation as a strategy development according to a global risk level tolerance. As an answer, decision trees (DTs) are regularly used in the literature on decision [5]. DT is a structure that represents decision problems with exclusive and competing solutions. It enables optimal solution to short time dynamic decision problems [6]. Dey [10] illustrates the use of DT to choose strategies of risk mitigation using the expected monetary values (EMVs). Based on decision variables, decision trees help choosing one way and to react accordingly in front of an event. It's dynamic from the left to the right knowing that decision has already been taken, but being able to imagine new ones. New evaluations are possible during the project development and future decisions can differ from the initially planned ones. In the backward induction, the plan is done ahead but studied consequences backward from the possible future end nodes to the imminent decision [9].

Many companies use project in order to develop innovative products. Even if projects are characterized by uniqueness, the expertise provides familiarity with practices. To increase the ef<sup>fi</sup>ciency of innovative projects, two main ways are possible: modifying the product, modifying the project structures and then practices. Both these perspectives lead to modi<sup>fi</sup>cations of the risk level and it is dif<sup>fi</sup>cult to evaluate the balance between risks and bene<sup>fi</sup>ts. If the <sup>fi</sup>rst way requires speci<sup>fi</sup>c and technical skills to reduce for example conception risks, there is no tool helping the project manager evaluate the project risk level when integrating the studied variants of the project and its consequences on (1) the planning of the project, (2) the risks and its associated treatment strategies.

As shown in this literature review, little account is taken of risk and the strategies to deal with it regarding their repercussions on planning. The ability to present the project manager with a range of alternative risk treatments in a risky situation, and the further ability to provide information on the consequences on decision criteria such as project cost and duration should improve the decision-making process. Therefore, there is a need of methodological tools to help measure the repercussion on the risk level of modi<sup>fi</sup>cation on the project structure. In this research work, we make the link between project planning, project management and risk management. To our knowledge, only a few methods can. They mainly apply risk management to an object, but the repercussions on planning are rarely modeled.

By taking into account the fact that well-managed technology risk leads to better NPD performance [22], our objective is to propose a complete framework helping decision-makers to decide novelty and risk prevention strategy. This tool should facilitate the decisionmaking process by making the link between project management and risk management and by analyzing the consequences of a risk “as an event” in a project. It should permit the evaluation of consequences of the changes in practices on project management, particularly on the deadline and cost dimensions. In addition, this environment will be useful for managers, in order to measure the project global risk level, by taking into account the different possible scenarios, as well as helping choose the most suitable risk strategies.

## 3. Model

Making decisions in the choice of modi<sup>fi</sup>cations to improve an existing project is a multicriteria problem. When the project manager makes the decision, the number of criteria used to evaluate the proposal is most often reduced to the main ones: the cost, which is a sensitive and <sup>fi</sup>nite resource and the delay, which traditionally is a matter of contractual commitment. However, when different possible technological novelties are identi<sup>fi</sup>ed to increase the potential for the success of the project, the repercussions on the risks are rarely anticipated by the classical approach. The project manager has to evaluate each potential novelty and its associated risks. Then he must consider the pro<sup>fi</sup>tability of each pair of choices: technological novelty/risk treatment.

## 3.1. Hypothesis

The model we propose is based on four main hypotheses:

– for each project, several novelties are considered to improve its development. Even if the novelty does not completely change the planning, the modi<sup>fi</sup>cations generate repercussions on the risks and their treatment strategies,

– the risk integration to the project management takes into account the deadlines and the cost criteria. The considered impacts (modi<sup>fi</sup>- cation or suppression of an existing task or the insertion of a new task for example) in<sup>fl</sup>uence the project total duration and cost,

– for each risk, several treatment strategies are possible to limit the impacts,

– another hypothesis used for this model is that, when the decision of treatment strategy and project structure has to be made, the task list and the risk list are known and are assumed not to vary, during the considered phase or the sub-project. This research work's objective is not to develop a tool facilitating the datagathering that may be costly in time and effort with a realistic number of tasks.

At any time, the objectives of the model are (1) to analyze the possible scenarios, (2) to evaluate the global risk level, i.e. the global risk level represents the chance, for the project, to satisfy commitments, and (3) to select the best treatment strategies.

## 3.2. Data

$P V ^ { \nu } \left( \nu = 0 , . . . , V \right)$ is a project variant associated to a development strategy of a project, V being the number of possible variants and $P V ^ { 0 }$ is the project reference that is improved by the added modi<sup>fi</sup>cations.

Each $P V ^ { \nu }$ is described by its tasks $T _ { t } ^ { \nu } ( t = 1 \ldots T ^ { \nu } ) , T ^ { \nu }$ being the number of project tasks of the project variant $P V ^ {  \nu }$ . The planning process gives an initial planning $P V i ^ { \nu }$ that does not integrate any risks. A project variant is also described by its set $E _ { R } ^ { \nu }$ of identi<sup>fi</sup>ed risks $R _ { i } ^ { \nu } ( i = 0 \ldots n ^ { \nu } )$ $n ^ { \nu }$ being the number of identi<sup>fi</sup>ed risks in $P V .$ . Each R<sup>v</sup> is characterized via the risk management process. A risk $R _ { i } ^ { \nu }$ is also characterized by its period of occurrence, i.e. the tasks during which the risk can occur. Its probability proba(R<sup>v</sup>) (the probability that the event related to $R _ { i } ^ { \nu }$ occurs) and its impacts on costs $C I ( R _ { i } ^ { v } )$ and/or in delay $D I ( R _ { i } ^ { \nu } )$ on a task can be different of the period of occurrence. These probability and impact are also called initial probability and initial impact.

A risk scenario ScR<sup>v</sup> corresponds to the combination of the risks occurring during a project variant PV<sup>v</sup>. A project variant presenting $n ^ { \nu }$ risks leads to $2 ^ { n ^ { v } }$ risk scenarios. Then ScR<sup>v</sup> $\left( s = 1 , . . . , 2 ^ { n ^ { \nu } } \right)$ is a possible achievement with k risks $( 0 \leq k \leq n )$ and the total number of risk scenarios, presenting k of the n identi<sup>fi</sup>ed risks, is equal to $\frac { n ! } { k ! ( n - k ) ! } .$ . Its probability is proba(ScR<sup>v</sup>) (the probability that the events related to this risk scenario occur and that the other risks do not occur).

$$
\operatorname{proba} \left(S c R _ {s} ^ {v}\right) = \prod_ {i = 1} ^ {n} \left\{ \begin{array}{c l} \operatorname{proba} (R _ {i}) & \text { if } (R _ {i} \in S c R) \\ 1 - \operatorname{proba} (R _ {i}) & \text { if } (R _ {i} \notin S c R) \end{array} \right.
$$

Each risk can be treated in various ways that can be preventive, corrective or a combination of both preventive and corrective if the risk occurs despite the preventive action. A risk R<sup>v</sup> can be associated to one or more treatment strategies $S t T _ { i j } ^ { \nu } ( j = 1 \ldots m ^ { \nu } ) ,$ , m<sup>v</sup> being the number of identi<sup>fi</sup>ed strategies for $R _ { i } ^ { \nu } , \mathsf { A }$ treatment strategy StT<sub>ij</sub><sup>v</sup> groups a set of treatment actions $A _ { i j \alpha } ( \alpha = 1 \ldots a )$ to avoid or reduce the risk $R _ { i } ^ { \nu } ,$ a being the number of identi<sup>fi</sup>ed treatment actions. A treatment action can be materialized by a task to achieve and introduces three types of modi<sup>fi</sup>cations to the WBS: (1) addition of a new task, which is also added to the planning; and (2) suppression of a task from the initial schedule. The risk is reduced by suppressing a task from the schedule; (3) modi<sup>fi</sup>cation of an existing task.

A treatment strategy is a preventive strategy if it contains at least one preventive treatment action. Otherwise, it is a corrective strategy. It is possible that the task is running in a graceful degradation. This leads to delays or cost overruns already taken into consideration in the initial impact. The fact that the strategy consists in running no action at all is noted as being an empty set such as ∅.

Finally, several treatment strategies are possible for each risk $R _ { i } ^ { \nu } .$ The de<sup>fi</sup>nition of these strategies can lead to the appearance of treatment actions common to several risks. The set of all the identi<sup>fi</sup>ed StT<sup>v</sup> for a risk R<sup>v</sup> is written StR<sup>v</sup>. Then $S t R _ { i } ^ { \nu } = \{ { \mathcal O } , S t T _ { i 1 } ^ { \nu } , ~ . . , ~ S t T _ { i j } ^ { \nu } , ~ . . , ~ S t T _ { i m } ^ { \nu } \}$ and $\operatorname { C a r d } ( S t { R _ { i } } ^ { \nu } ) = m ^ { \nu } + 1$

A treatment scenario $S c T _ { d } ^ { \nu } ( d = 1 \dots D ^ { \nu } )$ corresponds to a combination of the treatment strategies chosen to deal with the different risks of a project variant. The set of treatment scenarios is given by: $E _ { S c T } ^ { \nu } = \prod _ { i = 1 } ^ { n } S t R _ { i } ^ { \nu }$ . For each $P V ^ { \nu } , E _ { S c T } ^ { \nu }$ may contain a set of preventive treatment scenarios $E _ { S c T _ { \mathrm { p r e v } } } ^ { \nu }$ and corrective treatment scenarios $E _ { S c T _ { \mathrm { c o r r e c } } } ^ { \nu }$

The proba(R<sup>v</sup>|StT<sup>v</sup>) is the probability that the event related to $R _ { i } ^ { \nu }$ occurs, knowing that StT<sup>v</sup> (preventive strategy) has been achieved. This probability, as well as the impacts $C I ( R _ { i } ^ { \nu } | S t T _ { i j } ^ { \nu } )$ and DI(R<sub>i</sub><sup>v</sup>|StT<sub>ij</sub><sup>v</sup>), are then quali<sup>fi</sup>ed “reduced probability” and “reduced impact”.

A project scenario $S c P _ { p } ^ { v } ( p = 1 \ldots P )$ is de<sup>fi</sup>ned as being a possible project achievement that is built with a risk scenario and treatment scenario $( S c P _ { p } ^ { \nu } = < P i ^ { \nu } , S c R _ { s } ^ { \nu } , S c T _ { d } ^ { \nu } > )$ . The set of project scenarios $E S ^ { \nu }$ is obtained by combining the set of risk scenarios and the set of treatment scenarios.

proba $( S c P _ { p } ^ { \nu } )$ is the probability of a given $S c P _ { p } ^ { \nu } .$ It takes into account (1) the probability of the occurring risks $( R _ { i } ^ { v } \in S c R _ { s } ^ { v } )$ ), (2) the probability that several risks do not occur $( R _ { i } ^ { \nu } \notin S c R _ { s } ^ { \nu } ) , ( 3 )$ the probability of the occurring risks $( R _ { i } ^ { v } \in S c R _ { s } ^ { v } )$ knowing that a treatment strategy is developed $( S t T _ { i j } ^ { \nu } \in S c T _ { d } ^ { \nu } )$ and (4) the probability that $R _ { i } ^ { \nu }$ does not occur $( R _ { i } ^ { v } \notin S c R _ { s } ^ { v } )$ knowing that a preventive strategy has been processed and the initial probability has been modi<sup>fi</sup>ed $( S t T _ { i j } ^ { \nu } \in S c T _ { d } ^ { \nu } )$

$$
\operatorname{proba} \left(S c P _ {p} ^ {\nu}\right) = \prod_ {i, j} ^ {R _ {i} ^ {\nu} \in S c R _ {s} ^ {\nu}, S t T _ {i j} ^ {\nu} \in S c T _ {d} ^ {\nu}} \left\{ \begin{array}{l} \operatorname{proba} \left(R _ {i} ^ {\nu}\right) \\ 1 - \operatorname{proba} \left(R _ {i} ^ {\nu}\right) \\ \operatorname{proba} \left(R _ {i} ^ {\nu} \mid S t T _ {i j} ^ {\nu}\right) \\ 1 - \operatorname{proba} \left(R _ {i} ^ {\nu} \mid S t T _ {i j} ^ {\nu}\right) \end{array} \right.\tag{1}
$$

ð Þ <sup>2</sup>

ð Þ <sup>3</sup>

ð Þ <sup>4</sup>

The cost of a project scenario is noted $C ( S c P _ { p } ^ { \nu } )$ . It includes the cost of the T tasks that constitute the initial planning of the project variant, the $S c R _ { p } ^ { \nu }$ and the chosen $S c T _ { p } ^ { \nu }$ and (1) the global cost $G \bar { C } ^ { \mathrm { i n i t i a l } } ( R _ { i } ^ { \nu } )$ of the occurring risks that are not treated by the treatment strategies. It includes the cost impact that is composed of a <sup>fi</sup>xed part of the total cost (materials, tools, parts etc.) and of an indirect cost that depends on the action duration, through the delay impact, and the actors' charge. (2) The reduced global cost impact $\mathsf { G C } ^ { \mathrm { r e d u c e d } } ( R _ { i } ^ { \nu } )$ is obtained taking into account the different strategies $S t T _ { i j } ^ { \nu }$ applied to treat $R _ { i } ^ { \nu }$ and its reduced repercussions on the project cost and duration. (3) The cost of the treatment strategies $S t T _ { i j } ^ { \nu }$ that is determined of the cost of the action is composed by a direct cost (materials, tools etc.) and of an indirect cost that depends on the action duration and on the actors.

$$
\begin{array}{l} C \left(S c P _ {p} ^ {\nu}\right) = \sum_ {t = 1} ^ {T} C \left(T _ {t} ^ {\nu}\right) \\ + \sum_ {i, j} ^ {R _ {i} ^ {\nu} \in S c R _ {s} ^ {\nu}, S t T _ {i j} ^ {\nu} \in S c T _ {d} ^ {\nu}} \left\{ \begin{array}{l} \sum_ {R _ {i} ^ {\nu} \in S c R _ {s} ^ {\nu}} G C ^ {\text { initial }} \left(R _ {i} ^ {\nu}\right) \\ \sum_ {R _ {i} ^ {\nu} \in S c R _ {s} ^ {\nu}} G C ^ {\text { reduced }} \left(R _ {i} ^ {\nu}\right) \Bigg | S t T _ {i j} ^ {\nu} \\ \sum_ {R _ {i} ^ {\nu} \in S c R _ {s} ^ {\nu}} \sum_ {S t T _ {i j} ^ {\nu} \in S t R _ {i} ^ {\nu}} C \left(S t T _ {i j} ^ {\nu}\right) \end{array} \right. \end{array}\tag{1}
$$

ð Þ <sup>2</sup>

ð Þ <sup>3</sup>

## 3.3. Objectives

Project managers have to provide target on costs and deadlines in the project conception phase. He has to estimate the chances of success, as well as of meeting the budget and the contractual commitments, taking into account the different risks. Two different project variants (a and b) of a same project are presented in Fig. 2. Each project variant could lead to a set of project scenario. For each project scenario, the project duration is represented in x-coordinate and its cost in y-coordinate. The probability of the scenario is represented by the bubble diameter. Therefore, an acceptability zone can be de<sup>fi</sup>ned, using the budget and deadline thresholds. The choice of the best variant is based on the potential of reaching the improvements promised but also on the performance of the improvement itself.

Each project variant is associated with different development strategies. They induce a speci<sup>fi</sup>c risk portfolio that can impact the respective duration and cost of each scenario. The respective global risk level of each variant is then different. The objective of this research work is to give the decision-maker a methodological tool to compare each project variant regarding its global bene<sup>fi</sup>ts/risk balance.

## 4. Resolution approach

## 4.1. Representation of the decision problem

In an industrial context, the modi<sup>fi</sup>cation of a project structure or process is the source of many uncertainties. For this reason, different decisions are made over the different phases of project conception and management in order to reduce and control the risk level.

Fig. 1 shows the decisional process of risk management over the time. The project management team goes through different phases of decision represented by the decision nodes D1 to D3 on Fig. 1 to reach its objectives. Its <sup>fi</sup>rst decision (D1) aims to choose a project variant among a list of project variants. The second one (D2) is to select the preventive risk treatment strategy. D1 and D2 are made during the preparation phase of the project. However, D3 is made to react when events occur. Decision D3 consists in deciding which corrective actions should be carried on facing an undesirable set of events (a risk scenario). These events are represented by the event nodes E (also called chance node) on the decision tree.

## 4.2. The proposed proactive approach

The body of the approach is composed of three phases: (a) the generation of all the possible project scenarios and their evaluations for each of the variant proposed, (b) the selection in each project variant of the best project scenarios based on the decision of preventive treatment scenario, and (c) the selection of the best project variant following the criteria identi<sup>fi</sup>ed.

In the preparation phase of a project, the technical orientations and the way of managing risks have to be chosen. The approach we propose (Fig. 3) uses data relatives to the project in its classical view: the different tasks planned, the risks, and their associated treatment actions. It also uses data relatives to the variants and their modi<sup>fi</sup>cations: consequences on the tasks and consequently on the risks and treatment strategies. These data are supposed to be collected on the

<table><tr><td>Time</td><td colspan="2">Preparation phase</td><td>Running phase</td><td>t</td></tr><tr><td>Decision nodes</td><td>Variants</td><td>Preventive strategies</td><td>Corrective strategies</td><td></td></tr><tr><td>Events nodes</td><td></td><td></td><td>Occuring Risks</td><td></td></tr></table>

![](/api/attachments/7CNHPCN5/fulltext/images/badff9f1107961984d1f3820cfc7fe51ae9af2616502b64b04348e069fdb8779.jpg)  
Fig. 1. Decision tree to compare project variants.

Please cite this article as: F. Marmier, et al., A risk oriented model to assess strategic decisions in new product development projects, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.05.002

F. Marmier et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/7CNHPCN5/fulltext/images/0cc69f39ac5c930f567238901a3c575eb6f4df1a5c1ec357bd20632392cd7579.jpg)  
Fig. 2. Example of two project variants

basis of expert knowledge concerned by the project. Therefore, our method includes input data provided by the schedule process (management team) and from the risk management process.

4.2.1. The generation of all the project scenarios for each proposed variants

To evaluate the different possible project scenarios, the management team needs to generate an initial schedule, without integrating the notions of variant, risk and risk treatment. From this initial planning, called Reference, for each variant, a planning is realized including the project modi<sup>fi</sup>cations.

It is then necessary to calculate the different risks and treatment scenarios. These scenarios allow the set of the project scenarios to be constructed. Finally, when the project scenarios are known it is possible to obtain their durations and costs. The approach called ProRisk proposed in Ref. [25] is then used to generate $E _ { S c P ^ { \nu } }$ . For each project scenario, the calculation of the probability, the cost and the duration take into account the potential modi<sup>fi</sup>cations induced by the achievement of treatment strategies at the schedule level. Once the initial schedule is adapted in accordance with the studied scenario (modi<sup>fi</sup>ed duration, tasks added or removed), the project scenario duration is computed using the PERT method and the earliest starting dates.

4.2.2. The selection in each project variant of best project scenarios for each preventive treatment scenario

Step (a) of our approach, makes it possible to adopt an opposite way than presented in the classical approach (Section 4.1) and then to become proactive. First, all the D3 are made regarding the best evaluation at the end of each branch. Then D2 can be made knowing, for each variant, the best D3 and D1 can be made knowing the best D2.

Two steps consequently compose the selection phase. D3 is the step of selection of the coherent or pertinent project scenario. The corrective strategies are selected in order to avoid scenarios that would not be possible in the reality, i.e. the scenario where the project is stopped waiting for a corrective action or the scenario presenting a NoGo situation.

D2 is the second step that composes the selection phase. It consists in avoiding the worst possible cases (project scenarios) as de<sup>fi</sup>ned by the Savage's criterion often used in decision-making theory [27]. Project scenarios are evaluated regarding their costs, their durations and their probability of ful<sup>fi</sup>llment. The criticality is commonly used for the risk assessment. It allows to aggregate these three criteria and obtain a representative evaluation of each project scenario. Project scenarios are evaluated regarding their costs, their durations and their probability of ful<sup>fi</sup>llment. Criticality is commonly used for the risk assessment. It allows these three criteria to be aggregated, thus obtaining a representative evaluation of each project scenario. Minimizing the maximum criticality (also called in similar context regret) can, when the assessment of each scenario is known, measure the regret that the decision-maker would have, had he preferred an action over another. A measure of the criticality of each project scenario allows to evaluate the project scenarios, knowing the selections realized in D3. The criticality calculation is obtained as follows:

Each $P V ^ { \nu }$ presents a set of ScP<sub>p</sub><sup>v</sup> and each of them can be characterized by a criticality $C r ( S c P _ { p } ^ { \nu } ) .$ . This criticality measure is based on its probability of occurrence proba(ScP<sup>v</sup>), and a duration and a cost metrics of the project scenario respectively $\alpha _ { p } ^ { \nu }$ and $\beta _ { p } ^ { \nu } \mathrm { : }$

$$
\alpha_ {p} ^ {\nu} = \frac {D I (S c P _ {p} ^ {\nu})}{\max (D I (S c P _ {p} ^ {\nu}))} \text { and } \beta_ {p} ^ {\nu} = \frac {C l (S c P _ {p} ^ {\nu})}{\max (C l (S c P _ {p} ^ {\nu}))}, (p = 1... P) (\nu = 0... V)
$$

then $\alpha _ { p } ^ { v } , \ \beta _ { p } ^ { v } \in [ 0 , 1$ ]where CI(ScP<sup>v</sup>) and $D I ( S c P _ { p } ^ { \nu } )$ are respectively the distance between the cost and duration impacts and the budget and delay thresholds de<sup>fi</sup>ned in the contractual agreement of the project. max(CI(ScP<sub>p</sub><sup>v</sup>)) and max $\leq f t ( C I ( S c P _ { p } ^ { v } ) )$ the distance of the costly and longest project scenario over the project variants with the thresholds de<sup>fi</sup>ned.

To model possible priorities of the project manager, coef<sup>fi</sup>cients are introduced in the impact de<sup>fi</sup>nition formula. They enable the project manager to balance the importance of reaching the cost objective as compared to the duration objective. The global impact, weighted and normalized, Impact(ScP<sup>v</sup>) is then obtained through the following formulae:

$$
\operatorname{Impact} \left(S c P _ {p} ^ {\nu}\right) = q \times \alpha_ {p} ^ {\nu} + q ^ {\prime} \times \beta_ {p} ^ {\nu}
$$

where q and $q ^ { \prime }$ (respecting $q + q ^ { \prime } = 1 )$ are two coef<sup>fi</sup>cients that are chosen by the project manager in accordance with the importance of the duration relatively to the cost.

Then, ∀ v and $\forall ~ p , C r ( S c P _ { p } ^ { \nu } ) = \mathrm { p r o b a } ( S c P _ { p } ^ { \nu } ) \times \mathrm { I m p a c t } ( S c P _ { p } ^ { \nu } )$ .

D2 consists in choosing which preventive strategy is the most adequate for each variant. The preventive strategies that minimize the maximal criticality are chosen depending on the selections realized in D3 for each project variant. For each ScTprev<sup>v</sup>, the maximal criticality $C r _ { \mathrm { m a x } } ( S c P _ { p } ^ { \nu } / S c T p r e \nu _ { s } ^ { \nu } )$ is obtained by the ScP<sup>v</sup> associated with the given ScTprev<sup>v</sup> that presents the maximal Cr(ScP<sup>v</sup>).

Then, ∀ v chooses ScTprev<sup>v</sup> that min $C r _ { \operatorname* { m a x } } ( S c P _ { p } ^ { \nu } / S c T p r e \nu _ { s } ^ { \nu } )$

## 4.2.3. The selection of the best project variant

The project management team wants to maximize the chance of meeting the commitments that is modeled in Fig. 2 by the zone of agreement. To choose the appropriate project variant, D1 consists in selecting the variant that maximizes the number of possible ScP<sup>v</sup> in this area knowing D2 for each variant. Finer time slicing can give more reliable and precise information. Depending on the need, the approach can: (1) be applied at a macroscopic level (phase of the project) or at a more detailed level (elementary tasks of the project), and (2) be applied at the beginning of the project or at the different decisional milestones taking into account new information.

Please cite this article as: F. Marmier, et al., A risk oriented model to assess strategic decisions in new product development projects, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.05.002

## 5. A satellite development project based case study

This approach was applied to the case of the Company ${ \mathrm { X } } ,$ an anonymous satellite constructor. The aerospace industry, characterized by its continuous technological innovation, has been pressured over the last twenty years. In the 90s, in the US, the reduced founding of the NASA forces the integration of cost reduction in the aerospace industry. Programs such as “Faster, Better, Cheaper” and “Smaller, Better, Cheaper” [26] are then launched. Many potentially more or less good ideas have been developed to meet the requirements of the market. The problem of our industrial partner consists in being able to select new technological solutions by taking into account their repercussion on the existing risks that make the decision tricky.

## 5.1. Presentation of a satellite integration and test project

The probabilities and the risk data have initially been characterized by experts referring to their experience but were slightly modi<sup>fi</sup>ed. The different numerical data was modi<sup>fi</sup>ed accordingly without any impact on the scienti<sup>fi</sup>c logic of our approach.

Each satellite follows numerous steps from the conception to its launching in space. The phase that is handled here is the integration and test phase. Its particularity is to represent about the half of the total time of the conception, i.e. between 9 and 18 months out of the 24 to 36 months necessary to achieve all the steps. An observation satellite is composed of several modules and each of them is tested to valid its behavior.

The different tasks, presenting a <sup>fi</sup>xed rate, that compose the process studied are detailed in Table 1 where the duration is in time unit (TU) and the costs in monetary unit (MU).

An associated provision for risks makes the contractual commitment of for this part of the global satellite project of 425 TU and 39 MU.

Different risks have been identi<sup>fi</sup>ed during the project (Table 2). Possible treatment strategies characterize them (Table 3). The impacts of the majority of the risks are judged as ∞ since the costs and delay will continually increase until an action is decided.

The <sup>fi</sup>rst risk $\left( R _ { 1 } \right)$ , expresses the anomaly observed during the material integration on the satellite (error of wiring, systems presenting default…). $R _ { 1 }$ is relatively probable since all the failures are recorded. If such a risk occurs, the production is immediately stopped until a strat-$\mathrm { e g y }$ is implemented. Then two strategies are possible: a preventive one $S t T _ { 1 1 ( p ) }$ and a corrective one $S t T _ { 1 2 ( c ) } . S t T _ { 1 1 ( p ) }$ consists in carefully check critical material at the subcontractor plant by participating to the reviews, auditing etc. If it did not suppress the risks, it reduced its probability of occurrence of 10%. The cost of these actions is estimated to 10 MU for an associated duration that is not located on the critical path. $S t T _ { 1 2 ( c ) }$ aims to modify the material or the software when problems are observed. Such a strategy costs 5 MU and makes the satellite unavailable for 5 TU. If $\left( R _ { 1 } \right)$ occurs even if a preventive strategy has been carried out, it is still possible to develop the corrective strategy. However, only its duration will be passed onto, since the cost will be supported by the suppliers.

$R _ { 2 }$ represents the lateness of material reception during the integration phase. It stops the action continuity and leads to a mean lateness of 20 TU with an extra cost of 10 MU. A preventive strategy $S t T _ { 2 1 ( p ) }$ permits avoiding this kind of risk by stocking additive critical parts. The whole type of parts couldn't be stocked, the probability of occurrence is only reduce to 10%.

Table 1  
Detail of the planning phases.

<table><tr><td>Phases</td><td>Description</td><td>Duration (TU)</td><td>Cost (MU)</td></tr><tr><td>T1</td><td>Material integration</td><td>216</td><td>16.2</td></tr><tr><td>T2</td><td>Initial tests for reference</td><td>27</td><td>2</td></tr><tr><td>T3</td><td>EMC tests</td><td>18</td><td>1.4</td></tr><tr><td>T4</td><td>Thermal vacuum test</td><td>27</td><td>2.2</td></tr><tr><td>T5</td><td>Mechanical tests</td><td>12</td><td>0.9</td></tr><tr><td>T6</td><td>Final tests for reference</td><td>27</td><td>2</td></tr><tr><td>T7</td><td>Flight</td><td>-</td><td>-</td></tr><tr><td></td><td>Total</td><td>327</td><td>24.7</td></tr></table>

Table 3

Table 2  
Risks associated with the project.

<table><tr><td>Risks</td><td>Probability</td><td>Occurrence period</td><td>Fixe cost impact</td><td>Delay impact</td><td>Strategies</td></tr><tr><td> $R_1$ </td><td>30%</td><td> $T_1$ </td><td>∞</td><td>∞</td><td> $StT_{11(p)}$  $StT_{12(c)}$ </td></tr><tr><td> $R_2$ </td><td>20%</td><td> $T_1$ </td><td>10</td><td>20</td><td> $StT_{21(p)}$ </td></tr><tr><td> $R_3$ </td><td>25%</td><td> $T_2$ </td><td>∞</td><td>∞</td><td> $StT_{31(c)}$ </td></tr><tr><td> $R_4$ </td><td>1%</td><td> $T_3$ </td><td>∞</td><td>∞</td><td> $StT_{41(c)}$ </td></tr><tr><td> $R_5$ </td><td>15%</td><td> $T_6$ </td><td>∞</td><td>∞</td><td> $StT_{51(c)}$ </td></tr><tr><td> $R_6$ </td><td>6%</td><td> $T_6$ </td><td>∞</td><td>∞</td><td> $StT_{61(c)}$ </td></tr><tr><td> $R_7$ </td><td>1%</td><td> $T_7$ </td><td>∞</td><td>∞</td><td></td></tr></table>

$R _ { 3 }$ may occur during the initial tests for reference through the failure of a component or software. Consequences are high since the project is stopped waiting for the corrective action $S t T _ { 3 1 ( c ) } . \ S t T _ { 3 1 ( c ) }$ consists in looking for the problem and <sup>fi</sup>xed it. In average, it takes about 5 TU for a cost of 2 MU to <sup>fi</sup>nd and solve the problem.

$R _ { 4 }$ is the fact that an electrical incompatibility may happen in the satellite. The probability of this risk is relatively low (1%) but the consequence quite huge since it may stop the project until a solution is found. A corrective strategy is then proposed $S t T _ { 4 1 ( c ) }$ that consists in modifying the part of the satellite to solve the problem. Time and costs have been evaluated by the experts to 5 TU and 2 MU.

$R _ { 5 }$ and $R _ { 6 }$ are representatives of the main two risks that can be identi<sup>fi</sup>ed during the achievement of the <sup>fi</sup>nal tests. These anomalies may be respectively highly and faintly consequent. Their respective probability of occurrence is 15% and may stop the project. Two corrective strategies can then be developed. $S t T _ { 5 1 ( c ) }$ for the weak anomalies that consists in repairing the failures (5 TU and 2 MU) and $S t T _ { 6 1 ( c ) }$ for the strong anomalies that implies to return the defective equipment to the suppliers (120 TU and 12 MU).

The last identi<sup>fi</sup>ed risk, $R _ { 7 } ,$ de<sup>fi</sup>ned the potential occurrence of failure of the satellite during its deployment in the space. It leads to a complete failure of the mission and does not have any treatment strategies. The probability of ${ \bf \dot { R } } _ { 7 }$ is estimated to 1%.

## 5.2. How to improve the project

In this study, the project management team has to respect contractual commitments. Therefore and in order to improve the success rate, different modi<sup>fi</sup>cations of the structure of their satellite development projects are proposed by experts: the reduction of the tests for references, the suppression of tests for EMC compatibility and the suppression of the <sup>fi</sup>nal ones. This approach will then be applied to comparatively show the advantage and the risks of each proposition. The phase of the initial tests for reference is composed of global tests and speci<sup>fi</sup>c ones to each subset of the satellite. However, each equipment is already tested and certi<sup>fi</sup>ed by the retailer. The philosophy of

Available risk treatment strategies

<table><tr><td>Strategies</td><td>Modified task</td><td>Successor</td><td>Duration (TU)</td><td>Total cost (MU)</td><td>Reduced probability</td></tr><tr><td> $StT_{11(p)}$ </td><td> $T_1$ </td><td> $T_2$ </td><td>0</td><td>30</td><td>10%</td></tr><tr><td> $StT_{12(c)}$ </td><td> $T_1$ </td><td> $T_2$ </td><td>5</td><td>5</td><td></td></tr><tr><td> $StT_{11(p)}$  &amp;  $StT_{12(c)}$ </td><td> $T_1$ </td><td> $T_2$ </td><td>5</td><td>5</td><td></td></tr><tr><td> $StT_{21(p)}$ </td><td> $T_1$ </td><td> $T_2$ </td><td>5</td><td>10</td><td>10%</td></tr><tr><td> $StT_{31(c)}$ </td><td> $T_2$ </td><td> $T_3$ </td><td>5</td><td>2</td><td></td></tr><tr><td> $StT_{41(c)}$ </td><td> $T_3$ </td><td> $T_4$ </td><td>5</td><td>2</td><td></td></tr><tr><td> $StT_{51(c)}$ </td><td> $T_6$ </td><td> $T_5$ </td><td>5</td><td>2</td><td></td></tr><tr><td> $StT_{61(c)}$ </td><td> $T_6$ </td><td> $T_5$ </td><td>120</td><td>12</td><td></td></tr></table>

Please cite this article as: F. Marmier, et al., A risk oriented model to assess strategic decisions in new product development projects, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.05.002

the reduction we propose for these tests (alternative 1) would then be based on retailers certi<sup>fi</sup>ed equipments. Only then should the global systems be tested, leading to an increase of the failure probability in the phase of <sup>fi</sup>nal tests for reference (R5). For several years and many projects, the EMC tests did not allow to <sup>fi</sup>nd major failures. Therefore EMC tests are regularly reduced. Their suppression (alternative 2) would mainly save time, but also increase the possibility of defect during the <sup>fl</sup>ight and a failure of the mission.

The third proposition consists in planning the mechanical tests before the thermal vacuum test and suppresses the <sup>fi</sup>nal tests (alternative 3). The thermal vacuum will valid the global behavior of the system and the <sup>fi</sup>nal reference test could be suppressed. However, the risk of failure during the thermal vacuum test could be more consequent, since the cost of such tests is important. Experts consider the combination of reduction of the tests for references and suppression of tests for EMC compatibility as potentially pertinent (alternative 4). Table 4 presents such possible alternatives, their consequence on risks and then the different simulations developed in this paper. In this table, NC means no change (for example the probability may change but not the impact delay) and NoGo means that the project failed since no corrective action was possible once the project launched.

## 5.3. Results and discussion

## 5.3.1. Presentation of the results

Table 5 presents the results obtained with our approach. The <sup>fi</sup>rst column shows the different variants introduced in Section 5.2. For each variant, the second column gives the possible preventive strategies. For each variant, ∅ means that no preventive strategy is applied. The third column presents the number of project scenarios containing the previously evoked preventive strategy. The column entitled “% pertinents” refers to the percentage of pertinent project scenarios. Are considered as non-pertinent scenarios, the scenarios in which one or more risks occurred, stopping the project without any corrective strategies despite the presence of possible preventive strategies. We consider that the corrective strategies should have been applied to that case. The next column presents the maximal criticality among the pertinent scenarios. Still, among the pertinent scenarios, the last column shows the percentage of scenarios that respect the contractual commitments.

## 5.3.2. About taking decisions

By going through the decision tree proposed in Fig. 1 in the backward induction, we consider decision D3 to D1 and not D1 to D3 as it could be classically done. The phase (a) of the approach consists in generating the whole set of the possible project scenarios using the initial data (planning, risks and strategies) but also the additional data relative to the variants (modi<sup>fi</sup>cation of the project planning and consequences on risks). It provides, for the case study, 4536 project scenarios for the reference and for the variants 1 and 3 and 3024 project scenarios for the variants 2 and 4. The difference comes from the fact that risk R4 is transferred in the phase of <sup>fl</sup>ight making impossible the use of treatment strategies and by the way reducing the combinatorial complexity.

The phase (b) of the proposed approach is composed of 2 steps. D3, the <sup>fi</sup>rst step, consists in deciding of corrective treatment strategies in the case of risks occur. Then, it provides the selection of the coherent or pertinent project scenario. A huge number possible scenario are removed since for each possible treatment scenario in each variant, the list of pertinent scenarios represents only about 3 to 7% of the total project scenario number. This point is explained by the fact that, in such type of innovative products, there is no possible degraded mode. So, for the different technological failures, corrective actions have to be done. The second step of the phase (b) is the decision D2 of the decision tree (Fig. 1). D2 consists in avoiding the worst possible cases or project scenarios for each variants by selecting the preventive treatment scenario that minimize the maximal criticality. For each variant the minimal values of the maximal criticalities are presented in bold in Table 5 (knowing D3). It can be noted that for each variant, results are similar since the preventive treatment scenario leading the minimal value is the empty set. Therefore, due to their cost, the proposed preventive treatment strategies may have disadvantageous consequences on the criticality.

Table 4  
Repercussion of the modi<sup>fi</sup>cations.

<table><tr><td>Alternatives</td><td>Modified risk</td><td>New characteristic proba/delay/cost</td></tr><tr><td colspan="3">Reference</td></tr><tr><td>1</td><td>R5</td><td>30%/NC/NC</td></tr><tr><td>2</td><td>R4 transferred to T7</td><td>NC/NoGo</td></tr><tr><td rowspan="2">3</td><td>R5 transferred to T4</td><td>R5:15%/5/8</td></tr><tr><td>R6 transferred to T4</td><td>R6:15%/120/48</td></tr><tr><td rowspan="2">4</td><td>R5</td><td>30%/NC/NC</td></tr><tr><td>R4 transferred to T7</td><td>NC/NoGo</td></tr></table>

Table 5  
Results of the proposed approach.

<table><tr><td>Variants</td><td>Preventive strategies</td><td>Nbr ScP</td><td>% pertinents</td><td>Criticality max</td><td>% contract respected</td></tr><tr><td rowspan="4">Reference</td><td> $\emptyset$ </td><td>972</td><td>6.5844</td><td>0.1652</td><td>31.2500</td></tr><tr><td> $StT_1$ </td><td>1296</td><td>4.9383</td><td>0.2409</td><td>21.8750</td></tr><tr><td> $StT_2$ </td><td>972</td><td>6.5844</td><td>0.2107</td><td>10.9375</td></tr><tr><td> $StT_1 + StT_2$ </td><td>1296</td><td>4.9383</td><td>0.3030</td><td>0</td></tr><tr><td rowspan="4">1</td><td> $\emptyset$ </td><td>972</td><td>6.5844</td><td>0.1328</td><td>35.9375</td></tr><tr><td> $StT_1$ </td><td>1296</td><td>4.9383</td><td>0.1947</td><td>21.8750</td></tr><tr><td> $StT_2$ </td><td>972</td><td>6.5844</td><td>0.1703</td><td>12.5000</td></tr><tr><td> $StT_1 + StT_2$ </td><td>1296</td><td>4.9383</td><td>0.2459</td><td>0</td></tr><tr><td rowspan="4">2</td><td> $\emptyset$ </td><td>648</td><td>4.9383</td><td>0.1658</td><td>34.3750</td></tr><tr><td> $StT_1$ </td><td>864</td><td>3.7037</td><td>0.2424</td><td>25.0000</td></tr><tr><td> $StT_2$ </td><td>648</td><td>4.9383</td><td>0.2121</td><td>12.5000</td></tr><tr><td> $StT_1 + StT_2$ </td><td>864</td><td>3.7037</td><td>0.3057</td><td>0</td></tr><tr><td rowspan="4">3</td><td> $\emptyset$ </td><td>972</td><td>6.5844</td><td>0.1399</td><td>29.6875</td></tr><tr><td> $StT_1$ </td><td>1296</td><td>4.9383</td><td>0.1984</td><td>12.5000</td></tr><tr><td> $StT_2$ </td><td>948</td><td>6.7511</td><td>0.1736</td><td>7.8125</td></tr><tr><td> $StT_1 + StT_2$ </td><td>1296</td><td>4.9383</td><td>0.2441</td><td>0</td></tr><tr><td rowspan="4">4</td><td> $\emptyset$ </td><td>648</td><td>4.9383</td><td>0.1319</td><td>53.1250</td></tr><tr><td> $StT_1$ </td><td>864</td><td>3.7037</td><td>0.1945</td><td>25.0000</td></tr><tr><td> $StT_2$ </td><td>648</td><td>4.9383</td><td>0.1702</td><td>15.6250</td></tr><tr><td> $StT_1 + StT_2$ </td><td>864</td><td>3.7037</td><td>0.2468</td><td>0</td></tr></table>

The phase (c) consists in selecting the project variant that gives the best potential of meeting commitments, knowing the fact that no preventive actions would be carried on (knowing D2). The variant that maximizes the project scenario number in the zone of agreement is presented in bold in the last column of Table 5. This result means that by choosing the variant 4 and by applying no preventive treatment strategy, 53% of the pertinent project scenario respects the contractual commitments. Based on these results, the recommendation to the project manager would be simple: choose variant 4 and apply no preventive strategy.

## 5.3.3. Discussion

The selection of a project structure is made taking into account its consequences. The proposed approach has been developed to help the decision-maker in front of the combinatorial complexity of possible future for a project (Fig. 3). Therefore, it helps to decide project orientations and strategies of risk treatment in order to <sup>fi</sup>nd the best balanced between bene<sup>fi</sup>ts and risks. Indeed, this work has been guided by the need of our industrial partner, and the approach has been designed to be a general approach. In that way it should be usable in other industrial context and the feasibility remains to be proved. This discussion will be oriented on two different axes: (1) the approach through its conception and the evaluation of its performance, (2) the case study.

Concerning the approach, different choices have been done regarding the criteria used at the different decision steps. They have been chosen to answer to the problem, however other criteria could give complementary informations such as the total probability of being in the contractual agreement (for D1) area instead of the total number of scenario. Several statistical criteria have been tried comparing to the maximal criticality such as the dispersion through ranges of values. However, the minimal criticality is very low and close to zero. A deep analysis of the possible criteria could then lead to make the approach more robust and more informative.

![](/api/attachments/7CNHPCN5/fulltext/images/12f31345912596c7beab26aec3b92cba5ed8cf016a49d77af00b6d67815e0ef0.jpg)  
Fig. 3. The proposed approach.

Concerning the case study, different particularities of the context make the comparison of the results dif<sup>fi</sup>cult to other contexts: (1) Several risks present the particularity of requiring corrective treatment in order to continue the project. (2) Risks may occur during a task that does not give the possibility of corrective treatment and then the project failed. (3) The cost of the preventive actions is relatively high. Policies, in the aerospace industry, and model hypothesis, make dif<sup>fi</sup>cult the application of results providing of such system. However, by given visibility on consequences, it permits discussions and it gives arguments to negotiate improvements.

## 6. Conclusion

Choosing the best strategy in a project structure in the preparation phase of a project is often tricky, especially when the project should deliver a product presenting technological novelty. If the bene<sup>fi</sup>t of such modi<sup>fi</sup>cations is easy to evaluate, each possible modi<sup>fi</sup>cation of the project structure generates variants with different plannings and different costs and delays but also different risk levels. To estimate the risk level for each project variant, we propose an approach to model and evaluate the impact of risks on the project cost and the schedule cost. This approach uses the synchronized process principle and integrates the repercussion of the project structure modi<sup>fi</sup>cations on risks and the global risk level. We used the concepts of risk scenario, treatment scenario and project scenario to characterize and evaluate the project variants. We illustrate the principles of our approach through a case study from the aerospace industry. This methodology analyzes the possible scenarios, evaluates the global risk level and selects the best treatment scenarios at any time. An estimate of the global risk level of each project variant can be made and gives a vision of the possible scenarios: from the least to the most probable, from the most disastrous to the most optimistic! A software tool has been developed (Java platform). During a project, risk sources can be the cause of several risks.

The occurrence of a risk can modify the project. In this new context, the remaining risks can change and new risks can occur. The riskman methodology generates a relationship between a list of causes and a list of risks. Several risks can be associated with the same cause [3]. We observe that most of the different project risk analysis methods study risks under the hypothesis of independence between risks. The risk behavior is easier to model and integrate in a new risk assessment approach in an independent way. However, in reality, interdependencies exist between risks. These interdependencies can be strong enough to change the parameters of certain risks, such as the probability and/or the impact if one or more risks occur simultaneously. The risk may be a factor of generation of other risks [2]. Therefore, it must be considered when calculating other risk parameters. As a result, the risk impact evaluation can be in<sup>fl</sup>uenced by interdependencies. Several research works propose an approach to model risk interdependency [4,21]. These in<sup>fl</sup>uence mechanisms are currently being implemented. The main perspective for this research work will be to examine the in<sup>fl</sup>uence of previously occurring risks as initialized through the model proposed in Refs. [23,24] which also consider risk as an event, like the work presented in this paper. Risk aversion or risk attractiveness would lead to different decisions based on the same information. A complementary perspective could be to study, model and integrate into the approach the possible behavior of the decision maker. The resolution of the decision tree could then lead to different solutions.

## Acknowledgment

The authors would like to thank Mr Mena for his support and his expertise on the aerospace industry. They also would like to address special thanks to Mrs Carbonnel for her contribution to the platform developments.

## References

[1] BSI, BS 6079-3: Project Management — Guide to the Management of Business Related Project Related, 2000.

[2] V. Carr, J.H.M. Tah, A fuzzy approach to construction project risk assessment and analysis: construction project risk management system, Advances in Engineering Software 32 (2001) 847–857.

[3] B. Carter, T. Hancock, J. Morin, N. Robin, Introducing Riskman: the European Project Risk Management Methodology, The Stationery Of<sup>fi</sup>ce, 1996.

[4] E. Chauveau, How risks affect a project duration, 6th International Workshop on Economics-Driven Software Engineering Research (EDSER-6) 26th International conference on Software Engineering (ICSE), May 23–28, 2004, Scotland, UK, 2004.

[5] Y.C. Chiu, B. Chen, J.Z. Shyu, G.H. Tzeng, An evaluation model of new product launch strategy, Technovation 26 (2006) 1244–1252.

[6] R.T. Clemen, Making Hard Decisions: an Introduction to Decision Analysis, 2nd edition Duxbury, 1997

[7] C.M. Crawford, C.A.D. Benedetto, New Products Management, McGraw-Hill/Irwin, 2006.

[8] CSA, CAN/CSA-Q850: Risk Management, Guideline for Decision Makers, 1997.

[9] R. Cubitt, C. Starmer, R. Sugden, Dynamic decisions: some recent evidence from economics and psychology reasons and choices in: I Brocas LD. Carrillo (Eds.) The Psychology of Economic Decisions Oxford University Press Oxford 2004

Please cite this article as: F. Marmier, et al., A risk oriented model to assess strategic decisions in new product development projects, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.05.002

[10] P.K. Dey, Project risk management using multiple criteria decision-making technique and decision tree analysis: a case study of Indian oil re<sup>fi</sup>nery, Production Planning & Control 23 (2012) 903–921.

[11] D.S. Doering, R. Parayre, Identi<sup>fi</sup>cation and assessment of emerging technologies, Wharton on Emerging Technologies, John Wiley & Sons Edition, New York, 2000.

[12] C. Fang, F. Marle, A simulation-based risk network model for decision support in project risk management, Decision Support Systems 52 (2012) 635–644.

[13] C. Fang, F. Marle, M. Xie, E. Zio, An integrated framework for risk response planning under resource constraints in large engineering projects, IEEE Transactions on Engineering Management 99 (2013) 1–13.

[14] D. Gourc, Towards a General Risk Model for Piloting Goods- and Service-Related Activities (Vers un modèle general du risque pour le pilotage et la conduite des activités de biens et de services), HDR, INPT, Toulouse, France, 2006

[15] I.P.M.A., IPMA, Competence Baseline, 1999.

[16] ISO10006, Quality Management. Guidelines to Quality in Project Management, 1997.

[17] ISO31000, International Standards for Business, Risk Management — Principles and Guidelines. 2009

[18] ISO-Guide73, Risk Management Vocabulary: Guidelines for Use in Standards, Technical Report, 2002.

[19] M. Kiliç, G. Ulusoy, F.S. Serifoglu, A bi-objective genetic algorithm approach to risk mitigation in project scheduling, International Journal of Production Economics 112 (2008) 202–216.

[20] Y.H. Kwak, K.S. LaPlace, Examining risk tolerance in project-driven organization, Technovation 25 (2005) 691–695.

[21] F. Marle, L.A. Vidal, J.C. Bocquet, Interactions-based risk clustering methodologies and algorithms for complex project management, International Journal of Production Economics 142 (2013) 225–234.

[22] J. Mu, G. Peng, D.L. MacLachlan, Effect of risk management strategy on NPD performance, Technovation 29 (2009) 170–180.

[23] T.H. Nguyen, Contribution to the planning project: model for evaluating scenarios of risk project, In French (Contribution Ã la plani<sup>fi</sup>cation de projet: proposition d'un modèle d'évaluation des scénarios de risque-projet), 2011. (PhD thesis).

[24] T.H. Nguyen, D. Gourc, Towards a model for assessing risk impact on project planning, 22nd International Project Management Association (IPMA) World Congress, 2008.

[25] T.H. Nguyen, F. Marmier, D. Gourc, A decision-making tool to maximize chances of meeting project commitments, International Journal of Production Economics 142.(2013).214-224

[26] L.J. Paxton, “Faster, better, and cheaper” at NASA: lessons learned in managing and accepting risk, Acta Astronautica 61 (2007) 954–963.

[27] J. Petar, Application of sensitivity analysis in investment project evaluation under uncertainty and risk, International Journal of Project Management 17 (1999) 217–222.

[28] H. Pingaud, D. Gourc, Approach of controlling an industrial project by the risk analysis (démarche de pilotage d'un projet industriel par l'analyse des risques), 5e Congrès International Franco-Québécois de Génie Industriel, Canada, 2003.

[29] PMBoK, A Guide to the Project Management Body of Knowledge, 4th edition Project Management Institute, 2009.

[30] J. Tixier, G. Dusserre, O. Salvi, D. Gaston, Review of 62 risk analysis methodologies of industrial plants, Journal of Loss Prevention in the Process Industries 15 (2002) 291-303.

[31] J.R. Turner, The global body of knowledge, and its coverage by the referees and members of the international editorial board of this journal, International Journal of Project Management 18 (2000) 1–6.

[32] S. Van de Vonder, E. Demeulemeester, W. Herroelen, R. Leus, The use of buffers in project management: the trade-off between stability and makespan, International Journal of Production Economics 97 (2005) 227–240.

[33] S. Ward, C. Chapman, Transforming project risk management into project uncertainty management, International Journal of Project Management 21 (2003) 97–105.

![](/api/attachments/7CNHPCN5/fulltext/images/417d6fcd2f013334a4ccaee8d0cf735043f8d1ce797476c3485ede42fb2be059.jpg)

François Marmier is currently an associate professor at the École Nationale Supérieure des Mines d'Albi-Carmaux, in France. He obtained his PhD in Industrial Engineering from the University of Franche-Comté, France, in 2007. His research interests include integration of human aspects, the uncertainty and the risk to make better decisions in projects, logistics and services. Dr. Marmier has published several papers in various journals and international conferences.

![](/api/attachments/7CNHPCN5/fulltext/images/5027f5f091c6f6f8c18f36a7834bc39954f789b695db6e667a6958a15dae2564.jpg)

Didier Gourc is currently an associate professor at the École Nationale Supérieure des Mines d'Albi-Carmaux, in France. He obtained his PhD in Automated Systems Engineering from the University of Tours, France, in 1997. He graduated in Software Development Engineering from the Paul Sabatier University of Toulouse, France, in 1990. He has gained a strong industrial experience in software development, project management and consultancy on diagnostic of production process and project management organization, since 1992. His current research interests include project risk management, portfolio management and project selection. He develops his research work especially in relation with the pharmaceutical industry.

![](/api/attachments/7CNHPCN5/fulltext/images/7476e8f5f702f916dfdb6e2cea448c9a429106aebfdb39264f5c8027ddd428ea.jpg)

Frédéric Laarz is currently an engineer at the APAVE, in France. He graduated in Management and Production Engineering from the École Nationale Supérieure des Mines d'Albi-Carmaux, France, in 2010.
