---
otero_id: 17315
otero_key: "P4GGEU7G"
title: "Model type selection in an integrated DSS environment"
authors: "Snehamay Banerjee; Amit Basu"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90024-w"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model type selection in an integrated DSS environment

Snehamay Banerjee

Drexel University, Philadelphia, PA 19104, USA

Amit Basu

Vanderbilt University, Nashville, TN 37203, USA

Effective computer based support for the use of analytic models in management decision making requires model management systems (MMS) that facilitate all phases of the modeling process. Existing approaches to the design of MMS commonly assume that the type of model needed to solve each problem is predetermined by the decision maker. This is a limited view, since determination of the appropriate model type is a difficult task, and is hampered by the subjective preferences of individuals. In this paper, we describe the model (type) selection process, argue why support for this should be integral to MMS design, and overview an approach to the design of the model selection subsystem in an integrated DSS.

Keywords: Model management, Decision support systems, Knowledge based systems, Model selection, Management science

![](/api/attachments/P4GGEU7G/fulltext/images/21e6c5d99db965788f46542e8858b12028b9efe92db302808648af2dc6d921ea.jpg)

Snehamay Banerjee is an Assistant Professor of MIS in the College of Business at Drexel University. He holds B. Tech and M. Tech in engineering from India, MS from Case Western Reserve University, and Ph.D. from University of Maryland at College Park. His research work are to appear in Information and Management and International Journal of Product Technology. His current research interests include knowledge based systems and their uses in man-

agement science, model management, and electronic data interchange.

## 1. Introduction

One of the persistent challenges faced by a manager is to comprehend and respond in a timely manner to the threats and opportunities of the market place with decisions that will make the best use of the corporate resources. Several factors amplify the complexities associated with making such decisions. These include unpredictable political and financial environments, competitors' strategies and unpredictable consumer behavior. Consequently, the problem underlying a decision is often articulated by the manager/decision maker in an informal manner, with too many components interacting in unspecified ways. Solution of the problem is possible only after the problem description is substantially refined and structured, and a suitable model formulated. Given the non-trivial effort required for each of these steps, a system such as a decision support system (DSS) that can structure and simplify the problem, and present the complex interactions of the problem parameters in a comprehensible manner, is of great potential value.

A DSS is an effective combination of many interrelated components (e.g., data base, knowledge base, model base, solver base) which is used

![](/api/attachments/P4GGEU7G/fulltext/images/2a9a5f117d445d28ed41f94e18c8f0ef8f083796fd20b281d227d38bee50f212.jpg)

Correspondence to: Amit Basu, Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203, USA. (615) 322-7043.

by a decision maker to aid in the decision making process. The DSS helps a user comprehend the complex interactions between various problem parameters by presenting such information in an intelligible manner (e.g., the impact of cost increase of a raw material on the product mix decision or the impact of an added teller on average customer waiting time in a bank). There are many varying definitions of DSS $[5,34]$ with differing viewpoints on structures, tasks, expected level of user sophistication, etc. However, these varying definitions agree that a DSS must aid decision makers by providing realistic and useful information, derived through effective incorporation of models in the solution procedure, using appropriate user interfaces. The focus of DSS is not on increasing the efficiency of solving a well defined and structured procedure but on improving the effectiveness of the decision making process. Effectiveness requires the decision makers to adapt and learn, to make responsive adjustment to changes in the environment for and within which they make decisions $[6]$ . An effective DSS must help decision makers adapt to changes in the environment by helping them solve their problems in a manner that reflect reality and not force the decision makers make compromises so that problem descriptions can fit existing solution procedures. Therefore, different solution procedures may be used to solve similar problems under different conditions. Similar problems under different contexts may have to be solved differently.

Modeling activities are routinely performed by management scientists, who are skilled analytic persons, to help decision makers solve their problems. The desired roles of such specialists and the problem solving phases in which they should be involved have been discussed by many researchers $[1,2,17–19,26]$ . Several critical observations have been made by these researchers about the impact of such specialists and the use of analytical solution procedures (including management science techniques) on the business decision making process. These include the following:

\- Managers do not make wide use of management science techniques to solve complex business problems;

\- Problem models are often built based on what solution procedures are familiar or available.

This may lead to simplistic assumptions or exclusion of important features;

\- There is a lack of user participation in defining the problem and in developing the model;

\- There is often a lack of manager confidence in the DSS output;

\- Managers may not be aware of the fact that the problem at hand can be solved by the solution procedures that are available to them.

As a result the use of analytical models and the associated mathematical solution procedures in business appears to be ad-hoc [19]. In order to use model based DSS effectively in a decision making paradigm we need to get the decision makers more involved in different problem solving phases and make the significance of various tradeoffs understandable to them.

It is clear that if DSS are to become useful tools in the task of problem modeling and analysis, they must incorporate capabilities for a variety of model management functions, such as model selection, formulation, control, and synthesis. The focus of this paper is upon the first of these functions, namely model selection (or more precisely model type selection). For the purpose of clarity we distinguish between model types and model instances. A model instance is a specific formal representation of a problem instance in some desirable form e.g., algebraic, which can be used to solve the problem. A model type is a (possibly infinite) collection of model instances characterized by a set of rules and/or properties that distinguish instances of that model type from those of other model types. For example, capacitated minimal flow network algorithms represent a model type and “Min. $3x_{1} + 4x_{2}$ subject to $x_{1} + 2x_{2} \geqslant 100$ ” is a model instance of the linear programming model type. It is our contention that the ability to identify a model type for a problem is an important feature in model based DSS. Therefore, our focus in this paper is on developing a methodology to help identify a model type for a given problem instance. We do not directly address the problems of formulation and execution of model instances after the type has been determined. These later problems have been extensively studied in the literature. Therefore, unless otherwise specified, we will refer to model types as models in the rest of the paper, and to the model type selection problem as the model selection problem.

