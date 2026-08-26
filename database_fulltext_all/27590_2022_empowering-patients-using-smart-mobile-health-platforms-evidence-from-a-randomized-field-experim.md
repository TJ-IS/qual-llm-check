---
otero_id: 27590
otero_key: "76D8ZPZM"
title: "Empowering Patients Using Smart Mobile Health Platforms: Evidence From a Randomized Field Experiment"
authors: "Anindya Ghose; Xitong Guo; Beibei Li; Yuanyuan Dang"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16201"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EMPOWERING PATIENTS USING SMART MOBILE HEALTH PLATFORMS: EVIDENCE FROM A RANDOMIZED FIELD EXPERIMENT<sup>1</sup>

Anindya Ghose Stern School of Business, New York University, 44 West 4<sup>th</sup> Street, New York, NY 10012 U.S.A. {aghose@stern.nyu.edu}

Xitong Guo School of Management, Harbin Institute of Technology, 2 Yikuang Road, W., Nangang District, Harbin, Heilongjiang CHINA {xitongguo@gmail.com}

Beibei Li Heinz College, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, PA 15213 U.S.A. {beibeili@andrew.cmu.edu}

Yuanyuan Dang School of Business Administration, South China University of Technology, 381 Wushan Road, Tianhe District, Guangzhou, Guangdong CHINA {dyy777@scut.edu.cn}

With today’s technological advancements, mobile phones and wearable devices have become extensions of an increasingly diffused and smart digital infrastructure. In this paper, we examine mobile health (mHealth) platforms and their health and economic impacts on the outcomes of chronic disease patients. To do so, we partnered with a major mHealth firm that provides one of the largest mobile health app platforms in Asia specializing in diabetes care. We designed and implemented a randomized field experiment based on detailed patient health activities (e.g., steps, exercises, sleep, food intake) and blood glucose values from 1,070 diabetes patients over several months. Our main findings show that the adoption of the mHealth app leads to an improvement in health behavior, which in turn leads to both short term metrics (such as reduction in patients’ blood glucose and glycated hemoglobin levels) and longer-term metrics (such as hospital visits and medica expenses). Patients who adopted the mHealth app undertook higher levels of exercise, consumed healthier food with lower calories, walked more steps and slept for longer times on a daily basis. They also were more likely to substitute offline visits with telehealth. A comparison of mobile versus PC-enabled versions of the same app demonstrates that the mobile version has a stronger effect than PC version in helping patients make these behavioral modifications with respect to diet, exercise, and lifestyle, which ultimately leads to an improvement in their healthcare outcomes. We also compared outcomes when the platform facilitates personalized health reminders to patients vis-à-vis generic (non-personalized) reminders. Surprisingly, we found that personalized mobile messages with patient-specific guidance can have an inadvertent (smaller) effect on patient app engagement and lifestyle changes, leading to a lower health improvement. However, they are more like to encourage a substitution of offline visits by telehealth. Overall, our findings indicate the massive potential of mHealth technologies and platform design in achieving better healthcare outcomes.

Keywords: mHealth, mobile app, healthcare platform, chronic disease, diabetes, personalization, patient self management

## Introduction

Facilitated by emerging smart mobile health (mHealth) technologies, the healthcare ecosystem has been undergoing a disruptive, digital transformation in transitioning from reactive care to proactive and preventive care that can potentially be administered more cost-effectively. As defined by Estrin and Sim (2010), mHealth is the combination of mobile computing, medical sensor, and communications technologies used for healthcare services, including chronic-disease management and wellness. mHealth includes medical applications that may run on smartphones, tablets, sensors that track vital signs and health activities, and cloud-based computing systems for collecting health data. Indeed, mHealth technologies have demonstrated tremendous potential in shaping the healthcare industry toward a new era of evidence-based medicine and “Quantified Self” (QS)—individuals engaged in the selftracking of biological, physical, behavioral, and environmental information (e.g., Manyika et al. 2013). The global mHealth market will reach \$49 billion by 2020, growing at a rate of more than 47% between 2013 and 2020.<sup>2</sup>

Given the importance of health behaviors to well-being, health outcomes, and disease processes, mHealth technologies have great potential in facilitating patient life style and behavior modification through patient education, improved autonomous self-regulation and perceived competence. The accessibility, convenience, and ubiquity inherent to mobile devices can help patients easily upload information on a regular basis and follow the guidance that would eventually lead to improved health conditions. However, although there is tremendous promise, uncertainty exists regarding whether mHealth can indeed improve patient health and behavior outcome, for a number of reasons.

First, although mHealth technologies can facilitate easy medical communication and interventions for patients, too frequent interventions might lead to annoyingness or habituation (Pop-Eleches et al. 2011). Second, health information that is inconsistent with patients’ prior belief or perceived as non-credible may be less persuasive and lead to potential information avoidance (Klein and Stefanek 2007). Third, the increased pervasiveness of personal behavioral tracking may bring potential privacy concerns to the users. Previous studies show patients might perceive highly personalized mobile SMS messages as intrusive (e.g., Pop-Eleches et al. 2011).

Furthermore, frequent personalized messages can also cause patients to feel pressured or coerced. Such perceived control and judgment can significantly demotivate patient behavior and lead to lower level of engagement and healthy activities. In particular, prior theories on self-determination (SDT) and cognitive evaluation (CET) have demonstrated that lack of choiceful and volitional feeling can lead to loss of autonomy and self-motivation (Deci and Ryan 1985). Such loss of autonomy can lead to lower patient engagement in the health self-management process (e.g., lower mHealth app usage, lower patient–physician engagement, lower compliance to medication and treatment). Also, prior research showed that pressured evaluations and imposed goals diminish intrinsic motivation because they conduce toward an external perceived locus of causality (Deci and Ryan 1985). Therefore, frequent and advanced personalization enabled by mHealth technologies might backfire patients’ engagement in health self-management.

Finally, from a methodological perspective, measuring the effectiveness of mHealth technology on patient health and behavior outcomes can be rather challenging. To date, very little knowledge has been developed toward evaluating the effectiveness of the mHealth applications. Archival analyses using secondary data may not work due to the potential patient self-selection bias in mHealth technology adoption, as well as patient heterogeneity and high dropout rate in mHealth technology usage. Hence, these issues call for a scientific, rigorous approach to evaluate and quantify the effectiveness of the mHealth platforms.

The above challenges motivate us to ask the following research questions in this paper: In the context of healthcare, does the adoption of mHealth technologies (such as mobile apps) persuade patients with chronic diseases to make behavioral modification in their wellness and lifestyle? If so, what is the corresponding impact on patients’ healthcare outcomes, in both short-term metrics (such as reduction in patients’ blood glucose and glycated hemoglobin levels) and longer-term metrics (such as hospital visits and medical expenses)?

Furthermore, to disentangle the underlying mechanism that drives the observed health outcome, we also look into the detailed patient activities, such as daily walking steps, exercise time, sleeping pattern and food intake, documented through the app, together with the detailed app usage data. This enables us to understand how patients actually use the mHealth app, what kinds of behavioral modifications occur in response to the app usage, and the underlying mechanism. Note that looking into the detailed patient activities and app usage logs can help us understand not only whether or not but also why mHealth technologies can help improve the health care outcomes over time. This is one unique aspect of our work, which distinguishes it from the existing work in this area.

To achieve our goal, in this paper, we instantiate our study within the context of mHealth application for diabetes care. Diabetes is a chronic illness with significant health consequences that lead to macro- and microvascular complications, including heart disease, stroke, hypertension, nephropathy, and neuropathy. The American Diabetes Association (ADA) estimates that 25.8 million children and adults in the United States in 2011 had type 1 or type 2 diabetes. Diabetes poses a heavy economic burden on the U.S. healthcare system, with estimated associated costs in 2017 of \$327 billion (American Diabetes Association 2018). Worldwide, high blood glucose kills about 3.4 million people annually. WHO projects diabetes deaths will double between 2005 and 2030.<sup>3</sup> Therefore, proper patient education and self-management are pivotal, especially for those who are unable to adhere to the complex treatment regimen. However, self-management tasks such as regular medication, frequent blood sugar checks, strict diet management, and consistent exercise can be quite challenging. Hence, there is potential for mHealth applications, to help improve patients’ adherence to these behaviors through longterm engagement. Beyond diabetes care, our methodologies and insights have the potential to be generalized to other chronic disease or wellness contexts.

In particular, to evaluate the effectiveness of mHealth applications on diabetes patients’ behavior and health outcomes, we partnered with a major mHealth company in Asia that provides the nation’s largest mHealth app platform that specializes in diabetes care. We designed and implemented a randomized field experiment based on 9,251 unique observations on blood glucose values and 55,359 unique observations on detailed patient health activities (e.g., steps, exercises, sleep, food intake) and app usage logs from 1,070 diabetes patients over 3 months together with a follow-up survey after 5 months. We recruited our participants on a rolling basis. The entire study spanned from May 1, 2015, to July 31, 2016. By randomly assigning patients to different groups (e.g., adoption versus no adoption of mHealth application), we are able to measure the treatment effect from a causal perspective. Moreover, to evaluate the potential economic impact of the mHealth platform on patients’ medical costs and hospital visits, we conducted additional surveys and telephone interviews before and after the experimental period.

Our main findings are as follows. First, the adoption of the mHealth platform demonstrates a statistically significant impact on reducing the blood glucose and glycated hemoglobin levels<sup>4</sup> of diabetes patients over time. The mHealth platform also has a statistically significant impact on reducing hospital visits and medical expenses for diabetes patients through increased usage of telehealth.

Second, the mHealth platform shows a 21.6% stronger impact on patients’ health outcome than does the web-based platform (i.e., PC version of the application) that provides the same functions for diabetes management. This finding builds on the prior literature on the differences between PC and mobile devices (e.g., Ghose 2017; Xu et al. 2017), indicating an edge that mobile devices have over PC in affecting patients’ health behavior because mobility allows a user to respond more flexibly to real-time information (Ghose et al. 2013).

Third, the mHealth platform also demonstrates a significantly stronger impact on patients’ dietary and life style improvement as well as engagement with app usage than does the web-based platform. Interestingly, we found that patients who adopted the mHealth application did significantly higher level of daily exercise, consumed healthier food with lower daily calories intake, walked more steps and slept for longer time a day. In particular, when patients double their time of mHealth app usage, we observe an average of 17.1% decrease in food calorie consumption, 5.4% increase in daily exercise time, and 14.5% increase in daily sleeping time, leading to an average of 0.29 mmol/L decrease in blood glucose. Our results suggest that mHealth technology can help patients become more autonomously self-regulated with their health behavior. Such increasing intrinsic motivation can help patients become more engaged, persistent and stable in their health activities, leading to long-term behavioral modifications toward a healthier dietary and life style, which ultimately leads to an improvement in their health outcomes (e.g., glucose values, hospital visits). This finding provides strong evidence of the underlying mechanism that drives the health outcome.

Fourth, in conjunction with patient self-management through the mHealth platform, we find heterogeneous effects between personalized and non-personalized messages. Interestingly, paired with all the health-management functions and resources provided by the mHealth platform, non-personalized SMS message interventions with general guidance about diabetes care demonstrate on average the highest effect on reducing patient glucose over time, 18.2% higher than personalized SMS message interventions with patient-specific medical guidance and 7.9% higher than no mobile message intervention at all.

Moreover, personalization is not as effective as nonpersonalization if we try to improve diabetes patients’ engagement with the app usage or general life style (i.e., sleeping behavior or movement habits). This is likely because patients might perceive frequent personalized SMS messages as intrusive and annoying as mentioned in prior work albeit in a different context (Pop-Eleches et al. 2011). These findings are surprising and suggest personalized messaging may not always work in the context of mHealth, and the design of the mHealth platform is critical in achieving better patient health outcomes.

The major contributions of our study are as follows. First, to the best of our knowledge, our study is among the first research to examine the effectiveness and mechanism of the mHealth application platform on chronic-disease management. To disentangle the underlying mechanism that drives the observed health outcome, we investigated the detailed patient activities, such as daily walking steps, exercise time, sleeping pattern and food intake, documented through the app, together with the detailed app usage data. This step enables us to understand how and why mHealth technologies are able to lead to improved healthcare outcomes through patients behavioral modifications.

Second, by partnering with a major mHealth platform as a real-world test bed, we design and conduct a randomized field experiment. This step enables us to identify and measure the impact of mHealth on patient health from a causal perspective, by eliminating the potential self-selection bias in mHealth technology adoption. Moreover, our randomized experiment was conducted on a relatively large scale (with eligible sample size n = 1070), over 3-month treatment period together with a follow-up after 5 months. This experimental design allows our findings to be more rigorous than most prior research that was conducted via smaller-scale pilot studies, over a shorter study period, or without follow-ups in the long run.

Third, this study also presents a unique opportunity to examine the potential economic impact of mHealth technologies on the efficiency of healthcare management.

Fourth, our research provides important insights on mHealth platform design through a better understanding of patient health behavior and interactions with the platform. Such knowledge can be highly valuable for healthcare mobile platform designers and policy makers to improve the design of smart and connected health infrastructures through sustained usage of the emerging technologies.

The rest of this paper is organized as follows. In the next section, we discuss the related literature. The subsequent sectoin describes in detail how we design the randomized field experiments and how we partner with the real-world testbed to carry out the experiment on a large scale. We then describe the experimental data. This is followed by a discussion of how we analyze the data as well as our final results. Further analyses on patient activities and app usage are discussed to understand the underlying mechanism that drives the observed healthcare outcomes, followed by a discussion of additional robustness tests. Finally, we conclude with potential future directions.

## Literature Review

## Impact of Healthcare IT

Our work is related to prior literature on the impact of healthcare IT. Recently, with the development of healthcare IT technologies and digital platforms, researchers have looked into the digital transformation of healthcare (e.g., Agarwal et al. 2010; Bardhan et al. 2015; Liu et al. 2020).

There has been growing interest in the consumer perspective of healthcare IT (e.g., Agarwal and Khuntia 2009; Bardhan et al. 2015; Gao et al 2010; Liu et al. 2020; Yan and Tan 2014). Recent studies have examined the impact of healthcare IT on patient care outcomes (e.g., Anderson and Agarwal 2011; Bardhan and Thouin 2013). For example, Bardhan et al. (2015) focused on a chronic condition (congestive heart failure, CHF) and examined health IT usage in relation to visits and readmissions. They found the adoption of health IT is associated with a reduction in the readmission risk of CHF patients. Interestingly, the evidence thus far for the impact of healthcare IT on patient care outcomes is equivocal, with prior research reporting positive, negative, and nonexistent effects (Agarwal et al. 2010; Bardhan et al. 2015). This, to a large extent, is due to the limitation in data deficiencies and limitations in the econometric estimation methods (Bardhan et al. 2015). These discrepant findings call for plausible explanations and present important opportunities for further work, especially from the patient care perspective.

Recently, studies have also focused on the social perspective and online healthcare platform design (e.g., Gao et al. 2010; Kane et al. 2009; Liu et al. 2020; Yan 2020; Yan and Tan 2014). For example, Liu et al. (2020) proposed an interdisciplinary lens that synthesizes deep learning methods to examine user engagement with encoded medical information in YouTube videos. They found videos with low medical information result in nonengagement; at the same time, videos with a greater amount of encoded medical information struggle to maintain sustained attention driven engagement. Yan and Tan (2014) investigate the role of social support from online healthcare community in patients’ mental health. They found that patients benefit from learning from others. Yan (2020) further studies how online communities can better design social tools to facilitate communication and establish a variety of relationships between users.

In addition to the above, our paper is related to a stream of literature regarding the impact of healthcare IT on patient selfmanagement of disease (particularly chronic disease).<sup>5</sup> For example, Lancaster et al. (2018) has reviewed the use and effects of recent electronic health (eHealth) tools (including linked to electronic medical record, personal health record, web-based surveys and drug list, web-based access to lab results, patient educational resources, patient-clinician messaging) for patient self-monitoring. They found consistent evidence that the use of eHealth tools can lead to improvement in patient symptoms. However, little evidence was found to support the effectiveness of eHealth tools at improving patient self-efficacy and self-management of chronic disease. And no evidence was found toward medication recommendations and reconciliation by clinicians, medication use behavior, health service utilization, adverse effects, quality of life, or patient satisfaction (Lancaster et al. 2018).

Our study builds on this prior set of literature on the impact of healthcare IT. We distinguish our study by focusing specifically on the novel context of mHealth technology, and examine its impact from the patient care perspective, including patients’ engagement with mHealth applications, patients’ self-efficacy and self-management of chronic disease, patients’ behavior modification and health outcome, and patients’ healthcare costs. We also focus on understanding both the immediate impact (upon adoption and usage) and long-term impact (3 to 8 months after the adoption and usage).

