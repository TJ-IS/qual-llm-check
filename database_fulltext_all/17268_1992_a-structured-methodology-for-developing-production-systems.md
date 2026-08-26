---
otero_id: 17268
otero_key: "SBCC4C6E"
title: "A structured methodology for developing production systems"
authors: "Ritu Agarwal; Mohan Tanniru"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90042-n"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A structured methodology for developing production systems \*

Ritu Agarwal

University of Dayton, Dayton, OH 45469, USA

Mohan Tanniru

Syracuse University, Syracuse, NY 13244, USA

Issues such as project management, documentation, and maintenance, typically associated with large traditional software development projects have recently become important concerns in the development of expert systems. We describe a structured methodology for the development of production rule-based expert systems. The methodology prescribes a procedure to help knowledge engineers manage the complexity of a knowledge base by viewing rule and parameter dependencies at successive levels of abstraction. Parameters are clustered into modules, in a manner analogous to functional decomposition in structured design. The modularization thus obtained provides three significant benefits: ease of subsequent knowledge base maintenance, enhancement of code reusability, and support for knowledge base verification. The visual tools used by the methodology facilitate communication between knowledge engineers and experts and provide ongoing documentation of the system.

Keywords: Rule-based systems, Software engineering, Structured methodology, Production systems, System maintenance, Expert systems, Rule base Modularization

![](/api/attachments/SBCC4C6E/fulltext/images/8f134485610c84f8dc95f9a4115de58b0ceb276f6aec9e2c3c6dc49d9c02b6ab.jpg)

Ritu Agarwal is an Assistant Professor in the Department of MIS and Decision Sciences at the University of Dayton. She received her Ph.D. in MIS and M.S. in Computer Science from Syracuse University in 1988. Professor Agarwal's publications have appeared and are forthcoming in Journal of MIS, Information and Management, OMEGA, Knowledge-Based Systems, International Journal of Man-Machine Studies and elsewhere and she has presented papers at national and international meetings. Her research interests are in knowledge acquisition, expert system development and validation, decision support systems, and group decision making.

Correspondence to: R. Agarwal, Department of MIS & Decision Sciences, University of Dayton, Dayton, OH 45469-2130, USA. E-mail: agarwal@udavxb.oca.udayton.edu.

\* All earlier version of this paper was published in the Proceedings of the Twenty-Fourth Hawaii International Conference on Systems Sciences, IEEE Computer Society Press, 1991.

## 1. Introduction

The production rule formalism has become a popular method for knowledge representation in expert systems [8], as conceptually, it is relatively simple to program and develop. Knowledge modeled through production rules is purported to exhibit many desirable properties that enhance both its semantic clarity and its maintainability. These include modularity, uniformity [3], and the ability of the resultant expert system to explain and justify its reasoning to the user. The high degree of modularity inherent in rule-based systems, however, also contributes to the opacity of the production rule representation which renders the behavior flow or procedural component of the system completely invisible to the user (and more importantly, to the developer) [3]. Procedural or algorithmic transparency may be a desirable attribute from the perspective of end users, but, from a developer's perspective, it only exacerbates the complexity of the program.

The espoused methodology for the development of expert systems is an evolutionary, prototyping approach [6], where the software evolves in an iterative fashion through interactions between knowledge engineers and experts. While there is merit to this approach in that prototyping is an appropriate mechanism for extracting ill-specified and unformalized expert knowledge, the inher-

![](/api/attachments/SBCC4C6E/fulltext/images/46a3b065d4d86553eb97ba1b83c0f492d5eb0c069703e42255dfd2846b2bed70.jpg)

Consultancy Services. His current research interests are in systems analysis and design, decision support systems, and expert systems.

ently ad-hoc nature of the development can lead to unanticipated problems after the system has been put into production.

Evolutionary development implies that the system designer does not, at project inception, possess an overall global picture of what knowledge the system will contain and how it eventually will be structured in the knowledge base. Further, as knowledge and decision rules are extracted in a piece-meal manner, ensuring the longitudinal correctness and consistency of the expert's utterances frequently becomes a significant issue. The primary vehicle for providing feedback to the expert in terms of what knowledge has already been acquired and encapsulated in the system is the actual prototype itself. Due to the intrinsically opaque nature of the representation and the context sensitive execution of rules, there are no guarantees that every thread of logic and reasoning is made obvious as the expert interacts with the system.

An important concern as the technology moves out of the laboratory into commercial environments is the amount of effort and resources required in updating expert systems, both in terms of adding new knowledge and maintaining existing rules $[2,16,20,23]$ . Though the nature of the rule-based programming paradigm permits flexibility in that new knowledge can be added without significantly impacting other parts of the program (often referred to as the modularity advantage), the development process itself provides no well-defined techniques for documenting these changes. Further, modifications to the knowledge base often lead to unanticipated inconsistency and redundancy problems $[19]$ . This can result in software that soon becomes too complex to manage efficiently and where maintenance costs outweigh the benefits accruing to the organization.

Structured analysis, design, and coding have been accepted as effective techniques for managing the complexity of large and often ill-defined traditional software development projects $[4,17]$ . With an increasing installed base of commercial expert system applications, recent research has focused on applying software engineering concepts and principles to the development and maintenance of expert systems $[2,7,16,23]$ . As expert systems applications become larger in size and permeate many areas of an organization's operations, concerns related to the issue of multiple knowledge engineers working on the same project, documentation, and code reusability have acquired greater significance [2,10,12,16].

De Marco [9] defines structured analysis as a modern discipline for conduct in the analysis phase. The primary shortcomings of the classical analysis techniques are being addressed through structured analysis by attempting to develop specifications that: (i) are decomposable (to manage complexity); (ii) provide avenues for user-analyst communication (through graphical aids); and (iii) enhance maintainability through limited redundancy. The major vehicle for analysis and communication under this approach is the data flow diagram, which provides a graphic representation of the flow of data in an existing or proposed information system. Central to the philosophy of structured design is the notion of modularization or functional decomposition, where the tasks that the software is required to perform are divided into independent modules to minimize coupling and communication [25]. In addition to providing graphical aids for program coding such as the top-down structured design chart, this approach helps provide an overall conceptual visualization of the system and how various components of it relate to each other. The outputs of structured design are then translated into structured programs, which use a limited set of programming constructs to enhance their readability and maintainability [5].

