---
otero_id: 16902
otero_key: "97HJAAW4"
title: "Toward representing management-domain knowledge"
authors: "Dirk Baldwin; George M. Kasper"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90093-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Toward Representing Management-domain Knowledge

Dirk BALDWIN and George M. KASPER
Texas Tech University, Lubbock, TX 79409, USA

Guidelines for the application of artificial intelligence to management-domain problems are proposed. A tutorial highlighting the strengths and weaknesses of several popular knowledge representation techniques is presented. Matching the strengths of these techniques with the requirements of different management decision-making domains provides a basis for the proposed guidelines. Management areas for which current approaches to knowledge representation provide little support are also discussed.

Keywords: Knowledge representation; Artificial intelligence; Decision support systems; Expert systems; Surface knowledge; Deep knowledge; Management decisions.

![](/api/attachments/97HJAAW4/fulltext/images/0721e8feeb2d9096d76b27b23525ffcfec1e5693791d6dea0f3c108665b8acdd.jpg)

![](/api/attachments/97HJAAW4/fulltext/images/c93e47954a192e8119731f78ec3dcff4e6610378004a7e0a6a391bada629b9e7.jpg)

Dirk Baldwin is a doctoral student in management information systems at Texas Tech University. His research interests include decision support systems, expert systems, applications of artificial intelligence to management decision making and information systems management.

George M. Kasper is Assistant Professor of Information Systems and Quantitative Sciences at Texas Tech University. He received the Ph.D. degree from the State University of New York at Buffalo. His papers have appeared in Decision Sciences, Information and Management and the Journal of Management Information Systems. His research interests include DSS design and development, expert system-aided decision making and data communications network management.

## 1. Introduction

An interest in the application of artificial intelligence (AI) to management decision making has existed for some time. Though not the first to recognize the potential decision supporting applications of AI, Keen and Scott Morton stated that AI is the subfield of computer science which offers 'the greatest potential with respect to decision making' [30, p. 39]. Despite this interest, very few management-oriented AI applications exist. Conversely, many of the best known applications of AI have been in fields such as medicine, chemistry and engineering. The current lack of AI-based management supporting systems is likely due to a combination of the difficulties associated with representing ill-defined relationships such as those found in many management decision-making domains, the lack of system design and application guidelines, and the limited interchange of knowledge between MIS and AI professionals.

The primary purpose of this paper is to suggest a set of guidelines for MIS in the application of AI. The strengths and weaknesses of several knowledge representation (KR) techniques are discussed, and the domains in which each technique is best suited are compared. Matching the strengths of these KR techniques with the needs of different management decision-making types provides a basis for the proposed guidelines. The resulting contingency model also highlights management areas for which current AI knowledge representation techniques provide little support.

The paper is divided into six sections. The next section presents background information and defines key terms. This is followed by a statement of the problem. In the fourth section various knowledge representation schemes are compared and contrasted. Based upon the MIS and management literature, section five discusses the decision support needs of different functions and at different levels of management. The proposed contingency model is also presented in this section. The paper

North-Holland
Decision Support Systems 2 (1986) 159–172 concludes with a discussion of the contingency model's implications for both AI and MIS.

## 2. Background

Perhaps the greatest advance in AI within the past fifteen years has been the recognition that intelligence does not result simply from a few general problem-solving techniques, but requires the use of knowledge specific to a problem domain [12], [15], [20], [23], [42]. Four terms are central to the development of AI tools that organize and apply domain-specific knowledge. Although there is only limited agreement on the precise definition of these terms [9], the following are consistent with those presented by a number of authors in the AI field:

Knowledge. ‘Whatever can be ascribed to an agent, such that its behavior can be computed according to the principal of rationality’ [43, p. 105].

Knowledge domain. That problem domain in which a particular chunk of knowledge facilitates effective and efficient problem solving [12], [23].

Knowledge base. That component of an AI system consisting of data structures and procedures which represent domain specific knowledge for a particular AI application [3].

Knowledge representation schemes. A general framework (or notation) used to construct a knowledge base [42], [46].

Concentrating on domain specific knowledge has facilitated research in a number of AI application areas, including expert systems [14], [15], [20], natural language systems [23], [46] and intelligent data base systems [28], [50]. Currently, the most popular of these is expert systems. This type of system uses encoded knowledge to give expert advice in a particular problem domain. Successful systems have been developed in such fields as medicine, mathematics, the natural sciences and engineering.

The MIS community has recognized the importance of AI applications in the development of Decision Support Systems (DSS). For example, Bonczek et al. [6] define a DSS as consisting of three principal components: a language system, a knowledge system and a problem-processing system. Further they state that unless the system contains some knowledge about the decision-maker's problem domain, a DSS is likely to be of little practical value [6, p. 70].

To date, the most popular use of AI techniques in DSS is for model management. The objectives of this application are to support the building, testing, execution and maintenance of MS/OR models [6], [19], [31], [38]. In addition to its model management roles, the DSS literature has proposed a number of other AI applications. These include natural language interfaces [4], expert advice [35], [48], and problem identification and alternative generation [22]. Table 1 presents many of the AI systems currently in prototype which are relevant to specific management domains.

The projected roles of AI in management domains may be more ambitious than previous AI applications. The resolution of a number of issues by both the AI and MIS community will be required to achieve these goals. A principal issue to be addressed in providing this domain-specific knowledge is how to represent knowledge [6, p.

Table 1  
AI-based Management-domain Applications.

<table><tr><td>Name</td><td>Purpose</td></tr><tr><td>TAX ADVISOR</td><td>Provides investment advice so that certain taxes are minimized [35].</td></tr><tr><td>AUDITOR</td><td>Supports an auditor in determining allowance for bad debts [35].</td></tr><tr><td>EDP AUDITOR</td><td>Assists auditors in auditing EDP systems [35].</td></tr><tr><td>TAXMAN</td><td>Evaluates the tax consequences of certain types of corporate reorganizations [34].</td></tr><tr><td>NUDGE</td><td>Schedules business meeting times and locations [24].</td></tr><tr><td>ODYSSEY</td><td>Plans business trips including the scheduling of plane flights and hotel reservations [21].</td></tr><tr><td>EPISTLE</td><td>A combination natural language and expert system, EPISTLE provides a synopsis of the meaning of correspondence, and a critique of spelling, grammar, punctuation and tone [37].</td></tr><tr><td>LADDER</td><td>An intelligent data base management system [28].</td></tr><tr><td>SYLLOG</td><td>An intelligent data base management system [50].</td></tr></table>

380] in a way that is consistent with the nature of both the problem and the decision makers that the system is designed to support.

