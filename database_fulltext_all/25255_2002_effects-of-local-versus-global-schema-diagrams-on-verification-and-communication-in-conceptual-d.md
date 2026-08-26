---
otero_id: 25255
otero_key: "WBDW7NDD"
title: "Effects of Local Versus Global Schema Diagrams on Verification and Communication in Conceptual Data Modeling"
authors: ""
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045730"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effects of Local Versus Global Schema Diagrams on Verification and Communication in Conceptual Data Modeling

Jeffrey Parsons

To cite this article: Jeffrey Parsons (2002) Effects of Local Versus Global Schema Diagrams on Verification and Communication in Conceptual Data Modeling, Journal of Management Information Systems, 19:3, 155-183

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045730

![](/api/attachments/WBDW7NDD/fulltext/images/583750d2970f985a265f54fb9a3298840721adf9ee97052b987b6633d71c538f.jpg)

Published online: 23 Dec 2014.

![](/api/attachments/WBDW7NDD/fulltext/images/a316450b3fa0ca43628e54a923d15c46f073452920f5183bf52b64696cb8e610.jpg)

Submit your article to this journal

![](/api/attachments/WBDW7NDD/fulltext/images/c2927ffcd42394896ad6b4e7fb20b5443902ede3e5d36dba7ec1d9fcb2e16b7c.jpg)

Article views: 8

![](/api/attachments/WBDW7NDD/fulltext/images/0b35eafd05c389b292bd7e556eaf7613b5f8ce4aeb62334d144a6875a34a6a13.jpg)

View related articles

# Effects of Local Versus Global Schema Diagrams on Verification and Communication in Conceptual Data Modeling

JEFFREY PARSONS

JEFFREY PARSONS is Professor of Information Systems in the Faculty of Business Administration at Memorial University of Newfoundland. He received a Ph.D. from the University of British Columbia. His research interests include systems analysis and design, database management, and electronic commerce. His research has been published in journals such as Management Science, Communications of the ACM, and ACM Transactions on Database Systems, and has been presented at numerous conferences. In 2001, he was Program Co-Chair of the Workshop on Information Technologies and Systems.

ABSTRACT: Much research in conceptual data modeling has focused on developing techniques for view integration, or combining local conceptual schemas into a global schema. Local schemas are argued to be important in verifying conceptual data requirements before proceeding to database design. View integration is claimed to fulfill two purposes. First, a global conceptual schema is a prerequisite to logical design and implementation. Second, global schemas are thought to be useful in improving organizational communication among diverse user groups with different perspectives and information needs. However, performing view integration is difficult. Moreover, there is no empirical evidence that global schemas either impede local verification or support communication. Drawing on classification research, this paper develops and tests claims about the impact of schema structure (local versus global) on verification and communication. Local schemas are hypothesized to better support verification than global schemas. When different local views contain conflicting structure, loca schemas are expected to be superior in supporting communication. However, when local views contain complementary structure, global schemas are expected to be superior in supporting communication. A laboratory experiment was conducted to test these predictions. The results support the hypotheses. Implications for the practice of database design and for further research are considered.

KEY WORDS AND PHRASES: classification theory, conceptual database models, database schemas, empirical data modeling research, view integration.

THE GROWING SCOPE AND COMPLEXITY OF information systems has been accompa nied by an ongoing interest among both researchers and practitioners in developing useful methods and techniques to support various aspects of information systems development. Much of this activity has focused on developing new techniques for modeling data requirements and business or information systems processes. In data modeling, the Entity-Relationship (ER) model [11] has had considerable impact on research and practice. Since its publication, the ER model (and its closely derived offspring, the class model of the Unified Modeling Language [UML]) has gained wide acceptance as a conceptual data modeling technique. It contains a small number of simple modeling constructs that enable the development of conceptual schema diagrams that clearly communicate data requirements. Over the years, additional research has been done to increase the power and usefulness of the model by adding modeling constructs [34, 35].

Despite the attention to developing and extending the ER model, a relatively small amount of research has focused on evaluating the technique empirically. In general, such studies have looked at issues related to the ease of constructing diagrams using the technique (such as among novices and experts) and the quality or comprehensi bility of diagrams produced with it (for example [4, 5, 6, 7]). Some studies have compared the ER model with other data modeling or requirements analysis techniques, such as the relational model [8, 19], NIAM [20], or an object model [31]. More recently, some research has looked at the usefulness of ER representations in problem-solving contexts and the role of optional and mandatory properties [9, 16].

As the ER model grew in popularity, the practical need to employ it in large and complex data modeling applications led to the emergence of view integration as a major research area within conceptual data modeling [2, 3, 25]. In a large data modeling project, there can be many groups of users, each having different, partial views of the conceptual data requirements for an application. Since conceptual data models are intended to reflect the requirements of users, creating separate local schema diagrams to reflect distinct views is a reasonable approach given the need to verify with users the quality of the conceptual model before proceeding to logical database design and implementation. View integration techniques provide mechanisms to combine several partial local conceptual schema diagrams into a consistent, global schema diagram that constitutes an overall picture of data requirements. The global schema serves as a blueprint for implementation, as there is a well-defined procedure for converting a single conceptual schema into a relational database design.

In addition to this technical rationale for performing view integration, a global schema may improve organizational communication by showing a “big picture” that places the local data requirements of one user or group in the larger context of the data requirements of other users or groups. In this way, a group of users may become aware of other data in the organization that may be valuable to the group, thereby facilitating knowledge management and enhancing decision-making by providing access to data from multiple units or functions. Modern enterprise resource planning (ERP) systems typically have an integrated global data model that is used to show the “big picture” of organizational data [21]. However, despite the appeal of the argument, there is no empirical evidence that a global schema in any way improves organizational communication, as previous empirical studies on the ER model have dealt exclusively with a single conceptual schema or view.

This paper empirically evaluates the contribution of conceptual schema diagrams to both verifying partial views and improving communication. We introduce classification research as a theoretical foundation for predicting: (1) that maintaining distinct local schema diagrams leads to improved local verification, and (2) the conditions under which local versus global schema diagrams lead to better organizational communication. We describe a laboratory experiment testing hypotheses derived from these predictions, present the results of the experiment, and discuss the implications of our findings. Finally, we consider implications for practice and identify avenues for additional research.

## Local and Global Conceptual Schemas

A VARIETY OF MODELING TECHNIQUES, including the ER model and closely related object-oriented techniques such as class diagrams in the UML, advocate “identifying classes” of entities as one of the first and most important activities in conceptual data modeling (for example [10, 13, 14, 18, 29]). It is clear, however, that different groups in an organization may identify different classes of interest. For example, in a univer sity domain, libraries may be interested in entities like “book” and “journal,” which are not of interest to the registrar’s office. Moreover, libraries and registrars are likely to be interested in different attributes, and possibly not exactly the same instances, of entities such as “student.”