The rationale underlying structured analysis and design is that of complexity management through abstraction, by enhancing system correctness, reliability, maintainability, and extensibility $[22]$ , and providing on-going documentation throughout the development process. This paper presents a structured methodology for the development of rule-based expert systems. The methodology arose from motivations similar to those underlying RIME, a software engineering approach developed to enhance programmer productivity in the design and maintenance of very large knowledge bases $[2,23]$ . RIME prescribes control methods that allow for a certain level of code dependency and procedural control to be introduced into the inherently non-procedural rule-based programming paradigm. Additionally, RIME includes explicit criteria for organizing the rule base. The application of these criteria groups rules into abstract sets to allow efficient indexing into the rule-base. The developers of RIME cite several benefits they have obtained from its deployment in the reconstruction of XCON, including reduction in rule size and complexity and an increase in programmer productivity in maintenance.

Similar to RIME, the methodology described here is designed to help knowledge engineers manage the complexity of a knowledge base through a graphical aid that allows rule and parameter dependencies to be viewed at successive levels of abstraction, thereby achieving information hiding and data encapsulation. Parameters are clustered into modules, in a manner analogous to functional decomposition in structured design. The modularization thus obtained provides three significant benefits: Ease of subsequent knowledge base maintenance, enhancement of code reusability, and support for knowledge base verification. The visual tools used by the methodology construct a paper model of the system as it evolves, facilitate communication between knowledge engineers and experts, and provide on-going documentation of the system. Unlike RIME, however, our approach does not impose any form of inference control in the resultant expert system.

![](/api/attachments/SBCC4C6E/fulltext/images/34c6d86aa3e448ada9c7853a58bdaa15055df546397ffa5cf08e3b286e26758d.jpg)  
Fig. 1. Parameter dependency network.

The paper is organized as follows. Section 2 describes the general type of relationship modeled through a knowledge rule and develops a parameter dependency network (PDN) which is the analogue of the data flow diagram in the expert system context. Using the properties exhibited by the dependency relationship, rules for the decomposition of this network at successive levels of abstraction are developed in Section 3. The clustering obtained by the application of these rules is synthesized into the parameter hierarchy chart (PHC) which provides a top-level abstraction of the knowledge and rules contained in the system. Section 4 illustrates how the methodology assists in maintenance, code reusability, and verification. The final section presents some directions in which further research is underway.

## 2. Parameter dependency network

A knowledge rule is a modular chunk of problem solving knowledge of the form IF $\langle$ antecedent $\rangle$ THEN $\langle$ consequent $\rangle$ . The antecedent or conditional part of the rule contains one or more parameters, connected by logical operators, which specify the conditions under which the consequent is true. The consequent itself may specify an intermediate or final inference that can be drawn about a parameter, or it may be the invocation of another rule, i.e., the next problem solving step.

Problem solving knowledge expressed as rules is synthesized into a directed graph called a parameter dependency network (PDN). The PDN captures causal relationships between antecedent and consequent parameter sets and is a useful graphic technique for visualizing relationships among relevant domain variables $[14]$ . The purpose of the PDN is to serve as an aid during the design phase of rule-based systems. During the knowledge acquisition phase of development, other techniques such as influence diagrams (which show the relationship between actions taken and information possessed at the time of action) and knowledge maps $[15]$ (which depict probabilistic dependency between variables of interest) may be used to facilitate communication between knowledge engineers and experts. In spirit, the PDN is very similar to a cognitive map [18] which has been proposed as an aid for information requirements determination. However, while techniques such as knowledge maps, influence diagrams, and cognitive maps are useful for knowledge acquisition and documentation; as illustrated later, in order to study possible design architectures, it becomes necessary to translate them into a representation such as a PDN.

Fig. 1 shows one such network that is used to establish the value of a goal variable, u. In this figure, circles represent nodes or parameters and vertical bars represent the functional relationships or rules. This section describes the conventions used to construct the network, as well as relevant terminology and notation, and the following section describes rules that can be applied to level the network so that each level provides a different degree of abstraction.

Let $P(j)$ represent the set of all parameters whose values are required to obtain a value for parameter $p_j$ . Thus, $P(j)$ contains all the parameters which appear in the antecedent of rules that have $p_j$ as the consequent. Let $f_{p_j}$ represent the set of all rules that describe such a relationship between $p_j$ and $P(j)$ . If the set $P(j)$ is empty, then the value of the parameter $p_j$ is either input by the user (U) or internally defined to assume one value from a fixed set of values (I), i.e. $f_{p_j} = U$ or I. For example, the relationships used in estimating the value for a parameter $u_2$ in fig. 1 are: $f_{u_{2.11}} = I$ , $f_{u_{2.12}} = I$ , $f_{u_3} = U$ , $f_{u_{2.1}} = \{(u_{2.11}), (u_{2.12}), (u_3)\}$ , and $f_{u_2} = \{(u_{2.1})\}$ . In other words, the parameter $u_2$ needs $u_{2.1}$ , which in turn needs parameters $u_{2.11}$ and $u_{2.12}$ , and $u_3$ . The parameters $u_{2.11}, u_{2.12}$ and $u_{9.11}$ are all internally defined and the value for parameter $u_3$ is input by the user.

Note that each member of the rule set (e.g., $f_{u_{2,1}}$ ) that defines a parameter (such as $u_{2,1}$ ) need not use all its input parameters. The parameters that appear to the right of the network with no successors ( $\{p_{k} \mid p_{k} \notin P(l), p_{l} \neq p_{k}\}$ ) are referred to as goal parameters (G). Those parameters that appear to the left of the network with no predecessors and are defined by the user ( $\{p_{m} \mid f_{p_{m}} = U\}$ ) are called entry level parameters (E). Hence, an entry level parameter is one whose value is supplied through user input. In fig. 1, $G = \{u\}$ and $E = \{u_{5.111}, u_{1}, u_{3}, u_{4}, u_{6}, u_{10}\}$ . Further, note that $u_{5.11}$ and $u_{5.111}$ are both needed to establish the value of $u_{5.1}$ , but $u_{5.111}$ is also an antecedent of $u_{5.11}$ .

Define a relation R on the parameter set in the following manner

$$
p _ {j} \text {   R   } p _ {k} \quad \text { iff } \quad p _ {j} \in P (k).
$$

