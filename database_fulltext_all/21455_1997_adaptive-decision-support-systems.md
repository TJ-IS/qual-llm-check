---
otero_id: 21455
otero_key: "U854FAWS"
title: "Adaptive decision support systems"
authors: "Bijan Fazlollahi; Mihir A. Parikh; Sameer Verma"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00014-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adaptive decision support systems

Bijan Fazlollahi $^{*}$ , Mihir A. Parikh, Sameer Verma

Department of Decision Sciences, College of Business Administration, Georgia State University, Atlanta, GA 30303, USA

## Abstract

The effectiveness of decision support systems (DSS) is enhanced through dynamic adaptation of support to the needs of the decision maker, to the problem, and to the decision context. We define this enhanced DSS as adaptive decision support systems (ADSS) and propose its architecture. In an ADSS, the decision maker controls the decision process. However, the system monitors the process to match support to the needs. The proposed architecture evolves from the traditional DSS models and includes an additional intelligent ‘Adaptation’ component. The ‘Adaptation’ component works with the traditional data, model, and interface components to provide adaptive support. The architecture also integrates enhancements proposed in the past research. In this paper, we have illustrated the proposed architecture with two examples, a prototype system, and results from a preliminary empirical investigation. © 1997 Elsevier Science B.V.

Keywords: Decision support systems; Active decision support; Intelligent decision support; Adaptive support; DSS architecture; Cognitive support

## 1. Introduction

Decision support systems (DSS) have benefited from advances in software and hardware technology $[1]$ . The data, model and interface components of DSS are now much more sophisticated and powerful than they were two decades ago. The databases are larger, more current and easier to query and search, the models are more complex reflecting reality, and the interfaces are much more user-friendly. However, the evolution has been in the direction of building a DSS to provide more effective support for the low-level cognitive tasks, such as data storage and retrieval, data drilling, manipulation, and consistency checking $[2]$ . Little has been done in developing DSS that provide support for the high-level cognitive tasks, such as framing of problems, alternative generation $[3]$ , making tradeoffs involved in preferences, and handling incomplete information, misinformation, and uncertainty. These high-level cognitive tasks involve human mental activities of reasoning, learning, and idea generation requiring human judgmental inputs.

A primary objective of DSS is to help the decision maker make effective decisions by identifying what should be done and ensure that the chosen criterion is relevant $[4]$ . The provision of support for the high-level cognitive tasks (i.e., the high-level cognitive support) can strengthen the capabilities for achieving the objective. This type of support extends the limits of ‘bounded’ rationality by promoting improved understanding, better insights, and more extensive analysis $[4–7]$ . The high-level cognitive support is analogous to referring the decision-making tasks to human staff assistants and staff advisors. Normally, a staff assistant makes efforts to understand the changing requirements of the task, the needs of the decision maker, and the best way to support the particular decision maker. For this, the staff assistant constantly monitors the current status of the task, provides interim reports, and is sensitive to the needs and the peculiarities of the decision maker and the context in which the decision is made. The high-level cognitive support adds to the functionality of DSS, especially for situations with complex problems and expert decision makers. As an example of the added functionality, some of the tasks may be delegated to the intelligent agents $[8]$ . The intelligent agents accomplish the tasks on their own initiatives while interacting with the decision maker and the decision environment. However, the agents operate within the user control philosophy of DSS $[9]$ where the decision maker exercises human judgement and provides judgmental inputs.

The purpose of this paper is to propose an enhanced DSS, adaptive decision support system (ADSS), which provides the high-level cognitive support adapted to the needs of the user, the decision task characteristics, and the decision context. The paper reviews past research and discusses ADSS as a prescription to the unaddressed requirements of complex decision-making situations. It proposes an architecture that identifies and incorporates key components for designing and developing an ADSS. It illustrates the architecture through building and using a prototype ADSS including results from a preliminary empirical investigation. Finally, it provides a summary of observations and recommendations for future directions of research in ADSS.

## 2. Background

DSS have evolved to provide more effective support for decision-making. The factors influencing DSS evolution include (1) the discovery of structure in some judgmental tasks and then assigning the task to the computer, and (2) improvements in technology allowing the computer to do more tasks. Keen and Scott Morton as far back as in 1978 foresaw that decision support may be achieved by exploitation of many technologies [4]. Modern database technology, graphical user interface, hypermedia, multimedia, expert systems, neural networks, fuzzy logic, genetic algorithms, distributed systems, client-server, object-oriented approach are examples of recent technologies that can carry out prescriptions that were not feasible in 1978. In recent years, some of the emerging technologies have been used in providing the high-level cognitive support. Research in the area of high-level cognitive support is labeled active decision support, inductive learning, decisional guidance, and adaptive interface.

Manheim and Isenberg [10] suggest active DSS having few features that can provide the high-level cognitive support. These features include: (a) maintaining an explicit representation of the decision maker's conceptual problem-solving model and using it to guide support activities; (b) providing tools for supporting the ‘natural heuristics’, such as ‘do the easy things right away’ as well as tools for rational model-type such as linear programming and break-even analysis model; and (c) providing tools to enhance the user's ability to balance strategic (global and long-term) and opportunistic (local and short term) thinking.

The active DSS are capable of active participation in the decision-making processes. The systems operate almost independent of explicit directions from the users and provide support which the users may find helpful $[11,12]$ . Raghavan $[13]$ identifies support features of the active DSS as monitoring the user activities, making inferences, and conducting appropriate activities such as alerting, engaging in an insightful conversation, or automatically carrying out certain tasks. The active DSS aim at improving the decision-making effectiveness through stimulating creative ideas, criticizing choices, and guiding decision structuring.

The active DSS complement users' problem-solving abilities in the application domain [12]. The DSS use alternative models of the problem-solving processes, ask the users to make choices at the intermediate stages allowing the users to determine the problem-solving paths, and maintain updated models of the user problem-solving processes. They support the users in a number of forms such as suggesting alternative actions and indicating issues that the users may have overlooked. Raghav Rao et al. [12] concludes that the active DSS should be designed as knowledge-based systems.

