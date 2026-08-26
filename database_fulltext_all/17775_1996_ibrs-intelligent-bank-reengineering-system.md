---
otero_id: 17775
otero_key: "KVYKDA2Q"
title: "IBRS: Intelligent bank reengineering system"
authors: "Daniel Moonkee Min; Jong Ryul Kim; Won Chul Kim; Daihwan Min; Steve Ku"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00021-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# IBRS: Intelligent bank reengineering system

Daniel Moonkee Min $^{a,*}$ , Jong Ryul Kim $^{a}$ , Won Chul Kim $^{a}$ , Daihwan Min $^{b}$ , Steve Ku $^{c}$

$^{a}$ DongSung Inforcomm, Inc., 158-24 SamSung-dong, KangNam-ku, Seoul, 135-090, South Korea $^{b}$ Business School, Korea University, Seochang-dong, Jochiwon, Choongnam, 339-700, South Korea $^{c}$ Battelle, 2101 Wilson Blvd., Suite 800, Arlington, Virginia 22201, USA

## Abstract

Intelligent Bank Reengineering System (IBRS) is a knowledge based system which assists a bank in choosing the most appropriate Business Process Reengineering (BPR) alternative and in implementing the selected alternative. IBRS's problem solving approach consists of three stages: generation, evaluation, and choice. In the generation stage, IBRS identifies BPR alternatives from previous BPR cases which are represented using Integrated DEFinition (IDEF) modeling methodology. Constraint satisfaction search is employed to identify candidate BPR alternatives which satisfy the constraints of the bank such as goals, budget constraints, and other situational factors. IBRS evaluates the generated BPR alternatives by work flow analysis and functional economic analysis. Then IBRS chooses a BPR alternative based on a multi-criteria decision making procedure. The main benefits of IBRS are to facilitate BPR efforts by helping banks to identify problems, search for alternative opportunities, and compare and evaluate “To-Be” models generated. IBRS's knowledge base incorporates and utilizes the previous case studies, examples, and expert BPR knowledge. It will help improve quality, reduce cost, and explore feasibility and advantages of new technology and processes.

Keywords: BPR (Business Process Reengineering); IDEF model; Activity based costing; Knowledge base; Constraint satisfaction

## 1. Introduction

During the past decades, many corporates have been facing economic instability, intensified competition, budget reductions, and more demanding customers. Under these circumstances, many organizations have aspired to reevaluate their business performance and redesign their business processes $[1,13]$ . However, BPR attempts have not always been fruitful. In fact, successful identification and implementation of BPR requires substantial expertise in the target problem domain. The purpose of this paper is to present an IBRS which uses an expert system approach in facilitating BPR efforts.

## 1.1. Review of BPR methodology

BPR is defined as a fundamental analysis and radical redesign of critical business processes to achieve dramatic improvements in cost, quality, and service. It is the process of overhauling archaic, inefficient organizational structures and business processes.

United States Air Force initiated an Integrated Computer Aided Manufacturing (ICAM) program to build the composite architecture of aerospace manufacturing. A basic part of ICAM was IDEF – the ICAM DEFINition methodology or Integrated DEFINition. Since then, IDEF modeling technique has been popular in redesigning business processes both in the U.S. industry and government because it provides an easy but effective functional analysis of the business [11]. Specially, the U.S. Department of Defense mandated using the IDEF modeling technique in their BPR projects.

IDEF methodology involves process modeling (IDEF0), data modeling (IDEF1x), and work flow analysis (IDEF0 simulation). IDEF0 is a refinement of Structured Analysis and Design Technique (SADT) by Ross [12]. In IDEF0 modeling, an activity models the transformation of inputs into outputs performed by mechanisms under the constraints set by controls. Activities and interfaces are gradually decomposed to show more detail in the model. When an activity is decomposed, child screen inherits all relevant information, like author, activity, and data.

IDEF1x is a conceptual data base designing method based on the Entity-Relationship-Attribute model. In IDEF1x, things (that are represented by arrows in IDEF0) are modeled as entities. An entity can be described by its name, description, and a set of attributes. A relationship is an association among entity types. Business rules are represented by this relationship in IDEF1x.

