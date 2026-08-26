---
otero_id: 14616
otero_key: "3HGSQ547"
title: "User-Database Interface: The Effect of Abstraction Levels on Query Performance"
authors: "Hock Chuan Chan; Kwok Kee Wei; Keng Leng Siau"
year: "1993"
journal: "MIS Quarterly"
doi: "10.2307/249587"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# User-Database Interface: The Effect of Abstraction Levels on Query Performance\*

By: Hock Chuan Chan
Department of Information
Systems and Computer Science
National University of Singapore
Lower Kent Ridge Road
Singapore 0511

Kwok Kee Wei
Department of Information
Systems and Computer Science
National University of Singapore
Lower Kent Ridge Road
Singapore 0511

Keng Leng Siau
The Faculty of Commerce and Business Administration
University of British Columbia
2053 Main Mall
Vancouver, B.C., Canada V6T 1Z2

## Abstract

A common classification of data models is based on their abstraction levels: physical, logical and conceptual. The user-database interaction can be similarly classified. For the conceptual-level interaction, the user and the database exchange information on the user's world, e.g., information of entities, relationships, and attributes. For the logical-level interaction, the user and the database communicate based on concepts in the database system, e.g., relations and join operations. We expect users to be familiar with concepts in their world but not the concepts in the database system. This is especially so for infrequent or naive database users. The conceptual level should therefore be easier because it is semantically closer to the user. This deduction was tested in an experiment using the entity-relationship (ER) model for the conceptual-level model and the relational model for the logical-level model. The results were affirmative. The users at the conceptual level had 38 percent higher accuracy and 16 percent higher confidence than users at the logical level. The conceptual-level users took 65 percent less time than the logical-level users, and it took 33 percent less time to train them. The differences were statistically significant with p<0.003. The huge differences indicate that noticeable improvements can be made by switching from the relational model to the ER model. The experiment also provided valuable data on errors commonly made by users.

Keywords: Data resource utilization, user-database interface, abstraction levels, conceptual level, logical level, relational model, entity-relationship model, query languages, SQL, experimental study, user performance

ISRL Categories: Al0105, CB0601, CB0602.03, CB0602.04, FB0401, FB0402.04, HC01, HC0102

## Introduction

Recent surveys on MIS issues show that effective use of the data resource is very important. For example, one survey shows that data resource is the second top critical issue (Niederman, et al., 1991). Another reports that chief information officers rate data utilization as the fourth most important issue (McCormick, 1991).

On the other hand, the design of effective user interfaces to the database systems has not been vigorously pursued. The major interface language is still SQL, a system that was developed almost 20 years ago (Chamberlain and Boyce, 1974) and was found to be very difficult, even for trained users (Date, 1990b; Greenblatt and Waxman, 1978; Welty, 1985; Welty and Stemple, 1981).

With the widespread availability of computers and data to not only MIS professionals but increasingly to end users, data access will expectedly remain an important issue, but with some new twists. To avoid any bottle-necks caused by heavy end-user demand on MIS professionals, it has become imperative to provide general-purpose database interfaces that enable end users to perform reliable database retrieval (and occasionally design) on their own.

We believe this is possible by migrating from the relational model to models that are at higher levels of abstraction, and we empirically test this view in this paper. Past empirical works on database query typically compare one model against another or one language against another. For example, much work was done to compare the three traditional models of relational, network, and hierarchical (Chamberlain, 1980; Greenblatt and Waxman, 1978; Reisner, 1981; Thomas, 1983; Welty, 1985; Welty and Stemple 1981). These studies showed the relational model to be the best of the three (Date, 1982; Goldstein, 1985; Lochovsky and Tsichritzis, 1977).

The traditional data models, however, are not expressive enough, and many semantic models have been proposed. The most common of these is probably the entity-relationship (ER) model (Chen, 1976). There are many claims that the ER model is better than the relational because it is easier to use and understand, or it is more natural. However, there are very few empirical studies on the relative merits of the ER model and the relational model. Two studies show slightly better user design using the ER model than the relational model (Batra, et al., 1990; Jarvenpaa and Machesky, 1986). However, one study shows no difference in query performance between the ER and relational model (Jih, et al., 1989). The apparently conflicting results raise an interesting and important question: Is there no difference in query performance for the ER and the relational models?

Although comparing model by model is interesting, we determined that it would be more meaningful to compare not just specific data models, but levels of data models. In this study, the models are grouped according to their abstraction levels. An abstraction-level model common in the database and information systems fields (Batini, et al., 1992; Gogolla and

Hohenstein, 1991; Olive, 1983; Teorey, 1990; Teorey, et al., 1986) is adopted to classify the user-database interaction and is described in the next section. The model, though common, has not been used to analyze empirical results on user performance for the various data models. This is used to show that the triumph of the relational model over the network and hierarchical models is actually the triumph of a higher abstraction level over a lower level. We therefore hypothesize that the ER model, which is an example of an even higher level, will be better than the relational model.

The rest of the paper is organized as follows. The next section describes the user-database interaction model. The following section gives a review of the few experimental studies that compare users' performance for the ER and relational models. The section after that describes the research model, the hypotheses, and the experimental procedure. Then the next section describes and discusses the experimental results. The final section interprets the practical implications of these findings and suggests some avenues for future research.

## User-Database Interface

User-database interfaces may be classified according to many factors. If we were interested in the mechanics of the interface, they might be classified under mouse, pen, or keyboard input. In this paper, we are interested in the substance of the user-database interaction. For textual commands, a user's input is a string of letters that conveys some concepts. Are these concepts about objects in the user's world or about storage structures in the computer? It is possible to classify user-database interfaces into abstraction levels based on the concepts that they use. There are three main levels—the physical, logical, and conceptual level. The physical level is the lowest, while the conceptual level is the highest. This is shown in Figure 1.

At the lowest level, the physical level, the user must know the details of the data structures in the computer memory. He or she may, for example, need to know the various files and physical pointers that link data to data, or records to records. A query will typically involve some specification and tracing of physical pointers.

![](/api/attachments/3HGSQ547/fulltext/images/bf619e3cd227a130899737b206905787ad81371756a3b915952537be559563d8.jpg)  
Figure 1. Levels of User-Database Interaction

This level is exemplified by the interfaces provided by the network and hierarchical data models, which have been aptly described as “navigational” (Bachman, 1973).

The user may even need to know the identifiers of files that store the data, as required by many microcomputer database systems. A database may be stored in several files and the user must know how the data are distributed among the files. The use of indices, row order, and column order also belong to this level.

The logical level deals with logical data. The physical storage is hidden. The user must know the layout of the logical data and the possible, and normally unspecified, relationship among data elements. This is exemplified by the relational database interfaces (Hawryszkiewycz, 1990), such as those provided by SQL, QBE, SQUARE, or relational algebra. There are no physical pointers or files, and the order of the columns and rows is not important. The linkages are in the mind of the user who knows that by joining relations based on certain fields, it is possible to specify relationships that at the physical level are represented by physical pointers. In fact, it is common to refer to joins as logical pointers.

The conceptual level deals with objects in the user's world. At this level, the database is supposed to know the user's world of entities and relationships. There are no logical pointers for the user to trace. Relationships are specified naturally, such as "where S supplies P" rather than with a roundabout join: "where s.sno = sp.sno and sp.pno = p.pno." More advanced concepts such as is-a relationships, aggregation, and relationships among relationship (Thalheim, 1991) are included in the conceptual level. Special characteristics for these concepts are directly supported at this level. For example, the inheritance of attributes and relationships from a supertype entity to a subtype entity is managed automatically.

