---
otero_id: 9270
otero_key: "TRN6XVD3"
title: "The effects of data model representation method on task performance"
authors: "Robert M. Fuller; Uday Murthy; Brad A. Schafer"
year: "2010"
journal: "Information & Management"
doi: "10.1016/j.im.2009.06.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effects of data model representation method on task performance

Robert M. Fuller <sup>a,</sup>\*, Uday Murthy <sup>b</sup>, Brad A. Schafer <sup>c</sup>

<sup>a</sup> Department of Accounting and Information Management, University of Tennessee, 623 Stokely Management Center, Knoxville, TN 37996, United States

<sup>b</sup> Accounting Information Systems, School of Accountancy, University of South Florida, United States

<sup>c</sup> School of Accountancy, J. Mack Robinson College of Business, Georgia State University, United States

## A R T I C L E I N F O

Article history: Received 16 May 2008 Received in revised form 30 April 2009 Accepted 5 June 2009 Available online 20 February 2010

Keywords: Data model organization Data modeling training Error detection performance Querying Experiment

## A B S T R A C T

Data models are frequently created with little thought about their layout. Our research examined how data models organized in a columnar fashion compared to equivalent data models which did not, by improving novice designer’s performance in error detection, comprehension, and query construction.

Experimental results showed that the columnar organized data model improved performance in error detection and querying, but not in comprehension. Also, the columnar organized data model was perceived as being more useful. The results of our research have important implications for data model design, especially for novices who must interpret and use them.

\- 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

In the process of designing a software artifact, one of the first steps is to construct a data model that represents users’ needs. This conceptual data model becomes part of the basis for developing a functioning IS. The entity-relationship (ER) modeling approach was one of the early attempts to allow designers to focus on the semantics of their problem domain in terms of the entities of interest and the logical relationships among them. It is often used by systems analysts and designers to depict the information needs in the domain as a basis for developing a system as well as to provide a communication mechanism between systems analysts, designers and users. There are, however, no overarching guidelines or standards to follow for laying out the entities in an ER model.

Some researchers have proposed the structuring of ER diagrams by incorporating domain-specific semantics (e.g., accounting resources, events, agents, (REA)) to improve the semantic representation of the model [3]. One interesting aspect of such semantics is the placement of the data entities into three columns representing economic resources, events, and agents and the listing of event data entities in the sequence in which they typically occur in a business context. From a theoretical perspective, Cognitive Fit Theory and computational efficiency of representation both suggest that a data model representation that is shown in a way that more closely mirrors a user’s perception of reality should result in better performance in tasks using that representation. While this may be true for individuals trained in the representation domain, it is not clear what a domain-specific representation might mean to individuals who are trained in a different domain or are novices in it [5]. Accordingly, we investigated whether the use of a specific data model representation, such as the organization of entities into columns of resources, events, and agents would improve task performance for novice users of data models [8]. The research question addressed is: What impact does data model organization have on an individual’s data task performance and perceptions, even when the individual is not specifically trained to recognize the model organization format?

This has important practical and theoretical implications. First, if novices realize significant improvement in performing basic database tasks, the organization benefits by improving their performance when interacting with (or querying from) the system. Second, it extends prior results by examining the extent to which the data model representation method impacts subsequent comprehension and assessment of the system.

## 2. Theory development and hypotheses

Cognitive Fit Theory suggests that an appropriate fit between a graphical representation and the requirements of the task will result in improved performance. Higher levels of fit between the task and its representation improve the cognitive processes performed to complete the task: thus higher levels of fit are associated with greater comprehension. Also, less cognitive effort will be required to perform the task, resulting in better performance.

![](/api/attachments/TRN6XVD3/fulltext/images/8c2ab2f4662296bfa35687dfa4658f679cdde8f9b6feec3e54f46a44e8963a60.jpg)  
Fig. 1. Research model.

We are generally interested in how both the graphical representation and the individual’s skills impact task performance for a specific set of tasks. Specifically, as depicted in Fig. 1, we focus on the impact of the graphical representation (organization method) on database task performance and perceptions about the representation, and how skills developed through training might moderate these relationships. For our research we were particularly interested in tasks that assessed data models for their accuracy in depicting the underlying business reality, tasks related to the comprehension and understanding of a data model itself, and ongoing tasks that were facilitated by the use of a data model such as the development of queries to extract data as depicted in the data model.

## 2.1. Representation method – semantic richness

Conceptual models are graphical representations of an IS drawn at an abstract level that focus only on those parts of interest. The creation of the abstraction is governed by rules that define what constructs are of interest and how they relate to one another. For example, the ER model identifies entities and relationships and provides a graphical method to represent them using a specific set of rules governing how they are related and represented.

Graphical representations can vary in both informational and computational equivalence. Two diagrams are informationally equivalent if the same inferences can be made from both. To describe or explain a database or business scenario, ER modeling makes use of structures such as entities, relationships, and relationship cardinalities. Our hypothesis is that two diagrams should be considered informationally equivalent if they both describe the same underlying business reality. Also, they are computationally equivalent if the same amount of cognitive effort is required to draw the same inferences from them. A representation is therefore more computationally efficient than another if it facilitates improved search, recognition, and inference. Organization in a data model implies that there is some coherent structure or arrangement underlying the placement of the constructs that make up the model; this could include relationships resulting from entities being placed adjacent to one another. As a result, the structure may suggest the way that the data model should be examined, thereby improving its computational efficiency. However, a data model that lacks organization may still be informationally equivalent, as long as it contains all the semantics inherent in the organized model.