The prevailing strategy for handling multiple views in conceptual data modeling is to first model the information structure of each view as a separate conceptual schema diagram, termed a local schema. Each local schema represents a partial structure of the data requirements for the database. Subsequently, the local schemas are combined in a process called view integration. Several local schemas (also called external schemas), consisting of classes of interrelated entity types defined by attributes, are merged into a single global schema diagram. This global schema reflects the total information structure of the application, and is constructed prior to logical database design [25]. Such techniques are heavily emphasized in standard database textbooks (for example [15, 34]). Moreover, the growth of the Internet and e-business has greatly increased the availability of diverse independent information sources having differen conceptual schemas, and thereby accelerated the need for information integration [30]

In the case of ER schemas, view integration is performed by applying structural rules to combine entity types, relationships, and attributes, and by resolving naming and semantic conflicts that arise between local schemas, such as synonyms and homonyms. Research in this area has focused on developing and automating rules for integrating various components of local schemas into a global schema (for example [3, 25]). The primary rationale for view integration has been to develop the global schema diagram as a blueprint for the logical design and implementation of an information system [15].

For this purpose, schema integration is regarded as essential since each local schema contains only partial information, and there may be conflicts or inconsistencies between different views that must be resolved before a database is implemented. Algorithms exist to convert a global schema to a logical (relational) design [15]. No such algorithm is available for creating an integrated logical design from a set of local schemas. In fact, it has been proposed that the prevailing practice that logical database design starts from a single conceptual schema diagram underlies much of the database research on view integration [26]. This, in turn, may be an artifact of the dominance of “class-based” data models, such as the relational model, in database management systems. Class-based databases must have a definition of the database in the form of a schema [3, p. 325]. If methods or logical models existed for implementing a system directly from multiple local schemas, schema integration might be unnecessary to support logical design.

However, a conceptual model is important for other reasons [22]. Foremost, there is inevitably a degree of interpretation in conceptual modeling. The conceptual schema constitutes a medium by which designers express their understanding of the domain diagrammatically to users so that users can verify whether the interpretation reflects their perspective. Users should find it easier to verify local schemas—based on thei own perspective—than to verify relevant parts of a global schema that includes irrelevant (from that perspective), and possibly conflicting, information.

Although neither the “verification” nor “blueprint” rationale justifies the use of a global schema from a representational perspective, Batini et al. [3, pp. 327–328] have argued that a global conceptual schema also serves as a shared resource for users in understanding how their local information structure fits with those of other users or groups. In other words, a global schema may improve organizational communication and knowledge sharing by serving as a map that enables users to position their view on the information structure of the organization in a larger context, and to understand the extent to which their view is shared with, or common to, other views [24]. Unde this rationale, differences in users’ views can be communicated more effectively through a global conceptual schema. For example, two user groups may use the nouns “client” and “account” to refer to the same category of entities. This can be shown more clearly on a single integrated schema diagram than on two distinct local diagrams.

The discussion thus far outlines the informal rationales for using local and globa schemas in conceptual data modeling, as advocated by proponents of view integra tion techniques. Next, we offer a theoretical framework and analysis of the relative merits of local and global schemas for verification and communication.

## Theoretical Framework and Propositions

LOCAL AND GLOBAL SCHEMA DIAGRAMS typically consist of classes. In the case of the extended ER (EER) model [34], the classes are entity types defined by attributes and relationships, and linked by relationships, generalization/specialization hierarchies, and aggregation. Resolving differences between classes or entity types is a critical task in schema integration [15]. Given the pervasiveness of classification in data modeling, we turn to classification theory, a branch of cognitive science, for theoretical guidance on the relative merits of local and global schemas in conceptual data modeling.

## Classification Theory

CLASSIFICATION IS A FUNDAMENTAL ACTIVITY by which humans group individual things into categories based on similarity [33]. Classification theory seeks answers to two principal questions: (1) Why do people classify? and (2) What is a class?

Regarding the first question, it is well established that classification serves three primary functions [33]. First, classes provide cognitive economy, meaning that classifying things reduces the mental burden of remembering information about them. Instead of having to keep track of all the facts that a person knows about everything separately, one defines categories of things that have common properties and keeps track of the properties with the class. For example, suppose a university requires that every student take at least one course. The effort required to remember this fact is much less if we associate the property “takes a course” with the class “student” than if we associate the property with each individual student in the university.

Second, classification supports inference, meaning that people can reason about instances based on the classes to which they are assigned. For example, one typically classifies a thing based on observing a subset of its properties, and infers additional properties the thing possesses by virtue of being a member of the class, even if these properties are not observed [28, 32]. This affords tremendous survival value, as classifying an entity based on incomplete information (such as seeing flame) allows us to infer the presence of as yet unobserved properties (such as heat).

Third, classification enables communication. Much communication involves reference to classes, or to things as members of classes [32]. To the extent that people share common class definitions, effective communication is facilitated. Where class definitions differ, effective communication will be inhibited to the extent that the parties involved are unable to pinpoint these differences. Problems in communication are largely a consequence of the extent to which the participating parties attach different meanings or definitions to the same terms, or the same meaning to different terms, and are unable to identify the precise nature of those differences [23, pp. 304–337].

Regarding the question of what a class is, various models have been proposed [33]. Despite their differences, all models of classification share the idea that a class is an abstraction of similarity among individual things. In addition, current theory holds that classes are simply artifacts constructed by humans to abstract useful (for econom and inference) similarities among things [23].

The idea of usefulness is context-dependent. Certain distinctions that may be usefu to people in certain circumstances (such as a skier who distinguishes varieties of snow depending on factors such as moisture content) may not be useful in a differen context (such as a person who is seeing snow for the first time). Consequently, there are many ways of modeling a given domain in terms of classes. People abstract different classification structures, defining classes and their associations, based on thei varying needs. This helps explain why problems of miscommunication arise—there is no single, shared classification scheme for the objects in the world [23].

## Implications for Local Versus Global Schemas

Classification theory accounts for the potential multiplicity of classification structures across people and over time based on varying usefulness. One of the objectives of conceptual data modeling is to graphically represent the classification structure of a domain. Therefore, in situations involving many users, who may find different abstractions useful for their work, multiple classification structures or views are to be expected and should be accommodated in conceptual data modeling [27].

Classification theory also predicts that problems in communication arise from the inability of people with different classification structures to identify differences between their views. Therefore, in situations involving multiple users and views, data modeling practices will facilitate or inhibit communication to the extent to which they enable these differences to be identified.

Based on these two observations, we next develop three general theoretical propositions regarding verification and communication.

## Local Verification

A global schema diagram describes an aggregate, and implicitly “shared,” classifica tion structure. Since conceptual models are intended to be good reflections of the world as perceived by humans, the use of global schemas in conceptual data model ing is, therefore, inconsistent with the notion that there may be no single “shared” classification structure for a domain. View integration effectively imposes a single artificial classification structure for the purpose of database design, even if that structure does not reflect the perspective of organizational members.

A global schema diagram by definition contains extraneous, and possibly conflict ing, information from the perspective of any single user and is, therefore, more complex than a local schema diagram. For example, a global view may include entity types, attributes, and relationships not included in a local view. Therefore, one would expect users to perform more poorly on tasks involving verifying their classification structure using a global schema diagram that embeds that structure within a larger structure than using a local schema diagram intended to directly reflect that structure. This leads to the first proposition:

Proposition 1 (LV): Users will be better able to verify local classification structure from a local schema diagram than from a global schema diagram.

## Communication

A global schema integrates two or more local schemas corresponding to different user views. The key issue in determining whether local or global schemas enhance communication is the extent to which each allows users with a particular view to understand the classification structure associated with other views.

To the extent that the classification structures of two views are the same, this reflects shared class definitions between the user groups involved. Such commonality will be represented the same way when modeled using local schemas (the same structure will appear in each of the views) or global schemas. In this case, since there are no differences to be resolved, there is no opportunity for miscommunication.

More interesting issues in communication arise when there are differences between views, since these differences give rise to miscommunication if they cannot be resolved. Differences in classification structure between views can be of two types. First, each view may constitute a partial structure involving some (but not all) of the same concepts [1]. For example, a primary interest in a registrar’s view of students may involve the relationships between students and courses (when taken, grades received, and so on). In contrast, a primary interest in a library’s view of students may involve the borrowing relationships between students and library materials. In this case, each view can be seen as capturing distinct, but complementary, parts of a more complex structure. The concept of student is common to both views, whereas those of course and library material are each relevant to only one of the views.

From the perspective of users holding one of the two views, the communication issue is the extent to which local versus global schema diagrams better enable users to integrate the other perspective with their own. Such integration might be demon strated by the ability of users to answer questions that require combining comple mentary information from their local view and the other view. Since a global schema depicts this integrated perspective, it will better facilitate this sense of communica tion. In contrast, the use of local schemas would require users to perform schema integration in order to answer questions requiring the combination of information from both schemas.

The second type of difference between classification structures in two views arises when there is conflicting information in each view. Conflicts can arise only with respect to those entity types that are common to two or more local schemas (common associations or attributes imply common entity types) and which, thereby, are intended to model the same domain concepts. A conflict means that two (or more) views “tell a different story” about a common aspect of the domain. Conflicts are potentially resolvable within the context of a global view, and therefore should be distinguished from contradictions in which there can be no resolution that satisfies the contradicting views [1, p. 18]. Several types of conflict are possible. First, a local schema and a global schema can disagree on the attributes of an entity type (as a result of schema integration, the global schema can contain attributes that are not deemed to belong to the entity type from the perspective of some local view). This type of conflict is different from the case of partial views discussed above. The conflict deals with structure (namely, entity types) common to two or more local views, but defined differently (in terms of attributes) under each view, instead of structure (entity types) contained in only one of the two views.

Second, a local schema and a global schema can disagree on whether an entity type may or must participate in a relationship that is common to two or more views, since participation can be optional under one view, but mandatory under another. For example, in the university case previously mentioned, the financial aid office may require that every active student be registered in at least one course (that is, mandatory relationship), since they define students by eligibility for financial aid. In contrast, the undergraduate studies office may view the relationship as optional (such as students may not take courses during a particular semester). A global schema that resolves this apparent inconsistency by showing the relationship as optional will conflict with the financial aid office’s view.

Third, local and global schemas can disagree on type hierarchies. This is particu larly true if a global schema contains a generalization of specific entity types taken from the views involved, where this general type is not defined in any view.

In such cases, local schemas preserve and highlight differences among views, whereas a global schema can mask them. From a communication perspective, using local schemas will better enable users to understand another view to the extent that it conflicts with their own view.

Based on this analysis, we make the following propositions regarding communica tion:

Proposition 2a (C-a): Users will be better able to understand a complex classification structure that integrates complementary views by examining a globa schema, rather than by examining distinct local schemas.

Proposition 2b (C-b): Users will be better able to understand the classification structure of other users with conflicting views by directly examining the other users’ local schemas, rather than by examining a global schema.

Another way of viewing these propositions is that the ability to interpret information from conceptual schema diagrams is determined by an interaction between the type of diagram (local versus global) and the nature of the interpretation task (interpreting an integrated structure versus interpreting a view that contains conflicting information).

## Research Method

## Experimental Design

THE PROPOSITIONS DEAL EXPLICITLY WITH the ability of users to understand classification structure contained in a set of local schemas versus a single integrated schema, and not on issues involved in constructing local versus global schema diagrams. Hence, a task in which participants are provided with schemas and asked to answer questions about the subject matter supports a more direct test of the propositions than one in which they are asked to construct schemas. Relevant criteria in such extraction tasks include the accuracy with which subjects can answer questions and the time required to extract correct information.

The independent variable is the form of representation. To maintain a reasonable level of complexity in the task, two levels of this independent variable were chosen: a single global schema and a set of two local schemas.<sup>1</sup> The global schema was produced by applying schema integration rules to the local schemas. After the globa schema was constructed, a complete mapping between schemas was conducted to verify that the information content of the two forms of representation was identical.

The primary dependent variable, our operationalization of “understanding,” is the ability of participants to correctly interpret information from a conceptual schema diagram. This was measured directly by the number of correct responses on identical questionnaires administered to each of the experimental groups. The responses measure ability to interpret information from a single global schema versus a set of two local schemas containing the same information. A second dependent variable of potential interest is the time required to extract information under each treatment. Time may be a useful secondary measure of the “naturalness” of a representation if treatments do not yield significant differences in accuracy. This was measured by recording the time required by each participant to complete the questionnaire.

## Task Domain

The key issue in selecting a task domain was to isolate the effect of the form of representation (local or global schemas) from extraneous factors that could confound the results. One can manage many such factors for which there may be variation among participants (such as intelligence, motivation) by both randomly assigning participants to experimental groups (see the next subsection) and selecting relatively similar participants (such as students). However, in the absence of having organiza tional participants involved in a real application,<sup>2</sup> one important confound may persist despite randomization—namely, prior knowledge of the task domain. For many conceivable domains, similar experimental participants might have a relatively homogeneous level of background knowledge that would influence how they interpreted local or global schema diagrams associated with that domain.

For example, if a university domain was chosen, one might expect student partici pants (all of whom have had similar experiences with the university) to come to the task equipped with a relatively homogeneous view of what should be the conceptual schema of that subject matter. As a result, questions about “another view” (such as the school of graduate studies) might in fact be answered by participants based on thei prior knowledge as students, rather than on the information given in the conceptual schema diagrams. In such a setting, a question such as “Do all graduate students have supervisors?” might be answered based on a student’s experience or commonsense interpretations (for example, “All the graduate students I know have supervisors; therefore, I believe the answer is ‘yes’”), rather than on the possibly quite different domain semantics of the experimental task. In such a case, prior knowledge may interfere with any effects due to the use of local versus global schemas in the task.

Alternatively, one can avoid the problem described above by choosing a domain about which participants have little or no prior knowledge.<sup>3</sup> However, for most “realistic” domains, it may be difficult to do this. For example, suppose that a domain such as pharmaceutical manufacturing was used for the task. By using “real” terms, such as scientist, laboratory, and drug, participants would bring some background knowl edge to the task. Therefore, questions might be answered based on that background knowledge, interfering with any effects caused by the independent variable.

