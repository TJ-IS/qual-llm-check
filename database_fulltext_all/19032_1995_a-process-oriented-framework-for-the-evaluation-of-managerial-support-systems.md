---
otero_id: 19032
otero_key: "6HAQJGA7"
title: "A process-oriented framework for the evaluation of managerial support systems"
authors: "Rudolf Vetschera; Heinz Walterscheid"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00039-l"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# A process-oriented framework for the evaluation of managerial support systems

Rudolf Vetschera, Heinz Walterscheid

Faculty of Economics and Statistics, University of Konstanz, P.O. Box 5560 D130, D-78434 Konstanz, Germany

## Abstract

A new method of evaluating the benefits of decision-oriented information systems is proposed. This method is based on a detailed analysis of decision processes. Using prescriptive decision theory, correct results are established for different sub-phases of the process and possible deviations from these results are analyzed. Systems are then evaluated according to their contribution to the elimination of such errors.

Keywords: Decision support systems; Evaluation; Decision processes; Fault trees

## 1. Introduction

Information systems (IS) are evolving to support increasingly complex, unstructured decision tasks. Decision Support Systems [29], Expert Information Systems and Intelligent Decision Systems [22] are gaining importance in practice and research. In this paper, we use the term “Managerial Support System” (MSS) for any kind of IS aiding non-trivial managerial problem-solving. With the development of MSS, the problem of evaluating and justifying IS is becoming more complex and unstructured.

The problem of evaluating MSS and especially of measuring their benefits was recognized in the early literature on DSS [28]. Process-oriented methods form an important branch of this research. These methods try to evaluate the benefits of an MSS in terms of its impact upon the decision process of the manager. However, this approach leaves one question open: Is the change induced by an MSS actually beneficial? Systems built from a “directed change” perspective [56] are designed to enforce a structure of the decision process; since the change is based on a normative process model, one can argue that it is by definition beneficial. However, an evaluation methodology must go one step further and determine whether the system actually achieves the desired changes to the decision process. The situation is even more complicated with systems not trying to enforce a defined process structure. Here, changes in the decision process must be inferred from system characteristics and then evaluated according to a standard provided by the evaluation method.

## 2. An overview of MSS evaluation methodology

In recent years, many methods have been developed for the evaluation of MSS. For previous reviews of research in this field, see e.g. [1,45]. One group of methods is based on traditional cost-benefit analysis [31]. They utilize capital budgeting techniques, such as the payback method, accounting rate of return, net present value or internal rate of return. These methods interpret MSS as investments to achieve monetary goals. This emphasis constitutes both the strengths and weaknesses of traditional cost-benefit analyses. On the one hand, these goals are directly related to the goal system of business users of MSS. On the other hand, the relevant cash outflows and inflows of a project must be determined in order to apply cost-benefit analysis.

The identification and accounting of all MSS cash outflows (e.g. for hardware, software, and personnel) is often difficult or impossible. However, the determination of MSS cash inflows is still more difficult: only a few benefits are directly measurable in monetary terms (e.g. cost savings). Other MSS benefits can only be assigned a monetary value by means of subjective evaluation or indirect methods. For example, productivity increases, arising from the introduction of information systems, can be measured by the hedonic wage model $[49,50,60]$ . Increased productivity is, however, only a small part of the benefits usually claimed by the advocates of MSS. Most other benefits, such as a better understanding of the problem, improved communication, or better control of the decision process, are intangible. Since these benefits must be considered by an adequate MSS evaluation method, cost-benefit analysis, in its standard form, is not regarded as suitable for the evaluation of MSS $[35,42]$ .

Therefore, modifications to cost-benefit analysis have been proposed. They compare the net costs (minus monetary benefits) to the remaining benefits. The best known method is Value Analysis [28], which consists of the following steps:

1. Establish the benefits the system must achieve and determine the maximum cost to obtain those benefits.

2. Build an MSS prototype and assess its benefits and costs.

3. If accepted, establish the cost of a new version, determine its benefit-threshold and build it. If not, abandon the project.

4. Iterate until a satisfactory version is reached. According to [59], Value Analysis differs in three ways from traditional cost-benefit analysis:

\- MSS are interpreted as an R&D effort rather than as a capital investment.

\- MSS benefits are considered first and costs second.

\- The risk of failure is reduced through prototyping.

This approach can be characterized as “semiformal” [45]. No method is provided by which costs and benefits of the systems at different levels can be specified and evaluated.

Another modification of traditional cost-benefit analysis is the graphical cost-benefit approach of $[54]$ . It presumes that the costs and benefits have already been established and provides a mechanism for establishing trade-offs. The relative importance of factors is taken into account by maximizing the weighted sums of normalized costs and the corresponding benefits. Various ways of normalizing costs are presented and combined with the Eigenvector and utility models, thus considering, in addition, risk and uncertainty. The approach illustrates the great importance of the qualitative benefits of an MSS and is thus a flexible tool, once a measurement of benefits can be established.

However, there is still a lack of focus on value [42]. To evaluate non-monetary benefits of an MSS, four kinds of measures can be used [2,29,59]:

