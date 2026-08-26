---
otero_id: 21723
otero_key: "N9E5WFX6"
title: "Representational congruence and information retrieval: Towards an extended model of cognitive fit"
authors: "Akhilesh Chandra; Ravindra Krovi"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00014-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Representational congruence and information retrieval: Towards an extended model of cognitive fit

Akhilesh Chandra <sup>a,)</sup>, Ravindra Krovi <sup>b</sup>

<sup>a</sup> School of Business and Economics, North Carolina A&T State UniÕersity, 1601 East Market Street, Greensboro, NC 27411, USA b Department of Management, College of Business Administration, The UniÕersity of Akron, Akron, OH, USA

Accepted 11 February 1999

## Abstract

The theory of cognitive fit suggests that a match between the problem representation and the task results in a better problem solving performance. In this paper, we extend the concept of cognitive fit to also account for the congruence between the external information and the internal representation of the user. This representational congruence and its effect on information retrieval are tested in an experimental setting. Subjects who are assigned to either of the two models of external representation propositional networks, PNs, and object-oriented, OO are provided domain-based information. AŽ . computer program, OBJECT\_IMAGE, is used to measure the reaction times and error rates of subjects on different attributes such as inheritance, message passing, and changing dynamics. The results favor the existence of OO-like features to attain cognitive economy in human information processing. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Representational congruence; Object-oriented; Propositional networks; Internal representations; Mental models; Cognitive economy; Cognitive fit; Information retrieval

## 1. Introduction

Internal representations are mental models employed by users to store and retrieve information. The mechanisms underlying these representations have always been a subject of intense research interest. However, the literature has yet to settle on an organizing principle, which elucidates the mechanics of human information processing. The experimental evidence has ranged in support for propositional networks hereinafter referred to as PNs 4 to otherŽ . models such as schemas 27 and frames 19 . Both<sup>w x</sup> <sup>w x</sup> schemas and frames appear to have some object-oriented hereafter, OO -like features such as hierarchi- Ž . cal classification and inheritance. Further motivation for considering OO cognition stems from claims made by proponents of OO design 7,11 , who have <sup>w</sup> <sup>x</sup> suggested that internal representations may have features similar to those employed by OO programming models. Such beliefs, when put in perspective with the concept of cognitive economy 26,32 , provide<sup>w</sup> <sup>x</sup> compelling reasons to test its validity through empirical support. However, the information systems literature lacks any experimental evidence that corroborates OO-like features of internal representation.

Information processing theory states that humans will employ strategies and representations that reduce the cognitive load 21 . This paper suggests that<sup>w</sup> <sup>x</sup> representational congruence is one way to reduce such a cognitive load. Similar in principle to the construct of cognitive fit 33,34 , representational <sup>w</sup> <sup>x</sup> congruence is the parity between information organization and internal representation.

The OO paradigm appears to offer several advantages to human information processing. First, principles of modularity and code reusability impart efficiency to OO-based programs if designed well . Ž . Inheritance of data and procedures is one of the primary causes of the existence of modularity and code reusability. Since business users are believed to process information in terms of objects, analysis of information using OO principles should be more effective and efficient than those using other competing models. Second, encapsulation of data and procedures within objects provides motivation for organizing and presenting information using the same techniques that are employed for the OO-based program designs. Third, objects are linked together through the message-passing feature that enhances the efficiency of programs. Presenting information to users in ‘chunks’ with embedded message-passing feature should improve user performance.

The objective in this paper is to test whether the PN model from the cognition literature or the OO model from the systems literature more closely aligns with the internal representation of users. This paper presents results of an experiment designed to test the effect on information retrieval of an interaction between information organization and internal representation. The efficiency and effectiveness of information retrieval are assumed to increase decrease Ž . with congruence non-congruence between informa-Ž . tion organization and internal representation. An inherent assumption in any such investigation is that information organization that best approximates internal representation should result in a faster and more error-free performance.

The knowledge of internal representation employed by users is critical from the perspective of information presentation to improve user performance. First, such an understanding should help in an efficient design of user interfaces. Second, it may enhance the effectiveness of requirements analysis in the application development process. Expectations of performance improvements are presumed because of the significance of intense and constant interaction between users and systems analysts<sup>r</sup>developers for a successful analysis and design effort. This is particularly significant in lieu of the popularity of OO analysis. Third, understanding the mechanics of human information processing may help increase the effectiveness of instructional delivery systems. Recent efforts to reengineer such systems have not addressed the issue of congruence of information organization with cognition 8,10 . Fourth, user cog- <sup>w</sup> <sup>x</sup> nition seems to be critical for the success of software engineering 1,22 25,39 .<sup>w</sup> <sup>x w</sup> <sup>x</sup>

The rest of this paper is organized along the following lines. Section 2 presents the theoretical basis for representational congruence and relates it to cognitive fit theory 34 . Section 3 summarizes the <sup>w</sup> <sup>x</sup> literature on various models of internal representation, and presents a conceptual foundation for a viable OO model. Section 4 uses an example based on the taxonomy of the animal kingdom to develop research hypotheses. The experimental design is discussed in Section 5, followed by the results of this study in Section 6. Section 7 discusses the implications and limitations of this research, and avenues for future extensions. This is followed by our conclusions in Section 8.

## 2. The theory of cognitive fit: an extended model

The theory of cognitive fit was initially proposed and tested by Vessey 34 to explain contradictory<sup>w</sup> <sup>x</sup> results in comparison studies of the effects of tables vs. graphs. Much of the initial research focused only on problem solving outcomes such as decision quality, decision confidence, and satisfaction. The problem solving process was largely ignored. The cognitive fit model was one of the first serious attempts at Ž . indirectly understanding the internal mechanisms of human problem solving. The basic model suggests that cognitive fit is the match between the problem Ž . or external representation and the problem solving task. A good fit results in a more consistent mental representation, which facilitates the problem solving process thereby leading to an efficient solution. This is represented in Fig. 1a. Since its inception, the model has been extended to include other variables such as problem solving skill 36 ; other domains<sup>w</sup> <sup>x</sup> such as programming 30 and requirements analysis <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 1 ; and data presentation variations such as multiattribute data 33 and maps 31 .<sup>w x</sup> <sup>w x</sup>

