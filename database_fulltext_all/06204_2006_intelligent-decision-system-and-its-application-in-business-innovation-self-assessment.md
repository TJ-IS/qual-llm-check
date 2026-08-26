---
otero_id: 6204
otero_key: "PYMP4E56"
title: "Intelligent decision system and its application in business innovation self assessment"
authors: "Dong-Ling Xu; McCarthy; Jian-Bo Yang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 664 – 673

www.elsevier.com/locate/dsw

# Intelligent decision system and its application in business innovation self assessment

Dong-Ling Xu <sup>\*</sup>, Grace McCarthy, Jian-Bo Yang

Manchester Business School, The University of Manchester, P.O. Box 88, Manchester, M60 1QD, United Kingdom

Available online 25 May 2005

## Abstract

In this paper, it is described how a multiple criteria decision analysis software tool, the Intelligent Decision System (IDS), can be used to help business self-assessment. Following a brief outline of a model for assessing business innovation capability and the IDS software, the process of using IDS to implement different types of assessment questions is discussed. It is demonstrated that IDS is a flexible tool capable of handling different types of data in self-assessment, including uncertain and incomplete data, and providing a wide range of information including scores, performance diversity, strength and weakness profile and graphics.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Multiple attribute decision making; Evidential reasoning approach; Intelligent decision system; Decision support system; Self assessment; Knowledge management

## 1. Introduction

Many small and medium sized enterprises (SMEs) in the UK and Europe strive for business excellence through innovation. Entering Tailored Innovation Management in Very Small Enterprises (ENTER-TAIN) is a European Commission funded project under the Innovation and SME Programme. The main objective of the project is to help SMEs to improve their innovation strength through self-assessment, self-training and remotely assisted consultancy.

In order to achieve the first goal, an innovation capability Self-Assessment model (SA model) was developed by the project consortium, taking into account the specific needs and characteristics of SMEs. The SA model covers 7 areas of a business. Under each area, 7–14 questions are asked about the business. Some questions are divided into a few sub-questions. Therefore the self-assessment model is in a hierarchical structure (Fig. 1).

The SA model and indeed many other self-assessment models such as EFQM (European Foundation of Quality Management) model [3] are typical Multiple Criteria Decision Making (MCDM) problems [22,1]. Assessment models, however, also have the following two features. The first feature is that they are normally pre-structured. The same fixed models will be used by many different organisations to ensure that assessments are based on the same standards. The other feature is that they normally consist of tens, sometimes hundreds, of questions. The EFQM model lists 172 areas for a business to consider when using the model for self-assessment and for award applications.

![](/api/attachments/PYMP4E56/fulltext/images/d063600115b0f92bb37ce4652b9b9c194ec5299145b9ff397ca3c1439536f80e.jpg)  
Fig. 1. IDS main window and the SA model hierarchy.

The Intelligent Decision System<sup>1</sup> (IDS for short) is a general-purpose multicriteria decision analysis tool based on a new methodology called the Evidential Reasoning (ER) approach [20]. During the past few years, the authors and their colleagues have applied IDS to support business performance assessment and organisational self-assessment using different models [7–9,22,13]. The results show that the ER approach, supported by IDS, has significant advantages over conventional methods in helping to improve consistency, transparency and objectivity in the assessments.

As such, one of the tasks of the ENTERTAIN project is to implement the SA model using IDS in order to help SMEs to conduct the self-assessment more efficiently, objectively and informatively.

Like many other business performance assessment models, the SA model is also pre-structured. The questions, answers and scoring scheme in the SA model are designed mainly based on experiences, other similar models and consultation with business advisors and small business owners. Although the IDS software can also provide support in problem structuring, weight and value elicitation, and sensitivity analysis, such support is not required in this case. Therefore the main focus of this paper is on how the SA model is implemented, how the self-assessment process is supported by IDS, and the advantages of IDS over other tools.

In the following section, the SA model will be outlined and the ER approach and the IDS software briefly described. The process of implementing the SA model using IDS will be demonstrated using examples. The features, advantages and benefits of using IDS for self-assessment will be demonstrated by the self-assessment data of a few fictitious companies. Although the package was used to assess real businesses, due to confidentiality restriction we are unable to use the real data in this paper.