\- Productivity Measures: Evaluation of the impact on decisions.

\- Process Measures: Evaluation of the impact on the decision making process.

\- Perception Measures: Evaluation of the impact on the decision maker.

\- Product Measures: Evaluation of the technical merits of the MSS.

Productivity measures are output-oriented and evaluate the effect on decisions: the time and cost of decision-making and implementation and the outcomes. This impact can be studied using microeconomic production theory $[11,43]$ and information economics. It is only applicable to structured decisions and requires the relation between information inputs and decisions to be specified in a closed functional form.

Process measures are based on the traditional definition and objectives of assisting managers in their decision processes. As it is impossible to directly evaluate the impact of an MSS on outputs, it is necessary to examine the process leading to a decision and its changes induced by the MSS.

Perception measures are used to evaluate the decision makers' perception of the MSS in terms of user involvement, control of the process, understanding, etc. Most of the literature pertaining to this approach is reviewed in [61] and [24]. The latter maintain that there is a particular need to develop and validate standard measures for user involvement and satisfaction. For perceived usefulness and ease of use, scales have been developed and validated by [12]. For most other variables, a rigorous conceptual foundation is lacking [32].

Product measures have been developed, among others, by [40], [53] and [36]. They are used to evaluate the technical characteristics of an MSS. Examples are: resource requirements, calculation speed, problem size, response time, availability etc. They are often used as necessary conditions in an MSS selection process. However, technical quality is only one of several prerequisites to support the organization's goals. The extent of support depends also on a variety of non-technical factors.

The four groups of measures are related. Product characteristics influence process measures, because the support provided to different phases of the decision process depends upon the technical capabilities of the system. Outcome-oriented measures describe the results of the decision process. The perception a user has depends on how the system affects the decision process. Process-oriented measures are particularly well-suited as the basis for an evaluation methodology because they:

\- closely relate to and can be used as proxy measures for productivity- and perception-related measures;

\- can also be connected to product-oriented measures by considering system features as inputs;

\- can be more easily established than measures which directly relate to outputs.

Despite the importance of the decision process in the classical MSS papers, only a few authors have considered this approach in detail [62]. The first step towards a process-oriented evaluation methodology was made by [48]. They propose a graphical value-price gap analysis based on a two-dimensional classification scheme for MSS. One dimension consists of the three main phases of decision processes (intelligence, design, choice) proposed by [57] and introduced as a category for the classification of decision support by [37]. The second dimension combines the degree of decision structure, level of management activity, degree of uncertainty and source of information used. For systems supporting the intelligence phase of “class 3” decisions (highly unstructured, top management level, uncertainty, internal and external sources of information) traditional cost-benefit analysis should be employed. For systems supporting the choice phase of “class 1” decisions (opposite of above), value-based methods are more appropriate.

[63] found several contradictions and weaknesses in this framework. They reject equating the intangibility of benefits to the term “value-price gap” and argue that the true relationship between the phases of a decision process and the intangibility of MSS benefits is exactly the opposite, i.e. that MSS used for the intelligence phase of class 3 decisions have the highest intangibility of benefits. They also find Simon’s scheme unsuitable for a clear-cut classification of MSS, because usually more than one decision phase is supported.

The process-oriented method developed by [1] can be used as an ex-ante selection tool or ex-post evaluation tool. A detailed model of the decision process, similar to [41], is established and the relationships between development tools and support provided to process phases are analyzed. The model was validated by a questionnaire sent to users of two leading model-oriented MSS generators. Support provided by the systems considered was much better for the choice/selection phase than for intelligence/identification.

A similar approach was taken by [9] in a review of software packages supporting decision analysis. He proposes an evaluation structure with the three main criteria: performance, user friendliness, and cost. The subcriteria used to evaluate performance are process-oriented and based on Simon's decision elements.

![](/api/attachments/6HAQJGA7/fulltext/images/79fbf64091138df63405db07163db526b6f977127342efc9f8b656f49ee2a594.jpg)  
Fig. 1. Overall framework for MSS evaluation

## 3. A process-oriented evaluation model

Figure 1 presents our overall framework for evaluating MSS: the decision process performed by the user results in a decision, i.e. a course of action being taken, and this leads to certain results. The decision process is influenced by various features of the system under evaluation. The relationship between the decision process and system features corresponds to the three-tiered scheme for describing DSS proposed by [55]. To link the features of the system to changes in the results of the organization using the system, the evaluation methodology needs to trace the effects of the system through all stages.

In order to evaluate an MSS, we firstly have to evaluate the decision process it induces. A “good” decision process is one that leads to “good” decisions, which in turn produce “good” outcomes. Our evaluation methodology is therefore not based on the structure of the decision process itself or its elements, but rather on the outcomes of the process and its individual steps. Evaluating a decision process by analyzing the outcomes of its phases, rather than by looking at the actions performed within the phases, also has the advantage that the definition of a “good” decision process can be based on theoretical concepts. Prescriptive decision theory provides an axiomatic definition of rational decision making in various contexts against which the outcomes of a given decision process can be measured.

