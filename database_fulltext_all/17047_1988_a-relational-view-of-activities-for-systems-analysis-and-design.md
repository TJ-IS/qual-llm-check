---
otero_id: 17047
otero_key: "Q8X9NFKH"
title: "A relational view of activities for systems analysis and design"
authors: "Ari P.J. Vepsalainen"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90130-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Relational View of Activities for Systems Analysis and Design \*

Ari P.J. VEPSALAINEN

Department of Decision Sciences, University of Pennsylvania, Philadelphia, PA 19104-6366, USA

Decision support research has emphasized, traditionally, problem analysis and the use of models in problem solving tasks. Only few models have been promoted for the problem finding and early intelligence stage. A suitable modeling method, we argue, should describe activities in abstract concepts as well as in concrete detail, and should relate interesting activities to organizational goals and constraints. The models would be flexible and expandable enough to be reused in many managerial situations. A case in point is information requirements analysis.

We propose a specific relational approach for modeling organizations, in general. Activities and their interactions are represented, at an appropriate level of detail, as diagonal activity matrices. The visual modeling and data collection for further analysis can be started before actual problems have been identified and without preconceived ideas of the eventual activity citing. With the relational activity models, the analysis can focus on problem structuring and information requirements analysis for applications ranging from business planning to transactions processing and operations scheduling. Besides supporting the analysis of organizational problems the relational activity view is also downward-compatible with software design, model management, and prototyping.

Keywords: Activity Modeling, Systems Design, Documentation Methods, Information Requirements Analysis, Relational Systems Analysis.

## 1. Introduction

In traditional decision support systems, the use of models has been motivated primarily by efficient problem solving. There are customized linear programs for large resource allocation problems, application packages for inventory problems, and spreadsheets for business planning problems. Much less emphasis has been given to models as a perceptual tool for understanding of managerial situations before a specific problem (or a method of solution) has been identified. This is the modeling dilemma of decision support [31]: Should a decision maker use, during the problem finding and intelligence phase, a modeling method that might lead to the solution of wrong problems, or should he trust intuition and perhaps fail to identify, in time, any relevant problems at all? The recent interest in model management has barely addressed this issue.

Information requirements analysis is a case in point. Not only are there current problems to be solved but, more importantly, future decision situations and potential information systems to be defined. Furthermore, major constraints derive from organization and business strategies, but existing modeling methods address only technical specifications [8,25]. The inability to relate the problems of the organization to information requirements and systems design has led to errors which are expensive to correct in later implementation stages [14]. As a remedy, a ‘contingency theory' is suggested for the selection of methods on the basis of anticipated uncertainty and risks [11,28]. But the proposed methods of structured analysis, geared toward system specification, will instill the design with preconceived ideas of critical activities and interactions. Similarly, the use of prototyping and knowledge engineering [13] may further shortcircuit the requirements identification process unless directed by an appropriate organization model.

![](/api/attachments/Q8X9NFKH/fulltext/images/6fd5af696da1a86d166f664d4efc8b049c30322971071b359cf5def02a2839eb.jpg)

A solution is a modeling method flexible (and perceptual) enough to describe interesting activities in abstract concepts as well as in concrete detail and to relate them to organizational goals and constraints. Such as general method, the Relational Activity View Environment (RAVE), is proposed here. RAVE helps identifying problems and opportunities early in the decision making cycle. RAVE's output is a conceptual model of activities and organizational relationships that is visualized as a diagonal matrix. This representation is easy to use and expandable, making it preferable over its more structured graph-based counterparts in model management (as the relational model is preferable over network models in data management). A similar matrix model of activities has been applied previously in corporate planning [19,20,40] and in interface design [24].

In addition to supporting data collection and activity structuring, RAVE models are reusable in design and performance evaluation. Organizational structure can be related to dynamic behavior, for example, in comparing resource-based and process-based alternatives. The relational view is easy to translate into other models and software design methods, thereby avoiding redundant specifications and premature freezing of partial designs.

In the following, the need for a problem modeling method is first articulated in terms of the domain of representation and the level of abstraction not addressed by existing methods (section 2). A formal relational activity view environment, or RAVE, is outlined in section 3, with an illustration, definition of semantics and principles of activity structuring. Examples in section 4, taken from operations management, emphasize the interplay between activity scheduling and information systems. Extensions to performance evaluation and other applications are suggested, followed by conclusions.

## 2. System Specification and Activity Analysis

## 2.1. Elements of Systems Specification Methods

Analysis of information requirements is based on some specification by the organization of its purpose, activities, and systems. A modeling method is the formal part of the specification which determines the domain of requirements and problems that can represented. Examples of different modeling methods are data flow diagramming and linear programming, both having typical representations and underlying theories. The work with models is made easier with mnemonic symbols and graphic conventions and model manipulation can be enhanced, even automated, through rules for aggregating, focusing and reconfiguring the models. The variety of modeling methods and manipulation features now available has resulted from thirty-plus years of experimentation and development. To facilitate a concise review, we establish a three-by-three classification of methods that also summarizes the main findings.

A modeling method is characterized by two factors, domain of description and level of abstraction. First, domain of description defines a point of view for modeling the system and its environment. Three domains can be distinguished (adapted from [45]):

(1) The subject domain - Any system is part of a host organization that can be described in terms of activities, resources, decision making and information processing.

(2) The interaction domain - The system is described from the user's viewpoint, as a collection of parts interacting with one another and with the environment. Major views are expressed in terms of architectures of applications, communications, data and technology.

(3) The implementation domain - The configuration, data and programs constituting the system are described in detail sufficient for determining its behavior.

Second, the entities of these domains may be represented by abstract concepts and by graphic or symbolic models. Usually, several levels of abstraction must be supported to provide sufficient power and flexibility for analysis and problem solving. Three levels of abstraction are conventional:

