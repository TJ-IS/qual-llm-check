---
otero_id: 1604
otero_key: "BCHUW32N"
title: "Knowledge-based scenario management — Process and support"
authors: "Daud M. Ahmed; David Sundaram; Selwyn Piramuthu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.06.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-based scenario management — Process and support

Daud M. Ahmed <sup>a</sup>, David Sundaram <sup>b</sup>, Selwyn Piramuthu <sup>c,</sup>⁎

<sup>a</sup> The School of Computing and Information Technology, Manukau Institute of Technology, Manukau City, Auckland, New Zealand

<sup>b</sup> Information Systems & Operations Management, The University of Auckland Business School, Auckland, New Zealand

<sup>c</sup> Information Systems and Operations Management, University of Florida, Gainesville, FL 32611-7169, USA

## a r t i c l e i n f o

Article history: Received 19 November 2009 Received in revised form 19 May 2010 Accepted 18 June 2010 Available online 1 July 2010

Keywords: Decision Support Systems Generator Knowledge-based system Scenario planning Scenario management life cycle

## a b s t r a c t

Scenario planning is a widely accepted management process for decision support activities. Though conventional decision support systems provide a strong database, modeling and visualization capabilities for the decision maker, they do not explicitly support scenario management. We propose an integrated life cycle approach for knowledge-based scenario-driven decision support incorporating three interrelated frameworks at different abstraction levels to support this process. The macro-level knowledge-based framework guides the Meso-level Scenario-driven framework, and these two in turn guide and inform the micro-level process-oriented framework. We develop a domain independent, component-based, and layered architecture to support the scenario management process and framework. The framework and architecture are realized through a concrete prototype.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Scenarios are de<sup>fi</sup>ned as a management tool for identifying a plausible future [10,15,24,25,31,33] and a process for forward-looking analysis. Scenarios offer a dynamic view of possible futures [22,37]. Scenarios have also been de<sup>fi</sup>ned in many other ways: a story with a focused description of a fundamentally different future [30]; that is plausibly based on analysis of the interaction of a number of environmental variables [21]; that improves cognition by organizing many different pieces of information [7,8,34,36]; and that is analogous to a ‘what-if’ story [33]. A scenario can be a series of events that could lead the current situation to a possible or desirable future state. Scenarios are not forecasts [31], predictions [37], future plans [12], trend analyses or analyses of the past. They are for strategy identi<sup>fi</sup>cation rather than strategy development [30], to anticipate and understand risk [13], and to discover new options for action. Ritson [28] agrees with Schoemaker [29] and explains that scenario planning scenarios are conceived against known facts and trends but deliberately structured to enable a wide range of options and to track the key triggers that precede a given situation or event within the scenario. Scenario management facilitates the proactive decisionmaking process (e.g., [9]).

Decision makers have been using the concept of scenarios for a long time but, due to their complexity, their use is still limited to strategic decision-making tasks [20]. Scenario planning varies widely from one decision maker to another mainly because of a lack of a generally accepted principle for scenario management. Albert [2] proposes three approaches for scenario planning, namely the Expert scenario approach, the Morphological approach and the Cross-Impact approach. Ringland [27] describes a three-step scenario planning: brainstorming, building scenarios, and decisions and action planning. Schoemaker [29] outlines a ten-step scenario analysis process. Huss and Honton [19] identify three categories of scenario planning: Intuitive Logics, Trend-Impact analysis, and Cross-Impact analysis. Extant literature lacks a suitable approach for planning, developing, analyzing, organizing and evaluating scenarios using model-driven decision support systems. Currently available scenario management processes are cumbersome and not properly supported by available tools and technologies. They support neither the top-down approach — the breaking down of a scenario into executable and assessable component scenarios at various levels of abstraction; nor the bottom-up approach — the combining of small scenarios into the development of a high level scenario that represents a complex set of problems. To <sup>fi</sup>ll this void we propose a knowledge-based life cycle approach to scenario management that supports both top-down and bottom-up processes.

The generation of multiple scenarios and sensitivity analyses exacerbates the decision maker's problem. Existing scenario planning tools are not suitable for assessing scenario quality and do not fully support evaluating scenarios through a comparison process. We introduce an evaluation process for comparison of instances of homogeneous and heterogeneous scenarios that enables the user to identify the most suitable and plausible scenario for the organization.

Considering the signi<sup>fi</sup>cance of scenarios in the decision-making process, we model scenario as a decision support component of a knowledge-based DSS and de<sup>fi</sup>ne the scenario-driven DSS as an interactive computer-based system, which learns and integrates diverse data, models, solvers, and visualizations to explore decision scenarios that support decision makers in a dynamic environment.

Traditional DSS has been for the most part data-driven, modeldriven and/or knowledge-driven [26] but due importance has not been given to scenario planning and analysis. Some of the DSS have partial support for sensitivity analysis and goal-seek analysis but this does not ful<sup>fi</sup>ll the needs of the decision maker. Existing scenario analysis tools deal with scenarios one at a time and are not suitable for simultaneous development of multiple scenarios. While a scenario impacts related scenarios, existing tools are not suitable for developing a scenario based on another scenario. Generation of a scenario and its analysis are inadequate for the decision support environment.

To address these issues we follow an iterative process of observation/evaluation, theory building, and systems development, wherein we propose and implement a knowledge-based, scenariodriven, and process-oriented framework and architecture for a Decision Support Systems Generator (DSSG). We develop a prototype, which we then test and evaluate using the evaluation criteria for Design Science [18], quality and appropriateness of scenarios [29], and principles of DSSG framework and architecture [6,16].

In the remainder of this paper, we <sup>fi</sup>rst introduce a life cycle approach for scenario management including a detailed discussion of handling homogeneous and heterogeneous scenarios. We then present knowledge-based, scenario-driven, and process-oriented decision support frameworks, followed by a discussion on how they realize the scenario management process. We then present an ntiered architecture that details the frameworks. Finally, we discuss the implementation platform and domain within which the proposed process, frameworks, and architecture were implemented and validated.

## 2. Scenarios and their management

## 2.1. Definition of a scenario

The de<sup>fi</sup>nitions given in the previous section do not provide a complete picture of scenario modeling as they do not entail the exact scenario structure. We now discuss a proper implementation-level de<sup>fi</sup>nition that addresses the structure of the problem situation and its dynamic behavior.

A scenario is a situation containing one or more problem instances. A change in one scenario might have chain effects on related scenarios. But the basic structure and behavior of the scenario is similar to the decision support system components model and solver respectively as a model describes real-life phenomena and solves reallife problems [14]. Hence we de<sup>fi</sup>ne a basic scenario as a complex situation analogous to a model that is instantiated by data and tied to solver(s). In its simplest form, a scenario is a complex combination of data, model and solver; it can be presented using different visualizations. A scenario structure is a template object that establishes a complex relationship for integrating various related models, solvers, visualizations, contained scenarios and related data. A scenario could be developed by factoring a high level business problem into smaller problems using a top-down approach, or it could be generated by integrating various small systems into a real-life business case using a bottom-up approach. The lower-level systems on both top-down and bottom-up approaches comprise con<sup>fi</sup>gurable DSS scenarios that include model, solver, and data.

## 2.2. An example (mortgage management) scenario

A mortgage management scenario includes a series of external environment-sensitive interrelated scenarios. AMP ([3]) describes a mortgage scenario wherein the median wage and home prices increase, and the interest rate drop. What is the impact of this change, or any other changes, on an individual buyer as well as on the mortgage market? Any change in interest rate, average income, demand and supply, etc., highly in<sup>fl</sup>uences mortgage markets.

