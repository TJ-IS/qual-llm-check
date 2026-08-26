---
otero_id: 18855
otero_key: "ABBCFBUN"
title: "Selection of a good expert system shell for instructional purposes in business"
authors: "Chung S. Kim; Youngohc Yoon"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90056-l"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Selection of a good expert system shell for instructional purposes in business

Chung S. Kim and Youngohc Yoon
Southwest Missouri State University, Springfield MO, USA

Expert systems (ES) have become very important tools in making decisions in business. In order to meet the rising demand for both technical and managerial skills for ES, many business schools have started to use ES shells to teach students the concepts and skills necessary to develop various ES applications, but little research has been done in evaluating expert shells for instructional purposes. This paper develops a model for selecting the most appropriate expert shell as an instructional tool for an ES course. The instructional objectives of incorporating expert shells in a learning environment are discussed and a set of evaluation criteria are developed. Then an evaluation model is presented; it is to be used to select the best shell under different class environments. An illustrative example is also presented.

Keywords: Selection of expert system (ES) shells, ES shells for business instruction, Bloom's learning model, Evaluation of microcomputer ES shells, Analytic hierarchy process (AHP) method.

![](/api/attachments/ABBCFBUN/fulltext/images/7dcc25ef7c9c14729d443efa6fd0ab15443d37c023b3b511833d16f8b3e4fc4d.jpg)  
ORSA, and IACIS.

Chung S. Kim is an Assistant professor in the Department of Computer Information Systems at Southwest Missouri State University. She received her MBA from the University of Missouri in St. Louis and her Ph.D. from the Texas Tech University. She has recently published articles in the Journal of Computer Information Systems, and the International Journal of Management Science and Information Systems. Dr. Kim is a member of the Decision Sciences Institute, TIMS/

Correspondence to: C.S. Kim, Computer Information Systems Department, Southwest Missouri State University, 901 South National, Springfield, MO 65804, USA. Tel: (417) 836-4131.

## 1. Introduction

An expert system (ES) is a computer program that encapsulates the problem-solving knowledge of human experts in order to attain high levels of performance in a narrow problem domain. Many successful ES applications have been reported, e.g., in loan approval, the diagnosis of malfunctioning machinery, and training novices. The value of these ES is that they provide a means of capturing and using expertise in a particular field, which in turn improves the productivity and competitiveness of the company. For example, the use of an ES called XCON has saved DEC company \$40 million annually. Furthermore, each of Dupont's ES saves them approximately \$100 000, while each cost only an average of \$25 000 to develop [24].

There are two major alternatives in developing an ES: One way is to develop a system from scratch using a programming language such as Lisp or Prologue; the other way is to build a system with an ES building tool called a shell. Using a programming language requires an ES developer to construct not only a knowledge base, but also an inference engine and an explanation facility. On the other hand, an ES shell has a knowledge base editor, an inference engine, an

![](/api/attachments/ABBCFBUN/fulltext/images/6d955ee3bf3ae41f2bda9d65042e2c86f000da87fcb2fa3f174c6d409d648767.jpg)  
ciation for Artificial Intelligence, ACM SIGBDP, and IEEE Computer Society.

Youngohc Yoon is an Assistant Professor in the Department of Computer Information Systems at Southwest Missouri State University. She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. She has recently published articles in Data Base, the Journal of Neural Network Computing, and Expert Systems. Dr. Yoon is a member of the Decision Sciences Institute, International Neural Network Society, American Asso explanation facility, debugging aids, and other useful facilities which are already built into the system. The major task of an ES developer when using an ES shell is to acquire knowledge from human experts and then store them in a knowledge base via a knowledge-based editor. Thus, using an ES shell saves the developer significant time and effort in developing an ES application.

As inexpensive and easy-to-use ES shells are readily available on the market, managers have started to participate directly in developing various ES applications. The ability to create and manage ES applications has thus become an important skill not only for prospective MIS personnel but also for prospective managers $[22]$ . In order to meet a rising demand for both technical and managerial skills in ES development, many schools are incorporating ES courses into their curricula $[39]$ . These schools are often using ES shells, since the shells help students acquire basic concepts of an ES as well as the practical skills of building an ES application $[3,6]$ .

Students can build a prototype ES application within a short time period, if an ES shell is used. Since these students do not have to build an ES from scratch, they can concentrate on the development of a knowledge base. According to Mockler [26], most of the time spent in the development of a business ES application involves understanding and modeling a manager's decision process. Thus, actually acquiring and encoding the knowledge of a specific domain allows students to gain a better understanding of the managerial decision-making processes in that domain and the application development processes. Because the ES shells in today's market are similar in knowledge representation and inferencing processing, the knowledge and experience obtained using one shell can be easily transferable to building an ES application using a different shell.

Selection of an ES shell for instructional purposes requires a different set of criteria from that of selecting an ES shell for business applications. An ES shell for business applications requires power, capacity, and technical sophistication to solve large real-world problems; however, a shell used for instructional purposes should help students learn ES concepts and basic skills necessary for building an ES. One ES shell might be superior in technology, features, and level of sophistication compared to another, but it may not be a proper shell for instructional purposes unless it helps achieve the course objectives.

