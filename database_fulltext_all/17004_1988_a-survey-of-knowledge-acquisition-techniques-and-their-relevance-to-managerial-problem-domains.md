---
otero_id: 17004
otero_key: "8WFX8XHM"
title: "A survey of knowledge acquisition techniques and their relevance to managerial problem domains"
authors: "Jungduck Kim; James F. Courtney"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90016-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Survey of Knowledge Acquisition Techniques and Their Relevance to Managerial Problem Domains

Jungduck KIM and James F. COURTNEY
Business Analysis and Research, College of Business Administration, Texas A&M University, College Station, TX 77843-4217, USA

A conceptual contingency model matching the characteristics of knowledge acquisition (KA) methodologies to several decision types is proposed. KA methodologies are divided into three categories: knowledge engineer-driven, expert-driven, and machine-driven. To evaluate current KA methodologies, a framework is proposed by addressing the nature of knowledge and problem domains. Different methodologies in each category are described and evaluated for their ability to support various kinds of problem domain and the types of knowledge they are designed to elicit. A contingency model mapping these methodologies to Mintzberg's managerial decision categories is developed. Implications of the proposed model and future research directions are addressed.

Keywords: Knowledge Acquisition, Knowledge Elicitation, Artificial Intelligence, Knowledge-based Decision Support Systems, Types of Knowledge, Management Decisions.

## 1. Introduction

One of the most difficult and time-consuming activities in constructing a managerially-oriented knowledge-based DSS is the process of knowledge acquisition (KA). KA is the process of gathering knowledge about a domain, usually from an expert, and incorporating it into a computer program. This is a part of the knowledge-engineering process, which includes defining a problem, designing an architecture, building a knowledge base, and testing and refining the program [30]. If it is true that the power of an intelligent program is primarily a function of the quality and completeness of the knowledge base, then extracting and formalizing expert knowledge is the critical ‘bottleneck’ in building knowledge-based systems [18].

Since the problem domain of management is wider and shallower than that of most expert systems [16], it is quite natural to ask whether existing KA methods are appropriate for acquiring knowledge necessary in building knowledge-based DSS in managerial domains, where many of the tasks tend to be fairly open-ended and nonrepetitive. Answering this question requires addressing the following, more fundamental questions:

![](/api/attachments/8WFX8XHM/fulltext/images/5a3afb9919235ac14fcafc437de73e08c5b0bdbbed143a73d52d5ebdbef6a70b.jpg)

![](/api/attachments/8WFX8XHM/fulltext/images/070948295ce26f9f3320d284fde010000c0b755812d3ec06ba667c05b4f06be0.jpg)  
Information Systems, Database, Interfaces, the Journal of Applied Systems Analysis, the Journal of Bank Research, Socio-Economic Planning Sciences, and the Journal of Experimental Learning and Simulation. He is codeveloper of the Systems Laboratory for Information Management, a software package to support research and education in decision support systems and coauthor of the textbook Database Systems for Management. His present research interests are in knowledge-based decision support systems, GDSS, database systems, and management information systems.

(1) What is the nature of knowledge to be acquired for knowledge-based systems in management?

(2) What are current KA methodologies? How is knowledge elicited in each KA methodology?

(3) What is the most plausible approach to KA for building knowledge-based DSS for management?

The major purpose of this research is to review the literature on KA techniques, and to suggest a set of guidelines for knowledge-based DSS development. In the following section, a framework that allows us to analyze current KA methodologies is proposed by addressing the first question. Based on the framework, current KA methodologies are classified in terms of strategic level and tactical (or technical) level in the next section. The major goal is to identify what type of knowledge can be acquired and how knowledge can be elicited for each KA methodology. A conceptual contingency model is proposed by matching different KA methodologies to the several decision types within the framework proposed by Mintzberg [42]. Finally, implications of the proposed model and future research directions are addressed.

## 2. Categories of Knowledge and Problem Domain

Research on AI has recognized that the time taken and problems encountered in the KA process are dependent upon the complexity and the size of the problem domain being tackled [33]. Some methods work better for certain domains than other methods. The problem is that no framework exists to guide the system builder in the selection of a KA technique for a particular application, especially in the management domain.

On the other hand, different types of knowledge are needed to solve different types of problem [2]. Since the major objective of the KA process is to elicit knowledge from experts, it is important to identify the types of knowledge a specific KA method can elicit. Based on these perspectives, the following assertion can be derived: Selection of a KA technique is dependent upon the attributes of the problem domain and the types of knowledge associated with a specific type of decision. As an initial step to verify this assertion, this section examines the nature of knowledge to be acquired and the characteristics of the problem domain to be tackled.

## 2.1. Categories of Knowledge

Knowledge can be classified in a number of ways. It is generally recognized that there are two types of knowledge: declarative and procedural (or content and process). Declarative knowledge is information about facts, concepts, and relationships of a particular problem domain, whereas procedural knowledge is information about how to reason with the declarative knowledge [39].

Knowledge can be further classified into surface and deep knowledge. Surface knowledge combines declarative and procedural knowledge into problem-solving heuristics so that an expert can quickly solve the commonly occurring problems in a domain without going through formal reasoning. Deep knowledge generally consists of fundamental knowledge of a domain, including definitions, axioms, general laws, principles and causal relationships. Since surface systems have inherent limitations in complex problems, deep systems will be needed to handle such problems, just as a human expert might resort to 'first principles' in a similar situation. Therefore, surface and deep knowledge must be compiled to produce problem-solving structures for various tasks [11]. Most current expert systems (ES) use knowledge which fails to represent a deep understanding of a domain, but is instead based on a set of pattern-decision pairs (i.e., surface knowledge) which are found in production-rule systems [12].

Kornell [37] employed two modes of thinking, formal and narrative, to describe some of the difficulties in KA, and to provide direction in the development of KA tools. Formal thinking is concerned with constructing publicly scrutable chains of reasoning, using explicit premises and methods of combination (e.g., resolution). By using axioms and legal transformations, truth is derived. Structure comes from the composition of basic elements which are atomic. Formal thinking deals with closed worlds, in which overall models emerge from elements. Any model from formal thinking can be thought of as a Leibnitzian system which is based on formal logic and does not allow any other input from the outside world [14]. An example of formal thinking is predicate calculus.