Piramuthu et al. [14] describes an adaptive DSS for real-time scheduling of a flexible manufacturing system. The DSS dynamically identifies a pattern in the scheduling environment and matches an appropriate scheduling heuristic rule to the task. The system architecture includes a ‘learning and refining’ module capable of simulation and inductive learning for acquisition and refinement of heuristics. The module interacts with the knowledge base to provide adaptive scheduling.

Holsapple et al. [15] describe an adaptive DSS that utilizes unsupervised inductive learning, a learning through observation and discovery, to acquire problem processing knowledge for machine learning. The DSS refines the problem-processing knowledge to match the existing conditions.

Holsapple et al. [15] summarize the relationship among DSS paradigms based on two problem processor-related factors of active/reactive and adaptive/nonadaptive. The traditional DSS are labeled as nonadaptive and reactive. They suggest that the focus of research should be on adaptive and active DSS. These are the systems where problem processors acquire and eliminate knowledge through unsupervised learning and are largely self-driven. The research is concerned more with learning abilities that improve the problem processing behavior of a DSS [15].

Silver [16] proposes ‘decisional guidance’ as an enhancement to the DSS. The decisional guidance enlightens or sways its users as they structure and execute their decision-making processes and provide metasupport for judgmental activities. The guidance is implemented in the form of help facilities [17] or embedded intelligence that inform and advise users. The objective of the decisional guidance is more effective use of DSS leading to more effective decision-making.

Several researchers propose adaptive interface, user-controlled or self-adaptive, to allow for the differences in the users and to enhance DSS quality and effectiveness $[18,19]$ . Adaptability of interface ensures that the system provides flexibility to satisfy the different users' cognitive styles, the users' experience level, and different decision approaches. Thus, adaptable interface allows a DSS to provide ease of learning and user control.

Dutta [20] proposes additional intelligent components to a planning DSS so that the system can adapt to the changing task requirements. He identifies a need for support in monitoring, replanning, and managing interdependencies among different temporally separated actions in the iterative process of planning. The DSS monitors the environment, handles uncertain and incomplete information, and interprets and integrates conflicting output from different models and viewpoints.

Although the enhancements proposed in the past research provide the high-level cognitive support through increased DSS functionalities, the research and development in the area of providing high-level cognitive support is fragmented and technologically oriented. The methodology for providing the support is still in the infant stage $[2]$ . In particular, there are no frameworks to guide the identification of the necessary enhancements and addition of functionalities to the DSS that would provide the high-level cognitive support. In the following section, we propose an ADSS that incorporates different ideas regarding extensions and enhancements to the traditional DSS for providing the high-level cognitive support.

## 3. Adaptive decision support systems

We define ADSS as DSS that support human decision making judgements by adapting support to the high-level cognitive needs of the users, task characteristics, and decision contexts.

ADSS are enhanced DSS with an objective to improve the effectiveness of the decision maker in performing tasks requiring high degree of human judgement such as framing problems, generating alternatives, making tradeoffs, and handling equivocality and uncertainty. ADSS, due to their emphasis on the high-level cognitive support, will also improve user learning and understanding of the decision-making process and the domain knowledge.

ADSS, unlike traditional DSS that are adaptive systems only through evolution $[21]$ , are adaptive through adjustments to the skill level and changing needs of the decision maker during the decision-making process. The decision maker learns through interaction with the ADSS $[4]$ . The learning leads to changes in problem-solving expertise and support needs. ADSS provide support that fits the user's current needs. Also, the progress through the intelligent, design and choice phases in a dynamic decision environment leads to changing problem-solving task. ADSS adapt to the changing problem-solving model and provide support for the appropriate tasks. Furthermore, ADSS adapt to the decision contexts such as organizational structure. For example, a decision in a matrix structure would require more coordination with other decision makers than in a hierarchical structure. In such situations, the support must also provide mechanism for coordination of decisions. Matching support to the decision maker, the decision problem, and the decision context, substantially helps the decision maker to make effective decisions $[4]$ .

Adaptation is achieved by matching support needs with the system support. The support needs of the user are determined by monitoring the user performance and support history. The support needs of the task and the contexts are identified through monitoring the decision process and selecting the appropriate models. ADSS monitor the decision-making process, diagnose problems/opportunities, and design and implement interventions. Such abilities rest on having knowledge of the specific user, the problem domain, an expert model of the decision process, and strategies for intervention. As the support needs change, the systems dynamically change their support to match the current needs. Dynamic adaptation enables ADSS to better address learning, interaction, support, and evolution — the keywords in the DSS definition $[4]$ .

ADSS use intelligent technologies to determine the support needs and may provide an active, rather than a passive participation in the decision-making process $[11]$ . The active participation includes performing tasks such as finding patterns in data, selecting appropriate models, or acting as critiquing agents $[22,8]$ . It further means that the user/DSS interaction (a two-way communication) is established with the decision maker controlling the process, similar to in the case of a decision maker with a human staff assistant.

## 4. ADSS architecture

The architecture of decision support systems was first proposed by Sprague and Carlson $[23]$ as a macro architectural model with three components data, model, and interface. Later, Turban $[24]$ revised this model and added expert systems/knowledge-based component to the model. Other researchers $[20,11,25,10,26,27,19,16,28]$ have proposed enhanced architectures to encompass particular functionalities not specifically identified in the original macro model.

Fig. 1 shows the proposed architecture for ADSS. The architecture is an evolution of the Sprague and Carlson model [23]. In addition to the three; data, model, and interface components, of the traditional DSS, ADSS have an ‘Adaptation’ component. The adaptation component is integrated with the other three components to generate and provide adaptive support.