While the cognitive fit model is an excellent framework for understanding the relationship between problem representation and problem solving task, it does not explicitly account for either directlyŽ or indirectly specific internal representations and. their effect on the efficiency and effectiveness of information retrieval. We propose an extended model of cognitive fit and include another component called representational congruence please see Fig. 1b . Ž . Similar to cognitive fit, representational congruence is an emergent property resulting from the match between information organization <sup>1</sup> and internal representation. Performance during information retrieval is a function of the interaction between internal representation and the structural content of information organization.

![](/api/attachments/N9E5WFX6/fulltext/images/5c030ee797c09cf91870753e56d910dde58926a2bd5d09a1d19cc4f2fbef42fc.jpg)

![](/api/attachments/N9E5WFX6/fulltext/images/7d155e5b87a2bbaaaf427a0d0b3cd4fd2b582af17e728079f727dddbf2cf6ed2.jpg)

![](/api/attachments/N9E5WFX6/fulltext/images/fb2bdf137acb4e839cb3cee77adbcc01642c929f9779529228fb248ff54119d3.jpg)  
Fig. 1. a Cognitive fit model adapted from Vessey 34 . b Ž . Ž <sup>w</sup> <sup>x</sup>. Ž . Representational congruence. c Variable relationships.Ž .

Cognitive fit is a broad construct, which subsumes all elements of the problem solving process. Representational congruence is an extension of this theory with an emphasis on internal representation. The premise of the proposed model is that an emphasis on process focus of representational congruenceŽ . leads to an understanding of the effect on outcomes Ž . focus of cognitive fit in improving decision quality. Prior work using the cognitive fit model has attempted to match the task to methodologies e.g., Ž structured techniques, data flow diagrams, etc. . It. must be realized, however, that a range of methodologies exists in the systems design field 35 , and<sup>w</sup> <sup>x</sup> attempts at matching methodologies to task can become frustrating. A more efficient alternative is to structure the information that best aligns with the user’s cognitive model in a specific domain. Earlier studies have ignored information organization as a variable to infer user’s cognitive model. The lack of information organization variable may have accounted for the adverse findings in favor of the OO group in the experiment conducted by Agarwal et al. <sup>w</sup> <sup>x</sup> 1 . In proposing the representational congruence as an extension of the cognitive fit model, we seek to match users’ internal representation with information organization. The task characteristics then become an indirect variable since those characteristics can be modified in the information organization variable. It is expected that this extended model is richer in import and robust across tasks.

If there is parity between an already existing knowledge structure internal representation and in- Ž . formation organization, the problem solver is better able to match the latter to the internal knowledge, thereby, leading to better or more efficient navigational strategies. On the other hand, if there is a mismatch between internal representation and information organization i.e., information is presented in Ž a manner that is not congruent with internal representation , then the problem solver is forced to blend . incompatible structures resulting in memory loss and inefficiency. Hence, information retrieval with representational congruence should lead to efficient retention and recall.

## 3. Representation paradigms

Internal representations are mental models employed by users to store and retrieve information. Problem solvers attempt to match information organization with their preexisting knowledge structures. Such structures are important because efficient structures could lead to efficient problem solving strategies. Viewed another way, internal representations are generic strategies for representing information in the mind. They help to bring out relevant and essential domain aspects, and enable individuals to make inferences and predictions 17 . It is in this context<sup>w</sup> <sup>x</sup> that previous research has examined representations such as PN, frames, and schemas. However, agreement on a specific model of internal representation has been elusive 4,18,37 .<sup>w</sup> <sup>x</sup>

The models used to explain internal representation include schemas 27 , frames 19 , scripts 29 , and<sup>w x</sup> <sup>w x</sup> <sup>w x</sup> PNs 12 . The context in which these constructs have <sup>w</sup> <sup>x</sup> been proposed and used provides one of the primary sources of distinction between them 20 . These con-<sup>w</sup> <sup>x</sup> structs are briefly summarized below.

PNs see Appendix A for a brief PN exampleŽ . organize information into groups of nodes and links with meaningful associations 14,38 . A group of<sup>w</sup> <sup>x</sup> propositions containing the meaning of an event is interconnected to form a network. Nodes are propositions and arguments, while links are connections between nodes. The set of propositions is constantly reorganized into a hierarchical relationship where one proposition occurs as a unit within another proposition. Different propositions must be combined using relevant links to reflect meaningful information. Links between nodes are useful to infer and explain processing efficiency during information retrieval. For example, Collins and Quillian 12<sup>w</sup> <sup>x</sup> presented subjects with statements both true and Ž false about concepts in the animal kingdom, and . asked them to judge the truth of those assertions. Based on the time taken to answer different questions, they were able to infer that statements which connect concepts closer in the network were answered more quickly than those in which concepts were farther apart in the network. The general conclusion emerging from other similar studies 23<sup>w</sup> <sup>x</sup> points towards the fact that the retrieval time in PN is a function of the number of links traversed.

Both schemas and frames represent the structure of information. Schemas store general properties about categories. They exhibit inheritance of properties and processes, and the ability to generalize and specialize. Frames are hierarchical structures, and define specific attributes of an entity. The attribute and its value are held in a node with an associated slot. Less specific properties are found at higher levels of the hierarchy. An entity, which inherits upper level properties, fills its slots with default values. Information retrieval using schema or frames becomes a process of finding nodes that match the desired values. Scripts are special types of schemas, which store sequence of actions during an event.

Schema and frames have some OO-like features such as hierarchical classification and inheritance. But these two representational forms are not known to exhibit other features e.g., message passing ofŽ . the OO model. Message passing may affect cognitive economy, the presence of which has not been empirically documented using other forms of internal representation. A study providing evidence of message passing in cognition would lend support to the fact that knowledge is stored to achieve cognitive economy.

There are three reasons for focusing on OO-based representations. These are:

1. Some of the representational paradigms such as schemas and frames have OO-like features.

2. An OO-based representation provides for cognitive economy, thereby, further validating fundamental information processing theory 21,28 .<sup>w</sup> <sup>x</sup>

3. The concept of representational congruence could also have implications for user–analyst communications. Results of an OO-based internal representation could provide insights into ways of improving ‘OO analysis’, a popular requirements analysis technique.

The lack of accepted theories about internal representation presents a perplexing situation about the choice of a construct to serve as the control group. An obvious danger in choosing one over the other is to generate potentially conflicting hypotheses. Therefore, this paper adopts a more conservative approach by selecting the PN-based representation, which is a traditional construct of human cognition, and is very different from the OO model. As pointed out before, most of the other representations have some OO-like features and as a result would not serve as good candidates for a control group in an experimental setup.