This scenario can be broken down into several scenarios such as affordability, loan, and payment scenarios. The affordability scenario assists in understanding the borrower's eligibility to acquire a loan and their capacity to repay the loan. The loan scenario analyses the cost of <sup>fi</sup>nancing, the loan amount, and the installment; depending on the loan type, this analysis process can differ widely. The payment scenario considers installment, interest payment, principal repayment, and loan balance, addressing the entire loan repayment life cycle. The affordability scenario is a constraint to the loan analysis scenario. Each of these scenarios can be further factored down to several smaller ones. For example, the affordability scenario depends on the income and expense scenarios while the income scenario may be sub-divided into personal income and family income scenarios. All are interrelated and the higher level scenarios are dependent on lower-level scenarios. On the other hand, lower-level scenarios can be integrated to develop the complete mortgage scenario. Sensitivity analysis and goal-seek analysis of these scenarios would greatly enhance the decision-making process.

## 2.3. Structuring scenarios

To address the complexity and interrelatedness of scenarios, we divide larger scenarios into multiple smaller ones with independent meaning and existence. In this context, we identify three types of scenarios, namely:

Simple scenario — This is not dependent on other scenarios but completely meaningful and usable.

Aggregate scenario — This comprises several scenarios. A top-level scenario can be broken down to low level scenarios or several low level scenarios can be combined to develop a higher level scenario. Pipelining scenario — This scenario is an input to another, in a hierarchical scenario structure. Here, a lower-level scenario can be tightly or loosely integrated with the higher level scenario.

The decision maker may combine simple as well as complex scenarios using pipelining and aggregation to develop more complex scenarios.

## 2.4. Scenario management: A life cycle approach

We introduce a scenario management process that synthesizes and extends ideas from Ringland [27], Schoemaker [29], Albert [2], Huss and Honton [19] and Wright [38]. The scenario management process uses a life cycle approach that is able to address a variety of problem instances. The proposed life cycle approach for scenario management process is illustrated in Fig. 1.

The process begins with scenario conceptualization and ends with the usage of scenario for decision support. The intermediate stages are scenario planning and organization, development, simulation, analysis and evaluation. We now discuss these phases of the scenario management life cycle.

## 2.4.1. Scenario conception

At the outset, the decision maker anticipates the problems and analyses them to determine the in<sup>fl</sup>uential driving forces, critical success factors, key performance indicators (KPIs), and parameters of the scenarios. The internal and/or external governing factors exert pressure on the system for various changes. The decision maker as a domain expert may predict possible changes to the KPIs to conceptualize scenarios and their planning, development and analysis processes.

In the next phase, we describe the tasks of scenario planning and development.

![](/api/attachments/BCHUW32N/fulltext/images/7f3752662f2a49bcb03ed1ce2751f3802780170c0d155177505b532801c1706e.jpg)  
Fig. 1. Scenario management life cycle.

## 2.4.2. Scenario planning and organization

The scenario planning stage focuses on decomposing the top-level scenario into multiple smaller interrelated scenarios suitable for development, simulation, analysis and evaluation. It also includes structuring and identi<sup>fi</sup>cation of the scenario components, and relates to the sequence of their development, simulation and selection for analysis. Existing scenarios could also be used as inputs to this phase in addition to the concepts generated from the previous phase.

The components of the scenario can be either pre-customized or loosely coupled. For a pre-customized scenario, the relationships among data, model, and solver, as well as with other dependent scenarios, are in<sup>fl</sup>exible and are de<sup>fi</sup>ned during scenario planning. For example, a scenario is a collection of data, models, solvers, and scenario(s) in which the relationships among the constituent components are <sup>fi</sup>xed and the model instantiation and model execution processes by data and solver are distinct. The scenario components are tightly integrated and the relationships are not visible to the end users (Fig. 2).

For a loosely coupled scenario, the components, including data, model, solver, and dependent scenarios, remain independent until they are de<sup>fi</sup>ned and mapped, using a mapping component, and validated, using a validation component, during scenario development, and are then simulated at runtime (Fig. 3). A scenario pool stores developed scenarios or scenario instances and dynamically retrieves and associates them for developing pipelining or aggregate scenarios. The contained scenario(s) is used as an input or mapped to the model component of the containing scenario.

Scenario organization activities include rendering access to already developed scenarios as well as storing, retrieving, deleting and updating the scenarios to and from a scenario pool. This pool supports both temporary and permanent objects including data, model, solver, visualization and scenario. The temporary storage, termed ‘runtime pool’, is used for developing aggregate or pipelining scenarios, simulation, analysis and evaluation. The pool also permanently stores scenarios for future reference or use. Both temporary and permanent storage systems are capable of storing the structures and instances of the scenarios.

![](/api/attachments/BCHUW32N/fulltext/images/ae8344b7dd05d59992414128dd5217abe1ff599c357e096b56addfa4ee2917d7.jpg)  
Fig. 2. Pre-customized tightly coupled scenario structure.

![](/api/attachments/BCHUW32N/fulltext/images/6fe3137f8ae2db3102c2fe286c4fb96b6514e615172696dd377a8e64e6685c90.jpg)  
Fig. 3. Loosely coupled scenario structure.

## 2.4.3. Scenario development

Scenario planning and organization, and scenario development stages are interdependent and iterative in nature. Scenario development is the process of conversion and representation of planned scenarios into fully computer-based scenarios. Chermack [4] argues that scenarios have rarely been applied to develop alternative processes. The proposed life cycle approach supports the development of alternative process models and scenarios. At this stage, the decision maker organizes related data, model, solver, and dependent scenarios for constituting the relationships among them to develop scenario(s). The decision maker could potentially use pre-customized and/or loosely coupled scenarios and may skip this stage if they use previously developed scenarios. The scenarios are developed in two steps. In step 1, the basic scenarios of the domain are developed and in step 2, scenarios related to what-if (goal-seek and sensitivity) analysis are developed.

These developed scenarios are then executed/simulated and analyzed as described in the following sections.

## 2.4.4. Scenario simulation

The proposed scenario development process in the previous stage ensures that the scenario can be executed and analyzed for determining quality and plausibility. In this stage, the models are instantiated using the data, and the model instance is then executed using the appropriate solver(s). Model selection is independent of selection of data and solver while one or more solvers may be used for model execution. A <sup>fl</sup>exible mapping process bridges the state attributes of the model, data, and solver to engage in a relationship and to participate in the instantiation and simulation process. For aggregate or pipelining scenarios, the decision maker feeds the already developed scenarios (structures and/or instances) into the current process. Simulation of the containing scenario depends on the simulation of the contained scenarios. For example, if the containing scenario contains the structure of the contained scenarios, the containing scenario simulation process would also involve a series of model instantiation and model execution. The contained scenario(s), if loosely coupled, may be recon<sup>fi</sup>gured as and when required.

## 2.4.5. What-if analysis

What-if analysis can be divided into two categories, namely sensitivity and goal-seek analyses. Sensitivity analysis identi<sup>fi</sup>es the impact of an increase or decrease in the values of one or more parameter(s) separately or simultaneously for assessing the impact on itself and its related scenarios. Goal-seek analysis accomplishes a reverse or feedback evaluation where the decision maker supplies the target output value for assessing the required inputs. In this step, the decision maker predicts a future scenario state and investigates the input parameters for achieving the target state.

