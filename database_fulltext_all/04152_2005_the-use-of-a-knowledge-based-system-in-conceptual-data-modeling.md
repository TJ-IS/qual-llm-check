---
otero_id: 4152
otero_key: "BCW8GKDJ"
title: "The use of a knowledge-based system in conceptual data modeling"
authors: "Solomon Antony; Dinesh Batra; Radhika Santhanam"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# The use of a knowledge-based system in conceptual data modeling

Solomon Antony<sup>a,\*</sup>, Dinesh Batra<sup>b</sup>, Radhika Santhanam<sup>c</sup>

<sup>a</sup>Area of ISQS, Rawls College of Business Administration, Texas Tech University, Lubbock, TX 79409, United States <sup>b</sup>Florida International University, United States <sup>c</sup>University of Kentucky, United States

Received 26 February 2003; received in revised form 19 May 2004; accepted 31 May 2004 Available online 28 July 2004

## Abstract

Based on a study of the data modeling process of novice designers, and the errors they commit, a knowledge-based system (KBS) was designed and developed. It was found that the performance of novice designers was significantly better when they utilized the KBS instead of a system with no knowledge base. Two versions of the KBS—one with a guidance interface that advised the designer on appropriate design choices and another with a restrictive interface that restricted the design choices available to the designer—were developed. The restrictive interface was rated as being significantly easier to use than the guidance interface.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Knowledge-based systems; DSS; Decisional guidance; Restrictiveness; Human computer interaction; Conceptual data modeling

## 1. Introduction

Expert database designers are scarce and expensive, and therefore, inexperienced designers sometimes undertake database development tasks. Furthermore, large numbers of end-users, frustrated by the backlog in systems development, and aware of the availability of easy-to-use end-user software, design and develop their own databases [10,13]. These inexperienced designers or end-users, not adequately trained in database design and development procedures, are collectively referred as novice designers [40,49]. Research indicates that systems developed by such novice designers, lead to unsatisfactory and inaccurate outcomes [23,53]. Hence, researchers proposed that knowledge-based systems (KBS) be utilized as one means to help novice designers develop better quality databases [48]. Based on this proposal, several KBS to support database design activities have been developed. In-depth surveys of these systems is provided in Refs. [30,49]. As in other domains, these surveys conclude that systematic tests on the effectiveness and usability of these systems must be conducted in order to facilitate continued research and improvements in KBS [30,41,49].

KBS to support various phases of database design and development have been developed including systems to support the conceptual data modeling phase [14,25,48]. Conceptual data modeling is considered to be a very critical phase of database development, and errors committed during this phase could result in a poor quality database and lead to inaccurate query outcomes [3,33]. Although several KBS have been proposed to prevent such errors and assist the novice designer; the effectiveness of these systems has not been tested empirically, and is a drawback of current research [30,49]. Hence, it is important to conduct empirical tests and investigate whether novice designers benefit from the use of KBS during conceptual data modeling phase. A related issue is whether design differences in a KBS’s interface could impact the effectiveness of the system. A KBS can be designed using either a restrictive or a guidance interface [45,46]. With a restrictive interface (referred also as a restrictive system), the KBS limits the number of design choices available to the novice designer and thus steers her towards making correct design decisions. With a guidance interface (referred also as a guidance system), the system need not restrict the designer’s choices but instead could provide intermittent context-specific advice on appropriate design decisions, and the designer could use this advice. Thus, either of these interface design approaches could be undertaken to assist the novice designer and improve the outcomes, but it is not known which is more effective.

To address the above issues, a KBS for conceptual data modeling, called CODASYS was developed [2]. Further, two versions of this KBS, one with a restrictive and the other with a guidance interface were developed. A control version—with a similar graphical interface to CODASYS but which did not contain information to influence the user’s process— was also developed. Using laboratory experimentation methods, our research goals were: (1) to determine if novice designers can improve their conceptual data modeling performance by using the KBS and (2) to determine which of the two interfaces, restrictive or guidance, is more effective in improving the outcomes of the data modeling process. Section 2 of this paper describes our research framework and hypotheses. Section 3 describes the system and the research method. Section 4 presents the results from the study. Findings are discussed in the concluding section.

## 2. Research framework

## 2.1. Knowledge-based support for conceptual data modeling

There are several phases in the design of a database, which begin with the definition of user requirements and conclude with the physical design of the database. During the conceptual data modeling phase, user requirements are synthesized into a conceptual data model, which is later converted to a specific data storage model [3], such as the relational data model [15]. While there are several methods to create a conceptual data model, the entity-relationship (E-R) model proposed by Chen [12] is one of the most effective approaches [6,9]. Details of conceptual data modeling are described in [3]. Several KBS, such as in Refs. [25,48], have been developed to support novice designers conducting their conceptual data modeling tasks. These systems are very useful but have some functional limitations that could be improved upon. For example, existing KBS support only binary relationships and not higher degree relationships. Higher degree relationships are not uncommon in many business applications (see Ref. [42] for examples) and must be addressed [47]. Existing KBS do not prevent the user from creating derived relationships that could result in the creation of redundant relationships. These issues were addressed in CODASYS. It was designed to allow modeling of ternary relationships and prevent the creation of derived relationships.

## 2.2. Data modeling by novice designers

Research indicates that novice designers are able to identify and model entities moderately well, but have a particularly difficult time in modeling relationships [4]. Because relationships are a key aspect of conceptual data modeling, we therefore decided to provide maximum help in this area. CODASYS was designed to prescribe a strict sequence in creating relationships. Using the GEMS model [39], we also tried to understand the type of errors that novice designers commit. According to this model, errors can be classified as slips, rule-based errors or knowledgebased errors. Slips occur because of a lapse of attention and cannot be prevented by a KBS. Hence, it was not explored further.

