---
otero_id: 10396
otero_key: "Y48CWTV3"
title: "Towards a multi-dimensional project Performance Measurement System"
authors: "Matthieu Lauras; Guillaume Marques; Didier Gourc"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.09.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a multi-dimensional project Performance Measurement System

Matthieu Lauras <sup>a,b</sup>, Guillaume Marques <sup>a,</sup>⁎, Didier Gourc <sup>a</sup>

<sup>a</sup> Université Toulouse / Mines Albi / Centre Génie Industriel, Campus Jarlard, Route de Teillet, 81013 Albi, France

<sup>b</sup> Toulouse Business School/Department of Industrial Organisation, Logistics and Technology, 20 Boulevard Lascrosses, BP 7010, 31068 Toulouse Cedex 7, France

## a r t i c l e i n f o

Article history: Received 23 June 2008 Received in revised form 10 September 2009 Accepted 17 September 2009 Available online 25 September 2009

Keywords: Project performance Performance Measurement System Project management Multiple criteria analysis Decision Support Systems

## a b s t r a c t

This paper discusses the dif<sup>fi</sup>culty of controlling a complex project caused by the great number of performance indicators. The problem studied is how to allow project managers to better control the performance of their projects. From a literature review we noted several critical aspects to this problem: there are many dimensions for evaluating project performance (cost, time, quality, risk, etc.); performance factors should be able to be relevantly aggregated for controlling the project, but no formalized tool exists to do this. We suggest a method to facilitate project performance analysis via a multi-criteria approach. The method focuses on three particular axes for the analysis of project performance: project task, performance indicator categories, and a breakdown of the performance triptych (Effectiveness, Ef<sup>fi</sup>ciency, Relevance). Finally, the MACBETH method is used to aggregate performance expressions. An application case study examining a real project management situation is included to illustrate the implementation

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

More and more information with less and less time! This could be a description of everyday decision-making in a project context. Project management has become very popular [20] and we <sup>fi</sup>nd many methods and good practices which promote particular visions of project management. Most of these methods are based on performance measurements at the operational level of the project: the tasks. Performance Measurement Systems (PMS) are the instruments that support decision-making. From a global point of view, a PMS can be seen as a multi-criteria instrument made of performance expressions [4]. As a project manager, you have to monitor the performance of your project by using a large quantity of information and integrating the vision of senior management. But can this be achieved in a very complex project context? Arnott and Pervan [1] present Decision support Systems as an area that is focused on supporting and improving managerial decision-making. Consequently, which decision-assisting tool or method do you use to facilitate and improve decision-making? In other words, the project manager is at the point where many management constraints converge:

– from senior management;

– from the project complexity and the quantity of information stemming from it;

– from her/his own management policy;

How can s/he aggregate all of them? How can this aggregation help her/him to be ef<sup>fi</sup>cient and relevant in her/his corrective actions?

Furthermore, a project is intrinsically unique and subject to its environment [35]. Under these conditions, to give a clear and accurate de<sup>fi</sup>nition of the performance of your project is probably one of the most important actions you can take to ensure success. Indeed, you have to clarify what are the essential bene<sup>fi</sup>ts that the project will deliver in the minds of the project team and service managers. The clearer the target, the more likely you are to hit it.

But how to de<sup>fi</sup>ne this target? And how to be sure that you control the project performance according to this target?

PMS is a topic which is often discussed but rarely de<sup>fi</sup>ned, and which traditionally adopts a narrow or uni-dimensional focus [25]. In fact, for many project managers, the Iron Triangle—Time, Cost and Quality—de<sup>fi</sup>nes the performance dimensions of a project. According to this idea, many project managers only use these three criteria. However, other success criteria should be considered in order to incorporate local project speci<sup>fi</sup>cities [2].

Consequently, the purpose of this paper is to:

– propose a project performance method suitable for the design of a Project Performance Measurement System (PPMS) that can consolidate all good practices in terms of project performance;

– propose a way to aggregate multi-criteria performance measurements.

The paper comprises four main sections: <sup>fi</sup>rst, a bibliographical study to identify good practices in terms of performance management in a project context. Second, the problem under study is described on the basis of this literature review. Third, our project performance method is presented and implemented in a PPMS. Fourth, a real-life case study based on the MACBETH method is developed to illustrate our proposition. Finally, some conclusions and areas for discussions are presented.

## 2. Literature review

Performance evaluation is used either to design/modify a system, or to control an existing system. It is an essential element of effective planning and control as well as decision-making [3]. We speak of a priori or a posteriori evaluation respectively, either to help decisionmaking or to evaluate the quality of the most recent decisions. In this study, we focus on an a posteriori performance evaluation of a particular system, a project in this case.

## 2.1. Dimensions of project performance

A project is unique and limited over time. Projects have a unique content and unique scope. Each project differs from others regarding its goals, activities (tasks), resources and deliverables. According to Yu Angus et al. [34], different project de<sup>fi</sup>nitions might warrant different success criteria. In other words, the Iron Triangle is not suf<sup>fi</sup>cient to cover all the particularities of each project. So, each project manager has to develop her/his range of Key Performance Indicators (KPI). But can the relevance of these choices be certi<sup>fi</sup>ed?

According to Swink et al. [31], the effectiveness of a project is the degree to which the managers of the project make use of techniques which improve the ef<sup>fi</sup>ciency of project execution. Critical success factors can be described as characteristics, conditions, or variables that can have a signi<sup>fi</sup>cant impact on the success of the project when properly sustained, maintained or managed [23]. Dweiri and Kablan [11] claim that standard performance management metrics and tools impact standard performance management methodology, which in turn in<sup>fl</sup>uence project success. Atkinson [2] shows that using the Iron Triangle as the criterion of success is not optimal. Something is missing; the system is not as good as it could be. Many authors, such as Grey [14] or Pritchard [27], advocate using a risk assessment report to complete a project performance management system. This report provides the information needed to start any actions for the correction of potential problems.

Dweiri and Kablan [11] show that project management activities using only time, cost or quality measures may fall through the gaps. Consequently, areas covered by performance management must be as complete as possible. The PM Body of Knowledge proposes nine essential knowledge and management areas to describe project management [26]. A complete project management dimension is de<sup>fi</sup>ned: Integration, Scope, Time, Cost, Quality, Human Resources, Communication, Risks and Procurement.

## 2.2. Aggregation and stakeholder needs in terms of project performance

Each KPI should be examined separately and then in related groups of indicators [27]. Analysts such as the project manager, task leader or senior manager must simultaneously consider all these factors.

## 2.2.1. Disparate measurement systems

Dweiri and Kablan [11] note that disparate measurement systems may result in super<sup>fl</sup>uous and incompatible performance measurement frameworks. There is a need for project managers to quantify performance as a whole and to be able to drill down to different measurements at different levels of detail and time. Consequently, any project performance evaluation supposes the need to analyze the measurements taken, whatever the dimensions. It is a question of considering the impact of each component of a performance.

