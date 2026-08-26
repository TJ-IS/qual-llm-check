---
otero_id: 23029
otero_key: "F3REZ9UC"
title: "The effect of graphic style on data model interpretation"
authors: "J. C. Nordbotten; M. E. Crosby"
year: "1999"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.1999.00052.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effect of graphic style on data model interpretation

J.C. Nordbotten & M.E. Crosby\*

Department of Information Science, University of Bergen, N-5020 Bergen, Norway, email: Joan@ifi.uib.no, and \*Department of Information and Computer Science, University of Hawaii at Manoa, Honolulu, HI 96822, USA, email: crosby@uhics.ics.hawaii.edu

Abstract. Graphic data models are commonly used as a tool for presentation of information structures in the design, implementation, use and maintenance of the databases that support information systems. The methods proposed for database design assume that the use of graphic data models will enhance understanding of system specifications by both the end-users and the implementers of the system. For this assumption to hold, the information presented in the graphic data model must be readily comprehensible so that the design, represented by the model, can be confirmed and implemented correctly. The lack of standard representations for graphic models has led to a variety of graphic styles. To date, there has been little focus on studying the effect graphic style has on model comprehension. We have studied the effect of three graphic styles proposed for data models on model legibility and interpretation. Our study shows a significant variation in model interpretation that can be attributed to the graphic syntax used. Graphic style appears to influence which model elements are included in the interpretation, as well as the way data models are read.

Keywords: Data model comprehension, graphic data models, graphic model legibility, graphic style

## INTRODUCTION

In the early 1980s, IFIP's Work Group 8.1 hosted a series of conferences about information system design methodologies in which it became clear that ‘practically all of the methodologies used in practice today employ a graphical description technique to depict activities, processes, flows, data objects, relationships, and whatever modelling concepts are advocated in specifying information systems.’ (Bubenko, 1986).

Bubenko also noted that the information system design community ‘appears to assume that users have great difficulties in understanding anything else than graphical descriptions.’

The situation is similar today. Most information system design methodologies rely heavily on graphical modelling for the presentation of system specifications. The lack of graphic syntax standards implies a continued assumption that any graphic syntax will be legible.

Information systems have two major components: an information archive (database) and multiple information processing applications (user programs). During database design, graphic data models are used to specify the information objects, their attributes, interrelationships, and the constraints required by the application system. The use of graphic data models is intended to facilitate communication between the system designer and the user(s) and system implementers. When the design, with its graphic data model, has been confirmed by the system owner/user, it then forms the basis for database implementation.

Although it is generally assumed that graphical presentation improves comprehension, it has been shown that graphic displays, showing relationships between objects, are not easily understood. Only 21% of young adults (21–25 years) were found to be proficient at locating and using information contained in maps, tables or charts (Gillespie, 1993). A study of the errors made by young students (12–14 years) asked to interpret Cartesian graphs found that half of the error types were caused by graphic presentation characteristics, such as domain specification, language wording, graph appearance, graph concepts and/or graphic syntax (Preece, 1983). Studies of graphic model comprehension indicate that the ability to interpret the graphical language used is a skill that requires learning. In particular, novice readers have problems locating and focusing on essential parts of the graph (Petre, 1995).

Several studies have been carried out on the effectiveness of graphic representations of processes on programmer interpretation of system specifications under the hypothesis that presentation formats affect comprehension (Wright & Reid, 1973, Brooke & Duncan, 1980). An experiment that presented programmers with design specifications in three spatial formats – sequential, hierarchical and branching flow charts – indicated that the branching spatial arrangement combined with a succinct program design language significantly facilitated design interpretation (Sheppard et al., 1982). However, a comparison between textual and graphical presentations of three-level nested program structures concluded that graphic presentations were not necessarily more accessible, comprehensible or memorable than textual presentations (Petre, 1995).

Experiments comparing tabular vs. graphical data models indicate that the graphical models can be easier to comprehend (Kim & March, 1995). Kim further studied two groups of system designers, each trained in one of two data modelling procedures, with their accompanying graphic data models, NIAM (Nijssen & Halpin, 1989) and EER (Teorey et al., 1986) respectively. He found that the model styles had no significant impact on the designer's ability to construct data models, detect errors, or comprehend a given model (Kim, 1995). One explanation of these findings could be that the graphic styles used for these model types have similar complexity.