Rule-based errors occur because the user applies a wrong set of rules or misapplies known rules/heuristics to execute the task. For example, one commonly used problem-solving rule used by database designers is: <sup>b</sup>If the problem description tends to describe entities in the same sentence, then there is possibly a relationship between the entities<sup>Q</sup>. Novices tend to apply this rule incorrectly and commit errors [4]. Consider the following description of a scenario: <sup>b</sup>A customer creates purchase orders; a particular purchase order is created by only one customer. A customer buys products using the purchase orders<sup>Q</sup>. Observations indicate that novice designers, after reading the first sentence, create a one– many relationship between customer and purchase order. This is correct. However, after reading the second sentence, they often tend to create a ternary relationship involving customer, purchase order and product because these entities are described together. The ternary relationship is incorrect and will lead to redundant relationships. Instead, the correct solution is to create a many–many relationship between product and purchase order. This can be labeled as a rule-based error and is sometimes referred as literal translation errors i.e. problem-solving rule applied without deeper analysis of the context. CODASYS was designed so that it would identify these rule-based errors and caution the designer that an error has occurred.

Knowledge-based errors typically occur in situations that have not been faced by the user. The user has to reason and obtain a solution based on basic principles. Since novice designers do not have much experience, they tend to make many knowledge-based errors. It has been found that nearly one-third of errors committed can be classified as knowledge-based errors [4]. For example, the definition of the First Normal form applied to determine the appropriate attributes of an entity states: <sup>b</sup>Only one value is associated with each attribute and the value is not a set of values or a list of values<sup>Q</sup> (Ref. [19], p. 309). Whenever a designer is unsure about assigning an attribute to an entity, she will have to think of this principle and reason, and apply it appropriately. Consider a problem description as follows: <sup>b</sup>A programmer may have knowledge of many programming languages, but of varying expertise<sup>Q</sup>. Observations indicate that novice designers tend to model languages as an attribute of programmer. A correct solution is to model an entity called language and create a relationship between programmer and language. CODASYS was designed such that it would attempt to prevent the occurrence of these errors by prompting the user to verify that attributes are always single valued.

These errors occur because novice designers lack knowledge and cannot draw from past experiences. Another reason could be the cognitive strain novices typically face when they have to keep track of many pieces of information including information on entities, relationships, and procedures for data modeling. It has been observed that novice designers seek to minimize cognitive strain by resorting to literal translation heuristic and to anchoring [4]. Literal translation implies that data model is developed based on the literal interpretation of the wording of the problem. Anchoring means that a novice designer will pick an initial solution and will be reluctant to alter it even though additional information contradicts the initial solution [4]. A KBS could reduce the cognitive strain by helping to keep track of information, and reminding the user of entities and relationships created earlier. Based on these observations, CODASYS was designed using information available in textbooks [34], journal articles [49], and heuristics formulated to alleviate errors made by novice designers [5]. While the information provided in text books and articles are useful to developing the KBS, guidelines from these heuristics focus on specific problems faced by novice designers, and provided additional information to build the system. For example, because novice designers make knowledge-based errors when determining the cardinality of a relationship [6], the KBS was designed such that it would always prompt the user with several questions before the user created a relationship. If a user chooses customer and purchase order entities to participate in a relationship, the system would ask: <sup>b</sup>How many instances of customer are associated with one instance of purchase order?<sup>Q</sup> and after the user answers <sup>b</sup>one<sup>Q</sup> or <sup>b</sup>many<sup>Q</sup> the system would ask: <sup>b</sup>How many instances of purchase order are associated with one instance of customer?<sup>Q</sup> These questions can help the novice designer to think and decide on the cardinality of the relationship.

The knowledge included in the system is summarized in Appendix A. Details of the system and how it appears to the user are described in further detail in a later section and in Appendix B. A control version that did not contain any information to specifically assist the novice designer or to identify their errors was also created. The control version could be likened to a drawing tool that can help the user create a conceptual model. It will not provide advice or prevent the user from making errors. For example, with three entities, if the user models a ternary relationship and a binary relationship, the control version system will not intervene but will draw the E-R model. Hence, this system could be said to have some level of data modeling knowledge in that it could help a novice designer create an E-R model. But, it did not have the additional functionalities that could steer the novice designer towards better design choices and prevent error-prone situations. Hence, it was expected that in comparison, the KBS system would be more effective in helping novice designers create better quality data models. The first hypothesis is therefore stated as:

Hypothesis 1. Novice designers’ performance in conceptual data modeling will be superior when they utilize a knowledge-based system compared to when they use a control version.

## 2.3. Design of the KBS’s interface

A key aspect of KBS that impact the effectiveness and acceptance of the system is the system interface [11,29,32]. Specifically in the area of IS design, Silver [45,46] suggests that element of system restrictiveness and decisional guidance be applied to develop a KBS interface. The definition of system restrictiveness is <sup>b</sup>the manner by which a system limits its user’s decision making processes to a subset of all possible processes<sup>Q</sup> [46]. By blocking certain functionalities and constraining/restricting the decision process, the system influences the decision-making process. A support system for strategic planning may restrict the user from utilizing multi-objective decision modeling operators but allow the use of operators that can help formulate a uni-objective linear programming model. On the other hand, a system that provides decisional guidance would <sup>b</sup>guide the user in constructing and executing decision-making processes by assisting them in choosing and using its operators<sup>Q</sup> [46]. In the strategic planning task, the system will suggest that the user apply a linear programming model but it will make available all the operators, including those that help to formulate a multi-objective and uni-objective model. Thus, in a guided interface, the system guides and makes a recommendation on design choices but does not restrict the choices.

