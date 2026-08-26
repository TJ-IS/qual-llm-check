---
otero_id: 17052
otero_key: "4T8KHCJ2"
title: "An expert decision support system for production control"
authors: "Gautam Biswas; Michael Oliff; Arun Sen"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90132-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Expert Decision Support System for Production Control

Gautam BISWAS \*, Michael OLIFF \* and Arun SEN \*\*

\* University of South Carolina, Columbia, SC 29208, USA

\*\* Texas A&M University, College Station, TX 77843-4217, USA

The most crucial resource in manufacturing and production is human expertise. Unfortunately it is often the most costly to acquire. Corporate consulting fees and management training expenses testify to this end. Recent advances in artificial intelligence, decision support, and information processing offer a potential solution to this scarcity. The development of expert decision support systems in the production domain may prove to be the productivity theme of the decade. We present OASES (Operations AnalySis Expert System), designed using the XDSS framework proposed in $[10]$ to emulate a consultant and aid management in troubleshooting manufacturing processes.

Keywords: Knowledge Based Systems, Decision Support Systems, Operations Analysis, Inexact Reasoning, Dempster Shafer Theory, Production Process, Diagnostic Problem Solving.

![](/api/attachments/4T8KHCJ2/fulltext/images/f20b444e617d9ca95efc5406a10a8026643be4b6fa859b10af746cbb26b54008.jpg)  
formation Retrieval.

Gautam Biswas is an Assistant Professor of Computer Science at the University of South Carolina. He received a B.Tech. degree in Electrical Engineering from the Indian Institute of Technology, Bombay, India, in 1977, and M.S. and Ph.D. degrees in Computer Science from Michigan State University, East Lansing, in 1979 and 1982, respectively. His primary research interests are in Artificial Intelligence, Knowledge Based Systems, Inexact and Default Reasoning, and In-

He spent the summer of 1984 at the AT&T Bell Labs in Holmdel, N.J., working on an expert systems project with the CMS-1 Systems Engineering group. He is currently working on knowledge based system applications in areas such as operations analysis, active assistance interfaces, information retrieval, and oil exploration.

Dr. Biswas has published in a number of journals, such as the IEEE Trans. on Pattern Analysis and Machine Intelligence, IEEE Transactions on Systems, Man, and Cybernetics, Intl. Journal of Man Machine Studies, and the Journal of the American Society of Information Sciences. He is an associate editor of the International Journal of Approximate Reasoning, and a member of the IEEE Computer Society, ACM, AAAI, and the Sigma Xi Research Society.

## 1. Introduction

Recent advances in artificial intelligence techniques have led to its application in many real world settings. Notable strides have been made in applications of expert systems to medical diagnosis, signal analysis, machine failure analysis, geology and chemical data interpretation [2]. Researchers are attempting to extend these accomplishments into other domains to enhance produc-

![](/api/attachments/4T8KHCJ2/fulltext/images/8a24c8cf4bf962d2dfcdd861cec4c6989fbee719c8a7c0710d944195473cf27f.jpg)

Michael D. Oliff is currently a Research Fellow and Graduate Faculty Member of Management Science at the University of South Carolina, Columbia. He has degrees in mathematics, computer science and operations management, and has published applied research in leading professional journals including: IEEE Transactions, Decision Sciences, Decision Support Systems, IEEE Transactions on Systems, Man, and Cybernetics, and Production and Inventory

Management. He received his Ph.D. from Clemson University.

Dr. Oliff is Program Chairman for the Second International Conference on Expert Systems and the Leading Edge in Production Planning, co-sponsored by the Operations Management Association, and the American Association for Artificial Intelligence, to be held in Charleston, S.C. in May 1988.

Dr. Oliff has served as Milliken and Company's manager for Corporate Operations Research. He has experience in Task Force administration from advisory and management perspectives. He has been retained by Owens Corning Fiberglass since 1981 as a planning consultant and is also retained by NCR Corporation.

![](/api/attachments/4T8KHCJ2/fulltext/images/6c157dde5ec0530971067a898c6f6362716fb98baad157f1991b7b58b6f4e456.jpg)

Arun Sen is an Associate Professor in the Department of Business Analysis and Research, College of Business Administration, Texas A&M University. Prior to joining the faculty at Texas A&M, he was a faculty member in the Management Science department in University of South Carolina at Columbia.

His research interests include Data Base Management Systems, Deductive Data Bases, Decision Support Systems, Business Expert Systems, Distributed Processing, EDP Auditing, Information Resource Management, End User Computing, and Application of OR techniques in Information Systems. He has published in numerous journals including Information Systems, Information Science, Computers and OR, MIS Quarterly, Decision Support Systems, Information and Management and Data and Knowledge Engineering.

Dr. Sen is a member of Decision Sciences Institute, The Institute of Management Science, Association of Computing Machinery and its special groups SIGMOD, SIGBDP, and SIGART.

tivity. There is evidence that they can greatly enhance the capability of management support systems in the business domain [6,8].

Problem solving and decision making in the business domain is complex and relatively unstructured. In [7] Oliff includes eight examples of artificial intelligence applications in manufacturing along with eight written by noted domain experts that addresses different issues in the domain. These authors illustrate, among other things, that few experts agree on specific 'best' approaches to decision making and problem solving within the domain itself. There are often multiple, if not conflicting objectives that must be considered well before models are even formulated. Expert or knowledge based systems are simply application programs that emulate human experts in specialized domains. Their ability to solve complex problems is based on the creation of a comprehensive knowledge base that includes relevant facts and heuristics developed by experts in the given domain. Heuristics provide these systems with a feasible tool for semi-structured and unstructured decision making in the business domain [10]. Significant characteristics of knowledge based systems that differentiate them from conventional programs are their emphasis on symbolic rather than numerical manipulation, a clear separation of the knowledge base and the reasoning mechanisms, and the ability of the system to explain its reasoning mechanism in a natural and transparent manner.