Narrative thinking is concerned with implicit assumptions and plausible (or habitual) methods of combinations. By exploring plausibility and hypotheses, meaning is constructed. Narrative thinking seeks open, dynamic systems in which elements do not have to be self-sufficient. Any model from narrative thinking can be thought of as a Singerian system which involves continual learning and adaptation through feedback, and encompasses the whole breadth of inquiry in its attempt to authorize and control its procedures $[14]$ . Some examples of narrative thinking are metaphors and analogies.

From the discussions on the nature of knowledge, we view knowledge in terms of three related components: concepts, heuristics, and reasoning. By concepts, we mean facts, first principles, general laws, and causal relationships in a domain. Concepts can be thought of as deep knowledge. By heuristics, we mean empirical knowledge in the form of pattern-action rules which have been acquired through long experience by an expert. Heuristics can be thought of as surface knowledge. One thing to be noticed here is that the first generation of ES is based on heuristics, whereas the second generation of ES is based not only on surface knowledge, but also on deep knowledge. By reasoning, we mean meta-rules or strategies of inference which provide a general approach to problem-solving in some domain. This provides a rationale not only for arranging and processing rules or procedures, but also for choosing a class of inference strategies or a set of criteria. Different KA techniques will be analyzed in Section 3 for their ability to elicit these three types of knowledge.

## 2.2. Types of Problem Domain

The type of knowledge required to solve a problem is influenced by the degree to which the task has been formalized [20]. As a problem domain becomes better understood, formal theories or normative models can be constructed. In the absence of this formalization, problem-solving and understanding are more likely to depend on informal, intuitive, possibly unarticulated models.

The problem domain can be classified in terms of size, complexity, and degree of structure. Size of the problem domain refers to the number of elements that must be considered. Complexity of the problem domain relates to the number of interrelationships between elements. Structuredness means the degree of uncertainty about the precise nature of the relationship between elements. For example, if a problem domain contains many elements and interrelationships between these elements, and the interrelationships are too vague to describe precisely, then it can be referred to as a large, complex, and ill-structured domain. Fig. 1 shows a framework that gives us criteria (i.e., the types of knowledge and problem domain that a specific KA methodology can support) to evaluate current KA methodologies.

![](/api/attachments/8WFX8XHM/fulltext/images/182e68546a19244b040e02e06c08e5fcb8fa6e64e37f928642416bbe7fcde6bf.jpg)  
Fig. 1. A framework for knowledge acquisition.

## 3. Methodologies for Knowledge Acquisition

In the development of knowledge engineering methodologies and rapid prototyping techniques for ES, the major KA method has been based on interviewing experts and hence on linguistic transmission of expertise. Although the interviewing method is simple and often-used in the real world, it has several drawbacks as a KA method. First, it is difficult to acquire relevant and correct information. The expert often does not know how he or she makes decisions. Human interviewing processes elicit knowledge that is ‘imprecise, incomplete, and inconsistent’ [5, p. 514]. Knowledge is often subconscious, and the expert usually has not been precisely introspective about his/her work. Second, the interviewing process lacks overall structure. This lack of structure makes analysis of interviews difficult. Third, the interviewing process is time-consuming and tedious so that it is hard to maintain the expert’s enthusiasm, which is the most critical success factor in the KA process.

To complement the interviewing method or to replace it with an automated system, more structured KA approaches have been suggested. Structured KA approaches, based on the concept of the 'knowledge level' [48], seek to describe domain knowledge and problem-solving at a level independent of implementation. These approaches emphasize building a paper knowledge base, or a conceptual or knowledge-level structure of the domain, prior to incorporating knowledge into the machine. These approaches get their power from paying close attention to problem-solving methods, rather than knowledge representation schemes.

These structured approaches can be further classified in terms of two dimensions: strategic and tactical. The strategic dimension is concerned with the way the KA processes are driven: knowledge engineer-driven, expert-driven or machine-driven. The tactical dimension is concerned with the technical level of KA processes. KA methods are classified according to the techniques that are used for each category. Specific KA techniques include protocol analysis, the repertory grid method, visual modeling, and induction. Protocol analysis and the repertory grid method are used in the knowledge engineer-driven approach. Visual modeling is used in the expert-driven approach, and induction is used in the machine-driven approach. These approaches to KA are analyzed next.

## 3.1. Knowledge Engineer-driven KA

The classical approach to KA is to employ a knowledge engineer to replicate the knowledge underlying expert performance by using KA techniques. Often the knowledge engineer is compared to a systems analyst in conventional computer systems development. KA is, however, a much more complex activity than systems analysis. The fact that KA is dealing with knowledge rather than procedures makes KA much more difficult and complex. After conducting systems analysis, the systems analyst should have a fairly good idea of what he needs to know. In KA this is not the case. Experts are not merely persons who know many facts and procedures. Through years of experience they have built up a body of knowledge (i.e., expertise) which they use to make informed and wise decisions. The problem is, however, that experts are often unaware of how they make decisions. They can often give the decision but not describe the process. 'Expertise is difficult to teach and to describe. Experts use it without knowing what they are doing, but are confident that their methods are effective.' [33, p. 455].

Since a knowledge engineer's task is relatively ill-defined when compared with the systems analyst's, a whole new set of difficulties arises in KA. Two major reasons why an expert should not be his or her own knowledge engineer are [31]:

(1) Lack of technical knowledge; Experts will usually have insufficient knowledge about programming and ES techniques.

(2) Incompleteness and incorrectness; Experts will find it difficult to describe their knowledge completely and correctly.

Necessary skills and requirements for a successful knowledge engineer include good communication skills, empathy and patience, persistence, and intelligence [31].

Knowledge engineers often use techniques to complement the basic interviewing method. Protocol analysis and the repertory grid method are the most commonly used techniques.

## 3.1.1. Protocol Analysis

'Protocol analysis is based on a transcribed interview, but attempts to structure the process, and produces more meaningful results.' [33, p. 457] Questions about specific examples of problems or cases make it easier for the expert to respond than in the case of abstract questions. Concentrating on a series of cases means that the expert is less likely to disagree or jump from one subject to another. Also, interference with the expert's decision-making process, which might be caused when asking questions, can be minimized by asking him or her to verbalize immediate thoughts instead of the reasoning behind the decision [54]. As a result, comments are more coherent and structured. From the comments on specific examples, it is possible to detect general patterns so that it might be easier to structure the comment into knowledge. Although it is still necessary to document the comments, the main advantage of protocol analysis over the interviewing method is that transcripts reflect individual decision-making processes.