There are currently several dozen ES shells on the market, and they vary in their capabilities, features, and sophistication level. Since there is no single ES shell which dominates others in all respects, it is difficult to evaluate them. Although many guidelines and suggestions have been presented for the selection of ES shells for a real application development $[15,16,21,27,35,36,40]$ , few guidelines are available about their selection as media for instructional purposes. This paper presents such an evaluation model.

## 2. Shell objectives

The objectives of using an ES shell can be refined in light of the learning model developed by Bloom et al. [5]. They describe learning objectives in six different levels: Knowledge, comprehension, application, analysis, synthesis, and evaluation [41]. The lecture-oriented instruction of an ES can lead students to the knowledge and possibly to the comprehension learning levels. However, hands-on exercises are essential for students to reach the higher learning levels.

(1) On the knowledge and comprehension levels, a shell is used to demonstrate a working ES in order to help students comprehend the concepts, the function of each component, and their interactions in an inferencing process. Students also learn about ES potential as an aid in managerial decision-making.

(2) On the application level, students learn to apply methodologies and techniques to real managerial problem domains. A shell can be used to review various ES examples. It can also be used to apply various knowledge acquisitions, knowledge representations, and inference methods to different problem domains.

(3) On the analysis and synthesis levels, a shell is used to design and build a prototype which can support managerial decisions. Students analyze a problem and elicit the domain knowledge necessary to solve the problem. They then synthesize this knowledge and represent it in a knowledge base. They may also build an integrated system which can interface with another software package.

(4) On the evaluation level, the shell is used to promote the evaluation capability of students; students should be able to evaluate their own ES as well as the ES shell used in their prototyping process. This objective can be accomplished through the presentation and discussion of their projects.

Different courses may require different emphases on each level of shell objectives. For instance, an introductory ES course or a non-computer-major course may put more emphasis on the comprehension level of the shell objectives, while an advanced ES course may put more emphasis on higher levels. The learning objectives, the related course topics, and the related shell objectives are summarized in Table 1.

## 3. Evaluation criteria

The objectives of using an ES shell in a classroom environment produce the eight evaluation criteria and features shown in Table 2.

## 3.1. Capability of demonstrating session activities

In order for an ES shell to enhance the understanding of the basic concepts of the use of ES, demonstration of the session activities is very important. The function of each component of an ES shell should be quite transparent to a user during a session. A shell should demonstrate which step it has accomplished and how it did it, what rules the inference engine has used, its current goal, the contents of the working mem-

Learning objectives, topics, shell objectives.

<table><tr><td>Learning objectives</td><td>Course topics</td><td>Shell objectives</td></tr><tr><td>Knowledge &amp; comprehension level</td><td>ES Concepts- ES architecture- ES components- ES vs. other information systems</td><td>ES Concepts- ES components- Interactions of the components in an inferencing processingES potential</td></tr><tr><td>Application level</td><td>Domain selectionCase studiesLab exercisesApplying different ES techniques</td><td>Examination of working ES examplesApply different KA, KR, &amp; inference mechanisms</td></tr><tr><td>Analysis &amp; Synthesis level</td><td>Prototyping methodsProject development requirement- Identification- Conceptualization- Formalization &amp; representation- Implementation &amp; integration- Validation &amp; verification</td><td>Prototyping development-simple prototype-complex prototype-integration with other systems</td></tr><tr><td>Evaluation level</td><td>Evaluation of managerial &amp; social implicationsEvaluation of Various ES shells</td><td>Product evaluationProcedure evaluation-the prototyping process-the shell used-the finished ES</td></tr></table>

E5 evaluation criteria and related features.

1. Capability of demonstrating session activities:
Display of the contents of the working memory;
Display of intermediate goals; and
Display of rules being used.
2. Capability of end-user supporting facilities:
Explanation facilities: How, Why, What If?
Input/Output facilities.
3. Flexibility of knowledge representation (KR) and inference mechanisms:
Knowledge representations (KR):
Rule, frame, example.
Inferencing Mechanisms:
Forward, backward, agenda manager,
Demon, confidence calculation.
4. Availability of Development Support Facilities:
Debugging aids, knowledge base editor, syntax checking, consistency checking, case facilities, rule induction.
5. Accessibility of external programs:
With database, spreadsheet, ASCII file, other software packages.
6. Documentation and Supporting Service:
Sample applications, documentation (user manuals), supporting books, on-line tutorial, hot-line service.
7. Ease of use/case of learning:
Hypertext, natural language interface,
speech interface, context sensitive help,
consistent commands throughout the subsystems, meaningful identifiers (labels).

ory, and the change of these over time. Displaying this information during a consultation process helps users understand the key concepts of an ES. Some shells reveal only those session activities that occur during the inferencing process. For instructional purposes, however, it is better to display the complete operation of each session; thus, separate windows designed to show the basic operation are more informative and helpful.

## 3.2. Capability of end-user supporting facilities

The end-user supporting facilities include input/output facilities and explanation mechanisms. In particular, the explanation facility is considered the most important quality of an expert system [42]. Together, this helps a user understand the decision path.

