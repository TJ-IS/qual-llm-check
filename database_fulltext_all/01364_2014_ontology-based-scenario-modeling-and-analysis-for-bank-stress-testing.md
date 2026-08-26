---
otero_id: 1364
otero_key: "NRJ8D628"
title: "Ontology-based scenario modeling and analysis for bank stress testing"
authors: "Daning Hu; Jiaqi Yan; J. Leon Zhao; Zhimin Hua"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.08.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ontology-based scenario modeling and analysis for bank stress testing

Daning Hu <sup>a</sup>, Jiaqi Yan <sup>a,</sup>⁎, J. Leon Zhao <sup>b</sup>, Zhimin Hua b

<sup>a</sup> Department of Informatics, University of Zurich, Zurich, Switzerland

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Kowloon, Hong Kong, China

## a r t i c l e i n f o

Available online xxxx

Keywords: Bank stress testing Ontology Scenario modeling Plausibility check

## a b s t r a c t

The 2008 banking crisis demonstrated that there is a lack of effective methods for modeling and analyzing “exceptional but plausible” risk scenarios in bank stress testing. Existing stress testing practices mainly focus on modeling probability-based risk factors and events in banking systems using historical data. Rare (low probability) risk events that can cause <sup>fi</sup>nancial crises in banking systems, such as the bankruptcy of Lehman Brothers, are largely ignored due to the lack of appropriate modeling and analysis methods. To address this problem, we propose an approach called Banking Event-driven Scenario-oriented Stress Testing (or simply, BESST) which has two main components: 1) an ontology-based event-driven scenario model (OESM), and 2) two analysis methods based on OESM for scenario recommendation and plausibility checking. The proposed BESST approach provides bank stress testing stakeholders an effective method for modeling and analyzing <sup>fi</sup>nancial crisis scenarios that are rare but often have signi<sup>fi</sup>cant consequences.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

The recent 2008 global <sup>fi</sup>nancial tsunami has been considered as the worst <sup>fi</sup>nancial crisis since the Great Depression. It was triggered by the decline of U.S. housing prices and resulted in a liquidity shortfall in the U.S. banking system, pushing it to the brink of a system-wide collapse. One of the major causes of this crisis was that the <sup>fi</sup>nancial stakeholders, including the major banks and regulators, failed to model and calibrate the “exceptional but plausible” scenarios in bank stress testing in which macroeconomic shocks may cause contagious bank failures and lead to the breakdown of a banking system [1]. Such crisis scenarios contain complex events of large magnitude and impact on banking systems that are often very rare (e.g., the bankruptcy of Lehman Brothers). These highly important events that are beyond the realm of normal expectations are called “Black Swan” events [2]. The 2008 <sup>fi</sup>nancial tsunami and the recent Euro debt crisis have demonstrated that modeling and analyzing such “Black Swan” events in bank stress testing is critical for the stability of the global banking system.

However, there are three major challenges in effectively modeling and analyzing stress testing scenarios that contain such exceptional but plausible events. First, existing stress testing methods mainly rely on probability-based models and historical <sup>fi</sup>nancial data such as the Value-at-Risk measure [3]. Such methods are not suitable for modeling “Black Swan” events which are very rare and often do not have any precedents. On the other hand, decision support technologies (e.g., conceptual modeling, business process modeling) and systems, which are becoming more and more popular in <sup>fi</sup>nancial risk management [4,5] and knowledge management [6], could provide new means to support bank stress testing.

Second, stress testing scenario designers (e.g., bank risk management professionals) need to imagine various possible <sup>fi</sup>nancial crisis scenarios. But their imaginations are often limited since “Black Swan” events are too rare to imagine or because of the groupthink within a profession. For example, the European Banking Authority in 2009 and 2010 designed their stress testing scenarios by assuming a relatively small (−0.6%) economic growth in the Euro area. However, in 2011 it was clear that such an assumption (−0.6%) was not only plausible but was certain to happen. They had to redesign the scenarios assuming a −4.0% growth scenario. Therefore, effective methods and tools are needed to support imagining all possible scenarios in stress testing, including such rare “Black Swan” events.

Third, the scenarios designed by stress testing designers also need to be checked for plausibility. Because of the complexities of various risk events and their interactions, designers may ignore risk factors or make mistakes in imagining such events, leading to implausible stress testing scenarios. An effective mechanism is needed to check the plausibility of the designed scenarios.

To address the three above challenges, we developed an approach called Banking Event-driven Scenario-oriented Stress Testing (or simply, BESST). BESST consists of two components: 1) an ontology-based event-driven scenario model (OESM), and 2) two analysis methods based on OESM for scenario recommendation and plausibility checking. The OESM provides a formal representation of stress testing domain knowledge and lays the foundation for modeling and analyzing exceptional but plausible <sup>fi</sup>nancial crisis scenarios. The second component aims to address the second and third research challenges.

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

To the best of our knowledge, BESST is the <sup>fi</sup>rst non-probabilitybased approach for modeling and analyzing exceptional but plausible stress testing scenarios without historical data. It enables <sup>fi</sup>nancial researchers to study the “Black Swan” events and their impacts in <sup>fi</sup>nancial crisis scenarios. From the practical perspective, BESST supports stress testing designers by providing 1) the capability of modeling exceptional but plausible crisis scenarios; 2) recommendations of plausible scenarios; 3) plausibility checks on designed scenarios.

The remainder of this paper is organized as follows. In the next section, we provide a review of related studies used in our scenario modeling approach. The third and fourth sections describe the proposed approach in detail. We then provide a case study to demonstrate how our approach can be used for bank stress testing. Finally, we discuss our contributions and future research directions.

## 2. Related studies

## 2.1. Bank stress testing approaches

Sorge and Virolainen [7] have proposed a schematic classi<sup>fi</sup>cation of existing stress testing approaches in <sup>fi</sup>nance literature. There are two types of approaches: 1) the piecewise approach, and 2) the integrated approach. The piecewise approach mainly focuses on modeling banks' vulnerabilities to single risk factors by forecasting several <sup>fi</sup>nancial indicators such as capital asset ratio and exposure to exchange rate risks under different economic environments. It generally models the direct linear relationships between macro fundamental variables (independent variables) and certain <sup>fi</sup>nancial risk indicators (dependent variables) (e.g., capital adequacy ratio and return on equity). The estimated coef<sup>fi</sup>cients are used to simulate the impacts of possible adverse economic scenarios on the banks' <sup>fi</sup>nancial risk indicators.

Therefore, the piecewise approach models an individual stress testing scenario as a combination of several macro fundamental variables. For instance, Kalirai and Scheicher [8] modeled the aggregate loan loss provisions in the Austrian banking system as a function of a set of macroeconomic variables which include general economic indicators such as GDP, CPI in<sup>fl</sup>ation, and income, consumption and investment in the household and corporate sectors. Hoggarth et al. [9] focused on the relationship between banks' loan write-offs and the UK output gap, retail and house price in<sup>fl</sup>ation, and the nominal short-term interest rate. Moreover, Saurina and Delgado [10] studied the relationship between loan loss provisions and a set of macroeconomic indicators which includes unemployment rate, interest rates and indebtedness.

The piecewise approach is very intuitive and its computational cost is usually low since these models are often in linear functional forms. However, in general there is a lack of empirical proofs for the validity of such linear relationships in past <sup>fi</sup>nancial crises. Relationships among risk factors in real-world <sup>fi</sup>nancial crisis scenarios are often much more complex than the linear relationship assumptions in the piecewise approach.

The integrated approach takes a further step to integrate the analysis of banks' vulnerabilities to multiple risk factors into a single estimate of the probability distribution of banks' losses under a stress scenario. This approach combines the analysis of multiple risk factors into a single distribution and models nonlinear effects of economic shocks on banks. The integrated approach differs from the piecewise approach from two perspectives: 1) it focuses on integrating the analysis of banks' market and credit risk factors rather than several single <sup>fi</sup>nancial risk indicators; 2) it enables researchers to model the non-linear relationships between the macroeconomic factors and possible bank losses, as opposed to just modeling the direct linear relationships as the piecewise approach did.

