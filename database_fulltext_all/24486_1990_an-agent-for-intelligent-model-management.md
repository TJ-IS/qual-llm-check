---
otero_id: 24486
otero_key: "JYPFAWC6"
title: "An Agent for Intelligent Model Management"
authors: "John I. C. Liu; David Y. Y. Yun; Gary Klein"
year: "1990"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1990.11517883"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Agent for Intelligent Model Management

John I. C. Liu, David Y. Y. Yun & Gary Klein

To cite this article: John I. C. Liu, David Y. Y. Yun & Gary Klein (1990) An Agent for Intelligent Model Management, Journal of Management Information Systems, 7:1, 101-122, DOI: 10.1080/07421222.1990.11517883

To link to this article: http://dx.doi.org/10.1080/07421222.1990.11517883

![](/api/attachments/JYPFAWC6/fulltext/images/d34c5f322462b53a4ffd8bff20e41b838a5e3ebd9ad1374a2ef4f092a8230f30.jpg)

Published online: 21 Dec 2015.

![](/api/attachments/JYPFAWC6/fulltext/images/481f7a48a3a83a00fd50263ebaf4844dd9bb503683045e0869512a17161ad61b.jpg)

Submit your article to this journal ↗

![](/api/attachments/JYPFAWC6/fulltext/images/ad210df9b2c09a9b2d51b3bdb48c4d2699f5d79560cfaa3729a14efb9d125d4f.jpg)

View related articles ↗

# An Agent for Intelligent Model Management

JOHN I. C. LIU, DAVID Y. Y. YUN, and GARY KLEIN

JOHN I. C. LIU is Associate Professor of Information Management at the National Defense Management College in Taipei, Taiwan, Republic of China. He also serves as Director of the Computer Center. He received his Ph.D. in Computer Science from the School of Engineering and Applied Science at Southern Methodist University. Before his doctorate program, he worked for the R.O.C. government as an analysis and design consultant in the area of computer-based information systems. His research interests include expert systems, decision support systems, and software engineering.

DAVID Y. Y. YUN is Professor of Computer Science and Engineering at Southern Methodist University. He received his B.S. in Mathematics from Ohio State University in 1970, and his Ph.D. in Computer Science and Applied Mathematics from MIT in 1973. He was Manager of Research for the Symbolic and Algebraic Computations Group at the IBM T.J. Watson Research Center from 1973 to 1983. His current research interests are in symbolic computation, knowledge management and systems, computer algebra, artificial intelligence, and software engineering. He is an editor of International Journal of Symbolic Computation, International Journal of Data and Knowledge Engineering, and ACM Transactions on Mathematical Software. His academic honors and awards include a listing in Who's Who in Frontier Science and Technology, IBM Outstanding Technical Contribution Award, and Outstanding Dissertation in Computer Science.

GARY KLEIN is Associate Professor of Business Analysis and Communication in the College of Administration and Business at Louisiana Tech University. His Ph.D. in Management Science was awarded by Purdue University's Krannert Graduate School of Management in 1981. He previously served as Exchange Professor to Kwansei Gakuin University in Nishinomiya, Japan. An active participant in national academic conferences, he has also made professional presentations on decision support system technology in the U.S. and Japan. His main research centers on the model management aspects of decision support systems. However, his works in the fields of automated system development, multiple criteria optimization, quality control, and integer programming have appeared in Decision Sciences, JMIS, Management Information Systems Quarterly, Naval Research Logistics Quarterly, and others. He is co-author of the textbook Structured COBOL by Design.

ABSTRACT: Decision Support Systems (DSS) and Expert Systems (ES) are both aimed at improving decision making. Current DSS usually concentrate on quantitative models while ES emphasize logic and reasoning. In this paper, we review previous ES approaches used by DSS to handle decision models. We propose an extension to such systems, an Agent for Intelligent Model Management (AIMM), as an interface between DSS and the users. AIMM utilizes a combination of ES knowledge representations and reasoning mechanisms to make a wide variety of models available to decision makers so that they may apply these models without becoming involved in technical or procedural aspects of implementation. A prototype of the system for financial problems is described.

KEY WORDS AND PHRASES: Expert system, intelligent agent, decision support system, model management.

## 1. Introduction

IN RECENT YEARS THERE HAVE BEEN RAPID DEVELOPMENTS in two different fields aimed at improving decision making: Decision Support Systems (DSS) in management science and Expert Systems (ES) in computer science. Although both seek to improve decision quality, current DSS usually concentrate on quantitative model methods and are weak on logical reasoning, whereas ES emphasize logical expression and reasoning. The joining of the two approaches, with models as the common basis, will greatly enhance model usage in decision making [12].

Much research has looked at specific technology and proposed that Artificial Intelligence (AI), specifically knowledge engineering [21], should enhance the modeling aspects of DSS [17, 28]. The task of controlling DSS models through AI, or through any means, has come to be known as model management. Much recent research has been done on the model management aspect of DSS. The reason that model managers have proven difficult to develop is that many functions must be performed from the technical as well as the user viewpoint. Klein, Konsynski, and Beck [16] discuss the minimal technical functions that must be performed. These include: (1) model abstraction methods that allow decomposition of models into their elemental components; (2) model base storage techniques that preserve the models and are compatible with data storage techniques; (3) model extraction methods that are used to select faithfully a proper model from the model base; (4) model integration techniques that expand the domain of the model base by construction of hybrid models when no existing model in the model base is appropriate for the new problem environment; and (5) model application rules to ensure the accurate use of the selected models. The user functions that must be supported by a model manager are problem identification, formulation, analysis, and interpretation [11, 29].

In this paper, we briefly review certain model management techniques using ES capabilities to meet DSS design requirements. The need of DSS to provide expertise in modeling along with model availability leads us to apply Intelligent Agent (IA) technology $[13]$ to the model management aspects of DSS. We call the system an Agent for Intelligent Model Management (AIMM) and describe its basic architecture. A prototype of AIMM for a simple financial problem is discussed and demonstrated.