(1) The level of semantics - Generic concepts (entities and attributes) are defined, and rules for identifying relationships between concepts and observations are given.

(2) The level of reference models - Guidelines for structuring the relationships and for fitting the structures to specific problems are defined. Possible solutions to the problems are specified explicitly or implicitly.

(3) The level of model instantiations - The method allows collection of data to generate an instance of the model and to solve it, or the model can be implemented so as to simulate or prototype the referent system.

These levels are similar to the axiomatic, axiomatamedia, and instantial levels ([23]; see also [25]). Modeling methods can be classified according to their emphasis and efficiency in the different domains and levels of abstraction. In systems engineering, for instance, some systems, such as PLEXSYS [22], have general concepts and allow flexible modeling, whereas others, namely application packages, allow only pre-specified concepts and few alternative solutions. On the other hand, a package may provide more efficient instantiation. Similar tradeoffs are common in operations research: a general LP package can be applied in most problems, but special codes are more efficient for network modeling.

Even if two modeling methods would seem equivalent in the above framework, they may differ in terms of notational and graphical conventions provided and in terms of computational power. These model manipulation facilities are often critical to users in supporting the cognitive aspects of modeling and model management. Sprague and Carlson [38] distinguish four types of manipulations: representations, operations, memory aids, and control. Despite the development of flexible graphics interfaces and general-purpose model management principles (see [3]), some modeling methods are still superior for their power of manipulations. The following facilities are often critical:

\- Representing entities in different granularity and moving 'up' and 'down' the aggregation or refinement hierarchies. For example, all customers may be aggregated as a composite customer, or an activity may be refined in terms of functions or resources. Here disaggregation refers to the specification of attribute values of similar entities, whereas refinement means the specification of an inner structure. Both are hierarchical operations with typical cognitive and computational benefits [37].

\- Extending or focusing the current model with respect to the scope, aspect, or time horizon is often needed for different concerns. For example, an organization may be inspected including only the plant or by extending the scope to the distribution channels as well, or the analysis may focus on transactions dealing with a given resource.

\- Quantification of model attributes at different levels of abstraction or aggregation can be done through estimates functions, or discrete attribute values may be stored at each level.

An ideal method, then, would support efficient manipulations and representations of all domains and on all levels of abstraction.

## 2.2. Review of Systems Modeling Methods

Despite the attempts to create such a general method, the existing models have been confined to limited types of problems (resource allocation, policy analysis, or systems design), to one of the stages of problem solving process (requirements analysis, systems design, or implementation), and to few primary user groups. Users in large organizations obviously have preferred methods that fit their specialty and responsibility, causing further separation. It is well known that formal documentation tends to gravitate towards the design and implementation stages whereas requirements analysis is less model-oriented [8,25]. In terms of the above framework, the primary domain of modeling depends on the stage: requirements analysis is based on models of subject domain, design refers mainly to interaction domain, and data and programs are specified in implementation domain. Furthermore, the sharing of actual models is inhibited by their different levels of abstraction: requirements analysis deals with general concepts, design defines reference models, and instances of the models are implemented.

The following review traces this separation of modeling methods in more depth.

The methods of implementation domain have advanced from programming languages to integrated application generators [7]. The ISDOS project has created the Problem Statement Language (PSL [39]) for general modeling of the interactions and implementation. Complete information system development environments include PSL/PSA, SREM [2], PLEXSYS [22], and IDA [5]. Mathematical programming and simulation packages have been used only in special applications. Context-free representations, originally flow charts and module charts, have improved with non-procedural and declarative languages and now include semantic nets, frames, rule-based languages and logic programming [13,32]. Knowledge engineering allows new customized expert systems to be built which use design heuristics. Without powerful domain specific (or, as defined above, subject-specific) modeling theory, however, problem representation may become complex, inconsistent, and confusing to users [35]. This limits the use of knowledge engineering in implementation as well as requirements analysis.

The interaction domain deals with the structuring of systems and organizations. This general aspect of design has been incorporated usually into the models of implementation or subject domains, as in logistics, communications, and systems theory. The interaction domain is degenerate especially in many traditional fields of design because of their concrete objects such as a product or a building. On the contrary, information systems are built to generate complex, less tangible multi-media interactions and social relations which defy those ‘natural’ representations and ‘scale’ models. Hence domain-independent structural analyses could be built into a modeling system. Hierarchical structures, for example, are fundamental for the evolution, efficiency, and stability of organizations and can be applied in designing systems [37]. Even though hierarchical coding and visualizations have cognitive economy across different domains, information algebra or other formal theories are yet to be incorporated in practical approaches. Mathematical models of hierarchical systems are used in control theory and economics but applications to information systems are scarce. The study of decomposability is also important for the domain of interactions [9].

The early models of subject domain specified requirements for accounting, order entry and inventory systems (see, e.g., SOP and BISAD [8]). More integrated models were built into a parameterized template of the business operations (BI-AIT [21]), or in a systematic framework of business processes and data flow with checklists and cross-tabulation of files, systems and user departments (BSP [17]). To certain extent, however, these models emphasize the interaction domain along with the organizational activities.

General information analysis starts from the objectives of the organization to derive a graphic specification of the information processes (ISAC [26]). Many other methods are closer to actual input-process-output system structuring, such as ADS and HIPO [8] and structured systems analysis [14,34]. Decision analysis is another natural starting point for requirements analysis [1]. Quantitative methods have not been used except for decision support systems. The attention to decision support has further emphasized managers' situational information needs [38] and the critical success factors [33]. Recently, the value chain [30] has become a popular model of organization among systems professionals. The analysis based on value chain concepts is descriptive, however, and business strategies and technical solutions are not represented in a formal model.

