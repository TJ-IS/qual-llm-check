---
otero_id: 18932
otero_key: "BMN28XJM"
title: "A framework for studying human error behavior in conceptual database modeling"
authors: "Dinesh Batra"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90035-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A framework for studying human error behavior in conceptual database modeling

Dinesh Batra

Florida International University, Miami, FL, USA

A framework is developed to explain human error behavior in modeling conceptual databases. The framework is based on the notion of directness distance or 'gulf' suggested in recent literature. It specifies four aspects of 'gulf' in the context of conceptual database design – syntax, mapping, rules, and consistency. Based on the model, six types of errors are suggested – syntactic, abstraction, simplification, overload, convergence, and divergence. These are then matched to errors found in four empirical studies on database representation. Four types of errors – convergence, abstraction, simplification and overload – were typically found in these studies. The paper provides design guidelines to prevent these errors.

Keywords: Human error; Conceptual database; Logical database; Designer training; End user training

![](/api/attachments/BMN28XJM/fulltext/images/c9504d25dd7fcd472ca7ae44b75e2571c18a382fe8d24f6b1414a84fcdfb0de8.jpg)

Dinesh Batra is an Assistant Professor in the Department of Decision Sciences and Information Systems at Florida International University in Miami. He holds a Ph.D. from Indiana University. He has published papers in Communications of the ACM, International Journal of Man-Machine Studies, and International Conference on Information Systems. His research interests include human factors in database design, conceptual and logical database design methodologies, and statistical database security.

Correspondence to: D. Batra, Decision Science and Information Systems, College of Business Administration, Florida International University, University Park, Miami, FL 33199, USA.

## 1. Introduction

Human computer interaction studies can be used to determine the usability of information systems $[8,30]$ . In the context of database management, human factor studies have focused on the usability of data models and query languages $[6]$ . While novice designers have been the intended target of many usability studies, with the advent and proliferation of end user computing $[1,9,25]$ , the implications of these studies is applicable to a wider population. The broad goal of these studies has been to consider user performance in terms of achieving higher quality solutions to database design or query problems. However, these studies have not explicitly addressed human error behavior in conceptual data modeling. There is no framework to explain why designers, especially novices, make errors and what might be done to prevent them. In fact, the way in which humans detect their own errors has been a relatively neglected issue in the area of human–computer interaction $[39]$ .

Conceptual data modeling is an important activity in database design. A conceptual (or logical) representation is free of database management system (DBMS) specific details $[16,17]$ . Some researchers make a distinction between logical models, which are implementable, and conceptual models, which are not implementable and need to be translated to a logical representation before using a DBMS. Since models like “entity relationship” $[11]$ that are considered conceptual are now implementable, this paper does not make the distinction between conceptual and logical models.

This paper develops a framework that can be used to explain why end users and nonexpert designers commit errors in developing conceptual representations. The model helps predict types of errors, which are then discussed using four recent usability studies. The implication of the paper includes design guidelines to minimize human errors in developing conceptual database representations.

## 2. Research model

Human factor studies of data management environments have addressed usability issues of data models [e.g., 10,18,21,22,28,38,41] and database query languages [e.g., 20 and 36 for detailed surveys]. These studies have generally considered the degree of correctness of a designer's or user's solution as the dependent variable. However, they do not explicitly postulate reasons for the cause of these errors. Further, although they have provided useful findings, most of them have not been based on theoretical models. Keen [24] suggests the need to identify reference disciplines, conduct studies with a theoretical base, and build a cumulative tradition in the MIS area.

This paper proposes a framework to examine usability of database representation. The framework is adapted from ideas, frameworks, and models suggested in the literature on human-computer interaction and human reliability. The primary source is Hutchins, Hollan and Norman's [19] concept of 'gulf' or directness distance between a user's goals and the human-computer interface. They specified two components of this distance – semantic and articulatory. Semantic distance separates what the user wants to say from the meaning of an expression in the interface language. Articulatory distance separates the meaning of an expression from its physical form. If the gulf between user's goals and the interface is large, the user would require considerable effort to accomplish the goals.

The same concept can be applied in the context of database modeling. There is a gulf between reality and representation with two components, that is, articulatory and semantic distance. However, this classification is too broad to be readily used. It is important, therefore, to determine finer aspects of this distance.

This paper proposes four aspects of gulf (Figure 1): syntax corresponds to the articulatory distance, and mapping, rules and consistency are features of the semantic distance. The usability of a data model can be determined by considering how it addresses these aspects of representation.

