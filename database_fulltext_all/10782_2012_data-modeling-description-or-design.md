---
otero_id: 10782
otero_key: "AGRGWQUY"
title: "Data modeling: Description or design?"
authors: "Graeme Simsion; Simon K. Milton; Graeme Shanks"
year: "2012"
journal: "Information & Management"
doi: "10.1016/j.im.2012.01.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data modeling: Description or design?

Graeme Simsion, Simon K. Milton \*, Graeme Shanks

Department of Computing and Information Systems, The University of Melbourne, Victoria 3010, Australia

## A R T I C L E I N F O

Article history: Received 13 November 2010 Received in revised form 15 November 2011 Accepted 25 January 2012 Available online 14 February 2012

Keywords: Conceptual data modeling Practitioner study Design Analysis

## A B S T R A C T

Data modeling for database creation has generally been considered to be a descriptive process: the realworld is observed and represented in a conceptual model that is then transformed into a logical structure for a database. This is reflected in prescriptive methods and is the dominant assumption in most studies. However, data modeling can also be considered a type of design with negotiable requirements, a creative process, and many workable solutions. Our paper discusses empirical results from almost 500 practitioners on three continents comparing data modeling to design. We found that data modeling, as practiced, was better characterized as design.

\- 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Alternative views of data modeling

Data modeling is one of the most critical activities in the implementation of an IS: it has been characterized as a process of reality mapping. This characterization has been occasionally challenged from a philosophical perspective, from observations of practice, and from empirical evidence.

This descriptive characterization also dominates the practitioner literature. In a descriptive activity, a set of artifacts may be created, and this might well be called design, but not be of sufficient importance to the overall result as to characterize the entire activity as design. In data modeling, there is choice in the selection of components (typically entities, relationships and attributes) used to represent some part of reality. The difference between description and design is in whether this selection is a trivial part of the process compared to understanding the Universe of Discourse (UoD) {descriptive type}, or whether it is the essence of the process {design type}.

## 1.2. Previous empirical research

We know little about how experienced data modelers approach their work or about the models that are produced for real business applications. This is because most studies have assumed the process to be descriptive and have not involved practitioners.

The descriptive characterization is embodied in most empirical studies through the use of a gold standard – a single correct solution devised by the researcher, who often embedded entity and relationship names in descriptions, thus constraining the modeling abstractions. The ‘‘business requirements’’ amounted to a plain language description and the participant’s task was to translate the description to the original diagram. For example, ‘‘An employee can report to only one department. Each department has a phone number.’’ Tasks showing these two traits mainly tested facility with modeling formalisms. Yet it is common to see conclusions that indicated that novice designers did not run into much trouble in modeling entities and attributes. In the context of the research task, modeling entities may have meant little more than identifying nouns in the description. The use of simple models and prescriptive instructions limited the scope of the design.

Most empirical studies have used students as participants; of course, this limited the difficulty of the problems posed. Of the total of 3210 participants across 59 studies that we surveyed, only 147 in nine studies had more than one year’s industry experience of data modeling. Thus most studies used unrealistically simple data models. Nevertheless, some studies have used experienced data modelers and have uncovered design behavior. Comparisons of novice and expert data modelers have revealed behaviors characteristic of designers (attempting to gain a holistic understanding, categorization of problems, pattern re-use) in the experts but not in the novices.

## 1.3. The research question

Our research question was: Is data modeling better characterized as description or design? Here, data model refers to a model of a specific UoD (e.g. the data model of ABC corporation’s human

Table 1

resources operations), while data modeling refers to the set of activities required to specify a conceptual schema that will transform into a database schema but prior to its transformation into a specific DBMS data definition.

Specifically, we examined the process of data modeling that resulted in a database design that could be implemented in a relational DBMS. We did not include other purposes of conceptual data modeling (e.g., its use in IS planning).

This is an important research question for at least three reasons:

\- Most data modeling research assumes the descriptive characterization, notably in the design of experiments and in the application of ontology [2,3]. If data modeling is, in fact, design, research results need to be reinterpreted in that light.

\- Data modeling education should include expert level practice.

\- Creative thinking and evaluation of alternative designs are intrinsic to design processes. If data modeling is seen as a design activity rather than description, then data modeling methods should be updated to reflect a design process and explicitly include creative thinking and comparative evaluation.

## 2. The ideal type of ‘design’

Design is the ideal type against which we measure data modeling. Its essence has been synthesized in the form of a list of some of the important characteristics of design problems and solutions, and the design process itself. These characteristics are intended to typify design and thus to differentiate it from description.

The list is not exhaustive, and the characteristics are interrelated. Collectively, they provide an overall picture of design. The characteristics (shown in Table 1) were grouped into fourteen properties within three dimensions – Problems, Solutions (i.e., Products), and Process, following Lawson’s [1] properties of design

## 3. Research design

The framework provides a basis for expanding the research question to 11 research sub-questions (RSQs) (see Table 2). Scope seeks to clarify what practitioners mean by data modeling. The remaining three dimensions determine whether data modeling practice has the properties of the design type: Problem deals with the negotiability of data modeling requirements, Process examines whether data modeling is creative, and Product deals with the diversity in data models produced by experienced practitioners in response to a task; this suggests that data modeling is a design process.

<table><tr><td>Lawson&#x27;s properties of design.</td></tr><tr><td>Design problems</td></tr><tr><td>1. Design problems cannot be comprehensively stated</td></tr><tr><td>2. Design problems require subjective interpretation</td></tr><tr><td>3. Design problems tend to be organized hierarchically</td></tr><tr><td>The design process</td></tr><tr><td>1. The process is endless</td></tr><tr><td>2. There is no infallibly correct process</td></tr><tr><td>3. The process involves finding as well as solving problems (including creativity)</td></tr><tr><td>4. Design inevitably involves subjective value judgments</td></tr><tr><td>5. Design is a prescriptive activity</td></tr><tr><td>6. Designers work in the context of a need for action</td></tr><tr><td>Design solutions</td></tr><tr><td>1. There are [sic] an inexhaustible number of different solutions</td></tr><tr><td>2. There are no optimal solutions to design problems</td></tr><tr><td>3. Design solutions are often holistic responses</td></tr><tr><td>4. Design solutions are a contribution to knowledge</td></tr><tr><td>5. Design solutions are parts of other design problems</td></tr></table>

The RSQs were addressed with a combination of surveys, laboratory studies, and interviews. The selection of the mode for each is shown in Table 3. Semi-structured interviews (with influencers of practitioners or thought leaders), surveys (to collect the perceptions of experienced data modelers about data modeling products, processes, and problems), and laboratory studies (designed to explore diversity and style in data models by asking participants to complete modeling tasks which were examined for evidence of diversity, style, and patterns in data modeling) were chosen to provide multiple sources of data to assess the practice of data model against the ideal type of design.

The surveys and laboratory studies were incorporated into 12 data modeling seminars and workshops for experienced practitioners delivered by the first author in the US, UK, Scandinavia and Australia between May 2002 and November 2004 (see Appendix A for summary of participants). Figs. 1–4 summarize the responses to demographic questions.

There was a strong correlation between the two experience measures (g = 0.65, p < 0.0005). Our study was the largest currently published; it included 381 participants with at least one year of data modeling experience. The minimum number to complete any task was 55. Three other groups participated in the research. The Practitioner thought-leaders and expert model evaluators were purposive samples. Architects and accountants (who provided a benchmark for the Characteristics of Data Modeling component) were recruited from personal and professional contact lists.

Research sub-questions (RSQs).