Most prior research based on cognitive fit theory or on the effect of presentation modes has primarily focused on problem solving performance 1,5,13,<sup>w</sup> 15,24,30,31,33,34,36 . However, the literature has<sup>x</sup> yet to document and test the relationship between representational congruence and information retrieval. It seems a realistic assumption that congruence between internal representation and information organization should exist to achieve efficiency and effectiveness during information retrieval. Since internal representation is not directly observable, its model can be implied only by the relative performance during processing of various constructs embedded in information organization. Based on the proposed model of representational congruence, if internal representations are indeed OO-based, then we should expect to see better retrieval for an OObased information. On the other hand, better performance for PN-based information should provide for stronger evidence of internal representations that are inherently PN in nature. Accordingly, our main proposition is stated as follows:

More effective and efficient information retrieval results when the organization of information matches the internal representation of the user.

Information retrieval efficiency is measured by reaction time and effectiveness is measured by the error rate. The relationship between model type and dependent variables is shown in Fig. 1 c .Ž .

## 4. Research hypotheses

The experiment discussed in Section 5 uses anŽ . example based on the animal kingdom. Figs. 2 and 3 schematically describe two illustrations drawn from the animal kingdom example. The two illustrations are:

Ž .a Robin can fly.

Ž . b Cobra can be eaten by a bird.

Both illustrations are described using principles of OO and PN. The figure in the PN format consists of a network of propositions, each having an object, a subject, and the relationship feature. The OO format organizes this example in the form of various objects arranged hierarchically similar to a parent–childŽ relationship . Each object encapsulates data and pro-. cedures. Objects in dissimilar hierarchies e.g., birdŽ and reptile are related with the help of the. message-passing feature. Methods and procedures within an object are indented to capture encapsulation. Such arrangement of information to simulate OO features is consistent with the procedure used by Larkin and Simon 18 to represent diagrams. The<sup>w</sup> <sup>x</sup> two formats PN and OO are drawn to illustrateŽ . their respective theoretical foundations. Representations in the PN and OO formats are informationally equivalent but organizationally different.

The information processing time for PN is a function of the number of links traversed. Consider the following true–false question:

Robin can fly.

Both models begin processing the above assertion at the ROBIN node. The PN network and its OO

Propositional Network Representation

![](/api/attachments/N9E5WFX6/fulltext/images/bf6164ffc98dbe19fc5e4951ae3b7b9051d5f7664d76031400bd89463dc40946.jpg)  
Fig. 2. Representations of ‘Robin can fly’.

counterpart for this statement are shown in Fig. 2. An examination of the PN representation reveals that only two links will need to be traversed to answer this question. These two links are between:

## Robin is a bird, and Bird can fly.

The relation between these two links must be integrated to respond to the question. Implicit in the PN model is the concept of a relation between subjects. The network of relations requires traversal along the net during the retrieval and the processing of information. The longer the traversal path, the longer should be the expected retrieval and processing time.

In contrast, the OO model allows for properties to be inherited by the subordinate class es including Ž . Ž instances from a superordinate class. An object is a . repository of all information unless overridden orŽ cancelled by the instance object above its hierarchy.. This feature should eliminate the need for an upward traversal along the hierarchy to retrieve information. Thus, ROBIN object inherits the CAN FLY property from its super class BIRD. The inheritance feature is expected to increase efficiency during information processing by making it independent of the link traversal that is characteristic of the PN mode. It may also help preserve the cognitive economy and reduce redundancy. The foregoing expectations attributable to the inheritance feature lead to the following hypothesis expressed in its alternate form:

H : The mean reaction time for the OO treatment group is less than the PN control group for tasks requiring information retrieval along a hierarchy.

The disparity between the two models is further evident for a search requiring traversal across hierarchies. Consider the truthfulness of the following assertion:

## Cobra can be eaten by a bird.

This assertion contains two independent cues Ž . COBRA and BIRD to initiate information processing. The PN model see Fig. 3 requires that process-Ž . ing may begin at either the COBRA node or the BIRD node. Beginning at the COBRA node, the processing continues until it reaches the BIRD node; and examines all instances of BIRD to register any match. Such information processing requires traversal along two hierarchies covering at least a minimum of six links. If processing begins at the BIRD node, it may take one of the two routes. The first alternative takes the processing through the EAGLE node. In the second alternative, links are established through the ROBIN node. When the EAGLE node is selected, the search process would traverse only one link in order to provide an answer. Alternately, a total of three links would be traversed if the search goes through the ROBIN node in order to evaluate the truthfulness of the assertion. Thus, the PN-based processing would require, on an average, a traversal of three to four links.

![](/api/attachments/N9E5WFX6/fulltext/images/5b7fe720a463623177cf498a39b4653e57dede10220a6e093a1d95ed09a52d19.jpg)  
Fig. 3. Representations of ‘Cobra can be eaten by a bird’.

In contrast, the OO representation uses the message-passing feature to make direct connections between hierarchies. Message passing is assumed to be a natural metaphor for reducing cognitive strain to help reduce a broad search that is typical in a PN model. In this example, the COBRA object directly sends a message to the BIRD class, which checks all its instances i.e., ROBIN and EAGLE where theirŽ . respective services are stored. When the search goes through the EAGLE node, the assertion is evaluated in affirmative instantaneously since no connection needs to be made. Alternately, when the processing begins at the BIRD node, again the message-passing feature may not be invoked since an answer can be found by simply checking all the instances of the BIRD node and verifying the services embedded within them. Thus, the number of links traversed is few two, at the most primarily due to the message- Ž . passing feature that should prevent a complete hierarchy traversal. These expectations are formalized into the second hypothesis stated as below:

H : Regardless of the cue selected<sup>r</sup>provided, the mean reaction time for the OO treatment group is less than the PN control group for tasks requiring information retrieval across different hierarchies.

Information retrieval and decision making is affected by an interaction with the external world. Hence, any viable theory of representation should explain the evolution of existing knowledge-structure —How is new knowledge incorporated into an existing structure? Which of the two models of representation is more flexible and adaptable to account for changing information dynamics? Consider the following preexisting information:

Ž . A Frog is an amphibian.

The following sentence reflects new information:

Ž . B Amphibians liÕe in land as well as water.

![](/api/attachments/N9E5WFX6/fulltext/images/56a877c2c83819eb6b8e4250ffb008ce4d6f193f620ed54f2403fcc832c7be8e.jpg)  
Fig. 4. Incorporation of changing dynamics.

The objective is to judge the truthfulness of the following assertion:

Frog liÕes in land and water.