Techniques for obtaining protocols form a continuum from concurrent ‘thinking aloud’ verbalization to retrospective verbalization. Concurrent verbalization causes minimum interference with the decision-making process by requiring subjects to verbalize information that is in short-term memory. On the other hand, retrospective verbalization increases interference by requiring subjects to recall the decision-making process which makes the resulting protocols easier to analyze. The specific objective of a researcher’s analysis must be considered when selecting a particular protocol technique [58].

The resulting protocols consist of a continuous string of words, exclamations, and incomplete sentences which appear to be rather disorganized. Protocol analysis is the process of translating this chaotic collection of verbalizations into more accessible representations. Protocol analysis requires a time-consuming search for a workable compromise between, on the one hand, eliminating irrelevant information, thereby increasing the accessibility of the remaining information and, on the other hand, retaining and structuring as much information as possible to avoid discarding information which is essential for a proper understanding of the underlying thought process [7].

The analysis of protocols requires a number of phases to produce a structured model of the expert's knowledge. Medical protocols which were used in EMYCIN illustrated the systemic approach. The procedure is outlined in table 1.

Protocol analysis has been implemented successfully in several areas including financial analysis [7], cryptarithmic [49], medical diagnosis [47], and media planning [43]. Mitchell [43] used four different procedures to acquire knowledge from

## Table 1

## Summarized procedure of protocol analysis.

1. Provide the expert with a full range of information normally associated with a task.

2. Ask the expert to verbalize the task in the same manner as would be done normally while verbalizing his or her decision process and record the verbalization on tape.

3. Make statements by transcribing the verbal protocols.

4. Gather the statements which seem to have high information content.

5. Simplify and rewrite the collected statements and construct a table of production rules out of the collected statements.

6. Produce a series of models by using the production rules.

media planners, including elicitation, problem sorting, protocol analysis, and problem-solving with a decision frame. Several studies have been made to automate protocol analysis by exploiting AI techniques [56].

Although protocol analysis is good at diagnosis, it is difficult to get perfect accuracy in diagnosis because more complex problems may have a completely different structure from the more common ones [33]. Protocol analysis seems suitable for well-structured, homogenous problem domains. Actual implementation shows that it is appropriate for diagnosis type problems. Since protocol analysis represents knowledge as rules or procedures, it is suitable for the elicitation of heuristics and simple concepts. It does not provide assistance to the knowledge engineer in identifying and acquiring deep knowledge or reasoning processes.

## 3.1.2. Repertory Grid

'Much of the difficulty in knowledge acquisition lies in the fact that the expert cannot easily describe how he views a problem' [32, p. 24]. The expert may be confused between facts and factors which actually influence decision making. Expertise is often based on perception or insight [13].

One approach to handling these problems is based on the repertory grid technique developed by Kelly [34]. Kelly viewed a human being as a ‘personal scientist’ who seeks to predict and control events by forming theories, testing hypotheses, and weighing experimental evidence. Based on this perspective, Kelly developed a ‘personal construct theory’ that everyone has his/her own model of the world which is made up of individual personal constructs. The repertory grid is a method of investigating such a model.

![](/api/attachments/8WFX8XHM/fulltext/images/7adf118b3031561f440bf1675bf7e5689182e3be81bd0ed4f9995c819c528353.jpg)  
Fig. 2. A repertory grid used in PLA [6].

The model consists of elements and constructs. Elements are similar to examples in induction, and the expert chooses the elements which are considered important. Then, the expert is asked to compared successive sets of these elements, listing distinguishing characteristics and their opposites in a grid. A trait and its opposite represent a bipolar scaled construct. The construct is similar to an attribute in induction, except for the bipolarity. Having supplied the construct, the expert rates each element according to this construct. A collection of elements, constructs, and ratings is referred to as a rating grid [6].

Fig. 2 shows an example of rating grid method used in the Programming Language Advisor [6]. The problem solutions (elements), which are programming languages in this case, are elicited from the expert and placed across the grid in columns, and solution traits (constructs) are listed down the rows of the grid as bipolar scales. Traits are elicited by presenting groups of elements and then asking the expert to discriminate among them. Then the expert gives each element a rating showing where it falls on the trait scale.

Researchers have extended Kelly's original binary rating method (x or blank) to include rating scales. At any stage, the expert can insert, delete, or update elements or constructs to represent a coherent model of the expert's view. This process might be a very useful technique for extracting attributes for induction or forming the basis of a consultation. More recently, elicitation and analysis of repertory grids have been made available through interactive computer programs. A variety of distance-based grid analysis techniques have been used. In those techniques, both elements and constructs may be graphically compared by the expert to find similarities and differences [5].

There have been several successful implementations of the grid method. ETS (Expertise Transfer System) interviews experts and helps them construct, analyze, test, and refine knowledge bases. Aquinas [6] extends the problem solving and knowledge representation capabilities of ETS by allowing experts to structure information in hierarchies. A set of heuristics of KA has been defined and incorporated in the Dialog Manager, a subsystem of Aquinas, to provide guidance in the KA process to domain experts and knowledge engineers [35].

KRITON [21] employs several KA methods to capture different kinds of knowledge. For human declarative knowledge, the repertory grid technique is used. For procedural knowledge, protocol analysis is used. Textbook knowledge is captured by incremental text analysis. After a completion process and a consistency check, the elicited information is transformed into an intermediate knowledge representation language. Frame, rule, and constraint generators operating on the intermediate representation level are used to build up the final knowledge base. On the other hand, knowledge already acquired guides the employment of the elicitation methods to complete the knowledge bases incrementally. ROGET [3] was developed to acquire a conceptual structure in a specific domain (of the EMYCIN type).

There are some strengths and weaknesses of the grid methods. Grid methodologies are best suited for structured analysis problems (e.g., debugging, diagnosis, interpretation, classification) whose solutions may be enumerated ahead of time. However, these methods cannot readily handle synthesis problems (e.g., design and planning) where unique solutions can be derived from components or problems that require a combination of analysis and synthesis (e.g., control, monitoring, prediction, repair) [5]. It also is difficult to apply the grid methodology to elicit deep causal knowledge, or strategic knowledge. Grid methods can elicit traits and build relationships, but cannot determine how or when this information is used in the problem-solving process [5]. These methods do not provide facilities for choosing or mixing reasoning processes. In addition, it is difficult to verify the sufficiency of element and construct sets [34]. Based on these characteristics, the grid methods seem suited to well-structured, medium-sized, and homogeneous problem domains.

## 3.2. Expert-driven KA

