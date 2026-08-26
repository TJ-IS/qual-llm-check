---
otero_id: 10128
otero_key: "YFW759AF"
title: "Mobile health: A carrot and stick intervention to improve medication adherence"
authors: "Xinying Liu; Upkar Varshney"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113165"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mobile health: A carrot and stick intervention to improve medication adherence

![](/api/attachments/YFW759AF/fulltext/images/5cf42b4def1b48baaab700aca31149eb17074f5a5c614674ad2578db3bda1b49.jpg)

Xinying Liu, Upkar Varshney

Department of Computer Information Systems, Georgia State University, Atlanta, GA 30302-4015, United States of America

## A R T I C L E I N F O

Keywords: Intervention Mobile health Medication non-adherence Positive reinforcement Negative reinforcement Analytical modeling

## A B S T R A C T

Medication adherence is a critical element in promoting healthcare outcomes, especially for chronic medical conditions. However, due to several underlying factors, major challenges such as how to improve and maintain the required level of medication adherence still exist. We propose a novel mobile health-based intervention, we call Carrot and Stick, to promote medication adherence (MA) for patients with intentional and/or unintentional non-adherence. Drawing on Social Cognitive Theory, Social Exchange Theory, Goal-setting Theory, and people's dependency on smartphones, we develop a composite intervention using both positive and negative reinforcements, goal-setting, and social connections. The m-health intervention provides decision support to patients in their medication-taking process. With multiple intervention scenarios, healthcare professionals have baselines to adjust the intervention to meet patients' needs. We validate our design using analytical modeling and show that (1) high medication adherence is achievable by the composite intervention for single and multiple medications, (2) negative reinforcement (NR) leads to better MA outcomes in addition to positive reinforcement (PR), (3) the intervention can maintain efectiveness in the operational environment due to its adaptability, and, (4) the estimated healthcare savings are significant even for slightly improved medication adherence. Our research is the first to utilize NR in intervention design to enhance MA and to categorize patients based on elements derived from theories while providing technical and behavioral interventions for both unintentional as well as inten tional non-adherence. The future work can address multiple diferent types of NR; development of DSS for patients, caregivers, and healthcare professionals; and, integration of other m-health interventions for creating sophisticated and highly efective personalized solutions.

## 1. Introduction

## 1.1. Background

Medication non-adherence is an ever-present and complex problem, especially for patients with chronic diseases. Research eforts have led to medications with proven eficacy and the adherence to medications works as “the key mediator between medical practice and patient outcomes” [1]. However, about half of Americans with chronic diseases are non-adherent [2]. A strong association between medication ad herence (MA) and clinical outcomes (re-hospitalization, morbidity, and mortality) has been demonstrated [3]. For example, antihypertensive medications reduce the stroke risk by 30%; however, the adherence rate is 60% two years after the first ischemic stroke [4]. Further, non-adherence imposes an estimated financial burden of \$100 billion/year upon US healthcare systems [5].

Four groups of factors contribute to medication non-adherence:

inadequate dose frequency and/or scheduling [7,8]; poor health literacy [9]; demographic factors [10,11] including beliefs in treatment efectiveness [12] and motivational factors [13]; and lack of social support [14]. Interventions have been proposed to improve medication adherence rate (MAR) to 80% or higher [15,16]. However, efective interventions are complex and expensive [17].

M-health is defined as “healthcare to anyone, anytime, and anywhere by removing locational and temporal constraints while increasing both the coverage and the quality of healthcare” [15,18]. M health facilitates interventions based on its functionalities, inexpensiveness, broad adoption and constant accessibility, and sustainable and afordable decision support [19]. M-health provides healthcare information to help patients make better decisions, follow physicians' advice, and receive better healthcare [18]. The common interventions are reminders, educational messages, and self-monitoring. Many studies have found significant improvement in MA with these intervention [20].

## 1.2. Our focus and contributions

Despite the promising outcomes of existing interventions, there is a lack of long-term studies, appropriate statistical and economic analysis, and test of theory-based interventions [5,20]. Many interventions are based on short-term studies and small sample size, which lead to less than reliable results [24–26]. Smartphone users are dependent or almost addicted to mobile apps, such as Facebook, Twitter, and many games. This dependence inspires us to design our novel intervention, Carrot and Stick (C&S). The “carrot” element is Positive Reinforcement (PR) or a reward to increase a specific response. The “stick” element is Negative Reinforcement (NR) taking away an element in the in dividual's environment when the undesired behavior occurs. We use “blocking the user's most used app” as our innovative NR, facilitated by the dependence or addiction to particular app(s). Our design of C&S intervention addresses the lack of evidence of the motivational intervention's efectiveness by answering our first research question: how can positive and negative reinforcement-based interventions improve MA through impacting patients'decisions? We also fill the gaps in mhealth intervention literature, namely lack of economic analysis and insuficient theory base, by answering our second and third research questions: What is the theory base of studied intervention? And what are the efectiveness and decision support application scenarios of the intervention?

We follow the design science approach and use theories to generate, evaluate, and improve our C&S design by integrating NR and PR. We also develop the application scenarios of the intervention following an iterative process. Our research contributes to the literature in two ways. First, we establish a theoretical foundation to address the gap in reinforcement interventions in m-health. Our research is the first to uti lize NR in the intervention for medication adherence. This NR com plements the application of reinforcements in behavior change literature. Second, we develop scenarios for diferent patient types and illustrate how to optimize designed system parameters. Our research is also the first to categorize the patients based on theories and to provide suitable technical and behavioral interventions. Our study ofers a welldesigned and valid novel intervention to impact patients' medication intake decisions. We utilize analytical modeling to validate our design based on theories. The results confirm the individual efectiveness of reinforcements and in combinations with other interventions, such as reminders, in promoting patients' MA over time. The intervention can lower patients' risk of re-hospitalization by enhancing MA, thus reducing the burden on healthcare systems. Moreover, the tracked medi cation-intake through our intervention can improve the quality of in formation for treatment decisions. Further, the reduced probability of overconsumption of medication doses is highly beneficial to patients and highly desirable for healthcare professionals.

## 1.3. Organization of the paper

First, we discuss related theories for the intervention design and review the literature on medication adherence. We then present the design and detailed operation of our m-health-based intervention. For validation, applicable scenarios of the intervention are described, followed by the evaluation using analytical modeling. Then, we present conclusions of our study and discuss avenues for future research.

## 2. Theoretical background and related literature

In this section, we discuss some theories to support the intervention design and its efectiveness. Also, the theories provide us with guide lines in creating multiple scenarios of intervention application.

## 2.1. Social Cognitive Theory and health promotion

Social Cognitive Theory (SCT) posits that learning occurs in a social context with a dynamic interaction of the person, environment, and behavior [27]. SCT emphasizes social influence on external and internal social reinforcement. SCT is widely applied in public health as it explains how people regulate their behavior through control and reinforcement to achieve goal-directed behavior that can be maintained over time [27]. The five core determinants in health promotion beha viors [28] are

1. Knowledge of health risks and benefits of diferent health practices (people will not change their habits if they lack knowledge of how these behaviors would afect their health)

2. People's outcome expectations of diferent health habits (not only positive or negative efects of the behavior on an individual but also social reactions of the action)

3. The health goals people set for themselves and the concrete plans and strategies to realize them (cognitive goals provide further selfincentives and guides to health behavior)

4. Perceived facilitators and social/structural impediments to the changes (this would partly determine how smooth the change process could be)

5. Perceived self-eficacy that one can exercise over one's health habits (a focal determinant because it afects health behavior both directly and by influencing other determinants).

Based on these, three approaches are developed to encourage people to adopt health-promoting behaviors (a) informing people about the health risks of detrimental habits and the benefits of healthy behaviors, (b) rewarding people for health-promoting behaviors by linking beha viors to extrinsic reinforcements, and, (c) treating personal change as occurring within a network of social influences. The four intervention categories are (1) informational interventions on cognitive strategies designed to educate and motivate patients, (2) behavioral interventions designed to influence behavior through shaping, reminding, or rewarding desired behavior (reinforcement), (3) family and social inter ventions provided by family or friends, and, (4) composite interventions with two or more interventions [29]. The convergence of theory-based approaches and evidence-summarized categories lend credence to using SCT to design our intervention. Meanwhile, not all previous studies show very clear and robust support for the interventions' efectiveness, and most studies only focus on single intervention type. We identify this as a major gap in the literature. This also creates an opportunity to (a) improve the intervention design and (b) combine multiple interventions with significant functionalities to address medication non-adherence, both intentional and unintentional.

A review article, using 19 papers on PR including cash, voucher, lottery, and candy for kids, shows that PR can efectively promote MA for diferent diseases, including children with TB, HIV patients, and opioid addiction patients. The study finds a positive relationship between the value of incentives and the impact of the intervention. In general, for PR, post-intervention evaluations are rare, however, there is a significant drop in adherence after the PR-based interventions are discontinued [30]. The benefits patients get from following health promotion behavior are only reflected in gaining PR but are not internalized to the perceived health condition improvement before the incentives are discontinued. So, the efect of PR is examined in several studies, but the combined efects of both PR and NR have not been studied for healthcare interventions. This is promising as NR is shown, in other disciplines (education and criminology), to be more efective in modifying behavior than PR [31].

## 2.2. Goal-setting theory

The goals people set and the plans they make are important determinants of the behavior change process. Furthermore, in Goal-setting Theory, setting specific goal to achieve a task, in combination with performance feedback, leads to higher performance than no or vague goal [33,34]. Goal-setting encourages a person to try harder for extended period. Another central tenet is the linear goal dificulty-performance relationship, where higher the goal, the better people perform [33,34]. There are conditions for which the goal dificulty-performance relationship is not strong when tasks are too complex and the individual is not capable of or not committed to the goals [35].