The separate levels of abstraction lead to inflexible modeling and to design by brute force. Instead of studying requirements and constraints an analyst may specify a generic design by fixing the solutions all three domains (i.e., managerial principles, control structure, and software). However, such a ‘packaged solution’ is feasible only under specific circumstances. In operations scheduling and inventory management, for instance, there are three such packaged solutions (see [36]): one is computationally intensive (planning based on standards: MRP); second is informationally reduced (planning avoided by stable production and fast reaction: Kanban); and third that could be called information-rich (focus on critical orders and facilities: OPT). These solutions have very different demands for the manufacturing organization in terms of machine capacities, worker compensation, target quality, and so on. When a firm adopts one of these packages, it also has to adhere to the underlying management principles to get the benefits – otherwise, organization, production process, and/or products have to be redesigned at extra cost. The question addressed in this paper is, then, how to model the organization in the first place so as to determine the trade-offs among the different packages and organizational options.

To reiterate, we have found a methodological gap between the concepts and descriptive models of the subject domain used in information requirements analysis, and the methods of specifying computer-based systems in the implementation domain. Because of this gap, an attempt to relate organizational requirements to system designs leads to complex and redundant documentation and to communication problems. A solution suggested here is to formulate a general model of activities that represents relevant interactions and structures of organizations and systems (both in subject domain and in interaction domain). Hence it can integrate the broad spectrum of managerial concerns involved in requirements analysis.

## 2.3. Precedents of Activity Analysis

Lano [24] has introduced a ‘ $N^{2}$ Chart’ as a method to define functional interactions and interfaces in large software systems. The $N^{2}$ Chart is a visual aid for relational analysis of any functions or activities and their (often dynamic or implicit) structures. The basic concepts are illustrated in fig. 1. The N activities form the main diagonal of a $N \times N$ matrix as shown for system S of four activities (N = 4). The activities 1 to 4 are described in the main diagonal cells and their interactions in the off-diagonal cells (reading clockwise): a command from activity 1 to activity 2, for instance, is marked on row 1, column 2. Basic units are the binary interactions (individual cells), composite inputs and outputs can be read on activity's column and row, respectively, and more complex multilateral interactions are coded into clusters of cells.

Besides individual activities and their interactions, more complex relationships can be depicted. System S in fig. 1 is a hierarchy consisting of subsystems $S_{1}$ (activities 1 and 2) and $S_{2}$ (activities 3 and 4). The $N^{2}$ Chart representation has been used at TRW for defining interaction patterns, including secondary flows and dependencies (control, monitoring, support, etc.), along with structured programming and modular top-down design.

Similar visualization is used in the Activity Matrix [19], also called the DAJE system [20]. An activity refers to a part of an organization, with resources and agents, capable of performing certain tasks. Etymologically, the activity view draws from the systems approach [6] and from ‘socio-cybernetics’ [15]. Activities capture the essential structure of the organization – permanent resource allocation, authority relationships, and temporary task assignments. Activity matrices have been applied in corporate planning [40], analysis of mergers, and in reorganization of marketing and R&D functions [20]. An activity map depicts the material and information flows and potential problems are perceived as inappropriate patterns of interactions or as other constraints among the activities. Many powerful concepts, such as the stage theory [29] and the value chain analysis [30], are readily visualized in activity matrix.

![](/api/attachments/Q8X9NFKH/fulltext/images/763d1bbc6149d1437fd5380deff4f74d4354c7e9f2a949a3b897327ba5c21d97.jpg)  
Fig. 1. $N^{2}$ Chart: An Illustration of an Activity Matrix.

Both the $N^{2}$ Chart and the Activity Matrix have been used predominantly as documentation tools, often in the form of wall-charts and workbooks. In the following, a conceptual view of activities is defined that complements the matrix visualization for a formal analysis of organizations and information requirements.

## 3. The Relational View of Activities

## 3.1. An Illustrative Example

The new matrix method can be illustrated by converting a familiar structural representation, such as a data flow diagram, into a relational activity form. Data flow diagrams (DFDs) are used in the logical analysis and design of structured information systems. Consider an order processing example adapted from a textbook $[14]$ (fig. 2). The entities in a DFD can be customers, data flows, data processing tasks, or data stores (a file).

The same order processing example is represented as an activity matrix in fig. 3. Data flows are shown as interactions between the other entities, processes and files. Alternative designs of the information systems can be tested visually by rearranging the activities on the diagonal (i.e., adjac-

![](/api/attachments/Q8X9NFKH/fulltext/images/8fd732e846b77df77aad926d829a985263ba0a74b04048013fc05a6258cf416d.jpg)  
Fig. 2. Data Flow Diagram of an Order Processing System.

![](/api/attachments/Q8X9NFKH/fulltext/images/63840e455f634686d6f4d05f7b8ed39ba3006bc2aa7157cc361a3273e5716957.jpg)  
Fig. 3. Activity Matrix of the Order Processing System.

ent activities and clusters of interaction cells suggest a joint system context). This kind of structuring is typical in the BSP system [17], except that in BSP the matrices relate activities to data classes, data classes to systems, and systems to activities. Here we relate activities to other activities through data and other interactions. Hierarchical structures are indicated by clusters of intensive (or missing) interactions and can be emphasized by joint boundaries. Systematic codes are used for activities and interactions, including tentative and residual activities that help in data collection. Tentative activity structures are easy to display without committing to a specific decomposition.

With network graphics systems, more detailed definitions are needed early on that make the graphs harder to change later.

Narratives can be displayed next to the activity matrix. Resources can be declared on activity rows in right margin, and tasks (including inputs and outputs) below in the columns. With the activity matrix it is easy to relate information processing to other interactions, such as payment flows, materials handling, and authority relationships. These can be included without obscuring the view of the data flows. Since the interactions are easy to read from the off-diagonal cells, it is possible to get an idea of the dynamics of individual transactions. For more detailed study, however, the activities can be ‘stretched’ into a dynamic structure which associates the appropriate precedence relations with the interactions and activities. This is illustrated with a process of handling an order (below the activity matrix in fig. 3). The dynamic aspect is a logical extension of activity structure, and only the factors most relevant for understanding the dynamics need to be represented here.