A model that is suitable for this level of interaction is the entity-relationship (ER) model, as advocated by Batini, et al. (1992), Gogolla and Hohenstein (1991), Hawryszkiewycz (1990), Elmasri and Navathe (1989), and Teorey (1990). Like the relational model, the ER model is also a formal model. It has many proposed calculi and algebras, such as those proposed by Atzeni and Chen (1981), Chan (1991), Chen (1984), Gogolla and Hohenstein (1991), Parent and Spaccapietra (1984), and Parent, et al. (1989). Even the basically relational idea of normalization can be applied with the ER model (Ling, 1985). There are also many query languages proposed for the ER model (see, for example, Hohenstein (1989); Junet (1987); Roesner (1985); Subieta and Missala (1987); and Velez (1985)).

It is vital to note that these abstraction levels are different from the three levels proposed by the ANSI/SPARC Study Group on DBMSs (1975). The three levels there—internal, conceptual, and external—refer more to the DBMS architecture (Date, 1990a). The internal level refers to the storage details. The ANSI/SPARC conceptual level refers to an overall view of the data within the organization. The external level refers to views created to suit individuals or groups of users (Elmasri and Navathe, 1989). Date (1990a) calls these storage view, community user view, and individual user views, respectively. With this division, any model can be used at the conceptual level or the external level, or both. In fact, the external level need not be any formal model, it can just be a screen input. The abstraction levels can be used to further classify the community user view and individual user views.

We would also add that some interfaces have a mix of levels. For example, the common relational interfaces have both logical and physical-level concepts that the user has to deal with. The user must know the relations, which belong at the logical level, and the indexes, which belong at the physical level of efficient storage access.

We emphasize that these abstraction levels represent broad intervals in the semantic range from the user world of entities, relationships, and attributes to the core of the computer system that consists of 1s and 0s. For any interaction to occur, the semantic ranges understood by the user and the database system must overlap, i.e., the user and the system must have some common knowledge. Where the user understands the details at the physical level, there is no need for the database system to know the logical level. Where the user knows only the conceptual level, the system must know all three levels. Furthermore, there are transformations between the knowledge in the various levels, e.g., conceptual to logical transformations and logical to conceptual transformations.

Hence, the more the database system understands (the higher the level of interaction), the less the user needs to understand. This is the fundamental reason for hypothesizing that users will perform better at higher levels.

The abstraction-level classification leads to the hypothesis that it is not by random design that the relational model is better (for the user) than the network and hierarchical models. It is not just one data model being better than two other data models. It is reasonable to generalize that the logical level of interaction, represented by the relational model, is better than the physical level, represented by the hierarchical and network models. Since the logical level is better than the physical level, it is merely an extrapolation to hypothesize that the conceptual level will be even better than the logical level. This, however, needs to be empirically tested.

## Literature Review

A survey of empirical studies of data models revealed two categories—studies that compare one classical data model with another classical data model, and studies that compare the relational model with a semantic data model such as the ER model. There are many that empirically evaluate the classical data models (Chamberlain, 1980; Greenblatt and Waxman, 1978; Reisner, 1981; Reisner, et al., 1975; Thomas, 1983; Thomas and Gould, 1975; Welty, 1985; Welty and Stemple, 1981). However, very few empirical studies were found that compare the ER model and the relational model.

One study compares the user's performance in representing his or her world using the ER model and the relational model (Batra, et al., 1990). The modeling correctness was measured for different tasks of modeling various concepts, such as unary and binary relationships. The results show that for most tasks the ER model allowed significantly more accurate designs. The ER model was perceived by the subjects to be slightly easier to use, though the difference was not statistically significant. Another study compares database design using the relational model versus a simplified ER model, where relationships are represented only by lines without diamonds (Jarvenpaa and Machesky, 1986). The authors found better user performance with the simplified ER model.

Another experimental study reports on user performance when querying the ER model and the relational model (Jih, et al., 1989). The users looked at different models (either ER or relational) but they answered with the same query language, SQL. There was no significant difference in the semantic accuracy of the queries. However, users of the relational model took more time and made fewer syntactic errors.

The experiment failed to isolate the level of user-database interaction. SQL is inherently designed for use with the relational model. SQL users must understand logical pointers and specify join operations. Therefore, both ER and relational users had to know the logical level and manipulate logical pointers. This may explain the lack of difference in the semantic accuracy. Furthermore, users answered only four queries—two simple and two complex. A complex query involved a simple join of two relations. This is actually a rather simple query. There are much more complex queries in SQL, such as nested queries and the use of the "GROUP BY" clause.

The above experiment used SQL for both the ER and the relational groups because of a common concern with the interaction effects between the data model and the query language. However, it is impossible to have one language that suits two data models. If two data models are different, it is because they contain different constructs, and their languages must differ to reflect this.

A clear illustration is the Unified Database Language (UDL) (Date, 1982), designed to provide for relational, network, and hierarchical models. Date (1982, p.451) clearly states that the language features needed for the relational model form a subset of the language features needed for the hierarchical model; this subset is in turn a subset of the language features needed for the network model. Thus, users of different models need to learn the language to different extents. Interactive effects will not be eliminated even if we use UDL in an experiment to compare relational and network models.

Furthermore, a common language may not be optimal for both. It may be optimal for one, in which case the experiment will be biased. If it is not optimal for either of the two models, then the practical usefulness of the results is doubtful. There will be nagging questions of what will happen if users employ the optimal languages in practice.

In summary, we found two experiments that compare the ER and relational models for the task of database design. The ER model was found to be slightly superior. We found one experiment that compared the models for the task of database retrieval. However, the use of SQL for both models negated any advantages of the ER model because SQL is essentially relational. There is, therefore, a need for an empirical study that makes a clear distinction between the two models.

## Research Methodology

## Research model

The research model for this study is shown in Figure 2. The model asserts that the performance of a database user is influenced by the following four factors:

1. Data model characteristics

2. Task characteristics

3. User characteristics (human factors)

4. System characteristics

Three of the factors in this model were also proposed in Reisner (1981), where a survey of laboratory studies on query languages showed frequent use of task, data model, and user characteristics as factors affecting user performance. A literature survey of empirical studies in database design revealed that, when measuring user performance, it is necessary to add a fourth dimension to Reisner's model: the physical characteristics of the database system.

These system characteristics refer to physical aspects of the system. One aspect is the capability of the system, such as its response time and the physical input/output devices being used. Another aspect is “dialogue style.” This includes the question/answer approach, command languages, menus, icons, graphical representations, and “fill in the blanks.” The advantages and disadvantages of each style are not absolute but depend on the type of task, data model, and user characteristics.

## Research hypotheses

Based on the above discussions, particularly those in the second and third sections, our hypotheses on user performance at the conceptual and logical levels are now summarized. Three aspects of performance are measured—accuracy, confidence, and speed. The hypotheses are stated in null form. The alternative hypotheses are one-sided, since we have reasons, as discussed in the second section, to believe that performance at the conceptual level will be better.

H1: Subjects in the conceptual-level and the logical-level groups will show no time difference in formulating queries.

H1a: Subjects in the conceptual-level group will take less time than the subjects in the logical-level group.

H2: There will be no difference in the accuracy of the queries from subjects in the conceptual and logical-level groups.

![](/api/attachments/3HGSQ547/fulltext/images/f2366e6ba94bceba169189ac4d93fb8a0ab7eceda4d51db85859f78f099f56f5.jpg)  
Figure 2. A Research Model

H2a: Queries from subjects in the conceptual-level group will be more accurate than queries from subjects in the logical-level group.

H3: There will be no difference in the confidence of subjects in the conceptual and logical-level groups.

H3a: Subjects in the conceptual-level group will show more confidence than subjects in the logical-level group.