![](/api/attachments/6HAQJGA7/fulltext/images/df4ea6a7fbdc17c0f99d276e4b425fca351b4bf65d35573f0800f3021b42ceeb.jpg)  
Fig. 2. MSS evaluation based on comparing actual and ideal decision processes

One cannot expect actual decision processes, whether supported by an MSS or not, to lead to exactly the results required by prescriptive decision theory. To measure the impact of an MSS upon the decision process, further steps are needed. When two decision processes are compared, one is better than the other if it is more likely to produce a result closer to that from prescriptive decision theory. The purpose of an MSS can therefore be seen as reducing the possibilities of “errors” (in the broadest sense), that would cause a process to generate incorrect results.

The specific view underlying our methodology is shown in Figure 2. Actual decision processes will usually be different from and produce different results to an “ideal” decision process. The methodology proceeds by analyzing potential errors, i.e. differences between the results of the two processes and their possible sources in the individual stages. The features of an MSS are then evaluated according to their ability to reduce the probabilities of errors.

## 4. Components of the evaluation model

In order to perform this analysis, we break down the process into distinct phases, thus facilitating the establishment and analysis of prescriptively correct results.

## 4.1. Decision process

In the literature, several models of the decision process have been proposed, starting with the work of Simon [57], who structured a decision process into the phases of intelligence, design and choice. For our purpose, we use an extension of this framework based on [41]. An overview of this model is given in Figure 3. For the purpose of this evaluation, it is not necessary that the activities be carried out in some specific order, they can even be carried out simultaneously.

Following prescriptive decision theory, we distinguish between control space, i.e. the variables under control of the decision maker, goal space (the criteria used in evaluating different courses of action) and value space, in which the individual preferences of the decision maker are taken into account.

![](/api/attachments/6HAQJGA7/fulltext/images/a3ab9a7c8458b1084cdd009a4c249b06a85dfe85c2c811ff4aff0896c0187449.jpg)  
Fig. 3. Overview of the decision process model

In the intelligence phase, a problem is identified. We separate it into recognition, where a problem is detected by observing symptoms (e.g. a difference between observed and planned data) and diagnosis, in which the precise nature of the problem is identified. Recognition is carried out entirely in goal space. In diagnosis, relevant decision variables pertaining to the problem are identified, linking goal space to control space.

During the design phase, possible courses of action are generated. This phase takes place exclusively in control space. Each candidate solution corresponds to a set of values for the decision variables. We further distinguish between the search for existing solutions, e.g. those previously employed in solving similar problems, and the development of new solutions, i.e. combinations of values of decision variables not considered before.

The structure of the choice phase of our process model is closely based upon the structure imposed by prescriptive decision theory. Most of this phase takes place in goal and value space. In transformation, the plans of action developed in the design phase are evaluated according to their contribution to the goals. In screening, inefficient alternatives are eliminated. This operation can be performed in goal space. During evaluation, the alternatives are mapped into value space, where the actual selection takes place. Finally, sensitivity analysis spans all three spaces involved.

4.2. Normative results, deviations and system characteristics

## Intelligence phase

The goal of the intelligence phase is to indicate whether a decision problem actually exists and to classify it. This phase has no corresponding element in prescriptive decision theory. Nevertheless, our analysis will take into account the requirements of prescriptive decision theory for the following phases, e.g. the completeness of alternatives.

The output of the recognition phase is a single binary value: whether a problem warranting further consideration exists or not. Two errors can therefore be made during this phase: an actual problem is not recognized or a problem is seen where none exists.

In order to estimate the possible influence of an MSS upon these error probabilities in more detail, the recognition phase must be further structured. A managerial problem can be defined as a significant deviation between planned and realized values in important goals. The decision maker (or the support system) therefore must perform the following steps:

1. Obtain the planned values.

2a. Obtain actual values or

2b. Forecast future values.

3. Compare planned and actual/forecast values.

4. Establish the significance of the difference.

These steps, in turn, can be decomposed into elementary tasks like obtaining a specific value of a variable. A detailed analysis is shown in section 5.

Diagnosis deals with the specific classification of the problem, e.g. is it a production problem or a marketing problem? We can characterize a problem class by the subsets of control, goal and value spaces, to which the problem relates. The output of diagnosis is a subset of control space, i.e. the variables to change in order to correct the problem.

Again, two possibilities for errors exist: a relevant variable in control space can be overlooked (e.g. a problem is considered as a capacity problem in production, but the possibility of obtaining a needed part from an external supplier is overlooked) or an irrelevant variable is included in the analysis. The task of a support system here, is to help the decision maker identify relevant relationships between variables in control space and their effects in goal space.

## Design phase

The output of the design phase consists of a set of decision alternatives, either previous solutions that have been retrieved or new solutions. These actions take place entirely in control space.

Prescriptive decision theory poses the requirement to generate an “exhaustive list of exclusive decisions” [38]. The set of alternatives should therefore have two properties:

\- It should be complete, for practical purposes, it should contain as many relevant decision alternatives as possible.

\- The alternatives should be mutually exclusive, exactly one has to be selected.