Please note that system features in any support tool provide some level of guidance or restrictiveness, but these are unintentional consequences of system design [37]. For example, a system can be said to provide guidance when it prompts a user to insert a formula in the appropriate cell in a spreadsheet, or when it displays a help message when the user makes an error. But, the interest in IS research is to understand the extent to which deliberate decisional guidance or deliberate restrictiveness is useful in problem-solving, and to determine how it can be implemented in system design [38,46,55]. In the KBS, a knowledge rule that states, <sup>b</sup>If there are no key attributes then an entity cannot be defined<sup>Q</sup> can be implemented in two ways. With a restrictive interface, the system would prevent the user from storing an entity if a key attribute is not assigned to it. A KBS using a decisional guidance interface would remind the user to define the key attribute for the entity, providing what is known as suggestive guidance [46]. Other differences in the two interfaces are listed in Appendix B.

Silver [46] does not provide strong theoretical reasons to expect the guidance or the restrictive interface to perform better in a particular task. Empirical studies have examined the effectiveness of each of these interface types, but to the best of our knowledge, there has not been much research directly comparing the effects of the two interfaces. In several scenarios, such as multi-criteria decision making, forecasting, policy making, and in group support system environments, guidance based interfaces were found to be effective than providing no decisional guidance [35,36,54]. Restrictive interfaces were found effective in helping users structure their model manipulation strategy [22], but did not have a significant effect when users solved preferential choice problems [52]. Thus, neither theory nor empirical results point to the superiority of either interface, so we stated an exploratory hypothesis as follows:

Hypothesis 2. There is a difference in novice designers’ performance when they use a guidance interface compared to when they use a restrictive interface.

Performance outcomes are not the only relevant measure when examining the effects of the interface.

Perceptual outcomes are equally important because interfaces not perceived as being easy to use may not be used even if they are effective [43,56]. In the IS domain, the widely used technology acceptance model (TAM) identifies ease-of-use as a critical user perception that directly impacts users’ intentions to use a specific system [17,18]. Measurement of the ease-of-use provides an assessment of whether the user perceives the system to be flexible, easy to learn and use and thus provides information on the likely acceptance of the system.

Restrictive interfaces provide very few decision choices and lead the user on a specific path. The guidance system provides advice that the user has to think and act upon, and it may seem as requiring more cognitive effort, particularly to novice designers. According to the cost-benefit framework, decision makers choose a strategy based on trade-offs between perceived effort and perceived accuracy, i.e. they try to maximize decision accuracy and minimize effort [37]. The overall empirical and conceptual research indicates that effort is the more important factor that influences decision makers [51]. Because this system is being used by novice designers and it provides several alternative options, the guidance interface may be perceived as requiring more effort and thought. Therefore, compared to the restrictive system, the guidance system may be perceived as being less easy-to-use. In the restrictive interface, messages and prompts are direct and not flexible. Empirical results and design guidelines indicate that novices prefer a systemcontrolled interaction process with less flexibility in the dialogue style [7]. Therefore, the restrictive interface will be perceived as easier to use. We state our next hypothesis as:

Hypothesis 3. Novice designers will perceive the restrictive interface to be easier to use than the guidance interface.

## 3. Research method

Based on the above, we draw our research model as shown in Fig. 1. Subjects’ prior knowledge on data modeling was measured before the experiment and used as a covariate, thus controlling for individual knowledge level effects on the quality of the data model. By using subjects from the same population and assigning them randomly to experimental groups, we randomized user characteristics and minimized their effects. The same task was used across all groups eliminating the effects of the task factor. Thus, any differences in the quality of the data model could be attributed to differences in the system type, and the interface.

## 3.1. Description of the system

The KBS was developed using a GUI programming language to run on the Windows platform. The rules included in the system are listed in Appendix A and sources for this were obtained from Refs. [3,5,50]. The interface was designed to be simple, with only five main menu items: file, attributes, entities, relationships, and assumptions. As shown in Appendix B, two versions of the software, one with a restrictive interface and the other with a guidance interface, were developed. These two systems were functionally equivalent, i.e., they used the same knowledge base but had a different interface for implementing the knowledge base. See Figs. 2 and 3 for screen images that indicate differences between the two interfaces. The control version had the same look and feel of the knowledgebased system but did not have any of the knowledge listed in Appendix A. It behaves like a CASE tool that facilitates the creation of the E-R diagram, but did not provide suggestive messages to help them in creating relationships, or prevent them from creating incorrect relationships or provide error messages. A user manual for each version was developed which described the available menu and window options.

![](/api/attachments/BCW8GKDJ/fulltext/images/45d43d5a5644bd01c1a88d7568b576b28f83ebd373a57dfcbcbad91ea35e7940.jpg)  
Fig. 1. Research model.

Please note that this KBS was specifically oriented towards the novice designer, while commercial data modeling systems, including CASE tools, are built primarily for experienced designers. Users of Designer/2000 need to convert all higher degree relationships to binary relationships using associative entities (see p. 55 of Ref. [8]). Only designers, who are experienced in conceptual modeling, will be able to do such conversions. CODASYS can support ternary relationships, and so there is no need for the designer to know procedures to convert ternary relationships to binary types. Similarly, users of another popular CASE tool, ER/WIN from Logic Works, also have to convert higher degree relationships into binary relationships (see p. 60 of Ref. [31]). Such requirement of converting tenary relationships to binary relationships forces designers to consider issues relating to both the physical design (i.e. concatenated keys), and conceptual design (i.e. entities and attributes). Novice designers are likely to be overwhelmed by such expectations. Hence, CODASYS can be said to be more suited than commercially available tools in supporting novice designers.

![](/api/attachments/BCW8GKDJ/fulltext/images/d4018b5368152de5a455443e8287b8fe36193e54ca9612df941299a9f4b36abb.jpg)  
Fig. 2. Relationships sequences–restrictive interface.

![](/api/attachments/BCW8GKDJ/fulltext/images/9ebb1452348bb9760ce51e14f1f924c600091042325e511e09e2a5f9f8930f69.jpg)  
Fig. 3. Relationships sequence–guidance interface.

## 3.2. Pilot studies

