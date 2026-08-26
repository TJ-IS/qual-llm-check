---
otero_id: 17935
otero_key: "UXH877C5"
title: "A framework for decision support systems evaluation"
authors: "J. Akoka"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90040-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Framework for Decision Support Systems Evaluation

J. Akoka

École Supérieure des Sciences Economiques et Commerciales, BP 105, 95021 CERGY Cedex, France

In this paper, we present a framework for the Decision Support Systems evaluation problem. Using the Gorry-Scott Morton's framework for information systems, we develop several evaluation methods that structure the evaluation process. The framework determines the best methods of evaluation that are suitable to the characteristics of the Decision Support System concerned. Finally, we use the framework to evaluate two widely used Decision Support Systems.

Keywords: Decision Support System, Evaluation, Gorry-Scott Morton framework.

![](/api/attachments/UXH877C5/fulltext/images/6c3e601555bc2bf95ceff6e868a34229ecf5319f53657567e5a944a1b13eb6b6.jpg)

Jacob Akoka received the R.S., M.S., and Doctorate degrees in computer science and operations research from the University of Paris VI, Paris, France, and the Ph.D. degree in Management Information Systems from the Sloan School of Management, Massachusetts Institute of Technology, Cambridge, USA. Currently, he is Associate Professor of Management Science at the Ecole Supérieure des Sciences Economiques

et Commerciales (ESSEC), where he has been a member of the faculty since 1971. He is also Head of the Research Center. He has done research in the fields of Management Information Systems (design of computer networks, optimization of distributed data systems, centralization versus decentralization of information systems, teleconference systems, design implementation, and evaluation of Decision Support Systems). Dr. Akoka has industrial experience as a Systems Engineer in a large French Bank, and has done extensive consulting work for French and other international companies. His current interests are in the design of distributed processing and the evaluation of DSS and information systems. Dr. Akoka is a member of several international scientific societies, Editor of Revue Sciences de Gestion, and Series Editor of the Enterprise Moderne d'Edition series in Management Science.

## 1. Introduction

Decision support systems (DSS) are defined as a category of information systems used in organizations to assist managers in semi-structured decision processes. They are intended to improve the effectiveness of this process [1]. One framework [2] was designed to structure the Management Information System field along two dimensions: the type of managerial activity (operational control, management control and strategic planning) and the degree of structure of the decision process considered (from structured to unstructured). Decision Support Systems are defined as covering the intermediate horizontal area corresponding to the 'semi-structured' decisions (Fig. 1).

Three inter-related phases are involved in Decision Support Systems development:

1) the design phase, where the decision situation is analyzed and criteria for the technical structure and DSS routines are defined;

2) the implementation phase, where the system is nested into the organizational, political and behavioral context;

3) the evaluation phase, where the achievement of pre-determined objectives is assessed. This assessment leads back to the design phase for improvement and correction of some of the system features.

The purpose of this paper is to consider one of the development phases, namely the evaluation phase, and to lay out some proposals about the ways one could use the DSS framework in order to find out what evaluation methods best suit different types of DSS's according to their position within the framework. From this point of view, our aim is to make an 'active tool' from this framework: to take advantage of the structure it provides to state general properties of each cell as far as evaluation is concerned, so that these properties can then be used for specific DSS examples.

<table><tr><td></td><td>Operational Control</td><td>Management Control</td><td>Strategic Planning</td></tr><tr><td>Structured</td><td>Account receivablesOrder EntryInventory</td><td>Budget AnalysisShort-term Forecasting</td><td>Tanker Fleet MixWarehouse Location</td></tr><tr><td>Semi-Structured</td><td>Production SchedulingCash Management</td><td>Variance Analysis-overall BudgetBudget Preparation</td><td>Mergers and AcquisitionsNew Product Planning</td></tr><tr><td>Unstructured</td><td>PERT/COST Systems</td><td>Sales and Production</td><td>R &amp; D Planning</td></tr></table>

Fig. 1: Information Systems: a Framework.

Let us take, for instance, the Portfolio Management System (PMS) [3], a DSS developed to assist investment managers in security selection. In this case, the evaluation problem is currently solved by assessing what evaluation methods are best for this system, considering its specific characteristics. We think it would be useful to be also able to solve this evaluation problem by:

1) looking at what place PMS occupies in the DSS framework;

2) using general properties of this cell concerning the evaluation phase.