<table><tr><td>Type dimension</td><td>Name</td><td>Research sub-question</td></tr><tr><td rowspan="3">General – applying to all three dimensions</td><td>Scope</td><td>(RSQ1) What do data modeling practitioners believe is the scope and role of data modeling within the database design process?</td></tr><tr><td>Importance</td><td>(RSQ2) Is the description/design question considered important by data modeling practitioners?</td></tr><tr><td>Espoused Beliefs</td><td>(RSQ3) What are the (espoused) beliefs of data modeling practitioners on the description/design question?</td></tr><tr><td rowspan="3">Problem Process</td><td>Perception of Problems</td><td>(RSQ4) Are data modeling problems perceived as design problems by data modeling practitioners?</td></tr><tr><td>Methods</td><td>(RSQ5) Do database design methods used in practice support a descriptive or design characterization of data modeling?</td></tr><tr><td>Perception of Processes</td><td>(RSQ6) Are data modeling processes perceived as design processes by data modeling practitioners?</td></tr><tr><td rowspan="5">Product</td><td>Perception of Products</td><td>(RSQ7) Are data modeling products perceived as design products by data modeling practitioners?</td></tr><tr><td>Diversity in Conceptual Modeling</td><td>(RSQ8) Will different data modeling practitioners produce different conceptual data models for the same scenario?</td></tr><tr><td>Diversity in Logical Modeling</td><td>(RSQ9) Will different data modeling practitioners produce different logical data models from the same conceptual model?</td></tr><tr><td>Patterns</td><td>(RSQ10) Do data modeling practitioners use patterns when developing models?</td></tr><tr><td>Style</td><td>(RSQ11) Do data modeling practitioners exhibit personal styles that can be identified in the data models that they create?</td></tr></table>

Table 3  
Research methods used.

<table><tr><td>Research component</td><td>Method</td><td>Sub-questions addressed (listed by name)</td></tr><tr><td>Interviews with thought-leaders</td><td>Interviews</td><td>Importance (RSQ2), Espoused Beliefs (RSQ3), Perception of Problems (RSQ4), Perception of Processes (RSQ6), Perception of Products (RSQ7)</td></tr><tr><td>Scope and stages</td><td>Survey</td><td>Scope (RSQ1), Methods (RSQ5)</td></tr><tr><td>Espoused positions on data modeling</td><td>Survey</td><td>Importance (RSQ2), Espoused Beliefs (RSQ3)</td></tr><tr><td>Characteristics of data modeling</td><td>Survey</td><td>Perception of Problems (RSQ4), Perception of Processes (RSQ6), Perception of Products (RSQ7)</td></tr><tr><td>Diversity in conceptual modeling</td><td>Laboratory study</td><td>Diversity in Conceptual Modeling (RSQ8), Style (RSQ11)</td></tr><tr><td>Diversity in logical modeling</td><td>Laboratory study</td><td>Diversity in Logical Modeling (RSQ9), Style (RSQ11)</td></tr><tr><td>Style in data modeling</td><td>Laboratory study</td><td>Style (RSQ11), Diversity in Conceptual Modeling (RSQ8), Diversity in Logical Modeling (RSQ9), Patterns (RSQ10)</td></tr></table>

## 4. Results

## 4.1. Interviews with thought leaders

Interviews were held with seventeen ‘‘thought leaders’’ (see Appendix B); they were conducted by the first author. These were used to confirm the currency of the research question and to clarify which aspects of the research would shed most light on the questions. All interviewees chose acknowledgment over anonymity. Interviewees were asked for their views on the research question and asked to comment on three aspects of the ideal type:

1. Whether the data modeler should challenge business requirements (Problem).

2. Whether data modeling is a creative activity (Process).

3. Whether data modeling problems have a single right answer (Product).

Analysis was based on videotape transcription and confirmation; organization of statements by common meanings; organization of meanings into themes, and then into the research framework; synthesis of views and positions; and participant review of the findings. Opinions on the research question, expressed directly and in discussion, varied widely and were summarized in Table 4. Positions were starkly articulated:

Occupation of Participants  
![](/api/attachments/AGRGWQUY/fulltext/images/7d711079495f4618afd3777488069022905dc1d69c8563c1523712462427f2df.jpg)  
Fig. 1. Occupation of participants.

![](/api/attachments/AGRGWQUY/fulltext/images/a97fcf71fb4a60c9a9d093a8a816357dd3fe0d9bf2fbe8b7c7baef98d8b98b92.jpg)  
Fig. 2. How participants learned

\- Data modeling is not a process of creation, it is a process of discovery.

\- Data modeling is certainly a descriptive activity, it’s not a design activity.

\- I believe rabidly and intensely that it’s a design process.

\- We’re designing (but) some of the people that we work with see us as scribes.

## 4.1.1. Problem: are business requirements negotiable?

Proponents of the design characterization answered that business requirements were negotiable, and that modelers should be active in exposing new ways of doing business. One view was that the business does not know what is best for it. Modelers were seen as being able to make suggestions, and to bring in their own business knowledge to provide new perspectives.

Interviewees favoring the description characterization supported the primacy of the business in determining its data model and the danger of the modeler taking that role: ‘‘What we’re modeling is what the domain expert says is right’

## 4.1.2. Process: is data modeling a creative activity?

Proponents of design believed that they were ‘‘creating’’ the objects in the model: ‘‘10–15% of entities are obvious and everyone agrees with them, but (beyond that) the actual choice of entities requires a lot of imagination and creativity.’

Some supporters of the description characterization recognized a role for creativity in peripheral areas like the layout and presentation of the model, or in the way of understanding the business.

![](/api/attachments/AGRGWQUY/fulltext/images/b03598de743db5759d30a724c63e8bc14d9382ea924759f06226f9ed1e37ec0a.jpg)  
Fig. 3. Experience: number of models.

![](/api/attachments/AGRGWQUY/fulltext/images/caecf8a26ee560d2aa348e84f4aa32290244a2065cfb433979a3a320239c5351.jpg)  
Fig. 4. Experience: years

Table 4  
Interviewees’ overall positions.

<table><tr><td>Position</td><td>Number of interviewees</td></tr><tr><td>Strongly supports description</td><td>5</td></tr><tr><td>Somewhat supports description</td><td>1</td></tr><tr><td>Supports neither position more strongly than the other</td><td>3</td></tr><tr><td>Position depends on modeling formalism/language</td><td>1</td></tr><tr><td>Somewhat supports design</td><td>3</td></tr><tr><td>Strongly supports design</td><td>4</td></tr></table>

## 4.1.3. Product: one right answer?

This generated strongly conflicting responses. Some who believed that requirements were negotiable were less sure that the models would vary once requirements were settled. Some held that there is a right model, allowing for variation only in notation and the naming of objects.

Those who saw differences because modeling was design spoke in terms of utility vs truth. A few raised the theoretical position of choice in classification, but most who argued against the one right answer drew on personal experience. Instructors noted that students produced different workable models in response to case study scenarios. The difficulty of integrating different databases within and across organizations was evidence that different workable models could be implemented for the same data.

The trade-off between level of generalization and enforcement of business rules was a central theme for those who believed in design. Three groups emerged: the literalists (concepts should be modeled as used in the business); the moderate abstractors (some generalizations) and the rule removers (deliberately removing business rules for representation elsewhere). Some saw these as stylistic preferences of modelers.

## 4.1.4. Summary

Thought leaders considered the question was important. Further, they were divided about whether they believed that data modeling was design or description. Their perceptions of whether the problems, processes, and products were best characterized as design or description also varied.

## 4.2. Survey: scope and stages