ADSS have three subsystems: user diagnosis, problem-solving, and guidance/instruction. Each subsystem incorporates data, model and adaptation component. The user diagnosis subsystem includes information regarding what the user knows and what support the system has already communicated to the user. The problem-solving subsystem includes the model derived from a theory or stated by the user for appropriately solving the problem. ADSS do not require the general model of human problem-solving processes to guide their automatic intervention in the decision-making processes. Instead, the more attainable descriptive models of specific tasks are used to guide some of the activities of ADSS. The guidance/instruction subsystem includes knowledge about how to intervene in the decision-making processes. The ADSS architecture addresses the functionalities of ADSS, which are (1) to monitor the decision makers, the decision-making tasks and the decision contexts, (2) to make inferences on the basis of descriptive models, and (3) to intervene at the discretion of the decision maker to provide decision support.

![](/api/attachments/U854FAWS/fulltext/images/38c5cb165ee0599f2cefe8b30d2dc12f8b0539f605c9fa021295da568da7504e.jpg)  
Fig. 1. An architecture of adaptive decision support systems.

Two examples are selected from management science and personal finance domain to explain the architecture. Example A refers to an ADSS used for selecting appropriate forecasting model for a given historical data. This decision-making situation is structured with well-defined statistical models and quantitative methods to identify which forecasting model is more suitable. Example B refers to an ADSS used for determining appropriate allocation of assets for an individual investor. The process of asset allocation is dependent on subjective variables such as the degrees of risk preference, time horizons, and financial conditions of the investor. This decision-making situation is unstructured as there is a lack of quantitative models that incorporate the individual investor's characteristics and concerns in performing asset allocation.

The components of each ADSS are described in details and are illustrated with examples A and B in the following subsections.

## 4.1.Data

This component is similar to the data component of the Sprague and Carlson model $[23]$ . It stores raw data about the problems, the concepts and procedures, and the user history. It has three subcomponents: Problem, concept/procedure, and user history.

## 4.1.1. Problem

This subcomponent stores raw data about the problem or decision at hand. The details of the problem can be obtained from this database and presented to the user of the system. This subcomponent can be an external database dynamically linked to the other components of the system.

<table><tr><td>Example A —</td><td>Domain knowledge: Time-series forecastingModel: Linear forecasting</td></tr><tr><td></td><td>Concepts What a linear forecasting model is; when it should be used; the underlying assumptions of the model; the advantages and disadvantages of using this model.Procedures How to find the coefficients of the independent variables; how to import data into the model.</td></tr></table>

Example A — Problem: Forecasting sales for year 1997

<table><tr><td>Data (historical):</td><td>Year</td><td>Sales</td></tr><tr><td></td><td>1985</td><td>US$5,234,667.00</td></tr><tr><td></td><td>1986</td><td>US$8,342,235.00</td></tr><tr><td></td><td>1995</td><td>US$41,564,982.00</td></tr><tr><td></td><td>1996</td><td>US$59,002,538.00</td></tr></table>

Example B — Problem: Investment asset allocation for a household with four members — husband, wife and two young children.

<table><tr><td colspan="2">Data: Household Income</td><td>US$60,000/yr</td></tr><tr><td rowspan="3">Major expenses</td><td>Rent + utilities</td><td>US$1,000</td></tr><tr><td>Auto loans</td><td>US$600</td></tr><tr><td>Other</td><td>US$2,000</td></tr><tr><td rowspan="3">Major financial goals</td><td>Retirement</td><td>US$400,000 in 30 yr</td></tr><tr><td>Education for the children</td><td>US$50,000 in 14 yr</td></tr><tr><td>Buying a house</td><td>US$25,000 in 2 yr</td></tr></table>

## 4.1.2. Concept / procedure

This subcomponent stores information on the concepts and procedures related to the domain knowledge area. This subcomponent can also be dynamically linked with an external concept/procedure library.

Example B — Domain knowledge: Personal finance and investments
Concepts What stocks, bonds, or money market funds are; what an emergency fund is; what a portfolio is; risk and return of a portfolio.
Procedures How to determine portfolio risk; how to determine portfolio return.

## 4.1.3. User history

Before the user uses the system, the system performs a diagnostic test and determines the knowledge level of the user in the concepts and procedures involved in the decision-making process. These diagnostic data are stored in this component. When the user uses the system, the system continuously monitors actions of the user. This subcomponent stores the sequential historical actions and interactions such as performance of the user, type of help the user requested, and time it took the user to solve the problem.

<table><tr><td colspan="3">Example A — User: Jeff Jones</td></tr><tr><td></td><td>Performance history:</td><td>Outcome Time</td></tr><tr><td></td><td>Problem 1</td><td>Right 5 min</td></tr><tr><td></td><td>Problem 2</td><td>Right 7 min</td></tr><tr><td></td><td>Problem 3</td><td>Wrong 3 min</td></tr><tr><td></td><td>Problem 4</td><td>Right 2 min</td></tr><tr><td></td><td colspan="2">Support history:</td></tr><tr><td></td><td>Concept</td><td>Linear model, Exponential Smoothing model,</td></tr><tr><td></td><td>Procedure</td><td>Doing a square of differences, Finding a coefficient for independent variable.</td></tr><tr><td colspan="3">Example B — Performance history (alternate portfolio developed by the user):</td></tr><tr><td></td><td>Iteration 1</td><td>Stocks-30%, Bonds-20%, Cash-50%</td></tr><tr><td></td><td>Iteration 2</td><td>Stocks-35%, Bonds-35%, Cash-30%</td></tr><tr><td></td><td>Iteration 3</td><td>Stocks-50%, Bonds-40%, Cash-10%</td></tr><tr><td></td><td>Iteration 4</td><td>Stocks-50%, Bonds-30%, Cash-20%</td></tr><tr><td></td><td colspan="2">Support history:</td></tr><tr><td></td><td>Iteration 1</td><td>The user did not ask for support.</td></tr><tr><td></td><td>Iteration 2</td><td>The user asked for support on:</td></tr><tr><td></td><td>Concepts</td><td>Returns on stocks, risk involved in the cash investments</td></tr><tr><td></td><td>Procedure</td><td>How to determine portfolio return</td></tr><tr><td></td><td>Iteration 3</td><td>The user asked for support on:</td></tr><tr><td></td><td>Concepts</td><td>Portfolio evaluation, risk involved in stocks</td></tr><tr><td></td><td>Procedure</td><td>How to determine portfolio risk</td></tr><tr><td></td><td>Iteration 4</td><td>The user did not ask for support.</td></tr></table>