Here R captures the dependency of the parameter $p_{k}$ on $p_{j}$ . The relation R forms a partial order on the set of parameters, i.e., it is

reflexive $(p_x\mathbb{R}p_x)$

$$
\text { transitive } \left(p _ {x} \mathrm{R} p _ {z}, p _ {y} \mathrm{R} p _ {z}, \Rightarrow p _ {x} \mathrm{R} p _ {z}\right),
$$

$$
\text { anti - symmetric } \left(p _ {x} R p _ {y}, p _ {y} R p _ {x} \Rightarrow p _ {x} = p _ {y}\right).
$$

Similarly, define the complement relation of R as $R'$ , where $p_{j}$ $R'$ $p_{j}$ iff $p_{j} \in P(k)$ . Further, $p_{j}$ ; is said to be independent of $p_{k}$ , written $p_{j}$ $R^{\sim}$ $p_{k}$ iff not ( $p_{j}$ R $p_{k}$ ) and not ( $p_{k}$ R $p_{j}$ ). See table 1 for a description of some of the relationships exhibited in fig. 1.

The order of the relationship between two parameters, $p_{j}$ and $p_{m}$ is defined as follows: If there exists $p_{k}$ s.t. $p_{j}$ R $p_{k}$ and $p_{k}$ R $p_{m}$ , then $p_{j}$ R $^{2}$ $p_{m}$ . Notice that the order of the relationship between two parameters specifies the number of arcs (or number of nodes -1) that occur between the two parameters on a given path. The order of relationships is path dependent. For example, the order of the relationship between $u_{5.111}$ and $u_{5.1}$ is 2 using path ( $u_{5.111}$ , $u_{5.11}$ , $u_{5.1}$ ) and 1 using path ( $u_{5.111}$ , $u_{5.1}$ ).

Let $C_{p_j}$ denote the cardinality of $P(j)$ . The number of immediate predecessors of a parameter $p_j$ (predecessor cardinality) is given by

$$
C _ {p _ {j}} = | P (j) |,
$$

and the successor cardinality of $p_j$ is given by

$$
C _ {p _ {j}} ^ {\prime} = \left\{p _ {m} \mid p _ {j} \in P (m) \right\}.
$$

See table 2 for an illustration of some measurements associated with fig. 1.

A description of some of the relationships in fig. 1.

<table><tr><td> $\{u_2, u_5\}$  R  $u$ </td><td> $u_{5.11}$  R′  $u_{5.111}$ </td></tr><tr><td> $u_{2.1}$  R  $u_2$ </td><td> $u_{5.1}$  R′  $\{u_{5.111} 1 \ u_{5.11}\}$ </td></tr><tr><td> $u_{5.1}$  R  $u_5$ </td><td> $u_{2.1}$  R′  $\{u_{2.11}, u_{2.12} \ u_3\}$ </td></tr><tr><td> $u_2$  R~  $u_5$  as  $(u_2$  R~  $u_5)$  and  $(u_5$  R~  $u_2)$ </td><td></td></tr></table>

An illustration of some measurements associated with fig. 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$u_{2}$  R u includes arc between  $u_{2}$  and u
 $u_{2.1}$ $R^{2}$  u includes arc that links  $u_{2.1}$  to u via  $u_{2}$ $u_{2.111}$ $R^{3}$  u defines the path ( $u_{2.11}$ ,  $u_{2.1}$ ,  $u_{2}$ , u)
 $u_{5.111}$  R  $u_{5.1}$  defines the path ( $u_{5.111}$ ,  $u_{5.1}$ )
 $u_{5.111}$ $R^{2}$ $u_{5.1}$  defines the path ( $u_{5.111}$ ,  $u_{5.11}$ ,  $u_{5.1}$ )

 $C_{u}=|P(u)|=9$ $C'_{u_{2}}=|\{p_{k}|u_{2}\in P(k)\}|$ $=|\{u,u_{8.11}\}|$ 

=2
</div>

## 3. Network simplification through abstraction and leveling

The objective of simplifying a network is to understand the major relationships between entry level and goal parameters at different levels of detail. In other words, we want to be able to provide a top-down view of the network. While a system specification of any type can take a global view to start with (describe the relationship between major input and goal variables) and gradually refine it into greater detail, this paper presents a bottom-up approach to developing a top-down view. Developing this bottom-up view involves designing certain detailed components first and iteratively aggregating them as a greater number of detailed components are assembled together. This approach is not inconsistent or unrealistic as most expert systems are developed using a prototyping methodology. Improvements in the prototype are achieved through new knowledge extracted from the expert, based upon the expert's reaction to knowledge already encapsulated in the system. A top-down design in such an environment may be unfeasible as most of the expert's knowledge can be extracted only incrementally and not necessarily in a top-down, breadth to depth form.

If, however, knowledge acquisition methods allow for a good understanding of system goals and major sub-goals, then it may be possible to develop a top-down view of the system for design. Even in these cases, as knowledge in continuously added over time, network simplification through abstraction can be used to reassess the view used for design from a performance standpoint. Thus, a top-down view may be altered using the abstraction derived from the bottom-up approach as the knowledge base evolves over time.

The development of decision support systems (DSS) is similar to expert systems development as they both employ preliminary models of the domain to understand and iteratively build more complete and complex systems [24]. The major difference is that in DSS, the flexibility of the architecture to accommodate changes in the decision making situation over time is a more important performance criterion for the system than is its computational efficiency. Expert systems, on the other hand, use methods of representation that are computationally intensive, and while the initial development may be ad-hoc, the system may need redesign to gain performance efficiencies at later stages of its usage [26]. Thus, a top-down view of an expert system developed using a bottom-up approach is necessary both from the perspective of being able to evaluate its performance and from the perspective of the eventual maintainability of the system.

![](/api/attachments/SBCC4C6E/fulltext/images/73f888d2d4ae01e74a3998d7dd190f446d72fda6de3ddc9a13ef9c92d2f6a227.jpg)  
Fig. 2. PDN after applying Rules 1 and 2.

In this section a set of rules is proposed to provide multiple levels of abstraction of the parameter dependency network. Each level of abstraction masks a certain degree of detail by aggregating parameters into groups of parameters, with the top level providing the interface and dependency information among groups. It is important to note that at each level of abstraction the dependencies among parameters and groups of parameters are retained, i.e. the basic characteristics of the PDN are not violated. The example used to illustrate the application of the rules has been extracted from an expert system that is currently in use [1].