The recognition of alternatives in the design phase can fail in two ways: important alternatives are not recognized or alternatives are proposed which cannot be implemented. The design phase is performed strictly in control space. Therefore, questions of effectiveness of alternatives, which would require a mapping from control space into goal space, are not relevant here. Even if we only consider control space, we have to take into account the possibility of constraints that must be fulfilled. In the second kind of error, such constraints are violated. If previous (successful) solutions are retrieved, they were feasible at the time of their first use. A violation can then only occur if either the evaluation of the proposed decision against the constraints or the constraints themselves have changed. The function of an MSS, in this case, is to alert the user to such changes. For newly generated alternatives, the MSS should support the user in evaluating them with respect to constraints. Figure 4 presents a fault tree [47] which develops the possible sources of error in the design phase and also relates possible errors to system capabilities. Error nodes are represented by white rectangles, system capabilities influencing the likelihood of such errors, are represented by rounded boxes.

Four examples of system capabilities are shown that influence the error scenario: database capabilities, allowing access to internal data of the organization, can aid the decision maker in retrieving existing solutions. Similarly, access to external databases might help the decision maker to identify solutions developed elsewhere, that can be applied. The development of new solutions is supported by external databases and creativity enhancing techniques such as morphological boxes. The creation of infeasible alternatives can be avoided by analytical capabilities for modelling and analysis.

![](/api/attachments/6HAQJGA7/fulltext/images/78868d95d87bb007d955bc446c7e8dfc1bfe648b076d9f74a6798715e631bcb9.jpg)  
Fig. 4. Fault tree for the design phase

Table 1  
Sub-phases of the choice phase and their results

<table><tr><td>Sub-phase</td><td>Results</td></tr><tr><td>Transformation</td><td>Outcomes of the decision alternatives with respect to the goals of the decision maker, possibly in the form of probability distributions.</td></tr><tr><td>Screening</td><td>Subset of efficient alternatives</td></tr><tr><td>Evaluation</td><td>Description of the decision maker&#x27;s preferences</td></tr><tr><td>Selection</td><td>Optimal alternative, taking into account the data and the decision maker&#x27;s preferences</td></tr><tr><td>Sensitivity Analysis</td><td>Information about the stability of the results</td></tr></table>

## Choice phase

The structure of the choice phase is more complex than the others. Table 1 provides an overview of the results that each of these subphases should generate, according to prescriptive decision theory.

Transformation. During transformation, the consequences of the decision alternatives are evaluated. In the language of prescriptive decision theory, this task corresponds to the construction of a decision matrix, which should contain an evaluation of each decision alternative for all goals of the decision maker. If the outcomes depend on uncertain states, each such result is a probability distribution.

For the estimation of the consequences of a decision alternative, two kinds of analyses must be performed. Future external events must be forecast and their interaction with the decision alternative must be modelled. A wide range of computerized methods for forecasting and evaluation can be used. However, it is difficult to analyze in general which properties of an MSS influence the quality of the output. Specific techniques for forecasting and analysis, like time series analysis or discrete event simulation models, might be extremely beneficial for one kind of problem and completely useless for another. The corresponding system features can therefore only be evaluated within a specific context.

![](/api/attachments/6HAQJGA7/fulltext/images/533bb6b24b439639efa91a3b4398d82c1dba9932b0e055c7088505c0009a0b38.jpg)  
Fig. 5. Fault tree for the screening phase

Screening. Here, clearly inferior alternatives are discarded. Prescriptive decision theory requires the elimination of dominated alternatives for which another alternative exists, that is as good in all criteria and strictly better in at least one criterion.

There are two possible deviations: the elimination of alternatives that are not dominated and the failure to eliminate dominated ones. The first error is more severe, because the optimal alternative could be eliminated. If, on the other hand, dominated alternatives remain, the effort to carry out the subsequent steps will be greater, but the result will not be affected.

A fault tree is given in Figure 5. Two system capabilities are important in reducing these types of error: analytical capabilities help to identify possible dominance relations between alternatives and database capabilities can be used to correctly apply the dominance relations.

Evaluation and selection. In evaluation, alternatives are mapped from goal space into value space by taking the decision maker's preferences into account. A number of software packages have been developed for preference estimation $[23,25,30,69]$ and also for the entire estimation and choice process $[16,20,39,65,68]$ . For a survey of these software packages see e.g. $[4,9,18]$ .

Empirical research has identified a number of biases [17] by which actual behavior deviates from the prescriptive theory. The purpose of an MSS in the evaluation and selection phases can be seen in reducing these biases [70], although few systems are designed in a way that explicitly tries to avoid such problems. If the system is not designed to counterbalance bias phenomena, it is even possible that its use will increase the possibility or extent of a bias [33].

![](/api/attachments/6HAQJGA7/fulltext/images/1d808952950f0b45d1a67e994cfbf6609e5ff55bd539803cd17b16cb26a8ed70.jpg)  
Fig. 6. Fault tree for sensitivity analysis

