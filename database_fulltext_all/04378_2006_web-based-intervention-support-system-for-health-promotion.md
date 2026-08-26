---
otero_id: 4378
otero_key: "QT9FW9X4"
title: "Web-based intervention support system for health promotion"
authors: "Huigang Liang; Yajiong Xue; Bruce A. Berger"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Web-based intervention support system for health promotion

Huigang Liang <sup>a,T</sup>, Yajiong Xue <sup>b</sup>, Bruce A. Berger <sup>c</sup>

<sup>a</sup> Department of Information Technology and Operations Management, Florida Atlantic University, Ft. Lauderdale, FL, USA <sup>b</sup> College of Business Administration, University of Rhode Island, Kingston, RI, USA <sup>c</sup> Department of Pharmacy Care Systems, Auburn University, Auburn, AL, USA

Available online 17 March 2005

## Abstract

The Web has attracted considerable attention as an avenue to improve healthcare delivery. This paper describes the development of a Web-based intervention support system (WISS) that helps provide tailored interventions to enhance healthrelated behavior change. The tailoring strategy is based on the transtheoretical model (TTM). The performance of WISS was assessed by a pilot study, a controlled randomized longitudinal experiment involving 366 multiple sclerosis (MS) patients. Results suggest that WISS can reduce MS patients’ medication discontinuation rate and move more patients to a stage where dropout is least likely to occur.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Web-based decision support systems; Transtheoretical model; Tailored intervention; Health behavior change

## 1. Introduction

Web-based decision support systems (WDSS) refer to computerized systems that deliver decision support information or decision support tools to business end users using regular Web browsers [51,60] The ubiquity of the Web greatly extends the reach of WDSS capability so that decision-relevant information can be readily available to managers and staff users in geographically distributed locations [11,21,33,34,36,65] at a relatively low cost [64].

WDSS entails benefits in three dimensions: userfriendly dialog, seamless data access, and effortless sharing of business decision models [64]. Users can focus on system use and be freed from software installation, updates, and management by using WDSS [10,12]. Moreover, the Web makes it possible for firms to rent WDSS capability on a per-use basis from Application Service Providers [60]. WDSS have become the center of DSS vendors’ development activity [60] with the explosive use of the Web in business and personal activities.

Particularly, WDSS has received considerable attention in the healthcare arena, since the Web has increasingly become an innovative and important avenue for transforming healthcare [61]. The Web holds the promise of disseminating healthcare information, enhancing communication, and facilitating a wide range of interactions between patients and other stakeholders in the healthcare system [3]. A variety of WDSS have been applied in the healthcare practice including electronic patient records [35], telemedicine [28,57], the smart card application [14], computerized physician order entry systems [6], physician profiling systems [38], and community healthcare data warehouses [9]. By leveraging the power of the Web, these applications can integrate clinical and administrative information and share knowledge among healthcare stakeholders. Knowledge sharing is desirable in healthcare practice. The key to success is to embed specialized knowledge into IT that knowledge workers use to do their jobs [17]. WDSS is a promising tool to make knowledge sharing available in healthcare practice.

This paper describes the development and preliminary evaluation of a Web-based intervention support system (WISS) that shares knowledge about providing tailored interventions to individual patients. The WISS is designed to help patients with chronic diseases make decisions about their medication persistency. The objective is to motivate patients to continue taking their medications. The transtheoretical model (TTM), a dominant model in the health promotion field is used as the theoretical foundation of the WISS. The TTM constructs were validated by in-depth telephone interviews and surveys before they were used for system development. Based on the items of the TTM constructs and motivational interviewing techniques, the intervention structure and content were created by TTM experts and transferred into the WISS. A controlled randomized experiment was conducted to test the effectiveness of the WISS in terms of its impact on the patients’ medication discontinuation rate and their intention towards medication persistency.

The WISS we developed is a type of WDSS which has substantial significance for healthcare delivery. Healthcare organizations and pharmaceutical companies consider WDSS a strategic initiative in fulfilling consumers’ increasing requests of health-related information [54]. The Web cannot only disperse general health information and specialized information regarding specific diseases and treatments, but, more importantly, support delivery of health services such as behavioral interventions to facilitate healthrelated behavior change. Health-related behavior change has an important role in the American healthcare system. With the aging of American populations, especially the postwar <sup>b</sup>baby boomers,<sup>Q</sup> the American healthcare system has become flooded with patients suffering from chronic diseases [24]. The IOM report [16], <sup>b</sup>Crossing the quality chasm: a new healthcare system for the 21st century,<sup>Q</sup> states that the American healthcare system is outdated and characterized by worsening chronic medical conditions and skyrocketing healthcare expenditures. In order to reduce the incidence of chronic diseases and contain health expenditures, the focus of healthcare needs to be transferred to disease prevention and health promotion. Health promotion heavily relies on behavior change, which means that people should adapt to behaviors or a lifestyle that help them maintain an optimal health status. Behavior interventions delivered via the Web have been demonstrated to be useful in facilitating a variety of health-related behavior changes [22,49,66] and can potentially make significant contributions to the American healthcare system.

The paper proceeds as follows: First the research background is described. This is followed by a review of the system development of the WISS. The remaining sections present the hypotheses, experimental design, and results of the preliminary system evaluation. The paper ends with a discussion of the results and concluding comments.

## 2. Research background

This study was funded by a major biopharmaceutical company, Biogen, and the WISS we developed focuses on multiple sclerosis (MS) patients’ medication persistency with Avonex, a weekly intramuscular injection. MS is an incurable central nervous system disease [45]. Given the chronic nature of MS, which requires lifelong therapy, certain medications must be taken continuously over the long-term to manage the disease. Some patients, however, tend to discontinue their medications prematurely, causing unpredictable clinical outcomes. The factors influencing MS patients’ discontinuation behavior may include side effects, depression, unrealistic expectations, and selfefficacy [48,43,42,46,47,44], and each patient may be influenced by a different combination of these factors.

The objective of the WISS is to provide tailored interventions to MS patients to motivate them to continue taking their prescribed medications.

Avonex and MS were selected to illustrate the research paradigm of integrating a behavioral model and Web technologies for health promotion. We attempt to explain how the TTM can be integrated into the WISS to support health promotion in a general sense. Therefore, the scope of this study is not restricted to specific diseases or medications.

## 2.1. Tailored Intervention

Tailoring information is an important persuasive strategy [23] used to help people achieve healthrelated behavior change such as smoking cessation, chronic disease management, self-care, and exercising [37]. Patients pay more attention to and value tailored health information more highly than general health information on the Internet [7,37]. General consumers who are not presently sick also demonstrate a desire to obtain relevant health information. The Harris Poll of healthcare consumers in the U.S. revealed that 81% of consumers want to receive personalized health information online [26].

