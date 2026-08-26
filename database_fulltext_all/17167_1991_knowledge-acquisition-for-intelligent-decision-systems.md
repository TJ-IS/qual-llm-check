---
otero_id: 17167
otero_key: "3P8GHEHA"
title: "Knowledge acquisition for intelligent decision systems"
authors: "Jim McGovern; Danny Samson; Andrew Wirth"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90043-b"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge acquisition for intelligent decision systems

Jim McGovern

Department of Mathematics and Computing, Phillip Institute of Technology, Bundoora, Victoria, Australia, 3083

Danny Samson and Andrew Wirth

Graduate School of Management, University of Melbourne, Carlton, Victoria, Australia, 3053

The combination of Decision Analysis and Expert Systems as Intelligent Decision Systems is proposed as a means of supporting strategic decision making. An approach to knowledge acquisition for such systems is to use a domain independent aid to acquire problem knowledge, including structure, directly from the decision maker. Influence Diagrams are proposed as a suitable means of representing domain knowledge and as a target structure for the elicitation of decision structures from text. The text analysis procedure goes some way towards a much needed emphasis on the process of model building rather than on model representation and solution.

Keywords: Intelligent decision systems, Knowledge acquisition, Decision analysis, Expert systems, Text analysis.

![](/api/attachments/3P8GHEHA/fulltext/images/4754448bdac9278e3b956df17c79f3e063f296a71162bcff587aa5a4506607b2.jpg)

Andrew Wirth is a Senior Lecturer in the Graduate School of Management at the University of Melbourne. His previous positions have included Research Fellow in the Control Theory Centre at the University of Warwick and Visiting Associate at Templeton College, Oxford. His current fields of research interest are multiattribute optimisation, decision analysis and inventory control. His articles have appeared in journals such as Zeitschrift fur Operations Research, European

## Introduction

This approach is a promising basis for a needed and usable decision making aid for strategic management. Strategic decisions in business are

The term Intelligent Decision System has been used to refer to the combination of Decision Analysis and Expert Systems $[4,11,12]$ . Such systems can be considered a class of Expert Systems with an inference engine based on the application of the axioms of decision theory $[1]$ . Decision theory provides a means of problem structuring based on the normative processing of uncertainty and preferences, which has been widely and successfully applied to strategic problems $[3,5,15,16,18,31,36,40]$ . Expert Systems technology provides a flexible means of representing and processing specific control and domain knowledge.

Journal of Operational Research, Omega and the Journal of Business Finance and Accounting.

![](/api/attachments/3P8GHEHA/fulltext/images/51f5c5b7f65ff24cc758c60765e92c322b000ce966c18a216f4164e804a19b80.jpg)

Danny Samson is Professor of Manufacturing Management at the University of Melbourne and Program Director of the Centre for Manufacturing Management. His degrees are in Chemical Engineering and his PhD is in Managerial Decision Analysis. He has published in the Journal of the Operational Research Society, European Journal of Operational Research, Journal of Risk and Insurance, Journal of Business Research, International Journal of Management Science,

ASTIN Bulletin, Interfaces and the International Journal of Technology Management. His books include Managerial Decision Analysis (1988), Management for Engineers (1989) and Production/Operations Management (forthcoming).

![](/api/attachments/3P8GHEHA/fulltext/images/80a79bac8f8910e49592784da01f63062e1fb9caa6a6b8c8f823ab4dc0502e0d.jpg)

Jim McGovern obtained a Computing Science degree from Queensland University of Technology in 1980, and an M.Phil. from Griffith University in 1986 for the application of computer models to energy policy analysis. He is currently undertaking a PhD at the Graduate School of Management at the University of Melbourne in the area of knowledge based decision support.

valuable, involve a high level of uncertainty and are sensitive to the preferences of decision makers. Furthermore, there is evidence that unaided decision making for such problems is flawed $[10,35,39]$ and that software technologies such as DSS and conventional Expert Systems have failed to be widely applied $[2,8,24]$ . DSS have failed to provide the generality which allows the modeling techniques of management science to be easily applied to new problems while Expert Systems have failed to be adapted from “deep and narrow” domains based on the hard sciences and well defined artificial rules to the “wide and shallow” and fuzzy domain of management $[26]$ .