Let us also point out that our statement of these general cell properties is not an easy task and cannot be considered as a definitive answer. First, because evaluation is tightly interrelated with the design and implementation phases, consideration of only one of them reflects a partial view of a more comprehensive problem (i.e., the relation between the framework and DSS development phases). Second, because the breakdown of the DSS field into cells somewhat overlooks the continuity of the two dimensions, no sharp defined conclusion is really attainable (or even desirable).

## 2. The Evaluation Problem

During the sixties, when 98% of the applications where solely aimed at automating existing procedures (e.g., accounting and payroll), evaluation did not seem to be a problem. Costs incurred in developing such systems were reasonably clearly discernable, as were benefits; most often the benefits were in terms of clerical cost displacement. Today, companies are turning to more difficult applications, often less well structured types of applications, for which "hard" measures are not enough to evaluate the impact of decision support systems. Nevertheless, there are many reasons why an organization must not skip the evaluation phase.

## 2.1. Reasons for Evaluation

When an organization develops a DSS, it is making an investment. As McRaw [4] says, it is “an expenditure of present resources to provide a future income”. The DSS is a difficult investment to evaluate, because the income from the DSS is not as clearly defined as it is with most other investments. Nonetheless, it is needed for the following reasons:

\- To determine, if possible, the benefits of the DSS.

\- To measure the quality of the system.

\- To assess, by using managers' perceptions, the "value" of the system. This may include the responsiveness, availability, and reliability of the system.

\- To measure the impact of the system on the decision process.

\- To assess the influence of the new system on the learning and attitude styles of the managers.

\- To investigate the influence of the DSS on the decision outputs.

\- To learn, so that improvements are possible.

Of course, this list is not exhaustive, but it helps the manager to understand the need for an evaluation process. At this point let us stress the fact that managers are more easily convinced about the need and the utility of evaluation if a clear strategy is proposed.

## 2.2. Strategy for Evaluation

We propose two principles:

\- The evaluation procedure has to be considered as an evolving process design.

\- If possible, the evaluation should not be a post facto accounting process.

Evaluation is a continuous process that begins before the system is designed. It should be embedded in the implementation process; it needs to be an ongoing activity throughout implementation. This implies that the evaluation process should not be a post facto accounting process. To be effective, an evaluation should answer the following questions [5]: - Have the predefined aims of the system been met? - Do the key indicators show that the system is generating the changes and benefits expected? - What are the cost in dollars and time required for success?

## 2.3. Evaluation Methods

One of the issues concerning DSS evaluation is methodology: what is to be assessed and measured? How to do it? A 'smorgasbord' of evaluation methods has been proposed [1] and we will use these (adding one more) as the set to be considered for each ceil of the framework.

## 2.3.1. Decision Outputs

This focuses on the output of the decision making process and attempts to measure whether output has been improved through the use of the DSS. It involves a direct comparison between old and new elements according to a given criterion. For example, in a cash management system, the output is the decision to invest some idle cash, and where to invest it; the criterion is the extra-return obtained from these short-term investments; the decision output evaluation method will consist in comparing the returns before and after introduction of the system. Three conditions must occur for this method to be applicable:

\- the output of the decision making process must be clearly defined and of a similar nature before and after the DSS is implemented.

\- there must be some way of measuring the output in order to make comparisons. Clearly quantifiable outputs are best.

-- it must be possible to leave out external factors that could be also responsible for a better (or a worse) output in order to be able to assess the impact of the DSS, and of the DSS only. This requirement is generally the most difficult.

## 2.3.2. Decision Process

While the first method looks at the output, the second looks at the decision making process. Its goal is to assess whether this process is likely to be more effective with the new DSS than prior to it. In most cases, the two processes (before and after) are substantially different, and comparison cannot be made a piece at a time, but rather on a more global basis. The criteria for this comparison are generally more qualitative and involve an analysis of the characteristics of the new process in terms of likely rather than certain effectiveness. For example, a reason for a better process would be that the DSS incorporates (totally or in part) a normative model that is known to have advantages over the former existing model. From a practical viewpoint, a tool for this type of evaluation is the use of trace (as mentioned in Keen & Scott Morton [1]): it avoids the danger of comparing the old process with the new as conceived by the designer instead of as actually understood and carried out by the user. Here, it is necessary to have an objective descriptive model of the new process.

## 2.3.3. Managerial Attitudes and Concepts