A major problem here is the methodological variety of approaches. Since no methodology is universally accepted, no theoretically correct result can be given. Within the framework of one methodology, however, the evaluation of a system's features, with respect to the elimination of errors, is possible, but no general description of errors can be given.

Sensitivity analysis. The purpose of a final sensitivity analysis is to determine the robustness of a decision against changes in assumptions and parameters. The results can have an immediate impact upon the solution chosen, when an optimal, but highly sensitive solution is replaced by a more robust alternative with slightly worse performance. However, even if sensitivity analysis does not have an immediate effect upon the outcome, it might have an influence on the implementation phase. For example, stricter control might be exercised when implementing a sensitive solution.

Again, two errors can occur: a solution which is robust can be classified as sensitive and vice versa. In sensitivity analysis, changes in the outcomes are related to possible changes in parameters. Errors can therefore be traced back to misjudgements in these two changes, as shown in Figure 6.

## 4.3. Synthesis

A set of extended fault trees makes it possible to relate features of the MSS to possible improvements in the decision process. This relation is at first established at the bottom level of each fault tree and is then only qualitative. In order to establish a final evaluation, two further steps are necessary:

![](/api/attachments/6HAQJGA7/fulltext/images/1d63c49594beef6a6e38ee48ca6c9e906c2b9ea0009d42f6ddc395af545885b1.jpg)  
Fig. 7. Fault tree for the problem recognition phase

1. The relations must be quantified.

2. An aggregation has to be performed, first across the fault trees for each phase of the decision process and then across the phases of the process.

In technical risk analysis, fault trees are evaluated using standard rules of probability theory: the probability of an error at the top level is derived from the individual probabilities of errors at the lower levels, taking into account possible correlations between them. This approach is not feasible here, since it would require unavailable information (the relative frequency of errors and quantitative, probability-based evaluations of the effects of MSS upon these errors). Eventually, this information could be obtained from empirical studies. Up to now, empirical studies, e.g. [27], provide only qualitative guidelines. Therefore, a different methodology must be used for aggregation, which can build upon this weaker information.

We propose to view the aggregation process as a multi-criteria decision problem. The use of several such methods has been proposed in the literature for selection problems in information technology, most notably the Analytic Hierarchy Process of Saaty [19,44,51]. Other methods include multi-attribute utility theory [8]; goal programming and related methods [26,34,67], or screening methods [36].

These and similar methods (for a survey see e.g. [66]) allow aggregation of evaluations in several criteria to provide an overall evaluation. The importance of the different criteria is represented by parameters of the decision methods such as criteria weights or aspiration levels.

While the importance of the phases for the quality of the entire process cannot be measured in an entirely objective way, some aspects can be assessed objectively. By analyzing the existing decision process and its shortcomings, phases can be identified for which support is especially important.

## 5. Example: the problem recognition phase

In this section, we will demonstrate a more detailed analysis, which actually links observable features of a system to decision behavior. As an example, we use the problem recognition phase and concentrate on system features relating to user interface design.

Figure 7 shows a section of a detailed fault tree for the problem recognition phase corresponding to the error of overlooking a deviation of planned and actual values. This error can be made during comparison, retrieving data, or forecasting. Failure to obtain the correct values can be caused by a deficiency in the system's database, making data unavailable or irretrievable, or by a problem in the user interface, so that the user does obtain the correct values. Errors in comparison can be alleviated by automated comparison methods and by a user interface that simplifies this task.

Table 2  
Empirical results to evaluate user interfaces

<table><tr><td>Feature</td><td>Identification of patterns/trends</td><td>Retrieval of values</td><td>Comparison</td><td>Recall</td><td>Structuring</td></tr><tr><td>Tables</td><td>[6], [14], [10], [27], [58], [13]</td><td>[5], [6], [14], [27], [10], [58]</td><td>[5], [10], [27]</td><td>[14], [58]</td><td>[21], [46],</td></tr><tr><td>Bar charts</td><td>[27], [10], [13], [58]</td><td>[14], [10], [58]</td><td>[10], [27]</td><td>[14], [64], [58]</td><td></td></tr><tr><td>Line charts</td><td>[14], [6], [27], [58], [10]</td><td>[14], [6], [58], [10], [5]</td><td>[27], [10], [5]</td><td>[14], [58]</td><td></td></tr><tr><td>Pie charts</td><td>[58]</td><td>[58]</td><td>[27]</td><td></td><td></td></tr><tr><td>3D charts</td><td>[10]</td><td>[10]</td><td>[10]</td><td></td><td></td></tr><tr><td>Graphs in General</td><td>[27]</td><td>[27]</td><td>[27]</td><td></td><td></td></tr><tr><td>Integration of graphs and tables</td><td>[6], [13]</td><td>[6]</td><td></td><td></td><td></td></tr><tr><td>Color graphics</td><td>[6]</td><td></td><td></td><td></td><td></td></tr><tr><td>Hierarchical Structuring</td><td></td><td></td><td></td><td></td><td>[21], [46]</td></tr></table>