Decision Support Systems (DSS) allow non-technical users easy access to analytic and data management tools [1,4]. In addition, they integrate these tools with report generators and graphic routines to produce output in a form that non-technical users can easily relate to. Therefore, these systems alleviate difficulties present day management face in using analytic tools and computer programs for decision making. Sen and Biswas [10] proposed an expert DSS (XDSS) framework to extend the capabilities of traditional DSS systems and make them more intelligent and user-friendly. Enhanced capabilities of this framework were obtained by integrating knowledge based, semantic data modeling, and advanced data base techniques with traditional DSS components.

Given the current state of the art in knowledge based systems, the design and implementation of a general XDSS to handle a wide variety of problem domains infeasible. However, expert system technology has been successfully applied to difficult and complex problems in narrow domains of expertise [2,7]. In this paper we apply the XDSS framework to the operations analysis domain in manufacturing. OASES (Operations Analysis Expert System) is designed to deal with problems specifically in the steady state phase of manufacturing processes such as automobile assembly or fiberglass production.

The current scope of OASES spans the problem acquisition and problem understanding phases of a general XDSS. It is designed to play the role of an intelligent assistant to management and aid them in diagnosing problems. The diagnosis (the problem acquisition and understanding phase) in OASES is divided into two parts: general cause analysis and specific cause analysis. Choice analysis follows cause analysis, and basically corresponds to problem analysis, integrated instance generation and instance execution in the XDSS framework. Choice analysis has not been incorporated into the OASES framework.

Section 2 describes the operations domain and the knowledge engineering process in that domain. Section 3 presents the framework and architecture of OASES, an expert system for cause analysis. Section 4 discusses implementation details and Section 5 presents the summary and conclusions of our research.

## 2. The Production Control Domain

Within the Operations Management domain, managerial activities entail selecting, designing, operating, controlling and updating a production system [3]. These activities span the life cycle of the production system as illustrated in fig. 1. At the onset a product or service is proposed. This product or service is examined to determine various factors, including marketability, profitability and technical requirements. If a decision is made to produce the good or service, then the final form of the production facility, the building, floor layouts, etc., are each specified. Equipment is purchased and the production, inventory and quality control systems are determined. The required processing and delivery tasks are designed, the functional groups are manned and production is initiated. There are often problems in the startup phase which require design changes, changes in layout or adjustments in personnel. However, after the startup phase is complete, day to day problems still occur in the form of losses in efficiency, off quality, process bottlenecks, and a host of other recurring ailments. This phase of the life cycle is identified as the steady state phase of the system. The steady state operating conditions may be perturbed in a number of ways: new products and services are offered; new developments and changes in technology render current methods obsolete; existing equipment fails, markets shift, and so on. If the system cannot adjust to these stimuli, the enterprise declines and ultimately ceases to exist.

![](/api/attachments/4T8KHCJ2/fulltext/images/6115c8efa31a38733ee0cb18ca3291de5d0fa18d3e5ec6b92877d72e34886566.jpg)  
Fig. 1. The operations analysis domain.

Production managers are constantly involved in planning and decision making even in the steady state phase. Problems arise from sources that are both internal and external to the system. Sources within the production system include the production process itself, personnel, and control systems. Sources external to the system include corporate policy, other functional areas of the firm, suppliers, unions, competitors and customers.

The domain of production control spans the steady state level discussed above. The possibility of many sources of malfunction raises the need to continually monitor, evaluate and adjust system performance to ensure that desired goals are met. For the management staff this implies five primary tasks: sensing, comparing, analyzing, decision making and corrective action. Sensing involves data gathering to determine the status of the system. The comparison process involves matching operating data to predetermined standards of performance. Analysis determines the cause of the malfunction. Decision making involves choosing the appropriate corrective action from among some specified set of alternatives. Corrective action implements the adjustment decision and may be composed of single or multiple actions.

The complexity of problems in production control tends to emphasize the need for either in-house consultants or external experts. These consultants, often experienced executives, initially familiarize themselves with the process where the problem has been observed. The next step involves identifying and characterizing the problem, and gathering data that can be used to determine appropriate solutions. The last step often involves the use of analytic tools such as linear programming, integer programming, simulation, or statistical modeling tools, to analyze and solve the problem.

The human expert for the project is a member of the graduate faculty of a major university and is also a retained production planning consultant for several Fortune 500 companies. He has previous experience as corporate manager of operations research in a 2.5 billion dollar company. The following section sketches his method for cause analysis, a technique he has developed over a number of years as a production control consultant.

## 2.1. The Expert's Approach

The opportunities for improving performance within steady state operations arise in two very general contexts. First, the perturbations that occur and their root causes must be efficiently identified. In other instances, actual alternatives (choices) for improved performance present themselves via new technologies or methods, and decisions must be made. In group settings, such as manufacturing meetings, corrective action meetings, or quality improvement meetings, these opportunities are often ignored or confused.

Problem solving meetings often break down as alternative actions are discussed before the true cause of the problem has been established. Favorite causes and associated corrective actions are discussed and then championed often without focusing on the ‘problem’ itself. Recognizing this and related dysfunctional behavior in decision making as well, a systematic approach to cause analysis and choice analysis is imperative in any quest for true performance improvement.

