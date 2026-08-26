---
otero_id: 16907
otero_key: "WMH7ZKKM"
title: "Representing modeling knowledge in an intelligent decision support system"
authors: "Jane Fedorowicz; Gerald B Williams"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90116-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Representing Modeling Knowledge in an Intelligent Decision Support System

Jane FEDOROWICZ $^{+}$ and

Gerald B. WILLIAMS \*

$^{+}$ MIS Department, School of Management, Boston University, 704 Commonwealth Ave., Boston, MA 02215 and $*$ Electrical Engineering and Computer Science, The Technological Institute, Northwestern University, Evanston, Illinois, USA

Knowledge representation for data, models, and other decision support system (DSS) elements is a complex and ever-adapting task. The representation scheme for an intelligent DSS will need to provide general problem-solving model management activities as well as a mechanism for refining and testing the applicability of these models for each problem instance it encounters. We present traditional knowledge representation alternatives, and demonstrate why a multi-level scheme is superior for DSS use. We advance a two-level scheme, joining the advantages of connection graphs for the generalized analytical requirements and a frame component for problem-specific query resolution.

Keywords: Decision Support Systems; Knowledge Representation Schemes; Artificial Intelligence

![](/api/attachments/WMH7ZKKM/fulltext/images/21a6c945f8dfe8dabb6afe8a019cf5d0ff1eddcf6402d5e62120746305e685a2.jpg)

Jane Fedorowicz is an Associate Professor of Management Information Systems at the Boston University School of Management. She has a B.S. in Health Systems from the University of Connecticut. She holds M.S. and Ph.D. degrees in Systems Sciences from Carnegie-Mellon University. She is a member of ACM, SIM and TIMS. Her publication list includes articles in Communications of the ACM, SIGMOD Record, Health Care Management Review, Journal of the

American Society for Information Science, and the Journal of Medical Systems. Her current research interests are in the application of artificial intelligence techniques to the design of decision support systems, and the impact of these systems on individual decision-making.

## 1. Introduction

Knowledge representation research efforts have been focused historically in the subfields of artificial intelligence (AI) known as expert systems and natural language processing. It is our view that many of the techniques employed can be transferred to the newer area of AI-based Decision Support Systems (DSS). In particular, knowledge representation will have impact on how data and models will be used in the DSS of the future.

Traditional DSSs are composed of three basic elements: a database, a model base and a user interface. The database may be the corporate database, or one that has been specifically designed to accompany the DSS package. The model base usually consists of a series of domain-dependent models (i.e., models which support a particular class of problems encountered by the intended user). The user interface allows the end user (in most cases, a manager) to select appropriate data and models to perform an analysis in response to a particular problem. The choice of an analysis may be up to the user, in which case s/he must procedurally specify the required inputs to the analysis. The other option is to give the user access to a set of stored analyses, limiting the flexibility of the system at the same time that the

![](/api/attachments/WMH7ZKKM/fulltext/images/658408fd5715c3ecb88700a7d0c1685ece9d67f629bacabbc77e1e3bd1c9952c.jpg)

Gerald B. Williams received a B.A. in mathematics from William Jewell College, M.S. in statistics (77), an M.B.A. in finance from Miami University, and an M.S. in computer science from Northwestern University, where he is presently a candidate for a Ph.D. in computer science. From 1977 to 1982 he served on the faculty of the School of Business Administration at Miami University in the Department of Decision Sciences. Currently he is involved in a large knowledge-based CAD research project at the Gould Research Center in Rolling Meadows, Ill. His research interests include intelligent decision support systems, knowledge engineering, generalization of problem solving methodologies, and the development and use of AI system tools. He is a member of the Association for Computing Machinery, SIGART, and the American Association for Artificial Intelligence.

user is freed from having to be acquainted with the necessary procedural instructions for constructing the analysis. Combinations of these two approaches are also possible.

Knowledge representation in such an environment is fairly straightforward. The database uses a traditional representation (e.g., relational or network), and the model base is a set of procedures accessible through the user interface (e.g., METAPHOR, ESCA, IFPS). It is only when a more powerful DSS design is introduced using AI that knowledge representation becomes an important issue.

## 2. AI Component

In addition to the basic functions of a DSS, an intelligent DSS (IDSS) contains generalized decision-making aids. The AI-based component of the system must generate the requisite data for an analysis and transform it, if necessary, before it can be used by whatever models and routines the system has assessed to be appropriate in responding to a query. Also, the system must be able to detect and store higher-level knowledge about the applicability of its suggested solution tactics. A generic IDSS is depicted in Fig. 1.