The simulator component of the work flow analyzer of Meta Software [10] processes the static IDEF0 model to automatically generate a Petri-net model which provides statistics such as processing bottlenecks and idle resources. The Petri-net models actions, pre-conditions, and state transitions. The work flow analyzer helps to determine not only the time and resources required to perform each activity, but also the waiting time between processing steps and the idle time for resources such as staff and equipment. The Canadian Imperial Bank of Commerce used the work flow analyzer to identify the cause of bottleneck in check processing operations. The analysis revealed that the bottleneck occurred during the sorting task. By adding an extra person for sorting, an additional 95,000 checks a day were processed. The Canadian Imperial Bank of Commerce adopted smart card technology also to improve the convenience and security in corporate banking processes.

Functional economic analysis is a framework for modeling the costs, benefits, and risk associated with alternative investment and management practices. The approach is zero-based in that it considers a new way of doing business, managing organizations, and investing in information technology. That is, the tasks and activities of each organizational unit as well as all supporting technology and constraining regulations are potential decision variables. Functional economic analysis provides a more comprehensive evaluation information than work flow analysis.

## 1.2. IBRS approach

Effective BPR often requires the strategic use of advanced information technology. It involves in-depth analysis, exploration of alternative choices, careful evaluation of feasible solutions, and appropriate planning strategies for improvements which may require the construction of a new information system.

Various tools exist to assist some aspects of BPR, but these tools lack comprehensive assistance throughout the whole BPR process. The distinctive benefits and power of IBRS come from the comprehensive support that incorporates:

\- Application of the formal methodology such as IDEF modeling, work flow analysis, and functional economic analysis.

\- Utilization of the knowledge representation techniques, i.e. rules and frames to store previous BPR cases and to provide the basis for analysis.

\- Encapsulation of data model, process model, simulation model, economic model, and search model to empower the tool to carry out effective analysis and evaluation.

IBRS manages BPR in three stages. The first is the generation stage that identifies BPR alternatives based on user requirements and strategic goals. The current information system, i.e. the “As-Is” model, is represented using IDEF methodology. The constraint satisfaction search is employed to match and select candidate BPR opportunities from past experiences represented. The second is the evaluation stage that applies the work flow analysis and functional economic analysis to compare BPR alternatives. The third is the choice stage where the user selects the combination of BPR alternatives based on the generated evaluation statistics. The result of the choice stage is the best “To-Be” model. Once the “To-Be” model has been defined, the actual components of the new information system can be assembled from reusable codes from the code repository.

![](/api/attachments/KVYKDA2Q/fulltext/images/c1c49f50f9666b3dbb0e005ee4da2e97e48dde32b45e49b4df2f0270b95883cf.jpg)  
Fig. 1. IBRS components.

## 2. IBRS architecture

IBRS consists of two major modules: IBRS-Planner and IBRS-Constructor. The IBRS-Planner analyses the “As-Is” model and recommends the “To-Be” model, as shown in Fig. 1. The IBRS-Constructor uses the “To-Be” model and assists in constructing a new information system by assembling reusable codes from the code repository.

The model base of the IBRS-Planner contains various types of models such as the simulation model, functional economic model, IDEF0 process model, and IDEF1X data model. IDEF models are stored also in model definition languages which allow other tools, e.g. CASE tools, to utilize the IDEF model information. Behavior information can be added to an IDEF0 model which then can be used as a simulation model. Work flow analysis is performed by executing the simulation model. Functional economic analysis models provide cost/benefit analysis of the BPR alternative for the upcoming periods. Functional economic analysis model generates statistics such as net present values [4].

The planner knowledge base is a set of rules and frames which represents knowledge required to generate and evaluate BPR alternatives, and finally choose a BPR alternative. Rules are used to represent heuristic knowledge and frames are used to represent knowledge of domain entities. The knowledge of the BPR planner stored in the planner knowledge base covers:

• Smart card technology.

\- Performance history of smart card banking processes (process/performance).

• Performance history of smart card banking projects.

\- BPR model management (decomposition, integration, execution).

• BPR tool and methodology.

A smart card or an integrated circuit (IC) card has an IC chip on its surface and the size is the same as that of a credit card. Since the IC chip contains a CPU and memory, a smart card can process and store data up to 8k bytes. In addition to larger data storage, data security of smart cards is also much higher than that of magnetic stripe cards. Smart card technology provides an opportunity for banks to reengineer approval and payment processes; it allows off-line transactions and multi-applications in one smart card. While DongSung Inforcomm (DSI) [3] performs the smart card banking system projects for the KwangJu Bank, the DongNam Bank, and the Korea First Bank in Korea, the company has identified BPR opportunities and implemented the systems. The accumulated smart card banking knowledge of DSI is stored in the knowledge base of IBRS while IDEF0 process models are stored in the model base.