## 3.3. Flexibility of knowledge representations (KR) and inference mechanisms

There are various KR schemes used in building a knowledge base: Rules, frames, examples, etc. [4]. Each has advantages and disadvantages in representing knowledge [28]. In order to exploit the advantages and overcome the disadvantages, two or more representation methods are usually necessary in the development of a knowledge base [13]. Therefore, it is important for students to comprehend the methods: Their schemes, operations, pros and cons. It is fairly easy for students to understand the rule and to use its scheme, but it is more difficult for them to comprehend the frame system. An ES shell with frame knowledge representation can be useful not only in guiding a student in representing an object and its properties, but also in demonstrating the function of each slot and demon for solving a problem. Hands-on experience in representing knowledge in various methods significantly enhances the students' comprehension.

Just as there are a variety of methods for knowledge representation, there are also many different ways to process the inference, such as forward/backward reasoning [7], agenda mechanisms [17], truth maintenance systems [10], etc. Utilization of the various inferencing mechanisms can enrich a student's experience and improve understanding. Therefore, the flexibility of knowledge representation methods and inference mechanisms becomes an important evaluation criteria.

## 3.4. Availability of development support facilities

The supporting tools for a knowledge engineer include editors, debugging aids (trace and break package), and rule induction. The trace facility provides a user with a display of system operations, usually by listing the names of the rules executed. The break package enables a user to stop the system to examine it for possible error. The induction facility selects a set of decision rules from the list of training examples so that a user does not have to specify the functional relationship between variables in solving a problem. These supporting facilities are an extra software package that makes the ES shell easier, friendlier, and more efficient. The availability of these tools determines the usefulness of an ES shell for quick construction of an ES.

## 3.5. Accessibility of external programs

The ability to interface with other systems, such as a text editor, spreadsheet, data base, or a fourth-generation language, is important in using an ES shell. As a recent development, more software packages tend to be integrated in order to expand the functionality of a single entity (system). An ES is no longer viewed as a separate entity but rather as a subset of information technologies used to address problems $[8,18,23]$ . Thus, students need to understand how an ES can integrate with other software, especially with a data base as a means of providing more intelligent decision support.

## 3.6. Documentation and supporting service

The user's manual should be self-explanatory, detailed, and complete. A well-written manual will aid users in learning how to use the software with relative ease. Other important documents are the supporting textbooks which provide the comprehensive guidelines for using an ES shell and some excellent sample expert systems [14,19,37]. Such books utilize a particular shell and are excellent resources. The availability of help and self-paced tutorial programs is also very important, especially when attempting to learn the system without extended help.

## 3.7. Ease of use / ease of learning

An ES shell should provide features that facilitate easy development and use of an application. Ease of use includes (but is not limited to): A natural language interface, a speech interface, hypertext, an on-line tutorial, context-sensitive help, and a menu-driven command structure. A natural language facility enables a user to define rules and concepts using 'ordinary' English. Users can then question the knowledge base in English. The speech interface further simplifies the use of an ES shell. A hypertext facility makes it easy for users to reveal a more complete description of the highlighted picture on the screen to increase their understanding. A context-sensitive help facility is also very useful for accessing reference information on-line as needed. The on-line help documentation should be organized in a hierarchical fashion, allowing a user to access additional, more detailed levels of help text in a specific situation. Also important are consistent commands through different levels of subsystems, convenient menus and prompts, meaningful terms and labels, easy knowledge-base data editing, and a simple means of executing commands.

Shell objectives and related criteria

<table><tr><td>Shell objectives</td><td>Criteria</td></tr><tr><td>1. Basic concept of an ES- components of ES- interaction of the componentsES potential</td><td>Capability of monitoring session activities- rules- working memory- intermediate goalsAvailability of end-user supporting facilities</td></tr><tr><td>2. Examples of working ES- knowledge bases- inference methodsLearn and apply different KR and inference techniques</td><td>Availability of good sample ESFlexibility of inference methodsFlexibility of KRAccessibility of external programs</td></tr><tr><td>3. Prototyping- simple prototype construction</td><td>Rule induction (development support facilities)Flexibility of KR</td></tr><tr><td>- complex prototype construction</td><td>Flexibility of inference methodsDocumentation &amp; supporting service</td></tr><tr><td>- integration with other systems</td><td>Availability of development support facilityEase of use/easy to learnAccessibility of external programs</td></tr><tr><td>4. Prototype evaluation</td><td>All of the above criteria</td></tr></table>

These seven evaluation criteria are all necessary to aid in the selection of the best ES shell for an instructional environment. While most criteria are necessary to achieve each objective, some criteria may be more important in accomplishing a specific shell objective. Therefore, the evaluation criteria are categorized according to the related shell objectives (redundant grouping is allowed) as shown in Table 3.

## 4. The evaluation model