## 3. Problem statement

AI researchers have recognized for some time that a particular KR technique works better in some problem domains than in others. For example, Stefik et al. write 'The choice of a data structure (KR technique) depends on assumptions about how the data will be used' [49, p. 167]. In addition, Barr and Feigenbaum state 'The most important consideration in examining and comparing KR schemes is the eventual use of the knowledge' [3, p. 145]. The critical problem is that no framework exists to guide the system builder in the selection of a KR technique for a particular application. Although AI researchers state that the correct selection of a KR technique for an application is a critical success factor, they have not been able to identify the selection criteria. Stefik et al. state, 'Systems with seemingly similar tasks sometimes have radically different organizations, and seemingly different tasks are sometimes performed with only a minor variation on a single organization' [49, p. 136].

From an MIS perspective, the lack of guidelines has a number of implications. First, it is difficult to determine the management applications that AI can support. A set of guidelines illustrating the capabilities of the various knowledge representation techniques would help MIS professionals perceive the potential uses of AI in an organization. Second, it is difficult to evaluate and select among existing KR techniques those best suited for a particular management domain. To build an AI system for a particular domain it is desirable to decompose the domain's problems into subtasks. If for each of these subtasks we know how to design and build an AI system, then there exists a basis for concluding that an AI system can be successfully developed to support decision making within the problem domain [12]. Further, there exists some design guidelines for the actual development of the system. To a great extent, decomposing a problem into subtasks is the responsibility of the application area. For example, the characteristics of management problems are likely better understood by MIS practitioners and researchers than AI researchers. A set of KR selection guidelines would allow MIS professionals to determine how subtasks can be supported.

An additional benefit of matching KR capabilities to management-domain requirements is that it promotes an interchange of knowledge between MIS and AI professionals. From a conceptual perspective, DSS and AI seem to differ in focus. At the extremes, AI has focused on systems that replace the decision maker in a specific task, while DSS has emphasized systems that supply tools to support a decision maker in large problem domains. Not only is it important for MIS professionals to understand the capabilities of AI, it is essential that AI researchers understand the difficulties of the management domain. A merging of the ideas of the MIS and AI disciplines may result in a more effective management support system. The objective of this paper is to associate management decision-types with knowledge representation techniques so as to both address some of the above identified application problems and promote the development of better management decision support tools.

## 4. Knowledge representation

Our definition and corresponding analysis of knowledge representation techniques is at the knowledge level [43]. That is, we are not interested in how a KR technique is implemented, rather we are concerned with the kinds of knowledge that the technique can represent. Analysis at this level points out some fundamental tradeoffs in knowledge representation [32]. These tradeoffs will serve as the basis for the KR technique comparisons. There are two advantages to the knowledge level view. First, the analysis is applicable to a variety of algorithms. Second, it encourages well-defined KR technique descriptions. A major problem with past KR technique comparisons is that the descriptions of the techniques were so general that it could be shown that one technique might be converted to another [18], [27], [45].

A prime indication of an AI system's intelligence is its ability to solve problems [33], [44]. Applying this to Newell's previously cited definition of knowledge provides a basis for determining the knowledge level requirements of a knowledge base. We can now ask the question, 'What are the types of knowledge necessary to ascribe to an agent so that it is capable of rationally solving problems?'

The AI literature has answered this question by identifying two general types of knowledge. Referred to as 'what' knowledge, this is information about the facts, concepts and relationships of a particular problem domain [33], [53]. The second type of knowledge, 'how to' knowledge, is information about how to reason with the facts, concepts and relationships [33], [53]. Clearly both types of knowledge are required to solve problems. However, the kind of 'what' and 'how to' knowledge the system can represent has a direct impact upon the types of problems the system can solve.

The first tradeoff, involving both ‘what’ and ‘how to’ knowledge, results from the distinction made between surface and deep knowledge [13], [14], [26], [36]. Surface knowledge combines ‘what’ and ‘how to’ knowledge into problem-solving heuristics. An example of surface knowledge is the statement, ‘If we run out of part No. 311, see if we have part No. 312’. Implied in this statement is a mixture of ‘what’ knowledge indicating that part No. 311 and part No. 312 are similar and the ‘how to’ knowledge that when items are similar they may be interchanged. The use of surface knowledge in problem solving is a common trait of experts [47], [48], and is the most popular form of knowledge contain in expert systems [14], [26].

In contrast, deep knowledge is the basic knowledge from which experts derive heuristics. This basic knowledge may consist of causal relationships, mathematical laws, et cetera. To support deep knowledge, the system must maintain a clear distinction between different categories of 'what' and 'how to' knowledge. Further, deep knowledge requires that the relationships between facts and/or concepts be explicitly defined. Returning to the parts example discussed above, a deep knowledge base would explicitly represent the attributes of both parts No. 311 and No. 312, knowledge of the items' characteristics which identify them as being similar, and the 'how to' knowledge that similar items may be substitutes.

Designers of a knowledge base must determine whether a knowledge domain should be represented as surface knowledge, deep knowledge or some combination. Although advocates of deep knowledge representation list a number of system advantages, the primary advantage is that the knowledge is not confined to problem-solving heuristics and therefore the system is capable of supporting a wider range of problems than surface systems. This advantage is especially important when the problem domain requires the solution of novel or ad hoc problems [10]. A disadvantage of deep knowledge systems is that their size and computational requirements may make them less efficient and more costly than surface systems. Many maintain that the use of problem-solving heuristics enhances a surface system's reasoning efficiency [36]. Hart [26], however, contends that surface systems cost less in simple domains, while deep systems are less expensive in complex domains. A definite advantage of surface systems is the ease with which procedural knowledge can be expressed [53]. In domains such as planning it is common to express knowledge as a set of heuristics.

