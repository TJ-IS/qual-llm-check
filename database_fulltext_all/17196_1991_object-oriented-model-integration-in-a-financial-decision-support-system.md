---
otero_id: 17196
otero_key: "FXGP4MDF"
title: "Object-oriented model integration in a financial decision support system"
authors: "M.A.H. Dempster; A.M. Ireland"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90062-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Object-oriented model integration in a financial decision support system \*

M.A.H. Dempster

Dalhousie University, Halifax, N.S. B3H 1Z5, Canada and Balliol College, Oxford, England OX1 3BJ and University of Essex, Colchester, England CO4 35Q

A.M. Ireland

Saint Mary's University, Halifax, N.S., Canada B3H 3C3

Decision support systems for users without modeling expertise require domain-specific modeling knowledge to translate between conceptual and mathematical problem views. In complex, dynamic decision situations using multiple model types, the system must create and modify individual models to reflect changing conditions and assumptions, maintain consistency among different models in the same decision situation and allow communication among models for their complementary use, all without relying on user expertise. This paper describes a system for debt decision support which flexibly formulates and integrates optimization and simulation modeling and heuristic reasoning for non-expert users through an object-oriented, domain-specific knowledge base. Stable domain relationships and mathematical procedures are encapsulated in domain object classes; domain object instances are combined to form common model representations manipulated by operators specific to each model type. The approach is applicable in domains in which stable entities and interactions exist and in which model flexibility results from varying combinations of entities – conditions which are found in many financial and other business modeling situations.

Keywords: Model management, Model integration, Scenario-based dynamic stochastic programming, Financial decision support systems.

Introduction

A major goal of decision support systems research is provision of flexible, dynamic modeling environments for users who are not modeling specialists (Elam and Konsynski 1987). Such an environment must contain application domain knowledge for mapping between user and model problem views; modeling knowledge for model formulation, solution and modification; and model management knowledge for user guidance in model manipulation and interpretation. Where multiple model types are used, such systems must recognize when and how to apply each type, maintain consistent problem descriptions for various models (or recognize and handle inconsistencies), provide for communication among different models and present a uniform interface shielding the inexperienced user from modeling details.

These requirements have only begun to be realized in current model management research. Work on generalized model management systems has provided formal, data-independent model representations and suggestions for generalized manipulation languages (Bonczek et al. 1981; Blanning 1985; Geoffrion 1987) but has not yet solved practical synthesis, consistency or multiple-model integration problems. Research on model synthesis (Murphy and Stohr 1986; Dhar and Pople 1987; Dhar and Croker 1988) has successfully illustrated model formulation from fragments for a single model type (linear programming or simulation) but has not considered different model types applied to a common decision situation.

Artificial intelligence researchers have realized the importance of specific domain knowledge in extending the capabilities of rule-based expert systems beyond that of generalized problem solvers (Davis 1984). Similarly, domain-specific research in decision support and model management has led to more immediately successful systems because the characteristics of individual domains can be exploited to add power to the systems. Examples include an actuarial modeling system (Sivasankaran and Jarke 1985) which is able to formulate and execute problem-solving plans using multiple models sequenced according to varying problem descriptions, and a production planning system which formulates linear programs based on object-oriented domain entity descriptions (Binbasioglu and Jarke 1986).