In view of the inherent difficulties associated with eliminating the effect of back ground knowledge on any “real” task domain, a purely artificial task domain was constructed to ensure internal validity. An arbitrary naming scheme containing no real-world concepts was used in the material presented to participants. All entity type, attribute, and relationship names were thus randomly selected and semantically devoid. This ensured that participants extracted information from the diagrams based on their understanding of the semantics of the modeling constructs, rather than on their prior knowledge of the terms used in the diagram. Appendix A contains the narrative describing the local view that all participants in the study were asked to assume.

Given this artificial domain, it is natural to question the representativeness of the study since, in practice, users bring background knowledge and “common sense” to the task of interpreting a conceptual schema diagram. However, since this study focuses only on differences in information extraction from global and local conceptual schema diagrams based on the semantics of the modeling constructs (entities, attributes, relationships, cardinality, type hierarchies), the introduction of a context through a task involving familiar entities is unnecessary. Therefore, the use of a contrived domain is appropriate for an initial test of the theory, and sets the stage for future research that examines the research questions in a real organization setting (see the “Conclusions and Future Research” section).

A second critical issue regarding the task and materials is reflecting the role of user views in the experimental task, as called for by both propositions. Using an artificial domain means it is not possible to have views that are based on prior knowledge. However, the objective in developing a global conceptual schema is to represent tota information requirements that combine and resolve inconsistencies among two or more partial schemas. One way to simulate this is to expose participants to a narrative containing a partial (relative to the model depicted in a global schema) description of the artificial domain corresponding to the information contained in the local schema diagram.

In this study, the simulation took the form of a briefing in advance of exposure to the schema diagram(s). Participants were provided with a written narrative describ ing their view of the information model for purposes of the experimental task and asked to act as if this narrative described their view of the organization. The narrative consisted of statements describing the entity types, the attributes of entity types, the relationships between entity types, and generalization/specialization hierarchies (see

Appendix A). This ensured participants were exposed to a subset of, but not the entire, domain of interest. In this context, “local” simply means having prior exposure to a narrative description of the domain.

## Participants and Procedure

Thirty-four volunteers from an introductory undergraduate information systems course were recruited to participate in the study. Volunteers were prescreened. To be consis tent with the research objective of studying local and global schemas from the point of view of users (as opposed to database specialists) and to eliminate possible effects associated with variations in data modeling experience, only participants with no previous exposure to data modeling or other database experience were selected.

In order to eliminate systematic effects from other variables, participants were randomly assigned to either the local schema (Local) group or the global schema (Global) group. Participants were told the purpose of the study was to “test which of a number of methods of displaying information is easiest for people to understand.” They were told the activities involved and asked to sign a consent form.

Since none of the participants had previously been exposed to ER diagrams, a common training session was held for both groups to ensure that they received identica training. In the session, participants were given a fifteen-minute tutorial on EER modeling. Each participant received a handout containing the tutorial and the trainer went through this handout thoroughly. The tutorial first explained the semantics of the basic symbols used in EER diagrams (entity type, relationship type, attribute, and connecting line) and used example diagrams to illustrate these constructs. Next, extended constructs were explained and demonstrated (generalization/specialization, connectivity constraints). Then, rules for integrating or combining diagrams to form a global schema were introduced through an example that integrated the diagrams used in the previous two examples.

After the tutorial, participants worked through a sample questionnaire containing ten questions that covered the EER concepts introduced. Participants were given time to complete the questionnaire, after which the trainer went over each question giving the correct answer and an explanation.<sup>4</sup> During this feedback component, partici pants asked questions about anything they did not understand

Next, participants were sent to two different rooms based on the experimental group to which they were assigned. There they were given instructions for the experimental task. Each group was told they would be given a paragraph describing the information requirements for a hypothetical organization (Appendix A), and were asked to assume this paragraph described their view of the organization, for which a database is to be developed. They were told that the entity type, attribute, and relationship names were invented, and to “pretend they are meaningful for the hypothetical organization.” They were told they would be given a few minutes to review the narrative, after which an EER diagram based on the narrative would be distributed. Participants in group Local were told there would be two separate diagrams, one reflecting the view contained in the paragraph, and the other the view of another group of people in the organization (see Appendix B). The “remote” view differed from the “partici pant” view on a number of dimensions. It contained entity types and their attributes (Alphas, Deltas), and a relationship (Heltify) not present in the participant view, as well as additional attributes (such as attribute H of Gammas), and varying relation ship cardinalities (such as on the relationship Antilate).

Participants in group Global were told that the diagram would contain “all the information in the written narrative, plus additional information that reflects additional data requirements of other users in your organization” (see Appendix C). Participants were also told they could refer to the training materials in reviewing the diagram.

Next, participants in each group were presented with the same narrative (Appendix A); participants in group Local were given two partial schema diagrams (Appendix B) and those in group Global were given a single global schema diagram (Appendix C). Five minutes were allocated to read and internalize the narrative, and another five to review the diagram and compare it to the written narrative. A questionnaire was then distributed containing questions about various aspects of the data model (Appendix D).

## Questionnaire Design and Testing

An initial set of questions was developed according to four EER constructs about which questions could be asked. Table 1 lists each construct and a sample question covering that construct.

The questions were treated in one of two ways for scoring. Most questions required a true/false or yes/no response. One point was awarded for a correct answer and zero points otherwise. Some questions asked participants to list attributes or relationships. Rather than ask individual questions about whether a particular attribute belongs to an entity type, it was more natural to ask for a list of the attributes of that entity type (since listing the attributes of an entity type is the major task in identifying how an entity type is defined). Each correct item listed in the response was awarded one point. Although asking for a list of attributes of an entity type produces higher overall composite score numbers relative to asking whether or not a particular attribute belongs to that type, it does not affect the comparison between Local and Global groups. The number of incorrect responses (such as attributes listed for an entity type tha were incorrect based on the diagram[s]) was also measured.

Classifying questions by type of EER construct is useful for generating possible items for the questionnaire; however, this is not adequate for testing the verification and communication propositions. Verification questions deal with information contained only in the local schema diagram, whereas communication questions deal either with information that must be combined from local and “remote” partial diagrams, or with information that can be extracted from the remote diagram that conflicts with information from the local diagram. In that context, from the perspective of the Loca group, the initial set of questions can be seen as belonging to four types based on the strategy and effort required to answer them correctly. Type 1 (Look Local) questions could be answered correctly by looking only at the schema corresponding to the local view. Clearly, these are relevant in testing the verification proposition but do not aid in testing the communication propositions. Type 2 (Look Remote) questions could be answered correctly by looking only at the schema corresponding to the other view, and deal with entities, attributes, or relationships that were not described in the narra tive given to participants. Type 3 (Look Both) questions could be answered correctl only by looking at both schemas, since they necessitated combining information from the two views. Finally, Type 4 (Look Remote, Local Conflicting) questions could be answered by looking only at the other schema, but incorrect answers may be more likely due to conflicts with the local view. Questions of Types 2 through 4 are relevant to communication, rather than verification. This classification is summarized in Table 2. A sample question of each type is given in Table 3, along with the rationale for the classification.<sup>5</sup> As the rationales indicate, Type 1 questions deal only with information from the schema diagram corresponding to the local schema; Type 2 questions dea only with information from the diagram corresponding to the remote schema; Type 3 questions deal with information that spans both diagrams; and Type 4 questions dea with information that is completely expressed in the remote diagram, but which is incompletely (and therefore inconsistently) expressed in the local diagram.