An answer to the above question requires adapting the new information B to the already existingŽ . knowledge structure A . Information processing ac-Ž . cording to the PN model requires an explicit association to be made between A and B . In the case ofŽ . Ž . the OO model, ‘FROG’ automatically inherits all properties of ‘AMPHIBIAN’ see Fig. 4 . Therefore, Ž . the OO model is expected to be efficient than the PN model in incorporating changing dynamics. These expectations are reflected in the third hypothesis stated in its alternate form as follows:

H : The mean reaction time for the OO treatment group is less than the PN control group for tasks requiring incorporation of additional information.

The primary method of information retrieval for the PN model is by means of traversal along the network. The larger the network, the more the traversal that will be required. This should impose cognitive load, thereby, increasing the probability of errors. In contrast, the inheritance and message-passing features of object orientation should result in a reduced incidence of such errors. Hence, expectations about the error rate are stated as follows:

1. The error rate for the OO treatment group is lower than the PN control group for tasks, which require information retrieval along a hierarchy.

2. The error rate for the OO treatment group is lower than the PN control group for tasks, which require information retrieval across different hierarchies.

3. The error rate for the OO treatment group is lower than the PN control group for tasks, which require the incorporation of additional information.

Six expectations formulated as hypotheses above can be categorized into two groups. First group tests differences between the OO and PN groups using the mean reaction time of information retrieval. The second group measures the error rate for the two groups. The two dependent variables, mean reaction time and error rate proxy the efficiency and effectiveness of a decision, respectively.

## 5. Experimental design

The research hypotheses are tested using an experimental design in which subjects are first presented with task related information, and then asked to respond to questions based on such information. This approach of drawing inferences about internal representation is methodologically sound and can be found in several psychological studies related to memory tracing see, for example, Ref. 4 .Ž <sup>w</sup> <sup>x</sup>.

A computer program called OBJECT\_IMAGE was developed to capture subjects’ responses, and their processing time. The mechanics and objective of this program is similar to the text editing and usability testing experiments discussed in Card et al. <sup>w</sup> <sup>x</sup> 9 . The use of computer programs to track cognitive behavior prevents measurement errors and enables precise recording of the processing time.

Fig. 5 provides an overview of the inputs and outputs of this program. The program presents the domain- and distracter-based information and records the response time of each subject for every query. Fig. 6 describes the sequence in which different steps of the experiment are executed. The program presents to subjects a set of screens in a specified order for a predetermined time. Subjects are automatically led from one screen to another except the instruction-screen where subjects can control the display time. A typical session starts with the instructionscreen, which describes the objective of this study, and specific steps subjects should follow during the experiment. The second screen displays domain information. After reading the domain information seeŽ Figs. 7 and 8 , subjects are presented with a dis-. tracter screen see Fig. 9 . Distracters are designed toŽ . prevent recency effects. The next set of screens prompts subjects with questions based on domain information see Fig. 10 . The fifth screen presentsŽ . new information to test the ability of the two models to incorporate the changing dynamics. This is followed by another distracter screen to minimize the recency effect. The final set of screens asks additional questions which combine the new information with the previous information. Subjects complete a demographic sheet towards the conclusion of the experiment.

The experimental task is derived from the taxonomy of animal kingdom. Some previous studies documenting the PN model have used the animal kingdom example. Since subjects in the control group of this study receive information organized according to propositions, and since this is the first study known Ž to the authors to test the validity of a competing . representation using the OO principles, keeping the same domain affords a better and realistic evaluation. A simple task also ensures that the subjects did not have to construct new representations. A complex task would have the confounding effect of subjects having to create new internal knowledge structures.

![](/api/attachments/N9E5WFX6/fulltext/images/34cdc44571803cdb8210b1ced2201c9277722cee6171e0c5957c7d5e7d4fd9d2.jpg)  
Fig. 5. OBJECT\_IMAGE overview.

![](/api/attachments/N9E5WFX6/fulltext/images/2ab14d791eb2a4897d3333eff8f0985fb7bc8f4ad3f35467c42a18994a4168a1.jpg)  
Fig. 6. Sequence of screens in OBJECT\_IMAGE.

The OO and PN scenarios derived from this example are shown in Figs. 7 and 8, respectively.

Both scenarios preserve the same information content required to answer questions; the two differ, however, in the arrangement of information. This is consistent with the objective of manipulating information organization. The composition and order of sentences are designed to capture essential features of the two models. The OO screen indents the relevant information to capture classes, class hierarchies, and class instances. As alluded to earlier, indenting information, to reflect the OO features, is similar to the methodology used by Larkin and Simon 18 . At<sup>w</sup> <sup>x</sup> each level, specific attributes and procedures are also provided. The PN screen is ordered in a breadth-wise fashion. It includes composite sentences to incorporate object–relation patterns among different concepts.

Fig. 7. Object oriented treatment.

Both the PN and OO groups present information in the form of ‘chunks’ per unit time. Thus, a chunk for the OO group refers to all information related to each class presented at a time see Fig. 7 . TheŽ . corresponding PN screen operationalizes ‘chunk’ by grouping object–relation patterns as shown in Fig. 8. As an illustration, information chunk in Fig. 7 uses OO principles to depict REPTILE class. It shows general attributes of reptiles at the higher level. Instances of this class are shown as indented information. Instances inherit general attributes from their

<table><tr><td>A frog is an Amphibian and is eaten by Pythons</td></tr><tr><td>Birds have feathers and move by flying</td></tr><tr><td>Small birds like a robin peck at their food</td></tr><tr><td>A Robin eats worms and is red in color</td></tr><tr><td>Large birds like an eagle swoop down on their prey</td></tr><tr><td>An Eagle eats Vipers</td></tr><tr><td>Reptiles are cold blooded, have scales, and move by crawling</td></tr><tr><td>Snakes like vipers are reptiles, which can be poisonous</td></tr><tr><td>A Python is a no poisonous snake that swallows humans by coiling around and suffocating its prey</td></tr><tr><td>Lizards have long tails</td></tr></table>

Fig. 8. Propositional network treatment.

superordinate class; they also add attributes<sup>r</sup>procedures specific to them. The procedure embodied in an object allows it to react to a message and communicate with other objects related to it either within the same or a different hierarchy. Nesting instance statements is an indirect approach to capture the features of the OO model. Fig. 8 presents the same information chunk organized according to the PN rules. The figure contains composite statements about facts. These statements do not have a parent–child relationship. If these facts were to be arranged in an object–relation–subject format, they would form a network of concepts in which case two or more statements would be combined to make decisions.