Our interest has been focused on data model legibility, rather than the process of data model construction. We have studied the effect of the graphic style on model comprehension by data model readers, in particular end-users who will confirm the correctness of the model and/or implementers of a database system based on the data model. We have observed significant variation in model interpretation that can be attributed to the graphic style used. Graphic style appears to influence which model elements are included in the interpretation as well as the reading strategy used. We also observed that training in one data model type does not assure correct interpretation of comparable concepts presented in another syntactical representation.

## AN EXPERIMENT IN GRAPHIC DATA MODEL INTERPRETATION

Data models are used to describe the information/data required by an information system. Typically, a graphic data model depicts information objects, object attributes, interobject relationships and system constraints. For correct system interpretation and implementation, all model components must be seen and comprehended.

Different data model types use varying graphic symbols for presentation of data model concepts. The number and type of graphic symbols chosen give a distinct graphic style to data models of a specific type. Experience indicates that graphic models are not easy to comprehend. The question arises of the effect that graphic symbols and model style have on model legibility. As errors in model interpretation are frequently omission errors, we have focused our study on identifying model components that are not seen, or are misinterpreted. We have also studied how graphic style affects the way in which data models are read.

The hypotheses tested in our experiment include:

\- Graphic style affects data model legibility by influencing which model components are seen during interpretation.

● Graphic style affects the reading strategy chosen for data model interpretation.

● Skill level of data model interpreters affects how a graphic data model is read.

## Three graphic styles

In graphic data models, area symbols (rectangles, ellipses or diamonds) are commonly used for object and relationship type specifications. Relationship arcs may contain a graphic symbol within which relationship characteristics, such as name, attributes, and/or constraints, are placed. The line-end notation of an arc typically indicates a cardinality constraint associated with the relationship. Annotations, giving more detailed constraint specification, such as primary key attributes, domain constraints and subclass specification, can be placed near/in the node or on the arc.

Figure 1a–d shows four data models for a project administration application. These models are presented in the syntax of NIAM (Nijssen, 1989), SSM (Nordbotten, 1993), OODM (Cattell, 1991) and IDEF1X (Loomis, 1986). The graphic notation variation used for specification of relationships is perhaps the most pronounced difference in these data models, see the StaffedBy/WorksOn relationship between Project and Person. Note that the graphic syntax used gives the data models distinctive graphic styles.

Model complexity increases with the use of embedded symbols and distinct graphic symbols, such that the SSM model is least complex, followed by the OODM and NIAM model types. One can classify the graphic styles proposed for different data model types as:

\- highly graphic, characterized by encapsulation of each information element type in a graphic symbol which can then be annotated externally and/or internally, e.g. the project title specification given in Figure 1a.

![](/api/attachments/F3REZ9UC/fulltext/images/433564c2845ed381f84cb8412c4183253b04ab0685e2c16c9737cc29bd9bf24f.jpg)  
Figure 1. Equivalent data models for a project administration system. (a) Highly graphic NIAM model. (b) Minimally graphic SSM model. (c) Embedded graphic OODM model. (d) Embedded graphic IDEFIX Model – the benchmark model type.

\- minimally graphic, characterized by the use of list structures rather than individual element encapsulation. In these models, only the principal object and relationship types are enclosed in graphic symbols and attribute specifications are appended as lists. Figure 1b shows a model style that combines attribute lists with a graphic syntax for the main object structure.

\- embedded graphic, characterized by large node symbols within which object specifications are placed in list and/or encapsulated form. Figures 1c and d show two models of this style category.

## The experiment design

A data model type from each of the three style categories was chosen for the experiment: NIAM (Nijssen, 1989), SSM (Nordbotten, 1993), and OODM (Cattell, 1991), as highly graphic, minimally graphic and embedded graphic model types respectively. The test model types were modified somewhat so that concept equivalent data models could be constructed, although the basic graphic style of each model type was maintained. In particular, domain specifications, which are included in NIAM models, were added to the OODM and SSM data models. Also, only those constraint types of the NIAM model, which are can be expressed in the OODM or SSM model types, were used. A fourth data model type, IDEF1X (Loomis, 1986), in which the experiment subjects were trained, was included as a benchmark for determining data model interpretation skill. (Experiment participants had been taught IDEF1X modelling in a course in system analysis and design, taken the same term as the experiment.)