The shell objectives and the evaluation criteria discussed above are incorporated into the evaluation model using the analytic hierarchy process (AHP) method [30,31]. The AHP method structures any complex, multi-criterion, multi-person, and multi-period problem into a hierarchical model. The elements on the higher levels of the hierarchy represent more general issues, such as objectives, while the elements on the lower level indicate more detailed issues, such as criteria or alternatives. On each level, each pair of elements is compared in terms of its relative importance in accomplishing a higher-level objective. Through this process, a matrix of pair-wise comparisons is constructed for each level, where each matrix entry indicates the strength with which one element dominates another (relative to a given criterion at the higher level). This scaling formulation is translated into a largest eigenvalue problem, which results in a normalized and unique vector of weights for each level of the hierarchy. In turn, the weight vectors of all levels are synthesized into a single composite vector of weights for the entire hierarchy. This measures the relative priority of all entities at the lowest level in terms of their strength in accomplishing the highest objective of the hierarchy.

The AHP technique uses a 9-point scale to assess the intensity of dominance of each element over the other. This scale is used to express judgment in making pair-wise comparisons: 1 for equal; 3 for moderate; 5 for strong; 7 for very strong, 9 for extreme; reciprocals are used for an inverse comparison. Assuming that there are n elements on the stratum L, the pair-wise comparison among n elements with respect to an element in the higher level will result in an $(n \times n)$ matrix. The principal eigenvector of this matrix is then derived and weighed by the priority of the corresponding objective. This process continues for all elements in the higher level and for all levels until the final weight vector is calculated at the lowest level.

Although other models are also available for computer system evaluation and selection $[33,34]$ , including multi-attribute utility and scoring models, there are several advantages of using the AHP. First, the AHP uses the systems approach and the problem is evaluated in the context of the degree to which the higher level objectives are accomplished. Since various ES shells can be evaluated in terms of their contribution to the course objectives, this method is valid.

Second, the AHP method induces users to make comparable measures through pairwise comparisons, instead of forcing them to assign weights. The AHP facilitates group discussion and can handle qualitative criteria of fuzzy and complex problems.

Third, the consistency of judgments is checked; if the decision-maker's judgment is not consistent throughout the procedure, the decision-maker should reevaluate the process. Saaty considers a consistency ratio of 10% or less acceptable. When the degree of consistency is poor, it is necessary to get more information; this typically involves re-collecting data in another round. (See also [43,44].)

Fourth, the model of the AHP is stable and flexible: Small changes in a local area of the model do not affect the entire model, and different objectives and scenarios can be evaluated using the model. For instance, a reduced set of objectives and criteria that are considered more important can be used in the evaluation model.

Lastly, there is a convenient AHP software package available for use (Expert Choice by Decision Support Systems, Inc.).

The evaluation model for ES shells using the AHP method is shown in Figure 1. On the highest level of the model, the shell objectives are evaluated in terms of their contributions to the overall objectives. On the second level, the criteria are evaluated in terms of their importance in accomplishing individual shell objectives. On the last level, the candidate shells are evaluated in terms of their strengths relative to each criteria. When the measures of all levels are synthesized, the strength of each candidate ES shell in accomplishing shell objectives is computed and used as a weight.

![](/api/attachments/ABBCFBUN/fulltext/images/c16e4055f670a978ad5b52045da1b888e3868421ec46e0a56cf7aee41569c73b.jpg)  
Fig. 1. The evaluation model for ES shells.

![](/api/attachments/ABBCFBUN/fulltext/images/770c5a83b1d55ee7e8a0b7640c10ae26e215ec0750dc21f51b56ee716762e5ad.jpg)  
Fig. 2. Evaluation of four ES shells for an ES course.

## 5. Application of the model

## 5.1. Selection of the course and candidate ES shells

To illustrate the use of the evaluation model presented earlier, an introductory ES course was selected. It is first necessary to examine the course objectives and contents so that more concrete shell objectives can be defined. The objectives of an introductory-level ES course with a well-balanced technical and non-technical emphasis, as typically offered in business schools, generally encompass the five dimensions of basic ES concepts, ES application, prototype development, ES evaluation, and ES impact. The relevant topics are similar to the ones shown in Table 1.

Once the course objectives and content are examined, candidate ES shells should be selected for closer examination in terms of price, hardware/software compatibility, and sophistication. There are several dozen ES shells on the United States market; they vary considerably in capability, price, sophistication, and technology (see Appendix A). The most commonly used shells are listed in Table 4, according to their level of sophistication [9]. The four ES shells selected for evaluation for this ES course are 1st class [1], Level 5 object [20], Exsys Professional [12], and VP-Expert [29]. All four shells have a low level of sophistication, are relatively easy to use, run on a PC, and cost less than \$1000.

## 5.2. Evaluation of ES shells using expert choice

Expert Choice is the software which implements the AHP method. In our case, the users are the instructors of the ES course. The evaluation model is constructed as shown in Figure 2. The first level is the general objective of evaluating ES shells according to course goals. The second level represents the shell objectives. The third level indicates the evaluation criteria. The fourth layer represents the four candidate ES shells.

The input data to the system are the judgmental comparison data of the decision makers. For instance, the comparison between a pair of objectives is given a numeric value when the decision maker selects from a menu, as shown in Figure 3. These comparisons are converted into the weights of individual elements which are the output data.