The IBRS-Planner solves a BPR selection problem by interacting with a user. A user specifies BPR selection criteria, and the planner assists in exploration of BPR opportunities by searching process models in the model base. The BPR selection problem is decomposed into three subproblems: generation, evaluation, and choice problem. IBRS' problem solving process consists of three corresponding stages similar to the knowledge-based hybrid modeling approach applied to production planning of flexible manufacturing systems [14,7,8]. The knowledge-based user interface design tool [5] incorporates the framework of generation, evaluation, and choice ap proach to automatically generate user interface presentation based on user specified constraints.

## 2.1. Generation

In the generation stage, IBRS identifies essentially a subset of BPR alternatives. IBRS analyses user's requirements and represents them as constraints. The process/performance matrix and constraint satisfaction reasoning are employed to identify candidate alternatives. The constraint factors that affect the selection process include the strategic goals and objectives, approved budget, size of the bank, and competitors' strategies.

The BPR generation problem is formulated as a Constraint Satisfaction Problem (CSP). CSP is a type of search problems. CSPs have three components: variables, values, and constraints. The goal of a CSP is to assign values to variables subject to a set of constraints. Thus, a CSP involves a set of n variables $(x_{1}, x_{2}, \ldots, x_{n})$ , each represented by its domain values $(D_{1}, D_{2}, \ldots, D_{n})$ and a set of constraints. The BPR generation problem, as a CSP, involves a set of n processes $(p_{1}, p_{2}, \ldots, p_{n})$ , each represented by its domain values $(0, 1)$ and a set of constraints. The goal of the BPR generation problem is assigning 0 or 1 to processes subject to a set of constraints. If 0 is selected as the value of $p_{i}$ , process i is included in the BPR alternative.

CSP algorithms include backtrack search algorithm and enhanced backtrack [2,9]. The most straightforward approach to solving CSPs uses the backtrack search algorithm. This generates a tree of all instantiations (assignments of values to variables), checking each instantiation against all earlier ones along the corresponding branch of the tree. Only if no incompatibility occurs between the current instantiation and a past one, does the branch become extended by instantiating the next variable with each of the values in its domain. This has a potentially great advantage over the brute-force generation and testing of all possible solutions, in that large subsets of inconsistent solutions are avoided each time a branch of the tree is pruned.

IBRS employs a backtrack search augmented with rule-based reasoning for checking feasibility of candidate solutions. Constraints are represented as rules and feasibility checking procedures are based on rule-based reasoning.

By using CSP search, IBRS prunes the decision alternatives of the BPR opportunities by matching the candidate solutions to user's requirements, and then passes on the selected business opportunities to the evaluation stage to be analyzed in more detail.

## 2.2. Evaluation

In the evaluation stage, IBRS evaluates the generated BPR alternative through simulation. The following is a way to utilize an IDEF0 model in simulation to obtain statistics such as service time and resource utilization [10].

1. Create an IDEF0 model.

2. Output model to a Petri-net model.

3. Run work flow analysis generator.

4. Save executable model.

5. Modify default input files created by the work flow analysis generator.

6. Run the model and analyze results.

7. Change input and repeat step 6.

IBRS represents the above procedure as a set of rules in the knowledge base. Currently, the Petri-net model is in the form of a file. Since the Petri-net model is similar to rule-based representation, a Petri-net model can be transformed into a set of rules for an effective integration in the model base. By making the rule-based simulation possible, IBRS facilitates the natural integration of rule-based knowledge and process models.

In addition to work flow statistics, net present values for upcoming periods can be obtained from a spreadsheet-based functional economic analysis model [4].

While the purpose of the generation stage is to roughly cut out the decision alternatives, the purpose of the evaluation stage is to derive more detailed information about each BPR alternative generated. Simulation assists in predicting the state of the system when it is redesigned according to the generated BPR alternative.

## 2.3. Choice

Through a multi-attribute criteria decision analysis, the best BPR alternative is chosen based on various performance statistics obtained in the evaluation stage. This decision making procedure is represented as rules in the knowledge base of the IBRS-Planner. The types and weights of each decision parameter are obtained by interacting with the system user.

Table 1  
Process/performance matrix