## Research method

A laboratory experiment was conducted to investigate the effects of the independent variable (the data model) on the dependent variables (user performance). The experimental plan and the number of subjects who completed the experiment is summarized in Table 1. The methodology was straightforward and similar to many previous studies. Therefore, no pilot test was conducted. Any pilot study to gauge the variances would have required a substantial number of subjects, and in effect, would have been very similar to the actual experiment. The experimental procedure was, however, tested among the three researchers.

## Independent Variable—The Data Model

The independent variable is the abstraction level of the data model used in the user-database interaction. The data model affects the way the user views and manipulates the data in the database. It is traditional to say that the user manipulates the data in the database. This is true for the logical level, where the logical data must be manipulated (e.g., join, project, select, and union). With a conceptual-level interface, it is more accurate to say that users manipulate the concepts of their world, which are also known to the database system. The independent variable was controlled to be either the conceptual level or the logical level. The conceptual-level subjects used the ER model with the ER query language KQL, and the logical-level subjects used the relational model with the relational query language SQL. As was discussed previously, the relational model is an example of the logical level, and the ER model is an example of the conceptual level. The validity of choosing the ER model for the conceptual level and the relational model for the logical level is well supported by textbooks on database design (Batini, et al., 1992; Elmasri and Navathe, 1989; Hawryszkiewycz, 1990; Hughes, 1991; Teorey, 1990). The validity is also clear from the following quotes, “The conceptual design of a database has so far been based on the entity-relationship model” (Vossen, 1991, p. 197), and “There exists an extensive literature on the (logical) design of relational database schemas” (Vossen, 1991, p. 258).

It should be noted that the relational model is sometimes used for conceptual modeling. This, however, is a bad choice, as noted by Gray, et al. (1992): “Classical data models are not suitable candidates for conceptual data modeling . . . all three models fail to capture much of the semantics . . . these models require extensive additional constraints to maintain the semantic integrity” (p. 5).

Table 1. Experimental Plan

<table><tr><td colspan="2">Abstraction Level of User-Database Interaction</td></tr><tr><td>Logical Level (Relational + SQL)</td><td>Conceptual level (ER + KQL)</td></tr><tr><td>24 subjects</td><td>23 subjects</td></tr></table>

Unlike the study by Jih, et al. (1989), the level distinction was made complete by providing a query language (KQL) tailored to the ER model. Hence, the conceptual level was operationalized by the ER model plus the ER query language KQL, and the logical level was operationalized by the relational model supported by the ANSI standard relational query language SQL.

SQL was selected because it is widely considered the best query language for the relational model. In fact, it is the ANSI and ISO standard for the relational model (Date, 1987; Negri, et al., 1991). It is the language that will be supported by most, if not all, relational DBMSs. In addition, various empirical studies on the relational languages did not show any others superior to SQL. For example, one study found no significant difference in accuracy between SQL and Query By Example (QBE) (Greenblatt and Waxman, 1978), and another study found no significant difference in accuracy between SQL and TABLET (Welty and Stemple, 1981).

There is no commonly used query language for the ER model. Instead, there are development products. Hence, KQL was used in this study. A BNF description of a subset of the KQL retrieval queries is given in Appendix A. Some examples of KQL queries are also given in Appendix B. Full details of its syntax are available in the Chan study (1989). It is a definition and query language designed specifically for the ER model, including concepts of is-a (specialization and generalization) relationships and inheritances. Like SQL,

KQL allows for arbitrarily complex queries; it allows nested queries and includes statistical functions such as count and average. Another reason for choosing KQL is that its format is very similar to SQL's. Both are command-line queries with set results. This removes any unwanted factors such as menu versus graphics or graphics versus command-line.

We stress that we are comparing two different abstraction levels. They cannot be made equal. Consider the two major differences of relationships and is-a inheritances. The conceptual-level system understands these concepts; it can automatically perform inheritance and link entities through relationships. In contrast, the logical-level system does not have these concepts. Users must do the inheritance and relationship joins themselves. These capabilities are beyond the logical-level systems. If the differences affect the results, then these can be attributed to the different abstraction levels. For reasons already given, a single language cannot be imposed for both levels. In fact, the languages should be different, and preferably the best that the two levels can offer.

## Controlled Variables

The other three factors in Figure 2 were controlled. The task was controlled by having the same set of queries for all subjects. The queries covered a comprehensive range from the very simple to the very difficult. The primary research interest was in the overall query performance. The 10 queries chosen covered the following semantic specifications:

\- Single entity

\- Two entities (of different types) connected by a relationship

\- Attribute condition

\- Two instances of the same type

\- Counting of relationships

• The quantifiers for all, and there exists

These cover all the basic queries that can be made on the ER model and the relational model. Ideally, we would like to include more queries, such as those with average or maximum computations. There is, however, a limit to the number of queries that can be performed in an experiment. If the subjects experience fatigue, the results may not be valid.

User characteristics were controlled as follows: 48 subjects (of which one was absent from the experiment) were randomly selected from a pool of 430 subjects. They were randomized into two groups for the two abstraction levels. The number of subjects (48) was an opportunistic decision based on estimates of the differences in the dependent measures. It was also comparable to the number of subjects used in many other similar studies, e.g., 17 in Gould and Ascher (1975), 39 in Thomas and Gould (1975), 64 (which were further divided into two groups based on individual characteristics) in Reisner, et al. (1975), 72 (which were also further divided into two groups based on individual characteristics) in Welty and Stemple (1981), 42 in Batra, et al. (1990), 36 and 20 in Jarvenpaa and Machesky (1986), and 56 in Jih, et al. (1989). The significance tests presented in the next section clearly show that our sample size was, in fact, adequate.

All the subjects had used computers before but had no database experience. On average, the students were 20 years old. To motivate the subjects, they were informed that course credit would be awarded. Students who did not participate in this experiment earned their credits by participating in other experiments. The subjects were told that they would be assessed based on their speed and accuracy in constructing the queries, and also based on the correlation between the accuracy of their queries and the self-reported confidence level. This encouraged them to report their confidence honestly rather than to show excessive confidence. One subject was absent, so the actual number was 47.

An important point to note is that our subjects are representative of users who are intelligent, have some computer experience, and little database training. Users matching these characteristics are likely to be at the executive or managerial levels, where end-user computing is most prevalent.

System characteristics were controlled by having the same system for both groups. This system was essentially a simple text editor, customized to display queries and record answers and other data. Although there were valid reasons to use real systems that can parse the answers, point out errors, and return results, the concern was that other factors could invalidate the empirical result. Real systems for KQL and SQL would have to be different, and they might therefore not be equally “user friendly.” These are important factors that should be carefully excluded. Hence, a simple text editor was chosen. It provides realism without introducing extraneous factors. This system has many advantages over a pencil and paper system: it is more realistic, it provides automatic timing (the subject cannot go back to previous answers whereby timing would be seriously jeopardized), and the output can be fed to programs for computerized extraction of two of the dependent measures.

## Training

The training was done in two groups: the KQL group and the SQL group. The subjects in each group were trained together. Two training booklets were used during the experiment: an SQL booklet (11 pages) for the logical-level group and a KQL booklet (11 pages) for the conceptual-level group. Each training booklet gave a brief overview of its data model and query language.

To maintain consistency, the same database domain (suppliers and parts) and the same example queries were used in both booklets. In addition, the same administrator provided the different training for each group.