Knowledge engineers typically lack the background needed to pose optimal questions about a particular application area. At the same time, domain experts may find it difficult to reflect on an explicate their problem-solving strategies, and often have little appreciation for how the knowledge engineer formalizes expertise in a knowledge base. Many cycles of potentially unnecessary elicitation, programming, and evaluation may occur simply because of miscommunication between the expert and the knowledge engineer [9]. It has long been recognized that the development of new ES might be greatly expedited if experts could somehow enter their knowledge directly into computers without relying on knowledge engineers as intermediaries [17].

The idea of having experts encode their expertise has some advantages. First, there is less noise introduced in the encoded knowledge. Second, there is no need for the knowledge engineer to spend time learning domain specific language and concepts. This is especially true when there is a large amount of knowledge to be entered into the system. Third, the resultant system has the expert's – and not an intermediary's – view of the domain [26].

From the perspective of this approach, KA can be viewed as a descriptive and creative modeling activity. The key assumptions behind this approach are that [44]:

(1) The expert can learn and use the encoding interface.

(2) The expert can identify variables and relationships among them.

(3) The expert can structure a refinable model by using a structured approach to one's domain.

(4) The inevitable loss of transparency in encoded knowledge is acceptable if the expert can assure the performance of the model.

Since the approach is to replace the knowledge engineer with an automated system, the following two problems of the KA process must be addressed [24].

(1) Indeterminateness: The expert is likely to be fairly vague about the nature of associations among events.

(2) Incompleteness: The expert will probably forget to specify certain pieces of knowledge.

The indeterminateness problem reflects the fact that experts are not accustomed to talking about the associations between events in a way that precisely fits the correct problem-solving method. Although the expert can be encouraged to be as specific as possible, a smart KA tool must be able to tolerate ambiguity and indeterminateness. The problem of incompleteness is one of identifying missing knowledge. The expert, no matter how qualified and thorough he may be, is likely to forget to mention certain circumstances. And sometimes the expert will make mistakes. Thus, a smart knowledge acquisition tool needs to be able to add knowledge incrementally to the knowledge base, to refine existing knowledge, and sometimes to correct existing knowledge. The indeterminateness problem and the incompleteness problem dominate the two phases of KA: (1) the gathering of information for constructing the initial knowledge base, and (2) the iterative refinement of this knowledge base.

Visual modeling techniques are often used to construct the initial domain model. The objective of the visual modeling approach is to give the user the ability to visualize real world problems, and to manipulate elements of it naturally through the use of graphical entities [51]. Research on human problem information processing suggests that image-oriented systems enable users to apply the power of the computer in a manner which more closely resembles the natural cognitive process [53]. Weber [57] pointed out the role of images and graphics in problem solving and problem structuring activities. She indicates that diagrams and drawings are useful in representing problems, serving as a set of external memory aids, and revealing inconsistencies in an individual's knowledge.

Thus, visual modeling approaches: (1) enhance man/machine interaction; (2) support structuring complex problems; (3) provide the capability for modeling the behavior of a system; and (4) serve as the basis for incorporating heuristic rules appropriate for automated inference procedures [51]. Graphical approaches to knowledge structuring or KA have been developed in structural modeling (SM), which has digraph theory as a theoretical basis. In this approach, knowledge is structured as

1. Specify the problem elements and relationships between the elements. The relationships of the model are represented in the form of a matrix.

2. Construct a binary connection matrix which indicates an interaction or lack of interaction between pairs of elements.

3. Specify the signs, weights and time delays for the relationships.

4. Construct a digraph which presents model variables as nodes with the functional relationships between the variables.

5. Refine the digraph (inserting, deleting, and updating elements or relationships).

a set of facts, with each fact being related to one or more others facts in causal relationships. A number of methodologies have been developed to guide the structural modeling process. A survey of these SM tools is given by Lendaris [38]. However, the SM tools discussed by Lendaris assume that the set of elements is given, and focus on the investigation of relationships among them. These analytical tools may be used to investigate the structure in the expert's perception of the problem domain, and are useful in improving the accuracy of the knowledge base.

Applications of the visual modeling methodology have been developed by Pracht [51,52]. He developed a software tool called GISMO (Graphical Interactive Structural Modeling Option) to support knowledge structuring and acquisition. The software includes a menu-driven user interface, a set of interactive digraph generation routines, digraph design and modification proce-

![](/api/attachments/8WFX8XHM/fulltext/images/a7e3b1370f5125a3c0d5bebe1d3d6ef432a90459651842ce079eac731ba5827a.jpg)  
Fig. 3. A graphical representation of a marketing model constructed by using GISMO [53].

Knowledge acquisition procedures in Pract's knowledge system.

1. Construct a model showing relationships among objects.

2. Assign attributes to the objects. These attributes may involve mathematical functions for pointing to quantities in a database or for calculating values for other attributes of the model.

3. Select a specific time and verify the model by instructing it to calculate for the specified time.

4. Specify a sequence of times corresponding to data in the data base and trace the evolution of model elements to further verify the model behavior.

5. Incorporate heuristic rules corresponding to paths through O-A-V triplets for a more complete knowledge base and reasoning system.

dures, and on-line help messages. Four phases of interactive knowledge organization described in GISMO are summarized in table 2. A graphical representation of an example marketing model can be constructed by using GISMO (see fig. 3).

As an extension of GISMO, Pracht [51] proposed an image-based knowledge system by adopting the object-attribute-value (O-A-V) triplet approach. In this system, he attempted to represent uncertain rules, heuristics, and the behavior of a system in the graphical representation format shown in GISMO. The manager's activities in structuring and diagnosing the problem in this system are outlined in table 3. Fig. 4 shows a graphical representation of a financial model constructed in this system. Finch et al. [25] proposed a two-part methodology, consisting of cognitive mapping and information display boards, to elicit and structure knowledge.

The major goal of the expert-driven approach is to build a reasonable initial knowledge base with a minimal amount of information elicited from the expert. MOLE [24] is an ES shell that can help domain experts build a heuristic problem-solver by working with them to generate an initial knowledge base, and then detect and remedy deficiencies in it. INFORM [44] is a domain-independent, expert-directed KA tool. Influence diagrams, graphical representations of the decision problem structure, are used to structure knowledge and computational processes. The architecture is best suited to heuristic classification problem-solving, in particular, domains with diagnosis or decision-making under uncertainty. Gale's Student [28] and Musen's OPAL [46] used the visual modeling approach, which made it easy for experts to express ideas relevant to their domain.