<table><tr><td></td><td>Process</td><td>Performance</td><td>Reduce service time</td><td>Increase security</td><td>Increase customer base</td></tr><tr><td>P1</td><td colspan="2">Bank staff ID card service</td><td></td><td></td><td>●</td></tr><tr><td>P2</td><td colspan="2">Telephone card service</td><td></td><td></td><td>●</td></tr><tr><td>P3</td><td colspan="2">Health care card service</td><td></td><td></td><td>●</td></tr><tr><td>P4</td><td colspan="2">Home banking</td><td>●</td><td>●</td><td>●</td></tr><tr><td>P5</td><td colspan="2">Corporate banking</td><td>●</td><td>●</td><td>●</td></tr><tr><td>P6</td><td colspan="2">Interbank fund transfer</td><td></td><td>●</td><td></td></tr><tr><td>P7</td><td colspan="2">Student ID card service</td><td></td><td></td><td>●</td></tr><tr><td>P8</td><td colspan="2">Merchant store service</td><td>●</td><td></td><td>●</td></tr><tr><td>P9</td><td colspan="2">ATM service</td><td>●</td><td></td><td>●</td></tr></table>

After a cycle of evaluation and choice, it is possible to analyze the performance of some heuristic constraints used to prune decision alternatives. Based on this analysis, the refinement of the candidate-solution generation process can be made. This is accomplished by dynamically modifying, adding, or removing heuristic constraints in order to improve the CSP search.

IBRS stores the previous experiences of BPR recommendations and results. Once a bank chooses the best alternative, the Bank/BPR alternative matrix is stored into the IBRS model base. This provides an additional source of useful information vital to other banks with similar environments.

## 3. Scenario

This section presents a scenario of using IBRS to identify smart card banking opportunities. Fig. 2 shows the main screen of IBRS.

To overview smart card technology and previous smart card banking system projects, click “Smart Card Banking Cases” button. Using multimedia technology, representation of previous cases will be displayed. To review previous BPR processes, click “Process/Performance Matrix” button. Then, IBRS displays a Process/Performance (PP) Matrix screen (see Table 1).

Each process, when clicked, leads to the corresponding IDEF process model, which also provides activity based costing information. For example, when the Merchant Store Service process is clicked, IBRS shows two diagrams, Figs. 3 and 4. These two diagrams are only a part of the IDEF model for the Merchant Store Service process.

Fig. 3, the so-called context diagram, describes the environment of the Merchant Store Service process from the merchant store manager's point of view, not from the bank's viewpoint. The context diagram shows two inputs (IC Card and Password), one control (Blacklist of IC Cards), two outputs (IC Card and Electronic Fund Transfer Requests), and three mechanisms (Product DB, Electronic Fund Transfer/Point Of Sales Terminal, and Bank).

The activities performed in a merchant store in relation with the IC card consist of the IC card validation, transaction processing, request for Electronic Fund Transfer (EFT), and closing.

Fig. 4 shows these four activities with the costs of performing them – Activity Based Costing. For ex-

![](/api/attachments/KVYKDA2Q/fulltext/images/c540594750931e7c77d6adba639177b203a0b86c6ef0802e9094f95902ce477e.jpg)  
Fig. 2. Main screen of IBRS.

![](/api/attachments/KVYKDA2Q/fulltext/images/33efa8dd566c671c5c2e8faf51861e8847ab94027c2c18c30f0cc004b293879a.jpg)  
Purpose: Model the process of merchant store service for IBRS.  
View: Merchant store manager

Fig. 3. Context diagram.

ample, A1 represents that if the IC card a customer (cardholder) presents is not included in the blacklist, a salesperson would check the balance on the customer's account. This activity is performed off-line rather than on-line, i.e. without connection to any outside computer. The cost for performing A1 once is just \$0.5. In the old process, validating a credit card requires an on-line connection to the computer of a company which issues a permission number. This involves the cost of communication and the fee for credit check. The cost of each occurrence in the old process was about \$2. Therefore, the time and cost of performing A1 can be saved in the new process with the IC card in comparison with the old process without the IC card. The Merchant Store Service process contributes the goal of reducing service time. The cost of performing A1 is shown inside the lower left corner of the A1 box.

Similarly, the time and cost for performing A3 is much less than the time and cost in the old process. In the new process, use of an Electronic Fund Transfer/Point Of Sales (EFTPOS) terminal during A2 collects and stores all sales records in electronic form. There is no need for preparing documents for requesting fund transfer. Electronic sales record stored in the EFTPOS terminal are transmitted to the bank where customers' deposits are transferred to the merchant's account within a fixed time interval, for example, 10 minutes. Merchants can perform A3 as often as they want, but usually once a day after they close their store. In the old process, collecting money takes a few weeks and merchants request once or twice a month.