All examples in the training booklets were discussed. Subjects practiced answering a question after each example. Feedback on query accuracy was given to improve learning before proceeding to the next example. All questions from the subjects were answered, and training continued until the subjects were fully satisfied. Training for the KQL group lasted for 1 hour; training for the SQL group was longer by 30 minutes. We allowed different training times because the main objective was to have the subjects fully trained. This was also done in other empirical studies (Batra, et al., 1990; Greenblatt and Waxman, 1978; Jarvenpaa and Machesky, 1986).

After a 10-minute break, the subjects had a practice session where they wrote queries using a practice program similar to the test program. This was to acquaint them with the mechanics of the interface so that during the real test, they would not have to spend time figuring out how to enter the query, how to report their confidence levels, or how to get to the next question. The measured time for the real test was then the real query formulation time. For consistency, the subjects in both groups were asked to construct the same set of queries using the same training database. The administrator answered all questions from the subjects.

Any biases toward SQL or KQL were eliminated as much as possible. The trainer had no hand in designing SQL or KQL. The students were not informed beforehand of the nature of the study. This prevented any student from learning SQL before the experiment. During the training, the students were simply informed that SQL (or KQL) was a database query language. They did not know that SQL was a standard language or that KQL was a development product.

Similar learning times were reported in previous experiments. For example, Greenblatt and Waxman (1978) reported 1 hour and 40 minutes for the learning of SEQUEL, which is an earlier version of SQL, and 1 hour and 35 minutes for QBE.

## Test

For the experiment, the students ran the test program in which they had to answer 10 questions based on a new database domain. The program displayed the questions one by one. Answers were entered directly into the computer via a simple text editor. Subjects could refer to the training material and use paper and pencil to help formulate the answers.

The same test program was used for both groups. This meant that both groups answered the same set of questions in exactly the same order. The conceptual-level group was given a diagram, on paper, of the ER model. The logical-level group had a diagram, also on paper, of a set of relations. The ER model and the set of relations showed the database about departments and employees. The diagrams, the set of 10 questions, and the sample answers can be found in Appendix B.

The computer automatically timed the interval between the display of the question and the time when the student keyed ctrl-Z, signifying that the query had been constructed. Immediately after each answer, the subjects were asked for their confidence in their answer, using values ranging from 0 (zero confidence) to 5 (absolute confidence). The proposed query, the time in seconds, and the confidence level for each question were recorded by the computer. In addition, the subjects had to enter their name at the beginning of the program.

## Dependent Variables—Performance

The dependent variables are the usual measures used in studies on query performance. These include the accuracy of the answer, the time taken to answer the query, and the subject's confidence in his answer. Time and confidence were measured as noted above. The accuracy of the answer, measured from 0 to 5, was determined separately by two graders. The separate grading provided an estimate of the reliability. The accuracy was an overall assessment of the correctness of the answer. Both semantic and syntactic accuracies were considered.

Accuracy is the most important measure. The other two are supportive measures. We considered having a grading scheme for both KQL and SQL. However, KQL and SQL have different concepts because they belong to different abstraction levels. As a result, there is very little overlap in their errors. The grading schemes will be very different, calling on subjective judgments on the seriousness of the different errors. Strict error classification is not possible for retrieval queries, since many actual errors fall into many classes. For example, although Batra, et al. (1990) used a grading scheme, certain errors were still left to the discretion of the graders. For our experiment, we graded based on an assessment of the overall accuracy of the query, bearing in mind the number of steps needed to correct the query, and the probable difficulty of doing so.

## Experimental Results and Discussions

## Statistical results

Two graders separately determined the accuracy of the students' answers. Each answer could get a maximum of 5 points and a minimum of 0 points. The grades for the 10 questions were totalled to give the score for each subject. The mean scores and the standard deviations (given in parentheses) for the subjects in the two groups are shown in Table 2.

Table. 2. Total Group Scores

<table><tr><td></td><td>Grader A</td><td>Grader B</td></tr><tr><td>SQL</td><td>32.2 (8.3)</td><td>32.9 (7.8)</td></tr><tr><td>KQL</td><td>44.4 (5.7)</td><td>44.9 (5.0)</td></tr></table>

The correlation coefficient for the grades from the two graders was 0.96. This showed a high reliability for the measure of accuracy. Thus, only the first set of grades was used for the subsequent tests. We note that using the second set of grades also produced the same statistical results.

The means and standard deviations (given in parentheses) for the three dependent variables of time, confidence, and accuracy of the two groups are shown in Table 3.

The t-test was suitable for testing the hypotheses because the independent variable had only two nominal levels. The t values and the significance levels are shown in Table 4. The probability values given are for one-tailed t-tests.

Table 4. T-test Results

<table><tr><td>Measure</td><td>t</td><td>P (Prob &gt; t)</td></tr><tr><td>Time</td><td>7.66</td><td>0.0001</td></tr><tr><td>Confidence</td><td>3.01</td><td>0.0027</td></tr><tr><td>Accuracy</td><td>5.86</td><td>0.0001</td></tr></table>

The two groups had different variances for time and the same variances for accuracy and confidence. Hence, the t-test for time was based on the assumption of unequal variances. An additional non-parametric test was done for the measures of accuracy and confidence, in case these were only ordinal and not interval. The Mann-Whitney U test obtained p values of 0.0001 for accuracy and 0.005 for confidence, supporting the results from the t-test. These tests were done using the SAS software.

The null hypotheses about time and accuracy were rejected at the 0.01% level. The null hypothesis about confidence was rejected at the 0.27% level. We therefore accept all the alternative hypotheses. Users are better at the conceptual level than at the logical level. The results supported the basic hypothesis that users can perform better at higher abstraction levels. The reason is that the higher levels have semantics closer to the user's world so that the user needs to know less, while the system needs to know more.

Table 3. Scores for Dependent Variables

<table><tr><td>Measure</td><td>SQL Mean (Std. Dev.)</td><td>KQL Mean (Std. Dev.)</td></tr><tr><td>Time</td><td>2569 (1024)</td><td>894 (306)</td></tr><tr><td>Confidence</td><td>35.6 (7.5)</td><td>41.3 (5.1)</td></tr><tr><td>Accuracy</td><td>32.2 (8.3)</td><td>44.4 (5.7)</td></tr></table>

## Discussion

## General Results

The results are in sharp contrast to the results found by Jih, et al. (1989), which showed little difference in the performances using the ER model and the relational model. We believe there are two reasons for the different results. The main reason is that a special ER query language, KQL, was used in this study, making the distinction between the ER and the relational model complete. Jih, et al. (1989) used SQL for both models, thus, the distinction was not clear.

The other reason is that our subjects were tested with more queries covering a much wider range. In fact, for the simple queries that involve only one relation, our study also showed no significant differences in the accuracies—because the scores were all close to the maximum score!

For all but one question, the confidence of the SQL group exceeded its accuracy. In contrast, for all but one question, the confidence of the KQL group was lower than its accuracy. The correlation coefficient for accuracy and confidence for the two groups are, however, the same. The explanation for this phenomenon may be this: in SQL, it is easier to make mistakes unknowingly.

This observation corroborates previous studies (Welty, 1985; Welty and Stemple, 1981), which found that subjects tend to omit join operations without realizing that these are needed. For example, for question 5, one subject specified a join based on employee name and department name directly without the intermediate relation WORK. The accuracy was low (1) but the confidence was high (4). Another subject specified the join using the correct key fields but again without the intermediate relation WORK. The accuracy was low (2) but the confidence was high (5). Some subjects specified one join correctly but omitted the second join, and they also reported high confidence levels.