## Mobile Health (mHealth) and User Behavior

Our paper is also related to the recent work on mHealth and how it can change user behavior and adherence to medical treatment. Several recent studies have successfully piloted programs based on mobile SMS text messages, targeting patients with asthma, obesity, smoking, HIV/AIDS, and diabetes (e.g., Lester et al. 2010; Pop-Eleches et al. 2011). They have found an impact from mobile SMS messaging on user health behavior; however, the content, intensity, and delivery mode of the SMS messaging seem to have a significant influence on the effectiveness of the mHealth interventions (Free et al. 2013).

For example, Pop-Eleches et al. (2011) conducted a randomized trial using mobile SMS interventions in Kenya to test the effect of mobile SMS reminders on the adherence to HIV treatment. They found simple weekly reminder messages (without any additional counseling) can significantly improve adherence. But surprisingly, more frequent daily messages do not improve patient adherence, because of potential habituation or intrusion. They also found adding more personal words, such as words of encouragement, in the longer text messages was not more effective than either a short reminder or no reminder.

A recent survey by Wang et al. (2017) systematically searched PubMed for mHealth-related studies on diabetes and obesity treatment and management published since 2000. They found existing studies in this area mainly focused on examining the impact from three major types of mHealth interventions: mobile phone text messaging, wearable or portable monitoring devices, and smartphone apps. They also noted that most existing studies included only small samples (< 60 sub jects per group) and short intervention periods (< 3 months, no follow-up) and did not use rigorous data collection or analytic approaches. Although some studies suggest that mHealth interventions are effective and promising, most are pilot studies or have limitations in their study designs. There is an essential need for future studies that use larger study samples, longer intervention and follow-up periods to provide comprehensive and sustainable support for patients and health service providers.

Similar to our paper, a few recent studies also focused on examining the impact of diabetes smartphone app on patient health such as patient weight loss (Allen et al. 2013; Martin et al. 2015) or food intake (Nollen et al. 2014). Instead, our study focuses on more concrete healthcare-centric outcomes including blood glucose, hospital visits and medical expenses. Moreover, we also investigate various behavioral outcomes including patient activities and app usage to disentangle the underlying mechanism that drives the observed health outcomes. This is one unique feature of our study which distinguishes it from all existing studies. Another study related to ours is Rossi et al. (2009). The authors examined the impact of a mobile application “Diabetes Interactive Diary” on type 1 diabetes patients but found the app was associated with a non-statistically significant reduction in blood glucose based on a study with only 41 patients. Kato-Lin et al. (2016) found a strong positive impact of the mobile-based visual diary and dietitian support on improving customer engagement. Using a unique dataset from a freemium mobile weight management application, Uetake and Yang (2017) have found the impact of short-term goal achievement varies across user segments.

Compared with these studies, our work distinguishes itself in its focus on mHealth app and chronic disease care (particularly diabetes), to examine the causal impact on patient behavior, medical expense, and health outcome. Our study is significantly different from all these papers in research context, goal, methodology, and study scale (sample size): (1) our study focused mainly on type 2 diabetes which, different from type 1 diabetes, is directly tied to dietary or lifestyle self-management; (2) our goal is to understand the causal impact of mHealth app on diabetes patient health outcomes, as well as the underlying mechanism of how such technology can persuade patients to modify their behaviors to achieve these outcomes; (3) our research method was based on randomized controlled trial, (4) our study was conducted based on a much larger scale (sample size n = 1070), which allows our study to be much more rigorous than many existing pilot studies.

## A Randomized mHealth Field Experiment

To evaluate the effectiveness of the mHealth app on patients behavior and health outcomes, one could collect secondary app user data and examine the user health behavior before and after the app adoption. However, the critical challenge for such an archival data analytical approach is the potential (strong) self-selection bias in the app user population. For example, users who care more about their health will be more likely to adopt the mHealth app, and will be more likely to change their behavior and life style in a healthier direction. This self-selection could lead to a statistically significant and positive correlation between the app adoption/usage and user health over time. However, this positive relationship might be endogenous, because of the unobserved user-level attributes that lead to the app adoption/usage in the first place.

Therefore, ideally, we would like the users to be randomly assigned to use the mHealth app—those who use the app and those who do not use the app will show no significant difference statistically. If so, the difference in their health behavior changes before and after the app adoption would be attributed solely to the impact of the app adoption/usage over time. Unfortunately, using only secondary data, we cannot easily identify such an impact from a causal perspective.

To ensure the random assignment of users, we propose to design and implement a randomized field experiment by part nering with a major mHealth company in Asia that provides the largest mHealth app platform in the nation that specializes in diabetes care. In this section, we will first introduce the background of this mHealth app platform. Then, we will discuss in detail how we design and implement our experiment.

## Mobile Health Platform Background

Our research partner is a major mHealth firm in Asia. It provides the largest mHealth platform for chronic-disease management, specializing in diabetes care. To date, the mobile platform has 156,120 active users and 9,970 affiliated physicians who specialize in diabetes care across the nation. In addition to the external expert network, the platform also has a full-time internal expert team with more than 20 medical professionals including physicians, pharmacists, nurses, psychologists, and nutritionists. The platform integrates all the medical resources into a mobile app for patients.

This patient app provides diabetes patients with 24/7 services with four sets of core functions to facilitate patient selfmanagement:

(1) Behavior Tracking: patients can record and upload at any time their blood glucose, blood pressure, exercises, diet, weight, sleep, and so on.

(2) Risk Assessment and Personalized Solutions: a cloudbased backend data analytic system will analyze individual patients’ data and assesses the real-time health risk for each patient by taking into consideration 45 different types of medical conditions, including the stage and type of diabetes, whether the patient is pregnant, whether the patient has a complication, and so on. Based on the data analytic results, the app will recommend personalized self-management solutions for each patient regarding diet, exercise, life style, and potential medication. To ensure the validity of the recommendation, the internal medical team will view and discuss the data analytic results and personalized solutions regularly to improve the algorithm.

(3) Q&A: the patients can contact the physicians in the internal and external expert networks for free consul tation at any time regarding the medication, treatment, or self-management of their health.

(4) Patient Community: the patients can participate in a digital community through the mobile app platform to discuss and communicate with each other.

For a better understanding of the patient app function, we provide screenshots of the major functions in Figure A1 in Appendix A. In particular, Figure A1(a) illustrates the overview of the user homepage after login. Figure A1(b) illustrates the page of recording a new blood glucose value. Figure A1(c) illustrates a set of user behavior tracking pages that visualize blood glucose, blood pressure, diet, and exercise. In addition, we also provide more screenshots for other related app functions in Figures A3 and A4.

One critical challenge from the app platform designer’s perspective is to examine how effective the app is in actually improving the patient health behavior and outcomes over time. To achieve this goal, we designed a large-scale randomized field experiment, which we discuss next.

## Experiment Design and Implementation

We designed and implemented a nationwide large randomized field experiment by partnering with the firm. Our national campaign for the event received widespread attention from the society. To examine the impact of the mHealth platform under various situations, we designed five experimental conditions (2 Control Groups + 3 Treatment Groups) as follows:

• Control Group (C1): No treatment, behave as usual.

Control Group (C2): Use the web (PC) version of the health app;

• Treatment Group (T1): Use the mHealth app;

Treatment Group (T2): Use the mHealth app + Receive non-personalized SMS reminder messages with general knowledge about diabetes care twice a week; and

Treatment Group (T3): Use the mHealth app + Receive personalized SMS reminder messages with patientspecific health advice from the internal expert team twice a week.

Control Group C1 is the baseline. Control Group C2 is a second baseline to examine the potential device effect that can lead to differences in the effectiveness of the diabetes selfmanagement application. Treatment Group T1 contains the normal mHealth app users who have access to all four sets of app functions. We designed Treatment Group T2 to test the potential synergetic effect when the mHealth app is paired with the mobile SMS messaging; research has shown the latter alone to be effective in improving patient treatment adherence and health outcomes (e.g., Lester et al. 2010). Finally, we designed Treatment Group T3 to further test the potential impact from the design of the SMS messaging, which were shown to have a significant influence on the effectiveness of the mHealth interventions (Free et al. 2013; Pop-Eleches et al. 2011). We provide an example of the two types of mobile SMS messages in Figure A5 in Appendix A. Notice that all three treatment groups have access to the same mHealth support including behavioral tracking, personalized risk assessment and solutions, Q & A, and online community. The SMS reminder messages sent in T2 or T3 do not contain any new information beyond what is shown in the app, but they simply serve as an additional “nudge” (either nonpersonalized or personalized).

We recruited participants for our experiment based on a voluntary basis through a combination of channels, including announcements through several national major news websites, social media and social networks via both web and mobile platforms, as well as offline recruiting through local hospitals and communities. Upon registration, each participant was randomly assigned to one of the five experimental groups. As compensation for their time and efforts, participants were automatically enrolled in a lottery upon completion of the experiment. The potential rewards from the lottery included Apple Watch, Fitbit smart bands, blood glucose meters, air purifiers, or gift cards with various values (from \$5 to \$750).

The initial round of participant recruitment started in May 2015. One practical challenge in medical trials is the potential delays in recruitment and the high rates of dropout, which might lead to uncertainty in the treatment effectiveness and might confound results (e.g., Gupta et al. 2015; Watson and Torgerson 2006). To ensure an effective sample size, we conducted the experiment by recruiting participants on a rolling “first-come-first-served” basis until the target sample size was met. Such an approach is common in medical trials (e.g., Gupta et al. 2015; Kim Yeary et al. 2017; Myerson et al. 2018). Overall, the recruitment period spanned over 7 months, from May 2015 to Dec 2015. To guarantee that long recruitment window would not introduce any confounding factors caused by time trend, we conducted an additional sub sample analysis by selecting a subset of control and treatment groups who were recruited into our experiment during the same month. We provide more details on this in the “Robustness Analyses” section.

The treatment period of the experiment lasted for 3 months (90 days) starting from the day of registration. Based on the random assignment to the experimental group, each participant received the corresponding treatment according to the experimental design during the treatment period. In addition, to collect patient-level demographics and medical history, as well as to evaluate the potential economic impact of the mHealth platform on patients’ medical costs and hospital visits, we conducted additional surveys through telephone interviews before and after the treatment period. In particular, we interviewed each participant three times—first at the beginning of the experiment (during registration), and second at the end of the 3-month treatment period, and then another 5 months after that.

Therefore, for each participant, the total experimental period lasted for 8 months (i.e., pre-treatment survey + 3-month treatment period + post-treatment survey + 5-month posttreatment period + another post-treatment survey). Overall, the entire study for all our participants spanned 15 months from May 2015 to July 2016. The last batch of participants was recruited in December 2015. They completed the experiment and surveys by the end of July 2016.

During the three telephone interviews for the pre- and posttreatment surveys, we asked the participants about their demographics, medication and medical history, most recent blood glucose and glycated hemoglobin levels, frequency of hospital visits, medical costs, and so on.<sup>6</sup> Informed consent was obtained at each phase of the study that required data collection. In the next section, we will discuss in more detail the exact survey variables we collected.

Note that to eliminate potential confounding factors, during the experimental period we ensured the following facts:

(1) No participant had previously adopted the mHealth app prior to the registration to our experiment.

(2) Participants who were assigned to the two control groups did not happen to adopt the mHealth app during the experiment on their own. (We validated these first two facts by crosschecking the phone numbers between the participants and the mHealth app adopters in the company database, and also through the post-treatment survey to exclude those who were not supposed to be adopters of the app prior or during the experiment.)

(3) Participants did not adopt other similar apps during the experiment. (We validated this fact through the posttreatment survey to exclude the potential impact from other similar apps.)

(4) Participants had no other major medical conditions prior to the experiment. Besides, we focused on type 2 diabetes which, different from type 1 diabetes or gestational diabetes, is directly tied to dietary or lifestyle selfmanagement.

Finally, to avoid potential bias due to misalignment with participants’ prior expectation, we followed prior social and behavioral research methods (Hoyle et al. 2001) and ensured that the recruitment announcement only revealed the general purpose of the experiment (i.e., to help improve diabetes care), whereas it did not reveal the exact details of the experiment (i.e., to study the impact of adoption of mHealth app on diabetes patient behavior).

## Data

In this section, we will describe our data from both the experiment and the pre- and post-treatment surveys. We first illustrate our data sampling procedure during the recruitment and randomization processes. To validate our samples, we conducted the randomization check and briefly discuss it.

## Randomization and Sampling

Our recruitment process led to the enrollment of 1,770 patients. To ensure minimum confounding factors, we excluded 427 (24.1%) patients from our sample who did not have diabetes (e.g., people whose blood glucose value was reaching the upper bound of the normal range but were not classified as diabetic yet), or had other major chronic disease(s) at the same time (e.g., kidney disease, heart disease, arthritis, HIV/AIDS), or were already users of the app. These exclusions led to a sample of 1,343 patients whom we randomly assigned into one of the five experimental groups. During the 3-month treatment period, 273 (15.4%) patients dropped out. Hence, our final eligible sample for analysis contains 1,070 patients, 60.5% of the original enrolled sample. We illustrate the flow of the randomization and sampling procedure in Figure C1 in Appendix C.

Note that high patient dropout rate is a common challenge in medical trials (e.g., Gupta et al. 2015). To alleviate any additional concern toward this issue, we compared the distributions of participants’ demographic and baseline healthrelated characteristics between the dropout samples and the eligible samples. We did not find statistically significant difference between the two. We also compared the distributions of participants’ demographic and baseline health-related characteristics among all the dropout samples across the five experimental groups. We did not find statistically significant difference across the control and treatment groups regarding dropout samples. In the “Robustness Analyses” section, we provide more detailed results on these tests. Therefore, while we acknowledge this fact as one potential data limitation in our study, we are more confident that it is not a serious concern in affecting our results.

## Data Description

Our main experimental data contain a combination of three data sets:

(1) Panel data of individual health and behavior characteristics recorded through the mobile (or web-based) health application during the 3-month treatment period. This information includes diabetes-related health activities such as glucose value, glucose type (e.g., pre-/postbreakfast, pre-/post-lunch, pre-/post-dinner, before sleep), and uploading time/date. Notice that for the control group (C1) that did not use the mobile or web-based health application, we asked the participants to upload their glucose values at least twice: at the beginning and end of the 3-month treatment period through a web portal. We provide the screenshot of this web portal in Figure A2 in Appendix A.

(2) Panel data of individual activities and app usage logs. This information includes walking steps, exercise time and calories burned, food intake and estimated calories, sleeping time (starting and ending time, and length), app opening time and frequency, frequency of documenting activity logs, loyalty rewards, shopping activities (product purchased, price, order time), in-app Q&A with medical experts (query time, answer time). For some of the activities such as walking steps, the app can automatically log them through the build-in sensors of the smartphone.<sup>7</sup> For other activities like exercise, sleep, or food intake, they require the patients to document them in the app. Note that the patients only need to document (select from a pre-compiled list) the type of exercise/food and corresponding time/amount; the app can then automatically calculate the estimated calories burn/intake. For the purpose of understanding patient app usage behavior, we consider the frequency of documenting activity logs as the times only when patients document exercise, sleep and food activities in the app (instead of the automatic activity logs generated by the app).

(3) Survey data of individual demographics, health, and behavior characteristics from the pre- and post-treatment surveys. This information contains individual age group, gender, marital status, income level, diabetes type (i.e., type 1, type 2, gestational), diabetes age (time since diabetes was first diagnosed), frequency of glucose monitoring, whether the patient has any complications, the most recent blood glucose value and type, glycated hemoglobin for the most recent 3 months, average time for exercise and sleep per day during the most recent 3 months, average calories per meal during the most recent 3 months, whether the patient is a smoker or drinker, whether the patient is pregnant, current and past medication, medical history (e.g., blood pressure, blood fat, family history), frequency of hospital visits per year, frequency of hospital visits during the last 3 months, and medical costs during the last 3 months. The survey data also contain information on individual app-related activities including registration time/date, frequency of app daily usage, and satisfaction rate. For details on these variables, we provide the summary statistics in Table 1.

## Randomization Check

To validate the randomization procedure, we conducted a randomization check. We provide the details about the randomization check in Table 2. Across the five experimental groups, we compared the distributions of the patient demographics and baseline health condition characteristics. We found the distributions are similar across groups. Furthermore, to better control for the potential variation in the patient-level characteristics, we tested several different models by including all or different subsets of these variables in our analyses as control variables. We found our results stay highly consistent. We will discuss more details in the next section.

## Analysis and Findings