![](/api/attachments/KVYKDA2Q/fulltext/images/8bdfe96a4ee155a5d6c5aacca52a4eb760a423d23510c81824c3d3da9a390ff3.jpg)  
Fig. 4. Merchant Store Service process.

Then, to generate candidate BPR opportunities:

\- Click “Generate BPR Opportunities” button.

IBRS interacts with the user to analyze the current system and new system requirements, and to identify constraints of the bank. In the following scenario, the bank has three constraints: process priority, process dependency, and customer-base expansion goal. Constraints-Set-1 is a rule class of the three rule constraints, which are used to prune BPR alternatives during CSP search. IBRS also determines a priority list of the processes from the Process/Performance matrix according to their importance and urgency. In this example, the list is $(p_{8} p_{1} p_{7} p_{9} p_{5} p_{4} p_{6} p_{2} p_{3})$ .

After a process priority list is obtained, sequences of generation, evaluation, and choice rules are iteratively fired to finally choose a BPR alternative. The following shows a cycle of rule-based reasoning.

\- IBRS fires Generation-Rule-1 representing the budget constraint to find an initial process set, $\{p_{8}, p_{1}, p_{7}, p_{9}, p_{5}, p_{4}, p_{6}\}$ .

\- IBRS fires Generation-Rule-2 to start constraint satisfaction search, as shown in Fig. 6. To test the feasibility of candidate solutions during backtrack search, the following Generation-Rules 3, 4, 5, and 6 are used.

\- IBRS fires Generation-Rule-3 to check constraints in Constraints-Set-1 during CSP search.

\- IBRS fires Generation-Rule-4 to check the Process-Priority constraint.

\- IBRS fires Generation-Rule-5 to check the Process-Dependency constraint when the conditions of Generation-Rule-4 are met.

\- IBRS fires Generation-Rule-6 to check the Customer-Expansion-Goal constraint when the conditions of Generation-Rule-4 and 5 are met.

\- IBRS fires Evaluation-Rule-1 to start simulation.

Fig. 5. Heuristic rules.

```lisp
(FUNCTION CSP-Search (Solution-List)
(WHILE (solution-list empty)
(LET solution-list = rest in the solution-list)
(LET solution = first in the solution-list)
(IF (The solution is feasible using Constraints-Set-1)
IF (The solution is partial)
THEN (Extend the solution list and update it)
ELSEIF (The solution is full)
THEN (A feasible solution is found)
ENDIF)
ENDIF)
(CSP-Search Solution-list))
```  
Fig. 6. Constraint satisfaction search.

\- IBRS fires Choice-Rule-1 to find out the best solution so far.

After cycles of rule-based reasoning, $\{p8, p1, p7, p9\}$ is selected as the best BPR alternative; Merchant store service, Bank staff ID card service, Student card service, and ATM service constitute the chosen alternative. The description of rules and CSP search used above are shown in Figs. 5 and 6.

## 4. Summary

IBRS demonstrates an expert system approach to BPR. IBRS generates and evaluates BPR opportunities in an integrated fashion. The knowledge base of BPR cases can be continuously expanded to enrich the applicability of this system. The current knowledge base focuses on the smart card banking technology and opportunities based on accumulated experiences of the smart card banking system projects by DongSung Inforcomm (DSI).

The function of IBRS needs to be extended to cover the IBRS-Constructor, to help construct a new business information system. Resulting analysis of IBRS can be used to define and develop a work flow management system. The work flow automation based on in-depth analysis can enhance communication, cooperation, and collaboration, in addition to improved productivity and efficiency.

Currently, process models are represented in the form of files. Relational data base management methodology can be applied to process model base (repository) management. In order to store processes in the model base and share them among various users effectively, the names and attributes of processes need to be standardized. Costs and benefits from standardization should be weighed carefully.

Methodology to facilitate decomposition and integration of process models needs to be further developed.

IBRS is an evolving system. IBRS provides a framework in which we can put more models and knowledge as we acquire them to facilitate BPR in the expanded target domain.

## References

[1] T.H. Davenport and J.E. Short, The New Industrial Engineering Information Technology and Business Process Redesign, Sloan Management Review (Summer 1990).

[2] R. Dechter and J. Pearl, Network-Based Heuristics for Constraint Satisfaction Problems, Artificial Intelligence 34 (1988) 1–38.

[3] DSI, Analysis and Design of a Smart Card Banking System for KwangJu Bank (DongSung Inforcomm, 1993).

