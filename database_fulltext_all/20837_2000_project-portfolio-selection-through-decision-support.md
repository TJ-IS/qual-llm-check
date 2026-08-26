---
otero_id: 20837
otero_key: "CAER6KEM"
title: "Project portfolio selection through decision support"
authors: "F. Ghasemzadeh; N.P. Archer"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00065-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Project portfolio selection through decision support

F. Ghasemzadeh, N.P. Archer )

Michael G. DeGroote School of Business, McMaster UniÕersity, Hamilton, ON, Canada L8S 4M4

Accepted 24 February 2000

## Abstract

Project portfolio selection is a crucial decision in many organizations, which must make informed decisions on investment, where the appropriate distribution of investment is complex, due to varying levels of risk, resource requirements, and interaction among the proposed projects. In this paper, we discuss the implementation of an organized framework for project portfolio selection through a decision support system DSS , which we call Project Analysis and Selection SystemŽ . Ž .PASS . We describe the results of laboratory tests undertaken to measure its usability and quality, compared to manual selection processes, in typical portfolio selection problems. We also discuss the potential of PASS in supporting corporate decision making, through exposure this system has received through demonstrations for several companies. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Project portfolio selection; Project management

## 1. Introduction

Project portfolio selection is the periodic activity involved in selecting a portfolio of projects, that meets an organization’s stated objectives without exceeding available resources or violating other constraints. Some of the issues that have to be addressed in this process are the organization’s objectives and priorities, financial benefits, intangible benefits, availability of resources, and risk level of the project portfolio 37 . <sup>w</sup> <sup>x</sup>

Difficulties associated with project portfolio selection result from several factors: 1 there are multipleŽ . and often-conflicting objectives, 2 some of the Ž . objectives may be qualitative, 3 uncertainty and Ž . risk can affect projects, 4 the selected portfolio Ž . may need to be balanced in terms of important factors, such as risk and time to completion, 5Ž . some projects may be interdependent, and 6 theŽ . number of feasible portfolios is often enormous.

In addition to these difficulties, due to resource limitations there are usually constraints such as finance, work force, and facilities or equipment, to be considered. As some researchers have noted 30 , the<sup>w</sup> <sup>x</sup> major reason why some projects are selected but not completed is that resource limitations are not always formally included in the project selection process. In cases where resource limitations are at fault for a failed project, a selection model that incorporated resource limitations could have aided the decision maker in avoiding such mistakes 37 . Portfolio selection becomes more complex when resource availability and consumption are not uniform over time.

There are many different techniques that can be used to estimate, evaluate, and choose project portfolios 11,18 . Some of these techniques are not widely<sup>w</sup> <sup>x</sup> used because they address only some of the above issues, they are too complex and require too much input data, they may be too difficult for decision makers to understand and use, or they may not be used in the form of an organized process 10 . Among <sup>w</sup> <sup>x</sup> all of the techniques that are available, optimization techniques are the most fundamental quantitative tool for project portfolio selection 26 and address<sup>w</sup> <sup>x</sup> most of the important issues. However, they have largely failed to gain user acceptance 31 , and few<sup>w</sup> <sup>x</sup> modeling approaches, from a variety of optimization approaches that have been developed, are being utilized as aids to decision making in this area 29 .<sup>w</sup> <sup>x</sup> According to Hess 24 ‘‘management science has<sup>w</sup> <sup>x</sup> failed altogether to implement project selection models; we have proposed more and more sophistication with less and less practical impact’’. One of the major reasons for the failure of traditional optimization techniques is that they prescribe solutions to portfolio selection problems without allowing for the judgment, experience and insight of the decisionmaker 31 .<sup>w</sup> <sup>x</sup>

A literature review we conducted in this field 3<sup>w</sup> <sup>x</sup> clearly showed that, although there are many different methods for project evaluation and portfolio selection that have their own advantages, no single technique addresses all of the issues that should be considered in project portfolio selection. Among published methodologies for project portfolio selection, there has been little progress towards achieving an integrated framework that: a simultaneouslyŽ . considers all the different criteria in determining the most suitable project portfolio, b takes advantageŽ . of the best characteristics of existing methods by decomposing the process into a flexible and logical series of activities and applying the most appropriate technique s at each stage, and c involves full Ž . Ž . participation by decision makers. This is partly because of the complexities involved in project portfolio selection, as explained before. A few attempts to build integrated support for portfolio selection have been reported 16,23,27 . However, these have been limited and specific to the methods used, rather than providing flexible choices of techniques and interactive system support for users.

In an attempt to overcome these difficulties, we have developed an integrated framework for project portfolio selection, which takes advantage of the best characteristics of some of the existing methods 4 .<sup>w</sup> <sup>x</sup> The proposed framework combines methods, which have a good theoretical base with other methods, which are commonly used because of their desirable decision support characteristics. The framework includes a staged approach, where the most relevant and appropriate methods can be selected by the organization and used at each stage.

To increase the likelihood of user acceptability, we use a decision support approach to project portfolio selection 7,29 . This approach is consistent with<sup>w</sup> <sup>x</sup> the recent shift of researcher interest from solving well-structured problems under often unrealistic assumptions, to developing decision support systems Ž . DSSs that support decision makers in capturing and making explicit their own actual preferences, interacting with them in several steps of decision making <sup>w</sup> <sup>x</sup> 19 . Criteria identified for success in implementing such systems include: a a committed senior execu-Ž . tive sponsor, b carefully defined system require- Ž . ments, c carefully defined information require-Ž . ments, d a team approach to system development, Ž . Ž . Ž . e an evolutionary development approach, and f careful computer hardware and software selection <sup>w</sup> <sup>x</sup> 25 . The framework we propose lends itself to these implementation criteria.

In the following, first we describe the proposed framework briefly. The model, which manages optimization and interaction, among the projects available for the portfolio during on-line decision making, is outlined. Then, in order to demonstrate the potential of the framework, we describe a prototype DSS, called Project Analysis and Selection System PASSŽ . that we developed for this purpose. A set of hypotheses are developed to test PASS usefulness, perceived usefulness and perceived ease of use. The experimental design and results of lab experiments are discussed. We outline implementation requirements and our experience in discussing the system with two high tech companies, and finally some of the additional work needed to address some related and unsolved issues in project portfolio selection.

## 2. A framework for project portfolio selection

Project portfolio selection should be considered as a process that includes several related steps, rather than just evaluating or scoring projects, or solving an optimization problem. The proposed framework consists of discrete stages. Pre-process stages provide high level guidance to the portfolio selection process. These include Strategy DeÕelopment Ždetermination of strategic focus and setting resource constraints ,. and Methodology Selection Žchoosing the techniques to use for portfolio selection . Strategy development. may be carried out at higher managerial levels, since it involves the firm’s strategic direction. Selecting methodologies that suit the project class at hand, the organization’s culture, problem-solving style, and project environment, must also be done in advance of the portfolio selection process.