## 4.2. Models

This component stores models and knowledge about problem-solving, guidance/instruction, and user diagnosis in three subcomponents: problem-solving model, guidance/instruction model, and user diagnosis model.

## 4.2.1. Problem-solving model

This subcomponent stores descriptive problem-solving models for different problems. When a problem is presented, this subcomponent has the knowledge and the models for identifying and solving the problem. This subcomponent has two parts: associated concepts and associated procedures. Associated concepts include the models about the identifying concepts involved in solving the problem. Associated procedures have the models about identifying the procedures involved in solving the problem.

Example A:

Associated concept

If the historical data shows a linear trend with no seasonality and low fluctuations, then simple linear regression model should be used.

Associated procedure

To use the linear model: (1) find the coefficient, (2) find the intercept, (3) select a future time period to forecast, and (4) use the developed model to find the new level of the dependent variable for the future time period.

Example B:

Associated concept If the risk preference is high, time horizon is long, and financial condition is stable, allocate a larger part of the portfolio to stocks.

Associated procedure To determine suitability of the portfolio in terms of risk, identify risk preference of the user and match that with the risk of the portfolio.

## 4.2.2. Guidance / instruction model

This subcomponent has models about presentation of the concepts and the procedures. It has models to determine when, how, and at what level a concept or a procedure should be presented.

Example A:

Problem In case of the linear regression model, present the concepts and procedures related only to the linear model and not other forecasting models.

User If the user knowledge is strong in linear model concept, give only brief conceptual information. If the user knowledge is weak in linear model concept, give detailed conceptual information about the model along with examples/nonexamples of the model.

Example B:

Problem In case of the portfolio return, present only the concept and procedures involved in determining portfolio return.

User If the user knowledge is strong in the concept of determining portfolio return but weak in calculating portfolio return, then give brief conceptual information and detailed step-by-step procedure for calculating portfolio return.

## 4.2.3. User diagnosis model

This subcomponent stores information about how to interpret the user history. This subcomponent has models and rules needed to interpret the conceptual and the procedural knowledge levels of the user and determine the level of expertise and support needs.

Example A:

Concepts If the user does not know what a trend is, the difference between high and low fluctuation, and what seasonality is, then the user knowledge in linear model is weak;

If at least two (of the above three) concepts are clear, then the user knowledge in linear model is average;

If all the concepts are clear, then the user knowledge in linear model is strong.

Procedure If historically the user was never able to perform this task, then the user knowledge is weak in finding coefficient of independent variables;

If the user was able to perform the task successfully half of the time, then the user knowledge is average in the procedure;

If the user was able to perform the task successfully most of the time, then the user knowledge is strong in the procedure.

## Example B:

Concepts If the user portfolio does not match with optimal portfolio given user's risk preference, time horizon, and financial condition, he is conceptually weak in understanding one or more of these three dimensions. The degree of weakness can be determined by the size of the difference in the portfolios.

Procedure If the user has never been able to perform the procedure of determining portfolio return, then the user is weak in the procedure.

If the user has determined the portfolio return successfully about half of the time, then the user is average in the procedure.

## 4.3. Adaptation

This component integrates the subcomponents of the data and model components to infer about the adaptive support. The component has three subcomponents: expert problem-solving evaluation, user performance evaluation, and guidance.

## 4.3.1. Expert problem-solving evaluation

This subcomponent represents expert's evaluation of the problem and problem-solving knowledge. It matches the problem subcomponent from the data component and the problem-solving model subcomponent from the model component and determines the concepts and procedures related to the problem. It creates a dynamic task profile of the associated concepts and procedures for solving the given problem. For example,

Let us say, problem T11 is selected from the problem subcomponent of the data component. The expert problem-solving evaluation subcomponent identifies the key features of the problem T11, (such as linear trend, low fluctuations, no seasonality for the example A and low risk preference, short time horizon for the example B). Then, it uses the models from the problem-solving model subcomponent of the model component and determines the associated concepts and the associated procedures as shown below:

Problem T11
Associated concepts C1 and C8
Associated procedures P2, P6, P8 and P14

## 4.3.2. User performance evaluation

This subcomponent evaluates the performance level of the user and develops a dynamic user performance profile for both concepts and procedures. As the user uses the system, the history of interaction is recorded in the user history subcomponent of the data component. The user performance evaluation subcomponent uses the user history and interprets the knowledge of the user based on the user diagnosis knowledge.

For example, let us say the user is Jeff Jones and has used the system for quite sometime and the system has accumulated a history of interaction during this time. The user performance evaluation subcomponent matches the interactions recorded in the user history subcomponent of the data components with the models form the user diagnosis model of the model component. From the comparison it determines a user profile indicating Jeff's degree of knowledge of concepts and procedures as shown below:

User Jeff Jones

Concepts Weak-C1, C3 and C7; Average-C2, C4 and C5; Strong-C6 and C8.

Procedure Weak-P1, P2, P9 and P14; Average-P3, P5, P6, P7, P8, and P10; Strong-P4, P11, P12, and P13.

## 4.3.3. Guidance

This subcomponent compares the task profile from the expert problem-solving evaluation subcomponent with the user profile from the user performance evaluation subcomponent. It compares knowledge required for an associated concept with user's knowledge in the concept and determines the concept differences $(\Delta C)$ . It also compares the proficiency required to preform an associated procedure with the user's proficiency in performing the procedure and determines the procedure differences $(\Delta P)$ . Based on $\Delta C$ and $\Delta P$ , this subcomponent determines which concepts and procedures should be presented and at what level. For example,