In this section, we discuss how we analyzed the experimental data to examine the impact of the mHealth platform on patient health behavior and outcomes. Note we have both the panel data on patient health and behavior characteristics during the 3-month treatment period, and the cross-sectional survey data before treatment (upon registration) and 5 months after treatment. We first conduct a group-level analysis using the survey data to compare the difference in patient health and behavior before and after the treatment. Then, we use the panel data to conduct the analysis of the treatment effect at the individual level.

<table><tr><td colspan="6">Table 1. Summary Statistics of Main Variables</td></tr><tr><td></td><td>Description</td><td>Mean</td><td>Std.</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Variable</td></tr><tr><td>C1</td><td>Dummy for control group 1</td><td>0.15</td><td>0.33</td><td>0</td><td>1</td></tr><tr><td>C2</td><td>Dummy for control group 2 (Web)</td><td>0.20</td><td>0.40</td><td>0</td><td>1</td></tr><tr><td>T1</td><td>Dummy for treatment group 1</td><td>0.21</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td>T2</td><td>Dummy for treatment group 2</td><td>0.22</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>T3</td><td>Dummy for treatment group 3</td><td>0.22</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td colspan="6">Patient Demographics</td></tr><tr><td>Male</td><td>Whether the patient is male</td><td>0.65</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>Age</td><td>Numerical value of age</td><td>55.17</td><td>8.91</td><td>23</td><td>72</td></tr><tr><td>Age_30</td><td>Dummy for age group &lt; 30</td><td>0.24</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>Age_30_40</td><td>Dummy for age group 31–40</td><td>0.30</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>Age_41_60</td><td>Dummy for age group 41–60</td><td>0.39</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Age_60</td><td>Dummy for age group &gt; 60</td><td>0.06</td><td>0.24</td><td>0</td><td>1</td></tr><tr><td>Married</td><td>Whether the patient is married</td><td>0.83</td><td>0.39</td><td>0</td><td>1</td></tr><tr><td>Income</td><td>Numerical value of income ($, annual)</td><td>76827.27</td><td>12258.67</td><td>29630</td><td>234524</td></tr><tr><td>Income_50K</td><td>Dummy for income &lt; 50K</td><td>0.24</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>Income_50_100K</td><td>Dummy for income 50–100K</td><td>0.66</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Income_100_200K</td><td>Dummy for income 100,001–200K</td><td>0.09</td><td>0.29</td><td>0</td><td>1</td></tr><tr><td>Income_200K</td><td>Dummy for income &gt; 200K</td><td>0.01</td><td>0.11</td><td>0</td><td>1</td></tr><tr><td colspan="6">Patient Prior Conditions</td></tr><tr><td>Pre-meal Glucose</td><td>Prior (most recent) pre-meal glucose value</td><td>7.23</td><td>1.83</td><td>3.2</td><td>18</td></tr><tr><td>Post-meal Glucose</td><td>Prior (most recent) post-meal glucose value</td><td>9.86</td><td>4.36</td><td>4.2</td><td>30.7</td></tr><tr><td>Hemoglobin</td><td>Most recent glycated hemoglobin</td><td>6.72</td><td>1.98</td><td>4.6</td><td>35</td></tr><tr><td>Complication</td><td>Whether there is a complication</td><td>0.19</td><td>0.39</td><td>0</td><td>1</td></tr><tr><td>Smoking</td><td>Whether the patient is a smoker</td><td>0.09</td><td>0.28</td><td>0</td><td>1</td></tr><tr><td>Drinking</td><td>Whether the patient drinks &gt; 140ml alcohol per week</td><td>0.08</td><td>0.25</td><td>0</td><td>1</td></tr><tr><td>Pregnant</td><td>Whether the patient is pregnant</td><td>0.01</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Other Major Disease</td><td>Whether the patient has other major diseases</td><td>0.01</td><td>0.11</td><td>0</td><td>1</td></tr><tr><td>Type 2 Diabetes</td><td>Whether the patient has type 2 diabetes</td><td>0.98</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Type 1 Diabetes</td><td>Whether the patient has type 1 diabetes</td><td>0.01</td><td>0.11</td><td>0</td><td>1</td></tr><tr><td>Gestational Diabetes</td><td>Whether the patient has gestational diabetes</td><td>0.01</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Diabetes Age</td><td>Year(s) since diabetes was first diagnosed</td><td>5.40</td><td>5.14</td><td>0</td><td>28</td></tr><tr><td colspan="6">Patient Health Outcomes</td></tr><tr><td>Uploaded Glucose</td><td>Patient self-uploaded real-time glucose (overall)</td><td>7.18</td><td>2.07</td><td>3.1</td><td>34.3</td></tr><tr><td>(Pre-meal)</td><td>Patient self-uploaded real-time glucose (pre-meal)</td><td>6.47</td><td>1.70</td><td>3.1</td><td>29.1</td></tr><tr><td>(Post-meal)</td><td>Patient self-uploaded real-time glucose (post-meal)</td><td>8.17</td><td>2.18</td><td>3.9</td><td>34.3</td></tr><tr><td>Upload_Morning</td><td>Whether uploading time is morning</td><td>0.36</td><td>0.48</td><td>0</td><td>1</td></tr><tr><td>Upload_Afternoon</td><td>Whether uploading time is afternoon</td><td>0.15</td><td>0.36</td><td>0</td><td>1</td></tr><tr><td>Upload_Night</td><td>Whether uploading time is night</td><td>0.49</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>Hospital Visits</td><td>Number of hospital visits related to diabetes during the last 3 months</td><td>2.64</td><td>6.69</td><td>0</td><td>12</td></tr><tr><td>Medical Spending</td><td>Amount of medical spending related to diabetes during the last 3 months ($)</td><td>57.14</td><td>63.49</td><td>20</td><td>1587.30</td></tr><tr><td colspan="6">Patient Activities</td></tr><tr><td>Daily #Steps</td><td>Number of steps walked per day</td><td>3597.82</td><td>5123.67</td><td>1021</td><td>49926</td></tr><tr><td>Daily Exercise Time</td><td>Daily exercise time (minutes)</td><td>55.26</td><td>62.15</td><td>0</td><td>269.01</td></tr><tr><td>Daily Exercise Calorie</td><td>Daily calories burned through exercise</td><td>330.19</td><td>372.40</td><td>0</td><td>1720</td></tr><tr><td>Daily Food Calories</td><td>Amount of calories consumed per day</td><td>1090.59</td><td>169.11</td><td>438</td><td>2647</td></tr><tr><td>Daily Sleeping Length</td><td>Total daily sleeping time (minutes)</td><td>559.28</td><td>196.60</td><td>198</td><td>1380</td></tr><tr><td>Weekly Late Night Sleep</td><td># Nights per week when go to bed after 11pm</td><td>1.97</td><td>4.21</td><td>0</td><td>7</td></tr><tr><td colspan="6">Patient App Usage</td></tr><tr><td>Daily #Opening App</td><td>Daily frequency of opening the app</td><td>1.14</td><td>0.43</td><td>0</td><td>6</td></tr><tr><td>Daily #Activity Logs</td><td>Daily frequency of activities documented through app</td><td>1.32</td><td>4.65</td><td>0</td><td>34</td></tr><tr><td>Weekly #Communications</td><td>Weekly # of in-app communications with physicians</td><td>1.94</td><td>3.26</td><td>0</td><td>9</td></tr><tr><td>Weekly Loyalty Rewards</td><td>Weekly loyalty rewards earned</td><td>19.43</td><td>241.32</td><td>0</td><td>35000</td></tr><tr><td>Weekly In-app Shopping</td><td>Weekly in-app shopping for health products ($)</td><td>25.97</td><td>180.60</td><td>0</td><td>2541.43</td></tr><tr><td colspan="6">#Observations on Uploaded Glucose Values: n = 9,251, #patients n = 1,070.#Observations on Patient Activities and App Usage: n = 55,359, #patients n = 1,070.Data Period: May 2015–July 2016.</td></tr></table>

Table 2. Randomization Check: Demographic and Baseline Characteristics across Five Groups

<table><tr><td>Variable</td><td>C1(n = 156)</td><td>C2(n = 209)</td><td>T1(n = 230)</td><td>T2(n = 234)</td><td>T3(n = 241)</td><td>ANOVA</td></tr><tr><td colspan="7">Age</td></tr><tr><td>&lt; 30</td><td>23%</td><td>22%</td><td>24%</td><td>21%</td><td>24%</td><td>p &gt; 0.05</td></tr><tr><td>30–40</td><td>31%</td><td>29%</td><td>26%</td><td>23%</td><td>21%</td><td>p &gt; 0.05</td></tr><tr><td>41–60</td><td>40%</td><td>42%</td><td>45%</td><td>51%</td><td>48%</td><td>p &gt; 0.05</td></tr><tr><td>&gt; 60</td><td>6%</td><td>6%</td><td>5%</td><td>5%</td><td>6%</td><td>p &gt; 0.05</td></tr><tr><td colspan="7">Gender</td></tr><tr><td>Male</td><td>65%</td><td>64%</td><td>65%</td><td>67%</td><td>66%</td><td>p &gt; 0.05</td></tr><tr><td>Female</td><td>35%</td><td>36%</td><td>34%</td><td>34%</td><td>35%</td><td>p &gt; 0.05</td></tr><tr><td>Married</td><td>82%</td><td>77%</td><td>90%</td><td>90%</td><td>86%</td><td>p &gt; 0.05</td></tr><tr><td colspan="7">Income ($, annual)</td></tr><tr><td>&lt; 50K</td><td>26%</td><td>25%</td><td>27%</td><td>24%</td><td>27%</td><td>p &gt; 0.05</td></tr><tr><td>50–100K</td><td>66%</td><td>65%</td><td>62%</td><td>65%</td><td>64%</td><td>p &gt; 0.05</td></tr><tr><td>100,001–200K</td><td>7%</td><td>8%</td><td>10%</td><td>10%</td><td>8%</td><td>p &gt; 0.05</td></tr><tr><td>&gt; 200K</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>1%</td><td>p &gt; 0.05</td></tr><tr><td colspan="7">Baseline Condition</td></tr><tr><td>Pre-meal Glucose</td><td>7.11</td><td>7.04</td><td>6.90</td><td>7.13</td><td>6.95</td><td>p &gt; 0.05</td></tr><tr><td>Post-meal Glucose</td><td>8.43</td><td>8.59</td><td>8.44</td><td>8.38</td><td>8.68</td><td>p &gt; 0.05</td></tr><tr><td>Glycated Hemoglobin</td><td>7.03</td><td>6.98</td><td>6.60</td><td>6.67</td><td>6.82</td><td>p &gt; 0.05</td></tr><tr><td>Complication</td><td>19%</td><td>20%</td><td>17%</td><td>18%</td><td>16%</td><td>p &gt; 0.05</td></tr><tr><td>Smoking</td><td>8%</td><td>9%</td><td>10%</td><td>9%</td><td>9%</td><td>p &gt; 0.05</td></tr><tr><td>Type 2 Diabetes</td><td>98%</td><td>96%</td><td>97%</td><td>96%</td><td>96%</td><td>p &gt; 0.05</td></tr><tr><td>Type 1 Diabetes</td><td>1%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>p &gt; 0.05</td></tr><tr><td>Gestational Diabetes</td><td>1%</td><td>1%</td><td>2%</td><td>2%</td><td>2%</td><td>p &gt; 0.05</td></tr><tr><td>Diabetes Age</td><td>5.41</td><td>5.32</td><td>5.46</td><td>5.42</td><td>5.36</td><td>p &gt; 0.05</td></tr></table>

Notes: Data are in percentage or mean value. Percentages do not add up to 100% in some cases because of rounding. The majority of our patient samples belong to type 2 diabetes, which is the main focus of our study. Income is adjusted based on the local cost of living.  
To better control for the potential variation in the patient-level characteristics, we also included all these variables in our primary analyses as control variables

## Group-Level Analysis

First, we conduct a group-level analysis using the survey data to compare the difference in patient health and behavior before and after the treatment. Note the total time period between the two surveys is 8 months: a 3-month treatment period plus a 5-month post-treatment period. By doing so, we aimed to capture the potential long-term effect of the treatment. In particular, across the five groups, we compare the differences in the blood glucose and glycated hemoglobin levels, the number of hospital visits during the most recent 3 months, and the total medical spending related to diabetes during the most recent 3 months. We provide the details in Table 3. The values across groups are statistically different at the p < 0.05 level based on the one-way ANOVA test.

The first thing we notice is that in the baseline control group (C1), the four variables stayed relatively stable before and after the treatment, whereas all other groups that used the health application (whether mobile- or web-based) showed a significant reduction in patient glucose and hemoglobin values, as well as a reduction in hospital visits and medical spending. This finding is promising. It indicates the health platform for diabetes self-management indeed has a significant effect on improving patient health outcomes as well as reducing costs.

Second, compared to the second baseline group (C2) with web-based health intervention, the three treatment groups with mHealth interventions (T1, T2, T3) experienced a statistically significantly higher impact on patient health and costs. For example, under the same functional setting of the health application, we observe a 21.6% increase in the mobile-based platform’s (T1) impact on reducing patients’ glucose, compared with the web-based platform’s (C2) impact. This result is consistent with previous findings indicating a significant mobile device effect (e.g., Jung et al. 2019; Wang et al. 2016; Xu et al. 2017). Such an effect can become salient in personal health management through faster and more flexible user response to real-time information and mobile-enhanced user self-efficacy (e.g., Kato-Lin et al. 2016).

Third, we notice that among the three mobile treatment groups, T2, when we paired the mHealth app with simple nonpersonalized SMS reminder messages about general guidance on diabetes care, demonstrates the strongest treatment impact on reducing blood glucose levels over time, 18.2% higher than personalized SMS message interventions with patientspecific medical guidance and 7.9% higher than no mobile message intervention at all. We also see a consistent trend in the hemoglobin value. Interestingly, T3, when we paired the mHealth app with personalized SMS messages about patientspecific medical advice, does not perform better than nonpersonalized messages in helping patients improve their health outcome. This finding is surprising but highly consistent with prior research that the design of the SMS messaging has a significant influence on the effectiveness of the mHealth interventions (Free et al. 2013), and that more personal and encouraging words in longer text messages were not more effective than either a short reminder or no reminder, because of potential habituation or perceived intrusion (Pop-Eleches et al. 2011), and that personalization might lead to potentia privacy concerns and information overload for consumers (e.g., Aral and Walker 2011; Ghose 2017; Ghose et al. 2014; Goldfarb and Tucker 2011).

Finally, and interestingly, when looking into the patient hospital visits and medical spending, we find T3 demonstrates the highest impact in reducing the two. T3 is 62.5% and 168.4% more effective compared with T2, the next best treatment, in reducing hospital visits and medical spending, respectively. This result suggests the potential of the mHealth app combined with personalized SMS messaging to reduce the medical and operational costs for chronic disease patients and healthcare providers. An intriguing implication of this finding is that, although personalized messaging is not more effective in affecting patient health outcome than nonpersonalized messaging, it can actually facilitate a personal connection between patients and physicians, which in turn leads to increased patient trust in the mHealth platform and higher willingness to adopt telehealth (e.g., through Q&As and online communications with physicians), hence reducing patients’ need (or urge) to visit hospitals in person.

Note that all the analyses in this subsection are based on the cross-sectional survey data and are conducted at the group (mean) level. The impacts here should be interpreted as the group-level mean treatment effect. To further account for the potential heterogeneity within the group, we conducted individual-level analysis using the panel data, which we will discuss next.

<sup>8</sup>To further verify this finding, we conducted a follow-up analysis to examine the potential usage of telehealth across different experimental groups (C2, T1, T2, T3). In particular, we looked into the frequency of in-app patient– physician communications. We found patients in T3 group indeed demonstrated the highest frequency of patient–physician communications through the platform, with an average of 4.35 times per person during the 3-month experimental period. In contrast, patients in T2 and T1 groups had an average of 2.57 and 1.44 patient–physician communications, respectively. We also found a similar mobile device effect in affecting patients’ likelihood to adopt telehealth. Patients in C2 showed the lowest frequency with only 0.78 patient–physician communications. A pair-wise t-test demonstrates these group-level differences are statistically significant.

<table><tr><td colspan="5">Table 3. Results from the Group Mean Analysis</td></tr><tr><td>Treatment Group</td><td>Diff-Glucose</td><td>Diff-Hemoglobin</td><td>Diff-Hospital Visits (Recent 3 Mons)</td><td>Diff-Spending (Recent 3 Mons, USD)</td></tr><tr><td>C1 (n = 156)</td><td>-0.0287</td><td>-0.0143</td><td>-0.0283</td><td>-0.95</td></tr><tr><td>C2 (n = 209)</td><td>-0.5173</td><td>-0.1967</td><td>-0.0568</td><td>-5.70</td></tr><tr><td>T1 (n = 230)</td><td>-0.6291</td><td>-1.0316</td><td>-0.1208</td><td>-8.55</td></tr><tr><td>T2 (n = 234)</td><td>-0.6790</td><td>-1.1612</td><td>-0.1393</td><td>-11.55</td></tr><tr><td>T3 (n = 241)</td><td>-0.5746</td><td>-0.9405</td><td>-0.2264</td><td>-31.00</td></tr></table>