## Intelligent Decision Systems

Intelligent Decision Systems represent a shift in emphasis from the solution techniques of Decision Analysis to its practice. A problem with Decision Analysis has been the need for a decision analyst to act as an intermediary between the problem owner and the technique (see fig. 1).

The intermediary can detract from the quality of decisions by moving beyond his/her role to that of the domain expert, and by concentrating on modeling and optimisation at the expense of exploration and interpretation [8]. Intermediaries add to the cost and may delay decisions. Expert Systems technology can be used to provide intelligent access to previous decisions and domain knowledge as well as to model intelligent human behavior for model building, model querying, solution technique selection, solution evaluation and learning from model behavior [21]. Howard [12] describes the potential of such systems as follows:

"The power of Decision Analysis transforms opaque decision situations into transparent ones. The Intelligent Decision System offers the promise of providing this power to individuals, and to lower-level corporate decision-makers who could not afford it at present and in situations requiring very rapid decision-making."

Issues in the development of Intelligent Decision Systems are the representation of domain knowledge and the representation of process knowledge. Domain knowledge is represented as facts, rules and model components for a particular problem. Process knowledge refers to knowledge which is used to guide the development and use of a specific decision making model.

![](/api/attachments/3P8GHEHA/fulltext/images/918a5a300db98c9d5b6acacd7f43bf536318bb4a8412e3ec5171f0fa628edab5.jpg)  
Fig. 1. An Intelligent Decision System, Showing Potential Expert Systems Contributions.

![](/api/attachments/3P8GHEHA/fulltext/images/72b94ef876568f2467ce9b6abac59c13d841ac44687c522e47071b25ca2fd7d7.jpg)  
Fig. 2. Influence Diagrams for Strategic Planning Model.

## Representing Domain Knowledge

The basis of Decision Analysis is the ability to specify decisions as sequences of choices, chance events for which the probability distribution can be estimated or outcomes for which a utility function can be specified. The chance and outcome can be combined as expected utility and the modeled decision maker will prefer the policy or set of choice values which produce the highest expected utility.

Decision problems can be represented as Influence Diagrams [33] with nodes representing choice, chance and outcome events. Links between nodes represent conditional and informational relationships. The nodes can be viewed from three levels, the relational, numerical and functional levels [22].

The labeled nodes and arcs represent the relational level; showing the major components, their types and interdependence. A major advantage of Influence Diagrams (and some other graphical representations) is the ability to support problem partitioning, decomposition and abstraction As an example, Figure 2 shows Influence Diagrams relating to a strategic planning model developed by Samson [31] in the domain of general insurance.

Fig. 2(a) shows the decision making model at the most abstract level. The major concern of this model is the overall satisfaction with retained earnings and the dividend paid to shareholders as indicated by the diamond shaped node. There is only one outcome node on a fully specified Influence Diagram. The circular nodes represent chance events. For example, the future tax rate may be subject to some uncertainty. Certainly the decision maker cannot be sure of the future income from insurance premiums, investments and sales of investments. The decisions shown on the diagram relate to policy design and investment portfolio design and are shown as rectangles.

Fig.2(b) shows the disaggregation of the insurance premiums income node. This node is further divided into other chance events and decisions. The partitioning allows nodes to be dealt with as independently as possible. For example, when dealing with reinsurance effects one need only be concerned with the options available and the claims distributions.

The second level from which Influence Diagrams can be viewed is the numerical level. Utility functions and parameters, probability distributions and decision values and costs are specified numerically for each node.

The third level or functional level is concerned with how nodes are related. For Influence Diagrams based on Decision Analysis the relationships expressed are probabilistic and informational. Conditional arcs effect the probabilities of another chance node. These arcs may emanate from chance or decision nodes. For example, in fig. 2(b) the reinsurance effect is conditioned by the level of claims and the probabilities in the reinsurance node are expressed as joint probabilities with claims. Informational arcs are inputs to decision nodes and indicate that the values of these nodes are known when the decision is made. For example, in fig. 2(b) the dividend can be decided after the net income is known.