Eight common application domains, which were assumed would be familiar to the participants, were chosen for the experiment. The applications included were student course registration, project management, library loan, concert management, customer sales and supplier part. The benchmark applications were tourist attraction registration and Olympic Game event management. A data model for each application was developed which contained two primary entity types related by a 1:n or n:m associative relationship, one class hierarchy and 24–25 attribute types with domain specifications, valid data value sets, primary key specifications, relationship cardinalities and classification constraints. Six of the applications were modelled using each of the test model types, NIAM, SSM and OODM. Figure 1a–c gives the models used for the project management application. Two applications were modelled in the familiar data model type IDEF1X.

The experiment consists of six sets of the eight application models. The sequence of applications was constant for each experiment set. Models no. 1 and no. 5 were the benchmark IDEF1X models. The model types used for application models nos 2, 3, and 4 were repeated for models nos 6, 7 and 8 as a test for learning during the experiment. The sets varied in the presentation sequence of the test data model types, as shown in Table 1.

Experiment participants were randomly assigned an experiment set in such a way that each set was assigned to a nearly equal number of interpreters. The experiment set was presented, one model at a time, on a graphic monitor. Each participant was asked to give a complete, oral description of the components of each data model in his/her set. The oral model interpretations were tape recorded. Eye movement data were collected using an Applied Sciences Laboratory Eye Movement Monitor connected to a Macintosh computer. Eye location co-ordinates were recorded 60 times per second as the participant viewed each model.

Table 1. Experiment layout

<table><tr><td>Set number</td><td>1, Tourist</td><td>2, Student</td><td>3, Project</td><td>4, Library</td><td>5, Sport</td><td>6, Concert</td><td>7, Sales</td><td>8, Supplier</td></tr><tr><td>1</td><td>IDEF1X</td><td>SSM</td><td>NIAM</td><td>OODM</td><td>IDEF1X</td><td>SSM</td><td>NIAM</td><td>OODM</td></tr><tr><td>2</td><td>IDEF1X</td><td>SSM</td><td>OODM</td><td>NIAM</td><td>IDEF1X</td><td>SSM</td><td>OODM</td><td>NIAM</td></tr><tr><td>3</td><td>IDEF1X</td><td>NIAM</td><td>SSM</td><td>OODM</td><td>IDEF1X</td><td>NIAM</td><td>SSM</td><td>OODM</td></tr><tr><td>4</td><td>IDEF1X</td><td>NIAM</td><td>OODM</td><td>SSM</td><td>IDEF1X</td><td>NIAM</td><td>OODM</td><td>SSM</td></tr><tr><td>5</td><td>IDEF1X</td><td>OODM</td><td>SSM</td><td>NIAM</td><td>IDEF1X</td><td>OODM</td><td>SSM</td><td>NIAM</td></tr><tr><td>6</td><td>IDEF1X</td><td>OODM</td><td>NIAM</td><td>SSM</td><td>IDEF1X</td><td>OODM</td><td>NIAM</td><td>SSM</td></tr></table>

Complete eye movement and verbal interpretation data are available for 35 participants, giving 280 model interpretations, 35 for each application model and 70 for each model type.

The experiment was run twice, in 1994 and again in 1996. In the first experiment, each participant was given an example data model and verbal explanations of the terminology used immediately preceding their interpretations of their model set. The instruction model was for an application and a data model type not included in the experiment. Participants in the second experiment were simply asked to 'give a complete specification of each data model.' The participants indicated when each interpretation was finished. Average interpretation time per model was 2.25 minutes. The maximum time used was 4 minutes.

## Experiment participants

Ideally, experiment participants should have been selected from the ‘real’ world of data model interpreters, i.e. persons whose work environment includes reading, confirming, and/or implementing information systems based, in part, on the specifications given in a data model. The participants of this experiment were final-term seniors and graduate students in computer science at the University of Hawaii who had volunteered to participate in the experiment. These students were expected to enter the work force 1–2 months after the experiment, most likely as system designers and/or implementers. Some would become users of systems developed by others.