Some research has promoted the use of an organized model to provide a semantic framework that is particularly suited to modeling domain-specific phenomena, while still employing familiar modeling constructs; for example, the REA model further identifies events that occur in an enterprise, resources that are affected by these events, and agents (internal and external) that participate in these events. Resource and event entities are connected by means of relationships that represent the stock–flow interactions between them, thus a credit sale event represents an outflow of finished goods that is eventually coupled with an inflow of cash when a customer pays. While stock–flow, duality, and control relationships represent major aspects of the semantics of an REA model, a deep structure distinction, we focused on a second aspect of the semantics, specifically the organization of the entities into columns of resources, events, and agents and the top-down sequencing of events in a chronological order: a surface structure distinction. Such a columnar representation, combined with the sequencing of events, should provide a better cognitive fit for users evaluating and understanding a data model of business processes. For data tasks involving business data and processes, a model depicted using some form of organization should represent a better fit for users working on data-related tasks, compared with a model lacking any organization, even if it is informationally equivalent. The increase in semantic richness, defined as the expressiveness of information communicated with a given amount of syntax, can guide the user in examining and assessing the model, improving computational efficiency.

Graphical representations can vary in the degree to which they aid a user in understanding the underlying business reality [7]. Prior research has shown that, for error detection tasks, the use of representation methods that are semantically rich lead to better accuracy and performance and comprehension. Furthermore, when analysts use representations that are more computationally efficient, performance improves. Therefore, for query performance, ability to comprehend the underlying data structures generates superior performance [2].

Therefore, we hypothesized that the use of a data model organized in columns of resources, events, and agents will provide a more semantically rich data representation of a business scenario, and will be associated with better task performance.

H1. The use of a columnar organized data representation will have a positive impact on task performance compared to data representation not so organized.

H1a. Individuals using a columnar organized model will perform better on error detection tasks than individuals using a model not so organized.

H1b. Individuals using a columnar organized model will perform better on comprehension tasks than individuals using a model not so organized.

H1c. Individuals using a columnar organized model will perform better on query tasks than individuals using a model not so organized.

## 2.2. Training

The skills that individuals have in either performing a task or applying a graphical representation to it can impact the performance of that task. These skills can come about either from experiences or training received. Therefore, providing the requisite training should make individuals more adept at applying the representation when solving a task requiring it and less cognitive effort should be required, resulting in improved performance. Prior research has supported this, though it often compared modeling representations that were not equivalent, from an informational or computational standpoint. Other research on two different but informationally equivalent data model representations showed that trained individuals had improved model comprehension and required, on average, less time to understand a semantically richer model (e.g. [4]). However, participants in these studies had been trained in using both types of representations and therefore they probably understood the additional semantics. In general, we would expect that individuals working on a task and provided with a representation in which they have been trained would perform better than individuals who had not received training. Therefore, we hypothesized:

H2. Individuals trained in the use of a particular graphical representation type (e.g., columnar organized or not organized) will perform better on tasks when using that type of representation.

H2a. Individuals’ performance on an error detection task will be better when the model type matches their training type.

H2b. Individuals’ performance on a comprehension task will be better when the model type matches their training type.

H2c. Individuals’ performance on a query task will be better when the model type matches their training type.

Research in cognition applied to information processing suggests that individuals prefer problem solving strategies that minimize cognitive effort. If we consider that one purpose of a data representation is to be a communication medium between database designers and end users, then an important aspect of the data model representation is the degree of difficulty that users have in understanding the business reality depicted in the data model. To the degree that a representation is computationally efficient in expressing the underlying business context, individuals will perceive that it is more useful and be more satisfied with its use. We expected that a data model organized in columnar fashion should help end users and would thus be more computationally efficient than a data model without such organization. Accordingly, we hypothesized:

H3. The use of a columnar organized data representation will have a positive impact on perceptual and satisfaction outcomes compared to a data representation not so organized.

H3a. Individuals using a columnar organized data model will perceive higher usefulness of the model than individuals using a data model not so organized.

H3b. Individuals using a columnar organized data model will perceive higher ease-of-use of the model than individuals using a data model not so organized.

H3c. Individuals using a columnar organized data model will be more satisfied with the model than individuals using a data model not so organized.

## 3. Research design and method

We tested these hypotheses using a 2 - 2 between-subjects experimental design. The independent variables included instruction type (training: measured variable) and model pattern (treatment: manipulated variable). The training variable depended on whether the participant’s instructor employed a non-organized ER graphical representation or an organized (columnar) representation. The model representation (treatment) manipulation was a random assignment of participants to one of the two data models.

## 3.1. Participants

One hundred and thirty-two junior and senior-level undergraduate business students enrolled in either a database design or an accounting information systems (AIS) course were the subjects. Sixty-two percent of participants were male. Both courses required students to create graphical representations for database designs and use them in querying databases. Students from seven classes participated. They received a nominal (1%) course credit for doing so. Students enrolled in the IS course (three sections) were taught by two different instructors who taught traditional ER data modeling (i.e., without reference to columnar organization). The AIS course (four sections) was taught by three instructors; three were taught data modeling using an organized model (columns of resource, events, and agents) and one was taught traditional ER data modeling.

## 3.2. Measures

The performance measure consisted of three parts: error detection, comprehension, and SQL-syntax. The error detection measure represented the number of errors found in a database model that had been seeded with 11 errors. A grader, who was blind to the experimental hypotheses, scored participants’ answers on this task. Due to its objective nature, (participants either did or did not correctly identify an error), only one grader was used. Participant scores could thus range from 0 to 11.