## 3.2. The Relational Activity View Environment

In order to automate the relational representation of activities, appropriate concepts and model manipulations have to be specified formally. This is achieved with the Relational Activity View Environment (RAVE). RAVE is meant for the unstructured stages of requirements analysis, data collection and activity modeling which are not adequately supported by the established methods. RAVE relates the information requirements and alternative system designs to the goals and strategies of the organization, maintaining relevant details of the technical, economic and behavioral constraints. The RAVE concept provides for data and model sharing across systems development and business planning projects. Further, it facilitates knowledge engineering among managers and systems experts.

To accomplish this, RAVE uses concise semantics and incorporates several activity structuring principles. For evaluation purposes, it also deals with dynamic models. In the modeling framework established above, RAVE supports the following domains and levels of abstraction:

(1) Subject domain - the activity models are provided for the documentation, retrieval and analysis of data and ideas. Abstract concepts and instances of detailed models are easy to relate to each other, with appropriate testing of conceptual consistency and completeness of models.

(2) Interaction domain - structural design and evaluation is facilitated by generic activity models and systems architectures. Theoretical concepts are translated into activity structures and systems, pointing out the roles of the agents, interactions, systems, resource allocations and task assignments.

(3) Implementation domain - simulations or actual prototypes are generated for functional and dynamic evaluation. Different transactions and resources are instantiated to test the performance level achieved through given activity structure, systems design, and priority assignments. General results can be derived from experimentation.

Flexible relational representation is essential for decomposing and refining the aspects of activities. In fact, the RAVE approach provides most model manipulations needed in data collection and analysis, as discussed above.

## 3.3. The Semantics of Activity Models

The RAVE concept integrates business planning and information systems development through a conceptual framework including semantics of activities and reference models for structuring organizations and information systems. The main concepts and their relationships are shown in the ‘semantic matrix’ in fig. 4.

An activity is a collection of agents and resources that can perform tasks and participate in the exchange the resources with other activities. An interaction is characterized by quantity (or rate of flow), duration, and conditions on the timing and precedence. 'Order entry' in fig. 3 is an activity, with an interaction 'valid order' to the database activity.

An activity is managed by some responsible agent, or the principal. Hence authority and control of resources may be additional determinants of an activity structure. Moreover, an activity serves some purpose in relation to other activities or agents. It is convenient to express the purpose of activities in terms of accumulation and use of resources through production and exchange. Resources include people, machines, raw materials, data, money, authority, etc. Resources are characterized by quantity (indivisible or continuous), and type (fixed or consumed, exhaustive or replenishable). Resources form hierarchies through aggregation, and different resources may be permanently configured into a 'system' to exploit synergy. Transactions are reciprocal relationships between activities, either exchange of resources or other contracts contingent on the status of resources. This concept traditionally refers to message handling in a transaction processing system, but here it denotes also, and perhaps more importantly, different economic contracts among people and firms [43,44]. A transaction has a goal, or postcondition, expressed as a set of criteria to be satisfied or optimized. Transactions and their goals form a hierarchy in which cumulative conditions of compound transactions usually are goals of higher level activities.

<table><tr><td rowspan="2">Economic aspect</td><td>RESOURCE</td><td>object-of means-of</td><td>belongs-to part-of</td><td>part-of</td><td>input/output</td><td>has-a acquires</td></tr><tr><td>requires</td><td>TRANS-ACTION</td><td>goal-of</td><td>implies</td><td>generates</td><td>refers-to</td></tr><tr><td rowspan="2">Functional aspect</td><td>controls</td><td>part-of controls</td><td>ACTIVITY</td><td>part-of controls</td><td>includes</td><td>monitors</td></tr><tr><td>includes</td><td>part-of</td><td>refers-to includes</td><td>INTER-ACTION</td><td>requires enables</td><td>depends-on</td></tr><tr><td rowspan="2">Process aspect</td><td>transforms</td><td>object-of</td><td>part-of</td><td>enables</td><td>TASK</td><td>changes requires</td></tr><tr><td>refers-to</td><td>pre-/post condition</td><td>defines</td><td>causes</td><td>enables/ends</td><td>STATUS</td></tr></table>

Fig. 4. A Semantic Matrix of the Relational Activity View (Not Complete).

The interactions and transaction flows are dynamic. The timing of these processes is determined by rules describing resource transformations and causality. The corresponding concepts here are task and status (similar concepts used elsewhere are event and state [12], or process and status [5]). A task is a procedure or transformation of resources (input, precondition) to some output (postcondition). Tasks can be enabled within an activity, without other interactions. For example, the task 'validate order' can be included in the order entry activity in fig. 3. Status indicates the state of a resource, event, or other condition on the system. It is a marginal statement regarding the state of the activity system. Examples of order status above are 'valid' and 'canceled'.

These concepts represent different aspects of the activities. The functional aspect, for example, refers to activities and their interactions, whereas the economic aspect deals with transactions and resource allocations. The process aspect refers to tasks and status changes. These aspects are, in principle, mutually complementary representations of organizations. In research, models are built around one of these aspects with less emphasis on the others. Operations management models, for example, specify transactions (jobs) and resources (inventory) as part of the process (operations and status changes of machines), whereas economists consider explicitly resource allocations and transactions among agents. Information systems analysis comprises all three aspects, motivating an explicit representation of each. The complex relationships among the aspects make a semantic matrix often preferable to a semantic net [32]. Semantic matrix is also a useful tool in building new activity models, as will be demonstrated below.

## 3.4. System Identification and Semantic Consistency