## 2. Background

THE LITERATURE CONTAINS VARIOUS APPROACHES TO MODEL MANAGEMENT [2]. The model representation schemes proposed include predicate calculus [5], knowledge abstractions in frames [9], linear curves [16], graphs [21], semantic networks [10], and relational data structures [3]. For each representation, methods must be developed to satisfy the technical and user functions of a Model Management System (MMS). Once model representation is accomplished, languages must be developed to facilitate the technical functions [3, 18, 19]. Model selection and sequencing is done with configuration scheme coupling [24], scheme splicing with typing calculus operators [6], and by planning methods and other reasoning approaches that can be complemented with the use of heuristics [7, 14, 19, 20]. Model managers can also be enhanced with learning approaches [8].

A conceptual representation scheme of models that is becoming a standard of comparison is the structured modeling approach of Geoffrion [12]. Structured modeling was developed as an extension to the field of management science for the purpose of facilitating modeling in a computerized environment. It is based on a modularized model structure that is organized as a hierarchy. The approach provides guidelines for decomposing mathematical models from an abstract level into elemental levels, and allows for the integration of the individual model components. Each structured model is composed of six types of elements. These are primitive and/or compound entities, fixed and/or variable attributes, and numeric-valued and/or logic-valued functions. The relationships among functionally dependent elements are preserved by a system of calls to each dependent element. Same type elements with identical relations are placed into a group called a genus. Groups of related genera are called modules. This hierarchical arrangement can be conceptually applied to methods using data representation [19] or frames [9]. A similar conceptual structure will be used by the method proposed in this paper with a hierarchical frame representation.

The selection of models for use must then be driven by a form of reasoning. Relational data models require the use of a query language that must incorporate a query processor and error-detection facilities that require further extensions to become practical $[19]$ . Forward chaining methods using feasibility $[15]$ or planning $[7]$ are limited in their scope of reasoning directions. The method in this paper will use multiple reasoning approaches.

New models developed by the user of the system should be preserved for future selection. This learning function is part of a problem diagnosis system $[8]$ that looks for causal relationships in existing data under the direction of a user. Once a relationship is established, it is preserved in a semantic network model for future reference. This search is under the control of the user and requires a great deal of insight into the problem structure by the user. AIMM will also be able to learn new models and default data from its users, yet it requires little operational knowledge on the part of the user. These benefits are attained through the use of intelligent agent technology.

An Intelligent Agent (IA) is a system that is capable of providing knowledge of existing programs and finding a sequence of such programs for achieving the users' goals $[13]$ . A beginning framework for the Intelligent Agent was first applied in the CMS-HELP expert system $[30]$ . CMS-HELP was developed to serve as an online consultant to users of the VM/CMS operating system and utilizes IA principles in its processing. The IA is a problem-solving paradigm that combines both conventional and AI problem solving. An IA problem-solving procedure is designed to handle a given class of problems for which solutions can be achieved with a set of available system capabilities.

The success of conventional problem solving by computer owes a great deal to the large amounts of systematic knowledge that exist in these areas, and to the availability of strong methods for finding solutions that use available knowledge in a highly effective manner. Under these conditions, efficient problem-solving procedures, whose correctness and optimality can often be justified on formal grounds, can be custom produced. Conventional problem solving is best applied to well-structured problems that can be described in terms of numerical variables, have a goal that can be specified in terms of a well-defined objective function, or have existing computational algorithms. The well-defined algorithm is coded in a procedural programming language.

The problem-solving situation is quite different in AI, where the emphasis is on problems with limited amounts of systematic knowledge, and where solution-finding processes rely primarily on weak methods such as Generate-and-Test, Hill Climbing, Best-First Search, Problem Reduction, Constraint Satisfaction, and Means-Ends Analysis. Their efficiency when applied to a particular problem is often highly dependent on the way they exploit domain-specific knowledge. Under the guidance of a heuristic, the weak methods use available knowledge about a problem in certain generic ways in their attempt to search for a solution.

In general, there is no sharp dividing line between the problem-solving procedures of AI and the procedures used in conventional computing $[1]$ . The distinctions are based on the relative amounts of systematic versus heuristic knowledge available for the procedures and on the form in which the available knowledge is used. Some problems that are being studied in AI can be placed in an intermediate position between these two ends. In some cases, for example, the essential variables are not numerical originally, but they can be quantified. Other cases exist where the objective function is vague before simplifying assumptions are made. For many problem classes there are many available algorithms, but one must understand what these algorithms can do in their relation to the problem at hand before one can apply them.

IA problem solving emphasizes available system capabilities, which are systematic knowledge for solving specific tasks, and heuristic knowledge as a guide for using the available capabilities effectively. The solution-finding process of the IA applies weak methods that are guided by heuristic knowledge to construct a solution plan. This solution plan is from the set of system capabilities, often well-defined algorithms, which are interpretable and executable by the system. The process can be seen as embodying a specific way of utilizing knowledge about a problem domain that results in a transformation of the initial problem class into a configuration of “simpler” problem classes that the system “knows how to solve.”

## 3. Agent for Intelligent Model Management (AIMM)

AIMM IS BASED UPON A COMBINATION OF REPRESENTATIONS and inference schemes and is designed to increase the utility of the DSS by enhancing the functions of model management. This is done by offering the user (1) the knowledge and guidance of how to identify a problem and choose a model, (2) the knowledge and guidance of how to apply the model or sequence of models to the problem, (3) the knowledge of how the models behave, and (4) a dynamic model-processing mechanism.

The two primary objectives of developing an IA consulting system are as follows:

(1) A supportive, adaptable, man-machine interaction: the intelligent agent must help the Decision Maker (DM) identify the problem and meet the requirements of problem identification and structuring, alternative analysis, sensitivity analysis, goal attainment, and solution implementation; in other words, meet the identified user functions of an MMS.