![](/api/attachments/ABBCFBUN/fulltext/images/bd2a6a3fefcab9345b1ac1bc096e7b9c49781073b4d37a8b3aaa159b123f10df.jpg)  
Fig. 3. Comparison of the shell objectives.

The evaluation starts with the pair-wise comparison of the shell objectives. The four objectives are evaluated resulting in the weights. For this introductory course, the objective of comprehending ES concepts is considered as important as the objective of prototyping. The objective of learning and applying different ES techniques is also considered somewhat important.

Next, each pair of criteria is compared in terms of their importance in accomplishing each objective. For example, criteria 1 (demonstration capability) and 2 (end-user supporting facilities) are evaluated in terms of their importance in achieving the first objective, learning ES concepts. Next, criteria 1 and 3 are evaluated, followed by the criteria 1 and 4 and so on. In order to estimate the consistency of the judgment, redundant comparisons are imposed: Criterion 2 is paired with 3, 4, and so on until criterion 6 is paired with 7. When all criteria are compared with respect to the first objective, the same procedure continues for the second, third, and fourth objectives. The resulting weights and the consistency ratio are shown in Table 5.

Table 4  
ES shells by sophistication levels

<table><tr><td>Level of sophistication</td><td>Expert system shells</td></tr><tr><td>High</td><td>KEE, ART, Knowledge craft, KBMS, ADS-MVS, ESE, G2</td></tr><tr><td>Medium</td><td>Goldworks, Nexpert object, GURU, ART-IM, KAPPA</td></tr><tr><td>Low</td><td>Level 5 object, Exsys professional, 1st-Class, VP-expert, Logic tree Expert edge, Instant expert</td></tr></table>

Table 5  
Local weights and synthesized weights.

<table><tr><td colspan="3">Shell objectives:</td></tr><tr><td>I.</td><td>ES concepts:</td><td>0.351</td></tr><tr><td>II.</td><td>Application of ES:</td><td>0.189</td></tr><tr><td>III.</td><td>Prototyping:</td><td>0.351</td></tr><tr><td>IV.</td><td>ES Evaluation:</td><td>0.109</td></tr></table>

Evaluation criteria with respect to each objective

<table><tr><td>Criteria</td><td>I</td><td>II</td><td>III</td><td>IV</td><td>Synthe-sized</td></tr><tr><td>1. Demonstration</td><td>0.258</td><td>0.092</td><td>0.061</td><td>0.088</td><td>0.139</td></tr><tr><td>2. End-user support</td><td>0.179</td><td>0.150</td><td>0.068</td><td>0.108</td><td>0.127</td></tr><tr><td>3. Flexibility of ES techniques</td><td>0.099</td><td>0.241</td><td>0.132</td><td>0.229</td><td>0.152</td></tr><tr><td>4. Developer support</td><td>0.099</td><td>0.083</td><td>0.299</td><td>0.243</td><td>0.183</td></tr><tr><td>5. External programs</td><td>0.092</td><td>0.141</td><td>0.116</td><td>0.121</td><td>0.113</td></tr><tr><td>6. Documentation</td><td>0.110</td><td>0.196</td><td>0.116</td><td>0.108</td><td>0.129</td></tr><tr><td>7. Ease of use</td><td>0.163</td><td>0.098</td><td>0.208</td><td>0.102</td><td>0.16</td></tr></table>

<table><tr><td>Criteria</td><td>1-ST class</td><td>Level-5</td><td>Exsys Prof.</td><td>Vp-expert</td></tr><tr><td>1. Demonstration</td><td>0.141</td><td>0.141</td><td>0.263</td><td>0.455</td></tr><tr><td>2. End-user support</td><td>0.087</td><td>0.428</td><td>0.200</td><td>0.284</td></tr><tr><td>3. Flexibility of ES techniques</td><td>0.121</td><td>0.464</td><td>0.304</td><td>0.111</td></tr><tr><td>4. Developer support</td><td>0.099</td><td>0.518</td><td>0.284</td><td>0.099</td></tr><tr><td>5. External programs</td><td>0.109</td><td>0.485</td><td>0.297</td><td>0.109</td></tr><tr><td>6. Documentation</td><td>0.500</td><td>0.167</td><td>0.167</td><td>0.167</td></tr><tr><td>7. Ease of use</td><td>0.395</td><td>0.089</td><td>0.161</td><td>0.355</td></tr><tr><td>Synthesized weights</td><td>0.206</td><td>0.329</td><td>0.240</td><td>0.225</td></tr><tr><td colspan="5">Overall consistency rate = 0.01</td></tr></table>

Finally the four ES shells are evaluated in terms of their strength in each criteria; the results are also shown in Table 5. The checklist used to examine the strength of each shell relative to each criterion is listed in Appendix B. The final weights for each objective, criteria, and shell are shown in Figure 2.

## 6. Conclusion

Selecting an appropriate shell is important in order to accomplish the intended goals of a course. Here, the shell objectives and evaluation criteria are discussed and organized into an hierarchical model so that all components can be evaluated within one framework. In this model, the candidate shells are not evaluated according to the technological superiority of the shell but according to the needs of the course. The model is flexible, since different courses with different objectives can modify and utilize it for their unique needs.