Table 1. Sample Question for Each EER Construct Tested

<table><tr><td>Construct</td><td>Sample Question</td></tr><tr><td>Attribute</td><td>List the attributes of Epsilon.</td></tr><tr><td>Relationship</td><td>Is there a relationship between Gammas and Epsilon?</td></tr><tr><td>Type hierarchy</td><td>Is every Alpha also an Omega?</td></tr><tr><td>Synonym</td><td>Do Epsilon and Sigmas refer to the same entity type?</td></tr></table>

A pretest conducted with 13 participants from a database class, randomly assigned to one of the two groups, revealed patterns generally consistent with the expected relationships, and showed that the task and instructions were clear (the overall correct score in the pretest was 86.4 percent). However, the pretest also clearly indicated an imbalance between types of questions. As a result, additional questions were added to the questionnaire. The final questionnaire is contained in Appendix D. Appendix E contains the complete classification of questions by type.

## Operational Hypotheses

The general propositions developed earlier can now be operationalized in conjunc tion with the classification in Table 2 as follows.

H1: For Type 1 (Look Local) questions, group Local will outperform group Global.

This operationalizes the local verification proposition (LV). LV states that users will be better able to verify their local classification structure given a local schema diagram than when the local view is embedded in a global schema. Type 1 questions involve only verifying local classification structure.

Table 2. Classification of Questions by Strategy Required of Group Local Participants

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Must look at local schema to answer correctly</td></tr><tr><td>Yes</td><td>No</td></tr><tr><td rowspan="2">Must look at remote schema to answer correctly</td><td>Yes</td><td>Type 3</td><td>Type 2, Type 4</td></tr><tr><td>No</td><td>Type 1</td><td>—</td></tr></table>

Table 3. Sample Questions by Strategy Required of Group Local Participant

<table><tr><td>Question</td><td>Question type</td><td>Explanation</td></tr><tr><td>List the properties of Omegas</td><td>1. Look local</td><td>Remote schema contains no “Omegas” entity type</td></tr><tr><td>List the properties of Epsilon</td><td>2. Look remote</td><td>Local schema contains no “Epsilon” entity type</td></tr><tr><td>Is every Alpha also Alphas</td><td>3. Look both</td><td>Must compare properties of (from the remote schema) and Omegas (from the local schema)</td></tr><tr><td>an Omega?</td><td></td><td></td></tr><tr><td>H is a property of Gammas</td><td>4: Look Remote/local conflicting</td><td>Local schema contains incomplete information, suggesting an incorrect answer (i.e., that H is not a property of Gammas)</td></tr></table>

H2: For Type 2 (Look Remote) questions, groups Local and Global are expected to perform equally well.

In Type 2 questions, the information needed to answer a question correctly appears identically in both groups. In group Local, participants get the information from the remote schema. In group Global, participants get the information from the global schema. There is no reason, based on the underlying theory, to expect a difference in performance of the two groups for this type of question. Since the theoretical propo sitions do not predict performance with respect to this type of question, Hypothesis 2 is included in null form simply to complete coverage of the four types of questions from Table 2.

## H3: For Type 3 (Look Both) questions, group Global will outperform group Local

This hypothesis operationalizes the first communication Proposition (2a). Type 3 questions deal with an integrated classification structure. To answer these questions correctly, participants in group Local must combine information from their local schema diagram with information from the remote schema representing another view. However, participants in group Global can answer such questions simply by reading the information off the global schema diagram, which contains the integrated information. Type 3 questions essentially require the participant to perform schema inte gration “on the fly” to provide correct answers. Since schema integration is known to be difficult, we expect participants in group Global to outperform participants in group Local on this subset of questions, as the integration has been performed for them in advance.

H4: For Type 4 (Look Remote/Local Conflicting) questions, group Local will outperform group Global.

Hypothesis 4 operationalizes the second communication Proposition (2b). Questions of this type deal with conflict between local schemas. For users in one group to understand the information requirements of users in another group, the users’ local classification structure provides a reference point for understanding what is different about the view of the other group. Maintaining local schemas allows users to high light these differences, whereas integrating views into a global schema masks the differences among local views.

Table 4 summarizes the operational hypotheses.

## Results

THE MAXIMUM POSSIBLE SCORE on the questionnaire was 43. There was no signifi cant difference in the mean total score between group Local and group Global (71.8 percent versus 76.7 percent). Not surprisingly, overall performance for these novices appears to be lower than the pretest scores involving participants with data modeling experience (74.3 percent versus 86.4 percent).<sup>6</sup> These overall differences cannot be interpreted with respect to the operational hypotheses, however, since the expected relative performance of the two groups varied with question type.

Based on the classification of questions summarized in Appendix E, there is one dependent variable (sum of scores on questions in that category) associated with each of the four hypotheses. Each hypothesis makes a priori predictions about differences in scores between the Local and Global groups based on the relative cognitive effort involved in answering questions that require or do not require the participant to perform schema integration. Therefore, it is appropriate to test each hypothesis as if it were the only one under consideration rather than make a Bonferroni-style adjust ment to the a-level to account for multiple dependent variables [12, 17].

A separate t-test was performed for each of the four hypotheses. Table 5 shows the results for each of the hypotheses.

As expected, Hypothesis 1 was supported; participants in group Local performed significantly better than those in group Global. Local schema diagrams appear to support local verification better than global schema diagrams.

There was no evidence to reject Hypothesis 2 (framed as a null hypothesis), which is consistent with the idea that there is no reason to expect differences in local versus global schemas when the information in question appears identically in both forms.

The results show strong support for Hypothesis 3. Participants in group Local fared significantly worse than those in group Global, lending empirical evidence to the notion that a global schema is better suited than a set of local schemas for communi cating information about combined, complementary classification structure.

<table><tr><td>Question type</td><td>Hypothesis</td><td>Rationale</td><td>Number of questions in category</td></tr><tr><td>1. Look local</td><td>Local &gt; Global</td><td>“Noise” in Global</td><td>6</td></tr><tr><td>2. Look remote</td><td>Local = Global</td><td>No basis to expect difference</td><td>8</td></tr><tr><td>3. Look both</td><td>Local &lt; Global</td><td>Local performs integration “on the fly”</td><td>10</td></tr><tr><td rowspan="2">4. Look remote/ local conflicting</td><td rowspan="2">Local &gt; Global</td><td>Local highlights differences</td><td></td></tr><tr><td>Global masks differences</td><td>6</td></tr></table>

<sub>4.Sum</sub><sup>maryofHypoth</sup>

<sub>.t-TestResult</sub><sup>sbyHypot</sup>