However, both piecewise and integrated approaches are limited in terms of their fundamental assumptions. First, both approaches assume that a scenario is “static” and all changes in macro fundamental variables happen at the same time and will not change during the course of study. But in reality, changes in risk factors are triggered by events or organizations' behaviors (e.g., Fed raises interest rate aiming to reduce in<sup>fl</sup>ation). And these events and behaviors can happen in different sequences and thus have different impacts on the stability of banking systems. In other words, these two approaches lack the ability to model and analyze risk event processes and banks in <sup>fi</sup>nancial crisis scenarios for stress testing

## 2.2. Scenario design and scenario plausibility

Currently, there are two primary approaches to designing the stress testing scenarios — the historical and the hypothetical approach [11]. The historical approach is based on historical data (e.g., using the largest observed changes or extreme values over a speci<sup>fi</sup>ed time period), while the hypothetical approach builds scenarios that are hypothetical and involve large movements thought to be plausible [12–14].

The setup of historical scenarios is based on the assumption that future crises will be similar to past ones. Thus, there is much criticism of the historical approach, arguing that bias toward historical experiences can lead to the risk of ignoring plausible but harmful scenarios which have not yet occurred [13]. Another challenge of the historical approach is rooted in the dynamic nature of <sup>fi</sup>nancial markets, e.g., the introduction of new <sup>fi</sup>nancial instruments that did not exist at the time of the historical stress event.

While historical scenarios are easier to implement and somewhat more tangible, the hypothetical approach may be the only available option when structural breaks in the <sup>fi</sup>nancial system – such as deregulation, consolidation, currency changes, etc. – make past history no longer informative [11,15]. The hypothetical approach constructs hypothetical shocks that are extreme but plausible changes in the external environment regardless of historical experience [11,16]. A hypothetical scenario is frequently based on a discretionary assessment by analysts, which tends to be the result of <sup>fi</sup>ercely debated discussions.

Despite their experiences, people who design stress testing scenarios are often limited by their imaginative capacities and fail to imagine exceptional but plausible scenarios. Sometimes this is because bank risk management professionals and researchers often rely on probabilitybased <sup>fi</sup>nancial risk management techniques and cannot imagine or believe events with extremely low chances like “Black Swan” events. Sometimes it is just that people do not possess the comprehensive deductive capabilities of computers to/that can predict all possible stress testing scenarios. Therefore, there is a lack of effective methods to support stress testing designers for considering all possible <sup>fi</sup>nancial crisis scenarios, including the exceptional but plausible ones.

Similarly, people often lack the capability to ensure the plausibility of the complex crisis scenarios they designed, simply because there are too many complex risk events and factors to consider with human deduction abilities. To address this issue, there are a few studies that propose some objective measurements of plausibility. For example, the plausibility is de<sup>fi</sup>ned as the distance from the scenario to the present state of the market in a probability perspective [17,18]. Statistical methods (e.g., extreme value approach [19], Monte Carlo simulation [20]) are used to design scenarios. As criticized by Quagliariello [11], these numerical and statistical methods are not practical and have the signi<sup>fi</sup>cant drawback that the risk factors may not behave as they did in the past, because these methods assume that there is no structural change over the entire period. Thus, an effective automatic deduction mechanism is needed to ensure the plausibility of the <sup>fi</sup>nancial crisis scenarios imagined by stress testing designers.

## 2.3. Ontologies for knowledge management

As discussed in Section 2.1, the capabilities of representing risk events and logical deductions are needed for designing stress testing scenarios which are driven by inter-dependent risk events. Ontologies combined with conceptual modeling [21] can provide such capabilities for scenario modeling since they are excellent knowledge representations for various domains, including <sup>fi</sup>nancial risk management [4]. Moreover, when ontologies are formalized using logic languages like <sup>fi</sup>rst-order logic, they can support logical deduction mechanisms, which are often used to derive new facts and check the logical consistency of the deduced facts. Therefore, ontologies to support/that support the knowledge representations and logical deductions of risk events are greatly needed in bank stress testing.

In this research, we adopted the ontology framework developed by Jurisica et al. [22] to meet knowledge management needs (i.e., knowledge representation and logical deductions) from an information systems perspective. This framework consists of four broad ontological categories, which, respectively, deal with static, dynamic, intentional and social aspects of the world. For a wide range of real-world applications, the representations of relevant knowledge can be built based on the primitive concepts derived from these four ontological categories. Static ontology describes the static aspects of the world (i.e., what things exist, their attributes and relationships) [23,24]. Dynamic ontology describes the changing aspects of the world in terms of states, state transitions and processes [25,26]. The intentional ontology can model individual or organizational motivations, intentions, goals, beliefs, choices, etc. [27–29]. Social ontology covers social settings, organizational structures or strategic dependencies between social actors [30–32]. These ontologies have been widely used for knowledge management purposes [33] and proved to be effective in supporting risk management in <sup>fi</sup>nancial and banking domains [34,35].

We suggest that these four types of ontologies can be customized and applied in bank stress testing to provide logical deduction capabilities. In particular, the intention as well as the capability of the actors (e.g., banks), which cannot be modeled using regular static ontology and is often ignored in existing stress testing approaches, can be effectively represented by intentional and dynamic ontologies. Intentional ontology can be used to justify the rationality of the activities of individuals or organizations and thereby can be used to 1) check the logical correctness of the events or process in any given scenario, or to 2) deduct and recommend all possible event/activities in stress testing scenarios. For example, either raising the interest rate or <sup>fi</sup>xing the exchange rate can be deduced from the event of in<sup>fl</sup>ation, because they are de<sup>fi</sup>ned to be means to achieve the goal of reducing in<sup>fl</sup>ation in an intentional ontology. On the other hand, by de<sup>fi</sup>ning the state changes associated with the execution of some tasks, dynamic ontology can be used to check whether the actor has the capability to change the state after the activity. Further, social ontology de<sup>fi</sup>nes the interactions and dependencies between actors. To summarize, four types of ontologies can be developed for bank stress testing to support logical deduction capabilities for scenario recommendation and plausibility checks.

## 3. Banking event-driven scenario-oriented stress testing (BESST)

To address the research challenges summarized in Sections 2.1 and 2.2, we proposed a bank stress testing approach called Banking Eventdriven Scenario-oriented Stress Testing (or simply, the BESST approach). Bank stress testing, as a multistage process [11], consists of economic modeling of the banking system, simulating stress testing scenarios and analyzing the impacts [36]. As shown in Fig. 1, the BESST approach provides decision support for generating stress testing scenarios, which consists of two components: 1) an ontology-based event-driven scenario model (OESM), and 2) two algorithms for checking scenario plausibility and recommending plausible scenarios.

OESM is composed of an event-driven scenario model and a set of bank stress testing ontologies. The event-driven scenario model de<sup>fi</sup>nes the risk events and organizational activities, as well as their interactions and the rules that govern their evolvement. We use business process <sup>fl</sup>owcharts to describe the dynamics of risk event sequences and event interactions in OESM. The four types of bank stress testing ontologies reviewed in Section 2.3 provide formal knowledge representations of the concepts and constraints used in the stress testing scenario modeling, as well as a foundation for logic deduction which enables plausibility checking and scenario recommendation. We will introduce the details of the BESST approach in the following sections.

## 4. Ontology-based stress testing scenario modeling

## 4.1. Event-driven scenario model

A stress testing scenario is a sequence of events. The events represent the facts of economic situations based the economic proposition at a time point. An economic proposition is a term or formula expressed in <sup>fi</sup>rst-order logic to describe the status of economic resources (e.g., low (interest\_rate), high (in<sup>fl</sup>ation\_rate)). An event describes the status of a time point where some economic propositions φ about economic resources hold true.

## De<sup>fi</sup>nition 1. Event