There were two reasons for this stage. We sought to determine what practitioners meant by data modeling before designing and interpreting survey questions, and sought responses about parts of the database design process to see whether they could individually be characterized as design or description.

Our questionnaire therefore asked participants to nominate the stages in database design, and map 26 elementary activities (such as normalization and definition of indexes) against the stages. The elementary activities served as common reference points for comparing the higher-level stages nominated by different participants. Participants were also asked to define data modeling in terms of the stages that it covered. Respondents were attendees at advanced data modeling classes in London (25) and Los Angeles (30). We found broad agreement on the scope, stages, and activities considered to be data modeling activities.

After consolidation of names, five stages accounted for 201 (83%) of the total of 243 activities cited: (1) Business Requirements Analysis; (2) Conceptual Data Modeling; (3) Logical Data Modeling; (4) Physical Data Modeling and/or Physical Database Design; and (5) Post-database-design Activities (optional). The two tasks in (4) were found to contain essentially the same activities. A stage simply named ‘‘Data Modeling’’ was listed on nine occasions and was in the same place in the sequence as ‘‘Logical Data

Modeling’’. Forty-one (75%) responses matched this overall pattern, and a further nine (16%) matched the pattern except for the omission of ‘‘Business Requirements Analysis’’.

Eighty percent of responses put the activities of data modeling and responsibilities of the data modeler as (at least) the specification of an initial conceptual schema, to meet agreed business requirements, prior to any modifications to improve performance. Thus there was a broad consensus on the overall composition and sequence of the database design process. The description/design debate was thus unlikely to be a consequence of different definitions of data modeling.

## 4.2.1. Questions measuring stages against the ideal type ‘Design

The data modeling scope and stages survey provided answers to the following questions.

Question 1 – Is a business requirements stage (not including entity, relationship, attribute identification) a necessary part? Including this stage prior to identifying key model components runs counter to the descriptive characterization when the UoD is mapped directly onto the data model. Requirements statements can be seen as problem statements to which the model provides a solution. A business requirements stage was nominated by 84% of our respondents of whom 46% saw it as the responsibility of the data modeler (solely or jointly); 65% the analyst and 39% the user.

Question 2 – Is entity/relationship/attribute identification part of the business requirements stage? If these are established before data modeling starts, then the data modeler cannot ‘‘create’’ them, and the description characterization is supported. Only 5% of respondents included identification of entities, relationships, and attributes in a business requirements stage.

Question 3 – Are there separate stages for DBMS-indepen dent (conceptual) modeling and DBMS-specific (logical) modeling? Data modeling can be seen as an implementationindependent descriptive stage followed by transformation to a logical data model, supporting the descriptive characterization. In contrast, designers are constantly conscious of the implementation environment or ‘‘medium’’. If data modeling is design, we would expect the two stages to blur and often combine. Respondents grouped most conceptual schema specification tasks into one stage, generally called Logical Data Modeling, with only entity and relationship identification being part of a Conceptual Data Modeling stage. Respondents effectively used the term conceptual modeling to describe a preliminary ‘‘sketch plan’’ and not a rigorous and complete product for mechanical translation into a conceptual schema. This is in line with practitioner terminology.

Question 4 – Where does view integration happen? In the descriptive characterization, where there is one right answer, view integration is relatively simple. In the design characterization, models may differ in complex ways and their integration becomes a process of negotiation. View development and integration was a median task in the sequence of the tasks classed as data modeling and it was considered ongoing rather than a discrete terminal task. No respondent nominated it as a discrete stage.

Question 5 – Where is external schema specification located and who is responsible? One approach to database design uses external schemas (views) to replicate user views. In the descriptive characterization, these are mappings from the conceptual schema that originally integrated them and the data modeler will be responsible for their definition. If, instead, external schemas are a tool for managing data independence, programming needs, and security rather than reproducing user views, we would expect them to be defined later in the process. This is indeed what we found and this activity was seen to be outside the primary responsibility of the data modeler.

## 4.2.2. Summary

In questions asked specifically about important aspects of the process that could illuminate whether data modeling is design or description, practitioners offered opinions that were consistent with the design type.

## 4.3. Survey: espoused positions on data modeling

We surveyed attendees at a one-day advanced data modeling seminar at an international practitioner convention in an attempt to determine their position on the description/design dichotomy by asking them two questions. We asked firstly, an open question: What is data modeling? and secondly, a closed question: Which better describes data modeling (a) Describing the data requirements of an organization or part of an organization? or (b) Designing data structures to meet the requirements of an organization or part of an organization? 93 respondents answered both questions. The questions were given after participants had completed a data modeling task developing a model from a business scenario. Participants were told: ‘‘We are referring to data modeling to support the development of a relational database; not enterprise data modeling or reverse-engineering’’. They were not shown the closed question until after they answered the open question.

Two researchers coded the responses neutral, somewhat, or strongly for the question depending on the level of support for either the design characterization (coded as 4 & 5) or the description characterization (coded as 1 & 2). The distribution of coded responses to the open question is shown in Fig. 5. Neutral was subdivided into both or neither (3 and 0 respectively). Inter-coder reliability (a) was 0.82 (0.7 was considered acceptable). Responses to the closed question are shown in Fig. 6. The word design (as a verb) was used in only six responses to the open question. Only 17% of responses to the open question did not embody a position. There was no significant correlation between responses and experience, method of learning, or job position.

Fig. 7 compared responses to the open and closed questions: the vertical axis shows the break-up of responses to the Closed Question for the participants who gave each of the possible (coded) responses to the Open Question. Thus, participants favoring the design characterization in the open question and mostly maintained that view in the closed question, but a significant number of participants whose open question answers supported description reversed it in the closed question: providing only a moderate correlation (<sub>K</sub> = 0.34, p = 0.007) between the open and closed questions when both and neither were excluded. This difference suggested that some responses to the open question may have been influenced by taught definitions of data modeling (which favor a description characterization) whilst the closed question demanded some reflection.

A facilitated discussion followed response collection. A show of hands reporting closed question answers caused surprise. The discussion which followed established that many participants had expected their own response to dominate. A second show of hands showed a close-to-unanimous view that the design/description distinction was real and important.

![](/api/attachments/AGRGWQUY/fulltext/images/74fd9ba38b5e81ea9bec668a7832bf745ca6ba100c36afabda3639d4db3ac238.jpg)  
Fig. 5. Coded responses to open question.

![](/api/attachments/AGRGWQUY/fulltext/images/1efe254ac1e2ae496e033a4db450ed6428e2930a8e28c2a2594b6a81f34952a6.jpg)  
Fig. 6. Responses to closed question.

![](/api/attachments/AGRGWQUY/fulltext/images/182b36a4a8c32fd81e5bfc412f094c42676614b4c39811f1f9228cd8d6d49164.jpg)  
Fig. 7. Source of responses to closed question.

## 4.3.1. Summary

Data modeling practitioners espouse beliefs that data modeling was description in response to the open question and were evenly split between description and design in response to the closed question. The practitioners confirmed that researching the design/ description dichotomy was of importance.

## 4.4. Survey: characteristics of data modeling

This part of our survey sought a deeper understanding of theory-in-use by addressing practitioners’ perceptions of characteristics of data modeling problems, products and processes to address RSQs 4, 7. The 25 questions shown in Appendix C used a five-point Likert scale.

The survey was benchmarked using architects and accountants. They were chosen because architecture is a design discipline whereas accounting is a process of recording, classifying, reporting and communicating, and is thus a descriptive characterization. Data modelers have been compared with both architects and accountants. Responses were received from a snowball sample of 38 accountants and 21 architects, all based in Australia. The results for these two professions were then used to benchmark the results for data modeling against them.