<table><tr><td rowspan="2">Question type</td><td rowspan="2">Hypothesis</td><td colspan="2">Mean</td><td colspan="2">Standard deviation</td><td rowspan="2">Levene F</td><td rowspan="2">t</td><td rowspan="2">Significance</td></tr><tr><td>L</td><td>G</td><td>L</td><td>G</td></tr><tr><td>Look local</td><td>L &gt; G</td><td>6.80</td><td>5.57</td><td>1.15</td><td>1.50</td><td>1.138</td><td>2.484</td><td>0.01</td></tr><tr><td>Look remote</td><td>L = G</td><td>6.93</td><td>7.00</td><td>1.79</td><td>1.52</td><td>1.350</td><td>0.108</td><td>n.s.</td></tr><tr><td>Look both</td><td>L &lt; G</td><td>8.80</td><td>12.57</td><td>1.47</td><td>1.70</td><td>1.611</td><td>6.403</td><td>&lt;0.001</td></tr><tr><td>Look remote/remote conflicting</td><td>L &gt; G</td><td>7.87</td><td>7.07</td><td>0.64</td><td>1.38</td><td>16.228*</td><td>1.962</td><td>0.032</td></tr><tr><td colspan="9">Notes: * Levene&#x27;s F-test is significant, hence, the hypothesis that the variances of the two groups are equal must be rejected. The t-statistic reported here is Welch&#x27;s t, which does not require the assumption of equal variances.</td></tr></table>

Finally, Hypothesis 4 was supported: participants in group Local performed better than those in group Global, lending support to the idea that preserving local schemas enhances communication when there are conflicts in classification structure between schemas. In addition, the variances for the two groups on Type 4 questions show an interesting pattern. The standard deviation for group Local was significantly lower than that of group Global, suggesting that group Local participants performed relatively uniformly on the task, whereas those in group Global tended to do well or very poorly. Examination of the raw results on these questions bears out this interpreta tion. As Figure 1 shows, scores of participants in group Local are consistent with a normal distribution, whereas those in group Global are more consistent with a bimodal distribution. This suggests that participants in group Global either “got it” or didn’t, in the sense of figuring out how, given a global schema diagram, to understand other views when they contain information conflicting with a local view. However, addi tional data on the characteristics of individuals in each of the two modes of the distribution would need to be collected to shed light on the reason for this bimodality.

Finally, the time taken by participants in each group to complete the questionnaire was examined. A comparison of means reveals that, whereas participants in group Local took longer than those in group Global to answer the questionnaire (on average, 15.2 versus 13.9 minutes), this difference is not statistically significant. It is possible there may have been differences by the type of questions that canceled each other out in the overall time measure. For example, participants in group Local may have answered “Look Local” questions more quickly than those in group Global, bu have answered “Look Both” questions more slowly. Given that the questionnaire was administered on paper, it was not possible to measure time at the granularity of question type. However, further insights could be obtained on this issue in the future by administering a computer-based questionnaire and measuring the time required to answer each question.

## Discussion

THIS STUDY PROVIDES SUPPORT FOR THE IDEA that global conceptual schema diagrams inhibit verification of classification structure relative to local (partial) schema diagrams. In addition, the results indicate that global schemas improve communica tion related to issues of combining complementary elements of the classification structures of distinct partial schemas. In contrast, where elements of local schemas are in conflict, preserving local schemas appears to improve understanding of other point of view with respect to the conflict.

The strong support for Hypothesis 1 indicates that people are better able to verify that a partial classification structure, with which they are familiar (through prior exposure), is properly captured when a local schema diagram representing this structure is used, rather than when this structure is embedded in a more complex global schema diagram. This result affirms with empirical evidence the commonly advocated practice of verifying local schemas before performing view integration. This experiment also provides the first empirical evidence we are aware of that building partial conceptual schemas or views should in fact be done at all. In other words, database designers should not build a global conceptual schema without first building and verifying local schemas that directly reflect user views. The approach of bypassing local schemas in favor of a global schema has been recognized as an alternative method of logica database design, but previously criticized only on conceptual grounds [15, 34].

![](/api/attachments/WBDW7NDD/fulltext/images/8cd1d989138a3c2c66900a2bf71617ae6c74934782ab0fb40b2edad2a23555e7.jpg)  
Figure 1. Scores on Type 4 (Look Remote/Local Conflicting) Questions by Group

The failure to refute the null form expressed in Hypothesis 2 is consistent with the lack of a theoretical basis to expect a difference in performance where there is no overlapping structure or potential conflict between two partial classification structures. In that case, it does not seem to matter whether a user examines this information in a local schema diagram corresponding to the unfamiliar structure, or in a global schema diagram. Of particular interest in relation to the general case for view integration, the results do not indicate that global schemas improve or impede the communication of such information.

The results associated with Hypothesis 3 show that, where there is complementary structure, but no conflict between two partial classification structures, a global schema provides a significantly better base for answering questions that require integrating that structure. In essence, participants presented with partial schemas must perform schema integration to answer questions about “global” requirements, and the results show at least that novices cannot do this very effectively. We believe this evidence clearly indicates that global schemas improve communication in relation to integrat ing complementary structure.

The support for Hypothesis 4 indicates that, where there is conflict between the classification structures in two partial schemas, preserving partial schemas enhances the ability (relative to a global schema) of participants to understand these differences in points of view. A global schema may mask these differences and make it more difficult or impossible to properly understand the unfamiliar view. In this case, users may be more susceptible to the cognitive heuristic of anchoring to the familiar (a classification structure with which they have prior experience) under a global schema than under distinct local schemas [36]. In addition, the fact that participants in group Global tended to do very poorly or very well on Type 4 questions warrants further research aimed at trying to understand the reasons for the bimodal distribution.

The results from this study must obviously be considered in light of the limitation imposed by the choices made in the experimental design. We deliberately used an artificial and contrived domain in order to remove any confounding effects due to overall level of domain knowledge that might be common to participants. The rationale for this choice hinges on the argument that, in testing for differences in the form of representation (local versus global schemas), it is only necessary to understand the semantics of the constructs in the EER model. Clearly, the “simulation” of users having a local view (by giving them a narrative describing the view) is not realistic. However, there is no reason to suspect that this would not have similar effects on the performance of users in both the Local and Global groups. In addition, since real users with real views would understand their views much better than the simulation undertaken by participants in this experiment, they might be better able to appreciate the differences between their view and other views when they are in conflict. In short, there is no compelling case that the results obtained would not generalize to real conceptual modeling settings, inasmuch as they deal with the ability to interpret the semantics of conceptual schema diagrams.

An additional limitation of this study is that it used only two local schemas. Although a pairwise approach is generally advocated in schema integration [3], the study does not permit generalization to more complex integration situations (that is, many views).

A further limitation arises from the small size of the experimental problem. In practical applications, schemas (in particular, global schemas) are likely to have many more entity types, attributes, and relationships than the example used in this study. I would be inappropriate to extrapolate the findings of this study to large problems.

Finally, it is possible the length of training could affect the results, in that additional training might reduce the differences between Local and Global groups.

## Conclusions and Future Research