![](/api/attachments/N9E5WFX6/fulltext/images/952d643fe2958e3e93e49c0c49c00392249745aba7a79f299e7bd9d70bd2565e.jpg)  
Fig. 9. Distractor information.

<table><tr><td>Inheritance:</td></tr><tr><td>Robin can fly</td></tr><tr><td>Cobra is a reptile</td></tr><tr><td>Message Passing:</td></tr><tr><td>Cobra can be eaten by a bird</td></tr><tr><td>Reptiles eat robins</td></tr><tr><td>Changing Dynamics:</td></tr><tr><td>Frogs live in land and water</td></tr></table>

Fig. 10. Domain questions true or false .Ž .

In order to reduce the possible confounding effect of unfamiliarity with the keyboard and the terminal, the computer program records three measures of Ž . system time to compute the reaction time for each question. The counter for scan-time starts with the display of each question on the screen. The counter for start-time begins when the subject is in the typing mode; the computer program captures it with the typing of the first character. The end-time is measured at the completion of the typing mode; it is captured with the pressing of the RETURN key after the subject has entered the last character of the response. The reaction time is computed as the difference between the start-time and scan-time. The difference between the end-time and start-time measures the typing time.

The experiment was conducted in a computer laboratory at a medium size urban university. Sixty business majors participated in the experiment. The actual number of subjects varied according to the attempt and correctness of the question responded. Subjects were all business majors who had no prior experience with either model. This was critical because of two reasons. First, it has been shown that prior modeling experience can influence performance 2 . Second, real world users do not have<sup>w</sup> <sup>x</sup> modeling experience or background. Subjects were randomly assigned to one of the two groups, each representing either the OO or PN model. As can be seen from Table 1, both groups were distributed in similar proportions in the various demographic categories of gender, major, GPA, and computer experience. The computer program, OBJECT\_IMAGE, was installed in the lab in such a manner that the information organization PN or OO was alternated fromŽ . one terminal to another. Hence, there was an equal number of terminals with PN and OO mode of organization. Upon entering the lab, subjects were allowed to pick any terminal. Subjects were not aware of the information organization underlying the program. Subjects were informed at the beginning of the experiment that this would be part of a quiz to be graded based on the number of correct answers. This step was taken to ensure that the experiment was taken seriously by student subjects. It is a realistic assumption that in real life, most decisions are made without specifically cuing the decision-maker with the organization of information. Therefore, it was felt that providing training to subjects before presenting them the experimental task might bias results in favor of the OO model. Training was not provided also because the study did not measure the effect of modeling ability but the ability of the model orŽ modeling paradigm to be congruent with internal. representations of users. This experimental design also assumes that ceteris paribus, cognitive processing involves interaction of internal representation and information organization.

Table 1  
Demographic distribution of both groups

<table><tr><td colspan="2"></td><td>OO (%)</td><td>PN (%)</td></tr><tr><td rowspan="2">Gender</td><td>Male</td><td>32.8</td><td>32.7</td></tr><tr><td>Female</td><td>67.2</td><td>67.3</td></tr><tr><td rowspan="5">Major</td><td>Accounting</td><td>71.6</td><td>63.4</td></tr><tr><td>Finance</td><td>4.5</td><td>5.8</td></tr><tr><td>Management</td><td>4.5</td><td>3.8</td></tr><tr><td>Marketing</td><td>6</td><td>15.4</td></tr><tr><td>Other</td><td>13.4</td><td>11.6</td></tr><tr><td rowspan="4">GPA</td><td>Less than 2.5</td><td>18.9</td><td>19.5</td></tr><tr><td>2.51–3.0</td><td>23.1</td><td>23.2</td></tr><tr><td>3.1–3.5</td><td>27.1</td><td>26.1</td></tr><tr><td>3.51–4.0</td><td>30.7</td><td>31.2</td></tr><tr><td rowspan="3">Experience</td><td>0–2 years</td><td>9.2</td><td>9.1</td></tr><tr><td>2–5 years</td><td>30.7</td><td>31.8</td></tr><tr><td>More than 5 years</td><td>59.9</td><td>59.1</td></tr></table>

Table 2  
Effect of inheritance questions on reaction times

<table><tr><td></td><td></td><td>Mean</td><td>Standard deviation</td><td>n</td><td>p-Values</td></tr><tr><td>Question 1: (True/False)</td><td>PN</td><td>294.45</td><td>225.60</td><td>51</td><td> $0.045^a$ </td></tr><tr><td>Robin can fly</td><td>OO</td><td>240.16</td><td>101.35</td><td>60</td><td></td></tr><tr><td>Question 2: (True/False)</td><td>PN</td><td>545.63</td><td>425.41</td><td>36</td><td>0.12</td></tr><tr><td>Cobra is a reptile</td><td>OO</td><td>452.83</td><td>282.39</td><td>42</td><td></td></tr></table>

<sup>a</sup>Significant at 5% alpha level.

Table 3  
Cumulative results for both models

<table><tr><td>Both questions combined</td><td>Mean (reaction time)</td><td>Standard deviation</td><td>n</td><td>p-Values</td></tr><tr><td>PN model</td><td>398.39</td><td>344.57</td><td>87</td><td> $0.045^a$ </td></tr><tr><td>OO model</td><td>327.74</td><td>222.34</td><td>102</td><td></td></tr></table>

Significant at 5% alpha level.

## 6. Results

The hypotheses grouped according to dependent variables are designed to test information retrieval on a set of three features: inheritance, message passing, and changing dynamics. The efficiency of retrieval based on the reaction time is analyzed for only correct responses. The test of significance is performed on the mean system-time taken to respond to questions. Wrong answers are not considered in the statistical analysis of reaction times. The effectiveness of retrieval based on error rates measures the proportion of incorrect responses for the two groups. Results are presented for reaction times and error rates together for each criterion.

The first hypothesis tests the effect on the reaction time due to the inheritance feature. Table 2 presents p-values corresponding to the one-tailed t-test for each of the two questions that measure performance due to the inheritance of information. The result is significant at 5% confidence level for the first question $\big ( \boldsymbol { p } = 0 . 0 4 5 \big )$ . But the p-value is not significant for the second question. However, the mean reaction time for the PN group is less than that of the OO group. Further, when we combined both questions and tested for cumulative differences between the two models, the OO model was significantly efficient than the PN model please see Table 3 . TableŽ . 4 reports error rates for the two inheritance-based questions. It is revealed that error rates are approximately close for both the models and, therefore, it appears that the inheritance feature of the OO model did not provide a major advantage from the perspective of effective recall.