Providing health information is an important part of behavioral intervention. Behavioral interventions can be standard or tailored. Standard interventions provide the same general information regardless of the recipient, while tailored interventions provide information customized to personal characteristics of each individual recipient [1,55,66]. Prior research has yielded evidence that tailored interventions affect health care more positively than generic standard interventions [56,58]. Tailored interventions consist of four components [18,39,58]: (1) an assessment of key characteristics of each recipient based on theory, (2) intervention content consisting of questions and messages stored in small segments, (3) a decision algorithm providing logic that matches appropriate intervention content to the recipient’s characteristics, and (4) a delivery channel through which interventions are provided.

## 2.2. The Transtheoretical Model

After researching and comparing a variety of behavioral theories and models, the Transtheoretical

Model (TTM) was chosen as the theoretical foundation for this study. Compared with other behavioral theories, the TTM is more intervention-oriented and can therefore be used effectively to underpin an intervention program. A previous study found that the Health Belief Model, the Theory of Reasoned Action, and the Social Cognitive Theory had not been successful in predicting adherence to various medication regimens, whereas the constructs of the TTM were significant predictors of non-adherence, accounting for more than 40% of the variance of non-adherence [30].

A prominent theory in health promotion research and practice [13], the TTM emerged in the late 1970s [53] and has become one of the most dominant models used to explain and predict health behavior change. The TTM posits that people progress through five discrete stages of behavior change: precontemplation, contemplation, preparation, action, and maintenance. These stages describe how people move from being unaware, unwilling, or too discouraged to change, to considering the possibility of change, then to becoming committed and prepared to make the change, and finally taking action and sustaining the change in the long run. The TTM [72] has been successfully applied in a wide range of health-related behaviors including: reduction of dietary fat consumption, smoking cessation, participation in mammography screening, adoption of exercise, sun protection, condom use, and diabetes self-manage ment. Since medication persistency can be regarded as a long-term behavioral change, applying the TTM in this study is justified. The TTM holds promise for developing effective interventions to enhance persistency or prevent drug discontinuation.

In addition to the stages of change, decisional balance and self-efficacy are two other central constructs of the TTM. Decisional balance represents both the cognitive and motivational aspects of human decision making [29,70]. It involves individuals weighing of the pros and cons of engaging in the goal behavior. Self-efficacy constitutes <sup>b</sup>the level of confidence that individuals have that they can cope with different situations without resorting to their problem behavior<sup>Q</sup> [5,4,52]. For medication users, self-efficacy is the confidence that they can continue taking their medications in the midst of difficult situations. Interventions can be developed to modify decisional balance and self-efficacy which will then affect the movement between stages of change.

As an illustration of the intervention, consider a female patient who fears performing self-injection and doubts the effectiveness of her medication. That is to say, the patient has low self-efficacy and perceives high cons of continuing her medication. These characteristics are forerunners of medication discontinuation. Her intervention will focus on educating her about self-injection and the working mechanism of her medication. As a result, her self-efficacy might increase and her cons decrease, which might help her move to a stage where she is less likely to discontinue her medication.

## 2.3. Delivery channel

Based on the TTM, intervention content and algorithms can be developed. Once the knowledge is in place, the next question is: how can we deliver this knowledge to the end users? We propose that two channels can be utilized. One is direct Web access which relies on direct interaction between patients and the WISS via Web browsers. The other is a <sup>b</sup>chauffeured<sup>Q</sup> approach which introduces an intermediary player who conveys the intervention from the WISS to the patients. Both channels are depicted as follows.

Direct Web access entails patients’ direct interaction with a Web application. The idea is similar to Web-based customer decision support systems [50] that augment customer loyalty and retention. The WISS acts as a hypothetical healthcare provider that communicates with the patient. The patient reads intervention information from a Web browser and enters his or her responses into the system via a graphical user interface.

The second channel of intervention delivery is a <sup>b</sup>chauffeured<sup>Q</sup> approach. Inspired by the idea of <sup>b</sup>chauffeured<sup>Q</sup> use of commercial databases [15], we propose that patients can access the WISS through a third party. Rather than ask patients to use the WISS directly, a call center is employed to mediate the WISS and patients. Call center representatives obtain instructions from the WISS and deliver the information to the patient by phone. During this transaction, the representative also enters the patient’s responses into the WISS.

The first channel is less expensive than the second since it does not require human resources from the provider side. For health promotion programs targeted at the general public, direct Web access is suitable. However, patients might not enjoy <sup>b</sup>talking<sup>Q</sup> to a computer program. The 2000 Harris poll [26] indicated that patients wanted a combination of <sup>b</sup>high tech<sup>Q</sup> and <sup>b</sup>high touch.<sup>Q</sup> They liked healthcare information online, but they also preferred more personal attention from healthcare providers.[73]. One of the major concerns was that online communication was perceived as a dehumanized way to deliver healthcare. Patients prefer interaction with humans, and direct Web access fails to provide this interaction. In order to give patients <sup>b</sup>high touch,<sup>Q</sup> some researchers have integrated a digitized voice into automated telephone systems to talk with patients about disease management and monitoring [25]. However, this does not solve the fundamental problem, and some patients still complain that the voice is impersonal.

Two benefits result from the <sup>b</sup>chauffeured<sup>Q</sup> approach. First, there is no concern about dehumanization. The system is invisible to patients who actually interact with call center representatives. Second, the <sup>b</sup>chauffeured<sup>Q</sup> approach is proactive rather than reactive. A DSS on the Web is reactive, meaning it only responds after a patient initiates an interaction. A reactive approach depends on the patient’s voluntariness to continue using the DSS and cannot force the patient to do so. In contrast, the <sup>b</sup>chauffeured<sup>Q</sup> approach requires call center representatives to call the patient proactively, reducing the likelihood that intervention will be missed. In addition, many chronic diseases affect patients’ physical activity. It is very difficult for a patient suffering from hand tremors to manipulate a mouse and keyboard. The <sup>b</sup>chauffeured<sup>Q</sup> approach can exempt them from that difficulty.

In this study, the WISS was designed with both accessibilities. In the pilot evaluation of the WISS, we implemented the interventions using the <sup>b</sup>chauffeured<sup>Q</sup> approach. Eventually, we plan to deploy the WISS on the Web and allow patients to interact with the WISS directly.

## 3. System development

## 3.1. Phase I study

Before system development, it is essential to develop measurement instruments for the TTM constructs and to examine the relationships among the constructs in the setting of this study. Hence, the Phase I study was carried out [8]. The objectives of the Phase I study were to develop instruments of accurately assessing motivational aspects of patient persistency to their Avonex regimen and identify patients most at risk for discontinuing a treatment program by utilizing established TTM constructs. The findings from the Phase I study are briefly described.

In order to identify variables that might be related to Avonex discontinuation, in-depth telephone interviews were conducted with 57 MS patients (36 current Avonex users, 16 previous users, and 5 na<sup>R</sup>ve users who never took Avonex) who were randomly selected from Biogen’s patient database. Based on the telephone interviews and a literature review, a questionnaire was designed, pre-tested, revised, and administered to 946 current and previous Avonex users. A total of 530 completed questionnaires were returned. Data analysis indicated that MS patients can be categorized into five stages in terms of their readiness to discontinue Avonex:

<sup>!</sup> Stage 1: I am not considering discontinuing my Avonex.

<sup>!</sup> Stage 2: From time to time, I have thought about discontinuing my Avonex, but plan to continue using it.

<sup>!</sup> Stage 3: I am considering discontinuing my Avonex sometime in the next 6 months.

<sup>!</sup> Stage 4: I quit using Avonex less than 6 months ago.

<sup>!</sup> Stage 5: I quit using Avonex more than 6 months ago.

Measurement scales for decisional balance (the pros and cons of using Avonex) and self-efficacy of using Avonex were determined by exploratory factor analyses using principle component methods. The final pros scale, cons scale, and self-efficacy scale have ten items, six items, and ten items, respectively. All of the scales showed acceptable reliability with Cronbach Alpha coefficients above .70. Consistent with what the TTM predicts, Phase I results indicated that the pros scores decreased systematically across the five stages while the cons scores increased across the five stages. The pros outweighed the cons in Stage 1, and the cons outweighed the pros in other stages.

The results also showed that the self-efficacy was correlated with the first three stages. These findings provide empirical evidence to support the applicability of the TTM in studying MS patients’ medication discontinuation behavior. A logistic regression analysis indicated that the ratio of pros and cons can significantly predict Avonex discontinuation, while self-efficacy cannot. Consequently, the intervention is primarily based on the 16 pros and cons items. In addition, the results show that patients’ perception of the importance of medication persistency decreased systematically across the first three stages. Along with stages of readiness to discontinue Avonex, patients perception of the importance of using the medication was utilized to estimate patients’ susceptibility to its discontinuation.

## 3.2. Development process

Seven steps were taken in the software development process (see Fig. 1). The single-headed arrows in Fig. 1 represent sequential relationships. The doubleheaded arrows between Design, Coding, and Testing reflect reciprocal relationships, indicating that several iterations of design, coding, and testing might be needed before completion of the system development. These seven steps are described separately in the following sections.

## 3.2.1. Software objectives

The WISS was designed to employ the principles of the TTM and motivational interviewing in order to direct call center representatives to communicate with MS patients by telephone so that the patients’ persistency to Avonex could be maintained or increased. The variables and principles of the TTM are complicated and potentially difficult for call center representatives to understand. The WISS was expected to give detailed messages to direct call center representatives on how to talk with patients based on the principles of the TTM and the motivational interviewing. Therefore, the objectives of software development were: (1) integrate the knowledge in the TTM and motivational interviewing into the software, (2) create motivational messages based on the obtained knowledge, (3) develop procedural structures for patient interventions, and (4) deliver the structure and the messages to call center representatives so they could provide intervention messages to the patients in a theoretically structured manner.

![](/api/attachments/QT9FW9X4/fulltext/images/6495cdf7fcf657e0940e01a9ddf372a3cefebf7c4edc2d65373d19af3010ba4f.jpg)  
Fig. 1. Software development process.

## 3.2.2. Software requirements

The requirements of the WISS were determined by the objectives of the software and the needs of the project. Some primary requirements are:

<sup>!</sup> The WISS should be a Web-based system.

<sup>!</sup> The WISS should be able to dynamically generate intervention structures and contents for each individual patient based on the patient’s Stage of Change, perceived importance of Avonex continuation, and decisional balance.

<sup>!</sup> The WISS should have adequate security.

<sup>!</sup> The WISS should be able to schedule intervention calls for the call center representatives.

<sup>!</sup> The WISS should have session control to ensure data integrity for each patient.

<sup>!</sup> The WISS should have a database to save intervention contents and patient data.

## 3.2.3. Knowledge acquisition

In this study, knowledge means the ability to use the TTM and motivational interviewing principles and turn them into the practice of enhancing patients’ persistency to their treatments. Knowledge acquisition is <sup>b</sup>the extraction and formulation of knowledge derived from various sources, especially from experts.<sup>Q</sup> [69] Since the WISS was intended to guide call center representatives through the intervention processes, the main objective of knowledge acquisition was process tracking and message formulating. Once the reasoning process of a human expert is transferred into the WISS, procedural instructions can be derived from the WISS to direct a lay person to perform behavioral interventions like an expert.

Expert self-report was used for knowledge acquisition. The initial script for the intervention was written by a TTM expert. The script includes questions and anticipated patient responses derived from the Phase I study, messages that promote patients’ medication persistency, patients’ possible responses to the promotional messages, and decision rules that direct the intervention. The script was reviewed and validated by another expert at a major western US University. Biogen added <sup>b</sup>Brain<sup>Q</sup> data, which is the FDAapproved educational information that Biogen can provide to its MS patients. The revised script was then reviewed from a technical perspective. Incomplete rules and broken links were identified and fixed. In addition, the script was reviewed by the Promotional Review Board (PRB)<sup>1</sup> in Biogen and the Institutional Review Board (IRB) in the university where this research was conducted. Inappropriate wording such as those that had marketing connotations or implied the effectiveness of the drug were deleted or modified.

## 3.2.4. Design

The WISS was designed to be a Web-based system. The core processes run on the server side and call center representatives are able to share the functionality and patient data seamlessly in real time. Any changes made by one representative are visible to other representatives on the system.

The software design also includes architecture design, interface design, database design, and algorithm design. Architecture design determines the modularity of the WISS, the components of the WISS, and the relationships among the components. As Fig. 2 shows, the WISS consists of a graphical user interface, database, and Interventions, Recruitment, and Schedule components. The Interventions component has three sub-components: First Call, Next Call, and Last Call. The Recruitment component was designed for patient registration. Random assignment algorithms were built into this component for research purposes. The Schedule component was used for making appointments with patients. It is connected with Interventions and Recruitment in the figure because the scheduling function would be called in the Recruitment and Intervention processes. All the components are connected with both the Interface and the Database, indicating that users access the components of the software through the Interface and data generated by all the components would be saved into the Database.

![](/api/attachments/QT9FW9X4/fulltext/images/74431733af6873f4af5c2a1844210e138679d171b7854ed4a49793d52e6418c3.jpg)  
Fig. 2. Components in the WISS.

Algorithms are based on the script generated in the knowledge acquisition step. It is intuitive to use branching rules to represent the procedural knowledge utilized to structure an intervention. For example, if a patient is in Stage 1 and has a perceived importance rating above 7, he or she will receive an intervention call every four weeks; otherwise, he or she will receive a call every two weeks. Another example is when a patient rates a decisional balance item saliently (greater than 3 on a 5-point scale), more questions are needed to probe possible problems and <sup>b</sup>Brain<sup>Q</sup> educational information may be provided to the patient.

A relational database was designed to hold the patient and intervention data. Eight tables were created, and foreign keys and constraints bonded the tables together to ensure data referential integrity. The database structure was normalized to reduce data redundancy.