The functional level determines the solution method for an Influence Diagram. Probabilistic Influence Diagrams can be solved using an algorithm described by Shachter [33]. This algorithm consists of the value-preserving removal of nodes and arc reversals which correspond to the rollback procedure in decision trees. Formal definition of Influence Diagrams and their transformations are described by Shachter [32,33] and Agogino and Rege [1].

Influence Diagrams provide a knowledge representation technique which is cognitively appealing, at the relational level, and mathematically meaningful and tractable at the numerical and functional levels. Particular decisions can be represented as fully specified Influence Diagrams while partially specified Influence Diagrams and nodes represent domain characteristics. The importance of such a system is its ability to isolate individual decision components which can be synthesised into new models [7]. For example, an insurance company may have probability distributions for premiums attracted by specific instruments of insurance. These distributions can be used in a number of decisions (Influence Diagrams) and can be updated independently of these decisions. These common building blocks for organisational decisions may even transcend organisations. For example, Howard [12] provides some evidence that different corporations have similar attitudes to risks.

Individual nodes may also be disaggregated into further nodes. In the system proposed by Holtzman [11], three types of domain knowledge are represented as rules, knowledge about model building, knowledge about the assessment of probability distributions and knowledge about preferences. The model building knowledge provides the means of expanding nodes. The probability and preference rules allow for the expansion of the numerical level for chance and outcome events based on the data of individual cases.

Interest in computer software which can be used to help build and re-use decision models has led to the development of model management systems [20]. These systems have been based on knowledge representation and processing techniques such as logic, rules and frames. Influence Diagrams can be stored within such a framework with each model fragment or node stored as frames which are located using rules or logic.

## Process Knowledge in Intelligent Decision Systems

Apart from the domain knowledge in Intelligent Decision Systems, knowledge which describes the behavior of the human decision analyst can be incorporated. According to the Turing test this is achieved successfully when the user, who is hidden from the source of advice, is unable to detect the difference between the performance of the human decision analyst and the computer based Intelligent Decision System.

At the general level, the process of Decision Analysis is well understood. It is typically described as an iterative process consisting of the structuring of the decision, the assessment of the impact of alternatives (probabilities), determining preferences (utility) and the evaluation and comparison of alternatives [15].

The actual successful execution of these steps for less well structured problems has been very dependent on the skill and experience of the human decision analyst. Howard [13] has suggested that the successful decision analyst uses art as well as technical skills and that to be fully trained, in the art and science of Decision Analysis, requires 3–4 years of graduate education and at least 2 years of practice. Howard [12] suggests that it will be too difficult to replicate these skills in a computer system because “...the human decision analyst is too general-purpose to be captured everywhere...”

Detailed descriptions of the process of Decision Analysis [12,13,15] support this view. The strength of Decision Analysis, for less well structured problems, has stemmed from the interaction between an analyst and the decision maker in all phases of analysis. Some of the main tasks which are highly dependent on human interaction and information processing are

– determining the appropriateness of the Decision Analysis Paradigm for a particular problem. Other techniques from management science may be more appropriate for some problems. The most common reason, however, may be the presence of extraneous factors such as political considerations which restrict normative analysis.

\- framing or building a model for the right problem, This requires that the analyst “probe deeply” [12].

\- getting the right level of detail. The aim of Decision Analysis is to build a model which is simple and understandable but contains the most important elements of the problem.

\- consideration of all alternatives. The elicitation of good alternatives may require approaches such as brainstorming and means-end analysis.

\- the application of the “clarity test”, Howard [12] has proposed a clarity test for clearly defining events and variables on an Influence Diagram. The test asks whether a clairvoyant who knows the future could specify “…whether an event had occurred or not or, in the case of a variable, the value of the variable.”

\- to determine if there are biases and to correct them. These may occur in the estimation of probabilities [10,38] or quantities, For example, someone who has developed a product and has a vested interest in its production may overestimate potential sales.

\- the development of a correct utility model requires a technically skilled analyst with strong interpersonal skills [14].

\- to check for consistency. Redundant questioning and decomposition are two means of dealing with this. Decomposition requires that numerical values be disaggregated and checked.

\- conflicting expert opinion.