A closely inter-twined step of what-if analysis is the generation and evaluation of homogeneous and heterogeneous scenarios. We explore this scenario evaluation process in the next section.

## 2.4.6. Scenario evaluation process

The decision maker can develop scenarios using different combinations of data, model, solver and other scenarios. Evaluation of these scenarios and <sup>fi</sup>nding the plausible scenario is not an easy task [5] but the <sup>fi</sup>nal state of a scenario can be pre-de<sup>fi</sup>ned based on the interrelation and interaction of the identi<sup>fi</sup>ed events [38] which can lead to the devising of an evaluation process for the developed scenarios. Each scenario might appropriately draw the strategic question, represent fundamentally different issues, present a plausible future, and challenge conventional wisdom. Schwartz [31] and Tucker [33] discourage too many scenarios and advocate for the use of bestcase, worst-case and most-likely scenarios. However, the selection of an appropriate scenario is reliant on the judgment of the decision maker. Evaluation is done through comparison of the simulated scenario outputs. A visualization component displays outputs of all the simulated scenario instances either as a table or as a graph and supports comparing the inputs and outputs of various simulations. The comparison may take place among homogeneous or heterogeneous scenarios as shown in Fig. 4. In order to avoid greater complexity, it is advisable to undertake homogeneous comparison <sup>fi</sup>rst and feed outcomes to the heterogeneous comparison stage. We now discuss this two-stage comparison process.

2.4.6.1. Homogeneous scenario comparison. Homogeneous scenarios represent closely comparable scenario instances that require similar inputs and provide analogous outputs, but they indicate quite distinct outcomes from one another. The decision maker <sup>fi</sup>rst compares instances of a scenario, selects a plausible instance for it and repeats the process for other scenarios. For example, in Fig. 4, the four outer ellipses represent four unique scenarios, namely Scenarios 1, 2, 3 and n that are coded as $\mathbf { T _ { 1 } } , \mathbf { T _ { 2 } } , \mathbf { T _ { 3 } }$ and ${ \bf T } _ { \mathrm { n } }$ respectively. Each scenario comprises three unique instances, namely $\mathrm { I } _ { 1 } , \mathrm { I } _ { 2 }$ and $\mathrm { I } _ { 3 }$ that represents the current scenario instance. Therefore, T I , ${ \bf T } _ { 1 } \mathbf { I } _ { 2 } ,$ and ${ \bf T } _ { 1 } { \bf I } _ { 3 }$ are three unique instances of scenario type 1. The decision maker compares these scenario instances and selects the most plausible scenario, which is ${ \bf T } _ { 1 } \mathbf I _ { 3 }$ in Fig. 4. The decision maker then repeats the entire process for scenario types 2, 3 and n. If a suitable instance for a scenario is not found, the decision maker repeats the scenario planning, development, simulation and analysis stages for developing different instances for the same scenario. The <sup>fi</sup>nally selected scenario instances are $\mathbf { T _ { 2 } I _ { 3 } } ,$ $\mathbf { T _ { 3 } I _ { 1 } }$ and $\mathbf { T _ { n } I _ { 1 } }$ for scenario types 2, 3 and n respectively, as shown in Fig. 4.

2.4.6.2. Heterogeneous scenario comparison. Heterogeneous scenarios are different types of scenarios. However, since they are derived from the same business system, change in one scenario impacts others as they are interrelated and simultaneously contribute towards a common solution. The heterogeneous scenario comparison process is complex as the attributes of these scenarios vary widely. Selected scenario instances from the homogeneous comparison process are presented in the centre circle (Fig. 4). The decision maker then compares common attributes (inputs and outputs) keeping the noncommon attributes <sup>fi</sup>xed. If any of the selected instances provides non-comparable output or is not suitable for heterogeneous comparison, the decision maker repeats the entire process to identify a new instance for that scenario. This provides the decision maker with an excellent overall view of the entire decision problem and an appropriate solution. For example, the selected scenario instances (i.e., T<sub>1</sub>I<sub>3</sub>, T<sub>2</sub>I<sub>3</sub>, ${ \bf T } _ { 3 } { \bf I } _ { 1 }$ and $\mathbf { T _ { n } I _ { 1 } } )$ in Fig. 4 are compared with the instance of the original (current) scenario during heterogeneous comparison.

![](/api/attachments/BCHUW32N/fulltext/images/1ba7cb2eed7ad157d59ca327d61fe3bd7452631b0d51a04595264b594f6ff031.jpg)  
Fig. 4. Scenario evaluation process.

## 2.4.7. Decision support

The above described scenario planning, development, simulation, and analysis through comparative evaluation, results in improved participant learning (e.g., [7,17,29]) and helps decision makers reperceive reality from several points of view [34,35], thereby resulting in better support for decision making.

## 3. Knowledge-based scenario management: from conceptualization to realization

We present and discuss three frameworks, architecture, and implementation that realize the proposed scenario management process in the following sections (Fig. 5). These frameworks are organized in a sequence of increasing complexity and detail. We <sup>fi</sup>rst discuss a Macrolevel Knowledge-based Decision Support Systems Framework. This high level framework guides our Meso-level Scenario-driven Decision Support Systems Generator Framework. These two frameworks in turn inform and guide our Micro-level Process-oriented Decision Support Systems Generator Framework. These frameworks are then realized through an architecture which is implemented and evaluated through functional and Design Science guidelines.

## 3.1. Macro-level Knowledge-based Decision Support Systems Framework

We use the macro-level knowledge-based adaptive DSS framework proposed by Piramuthu and Shaw [23] as given in Fig. 6 to guide our design. This generic, adaptive, DSS framework comprises four

Meso-level Scenario-driven DSSG Framework

![](/api/attachments/BCHUW32N/fulltext/images/4dda0058b375ea0235295d74b2397ed4fee24ec0929462a7837290e64c2cb4ca.jpg)

Micro-level Process-oriented DSSG Framework

Fig. 5. Knowledge-based scenario management: from conceptualization to realization.

![](/api/attachments/BCHUW32N/fulltext/images/587e49fd15bd6492376c78c45c124f9f2a39bf090ffbd1bddb9a2d130d7e55b7.jpg)  
Fig. 6. Macro-level knowledge-based adaptive DSS framework [23]

main components including Learning, Simulation, Problem-solving, and Performance-evaluation. The Learning component facilitates learning in response to changes in the environment and performance of the DSS based on the response from the Performance-evaluation component. The Simulation component is used to generate sample example scenarios to enable learning by the Learning component as and when gaps in the knowledge-base are identi<sup>fi</sup>ed. The Problemsolving component uses appropriate learned knowledge and instantaneous (current snapshot) input (problem) data from the environment to dynamically make decisions. The interested reader is referred to Piramuthu and Shaw [23] for detailed information on the macrolevel framework.

## 3.2. Meso-level Scenario-driven Decision Support Systems Generator Framework

A scenario framework offers a variety of scenarios designed to help guide strategic decision making [11]. Each scenario covers a range of circumstances that could have a signi<sup>fi</sup>cant impact on organizational strategies. Extant DSS frameworks do not emphasize fully featured scenario planning, development, simulation, analysis, evaluation and their usage for decision support. DSS components such as data, model, solver, and visualization have been extensively used in several DSS framework designs but they do not consider scenario as a DSS component. Given the critical role played by scenarios in the decisionmaking process, it is impractical to develop an effective decision modeling environment without this component. The scenario-driven DSS adds scenario as an independent component in addition to existing decision support components of data, model, solver, and visualization. Scenarios are closely related to model-driven DSS but they are more complex than models and do not have a separate existence without their base components. This signi<sup>fi</sup>es that every scenario is built up from the unique nature of the problem (model) that may have a number of alternative unique instances (data) and each instance can be interpreted, simulated or analyzed using one or more alternative methods (solver).