Therefore, to ensure a strong goal dificulty-performance relation ship in the designed intervention, one question is: which one is better, self-set goal or provider-assigned goal? Alexy [36] found that letting patients select their own goals did not lead to a diferent result from behavior change with provider-assigned goals. The assigned goal group was found to be statistically superior to the self-set goal group [37]. Self-set goals could result in poorer outcomes as it could be either too easy or too dificult, while a provider-assigned goal can be more appropriate. However, the provider may not be aware of the real dificulties for the patients and may set inappropriate goals. Also, patients may have a more significant commitment to self-set goals [38].

## 2.3. Social exchange theory

Homans defined social exchange as the exchange of activity, tangible or intangible, and more or less rewarding or costly, between at least two parties [39]. He argued that “there was nothing that emerges in social groups that cannot be explained by propositions about individuals as individuals, together with the given condition that they happen to be interacting” [40]. Reinforcement principles derived from the behavioral research were used to explain the persistence of exchange relations. Behavior is viewed as a function of payofs, whether the payofs are provided by the environment or by other humans.

Homans had five key propositions that examined social behavior regarding reinforcement. The first, the success proposition, states that action which generates rewards is likely to be repeated. The second, the stimulus proposition, states that behavior which has been rewarded under the specific circumstance in the past will be performed in similar circumstances in the future. The third, the value proposition, states that an individual is more likely to perform an action if the action has a more valuable result. The fourth, or the deprivation- satiation proposition, uses diminishing marginal utility: the more often an individual has recently received a particular reward, the less valuable is an addi tional unit of that reward. Finally, the fifth proposition says that individuals will react to diferent reward situations emotionally. People will become angry when they do not receive what they anticipate [41].

Following these propositions, we observe that PR in our intervention will encourage the patient to repeat medication-taking behavior if we reward each on-time-taken dose. In our design, the most suitable solution to avoid the diminishing efect is to provide an increasing PR value to the patient over time. However, individual variance exists, so providing an increasing PR to every patient is unnecessary. More details related to PR design and its suitable patient types are in the Scenarios section.

## 2.4. Current M-health interventions

To present the current research on mobile interventions for MA and to discover the literature gaps, a literature search of Web of Science, AIS electronic library, and IEEE digital library was conducted using (1) intervention, (2) medication adherence, and (3) mobile. The electronic databases were searched in April 2019 for publications after 2010. We use the following criteria: (1) adult patients (≥18 years) with chronic disease, (2) mobile intervention for MA, (3) quantitative efect of the intervention on MA. We excluded studies with only intervention design or study protocol or psychiatric, military, or institutionalized patients. This was to avoid the potential influence of psychological or institutional controls on adherence. The entire selection process is shown in Fig. 1.

We identified 24 studies that met our inclusion criteria. The studie evaluate mobile intervention's efect on various chronic diseases, including HIV, hypertension, and diabetes. Self-report is the most commonly used method to assess MA [5,42–46], followed by behavior monitoring [22,47] and smart pill container [48]. The intervention types (Table 1) includes text messages, with dose reminders [5,42,43,46,49,50] and medical information [51–53]. The variation in intervention characteristics is significant. Many studies utilize text messages at a fixed frequency [50,54]. Two studies compare the efect of simple vs personalized text message reminders [54,55]. No diference in MA was found in using or not using emotional status [54]. The personalized reminder is efective without increasing the probability of taking more than prescribed doses [55]. Most studies do not show a significant increase in MA, they text messages are an efective and feasible intervention. Social support, the second most studied intervention, can be provided by social network interaction or by instant connection with a physician and is shown to improve MA [23,47,56]. Also, combined social support and text messages as an intervention is more efective in improving MA and self-management behaviors than text messages alone [23]. Meanwhile, information sharing preference is found among elderly patients who are willing to share their profile but not medication loggers, but many patients are willing to share all in formation with the same community [22]. Mobile application and in home sensor monitoring have significant potential, and a higher MAR is found among elderly patients [21]. Besides, the mobile app with electronic medication container not only provides more accurate MA data than self-report but also helps to increase adherence and leads to improved control of health indicator such as blood pressure [47,48]. Inhome monitoring utilizes sensors for patient's behaviors. It enables condition-based medical treatment to increase MA and also decrease possible side-efects, while more work needs to be done for a broader adoption [47,57,58].

## 2.5. Limitations of existing interventions and our contributions

The limitations of existing interventions are (1) examined interventions' duration is not long enough to study the efectiveness for chronic diseases, (2) NR never been used in healthcare interventions, and (3) functionalities of examined interventions lack theoretical support, which combined with limited intervention duration afects the reliability of results.

From theories and literature review, there is a need for an inter vention using positive and negative reinforcements. The dependence on specific mobile apps can be utilized to implement NR. If we build a causal relationship between non-adherence behavior and disconnection to favorite mobile apps, the patient's intention to re-connect to the app can lead to changes in the non-adherence behavior. Our design of C&S is innovative in (a) addressing intentional non-adherence by integrating PR and NR with previously validated reminder and social connection elements, (b) using theories for design, which increases the reliability of results using analytical modeling, and, (c) developing ten scenarios for the intervention, identifying suitable patient types, and addressing costefectiveness as part of decision support. For validation, we illustrate detailed operation of the intervention. Even a slight improvement in the probability of dose taking in time-windows improves the adherence outcome. The work can lead to the implementation of diferent interventions; development of DSS for patients, caregivers, and healthcare professionals; and, integration of other interventions for creating personalized solutions. This can help patients and family members to improve MA, healthcare professionals to support patients with personalized interventions leading to desirable health outcomes, and decision makers to perform short and long-term decisions on resource allocations and outcomes.

![](/api/attachments/YFW759AF/fulltext/images/73733d62a65188403fa596525e5480a071c053976a35817adba170500a1690c1.jpg)  
Fig. 1. Study selection process.

Table 1 Intervention types and studies.

<table><tr><td>Intervention type</td><td>Number of studies</td></tr><tr><td>Text message reminder and/or educational text message</td><td>18</td></tr><tr><td>Social support</td><td>6</td></tr><tr><td>Mobile application enabled self-management</td><td>4</td></tr><tr><td>In-home monitoring</td><td>3</td></tr></table>

Note: some studies covered more than one type of interventions.

## 3. System design

Our design of the system utilizes the design science approach [60]. We generated guidelines for our design based on the theories discussed in the last section. Also, we considered the previous examined models about the adoption of health IT and m-health decision support systems by both patients and hospital's professionals [61.62]. as well as the longitudinal time frame of user acceptance of decision support technology [63] when we integrate our design. Following the design guidelines, we created an artifact and evaluated its efectiveness in promoting MA. We added modifications to our artifact to address any identified limitations in efectiveness evaluation and then repeated the evaluation and improvement process until our designed system met its performance goal. This iterative design science approach enabled us to support the system's requirements and validation goal. The requirements, derived from theories and empirical observations, using the design science approach are (a) allow personalized setting of goals, reinforcements, and social connection, (b) generate reminders, (c) monitor adherence, (d) record medication-taking behavior and generate reports for healthcare professionals, (e) interact with healthcare professionals, and (f) implement positive and negative reinforcements.

The monitoring function of the system is facilitated by “smart monitoring”, which can measure patients' behavior patterns automatically over a long-term without disturbing their daily life by using health monitoring devices over patients (e.g., Apple watch), near pa tients (e.g., electronic pill container), and/or around patients (e.g., environmental sensors) [16]. Comparing to self-reported data, the data captured by these monitoring products can improve the accuracy of the system process.

The primary focus of this paper is medication non-adherence because of its significance, the fundamental idea of our design can also be applied to address other healthcare-related issues such as cancellation or missing appointments with physicians. Though the influencing factors are diferent, patients' prior visit history and demographic factors matter more in attending appointments [64], but the reinforcements can still assist in encouraging patients to make better decisions.

## 3.1. System process

Our designed system interacts with patients' medication-taking pattern in five steps to fulfill the above requirements. The five steps are as follows.

First, we need to set several parameters of the system, including desired MAR, reinforcement type (PR and/or NR) and whether PR should be fixed or increasing, and the number of doses a patient can miss without receiving NR. MAR goal could be set by the patient or the physician. Reinforcement type can be selected based on the type of medications, past medication behavior, the patient's current status, MAR goal, and level of dependence on apps and smartphone. Whether PR should be fixed or increasing could be based on patient's characteristics.

Second, we need to specify two time-windows, for the patient to take medications, to be set by a healthcare professional. The first timewindow covers the period during which the taken dose will fulfill its function, and the second time-window specifies the timing for a taken dose to not interfere with the efect of next on-time-taken dose. At the beginning of the first time-window, the system will send a reminder, if the patient takes the dose, no further reminder will be sent; if the patient doesn't, then another reminder will be sent at the beginning of second time-window. We design these two time-windows to reduce the probability of overdosing due to the patient's catch-up behavior for their skipped or delayed doses. Occasionally, this catch-up behavior is the side efects of reducing dose frequency [65]. If the patient doesn't take the dose after second time-window, the system will display a message suggesting the patient must not take any medication until the next reminder is received. The association between a patient's behavior and PR is as follows. If the patient takes the dose within the first time window, he/she will get full PR; if the patient takes the dose within the second time window, he/she will get reduced PR; if the patient doesn't, then he/she will get no PR. More parameters of time windows design and intervals between time windows will be discussed in the Evaluatior Section.

Third, we will only implement NR if the patient initializes the system as he/she would like to receive it. Two conditions are for NR (1) when the MAR drops below the expected MAR for medication to be efective and (2) when the patient has missed a certain number of doses consecutively. Healthcare professionals decide the limit for the number of possible consecutive-missing-doses. We will start by blocking the most used app (besides our app) in smartphone and move on to the second most used app and so on. However, every blocking action could be reversed if the patient takes subsequent doses to get the adherence rate to the desired MAR.