Pre-pilot and pilot tests were conducted. During the pre-pilot test, subjects solved a data-modeling task using one of the three systems and some technical problems were discovered and resolved. Based on their feedback, the length of training on E-R modeling concepts was increased to 2.5 hours. During the pilot study, 23 volunteers from an undergraduate information systems course were trained on E-R modeling concepts and asked to solve a data modeling problem with the help of one of the three versions. The KBS group performed better than the control group (55.4 vs. 45.2 points on a 0–100 scale). Feedback from the subjects was used to modify the user manual.

## 3.3. Description of subjects, tasks, and variables

The choice of subjects depends on the criterion population [28]. In this study, they are novice designers, characterized as information workers who use productivity tools, such as spread sheets and personal database management systems. Undergraduate students in an introductory information system class, who had completed courses on microcomputer software, were found suitable as subjects. These student volunteers attended training sessions to learn data modeling principles after which they completed the experiment. All subjects received the same level of training in data modeling. Participating students received 10% credit toward their course grade and nonparticipants had alternative assignments to earn the same level of credit.

The dependent variable, i.e. novice designers’ performance, was measured in terms of the quality of data model created, using a grading scheme that has been validated and tested in other research (e.g., Refs. [9,24]). The system type (KBS or control) served as the independent variables. Subjects’ scores in the pretreatment task, completed after training but before the experiment, were used as the covariate. The pretreatment task involved four entities, a binary and a ternary relationship. The experimental task consisted of a binary one–many, a binary many– many, and a ternary one–many–many relationship. The experimental task was limited to one task, because it was felt that this would be sufficient to address main aspects of data modeling (entities, attributes, and relationships), and novice subjects would be overwhelmed otherwise. The questionnaire measuring perceived ease of use (EOU) was obtained from Ref. [17], and has been extensively validated and used in information systems research (for example, Refs. [1,26]).

## 3.4. Training sessions

Subjects attended two training sessions on conceptual data modeling, each lasting 2.5 hours. In the first session, subjects were taught relational database concepts such as tables, records, fields, key fields, and relationship among tables, etc. In the second session, subjects were trained specifically on the E-R modeling method. The second session included description of the E-R constructs and demonstration of E-R modeling method using some sample problems. Each subject was given a copy of the E-R modeling training script that provided definitions of essential concepts such as entities, attributes, and relationships. The subjects applied these concepts in a practice problem. Thus, before using the system, all subjects were familiar with the textbook method of using E-R modeling method.

## 3.5. Experimental procedures

The experiments were conducted in two instructional computer laboratories. Both rooms had similar layout and arrangement of computers. Side screens were used to minimize the potential for copying. The software was stored on the diskettes, which were handed to subjects. One of the authors, with the help of a research assistant, conducted all the experimental sessions. Once the subjects had completed conceptual training, they were free to report to any one of the nine experimental sessions scheduled over a two-day period. When subjects reported to the laboratory for experimental sessions, they signed a consent form and completed a background questionnaire. They were then asked to complete the pretreatment E-R modeling task manually, after which they were randomly assigned to one of the three systems (restrictive, guidance, or control) and given the appropriate software on a disk. The subjects were not aware that they were being given different systems. A three-digit code on the diskette label identified the type of system the subject used.

Prior to the start of experimental sessions, subjects were given the opportunity to become familiar with the system, by practicing an E-R modeling problem that they had solved earlier during the conceptual training sessions. Subjects could ask questions about the system during this session. Each subject was given a copy of the user manual, which he was permitted to keep till the end of the experiment. Most subjects completed the practice task within 20 minutes.

After completing the practice task, the subjects were given the experimental task and were asked to design the E-R model with the help of the system. The subjects were encouraged to do an accurate job of data modeling, taking as much time as needed but were free to give up after making adequate attempts. After completing the experimental task, subjects were asked to complete the ease-of-use questionnaire. Then, the subjects were thanked and allowed to leave.

## 4. Results

Of the 108 subjects who volunteered, 95 attended the experimental sessions. Of the 95 subjects, 6 faced hardware problems during the experiment. They were eliminated from the subject pool, leaving us with a usable sample of 89 subjects consisting of 50 males and 39 females. The average age was 26.7 years. On average, subjects were familiar with at least two software packages. Of the 89 subjects, 60 were in the treatment group using a knowledgebased system and 29 in the control group using the control version. Within the group using a knowledge-based system, 28 used the restrictive system while 32 used the guidance system. The subjects’ computer experience was comparable across the groups. The computer experience scores were 1.65 (S.D.=0.66) for control, 1.62 (S.D.=0.65) for guidance, and 1.71 (S.D.=0.60) for restrictive groups, but were not significantly different $( F { = } 0 . 1 5 , p { = } 0 . 8 6 4 )$

Table 2  
Table 1  
Table 4  
Table 3  
Performance scores for control and knowledge-based system groups

<table><tr><td>Group</td><td>N</td><td>Mean</td><td>S.D.</td><td>Significance</td></tr><tr><td>Control</td><td>29</td><td>45.54</td><td>27.91</td><td>F=2.75, p&lt;0.05</td></tr><tr><td>Knowledge-based system</td><td>60</td><td>55.29</td><td>22.91</td><td></td></tr></table>

## 4.1. Scoring process

Two graders, working independently and unaware of the type of system the subjects had used, graded the E-R diagrams. Because the grade codes are from a nominal scale, the reliability measure, using Cohen’s j [16], was computed for each entity and each relationship constructs. The overall j was 0.89 ( p<sup>b</sup>0.01). For analysis purposes, the average of the two graders’ scores was used as the quality of the data model—one of our dependent variables. This same grading scheme was used to grade the pretreatment task.

## 4.2. Effects of the KBS