## 2. The SA model

Most SMEs are of limited resources for self-assessment. Therefore the SA model has to be simple, easy to understand, not too long or tedious, general enough to be suitable for most SMEs in every sector and specific enough to stimulate honest and meaningful self-assessment.

The SA model was developed based on the EFQM model [3]. It covers the following 7 areas:

<sup>!</sup> Level of Innovation,

<sup>!</sup> Innovation Strategy,

<sup>!</sup> Innovation Process,

<sup>!</sup> People and Culture,

<sup>!</sup> Financial Resources,

<sup>!</sup> Knowledge and Information and Communication Technology, and

<sup>!</sup> Business Network.

There are in total 80 multiple choice questions under the 7 areas. Each question is explained to help users to understand it. Each answer is also explained. The explanations to each answer act as guidelines to help assessors to choose the most appropriate answer or answers. The explanations will also form the basis for generating a self-assessment profile report.

All questions are multiple-choice type, such as <sup>b</sup>How would you rate the company in terms of innovation<sup>Q</sup>. The answers to this question could be Below Average, Average, Best for Its Size and World Class. The number and wording of answers vary from question to question. A special case is the Yes/No, or Yes/Partially/No type of questions.

For most questions, each answer is associated with a different score, not necessarily equally spaced between the maximum and minimum scores. There are a few questions for which some answers are associated with the same scores. The scores reflect the values of the answers to the question and the importance of the question to the assessed area, and more details can be found in Section 4.1.2. There are a few other special questions for which no matter what answers are selected in a self-assessment, they will be given no score, such as <sup>b</sup>How many new or substantially improved products or processes has the company introduced in the last 12 months?<sup>Q</sup> Because this figure can vary widely from industry to industry, the real purpose of asking this type of questions is not to find out a number, but to direct users to think more specifically in order to be able to answer the follow-on question <sup>b</sup>Has the company evaluated the benefits it has achieved from process innovation?<sup>Q</sup>

The questions and answers in the SA model have been designed to be as SMEs friendly as possible. The explanations to each question and its answers, and the heterogeneous nature of the questions in the SA model reflect such intention. The SA model is developed independent of any software restrictions. To many MCDM software packages, implementing such a model proves to be a challenge. It turns out, however, that IDS is a perfect match for such an implementation.

## 3. The evidential reasoning (ER) approach