The survey was administered to 266 attendees at seven seminars targeting data modeling practitioners in the USA, Australia, UK, and Scandinavia (the smallest 20 and the largest 90). Participants were told, before completing the survey: ‘‘We are referring to data modeling to support the development of a relational database; not enterprise data modeling or reverse-engineering’’.

No significant differences were found in the results across the seminars. Scale reliability (Cronbach’s a) was 0.73. The Corrected Item-Total Correlation (CITC) was positive (showing that the questions were measuring the same underlying construct in the same direction) for all but one item. The exception was: ‘‘Data modeling is prescriptive rather than descriptive’’ – this had a CITC value of 0.15. Subsequent discussion has suggested that some respondents had interpreted ‘‘prescriptive’’ as applying to the modeling process rather than product (paradoxically supporting a descriptive characterization).

Table 5  
Summary of responses to the data modeling questionnaire

<table><tr><td>Design mean</td><td>Dimension</td><td>Property</td><td>Property mean</td></tr><tr><td rowspan="3">3.75 t(267)=31, p&lt;0.0005</td><td>A. Design problems mean=4.11 t(317)=37, p&lt;0.0005</td><td>1. Design problems cannot be comprehensively stated2. Design problems require subjective interpretation3. Design problems tend to be organized hierarchically</td><td>4.09 t(330)=31, p&lt;0.00054.08 t(335)=31, p&lt;0.00054.18 t(342)=24 p&lt;0.0005</td></tr><tr><td>B. Design products mean=3.60 t(302)=23, p&lt;0.0005</td><td>1. There are an inexhaustible number of different solutions2. There are no optimal solutions to design problems3. Design solutions are often holistic responses4. Design solutions are a contribution to knowledge</td><td>4.04 t(339)=23, p&lt;0.00053.90 t(340)=21, p&lt;0.00052.55 t(334)=-6.4, p&lt;0.00053.94 t(320)=19, p&lt;0.0005</td></tr><tr><td>C. The design process mean=3.49 t(299)=16, p&lt;0.0005</td><td>1. The process is endless2. There is no infallibly correct process3. The process involves finding as well as solving problems4. Design inevitably involves subjective value judgments5. Design is a prescriptive activity6. Designers work in the context of a need for action</td><td>4.00 t(342)=23, p&lt;0.00053.34 t(337)=4.9, p&lt;0.00054.00 t(341)=18, p&lt;0.00053.65 t(331)=10, p&lt;0.00052.66 t(323)=-6.7, p&lt;0.00053.35 t(337)=5.1, p&lt;0.0005</td></tr></table>

Table 5 shows the mean scores (maximum score of 5) for the survey, at the Property, Dimension, and Overall levels. The onesample t-test results indicated the significance of the difference between the mean and the neutral score of 3. Fig. 8 shows the frequency distribution of the Overall score, showing that most values were above the neutral value.

These results show that modeler-espoused characteristics fit a design characterization. Data modelers also scored significantly higher than accountants in all dimensions $( p < 0 . 0 1 )$ , and significantly higher than architects in the problem dimension $\left( p < 0 . 0 1 \right)$ and overall $\left( p = 0 . 0 2 \right)$ .

## 4.4.1. Summary

The results clearly showed that participants did perceive that the problems, products, and processes of data modeling fit the design ideal type.

## 4.5. Laboratory study: diversity in conceptual models

Our laboratory study examined product diversity in the conceptual data models developed by experienced data modelers for a real-world problem.

The task involved an effort to develop a conceptual model for a medical research database from a description of a real business requirement. Participants were attendees at an international (practitioner-oriented) data management conference in North America; they viewed a video of the project sponsor and data administrator describing the requirements, and were given a transcript of it (see Appendix D). Participants were then given 25 min to complete the task and a further 5 min to complete a questionnaire about the process. Ninety-three models were received. Forty-nine responded that they understood the problem fairly well or very well, did not find it very difficult, made no guesses or only trivial guesses and did not think their models would be much different if more time was allowed.

The first author judged 66 of the models to be workable; they were submitted by the more experienced (8.5 years vs 3.5 years;

![](/api/attachments/AGRGWQUY/fulltext/images/beb52620df5b769bdffaab71774a4ff2b451ec4536154e9705c22c7570d03a83.jpg)  
Fig. 8. Frequency distribution of overall score – 3 is neutral.

two-tailed $t ( 8 7 ) = 4 . 5 , \ p < 0 . 0 0 1 )$ who found the problem less difficult (difficulty 5-point Likert scale rating 2.6 vs 3.2; two tailed $t ( 8 9 ) = - 3 . 4 , p = 0 . 0 0 1$ ). 88% used some variant of the ‘‘crow’s foot’’ notation.

A reference set of standard entity names and definitions was synthesized to facilitate comparison of models.

## 4.5.1. Assessment of diversity

Seven measures of diversity were used. These are neither orthogonal nor exhaustive but are indicative of diversity.

Diversity measure no. 1 – Participants’ perceptions of difference: On completing their model, participants paired off and compared their models. One percent of participants perceived the models as identical, six percent as identical except for naming or agreed errors, 53% as structurally different in minor ways, and 40% as structurally different in important ways.

Diversity measure no. 2 – Number of entities: Fig. 9 shows the frequency distribution of entity counts from the models. Subtypes were excluded from the count to improve comparison with the 77% of models which did not use subtypes.

Diversity measure no. 3 – Variety of entity names: The 93 models had 291 different entity names after removing synonyms. In addition to unrecognized synonyms, it includes some homonyms. The different uses were evident through the context of relationships with other entities.

Diversity measure no. 4 – Use of nouns from the description: The frequency distribution of entity names matching nouns from the interview transcripts is shown in Fig. 10. Of the 291 different names given to entities, comparatively few came directly from the problem description but had been invented by the modeler.

Diversity measure no. 5 – Variability in construct use: One concept was represented in some models as an entity (52 times) and as a relationship (5 times) in others. Three concepts were shown in some models as entities and in others, explicitly or implicitly, as attributes. Correlation between the three decisions was negligible in two cases and weakly positive but not significant in the third $\left( \Phi = 0 . 1 4 , p = 0 . 2 \right)$

![](/api/attachments/AGRGWQUY/fulltext/images/c41250b3bda022c5d8becf2bd63cb52432472d55d3f12eadd932cc8056e71654.jpg)  
Fig. 9. Total number of entities in each model.

![](/api/attachments/AGRGWQUY/fulltext/images/6aa65cb7b9bce7197007d31933c04a3eedc89fbea93bd023857accba9d9b2e5f.jpg)  
Fig. 10. Number of entities corresponding to nouns in the problem description

Diversity measure no. 6 – Level of entity generalization: Three concepts were represented at different levels of generalization, though t here were significant correlations between the three generalization decisions suggesting that modelers bring personal styles to the generalization decision $( 0 . 4 2 \leq \gamma \leq 0 . 7 7 , p < 0 . 0 2 ) .$

Diversity measure no. 7 – Holistic difference (expert assessed): 19 experts assessed ten selected standardized models to assess the viability of their implementation. Standardization involved providing a common name for the same entities, removing entities outside the defined scope, and presenting the models in a common format. Diversity was supported if more than one model was judged as being practically viable. The expert modelers (with a minimum of 15 years experience), gave scores for the measures overall quality, understandability and flexibility on a 5- point Likert scale. The inter-rater reliability, measured by Cronbach’s a, was 0.92 for Overall Quality, 0.84 for understandability, and 0.73 for flexibility (0.7 would be considered acceptable) The level of understandability across all evaluators and models was 3.53 $( \sigma = 0 . 4 7 ) ,$ placing it between neither easy nor difficult to understand and reasonably easy to understand.