In addition to whether an AI system contains deep or surface knowledge, 'how to' knowledge alone is associated with certain tradeoffs. At one extreme, a system may utilize a deductive form of reasoning based upon logic's rules of inference (to be explained later). The advantage of this type of 'how to' knowledge is that it is sound (all deductions are correct) and complete (the system is capable of inferring all conclusions that logically follow from the premises) [45], [46]. However, not all domains lend themselves to strict logic reasoning. For example, many domains are characterized by a nondeterministic environment or incomplete knowledge. In these domains the KR techniques should allow probabilities in its 'what' knowledge and be able to manipulate these probabilities with its 'how to' knowledge [46]. The system could then present a number of alternative solutions and their corresponding probabilities. Other methods of inference include inductive reasoning [11], default reasoning [5], [21], [24] and guessing [49]. The disadvantage of these methods is that the system is no longer guaranteed to be sound or complete.

Levesque [32] demonstrated a third tradeoff at the knowledge level, involving the expressive power of a KR technique and search efficiency. One of the activities performed by any reasoning system is search [44]. A problem with sequential machines is that when the domain knowledge becomes large, search can become hopelessly inefficient and a solution to the problem may not be found. This problem is aggreviated when the KR technique can express a number of types of knowledge in a variety of forms. For example, in order to allow all possible deductions, a general inference procedure is required when a KR technique permits statements to be expressed in the form: either x or y is true; x is not true; there exists some x for which $f(x)$ is true; and for all x, $f(x)$ is true. On the other hand, a KR technique which restricts the knowledge that can be expressed can utilize specialized ‘how to’ knowledge and reduce the search time.

A final criterion for selecting a KR technique is whether the knowledge is to be represented descriptively or directly. That is, knowledge can be represented in a manner similar to the way a human describes the knowledge or the knowledge can be represented so that it directly models the domain. Examples of the latter are a city map, a model and a diagram. Since direct knowledge is classified as a kind of KR technique, the advantages of direct knowledge vis-à-vis descriptive knowledge are also discussed below.

Table 2 summarizes the knowledge level trade-offs that will guide the discussion of KR techniques. The schemes considered are logic, semantic nets, procedures and production rules, frames and direct representation.

## 4.1. Logic

Many of the early knowledge representation schemes were based upon predicate logic. These schemes represent 'what' knowledge in the form of independent well-formed formulas (wffs). These wffs consist of propositions (facts) and connectives (relationships between facts). A proposition itself is made up of two parts, a predicate and a subject. For example, MANAGER(DAVIS) is a proposition consisting of the predicate MANAGER and the subject DAVIS. 'How to' knowledge consists of the rules of inference and is usually represented as some general procedure. Logic-based systems typically solve problems by constructing proofs from an initial set of stated conditions and a goal.

Table 2
Knowledge level tradeoffs.

<table><tr><td>— Deep representation vs. surface representation</td></tr><tr><td>— Deductive inference vs. alternative methods of inference (probabilistic, default, guessing, etc.)</td></tr><tr><td>— Expressive power vs. search efficiency</td></tr><tr><td>— Descriptive representation vs. direct representation</td></tr></table>

A logic system has a number of important advantages. The primary strength of logic is its expressive power [32]. For example, a wff may represent statements of the form: x and y are true (conjunction); x or y is true (disjunction); x is not true (negation); if x is true, y is true (implication); there exists at least one x for which $f(x)$ is true (existential quantification); for all x, $f(x)$ is true (universal quantification) and any combination of these statements. A second advantage of logic is that the rules of inference are sound and complete [46]. It should be noted, however, that in practice most systems modeled after logic KR do not utilize the complete set of inference rules and thus do not exhibit the completeness characteristic [46].

The expressive power of wffs and the characteristics of the rules of inference also result in a number of problems. The major problem is that the construction of a proof from some goal and initial premises may require an unreasonable amount of time [3], [6], [20], [42]. Levesque [32] points out that this weakness is not a function of present algorithms, but a function of the problem; there will never exist an algorithm which will always construct proofs in a reasonable time. This makes logic difficult to use in large domains. A further weakness of logic is that it does not represent deep knowledge. Although, 'how to' and 'what' knowledge are not combined, the symbols used to represent 'what' knowledge have no 'meaning' to the inference procedure. The general format of a proposition is $B(X, Y, Z, \ldots)$ , where $B$ can be any symbol and any number of subjects are within the parentheses. The rules of inference simply manipulate these symbols without regard to the interpretation of the symbols [46]. Further, inconsistent with the requirements of deep knowledge, questions regarding the relationship between subjects or propositions cannot be deduced. For example, if the KB contained the fact PART (MACHINE,BOLT), the rules of inference could not answer the question, 'What is the relationship between machine and bolt?'

A second set of weaknesses results from logic's strict utilization of the rules of inference. These rules permit only a deductive form of reasoning based upon the truth value of premises (initial conditions) or previously derived theorems. Default reasoning and guessing, which allow conclusions to be drawn from statements with undecided truth values, are not permitted [42], [46]. For a similar reason, probabilistic reasoning is not directly representable. Logic cannot represent wffs that are not true or false with complete certainty. To represent a degree of certainty a proposition could contain a subject expressing the confidence in the proposition. However, this approach requires additional wffs to manipulate probabilities, resulting in increased search time. If the rules of inference included a capability to manipulate probabilities, the additional wffs would not be required. For a similar reason, it is difficult to use logic in domains where propositions are true only at a certain point in time. To manipulate propositions with a time component requires a number of additional wffs, increasing the search time [46].

Although the logic KR technique has a number of disadvantages, the expressive power of the technique, the soundness and the completeness of the rules of inference, and its large exposure in a number of disciplines make logic a good benchmark for comparing other KR techniques [9], [43]. The remaining analysis will therefore use logic to facilitate the KR comparisons.