Frequently external consultants are called in to analyze problems and operations. These people are presented initially with a general description of the problem by management and then, by probing and analysis, they are able to identify specific causes and recommend corrective techniques. Management must then be convinced of the validity of the analysis and the corrective actions that are suggested. The experts' abilities to efficiently identify the correct primary cause for observed problems, and to subsequently present effective corrective measures is the basis for their title and livelihood. Their final reports usually describe the line of reasoning that led to the discovery of specific causes for existing problems, followed by a list of possible corrective actions and/or techniques to resolve them.

An expert's reasoning process can be divided into two distinct yet related phases: cause analysis, and choice analysis. The cause analysis phase involves a study of the characteristics of the processes and/or products involved and the changes observed in these processes/products. The goal of cause analysis is simply to isolate the primary cause or causes for a problem. Once specific causes are identified, choice analysis involves selecting objectives and criteria, gathering further data, analyzing alternatives and recommending specific actions to eliminate the causes or alleviate their effects. This may involve analytic tools (such as simulation, regression, and operations research models), heuristics, or a combination of heuristic rules and analytic methods, as suggested by experts. Cause analysis and choice analysis are distinct processes; the data requirements and evidence gathering processes in the two phases are quite different. The focus of this paper is on the cause analysis phase of the reasoning process, itself consisting of a two step approach.

## 2.2. General Cause Analysis

In general cause analysis, the objective is to determine the general cause or set of causes that best match the observed symptoms described by the user. To understand the expert's reasoning process we must discuss the inherent knowledge he/she possesses. A typical expert in production/operations management has an in-depth understanding of different manufacturing processes. These process types can be classified into continuous flow, batch flow, machine-paced or worker-paced assembly line, job shop and hybrid processes [9]. Each of these processes demonstrate unique patterns that involve product features, process characteristics, inventory features, information-oriented features, labor-oriented features and management features. Within the operations domain, these patterns often imply or give rise to certain problems. For example, raw material sourcing is a common challenge in continuous flow environments, while shifting bottlenecks and scheduling are often the main concerns of job shop management. From experience, the expert also accumulates a list of causes that relate to observed symptoms and process characteristics. Problems, defined as observed deviations from a norm, manifest themselves in the form of symptoms such as changes in efficiency or effectiveness, reductions in quality, etc. This judgemental knowledge used by the expert forms the core of his reasoning process in general cause analysis.

Establishing general cause categories enables the expert and management staff to quickly focus on a broad problem area and then obtain specific evidence directly related to the problem at hand. This process begins with the identification of the process type involved, often obvious from the user's initial problem statement. For example, if the product is steel, paper, fiberglass, etc. the underlying process is often a flow manufacturing process or some type of hybrid. On the other hand, if the product is automobiles, it is likely that a machine paced flow process is involved. Similarly, industrial machinery typically implies either a job shop or a worker paced process.

Characteristics that are used to derive the process type include the type of processing layout (e.g., unstructured, partially structured, rigidly structured), and the key factors that influence output yield (e.g., workers, machines, raw materials). Once the process type is isolated, the expert seeks further evidence to establish the general cause (or causes). Fifteen general cause categories were listed by the expert.

The expert begins his diagnosis with basic questions regarding both the product/process and the symptoms observed: What, Where, When and How much? Typical queries are 'When have you observed the problem?', 'What percentage of your process is affected?' and 'Describe some of the symptoms that you have observed, i.e., changes in efficiency, service level, costs, quality, etc.'

This information enables the expert to select a subset of general cause categories for detailed examination. The expert uses heuristics, based on process types, to tie observed symptoms to general cause categories. For example, if the expert deduces an assembly line process (e.g., automotive, computer) 'excess capacity early' or 'insufficient capacity late' in the process indicates that 'process design' is a likely cause category. On the other hand if a jobshop process (e.g., a machine shop) is involved, 'missed due dates' suggests scheduling conflicts, bottlenecks or deficient information flows.

## 2.3. Specific Cause Analysis

The second step in the expert's reasoning process, specific cause analysis, is not only tied to the type of production process under consideration (e.g., textiles, fiberglass, machine tools, automobiles) but also to the most likely cause category derived by general cause analysis. The aim now is to gather much more refined and relevant evidence than was previously possible. For each type of general cause category, using knowledge of the process itself, the expert can begin to ask highly technical, cause specific questions. Unsolicited, ambiguous and incomplete data can be interspersed with a higher degree of confidence here as well. With directed probing, the expert elicits sufficient evidence (symptoms), and then selects a specific cause that ‘best explains the effect’. A matching and elimination process is employed to make the case for certain causes and rule out others entirely. If insufficient evidence exists, and a ‘best cause’ cannot be determined the expert returns to general cause analysis or shifts gears entirely to choice analysis.

The importance of general cause analysis can be readily seen. If the initial ‘high level’ cause category is incorrect, a substantial amount of time will be wasted searching or focusing on the wrong model (or the wrong part of a model), and may ultimately require backtracking to the general cause analysis phase. This makes it important to have a method that will transition from general to specific cause analysis only when there is sufficient information available to make an appropriate decision. Once a specific cause or set of causes is known one can decide on the best possible schemes to solve the problem.

## 3. Architecture of the Expert System