The identification of a model type for a problem instance is complicated by several factors that include:

(1) There are a large number of models and the list is growing;

(2) The application domains of different models are not mutually exclusive;

(3) Frequent users (and modelers) tend to develop preferences for certain models. Thus they tend to lose desired flexibility to represent a problem;

(4) Selection of a model depends not only on the problem description, but also on the resources available to solve the problem. These resources include not only direct factors such as efficient solvers, but also factors such as funds and human skills.

At the same time, inclusion of the model selection function in DSS is becoming increasingly important and relevant. There are several reasons for this. Increased use of end-user computing has resulted in more decision makers wanting to address decision problems directly, rather than using technical experts (i.e., management scientists) as intermediaries. Furthermore, model selection is becoming an ongoing (or at least periodic) activity, rather than a one-time activity. This is because the choice of a model type to represent the problem is significantly influenced by various environmental factors, and an increasingly complex and volatile business environment forces periodic re-evaluation of the applicability of models. Also, as users get more involved in interactive decision support systems, the demand for 'what-if' analysis increases. As the problem parameters are modified, model selection procedures are needed to identify alternative models to represent and solve the modified problem.

In this paper we discuss the role of the model selection process in the model management subsystem of a DSS, and propose a methodology to systematically guide the users to progressively obtain needed information and make intelligent tradeoffs for selecting model type that reflects reality under given economic, technological, and other constraints. This paper is organized in 6 sections. In Section 2 we present an overview of the current research on DSS and specifically on model management issues. Section 3 presents an overview of DSS by describing different components of DSS and their interactions that help us define the role and scope of the model selection process. Section 4 presents a hierarchical taxonomy that is useful for organizing different classes of models. Based on this taxonomy, in Section 5 we present a formal representation of models based on frames. An example illustrates the concepts presented in this paper. Finally in Section 6 we conclude by discussing potential hurdles that need to be crossed before an effective model selection system can be implemented.

## 2. Overview of current research

Recent research on model based DSS has focused on various aspects of modeling which include model construction, model manipulation, model representation, and modeling language. An ideal DSS may be a system that will interact with appropriate data bases, knowledge bases, model bases, and solver bases to effectively solve a wide range of business problems without expecting extensive user knowledge. The state-of-the-art is far from achieving this goal, and such an ultimate goal is perhaps not fully attainable. However, past DSS research has suggested solutions to improve different DSS functions.

Problem structuring concepts have been studied extensively and a comprehensive summary of problem structuring methodologies is found in $[44]$ . Smith proposes a decompositional approach to problem structuring and suggests the idea of matching structurable tasks to relevant techniques $[45]$ . Other notable work includes that of Woolley and Pidd $[50]$ , who looked at problem structuring as a part of or prelude to problem modeling, Taylor $[46]$ provides a state space based idea for problem structuring, and in $[43]$ a decompositional approach to problem structuring is presented.

Past research on model selection has been very limited because of the difficulties associated with this stage. Approaches used for model type identification include Liang [30] and Watson [47] who propose the selection of a solution procedure randomly from a feasible set, Kumar and Hsu [29] and Wheelright and Makridakis [48] use a scoring model to evaluate all potential solution techniques based on predetermined set of criteria, [21] uses a decision matrix, and [3,25] suggest different approaches to organize the model types in a knowledge base. Most of these methods are not in a form that can be used for practical automation, and current DSS rely on the expertise and experience of management scientists at this stage.

The area of model instantiation is a very active field of research that has developed modeling languages with sufficient expressive power to capture the intricacies of different problems. Structured Modeling [19,20] uses acyclic graphs to represent a model and views a model as being composed of five discrete types of elements to represent knowledge about a problem. Structured modeling can also be used to design and implement an integrated information systems architecture. GAMS [27] uses a similar structure with different notations for problem representation. PM\* and PDM [28] are first-order logic (FOL) based approaches to problem formulation where the problem domain is restricted to production-distribution-inventory environments. In [7,8] a FOL based approach is presented which is problem domain independent and is a combination of two modeling languages. Murphy and Stohr [41] use a number of theoretically derived rules to help build large Linear Programming models.

Other model management research focuses on the storage, execution, utilization, and manipulation of models that have been developed. Early researchers treated models as data in order to utilize database management theories to this new field. Blanning [10–12] proposes to store model information as records to create a model base and used relational database concepts to manipulate model base. In [31–33] a graph based approach is suggested where a model is represented as an acyclic directed graph. Dutta and Basu [16] use FOL to represent the parameters for, and conditions of executing a model. Dolk [15] proposes various levels of abstractions in model management and suggests the use of frames as a vehicle for implementing these ideas.

Finally the area of user interface design which had been, and still is, an active research area has produced interesting insight to interface design from different perspectives, e.g., differences in user characteristics [13], special requirement for different tasks that include model oriented DSS [42] and application programs [4], use of natural languages [9], looking at different learning stages [22,40], and human factors [39]. However, as the nature and level of human computer interaction changes this field will keep evolving to keep up with the changing environment.