Compared to the study by Jih, et al. (1989), our subjects answered the queries much faster. The average time for the SQL group for a single-relation query was only 0.82 minutes, compared to the average of 3.53 minutes recorded by Jih, et al. The average for the same queries for the KQL group was 0.49 minutes, compared to 2.38 minutes recorded by Jih, et al. Similarly, large differences exist for the one-join queries. It is difficult to explain the large differences since the subjects were all undergraduate students and they had roughly the same amount of training. One possibility may be the different methods of determining the time taken. The study by Jih, et al. (1989) used a paper and pencil test, and presumably the timing was self-reported. Our study used a computer program to automatically and precisely record the time taken for each query for each subject.

The results show that users with relatively little computer experience, immediately after a training session, performed better at the conceptual level than at the logical level. Will experienced database users benefit by switching from the logical level to the conceptual level? We suggest the answer is yes, after they have gone through the learning curve for the new level. The basic idea of the abstraction levels is that the higher the interface level, the less knowledge the user needs to learn. This applies to all users, expert or beginner. We concede that those who are already expert in use of the logical level may not gain advantages as large as those found by this study.

The difference in training time is 50 percent (one hour for KQL vs. one and a half hours for SQL). This suggests that KQL is easier to learn. That could be a significant factor in getting end users to learn database design and use.

## Question-By-Question

This study used a query-by-query analysis, which is important for two reasons. First, it showed the contribution of various queries to the overall results and identified the queries that are statistically different. Second, it provided a list of the common errors made by the subjects at the different abstraction levels. This allowed us to devise possible solutions to handle the errors. Table 5 shows the dependent measures for each of the 10 queries, averaged for all the subjects. The values in parentheses show the standard deviation. Pictorial views of the dependent measures for each of the 10 queries are shown in Figures 3a, 3b, and 3c.

The graphs clearly show that not all queries are significantly different between the two groups. A t-test for each query based on the measure of accuracy showed that queries 1, 2, 3, and 7 were not significantly different, while the other 6 queries were significantly different with p values of 0.001.

Table 5. Dependent Measures for Each Query

<table><tr><td>Query</td><td>Group</td><td>Time</td><td>Confidence</td><td>Accuracy</td></tr><tr><td rowspan="2">1</td><td>KQL</td><td>33.2 (18.5)</td><td>4.26 (1.54)</td><td>4.83 (0.39)</td></tr><tr><td>SQL</td><td>51.1 (20.9)</td><td>4.92 (0.28)</td><td>4.83 (0.38)</td></tr><tr><td rowspan="2">2</td><td>KQL</td><td>25.5 (10.6)</td><td>4.91 (0.29)</td><td>5.00 (0.00)</td></tr><tr><td>SQL</td><td>47.5 (29.0)</td><td>4.87 (0.61)</td><td>5.00 (0.00)</td></tr><tr><td rowspan="2">3</td><td>KQL</td><td>49.3 (26.8)</td><td>4.04 (1.55)</td><td>4.78 (0.85)</td></tr><tr><td>SQL</td><td>162.0 (82.1)</td><td>4.33 (1.27)</td><td>4.21 (1.96)</td></tr><tr><td rowspan="2">4</td><td>KQL</td><td>105.4 (62.9)</td><td>3.43 (1.31)</td><td>4.70 (.093)</td></tr><tr><td>SQL</td><td>248.8 (151.4)</td><td>3.58 (1.44)</td><td>2.87 (.196)</td></tr><tr><td rowspan="2">5</td><td>KQL</td><td>93.6 (41.8)</td><td>4.57 (0.66)</td><td>4.43 (0.51)</td></tr><tr><td>SQL</td><td>245.3 (167.0)</td><td>3.92 (1.41)</td><td>2.83 (1.86)</td></tr><tr><td rowspan="2">6</td><td>KQL</td><td>224.0 (124.7)</td><td>2.57 (1.95)</td><td>2.78 (1.09)</td></tr><tr><td>SQL</td><td>432.2 (310.7)</td><td>3.00 (1.56)</td><td>1.33 (1.27)</td></tr><tr><td rowspan="2">7</td><td>KQL</td><td>170.4 (98.8)</td><td>3.39 (1.16)</td><td>3.48 (1.83)</td></tr><tr><td>SQL</td><td>288.4 (192.1)</td><td>2.92 (1.98)</td><td>2.92 (2.10)</td></tr><tr><td rowspan="2">8</td><td>KQL</td><td>92.3 (58.6)</td><td>4.61 (0.66)</td><td>4.83 (0.83)</td></tr><tr><td>SQL</td><td>423.4 (319.6)</td><td>2.50 (1.50)</td><td>2.46 (1.47)</td></tr><tr><td rowspan="2">9</td><td>KQL</td><td>55.0 (24.7)</td><td>4.74 (0.86)</td><td>4.83 (0.83)</td></tr><tr><td>SQL</td><td>310.5 (136.6)</td><td>2.83 (1.58)</td><td>2.62 (1.66)</td></tr><tr><td rowspan="2">10</td><td>KQL</td><td>45.7 (19.0)</td><td>4.74 (1.05)</td><td>4.74 (0.86)</td></tr><tr><td>SQL</td><td>359.5 (200.7)</td><td>2.75 (1.73)</td><td>3.12 (1.62)</td></tr></table>

The first three questions concern only one entity. These were easy for both groups, with scores between 4.21 to 5.00. Query 7 involved the specification of two instances of employee. This was difficult for both groups, though KQL users performed slightly better. The other queries required the specification of relationships. These were much easier for the KQL group. The SQL group showed frequent difficulties in performing the necessary joins. For queries that involved relationships, the differences in accuracy were higher than the overall 38 percent.

The specification of relationships is essential to complex database retrievals. In fact, if there were no relationships, then there would be little need for DBMSs. Relationship specification cannot be automated for relational languages because the necessary knowledge is absent from the relational model; but models such as ER possess this knowledge and so can support automation.

In KQL, the inherent ability to specify relationships naturally is extended to cover the counting of relationships. For example, in English we may say “who are the students taking more than four courses?” In KQL, we state that condition as “student take >4 course,” without the need to use extra statements like “GROUP BY” and “HAVING.” Performance differences for queries with such conditions were also statistically different.

A detailed examination of the answers showed the following list of errors.

1. Wrong order in the data selection. Apparently, some subjects did not consider the order important.

2. Misunderstanding of attribute inheritance (only KQL).

![](/api/attachments/3HGSQ547/fulltext/images/c3e574e44e3caa8909de419b9fc8b2cfb343dd5750b6a4dee6fadb07ac335350.jpg)  
Figure 3a. Accuracy for Each Question

![](/api/attachments/3HGSQ547/fulltext/images/ab633ce0547181efef6e0e731bf0f29be5cda80f3c40e052530eae144905420a.jpg)  
Figure 3b. Confidence for Each Question

![](/api/attachments/3HGSQ547/fulltext/images/0fdb98937978561ef43e1d613ce6ca16e1f3de4c8e50f3f1abc1e36aacfb7312.jpg)  
Figure 3c. Time Taken (in Seconds) for Each Question

3. Wrong qualification of a column (e.g., engineer.name instead of the correct employee.name).

4. Joining wrong relations (only SQL).

5. Joining wrong fields of the correct relations (only SQL).

6. Making extra joins (only SQL).

7. Having extra relations (only SQL).

8. Omitting relations (only SQL).

9. Omitting necessary conditions.

10. Failure in specification of more than one instance of the same type.

11. Unnecessary use of GROUP BY and COUNT clauses.

12. Mixing the sequence of WHERE, GROUP BY, and HAVING. This confusion was also noted in a previous SQL study (Welty, 1985).

13. Incorrect shortening of conditions. Some examples are:

writing department = 'research' instead of department name = 'research.'

writing A department = B department instead of the correct A work-related department and B work-related department.