## 4.2. Semantic networks

As previously mentioned, Levesque [32] convincingly argues that there is a tradeoff between the expressive power of a KR technique and its search efficiency. Therefore, one way to reduce logic's search time is to restrict the format of the wffs. In terms of logic, the semantic network and some forms of the frame KR technique can be described as unary and binary propositions, utilizing a restricted set of predicates [32], [45]. Predicates common to semantic networks include: ISA, IS-SPECIALIZATION-OF, CAUSES, and HAS-PART [3], [8], [18], [42], [52]. For example, a typical proposition may be HAS-PART(CAR, BATTERY). Semantic networks and frames also have a number of other restrictions on the format of wffs. For instance, existential quantification, negation or disjunction may not be allowed. The important point is that there must be enough restrictions on the 'what' knowledge so that specialized 'how to' knowledge can be developed which reasons more efficiently than the rules of inference. Since a semantic network contains only unary and binary propositions, it is common to represent it in terms of a graph. The arcs in the graph are labeled according to the appropriate predicate. The 'how to' knowledge then utilizes specialized procedures corresponding to the arc labels or a graph search technique to reason about a problem [3], [32], [46].

In addition to increasing the search efficiency, a semantic network has a number of other strengths. A basic strength is its natural ability to represent deep knowledge. All arcs are labeled so that the relationships between facts and/or concepts are explicitly defined. Further, graph search techniques allow questions of the form 'What is the relationship between $A$ and $B$ ?' Other advantages result from the relaxing of 'how to' knowledge restrictions. Default reasoning, probabilistic reasoning as well as logical deductive reasoning are supported [3], [8], [18], [42], [46].

Restrictions on the expressiveness of 'what' knowledge, the lack of 'how to' knowledge standards and the representation of deep knowledge also present problems for semantic networks. Restricted expressiveness is an obvious disadvantage. The lack of 'how to' standards means that semantic network reasoning is not necessarily sound and complete. Finally, since a semantic network does not represent surface knowledge, it may be difficult to use in domains where knowledge is naturally expressed in terms of procedures. A problem which requires the system to plan a sequence of steps is probably not suited to a semantic network representation.

## 4.3. Production rules and procedures

Logic and semantic networks are characterized by a clear separation between 'how to' and 'what' knowledge. An alternative philosophy is to combine these two types of knowledge into a single representation [3], [53]. Since the combination of 'what' and 'how to' knowledge results in problem-solving heuristics, systems based upon this philosophy are classified as surface systems. At the extreme, the KR technique may consist of subroutines that contain knowledge on how to proceed in a specified situation; this technique is known as procedural. However, due to the advantages of modular knowledge representation, most surface systems are characterized by production rules.

A production rule system consists of a rule base, an inference engine and a data base [3], [16], [20], [51]. The rule base consists of independent rules of the form IF $\langle$ situation $\rangle$ THEN $\langle$ action $\rangle$ . In general, these rules represent heuristics for solving a particular class of problems. The inference engine contains ‘how to’ knowledge about a strategy for selecting a particular production rule to fire. For a rule to be a candidate for firing, the $\langle$ situation $\rangle$ component of the rule must match the data base. The data base represents the current state of the problem-solving process. If a match occurs, the data base is modified according to the specifications of the $\langle$ action $\rangle$ component. The problem-solving process consists of selecting and firing rules until some part of the data base matches the goal the system is attempting to achieve.

Since the distinguishing characteristic of production rule and procedural systems is their natural ability to represent surface knowledge, their strengths and weaknesses are primarily those already mentioned for surface systems. In summary, these systems can be relatively efficient in many domains and are especially adaptable to problems naturally expressed in terms of procedures (e.g., planning knowledge). The major limitation of the techniques is that they are not well suited to environments which require ad hoc problem solving.

Other advantages of production rule and procedural KR techniques result from their ability to utilize multiple forms of 'how to' knowledge. These systems are capable of probabilistic reasoning, default reasoning and guessing [15], [42], [46], [49]. However, like semantic networks, the reasoning is not guaranteed to be sound or complete.

A special problem of production rule systems is inefficiency in large domains [3]. Since the knowledge of production rule systems is represented in a modular format, the search efficiency is critically dependent upon the inference engine's ability to select the correct rules to fire. When the knowledge domain is large, the probability of selecting the correct rule decreases. Therefore, the inference engine's inefficiency may negate the efficiency gained by using problem-solving heuristics.

## 4.4. Frames

So far two knowledge representation techniques have been presented as modifications or restrictions to predicate logic; each technique has certain strengths and weaknesses. A natural method of retaining the strengths and reducing the weaknesses of procedures and production rules, and semantic networks is to combine them [2], [12]. The frame KR technique supports such a combination [39], [53]. Conceptually, knowledge in a frame system is viewed in terms of concepts such as objects or stereotypical situations, attributes of concepts, relations between concepts and 'how to' procedures. Like a semantic network, the concept's attributes and relationships between concepts can be defined as binary and unary propositions in predicate logic. Also as in a semantic network, the propositions use only a restricted set of allowable predicates. Further, some connectives and quantifiers may not be allowed [32]. Similar to procedural and production rule systems, frames incorporate heuristic knowledge about how to obtain a particular concept's attribute values. In frame terminology, a concept is represented by a structure called a frame, an attribute is represented by a labeled slot embedded in the frame, and relationships between concepts are represented as links between frames. Typically, frames are organized into a generalization hierarchy with 'ISA' links between the general and specific concepts. 'How to' knowledge is of two types. One type reasons with the nonprocedural knowledge of the frames. The other type consists of sets of production rules or procedures attached to the slots.