According to Silver [62], two schools of thought direct DSS design: directed change and non-direct change. The WISS used the notion of directed change which provides explicit decisional guidance [63] to influence decision makers. The goal of directed change is to determine the appropriate normative decision model to solve a problem and build it into software to move decision makers toward the normative strategy. Todd and Benbasat [68] believe that the DSS using directed change should focus on effort minimization to make the system easier to use than some competing alternative process that is available. The WISS is a directed change DSS. Correspondingly, simple and easy-to-use user interface is designed using the document object model (DOM).

## 3.2.5. Coding, testing, and deployment

Coding refers to the implementation of the software design. Active Server Pages, SQL, and ActiveX are used to implement the algorithms. HTML, JavaScript, and CSS are used to create the user interface. Visual Basic, ActiveX Data Object, and SQL are used to access the relational database. Extensive testing was undertaken after the first version of WISS was coded. Two Ph.D. students and a professor at a major southeastern university, a clinical assistant professor at a major western university, a marketing manager and a call center manager from Biogen, and two IT professionals from an IT consulting company tested the software against the software requirements. A good representative sample of all possible scenarios was fed into the software to examine the software performance. The testing was a repetitive process. After 15 rounds of testing and revising, the system performance was assessed by two TTM experts and was considered to have met the requirements. Before the WISS was deployed, several wording changes were made according to suggestions yielded from another PRB review.

## 3.3. Example scenarios

Some scenarios are presented here to illustrate the tailoring mechanism of the WISS. When a patient is called by a call center representative, her stage of change and perceived importance are assessed. If she is in Stage 1 and has a high importance score, the WISS will display encouraging comments and the intervention ends after that interaction, because, according to the TTM, the patient is not likely to discontinue her medication and no extra intervention is necessary at this time. If the patient is in Stage 2 or 3 or has a low importance score, the intervention will continue to explore her individual characteristics. For example, if her importance score is 5, she will be asked why she chooses 5 rather than 1. The purpose is to push her to think of the benefits of taking her medication. Next the representative will follow-up asking the patient what would have to happen in order for her to choose 6. The purpose is to elicit the most direct concern of the patient for her to move forward by a small step. At this point the WISS will address this concern immediately. For example, if the patient wants to experience fewer side effects, the WISS will display empathetic messages, explain the side effects, and offer tips about coping with the side effects. After this question, the WISS will assess the 16 pro and con items one by one. If the patient rates any item above 3 on a 5-point scale, the item will be considered as a salient characteristic and be addressed by the WISS. For example, if the patient chooses 5 on the con item <sup>b</sup>The injection is painful,<sup>Q</sup> the WISS will display a list of self-injection tips such as how to relax the mind and muscles for injections. Next the WISS will ask the patient if she wants to receive additional information on self-injection. If she does, a new entry will be entered into a to-do table in the database and Biogen’s employees will check the to-do table and mail requested materials to the patient.

As described above, the WISS only addresses problems relevant to each individual patient, thereby providing tailored interventions which reinforce pros and address cons perceived by a particular patient. Consequently, patients will perceive increased pros and decreased cons about continuing their Avonex. According to the TTM, these patients may move to a safer stage and become less likely to discontinue their medications.

## 4. Preliminary evaluation

A pilot study was carried out to preliminarily evaluate the implementation success of the WISS. The existing literature does not agree upon a single approach to define information systems’ implementation success, and a variety of different variables have been employed to reflect this construct [2,19].

DeLone and McLean [20] summarize information systems success dependent variables into a taxonomy which has six dimensions. In the latest update of their information systems success model DeLone and McLean [19] add net benefits as a new variable and remark that <sup>b</sup>the choice of where the impacts should be measured will depend on the system or systems being evaluated and their purpose.<sup>Q</sup> Zmud and Cox [74] also state that implementation success refers to realizing the intended benefits of the DSS. The WISS we developed is a specialized DSS intending to increase MS patients’ medication persistency. Enhancing medication persistency or reducing medication discontinuation is the purpose of the WISS. Therefore, we need to measure the variables that can reflect medication persistency. Specifically, the patient’s medication discontinuation rate and stages of change will be measured to reflect the system success. Randomized controlled trial is considered the most rigorous study design for evaluating the effect of IT applications in healthcare [67]. In order to test the causal relationship between the WISS and its intended benefits, we used a randomized controlled experiment for system evaluation.

## 4.1. Hypotheses

The medication persistency refers to the patient’s continuity with the prescribed medication. It can be measured from the group level and the individual level. In the group level, a group of patients who have high medication persistency should exhibit a low medication discontinuation rate. In the individual level, the medication persistency can be represented by the TTM construct, stages of change. As the Phase I study found, current Avonex users can be categorized into three stages with regard to patient readiness to discontinue Avonex (Note that patients in Stages 4 and 5 have already discontinued their medications). Stage 1 is the least risky stage and Stage 3 is the most risky stage. Patients in Stage 1 have higher medication persistency than patients in Stage 2 and 3. Therefore, the following hypotheses are created:

H1. Patients who receive interventions supported by WISS have a lower medication discontinuation rate than those who do not.

H2. Patients who receive interventions supported by WISS have a higher Stage 1 proportion than those who do not.

## 4.2. Experimental design

A longitudinal experiment was designed to evaluate the WISS. The experiment involved a treatment group and a control group with 224 patients in each group. All of the patients were currently taking Avonex to treat MS. Patients were randomly assigned to either the treatment group or the control group. A special randomization algorithm was utilized for the random assignment so that each group had the same number of patients.

Interventions were provided to the patients in the treatment group but not to those in the control group. Patients in Stage 1 with an importance scale rating greater than 7 were contacted every four weeks, whereas patients in Stage 2 or Stage 3 or with an importance scale rating less than or equal to 7 were called every two weeks. The ideal frequency for calling a patient was not known. The frequencies used in this study were based on practical experience of a pharmacy group who had extensive patient consultation experiences.

Three call center representatives were assigned to conduct interventions. Each representative received a short training course on how to use WISS. The experiment lasted three months. During this time, call center representatives made a series of calls to each patient in the treatment group. At the beginning of each intervention, patients were restaged and their perceived importance ratings were re-measured. Follow-up calls were scheduled based on the latest stage information and importance values. Therefore, the frequency for receiving interventions might fluctuate for each patient in the treatment group. At the end of the three months, final data collection was conducted by phone and online surveys.

## 4.3. Results

A total of 448 patients were recruited. There were 100 Stage 1 patients, 100 Stage 2 patients, and 24 Stage 3 patients in each group. The data of 82 patients became unusable during the experiment because we lost contact with the patients or the patients’ medical condition changed. At the end of the survey, a total of 366 patients’ data were collected. Table 1 shows the stage distribution of the 366 patients at the beginning of the experiment. Chi-square test shows that the stage proportions in the two groups were not significantly different $( \chi ^ { 2 } = . 6 8 , p = . 7 \bar { 1 } )$ . Ages ranged from 23 to 79 with an average of $4 6 . 0 \ \mathrm { ( S D } { = } 9 . 1 3 \mathrm { ) }$ . Approximately 83% of the patients were female and nearly 85% of the patients had received some college or higher education. Since the patients were randomly assigned to each group, their demographic data should be roughly the same. A T-test and Chi-square tests confirmed the two groups were not significantly different in terms of age $( t = . 9 2 , p = . 3 6 )$ , sex $( \chi ^ { 2 } = . 1 7 , p = . 6 8 )$ and education $( \chi ^ { 2 } = 1 . 6 5 , p = . 8 9 )$