The identification and naming of activities and other entities is the first task of systems specification. It may be confusing (what is an activity? a task? etc.), and it is always difficult because of necessary definitions and abstractions. Any tentative activity model should be normalized to ensure the integrity and to remove unintentional redundancy [10]. However, an activity model consists of the mutually dependent aspects and the complementary can be used to test if a model is consistent and complete. Three ‘consistency views’ have proven useful:

\- Activity view: Activities and their interactions are properly generated by transactions and exchange of resources,

\- Operational view: Transactions are generated by tasks and the process of status changes of resources,

\- Behavioral view: tasks and capabilities are assigned to the activities so as to facilitate compatible interactions.

These views help in the stepwise refinement of activity descriptions by testing consistency between the aspects, and by suggesting missing or confirming facts that guide the questions to be asked from the experts.

## 3.5. Activity Structuring

Activity structuring is a design method for matching organizations and systems. We distinguish two major constraints for activity structuring:

\- inherent structure of an aspect of the activities,
- efficient implementation of transactions.

First, each aspect has a structure which represents substantial properties of the activities. It can be an aggregation hierarchy (a market consists of customers, a computer of several components), a mutual dependency (one transaction may be contingent on another one, one task has to precede some others), or some other pattern (activities can be centralized or decentralized). These structures are usually indicated in the semantic matrix (however, the functional aspect is also shown as a separate activity matrix since the activity structure is of primary concern in systems design). Often the structure depends on some intangible (or indirectly defined) aspects, such as economies of scale, allocation of tasks, or the links of communication and control. In most cases, a hierarchical structure can be found (or evolves over time) that optimizes interactions among the activities while also building on the strengths of the resources available [27,37].

Second, efficient completion of transactions is another requirement for activity structuring. The number of separate steps and crossings of activity boundaries are reasonable measures of the costs incurred. Transaction costs can be reduced by rearranging the tasks among the activities, or by decomposing the transaction into fewer separable steps. The duality of transactions and resource allocation can guide the design – either the volume of transactions is maximized or the cost or resources is minimized. Similar dual relationships can be exploited in design between tasks and timing conditions (scheduling, inventory control), and between activity congestion and interaction costs.

## 4. Applications and extensions

In our experience, the activity matrices help designers to perceive systems problems and opportunities visually. In the following, we discuss how some criteria of systems feasibility, activity structuring, and dynamic analysis are represented in the RAVE diagrams. Examples are taken from manufacturing activities which always require a joint design of operations and information systems.

## 4.1. Feasibility Analysis

The RAVE analysis mandates several measures of activity performance that can be used as feasibility criteria. Transaction volume indicates the capacity of operations, resource usage per transaction measures productivity, and timeliness is related to the quality of service. Since the activity designation can change resource allocation and transaction costs, easy change of activity structures is important in searching for efficient designs. By including external activities, such as customers and suppliers, the activity analysis may suggest critical success factors for the systems [33]. These may be some transactions with volume or quality below expectations or bottlenecks or idle resources. Sometimes the mere complexity of interactions which are not well understood constitutes the maangerial problem.

The strategic feasibility of proposed systems depends on the bargaining position with the suppliers and potential allies, and on the competitive response. A system should also support the competitive strategy pursued by the firm (cost leadership, differentiation, or focus) as discussed by Porter [30]. These external aspects have been easy to integrate into the activity analysis in order to examine new interorganizational systems and strategies [20]. Especially interesting applications have been found by looking into the attributes of the customer contact cycle [18,42].

## 4.2. An Example of Activity Structuring

A challenging application area is the modeling of manufacturing systems. Existing models are meant for specific problem types: shop (or project) scheduling, production planning, process layout design, etc. Organizational aspects and alternative information flows are particularly difficult to add on to these models. As an example of the use of RAVE, consider a job shop which produces multiple products. Conventionally, the type of products (with particular components and volume) has determined the structure of operations and systems, whether a job shop, batch shop, or a flow shop [16]. Flexible manufacturing systems and small batch production have created new economically efficient product line architectures. Now the tradeoffs between many more factors (including product design, flexibility or machines and materials handling, process control, and integration) have to be determined explicitly, taking into account the need for possible reconfiguration later on. The conventional models and methods of documentation (bill of materials, operations charts, animated process simulations) have serious limitations as tools of analysis. For example, a graph-based representation of a production line with shared resources and selective information is hard to follow even with few jobs and machines. Moreover, reconfiguring only one of operations graphs, physical lay-outs, or resource networks obscures many useful visual associations.

Here we demonstrate how a job shop can be compared with a process-oriented design using the RAVE diagrams. In a job shop, machine centers, storage, shipping, scheduling, and sales are the main activities. Interactions consist of material flow (job routings) and scheduling information (fig. 5a). The transactions are products (denoted A, B, C and D) and administrative services, such as scheduling and sales. In this application, the main resources are machines, parts and components (denoted $A_{0}$ , $A_{1}$ , ..., $A_{5}$ for product A, etc.), and information. The activity structure is based on shop lay-out and flow volumes.

A semantic matrix of the job shop model showing some of the main concepts is given in fig. 5b. This semantic matrix is an instance of the generic matrix (fig. 4). The titles at the top of the matrix show the concepts (note that the process aspect is left out). More detailed structures can be shown in pop-up windows as sub-matrices or menus (for example, pointing to resource 'information' would reveal a selection: order; status; schedule; priority etc.). A user can modify the activity matrix and the semantic matrix by adding new entities and relationships on the basis of the default structures inherited from the generic matrix.

Machine centers are the primary activities which can be structured according to part routing, information systems (centralized or decentralized), and scheduling and inventory policies. Here the process flow is jumbled (indicated by the numerous interactions among the machine centers) which is typical in a low-volume operation. If, however, a high-volume product (transaction) with multiple stages and complex precedence relations (assembly, testing) would be added, alternative activity structures should be considered. Either project organization or a separate production line may be appropriate. An example of the activity matrix for a mixed shop, extended from the job shop model with separate production lines for C and D, is shown in fig. 6. Now the activity structure is based on product types as well as machines, and it is further decomposed along information and control systems. Some flexibility is retained by improving materials handling with a ‘traffic’ activity, such as conveyor belt.