writing P salary > Jack salary, employee salary > 'Jack' salary, or even employee salary > 'Jack' instead of Q name = 'Jack' and P salary > Q salary.

This error is likely to be a carryover of the normal English usage where it is more natural to say the research department rather than the department whose name is research.

In summary, the common KQL errors are the specification of multiple instances of the same entity or relationship type, the direct usage of nouns as in natural language, and a tendency to treat connected entities as attributes. The frequent SQL errors include the omission of joins, the omission of required relations, the inclusion of irrelevant relations and joins, joins on incompatible fields, and syntactic confusion over the handling of WHERE, GROUP BY, and HAVING clauses.

## Implications

Let us consider the practical implications of this result. The percentage differences of the KQL group over the SQL group are shown in Figures 4a, 4b, and 4c.

Large percentage differences were found for the two groups. Subjects in the conceptual group took only 35 percent of the time required by the logical-level group; they were also 16 percent more confident and 38 percent more accurate. These large differences should be of practical significance.

![](/api/attachments/3HGSQ547/fulltext/images/d2e33defd46d70e6c09fd1a818c50a1ef37ee820c4966a9cfb673d1bf2aadc1a.jpg)  
\*The maximum score of 50 would be achieved by a rating of 5 for each of the 10 queries.

Figure 4a. Accuracy Levels by KQL and SQL Groups  
![](/api/attachments/3HGSQ547/fulltext/images/f7611bbbb1d8363fb50a89d8eabf8205627f5d0d0e632b7f6e6ac51e5576ce01.jpg)  
\*The maximum score of 50 would be achieved by a rating of 5 for each of the 10 queries.

Figure 4b. Confidence Levels of KQL and SQL Groups  
![](/api/attachments/3HGSQ547/fulltext/images/c4fbb6fdddb759c8821eacdd9374eacf9f64213a046dbbd78a53ac9aaaa8bba2.jpg)  
Figure 4c. Time Taken by KQL and SQL Groups

An immediate effect on the end user's use of databases is not expected because there are no widely available commercialized ER database systems. However, many CASE tools that assist in the design of ER models are available (Batini, et al., 1992), and many research prototypes that allow ER queries have been built (Hohenstein, 1989; Junet, 1987; Roesner, 1985; Subieta and Missala, 1987; and Velez, 1985). The technology for such systems is available. If the demand is perceived by users and developers, there will be full-fledged ER systems in the near future.

Full-fledged ER systems will remove an anomaly in the existing methodology of database design and use. Many database models are designed based on the high-level ER model, but the use is based on the low-level relational model (Chen, 1976; Parent and Spaccapietra, 1985; Storey and Goldstein, 1988; Teorey, et al., 1986). ER systems will allow both designers and users to concentrate on only one model.

There are many add-on front-ends to SQL (Riccuiti, 1992) that help the user to assess the data and write reports. Some of these present a universal relation view, where all the relations are lumped into one. Some present the tables separately but help the users to join them appropriately. If the view is still basically tables and fields, then the front-ends remain at the logical level of abstraction. The assistance provided is of a syntactical nature. However, front-ends can be radically different. For example, some prototype ER systems are built as front-ends to relational DBMSs. These hide the relational system totally and present conceptual-level interfaces.

## Conclusion and Future Research

This study has highlighted an abstraction-level model to classify user-database interfaces, which provides an important framework to analyze empirical data on user performance for database tasks. It allows the existing results on model-versus-model comparisons to be generalized to comparisons of abstraction levels. Thus, data about the relational model versus the network model and the hierarchical model can be used to support hypotheses that the logical level is better than the physical level.

This framework has an important contribution for future empirical studies: we must not be unduly worried about the interaction effect between model and language. When models of different levels are compared, the languages must of necessity differ. We cannot compare ER and relational, or object-oriented and relational, based on one language. An analogy would be to compare the ease of applying music and structural engineering by asking the users to use a single language.

The literature survey showed that no studies have been made to compare user performance on database retrieval between the conceptual and the logical level. We conducted such a study to verify three hypotheses that the conceptual level is better than the logical level.

This experimental study produced confirming results. Conceptual-level queries were formulated in 35 percent of the time taken for logical level queries; they were also 38 percent more accurate. Furthermore, users of the conceptual level were 16 percent more confident. It also took 33 percent less time to train the conceptual-level users. We believe the results have significant practical implication: users can benefit greatly if they can replace the relational interface with an ER interface.

The experiment also provided many subject answers, which were analyzed to identify common errors in query retrieval. These common errors can be used to improve the user-database interface, either by modifying the query languages or by providing supplementary facilities in the interface.

Our study addresses the task of information retrieval. In addition, Batra, et al. (1990) and Jarvenpaa and Machesky (1986) show that users are better at designing ER models than relational models. Given the scarcity of empirical studies in this area, more studies are needed to confirm the findings. Besides database design and data retrieval, the other major task division is the update of information. This too needs to be tested.

Research on data models within an abstraction level is also of interest. Examples include past studies that compare the hierarchical and the network models, as well as studies that compare different query languages for the relational model. Future studies may compare different languages for the ER model or compare different models that belong to the conceptual level, such as the ER model and other object-oriented models.

For practitioners and end users working with database systems, the results show a possible path to improve their productivity. Unfortunately, there is presently no commercial system that fully supports the ER model. While many commercial CASE tools support the design of ER models (Batini, et al., 1992), none support ER query. On the other hand, many research ER systems have been reported. Most of them are built on top of existing DBMSs. Hence, the technology is available.

Finally, the abstraction-level model is relevant to HCI theory building. Consider the theory by Shneiderman (1987), which differentiates between task concepts and computer concepts. Task concepts correspond to the concepts in the conceptual level, while computer concepts correspond to the concepts in the logical and physical levels. The experiment shows that it is possible to free users from understanding and manipulating computer concepts and by so doing, improve user performance.

## Acknowledgements

We deeply appreciate the many comments by the senior editor, associate editor, and reviewers. They helped to shape this article into its final version.

## References

ANSI/X3/SPARC Study Group on Data Base Management Systems. “Interim Report, FDT,” ACM SIGMOD (7:2), 1975.

Atzeni, P. and Chen, P.P. “Completeness of Query Languages for the Entity Model,” in Entity-Relationship Approach to Information Modeling and Analysis, P.P. Chen (ed.), North-Holland, Amsterdam, 1981, pp. 109-122.

Bachman, C.W. "The Programmer as Navigator," Communications of the ACM (16:1), November 1973, pp. 653-658.

Batini, C., Ceri, S., and Navathe, S.B. Conceptual Database Design, An Entity Relationship Approach, The Benjamin/Cummings Publishing Company Inc., Menlo Park, CA, 1992.

Batra D., Hoffer, J.A., and Bostrom, R.P. "Comparing Representations with Relational and EER Models," Communications of the ACM (33:2), February 1990, pp. 126-139.

Chamberlain, D.D. "A Summary of User Experience with the SQL Data Sublanguage," Proceedings of the International Conference on Data Bases, July 1980, Aberdeen, Scotland, pp. 181-203.

Chamberlain, D.D. and Boyce, R.F. "SEQUEL: A Structured English Query Language," Proceedings of the 1974 ACM SIGMOD Workshop on Data Description, Access, and Control, Ann Arbor, MI, May 1974.

Chan H.C. A Knowledge Level User Interface Using the Entity-Relationship Model, unpublished Ph.D. dissertation, The University of British Columbia, Vancouver, BC., 1989.

Chan H.C. "An Entity-Relationship Enhanced Logic System," The Second International Symposium on Database Systems for Advanced Applications, Tokyo, April 1991, pp. 401-410.