An event is a 3-tuple $\mathsf { e } = < \mathsf { t } , \mathsf { R } , \mathsf { P } > ,$ , where t is a time point; $\mathsf { R } = \left\{ \mathrm { r } \mid \mathrm { r } \right\}$ is an economic resource in the scenario}; $\mathsf { P } = \{ \mathsf { P } ( \mathsf { e } , \mathsf { r } ) \colon \mathsf { \varphi } ( \mathsf { r } ) \} \to \{ \mathsf { t r u e } ,$ false} and ${ \bf r } \in { \bf R } \}$ is the set of truth assignments of the economic propositions $\{ \varphi ( \mathbf { r } ) \}$ at each event.

In other words, an event represents the current state of the modeled scenario, expressed as the status of a set of economic resources. An event is the result of the occurrence of one or more activities. An activity corresponds to a task executed by some actors in the scenario.

## De<sup>fi</sup>nition 2. Activity

An activity is a 3-tuple baid, ag, tN, where aid is the unique identi<sup>fi</sup>er of the activity; ag is the actor who carries out the task; t is the task that is carried out by the actor.

Therefore, in each modeled stress testing scenario, there is a timeline in which one or more activities occur at each time step and lead the scenario into different events (states) over time. At an instantaneous time point, multiple activities may occur and their joint impacts will result in one event (described by the values of economic resources in De<sup>fi</sup>nition 1).

## De<sup>fi</sup>nition 3. Event-driven scenario

An event-driven scenario is de<sup>fi</sup>ned to be a tuple $s = { < } \mathrm { E } , \mathrm { A } ,$ LN, where E is the set of events in the scenario; A is the set of activities in the scenario; $\mathrm { L } = \{ \mathrm { n e x t } ( \mathbf { e } _ { \mathrm { i } } , \mathsf { A } _ { \mathrm { i } + 1 } , \mathbf { e } _ { \mathrm { i } + 1 } ) \mid \mathbf { e } _ { \mathrm { i } } , \mathbf { e } _ { \mathrm { i } + 1 } \in \mathrm { E } , \mathsf { A } _ { \mathrm { i } + 1 } \subseteq \mathsf { A } ,$ $\mathsf { A } _ { \mathrm { i } + 1 }$ is the set of (multiple) activities that happened between e and $\mathsf { e } _ { \mathrm { i } + 1 } \mathsf { e } _ { \mathrm { i } }$ and $\mathsf { e } _ { \mathrm { i } + 1 }$ are both instances of events in the scenario, $\mathsf { e } _ { \mathrm { i } + 1 }$ is the next event after e }.

To model the interactions between activities and events (states), we incorporate two modal connectives: ◊ (i.e., sometimes) and ○ (i.e., next). More speci<sup>fi</sup>cally, at a particular time t, ◊φ is true if $\boldsymbol { \Phi }$ is true at some future event occurring at the time after t, and ○φ is true if φ is true at the next event after t. Fig. 2 shows an example scenario. $\mathsf { e } _ { 1 }$ is going to happen after $\mathsf { e } _ { 0 } ,$ and e is going to happen in the future after ${ \sf e } _ { 0 } .$ . Therefore, at the time point of $\mathsf { e } _ { 0 } ,$ the economic propositions of ○increased(federal\_funds\_rates) and ◊increased(unemployment\_rate) are true.

## 4.2. Bank stress testing ontologies

In order to have a representation of the relevant knowledge in an event-driven scenario, we develop a set of stress testing ontologies to express the entities and their relationships in the scenario. This set of ontologies can be used as tools to advance scenario modeling knowledge and practice [37,38] and to support the logical reasoning in stress testing scenarios for plausibility checks and scenario recommendations.

![](/api/attachments/NRJ8D628/fulltext/images/6e5a873e84ee6855bd769f615eb7eb81dc1f0c46c897bc28638209a4ed2d5217.jpg)  
Fig. 1. How the BESST approach is used in bank stress testing.

## De<sup>fi</sup>nition 4. Ontology

To develop the ontology, we <sup>fi</sup>rst propose four meta-classes: Actor Class, Goal Class, Task Class and Resource Class, shown in Fig. 3. Every entity in the domain can be an instance of these metaclasses.

An ontology is de<sup>fi</sup>ned to be a set of constraints, which declare the entities and entities' relationships in the stress testing scenario, O = {c | c is a constraint declaring the entities and their relationships}.

• Actor models a <sup>fi</sup>nancial institution (e.g., bank) that has strategic goals, possesses resources and intentionally acts according to the principles of rationality within the organizational setting.

![](/api/attachments/NRJ8D628/fulltext/images/981bcb4c884d5a0258cc856378a4c986f1646d806605c8fcb9b989ff9c77482a.jpg)

${ \tt e } _ { 0 } \dot { . }$ Inflation

$\mathsf { e } _ { 1 } \cdot$ Federal funds rate is increased

$\mathsf { e } _ { 2 } \cdot$ lending rates are increased

$\mathsf { e } _ { 3 } \mathrm { : }$ unemployment rate is increased and house prices drop

Activities

$\mathsf { a } _ { 1 } \cdot$ Fed raises federal funds rate

$\mathsf { a } _ { 2 } .$ commercial bank raises lending rates

$\mathsf { a } _ { 3 } \mathrm { : }$ manufacturer reduces investments

$\mathsf { a } _ { 4 } \cdot$ real estate investor reduces housing investments

Fig. 2. An event-driven scenario

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

![](/api/attachments/NRJ8D628/fulltext/images/6345faec699809b95b95f49e7cf0528932693bd8308dc908fe930813975792c5.jpg)  
Fig. 3. Relations between meta-classes.

• Resource represents the material or information an actor observes/ manipulates. The description of the resource's status forms an economic proposition.

• Task represents the particular course of action that can be executed in order to satisfy a goal.

• Goal represents an actor's strategic interests that refer to the actor's desire state.

Based on prior ontology studies [22,34,35], we develop static, dynamic, intentional, and social ontologies for bank stress testing. These ontologies provide a broad knowledge representation of the stress testing scenario. In addition, these ontologies provide a knowledge base for logical reasoning about the plausibility of the stress testing scenario in terms of intention and capability. These four categories of ontologies can be speci<sup>fi</sup>ed as constraint metadata as de<sup>fi</sup>ned below.

## De<sup>fi</sup>nition 5. Constraint metadata

For each constraint $\mathrm {  ~ c \in 0 , }$ , its metadata is de<sup>fi</sup>ned as a <sup>fi</sup>ve tuple bcid, TY, P, H, MCN, where cid is the unique identi<sup>fi</sup>er of the constraint.

TY ∈ {static ontology, intentional ontology, dynamic ontology, social ontology}; P is the premise of the constraint; H is the conclusion of the constraint; MC is the set of relations between actor, task, resource and goals; MC = {mc | mc ∈ Actor ∪ Task ∪ Resource ∪ Goal}.

For example, c1 $( \mathsf { c } 1 : \mathsf { g } 1 \Rightarrow \mathsf { g } 2 \vee \mathsf { g } 3 )$ is a constraint meaning that if g1 (i.e., goal NO.1) exists, then either g2 or g3 exists. Here, ‘c1’ is the unique identi<sup>fi</sup>er cid of this constraint; c1.TY means the ontology type of the underlying constraint c (i.e., Intentional Ontology); ${ \mathrm { c 1 . H } } = { \mathrm { \ " g 2 ~ \vee ~ g 3 " } }$ , as the head of the constraint, is inferred by the premise of the constraint ${ \mathsf { c } } 1 . { \mathsf { P } } = { } ^ { \mathfrak { u } } { \mathsf { g } } 1 ^ { \mathfrak { n } }$

## 4.2.1. Intentional ontology