Table 4  
Effect of inheritance questions on error rates

<table><tr><td></td><td></td><td>Error rate (%)</td><td>Average (%)</td></tr><tr><td rowspan="2">PN</td><td>Question 1</td><td>1.9</td><td>16.35</td></tr><tr><td>Question 2</td><td>30.8</td><td></td></tr><tr><td rowspan="2">OO</td><td>Question 1</td><td>10.4</td><td>23.90</td></tr><tr><td>Question 2</td><td>37.3</td><td></td></tr></table>

Table 5  
Effect of message-passing questions on reaction times

<table><tr><td></td><td></td><td>Mean</td><td>Standard deviation</td><td>n</td><td>p-Values</td></tr><tr><td>Question 1: (True/False)</td><td>PN</td><td>1139.80</td><td>647.77</td><td>10</td><td> $0.00^a$ </td></tr><tr><td>Cobra can be eaten by a bird</td><td>OO</td><td>643.00</td><td>546.09</td><td>38</td><td></td></tr><tr><td>Question 2: (True/False)</td><td>PN</td><td>631.38</td><td>353.98</td><td>26</td><td> $0.09^b$ </td></tr><tr><td>Reptiles eat robins</td><td>OO</td><td>523.65</td><td>319.05</td><td>44</td><td></td></tr></table>

<sup>a</sup>Significant at 1% alpha level.  
<sup>b</sup>Significant at 10% alpha level.

The second hypothesis tests the message-passing property of the OO model. Table 5 summarizes the one-tailed t-test for this analysis. It may be observed that the mean reaction times for both questions are lower for the OO treatment group compared to the PN group. Statistical significance is found for one question at 1% significance level $( \boldsymbol { p } = 0 . 0 0 )$ , and the other question at 10% significance level $( p = 0 . 0 9 )$ Table 6 presents the cumulative results of both the models and it can be seen that there is significant overall support for OO being the more efficient model $( p = 0 . 0 0 )$ . An abnormally high error rate for the PN model please see Table 7 as compared toŽ . the OO model further confirms our initial expectations of the synergy gained through message passing between objects. In the case of the PN group, a possible lack of congruence between information organization and internal representation may have adversely affected information retrieval.

Table 6  
Cumulative results for both models

<table><tr><td></td><td>Mean</td><td>Standard deviation</td><td>n</td><td>p-Values</td></tr><tr><td>PN model</td><td>772.61</td><td>311.90</td><td>36</td><td> $0.00^a$ </td></tr><tr><td>OO model</td><td>578.96</td><td>500.74</td><td>82</td><td></td></tr></table>

<sup>a</sup>Significant at 1% alpha level.

Table 7  
Effect of message-passing questions on error rates

<table><tr><td colspan="2"></td><td>Error rate (%)</td><td>Average (%)</td></tr><tr><td rowspan="2">PN</td><td>Question 1</td><td>80.8</td><td>65.4</td></tr><tr><td>Question 2</td><td>50.0</td><td></td></tr><tr><td rowspan="2">OO</td><td>Question 1</td><td>43.3</td><td>38.8</td></tr><tr><td>Question 2</td><td>34.3</td><td></td></tr></table>

Finally, the effect of incorporating the changing dynamics is tested by the third hypothesis. Table 8 presents the results for the changing dynamics feature. It is noted that the OO treatment group registered a lower mean reaction time compared to the PN group. But the one-tailed t-value is not significant at a conventional level of confidence. Further, Table 9 exhibits a lower error rate for this question within the PN group. The error rate result for the changing dynamics feature is contrary to the hypothesized expectations. Clearly, it appears on the surface that the PN model is better able to account for additional information and is more dynamic. A possible explanation for such an anomaly could also be that either the question-set or the case material could not convincingly capture the complexity of processing involved in incorporating additional information.

Table 8  
Effect of additional information on reaction times

<table><tr><td></td><td></td><td>Mean</td><td>Standard deviation</td><td>n</td><td>p-Values</td></tr><tr><td>Question: (True/False)</td><td>PN</td><td>422.33</td><td>361.95</td><td>48</td><td>0.40</td></tr><tr><td>A frog lives in land and water</td><td>OO</td><td>405.09</td><td>354.37</td><td>61</td><td></td></tr></table>

Table 9  
Effect of additional information on error rates

<table><tr><td></td><td>Error rates (%)</td></tr><tr><td>PN</td><td>9.0</td></tr><tr><td>OO</td><td>7.7</td></tr></table>

## 7. Discussion

The results of this study can be discussed from two separate viewpoints. First, the retrieval process seems to benefit when information organization is congruent with internal representation. Overall findings for the message-passing feature provide some evidence that information may be represented in the OO mode. Information organization incongruent with internal representation as evidenced for the PNŽ group deteriorated retrieval efficiency. However, ef-. ficiency and effectiveness appear to be superior in a network mode for tasks requiring the incorporation of additional information.

Second, internal representation does not appear to always process information in the PN mode as advocated by its proponents. Specifically, results suggest that message passing an OO feature is utilized toŽ . retrieve information. Absence of this feature in information organization for the PN group adversely affected the performance of subjects in the experiment. Among the three features tested in this study, both inheritance and message-passing-based questions provided a relatively better evidence for the presence of OO in internal representation. These findings lend empirical support to the theoretical contention that internal representation stores information to reduce redundancy and achieve cognitive economy.

It is well known that correct problem definition and requirements analysis are essential prerequisites for the success of the software process. The primary objective of this research is to gain a better understanding of internal representations during human information processing. Based on some of the results obtained, systems analysts should orient their analysis and acquisition strategies around user mental models. Further, user interfaces congruent with user representations have the potential to be more flexible and adaptive to dynamic user behavior.

We submit that this is the first systematic cognitive experimental study known to authors that in-Ž . vestigates the OO model as a natural metaphor for internal representation; although many researchers and practitioners have made claims for such a premise. Our basis for comparing the OO model with PN-based representation stems from fundamental similarities of PN models with process models used in the industry. Both models are inherently hierarchical level in nature please see Appendix A . Fur- Ž . Ž . ther, both models potentially evolve into a network architecture. Information is believed to traverse by forming meaningful associations between nodes both in PN and process models. The results of this study do suggest the presence of OO features in internal representations. However, the findings presented in this paper are inconclusive; at best, these are preliminary in import, and are relevant only within the bounds of the current study. Any assertion about internal representation being linked to OO mode must obviously await the consistent findings across extensions and replications in diverse domains. Hence, the prior discussion should be evaluated against the backdrop of ‘some initial’ evidence for the OO-like mechanics of cognition for some attributes.