Chen P.P. “The Entity-Relationship Model: Towards a Unified View of Data,” ACM Transactions on Database Systems (1:1), March 1976, pp. 9-36.

Chen, P.P. "An Algebra for a Directional Binary Entity Relationship Model," Proceedings of the First International Conference on Data Engineering, April 1984, pp. 37-41.

Date, C.J. An Introduction to Database Systems, Addison-Wesley, Reading, MA, 1982.

Date, C.J. A Guide to the SQL Standard, Addison-Wesley, Reading, MA, 1987.

Date, C.J. An Introduction to Database Systems, Volume I, 5th edition, Addison-Wesley, Reading, MA, 1990a.

Date, C.J. "What's Wrong with SQL?" in Relational Database Writings, 1985-1989, C.J. Date (ed.), Addison-Wesley, Reading, MA, 1990b.

Elmasri, R. and Navathe, S.B. Fundamentals of Database Systems, Addison-Wesley, Reading, MA, 1989.

Gogolla, M. and Hohenstein, U. “Towards a Semantic View of an Extended Entity-Relationship Model,” ACM Transactions on Database Systems (16:3) September 1991, pp. 369-416.

Goldstein, R.C. Database Technology and

Management, John Wiley, New York, NY, 1985.

Gould, J.D. and Ascher, R. "Use of an IQF-like Query Language by Non-Programmers," IBM Research Report, RC-5279, Yorktown Heights, NY, 1975.

Gray, P.M.D., Kulkarni, K.G., and Paton, N.W. Object-Oriented Databases, A Semantic Data Model Approach, Prentice Hall, Englewood Cliffs, NJ, 1992.

Greenblatt, D. and Waxman, J. "A Study of Three Database Query Languages," in Databases: Improving Usability and Representativeness, B. Shneiderman (ed.), Academic Press, New York, NY, 1978.

Hawryszkiewycz, I.T. Relational Database Design, Prentice Hall, Paramato, NSW, Australia, 1990.

Hohenstein, U. "Automatic Transformation of an Entity-Relationship Query Language into SQL," Proceedings of the Eighth International Conference on Entity-Relationship Approach, Toronto, Canada, October 1989, pp. 309-327.

Hughes, J.G. Object-oriented Databases, Prentice Hall, Hemel Hempstead, Hertfordshire, UK, 1991.

Jarvenpaa, S.L. and Machesky, J.J. "End User Learning Behavior in Data Analysis and Data Modeling Tools," Proceedings of the Seventh International Conference on Information Systems, San Diego, CA, December 1986, pp. 152-167.

Jih, W.J.K., Bradbard, D.A., Snyder, C.A., Thompson, N.G.A. "The Effects of Relational and Entity-Relationship Data Models on Query Performance of End-Users," International Journal on Man-Machine Studies (31:3), September 1989, pp. 257-267.

Junet, M. "Design and Implementation of an Extended Entity-Relationship Data Base Management System (ECRINS/86)," in Entity-Relationship Approach, S. Spaccapietra (ed.), Elsevier Sciences Publishers, New York, NY, 1987.

Ling, T.W. "A Normal Form for Entity-Relationship Diagrams," The 4th International Conference on Entity-Relationship Approach, IEEE Computer Society Press, Washington, D.C., 1985.

Lochovsky, F.H. and Tsichritzis, D.C. "User Performance Considerations in DBMS Selection," Proceedings, ACM SIGMOD, Toronto,

Canada, August 1977, pp. 128-134.

McCormick, J.J. "CIOs Reassess Priorities," Information Week, December 16, 1991, p. 13.

Negri, M., Pelagatti, G., and Sbattella, L. "Formal Semantics of SQL Queries," ACM Transactions on Database Systems (17:3), September 1991, pp. 513-534.

Niederman, F., Brancheau, J.C., and Wetherbe, J.C. “Information Systems Management Issues for the 1990s,” MIS Quarterly (15:4), December 1991, pp. 475-500.

Olive, A. "Analysis of Conceptual and Logical Models in Information Systems Design Methodologies," in Information Systems Design Methodologies, T.W. Olle, H.G. Sol, and C.J. Tully (eds.), Elsevier Science Publishers, Amsterdam, The Netherlands, IFIP 1983.

Parent, C. and Spaccapietra, S. "An Entity-Relationship Algebra," First International Conference on Data Engineering, Los Angeles, CA, April 1984, pp. 500-509.

Parent, C. and Spaccapietra, S. "Enhancing the Operational Semantics of the Entity-Relationship Model," in Data Semantics (DS-1), T.B. Steel, Jr. and R. Meersman (eds.), Elsevier Science Publishers, Amsterdam, The Netherlands, 1985.

Parent, C., Rolins, H., Yetongnon, K., and Spaccapietra, S. "An ER Calculus for the Entity-Relationship Complex Model," in Proceedings of the 8th International Conference on Entity-Relationship Approach, F.H. Lochovsky (ed.), Toronto, Canada, October 1989, pp. 248-262.

Reisner, P. "Human Factors Studies of Database Query Languages: A Survey and Assessment," Computing Surveys (13:1), March 1981, pp. 13-31.

Reisner, P., Boyce, R., and Chamberlain, D. "Human Factors Evaluation of Two Data-base Query Languages: SQUARE and SEQUEL," Proceedings of the National Computer Conference (Vol 44), AFIPS Press, Anaheim, CA, May 1975, pp. 447-452.

Riccuiti, M. "Idiot-Proof Your SQL Queries," Datamation (38:8), April 1, 1992, pp. 61-62.

Roesner, W. "DESPATH: An Entity Relationship Manipulation Language," The 4th International Conference on Entity-Relationship Approach, IEEE Computer Society Press, Washington D.C., October 1985.

Shneiderman, B. Designing the User Interface:

Strategies for Effective Human-Computer Interaction, Addison-Wesley, Reading, MA, 1987.

Storey, V.C. and Goldstein, R.C. "A Methodology for Creating User Views in Database Design," ACM TODS (13:3), September 1988.

Subieta, K. and Missala, M. "Semantics of Query Languages for the Entity Relationship Model," in Entity-Relationship Approach, S. Spaccapietra (ed.), Elsevier Sciences Publishers, Amsterdam, The Netherlands, 1987, pp. 197-216.

Teorey, T.J. Database Modeling and Design: The Entity-Relationship Approach, Morgan Kaufmann Publishers, Inc., San Mateo, CA, 1990.

Teorey, T.J., Yang, D., and Fry, J.P. "A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model," Computing Surveys (18:2), June 1986, pp. 197-222.

Thalheim, B. "Extending the Entity-Relationship Model for a High-Level Theory-Based Database Design," in Next Generation Information System Technology, J.W. Schmidt and A.A. Stogny (eds.), Springer-Verlag, Berlin, Germany, 1991.

Thomas, J.C. “Psychological Issues in the Design of Database Query Languages,” in Designing For Human-Computer Communication, M.E. Sime and M.J. Coombs (eds.), Academic Press, London, 1983.

Thomas, J. and Gould, J. "A Psychological Study of Query By Example," National Computer Conference Proceedings (Vol. 44), AFIPS Press, New York, NY, May 1975, pp. 439-445.

Velez, F. “LAMBDA: An Entity Relationship Based Query Language for the Retrieval of Structured Documents,” The 4th International Conference on Entity-Relationship Approach, IEEE Computer Society Press, Washington, D.C., October 1985.

Vossen, G. Data Models, Database Languages

and Database Management Systems, Addison-Wesley, Cornwall, England, 1991.

Welty, C. "Correcting User Errors in SQL," International Journal of Man-Machine Studies (22:4), April 1985, pp. 463-477.