The ES shells available on the market are versatile in nature, and ES technology is undergoing rapid advancement. While the evaluation model presented here is intended to provide a framework for the evaluation of ES shells that are rapidly changing, the checklist of the criteria may have to be updated frequently.

While the emphasis of the paper is on a typical ES course for information systems majors in a business school, a similar approach can be taken to select the best shell under different class environments including higher-level ES courses and for end-user training. Also, the evaluation criteria and checklist can be further refined so that various ES shells can be evaluated for many different environments and scenarios. If a school has many courses which incorporate ES concepts into their curricula using a single ES shell, then the analysis can start at a macro level so that the needs of these courses can be combined into the evaluation model.

## References

[1] AI Corp. Product Descriptions of 1st Class, 1990.

[2] Ashmore, G.M. “Applying Expert Systems to Business Strategy,” The Journal of Business Strategy, September/October 1989, pp. 46–49.

[3] Bahill, A.T. and Ferrell, W.R. “Teaching an Introductory Course in Expert Systems”, IEEE Expert, Winter 1987, pp. 59–63.

[4] Barr, A. and Feigenbaum, E. The Handbook of Artificial Intelligence, William Kaufmann, 1981.

[5] Bloom, B. et al., eds. Taxonomy of Educational Objectives, Handbook I, Cognitive Domain, edited by David McKay, New York, 1956.

[6] Brown, D.C. "A Graduate-Level Expert Systems Course", AI Magazine, Fall 1987, pp. 33–39.

[7] Buchanan, B. and Shortliffe, E., eds. Rule-Based Expert Systems, Addison-Wesley, Reading, MA, 1984.

[8] Cohen, B. "Merging Expert Systems and Databases", AI Expert, Vol. 4, No. 2, 1989, pp. 22-31.

[9] Davis, R. and Loofbourrow, T. "Evaluating Knowledge Engineering Tools", In: AAAI Tutorial Notebook, 1990.

[10] De Kleer, J. “An Assumption-Based TMS”, Artificial Intelligence, Vol. 28, 1986, pp. 127–162.

[11] Doukidis, G.I. “Decision Support System Concepts in Expert Systems: An Empirical Study”, Decision Support Systems, Vol. 4, 1988, pp. 345–354.

[12] EXSYS Inc. Production Descriptions of EXSYS Professional, 1990.

[13] Fikes, R. and Kehler, T. "The Role of Frame-Based Representation in Reasoning", Communications of the ACM, Vol. 28, No. 9, 1985, pp. 904–920.

[14] Friederich, Sylvia and Gargano, M. Expert Systems Design and Development using VP-Expert, Wiley, New York, 1989.

[15] Grunwald, S. “The Selection of Expert System Development Environments”, Microprocessing and Microprogramming, Vol. 25, No. 5, January 1989, pp. 21–26.

[16] Harmon, P., Maus, R. and Morrissey, W. Expert Systems: Tools and Applications, Wiley, New York, 1988.

[17] Hayes-Roth, R. “Blackboard Architecture for Control”, Artificial Intelligence, Vol. 26, 1985, pp. 251–321.

[18] Hellerstein, J.L., Klein, D.A. and Milliken, K.R. Expert System in Data Processing, Addison-Wesley, Reading, MA, 1990.

[19] Hick, R. and Lee, R. VP-Expert for Business Application, Holden-Day, San Francisco, CA, 1988.

[20] Information Builder, Inc. Product Descriptions of Level 5 Object.

[21] Laurent, J.P., Ayel, J., Thome, F. and Ziebelin, D. "Comparative Evaluation of Three Expert System Development Tools: KEE, Knowledge Craft, ART", Knowledge Engineering Review, Vol. 1, No. 4, 1986, pp. 19–29.

[22] Liebowitz, J. "Teaching an Expert System Course for the Graduate Business Program", The Journal of Computer Information Systems, Fall 1988.

[23] Liebowitz, J. "An Expert System Forecast", Journal of Information Systems Management, Spring 1990, pp. 69–72.

[24] Liebowitz, J. “Introducing Expert Systems into the Firm”, In: Liebowitz, J., ed., Expert Systems for Business and Management, Yourdon Press, Englewood Cliffs, NJ, 1990.

[25] Lu, M. and Guimaraes, T. "A Guide to Selecting Expert Systems Applications", Journal of Information Systems Management, Spring 1989, pp. 8–15.

[26] Mockler, R.J. Knowledge-based Systems for Management Decisions, Prentice-Hall, Englewood Cliffs, NJ, 1989.

[27] Moselhi, O, and Nicholas, M.J. "Expert System Building Tools: A Selection Criteria", AACE Transactions, 1988, G.9.1-G.9.4.

[28] Niwa, K., Sasaki, K. and Ihara, H. “An Experimental Comparison of Knowledge Representation Schemes”, AI Magazine, Summer 1984, pp. 29–36.

