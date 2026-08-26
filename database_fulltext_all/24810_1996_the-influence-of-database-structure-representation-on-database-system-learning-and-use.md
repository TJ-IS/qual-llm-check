---
otero_id: 24810
otero_key: "AFH8ZU6W"
title: "The Influence of Database Structure Representation on Database System Learning and Use"
authors: "Robert L. Leitheiser; Salvatore T. March"
year: "1996"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1996.11518106"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Influence of Database Structure Representation on Database System Learning and Use

Robert L. Leitheiser & Salvatore T. March

To cite this article: Robert L. Leitheiser & Salvatore T. March (1996) The Influence of Database Structure Representation on Database System Learning and Use, Journal of Management Information Systems, 12:4, 187-213, DOI: 10.1080/07421222.1996.11518106

To link to this article: http://dx.doi.org/10.1080/07421222.1996.11518106

![](/api/attachments/AFH8ZU6W/fulltext/images/51cd3a1340989fd5da2bf6fab2a16293314bf56223194f051e9dfb2a35ac347c.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/AFH8ZU6W/fulltext/images/63a41172986b5124f7ed0361397a1b2814f7029e94de757bffe2720ed14dcfb4.jpg)

Submit your article to this journal ↗

![](/api/attachments/AFH8ZU6W/fulltext/images/99254dfbd2f758b9df4074412fc69dfdf2c5a1e65bd1f7f144583ed11ca054b7.jpg)

View related articles ↗

![](/api/attachments/AFH8ZU6W/fulltext/images/288e74d9710bb2c3b773829dae0a09fe9d0c5a7a8f53a5706b360dbce8a771c1.jpg)

Citing articles: 12 View citing articles ↗

# The Influence of Database Structure Representation on Database System Learning and Use

ROBERT L. LEITHEISER AND SALVATORE T. MARCH

ROBERT L. LEITHEISER is an Associate Professor in the Management Department of the College of Business and Economics at the University of Wisconsin, Whitewater. Professor Leitheiser has a B.S. in industrial engineering and an M.B.A. He received a Ph.D. in management information systems from the University of Minnesota. His research has been in the areas of human factors, interface design, management of information systems, and end-user computing. Currently he is exploring business and academic applications of the World Wide Web. He has published in leading information systems journals including the Journal of Management Information Systems, MIS Quarterly, Information & Management, and Data Base.

SALVATORE T. MARCH is a Professor in the Information and Decision Sciences Department, Carlson School of Management, University of Minnesota. He received a B.S. in industrial engineering and M.S. and Ph.D. degrees in operations research from Cornell University. His primary research interests are information system development, logical and physical database design, and information resource management. His research has appeared in ACM Computing Surveys, ACM Transactions on Database Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, the Journal of Management Information Systems, and Information Systems Research. He has served as the Editor-in-Chief of ACM Computing Surveys and is currently an Associate Editor for MIS Quarterly.

ABSTRACT: Successful use of a computerized database by end users requires both an understanding of the structure of the database and knowledge of the available query language. Previous research has focused almost exclusively on query languages with little concern for how database structure is represented. This paper reports on an experiment that explores the influence of database structure representation on the ability of users to learn and use a database system. Four alternative representations of the same databases are developed and compared. These representations differ in semantics, symbols, and means of representing relationships. Interestingly, representation features that aid in communicating the contents of a database appear to hinder the learning of the SQL query language. We conclude that database representation is an important factor in database use and that the interaction between a database structure representation and a query language may dramatically affect database learning and use.

KEY WORDS AND PHRASES: database querying, entity-relationship model, relational model, human factors, interface design, SQL, training

AS FIRMS BECOME MORE EXPERIENCED WITH INFORMATION SYSTEMS they reach a point where managing data becomes more important than managing software [29]. Surveys of IS executives suggest that many firms have already reached this point (e.g., [4, 16, 28]). There is also substantial evidence that end users have come to rely increasingly on database applications (e.g., [34, 36, 45]). In order to get the most out of a firm's data resources, users need to know (1) what data are available to them and (2) how to access data that are of interest. The availability of data is communicated through the use of a representation of database structure. This structure details the stored data items and their logical organization. Access to data of interest requires knowledge of a database query language. This knowledge concerns not only the key words and the rules for their use, but also an understanding of how the commands relate to the database structure. Knowledge of query language syntax with partial or inaccurate understanding of database structure can lead to expensive end-user mistakes [13].

Given the importance of understanding database structure, it is surprising that more attention has not been given to improving the means of representing it to end users. The primary purpose of this study is to examine the influence of database structure representation on database system learning and use.

The paper begins with the presentation of a research model and a review of previous research. A description of the methodology of the current study follows and leads to a presentation and discussion of experimental results. The paper concludes with a summary and interpretation of the results as they apply to database system learning and use.

## Research Model

THE INFLUENCE DIAGRAM IN FIGURE 1 SHOWS THE ASSUMED and hypothesized relationships associated with this study. Data are stored in a computerized database managed by a database management system (DBMS). The DBMS has an underlying data model (e.g., relational, hierarchical, or network) and query language (e.g., SQL, DL/1, QBE) that define the static and dynamic properties of the database.

Static properties include the database structure—that is, the set of stored data items and their logical organization. A database representation is used to communicate database structure to users. Useful representations must cover the essential static properties of the underlying data model. The way these properties are depicted may vary. Ideally, representation syntax and semantics will be chosen that will comfortably communicate database contents to the target user group.

A query language is an implementation of the dynamic properties of a data model (e.g., commands used to update, delete, and retrieve data). A language is defined by its semantic and syntactic rules. The same underlying data model may be associated with multiple query languages (e.g., the relational model with SQL and QBE). The language's semantics and syntax should be designed to make information retrieval easy for the target user population. The semantics of the language (and perhaps the syntax) are typically communicated in terms of a specific database representation. For example, if the representation semantics are based on data being organized into tables, then the query language will be described as operations on rows and columns. If the representation semantics are based on entities and relationships, then the query language will be taught in these terms.

![](/api/attachments/AFH8ZU6W/fulltext/images/69ac10155d01a271c58aec0a5bdeff61d7d02a060461f4ef121f26747076285b.jpg)  
Figure 1. The Influence of Representation Characteristics on Representation and Query Language Learning and Use

User knowledge about job tasks and computers influences the effectiveness of database representations and query languages. Representations that rely on computer concepts are readily understood by users with significant computer experience but are alien to computer novices. Differences in computer knowledge also appear to influence the success of query languages (e.g., [18, 32]).

The effective use of a database means that users improve their job performance through an interaction with the database system. For business analysts this means better evaluations and recommendations, and for managers it means better decisions. Effective database use requires that users learn how to read and use database representations and that they learn how to query a database.

The current study focuses on the influences of database structure representation. Hypotheses are generated and tested to determine its role in representation learning and use (H1–H3) and on query language learning and use (H4–H6).

## Prior Research

[41], the method of teaching a query language [37], and/or the query language itself [18, 32, 38, 40, 42, 43], researchers attempted to determine how task, training, and language features affect language learning and use. While these studies furthered the development of powerful query languages, they contribute little to our understanding of the influence of representation features.

Several researchers varied the database representation as part of their language study. Lochovsky and Tsichritzis [23] compared the effectiveness of table, tree, and network database representations. They found some advantage to using table and network representations in a programming task but confounded the results by using a different language for each representation. Since languages that support the same representation may have very different features (e.g., QBE and SQL), there is no way of knowing how much of the observed effect is due to the representation.

Mayer [26] and Kenny et al. [21] performed studies where only the representation was varied while the language remained constant. Mayer used “concrete office objects” to describe the structure and processing of a database. The control group was presumably given the standard tabular representation. The office object representation resulted in improved comprehension of an SQL-like language.

In their experiment, Kenney et al. [21] compared querying performance of a group given an entity-relationship (E-R) representation with a group given a tabular representation. Both groups learned SQL. No significant differences were found in between the treatment groups. One interpretation of these results is that database representation has no influence on effective database use. Alternatively, it should be noted that the observed effects came from the combination of database representation and use of a specific query language (SQL). This study does not address what might happen if the query language was changed. It also does not answer the question of how much of the observed result is due to the representation and how much is due to SQL.

A recent study by Chan, Wei, and Siau [7] compared an entity-relationship representation to a table representation in a querying task. Each of the representations used its own language; KQL for E-R and SQL for tables. The researchers found that the KQL/E-R combination resulted in improved querying performance. This is an important study because, for the first time, a semantic representation resulted in higher performance than a tabular representation. Interpretation of the results is tricky, however, since representation and language are perfectly confounded. What would the result have been if QBE was used instead of SQL? In other words, is it the quality of the representation or the quality of the language implementation that produces the greatest effect on performance? In fact, KQL is significantly more powerful (e.g., support for inheritance relationships and powerful aggregation operators) than SQL.