![](/api/attachments/BMN28XJM/fulltext/images/260f9057d84322420d3bc28d243119fcd2c94c6703e1409b6e64b2817e50c3fa.jpg)  
DATABASE REPRESENTATION  
Fig. 1. Framework of database representation.

Syntax is a basic aspect of any language and representation and includes its form and the permissible structure. In the context of human-computer interaction, it is an important element of Shneiderman's [40] syntactic/semantic model of programmer behavior. The two main forms of representations are: tabular (e.g., relational [13]) and graphical (e.g., entity relationship). For research purposes, the form is the important feature of syntax, since the structure itself is quite simple. Further, the structure can be checked by a design aid. An intelligent system can even suggest corrections. For example, if a designer does not indicate a primary key of a relation, a design aid can prompt corrective action.

The mapping process is an important semantic aspect of modeling. A model or representation is an abstraction of the real world. It focuses on those aspects of the real world that are of interest and ignores the others. Further, by using symbols, these aspects are mapped into a representation that depicts a certain state of the world.

The relationship between reality and representation can be depicted as a mapping that transforms a world state (or application) into a knowledge-state (or representation) [7]. One can then answer questions about the world state by querying the representation. Inherent in this mapping process is the notion of abstraction. Similarly, a database representation may have an entity class (or entity) 'employee': this is an abstraction of many real world instances, e.g., 'Peter', 'Jane', etc. This entity class can be represented by a rectangle named 'employee'. There may be a relationship 'works' between 'employee' and 'project': an abstraction of relationships between their entity instances.

The mapping from a given state of the world to its representation is presumably governed by semantic rules. According to Tsichritzis and Lochovsky [45], a data model defines the rules according to which data are structured and the general nature of the operations that are allowed on the data. A rule is of the form IF $\langle pattern\rangle$ THEN $\langle action\rangle$ , that is, the left side that determines the applicability of rule, and the right side determines the action to be performed when the rule is applied [37]. The left side of the rule is determined by the semantics of the application.

For example, a relational representation of an application is expected to satisfy the normalization rules $[14]$ , which are based on the notions of functional and multivalued dependency. If a many-to-many relationship is to be represented using the relational model, it must be shown by creating a separate relation (sometimes called a link relation). Semantic data models have their own rules. For example, in the ER modeling scheme, if an object has descriptive information, it is treated as an entity $[17,44]$ . It may be remarked that in most cases, there is no ‘standard’ representation scheme. For example, there are some variations in the use of the entity relationship model. However, most rules are invariant between versions.

Finally, consistency is an offshoot of the mapping from the real world to the representation. Merely mapping the real world to a representation does not ensure understandability. The representation scheme should have some degree of consistency in modeling the real world, that is, similar features of real world should have similar representation. Consistency is a desirable though not mandatory aspect of a representation.

Many researchers have emphasized the need for consistency of operators for a human-computer interface. Norman [32] suggests that systems should be consistent in order to minimize memory problems in retrieving operations and should exhibit similarity of response sequences. Lewis and Norman [26] recommend that commands that share a common description of purpose and action should have similar structures. Similarly, in the context of database modeling, similar facets should map to similar representations. For example, in the context of data modeling, all types of binary relationships should have similar representation.

Thus, a data model would rate high in usability if it satisfies the following four criteria. First, the syntax should be simple and have the appropriate form for the context. Second, the mapping mechanism of the representation should provide a reasonable degree of resemblance to the real world. Third, the representation should require a minimum number of rules. Finally, there should be some degree of consistency in the mapping from reality to representation.

## 3. Types of errors

A number of papers have contributed to the literature on error behavior in human-computer interaction. Norman [31] has suggested error categories based on the activation-trigger schema (ATS) model. The ATS model assumes that action sequences are controlled by knowledge structures called schemas. A schema is an organized unit of knowledge that specifies some structured response sequence. An action sequence starts with the formation of an intention, which activates one or more schemas that control the various aspects of the action. An error in the action is called a mistake while an error in carrying out the intention is called a slip.

Based on his model, Norman suggests four types of slips, which, in the context of human computer interaction, are preventable: mode, description, capture, and activation errors. However, his work focuses on the human-computer interface and is not totally generalizable to database representations. Further, it restricts itself to slips and does not address mistakes, which are, perhaps, the more important errors.

Rasmussen [33] identified three different types of error behavior. Skill-based behavior consists of well organized and highly automated actions. Rule-based behavior is one or more actions performed depending on stored rules. Knowledge-based behavior is the result of an attempt to cope with unfamiliar situations where previously used rules are not sufficient.

