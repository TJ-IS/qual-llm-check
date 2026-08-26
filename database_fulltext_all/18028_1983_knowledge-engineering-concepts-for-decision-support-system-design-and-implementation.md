---
otero_id: 18028
otero_key: "VAET873H"
title: "Knowledge engineering concepts for decision support system design and implementation"
authors: "Joyce J. Elam; John C. Henderson"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90004-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge Engineering Concepts for Decision Support System Design and Implementation \*

Joyce J. Elam

College of Business Administration, Dept. of General Business, Business - Economics Building, University of Texas, Austin, Texas 78712, USA

and

John C. Henderson

Florida State University, Talhassee, Florida 32306, USA

The design of computer-based systems that simulate expert human consulting by drawing on large amounts of task-specific knowledge has been a major research activity of applied artificial intelligence over the last ten years. Building decision support systems that incorporate aspects of this research is a promising new field. The purpose of this paper is to discuss concepts of “knowledge engineering” that are most relevant in designing and building knowledge-based decision support systems.

Keywords: Decision Support Systems, Knowledge Representation Schemes, Artificial Intelligence

## 1. Introduction

A major research activity of applied artificial intelligence over the last ten years has been the design of knowledge-based systems that simulate expert human consulting and problem solving. The

![](/api/attachments/VAET873H/fulltext/images/2c27ccf6027a80757ef39d622e705bb9e831c2e8aeb0fea14485c4de3109d118.jpg)

Joyce J. Elam is an Associate Professor of Information Systems in the College of Business Administration, University of Texas at Austin. She hold two degrees from the University of Texas at Austin, a B.A. in Mathematics and Ph.D. in Operations Research. Previously she was an Assistant Professor at the Wharton School, University of Pennsylvania. She has been a consultant to several organizations including a major chemical corporation and the Department of

Defense. Consulting activities have included the development of logistics decision support systems and manpower planning systems. She has published in the professional literature on the application of operation research techniques to various management problems and the development of improved tools for building decision support systems based on mathematical models.  
![](/api/attachments/VAET873H/fulltext/images/4f3fabd9153796d12fa5b9ee2a748ce07f0b27a9ab337d1d9f56583d9c3a2d37.jpg)

Dr. John C. Henderson is Staff Director for the Joint Select Committee on Electronic Data Processing, Florida Legislature. While serving in this capacity he is on leave of absence from Florida State University where he is an Associate Professor of Management and Director of the Center for Information Systems Research. Prior to joining the faculty at Florida State University, he served on the faculty at The Wharton School, University of Pennsylvania and on the faculty of the

College of Business Administration at Ohio State University. Dr. Henderson's primary areas of teaching, research and consulting are in Decision Support Systems design and implementation and in strategic planning.

result of this activity has been the development of methods for acquiring and structuring expert knowledge in conjunction with the development of strategies of reasoning that apply this knowledge to unstructured and complex tasks. The extent to which this research, which has primarily focused on medical applications, can be applied in building computer-based systems that support organizational decision-making processes is a promising area of research [1,4,10]. Such systems will have the “intelligence” to interact with a user to aid in the structuring of a decision so that analytical tools can be used in generating possible solutions. These systems differ from most decision support systems which assume a predetermined underlying structure for the decision [8].

The purpose of this paper is to discuss concepts of knowledge engineering that are most relevant in designing decision support systems [6]. These concepts will now be examined.

## 1.1. Knowledge Representation Schemes

The problem-solving power exhibited by a knowledge-based system is primarily a result of the expert knowledge employed by the system. The knowledge base is thus a critical component for all systems. Different schemes have been used for representing knowledge, the most important being (1) production rule formalisms, (2) frame-like structures, and (3) graphical network structures. System characteristics (such as: usefulness, efficiency, maintenance of an evolutionary knowledge base, and support of an interactive consultant) are all impacted by the choice of a particular representation scheme.

## 12 Reasoning Mechanisms

The major purpose of knowledge-based systems is to provide advice to the user through logical deductions and judgmental reasoning. Different reasoning mechanisms are employed, though most are based on a generation-and-test framework and heuristic search techniques.

## 1.3. Explanation Models

Knowledge-based systems must be capable of supplying coherent explanations of their results to a user, rather than simply printing a set of recommendations. This is accomplished by maintaining a “line-of-reasoning” that can be given upon request.