In each of these latter studies, the characteristics of the language may overwhelm the effects of the representation. Studies by Brosey and Shneiderman [5] and Juhn and Naumann [20] avoid this problem by not using a query language and therefore directly address the effects of database representation on representation learning and use.

Brosey and Shneiderman [5] compared tree and table representations of the same data. Experimental tasks were defined that did not require a query language. The researchers found that tree representations were easier to recall and could be manually searched with fewer errors in retrieval. The authors argued that the reason for the superiority of tree representations over tables is that trees better fit the natural structure of the data. Differences in the method of representation for the schema (graphically for trees versus textual for tables) and the way relationships were indicated (explicitly with lines for trees versus implicitly for tables) may also have influenced the results.

Juhn and Naumann [20] compared the effects of four different database representations on representation learning and use. Subjects were given a database representation and answered questions about its structure. Two representations used semantic data modeling concepts and two used table concepts. The researchers found that users of the semantic representations had a better understanding of relationships but a poorer understanding of identifiers when compared with the table users. One of the table representations (data access diagram) explicitly represented relationships with arrows connecting foreign and primary keys. This additional information led to better understanding of relationships for table users (but still did not match that of the semantic groups).

Juhn and Naumann attempted to explore the effect of representation on information retrieval but did not collect sufficient data to perform an analysis. They state that this is unfortunate because “the database search strategy task is an important one both for user validation and as an indication of the utility of alternative representations in more general uses of data models” (p. 224). The current study takes up this challenge.

There has also been interest in studying the role of database representation in the design process. Studies by Ridjanovic [33], Jarvenpaa and Machesky [19], and Batra, Hoffer, and Bostrom [2, 3] have contrasted the use of E-R based representations with relational representations. Mantha [24] compared the use of E-R representations and data flow diagrams in generating data specifications for an application. These studies found that the E-R approach focused designer attention on relationships with the result that more relationships were identified by E-R users.

The design studies have only limited application to the current study, however, because the roles of the database representations are so different. In information retrieval the purpose of the representation is to communicate the contents and structure of the database while in database design its purpose is to determine content and structure. In the former case the representation user needs only to read and understand the representation while in the latter he or she needs to generate it. This distinction suggests that very different processes are involved in using the representation. The target user is also different. An end user may need to query a database but an IS professional is likely to be the database designer. There would be overlap if the design studies examined the process of bringing a database design to the user for review and validation, but this was not the case.

In summary, most prior research has either explored query language learning and use without regard to database representation, or has confounded database representation with query language features. Representation learning and use have been given little emphasis even though they are at the center of database use. The current study is designed to explore how features of database representations (1) influence representation learning and use, and (2) impact query language learning and use.

EMPLOYEE

<table><tr><td>EMP#</td><td>NAME</td><td>SALARY</td></tr><tr><td></td><td></td><td></td></tr></table>

Figure 2.

## Methodology

THIS STUDY INVESTIGATES THE EFFECTS OF USING ALTERNATIVE database representations on database and query language learning and use (see figure 1). The research design involved (1) designing treatments, (2) defining subjects, (3) generating hypotheses, (4) identifying measures, and (5) developing experimental procedures. Each of these elements of the methodology is addressed below.

## Research Treatments

Representations vary in what they represent (semantics) and in how they represent it (syntax). Database representations must contain the semantics to describe the logical structure of a database; that is, the contained data elements and their logical organization. One approach to semantics is to base a description on how data are stored. For example, a relational database is a database where the “data is perceived by the user as tables (and nothing but tables)” [14, p. 53]. An alternative is to describe data as being stored as a stack of data cards [26]. The use of storage concepts in database representations has become the norm.

An alternative to storage semantics is to use the structure of the “real world” to describe database structure. This has been done by describing a database as organized into sets of data that describe classes of things, people, or events (i.e., entities). In addition, relationships between entities in the world are also represented in the database. This approach has been popular for database design $[8]$ and is beginning to be applied to information retrieval $[7, 12, 17, 35]$ .

Representation syntax is the set of symbols used to depict database semantics and rules for using them. The same semantics may be represented in different ways. For example, each of the representations in figure 2 depicts the table EMPLOYEE with columns for EMP#, NAME, and SALARY. The first representation uses only text while the second uses graphical symbols and spatial position to suggest the “actual” organization of data. Representations incorporating entity semantics tend to be graphical but purely textual depictions may be devised.

This study explores the influence of different semantics and syntax on the effectiveness of database representations. Two types of semantics are compared: table and entity. Table semantics use storage constructs such as rows and columns. Relationships are implicitly represented by foreign keys. Entity semantics use logical or conceptual constructs such as entities, attributes, and relationships.

The Logical Data Structure, or LDS [6], is used to represent entity semantics. An LDS uses: (1) ovals to represent entities, (2) lines between ovals to depict relationships, and (3) lines attached to single ovals to indicate attributes (see appendix A). The “many” side of one to many relationships are represented by “chicken feet” (or “crows’ feet”). Primary identifiers for an entity are represented by single dots located on attribute and/or relationship lines. Secondary identifiers are indicated by multiple dots.

There are several reasons for using the LDS model instead of the E-R model for entity semantics. First, all attributes and identifiers are indicated in an LDS diagram. This is essential information for representation learning and use. Second, all relationships are binary (i.e., between two entities). Third, relationships may not be many to many and may not have attributes. New entities are created in the LDS to accommodate situations when an E-R diagram would use tertiary or higher relationships, many to many relationships, and relationships with attributes. In a traditional E-R diagram entities and some relationships map to relational tables. In the LDS all entities and only entities map to tables. Thus, the LDS enables a straightforward mapping to the query language constructs. Furthermore, it has been successfully used in previous research (e.g., [19, 20, 33]).

Representations of entity semantics usually use graphical symbols. In fact, Date $[14]$ has argued that graphical syntax may be the basis for their popularity. March, Carlis, and Flory $[25]$ claim that the graphical nature of the LDS approach helps users understand how to write queries correctly. To explore this claim, we include a graphical depiction for table semantics (see appendix B). This representation shows empty tables with names and column headings. It is similar to the table skeletons used in Query-By-Example $[45]$ and posited to help users conceptualize database operations $[39]$ . To test the effects of graphical depictions, we also include a representation that only uses textual symbols and a nonrepresentative spatial arrangement (see appendix D). The database description consists of a listing of column names within tables.

Previous research suggested our final representation variation. Brosey and Shneiderman [5] mention that the explicit representation of associations in their experiment may have given an advantage to their tree treatment group over their relational group. Juhn and Naumann [20] found that a table treatment with explicit representation of relationships produced results that were better than tables alone. Since the LDS explicitly represents relationships, we include a table representation with the same property. Arrows between tables indicate relationships explicitly in the final representation treatment (see appendix D). The many side of a relationship is depicted with double arrows. The resulting experimental treatments are summarized in Table 1.

Since we are more interested in the features of database representations than the actual treatments, a strategy of estimating contrasts among factor level means is employed [27].

## Subjects

Fifty-two graduate business students participated in this study. These students were felt to adequately represent the target population of business end users because (1)

Table 1. Experimental Treatments

<table><tr><td>Dimension</td><td>LDS</td><td>Table</td><td>Table/arrows</td><td>Table/text</td></tr><tr><td>Semantics</td><td>entity</td><td>table</td><td>table</td><td>table</td></tr><tr><td>Symbols</td><td>text &amp; graphics</td><td>text &amp; graphics</td><td>text &amp; graphics</td><td>text only</td></tr><tr><td>Relationships</td><td>explicit</td><td>implicit</td><td>explicit</td><td>implicit</td></tr></table>

they were being educated for business positions, (2) most had business experience, and (3) many were currently employed as business professionals. In addition, the experiment did not require business or computer experience. Finally, it should be pointed out that many previous studies have successfully used student subjects (e.g., [5, 26, 40, 43]).

Subjects were randomly assigned to one of the four treatment groups. Only one subject failed to complete the experiment and was replaced by another equivalent student. A summary of subject characteristics for each treatment is given in Table 2. An ANOVA analysis was performed for differences among treatments for gender, age, prior computer experience (1 = low, 6 = high), and mean scores for a spatial relations test. No statistically significant differences were found. The spatial relations test was performed to insure that differences in spatial ability would not bias graphical treatments. None of the subjects had any knowledge of SQL or had any significant prior experience using a database management system.