Jeff Jones is given the problem T11. This problem has C1 and C8 as associated concepts and P2, P6, P8 and P14 as associated procedures. Jeff is weak in concept C1 and procedures P2 and P14, average in procedures P6 and P8, and strong in concept C8. So, the guidance subcomponent determines to provide Jeff the detailed information along with examples and nonexamples of C1, P2 and P14, the detailed information about P6 and P8, and only the brief information about C8.

<table><tr><td colspan="2">Problem: T11</td></tr><tr><td>Associated concepts</td><td>C1 and C8</td></tr><tr><td>Associated procedures</td><td>P2, P6, P8 and P14</td></tr><tr><td colspan="2">User: Jeff Jones</td></tr><tr><td>Concepts</td><td>Weak-C1, C3 and C7; Average-C2, C4 and C5; Strong-C6 and C8.</td></tr><tr><td>Procedure</td><td>Weak-P1, P2, P9 and P14; Average-P3, P5, P6, P7, P8, and P10;Strong-P4, P11, P12, and P13.</td></tr><tr><td colspan="2">Prescription:</td></tr><tr><td rowspan="2">Concepts</td><td>C1 Detailed information along with examples and nonexamples</td></tr><tr><td>C8 Brief information</td></tr><tr><td rowspan="4">Procedures</td><td>P2 Detailed information along with examples and nonexamples</td></tr><tr><td>P6 Detailed information</td></tr><tr><td>P8 Detailed information</td></tr><tr><td>P14 Detailed information along with examples and nonexamples</td></tr></table>

## 4.4. User interface (dialogue)

The user interface component is the link between the user and the system. This component is the one that is seen and used directly by the user, so the user may think that this is the system. It is a self-adaptive interface that automatically adjusts to the users' preferences and tasks, and provides the functionality and form required to match the interface to a specific user performing a specific task. Self-adaptive interface promotes ease-of-use and consistency of features in the interface that are important factors in establishing usefulness and success of the system.

## 5. ADSS prototype

## 5.1. Problem description

We used the exploratory system development process methodology $[13]$ to investigate the proposed architecture with a prototype system. We selected forecasting, specifically data analysis and model selection, as the area of domain knowledge. In this prototype system, the user is provided with the sales data plotted against time and asked to examine the plot and select the most appropriate forecasting model to predict future sales. The system presents four cases/problems (labeled A, B, C, and D) of sales data, each of the problems requiring different forecasting model. The user examines the cases one at a time in a sequential and irreversible order, and selects an appropriate forecasting model for each case. In solving the problems, the user can access information about the data and the models pertinent to forecasting. The information may help in analyzing the data plot and selecting an appropriate model. In this prototype, the user's history of interactions in solving each case is stored to or retrieved from a database.

## 5.2. Prototype description

We developed the system by mapping the conceptual components of the architecture to different files, programs and other features in KnowledgePro software package. KnowledgePro is an environment that supports rapid prototyping in rule-based programming for expert systems. The software allows reading and writing to a variety of file and graphic formats. An add-on package called KPWIN++ generates C++ code for the KnowledgePro-based programs and compiles them into runtime executable files.

## 5.2.1. Physical representation

As described in the architecture, the system consists of the data, model, adaptation and user interface components. Each component is divided into subcomponents.

Data: This component consists of the problem, the concepts/procedures, and the user history subcomponents. It has data in the form of independent data files and random access memory (temporal data).

Problem: the problem data are loaded by runtime programs from an independent file on a disk. The data are presented to the user in a graphical format (bitmap) as a time series plot which the user has to analyze.

Concept/procedure: the concepts and procedures are assembled in text and graphics formats, in accordance with the problem type and the problem-solving stage requirements. They are stored in files on a disk.

User history: this subcomponent deals with temporal data. However, to maintain a cumulative user profile, the data from the random access memory is dumped to a trace (ASCII text/database) file, after every significant event. This file contains data regarding navigation, time stamping, results, performance, etc. In every new session, the trace file from the previous sessions of the user is accessed to adjust for the previously learned concepts and procedures.

Model: this component consists of rule-based programs (executables), which store the various models used by the system. The model component encapsulates three subcomponents: the problem-solving model, the guidance/instruction model, and the user diagnosis.

Problem-solving model: this subcomponent contains the problem-solving models, represented through associated concepts and associated procedures. We have modeled this knowledge by programming in Knowledge Pro's rule-based expert system shell.

Guidance/instruction model: this subcomponent is represented by the models that determine the format of the presentation of the concepts and procedures that the user may require. The inference is based on the performance of the user.

User diagnosis model: this subcomponent has rules that diagnose and interpret the user history for determining the strengths and weaknesses of the user in the domain knowledge.

## 5.2.2. Adaptation

This component has three subcomponents. All subcomponents are exclusively rule-based. The expert problem/solving evaluation subcomponent associates the problem file name with the problem-solving knowledge rule block. After comparing the problem and the expert's opinion, the subcomponent determines the expert's representation of the required concepts $(C_{\mathrm{E}})$ and the procedures $(P_{\mathrm{E}})$ . The user performance evaluation subcomponent examines user history from the trace file and the user diagnosis knowledge. Using the two, this subcomponent determines the concepts $(C_{\mathrm{U}})$ reviewed and procedure $(P_{\mathrm{U}})$ performed by the user. All these values are stored as temporal data in the RAM. Finally, the guidance subcomponent compares the inferences from the expert problem-solving evaluation subcomponent and the user performance evaluation subcomponent, and generates the deviations for concepts $(\Delta C)$ and procedure $(\Delta P)$ . The guidance subcomponent determines which and in what format the concepts and procedures need to be presented. The concepts and procedures are obtained from the data component's concept/procedure subcomponent, and the presentation format is obtained from the model component's guidance/instruction subcomponent. The system bases its inferences of formats and concepts on the user profile and present user performance ( $\Delta C$ and $\Delta P$ ). In the prototype system, the outcome for each of the four cases can be either right or wrong. Therefore, as more information is gathered, the decision tree develops more branches. As an example, trees for cases A and B are shown in Figs. 2 and 3, respectively.