Some authors, such as Xiaoyi Dai and Wells [33], develop a consensus for determining project failure rather than considering the multiple dimensions for evaluating project performance. As the majority of existing project performance measurement tools focus on <sup>fi</sup>nancial aspects, such as return on investment and pro<sup>fi</sup>t per unit, they argued that <sup>fi</sup>nancial parameters are useful, but there are inadequacies, such as lagging metrics, a lack of strategic focus, and a failure to provide data on quality, relationships and the environment [8]. In addition they do not permit the production of aggregated indicators to control projects. In fact, as Clivillé [9] points out, as soon as managers use more than one KPI, problems of comparison and aggregation of the performance expressions will exist. Thus, they have to ensure that:

– expressions are interpretable in the same way by the entire control system: commensurability;

– mathematical operations carried out on these expressions are coherent: meaningfulness.

## 2.2.2. Different views on project performance

Rosenau and Githens [28] emphasize the trend for project managers to try to circulate a single report between many different recipients. They explain that this is a mistake as senior management will look for summary status and forecast data, whereas middle managers will look for more speci<sup>fi</sup>c and tailored information on operational details. They stress the necessity to have a system of KPIs which allows visibility of performance at different levels as well as ensuring coherence between these views. Milosevic and Patanakul [23] af<sup>fi</sup>rm that measures of project success need to include the diversity of stakeholders' interests. This is the principal value of indicator aggregation: to provide an immediate and global overview of the project interpretable by an entity not conversant with the details of the activities.

## 2.3. Project performance analysis as a business process analysis

The International Organization for Standardization [18] de<sup>fi</sup>nes a project as “a unique process, consisting of a set of coordinated and controlled activities with start and <sup>fi</sup>nish dates, undertaken to achieve an objective conforming to speci<sup>fi</sup>c requirements.” This de<sup>fi</sup>nition assimilates projects to business processes. From this standpoint we can associate Project Management with Business Process Management (BPM). This allows standard business process Performance Measurement Systems (PMS) to be extended to project management.

A large number of these standards relate to measures needed to capture the relevant characteristics of activities that compose business processes. We can cite the Holistic Process Performance Measurement System, the Integrated Dynamic Performance Measurement System, Earned Value Added, the Fraunhofer approach or, more basically, the Activity Based Costing/Management and the Supply Chain Operations Reference model [6]. According to this idea, project tasks should be assimilated as business process activities. Each task can be described accordingly as input(s), output(s), resource(s) and control(s).

Finally, PMS can be de<sup>fi</sup>ned as the set of metrics, or performance measures, used to quantify both the ef<sup>fi</sup>ciency and the effectiveness of actions [24]. Performance evaluation supposes the need for tools to analyze the measurements taken according to these two dimensions of ef<sup>fi</sup>ciency and effectiveness. It is a question of considering the impact of each component of the performance. Basically, BPM analysis adds a third component: Relevance. Performance analysis could then be made with an approach based on Relevance, Effectiveness and Ef<sup>fi</sup>ciency (REE) [19]. REE compares the Objectives–Results– Resources of a business activity (in our case, a project task), and comprises a triptych that aims to describe an activity's performance (Fig. 1). Effectiveness measures whether the results of the activity meet the objectives. Ef<sup>fi</sup>ciency expresses whether the resources were well used to attain the results. Relevance measures the adequacy of the means to the objectives.

![](/api/attachments/Y48CWTV3/fulltext/images/23c1b184d9a1743edab7d76c8477fb184c3962d196ef25b277c72c425475d04c.jpg)  
Fig. 1. Performance triptych

## 2.4. Decision making (DM) and Multi-Criteria Decision-Making (MCDM)

Korhonen [20] argues that Multi-criteria Decision-Making (MCDM) is to make a choice from a countable set of countable or uncountable alternatives using 2 or more criteria. Roy [30] has de<sup>fi</sup>ned a framework to describe the decision aiding. He proposes a four-step methodology. The <sup>fi</sup>rst one (level I) de<sup>fi</sup>nes the object of the decision and the type of problematic. There are four reference problematics: choice (choose the best action), sorting (sort action according to norms), ranking (rank actions in order of decreasing preference) and description problematics. The level II allows the consequences to be analyzed and criteria to be developed in a consistent family. In the level III, the decision-maker's preferences are modeled and the performance assessments are aggregated. Finally, the level IV investigates and develops the recommendation. Globally, levels I, II and IV are similar from an author to the other. However, they differ about the level III: the aggregation methods. Chen et al. [7] consider Multi-Criteria Decision Analysis (MCDA) as a consequence-based preference aggregation problem Multi-Criteria support systems allow us to analyze multiple criteria and incorporate the decision-maker's preferences for these criteria into the analysis [13,20]. In other words, aggregation models enable us to capture the notion of priorities in the decision-maker's strategy [10]. Many methods have been developed and analyzed to date. For more detailed information about these methods we refer to Figueira et al. [12] who have recently proposed a large survey about multiple criteria decision analysis.

In the nutshell, we <sup>fi</sup>nd three different approaches (called operational approaches by Roy [30]):

– based on a single synthesizing criterion without incomparabilities (Operational approach 1). Associated methods are weight sum, Multi-Attribute Utility Theory (MAUT), MACBETH (Measuring Attractiveness by a Categorical Based Evaluation TecHnique [5]), Analytical Hierarchy Process (AHP), etc. In the project context, for example, Dweiri and Kablan [11] and Hwang [16] propose a fuzzy decision-making system to quantify a global project management internal ef<sup>fi</sup>ciency.

– based on synthesis by outranking with incomparabilities (Operational Approach 2). Associated methods are ELECTRE (I, II, III, IV), PROMETHE (I and II), etc.

– based on interactive local judgments with trial and error iterations (Operational Approach 3).

## 3. Problem under study

In this paper, we address the problem of modeling project performance in order to be able to design a relevant Project Performance Management System (PPMS). The quantity and diversity of academic research testify to the dif<sup>fi</sup>culty of building a universal model to tackle the question of project performance. Nevertheless, several good practices for the design of a PPMS can be extracted from the review of the literature (Fig. 2):

– project performance has to take account of the uniqueness of each project;

– project performance must consider some universal dimensions of project management, for instance measuring performance within the nine knowledge areas de<sup>fi</sup>ned by the PMI.

Finally, this PPMS has to permit an analysis of the performance in terms of the Relevance, Effectiveness and Ef<sup>fi</sup>ciency triptych.

Moreover, the bibliography study has shown that project performance has to be adapted to the different project stakeholders. Consequently, the PPMS must allow KPIs to be aggregated, regardless of their dimension.

## 4. Proposed method: Project performance cube—p<sup>cubed</sup>

## 4.1. Project performance uniqueness: Task control

The <sup>fi</sup>rst dimension focuses on the main phase of breaking down the project tasks. This is based on work packages de<sup>fi</sup>ned by the Work Breakdown Structure (WBS) of the project. Work packages represent the fundamental units of the project that the project manager has to manage. Rosenau and Githens [28] stress the fact that the size of a work package depends on the control needs. So, this dimension of the analysis could be broken down into several detail levels, from main activities to elementary tasks. In a very complex project we could also imagine only analyzing tasks on the critical path (avoiding too many measures to control).