This method does not directly consider the managerial decision making process but managers themselves: how the DSS is able to improve their decision making. The issue is highly qualitative, but the ways to reach conclusions are, in this case, very subjective (while they were objective in method 2.3.2. It involves interview techniques or other socio-psychological tools whose results are often likely to be challenged. However, for some systems this type of evaluation method can be the only relevant one.

## 2.3.4. Procedural Changes

This evaluation technique focuses on the mechanical aspects of the decision process rather than its qualities. Such components as time, human, and computer resources involved are measured, and an assessment is made as to whether an improvement has taken place or not. The ease with which such measurement are made often makes this method the only one that is actually undertaken, though it is likely to apply only to one category of systems.

## 2.3.5. Service

This attempts to measure how well the system performs its task for the user. Again, this is an issue only indirectly related to the quality of the decision process. It involves such factors as reliability, accessibility and invisibility to users, and response time. Here again the evaluation tools are quite easy to develop (e.g., breakdown statistics and degree and difficulty of training of users), and there is some danger in considering only this in expressing the value of the system.

## 2.3.6, Managers' Assessment of the Value

This method endeavours to define the value of a system whose benefits are difficult to qualify. One way is by asking managers. Through questionnaires or interviews. As stated by Keen & Scott Morton [1] "If their instructions differ from the 'facts' implied by other components of the evaluation smörgåsbord, the process of unravelling the differences can yield useful insights".

## 2.3.7. Anecdotal Reports

To supplement the formal evaluation process, it may be useful to gather information about insights, opinions, and events. This informal evaluation can help flesh out the picture implied by the formal measures.

## 2.3.8. Cost-Benefit Analysis

The development and usage of a DSS involve costs as well as benefits. The question usually asked in cost/benefit analysis is: "Do benefits exceed costs?" If so, the system is a "good investment". One disadvantage of this method is that it tends to ignore factors such as intangible costs, psychological cost of change, description of the organization's equilibrium, and customer annoyance.

## 2.3.9. Cost-effective Analysis

There is a distinction between cost-benefit and the cost-effective methods. The cost-effective method assumes the outputs from a DSS to be fixed in quantity and quality. It then explores the comparative cost of various methods of producing this fixed output. That system which can produce the fixed output at lowest cost is selected as being the most efficient system. The cost-effective approach assumes that although the inputs to a system are variable, the output is fixed. The cost-benefit approach removes this latter constraint; i.e., it allows both the inputs and the outputs from the several systems to vary, and then attempts to measure which of these systems has the most return.

The main objection that can be addressed to the methods discussed above is that they do not constitute a consistent theory: they may be considered more a grab bag. Nevertheless, if used in connection with the Garry Scott Morton's framework, they may be of help to managers dealing with the evaluation issue.

## 3. Framework for DSS Evaluation

We now attempt to establish a relationship between the DSS cells and the nine methods developed above. It must be noted, however, that it does not give a 'recipe' for a single method for each cell, but more a range of methods from which a choice must be made. We successively group the methods according to the first dimension (management activity) then according to the second (degree of structure).

## 3.1. Classification According to Management Activity

Two variables are chosen to represent the variations from operational control to strategic planning: the nature of the objectives and the type of information used:

\- Objectives. These change from very specific, numerical, and often cost oriented in the strictly operational control area (left side of the table) to general, qualitative, and policy oriented in the strategic planning area. In the intermediate area they mix quantitative (e.g., profits) and qualitative (nature and effectiveness of the process) features.

Information used. From quantitative, detailed, accurate, and narrow in scope in the area of operational control, to qualitative, aggregate, imprecise, and general in scope in the area of strategic planning. Evaluation methods must also take into account the specificity of the information processed through the DSS, since they use and analyze this information, as inputs or outputs of the system.

Our classification of the nine methods is made according to the 'value' of these two variables (objectives and information) in the three areas considered:

## 3.1.1. Operational Control

Three methods are considered to be well suited to the objectives and information characteristics of DSS supporting operational control activities:

(1) Cost-Effectiveness Analysis. This focuses on costs, whose decrease is the major objective of many operational control systems. It corresponds to the extreme case where all cost factors can be quantified because of the total numerical nature of the information processed.

(2) Cost-Benefit Analysis. This concerns the case where intangible cost and benefits are present. A more general, less strictly cost-oriented approach becomes necessary and becomes particularly relevant.

(3) Decision Output. Still in the area where numerical attributes can be given to decisions (though somewhat overlapping the management control area), but not necessary in terms of costs and benefits, this method is applicable for criteria depending on the system considered.

## 3.1.2. Management Control

As mentioned before, management control DSS have objectives mostly given in terms of improvement of the decision process. Three methods explicitly focus on the process rather than its inputs and outputs:

(1) Procedural Changes. This focuses on the mechanical aspects. It is best suited to management control DSS's that are close to operational control.

(2) Change in Decision Process. This is the most fundamental method for the management control area.

(3) Service Measure. How well the DSS is perceived by its users is an important part of the improvement it brings about in decision making.

## 3.1.3. Strategic planning

The three most 'qualitative' and general methods are relevant for strategic planning DSS's, as this area involves objectives and similar information:

(1) change in managers' concept and attitudes.

This is especially crucial for strategic planning: it involves quick adaptation and openness to change on the part of managers.

(2) managers' assessment of the system.

(3) anecdotal reports.

These two last methods refer to a subjective evaluation process that suits areas of strategic planning where personality or behavior are important.

The discussion thus leads to Fig. 2.

<table><tr><td></td><td colspan="2">Operational control</td><td colspan="2">Management Control</td><td colspan="2">Strategic Planning</td></tr><tr><td>Structured</td><td colspan="2">Account receivablesOrder Entry</td><td colspan="2">Budget Analysis</td><td colspan="2">Tanker Fleet Mix</td></tr><tr><td>Semi-structured</td><td colspan="2">Production scheduling</td><td colspan="2">Budget preparation</td><td colspan="2">Mergers and Acquisitions</td></tr><tr><td>Unstructured</td><td colspan="2">PERT/COST Systems</td><td colspan="2">Sales and Production</td><td colspan="2">R &amp; D Planning</td></tr><tr><td rowspan="9"></td><td rowspan="9" colspan="2"></td><td rowspan="9" colspan="2"></td><td colspan="2"></td></tr><tr><td colspan="2">Change indecisionprocess</td></tr><tr><td colspan="2">ServiceMeasure</td></tr><tr><td rowspan="6" colspan="2">Procedurechanges</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

Fig. 2. The Framework showing Evaluation Techniques and Managerial Activity interaction.

3.2. Classification According to the Degree of Structure

Three variables are chosen to represent the change from the structured to unstructured decisions: inputs, processes and outputs.

## 3.2.1. The Inputs

The inputs needed are the data (external or/and internal) used to achieve the task. For structured decisions, the data are detailed specific, easily quantifiable, and (most of the time) cost-oriented.

For the semi-structured area, the inputs tend to be less detailed, more qualitative, difficult to quantify, and less cost oriented. Finally, for structured decisions, the data tends to be fuzzy, non-cost oriented, judgemental, and very qualitative.

## 3.2.2. The Processes

When moving from structured to unstructured decisions, the processes tend to move from mathematical models (optimization, regression, ...) to more judgemental models representing a qualitative or behavioral science approach. In the semi-structured area, some simulation techniques may be useful.

## 3.2.3. The Outputs

These tend to have the same characteristics as the input. Evaluation methods have to be classified in relation to the characteristics of the decision and the three factors described above.

Structured Decisions. Three methods are considered to be well suited to the structured decisions: decision outputs, cost-benefit analysis and cost-effective analysis. The order in which are written is critical.

Semi-structured Decisions. Three methods can be used here, in the order: change in decision process, service measure and procedure changes.

Unstructured Decisions. The evaluation method to be used are: managerial assessment, managerial concepts and anecdotal reports. we now obtain the framework depicted in Figure 3.

<table><tr><td colspan="2"></td><td colspan="3">Operational Control</td><td colspan="3">Management Control</td><td colspan="4">Strategic Planning</td><td>Axis 2</td></tr><tr><td rowspan="3" colspan="2">Structured</td><td>A</td><td colspan="2"></td><td colspan="3"></td><td colspan="4"></td><td>decision outputs</td></tr><tr><td rowspan="2" colspan="3">Account receivables Order Entry</td><td rowspan="2" colspan="3">Budget Analysis</td><td rowspan="2" colspan="4">Tanker Fleet Mix</td><td>cost-benefit</td></tr><tr><td>cost-effective</td></tr><tr><td rowspan="3" colspan="2">Semi-Structured</td><td rowspan="3" colspan="3">Production Scheduling PMS</td><td rowspan="3" colspan="3">BRANDAID Budget Preparation</td><td rowspan="3" colspan="4">Mergers and Acquisitions</td><td>change in decision process</td></tr><tr><td>service measure</td></tr><tr><td>procedural change</td></tr><tr><td rowspan="3" colspan="2">Unstructured</td><td rowspan="3" colspan="3">Pert/cost Systems</td><td rowspan="3" colspan="3">Sales and Production</td><td rowspan="3" colspan="4">R &amp; D Planning</td><td>managerial assessment</td></tr><tr><td>managerial concepts</td></tr><tr><td>anecdotal reports</td></tr><tr><td rowspan="2"></td><td>Axis 1</td><td>cost- effective</td><td>cost- benefit</td><td>cost- output</td><td>decision decision changes</td><td>procedural measure</td><td>service process</td><td>change in decision</td><td>change in reports</td><td>anecdotal concepts</td><td>managerial assessment</td><td>managerial management</td></tr><tr><td colspan="12">Category 1 Category 2 Category 3</td></tr></table>

Fig. 3. A Complete Framework for DSS Evaluation.

## 4. Some Applications of our Framework

We now illustrate the application of this framework for two DSS's corresponding to two different cells: the Portfolio Management System [4] and Brandaid [6].

## 4.1. Portfolio Management System

The first question to be answered is: where does PMS fit in the framework? The recurring nature of the decision process and the detailed and relatively short-term characteristics of the information used leads us to place it in the right handside of operational control. On the other hand, this type of decision is semistructured, as no model is able to really cover all its components. Having placed this DSS into one cell, we may consider the methods of evaluation allowed by our analysis; e.g., for the horizontal axis, the decision output method would involve comparison of old and new rates of return of portfolios; however along the vertical axis, the decision process and the service measure method may be considered for their convenience of use, which is particularly important for this type of system. We are not arguing however, that the precedent methods are the only way to evaluate PMS. The evaluator should primarily concentrate on these methods and then possibly investigate other methods (such as a cost-oriented approach).

Let us consider the other methods and assess whether and why they are less relevant for PMS. Two groups have been excluded:

a) The cost-oriented methods: cost-effectiveness and cost benefit analysis.