(2) An automatic, flexible, modeling process: the intelligent agent can formulate specific models for various problems by automatically matching and chaining modules in the model base. This involves managing the capabilities of modules and managing the relations among interdependent modules; in other words, meet the technical functions of the model manager. This technical aspect is discussed first.

## 3.1. Central Module Library

The development of centralized module libraries marked the first concept of the AIMM approach. Module libraries are similar to early databases in that they allow a model element, which was previously hard-coded into a single application problem, to be saved for other applications. To illustrate this flexibility, consider spreadsheet models that have been employed to facilitate numerous decision problems and applications. The user has to develop a unique spreadsheet and fill out the cells of the spreadsheet for each application or specific problem. These problem-specific spreadsheets lack the flexibility and generality necessary to be useful in handling various problems even in the same domain. It is difficult to share any cell from one sheet with another unless the cell is manually copied. Conceptually, there are common model components in most models that could be centrally controlled for widespread access in a dynamic design and would save considerable programming effort and time for revision if organizational modeling needs changed.

With the AIMM approach, the idea of a model base for DSS is not a collection of specific models but a collection of sharable model components. Decision makers do not have to code the model for their problem, they can concentrate on the problems, and allow AIMM to construct the models. The storage of capabilities allows model constructs across application areas where the models can be decomposed.

## 3.2. Dynamic Model Chaining

From the model management perspective, AIMM treats primitive modules (basic elements of models) as capabilities of DSS, and approaches the modeling process as a reasoning or learning process from the users' tasks to a collection of functionally connected modules. Like management scientists who have long been experts in decisions, the AIMM's expertise is not in a specific domain, but in the construction of an appropriate model based upon the needs of the user. A system that could mimic the (a) Profit Margin = Total Revenue - Variable Cost

![](/api/attachments/JYPFAWC6/fulltext/images/53166bdb63a243d34517dccc396352c44dd6221f26e6cdf33660794228d53dae.jpg)

(b) Variable Cost = Unit Variable Cost X Volume Made  
![](/api/attachments/JYPFAWC6/fulltext/images/d8e5cfa5cd87f027b833c9a70ef7e32522626d1dc2f610f69af0d1efcee404af.jpg)

(c) Break Even Point
= (Fixed Cost + Profit) ÷ Unit Contribution Margin
Break Even Point
= (Fixed Cost + Profit) ÷ Contribution Margin Ratio

![](/api/attachments/JYPFAWC6/fulltext/images/6015bce4e71e62312adb75012e2e477f4f2d2b6744dbc444a3d0cff0266b011b.jpg)  
Figure 1. Financial Model Primitive Modules

management scientist's consulting expertise would be effective. AIMM plays the role of an adviser to guide applications in DSS by bridging the gap between a casual user and a comprehensive DSS.

## 3.3. Model/Knowledge Schema

Definition: A primitive module capability represents any distinctly identifiable function that is predefined in a system.

The application domain of AIMM, a specific DSS, must provide a set of primitive modules that are basic capabilities for solving problems in that particular application. Each primitive module in the model base is a stand-alone capability, and it is also a basic element for an application. It may be a relationship or association among entities. Each primitive module may consist of inputs, preconditions, procedures, outputs, and effects, i.e., several elements from structured models including the functions, attributes, and entities, along with their calls. The module is also an action that may give or change the value of the parameter set. The primitive modules of AIMM are independently stored in a model base. In a complex case, a module may be attached with procedures causing a specific task to be executed. Typical primitive modules are formula equations. Figure 1 shows several examples of primitive modules in a sample financial application. These primitive modules can be dynamically and flexibly chained to be specific models for different problems.

Definition: A specific model represents a composition of primitive modules with specific variables and coefficients and is developed to solve a specific application problem.

A specific model is a complete representation of the specific problem and is tightly coupled with a solution procedure. For example, these models may include a linear program with a certain objective function and a set of constraint functions that combine input variables. Through attached procedures, specific models can be solved and thereby produce a set of values for the decision variables.

Specific models are designed for specific decisions of decision makers. The variety of decisions and users requires a variety of specific models and solution procedures. From the descriptions, surveys, and studies of existing DSS, it is easy to conclude that their model bases are mostly collections of specific models $[26]$ . However, existing DSS do not seem to cluster such specific models around specific types of decisions or decision makers, nor to modify such models for similar decisions or different decision makers.

With the AIMM approach, a specific model is a structure of primitive modules with relevant knowledge and necessary solution procedures. In many cases, a single primitive module may not satisfy a user's goal. Instead, many goals can only be achieved by executing a sequence of modules. It is possible that a set of primitive modules, in combination, produce the required outputs for the user in making a decision. For example, a profit model may link several financial modules to produce desired information. Figure 2 shows a possible structure of this profit-specific model, which links together four primitive modules (M1 to M4). The hierarchical structure is similar to that of structured modeling.

Definition: A meta model is any prescribed class of model schema intended to represent a set of problems and reference techniques for solving problems of the prescribed class.

The meta model represents an abstraction of certain problems, tasks, and solvers. It may be viewed as a generalization of a set of lower specific models. A typical meta model is a mathematical programming model. It can be categorized into linear programming, integer programming, and dynamic programming models, among others. Thus, it is at a higher level than the modules defined by Geoffrion [12]. Such meta models are more general models incorporating knowledge about the wide range of alternatives for various types of decisions that are responsible for the generation of different specific solutions of decisions. Viewed differently, the lower-level model, the specific model, may be viewed as a typical instance of the meta model. In effect, the meta model can be used to generate specific models that determine the set of decision variables and algebraic relations among such decision variables. A second, important function of a meta model is recognizing and classifying problem situations in accordance with its broad understanding about the domain.