If forecasts are made using a model-based method, the system's ability to support the structuring task of model formulation, as well as to perform the required calculations and to retrieve the necessary inputs (possibly from external databases) are of importance. For intuitive forecasts, it is important to support the user in identifying trends or development patterns of variables over time and in obtaining exact values for making numerical forecasts.

The user interface is important for correctly performing several sub-tasks related to problem identification. These include the (precise) retrieval of single values, the recognition of patterns and trends, comparisons between values and patterns, recall of values and developments and structuring tasks. The effects of various design parameters in the user interface, most notably the use of graphics, have been the subject of considerable empirical research. Table 2 lists several empirical studies relating the efficiency and quality with which these sub-tasks are performed to user interface features, such as the types of graphs used, table formats, the use of color etc. It should be noted that this table contains studies with both positive and negative results concerning the suitability of a representation format for a given task. In most cases, this is also influenced by other context variables. It is therefore not possible to identify a “good” user interface for a given task in general terms. However, in the context of evaluating a specific MSS design in a specific environment, empirical evidence makes it possible to evaluate the features of the MSS in question. For example, consider the sub-problem of identifying trends for extrapolation in intuitive forecasting. If we have to compare a system design which presents data in tabular form, with a system providing line graphs, the studies listed in the appropriate fields of table 2 indicate that for many users, line graphs will lead to better results. In this way, it is possible to relate system features to the overall quality of decisions and thus to estimate the decision quality effect of an MSS.

## 6. Conclusions and topics for further research

We introduced a new methodology to evaluate the “soft” benefits of MSS based on several features that distinguish it from existing approaches:

\- It uses a prescriptive view of the results from different stages in the decision process.

\- It evaluates changes to the process induced by an MSS in terms of deviations from the pre-scriptively correct results.

\- It provides a framework for incorporating empirical research in various aspects of system design into the evaluation process.

Only a broad overview of our methodology has been given. For real applications, the analysis must be carried out at all stages of the decision process with finer detail. There is also a need for more empirical analysis, both in the construction of fault trees and in determining the effects of system characteristics on potential errors. The area of user interface design has been studied quite intensively in the literature. Except for some empirical studies on analytical features and models $[3,7,52]$ and their user interface $[15]$ , other areas have received considerably less attention in the literature. Our framework provides an indication of areas in which empirical research is most needed.

## References

[1] D.A. Adams, J.F. Courtney Jr. and G.M. Kasper. "A process-oriented method for the evaluation of decision support system generators." Information and Management. 19: 213–225, 1990.

[2] J. Akoka. "A Framework for Decision Support Systems Evaluation." Information and Management. 4: 133–141, 1981.

[3] R.J. Aldag and D.J. Power. "An Empirical Assessment of Computer-Assisted Decision Analysis." Decision Sciences. 17: 572-588, 1986.

[4] S. Barba-Romero. A Comparative Review of Discrete MCDM Software. 1990.

[5] I. Benbasat and A.S. Dexter. "An Experimental Evaluation of Graphical and Color-Enhanced Information Presentation." Management Science. 31: 1348–1364, 1985.

[6] I. Benbasat, A.S. Dexter and P. Todd. "An Experimental Program Investigating Color-Enhanced and Graphical Information Presentation: An Integration of the Findings." Communications of the ACM. 29: 1094–1105, 1986.

[7] I. Benbasat and B.F. Nault. "An Evaluation of Empirical Research in Managerial Support Systems." Decision Support Systems. 6: 203–226, 1990.

[8] D.G. Brooks and C.W. Kirkwood. "Decision Analysis to Select a Microcomputer Networking Strategy: A Procedure and a Case Study." Journal of the Operational Research Society. 39: 23-32, 1988.

[9] D.M. Buede. “Superior Design Features of Decision Analytic Software.” Computers and Operations Research. 19: 43–57, 1992.

[10] J.G. Casali and K.B. Gaylin. “Selected graph design variables in four interpretation tasks: a microcomputer-based pilot study.” Behaviour and Information Technology. 7: 31–49, 1988.

[11] R.B. Cooper. "Decision Production - A Step Toward a Theory of Managerial Information Requirements." Proceedings of the Fourth International Conference on Information Systems. 1983 Houston, Texas.

[12] F.D. Davis. "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology." MIS Quarterly. 13: 318–340, 1989.

[13] G. DeSanctis and S.L. Jarvenpaa. "Graphical Presentation of Accounting Data for Financial Forecasting: An Experimental Investigation." Accounting Organizations and Society. 14: 509–525, 1989.

[14] G.W. Dickson, G. DeSanctis and D.J. McBride. "Understanding the Effectiveness of Computer Graphics for Decision Support. A Cumulative Experimental Approach." Communications of the ACM. 29: 40–47, 1986.

[15] B.L. Dos Santos and M.L. Bariff. "A Study of User Interface Aids for Model-Oriented Decision Support Systems." Management Science. 34: 461–468, 1988.

[16] Expert Choice Inc. "Expert Choice Reference Manual." 1990 Pittsburgh.

[17] J.M. Fraser, P.J. Smith and J.W. Smith Jr. "A catalog of errors." International Journal of Man-Machine Studies. 37: 265–307, 1992.