These concepts will be illustrated by examining two knowledge-based systems, one that employs production rules and one that employs frame-like structures. The last section of this paper will discuss a knowledge-based system for organizational decision-making that is being developed using the knowledge engineering concepts described above.

## 2. Production Rule Formalisms

The MYCIN system [3] conducts a consultation with a physician-user about a patient case, constructing a line-of-reasoning leading to a diagnosis and suggested treatment plan. The primary source of domain-specific knowledge in this system is a set of approximately 200 production rules, each of the form:

## IF premise THEN action.

An example of a MYCIN rule is given in Figure 1. Each production rule represents a “chunk” of domain knowledge that is meaningful, in and of itself, to the domain specialist.

MYCIN accomplishes reasoning through a backward-chaining deduction scheme in which all applicable rules are tried. An IF condition is either immediately evaluated true or false by using data supplied by the physician-user; or is checked to see if it can be asserted by the THEN portions of other rules. If neither can be done, the user is asked for assistance. In this way, possible diagnosis are generated and then tested to see if a particular line-of-reasoning should be followed.

![](/api/attachments/VAET873H/fulltext/images/9fe09947aacb8f7e2423b03dda5bb871012770a0de5e69b5dfea9e5741072135.jpg)  
Fig. 1. MYCIN Rule.

MYCIN associates a “degree of certainty” with each rule (a number from 0.1 to 1.0) that represents the expert’s confidence in the validity of the rule. A simple model of inexact reasoning is used to accumulate the degrees of certainty of the rules used in an inference chain. This may lead to separate lines-of-reasoning-some indicating one diagnosis, some indicating others. All are used by the system as sources of knowledge in pursuing lines-of-reasoning.

MYCIN presents its line-of-reasoning in response to “Why” or “How” questions posed by the user. A user can see the rule currently being invoked or, after a consultation, be shown each rule used and the reason for using it.

MYCIN was designed to be a “see-through” system – its knowledge and reasoning processes in applying this knowledge are easily understood by the user. The use of production rules as the representation vehicle is primarily responsible for accomplishing this. Production rule formalisms also directly effect the ease by which new pieces of knowledge can be added or deleted to the knowledge base. In addition, system performance is increased since each production rule can be operationalized as a modular piece of code.

## 3. Frame-Based Schemes

A frame-based scheme for knowledge representation is employed by the Present Illness Program (PIP) [11]. The major concepts of this representation are a set of hypotheses, referred to frames, and a set of findings. Hypotheses represent conjectures about diseases or clinical states. Findings are facts supplied by a user about a patient. Prototypical findings are associated with each hypothesis and are used in supporting or refuting the hypothesis. Finding are matched with the prototypical findings of hypotheses in generating and testing diagnoses. The structure of a frame in PIP is shown in Fig. 2. The system asks for information that fills the hypothesis frames. As the frames are filled, certain hypotheses are selected for consideration. A hypothesis is considered if: (1) user-supplied findings match prototypical findings of the hypothesis; (2) any of its complimentary hypotheses (hypotheses for diseases or conditions that usually occur together) are selected for consideration; or (3) any of its competing hypotheses are selected for consideration that have similar findings that often cause a diagnostician to confuse one with the other. Once a hypothesis is under consideration, reasoning mechanisms are used to decide its merit. A hypothesis can be accepted with complete certainty if the IS-SUFFICIENT rule is satisfied. Uncertainty is incorporated into the reasoning by specifying a score function of certain conditions. A hypothesis that scores above a certain threshold level is accepted as plausible.

![](/api/attachments/VAET873H/fulltext/images/da0a4e670647b8ba778cb64f491f5f10118b9b5634ae60d43af34fd435926643.jpg)  
Fig. 2. PIP Frame.

Frame-based structures and hypothesis selection provide an alternative implementation strategy for knowledge-based systems. The major difference between the two approaches is how knowledge is conceptualized. In MYCIN, different facts are pulled together to infer some structure of interest; in particular, a disease. Connections that exist among different facts, however, are not explicitly addressed. In PIP, a context mechanism is used to focus explicitly on a structure; characteristics or facts only exist within the context of a structure. Production rules could be viewed within PIP as the heuristic procedures that are used to fill the frames.

While either the production rule or frame structure approach could be used in representing the knowledge required by either MYCIN or PIP, the use of production rules do provide clear advantages in ease of modification of the knowledge and ease of explanation.

## 4. Building Decision Support Systems