Based on Rasmussen's error types and Norman's taxonomy, Reason [35] has proposed a classification of errors involving the following categories of errors: slips, rule-based mistakes, and knowledge-based mistakes. Rule-based mistakes occur when a problem solver decides that the

![](/api/attachments/BMN28XJM/fulltext/images/a3aede21cf7c2df9aac32cec2c4909eff6866f44a1dfe41c06b56fbef60d9087.jpg)  
DATABASE REPRESENTATION

Fig. 2. Typology of errors.

situational component of a stored rule (IF $\langle$ situation $\rangle$ THEN $\langle$ action $\rangle$ ) is appropriate to the system when it is not. Knowledge-based mistakes occur when people cannot successfully use their repertoire of rules to solve an unfamiliar problem. While Reason's error typology is useful, it is too general for a given domain.

Here, the framework is used to develop a detailed typology of errors in the context of database representations. Six types of errors can be anticipated: syntactic, abstraction, simplification, overload, convergence and divergence (see Figure 2). While the list may not be exhaustive, it does show why errors may occur in data modeling. A brief explanation of each type follows.

Syntactic: As the name suggests, this pertains to an error in syntax. The syntactic/semantic framework was used by Leitheiser [27] to study query languages. An example of a syntactic error in a relational representation could be: Not specifying the primary key of a relation. Since the syntax of a database representation is fairly straightforward, this paper focuses on the semantic issues.

Abstraction: This is an error caused by inappropriate mapping from reality to representation. Change of level of abstraction involves a shift in concepts and structure [34]. The mapping from the real world state to a representation should ensure a degree of reality. If the representation is distorted during the abstraction process, the designer is likely to commit errors: these are called abstraction errors. A unary relationship as modeled by the entity relationship (ER) model provides an apt example of the possibility of this error. If a binary fact in the real world level maps to a unary fact at the representation level, the disparity can cause confusion and errors.

Simplification: This error type is caused by inappropriate use of rules. If a situation arises where a piece of the application is complex, requiring too many rules for representation, a designer may divide it into simpler pieces. However, the situation may not be divisible; that is, any attempt to break it up would lead to distorted semantics, and hence the representation would be erroneous. Reason [35] says that the limitations of the attentional resource leads to focusing (overattention) upon particular aspects. Further, human beings are active pattern matchers. Consequently, in complex situations, a portion of the situation may result in a pattern match which may trigger stored rules. The result could be simpler and drastically different from the correct one.

Another cause for this type of error is the availability heuristic, which can be summarized as: “Things that come readily to mind are likely to be more frequent, more probable, more important, more useful, and better understood than less readily available items” [23]. Thus, there is a tendency to force, at times erroneously, familiar structures into situations, which may require different and, perhaps, more complex structures. An example in the database context is the modeling of a ternary relationships as two or more of the easily understood binary relationships.

Overload: An overload error is similar to a simplification error, since both involve a complex situation and are caused by inappropriate use of rules. In this case, however, the designer does recognize the situation as a whole and does not use a simplifying approach. They are therefore less severe than simplification errors. The difference is similar to that between knowledge-based and rule-based mistakes. Simplification errors are likely to be knowledge-based, while overload errors are generally rule-based.

In the case of overload error, there are many elements of a situation, and the process of analysis and/or integration places a heavy burden on a person's memory. Further, the application description may not provide information about all such elements – some may have to be inferred or obtained by eliciting more from the user; but failure to consider all elements may lead to incomplete or erroneous representations.

The evidence indicates that working memory operates on a ‘first in first out’ basis. Thus, it is easier to recall the premises of a syllogism in the order in which they were presented than in the opposite order. When the load is excessive, false inference will be made. An example of this during database representation is: incorrect modeling of the connectivity of a ternary relationship. The designer may use the available facts and ignore any information that needs to be reasoned or elicited. A later example illustrates this.

Table 1
General parameters of the study.

<table><tr><td></td><td>Batra et al. 1990</td><td>Batra &amp; Kirs 1990</td><td>Batra &amp; Sein 1991</td><td>Batra &amp; Davis 1991</td></tr><tr><td>Objective of Study</td><td>Relational versus EER Model</td><td>LRDM versus DA Approach</td><td>Improving Conceptual Data Modeling Perf. using Feedback</td><td>Expert versus nonexpert Designers</td></tr><tr><td>Subject Experience</td><td>Novice</td><td>Novice</td><td>Intermediate</td><td>Experts: Advanced Non-Exp: Intermediates</td></tr><tr><td>Method</td><td>Lab Expt: Between subjects</td><td>Lab Expt: Between Subjects</td><td>Lab Expt: Within subjects</td><td>Lab Expt: Protocol Analysis</td></tr><tr><td>Number of Subjects</td><td>42</td><td>72</td><td>27</td><td>9</td></tr></table>