For the comprehension task, participants answered 19 objective questions designed to assess their ability to understand and interpret their graphical representation. Participant scores for this part could range from 0 to 19.

The SQL-syntax variable represents a percent correct score for two queries required from participants. A grader blind to the research hypotheses scored each SQL query in terms of the syntax elements that were correct, as the fields in the SELECT part of the query, the table(s) indicated in the FROM part of the query, the tables joined, and the criteria specified in the WHERE part of the query; these elements could be identified by using the provided graphical representation. The SQL-syntax score thus represented the decimal fraction of the SQL-syntax elements correctly identified (summed for the two queries of each participant). Participant scores for SQL-syntax could thus range from 0 to 2.00.

Upon finishing the task, each participant completed a questionnaire that contained manipulation checks, demographics, and measures of perceptions of the ease-of-use, usefulness, and satisfaction of the participant with the graphical representation they received. All perceptual measures were adapted from previously validated instruments (five items addressed perceived ease-of-use, six measured perceived usefulness, and six were for satisfaction). The Cronbach’s alpha for each construct was: ease-ofuse 0.787, perceived usefulness 0.972, and satisfaction 0.925. Since these measures indicated that the constructs were reasonably reliable, the individual questions were averaged to provide a single measure for each construct.

## 3.3. Tasks and procedures

Over the course of the experiment, participants performed three tasks. At the start, they read a business narrative. Second, they received a graphical representation (an ER data model without or including columnar organization); this was seeded with 11 errors, and students were asked to identify all possible errors (see Appendixes A and B). The entities and relationships were identical in the two representations; the only difference was that the organized representation treatment showed three columns of entities (resources on the left, events in the middle in the order in which they occurred in the narrative, and agents to the right).

Participants then logged in to a Web-based computer application that was programmed to lead participants through the phases of the experiment. For the error detection task, participants input errors as they found them into the Web-based application. They were allowed 10 min to complete this task. To motivate participants to be efficient and list as many errors as possible, they were told that the first five students to correctly identify each error would receive bonus points (these points were not used in the data analysis but to motivate students to be efficient).

Upon completion of the error detection task, the business narrative and incorrect model were collected from the participants and they were given the corrected version of their data model and another 5 min to review the corrected model (see Appendix C). Next, participants returned to the Web-based application and were presented with the 19 objective questions designed to assess their level of comprehension of the model (see Appendix D). Participants had access only to the corrected model when they answered these questions. This comprehension task took 10 min.

The next phase of our experiment involved using the corrected data model representation as the basis for framing and running SQL queries. Participants minimized the Web-based application and opened a SQL querying client (mySQL Control Center), and accessed a database with an implementation of the corrected model. They were also provided with an expanded version of their data model depicting all of the attributes within each entity. Participants were shown the questions to be answered on the webbased application (see Appendix E). After they input the SQLsyntax representing their answer to a question, they were presented with the next question. Two questions of increasing difficulty were presented to students. This phase of the experimented lasted 15 min.

Upon completion of this task, participants were directed to a post-task questionnaire (see Appendix F). Upon completion of this questionnaire, participants had completed the experiment.

## 4. Analysis and results

## 4.1. Manipulation check

One debriefing question asked participants to ‘‘Identify the model type presented in your case materials.’’ While the treatment variable included only two models, the question offered four choices. We excluded the 13 participants who answered this question incorrectly, since it meant that they were either not paying attention during training or when performing the experimental task. Excluding them allowed us to maximize our effect size: only those participants who answered the question correctly could have recognized the model pattern. Thus the final data set was from 119 participants.

## 4.2. Effect of training and treatment

## 4.2.1. Descriptive data

Of these 119 participants, 62 (52%) were in classes where a columnar organized data model was emphasized, and 57 were enrolled in classes where traditional ER data models were covered. Thus, the ‘‘training’’ treatment represents a measured independent variable rather than a manipulated one, depending on the class in which the participant was enrolled. Of the 62 participants trained in organization, 33 (53%) received an unorganized model and 29 received a columnar organized model in the case materials. Of the 57 participants trained using models lacking organization, 29 (51%) received an unorganized model in the case materials and 28 received a columnar organized model. Table 1, Panel A presents these data. Panel B presents the mean and standard deviations for each of the three dependent measures of performance, organized by training type and model representation method.

## 4.2.2. Performance tasks

To measure the impact of treatment and training on participant performance, a multivariate ANOVA was performed. Two covariates were included in the model as control variables. The first was an instructor variable. Because instructors may have focused more on some database tasks (design, use, and evaluation), including an instructor variable should control for possible differences in classroom instruction. The second was the participant’s confidence in their responses. Although confidence is not a precise measure of aptitude, this measure was included as a proxy controlling for general variance in the participant’s aptitude [1].

To determine the overall effect of our treatment and training on the dependent variables, a MANOVA was performed. The results indicated that treatment did have a direct main effect $( F _ { 3 , 1 1 1 } = 2 . 7 ,$ $p < 0 . 0 5 )$ , but training did not $( F _ { 3 , 1 1 1 } = 1 . 6 , \ : \mathrm { n } . s . )$ . There was also no overall interaction effect between treatment and training $( F _ { 3 , 1 1 1 } = 0 . 6 , \ \mathrm { n } . s . )$ (see Table 2). Given the significant main effect for the treatment, follow-up univariate tests were performed to assess its effect on the measures.