[29] Paperback Software Inc. Production Descriptions of VP-Expert, 1990.

[30] Saaty, T.L. "A Scaling Method for Priorities in Hierarchical Structures", Journal of Mathematical Psychology, 1977, Vol. 15, No. 3, pp. 234–245.

[31] Saaty, T.L. The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[32] Schumann, M. et al. "Business Strategy Advisor: An Expert Systems Implementation", Journal of Information Systems Management, Spring 1989, pp. 16–24.

[33] Seidmann, A. and Arbel, A. "Microcomputer Selection Process for Organizational Information Management", Information and Management, Vol. 7, 1984, pp. 317-329.

[34] Shoval, P and Lugasi, Y. “Models for Computer System Evaluation and Selection”, Information and Management, Vol. 12, 1987, pp. 117–129.

[35] Siegel, P. “1st Class: Expert System Builder Able to Write the Rules for Novices”, Infoworld, Vol. 9, No. 28, July 13, 1987, pp. 58–61.

[36] Siegel, P. "VP Expert: inexpensive Program Designs Expert Systems for Novices", Infoworld, Vol. 9, No. 38, September 21, 1987, pp. 67–70.

[37] Sprague, K.G. and Ruth, S.R. Developing Expert Systems using EXSYS, Mitchell Publishing, 1988.

[38] Turban, E. Decision Support and Expert Systems, Macmillan, New York, 1990.

[39] Vedder, R.G. “Teaching Artificial Intelligence in the Business School”, Interface, Winter 1986–1987, pp. 19–22.

[40] Vedder, R.G. et al. "Five PC Based Expert Systems for Business Reference: An Evaluation", Information Technology and Libraries, Vol. 8, No. 1, March 1989, pp. 42–54.

[41] Warman, D. and Modesitt, K.L. "A Student's View: Learning in an Introductory Expert System Course", Expert Systems, February 1988, pp. 30–39.

[42] Waterman, D. A Guide to Expert Systems, Addison-Wesley, Reading, MA, 1985.

[43] Wind, Yoram and Saaty, T.L. “Marketing Applications of the Analytic Hierarchy Process”, Management Science, Vol. 26, No. 7, 1980, pp. 641–658.

[44] Zahedi, F. “Database Management system Evaluation and Selection Decision”, Decision Sciences, Vol. 16, No. 1, 1985, pp. 91–116.

Appendix A. PC-based ES shells on the market

<table><tr><td>Tool</td><td>Methods</td><td>Company</td><td>Price</td></tr><tr><td>1st-CLASS</td><td>Inductive</td><td>AI Corp., Inc.</td><td>$995</td></tr><tr><td>Aion Development System (ADS) (5.1)</td><td>Hybrid</td><td>Aion Corp.</td><td>$7000</td></tr><tr><td>ART-IM</td><td>Hybrid</td><td>Inference Corp.</td><td>$8000</td></tr><tr><td>CA-DB : Expert</td><td>Formerly enterprise expert (Rule/Goal)</td><td>Computer Associates</td><td>$2000</td></tr><tr><td>Exsys Professional</td><td>Rule/frames</td><td>Exsys, Inc.</td><td>$795</td></tr><tr><td>GoldWorks II</td><td>Hybrid</td><td>Gold Hill Computers</td><td>$7500</td></tr><tr><td>GURU</td><td>Structured rule</td><td>MDBS Inc.</td><td>$6500</td></tr><tr><td>KAPPA</td><td>Hybrid</td><td>Intellicorp</td><td>$3500 per license</td></tr><tr><td>PRO KAPPA</td><td>Hybrid (unix-based)</td><td>Intellicorp</td><td>$14450</td></tr><tr><td>KBMS</td><td>Hybrid</td><td>Al Corp., Inc.</td><td>$5000</td></tr><tr><td>KES II/KES/VE</td><td>Structured rule</td><td>Software A&amp;E, Prime Comp., Unisys, Control Data</td><td>$4000</td></tr><tr><td>KnowledgeCraft</td><td>Hybrid</td><td>Carnegie Group</td><td>$10000</td></tr><tr><td>Level5</td><td>Rule-based</td><td>Information Builders Inc.</td><td>$685</td></tr><tr><td>Level5 Object</td><td>Hybrid</td><td>Information Builders Inc.</td><td>$995</td></tr><tr><td>Nexpert Object</td><td>Hybrid</td><td>Neuron Data</td><td>$5000</td></tr><tr><td>RuleMaster</td><td>Inductive</td><td>Radian Corp.</td><td>$7500</td></tr><tr><td>CLIPS</td><td>OPS</td><td>COSMIC/University of Georgia</td><td>$312</td></tr><tr><td>Crystal</td><td>Rule-based</td><td>Intelligent Environments</td><td>$995</td></tr><tr><td>EST</td><td>Rule-based</td><td>Mind Path Technologies</td><td>$495</td></tr><tr><td>Expert Edge</td><td>Rule-based</td><td>Helix Expert Systems Ltd.</td><td>$795</td></tr><tr><td>Exsys</td><td>Rule-based</td><td>Exsys Inc.</td><td>$395</td></tr><tr><td>Instant Expert/Instant Expert +</td><td>Rule-based</td><td>Human Intellect Systems</td><td>$69.95–498</td></tr><tr><td>KDS 2 &amp; 3</td><td>Inductive</td><td>KDS Corp.</td><td>$970–1495</td></tr><tr><td>KnowledgePro/Knowledge Pro Windows</td><td>Rule-based</td><td>Knowledge Garden Inc.</td><td>$495–695</td></tr><tr><td>Logic Tree</td><td>Rule-based</td><td>CAM Software, Inc.</td><td>$495</td></tr><tr><td>Personal Consultant Easy</td><td>Rule-based</td><td>Texas Instruments</td><td>$495</td></tr><tr><td>Personal Consultant Plus</td><td>Structured rule</td><td>Texas Instruments</td><td>$2950</td></tr><tr><td>PC Expert Professional</td><td>Structured rule</td><td>Software Artistry Technologies</td><td>$495</td></tr><tr><td>SuperExpert</td><td>Inductive</td><td>Softsync Inc.</td><td>$199.95</td></tr><tr><td>VP-Expert</td><td>Rule-based/inductive</td><td>paperback Software</td><td>$249</td></tr><tr><td>XI Plus</td><td>Rule-based</td><td>Expertech</td><td>$1995–17K</td></tr><tr><td>G2</td><td>Hybrid</td><td>Gensym</td><td>$17000</td></tr></table>