As emphasized earlier, the expert system for cause analysis plays the role of an intelligent assistant or a consultant to management in a production process. A successful expert system in this scenario should necessarily: (i) be interactive and user-friendly, (ii) use evidential reasoning, and (iii) allow inexact reasoning. The main components of the expert system are illustrated in fig. 2. The front-end uses a simple natural language processor to interact with the user. The query selector component directs the user-system dialogue by selecting relevant questions from a large database of stored queries. A directed question-answer technique makes the evidence gathering process efficient; the system avoids annoying the user with too many irrelevant or redundant queries. The system also adopts a mixed-initiative format of interaction so that user responses are not restricted to the context of the system query; the language processor is flexible enough to accept additional process information and not limit users to specific responses. Thus users can shift focus by providing information on other aspects of the problem that are not connected to the query. The third component of the front-end is a help mechanism, where the system displays a list of meaningful responses when users express their inability to understand queries.

Relations between process characteristics, problem symptoms, and cause categories based on the expert's judgemental knowledge are expressed as production rules and compiled into a partitioned rule base. Individual partitions contain expert rules based on one of several process types. This structure mirrors the expert's reasoning process and makes the directed dialogue and inferencing scheme easier to implement. An expert supplied rule links a pattern on its left hand side (LHS) to one or more conclusions on its right hand side (RHS). To accommodate uncertainty in the rule structure, expert supplied belief values are associated with conclusions on the RHS. These belief functions are modeled as basic probability assignments in the Dempster Shafer framework [11], and are described in greater detail in the next section. Examples of several OASES rules appear in fig. 3.

![](/api/attachments/4T8KHCJ2/fulltext/images/277a5b1246335e9022d0a4447726676d499eb5ebe0bca385a852fa3fc007cc7d.jpg)  
Fig. 2. System architecture.

The overall inferencing mechanism has four main components: the evidence combination mechanism, the procedure for selecting the top ranked hypothesis, the query selection mechanism that directs the user-system dialogue based on the top ranked hypothesis, and a top level controller for selection of partitions within the rule base.

Based on evidence obtained, the system ranks conclusions or hypotheses, and selects a query whose response is likely to support the top ranked hypothesis. Dempster's combination formula [11] is used to update belief values of the hypotheses based on evidence provided by the user. The system continues in this backward chaining mode until a final conclusion is established. However, if at any time users consider the current query to be irrelevant they may provide additional facts and other evidence. This causes the system to switch to the forward chaining mode, and deduce new conclusions, possibly establish a new top ranked hypothesis, and then switch back to the backward chaining mode.

## 4. The Implementation

The interaction between a user and the system is presented in the appendix. The front-end (rule001 [ (process type) (continuous flow) ] -->
[ (raw material sourcing) 0.25 ]
[ (process design) 0.25 ]
[ (technology) 0.17 ]
[ (maintenance) 0.13 ] )

(rule014 [ (process affected) (entire) ] -->
[ [ (raw material sourcing) 0.2 ]
[ (process design) 0.15 ]
[ (technology) 0.15 ]
[ (capacity planning) 0.1 ] })