![](/api/attachments/YFW759AF/fulltext/images/cba83eda42129bda98d5cd4aab77a1208985dd99a6b1ec3b46faf3c5043489c8.jpg)  
Fig. 2. The process of carrot & stick intervention.

Fourth, if a patient's behavior reaches the limit, we will execute the extreme action, which is to block all applications (besides our app) but still allow the phone calls or text from family, friends, police as well as healthcare professionals.

Fifth, our application will provide per-dose, daily, weekly, and monthly adherence data to healthcare professional for analysis and any further adjustments.

The intervention process is shown in Fig. 2, with PR for taking doses during the two time-windows and blocking and unblocking of the most commonly used apps. The PR and NR cycle can also be utilized for other healthy behaviors including keeping the appointments, consuming healthy food, doing exercise, managing total calories and weight-loss goals instead of just meeting MAR goal.

## 3.2. System operation

Fig. 3 shows the mobile interface involving reminder, PR record, and NR record. The first interface represents how reminder will be shown. The medication name (Med ABC) will be displayed to show the due dose. The second interface shows PR (two stars) when the patient takes the dose in first time-window. The third interface shows PR (one star) when the patient takes the dose in second time-window. The fourth interface represents how NR will be displayed when critical dose is skipped. An app can be unblocked if the patient takes the next N doses to bring the MAR to the desired level. The first interface in Fig. 4 shows the message if the patient tries to access a blocked App Q. This message can be in smartphone's notification center or with every reminder. Further, as shown in second interface, consumption history is transmitted to a healthcare professional who can take suitable action.

An example of dose consumption and the intervention includes PR based on when the dose is taken (FW: first window and SW: second window) in Fig. 5. For the desired goal of 80%, when the patient misses a dose (the fifth of five doses), the MAR remains ≥80%. However, when the patient misses the next dose, MAR drops below 80% (67% if the patient misses the sixth dose) triggering the blocking of App Q (the most common App). The PR accumulates for future doses, and once the MA reaches 80% (8 out of 10 doses taken) again, the App Q is unblocked.

![](/api/attachments/YFW759AF/fulltext/images/dbea9e3c9ad6246f55c3cfe03ca1d016abdbf4cc746fdbada83a5c1da0f405e5.jpg)  
C&S: Carrot and Stick

Fig. 3. The intervention as a mobile app.  
![](/api/attachments/YFW759AF/fulltext/images/be278abe6acc996b6d0adaea4ff24c668905aa0d1b9505031fd317289a8c2ab3.jpg)  
Fig. 4. Some actions of the intervention.

## 3.3. Multiple medications case

Patients with chronic diseases or elderly patients may take multiple medications. If the overall MAR of medications matters to patients health, the PR could be based on achieving adherence larger or equal to the desired value for all medications, and NR when the achieved ad herence goes lower. Here, the implementation of PR and NR is similar to a single medication case, with the diference being the average MAR of multiple medications as the new MAR. An example of two medications, MD1 and MD2, along with 80% average desired MAR is shown in Fig. 6. If medications need diferent levels of adherence due to diferent weights in health outcomes, the PR can be diferent to achieve a higher adherence for more important medications. Also, patients are more prone to receive NR when they miss their higher MAR medication. An example where MD3 requires 90% MAR and MD4 requires 80% MAR is shown in Fig. 7. We choose two diferent PR, reward 3 for MD3 and reward 4 for MD4, to increase the probability of reaching diferent MAR. If a medication requires a high MAR (90% in the example), the app could easily be blocked because of a single missing dose and it will take a long time to reverse the efect. The patient should work with healthcare professionals for multi-medication plan based on medication types and the medication-taking history.

The proposed intervention is the first of its kind, which takes advantage of dependence on smartphones using the C&S approach. To avoid confusion between situations involving “intentional blocking” and “app malfunction,” our intervention displays a message to show that such app has been blocked and will be unblocked if the patient takes the next N doses at their due time (Figs. 3 and 4). The value of N is based on the target MAR. If the blocking is not working, the healthcare professional will be informed along with consumption information for a suitable intervention. One major challenge is to maintain novelty and long-term use of our intervention for diferent patients. Using theories, we discuss scenarios of the intervention application to show how the system targets a diferent group of patients and sustains usefulness with changes in patients' behavior and preference.

## 4. Scenarios

SCT illustrates that reinforcement, goal-setting, and social support are critical in modifying and maintaining an individual's behavior. Accordingly, we integrate three functionalities in our intervention: (1) positive and negative reinforcement, (2) goal-setting, and (3) social connection. According to Goal-setting Theory, the goal should be (1) set to create individual's commitment and (2) challenging enough without exceeding the individual's capability. Positive reinforcement may have a diminishing efect in maintaining the behavioral change. Thus, we discuss three scenario segments, based on the three designed functions and patients' characteristics, to show how intervention covers diferent patient types to support decision making and behavior change process (Table 2).

![](/api/attachments/YFW759AF/fulltext/images/e0cf611cede808fb91b8b604ab904ba502ce910bcc4760bf94766bed5d474001.jpg)  
Fig. 5. An example of the intervention.

![](/api/attachments/YFW759AF/fulltext/images/6eb31aa18e687f01030423c1b47d08d1e57d0c32e4939bc13e7598215baa1c2f.jpg)  
Fig. 6. An example of average MAR for multi-medication intervention.

![](/api/attachments/YFW759AF/fulltext/images/d4fb383ecd0650b8106419c01a22978f72187ea8371dd6986ab2b3c5643002f9.jpg)  
Fig. 7. An example of diferent MAR for multi-medication intervention.

## 4.1. Scenario segments

## 4.1.1. First scenario segment: positive and negative reinforcement

Positive reinforcement (PR) such as money, lottery, and voucher, are efective in increasing patient's adherence rate [26]. However, repeated PR would have a diminished efect in keeping some people motivated over time. Some individuals have diferent sensitivity to repeated PR. If the benefits of repeating the particular behavior can be internalized, the diminishing utility of repeated PR could be supple mented by increased health wellness.

Beside PR, individuals can also adopt or give up specific behavior to avoid negative reinforcement (NR). Sometimes, people avoid losses to acquiring equivalent gains (loss aversion) [66]. Since individual differences also exist in patients' sensitivity toward NR, multiple NR should be included in our scenario components. The sensitivity can be assessed using the sensitivity to punishment and sensitivity to reward questionnaire (SPSRQ) [67] with modifications in items to fit our design better.

## 4.1.2. Second scenario segment: goal-setting

It should not always be the physician who sets up the goal for the patient. Not only because the more empowered patients feel in their treatment decisions, the more likely they are motivated to adhere to their medication, but also based on it is sometimes the patients themselves who understand their behavior patterns better. The patients who have a deeper understanding of their capabilities and real-life dificulties than their physicians are more suitable to set their goals by themselves. While the patients who would only set their goal to the minimum possible level or those who would overestimate their capabilities to achieving their goals are more suitable to a physician-assigned goal.

Table 2  
Scenario components.

<table><tr><td>Segment</td><td>Scenario</td><td>Specific</td><td>Description</td></tr><tr><td rowspan="4">1</td><td>1</td><td>Fixed PR and no NR</td><td>In each period, the patient receives the same PR. The patient will not receive NR if he/she doesn&#x27;t achieve MAR goal.</td></tr><tr><td>2</td><td>Increasing PR and no NR</td><td>The patient will receive an increasing PR. Also, the patient will not receive NR if he/she doesn&#x27;t achieve MAR goal.</td></tr><tr><td>3</td><td>Fixed PR and fixed NR</td><td>In each intervention period, the patient will receive the same PR. Also, the patient will receive NR if he/she doesn&#x27;t achieve MAR goal.</td></tr><tr><td>4</td><td>Increasing PR and fixed NR</td><td>The patient will receive an increasing PR. The patient also receives NR if he/she doesn&#x27;t achieve MAR goal.</td></tr><tr><td rowspan="2">2</td><td>5</td><td>Self-set goal</td><td>Patient himself/herself will set his/her MA goal.</td></tr><tr><td>6</td><td>Physician-assigned goal</td><td>Patient&#x27;s MA goal will be set by the physician.</td></tr><tr><td rowspan="4">3</td><td>7</td><td>Disable social connection</td><td>The patient will not be able to share his/her reinforcement information with others.</td></tr><tr><td>8</td><td>Enable social connection, only sharing PR information</td><td>The patient will share his/her PR information with others.</td></tr><tr><td>9</td><td>Enable social connection, only sharing NR information</td><td>The patient will share his/her NR information with others.</td></tr><tr><td>10</td><td>Enable social connection, sharing both PR and NR information</td><td>The patient will share his/her PR and NR information with others.</td></tr></table>

Table 3  
Scenario comparison.

<table><tr><td>Scenario</td><td>Probability of quitting</td><td>Suitable patient type</td><td>Cost-effectiveness</td></tr><tr><td>1</td><td>Medium</td><td>Patients who have medium to high sensitivity to NR and have low sensitivity to PR change</td><td>High</td></tr><tr><td>2</td><td>Low</td><td>Patients who have medium to high sensitivity to NR and have medium to high sensitivity to PR change</td><td>Medium</td></tr><tr><td>3</td><td>High</td><td>Patients who have low sensitivity to NR and have low sensitivity to PR change</td><td>Medium</td></tr><tr><td>4</td><td>Medium</td><td>Patients who have low sensitivity to NR and have medium to high sensitivity to PR change</td><td>Low</td></tr><tr><td>5</td><td>N/A</td><td>Patients who evaluate their capabilities and difficulties precisely</td><td>High</td></tr><tr><td>6</td><td>N/A</td><td>Patients who cannot evaluate their capabilities and difficulties precisely</td><td>Low</td></tr><tr><td>7</td><td>Medium</td><td>Patients who would not like to share personal information with others</td><td>High</td></tr><tr><td>8</td><td>Low</td><td>Patients who would like to share their achievement with others</td><td>Medium</td></tr><tr><td>9</td><td>High</td><td>Patients who would like to have other people help regulate their behaviors</td><td>Medium</td></tr><tr><td>10</td><td>Medium</td><td>Patients who would like to share their daily life with others</td><td>Low</td></tr></table>