![](/api/attachments/U854FAWS/fulltext/images/d236d6b923c6fb3cd48cdf3b85dac26710a8f685d9045fd5bab5b9d85e860352.jpg)  
Fig. 2. Decision tree for Case A.

![](/api/attachments/U854FAWS/fulltext/images/f98bf24c81bd7423747a166bbffacdef79d8e785e1a18b44e7de57a424210c61.jpg)  
Fig. 3. Decision tree for Case B.

For case A (Fig. 2), the system uses the user history, which indicates that the user could have been right or wrong about case A type of problems in previous sessions. The outcome here refers to concepts and the format of presentation. Therefore, while the user is in case A, he/she can get one of the two types of outcomes. As the system proceeds to case B (Fig. 3), the user's performance profile has changed. It now consists of not only the performance in previous sessions, but also of the performance on case A. This information is used in conjunction with the user's history. In case B, the outcomes increase to four. This is due to the number of combinations. It must be noted, that the user's performance is a cumulative variable. We have used this approach to decrease the search time for outcomes, and to make the process of concept retrieval and presentation more efficient. Based on the inferences made by the guidance/instruction subcomponent, the concepts are presented to the user through the user interface. Now for case C, we will have updated user history and the performance in case B.

![](/api/attachments/U854FAWS/fulltext/images/a7ffaeb78a8d7cff9af015c2484cf0d8fcd79980d989801c298d24af15d35eb4.jpg)  
Fig. 4. Menu pad.

![](/api/attachments/U854FAWS/fulltext/images/7f668abae0c3059f596d9cc4eb5fa9f78a66ebe6c6efe75be7d915b7bc399de2.jpg)  
Fig. 5. Data plot.

## 5.2.3. User interface

The user interface is designed in Microsoft Windows 3.1. By using windows and buttons, the system provides the ease of navigation. The hypertext is constrained to prevent the user from getting lost in hyperspace. For example, while using the system, only the relevant hot regions are activated. These controls are coded using KnowledgePro's event-based topic controls.

![](/api/attachments/U854FAWS/fulltext/images/ff92094943d743aa067d74b05295710e74436c703a57376bfa9d921d458f0cff.jpg)  
Fig. 6. Guidance screen for Case A.

## 5.2.4. Sample session and explanation

The user begins by registration. Registration allows the system to retrieve the user's history from the database. Then the user is presented with an information screen containing all the relevant and required information for using the system. After reading the instructions, the user continues by clicking on the Continue button. The system is designed to keep control over the decision-making process with the user.

The next screen consists of two windows (shown in Figs. 4 and 5), which show the data plot (Fig. 5) for case A, and a menu pad (Fig. 4) for access to guidance/instruction, and for model selection. The user can click on any of the specific information buttons to get extended guidance/instruction on those models, in the context of the present problem. For example, by clicking on the 'Information' button on 'Least Squares Regression', the information provided consists of textual information on least squares regression, and a suggestion about the data. The screen also displays the current plot. When the user selects the least squares model, the system provides feedback, indicating that the choice was wrong. The system automatically proceeds to case B. This time the user selects information option for Least Squares Regression. The screen looks different this time. This is due to the fact that the user chose the wrong model for case A. Therefore the guidance is more extended. A comparison of the two information screens is shown in the figures for case A and case B.

Comparing Figs. 6 and 7, we see that in addition to the information in Case A (Fig. 6), the figure for case B (Fig. 7) provides a comparison of example and nonexample. The user selects the least squares model this time. The feedback from the system indicates the choice to be correct. The system proceeds to case C (Fig. 8). In C, by clicking on the information option for 'Least Squares', it displays a third format. In this format the information includes three plots illustrating the key factors in forecasting. The reasoning for this format is based on the performance of the user on previous sessions (user history) and the performance on cases A and B (i.e., user history, and present user performance).

The user selects exponential smoothing model. The system indicates that this model is wrong. At this point, the user has two wrong and one correct choice. The system continues to case D (Fig. 9). Finally, case D reveals information on moving average model, which explains the modeling technique, shows a data plot, provides

![](/api/attachments/U854FAWS/fulltext/images/21a7b951351b0c24f06150caa779007c35f65aa7cb76a649f69aa1158f06d8fe.jpg)  
Fig. 7. Guidance screen for Case B.

![](/api/attachments/U854FAWS/fulltext/images/ac65b580a0f3c8e86a53c722bc54012ecdca096e765b6dfb3a7f00d1b3662d4e.jpg)  
Fig. 8. Guidance screen for Case C.

## Moving Average Model

When you plot the data with time on x-axis and a variable (sales, profit, cost, etc.) on y-axis, if you see no linear trend and low fluctuations from one time to another, moving average method should be used. In moving average method, we take an average of last few time periods for forecast for next future period.

![](/api/attachments/U854FAWS/fulltext/images/e76a9fe89f5c1cd6d97db03f82d2747cd33723c632ff6d19466e3845cae9dfc5.jpg)  
Fig. 9. Guidance screen for Case D.

graphical comparisons, and indicates strongly that the user should not use moving average ('so you should not use moving average model...'). Comparing the figures for case C and case D, we see that the graphical information and text are different. The suggestion also is different, with a more emphatic statement in case D.

Therefore, the system adapts to the user's history from previous sessions, and makes fine adjustments as the user goes from one problem to the other.

## 6. Results from a preliminary empirical investigation

We used the prototype discussed in the Section 5 to conduct a preliminary empirical investigation in a laboratory environment. The study and the results are reported in detail in other publications $[29–31]$ and conclusions are briefly discussed in the following paragraphs. One hundred and thirty five subjects participated in the study. The preliminary results from the experiment show that the metasupport in DSS increases decision-making performance, learning and satisfaction of the users. The study examined decisional, instructional and cognitive aspects related to the support provided by the system.