![](/api/attachments/8WFX8XHM/fulltext/images/72f7745ee46e9e2a0ddc2ec2494b46ed54babff7052fc030c0cde2649503133b.jpg)  
Fig. 4. O-A-V representation of a financial model [51].

The visual modeling method seems well suited for eliciting both concepts and heuristics. However, this approach does not provide a facility for acquiring reasoning within a domain. The limitations in this approach are thus the limitations of the domain model. If the domain model is sufficiently complete, the need for knowledge engineers could be obviated. Yet, regardless of the thoroughness with which one can understand the application area at the knowledge level, it is impossible to anticipate all of the constructs one might encounter in a specific domain. Designing acceptable graphical forms to capture the knowledge for such an all-inclusive model would be unwieldly. This problem is, however, also encountered in the knowledge engineer-driven approach. Another problem of the visual modeling approach is the difficulty in representing the wide range of knowledge domains that can be easily represented by other methods $[23]$ .

## 3.3. Machine-driven KA

The classical approach to the acquisition of knowledge is to program the facts and rules into the machine. Unfortunately, the amount of time required to program the equivalent of human intelligence is prohibitively large. An alternative approach allows a machine itself to learn how problems are solved.

Researchers in AI are investigating many aspects of the broader topic of learning. The survey article by Dietterich et al. [22] divides the topic of learning into four areas: rote learning, learning by being told, learning from examples, and learning by analogy. The collection of articles edited by Michalski et al. [40] covers a number of issues and recent developments in machine learning, and provides an extensive bibliography on the subject. Among these, learning from examples based on inductive inference is the most often used technique [19].

The basic idea behind induction is that instead of directly describing the decision-making processes, the expert provides a set of example cases consisting of decisions, along with the attributes which were considered in making those decisions. A computerized algorithm is then used to infer some rules from those examples. This means that a system would have to include a module capable of performing inductive inference. The induced rules apply to the example set, which is referred to as the 'training instance.' Many programs have been developed that are able to learn a single concept (BACON, ID3, SPARC) or multiple concepts (AQ11, DENDRAL, AM) from training instances (for details, see [15]).

The research on computer inductive inference is still at an early stage of development. However, recent research in this area indicates that induction often performs better than interviewing if the problem domain is sufficiently simple and well-structured [41]. As a rare application of machine learning to the business domain, Braun and Chandler [8] used a learning from examples technique for predicting stock market behavior. The system was capable of finding simple rules and performed at an expert level.

Induction itself certainly has advantages. It is ‘objective, repeatable, indefatigable, consistent, and easy to understand’ [33, p. 458]. A major advantage of this method is that the expert often finds it easier to provide examples of decision cases rather than to describe the decision-making process itself. In other words, he can describe ‘what’ rather than ‘how’. It can be used both to explain the effects of attributes and patterns in the data and to predict outcomes for examples which are not in the training instances.

The problem of induction is, however, that verification of induced rules is difficult because the quality of induced results will depend both on the algorithm used and the particular example set available. Success in induction lies in the selection of the training instances and attributes. The algorithm can not induce what is not there. A poor set of attributes results in a poor set of rules. In addition, it is difficult to judge the quality of the examples and attributes, since rules, which are the outcome of induction, are unknown from the early stages. Most implementations do not perform very well for contradictory data or probabilistic rules, therefore, output must be interpreted with care [32].

Although the induction method can elicit both concepts and heuristics, it is quite difficult to elicit reasoning processes used by experts. This method can support well-structured problem domains. The success of the induction method lies in the selection of appropriate examples, which can be done easily in simple, well-structured situations.

The new paradigms of machine learning, namely explanation-based learning and deductive learning, have overcome some limitations of the learning from examples paradigm. Explanation-based learning can be described in two steps. First, an example problem is solved producing an explanation which indicates what information was needed to arrive at a solution. Next, the example is generalized by retaining only those features of the example which were necessary to produce the explanation [50].

Several programs have been developed based on this technique. ACES [50], developed for fault diagnosis from device descriptions, deduces heuristics from device models which describe the system functionality and connectivity. OCCAM [50] learns to predict the outcome of economic sanction episodes from simple economic theories.

Explanation-based learning is based on a complete domain theory. In other words, the initial example problem should be solved on the basis of the domain model. However, building up the domain model is the real problem which has been ignored in existing machine learning approaches. Morik's BLIP [45] is an attempt to cope with this problem. It starts KA with a 'sloppy' domain model entered by user in the form of predicates. Based on the domain model, learning processes which include generating, rating, and testing hypotheses result in a well-organized model.

## 3.4. Comparison of KA Methodologies

As discussed above, the KA methodologies presented can be compared in terms of the types of knowledge and the characteristics of problem domain that a specific KA technique can support.

The knowledge engineer-driven approach has been the primary method used to elicit expertise. It is based on the assumptions that experts often have insufficient knowledge about programming and ES techniques, and have difficulty in describing their knowledge completely and objectively. Although this approach can elicit expertise in an objective manner, the time taken for the knowledge engineer to become familiar with the domain and miscommunication problems are the major drawbacks of the approach. Techniques that knowledge engineers use to complement the primitive interviewing method include protocol analysis and the repertory grid method. As discussed in the preceding sections, protocol analysis and grid methods seem to be well suited to the elicitation of heuristics. However, it is difficult to elicit deep knowledge and reasoning processes with these methods. Protocol analysis can support simple, well-structured problem domains, whereas grid methods can handle medium-sized domains that are at least moderately well-structured.

The expert-driven approach is based on the assumptions that experts can structure a refinable domain model and that a certain degree of objectivity-loss in encoded knowledge is acceptable. The major thrust of this approach is that there is less noise in the encoded knowledge, and that the KA process can be expedited. However, the fact that experts drive the KA process to elicit their own expertise often result in intrinsic problems: indeterminateness and incompleteness. To offset these problems, visual modeling methods may be used to construct the domain model. As identified in previous sections, visual modeling methods can support the elicitation of deep knowledge, as well as heuristics. The problem domain for which this method seems well suited is of medium size, moderate complexity, and at least moderately well-structured.

Table 4  
Comparison of KA methodologies.

<table><tr><td colspan="2">KA methodology</td><td>Types of knowledgea</td><td>Problem domain</td></tr><tr><td>Strategic</td><td>Tactical</td><td></td><td></td></tr><tr><td rowspan="2">KE-drivenb</td><td>Protocol</td><td>heuristics, concepts</td><td>small, simple, well-structured</td></tr><tr><td>Grid</td><td>heuristics, concepts</td><td>medium, moderate, well-structured</td></tr><tr><td>Expert-driven</td><td>Visual modeling</td><td>concepts, heuristics</td><td>medium, moderate, semi-structured</td></tr><tr><td>Machine-driven</td><td>Induction</td><td>heuristics, concepts</td><td>small, simple, well-structured</td></tr></table>