Note: comparison levels are within scenario segments.

## 4.1.3. Third scenario segment: social connection

The social support and reaction to an individual's behavior is an important determinant in the behavior change process. However, in cultural research, individual-level variances have been found in valuing others' opinions. For example, individualists value autonomy and self reliance [68], while collectivists change their behaviors by influence from others [69]. Patients in need of encouragement should share dif ferent reinforcement information from patients in need of regulation.

Indeed, these three segments of scenarios are not exclusive from each other. They cover diferent aspects to increase the intervention's efectiveness. One complete scenario of intervention application could include one or more segment's components. For example, a patient could set his own MA goal, receive a fixed reward for any dose he/she takes but no punishment for not reaching period's goal, and share only his/her reward information with others.

## 4.2. Within-segment scenarios comparison

We present scenarios comparison within each of the three segments as follows (Table 3):

## 4.2.1. Probability of quitting

For Segment 1 (scenario components 1 to 4), NR could cause negative emotions and is strongly associated with patients' dropping out behavior. However, if the PR is increasing, it is a stronger incentive for patients to keep participating. Thus, the patient who receives increasing PR and no NR has a low probability of quitting while the patient who receives fixed PR and fixed NR has a high likelihood of quitting. For Segment 2 (scenario components 5 and 6), we don't have enough evidence to compare the dificulty of self-set and physician-assigned goals, so we cannot compare the probability of quitting in this segment. For Segment 3 (scenario components 7 to 10), the adverse efects due to sharing only NR information (along with decreased self-eficacy) would increase the probability of quitting. If patients do not share information, they would not like to receive any judgments. So, the likelihood of quitting decreases compared to only sharing NR information. When patients only share PR information, the positive feedback they get further reduces the likelihood of quitting.

## 4.2.2. Suitable patient type

For Segment 1, NR should only be applied to patients with low sensitivity to it. Also, compared to patients with low sensitivity to PR change, patients with a medium to high sensitivity to PR change should receive an increasing PR overtime to neutralize the diminishing efect of PR. For Segment 2, the suitability of these two goal-setting types is based on the accuracy of evaluation of patients' ability and real-life dificulties. There should be a minimum MAR (e.g., 80%) that the self set goal needs to meet to prevent patients from setting their goals too low. For Segment 3, personality preference for social connection is the critical factor in deciding information sharing styles. Patients preferring a high level of autonomy and control are not suitable for sharing MA information because when they receive negative feedback they will drop out. If a patient is non-adherent to medication because he/she lacks self-regulation, sharing punishment information will be the right choice because there will be more people to help monitor and regulate his/her behavior. For some patients who don't want others to know any information as it would injure their self-images, only sharing PR information will help them receive social support. For patients who share moments in life to form connections, sharing both reward and punishment information is appropriate.

## 4.2.3. Cost-efectiveness

For Segment 1, implementing NR costs more than not implementing it. Providing increasing PR over time also costs more than providing fixed PR. For Segment 2, the physician-assigned goal costs more than a self-set goal because it involves more interaction and eforts from both the patient and the physician. For Segment 3, the cost of social connection increases with increasing shared information amount due to storage and maintenance cost.

## 4.3. Multiple medications cases comparison

Now, we compare multiple medications cases (a) multiple medications with average MAR and (b) multiple medications with diferent MARs. For the same average MAR, the situation is similar to the single medication case except that now the regimen complexity may cause a higher probability of quitting. However, the patient could also get multiple PR by following all medication prescriptions. Thus, the efect of PR counteracts the impact of complexity leading to little change in Table 3. When the patient has multiple medications with diferent MARs, both possibilities of quitting and cost-efectiveness of diferent scenarios are subject to change, especially when a prescription requires a rather high MAR. Comparing Figs. 4 and 6, the probability of blocking more than one app increases, and the duration to unblock specific app lasts longer with a medication requiring high MAR. The patient is more likely to quit because of these impacts even with multiple PR. System operation cost also increases because diferent PR needs to be set to encourage the patient to achieve diferent medication-based MARs. So, the cost-efectiveness also drops.

We discussed and analyzed three scenario segments and ten detailed components in this section. We also compared each component quali tatively in both single-medication and multiple-medication cases. We will evaluate and validate our designed system using the analytical model in the next section.

Table 4 Notations.

<table><tr><td colspan="2">Medication adherence</td></tr><tr><td> $N_P$ </td><td>The number of prescribed doses for the observed period.</td></tr><tr><td> $N_T$ </td><td>The number of doses taken by the patient over the observed period.</td></tr><tr><td> $N_{un-missing}$ </td><td>The number of doses missed unintentionally by the patient.</td></tr><tr><td> $N_{in-missing}$ </td><td>The number of doses missed intentionally by the patient.</td></tr><tr><td> $N_{st}$ </td><td>The number of doses the patient takes in the first time-window over the observed period.</td></tr><tr><td> $N_{nd}$ </td><td>The number of doses the patient takes in the second time-window over the observed period.</td></tr><tr><td> $R_{ex}$ </td><td>The expected medication adherence rate. This rate varies by disease and patient type.</td></tr><tr><td> $P_{Base}$ </td><td>The inherent average probability of the patient takes a dose of medication.</td></tr><tr><td> $P_{st}$ </td><td>The probability that the patient takes the dose during the first time-window.</td></tr><tr><td> $P_{nd}$ </td><td>The probability that the patient takes the dose during the second time window.</td></tr><tr><td colspan="2">Reminders</td></tr><tr><td> $T_{max}$ </td><td>The maximum interval time between two doses to remain medically effective and compliant.</td></tr><tr><td> $T_{min}$ </td><td>The minimum interval time between two doses for them to be compliant and safely consumed by the patient without causing any negative effects of overdosing.</td></tr><tr><td> $T_{i,bf}, T_{i+1,bf}$ </td><td>The beginning time of the first time-window of dose i, and dose i + 1, respectively.</td></tr><tr><td> $T_{i,bs}, T_{i+1,bs}$ </td><td>The beginning time of the second time-window of dose i, and dose i + 1, respectively.</td></tr><tr><td> $T_{i,es}, T_{i+1,es}$ </td><td>The ending time of the second time-window of dose i, and dose i + 1, respectively.</td></tr><tr><td> $T_{i,ef}, T_{i+1,ef}$ </td><td>The ending time of the first time-window of dose i, and dose i + 1, respectively.</td></tr><tr><td colspan="2">Reinforcements</td></tr><tr><td> $R_{st}$ </td><td>The constant PR for the patient when he/she takes the dose during the first time-window.</td></tr><tr><td> $R_{nd}$ </td><td>The constant PR for the patient when he/she takes the dose during the second time-window.</td></tr><tr><td>δ</td><td>The increase rate of first time-window reward over observed periods.</td></tr><tr><td>t</td><td>The number of observed periods.</td></tr><tr><td colspan="2">Social connection</td></tr><tr><td>S</td><td>The probability that the patient chooses to share personal MA information with other people.</td></tr><tr><td> $M_{sc}$ </td><td>The motivational factor the patient receives from social connections such as family support or better communication with healthcare professionals.</td></tr><tr><td colspan="2">Goal-setting</td></tr><tr><td> $M_G$ </td><td>The motivation that the patient has in reaching the goal.</td></tr><tr><td> $M_{FG}$ </td><td>The effect of feedback on the patient&#x27;s behavior during the process to reach the goal.</td></tr><tr><td colspan="2">Financial savings</td></tr><tr><td> $C_H$ </td><td>The total hospitalization cost during observed periods.</td></tr><tr><td> $L_{H}$ </td><td>The lost productivity per hospitalization during observed periods.</td></tr><tr><td> $N_H$ </td><td>The reduced number of hospitalizations during observed periods.</td></tr><tr><td> $C_{CS}$ </td><td>The cost of using the C&amp;S system during observed periods.</td></tr><tr><td> $C_{train}$ </td><td>The training cost to use the system.</td></tr><tr><td> $C_{NR}$ </td><td>The expense of negative reinforcement during observed periods.</td></tr></table>

## 5. Analytical modeling

Our designed intervention can be applied to diferent patients, preferring diferent levels of social connections, with varying sensitivities to either PR or NR, and with diverse goal-setting preference. These scenario segments can be adjusted based on the feedback of the patient's daily, weekly, and longer-term adherence patterns. We evaluate the performance of C&S by using analytical modeling. Analytical models have been used as formal proofs for a long time in Computer Science, Design Science, and Engineering because they can express complex relationships among many variables of interest. They also provide intermediate and immediate results, which can help to improve the design of artifacts.

As our core dependent variable, we only consider the percentage of prescribed medication taken by patients in this research as our calculated MAR (Medication Adherence Rate). We are aware that additional measurements of MA, such as longest uninterrupted period of MA (the time period that a patient takes the prescribed medication according to schedule without even missing a single dose) and time expired before all prescribed doses are taken (the time period passed until a patient actually take all prescribed doses), can be useful supplementary out come measures of our intervention [70]. Further, medication possession ratio (crude measure for counting how many days patients had access to medications at home), or patient recall (highly unreliable, especially for patients with cognitive challenges/busy lifestyle) have been tested in some studies. We choose to focus on MAR because of two reasons: 1) The treatment for chronic diseases requires relatively stable medica tion-taking behavior over long-term. Our defined MAR is the best representative of it. 2) Compare to other measurements, MAR is the most-used one in previous research. Even though we use analytical modeling, we want to align with empirical research for comparable outcomes.