In a DSS with inherent intelligence, the data usually found in a company's database will be augmented by other types of knowledge. Examples of knowledge include statements of company-related facts (All shipments to Europe originate from the New York office), corporate assumptions (Assume an inflation rate of 4.5% for 1986), and external information (Competitor X spent \$3,000,000 or 2% of income on R&D in 1985 and Competitor X is assumed to have allocated the same percentage of income to R&D for 1986). These types of knowledge are stored along with the more typical database content in the IDSS's knowledge base.

The model base contains both canned procedures (e.g., SPSS or linear programming modules) and custom-built models. The appropriate models are retrieved in much the same way as in the more traditional system: a call is issued by the IDSS when all necessary data and parameter settings have been supplied. The difference in use of the models lies in the manner in which their selection is made. This involves the component called the problem processor [6].

![](/api/attachments/WMH7ZKKM/fulltext/images/cdf1e8f3961e6e0d592ce7cb7597e6d2774bedfcd270c495545e635522ac5274.jpg)  
Fig. 1. Components of an Intelligent Decision Support System.

The problem processor translates the query issued through the user interface into a form that will interact with stored knowledge to select appropriate solution strategies. This definition is intentionally vague so that it will encompass many approaches to knowledge representation, selection and use. We will discuss alternative knowledge representation schemes (KRS) in the next section of this paper. Suffice it to say that the distribution of responsibility for data, knowledge and model selection will vary depending on the KRS and the type of control mechanism used in the problem processor.

## 3. Knowledge Representation Schemes-The Basics

## 3.1. Evaluation Criteria

Undeniably, the process of developing an appropriate representation is the central issue in any problem solving effort. Consequently, the importance of this task becomes increasingly paramount as one is continually challenged by the necessity of capturing (for some class of solution methods) the broader knowledge that enables the exhibition of intelligent behavior. The construction of a viable KRS is now recognized as the core component of any valuable DSS [6].

'At some uninteresting theoretical level, all computer-based KRS schemes are equivalent' [22] which is based on the necessity to translate any language into arrangements of bits in memory. However, it is clear that within a specified area of application, one representation scheme may be more advantageous to the user than another because of certain powerful features that are made convenient by the language. No single representation scheme can hope to be universally most powerful across all applications. Thus, identification of an appropriate representation is often problem-dependent and is never completely deterministic. At best one can identify a set of generalized properties that characterize good KRS features and exploit these properties to the advantage of the user.

As a guideline to the type of KRS features that lead to intelligent behavior in DSSs we offer the following comments (which are not intended to be exhaustive). For a more complete discussion see [4],[5],[6],[10],[15],[16],[22]:

1. The KRS should provide an abstraction of the application domain that is intuitively clear to the user (i.e., the 'knowledge engineer').

2. The KRS should be complete in that it represents all the necessary information and their relationships within an application and the KRS should be concise in that it does so efficiently.

3. The KRS should provide efficient access to the information represented by the scheme for the purposes of storage, retrieval, and modification.

4. The KRS should accentuate the important issues of a problem while suppressing the rarely used details necessary for completeness. (In terms of a specific DSS application consider a lease/buy decision model. The important aspects of the problem include available lending rates, life of the asset, and perhaps particular tax implications, while less important details such as the name and address of the lending institution while necessary for completeness do not directly affect the decision.)

It is generally accepted that most knowledge representation approaches in AI are built from components that belong to one of the following categories: logic-based approaches, semantic networks, or frames [10]. In what follows we will review these three primary KRS classifications and discuss their merits.

## 3.2. Logic-Based Approaches

Formal logic is the direct result of man's age-old desire to understand the nature of human reasoning and knowledge. Logic has been specifically constructed to capture the notions of truth and inference in human thought processes. Consequently, the idea of employing the well-founded results of mathematical logic as a method of symbolically representing knowledge is intuitively attractive. This attraction is quickly justified by examining some of the immediately obvious attributes of mathematical logic as a KRS.

Logic is a tremendously general language which, by its own design, provides a clearly defined interface between the semantic intent of an expression and its symbolic representation. The theory of logic is well-founded and has been actively studied, producing many efficient computational techniques that guarantee the consistency and soundness of resulting inferences [8],[23].

Several prominent representation schemes that are commonly cited as possible KRS foundations have their roots in the study of formal logic. We will review the more comprehensive approaches to processing logic-based knowledge while reminding the reader of the myriad of ‘variations on a scheme’ (e.g., [12]).