## Hypotheses

The goal of this research is to investigate the influence of database representation characteristics on representation and query language learning and use (see figure 1). Other factors will be held constant (i.e., underlying data model and query language) or will be randomized (user knowledge). The influence of Representation Learning on Query Language Learning is controlled by ensuring that subjects achieve the same minimum level of competency in their treatment representations.

The underlying data model for all treatments is the relational model $[10]$ . This model was chosen because it has become the most important model for end users $[14]$ . A single query language, SQL, was used for all treatments. The advantage of this is that the effects of changes in language and representation are not confounded. The disadvantage is that the chosen language may be biased toward one or more of the representations. The research design attempted to separate the effects on representation learning and use from those on query language learning and use.

SQL was chosen for the experiment for several reasons. First, the language has become very popular and runs on many computer platforms $[14, 15]$ . In fact, at the time of the study, SQL was the only relational database language that had become a national standard $[1]$ . Second, significant development and research have gone into the language including research with similar subjects (e.g., $[18, 26, 32, 37, 40, 43]$ ). Finally, and most important, the syntax of the language did not suggest an obvious representation bias. Query-by-Example [45], by contrast, is strongly tied to a database representation through its use of graphical tabular representations. SQL is a linear keyword language that (1) makes no direct reference to table or entity concepts in information retrieval queries, and (2) may be used with either graphical or textual representations. SQL does, however, make use of implicit relationship representations. Trial runs of the experiment convinced us that LDS could be successfully used to teach SQL. Given the decision to use a single language, SQL was the obvious choice.

Table 2. Characteristics of Experimental Subjects

<table><tr><td>Dimension</td><td>LDS</td><td>Table</td><td>Table/arrows</td><td>Table/text</td></tr><tr><td>Percent female</td><td>46%</td><td>54%</td><td>38%</td><td>38%</td></tr><tr><td>Mean age</td><td>28</td><td>32</td><td>29</td><td>28</td></tr><tr><td>Computer experience</td><td>4.9</td><td>4.3</td><td>4.8</td><td>4.9</td></tr><tr><td>Spatial relations score</td><td>30</td><td>31</td><td>29</td><td>32</td></tr></table>

In this study, database representations are distinguished by their semantics, symbols, and representations of relationships. Hypotheses were generated to guide the design and analysis of the experiment (see figure 1). Three hypotheses (stated in null form) were posited for representation learning and use (H1–H3) and three were proposed for query language learning and use (H4–H6).

Hypothesis 1 concerns the use of representation semantics. It is expected that the use of entity semantics will make it easier and more natural for users to interpret and understand a database representation. Users will not be forced to convert their understanding of task domain concepts (e.g., employees, departments, dependents) into storage concepts (e.g., tables). To insure that this treatment does not gain its advantage from the use of graphical symbols or the explicit representation of relationships, two other comparisons are made. Representations with graphical symbols will be compared with the text-only representation, and the two representations with explicit relationship representations will be compared with those that are implicit. It is expected that the graphical symbols will enhance conceptualization of the data structure and will lead to improved representation learning and use (H2). It is also expected that explicit representation of relationships will aid in recognizing and understanding relationships in the database structure which will assist learning and use (H3).

H1: Differences in the semantics of database representations have no influence on the learning and use of representation approaches.

H2: Differences in the symbols used in database representations have no influence on the learning and use of representation approaches.

H3: Differences in the way relationships are represented have no influence on the learning and use of representation approaches.

Three more hypotheses were generated for query language learning and use. It is expected that where a user can relate a query operation easily to the task that is being addressed (e.g., analyzing employee performance), he or she will more easily formulate the correct query. The user should also be better able to define a solution strategy in terms of data contained in the database. These points favor entity semantics (H4). It should be mentioned out, however, that counterarguments exist. Familiarity with table concepts from prior experience may provide an advantage for representations based on tables.

Graphical symbols provide help in visualizing objects, relationships, and operations. Extracting rows from a table or moving across relationships in an LDS may be imagined more easily if the involved elements are pictured. It is expected that independent of semantics, the representations with graphical symbols will result in improved query language learning and use (H5). Finally, the explicit representation of relationships is viewed as helpful for guiding subjects when they must do queries that join multiple relational tables (H6). Since these are an important class of queries, the benefit should be substantial.

H4: Differences in the semantics of database representations have no influence on the learning and use of a query language.

H5: Differences in the symbols used in database representations have no influence on the learning and use of a query language.

H6: Differences in the way relationships are represented have no influence on the learning and use of a query language.

Tests of these six hypotheses are operationalized below.

## Measures

Measures of representation and query language learning and use must be defined in order to test the six hypotheses. Reisner [31] presented a list of standard experimental tasks for database research that included query writing, query reading, memorization, and problem solving. Juhn and Naumann [20] added a set of comprehension questions to this list. Tasks and measures are summarized in Table 3.

Query writing, query reading, and query generation to solve a problem all require knowledge of database representation and a query language. These tasks, therefore, measure learning and/or use of both representations and query languages. The memorization and question generation tasks do not require knowledge of a query language and may be used to explore the influences of database representation without the confounding influence of a specific language. Since a database representation is required by users who perform queries, it is not possible to isolate query language effects. By examining database representation by itself first and then adding the query language component, we hope to evaluate the separate influences of representation characteristics on representation learning/use and query language learning/use.

To assess representation learning, we adapt Juhn and Naumann's [20] use of questions about the meaning of database representations to measure comprehension of specific elements of the database. The time required to demonstrate a given level of comprehension with these questions is the basic representation learning measure. As a final measure of understanding, we ask subjects to determine whether a given English question (representation use) or query (query language use) may be answered by using data from the represented database. All questions and queries were syntactically correct but some could not be answered with the represented database.

Table 3. Experimental Tasks and Measures

<table><tr><td>Task</td><td>Description</td><td>Measure</td></tr><tr><td>Query writing [31]</td><td>Write a query to answer an English language question</td><td>No. of correct queries</td></tr><tr><td>Query reading [31]</td><td>Write sentences to explain queries</td><td>No. of correct interpretations</td></tr><tr><td>Memorization [31]</td><td>Memorize and reproduce database representations</td><td>Amount of representation recalled</td></tr><tr><td>Problem solving [31]</td><td>Write questions and/or queries that would help solve a business problem</td><td>No. of valid and invalid questions or queries</td></tr><tr><td>Representation comprehension [21]</td><td>Answer questions about the meaning of components of database representation</td><td>No. of correct answers</td></tr><tr><td>Question/query evaluations</td><td>Evaluate whether a question or query can be answered with given database</td><td>No. of correct evaluations</td></tr></table>

## Experimental Procedures

Our attempt to separate effects on representation learning/use from effects on query language learning/use resulted in a lengthy and complicated experiment. Since representation learning/use is essential to using a query language, it is addressed in the first stage of the experiment. The second stage introduces the query language. Each stage, in turn, is broken down into two phases: a learning phase and a use phase. A learning phase was necessary because subjects had no specific knowledge about how to read database representations or how to query a database. Subjects participated in the learning phase until they demonstrated a predetermined level of comprehension (i.e., they could read representations or they could write SQL queries). Once this level was achieved, subjects entered the “use” phase. In this phase, they performed three different tasks requiring the use of representation and/or query language knowledge gained earlier in the experiment.

To provide flexibility for different speeds of learning and to create a realistic computing environment, personal computers were used to oversee each subject's participation. Software was developed to provide instructions and to present training items with feedback. The software also captured responses and tracked response times.

Table 4. Experimental Procedures

<table><tr><td rowspan="3" colspan="2"></td><td colspan="4">Experimental stages</td></tr><tr><td colspan="2">Representation</td><td colspan="2">Query</td></tr><tr><td>Reading</td><td>Practice</td><td>Reading</td><td>Practice</td></tr><tr><td rowspan="2">Phases</td><td>Learning</td><td>Read printed material describing how to interpret representation</td><td>Answer multiple choice questions about 2 specific databases until criterion reached</td><td>Read printed description of an SQL query type—repeated for each type</td><td>Write SQL queries to answer English questions until criterion reached for each type</td></tr><tr><td>Use</td><td colspan="2">For two new databases:memorization taskproblem-solving taskquestion evaluation task</td><td colspan="2">For two new databases:problem solving taskquery writing taskquery evaluation task</td></tr></table>

Table 4 summarizes the experimental procedures. For more details about tasks, procedures, and the experimental software see [22].