At the end of the experiment, 17 patients in the control group and 2 patients in the treatment group discontinued Avonex (Table 2). The Chi-square test shows that the discontinuation rate in the two groups is significantly different from each other $( \chi ^ { 2 } = 1 0 . { \bar { 5 5 } } .$ $p { = } . 0 0 1 )$ ). The discontinuation rate in the treatment group (1.2%) is much lower than that in the control group (8.7%), indicating that the interventions supported by the WISS have affected the patients decision to discontinue their Avonex regimen. Therefore, H1 is supported.

An examination of the stage distribution at the end of the experiment revealed that the treatment group had relatively more patients in Stage 1 and fewer patients in Stage 2 than the control group (Table 3). Since the stage distributions of the two groups were the same at the beginning of the experiment, this suggests that some patients in the treatment group moved from Stage 2 toward Stage 1. Chi-square test indicates that the stage proportions are significantly dependent on the group $( \chi ^ { 2 } { = } 9 . 6 1 , ~ p { = } . 0 0 8 )$ . This result shows that the interventions supported by the WISS lead to stage differences between the two groups. Therefore, H2 is supported.

Table 1  
Stage distribution at the beginning of the experiment

<table><tr><td>Group</td><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td><td>Total</td></tr><tr><td colspan="5">Control</td></tr><tr><td>Count</td><td>93</td><td>85</td><td>17</td><td>195</td></tr><tr><td>Expected count</td><td>93.8</td><td>86.3</td><td>14.9</td><td>195.0</td></tr><tr><td>% within group</td><td>47.7%</td><td>43.6%</td><td>8.7%</td><td>100.0%</td></tr><tr><td colspan="5">Treatment</td></tr><tr><td>Count</td><td>83</td><td>77</td><td>11</td><td>171</td></tr><tr><td>Expected count</td><td>82.2</td><td>75.7</td><td>13.1</td><td>171.0</td></tr><tr><td>% within group</td><td>48.5%</td><td>45.0%</td><td>6.4%</td><td>100.0%</td></tr></table>

Table 2  
Discontinuation rate comparison

<table><tr><td>Group</td><td>Continue</td><td>Discontinue</td><td>Total</td></tr><tr><td colspan="4">Control</td></tr><tr><td>Count</td><td>178</td><td>17</td><td>195</td></tr><tr><td>Expected count</td><td>184.9</td><td>10.1</td><td>195.0</td></tr><tr><td>% within group</td><td>91.3%</td><td>8.7%</td><td>100.0%</td></tr><tr><td colspan="4">Treatment</td></tr><tr><td>Count</td><td>169</td><td>2</td><td>171</td></tr><tr><td>Expected count</td><td>162.1</td><td>8.9</td><td>171.0</td></tr><tr><td>% within group</td><td>98.8%</td><td>1.2%</td><td>100.0%</td></tr></table>

Because only three call center representatives used the WISS, no quantitative method was utilized to measure their user satisfaction. Instead, interviews were performed to get their feedback on the WISS. Representatives thought the questions provided by the WISS were probing and elicited patient responses from which they could find specific barriers to using Avonex for every patient. They also found the messages generated by the software for each patient response helpful and simple to read to the patient. Overall, they thought the WISS made sense and they were satisfied with it, suggesting that the WISS has good system quality, information quality, and user satisfaction [20,19].

## 5. Discussion

## 5.1. Implications for healthcare

WISS can contribute to MS patients’ health by preventing them from prematurely discontinuing their Avonex regimens. MS has a relapsing form featured by sporadic exacerbations. A patient might feel that it is unnecessary to continue taking medication during the stable period. However, MS may continue to develop insidiously without overt symptomatology [41]. If the patient stops taking Avonex, his or her MS may worsen and eventually cause serious deterioration in health which could have been avoided. WISS has the potential to reduce the number of physician visits. Based on our telephone interviews, many patients were at risk to discontinue Avonex because of psychological factors. For example, if a patient had an exacerbation and thought Avonex was not working, he or she may want to switch to an alternative medication. However, because of the nature of MS, the treatments can only control the disease, which means they only stop MS from getting worse but the current disease severity will not be decreased. If the patient switches to another medication, it is likely that he or she will also lose confidence in the new medication after another exacerbation. In this case, it is not clinically advantageous to switch medications and WISS may be able to convince the patient that Avonex is working without explicit sign of symptom alleviation.

From the standpoint of Biogen, the WISS is a marketing tool to reduce customer churn. The interventions could increase patient satisfaction with Biogen and Avonex and help Biogen maintain its market position. Although the WISS intends to promote the health of MS patients, it can also be beneficial to Biogen in the meantime. WISS creates a win–win situation for both MS patients and Biogen.

WISS deliver two types of decision support capabilities through two channels: the <sup>b</sup>chauffeured<sup>Q</sup> approach and the direct Web access. These vehicles pertain to the decision making of call center representatives and patients. First, the WISS supports the call center representatives to make decisions on how to intervene with MS patients. It turns the call center representatives into professional intervention counselors by transferring knowledge from TTM experts to the representatives by means of the WISS. Second, the WISS supports the MS patients’ decision making on whether to discontinue their Avonex regimens or not. The WISS delivers pertinent information, motivation, and empathy to the patients to prevent them from moving to the action stage where they discontinue taking medication.

Table 3  
Stage distribution at the end of the experiment

<table><tr><td>Group</td><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td><td>Total</td></tr><tr><td colspan="5">Control</td></tr><tr><td>Count</td><td>111</td><td>61</td><td>6</td><td>178</td></tr><tr><td>Expected count</td><td>123.6</td><td>48.2</td><td>6.2</td><td>178.0</td></tr><tr><td>% within group</td><td>62.4%</td><td>34.3%</td><td>3.4%</td><td>100.0%</td></tr><tr><td colspan="5">Treatment</td></tr><tr><td>Count</td><td>130</td><td>33</td><td>6</td><td>169</td></tr><tr><td>Expected count</td><td>117.4</td><td>45.8</td><td>5.8</td><td>169.0</td></tr><tr><td>% within group</td><td>76.9%</td><td>19.5%</td><td>3.6%</td><td>100.0%</td></tr></table>

Since the final intervention recipient is the patient, the <sup>b</sup>chauffeured<sup>Q</sup> approach is optional. Note: in this study we used the <sup>b</sup>chauffeured<sup>Q</sup> approach mainly because we wanted to control the patients’ participation rate. For public health promotion programs, it is more cost-efficient to deliver the interventions via direct Web access. Direct Web access means a virtual intervention takes place between patients and the WISS, which to a large extent depends on the patient’s willingness to initiate the intervention. Little research has been done to evaluate the effectiveness of this type of virtual intervention. Future research is called for in this direction.