To overcome the problems and address the issues mentioned above, we propose a Meso-level Scenario-driven Decision Support Systems Generator (DSSG) framework as illustrated in Fig. 7. The DSSG components are separated into the following three categories: a) decision support components (DSC) that include the data, model, solver, scenario, and visualization b) integration components (IC) that include Kernel, component set, mapping, and validation component. c) Component pools that include data pool, model pool, solver pool and scenario pool. In this framework, the DSCs, ICs and component pools are independent of one another. The DSCs do not interact or recognize each other directly; rather, the components communicate using ICs. The Kernel helps to establish relationships among the DSCs; the mapping component develops the correct path of communication between data and model, and model and solver; while the validation component ensures correct matching of the interface and proper communication between the components.

The meso-level framework enables the user to establish relationships among the model, data, solver and previously generated scenario(s) for developing a scenario that leads to a speci<sup>fi</sup>c decision support system. Depending on the problem situations, various combinations of data, model and solver create different scenarios. A scenario can be used as a speci<sup>fi</sup>c DSS as well as a complex data for input to the next level of model or scenario for further analysis. Thus, the framework is a generator of scenarios as well as of decision support systems.

![](/api/attachments/BCHUW32N/fulltext/images/3e5f2a1acbdf08c8ea7fbaea9e4ee6ce5feeedc3fdc5b361514521151d581c5a.jpg)  
Fig. 7. Meso-level Scenario-driven Decision Support Systems Generator Framework.

The higher level components in the Macro-level DSS framework (Fig. 6) map loosely to the components in Fig. 7, as follows: The problem-solver maps to the solver and model, learning and knowledge-base together map to the solver pool and model pool, simulation maps to data pool and scenario pool, and performanceevaluation maps to Kernel validation.

The framework allows the generating of a number of simple, aggregate, and pipelined scenarios. Previously developed scenarios can be customized using new models and solvers. The DSCs can be independently developed and could remain independent within the system at runtime until called for a speci<sup>fi</sup>c purpose. Different scenarios can be computed simultaneously and goal-seek analysis can be done using different scenarios. The framework is suitable for analyzing internally coherent scenarios or scenario bundles, and examining the joint consequences of changes in the environment for supporting the decision maker's strategy. Multiple components can be simultaneously loaded to the system from the component pool and formed into a component set which in turn can be utilized independent of the component pool.

## 3.3. Micro-level Process-oriented Decision Support Systems Generator Framework

We now discuss and illustrate (Fig. 8) the mechanisms through which the scenario management process is realized using the processoriented DSSG framework. Speci<sup>fi</sup>cally, we discuss the means by which the framework supports all the life cycle phases of the proposed scenario management process. The key features of this framework are discussed below.

## 3.3.1. Supporting scenario conceptualization

The DSSG framework supports dynamic retrieval of the required DSS components from the respective component pools and establishes relationships among them for developing scenario(s) to support the decision maker's thought process. Decision makers use their own expertise and experience for making an initial assessment of the scenario prototypes that contribute towards the decision problems without rigorous development, analysis, and evaluation and subsequently identi<sup>fi</sup>es several unique scenario types and instances. It therefore supports generation of multiple instances of a scenario through various combinations of constituent components.

## 3.3.2. Scenario planning

Supports the planning of modeling-based scenario structure, precustomized and loosely coupled scenarios.

## 3.3.3. Runtime scenario organization

Incorporates a runtime scenario storage system named runtime scenario pool (RSP) to support the ongoing development process. The drafted/completed scenario(s) can be stored, retrieved, updated, or deleted from the RSP and used in developing aggregate and pipelining scenarios.

## 3.3.4. Scenario storing and retrieving

DSSG uses a component management system for bridging between component set and component pools for storing, retrieving, updating or deleting the scenarios from the scenario pool. The RSP is linked with the component set through the Kernel.

## 3.3.5. Scenario development

The basic scenario similar to that in Fig. 3 is developed using building blocks such as data, model, solver, and previously developed scenario(s) and is temporarily stored in RSP, as shown in Fig. 8. The sensitivity scenario and goal-seek scenario analysis processes use model, data and solver from the component source, user data regarding changing scenario parameters, and dependent scenario(s) from the runtime scenario pool. The Learning component also enables development of appropriate scenarios based on the current dynamics and existing Knowledge-base in the system. The Performance-evaluation component aids in this process by identifying gaps in existing knowledge in the system.

## 3.3.6. Development of aggregate and/or pipelining scenarios

In a pre-customized pipelining system, scenarios are pre-de<sup>fi</sup>ned as a chain from lower-level to upper-level scenarios. The upper-level scenarios directly receive executed values of the lower-level scenarios as input parameters. In loosely coupled scenarios, however, a top-level scenario uses the structures or values of the lower-level scenarios from the runtime scenario pool. Therefore, the DSSG supports the development of aggregate and/or pipelining scenarios.

![](/api/attachments/BCHUW32N/fulltext/images/2ffaf2a279180909616bc31c26ab5660a2b7b7cc14f88a581f3b47f362cd96c9.jpg)  
Fig. 8. Micro-level Process-oriented Decision Support Systems Generator Framework.

## 3.3.7. Scenario selection

The framework allows the user to select any scenario depending on its suitability, quality and appropriateness.

## 3.3.8. Scenario execution

The framework facilitates instantiation of the model with the data and execution of the instantiated model with appropriate solvers.

## 3.3.9. Scenario evaluation

The framework supports evaluation of scenarios through visualization of the output of basic, sensitivity, and goal-seek scenarios in a table and/or graph.

## 3.3.10. Decision support

The framework supports Simon's [32] intelligence, design, and choice phases of decision making. These phases are comparable to scenario generation, analysis, comparison, and selection of plausible scenarios. Scenario analysis and evaluation using the comparison process increase the cognitive knowledge of decision makers which in turn supports and leads them towards the <sup>fi</sup>nal decision.

## 3.4. Knowledge-based, scenario-driven, process-oriented decision support system generator architecture

In order to implement the above frameworks, we develop a knowledge-based, scenario-driven, process-oriented decision support system generator architecture as shown in Fig. 9. This componentbased and layered architecture is suitable for implementation as an ntiered system. The proposed architecture comprises the user services tier, application tier, and persistence tier. The layers include user services and presentation, integration, component access, decision support components, and components persistence. The architecture also contains an application customization layer that is used for plugand-play of new components for customizing the system. The interrelationship of these layers and their constituent components is shown in Fig. 9. The components persistence layer stores data, model, solver, and scenario. The component access layer provides components management services. The decision support components layer provides the service of model, solver, scenario and visualization components. The integration layer provides validation and mapping services during integration, instantiation, and execution of decision support components.

The architecture separates the decision support components from the integration components. It supports independent development and use of the components, <sup>fl</sup>exible scenario modeling, scenario manipulation and integration, <sup>fl</sup>exible mapping between different DSS components, <sup>fl</sup>exible integration of DSS components, and scenario analysis. A pre-customized and customizable modeling system can be achieved through pre-de<sup>fi</sup>ned relationships and the mapping component respectively. The Mapping component facilitates dynamic communication between model-data, model-solver, and model-visualization.