It is ultimately the decision maker who is responsible for these tasks which determine the efficiency and the correctness of the model and its evaluation. The final decision model, or requisite model, is one from which all sources of unease have been removed and from which no new intuitions emerge [28]. It is for this reason that the development of methods or software which can be used directly by decision makers is pursued. A primary task in this process is one of knowledge acquisition or the transfer of problem knowledge from the decision maker to the computer.

## Knowledge Acquisition for Intelligent Decision Systems

One approach which can be taken to the development of Intelligent Decision Systems is to isolate a class of decisions and to build a domain specific system for that class. This approach is taken, for example, in a system called RACHEL [11] in the domain of human fertility. The aim of this system is to help patients select a course of response particular to a diagnosis for infertility. RACHEL begins by examining a starting model for a particular diagnosis. The model in the form of an Influence Diagram is expanded by rules embodying model building, probability and preference knowledge. Further chance and decision nodes are added according to their applicability to a particular case. Probability functions and their parameters, and preference models are also selected using rules. RACHEL produces a model from a set of predetermined nodes to which uncertainty and preference data for a specific decision maker has been added.

A weakness of this approach is that although the end product may be user-friendly and appropriate for use by a broad range of decision makers, specific Intelligent Decision Systems require knowledge acquisition to be carried out upfront by an analyst with professional skills in both Expert Systems technology and Decision Analysis. This is particularly difficult in strategic management applications where the isolation a priori of a complete set of model components, especially choice nodes, and their possible relationships is required.

Another approach is to base development around the induction of Influence Diagrams from a training set of examples $[30]$ . It is likely that induction may be useful as one of the aids available to the modeler $[6]$ , however, in the domain of strategic management it will not be possible to acquire all knowledge from a database of examples and there will be an emphasis on the editing of knowledge bases rather than on their induction [22].

The final approach discussed here is to focus on the editing of knowledge bases using a domain independent tool which, while it does not replicate the skills of the expert decision analyst, offers general support for Decision Analysis. This approach has been taken, for example, by Moore and Agogino [22] in a system called INFORM. INFORM provides three types of support for knowledge acquisition by the modeler. The first type is an Influence Diagram language for representing and solving decision problems. The second type provides feedback facilities, such as graph drawing, which are commonly available in modeling software. The third type provides expert assistance specific to the Decision Analysis approach, the domain and to the particular user.

INFORM extends Influence Diagrams by providing some knowledge to control the modeling process. The system moves from the general to the specific by suggesting directions of analysis which are likely to be most rewarding. The most sensitive nodes or those about which the decision maker is least confident can be expanded. INFORM supports a process of progressive refinement which continues until the user or decision maker has built a requisite decision model $[28]$ . Moore and Agogino $[22]$ point out that INFORM (or any domain free system) can also be used to build domain specific systems.

The danger with the domain free approach is that, while the software will be a valuable aid to professional decision analysts and knowledge engineers, it will be too general and not friendly enough for managerial users. Attempts have been made to provide a basis for building Decision Analysis models interactively. Leal and Pearl [19] developed a system which uses question and answer sequences to build a model based on decision trees. This project failed because of the sequencing of decision elements required by the decision tree structure. As previously stated, the actions that a decision maker must consider are frequently not known prior to the circumstances which have prompted the current Decision Analysis and must be elicited. Pearl et al. [27] suggested that a goal driven approach which derives actions from goals, sub-goals and pre-conditions was more suitable for users.

Although it has not been automated, Owen [25] has shown that Influence Diagrams can be used for goal driven interactive model building. In this approach the goal is specified and expanded by posing questions such as “which value will help clarify this goal?”. The model can be developed at the relational level first and expanded at the numerical level as required.

A promising approach to the elicitation of decision structures is through text analysis. Text analysis is the processing of a fragment of text (as a document say) with the purpose of identifying the major elements of that fragment in the context of some target structure. This approach has been demonstrated using question and answer sequences for the analysis of the disposal of hazardous waste [37], and for the analysis of documents relating to foreign policy formulation by the Dutch government during World War 1 [9].