## 3.1. First level of abstraction

At this level, all internally defined parameters are suppressed so that only the relationships between the user-defined parameters and the intermediate and final goal parameters are shown explicitly. Since the parameters suppressed are internally defined, their impact is only local to the definition of the parameter which uses them and has little impact on other parameter dependency relationships.

## Rule 1. Suppression of internally defined parameters

Merge internally defined parameters with their immediate successors, i.e. combine $p_{j}$ with its successors if $f_{p_{j}} = I$ . Rename these successors to reflect this redefinition. The application of this rule is shown in fig. 1. Here $u_{2.11}$ and $u_{2.12}$ are combined with $u_{2.1}$ to form a new parameter $u_{2.1}^{\prime}$ , and $u_{9.11}$ is combined with $u_{9.1}$ to form a new parameter, $u_{9.1}^{\prime}$ .

## 3.2. Second level of abstraction

The second level of abstraction is used to substitute a single node (a supernode [15]) in place of a set of dependent nodes on a sequential path. At this level, our interest is in nodes that appear on multiple paths. Multiple nodes on a single path are not of particular interest as the evaluation of one node on the path implies the evaluation of all of them, and hence, a single representative node for all these sequential nodes provides the same information, while hiding the complexity.

## Rule 2. Successive merger

Merge parameters successively with those that have a successor and predecessor cardinality of 1.

$$
\begin{array}{l} p _ {k} \text { is   merged with } p _ {m} \\ \text { iff } p _ {k} \text { R } p _ {m} \\ \text { and } C _ {p _ {m}} = 1 \\ \text { and } p _ {k} \notin E \text { and } p _ {m} \notin G. \end{array}
$$

In fig. 1, $Cu_{2}$ , $Cu_{5}$ , $Cu_{8}$ and $Cu_{8.1}$ are all 1 and hence can be merged appropriately. The resulting network is shown in fig. 2. Since $u_{2}$ is renamed as $u_{2}'$ , all other occurrences of $u_{2}$ are changed to $u_{2}'$ .

A path in the network is a legitimate sequence of parameters with a length greater than 0. A path of length 0 is simply a node. Denote a path x from $p_{j}$ to $p_{k}$ (that includes both end parameters) by

$$
\begin{array}{l} \text {path} _ {[ p _ {j}, p _ {k} ]} ^ {x} = \left\{p _ {j}, p _ {m}, p _ {m + 1}, \dots p _ {m + n}, p _ {k} \right\}, \\ \text {and} p _ {j} R ^ {n + 2} p _ {k}. \end{array}
$$

Further, denote a path from $p_j$ to $p_k$ that does not include both end parameters by path $_{(p_j, p_k)}^x$ . The length of a path from $p_j$ to $p_k$ is given by $|\text{path}^{x}_{(p_j, p_k)}|$ . Therefore, if $p_j \mathbf{R} p_k$ or $p_k \mathbf{R}' p_j$ , then $|\text{path}^{x}_{(p_j, p_k)}| = 0$ .

Two paths between $p_j$ and $p_k$ , say path $_{(p_j, p_k)}^r$ and path $_{(p_j, p_k)}^s$ are said to be parallel to each other iff

$\mathrm{path}_{(p_j,p_k)}^r\cap \mathrm{path}_{(p_j,p_k)}^s = 0$ and $p_l\in \mathrm{path}_{(p_j,p_k)}^r$ and $p_m\in \mathrm{path}_{(p_j,p_k)}^s$ are not members of any other paths, path $_{(p_s,p_t)}^y$ , s.t. path $_{(p_s,p_t)}^y\notin \mathrm{path}_{(p_j,p_k)}^r$ and path $_{(p_s,p_t)}^y\notin \mathrm{path}_{(p_j,p_k)}^s,$ and $|\mathrm{path}_{(p_j,p_k)}^r| + |\mathrm{path}_{(p_j,p_k)}^s|\neq 0,$ i.e. at least one path has a length greater than 0

For example, in fig. 2, $\mathrm{path}_{(u_{5.111}, u_5')}^m = 0$ and $\mathrm{path}_{(u_{5.111}, u_5')}^n = u_{5.11}$ and, according to the definition above, these are considered parallel paths as long as $u_{5.11}$ is not a member of any other path. Two special cases can be defined in identifying parallel paths, viz., entry node and group node parallel paths.

## Entry node parallel path

This corresponds to a situation where two paths $\text{path}_{(p_{j},p_{k})}^{r}$ and $\text{path}_{(p_{l},p_{k})}^{s}$ are considered to be parallel if they satisfy all the conditions specified above for the parallel path definition, and, an additional restriction that the starting nodes of these paths (i.e. $p_{j}$ and $p_{l}$ ) are both members of the entry parameter set E. In other words, the paths $(u_{3}, u_{2}^{\prime}, u)$ and $(u_{5.111}, u_{5.11}, u_{5}^{\prime}, u)$ of fig. 2 could potentially be treated as parallel if $u_{2}^{\prime}, u_{5.11}$ , and $u_{5}^{\prime}$ are not members of any other paths, since $u_{3}$ and $u_{5.111}$ are both members of the entry parameter set E. However, $u_{2}^{\prime}$ is a member of another path that defines $u_{8}^{\prime}$ , and hence the paths are not regarded as parallel. On the other hand, path $(u_{3}, u)$ is parallel to path $(u_{5.111}, u_{5.11}$ , $u_{5}^{\prime}, u)$ as $u_{5.111}$ and $u_{3} \in E$ and $(u_{5.11}, u_{5}^{\prime})$ are not members of any other path.

## Group node parallel path

The parallel path definition is not restricted to situations where $p_{j}$ is a single parameter. The input parameter $p_{j}$ can represent a group of parameters. However, the end parameter, $p_{k}$ , is always restricted to be a single parameter. For example, $\text{path}_{((a,b,c),d)}^{r}=l_{1}$ and $\text{path}_{((x,y,z),d)}^{s}=l_{2}$ are parallel. The situation where $p_{k}$ represents a group of parameters can be trivial if multiple $p_{k}$ , when combined with the parameters that succeed $p_{k}$ , result in parallel paths. The entry node condition in parallel path definition can also apply when these starting nodes are groups of parameters and are members of the set E. In fig. 2, $\text{path}_{((u_{1},u_{3}),u_{9})}^{r}=\{u_{9.1}^{\prime}\}$ and $\text{path}_{(u_{1},u_{9})}^{s}=\phi$ are parallel if $u_{9.1}^{\prime}$ is not a member of any other path, as $u_{1}$ and $u_{3}$ are both members of E.