![](/api/attachments/JYPFAWC6/fulltext/images/5287bda6c1ad16b36569fac54d5db2855f92bceb8d169d167845678998e38d54.jpg)  
Figure 2. Profit Specific Model

Definition: Meta knowledge is the knowledge of chaining primitive modules, developing a meta model, and applying specific models in problem solving.

In the AIMM domain, it is necessary to encode the knowledge of determining which module can perform a particular task, how each module can be performed individually or can be chained into a group of modules, why a specific model may be selected, or possible reasons that a model may not work. AIMM has both extensive model-specific and problem-specific knowledge and also expertise in the explanation of knowledge and the model's application.

The model-specific knowledge is adequately equipped with knowledge about the modeling process as well as knowledge relating to the modules in the model base.

Such types of knowledge include the following: (1) the knowledge of how to choose a model or models; (2) the knowledge of how to use individual models or a sequence of models; and (3) the knowledge of how the models behave. This type of knowledge focuses strongly on the dependencies among the definitions of various primitive modules. The model-specific knowledge explicitly represents the natural chainings of the different model elements.

The problem-specific knowledge is represented by a profile that represents snapshots of different things (i.e., different users, different department, different applications). It is designed to simplify and minimize the amount of information required from the user in selecting modules. The profile serves to capture the default specifications that AIMM can refer to and write on, to provide the user with adaptability in accessing the model/knowledge base. The profiles are adaptable in the sense that the default specification can change as the different entities evolve. There are profiles that are designed for different users who are from different functional departments and different management levels. The profile is a collection of related, default, and entity-specific knowledge.

## 3.4. Model/Knowledge Representation

All primitive modules, meta models, meta knowledge, and specific models rely on the existence of a powerful representation. Such model/knowledge representation involves encoding facts about objects and the structure of models, as well as abilities to use those facts. It is a combination of data structures and interpretive procedures that represents both the problem and the solution. With regard to modeling and decision support, model/knowledge representation takes the form of relations [3], logic [4], semantic nets [10], and frames [9]. Different representation schemes have different advantages and disadvantages, depending on the function and complexity of the problem domain [2]. The required factors for selecting one particular representation or developing a hybrid type for AIMM are as follows:

(1) It must be able to implement the primitive modules and allow the integration of these into a specific model.

(2) It must be able to implement the meta models and allow them to acquire more knowledge relevant to the problem at hand.

(3) It must be able to classify and organize problems efficiently and match them with knowledge about available meta and specific models.

With the above requirements and available representations, a frame system is suitable for representing different objects in the model/knowledge base of AIMM. Frames can store information about models and how the models are used. This information includes expectations or default assumptions that are invariant items to fit different situations. Further, frames can store information about how they can be transformed into other models or different model instances. Dolk and Konsynski [9] propose a frame system together with model abstractions in which different specific models could be dynamically constructed from model abstractions, and also in which the similarities, differences, and relationships among models can be represented.

Since the system will allow the user to access groups of related models, the AIMM approach is to represent a model hierarchically, where a concept node is covered by a node representing a more general concept. For example, all models that relate to the variables cost, volume, and profit are grouped into a financial analysis category. The objective of this hierarchical structure is to allow tasks to interact with each other efficiently and to reflect the user's preferred strategies. The top-level frame of the hierarchy represents the general concept of a group of models for a class of problems, and the lower-level node represents more specific models for more specific problems. Furthermore, the meta-knowledge of each specific model, such as how to apply the model to a problem, can be included in a parent node.

The frame system is suitable to represent models in a hierarchical organization. The primitive capabilities and macro capabilities are organized in a hierarchical fashion. The bottom level of the hierarchy consists of a set of primitive capabilities. The ith level contains macro capabilities such that each capability involved in the macro is in the $(i + 1)$ th, or lower, levels. When a goal is submitted to the IA, the IA needs to determine whether a macro or a primitive capability can be applied. The IA always searches the highest level of the hierarchy first. When a capability is not found in the current hierarchy level, the IA searches the next lower hierarchy level.

## 3.5. Modeling/Reasoning Mechanism

AIMM requires a processing mechanism in order to participate actively in the consultation of modeling and the problem-solving process. This mechanism uses knowledge of the application and primitive modules offered by the system to convert the user problem into a specific model. It must be able to infer the true state of the system from incomplete and inaccurate information. It also must be able to generate problem solutions from situations never before encountered or anticipated, and be able to solve problems based on system capabilities and knowledge in a self-conscious fashion. The critical functions of this mechanism are often approached with dynamic, adaptive, or flexible strategies in ill-structured environments.

One primary role of AIMM is to guide the manager to retrieve and/or formulate automatically desired models for solving problems. This consulting is envisioned to be a reasoning process to assist users defining their tasks and chaining a collection of appropriate modules for such tasks. AIMM must employ an inference scheme to link appropriate primitive modules from the source to the sink of the problem goal. This scheme requires both goal-driven and data-driven reasoning.

The modeling process is initiated by the user's task to goal-driven reasoning. The goal-driven reasoning is continuously used to decompose the goal into subgoals until there is an available primitive module that can represent each subgoal. Whenever goal-driven reasoning reaches the state where there is more than one primitive module and it cannot decide which alternate modules should be selected, AIMM switches the inferencing to data-driven reasoning for continuation. The strength of the data-directed process is that it can quickly propagate the data obtained from the user rather than search all available models. During the modeling process, heuristic functions should be employed to guide the search direction in order to avoid either deadlock or the crossing of the two search patterns, since goal-driven and data-driven reasoning run the risk of not finding each other during a search. Bidirectional inference in which forward chaining is flexibly mixed with backward chaining is especially important in AIMM to meet modeling needs.