The intentional ontology models the actor's (e.g., <sup>fi</sup>nancial institutions) motivations — what the actor desires or intends to do. For example, the goals of the Federal Reserve (represented as a1) can be graphically represented as in Fig. 4. The goals can be further broken down into sub-goals by AND/OR decompositions. For instance, the goal of stable price (represented as g1) can be decomposed into reducing in<sup>fl</sup>ation (represented as g2) or reducing de<sup>fl</sup>ation (represented as g3), which can be represented by constraint c1; the goal of reducing in<sup>fl</sup>ation (g2) can be further decomposed into reducing inter-bank money supply (g4) and reducing public money supply (g5). This graphic representation can further be represented as constraint c1: g1 ⇒ g2 ∨g3, and c2: g2 ⇒ g4 ∧ g5.

Means-ends analysis can be used to connect the actor's goals and activities in modeled scenarios. For instance, the goal of reducing in<sup>fl</sup>ation (represented as g4) can be achieved by carrying out the task of raising the federal fund rate (represented as t1), which can be represented as a constraint c3: (a3, g4) ⇒ (a3, t1).

## 4.2.2. Dynamic ontology

The dynamic ontology de<sup>fi</sup>nes the economic propositions that will trigger the goals and de<sup>fi</sup>nes the economic propositions after carrying out tasks. In other words, the dynamic ontology represents the changing aspect of banking events. For example, as shown in Fig. 5, the goal of reducing in<sup>fl</sup>ation (represented as g2) is triggered by the economic proposition of highIn<sup>fl</sup>ationRate() (represented as φ), which can be represented as constraint c4: φ(r1) ⇒ (a3,g2).

![](/api/attachments/NRJ8D628/fulltext/images/ba0454dcff613d5c4eec4775a2fe2a747b40719831a7ebff36bed836aa87fc66.jpg)  
Fig. 4. Intentional ontology.

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/NRJ8D628/fulltext/images/b9ded21d33a1e1073814b97e6eaf15af77bea7ec13efe37618acf4e1f80d75d1.jpg)  
Fig. 5. Dynamic ontology.

The constraint of “the Federal funds rate will surge (represented as ψ) after carrying out the task of raising federal funds rate (represented as t1)” can be written as c5: $( \mathsf { a } 3 , \mathsf { t } 1 ) \Rightarrow \psi ( r 4 )$

## 4.2.3. Static ontology

The static ontology represents the static aspect of the <sup>fi</sup>nancial market and de<sup>fi</sup>nes the basic relation of actors and resources. For instance, as shown in Fig. 6, Fed (a3) is a kind of central bank (a2), represented as c6: a3 a2; US CPI (r3) is a kind of information rate (r1), which can be written as c7: r3 r1; it is the US CPI (represented as r3) that triggers the goal of reducing the in<sup>fl</sup>ation rate (g2), represented as c8: g2 a3 × #r3; the interest rate the Fed can manipulate (task t1) is the Federal Funds Rate (r4), represented as c9: t1 a3 × #r4.

## 4.2.4. Social ontology

The social ontology describes the social aspects of bank stress testing. In particular, it expresses knowledge about the social structure and interactions of <sup>fi</sup>nancial institutions. Three types of relationships are de<sup>fi</sup>ned: goal dependency, task dependency and resource dependency. For example, as shown in Fig. 7, the Fed's (a3) goal “public money supply reduced” (g5) relies on the commercial bank (a1), represented as c10: ${ \bf g } 5 \subseteq { \bf a } 1 \times { \bf a } 3 ;$ since the commercial bank has a relation with Federal Reserve with the Federal Funds Rate (resource dependency), the manipulation of “Federal Funds Rate” (r4) will have an impact on commercial banks (a1), which can be represented as constraint c11: #r4 a1 × a3; the commercial bank (a1) relies on manufacturer (a4) to repay the loan (t3), represented as c12: t3 a1 × a4.

## 4.3. Ontology development

The process of scenario modeling and analysis begins with the development of bank stress testing ontologies. Different stress testing practices require different types of knowledge that result in different stress testing ontologies. To ensure the scalability and generalizability of the proposed bank stress testing ontologies, we propose an ontology development method based on the four basic types of ontologies described in 4.2. This method aims to guide the users to develop their own stress testing ontologies using the four basic types.

To assess whether the ontologies developed by a user appropriately cover the complete domain of interest (in his stress testing application), a common approach is to use competency questions – a natural language processing technique – to <sup>fi</sup>nd relevant terms in/for ontology development [39]. Based on the proposed four basic types of bank stress

![](/api/attachments/NRJ8D628/fulltext/images/ddb1f02b1b006a7fb2c2ece519d2b808295b595bb212c32c1693a99a7b3855fe.jpg)  
Fig. 6. Static ontology.  
Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/NRJ8D628/fulltext/images/78daab5348853c13f3efa6266def285d433ba71aa04bde85306b843eb7903e6e.jpg)  
Fig. 7. Social ontology.

testing ontologies, we develop a set of general competency questions, adapted from [40], to help the bank stress testing users develop ontologies for their speci<sup>fi</sup>c needs.

• Competency questions for key classes

➢ What <sup>fi</sup>nancial individual/institution may be involved in the scenario?

➢ What activities may be involved in the scenario? What's the goal for each activity?

➢ What economic resources may be used in the scenario?

• Competency questions for intentional ontology

➢ What goal is an individual/institution committed to achieving?

➢ What activities must a particular individual/institution perform to achieve the goal?

• Competency questions for static ontology

➢ In order to perform a particular activity, which resource is needed? ➢ Given a set of actions that occur at different points in the future, what are the properties of resources and activities at arbitrary points in time?

• Competency questions for dynamic ontology

➢ Is it possible for an individual/institution to perform an activity in some situation? Does the individual/institution have the ability to perform the activity?

➢ What sequence of activities must be completed to achieve some goal? At what times must these activities be initiated and terminated?

• Competency questions for social ontology

➢ Which <sup>fi</sup>nancial individual/institution will be in<sup>fl</sup>uenced if an activity is carried out?

➢ Which <sup>fi</sup>nancial individual/institution will be in<sup>fl</sup>uenced if a goal is achieved? Which <sup>fi</sup>nancial individual/institution will be in<sup>fl</sup>uenced if a resource is changed?

As shown in Fig. 8, when the existing ontologies developed by a user contain enough information to answer these types of questions, these ontologies have completely covered the domain of interests for the underlying users. Otherwise, an expansion to existing ontologies is needed. New de<sup>fi</sup>nitions and facts can be added to existing ontologies to expand them [40,41].

![](/api/attachments/NRJ8D628/fulltext/images/0f3adba26bf125b546cffbd7b97aa67fc3412d3a023c08e502c58876b45d397a.jpg)  
Fig. 8. Ontology development and ontology expansion

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

## 5. Plausibility check and scenario recommendation

## 5.1. Plausibility check

## 5.1.1. Plausibility and Implausibility of a stress testing scenario

The quality of a stress test depends on the stress testing scenario used, the requirements of which are “exceptional but plausible.” An important criterion to design stress testing scenarios is to model events that are severe but may/could happen. In this subsection, we discuss the plausibility and implausibility in a scenario.

As de<sup>fi</sup>ned above, a stress testing scenario consists of a sequence of events which are sets of truth assignments of economic propositions. An economic proposition is plausible when it can be justi<sup>fi</sup>ed with “capability” and “intention,” in other words, the economic resources can reach a status because some actor has the capability to manipulate the economic resources into this status and the actor has an intention to do so. For example, interest rates are currently low because the Federal Reserve has the capability to manipulate the interest rate and it lowers the interest rate intentionally. We regard a scenario as a plausible scenario if all of the economic propositions in the scenario are plausible.

## De<sup>fi</sup>nition 6. Plausibility of a scenario

An economic proposition φ(resource) (resource ∈ Resource) is de<sup>fi</sup>ned to be plausible, $\mathrm { i f ~ \exists ~ \in \mathfrak { a } \in A c t o r , \ \exists ~ t \in T a s k , \ \exists ~ g \in G o a l , }$ $( \mathbf { a } , \mathbf { t } ) \Rightarrow \varphi ( \mathbf { r } ) , ( \mathbf { a } , \mathbf { g } ) \Rightarrow ( \mathbf { a } , \mathbf { t } ) .$ . A stress testing scenario is de<sup>fi</sup>ned to be plausible if all of the economic propositions in the scenario are plausible.