## 3.4.1. Layers of the architecture

We now discuss the components persistence, component access, decision support components, integration, user services/presentation, and application customization layers in detail.

3.4.1.1. Components persistence layer. The primary role of this layer is to store data, model, solver and scenario components and their management using standard Database Management Systems (DBMS) and/or XML. This layer comprises four separate pools e.g. data pool, model pool, solver pool, and scenario pool. It is independent and disconnected from the system. The component information can thus be updated separately using an application customization layer. Each of the pools manages its related components and their information using database tables or XML documents. The data related to the speci<sup>fi</sup>c domain used for model instantiation can be received from a DBMS or an XML <sup>fi</sup>le. The information regarding models, solvers and scenarios is speci<sup>fi</sup>cally related to the components of the DSSG and stored in the database or by using XML. The model pool, solver pool and scenario pool are updated only when a relevant component is updated in the DSSG system.

User Services Tier  
![](/api/attachments/BCHUW32N/fulltext/images/bf836976158d82d9b5b094fcaa49762888919a05ca4e60624e22ec27562b4941.jpg)  
Fig. 9. Knowledge-based, scenario-driven, process-oriented decision support system generator architecture.

3.4.1.2. Component access layer. The component access layer provides components' management services (e.g., addition, retrieval, update, or delete component information). It uses a services component for enabling on-demand communication between the integration layer and various pools of the components persistence layer. The component access layer facilitates importing component information to the component set as well as exporting or updating to the relevant pools. This layer develops the required connection and component handling commands at runtime.

3.4.1.3. Decision support components layer. The decision support components layer provides the services of DSS components (model, solver, scenario, and visualization components). Created and existing independently within this layer, these components interact with other components via the integration layer.

3.4.1.4. Integration layer. The integration layer provides integration, validation and mapping services during integration, instantiation and execution of decision support components through the Kernel, Mapping, and Validation components. The Kernel facilitates communication between data-model, model-solver and scenario-visualization using the mapping component for model instantiation, model execution, and scenario presentation respectively. It also uses the validation component to validate the proper communication and execution of the components. Validation proceeds automatically depending on the runtime usage of the system, while mapping is fully manual. The Kernel supports both loose and tight couplings.

3.4.1.5. User services/presentation layer. This layer is the graphical user interface and presentation of the system that supports the creation of dynamic graphical user interface (GUI) through dynamic and runtime creation of user controls, and facilitates scenario presentation depending on the decision maker's selection of data, model, solver, scenario, and visualization components at runtime. The components of the user services layer support decision maker interaction with the system for input, mapping, scenario development, execution, analysis, evaluation, and presentation activities.

3.4.1.6. Application customization layer. This layer includes three different components, namely framework template, template controls, and component container, and facilitates customization of the decision support components with new features. The component container stores information on version and interface of the decision support components. The framework template, with the help of template controls, replaces one or more selected decision support components with the support of the component container. This facilitates versioning and extension of existing components.

## 3.4.2. Tiers of the DSSG architecture

The DSSG architecture can be implemented in a single-, two- or ntiered fashion. In the single-tiered system, a desktop system contains all layers of the DSSG architecture. In a three-tiered system, the user services tier contains the user services/presentation layer; the application tier contains the integration, component access, and decision support components layers. The persistence tier contains only the component persistence layer. The distribution of layers may vary depending on the type of client-server system.

## 3.4.3. Components of the DSSG architecture

The components are broadly categorized into decision support, integration and user interface, and customization template components.

3.4.3.1. Decision support components. The decision support components of the DSSG architecture are model, data, solver, visualization, and scenario. Model refers to real-life problems, data is the parameter instance of the model, and solver is the operation that can be applied on the model. The solver is the disintegrated behavior(s) of the model from its structure; the scenario is the complex combination of data, model and solver. Visualization facilitates <sup>fl</sup>exible presentation of data, executed model, or scenario.

3.4.3.1.1. Model component. The model can be of the primitive or the compound type [16]. Primitive type models are directly derived using base data type variables as well as executed model values of the base level models. The compound type model, e.g. aggregate and pipelining models, either inherits or aggregates the base models or may both inherit and aggregate as well as add some other independent parameters.

3.4.3.1.2. Data component. The data component comprises data model and component service that work with the component pool using universal data access technology (e.g., OLEDB, ODBC). This component contains parameters and methods responsible for export and import of data, model, solver and scenario information to and from the component pool. Data component methods are generic but command texts can be supplied at runtime.

3.4.3.1.3. Visualization component. The visualization component generates runtime tables and graphs for model- or scenario-executed data. This component is used speci<sup>fi</sup>cally for presentation of scenarios for evaluation through comparison.

3.4.3.1.4. Scenario component. This component is dependent on the data, model, solver, and scenario (where applicable) and is generally created at runtime.

3.4.3.2. Integration and user interface components. The integration and user interface components contain Kernel, Component Set, Validation, and Mapping, and Common Component.

3.4.3.2.1. Kernel and common component. The Kernel is the main integration component of the system, integrating the decision support components and other associated integration components (such as component set, mapping, and validation). The Kernel works as the centre of communication between and among the components. Components or component instances are called inside the kernel when any member of the component is instantiated or invoked at runtime. The Kernel is designed for both loose and tight coupling of data, model, and solver. For the tightly coupled system, usage of data, model, and solver are pre-de<sup>fi</sup>ned. The model understands which data is to be picked up on the basis of data and model activation to instantiate the model and which solver is to be called to execute the model. In addition to activating and using the component functions, the Kernel, in association with the common component, generates runtime user interface, and communicates and integrates with other components of the system.

3.4.3.2.2. Mapping component. This is a generic process-oriented component that enables the model component communicating with data and solver components while they are developed independently. It plays a pivotal role for loose coupling. In the DSSG, this component establishes mapping between data-model and model-solver. During mapping, it collects the name and type of attributes of the selected data, model, and solver from the component set and presents them to a dynamically created user interface. This process is designed in such a way that the decision maker does not need to change any attribute name of component set data tables. The mapping component facilitates communication between two attributes with different names. The decision maker then maps the attributes of the components for communication. The model is the centre for mapping the attributes. The model attributes are <sup>fi</sup>xed; the user selects the data attributes for model-data mapping, and selects the solver name and solver attributes for model-solver mapping. A pre-customized and customizable modeling system can be achieved through pre-de<sup>fi</sup>ned relationships and the mapping component respectively. This mapping component facilitates connection and dynamic communication between model-data, model-solver, and model-visualization. It supports the conversion of data between different data sources, to link data with models, and to identify valid operations for the models. The data, models, and solvers are completely independent and reusable. The Mapping component helps achieve value, dimension, and data structure independence between model and data, as well as the representation, selection, and purpose independence between model and solver.

3.4.3.2.3. Validation component. The validation component is responsible for checking the input data type for model and solver after mapping. In model-data validation checking, the data type of the model attribute is <sup>fi</sup>xed and checks whether the data attributes are similar or convertible to the data type of the model attribute. For model-solver validation, the data type of the solver attribute is <sup>fi</sup>xed and checks whether the data types of the attributes of the model instance are similar or convertible to data type of the solver attribute.

3.4.3.2.4. Component set. The component set is a disconnected dataset. It coordinates the component pool and the application. The component set can be <sup>fi</sup>lled with records from Data Tables, Model Pool, Solver Pool, and Scenario Pool. A component set can be loaded with one or more data tables and model, solver and scenario data.