In the representation learning and use learning phase, subjects were given printed material that explained how to read and interpret a representation of a five-entity/table database. The material also described the types of questions that could be answered with the database. The text used for the treatments was as similar as possible while still being true to the details of the different approaches.

When subjects felt comfortable with the representation descriptions, they moved on to the practice part of the learning phase. Participants were given a representation of a new database and asked a series of multiple-choice questions designed to test their understanding of the database's structure. An indication of the correct answer was fed back to participants after each response. Most questions concerned the recognition of elements in the database structure. These questions were ordered according to underlying representation concepts. Questions about more basic elements (i.e., tables/entities, columns/attributes) appeared first and more difficult elements followed (i.e., foreign keys/relationships, primary keys/identifiers). When a subject had demonstrated competency with a particular concept by answering three consecutive questions correctly, he or she moved on to the next concept. Questions within concept groupings were generated and randomized into a single ordered set for all subjects. A final set of questions asked subjects to apply “real-world” interpretations to the described database (e.g., can two people have the same savings account?). After demonstrating competency with one database, the subject repeated the process with a second database to insure that their knowledge was transferable across target databases. The primary measure was the time required to achieve the learning criterion for both databases.

Following the learning phase, participants were given three new tasks to complete on two more databases. The first task was memorization, the second was problem solving, and the third required subjects to determine whether a question could be answered with data contained in the database (based on its structure).

For the memorization task, subjects were told to study a database representation for a fixed time and then to reproduce as much of it as they could from memory. Brosey and Shneiderman [5] argue that recall is a good measure of comprehension for data structures and programs. It was used in this study as a measure of influence on representation use. After the memorization task, subjects were allowed to use the previously presented representation to generate English questions that could be answered with the described database. The purpose of the questions was to solve a business problem. For example, subjects were asked to write questions for a university database that would help identify students who were deserving of a special scholarship. Questions generated to solve the management problem were categorized as valid (could be answered by using the database), invalid (could not be answered by using the database), or redundant (essentially the same as a previous question). When subjects had finished writing down questions, they moved on to the final task where they were asked to determine if a set of questions could be answered by using the given database. The results for both databases were combined into a single score for each task.

The language comprehension stage began with a short printed description of query languages in general and then proceeded to separate learning units for each of eight standard query types (see appendix E, based on [30, 43]). Each query type was described in text and by example. Descriptions were based on the previously learned representation syntax and semantics. A single database was used for all learning units. After they had read the printed material, subjects were given a sequence of English questions and asked to enter the shortest SQL query that would answer the question. The computer parsed the entered query and compared it with a set of acceptable answers. If no match was found, a correct answer was presented and highlighting was used to indicate where an error may have occurred. If the query was correct, the subject was informed of this result. After reviewing the system response, the subject went on to the next query. Query items were developed in sets of three to try to encompass a range of options within a single query type (e.g., use of OR or AND within the selection expression). A single randomized list of query items was given to all subjects. Previous research suggests [30] that the wording of the English questions has much to do with errors observed in query writing experiments. To minimize this problem, a formal process was used to convert target queries into English questions. This process is similar to Reisner's Transformation Grammar [30] but was performed in reverse by defining transformation rules that replaced SQL syntax with English syntax. A predetermined level of competency was established as entering two out of three queries correctly in a given item set for each query type. This level was judged to be high enough to rule out completion based on luck, but at the same time low enough to keep the process from becoming too tedious. The times spent reading the textual descriptions and the times spent practicing queries were captured by the system as the primary experimental measures.

Following the completion of the language learning phase, subjects were given three tasks to perform on each of two new databases. The first task was a problem-solving task that asked subjects to write down queries that would help them solve a given business problem (similar to the question generation task in the representation learning/use stage). The second task was a query writing task that was similar to the task used in the training phase but that provided no feedback and was of fixed length. The third task was a query evaluation task that asked subjects to determine whether a syntactically correct query could be run against the given database (similar to the question evaluation task in the representation learning/use stage).

When the experiment was piloted, it became clear that more than one session would be needed. The final design used two sessions, placed one week apart. In session one, the representation learning/use stage was completed and query language training was completed through the first four query types. The final four query types and the query language “use” phase were completed in the second session. Due to the time delay between sessions, a short review preceded the second session. For this review, each subject performed a self-scored review exercise and was told to take time to refamiliarize him or herself with previously learned queries. Subjects made up their own minds about how much review was necessary. Subjects worked at their own pace and could take short breaks at predetermined points in the computer-controlled session. The times for these breaks were not included in the experimental times. Subjects required three to six hours for each of the two sessions.

## Results and Discussion

THE HYPOTHESES WERE TESTED BY CONTRASTING COMBINATIONS of treatments that had the same characteristic (see Table 5). For example, the hypotheses concerning database semantics (i.e., H1 and H4) are tested by contrasting the LDS treatment representing entity semantics to the combined table treatments (i.e., Table, Table/Arrows, and Table/Text).

The contrasts are developed by first doing ANOVAs and then performing post hoc tests where the ANOVA indicates a difference among treatments. The post hoc tests involve performance of three t-tests on the differences between the three pairs of contrast groups. A Bonferroni confidence level of 0.05 is held for each set of three contrasts to reduce the chance of spurious results. An individual contrast that achieves a t-test level of 0.05 but fails to reach the Bonferroni level (0.05/3 = 0.017) will be labeled as suggestive rather than significant.

## Representation Learning and Use

The overall learning times for each treatment and the breakdowns in times by representation concept are given in appendix F. The means of the treatments that make up the contrasts are reported in Table 6.

Hypothesis 1 states that differences in representation semantics have no influence on representation learning and use. Support for rejecting this hypothesis is found in the first phase of the experiment. It took the entity group significantly less time to learn how to read database representations than it took the table groups (F = 11.04; p =

Table 5. Experimental Contrasts

<table><tr><td>Contrasts</td><td>Treatments</td><td>Hypotheses</td></tr><tr><td>Semantics</td><td>LDS vs. table, table/arrows, table/text</td><td>H1, H4</td></tr><tr><td>Symbols</td><td>LDS, table, table/arrows vs. table text</td><td>H2, H5</td></tr><tr><td>Relationships</td><td>LDS, table/arrows vs. table, table/text</td><td>H3, H6</td></tr></table>

Table 6. Representation Learning Times (seconds)

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Reading time</td><td>2,032</td><td>2,492</td><td>2,325</td><td>2,534</td><td>3,387</td><td>2,467</td></tr><tr><td>Practice time</td><td> $2,300^{**}$ </td><td> $3,609^{**}$ </td><td>3,293</td><td>3,248</td><td> $2,843^{**}$ </td><td>3,731</td></tr><tr><td>Total time</td><td> $4,332^{**}$ </td><td> $6,101^{**}$ </td><td>5,617</td><td>5,782</td><td> $5,119^*$ </td><td> $6,198^*$ </td></tr></table>

\* Suggestive difference; $p < {0.05}$ ; \*\* significant difference; $p < {0.017}$ ; Bonferroni group $p < {0.05}$ .

0.002). This advantage was not due to differences in the time required to read the materials (reading time) but was the result of less time being required to enter the number of correct interpretations (practice time: F = 9.822; p = 0.003).

Hypothesis 2 states that differences in symbols used in database representations will not influence representation learning and use. No evidence in the learning phase was discovered to refute this hypothesis. The difference between graphical and text-only groups was not significant (F = 0.095).

Hypothesis 3 states that differences in the way relationships are represented have no influence on representation learning and use. There is some evidence to reject this hypothesis and conclude that explicit representation makes a difference. Specifically, there is a suggestive difference $F = 5.474; p = 0.024$ in favor of the explicit groups for the overall learning times and a significant difference $F = 6.182; p = 0.016$ if only practice times are considered. Since reading times are likely to be more a function of individual reading speed and text length than of representation characteristics, we feel that the practice times better reflect learning differences than total times. Therefore, we reject hypothesis 3 and conclude that relationship representation does influence representation learning and use.

To further understand the source of the significant differences, practice times were broken down into the times required to achieve competency for each of the primary representation concepts (see Table 7).