Although students lack practical experience, a random group of database professionals could be expected to have a bias towards the model type of their training and/or experience. In this case, the participants were completing a senior level course in information systems analysis and design in which IDEF1X data modelling was taught. As such, they shared a common background in data model design and interpretation. As the experiment model notations were unfamiliar to the participants, it was assumed that consistent differences in model interpretations could be attributed to differences in the graphic style of the models.

## MODEL INTERPRETATION

Model interpretations generally used the Extended ER terminology, familiar to the experiment participants. The comprehension score calculated for each model interpretation was based on identification of model components. Each component in the interpretation was scored on a scale of 3–0: 3, correct concept; 2, incomplete; 1, incorrect concept identification; and 0, not mentioned. Synonym concept names were accepted, e.g. object = entity. The comprehension score for the model interpretation was then given as the percentage of a correct interpretation.

Comprehension score variation between the two experiments is not significant. As shown in Table 1, each of the six applications was modelled using the three model types. There was no significant difference between application interpretations, indicating that there was no significant difference in familiarity with the applications, and, interestingly, no learning of model syntax during the experiment. Average comprehension scores differed from 1% to 3% between interpretations of the first model and second model of the same type.

Of the 35 participants for which complete data is available, five were graduate students, 23 were native English speakers and 28 were men. No significant differences in model interpretation skill were found based on education level (computer science undergraduate/graduate), native language or gender. Participants in the second experiment were given a visual characteristics test to determine whether there was a correlation between visual preference and comprehension of graphical models. Although there was significant variation in model comprehension among the participants, no correlation was found between the visual classification and model interpretation scores.

## Model comprehension variation

Minimum, average and maximum comprehension scores for each model type are shown in Figure 2a. As expected, the interpretation scores for the familiar, IDEF1X models were significantly better than for the unfamiliar model types (P < 0.0001). Significance tests used the t-test for paired two sample means in MSExcel. The confidence level, $\alpha$ , was set at 0.5. The differences between the comprehension scores for the highly graphic models (NIAM) and the minimally and embedded graphic styled models (SSM and OODM) are also significant, P = 0.000012 and P = 0.009 respectively.

![](/api/attachments/F3REZ9UC/fulltext/images/2d6a61ef9d6399cfe3611e72431ddc34e348236a0dd12cff75a0f3a748c21665.jpg)

![](/api/attachments/F3REZ9UC/fulltext/images/ea2e736b7c3416662107bb3dccf06d6c36f08ea31f8f1f9636927b9f950767c4.jpg)  
Figure 2. (a) Comprehension scores per data model type. (b) Comprehension scores and per skill level.

b

A basic model interpretation, identifying the four primary entity/object types, their attributes, the associative relationship with its attributes, and the subclass hierarchy, but omitting all constraint details, would give a comprehension score of 33 percentage points. The average interpretations of five participants did not meet this level of comprehension. We have assumed that these participants did not understand the experiment task and that the remaining 30 participants had some level of skill at data model interpretation.

Comprehension scores for the IDEF1X models have a high correlation, > 0.8, with the scores for the interpretations of the other model types, indicating that the IDEF1X scores can be used as a predictor of model interpretation skill. We have used this score to classify the participants as skilled or novice model interpreters according to whether their average IDEF1X comprehension score was greater or less than the average, 72%. Figure 2b shows the average comprehension scores for each group. Comprehension differences between the highly graphic (NIAM) model interpretations and the minimally and embedded graphic styled models model interpretations (SSM and OODM) are significant for both the skilled and novice groups. P-values for NIAM to SSM and OODM = 0.007 and 0.078 for skilled interpreters and = 0.002 and 0.027 for novice interpreters.

The skilled and novice interpreters failed, on average, to include from one-third to one-half of the model components in their interpretations. An explanation for these omissions could be that either these components were seen but were not understood or considered relevant, or were not seen and therefore could not be included in the interpretation.

## Concept recognition

Each of the experiment models contained the basic data modelling concepts – entities, attributes, relationships and domain sets – as well as the constraint types – primary key, relationship cardinality, subclass participation and data value sets. Figure 3a shows the percentage of novice and skilled interpreters who recognized each concept in at least one of the data models.

![](/api/attachments/F3REZ9UC/fulltext/images/419c918776fe7c7cded8e4d8e34ab123f5f2309d3e835b1293c7c447f7b92fbe.jpg)