## 3.2.1. Resolution

Typically logic-based problem processing systems are founded on the computational method of predicate calculus referred to as resolution refutation. The essential idea of a resolution refutation process is to determine whether or not a statement expressed in the first-order predicate calculus infers a contradiction. The statement is a problem representation in terms of its axioms, pertinent data and the denial of a hypothesized conclusion. If the hypothesized conclusion is in fact true with respect to the problem's axioms and data then the inclusion of its denial as part of the problem statement will create a contradiction. The resolution refutation process, based on the resolution principle ([17],[18]) is a sound rule of inference providing a solution strategy that is guaranteed to find a contradiction in the problem statement if indeed a contradiction exists (i.e., the resolution process is complete).

While resolution theory provides computational methods for the predicate calculus that are sound and complete, problems exist with the complexity of solution control that often render the generalized search process infeasible. The central problem of resolution theorem proving is the vast number of clauses generated before a proof (verification of a solution) can be found. There do exist a number of strategies that begin to reduce the complexity of the solution search process by guiding, restricting, deleting or editing the possible resolutions. However, no known strategy provides a completely satisfactory approach.

## 3.2.2. Connection Graphs

As in ordinary resolution, connection graphs are constructed from the clause form representation of the application. Nodes are created for each literal of each clause and are partitioned into clauses (i.e., all and only the literals of a given clause are in a partition). Edges link unifiable literals and are labeled with the most general unifier for the corresponding nodes. The mode of solution is to identify a set of literals exhausting partial solutions that collectively eliminate the literals of a target or start clause.

The motivation for connection graph use results from the premise that many axioms of an application description are irrelevant to the solution process of a given problem instance. In the process of constructing the graph and evaluating the interrelationships of the expressed axiom components, one strives to determine the profitable inferences and avoid the combinatorial explosion of resolvents that characterizes general resolution strategies [20]. The avoidance of unnecessary or unprofitable (yet logically correct) inferences coincides with the desire to emulate human abilities to derive solutions in a direct straight-forward manner.

## 3.2.3. Production Rule Systems

A production rule system (PRS) is an unordered set of relatively independent data sensitive rules. In this scheme a rule is meant to be the atomic form of knowledge representation canonically represented by the following template:

## IF (antecedent conditions) THEN (consequences)

Conceptually a production rule system's architecture and processing mechanisms are quite simple.

A PRS generally consists of a set of production rules, a working memory and a simple control mechanism that is responsible for: (a) matching information contained in the working memory with the requirements of a rule; (b) selecting the rule(s) to be used based on the results of the match; and (c) executing the selected rules. For further discussion of production rule systems see [7].

As a justification of the production rule system as a model of human thought processes, it is often argued that a single rule corresponds well to a unit of human problem-solving knowledge. Rules are generally transparent with respect to their meaning and carry explicit explanatory information. That is, the reason a rule is fired can be extracted immediately by comparing the state of the working memory with the conditions required by the rule. Further, the ability to match data with either the antecedent or the consequence of a rule facilitates forward reasoning, backward reasoning or some appropriate combination of both.

The use of a production rule system as a KRS is especially appropriate when the problem solving environment is complex and the solution control procedures are not known in advance. A PRS is also well-suited in representing applications that expect a large number of modifications over a period of time and in representing loosely coupled problems that can be decomposed into relatively independent subproblems with no fixed order of solution processing.

The major advantages realized from the use of production rule systems stem from the inherent separation of the problem-knowledge and control-knowledge. Factual knowledge can be stored in fairly independent modules allowing easy modification and expansion of the knowledge base. Since the control structure is simple and non-sequential a production rule system has the ability to react successfully to unanticipated situations by applying knowledge when it is appropriate rather than during some predetermined procedure sequence. These same features facilitate the possibility of parallel computation on independent pieces of an application.

Still, many problems are not well represented by a PRS. Because of the non-directive nature of the control mechanism, possible undesirable interactions among rules and unpredictable behavior may occur. Problems that are by nature highly sequential or for which probably correct algorithms (or good approximation procedures) exist are not good PRS candidates. For example, problems involving numerical calculations or approximation methods, such as mathematical modeling procedures, are in general better represented by methods other than production rule systems. Classification is the most appropriate use of this technique.

## 3.3. Semantic Networks