Besides dynamically constructing models, another primary role of AIMM is to aid in model analysis and interpretation. From this perspective, AIMM works with the user to provide the required user functions, in the sense of a consultant helping users to solve problems with the model. The intelligent agent must help the DM to do alternative analysis, sensitivity analysis, goal attainment, and solution implementation. To accomplish these tasks successfully, the AIMM system must (1) detect anomalous inputs, (2) provide default assumptions, (3) give salient explanations, (4) present feasible suggestions, (5) suggest alternative constructions, (6) conduct sensitivity analysis, and (7) allow for goal setting. The reasoning mechanism of AIMM for providing such functions is based on several AI inference techniques:

(1) Default Reasoning [25]: Default reasoning is based on the suggestion of “usual” conditions and values to enable the continuation and completion of formulating by minimizing user specified values. Default reasoning is a form of non-monotonic reasoning that involves reasoning with assumptions which may later prove to be false. Therefore, it is based on a mechanism that allows retracting invalid assumptions.

(2) Constraint Reasoning [27]: Constraint-based reasoning allows the user to do sensitivity analysis by changing a particular independent variable and seeing the effect on the dependent variable. Backward causality is useful in goal setting by using constraint relations to identify those elements which impact the goal variable.

(3) Plausible Reasoning [25]: Plausible reasoning is better known as heuristics (rules of thumb), which are distilled from experience in response to combinatorially explosive solution spaces. When there is no apparent superior alternative, heuristics may be employed to give some possibly useful suggestions from which alternatives should be selected. If there is no candidate that matches the user's goal or subgoal, or if a dead end is reached, plausible reasoning can suggest other possible directions. Another use of plausible reasoning is to request more specification when more than one candidate specific model is available and no selection heuristic is available.

## 3.6. Model/Knowledge Acquisition

Essentially, each specific model that is formulated by AIMM is a potential primitive module. Any specific model designed for previous problems can be saved in a model base for later use. When a new problem includes one or more previously solved problems as subproblems, the respective specific models can be retrieved and chained into a new specific model. In other words, a specific model is the same as a primitive module except that the granularity of the model is larger and the functionality is more specific. From this perspective, model formulating is a learning process for acquiring structural knowledge. This knowledge can be stored as new elements of primitive knowledge for reuse. Conventional methods for knowledge acquisition focus on acquiring the primitive knowledge/modules. The AIMM approach to knowledge acquisition is different from conventional methods in that it tries to acquire additional knowledge based on primitive knowledge and the users' needs to improve the system's performance.

Besides chaining primitive modules, creating a specific model in some cases is based on meta model and model-specific knowledge. However, the meta model cannot solve the specific problem unless it captures necessary information related to the specific problem. Problems with different grain sizes can be represented as meta models at different levels. Actually, users usually describe their problem at an abstract level, and the problem solver recognizes and finds a meta model that matches the problem. If the problem fits the meta model, then it will be further developed for a specific model by filling in information related to the problem at hand. More information about the problem can be acquired based on the meta model either from the user or from the model/knowledge base of the system. Once such additional information is learned, a specific model can be built for the problem and the attached solution procedure can be executed to produce a solution. Therefore, the meta model is used to link the possible problems of users and the possible solutions of respective meta models.

From the perspective of machine learning, AIMM is similar to learning by analogy, which is the type of task-oriented knowledge acquisition needed for problem solving. AIMM acquires new facts by transforming and augmenting existing primitive modules, meta models, and meta knowledge that bears strong similarity to the desired new concept or solution into a form effectively useful in the new situation. A learning-by-analogy system such as AIMM might be applied to chaining a collection of primitive modules dynamically into a specific model (it may be based on a meta model) that performs a solution procedure for a problem for which it was not originally designed. Like learning by analogy, which requires inferencing on the part of the learner, AIMM learns from the modeling task. Since one cannot acquire the requisite specific model without solving the problem, the learning inference mechanism that accounts for model formulation is a fundamental component of the total inference mechanism. Therefore, problem solving and knowledge acquisition are two views of the IA paradigm, which combines the earlier efforts of extending the expert system technique with the current issues of knowledge acquisition into a single approach.

## 4. Implementation of an AIMM Prototype

THE MOST CREDIBLE DEMONSTRATION OF IA POWER IS WITH A RUNNING PROTOTYPE. The primary objective of this AIMM prototype system is to produce evidence showing the feasibility of the intelligent agent approach to support modeling and problem solving in both the MIS and AI fields. The scope of this research is to address the design and implementation of an effective Intelligent Agent system but confine the testing to technical feasibility.

The AIMM prototype has been developed on a TI Explorer II/LX (Lisp Machine) using the Automated Reasoning Tool (ART) expert system shell. ART was selected due to its reasoning capabilities and frame representation abilities. The TI Explorer was used because of its graphical capacity and Lisp intervention facilities. The prototype is designed to be modular; it is divided into more manageable subsystems that can be implemented and enhanced independently. The prototype system consists of three components, a user-interactive dialog component, an application model/knowledge base component, and an intelligent-agent reasoning mechanism. A set of ART rules implements the user interactive component, which provides the user with asynchronous menus to interrogate AIMM. A simple menu window with its associated help messages can aid the user in picking information by mouse, or by using a command window that provides a limited mechanism to handle typed input.

## 4.1. Model/Knowledge Representation

The AIMM prototype has been developed for classes of problems using financial models. Mathematical programming models have also been successful on the AIMM prototype as reported in [22]. The typical financial models can generally be expressed by formulas that are quantitative relationships among financial, accounting, and economic variables. For example, the following financial formulas are primitive modules for doing Cost–Volume–Profit (CVP) analysis:

Profit = Total Revenue - Total Cost,

Profit Margin = Total Revenue - Variable Cost,

Total Revenue = Selling Price × Volume Sold,

Total Cost = Fixed Cost + Variable Cost,

Variable Cost = Unit Variable Cost × Volume Made,

Break Even Point = (Fixed Cost + Profit)/Unit Contribution Margin,

Break Even Point = (Fixed Cost + Profit)/ Contribution Margin Ratio,

Unit Contribution Margin = Selling Price - Unit Variable Cost, and