If the knowledge of a domain can be organized into concepts and attributes, a frame system offers at least three advantages. First, relative to other KR techniques, a frame may be searched more efficiently [2], [3], [5], [42]. Similar to semantic networks, links between frames guide the reasoning process. Once a relevant frame has been found, procedures specific to the frame control the reasoning process. Second, 'how to' knowledge is not constrained to any predefined type; therefore, probabilistic reasoning, guessing, and default reasoning can be supported [3], [5], [27], [39], [42]. In addition, the representation of stereotypical concepts allows various types of reasoning based upon the goodness of fit between the current situation and the frame [46]. Finally, a frame represents some deep knowledge [2]. The relationship between frames and the relationship between a slot and a frame is explicit. The 'how to' knowledge that reasons with these relationships is separate from the 'what' knowledge. One aspect of a frame which may not be deep is the procedures attached to the slots. The ability to represent both surface and deep knowledge is a significant advantage of this technique. The primary problem with the frame KR scheme is that some knowledge cannot be easily implemented in terms of concepts and attributes. Further, frame systems are probably more difficult to implement then are other KR techniques.

## 4.5. Direct representation

The KR techniques presented so far represent a descriptive type of knowledge. That is, the knowledge represented corresponds to a human's description of the domain. Alternatively, a knowledge base could be formulated to directly represent the physical domain. In these cases there is a one-to-one correspondence between the representational data structure in the knowledge base and the relations in the actual domain. For instance, the distance between cities on a map must correspond to the actual distance between the two cities [3]. 'How to' knowledge for direct representation systems usually consists of two types. One type is responsible for simply interpreting the existing representational structure; this type of knowledge is similar to a human's sense of sight. The second type must be able to change the structure in a manner similar to a simulation.

It is obvious that there are many cases where a direct representation does not exist. However, when a direct representation does exist, there are some advantages to using this technique. First, for many questions reasoning efficiency may be enhanced. Rather than performing a long inference routine to determine if a particular property is true, the 'how to' knowledge simply looks at the model. Second, a direct representation supports deep knowledge. Therefore, the system has the potential to reason about a variety of related problems. The requirements of a deep representation are met by the clear separation between the 'what' knowledge of the structure and 'how to' knowledge. Further, the ability to simulate the real world is evidence of the deepest form of knowledge [26]. In fact, one of the disadvantages of direct representation is that it is totally dependent upon deep knowledge. Many times simulation is a very inefficient method of reasoning [3]. Also, since the system directly represents an entire portion of the domain, it may be difficult to perform some forms of probabilistic reasoning. Probabilistic reasoning would require that several models of the domain be maintained, each with a corresponding probability of being true.

Table 3  
A Comparison of KR Techniques.

<table><tr><td>Scheme</td><td>Deep or surfacea</td><td>Method of inference</td><td>Expressive power</td><td>Search efficiency</td><td>Direct or descriptive</td></tr><tr><td>Logic</td><td>-</td><td>Deductive</td><td>Excellent</td><td>Poor</td><td>Descriptive</td></tr><tr><td>Semantic net</td><td>Deep</td><td>Many types</td><td>Average</td><td>Average</td><td>Descriptive</td></tr><tr><td>Production rule</td><td>Surface</td><td>Many types</td><td>Average</td><td>Below average</td><td>Descriptive</td></tr><tr><td>Procedural</td><td>Surface</td><td>Many types</td><td>Average</td><td>Excellent</td><td>Descriptive</td></tr><tr><td>Frames</td><td>Deep and surface</td><td>Many types</td><td>Average</td><td>Good</td><td>Descriptive</td></tr><tr><td>Direct</td><td>Deep</td><td>Simulation</td><td>Below average</td><td>Average</td><td>Direct</td></tr></table>

## 4.6. Hybrid schemes

Since knowledge representation is one of the most active areas of AI research, it is impossible to present all of the existing techniques. However, most other KR schemes are modifications or hybrids of the techniques presented. By using the knowledge level tradeoffs and comparing a particular KR scheme to the ones presented, the strengths and weaknesses of alternative techniques can be determined. The strengths and weaknesses of the techniques presented are summarized in table 3.

## 5. Matching KR techniques to organizational domains

A fundamental tenant of management and MIS research is that organizational problems can be characterized along several dimensions. Gorry and Scott Morton [25] identified these dimensions as degree of problem structure and management level. Similarly, Mintzberg [40] described organizational problems in terms of organizational role, degree of problem familiarity and the degree of problem impact. Since the choice of KR technique is dependent upon problem characteristics, and organizations are subject to a number of problem types, it is likely that AI systems in business domains will require a variety of KR techniques.

The management side of the proposed guidelines is based upon Mintzberg's organizational view. This view conceptualizes the typical business as an organization consisting of five parts: (1) the operating core, (2) the strategic apex, (3) the middle line management, (4) the technostructure, and (5) the support staff [40]. These parts are depicted as a pyramid in fig. 1.

The base of the pyramid is the operating core, whose function is to perform the tasks directly related to the production of the organization's goods and services. Higher in the pyramid is the middle line management and strategic apex. The function of these two parts is to supervise the parts lower in the pyramid, to manage boundary conditions and to formulate strategy. A major goal of the strategic apex and middle line management is to protect the operating core from the uncertainties and the dynamic nature of the organization's environment. Since the operating core is the basic component that produces products to satisfy the organization's mission, it is critical that this component run efficiently. Similarly, the technostructure and the support staff attempt to provide a buffer between the operating core and the environment. For example, the role of the technostructure is to standardize certain activities in the organization and to provide advice to management regarding the organization's compatibility with its environment. Examples of departments making up the technostructure include operations research, strategic planning and production scheduling. The support staff also provides a buffer from the environment. They perform activities normally obtained from sources outside the organization. For example, an organization may have its own lawyers and public relations officers so that it does not have to rely on entities outside the organization to perform these activities. For our purposes, the technostructure and support staff will be combined into a single group called specialists.

![](/api/attachments/97HJAAW4/fulltext/images/746fffc233d2a5585ec2f17c7d5620584c862f9b6db4039adbc93d5efb4542ff.jpg)  
Fig. 1. The five basic parts of organizations [40, p. 20].