The results in Table 7 suggest that the significant differences found between entity and table groups and between explicit and implicit representation groups were primarily the result of learning the relationship/foreign key concept. It is not surprising that the emphasis that entity based representations place on relationships leads to reduced learning times $(F = 15.413; p < 0.001)$ when compared with the table approach of using foreign keys. It is also to be expected that by explicitly representing relationships, some advantage can be gained even when table concepts are used. An interesting finding that was hidden in the aggregated times is that the entity group took significantly longer to learn the identifier concept than the table groups took to learn about primary keys $(F = 14.265; p < 0.001)$ . On reflection, this advantage for table semantics makes sense because the identifier is a somewhat awkward construct in entity based representations. The initial E-R diagrams [8] did not include the concept. In the LDS representation, understanding identifiers requires an understanding of how combinations of attributes and/or relationships can uniquely identify an instance of an entity. This is made more difficult because instances are not themselves directly represented in LDS diagrams. In a table representation, one need only understand how values in one or more column may uniquely identify table rows. This is apparently a much easier task for subjects.

Table 7. Breakdown of Representation Learning and Use Learning Times (seconds)

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Entity/table</td><td>141</td><td>182</td><td>169</td><td>180</td><td>159</td><td>185</td></tr><tr><td>Attribute/column</td><td>141..</td><td>173..</td><td>176</td><td>133</td><td>150..</td><td>181..</td></tr><tr><td>Relationship/f. key</td><td>306..</td><td>1,343..</td><td>1,009</td><td>1,308</td><td>683</td><td>1,485</td></tr><tr><td>Identifier/p. key</td><td>483</td><td>249</td><td>341</td><td>208</td><td>339</td><td>277</td></tr><tr><td>Interpretation</td><td>1,230</td><td>1,662</td><td>1,599</td><td>1,420</td><td>1,503</td><td>1,605</td></tr></table>

\* Suggestive difference: $p < {0.05}$ ; \*\* significant difference: $p < {0.017}$ ; Bonferroni group $p < {0.05}$ .

Further tests of the representation learning and use hypotheses were based on the application phase of the database representation stage of the study. The results of the three experimental tasks for the contrast groups are reported in Table 8 (see appendix F for treatment means).

Hypothesis 1 stated that representation semantics did not influence representation learning and use. If the total number of recalled database elements is treated as the outcome measure, there is no support for rejecting hypothesis 1 (F = 3.472; p = 0.069). It might also be argued that some database elements are more important than others. In particular, since entities/tables and their relationships define the overall structure of the database, they might be considered more critical to representation use. An analysis of classified elements showed that the entity representation group recalled more entities (F = 10.261; p = 0.002) and more relationships (F = 11.842; p = 0.001) than the table groups recalled tables and foreign keys. While the evidence is not as direct as we originally hoped, it provides weak support for rejecting hypothesis 1. No additional support is provided by either the question generation task or the question evaluation task because they produced no significant differences.

No significant or suggestive differences were produced by the symbol or relationship contrasts for any of the application tasks. Therefore, no evidence resulted from this phase that could be used to reject hypotheses 2 or 3.

Table 8. Database Representation Use Tasks

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Entity recall</td><td>18.1**</td><td>14.6</td><td>15.3</td><td>16.2</td><td>16</td><td>15</td></tr><tr><td>Attribute recall</td><td>18.5**</td><td>18**</td><td>17.6</td><td>19.6</td><td>17.1</td><td>19.2</td></tr><tr><td>Relationship recall</td><td>8.6</td><td>3.7</td><td>4.7</td><td>5.7</td><td>5.4</td><td>4.5</td></tr><tr><td>Total recall</td><td>45.2</td><td>36.3</td><td>37.6</td><td>41.5</td><td>38.5</td><td>38.7</td></tr><tr><td>Valid questions</td><td>10.9</td><td>10.6</td><td>11</td><td>9.7</td><td>11</td><td>10.3</td></tr><tr><td>Invalid questions</td><td>1</td><td>2.2</td><td>2.1</td><td>1.4</td><td>1.5</td><td>2.4</td></tr><tr><td>Correct evaluations</td><td>19.9</td><td>20.8</td><td>20.6</td><td>20.4</td><td>20.1</td><td>21.1</td></tr></table>

\* Suggestive difference: $p < {0.05}$ ; \*\* significant difference: $p < {0.017}$ ; Bonferroni group $p < {0.05}$ .

In summary, measures of learning time, representation recall, question generation, and question evaluation were made for the purposes of testing hypotheses 1–3. Evidence was found in the learning time and recall data to reject hypothesis 1 (representation semantics have no influence on representation learning and use). Evidence was also found in the learning times to reject hypothesis 3 (explicit representation of relationships do not influence representation learning and use). No evidence was found to reject hypothesis 2 (representation symbols do not influence representation learning and use).

## Query Language Learning and Use

The second stage of the experiment examined the influence of representation semantics, symbols, and relationship representation on query language learning and use. Subjects were first taught eight basic query types and then they applied this knowledge to the performance of three querying tasks. The results of the query training for each of the contrasted groups are shown in Table 9 (see appendix G for treatment means).

Hypothesis 4 states that differences in representation semantics do not influence query language learning and use. There is suggestive evidence that the entity group took longer to learn SQL than the table groups (F = 4.726; p = 0.035). This difference becomes significant after the relatively constant reading times are removed (F = 8.233; p = 0.006). We take this as support for rejecting the hypothesis and concluding that representation semantics do influence query language learning and use. The finding that table semantics result in superior learning when compared with entity semantics was unexpected. It may be, as Codd [11] has argued, that when compared with entity-based representations, tables provide a more powerful way for users to conceptualize database operations. By using rows, table-based representations provide a means for depicting occurrences of data. An equivalent representation does not exist for Logical Data Structures or other common E-R approaches.

Or it may be that the specific language used in the study, SQL, is highly biased toward tabular representations. The possibility is given some credence when the results of the current study are compared with those of two related studies. If the representation and query language parts of this study were combined, the overall findings might very well show no advantage to either semantic group because the advantages in each experimental stage would offset the other. This finding would match that of Kenney et al. [21], who also compared semantics and used SQL but found no significant differences. On the other hand, if a language was used for the entity group that was not biased against it, the same advantage demonstrated by Chan et al. [7] would likely be observed. We caution that this is only speculation, however. It is dangerous to compare results from different studies (see [31]), and while this study contributes to our understanding of representation/query language interaction, further research is needed to disentangle their separate influences.

Table 9. Query Language Learning Times (seconds)

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Reading time</td><td>4,395..</td><td>5,001..</td><td>14,849..</td><td>4,851..</td><td>4,931..</td><td>4,769..</td></tr><tr><td>Practice time</td><td>9,479.</td><td>6,319.</td><td>7,823.</td><td>4,965.</td><td>8,397..</td><td>5,821..</td></tr><tr><td>Total time</td><td>13,874</td><td>11,320</td><td>12,673</td><td>9,816</td><td>13,328</td><td>10,590</td></tr></table>

\* Suggestive difference: $p < {0.05}$ ; \*\* significant difference: $p < {0.017}$ ; Bonferroni group $p < {0.05}$ .

To further explore the source of differences between contrast groups, the practice times for each query were broken out (Table 10). On the basis of the previous argument, we might expect queries that primarily define operations on rows to be helped the most by the table semantics. Supporting this supposition was a suggestive difference for simple selection queries ( $F = 5.627$ ; $p = 0.022$ ) and significant differences for union ( $F = 21.098$ ; $p < 0.001$ ) and join ( $F = 6.446$ ; $p = 0.014$ ) queries. No statistical differences were found for other queries that should benefit from row conceptualization (e.g., Boolean selection, group by, or order by). On the other hand, a suggestive difference was found for the projection query ( $F = 4.983$ ; $p = 0.030$ ), which does not involve the specification of rows. These results neither support nor refute the claim that row conceptualization is the basis for the table advantage. This is still an open question.

Hypothesis 5 states that differences in symbols used in database representations have no influence on the learning and use of a query language. There was suggestive evidence that the graphical groups required more time than the text only group (F = 4.726; p = 0.019). When the relatively constant reading times were removed, there was a significant advantage for the text only group (F = 6.737; p = 0.012). This is taken as support for rejecting the null hypothesis and concluding that representation symbols do influence query language learning and use. Surprisingly, this influence is in the opposite direction to what was expected. Once users have been trained to read text-only representations, it appears to be relatively easy for them to use these representations when learning the SQL query language. The reasons for this advantage are not clear. It may be that the economy of symbols used in this representation has some advantages when it is used to support querying. An examination of differences in practice times for specific query times (Table 10) even reveals a suggestive difference favoring the text only treatment for join queries (F = 4.498; p = 0.039). Even on the hardest of queries, subjects were not helped by graphical symbols.