Table 1 Descriptive statistics.

<table><tr><td rowspan="2">Panel A</td><td colspan="3">Number of participants in each condition</td></tr><tr><td colspan="3">Training type</td></tr><tr><td>Model pattern</td><td>Organized</td><td>Non-organized</td><td>Total</td></tr><tr><td>Non-organized</td><td>33</td><td>29</td><td>62</td></tr><tr><td>Organized</td><td>29</td><td>28</td><td>57</td></tr><tr><td>Total</td><td>62</td><td>57</td><td>119</td></tr><tr><td>Panel B</td><td colspan="3">Mean score for participants by condition (standard deviation in parentheses)</td></tr><tr><td rowspan="2">Task</td><td rowspan="2">Model pattern (treatment)</td><td colspan="2">Training type</td></tr><tr><td>Organized</td><td>Non-organized</td></tr><tr><td rowspan="2">Error detectiona</td><td>Non-organized</td><td>2.0 (1.5)</td><td>1.3 (1.7)</td></tr><tr><td>Organized</td><td>2.5 (1.7)</td><td>2.4 (1.8)</td></tr><tr><td rowspan="2">Comprehensionb</td><td>Non-organized</td><td>17.4 (2.1)</td><td>15.6 (3.1)</td></tr><tr><td>Organized</td><td>16.7 (3.3)</td><td>16.0 (3.1)</td></tr><tr><td rowspan="2">SQL - syntaxc</td><td>Non-organized</td><td>1.2 (.4)</td><td>1.1 (.5)</td></tr><tr><td>Organized</td><td>1.3 (.3)</td><td>1.3 (.4)</td></tr></table>

<sup>a</sup> Number of errors correctly identified out of 11 seeded errors.  
<sup>b</sup> Summed number of questions correctly answered out of 19 questions.  
<sup>c</sup> Summed percentage correct for two queries representing correctly written SQL-syntax statements in query design (range 0.0–2.0).

Table 3  
Table 2  
MANOVA – task performance on error detection, comprehension, and querying.

<table><tr><td colspan="6">Multivariate test</td></tr><tr><td>Effect</td><td>Df</td><td>Value</td><td colspan="2">F</td><td>Significance</td></tr><tr><td>Instructor</td><td>3</td><td>0.88</td><td colspan="2">4.9</td><td>0.00</td></tr><tr><td>Confidence</td><td>3</td><td>0.89</td><td colspan="2">4.4</td><td>0.01</td></tr><tr><td>Treatment</td><td>3</td><td>0.93</td><td colspan="2">2.7</td><td>0.05</td></tr><tr><td>Training</td><td>3</td><td>0.96</td><td colspan="2">1.6</td><td>0.20</td></tr><tr><td>Treatment × training</td><td>3</td><td>0.99</td><td colspan="2">0.6</td><td>0.65</td></tr><tr><td>Source</td><td>Dependent variable</td><td>Df</td><td>Mean square</td><td>F</td><td>Significance</td></tr><tr><td rowspan="3">Instructor</td><td>Error detection</td><td>1</td><td>0.3</td><td>0.1</td><td>0.370</td></tr><tr><td>Comprehension</td><td>1</td><td>55.8</td><td>7.3</td><td>0.004</td></tr><tr><td>SQL-syntax</td><td>1</td><td>0.92</td><td>6.0</td><td>0.008</td></tr><tr><td rowspan="3">Confidence</td><td>Error detection</td><td>1</td><td>8.5</td><td>3.2</td><td>0.039</td></tr><tr><td>Comprehension</td><td>1</td><td>28.9</td><td>3.8</td><td>0.027</td></tr><tr><td>SQL-syntax</td><td>1</td><td>1.4</td><td>8.7</td><td>0.002</td></tr><tr><td rowspan="3">Treatment (model type)</td><td>Error detection</td><td>1</td><td>14.5</td><td>5.4</td><td> $0.011^a$ </td></tr><tr><td>Comprehension</td><td>1</td><td>0.3</td><td>0.0</td><td> $0.420^b$ </td></tr><tr><td>SQL-syntax</td><td>1</td><td>0.6</td><td>3.6</td><td> $0.031^c$ </td></tr><tr><td rowspan="3">Training</td><td>Error detection</td><td>1</td><td>6.0</td><td>2.3</td><td>0.069</td></tr><tr><td>Comprehension</td><td>1</td><td>27.0</td><td>3.5</td><td>0.032</td></tr><tr><td>SQL-syntax</td><td>1</td><td>0.0</td><td>0.0</td><td>0.483</td></tr><tr><td rowspan="3">Treatment × training</td><td>Error detection</td><td>1</td><td>2.5</td><td>0.9</td><td> $0.169^d$ </td></tr><tr><td>Comprehension</td><td>1</td><td>7.7</td><td>1.0</td><td> $0.159^e$ </td></tr><tr><td>SQL-syntax</td><td>1</td><td>0.0</td><td>0.0</td><td> $0.432^f$ </td></tr></table>

a, b and c = Hypothesis 1 predicts a significant difference in performance based on model type. This tests the hypothesis based on treatment (columnar/lacking columnar model presented) for error detection performance, comprehension, and querying SQL-syntax respectively.  
d, e and f = Hypothesis 2 predicts a significant interaction between training and treatment.