Fig. 11 shows, for each model, the number of experts who assessed overall quality as 3 (mid-point of the scale: application would work with no serious problems) or more, and the benchmark (experts who scored it equal to or higher than an average model that they would expect to encounter in their work, developed in the last ten years by someone other than themselves.) Thus, between three and five models were acceptable to the majority of these experts. Evaluators were also asked to nominate the best model overall; four different models were selected.

## 4.5.2. Summary

The results demonstrated a diversity of objectively assessed workable solutions to the same problem and answer RSQ8. The diversity observed was consistent with the design characterization.

## 4.6. Laboratory study: diversity in logical models

Our laboratory study also examined product diversity in the logical data models developed by experienced data modelers in a real-world problem.

![](/api/attachments/AGRGWQUY/fulltext/images/91fb96244de2d45ae0fd3ae85f57f34be7f6eec14fe11740a2570d28855480ac.jpg)  
Fig. 11. Model acceptability

The task involved developing a logical data model to serve as the specification for a relational database from a list of 22 attributes that the user wished to record for a real business application. The attributes were presented as a single table relation (see Appendix E). Participants were attendees at advanced data modeling seminars: for measures 1–4 these were attendees in London, U.K., and Pittsburg, U.S.A. (40 participants in total); for measure 5 the participants included a further 58 at two other seminars.

All but two of the models produced supported the data specified by the original table and were thus workable. All but three models were fully normalized. Straightforward assumptions were made about the columns in each table for the few solutions that did not provide a full list. Consistent application of these assumptions may have led to less diversity than if this task had been completed by the modelers themselves.

## 4.6.1. Diversity measures

Diversity measure no. 1 – Participants’ perceptions of difference: Participants paired off and compared models. No participant reported the two models as identical, nine percent reported the models as identical except for naming or agreed errors, 39% as structurally different in minor ways, and 52% as structurally different in important ways.

Diversity measure no. 2 – Number of tables: Fig. 12 shows the frequency distribution of table counts in the models.

Diversity measure no. 3 – Variety of table names: After consolidation of obvious synonyms, the 39 models contained 66 different table names.

Diversity measure no. 4 – Construct variability: The 39 models resulted in seven concepts being represented in more than one way: as tables in some models and in others as columns (see Appendix E).

Diversity measure no. 5 – Generalization: Examination of the models revealed five different generalizations: four produced a single column from two different attributes and one changed a column’s name to increase consistency with other columns (see Appendix E). A score was then calculated for each participant by totaling the number of decisions taken by the participant. Fig. 13 shows the frequency distribution of the scores.

With one exception, generalization scores were not significantly correlated with the standard demographic groupings or with responses to the process questions. The sole significant correlation was that participants who had developed more than one model in practice had significantly higher generalization scores.

## 4.6.2. Summary

The diversity in logical models is evident from the results (RSQ9.)

![](/api/attachments/AGRGWQUY/fulltext/images/270403ae5a19701b6744644393789a86953bbe764de3007ae44cc2b06e9c0c89.jpg)  
Fig. 12. Total number of tables in each model.

Table 8

![](/api/attachments/AGRGWQUY/fulltext/images/aad8901702e2b628d0337fc93941938c4b586ea3318c76dd0f1287bd108e4f03.jpg)  
Fig. 13. Frequency distribution of generalization scores.

## 4.7. Laboratory study: style in data modeling

Our laboratory study also examined whether by consistently favored higher or lower levels of generalization within and between models.

The task involved an effort to develop two models. As in the prior section generalization scores were calculated for each model. These were then used to determine the consistency of decisions within each model, and the correlation of the scores between the two models. Participants were attendees at advanced data modeling seminars in the USA (two seminars) and in Stockholm, Sweden: a total of 91 participants. Three modeling problems were used, with each participant being assigned two. Two of the problems required the development of a conceptual data model from a text description and one required the development of a logical data model (see Appendix F).

Models that omitted any of the constructs were excluded from analysis. Each identified construct in each model was coded according to the level of generalization using ‘0’ for lowest, ‘1’ for next-lowest, to the lowest level of generalization. A total generalization score was determined by adding the individual levels coded.

Four concepts in the Bank Loans and three concepts in the Family Tree solutions were identified as being subject to different levels of generalization. In each case, only two levels were found. With one exception, the decisions were logically independent. Appendix F contains the frequencies with which each decision was used. Recall from the previous section that there were five generalization decisions in the logical data-modeling task (see ‘‘diversity measure no. 5’’.).

Combinations of the decisions resulted in ten versions of the Bank Loans model and five versions of the Family Tree model, the most popular in each case accounted for 50% of the models. Tables 6 and 7 show the correlation between each pair of generalization decisions.

Covariance using the Kuder-Richardson 20 (KR20) coefficient was 0.80 for the Family Tree decisions, 0.75 for the Bank Loans decisions, and 0.68 for the logical data modeling task generalization decisions

Generalization scores for the Family Tree and Bank Loans models were moderately positively correlated. The gamma statistic $( \gamma = 0 . 6 9 , p < 0 . 0 0 0 5 )$ , showed a strong correlation. Thus, between model generalization correlation was supported for the two conceptual models. There was some correlation with demographic categories, so the analysis was repeated for each of them. Table 8 shows that the correlation remained moderate and significant $( p < 0 . 0 0 5 )$ within all but one group.

Table 6  
Bank loans generalization decisions.

<table><tr><td></td><td>Party</td><td>Party relationship</td><td>Transaction</td></tr><tr><td>Customer</td><td>0.77 (p&lt;0.0005)</td><td>0.58 (p&lt;0.0005)</td><td>0.27 (p=0.03)</td></tr><tr><td>Party</td><td></td><td>0.75 (p&lt;0.0005)</td><td>0.28 (p=0.03)</td></tr><tr><td>Party relationship</td><td></td><td></td><td>0.36 (p&lt;0.0005)</td></tr></table>

Table 7  
Family Tree generalization decisions.

<table><tr><td></td><td>Relationship</td><td>Parenthood</td></tr><tr><td>Person</td><td>0.39 (p&lt;0.0005)</td><td>0.37 (p&lt;0.0005)</td></tr><tr><td>Relationship</td><td></td><td>0.88 (p&lt;0.0005)</td></tr></table>

Correlation between generalization scores across the conceptual models.

<table><tr><td>Demographic group</td><td>γ</td><td>p</td></tr><tr><td>&gt;10 models produced</td><td>0.54</td><td>&lt;0.0005</td></tr><tr><td>≤10 models produced</td><td>0.27</td><td>0.32</td></tr><tr><td>Occupation = data modelers</td><td>0.52</td><td>&lt;0.0005</td></tr><tr><td>Occupation = non data modelers</td><td>0.62</td><td>0.001</td></tr><tr><td>&gt;6 years experience</td><td>0.56</td><td>0.001</td></tr><tr><td>&lt;6 years experience</td><td>0.49</td><td>0.003</td></tr><tr><td>Total sample</td><td>0.51</td><td>&lt;0.0005</td></tr></table>

No significant correlation was found between the generalization scores for the Annual Budget (logical) model and either the Family Tree or Bank Loans conceptual models (Family Tree: g = 0.26, $p = 0 . 4 6 ;$ Bank Loans: $\gamma = - 0 . 5 3 , p = 0 . 8 6 ) .$

## 4.7.1. Summary