This paper describes the model synthesis and integration aspects of a system called MIDAS (Manager's Intelligent Debt Advisory System) which provides assistance to non-expert users in the configuration and complementary use of multiple model types in a limited but complex financial management domain. We address issues of flexibility, consistency and communication among multiple model classes using a common frame-based problem representation with object-oriented programming features. In this representation, domain objects encapsulate facts, mathematical relationships and qualitative relationships for common use by all model types. These objects act as building blocks for a common representation of each problem situation which is manipulated by operators carrying out configuration, reasoning and solution procedures as required for each model type. The approach takes advantage of the structural characteristics of the domain and model types to produce a powerful and flexible modeling environment for non-expert users.

In the following sections we present the problem domain, overall system architecture and the model types and heuristics which provide the system's debt planning framework. These are followed by a description of the knowledge representation and model control techniques which give MIDAS the ability to formulate and integrate multiple complex models consistently and flexibly. We close with some observations on domain-related success factors and some suggested design principles for systems of this type.

## Problem and system overview

Our problem domain is corporate debt planning for a Canadian public utility. The organization's Treasurer must develop and implement borrowing plans to meet forecast cash requirements over a rolling planning horizon (usually 2 to 5 years) at minimal cost subject to risk, market and other internally and externally imposed constraints. Financing sources include domestic and foreign public bond markets, banks, equipment suppliers and local consumers through savings bonds. Constraints arise from external market conditions such as limitations on amounts available from particular sources, and from internal conditions such as a desire to smooth cash flows in future operating periods. Finally, the future interest and exchange rates which determine costs are uncertain and subject to fluctuations of varying degrees depending on future economic conditions and the financial soundness of the corporation as perceived by rating agencies.

Total borrowing cost and risk (cost variation) is a product of many interacting conditions and decisions. For example, \$100 million needed for five years beginning today could be borrowed at a fixed rate for five years, in which case costs are known for the entire period, or for two years with refinancing after the initial term, in which case costs depend on refinancing arrangements and applicable future interest rates. Developing a borrowing plan is thus a portfolio management problem, in which the debt portfolio is the collection of debts used over the planning horizon to meet cash requirements. The problem is highly complex because the planning horizon extends over a number of time periods, many decisions may be required, and borrowing decisions are contingent on previous borrowing decisions and on future interest and foreign exchange rates. It also requires great modeling flexibility to handle multiple portfolio configurations and the innovative types of debt that are regularly being created and offered as potential portfolio components.

Currently, the Treasurer supports borrowing decisions with spreadsheet-based deterministic cost projections for individual borrowing alternatives. A model is constructed for each possible debt issue (callable bond, bond with a sinking fund, savings bond, mortgage, etc.) and costs are calculated over the planning horizon using varying interest and exchange rate assumptions. This has the advantage of modeling flexibility, since any debt can be ‘custom-modeled’ using a new spreadsheet; it also allows the Treasurer to assess the sensitivity to future rates of one debt’s cost. However, it is limited to deterministic rate scenario specifications, and it does not capture the full portfolio or contingency aspects of the debt management problem because it models individual decisions without their interactions.

Several more comprehensive modeling techniques are applicable to borrowing decisions, particularly when borrowing is regarded as an investment problem with cash flow directions reversed. Stochastic linear programming (Crane 1971; Bradley and Crane 1972, 1975, 1980; Crane, Knoop and Pettigrew 1977; Lane and Hutchinson 1980), mixed integer programming (Shapiro 1987) and dynamic programming (Elton and Gruber 1971;

Kalymon 1971; Boyce and Kalotay 1979) have all been applied to debt or investment portfolio management. Stochastic simulation is a well-known tool for capital budgeting analysis and has been applied to the analysis of borrowing alternatives (Hertz 1964; Bradley and Crane 1975; Howard 1986). As in other domains, optimization techniques can handle simplified versions of the problem but cannot practically solve problems in the detail required for actual decisions. On the other hand, simulation can flexibly model many details but cannot suggest optimal solutions, particularly in complex decision situations. We are not aware of any efforts to combine optimization and simulation analysis for portfolio decision support, although this approach has been demonstrated for overall corporate financial planning (Hamilton and Moses 1973, 1974).

The approach we have chosen in MIDAS is the complementary use of stochastic linear programming and simulation modeling, extended with rule-based modules. The two models and their extensions support a hierarchical planning process in which borrowing plans are produced and refined in successive stages (fig. 1). First, the user states a borrowing problem in terms of its planning horizon, cash requirements, performance goals and available debt types. He then uses a scenario-based stochastic programming model to build an optimal but simplified borrowing plan based on a probabilistic 'tree' representation of his assessment of future rates. A rule-based plan refinement module examines the optimal plan and produces several candidate plans with additional details and decision values rounded to marketable quantities; these plans are no longer optimal but will satisfy the stated borrowing requirements. Finally, the simulation tests the candidate plans by projecting their future cash flows, costs and ending portfolio values for comparison and evaluation. Each of the modeling components is run with the assistance of a dedicated assistant module, and all components (and planned additional modules for model checking, interpretation, and other functions) are linked by an object-oriented knowledge base, which maintains a consistent portfolio and domain description underlying all model and rule operations. Because the system is highly modular with a flexible interface, it can also be used for subsets of the complete planning process such as testing individual borrowing decision alternatives or a user-defined borrowing plan.

![](/api/attachments/FXGP4MDF/fulltext/images/3f041a03efca83c31a0e7ceb91acd9dce1ad02c2d71a2b0531d3b729e672c8d3.jpg)  
Fig. 1. MIDAS Architecture.

This approach replaces spreadsheets with two types of modeling (stochastic programming and stochastic simulation) which are not familiar to the system's intended user except at a broad conceptual level. Lack of experienced and trained staff able to build and run such models has kept these sophisticated techniques from being used in the past. MIDAS is therefore designed to lessen the need for a scarce intermediary by automating model formulation, solution, modification, sensitivity analysis, and presentation of results. The system is being implemented in KEE (Fikes and Kehler 1985; Stefik and Bobrow 1986; Filman 1988) and LISP on a Unisys Explorer workstation, with its optimization model solver implemented in FORTRAN, running on a MicroVAX II Ethernetted to the Explorer.

## Optimization modeling

Following Bradley and Crane and Lane and Hutchinson, MIDAS's optimization modeling uses scenario-based stochastic linear programming to minimize the expected debt portfolio value at the end of the planning period subject to cash requirement, maximal debt cost, corporate and market constraints. Decision variables correspond to 'debt types' consisting of hypothetical debts for various terms in various markets; decisions are amounts of debt issued, held and retired of each type, contingent on realized rate scenarios. All interest is financed through debt so that the objective function (ending debt portfolio value) reflects total borrowing cost financed at minimal rates. (A formal specification of the model is found in Dempster and Ireland 1988).

Because the system solves a single decision problem (debt portfolio selection), the optimization model's general form is constant regardless of the particular decision situation. However, decision variables and constraints, both user-controlled at this time, vary with parametric analysis requirements in individual decision situations in the short term and changing market conditions in the longer term. Flexible and efficient model formulation is therefore an important performance criterion for the system.

## Heuristic plan refinement

The optimization model suggests an optimal debt plan in the form of a portfolio of realized decisions (debts) with specified issue dates, markets, terms, principal amounts, and features. However, as it is now specified, the optimization model simplifies reality. To be solved in reasonable time, we have eliminated integer-valued constraints such as market minimum borrowing constraints (which are either 0 or a minimum value). We have allowed decisions to be continuous even though in practice debt issue amounts for the test corporation are usually in multiples of \$25 million. We have also ignored sinking funds as decision variables. (Certain debts may be issued with or without sinking funds – investment funds which build toward the repayment value at the end of the debt term).

To modify the optimal solution into a feasible ‘real-world’ plan, a rule-based module reviews optimization model output at user request and modifies it by suggesting alternatives for the optimal but simplified decisions. Simple heuristics reduce the number of alternative plans by altering decisions in groups by market or by a system-produced significance ranking, and constraints other than cash or cost requirements are checked and maintained during the modification process. Violations of cash requirement constraints (i.e., borrowing too much or too little in a time period) are noted and penalized during plan simulation.

## Simulation modeling

MIDAS's simulation is a spreadsheet-style projection of cash flows, ending market value, and borrowing costs over the planning horizon for each portfolio. It can be done either in a single pass with the mean rate scenarios in the rate event tree, or in multiple passes using randomly-generated rates consistent with the underlying rate scenarios. (For details of the rate generation process, see Dempster and Ireland 1988.) Single-pass deterministic simulations produce detailed cost and performance figures by time period; multiple-pass simulations produce distributions for various performance indicators including ending value and net present cost as well as details for the mean-rate scenarios.

## Knowledge representation

Several types of knowledge and processing are required to support MIDAS's diverse functions. The system's implementation mixes several knowledge representation and reasoning/control techniques as appropriate but relies primarily on KEE frames and object-oriented programming.

KEE frames exhibit the usual characteristics of inheritance network representations in which generic object classes are defined, specialized, and instantiated as nodes in a hierarchy (Minsky 1975; Fikes and Kehler 1985; Stefik and Bobrow 1986; Intellicorp 1987). Classes and instances contain attributes describing their properties and relationships; attributes and their values are inherited downward through the hierarchy unless overridden. Frames also contain methods (LISP procedures) specifying object operations; like attributes, these are inherited unless modified or overridden. This representation allows modular, non-redundant specification of domain entities, relationships and behaviors.

MIDAS objects fall into three broad groups according to their knowledge types and functional roles within the system. MODEL OBJECTS represent entities in the problem domain such as debts, investments, markets and rate scenarios; they describe and model the problem domain and store the common problem states referred to in all system operations. MODEL MANAGEMENT OBJECTS store model management knowledge and perform the intermediary functions which allow the novice user to operate, manipulate, and interpret the system's models; they comprise the optimization and simulation assistants previously referred to. SYSTEM SUPPORT OBJECTS organize the knowledge and procedures necessary for generalized system control and support functions such as windowing, menu generation, table and graph presentation, and system housekeeping. The three groups of objects generally work in a hierarchical relationship in which users interact with system support objects, which request action from model managers, which in turn request detailed modeling in either optimization or simulation mode from the domain model. In the following section, we describe the model representation in more detail since it is through these objects that MIDAS's model formulation and integration functions are implemented.

## Model objects

Model objects, which represent domain entities, are the primary vehicle in MIDAS for representing domain and modeling knowledge and for carrying out model processing. These objects structure facts, parameter values, and assumptions about the domain and function as building blocks for the system's models. Rules for model refinement and other non-algorithmic functions refer to and modify the model objects, which together describe the current problem state. Model objects thus provide a clear semantic starting point for communication between system users and developers, a natural mapping between domain and model concepts and relationships and a flexible, modular, easily extendable modeling environment.

## Basic and composite model objects

Because MIDAS views debt planning as a portfolio management problem, the central model objects in the system are financial instruments (debts and investments) and portfolios of these instruments. Financial instrument objects are referred to as ‘basic model objects’ because they are the fundamental building blocks for the portfolio models used to evaluate possible borrowing plans. Portfolios, or groups of financial instruments, are referred to as ‘composite model objects’.

Financial instruments include both debt and investment types which are relevant for debt planning. (The need for investments arises when sinking funds are used and when surplus cash is invested for short periods.) Each financial instrument encapsulates descriptive attributes (interest rate, principal amount, issue date, term, maturity date, etc.) and their values. Each is also capable of modeling its own financial performance, given future interest and exchange rates; the results of individual borrowing alternatives can thus be modeled using individual financial instrument objects.

Financial instruments are defined within the system using an inheritance hierarchy of debt and investment classes (fig. 2). The hierarchy follows the standard asset/liability classification scheme used in financial statements and by financial managers. The inheritance hierarchy streamlines financial instrument definitions in several ways. First, attributes and their default values are defined at the highest possible level and inherited by subclasses and instances. Second, behaviors or results associated with financial instrument classes are described either through rules or (more commonly) through numeric algorithms, again defined at the highest possible level and inherited downward. Third, multiple inheritance is used to create instances of debts having features of more than one subclass, as when bonds with collections of features such as a call feature together with a sinking fund are required.

Portfolios are composite model objects which group individual debts and investments. Portfolio performance is modeled as the combined performance of the individual instruments in the group, so that financial instrument objects form (rather large) fragments for comprehensive portfolio models. Portfolios supervise coefficient generation for optimization and simulation of portfolios, handle interactions among objects and summarize portfolio results. It is these composite objects which provide the flexibility needed to configure models for debt portfolios reflecting alternative borrowing plans.

## Model support objects

Objects representing domain entities which are part of the environment affecting the debt planning task are referred to as 'model support objects'. These objects provide assumptions, constraints, and evaluation criteria for debt planning.

![](/api/attachments/FXGP4MDF/fulltext/images/f62c50aa623b83b0c6f54474dceb0d35cca005c9d3c0bd797c9cc20bfa81b8f5.jpg)  
Fig. 2. MIDAS financial instrument class hierarchy.

MIDAS's model support objects include the borrower (borrowing corporation), borrowing plans, financial markets (domestic and foreign), and rate event trees. The borrower handles financial goals, cash requirements, and constraint parameters arising from borrower policies and preferences. Borrowing plans specify borrowing actions to be taken in order to meet financing requirements over the planning horizon, as well as decision rules or strategies to be used to adjust financing actions during the course of the plan for dynamic response to certain conditions. Financial markets provide default debt types for borrowing in various markets, hold market-related constraint values such as maximum allowable borrowing in a period and provide market interest and exchange rates (deterministic or stochastic) consistent with existing rate scenarios as required by mathematical models or rule sets.

Random interest and exchange rate generators are implemented as methods in financial market objects. The general rate-generation algorithms are defined in the top-level market class; parameters which customize each rate generator for its particular market, based on historical market performance, are stored as attribute values in the market instance.

Uncertainty is handled in MIDAS through rate event trees, which represent branching, probabilistic rate movements over the planning horizon, as forecast outside the system (fig. 3). Rate events are incorporated into both the optimization and simulation modeling processes through KEEWorlds (Filman 1988); each path (called a scenario) in a tree specifies a KEEWorld with its own future rates, corresponding borrowing actions and projected portfolio performance. KEEWorlds are further utilized to represent and simulate multiple borrowing plans arising from the application of plan refinement heuristics.

In addition to attribute values and model operators, all model objects incorporate methods for handling their own maintenance through form-based input, consistency checks and attribute value displays. This allows system control methods to remain general, ignoring the maintenance details for individual sub-models and support objects.

## Model controllers

Although each financial instrument and portfolio object is capable of carrying out a cash flow projection (deterministic simulation) for itself, high-level model control for both the optimization and simulation models is handled through separate objects dedicated to this task. These controllers encapsulate parameters and methods for directing model execution through sequential, procedural LISP code or rule-based reasoning as appropriate.

## Model formulation and operation

Using this scheme, MIDAS is able to formulate, solve and modify both optimization and simulation models as integrated collections of model objects. Each model is formulated by first building a model-object representation of the problem situation, including a borrowing plan, borrower and market conditions, rate scenarios and a hypothetical debt portfolio; this dynamic domain representation reflects the current state of problem analysis at any time and is referred to and modified by all modeling processes. For modeling, the representation's current attribute and cash flow values are translated into particular model formats and 'solved' using model operators (methods) specific to each model type. This approach is similar in spirit, if not in implementation, to Geoffrion's (1987) structured modeling, which describes models with abstract descriptions of entities and relationships and then solves them with separate model operators.

![](/api/attachments/FXGP4MDF/fulltext/images/ad2bd4b9c062ea4c3bc65cda23412d1c9a253f08b871c06db1c18ff176eca58e.jpg)  
Fig. 3. Interest rate event tree.

## Simulation modeling

The simulation is conceptually simpler than the optimization model, since it carries out straightforward cash flow projections for individual debts and investments and accumulates them for portfolios. Each financial instrument object contains all methods necessary to calculate its future cash flows and performance over the planning period. (Cash flow projection for a particular debt is accomplished in a predefined, sequentially executed series of calculations called in order by a procedural method in the debt object.) A full portfolio projection is controlled by procedural methods in a portfolio object, which send messages in turn to all debts in the portfolio requesting period-by-period cash flow calculations, summarize portfolio activity, handle cash surpluses and deficits, and compute all requested performance indicators. High-level simulation control, including random rate generation, execution of multiple simulation passes, and summarization of results, is controlled through generalized simulation operators (methods) in the simulation controller; for details see Ireland (1988).

Computational details for deterministic simulations of individual debts and portfolios are stored uniformly in output tables, giving a complete simulation history for examination by other system components. This allows recalculation of only affected parts of the mean simulation for sensitivity analysis purposes. For stochastic simulation, computational detail for the mean-rate case is stored to provide an audit trail for subsequent analysis by the user or the system.

## Optimization modeling

As with the simulation, a specific optimization model is formulated through the underlying domain representation and solved through high-level methods in a model controller. However, the domain description prior to optimization differs from that before simulation because borrowing actions and resulting financial instruments are unknown. For purposes of optimization, a portfolio consists not of specific debt objects but of debt alternatives – borrowing possibilities in the form of partly-specified financial instruments. (The optimization model selects from these possibilities to produce a plan which fully specifies the corresponding financial instruments.) A borrowing possibility is a debt object starting in a specific rate scenario and time period with principal equal to \$1. Its known scenario and start date determine its associated interest and exchange rates; its \$1 principal gives per-dollar coefficients when cash flows are projected. At this time borrowing possibilities are defined by the user prior to the start of optimization; future plans are to incorporate heuristic possibility selection.

Once the borrowing possibilities portfolio is defined, generalized methods in the optimization controller request coefficient generation, build the input matrix, send the matrix to the solver, and request solution. Input is set up in a fixed-format standard extending the MPS format to handle stochastic programming (Birge et al. 1987).

Output from the LP solver has the form of decision variable values, i.e., amounts of each debt type borrowed, held, or repaid. These are stored in a straightforward manner in the debt variable instances as principal amounts and repayment schedule attributes (amounts held are implicit results of issue and repayment amounts). Shadow prices from the solver now used are not meaningful; when they do become useful, they will be stored as additional attributes in decision variable objects. Meanwhile, parametric analysis using multiple calls to the solver is used to develop a profile of the maximal cost constraint/objective value relationship, with results stored as portfolio parameters.

Mathematical relationships in the linear program are extended by simulation to produce detailed tables of financial results rather than coefficient matrices; consistency with the optimization model is maintained (a) through the use of common methods for cost calculation and ending market-value assessment, (b) through a penalization procedure in the simulation which mimics recourse (short-term borrowing) penalties in the linear program, and (c) through debt financing of all interest and sinking fund payments as in the optimization model's cash requirements constraint. New borrowing decisions are generated heuristically using user-specified rules by the simulation whenever additional cash is required (as, for example, when a plan modification results in too little borrowing in a given period); the simulation of course differs from the optimization in not generating optimal borrowing decisions in these cases.

## Design principles

Both the simulation and optimization models are highly complex in terms of the number of parameters, algorithms, and output values involved, and their variations among the numerous financial instruments modeled. Additional complexity arises from the treatment of uncertainty through branching scenarios and stochastic simulation. Formulating such models and maintaining their flexibility and user accessibility thus goes beyond the straightforward input/output specifications used in simpler situations.

Four design principles are largely responsible for the power, flexibility and efficiency of MIDAS's model formulation and operation. These are:

1. Object definition through multiple inheritance. Multiple inheritance allows the creation of financial instruments with many different combinations of features from limited plan or user specification; an instrument automatically acquires all necessary attributes and methods merely through specification of its (possibly several) parent classes. Attribute requirements, input prompts, and calculation methods are inherited for only the requested features in a financial instrument; default values are likewise inherited and eliminate the need for complete specification of attribute values in situations where plan details are not yet under consideration.

2. The use of standard method names and protocols. This principle follows the object-oriented programming convention of standard method names and argument lists for similar behaviors regardless of object type. The use of these standards for all financial instruments and portfolios allows us to ignore calculation details which vary with object type, once they are implemented and tested within object classes; for example, the standard message ‘calculate.interest (time period)’ may be used to produce a value for interest for any object regardless of its particular interest computation method. The standard messages can thus be treated as a set of operators for producing parameters or manipulating model objects in accordance with modeling requirements.

3. Extensive ‘information hiding’. This principle limits access to an object’s internal attribute values to specific attributes necessary for that object’s interaction with others (Meyer 1988). For example, attribute slots could be defined as external (available to other objects) or internal (not available except to the object’s own methods). Although KEE does not formally support information hiding, MIDAS adopts the convention that all values passed among objects are passed through message arguments rather than accessed directly by methods.

4. Separation of domain knowledge from model control through meta-knowledge in model objects. Method code for cash flow summarization and model control is procedural to the extent that specific tasks are specified in order; it does not contain specific attribute or object references that limit its flexibility. For example, each financial instrument 'knows' which cash flow items are relevant to it; the portfolio object consults this knowledge in deciding which slots to summarize. As a result, high-level model control methods can readily accommodate variations in debt and investment cash flows and other attributes, and new model operators can be implemented without specific knowledge of the internal structure or operations of individual sub-models.

Integration within each model is thus accomplished through multi-parented objects, standardized object interfaces, meta-knowledge within objects and generalized modeling routines. The first three of these principles embody the object-oriented programming philosophy of objects as selfcontained ‘machines’, of which knowledge of internal details is not required for their combination into cooperating groups. The fourth principle applies to modeling the well-known artificial intelligence approach of separating knowledge from reasoning and control.

## Multiple model integration and communication

Multiple-model DSSs provide the ability to analyze a single problem in several ways that may or may not be consistent in their assumptions, internal algorithms, or preconditions for meaningful application. Where the DSS user is not a modeling expert, such inconsistencies can lead to confusing differences in model results which the user may not be able to reconcile. As we have seen, MIDAS's use of a common domain representation gives common assumptions, parameter values and low-level calculations such as coefficients for all models, extending integration to include access to common algorithms as well as common data values.

The use of domain objects as common underlying conceptual and operational sub-models ensures model consistency and communication in several ways:

1. Both types of models are configured or reconfigured simultaneously when a portfolio is created.

2. The different models have common parameter values for coefficient and simulation result calculations, arising from their definition and storage in common model and support objects.

3. The models use the same methods for common calculations even though results are used for different purposes in the modeling process.

4. All model communication, including communication with rule-based reasoning modules, is through the common objects. Input to and results from each model or rule set are stored as attribute values available to the entire system.

5. Because underlying objects store intermediate domain states, the optimization, refinement, and simulation models are linked in the staged planning process supported by the system. Each has a well-defined, complementary function to perform in adding to or modifying the domain description.

## Conclusions and future directions

Our primary achievement to date is the illustration of a system enabling complementary use of multiple, complex models and rule-based components in a complex domain by a non-expert user. Relying on extensive object-oriented domain and modeling knowledge, the system shields the user from modeling technicalities while retaining the ability to flexibly configure borrowing plans in response to changing assumptions or conditions. It is clear from this work that domain-specific knowledge can provide a common conceptual structure for organizing and controlling input, computations, and results for different modeling techniques applied to a single problem. Moreover, domain knowledge and system-based translation between user and model problem views is a fundamental requirement for modeling assistance to inexperienced users.

The system as developed so far is weak in the areas of user help, result interpretation and model formulation for innovative debt types; also, it does not yet assist in evaluating borrowing plans based on simulation results. We expect that these facilities will be added as the prototype system becomes operational and supported within the test corporation. The other major effort planned for the MIDAS project is enhancement of the modeling assistant modules to provide intelligent user support in interpreting and refining model results for both the optimization and the simulation components (Dempster and Ireland 1988). Our preliminary design utilizes a combined frame- and rule-based diagnostic approach, so that the underlying representation described in this paper will continue to support enhanced power for user modeling assistance.

Our domain-specific approach contrasts with two other directions in intelligent decision support systems research. In designing and developing MIDAS, we have not attempted to build from formalisms to a working but circumscribed system, cf. Geoffrion (1987). Neither have we attempted to provide generalized support for modeling of a general class such as activity analysis by linear programming (Murphy and Stohr 1986). Instead, we have chosen a complex, semi-structured domain and induced design principles from both domain structure and user heuristics. This has allowed us the freedom to explore our domain and its modeling support requirements guided by user needs; attempts to formalize or generalize will arise from insights we gain through building a fully functioning real-world system.

Nevertheless, we observe that the design principles and model integration techniques identified in this paper appear applicable to any domain in which (a) stable entities and interactions exist, (b) model flexibility results from varying combinations of entities, and (c) deterministic simulation is a useful analytical tool and a generator of input for other modeling techniques. Examples which we have identified include corporate financial planning, research and development, and integrated design/manufacturing/maintenance project control.

To summarize, our approach to model formulation and integration relies on an underlying domain model for support of generalized modeling algorithms. In so doing, it extends the role of the structural domain model in an intelligent decision support system beyond support for single models and heuristic planning to formulation and integration of multiple complex models and rules. The result is increased model flexibility and consistency for decision support for inexperienced users.

## References

Binbasioglu, M., and M. Jarke (1986). Domain-specific DSS tools for knowledge-based model building. Decision Support Systems 2, 213–223.

Birge, J.R., M.A.H. Dempster, H.I. Gassmann, E.A. Gunn, A.J. King, and S.W. Wallace (1987). A standard input format for multiperiod stochastic linear programs. COAL Newsletter, Mathematical Programming Society 17, 1–19.

Blanning, R.H. (1985). A relational theory of model management. Working Paper No. 85-106, Owen Graduate School of Management, Vanderbilt University, Nashville, Tennessee.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston (1981). A generalized decision support system using predicate calculus and network data base management. Operations Research 29, 263–281.

Boyce, W.M., and A.J. Kalotay (1979). Optimum bond calling and refunding. Interfaces 9, 36–49.

Bradley, S.P., and D.B. Crane (1972). A dynamic model for bond portfolio management. Management Science 19, 139–151.

Bradley, S.P., and D.B. Crane (1975). Management of bank portfolios. New York: Wiley.

Bradley, S.P., and D.B. Crane (1980). Managing a bank bond portfolio over time. In: M.A.H. Dempster (ed.), Stochastic Programming. London: Academic Press, 449–471.

Crane, D.B. (1971). A stochastic programming model for commercial bank bond portfolio management. Journal of Financial and Quantitative Analysis 6, 955–976.

Crane, D.B., F. Knoop and W. Pettigrew (1977). An application of management science to bank borrowing strategies. Interfaces 8, 70–81.

Davis, R. (1984). Amplifying expertise with expert systems. In: P.H. Winston and K.A. Prendergast (ed.), The AI Business. Cambridge, Mass: MIT Press, 17–40.

Dempster, M.A.H., and A.M. Ireland (1988). A financial expert decision support system. In: G. Mitra (ed.), Mathematical models for decision support, NATO ASI Series F48. Heidelberg: Springer-Verlag, 415–440.

Dhar, V., and A. Croker (1988). Knowledge-based decision support in business: issues and a solution. IEEE Expert 3, 53–62.

Dhar, V., and H.E. Pople (1987). Rule-based versus structure-based models for explaining and generating expert behavior. Communications of the ACM 30, 542–555.

Elton, E.J., and M.J. Gruber (1971). Dynamic programming applications in finance. Journal of Finance 26, 473–506.

Elam, J.J., and B. Konsynski (1987). Using artificial intelligence techniques to enhance the capabilities of model management systems. Decision Sciences 18, 487–502.

Fikes, R., and T. Kehler (1985). The role of frame-based representation in reasoning. Communications of the ACM 28, 904–920.

Filman, R.E. (1988). Reasoning with worlds and truth maintenance in a knowledge-based programming environment. Communications of the ACM 31, 382–401.

Geoffrion, A.M. (1987). Introduction to structured modeling. Management Science 33, 547–588.

Hertz, D.B. (1964). Risk analysis in capital investment. Harvard Business Review 42, 95–106.

Howard, C.D. (1986). Applications of Monte Carlo simulation to corporate financial liability management. Paper presented at the Financial Management Association Conference, New York.

Intellicorp (1987). KEE v.3.0 User Guide. Menlo Park, Cal.

Ireland, A.M. (1988). Object-oriented financial modeling: a case study. Proceedings of the Sixteenth Annual Conference, Administrative Sciences Association of Canada.

Kalymon, B.A. (1971). Bond refunding with stochastic interest rates. Management Science 18, 563–575.

Lane, M., and P. Hutchinson (1980). A model for managing a certificate of deposit portfolio under uncertainty. In: M.A.H. Dempster (ed.), Stochastic Programming. London: Academic Press.

Meyer, B. (1988). Object-oriented software construction. Englewood Cliffs, NJ: Prentice-Hall.

Minsky, M. (1975). A framework for representing knowledge. In P.H. Winston (ed.), The Psychology of Computer Vision. New York: McGraw-Hill.

Murphy, F.H., and E.A. Stohr (1986). An intelligent system for formulating linear programs. Decision Support Systems 2, 39–47.

Shapiro, J.F. (1988). Stochastic programming models for dedicated portfolio selection. In: G. Mitra, ed., Mathematical models for decision support, NATO ASI Series F48. Heidelberg: Springer-Verlag, 587–611.

Sivasankaran, T., and M. Jarke (1985). Logic-based formula

management strategies in an actuarial consulting system. Decision Support Systems 1, 251–262.

Stefik, M.J., and D.G. Bobrow (1986). Object-oriented programming: themes and variations. The AI Magazine 8, 40–62.