This study uses a Web-based DSS to effectively change patients’ health-related behavior. The Webbased characteristic allows healthcare organizations or pharmaceutical companies to easily outsource the call center work to third parties. Two advantages are associated with using WDSS in call center outsourcing. First, the outsourcers can share their expertise with the outsourcees to increase the service quality. Second, the outsourcees’ work becomes more accountable since the outsourcers are able to check the calling data and patient retention rate in the central database. In addition, with patient data residing on the server which is physically located in the outsourcers facility, it is easier to apply security measures to protect patients’ privacy and ensure health data confidentiality.

Our study integrates the TTM into WDSS to help MS patients continue taking their Avonex. This idea can be extended to other health-related behaviors involving various chronic diseases and medications. Given that different health-related behaviors have different characteristics, we contend that it is essential to thoroughly investigate the behavior of interest and develop measurement instruments of the TTM constructs before the system development. For example, a WISS may be developed for Type II diabetes patients. Similar to MS, Type II diabetes is a chronic, progressive disease requiring lifelong treatment. Only a third of those who have Type II diabetes develop symptoms [27]. So, although treatment is necessary, patient compliance to treatment could be a problem and behavioral interventions are needed to enhance patient compliance. Different from MS, Type II diabetes patients usually need combination therapy ncluding diet, exercise, oral medications, and insulin injections [71]. Therefore, factors influencing Type II diabetes patient will differ from those influencing MS patient and should be investigated so that they can be utilized to develop effective intervention. Such investigation helps improve the information quality, an indicator of information systems success [20,19].

## 5.2. Experimental design adequacy

The preliminary evaluation of the WISS used a control group and a treatment group and randomly assigned patients to each group. This randomized, controlled experimental design allows the logical conclusion of a cause and effect relationship between the stimulus (independent variable) and the response (dependent variable) to be made manifest [40]. There are three requirements of causality: concomitant variation, order of occurrence of variables, and elimination of other possible causal factors [59]. The research design of this study satisfies all of these requirements. First, the presence of the WISS and the patient discontinuation behavior are correlated (concomitant variation). Second, the interventions were provided before the response differences took place (order of occurrence). Finally, the existence of the control group and random assignment controlled all the extraneous variables that could affect patient responses [32]. The effects of these extraneous variables were deemed theoretically equal between the treatment and the control group (elimination of other possible causal factors). The intervention was considered the only variable differentiating the two groups. Therefore, the significant differences in the drug discontinuation rates and stage proportions between the treatment group and the control group are attributed to the intervention supported by the WISS.

It is worth noting that WISS is used to improve effectiveness of call center representatives, not efficiency. Providing behavioral interventions to multiple sclerosis patients requires substantial professional training in health psychology. The representatives did not have such training and could not provide tailored intervention independently. WISS offers stepby-step instructions to enable representatives to conduct tailored interventions. It is clear that WISS is designed to enable people to do something they couldn’t do before, rather than to do things more efficiently which they have been doing. The idea is to make professional knowledge available to lay people who work as call center representatives and employ these lay people to provide health behavioral interventions, thereby reducing healthcare delivery costs. Therefore, this paper focuses on effectiveness of WISS-supported interventions rather than improved efficiency of call center representatives as a result of using WISS.

## 5.3. Limitations

It should be noted that this study has a practical limitation. The experiment was designed in such a way that it provided indirect evidence to support the effectiveness of WISS. It is tempting to include a third patient group that receives regular phone calls, and to validate the efficacy of the WISS only when interventions supported by the WISS are proven to be better than interventions not supported by the WISS. A practical concern stopped us from employing the third patient group. Biogen would not staff a caller team to call patients without using the WISS, because past experience of Biogen’s call center revealed that making phone calls to patients would not stop them from discontinuing Avonex. Given Biogen’s past experience, our current two-group experimental design seems to be adequate to evaluate the effectiveness of the WISS, and adding a third group becomes inconsequential.

Another limitation stems from an assumption we take when we demonstrate the value of WISS. We assume that if call center representatives, helped by the WISS, can persuade patients to continue using Avonex, then the WISS is effective. Under this assumption, representatives’ intervention capability is solely obtained from the WISS. The assumption could be wrong. For example, if the representatives suddenly become TTM experts, we cannot conclude that WISS is effective. However, likelihood of violating this assumption is low. There is little evidence showing that representatives can possibly obtain TTM-based behavioral intervention knowledge from sources other than the WISS during the experiment. Therefore, limitation resulting from this assumption is not serious.

Due to the limitations, we took a conservative stance to draw conclusions from this study. We have no intention to claim that WISS-supported interventions are more effective than general interventions. Nonetheless, we found that WISS-supported interventions are effective. So we confined our conclusion to effectiveness of the WISS in terms of its ability to turn lay people into effective health intervention providers.

## 6. Conclusion

The Web’s ability to disseminate knowledge and drive down interaction costs is fundamentally transforming the healthcare system [31]. Tailored health information can be disseminated on the Web and delivered to patients. This paper describes the development and evaluation of a Web-based intervention support system that enhances MS patients’ medication persistency. The intervention strategy based on the TTM is built into the system after careful planning and research. Results of preliminary system evaluation indicate that the WISS can reduce the MS patients’ medication discontinuation rate and move more patients to the stage where discontinuation is less likely to happen. The findings suggest that the integration of behavioral theories and Web-based DSS can make significant contribution to the healthcare delivery to the public. In addition, this research has implications for the development of Web-based DSS in general. It demonstrates that complicated theory-based knowledge can be embedded into DSS and distributed through the Web. It is essential to have a welldefined problem domain and adapt general theory to fit that domain. Therefore, adequate emphasis should be put on the development of problemspecific knowledge.

## Acknowledgement

This research is supported by a research grant from Biogen. The authors thank the project team in Biogen for their cooperation. The authors also thank Dr. Terry Anthony Byrd for his comments on an early version of this paper.

## References

[1] D. Abrams, S. Mills, D. Bulger, Challenges and future for tailored communication research, Annals of Behavioral Medecine 21 (4) (1999) 299–306.

[2] M. Alavi, E.A. Joachimsthaler, Revisiting DSS implementation research: a meta-analysis of the literature and suggestions for researchers, MIS Quarterly 16 (1) (1992) 95 – 116.

[3] L. Baker, T.H. Wagner, S. Singer, M.K. Bundorf, Use of the internet and e-mail for health care information, JAMA 289 (18) (2003 May) 2400– 2406.

[4] A. Bandura, Self-efficacy: toward a unifying theory of behavior change, Psychological Review 84 (1977) 191– 215.

[5] A. Bandura, Self-efficacy mechanism in human agency, American Psychologist (37) (1982) 122– 147.

[6] D. Bates, L. Leape, D. Cullen, Effect of computerized physician order entry and a team intervention on prevention of serious medication errors, JAMA 280 (1998) 1311 –1316.

[7] D. Bental, A. Cawsey, Personalized and adaptive systems for medical consumer applications, Communications of the ACM 45 (5) (2002) 62– 63.