Gallhofer and Saris [9] describe a “bottom-up” process for the elicitation of decision trees in three parts, the coding of sub-trees from fragments of text, the combination of sub-trees and the development of an overview tree. To force the coders to better appreciate the main strategy they are also asked to briefly describe the strategies mentioned in each paragraph.

In this paper it is proposed that text analysis with Influence Diagrams as a target structure be used as a basis for knowledge acquisition in Intelligent Decision Systems. This approach is driven by the user and allows for the analysis of problems expressed in fragments of text such as a number of paragraphs. Such fragments of text are an appropriate communication medium for managerial users. Text is analysed and variables or more abstract descriptions of actions, events and goals elicited. The relationships are reduced to influences and informational links which can be used to build Influence Diagrams from the isolated elements.

With less well structured problems the approach to modeling is primarily exploratory. “Top down” progressive refinement is made possible by the ability to construct a hierarchy of Influence Diagrams [29]. Within each fragment of text different approaches may be taken to knowledge acquisition. The goal driven approach mentioned previously may be used, or relationships may be constructed in a forward manner, such as cause-effect, as advocated by Shachter and Heckerman [34]. The ability to represent problems at different levels of abstraction, and the separation of the relational and numerical representation help overcome human cognitive limitations in information processing.

The ability to interactively process diagrams at the numerical level will provide feedback necessary to focus attention on those parts of the problem about which there is least confidence or to which policy is most sensitive $[25]$ . Computational limitations will also be reduced. Strategic management problems require deep knowledge which can generate a large search space $[17]$ . The ability to deal only with those elements of the problem to which the outcome is sensitive can make the solution of such problems feasible.

An advantage of Intelligent Decision Systems is the potential for improved Natural Language Processing. There is difficulty in understanding unrestricted Natural Language input. Text analysis focuses on the location of a fixed number of components and their integration into an Influence Diagram. The aim is to build a proper Influence Diagram or an Influence Diagram which provides an unambiguos view of the world [33]. If user input is reasonably constrained to fit the target structure, the synthesis and checking of an Influence Diagram is an achievable task.

The combination of “top down” text analysis and real-time sensitivity analysis within the Decision Analysis framework is a promising means of providing the sort of effective support for the process of decision making which could be as easily and widely embraced as spreadsheet software. Even without the automation of text analysis it may provide the key to a “cookbook” style methodology which can be used, by analysts or in conjunction with some automation, to build Intelligent Decision Systems.

## Text Analysis for Intelligent Decision Systems

The overall process involves the successive analysis of text, numerical specification and sensitivity analysis. The following steps can be used to develop a “first cut” Influence Diagram.

Step 1. Write a description of the problem in simple declarative sentences.

This step overcomes the difficulty of reading sentences with complex clausal structures.

Step 2. Identify and isolate decision elements.

The major concepts can be listed and classified according to whether they are actions, events or outcomes. Rarely are these elements explicitly, completely and uniformly referenced in natural language and this step can require considerable analytical skill. Typical text includes a mixture of concepts, synonyms of concepts and values. This phase consists of the careful examination of noun phrases in the text.

Step 3. Establish relationships between decision elements.

The relationships between concepts are listed in pairs. Different types of relationships can be used in combining decision elements. Paradice [26] has described a number of relevant relationships.

(i) Causal relationships are typically established by verb phrases equivalent to “results in”, “leads to” and “initiates”. There are three conditions for a causal relationship; one event must precede a second event, there must be a relationship which can be formulated between two events and there must be some justification for believing the relationship is causal.

(ii) Derived or definitional relationships where one event is determined from another action or event. For example, Net Income can be readily determined from Sales and Total Costs. Such relationships are present for deterministic variables on an Influence Diagram.

(iii) Bounding relationships where one event determines the upper or lower limit of another. For example, the lower and upper limits for dividends are bounded by income.

Step 4. Draw Influence Diagram.

Examine each node and determine its type; decision, probabilistic event or deterministic event.

Step 5. Add Goal node.

Add goal and an arc from all events which influence the goal. A goal may not be explicitly defined or it may simply be concealed as an event.

At this point a first cut Influence Diagram has been developed. The next phase is to examine each of the nodes, to check for clarity and to expand them if necessary. By progressively refining the model the decision maker will move towards a requisite model and a policy with which he/she is satisfied.