Note: Values are calculated based on the difference between the two surveys (post-treatment value minus pre-treatment value). Glucose value is calculated based on an average across all glucose types. (Pairwise t-Test was conducted to test the pairwise difference between each two experimental groups for each of the four health outcome variables. The null hypothesis was rejected at $\rho < 0 . 0 5$ for each comparison.)

## Individual-Level Diff-in-Diff Analysis

To better control for the potential individual heterogeneity and explain the potential discrepancy in the observed outcome, we conduct individual-level analysis using the panel data of individual health and behavior characteristics we collected during the 3-month treatment period. Because our recruitment is conducted on a rolling basis, we consider the time indicator in our context as the time elapsed since the patient started the experiment. Particularly, in our analysis, it is defined as the unique sequence index of each patient’s uploaded glucose value.

To account for the patient-level baseline time trend,<sup>9</sup> we apply a diff-in-diff method to model individual-level glucose change over time. In particular, the first-level difference is the within-group glucose change over time (i.e., group-specific time trend), and the second-level difference is the discrepancy in this time trend across groups. Put more formally, we model the glucose value for patient i at time t as follows:

$$
\begin{array}{l} G l u c o s e _ {i t} = \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} + \beta_ {2} T i m e _ {t} + \\ \beta_ {3} T r e a t m e n t _ {i} \times T i m e _ {t} + X _ {i} \beta_ {4} + C _ {i t} \beta_ {5} + \varepsilon_ {i t} \end{array}\tag{[1]}
$$

where Treatment<sup>i</sup> represents the indicators of the five experimental groups. Time represents the time indicator of how many days since the start of the treatment period when the corresponding glucose value was uploaded $( 1 \leq T i m e _ { t } \leq 9 0 )$ 10

$X _ { i }$ is a vector of control variables for patient-specific timeinvariant characteristics including age group, gender, income level, marital status, diabetes type, diabetes age, frequency of glucose monitoring, whether the patient has any complications, most recent glucose and glycated hemoglobin levels prior to the experiment, average time for exercise and sleep per day and average calories per meal prior to the experiment, whether the patient is a smoker or drinker, whether the patient is pregnant, whether the patient has any other health concerns, such as high blood pressure or cholesterol, whether the patient is currently on any medications, and whether any patient– physician interaction occurred during the 3-month treatment period.

$C _ { i t }$ is a vector of control variables for patient-specific timevarying characteristics including the time of day (morning, afternoon, evening), day of the week (Monday–Sunday), and month indicators of the corresponding glucose uploading activity, uploaded glucose type, daily exercise from the patient (total steps), as well as the patient’s frequency of daily app usage (including all types of activities). $\varepsilon _ { i t }$ is a stochastic error to capture any randomness in patient behavior. The unobserved error term is assumed to be orthogonal to other independent variables and has a mean zero. In the estimation, we cluster the at the experimental group level to account for potential within-group relationships.<sup>11</sup>

We have tested different models (Models I–IV) with different combination of the set of control variables. We provide our estimation results from these models in Table 4. In the estimation, the primary coefficient of interest is $\beta _ { 3 } ,$ , which is a vector that contains coefficients for the four interaction effects (Treatment × Time ). Note the control group indicator C1 is dropped due to collinearity (i.e., the interaction effect between C1 and Time will be captured as the baseline effect, $\beta _ { 2 } ,$ the coefficient of Time ).