On the decisional aspects, the decision quality improved, however, the decision time increased. The reason for the increase in the decision time is that the user spends more time using the DSS facility to explore more alternatives and increase understanding. The users with dynamic guidance, where the message content is tailored to the user's needs, performed better than the users with predefined guidance, where the users got 'canned' or predetermined messages. The users with suggestive guidance, where the system provides recommendation, did not perform better than the users with informative guidance, where the system provides detailed information without any recommendations [29].

On the instructional aspects, the users of the DSS with guidance learned significantly more than the users of the DSS without guidance. In addition, the users of the DSS with guidance were more satisfied with the overall process of decision-making than the users of the DSS without guidance. Also, the users with dynamic guidance learned more and were more satisfied with the process than the users with predefined guidance. Furthermore, the users with informative guidance learned more than the users with suggestive guidance. However, both groups were equally satisfied with the process $[30]$ .

On the cognitive aspects, the influence of guidance on the user depended on the user's cognitive styles. We used Jung's Psychological Types with Myers-Briggs Type Indicators to determine cognitive styles of the users. The users with Sensing-Dominant and Thinking-Auxiliary (ST) type performed better than the users with Intuition-Dominant and Thinking-Auxiliary (IT) type. Furthermore, the ST users with dynamic guidance performed better than the ST users with predefined guidance. However, the ST users with suggestive guidance did not perform better than the ST users with informative guidance [31].

## 7. Summary and conclusion

Traditionally, DSS have provided support for low-level cognitive tasks. To increase decision support effectiveness of DSS, there is a need to support high-level cognitive tasks which require human mental activities of reasoning and learning. In this paper, we propose ADSS which provide support for high-level cognitive tasks by dynamically adapting system support to the knowledge level of the user, the decision task characteristics, and the context in which the decision is made. ADSS are a result of integration of research in the field of decision support systems, cognitive science, and artificial intelligence.

ADSS monitor the problem-solving processes and the human decision maker to determine the support needs for making the judgmental inputs. The systems determine the gaps in the conceptual and procedural knowledge of the user for performing the given decision task. Based on the gaps, the systems determine the support needs and customize the support to match the needs.

ADSS have, in addition to the data, model and user interface components of the traditional DSS, an 'adaptation' component. The adaptation component uses artificial intelligence techniques to identify user needs and problem-solving model, and matches them with appropriate level of support.

We developed a prototype ADSS with decisional guidance capabilities to support the decision maker in selecting an appropriate forecasting model for a given set of data. Selection of the appropriate forecasting model required user judgement as to which forecasting model was more appropriate. The prototype system provided guidance for making the judgement, the guidance was matched to the particular user's needs and the decision task on hand. A preliminary empirical investigation was conducted using the prototype. The investigation was designed on the basis of a research practice where the researchers invent and test ways for improving decision-making effectiveness. The results of the investigation show that the guidance for judgmental inputs improves decision quality, user learning, and user satisfaction.

This study provides an architecture to integrate the currently disparate and fragmented research efforts. By applying this architecture in the development of real world DSS, decision-support effectiveness of the DSS could be increased.

ADSS can be applied to other areas of decision-making. We anticipate their usefulness will be optimal in the areas, (1) where the task environment is unstructured requiring more judgmental inputs from the decision maker and (2) where the impact of the decision is high, such as strategic management and crisis management.

In strategic management and planning, top management has to develop comprehensive strategies to cope with the instability, uncertainty, and complexity of the environment. This requires sophisticated and comprehensive understanding of the internal and the external factors to develop strategic plans for long-term direction of the establishment. While a traditional DSS does not adequately support tasks like problem formulation and problem structuring, an ADSS can provide support for high-level cognitive tasks such as setting goals and objectives, evaluation of alternative strategies, and stakeholder analysis $[32]$ .

In crisis management situation, a tendency is to consider a limited number of alternatives and quickly reach a decision. The limited analysis reduces the decision quality by rejecting a correct course of action, accepting a wrong solution to the problem, solving the wrong problem, and solving the right problem correctly but too late $[33]$ . ADSS can support the decision-making process by supporting generation and evaluation of more alternatives, identifying objectives, and evaluating the consequences.

Although we performed a preliminary investigation of the architecture using a prototype with decisional guidance capabilities, there is a need for further research. We suggest ADSS research in the following areas: 1. Investigate ADSS for unstructured and complex decision-making situations.

2. Develop and test alternative strategies for adaptive support.

3. Study the impact of adaptive support on the expert and novice decision makers.

4. Investigate the use of emerging technologies (e.g., neural networks, fuzzy logic, and genetic algorithms) in developing ADSS. New developments in online analytical processing and data-mining could also be used in building ADSS.

5. Investigate other related issues such as information overload, biasing behavior, and restriction on flexibility and creativity in the context of ADSS.

## References

[1] P.G.W. Keen, Decision support systems: the next decade, Decision Support Systems 3 (1987) 253–265.

[2] F.J. Radermacher, Decision support systems: scope and potential, Decision Support Systems 12 (4/5) (1994) 257–265.

[3] G.I. Nierenberg, The Idea Generator (A Software Product), Experience in Software, Berkeley, CA (1987).

[4] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA (1978).

[5] A. Newell, H.A. Simon, Human Problem-Solving, Prentice-Hall, Englewood Cliffs, NJ (1972).

[6] H.A. Simon, Sciences of the Artificial, MIT Press (1981).

[7] H.A. Simon, The New Science of Management Decision, Harper and Row, New York (1960).

[8] B.G. Silverman, Unifying expert systems and decision sciences, Oper. Res. 2 (3) (1994) 393–413.

[9] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of ‘unstructured’ decision processes, Administrative Sci. Q. 21 (2) (1976) 246–275.