![](/api/attachments/F3REZ9UC/fulltext/images/c2613449ca5e7e90db2dc15632f03cdd49f5d1c4d58ec0a48a1856eed4fed963.jpg)  
Figure 3. (a) Concept recognition by skill level. (b) Concept recognition by data model type.

All interpreters recognized entity types and attribute sets, as well as the two interentity structures, associative relationships and classification hierarchies. The skilled interpreters recognized key attributes and cardinality constraints and were able to differentiate methods from attributes in the object-oriented models as well. The novice interpreters omitted data value specifications: most (57%) omitted key constraints, and nearly half omitted domain specifications as well. Lack of recognition of domain specifications may have been caused by a lack of expectancy since the familiar IDEF1X model type does not include them.

Figure 3b shows the percentage of models of each type in which the concepts and constraints were correctly identified. The choice of graph symbol and the form and placement of the attribute set do not appear to affect entity and attribute recognition. The graphic symbols used for relationship specifications in the NIAM and OODM models (see Figure 1a and c) may have led to misinterpretations, because many of these specifications were incorrectly identified as entities. Although all readers included the classification structure in some model interpretation, inclusion varied significantly by model type. Primary keys, relationship cardinalities and data value constraints were often omitted, indicating that although the concepts were known (Figure 3a) they were not seen or perhaps not recognized in the unfamiliar model notations.

## What was seen

An analysis of eye fixation data gives information about which graph components were seen/not seen, in the sense of 'looked at'. A fixation is here defined as 10 or more consecutive eye locations within a $10 \times 18$ pixel area on the eye tracking monitor, which in this case displayed the data model being interpreted. This is equivalent to at least 167 ms, which is considered the minimum time needed to consciously record an observation. The area is large enough to contain two or three letters as well as the line-end notation used. Clearly, components not seen cannot be interpreted or articulated. Presumably, components seen but not articulated were not understood or were not considered important to the model interpretation. Figure 4a and b shows the percentage of model components seen and articulated by the novice and skilled interpreters, respectively.

![](/api/attachments/F3REZ9UC/fulltext/images/41647c1c9520fc3df188b4f6f968fdb458dedf27a666e0295ccfbdd4614ed7da.jpg)  
Figure 4. Model components seen and articulated by skill level.

![](/api/attachments/F3REZ9UC/fulltext/images/fa85a2cf34defbc68b66dcdca4307b59cf0ca79e337aae4300faa2efe2c10e06.jpg)

Twenty per cent to 30% of the components of the unfamiliar models were not seen, whereas 35–55% were not articulated in the model interpretations. Skilled interpreters saw somewhat more of the model components than novice interpreters. They also articulated most (75–90%) of what they saw.

Both skilled and novice readers found the highly graphic models (NIAM) most difficult to interpret, omitting more than 25% of the components that were seen. Novice interpreters omitted 20–30% of the model components that were seen, indicating that they had problems interpreting components in all of the model types.

One measure of interpretation effort is the number of fixations used to see and articulate the model components. Figure 5a shows the average effort, measured in average number of fixations, used for interpretation of the different model types by the novice and skilled groups. In general, interpreting the unfamiliar model notations required more effort. Novice interpreters used less effort, 8–30% fewer fixations, in their model interpretations than the skilled interpreters. Although interpretation effort increased with the increase of model complexity, comprehension scores fell as data model components were omitted from the interpretations (see Figures 2b and 4b).

Figure 5b shows the average attention given to interpretation of the data model components. All participants used a similar distribution of fixations for model component interpretation, irrespective of familiarity and/or graphic style, indicating that graphic style has little effect on the amount of attention given to model components. One exception is the attention given to the classification specification in the SSM models, which is given with a distinct graph symbol in a separate graph area. Interpretation of the relationship structure required four to five times the effort of entity identification, which supports other observations that interentity relationships require more effort to comprehend than the identification of entity types.

![](/api/attachments/F3REZ9UC/fulltext/images/68033ef31718c1d41de244931152a7f6876a56efe041981ae49f855ea9159fe0.jpg)

![](/api/attachments/F3REZ9UC/fulltext/images/6bb711c3d80c51bcff6d76032a8e5ce759140f1bab8c30eb1a44cf336775bf36.jpg)  
Figure 5. (a) Interpretation effort by skill level. (b) Interpretation effort by concept.