The ER approach is developed to deal with MCDM problems having both quantitative and qualitative information with uncertainties and subjectivity. The ER approach uses concepts from several disciplines, including decision sciences (in particular value theory), artificial intelligence (in particular the theory of evidence [12], statistical analysis and computer technology [25,19,17,20,21].

While most conventional MCDM methods use a decision matrix for problem modelling, the ER approach uses a belief decision matrix, of which the conventional decision matrix is a special case. In a belief decision matrix, a distribution instead of a single value is used to represent an alternative’s performance on an attribute. For example, if a company is assessed to be Excellent on <sup>b</sup>short-term planning<sup>Q</sup> and Poor on <sup>b</sup>long-term planning<sup>Q</sup>, it would then be described as Average on Planning in a decision matrix, while in a belief decision matrix, this would be a distribution of {[Excellent 50%], [Average, 0], [Poor, 50%]}.

A modified Dempster’s evidence combination algorithm [20] is used for aggregating the information in the belief decision matrix. The aggregation process is nonlinear, and in essence a probabilistic approach [21]. The outcome of the aggregation is also a distribution, not a single score, of an alternative’s performance on the top attribute. However, a score can be calculated from the distribution by adding each assessment grade value weighted by the associated belief degree in the distribution [20,17]. However the score will normally be different from weighted sum method because the distribution is generated through a nonlinear aggregation process.

There are two general advantages in employing the ER approach for MCDM. Firstly, it provides a novel belief framework to model and synthesise subjective information. Secondly the ER approach can make full use of different types of data, including subjective judgements, probabilistic data, and incomplete data under weaker assumptions that may underlie other methods such as MAVT. For example, it requires only the satisfaction of value independence condition, which is easy to check and satisfy, in order to apply the ER approach for attribute aggregation, not the stringent preferential independence condition required by the multiple value function theory (MAVT) [2,6,4].

When there are only a few attributes, it may be manageable to check the satisfaction of the preferential independence conditions. It becomes much more difficult when attribute number increases beyond a handful. Therefore decision scientists normally recommend to carefully select only a small number of attributes, such as 9 or up to a few tens, when structuring a MCDM problem [4,1].

Unfortunately, real life MCDM problems, such as business performance assessment problems represented by many quality award models, such as the EFQM model and the Malcolm Baldrige Award criteria [10], may contain many more attributes than just a few dozens. Worse still, the preferential independence condition as defined by Keeney-Raiffa [4] can easily be violated. In those circumstances, the MAVT are not applicable but the ER approach can still be applicable, which only requires the milder value (or utility) independence conditions [4].

In self-assessment, the above general advantages of the ER approach can be transformed into the following three practical advantages. Firstly the belief decision matrix provides flexibilities in question presentation and data collection. Secondly, the ER aggregation process generates more insight information on performance diversities and supports the identification of strengths and weaknesses. Thirdly, the number of attribute (or questions) in the assessment model is much less a concern to the ER approach than to other conventional approaches.

The support of the IDS software provides extra benefits. IDS provides not only user friendly interfaces for applying the ER approach, but also knowledge management, report generation, and data presentation facilities.

These advantages and benefits will be demonstrated and explained in the next section.

## 4. Application of IDS in innovation self-assessment

As mentioned earlier, self-assessment problems are typical multiple criteria decision making (MCDM) problems. In MCDM terms, the companies to be assessed will be referred to as alternatives or options. Assessed areas and assessment questions under each of the areas are referred to as attributes or criteria. Consequently, the terms such as questions, attributes and criteria are used interchangeably in this paper. Also the terms like answers and grades are also used interchangeably because normally each answer is associated with a score, just as a grade does when it is used to assess an attribute.

There are 3 major steps in applying IDS for selfassessment: model implementation, assessment information input, and assessment result report. The first step is a task for questionnaire designers or business advisors. Assessors in SMEs do not need to repeat the implementation process described later. Their tasks are to collect information and answer all the questions as objectively as possible.

The steps will be discussed in the following 3 subsections.

## 4.1. Model implementation

Implementing the SA model with IDS involves a few steps: implementing a question hierarchy, defining the questions and their multiple-choice answers, including value functions for the answers, and assigning question weights. Using IDS, the construction of the attribute (question) hierarchy is straightforward. The IDS main window is shown in Fig. 1, where there are a tree view window for displaying a hierarchy of assessed areas and questions, and a list view window to display the names of the businesses to be assessed.

## 4.1.1. Define questions and answers

After the hierarchy is structured, each question needs to be further defined. The definition includes a description about the question, the number, wording and values of the answers (grades) to the question (Fig. 2), and answer explanations or guidelines. When a score associated to an answer is already decided, which is the case in the SA model, the value of the answer is then determined by dividing the score with the weight of the question (weights are discussed in Assign Question Weights section). In general, the value should be a number between 0 (most unfavourable) and 1 (most favourable) to represent the preferences of questionnaire designers.

When IDS detects that different numbers of answers (or grades) are used between a question and its associated area in an upper level of the hierarchy, it will prompt the questionnaire designers to convert the values of the answers to the values of the grades used in the higher-level area. The conversion can be conducted either using rules or value equivalence [17]. If the users prefer, IDS will conduct the conversion automatically based on value equivalence.

Because of the use of the value equivalence transformation, the questionnaire designers are free to use any wording and number of answers which are most appropriate to a question. They are also free to ask any types of questions, whether numerical or subjective. In fact, the questions and answers in the SA model are developed initially on paper, completely free of software consideration.

The explanations to questions and answers entered in this stage can be retrieved later and is helpful when assessors need to clarify the definition of a question and the meaning of an answer. Consequently it helps to increase the consistency and reduce subjectivity in scoring, even for relatively inexperienced assessors.

![](/api/attachments/PYMP4E56/fulltext/images/1249256c6c26dd143d6fc591c179eaa9ecd138394a508b7487912f901830f16f.jpg)  
Fig. 2. Attribute definition window.

Together with evidence and comments recorded during the Input Assessment Information process discussed later, the information forms a knowledge-base and will be used to generate an automated and tailored self-assessment report.

## 4.1.2. Assign question weights

For any assessment, different questions may be of different importance. In the SA model, the maximum score obtained by answering a question reflects the importance of the question. Therefore, the weight assigned to a question is its maximum score, that is, the score given to the most favourable answer. For those questions whose answers are associated with zero score, the weight is zero.

Once the weights for all the questions at the bottom level of the attribute hierarch are assigned, the weight of a higher level area is then the sum of the weights assigned to its immediate child attributes, or the associated questions.

If weights are not known and need to be determined, IDS provides a few methods and interfaces to help decision makers to assign weights, such as weight swing [1], direct assignment (Fig. 3), and pairwise comparisons [11]. It also provides sensitivity analysis interfaces for fine-tuning weights.

In the SA model, the scores assigned to each answer of each question are calibrated and validated through the tests of a few SMEs in the northwest of England. Adjustments to the initial weights have been made based on the tests so that the generated scores and company profiles fits the current situations of the companies, to the best belief of the company owners. Therefore the weights are determined beforehand. In such case, the visual scoring interface as shown in Fig. 3 can be used. A weight can be assigned to each attribute by either dragging a corresponding bar or typing a precise figure in the weight edit box.

## 4.2. Self-assessment

Self-assessment involves collecting evidence, comparing evidence with standards, and making judgements. Using the IDS implemented SA model for selfassessment, not only the process is technically supported, but cognitively supported as well, as discussed below.

![](/api/attachments/PYMP4E56/fulltext/images/db88dc57dae0a5c2e2d31d88f6b676a8244de58c1b700f0085fa90f380a4371f.jpg)  
Fig. 3. Window for assigning weights to attributes.

4.2.1. Answer questions and assign belief degrees When conducting a self-assessment, IDS allows several answers to be selected and each is associated with a belief degree. Technically, this means simply ticking the appropriate answers and typing a belief degree beside each answer in the data input window (Fig. 4). A belief degree represents the strength to which an answer is believed to be true. The total belief degree can be equal to or less than 100%. This feature is originated from the use of the belief decision matrix to model MCDM problems in the ER approach.

Such a feature brings unique flexibility in handling judgmental uncertainty and complexity. For example, if an assessor believes that a company’s performance falls somewhere between two predefined grades, he has the freedom to assign different belief degrees to the two grades. If there are a few people to answer the same question, the belief degree structure allows different views to be accommodated. If a question covers several sub-areas or if some sub-areas are better represented by one answer but other areas by another answer, then the belief structure will also allow the sub-area differences to be reflected. Indeed, the belief information is preserved when the ER approach aggregates the entered data from lower level questions to higher level areas in the hierarchy (Fig. 1). The belief information at the top level reveals the overall performance distribution and facilitates strength and weakness analysis.

In addition to the flexibility, the belief structure and the ER aggregation process can make maximum use of different types of raw information logically, including probabilistic data, incomplete and missing data [16]. For example, if there is not sufficient evidence, an assessor may leave the question completely unanswered or assign less than 100% belief degrees. For missing data, IDS by default assigns 0% belief degree to each answer and the ER approach assumes that incomplete or missing answers are in an interval covering the whole category range.

## 4.2.2. Support to improve consistency

Although IDS can use data with uncertainty, it does not mean that IDS would encourage assessors to be vague or subjective or leave questions unanswered.

![](/api/attachments/PYMP4E56/fulltext/images/4188a378c21f3913387b7a4cdf0c56177c04c999bd1a9aad60a7c9772eb359c9.jpg)  
Fig. 4. An interface for inputting assessment information.

On the contrary, the belief structure requires more detailed information and hence encourages more specific and objective thinking.

To reduce subjectivity and inconsistency, the data input window (Fig. 4) provides access to question and answer explanations as well. If the cursor is placed on an answer, the explanation to the answer, entered earlier in the model building process, will be displayed in the Grade Definition box. The explanations act as guidelines to help assessors to tick the right answers and assign appropriate belief degrees. If needed, pressing the Attribute Definition button will popup the display of the question explanation, also entered earlier.

## 4.2.3. Evidence mapping

Optionally, evidence and comments can be recorded using the Provide Evidence button in the same data input window (Fig. 4). The Provide Comments button displays the evidence mapping interface, which displays evidence and the guidelines for answers side by side so that belief degrees can be assigned based on the match of evidence with the category standards. Blank spaces are provided in the same interface for assessors to enter comments on why some answers are selected and the belief degrees given.

If it is a new assessment based on a previous one, then the comments and evidences recorded earlier will be available through the Provide Evidence and Provide

Comments buttons. The evidence recorded in the past assessments can be used as references to maintain relative consistency. It also improves efficiency, because only the changed parts need to be adjusted.

## 4.3. View assessment results

The IDS software can generate different types of assessment results in graphical format such as performance ranking, performance score range when an assessment is not complete [15], and performance distribution (Fig. 5). Those graphs enable the comparisons among selected alternatives to be carried out on any selected areas in different levels of the assessment hierarchy.

Distributed performance graphs provide more insight information than scores and simple ranking graphs. Fig. 5 shows the distributed overall performance of two companies. It reveals the performance composition in different categories (grades). Although both companies have similar overall scores, the X Limited has more Best and less Worst performed areas than the other company. The distribution also indicates that in X Limited 11% of the areas are assessed to the lowest grade, which alerts managers to focus on those areas for improvement. A search function is also provided in IDS to search for those areas.

Text reports are also provided. The questionnaire, question and answer explanations, assessment data entered by assessors and aggregated results on every attribute can be saved in a text file. A tailored company profile report can also be generated highlighting key areas to consider for improvement. A text report provides an accurate account of the assessment and can be used as a basis for generating documents such as quality award applications and action plans.

![](/api/attachments/PYMP4E56/fulltext/images/9c3632d181054744dba11131b923502022ca7909da033f22663f0957373e8b5a.jpg)  
Fig. 5. Distributed performances of two companies.

## 5. Self-assessment trial

After the SA model is implemented in IDS, a trial is organised to test the tool. The 4 principal contractors of the consortium are responsible for organising the trial in their own respective countries. Ten SMEs, who are the assistant contractors of the project, participated in the test with more than 30 people involved, including managing directors, marketing directors or technical directors from these SMEs. The ten SMEs were not involved in the development of the model before the test. To measure the effectiveness of the tool, feedbacks are collected by asking participants to rate in a 5-point scale in seven areas. The seven areas and the average scores given by the consortium are shown in Fig. 6.

The main messages from the feedback are that the questions and software interfaces are easy to understand and the tool can help users to understand potential areas for innovation. While the average ratings are positive and encouraging, improvements are also requested by the participants in their feedback. For example, business users are not familiar with the jargons used in the MCDM field and words such as <sup>b</sup>Alternatives<sup>Q</sup> and <sup>b</sup>Attributes<sup>Q</sup> should be replaced with <sup>b</sup>Company Names<sup>Q</sup> and <sup>b</sup>Questions<sup>Q</sup> respectively in some of the IDS interfaces.

![](/api/attachments/PYMP4E56/fulltext/images/cc74f4b0eef7ea4cefa8f875c188d0f0dc66b3a93fe70a95dccdbec49b48ff22.jpg)  
Fig. 6. Consortium average ratings of the SA-IDS tool by question.

The usefulness of graphics is not highly rated, but when asked whether the graphics functions should be excluded from the package, the answer is no. As graphics are good for comparisons and showing differences, they will become more useful in the subsequent rounds of assessment, but may be less useful at the initial trial when there is nothing to compare with.

There are significant discrepancies on the ratings between countries. UK rated the tool the highest with 4.4, Spain with 3.4 and Norway with 3.3. Because the SA model is developed in the UK, the model is probably more compatible with the UK business culture.

Some companies asked different people to test the tool independently during the trial. The outcomes are reported to be <sup>b</sup>amazingly consistent<sup>Q</sup>.

## 6. Concluding remarks

In this paper, it is described how the multi-criteria decision software IDS can support business to conduct innovation self-assessment. It is demonstrated that the process is not only technically supported to improve efficiency but also cognitively supported to improve objectivity and consistency.

As the ER approach does not require the value preference independence condition like other value function approaches do, it makes the ER the most suitable approach for supporting different types of assessments, which are normally of large scale and do not satisfy the condition. It is indeed used for supplier assessment and engineering product design assessment. This is evidenced by a series of published results on the applied research of using the ER approach for supplier assessment, risk assessment and engineering design assessment [14,5,18]. Theoretical research on the ER approach is still ongoing. The belief decision matrix concept has also instigated the belief rule concept, which has shown promising potential in self-learning and training of expert systems [23,24].

## Acknowledgements

This work is supported by the UK Engineering and Physical Science Research Council (EPSRC) under the grant number GR/N65615/01 and the European Commission (EC) under the grant number IPS-2000- 00030. The business advisors and the directors and managers of the participating companies have contributed to the work by participating in the SA model development and testing the IDS implemented package. The authors would also like to thank two anonymous referees for their constructive comments, which helped to re-shape the paper.

## References

[1] V. Belton, T.J. Stewart, Multiple Criteria Decision Analysis—An Integrated Approach, Kluwer Academic Publishers, 2002.

[2] B.G. Buchanan, E.H. Shortliffe, Rule-Based Expert Systems, Addison-Wesley, Reading, MA, 1984.

[3] EFQM, The EFQM Excellence Model, European Foundation for Quality Management, Brussels, ISBN: 90-5236-082-0, 1999.

[4] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, Cambridge University Press, 1976.

[5] J. Liu, J.B. Yang, J. Wang, S.K. Sii, Review of uncertainty reasoning approaches as guidance for maritime and offshore safety-based assessment, Journal of UK Safety and Reliability Society 23 (2002) 63– 80.

[6] R. Lopez de Mantaras, Approximate Reasoning Models, Ellis Horwood Limited, Chichester, England, 1990.

[7] G. McCarthy, R. Greatbanks, J.B. Yang, Guidelines for assessing organisational performance against the EFQM model of excellence using the radar logic Working Paper Series, Paper No.: 0203, ISBN:1 86115 111 X, 2002, http://www.sm.umist. ac.uk/wp/abstract/wp0203.htm (accessed July 2004).

[8] G. McCarthy, R. Greatbanks, J.B. Yang, Simulating self-assessment improvements using evidential reasoning software. International Journal of Quality and Reliability Management (submitted for publication).

[9] G. McCarthy, R. Greatbanks, J.B. Yang, Validation of selfassessment guidelines, Quality Management Journal (accepted for publication) subject to revision.

[10] L. Porter, J. Tanner, Assessing Business Excellence, Butterworth-Heinmann, London, 1998.

[11] T.L. Saaty, The Analytic Hierarchy Process, University of Pittsburgh, 1988.

[12] G.A. Shafer, Mathematical Theory of Evidence, Princeton University Press, 1976.

[13] C.H.R. Siow, J.B. Yang, B.G. Dale, A new modelling framework for organisational self-assessment: development and application, Quality Management Journal 8 (2001) 34 – 47.

[14] M. Sonmez, J.B. Yang, G. Graham, G.D. Holt, An evidential reasoning based decision making process for pre-qualifying construction contractors, Journal of Decision Systems, Special issue on Decision Making on Urban and Civil Engineering 11 (2002) 355–381.

[15] D.L. Xu, J.B. Yang, Intelligent decision system for self-assessment, Journal of Multi-criteria Decision Analysis 12 (2003) 43–60.

[16] D.L. Xu, J.B. Yang, Making decisions under uncertainties using the evidential reasoning approach, Proceedings of the 15th Mini-EURO Conference on Managing Uncertainty in Decision Support Models, Portugal, 2004 (Sept.).

[17] J.B. Yang, Rule and utility based evidential reasoning approach for multiple attribute decision analysis under uncertainty, European Journal of Operational Research 131 (2001) 31 – 61.

[18] J.B. Yang, P. Sen, Multiple attribute design evaluation of large engineering products using the evidential reasoning approach, Journal of Engineering Design 8 (1997) 211 – 230.

[19] J.B. Yang, M.G. Singh, An evidential reasoning approach for multiple attribute decision making with uncertainty, IEEE Transactions on Systems, Man, and Cybernetics 24 (1994) 1 –18.

[20] J.B. Yang, D.L. Xu, On the evidential reasoning algorithm for multiple attribute decision analysis under uncertainty, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 32 (2002) 289 – 304.

[21] J.B. Yang, D.L. Xu, Nonlinear information aggregation via evidential reasoning in multiple attribute decision analysis under uncertainty, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 32 (2002) 373–393.

[22] J.B. Yang, B.G. Dale, C.H.R. Siow, Self-assessment of excellence: an application of the evidential reasoning approach, International Journal of Production Research 39 (2001) 3789– 3812.

[23] J.B. Yang, J. Liu, J. Wang, H.S. Sii, The evidential reasoning approach for inference in rule-based systems, The 2003 IEEE Conference on Systems, Man and Cybernetics, Hyatt Regency, Washington, DC, USA, 2003 (October), pp. 5 – 8.

[24] J.B. Yang, J. Liu, J. Wang and H. S. Sii, A belief rule-base inference methodology using the evidential reasoning approach-RIMER, IEEE Transactions on Systems, Man and Cybernetics. Part A (in press).

[25] Z.J. Zhang, J.B. Yang, D.L. Xu, A hierarchical analysis model for multiobjective decision making, Analysis, Design and Evaluation of Man-Machine System 1989 (Selected Papers from the 4th IFAC/IFIP/IFORS/IEA Conference, Xian, P.R. China, September 1989), Pergamon, Oxford, UK, 1990, pp. 13–18.

Dong-Ling Xu received her PhD degree in system control engineering from Shanghai Jiao Tong University and MBA from Manchester Business School in 1988 and 2004, respectively. Dr. Xu is currently Research Fellow in decision and system sciences at the Manchester Business School, UK. She was a senior engineer in an IT company specialized in fault diagnosis from 1995 to early 2001, a Postdoctoral Research Associate at the University of Newcastleupon-Tyne from 1993 to 1995, and a Lecturer and then an Associate Professor of East China University in Shanghai from 1988 to 1993. As a co-designer, she developed several web-based and Windows based software packages icluding IDS. She has published a book and over 60 papers in computerised traffic management and control, optimisation, decision analysis, control system design, statistical process control and statistical analysis. Her current research interests are in the areas of multiple attribute decision analysis under uncertainties, decision theory, utility theory, evidential reasoning approach, belief rule-based expert systems and their applications in different areas, including decision modelling, quality management, impact assessment, engineering design, and fault diagnosis.

At the time of submitting this paper, Grace McCarthy was a researcher at Manchester Business School, working on both European and UK-funded projects. Her research interests include leadership, multinational teams, business excellence and innovation. Grace spent several years in industry in a variety of roles, including librarian, business excellence, internal communications, and European Director of Customer Service for a major telecommunications equipment supplier. She thus combines real-world experience with academic rigour in exploring significant themes in management today. Grace has now moved to Australia and is enjoying the challenge of life in a new country.

Jian-Bo Yang received his BEng and MEng degrees in control engineering at North Western Polytechnic University, Xi’an, China in 1981 and 1984 and PhD degree in Systems Engineering at Shanghai Jiao Tong University, Shanghai, China, in 1987. Professor Yang is Chair of Decision and System Sciences at the Manchester Business School, the University of Manchester, UK. He is also Visiting Professor of Huazhong University of Science and Technology of China. Prior to his current appointment, he was a faculty member of the University of Birmingham (1995–1997), the University of Newcastle-upon-Tyne (1991–1995), UMIST (1990) and Shanghai Jiao Tong University (1987–1989). In the past two decades, he has been conducting research in multiple criteria decision analysis under uncertainty, multiple objective optimisation, intelligent decision support systems, hybrid quantitative and qualitative decision modelling using techniques from operational research, artificial intelligence and systems engineering, and dynamic system modelling, simulation and control for engineering and management systems. His current applied research is in design decision-making, risk and safety analysis, production planning and scheduling, quality modelling and evaluation, supply chain modelling and supplier assessment, and the integrated evaluation of products, systems, projects, policies, etc. Professor Yang’s current research has been supported by EPSRC, EC, SERC and HKRGC. He has published widely and developed several software packages in these areas including the Windows-based Intelligent Decision System (IDS) via evidential reasoning.