A network is a system of nodes and links where each node represents an object and each link connects two nodes that are in some way related. A semantic network differs from an ordinary network in that descriptive labels attached to the links and nodes tend to ascribe an informal, intuition-based semantics to the network. However, as a KRS an intuitive semantics is not strong enough. Instead, the intended meanings of a semantic network must be formalized to present a clear, stable, and unambiguous picture of the represented application. There is no set of unifying principles governing the construction and use of a semantic network that will guarantee the satisfaction of these formalization requirements, yet the following guidelines present a vehicle by which one can create a reliable semantics definition [22].

To assure a consistent interpretation of a description represented by a semantic network there should exist an equivalence semantics that relates the network description to description methods of representation schemes that do possess an accepted semantic definition (perhaps the predicate calculus). The set of procedures designed to manipulate the semantic network should have well-defined meanings (i.e., procedural semantics) that reflect the tasks they perform. Likewise, a descriptive semantics must be explicitly stated to provide an explanation of exactly how a component of the network is used to represent an object, an event or an action.

The semantic network is a powerful representation scheme due to tremendous flexibility and intuitively pleasing explanatory capabilities. A large class of naturally occurring problems involve the codification of objects and their relationships. Any application that requires a description framework based on a complicated taxonomy is an excellent candidate for representation as a semantic network. They are especially well-suited for constructing inheritance hierarchies.

Caution must be exercised in the use of semantic nets as with most KRSs. As alluded to earlier, the success of a semantic net is dependent on a well-planned, highly structured definition. The power and flexibility of the system may be hard to control in complex applications while a failure to allow adequate descriptive power could impede the recovery of essential information or preclude unanticipated situations. As expected, the computational burden on a semantic network KRS increases significantly as the size of the representation grows.

## 3.4. Frames

The concept of frames as a knowledge representation vehicle originated from the realization that the primary building blocks of artificial intelligence and psychological theory should represent relatively large chunks of well-structured information relating to perception and reasoning ability. The typical and appropriately amorphous definition claims a frame to be a data structure for representing prototyped/stereotyped concepts or situations (i.e., acts, objects or events) [13,14]. Frames are an attempt to organize the representation of knowledge into a structured framework that facilitates recall and inference and most importantly, supports the interpretation of new data in terms of previous knowledge concerning similar experiences.

Although the actual implementation details of a frame-based KRS may vary radically, it is pedagogically astute to draw an analogy between a record with fields and a frame with slots. The difference lies in the additional powers ascribed to the slots of a frame. In general a slot provides information describing the pertinent details of a situation that the frame is intended to represent. A slot is filled (i.e., assigned a value) by one of several methods detailed below, giving rise to a frame system's power and flexibility of representation.

## 3.4.1. Defaults

Many slots of a frame can be pre-filled with values that remain somewhat stable within a class of situations being represented. This allows the explicit representation of information that is assumed to be pertinent even when facts are not explicitly stated in the input. Default values are said to be loosely connected to a slot to emphasize the system's willingness to accept new slot values when the input data indicates a conflict or special case attribute value that differs from the original default values.

## 3.4.2. Procedures

Often the information needed to fill a slot requires some conditional computational power or data-driven inference processing. In such cases it is appropriate to initially assign to a slot the name of a process that will provide the desired data. When it becomes necessary to obtain information from a procedure-filled slot, the indicated process is invoked and the result returned as the value of the slot. Conditional statements that enable the procedural knowledge are referred to as triggers.

## 3.4.3. Demons

To facilitate a sufficient level of abstraction using a frame KRS it may be necessary to initially ignore descriptive details below some determined level. Upon encountering an application, the system must rely on its capability to recognize conditions under which it becomes necessary to dynamically modify the frame, possibly adding new slots, or enhancing the descriptive power of the old slots. Processes that produce side-effects such as these are referred to as demons. Demons differ from the procedures described above in that they are called when needed and are not necessarily dependent on the details of the invoking application.

## 3.4.4. Scripts

Often an adequate description of a particular application requires the expression of a stereotypical event sequence in addition to the 'value' information supplied by defaults and procedures ([1],[19]). For example, consider the case where management wishes to obtain market analysis information related to a particular product. The explicitly important attributes of a market analysis would include details such as product type, target market definition, current market position, profit margin, etc., all examples of data that are well represented as frame slot values. What is not explicitly represented with this value information is the generic sequence of events that describes the analysis process (e.g., a survey is taken, the results analyzed, inferences made, a report generated and sent to the parties of interest). The expression of a sequence of actions that are relevant to a situation description is called a script and can be represented in a frame as a specialized slot that contains multiple values.