The semantic matrix (fig. 5b) requires minor changes to accommodate the new activity model. The dedicated product line can be indicated as a production activity determined by a product, not just by a machine center (or, alternatively, a new transaction-based activity concept could be defined). Hence the limitations of a functional (resource-based) activity structure suggested the addition of new activities which have greatly streamlined the interactions. The new activity structure is closer to a matrix organization than the functional one. Problems of coordination, matching of skills and tasks, complex interactions and fragmented resources can be addressed explicitly in the activity matrix. Resource sharing and assignment can be depicted directly and, for example, the need for flexibility due to product variability is easy to analyze. In some cases, the interactions could be further simplified by decomposing all resources into individual product lines, resulting in product-division activities (matrix not shown). Further ramifications of production planning can be studied on the basis of the hierarchy of products types [16] imposed upon the alternative shop structures.

<table><tr><td>SCHED</td><td>release</td><td>priority</td><td>priority</td><td>priority</td><td></td><td>Master plan</td><td></td></tr><tr><td></td><td>MATERIAL INV.</td><td> $A_0$ ,  $C_0$ </td><td> $B_0$ ,  $D_0$ </td><td></td><td></td><td></td><td></td></tr><tr><td>status</td><td></td><td>M/C 1</td><td> $A_1$ ,  $B_4$ ,  $D_2$  $D_5$ </td><td> $A_4$ ,  $C_1$ ,  $C_4$ </td><td></td><td></td><td></td></tr><tr><td>status</td><td></td><td> $B_3$ ,  $C_3$ ,  $D_1$ </td><td>M/C 2</td><td> $A_2$ ,  $B_4$ ,  $B_5$  $D_3$ </td><td> $D_6$ </td><td></td><td></td></tr><tr><td>status</td><td>scrap</td><td> $A_3$ ,  $D_4$ </td><td> $B_2$ ,  $C_2$ </td><td>M/C 3</td><td> $A_5$ ,  $B_5$ ,  $C_5$ </td><td></td><td></td></tr><tr><td>status</td><td></td><td></td><td></td><td></td><td>FINISHED GOODS INV.</td><td>status</td><td>goods</td></tr><tr><td>forecast query</td><td></td><td></td><td></td><td></td><td>request</td><td>SALES</td><td>inform.</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>orders</td><td>CUSTOMER</td></tr></table>

Fig. 5a. Activity Representation of a Job Shop.

The RAVE models are used in information systems design in several ways. First, different patterns of interactions among activities suggest requirements for information systems. Extremely complex interactions may signal that the proposed activity structure is informationally demanding, and that modifications are needed even before information systems are explicitly considered. Second, information flows can be related to other interactions (such as material or monetary flows). This helps in distributing the decision making authority at appropriate levels of organization.

Third, the design of information systems is explicit in the activity view. The interfaces between users and systems can be designed using the principles suggested by Lano [24]. The main factors are the access to data, availability of feedback, and the complexity of individual tasks. System architecture is determined in terms of processing power, communication capacity, data base design, and applications. Detailed conceptual models for data, programs, computers, and other information resources are needed for the technical design.

Finally, the semantic matrix serves the analyst in many ways. It supports data collection and semantic analysis of the activity models. The structures of the resources and transactions can be analyzed separately from activities and the activity matrix. This leads often to ideas for new activity structures. In data base design and programming, the semantic matrices provide an initial schema for implementation.

## 4.3. Dynamic Analysis of Priorities

In addition to the static view of the activity structure as discussed above, the design of an information system should take into account the dynamic performance of the shop. Unforeseen problems may surface later on (low throughput, or late completion of jobs) if the variations in system load and the ensuing contention over resources have not been tested thoroughly. The true capacity

![](/api/attachments/Q8X9NFKH/fulltext/images/cce562363205dac61a658b97fec53108ecc1de1e48e82c4309fbe62b11e034ac.jpg)  
Fig. 5b. Semantic Matrix for the Job Shop Model (Not Complete).

can be estimated by instantiating a typical stream of transactions and by analyzing the behavior of the system. Unfortunately, scheduling problems are too complex for casual inspection and often exceed the limits of statistical analysis. But using simulation and a priority scheduling rule to resolve the resource allocation problems, a reasonable estimate of performance can be obtained. However, priority rules differ considerably in terms of the information required and the performance for different criteria such as in-process inventories and timeliness [4,41]. In fact, a priority rule may determine the desirable activity structure. Information requirements are affected as well. In RAVE, a desired load can be instantiated and the transactions simulated within the same activity model. The results can be visualized in terms of resource utilization and inventory levels shown in an extended matrix, or a GANTT-chart (fig. 7). Instances of critical resources or jobs can analyze along the time lines, and long-term averages may be shown for comparisons. The dynamic flows of information and logistics can be analyzed similarly to the model discussed above (fig. 3).

## 4.4. Software Support

In the RAVE approach, organizations are specified as relations among the tasks, resources, and transactions (traditional organization charts, network graphs, and flow diagrams are not needed). Specific software (still a prototype) supports the visualization and different manipulations of activity models. A graphics interface has been