[10] M.L. Manheim, D. Isenberg, A Theoretical Model of Human Problem-Solving and Its Use for Designing Decision-Support Systems, Proceedings of 20 $^{th}$ Hawaii International Conference on System Sciences, IEEE Computer Society (1987) 614–627.

[11] M.L. Manheim, An Architecture for Active DSS, Proceedings of 21 $^{st}$ Hawaii International Conference on System Sciences, IEEE Computer Society (1988) 356–365.

[12] H. Raghav Rao, R. Sridhar, S. Narain, An active intelligent decision support system — architecture and simulation, Decision Support Systems 12 (1) (1994) 79–91.

[13] S.A. Raghavan, JANUS — A paradigm for active decision support, Decision Support Systems 7 (1991) 379–395.

[14] S. Piramuthu, N. Raman, M.J. Shaw, S.C. Park, Integration of simulation modeling and inductive learning in an adaptive decision support system, Decision Support Systems 9 (1993) 127–142.

[15] C.W. Holsapple, R. Pakath, V. Jacob, J.S. Zaveri, Learning by problem processors, Decision Support Systems 10 (1993) 85–108.

[16] M.S. Silver, Decisional guidance for computer-based decision support, MIS Q. 15 (1991) 47–71.

[17] M.D. Merrill, R.D. Tennyson, L.O. Posey, Teaching Concepts: An Instructional Design Guide, 2 $^{nd}$ edn., Educational Technology Publications (1992).

[18] B.L. Dos Santos, C.W. Holsapple, A framework for designing adaptive DSS interface, Decision Support Systems 5 (1) (1989) 1–11.

[19] C.S. Sankar, F. Nelson, M. Bauer, A DSS user interface model to provide consistency and adaptability, Decision Support Systems 13 (1995) 93–104.

[20] S. Dutta, Decision support for planning, Decision Support Systems 12 (1994) 337–353.

[21] P.G.W. Keen, Adaptive design for DSS, DataBase 12 (1-2) (1980) 15–25.

[22] F. Milli, Dynamic View of Decision Domains for the Design of Active DSS, 22 $^{nd}$ Hawaii International Conference on System Sciences, IEEE Computer Society (1989) 24–32.

[23] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ (1982).

[24] E. Turban, Decision Support and Expert Systems, $2^{nd}$ edn., Macmillan (1990).

[25] M.L. Manheim, Issues in Design of a Symbolic DSS, Proceedings of 22 $^{nd}$ Hawaii Int. Conf. on System Sci., IEEE Computer Society (1989) 14–23.

[26] M.L. Manheim, M.L. Srivastava, S. Vlahos, N. Hsu, J. Jones, A Symbolic DSS for Production Planning and Scheduling: Issues and Approaches, 23 $^{nd}$ Hawaii Int. Conf. on System Sci. (1990) 383–390.

[27] W.E. Remus, J.E. Kottemann, Toward Intelligent Decision Support Systems: An Artificially Intelligent Statistician, MIS Q. (1986) 403–418.

[28] R. Sridhar, H.R. Rao, S. Narain, An architectural framework for an intelligent decision support system, Int. J. of Mini and Microcomputers 12 (2) (1990).

[29] Fazlollahi, Parikh, Verma, Evaluation of Decisional Guidance in Decision Support Systems: An Empirical Study, Proc. of the Third Int. Conf. of the Decision Sciences Institute, June 1995, Pueblo, Mexico (1995) pp. 78–80.

[30] Fazlollahi, Parikh, Verma, Evaluation of Alternate Instructional Strategies in Intelligent Coaching Systems: An Empirical Study, Proc. of the 26 $^{th}$ Annual Meeting of the Decision Science Institute, November 1995, Boston, MA (1995) pp. 499–501.

[31] Fazlollahi, Parikh, Verma, Influence of Decision Making Cognitive Style on the Design Features of Intelligent Guidance/Help for DSS: An Empirical Study. Proc. of the 1995 Information Resources Management Association Int. Conf., May 1995, Atlanta, GA (1995) pp. 25–30.

[32] J. Moormann, M. Lochte-Holtgreven, An approach for an integrated DSS for strategic planning, Decision Support Systems 10 (4) (1993) 401–411.

[33] H. Raiffa, Decision Analysis. Addison-Wesley, Reading, MA (1968).

![](/api/attachments/U854FAWS/fulltext/images/984bbe72b51978fc671cfd419073a8d3213c90954c06ff1b85587f457cbe947f.jpg)  
Bijan Fazlollahi is an Associate Professor of Decision Sciences at Georgia State University, Atlanta, GA. His research is in the area of Decision Support Systems. He has published over 30 articles in various journals and proceedings including Journal of Information Systems Research, Interfaces, and Information and Management. He is on the Editorial Board of the Journal of Database Management. He is a former Fulbright Scholar.

![](/api/attachments/U854FAWS/fulltext/images/511d998a5164b555d6d848f36c10566fb8e2203d85fb2d89f66f28661d06d9a1.jpg)

Mihir A. Parikh is a doctoral candidate in Decision Sciences at Georgia State University. He has received a Bachelor of Mechanical Engineering from Gujarat University, India and a Master of Business Administration from Georgia State University. His current research interests are in the areas of decision support and end-user systems, and applications of emerging information technologies (e.g., neural networks, fuzzy logic, genetic algorithms, multimedia) in decision-making and business training.

![](/api/attachments/U854FAWS/fulltext/images/edfe7b81dd56179695f0912574fd461e8ea805027d70ca9f7cae20c07612a215.jpg)

Sameer Verma is a doctoral student in Decision Sciences at Georgia State University, Atlanta GA. He has a Master of Science in Decision Sciences from Georgia State University, and a Bachelor of Engineering from Osmania University, Hyderabad, India. His areas of interest and work include intelligent decision support systems, education support systems, business training systems and strategic management through decision support and guidance. His focus is on the implementation of these systems through cognitive style research, using hypermedia/multimedia technologies.