Table 10. Query Type Practice Times (seconds)

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Projection</td><td>677.</td><td>458.</td><td>556</td><td>385</td><td>614..</td><td>412..</td></tr><tr><td>Simple selection</td><td>1,761</td><td>1,002</td><td>1,350</td><td>716</td><td>1,559</td><td>824</td></tr><tr><td>Boolean selection</td><td>712</td><td>518</td><td>616</td><td>418</td><td>629</td><td>504</td></tr><tr><td>Built-in function</td><td>434</td><td>414</td><td>448</td><td>333</td><td>471</td><td>368</td></tr><tr><td>Group by</td><td>1,532</td><td>1,351</td><td>1,453</td><td>1,228</td><td>1,547</td><td>1,247</td></tr><tr><td>Order by</td><td>1,255..</td><td>945..</td><td>1,171</td><td>577</td><td>1,242.</td><td>803.</td></tr><tr><td>Union</td><td>1,102..</td><td>510..</td><td>723.</td><td>461.</td><td>808</td><td>508</td></tr><tr><td>Join</td><td>2,005</td><td>1,121</td><td>1,507</td><td>846</td><td>1,527</td><td>1,157</td></tr></table>

\* Suggestive difference: $p < 0.05$ ; \*\* significant difference: $p < 0.017$ ; Bonferroni group $p < 0.05$ .

Hypothesis 6 states that differences in the way relationships are represented have no influence on the learning and use of query languages. There is evidence in the overall times $(F = 7.241; p = 0.010)$ and the training times $(F = 7.292; p = 0.010)$ to support the rejection of the null hypothesis and conclude that relationship representation does affect language learning and use. This effect, however, is in the opposite direction to what was expected. Subjects with implicit relationship representations took less time to learn SQL than subjects with explicit representations (i.e., lines or arrows). One obvious disadvantage of the explicit relationships is the additional clutter they bring to the database representation. Since the additional information provided by the lines or arrows is only important for join queries, it may only get in the way for the other seven query types. In fact, no suggestive or significant difference was found for the relationship contrast for join queries (Table 10) but important differences were found for projection $(F = 5.648; p = 0.022)$ , selection $(F = 7.030; p = 0.011)$ , and union $(F = 5.929; p = 0.019)$ queries. It should be remembered that subjects in the implicit group had already invested the time required to learn how to successfully read the implicit relationships. It appears that once this competency has been achieved, there is no benefit to providing explicit representations of relationships.

The results of the application phase of the query language learning and use stage are reported in Table 11. Hypothesis 4 concerned the influence of representation semantics. No statistical advantage was found in the query generation task but the table semantics groups outperformed the entity semantics group on both the query writing $F=6.745;p=0.015$ and query evaluation $F=56.301;p<0.001$ tasks. These results are in line with the query learning data and provide further evidence for the rejection of hypothesis 4. It appears that differences in representation semantics do influence query language learning and use.

Table 11. Query Language Use

<table><tr><td rowspan="2">Measure</td><td colspan="2">Semantics</td><td colspan="2">Symbols</td><td colspan="2">Relationships</td></tr><tr><td>Entity</td><td>Table</td><td>Graphical</td><td>Text only</td><td>Explicit</td><td>Implicit</td></tr><tr><td>Valid queries</td><td>5.3</td><td>7.2</td><td>6.3</td><td>8.1</td><td>6.4</td><td>7.2</td></tr><tr><td>Invalid queries</td><td>4.8..</td><td>3.6..</td><td>3.9</td><td>3.9</td><td>4.3</td><td>3.5</td></tr><tr><td>Correct queries</td><td>8.3..</td><td>11.4</td><td>10.1.</td><td>12.4.</td><td>9.7..</td><td>11.6..</td></tr><tr><td>Correct evaluations</td><td>17.9</td><td>20.</td><td>19.9</td><td>20.8</td><td>19.7</td><td>20.7</td></tr></table>

\* Suggestive difference: $p < {0.05}$ ; \*\* significant difference: $p < {0.017}$ ; Bonferroni group $p < {0.05}$ .

Hypothesis 5 posited that differences in symbols influence query language learning and use. No differences were found in the query generation or writing tasks. A suggestive difference favoring the text-only group (F = 4.285; p = 0.044) was found for the query evaluation task. By themselves, these results do not support the rejection of hypothesis 5, but when combined with the query learning results, there is weak evidence to support a rejection of the null hypothesis. Differences in symbols probably influence query language learning and use.

Hypothesis 6 states that the way relationships are represented does not influence query language learning and use. The query generation and query writing tasks provide no support for rejecting the null hypothesis. A significant difference in query evaluations (F = 8.485; p = 0.015), however, favors rejection. When this finding is combined with that for query learning, a relatively strong rejection of hypothesis 6 is possible. The way relationships are represented does appear to influence query language learning and use.

## Conclusions

THIS STUDY EXPLORES THE INFLUENCE OF DATABASE REPRESENTATION characteristics on representation and query language learning and use. Six hypotheses based on three representation dimensions were proposed to guide this exploration. A summary of findings for representation hypotheses is given in Table 12.

Evidence was found to reject hypothesis 1 and conclude that the semantics of database representation influences representation learning and use. In particular, entity semantics improved representation learning/use when compared with table semantics. This result provides support for using entity semantics when describing databases to end users. There may be limits to this influence, however, since neither the question generation nor question evaluation task provided additional supporting evidence.

No evidence was found to reject hypothesis 2. It cannot be concluded that differences in symbols influence database representation learning and use. Perhaps Date [14] is right in speculating that E-R popularity is largely due to its graphical nature. We can find no evidence, however, that this “nature” improves representation learning and use.

Some evidence was found to reject hypothesis 3. Specifically, practice times were significantly shortened for the groups with explicit relationships. This result is in line with Juhn and Naumann's [20] finding that Data Access Diagrams had an advantage over standard relational tables. There appears to be some benefit to explicitly representing relationships when communicating database structure to users.

Table 12. Representation Learning and Use Hypotheses Results

<table><tr><td>Measure</td><td>H1: semantics</td><td>H2: symbols</td><td>H3: relationships</td></tr><tr><td>Reading time</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Practice time</td><td>entity &lt; table</td><td>n.s.</td><td>explicit &lt; implicit</td></tr><tr><td>Total learning time</td><td>entity &lt; table</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Entity/table recall</td><td>entity &gt; table</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Attribute/column recall</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Relationship/f. key recall</td><td>entity &gt; table</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Valid questions</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Invalid questions</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Correct evaluations</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr></table>

n.s.: not significant at Bonferroni group level of p < 0.05.

Table 13. Query Language Learning and Use Hypotheses Results

<table><tr><td>Measure</td><td>H4: semantics</td><td>H5: symbols</td><td>H6: relationships</td></tr><tr><td>Reading time</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Practice time</td><td>entity &gt; table</td><td>graph &gt; text only</td><td>explicit &gt; implicit</td></tr><tr><td>Total learning time</td><td>n.s.</td><td>n.s.</td><td>explicit &gt; implicit</td></tr><tr><td>Valid queries</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Invalid queries</td><td>n.s.</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Correct queries</td><td>entity &lt; table</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Correct evaluations</td><td>entity &lt; table</td><td>n.s.</td><td>explicit &lt; implicit</td></tr></table>

n.s.: not significant at Bonferroni group level of p < 0.05.

The results for the hypotheses related to query language learning and use are summarized in Table 13. In this case, there is some evidence to reject each of the null hypotheses 4–6, but the differences are in the opposite direction than expected.

The evidence for rejecting hypothesis 4 suggests that entity semantics make query language learning and use more difficult than it is with table semantics. This finding is especially interesting because of the advantage entity semantics displayed in representation learning and use. Possible explanations include an advantage due to the use of the row concept in tables and a strong bias in the target query language (SQL). More research is needed to distinguish among these possibilities. It may be possible to eliminate this disadvantage for entity semantics by using a language that is specifically based on E-R representations.

Evidence was found that graphical symbols retard query language learning (reject H5). When combined with the representation learning and use results, we must conclude that graphics did not help in training database users or in helping them to use the system. This result is troubling because significant expense is incurred to put graphics into training materials as well as to include graphical database representations in user interfaces. While we personally feel that graphical representations can be useful in certain training and interface situations, we also urge caution and suggest that the cost of including graphics be carefully considered against the unproven benefits.

Finally, evidence exists to reject hypothesis 6 and conclude that the explicit representation of relationships negatively impacts query language learning and use. This result occurred in spite of a demonstrated benefit to explicit representations in the database representation stage.