$^{a}$ Th orders in Types of knowledge column represents the degree of easiness with which a specific KA method can acquire certain types of knowledge.  
$^{b}$ KE stands for knowledge engineer.

The machine-driven approach has been recognized as an emerging research area. It is based on assumptions that the machine can learn by using some inference mechanism (usually induction). The major advantage of this approach is that it is objective, repeatable, consistent, and fast. The problem is, however, that verification of results is difficult, since the quality of induced results depends both on the algorithm used and the particular example set available. Although induction can elicit concepts and heuristics, knowledge that machines can learn is quite restricted in terms of both quality and quantity because research on machine learning is still at an early stage of development. The problem domains supported are, therefore, small, simple, and well-structured.

Above all, current KA techniques seem to be well suited to elicit heuristics and concepts to varying degrees. However, none of the KA techniques provides assistance to elicit reasoning. In addition, most techniques support well-structured problem domains only. The characteristics of the KA techniques discussed are summarized in table 4.

## 4. Matching KA Methods to Managerial Problem Domain

In order to match KA methodologies to management problem-solving, we use Mintzberg's [42] organizational model, which defines four decision categories: operating decisions, coordinative decisions, exception decisions, and strategic decisions. Each of these decision categories is described and its supporting KA techniques are discussed in this section.

The major theme of the proposed model is a conceptual verification of the assertion described in section 2. The assertion suggests that the choice of a KA technique is dependent upon characteristics of the problem domain and the types of knowledge required. The preceding sections have essentially illustrated this conceptually, thus implying that problems domains can be mapped to KA methods. The specific task the system is to accomplish is the major factor in choosing the appropriate KA methodology. Actually, any KA technique might be used within any decision category. Since the proposed model is based on generalities and tendencies, it may be used to guide KA technique selection once the task is analyzed in detail. The following discussion describes the general mapping of decision types to KA techniques.

Operating decisions are decisions which assure that a specific task is carried out effectively and efficiently. Operational decisions are more concerned with tasks rather than people [1]. Problem domains in operating decisions are relatively well structured and the solution to these problems can be easily predefined. Most operating decisions are based on rules and procedures set by experts.

Operating decisions can be partitioned into two categories. One type of operating decision is made by the operating core and the other is made by specialists. Operating core decisions are repeatable and routine because of the standards and policies set forth by the operating supervisors. Based on these generalities, there is little need to build knowledge-based systems for this type of decision. Rather, the conventional DSS or MIS would be adequate to solve the problem. Operating decisions made by specialists have some different characteristics from the decisions made by the operating core. Since experts make the decision, heuristics and procedures are often used, and the problem domain may be larger than that of operating core decisions. It is noteworthy that current expert systems attempt to support this kind of problem domain [18]. Based on these characteristics, knowledge engineer-driven or machine-driven approaches might be appropriate for this decision type at the strategic level. Specifically, repertory grids or induction methods seem well suited to this domain at the technical level.

Coordinative decisions are decisions which assure that resources are obtained and used effectively and efficiently in the accomplishment of the organization's objectives. This kind of decision involves interpersonal interaction and consideration of a larger number of factors within the context of the policies and objectives developed in strategic planning [1]. Examples of coordinative decisions are budgeting, scheduling, and manpower planning. In general, this type of decision is made by middle managers. Coordinative decision making appears to be a good place to build knowledge-based systems that support, rather than replace the decision maker [2]. Certainly, the need for interpersonal interaction and consideration of the external environment makes it difficult to computerize the entire decision process. However, it is possible to computerize some parts of the process since certain aspects are routine.

The type of knowledge required for this type of decision includes both concepts and heuristics. The problems domains in this decision-type range from well-structured to ill-structured. Also, the size of the problem domain becomes larger as external factors and human relations must be considered. Based on these characteristics, the repertory grid method is suggested for structured aspects, while the visual modeling approach is appropriate for ill-structured aspects of the coordinative decision type.

Exception decisions are characterized as ad hoc decisions that have nonroutine occurrences and use few heuristics for solving problems. To solve this problem type, deep knowledge is desirable [2]. The major characteristics of this kind of problem are that the knowledge base is larger than that of coordinative decisions, and causal relationships in the external environment make the knowledge structure complex and uncertain. The time pressure in this type of decision prohibits the use of labor-intensive approaches. Thus, the expert-driven approach is plausible. Therefore, the visual modeling technique seems best suited for exception decisions.

Strategic decisions are decisions on objectives of the organization, on changes in these objectives, on the resources used to attain these objectives, and on the policies that are to govern the acquisition, use, and disposition of these resources [1]. A major problem in this area is predicting the future of the organization and its environment, which makes the knowledge domain complex and large. Because strategic decisions have significant impact on the entire organization, many people are involved and political motives may delay the decision process [42].

The application of an AI system to a strategic decision must be capable of solving the following problems. Since decisions are ad hoc, deep knowledge is needed. However, deep knowledge is unknown in many cases. Another problem is that even if a deep knowledge model could be developed, there would be severe search problems [2]. In addition, the system should provide various knowledge sources to meet the various kinds of information needs. Based on these characteristics, no single KA technique might be appropriate for strategic decisions. Some combination of KA techniques is suggested for this type of decision. One plausible would be to first let the expert build a domain model (i.e., intermediate knowledge base) by using a visual modeling method, and then revise or enlarge the model by using either grid or induction methods. This is, in effect, an on-going process in which the domain model is continually refined as experts learn more about the domain.

Table 5

<table><tr><td colspan="3">Decision</td><td colspan="2">KA methodologies</td></tr><tr><td>Type</td><td>Knowledge</td><td>Problem domain</td><td>Strategic level</td><td>Tactical level</td></tr><tr><td>Operating decisions</td><td>heuristics, concepts</td><td>medium, moderate, well-structured</td><td>KE-drivenaM-drivenb</td><td>grid, protocol induction</td></tr><tr><td>Coord. decisions</td><td>heuristics, concepts</td><td>medium, moderate, semi-structured</td><td>KE-driven</td><td>grid, protocol</td></tr><tr><td>Exception decision</td><td>concepts, heuristics, reasoning</td><td>large, complex, ill-structured</td><td>E-drivenc</td><td>visual modeling</td></tr><tr><td>Strategic decision</td><td>concepts, heuristics, reasoning</td><td>large, complex, ill-structured</td><td>combination of above</td><td></td></tr></table>