Hypothesis 1(a, b and c) predicted that columnar organization would provide a richer semantic representation through better alignment of the data model with the narrative. The univariate result from the MANOVA, one-tail adjusted, supported H1a for error detection $( F _ { 1 , 1 1 3 } = 5 . 4 , p < 0 . 0 5 )$ and H1c for querying tasks $( F _ { 1 , 1 1 3 } = 3 . 6 ,  p < 0 . 0 5 )$ , but not H1b for the comprehension task $( F _ { 1 , 1 1 3 } = 0 . 0 , \ : \mathrm { n } . s . )$

Hypothesis 2(a, b and c) predicted that the individuals would perform better on the task when the representation they receive matched the representation in which they have been trained and also predicted an interaction between training and treatment. The result did not support the inclusion of training as a moderating variable for the comprehension task $( F _ { 1 , 1 1 3 } = 1 . 0 , ~ \mathrm { n } . s . )$ , error detection $( F _ { 1 , 1 1 3 } = 0 . 9 , \ \mathrm { n . } s . )$ or querying tasks $( F _ { 1 , 1 1 3 } = 0 . 0$ , n.s.). Because the treatment by training interaction was not significant, the results therefore do not support Hypothesis 2. While the main effect of training was not hypothesized for performance on the three tasks, the results indicated a statistical difference of training on the comprehension task $( F _ { 1 , 1 1 3 } = 3 . 5 , p < 0 . 0 5 )$ . Thus, performance on the three tasks was not impacted by a match of training type to model representation presented, but performance on one task (comprehension) was significantly better for those trained with organized models.

Participant perceptions of the data model Mean score for participants by condition (standard deviation in parentheses).

<table><tr><td rowspan="2">Task</td><td rowspan="2">Model pattern (treatment)</td><td colspan="4">Training type</td></tr><tr><td colspan="2">Organized</td><td colspan="2">Non-organized</td></tr><tr><td rowspan="2">Ease-of-usea</td><td>Non-organized</td><td>3.8</td><td>(0.9)</td><td>3.68</td><td>(1.1)</td></tr><tr><td>Organized</td><td>4.2</td><td>(0.9)</td><td>3.73</td><td>(1.2)</td></tr><tr><td rowspan="2">Usefulnessb</td><td>Non-organized</td><td>4.4</td><td>(1.3)</td><td>4.12</td><td>(1.4)</td></tr><tr><td>Organized</td><td>4.7</td><td>(1.0)</td><td>4.62</td><td>(1.4)</td></tr><tr><td rowspan="2">Satisfactionc</td><td>Non-organized</td><td>4.8</td><td>(1.1)</td><td>4.69</td><td>(0.9)</td></tr><tr><td>Organized</td><td>5.0</td><td>(0.9)</td><td>4.32</td><td>(1.2)</td></tr></table>

<sup>a</sup> Participant perception of data model scaled response (1-7) with 7 representing strong agreement.  
<sup>b</sup> Participant perception of data model scaled response (1-7) with 7 representing strong agreement.  
<sup>c</sup> Participant perception of data model scaled response (1-7) with 7 representing strong agreement.

## 4.2.3. Participant perceptions

Hypothesis 3(a, b and c) predicted that participants would have more positive perceptions of the columnar organized data model. Participants provided their perceptions of the model’s usefulness, ease-of-use, and satisfaction in the post-task questionnaire. The means and standard deviations for each of the three measures are shown in Table 3.

To determine the effect of treatment and training on the perceptual dependent variables, an overall MANOVA was performed. The results indicated that treatment did have a direct main effect $( F _ { 3 , 1 0 9 } = 2 . 1 , p = 0 . 0 5 )$ , and training did not $( F _ { 3 , 1 0 9 } = 1 . 1 , \mathrm { n } . s . ) .$ There was also an overall interaction effect between treatment and training $( F _ { 3 , 1 0 9 } = 2 . 1 , p = 0 . 0 5 )$ (see Table 4). Given the significant main effect for the treatment, follow-up univariate tests were performed to assess its effect on the measures.

To test the impact of different model representations on participant’s satisfaction with them, the univariate results revealed that the model was significant for usefulness but not the other measures. Specifically, we found a significant one-tail adjusted main effect for treatment for model usefulness $( F _ { 1 , 1 1 1 } = 3 . 3 , ~ p < 0 . 0 5 )$ . However, we do not find a significant treatment effect for ease-of-use or satisfaction. Hypothesis 3 would have had support with a significant treatment effect for each measure. Based on the analysis, however, we found statistical support only for Hypothesis 3a. These results are shown in Table 4.

Table 4  
MANOVA – perceptions of model usefulness and ease-of-use and satisfaction with the model.