Appendix B. Checklist of four PC shells

<table><tr><td>Features</td><td>1st class</td><td>Level 5 object</td><td>EXsys prof.</td><td>VP-expert</td></tr><tr><td colspan="5">Session activities displaying</td></tr><tr><td>- Contents of working memory</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>- Intermediate goal</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>- rules</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">End-user supporting facilities:</td></tr><tr><td colspan="5">Explanation facilities</td></tr><tr><td>- How?</td><td>limited</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Why?</td><td>limited</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- What If?</td><td>Yes</td><td>Yes</td><td>Limited</td><td>Yes</td></tr><tr><td colspan="5">Knowledge representation</td></tr><tr><td>- Rule</td><td>Limited</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Frame</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>- Example</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td colspan="5">Inference mechanism</td></tr><tr><td>- Forward</td><td>Limited</td><td>Yes</td><td>Yes</td><td>Limited</td></tr><tr><td>- Backward</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Agenda manager (blackboard)</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>- Multiple hypothetical pursuits</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>- Demon</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td colspan="5">Confidence calculation</td></tr><tr><td>- User response</td><td>Limited</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Conclusion</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">Developer supporting facilities</td></tr><tr><td colspan="5">● Debugging aids</td></tr><tr><td>- Trace</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">● Knowledge base editor</td></tr><tr><td>- Editing</td><td>Menu driven</td><td>Text &amp; graphic</td><td>Menu driven</td><td>Text driven</td></tr><tr><td>- Rule induction</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>- Knowledge Tree</td><td>Yes</td><td>Yes</td><td>no</td><td>No</td></tr><tr><td>- Syntax checking</td><td>N/A (menu driven)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">- Consistency checking</td></tr><tr><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>- Case facilities</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td colspan="5">Interface of external program</td></tr><tr><td>- Data base</td><td>Dbase</td><td>Dbase</td><td>Dbase</td><td>Dbase</td></tr><tr><td>- ACSII file</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Spreadsheet</td><td>Lotus</td><td>Lotus</td><td>Lotus</td><td>Lotus</td></tr><tr><td>- Others</td><td></td><td>Focus</td><td>Symphony</td><td></td></tr><tr><td colspan="5">Documentation</td></tr><tr><td>- Sample Application</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- On-line tutorial</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Context Sensitive Help</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">Support/Service</td></tr><tr><td>- Hot-line</td><td>Yes (Toll Free)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">Ease of use/ease of learning:</td></tr><tr><td>- Graphical editing with mouse</td><td>No</td><td>Yes</td><td>no</td><td>No</td></tr><tr><td>- Menu-driven</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>- Hypertext</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>- Natural language</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>- Speech interface</td><td>No</td><td>No</td><td>Limited</td><td>No</td></tr><tr><td colspan="5">Platforms</td></tr><tr><td>- Hardware</td><td>IBM PC XT, AT PS/2, Compatibles.</td><td>IBM PC AT, PS/2 Compatibles</td><td>IBM PC AT, PS/2 compatibles</td><td>IBM PC XT, AT PS/2 Compatibles</td></tr><tr><td>- Required Memory</td><td>512K</td><td>640K</td><td>400K</td><td>384K</td></tr><tr><td>- Recommended memory</td><td>640K</td><td>2MB</td><td>640K</td><td>640K</td></tr><tr><td>- MS-DOS</td><td>2.0+</td><td>3.0+</td><td>2.0+</td><td>2.0+</td></tr><tr><td>- Window Software</td><td>None</td><td>MS window 2.0+</td><td>None</td><td>None</td></tr><tr><td>Price</td><td>$995</td><td>$995</td><td>$795</td><td>$249</td></tr></table>