To detect an implausible scenario, we propose two kinds of implausibility: capability implausible and intention implausible. An economic proposition is capability implausible if none of the actors (in the situation) has the capability of manipulating the resources to the status that the economic proposition states. Intention implausible of an economic proposition refers to the situation that none of the actors has the intention to manipulate the economic resources to the status that the economic proposition states. A stress testing scenario is regarded as implausible if any economic proposition in the scenario is either capability implausible or intention implausible.

## De<sup>fi</sup>nition 7. Implausibility of a scenario

An economic proposition φ(resource) (resource ∈ Resource) is de<sup>fi</sup>ned to be capability plausible, iff $\forall \mathbf { a } \in \mathbf { A c t o r } , \lnot \exists ~ \mathbf { t } \in \mathrm { T a s k } ,$ $( \mathsf { a } , \mathsf { t } ) \Rightarrow \varphi ( \mathsf { r } )$ . An economic proposition φ(resource) (resource ∈ Resource) is de<sup>fi</sup>ned to be intention implausible, iff ∀a ∈Actor, $\beth \ \mathrm { g } \in { \mathrm { G o a l } } , \ \left( \mathrm { a } , \ \mathrm { g } \right) \bumpeq \left( \mathrm { a } , \ \mathrm { t } \right)$ , where t ∈ Task, (a, t) ⇒ φ(r). A stress testing scenario is de<sup>fi</sup>ned to be implausible if there's any economic proposition in the scenario that is either capability implausible or intention implausible.

## 5.1.2. Plausibility check algorithm

Plausibility check is a process of detecting the intention implausibility and capability implausibility in a given stress testing scenario. We <sup>fi</sup>rst present lemmas that give rise to stress testing scenario veri<sup>fi</sup>cation rules, which lay the foundation for plausibility checks in a scenario.

Lemma 1. Conditions for capability implausible

Given a scenario $s = < \mathrm { ~ E , ~ A , ~ } \mathrm { L } \mathrm { > } ,$ if ∃event = bt,R.PN ∈ s.E, φ event.P, activit $\begin{array} { r } { { \boldsymbol { y } } = < \mathrm { a i d } , \mathrm { a g } , \mathrm { t s k } > \in \mathrm { { \sf s } } . { \mathrm { A } } , } \end{array}$ actor = activity.ag, task = activity.tsk, l = next(activity,event) ∈ s.L, ∀c ∈ O, c.TY = dynamic ontology, c.P = (actor, task), c.H∩φ = Ф (Ф is an empty set), then s is capability implausible.

Discussion: In this proposition, an event appears after an activity. However, we cannot <sup>fi</sup>nd any dynamic ontology that de<sup>fi</sup>nes that the task carried out in the activity can lead to the event. Therefore, it is capability implausible that the event can appear after the activity.

## Lemma 2. Conditions for intention implausible

Given a scenario $s = < \mathrm { E , A , R C , L , e } _ { s } > , \mathrm { i f \exists e v e n t = < t , R . P > \in { s . E } } ,$ $\exists \boldsymbol { \varphi } \in \mathrm { e v e n t . P }$ , ∃activit $\prime = < \mathrm { a i d } , \mathrm { a g } , \mathrm { t s k } > \in { \tt S } . { \tt A }$ , actor = activity.ag, task = activity.tsk, l = next(event,activity) ∈ s.L, ∀c ${ \mathrm { , } } { \mathrm { 2 } } \in { \mathrm { 0 } } ,$ c1.TY = dynamic ontology, ${ \mathrm { c 1 . P } } = \varphi , { \mathrm { c 2 } } = { \mathrm { i n t e n } }$ tional ontology, ${ \mathsf { c } } 2 . { \mathrm { H } } = ( { \mathsf { a c t o r } } ,$ task), ${ \mathsf { c } } 1 . { \mathsf { H } } { \cap } { \mathsf { c } } 2 . { \mathsf { H } } = \Phi$ (Ф is an empty set), then s is intention implausible.

Discussion: In this proposition, an activity (an actor carries out a task) appears after an event. However, we cannot <sup>fi</sup>nd any intentional ontology de<sup>fi</sup>ning a goal that triggers this task after that event. In other words, the activity that happened after the event is without intention. Thus, the s is intention implausible.

A plausibility check algorithm based on the lemmas is developed, as shown in Fig. 9, to check the plausibility of a scenario. By applying this algorithm to the event-driven stress testing scenario, we can identify the intention implausibility and capability implausibility. This algorithm also illustrates the precedence of the two lemmas, i.e., the sequence of applying the lemmas on plausibility checks in the scenario. More specifically, we <sup>fi</sup>rst check activity constructs with the intentional ontology to see whether this activity is to achieve some goal. If it is an activity without any goal, then it is a case of intention implausible. Otherwise, the goal of this activity will be further checked in the dynamic ontology to see whether the goal is to be triggered by the event before this activity. If the economic propositions in the event preceding the activity do not trigger the goal, then it is a case of intention implausible. For the event after the activity, the dynamic ontology will be checked to see whether this event is caused by the prior activity. If the activity results in the event, then the economic propositions in this event are plausible. Otherwise, it is a case of capability implausible.

## 5.2. Stress testing scenario recommendation

## 5.2.1. Scenario recommendation

Scenario recommendation is a process of providing possible but plausible events and activities for the user's consideration when designing the stress testing scenario. In this section, we will <sup>fi</sup>rst de<sup>fi</sup>ne the

Procedure Plausibility check in a scenario $\mathtt { s } = < \mathsf { E } , \mathsf { A } , \mathsf { L } >$

For each event $\scriptstyle \mathtt { e = \mathtt { d } , R , P > }$

For each activity ac=<aid, ag, t> s.A following e

{Check the intentional ontology

If goal g, and (ag, g) (ag, t)

{Check the dynamic ontology

If e1.P and (ag, g)

{For the event $\mathtt { e 1 = < t , R , P > }$ follows the activity ac

{Check the dynamic ontology

If e1.P-e.P and (ag, g)

Else print “Capability Implausible”}

}Else print “Intention Implausible”}

Else print “Intention Implausible”}

Fig. 9. The plausibility check algorithm.

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

logic of scenario recommendation and then discuss the completeness and soundness of the recommendation logic.

At any instant of an event, there are potentially many different future events in which the scenario can evolve. Thus, to model what possible scenarios may exist and can be recommended to the user, we link different possible scenarios to the stress testing scenario that user is designing with a RECOMMEND-Link. When the stress testing scenario evolves, we say it is in a new stress testing event in which new economic propositions hold true and the sets of possible scenarios have altered.

## De<sup>fi</sup>nition 8. Scenario recommendation logical system

A scenario recommendation logical system is de<sup>fi</sup>ned to be a fourtuple M = bS, RECOMMEND, PS, EtN, where S is a set of stress testing scenarios; RECOMMEND is a set of connections that maps the stress testing scenario to the possible scenarios, i.e., RECOMMEND $S \times E t \times P S ;$ PS is a set of possible scenarios; Et is the set of stress testing events that are shared by the stress testing scenario and the possible scenarios.

Suggested economic propositions, denoted by ⊨, are given with respect to a scenario recommendation logical system M and a scenario s. The expression M, s ⊨φ is read as “the scenario recommendation logical system M in scenario s suggests φ.”

Depending on the scenario complexity, it could be dif<sup>fi</sup>cult to analyze every possible future event, thus some “exceptional” scenario could be missing. Therefore, the scenario recommendation logical system can be evaluated from the perspective of completeness. We de<sup>fi</sup>ne two levels of completeness in terms of whether the model could forecast all future events or the next event(s) to happen from the inferences of the bank stress testing ontologies. More speci<sup>fi</sup>cally, if the recommendation logic can suggest all of the future plausible economic propositions de<sup>fi</sup>ned in the bank stress testing ontologies, it is regarded as strong complete. If the recommendation logic can suggest all the plausible economic propositions in the next event, it is regarded as weak complete.