The focus of this study has been on features of representations rather than specific representations. The relative merits of LDS versus E-R diagrams are less important than the fact that entity semantics are better or worse than table semantics. We believe that the results have some application to other representation approaches. The object-oriented approaches to modeling databases offer new (but related) semantics. They also typically (e.g., [9]) involve graphical symbols and explicit representation of relationships. Our findings suggest that any advantage object-oriented representations provide to database users will come from the semantics used rather than from the proposed symbolic notation. Confirmation of this claim is an exciting new area of research.

The primary goal of this study was to show that database representations should be considered in research and practice. Our findings suggest that previous studies have missed an important variable by failing to consider the way database structure is presented to users. A secondary goal was to explore the influence of three specific representation dimensions on database and query language learning and use. Varying degrees of evidence were found linking representation semantics, symbols, and relationship representation to database and query language learning and use. Finally, we wished to explore the research problems associated with the interaction of database representations and query languages. The results discussed here clearly show that database representations that are beneficial to users trying to understand the contents of a database, may be a problem when they learn a specific query language. Understanding the separate influences of representation characteristics and query language features on database use will help guide efforts to improve both representations and languages.

## REFERENCES

1. ANSI, American National Standards Institute. Database Language SQL2. ANSI X3H2-89-001, (ISO DBL SYD-2a), October 1988.

2. Batra, D.; Hoffer, J.; and Bostrom, R. A comparison of user performance between the relational and the Extended Entity Relationship models in the discovery phase of database design. In Proceedings of the Ninth International Conference on Information Systems, Minneapolis, November 30 – December 3, 1988, pp. 295–308.

3. Batra, D.; Hoffer, J.; and Bostrom, R. Comparing representations with relational and EER models. Communications of the ACM, 33, 2 (February 1990), 126–140.

4. Brancheau, J., and Wetherbe, J.C. Key issues in information systems—1986. MIS Quarterly, 11, 1 (March 1987), 23–45.

5. Brosey, M., and Shneiderman, B. Two experimental comparisons of relational and hierarchical database models. International Journal of Man-Machine Studies, 10 (1978), 625–637.

6. Carlis, J.V., and March, S.T. A descriptive model of physical database design problems and solutions. In Proceedings of the International Conference on Data Engineering, IEEE Computer Society, Los Angeles, April 24–27, 1984.

7. Chan, H.C.; Wei, K.K.; and Siau, K.L. User-database interface: the effect of abstraction levels on query performance. MIS Quarterly, 17, 4 (December 1993), 441–464.

8. Chen, P.P. The entity-relationship model: toward a unified view of data. ACM Transactions on Database Systems, 1, 1 (January 1976), 9–36.

9. Coad, P., and Yourdon, E. Object-Oriented Analysis, 2d ed. Englewood Cliffs, NJ: Yourdon Press, 1991.

10. Codd, E.F. A relational model of data for large shared data banks. Communications of the ACM, 25, 2 (February 1970), 109–117.

11. Codd, E.F. Relational database: a practical foundation for productivity. Communications of the ACM, 25, 2 (February 1982), 109–117.

12. Czejdo, B.; Elmasri, R.; Rusinkiewicz, M.; and Embley, D.W. A graphical data manipulation language for an extended entity-relationship model. IEEE Computer, 23, 3 (March 1990), 26–36.

13. Davis, G.B. Caution: user developed systems can be dangerous to your organization. Working Paper MISRC-WP-82-04, MIS Research Center, University of Minnesota, Minneapolis, 1984.

14. Date, C.J. An Introduction to Database Systems, 6th ed. Reading, MA: Addison-Wesley, 1995.

15. Date, C.J., with Darwen, H. A Guide to the SQL Standard, 3d ed. Reading, MA: Addison-Wesley, 1994.

16. Dickson, G.W.; Leitheiser, R.L.; Wetherbe, J.C.; and Nechis, M. Key information systems issues for the 1980's. MIS Quarterly, 8, 3 (September 1984), 135–154.

17. Elmasri, R.A., and Larson, J.A. A graphical query facility for ER databases. In Proceedings of the 4th International Conference on Entity-Relationship Approach, October 1985, Chicago, 1985, pp. 236–245.

18. Greenblatt, D., and Waxman, J. A study of three database query languages. In B. Shneiderman (ed.), Databases: Improving Usability and Responsiveness. London: Academic Press, 1978, pp. 77–97.

19. Jarvenpaa, S.L., and Machesky, J.J. End user learning behavior in data analysis and data modeling tools. In Proceedings of the 7th International Conference on Information Systems, San Diego, 1986, pp. 152–167.

20. Juhn, S.H., and Naumann, J.D. The effectiveness of data representation characteristics on user validation. In Proceedings of the 6th International Conference on Information Systems, Indianapolis, 1985, pp. 212–226.

21. Kenny, J.W.; Bradford, D.A.; Snyder, C.A.; and Thompson, N.G. The effects of relational and entity-relationship data models on query performance of end users. International Journal of Man-Machine Studies, 31 (1989), 257–267.

22. Leitheiser, R.L. An examination of the effects of alternative schema descriptions on the understanding of database structure and the use of a query language. Unpublished Ph.D. dissertation. University of Minnesota, Minneapolis, 1988.

23. Lochovsky, F.H., and Tsichritzis, D.C. User performance considerations in DBMS selection. Proceedings of the 1977 ACM SIG-MOD Conference on Management of Data, 1977, pp. 128–134.

24. Mantha, R. Data flow and data structure modeling for database requirements determination: a comparative study. MIS Quarterly, 11, 4 (December 1987), 531–546.

25. March, S.T.; Carlis, J.V.; and Flory, A. On the effective use of fourth generation languages: a manager's guide to relational database design and use. Information Center Resource, End User Computing. New York: Auerbach Publishers, April 1986.

26. Mayer, R.E. Elaboration techniques that increase the meaningfulness of technical text. Journal of Educational Psychology, 72 (1980), 770–784.

27. Neter, J., and Wasserman, W. Applied Linear Statistical Models. Homewood, IL: Richard D. Irwin, 1974.

28. Niederman, F.; Brancheau, J.C.; and Wetherbe, J.C. Information systems management issues for the 1990's. MIS Quarterly, 15, 4 (December 1991), 475–500.

29. Nolan, R.L. Managing the crisis in data processing. Harvard Business Review, 57, 2 (March–April 1979), 115–126.

30. Reisner, P. Use of psychological experimentation as an aid to development of a query language. IEEE Transactions on Software Engineering, SE-3 (1977), 218–229.

31. Reisner, P. Human factors studies of database query languages: a survey and assessment. ACM Computing Surveys, 13 (1981), 13–31.

32. Reisner, P.; Boyce, R.F.; and Chamberlin, D.D. Human factors evaluation of two data base query languages—Square and Sequel. In Proceedings of the National Computer Conference, 1975, pp. 447–452.

33. Ridjanovic, D. Comparing quality of data representations produced by nonexperts using logical data structure and relational data models. Unpublished doctoral dissertation, University of Minnesota, Minneapolis, 1985.

34. Rivard, S.R., and Huff, S.L. An empirical study of users as application developers. Information & Management, 8, 2 (1985), 89–102.

35. Rogers, T.R., and Cattell, R.G.G. Entity-relationship database user interfaces. In Proceedings of the Sixth International Conference on Entity-Relationship Approach, New York, November 9–11, 1987; North-Holland, 1988, pp. 353–366.

36. Rockart, J.F., and Flannery, L.S. The management of end user computing. Communications of the ACM, 26, 10 (October 1983), 776–784.

37. Schlager, M.S., and Ogden, W.C. A cognitive model of database querying. Proceedings CHI'86 Human Factors in Computing Systems, Boston, 1986, pp. 107–113.

38. Shneiderman, B. Improving the human factors aspect of database interactions. ACM Transactions on Database Systems, 3, 3 (September 1978), 417–439.

39. Shneiderman, B. Direct manipulation: a step beyond programming languages. IEEE Computer, 16, 8 (August 1983), 57–69.

40. Suh, K.S., and Jenkins, A. M. A comparison of linear keyword and restricted natural language data base interfaces for novice users. Information Systems Research, 3, 3 (1992), 252–272.

41. Thomas, J.C., and Gould, J.D. A psychological study of query by example. In Proceedings of the National Computer Conference, 1975, pp. 439–445.

42. Vassiliou, Y.; Jarke, M.; Stohr, E.A.; Turner, J.A.; and White, N.H. Natural languages for database queries: a laboratory study. MIS Quarterly, 7, 4 (December 1983), 47–61.

43. Welty, C., and Stemple, D.W. Human factors comparison of a procedural and a nonprocedural query language. ACM Transactions on Database Systems, 6, 4 (December 1981), 626–649.