$^{a}$ Knowledge engineer-driven.

![](/api/attachments/8WFX8XHM/fulltext/images/2113b7286c047a4b827eed03b7724271da3f8a7627692c4933c455a577dc7b1b.jpg)  
Fig. 5. A conceptual mapping of KA methodologies with decision types.

## 5. Conclusions

Table 5 summarizes the proposed model. Fig. 5 shows a conceptual mapping of KA methods to problem domains. The model is based on the arguments that the choice of KA techniques is dependent upon problem domain characteristics and knowledge types. This model can guide the system builder in selecting appropriate KA techniques for the specific decision type that the system is intended to support. Despite this benefit, characteristics of the specific task should first be analyzed in detail and then used to drive the selection of specific KA techniques.

The model and discussion above have important implications for developing knowledge-based DSS. First, no current single KA technique is optimal for all business problems. Second, current KA techniques have concentrated on structured knowledge domains. Third, this is one of the very few studies to examine KA techniques in the management domain.

The result of this work provides a basis for further research in KA. One direction that future research might take is more studies on KA techniques for ill-structured problem domains which most DSS attempt to support. Another direction would be more efforts to develop KA methods that can effectively elicit reasoning used by experts.

## References

[1] Anthony, R.N., Planning and Control Systems: A Framework for Analysis, Harvard University, Graduate School of Business Administration, 1965.

[2] Baldwin, D. and G.M. Kasper, Toward Representing Management-Domain Knowledge, Decision Support Systems, Vol. 2, No. 2, 1986, 159–172.

[3] Bennett, J.S., ROGET: A Knowledge-Based System for Acquiring The Conceptual Structure of A Diagnostic Expert System, Journal of Automated Reasoning, Vol. 1, No. 1, 1985, 49–74.

[4] Boose, J.H., A Tool for Acquiring and Combining Knowledge from Multiple Experts, Working Paper, Knowledge Systems Laboratory, Boeing Computer Services, 1986.

[5] Boose, J.H., A Knowledge Acquisition Program for Expert Systems Based on Personal Construct Psychology, Int. J. Man–Machine Studies, Vol. 23, No. 4, 1985, 495–525.

[6] Boose, J.H. and J.M. Bradshaw, A Knowledge Acquisition Workbench for Eliciting Decision Knowledge, Proceedings of the Twentieth Hawaii International Conference on Systems Sciences, Vol. 1, 1987, 450–457.

[7] Bouwman, M.J., Human Diagnostic Reasoning By Computer: An Illustration from Financial Analysis, Management Science, Vol. 29, No. 6, 1983, 653–664.

[8] Braun, H. and J.S. Chandler, Predicting Stock Market Behavior Through Rule Induction: An Application of the Learning-From-Example Approach, Decision Sciences, Vol. 18, No. 3, 1987, 415–429.

[9] Buchanan, B.G., D. Barstow, R. Bethtal, J. Bennett, W. Clancey, C. Kulikowski, T. Mitchell, and D.A. Waterman, Constructing An Expert System, in: F. Hayes-Roth, D.A. Waterman, and D.B. Lenat, eds., Building Expert Systems, Reading, Massachusetts: Addison-Wesley, 1983, 127–167.

[16] Bylander, T. and B. Chandrasekaran, Generic Tasks for Knowledge-Based Reasoning: The 'Right' Level of Abstraction for Knowledge Acquisition, Int. J. Man-Machine Studies, Vol. 26, No. 2, 1987, 231–243.

[11] Chandrasekaran, B., Towards a Taxonomy of Problem Solving Types, The AI Magazine, Vol. 11, No. 1, 1983, 9–17.

[12] Chandrasekaran, B. and S. Mittal, Deep Versus Compiled Knowledge Approaches to Diagnostic Problem-Solving, Int. J. Man-Machine Studies Vol. 19, No. 4, 1983, 425–436.

[13] Chi, M.T.H., P.J. Feltovich, and R. Glaser, Categorization and Representation of Physics Problems by Experts and Novices, Cognitive Science, Vol. 5, No. 2, 1981, 121–152.

[14] Churchman, C.W., The Design of Inquiring Systems: Basic Concepts of Systems and Organization, Basic Books, Inc., NY, 1971.

[15] Cohen, P.R. and E.A. Feigenbaum (ed), The Handbook of Artificial Intelligence, Vol. 3, Pitman, 1982.

[16] Courtney, J.F. and D.B. Paradice, A Knowledge-Based DSS for Managerial Problem Diagnosis, Decision Sciences, Vol. 18, No. 3, 1987, 373–399.

[17] Davis, R., Applications of Meta-Level Knowledge to the Construction, Maintenance, and Use of Large Knowledge Bases, Ph. D. Thesis, Stanford University, 1976, Rep. No. STAN-S-76-564.

[18] Davis, R. and D.B. Lenat, Knowledge-Based Systems in Artificial Intelligence, McGraw-Hill, New York, 1982.

[19] Delgrande, J.P., A Formal Approach to Learning from Examples, Int. J. Man–Machine Studies, Vol. 26, No. 2, 1987, 123–141.

[20] Dhar, V., On the Plausibility and Scope of Expert Systems in Management, J. of Management Information Systems, Vol. 26, No. 1, 1987, 25–41.

[21] Diederich, J., I. Ruhmann, and M. May, KRITON: A Knowledge-Acquisition Tool For Expert Systems, Int. J. Man-Machine Studies, Vol. 26, No. 1, 1987, 29–40.

[22] Dietterich, T.G., R. London, K. Clarkson, and R. Dromey, Learning and Inductive Inference, in P. Cohen, and E. Feigenbaum eds., The Handbook of Artificial Intelligence, Kaufman, Los Altos, Calif. 1982, 323–512.

[23] Elam, J.J., J.C. Henderson, and L.W. Hiller, Model Management Systems: An Approach to Decision Support in Complex Organizations, University of Pennsylvania, 1980.

[24] Eshelman, L., D. Ehret, J. McDermott, and M. Tan, MOLE: A Tenacious Knowledge Acquisition Tool, Int. J. Man–Machine Studies, Vol. 26, No. 1, 1987, 41–54.

[25] Finch, L., J. Landry, and D. Monarchi, and D. Tegarden, A Knowledge Acquisition Methodology Using Cognitive Mapping and Information Display Boards, Proceedings of the Twentieth Hawaii International Conference on Systems Sciences, Vol. 1, 1987, 470–477.