<table><tr><td>SCHED</td><td>schedules</td><td></td><td>priorities</td><td></td><td></td><td>release</td><td></td><td></td><td></td><td>release</td><td></td><td>Master Plan</td></tr><tr><td></td><td>WORKER</td><td> $X_{2}$ </td><td> $X_{5}$ </td><td> $X_{1}$  $X_{4}$ </td><td></td><td> $X_{2}$ </td><td> $X_{4}$ </td><td> $X_{5}$ </td><td></td><td> $X_{i}$ </td><td> $X_{3}$ </td><td></td></tr><tr><td></td><td>MAT&#x27;L</td><td> $A_{0}$ </td><td> $B_{0}$ </td><td></td><td> $C_{0},D_{0}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>status</td><td></td><td>M/C1</td><td></td><td></td><td></td><td> $f_{1}$ </td><td> $t_{4}$ </td><td></td><td></td><td> $f_{1}$ </td><td></td><td></td></tr><tr><td>status</td><td></td><td> $B_{3}$ </td><td>M/C2</td><td></td><td></td><td></td><td> $t_{1}$ </td><td> $f_{2}$ </td><td></td><td> $t_{1}$ </td><td></td><td></td></tr><tr><td>status</td><td>scrap</td><td> $A_{3}$ </td><td> $B_{2}$ </td><td>M/C3</td><td> $A_{5},B_{6}$ </td><td></td><td></td><td> $t_{2}$ </td><td> $t_{5}$ </td><td></td><td> $f_{3},t_{2}$ </td><td></td></tr><tr><td>status</td><td></td><td></td><td></td><td></td><td>TRAFFIC BELT</td><td> $C_{0}$ </td><td></td><td> $C_{3}$ </td><td></td><td> $D_{0}$ </td><td></td><td>goods</td></tr><tr><td>status</td><td></td><td></td><td></td><td></td><td> $C_{3}$ </td><td> $OC_{a}$ </td><td> $C_{1}$ </td><td></td><td></td><td></td><td></td><td>status</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td> $C_{2}$ </td><td> $OC_{b}$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>status</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td> $OC_{c}$ </td><td> $C_{4}$ </td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $C_{5}$ </td><td></td><td></td><td></td><td> $OC_{d}$ </td><td></td><td></td><td></td></tr><tr><td>status</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td> $OD_{a}$ </td><td> $D_{1},D_{3}$  $D_{5}$ </td><td>status</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td> $D_{6}$ </td><td></td><td></td><td></td><td></td><td> $D_{2},D_{4}$ </td><td> $OD_{b}$ </td><td></td></tr><tr><td rowspan="2" colspan="2">forecast queries</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td>SALES inform.</td></tr><tr><td>orders CUSTOMERS</td></tr></table>

$$
\mathbf {x} _ {\mathrm{i}}
$$

$$
\mathbf {f} _ {\mathbf {i}}
$$

Fig. 6. Activities of a Flexible Manufacturing Shop.  
![](/api/attachments/Q8X9NFKH/fulltext/images/2b408cc6e25eed1da1aaaeec5eb21f1e751925ba8f9fc3b7fa09d951d66cc06f.jpg)  
Fig. 7. Dynamic Analysis of Job Priorities and Shop Loading.

instrumental in evaluation of alternatives and in generation of new ones [20]. With the help of focusing capability and pop-up windows, the building of the semantic and activity models is possible without programming. The ‘canonical’ matrix can be transformed into a network form (or into any other structured model, as may be needed) as shown in the data flow example above. The matrix is also compatible downward to the implementation level (for example, structured programs have a ‘staircase’ design). The specification of activities as collections of resources, tasks and other entities, lends itself naturally to object-oriented design and easy prototyping.

The RAVE software can be integrated with other packages. An example is the ordinary spreadsheet. The link is two-way: input to the spreadsheet is taken from the RAVE model (interactions, resource allocations, and transaction costs), and changes, cumulative figures and other solutions worked out on the spreadsheet are fed back into the RAVE matrix. Again, the mapping between spreadsheet and RAVE matrix is straight forward, helping the implementation of standard cost/benefit analyses and encouraging incremental evaluation during design. Model manipulations can be enhanced with colors and icons which also allow smaller scale (and wider scope) of matrix to be displayed. The dynamic instantiations can be illustrated with rolling horizon techniques.

## 5. Conclusions

This paper deals with the dilemma of how to use models for identifying problems when traditional methods are geared for specific solutions. The approach proposed here, a Relational Activity View Environment, or RAVE, supports problem diagnosis by representing generic concepts of an organization and by relating activities and transactions to their respective goals and resource requirements. RAVE matrix draws attention to different patterns of interactions, revealing efficient hierarchies and other ‘natural’ structures. Visual tools are streamlined by avoiding fancy graphics and free-form layouts. Within decision support systems, RAVE serves the model management function [3] by offering associations between problems and models. In particular, RAVE can be used in information requirements analysis for linking technical specifications to the concepts of organization structure and strategy.

This paper has presented the basic idea of relational modeling and its visualization as diagonal activity matrices. Some experiences with the activity analysis are discussed and a semantic model is specified. In designing systems which are closely integrated to business strategies managers cannot rely on outside analysts. RAVE has been tested in marketing analysis, organizational design, merger problems, production and R&D planning, and project management, and in all cases managers have found it helpful and easy to use.

Future papers will address other interesting questions concerning the extensions and applications of RAVE. Technically, RAVE provides a canonical form of representation of organizations for knowledge engineering which can be further capitalized by enhanced interface and object-oriented implementation. In systems development, the applications extend from requirements analysis to the planning of the development project. The next step is the specification of software and integration of the day-to-day monitoring of the implementation project.

## References

[1] Ackoff, Russell L., Management Misinformation Systems, Management Science 14, No. 4 (1967) B147–156.

[2] Alford, M.W., A Requirements Engineering Methodology for Real-Time Processing Requirements, IEEE Transactions of Software Engineering SE-6, No. 1 (1977) 60–69.

[3] Applegate, L.M., G. Klein, B.R. Konsynski and J.F. Nunamaker, Model Management Systems: Proposed Model Representations and Future Designs, Proceedings of the Sixth International Conference of Information Systems, Indianapolis (1985) 1–16.

[4] Baker, Kenneth R., Introduction to Sequencing and Scheduling (Wiley, New York, NY, 1974).