## 3.4.4. Independence and reusability of Components

The decision support components are independent of one another with mappings between them. Since the components are independent, they can be reused in other systems. Of paramount importance in making the components reusable, are the model-data and modelsolver independences.

3.4.4.1. Model–data independence. The architecture achieves the following aspects of model-data independence:

Value independence — the data value of a variable can be changed without affecting the model representation.

Dimension independence — the number of variables in the data can be changed without affecting the model representation.

Data structure independence — the names and types of variables of models may be different from those of datasets, but the model can work with the dataset. The base entities in the model do not have to exist as base entities in the database.

3.4.4.2. Model–solver independence. The architecture achieves the following aspects of model-solver independence:

Representation independence — model and solver are independently developed and one component is not dependent on another for its representation.

Selection independence — choice of solver does not depend on the model representation. A solver can be used with other models or a model can be executed with a different solver.

Purpose independence — the model representation is independent of the direction of computation.

3.4.4.3. Domain independence of the frameworks and architecture. The frameworks and architecture have been designed in a generic fashion. Since conceptual frameworks do not include domain related information, they are appropriate for any domain. The architecture does not depend on domain information; rather, it allocates the function of the components within the system. The components have been placed in different layers of the architecture. Most of them are domain independent, e.g. data, scenario, mapping, validation, while some components may deal with domain-speci<sup>fi</sup>c problems (e.g. model). Scenario analysis is more domain-speci<sup>fi</sup>c analysis. Generalized scenario analysis has little or no impact on the scenario-based decision support system. Some of the components (e.g. model) are thus more oriented towards the domain to achieve better decision support. These domain-speci<sup>fi</sup>c components can be recon<sup>fi</sup>gured as per the needs of other domains and the architecture can use these modi<sup>fi</sup>ed components. The framework and architecture are domain independent, while some components may need to be recon<sup>fi</sup>gured for use in another domain.

## 3.4.5. Extensibility of the architecture

The architecture allows the addition of external components. However, in order to use the components without modifying others, their interfaces have to be similar. The original component of the system is replaced by external components. As the components have been designed using the object-oriented paradigm, adding new functions to the component is possible by extending the components through object-oriented principles.

## 3.5. Implementation platform and domain

The frameworks and architecture can be implemented using any platform that supports component-based development. Since objectoriented and component-based concepts are the central focus of the frameworks and architecture, we leveraged Microsoft's.NET Framework for implementing the DSSG architecture and used object-oriented languages (such as C#, VB.NET) and componentization methodologies (such as Dynamic Link Library, Component Object Model), Relational Database Management Systems (e.g. SQL Server, Microsoft Access), and Extensible Markup Language (XML) for building the system and managing data, model, solver, and scenario components. The frameworks, architecture, and implementation were tested within the context of the mortgage domain provided in Section 2.2. Speci<sup>fi</sup>cally, we implemented affordability scenario, lending scenario (table loan, reducing installment, interest only), and payment scenario, among others. A generic component diagram of the scenario is given in Fig. 10. According to this component diagram, a scenario inherits basic features from another generic service component named ComponentServices, which in turn inherits from an abstract component named StandardObject for behaving and exhibiting scenario as a component. A schematic of these two components is shown in Fig. 11. The scenario component contains a number of collection objects for managing model, solver, visualization, and mapping components, as shown in Fig. 10. It also contains a collection of its own objects for referring to and using previously de<sup>fi</sup>ned scenarios. In addition, a scenario component contains several objects such as a data component for managing instances of scenario constituents and facts, and a ScenarioValidator for testing and validating suitability of various scenario components and their relationships.

Each of the above-mentioned constituent components (such as Model, Solver, Data, Visualization, Mapping, and Validator) as well as parent components (such as ComponentServices and StandardObject) implements one or more interfaces that contain abstract structural and behavioral de<sup>fi</sup>nitions of the related components. The scenario component also incorporates several other properties for extension of structural de<sup>fi</sup>nitions such as scenario description and creation, modi<sup>fi</sup>cation and usage history: it extends the basic component behavior for its management such as display, instantiation, and simulation; and <sup>fi</sup>nally incorporation of various event-based message and state management services for informing the modeler about addition and removal of new constituent components (models, solvers, data, visualizations, maps) and assisting the user by informing selection, instantiation, and simulation of a scenario or any of its constituent components.

The ComponentServices and StandardObject components as shown in Fig. 11 contain several properties for its structuring, representation, behavioral and message communication. The ComponentServices component provides basic service requirements to most of the participative components (such as models, solvers, data, visualizations, maps). It also supports conversion and transformation of an object to various forms such as binary, XML, relational data, document for persistence services or regeneration of the object from the previously converted format. During the conversion of a scenario for persistence management, basic information of the scenario is initially converted to discrete data format and the constituent components are then converted to various formats that enable persistence.

![](/api/attachments/BCHUW32N/fulltext/images/130f3d4c576bcfb4b4f2d29de249869deba949e86c6501fe00fb3f3c9fd209e3.jpg)  
Fig. 10. Scenario component diagram.

The scenario components hold reference to each of those converted objects. During regeneration of the scenario, <sup>fi</sup>rst the main scenario is constructed with empty containers for each of the component type; it then regenerates all the components and puts them in containers; in the next step, it creates all references for establishing relationships among the components; and <sup>fi</sup>nally, it runs the associated scenario validation object for checking, testing and validating the regenerated scenarios.

A user interface of the system is shown in Fig. 12. Within each of these scenarios, we explore sensitivity and goal-seek analyses. First we develop basic scenarios. We then explore a number of alternative scenarios including the best-case, worst-case, and most-likely scenarios through sensitivity analysis. We then evaluate the scenario instances using homogeneous and heterogeneous comparison processes as discussed in Section 3.3. The system was tested and evaluated for sensitivity analysis for re<sup>fi</sup>nancing from different lending sources, and increase or decrease of the interest rate (IRC), loan amount, initial payment (IPC), installment (IC), and pay period (PPC). Apart from this, we also explored sensitivity analysis on aggregate and pipelining scenarios.

The system supports complex analyses from the very lower-level scenarios to top-level/aggregate scenarios. Scenarios analyzed bottomup may or may not satisfy the primary objective. In this case, a top-down scenario analysis could produce the optimum acceptable scenarios that would satisfy the objective. We explored both top-down and bottom-up approaches for scenario analysis using the system where both the approaches produced similar outputs.

The prototype supports different levels of users and various levels of customization and abstraction. In order to minimize the trade-off between versatility and usability, the DSSG enables the decision maker to use both customizable generic systems and pre-customized and packaged scenarios for a particular use. A DSS builder con<sup>fi</sup>gures the DSSG system to develop purpose-built very speci<sup>fi</sup>c and effective DSS and stores them for use by decision makers. Due to the nature of dynamic user interface and visualization, this DSS is easy to use for its intended purpose.

## 4. Evaluation of the research artifacts

## 4.1. Functional evaluation

We used eight different categories of evaluation criteria including scenario management, scenario analysis and development, scenario evaluation, appropriateness of scenarios, computational performance, functionality, usability, and ancillary task support for evaluation of the DSSG framework and architecture and various processes. The principles proposed by Geoffrion [16] and Collier et al. [6], namely ease of model selection, algorithmic variety, <sup>fl</sup>exible visualization, management of components, data-model independence, modelsolver independence, data-visualization independence, mapping, reusability, domain independence, extensibility, model abstraction level, purpose independence, model instantiation, model termination, model execution, and model version support were applied for critical evaluation and validation of the DSSG framework and architecture. The quality and appropriateness of the scenarios were evaluated based on the appropriateness, usability, uniqueness, variety, and quality as prescribed in Schoemaker [29].