The major design principles that have emerged from the development of knowledge-based systems such, as those illustrated, are [6]:

1. Domain specific knowledge that incorporates both contextual information and procedural information is desirable.

2. The expert knowledge represented in the knowledge base cannot be used with complete certainty in reaching conclusions or recommending courses of action. Systems must have the ability to deal with this uncertainty in their reasoning mechanisms.

3. System acceptability and usability are strongly dependent upon the extent to which the system performance is natural and transparent to the user. Easily understood heuristics that can be explained to users are desirable for processing the knowledge base.

4. An English-like question generating and answering component is effective in interfacing a user with the system.

A system to support the structuring and solution of problems that arise in a production environment is currently being developed and implemented using the knowledge engineering principles described above and the Model Management System (MMS) framework described in [5]. A brief description of the representation and reasoning mechanism of the system follows.

A major objective of the MMS being developed for a production environment (MMS-P) is to facilitate the structuring of decisions so that analytical tools can be used in generating possible solutions. To accomplish this, the system accesses knowledge on general problem structuring techniques as well as knowledge specific to production. Like other knowledge-based systems, new knowledge about the problem environment (acquired through interaction with users) is captured so that it can be accessed and used at a later time.

The basic types of knowledge represented in the system include the technical problem structuring knowledge that one would expect in a management scientist. This knowledge involves information on mathematical modeling methods (linear programming models, network models, deterministic simulation models, etc.), on the parameters that define a model and distinguish it from others (constraints, decision variables, objectives, etc.), and the structural relationships between parameters. The system must also have “understanding” of the basic activities involved in the production environment (allocation, scheduling, distribution, etc.) and the way in which these activities interrelate. To support user understanding, usability, and acceptance, the system must also have an appropriate vocabulary that can be easily incorporated into the user interface. Finally, the system must have knowledge about models that have been developed for specific applications in order to support their execution and analysis. The knowledge base, thus contains four types of information: technical, application, language, and model.

More importantly, the knowledge base contains information on how all of this information is related, e.g., "How is a user-supplied description of a problem related to basic activities that are known to exist in a production environment?" and "How can the activities be structured into an appropriate model to which some algorithm can be applied?". It is this knowledge that supports the reasoning power of the system.

The knowledge base, as viewed by this system, is highly interconnected and forms a network of concepts, facts, and perceptions. Relationships that exist between these components can be used to provide the “meaning” necessary for problem structuring. A frame-like representation would provide the capability to define such concepts as production, distribution, vehicle routing, etc., while production rules would provide the capability to capture conditions, such as – if the initial state and ending state of a process are distinct and the process involves the movement of goods from one state to another, then the process is probably shipping. Neither representation would directly represent the knowledge required to determine such things as: “How is distribution different from production?” or “Is distribution a type of resource allocation problem?” Given the knowledge requirements of this system, neither production rules or frames by themselves could provide it.

Graphical representations were explored as an alternative representation vehicle. A graphical representation was attractive for two reasons: (1) the expressive power of graphs is sufficient to encode any fact or concept that is encodable in any other representation, and (2) graphical structures themselves serve as a guide for knowledge retrieval and processing. Graphical representation [7] (e.g., the well-known semantic net [9]) contain nodes and arcs, where the arcs represent relationships that can be used to provide general types of knowledge. For example, a common type of relationship is labeled “is a” and it is used to convey such knowledge as “distribution is a type of resource allocation problem.” Combining an “is a” relationship with another type of relationship “has a part of” allows the graph to define a structure in much the same way as a frame. For example, “shipping” is defined as a type of process that has an initial state, an ending state, and involves the movement of some type of good between states.” These relationships allow knowledge to be “chunked” into groups of descriptions about a concept or structure rather than put into independent descriptions or characteristics as in the production rule formalism.

The major limitation of a semantic net is inability to represent explicitly the wide range conditions that can be easily represented by production rules. Due to this restriction, an expanded graphical representation based on a semantic net, but extended to incorporate production-like rules, was used to represent the MMS-P knowledge base. This representation, called the Structured Inheritance Network (SI-Net) [2], was felt to bring together the advantages of graphical, frame, and production rule representations. A brief description of a SI-Net follows.

A SI-Net is a graphical language composed of nodes and links for describing concepts and the interrelationships between these concepts. A “concept” is defined as a set of functional roles tied together with an explicit structuring relationship. Two basic types of relationships are involved in defining a concept – “is a part of” which describes the roles in a concept, and “are structured as”, which describes how these roles are put together. It is through the structure relationship that one defines IF/THEN production-like rules.