Using the pretreatment task score as a covariate, an analysis of covariance (ANCOVA) procedure was conducted on the quality of the data model. Using this technique is warranted since the ratio of higher variance to lower variance between the two groups was 1.61 and it was not significant $\left( { p / - 0 . 2 9 1 } \right)$ . The mean pretreatment score was 33.3 with a standard deviation of $1 9 . 9 \ : \ : ( p { < } 0 . 0 5 )$ . From the summary statistics for the dependent variable, shown in Table 1, it is seen that the subjects using a KBS scored significantly higher than those who used the control version $( F { = } 2 . 7 5 , p { < } 0 . 0 5 )$ supporting Hypothesis 1, which stated <sup>b</sup>Novice designers’ performance in conceptual data modeling will be superior when they utilize a knowledge-based system compared to when they use a control version<sup>Q</sup>.

Performance scores for guidance and restrictive interfaces

<table><tr><td>Group</td><td>N</td><td>Mean</td><td>S.D.</td><td>Significance</td></tr><tr><td>Guidance</td><td>32</td><td>58.11</td><td>23.64</td><td>F=1.12, p&lt;0.29</td></tr><tr><td>Restrictive</td><td>28</td><td>52.07</td><td>22.01</td><td></td></tr></table>

Effects of interface and pretreatment scores on performance (ANCOVA results)

<table><tr><td>Source</td><td>df</td><td>SS</td><td>MS</td><td>F</td><td>Pr&gt;F</td></tr><tr><td>Model</td><td>2</td><td>3143</td><td>1571</td><td>3.22</td><td>0.0473</td></tr><tr><td>Interface</td><td>1</td><td>544</td><td>544</td><td>1.12</td><td>0.2953</td></tr><tr><td>Pretreatment score</td><td>1</td><td>2598</td><td>2598</td><td>5.33</td><td>0.0247</td></tr><tr><td>Error</td><td>57</td><td>27,815</td><td>487</td><td></td><td></td></tr><tr><td>Total</td><td>59</td><td>30,958</td><td></td><td></td><td></td></tr></table>

## 4.3. Perceived effects of the interface

The results on the effects of the interface are shown in Table 2. It is seen that the covariate, pretreatment task score (prior knowledge) was significant $( p { < } 0 . 0 5 )$ , but there were no performance differences between the two interfaces $( F { = } 1 . 1 2 , p { = } 0 . 2 9 )$ . (Please see Table 3 for the complete ANCOVA results.) Hence, Hypothesis 2 stating, <sup>b</sup>There is a difference in novice designers’ performance when they use a guidance interface compared to when they use a restrictive interface<sup>Q</sup>, is not supported. In the original Davis (1989) study [17], flexibility is one of the components of the ease-of-use measure. However, for the novice designers in this study, a flexible system may be considered more difficult to use than an inflexible one. Researchers have recommended that this item be excluded; therefore, this item was dropped from the EOU measure. After this was done, the Cronbach’s a for the ease-of-use scale was computed to be 0.98. The one-tailed t-test comparing the perceived ease-of-use measures of the two interfaces shown in Table 4 indicates that the restrictive interface is perceived to be easier to use ( p<sup>b</sup>0.05). Hence, there is support for Hypothesis 3, which states: <sup>b</sup>Novice designers will perceive the restrictive interface to be easier to use than the guidance interface<sup>Q</sup>.

Perceptual effects of the interface

<table><tr><td rowspan="2">System</td><td colspan="3">Ease of use</td></tr><tr><td>N</td><td>Mean</td><td>S.D.</td></tr><tr><td>Guidance</td><td>32</td><td>5.08</td><td>2.19</td></tr><tr><td>Restrictive</td><td>28</td><td>5.80</td><td>1.23</td></tr><tr><td>T-test (one-tailed)</td><td colspan="3">t-statistic=-1.59, p&lt;0.05</td></tr></table>

## 5. Discussion

Researchers have called for more investigations of the role of KBS in improving novice designers’ data modeling tasks [14,30,49]. This research addressed the issue with an empirical study and found that novice designers’ performance improves significantly with the aid of a KBS. Novice designers’ performance was not significantly different when they used a restrictive instead of a guided interface but they rated the restrictive interface as being easier to use.

Note that all subjects received the same amount of training in data modeling procedures prior to the experiment. Yet, because the group using the KBS performed significantly better, the results indicate the usefulness of developing KBS that are tuned to address specific problems faced by novice designers. The difference in the data modeling score not being very large suggests that other design approaches to build the KBS could be investigated. Our design, focused on problems faced by novices, does not take advantage of data modeling patterns, which have been applied in the design of other KBS [38]. Future research could examine if this or other design approaches are more effective than the one utilized in this study. Note that the overall lower level of data modeling scores could be due to the fact that subjects in this study had very little experience and knowledge in data modeling and are at the lower continuum of novice designers [29]. Though we expected the KBS to reduce their cognitive load, the data-modeling task consisting of five entities and three relationships could have characterized a fairly complex task. Overall, these results indicate that a KBS designed to sequence the creation of relationships, prevent derived relationships, and provide help in formulating cardinality of relationships, i.e. a system geared towards providing additional support for modeling relationships, can help novice designers.

We did not observe any significant differences in novice designers’ performance attributable to the interface choice, and therefore we examined the process trace of a sample of our subjects to gather some insight. The log files indicated that some users did not heed the advice provided by the system i.e. they did not make the best design choices. We found instances when a subject heeded a message at one time but not at other times. Thus, despite intervention from the guidance system, some errors occurred. In the restrictive system, we found that when subjects made errors, these errors sometimes propagated because we had implemented a high level of restrictiveness in the system. For example, we enforced the rule that a binary one–many type relationships must be modeled before ternary relationships. If the user wished to model a newly discovered binary one–many relationship after having modeled a ternary relationship, he would have to delete the ternary relationship and add the binary relationship. Correction of errors and reversing earlier design decisions were harder with the restrictive system, and users sometimes chose not go back and correct the errors. Thus, errors were made with both interfaces reducing the quality of the data model.