The above research has contributed significantly to the enhancement of DSS. However, there is much yet to be done before DSS can provide automated, intelligent, reliable, user friendly decision support. Because of the inherent diversity of the problem descriptions and their associated environments and the diversities of potential solution procedures it may be impossible to develop a DSS that can fully automate the problem solving process even for the simplest of the business problems. The aim of DSS research is not to eliminate the human being from the problem solving process but to facilitate the process by solving more structured parts without much interaction from the decision makers and guiding decision makers by providing them with relevant information at appropriate stages.

![](/api/attachments/P4GGEU7G/fulltext/images/888b7d8f23a26d19585724d3c9ec29299862c47e028dd85a73bd2000b9fe6c15.jpg)  
Nomenclature: Solid lines represent both control and information flow
Dashed lines represent information flow only  
Fig. 1. DSS architecture in integrated modeling environment.

## 3. Model management in decision support systems

A decision support system consists of several interacting processes or subsystems some of which need to be performed iteratively. Figure 1 presents a schematic view of these interacting processes which are listed below:

– Problem requirements analysis;

\- Problem structuring including necessary problem decomposition;

\- Model type selection;

\- Model instance formulation;

\- Model execution and control;

\- Model storage and retrieval;

\- Data base management;

\- Knowledge base management;

\- Dialogue management.

The processes associated with data base and knowledge base management are well documented in the literature. Though these processes are essential for a DSS these are not the proprietary functions of DSS. We focus our attention in this section to those components that are unique to DSS, namely, problem structuring, model type identification, model formulation and execution. Figure 2 provides a more elaborate view of these components and their interactions.

Problem analysis and structuring methods have been studied extensively in the literature. Existing approaches range from purely cognitive descriptions to a mixture of formal and informal descriptions that can at least partially facilitate machine representation and manipulation of the problem model. We present a general problem representation structure to capture essential problem and environmental characteristics that can be translated into many of the existing detailed representation methods. This representation scheme is based on the observation that problem formulation shares the same basic attributes of description as system development. Both problems and systems are described in terms of stimuli (inputs), responses (outputs), state (data structures), and procedures (control structures). Thus, similar representation structures can be used for both problems and systems. The essential theory behind this approach of problem structuring comes from the formal theory of box structure information systems development described in [23,36,37]. A complete description and evaluation of systemic problem structuring with box structures can be found in [24]. Here we provide a brief overview of the process.

![](/api/attachments/P4GGEU7G/fulltext/images/7dd7fd7db96c8cc05142208574faa9dc927ea76a6be18e0a969837645fc2f88c.jpg)  
Fig. 2. Schematic view of interactions between modeling subsystems.

Box structures support the manager in dealing with a problem at different levels of abstraction, from describing the complete problem as a high level abstraction through discovering subproblems at lower levels of problem abstraction. Three basic principles underlie the box-structured design process [35]:

(1) All data to be defined and stored in the design are hidden in data abstractions;

(2) All processing is defined by sequential and concurrent uses of data abstractions;

(3) Each use of data abstraction in the system occupies a distinct place in the usage hierarchy of the system.

Box structure methods define a single data abstraction in three forms in order to isolate the creative design steps involved in building the abstraction. The black box gives an external description of data abstraction behavior in terms of stimulus histories to responses. The black box is the most abstract description of system behavior and can be considered as a formal requirements statement for the system. The state box includes a designed state and an internal data abstraction that transforms the stimulus and an initial state into the response and a new state. The state is designed from an analysis of the required stimulus histories and responses for the system. Finally, the clear box replaces the internal data abstraction with the designed sequential or concurrent usage of other black boxes. These other black boxes are new data abstractions that are expanded at the next level of the system box structure hierarchy into state box and clear box forms. Formal, mathematical definitions and relationships of the three box structures are presented in [37].

In order to gain intellectual control over the development of a complex system, it is necessary to be able to decompose the system into smaller, more manageable parts. Analogously, a problem can be broken into several, better understood subproblems leaving design trails in the decomposition process so that more formal inspection of such process can be performed. Such steps for problem analysis are discussed in $[24]$ . There is no escaping the necessity for creativity in the problem structuring process, but these steps isolate and embed it in a way that allows review in canonical forms.

A box structure usage hierarchy represents the usage of black box data abstractions in a higher level clear box data abstraction. A usage hierarchy of data abstractions provides referential transparency among all black boxes within a clear box. Thus, each black box (i.e., subproblem) can be designed independently of the others. The usage hierarchy provides the intellectual control of the structuring process. The collection of relationships between subproblems in the clear box description provides guidance to control the solution process of the overall problem. The underlying assumption in this structuring process is that at the final stage of the structuring process each of the subproblem descriptions will be simple enough so that it can be represented by one model. The creation of a meta model for a complex problem is done by combining these models using the clear box descriptions obtained through the usage hierarchy.

The model type selection subsystem of a DSS presents a formidable task. One of the major obstacles is the lack of structure and procedures for this process. Lack of required information on the problem, its environment, and the data needed to solve the problem makes the selection process even more difficult. Management scientists have developed many mathematically sophisticated procedures that can efficiently solve a problem that meets the rigid specification of the solution procedures. However, it is not only the problem description but also the problem environment that influences the choice of the problem solution method. Factors that contribute to the model type selection process can be categorized as follows:

\- Environmental factors. This refers to the nature of the organization and industry in which this problem has been observed. For example, if a set of goods have to be transferred from a set of sources to a set of destinations it is a transportation (optimization) problem. However, environmental factors can change the perception of the problem. If the problem is for a company sending products from factories to warehouses, then it is a cost minimization problem. If it is a church trying to reach a disaster area with medical supplies then the problem is not a cost minimization problem but how to reach the maximum number of people with existing supplies, and if it is a military operation during war then the problem is one of finding a feasible solution satisfying several time and place constraints.

\- Functional factors. This relates to the internal characteristics of the problem. For example, a manufacturer offers a $5\%$ discount if the quantity ordered is more than 100000 units where the price of each unit of material is not significant. Though the relationship between the cost and quantity parameters are not linear because of the complexities involved in dealing with non linear relationships it may be more practical to approximate the relationship by a linear one. If, however, the product was a mainframe computer and the company was offering a gradually increasing discount for each additional computer ordered then it will be impractical to consider the relationship as linear.

\- Technological factors. These factors set practical limitations on the size of the problem that can be solved, the accuracy that can be expected from the problem solution, or the time required to solve the problem. For example, products may have to be grouped together if the software has a limitation on the number of variables it can handle, or an algorithm with less calculations may have to be used if we want a speedier execution even though it may provide an inferior result.

\- Economic factors. This is one of the major factors influencing the selection of model types.

The cost justification for solving a problem dictates the type of resources that can be made available to solve the problem. For example, if data required to solve the problem using a particular model type is not available then such data has to be obtained from another source. If the cost associated with obtaining such data outweighs the potential benefits from solving the problem accurately then an alternate model type to solve the problem has to be considered. This obviously compromises the quality of the problem solution but may still be a more practical way to solve a problem.

\- Subjective factors. There have been several arguments in the research literature on the need to eliminate the personal bias and other subjective factors from the model type selection process. It is our contention that such a step is neither practical nor necessary. Problem solvers must have faith in the solution process. If a user feels comfortable with a specific method, there is a higher likelihood that output from that model will be acceptable to that user. Such subjective factors should be considered in the selection of a model type for a problem.

Once a model type has been identified for a problem, methods such as structured modeling $[19]$ can be used to formulate the problem. Procedures to represent and manipulate such representations in the machine and execute such formulations by accessing appropriate data bases and tool bases are well documented in the literature. Two key observations that are pertinent to the design of effective DSS are:

\- The problem solving process is an evolving procedure which gets modified as more and more information becomes available and the user makes necessary tradeoffs based on better understanding of the problem and its environment. So the model type selection process also evolves as the user compares the problem information with knowledge needed for model type selection.

\- The user may not have an idea about how to proceed at any given stage with the type of information available, and may need guidance towards better understanding and use of the available information. This in turn can help determine what additional information is needed about the problem in order to successfully identify an appropriate model type.

## 4. A taxonomy of model types

In order to provide automated support for model selection, a framework to represent different model types is needed. Unfortunately, there are no clear procedural rules to differentiate between, and to choose from existing model types. Two observations that can be made about the selection process are:

(a) The emphasis of the selection process is on what the model type is capable of doing and not on how the solution procedure works. In other words the focus in model selection is on the structure of the model for a problem, not the process or procedural aspects of how it is manipulated to solve the problem. Therefore if two algorithms can be used to solve the same model of a problem, we do not differentiate them as two different model types. This separation of concern between ‘what?’ and ‘how?’ must be clearly maintained in developing any model type selection procedure.

(b) Different types of information (e.g., functional, environmental, economic etc.) will be needed to select a model type and it is impossible to deal with all such information at the same time. Thus there is a need for a stepwise refinement process of the model selection procedure that navigates through the information in a systematic manner by narrowing the focus of the search process from the broad environmental and economic factors to narrowly focused details of the specific problem instance.

In order to address these issues and to alleviate some of the problems associated with the model type selection process we describe a classification scheme that we have developed [3]. This organizes different models in a four level abstraction scheme. A major motivation for this classification scheme is that it requires broad problem characteristics at the higher levels of abstraction, and progressively more specific and detailed information at lower levels. Such a classification scheme facilitates both problem structuring and model type selection phases by providing focus for both activities. It should be noted that though the taxonomy is largely hierarchical, it is not a strict hierarchy since the application domains of different model types are not mutually exclusive [3]. The mechanism for superimposing such flexibility on the four level abstraction scheme discussed here is presented in the next section.

<table><tr><td>Abstraction Levels</td><td colspan="4">A Sample Set of Optimization Model Types</td></tr><tr><td>Environment Level</td><td>Forecasting</td><td>Optimization</td><td>Queueing ....</td><td></td></tr><tr><td>Structural Level</td><td colspan="2">Non-Linear Programming</td><td>Linear Programming</td><td></td></tr><tr><td>Instance Level</td><td>General LP</td><td>Integer Prog.</td><td>Assignment</td><td>Transportation</td></tr><tr><td>Solver Level</td><td>Simplex Algorithm</td><td>Revised Simplex Algorithm</td><td>Ellipsoid Algorithm</td><td></td></tr></table>

Fig. 3a. Abstraction levels of management science models.

The four abstraction levels in our taxonomy for organizing different model types are:

(a) The environment level;

(b) The structure level;

(c) The instance level;

(d) The solver level;

Note that because of the class subclass relationship a model type at the higher level of abstraction represents a group of similar model types at the lower level of abstraction. Figures 3a and 3b illustrate this classification scheme for two subsets of model types. Each of these categories are discussed below.

## The environment level