## Example

The following is an example of a problem description which could be used as the basis for building the relational model shown in fig. 2.

Our main income is from insurance premiums. We aim to sell as many insurance policies as possible by designing policies which are attractive. The income from the insurance policies is used to generate further income from investments in shares, property, etc. We also derive some income from the sale of these investments from time to time.

We try to maximise retained earnings and to pay a satisfactory dividend to shareholders.

Our most critical decisions are the design of our policies as these affect the overall level of premiums we receive and the claims we must settle, and the design of our investment portfolio.

This description is a typical high level description of a strategic problem. It embodies a description of the business, the goals of the business and the major decisions. Such a description could easily be prepared by a high level manager and easily comprehended by the decision analyst. To facilitate analysis it is suggested that guidelines be prepared for the manager. These guidelines can be part of the entire process of developing an Influence Diagram from a problem or domain description. Whether it is accurate or not need be of no concern now. Typical analysis can be made as follows.

Step 1. Rewrite as simple sentences.

\- (main) income is derived from insurance premiums

\- (attractive) policy design leads to insurance premiums

\- income is derived from investments

– income is derived from investments sale

– retained earnings influence satisfaction

\- dividends influence satisfaction.

Step 2. Isolate decision elements.

\- insurance premiums (probabilistic variable)

– investment income (probabilistic variable)

\- dividends (decision)

\- net income (deterministic variable)

\- policy design (decision)

\- portfolio design (decision).

Step 3. Establish relationships. In this case we have added the tax rate relationship. This influence, although not indicated in the original problem statement, may emerge from common business knowledge associated with the definition of retained earnings.

<table><tr><td>policy design</td><td>influences</td><td>insurance premiums</td></tr><tr><td>investment portfolio design</td><td>influences</td><td>investment income</td></tr><tr><td>investment sales</td><td>influences</td><td>net income</td></tr><tr><td>investment income</td><td>influences</td><td>net income</td></tr><tr><td rowspan="2">insurance premiums (tax rate</td><td>influences</td><td>net income</td></tr><tr><td>influences</td><td>net income)</td></tr><tr><td>portfolio design</td><td>influences</td><td>investment income</td></tr><tr><td>portfolio design</td><td>influences</td><td>investment sales</td></tr></table>

Steps 4 and 5. Combine related concepts in an Influence Diagram and determine the goal node to produce the diagram shown in fig. 2(a).

The next step is to expand the model. Estimated (or historical) values and the variability of individual nodes can be assessed. The above model may reveal that insurance premium income is the most important variable contribution to net income. This node could be further expanded through text analysis to include further significant model elements such as re-insurance effects, claims and costs as shown in fig. 2(b). The process continues until the decision maker has a decision which is satisfactory and more importantly, understood.

The formalisation of text analysis may provide a basis for the automation of problem structuring in combination with the use of fragments of knowledge and advances in Natural Language Processing. Combined with the model refinement heuristics suggested by Moore and Agogino [22], it may be possible to develop software which supports the process of decision making. Such software must be able to handle very different levels of abstraction from the initial “back of the envelope” description to a highly detailed and quantified analysis.

Ultimately such software would have strong linguistic abilities, being able to build models from complex fragments of text by referencing, not only process knowledge, but factual and semantic knowledge from domain databases, commonsense business knowledge bases and previous decisions. Computational linguistics is hard and unrestricted natural language requires semantic analysis beyond the current capabilities of Computer Science. Even without automation, text analysis can be the basis of a manual methodology for the development of decision models much in the way that semantic data models are constructed [23].

## Further Research

This paper addresses a major deficiency, the absence of a methodology which supports the development of specific Intelligent Decision Systems by end-users. An obvious next step in this project is to empirically investigate the effectiveness of this approach in the development of decision models.

A number of other areas of potentially fruitful research have also emerged.

\- Process knowledge such as the heuristics that the expert decision analyst uses to guide problem structuring and sensitivity analysis have not been established.

\- Solution time may increase exponentially with problem size. A fruitful area of research may be to reason about Influence Diagrams and their solution. Rule processing produces a single model. Instead a number of models may be selected and a single model or Influence Diagram chosen on the basis of solution path [4 p. 120].