The ultimate power of a frame-based KRS comes from the realization that the values of a slot may be filled with another frame. The notion of a multileveled hierarchical frame system facilitates data manipulation efficiencies through inheritance of higher-level attributes by the nested concepts occupying the slots of some ancestral frame. The inheritance process and the use of default values provide relatively inexpensive instantiation capabilities.

The strategy of the processing mechanism of a frame-based KRS is quite simple. Based on initial clues extracted from early input the system will attempt to select a potentially suitable frame and proceed to instantiate the various slots. As accumulated information begins to disclose more details it may be determined that the original frame is slightly inappropriate or that another frame will provide a better representation structure. If this is the case a frame change can be made and the slot fill-in process continued. This frame switching strategy and its control, although intuitively pleasing, is the major computational obstacle of efficient use and implementation. However, once the appropriate frame is selected the system functioning process is very effective.

## 4. Macro and Micro Levels of Representation

There are many types of knowledge within the IDSS, as discussed earlier. The KRS chosen to represent this knowledge must be able to differentiate between general (or meta) knowledge and instantiations of that knowledge (i.e., its application to a particular problem occurrence). The solution space stored within the IDSS supports a parallel structure. Data, models and linkages will have a general structure, but also must dynamically adapt to a particular user request. For example, a general request to predict 1986 sales will make use of a regression routine. After obtaining actual data from the data base, the system should test a number of assumptions that must be upheld before the regression can be run. Tests on the data may show irregularities, suggesting that an alternative formulation must be employed. This may require the use of a different model altogether, or merely a change in the defaulted model parameters.

The KRS are defined to represent the general (macro) structure of the solution space. We are proposing that a distinction be made between the macro level and the instantiated or micro level. By separating the two types of structures, we will be able to provide the user with general problem-solving capabilities and at the same time, supply detailed alternative formulations representative of the myriad of options resplendent in present-day analysis. It is precisely this array of alternative model configurations that differentiates the management of models in the IDSS from the far simpler task of data management.

## 5. Combinations of KRS

Many of the shortcomings of KRSs lie in their inability to support IDSS requirements at both the macro and micro levels. Most schemes differentiate between a macro level generalization and a micro level instantiation only by providing two (or more) distinct representations (e.g., two production rules, clauses, or frames/slots). For example, a logic clause stating that sales data is to be retrieved from the database would read

\~ Lessthan(year, 1985) \~ SALES(year, amount)
\~ Display(amount) Query('sales', year, ?)

Another clause would be required to state that 1985 data must be computed rather than retrieved.

\~ SALES(year, amount) \~ Regress(amount, year, A, B) \~ Predict(A, B, '1985', expected)
\~ Display(expected) Query('sales', '1985', ?)

These series of micro level representations will quickly lead to an explosion in size of the knowledge base and may greatly increase solution time. Both of these issues point to a need for separating macro and micro knowledge requirements.

Combinations of KRS are found in expert systems research. An example is the CENTAUR system [2], in which rules are one type of value for slots, and slots may be represented by separate frames. LPS [3] combined production rules with frames, but prohibits the inclusion of procedures in slots. In addition, notable contributions are beginning to appear in commercially available expert system tools, lending credence to our contention that a single representation scheme does not offer a sufficient solution. Silverman [21] lists the following shells as possessing the ability to switch from backward to forward chaining, from rule- to frame-based orientation, or from symbolic to graphical representations: the Knowledge Engineering Environment (KEE) from Intellicorp, LOOPS from Xerox Special Information Systems, and, to some extent, S. 1, ART, and SRL + .

Dolk and Konsynski [10] present a frame-like concept called a model abstraction in one of the first attempts at applying formal KRS to model management and IDSS design. These abstractions, or frames, are accessed by either a metaframe or by a semantic network. Details on the access method are not included in their presentation, so a direct analogy to the macro/micro delineation cannot be made.

One proposal for a multiple-KRS scheme for logic-based IDSS is presented in the next section. The proposed scheme conforms to the requirement of domain independence, and supports both macro and micro level representations.

## 6. Knowledge Representation Using GUTS

The functions of any IDSS include user specification of a task, classification and selection of solution procedures, and execution of the analysis. As discussed earlier, multiple representation schemes are required to adequately describe both macro and micro level concepts. The KRSs underlying our proposed system employ connection graphs and frames at the macro and micro levels respectively. In what follows we will elaborate on our choice of KRS.