Welty C. and Stemple, D.W. "Human Factors Comparison of a Procedural and a Non-procedural Query Language," ACM Transactions on Database Systems (6:4), December 1981, pp. 626-649.

## About the Authors

Hock Chuan Chan is a lecturer in the Department of Information Systems and Computer Science at the National University of Singapore. He lectures in programming and databases. He obtained his B.A. and M.A. from the University of Cambridge, UK, and Ph.D. in management information systems from the University of British Columbia, Canada. His research interests include database and system modeling, query languages, and user-database interactions.

Kwok Kee Wei received his D.Phil in computer science from the University of York, UK. He is a senior lecturer in the Department of Information Systems and Computer Science, National University of Singapore. His research interests include electronic data interchange systems, inter-organizational systems, strategic information systems planning, group decision support systems, and user-database interaction.

Keng Leng Siau is a doctoral candidate in MIS at the University of British Columbia. He received his B.S. and M.S. degrees in computer and information sciences from the National University of Singapore. His research interests include human-computer interaction, systems analysis and design, and data modeling.

## Appendix A

## Syntax of KQL

A BNF description of the syntax of a subset of the KQL retrieval queries is given below. This subset is sufficient to form the queries used in the test. The full KQL language for retrieval, update, and model definition can be found in Chan (1989).

```txt
<query> ::= [<instance-clause>] <select-clause> [<where-clause>].
<instance-clause> ::=
    <variable-name> IS <entity/relationship-name>
    {,<variable-name> IS <entity/relationship-name>}
```

Variable-names define the entity/relationship instances that are required in a particular query. Throughout a query, the same variable will refer to the same instance.

```txt
<select-clause> ::= SELECT <select-item> {,<select-item>}
<select-item> ::= 
    <variable-name> <attribute-name>
    | <variable-name> *
    | <arithmetic-operation>
```

Select-items are the items that will be printed by the query.

```txt
<where-clause> ::= WHERE <condition-list>
<condition-list> ::= 
    <condition-andlist> [OR <condition-list>]
<condition-andlist> ::= 
    <condition> [AND <condition-andlist>]
<condition> ::= 
    NOT (<condition-list>)
    <relationship-existence-condition>
    <comparison-condition>
    <membership-condition>
    <exists-condition>
    <combination-relationship-condition>
```

Where-clause consists of a logical combination of basic conditions.

```txt
<relationship-existence-condition> ::=
    <variable-name> <variable-name> <variable-name>
```

This condition states that the first and third variables (instances) are related through the second variable, which must be a relationship instance.

```txt
<comparison-condition> ::=
    <value> <comparison> <value>
<comparison> ::=
    = | < | > | <= | >=
```

This condition allows the attribute values of instances to be compared. A <value> is an arithmetic expression that may involve attribute values and statistical functions, such as COUNT, AVG, MAX, MIN and SUM on these values. It can also be a simple integer or string.

```txt
<membership-condition> ::=
    <value> IN (<list-of-values>)
<list-of-values> ::=
    <value> {,<value>}
<list-of-values> ::=
```

```ini
[ <instance-clause> ]
SELECT <value>
[<where-clause> ]
<exists-condition> ::=
    EXISTS (<query>)
<combination-relationship-condition> ::=
    <variable-name> <relationship-name>-RELATED <variable-name>
```

This condition allows the specification that the two variables, which must be entity instances, be related through the specified relationship. The particular instance of the relationship that relates the two entity instances is not important.

```txt
<combination-relationship-condition> ::=
    <variable-name> <relationship-name>-RELATED
    <number-specification> <entity-type-name>
    <number-specification> ::=
    ALL | NO | [<comparison>] <integer>
```

This condition allows the counting of instances of type <entity-type-name> that are related to the variable instance through the relationship type <relationship-name>. The relationship instances that link these entity instances are not important. Also, the particulars of the entity instances of type <entity-type-name> are not important.

## Appendix B

## Database and Queries for the Experiment

This appendix contains the ER diagram, the relational schema, and the set of questions that were given to the subjects. The sample answers to the questions are also listed here.

![](/api/attachments/3HGSQ547/fulltext/images/6c02f9a04ad8cb15e980d0853a2c5ed78eeb55996c71f04ca842c4257852983d.jpg)  
Figure B1. An Entity Relationship Model

![](/api/attachments/3HGSQ547/fulltext/images/b117b827ad18f5d80607b4161a3bbb22f57d0f0da25e20c7e1c5f137f9229682.jpg)  
Figure B2. The Relational Schema

## Questionnaire:

1. Show the names and numbers of all employees.

2. Show the department name and city.

3. Show the engineers' numbers, names and professions.

4. Show the names of employees who head any projects.

5. Show the names of employees who work in the research department.

6. Show the names of employees who work in the same department as Jack.

7. Show the names of employees with higher salaries than Jack's.

8. List the names of managers who manage more than one department.

9. List the names of engineers who do not head any projects.

10. List the names of engineers who head all projects.

## Sample SQL Answers:

1. SELECT NAME, NUMBER FROM EMPLOYEE

2. SELECT NAME, CITY FROM DEPARTMENT

3. SELECT EMPLOYEE.NUMBER, NAME, PROFESSION FROM EMPLOYEE, ENGINEER
WHERE EMPLOYEE.NUMBER = ENGINEER.NUMBER

4. SELECT NAME FROM EMPLOYEE, HEAD

WHERE EMPLOYEE.NUMBER = HEAD.ENGINEER\_NUMBER

5. SELECT EMPLOYEE.NAME 
FROM EMPLOYEE, WORK, DEPARTMENT 
WHERE DEPARTMENT.NAME = 'RESEARCH'
AND WORK.EMPLOYEE\_\_NUMBER = EMPLOYEE.NUMBER 
AND WORK.DEPARTMENT\_\_NUMBER = DEPARTMENT.NUMBER

6. SELECT E1.NAME 
FROM EMPLOYEE E1, EMPLOYEE E2, WORK W1, WORK W2 . 
WHERE E1.NUMBER = W1.EMPLOYEE\_NUMBER 
AND E2.NUMBER = W2.EMPLOYEE\_NUMBER AND E2.NAME = 'JACK' 
AND W2.DEPARTMENT\_NUMBER = W1.DEPARTMENT\_NUMBER.

8. SELECT EMPLOYEE.NAME FROM EMPLOYEE, MANAGEMENT WHERE EMPLOYEE.NUMBER = MANAGEMENT.MANAGER\_\_NUMBER GROUP BY EMPLOYEE.NUMBER HAVING COUNT(\*) > 1

9. SELECT NAME FROM EMPLOYEE
WHERE NOT EXISTS
(SELECT \*
FROM HEAD
WHERE HEAD.ENGINEER\_NUMBER = EMPLOYEE.NUMBER)

10. SELECT NAME FROM EMPLOYEE
WHERE NOT EXISTS
(SELECT \*
FROM PROJECT
WHERE NOT EXISTS
(SELECT \* FROM HEAD
WHERE HEAD.ENGINEER\_NUMBER = EMPLOYEE.NUMBER AND HEAD.PROJECT\_NUMBER = PROJECT.NUMBER))

## Sample KQL Answers:

1. select employee name, number.

2. select department name, city.

3. select engineer number, name, profession.

4. select employee name where employee head project.

5. select employee name where employee work department and department name = 'research.'

6. E1 is employee, E2 is employee select E1 name where e1 work-related department and e2 work-related department and e2 name = 'Jack.'

7. E1 is employee, E2 is employee
select E1 name
where E1 salary > E2 salary and E2 name = 'Jack.'

8. select manager name

9. select engineer name
where engineer head-related no project.

10. select engineer name
where engineer head-related all project.