[8] B. Berger, K. Hudmon, H. Liang, Predicting discontinuation of treatment among patients with multiple sclerosis: an application of the transtheoretical model of change, Journal of the American Pharmacists Association 44 (4) (2004) 445 – 454.

[9] D.J. Berndt, A.R. Hevner, J. Studnicki, The catch data warehouse: support for community health care decisionmaking, Decision Support Systems 35 (3) (2003 June) 367– 384.

[10] H.K. Bhargava, R. Krishnan, The world wide web: opportunities for operations research and management science, INFORMS Journal on Computing 10 (4) (1998) 359–383.

[11] H.K. Bhargava, C.G. Tettelbach, A Web-based decision support system for waste disposal and recycling, Computers, Environment and Urban Systems 21 (1) (1997) 47–65.

[12] H.K. Bhargava, R. Krishnan, R. Mu¨ller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 19 (3) (1997) 193– 214.

[13] R. Bunton, S. Baldwin, D. Flynn, S. Whitelaw, The <sup>d</sup>stages of change<sup>T</sup> model in health promotion: science and ideology, Critical Public Health 10 (1) (2000) 55 – 71.

[14] A.T.S. Chan, J. Cao, H. Chan, G. Young, A Web-enabled framework for smart cared application in health services, Communications of the ACM 44 (9) (2001 September) 77–82.

[15] M. Culnan, Chauffeured vs. access to commercial database: the effects of task and individual differences, MIS Quarterly 7 (1) (1983 March) 57– 67.

[16] Crossing the quality chasm: a new health care system for the 21st century, Institute of Medicine, Washington DC, 2001.

[17] T.H. Davenport, J. Glaser, Just-in-time delivery comes to knowledge management, Harvard Business Review 80 (7) (2002 July) 107– 111.

[18] H. De Vries, J. Brug, Computer-tailored interventions motivating people to adopt health promoting behaviors: introduction to a new approach, Patient Education and Counseling 36 (1999) 99– 105.

[19] W.H. Delone, E.R. McLean, Information systems success: the quest of the dependent variable, Information Systems Research 3 (1) (1992) 60– 95.

[20] W.H. Delone, E.R. McLean, The DeLone and McLean model of information systems success: a ten-year update, Journal of Management Information Systems 19 (4) (2003) 9– 30.

[21] J. Dong, H.S. Du, S. Wang, K. Chen, X. Deng, A framework of Web-based decision support systems for portfolio selection with OLAP and PVM, Decision Support Systems 37 (3) (2004) 367– 376.

[22] E. Feil, J. Noell, E. Lichtenstein, S. Boles, H. McKay, Evaluation of an internet-based smoking cessation program: lessons learned from a pilot study, Nicotine Tobacco Research 5 (2) (2003 April) 189– 194.

[23] B.J. Fogg, Persuasive technologies, Communications of the ACM 42 (5) (1999) 27–29.

[24] J. Forkner-Dunn, Internet-based patient self-care: the next generation of health care delivery, Journal of Medical Internet Research 5 (2) (2003) e8.

[25] R. Friedman, J. Stollerman, D. Mahoney, L. Rozenblyum, The virtual visit: using telecommunications technology to take care of patients, Journal of the American Medical Informatics Association 4 (1997) 413–425.

[26] Healthcare satisfaction study 2000. Harris Interactive/ARiA marketing, World Wide Web, http://www.harrisinteractive. com/news/downloads/HarrisAriaHCSatRpt.pdf, 2000.

[27] A. Hingley, Diabetes demands a triad of treatments, in FDA consumer, The Food and Drug Administration, 1997, http:// vm.cfsan.fda.gov/\~dms/fdacdia2.html.

[28] T.L. Huston, J.L. Huston, Is telemedicine a practical reality?, Communications of the ACM 43 (6) (2000 June) 91 – 95.

[29] I.L. Janis, L. Mann, Decision making: a psychological analysis of conflict, choice and commitment, Free Press, New York, 1977.

[30] S.S. Johnson, D.M. Grimley, J.O. Prochaska, Prediction of adherence using the transtheoretical model: implications for pharmacy care practice, Journal of Social and Administrative Pharmacy 15 (3) (1998) 135– 148.

[31] A.S. Kellen, S.V. Kuiken, Health on-line: the best will get bigger, The McKinsey Quarterly (4) (2000) 131– 135.

[32] F.N. Kerlinger, H.B. Lee, Foundations of Behavioral Research, 4th ed, Harcourt College Publishers, 2000.

[33] G.E. Kersten, S.J. Noronha, WWW-based negotiation support: design, implementation, and use, Decision Support Systems 25 (2) (1999 March) 135–154.

[34] P. Keskinocak, R. Goodwin, F. Wu, R. Akkiraju, S. Murthy, Decision support for managing an electronic supply chain, Electronic Commerce Research 1 (2001) 15 – 31.

[35] D.G. Kilman, D.W. Forslund, An international collaboratory based on virtual patient records, Communications of the ACM 40 (8) (1997 August) 111 – 117.

[36] E. Kim, W. Kim, Y. Lee, Combination of multiple classifiers for the customer’s purchase behavior prediction, Decision Support Systems 34 (2) (2003 January) 167 – 175.

[37] P. King, J. Tester, The landscape of persuasive technologies, Communications of the ACM 42 (5) (1999) 31 – 38.

[38] R. Kohli, F. Piontek, T. Ellington, T. VanOsdol, M. Shepard, G. Brazel, Managing customer relationships through Ebusiness decision support applications: a case of hospital– physician collaboration, Decision Support Systems 32 (2) (2001 December) 171– 187.

[39] M. Kreuter, C. Skinner, Tailoring: what’s in a name?, Health Education Research 15 (2000) 1 – 4.

[40] R.L. Mikeal, in: A. Nelson (Ed.), General Research Design, in Research in Pharmacy Practice: Principles and Methods, American Society of Hospital Pharmacist, 1981, pp. 23 – 29.

[41] D.C. Mohr, D. Cox, Multiple sclerosis: empirical literature for the clinical health psychologist, Journal of Clinical Psychology 57 (4) (2001) 479– 499.

[42] D.C. Mohr, et al., Therapeutic expectations of patients with multiple sclerosis upon initiating interferon beta-1b: relationship to adherence to treatment, Multiple Sclerosis 2 (5) (1996) 222–226.

[43] D.C. Mohr, D.E. Gooddin, W. Lidosky, N. Gatto, K.A. Baumann, R.A. Rudick, Treatment of depression improves adherence to interferon beta-1b therapy for multiple sclerosis, Archives of Neurology 54 (1997 May) 531– 533.

[44] D.C. Mohr, et al., Side effect profile and adherence to in the treatment of multiple sclerosis with interferon beta-1a, Multiple Sclerosis 4 (6) (1998) 487– 489.

[45] D.C. Mohr, et al., The psychosocial impact of multiple sclerosis: exploring the patient’s perspective, Health Psychology 18 (4) (1999) 376– 382.