Examining these results from a theoretical perspective, it is worth noting that Silver [45] does not describe restrictiveness and guidance as mutually exclusive categories. Instead, they are described as being interdependent. A high level of restrictiveness in a system that blocks many operators implies that the system provides very little guidance, and a system with a high level of guidance that advices at every stage, implies that the system will have a low level of restrictiveness. In our implementation of Silver’s framework, we enforced a very high level of restrictiveness in the restrictive version, because we thought that this approach would reduce the cognitive strain on the novice user, and they should have minimum responsibility for making design decisions. On the other hand, in the guidance system, we gave the users maximum responsibility for making design decisions by building a high level of guidance, and it gave many suggestive messages to the user. But, it was easy to ignore these system messages and as indicated in other studies [27], we also found that system advice was not followed in many instances. Hence, errors were made when using either of the interfaces and no interface resulted in a significantly superior score. However, in perceptual outcomes, as expected, the novice designer found the restrictive interface to be significantly easier-to use. Because design choices are influenced by the trade-off between improving ease-of-use vs. the functionality of a system [43], based on our results, more restrictiveness in a system appear to be more suitable for use by novice designers.

Taken together, these perceptual and performance results suggest some design modifications and ideas for building future systems. One design approach could be to build an interface that takes a more <sup>b</sup>middle of the road<sup>Q</sup> approach, in that the system need not have either a very high level of guidance or a high level of restrictiveness. Because the subjects rated the restrictive interface as being easier to user, the system could have a higher level of restrictiveness but it could also provide some guidance. For example, in certain situations, the system can be restrictive and prevent the creation of derived relationships. However, the system may permit the user easier to go back and correct prior relationships, and also provide advice when necessary. What needs to be determined are those instances in the data modeling process where guidance or restrictiveness will be most effective in helping a novice designer. Finding an optimal level of balance between guidance and restrictiveness may be the most suitable approach. Our observations also indicate that the design of the KBS could be improved by providing more feedback to the novice designer, which will allow him to understand the implications of various design choices. An E-R diagram could be converted to its equivalent relational model, and the relational model can be displayed to the user in simpler language. For example, if the user chooses one–many relationship between programmer entity and skills entity, the system can state: <sup>b</sup>This means that there can be only one programmer with a specific skill. Is that acceptable?<sup>Q</sup> Such real-time feedback on user’s design choices could potentially improve their decisions.

From a system design perspective, our results provide some suggestions. Even though guidance system has been found useful in many situations, the behavior of some of our subjects in not heeding system messages may explain those cases where the guidance interfaces was found to have no effect [51]. Please note that to the best of our knowledge, this is the first time that the two types of interfaces have been directly compared against one another in the conceptual modelling domain. Our results suggest that for each class of users and each task, the optimal level of restrictiveness/guidance may have to be determined. This corroborates Silver’s [45,46] recommendation that the extent to which the differing forms of decisional guidance and restrictiveness will be effective is not readily apparent and must be empirically determined in each domain. Because we found that some users did not heed system messages, it suggests that individual attitudes/differences may be an influencing factor similar to those found in experiments on research on CASE tools [20,21]. These factors have to be considered in future design and testing of KBS.

## 5.1. Limitations of the study

As in any experimental study, this study has several limitations. The study was conducted in a laboratory setting, and hence the internal validity is high, but the external validity has to be tested in real-world organizational environments. The lower level of external validity arises primarily due to the use of student subjects. However, in this study, because we were interested in the performance of novice designers, the use of students as subjects was reasonable to answer our research questions. Despite these limitations, our study indicates that KBS approaches to support novice database designers is useful and worth pursuing, particularly given that databases are going to be even more widely used [44] in the future. By combining system design with empirical tests, our study has provided some useful information to build upon.

## Appendix A. Knowledge-base in CODASYS

Overview

<sup>!</sup> CODASYS contains procedural knowledge of data modeling. It does not possess any application level knowledge. Hence, it cannot automatically associate an entity with an attribute (e.g., Customer and

Customer ID). Nor does it posses any understanding of what these application concepts mean.

<sup>!</sup> The user is expected to model all the entities before modeling the first relationship. This enables proper sequencing of relationships.

<sup>!</sup> Users can model binary and ternary relationships only. Unary and 4-way relationships cannot be modeled with this implementation of CODASYS.

<sup>!</sup> The E-R diagram is automatically redrawn whenever any change is made to the data model.

## Entity-related rules

<sup>!</sup> Each entity must have at least two attributes.

<sup>!</sup> Each entity can have one and only one attribute as the key-attribute.

<sup>!</sup> The non-key attributes are single-valued and they depend only on the key and nothing but the key attribute.

## Relationships-related rules

<sup>!</sup> All the binary one–many relationships are to be modeled first.

<sup>!</sup> For modeling relationships other than binary one– many, use only entities that are on the many sides of the binary relationships. These entities are called <sup>d</sup>free-entities<sup>T</sup>.

<sup>!</sup> If there are three or more free-entities, and if a ternary relationship appears likely, model a ternary one–one–many or a one–many–many relationship next.

<sup>!</sup> If there are three or more free-entities and a ternary relationship appears likely, model a many–many– many relationship next.

<sup>!</sup> After considering ternary relationships, if there are at least two free entities, binary many–many relationships may be modeled.

<sup>!</sup> When selecting entities for a relationship, only those entities that are neither a sub-set, nor a super-set nor an equal set of entities from another relationship may be used. This requirement is to prevent redundant relationships.

<sup>!</sup> If there are no more <sup>d</sup>free<sup>T</sup> entities, then there are no more relationships to be modeled.

## Cardinality-related rules

<sup>!</sup> Cardinality value is either <sup>d</sup>one<sup>T</sup> or <sup>d</sup>many<sup>T</sup>.

<sup>!</sup> Binary relationships have two cardinalities. If there is a relationship between two entities A and B, the cardinality of B is the number of instances of C that maps to one instance of A, and vice-versa.

<sup>!</sup> Ternary relationships have three cardinalities. If there is a relationship between three entities A, B, and C, the cardinality of C is the number of instances of C, that maps to one instance each of A and B. Similarly, the cardinalities of A and B can be determined.