## De<sup>fi</sup>nition 9. Completeness of scenario recommendation logical system

Given a set of bank stress testing ontologies, a scenario recommendation logical system M is strong complete, iff ∀◊φ that is plausible, s S, M, s ◊φ. A scenario recommendation logical system M is weak complete, iff ∀○φ that is plausible, $\exists s \in S , M , s \in O \varphi .$

Implausibility of economic propositions may exist in a possible scenario. A good scenario recommendation logical system should ensure the plausibility of recommended scenarios in a perspective of soundness. We provide two levels of soundness: strong sound and weak sound. If all the future economic propositions suggested by the scenario recommendation logical system are plausible, it is regarded as strong sound. If all the economic propositions in the next event recommended by the recommendation logic are plausible, it is regarded as weak sound.

## De<sup>fi</sup>nition 10. Soundness of scenario recommendation logical system

Given a set of bank stress testing ontologies, a scenario recommendation logical system M is strong sound, iff ∀s ∈ S, M, s ⊨ ◊φ, ◊φ is plausible. A scenario recommendation logical system M is weak sound, iff $\forall s \in S , M , s \in \mathsf { O } \varphi ,$ ○φ is plausible.

## 5.2.2. Scenario recommendation algorithm

Fig. 10 shows an algorithm that aims to construct a scenario recommendation logical system for the ontology-based scenario model. It is proven that this logical system is weak complete and weak sound.

The core part of the algorithm is the traversals of the ontologies to seek the possible scenario that predicts a next event for the user to design his/ her stress testing scenario. When the user chooses a scenario from the possible scenarios, we say the stress testing scenario has evolved to a new event, and a new traversal of the ontologies will generate a new set of possible scenarios for predicting a next event for the new stress testing scenario. Fig. 11 shows the process of constructing the scenario recommendation logical system. We <sup>fi</sup>rst construct a stress testing scenario s<sub>0</sub> by the given starting event E0. Then a set of possible scenarios {s<sub>01</sub>, s<sub>02</sub>, …, s<sub>0m</sub>} are generated through inferences in the ontologies. Assuming that the user chooses scenario $\mathsf { S } _ { 0 1 }$ as the new stress testing scenario, we say it evolves to the time point of E1, and a new set of possible scenarios $\left\{ { { S _ { 0 1 1 } } , { S _ { 0 1 2 } } , . . , { S _ { 0 1 n } } } \right\}$ are recommended to the user.

Fig. 12 shows an example of the process to construct a possible scenario from inferences in the ontologies. First, the static and social ontologies are checked to see which actor will be evoked; <sup>fi</sup>nding one of the responsibilities of actor “Fed” is to monitor the changing status of US CPI. The dynamic ontology is checked then in step 2(b), and because it is in an event consisting of an economic proposition on high in<sup>fl</sup>ation rate φ(r1), the head of constraint c4 (as shown in Fig. 5) will be assigned to be true in the current event. In step 2(c), the activity of raise the federal funds rate will be executed (constraint c3 in Fig. 4). A new event, high federal funds rate, will then be assigned to the scenario according to constraint c5 (as shown in Fig. 5).

We propose that the scenario recommendation logical system constructed by our algorithm is weak complete and weak sound.

Theorem 1. The scenario recommendation logical system M is weak complete.

Proof: According to De<sup>fi</sup>nition 10, ∀○φ that is plausible, $\exists \mathsf { a } \in \mathsf { A c t o r } ,$ $\exists \mathrm { t } \in \mathrm { T a s k } , \exists \mathrm { g } \in \mathrm { G o a l } , ( \mathrm { a } , \mathrm { t } ) \Rightarrow \varphi ( \mathrm { r } ) , ( \mathrm { a } , \mathrm { g } ) \Rightarrow ( \mathrm { a } , \mathrm { t } )$ . Thus, a constraint will be found in the intentional ontology de<sup>fi</sup>ning the relation between goal and task, and a constraint will be found in the dynamic ontology de<sup>fi</sup>ning the task and φ, the goal and the current event. If there exists a next event stating φ, then the proposition has been proved.

Otherwise, according to Steps 3, 4 and 5, because there is a constraint de<sup>fi</sup>ned in dynamic ontology, a new scenario will be constructed with a next event stating φ.

Theorem 2. The scenario recommendation logical system M is weak sound.

Proof: According to Steps 3, 4 and 5, the next event will be constructed only when the actor has the goal to execute the task. In other words, some actors have the capability to manipulate the economic resources into the economic proposition and the actors have intentions to do so. Thus, the economic proposition derived from the next event of the scenario recommendation logical system M is plausible. Therefore, M is weak sound.

## 6. Case study

The proposed scenario modeling and analysis approach provides stress testing designers with the capabilities to model exceptional but plausible <sup>fi</sup>nancial crisis scenarios. In order to further validate the BESST approach, we conduct a case study.

## 6.1. Ontology development

The <sup>fi</sup>rst step for scenario modeling and analysis is to build the domain ontologies for bank stress testing. As introduced in Section 4.3, the user may start the ontology development by de<sup>fi</sup>ning the domain and scope using the competency questions. In this period, the user will write down a list of <sup>fi</sup>nancial institutions to be involved in the scenario. These institutions will pursue different goals, and their possible activities to achieve the goals will also be identi<sup>fi</sup>ed.

The user gives a set of answers to the competency questions in the form of Fig. 13. As we can see, not only commercial banks, but also the Federal Reserve, U.S. government, workers and the manufacturer are identi<sup>fi</sup>ed as actors in the ontologies. Their possible behaviors include the Fed raising interest rates, the government controlling prices and wages, the manufacturer employing works, commercial banks loaning to manufacturers, etc. These ontological constraints are written in natural language in Fig. 13. They can also be represented in the <sup>fi</sup>rst-order logic or

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

Step 1: Construct a stress testing scenario consisting of the single event, and set the event as current event.

Step 2: Repeat until none of (a) – (d) below applies

(a) Check static/social ontology and evoke direct/indirect actors.

c O, c.TY = static ontology, if c.P R, then assign c.H true at the current event. c O, c.TY = social ontology, if c.P R, then assign c.H true at the current event.

(b) Check dynamic ontology and trigger goals of evoked actors. Construct new scenarios as a possible scenario with every triggered goal.

c O, c.TY = dynamic ontology, if c.P P, then construct a new scenario with assign c.H true at the current event.

(c) Check intentional ontology and assign new activities to the scenario.

c O, c.TY = intentional ontology, if c.P P, then construct a new activity and assign c.H to the activity.

If there exists more than one c meeting the above condition, then construct new activities assigned with the Combination(c).H.

(d) Check dynamic ontology and assign new event to the next event of the scenario.

Construct a new event.

c O, c.TY = dynamic ontology, if c.P A, then assign c.H to the new event.

Step 3: User chooses a scenario from the possible scenarios. Then the selected

scenario is set as the stress testing scenario.

Step 4: Repeat Step 2 & Step 3, until the user gets the desired stress testing scenario.

Fig. 10. The scenario recommendation algorithm.

conceptual models introduced in Section 2.2. To illustrate the process of plausibility check and scenario recommendation with these ontological constraints, the conceptual models are used to represent the ontological constraints c1 to c9, as shown on the right side of Fig. 14.

## 6.2. Plausibility check and scenario recommendation

Fig. 14 shows an example of how the user can model a stress testing scenario based on the ontologies. This example demonstrates the two main functions of BESST: 1) automatically suggest the possible constructs (e.g., events) in stress testing scenarios, 2) verify the correctness of constructs (check the plausibility of the designed scenarios).