This is the highest level of abstraction in the classification scheme where a model type is viewed as a “black box”. That is, the essential elements of a model type here are its input types, output types and goals. A potential model type is determined by matching broad characteristics of the problem and its environment with the broad problem-solving characteristics of the model types. Information required for such classification are primarily obtained from environmental factors which help define the objective or goal of the problem. For example, in the transportation problem discussed earlier in this paper, environmental factors such as competition, and the strategic thrust of the corporation help decide whether the lowest cost transportation solution should be sought, or a feasible route given a set of time or place restrictions. It is easy to see that the relevant problem information for this purpose is directly captured by the black box view of its systemic representation. This provides a direct link between the problem structuring phase and the beginning of the model type identification phase. Each model type at this level corresponds to a significantly different perception of the problem to be solved. Therefore, once a model type has been selected at this level other model types become irrelevant unless the user makes significant modifications for the factors describing the environment that changes the overall objective of the problem to be solved.

![](/api/attachments/P4GGEU7G/fulltext/images/b8fdc438e7552f01b9aae0ca7907df3cf20fe24966fe8ed17423ee6bfd9093eb.jpg)  
Fig. 3b. Abstraction levels of queuing models.

## The structure level

The next level of model type classification is based on the structural characteristics of the parameters that define the model type which are mainly obtained from the functional factors of the problem instance. Potential representation of structural characteristics include relationship between problem parameters or the distribution function of a parameter (or decision variable). For example, in linear programming models, the relationship between all the variables must be linear, whereas in non-linear programming the relationship between at least one set of variables is non-linear. In the case of queuing problems, the service time is exponential or some other distribution. Such structural information about a problem instance is captured in the state description of its systemic structuring procedure (state variable properties, relationships between state variables). Many other problem structuring methods capture similar information in different formats. Note that selection at this level requires the user to delve into more specific details of the problem compared to the previous level and a given problem is not likely to fit into multiple models types at this level without modifying some structural characteristics of the problem instance.

## The parameter level

A model type is further classified at this level based on specific parameter values for a given instance that are used to differentiate model types. For example, a problem could be modeled as a single server problem or a multiple server problem, depending upon certain parameters (of the service facility). The difference between the Transportation models and Assignment models are based on the values of the variables of the right hand side of the constraints matrix (i.e., the b vector for the problem: Min. CX, Subject to $AX \geqslant b$ , $X \geqslant 0$ must be integer values for Transportation problems and must be unity for Assignment problems). The distinguishing characteristics of models at this level are mainly in terms of the domains of their different parameters, such as inputs and outputs. Given that domain characteristics of the features of one model type could include those of others, it is possible that the specific characteristics of a problem instance allow it to be matched with multiple model types at the parameter level, provided that they occur within the same structural class of models. For example, if a problem has a b vector whose members are all 1, then it can be treated as an instance of either the Assignment algorithm or the Transportation algorithm, since 1 is an integer value. This implies that models which are members of sibling classes at this level of the taxonomy can be used to solve a specific problem with minor or no changes in the problem description.

## The solver level

The final level of the taxonomy does not really distinguish between model types but it differentiates between different implementations and/or algorithms of a model type. Though problem parameters (e.g., number of decision variables) play a role in the selection process at this level, technological and economic factors which are not problem specific but a representation of the environment for and within which the problem is being solved play a major role. These criteria play a very important role in the selection process, since the feasibility of a particular model for a problem is dependent upon the availability of a convenient and acceptable solver and the economic feasibility of using such a solver. Other relevant factors that are considered at this level include speed of execution, storage requirement, accuracy of the output, and security specifications. A problem can be solved using sibling nodes at this level without imposing any restrictions on the problem description.

Subjective factors (e.g., the bias of a decision maker toward a particular model type) can always influence the selection process. Tradeoffs made at different levels of the selection process can also introduce some subjective bias in the selection process. However, the impact of such tradeoffs reduces as we move down the abstraction hierarchy. Moreover we are not looking for the best model to solve a problem but merely a feasible one, so the impact of such subjective factors will not be severe if such factors are controlled properly. In fact it may be desirable to have such subjective factors if they do not compromise the output quality seriously, since these factors can enhance user confidence in the DSS output.

The above framework provides a degree of flexibility to the model type selection process. The degree of flexibility (i.e., the set of alternative models for a problem) increases as we move down the abstraction hierarchy. This demonstrates how the classification structure facilitates the determination of model substitutability; that is, why some models are not interchangeable, some are interchangeable with some compromises on problem description or accuracy of the output, while others are interchangeable with minor or no changes at all. For example, Queuing and Forecasting models (environment level) are not interchangeable at all, Linear Programming and Non-Linear Programming (structure level) are interchangeable only after imposing major assumptions on the problem description whereas the Simplex algorithm and Karmarkar's algorithm (solver level) can be interchanged without any changes in the problem description. Organizing the knowledge required to identify model types will help in establishing an efficient search procedure.

## 5. Formal representation of the model type hierarchy

In Section 3, we have argued that the selection of a specific model type for a given problem instance is a difficult, iterative process. The model type hierarchy described in Section 4 plays a central role in this process, by providing a framework within which both problem structuring and model selection can proceed. Interestingly, while the knowledge of the problem instance is evolving and unpredictable, and while the decision making environment is highly instance specific, the model taxonomy itself is relatively stable and well-defined. This suggests that the taxonomical knowledge is perhaps the most amenable to formal representation and manipulation via automated reasoning mechanisms.