![](/api/attachments/SBCC4C6E/fulltext/images/4b1f852797a5f21dfdfbe8a35173fe1b2dbfbe9041268c6ad09e1edfc6f9030f.jpg)  
Fig. 3. PDN after applying Rules 3 and 2.

## 3.3. Third level of abstraction

At this level, all parallel paths are replaced by a single path, since the function performed by each of the parallel paths is to estimate the value of their end nodes. From a global perspective, the end node of these parallel paths and their input nodes are of major interest, while each parallel path is primarily of local interest.

In determining and collapsing parallel paths, two points are worth noting: (i) Not all parallel paths are immediately obvious to visual inspection, especially when the network is complex. Hence, a systematic, algorithmic procedure is required to identify parallel paths; and (ii) The following rule is applied iteratively until all parallel paths are collapsed. In doing so, paths nested inside other parallel paths are collapsed first. For example, in fig. 2, $(u_{9.1}^{\prime}, u_{9})$ , $(u_{9.1}^{\prime}, x_{1}, u_{9})$ and $(u_{9.1}^{\prime}, x_{2}, u_{9})$ are all parallel and are nested within the parallel paths $(u_{1}, u_{3}, u_{9})$ and $(u_{1}, u_{9})$ .

Thus, the three inner paths will be merged before the two outer paths.

## Rule 3. Collapsing parallel paths

Replace parallel paths with a single sequential path of length 0 with the start node of the new path representing the start nodes of all the parallel paths being collapsed, and a new end node representing the end node of the parallel paths plus all the individual nodes that are members of each of these parallel paths. Do not collapse parallel paths with an end node if information about a significant intermediate note is being lost (this concept is explained subsequently). Fig. 3 describes the PDN after the parallel paths represented in fig. 2 are collapsed.

Notice that this simplified network shows the relationship between entry parameters $(u_{3}, u_{1}, u_{4}, u_{5.111}, u_{6}, u_{10})$ and the goal parameter, u, via certain intermediate parameters, $(u_{2}^{\prime}, u_{5}^{\prime\prime}, u_{8}^{\prime}, x_{1}^{\prime}, x_{2}^{\prime}, u_{9}^{\prime})$ . Also, collapsing of parallel paths creates a new sequential path $(u_{3}, u_{2}^{\prime}, u_{8}^{\prime}, u)$ and hence, a need for reapplication of Rule 2.

In certain cases, two parallel paths may be combined into a sequential path, but may not be collapsed with the end node if it appears that information about a significant intermediate node is being lost. For example, paths $(u_{9.1}^{\prime}, u_{9})$ , $(u_{9.1}^{\prime}, x_{1}, u_{9})$ , and $(u_{9.1}^{\prime}, x_{2}, u_{9})$ are all parallel and can be collapsed to $(u_{9.1}^{\prime}, u_{9}^{*})$ , where $u_{9}^{*} = u_{9} + x_{1} + x_{2}$ . However, if, in the designer's view, the intermediate nodes $x_{1}$ and $x_{2}$ are important parameters of interest, then the collapsing of these paths may be avoided. As we will see later, if these intermediate nodes are needed to determine the values of certain other goals (not shown in fig. 1), then this type of collapsing would violate Rule 3. In fig. 3, the designer's discretion is used to preserve information on $x_{1}$ and $x_{2}$ .

![](/api/attachments/SBCC4C6E/fulltext/images/619a68cb6e2f7401b042c6089b4ec06e91a287377dc69212b663c989f575e82f.jpg)  
Fig. 4. Dependency matrix.

## 3.4. Fourth level of abstraction

At this highest level of abstraction, all entry level parameters and intermediate parameters are merged with the goal parameter if they are used only in estimating that particular goal parameter and none others. If the expert system has a single goal, this abstraction merely highlights the relationship between entry-level and goal parameters (similar to a context diagram in the data-flow approach). However, if there are multiple goals or a single goal with a set of pre-specified intermediate sub-goals that have to be explicitly recognized, then this level of abstraction provides an overview of the major dependencies between groups of parameters and goal variables.

Rule 4. Reapplication of successive merger
Apply Rule 2 to a path, path $_{(p_{j},p_{k})}^{x}$ iff $p_{j}\in E,\ p_{k}\in G$ , and

$p_j \in \mathrm{path}_{[p_j, p_k)}^x$ is not an element of any other path

Note here that the path includes $p_{j}$ and all the nodes in the path leading to $p_{k}$ , but excludes $p_{k}$ , the goal parameter.

The application of this rule necessitates the availability of information on other goals, contained in fig. 4. Fig. 4 describes all the goals of the expert system (of which u is one) and their dependencies on entry level and intermediate parameters. A cross in cell $(i, j)$ indicates that parameter j is dependent on parameter i. The matrix is constructed by applying Rules 1, 2, and 3 to the PDNs associated with all system goals. As is evident from the definitions of these rules, this matrix contains only those entry level and intermediate parameters that are needed by more than one goal.

The application of any new rule is preceded by a reapplication, if necessary, of prior rules. Applying Rule 2 to fig. 3 results in the merger of $u_2'$ and $u_8'$ to form $u_8''$ . Now, applying Rule 4 to the same figure yields fig. 5. This is a top-down overview or context diagram of goal parameter $U'$ . Nodes $u_{5.111}$ , $u_5'', u_6$ , and $u_9'$ are all merged with $u$ as their use is local to the establishment of $u$ . On the other hand, $x_1', x_2'$ , and $u_8''$ , (intermediate nodes) as well as $u_{1}$ , $u_{3}$ , $u_{4}$ , and $u_{10}$ (entry nodes) are needed by other goals, and are hence retained.

![](/api/attachments/SBCC4C6E/fulltext/images/da8ae434934317df781925e5b8e2e844de9ae7b919483b13b36b2cdb474ba8db.jpg)  
Fig. 5. PDN after applying Rules 4 and 3.

## 3.5. Construction of parameter hierarchy chart