[18] B.L. Golden, A. Hevner and D. Power. "Decision insight systems for microcomputers: a critical evaluation." Computers and Operations Research. 13: 287-300, 1986.

[19] B.L. Golden and E.A. Wasil. “Nonlinear Programming on a Microcomputer.” Computers and Operations Research. 13: 149–166, 1986.

[20] R.P. Hämäläinen and H. Lauri. HIPRE 3 + User's Guide. 1992.

[21] J. Hauschildt. “Graphische Unterstützung der Informationssuche - Eine experimentelle Effizienzprüfung.” Information und Wirtschaftlichkeit. Wissenschaftliche Tagung des Verbandes der Hochschullehrer für Betriebswirtschaft e.V. an der Universität Hannover 1985. Ballwieser and Berger ed. 1986 Gabler. Wiesbaden.

[22] S. Holtzman. “Intelligent Decision Systems.” The Teknowledge Series in Knowledge Engineering. Hayes-Roth ed. 1989 Addison-Wesley. Reading, Mass.

[23] P. Humphreys and A. Wishuda. Multi Attribute Utility Decomposition. MAUD - An interactive computer program for the structuring, decomposition and recomposition of preferences between multi-attributed alternatives. 1979.

[24] B. Ives and M.H. Olson. "User Involvement and MIS Success: A Review of Research." Management Science. 30: 586–603, 1984.

[25] E. Jacquet-Lagreze and J. Siskos. “Assessing a set of additive utility functions for multicriteria decision-making, the UTA method.” European Journal of Operational Research. 10: 151–164, 1982.

[26] H.K. Jain and A. Dutta. "Distributed Computer System Design: A Multicriteria Decision-Making Methodology." Decision Sciences. 17: 437-453, 1986.

[27] S.L. Jarvenpaa and G.W. Dickson. "Graphics and Managerial Decision Making: Research Based Guidelines." Communications of the ACM. 31: 764–774, 1988.

[28] P.G.W. Keen. "Value Analysis: Justifying Decision Support Systems." MIS Quarterly. 5: 1–15, 1981.

[29] P.G.W. Keen and M.S. Scott Morton. "Decision Support Systems: An Organizational Perspective." 1978 Addison-Wesley. Reading, Mass.

[30] S.O. Kimbrough and M. Weber. "An Empirical Comparison of Utility Assessment Programs." European Journal of Operational Research. 75: 617-633, 1994.

[31] J.L. King and E.L. Schrems. "Cost-Benefit Analysis in Information Systems Development and Operation." ACM Computing Surveys. 10: 19-34, 1978.

[32] K. Klenke. “Construct Measurement in Management Information Systems: A Review and Critique of User Satisfaction and User Involvement Instruments.” INFOR. 30:325–348, 1992.

[33] C.T. Kydd. “Cognitive Biases in the Use of Computer-Based Decision Support Systems.” Omega. 17: 335–344, 1989.

[34] K.D. Lawrence, S.M. Lawrence and R.A. Marose. "A Multiple Goal Portfolio Analysis Model for the Selection of MIS Projects." Essays and Surveys on Multiple Criteria Decision Making. Hansen ed. 1983 Springer. Berlin et al.

[35] P.M.W. Lay. "Beware of the Cost/Benefit Model for IS Project Evaluation." Journal of Systems Management. 36: 30–35, 1985.

[36] L.A. Le Blanc and M.T. Jelassi. "DSS Software Selection: A Multiple Criteria Decision Methodology." Information and Management. 17: 49–65, 1989.

[37] F.J. Lerch and M.M. Mantei. "A Framework for Computer Support in Managerial Decision Making." Proceedings of the Fifth International Conference on Information Systems. 1984 Tucson, Arizona.

[38] D.V. Lindley. "Making Decisions." 1985 J. Wiley and Sons. New York.

[39] Logical Decision. "Logical Decision - Multi-Measure Decision Analysis Software." 1989 Point Richmond, CA.

[40] C.L. Meador and R.A. Mezger. "Selecting an End User Programming Language for DSS Development." MIS Quarterly. 8: 267–281, 1984.

[41] H. Mintzberg, D. Raisinghani and A. Theoret. "The Structure of "Unstructured" Decision Processes." Administrative Science Quarterly. 21: 246–275, 1976.

[42] A. Money, D. Tromp and T. Wegner. "The Quantification of Decision Support Benefits within the Context of Value Analysis." MIS Quarterly. 12: 223–236, 1988.

[43] T. Mukhopadhyay and R.B. Cooper. "Impact of Management Information Systems on Decisions." Omega. 20:37–49, 1992.

[44] K. Muralidhar, R. Santhanam and R.L. Wilson. "Using the Analytic Hierarchy Process for Information System Project Selection." Information and Management. 18: 87-95, 1990.

[45] R.M. O'Keefe. "The Evaluation of Decision-Aiding Systems: Guidelines and Methods." Information and Management. 17: 217–226, 1989.

[46] S.C. Palvia and S.R. Gordon. "Tables, Trees and Formulas in Decision Analysis." Communications of the ACM. 35: 104-113, 1992.