The study also assumed that the very nature of cognitive economy rejects any mode of information organization that is incongruent with the user’s internal representation. That is, we attribute all significant results to the presence of the congruence construct. However, it is not clear whether the organization of information could be used to modify the structure of internal representation beyond mere interference. It could also be possible that internal representation could have multiple forms varying with the task or problem domain. Variations of domain knowledge according to soft vs. hard, procedural vs. declarative, interpretive vs. analytical, and static vs. dynamic model should provide a multidimensional view of internal representations. Future extensions of the study need to consider these factors as well as provide generalizations of these results in a corporate setting.

## 8. Conclusions

The cognitive fit theory considers the effect of synergy between problem representation and task on problem solving performance. In this study, we extended this model to account for the parity between information organization and internal representation. The study investigated the effect of organization of information presented to the user on the retrieval performance. The general hypothesis of congruence between information organization and internal representation was tested on a set of three features, i.e., inheritance, message passing, and changing dynamics. Two sets of dependent variables—reaction times and error rates—measured the efficiency and effectiveness of the retrieval process, respectively. The findings reveal that information is differentially represented for making effective and efficient retrieval. The inheritance and the message-passing feature generated a relatively better performance, which lends credence to the presence of assumed cogni-Ž . tive economy advocated in the cognition literature.

![](/api/attachments/N9E5WFX6/fulltext/images/15a34ae0f42f61c49615ad8ae53b8f56bd5e26475bfed6eb870511fddf6750dd.jpg)  
Fig. 11. A sample propositional network adapted from Anderson 4 . Ž <sup>w</sup> <sup>x</sup>.

Our results have significant implications for the presentation of information and systems design in general. Designers need to take into account the mechanics of the retrieval efficiency or effective-Ž ness when presenting information to users. Training . material should be designed to achieve representational congruence. The nature of the retrieval process is likely to differ between strategic, tactical, and operational decisions. Information systems should appropriately organize information for different types of decisions to enhance the user’s efficiency and effectiveness.

The congruence issue is particularly relevant in a systems design project where the analyst attempts to elicit information requirements in a way that directly maps to the implementation model. A representational incongruence might result due to a disparity between the user’s internal representation of his<sup>r</sup>her world of application domain and that of the analyst’s mechanics of implementation. This in turn affects the completeness and accuracy of the requirements specification process potentially resulting in poorer system quality.

## Appendix A. Propositional network-based representation

A proposition is the most basic fact about a concept. Hence, a group of propositions combined in an integrated network form a meaningful event. PNs organize ideas as groups of nodes and links with meaningful association. Each node connects to another node via an Is-a link. For example, the Shark node see Fig. 11 is connected to the Fish node,Ž . reflecting an Is-a property or an instantiation. Associated with each node are also subject–relation or subject–relation–object patterns. For example, Canary is a node which has attached to it a subject–relation pattern; i.e., ‘Canary is Yellow’. On the other hand, Robin is a node which includes a ‘subject–relation–object’ pattern; i.e., ‘Robin eats worms’. Propositions must be combined through the relevant links to reflect meaningful information. Thus, the retrieval time in a PN is a function of the number of links traversed. As a result, it is expected that the time taken to judge the truthfulness of ‘Robin eats worms’ where the number of links traversed isŽ zero , should be less than that of ‘Robin has skin’ . Ž . where the number of links traversed is two . Based on such time measurements, researchers 3,11,22<sup>w</sup> <sup>x</sup> have deduced the kind of knowledge network shown in Fig. 10. Studies investigating PNs also document that retrieval time within a node i.e., subject–rela-Ž tion or subject–relation–object patterns is affected. by the frequency with which it is invoked. A higher frequency about a node has the effect of increasing the strength of its association with that relation.

## References

<sup>w</sup> <sup>x</sup> 1 R. Agarwal, A. Sinha, M. Tanniru, Cognitive fit in requirements modeling: a study of object and process methodologies, Journal of Management Information Systems 13 2Ž . Ž . 1996 137–148.

<sup>w</sup> <sup>x</sup> 2 R. Agarwal, A. Sinha, M. Tanniru, The role of prior experience and task characteristics in object oriented modeling: an empirical study, International Journal of Human Computer Studies 45 1996 639–667.Ž .

<sup>w</sup> <sup>x</sup> 3 J.C. Anderson, P.M.J. Reckers, An empirical investigation of the effects of presentation format and personality on auditor’s judgment in applying analytical procedures, Advances in Accounting 10 1 1992 19–43.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 J.R. Anderson, Cognitive Psychology and its Implications, 3rd edn., Freeman, New York, 1990.

<sup>w</sup> <sup>x</sup> 5 J.R. Bettman, P. Kakkar, Effects of information presentation format on consumer information acquisition strategies, Journal of Consumer Research 3 1977 233–240.Ž .

<sup>w</sup> <sup>x</sup> 6 Benbasat, A.S. Dexter, An experimental evaluation of graph-

ical and color enhanced information presentation, Management Science 31 1985 1349–1364.Ž .

7 G. Booch, Object Oriented Design with Applications, Benjamin Cummings Publishing, Reading, MA, 1991.

<sup>w</sup> <sup>x</sup> 8 R.P. Bostrom, L. Olfman, M.K. Sein, The importance of learning style in end-user training, MIS Quarterly 14 1Ž . Ž . 1990 101.

<sup>w</sup> <sup>x</sup> 9 F.K. Card, T.P. Moran, A. Newell, The Psychology of Human Computer Interaction, Erlbaum, Hillsdale, NJ, 1983.

<sup>w</sup> <sup>x</sup> 10 J. Chadwick, How learning is aided by technology, Link-Up 12 1 1995 16.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 P. Coad, E. Yourdon, Object-Oriented Analysis, Yourdan Press<sup>r</sup>Prentice-Hall, Englewood Cliffs, NJ, 1991.

<sup>w</sup> <sup>x</sup>12 A.M. Collins, M.R. Quillian, Retrieval time from semantic memory, Journal of Verbal Learning and Verbal Behavior 8 Ž .1969 240–247.

<sup>w</sup> <sup>x</sup> 13 G. DeSanctis, Computer graphics as decision aids: directions for research, Decision Sciences 15 1984 463–487.Ž .