<table><tr><td colspan="6">Multivariate test</td></tr><tr><td>Effect</td><td>Df</td><td>Value</td><td colspan="2">F</td><td>Significance</td></tr><tr><td>Instructor</td><td>3</td><td>0.92</td><td colspan="2">3.1</td><td>0.02</td></tr><tr><td>Treatment</td><td>3</td><td>0.95</td><td colspan="2">2.1</td><td>0.05</td></tr><tr><td>Training</td><td>3</td><td>0.97</td><td colspan="2">1.1</td><td>0.17</td></tr><tr><td>Treatment × training</td><td>3</td><td>0.95</td><td colspan="2">2.1</td><td>0.05</td></tr><tr><td>Source</td><td>Dependent variable</td><td>Df</td><td>Mean square</td><td>F</td><td>Significance</td></tr><tr><td rowspan="3">Instructor</td><td>Ease-of-use</td><td>1</td><td>6.3</td><td>6.2</td><td>0.007</td></tr><tr><td>Usefulness</td><td>1</td><td>8.6</td><td>5.7</td><td>0.009</td></tr><tr><td>Satisfaction</td><td>1</td><td>6.3</td><td>5.7</td><td>0.009</td></tr><tr><td rowspan="3">Treatment</td><td>Ease-of-use</td><td>1</td><td>2.0</td><td>2.0</td><td> $0.080^a$ </td></tr><tr><td>Usefulness</td><td>1</td><td>5.1</td><td>3.3</td><td> $0.035^b$ </td></tr><tr><td>Satisfaction</td><td>1</td><td>0.0</td><td>0.0</td><td> $0.432^c$ </td></tr><tr><td rowspan="3">Training</td><td>Ease-of-use</td><td>1</td><td>1.0</td><td>1.0</td><td>0.164</td></tr><tr><td>Usefulness</td><td>1</td><td>0.2</td><td>0.1</td><td>0.366</td></tr><tr><td>Satisfaction</td><td>1</td><td>2.7</td><td>2.4</td><td>0.061</td></tr><tr><td rowspan="3">Treatment × training</td><td>Ease-of-use</td><td>1</td><td>1.1</td><td>1.1</td><td>0.153</td></tr><tr><td>Usefulness</td><td>1</td><td>0.4</td><td>0.3</td><td>0.299</td></tr><tr><td>Satisfaction</td><td>1</td><td>2.5</td><td>2.3</td><td>0.067</td></tr></table>

a, b and c = Hypotheses 3a, b and c predicts user perception of ease-of-use, usefulness, and satisfaction will be greater with the organized modeling representation respectively.

## 5. Discussion and conclusion

Our research investigated whether novices could achieve performance gains by using a data model organized in columns of resources, events, and agents versus a traditional ER model representation, and whether users reported greater ease-of-use, usefulness, and satisfaction with a columnar organized model. An experiment was performed employing a 2 (training type: columnar model organization versus no organization) - 2 (model pattern: columnar model versus no organization) design, in which participants performed three tasks—an error detection task, a comprehension task, and a querying task. The results supported our argument that the columnar organized model carried meaning beyond an ER representation that contained the same database semantic elements but did not have any particular organization. The results are summarized in Table 5.

As observed from the results for Hypothesis 1, the columnar organization by itself yielded a significant improvement in error detection and querying performance, regardless of instructor and prior training effects. This suggests that for modeling of business/ accounting phenomena, it is important and beneficial to organize the model in a manner consistent with business semantics. Our results indicated that identifying errors and omissions in the model became easier when it conformed to a columnar organization, than when the same information was presented in an ER model that contained the same database semantics but was not so as organized.

Our results revealed no significant difference between the columnar organized representation and the traditional ER representation. Perhaps this result is not surprising, given that the two representations were equivalent in terms of database semantics. When asked specific questions, such as ‘‘How many activities are employees involved in?’’ it appeared that participants could reply equally accurately from either representation, because one simply has to locate the EMPLOYEES entity and count the number of event type or associative entities to which it is linked. However, for a more cognitively demanding task such as detecting errors, which requires switching back and forth between a narrative description and the corresponding model representation, the columnar organization facilitates identification of errors and omissions more readily. For constructing SQL queries as well, a task which requires traversing the data model to identify all entities or tables needed for the query, the columnar organized model lends itself to the task more naturally.

Our results showed that, regardless of training, the use of a columnar organized model generated results that were as good as, or superior to results obtained by individuals trained to use simple ER data models. This surprising result amplifies the benefit of using models with an organizational structure when modeling business processes.

## Table 5

Finally, the results for Hypothesis 3 indicate that while participants between the two treatments did not perceive their models differently in terms of ease-of-use and satisfaction, they did rate the models significantly different in terms of usefulness: users of the columnar model perceived it to be more useful than users of the simple ER model.

<sup>a</sup> Performance on comprehension was significantly better for participants trained with organized models, regardless of the model used.

Research results by hypothesis.

<table><tr><td>Hypothesis</td><td>Description</td><td>Result</td></tr><tr><td>H1a</td><td>Organized model better for error detection</td><td>Supported</td></tr><tr><td>H1b</td><td>Organized model better for comprehension</td><td>Not supported</td></tr><tr><td>H1c</td><td>Organized model better for query</td><td>Supported</td></tr><tr><td>H2a</td><td>If training = model type, better error detection</td><td>Not supported</td></tr><tr><td>H2b</td><td>If training = model type, better comprehension</td><td>Not supported $^{a}$ </td></tr><tr><td>H2c</td><td>If training = model type, better query</td><td>Not supported</td></tr><tr><td>H3a</td><td>Organized model rated higher usefulness</td><td>Supported</td></tr><tr><td>H3b</td><td>Organized model rated higher ease-of-use</td><td>Not supported</td></tr><tr><td>H3c</td><td>Organized model rated higher satisfaction</td><td>Not supported</td></tr></table>

## 5.1. Limitations

In addition to the limitations normally associated with experiments, the generalizability of our research was limited by the use of student participants at a single institution. Caution should be exercised in generalizing the results to practicing auditors, accountants, and database analysts, because it is not clear whether greater experience with a particular model representation, with SQL querying, or even the specific domain of interest, would yield results similar to the findings of our research [9]. However, prior research has shown the robustness of the measures used in this research in generalizing to professionals [6]