Our system has three components as depicted in Fig. 2. The first component translates a user request from natural language to the clause form required by the Graph Upkeep and Task Support system (GUTS). GUTS is a macro level process controller whose specific functions include the determination of the appropriate solution paths in the connection graph, addition of new clauses to the connection graph or modification of an existing graph. Much like the Knowledge Representation System and the Assessment and Deduction System in [9], and the Language System and Problem Processor of [6], these components free the user from having to specify requisite procedures and knowledge resident in the knowledge base. The knowledge base, our third component, contains five distinct parts. These are a model base, a database, a set of connection graphs, a set of frames which reference the model base, and other domain-dependent knowledge such as assumptions and parameters.

![](/api/attachments/WMH7ZKKM/fulltext/images/6680c04cc3c2a3e86affa0103d17f3b8c2618a3a3d4fee0e67a1ffc11cc4fe40.jpg)  
Fig. 2. Proposed System.

Upon receipt of a user query expressed in clause form, GUTS will link it to an appropriate graph and assess the possible solution paths. This involves the invocation of applicable frames, database calls, and other pertinent knowledge which together comprise input to the models designated within the solution path. Successful completion of these processes will trigger execution of the frame-specified models.

## 6.1. Connection Graph Component

As explained earlier, a connection graph is a specialized instance of a first order logic representation scheme expressed in clause form. The types of literals in a graph will inherently determine the system's behavior and can, for purposes of explanation, be categorized by their intended role within a level (i.e., macro and micro). Although the specific duties of each literal type vary, the ultimate effect of each is to instantiate the arguments of the connection graphs. Here we present a brief discussion of the specialized functions of each literal type. (See also [6] and [9] for a discussion of more limited sets of literal types.)

## 6.1.1. Deduction Literals

The purpose of a deduction literal is to provide a vehicle through which two clauses can be linked during the construction or modification of a connection graph. The arguments of a deduction literal represent an integral part of the inter-clausal communication process allowing control and consistent instantiation of the problem parameters. All deduction literals will resolve away when a satisfactory solution path is established.

## 6.1.2. Process Literals

A process literal causes some arithmetic, Boolean, or other type of operation to be performed. Examples include Add, Less than, Report and Compare.

## 6.1.3. Frame Literals

Frame literals are used to establish a link between the connection graph and the model base through the frame construct. Each frame literal represents a call to a particular frame where the arguments of the literal provide model parameter value definitions.

## 6.1.4. Data Retrieval Literals

A call to the database is handled by the connection graph through a data retrieval literal. As expected, the data attribute specification details necessary for the identification of the information to be retrieved are carried by the literal's arguments.

## 6.1.5. Translation and Aggregation Literals

It must be anticipated that the stored form of the information in the database may not correspond to the data input requirements of a selected model process. For example, the analysis of a company's sales data may require the total sales per division which may not be explicitly stored in the database. Rather, the divisional sales would be an aggregation of individual sales performance within the separate divisions. An aggregation literal must bridge the explicit/implicit data representation gap.

Similarly, the analysis request (whether from the user or from another process) may specify output according to some convenient or necessary terms not explicit in the database (i.e., as a simple case, a request for sales figures in terms of German marks may need to be translated from U.S. dollars, the monetary unit stored in the database). This process is the function of a translation literal [11].

## 6.1.6. Constraint Literals

Often it is the case that an analysis request may impose specific conditions on the process result or even on the analysis method. The notion of constraint exists independently at both the macro and micro levels. It is conceivable to request an analysis of a given problem while restricting the process to a particular set of desired analysis tools (i.e., a constraint at the macro level). At the same time a request to limit the results to a certain class of answers would constitute a micro level constraint [9]. For example, a lease/buy analysis can be conducted using many different combinations of financial modeling tools. Because of company policy or a personal preference the user may elect a given analysis process by limiting (at the macro level) the available models for the given class of application (e.g., only allow straight line depreciation of an asset). At the micro level the manager requesting an optimal assignment of resources to projects may insist that at least 30 man hours per week be devoted to each project. Another example of micro level constraints would be their use in testing assumptions for statistical analyses. Generalized constraint literals for micro level considerations are a part of the system's frame component.

## 6.1.7. I/O Literals

The input/output literals are designed to handle the user communication chores for cases when the system may have to request additional information from the user or report analysis status to the user.

## 6.1.8. Format Literals

Similar to the I/O and translation literal functions, format literals can be used to observe system protocol requirements. It is also important to realize that format literals can be used to control the inter-model communication process for those cases where output from one model is expected as input to another in another form [11]. Theoretically, these literals are not needed. However, in reality, many canned programs have very strict formatting requirements, justifying their inclusion here.