In this example, when the user wants to model an activity after an event of “in<sup>fl</sup>ation,” several possible activities are suggested by the deduction capability of BESST based on the intentional ontology c1 and c2. After the user chooses “raise interest rate” as the stress testing activity, a new event “interest rate surges” can be inferred from the dynamic ontology c3. If the user wants to have either “real estate investor increases housing investment” or “manufacturer reduces production” as the next activity, the ontologies will also have a process of detecting

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

Stress Testing Scenario

Possible Scenarios

![](/api/attachments/NRJ8D628/fulltext/images/1a22c57db7dc4ae1004f8b4dcf03c64706b8735b63375e6e0cd2e9b4dcfbb55a.jpg)  
Fig. 11. Scenario recommendation.

intention and capability implausibility. First, the social ontologies suggest that both the real estate investors and manufacturers depend on loans from commercial banks, and the rates of loans are determined by interest rates as de<sup>fi</sup>ned in the static ontology. However, the event “interest rate surges” will trigger the real estate investor’s goal of “pay as little interest as possible” and carry out a task of “reduce real estate investment.” Thus, the activity “increase real estate investment” is intention implausible. If the user chooses the activity “manufacturers reduce production,” which will result in a decrease in employment, the event “unemployment rate is decreased” would be capability implausible.

Based on our experience with the above case study, we summarize the methodological and practical contributions of the proposed BESST approach. First, to the best of our knowledge, it is the <sup>fi</sup>rst to use conceptual modeling methods to systematically model bank stress testing scenarios, especially the “exceptional but plausible” Black Swan <sup>fi</sup>nancial crisis scenarios that are not captured by the traditional <sup>fi</sup>nance approaches. Second, the plausibility check along with the intention implausibility and capability implausibility concepts help the stress testing stakeholders to better validate the plausibility of extreme scenarios they design/imagine. Third, the scenario recommendation function is a practical tool that helps scenario designers consider complex and rare scenarios that are beyond their imagination. In the above example, the activity “control wage and price” may not be considered by the scenario designers, since there are few example of “control wage and price” in the history. However, the government has the ability and may intend to take this action in extreme economic conditions.

As Fig. 1 shows, after we used the BESST approach to design stress testing scenarios, these scenarios are then used as base settings for simulating <sup>fi</sup>nancial crises. In such simulations, the values of variables (e.g., interest rate) of the designed risk events and activities are drawn from probability distributions of real-world <sup>fi</sup>nancial data. The simulation is not the focus of this paper since it is not part of the BESST approach. But we intend to study and integrate it with BESST in the future for developing better bank stress testing approaches.

The simulation consists of two steps. In the <sup>fi</sup>rst step, we use the BESST approach to create a set of base scenarios. In the second step, for each base scenario, we generate systemic risk scenarios in which various <sup>fi</sup>nancial variables of interest covering a wide range of possible situations are simulated. These variables are drawn from pre-speci<sup>fi</sup>ed probability distributions that are assumed to be known, including the analytical function and its parameters.

## 7. Conclusion

In this study, we developed an ontology-based bank stress testing approach called BESST. BESST provides the stress testing stakeholders

![](/api/attachments/NRJ8D628/fulltext/images/d518bfc0ad8f91e020fd7270e561d8367b72d265f89baca1a187c4a27927569d.jpg)  
Fig. 12. Constructing a possible scenario.  
Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

c1: (Intentional Ontology) Federal Reserve has a goal to reduce inflation, which can be achieved by either raising the interest rate or fixing the exchange rate.

c2: (Intentional Ontology) U.S. Government has a goal to reduce inflation, which can be achieved by controlling wages and prices.

c3: (Dynamic Ontology) Carrying out the task of raising the interest rate results in interest rate surge.

c4: (Social Ontology) Manufacturer relies on loans from commercial banks.

c5: (Social Ontology) Manufacturer needs to pay interest for the loans from commercial banks.

c6: (Social Ontology) Workers rely on employment from manufacturer.

c7: (Social Ontology) Manufacturer depends on workers to carry out production.

c8: (Static Ontology) The employment rate has a data-property relationship with employment.

c9: (Static Ontology) The interest paid to commercial banks has a data-property relationship with interest rate.

Fig. 13. Key ontological constraints.

![](/api/attachments/NRJ8D628/fulltext/images/8e2b03c5f0d3ff2e72176e44c1dc09b818ffbc5d27cef5ea4127bb1948d24dd8.jpg)  
Fig. 14. The role of ontologies in scenario modeling.

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

with 1) the capability to model “exceptional but plausible” <sup>fi</sup>nancial crisis scenarios; 2) recommendations of possible scenarios at each time step in a modeled scenario; as well as 3) the plausibility check on the designed scenarios.

We claim the following contributions from both methodological and practical perspectives. First, to the best of our knowledge, this study is the <sup>fi</sup>rst to introduce ontology and conceptual modeling methods into designing bank stress testing scenarios. It provides researchers and practitioners new methods and tools other than probability-based econometric approaches for modeling “exceptional but plausible” <sup>fi</sup>nancial crisis scenarios without historical data. In addition, the plausibility check and scenario recommendation mechanisms in BESST provide stress testing stakeholders practical tools for developing complex and rare crisis scenarios that are dif<sup>fi</sup>cult to imagine and also plausible.

For future research, we aim to 1) integrate the BESST approach with simulation methods into a decision support system for bank stress testing, and 2) explore the possibility of extending the scenario recommendation functions to strong complete and sound.

## Acknowledgements

This research was partly supported by the GRF Grant 9041582 of the Hong Kong Research Grant Council, the endowment fund “Fonds zur Förderung des Akademischen Nachwuchses (FAN)” of Zürcher Universitätsverein (ZUNIV), the Grant 7008121 from City University of Hong Kong, and a startup grant from the Faculty of Economics, Business Administration and Information Technology at University of Zurich.

## References

[1] D. Hu, J.L. Zhao, Z. Hua, Ranking systemic risks in banking networks, ICIS 2010 Proceedings. 2010.

[2] N.N. Taleb, The Black Swan: The Impact of The Highly Improbable, Random House Trade Paperbacks, 2011.

[3] P. Jorion, Value At Risk: The New Benchmark for Controlling Market Risk, Irwin Professional Publishing, Chicago, 1997.

[4] C. Zopounidis, M. Doumpos, N.F. Matsatsinis, On the use of knowledge-based decision support systems in <sup>fi</sup>nancial management: a survey, Decision Support Systems 20 (3) (1997) 259–277.

[5] M. Doumpos, C. Zopounidis, A multicriteria decision support system for bank rating, Decision Support Systems 50 (1) (2010) 55–63.

[6] T.S. Raghu, A. Vinze, A business process context for knowledge management, Decision Support Systems 43 (3) (2007) 1062-1079

[7] M. Sorge, K. Virolainen, A comparative analysis of macro stress-testing methodologies with application to Finland, Journal of Financial Stability 2 (2) (2006) 113-151.

[8] H. Kalirai, M. Scheicher, Macroeconomic stress testing: preliminary evidence for Austria, Financial Stability Report 3 (2002) 58–74.

[9] G. Hoggarth, A. Logan, L. Zicchino, Macro Stress Testing UK Banks, Bank of England, Paper Presented at The Workshop on Financial Stability in Frankfurt, 2004.

[10] J. Delgado, J. Saurina, Credit Risk And Loan Loss Provisions: An Analysis with Macroeconomic Variables, Directorate General Banking Regulation, Bank of Spain, 2004

[11] M. Quagliariello, Stress-Testing The Banking System: Methodologies and Applications, Cambridge University Press, 2009.

[12] M. Sorge, Stress-Testing Financial Systems An Overview of Current Methodologies. , 2004.

[13] J.W. Van Den End, M. Hoeberichts, M. Tabbae, Modelling Scenario Analysis and Macro Stress-Testing 2006: De Nederlandsche Bank, , 2006.

[14] T. Breuer, G. Krenn, O. Nationalbank, Identifying Stress Test Scenarios, Citeseer 2000.