Another consideration is the impact of time constraints on task performance. Our participants were limited to 10-min for the error detection task. Because they were required to refer back to a full page of narrative text as they attempted to identify errors in the graphical model, it is possible that the 10-min time constraint impacted results. Since the computational efficiency of the model was of interest, a time constraint was desired. However, we cannot generalize to a less time-constrained task.

We did have one section of accounting students who received training in general ER data modeling without reference to the REA framework; this allowed us to determine if training domain had an impact on the results. We found no differences between this accounting group and the IS group.

## 5.2. Implications

Our findings have practical implications for database designers and users of data models. Many business organizations employ traditional ER diagrams to depict the structure of their databases. The ‘‘reference model’’ within enterprise systems such as SAP R/3 is often depicted using such ER data models. Furthermore, data models encountered by accountants, auditors, and end users in practice rarely have any form of organization. The results of our research suggest that developers should be encouraged to organize data models in some manner to foster better understanding and use of the underlying database system and business reality especially when the target domain involves business processes. To conclude, our research supported the idea that providing organization in a data model improved performance.

## Appendix A. Business scenario

Ms. Jane Smith is the owner of CDX, a ‘‘members only’’ store in Clearwater, Florida, that buys and sells new and used compact discs (CD). Ms. Smith feels that membership gives people a sense of belonging and builds loyalty to the store. To become a new member, an individual must provide his or her name, address, and phone number and pay a one time, \$15 fee, which is eventually deposited into one of CDX’s three bank accounts held at First National Bank. New members receive a membership card that shows their membership number, name, and date of membership. The membership process, as well the process of buying and selling CDs, can be handled by any one of the four employees at CDX.

Once a person becomes a member, CDX can sell CDs to or purchase CDs from the member. It is possible that a person signs up for membership but CDX never either purchases CDs from or sells CDs to the member. It is also possible that CDX sells CDs to a member without ever purchasing any from that member, or that CDX purchases CDs from a member, and never sells any CDs to that member. In summary, once a person becomes a member, CDX can purchase from or sell to that member, but the member is under no obligation to transact any purchases or sales with CDX.

The process of purchasing CDs from members involves one member and may involve the purchase of one or more CDs at a time. Each CD purchase is handled by one employee. For the CDs, members are paid cash, which comes out of one of CDX’s bank accounts at First National Bank. A ‘‘purchase receipt’’ is generated and given to the member as confirmation of the transaction. Each CD purchased by CDX is added to the inventory of CDs and is uniquely identified by a bar code on the CD jewel case. Thus, it is possible that CDX will be carrying more than one units of the same CD (e.g., three units of The Rolling Stones ‘‘Wild Horses’’ CD).

The process of selling CDs to members also involves one member and may be for one or more CDs at a time. Each CD sale is handled by one employee. Members pay for the CDs by cash, check or credit card (checks and credit cards can be considered to be ‘‘cash equivalents’’). The payment received is deposited into one of CDX’s bank accounts at First National Bank. A ‘‘sale receipt’’ is generated and given to the member as confirmation of the sale. Each CD sold by CDX reduces the inventory of CDs and the bar code of each CD sold is captured at the time of sale.

CDX not only obtains its CDs from members, but also purchases new CDs from several CD vendors. CDX maintains information on the vendors from whom they have purchased CDs such as the vendor’s name, address, phone and fax numbers, as well as the name of their contact at the vendor. An order for new CDs from a vendor is usually for many CDs, but may be for as few as one CD. An order is submitted by one employee and is submitted to only one vendor. To keep track of the ordering process, CDX captures the date of the order, as well as an expected receiving date for the order, and they assign each order a specific order number. Not every CD that CDX has in inventory has been purchased through a vendor, but many have been obtained that way. The inventory of CDs at CDX includes both CDs purchased from members and CDs purchased from vendors.

## A.1. Instructions

Assume that the above narrative describing the scenario at CDX is correct. The model that follows is intended to be a representation of the business rules as described in the narrative. You are required to identify ALL errors in the model as it differs from the narrative. As you find an error, immediately input the error, being as specific as possible, into the box shown on the screen. It is important that you work efficiently. For each error, the first five students that correctly identify that error will receive bonus points. It is therefore to your advantage to input each error immediately into the system as you find it.

Appendix B. Error detection data models (with seeded errors, not to scale)  
![](/api/attachments/TRN6XVD3/fulltext/images/061e6d3556a13779a4fb6742ed5543781559b785c51c288e903c4eb9bb4e38e9.jpg)

Appendix C. Comprehension data models (corrected, not to scale)  
![](/api/attachments/TRN6XVD3/fulltext/images/72a01c100d8d904c8ebccf052772cdc2a58511bc05446a2692e0ebf8e0f68821.jpg)

## Appendix D<sup>.</sup> Comprehension questions (answers are yes, no, unable to determine)

1. How many activities are employees involved in?

2. Of the following relationships in the model, which will need a linking table in a physical design?

a. Members—CD-selling

b. Employees—CD-buying

c. CD-inventory—CD-selling

3. Do all employees have to be involved in selling CDs?

4. Can a member sell us (we buy) a CD without involving an employee (a do-it-yourself transaction)?

5. Do we issue credit to our members (can a member pay us later for a CD?)

6. By having a circle on the relationship between receiving and employee, does an employee have to sign for received goods (CDs)?

7. Does a member have to have purchased (Our sell) before they can sell us (our buy) as a rule?

8. Can a member order CDs from our vendors?

9. Because all cardinalities for the cash entity relationships, at the cash side of the relationship line, have a single line, does this indicate we only have one bank account?

10. Does the model show how to adjust inventory if a CD is stolen or lost?