Two reasons make these methods of little value for PMS assessment: First, the objective of PMS design and implementation was not to 'save' money and therefore it was not really cost-oriented. The best evidence of this is that the use of PMS is not mandatory for investment managers: yet if cost effectiveness was the objective, there would be no reason for keeping the old process alive in parallel, since cost effectiveness could not be fully assessed in a partial implementation. The system objectives were stated in much broader terms: emphasizing changes in the decision process, and methods in the middle of the range are better suited for this.

Second, though cost data are relatively easy to get (e.g., development and operating costs), the benefits are very difficult to state in monetary terms. For example, What is clients' satisfaction? How do we assess any time saved by managers using this system? Now are we sure that some benefits are due to the system and not to other environmental factors? We do not think that these questions can be answered for PMS and this makes cost-benefit evaluation close to impossible. However, broad quantitative pay-offs can be evaluated; e.g., in terms of portfolio returns. This brings us to the decision output method that we proposed as relevant.

b) The subjective methods: managers' concepts and attitudes changes, managers' assessment of system value and anecdotal reports methods.

It is likely that these methods would help in PMS evaluation. However, our argument is rather that they would be of little help in deciding if PMS is a good system or a bad one.

Essentially, the evidence presented by people who have interviewed managers using – or not using – PMS has too many contradictions in their statements about its value. One says “The department is now performing better” while another says “No, hasn’t increased account performance”. Clearly, their view of the system is highly dependent on their management style and it contains too many biases. This does not mean these opinions are not relevant and somewhat helpful, but we do not think they enable one to reach major conclusions about PMS effectiveness. The same reasoning holds for the anecdotal reports method: they are interesting, sometimes amusing, but too subjective and narrow in scope for a system that claims to create a better decision process.