44. Wetherbe, J.C., and Leitheiser, R.L. Information centers: a survey of services, decisions, problems, and successes. Journal of Information Systems Management, 3, 1 (1985), 3–10.

45. Zloof, M. Query-By-Example: A data base language. IBM Systems Journal, 16 (1977), 324–343.

## APPENDIX A: Logical Data Structure Example (LDS)

![](/api/attachments/AFH8ZU6W/fulltext/images/544188d700614b7ce889fff088f8de09b0274c889cbe8c52500858884cc57c42.jpg)

## APPENDIX B: Table Representation Example

DEPENDENT

<table><tr><td>EMPLOYEE</td><td>FIRSTNAME</td><td>AGE</td><td>SEX</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

EMPLOYEE

<table><tr><td>EMPLOYEENO</td><td>LASTNAME</td><td>FIRSTNAME</td><td>SEX</td><td>AGE</td><td>PHONENO</td><td>STARTYEAR</td><td>SALARY</td><td>DEPARTMENT</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

DIVISION

<table><tr><td>NAME</td><td>CITY</td><td>STATE</td><td>DIRECTOR</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

EDUCATION

<table><tr><td>EMPLOYEE</td><td>SCHOOL</td><td>DEGREE</td><td>BEGINYEAR</td><td>FINYEAR</td><td>GPA</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

DEPARTMENT

<table><tr><td>DEPTNO</td><td>DEPTNAME</td><td>CITY</td><td>STATE</td><td>BUDGET</td><td>MANAGER</td><td>DIVISION</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## APPENDIX C: Table with Arrows Representation Example

DEPENDENT

<table><tr><td>EMPLOYEE</td><td>FIRSTNAME</td><td>AGE</td><td>SEX</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

EMPLOYEE

<table><tr><td>EMPLOYEENO</td><td>LASTNAME</td><td>FIRSTNAME</td><td>SEX</td><td>AGE</td><td>PHONENO</td><td>STARTYEAR</td><td>SALARY</td><td>DEPARTMENT</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="4">DIVISION</td></tr><tr><td>NAME</td><td>CITY</td><td>STATE</td><td>DIRECTOR</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

EDUCATION

<table><tr><td>EMPLOYEE</td><td>SCHOOL</td><td>DEGREE</td><td>BEGINYEAR</td><td>FINYEAR</td><td>GPA</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

DEPARTMENT

<table><tr><td>DEPTNO</td><td>DEPTNAME</td><td>CITY</td><td>STATE</td><td>BUDGET</td><td>MANAGER</td><td>DIVISION</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## APPENDIX D: Table with Text Only Representation Example

<table><tr><td colspan="2">DEPENDENT</td></tr><tr><td>EMPLOYEE</td><td></td></tr><tr><td>FIRSTNAME</td><td></td></tr><tr><td>AGE</td><td>EMPLOYEE</td></tr><tr><td>SEX</td><td>EMPLOYEEENO LASTNAME</td></tr><tr><td></td><td>FIRSTNAME</td></tr><tr><td></td><td>SEX</td></tr><tr><td></td><td>AGE</td></tr><tr><td></td><td>PHONENO STARTYEAR</td></tr><tr><td>DIVISION</td><td>SALARY DEPARTMENT</td></tr><tr><td>NAME</td><td></td></tr><tr><td>CITY</td><td></td></tr><tr><td>STATE</td><td></td></tr><tr><td>DIRECTOR</td><td></td></tr><tr><td></td><td>EDUCATION</td></tr><tr><td></td><td>EMPLOYEE SCHOOL DEGREE</td></tr><tr><td>DEPARTMENT</td><td>BEGINYEAR FINYEAR GPA</td></tr><tr><td>DEPTNO</td><td></td></tr><tr><td>DEPTNAME</td><td></td></tr><tr><td>CITY</td><td></td></tr><tr><td>STATE</td><td></td></tr><tr><td>BUDGET</td><td></td></tr><tr><td>MANAGER</td><td></td></tr><tr><td>DIVISION</td><td></td></tr></table>

APPENDIX E: Descriptions and Examples of SQL Query Types

Projection query: returns specified attribute/column values from all instances/rows for a single entity/table.

Simple selection query: returns specified attribute/column values from instances/rows for a single entity/table that meet a given condition.

Boolean selection query: returns specified attribute/column values from instances/rows for a single entity/table that meet an AND/OR combination of conditions.

Built-in function query: returns the result of a calculation applied to attribute/column values from instances/rows for a single entity/table.

Group by query: returns the results of calculations applied to attribute/column values from instances/rows that are grouped based on common attribute/column values from a single entity/table.

SELECT EMPLOYEENO, DEPARTMENT, SALARY FROM EMPLOYEE;

SELECT EMPLOYEENO, DEPARTMENT, SALARY FROM EMPLOYEE WHERE AGE > 35;

SELECT EMPLOYEENO, DEPARTMENT,
SALARY FROM EMPLOYEE WHERE AGE > 35 AND SEX = 'F';

SELECT AVG (SALARY) FROM EMPLOYEE WHERE AGE > 35;

SELECT DEPARTMENT, AVG (SALARY) FROM EMPLOYEE WHERE AGE > 35 GROUP BY DEPARTMENT;

<table><tr><td>Order by query: returns sorted, specified attribute/column values from instances/rows for a single entity/table</td><td>SELECT EMPLOYEEENO, SALARY FROM EMPLOYEE WHERE AGE &gt;35 ORDER BY SALARY DESC;</td></tr><tr><td>Union query: returns and combines sets of specified attribute/column values from instances/rows for more than one entity/table.</td><td>SELECT AGE FROM EMPLOYEE UNION SELECT AGE FROM DEPENDENT;</td></tr><tr><td>Join query: returns specified attribute/column values from joined instances/rows for more than one entity/table.</td><td>SELECT EMPLOYEEENO, SALARY FROM EMPLOYEE, DEPARTMENT WHERE STATE = &#x27;W&#x27; AND DEPARTMENT = DEPTNO;</td></tr></table>

APPENDIX F: Treatment Means for Representation Stage

<table><tr><td colspan="5">Individual Treatment Means</td></tr><tr><td>Measure</td><td>LDS</td><td>Table</td><td>Table/arrows</td><td>Table/text</td></tr><tr><td>Reading time</td><td>2,031</td><td>2,400</td><td>2,543</td><td>2,533</td></tr><tr><td>Practice time</td><td>2,300</td><td>4,214</td><td>3,364</td><td>3,248</td></tr><tr><td>Total time</td><td>4,332</td><td>6,614</td><td>5,906</td><td>5,782</td></tr><tr><td>Entity recall</td><td>18.1</td><td>13.8</td><td>13.9</td><td>16.2</td></tr><tr><td>Attribute recall</td><td>18.5</td><td>18.8</td><td>15.6</td><td>19.6</td></tr><tr><td>Relationship recall</td><td>8.6</td><td>3.2</td><td>2.2</td><td>5.7</td></tr><tr><td>Total recall</td><td>45.2</td><td>35.8</td><td>31.7</td><td>41.5</td></tr><tr><td>Valid questions</td><td>10.9</td><td>10.9</td><td>11.1</td><td>9.7</td></tr><tr><td>Invalid questions</td><td>1</td><td>3.4</td><td>1.9</td><td>1.4</td></tr><tr><td>Correct evaluations</td><td>19.9</td><td>21.7</td><td>20.2</td><td>20.4</td></tr></table>

APPENDIX G: Treatment Means for Query Language Stage

Individual Treatment Means

<table><tr><td>Measure</td><td>LDS</td><td>Table</td><td>Table/arrows</td><td>Table/text</td></tr><tr><td>Reading time</td><td>4,395</td><td>4,686</td><td>5,467</td><td>4,851</td></tr><tr><td>Practice time</td><td>9,479</td><td>6,677</td><td>7,314</td><td>4,965</td></tr><tr><td>Total time</td><td>13,874</td><td>11,363</td><td>12,781</td><td>9,816</td></tr><tr><td>Valid queries</td><td>5.3</td><td>6.2</td><td>7.4</td><td>8.1</td></tr><tr><td>Invalid queries</td><td>4.8</td><td>3</td><td>3.8</td><td>3.9</td></tr><tr><td>Correct queries</td><td>8.3</td><td>10.8</td><td>11.1</td><td>12.4</td></tr><tr><td>Correct evaluations</td><td>17.9</td><td>20.5</td><td>21.4</td><td>20.8</td></tr></table>