[15] O. Nationalbank, Guidelines on Market Risk, Stress Testing, 1999.

[16] T. Breuer, O. Nationalbank, How to Find Plausible, Severe, and Useful Stress Scenarios, Oesterreichische Nationalbank, 2009.

[17] T. Breuer, G. Krenn, What Is A Plausible Stress Scenario Computational Intelligence: Methods and Applications, ICSC Academic Press, Canada/Switzerland, 2001. 215–221.

[18] T. Breuer, et al., Inter-risk Diversi<sup>fi</sup>cation Effects of Integrated Market and Credit Risk Analysis Oenb Mimeo 2008

[19] F.M. Longin, From value at risk to stress testing: the extreme value approach, Journal of Banking & Finance 24 (7) (2000) 1097–1130

[20] H. Elsinger, A. Lehar, M. Summer, Risk assessment for banking systems, Management Science 52 (9) (2006) 1301–1314.

[21] Y. Wand, et al., Theoretical foundations for conceptual modelling in information sys tems development, Decision Support Systems 15 (4) (1995) 285–304

[22] I. Jurisica, J. Mylopoulos, E. Yu, Ontologies for knowledge management: an information systems perspective, Knowledge and Information Systems 6 (4) (2004) 380–401.

[23] Z. Zhang, C. Zhang, S. Ong, Building an ontology for <sup>fi</sup>nancial investment. Intelligent Data Engineering and Automated Learning—IDEAL 2000, Data Mining, Financial Engineering, And Intelligent Agents, 2000. 379–395.

[24] S.L. Alonso, et al., WP10: Case study ebanking D10. 7 Financial ontology, Data, Information and Process Integration With Semantic Web Services 2005. (FP6–507483)

[25] D. Harel, Statecharts: a visual formalism for complex systems, Science of Computer Programming 8 (3) (1987) 231–274

[26] A.W. Scheer, ARIS—Business Process Modeling, Springer Verlag, 2000.

[27] P. Giorgini, J. Mylopoulos, R. Sebastiani, Goal-oriented requirements analysis and reasoning in the Tropos methodology, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 18 (2) (2005) 159–171.

[28] L. Chung, J. Do Prado Leite, On non-functional requirements in software engineering, Conceptual Modeling: Foundations and Applications, 2009. 363–379.

[29] J. Mylopoulos, L. Chung, E. Yu, From object-oriented to goal-oriented requirements analysis, Communications of the ACM 42 (1) (1999) 31–37.

[30] E.S.K. Yu, Modeling Organizations for Information Systems Requirements Engineering, IEEE, 1993.

[31] E. Yu, Modeling strategic relationships for process reengineering, Social Modeling for Requirements Engineering, 2011. 11.

[32] E.S.K. Yu, J. Mylopoulos, Y. Lespérance, Al models for business process reengineering, IEEE Expert 11 (4) (1996) 16–23.

[33] L. Aldin, S. De Cesare, A literature review on business process modelling: new frontiers of reusability, Enterprise Information Systems 5 (3) (2011) 359–383.

[34] K. Ye, et al., Ontologies for crisis contagion management in <sup>fi</sup>nancial institutions, Journal of Information Science 35 (5) (2009) 548–562.

[35] K. Ye, et al., Knowledge level modeling for systemic risk management in <sup>fi</sup>nancial institutions, Expert Systems with Applications 38 (4) (2011) 3528–3538.

[36] D. Hu, et al., Network-based modeling and analysis of systemic risks in banking systems, MIS Quarterly 36 (34) (2012) 1269–1291.

[37] G. Shanks, E. Tansley, R. Weber, Using ontology to validate conceptual models, Communications of the ACM 46 (10) (2003) 85–89.

[38] R. Weber, Conceptual modelling and ontology: possibilities and pitfalls, Journal of Database Management 14 (3) (2003) 1–20.

[39] P. Velardi, et al., Evaluation of Ontolearn, a methodology for automatic learning of domain ontologies, Ontology Learning from Text: Methods, Evaluation and Applications, 2005. 92–106.

[40] M. Gruninger, M.S. Fox, Methodology for the design and evaluation of ontologies, Proceedings of The Workshop On Basic Ontological Issues In Knowledge Sharing, IJCAI, 1995.

[41] A. Gomez-Perez, Ontology evaluation, in: S. Staab, R. Studer (Eds.), Handbook on Ontologies, Springer, 2004, pp. 251–274.

![](/api/attachments/NRJ8D628/fulltext/images/b29fadb70be66b40f8550b21cd9098aaa6b5db7e69f0f7035ff56939349022a8.jpg)  
Dr. Daning Hu is an Assistant Professor of the Department of Informatics at University of Zurich and Head of the Business Intelligence Research Group. He holds his Ph.D. degree in Management Information Systems (minor in Finance) from the University of Arizona, and B.S. degree in Computer Science from Zhejiang University. His research goal is to derive analytical and empirical insights from the analyses of various real-world networks such as organization networks, communication networks, and social networks. Based on such insights, he aims to develop network-based business intelligence techniques and information systems for supporting decision making in various application domains. He has published in MIS Quarterly, Decision Support Systems, Journal of the Association for Information Systems, Journal

of the American Society for Information Science and Technology, and Information Systems Frontiers.

![](/api/attachments/NRJ8D628/fulltext/images/6f24a9d733a3adda7faa7e7d34abcbefbccf7e32ac9df53a897bf85dc39c8862.jpg)

Jiaqi Yan is a postdoctoral research fellow in the Department of Informatics at University of Zurich. He got his Ph.D. degree in Management Science and Engineering from the University of Science and Technology of China, and a joint Ph.D. degree in Information Systems from the City University of Hong Kong. His research interests focus on business intelligence, risk management and business process management. He has published papers in Decision Support Systems, Journal of Information Systems, and Expert Systems with Applicants.

Please cite this article as: D. Hu, et al., Ontology-based scenario modeling and analysis for bank stress testing, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.08.009

D. Hu et al. / Decision Support Systems xxx (2013) xxx–xxx

![](/api/attachments/NRJ8D628/fulltext/images/4df9f0c00efd1075ddbb7040d3f163e75ba4ff2ff48b19238ee9d85d5f8c8be2.jpg)

J. Leon Zhao is Head and Chair Professor in Information Systems, City University of Hong Kong. He was Interim Head and Eller Professor in the Department of Management Information Systems, University of Arizona, previously. He holds Ph.D. and M.S. degrees from the Haas School of Business, UC Berkeley, M.S. in Engineering from UC Davis, and B.S. from Beijing Institute of Agricultural Mechanization. Leon's research has been supported by NSF, SAP, and other funding agencies. Leon has served as associate editor of Information Systems Research, ACM Transactions on MIS, IEEE Transactions on Services Computing, Decision Support Systems, Electronic Commerce Research and Applications, among other journals. He has co-edited more than ten special issues in various IS journals including Decision Support Systems and Information Systems Frontiers and has chaired numerous international conferences including the 2010 Conference on Design Science Research, the 2009 IEEE Conference on Services Computing, the 2008 IEEE Symposium on Advanced Management of Information for Globalized Enterprises, the 2007 China Summer Workshop on Information Management, the 2006 IEEE Conference on Services Computing, among others. He received an IBM Faculty Award in 2005 for his work in business process management and services computing and was awarded Chang Jiang Scholar Chair Professorship at Tsinghua University by the Ministry of Education of China in 2009.

![](/api/attachments/NRJ8D628/fulltext/images/7ee2fd35b062b0f265db7fb333d9a19386e3d087cc6db35d97b80e5d21a0067c.jpg)

Zhimin Hua is a doctoral student in the Department of Information Systems, College of Business, at the City University of Hong Kong. He received a B.S. in Computer Science from the University of Electronic Science and Technology of China. His research interests include Business Intelligence, Financial In formation Services, Business Process Management, etc. His work has appeared in ICIS, WITS, etc. He is a student member of the INFORMS and AIS.