On the other hand, we are not sure whether we can state that the managers concepts and attitudes changes method should not be used at all: for example, one of the objectives of PMS was to shift from a security-oriented to a portfolio-oriented type of financial management, and this method is clearly relevant for evaluating how well this objective was reached. Our framework does not properly take this into account. Thus, we conclude that, taking the PMS system as a test, our framework enables one to focus on the most useful methods quite well, while it does not definitely imply that the other methods should be discarded without further analysis.

## 4.2. Brandaid

Two facts allow us to put Brandaid [6] in the semi-structured management control cell: (i) it involves the determination of timing and nature of expenditures for various aspects of marketing promotion; (ii) it deals with the investigation of advertising response curves implicit to the manager's own concepts. Since it is placed on the diagonal of the framework, the methods of evaluation that are the most suitable to Brandaid are: Services measures, change in the decision process and procedural changes. Some cost-oriented methods can be applied but it will be very difficult to argue that any improvement in the marketing sector is due only to Brandaid and not to other economic conjectural factors. Even if a cost-oriented method is applied, we feel that more than 80% of the evaluation can be obtained by using the methods related to changes in procedures and decision processes. As one can see it, both examples fit pretty well in our framework. However, we are aware that other DSS could point out some of the shortcomings and deficiencies of this approach.