[26] Friedland, P., Acquisition of Procedual Knowledge from Domain Experts, Proceedings International Joint Conference on Artificial Intelligence 1981, 856–861.

[27] Gaines, B.R., An Overview of Knowledge-Acquisition and Transfer, Int. J. Man–Machine Studies, Vol. 26, No. 4, 1987, 453–472.

[28] Gale, W., Knowledge-Based Knowledge Acquisition for a Statistical Consulting System, Int. J. Man–Machine Studies, Vol. 26, No. 1, 1987, 55–64.

[29] Gorden, R.L., Interviewing: Strategy. Techniques, and Tactics, 3rd ed. The Dorsey Press, 1980.

[30] Gruber, T.R. and P.R. Cohen, Design for Acquisition: Principles of Knowledge-System Design to Facilitate Knowledge Acquisition, Int. J. Man–Machine Studies, Vol. 26, No. 2, 1987, 143–159.

[31] Hart, A., Knowledge Acquisition for Expert Systems, McGraw-Hill Book Company, New York, 1986.

[32] Hart, A., The Role of Induction In Knowledge Elicitation. Expert Systems, Vol. 2, No. 1, 1985, 24–28.

[33] Hart, A., Knowledge Elicitation: Issues and Methods. Computer-Aided Design, Vol. 17, No. 9, 1985, 455–462.

[34] Kelly, G., The Psychology of Personal Constructs, Norton, 1955.

[35] Kitto, C.M., and J.H. Boose, Heuristics For Expertise Transfer: An Implementation of A Dialog Manager for Knowledge Acquisition, Int. J. Man-Machine Studies, Vol. 26, No. 2, 1987, 183–202.

[36] Klinker, G., J. Bentolila, S. Genetet, M. Grimes, and J. McDermott, KNACK: Report-Driven Knowledge Acquisition, Int. J. Man–Machine Studies, Vol. 26, No. 1, 1987, 65–79.

[37] Kornell, J., Formal Thought and Narrative Thought in Knowledge Acquisition, Int. J. Man–Machine Studies, Vol. 26, No. 2, 1987, 203–212.

[38] Lendaris, G.G., Structural Modeling - A Tutorial Guide, IEEE Transaction on Systems, Man, and Cybernetics, Vol. SMC-10, No. 12, 1980, 807-840.

[39] McCarthy, J. and P. Hayes, Some Philosophical Problems from The Standpoint of Artificial Intelligence, in: B.L. Weber and N.J. Nilsson eds., Readings in Artificial Intelligence, Tioga, Palo Alto, 1981, 431–450.

[40] Michalski, R.S., J.G. Carbonell, and T.M. Mitchell, Machine Learning: An Artificial Approach, Vol. II., Morgan Kaufman Publishers, Inc., Los Altos, Calif., 1986.

[41] Michalski, R.S. and R.L. Chilansky, Knowledge Acquisition by Encoding Expert Rules Versus Computer Induction from Examples – A Case Study Involving Soybean Pathology, Int. J. of Man-Machine Studies, Vol. 12, No. 1, 1980, 63–87.

[42] Mintzberg, H., The Structuring of Organizations, Prentice Hall, Englewood Cliffs, NJ, 1979.

[43] Mitchell, A.A., The Use of Alternative Knowledge-Acquisition Procedures in The Development of A Knowledge-Based Media Planning System, Int. J. Man-Machine Studies, Vol. 26, No. 4, 1987, 399–411.

[44] Moore, E.A. and A.M. Agongino, INFORM: An Architecture for Expert-Directed Knowledge Acquisition, Int. J. Man-Machine Studies, Vol. 26, No. 2, 1987, 213–230.

[45] Morik, K., Acquiring Domain Models, Int. J. Man-Machine Studies, Vol. 26, No. 1, 1987, 93–104.

[46] Musen, M.A., L.M. Fagan, D.M. Combs, and E.H. Shortliffe. Use of a Domain Model to Drive An Interactive Knowledge-Editing Tool, Int. J. Man-Machine Studies, Vol. 26, No. 1, 1987, 105–121.

[47] Myers, C.D., J. Fox, S.M. Pegram, and M.F. Greaves, Knowledge Acquisition for Expert Systems: Experience Using EMYCIN for Leukemia Diagnosis, Expert Systems, Vol. 1, No. 3, 1983, 277–293.

[48] Newell, A., The Knowledge Level, Artificial Intelligence, Vol. 18, No. 1, 1982, 87–127.

[49] Newell, A. and H.A. Simon, Human Problem Solving, Prentice-Hall, 1972.

[50] Pazzani, M.J., Explanation-Based Learning for Knowledge-Based Systems, Int. J. Man–Machine Studies. Vol. 26, No. 4, 1987, 413–433.

[51] Pract, W.E., A Visual Modeling Approach for DSS Knowledge Acquisition and Organization, Proceedings of the Twentieth Hawaii International Conference on Systems Sciences, Vol. 1, 1987, 478–486.

[52] Pracht, W.E., GISMO: A Visual Problem Structuring and Knowledge Organization Tool, IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-16, No. 2, 1986, 265–270.

[53] Pracht, W.E. and J.F. Courtney, A Visual User Interface for Capturing Mental Models in Model Management Systems, Proceedings of the Nineteenth Hawaii International Conference on Systems Sciences, Vol. 1, 1986, 535–545.

[54] Schweiger, D.M., C.R. Anderson, and E.A. Locke, Complex Decision Making: A Longitudinal Study of Process and Performance, Organizational Behavior and Human Decision Processes, Vol. 36, No. 2, 1985, 245–272.

[55] Simon, H.A. and G. Lea, Problem Solving and Ruie Induction: A Unified View, in: L. Gregg, ed., Knowledge and Cognition, Hillsdale, N.J., 1974, 105–127.

[56] Waterman, D.A. and A. Newell, Protocol Analysis as a Task for Artificial Intelligence, Artificial Intelligence, Vol. 2, No. 3/4, 1971, 285–318.

[57] Weber, E.S., Systems to Think With: A Response to 'A Vision for Decision Support Systems', Proceedings of the Nineteenth Hawaii International Conference on Systems Sciences, Vol. 1, 1986, 618–626.

[58] Winkler, L.R., A Research Proposal for An Expert System for Monitoring, Diagnosing, and Interpreting Variances, Unpublished Paper, Texas Tech University, May 1986.