Some modelers consistently choose higher (or lower) levels of generalization than others, within both conceptual and logical models and across conceptual models. This bias (or style) is not due to their level or experience (and, by implication, expertise). Consequently, RSQ9, was answered in the affirmative and thus supported the conclusion that the products of data modeling were influenced by differences in style of the practitioners that produce them.

## 5. Summary

Our findings were based on the four key dimensions of our design framework: general, problem, process and product. The general dimension includes scope, importance and beliefs. Data modeling was found to consist of the specification of the initial conceptual schema to meet the business requirements prior to any performance tuning (RSQ1). The research question was considered to be important (RSQ2). Data modeling practitioners were evenly divided between their belief that data modeling was design and description (RSQ3).

Data modeling problems were seen as having the characteristics of design problems by data modeling practitioners, significantly more so than architects and accountants (RSQ4). Data modelers generally worked from a problem statement rather than directly from observations of the UoD (RSQ4).

The data modeling process was perceived as having the characteristics of design processes, similar to the perceptions of architects and significantly more than the perceptions of accountants (RSQ6). Consistent with the design characterization, identification of entities, relationships, and attributes was not considered to be part of the business requirements analysis. Furthermore, there was no evidence of the widely advocated ‘‘view-definition, view-integration, view-reconstruction’’ sequence, which required that model differences can be reduced to reconcilable views (RSQ5).

Data modeling products were perceived to be design products by data modeling practitioners, significantly more than percep tions of accountants, and similar to perceptions of architects (RSQ7). Conceptual data models and logical data models developed in response to a common problem were found to have substantial diversity (RSQ8, RSQ9). Data modelers frequently re-used their own or other’s patterns, significantly more than architects. Experienced conceptual data modelers re-used patterns much more than less-experienced data modelers (RSQ10). A significant correlation was found between the levels of generalization of entities within and between conceptual data models developed by the same modeler. This suggested that personal style, evidenced by generalization decisions, affected the data models that modelers produce (RSQ11).

## 6. Discussion and conclusions

Answers to our research sub-questions suggested that: data modeling, while traditionally characterized as description, was better characterized as design based as it was practiced. We focused entirely on the design/description question and produced consistent evidence in favor of the design characterization.

For researchers, there are two implications. First, careful design of data modeling experiments that take into account the likelihood of alternative solutions is required. Second, generalization of the results of empirical studies that use students as participants is problematic, because design skills take time to develop.

Data modeling teachers should consider it as a design activity. Designing data modeling tasks by articulating a domain based on nouns and verbs that relate to the entity types and relationship types is a way to teach data modeling notation but it does not teach the practice of data modeling.

Practitioners should be aware that their method is more consistent with data modelling as a design activity. They should be aware that alternative data modeling solutions may be useful and need to be evaluated for quality as part of the process.

## Appendix A. Summary of participants

<table><tr><td>Location</td><td>Research component</td><td>Number</td><td>Response rate (%)</td></tr><tr><td rowspan="2">DAMA/Metadata Conference, San Antonio, TX, USA</td><td>Diversity in conceptual modeling</td><td>112</td><td>66%</td></tr><tr><td>Espoused positions on data modeling</td><td></td><td></td></tr><tr><td>DAMA Conference, London, UK</td><td>Diversity in logical modeling</td><td>17</td><td>85%</td></tr><tr><td>Enterprise Data Forum, Pittsburgh, PA, USA</td><td>Diversity in logical modeling</td><td>23</td><td>80%</td></tr><tr><td>DAMA /Metadata Conference, Orlando, FL, USA</td><td>Data modeling style</td><td>41</td><td>77%</td></tr><tr><td>DAMA Chapter Presentation, Portland, OR, USA</td><td>Characteristics of data modeling</td><td>54</td><td> $90\%^b$ </td></tr><tr><td>DAMA Chapter Presentation, Phoenix, AZ, USA</td><td>Characteristics of data modeling</td><td>28</td><td> $90\%^b$ </td></tr><tr><td>DAMA Chapter Presentation, Des Moines, IA, USA</td><td>Characteristics of data modeling</td><td>39</td><td> $90\%^b$ </td></tr><tr><td>IRM Data Modeling Workshop Stockholm, Sweden</td><td>Data modeling style and Diversity in logical modelinga</td><td>28</td><td> $70\%^b$ </td></tr><tr><td>IRM /DAMA Conference, Stockholm, Sweden</td><td>Characteristics of data modeling</td><td> $70^c$ </td><td> $90\%^b$ </td></tr><tr><td>DAMA Chapter Presentation, Sydney, Australia</td><td>Characteristics of data modeling</td><td>20</td><td> $90\%^b$ </td></tr><tr><td>DAMA/Data Quality Conference, London, UK</td><td>Characteristics of data modeling Scope and stages</td><td>25</td><td>83%</td></tr><tr><td rowspan="3">Wilshire Conferences Data Modeling Masterclass, Los Angeles, CA, USA</td><td>Characteristics of data modeling;</td><td>30</td><td>86%</td></tr><tr><td>Scope and stages</td><td>459</td><td>75%</td></tr><tr><td>Data modeling style and Diversity in Logical Modelinga</td><td></td><td></td></tr></table>

<sup>a</sup> The Diversity in Logical Modeling task was incorporated in the Data Modeling Style task in these two locations.  
<sup>b</sup> Estimate – exact attendee numbers not available.  
<sup>c</sup> This group included 28 who attended the previous item.

## Appendix B. List of participants in the thought leaders interviews

The participants, and their positions or roles at the time of interview were:

\- Peter Aiken, data management consultant, Associate Professor at Virginia Commonwealth University.

\- Richard Barker, company director, architect of the Oracle CASE tool.

\- Michael Brackett, President of the International Data Management Association.

\- Harry Ellis, data modeling consultant to the British Department of Defence.

\- Larry English, leading proponent of data quality techniques.

\- Terry Halpin, Professor at Northface University Utah.

\- David Hay, independent data modeling consultant and educator.

\- Steve Hoberman, global reference data manager with Mars, Inc.

\- Karen Lopez, data modeling consultant and commentator.

\- Dawn Michels, data modeling specialist, Vice President of Chapter Services for DAMA International.

\- Terry Moriarty, president of Inastrol data modeling consultancy.

\- Ronald Ross, editor of the Database Newsletter for 22 years.

\- Robert Seiner, data management consultant.

\- Alec Sharp, independent data and process modeling consultant.

\- Len Silverston, data modeling consultant, industry educator.

\- Eskil Swende, Chief Executive of the IRM group. President of the Scandinavian chapter of the Data Management Association.

\- John Zachman, industry consultant and educator.

Appendix C. Survey questions – perceptions of characteristics of data modeling Properties of design organized as a set of questions.