In all of the test models, domain and data value specifications were given as a right-hand extension to the attribute specification, which, in general, were not seen. Also, so little attention was given to interpretation of the cardinality constraints given as line-end symbols in the NIAM and OODM models that we can conclude that they were not seen.

## READING STRATEGIES

Improving the visibility of model components is one strategy for improving the legibility of graphic models. Another could be to teach ‘good’ reading strategies, defined as those used by skilled model interpreters. A reading strategy consists of three observable components: model viewing strategy, viewing focus and articulation sequence.

## Viewing strategy

In general, graphic models are expected to be read, as text, left to right, top to bottom (Gillespie, 1993). As graphic data models have no inherent interpretation sequence, an alternative strategy would be to view the model as a picture, starting at the centre or some dominant model component and scanning the model following arc connections. We have termed these basic viewing strategies as:

\- Text, starting from the top left or top centre of the model and down the page, indicating that the model was read in a fashion similar to text reading patterns.

\- Image, starting at the centre or dominant graph area and scanning in any direction, indicating that the model was viewed as a picture.

Figure 6a and b shows the usage of these strategies by the skilled and novice interpreters respectively. Most of the skilled (75% and 63%) and novice (64% and 93%) interpreters viewed the embedded models as text. The minimally and highly graphic models were viewed differently by the skilled and novice interpreters. In particular, minimally graphic models were viewed as images by the skilled interpreters, whereas the highly graphic models were so viewed by the novice interpreters.

## Viewing focus

An analysis of the concentration of fixation movements (saccades) within graph areas and between areas provides data for identification of the viewing focus used for model interpretation. Nearly 80% of the interpretations could be classified as using:

\- An object focus in which more than the average number of fixation movements were concentrated within graph components, indicating that the reader has focused on interpretation of the of graph nodes that represent the objects included in the model. The average number of fixations within the object nodes was 37%, whereas the average number of fixations focused on model structure was 17%.

![](/api/attachments/F3REZ9UC/fulltext/images/df2d4423d549c53c6be8fc833a2e98583dd79b0e8f01e88e99bb778f2cb3b2a6.jpg)  
Figure 6. Viewing strategies for skilled and novice interpreters.

![](/api/attachments/F3REZ9UC/fulltext/images/5be151786fd07f77c5a2534405e5e6dfa69ea9ef4fc8b77bc1d17097120a9b15.jpg)

\- A structural focus when more than the average number of fixation movements followed on the structure of the model represented by the arc relationships between model objects.

As shown in Figure 7a and b, skilled model interpreters were more focused than the novice interpreters. For both groups, up to 25% of the interpretations showed both object and structure focus. Novice interpreters were more likely to use an indeterminate strategy for many of their interpretations, up to 57% of the familiar and minimally graphic models.

It appears that graphic style influences the viewing focus differently for the novice and skilled interpreter groups. This is most clearly evident for the highly graphic styled models (NIAM), where the skilled interpreters focused on model objects, whereas the novice group focused more on the relationship structure. The skilled interpreters were not consistent in the way they viewed the models, using a structured focus for the familiar and minimally graphic models (SSM), and an object focus for the unfamiliar, highly structured and embedded models.

![](/api/attachments/F3REZ9UC/fulltext/images/eb35cdf1a034c1ff11183d1095757bd366c1008da0fcd009f752a059d55b8af3.jpg)  
Figure 7. Viewing focus for skilled and novice interpreters.

![](/api/attachments/F3REZ9UC/fulltext/images/904cff86ad012c9b2fa9eaa74920e24f9e83f9a86a67c7499bd2a21cd27565d4.jpg)

## Articulation sequence

Articulation strategies may enhance model interpretation by encouraging attention to detail and thus a more complete presentation. Eighty per cent of the model interpretations included the basic entity–attribute–relationship structure, which can be used to distinguish two articulation patterns:

\- detail starting with an entity–attribute specification followed by the connecting relationships, in a text-like pattern, and

\- structural starting with the entity–relationship structure, followed by the attribute sets and constraints in a scan-like pattern.