There are five major process stages in the proposed framework for project portfolio selection. The first three stages pre-screening, individual projectŽ analysis, and screening are off-line activities done. Ž in advance of the management committee meeting normally used for portfolio selection . These can be. accomplished by decision analysts or managers working individually. Pre-screening applies guidelines developed in the strategy development stage to ensure that any project being considered fits the strategic focus of the portfolio, has undergone a preliminary analysis, and has a champion to ensure its implementation if chosen. At the IndiÕidual Project Analysis stage, a common set of parameters, such as net present value, internal rate of return, or weighted score is calculated for each project. During portfolio selection, these parameters allow comparison of projects on a common basis. Finally, during the Screening stage, project attributes from the previous stage are examined to eliminate any project, which do not meet pre-set criteria such as minimum rate of return. The intent of pre-screening and screening stages is to eliminate any obvious non-starter and thus reduce the number of projects to be considered by the committee.

The last two stages optimal portfolio selectionŽ and portfolio adjustment , the major focus of this. paper, can be performed in an on-line session by management decision makers through an appropriate DSS. Selecting project portfolios is commonly carried out by a management committee 12 at regular<sup>w</sup> <sup>x</sup> Ž . e.g. quarterly intervals. At the Optimal Portfolio Selection stage, there may be more than one objective involved, such as maximizing net present value and maximizing estimated score for market suitability. These objectives are first integrated by means of a weighted value function, and reduced to one objective. Then an optimization model is applied that considers resource limitations, timing, project interdependencies, balancing criteria, and other constraints, and maximizes total portfolio benefit. Portfolio Adjustment is the final stage of the process, where decision-makers apply their knowledge and experience to balance and make other adjustments to the portfolio by adding or deleting projects. Once the portfolio has been adjusted, results can be finalized by cycling back to re-calculate portfolio parameters such as project schedules and time-dependent resource requirements. Obviously, in terms of the original problem specification only, adjustments to the initial solution will result in a mathematically suboptimal result. But the adjustment phase allows the consideration of issues and constraints that are difficult for decision-makers to articulate analytically. Thus, since the final solution will be more satisfactory to decision-makers than the initial optimal solution, we could say that they are ‘‘satisficing’’ rather than ‘‘optimizing’’.

In this final stage, the group dynamic among management committee members becomes the governing process, supported by the PASS decision tool. Research has shown that Group Support Systems Ž . GSS , which are DSS applications adapted to group decision making in decision rooms or other synchronous situations, can improve decision quality significantly 20,39 . Although this paper does not <sup>w</sup> <sup>x</sup> address group support by PASS directly, the next step in the evolution of this technology in the support of real business applications will be to test it in a GSS environment.

## 3. Optimal portfolio selection

Optimal portfolio selection is a major stage in the framework. It consists of two phases. The first phase applies only when projects are characterized by multiple objective functions. It is used to integrate the multiple objectives into a single objective function, which represents the relative value of each project, and serves as input to the second phase. If projects have a single objective, such as net present value or expected net present value, this can be input directly into the second phase. When there are multiple objectives, we suggest that the objectives be approximated as additive value functions, using expected values as certainty replacements where necessary for stochastic elements. The decomposition form of such objectives requires the assumption of mutual preference independence. Any related risk characteristics are not discarded, but are carried forward as attributes to be used in balancing portfolio risk in the final adjustment stage.

There are a number of techniques that can be used for multiple objective problems in the first phase of optimal portfolio selection. Linear goal programming is one possibility. However, most projects are characterized by both objective and judgmental criteria, and goal programming is best suited to situations involving objective criteria. Arguably, the most widely used technique for value determination, where there are multiple criteria of both types, is weighted scoring. Here, each criteria is weighted according to its importance, and each candidate project is then scored on each criteria by the decision maker s . TheŽ . sum of the weighted scores for each project is then the relative value of the project. The aspect of this technique, which gives the greatest difficulty, is weight determination. Another technique, which is arguably better at handling the weight determination problem, is the analytical hierarchy process AHP .Ž . In AHP 36 , the criteria are decomposed into a <sup>w</sup> <sup>x</sup> hierarchy and the relative priority or importance of the elements at the bottom level are determined through pair-wise comparison by the decision maker s . These are combined at the next higherŽ . level into relative priorities at that level, until the highest level is reached. A linear model is then derived, and used for weighting the criteria. If there are only a few projects, a pairwise comparison of alternative projects by criteria can be used at this point. However, many portfolio projects involve tens of projects, and the number of pairwise comparisons necessary would rule this out. Instead, the relative value of each project can be determined by using the weights already determined, after scores are supplied for the project on each criteria by the decision maker s . AHP has been implemented in the form ofŽ . a commercial software package called Expert Choice<sup>w</sup>.

The second phase of the optimization process is the application of an optimization model, using the single objective function values derived in phase one. We have chosen a zero–one integer linear programming 0–1 ILP model that maximizes the Ž . overall objective of the portfolio, while satisfying existing constraints. Together with the phase one process, this approach handles a multiple, conflict- Ž . ing goals, b qualitative or judgmental as well as Ž . objective criteria, and c explicit constraints such as Ž . resource limitations and project interdependencies. We have also included the facility to perform portfolio balancing in an interactive manner, to handle non-uniform resource consumption over time, and to select and schedule the optimal set of projects that will maximize overall benefit, based on the relative value of the projects being considered.

The decision variables, objective function, and constraints of the 0–1 ILP model are shown below.

## 3.1. Decision Õariables

The decision variables of the model are defined by:

$$
\begin{array}{r l} X _ {i j} & \\ = \left\{ \begin{array}{l l} 1 & \text { if   project } i \text { is   included   in   the   portfolio   and   starts   in   period } j \\ 0 & \text { otherwise } \end{array} \right. \end{array}
$$

for $i = 1 , \ldots , N ,$ where N is the total number of projects being considered, and $j = 1 , \hdots , T$ , when the planning horizon is divided into T periods.

## 3.2. ObjectiÕe function

The objective function is given by:

$$
\text { Maximize } Z = \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {T} a _ {i} X _ {i j}\tag{1}
$$

where Z is the value function to be maximized, and $a _ { i }$ is the potential benefit from project i.

## 3.3. Constraints

There are a very large set of possible constraints, which can be invoked through constraint equations, including some or all of the following examples 20 :<sup>w</sup> <sup>x</sup>

1. a guarantee that each project, if selected, will not start twice during the planning horizon,

2. maximum expenditures will not exceed specified amounts in each of a set of time periods,

3. other resource demands, such as personnel or facility requirements, must not exceed the amount available in each time period,

4. all of the projects selected must be completed within the planning horizon,

5. precursor projects must be completed before successor projects start,

6. certain projects are mandatory and must be scheduled,

7. only one of several mutually exclusive projects can be chosen.

There are many other types of constraints, which can be added to this model, depending on the situation at hand 21 . Every company using this approach<sup>w</sup> <sup>x</sup> will have its own policies and procedures, and the choice of criteria to use will also depend upon its ability to actually specify the various parameters involved in both the benefit measures and the constraint equations. The model we suggest should be flexible enough to suit the requirements of most companies. Solving the model the company chooses will select and schedule a portfolio of projects that maximizes the total benefit of the portfolio and satisfy any constraint specified. Shadow prices are not applicable in 0–1 ILP models. As an alternative, because of the sensitivity of the optimal solution to the constraint coefficients in integer programming models, the model should be re-solved several times, with slight variations in the coefficients each time, to test model sensitivity to parameters and data before attempting to choose a solution for implementation <sup>w</sup> <sup>x</sup> 2 . We will discuss such a DSS in the following, which implements the optimization and portfolio adjustment stages.

## 4. Project portfolio selection through DSS support

From the foregoing discussion, in all stages of the portfolio selection process, decision makers and analysts should be able to interact with the system since it provides models and data to support the decision process. Provision for continuous interaction between system and decision makers is important because: a it is extremely difficult to formulate ex-Ž . plicitly in advance all of the preferences of the decision makers, b involvement of decision makersŽ . in the solution process indirectly motivates successful implementation of the selected projects, and cŽ . interactive decision making has been accepted as the most appropriate way to obtain the correct preferences of decision makers 31,33 , whether working<sup>w</sup> <sup>x</sup> as individuals or as a group in the context of a GSS <sup>w</sup> <sup>x</sup> <sub>8</sub> <sub>.</sub>

If this interaction is to be supported by a computer-based system, then there is a need for a subsystem to manage the related techniques<sup>r</sup>models, another sub-system to support the data needs of the process, and finally a sub-system that acts as an interface between the decision maker and the system. This is a system, which is equivalent conceptually to a DSS. According to Turban 40 ‘‘A Decision Sup-<sup>w</sup> <sup>x</sup> port System DSS is an interactive, flexible, and Ž . adaptable computer-based information system, specially developed for supporting the solution of a non-structured management problem for improved decision making. It utilizes data, provides an easy-touse interface, and allows for the decision maker’s own insights’’.

A DSS to support the main stages in the framework requires a carefully designed model management module to handle models of the many different types, which may be chosen. Its implementation requires considerations of model representation and integration. Integrated DSS modeling approaches include process integration <sup>w</sup> <sup>x</sup> 17 where heterogeneous models models from different paradigms are to beŽ . integrated. The major issues that arise during process integration are synchronization and Õariable correspondence integration <sup>w</sup> <sup>x</sup> 28 . Synchronization deals with the order in which models must be executed, and timing of dynamic interactions among the models. Variable correspondence deals with input<sup>r</sup>output relationships among the component variables in the various models being used, and assuring dimensional consistency among these variables. In our DSS, models are not executed in parallel. They terminate after transferring their outputs for use by subsequent models, so synchronization is not a critical issue.

To handle variable correspondence, a central database is used. This acts as a data repository, which is open to inspection by users during the portfolio selection process, and as a transfer site to provide matched data for the input and output variables of the various models being used. The database can be updated during the portfolio selection process through direct user input, interactions with associated project databases, and from the outputs of models and their components. Portfolio database updates also include relevant data extracted from other databases that relate to ongoing management of existing projects.

In accordance with the enterprise-wide modelling system suggested by Ba et al. 6 , we have also <sup>w</sup> <sup>x</sup> adopted an approach that allows the use of both quantitative inputs at the optimization stage andŽ .

qualitative judgmental inputs during the portfolioŽ adjustment stage . In addition, we apply their sug- . gested approach of integrating model fragments in-Ž dividual projects in our case to construct a portfolio. model that can be optimized and then adjusted, within given resource and time constraints, to meet overall objectives.

The DSS must also have a user-friendly interface, which hides the complexities of the system and its models from decision-makers, and provides a bridge between users and other components of the DSS. It is used by decision-makers to input data and decisions, to retrieve data from related databases, and to provide direction and control of the system. It also presents the results of computations to users and allows them to interact with the system to arrive at satisfactory solutions.

## 5. Design and implementation of PASS

We developed a prototype DSS called PASS to support decision-makers in project portfolio selection. The conceptual design of this system has been discussed elsewhere 5 . DSS support of project port-<sup>w</sup> <sup>x</sup> folio selection can be divided into off-line and on-line sessions. Decision analysts are the major players in the off-line sessions, where data are gathered, manipulated, and results stored for each project. Tasks such as data entry, pre-screening, individual project evaluation and scoring, screening, and optimization model definition can be performed in off-line sessions, to prepare candidate projects for consideration. Portfolio selection requires that a common set of parameters be generated for all the projects in advance of the selection process, with or without the direct involvement of individual decision-makers. Commercially available software packages such as spreadsheets can be used to support these activities. On-line sessions, involving optimal portfolio selection and portfolio adjustment, are performed directly by committees of decision-makers. The current version of PASS supports decision-makers in on-line sessions.

![](/api/attachments/CAER6KEM/fulltext/images/ed2c150432be766a42db5b658c97d0ba27001070e78049528f54d3ee9b149f7a.jpg)  
Fig. 1. Project portfolio matrix.

PASS initially applies an optimization model to find an optimal solution, which maximizes the benefit s of interest. At the present time, net present Ž . value NPV and Expected NPV ENPV are avail-Ž . Ž . able, but this can be expanded to a variety of benefit measures. Solutions are presented to decision makers in a portfolio matrix display Fig. 1 and used asŽ . starting points for decision makers to reach satisfactory portfolios through interactions with PASS. A portfolio matrix display style is used since it displays the end product of the selection process, and is more understandable by users. There are different types of portfolio matrices that can be used at this stage 12 .<sup>w</sup> <sup>x</sup> PASS also provides decision-makers with a modified Gantt chart that shows a project implementation schedule based on optimization model output.

PASS not only supports the intuition of the decision makers in the process, but it avoids the development of, and direct interaction with, complex models, which are typically developed by decision analysts in advance during off-line sessions. This eliminates a major obstacle that often inhibits managers from using more sophisticated models at the strategic level, and enhances the possibility of system use by higher level managers.

Decision makers, who are active elements in the decision making process, can also use PASS to perform sensitivity analysis in order to examine the robustness of the solution to changes in different variables and parameters. In addition, optimal solutions that are proposed by the system can be modified by adding or dropping different projects to find a more balanced and intuitively satisfactory portfolio. Moreover, PASS allows decision-makers to observe the resulting impact of any proposed change on the optimality of the solution and on the availability of required resources.

During the adjustment stage, PASS prevents decision makers from selecting or de-selecting a project when certain constraints, such as resource limitations or interdependence among projects, are binding the decision maker; the system also provides the user with the necessary feedback in such situations. The final portfolio that decision-makers choose might not be optimal. However, this should not be a critical issue as long as the decision-makers know how far the selected portfolio is from the optimal portfolio initially recommended by the system, and how much of each resource is actually required.

## 6. Effectiveness measures

Sharda et al. 38 provide a good overview of <sup>w</sup> <sup>x</sup> measures of DSS-aided decision performance. These include hard measures such as profit or earnings, and efficiency measures such as time spent in making decisions. Moderators that may affect either efficiency or effectiveness include the number of alternatives generated and the confidence of decisionmakers in their decisions. This paper also included an experimental study of the time dependency of decision quality by groups. Decision quality and number of alternatives examined was compared, between DSS-supported groups and groups that performed manual calculations. However, there are several issues they did not examine. First, they did not apply subjective measures of usability to compare the reactions of the two types of decision groups Ž . manual and DSS supported to the techniques they were using. User-friendliness is of critical importance because ease of use and user acceptance are significant determinants of intention to use a computer technology, and users are not likely to adopt a system unless they perceive it as a useful and easyto-use tool 14,15,32 . Even in mandatory use situa- <sup>w</sup> <sup>x</sup> tions or when there is no other alternative but to use a DSS captive situation , perceived usefulness andŽ . perceived ease of use can enhance user satisfaction <sup>w</sup> <sup>x</sup> <sub>1</sub> <sub>.</sub>

Second, it is important to measure performance with problems of different size. This is an important variable, especially when problems are to be solved by groups of management decision-makers, and meeting time is a very scarce commodity. Larger problems are likely to take much longer to solve manually than with DSS support, directly affecting how many alternative choices can be examined, with a resulting impact on decision quality.

Project portfolio problems, the focus of our study, have their own peculiar characteristics, for which there is little DSS application literature available. These characteristics include the following.

Ž . 1 Problems can be large, complex, and sensitive to variations in parameters such as resource constraints. There are likely to be many alternatives that are close to, if not optimal. Managerial discretion is typically used to choose a final solution, which is more likely to be satisfying than optimal, although the optimal solution can provide a starting point for the investigation.

Ž . 2 Problems differ greatly from one company to another. This emphasizes the importance of the flexible, framework-based approach we suggest 4 , mak-<sup>w</sup> <sup>x</sup> ing it easy to adapt to a particular company’s environment by using different strategies, models, and procedures. To examine adaptability issues, we visited several companies to get their reactions to our approach and to determine if we could meet their needs easily by adapting our model see Section 9 .Ž .

Ž . 3 Portfolio selection problems differ greatly in size, ranging from four or five to hundreds of potential projects. The Sharda et al. study 38 did not find <sup>w</sup> <sup>x</sup> a significant difference in the number of alternatives examined by the DSS-supported and manual groups. Perhaps they would have come to a different conclusion if they had also compared small with large problems.

Clearly, manual approaches are not adequate for exploring alternative solutions for any but the smallest of portfolios, since manual investigations are likely to be too time-consuming for a committee of decision-makers to consider in real time. DSS interface design and usability is critical in such situations, since decision makers need to examine alternative solutions quickly and the results must be presented in an easily understood format. Relevant interface issues are the usability constructs of usefulness and ease of use 34 . Positive user perceptions of these<sup>w</sup> <sup>x</sup> constructs does not necessarily mean that the system helps decision-makers to make better decisions. However, if test results show that users do not perceive a DSS as a useful tool, even if it really offers better solutions, its perceived usefulness needs to be improved. The problem size dimension of portfolio problems also should be examined, to determine user reaction to DSS support for small problems handled with little difficulty manually andŽ . larger problems difficult to consider manually be-Ž cause of calculation time considerations, thus limiting the number of alternatives that can be evaluated ..

## 7. Hypotheses and experimental design

## 7.1. Hypotheses

The following three hypotheses were developed to test the effectiveness of PASS, as well as user perceptions of its usefulness and ease of use. The first hypothesis concerns the improvement of project portfolio decisions when using PASS vs. normal Manual Methods MM . The second and third hy-Ž . potheses examine the perceived usefulness and perceived ease of use of PASS. Davis 14 has devel-<sup>w</sup> <sup>x</sup> oped and validated measurement constructs for perceived usefulness and perceived ease of use, and these constructs were validated later by other researchers 1 . We adapted his questionnaire in our<sup>w</sup> <sup>x</sup> research, with some minor changes.

Hypothesis 1. The use of PASS improÕes the quality of project portfolio selection decisions.

$$
\begin{array}{l} \mathrm{H} _ {0}: \mathrm{PFB} \leq 0. 5 \\ \mathrm{H} _ {1}: \mathrm{PFB} > 0. 5 \end{array}
$$

where PFB is the probability of finding a portfolio with PASS, which is better than the portfolio found by the cc MM . We define a higher quality decision ( ) as selection of a portfolio that: 1 pro( ) Õides more benefits oÕerall, 2 is better balanced, 3 considers( ) ( )

interdependencies among projects, and 4 satisfies( ) resource constraints.

Hypothesis 2. Users perceiÕe PASS as a useful tool for project portfolio selection.

This hypothesis deals with the perceiÕed usefulness of PASS and was tested by the following sub-hypotheses, using responses to questions 1 to 4 in a questionnaire see( Appendix A ..

$\mathrm { H } _ { 2 . 1 } \mathrm { : }$ : PASS helps to accomplish project portfolio selection more quickly than MM.

$\mathrm { H } _ { 2 . 2 }$ : PASS improÕes project portfolio selection decisions.

$\mathrm { H } _ { 2 . 3 } \colon$ PASS makes it easier to do project portfolio selection.

$\mathrm { H } _ { 2 . 4 }$ : OÕerall, PASS is a useful tool for project portfolio selection.

The null and alternatiÕe hypotheses are stated below. A seÕen-point Likert scale was used for measurement in the questionnaire. A score of four, which has been used in the following, indicates the middle ( ) neutral point on each scale, and $M _ { i }$ is the estimated median of responses to question i $( I \leq i \leq 4 )$

$$
\begin{array}{l} \mathrm{H} _ {0} \colon M _ {i} \leq 4 \\ \mathrm{H} _ {1} \colon M _ {i} > 4 \end{array}
$$

Hypothesis 3. Users perceiÕe PASS as an easy-to-use tool.

This hypothesis deals with the perceiÕed ease of use of PASS and was tested by the following six sub-hy potheses using responses to questions 5 to 10 in the questionnaire.

$\mathrm { H } _ { 3 . 1 } \colon$ It was easy to learn PASS.

$\mathrm { H } _ { 3 . 2 } \colon$ It was easy to get PASS to do what I wanted to do.

$\mathrm { H } _ { 3 . 3 } \colon$ PASS was clear and understandable.

$\mathrm { H } _ { 3 . 4 } \mathrm { : }$ PASS was flexible to interact with.

$\mathrm { H } _ { 3 . 5 } \colon$ It would be easy to become skillful at using PASS.

$\mathrm { H } _ { 3 . 6 } \colon$ OÕerall, PASS is easy to use.

The null and alternatiÕe hypotheses are stated below. A score of four indicates the middle point on the scale, and $M _ { i }$ is the estimated median of responses to question $i ( 5 \leq i \leq I O )$ .

$$
\begin{array}{l} \mathrm{H} _ {0} \colon M _ {i} \leq 4 \\ \mathrm{H} _ {1} \colon M _ {i} > 4 \end{array}
$$

We applied tests of these hypotheses to both small and larger problems. We define small problems as problems with five candidate projects or less to beŽ . selected over a time horizon of 10 periods or lessŽ . and larger problems as problems with more than five projects to be selected and scheduled over at least 10 periods.

## 7.2. Experimental design

Two project portfolio cases were developed. The first test case Acme is a small problem in whichŽ . subjects were asked to select a portfolio from a list of four candidate projects and schedule them within a 10-period time horizon. The second case MerrittŽ . is a larger problem in which subjects were asked to select a portfolio from a list of 12 candidate projects and schedule them within a 10-period time horizon. Since the solution space for project portfolio selection problems is usually huge, finding the optimal solution manually can be difficult. For example, since in the Merritt Case, the number of projects and periods is 12 and 10 successively, and since each project can be selected or not selected in each period, the number of possible combinations is 2<sup>120</sup>. It should be noted that, due to real world considerations, the number of alternative solutions is usually much less, but a large solution space still must be searched in order to find the global optimal solution. For example, if we impose a constraint related to project length, where projects must be completed during the planning horizon, the number of feasible solutions reduces to $\Pi _ { i = 1 } ^ { N } ( T - D _ { i } + 2 )$ where N and T are the total number of projects and periods, respectively, and $D _ { i }$ is the duration of project i.

Due to the size of the solution space in project portfolio selection problems, although PASS can easily solve larger and more complex problems, in this experiment we simplified the cases to reduce frustration of subjects when solving the problem. For example, in the larger problem Merritt , a company Ž . wants to select a portfolio of projects from a list of 12 candidate projects and schedule them within a 10-period time horizon to maximize the total benefits. Some of the major issues that the company needs to address include: 1 total and periodic bud-Ž . get limitations, 2 balancing the portfolio in terms of Ž . risk and time to complete the company does notŽ want too much investment in high risk or long term projects , 3 some projects are interdependent, 4 . Ž . Ž . projects selected must be able to be completed by the end of the 10-period plan, and 5 projects, once Ž . started, cannot be interrupted. Many other types of issues might exist in a real case that can be addressed by adding appropriate sets of constraints to the optimization model.

The objective of developing these cases was to have one relatively straightforward portfolio problem Ž . Ž . Acme and one more complex one Merritt , to compare the quality of manual vs. PASS solutions for two quite different problems. In all cases, subjects solved the case manually first, and then solved it with the help of PASS, to avoid biasing the results obtained in the manual part of the test towards the optimal PASS solutions. The subjects who received the Acme case were expected to solve it in about 20 min and those who received the Merritt case, in about 40 min. These timings were not rigidly enforced and subjects could keep working on their cases as long as they felt comfortable in continuing. After using PASS to obtain the optimal solution, the subjects performed a sensitivity analysis with PASS by increasing financial resources by 10%. They also changed the balancing criteria and observed the impact of such changes on the optimal solution. The time taken by PASS to generate a solution on a 150-Mhz Pentium<sup>w</sup> laptop computer was 5 and 8 s for the Acme and Merritt cases, respectively.

To reduce learning effects, and also to prepare the subjects for the test, we developed a simple case Ž . ABC , which consisted of three candidate projects that could be selected and scheduled within a 10- period time horizon, with few constraints. Solving this case with both the MM and PASS helped the subjects to learn both methods before undertaking their assigned tasks.

Some participants, due to past experience, might have been more familiar with project selection and scheduling problems and the heuristics that could be applied for these kinds of problems than others. To decrease the impact of this potential difference among participants, a sheet was given to each subject, which contained some heuristics for manually solving the case. The use of these heuristics was not mandatory and subjects could use any MM they found to be useful.

In order to collect data on the variables of interest during the test, a test data sheet and a questionnaire Ž . see Appendix A were developed. The test data sheet gathered data about the solution that subjects found by using the MM. The questionnaire, which was filled out by subjects at the end of the test, contained questions that measured different aspects of user perception of usefulness and ease of use. The questionnaire contained 10 questions where user perceptions were measured on a seven-point Likert scale in which 1 means ‘‘strongly disagree’’, and 7 means ‘‘strongly agree’’.

## 8. Experimental results

A pilot test was conducted with seven subjects to collect some initial data and to identify and correct potential problems in PASS, the test procedure and questionnaire, and to finalize the hypotheses before embarking on the full-scale test. The pilot test helped us to modify and improve the experimental design and interface as well as the hypotheses. A full-scale test was conducted with 26 third- and fourth-year Commerce undergraduate volunteers. All had completed introductory micro-economics and finance courses. The Acme and Merritt cases were randomly assigned to individual participating subjects; each case was assigned to 13 subjects. Subjects first solved the case that was assigned to them manually to find a portfolio, from the candidate projects, that maximized the net present value NPV of the portfolioŽ . while satisfying all of the existing constraints. Information that was required, such as project characteristics and existing constraints for example, financial Ž constraints, balancing criteria, and project interdependencies was provided with the case. After solv- . ing their assigned cases manually, subjects then used PASS to find the optimal solutions to the identical problems, using data that had previously been input to the computer. Comparisons between the manual and PASS solutions were made on the basis of these results, and subject perceptions of usefulness and ease of use, based on their experiences with the two approaches, were collected through the questionnaire shown in Appendix A. The results of the tests are described below.

## 8.1. Data consistency test

The reliability of responses to the questionnaire was evaluated with the Cronbach 13 alpha test. <sup>w</sup> <sup>x</sup> Reliability assesses the internal consistency of the data; that is, how consistently individuals responded to questions. For perceived usefulness, the Cronbach alpha was 0.67, and for perceived ease of use, it was 0.81. A reliability score of 0.6 is considered acceptable 35 . <sup>w</sup> <sup>x</sup>

## 8.2. Data analysis

The three hypotheses were examined, for small and larger problems, respectively. In order to test each hypothesis, its sub-hypotheses were examined to see how well they supported the main hypothesis.

Hypothesis 1 was analyzed using quantitative data collected during the test. Since a yes<sup>r</sup>no nominal scale was used for measurement, the Binomial test was used.

## 8.2.1. Test results for the small problem

Of the 13 subjects, two found infeasible solutions and only one subject found the optimal solution. Thus, in 12 of 13 cases PASS found a better portfolio than the MM to the problem as initially stated. Fig. 2 shows the distribution of the feasible solutions found by subjects in comparison with the optimal solution. Five subjects found feasible solutions that were less than 1% below the optimal PASS solution. The test result for Hypothesis 1 for the small problem was highly significant $( \boldsymbol { p } = 0 . 0 0 2 )$ . The null hypothesis was rejected and we can conclude that for the small problem ‘‘The use of PASS improves the quality of project portfolio selection decisions’’.

![](/api/attachments/CAER6KEM/fulltext/images/3a028dc5d67898ea74d831edfd5700409ac33f85aa6a23e8d4c709e853d8610c.jpg)  
Fig. 2. Manual solutions for the small problem.

![](/api/attachments/CAER6KEM/fulltext/images/3352622158194f2a1abdee7746cf3283197e71e56ac7af9fd80bbed93e23a604.jpg)  
Fig. 3. Manual solutions for the larger problem.

## 8.2.2. Test results for the larger problem

Of the 13 subjects, three found infeasible solutions and only three found the optimal solution. Thus, in 10 of 13 cases PASS found a better portfolio than the MM to the problem as initially stated. Fig. 3 shows the distribution of the feasible solutions found by subjects in comparison with the optimal PASS solution. Six subjects found feasible solutions that were less than 1% below the optimal solution. The Binomial test result for Hypothesis 1 for the larger problem was significant $( \boldsymbol { p } = 0 . 0 4 6 )$ . The null hypothesis was rejected and so we can conclude that for the larger problem ‘‘The use of PASS improves the quality of project portfolio selection decisions’’.

In comparing the results from the two problem sizes, we had anticipated that users would have more difficulty in manually achieving optimal or near-optimal results for the larger problem than for the smaller one. Surprisingly, there was no qualitative difference between results from the two types of problems.

Hypothesis 2 was examined by four sub-hypotheses using the answers to questions 1 to 4, using the Median test.

## 8.2.3. Test results for the small problem

The statistical results for all of the first three sub-hypotheses were very significant $( p = 0 . 0 0 )$ . The null hypotheses for these questions were rejected. As a result, we can conclude that for the small problem ‘‘Users perceive PASS as a useful tool for project portfolio selection’’. This conclusion was also strongly supported by the result $( p = 0 . 0 0 )$ for subhypothesis $\mathrm { H } _ { 2 . 4 }$ that claims ‘‘Overall, PASS is a useful tool for project portfolio selection’’.

## 8.2.4. Test results for the larger problem

The statistical results for all of the first three sub-hypotheses were very significant $( p = 0 . 0 0 )$ . The null hypotheses for these questions were rejected. As a result, we can conclude that for the larger problem ‘‘Users perceive PASS as a useful tool for project portfolio selection’’. This conclusion is also strongly supported by the result $( p = 0 . 0 0 )$ for sub-hypothesis $\mathrm { H } _ { 2 . 4 }$ that claims ‘‘Overall, PASS is a useful tool for project portfolio selection’’.

Hypothesis 3 was examined by six sub-hypotheses using the answers to questions 5 to 10 in the questionnaire, with the Median test.

## 8.2.5. Test results for the small problem

The statistical results for all of the first five sub-hypotheses were very significant $( p = 0 . 0 0 )$ . The null hypotheses for these questions were rejected. As a result, we can conclude that for the small problem ‘‘Users perceive PASS as an easy to use tool for project portfolio selection’’. This conclusion was also strongly supported by the result $( p = 0 . 0 0 )$ for sub-hypothesis $\mathrm { H } _ { 3 . 6 }$ that claims ‘‘Overall, PASS is easy to use’’.

## 8.2.6. Test results for the larger problem

The statistical results for all of the first three sub-hypotheses were very significant $( p = 0 . 0 0 )$ . The null hypotheses for these questions were rejected. As a result, we can conclude that for the larger problem ‘‘Users perceive PASS as an easy to use tool for project portfolio selection’’. This conclusion was also strongly supported by the result $( p = 0 . 0 0 )$ for sub-hypothesis $\mathrm { H } _ { 3 . 6 }$ that claims ‘‘Overall, PASS is easy to use’’.

## 9. Discussion

In this paper, we proposed a framework for project portfolio selection. The proposed framework combines methods that are well grounded in theory with those that are easy to understand, and applies them in a logical manner. It also allows a choice of techniques by decision makers. Our approach is not intended to prescribe a certain portfolio, but rather to assist decision makers to find a satisfactory portfolio, which is close to or at optimality, but at the same time satisfies any resource constraints that have been imposed.

The implementation of the framework in our PASS DSS gave an opportunity for a limited test of the on-line portion of the framework. Although the test results suggest that PASS is a useful tool, users will not adopt and use PASS unless they perceiÕe it as a useful and easy to use tool. Our test results strongly supported the hypothesis that ‘‘users perceive PASS as a useful tool for project portfolio selection’’ in both the small and the larger problems. Moreover, the test results strongly supported the hypothesis that ‘‘Users perceive PASS as an easy to use tool’’ in both small and the larger problems’’. These two fundamental determinants of user acceptance show the high potential of using PASS in practical situations. Since solving problems without violating constraints would seem to be less difficult in smaller problems, we expected more subjects to find optimal or close to optimal solutions in the small problem case. Surprisingly, this did not happen, but to obtain an appropriate interpretation of these results would require additional experiments with a spectrum of problem sizes and constraint numbers and values. This was beyond the scope of our study.

Due to human limitations in handling larger and more sophisticated problems we expect even better support for this hypothesis in real world problems, since they are typically larger and more complex than the simplified example cases developed for this experiment. For example, since both of the cases used for the test Acme and Merritt were intention-Ž . ally simplified to prevent subject frustration at the outset, six subjects in each of the two cases were able to find a portfolio that was only 2% below the optimal solution. Although these results are acceptable in practical situations considering that many of Ž the model parameters, such as NPV, are based on uncertain estimates , typical real world problems are . not as small and simple as the cases developed for this test. As the number of projects or periods increases, the solution space grows exponentially ad-Ž dition of only one project or one time period doubles the solution space , and addition of real world con-. straints such as having more than one limited re-Ž source, more than one project interdependency, and so on makes real problems much more complex. As . a result we do not expect as many people to find the optimal or close to optimal portfolios in a real environment as they did in this experiment with the simplified cases.

An additional effect in real world situation is the need to re-calculate solutions each time portfolio adjustments are made, so the impact of adjustments can be estimated. The same issue applies when decision makers want to perform sensitivity analysis to investigate the impact of changes in certain parameters such as balancing criteria on the solution Ž . and on the availability of resources which can also Ž be varied during sensitivity studies . Clearly, this. would be impractical if manual calculations had to be re-done at each iteration, because of the long time delays involved. The time taken for PASS to solve a case is relatively small only a few seconds in theŽ cases we studied , allowing more time to study . important sensitivity and balance issues, by making adjustments to the portfolio chosen or by changing resource or financial constraints.

In terms of potential success of PASS in a real implementation environment 25 , we note that the<sup>w</sup> <sup>x</sup> system is based on a framework that supports a flexible team approach to system development and use, since users can choose their own methodologies for preparing project parameters and setting constraints. It is also evolutionary, allowing models to be developed across the range of the simple to the complex, as the decision makers wish. Ease of use is critical for executive users, and response time is fast. Successful application depends upon careful choice of both the data to use and the methodologies with which to analyze the data, and these are open to the users. Satisfying these criteria fits four of the six success factors noted for decision support by Houdeshel and Watson 25 the other two are a <sup>w</sup> <sup>x</sup> Ž committed senior executive sponsor and careful computer software and hardware selection, not examined in this study ..

To examine the potential for applying the proposed framework and the PASS DSS in practical situations, we demonstrated PASS for two high-tech companies. These meetings were very useful and the participants were very supportive and enthusiastic about using the proposed framework and PASS. Officials in both firms raised major concerns and problems that they had with project portfolio selection. These are discussed briefly below, with proposed solutions arising from our framework and the PASS DSS.

The department with whom we met in company A was an internal support organization, which needed to select the best projects from among about 200 candidate projects. Because of the large number of projects, the pre-screening and screening stages in our framework would be useful in reducing the number of projects by eliminating from consideration any that clearly would not be appropriate to consider in the on-line stages. Some other problems in this organization, and how they could be resolved by using our framework and DSS included the following.

Ž .i There were candidate projects from more than one major category e.g. customer requests, internal Ž projects, etc. with different objectives for each cate- . gory. A solution would be to use overall importance weights derived for each category, and weights for attributes within each category. These could be derived off-line using an interactive procedure such as the Analytic Hierarchy Process 22,36 . These<sup>w</sup> <sup>x</sup> weights could then be used interactively to calculate the relative value of projects across all the categories, for input to the optimization stage of the on-line selection process.

Ž . ii The department had limited human expertise, with the added complication of interdependencies created by the fact that some of their workers had expertise in more than one area. These interactions can be resolved by including additional constraint equations in the optimization model. Suppose the company has three types of experts, each with different expertise: a Expertise A: can only perform job Ž . 1, b Expertise B: can only perform job 2, and c Ž . Ž . Expertise C: can perform both jobs 1 and 2. Each of these types of expertise can be considered as a scarce resource and more constraints can be added to the model, to handle these resource interdependencies. For example, if the company has only 100 h per month available from each of the three types of expertise, the following sets of constraints would address this issue:

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {k} \operatorname{RA} (i, k + 1 - j) X _ {i, j} \leq 2 0 0
$$

$$
\text { for } k = 1, \dots T\tag{2}
$$

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {k} \mathrm{RB} (i, k + 1 - j) X _ {i, j} \leq 2 0 0
$$

$$
\mathrm{for} k = 1, \ldots T\tag{3}
$$

$$
\sum_ {i = 1} ^ {n} \sum_ {i = j = 1} ^ {k} \mathrm{RA} (i, k + 1 - j) X _ {i, j} + \mathrm{RB} (i) X _ {i, k + 1 - j}
$$

$$
\begin{array}{c} \leq 3 0 0 \\ \text { for } k = 1, \ldots T \end{array}\tag{4}
$$

where ${ \mathrm { R A } } ( i , k + 1 - j ) , { \mathrm { R B } } ( i , k + 1 - j )$ are respectively the amount of expertise A and B, required by project i in period k, N is the total number of projects being considered, and T is the last period in the planning horizon. $X _ { i , j } ,$ the decision variable, is 1 if project i is selected to start in period j and is 0 otherwise.

Company B had two departments new productŽ research, and development , each with up to 12. product development projects underway at any time. A major concern was to achieve a balance among the projects included in each portfolio. Adding a constraint to the optimization model similar to those,Ž which can be used to maintain portfolio balance in terms of risk and duration would maintain the re-. quired balance between the portfolios. Obviously, this balance could be adjusted interactively by adding or deleting specific projects during the on-line adjustment stage. Other problems identified were as follows.

Ž .i An important requirement was to select previously specified mandatory projects and projects already started, and to ensure that ongoing projects ‘‘started’’ at time zero. This requires that ongoing projects be identified during data entry, and also displayed in a special manner by altering the interface iconic display. To ensure that ongoing projects start at time zero, the following constraint equations could be added to the optimization model.

$$
\sum_ {j = 1} ^ {T} X _ {i 1} = 1
$$

for $i \in S _ { 0 }$ where $S _ { 0 }$ is the set of ongoing projects.

Ž . 5

Ž . ii For certain special projects, the company needed to establish completion dates to meet delivery schedules. Adding the following constraint equations to the model would ensure that such projects, if selected, would be scheduled for completion before the due date. This was, of course, subject to the provision that it was feasible to do so within the time constraint.

$$
\sum_ {j = 1} ^ {L _ {1}} j X _ {i j} + D _ {i} \leq L _ {i} + 1 \quad \text { for } i \in S _ {\mathrm{f}}\tag{6}
$$

where $S _ { \mathrm { f } }$ is the set of projects that should be finished before their delivery time $L _ { i } ,$ and $D _ { i }$ is the duration of project i.

These solutions can be implemented easily within the proposed framework and DSS. This demonstrates the importance of the flexibility of the proposed framework in a real working environment, where there is no way to predict in advance all possible problems.

Additional research is needed to extend our work. For example, the proposed approach takes uncertainty and risk into consideration but it assumes that these parameters can be estimated accurately. However, risk estimation is a challenging task and more research is required to find suitable methods for evaluating project risks and their impact on portfolio selection. Depending on the type of application at hand and decision maker preferences about items to be balanced in the selected portfolio, different types of portfolio matrix displays can be provided. Research is required to find the most appropriate portfolio matrices to use for information display in the adjustment stage of the proposed framework.

There are other important issues as well, such as representativeness of the displayed information, that should be taken into consideration. These may at times conflict with user friendliness of the system.

For example, although the use of circles in displays to represent certain aspects of a project, such as its benefit, seems to be very suitable, some researchers contend that circles cause the decision makers to overvalue or undervalue the amounts that are represented 9 . This issue requires further research. Fi-<sup>w</sup> <sup>x</sup> nally, in most situations, a committee of decision makers makes portfolio selection decisions. Decision makers may often disagree in such situations and the DSS should provide support for reaching a consensus. This will also require adjusting the PASS concept to a group support system environment.

## 10. Uncited references

<sup>w</sup> <sup>x</sup> <sub>11</sub> <sup>w</sup> <sup>x</sup> <sub>33</sub>

## Acknowledgements

This research was supported by a grant from the Innovation Research Centre, Michael G. DeGroote School of Business, McMaster University.

## Appendix A

<table><tr><td rowspan="2"></td><td colspan="5">Strongly Disagree</td><td colspan="2">Strongly Agree</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1. PASS helps to accomplish project portfolio selection more quickly......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>2. PASS improves project portfolio selection decisions......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>3. PASS makes it easier to accomplish project portfolio selection......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>4. Overall, PASS is a useful tool for project portfolio selection......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>5. It is easy to learn PASS......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>6. It is easy to get PASS to do what I wanted to do......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>7. PASS is clear and understandable......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>8. PASS is flexible to interact with......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>9. It would be easy for me to become skillful at using PASS......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>10. Overall, PASS is easy to use......</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 D.A. Adams, R.R. Nelson, P.A. Todd, Perceived usefulness, ease of use, and usage of information technology: a replication, MIS Quarterly 1992 227–247, June 1992 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 D.R. Anderson, D.J. Sweeney, T.A. Williams, An Introduction to Management Science: Quantitative Approaches to Decision Making, West Publishing, New York, 1994.

<sup>w</sup> <sup>x</sup> 3 N.P. Archer, F. Ghasemzadeh, Portfolio selection techniques:

A review and a suggested integrated approach, Innovation Ž Research Center Working Paper 46, School of Business, McMaster University, Hamilton, ON, 1996 ..

<sup>w</sup> <sup>x</sup> 4 N.P. Archer, F. Ghasemzadeh, A decision support system for project portfolio selection, International Journal of Technology Management 16 1 ŽŽ .. Ž . <sup>r</sup>2<sup>r</sup>3 1998 105–114.

<sup>w</sup> <sup>x</sup> 5 N.P. Archer, F. Ghasemzadeh, An integrated framework for project portfolio selection, International Journal of Project Management 17 4 1999 207–216. Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 S. Ba, K.R. Lang, A.B. Whinston, Enterprise decision support using intranet technology, Decision Support Systems 20 Ž . 1997 99–134.

<sup>w</sup> <sup>x</sup> 7 J.F. Bard, R. Balachandra, P.E. Kaufman, An interactive approach to R&D project selection and termination, IEEE Transactions on Engineering Management 35 1988 139–Ž . 146.

<sup>w</sup> <sup>x</sup> 8 R.O. Briggs, J.F. Nunamaker Jr., R.H. Sprague Jr., 1001 unanswered research questions in GSS, Journal of Management Information Systems 14 3 1997Ž . Ž . <sup>r</sup>98 3–21.

<sup>w</sup> <sup>x</sup> 9 S.W. Clevel, R. McGill, Graphical perception: theory, experimentation, and application to the development of graphical methods, Journal of the American Statistical Association 79 Ž .1984 .

<sup>w</sup> <sup>x</sup> 10 R.G. Cooper, Winning At New Products, Addison-Wesley, Reading, MA, 1993.

<sup>w</sup> <sup>x</sup> 11 R.G. Cooper, S.J. Edgett, E.J. Kleinschmidt, Portfolio management in new products: lessons from the leaders-I, Research Technology Management 40 5 1997 16–28, Sep.–Ž . Ž . Ž Oct., 1997 ..

<sup>w</sup> <sup>x</sup>12 R.G. Cooper, S.J. Edgett, E.J. Kleinschmidt, Portfolio Management for New Products, Addison-Wesley, Reading, MA, 1998.

<sup>w</sup> <sup>x</sup> 13 L.J. Cronbach, Coefficient alpha and the internal consistency of tests, Psychometrika 16 1951 297–334.Ž .

<sup>w</sup> <sup>x</sup> 14 F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly Ž . Ž . 1989 319–340, Sept. 1989 .

<sup>w</sup> <sup>x</sup> 15 F. Davis, R. Bagozzi, P. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 8 1989 982–1003.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 A. De Maio, R. Verganti, M. Corso, A multi-project management framework for new product development, European Journal of Operational Research 78 1994 178–191.Ž .

<sup>w</sup> <sup>x</sup> 17 D.R. Dolk, J.E. Kottemann, Model integration and a theory of models, Decision Support Systems 9 1993 51–63.Ž .

<sup>w</sup> <sup>x</sup> 18 B.L. Dos Santos, Proceedings of the Hawaii Conference on System Sciences, Selecting information system projects: problems, solutions and challenges 1989 1131–1140.Ž .

<sup>w</sup> <sup>x</sup> 19 J.S. Dyer, P.C. Fishburn, J. Wallenius, S. Zionts, Multiple criteria decision making, multi attribute utility theory: the next ten years, Management Science 38 5 1992 645–654.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 J. Fjermestad, S.R. Hiltz, An assessment of group support systems experiment research: methodology and results, Journal of Management Information Systems 15 3 1998–1999Ž . Ž . 7–149.

<sup>w</sup> <sup>x</sup> 21 F. Ghasemzadeh, N.P. Archer, P. Iyogun, A zero–one ILP model for project portfolio selection and scheduling, Journal of the Operational Research Society 50 1999 745–755.Ž .

<sup>w</sup> <sup>x</sup> 22 B.L. Golden, E.A. Wasil, D.E. Levy, Applications of the analytic hierarchy process: a categorized, annotated bibliography, in: B.L. Golden, E.A. Wasil, P.T. Harker Eds. , TheŽ . Analytic Hierarchy Process: Applications and Studies,1989, pp. 37–58.

<sup>w</sup> <sup>x</sup> 23 D.L. Hall, A. Nauda, An interactive approach for selecting IR&D projects, IEEE Transactions on Engineering Management 37 2 1990 126–133.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 S.W. Hess, Swinging on the branch of a tree: project selection applications, Interfaces 23 6 1993 5–12.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 G. Houdeshel, H.J. Watson, The management information and decision support MIDS system at Lockheed, Georgia,Ž . MIS Quarterly 11 1 1987 March 1987 .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 B. Jackson, Decision methods for selecting a portfolio of R&D projects, Research Management 1983 21–26, Sep.– Ž . Ž Oct. 1983 ..

<sup>w</sup> <sup>x</sup> 27 D.S. Kira, M.I. Kusy, D.H. Murray, B.J. Goranson, A Specific Decision Support System SDSS to develop an optimalŽ . project portfolio mix under uncertainty, IEEE Transactions On Engineering Management 37 3 1990 213–221.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 J.E. Kottemann, D.R. Dolk, Model integration and modeling languages: a process perspective, Information Systems Research 3 1 1992 1–16.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 M.L. Liberatore, G.J. Titus, The practice of management science in R&D project selection, Management Science 29 Ž .1983 962–974.

<sup>w</sup> <sup>x</sup> 30 H.C. Lucas, Computer-Based Information Systems in Organizations, Science Research Associates, Chicago, IL, 1973.

<sup>w</sup> <sup>x</sup> 31 R.G. Mathieu, J.E. Gibson, A methodology for large scale R&D planning based on cluster analysis, IEEE Transactions On Engineering Management 30 3 1993 283–291. Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 G.C. Moore, I. Benbasat, The development of an instrument to measure the perceived characteristics of adopting an information technology innovation, Information Systems Research 2 3 1991 192–222.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 K. Mukherjee, Application of an interactive method for MOLIP in project selection decision: a case from Indian coal mining industry, International Journal of Production Economics 36 1994 203–211.Ž .

<sup>w</sup> <sup>x</sup> 34 J. Nielsen, Usability Engineering, Academic Press, Boston, MA, 1993.

<sup>w</sup> <sup>x</sup> 35 J. Nunnally, Psychometric Theory, McGraw-Hill, New York, NY, 1967.

<sup>w</sup> <sup>x</sup> 36 T.L. Saaty, P.C. Rogers, Ricardo Pell, Portfolio selection through hierarchies, The Journal of Portfolio Management 6 Ž . Ž . 3 1980 16–21.

<sup>w</sup> <sup>x</sup> 37 M. Schniederjans, R. Santhanam, A multi-objective constrained resource information system project selection method, European Journal of Operational Research 70 1993Ž . 244–253.

<sup>w</sup> <sup>x</sup> 38 R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Management Science 34 2 1988 139–159.Ž . Ž .

<sup>w</sup> <sup>x</sup> 39 M.M. Shepherd, R.O. Briggs, B.A. Reinig, J. Yen, J.F. Nunamaker Jr., Invoking social comparison to improve electronic brainstorming: beyond anonymity, Journal of Management Information Systems 12 3 1995–1996 155–170.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 E. Turban, Decision Support and Expert Systems, 4th edn., Prentice-Hall, Englewood Cliffs, NJ, 1995.