[46] D.C. Mohr, et al., Treatment adherence and patient retention in the first year of a phase-III clinical trial for the treatment of multiple sclerosis, Multiple Sclerosis 5 (1999) 192 – 197.

[47] D.C. Mohr, et al., Telephone-administered cognitive-behavioral therapy for the treatment of depressive symptoms in multiple sclerosis, Journal of Consulting and Clinical Psychology 68 (2) (2000) 356– 361.

[48] D.C. Mohr, A.C. Boudewyn, W. Likosky, E. Levine, D.E. Goodkin, Injectable medication for the treatment of multiple sclerosis: the influence of self-efficacy expectations and injection anxiety on adherence and ability to self-inject, Annals of Behavioral Medecine 23 (2) (2001) 125– 132.

[49] M. Napolitano, et al., Evaluation of an Internet-based physical activity intervention: a preliminary investigation, Annals of Behavioral Medecine 25 (2) (2003) 92– 99.

[50] R.M. O’Keefe, T. McEachern, Web-based customer decision support systems, Communications of the ACM 41 (3) (1998) 71– 78.

[51] D.J. Power, Free decision support systems glossary. DSSResources.com, World Wide Web, http://www.dssresources.com/ glossary/, 2004.

[52] J.O. Prochaska, C.C. DiClemente, The transtheoretical approach: crossing traditional boundaries of therapy, Dow Jones-Irwin, Homewood, Illinois, 1984.

[53] J.O. Prochaska, C.C. DiClemente, in: N. Heather (Ed.), Toward a comprehensive model of change, in treating addictive behaviors: processes of change, Plenum Press, New York, 1986.

[54] W. Raghupathi, J. Tan, Strategic IT applications in health care, Communications of the ACM 45 (12) (2002 December) 56– 61.

[55] W. Rakowski, et al., Confirmatory factor analysis of opinions regarding the pros and cons of mammography, Health Psychology 18 (5) (1997) 433 – 441.

[56] D. Revere, P. Dunbar, Review of computer-generated outpatient health behavior interventions: clinical encounters <sup>b</sup>in absentia<sup>Q</sup>, JAMIA 8 (1) (2001) 62– 79.

[57] J.A. Rodger, P.C. Pendharkar, Using telemedicine in the Department of Defense, Communications of the ACM 43 (3) (2000 March) 19–20.

[58] P. Ryan, R. Lauver, The efficacy of tailored interventions, Journal of Nursing Scholarship 34 (4) (2002) 331– 337.

[59] C. Selltiz, L.S. Wrightsman, S.W. Cook, Research methods in social relations, Holt, Rinehart and Winston, New York, 1976.

[60] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002 June) 111– 126.

[61] W. Silberg, C. Lundberg, R. Musacchio, Assessing, controlling, and assuring the quality of medical information on the internet, JAMA 277 (1997) 1244– 1245.

[62] M.S. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 (1) (1990) 47– 70.

[63] M.S. Silver, Decisional guidance for computer-based decision support, MIS Quarterly 16 (1) (1991) 105– 122.

[64] S. Sridhar, Decision support using the intranet, Decision Support Systems 23 (1) (1998 May) 19– 28.

[65] R.P. Sundarraj, A Web-based AHP approach to standardize the process of managing service-contracts, Decision Support Systems (2003).

[66] D.F. Tate, E.H. Jackvony, R.R. Wing, Effects of internet behavioral counseling on weight loss in adults at risk for type 2 diabetes, JAMA 289 (14) (2003 April) 1833– 1836.

[67] W.M. Tierney, Improving clinical decisions and outcomes with information: a review, International Journal of Medical Informatics 62 (2001) 1– 9.

[68] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aid, MIS Quarterly 16 (3) (1992) 373– 393.

[69] E. Turban, J.E. Aronson, Decision support systems and intelligent systems, Prentice Hall, Upper Saddle River, New Jersey, 2001.

[70] W.F. Velicer, C.C. DiClemente, J.O. Prochaska, N. Brandenburg, Decisional balance measure for assessing and predicting

smoking status, Journal of Personality and Social Psychology 48 (5) (1985) 1279– 1289.

[71] J.R. White, Combination oral/insulin therapy in patients with type II diabetes mellitus, Clinical Diabetes (1997 May–June).

[72] C. Willey, et al., Stages of change for adherence with medication regimens for chronic disease: development and validation of a measure, Clinical Therapeutics 22 (7) (2000 July) 858 – 871.

[73] V.E. Wilson, Asynchronous health care communication, Communications of the ACM 46 (6) (2003 June) 79– 84.

[74] R.W. Zmud, J.F. Cox, The implementation process: a change approach, MIS Quarterly 3 (2) (1979) 35 – 43.

![](/api/attachments/QT9FW9X4/fulltext/images/113a24acadeedb11e61e47938867dff2e0ae267f3215a90fd3039fea8921cd8b.jpg)

Huigang Liang is an Assistant Professor of Information Systems at Florida Atlantic University. He received his Ph.D. from Auburn University in 2003. His research focuses on information systems in health care, enterprise systems implementation, and electronic commerce. His research appeared in Communications of the ACM, Communications of the AIS, the Journal of Strategic Information Systems, International Journal of Medical Infor-

matics, Journal of the American Pharmacists Association, Hospital Pharmacy, International Journal of Production Economics, International Journal of Information Management, among others.

![](/api/attachments/QT9FW9X4/fulltext/images/c0eede67f448d5f226daa73e7ce396a19aa5788cb2c3b0ec1090d8c0e8053a7b.jpg)

Yajiong Xue is an Assistant Professor of Information Systems at the University of Rhode Island. She received her Ph.D. from Auburn University in 2004. She worked for Pharmacia and Upjohn and Kirsch Pharma GmbH for several years. Her research appears in such journals as Communications of the ACM, Communications of the AIS, Journal of Computer Information Systems, the Journal of Strategic Information Systems, International Journal of Pro-

duction Economics, International Journal of Medical Informatics, and International Journal of Information Management. Her current research interests include the strategic management of information technology, IT decision making, and healthcare information systems.

![](/api/attachments/QT9FW9X4/fulltext/images/916d86870e6d414bf2e97d8d06d419d685667512db58495c7a338790cc74d6c5.jpg)

Bruce Berger is a Professor and currently Head of the department of Pharmacy Care Systems at Auburn University. Bruce received his BS in Pharmacy, Master and Ph.D. in social and behavioral pharmacy from The Ohio State University. His research interests include interpersonal and organizational communication and psychology, and application of these disciplines to the pharmacist’s role in treatment adherence and treatment outcomes. He is also inter-

ested in developing new service roles for the pharmacist. He has published or presented over 500 papers or seminars on these topics. He has attracted over three million dollars in funding to support his research and has been a project leader in a reengineering project of a major U.S. drug chain. In October of 1997 Bruce was named by American Druggist magazine one of the 50 most influential people in U.S. pharmacy. In March of 2004 Bruce was awarded a fellowship by the American Pharmacists Association Academy of Pharmaceutical Research and Science for a lifetime of quality research.