A central issue in the formal representation of any non-procedural domain knowledge in a knowledge based system is the choice of knowledge representation formalism $[49]$ . While a variety of such formalisms are available, the rich structure of the model taxonomy, combined with its inherently hierarchical basis, suggests the use of a complex-object oriented framework such as frames $[38]$ . As shown in $[14]$ , this has a number of advantages, some of which we discuss in this section.

To start with, frames are well-suited for representing hierarchical relationships. They support distinctions between classes and instances of classes, through the use of class frames and instance (or member) frames. Furthermore, they facilitate inheritance of properties, both (a) by classes inheriting properties specified for their superclasses; and (b) instances inheriting properties specified for (or inherited by) their classes. This in turn provides a basis for establishing default values for properties, so that frame knowledge bases can be used to support mechanical reasoning with incomplete information about problem instances. Given that during much of the model type selection process, the available information about the problem instance is usually incomplete, default reasoning serves as a valuable aid in this task.

Another strength of frames is that they facilitate expectation-driven reasoning. In the model selection task, the model type currently under consideration at any point, provides a frame of reference. For instance, it determines what information about the problem instance is needed to ascertain whether the model type is viable for the problem. This can then serve to focus the problem structuring process towards that specific model type. In Section 1, we had argued that a weakness of manual model selection is the inherent bias of a modeler towards certain model types. The difference between this bias and the focus provided by frames is that in the latter case, the determination of the specific model type can be made objectively, and perhaps more comprehensively.

Yet another useful feature of frames is that computational procedures can be easily attached to frames to supplement the declarative structural knowledge. This is especially valuable when reasoning about aspects of the model selection process that involve evaluation of quantitative relationships between problem parameters, or verification of algebraic properties. Procedural attachments can also be used to incorporate other formalisms, such as production rule modules, into the model taxonomy knowledge base.

The frame representation of management science models is described in $[3]$ . We will briefly describe the method here, and show how it is used through an example. To start with, the model taxonomy knowledge base is primarily a class hierarchy, and thus most of the frames are class frames. Each model type is represented as a class frame, and there are frames corresponding to model types at each level of abstraction in the taxonomy (i.e., environment, structure, parameter, solver). Thus the minimal knowledge base is a network of class frames, and the only instance frame is the current problem instance. In fact, the model type selection process can be viewed as a process of generating the instance frame and identifying it as a member of a suitable model class. A major benefit of the inheritance functionality of frames is that it enables a more compact representation of model knowledge. For instance, the frames corresponding to a model class at the environment level need only capture features relevant to that level of model distinction (that is, inputs, outputs and goals). Similarly, the frames for a parameter level model class can focus on domain characteristics, since other characteristics can be inferred by inheritance from its ancestor classes at higher levels.

A valuable side benefit of the use of frames is that although a top-down, gradual refinement procedure for model selection is certainly possible, the frame representation supports alternative control mechanisms, since a problem could be matched directly with a model frame at any level, such that all the features of the model are considered, even though the specific frame may have only a few slots. The class hierarchy of frames can also be augmented with additional instance frames, corresponding to specific problem instances. Such instance frames may not directly benefit a top-down model selection procedure, but may still be useful (for instance, as a basis for case based model selection). This ability to add instance information represents yet another advantage of the frame approach.

While the model knowledge base can be constructed to a large extent using traditional features of frame systems, several additional features are found to be useful. These are as follows:

(a) Slots may have two types of values, a preferred value and an acceptable value. This two level approach provides a qualitative basis for model comparison, i.e., that a model that matches a problem based on the preferred value of a parameter is likely to be better than one which only matches with an acceptable value. For instance, judgmental forecasting methods are most suitable for short-term forecasts, but may also be used for medium term forecasts (although with less effectiveness) [21]. Similarly, linear programming models can solve an integer programming problem but the answer may not be optimal and feasible for the problem (it is expected that the answer may be near optimal). The acceptable value facet contains values for a slot that can make a problem compatible with a model type with some compromises on the quality of the results.

(b) Search through the model taxonomy can be redirected through the use of a “link” slot containing conditions specified by a suitable predicate. For example, in the time series class of forecasting we can have a link slot to the Delphi method indicating that if the users are looking for a second opinion then they can try the Delphi method of forecasting even though this method does not belong to the same class of techniques.

(c) Exclusionary conditions can be specified using the value class facet in slots. These can be checked first to determine the membership of a given problem. For example, a slot for the optimization class may check for the functional continuity of the function over the given range. The exclusionary condition may specify that if there is a discontinuity in the function then the problem can not belong to this class. Although this imposes some procedurality on the system, it represents a useful way to avoid wasteful search.

The top-down model type selection process starts with the initial problem description, and attempts to find the most specific model type for which the problem can represent a valid instance. At any point where the downward traversal of the model taxonomy is interrupted by lack of information, the PAS is accessed with a request for the necessary information. The search backtracks when either the problem is disqualified from a

![](/api/attachments/P4GGEU7G/fulltext/images/e9f1274240268aaaedcfa167173ed74ded5a6591405e26cea2609cac4360be13.jpg)  
Fig. 4. Schematic representation of the iterative search procedure.