The evaluation criteria are extended to assess various processes (e.g., scenario management, scenario planning, development and analysis, and scenario evaluation, and mapping between components). The scenario management process was evaluated using the life cycle stages of scenarios such as idea generation, scenario analysis and management, scenario development, scenario storage and retrieval, runtime scenario management, scenario execution, and scenario evaluation. Scenario planning, development and analysis processes were evaluated using principles of scenario structuring (simple scenario, simple pipelining scenario, complex scenario, complex pipelining scenario), provision of runtime scenario pools, ability to conduct sensitivity and goal-seek analysis, ease of scenario generation, tight and <sup>fl</sup>exible coupling of components. Scenario evaluation sub-process was evaluated based on the ability to compare multiple instances of a scenario and instances of multiple scenarios, ease of scenario comparison and use, support for decision making, and organizational learning. Ahmed [1] applies the concept of these frameworks and architecture for the development of a roadmap of sustainable business transformation, and frameworks and architectures for a sustainability-oriented decision-making system.

![](/api/attachments/BCHUW32N/fulltext/images/09f357323eb3fdff36c32a761d4a767e76d669956cbd523ffaff92705515feac.jpg)  
Fig. 11. Standard object and component services.

Many of the models' and solvers' structures are domain independent and can be used in any applicable domain. Specialized scenarios are more oriented towards the domain to perfectly represent the scenarios. This type of models and their relevant solvers are sometimes domain dependent. We have extensively explored the use of the proposed system in the context of the mortgage domain. However, given its generic nature the proposed system is equally applicable to other domains where ‘what-if’ analysis, goal-seek and iterative problem-solving/search is of importance. The current DSSG system allows minor versioning of the components without any impact on the kernel. However, a major change in the paradigm could necessitate a change to the public interface of the components which in turn may require modi<sup>fi</sup>cation of the kernel component.

## 4.2. Methodological evaluation

The Design Science perspective proposed by Hevner et al. [18] has been quite in<sup>fl</sup>uential in generating a stream of research ideas and implementations that have generally been shown to be effective. Hevner et al. [18] presented seven Design Science guidelines that aid in the acquisition of knowledge and understanding of a design problem and its solution through building and applying an artifact. We consider each of these in turn and brie<sup>fl</sup>y discuss how the proposed scenario planning process and knowledge-based DSSG frameworks, architecture, and implementation measure in term of these guidelines. The guidelines proposed by Hevner et al. [18] are as follows:

Design Science requires the creation of an innovative and purposeful artifact: The knowledge-based scenario-driven process-oriented frameworks for scenario management are innovative artifacts since existing DSS frameworks do not explicitly incorporate the capacity to learn. This is a signi<sup>fi</sup>cant characteristic since the capability to be adaptive becomes ineffective without learning capability and it erodes rapidly with time as changes in the dynamics of system and environment dictate continual learning. The knowledge-based DSSG is purposeful since it is designed to be used in dynamic environments where learning is of paramount importance. The artifact thus created must be relevant: The knowledge-based DSSG framework is relevant, and can be instantiated in dynamic application areas to show its applicability in several real-world adaptive decision-making scenarios. We instantiate the proposed knowledge-based scenario-oriented DSSG with learning capability in a dynamic environment.

Thorough evaluation of the artifact must reveal its utility: Utility in the knowledge-based DSS frameworks can be viewed in terms of performance measures, which vary across application domains. For example, in the dynamic manufacturing shop <sup>fl</sup>oor scenario, the performance measure could be minimizing make-span, whereas in the supply chain management context it could be minimizing inventory. A successful artifact proves itself through better performance, based on appropriate performance criteria. Results based on speci<sup>fi</sup>c applications provide strong evidence for the utility of this artifact. The artifact is novel and innovative in being able to solve a heretofore unsolved problem or a known problem effectively and ef<sup>fi</sup>ciently. In the Scenario Management context, the generation of an innovative solution could be considered a performance measure.

Research contributions: As per Design Science principles, the artifact must enable the solution of heretofore unsolved problems. The DSSG frameworks incorporating information from several feasible scenarios considered in this paper enable the addressing of a novel scenario where scenario management data are seamlessly incorporated in the knowledge-based DSSG for decision-making purposes.

![](/api/attachments/BCHUW32N/fulltext/images/78c22d1ecc287bfc296b81bada78c922c97f659381982e9428df43193dfc63c0.jpg)  
Fig. 12. The DSSG implementation in the mortgage domain.

The artifact must be rigorously de<sup>fi</sup>ned, represented, coherent, and consistent: The DSSG considered has <sup>fi</sup>ve formally de<sup>fi</sup>ned components that interact with one another. The general functionalities of each of these components are also de<sup>fi</sup>ned, although the details are context-speci<sup>fi</sup>c and therefore depend on the application area. In scenario management, for example, several components of input data are generated automatically by the process and streamed through to the system, while others, such as user input data, are manually obtained.

The artifact or its creation process is the best in a given problem space: As mentioned in Hevner et al. [18] the iterative nature of the design process allows for continual feedback between evaluation and construction phases to improve the quality of the system of interest. This process can be clearly observed in the DSSG. As environmental characteristics and the best approach to address them evolve over time, a system that captures the dynamics and addresses them appropriately is clearly better than existing static systems.

The results from the creation and use of an artifact must be communicated to both researchers and practitioners: The learning-based framework helps to summarize and communicate the qualities and utility of the considered DSSG, both in terms of its essential components and in the way they synergistically interact with one another, to both researchers and practitioners alike. This process is facilitated by considering signi<sup>fi</sup>cant problems such as scenario management where tangible improvements could be obtained.

The considered knowledge-based scenario-driven and processoriented frameworks, architecture, and implementation do therefore adhere to the guidelines of a Design Science artifact. The frameworks and architecture are generic and <sup>fl</sup>exible enough that thus can be used for decision support in disparate domains. They are also powerful enough to be used for decision support in approaching problems that are dif<sup>fi</sup>cult to solve otherwise. The frameworks and architecture are innovative, relevant, purposeful, and rigorously de<sup>fi</sup>ned artifacts, generic and powerful enough to be implemented and instantiated with required speci<sup>fi</sup>cities in disparate domains. They address problems that are unsolvable by deterministic means, speci<sup>fi</sup>cally those that involve dynamic environments, and their utility is demonstrated by their implementation and validation through the scenario management case presented in this paper.

## 5. Discussion

Current scenario planning and analysis systems are very complex, not user friendly, and do not support modeling and evaluating multiple scenarios. Scenario-based decision support systems focus mostly on developing corporate strategies rather than supporting tactical or operational level decision making. To overcome these problems we propose a knowledge-based scenario management life cycle including frameworks and architecture to support the lifecycle. The lifecycle, as well as the frameworks and architecture, are validated through an implemented prototype.