<table><tr><td>Design</td><td>Dimension</td><td>Property</td><td>Additional survey question</td></tr><tr><td rowspan="3">Overall</td><td>A. Design problems</td><td>1. Problems cannot be comprehensively stated2. Problems require subjective interpretation3. Problems tend to be organized hierarchically</td><td>2. Data modeling problems are often full of uncertainties about objectives and relative priorities3. Many requirements do not emerge until some attempt has been made at developing a model4. Objectives and priorities are likely to change during the modeling process5. In establishing requirements for a data model, something that seems important to one data modeler may not seem important to another data modeler6. In establishing requirements for a data model, something that seems important to one business stakeholder may not seem important to another business stakeholder7. Modeling problems are often symptoms of higher level problems</td></tr><tr><td>B. Design products</td><td>1. There are an inexhaustible number of different solutions2. There are no optimal solutions to design problems3. Design solutions are often holistic responses4. Design solutions are a contribution to knowledge</td><td>9. Most data modeling problems do not have a single correct solution10. In most practical business situations, there is a wide range of possible (and workable) data models11. Data modeling almost invariably involves compromise12. Data modelers will almost invariably appear wrong in some ways to some people13. It is not usually possible to dissect a data model and identify which piece of the model supports each piece of the business requirements14. I frequently re-use patterns (structures) from other data models that I have developed myself15. I frequently re-use patterns (structures) that I have seen in models developed by others</td></tr><tr><td>C. The design process</td><td>1. The process is endless2. There is no infallibly correct process3. The process involves finding as well as solving problems4. Design inevitably involves subjective value judgments5. Design is a prescriptive activity6. Designers work in the context of a need for action</td><td>17. Identifying the end of the data modeling process (i.e. when to stop modeling) requires experience and judgment16. There is no infallible correct process that (if properly followed) will always produce a sound data model21. Data modeling requires a high level of creative thinking23. I find it difficult to remain dispassionate and detached in my data modeling work24. Data modeling is prescriptive rather than descriptive25. The final data model is often a result of compromise decisions made on the basis of inadequate information</td></tr></table>

The 19 Characteristics at the lowest level were derived from concepts in the descriptions of the Properties, and were operationalized as questions that could be scored on a Likert scale (the numbers, complete with gaps in the sequence, are the numbers of the corresponding questions in the resulting questionnaire). Scores were computed by taking the mean to provide a score for the higher level Property. Then the Property scores were computed to provide Problem, Product, and Process scores, and ultimately an overall Design score.

There was some subjectivity in the identification of these concepts and the framing of the questions. There was no question addressing the Property (of design products) Design solutions are parts of other design problems. This Property proved difficult to communicate in a simple question or questions and after pilot testing it was excluded. In all, six questions addressed problem, seven addressed product, and six addressed process.

Five further questions were added based on other differences between description and design. These were classified under their relevant dimensions.

Questions added to characteristics of data modeling survey.

<table><tr><td>Additional survey question</td><td>Dimension</td></tr><tr><td>8. Business requirements are often negotiable</td><td>Problem</td></tr><tr><td>18. When I am developing a data model, I sometimes produce more than one workable solution, and then choose the best one</td><td>Process</td></tr><tr><td>19. I often start modeling before I have a thorough understanding of business requirements</td><td>Process</td></tr><tr><td>20. Sometimes, even when I understand the business requirements, I find it difficult to produce a data model</td><td>Process</td></tr><tr><td>22. I have experienced “eureka” moments (sudden and dramatic insights or solutions to problems) in my data modeling work</td><td>Process</td></tr></table>

A further question was added as Question 1 in the survey to determine whether the most difficult part of data modeling was in understanding the business requirements. It served three purposes:

(1) To answer the question: are requirements fixed or negotiable? If requirements are negotiable, but perceived as fixed by some modelers (or vice versa), we would expect those modelers to find the task difficult.

(2) To determine whether perceived difficulty in understanding requirements correlated with other indicators of design. Incompleteness, subjectivity, and negotiability of requirements are cited as properties of design; if the task is essentially descriptive, then gaining an understanding of it is the central (and most difficult) task.

(3) In eliciting a deeper understanding of either description or design positions, to reduce the possibility that respondents would recognize the dichotomy behind their questions and answer. The question did not signal the dichotomy. It was placed first on the questionnaire.

The model was developed specifically for our research, in the absence of established measures for differentiating description and design activities. We were obliged to rely solely on the soundness of the underlying theory (and on its operationalization) when drawing conclusions from the results.

Questions were adapted, through minor re-wording, to enable them to be used with two other professional groups, viz. architects and accountants. The two groups were chosen because:

(1) Architecture is generally recognized as a design discipline and is frequently employed as a metaphor for IS tasks and deliverables.

(2) Accounting is a process of recording, classifying, reporting and communicating, a definition consistent with the descriptive paradigm. Data modelers have in fact been compared with accountants: ‘‘Just as an accountant might use a financial model, the analyst can develop an entity model’’.

To encourage a focus on common tasks, the accountants questions were framed in the context of preparing a set of accounts for a business and the architects’ questions in the context of designing a building.

## Appendix DLaboratory materials – diversity in conceptual modeling

The problem to be analyzed was presented to the participant in three parts:

(1) A videotaped description of the business requirements as recorded by the project director and also by the manager responsible for managing the production system. The two stakeholders were responding independently to our request to tell us about a project and the data that was needed to run it.

(2) A verbatim transcript of the videotape (see below), with a short glossary of terms added by the author in consultation with the project director.

(3) A list of questionnaires to be used for data collection, with excerpts from two questionnaires.

A couple of the other problems we have are the need for a central identification number that we need to generate: we can’t use (for instance) a Medicare number or social security number because of privacy issues. Another one of the problems that we have is that a lot of these surveys are used multiple times – two, sometimes three times. So it’s the ability to be able to collect data on the third survey, linking it up with the same patient that we used for the first survey.

So if you were to participate in the study, you would come into your ante-natal visit and with the help of staff fill out (say) four or five questionnaires asking you about your mood and how you’re feeling. You would then answer the same questionnaires again at your post-natal visit, and the reason we have the same questionnaires again is just to see how the mood and the response has changed over a period of time.

Instructions and a set of ‘‘process’’ questions addressing assumptions, level of difficulty and use of patterns (common to all modeling exercises used in our research) were added to the standard demographics questionnaire.

## Appendix ELaboratory materials – diversity in logical modeling

The task was to produce a logical model based on the conceptual model (see Fig. E1). The logical model needed to be a workable specification for a database: a single table/relation is needed so that data can be stored: it is already normalized. The quarterly items are not repeating groups; they are different items with different names and meanings.

The task and associated questionnaire were administered to 96 attendees at four advanced data modeling seminars. For some of the measures of diversity, only the 39 responses from London (a substantial European conference) and Pittsburgh (a substantial North American conference) were included.

The last three concepts in Table E1 did not directly reflect columns in the original model but were added by modelers to capture semantics lost when generalizing some of the original columns. Ignoring differing levels of generalization and considering only the choices of representing each concept as either a column or table resulted in 19 distinct models.

There were five situations in which some participants had:

(a) explicitly generalized two or more of the attributes in the original model to produce a single column, e.g. Generalizing Budget First Quarter Material, Budget Second Quarter Material, Budget Third Quarter Material and Budget Last Quarter Material into a single column Quarterly Material Budget plus a Quarter Number column to identify which quarter the amount applied to (Decision 1 in Table E2).or

(b) Altered columns to increase consistency: e.g. Replacing Actual Total Material with Actual Fourth Quarter Material (Decision 5 in Table E2) to make it consistent with the representation of budgeted amounts and comparable with the other (quarterly) actual material amounts. Although these decisions are not manifested as generalizations, they are based on the recognition of commonality, and thus have been treated together with the explicit generalizations.

Table E2 shows the five situations and the different decisions made by participants.

Fig. E2 shows the frequency distribution of the decisions.

Nineteen of the 22 modelers who generalized Budget and Actual amounts (Gen BA) also made the other four generalizations and this covariance amongst the decisions was supported by a Kuder-Richardson 20 (KR20) statistic of 0.68. Apparently this modeler had an underlying concept of propensity to generalize on the part of the modeler. Correlations between individual decisions (f) ranged from negligible to strong, and were positive in all cases.