Mintzberg [40] uses his organizational model and the roles of each of the parts to define four decision categories: operating decisions, coordinative decisions, exception decisions and strategic decisions. Each of these decision categories is described below and its supporting KR technique discussed. A key assumption of our proposed model is that the general characteristics of the decision category will tend to influence the properties of knowledge utilized to support decision making within that category. The limitation of this assumption is that this model cannot be used as the sole determinant for selecting a KR technique for a particular application. The 'optimal' KR technique is critically dependent upon the specific task the system is to perform. For example, choices such as learning vs. nonlearning, expert advice vs. data retrieval and the type of explanation capability needed, all influence the choice of KR technique. Therefore, any KR scheme might be used within any decision category. Our model is based on generalities and tendencies. Once a specific application is analyzed in detail, however, careful use of the arguments in this paper may guide KR technique selection.

## 5.1. Operating decisions

Operating decisions are decisions resulting from fairly well established routines or guidelines. The individual making this type of decision is so familiar with the problem type that problem recognition is immediate. Further, the nature of the solution is predefined. Mintzberg states that this type of decision making utilizes rules such as 'if $a$ , do $x'$ ; 'if $b$ , do $y'$ [40, p. 59].

Operating decisions are made primarily by the operating core and the specialists. Operating core decisions are routine primarily because of the standards and policies set forth by the operating core's supervisors. For example, a warehouse clerk may be given a precise routine to handle delivery shortages. An expert system for an operating decision by the operating core could potentially replace the decision maker by encoding the rules and procedures the decision maker follows. Since these decisions are based upon rules and procedures, the system would represent surface knowledge. Further, the standardization of jobs and the division of labor at the operating core make each decision-maker's domain relatively small (compared to other management domains), so that search is less of a problem in this domain as compared to other management domains. Finally, routines are so standardized at this level that advanced inference procedures would most likely not be required (although default reasoning may be desirable). Based upon these generalities, a procedural or production rule system appears best suited to this domain.

A system designed to support operating decisions by specialists would be more complex. In fact, a justification for classifying some specialist decisions as operating decisions is required. First, as specialists, the decision maker has become an expert at performing a particular activity. In the process of becoming an expert, heuristics are formed which allow the specialists to view a large domain of problems as 'routine.' Second, any problem referred to a specialist is in a sense predefined. That is, the problem has been recognized as appropriate for the specialist's expertise and the nature of the possible results is thus predetermined. Therefore, many specialists' problems utilize heuristics or procedures, require little problem recognition and the nature of the solution is predefined – precisely the requirements of an operating decision. These characteristics are very similar to the characteristics of problems that current expert systems attempt to support [17, p. 412]. This commonality has promoted expert system development in specialized business domains (see table 1).

As in all expert systems, the ‘optimal’ KR technique to support operating decisions made by specialists is dependent upon the task. However, some general conclusions can be drawn. First, since operating decisions are based on heuristics, it is likely that these systems will contain surface knowledge. Second, inference procedures such as probabilistic reasoning, default reasoning or guessing may be required. Many specialists must take into account the elements of the business environment. This environment is nondeterministic and dynamic, potentially forcing the system to utilize more advanced reasoning. Third, the size of the domain is typically larger than that of the operating core so that search may be a problem. Finally, since specialists use heuristics to perform a limited number of tasks, expert systems could potentially replace the specialist. Based on these contentions, production rules and procedures seem well suited for this domain. However KR technique selection should take into account the specific requirements of the task.

## 5.2. Coordinative decisions

Coordinative decisions guide and coordinate the operating core. Examples of these decisions are budgeting, scheduling and man-power planning. The decisions are typically re-occurring and can be quite routine. They are distinguished from operating core's operating decisions in three areas. First, the decisions require interpersonal communication [25]. Information can be obtained from the strategic apex, specialists and the operating core. Second, many of these decisions take into account factors in the external environment (e.g., forecasts of inflation). Third, there are a larger number of factors to consider. Typically, these decisions are made by middle line management or the technostructure. However, the strategic apex may also make some of the more critical of these decisions.

Coordinative decision making appears to provide a good opportunity for building expert systems that support, rather than replace the decision maker. The need for interpersonal communication and human judgement makes it difficult to computerize the entire decision process. For example, budgeting may result in a debate among the participants. The final budgeting decisions are based upon these debates. It is difficult to imagine managers accepting a budget derived solely by the computer. Yet, since aspects of the decision are routine, selected parts of the decision process might be computerized. For example, a system which forecasts the environment would help the budgeting process, and a system which finds conflicts in a schedule would help the scheduling process. A system with separate knowledge sources, each with surface knowledge on how to accomplish a particular task would be useful in this type of environment. The decision maker could call on the knowledge sources as needed. A frame KR technique meets these requirements. Each frame could represent a separate knowledge source. An advantage of this type of knowledge representation is that knowledge is partitioned, potentially reducing any search problems. In addition, the deep knowledge in frames would also support some ad hoc queries. Finally, frames would allow probabilistic and default reasoning. This type of reasoning is required whenever a decision is influenced by the uncertainty of the business environment.

## 5.3. Exception decisions

Exception decisions are made on an ad hoc basis but do not impact a significant proportion of the organization. They are nonroutine and therefore there are few heuristics for solving these problems. Further, the problem requires recognition and diagnosis and the solution may need to be customized. A production manager may experience this type of problem when a new product is introduced. The manager must determine how to accommodate production of the product. The solution to this type of problem requires intuition [29] and communication with other departments [41]. In addition, Ackoff [1] advocates a planning technique which attempts to solve a number of such problems simultaneously.

Since heuristics cannot be used to solve exception decisions, surface knowledge representation, alone, cannot be used to support these decisions. Deep knowledge is desirable. In order to represent deep knowledge, however, such knowledge must be known. One domain especially useful to middle line management, which could be represented as deep knowledge, involves the functions of the operating core. For example, an assembly line could be represented with direct representation or a causation semantic network. This knowledge base could not solve the exception problem, but could answer ad hoc queries about relationships between parts of the line, help diagnose problems and/or show the impact of management's alternative solutions. One problem is that the higher the management position, the larger the knowledge domain and more severe the search problem. In addition, the need to model the external environment increases with higher positions in the organization. To some extent, the cause-and-effect relationships in the external environment could be represented as deep knowledge, but in a large number of cases these relationships may not be known. Finally, it may be desirable to give the decision maker access to various specialists' knowledge. This knowledge could provide the decision maker with information to consider during the decision process. In this case, a frame-based system could provide both deep knowledge and represent the heuristic knowledge of the specialist.