Figure 8a and b shows the articulation sequence usage for the experiment (an incomplete interpretation is one that does not include the relationship structure). Note that the structural sequence was preferred by the skilled interpreters for three of the four model types. This sequence was also the dominant pattern for the familiar model type (IDEF1X) for both skill groups, which can be an indication that it can be taught. Novice interpreters read the nodes of the unfamiliar model types as text, overlooking both structure and annotations. They also had problems correctly identifying the relationships in the embedded graphic models.

## SUMMARY OF OBSERVATIONS

Graphic data models are intended to support user-designer and designer-implementer communication during the specification, implementation and use of an information system. One assumption appears to have been that anyone will be able to read and understand graphic models. A second assumption has been that alternative graphic syntax would not hinder comprehension. Our experiment data do not support either of these assumptions. We found significant differences in model comprehension that appear to be dependent on graphic style.

![](/api/attachments/F3REZ9UC/fulltext/images/2957f7e5eb2c5012b0bac0c5fbaea229d864b5e664d48609c13aac5d43c1539e.jpg)  
Figure 8. Articulation sequence for skilled and novice interpreters.

b  
![](/api/attachments/F3REZ9UC/fulltext/images/0f661f663109db92eb6a5d68cdb548c7175c6e76680a337ac3b7a6d5d554604d.jpg)

Of the 35 participants for whom we have both eye movement and audio data, one in seven were not able to give a basic interpretation of the unfamiliar data model types. The observations we have presented in this paper are based on the remaining 30 participants, who showed at least a minimum skill level in graphic data model interpretation.

We have focused on the effect of graphic style on model comprehension and how data models are read. Our principal motivation has been to identify graphic style characteristics and reading strategies that enhance model comprehension. In particular, we have focused on the effect of graphic style on:

● The visibility of model components and thereby model comprehension.

\- Reading strategies of skilled vs. novice data model interpreters.

An analysis of the eye movement data, taken while the audio report was being made, allows us to determine viewing patterns used for model interpretation. It also allows determination of which model components, omitted from interpretations, were not seen, and whether these omissions are correlated with the graphic style of the model and/or the way in which the models are read.

## Model comprehension

Model comprehension depends on seeing the model components and recognizing each as a relevant system concept. The participants had been taught the basic data modelling concepts (entities, primary keys, attributes, interentity relationships, classification hierarchies, cardinality and classification constraints) using the IDEF1X notation. Average comprehension scores were 72% for the familiar model type and varied from 53% to 61% for the unfamiliar model notations. Individual interpretations varied from 27% to 90% across all model types, indicating substantial individual variation.

We have assumed that observed components that were not reported were either not understood or were considered unimportant to the interpretation. As could be expected, the notation of the unfamiliar models proved difficult to interpret, particularly for the novice readers who omitted up to 28% of the components that they had seen from their interpretations. However, even the skilled data model interpreters omitted model components presented in an unfamiliar graphic syntax. The highly graphic model, which has the richest graphic syntax, most distant from the familiar model type, was also the most difficult to interpret for both skill level groups.

## Component identification

The low scores were due to misinterpretation and lack of inclusion of model detail in the interpretations. Although entities and attributes were recognized in all interpretations, 30–50% of the relationships in the highly graphic and embedded structure styles were identified as entities, indicating that the graphic symbols used for entities and relationships may have been too similar. Further, the use of embedded symbols and annotations in both of these model types may have led to incorrect or incomplete relationship identification.

Relationship cardinality constraints are frequently given in a data model as line-end dot or arrow notations. These were literally not seen. Also, underlined and embedded attributes and cardinalities placed within entity symbols were unnoticed.

The highly graphic model type used in this experiment contained numerous new (to the participants) graphic symbols that appeared to reduce legibility. Interpretations of this model type were significantly poorer than the other model interpretations for both skilled and novice interpreters.

## Reading strategy

It has been assumed that graphic models would be read as text, top-down the graph page using a serial, text-like reading pattern. Our participants followed the text-like viewing strategy for about 60% of their model interpretations. However, less than half of the interpretation presentation patterns can be classified as being text-like.

Skilled interpreters tended to focus on identifying and articulating the model structure. Novice interpreters used a less structured reading strategy. Although most models were read top-down, they were scanned in an unfocused manner. Many of the interpretations were incomplete, indicating problems with identification of relationships.

## CONCLUSIONS