<table><tr><td>Department Number (Primary key item)</td><td>Budget-First-Quarter-Labor</td></tr><tr><td>Year (Primary key item)</td><td>Budget-Second-Quarter-Labor</td></tr><tr><td>Approved-By</td><td>Budget-Third-Quarter-Labor</td></tr><tr><td>Budget-First-Quarter-Material</td><td>Budget-Last-Quarter-Labor</td></tr><tr><td>Budget-Second-Quarter-Material</td><td>Actual-First-Quarter-Labor</td></tr><tr><td>Budget-Third-Quarter-Material</td><td>Actual-Second-Quarter-Labor</td></tr><tr><td>Budget-Last-Quarter-Material</td><td>Actual-Third-Quarter-Labor</td></tr><tr><td>Actual-First-Quarter-Material</td><td>Actual-Total-Labor</td></tr><tr><td>Actual-Second-Quarter-Material</td><td>Budget-Other</td></tr><tr><td>Actual-Third-Quarter-Material</td><td>Actual-Other</td></tr><tr><td>Actual-Total-Material</td><td>Discretionary-Spending-Limit</td></tr></table>

Fig. E1. Annual Budget conceptual model.

Table E1  
Alternative representations of concepts.

<table><tr><td>Concept</td><td>Not present</td><td>As column</td><td>Literal table</td><td>Generalized table (in scope)</td><td>Generalized table (beyond scope)</td><td>Total</td></tr><tr><td>Approved by</td><td>0</td><td>13</td><td>7</td><td>1</td><td>18</td><td>39</td></tr><tr><td>Department</td><td>0</td><td>4</td><td>34</td><td>1</td><td>0</td><td>39</td></tr><tr><td>Disc spending limit</td><td>0</td><td>27</td><td>12</td><td>0</td><td>0</td><td>39</td></tr><tr><td>Year</td><td>0</td><td>26</td><td>6</td><td>7</td><td>0</td><td>39</td></tr><tr><td>LMO-type</td><td>14</td><td>7</td><td>18</td><td>0</td><td>0</td><td>39</td></tr><tr><td>Quarter</td><td>10</td><td>13</td><td>8</td><td>7</td><td>1</td><td>39</td></tr><tr><td>BA-type</td><td>28</td><td>7</td><td>4</td><td>0</td><td>0</td><td>39</td></tr></table>

Table E2  
Generalization choices in the logical data models.

<table><tr><td>Decision number</td><td>Decision name</td><td>Yes</td><td>No</td><td>Both</td></tr><tr><td>1</td><td>Gen QTR (generalization decision)</td><td>Quarterly amount columns generalized – no columns specific to a particular quarter.</td><td>Columns for individual quarters</td><td>N/A</td></tr><tr><td>2</td><td>Gen LMO (generalization decision)</td><td>Labor, material, other generalized – no columns specific to a particular type</td><td>Specific columns for Labor, Material, Other amounts</td><td>N/A</td></tr><tr><td>3</td><td>Gen BA (generalization decision)</td><td>Budget and actual columns generalized – no columns specific to a particular type.</td><td>Specific Columns for Budget and Actual amounts</td><td>N/A</td></tr><tr><td>4</td><td>Other QTR (consistency decision)</td><td>Support for quarterly values for “Other” amounts – no column for annual amount</td><td>Support only for annual values for Other amounts</td><td>Both options supported</td></tr><tr><td>5</td><td>Fourth QTR LM (consistency decision)</td><td>Direct representation of fourth quarter labor and material actual amounts</td><td>Annual totals held for Labor and Material Actual amounts</td><td>N/A</td></tr></table>

![](/api/attachments/AGRGWQUY/fulltext/images/e55b12f133ab1bcf0259eef14868252167090ba398cdb6fac2916d06c552fef3.jpg)  
Fig. E2. Frequency of design options.

## Appendix F Laboratory materials – style in data modeling

Three data modeling problems were used in this research component.

The Annual Budget problem: participants were presented with a conceptual model and some supporting information, and asked to produce a logical data model (the model shown in Appendix E).

A Bank Loans problem: a simplified version of a real example, presented as a short plain-language description written by the author.

A Family Tree problem: it included the concept of marriage, presented as short plain-language description written by the author.

Bank loans data modeling problem.

To support the business of a bank, we need to record details of personal loans, housing loans and motor vehicle finance loans. Against each loan, we need to record the details of the borrower(s), the Loan Officer who approved the loan, and (in some cases) a guarantor. We also need to record payments, drawings (initial and further borrowings) and interest transactions against each loan.

Family tree data modeling problem.

## Family tree

We are developing a database to record details of a family tree. For each person of interest to us, we need to be able to record details (where known) of their mother, father, children, and marriages, and their date of birth, death and marriages

![](/api/attachments/AGRGWQUY/fulltext/images/895466d6b2e0ce7613a7b1f8117b471c90ccccb6a5945d0206d49a2f2f5d2349.jpg)  
Fig. F1. Bank Loans generalization decisions.

Frequency of Design Options  
![](/api/attachments/AGRGWQUY/fulltext/images/47d13f8179a20aaee675af47759f035c81f7cf5463d267be15f7c87192744a50.jpg)  
Fig. F2. Family Tree generalization decisions.

Figs. F1 and F2 show the frequency with which each generalization option was used in the two models.

## References

[1] B. Lawson, How Designers Think: The Design Process Demystified, 4th ed., Architectural Press, Oxford, 2005.

[2] S.K. Milton, E. Kazmierczak, An ontology of data modelling languages: a study using a common-sense realistic ontology, Journal of Database Management 15 (2), 2004, pp. 19–38.

[3] Y. Wand, R. Weber, Research commentary: information systems and conceptual modeling: a research agenda, Information Systems Research 13 (4), 2002, pp. 363–376.

![](/api/attachments/AGRGWQUY/fulltext/images/de6b0b0c5f2c9095bd28a0e577b67883c301f2374c978d4f84b23065d8c455f1.jpg)

Graeme Simsion is an Information Systems Consultant, Educator, and Researcher. For 20 years he was CEO of a business and information systems consultancy with offices in three Australian cities. His PhD from The University of Melbourne examined attitudes and practices of data modeling practitioners. He is the author of Data Modeling Essentials, one of the mos widely used practitioner texts on the subject, Data Modeling Theory and Practice, and numerous academic and practitioner articles, and is a regular speaker at industry and academic forums. His current focus is on improving the consulting skills of business and information systems professionals.

![](/api/attachments/AGRGWQUY/fulltext/images/2a88b645462d0b65959a3a9097f371bbdaad9b4e53c7a456f9f41399048200f6.jpg)

Simon Milton is a Senior Lecturer in the Department of Computing and Information Systems at The University of Melbourne, and received his PhD from The University of Tasmania in which he reported the first comprehen sive analysis of data modeling languages using a common-sense realistic ontology. Dr Milton continues his interest in the ontological foundations and practice of data modeling. He is also interested in the value and use of ontologies for business and biomedicine.

![](/api/attachments/AGRGWQUY/fulltext/images/f0c1e4f72670cf2a5607eb0bd78fd9c2da79e82792ff90276fe4ceccbf203379.jpg)

Graeme Shanks is an AustralianProfessorialFellow in the Department of Computing and Information Systems at The University of Melbourne. He received his PhD from Monash University. His research interests focus on the management and impact of information systems, business analytics, data quality and conceptual modeling. Graeme has published in journals including MIS Quarterly, Journal of Information Technology, Information Systems Journal, Information & Management, Journal of the AIS, Electronic Commerce Research, Journal of Strategic Information Systems, Information Systems, Behaviour and Information Technology, Communications of the AIS, Communications of the ACM, and Requirements Engineering.