\- When introducing “canned” fragments from previous decisions it is necessary to validate these in the context of a new decision [11].

\- Intelligent Decision Systems are good at screening known options, however, a problem which needs addressing is the generation of suitable alternatives.

\- Decision Analysis, the modeling basis of Intelligent Decision Systems is not favoured by all personality types and there is no consensus about the factors which determine suitability for use by individuals. Howard [12] suggests that indicators such as the Myers-Briggs personality inventory may be useful in matching users to these decision making aids.

\- Integration with other sources of knowledge, such as semantic and factual knowledge in a domain database or a common sense knowledge base.

\- Subjective probability estimates may be biased.

## Conclusion

The combination of Expert Systems and Decision Analysis as Intelligent Decision Systems is a promising means of supporting complex, “one-off” and valuable decisions in the domain of strategic management. Intelligent Decision Systems extend the bounds of automated support to those problems for which conventional Expert Systems have failed to be successfully adapted and for which the methods of Decision Analysis have proven successful. An important component of Decision Analysis, the Influence Diagram, is especially important as a problem partitioning device, for model management and as a target structure for knowledge acquisition through text analysis.

## References

[1] Agogino, Alice M., and Rege, Ashutosh, IDES: Influence Diagram Based Expert System, Mathematical Modeling, V.8. (1987) 227–233.

[2] Blanning, Robert W., Issues in the design of expert systems for management, Proceedings of National Computer Conference (1984) 489–495.

[3] Brooks, Daniel G. and Kirkwood, Craig W., Decision Analysis to Select a Microcomputer Networking Strategy: A Procedure and a Case Study, J. Opl. Res. Soc. Vol. 39, No. 1 (1988) 23–32.

[4] Breese, John S., Knowledge Representation and Inference in Intelligent Decision Systems, Rockwell International Science Center Palo Alto Laboratory Research Report 2 (April 1987).

[5] Conway, Walter, Application of Decision Analysis to New

Product Development - A Case Study, in: Mitra, G, Ed., Computer Assisted Decision Making (North-Holland).

[6] Crawford, Stuart L., Fung, Robert M. and Tse, Edison, Data Driven Assessment and Decision Making, Proceedings of 2nd International IFIP/IFAC/IFORS workshop on Artificial Intelligence in Economics and Management, Singapore (Jan 9–13, 1989).

[7] Dhar, Vasant and Pople, Harry E., Rule-Based versus Structure-Based Models for Explaining and Generating Expert Behavior, Communications of the ACM, Number 6, Volume 30 (1987) 542–555.

[8] Elam, Joyce and Konsynski, Benn, Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences, Volume 18, No. 3 (1987) 487–501.

[9] Gallhofer, I.N. and Saris, W.E., A Coding Procedure for Empirical Research of Political Decision-making, in: Saris, William E. and Gallhofer, Irmtraud N., Eds., Sociometric Research: Volume 1: Data Collection and Scaling (Macmillan, London, 1988, ISBN: 0-333-43723-3).

[10] Hink, Robert F. and Woods, David L., How Humans Process Uncertain Knowledge: An Introduction for Knowledge Engineers, AI Magazine (Fall 1987).

[11] Holtzman, Sam, Intelligent Decision Systems (Addison-Wesley, 1989).

[12] Howard, Ronald A., Decision Analysis: Practice and Promise, Management Science, Vol. 34. No. 6 (1988) 679–695.

[13] Howard, Ronald A., 1980, An Assessment of Decision Analysis, Operations Research, Volume 28, No. 1 (1980) 4–27.

[14] Keeney, Ralph L., Building models of values, European Journal of Operational Research, 37 (1988) 149–157.

[15] Keeney, Ralph L., Decision Analysis: An Overview, Operations Research, Vol. 30., No. 5 (1982) 803–838.

[16] Keeney, Ralph L., Lathrop, John F. and Sicherman, Alan, An Analysis of Baltimore Gas and Electric Company's Technology Choice, Operations Research, Vol. 34., No. 1 (1986) 18–39.