The overview diagram in traditional systems analysis provides the interfaces among various subsystems, hiding specific, local details and relegating them to lower level diagrams. In a similar spirit, the information contained in fig. 4 allows us to construct a PHC for the expert system. In fig. 6, parameters shown in rectangles correspond to entry level or intermediate parameters, while those contained in circles represent goal parameters. The figure is interpreted as follows. The highest level (level 0) rectangle contains all entry parameters. Goals that can be established solely on the basis of these parameters are shown at the following level (in this case, there are no such goals). At each subsequent level, goals that require, incrementally, the fewest number of intermediate parameters, as well as the intermediate parameters themselves are shown. The intermediate parameters contained in the rectangles have access to all intermediate parameters at and above their level, and all goal parameters above their level. For example, goals $E'$ and $M'/D'$ need only one additional parameter (shown at level 1) beyond the entry level parameters, and are hence included at level 2. Goal parameters at level n, thus, need parameters upto levels n-1. The parameters that are visible to intermediate parameter $L_{18}$ include $u_{1}, u_{3}, u_{4}, u_{10}$ , and $u_{8}'$ .

In this section we have described a methodology for decomposing the original PDN into successive levels of abstraction. The final outcome of the abstraction process is the PHC, which serves the important function of providing a top-down overview of the rules contained in the expert system. The next section examines the role of the modularization described here in knowledge base management. Specifically, we illustrate how the PDN and PHC can assist in knowledge base maintenance, code reusability, and knowledge base verification.

![](/api/attachments/SBCC4C6E/fulltext/images/337310bff3d9d28147b346922dc393b25e1ba8bbc8340cf2a3619ad41cbf2f0c.jpg)  
Fig. 6. Parameter hierarchy chart.

## 4. Modularization and knowledge base management