4.2. Project performance universality: PMI knowledge areas and BPM analysis axes

## 4.2.1. Multi-dimensional project management

According to Westerveld [32], the PMI's de<sup>fi</sup>nition of project management is unclear and it is dif<sup>fi</sup>cult to link areas and project situations. However, if we consider the project as a business process as de<sup>fi</sup>ned by the ISO 10006:2003 standard, it becomes possible to break the project into activities (tasks). We could then apply the PMI's nine knowledge areas to each task. The nine areas appear as nine points of view we take of the activity being considered. In our case, we could apply this breakdown to tasks which appear in the project WBS. In other words, we can associate nine characters to each task. These nine points of views de<sup>fi</sup>ne a set that we call character set C.

![](/api/attachments/Y48CWTV3/fulltext/images/0b992fdb7fa8d760affd40b2f07dfe9253179d67d8bb2de38a83aa999a77fd20.jpg)  
Fig. 2. Good practices for the design of a PPMS

By de<sup>fi</sup>nition, this KPI framework allows all aspects of project management to be reached. Of course, we should underline that independence between each character is not total. For example, the delay could have cost consequences. However, this additional cost imputable to the delay has to be considerate from the <sup>fi</sup>nancial management point of view. The project is doubly impacted: by the delay and by the additional cost. Consequently, in this study, the potential partial interdependence between characters does not modify the assessment

Furthermore, the aim is not to produce a single reduced evaluation of the project, but to operationally control it. This distinction refers to Hansen and Riis [15] who oppose the two fundamentally different approaches: the aggregate approach with long term and strategic implications and the composite (partial) approach with an operational and applicational point of view. If our evaluation is exclusively time- and cost-centered (aggregate), we cannot immediately know the origin of a deviation in the performance level. From an operational point of view, measures are easily interpretable [32]. Having a complete vision of all aspects of the project allows faster and better targeted corrective actions. In the particular case of resource leveraging, Martinez et al. [22] explain that this demands a global vision of the different alternatives to make milestones both feasible and near optimal from the performance standpoint.

## 4.2.2. Performance analysis

We de<sup>fi</sup>ne:

– D, the set of project review dates. There are R review dates during the project. One review date, t, belongs to $D = [ 1 ; R ] ( R \in \mathbb { N } ^ { * } )$ 1

– C, the set of the characters (time, cost, etc.). We can analyze the performance of 1 to m characters. One character, I, belongs to $C =$ [1; m] $( m \in \mathbb { N } ^ { * } )$

– T, the set of the tasks. There are n tracked tasks in the project. One task, k, belongs to T=[1; n] (n∈ℕ<sup>\*</sup>).

Each project task can be modeled as an activity with its inputs, outputs, resources and controls. These tasks represent the operational and support processes of a project. At a given $t \in D ,$ , we can analyze the task $k \in T$ with the character $i \in C \colon$

$$
\begin{array}{l}D \times T \times C \rightarrow K P I\\\text { date } (t), \text { task } (k), \text { character } (i) \mapsto S (t, k, i) = \{E _ {\mathrm{ft}}; E _ {\mathrm{fc}}; R _ {\mathrm{vc}} \}\end{array}
$$

Effectiveness $\left( E _ { \mathrm { f t } } \right)$ , Ef<sup>fi</sup>ciency $\left( E _ { \mathrm { f c } } \right)$ , Relevance $( R _ { \mathrm { v c } } )$ are not obligatory quantitative values. They could be qualitative or even equal to an empty set. Another function $E _ { \mathrm { x t } }$ can be de<sup>fi</sup>ned. This allows one particular element to be extracted from the triptych:

$$
K P I \times \{1, 2, 3 \} \rightarrow E
$$