[17] Kim, J. and Courtney, James F., A Survey of Knowledge Acquisition Techniques and their relevance to Managerial Problem Domains, Decision Support Systems, Vol 4 (1988) 269–284.

[18] Kirkwood, Craig W., A Case History of Nuclear Power Plant Site Selection, J. Opl. Res. Soc., Vol. 33, No. 4 (1982) 353–363.

[19] Leal, Antonio and Pearl, Judea, An Interactive Program for Conversational Elicitation of Decision Structures, IEEE Transactions on Systems, Man and Cybernetics, Vol. SMC-7, No. 5 (1977) 368–376.

[20] Liang, Ting-peng and Jones, Christopher, V., Meta-Design Considerations in Developing Model Management Systems, Decision Sciences, Vol 19 (1988) 72–92.

[21] McGovern, J. and Samson, D., Incorporating Expertise into Decision Analysis based DSS, Annals of OR: Linkages with Artificial Intelligence (1989).

[22] Moore, Eric A. and Agogino, Alice M., INFORM: an architecture for expert-directed knowledge acquisition, Int. J. Man-Machine Studies, 26 (1987) 213–230.

[23] Nijssen, G.M and Halpin, T.A., Conceptual Schemas and Relational Databases: A fact based approach (Prentice-Hall, 1989).

[24] O'Keefe, Robert M., Expert Systems and Operational Research – Mutual Benefits, J. Opl. Res. Soc., Vol 36, No. 2 (1985) 125–129.

[25] Owen, D.L., The use of Influence Diagrams in Structuring Complex Decision Problems, in Bunn, D.W., Applied Decision Analysis (McGraw-Hill, New York, 1984).

[26] Paradice, D.B., Databases and Knowledge Bases in Managerial Expert Systems, in Artificial Intelligence: implications for computer integrated manufacturing (1988) 403–432.

[27] Pearl, Judea, Leal, Antonio and Saleh, Joseph, Goddess: A Goal-Directed Decision Structuring System, IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol PAMI-4, No. 3 (1982) 250–262.

[28] Phillips, Lawrence, A Theory of Requisite Decision Models, Acta Psychologica 56 (1984) 29–48.

[29] Rege, Ashutosh and Agogino, Alice, Topological Framework for Representing and Solving Probabilistic Inference Problems in Expert Systems, Transactions of IEEE; Systems, Man and Cybernetics, Vol. 18(3) (1988).

[30] Russel, Stuart, Srinivas Sampath and Alice Agogino, Creating Influence Diagrams from Examples, Berkeley Expert Systems Laboratory, University of California, Berkeley (1988).

[31] Samson, Danny, Expected Utility Strategic Decision Models for General Insurers, Astin Bulletin, V165 (1986) 545–558.

[32] Shachter, Ross D., Probabilistic Inference and Influence Diagrams, Operations Research, Vol 36, No. 4 (1988) 589–604.

[33] Shachter, Ross D., Evaluating Influence Diagrams, Operations Research, Vol 34, No. 6 (1986) 871–882.

[34] Shachter, Ross D., and Heckerman, Thinking Backward for Knowledge Acquisition, The AI Magazine, Fall (1987) 55–61.

[35] Thomas, Howard and Schwenk, Charles R., Decision Analysis as an aid to Strategy, Management Decision, Volume 22, No. 2 (1984) 50–60.

[36] Ulvila, Jacob W. and Brown, Rex V., Decision Analysis comes of age, Harvard Business Review, September-October (1982) 130–141.

[37] Vari, Anna, Argumatics: A text analysis procedure for supporting problem formulation, Mass Communication Research Center, Budapest, Hungary (1987).

[38] Wallsten, Thomas S. and Budescu, David V., Encoding Subjective Probabilities: A Psychological and Psychometric Review, Management Science, Vol. 29, No. 2 (1983) 151–173.

[39] Walsh, James P., The Role of Cognition in Strategy Making: An Impirical Investigation, International Journal of Management, Vol. 5, No. 2 (1988) 188–200.

[40] Williams, Adrian J., Decision Analysis for Computer Strategy Planning, in: Mitra, G., Ed., Computer Assisted Decision Making (North-Holland, 1986).