## 6.2. Frame Component

The frame component represents a collection of model specific knowledge packages (i.e., frames) containing the information necessary to complete the instantiation of a model's parameters upon the designation of its use by the connection graph (in GUTS). For each model resident in the model base there exists one (or more) associated frame(s) in the frame component. A frame specifies the parameter structure of a model, default parameter values, data input/output characteristics, inherent assumptions, related models, optional model configurations, and other application, specific details necessary for appropriate model use. It is the structure of this mechanism that enables the domain-independent performance of the system's problem processor (GUTS).

GUTS works with the connection graph and frame components in different ways. The connection graph component provides one or more possible solution strategies which are determined upon user query (since the graphs are precompiled). All generated paths (analyses) are followed in the solution process. The frame component, on the other hand, is not precompiled. The appropriate options within a frame are evaluated during query instantiation, and results of one stage of frame processing may determine the next activity, much as in an expert system. A single solution is provided to the frame literal that called the frame from the connection graph.

Obviously, the type of information needed to specify the appropriate activation of a model is diverse and must be represented by various means. The ability to assemble these diverse representation types into a manageable unit is facilitated by the frame's slots. By definition, the slots of a frame serve only as labeled conduits through which a system can access information pertinent to a given context. The type of knowledge stored in a frame slot is virtually unrestricted. Each slot contains a logic clause or a single literal that resolves with the connection graph once the frame is instantiated.

The least complex use of a slot in our proposed system is to hold parameter values with the realization that the actual values are subject to change under given conditions. Typically a value slot is initially instantiated with a default value or set of values. Then, when and if conditions warrant a change, these values can be altered. For example, unless otherwise specified, a hypothesis-testing model may assume (by default) a test level of significance of 0.05.

In a complex setting, we use a frame slot to access additional frames that may relate to the current analysis. For instance, portions of the frame may represent a relatively generalized implementation of a model that has several specific instances appropriate under varying circumstances. The details of these offspring models can be accessed through other frames that are bound to a slot in the parent frame.

Similarly, the valid use of a given model often depends on the satisfaction of some preliminary assumptions about the nature of the data being analyzed. One slot of the model's associated frame will contain information indicating the appropriate assumptions for the analysis by referencing models used to check the assumptions' status. In turn execution of an assumption model involves the use of its associated frame. We do not exclude the possibility of recursively referencing a frame either directly or indirectly.

Analogous to the design of the connection graph component of GUTS, each frame in the frame component is represented as a structured relationship of clauses in first order logic. The literals used to construct the clauses of a frame representation are consistent with the literal types defined in the previous section. At the core of each frame is a process clause whose single positive literal serves as the link to the frame call literal generated either by GUTS or some parent frame. The remaining literals of the process clause act as slot fillers when they link with related clauses depicting the necessary data for the model's appropriate use.

We generically refer to various frame slot types as a method of indicating their ultimate purpose. We acknowledge these categorizations to be intentionally loose to compensate for the unavoidable overlap of duties. The prominent types and a buried description of their intended purposes are listed here.

Value slots—provide parameter settings or similar information that is inherent in the model's use and is relatively constant over time.

Default slots—initially hold information representing the best guess or the most probable circumstances. Defaults are loosely connected to facilitate change by either the user or as a result of problem specific information recognized by the system.

Alternative slots—facilitate the selection of an option (by the system or the user) from a well defined set of options.

Procedure slots—represent processes that are external to model execution but are essential to its appropriate use (e.g., providing a mechanism to iteratively apply a test for population normalcy at each level of the independent variable when validating ANOVA assumptions).

Assumption slots—generally contain a list of models that can be used to test the validity of a model's use. Each assumption model would call up another frame to process.

Constraint slots—provide conditions that must be met by the model's implementation.

Related frames slots—contain recovery procedures if problems are encountered in processing; also might be used to recommend related analysis frames.

## 7. Future Research

This discussion represents the initial stage of an ambitious research effort. It is the intent of this paper to illustrate the conceptual structure of an intelligent domain-independent decision support system. The implementation stage will force the refinement of the frame component in terms of its definition, composition and behavior. Special attention must be given to the concepts of information, temporal relationships and the problems of imprecision in the storages and evaluation of knowledge. Major efforts will concentrate on the system definition, access capabilities and modification skills of GUTS. The final design issue will be concerned with the user interface and translator.