## 5.1. Assumptions

Several assumptions were made to keep the analytical model reasonably accurate and can be relaxed in future to improve accuracy at additional complexity. Assumption 1 states that the patients are able to self-medicate as prescribed. Assumption 2 states that the two events of NR involving MAR dropping below the expected value and the patient missing a certain number of doses consecutively are independent of each other.

## 5.2. Validation of the model

## 5.2.1. Notations

The notations used in our models are in Table 4.

## 5.2.2. General medication adherence

The MAR over the observed period is given by

$$
M A R = \left(\frac {N _ {T}}{N _ {P}}\right) \times 100 \%
$$

$$
= (N _ {T} / (N _ {T} + (N _ {u n - m i s s i n g} + N _ {i n - m i s s i n g})\tag{1}
$$

The unintentionally missed doses are due to forgetfulness or carefulness. The intentionally missed doses are due to patient characteristics, treatment factors, or patient-provider issues. To reduce the first, we use two reminders that can lower the probability of overdose due to the patient's behavior to take doses at an inappropriate time to make up for their skipped or delayed doses.

![](/api/attachments/YFW759AF/fulltext/images/a3a2fcc26c4b643b618eac18ec73565181f7f5ba38b797caad32f00be8f8d4ef.jpg)  
Fig. 8. Time-windows design.

The gap between the start of first time-window and the end of the next dose's second time-window should not exceed the max-interdosetime for the medication to be efective. Thus,

$$
T _ {i + 1, e s} - T _ {i, b f} \leq T _ {m a x}\tag{2}
$$

The min-interdose-time which prevents the patients from over dosing is given by

$$
T _ {i + 1, b f} - T _ {i, e s} \geq T _ {m i n}\tag{3}
$$

The two time-windows, max-interdose-time and min-interdose-time are shown in Fig. 8.

## 5.2.3. Probability of reaching desired MAR without interventions

Based on the probability that the patient takes m doses among $N _ { P }$ without intervention (Eq. (A1) in Appendix A), the probability that the patient has MAR equal or more than expected MAR without intervention is the sum of probability that a patient takes $\lceil R _ { e x } N _ { P } \rceil$ doses or more and is given as

$$
P _ {w i t h o u t} = \sum_ {k = \lceil R _ {e x} N _ {P} \rceil} ^ {N _ {P}} \left(\frac {\prod_ {k} ^ {N _ {P}} P _ {B a s e} ^ {k} (1 - P _ {B a s e}) ^ {N _ {P} - k}}{\prod_ {i = 1} ^ {k} \mathrm{i} \times \prod_ {i = 1} ^ {N _ {P} - k} i}\right)\tag{4}
$$

5.2.4. Probability of reaching desired MAR with reminders and positive reinforcement

Studies on nonadherence indicate that forgetfulness is the main reason behind failing to take their medication (e.g., [71]). Reminders have been tested and validated to improve MA significantly in multiple studies. Since in our design, taking medication following reminders will also result in another type of intervention, PR, as well, we formulate the efects of these two intervention types together.

With PR, the overall probability that a patient takes one dose in two time-windows is

$$
P _ {R} = P _ {s t} + (1 - P _ {s t}) P _ {n d}\tag{5}
$$

We can derive the probability that the patient takes $N _ { s t }$ out of $N _ { P }$ doses within the first time-window (Eq. (A2) in Appendix $\mathrm { A } ) ,$ and then the probability that a patient takes total k doses among $N _ { P }$ doses within either time-windows (Eq. (A3) in Appendix A). Following, we can cal culate the probability that a patient has MAR equal or higher than expected MAR with reminders and PR as

P<sub>withR</sub>

$$
\begin{array}{l} = \sum_ {N _ {s t} = 1} ^ {N _ {P}} \left(\frac {\prod_ {i = 0} ^ {N _ {P}} i \times P _ {s t} ^ {N _ {s t}} (1 - P _ {s t}) ^ {N _ {P} - N _ {s t}}}{\prod_ {i = 1} ^ {N _ {s t}} i \times \prod_ {i = 1} ^ {N _ {P} - N _ {s t}} i}\right) \times \sum_ {N _ {n d} = m a x (| R e x N _ {P} | - N _ {s t}, 1)} ^ {N _ {P} - N _ {s t}} \left(\frac {\prod_ {i = 1} ^ {N _ {P} - N _ {s t}} i \times P _ {n d} ^ {N _ {n d}} (1 - P _ {n d}) ^ {N _ {P} - N _ {s t} - N _ {n d}}}{\prod_ {i = 1} ^ {N _ {n d}} i \times \prod_ {i = 1} ^ {N _ {P} - N _ {s t} - N _ {n d}} i}\right) \end{array}\tag{6}
$$

## 5.2.5. Probability of implementing negative reinforcement

NR would be implemented under two conditions. These are (1) when the patient's MAR drops below expected MAR and (2) when the patient has missed a certain number of consecutive doses.

To model the first condition, it is the opposite situation of the patient always taking at least $\lceil R _ { e x } N _ { P } \rceil$ doses within $N _ { P }$ doses. So using Eq. $^ { ( 6 ) , }$ the probability of first NR condition is

$$
P _ {N R 1} = 1 - P _ {w i t h R}\tag{7}
$$

Using Feller's [72] consecutive missing trials, the probability of second NR condition is:

$$
P _ {N R 2} \sim 1 - \frac {1 - P _ {R} x}{(N _ {m} + 1 - N _ {m} x) q} \times \frac {1}{x ^ {N _ {P} + 1}}\tag{8}
$$

where $N _ { m }$ is the number of consecutive missing doses, $P _ { R }$ comes from Eq. $( 5 ) , q = 1 - P _ { R } ,$ and x is the root near 1 of

$$
1 - \mathrm{x} + \mathrm{q} P _ {R} ^ {N _ {m}} x ^ {N _ {m} + 1} = 0\tag{9}
$$

## 5.2.6. Fixed and increasing positive reinforcement

RW is the amount of PR gained over the observed period. The fixed PR is given by

$$
R W _ {F} = R _ {s t} N _ {s t} + R _ {n d} N _ {n d}\tag{10}
$$

where $\mathrm { R } _ { \mathrm { s t } }$ is larger than $\mathrm { R } _ { \mathrm { n d } } .$ . The increasing PR is

$$
R W _ {I} = R _ {s t} (1 + \delta) ^ {(t - 1)} N _ {s t} + R _ {n d} N _ {n d} (t \geq 1)\tag{11}
$$

![](/api/attachments/YFW759AF/fulltext/images/a5ee9be4a5f64954bea48698345f52e8fa2b5067708052e421624f65ddcaae3e.jpg)  
Fig. 9. Probability of reaching expected MAR.

![](/api/attachments/YFW759AF/fulltext/images/1d0d4278cf490cfed1b5ec7209c98d24caa7cd67a1fcc8077e047ff668fdc5b8.jpg)  
Fig. 10. Diference in PR amount with fixed PR and increasing PR.

## 5.2.7. Social connection with others

Social connection with other people, especially with family mem bers, has shown to help the patient holding a more positive attitude toward medication. However, the patient is likely to prefer not to share MA information. When the patient chooses to connect with other people, the feedback he/she receives could be an additive factor to improve MA. Therefore:

$$
P _ {S C} = M i n ((P _ {B a s e} + S \bullet M _ {s c}), 1)\tag{12}
$$

## 5.2.8. Impact of goal-setting

Setting specific goals to achieve a task, in combination with performance feedback, results in higher performance than does no or a vague goal [33,34]. The desire to fulfill a goal and the feedback provided to the patients after the goal gets reached are both additive factors to improve MA, but not to exceed 100%. Therefore, the following expression can be developed:

$$
P _ {G} = \min ((P _ {B a s e} + M _ {G} \bullet M _ {F G}), 1)\tag{13}
$$

## 5.2.9. Savings due to improved MA

The savings due to improved MA can be expressed as

$$
S _ {s a v} = R W + (C _ {H} + L P _ {H}) \bullet N _ {H} - (C _ {C S} + C _ {t r a i n} + C _ {N R})\tag{14}
$$

![](/api/attachments/YFW759AF/fulltext/images/967c80e67a4bd486566feb3f7d5609af9caf06005f65f8eedb5e55679a413b93.jpg)  
Fig. 11. Diference in increasing PR amount with diferent $P _ { s t }$ and $P _ { n d } .$

Table 5  
The efectiveness of reminders and fixed PR.

<table><tr><td colspan="11"> $P_{nd}$ </td></tr><tr><td rowspan="10"> $P_{st}$ </td><td></td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>0.1</td><td>0.76</td><td>0.68</td><td>0.64</td><td>0.61</td><td>0.59</td><td>0.58</td><td>0.57</td><td>0.56</td><td>0.55</td></tr><tr><td>0.2</td><td>0.86</td><td>0.78</td><td>0.73</td><td>0.69</td><td>0.67</td><td>0.65</td><td>0.63</td><td>0.62</td><td>0.61</td></tr><tr><td>0.3</td><td>0.91</td><td>0.84</td><td>0.79</td><td>0.76</td><td>0.73</td><td>0.71</td><td>0.69</td><td>0.67</td><td>0.66</td></tr><tr><td>0.4</td><td>0.93</td><td>0.88</td><td>0.84</td><td>0.81</td><td>0.79</td><td>0.76</td><td>0.74</td><td>0.73</td><td>0.71</td></tr><tr><td>0.5</td><td>0.95</td><td>0.92</td><td>0.88</td><td>0.86</td><td>0.83</td><td>0.81</td><td>0.79</td><td>0.78</td><td>0.76</td></tr><tr><td>0.6</td><td>0.97</td><td>0.94</td><td>0.92</td><td>0.89</td><td>0.88</td><td>0.86</td><td>0.84</td><td>0.83</td><td>0.81</td></tr><tr><td>0.7</td><td>0.98</td><td>0.96</td><td>0.94</td><td>0.93</td><td>0.91</td><td>0.9</td><td>0.88</td><td>0.87</td><td>0.86</td></tr><tr><td>0.8</td><td>0.99</td><td>0.98</td><td>0.97</td><td>0.95</td><td>0.94</td><td>0.93</td><td>0.93</td><td>0.92</td><td>0.91</td></tr><tr><td>0.9</td><td>0.99</td><td>0.99</td><td>0.98</td><td>0.98</td><td>0.97</td><td>0.97</td><td>0.96</td><td>0.96</td><td>0.95</td></tr></table>

![](/api/attachments/YFW759AF/fulltext/images/90450203c35549c298bb1949e6366bc37e172c9d6b3a43ad42454659c493a54c.jpg)  
Fig. 12. Efectiveness of reminders and increasing PR.

## 6. Results and discussion

## 6.1. The impact of reminders and positive reinforcement

To evaluate the impact of reminders and PR, we utilize a prescription for 30 days with three doses/day. Thus the total doses are 90 and the expected MAR is set as 80%. The probability of the patient reaching expected MAR for diferent $P _ { B a s e } ,$ the average probability of the dose taking, $P _ { s t }$ and $P _ { n d }$ are shown in Fig. 9. The line with $P _ { n d } = 0$ represents the efect of diferent level of $P _ { B a s e } .$ . Without reminders and PR, higher is the probability dose taking, more likely he/she satisfies the expected MAR. However, even when $P _ { B a s e }$ is high (e.g. $P _ { B a s e } = 0 . 8 )$ , the probability that the patient reaches expected MAR is relatively low (e.g. < 60%). Also, with low $P _ { B a s e }$ (e.g. 0.2–0.4), it is almost impossible to meet the expect MAR. The situation is changed by including reminders and PR as interventions. Even if the first reminder doesn't change the patient's behavior, or $P _ { s t }$ is the same as $P _ { B a s e } ,$ , a low $P _ { n d }$ (e.g., $P _ { n d } = 0 . 2 )$ could still improve the probability of reaching expected MAR significantly, from < 60% to higher than 85%. If the first reminder and associating PR could lead to a small increase (e.g., 0.1, from 0.8 to 0.9), the probability of the patient reaching expected MAR will jump from $< 6 0 \%$ to almost 100%.

![](/api/attachments/YFW759AF/fulltext/images/cae4e8120f284acf99537729229dcd6ec92aa2c13026a2466fdc5054988094dd.jpg)  
Fig. 13. The probability of receiving NR due to MAR lower than expected

![](/api/attachments/YFW759AF/fulltext/images/cf7aac34e6e56a895939b4b29fdd1f8e634dd271efe4a92087f542dba933bba5.jpg)  
Fig. 14. The probability of receiving NR due to consecutive dose missing.

## 6.2. Efectiveness of reminders and positive reinforcement

We use \$1 reward (cash, voucher, lottery or other types) as the financial value of $\mathrm { R } _ { \mathrm { s t } }$ and \$0.5 for $\mathbf { R } _ { \mathbf { n d } } .$ The reminders can be done in expensively on mobile phones. In Fig. 10, we assume the increasing rate of reward is 8% $( \delta = 0 . 0 8 ) _ { : }$ , and $P _ { s t }$ and $P _ { n d }$ are both 0.5. The figure shows rewards for taking each dose across twelve time periods. Fig. 11 shows the rewards for taking each dose with the same increasing rate $( \delta = 0 . 0 8 )$ but diferent $P _ { s t }$ and $P _ { n d } .$ Increasing reward 1 captures the rewards based on $P _ { s t } = 0 . 5 , P _ { n d } = 0 . 5 ,$ , increasing reward 2 captures rewards based on $P _ { s t } = 0 . 7 , P _ { n d } = 0 . 5$ , and increasing reward 3 captures rewards based on $P _ { s t } = 0 . 5 , P _ { n d } = 0 . 7$ . It is clear that $P _ { s t }$ plays a bigger role than $P _ { n d }$ if the patient wants to get a higher reward in increasing PR scenarios. The efectiveness of a fixed PR is shown in Table 5. The intervention reaches the highest efectiveness (0.99) when the chance of taking the medication dose in the first time-window is high (0.8 or 0.9) while the probability of taking the medication dose in second timewindow is low (0.1 or 0.2). Efectiveness decreases with decreasing first time-window probability and increasing second time-window probability. The efectiveness of increasing PR over time with diferent $P _ { s t }$ and $P _ { n d }$ is shown in $\mathrm { F i g }$ . 12. The efectiveness of PR decreases over time since PR has to increase to keep the same $P _ { s t }$ and $P _ { n d } .$ Comparing line 1 and line $^ { 3 , }$ with the same $P _ { s t , }$ the efectiveness of PR which induces higher $P _ { n d }$ would have a slower decrease. Similarly, comparing line 1 and line $^ { 2 , }$ with the same $P _ { n d , \quad }$ the efectiveness of PR which induce higher $P _ { s t }$ would have a slower decrease.

Table 6  
Savings per patient/month with interventions.

<table><tr><td> $C_{H} + LP_{H}$ </td><td> $N_{H}$ </td><td> $C_{CS} + C_{train}$ </td><td> $C_{NR}$ </td><td>RW</td><td> $T_{sav}$ </td></tr><tr><td rowspan="2">$500</td><td rowspan="2">1</td><td rowspan="2">$100</td><td rowspan="2">$2</td><td>$35.5</td><td>$433.5</td></tr><tr><td>$89</td><td>$487</td></tr><tr><td rowspan="2">$500</td><td rowspan="2">1</td><td rowspan="2">$300</td><td rowspan="2">$2</td><td>$35.5</td><td>$233.5</td></tr><tr><td>$89</td><td>$287</td></tr><tr><td rowspan="2">$500</td><td rowspan="2">1</td><td rowspan="2">$100</td><td rowspan="2">$20</td><td>$31</td><td>$411</td></tr><tr><td>$80</td><td>$460</td></tr><tr><td rowspan="2">$500</td><td rowspan="2">1</td><td rowspan="2">$300</td><td rowspan="2">$20</td><td>$31</td><td>$211</td></tr><tr><td>$80</td><td>$260</td></tr></table>

## 6.3. The efectiveness of negative reinforcement

Now, we evaluate the two NR implementation. When the patient's MAR drops below the expected MAR, the NR receiving probability is shown in Fig. 13. With expected MAR varying from 0.8 to 0.95, the patient needs a high $\mathbf { P _ { R } } ,$ probability of taking a dose in two time-windows with $\mathrm { P R } ,$ to avoid receiving NR. If expected MAR is 0.8, the patient needs $\mathrm { P _ { R } } = 0 . 8$ to have the mobile app blocking < 45%. When the patient misses several consecutive doses, the probability of receiving NR is shown in Fig. 14. With diferent limits of consecutive missing doses, the probability of the patient receiving NR varies. For example, the patient would have a much lower $\mathrm { { P _ { R } } , }$ , 0.37 in four consecutive missing cases to avoid being disconnected from the favorite app, than the needed $\mathrm { P _ { R } } , 0 . 7$ for the two consecutive missing cases.

## 6.4. Savings from reducing hospitalization

The total savings due to the composite interventions are shown in Table 6. We transfer the efect of negative reinforcement into a financial value as the losses can be twice as powerful as the gains psychologically [73]. The loss value of each blocking app is set to be \$2, twice as $\mathrm { R } _ { \mathrm { s t } } .$ The extreme negative reinforcement involves blocking ten apps per month. The savings are significant even for small reduction in hospitalization rate and are higher for longer periods and lower hospitalization rates.

From the above model and results, the following observations can be made:

• The two reminders and PR can increase the probability of achieving the expected MAR.

• Reminders and fixed PR intervention can be highly efective even when the patient's probability of taking the dose in the first timewindow is moderately low.

The PR should be adjusted over time to compensate for the dimin ishing efects.

If the patient wants to avoid NR, he/she must maintain a high probability of taking doses. This overall probability is higher than the outcome increased by only delivering reminders and PR, especially when the expected MAR is high, or the limit for consecutivemissing-dose is small.

The composite intervention performs better than reminders and PR or only NR.

Healthcare savings are significant and even more with higher hos pitalization cost.

## 7. Conclusions and future work

Most research in medication adherence has been on unintentional non-adherence, where patients forget to take their medications on time. We present, evaluate, and validate a novel mobile health intervention, Carrot & Stick (C&S), to support patients' medication decisions and to reinforce behavior changes for both unintentional as well as intentional non-adherence. Therefore, our design of C&S is innovative in three ways: 1) addressing intentional non-adherence by integrating PR and NR with previously validated reminder and social connection elements, 2) using theories for design, which increases the reliability of results using analytical modeling, and, 3) developing ten scenarios for the intervention, identifying suitable patient types, and addressing cost-effectiveness as part of decision support. Additionally, the use of two time-windows leads to avoidance of unintentional-missing-doses while the specified time intervals prevent the patient from overdosing. Even a slight increase in the probability that the patient takes a dose in either time-windows would improve the adherence outcome.

From analytical modeling, the probability to achieve expected MA is significantly increased after the intervention. Even reminders and PR alone can be efective in promoting MA, but NR can still assist. Patients adopt better medication-taking habit when they engage to avoid NR compared to the situation when they only pursue PR. Also, healthcare savings by higher MA are significant even over a short period.

We note several limitations of the present study. First, we evaluated the designed intervention using analytical modeling and not by empirical data. Even though our models and results are reliable and validated, future work can collect empirical data to evaluate the design. Second, we selected the average MA as our primary outcome measurement. This has its own weakness in reflecting the patterns of medication intake decision, an important factor afecting medications eficacy. Future work can utilize alternative measurements, including the uninterrupted period of adherence and efective medication ad herence, to examine C&S. The third limitation relates to application scenarios. We compare those scenarios within segments in this paper, while work can be done to perform comparison across diferent segments.

Our work can lead to the implementation of diferent intervention types and their combinations. The duration of PR and NR for creating permanent behavioral change for MA can be studied for diferent patients. The future work can also address multiple diferent types of NR; development of DSS for patients, caregivers, and healthcare professionals; and, integration of other m-health interventions for implementing and evaluating personalized solutions.

## Appendix A

1. The probability that the patient takes m doses among $N _ { P }$ without intervention

$$
P _ {O r i} = \frac {\prod_ {m = 1} ^ {N _ {P}} P _ {B a s e} ^ {m} (1 - P _ {B a s e}) ^ {N _ {P} - m}}{\prod_ {1} ^ {m} m \times \prod_ {1} ^ {N _ {P} - m} m}\tag{A1}
$$

2. With reminders and positive reinforcement, the probability that the patient takes $N _ { s t }$ out of $N _ { P }$ doses within the first time-window is

$$
P _ {F} = \frac {\prod_ {i = 1} ^ {N _ {P}} i \times P _ {s t} ^ {N _ {s t}} (1 - P _ {s t}) ^ {N _ {P} - N _ {s t}}}{\prod_ {i = 1} ^ {N _ {s t}} i \times \prod_ {i = 1} ^ {N _ {P} - N _ {s t}} i}\tag{A2}
$$

3. The probability that a patient takes total k doses among $N _ { P }$ doses within either time-windows as

$$
P _ {n e w} = \frac {\prod_ {i = 1} ^ {N p} i \times P _ {s t} ^ {N _ {s t}} (1 - P _ {s t}) ^ {N p - N _ {s t}}}{\prod_ {i = 1} ^ {N _ {s t}} i \times \prod_ {i = 1} ^ {N p - N _ {s t}} i} \times \frac {\prod_ {i = 1} ^ {N p - N _ {s t}} i \times P _ {n d} ^ {k - N _ {s t}} (1 - P _ {n d}) ^ {N p - k}}{\prod_ {i = 1} ^ {k - N _ {s t}} i \times \prod_ {i = 1} ^ {N p - k} i}\tag{A3}
$$

## References

[1] R.L. Kravitz, J. Melnikow, Medical adherence research: time for a change in di rection? Med, Care 42 (2004) 197–199.

[2] M.T. Brown, J.K. Bussell, Medication Adherence: WHO Cares?, Mayo Clinic Proceedings. Elsevier. 2011, pp. 304–314.

[3] S.C. Smith, E.J. Benjamin, R.O. Bonow, L.T. Braun, M.A. Creager, B.A. Franklin, R.J. Gibbons, S.M. Grundy, L.F. Hiratzka, D.W. Jones, AHA/ACCF secondary prevention and risk reduction therapy for patients with coronary and other atherosclerotic vascular disease: a guideline from the American Heart Association and American College of Cardiology Foundation. Circulation 124 (2011) 2458–2473.

[4] E.-L. Glader, M. Sjölander, M. Eriksson, M. Lundberg, Persistent use of secondary preventive drugs declines rapidly during the first 2 years after stroke, Stroke 41 (2010) 397–401.

[5] J. Thakkar. R. Kurup. T.-L. Laba, K. Santo, A. Thiagalingam, A. Rodgers M. Woodward. J. Redfern. C.K. Chow, Mobile telephone text messaging for medication adherence in chronic disease: a meta-analysis, JAMA Intern. Med. 176 (2016) 340–349.

[7] S.A. Eisen, D.K. Miller, R.S. Woodward, E. Spitznagel, T.R. Przybeck, The effect of prescribed daily dose frequency on patient medication compliance, Arch. Intern. Med. 150 (1990) 1881–1884.

[8] A.H. Paes, A. Bakker, C.J. Soe-Agnie, Impact of dosage frequency on patient com pliance, Diabetes Care 20 (1997) 1512–1517

[9] A. Seltzer, I. Roncari, P.E. Garfinkel, Efect of patient education on medication compliance, Can. J. Psychiatry/La Rev. Can. Psychiatr. 25 (8) (1980) 638–645.

[10] P. Beardon, M. McGilchrist, A. McKendrick, D. McDevitt, T. MacDonald, Primary non-compliance with prescribed medication in primary care, Bmj 307 (1993) 846–848.

[11] X. Ren, L. Kazis, A. Lee, H. Zhang, D. Miller, Identifying patient and physician characteristics that afect compliance with antihypertensive medications, J. Clin. Pharm. Ther. 27 (2002) 47–56.

[12] R. Horne, J. Weinman, N. Barber, R. Elliott, M. Morgan, A. Cribb, I. Kellar, Concordance. Adherence and Compliance in Medicine Taking. 2005 NCCSDO. London, 2005, pp. 40–46.

[13] M.R. DiMatteo, H.S. Lepper, T.W. Croghan, Depression is a risk factor for noncompliance with medical treatment: meta-analysis of the effects of anxiety and depression on patient adherence, Arch. Intern. Med. 160 (2000) 2101–2107.

[14] M.R. DiMatteo, Social support and patient adherence to medical treatment: a meta analysis, Health Psychol. 23 (2004) 207.

[15] U. Varshney, Pervasive Healthcare Computing: EMR/EHR. Wireless and Health Monitoring, Springer Science & Business Media, 2009.

[16] U. Varshney. Smart medication management system and multiple interventions fot

medication adherence, Decis. Support. Syst. 55 (2013) 538–551.

[17] H.P. McDonald. A.X. Garg, R.B. Haynes, Interventions to enhance patient adherence to medication prescriptions: scientific review, Jama 288 (2002) 2868–2879

[18] U. Varshney, Mobile health: four emerging themes of research, Decis. Support, Syst 66 (2014) 20–35.

[19] J. Barjis, G. Kolfschoten, J. Maritz, A sustainable and afordable support system for rural healthcare delivery, Decis. Support. Syst. 56 (2013) 223–233.

[20] L.G. Park, J. Howie-Esquivel, M.A. Whooley, K. Dracup, Psychosocial factors and medication adherence among patients with coronary heart disease: a text messaging intervention Eur. J. Cardiovasc, Nurs. 14 (2015) 264–273

[21] A. Mertens, S. Becker, S. Theis, P. Rasche, M. Wille, C. Bröhl, L. Finken, C. Schlick, Mobile Technology Improves Therapy-Adherence Rates in Elderly Patients Undergoing Rehabilitation—A Crossover Design Study, Advances in Human Factors and Ergonomics in Healthcare, Springer, Cham, 2017, pp. 295–308

[22] Z.W. Yu, Y.J. Liang, B. Guo, X.S. Zhou, H.B. Ni, Facilitating medication adherence in elderly care using ubiquitous sensors and mobile social networks, Comput. Commun, 65 (2015) 1–9

[23] K. Myoungsuk, Efects of customized long-message service and phone-based healthcoaching on elderly people with hypertension, Iran. J. Public Health 48 (2019) 655.

[24] P.G. Barnett, J.L. Sorensen, W. Wong, N.A. Haug, S.M. Hall, Efect of incentives for medication adherence on health care use and costs in methadone patients with HIV Drug Alcohol Depend, 100 (2009) 115–121.

[25] B.A. Moore, M.I. Rosen, Y. Wang, J. Shen, K. Ablondi, A. Sullivan, M. Guerrero, L. Siqueiros, E.S. Daar, H. Liu, A remotely-delivered CBT and contingency management therapy for substance using people with HIV, AIDS Behav. 19 (2015) 156–162.

[26] A.P. Sen, T.B. Sewell, E.B. Riley, B. Stearman, S.L. Bellamy, M.F. Hu, Y. Tao, J. Zhu, J.D. Park, G. Loewenstein. Financial incentives for home-based health monitoring: a randomized controlled trial. J. Gen. Intern. Med. 29 (2014) 770–777

[27] A. Bandura, Social Foundations of Thought and Action: A Social Cognitive Theory, Prentice-Hall Inc Fnglewood Cliffs NJ US 1986

[28] A. Bandura, Health promotion by social cognitive means, Health Educ. Behay, 31 (2004) 143-164.

[29] S. Kripalani, X. Yao, R.B. Haynes, Interventions to enhance medication adherence in chronic medical conditions: a systematic review, Arch. Intern. Med. 167 (2007) 540-549.

[30] A. DeFulio, K. Silverman, The use of incentives to reinforce medication adherence, Prev. Med. 55 (2012) S86–S94

[31] L.N. Gray, I. Tallman, Theories of choice: contingent reward and punishment ap. plications, Soc. Psychol. O. (1987) 16–23.

[33] G.P. Latham, E.A. Locke, Self-regulation through goal setting, Organ. Behav. Hum. Decis Process, 50 (1991) 212–247

[34] A.J. Mento, R.P. Steel, R.J. Karren, A meta-analytic study of the efects of goa

setting on task performance: 1966–1984, Organ. Behav. Hum. Decis. Process. 39 (1987) 52–83.

[35] D. Cervone, N. Jiwani, R. Wood, Goal setting and the diferential influence of self regulatory processes on complex decision-making performance, J. Pers. Soc. Psychol. 61 (1991) 257.

[36] B. Alexy, Goal setting and health risk reduction, Nurs. Res. 34 (1985) 283–288

[37] B.A. Boyce, V.K. Wayda, The efects of assigned and self-set goals on task perfor mance, Journal of Sport and Exercise Psychology 16 (1994) 258–269.

[38] A. Tesser, J. Campbell, M. Smith, Friendship choice and performance: self-evaluation maintenance in children, J. Pers. Soc. Psychol. 46 (1984) 561.

[39] G.C. Homans, Social behavior as exchange, Am. J. Sociol. 63 (1958) 597–606.

[40] S.T. Fiske, D.T. Gilbert, G. Lindzey, Handbook of Social Psychology, John Wiley & Sons, 2010.

[41] G.C. Homans, Social Behavior: Its Elementary Forms, Harcourt, Brace and World, New York. 1974.

[42] K. Bobrow, A.J. Farmer, D. Springer, M. Shanyinde, L.-M. Yu, T. Brennan, B. Rayner, M. Namane, K. Steyn, L. Tarassenko, Mobile phone text messages to support treatment adherence in adults with high blood pressure (StAR): a singleblind. randomized trial. Circulation (2016) (CIRCULATIONAHA. 115.017530).

[43] R.E. Sarabi, F. Sadoughi, R.J. Orak, K. Bahaadinbeigy, The efectiveness of mobile phone text messaging in improving medication adherence for patients with chroni diseases: a systematic review. Iran Red Crescent Med J 18 (2016).

[44] A. Mertens, C. Brandl, T. Miron-Shatz, C. Schlick, T. Neumann, A. Kribben, S. Meister, C.J. Diamantidis, U.-V. Albrecht, P. Horn, A mobile application improve therapv-adherence rates in elderly patients undergoing rehabilitation: a crossover design study comparing documentation via iPad with paper-based control. Medicine 95 (2016).

[45] E.M. Contreras, O.V. GarcÍa, N.M. Claros, V.G. Guillén, M.d.l.F.v. Wichmann, J.J.C. Martínez, R. Fernández, Eficacy of telephone and mail intervention in patient compliance with antihypertensive drugs in hypertension. ETECUM-HTA study, Blood Press. 14 (2005) 151–158.

[46] M.B. KC, P.J. Murray, Cell phone short messaging service (SMS) for HIV/AIDS in South Africa: a literature review, Studies in Health Technology and Informatics 160 (2010) 530–534.

[47] J. Chandler, L. Sox, K. Kellam, L. Feder, L. Nemeth, F. Treiber, Impact of a culturally tailored mHealth medication regimen self-management program upon blood pressure among hypertensive Hispanic adults, Int. J. Environ. Res. Public Health 16 (2019) 1226.

[48] H. Brath. J. Morak. T. Kastenbauer. R. Modre-Osprian. H. Strohner-Kastenbauer. M. Schwarz. W. Kort, G. Schreier, Mobile health (mHealth) based medication adherence measurement - a pilot trial using electronic blisters in diabetes patients, Br. J. Clin. Pharmacol. 76 (2013) 47–55.

[49] I. Maglogiannis, G. Spyroglou, C. Panagopoulos, M. Mazonaki, P. Tsanakas, Mobile reminder system for furthering patient adherence utilizing commodity smartwatch and android devices, Wireless Mobile Communication and Healthcare (Mobihealth), 2014 EAI 4th International Conference on, 2014, pp. 124–127.

[50] A. Ojo, S. Chatterjee, H.W. Neighbors, G.A. Piatt, S. Moulik, B.D. Neighbors, J. Abelson, C. Krenz, D. Jones, OH-BUDDY: Mobile phone texting based intervention for diabetes and oral health management, system sciences (HICSS), 2015 48th Hawaii International Conference on, 2015, pp. 803–813.

[51] D. Onime, J. Wood, J. Finkelstein, Cognitive evaluation of a mobile HIV tele management system utilizing multiple health communication channels. Point-of-Care Healthcare Technologies (PHT). 2013 IEEE. 2013. pp. 204–207.

[52] E. Márquez Contreras, S. Márquez Rivero. E. Rodríguez García, L. López-García-Ramos, J. Carlos Pastoriza Vilas, A. Baldonedo Suárez, C. Gracia Diez, V. Gil Guillén, N. Martell Claros, C.G.o.S.S.o. hypertension, specific hypertension smartphone application to improve medication adherence in hypertension: a clusterrandomized trial, Curr, Med, Res, Opin, 35 (2019) 167–173.

[53] N. Andre, R. Wibawanti, B.B. Siswanto, Mobile phone-based intervention in hy pertension management, Int. J. Hypertens. 2019 (2019).

[54] P.F. Cook, J.M. Carrington, S.J. Schmiege, W. Starr, B. Reeder, A counselor in your pocket: feasibility of mobile health tailored messages to support HIV medication adherence, Patient Preference and Adherence 9 (2015) 1353–1366.

[55] N. Singh, U. Varshney. Patterns of effective medication adherence: The role of wireless interventions, Wireless Telecommunications Symposium (WTS), 2014 2014, pp. 1–10.

[56] J.W. McGillicuddy, D.J. Taber, M. Mueller, S. Patel, P.K. Baliga, K.D. Chavin, L. Sox, A.P. Faye, B.M. Brunner-Jackson, F.A. Treiber, Sustainability of improvements in

medication adherence through a mobile health intervention, Prog. Transplant. 25 (2015) 217–223.

[57] J. Morak, M. Schwarz, D. Hayn, G. Schreier, Feasibility of mHealth and near field communication technology based medication adherence monitoring, Engineering in Medicine and Biology Society (EMBC), 2012 Annual International Conference of the IEEE, 2012, pp. 272–275.

[58] S. Sneha, U. Varshney, A framework for enabling patient monitoring via mobile ad hoc network, Decis. Support. Syst. 55 (2013) 218–234.

[60] V.K. Vaishnavi, W. Kuechler, Design Science Research Methods and Patterns: Innovating Information and Communication Technology, Crc Press, 2015.

[61] L. Wu, J.-Y. Li, C.-Y. Fu, The adoption of mobile healthcare by hospital’s professionals: an integrative perspective, Decis. Support. Syst. 51 (2011) 587–596.

[62] T.T. Moores, Towards an integrated model of IT acceptance in healthcare, Decis. Support. Syst. 53 (2012) 507–516.

[63] M.P. Johnson, K. Zheng, R. Padman, Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system, Decis. Support. Syst. 57 (2014) 444–453.

[64] J.B. Norris, C. Kumar, S. Chand, H. Moskowitz, S.A. Shade, D.R. Willis, An empirical investigation into factors afecting patient cancellations and no-shows at outpatient clinics, Decis. Support. Syst. 57 (2014) 428–443.

[65] A.J. Claxton, J. Cramer, C. Pierce, A systematic review of the associations between dose regimens and medication compliance, Clin. Ther. 23 (2001) 1296–1310.

[66] D. Kahneman, A. Tversky, Choices, values, and frames, Handbook of the Fundamental of Financial Decision Making: Part I World Scientific, 2013, pp. 269-278.

[67] R. Torrubia, C. Avila, J. Moltó, X. Caseras, The Sensitivity to Punishment and Sensitivity to Reward Questionnaire (SPSRQ) as a measure of Gray's anxiety and impulsivity dimensions, Personal. Individ. Difer. 31 (2001) 837–862.

[68] H.C. Triandis, Individualism-collectivism and personality, J. Pers. 69 (2001) 907–924.

[69] R.B. Cialdini, W. Wosinska, D.W. Barrett, J. Butner, M. Gornik-Durose, Compliance with a request in two cultures: the diferential influence of social proof and commitment/consistency on collectivists and individualists, Personal. Soc. Psychol. Bull. 25 (1999) 1242–1253.

[70] E.L. Noordraven, C.H. Audier, A.B. Staring, A.I. Wierdsma, P. Blanken, B.E. van der Hoorn, L. Hakkaart-van Roijen, C.L. Mulder, Money for medication: a randomized controlled study on the efectiveness of financial incentives to improve medication adherence in patients with psychotic disorders, BMC Psychiatry 14 (2014) 343.

[71] R. Khatib, J.-D. Schwalm, S. Yusuf, R.B. Haynes, M. McKee, M. Khan, R. Nieuwlaat, Patient and healthcare provider barriers to hypertension awareness, treatment and follow up: a systematic review and meta-analysis of qualitative and quantitative studies, PLoS One 9 (2014) e84238.

[72] W. Feller, An Introduction to Probability Theory and its Applications, Wiley New York, 1968.

[73] A. Tversky, D. Kahneman, Advances in prospect theory: cumulative representation of uncertainty, J. Risk Uncertain. 5 (1992) 297–323.

Xinying Liu is currently a PhD student at Georgia State University and is expected to graduate in 2020. She received an MS in MIS from the University of Maryland College Park in 2013 and a BS from Zhongnan University of Economics and Law in 2012. Amber is interested in mobile health, medication adherence and technical and behavioral inter ventions. She has published several papers in major conferences and has also reviewed for major journals.

Upkar Varshney is an Associate Professor of Computer Information Systems at Georgia State University. He has authored numerous papers in mobile health, mobile commerce and wireless networks and has been widely cited. He is the author of Pervasive Healthcare Computing: EMR/EHR, Wireless and Health Monitoring (2009, 2010, and 2011). He has received several teaching awards at GSU. Upkar has presented over fifty tutorials workshops, and a few keynotes at major wireless, computing, and information systems conferences. He has also received grants exceeding \$500K from funding agencies including the National Science Foundation. Upkar is the founding chair of International Pervasive Health conference and was the program chair for AMCIS 2009. He has served or is serving as an editor/guest editor for several major journals including IEEE Transactions on IT in Biomedicine, ACM/Springer Mobile Networks (MONET), Decision Support Systems (DSS), and Communications of the AIS (CAIS) among others. He has been a senior editor for Decision Support Systems and IEEE Computer.