Conventional programming languages exhibit low transparency (i.e., an individual line of code provides little information about the program's overall functionality) and high behavior visibility (i.e., the sequence of code execution can be determined easily). Rule-based formalisms, on the other hand, exhibit high transparency (each rule provides information about its logical context) and extremely low behavior visibility (the sequence of rule firings is difficult to determine a priori) [21]. Traditional structured methodologies have addressed the transparency or functional context issues through design techniques such as top-down modular charts and structured programming. In a similar fashion, the PDN and the PHC are constructed to address the low behavior visibility or procedural context of rule-based systems. From a design perspective, the PDN and PHC provide three critical functionalities which are detailed in this section.

As highlighted previously, the iterative development of expert systems makes it difficult to design them in a top-down, modular fashion. However, once the system reaches a production stage, the rules of abstraction provide an effective means to document the knowledge base and, if required, redesign the system for performance efficiencies. Given the evolutionary nature of knowledge bases, it is imperative that the design allow for flexibility in evaluating the impact of and incorporating modifications on a continual basis. In fact, the rationale for decomposing systems into subsystems for modular design hinges around the following key issues: Flexibility of the system to adapt to changes quickly; separability/uniqueness of each module so that changes may be made relatively independently; enhancement of the semantics of each module; facilitation of code reusability and integration with other modules as such a need arises; and functional cohesion to make each module own only those parameters/rules that are absolutely necessary to fulfill its mission [11].

In the ensuing discussion, we demonstrate how the PDN and the PHC can be used to manage a knowledge base as it evolves over time, specifically in the areas of maintenance/modifications, code reusability, and verification. The example used before is extended. The knowledge structures used in the previous section describe an expert system before it went into production for the first time. The system guides salespeople through the task of configuring orders for air conditioners based on customer specifications and provides a series of correctly configured product codes (part numbers) as its output [1]. The individual subgoals (e.g., $E'$ , $M'/D'$ , etc.) correspond to constituent parts of an air conditioning unit such as electric coil and motor drive, and together, they provide a complete and correct manufacturing specification. Since its original design, the system has tripled in size and many enhancements and modifications have been made to the knowledge base. These changes were isolated for their effect and managed through the PDN and PHC associated with the knowledge base.

## 4.1. Role in maintenance and change management

Changes to a rule base can potentially influence the parameter dependency network to some degree and, in turn, the hierarchy chart. The discussion first evaluates the impact of the change in terms of the components of the modular hierarchy/PDN that would be affected, and then refines the knowledge structure after the change has been implemented.

Change 1. Changes which have minimal impact on existing levels of abstraction

These types of changes simply add new information to the system (entry or internally defined parameters) or use the values of existing goal/subgoal parameters defined in the PHC. Such modifications do not require any alteration in the abstractions used to derive the current hierarchy.

There was a requirement that a DATE be added to the order and be output with all the product codes generated by the configurator. Further, it was required that individual codes generated for each subgoal be concatenated and output as a single product code. Here a new parameter (CC) was defined to concatenate all previous goal values $E', M'/D', U', L1', L2', L3', \text{and } W'$ . Since goals at any level have access to all information at and above that level, the new goal was made a part of a new module at level 5. The parameter DATE was now included as a part of this module. This addition had minimal impact on other modules defined.

Certain job information (J) was requested from the user and it was to be associated with the output generated by the configurator. Again, this could be added as a subgoal at level 4 and could be included in the final goal, CC, since it does not impact any other parameters. However, users wanted the job information asked right up front, before requesting any other information. So, it was placed as a separate module at level 0. While this did not affect the intrinsic dependency requirements of the PHC in any way, it does highlight the need to consider the aesthetic needs of the user in the design whenever possible. Again, the impact here was somewhat minimal.

Similar to the job information option, another miscellaneous option (MO) was added. This merely depended on $u_{1}$ and $u_{3}$ , with the output of this option becoming an input to CC. Since $u_{1}$ and $u_{3}$ are established at level 0, the logical place for this subgoal was at level 1.

## Change 2. Changes that require modifications to the current levels of abstraction

These changes can potentially affect the levels of abstraction and the PHC in a variety of ways, depending on the complexity of the change. A few illustrative examples are presented below.

The engineer wanted to provide another subgoal (called electronic option, EO). The parameters on which it depended were $u_{1}$ , $u_{3}$ and $u_{6}$ . In the current hierarchy $u_{1}$ and $u_{3}$ belong to level 0, but $u_{6}$ is a part of $U'$ . By reassessing the abstraction used in generating $U'$ , it was decided to remove $u_{6}$ from $U'$ and place it at level 0 (being an entry level parameter) and the new option parameter (EO) was now established at level 1. While the EO parameter utilizes several other parameters, all of them are local to that module alone. EO was also included as a part of the final goal (CC) in level 5.

After incorporating the new subgoal, it was determined that the EO option was dependent on the date (which was a part of the level 5 module). A decision was then made to move the date up to level 0 (being an entry parameter). Obviously, another alternative would have been to add the new subgoal (EO) at level 5 and to move the final goal (CC) to level 6. However, this would have deepened the structure and delayed the inquiry on these options until the end. Since the EO option (based on the DATE) could possibly influence the customer's decision on placing the entire order, it was felt that it should be determined at the earliest.

A complex pricing scheme $(P)$ was added to price each order based on the cost of each component (or sub-goal) of the configurator. Since the components required to estimate price are established within each sub-goal, price could have been estimated within the modules and consolidated later, similar to the goal CC. This required examining each level of abstraction and adding/modifying the appropriate parameters. The other alternative was to decompose the configurator components at the end in order to price it all at once. Initially, for ease in managing change, pricing was performed at level 5.

A parameter (nozzle option, Dz) was defined in the original model as a local parameter associated with each of the sub-goals $L1'$ , $L2'$ , and $L3'$ . However, a change in this option made it common to all these sub-goals. As expected, this would make it a part of the parameters defined in the level 3 module and would require a change in the abstractions.

Change 3. User requested interaction changes with no impact on dependencies

These changes do not add to or alter the logical structure of the knowledge base with the introduction of any new parameters, but may cause changes to the physical structure or the mode of interaction.

Several screen changes were desired: either, in the form of consolidation of existing screens, i.e., requesting values of several parameters using a single screen, or the splitting of some existing consolidated screens. If the parameters affected by these changes are established at the same level or within the same sub-goal, this would have no impact. In a few cases, however, some parameters established at different levels were combined for comprehension and, as long as no parameter dependencies were violated, the change was accommodated. For example, users preferred that $u_{1}$ , $u_{3}$ and $u_{10}$ be asked together and this input was separated from other entry parameters such as DATE, $u_{4}$ , and $u_{6}$ . This change need not alter the structure of the PHC. On the other hand, if $u_{4}$ was needed to be combined with $L_{18}$ for screen definition, it may be moved down to the level 1 module.

The revised PHC is shown in fig. 7, which incorporates all the changes discussed thus far.

## 4.2. Role in code reusability

A major motivation for modularizing complex systems is to allow for future reusability of code $[2,23]$ . The modular design discipline enforced by the PDN and PHC assures this. For example, in the pricing change discussed above, a separate module to decompose the order for pricing purposes provided that module with important additional functionality. Subsequent to its transfer to production mode, a part of the configurator system was considered for use as a diagnostic tool. Now, in addition to providing the correct configuration for an order, if the user provides a product code, the system should diagnose its correctness and detect inconsistencies. In order to accomplish this, it needs to decompose the code into its constituent parts. Plans are underway to reuse the decomposition module for constructing such a diagnostic system.

Users requested that the possibility of building another configurator for a product that is smaller in scope, but with many similar sub-goals, be investigated. The modular structure of the existing system allowed the knowledge engineer to port a part of the hierarchy $(J, U', M'/D', \text{and associated dependencies})$ to a new knowledge base and alter it appropriately.

These two situations illustrate how a modular hierarchy can be effective not only for studying the impact of a change, but also to facilitate reusability of code. In both the cases of reusing existing knowledge and adding new knowledge, however, one needs to ensure that the revised knowledge base has not become inconsistent. The PHC can also be used to examine this issue.

![](/api/attachments/SBCC4C6E/fulltext/images/9e35982394cba41dc438a3d2270c395908aa8576b1eca8f6693a4a52f30178ef.jpg)  
Fig. 7. Modified parameter hierarchy chart.

## 4.3. Role in knowledge base verification

Whenever a new rule is added to a knowledge base, there is a potential for making the existing knowledge base redundant or inconsistent $[19]$ . The first step in verifying knowledge base integrity is to isolate the portion of the knowledge base which is directly affected by the rule addition. This process can be quite complex if there is no behavioral or procedural structure available to the knowledge engineer. However, using the levels of abstraction defined in the previous section and the resultant PHC, one can effectively partition the system to isolate the relevant set of parameters and rules impacted by addition.

For example, consider the case of a new rule being added to the knowledge base to establish the value for consequent $p_{n}$ . As before, let $P(n)$ represent the set of antecedent parameters for this rule. Several scenarios can emerge.

Scenario 1. Both $p_j$ and $P(n)$ are members of a single module

In this case, integrity checking can be localized to that module only, thus potentially limiting the investigation to a smaller set of existing rules in the rule base.

Scenario 2. Some members of $P(n)$ are at levels above the consequent parameter $p_n$

In this case, one needs to identify the entire path that is defined between these parameters and the consequent (i.e., all the rules that are defined in the knowledge base that use some of the parameters in the set $P(n)$ and reach $p_{n}$ using a variety of intermediate parameters). These are then used to check consistency/redundancy against the newly defined rule. While this task is not easy, the PHC does identify the part of the network that is of concern. Here the new rule does not violate any parameter dependencies.

Scenario 3. Some members of $P(n)$ are at levels below the consequent parameter $p_n$

The final scenario basically violates parameter dependencies defined in the current knowledge base. This implies that one needs to first investigate the appropriateness of the rule definition (i.e., are there inconsistencies in the definition, can one move some of these parameters at a lower level to a higher level to avoid this anomaly, etc.), before performing any kind of integrity checking for consistency or redundancy. The actual approach used for checking the integrity (local or global) is beyond the scope of this paper.

An important point to remember is that most inference engines do the necessary back-tracking to determine the value of a sub-goal or goal, without the benefit of any explicit procedural structure. As a matter of fact, that is one of the major benefits of separating knowledge from the reasoning process $[13]$ . While this is definitely useful in the initial system design, managing changes by evaluating their impact on existing knowledge bases can become a tedious process, especially if the knowledge engineer has to muddle through the internal reference lists supplied by most shells. This lack of behavioral visibility makes it necessary that certain support mechanisms be provided so that the effect of changes on the existing parameter dependencies is clearly highlighted. This is especially true when the knowledge base is partitioned into chunks or modules (as is typical in any reasonably large knowledge base), since many of these modular structures limit ownership of parameters or rules, and restrict certain amount of navigation through them. In such cases, a dependency-based hierarchy can provide significant help to knowledge engineers in making the needed adjustments to the knowledge bases when changes occur.

The philosophy of structured analysis and design in developing conventional systems is one of extracting ‘correct’ user requirements prior to making a substantial investment in designing systems and of ensuring that misunderstandings and misinterpretations do not propagate to system design. Such miscommunication can occur even more frequently in expert systems design, since the degree of complexity with the knowledge is much higher and it is extracted in many intermittent spurts. Graphical tools such as the PDN and PHC provide a quick visual examination of the knowledge encapsulated in the expert system to observe any anomalies, incompleteness, or inconsistencies in the parameter dependency definitions. Our experience suggests that the discipline imposed by these tools can assist in substantial ways in designing systems that are robust, correct, and maintainable.

## 5. Conclusions

The incipient nature of expert systems technology has precluded, to a large extent, the development of scientific methods for knowledge engineering. If systems developed using this technology are to exhibit tangible benefits downstream, it is imperative that the development process be made more manageable and development practices more structured. In this paper we have described structured tools, the PDN and the PHC, for managing the development of rule based systems. The PDN and PHC exhibit many properties desired of software development aids, including achieving information hiding, facilitating expert/knowledge engineer communication, providing system documentation, and allowing for the management of system complexity through leveling and abstraction. We further demonstrate how these tools can enhance software maintainability, code reusability, and knowledge base verification.

Two further areas of research are currently under investigation. First, the construction of the PDN and its subsequent leveling have been described in sufficient detail so as to permit the automation of these tasks. We are in the process of developing a prototype computer aided knowledge engineering tool that automatically constructs a PDN and levels it. Second, the specification of the PDN provided here does not provide parameter details at the value level, i.e., information about the feasible range of values that parameters can assume is not included explicitly in the representation. We plan to enhance the PDN to incorporate parameter values, so that concepts such as reachability may be applied to determine if system goals are achievable from given sets of input parameters. The inclusion of parameter values will also allow for the identification of missing rules, i.e., sets of parameters and associated values that do not have an appropriate action defined for them.

## References

[1] R. Agarwal and M. Tanniru, Systems Development Life-Cycle for Expert Systems, Knowledge-Based Systems 3., No. 3, 170–1180 (1990).

[2] J. Bachant and E. Soloway, The Engineering of XCON, Communications of the ACM, 311–317 (March 1989).

[3] A. Barr and E.A. Feigenbaum, The Handbook of Artificial Intelligence 1 (Kaufman, Los Altos, CA, 1981).

[4] B.W. Boehm, Software Engineering, IEEE Transactions on Computers, C-25, No. 12, 1226–1241 (December 1976).

[5] C. Bohm and G. Jacopini, Flow Diagrams, Turing Machines, and Languages with Only Two Formation Rules, Communications of the ACM 9, No. 5, 366–371 (May 1966).

[6] B.G. Buchanan, D. Barstow, R. Bechtel, J. Bennet, W. Clancey, C. Kulikowski, T. Mitchell and D.A. Waterman, Constructing an Expert System, in Building Expert Systems, F. Hayes-Roth, D.A. Waterman and D.B. Lenat (eds.) (Addison-Wesley, MA, 1983) 127-167.

[7] J.S. Davis, Effect of Modularity on maintainability of rule-based systems, International Journal of Man-Machine Studies 32, 439–447 (1990).

[8] R. Davis and J. King, An Overview of Production Systems, Machine Intelligence 8, J. Elcock and D. Michie (eds.), Chichester: Ellis Horwood, 300–332 (1977).

[9] T. DeMarco, Structured Analysis and System Specification, in Classics in Software Engineering, E.N. Yourdon (ed.), 411–424 (Yourdon, NY, 1979).

[10] L. Druffel and R. Little, Software engineering for AI based software products, Data and Knowledge Engineering 5, 93–103 (1990).

[11] K. Ewusi-Mensah, Identifying Subsystems in Information Systems Analysis, Information Systems 9, No. 2, 181-190 (1984).

[12] A.N. Habermann, Engineering large knowledge-based systems, Data and Knowledge Engineering 5, 105–117 (1990).

[13] F. Hayes-Roth., Rule Based Systems, Communications of the ACM 28, No. 9, 921-932 (September 1985).

[14] C.W. Holsapple and A.B. Whinston, Business Expert Systems Irwin, Homewood, IL (1987).

[15] R.A. Howard, Knowledge Maps, Management Science 35, No. 8, 903–922 (1989).

[16] R.J.K. Jacob and J.N. Froscher, A Software Engineering Methodology for Rule-Based Systems, IEEE Transactions on Knowledge and Data Engineering 2, No. 2, 173–189 (June 1990).

[17] E.F. Miller and G.E. Lindamood, Structured Programming: Top-Down Approach, Datamation 19, No. 12, 55–57 (December 1973).

[18] A.R. Montazemi and D.W. Conrath, The Use of Cognitive Mapping for Information Requirements Analysis, MIS Quarterly, 45–55 (March 1986).

[19] D.L. Nazareth, Issues in the verification of knowledge in rule-base systems, International Journal of Man-Machine Studies 30, 255–271 (April 1989).

[20] H.P. Newquist III, Struggling to Maintain, Al Expert 3, No. 8, 69–71 (August 1988).

[21] K. Pederson, Well Structured Knowledge Bases, Al Expert 4, No. 4, 44–55 (April 1989).

[22] D.T. Ross and K.E. Schoman, Jr., Structured Analysis for Requirements Definition, IEEE Transactions on Software Engineering SE-3, No. 1, 41–48 (January 1977).

[23] E. Soloway, J. Bachant, and K. Jensen, Assessing the Maintainability of XCON-in-RIME: Coping with the

Problems of a VERY Large Rule-Base, Proceedings of the AAAI, 824–829 (1987).

[24] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly 4, No. 4 (June 1980).

[25] W. Stevens, G. Myers, and L. Constantine, Structured Design, IBM Systems Journal 13, No. 2 115–139 (May 1974).

[26] D.A. Waterman, A Guide to Expert Systems (Addison-Wesley, Reading, MA, 1985).