[4] IDA, User's Manual for the Functional Economic Analysis Model (Institute for Defense Analyses, 1991).

[5] W.C. Kim and J.D. Foley, Providing High-Level Control and Expert Assistance in the User Interface Presentation Design. INTERCHI'93 – Conference on Human Factors in Computing Systems (Amsterdam, The Netherlands, April 1993).

[6] Meta Software, Design/IDEF 3.0 Tutorial for Microsoft Windows (Meta Software Corporation, Cambridge, 1994).

[7] D.M. Min, A Knowledge-Based Hybrid Modeling Approach to Planning Problems in Flexible Manufacturing Systems. Ph.D. Thesis (University of Michigan, Ann Arbor, Michigan, 1990).

[8] D.M. Min, T. Schriber and K. Stecke, KIMS: Knowledge-Based Integrated Manufacturing System, Flexible Automation and Information Management (CRC Press, Inc., 1992).

[9] B.A. Nadel, Tree Search and Arc Consistency in Constraint Satisfaction Algorithms, in: L. Kanal and V. Kumar (Eds.) (Springer-Verlag, 1988).

[10] V. Pinci and R.M. Shapiro, Work Flow Analysis (Meta Software Corporation, Cambridge, 1993).

[11] D. Rasmus, Redesigning the Corporation with IDEF's Help. Manufacturing Systems (Hitchcock Publishing Company, December 1988).

[12] D.T. Ross, Structured Analysis: A Language for Communicating Ideas, IEEE Transactions on Software Engineering SE-3, No. 1 (January 1977) 16–34.

[13] D.L. Schnitt, Reengineering the Organization Using Information Technology, Journal of Systems Management (January 1993) 14–20, 41–42.

[14] K.E. Stecke, M. Min and I. Kim, A Hybrid Model-Based Approach for the Production Planning of FMSs, Proceedings of the Third International Conference: Expert Systems and the Leading Edge in Production and Operations Management (May 1989) 281–291.

![](/api/attachments/KVYKDA2Q/fulltext/images/8957fe9a02e2da6994b5da899df7f5c724bbe9eb440c071205909ee9e055a64d.jpg)

Daniel Moonkee Min is the president of DSI, Inc. He holds a Ph.D. from the University of Michigan, Ann Arbor. His company has been developing banking applications using smart card technology. His research interests include business reengineering, expert systems, and computer integrated manufacturing.

![](/api/attachments/KVYKDA2Q/fulltext/images/3c0dfdbf027255b22f17ee43b7c69ca005b8a8d52e8ead829c475700cb1208fe.jpg)

Daihwan Min is assistant professor of Management Information Systems at Korea University. He holds a Ph.D. from the University of Michigan, Ann Arbor. His research interests include systems analysis and design, business reengineering, human-computer interface, and expert systems.

![](/api/attachments/KVYKDA2Q/fulltext/images/371d55fee65f3cf084e18371137bdc3bdcf3ba41eaafa56801a623001624ed59.jpg)

Jong Ryul Kim is director of DSI, Inc. He holds a Ph.D. from the Korea Advanced Institute of Science and Technology. Previously, he worked for the National Institute of Health, USA. His research interests include neural network, molecular graphics, image processing, and smart card applications.

![](/api/attachments/KVYKDA2Q/fulltext/images/a31848a1275a9df552ea18bebd3d103f8782223edfb0e86788ad8b0a61bf4f6f.jpg)

![](/api/attachments/KVYKDA2Q/fulltext/images/ddceba67cd6cedbd5efeecd8e0bc01afb342f7d2176ae0ae8dddfaad6284fb61.jpg)

Won Chul Kim is a member of the research and development group at DongSung Inforcomm and a member of the Strategic Technology Group in the International Monetary Fund. His research interests include user-computer interfaces, computer graphics, workflow automation, information management systems, document management systems, image management systems, and knowledge base systems. He has developed high-level expert user interface de-

Steve Ku is a principal scientist at the Battele Memorial Institute. His current research interests include development of automated planning system, evaluation of decision support systems, application of artificial intelligence in software engineering, expert systems with learning capabilities, and knowledge acquisition and inference strategies for information fusion. He received a Ph.D. from the George Washington University. He is a member of IEEE Computer Society, ACM, and AAAI.

sign tools based on the knowledge-based framework, and designed and implemented task coordination tools based on the workflow, imaging, and document management software. He received a Ph.D. in Software and Artificial Intelligence from the George Washington University in 1993. His research focus was User Interface Design and applications of expert systems and knowledge base systems.