From a more general perspective, we will continue the examination of competing knowledge representation schemes in decision-making environments with expectations of gaining additional insight into the relationships and analogies between human and machine knowledge-processing techniques. The understanding of the human decision-making process at the individual level is paramount in the development of valuable decision support tools.

## 8. Conclusion

We have outlined various knowledge representation schemes and discussed their application to intelligent decision support systems and model management system design.

In harmony with the stated KRS evaluation criteria, an argument is made for a two-level scheme within the IDSS in which problem-solving abstractions of the application domain are represented by structures resident in the macro level, and complete or instantiated strategies are concisely represented in the micro level. We propose a system using a logic-based macro-component reppresentation that exploits the efficiencies of a construct called a connection graph. Connection graphs comprise the active component of the Graph Upkeep and Task Support system (GUTS). GUTS accepts a clause form query and instantiates frames associated with models in the model base. The process proceeds in a top-down fashion accentuating the prominent problem solving issues first. Details of the knowledge base components are described including database representations, process calls, data translation, aggregation of formatting, constraints, input and output, assumption testing and other representation issues.

## Acknowledgement

This work was conducted while J. Fedorowicz was a J.L. Kellogg Research Professor at the J.L. Kellogg Graduate School of Management at Northwestern University.

## References

[1] Ableson, R.P., Psychological Status of the Script Concept, Amer. Psychol. (July 1981).

[2] Aikens, J.S., Prototypical Knowledge for Expert Systems, Artif. Intell. 20 (1983) 163–210.

[3] Anzai, Y., Y. Mitsuya, S. Nakajima and S. Ura, LPS: A Role-based Schema-oriented Knowledge Representation System, J. Inform. Process. 14 (1981) 177–185.

[4] Applegate, L.M., G. Klein, and B.R. Konsynski, Model Management Systems: Proposed Model Representations and Future Designs Proc. Sixth International Conference on Information Systems, Indianapolis, December (1985) 1–16.

[5] Barr, A., E. Feigenbaum and P. Cohen, The Handbook of Artificial Intelligence, 3 vols., William Kaufman, Inc., Los Altos CA (1982).

[6] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[7] Browston, L., L., R. Farrell, E. Kant and N. Martin, Programming Expert Systems in OPS5, Addison-Wesley, 1985.

[8] Chang and Lee, Symbolic Logic and Mechanical Theorem Proving, Academic Press, New York (1973).

[9] Chen, M.C. and L.J. Henschen, On the Use and Internal Structure of Logic-based Decision Support Systems, Decision Support Systems 1 (1985) 205–219.

[10] Dolk, D and B. Konsynski, Knowledge Representation for Model Management Systems, IEEE Trans. Software Engineering (Nov. 1984).

[11] Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support

in Complex Organizations, Proc. First International Conference on Information Systems, Philadelphia, December (1980) 98–110.

[12] Kimbrough, S.O., A Graph Representation for Management of Logic Models, Decision Support Systems 2 (1986) in press.

[13] Minsky, M., Framework for Representing Knowledge, in: Winston, P.H. (ed.), The Psychology of Computer Vision, McGraw-Hill, New York (1975).

[14] Minsky, M. (ed.) Semantic Information Processing, MIT Press, Cambridge (1968).

[15] Nilsson, N., Principles of Artificial Intelligence, Tioga Publishing Co., Palo Alto CA (1980).

[16] Rich, E., Artificial Intelligence, McGraw-Hill, New York (1983).

[17] Robinson, J.A., A Machine-Oriented Logic Based on the

Resolution Principle, J. Assoc. Comput. Machin. 12 (1965) no. 1.

[18] Robinson, J.A., The Generalized Resolution Principle, in: Machine Intelligence, vol. 3, Michie, D., (ed.) Elsevier North-Holland, New York (1968).

[19] Schank, R.C. and R.P. Ableson, Scripts, Plans, Goals and Understanding, Erlbaum, Hillsdale NJ (1977).

[20] Sickel, S., A Search Technique for Clause Interconnectivity Graphs, IEEE Comput. c25 (August 1976).

[21] Silverman, B.G., AI Development Tools in Review, CAIMS Newsletter, Providence RI (April 1985).

[22] Winston, P.H., Artificial Intelligence, 2nd edn., Addison-Wesley, Reading MA (1984).

[23] Wos, L., R. Overbeek, E. Lusk and J. Boyle, Automated Reasoning, Introduction and Applications, Prentice-Hall, Englewood Cliffs, (1984).