11. Based on the model, can we pay for an order before it is received?

12. Can the same employee order the CD, receive the CD, pay for the CD, and sell the CD?

13. Do all employees have to be involved in receiving CDs?

14. Can we sell a CD to a vendor if the vendor is not a member?

15. Can two employees place an order for the same CD from the same vendor?

16. Can a member exist in the database and never purchase a CD?

## Appendix E. SQL Questions (corrected model used with fields added)

1. List the first and last name of members who joined after January

1, 2002 and live in Tampa

select firstname, lastname

from members

where joindate > ‘2002-01-01’

and city = ‘Tampa’

2. List the artist, title, and price at which CDs were bought from members with ‘Platinum’ status

select artist, title, price

from cdinventory, cdsold, cdselling, members

where members.memberid = cdselling.memberid

and cdselling.saleid = cdsold.saleid

and cdsold.itemid = cdinventory.itemid

and members.status = ’Platinum

## Appendix F. Post-task questionnaire

Perceived ease-of-use

1. I found the data modeling representation cumbersome to use. (r)

2. Using the data modeling representation was frustrating. (r)

3. Using the data modeling representation required a lot of mental effort. (r)

4. The data modeling representation was clear and understandable to me.

5. Overall, I found the data modeling representation easy to use.

## Perceived usefulness

1. The data modeling representation allowed me to complete the task more quickly.

2. The data modeling representation improved my task performance.

3. The data modeling representation increased my productivity on the task.

4. The data modeling representation enhanced my effectiveness on the task.

5. The data modeling representation made it easier to complete the task.

6. Overall, I found the data modeling representation useful to complete the task.

## Satisfaction

1. The data modeling representation provided the information I needed.

2. The content of the data modeling representation met my needs.

3. The data modeling representation provided sufficient information.

4. The format of the data modeling representation was useful

5. The data modeling representation was clear.

6. Overall, I am satisfied with the data modeling representation for providing me the information I needed.

## References

[1] A. Blais, M. Thompson, J. Baranski, Individual differences in decision processing and confidence judgments in comparative judgment tasks: the role of cognitive styles, Personality and Individual Differences 38, 2005, pp. 1701–1713.

[2] P.L. Bowen, R.A. O’Farrell, F.H. Rohde, Analysis of competing data structures: does ontological clarity produce better end-user query performance? 25th International Conference on Information Systems, 2004.

[3] G.L. Geerts, W.E. McCarthy, An ontological analysis of the economic primitives of the extended-REA enterprise information architecture, International Journal of Accounting Information Systems 3 (1), 2002, pp. 1–16.

[4] G.J. Gerard, The REA pattern, knowledge structures, and conceptual modeling performance, Journal of Information Systems 19 (2), 2005, pp. 57–77.

[5] S.Y. Hung, Expert versus novice use of the executive support systems: an empirical study, Information & Management 40 (3), 2003, pp. 177–189.

[6] W.R. King, J. He, A meta-analysis of the technology acceptance model, Information & Management 43 (6), 2006, pp. 740–755.

[7] K.R. Walsh, M.H. Dickey, Structured modeling group support systems: a product design theory, Information & Management 41 (5), 2004, pp. 655–667.

[8] Y. Wand, R. Weber, Research commentary: information systems and conceptual modeling – a research agenda, Information Systems Research 13 (4), 2002, pp. 363– 376.

[9] S.H. Wang, G. Ariguzo, Knowledge management through the development of information schema, Information & Management 41 (4), 2004, pp. 445–456.

![](/api/attachments/TRN6XVD3/fulltext/images/a3b66fa5b996acfe57a6a2d88570884831f916c02924476b6a40c9b0d91de179.jpg)  
Robert M. Fuller is an assistant professor and Reagan Scholar in the Department of Accounting and Informa: tion Systems of the College of Business at the University of Tennessee. He received his Ph.D. in Information Systems from Indiana University. His research interests are in the areas of collaborative technologies, computer-mediated communication and communication in requirements elicitation. His research has been published in such journals as MIS Quarterly, Information Systems Research, Decision Support Systems, the Journal of the Association for Information Systems and the Journal of Computer Information Systems.

![](/api/attachments/TRN6XVD3/fulltext/images/0f0252a0fa8727d19bfe9947cae0abd5da013e7d0c1fc4ce76756d61b4a74237.jpg)

Uday Murthy is professor and holder of the Quinn Eminent Scholar Chair in the School of Accountancy at the University of South Florida. He has a Ph.D. from Indiana University and an MBA from Drexel University. Professor Murthy’s teaching and research interests are in the area of accounting information systems. His research has been published in a number of journals including The Accounting Review, Auditing: A Journal of Practice & Theory, Journal of Information Systems, International Journal of Accounting Information Systems, Journal of Management Information Systems, Decision Support Systems, and Information & Management.

Professor Murthy has served as coeditor of the Journal of Information Systems, the leading academic journal for accounting information systems research.

![](/api/attachments/TRN6XVD3/fulltext/images/48acb8dc3252f0c7ed252d97db83fe85eadd3929081f6e22a7dc0fe80f01154c.jpg)

Brad A. Schafer is a Clinical Assistant Professor in the School of Accountancy at the J. Mack Robinson College of Business of Georgia State University. He earned a Ph.D. in Business Administration from the University of Utah. His research and teaching are in the areas of auditing and information systems. His research has been published in such journals as Issues in Accounting Education, AIS Educator Journal, and Advances in Accounting Behavioral Research.