Appendix B. Differences in interface implementations

<table><tr><td>The user</td><td>The guidance interface</td><td>The restrictive interface</td></tr><tr><td>Enters the name of a new entity</td><td>Reminds the user to model at least two attributes for an entity, but the user can use that entity in a relationship without assigning attributes to it.</td><td>Does not remind the user to assign two attributes, but entities without two attributes cannot be used in relationships.</td></tr><tr><td>Saves an entity without specifying its key attribute</td><td>Reminds the user to define key attribute.</td><td>Will not save the entity until a key attribute has been defined.</td></tr><tr><td>Specifies the key attribute for an entity</td><td>Reminds the user to verify uniqueness of the key attribute</td><td>Asks the user whether the key attribute is unique or not; user answers yes or no.</td></tr><tr><td>Chooses the relationship menu</td><td>Recommends the use of a sequence of relationships to model.</td><td>Forces the user to model a specific type relationship.</td></tr><tr><td>Tries to select a non-free entity for a relationship</td><td>Advises the user against use of a non-free entity, but does not prevent him/her from using it.</td><td>Blocks the use of non-free entities, by not displaying that entity.</td></tr><tr><td>Tries to determine connectivity of the relationship</td><td>Formulates questions to help determine the connectivity.</td><td>Formulates the question and also fills in the cardinalities if possible.</td></tr><tr><td>Is using any window within the application</td><td>Allows all controls to be accessed.</td><td>Does not allow access to all controls, but only a specific set of controls is enabled at any time, including menu options.</td></tr><tr><td>Tries to delete a relationship</td><td>Allows the deletion of any relationship, and will free up relevant entities so that they can be used later for more relationships.</td><td>Allows deletion of only the most recently modeled relationship.</td></tr><tr><td>Tries to modify a relationship</td><td>Allows the user to modify any relationship.</td><td>Allows modification of only the most recently modeled relationship.</td></tr><tr><td>Attempts to use a sub-set of or super-set of or same set of entities in two relationships</td><td>Advices the user about derived relationship; but does not prevent him/her from doing so.</td><td>Once a relationship has been declared the same entities cannot participate in another relationship. User will be unable to select them.</td></tr></table>

## References

[1] D.A. Adams, R.R. Nelson, P.A. Todd, Perceived usefulness, ease of use and usage of information technology: a replication, MIS Quarterly 16 (1992) 227– 247.

[2] S.R. Antony, D. Batra, CODASYS: a consulting tool for novice database designers, Data Base for Advances in Information Systems 33 (3) (2002 Summer) 54– 88.

[3] C. Batini, S. Ceri, S.B. Navathe, Conceptual Database Design: An Entity-Relationship Approach, Benjamin Cummings, Redwood City, CA, 1992.

[4] D. Batra, S.R. Antony, Novice errors in conceptual database design, European Journal of Information Systems 3 (1) (1994) 57– 69.

[5] D. Batra, S.H. Zanakis, A conceptual database design approach based on rules and heuristics, European Journal of Information Systems 3 (3) (1994) 228 – 239.

[6] D. Batra, J.A. Hoffer, R.P. Bostrom, Comparing representations with the relational and extended entity relationship models, Communications of the ACM 33 (1990) 126– 139.

[7] I. Benbasat, A.S. Dexter, P.S. Marulis, An experimental study of the human computer interface, Communications of the ACM 24 (11) (1981) 752 – 762.

[8] C. Billings, M. Billings, J. Tower, Rapid Application Development with Oracle Designer/2000, Addison Wesley Publishing, Reading, MA, 1997.

[9] D.B. Bock, T. Ryan, Accuracy in modeling with extended entity relationship and object-oriented data models, Journal of Database Management 4 (4) (1993) 30–39.

[10] J.C. Brancheau, C.V. Brown, The management of end-user computing: status and directions, ACM Computing Surveys 25 (4) (1993) 437– 482.

[11] J.M. Carroll, J. McKendree, Interface design issues for advicegiving expert systems, Communications of the ACM 30 (1) (1987) 14– 32.

[12] P.P. Chen, The entity-relationship model-toward unified view of data, ACM Transactions on Database Systems 1 (1976) 9– 36.

[13] L. Chidambaram, Knowledge transfer in conceptual modeling by end users, Journal of End User Computing 11 (1) (1999 Jan–March) 40– 51.

[14] J. Choobineh, B.R. Konsynski, M.V. Mannino, J.F. Nunamaker, An expert system based on analysis of forms, IEEE Transactions on Software Engineering 14 (2) (1988) 242 – 253.

[15] E. Codd, A relational model for large shared data banks, Communications of the ACM 13 (6) (1970) 377–387.

[16] J. Cohen, Coefficient of agreement for nominal scales, Educational and Psychological Measurement 1 (1960) 37 – 46.

[17] F.D. Davis, Perceived usefulness, perceived ease of use and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 318– 340.

[18] F.D. Davis, R. Bagozzi, P. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 (8) (1989) 982–1003.

[19] B.C. Desai, An Introduction to Database Systems, West Publishing, St. Paul, MN, 1990.

[20] D. Dey, User responses to constraints in computerized design tools, Unpublished doctoral dissertation (School of Information Studies, Syracuse University, NY 1995).

[21] D. Dey, V.C. Storey, T.M. Barron, Improving database design through the analysis of relationships, ACM Transactions on Database Systems 24 (4) (1999) 453 – 486.

[22] B.L. Dos Santos, M.L. Bariff, A study of user interface aids for model-oriented decision support systems, Management Science 34 (4) (1988) 461– 468.

[23] D.T. Edberg, B.J. Bowman, User-developed applications: an empirical study of application quality and development productivity, Journal of MIS 13 (1) (1996) 167 – 186.

[24] B.C. Hardgrave, N.P. Dalal, Comparing object-oriented and extended entity relationship data models, Journal of Database Management (1995 Summer) 15–21.