[47] M.E. Pate-Cornell. "Fault Trees vs. Event Trees in Reliability Analysis." Risk Analysis. 4: 177-186, 1984.

[48] D.R. Pieptea and E. Anderson. "Price and Value of Decision Support Systems." MIS Quarterly. 11: 515-528, 1987.

[49] S. Rosen. "Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition." Journal of Political Economy. 82: 34–55, 1974.

[50] P.G. Sassone. "Cost-Benefit Methodology for Office Systems." ACM Transactions on Office Information Systems. 5: 273-289, 1987.

[51] M.J. Schniederjans and R.L. Wilson. "Using the analytic hierarchy process and goal programming for information system project selection." Information and Management. 20: 333-342, 1991.

[52] R. Sharda, S.H. Barr and J.C. McDonnell. "Decision Support System Effectiveness: A Review and an Empirical Test." Management Science. 34: 139–159, 1988.

[53] P. Shoval and Y. Lugasi. "Models for Computer System Evaluation and Selection." Information and Management. 12: 117-129, 1987.

[54] P. Shoval and Y. Lugasi. "Computer Systems Selection: The Graphical Cost-Benefit Approach." Information and Management. 15: 163–172, 1988.

[55] M.S. Silver. "Descriptive Analysis for Computer-Based Decision Support." Operations Research. 36: 904–916, 1988.

[56] M.S. Silver. “Decision Support Systems: Directed and Nondirected Change.” Information Systems Research. 1: 47–70, 1990.

[57] H.A. Simon. "The New Science of Management Decision." 1960 Harper and Row. New York.

[58] J.A. Sparrow. “Graphical displays in information systems: some data properties influencing the effectiveness of alternative forms.” Behaviour and Information Technology. 8: 43–56, 1989.

[59] R.H. Sprague Jr. and E.D. Carlson. "Building Effective

Decision Support Systems." 1982 Prentice-Hall. Englewood Cliffs, New Jersey.

[60] E. Stickel. "Eine Erweiterung des hedonistischen Verfahrens zur Ermittlung der Wirtschaftlichkeit des Einsatzes von Informationstechnik." Zeitschrift für Betriebswirtschaft. 62: 743–759, 1992.

[61] E.B. Swanson. "Measuring User Attitudes in MIS Research: a Review." Omega. 10: 157–165, 1982.

[62] P. Todd and I. Benbasat. "Process Tracing Methods in Decision Support Systems Research: Exploring the Black Box." MIS Quarterly. 11: 493-512, 1987.

[63] K.V. Toraskar and P.N. Joglekar. "Comments on "Price and Value of Decision Support Systems"." MIS Quarterly. 14: 7–12, 1990.

[64] N.S. Umanath, R.W. Scamell and S.R. Das. "An Examination of Two Screen Report Design Variables in an Information Recall Context." Decision Sciences. 21: 216-240, 1990.

[65] R. Vetschera. "An Interactive Outranking System for Multi-Attribute Decision Making." Computers and Operations Research. 15: 311–322, 1988.

[66] P. Vincke. "Multicriteria Decision-aid." 1992 J. Wiley and Sons. Chichester.

[67] L. Vlacic, A. Wierzbicki and B. Matic. “Aggregation Procedures for Hierarchically Grouped Decision Attributes with Application to Control System Performance Evaluation.” Recent Advances and Historical Development of Vector Optimization. Jahn and Krabs ed. 1986 Springer. Berlin.

[68] R. von Nitzsch. “Entscheidung bei Zielkonflikten – Ein PC-gestütztes Verfahren.” 1992 Gabler. Wiesbaden.

[69] R. von Nitzsch and M. Weber. "Utility Function Assessment on a Micro-Computer: An Interactive Procedure." Annals of Operations Research. 16: 149–160, 1988.

[70] E.U. Weber and O. Coskunoglu. "Descriptive and Prescriptive Models of Decisionmaking: Implications for the Development of Decision Aids." IEEE Transactions on Systems, Man, and Cybernetics. 20: 310–317, 1990.

![](/api/attachments/6HAQJGA7/fulltext/images/88c9325fa758272e44f9a3d1970d9f9c0871a3df0a458721b8fb3ce894d05f6a.jpg)

Rudolf Vetschera is Full Professor of Management at the University of Konstanz, Germany. He received his degree and PhD. in Economics and Computer Sciences from the University of Vienna, Austria. His research interests are in the fields of decision theory, the conceptual development and implementation of decision support systems and the impact of advanced information technology on organizations. He has published two books and articles in, among others, Decision Support Systems, European Journal of Operations Research, Computers and Operations Research and Journal of Economic Behavior and Organization.

![](/api/attachments/6HAQJGA7/fulltext/images/b607b44d9e397d8d3330d35d0c08650b62ff1c300ffbf30b91c3f6b0ec444502.jpg)

Heinz Walterscheid is a research assistant at the Faculty of Economics and Statistics of the University of Konstanz, Germany. He holds a degree in Economics from the University of Bonn. His current research is focused on methodologies for the evaluation of advanced information systems.