<table><tr><td>frame: Math. Programming (MP)type: classsuperclass: class</td><td>frame: Constrained Math. Programming (CMP)type: classsuperclass: MP</td></tr><tr><td>member slot: coefficient vector (C)type: inputcardinality: ndomain: numericvalueclass: required</td><td>member slot: decision var. vector(X) from MPcardinality: ndomain: numeric</td></tr><tr><td>member slot: decision variable vector (X)type: outputcardinality: n1domain: numericvalueclass: requiredpredicate: n1 = n</td><td>member slot: resource vector (b)type: inputvalueclass: requiredcardinality: mdomain: numeric</td></tr><tr><td>member slot: objective function (F)type: function, inputftype: generalfparameters: C,Xvalueclass: required</td><td>member slot: constraint matrix (A)type: inputvalueclass: requiredcardinality: n X mdomain: numeric</td></tr><tr><td>member slot: goaltype: goal assertionparameter: Fcondition: minimumvalueclass: required</td><td>member slot: constraints (con)type: property assertionvalueclass: requiredcardinality: mdomain: numericftype: generalfparameters: A,B,X</td></tr></table>

model type, or the necessary information cannot be obtained from the PAS. Figure 4 illustrates the iterative nature of the search process through the four level taxonomy using the features described here.

The procedural aspects of the interactions in fig. 2 have been described in Section 3. It is worth noting here, that while the general flow of control is from left to right in fig. 2 (i.e., starting with problem analysis, then model type selection, and then model formulation), in practice the process is far more iterative. For instance, once the model selection process is initiated, the PAS may need to be activated to refine the structure of the problem so that information, necessary for selection of a specific model type, is obtained. Similarly, the availability of a limited number of solvers in the DSS (and thus model formulation modules for only those solvers) can be used to limit the search process during model selection. Put another way, it may be advisable to avoid selecting a

Fig. 5(c). Another structure level frame.

frame: Integer LP (ILP)
type: class
superclass: LP

member slot: decision var. vector (X1)
type: output
valueclass: required
cardinality: n1
domain: numeric

member slot: integer dec. var. vector (X2)
type: output
valueclass: required
cardinality: n2
domain: integer

member slot: decision var. vector (X) from MP
cardinality: n1 + n2
predicate: X = X1 union X2

member slot: constraints (con) from CMP
member slot: size-bound
type: property assertion
parameter: X2
predicate: n2 <= 20 (preferred)
predicate: n2 <= 50 (acceptable)

own slot: GLP
type: link
condition: infeasible X2 acceptable

Fig. 5(d). A parameter level frame.

queuing model type for a problem if no relevant software is available to perform the queuing analysis (note that this is not strictly true, since in principle it may be worthwhile learning that a queuing model is the best choice, even if that means that the decision maker has to access resources external to the DSS to solve his/her problem).

The frame representation method for the model taxonomy is illustrated by example frames for a subset of the mathematical programming model class, in fig. 5. The four frames shown in parts (a)–(d) of this figure show frames for increasingly specific model types; furthermore, the mathematical programming model type in fig. 5(a) represents the objective level of the taxonomy, figs. 5(b) and 5(c) show structure level model types, while fig. 5(d) shows a parameter level model type. The model types at the lowest level, the implementation level are determined by the available solvers in the DSS. Note that although the taxonomy has four levels of abstraction, the knowledge base may have more (or less) levels of classification.

## 6. Conclusion

The goal of this paper is to present a framework to support the model selection process based on a broad set of criteria. We recognize that this is a difficult and complex task and one that is difficult to automate. The selection process is based on matching problem parameters (including the effect of the environment in which the problem is being solved) with model parameters. However, much more research is needed for a practical machine implementation of such a matching process.

Additional research is needed to address the two potential types of errors found in matching: (a) indicating the non existence of a model type when there exists a potential one; and (b) indicating the existence of a model type when there does not exist any. In the second case we essentially identify an inappropriate model for the problem. Given the impact of these two types of errors we need to control and reduce the former one. Other potential research areas include: (i) development of more exhaustive model knowledge bases to differentiate between the large and growing number of models in an effective and efficient way; (ii) development of procedures to redirect the search process when model selection fails; (iii) development of efficient search algorithms to navigate through the knowledge base in an efficient manner; and (iv) investigation of alternative paradigms for reasoning in the model selection context, such as case-based reasoning and pattern directed reasoning.

## References

[1] S. Alter, Why is Man-Computer Interaction Important for Decision Support Systems, Interfaces 7, No. 2 (1977) pp 109–115.

[2] S. Andriole, The Design of Microcomputer Based Personal Decision Aiding Systems, IEEE Transactions on Systems, Man, and Cybernetics, 12 (1982) pp 463–469.

[3] S. Banerjee and A. Basu, A Knowledge Based Framework for Selecting Management Science Models, Proceedings of the Twenty Third Hawaii International Conference on Systems Sciences (1990) pp 484–493.

[4] L.J. Bass, A Generalized User Interface for Applications Programs (II), Communications of the ACM 28, No. 6 (1985) pp 617–627.

[5] I. Benbasat, Cognitive Style Considerations in DSS Design, DataBase 8, No. 3 (1977).

[6] J.L. Bennett, Building Decision Support Systems (Addison Wesley, 1983).

[7] H. Bhargava and S. Kimbrough, On Embedded Language for Model Management, Proceedings of the Twenty Third Hawaii International Conference on System Sciences (1990).

[8] H.K. Bhargava and R. Krishnan, A Formal Approach for Model Formulation in a Model Management System, Proceedings of the Twenty Third Hawaii International Conference on System Sciences (1990).

[9] R.W. Blanning, Conversing with Management Information Systems in Natural Language, Communications of the ACM, 27, No. 3 (1984a) pp 201–207.