[5] Bodart, F., A-M. Hennebert and J-M. Leheureux, Computer-Aided Specification, Evaluation and Monitoring of Information Systems, Proceedings of the Sixth International Conference of Information Systems, Indianapolis (1985) 27–44.

[6] Churchman, C. West, The Design of Inquiring Systems (Basic Books, New York, NY, 1971).

[7] Colter, Mel A., Evolution of The Structured Methodologies, in: Couger et. al., (1982) 73–96.

[8] Couger, J.D., M.A. Colter, R.W. Knapp, eds., Advanced System Development/Feasibility Techniques (Wiley, New York, 1982).

[9] Courtois, P.-J. On Time and Space Decomposition of Complex Structures, Communications of the ACM 28(6) (1985) 590–604.

[10] Date, C.J., An Introduction to Database Systems (3rd ed.)(Addison-Wesley, Reading, MA, 1981).

[11] Davis, Gordon B., Strategies for Information Requirements Determination, IBM Systems Journal 21, No 1 (1982) 4–30.

[12] De, P. and A. Sen, A New Methodology for Database Requirements Analysis, MIS Quarterly (1984) 179–193.

[13] Frenkel, Karen A., Toward Automating the Software-Development Cycle, Communications of the ACM 28(6) (1985) 578–589.

[14] Gane, C., and T. Sarson, Structured Systems Analysis: Tools and Techniques (McAuto/McDonnell Douglas Corporation, St. Louis, M, 1977).

[15] Geyer, R.F. and J. van der Zouwen, eds., Sociocybernetics (Martinus Nijhoff, Leiden, 1978).

[16] Hax, A.C. and D. Candea, Production and Inventory Management (Prentice-Hall, Englewood Cliffs, NJ, 1984).

[17] IBM Business Systems Planning, International Business Machines Corp. report GE 20-0527-3 (1981).

[18] Ives B. and G.P. Learmonth, The Information System as a Competitive Weapon, Communications of the ACM 27, No. 12 (1984) 1193–1201.

[19] Kaje, Matti, The Tasks and Tools of Corporate Managers (in Finnish)(Weilin and Goos, Helsinki, 1978).

[20] Kaje, M. and R. Nevalainen, DAJE (Diagonal Matrix Method) System for Corporate Management and Development (in Finnish) (DAVA Institute, Otakustantamo, Jyvaskyla, 1986).

[21] Kerner, David V, Business Information Characterization Study, DATA BASE 10, No. 4 (1979) 10–17.

[22] Konsynski, B.R. and J.F. Nunamaker, PLEXSYS: A System Development System, in: Couger et al. (1982) 399–423.

[23] Kottemann, J.E. and B.R. Konsynski, Dynamic Metasystems for Information Systems Development, Proceedings of the Fifth International Conference on Information Systems (1984) 187–204.

[24] Lano, Robert J., A Technique for Software and Systems Design [Elsevier, North Holland, New York, 1979).

[25] Lockemann, P.C. and H.C. Mayr, Information Systems Design: Techniques and Software Support, in: H.J. Kugler, ed., Proceedings of the 10 $^{th}$ IFIP World Computer Congress, Dublin (1986) 617–634.

[26] Lundeberg, M., G. Goldkuhl and A. Nilsson, Information Systems Development: A Systematic Approach (Prentice-Hall, Englewood Cliffs, NJ, 1981).

[27] March, J.G. and H.A. Simon, Organizations (Wiley, New York, NY, 1958).

[28] McFarlan, F.W. and J.L. McKenney, Corporate Information Systems Management (Irwin, Homewood, IL., 1983).

[29] Nolan, Richard L., Managing the Crises in Data Processing, Harvard Business Review, March–April (1979).

[30] Porter, Michael, Competitive Advantage (Free Press, New York, NY, 1985).

[31] Pounds, William F., The Process of Problem Finding, Industrial Management Review, Fall (1969).

[32] Rich, Elaine, Artificial Intelligence (McGraw-Hill, New York, 1983).

[33] Rockart, John F., Chief Executives Define Their Own Data Needs, Harvard Business Review (March–April, 1979) 81–93.

[34] Ross, Douglas T., Structured Analysis (SA): A Language for Communicating Ideas, IEEE Transactions on Software Engineering SE-6, No. 1 (1977) 16–34.

[35] Sathi, A., M.S. Fox and M. Greenberg, Representation of Activity Knowledge for Project Management, IEEE Transact. on Pattern Analysis and Machine Intelligence PAMI-7, No. 5 (1985) 531–552.

[36] Schonberger, Richard J., Operations Management: Productivity and Quality (2nd ed.) (Business Publications, Plano, TX, 1985).

[37] Simon, Herbert A., The Sciences of the Artificial (MIT Press, Cambridge, MA, 1982).

[38] Sprague, R.H. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[39] Teichroew, D., and Hershey D.A.III, PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems, IEEE Transactions on Software Engineering SE-6, No. 1 (1977) 41–48.

[40] Vepsalainen, Ari, Modeling of Corporate Planning, Tech. Lic. thesis (in Finnish), Helsinki University of Technology (1978).

[41] Vepsalainen, A. and T.E. Morton, Priority Rules for Job Shops with Weighted Tardiness Costs, Management Science 33, No. 8 (1987) 1035–1047.

[42] Vepsalainen, A. and P.R. Gupta, Competitive Systems Discipline: Focusing on Service before Productivity, Decision Sciences working paper 87-03-04, The Wharton School, University of Pennsylvania (1987).

[43] Williamson, Oliver E., Transaction Cost Economics: The Governance of Contractual Relations, Journal of Law and Economics 22 (1979) 233–261.

[44] Williamson, Oliver E., The Economics of Organization: The Transaction Cost Approach, American Journal of Sociology 87(3) (1981) 548–577.

[45] Winograd, Terry, Beyond Programming Languages, Communications of the ACM 22(7) (1979) 391–401.