Our study supports earlier observations which suggest that graphic models are not readily interpreted without training in the particular graphic syntax used. It is discouraging that training in one graphic syntax does not have a stronger carry-over effect to other, related model types. This indicates that system designer-drawn graphic models alone are not dependable tools for either confirmation of requirements by system users, or reliable system implementation by system programmers unless these parties have been trained in the model syntax used and, probably, have participated in the construction of the models.

Graphic syntax appears to influence the reading strategy used. Skilled interpreters used a structural reading strategy for all but the highly graphic models. As this strategy is associated with the best interpretations and was preferred for the familiar models, it is possible that training in structural reading would enhance model interpretation.

Highly graphic models are more difficult to interpret than those with a simpler graphic syntax. This model syntax also encourages a serial viewing strategy that is associated with significantly poorer interpretations. It appears that a simple graphic representation, which encourages a structural reading strategy, gives the best support for model interpretation.

Our analysis has been based on verbal and visual data collected while 30 participants interpreted 240 data models. Although this is a small study, we believe that the observed correlation between minimal graphic styles, structured reading patterns, and comparatively high model comprehension could be used for training system users, designers and implementers. Data model editors and system interfaces should use simple models to enhance system understanding.

## ACKNOWLEDGEMENTS

This work was partly supported by The National Science Foundation under grant IRI93-09711 to the second author. We are especially grateful to Professors W. Wesley Peterson and Svein Nordbotten for help in preparation of the experiment, its execution, preparation of the data, and their analysis. Also appreciated are the interest and co-operation of Assistant Professor Donald DeRyke and the students in two of his systems analysis classes. We also wish to thank the reviewers for positive and constructive suggestions.

## REFERENCES

Brooke, J. & Duncan, K. (1980) An experimental study of flowcharts as an aid to the identification of procedural faults. Ergonomics, 23, 387–399.

Bubenko, J.A. Jr (1986) Information System Methodologies – a Research Review. In: Information Systems Design Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. & Verrijn-Stuart, A.A. (eds), pp. 289–318. Elsevier Science Publ. (North Holland), Amsterdam.

Cattell, R.G.G. (1991) Object Data Management Object-oriented and Extended RDBS. Addison Wesley, USA.

Gillespie, C.S. (1993) Reading graphic displays: what teachers should know. Journal of Reading, 36, pp. 350–354.

Kim, Y.-G. & March, S.T. (1995) Comparing data modeling formalisms. Communications of the ACM, 38, 103–115.

Loomis, M. (1986) Data modeling – the IDEF1X Technique. Proceedings IEEE Conference On Computers and Communications, pp. 146–151.

Nijssen, G.M. & Halpin, T.A. (1989) Conceptual Schema and Relational Database Design – a Fact Oriented Approach. Prentice Hall, Sydney.

Nordbotten, J.C. (1993) Modelling Relationships And Constraints In SSM – A Structural Semantic Data Model. Report No. 14, ISSN 0803-6489. Department of Information Science, University of Bergen.

Petre, M. (1995) Why Looking isn't always seeing: readership skills and graphical programming CACM, 38, 33–44.

Preece, J. (1983) Graphs are not straightforward. In: The Psychology of Computer Use, Green, T.R.G., Payne, S.J. & van der Veer, G.C. (eds), pp. 41–pp. 56. Academic Press, Wokingham.

Sheppard, S.B., Kruisi, E. & Bailey, J.W. (1982) An empirical evaluation of software documentation formats. Proceedings of Human Factors in Computer Systems, 1, 121–124.

Teorey, T., Yang, D. & Fry, J. (1986) A Logical Design methodology for relational databases using the extended entity-relationship model. ACM Computer Surveys, 8, 197–222.

Wright, P. & Reid, F. (1973) Written information: some alternatives to prose for expressing the outcome of complex contingencies. Journal of Applied Psychology, 57, 160–166.

## Biographies

Joan C. Nordbotten is an associate professor in Information Science. Her research interests include data management (data modelling, database management, multidatabase management) and HCI (computer interface usage and usability). She is the author of numerous papers on data analysis and design and HCI as well as a book on information system analysis and design.

Martha E. Crosby, is a professor in Information and Computer Science. Her research interests include HCI (interactions between the user and the interface, hypermedia, and cognitive science). She is the author of numerous papers and is active in the HCI community.