<table><tr><td>Variables</td><td colspan="2">Coef. (Std. Err.) $^{\mathrm{I}}$ </td><td>Coef. (Std. Err.) $^{\mathrm{{II}}}$ </td><td>Coef. (Std. Err.) $^{\mathrm{{III}}}$ </td><td>Coef. (Std. Err.) $^{\mathrm{{IV}}}$ </td></tr><tr><td colspan="6">Treatment Effect  $(\beta_3)$ </td></tr><tr><td> $C2 \times Time_t$ </td><td colspan="2">-0.3448**(0.1804)</td><td>-0.4606***(0.1805)</td><td>-0.4105**(0.1819)</td><td>-0.5106**(0.2059)</td></tr><tr><td> $T1 \times Time_t$ </td><td colspan="2">-0.4107***(0.1553)</td><td>-0.4871***(0.1588)</td><td>-0.4642***(0.1589)</td><td>-0.5733***(0.1832)</td></tr><tr><td> $T2 \times Time_t$ </td><td colspan="2">-0.4589***(0.1551)</td><td>-0.5327***(0.1565)</td><td>-0.4588***(0.1587)</td><td>-0.6170***(0.1816)</td></tr><tr><td> $T3 \times Time_t$ </td><td colspan="2">-0.3753**(0.1506)</td><td>-0.4669***(0.1520)</td><td>-0.4243**(0.1531)</td><td>-0.5408**(0.1802)</td></tr><tr><td> $C2(\beta_1)$ </td><td colspan="2">1.4013(1.5766)</td><td>3.2889(2.6396)</td><td>1.5622(0.9973)</td><td>4.7363(3.4386)</td></tr><tr><td> $T1(\beta_1)$ </td><td colspan="2">0.8605(0.6704)</td><td>0.8829(0.6837)</td><td>0.8565(0.6912)</td><td>1.1794(1.0350)</td></tr><tr><td> $T2(\beta_1)$ </td><td colspan="2">0.8282(0.6747)</td><td>0.9042(0.6893)</td><td>0.9756(0.6919)</td><td>1.1432*(0.6361)</td></tr><tr><td> $T2(\beta_1)$ </td><td colspan="2">0.9583(0.6784)</td><td>0.9424(0.6893)</td><td>1.0193(0.6893)</td><td>1.2649*(0.6347)</td></tr><tr><td> $Time_t(\beta_2)$ </td><td colspan="2">0.3095**(0.1528)</td><td>0.3920***(0.1545)</td><td>0.3674**(0.1559)</td><td>0.4755***(0.1822)</td></tr><tr><td>Intercept  $(\beta_0)$ </td><td colspan="2">13.3714***(0.9649)</td><td>11.4988***(1.0279)</td><td>11.8268***(0.8336)</td><td>10.5798***(1.8447)</td></tr><tr><td colspan="6">Patient-Specific Control Variables  $(X_i)$ </td></tr><tr><td colspan="2">Age, Married, Gender, Income, Prior Glucose, Prior Hemoglobin, Prior Medication, Other Disease, Complication, Smoking/Drinking, Pregnant, Diabetes Type, Interaction with Physicians.</td><td>Yes</td><td>Yes</td><td>—</td><td></td></tr><tr><td colspan="6">Patient-Time-Specific Control Variables  $(C_{it})$ </td></tr><tr><td colspan="2">Diabetes Age, Uploaded Glucose Type, Upload Time/Day/Month, Daily Exercise (#Steps), Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td><td>—</td><td>Yes</td><td>—</td></tr></table>

Note: $^ { \star } \mathsf { p } < 0 . 1 , ^ { \star \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star \star } \mathsf { p } < 0 . 0 1$ . Errors are clustered at the experimental group level. Age and Income are in log form. Models I–IV include different sets of control variables. #patients = 1,070, #observations = 9,251.

All four models demonstrate similar estimation results and provide evidence consistent with our previous group-level analyses. First, we notice that all four groups (C2, T1, T2, T3) experience a significant reduction in patient glucose values. This finding indicates the diabetes self-management platform (whether mobile- or web-based) is effective compared with the baseline control group (C1) that did not use the platform.

Second, comparing T1 with C2, we notice a significant device effect: the mobile-based platform is more effective than the web-based platform in reducing glucose levels over time. In particular, we find that when the time since the patient adoption of the platform doubles, the glucose value on average drops 0.24 mmol/L for patients in C2 and 0.28 mmol/L for patients in T1.<sup>12</sup>

Third, when comparing the three treatment groups (T1, T2, T3), we see an interesting trend: T2 (the mHealth app with non-personalized mobile SMS reminder messages) is overall most effective in helping patients reduce their glucose over time, whereas T3 (mHealth app with personalized mobile SMS messages) is less effective. In particular, our results show that when the time since mHealth adoption doubles, the glucose value on average drops 0.28 mmol/L, 0.32 mmol/L and 0.26 mmol/L, for patients in T1, T2 and T3, respectively. In essence, this indicates that T2 (non-personalized) exhibit a 23.1% higher effectiveness in decreasing patient glucose than T3 (personalized).<sup>13</sup>

This observation is consistent with our findings from the group-level analyses as well as the prior literature (e.g., Harle et al. 2012), indicating the design of the mobile SMS messaging plays an important role in the effectiveness of the mHealth interventions on patient health outcomes (e.g., Free et al. 2013; Pop-Eleches et al. 2011). Carefully designing the content, format, intensity, and delivery mode of the SMS messaging is critical.

Finally, when looking at the baseline coefficients in Table 4, we see the four baseline coefficients $( \beta _ { 1 } )$ for the treatment groups $( C _ { 2 } , T _ { 1 } , T _ { 2 } , T _ { 3 } )$ are not statistically significant. This finding further validates our random group assignment indicating the initial glucose values do not vary significantly across groups. Moreover, when looking at the baseline coefficient for $T i m e _ { t } ,$ we find $\beta _ { 2 }$ is statistically significant and positive for all groups. This finding indicates the baseline time trend of patient glucose for control group (C1) without any intervention is increasing over time. This result delivers an important message. It indicates the potential risk and challenge in diabetes care over time, and suggests the importance of empowering patients to improve their self-management for diabetes through smart and digital health platforms.

## Patient-Level Fixed Effect

In the previous section, we considered a large number of patient-level characteristics in the individual-level analysis to control for individual-level heterogeneity. To further account for any other potential unobserved individual characteristics, we conduct the diff-in-diff analysis with patient-level fixed effects as follows:

$$
\begin{array}{r l} G l u c o s e _ {i t} & = \beta_ {0} T i m e _ {t} + \beta_ {2} T r e a t m e n t _ {i} \times \\ & \quad T i m e _ {t} + \mu_ {i} + C _ {i t} \beta_ {3} + \varepsilon_ {i t} \end{array}\tag{[2]}
$$

where $\mu _ { i }$ captures the patient-level fixed effect. Note that in this model, we drop the treatment group indicator Treatment and the patient-specific time-invariant characteristics X from the model because of collinearity with the patient fixed effect. The primary coefficient of interest is $\beta _ { 2 } ,$ the interaction between the treatment group indicator and time. We estimate the model with the patient-specific time-variant characteristics, $C _ { i t }$ (Model V), and without, $C _ { i t }$ (Model VI). The corresponding estimation results are shown in Table 5.

Overall, our findings from the patient-level fixed-effects model demonstrate high consistency with our previous analysis using the treatment-group-level fixed effect (i.e., equation [1]). We find the adoption of the mobile-based platform (T1, T2, T3) can statistically significantly improve the health outcome of diabetes patients in reducing their blood glucose values over time, even after controlling for the individual-level fixed effects.

Moreover, we also see a consistent trend: in conjunction with the mHealth app platform, non-personalized mobile messages with general guidance for diabetes care have a higher impact on patient health improvement than personalized mobile messages. These additional empirical analyses provide us with robust evidence in our results.

## Further Analyses on Patient Behavioral Modifications

To disentangle the underlying mechanism that drives the observed health outcome, we further investigated the detailed patient behavioral activities, such as walking steps, exercise time, sleeping pattern and food intake, documented through the app, together with the detailed app usage data. This step enables us to understand how patients actually use the mHealth app and what kinds of behavioral modifications occur in response to the app usage. Note that looking into the detailed patient activities and app usage logs to study how exactly mHealth technologies can lead to patients’ behavioral modifications over time to achieve better healthcare outcomes is a unique feature of our work, which distinguishes it from all the existing work in this area.

## Analyses on Patient Activity and App Usage

We conducted empirical analyses to study the impact of mHealth treatments on each of these patient activity and app usage outcome variables, using a diff-in-diff model with patient-level fixed effect. We provided the detailed estimation results in Tables 6 and 7 (Patient Activities) and Table 8 (App Usage). Note that because control group C1 did not have access to the health application (web or mobile), we did not have any individual-level activities or app usage data from these patients. In all the analyses below, control group C2 (who had access to the PC-based application) was used as the baseline for comparison.

<table><tr><td>Variables</td><td>Coef. (Std. Err.) $^{v}$ </td><td>Coef. (Std. Err.) $^{vi}$ </td></tr><tr><td colspan="3">Treatment Effect ( $\beta_2$ )</td></tr><tr><td> $C2 \times Time_t$ </td><td>-0.3327**(0.1704)</td><td>-0.4267**(0.1977)</td></tr><tr><td> $T1 \times Time_t$ </td><td>-0.3461**(0.1795)</td><td>-0.4349**(0.1945)</td></tr><tr><td> $T2 \times Time_t$ </td><td>-0.4909***(0.1752)</td><td>-0.5172***(0.1703)</td></tr><tr><td> $T3 \times Time_t$ </td><td>-0.4430**(0.1951)</td><td>-0.4873**(0.1944)</td></tr><tr><td> $Time_t(\beta_2)$ </td><td>0.3557**(0.1732)</td><td>0.3936**(0.1572)</td></tr><tr><td>Intercept ( $\beta_0$ )</td><td>10.1937***(1.7438)</td><td>7.3579***(1.1258)</td></tr><tr><td colspan="3">Patient-Time-Specific Control Variables ( $C_{it}$ )</td></tr><tr><td>Diabetes Age, Uploaded Glucose Type, Upload Time/Day/Month, Daily Exercise (#Steps), Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td><td>—</td></tr></table>

Note: $^ { \star } \mathsf { p } < 0 . 1 , ^ { \star \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star \star } \mathsf { p } < 0 . 0 1$ . Errors are clustered at experimental group level. Models I–IV include different sets of control variables. #patients = 1,070, #observations = 9,251.

Specifically, our main findings are the following. First, when looking into the patient activities as outcome variables (Tables 6 and 7), we found that compared to patients from the PC group (C2), patients from the three mHealth treatment groups (T1, T2, T3) did significantly higher level of daily exercise, consumed healthier food with lower daily calories intake, walked more steps and slept for longer time a day. For example, based on Table 7,<sup>14</sup> when patients double their time of mHealth app usage, we observe an average of 16.8% decrease in food calorie consumption, 6% increase in daily exercise time, and 14% increase in daily sleeping time, for treatment group T1. We observe a similar trend for T2 and T3, with an average of 17.2% (T2) and 17.1% (T3) decrease in food calorie consumption, 6% (T2) and 4.3% (T3) increase in daily exercise time, and 18.2% (T2) and 11.1% (T3) increase in daily sleeping time.

These findings indicate that patients indeed have made significant behavioral modifications toward a healthier dietary and life style after adopting and using the mHealth application. As seen from our results, patients in the mHealth treatment groups became more autonomously self-regulated with their health behavior. Such increasing intrinsic motivation helped them become more engaged, persistent and stable in their behavior, leading to an improvement in their health outcomes (e.g., glucose values, hospital visits).

Interestingly, we found the three mHealth treatment groups performed relatively similarly in daily food calories intake from breakfast, lunch and dinner. However, we noticed a significant drop in the performance from T3, the patient group provided with additional personalized SMS reminder messages, with regard to daily walking, exercise and sleeping patterns. For example, based on Table 7, when combining mHealth app with personalized reminder messages (T3), it leads to a 15% decrease in the number of daily walking steps and a 27.8% decrease in total exercise time compared to using mHealth app alone (T1), and it leads to a 41.2% decrease in the daily steps and a 28.4% decrease in total exercise time compared to combining mHealth app with non-personalized reminder messages (T2).

Table 6. Estimation Results on Patient Activities Using Diff-in-Diff Model with Patient Fixed Effects

<table><tr><td></td><td>Daily Food Calories Intake</td><td>Daily Exercise Time</td><td>Daily Exercise Calories</td><td>Daily #Steps Walked</td><td>Daily Sleeping Length</td><td>Weekly Freq. of Late Night Sleep</td></tr><tr><td>Variables</td><td>Coef. (Std. Err.) $^{A1}$ </td><td>Coef. (Std. Err.) $^{A2}$ </td><td>Coef. (Std. Err.) $^{A3}$ </td><td>Coef. (Std. Err.) $^{A4}$ </td><td>Coef. (Std. Err.) $^{A5}$ </td><td>Coef. (Std. Err.) $^{A6}$ </td></tr><tr><td colspan="7">Treatment Effect</td></tr><tr><td> $C2 \times Time_t$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td> $T1 \times Time_t$ </td><td>-0.1803***(0.0258)</td><td>0.0642**(0.0258)</td><td>0.0626**(0.0241)</td><td>0.0326**(0.0161)</td><td>0.1417**(0.0710)</td><td>0.0332(0.0273)</td></tr><tr><td> $T2 \times Time_t$ </td><td>-0.1854***(0.0227)</td><td>0.0688***(0.0262)</td><td>0.0681**(0.0265)</td><td>0.0434***(0.0168)</td><td>0.1814**(0.0719)</td><td>0.0306(0.0283)</td></tr><tr><td> $T3 \times Time_t$ </td><td>-0.1843***(0.0223)</td><td>0.0457*(0.0250)</td><td>0.0472**(0.0233)</td><td>0.0218*(0.0165)</td><td>0.1019*(0.0691)</td><td>0.0423*(0.0278)</td></tr><tr><td> $Time_t(\beta_1)$ </td><td>0.0197(0.0234)</td><td>-0.0331(0.0274)</td><td>-0.0135(0.0221)</td><td>0.0102(0.0162)</td><td>-0.0298(0.0575)</td><td>-0.0115(0.0245)</td></tr><tr><td> $Intercept(\beta_1)$ </td><td>2.1149***(0.0206)</td><td>1.1162***(0.0229)</td><td>1.4566***(0.0262)</td><td>1.3729***(0.0175)</td><td>1.7192***(0.0575)</td><td>0.4192***(0.0302)</td></tr></table>

Notes: ${ } ^ { \star } \mathsf { p } < 0 . 1 , { } ^ { \star \star } \mathsf { p } < 0 . 0 5 .$ \*\*\*p < 0.01. Errors are clustered at experimental group level. Models A1–A6 correspond to the following user activity outcome variables: A1: (log) Daily food calories intake; A2: (log) Daily exercise time (mins); A3: (log) Daily exercise calories; A4: (log) Daily #steps walked; A5: (log) Daily sleeping length (mins); A6: #Nights per week when the patient went to sleep later than 11 p.m. #Patients = 1,070; #Observations = 55,359.

Table 7. Estimation Results on Patient Activities Using Diff-in-Diff Model with Patient Fixed Effects and Additional Patient-Time-Specific Control Variables

<table><tr><td></td><td>Daily Food Calories Intake</td><td>Daily Exercise Time</td><td>Daily Exercise Calories</td><td>Daily #Steps Walked</td><td>Daily Sleeping Length</td><td>Weekly Freq. of Late Night Sleep</td></tr><tr><td>Variables</td><td>Coef. (Std. Err.)A1</td><td>Coef. (Std. Err.)A2</td><td>Coef. (Std. Err.)A3</td><td>Coef. (Std. Err.)A4</td><td>Coef. (Std. Err.)A5</td><td>Coef. (Std. Err.)A6</td></tr><tr><td colspan="7">Treatment Effects</td></tr><tr><td>C2 × Time $_t$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>T1 × Time $_t$ </td><td>-0.1677***(0.0243)</td><td>0.0597**(0.0252)</td><td>0.0601**(0.0240)</td><td>0.0313**(0.0162)</td><td>0.1399**(0.0711)</td><td>0.0320(0.0275)</td></tr><tr><td>T2 × Time $_t$ </td><td>-0.1724***(0.0202)</td><td>0.0602***(0.0268)</td><td>0.0692**(0.0262)</td><td>0.0452***(0.0169)</td><td>0.1826**(0.0722)</td><td>0.0329(0.0288)</td></tr><tr><td>T3 × Time $_t$ </td><td>-0.1714***(0.0204)</td><td>0.0431*(0.0252)</td><td>0.0455**(0.0235)</td><td>0.0266*(0.0168)</td><td>0.1112*(0.0694)</td><td>0.0443*(0.0279)</td></tr><tr><td>Time $_t(\beta_1)$ </td><td>0.0183(0.0219)</td><td>-0.0348(0.0271)</td><td>-0.0132(0.0222)</td><td>0.0101(0.0163)</td><td>-0.0275(0.0577)</td><td>-0.0122(0.0247)</td></tr><tr><td>Intercept( $\beta_1$ )</td><td>1.9668***(0.0198)</td><td>1.1198***(0.0226)</td><td>1.4574***(0.0267)</td><td>1.3818***(0.0177)</td><td>1.7158***(0.0578)</td><td>0.4432***(0.0305)</td></tr><tr><td colspan="7">Patient-Time-Specific Control Variables:Diabetes Age, Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td></tr><tr><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes: $^ { \star } \mathsf { p } < 0 . 1 , ^ { \star \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star \star } \mathsf { p } < 0 . 0 1$ . Errors are clustered at experimental group level. Models A1–A6 correspond to the following user activity outcome variables: A1: (log) Daily food calories intake; A2: (log) Daily exercise time (mins); A3: (log) Daily exercise calories; A4: (log) Daily #steps walked; A5: (log) Daily sleeping length (mins); A6: #Nights per week when the patient went to sleep later than 11 p.m. #Patients = 1,070; #Observations = 55,359.

Table 8. Estimation Results on App Usage Using Diff-in-Diff Model with Patient Fixed Effects

<table><tr><td></td><td>Daily Freq. of Opening App</td><td>Daily Freq. of Documenting Activity Logs</td><td>Weekly Freq. of Communications</td><td>Weekly Loyalty Rewards</td><td>Weekly In-App Shopping (Total Purchase $)</td></tr><tr><td>Variables</td><td>Coef. (Std. Err.) $^{U1}$ </td><td>Coef. (Std. Err.) $^{U2}$ </td><td>Coef. (Std. Err.) $^{U3}$ </td><td>Coef. (Std. Err.) $^{U4}$ </td><td>Coef. (Std. Err.) $^{U5}$ </td></tr><tr><td colspan="6">Treatment Effect</td></tr><tr><td> $C2 \times Time_t$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td> $T1 \times Time_t$ </td><td>0.1808***(0.0190)</td><td>0.2734***(0.0873)</td><td>0.0812***(0.0059)</td><td>0.2678*(0.1289)</td><td>-0.0023(0.2652)</td></tr><tr><td> $T2 \times Time_t$ </td><td>0.1951***(0.0190)</td><td>0.2965***(0.0881)</td><td>0.0872***(0.0058)</td><td>0.2863*(0.1266)</td><td>0.0375(0.2879)</td></tr><tr><td> $T3 \times Time_t$ </td><td>0.1243***(0.0185)</td><td>0.2160**(0.0893)</td><td>0.0241***(0.0049)</td><td>0.1557**(0.1240)</td><td>-0.1127(0.3201)</td></tr><tr><td> $Time_t(\beta_1)$ </td><td>-0.0401**(0.0176)</td><td>-0.1626**(0.0797)</td><td>-0.1009***(0.0051)</td><td>-0.1906*(0.1107)</td><td>0.0870(0.2035)</td></tr><tr><td> $Intercept(\beta_1)$ </td><td>1.0187***(0.0167)</td><td>2.2540***(0.0802)</td><td>1.2167***(0.0058)</td><td>2.0932***(0.1224)</td><td>0.8096**(0.3317)</td></tr></table>

Notes: $^ { \star } \mathsf { p } < 0 . 1 , ^ { \star \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star \star } \mathsf { p } < 0 . 0 1$ . Errors are clustered at experimental group level. Models U1–U5 correspond to the following app usage outcome variables: U1: (log) Daily frequency of opening the mHealth app; U2: (log) Daily frequency of documenting activities through the app; U3: Weekly frequency of communications with medical experts; U4: (log) Weekly loyalty rewards earned; U5: (log) Weekly shopping total purchase (\$). #Patients = 1,070; #Observations = 55,359.

Meanwhile, providing additional personalized reminder messages (T3) also leads to a 20.5% and a 39.1% decrease in daily sleeping length, compared to using mHealth app alone (T1) and providing additional non-personalized reminder messages (T2) respectively. Furthermore, when looking into the frequency of late night sleep—when patients went to sleep later than 11 p.m.—we noticed that providing personalized reminder messages in conjunction with the mHealth app can lead to more frequent late night sleep by the patients.

These findings suggest that highly personalized messages may not always work well in trying to persuade patients’ behavioral modifications. As shown in our results, personalization is not as effective as non-personalization if we try to improve diabetes patients’ general life style (i.e., sleeping behavior or movement habits).

This is likely because patients might perceive frequent personalized SMS messages as intrusive and annoying (Pop-Eleches et al. 2011). More importantly, frequent personalized messages might cause patients to feel pressured or coerced by intrapsychic or interpersonal forces, which can significantly demotivate patient behavior from being autonomously selfregulated (Deci and Ryan 1985; Ryan and Deci 2000).

Second, when looking into the app usage as outcome variables (Table 8), we found that overall patients from the three mHealth treatment groups (T1, T2, T3) demonstrated a higher level of usage activities compared to the PC group (C2): opening app and documenting their daily health activities more frequently, more frequent in-app communications with medical experts, and higher loyalty rewards. This finding indicates a strong positive impact of mobile platform on patient engagement with the healthcare technologies. Patients are more likely to engage with the health self-management functions provided in a more flexible setting (i.e., on mobile devices). The accessibility, convenience, and ubiquity inherent to mobile devices help patients easily upload information on a regular basis and follow the guidance that would eventually lead to improved health conditions.

Among the three mHealth treatment groups, the effect appeared to be the strongest when combining the mHealth app with non-personalized reminder messages (T2), followed by the case when using mHealth app alone (T1). Again, we found that providing additional personalized reminder messages can attenuate the mHealth treatment effect and lead to lower app usage by the patients: lower daily frequency of opening app and documenting health activities, lower frequency of communicating with medical experts, and lower loyalty rewards.

This is likely due to patient perceived intrusion, annoyingness and privacy concern (Pop-Eleches et al. 2011). Moreover, frequent personalized messages might cause the patients to feel increased control and judgment. Lack of choiceful and volitional feeling can lead to loss of autonomy and selfmotivation (Deci and Ryan 1985; Ryan and Deci 2000). Correspondingly, it can lead to lower engagement in app usage.

## Mediation Effect of Patient Behavioral Change

In addition to the above analyses, to further test the mediation effect of patient behavioral change on the health outcome, we conducted two additional mediation analyses using (1) a simultaneous equation model and (2) a directed acyclic graph (DAG) in the form of a parametric structural equation model (SEM).<sup>15</sup>

First, we applied a simultaneous equation model to analyze the health outcome and the patient activities simultaneously. More specifically, we model the glucose change (i.e., post experiment–preexperiment) for each patient as a function of individual behavioral activities (i.e., exercises, food intake), demographics, and other control variables $( X _ { i } , \thinspace C _ { i t } ) ;$ in the meantime, we model the individual behavioral activities as a function of mHealth app treatment, while controlling for demographics and other factors $( X _ { i } , C _ { i t } )$

$$
\begin{array}{r l} G l u c o s e C h a n g e _ {i t} & = \gamma_ {0} + \gamma_ {1} B e h a v i o r a l A c t i v i t i e s _ {i t} \\ & + X _ {i} \gamma_ {2} + C _ {i t} \gamma_ {3} + \omega_ {i t} \end{array}\tag{[3]}
$$

$$
\begin{array}{r l} \text { BehavioralActivities } _ {i t} & = \alpha_ {0} + \alpha_ {1} \text { Treatment } _ {i} \\ & + X _ {i} \alpha_ {2} + C _ {i t} \beta \alpha_ {3} + \mu_ {i t} \end{array}\tag{[4]}
$$

We provide the results in Tables 9 and 10. As we can see from this analysis, the effects of mHealth adoption (T1, T2, T3) demonstrate a statistically significant impact on increasing patients’ exercises and decreasing patients’ food calories intake, which in turn, leads to a lower blood glucose over time.

Second, we built a directed acyclic graph (DAG) in the form of a parametric structural equation model (SEM) to test the causal path of the mHealth impact on patient health outcome through the behavioral modification. In particular, we empirically test whether there is a statistically significant impact of mHealth adoption through the mediation effect of individual behavioral activities (i.e., exercises, food intake). We provide the estimation results in Figures 1 and 2.

In Figure 1, C1 is dropped out of the model (hence no coefficient estimated associated with the arrow) because no behavioral activities were observed for this group. C2 is dropped out of the model because it is used as the baseline. The effects of mHealth adoption (T1, T2, T3) are highly consistent with our main analyses, demonstrating a statistically significant and positive impact on patients’ exercise activities (with the estimated coefficients 0.81, 0.88, and 0.26, respectively), which in turn, leads to a lower blood glucose over time (with the estimated coefficient -0.14). We also found a consistent trend where the combination of non-personalized SMS (T2) was the most effective, whereas the personalized SMS (T3) was the least effective.

We also conducted similar empirical test for the causal mediation effect of “Food Intake” and found consistent trend. As we see in Figure 2, the effects of mHealth adoption (T1, T2, T3) demonstrate a statistically significant and negative impact on patients’ food calories intake (with the estimated coefficients -0.4, -0.26, and -0.21, respectively). In the meantime, lower food calories intake leads to a lower blood glucose over time (with the estimated coefficient 0.19).

Overall, we found that the two additional mediation analyses using the simultaneous equation model and the directed acyclic graph (DAG) have demonstrated highly consistent evidence with our main results. They further support the causal impact of mHealth adoption on the health outcome, through the mediation effect of patient behavioral change.

## Additional Follow-Up Survey and Interview

To further verify our findings, we conducted an additional round of follow-up survey and interview. We provide the details in Appendix E. We asked the participants three major questions:

(1) What is your favorite function of the blood glucose management mobile app?

(2) How did these functions help improve your health?

(3) For participants in T3, what is your feedback regarding the personalized text messages about medical guidance based on your personal exercise, diet and health status?

Based on the survey user responses, the most useful app func tion liked by the users is “Learning about health knowledge (68%),” followed by “Health real-time tracking: blood glucose, exercise, drug, diet (67%),” “Personalized diabetes risk assessment (61%),” “Doctor consultation (53%),” and “Social network support (48%).”

<table><tr><td colspan="2">Table 9. Estimation Results Using Simultaneous Equation Model: Exercise and Glucose</td></tr><tr><td></td><td>Coef. (Std. Err.) $^{v}$ </td></tr><tr><td colspan="2">Glucose Change (Post – Pre)</td></tr><tr><td>Exercise Calories (log)</td><td>-0.6935***(0.0974)</td></tr><tr><td>Intercept</td><td>10.8099***(1.7367)</td></tr><tr><td colspan="2">Patient -Specific Control Variables</td></tr><tr><td>Age, Married, Gender, Income, Prior Glucose, Prior Hemoglobin, Prior Medication, Other Disease, Complication, Smoking/Drinking, Pregnant, Diabetes Type, Interaction with Physicians. Diabetes Age, average Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td></tr><tr><td>Exercise Calories (log)</td><td></td></tr><tr><td>T1</td><td>0.2148***(0.0551)</td></tr><tr><td>T2</td><td>0.2498**(0.1232)</td></tr><tr><td>T3</td><td>0.1661***(0.0678)</td></tr><tr><td>Intercept</td><td>5.0485***(0.1348)</td></tr><tr><td colspan="2">Patient -Specific Control Variables</td></tr><tr><td>Age, Married, Gender, Income, Prior Glucose, Prior Hemoglobin, Prior Medication, Other Disease, Complication, Smoking/Drinking, Pregnant, Diabetes Type, Interaction with Physicians. Diabetes Age, average Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td></tr></table>

Note: \*p < 0.1, $^ { \star \star } \mathsf { p } < 0 . 0 5$ $\star \star \star _ { \mathsf { p } } < 0 . 0 1$ . #patients = 1,070, #observations = 9,251.

<table><tr><td colspan="2">Table 10. Estimation Results Using Simultaneous Equation Model: Food Intake and Glucose</td></tr><tr><td></td><td>Coef. (Std. Err.)</td></tr><tr><td colspan="2">Glucose Change (Post – Pre)</td></tr><tr><td>Food Calories Intake (log)</td><td>0.3760***(0.1258)</td></tr><tr><td>Intercept</td><td>7.5798***(1.4316)</td></tr><tr><td colspan="2">Patient -Specific Control Variables</td></tr><tr><td>Age, Married, Gender, Income, Prior Glucose, Prior Hemoglobin, Prior Medication, Other Disease, Complication, Smoking/Drinking, Pregnant, Diabetes Type, Interaction with Physicians. Diabetes Age, average Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td></tr><tr><td colspan="2">Food Calories Intake (log)</td></tr><tr><td>T1</td><td>-0.5664***(0.1540)</td></tr><tr><td>T2</td><td>-0.8825***(0.1402)</td></tr><tr><td>T3</td><td>-0.2134***(0.0251)</td></tr><tr><td>Intercept</td><td>-6.9580***(2.0145)</td></tr><tr><td colspan="2">Patient -Specific Control Variables</td></tr><tr><td>Age, Married, Gender, Income, Prior Glucose, Prior Hemoglobin, Prior Medication, Other Disease, Complication, Smoking/Drinking, Pregnant, Diabetes Type, Interaction with Physicians. Diabetes Age, average Daily App Usage (daily frequency of opening the app, daily frequency of documenting activity logs, weekly frequency of communications, weekly loyalty rewards and other in-app engagement like shopping).</td><td>Yes</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01. #patients = 1,070, #observations = 9,251.

![](/api/attachments/76D8ZPZM/fulltext/images/28e29070b7b6521fd23fd213daef13d7bdbf8348b19763d470013ad5d5765199.jpg)  
Figure 1. Directed Acyclic Graph (DAG) to Test the Mediation Effect of Exercise on Post-Experiment Blood Glucose Change

![](/api/attachments/76D8ZPZM/fulltext/images/df8390a6983c9b778e7ec54e7dca62ffb735909db104e8e613cad6a9ffca0927.jpg)  
Figure 2. Directed Acyclic Graph (DAG) to Test the Mediation Effect of Food Intake on Post-Experiment Blood Glucose Change

When being asked how these functions helped improve their health, a large majority of the users mentioned that the app provided them a way to better monitor and “quantify” their life and health in real time, hence they were able to better manage food intake and exercise. For example, “The combination of my blood glucose level and exercise diet allows me to understand the relationship between them clearly, which motivates me to exercise more and eat healthier food” and “Self-tracking of health status provides a quantitative basis in real time, and thus improves my health level.”

Regarding the personalized text message about medical guidance, users raised three major concerns: (1) Interruption and annoyingness (58%), (2) Avoidance toward negative information (54%), and (3) Privacy (53%).

In addition to the survey responses, we have also conducted in-depth phone interviews with a randomly selected group of seven experimental users from T3 treatment group. The main purpose of the interview was to further verify the survey responses, and meanwhile with a focus on why the personalized text messages did not work well.

We found the responses from the interview were highly consistent with those from the survey. When the participants were asked what functions they liked the most, all seven interview participants indicated that the real-time health tracking function provided them a way of better monitoring and managing their health. They (and their family members) have also gained professional health knowledge through using the app.

When the participants were asked whether they liked the personalized medical guidance via text messages and why, a majority of them (six out of seven) indicated that they found these personalized text messages “too frequent,” “annoying,” and violating “privacy.”

Interestingly, during our interview, one of the participants explicitly mentioned his/her preference of a less personalized text message to avoid “being judged all the time by someone.” This is highly consistent with our previous finding that frequent personalized messages might cause the patients to feel increased control and judgment. They can in tern lead to a significant decrease in patient intrinsic motivation of disease self-management and a lower health outcome.

## Summary of Findings and Managerial Implications

Overall, our further analyses on patient glucose values, behavioral activities and app usage, together with the additional survey and interview, demonstrate highly consistent evidence that mobile health app platforms have a statistically significant impact on empowering patients with diabetes selfmanagement, reducing patients’ glucose values, improving their life style and health outcomes over time. Our results also provide strong evidence of the underlying behavioral mechanism that drives the observed health outcome.

Specifically, first, we find the adoption and usage of the mHealth platform has a significant impact on improving diabetes patient health outcomes as well as reducing medical costs. Second, between web-based and mobile-based platforms, we find a strong device effect: the mobile interventions led to a statistically significantly higher impact than the web-based intervention. Third, the mHealth platform also demonstrates a significantly stronger impact on patients’ dietary and life style improvement as well as engagement with app usage than does the web-based platform. This finding suggests that patients in the mHealth treatment groups indeed became more engaged, motivated, and autonomously selfregulated with their health behavior over time. Such increased intrinsic motivation can in turn lead to an improvement in their health outcomes (e.g., glucose values, hospital visits). This insight is critical. It provides strong evidence of the underlying mechanism that drives the observed health outcome, demonstrating the potential of mHealth in empowering diabetes patients for efficient health management.

Furthermore, in conjunction with patient self-management through the mHealth platform, we find heterogeneous effects between personalized and non-personalized messages. Interestingly, paired with all the health-management functions and resources provided by the mHealth platform, nonpersonalized SMS messages demonstrate on average the highest effect on reducing patient glucose over time. In contrast, personalization is not as effective as non-personalization if we try to improve diabetes patients’ engagement with the app usage or general life style (i.e., sleeping behavior or movement habits). This is likely due to patient perceived intrusion, annoyingness and privacy concern (Pop-Eleches et al. 2011). Furthermore, frequent personalized messages might cause the patients to feel increased control and judgment. They might cause patients to feel pressured or coerced by intrapsychic or interpersonal forces. We have seen such evidence in both our experimental analyses and our additional follow-up survey and interview (Appendix E).

Our finding is also highly consistent with prior research on self-determination theory (SDT) and cognitive evaluation theory (CET). Prior theoretical literature has demonstrated that lack of choiceful and volitional feeling can lead to loss of autonomy and self-motivation (Deci and Ryan 1985; Ryan and Deci 2000). It in turn can lead to a significant decrease in patient intrinsic motivation of self-management, demotivating patient behavior from being autonomously selfregulated in health. Such loss of autonomy can lead to lower patient engagement in the health self-management process (e.g., lower mHealth app usage, lower patient–physician engagement, lower compliance to medication and treatment). Also, prior research showed that pressured evaluations and imposed goals diminish intrinsic motivation because they conduce toward an external perceived locus of causality. In contrast, choice, acknowledgment of feelings, opportunities for self-direction, and positive social-contextual events (e.g., feedback, communications, rewards) were found to enhance intrinsic motivation because they allow people a greater feeling of autonomy and competence (Deci and Ryan 1985). In sum, these findings are surprising and suggest frequent personalized mobile messaging may undermine the effectiveness of mHealth technology. The design of the mHealth platform, and health IT in general, is critical in achieving better patient engagement and health outcomes.

Our findings have several important implications. From the healthcare provider’s perspective, our study illustrates the importance of mHealth technology in facilitating diabetes patient self-management to improve well-being and health outcomes through behavioral modifications over time. Importantly, mHealth technology has shown great potential to improve patients’ compliance: following diets and executing life style changes that coincide with healthcare providers recommendations for health and medical advice.

From the mHealth platform designer’s perspective, our study suggests the design of the mHealth platform is critical in achieving better patient engagement, empowerment, and health outcomes. Instead of personalized messaging, mHealth applications should be paired with non-personalized messaging with general knowledge about disease management for patient education. Our research also provides important design guidance for supporting communication and shared decision making via reminders, notifications and informed guidance, and improving care delivery operations to increase satisfaction and quality of care.

Finally, from the policy maker’s perspective, our findings demonstrate the potential of mHealth technologies in improving healthcare delivery to significantly impact outcomes, quality and costs. Our study also significantly improves the understanding of issues that interfere with patients’ sustained engagement with mHealth apps and population adherence to treatment and wellness regimens. It provides key insights in the underlying mechanisms that drive individual and population health behaviors and life style changes through mHealth app, and, moreover, the critical policy implications regarding the adoption and sustained usage of mHealth technologies.

## Robustness Analyses

We conducted several robustness analyses to check the validity of our experimental design and data quality. We discuss them in this section.

## Long Recruitment Window

The rolling recruitment process in our study lasted for 7 months. To guarantee that such long window would not introduce any confounding factors caused by time trend, first we have considered a time fixed effect in the individual-level Diff-in-Diff analysis (Time\_t, coded as the time sequence index of patient glucose upload time) to control for any individual-level time trend. Moreover, in the analysis we have also controlled for the glucose type (before/after breakfast/lunch/dinner/sleep), the actual time, day and month indicators for the glucose upload time. This aims to control for any potential common time-of-day or seasonality effects for the entire population.

To further alleviate the concern, we have conducted an additional subsample analysis by selecting a subset of control and treatment groups who were recruited into our experiment during the same month. In particular, we focused on only those patients who were recruited in May 2015 (i.e., we chose the first month of the recruitment period to also minimize any potential risk of sample contamination). This led to a subsample of 285 patients: C1 (n = 49), C2 (n = 63), T1 (n = 57), T2 (n = 64), T3 (n = 52). We then conducted Diff-in-Diff analysis to compare the group means in the glucose change based on this subsample. Overall, our findings remain highly consistent based on the subsample analysis. The detailed results are provided in Table 11.

## Sample Dropout

Indeed, high patient dropout rate is a common challenge in medical trials (e.g., Gupta et al. 2015). To alleviate any additional concern toward this issue, we conducted two levels of analyses. First, we compared the distributions of participants’ demographic and baseline health-related characteristics between the dropout samples and the eligible samples. Based on a Welch’s t-test, we could not reject the null hypothesis that there is no statistically significant difference between the two samples. The results are provided in Table 12.

Second, we compared the distributions of participants’ demographic and baseline health-related characteristics among all the dropout samples across the five experimental groups. We then conducted one-way ANOVA test and could not reject the null hypothesis that all the five groups are from the same sample distribution. The detailed results are provided in Table 13.

The results from the above two tests show that although dropout rate is non-negligible (\~15%) in our study, the distribution of dropout samples remains quite consistent with that of the eligible samples, and moreover, the distribution of dropout samples remains quite consistent across the five experimental groups (i.e., missing data at random). Therefore, while we acknowledge this fact as one potential data limitation in our study, we are more confident that it is not a serious concern in affecting our results.

## Validity Check for Self-Reported Data

Because medical information is sensitive, the accuracy of selfreported data is important for the validity of the results. We have validated our data using a multi-pronged approach.

First, our mHealth app partner provided an internal (full-time) medical expert team who helped review and validated the information about our experimental participants during the entire experimental period. In particular, as part of the risk assessment function, the internal medical team will communicate with each patient in person (mostly through phone calls) at least once every 3 months to carefully go over the historical (self-reported) records and the corresponding algorithm-generated diabetes risk score with the patient to better explain and validate the results. This validity check was done for all patients in C2, T1, T2, and T3 groups (who had access to the entire app functions through either PC or mobile devices). For patients in C1 group (who did not have access to the app), we checked the validity of their selfreported information during the surveys. In particular, during the phone calls we went through all the self-reported glucose values with them and validate their answers in person.

Second, during pre- and post-treatment surveys we purposely asked the same set of questions regarding the demographics and historical medical conditions. This to some extent helped cross validate the accuracy of the information (i.e., it is less likely a person will remember exactly what he/she said 8 months ago if that was a lie). In addition, the surveys were conducted through phone calls. The spontaneous in-person conversation also helped our researchers to spot anything suspicious (e.g., an obvious lie).

Third, from an experimental design perspective, because our participants were fully randomized into the experimental groups, even if any potential noise might exist in the individual data, such noise effect would be minor and likely to cancel out across the experimental groups due to randomization.

Table 11. Subsample Analysis (Patients Recruited in May 2015)

<table><tr><td>Treatment Group</td><td>Diff- Glucose</td><td>Diff-Hemoglobin</td><td>Diff-Hospital Visits (Recent 3 Months)</td><td>Diff-Spending (Recent 3 Months, USD)</td></tr><tr><td>C1 (n = 49)</td><td>-0.0338</td><td>-0.0149</td><td>-0.0297</td><td>-0.88</td></tr><tr><td>C2 (n = 63)</td><td>-0.5202</td><td>-0.1943</td><td>-0.0601</td><td>-5.62</td></tr><tr><td>T1 (n = 57)</td><td>-0.6312</td><td>-1.0307</td><td>-0.1319</td><td>-9.69</td></tr><tr><td>T2 (n = 64)</td><td>-0.6978</td><td>-1.1588</td><td>-0.1443</td><td>-14.70</td></tr><tr><td>T3 (n = 52)</td><td>-0.5889</td><td>-0.9576</td><td>-0.2098</td><td>-29.63</td></tr></table>

Note: Values are calculated based on the difference between the two surveys (post-treatment value minus pre-treatment value). Glucose value is calculated based on an average across all glucose types. p < 0.05 (ANOVA).

Table 12. Comparison of Main Variables between Eligible Samples and Dropout Samples

<table><tr><td></td><td colspan="2">Eligible Samples</td><td colspan="2">Dropout Samples</td><td rowspan="2">t-test</td></tr><tr><td>Variable</td><td>Mean</td><td>Std.</td><td>Mean</td><td>Std.</td></tr><tr><td>Male</td><td>0.65</td><td>0.47</td><td>0.63</td><td>0.49</td><td>t = 1.39 (p &gt; 0.05)</td></tr><tr><td>Age</td><td>55.17</td><td>8.91</td><td>54.01</td><td>8.82</td><td>t = 1.93 (p &gt; 0.05)</td></tr><tr><td>Married</td><td>0.83</td><td>0.39</td><td>0.79</td><td>0.35</td><td>t = 1.65 (p &gt; 0.05)</td></tr><tr><td>Income</td><td>76827.27</td><td>12258.67</td><td>75403.57</td><td>13179.28</td><td>t = 1.62 (p &gt; 0.05)</td></tr><tr><td>Pre-meal Glucose</td><td>7.23</td><td>1.83</td><td>7.32</td><td>1.92</td><td>t = 1.61 (p &gt; 0.05)</td></tr><tr><td>Post-meal Glucose</td><td>9.86</td><td>4.36</td><td>9.95</td><td>4.22</td><td>t = 0.68 (p &gt; 0.05)</td></tr><tr><td>Hemoglobin</td><td>6.72</td><td>1.98</td><td>6.81</td><td>1.87</td><td>t = 1.49 (p &gt; 0.05)</td></tr><tr><td>Diabetes Age</td><td>5.40</td><td>5.14</td><td>5.11</td><td>5.02</td><td>t = 1.85 (p &gt; 0.05)</td></tr></table>

Eligible samples: #patients $\mathsf { n } = 1 , 0 7 0 .$ Dropout Samples: #patients ${ \mathsf n } = 2 7 3$

Table 13. Comparison of Main Variables among Dropout Samples across Five Experimental Groups

<table><tr><td></td><td>C1</td><td>C2</td><td>T1</td><td>T2</td><td>T3</td><td rowspan="2">ANOVA</td></tr><tr><td>Variable</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td></tr><tr><td>Male</td><td>0.65</td><td>0.64</td><td>0.63</td><td>0.65</td><td>0.66</td><td>p &gt; 0.05</td></tr><tr><td>Age</td><td>55.21</td><td>54.68</td><td>54.14</td><td>54.79</td><td>55.02</td><td>p &gt; 0.05</td></tr><tr><td>Married</td><td>0.83</td><td>0.81</td><td>0.80</td><td>0.81</td><td>0.79</td><td>p &gt; 0.05</td></tr><tr><td>Income</td><td>76809.0</td><td>76092.0</td><td>75631.0</td><td>75395.0</td><td>78909.0</td><td>p &gt; 0.05</td></tr><tr><td>Pre-meal Glucose</td><td>7.21</td><td>7.27</td><td>7.32</td><td>7.24</td><td>7.36</td><td>p &gt; 0.05</td></tr><tr><td>Post-meal Glucose</td><td>9.89</td><td>9.82</td><td>9.91</td><td>9.94</td><td>9.86</td><td>p &gt; 0.05</td></tr><tr><td>Hemoglobin</td><td>6.78</td><td>6.72</td><td>6.80</td><td>6.83</td><td>6.79</td><td>p &gt; 0.05</td></tr><tr><td>Diabetes Age</td><td>5.38</td><td>5.25</td><td>5.16</td><td>5.21</td><td>5.19</td><td>p &gt; 0.05</td></tr></table>

Sample Size: C1 (n = 97), C2 (n = 92), T1 (n = 23), T2 (n = 35), T3 (n = 26)

Therefore, based on the above efforts, we are confident about the validity of our data and the accuracy of our final results.

## Conclusion and Future Directions

In this paper, we have examined the mHealth ecosystem and its health and economic impacts on diabetes patient outcomes. To achieve our goal, we partnered with a firm in Asia that provides the nation’s largest mobile health app platform that specializes in diabetes care. We have designed and implemented a large-scale, randomized field experiment based on unique observations from diabetes patients over several months.

Our research demonstrates that adoption of the mHealth platform has a statistically significant impact on improving patients’ dietary and life style, leading to a reduction in patients’ blood glucose, hospital visits, and medical expenses over time. We also find heterogeneous effects between personalized and non-personalized messages. Interestingly, non-personalized mobile messages with general diabetes care guidance demonstrate a stronger impact on patient engagement with the app, behavior and life style change, and health improvement. While personalized mobile messages show a smaller impact on the above, they are more likely to encourage a substitution of offline or in-person interactions with telehealth. Our study indicates the mHealth apps have great potential in improving patients’ health outcomes by assisting them with behavior modification and chronic disease selfmanagement. It also provides important insights into the design of such mHealth platforms in transforming healthcare by substituting offline physician visits with telehealth and telemedicine.

On a broader note, our research significantly improves our understanding of human behavior and interactions with smart and connected mHealth platforms, and broadly in the consumer Internet of Things. Digital health platform infrastructures are often the manifestation of complex technological and social systems (Eisenmann et al. 2011) and can have profound implications on social and economic transactions. However, how humans interact with the mHealth infrastructures is not as well understood. Our study provides important managerial insights on issues that may influence individuals’ sustained engagement with mobile and wearable technologies, health and wellness, adherence to treatment and wellness regimens, and patient welfare. It improves our understanding of the key mechanisms that drive individual health and wellness behavior and lifestyle changes through mobile technologies. Finally, it provides critical policy implications regarding the design of smart digital health platforms through effective, sustained usage of these emerging technologies.

Our paper has some limitations, which can serve as fruitful areas for future research. First, in our data sample, the majority of the diabetes patients have type 2 diabetes (approximately 98%). Although type 2 diabetes accounts for approximately 90% to 95% of all diagnosed cases of diabetes,<sup>16</sup> an examination of the mHealth impact on other types of diabetes with a larger sample in future would be useful.

Second, in this study, we have evaluated the mHealth app as a bundle of all the major functions. However, breaking down the overall application into different functional components (e.g., behavior tracking, risk assessment and personalized solution, Q&A, and patient community) and examining the health and economic impacts from each of them separately would be interesting. It would also be interesting to examine the impact of personalized reminders when the messages are positive versus negative as people may react differently to positive than to negative sentiments.

Third, in this paper, we have not considered the potential impact related to the textual content of patient–physician communications, mainly because of potential privacy concerns blocking access to the textual content of the personal communications. However, based on our conversation with the platform, we believe these patient–physician communications are highly professional and provide similar quality in medical guidance. In addition, in our analyses, we are able to control the frequency of the patient–physician communications.

Finally, our research focuses on the context of diabetes care management. The methodologies and insights have the potential to be generalized to other chronic disease and wellnesscare contexts. However, examining other medical scenarios to compare the relationship and heterogeneity in the impact of the mHealth platform on patient behavior and outcomes under different healthcare contexts would be interesting and important for future research.

## Acknowledgments

We thank seminar participants in Harvard University, University of Washington, University of British Columbia, University of Georgia, Dartmouth College, CMU-Pitt Seminar series, Boston University, and conference participants at MIT CODE for their helpful comments that have improved the paper. Anindya Ghose and Beibei Li thank the National Science Foundation for supporting this research through an NSF-EAGER grant.

## References

Agarwal, R., Gao, G., DesRoches, C., and Jha, A. K. 2010. “Research Commentary—The Digital Transformation of Healthcare: Current Status and the Road Ahead,” Information Systems Research (21:4), pp. 796-809.

Agarwal, R., and Khuntia, J. 2009. “Personal Health Information Management and the Design of Consumer Health Information Technology,” ARQH Publication No. 09-0075-EF, Rockville, MD: Agency for Healthcare Research and Quality.

Allegrante, J. P., Wells, M. T., and Peterson, J. C. 2019. “Interventions to Support Behavioral Self-Management of Chronic Diseases,” Annual Review of Public Health (40), pp. 127-146.

Allen, J. K., Stephens, J., Dennison Himmelfarb, C. R., Stewart, K. J., and Hauck, S. 2013. “Randomized Controlled Pilot Study Testing Use of Smartphone Technology for Obesity Treatment,” Journal of Obesity (2013), Article ID 151597.

American Diabetes Association. 2018. “Economic Costs of Diabetes in the U.S. in 2017,” Diabetes Care (45:1), pp. 917-928.

Anderson, C. L., and Agarwal, R. 2011. “The Digitization of Healthcare: Boundary Risks, Emotion, and Willingness to Disclose Personal Health Information,” Information Systems Research (22:3), pp. 469-490.

Aral, S., and Walker, D. 2011. “Creating Social Contagion Through Viral Product Design: A Randomized Trial of Peer Influence in Networks,” Management Science (57:9), pp. 1623-1639.

Bardhan, I., Oh, J. H., Zheng, Z., and Kirksey, K. 2015. “Predictive Analytics for Readmission of Patients with Congestive Heart Failure,” Information Systems Research (26:1), pp. 19-39.

Bardhan, I. R., and Thouin, M. F. 2013. “Health Information Technology and its Impact on the Quality and Cost of Healthcare Delivery,” Decision Support Systems (55:2), pp. 438-449.

Deci, E. L., and Ryan, R. M. 1985. “Conceptualizations of Intrinsic Motivation and Self-Determination,” in Intrinsic Motivation and Self-Determination Human Behavior, Boston: Springer, pp. 11-40.

Eisenmann, T., Parker, G., and Van Alstyne, M. 2011. “Platform Envelopment,” Strategic Management Journal (32:12), pp. 1270-1285.

Estrin, D., and Sim, I. 2010. “Open mHealth Architecture: An Engine for Health Care Innovation.” Science (330:6005), pp. 759-760.

Free, C., Phillips, G., Galli, L., Watson, L., Felix, L., Edwards, P., Patel, V., and Haines, A. 2013. “The Effectiveness of Mobile-Health Technology-Based Health Behavior Change or Disease Management Interventions for Health Care Consumers: A Systematic Review,” PLoS Med (10:1), e1001362.

Gao, G., McCullough, J., Agarwal, R., and Jha, A. 2010. “A Study of Online Physician Ratings by Patients,” Working Paper, R. H. Smith School of Business, University of Maryland, College Park.

Ghose, A. 2017. Tap: Unlocking the Mobile Economy, Cambridge, MA: MIT Press.

Ghose, A., Goldfarb, A., and Han, S. P. 2013. “How Is the Mobile Internet Different? Search Costs and Local Activities,” Information Systems Research (24:3), pp. 613-631.

Ghose, A., Ipeirotis, P. G., and Li, B. 2014. “Examining the Impact of Ranking and Consumer Behavior on Search Engine Revenue,” Management Science (60:7), pp. 1632-1654.

Goldfarb, A., and Tucker, C. 2011. “Online Display Advertising: Targeting and Obtrusiveness,” Marketing Science (30:3), pp. 389-404.

Gupta, A., Calfas, K. J., Marshall, S. J., Robinson, T. N., Rock, C. L., Huang, J. S., Epstein-Corbin, M., Servetas, C., Donohue, M. C., Norman, G. J., Raab, F., Merchant, G., Fowler, J. F., Griswold, W. G., Fogg, B. J., and Patrick, K. 2015. “Clinical Trial Management of Participant Recruitment, Enrollment, Engagement, and Retention in the SMART Study Using a Marketing and Information Technology (MARKIT) Model,” Contemporary Clinical Trials (42:), pp. 195-195.

Harle, C. A., Downs, J. S., and Padman, R. 2012. “Effectiveness of Personalized and Interactive Health Risk Calculators: A Randomized Trial,” Medical Decision Making (32:4), pp. 594-605.

Hoyle, R. H., Harris, M. J., and Judd, C. M. 2001. Research Methods in Social Relations (7<sup>th</sup> ed.), Boston: Cengage Learning.

Jung, J., Bapna, R., Ramaprasad, J., and Umyarov, A. 2019. “Love Unshackled: Identifying the Effect of Mobile App Adoption in Online Dating,” MIS Quarterly (43:1), pp. 47-72.

Kane, G., Fichman, R. G., Gallaugher, J., and Glaser, J. 2009. “Community Relations 2.0,” Harvard Business Review (87:11), pp. 45-50.

Kato-Lin, Y. C., Abhishek, V., Downs, J., and Padman, R. 2016. “Food for Thought: The Impact of m-Health Enabled Interventions on Eating Behavior,” Working Paper, SSRN (https://dx.doi.org/10.2139/ssrn.2736792).

Kim Yeary, K. H-C., Long, C. R., Bursac, Z., and McElfish, P. A. 2017. “Design of a Randomized, Controlled, Comparative– Effectiveness Trial Testing a Family Model of Diabetes Self-Management Education (DSME) vs. Standard DSME for Marshallese in the United States,” Contemporary Clinical Trials Communications (6), pp. 97-104.

Klein, W. M., and Stefanek, M. E. 2007. “Cancer Risk Elicitation and Communication: Lessons from the Psychology of Risk Perception,” CA: A Cancer Journal for Clinicians (57:3), pp. 147-67.

Lancaster, K., Abuzour, A., Khaira, M., Mathers, A., Chan, A., Bui, V., Lok, A., Thabane, L., and Dolovich, L. 2018. “The Use and Effects of Electronic Health Tools for Patient Self-Monitoring and Reporting of Outcomes Following Medication Use: Systematic Review,” Journal of Medical Internet Research (20:12), e294.

Lester, R.T., Ritvo, P., Mills, E. J., Kariri, A., Karanja, S., Chung. M. H., Jack, W., Habyarimana, J., Sadatsafavi, M., Najafzadeh, M., Marra, C. A., Estambale, B., Ngugi, E., Ball, T. B., Thabane, L., Gelmon, L. J., Kimani, J., Ackers, M., and Plummer, F. A. 2010. “Effects of a Mobile Phone Short Message Service on Antiretroviral Treatment Adherence in Kenya (WelTel Kenya1): A Randomised Trial,” The Lancet (376:9755), pp. 1838-1845.

Liu, X., Zhang, B., Susarla, A., and Padman, R. 2020. “Go to You Tube and Call Me in the Morning: Use of Social Media for Chronic Conditions,” MIS Quarterly (44:1), pp. 275-283.

Manyika, J., Chui, M., Bughin, J., Dobbs, R., Bisson, P., and Marrs, A. 2013. “Disruptive Technologies: Advances That Will Transform Life, Business, and the Global Economy,” Report, McKinsey Global Institute.

Martin, C. K., Miller, A. C., Thomas, D. M., Champagne, C. M., Han, H., and Church, T. 2015. “Efficacy of SmartLossK, a Smartphone-Based Weight Loss Intervention: Results from a Randomized Controlled Trial,” Obesity (23:5), pp. 935-942.

Myerson, R. M., Colantonio, L. D., Safford, E. M., and Huang, E. S. 2018. “Does Identification of Previously Undiagnosed Conditions Change Care Seeking Behavior?,” Health Services Research (53:3), pp. 1517-1538.

Nollen, N. L., Mayo, M. S., Carlson, S. E., Rapoff, M. A., Goggin, K. J., and Ellerbeck, E. F. 2014. “Mobile Technology for Obesity Prevention: A Randomized Pilot Study in Racial- and Ethnic-Minority Girls,” American Journal of Preventative Medicine (46:4), pp. 404-408.

Pop-Eleches, C., Thirumurthy, H., Habyarimana, J. P., Zivin, J. G., Goldstein, M. P., de Walque, M., MacKeen, L., Haberer, J., Kimaiyo, S., Sidle, J., Ngare, D., and Bangsberg, D. R. “Mobile Phone Technologies Improve Adherence to Antiretroviral Treatment in a Resource-Limited Setting: A Randomized Controlled Trial of Text Message Reminders,” AIDS (25:6), pp. 825-834.

Rossi, M. C., Nicolucci, A., Pellegrini, F., Bruttomesso, D., Bartolo, P. D., Marelli, G., Dal Pos, M., Galetta, M., Horwitz, D., and Vespasiani, G. 2009. “Interactive Diary for Diabetes: A Useful and Easy-to-Use New Telemedicine System to Support the Decision-Making Process in Type 1 Diabetes,” Diabetes Technology & Therapeutics (11:1), pp. 19-24.

Ryan, R. M., and Deci, E. L. 2000. “Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being,” American Psychologist (55:1), pp. 68-78.

Uetake, K., and Yang, N. 2017. “Success Breeds Success: Weight Loss Dynamics in the Presence of Short-Term and Long-Term Goals,” Working Paper No. 170002, Canadian Centre for Health Economics, Toronto.

Wang, Q., Li, B., and Wang, P. 2016. “Using TB-Sized Data to Understand Multi- Device Advertising,” in Proceedings of 37<sup>th</sup> International Conference on Information Systems, Dublin.

Wang, Y., Xue, H., Huang, Y., Huang, L., and Zhang, D. 2017. “A Systematic Review of Application and Effectiveness of mHealth Interventions for Obesity and Diabetes Treatment and Self-Management,” Advances in Nutrition (8:3), pp. 449-462.

Watson, J. M., and Torgerson, D. J. 2006. “Increasing Recruitment to Randomised Trials: A Review of Randomised Controlled Trials,” BMC Medical Research Methodology (6:34).

Xu, K., Chan, J., Ghose, A., and Han, S. 2017. “Battle of the Channels: The Impact of Tablets on Digital Commerce,” Management Science (63:5), pp. 1469-1492.

Yan, L. 2020. “The Kindness of Commenters: An Empirical Study of the Effectiveness of Perceived and Received Support for Weight-Loss Outcomes,” Production and Operations Management (29:6), pp. 1448-1466.

Yan, L., and Tan, Y. 2014. “Feeling Blue? Go Online: An Empirical Study of Online Supports among Patients,” Information Systems Research (25:4), pp. 690-709.

## About the Authors

Anindya Ghose is the Heinz Riehl Chair Professor of Business at NYU Stern School. He is the author of TAP: Unlocking the Mobile Economy and a recipient of the INFORMS ISS Distinguished Fellow Award. In 2014, he was named by Poets & Quants as one of the “Top 40 Professors Under 40.” In 2017, he was recognized by Thinkers50 as one of the “Top Management Thinkers.” In 2019, he was recognized by Web of Science in the top 1% of researchers. His research has received 16 best paper awards and nominations. He has consulted to many firms globally on realizing business value from digital investments. In 2020 he received the inaugural INFORMS ISS Practical Impact award. He is currently serving as a department editor for Management Science.

Xitong Guo is a professor of Information Systems and the executive director of eHealth research institute at the school of Management in Harbin Institute of Technology. His research focuses on eHealth. His research has appeared in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, among others. Xitong thanks the National Natural Science Foundation of China (72071054, 72125001) for its support for this study.

Beibei Li is the Anna Loomis McCandless Chair and Associate Professor of IT & Management at the H. John Heinz III College of Carnegie Mellon University. She has extensive experience at leveraging large-scale observational data analytics and experimental analysis with a strong focus on modeling individual user behavior across online, offline and mobile channels for decision support. She is the winner of several best paper awards and is recipient of over \$3M research awards and grants. Beibei has won the INFORMS ISS Sandy Slaughter Early Career Award. She is also the winner of the INFORMS ISS Nunamaker-Chen Dissertation Award and the ACM SIGMIS Best Doctoral Dissertation Award.

Yuanyuan Dang is an assistant professor in the Department of Industrial Engineering at South China University of Technology’s School of Business Administration. She pushes the envelope and seeks new research opportunities enabled by the central use, implementation, design, and diffusion of human-centered IT artifacts, especially in healthcare.

![](/api/attachments/76D8ZPZM/fulltext/images/7f44f297e7e9bbd211b8a841d0e6b430ded0931ceb99e687958201dee7985090.jpg)

## (b) Adding a New Blood Glucose Value

## Appendix A

Screenshots of Mobile/Web Interfaces  
![](/api/attachments/76D8ZPZM/fulltext/images/657da0b854ef3897413050c9521cf96c26dcab40afe1c986049b07503d7036e5.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/701297f58c12722f68581de5fa3a0c15e7b10120dfcb6198fc5d91c0870b5d96.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/30e939074753e8b820bc4a1716740ab0d9dc971fb7f779cc2bcb774c29c1f939.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/5f3ffbfbaafe6fa7b36a733620e013eebf3ec81b6c13145cffa3345e3a49fcde.jpg)

(a) Overview of User Homepage  
![](/api/attachments/76D8ZPZM/fulltext/images/730a534c28ff9eda36234cc2b61ce06153124240254b19493129b180be89c242.jpg)

## (c) User Behavior Tracking Over Time (from left to right: Glucose, Blood pressure, Diet, and Exercise (Sports))

## Figure A1. Screenshots of the Main App Functions

![](/api/attachments/76D8ZPZM/fulltext/images/f4cd6b9393539a571a85cf38a5b2458e48f6562e05843c759ceb00d6714908f8.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/f8e77f7cbb2233065cd93dac515dedf088ee599cae14f3e162028f1366f48b9c.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/013e411af5bb6c71d223c144a9a657313f6f97d4e4df0c7a58e38c2c37ced8ed.jpg)

## Figure A2. Screenshot of the Web Portal for Control Group C1 to Upload the Blood Glucose and Hemoglobin Values at the Beginning and End of the Month Treatment Period

![](/api/attachments/76D8ZPZM/fulltext/images/c576608a4e768b9ce005f44c18f7e37a521b4ec6f9b1c741ce7f618e42b00a63.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/1ca4c8dd1d46fcda7385d8112cd6e393c8e7501bb51af9ddf96ed534b2d57b62.jpg)

![](/api/attachments/76D8ZPZM/fulltext/images/a42bff3ba120044246680724115854f0494a9975990c131c66fa2454a5bd6cba.jpg)

## Appendix B

## Survey Questionnaires<sup>17</sup>

## Pre-experiment Questionnaire

1. What is your last two pre-meal blood glucose values (mmol/L)? A. 6.1–9.1 B. 9.1–12.1 C. 12.1–15.1 D. Over 15.1

2. What is your last two post-meal blood glucose values (mmol/L)? A. 6.1–9.1 B. 9.1–12.1 C. 12.1–15.1 D. Over 15.1

3. What’s your age? A. Under 30 years old B. 30–40 years old C. 40–60 years old D. Over 60 years old

4. How much do you spend monthly for your diabetes treatment? A. Less than 2000 RMB B. 2000–5000 RMB C. 5000–10000 RMB D. More than 10000 RMB

5. How many types of medicine are you currently taking to treat diabetes? A. None B. 1–2 C. 3–4 D. 5 or more than 5

6. How often do you test your blood sugar? A. Once a day B. 2–3 times per day C. Once every 2–3 days D. Once a week E. Other

7. How do you evaluate your current diet? A. My diet is healthy and in line with the dietary requirements of people with diabetes B. Quite regular, can eat three meals on time, can achieve less salt, less sugar, less oil C. Three meals a day, can be eaten on time, can try to achieve less salt, less sugar, less oil, but occasionally can’t. D. Three meals a day, but cannot control foods that eat less salt, less sugar, less oil. E. Three meals are irregular, but can control less salt, less sugar, less oil F. Three meals are irregular, unable to control diet

8. How do you think about healthy diet? (You can choose multiple options) A. Diet differentiation, eat more grains B. More pure natural food C. More fruit and vegetable D. Health care products, such as vitamin tablets E. I have no idea about healthy diet F. Other

9. Which of the following descriptions are appropriate for your daily workout? ( You can choose multiple options) A. I exercise lightly every day, like walking B. I participate in fitness activities every day, such as running, playing Tai Chi, square dance, etc. C. I rarely participate in physical exercise, I rarely go out. D. I usually do high-intensity exercises, such as weight-bearing anaerobic exercise, and occasionally mild exercise, such as walking and playing Tai Chi. E. I usually do mild exercise and occasionally do high-intensity exercises. F. I don’t do any exercise.

10. Do you feel that your current exercise situation is conducive to the recovery of diabetes? A. Obvious effect B. General effect C. Almost no effect D. No idea

11. If jogging is good for your body every day, you can stick to it under the following conditions: A. If someone reminds you to jog every day B. If someone encourage you to jog every day C. If someone is running around every day D. Anyway, it’s hard to stick to

12. Which kind of emotions do you often have?<sup>18</sup> A. Joyful and happy B. Feeling depressed C. Anxiety and depression D. Peaceful

13. Do you purchase and consume sugar-free health food for diabetics? A. Long-term consumption, regular purchase, fixed purchase location B. Occasionally eat, occasionally purchased, no fixed place to buy C. Seldom eat, there are patients recommended to try, there is no fixed place to buy D. Do not trust such products, think that you can stick to the kiln and diet, do not buy

14. Do you have the confidence to beat diabetes? A. Very confident B. General Confident C. Confident, but think it is hard D. Lack of confidence, but willing to try E. Lack of confidence, barely maintain the status

15. Have you ever participated in a diabetes rehabilitation program or a similar health management program? A. Yes, I have B. No, I have not C. No, but heard about that

16. What is your highest concern in health management? (You can choose multiple options ) A. Regular medical examination service B. Personal health record establishment and management C. Self-monitoring D. Private doctor service E. Personalized health management F. Health guidance, lifestyle intervention and adjustment G. Lecture, salon, party about heath management F. Personal consultation service

17. Do you Smoke? A. Yes B. No

18. What type of diabetes do you have? A. Type 1 diabetes B. Type 2 diabetes C. Gestational diabetes

19. How long do you have diabetes? Years

20. Have you had any complication? A. Yes, please specify B. No

## Post-experiment Questionnaire (end of the treatment period, and 5 months later)

1. What is your last two pre-meal blood glucose values (mmol/L)? A. 6.1–9.1 B. 9.1–12.1 C. 12.1–15.1 D. Over 15.1

2. What is your last two post-meal blood glucose values (mmol/L)? A. 6.1–9.1 B. 9.1–12.1 C. 12.1–15.1 D. Over 15.1

3. How many times did you visit the hospital during the last 3 months? A. None B. 1–3 C. 3–6 D. 6–10 E. More than 10

4. How many of these hospital visits were related to diabetes? A. 0 B. 1–3 C. 3–6 D. 6–10 E. More than 10

5. How much do you spend monthly for your diabetes treatment? A. Less than 2000 RMB B. 2000–5000 RMB C. 5000–10000 RMB D. More than 10000 RMB

5. What is your current solution to manage your blood sugar? A. Taking hypoglycemic drugs B. Insulin C. Diet management D. Sports management F. Daily life management (sufficient sleep, smoking cessation, alcohol restriction, etc.)

6. What kinds of drugs do you currently take? [Multiple choice questions] A. Metformin B. Acarbose C. Insulin D. Glipizide E. Gliclazide F. Giclazone G. Rpaglinide H. Sitagliptin I. Others

7. How many times do you use the app every day? (only for treatment group) A. 0 B. 1 C. 2 D. 3 E. More than 3

8. Can you rate the app? (only for treatment group) A. 1 star B. 2 stars C. 3 stars D. 4 stars E. 5 stars

## Appendix C

Overview of Randomization and Sampling  
![](/api/attachments/76D8ZPZM/fulltext/images/f76b44fc8eec882a1b43eb26f8709b9da59d50fe3fc5fb4ba1f3affb8140e770.jpg)  
Figure C1. Randomization and Sampling Procedure

## Appendix D

## Time Trends

We examined the overall time trends in each experimental group regarding the blood glucose change over time at the individual patient level. We plot the glucose value over time for each group in Figure D1.

The Y-axis is the glucose value for each individual patient. The X-axis is the sequence number as the time indicator. We show the plots fo both control groups and treatment groups at the individual level. From the time trend plots, we notice the three treatment groups on average uploaded more glucose values than the two control groups. This finding indicates a potential positive impact of mHealth in improving patien engagement with diabetes management. Furthermore, we see a noticeable downward trend over time in the three treatment groups compared to the two control groups. This finding suggests the mHealth platform seems to be able to help reduce patient glucose levels over time at the individual level. We also noticed an outlier in the T1 group at the very beginning, with a glucose value equal to 55. After consulting with the company and medical experts, we removed that sample from our primary model analysis.

![](/api/attachments/76D8ZPZM/fulltext/images/7847c44b141d46ad7e398eacc2eafc1d0dd30916f72ddebcd4d9656ea05c9512.jpg)  
Figure D1. Comparison of Time Trends for Blood Glucose Values over Time

## Appendix E

## An Additional Follow-Up Survey and Interview

To better understand the causal mechanisms of our findings, we have conducted a new round of survey and interview in September 2019.

## Summary of Survey Results

First, we sent a survey to app users from the three treatment groups (T1–T3) in our experiment. We approached these participants via WeChat groups the mobile app company maintained over years. There were 610 treatment participants (out of 705 total participants from T1–T3) in the WeChat groups. We received a total of 124 responses to our survey. The response rate was 124/610 = 20.3%.

The detailed survey questionnaire was provided in the end of this Appendix. We asked the participants three major questions:

(1) What is your favorite function of the blood glucose management mobile app?

(2) How did these functions help improve your health?

(3) For participants in T3, what’s your feedback toward the personalized text messages about medical guidance based on your persona exercise, diet and health status?

Based on the survey user responses, the most useful app function liked by the users is “Learning about health knowledge (68%),” followed by “Health real-time tracking: blood glucose, exercise, drug, diet (67%),” “Personalized diabetes risk assessment (61%),” “Doctor consultation (53%),” and “Social network support (48%).”

When being asked how these functions helped improve their health, a large majority of the users mentioned that the app provided them a way to better monitor and “quantify” their life and health in real time, hence they were able to better manage food intake and exercise. For example,

• “The blood glucose, exercise and diet tracking function provides me with a tool for daily health monitoring and comparison.”

“The combination of my blood glucose level and exercise diet allows me to understand the relationship between them clearly, which motivates me to exercise more and eat healthier food.”

• “Self-tracking of health status provides a quantitative basis in real time, and thus improves my health level.”

“Personalized recommendations for diet and exercise allow me to know exactly how many calories I should consume and how many I should burn.”

Regarding the personalized text message about medical guidance, users raised three major concerns: (1) interruption and annoyingness (58%), (2) avoidance toward negative information (54%), and (3) privacy (53%). For example,

• “Receiving personalized text messages frequently makes me feel interrupted and the user experience is terrible.”

“Sending personalized information frequently makes me feel terrible about my health, and too many negative emotions make me reluctant to try to change my health level.”

• “It makes me feel my privacy is being violated.”

## Summary of Interview Results

Second, in addition to the survey responses, we have also conducted in-depth phone interviews with a randomly selected group of seven experimental users from T3 treatment group. The main purpose of the interview was to further verify the survey responses, and meanwhile with a focus on why the personalized text messages did not work well. The detailed question design of the interview was provided in the end of this appendix.

We found the responses from the interview were highly consistent with those from the survey. When the participants were asked what functions they liked the most, all of the seven interview participants indicated that the real-time health tracking function provided them a way of better monitoring and managing their health. They (and their family members) have also gained professional health knowledge through using the app. For example,

• “After using the app for some time, I have gained some health knowledge.”

“The real-time tracking and the long-term blood glucose change trend helped me judge whether the medication, exercise or diet was reasonable and provided me a reference.”

“You see, some people don’t have a lot of knowledge about diabetes, right? People can gain some knowledge, and also have some reminders about their blood glucose management.”

• “I found the health tracking function is most useful for me. In daily life, it can help monitor my blood sugar.”

• “It can record my health data. I like this function most.”

“It certainly doesn’t make sense to people who are not sick, but it definitely makes sense to us who are sick, because we need such an assistant to let us know how high our blood sugar is at any time. We are very concerned about this.”

“The most important one is the health knowledge. Because the patient’s understanding of professional knowledge is still relatively inadequate. I have been learning a lot. Because I have had such instructions from the app, and my wife also has learned related knowledges and helped me.”

When the participants were asked whether they liked the personalized medical guidance via text messages and why, a majority of them (six out of seven) indicated that they found these personalized text messages “too frequent,” “annoying” and violating “privacy.” For example,

• “The personalized message was sent too often. It’s better to have a longer interval.”

• “I think it’s a bit troublesome. I think the frequency of the personalize message was a little high.”

• “I can accept the personalized advice, but you better not send the reminders so often.”

“If your blood glucose is in an expected range, you don’t need to be disturbed. Just when it’s abnormal (you can receive a personalized message intervention)”

• “It doesn’t need to be reminded too often, just once every half a month. Because my blood sugar is now in a stable state.”

“It feels that it knows what I do and feels like I am being watched by others.”

Of greater interest, during our interview one of the participants explicitly mentioned his/her preference of a less personalized text message to avoid “being judged all the time by someone”:

“Is it possible for you to make these personalized guidance text messages sound less personal, but instead more systematic—like the ones automatically sent by the system, not humans? That would make me feel less stressful. Not like being judged by someone all the time, but simply like having an alarm clock.”

This is highly consistent with our previous finding that frequent personalized messages might cause the patients to feel increased control and judgment. They might cause patients to feel pressured or coerced by intrapsychic or interpersonal forces. Such lack of choiceful and volitional feeling can lead to loss of autonomy and self-motivation (Deci and Ryan 1985; Ryan and Deci 2000). It in turn can lead to a significant decrease in patient intrinsic motivation of disease self-management and a lower health outcome.

In summary, our additional analyses from the new survey and interview demonstrated high consistency to our previous results. They provided richer causal evidence to our findings. We found that the positive impact of mobile health app is largely due to the real-time tracking and health monitoring functions provided by the app. Such functions can help patients with better self-educating, self-monitoring, and self-managing their own health. Besides, users raised three major concerns toward personalized health guidance via text messages: (1) interruption and annoyingness, (2) avoidance toward negative information, and (3) privacy concern. Based on user responses, when mHealth apps are trying to combine text messages with app functions to deliver medical guidance, a less frequent (i.e., once or at most twice a month) and less personalized (i.e., should sound less personal but more systematic) text message is strongly preferred.

## Survey Questionnaire Design

Hello, Dear users! I’m Dr. [insert name] from [insert institution]. Thank you for registering our diabetes management mobile application before. In order to improve the user experience, we have a few questions for you, which are expected to take you for less than 10 minutes. We will compensate you for 10 yuan after you complete the questionnaire.

1. What is your favorite function of the blood glucose management APP? [multiple choice]

A. Health Knowledge Function: health information

B. Diabetes Risk Assessment Function

C. Self-Tracking Function: blood glucose recording function; exercise recording function; drug recording function

D. Professional Support Function: doctor consultation function; manual personalized information guidance

E. Social Support Function: Patients’ moments (patients with diabetes can view the message posted by a friend)

F. None of the above, my favorite function is

2. Did these functions help improve my health? If so, how? If not, why? Please specify.

3. If we send you personalized guidance information via text messages based on your personal exercise and diet status, how would you feel? Do you think these personalized messages are helpful or not? Please specify.

Your gender: [single choice] A. Male B. Female

Your age: [single choice] A. Under 18 B. 18–25 C. 26–30 D. 31–40 E. 41–50 F. 51–60 G. Over 60

Your current industry: [single choice] A. IT / Software and Hardware Services / E-Commerce / Internet Operations B. Fast Moving Consumer Goods (Food / Beverage / Cosmetics) C. Wholesale / Retail D. Apparel / Textiles / Leather E. Furniture / Craft / Toy F. Education / Training / Scientific Research / Institute G. Home Appliance H. Communication / Telecom Operation / Network Equipment / Value-added Ser I. Manufacturing J. Automobile and Parts K. Catering / Entertainment / Tourism / Hospitality / Life Service L. Office Supplies and Equipment M. Accounting / Auditing N. Legal O. Bank / Insurance / Securities / Investment Bank / Risk Fund P. Electronic Technology / Semiconductor / Integrated Circuit Q. Instrument / Industry Automation R. Trade / Import & Export S. Machinery / Equipment / Heavy Industry T. Pharmaceutical / Biotechnology/ Medical Facilities / Equipment U. Healthcare / Nursing / Health V. Advertising / Public Relation / Media / Art Q. Publishing / Printing / Packaging Z. Real Estate Development / Construction Engineering / Decoration / Design Y. Property Management / Business Center Z. Agency / Consulting / Headhunting / Certification AA. Transportation / Logistics BB. Aerospace / Energy / Chemical CC. Agriculture / Fishery / Forestry 01

DD. Other industries

## Interview Outline Design

## Opening

Hello [insert name], I am Dr. [insertname] from [insert institution]. The purpose of this interview is to understand your attitude toward [app name] mobile app. This interview will take about 20 minutes. As compensation, we will pay you 20 yuan after the interview.

Your feedback and inputs are of great value to us. All your answers will be kept strictly confidential. We will not disclose your identity. All of your statements will only be used in research projects. If we want to cite any of your original words, we will use it in the form of a pseudonym.

## Developing

1. Do you remember when you (refer to the registration time) registered your blood glucose mobile app?

2. What is your evaluation and impression of this blood glucose management app? What is your favorite function of diabetes management software? Why? Does these functions change your health behavior?

3. Did you receive a text message for a personalized diet and exercise guide? If so, how often?

4. Do you think these personalized text messages for health guidance helped with your health (or will help with your help if the patients have not received any)?

5. Do you think there are any disadvantages to your health caused by these text messages?

6. Would you like to cooperate with the staff to improve your eating and sports behaviors?

7. Would you like to receive a call or a text message from the company’s nutritionist for active health guidance?

8. How often would you like to, if so?

9. What do you think is an acceptable personalized guidance program?

10. What do you think is the biggest pain point in the daily management of diabetes?

## Ending

[Insert name], thank you very much for your help. I have no further questions. Your opinion is very helpful and enlightening to us. Thank you very much.