(rule034 [(trouble occurs) (shifts 1 and 2)] -->
{ [(raw material sourcing) 0.25]
[(maintenance) 0.25] }

rules in continuous flow partition

(rule066 [ (raw material characteristics) (changed)] -->

{ [(raw material sourcing) 0.8] })

(rule067 [(process formula) (changed)] -->

[ [(raw material sourcing) 0.6]
[(process design,technology,maintenance) 0.2] })

rule in machine paced partition:

(rule078 [ (efficiency problem) (new or shifted bottleneck)] --> { [(process design) 0.8] })

Fig. 3. Sample rules from knowledge base.

processor first queries the user regarding the nature of the product(s)/process(es) involved and the changes in performance that have been observed. The processor uses a combination of augmented transition tree grammar and simple pattern matching techniques to interpret full statements of phrases. A mention of steel, fiberglass, automobiles, or printed circuit boards enables the system to draw preliminary conclusions about the type of process involved.

It may turn out that the user, in an opening statement, fails to provide sufficient information from which process characteristics and product types can be inferred. The system then provides specific queries from which it infers process and product characteristics. These characteristics are crucial in the expert's reasoning process. Sample responses to a query are provided via a help feature. This latter feature not only aids a user in query responses but also provides the expert with a simple debugging tool.

Once information regarding process characteristics has been acquired the system queries the user about observed symptoms and changes. The aim is to elicit general symptoms and establish a most likely general cause for the problem observed. Identification of a general cause, as a first step, enables the expert to efficiently focus on a specific line of reasoning and gather more detailed and refined information so that a specific cause that ‘best explains the observed effects’ can be derived. This directed probing is illustrated in the second part of the consultation in the appendix. The system uses the general cause derived earlier and the nature of the product and process to derive a specific raw material sourcing problem in the fiberglass manufacture process.

As discussed earlier, a directed questioning scheme controls the user-system dialogue. The system attempts to extract from the user those pieces of evidence that lend most support to the top ranked cause. The objective is to determine the most likely cause in the minimum amount of time using the fewest questions possible. The most likely cause is defined in terms of belief values. The overall control strategy adopted for the cause analysis phase of OASES reflects important aspects of the expert's diagnostic process. First, the expert perceives certain pieces of evidence to be more important than others. This evidence must be obtained in the early stage of the interaction. If the expert is unable to obtain it directly, he attempts to derive it indirectly by soliciting other related information. In this dialogue the system, like the human expert, judges when it has sufficient information to either confirm a certain piece of evidence or repudiate it. The Dempster Shafer belief values play an important role in this decision-making process. The accumulation of evidence directs the expert's search for other evidence; his goal is to come to a conclusion in the quickest possible manner while keeping the number of queries to a minimum.

The inferencing mechanism is implemented to maintain one active partition at a given time. Partitions in OASES are hierarchical in nature. The topmost partition contains general rules dealing with symptoms that are basically process independent. At the next level there are several partitions corresponding to general cause analysis for specific process types. Below this level we have partitions that deal with specific cause analysis for a specific process and general cause. The OASES consultant follows this hierarchical path, and eventually leads to the determination of a specific cause for an observed problem.

The Dempster Shafer method is used for combination of evidence in the presence of uncertainty. The main advantage of this scheme over traditional Bayesian [12] and other adhoc schemes [2], are it's ability to

(i) explicitly represents the concept of ignorance in the decision making process,

(ii) allow evidence to provide support for sets of hypotheses as opposed to singletons and

(iii) model the narrowing of the hypothesis set with the accumulation of evidence.

This method provides a flexible framework for modeling the human expert's reasoning process. Belief functions and the evidence combination scheme are well suited to represent the incremental accumulation of evidence and the results of its aggregation. Before explaining the rule formulation process, we formally define belief functions, and briefly present the mathematical formulation of the evidence combination scheme.

This discussion follows the notation used in Shafer [11] and Gordon & Shortliffe [5]. The Dempster Shafer formulation is based on a frame of discernment, $\Theta$ , a set of propositions or hypotheses about the exclusive and exhaustive possibilities in the domain under consideration. For example, the fifteen general cause categories form a frame of discernment in OASES. The notation $2^{\Theta}$ is used to denote the set of all subsets of $\Theta$ . Further discussion is based on two concepts that can be adopted for the representation of impact of evidence on judgemental conclusions: the measure of belief committed exactly to a subset $A$ of $\Theta$ (i.e., $A \in 2^{\Theta}$ ) and the total belief committed to $A$ . Exact belief relates to the situation where an observed evidence implies the subset of hypotheses, but this evidence does not provide any further discriminating evidence between individual hypotheses in $A$ . A function $m: 2^{\Theta} \to [0, 1]$ is called a basic probability assignment (bpa) whenever

$$
m (\Phi) = 0, \quad \text { and }\tag{1a}
$$

$$
\sum_ {A \subseteq \Theta} m (A) \leqslant 1,\tag{1b}
$$

where $2^{\Theta}$ is the set of all subsets of $\Theta$ . The quantity $m(A)$ represents the measure of belief that is committed exactly to A, e.g., the bpa represents the support each piece of evidence provides to subsets of $\Theta$ . Condition (1a) reflects the fact that no belief should be committed to $\Phi$ , the null hypothesis, while (1b) state the convention that one's total belief must be less than or equal to one. The measure of total belief committed to a subset A is defined as

$$
B e l (A) = \sum_ {B \subseteq A} m (B),\tag{2}
$$

where the summation is conducted over all B that are subsets of A. A function $Bel: 2^{\Theta} \to [0, 1]$ is called a belief function of $\Theta$ , if it is given by (2) for some basic probability assignment m. If (1b) sums to less than 1, then $(1 - \sum_{A \subset \Theta} m(A))$ defines a measure of ignorance, denoted by $m(\Theta)$ . $m(\Theta)$ then is the extent to which the observations provide no discriminating evidence among the hypothesis within the frame of discernment $\Theta$ .

Judgemental rules provided by experts represent individual pieces of evidence that imply subsets of hypothesis from $\Theta$ with belief values that correspond to measures of exact belief (fig. 3). Corresponding to two different pieces of evidence $e_{1}$ and $e_{2}$ with bpa's $m_{1}$ and $m_{2}$ , respectively (i.e., two different OASES rules), over the same frame of discernment, Dempster's rule of orthogonal products is applied to combine the effects of observing the two pieces of evidence and compute a new bpa, m, that is given by

$$
m \left(C _ {k}\right) = \frac {\sum_ {A _ {i} \cap B _ {j} = C _ {k}} m _ {1} \left(A _ {i}\right) m _ {2} \left(B _ {j}\right)}{1 - \sum_ {A _ {j} \cap B _ {j} = \emptyset} m _ {1} \left(A _ {i}\right) m _ {2} \left(B _ {j}\right)}.\tag{3}
$$

$A_{i}$ represents hypotheses subsets that are supported by $e_{1}$ , $B_{j}$ represents hypotheses subsets supported by $e_{2}$ , and $C_{k}$ represents the hypotheses subsets that are supported by the observation of both $e_{1}$ and $e_{2}$ . The denominator is a normalizing factor to ensure that no belief is committed to the null hypothesis (condition 1a). For example, given that the current exact belief function is as follows: $m(h_{1} = \text{raw material sourcing}) = 0.544$ , $m(h_{2} = \text{process design}) = 0.238$ , and $m(h_{3} = \text{technology}) = 0.155$ , and the system obtains in response to a query that physical properties of some important raw materials have changed, rule 066 is applied, and the new belief function is computed using eq. (3) as shown in the table.

<table><tr><td>m</td><td> $h_{1}$ </td><td> $h_{2}$ </td><td> $h_{3}$ </td><td> $\Theta$ </td></tr><tr><td>rule066</td><td>(0.544)</td><td>(0.238)</td><td>(0.155)</td><td>(0.06)</td></tr><tr><td> $h_{1}$  (0.80)</td><td> $h_{1}$  (0.435)</td><td> $\Phi$  (0.19)</td><td> $\Phi$  (0.124)</td><td> $h_{1}$  (0.048)</td></tr><tr><td> $\Theta$  (0.2)</td><td> $h_{1}$  (0.109)</td><td> $h_{2}$  (0.048)</td><td> $h_{3}$  (0.031)</td><td> $\Theta$  (0.012)</td></tr></table>

$\Phi$ represents the null set. The new bpa function, m is $m(h_{1} = \text{raw material sourcing}) = 0.863$ , $m(h_{2} = \text{process design}) = 0.067$ , and $m(h_{3} = \text{technology}) = 0.045$ . The narrowing of the conclusions as evidence is accumulated is clearly evident in the above computation. More detailed discussions on the Dempster Shafer theory of evidence combination appears in [5,11].

Another important aspect in the development of OASES is the acquisition of judgemental rules from the expert in the Dempster Shafer framework. From fig. 3 it is quite apparent that the basic format of a rule is

$$
\begin{array}{r l} \{\langle \text { attribute } \rangle \langle \text { value } \rangle \} & \Rightarrow \left\{\left[ (c a u s e _ {j}) (b f _ {i}) \right] \right. \\ & \left. \left[ (c a u s e _ {j}) (b f _ {j}) \right] \right. \\ & \left. \left[ (c a u s e _ {k}) (b f _ {k}) \right] \right\}, \end{array}
$$

where the attribute of the pattern on the left hand side is a process parameter or characteristic, a product characterization, or a problem symptom description. For example, the three patterns [(process type)(continuous flow)], [(process input)(mixed)], [(process layout)(unstructured)], refer to process parameters or characteristics, [(product type)(steel)] is an example of a product characterization, whereas [(problem occurrence) (all days of week)] is an example of a problem symptom description.

Cause in the rule refers to general cause categories such as bottlenecks, capacity planning, maintenance, process design, or raw material sourcing, specific causes such as contamination and bin level maintenance, or even sets of causes. $bf_{i}$ 's are numbers that refer to the expert's confidence, or degree of belief in the relationship between cause categories and the pattern.

A standardized format was used to expedite rule formulation (see fig. 4). The first step involves obtaining an evidence and its related diagnostic conclusions. For example, when dealing with worker or machine paced assembly lines, the expert provides the following conclusions, given an efficiency problem, for the evidence machinery speed and size are in good balance (i.e., <machinery speed and size><good balance>):

1. Known process type:

2. Evidence(s):

3. Hypotheses and Corresponding Belief Rankings (on a scale of 0-10) (One set per line):

4. Importance or Relevance of this evidence in making Decisive Conclusions (scale of 0-10):

5. How to Query User for this Evidence (list Questions):

6. Expected user responses (patterns and synonyms):

7. Alternate Queries for Evidence:

Fig. 4. Standard form for rule acquisition.

likely causes are materials management, workforce, capacity planning, and process design.

Next these conclusions are grouped into subsets, based on the expert's observation that the given evidence does not really distinguish between the individual causes. In this case the expert separates the causes into two subsets:

(materials management, workforce), and

(capacity planning, process design).

Then the expert ranks the conclusions on a scale of 0–10, giving a relative ranking of 9 to the first subset, and a relative ranking of 3 to the second. Note that the values provided are not absolute support or belief values, rather the expert merely provides a relative ranking based on his judgement.

The last step in the rule formation is to explicitly obtain a measure of ignorance for the particular evidence. This is done by determining the expert's belief in the relevance (importance) of the evidence, i.e., given that he will be providing other evidence for making conclusions in this frame of discernment, on a scale of 0–10, how much does the evidence contribute to a definite conclusion? In this case, the expert's reply of 8, is translated to a $m(\Theta)$ value of 0.2(1 – 8/10) for this particular rule. The relative rankings supplied by the expert are then normalized to yield the exact belief function for this rule:

[(machinery speed and size)(in good balance)] $\Rightarrow$

[(materials management, workforce) 0.6]

[(process design, capacity planning) 0.2].

The above knowledge acquisition scheme proved to be a useful framework for fine tuning rules as well as for system validation. A number of different case studies were run, and at each step, the system's results were compared to the expert's expectations on two counts:

(i) Given the evidence accumulated so far, are the system's conclusions appropriate, and is the relative ranking of the hypotheses that the system produced correct?

(ii) Is the next query posed by the system an appropriate one?

In many cases, discrepancies simply required fine tuning of the rule parameters, i.e., changes in the ignorance factor $[m(\Theta)$ value] of the rule, or changing the relative rankings of the conclusions on the right hand sides of rules. In a few cases, discrepancies required the addition of new rules, or a major rewrite of some of the existing ones. The current debugging and fine tuning procedures are performed manually, but automation is clearly possible and planned in subsequent prototypes of OASES.

## 5. Conclusions

This paper presents the design and implementation of OASES, a prototype consultant system for trouble shooting production processes. OASES is written in Franz Lisp and runs on the VAX-11/780 system implements general cause analysis and specific cause analysis for a fiberglass manufacturing process. A number of case studies provided by the expert are being run, and the results have either led to the fine tuning of current rules or the creation of new rules to fill gaps in the knowledge base.

In summary, the prototyping phase has been instrumental in gleaning insights and knowledge in four specific areas critical to the development of an expert system:

(i) the formalization of domain terminology, (ii) the expert's method of judgemental analysis, (iii) the expert's overall decision making process, and

(iv) the impact of multiple, and often conflicting symptoms upon hypothetical causes.

Via extensive case studies each area has provided fruitful results. Domain terminology in the form of semantics, keywords and relevant phrases supplied vital components for both the front end natural language processor and the inference engine. Much of this information has surfaced explicitly via user interaction. The expert's judgemental analysis, particularly the validation of initial belief values associated with specific symptom/cause relationships, was strengthened as he was confronted with explicit results of his implied heuristics. The expert's overall decision making process, including the choice of specific queries to direct a user to provide relevant evidence, and the determination of query priorities continues to evolve both in effectiveness and efficiency as the interaction process is refined by the inclusion of more precise sets of queries. Finally, a number of surprising results stemming from combinations of multiple, and sometimes conflicting hypotheses have forced the domain expert and knowledge engineers to rethink sometimes simplistic interpolations and one dimensional reasoning.

We believe in conclusion that both experts and system designers benefit tremendously as they are bombarded by the end results and implications of their decision processes in this simulated environment. Furthermore, the necessity to leverage human expertise within the manufacturing domain will provide the impetus for future development and application of XDSS for production control.

## Appendix: Example of a Diagnostic Consultation

OCF is a major product of fiberglass products. They have been experiencing severe profitability problems recently at one of their largest manufacturing locations. The factory manager interacts with the expert system OASES as outlined below.

## →OASES

OASES is ready.

Type “help.” if a question is not clear or a valid response is unknown.

Diagnostic commands are “show facts.” “show hypotheses.” “show rule $\langle rule\# \rangle$ .”

What type of products/services does your company provide?

We produce fiberglass products for the automotive, corrosives and marine industries

[From the above response the system picks ((product type) (fiberglass))].

I'm not sure what you mean. Our forming area is involved.

[Again no direct response is obtained, but the keyword forming enables the system to make some conclusion about the type of process involved. The following system queries are related to determining the process type.]

What is the type of layout?
Our furnaces and channels are very rigidly structured.

[OASES extracts (layout) (rigid) from this re-sponse.]

On what basis does the product operate in the market place?
Mainly on price and quality.

[This is a multiple evidence statement. OASES picks up two pieces of evidence price and quality from the above response.
At this stage the system is reasonably sure that the process type is continuous flow.
However, it asks one more question to be absolutely sure.]

What key factors influence your output (yields)? I don't understand. Help.

Is output mainly dependent on worker productivity machine productivity raw materials, or initial setups, etc. Probably on our raw materials, we experience wide variations in our yields.

[At this stage the system is convinced that the process type is “continuous flow”. In the next step it queries the manager for symptoms.]

What days of the week do your problems occur? all work days.

[The system accepts phrases as valid input.]

On which shifts have you observed the problem? We have been experiencing a gradual decrease in efficiency over all shifts.

[For this response, the system cannot parse it directly using an augmented transition tree. So it resorts to a pattern matching approach and finds two pieces of evidence which it then asks the user to verify.

OASES has extracted the following evidence. Confirm (y.) or disconfirm (n.). ((trouble occurs) (all shifts))? y. ((problem symptom) (decrease in efficiency))? y.

[As expected, the user confirms both symptoms. Otherwise, the system would have just ignored that part of the statement but the user would be aware of it.

This concludes the top level partition of the system. OASES has come to the following preliminary conclusions:]

Possible cause categories
(i) process design (certainty value = 0.358)
(ii) technology (certainty value = 0.329)
(iii) raw material sourcing (certainty value = 0.221)

[Other cause categories with certainty values less than 0.05 are ignored.

The next set of queries pertain to the continuous flow partition of the knowledge base. Note that process design is the top ranked hypothesis.]

Are you experiencing excess capacity early in the process flow? No, I don't think so.

Are you experiencing insufficient capacity late in the process flow?
No, there are no bottlenecks in the process.

[The above responses have ruled out “process design” as the top ranked hypothesis. The current ranking is: (i) technology (certainly value: 0.358), (ii) process design (certainty value: 0.299) and (iii) raw material sourcing (certainty value: 0.253).]

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
iron $\Rightarrow 0.0022$.
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
calcium $\Rightarrow 0.0124$.
</div>

When was your last major investment in process technology?

Two years ago we built new electrode-fired forming tanks.

[This response causes the system to rule out technology. The current ranking is: (i) raw material sourcing (certainty value: 0.358), (ii) process design (certainty value: 0.335) and (iii) technology (certainty value: 0.215).]

Does your input raw materials meet specifications? I'm not sure.

[This response causes the system to set aside this query for later. Actually the system considers this piece of evidence very important, so it tries to obtain it in a different way.]

Have you changed vendors for any major raw materials recently?
Yes.

[This causes belief in raw material sourcing to increase. The current certainty values are: (i) raw material sourcing (certainty value: 0.544), (ii) process design (certainty value: 0.238) and (iii) technology (certainty value: 0.155).

The system proceeds ...]

Is there any difference between the materials supplied by the new vendors and the old ones?

[This question is a follow up on the one before the previous one, where the system got no response.] Yes, both the dolomite and probertite have smaller particle densities.

[This piece of evidence enables the system to draw its final conclusions about the most likely cause category based on the peak certainty value (max. certainty value > 0.6 and difference between first and second values > 0.3). Also, the $m(\Theta)$ value < 0.05). The system's final response is ...]

The two top ranked cause hypotheses are: (i) raw material sourcing (belief value: 0.86)

(ii) process design (belief value: 0.07)

The following facts strongly supported the top ranked hypothesis:

(i) fiberglass products. (ii) rigidly structured layout. (iii) output depends mainly on raw materials. (iv) change of vendors.

(v) change in raw material quality.

[OASES has been able to confirm the most likely general problem cause is “raw material sourcing.” Therefore, it begins the Specific Cause Analysis Phase].

Product = (product type is fiberglass) Process Type = (process type is continuous flow) General Problem Cause = (cause is raw material sourcing) in partition FB CF RMS

Enter the viscosity level of the molten glass leaving the furnace (in vol/time). 22.0.

[OASES concludes that the molten glass viscosity level is not nominal.]

Enter tested physical characteristics of DOLO-MITE (5 percent = 0.05).

[OASES extracts ((batch ingredient dolomite iron content 0.0022 percent) 1.0)]

[OASES extracts ((batch ingredient dolomite calcium content 0.0124 percent) 1.0)]

titanium $\Rightarrow 0.0015$ .

[OASES extracts ((batch ingredient dolomite titanium content 0.0015 percent) 1.0)]

boron $\Rightarrow 0.0261$ .

[OASES extracts ((batch ingredient dolomite boron content 0.0261 percent) 1.0)]

flourine $\Rightarrow 0.032$ .

[OASES extracts ((batch ingredient dolomite flourine content 0.032 percent) 1.0)]

Enter tested physical characteristics of CLAY (5 percent = 0.05).
iron ⇒ 0.002.
calcium ⇒ 0.02013.
titanium ⇒ 0.00141.
boron ⇒ 0.01196.
flourine ⇒ 0.001.

Enter tested physical characteristics of PROBERTITE (5 percent = 0.05).
iron ⇒ 0.003.
calcium ⇒ 0.01.
titanium ⇒ 0.001002.
boron ⇒ 0.01.
flourine ⇒ 0.01.

Enter tested physical characteristics of FLOURSPAR (5 percent = 0.05).
iron ⇒ 0.0015.
calcium ⇒ 0.0018.
titanium ⇒ 0.0014.
boron ⇒ 0.02074.
flourine ⇒ 0.10.

rule rule213 deduces ((sc is BLF) 0.12) & ((sc is IRM) 0.48)

[in other words, top ranked specific cause is “in-consistency in raw materials.”]

Enter tested physical characteristics of SILICA (5 percent = 0.05).
iron ⇒ 0.003.
calcium ⇒ 0.02.
titanium ⇒ 0.001.
boron ⇒ 0.02.
flourine ⇒ 0.001.

Enter tested physical characteristics of LIMES-TONE (5 percent = 0.05).
iron ⇒ 0.001.
calcium ⇒ 0.02.
titanium ⇒ 0.001.
boron ⇒ 0.01
flourine ⇒ 0.001002.

Some ingredients oxide contents are OUTSIDE Control Limits

Max hyp is ((sc is IRM) 0.420)

[System concludes because some oxide contents are outside control limits. Specific cause “inconsistent raw material” is still the top ranked hypothesis.]

Do the post-mixer physical test results conform to the batch formula?
yes.

Provide the two most recent scale audit weights (in lbs)
WGT#1⇒49.99.
WGT#2⇒49.98.

Max hyp is ((sc is IRM) 0.420)

Provide the PSI pressure for each feeder line during use
F1 ⇒ 201.
F2 ⇒ 200.
F3 ⇒ 199.
F4 ⇒ 198.
F5 ⇒ 202.
F6 ⇒ 200.

Max hyp is ((sc is IRM) 0.420)

Observed any wide fluctuations in any bin levels recently?

the dolomite bin was low.

[OASES extracts (bin level fluctuation for dolomite has occurred)].

What was the DOLOMITE compaction ratio (wgt / area)?
4.2.

Max hyp is ((sc is BLF) 0.886).

OASES at SCA = FB CF RMS confirms that the specific cause is Bin Level Fluctuation with a belief value = 0.886

[At this point OASES confirms that the specific cause for the raw material sourcing problem is "bin level fluctuation."]

## References

[1] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, 1980, The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11, No. 4, 337–356.

[2] Buchanan, B.G. and E.H. Shortliffe, eds., 1984, Rule Based Expert Systems: The MYCIN Experiments of Stanford HPP (Addison-Weseley, Reading, MA).

[3] Chase. R.B. and N.J. Aquilano, 1977, Production and Operations Management (Irwin, Illinois).

[4] Dutta, A. and A. Basu, 1984, An Artificial Intelligence approach to Model Management in Decision Support, Computer, 17, No. 9, 89–97.

[5] Gordon, J. and E.H. Shortliffe, 1985, A Method for Managing Evidential Reasoning in a Hierarchical Hypothesis Space, Artificial Intelligence 26, 323–357.

[6] O'Connor, D.E., 1984, Using Expert Systems to Manage Change and Complexity in Manufacturing, Artificial Applications in Business (W. Reitman, ed.) (Ablex, NJ) 149–157.

[7] Oliff, M.D., ed., 1987, Expert Systems and the Leading Edge in Production Planning and Control (Benjamin/Cummings, Menlo Park, CA).

[8] Power, 1984, Using the Symptoms, Diagnosis and Treatment Framework to Structure Knowledge for Management Expert Systems, Working paper MS/S 84-206, Dept. of Management Science and Statistics, Univ. of Maryland.

[9] Schmmener, R.W., 1984, Production/Operations Management: Concepts and Situations (Scientific Research Associates, Chicago).

[10] Sen, A. and G. Biswas, 1985, Decision Support Systems: An Expert Systems Approach, Decision Support Systems 1, 197–204.

[11] Shafer, G., 1976, A Mathematical Theory of Evidence (Princeton Univ. Press, NJ).

[12] Szolovits, P. and S.G. Pauker, 1978, Categorical and Probabilistic Reasoning in Medical Diagnosis, Artificial Intelligence 11, 115–144.