By putting BRANDAID in the Management Control/Semi Structured cell, we discarded evaluation methods that are not in correspondence with this cell. If other words we are arguing that evaluation methods such as managerial assessment, managerial concepts and anecdotal reports are not of a great help in the evaluation process. We now give our reasons:

## 4.2.1. Anecdotal Reports

Being build around a mathematical model, Brandaid eliminates some anecdotal reports relevant to systems such as PMS. The decisions made by the managers are those related to prices, advertising, brand sales, etc... This kind of decisions are figure-oriented and therefore not subject to personal judgement within the framework of the model. This dictates the factors that are to be used, therefore allowing little flexibility, and hence no value to personal anecdotes.

## 4.2.2. Managerial Concepts

On can argue that Brandaid can be used as a learning tool: "Any discrepancy between predicted and actual quickly confronts the model's team. The pressure to understand the reasons is great". Although

Brandaid can be of help to managers in the learning process, one can questions its ability to bring change to their attitudes and concepts.

## 4.2.3. Managerial Assessment

There is no doubt that Brandaid is useful. But would it be possible to evaluate it by only asking managers? We think that this method may be misleading, since no managers can strongly assert that the improvement (if any) is due to Brandaid alone- or to other factors, such as their own ability to manage. We feel that managerial assessment can be used, but its impact on the overall evaluation may be very low.

We now turn to the cost-oriented methods. As suggested earlier, Brandaid can be situated between the line separating structured decisions from unstructured decisions. Therefore some cost-oriented measures can be applied, especially the cost/effective method. One can measure the effectiveness of the system before using Brandaid and compare it to the actual effectiveness after. This comparison may give some insights in the evaluation process. But once again it will be very difficult to attribute the improvement only to Brandaid. Other factors, such as the economical environment and the level of competition may be more important. This argument holds also for the other methods (decision outputs and cost-savings methods).

In summary, we have provided some arguments why Brandaid can be evaluate principally by using evaluation methods of the second category. More insights can be gained by using other evaluation methods, but the “added information” obtained may be very small and insignificant.

Once again we stress the fact that our framework is not intended to be a rigorous guide, but rather to be used as a way to narrow down the process of evaluation. It can help to eliminate the evaluation methods that are not relevant to a particular DSS.

## 6. Conclusion

In this paper, we developed a framework for the DSS evaluation issue. The main advantages of this framework are:

(i) It expands the smorgasboard described in Keen & Scott Morton's book [1].

(ii) It structures the evaluation process.

(iii) It can be used as a guide to determine the best methods of evaluation that are suitable to the characteristics of the DSS concerned.

(iv) It expands the role of Gorry - Scott Morton's framework by giving it a more active role.

We do not claim that we have solved the evaluation problem. Rather we are convinced that this is only a first step toward a more comprehensive model of the evaluation process. Although, the framework is incomplete, it has the merit to exist (especially when one considers the piece-meal approach that is used in other papers). Finally, we would recommend the use of the Gorry-Scott Morton framework to structure other aspects of DSS (e.g. implementation-design) in the same way as for the evaluation issue.

## References

[1] P.G.W. Keen, and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addision Wesley, 1978).

[2] G.A. Gorry and M.S. Scott Morton, "A framework for management Information Systems", Sloan Management Review, vol. 13, no. 1 (Fall 1971).

[3] T.P. Gerrity, "The design of man-machine decision systems: an application to portfolio management", Sloan Management Review, vol. 12, no. 3 (Winter 1971).

[4] T.W. McRae, "The evaluation of investment in computers", Abacus, vol. 6 (1970).

[5] P.G.W. Keen, "Computer-based decision aids: the evaluation problems", Sloan Management Review, vol. 16, no. 3 (Spring 1975).

[6] J.D.C. Little, "Brandaid: a marketing mix model, part. 1, Structure", Operations Research, vol. 23, no. 4 (July-August 1975).