[25] K. Hawryszkiewycz, A computer aid for E-R modeling, Proceedings of the Fourth International Conference on Entity Relationship Approach, North-Holland, Chicago, IL, 1985, pp. 64 – 69.

[26] A.R. Hendrickson, P.D. Massey, T.P. Cronan, On the test– retest reliability of perceived usefulness and perceived ease-ofuse, MIS Quarterly 17 (2) (1993) 227–230.

[27] W.C. Hill, How some advice fails, Proceedings of CHI 89, ACM Press, Austin, Texas, 1989.

[28] N.D. Kerlinger, Foundations of Behavioral Research, 3rd edition, Holt, Rinehart and Winston, New York, 1986.

[29] D.M. Lamberti, W.W. Wallace, Intelligent interface design: an empirical assessment of knowledge presentation in expert systems, MIS Quarterly 14 (3) (1990) 279–311.

[30] A.W. Lo, J. Choobineh, Knowledge-based systems as database design tools: a comparative study, Journal of Database Management 10 (3) (1999) 26 – 40.

[31] Logic Works, Erwin Methods Guide, Logic Works, Princeton, NJ, 1997.

[32] J. Mao, I. Benbasat, The use of explanations in knowledgebased systems: cognitive perspectives and a process-tracing analysis, Journal of Management Information Systems 17 (2) (2000) 159– 173.

[33] J. Martin, J. Leben, Client/Server Databases: Enterprise Computing, Prentice-Hall, Upper Saddle River, NJ, 1995.

[34] F.R. McFadden, J.A. Hoffer, M.B. Prescott, Modern Database Management, Prentice Hall, Upper Saddle River, NJ, 1999.

[35] L. Moez, Automating decision guidance: design and impacts in a group decision environment, Unpublished doctoral dissertation. (Carlson School of Management. University of Minnesota, MN 1992).

[36] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2) (2001) 303 – 331.

[37] J.W. Payne, J. Bettman, E.J. Johnson, The Adaptive Decision-Maker, Cambridge Univ. Press, New-York, 1993.

[38] S. Purao, APSARA: a tool to automate system design via intelligent pattern retrieval and synthesis, Data Base 29 (4) (1998) 45– 57.

[39] J. Reason, Human Error, Cambridge Univ. Press, Cambridge, 1990.

[40] J.F. Rockart, L.S. Flannery, The management of end-user computing, Communications of the ACM 26 (10) (1983) 776–784.

[41] R. Santhanam, J. Elam, A survey of knowledge-based systems research in decision sciences (1980–1995), Journal of the Operational Research 49 (5) (1998) 445– 457.

[42] A.W. Scheer, Enterprise-wide Data Modeling: Information Systems in Industry, Springer Verlag, Berlin, 1989.

[43] B. Schneiderman, Designing the User Interface: Strategies for Effective Human–Computer Interaction, Addison-Wesley, Reading, MA, 1987.

[44] B.A. Schuldt, Database challenges for the new millennium, Journal of Database Management 11 (1) (2000) 41– 42.

[45] M.S. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 (1) (1990) 47– 70.

[46] M.S. Silver, Systems that Support Decision Makers: Description and Analysis, John Wiley, Chichester, England, 1991.

[47] I.Y. Song, T.H. Jones, E.K. Park, Binary relationship imposition rules on ternary Relationships in ER modeling, Information & Knowledge Management 11 (1993) 57 – 66.

[48] V.C. Storey, View Creation: An Expert System for Database Design, ICIT Press, Washington, DC, 1988.

[49] V.C. Storey, R.C. Goldstein, Knowledge-based approaches to database design, MIS Quarterly 17 (1) (1993) 25 – 46.

[50] T.J. Teorey, D. Yang, J.F. Fry, A logical design methodology for relational databases using the extended entity-relationship model, Computing Surveys 18 (2) (1986) 197–222.

[51] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection, Information Systems Research 10 (4) (1999) 356 – 374.

[52] N.Y. Tractinsky, Effects of DSS restrictiveness on decision making under time pressure, PhD Dissertation (University of Texas at Austin 1993).

[53] E. Turban, E. McClean, J. Wetherbe, Information Technology and Management, John Wiley, New York, 1999.

[54] B.C. Wheeler, B.E. Mennecke, J.N. Scudder, Restrictive group support systems as a source of process structure for high and low procedural order groups, Small Group Research 24 (1993) 504– 522.

[55] E.V. Wilson, I. Zigurs, Decisional guidance and end-user display choices, Accounting, Management, Information Technologies 9 (1) (1999) 49 – 75.

[56] L.R. Ye, P.E. Johnson, The impact of explanation facilities on user acceptance of expert systems advice, MIS Quarterly 19 (2) (1995) 157– 171.

Solomon Antony is an Assistant Professor in the Rawls College of Business Administration at Texas Tech University. His publications have appeared in Data Base, International Journal of Human Computer Studies, European Journal of Information Systems, Omega, European Journal of Operational Research, and Control and Cybernetics. His research interests are in data modeling, problem solving and knowledge-based systems.

Dinesh Batra is an Associate Professor in the College of Business Administration at the Florida International University. His publications have appeared in, Management Science, Communications of the ACM, Journal of MIS, Data Base, European Journal of Information Systems, International Journal of Human Computer Studies, Computers and Operations Research, Information and Management, Journal of Database Management, and others. His research interests focus on usability issues in database design and use, and knowledgebased systems.

Radhika Santhanam is a Gatton Research Professor in the area of Decision Sciences and Information Systems Gatton School Business and Economics, at the University of Kentucky. She investigates issues relating to human computer interaction and the use of management support systems. Her findings have been published in a variety of journals such as Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Decision Support Systems, European Journal of Operational Research and Computers and Operations Research, among others. She currently serves on the editorial board of MIS Quarterly, Decision Support Systems, and Computers and Operations Research.
