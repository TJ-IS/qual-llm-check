---
otero_id: 1856
otero_key: "HVH4RRW5"
title: "Comparing the understandability of alternative data warehouse schemas: An empirical study"
authors: "David Schuff; Karen Corral; Ozgur Turetken"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparing the understandability of alternative data warehouse schemas: An empirical study

David Schuff <sup>a,</sup>⁎, Karen Corral <sup>b</sup>, Ozgur Turetken <sup>c</sup>

<sup>a</sup> Department of Management Information Systems, Fox School of Business, Temple University, 207G Speakman Hall, 1810 North 13th Street, Philadelphia, PA 19122, United State

<sup>b</sup> Department of Information Technology and Supply Chain Management, College of Business and Economics, Boise State University, United States

<sup>c</sup> Ted Rogers School of Information Technology Management, Ryerson University, Canada

## a r t i c l e i n f o

Article history: Received 7 November 2009 Received in revised form 9 February 2011 Accepted 11 April 2011 Available online 17 April 2011

Keywords: Data warehousing Schema understandabilit Experiment Cognitive effort

## a b s t r a c t

An easily understood data warehouse model enables users to better identify and retrieve its data. It also makes it easier for users to suggest changes to its structure and content. Through an exploratory, empirical study, we compared the understandability of the star and traditional relational schemas. The results of our experiment contradict previous <sup>fi</sup>ndings and show schema type did not lead to signi<sup>fi</sup>cant performance differences for a content identi<sup>fi</sup>cation task. Further, the relational schema actually led to slightly better results for a schema augmentation task. We discuss the implications of these <sup>fi</sup>ndings for data warehouse design and future research.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The data warehouse, the core tool in a business intelligence strategy, continues to increase in importance within the information technology function. According to IDC, data warehouse platform software and service sales were up 12% in 2008 to \$7.6 billion, and projected to continue growing at a rate of 7.4% annually [34]. Gartner also predicts that data warehouses in industries such as telecommunications, retail, and distribution will grow in size to hundreds of terabytes [5].

There are two predominant designs used to build these large information stores: the relational model and the dimensional model. Warehouses built using either model can be used to deploy an organization's data in a form ready for analysis by its users (i.e., a set of integrated and “cleansed” data from multiple data sources). The difference between the relational and dimensional models is in the structure of the logical schema used to represent each. Relational models are represented by the traditional relational schema, while the dimensional model is represented using a variant called the “star schema” (so called because of its appearance). These schemas are the logical models derived from the conceptual (ER) model, and are the mechanism by which users understand the structure of the database.

It has been asserted that the structure of a star schema, with its focus on business “facts,” is a simpler representation than that of a traditional relational schema; so much so that the dimensional model is advocated as “the only viable technique for designing end-user delivery databases” [23]. However, there is controversy surrounding this assertion (e.g., see [6,21]). The main criticism of the star schema is that it is overly restrictive because its structure forces the data warehouse designer to choose a narrow focus (sometimes even a single subject). It is often dif<sup>fi</sup>cult to retrieve data not related to that original focus. The result is a data warehouse optimized for some users to the exclusion of others [18]. Haughey [15] contends that “the world is not a star” and that star schema cannot effectively re<sup>fl</sup>ect complex business scenarios. Additionally, Jukic [21] proposes that model choice is a complex issue, and is essentially a tradeoff between simplicity and <sup>fl</sup>exibility. As these researchers suggest, the star schema may not be as semantically accurate as the traditional relational schema in certain cases, such as when direct relationships between some of the dimensions exist. However, for many practical problems, it is possible to create semantically equivalent alternative schemas using each approach. There are technical reasons for selecting one method over the other [21], but in this study, we will only be examining the impact of the data model on understandability of the data warehouse where the content that is contained in the data warehouse is equivalent regardless of the way it is presented.

Data models and their associated schemas are powerful communication tools that are used between users and analysts and especially between analysts and designers [33]. Data models represent the structure of the database and the data available within it [24]. There are several scenarios where it would be bene<sup>fi</sup>cial for business users, who typically are not technology experts, to understand a database model as operationalized through a schema. One example is during the systems analysis and design process, where verifying the validity of a database schema is an essential step in application development. A database designer can gather initial data requirements from the business users, but showing those users the resulting schema is a way of making sure that these requirements have been properly understood. Essentially, end users “sign off” on the schema, indicating that it meets the data requirements of the application. In situations where the schema cannot be understood, the client must rely on the developer's explanation of what is contained in the database, which may be subject to the same threats of misinterpretation as the original requirements gathering process. In addition, integrating the end user into the development process has ongoing practical signi<sup>fi</sup>cance as new data become available in the form of new data entities and relationships that can be added to the warehouse. The ability of business users to suggest modi<sup>fi</sup>cations to the data warehouse according to the changing data needs of the organization is greatly aided by how well they understand what data the current version of the warehouse provides.

Understandability of the schema also enables end users to more signi<sup>fi</sup>cantly contribute to the structural changes in the data warehouse when faced with the changing needs of the organization. Ideally, those non-experts that are closest to the business should be able to determine whether a data warehouse ful<sup>fi</sup>lls existing business needs and suggests modi<sup>fi</sup>cations that the IT department can implement. The ability of a schema to facilitate such “graceful extensibility” [23] has been suggested as an important characteristic in data warehouse design.

A second scenario where it is useful for business users to under stand the schema is situations where the user can query the database directly. Pre-canned reports and interfaces are not adequate for all users [22]. For example, when end users' data needs are not static, simply being able to use a query-by-example (QBE) tool is more expedient than construction of additional applications to facilitate the data retrieval. This ultimately increases the <sup>fl</sup>exibility afforded to users in their interactions with the warehouse. QBE tools are common in cube browsing products such as Cognos Business Intelligence or Microsoft Analysis Services.

The objective of this paper is to provide additional insight as to whether the underlying schema of a data warehouse (star or traditional relational) affects the understandability of that data warehouse. Since prior theory provides con<sup>fl</sup>icting guidance regarding the superiority of one schema over the other, we take an exploratory approach. Through two controlled experiments, we compare the relative understandability of the traditional relational schema to the dimensional schema. Previous studies have addressed schema comprehension using recall as a surrogate metric for understandability [7,35] to compare these schemas [9]. In this study, we build upon this research by conducting an empirical investigation that compares these two alternative schemas through two tasks that are more involved than simple recall.

## 2. Background

## 2.1. Evaluation of data model understandability