## 5.4. Strategic decisions

Like exception decisions, strategic decisions are ad hoc. However, unlike exception decisions, they have a significant impact on the organization. These decisions are the least routine in all phases of the decision-making process, including problem recognition and diagnosis. Frequently, these decisions require creative solutions which can take years to develop. Because of the importance of strategic decisions to the entire organization, many people are involved and political motives may delay the decision process [41]. Examples of these decisions are merger decisions, reaction to foreign competition and R&D budgeting.

There are significant problems with attempting to build an AI system for strategic support. Since the decisions are ad hoc, deep knowledge representation is desirable. But at this level, in a number of cases, deep knowledge is not known. The lack of reliable economic models is evidence of the difficulty of modeling environmental variables. Further, even if a deep model could be developed, it would be so large that there would be severe search problems. An AI-based system at this level must be strictly a support tool. Based upon a manager's request, such a system might access either surface or representable deep knowledge. One possibility is to utilize separate knowledge sources so that the inference procedure is confined to a small packet of knowledge, reducing the system's search time. A particular knowledge source may consist of any one of the KR techniques. The sources may also be connected by arcs similar to semantic nets or frames. In any case, an AI system for strategic management should give access to various sources of knowledge capable of providing useful information so that the user can derive his/her own solution.

## 6. Implications of the model

Table 4 summarizes the proposed contingency model. The purpose of the model is to suggest that the choice of KR technique and function of the system are influenced by the type of problem the system is to support. The model assumes that the major purpose of the knowledge base is to provide information to managers to support decision making. Further this information is stored either explicitly or implicitly in the knowledge base. Despite these generalizations, characteristics of the specific task(s) the system is to perform must guide the KR technique selection process.

The model and above discussion have some important implications. First, no current single KR technique is optimal for all business problems. Second, companies developing AI systems for management should have access to a number of KR techniques. Third, the utilization of a number of KR techniques in a single system should be explored and the implementation problems examined. Fourth, AI support for coordinative decisions appears promising. Current work seems exclusively concentrated on specialist operating decisions. Finally, more research on AI systems designed to support decision making, rather than replace decision makers, is required. A system capable of joint problem solving, combining the strengths of a human with those of a computer seems necessary for solving a large number of managerial problems.

## References

[1] Ackoff, R.L., Resurrecting the future of operational research, Journal of the Operational Research Society, 30, No. 3 (1979) 189–199.

[2] Aikins, J.S., Prototypical knowledge for expert systems, Artificial Intelligence 20, No. 2 (1983) 163–210.

[3] Barr, A., and E.A. Feigenbaum, The handbook of artificial intelligence, Kaufman, Los Altos, CA (1981).

[4] Blanning, R.W., Natural language query processing for

The Influence of Management-domain on KR Technique Selection.

<table><tr><td>Decision type</td><td>Function of system</td><td>Likely KR technique</td></tr><tr><td>Operating</td><td>Replace decision maker</td><td>Production rules and procedures</td></tr><tr><td>Coordinative</td><td>Support decision maker</td><td>Frames and semantic nets</td></tr><tr><td>Exception</td><td>Support decision maker</td><td>Frames, semantic nets and direct</td></tr><tr><td>Strategic</td><td>Support decision maker</td><td>Combination of techniques</td></tr></table>

model management, Working paper, Owen Graduate School of Management, Vanderbilt University (1983).

[5] Bobrow, D.G., and T. Winograd, An overview of KRL, a knowledge representation language, Cognitive Science 1, No. 1 (1977) 3–46.

[6] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of decision support systems, Academic Press, New York (1981).

[7] Brachman, R., What IS-A is and isn't: An analysis of taxonomic links in semantic networks, IEEE Computer 16, No. 10 (1983) 30–36.

[8] Brachman, R., What's in a concept: Structural foundations for semantic networks, International Journal of Man–Machine Studies 9, No. 2 (1977) 127–152.

[9] Brachman, R., and B. Smith, Special issue on knowledge representation, SIGART Newsletter 70 (1980).

[10] Brown, J.S., The low road, the middle road and the high road, in: P.H. Winston and K.A. Prendergast, eds., The AI business MIT Press, Cambridge, MA (1984) 81–90.

[11] Buchanan, B.G., and T.M. Mitchell, Model-directed learning of production rules, in: D.A. Waterman and F. Hayes-Roth, eds., Pattern directed inference systems, Academic Press, New York (1978) 297–312.

[12] Chandrasekaran, B., Expert systems: Matching techniques to tasks, in: W. Reitman, ed., Artificial intelligence applications for business, Ablex, Norwood, NJ (1984) 41–85.

[13] Chandrasekaran, B., and S. Mittal, Deep versus compiled knowledge approaches to diagnostic problem-solving, International Journal of Man–Machine Studies 19, No. 5 (1983) 425–436.

[14] Davis, R., Expert systems: Where are we? And where do we go from here? AI Magazine 3, No. 2 (1982) 3–22.

[15] Davis, R., B. Buchanan and E. Shortliffe, Production rules as a representation for a knowledge-based consultation program, Artificial Intelligence 8, No. 1 (1977) 15–45.

[16] Davis, R., and J. King, An overview of production systems, in: E.W. Elcock and Donald Michie, eds., Machine intelligence 8, Wiley, New York (1977) 300–332.

[17] Davis, R., and D.B. Lenat, Knowledge-based systems in artificial intelligence, McGraw-Hill, New York (1982).

[18] Duda, R.O., P.E. Hart, N.J. Nilsson and G.L. Sutherland, Semantic network representations in rule-based inference systems, in: D.A. Waterman and F. Hayes-Roth, eds., Pattern directed inference systems, Academic Press, New York (1978) 203–221.