CLASSIFICATION-BASED DATA MODELS such as the ER model and the class diagrams of the UML are important tools in information systems development. In addition to serving as the blueprint for database design and implementation, such diagrams are used for documenting and verifying data requirements. They have also been advo cated as a communication tool that allows users with a particular view to relate thei classification structure to other structures (views) that may exist in the organization, thereby supporting knowledge sharing and management. This research begins to characterize the relative merits of local and global schema diagrams in conceptual data modeling. The experimental results indicate that local schemas better enable the verification of familiar classification structure than does a global schema, confirming the generally advocated rationale for developing local schemas. In addition, local schemas appear to enable a clearer understanding of unfamiliar classification structures when these are in conflict with a familiar structure. The results also demonstrate that, to the extent that partial structures in local schemas are complementary, global schemas more clearly indicate the bigger picture of integrated structure.

Our findings suggest that both local and global schema diagrams can be useful in promoting organizational communication, and both should be preserved and made available to database users after a database is implemented. Global schemas can be useful in enhancing communication about combined complementary classification structure. However, since global schemas do not preserve information about conflict ing structure, local schema diagrams can be used to facilitate communication about conflicting views.

In view of these outcomes, we believe additional research will be valuable in shedding more light on the use of local and global schemas to facilitate information sharing in organizations. First, the relative frequency of “complementary”and “conflicting” classification structure in different views is unknown. A combination of surveys and case studies of data modeling practice will be useful in determining how frequently these issues arise in integrating local schemas. Findings from such studies will have an important impact on the practical use of local and global schemas to support communication between user groups.

In addition, it would be valuable to adapt the study reported here to a field setting. It is conceivable that real users with real views might have a greater tendency to anchor to their own view and exhibit less cognitive flexibility in trying to understand other views when there is a conflict. Moreover, field research would indicate whether the results in this study can be generalized to large models, or whether model size affects the relative advantages and disadvantages of local and global schemas.

In extending this work to the field, it will be possible to use natural assignments of participants to groups based on their actual views of the application domain and resulting classification structures. For example, if a follow-up quasi experiment is carried out in a manufacturing company, local views can be developed for users in each of the company’s manufacturing and marketing departments, and a global view can be developed from these. In this setting, the “prior knowledge” brought to the task by participants will in fact be the knowledge of the domain as expressed in their local schema.

Finally, additional work is needed to understand how individual characteristics or other factors might contribute to the bimodal distribution observed among partici pants in the Global group for Hypothesis 4. Improving our understanding of how such factors influence how people interpret schema diagrams can be useful in devel oping guidelines for tailoring diagrams to the kinds of people who will be reading them.

Systems. The author is grateful to two anonymous reviewers for valuable comments and sug gestions on an earlier version of this paper.

## NOTES

1. View integration techniques generally advocate pairwise integration of schemas (for example [34]).

2. Since this is an initial test of theory, the focus is on preserving internal validity by using a controlled laboratory setting. The section “Conclusions and Future Research” discusses some issues associated with extending this type of experiment in a field setting.

3. A third approach is to choose a domain about which participants have variable knowl edge. In this case, participants may respond based on prior knowledge, thereby potentially introducing additional variability to the data. However, differences in prior knowledge could be controlled by random assignment of participants to groups. Nevertheless, two problem arise. First, a larger sample size would be required relative to the case where participants have uniform knowledge. Second, the available student sample was relatively homogeneous on a range of variables, including demographic variables such as age. Within such a sample, there is unlikely to be a large natural variation in experience with the types of application domain typically used for data modeling studies.

4. Although this may appear to be excessively complex for novices, a pretest of the training material with three individuals with no data modeling experience suggested that the data modeling notation can be learned and understood by novices in a short period of time. This was confirmed in the main study, in which the mean correct score was 74.3 percent.

5. The classification can be more easily understood by noting two aspects of the experimental session. First, participants were told in the training session that an attribute is assigned to only one class (but is inherited by subclasses). Second, participants in the Local group were instructed that if an attribute appeared with the same name in both diagrams, it had the same meaning.

6. Since the main study used an expanded questionnaire, no direct statistical comparison of the pretest with the main study was made.

7. We also tested whether there were any differences between groups on the composite score of incorrect answers to each type of question. No significant differences were found. In addition, the responses to each individual question within a category were examined to deter mine if the overall result for any of the four question types could be accounted for by responses to a small number of questions within that type. In the large majority of cases, responses to individual questions were in the same direction as the overall result for that question type.

## REFERENCES

1. Baldwin, D. Applying multiple views to information systems: A preliminary framework. Data Base, 24, 4 (November 1993), 15–30.

2. Batini, C.; Ceri, S.; and Navathe, S. Conceptual Database Design: An Entity-Relationship Approach. Redwood City, CA: Benjamin/Cummings, 1992.

3. Batini, C.; Lenzerini, M.; and Navathe, S. A comparative analysis of methodologies for database schema integration. ACM Computing Surveys, 18, 4 (December 1986), 323–364.

4. Batra, D. The effect of user view characteristics on designer performance in logical design of relational databases. Journal of Database Management, 8, 2 (Summer 1997), 27–36.

5. Batra, D., and Antony, S. Novice biases in conceptual database design. European Jour nal of Information Systems, 3, 1 (1994), 57–69.

6. Batra, D., and Davis, J. Conceptual data modeling in database design: Similarities and differences between expert and novice designers. International Journal of Man-Machine Stud ies, 37, 1 (1992), 83–101

7. Batra, D., and Kirs, P. The quality of data representations developed by novice designers: An experimental study. Journal of Database Management, 4, 3 (Fall 1993), 17–29.

8. Batra, D.; Hoffer, J.; and Bostrom, R. Comparing representations with relational and EER models. Communications of the ACM, 33, 2 (February 1990), 126–139.

9. Bodart, F.; Patel, A.; Sim, M.; and Weber, R. Should optional properties be used in conceptual modeling? A theory and three empirical tests. Information Systems Research, 12, 4 (December 2001), 384–405.

10. Booch, G. Object-Oriented Design with Applications. Redwood City, CA: Benjamin Cummings, 1991.

11. Chen, P. The entity-relationshipmodel: Toward a unified model of data. ACM Transactions on Database Systems, 1, 1 (March 1976), 9–36.

12. Cliff, N. Analyzing Multivariate Data. San Diego, CA: Harcourt Brace Jovanovich, 1987.

13. Coad, P., and Yourdon, E. Object-Oriented Analysis. Upper Saddle River, NJ: Prentice Hall, 1991.

14. Connolly, T.; Begg, C.; and Strachan, A. Database Systems: A Practical Approach to Design, Implementation, and Management. Reading, MA: Addison-Wesley, 1995.

15. Elmasri, R., and Navathe, S. Fundamentals of Database Systems, 3d ed. Redwood City, CA: Benjamin/Cummings, 2000.

16. Gemino, A., and Wand, Y. Comparing mandatory and optional properties in conceptua data modeling. In V. Mookerjee and P. Bowen (eds.), Proceedings of the Tenth Workshop on Information Technologies and Systems. Atlanta: Association for Information Systems, 2000, pp. 97–102.

17. Harris, R. A Primer of Multivariate Statistics. New York: Academic Press, 1975.