Contribution Margin Ratio = Unit Contribution Margin / Selling Price.

“Profit,” “Profit Margin,” etc., are also referred to as the modules’ names. The formulas can be decomposed into a set of mathematical operations on specified data items that are represented and stored as primitive modules.

In this prototype system, these modules (or formulas) are implemented as a frame-like representation by ART schema. Each frame stores the basic knowledge such as input/output parameters, constraints, and computation procedures. It associates knowledge not only about the module, but also how to use each module, and how each module relates to the others, all of which may be used in model explanations. Knowledge about a module also contains key information associated with each of its inputs. The key value relevant to the inputs would be supplied by default or modified by the user. Other default knowledge about data items, such as data units, can also reduce the search time of processing by selecting the appropriate modules for the desired units. All these types of knowledge are model-specific knowledge. Meta knowledge about a specific model contains knowledge about the model selection, usage, and behavior. Along with these aspects are the definitions that could be used to build explanations for the user. An example from CVP analysis is the Profit Margin Model:

![](/api/attachments/JYPFAWC6/fulltext/images/b2f0244b85a4b46c7b42399c523cce806d91f5490a4d4c84955dc1dafc4c5bbb.jpg)  
Figure 3. CVP Model Base

WHAT-IS product profit margin is sales revenue less direct product cost

WHEN-THIS output-unit = dollar counting-unit = product

HOW-TO total-revenue - variable cost

WHY-THIS since the required profit is counted by product, the fixed cost is not involved.

In a frame-based representation, models and model-specific knowledge, such as input/output parameters or variables, default values, or other constraints, and computation procedures, can be represented by the slots of attributes, inheritance relations, and attach procedures. In other words, all primitive modules and relative knowledge are stored in the unified ART schema and all these schema are grouped into a model/knowledge base. The following are sample model/knowledge frames for the CVP prototype that show definitional and default information important in easing the burden on the user and in locating initial data values for the model:

(defschema profit
"profit of department"
(is-a model)
(definition "An organization's profit is equal to
the difference of the revenue and total cost.")
(default-unit dollar)
(default-entity department)
(default-period 1988)
(model-output)
(parm revenue cost))
(defschema profit-margin
"profit of product"
(is-a model)
(definition "product sales revenue less direct product cost.")
(default-unit dollar)
(default-entity product)
(default-period 1988)
(model-output)
(parm revenue variable cost))
(defschema revenue
"revenue of product"
(is-a model)
(definition "Total revenues are a function of the unit sales volume
selling price.")
(default-unit dollar)
(default-entity product)
(default-period nov)
(model-output)
(parm selling-price volume-sold))

The ART schema allows a graphic view of the model base as a relational network that connects each module by the specified relation (e.g., instance-of) explicitly or by the input/output parameters implicitly. Figure 3 shows a model base that collects primitive modules for CVP analysis. For a specific problem, a specific model would be developed by chaining primitive modules from a module base and would be represented by structured primitive modules. Figure 2 showed the specific model for dealing with Profit.

## 4.2. Menu and Request System

Malhotra's experiment [23] concluded that two major classes of queries—requests about the problem situation and requests about the system—are considered in a management support system. AIMM captures these requirements as a top-level menu (shown in Figure 4), which supports four model-related queries to assist the user in formulating and evaluating models. First, "How is the <goal-variable> calculated?" is to provide a definitional explanation of the model. This question can also be used to show what the primitive modules (capabilities) of the system would support. Second, "What is the <goal-variable> in current circumstance?" is to help the user to integrate and evaluate a model for a specific variable without any restrictions. This question type is usually used to formulate a specific model for generating the value of a target variable in the current circumstance. Third, "What is the <goal-variable> if <decision-variable>?" is to help formulate a model that includes an objective function and constraint functions. The fourth will select and call an optimization routine for the specific model.

<table><tr><td>AIMM MODELING AGENTYou are standing in the AIMM modeling environment.Your options are:1. How is thecalculated?2. What is thein current circumstance?3. What is theif?4. What is the bestif?5. Reset the AIMM environment.6. Retire from AIMM.</td><td>ROOTClearLoadResetWatchRunStepBrowseIcon EditorMiscellaneousExamplesExit</td></tr><tr><td>COMMAND WINDOW</td><td>MODELING BLACKBOARD</td></tr></table>

Figure 4. AIMM Top-Level Menu

The user can select any question by clicking the mouse and enter a goal by clicking on a variable list or typing the proper variable. Depending on the question type selected, the user is prompted to provide desired variables (sink or goal) and/or decision variables (source). It was assumed that on completing the identification session, the system would have an identification of the overall goal (sink) of the problem and/or the decision variables (sources) which are determined by the user. Examples such as “What was the profit of plant X last year?” can be interpreted as “Finding a collection of modules that can evaluate the profit (sink) from the current available data.” “How many units must be sold to meet a target profit?” can be interpreted as “Finding a collection of modules that can evaluate Volume-sold (sink) by transferring information from Profit (source).” And “What profit will be earned under estimated sales volume?” can be interpreted as “Finding a collection of modules that can evaluate the Profit (sink) from Volume-Sold (source)." Although the question itself may not be stated clearly in one of these forms, informal observations indicate that the intention of most utterances falls within one of these question types.

![](/api/attachments/JYPFAWC6/fulltext/images/663dbe0e7e2530025f0dae423eeb1948b7817db2cdc6c1cc7481fc556d646be7.jpg)  
Figure 5. AIMM Explanation of Break-even

The first three types of questions can be examined at any time in any order. However, a user may wish to know the system's capabilities before applying them to the problems. This can be accomplished with the first type of question to access information that describes the specific features. Figure 5 is an example where AIMM presents a definition of the breakeven point model. The other questions can then be requested to chain a specific model from the available modules of the system for a problem. The detailed interactions of modeling and the evaluated result for each question would be shown on the command window. The final result of each question would also be kept on the modeling blackboard window unless the system is asked to reset the environment. The results or alternatives on the modeling blackboard window assist the user in making a decision.

## 4.3. Modeling Process Mechanism

Once the problem type and the sink and/or source of the problem have been determined, the modeling process will be handled by the reasoning mechanism of AIMM. The reasoning process is actually a set of ART rules (and Lisp functions) generic for all applications. The task of AIMM then can be regarded as formulating a model from the source (data) to the sink (goal) by chaining primitive modules from the model base.

![](/api/attachments/JYPFAWC6/fulltext/images/e98bac64e9b10f6408d8f4357c22fd0f114ebae33240c544fb4fbc06a1af6a64.jpg)  
Figure 6. Break-even Model Structure

An advantage of using source/sink in problem solving is that it can flexibly mix backward chaining with forward chaining. In the case of consultation, the system may first use backward chaining because the user has a specified goal (sink); however, it may switch automatically to forward chaining if an unexpected but relevant piece of information is volunteered by the user. There are always two directions to the reasoning, and whenever one is stuck it is possible to switch to the other direction. If an important piece of information is missing, such as fixed cost, the user could provide either the data or the model extension.

Fundamental types of questions, such as “What was the net profit of department X in 1988?”, “What is the profit contribution of product A?”, and “What is the break-even point that must be sold?”, request the formulation and evaluation of a specific model. These questions specify a request for model evaluation of a goal variable, and cause a search for input names. Those inputs that are required for each of the modules may be either data items of the database or the outputs of other modules. For example, “Profit” may be defined as the difference between “Revenue” and “Total cost” where “Total cost” itself is the sum of “Fixed cost” and “Variable cost.” The IA system will treat this type of module as data. The goal-directed reasoning will dynamically explore and chain all related modules until all inputs of modules can be either retrieved from the database through standard data access methods or provided by the user. Figure 6 shows such a structural model for breakeven point analysis.

```txt
AIMM MODELING AGENT
You are standing in the modeling environment which can formulate and evaluate models for the desired variables.
Your options are:
Enter the goal variable.
Evaluate the goal variable.
Examine current models.
Exit from model evaluating.

COMMAND WINDOW
Now: You have specified the desirable variable: BREAK-EVEN and a model will be chained to evaluate this variable.
Break-even point to be computed by the number of units (u) or by the sales of dollars (d)? Enter (u or d) → d
Object: Variable is currently evaluated by model REVENUE-SALE assuming (1) Entity = PRODUCT1
(2) Period = DEC
Enter (y) to accept; or enter (1) or (2) to change default → y
Accept default of model REVENUE-SALE where entity = PRODUCT1, Period = DEC
AIMM assumes the target PROFIT of break-even point = 0 unit-contribution-model chained and/or executed contribution-ratio-model chained and/or executed revenue-model chained and/or executed volume-model chained and/or executed breakeven-model chained and/or executed Object: Variable REVENUE-SALE = 115000.0 is obtained by above models where entity = PRODUCT1, period = DEC

ROOT
Clear
Load
Reset
Watch
Run
Step
Browse
Icon Editor
Miscellaneous
Examples
Exit

MODELING BLACKBOARD
if PROFIT = 0
VOLUME-MUST-SOLD = 23000.0
if PROFIT = 0
REVENUE-SALE = 115000.0
```  
Figure 7. AIMM Break-even Session

A calculation procedure that is attached to each module can be executed whenever inputs of the respective modules are available; but the modules' (output) value can be produced for only those keys that are consistent with all inputs. For example, Profit is calculated by the default "Plant" or "Department" and then each of its inputs (Revenue and Cost) must have values constrained by the plant or the department. Furthermore, Profit cannot be calculated by "Product" as the key value. However, the Profit of a product can be defined as Profit-contribution and it can be calculated by the product since each input of the Contribution model (Revenue and Variable-cost) can be defined by a product. This default transition and consistency checking are called default propagation.

A question such as “What would the profit be if sales were \$55?” needs a more specific model than the fundamental “What is the profit?” In the AIMM prototype, the above statement about a given situation can be formed as a pair (source, sink). As examples, “What would profit (sink) be if sales (source) were \$55 million?” and “How would sales (sink) have decreased the price if Product 1 were to give a margin (source) of \$2?” If the problem goals are expressed in terms of source/sink, it can then proceed to perform a solution-seeking process more effectively. Both source and sink help narrow the search space and prevent exhaustive searching through irrelevant models. In fact, the user should be able to volunteer information about his problem either in the initial stage or at any point in the problem-solving process. A session of this type of questioning appears in Figure 7 for the breakeven analysis of Figure 6.

## 5. Conclusion

A CONSULTING INTELLIGENT AGENT, WHICH IS AN APPROACH that can offer the user (1) an automatic, flexible, reasoning process, and (2) a supportive, adaptable, man-machine interaction, has been developed to increase the utility and effectiveness of DSS or other application systems. This Agent for Intelligent Model Management (AIMM) makes a wide variety of models available to decision makers so that they may apply these models without becoming involved in the technical and/or procedural aspects of implementation. This research has strongly proposed a modular approach to model management, which allows models to be decomposed into a collection of primitive modules stored in a central model base. A unified representation has been proposed not only to represent primitive modules (e.g., input, output, and computation procedures) but also to store knowledge about the modeling, and knowledge related to other primitive modules. The modeling process has been designed as a learning and reasoning process that is based on various reasoning techniques and focuses on the process of dynamic chaining and integration. A prototype highlights the features of AIMM.

AIMM achieves learning in two ways. On the one hand, the system can dynamically chain a set of appropriate primitive modules that are based on the probable sink and/or sources. The second method of learning is more sophisticated. The specific model for solving a certain problem is formulated by acquiring further problem-specific knowledge that is based on an existing meta model. The dynamic chaining process can also be invoked whenever sinks and sources are determined by the meta model. All primitive modules and meta models are supposed to be implemented with meta knowledge in a model/knowledge base before they are used to formulate specific models for solving problems.

AIMM currently concentrates on the model management component of DSS for demonstrating the IA approach. Future work requires that the current database access of the described AIMM prototype address full DSS database concerns. A more sophisticated dialogue for AIMM is also under investigation. Another important extension of this research is to explore a possible approach for acquiring primitive modules of problem domains and meta models of management science. The system should provide an interface through which new primitive modules and meta models can be added into the current support. This learning process must be able to acquire necessary meta knowledge for using such new items and relating other old items of the model/knowledge base.

## REFERENCES

1. Amarel, S. Problem Solving: Article for Encyclopedia of Artificial Intelligence. Technical Report DCS-TR-188, Rutgers University, New Brunswick, NJ, 1986.
2. Applegate, L. M.; Klein, G.; Konsynski, B. R.; and Nunamaker, J. R., Jr. Model man-

18. Kottemann, J. E., and Dolk, D. R. Process-oriented constructs for model integration.

agement systems: proposed model representations and future designs. Proceedings of the Sixth International Conference on Information Systems (1985).

3. Blanning, R. W. A relational framework for model management in decision support systems. Proceedings of the International Conference on Decision Support Systems, DSS-82 Transactions (1982), 16–28.

4. Bonczek, R. H.; Holsapple, C. W.; and Whinston, A. B. Foundations to Decision Support Systems. New York: Academic Press, 1981.

5. Bonczek, R. H.; Holsapple, C. W.; and Whinston, A. B. The evolving roles of models in the decision support systems. Decision Sciences, 11, 4 (Fall 1980), 337–356.

6. Bradley, G. H., and Clemence, R. D., Jr. Model integration with a typed executive modeling language. Proceedings of the Twenty-first Hawaii International Conference on Systems Sciences, IEEE THO213–98 (1988), 403–410.

7. Bu-Halaiga, M. I., and Jain, H. K. An interactive plan-based procedure for model integration in DSS. Proceedings of the Twenty-first Hawaii International Conference of System Science, IEEE THO213–98 (1988), 428–434.

8. Courtney, J. F., Jr., and Paradice, D. B. A knowledge-based DSS for managerial problem diagnosis. Sciences, 18, 3 (Summer 1987), 373–399.

9. Dolk, D. R., and Konsynski, B. R. Knowledge representation in model management systems. IEEE Transactions on Software Engineering, 10, 6 (November 1984), 619–628.

10. Elam, J. J.; Henderson, J. C.; and Miller, L. W. Model management systems: an approach to decision support in complex organizations. Proceedings of the International Conference on Information Systems (1980), 98–110.

11. Elam, J. J., and Konsynski, B. R. Using artificial intelligence techniques to enhance the capabilities of model management systems. Decision Sciences, 18, 3 (Summer 1987), 487–502.

12. Geoffrion, A. M. An introduction to structured modeling. Management Science, 33, 5 (May 1987), 547–588.

13. Huang, P. W. The Formulation and Applications of an Intelligent Agent Model. Ph.D. dissertation, Southern Methodist University, School of Engineering and Applied Science, Dallas, TX, 1989.

14. Klein, G. Developing model strings for model managers. JMIS, 3, 2 (Fall 1986), 94-110.

15. Klein, G., and Cabrera, M. L. Optimal model integration for a DSS. Proceedings of the Nineteenth Hawaii International Conference of System Science (1986).

16. Klein, G.; Konsynski, B. R.; and Beck, P. O. A linear representation for model management in a DSS. JMIS, 2, 2 (Fall 1985), 40–54.

17. Klein, G.; Yun, D. Y. Y.; and Liu, J. I. C. Artificial intelligence in the architecture of decision support systems. Proceedings of the Conference on the Impact of Artificial Intelligence on Business and Industry (1988), 20–39.

NPS Working Paper 88–05, Naval Postgraduate School, Monterey, CA 93943, March 1988.
19. Lenard, M. L. Representing models as data. JMIS, 2, 4 (Spring 1986), 36–48.
20. Liang, T. P. Reasoning in model management systems. Proceedings of the Twenty-first

20. Liang, T. P. Reasoning in model management systems. Proceedings of the Twenty-first Hawaii International Conference on System Science, IEEE THO213-98 (1988), 461-470.

21. Liang, T. P. Development of a knowledge-based model management system. Operations Research, 36, 6 (November/December 1988), 849–863.

22. Liu, J. I. C.; Yun, D. Y. Y.; and Klein, G. An intelligent agent consulting system for production and operations management. Proceedings of the Third International Conference on Expert Systems and the Leading Edge in Production and Operations Management (1989), 1157–1172.

23. Malhotra, A. Knowledge-based English language systems for management support: an analysis of requirements. Proceedings of 4th IJCAI, 2 (1975), 842–847.

24. Muhanna, W. A., and Pick, R. A. Composite models in SYMMS. Proceedings of the Twenty-first Hawaii International Conference on Systems Sciences, Vol. II. IEEE Computer Society Press, 1988, 418–427.

25. Reiter, R. A logic for default reasoning. Artificial Intelligence, 13, 2 (April 1980), 81–132.

26. Sprague, R. H., and Carlson, E. D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall, 1982.

27. Stefik, M. Planning with constraints, MOLGEN: part 1. Artificial Intelligence, 16, 3 (May 1981), 141–169.

28. Turban, E., and Watkins, P. R. Integrating expert systems and decision support systems. MIS Quarterly, 10, 2 (June 1986), 121–136.

29. Weber, E. S., and Konsynski, B. R. Problem management: neglected elements in decision support systems. JMIS, 4, 3 (Winter 1987/88), 64–81.

30. Yun, D. Y. Y., and Loeb, D. The CMS-HELP expert system. Proceedings of the International Conference on Data Engineering (1984), 459–466.