<sup>w</sup> <sup>x</sup>14 A.C. Graesser, L.F. Clark, Structures and Procedures of Implicit Knowledge, Ablex Publishing, New Jersey, 1985.

<sup>w</sup> <sup>x</sup> 15 S.L. Jarvenpaa, The effect of task demands and graphica format on information processing strategies, Management Science 35 3 1989 285–303.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 S.L. Jarvenpaa, G.W. Dickson, Graphics and managerial decision making: research based guidelines, Communications of the ACM 31 6 1988 764–774.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 P.N. Johnson-Laird, Mental Models, Harvard University Press, Cambridge, MA, 1983.

<sup>w</sup> <sup>x</sup> 18 J.H. Larkin, H.A. Simon, Why a diagram is sometimes Ž . worth ten thousand words, Cognitive Science 11 1987Ž . 65–99.

<sup>w</sup> <sup>x</sup> 19 M. Minsky, A framework for representing knowledge, in: P.H. Winston Ed. , The Psychology of Computer Vision, Ž . McGraw-Hill, New York, 1975.

<sup>w</sup> <sup>x</sup> 20 G. Nakamura, B.A. Kleiber, K. Kim, Categories, propositional representations, and schemas: test of a structural hypothesis, American Journal of Psychology 105 4 1992Ž . Ž . 575–590.

21 Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

<sup>w</sup> <sup>x</sup> 22 D.E. O’Leary, Software engineering and research issues in accounting information systems, Journal of Information Systems, 1988 24–38.Ž .

<sup>w</sup> <sup>x</sup> 23 R.A. Ratcliff, G. McKoon, Priming in item recognition: evidence for the propositional structure of sentences, Journal of Verbal Learning and Verbal Behavior 17 1978 403–417.Ž .

<sup>w</sup> <sup>x</sup>24 W.E. Remus, An empirical investigation of the impact of graphical and tabular data representations on decision making, Management Science 30 5 1984 533–542.Ž . Ž .

<sup>w</sup> <sup>x</sup>25 J.H. Reneau, S.V. Grabski, A review of research in computer-human interaction and individual differences within a model for research in accounting information systems, Journal of Information Systems, 1987 33–53.Ž .

<sup>w</sup> <sup>x</sup> 26 E. Rosch, Principles of categorization, in: E. Rosch, B.B.

Lloyd Eds. , Cognition and Categorization, Erlbaum, Hills- Ž . dale, NJ, 1978, pp. 27–48.

<sup>w</sup> <sup>x</sup> 27 D.E. Rumelhart, Schemata: the building blocks of cognition, in: R. Spiro, B. Bruce, W. Brewer Eds. , Theoretical IssuesŽ . in Reading Comprehension, Erlbaum, Hillsdale, NJ, 1980, pp. 33–58.

<sup>w</sup> <sup>x</sup> 28 D.E. Rumelhart, P. Lindsay, D.A. Norman, A process model for long term memory, in: E. Tulving, W. Donaldson Eds. ,Ž . Organization of Memory, Academic Press, New York, 1972.

<sup>w</sup> <sup>x</sup> 29 R.C. Schank, R. Abelson, Scripts, Plans, Goals, and Understanding, Erlbaum, Hillsdale, NJ, 1977.

<sup>w</sup> <sup>x</sup> 30 A.P. Sinha, I. Vessey, Cognitive fit: an empirical study of recursion and iteration, IEEE Transactions on Software Engineering 18 5 1992 368–380.Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 J.B. Smelcer, E. Carmel, The effectiveness of differential representations for managerial problem solving: comparing tables and maps, Decision Sciences 28 2 1997 391–420.Ž . Ž .

<sup>w</sup> <sup>x</sup> 32 E.E. Smith, Concepts and thought, in: R.J. Sternberg, E.E. Smith Eds. , The Psychology of Human Thought, Cam- Ž . bridge Univ. Press, Cambridge, 1988, pp. 19–49.

<sup>w</sup> <sup>x</sup>33 N.S. Umanath, I. Vessey, Multiattribute data presentation and human judgement: a cognitive fit perspective, Decision Sciences 25 5 1994 795–823.Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 I. Vessey, Cognitive fit: a theory based analysis of the graphs versus tables literature, Decision Sciences 22 1991 219–Ž . 241.

<sup>w</sup> <sup>x</sup> 35 I. Vessey, S. Conger, Requirements specification: learning objects, process, and data methodologies, Communications of the ACM 37 1994 102–113.Ž .

<sup>w</sup> <sup>x</sup> 36 Vessey, D. Galleta, Cognitive fit: an empirical study of information acquisition, Information Systems Research 2 1Ž . Ž . 1991 63–84.

<sup>w</sup> <sup>x</sup> 37 J.R. Wilson, A. Rutherford, Mental models: theory and application in human factors, Human Factors 31 1989 617–634.Ž .

38 K.V. Wilson, From Associations to Structure, North-Holland, Amsterdam, 1980.

<sup>w</sup> <sup>x</sup> 39 D.D. Woods, Cognitive technologies: the design of joint human-machine cognitive systems, The AI Magazine, 1985Ž . 86–92.

![](/api/attachments/N9E5WFX6/fulltext/images/aa6a98d3562d69180541ef4f0bd967e872df7925c7e5e4b00dc40223afba7eb3.jpg)

Akhilesh Chandra is an Assistant Professor of Accounting Information Systems at North Carolina A&T State University. He works in the field of cognitive implications of technology on decision making, where he has published in numerous journals. He is active in several professional organizations including the American Accounting Association Žtogether with AI<sup>r</sup>ET, AIS, ABO sections , Association for Information Sys-. tems, and Decision Sciences Institute

His training and preparation include those in public accounting practice and government agencies.

![](/api/attachments/N9E5WFX6/fulltext/images/ae575d3c9e5c93d07c748d4395ab5ed2842acd877bda41a35eb1888fdfa1cdb2.jpg)

Ravindra Krovi received his PhD in Management Information Systems from Memphis State University in 1993. His prior background and training includes Degrees in Engineering and Computer Science. He has served as a faculty member at Southern Arkansas University, North Carolina A&T State University, and the University of Akron. He has consulted in the areas of electronic commerce, production scheduling systems, and data mining. He has published

in several reputed journals including IEEE Transactions on Systems, Man, and Cybernetics, and the European Journal of Operational Research. His research interests are in the areas of artificial intelligence applications.