18. Jacobson, I.; Booch, G.; and Rumbaugh, J. The Unified Software Development Process. Reading, MA: Addison-Wesley, 1999.

19. Jarvenpaa, S., and Machesky, J. Data analysis and learning: An experimental study of data modeling tools. International Journal of Man-Machine Studies, 31, 4 (1989), 367–391.

20. Kim, Y., and March, S. Comparing data model formalisms. Communications of the ACM 38, 6 (June 1995), 103–115.

21. Kumar, K., and van Hillegersberg, J. Enterprise resource planning: Introduction. Communications of the ACM, 43, 4 (April 2000), 23–26.

22. Kung, C., and Solvberg, A. Activity modelling and behaviour modelling. In T. Olle, H. Sol, and A. Verrijn-Stuart (eds.), Information Systems Design Methodologies: Improving the Practice. Amsterdam: North-Holland, 1986, pp. 145–171.

23. Lakoff, G. Women, Fire and Dangerous Things: What Categories Reveal About the Mind. Chicago: University of Chicago Press, 1987.

24. Lee, J., and Malone, T. Partially shared views: A scheme for communicating among groups that use different type hierarchies. ACM Transactions on Information Systems, 8, 1 (January 1990), 1–26.

25. Navathe, S.; Elmasri, R.; and Larson, J. Integrating user views in database design. IEEE Computer, 19, 6 (June 1986), 50–62.

26. Parsons, J. An information model based on classification theory. Management Science, 42, 10 (October 1996), 1437–1453.

27. Parsons, J., and Wand, Y. Choosing classes in conceptual modeling. Communications of the ACM, 40, 6 (June 1997), 63–69.

28. Rosch, E. Principles of categorization. In E. Rosch and B. Lloyd (eds.), Cognition and Categorization. Mahwah, NJ: Lawrence Erlbaum, 1978, pp. 27–48.

29. Rumbaugh, J.; Blaha, M.; Premerlani, W.; Eddy, F.; and Lorensen, W. Object-Oriented Modeling and Design. Upper Saddle River, NJ: Prentice Hall, 1991.

30. Singh, N. Unifying heterogeneous information models. Communications of the ACM 41, 5 (May 1998), 37–44.

31. Sinha, A., and Vessey, I. An empirical investigation of entity-based and object-oriented data modeling: A development life cycle approach. In P. De and J. DeGross (eds.), Proceedings of the Twentieth International Conference on Information Systems. Atlanta: Association for Information Systems, 1999, pp. 229–244.

32. Smith, E. Concepts and thoughts. In R. Sternberg and E. Smith (eds.), The Psychology of Human Thought. Cambridge: Cambridge University Press, 1988, pp. 19–49.

33. Smith, E., and Medin, D. Categories and Concepts. Cambridge: Cambridge University Press, 1981.

34. Teorey, T. Database Modeling and Design: The Fundamental Principles, 2d ed. San Francisco: Morgan Kaufmann, 1994.

35. Teorey, T.; Yang, D.; and Fry, J. A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys, 18, 2 (June 1986), 197–222.

36. Tversky. A., and Kahneman, D. Judgment under uncertainty: Heuristics and biases. Sci ence, 185, 4157 (September 1974), 1124–1131.

## Appendix A

## Narratives for Local View

OMEGAS HAVE PROPERTIES A, C, and D. There is a one-to-one correspondence between Omegas and Sigmas (which have properties K and L): each Omega jolatizes with exactly one Sigma, and vice versa. Omegas may additionally antilate up to one Beta (but do not have to antilate any). Betas (which have property E) are antilated in one or more Omegas. Betas may be caduated for up to one Gamma (Gammas have properties A, F, and G). Gammas may caduate many Betas, but do not have to caduate any. Since Gammas and Omegas share the property A, they are treated as specia types of a more general class called Chis. A Chi need not be either a Gamma or an Omega, and cannot be at the same time both a Gamma and an Omega.

## Appendix B

Local Conceptual Schema Diagrams

![](/api/attachments/WBDW7NDD/fulltext/images/9b1992b67b5f645b9c41e0bb852ead234fa78682173502cc6ac0a84fb18dba26.jpg)

(A) “Participant” View

![](/api/attachments/WBDW7NDD/fulltext/images/6396e8aade81e83f3eebc98f57c3e470fc32fa6bddd1a3f3483d951f022cd87e.jpg)

(B) “Remote” View

Appendix C

Global Conceptual Schema Diagram

![](/api/attachments/WBDW7NDD/fulltext/images/422c397cb8896590d12be2f98e88a65f84b813bd8c5c484fbd0f0a7c5e1c6868.jpg)

## Appendix D

## Questionnaire

1. List the properties of Alphas:

2. List the properties of Epsilons:

3. Which entities have a greater number of properties? (circle one) Alphas / Omegas

4. List the properties of Gammas?

5. What are the common properties of Deltas and Epsilons (leave blank if none)?

6. Can an instance of the entity type Delta also be an instance of the entity type Beta?

7. Can an instance of the entity type Delta also be an instance of the entity type Epsilon?

8. Is there a relationship between Gammas and Epsilons?

10. Is there a relationship between some Betas and Omegas? \_\_ If “yes,” what is the name of this relationship?

11. Do Epsilons and Sigmas refer to the same entity type?

12. Name any relationships between Epsilons and Omegas (leave blank if none)?

13. Do Alphas and Omegas refer to the same entity type?

14. Is every Alpha also an Omega?

15. Every Beta must heltify exactly one Gamma. True / False

16. Select the best name to describe those Omegas that must antilate with a Beta?

(a) Omegas; (b) Gammas; (c) Alphas; (d) Deltas; (e) Chis; (f) Epsilons

17. List the properties of Sigmas.

18. Some Gammas may caduate some Sigmas. True / False

19. Some Omegas may antilate some Epsilons. True / False

20. Some Gammas may jolatize some Epsilons. True / False

21. List the properties of Omegas.

22. Every Alpha must antilate exactly one Beta. True / False

23. Every Chi must be either an Omega or a Gamma. True / False

24. A Beta can be antilated by no more than one Alpha. True / False

25. All Epsilons are also Betas. True / False

26. H is a property of Gammas. True / False

27. Some Chis may antilate some Betas. True / False

28. Every Beta must be either a Delta or an Epsilon. True / False

29. Sigmas are a special type of Chis. True / False

30. Some Betas have the properties K and L.

The questionnaire administered to participants included an additional five questions about perceived difficulty of answering questions about the four major kinds of EER constructs and overall difficulty.

<table><tr><td colspan="2">Appendix E</td></tr><tr><td colspan="2">Classification of Questions</td></tr><tr><td>Type</td><td>Questions</td></tr><tr><td>1. Look local</td><td>10, 21, 23, 27, 29</td></tr><tr><td>2. Look remote</td><td>2, 5, 6, 7, 8, 15, 24, 30</td></tr><tr><td>3. Look both</td><td>3, 4, 9, 11, 12, 13, 14, 17, 18, 19, 20</td></tr><tr><td>4. Look remote/local conflicting</td><td>1, 16, 22, 25, 26, 28</td></tr></table>