[19] Elam, J.J., J.C. Henderson and L.W. Miller, Model management systems: An approach to decision support in complex organizations, Proceedings of the First International Conference on Information Systems (1980) 98–110.

[20] Feigenbaum, E.A., Themes and case studies of knowledge engineering, in: D. Michie, ed., Expert systems in the micro electronic age, Edinburgh University Press, Edinburgh, (1979) 3–25.

[21] Fikes, R.E., Odyssey: A knowledge based assistant, Artificial Intelligence 16, No. 3 (1981) 331–361.

[22] Ginzberg, M.J., and E.A. Stohr, Decision support systems: Issues and perspectives, in: M.J. Ginzberg, W. Reitman and E.A. Stohr, eds., Decision support systems, North-Holland, New York (1982) 9–27.

[23] Goldstein, I., and S. Papert, Artificial intelligence, lan-

guage and the study of knowledge, Cognitive Science 1, No. 1 (1977) 84–123.

[24] Goldstein, I.P., and R.B. Roberts, Nudge, a knowledge-based scheduling program, The Fifth International Joint Conference on Artificial Intelligence (1977) 257–263.

[25] Gorry, G.A., and M.S. Scott Morton, A framework for management information systems, Sloan Management Review 13, No. 1 (1971) 55–70.

[26] Hart, P.E., Direction for AI in the eighties, SIGART Newsletter 79 (1982) 11–16.

[27] Hayes, P.J., The logic of frames, in: B. Meltzer, ed., Frame conceptions and text understanding, Walter de Gruyter, Berlin (1979) 46–61, also in: B.L. Webber and N.J. Nilsson, eds., Readings in artificial intelligence, Tioga, Palo Alto, CA (1981) 451–458.

[28] Hendrix, G.G. et al., Developing a natural language interface to complex data, ACM Transactions on Database Systems 3, No. 2 (1978) 105–147.

[29] Isenberg, D.J., How senior managers think, Harvard Business Review 6 (1984) 81–90.

[30] Keen, P.G.W., and M.S. Scott Morton, Decision support systems: An organizational perspective, Addison-Wesley, Reading, MA (1978).

[31] Konsynski, B., and D. Dolk, Knowledge abstractions in model management, DSS-82 Transactions (1982) 187–202.

[32] Levesque, H.J., A fundamental tradeoff in knowledge representation and reasoning, Fairchild Technical Report 658 (1984).

[33] McCarthy, J., and P. Hayes, Some philosophical problems from the standpoint of artificial intelligence, in: B. Meltzer and D. Michie, eds., Machine intelligence 4, Edinburgh University Press, Edinburgh, (1969) 463–502, also in: B.L. Webber and N.J. Nilsson, eds., Readings in artificial intelligence, Tioga, Palo Alto, CA (1981) 431–450.

[34] McCarty, L.T., N.S. Sridharan and B.C. Sangster, The implementation of TAXMAN II: An experiment in artificial intelligence and legal reasoning, Report 154, Rutgers University (1979).

[35] Michaelson, D., and D. Michie, Expert systems in business, Datamation (1983) 240–246.

[36] Michie, D., High-road and low-road programs, AI Magazine 3, No. 1 (1981, 1982) 21–22.

[37] Miller, L.A., Project EPISTLE: A system for the automatic analysis of business correspondence, Proceedings of the First Annual National Conference on Artificial Intelligence (1980) 280–282.

[38] Minch, R.P. and J.R. Burns, Conceptual design of decision support systems utilizing management science models, IEEE Transactions on Systems, Man and Cybernetics SMC-13, No. 4 (1983) 549–557.

[39] Minsky, M., A framework for representing knowledge, in: P. Winston, ed., The psychology of computer vision, McGraw-Hill, New York (1975) 211–276.

[40] Mintzberg, H., The structuring of organizations, Prentice-Hall, Englewood Cliffs, NJ (1979).

[41] Mintzberg, H., D. Raisinghani and A. Theoret, The structure of unstructured decision processes, Administrative Science Quarterly 21, No. 2 (1976) 246–275.

[42] Mylopoulos, J., An overview of knowledge representation, SIGART Newsletter 74 (1981) 5–12.

[43] Newell, A., The knowledge level, Artificial Intelligence 18, No. 1 (1982) 87–127.

[44] Newell, A., and H.A. Simon, Computer science as empirical inquiry: Symbols and search, Communications of the ACM 19, No. 3 (1976) 113–126.

[45] Nilsson, Nils J., Principles of artificial intelligence, Tioga, Palo Alto, CA (1980).

[46] Rich, E., Artificial intelligence, McGraw-Hill, New York (1983).

[47] Sage, A.P., Behavioral and organizational considerations in the design of information systems and processes for planning and decision support, IEEE Transactions on Systems, Man and Cybernetics SMC-11, No. 9 (1981) 640–678.

[48] Sage, A.P., and A. Lagomasino, Knowledge representation and interpretation in decision support systems, Proceedings of the International Conference on Cybernetics and Society (1982) 658–662.

[49] Stefik, M. et al., The organization of expert systems, A tutorial, Artificial Intelligence 18, No. 2 (1982) 135–173.

[50] Walker, A., Databases, expert systems, and PROLOG, in: W. Reitman, ed., Artificial intelligence applications for business, Ablex, Norwood, NJ (1983) 87–109.

[51] Waterman D.A., and F. Hayes-Roth, An overview of pattern-directed inference system, in: D.A. Waterman and F. Hayes-Roth, eds., Pattern directed inference systems, Academic Press, New York (1978) 3–22.

[52] Weiss, S., C.A. Kulikowski and A. Safir, Glaucoma consultation by computer, Computers in Biology and Medicine 8, No. 1 (1978) 25–40.

[53] Winograd, T., Frame representation and the declarative/procedural controversy, in: D.G. Bobrow and A. Collins, eds., Representation and understanding, Academic Press, New York (1975) 185–210.