We develop a generic, knowledge-based, life cycle based approach for scenario management that supports a range of activities from idea generation to <sup>fi</sup>nal use of the scenarios. Key phases of the life cycle are idea generation, scenario planning, organization, development, execution, analysis, evaluation, and decision support. The process hides external factors and complexities of the scenario and allows the seamless combination of decision parameters for appropriate scenario generation. We also proposed a generalized scenario evaluation process that allows homogeneous and heterogeneous scenario comparisons among the multiple instances of similar and dissimilar scenarios respectively. This process enables the decision maker to <sup>fi</sup>nd appropriate and plausible scenarios. We introduced the concepts of scenario structure and their development strategy. The scenario management process decomposes large complex scenarios into multiple small and executable scenarios and uses the decomposition and re-composition methodology for de<sup>fi</sup>ning the scenario structure.

This study further realizes the scenario-driven decision-making process using model-driven decision support systems. The developed frameworks and architecture support the above-mentioned scenario management process as well as sensitivity and goal-seek analysis. The scenario-driven framework uses decision support components, integration components, and component pools. Scenario has been introduced as a new DSS component that is developed as a complex combination of other decision support components that include data, model and solver. The proposed frameworks and architecture are domain independent, platform independent, component-based and modular. The architecture comprises multiple layers, e.g. component pool layer, data access layer, decision support services layer, integration layer, and user services layer. Each layer performs speci<sup>fi</sup>c functions, which are suitable for implementation of the architecture as a single-, two-, three-, or n-tiered system. A prototype was developed using the frameworks and architecture. The implemented system is suitable both for the naïve user as well as the DSS builder. The naïve user can easily use the semi-automated pre-customized system while the DSS builder can use the versatile loosely coupled system.

## References

[1] M.D. Ahmed, Sustainable Business Transformation: Roadmap, Framework, Architecture and Implementation, Unpublished Doctoral Dissertation, University of Auckland Auckland 2009.

[2] K.J. Albert, The Strategic Management Handbook, McGraw-Hill, New York, 1983.

[3] AMP, AMP Banking Survey—New Zealand home affordability highest for two years, (http://www.amp.co.nz, July 2007).

[4] T.J. Chermack, A methodology for assessing performance-based scenario planning, Journal of Leadership & Organizational Studies 10 (2) (2003).

[5] T.J. Chermack, The mandate for theory in scenario planning, Futures Research Quarterly 18 (2) (2002).

[6] K. Collier, B. Carey, D. Sautter, C. Marjaniemi, A methodology for evaluating and selection data mining software, Proceedings of the 32nd Hawaii International Conference on System Sciences, 1999.

[7] A. De Gues, The Living Company: Habits for Survival in a Turbulent Business Environment. Harvard Business School Press, 1997

[8] E. Desmarais, The art of scenario planning: a review of two books, Journal of Business & Economic Studies 6 (1) (2000).

[9] K.C. DeSouza, Scenario Management: From Reactivity to Proactivity, IT Pro, Sept– Oct 2005.

[10] N.D. Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and scenario generation within a simulation framework: an information systems perspective, Decision Support Systems 42 (4) (2007).

[11] A.W.S. Drew, Building technology foresight: using scenarios to embrace innovation, European Journal of Innovation Management 9 (3) (2006).

[12] J.H. Epstein, Scenario planning: an introduction, Futurist 32 (6) (1998).

[13] D.P. Fordham, K.W.J. Malafant, The Murray–Darling basin irrigation futures framework, Proceedings of International Congress on Modelling and Simulation Conference (MODSIM 97), vol. 2, Modelling and Simulation Society of Australia, 1997.

[14] A. Gachet, Building Model-Driven Decision Support Systems with Dicodess, VDF, Zurich, 2004.

[15] I.A. Gelman, Setting priorities for data accuracy improvements in satis<sup>fi</sup>cing decision making scenarios: a guiding theory, Decision Support Systems 48 (4) (2010).

[16] A. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987).

[17] M. Godet, K. Radford, Creating futures: scenario planning as a strategic management tool, Economica (2001) London.

[18] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004).

[19] W.R. Huss, E.J. Honton, Scenario planning: what style should you use? Long Range Planning (April 1987).

[20] M. Jarke, X. Tung Bui, J.M. Carroll, Scenario management: an interdisciplinary approach, Requirements Engineering 3 (1998).

[21] L.L. Kloss, The suitability and application of scenario planning for national professional associations, Nonpro<sup>fi</sup>t Management & Leadership 10 (1) (1999).

[22] NIC, Mapping the global future, Report on the National Intelligence Council's 2020 Project, December 2004.

[23] S. Piramuthu, M.J. Shaw, Learning-enhanced adaptive DSS: a design science perspective, Information Technology and Management 10 (1) (2009).

[24] J.-C. Pomerol, Scenario development and practical decision making under uncertainty, Decision Support Systems 31 (2) (2001).

[25] M. Porter, Competitive Advantage, Free Press, New York, 1985.

[26] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books, Westport, Conn, 2002.

[27] G. Ringland, Scenario Planning — Managing for the Future, John Wiley & Sons, New York, 1998.

[28] N. Ritson, Scenario planning in action, Management Accounting 75 (11) (1997)

[29] P.J.H. Schoemaker, Scenario planning: a tool for strategic thinking, Sloan Management Review 36 (2) (1995).

[30] P.J.H. Schoemaker, Multiple scenario development: its conceptual and behavioural foundation, Strategic Management Journal 14 (3) (1993).

[31] P. Schwartz, The Art of the Long View, Doubleday, New York, 1991.

[32] H.A. Simon, The New Science of Management Decision, Harper and Row, New York, 1960.

[33] K. Tucker, Scenario planning, Association Management 51 (4) (1999).

[34] K. van der Heijden, Scenarios, The Art of Strategic Conversation, Wiley, New York, 1996.

[35] K. van der Heijden, R. Brad<sup>fi</sup>eld, G. Burt, G. Cairns, G. Wright, The Sixth Sense: Accelerating Organizational Learning with Scenarios, John Wiley, New York, 2002

[36] P. Wack, Scenarios, uncharted waters ahead, Harvard Business Review (1985).

[37] B. Weinstein, Scenario planning: current state of the art, Manager Update 18 (3) (2007).

[38] A.D. Wright, Scenario planning: a continuous improvement approach to strategy, Total Quality Management 11 (4–6) (2000).

Daud M. Ahmed is a senior lecturer in the Department of Computing and Information Technology, Manukau Institute of Technology, Auckland, New Zealand. He has varied academic (B.Sc. Engineering in Electrical and Electronics, MBA on Development Management, PG Dip in MSIS, M.Com. in MSIS) background and currently working on his PhD on developing sustainability modeling and reporting framework. He has 20 years working experience on engineering design, implementation monitoring, management consultancy, systems analysis, design, development and implementation, and teaching and actively participated in planning and management of a number of engineering and social development projects that are funded and implemented by the World Bank, Asian Development Bank, EEC, and OPEC, He has research publications on framework and architecture of decision support systems, software project management, sustainability modeling, triple bottom line reporting, and systems development.

David Sundaram is an engineer by background, a teacher, researcher, and consultant by profession, and a lifelong student. He is passionate about modelling, design, and implementation of <sup>fl</sup>exible and evolvable information, decision, knowledge, and social systems. Exploration and application of these in the architecture and design of learning, adaptive, agile, and sustainable enterprises and societies is close to his heart. Key research themes that he is at the moment exploring with his team of researchers include: (1) Adaptive Enterprises and Networks, (2) Knowledge Networks, (3) Sustainable Enterprises, Value Chains, and Alliances, (4) Purposeful Visualizations and (5) Ubiquitous Information Systems and Digital Natives.

Selwyn Piramuthu is a Professor in the Information Systems and Operations Management department at the University of Florida. His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.