According to McGee, “in order for a data model to be used, it must be understood” ([26], p. 372). He identi<sup>fi</sup>es three properties of data models that enhance their ability to be learned and understood: (1) simplicity refers to the number of structure types (e.g., tuples and relations) and the number of rules that govern the assembly of those structure types, (2) elegance describes the ability to create the model using the smallest number of structure types, and (3) picturability is the degree to which the model lends itself to a visual representation.

When comparing graphical representations to tabular representations, past research hypothesized graphical models to be advantageous for comprehension due to the additional semantic meaning conveyed by a drawing. Graphical semantic models have been associated with higher levels of comprehension [20] and graphical representations with simpler graphic styles (for example, lists within graphic elements instead of separate graphic elements for each item) have been found easier to interpret [28]. Other research has found that a model is more easily learned if it has greater syntactical clarity [19]. In a comparison of the extended E-R model (EER) to the tabular relational model, users could more effectively model relationships using the EER model because its lower semantic distance (i.e. how close the meaning of the diagram's components represent the constructs that are modeled) more clearly conveys relationships among entities [1]. Evidence from the prior literature supports McGee's assertion [26] that the most effective modeling techniques are those that are graphical and simple while describing all of the structure types.

## 2.2. The traditional relational schema versus the star schema

The traditional relational schema and the star schema are both logical data models. They differ in two important ways: the selection of tables, and the way in which the relationships are constructed between those tables. For example, consider two simple schemas (modeling scripts) for an airline reservation database. The <sup>fi</sup>rst is a traditional relational schema (Fig. 1) and the second is a star schema (Fig. 2). These two schemas highlight that the different models can be equivalent from an information-content perspective.

The relationships in a traditional relational schema are constructed based on the logical relationships between these tables, but without speci<sup>fi</sup>c emphasis on any one table or relationship. In other words, there are no structural rules de<sup>fi</sup>ning the organization of the relationships between the tables. The star schema's structure is more constrained—it is based on a set of relationships between descriptive tables and a central table that represents the subject of the database (a reservation). A series of one-to-many relationships exists between the central “fact” table and the associated dimensions. Essentially, Fig. 2 describes a reservation as a particular <sup>fl</sup>ight, with a particular passenger, on a particular airline, at a particular time.

Cognitive science provides some theoretical guidance suggesting a difference in understandability between the relational and star schema diagrams. Semantic network theory states that humans store concepts in memory as linked units [1,8]. Therefore, the representation of a collection of objects as a semantic network should be intrinsically easy for people to understand. Further, prior research has shown that the structure of human memory is organized into “chunks” which serve to increase memory capacity (e.g., [2,24,27]). This organization stores not only the data elements themselves, but also the relationships between the elements that are stored. The implication of this for comprehension of data models is that models that organize their elements into logical groupings (chunks) with clear associations between those elements will be more intuitive and therefore easier to understand.

![](/api/attachments/HVH4RRW5/fulltext/images/41f4062f3f6d1e293366d440f4a13ab71c95818c4695441969133bba1d3703b8.jpg)  
Fig. 1. Simple traditional relational schema.

![](/api/attachments/HVH4RRW5/fulltext/images/c1c1f90e7ff6bff4c0a3d8b8908e66868c87ac7d21b6faa274ae12efa78187da.jpg)  
Fig. 2. Simple star schema.

Looking at these alternative schemas in Figs. 1 and 2 using McGee's criteria of simplicity, elegance, and picturability [26], it can be argued that simplicity and elegance of the two models in these examples are comparable. They both use the same components (tables, attributes, and cardinality notation),<sup>1</sup> and therefore have the same number of structure types. However, the two schemas differ with regard to picturability. The star schema is able to convey more clearly than the traditional relational schema its most important information. Not only is the user able to see the database's structure through the positioning of its entities and relationships around the fact, but the visual centrality of the fact within the diagram makes clear the subject of the database. Because multiple dimensions link back to the same fact (a “reservation,” in the airline example), the fact itself is reinforced. This grouping of dimensions and the fact create a chunk that visually conveys relationships within the schema.

Previous research has found evidence to support this. Drawing primarily on the concepts of semantic network theory and chunking, the star schema pattern would be easier for users to recall [9]. In a lab experiment, subjects could recall a star schema diagram more accurately than an equivalently complex diagram of a traditional relational schema. Subjects also recalled the star schema in a pattern consistent with the semantic meaning of the diagram. When reconstructing the diagram, subjects <sup>fi</sup>rst recalled the fact table, followed by its surrounding dimensions. This implies that the focus of the warehouse (the fact) was reinforced by its associated dimensions.

However, it is less clear whether or not the advantage of the star schema is scalable, and would carry over to more complex models. There are two reasons for this. First, while chunking can enable people to process more information at once [27], this capacity is still limited. Given a more complex data warehouse with many dimensions, the bene<sup>fi</sup>ts of a star schema's presentation may be diminished by the sheer number of elements. Second, as the schemas become increasingly complex, the difference in picturability is likely to become less pronounced. A complex data warehouse typically consists of several smaller star schemas that share a common (conforming) dimension.

In that case, the schema will have several foci, making the diagram more complicated to understand.

As an example, compare the relatively simple schemas in Figs. 1 and 2 to the more complex schemas used for the experiment in our second study (Figs. 3 and 4). The difference in picturability of these two diagrams in Figs. 3 and 4 appears to be much less pronounced than in the simpler schemas of Figs. 1 and 2. While there is still no focus in the traditional relational schema, the star schema now has <sup>fi</sup>ve foci (Internship, Club Membership, Job Offer, Enroll, and Application). Further, at least visually, the conforming dimension (Student) becomes a sixth focal point of the schema.

Therefore, given the lack of a de<sup>fi</sup>nitive theoretical rationale, there is an open question as to whether the structural advantages of the star schema truly exist. They may actually diminish signi<sup>fi</sup>cantly when the schema is complex, and therefore have limited advantage under realistic, enterprise-wide scenarios. We have constructed two studies that speci<sup>fi</sup>cally address that issue. Our studies use complex schemas and tasks that go beyond the recall of a simple model to test subjects' comprehension of the underlying data model. In the next section, we develop our hypotheses and describe the studies that compare the star and traditional relational schemas.

## 3. Hypothesis development

We put forward a series of hypotheses to test whether the star schema will differ from the traditional relational schema on key evaluation metrics with regard to understandability. Gemino and Wand [11] make a distinction between model comprehension and understanding, where the latter requires an understanding of the modeled domain in addition to the grammar, and asserts that understanding (which is more inclusive than comprehension) should guide the choice of dependent variables in empirical studies. Topi and Ramesh [33] list “user performance” and “attitudes” as the two major categories of dependent variables in studies that evaluate data models. Because of its more objective nature we chose user performance as our surrogate for user understanding, which would be re<sup>fl</sup>ected in both the quality of end users' responses to experimental tasks and their effort expended to complete that task. Outcome quality (e.g., [4,10,11,16,17,25,29,31–33]) and effort (e.g., [4,10,11,29,31]) are commonly used indicators of success in information presentation studies, and most closely resemble the model correctness and time variables in Topi and Ramesh's categorization [33]. People use decision aids to reduce the cognitive effort they expend when performing a task [4]. A reduction in effort can serve as a measure of success, especially when there is no corresponding reduction in performance [29]. The more effective presentation of information can led to both a reduction in users' effort and a simultaneous increase in task performance [29]. Therefore, by considering both performance and effort, we can arrive at a richer measure of overall success.

In the previous section we contend that the advantages of the star schema may not exist when the schema becomes complex. We conducted two studies that aim to accurately represent the understanding and problem solving tasks one might perform when working with a complete, realistic schema (with tables, attributes, and cardinality notation). The <sup>fi</sup>rst study employs a content identi<sup>fi</sup>cation task, where subjects are required to determine whether a query can be answered by a given schema. Our second study requires subjects to augment an existing schema by adding additional entities and relationships. As we discussed earlier, these tasks have face validity as ways of measuring understandability of the underlying data model. Task choice is also important because the <sup>fi</sup>t between task and technology are key in<sup>fl</sup>uences on task success [12]. For example, Yang [36] found that the success of CASE tools depended upon their <sup>fi</sup>t with the organizations existing development methodology. The type of task the user performs may in<sup>fl</sup>uence the effectiveness of a particular diagram type (in this study, a database schema). In the context of systems analysis, Hahn and Kim [16] found that effective diagrams support the cognitive processes associated with the user's task. Due to this potential in<sup>fl</sup>uence of task on outcomes, the representativeness of the experimental tasks to those that users actually perform is important for the task-dependent nature of the results to be practical.

![](/api/attachments/HVH4RRW5/fulltext/images/799c2e9171076d9f0544748ec2c3750d956b9ff118e09bb6265ff7f35f4ac69d.jpg)  
Fig. 3. Complex traditional relational schema (used in study 2).

Since the direction and magnitude of the effect of schema type on the outcome variables are unclear, we take an exploratory approach to the problem. Because of the lack of strong theory to suggest the superiority of one diagrammatic representation over the other, we hypothesize that an effect exists but do not specify the direction. The question of whether there is a difference in understandability between the star schema and the traditional relational schema is tested through the following hypotheses:

H1. The type of schema (traditional relational or star schema) will affect the score subjects receive on the content identi<sup>fi</sup>cation task.

H2. The type of schema (traditional relational or star schema) will affect the effort subjects expend on the content identi<sup>fi</sup>cation task.

H3. The type of schema (traditional relational or star schema) will affect the score subjects receive on the schema augmentation task.

H4. The type of schema (traditional relational or star schema) will affect the effort subjects expend on the schema augmentation task.

Support for these hypotheses indicates evidence of a difference in understandability, in line with the conventional wisdom regarding these schema types [22]. A lack of support would suggest that this difference may not exist; this potential implication is also interesting from a theoretical standpoint.

The results of these studies should provide data warehouse designers new insights as to whether the practical claims on the superiority of one particular schema over the other are valid, and whether the implications of the earlier empirical studies [9] on the subject are generalizable to more complex models and more complex tasks.

## 4. Study one

## 4.1. Subjects, task, and procedure

The participants in the <sup>fi</sup>rst study were 205 undergraduate Management Information Systems students. Their average age was 23.18 years and 48% of the sample was female. Because the task involved interacting directly with a schema, we recorded the experience of the subjects with databases and database models for control purposes. Experience was modeled as a categorical, binary variable (experienced or inexperienced) based on whether the subjects had completed an introductory database design and management course. The course covered database use, SQL, and schema design using the traditional relational model.

Therefore, the study employed a 2×2 between subjects design (with schema type and experience as factors), and involved a content identi<sup>fi</sup>cation task. Through a web-based tool, subjects were shown either a traditional relational schema or a star schema diagram. The subject domain of both data warehouse schemas was a hypothetical university (see Figs. 5 and 6), and the schemas contained the same information. Subjects were given a series of ten English-language questions (see Appendix A), and then were asked whether or not the question could be answered based on the information given in the schema. Consistent with the notion of understandability [11], in order to answer the questions correctly the diagram must successfully convey both the grammar and subject domains of the model. The performance score was computed by simply totaling the number of correct answers for each subject.

![](/api/attachments/HVH4RRW5/fulltext/images/88085dafe624e12f2487e97c4a0cff52c76ad36d5504842e47fbfeb07e320fc8.jpg)  
Fig. 4. Complex star schema (used in study 2).

After the task was completed, each subject completed a questionnaire in which they assessed the level of effort they expended while performing the task using the NASA/TLX (Task Load Index) instrument [14] (see Appendix B). This instrument has been used in previous information systems studies to measure workload [e.g.. 13.30.31l. To complete the instrument, subjects must pair-wise compare six dimensions of effort (mental, physical, temporal, performance, frustration, and overall effort), each time selecting the one that contributed more to the effort expended completing the task. The subject then assesses the overall level of effort demanded on each dimension (on a scale from 1 to 7). The number of times each dimension of effort was selected in a pair-wise comparison is multiplied by its overall level in order to arrive at a weighted measure of perceived effort.

## 4.2. Results of study one

Because the dependent variables in the study (score and effort) were not signi<sup>fi</sup>cantly correlated (using Pearson's correlation test, p=0.875), we constructed two separate ANOVA models. Schema type and experience (with data modeling) were the independent variables for both models. The descriptive statistics for score are provided in Table 1. As seen in Table 2, neither the main effect of schema type (p=0.526) nor the interaction between model type and experience (p=0.181) is signi<sup>fi</sup>cant. Therefore, there was insuf<sup>fi</sup>cient evidence to support hypothesis 1 (a difference in schema type in terms of score).

The results of the analysis for hypothesis 2 are shown in Tables 3 and 4. As seen in Table 4, the schema type (p=0.833) and the interaction between schema type and experience (p=0.397) have no signi<sup>fi</sup>cant effect on effort, therefore there is also insuf<sup>fi</sup>cient evidence to support hypothesis 2 (a difference in schema type in terms of effort expended).

The results also indicate that experienced users have an overall advantage as we see a signi<sup>fi</sup>cant main effect of experience on both dependent variables (score and effort) favoring those experienced users. This <sup>fi</sup>nding still corroborates the hypotheses testing results as subjects with the same level of experience had similar levels of performance regardless of the schema type they were given. The power of our test was 0.7 for a medium effect size, making it unlikely that our inability to <sup>fi</sup>nd signi<sup>fi</sup>cant differences with the score is due to a lack of power. Similarly, the power of the test for effort is 0.99 for a small effect size. This provides compelling support for the conclusion that this lack of difference was due to the practical equivalence of the understandability of these two diagram types.

![](/api/attachments/HVH4RRW5/fulltext/images/c98b9b2c5552b1568d4cf98b8908ae0375530f03713a1540c324c188d380af9b.jpg)  
Fig. 5. Traditional relational schema used in study one.

## 5. Study two

## 5.1. Subjects, task, and procedure

The participants in the second study were 95 undergraduate Management Information Systems students (not the same students who participated in the <sup>fi</sup>rst study). They had an average age of 24.16 years, and 41.1% of the sample was female. As in the <sup>fi</sup>rst study, we controlled for the effect of subjects' familiarity with data models based on whether they had completed an introductory database design and management course.

As the <sup>fi</sup>rst study, this experiment employed a 2×2 between subjects design with schema type and experience as factors. Subjects were once again given either a traditional relational schema or a star schema diagram (that contained the same information) of a data warehouse for a hypothetical university and a textual description of the scenario (see Figs. 3 and 4). Subjects were asked to imagine that they were database designers for a <sup>fi</sup>ctitious business school (see Appendix A). They had to modify the existing data warehouse to track student participation in student clubs and professional societies. The instructions listed speci<sup>fi</sup>c information to be captured by the data warehouse, but not information regarding speci<sup>fi</sup>c tables or the relationships between them. The subjects were allowed to either draw directly on the database diagram or on a separate piece of paper. As with the <sup>fi</sup>rst study, this task was designed to test understanding as both subjects' mastery of the diagram's grammar and subject domain were needed to successfully augment the schema. As the <sup>fi</sup>rst study, each subject completed a questionnaire assessing the level of effort they expended while performing the task (see Appendix B).

The diagrams given to the subjects were missing the tables related to the task (tracking club membership). Because the schemas were equivalent with regard to information content, the task of completing the missing portion of the schema was similar regardless of the diagram. In order to calculate task scores, each response was compared to an “ideal” solution. The ideal solution was the simplest way to ful<sup>fi</sup>ll the requirements of the task, but this was not the only solution that would be considered correct. A response was considered correct as long as it was consistent with the guidelines set forth in the task instructions. Points were deducted if there were components of the response that were incorrect, such as missing or mislabeled tables and attributes, or missing or incorrect relationships.

Each element of the diagram – tables, attributes, relationships, and cardinality – was evaluated separately on a scale of 1 (“completely incorrect or missing”) to 4 (“completely correct”). A scale was used (instead of a simple “correct/incorrect” evaluation) because it provides a higher degree of differentiation between responses. It is possible that a subject might have included an element but not included it correctly (which would get rated a “2” or a “3”). For example, if a relationship should have been drawn from table A to table B, but instead it was drawn from table A to table C (and this was not correct given the rest of their solution), they would receive a score of 2 (“included but incorrect”). If there was no relationship drawn at all, they would receive a score of 1 (“completely incorrect or missing”). If they drew a relationship between table A and B (correct), and then between table A and C (incorrect), they would receive a 3 (“mostly correct”). Because there were a different number of responses for each category (e.g., the diagram had more attributes than tables) the scores for each element type (tables, attributes, relationships, and cardinality) were normalized to 25 points. The four normalized scores were summed to arrive at an overall score (out of 100). This scoring method is similar to what was done in earlier empirical research in the area, for example, the scoring based on “facets” as described in Batra et al. [3].

![](/api/attachments/HVH4RRW5/fulltext/images/75620a6de90ea2c83032048e0ffb228db489e42cf1d5a5d1ca9a789ad50c3646.jpg)  
Fig. 6. Star schema used in study one.

## Table 1

Descriptive statistics for score (study one).

<table><tr><td>Schema type</td><td>Experience</td><td>Mean</td><td>Std. deviation</td><td>N</td></tr><tr><td rowspan="3">Traditional relational schema</td><td>Experienced</td><td>8.215</td><td>0.879</td><td>51</td></tr><tr><td>Inexperienced</td><td>7.480</td><td>1.644</td><td>50</td></tr><tr><td>Total</td><td>7.852</td><td>1.359</td><td>101</td></tr><tr><td rowspan="3">Star schema</td><td>Experienced</td><td>8.346</td><td>0.988</td><td>52</td></tr><tr><td>Inexperienced</td><td>7.115</td><td>1.592</td><td>52</td></tr><tr><td>Total</td><td>7.731</td><td>1.456</td><td>104</td></tr><tr><td rowspan="3">Total</td><td>Experienced</td><td>8.282</td><td>0.933</td><td>103</td></tr><tr><td>Inexperienced</td><td>7.294</td><td>1.620</td><td>102</td></tr><tr><td>Total</td><td>7.790</td><td>1.407</td><td>205</td></tr></table>

Different pairs of the authors coded the diagrams separately. While this introduces the possibility of experimenter bias, a predetermined key was used in order to mitigate this effect. We believe the high agreement between the two sets of ratings (0.89) con<sup>fi</sup>rms this. Further, the authors evaluated only the technical correctness of the solutions rather than their subjective quality. Due to the high rater agreement, the two scores for each subject were averaged to calculate the task score.

Tests of between-subjects effects for score (study one).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>0.403</td><td>0.526</td></tr><tr><td>Experience</td><td>1</td><td>28.431</td><td>0.000</td></tr><tr><td>Schema type * experience</td><td>1</td><td>1.802</td><td>0.181</td></tr></table>

R<sup>2</sup>=0.133 (Adjusted R<sup>2</sup>=0.120).

Table 3  
Descriptive statistics for effort (study one).

<table><tr><td>Schema type</td><td>Experience</td><td>Mean</td><td>Std. deviation</td><td>N</td></tr><tr><td rowspan="3">Traditional relational schema</td><td>Experienced</td><td>0.529</td><td>0.177</td><td>51</td></tr><tr><td>Inexperienced</td><td>0.584</td><td>0.171</td><td>50</td></tr><tr><td>Total</td><td>0.556</td><td>0.176</td><td>101</td></tr><tr><td rowspan="3">Star schema</td><td>Experienced</td><td>0.504</td><td>0.167</td><td>52</td></tr><tr><td>Inexperienced</td><td>0.599</td><td>0.156</td><td>52</td></tr><tr><td>Total</td><td>0.551</td><td>0.168</td><td>104</td></tr><tr><td rowspan="3">Total</td><td>Experienced</td><td>0.517</td><td>0.172</td><td>103</td></tr><tr><td>Inexperienced</td><td>0.591</td><td>0.163</td><td>102</td></tr><tr><td>Total</td><td>0.554</td><td>0.171</td><td>205</td></tr></table>

## 5.2. Results of study two

As in the <sup>fi</sup>rst study, the data were analyzed using two ANOVA models, because score and effort were again not signi<sup>fi</sup>cantly correlated (using Pearson's correlation test, p=0.653). Schema type and experience were independent variables for both models (for descriptive statistics see Tables 5 and 9). To test hypothesis 3, the model was built using score as the dependent variable. The results show that although the main effect of schema type is not signi<sup>fi</sup>cant $( \mathtt { p } = 0 . 6 6 7 )$ ), there is a signi<sup>fi</sup>cant interaction effect between schema type and experience (p=0.013, see Table 6 and Fig. 7). To further examine the nature of this interaction, the effect of the schema type on score was tested separately for experienced and inexperienced subjects. As seen in Tables 7 and 8, experienced subjects did signi<sup>fi</sup>cantly better with traditional relational schema diagrams (score Nscore , p=0.040; see Table 7) while inexperienced subjects appear to have done better with the star schema diagrams (score Nscore , p=0.148, see Table 8) although the result for the inexperienced subjects is not signi<sup>fi</sup>cant. Therefore hypothesis 3 (a difference in schema types in terms of score) is partially supported. As for hypothesis 4, the results on effort are signi<sup>fi</sup>cant in favor of the traditional relational schema (effort Neffort , p=0.022, see Tables 9 and 10). Therefore hypothesis 4 (a difference in schema types in terms of effort expended) is supported.

These results indicate that all subjects (experienced or inexperienced) given the traditional relational schema expended less effort in completing the task than those given the star schema. Experienced subjects performed better with the traditional relational schema—those who were given that schema received a higher task score than those given the star schema. A possible explanation for this is that the experienced subjects are a group much more likely to have had experience with the traditional relational schema. Completion of the course used as criteria to classify subjects as experienced was heavily based on that schema. These subjects were more successful (performing better on the task while expending less effort) with the diagram with which they were more familiar. In addition, the increased role experience plays in modeling, as compared with simply retrieving information from a database, may have further accentuated the impact of prior modeling experience on their performance with the traditional relational schema.

## 6. Discussion

The purpose of the two studies reported in this paper was to determine whether the star schema differed from the traditional relational schema with regard to its understandability. This is an important step in demonstrating the relative effectiveness of these schemas as a delivery mechanism of data to end users. There was evidence to support this basic notion in previous studies, and we have expanded upon that work by conducting two controlled experiments, which required subjects to understand the semantic content of the schema to effectively perform the tasks. The results from the two studies are summarized in Table 11.

Tests of between-subjects effects for effort (study one).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>0.045</td><td>0.833</td></tr><tr><td>Experience</td><td>1</td><td>10.035</td><td>0.002</td></tr><tr><td>Schema type * experience</td><td>1</td><td>0.722</td><td>0.397</td></tr></table>

R<sup>2</sup>=0.051 (Adjusted R<sup>2</sup>=0.037).

Table 5  
Descriptive statistics for score (study two).

<table><tr><td>Schema type</td><td>Experience</td><td>Mean</td><td>Std. deviation</td><td>N</td></tr><tr><td rowspan="3">Traditional relational schema</td><td>Experienced</td><td>92.971</td><td>8.830</td><td>29</td></tr><tr><td>Inexperienced</td><td>49.106</td><td>19.939</td><td>17</td></tr><tr><td>Total</td><td>76.760</td><td>25.459</td><td>46</td></tr><tr><td rowspan="3">Star schema</td><td>Experienced</td><td>84.377</td><td>20.324</td><td>32</td></tr><tr><td>Inexperienced</td><td>61.222</td><td>27.119</td><td>17</td></tr><tr><td>Total</td><td>76.344</td><td>25.218</td><td>49</td></tr><tr><td rowspan="3">Total</td><td>Experienced</td><td>88.463</td><td>16.387</td><td>61</td></tr><tr><td>Inexperienced</td><td>55.164</td><td>24.231</td><td>34</td></tr><tr><td>Total</td><td>76.545</td><td>25.200</td><td>95</td></tr></table>

We found evidence that the differences in understanding for the two schema types are task-dependent [12]. In the <sup>fi</sup>rst study (which involved a content identi<sup>fi</sup>cation task), no differences were found with regard to either performance or effort expended, whether the subjects were given the star schema or the traditional relational schema. This <sup>fi</sup>nding is interesting because the formulation of queries is representative of the type of tasks typically performed by a data warehouse user. The retrieval of data from a warehouse is consistent with Kimball's [23] view of the star schema as a delivery mechanism of data to end users. However, the star schema appears to be no better than the traditional relational schema in enabling users to formulate queries.

For the schema augmentation task (the second study), users who were more experienced with data modeling appeared to do better (while still using less effort) when given the traditional relational schema. This may simply be a re<sup>fl</sup>ection of their course-speci<sup>fi</sup>c experience with that schema. It is possible that if this group had experience with the star schema in their course instead of the traditional relational schema, the experienced group would have favored the star schema. Therefore, what is most interesting is that inexperienced users did not have signi<sup>fi</sup>cantly different performance levels when using the different schema types. The lack of a difference found for these inexperienced users provides, at best, mixed evidence of a difference between the schema types. Since most end users of data warehouses are likely to be unfamiliar with data modeling, the inexperienced group is more representative of the typical end user.

The results of the experiments provided con<sup>fl</sup>icting evidence to the results of the Corral et al. study [9] (where the task required recall of the schema) as to what “technology” (i.e. the underlying schema used in design) best supports these tasks. In that context, the star schema appears to aid a simple task such as recall [9], but these bene<sup>fi</sup>ts do not appear to translate to the more complex tasks used in this paper. In the studies presented here, the results suggest that the advantage of the star schema is not scalable. Recall remains a good <sup>fi</sup>rst step, providing evidence regarding the understandability of a diagrammatic representation. However, further studies (such as this one) regarding whether this manifests itself in an improvement in task performance can provide additional insight in model comprehension in general.

As with any research, this study has limitations. First, the use of student subjects may limit the generalizability of the <sup>fi</sup>ndings. However, several aspects of the design of these studies minimize this issue. Student subjects typically differ from “real” end users because they lack domain knowledge. To alleviate this problem, in both experiments we used a domain with which students were familiar (a university). Additionally, since the level of experience among student subjects varies, we controlled for experience and incorporate its effects into our analysis.

Table 6  
Tests of between-subjects effects for score (study two).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>0.186</td><td>0.667</td></tr><tr><td>Experience</td><td>1</td><td>67.308</td><td>0.000</td></tr><tr><td>Schema type * experience</td><td>1</td><td>6.427</td><td>0.013</td></tr></table>

R<sup>2</sup>=0.445 (Adjusted R<sup>2</sup>=0.427).

![](/api/attachments/HVH4RRW5/fulltext/images/a7c4bb9dd3b30de7cafd13bfde4e508ab06243708c6488e88d3f982da2874d8f.jpg)  
Fig. 7. Interaction diagram for score-schema type by experience (study two).

Table 7  
Tests of between-subjects effects score for experienced subjects (study two).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>4.423</td><td>0.040</td></tr></table>

$\mathrm { R } ^ { 2 } { = } 0 . 0 7 0$ (Adjusted $\ R ^ { 2 } { = } 0 . 0 5 4 ) .$

A second limitation, as stated previously, is that conclusions drawn on a lack of statistical evidence to reject the null hypothesis should be made with caution. It is important to note that failure to <sup>fi</sup>nd a statistically signi<sup>fi</sup>cant difference does not prove that the effect does not exist. It simply means that we were unable to <sup>fi</sup>nd that effect. In study one, we had adequate power to detect a moderate-sized effect, making it likely that there was no effect of practical signi<sup>fi</sup>cance to be found. While we are con<sup>fi</sup>dent that the controlled nature of the experiment and the high rater reliability strengthen our ability to rule out alternative explanations, this study by itself still should not be considered conclusive. Instead, our <sup>fi</sup>ndings indicate a need for additional studies to further explore the relative ef<sup>fi</sup>cacy of these schemas.

Third, there is reason to believe that the complexity and size of the schema might have played a role, since the schemas used in study two had more entities and relationships than the schemas used in study one. Future studies should more rigorously examine these two effects by creating experimental conditions that test them separately. Speci<sup>fi</sup>cally, one could hold schema type constant and vary the size and complexity of the schema. Studies in this area should also consider different, more elaborate tasks, which test a wider range of interactions with a data warehouse to more fully understand this relationship.

## 7. Conclusions

For a data warehouse to be effective, its content must be easily understood by those who use it. This study provides insight regarding schema choice and its effect on understandability. Kimball [23] contends that using the star schema as the underlying model for a data warehouse should facilitate understanding more effectively than the traditional relational schema. However, there is controversy surrounding that statement [6,21,23]. Our results challenge Kimball's

Table 8  
Tests of between-subjects effects score for inexperienced subjects (study two).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>2.203</td><td>0.148</td></tr></table>

R<sup>2</sup>=0.064 (Adjusted R<sup>2</sup>=0.035).

Table 9  
Descriptive statistics for effort (study two).

<table><tr><td>Schema type</td><td>Experience</td><td>Mean</td><td>Std. deviation</td><td>N</td></tr><tr><td rowspan="3">Traditional relational schema</td><td>Experienced</td><td>51.931</td><td>22.274</td><td>29</td></tr><tr><td>Inexperienced</td><td>53.588</td><td>30.328</td><td>17</td></tr><tr><td>Total</td><td>52.543</td><td>25.227</td><td>46</td></tr><tr><td rowspan="3">Star schema</td><td>Experienced</td><td>62.094</td><td>24.781</td><td>32</td></tr><tr><td>Inexperienced</td><td>66.706</td><td>9.999</td><td>17</td></tr><tr><td>Total</td><td>63.694</td><td>20.853</td><td>49</td></tr><tr><td rowspan="3">Total</td><td>Experienced</td><td>57.262</td><td>23.979</td><td>61</td></tr><tr><td>Inexperienced</td><td>60.147</td><td>23.211</td><td>34</td></tr><tr><td>Total</td><td>58.295</td><td>23.624</td><td>95</td></tr></table>

## Table 10

Tests of between-subjects effects for effort (study two).

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td></tr><tr><td>Schema type</td><td>1</td><td>5.462</td><td>0.022</td></tr><tr><td>Experience</td><td>1</td><td>0.396</td><td>0.531</td></tr><tr><td>Schema type * experience</td><td>1</td><td>0.088</td><td>0.767</td></tr></table>

R<sup>2</sup>= 0.061 (Adjusted R<sup>2</sup>= 0.030).

[23] contention as we found that users performed no better when using the star schema for a content identi<sup>fi</sup>cation task, and experienced users actually performed worse at a more sophisticated schema augmentation task. There are still technical reasons to use a dimensional model and the star schema—for example, a cube is constructed and indexed for the ef<sup>fi</sup>cient retrieval of large amounts of data. The implication of our <sup>fi</sup>ndings is that those technical reasons [21], not the understandability of the two alternative schemas, should be the stronger determinant in the choice of a data model.

Our results also imply that the use of “cube browsing” tools may be no more effective than relational query-by-example tools to end users. If users do not understand the content of a dimensional database any better than they understand a traditional relational database, it is unlikely that they will be able to effectively interact with the warehouse using sophisticated business intelligence tools. Just as users of relational databases use high-level graphical interfaces with pre-de<sup>fi</sup>ned queries, the users of dimensional databases may require access to a set of prede<sup>fi</sup>ned “views” of the data cube. The burden of constructing these views will still remain with the Information Technology function. Certainly, many organizations use business intelligence tools simply as reporting tools, requiring little of the end user. Future research could focus on the construction of visual metaphors, which provide users more <sup>fl</sup>exibility without requiring direct interaction with the dimensional database.

Finally, the results of this study suggest that training is an important determinant of end user success in working with a data warehouse. Experience has a strongly signi<sup>fi</sup>cant effect on task performance (positive) and effort (negative) in the <sup>fi</sup>rst study, and a strongly signi<sup>fi</sup>cant effect on task performance (positive) in the second study. More importantly, when it comes to inexperienced users, we could not <sup>fi</sup>nd any evidence as to the superiority of one particular schema over the other. This would imply that data warehouse administrators should not, from a usability standpoint, spend time redesigning their data warehouse to improve understandability. Instead, they should train their users in the basic understanding of database schemas, regardless of their type.

## Table 11

Summary of results.

<table><tr><td></td><td>Test</td><td>Result</td><td>Direction</td></tr><tr><td colspan="4">Study one: content identification task</td></tr><tr><td>H1</td><td> $score_{ss} \neq score_{trs}$ </td><td>Not supported</td><td>N/A</td></tr><tr><td>H2</td><td> $effort_{ss} \neq effort_{trs}$ </td><td>Not supported</td><td>N/A</td></tr><tr><td colspan="4">Study two: schema augmentation task</td></tr><tr><td>H3</td><td> $score_{ss} \neq score_{trs}$ </td><td>Partially supported</td><td> $score_{ss} < score_{trs}$ (for experienced subjects only)</td></tr><tr><td>H4</td><td> $effort_{ss} \neq effort_{trs}$ </td><td>Supported</td><td> $effort_{ss} > effort_{trs}$ </td></tr></table>

## Appendix A. Experimental tasks

## Study one: content identification task

For a data warehouse built from the diagram shown, could you answer the following questions:

1. Which students had internships last year with GE?

2. How many “A”s did Professor John Doe give last semester?

3. How many jobs offered to students involved travel?

4. How many accounting majors have taken the “Introduction to Java” course?

5. How many CIS faculty got their Ph.D. from a Research I institution?

6. What percentage of internships offered no payment to students?

7. How many students failed “Introduction to Accounting” last semester?

8. How many CIS students transferred from another institution?

9. Which faculty had Mary Smith as a student?

10. Which students have been offered jobs with Motorola?

## Answers

## (1) Yes, (2) Yes, (3) No, (4) Yes, (5) No, (6) Yes, (7) Yes, (8) No, (9) Yes, (10) Yes

## Study two: schema augmentation task

You are in charge of designing the student database for the College of Business at Central State University. The Dean's of<sup>fi</sup>ce has set a goal to encourage student participation in the various student clubs on campus. To this end, they would like to track student membership in all clubs and professional societies

Your task is to add the necessary entities to the current database so that it will record that information. Given the schema of the database (see the attached diagram), you will add entities and their attributes to capture the following information:

• The name of the club or professional society

• The title of the student's role in the club or professional society, and whether they were elected or appointed to that position

• A description of the club or professional society

• The location of the club or professional society

• Any fees that are part of membership

• The dates of their af<sup>fi</sup>liation (beginning and end)

You can write your answer directly on the diagram, or in the space below.

![](/api/attachments/HVH4RRW5/fulltext/images/ff6b5420422b3da9c68a20e298616b14f463bf46bff4725e8a1a21df682ea07d.jpg)

Answers

Shaded tables were left off of the schema in Figs. 3 and 4. Subjects were asked to <sup>fi</sup>ll in the missing tables.

## Appendix B. NASA/TLX instrument

The following are dimensions of demand which could describe the task you have just completed:

<table><tr><td>Item</td><td></td><td>Description</td></tr><tr><td>MD</td><td>Mental Demand</td><td>How much mental and perceptual activity was required? Was the task easy or demanding, simple or complex?</td></tr><tr><td>PD</td><td>Physical Demand</td><td>How much physical activity was required? Was the task easy or demanding, slack or strenuous?</td></tr><tr><td>TD</td><td>Temporal Demand</td><td>How much time pressure did you feel due to the pace at which the tasks or task elements occurred? Was the pace slow or rapid?</td></tr><tr><td>OP</td><td>Overall Performance</td><td>How successful were you in performing the task? How satisfied were you with your performance?</td></tr><tr><td>FR</td><td>Frustration Level</td><td>How irritated, stressed, and annoyed versus content, relaxed, and complacent did you feel during the task?</td></tr><tr><td>EF</td><td>Effort</td><td>How hard did you have to work (mentally and physically) to accomplish your level of performance?</td></tr></table>

From each of the <sup>fi</sup>fteen pairs below, select the item that was the larger factor for you while performing the task you just completed (for example, for the <sup>fi</sup>rst pair, was there more physical demand or mental demand while completing the task?).

<table><tr><td>PD</td><td>MD</td></tr><tr><td>TD</td><td>MD</td></tr><tr><td>OP</td><td>MD</td></tr><tr><td>FR</td><td>MD</td></tr><tr><td>EF</td><td>MD</td></tr></table>

<table><tr><td>□ TD</td><td>□ PD</td></tr><tr><td>□ OP</td><td>□ PD</td></tr><tr><td>□ FR</td><td>□ PD</td></tr><tr><td>□ EF</td><td>□ PD</td></tr><tr><td>□ TD</td><td>□ OP</td></tr></table>

<table><tr><td>☐ TD</td><td>☐ FR</td></tr><tr><td>☐ TD</td><td>☐ EF</td></tr><tr><td>☐ OP</td><td>☐ FR</td></tr><tr><td>☐ OP</td><td>☐ EF</td></tr><tr><td>☐ EF</td><td>☐ FR</td></tr></table>

For each type of demand below, rate its overall level for the task you just completed (for example, what was the level of mental demand for this task?).

<table><tr><td>Demands</td><td colspan="7">Ratings for Task</td></tr><tr><td></td><td colspan="6">Low</td><td>High</td></tr><tr><td>MD</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr><tr><td>PD</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr><tr><td>TD</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr><tr><td>OP</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr><tr><td>FR</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr><tr><td>EF</td><td> $\square$ 1</td><td> $\square$ 2</td><td> $\square$ 3</td><td> $\square$ 4</td><td> $\square$ 5</td><td> $\square$ 6</td><td> $\square$ 7</td></tr></table>

## References

[1] J.R. Anderson, Cognitive Psychology and Its Implications, 3rd ed. W.H. Freeman and Co., New York, 1990.

[2] M.H. Ashcraft, Human Memory and Cognition, Scott Foresman and Co., Glenview, IL, 1989.

[3] D. Batra, J.A. Hoffer, R.P. Bostrom, Comparing representations with relational and EER models, Communications of the ACM 33 (2) (1990) 126–139.

[4] I. Benbasat, P. Todd, The effects of decision support and task contingencies on model formulation: a cognitive perspective, Decision Support Systems 33 (4) (1996) 241-252

[5] A. Bitterer, Management Update: Steer Clear of Common Data Warehousing Pitfalls (Gartner Group Research, November 16, 2005), , 2005

[6] M. Breslin, Data warehousing battle of the giants: comparing the basics of the Kimball and Inmon models, Business Intelligence Journal 9 (1) (Winter 2004) 6–20.

[7] M. Brosey, B. Shneiderman, Two experimental comparisons of relational and hierarchical database models, International Journal of Man-Machine Studies 10 (6) (1978) 625-637

[8] A.M. Collins, M.R. Quillian, How to make a language user, in: E. Tulving, W. Donaldson (Eds.), Organization of Memory, Academic Press, New York, 1972, pp. 309–351.

[9] K. Corral, D. Schuff, R.D. St. Louis, The impact of alternative diagrams on the accuracy of recall: a comparison of star-schema diagrams and entity-relationship diagrams, Decision Support Systems 42 (1) (2006) 450–468.

[10] W.H. DeLone, E.R. McLean, Information system success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60–95.

[11] A. Gemino, Y. Wand, A framework for empirical evaluation of conceptual modeling techniques, Requirements Engineering 9 (2004) 248–260.

[13] M. Grise, R.B. Gallupe, Information overload: addressing the productivity paradox in face-to-face electronic meetings, Journal of Management Information Systems 16 (3) (2000) 157–185.

[14] J. Hahn, J. Kim, Why are some diagrams easier to work with? Effects of diagrammatic representation on the cognitive integration process of systems analysis and design, ACM Transactions on Computer-Human Interaction 6 (3) (1999) 181–213.

[15] S.G. Hart, L.E. Staveland, Development of NASA-TLX (task load index): results of empirical and theoretical research, in: P.A. Hancock, N. Meshkati (Eds.), Human Mental Workload, 1988, pp. 239–250, North-Holland, New York.

[16] T. Haughey, Is dimensional modeling one of the great con jobs in data management history? Part 1, Information Management Magazine, 2004 downloaded 9/12/2009, http://www.information-management.com/issues/ 20040401/1000939-1.html.

[17] M. Hertzum, E. Frokjaer, Browsing and querying in online documentation: a study of user interfaces and the interaction process, ACM Transactions on Computer-Human Interaction 3 (2) (1996) 136–161

[18] W.H. Inmon, The Problem with Dimensional Modeling, DMReview.com, , 2000 downloaded 6/24/2009, http://www.dmreview.com/article\_sub.cfm? articleId=2184.

[19] S.L. Jarvenpaa, J.J. Machesky, End user learning behavior in data analysis and modeling tools, Proceedings of the 15th International Conference on Information Systems, 1986, pp. 152–167, Atlanta, Georgia.

[20] S.H. Juhn, J.D. Naumann, The effectiveness of data representation characteristics on user validation, Proceedings of the 14th International Conference on Information Systems, 1985, pp. 212–226, Atlanta, Georgia.

[21] N. Jukic, Modeling strategies and alternatives for data warehousing projects, Communications of the ACM 49 (4) (2006) 83–88

[22] R. Kimball, The Data Warehouse Toolkit, John Wiley, New York, 1996.

[23] R. Kimball, A Dimensional Modeling Manifesto, DBMSmag.com, , 1997 downloaded 6/24/2009, http://www.dbmsmag.com/9708d15.html.

[24] R.L. Leitheiser, S.T. March, The in<sup>fl</sup>uence of database structure representation on database system learning and use, Journal of Management Information Systems 12 (4) (1996) 187–213.

[25] K.H. Lim, I. Benbasat, P.A. Todd, An experimental investigation of the interactive effects of interface style, instructions, and task familiarity on user performance, ACM Transactions on Computer-Human Interaction 3 (1) (1996) 1–37.

[26] W.C. McGee, On user criteria for data model evaluation, ACM Transactions on Database Systems 1 (4) (1976) 380–387.

[27] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, The Psychology Review 63 (2) (1956) 81–97.

[28] J.C. Nordbotten, M.E. Crosby, The effect of graphic style on data model interpretation, Information Systems Journal 9 (2) (1999) 139–156.

[29] D.G. Roussinov, H. Chen, Document clustering for electronic meetings: an experimental comparison of two techniques, Decision Support Systems 27 (1–2) (1999) 67–79.

[30] D. Schuff, O. Turetken, J. D'Arcy, A multi-attribute, multi-weight clustering approach to managing ‘e-mail overload’, Decision Support Systems 42 (3) (2006) 1350–1365.

[31] C. Speier, M.G. Morris, The in<sup>fl</sup>uence of query interface design on decision-making performance, Management Information Systems Quarterly 27 (3) (2003) 397–423.

[32] J.K.H. Tan, I. Benbasat, The effectiveness of graphical presentation for information extraction: a cumulative experimental approach, Decision Sciences 24 (1) (1993) 167–191.

[33] H. Topi, V. Ramesh, Human factors research on data modeling: a review of prior research, an extended framework and future research directions, Journal of Database Management 13 (2) (2002) 3–19.

[34] D. Vesset, B. McDonough, Worldwide Data Warehouse Platform Software 2009– 2013 Forecast, 2009 downloaded 9/12/2009, http://www.idc.com/getdoc.jsp? containerID=217442

[35] R. Weber, Are attributes entities? A study of database designers' memory structures, Information System Research 7 (2) (1996) 137–162.

[36] H. Yang, Adoption and implementation of CASE tools in Taiwan, Information & Management 35 (2) (1999) 89–112.

David Schuff is Associate Professor of Management Information Systems in the Fox School of Business and Management at Temple University. He holds a BA in Economics from the University of Pittsburgh, an MBA from Villanova University, an MS in Information Management from Arizona State University, and a Ph.D. in Business Administration from Arizona State University. His research interests include the application of information visualization to decision support systems, data warehousing, the use of Web 2.0 media by organizations as a communications tool, and the assessment of total cost of ownership. His work has been published in MIS Quarterly, Decision Support Systems, Information & Management, Communications of the ACM, and Information Systems Journal.

Karen Corral is Associate Professor in the Department of Information Technology and Supply Chain Management at the College of Business and Economics at Boise State University. She holds a BA in English from the University of Michigan, an MS in Computer Information Systems from Arizona State University, and a Ph.D. in Business Administration from Arizona State University. Her research interests are in the area of data and knowledge management as related to decision support. Her work has been published in journals such as Communications of the ACM, Information Systems Frontiers, and Decision Support Systems.

Ozgur Turetken is Associate Professor at the Ted Rogers School of IT Management, and a senior research scientist at the Institute for Innovation and Technology Management at Ryerson University. His research interests are decision modeling and human computer interaction with an emphasis on information organization and presentation. His previous work has appeared in ACM Database, Communications of the ACM, Decision Support Systems, IEEE Computer, Information & Management, Information Systems, and Information Systems Frontiers. Dr. Turetken holds a BS in EE, an MBA (both from Middle East Technical University-Ankara, Turkey), and a PhD in Management Science and Information Systems (Oklahoma State University). He currently serves on the editorial board of the AIS Transactions on Human Computer Interaction.