Convergence: This is one of the errors caused by the lack of consistency between the real world and the representation. If similar situations in the real world lead to dissimilar representations, the resulting confusion may cause errors; e.g., the relational representation of a one-to-many relationship is represented quite differently from a many-to-many relationship. This problem does not exist in the entity relationship model; consequently, there is less likelihood of a convergence error.

Table 2  
Error types in empirical studies

<table><tr><td></td><td>Batra et al. 1990Study 1</td><td>Batra &amp; Kirs 1990Study 2</td><td>Batra &amp; Scin 1991Study 3</td><td>Batra &amp; Davis 1991Study 4</td></tr><tr><td>Models Used</td><td>Relational &amp; ER</td><td>Relational,ER &amp; DA</td><td>Relational</td><td>Generally Relational</td></tr><tr><td>Binary Relationship</td><td>Convergence in Relational</td><td>Convergence in Relational</td><td>Not found</td><td>Not found</td></tr><tr><td rowspan="2">Unary Relationship</td><td>Abstraction</td><td>Not considered</td><td>Abstraction (Rare however)</td><td>Abstraction (Rare: by nonexperts)</td></tr><tr><td>Simplification in ER</td><td>Not considered</td><td>Simplification</td><td>Not Applicable</td></tr><tr><td rowspan="4">Ternary Relationship</td><td>Convergence</td><td>Not Considered</td><td>Convergence (Rare however)</td><td>Not found</td></tr><tr><td>Simplification in ER &amp; Relational;Higher incidence in Relational</td><td>Simplification in ER &amp; Relational;Higher incidence in Relational</td><td>Simplification (Rare however)</td><td>Simplification (Rare; by non-experts)</td></tr><tr><td>Overload in ER &amp; Relational;Higher incidence in Relational</td><td>Overload in ER &amp; Relational;Higher incidence in Relational</td><td>Overload</td><td>Not found</td></tr><tr><td>Not found</td><td>Divergence</td><td>Not found</td><td>Not found</td></tr><tr><td>Entity</td><td>None</td><td>None</td><td>None</td><td>None</td></tr><tr><td>Attribute</td><td>None</td><td>None</td><td>None</td><td>None</td></tr></table>

Divergence: Another error caused by lack of consistency occurs when dissimilar situations have similar representation. This may happen in the data aggregation approach [42], where entities and the associations between them are represented in the same way as objects. For example, an entity INSTRUCTOR and its relationship TEACH with a course have the same notation (usually a rectangle). Such similarity of dissimilar concepts may lead to overlap of rules and increase the possibility of error.

## 4. Error types found in four empirical studies

The six error types derived from the framework were matched with the errors found in four recent empirical studies. While the objectives of the studies were different, all used similar tasks and grading scheme and are therefore comparable. The experience level of the subjects, however, was different. The subjects in [5] were more advanced than novices (they are called intermediates), while the ones in [2] and [3] had very limited training and were surrogates of typical end users and novice designers. Both experts and intermediates were used in [4]. The general parameters of the studies are compared in Table 1. A short description follows.

Study 1 compared the relational model with the extended entity relationship (EER) model. Study 2 compared the logical relational design methodology (LRDM) [44] with the data aggregation approach. The LRDM approach involves modeling the requirements in the ER form and then translating it to the relational form. The data aggregation approach requires modeling the requirements in a data aggregation diagram [42] and then translating it to relational form. Study 3 conducted a laboratory experiment using the 'hidden operator' method to study the effect of intelligent feedback on user performance in a conceptual modeling task. Study 4 compared the modeling processes of experts and novices engaged in database design. They analyzed the protocols of experts and novices and developed a process model of data modeling.

The errors uncovered in these studies are discussed for one or more of the following set of 'facets': binary relationship, unary relationship, ternary relationship, entity, and attribute (see Table 2). They provide the semantics found in most databases. This paper makes minimal reference to the data aggregation approach.

## 4.1. Binary relationship

A binary relationship is an association between two entities. A review of text and case books [e.g., 29] indicates that it is the most common of all. This is probably because many semantics in everyday speech and common applications are actually binary, even though they appear as ternary or higher degree. Research indicates that subjects are generally successful in recognizing binary relationships in natural language facts. However, certain representations lead to better solutions.

Modeling a binary relationship using the ER model does not present any apparent difficulty. However, when the relational model is used, an obvious problem is the inconsistency of its representation - similar semantics may differ widely in their representations. Consider the following one-to-many relationship depicting the semantics that an employee belongs to only one department while the department may have many employees:

EMPLOYEE(EMP#, <employee attributes>, DEPT#)

DEPT(DEPT#, <department attributes>)

If an employee can belong to many departments, the relationship changes to many-to-many, and a representation change is needed:

EMPLOYEE(EMP#, <employee attributes>)
DEPT(DEPT#, <department attributes>)
WORKS(EMP#, DEPT#)

A new relation had to be created. Thus, one can expect convergence errors in modeling the connectivity of a binary relationship using the relational model. The ER model does not suffer from the same problem.

These expectations were partially confirmed from the studies. Subjects using the relational model in Studies 1 and 2 committed far more errors in modeling the connectivity of the binary relationships. In comparison, fewer errors were observed in the ER solutions. However, in the other studies, which used more advanced subjects, there were no serious problems for either data model. Thus, convergence error showed up only for novice subjects.

![](/api/attachments/BMN28XJM/fulltext/images/d4db4744f337e33f3b420a68c85b85390b8221505ccd60f968ddd8e2e0719844.jpg)

![](/api/attachments/BMN28XJM/fulltext/images/dbecaeee4bcd83fcb626b5832f72b7ef24ef216aa07c3353ee2a3de550f8b1ed.jpg)  
Fig. 3.

Unary Relationships: A unary relationship is an association between instances of the same entity type. Consider the example adapted from [44]: one may be interested in capturing the MARRIAGE relationship between two different instances of the same entity EMPLOYEE, that is, pairs of employees who are married. Note that the application demands that the relationship be captured only if an employee is married to another, but not if the employee is married to any non employee (which has a different representation).

The relational model exhibits the convergence problem as in the binary relationship. Further, both relational and ER models suffer from a more serious problem, as illustrated using the ER model. Figure 3a shows a unary relationship in the ER form. If we consider the relationship at the instance level, it appears as a binary relationship (Figure 3b). Thus, mapping from the instance level to the schema level requires a change from a binary to a unary representation. Such mapping problem could lead to abstraction errors.

Three of the four studies revealed that subjects committed abstraction errors in modeling unary relationships. (Study 2 did not grade unary relationships). Many subjects actually showed the unary relationship as binary (Figure 3c), which was incorrect since the relationship is between instances of the same entity. In fact, the unary concept seemed troublesome to the subjects in all studies. Many subjects did not even attempt the relationship. Only the experts in Study 4 showed a firm grasp of its representation.

Another error that was found frequently was the modeling of a unary relationship by an easier approach; that is, by using a descriptor (Figure 3d). This seems like a simplification error. In this figure, the semantics conveyed is that “an employee is married to another person” instead of “an employee is married to another employee”.

Ternary Relationship: A ternary relationship is an association between three entities. However, the involvement of three entities is a necessary but not a sufficient condition. In other words, every association between three entities is not ternary. For a relationship to be ternary, the association between the three entities must be considered as one unit and they cannot be losslessly and nonadditively decomposed into binary relationships.

Consider the following sentence which seems ternary: “Order number shows that John sold the car to Mary”. There are three entities – ORDER, SALESPERSON, and CUSTOMER. Is the relationship SOLD ternary? Since ORDER can uniquely determine SALESPERSON as well as CUSTOMER, the relationship SOLD can be losslessly decomposed into two binary relationships (ORDER-SALES PERSON and ORDER-CUSTOMER). In other words, the relationship is not ternary.

The confusion between binary and ternary can arise even when no entity among a group of three can determine another. As an example, consider three entities, say, INSTRUCTOR, BOOK and COURSE [adapted from 14). If the assignment of BOOK to a COURSE depends on the IN-STRUCTOR teaching the course, there is one ternary relationship (see Figure 4a). If the assignment of COURSE to BOOK is independent from the assignment of COURSE to INSTRUCTOR, that is, all instructors use the same books for a given course, there are two binary relationships – between COURSE and INSTRUCTOR, and COURSE and BOOK (see Figure 4b). It is obvious that the ternary concept is difficult. One would expect, therefore, that nonexpert designers would attempt to simplify a ternary situation by substituting it by binary facts. This may result in a simplification error.

![](/api/attachments/BMN28XJM/fulltext/images/77f2e73d1c0b00d0f999a0ef05a9e5bbbf3201ecec390330eeab6d18c5ce6048.jpg)  
Fig. 4.

This error was quite apparent in Studies 1 and 2, but was rarely found in the other two. In other words, the error was not committed by the more advanced subjects. As subjects gained more experience, they developed the ability to differentiate the situations.

Another error that was expected in the case of ternary relationships was overload. Consider a ternary relationship between the entities ANIMAL, MEDICATION and DOCTOR. Assume that the connectivity of the relationship is one-many-many, 'one' on the DOCTOR side, and 'many' on the others. The one-many-many connectivity suggests the following:

Given one instance each of ANIMAL and MEDICATION, there is only one instance of DOCTOR associated;

Given one instance each of ANIMAL and DOCTOR, there are many instances of MEDI-CATION associated;

Given one instance each of MEDICATION and DOCTOR, there are many instances of ANIMAL associated.

If any of the facts are ignored, the resulting representation may be faulty. The designer may consider the available facts only and draw hasty conclusions about the connectivity. Further, it is interesting that an ANIMAL may be associated with many instances of DOCTOR, and a MEDICATION may be associated with many instances of DOCTOR, yet a combination of ANIMAL and MEDICATION is associated with only one instance of DOCTOR. The situation gets even more complicated if it is a one-one-many relationship although it may be admitted that such a relationship is quite infrequent.

This discussion illustrates the complexity of modeling the connectivity of a ternary relationship. There are too many rules to be systematically followed. Failure to follow all could lead to overload errors. Except for Study 4, which ostensibly had the most advanced subjects, all other studies exhibited overload error. The problem was more acute in the case of relational representation, probably because the convergence problem interacted with the overload error.

Finally, divergence errors were noted when the data aggregation (DA) model was used in Study 2. The DA model has the same representation for an entity and an association (or relationship) between entities. However, the association is shown as an aggregate object of the entities (called objects). It was found that this notation was confusing to the subjects, especially in the case of ternary relationships. Instead of creating an aggregate object for the association, the subjects frequently depicted one as the aggregate of the other. For example, instead of showing a separate aggregate object for the relationship between EMPLOYEE, PROJECT and CITY, the subjects often depicted one object as the aggregate of others. For example, there were cases showing PROJECT as the aggregate of CITY and EMPLOYEE, some built a hierarchy showing CITY as an aggregate of EMPLOYEE, and PROJECT as aggregate of CITY. Thus, the lack of a separate representation for relationship resulted in a number of divergence errors.

Entity and attribute: Subjects were usually successful in modeling entities and attributes.

In summary, abstraction errors were found in modeling unary relationships; simplification, overload, and divergence in ternary relationships; and convergence in modeling binary relationships. The analysis shows that the modeling of different facets requires different cognitive thinking, and leads to different types of errors. The following section presents some design guidelines.

## 5. Discussion and implications

Since both relational and ER data models are quite popular, the error types found when these data models were used are quite important. Four types of errors – convergence, abstraction, simplification, and overload – were found when subjects used these data models. The divergence error, which was found only in data aggregation (DA) solutions, does not have practical implications since the DA modeling approach has not been widely adopted in practice. With the advent of object oriented approaches, the study of the aggregation concept and its usability would assume more importance.

Convergence: These errors were noted only in the relational solutions developed by novices. Since binary relationships are the most common types of relationships, this error is by far the most serious. One approach would be to use the ER data model instead of relational. However, since ER based DBMS are not commercially popular, the ER representations must be translated to relations to allow implementation. Thus, design aids should be used to convert ER diagrams to relations. However, the extent to which subjects would understand representations translated by a third party, is a research issue.

Abstraction: This error is associated with unary relationships. Apparently, even intermediates have problems with this concept. It is evident, therefore, that the unary concept is inherently difficult. The only strategy to avoid such errors is appropriate training. Training exercises should test the mapping process from the instance to the schema level and vice versa by using examples employing the notion of unary relationship.

Simplification: A simplification error is usually a knowledge based error that arises because a situation has been considered to be made of simpler pieces than it should be. Comparison of the studies suggests that the problem does go away as users acquire more experience. Thus, after users have learnt to design simple databases, they should be trained to diagnose complex situations. Specifically, they should be able to recognize a situation where the only representation is ternary and not as two binary facts.

Overload: An overload error occurs when too many pieces must be considered together and some may be overlooked. Even intermediates commit overload errors. Many subjects who correctly diagnosed a situation as ternary were unable to specify the connectivity of the relationship correctly. The incidence of this error could be lowered by using a feedback mechanism to force the subject to consider all pieces of the situation. Training, too, would help users avoid this error.

## 6. Conclusions

This paper developed a framework to study human error behavior in the context of database design. From the model, six error types were derived, and four of these - convergence, abstraction, simplification, and overload - were found especially pertinent.

Based on the suggestions provided in this paper, knowledge based tools can incorporate mechanisms to prevent commonly found errors. Convergence errors can be prevented by developing ER model based tools, which can model an application as an ER diagram, and translate it into relational, network, or hierarchical representation. Abstraction and simplification errors can be prevented by including tutorials, which train designers and point out common misconceptions. A knowledge based system can prevent overload errors by forcing a systematic checking procedure in an overloaded situation.

Conversely, knowledge based tools currently available [e.g., 12,15,43,46] can be evaluated based on the proposed typology. Finally, the paper has strong training implications. Training strategies can be devised and empirically tested for effectiveness in reducing occurrence of errors.

## References

[1] M. Alavi and I.R. Weiss, “Managing the Risks Associated with End-User Computing,” Journal of MIS, Vol. 2, No. 3, Winter 1985-86, 1 pp. 5–20.

[2] D. Batra, J.A. Hoffer and R.P. Bostrom, “Comparing Representations Developed Using Relational and EER Models,” Communications of the ACM, (February 1990), pp. 126–139.

[3] D. Batra and P. Kirs, "A Comparison of the Data Aggregation Approach with the Logical Relational Design Methodology," Eleventh International Conference on Information Systems, (December 16–19, 1990), pp. 111–123.

[4] D. Batra and J.G. Davis “Conceptual Data Modeling in Database Design: Similarities and Differences Between Expert and Novice Designers,” International Journal of Man Machine Studies, (1992), 37, pp. 82–101.

[5] D. Batra and M.K. Sein “Improving Conceptual Database Design Through Feedback,” Florida International University Working Paper No. 92–11.

[6] D. Batra and A. Srinivasan “A Review and Analysis of the Usability of Data Management Environments,” International Journal of Man-Machine Studies, (1992), 36, pp. 395–417.

[7] D.G. Bobrow “Dimensions of Representation,” in Representation and Understanding by D.G. Bobrow and A. Collins, New York: Academic Press, 1975.

[8] C.L. Borgman “Psychological Research in Human-Computer Interaction,” Human Computer Interaction, pp. 33–64, (1984).

[9] J.C. Brancheau and J.C. Wetherbe, "Key Issues in Information Systems Development," MIS Quarterly, (11:1), March 1987, pp. 23–45.

[10] M. Brosey and B. Shneiderman, “Two Experimental Comparisons of Relational and Hierarchical Database Models,” International Journal of Man-Machine Studies, (1978), 10, pp. 625–637.

[11] P.P. Chen, “The Entity-Relationship Model - Toward a Unified View of Data,” ACM Transactions on Database Systems, Vol 1, No 1, (March 1976), pp. 9–36.

[12] J. Choobineh, B.R. Konsynski, M.V. Mannino and J.F. Nunamaker, “An Expert System based on Forms,” IEEE Transactions on Software Engineering, Vol. 14, No. 2, February 1988.

[13] E.F. Codd, “A Relational Model of Data for Large Shared banks,” Communications of the ACM, 13, (1970), pp. 377–387.

[14] C.J. Date, An Introduction to Database Systems, Vol. 1, Reading, MA: 1990.

[15] A. Dogac, B. Yuruten, and S. Spaccapietra, “A Generalized Expert System for Database Design,” IEEE Trans-

actions on Software Engineering, Vol. 15, No. 4, April 1989, pp. 479–491.

[16] G.C. Everest, and E.H. Sibley, “A Critique of the GUIDESHARE Data Base Management Systems Requirements,” Proceedings of the 1971 ACM-SIGFIDET Annual Workshop, “Data Description, Access and Control, San Diego, California, 1971, November 11–12, edited by E.F. Codd and A.L. Dean, New York: ACM, 1971, pages 92–112.

[17] J.P. Fry and E.H. Sibley, “Evolution of Data Base Management Systems,” ACM Computing Surveys, (8:1) 1976 March, pages 7–42.

[18] J.A. Hoffer, “An Empirical Investigation into Individual Differences in Database Models,” Proceedings of the Third International Conference on Information Systems, (December 1982), pp. 153–168.

[19] E.L. Hutchins, J.D. Hollan and D.A. Norman, “Direct manipulation Interfaces,” Human Computer Interaction, Volume 1, (1985), pp. 311–338.

[20] M. Jarke and Y. Vassiliou, “A Framework for Choosing a Database Query Language,” Computing Surveys, Vol 17, No 3, (Sep 1985), pp. 313–340.

[21] S.L. Jarvenpaa and J.J. Machesky, “Data Analysis and Learning: an Experimental study of data modeling tools,” International Journal of Man-Machine Studies, (1989), 31, pp. 367–391.

[22] S. Juhn and J.D. Naumann, “The Effectiveness of Data Representation Characteristics on User Validation,” in Proceedings of the Sixth International Conference on Information Systems, Indianapolis, (1985), pp. 212–226.

[23] D. Kahneman, P. Slovic and A. Tversky, Judgment Under Uncertainty: Heuristics and Biases, Cambridge: Cambridge University Press, 1982.

[24] P.G. Keen, “MIS Research: Reference Disciplines and a Cumulative Tradition,” Proceedings of the 1st International Conference on Information Systems, Philadelphia, 1980, pp. 9–18.

[25] R.L. Leitheiser and J.C. Wetherbe, “Service Support Levels: An Organized Approach to End-User computing,” MIS Quarterly, Vol. 10, No. 2, June 1986, pp. 313–325.

[26] C. Lewis and D.A. Norman “Designing for Error,” in User Centered System Design Edited by D.A. Norman and S.W. Draper, Hillsdale, NJ: Lawrence Erlbaum Associates, 1986.

[27] R. Leitheiser, “An Examination of the Effects of Alternative Schema Descriptions on the Understanding of Database Structure and the Use of a Query Language,” Ph.D. Thesis, University of Minnesota, 1988.

[28] F.H. Lochovsky and D.C. Tsichritzis, “User Performance considerations in DBMS selection,” in Proceedings of ACM SIGMOD, (1977), pp. 128–134.

[29] F.R. McFadden, J.A. Hoffer and A. Srinivasan, Casebook for Database Management, Menlo Park, CA: Benjamin/Cummings, 1990.

[30] A. Newell and S.K. Card, “The prospects for Psychological Science in Human-Computer Interaction,” Human Computer Interaction, Vol. 1, 1985, pp. 209–242.

[31] D.A. Norman, “Categorization of Action Slips,” Psychological Review, Volume 88, Number 1, (January 1981), pp. 1–15.

[32] D.A. Norman, “Design Rules Based on Analyses of Human Error,” Communications of the ACM, (April 1983), Vol 26, Number 4, pp. 254–258.

[33] J. Rasmussen, “Skills, Rules, and Knowledge; Signals, Signs and Symbols, and other Distinctions in Human Performance Models,” IEEE Transactions on Systems, Man, and Cybernetics, 3, (1983), pp. 257–266.

[34] J. Rasmussen, “Cognitive Control and Human Error Mechanisms,” in New Technology and Human Error by Rasmussen, J., Duncan, K., and Leplat, J., Eds., London: John Wiley, (1987), pp. 53–61.

[35] J.T. Reason, “Generic Error-Modeling System (GEMS): a Cognitive Framework for Locating Common Human Error Form,” in New Technology and Human Error by J. Rasmussen, K. Duncan, and J. Leplat, Eds., London: John Wiley, (1987), pp. 63–83.

[36] P. Reisner, "Human Factor Studies of Database Query Languages," Computing Surveys, vol 13, No. 1, (March 1981), pp. 13–31.

[38] D. Ridjanovic, “Comparing Quality of Data Representations Produced by Nonexperts using Logical Data Structure and Relational Data Models,” Unpublished PhD Dissertation, University of Minnesota, (1986).

[37] E. Rich, Artificial Intelligence, McGraw-Hill, 1983.

[39] A. Rizzo, S. Bagnara and M. Visciola. "Human Error

Detection Processes," International Journal of Man-Machine Studies, Vol. 27, 1987, pp. 555–570.

[40] B. Shneiderman, Software Psychology, Cambridge: Winthrop Publishers, (1980).

[41] P. Shoval, and M. Evcn-Chaime, “Database Schema Design: An Experimental Comparison Between Normalization and Information Analysis,” Database, (Spring 1987), 18(3), pp. 30–39.

[42] J.M. Smith and D.C.P. Smith, “Database Abstractions: Aggregation,” Communications of the ACM, 20(6), (June 1977), pp. 405–413.

[43] V.C. Storey and R.C. Goldstein, “A Methodology for Creating User Views in Database Design,” ACM Transactions on Database Systems, (September 1988), pp. 305–338.

[44] T.J. Teorey, D. Yang and J.F. Fry, “A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model,” Computing Surveys, Vol. 18, No. 2, (June 1986), pp. 197–222.

[45] D.C. Tsichritzis and F.H. Lochovsky, Data Models, Englewood Cliffs: Prentice-Hall, 1982.

[46] C. Wagner, “View Integration in Database Design,” Unpublished Ph.D. Dissertation, University of British Columbia, Vancouver, Canada 1989.