The SI-Net also represents relationships between concepts through a fixed set of link types. These relationships include such things as “is analogous to,” “is a subconcept of,” “is the same as, except,” “is an individual,” etc. These links allow a concept to inherit all properties (roles and structure) of other concepts, and to modify, extend, or differentiate these properties as necessary. Each link as a “meaning” that provides the basis for a fixed and well-defined processing mechanism.

The knowledge-base for the MMS-P can be considered to be four distinct, but coupled SI-Nets: the technical net, the application net, the language net, and the model net. Concepts in the technical and application net are linked together in a hierarchy of less-to-more abstract concepts. The less abstract concepts relate to fundamental production activities, while the more abstract focus on problem systems, such as production/distribution/inventory. Structural conditions are used to cluster related activities into a problem system. For example, a distribution system involves both shipping and storing, where the shipment of goods from location must also involve the storing of the goods at some of the same locations.

The language net directly confronts the particular jargon, terminology, etc., associated with the organization using the MMS-P. The language net provides the capability for translating between a user's description of a concept and the system-defined label associated with the same concept. Thus, a manufacturer speaks of factories and products while the military communicates in terms of depots and spares. They both may be referring to identical problem systems and technical structures. The language net allows the system to communicate to the user in a language that is both familiar and more precise.

The knowledge base is made available to an organization via an interrogation component. This component provides the reasoning facilities for the system. The basic objectives for this component are fourfold:

1. to recall actual model instances;

2. to support the problem definition and model conceptualization process;

3. to identify necessary modifications for existing models; and

4. to initiate the actual process of model building. The attainment of these objectives is realized through an interactive stimuli/response sequence with a user. The system attempts to identify basic concepts, verify these concepts and infer potential logical structures that could be used to model the problem. Models of inexact reasoning are incorporated into this process to capture the uncertainty in structuring a problem. Further, user generated labels for concepts are captured and used to adapt the semantics of the interaction dynamically so as to become increasingly “friendly.” A more detailed explanation of the system can be found in [5].

## 5. Conclusions

Most current decision support systems are designed and built for decisions that relate to a specific problem. Each of these systems center around a single, predetermined model that a decision-maker can use to explore various problem characteristics and solutions. The purpose of this paper has been to explore the possibility of designing decision support systems that can be more “intelligent” in helping a decisionmaker structure and analyze a problem. Systems that perform similar consulting functions have been successfully implemented in such areas as medical diagnosis, speech understanding, and chemical inference. Applying the tools and technologies developed by these efforts in builing and implementing knowledge-based decision support systems is a promising new direction for decision support research.

## References

[1] R.C. Bonczek, W. Holsapple, and A. Whinston, "Computer-Based Support of Organizational Decision-Making," Decision Sciences, April, 1979.

[2] R.J. Brachman, "A Structural Paradigm for Representing Knowledge," Report No. 3605, Bolt, Beranek, and Newman, Inc. 1978.

[3] R. Davis, B. Buchanan, E. Shortliffe, "Production Rules as a Representation for a Knowledge-Based Consultation Program." Artificial Intelligence Vol. 8, 1977.

[4] John Donovan, "Database System Approach to Management Decision Support," TODS. 1, 4, 1979.

[5] J. Elam, J. Henderson and L. Miller, "Model Management Systems: An Approach to Decision Support in Complex Organizations," Proceedings of the First International Conference on Information Systems, December, 1980.

[6] E.A. Feigenbaum, "The Art of Artificial Intelligence - Themes and Case Studies of Knowledge Engineering." Proc. NCC 1978.

[7] Finuller (Ed.), Associative Networks: Representation and Use of Knowledge by Computers, Academic Press, 1979.

[8] P. Keen and Morton M. Scott, Decision Support Systems., An Organizational Perspective, Addison Wesley 1978.

[9] Ross Quilian, "Semantic Memory," Semantic Information Processing, Marvin Minsky, ed. MIT Press, 1968.

[10] E.A. Stohr and M.R. Tanniru, "A Data Base for Operation Research Models," Policy Analysis and Information Systems V4 N2, Dec. 1980.

[11] P. Szolovits and S.G. Pauker, "Categorical and Probabilistic Reasoning in Medical Diagnosis," Artificial Intelligence 11, 1978.