[10] R.W. Blanning, Language Design for Relational Model Management, Management and Office Information Systems (1984b) pp 217–235.

[11] R.W. Blanning, A Relational Framework for Join Implementation in Model Management System, Decision Support System 1, No. 1 (1985) pp 69–81.

[12] R.W. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems 2 (1986) pp 65–72.

[13] T. Carey, User Differences in Interface Design, Computer 11 (1982) pp 14–20.

[14] D.R. Dolk and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering 10, No. 6 (1984) pp 619–628.

[15] D.R. Dolk, A Generalized Model Management System for Mathematical Programming, ACM Transactions on Mathematical Software 12 (1986) pp 92–125.

[16] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984) pp 89–97.

[17] J.J. Elam and B.R. Konsynski, Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences 18 No. 3 (1987) pp 487–502.

[18] S.I. Gass, Managing the Modeling Process: A Personal Reflection, European Journal of Operations Research 31 (1987).

[19] A. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) pp 547–588.

[20] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989) pp 30–51.

[21] D.M. Georgoff and R.G. Murdick, Manager's Guide to Forecasting, Harvard Business Review 1 (1986) pp 110–120.

[22] M.D. Good, J.A. Whiteside, D.R. Wixon and S.J. Jones, Building a User-Derived Interface, Communications of the ACM 27, No. 10 (1984) pp 1032–1043.

[23] A. Hevner and H. Mills, Object Oriented Design with Box Structures, Proceedings of the SERC Symposium on Software Engineering (1989).

[24] A.R. Hevner and S. Banerjee, A Systemic Approach for Structuring Business Problems, University of Maryland—College Park, Working Paper, College of Business (1990).

[25] S.N. Hong, M.V. Mannino and B.S. Greenberg, Inheritance and Instantiation in Model Management, Proceedings of the Twenty Third Hawaii International Conference on Systems Sciences (1990) pp 424–432.

[26] P. Keen, Interactive Computer Systems for Managers: A Modest Proposal. Sloan Management Review 18, No. 1 (1976) pp 1–17.

[27] D. Kendrik and A. Meeraus, GAMS: An Introduction (The Scientific Press, 1987).

[28] R. Krishnan, A Logic Modeling Language for Model Construction, Decision Support Systems 6, No. 2 (1990) pp 123–152.

[29] S. Kumar and C. Hsu, An Expert System Framework for Forecasting Method Selection, Proceedings of the Twenty-First Hawaii International Conference on System Sciences (1988) pp 86–95.

[30] T.P. Liang, Toward the Development of a Knowledge Based Model Management System, Unpublished Ph.D. Dissertation, Decision Sciences, University of Pennsylvania—The Wharton School (1986).

[31] T.P. Liang, Development of a Knowledge Based Model Management System, Operations Research 36, No. 6 (1988) pp 849–863.

[32] T.P. Liang and C.V. Jones Design of a Self Evolving Decision Support System. Journal of MIS 4, No. 1 (1987) pp 59–82.

[33] T.P. Liang and C.V. Jones, Meta-design Considerations in Developing Model Management Systems, Decision Sciences 19 (1988) pp 72–92.

[34] E.R. McLean and T.F. Riesing, MAPP: A DSS for Financial Planning, DataBase 8, No. 3 (1977).

[35] H. Mills, Stepwise Refinement and Verification in Box Structured Systems, IEEE Computer, 1, No. 6 (1988) pp 23–36.

[36] H. Mills, R. Linger and A. Hevner, Principles of Information Systems Analysis and Design (Academic Press, Orlando, Florida, 1986).

[37] H. Mills, R. Linger and A.R. Hevner. Mathematical Aspects of Box Structures, Proceedings of the Twenty First Hawaii International Conference on System Sciences (1988) pp 745–753.

[38] M. Minsky, A Framework for Representing Knowledge. The Psychology of Computer Vision (1975).

[39] D.V. Morland, Human Factors guidelines for Terminal Interface Design, Communications of the ACM 26, No. 7 (1983) pp 484–494.

[40] H. Mozeico, A Human/Computer Interface to Accommodate User Learning Stages, Communications of the ACM 25, No. 2 (1982) pp 100–104.

[41] F. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1 (1986) pp 39–47.

[42] B.L.D. Santos and M.L. Bariff, A Study of User Interface Aids for Model Oriented Decision Support Systems, Management Science 34, No. 4 (1988) pp 461–468.

[43] H.A. Simon, The Structure of Ill Structured Problems, Artificial Intelligence 4 (1973) pp 181–201.

[44] G.F. Smith, Towards a Heuristic Theory of Problem Structuring, Management Science 34, No. 12 (1988) pp 1489–1506.

[45] G.F. Smith, Defining Managerial Problems: A Framework for Perspective Theorizing. Management Science 35, No. 8 (1989) pp 963–981.

[46] R.N. Taylor, Nature of Problem Ill-structuredness: Implication for Problem Formulation and Solution, Decision Sciences 5 (1974) pp 632–643.

[47] G.W. Watson, Knowledge Base Management for Model Management System, Unpublished Masters Dissertation, Decision Sciences, Naval Postgraduate School, Monterey, CA (1983).

[48] S.C. Wheelright and S. Makridakis. Forecasting Methods for Management (John Wiley, 1980).

[49] P.H. Winston, Artificial Intelligence (Addison–Wesley, 1977).

[50] R.N. Woolley and M. Pidd, Problem Structuring: A Literature Review, J. Oper. Res. Soc. 32 (1981) pp 197–206.