$$
S (t, k, i) \times j \mapsto E _ {\mathrm{xt}} (S, j) = \left\{ \begin{array}{l} E _ {\mathrm{ft}} \text {if} j = 1 \\ E _ {\mathrm{fc}} \text {if} j = 2 \\ R _ {\mathrm{vc}} \text {if} j = 3 \end{array} \right.
$$

The task $k ^ { i }$ is then observed using the three views of the triptych {Relevance; Effectiveness; Ef<sup>fi</sup>ciency}. For one j, i.e. one view $( j \in [ 1 ; 2 ;$ 3]), the manager de<sup>fi</sup>nes 0 to $L ^ { k i j }$ metrics to measure the performance. $L ^ { \hat { k i j } }$ is a parameter previously de<sup>fi</sup>ned for all kij. For each j, i.e., each view, we have a vector with $L ^ { k i j } \times \mathbf { \mathcal { I } }$ 1 dimension. This is resumed in Fig. 3.

$$
\begin{array}{l}E \times \mathrm{N} \rightarrow L\\E _ {\mathrm{xt}} (S, j), l \mapsto E _ {\mathrm{xt}} ^ {l} (S, j)\end{array}
$$

One KPI is de<sup>fi</sup>ned by the triptych {Relevance; Effectiveness; Ef<sup>fi</sup>ciency}. According to the way that each view of triptych is built, one KPI will not be a $1 \times 3$ dimension matrix but a Max $L ^ { k i j } \times 3$ dimension matrix, built as shown in Fig. 4.

$\mathbf { Z } _ { 1 } , \mathbf { Z } _ { 2 }$ and ${ \bf Z } _ { 3 }$ are null vectors used to adapt an entire column to the dimension of the matrix. Their dimensions are de<sup>fi</sup>ned as followed:

$$
\begin{array}{r l} & {- \dim \mathbf {Z} _ {1} = (\max L ^ {k i j} - L ^ {k i 1}) \times 1} \\ & {- \dim \mathbf {Z} _ {2} = (\max L ^ {k i j} - L ^ {k i 2}) \times 1} \\ & {- \dim \mathbf {Z} _ {3} = (\max L ^ {k i j} - L ^ {k i 3}) \times 1} \end{array}
$$

## 4.3. The project performance cube: $P ^ { C U B E D }$

All the performance measures of a project can be arranged into a cube—called P<sup>CUBED</sup>—de<sup>fi</sup>ned by the three dimensions cited previously [21]. A cell of this cube includes the KPIs of a given project activity (task), considering a given character (knowledge area), and the same element of the triptych. As an example, we can consider a cell that

![](/api/attachments/Y48CWTV3/fulltext/images/e43fe048493eefad4984f76fe65027d04d73e300cce7befdde35419f9b4a6723.jpg)  
Fig. 3. Project task model.

$$
S (t, k, i) = \left( \begin{array}{c c c} E x t (S, 1) & E x t (S, 2) & E x t (S, 3) \\ Z _ {1} ^ {k i} & Z _ {2} ^ {k i} & Z _ {3} ^ {k i} \end{array} \right) _ {t} = \left( \begin{array}{c c c} \binom {\circ} {\cdot} & \binom {\circ} {\cdot} & \binom {\circ} {\cdot} \\ \binom {\cdot} {\cdot} & \binom {\cdot} {\cdot} & \binom {\cdot} {\cdot} \\ \binom {\cdot} {\circ} & \binom {\circ} {\circ} & \binom {\circ} {\circ} \\ \binom {0} {\cdot} & \binom {0} {\cdot} & \binom {0} {\cdot} \\ \binom {\cdot} {\cdot} & \binom {\cdot} {\cdot} & \binom {0} {\cdot} \\ \binom {0} {0} & \binom {0} {j = 1} & \binom {0} {j = 2} \end{array} \right) _ {t}
$$

Fig. 4. KPI matrix.

corresponds to the Task “To Design product A”, considering the “Time” character and the “effectiveness” in the triptych (Fig. 5).

Let:

– i =Characters, [1; m] (m ≤ 9) (m =number of characters)

– j = Elements of triptych, [1,2,3] (for $E _ { \mathrm { f t } } , E _ { \mathrm { f c } } , R _ { \mathrm { v c } } )$

– k=project activities or tasks [1; n] (n =number of tasks)

– l = number of the value of the elementary component of a KPI $[ 0 ; L ^ { k i j } ] \ ( L ^ { k i j } \in \mathbb { N } . )$

– y<sub>ijkl</sub>=measure associated to a elementary component of a KPI – X=a KPI on a cube's face.

Implementation of the performance cube method comprises three main steps: <sup>fi</sup>rst, scaling the cube to the project dimension. This step de<sup>fi</sup>nes the task dimension; Secondly, parameterizing the cube to re<sup>fl</sup>ect the performance management choice. This step adjusts the KPI categories dimension. We have to consider that the de<sup>fi</sup>nition of the categories depends on the point of view chosen; <sup>fi</sup>nally, using the cube from the starting date of the project.

## 4.4. Project performance control with the $P ^ { C U B E D } .$ : Aggregation process

As explained previously, the $\mathrm { P ^ { C U B E D } }$ objective consists in supporting decision-makers in terms of project performance control. To achieve this, we have stressed the necessity to produce different analysis reports that aid the decision-maker in proposing an ordered list of possible actions. Consequently, in our study we are confronted to a “ranking problematic” like de<sup>fi</sup>ned by Roy [30] and presented in Section 2.4. Furthermore, these reports include different points of view and levels of granularity. The multi-dimensional property of the model allows this.

## 4.4.1. P<sup>CUBED</sup> aggregation structures

KPIs can be aggregated from different angles. In fact, each project stakeholder should be able to interpret the model from her/his point of view. For example, senior management should be interested in greater aggregation (for instance, a unique value for judging project performance) than the project manager, who will concentrate her/his analysis on task or character performance. Consequently, aggregation methodology must be adapted to the different actors' points of view. According to previously cited constraints, we have constructed three different ways of aggregating the cube values (Fig. 6):

![](/api/attachments/Y48CWTV3/fulltext/images/866268eddd01ed1dff537b39bb3bd1c026983945ded591d223ad767d924c0651.jpg)  
Fig. 5. Construction principle of the performance cube.

![](/api/attachments/Y48CWTV3/fulltext/images/6c4aff43d1f82ea18add05af1dd973fc97f83217f741ab5950e0523787f60523.jpg)

Triptych oriented  
![](/api/attachments/Y48CWTV3/fulltext/images/a0691010b8423926630caac798bfccd60e6c0b6577e4699c6bc113f80182abe6.jpg)  
Fig. 6. $\mathrm { P ^ { C U B E D } }$ aggregation tree structures.

– task-oriented;

– character-oriented (9 PMI areas);

– triptych-oriented $\big ( E _ { \mathrm { f t } } , E _ { \mathrm { f c } } , R _ { \mathrm { v c } } \big ) .$

T1,…, Tn are project tasks. $\mathrm { C 1 } , . . . , \mathrm { C 9 }$ are the nine characters. In Table 1 these three aggregation orientations are not of equal interest to all project members.

## 4.4.2. Commensurability and meaningfulness

Each KPI has its own metrics and measures. But, as discussed in Section 2.2.1, we have to consider the commensurability and the meaningfulness of these three dimensions. In an ideal case, performance expressions should be de<sup>fi</sup>ned without any dimension (units) to ensure commensurability. The calculated values are standardized in order to be comparable.

## 4.4.3. A first and simple aggregation model

To facilitate management, we suggest <sup>fi</sup>rst computing mean values that can be compared and that alarm levels can be de<sup>fi</sup>ned for. If we take a non-linear aggregation operator, we only obtain a relative comparison between values (and not an absolute comparison). Since the physical direction of aggregate values is important for project managers, we propose using a simple means operator where the:

• mean project activity indicator is the mean value of all the categories of indicators of a project activity for a given component of the performance triptych. This allows de<sup>fi</sup>nition of the visible face of the cube that aggregates all the categories of measures for a given project activity or task: cf. formula (1);

Intended aggregation models.

<table><tr><td rowspan="2">Orientation</td><td colspan="3">Intended for</td></tr><tr><td>Task leader</td><td>Project manager</td><td>Senior manager</td></tr><tr><td>Task</td><td>++</td><td>++</td><td>-</td></tr><tr><td>Character</td><td>+</td><td>++</td><td>+</td></tr><tr><td>Triptych</td><td>-</td><td>+</td><td>++</td></tr></table>

• mean indicator type is the mean value of all the activities of this type of indicator for a given component of the performance triptych. This allows de<sup>fi</sup>nition of the visible face of the cube that aggregates all the measures for a given category of performance indicator (cost, time, risk, quality, etc.): cf. formula (2);

• mean performance view is the mean value of all views of the performance triptych for a given task and a given type of indicator (character). This allows de<sup>fi</sup>nition of the visible face of the cube that aggregates all the measures for a given view of the performance triptych: cf. formula (3).

$$
X _ {i j.} = \frac {\sum_ {k} \sum_ {l = 1} ^ {L ^ {k i j}} y _ {i j k l}}{\sum_ {k} L ^ {k i j}}\tag{1}
$$

$$
X _ {j k} = \frac {\sum_ {i} \sum_ {l = 1} ^ {L ^ {k i j}} y _ {i j k l}}{\sum_ {i} L ^ {k i j}}\tag{2}
$$

$$
X _ {i. k} = \frac {\sum_ {j} \sum_ {l = 1} ^ {L ^ {k i j}} y _ {i j k l}}{\sum_ {j} L ^ {k i j}}\tag{3}
$$

Note that not all cells of the cube contain the same number of indicators. It therefore follows that a project activity or a performance indicator category which carries many indicators will weigh more in the <sup>fi</sup>nal evaluation. Consequently, means per line or column are not necessarily homogeneous; the total of project activities and the total of categories of performance indicators are not identical. A solution for avoiding this problem consists of aggregating using a mean operation at the cell level. Hence we have to validate that the elementary performance indicators authorize compensation at the cell level: i.e. we consider in an identical way a situation in which the value of a cell's indicator is 50, and a situation in which the value a cell's four indicators are 100, 100, 0 and 0. Clearly not all projects meet this condition. Nevertheless, when this hypothesis is validated then a cell of the cube will take the value expressed in the formula (4), and the faces of the cube will take the value expressed in the formulae (5), (6) and (7).

$$
x _ {i j k} = \sum_ {l = 1} ^ {L ^ {k i j}} \frac {y _ {i j k l}}{L ^ {k i j}}\tag{4}
$$

Table 2

$$
X _ {. j k} = \sum_ {i} \frac {x _ {i j k}}{m}\tag{5}
$$

$$
X _ {i j.} = \sum_ {k} \frac {x _ {i j k}}{n}\tag{6}
$$

$$
X _ {i. k} = \sum_ {j} \frac {x _ {i j k}}{3}\tag{7}
$$

The implementation of one of the aggregation methods is subject to constraints. It should be noted that some limits appear on the aggregation criteria of the individual measures. Indeed, all project tasks and, reciprocally, all categories of KPI have the same weight in the <sup>fi</sup>nal result. It is obvious that a project manager will lend more or less importance to such a task as a function of the aims of the global project, of the project success criteria (maximum date, budget, etc.) or according to her/his own personal preferences. Consequently, in the next part we consider an advanced aggregation that integrates the point of view of the decision-maker.

## 4.4.4. KPI weighting for an advanced approach to cube analysis

As argues Roy [30], the choice of aggregation approach is often dif<sup>fi</sup>cult and we have no theoretical rules that allow the aggregation approach to be selected. Outranking and interactive approaches (Operational Approaches 2 and 3) are more recent and so less explored and used in the reality. Furthermore, outranking methods do not always allow to discriminate the set of possible action. Even if the default of single criterion approach is the dif<sup>fi</sup>culty to validate the choice of the aggregation operator, in this study, we seek to propose an ordered list of possible actions without incomparabilities. For example, how can a project manager concentrate his resources on one task rather than another if he is not able to compare their performance? Furthermore, implementing outranking methods requires more expert intervention and if quantity of required information is often underlined to describe the dif<sup>fi</sup>culties in applying a single criterion approach, in the project context, information is available. Consequently, here, we stay in the Operational Approach 1, i.e. the approach based on a single synthesizing criterion.

As the last part shows, the mean value does not allow the complexity of decision-maker's points of view to be integrated. AHP method could be better about this point but coherence problem between the scales of criteria could appear because of the structure of the preference scale. The ratio scale used in AHP could be manipulated with more dif<sup>fi</sup>culties in the context of project management. Consequently, we prefer methods based on the interval scale to express decision-maker's opinion. Furthermore, we want to achieve greater relevance by weighting each elementary criterion. But, in a complex project (with many tasks and categories of indicators) it is quite dif<sup>fi</sup>cult to quantify the exact weight of each category of performance indicator or the exact weight of each project task. With the orientations previously de<sup>fi</sup>ned, we have:

– task-oriented: 9×3=27 criteria to compare;

– character-oriented: T×3 criteria to compare, where T is the number of tasks;

– triptych-oriented: T×9 criteria to compare.

It is increasingly dif<sup>fi</sup>cult to attribute a weight to each criterion. In fact, it is proportional to the project complexity. However, it could be easier to evaluate the relative position between the two of them.

We intend using a MACBETH approach to weight the aggregation process. MACBETH employs a non-numerical interactive questioning procedure that compares two stimuli at the same time, requesting only a qualitative judgment about their difference of attractiveness [35]. As the answers are given, the consistency is veri<sup>fi</sup>ed, and a numerical scale (interval scale) that is representative of the decisionmaker's judgments is subsequently generated and discussed. An overview and some applications of MACBETH are presented, for instance, by Bana e Costa and Chagas [4], Roubens et al. [29], and on www.m-macbeth.com.

## 4.5. Global step for implementing $P ^ { C U B E D }$

In summary, we suggest adopting the following <sup>fi</sup>ve steps for using the $\mathsf { P } ^ { \mathrm { C U B E D } }$ proposition:

1. scale the cube;

2. design KPIs;

3. weight KPIs;

4. aggregate Project Performance;

5. analyze performance and make decisions.

## 5. Case study: A project for the manufacture of landing gear doors

In this section, we propose implementing our P<sup>CUBED</sup> proposition by controlling the performance of a product development project.

## 5.1. Project overview

Let us consider a 2nd tier supplier to the aeronautics sector. This supplier produces composite equipment for aircraft manufacturers. The project examined deals with “study and industrialization” phases of new composite landing gear doors.

## 5.2. Step 1: Scale the cube

We use the Work Breakdown Structure (extract in Table 2) to identify the project tasks. This allows us to deduce the useful dimensions of the cube. Here, they are numbered from 1 to 55. The numbering does not differentiate between simple and summary tasks. Without these summary tasks we have 45 simple tasks. Concerning the knowledge areas, we have chosen to focus the project performance analysis only on the dimensions of Time, Cost, Quality and Risk. In addition, ten review dates are programmed, labeled D1, …, D10. We have monitored this project in its entirety. However, due to space restrictions we have only developed a performance analysis of review date D6. Using the letter notation cited above, the parameters of the P<sup>CUBED</sup> are for this project:

– n= 45;

$$
- R = 1 0.
$$

Extract of the WBS for the Landing Gear Doors Project.

<table><tr><td colspan="2">Composites Landing Gear development project</td></tr><tr><td>2</td><td>Initialization step</td></tr><tr><td>3</td><td>Project organization specification</td></tr><tr><td>4</td><td>Contract negotiation</td></tr><tr><td>5</td><td>Contract signed</td></tr><tr><td>6</td><td>Research step</td></tr><tr><td>7</td><td>Preliminary study</td></tr><tr><td>8</td><td>Development</td></tr><tr><td>9</td><td>Customer agreement</td></tr><tr><td>10</td><td>Plans and definition bundle reception</td></tr><tr><td>11</td><td>Industrialization step</td></tr><tr><td>12</td><td>Moulding equipment fabrication</td></tr><tr><td>13</td><td>Specifications drafting</td></tr><tr><td>14</td><td>Specifications validation</td></tr><tr><td>15</td><td>Industrialization study</td></tr></table>

![](/api/attachments/Y48CWTV3/fulltext/images/ff13ff128516fafdbabd9c14f526938a7e64acc44c7e6bd92145afde421aef4c.jpg)  
Fig. 7. MACBETH procedure (from Clivillé et al. [10]).

## 5.3. Step 2: KPI design

## 5.3.1. MACBETH design

During this Step we enter the MACBETH procedure. According to the four main steps of this procedure described by Clivillié et al. [10] (Fig. 7), we begin by identifying criteria and options. Criteria and options de<sup>fi</sup>ned in MACBETH differ according to orientation of the study. Table 3 resumes this difference using the letter notation cited above.

We shall now continue with an explanation of the task-oriented case. Only the results will be given for the character and triptych orientations.

The target is to compare many options according to the criteria we have de<sup>fi</sup>ned. At a given t, we identify some tasks which the project manager wants to analyze in order to highlight particular parts of the project which are in dif<sup>fi</sup>culty. We introduce these n tasks into the MACBETH software. We then create the value tree (Fig. 8) in which we identify our criteria, i.e. the i–j character pairing and triptych views.

As previously stated, values associated to the criteria could be quantitative or qualitative. Furthermore, we seek to aggregate these criteria in order to obtain a ranking for the options. MACBETH, therefore, starts by creating a value scale for each criterion. The principle is to translate human expertise concerning given situations into quanti<sup>fi</sup>ed elementary performance expressions, along an interval scale [10]. A criteria, r, could have many values. These different possibilities are different situations: $S _ { 1 } , \ S _ { 2 } , . . . , \ S _ { \nu } \ ( \nu \in \mathbb { N } )$ MACBETH introduces the notion of the degree of strength of attractiveness between two situations denoted by h; h can take seven values, from 0 for no strength, to 6 for extreme strength.

Table 3 MACBETH design.

<table><tr><td>Orientation of the analysis</td><td>Options</td><td>Criteria (r)</td><td>Number of criteria</td></tr><tr><td>Task</td><td>Task (k)</td><td>ij</td><td>m×3</td></tr><tr><td>Character</td><td>Character (i)</td><td>kj</td><td>n×3</td></tr><tr><td>Triptych</td><td>Views of triptych (j)</td><td>ki</td><td>n×m</td></tr></table>

![](/api/attachments/Y48CWTV3/fulltext/images/a0f5e53fadc926dd8a6f219892d9ae88e6c71252e7baf20d85591d6fe726a288.jpg)  
Fig. 8. Value tree.

![](/api/attachments/Y48CWTV3/fulltext/images/0106a62dcbb18cddcfc8b67b382207706d25a9ca12c07092c2052289c4f2d24e.jpg)  
Fig. 9. Example of decision-maker's preference expression for a given criterion.

Decision-makers provide preferences for each consideration criterion r in the form:

– s/he prefers the situation $S _ { 1 }$ to $S _ { 2 }$ with a strength h: $S _ { 1 } \succ ^ { h } S _ { 2 }$

$- \ S _ { 1 }$ and $S _ { 2 }$ are equivalent: $S _ { 1 } { \approx } S _ { 2 }$

MACBETH translates these relationships into a system of independent equations. It then resolves these and calculates the aggregation using the weight mean operator. An interrogation procedure occurs to validate the consistency of the matrix of qualitative judgments. On this basis, MACBETH creates a numerical scale for each criterion that explains the relative magnitude of the decision-maker's judgments (Fig. 9).

## 5.3.2. Metrics design

When the project manager establishes project dashboards, s/he has to design the project KPIs. The problem here is how to de<sup>fi</sup>ne coherent KPIs for the project. The performance analysis triptych dimensions can be used to guide this step. Because effectiveness compares result levels against objectives, then the effectiveness component of KPIs could express a notion of “achievement progress”. Because ef<sup>fi</sup>ciency expresses resources bonding to achieve the task, then the ef<sup>fi</sup>ciency component of KPIs could be associated with the “using rate” dimension. Finally, because relevance expresses appropriateness between targets and bound resources, “re-estimation level” notions could constitute an appropriate dimension to de<sup>fi</sup>ne the relevance KPIs.

## 5.4. Step 3: KPI weighting

In line with senior management's performance strategy, we have to determine the respective weight to accord each project performance criteria. We compare one criterion to the other according to the same methodology used to treat values for each criterion. We indicate existing subordinations that could or should exist between KPIs by implementing the judgment matrix. A ranking of the KPI Categories is then established. At this stage information is purely ordinal. The solutions are then compared pair by pair for each criterion. Two <sup>fi</sup>ctional alternatives are introduced into the comparison process; these provide the reference values corresponding to the two extreme degrees of performance [21]. The comparison then consists in quantifying the difference of performance degree for each criterion. The resulting set of constraints de<sup>fi</sup>nes a linear programming problem. The solution of this problem provides the cardinal scale of performance associated with a criterion. This step is repeated for each criterion. Fig. 7 illustrates this process. The project manager compares all criteria pair by pair. In our example (Fig. 10), Delay Effectiveness and Cost Effectiveness KPIs appear as the most important criteria, whereas Quality Relevance is the least important.

## 5.5. Step 4: Project performance aggregation

Fig. 11 shows project KPIs and their values at D6. This <sup>fi</sup>gure shows how dif<sup>fi</sup>cult it is to identify clear trends and, therefore, to de<sup>fi</sup>ne improvement decisions. The most problematic tasks are quite hard to identify.

The target is to supply the decision-maker with the best and more accurate information to decide on the corrective action.

## 5.6. Step 5: Performance analysis

Finally, Fig. 12 presents the result given by the tool. From these results, in analyzing the groups of tasks that appear, we can extract the conclusions exposed in Fig. 13. We propose to distinguish four types of monitoring from absolute vigilance to normal monitoring. Here, the mapping between the tool output and the monitoring families is relative to this particular project: “worst” tasks in absolute vigilance and “better” in normal monitoring. In the future, it would be possible to generalize the analysis, for example in de<sup>fi</sup>ning theoretical threshold in order to constitute the families.

![](/api/attachments/Y48CWTV3/fulltext/images/0c4a4386e9e379af90baac7eefdd07bf6ea49bbcb1a3bf2216502971de7eba78.jpg)  
Fig. 10. KPI's relative weight.

<table><tr><td rowspan="2" colspan="2">Tasks</td><td>Current Time Progress</td><td>Current duration</td><td>Re-estimated fianl duration</td><td>Current Cost</td><td>Re-estimated total cost</td><td>Current Physic Progress</td><td>Re-estimated Final physic level</td><td>Current Criticity</td></tr><tr><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr><tr><td colspan="2">Composites Landing Gear development project</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>Industrialization study</td><td>80%</td><td>18</td><td>22</td><td>5 000 €</td><td>6 000 €</td><td>40%</td><td>1,2</td><td>00,6</td></tr><tr><td>22</td><td>Specifications drafting</td><td>100%</td><td>6</td><td>6</td><td>2 940 €</td><td>2 940 €</td><td>100%</td><td>1</td><td>0</td></tr><tr><td>23</td><td>Specifications validation</td><td>100%</td><td>3</td><td>3</td><td>1 260 €</td><td>1 260 €</td><td>100%</td><td>1</td><td>0</td></tr><tr><td>24</td><td>Industrialization study</td><td>50%</td><td>10</td><td>25</td><td>2 000 €</td><td>10 000 €</td><td>25%</td><td>1</td><td>0,3</td></tr><tr><td>34</td><td>Fitting Instruction sheet drafting</td><td>100%</td><td>4</td><td>4</td><td>1 500 €</td><td>1 500 €</td><td>100%</td><td>1</td><td>0</td></tr><tr><td>36</td><td>Pre-impregnated material numerical cutting program controlling</td><td>100%</td><td>0,5</td><td>0,5</td><td>210 €</td><td>210 €</td><td>100%</td><td>3</td><td>0</td></tr><tr><td>37</td><td>Moulding Instructions sheet controlling</td><td>100%</td><td>4</td><td>4</td><td>2 000 €</td><td>2 000 €</td><td>100%</td><td>1</td><td>0</td></tr><tr><td>38</td><td>Polymerization Instruction sheet controlling</td><td>100%</td><td>1</td><td>1</td><td>420 €</td><td>420 €</td><td>100%</td><td>1</td><td>0</td></tr><tr><td>39</td><td>Fitting Instruction sheet controlling</td><td>60%</td><td>3</td><td>5</td><td>1 260 €</td><td>2 000 €</td><td>60%</td><td>1</td><td>0,2</td></tr><tr><td>41</td><td>Control Instruction Sheet drafting</td><td>100%</td><td>4</td><td>4</td><td>1 680 €</td><td>1 680 €</td><td>100%</td><td>1,5</td><td>0</td></tr><tr><td>43</td><td>FAI finalization</td><td>57%</td><td>4</td><td>7</td><td>1 680 €</td><td>3 000 €</td><td>25%</td><td>1</td><td>0,5</td></tr><tr><td>47</td><td>Pre-impregnated material cutting</td><td>100%</td><td>1</td><td>1</td><td>100 €</td><td>100 €</td><td>100%</td><td>3</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Legend</td><td>OK</td><td>Warning</td><td>Problem</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 11. Scorecard at D6.

In this example, we can clearly identify which tasks need corrective actions. In this case, task 43 has the worst performance result and necessitate an absolute vigilance. Tasks 36, 24 and 15 require strong attention. Conversely, the overall thermometer clearly shows that the global performance of tasks 37, 41, 22, 23, 38 and 47 is on track. When we develop the same approach with KPI categories as options, we can explain which project dimension was particularly de<sup>fi</sup>cient (Cost, Quality, Time or Risk), and adapt the decision-making process as a result. The project manager has to pay particular attention to time management. A third analysis could consist of aggregating the project performance according to the performance analysis triptych in order to give the improvements a more precise orientation. Through this last analysis, we can envisage detecting trends in the project tending to de<sup>fi</sup>ne eccentric task objectives (Effectiveness) as shown in Fig. 13, use resources improperly (Ef<sup>fi</sup>ciency) or to allocate insuf<sup>fi</sup>cient or oversized means (Relevance).

Thus, cross-comparison of these three analyses will allow relevant improvement actions to be taken. Finally, we are able to drill down measurements at different levels of detail and time on the one hand, and at different dimensions on the other.

Note also that MACBETH allows robustness and sensitivity analyses to be performed.

![](/api/attachments/Y48CWTV3/fulltext/images/13e24fa429d25e6a3b1b19c1dfba4ff2149543db02a645859db346bd038159b1.jpg)  
Fig. 12. Performance aggregated assessment proposed by MACBETH for character, triptych and task orientations.

<table><tr><td></td><td>Tasks</td></tr><tr><td>absolute vigilance</td><td>T43,</td></tr><tr><td>strong attention</td><td>T24*, T15, T36</td></tr><tr><td>close surveillance</td><td>T34, T39</td></tr><tr><td>normal monitoring</td><td>T47, T38, T23*, T22, T41, T37*</td></tr></table>

\* = On the critical path

<table><tr><td></td><td>Characters</td></tr><tr><td>absolute vigilance</td><td>Time</td></tr><tr><td>strong attention</td><td>Cost</td></tr><tr><td>close surveillance</td><td>Quality, Risk</td></tr><tr><td>normal monitoring</td><td></td></tr></table>

<table><tr><td></td><td>Triptych elements</td></tr><tr><td>absolute vigilance</td><td>Effectiveness</td></tr><tr><td>strong attention</td><td></td></tr><tr><td>close surveillance</td><td>Efficiency</td></tr><tr><td>normal monitoring</td><td>Relevance</td></tr></table>

Fig. 13. Final performance aggregated assessment for character, triptych and task orientations.

Fig. 14 well underlines the weight of the decision-maker's preferences and constraints on the performance assessment. Depending on the strength associated with the Time Effectiveness, the <sup>fi</sup>nal task order will be different. In other words, we will not accord it the same priority. Corrective actions will not be the same.

## 6. Conclusion

Project control is characterized by many performance factors of different dimensions. If methods and tools to analyze project performance according to these dimensions (cost, time, quality, risk, etc.) exist, the published literature reveals the lack of a formalized tool to support a global analysis of all these criteria. In this paper, we propose a multi-criteria approach based on a performance cube composed of three dimensions: project activities or tasks; categories of performance indicators; and a breakdown of the performance triptych. Using a simple aggregation mean operator, the proposed approach allows us to make a global analysis of project performance. A special development based on the MACBETH method then offers the possibility of de<sup>fi</sup>ning (via a qualitative interaction with the project manager but in a quantitative manner) the weight for each performance's expression of the project. Finally, we propose a complete method to globally analyze a project's performance status from the task or performance category point of view. We present details of a case study. Many perspectives arise directly from this work. The main areas for study that we could explore center on four main topics:

– the robustness of using MACBETH, especially in projects with many tasks to manage;

– the impact of performance indicator interdependency on the proposition;

– links between research into project classi<sup>fi</sup>cation and choices for relative KPI weighting could be studied;

– the possibility of cross-aggregated analysis oriented in pairs could be studied. It could be relevant for several functions, such as Risk Manager or Financial Director.

In addition, the literature offers several methods of forecasting <sup>fi</sup>nal project cost, based on the actual cost performance at intermediate points in time [17]. Earned Value, for example, is a quantitative approach to evaluate the true performance of a project both in terms of cost deviation and schedule deviation. Other methods allow forecasting of project status in terms of quality or time [17]. However, we did not <sup>fi</sup>nd any references that simultaneously attempt to forecast project outputs for cost, time and quality. So, the development could be envisaged as a tool to forecast the global position (considering all dimensions: cost, time and quality factors at a minimum) of a project at the next period. This <sup>fi</sup>nal prospect clearly points to an evolution of our work towards an a priori performance evaluation.

![](/api/attachments/Y48CWTV3/fulltext/images/f5dccacbdde5e53415f243273622a63385a731fd0c04a7113a7a5d7672c124b4.jpg)  
Fig. 14. Time effectiveness sensitivity analysis

## References

[1] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (2008) 657–672.

[2] R. Atkinson, Project management: cost, time and quality, two best guesses and a phenomenon, its time to accept other success criteria, International Journal of Project Management 17 (6) (1999) 337–342.

[3] R. Bagwat, M.K. Sharma, Performance measurement of supply chain management: a balanced scorecard approach, Computers & Industrial Engineering 53 (2007) 43–62.

[4] C.A. Bana e Costa, P.M. Chagas, A career choice problem: an example of how to use MACBETH to build a quantitative value model based on qualitative value judgments, European Journal of Operation Research 153 (2004) 323–331.

[5] C.A. Bana e Costa, J.M. De Corte, J.C. Vansnick, “MACBETH”, LSE OR Working Paper 03.56, London School of Economics, London, 2004.

[6] M. Bourne, A. Neely, J. Mills, K. Platts, Implementing performance measurement systems literature review, International Journal of Business Performance Management 5 (1) (2003) 1–24.

[7] Y. Chen, D. Marc Kilgour, K.W. Hipel, Screening in multiple criteria decision analysis, Decision Support Systems 45 (2008) 278–290

[8] S.O. Cheung, C.H. Suen Henry, K.W. Cheung, PPMS: a web based construction project performance monitoring system, Automation in construction 13 (2004) 361–376.

[9] V. Clivillé, 2004. Approche systémique et méthode multicritère pour la dé<sup>fi</sup>nition d'un système d'indicateurs de performance. PhD Thesis, Université de Savoie.

[10] V. Clivillé, L. Berrah, G. Mauris, Quantitative expression and aggregation of performance measurements based on the MACBETH multi-criteria method, International Journal of Production Economics 105 (2007) 171–189.

[11] F.T. Dweiri, M.M. Kablan, Using fuzzy decision-making for the evaluation of the project management internal ef<sup>fi</sup>ciency, Decision Support System 42 (2) (2005) 712-726.

[12] J. Figueira, S. Greco, M. Ehrgott, Multiple Criteria Decision Analysis: State of the Art Surveys, Springer, 2005 1045 pp.

[13] F. Ghasemzadeh, N.P. Archer, Project portfolio selection through decision support Decision Support Systems 29 (2000) 73–88.

[14] Grey, S., 1995. Practical Risk Assessment for Project Management. John Wiley & Sons Editor.

[15] T.A. Hansen, J.O. Riis, Exploratory performance assessment, International Journal Business Peformance Management 1 (2) (1999) 113–133.

[16] H.S. Hwang, Web-based multi-attribute analysis model for engineering project evaluation, Computers & Industrial Engineering 46 (2004) 669–678.

[17] I. Hyväri, Project management effectiveness in project oriented business organizations, International Journal of Project Management 24 (3) (2006) 216–225.

[18] International Organization for Standardization (ISO), ISO 10006:2003 standard: quality management systems—guidelines for quality management in projects, vol. 32, 2003.

[19] J.H. Jacot, A propos de l'évaluation économique des systèmes intégrés de production, in ECOSIP, Gestion industrielle et mesure économique, Paris: Economica, 1990, pp 61–70.

[20] P. Korhonen, Multiple criteria decision support—a review, European Journal of Operational Research 63 (1992) 361–375.

[21] M. Lauras, D. Gourc, A multi-criteria approach to a more effective management of projects, International Conference on Industrial Engineering and System Management; IESM; May 30–June 2, Beijing, 2007.

[22] E.C. Martinez, D. Duje, A. Perez, On performance modeling of project-oriented production, Computers & Industrial Engineering 32 (1997) 509–527.

[23] D. Milosevic, P. Patanakul, Standardized project management may increase development project success, International Journal of Project Management 23 (2005).181-192.

[24] A. Neely, M. Gregory, K. Platts, Performance measurement system design: a literature review and research agenda, International Journal of operations & Production Management 15 (4) (1995) 80–116.

[25] A.D. Neely, J. Mills, K. Platts, M. Gregory, H. Richards, Performance measurement system design: should process based approach be adopted? International Journal of Production Economics 46–47 (1996) 423–431.

[26] PMI Standards Committee, A Guide to the Project Management Body of Knowledge, PMI Publishing Division. 1996.

[27] Pritchard, C.L., 1997. Risk Management: Concepts and Guidance. ESI International Editor.

[28] Roseneau Milton, D., and G.D. Githens, 2005. Successful Project Management: A Step by Step Approach with Practical Examples. John Wiley & Sons Editor, 4th edition.

[29] M. Roubens, A. Rusinowska, H. de Swart, Using MACBETH to determine utilities of governments to parties in coalition formation, European Journal of Operation Research 172 (2) (2004) 588–603.

[30] B. Roy, Multicriteria Methodology for Decision Analysis, Kluwer Academic Publishers, 1996.

[31] M. Swink, S. Talluri, T. Pandejpong, Faster, better, cheaper: a study of NPD project ef<sup>fi</sup>ciency and performance tradeoffs, Journal of Operations Management 24 (2005) 542–562.

[32] E. Westerveld, The Project Excellence Model: linking success criteria and critical success factors, International Journal of Project Management 21 (2003) 411–418.

[33] C. Xiaoyi Dai, W.G. Wells, An exploration of project management of<sup>fi</sup>ce features and their relationship to project performance, International Journal of Project Management 22 (2004) 523–532.

[34] G. Yu Angus, P.D. Flett, J.A. Bowers, Developing a value-centred proposal for assessing project success, International Journal of Project Management 23 (2005) 428–436.

[35] O. Zwikael, K. Shimizu, S. Globerson, Cultural differences in project management capabilities: a <sup>fi</sup>eld study, International Journal of Project Management 23 (2005) 454–462.

![](/api/attachments/Y48CWTV3/fulltext/images/72df8d1d4af39a4bc1a659540149e4ef92258283faa6efeef3368f8d5d6a0c36.jpg)

Matthieu Lauras was Supply Chain Project Manager in a pharmaceutical company from 2001 to 2005. After this experience he joined the Industrial Engineering Department of the Université Toulouse—Mines Albi, as an Associate Professor and the Toulouse Business School as an Af<sup>fi</sup>liate Professor. His works mostly focus on supply chain management and performance management for project and business process. All his researches concern as well the industrial sector as the humanitarian sector. He has published several papers in journals and international conferences in the area of performance assessment and supply chain management.

![](/api/attachments/Y48CWTV3/fulltext/images/7c560b5b58a83e2c0b558a14626ceeac644db1c5f643ab3fec92c19cdc180012.jpg)

Guillaume Marquès works as PhD student at the Universite Toulouse—Mines Albi. He is a young logistics engineer with some experiences in industry. His works mainly focus on the risks management for supply chain management through a simulation approach. During his master he worked on project management and particularly the link with decision support systems and multi-criteria performance assessment.

![](/api/attachments/Y48CWTV3/fulltext/images/893722b15477b5940bcd233609131c60730fa6d93996fc13435c4c1801b2c6e8.jpg)

Didier Gourc, Ph.D., is currently an Associate Professor at the Ecole des Mines d'Albi-Carmaux where he teaches Project Management. He has a PhD from the University of Tours and he has gained industrial experiences in software development, project management and consultancy on diagnostic of production process and project management organization since 1992. His current research interests include project management, project risk management, portfolio management and project selection. He develops his research specially in relation with pharmaceutical industry.
