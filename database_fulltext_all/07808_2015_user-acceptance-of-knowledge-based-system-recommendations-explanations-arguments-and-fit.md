---
otero_id: 7808
otero_key: "F3CTK7Q8"
title: "User acceptance of knowledge-based system recommendations: Explanations, arguments, and fit"
authors: "Justin Scott Giboney; Susan A. Brown; Paul Benjamin Lowry; Jay F. Nunamaker"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.02.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# User acceptance of knowledge-based system recommendations: Explanations, arguments, and <sup>fi</sup>t

Justin Scott Giboney <sup>a,</sup>⁎, Susan A. Brown <sup>b</sup>, Paul Benjamin Lowry <sup>c</sup>, Jay F. Nunamaker Jr. <sup>b</sup>

<sup>a</sup> University at Albany, 1400 Washington Ave., Albany, NY 12222, USA

<sup>b</sup> University of Arizona, 1130 E. Helen St., Tucson, AZ 85721, USA

<sup>c</sup> City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong

## a r t i c l e i n f o

Article history: Received 19 August 2014 Received in revised form 2 February 2015 Accepted 5 February 2015 Available online 11 February 2015

Keywords: User acceptance Explanations Cognitive <sup>fi</sup>t Recommendations

## a b s t r a c t

Knowledge-based systems (KBS) can potentially enhance individual decision-making. Yet, recommendations from KBS continue to be met with resistance. This is particularly troubling in the context of deception detection (e.g., border control), in which humans are accurate only about half the time. In this study, we examine how the <sup>fi</sup>t between KBS explanations and users' internal explanations in<sup>fl</sup>uences acceptance of KBS recommendations. We leverage cognitive <sup>fi</sup>t theory (CFT) to explain why <sup>fi</sup>t is important for user acceptance of KBS evaluations. We also compare the predictions of CFT to those of the person–environment <sup>fi</sup>t (PEF) paradigm. The two theories make con<sup>fl</sup>icting predictions about the outcomes of <sup>fi</sup>t when it comes to KBS explanations. CFT predicts that explanations with a higher cognitive <sup>fi</sup>t will have more in<sup>fl</sup>uence and be evaluated faster whereas PEF predicts that individuals will take more time in evaluating explanations with greater <sup>fi</sup>t. In our deception detection scenario, we <sup>fi</sup>nd support for CFT in the sense that people are in<sup>fl</sup>uenced more by cognitively <sup>fi</sup>tting explanations, however PEF is supported in the sense that people take more time to evaluate the explanation.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Knowledge-based systems (KBS) have the potential to enhance the way people make decisions. In cases in which a KBS's accuracy is much higher than the decision maker's—such as IBM's Jeopardyplaying Watson [1] —the decision makers are missing out on the potential value created by the KBS if they do not use them [2]. Nonetheless, in many domains, such as credibility assessment [3] and medical informatics [4], acceptance of KBS decisions often still falls below 60%. The potential value of accepting a correct decision from a KBS can be particularly meaningful in cases where individuals are attempting to discern whether or not someone is being deceptive, such as in border crossings [3] and auditing [5]. Therefore, if researchers can better understand why users do or do not accept the decisions of a KBS, the potential value of KBS for decision making in practice can be improved.

One unique aspect of KBS is the use of lines-of-reasoning explanations [6]. These explanations attempt to assist the user in evaluating the KBS's decision by helping the user understand how the KBS came to a certain conclusion (e.g., showing the logic by which the system arrived at the conclusion). Explanations have been studied since the introduction of MYCIN (a medical KBS) in the 1970s [7] to today [e.g., 8–10]. Notably, researchers continue to explore ways to present lines-of-reasoning explanations to users to increase acceptance of KBS recommendations [6]. Ye & Johnson [5] proposed that “one future direction may be to assess the impact of different kinds of justi<sup>fi</sup>cation and to identify the appropriate conditions under which each should be employed” (p. 169).

In addition to differential impacts of justi<sup>fi</sup>cations, research also indicates that differing representations of information can alter the amount of KBS in<sup>fl</sup>uence. For example, Papamichail and French [11] found that users preferred certain information formats over others. Users performed better with their preferred formats, and the preferred formats were not consistent among users (i.e., some users preferred formats rejected by other users). This <sup>fi</sup>nding suggests that a matching, or <sup>fi</sup>t, between users and information format is needed for the KBS to be perceived favorably and thus adopted. When we combine this with the suggestion that certain justi<sup>fi</sup>cations (i.e., lines of reasoning) are stronger than others [12], it logically leads us to propose that providing justi<sup>fi</sup>cations that <sup>fi</sup>t with user preferences should be valuable for increasing KBS recommendation acceptance. Accordingly, the following research question guides our study:

RQ: How does <sup>fi</sup>tting KBS justi<sup>fi</sup>cations to a user's cognitive preferences in<sup>fl</sup>uence the user's acceptance of KBS recommendations?

To address our research question, we <sup>fi</sup>rst review the explanation literature to build a foundation for our research. Then, we leverage CFT to explain why <sup>fi</sup>t is important for understanding the in<sup>fl</sup>uence of

KBS recommendations on users. We also employ the PEF paradigm to provide an alternative explanation of how KBS recommendations will in<sup>fl</sup>uence user behavior. Our theoretical model is then tested by an experiment in which we examine the processing of explanations provided by a KBS—focusing on explanations in a credibilityassessment task that will allow us to compare the two theories. Finally, we address the results and contributions of this experiment with respect to improving KBS acceptance.

## 2. Theory and hypotheses for KBS recommendations

We examine KBS explanations through two bodies of literature. First, we examine the KBS explanation literature. The KBS explanation literature provides constructs such as explanation quality and explanation in<sup>fl</sup>uence (see Fig. 1). Second, we combine the KBS literature with theories of <sup>fi</sup>t literature. In particular, we look out how <sup>fi</sup>tting the explanation to the user will impact explanation quality and explanation in<sup>fl</sup>uence. Fig. 1 depicts the overall theoretical model that we propose and further justify in this section. Before explaining our speci<sup>fi</sup>c hypotheses, we de<sup>fi</sup>ne our null hypothesis:

H0. Fitting KBS justi<sup>fi</sup>cations to a user's cognitive preferences does not in<sup>fl</sup>uence the user's acceptance of KBS recommendations

## 2.1. Knowledge-based system explanations

KBS have been an important theme in information systems (IS) research for quite some time. Topics include adoption of early medical information systems [e.g., 7], loan evaluation systems [e.g., 13], and more recently, deception detection systems [e.g., 3]. One continuing theme in KBS research is the use of explanations. An explanation is a description of the reasoning processes the KBS uses to solve problems and make recommendations [5,14].

Explanation use is an important determinant of the in<sup>fl</sup>uence and user acceptance of the KBS's decision [15–17]. Explanations help the user understand the situation or how the KBS came up with its results. Understanding a KBS can in<sup>fl</sup>uence the user to believe the KBS, thus causing the user to agree more with the KBS [18].

![](/api/attachments/F3CTK7Q8/fulltext/images/a8f72d6dc6c6a0d9d0e2fd2c479159ba07febde114cb1cbbcc1036a222d2b1cd.jpg)  
Fig. 1. Hypothetical model.

Because convincing the user to agree with the KBS is the goal of a KBS (assuming that the KBS recommendation is correct), we use two metrics to evaluate the KBS regarding this goal: explanation in<sup>fl</sup>uence and explanation evaluation time. Explanation influence is the amount of change from what a user would have decided before the explanation to what the user decides after the explanation. This is often measured as the accuracy of the user [19]. Explanation evaluation time is the amount of time the user spends reading the explanation and coming to a decision [19].

Many types of explanations are possible, from emotion-based explanations to probability-based explanations [20–24], and people process explanations in different ways [25–28]. When people process explanations they aggregate their thoughts, feelings, and the argument made by the explanation into a perceived explanation quality. Explanation quality is a user's perception of the explanation's strength and adequacy. Measuring this allows researchers to collect and remove individual differences in scienti<sup>fi</sup>c studies. An explanation with high quality is perceived as well written and understandable, whether or not the user agrees with it. Evidence of strong, persuasive arguments leading to attitude and belief change has been well supported in the literature [29–31] (see Fig. 1). When a user perceives an explanation to be strong and of high quality, he or she is more likely to have favorable messageoriented thoughts that cause the user to believe the message [32]. These message-oriented thoughts occur because high-quality explanations motivate a reader to understand and process the explanation [30].

## H1. Explanation quality will increase explanation in<sup>fl</sup>uence.

The perceptions and in<sup>fl</sup>uence of a KBS explanation are tightly integrated with the KBS that provides the explanation to the user. Speci<sup>fi</sup>cally, explanation quality will increase the user's perception of the system's competence. Explanations can cause users to perceive a KBS as more competent [10] than a KBS without an explanation. KBS are seen as competent when users believe that KBS have the ability, skills, and expertise to act [33]. Explanations make the reasoning process of the KBS transparent, allowing the user to judge the ability, expertise, and usefulness of the system [10]. The perceived usefulness of the KBS is a user's belief regarding its ability to enhance job performance [34].

## H2. Explanation quality will increase perceived usefulness of the KBS.

When users perceive KBS as more useful, they will have more con<sup>fi</sup>- dence in the output and decisions made by the KBS [35]. This con<sup>fi</sup>dence is due to users perceiving KBS as accurate and reliable, which in turn leads them to trust KBS to make more correct decisions then the user would have made without the KBS [10,35]. When users believe that KBS will provide more correct decisions, they will follow the recommendation of KBS, thereby increasing the in<sup>fl</sup>uence of outputted explanations on the user.

## H3. Perceived usefulness of the KBS will increase explanation in<sup>fl</sup>uence.

The perceived usefulness of a KBS is not complete without considering the in<sup>fl</sup>uence of how easy the KBS is to use. Perceived ease of use is the degree to which a user believes using the KBS is free from effort [34]. When a KBS is easier to use, all other things being equal, it has greater potential to be useful [34]. This positive relationship has been replicated in a large number of studies [e.g., 34,36]. We add this relationship to our model simply for nomological completeness.

## H4. Perceived ease of use will increase perceived usefulness.

## 2.2. Applying theories of fit to KBS

The combination of the task and the style and wording of the explanation can in<sup>fl</sup>uence the effectiveness of the explanation [37]. Therefore, the <sup>fi</sup>t between the explanation given and the person receiving it is an important factor of the in<sup>fl</sup>uence, the evaluation time, and even the perceived quality of the explanation. To understand these relationships, we look to theories of <sup>fi</sup>t. We highlight two theories of <sup>fi</sup>t: CFT [38] and stage-environment <sup>fi</sup>t (SEF) [39], with the latter being part of the PEF paradigm [40].

Fig. 1 introduces the hypotheses that we have covered so far, plus the extension we are introducing using theories of <sup>fi</sup>t. Our extension of current literature adds the cognitive <sup>fi</sup>t leading to explanation quality, explanation in<sup>fl</sup>uence, and explanation evaluation time. Each piece of this extension will be discussed in detail after we discuss theories of <sup>fi</sup>t.

Cognitive fit indicates the degree to which a task's environmental factors—such as programming language [41] and visual representation [42]—match the nature of the task [38]. When there is good cognitive <sup>fi</sup>t, a person does not have to transform his or her mental understanding of a task into a representation of the task [38]. When cognitive <sup>fi</sup>t does not exist, a person has to perform multiple tasks simultaneously, increasing cognitive load [43] and decreasing task speed and task accuracy [44]. Consequently, CFT proposes that decision makers can be faster and more accurate in their decisions when their mental representation matches the task representation (see Fig. 2), that is, whenever there is cognitive <sup>fi</sup>t [38,45]. For examples of CFT research in the IS literature see Appendix A.

According to CFT, the task representation is the format and manner of presenting the task. The nature of the problem changes an individual's mental representation of the task [38,46,47] because individuals acquire information based on how it is presented [42,48]. Task instructions often de<sup>fi</sup>ne the task as well as provide a mental model of the task that can in<sup>fl</sup>uence the mental representation [49,50].

A mental representation is a person's knowledge or understanding of how a task functions and how to attempt to obtain a solution to the task. A mental representation allows a person to retrieve, store, analyze, and use information [51]. A person's mental representation can take form on the basis of various sources: task-related skills, abilities possessed by the individual that facilitate the task [52], decision style [53], cognitive style [54,55], and experience with the domain and the tool [44,56–58].

CFT explains that the task and mental representations are part of the task space, which is “a set of points, or nodes, each of which is a knowledge state” [46 p. 108]. A knowledge state “is the set of things the problem solver knows or postulates” [46 p. 108]. Consequently, what an individual knows or perceives changes the individual's model of the problem. Even isomorphs—two tasks in which “the solution path of one may be translated step by step into a solution path of the other and vice versa” [59 p. 22]—change the ability of an individual to accomplish the task [59].

CFT also proposes that individuals have a limited capacity to process information and that, because of this limitation, they are more effective at problem solving when task-environment complexity is reduced [38]. Because processing information is in<sup>fl</sup>uenced by how the information is received, factors related to the problem-solving environment, such as problem representation, tools, and techniques, can reduce complexity if the environment supports the strategies required to perform the task [38]. That is, if an environment facilitates the cognitive processes necessary to transform the problem into a solution (i.e., <sup>fi</sup>t), then task complexity is reduced [41]. This reduction is due to the fact that when the cognitive processes the individual uses to acquire information from the task match the cognitive processes required to complete the task, the task will be facilitated by the task representation [38]. This happens because there is no need to transform the mental representation generated by the processes used to acquire the information into a mental representation that can use the processes needed to accomplish the task [38]. Thus, cognitive load is decreased [43].

![](/api/attachments/F3CTK7Q8/fulltext/images/c3041179200894b8adb580f69a6bd5a3fbc3a50c3343514f3047f85e7eec756c.jpg)  
Fig. 2. Cognitive <sup>fi</sup>t theory.

Conversely, where there is no <sup>fi</sup>t—as a result of either under- or over-<sup>fi</sup>t [60] —the processes used to acquire information cannot be used to accomplish the task [38]. When the same process cannot be used, individuals have to perform two subtasks: acquiring information and transforming the information to perform the task. The problem with having two subtasks is that individuals typically either form a mental representation based on the information and will need to transform the representation to accomplish the task, or they form a mental representation based on the task and will need to transform the information to accomplish the task [38]. Therefore, when the information does not have to be transformed, individuals will be able to internalize information in an explanation and apply it directly to the task, allowing the explanation to have more in<sup>fl</sup>uence.

Speci<sup>fi</sup>cally, in the context of this paper, we look at the <sup>fi</sup>t between classi<sup>fi</sup>cation explanations and propensity to stereotype. A classi<sup>fi</sup>cation explanation is one that makes a conclusion about a speci<sup>fi</sup>c instance based on a general population (in other words, such explanations are stereotypes). A propensity to stereotype (PtS) is a cognitive style de<sup>fi</sup>ned as the “inferential logic by which people translate easily detected information about demographic attributes into best-guess hypotheses about personal attributes of a stranger” [61, p. 56]. For hypotheses 5–7, we focus on the <sup>fi</sup>t between an individual's PtS and whether or not they receive a classi<sup>fi</sup>cation explanation.

## H5. Explanation cognitive <sup>fi</sup>t will increase explanation in<sup>fl</sup>uence.

The reduction of complexity by cognitive <sup>fi</sup>t will cause individuals to perceive the argument as a stronger and better one, because the user will be able to focus on the explanation itself and will not have to spend time trying to understand the explanation. That is, the user does not have to transform the explanation into something usable [38]. Because the user does not have to transform the explanation, the user will be able to perceive more readily the bene<sup>fi</sup>ts of using the explanation.

## H6. Explanation cognitive <sup>fi</sup>t will increase explanation quality.

CFT explains that when an individual tries to perform multiple tasks simultaneously, the person's performance (task speed and accuracy) of the tasks worsens [44]. When an individual's mental representation and task representation differ, it is as though the person is performing multiple tasks simultaneously. This mismatch causes degradation in task accuracy and speed [45,62]. The degradation is increased in complex tasks where increased cognitive effort is needed just to accomplish a single task [45]. To recap, CFT states that decision makers can be faster and more accurate in their decisions when the individual's mental representation matches the task representation, that is, whenever there is cognitive <sup>fi</sup>t [38,45]. Therefore, the less complex the KBS explanation, the more rapidly the user should be able to process and evaluate the explanation.

H7. Explanation cognitive <sup>fi</sup>t will decrease explanation evaluation time.

## 3. Methodology

## 3.1. Study context

The context for this study is deception detection. Deception detection is a common decision-making task for security and law enforcement. Furthermore, because accuracy in deception detection tasks is often as low as 50% [3,63,64], it is a decision-making context that has room for improvement.

## 3.2. Participants and demographics

A total of 263 upper-division students from a large southwestern U.S. university participated in this study. We chose university students because deception detection is a common, if not daily, activity for most adults and deception detection rates for untrained populations and trained professionals are similarly poor [3]. Moreover, because the task was a simple decision-making task, the use of student participants allowed us to generalize to most young decision-making adults [65]. The average age range of the participants was 18–24 years, with 109 participants (41.44%) being female.

## 3.3. Research stimulus and task

Participants were recruited from a large introductory IS course required for all business school students. Participants were given course credit for completing the study. Upon recruitment, participants were directed to an online pre-survey that we used to measure demographics and various personality measures, including the PtS<sup>1</sup>. Participants were also asked to sign up for a time (roughly a week in the future) to participate in the second portion of the study.

For the second portion of the study, participants came to a large computer lab on campus. This setting was chosen to introduce a sense of seriousness to the study. In the computer lab, participants were once again directed to an online survey that informed them they would be watching some videos, their input is needed to help determine whether the person in the video is telling the truth or lying, and their input will help determine the legal actions that should be taken against each person.

Participants then watched three of four randomly ordered twominute videos of subjects in another study who could have cheated or stolen a ring. In the videos (e.g., Fig. 3) the people are interviewed regarding whether or not they cheated or stole the ring. Two of the videos are of females from a cheating study, one being truthful (did not cheat) and one being deceitful (cheated). The other two videos are of two males from a ring-theft study, one being truthful (did not steal the ring) and one being deceitful (stole the ring).

The participants in our study were then directed to make a judgment and indicate whether they thought the person in the video was truthful or deceptive (binary), how deceptive or truthful the person was (Likert-type scale from 1, “deceptive”, to 7, “truthful”), and how con<sup>fi</sup>dent they were in their response (Likert-type scale from 1, strongly uncon<sup>fi</sup>dent, to 7, strongly con<sup>fi</sup>dent).

After they made this judgment, participants were shown the KBS's decision (see Fig. 4). The KBS's decisions were always accurate. The participants were also given an explanation of how the KBS arrived at that answer. The explanation randomly <sup>fi</sup>t or did not <sup>fi</sup>t the participant's cognitive style (i.e., the explanation was about classifying stereotypes or it was not). Each participant received either all <sup>fi</sup>tting explanations or all non<sup>fi</sup>tting explanations. Consequently, the match between PtS and classi<sup>fi</sup>cation explanations was used as the measure of <sup>fi</sup>t. Participants were also asked to rate the explanation quality of each explanation.

To give the participants the opportunity to modify their original judgments, they were asked the same judgment questions previously given. The <sup>fi</sup>rst two rounds were used as a practice to accustom participants to the environment. After watching all videos, the participants were given the post-experimental survey.

## 3.4. Measurement

We used previously validated scales for perceived ease of use, perceived usefulness, and explanation quality but modi<sup>fi</sup>ed them to <sup>fi</sup>t the context. Both perceived ease of use and perceived usefulness were measured with four items from Venkatesh and Davis [34]. Explanation quality was measured with four items from Andrews and Shimp [32].

For our context, we measured <sup>fi</sup>t as the match between PtS and whether or not the person received a classi<sup>fi</sup>cation explanation. PtS was measured with six items from Shrivastava and Gregory [66]. The cognitive <sup>fi</sup>t is between the cognitive style of a person and the cognitive style used in the explanation. The interaction of the two was used as the measure of <sup>fi</sup>t. Therefore, participants scoring high on the PtS scale who also received a classi<sup>fi</sup>cation explanation had high <sup>fi</sup>t, whereas everyone else had low <sup>fi</sup>t. For a complete list of scale items see Appendix B.

Explanation evaluation time was calculated by the survey software using the time that participants spent on the page with the explanation before making their <sup>fi</sup>nal judgments. Explanation in<sup>fl</sup>uence was calculated by comparing the movement from the initial judgment (binary scale, truthfulness scale, and con<sup>fi</sup>dence scale) to the <sup>fi</sup>nal judgment (binary scale, truthfulness scale, and con<sup>fi</sup>dence scale). If the explanation was more in<sup>fl</sup>uential, there was more movement toward the accurate judgment. We also included a manipulation check to verify that the participants were reading the explanations given to them. Five participants failed the manipulation check, meaning that they did not read any of the explanations (or completely disregarded them), and therefore were not included our analysis. Also, it has been shown that when a user already agrees with the decision of the KBS there is no incentive to read an explanation [67]. Users who agreed with all decisions were not evaluated. This left us with 140 usable responses.

## 4. Analyses

We chose to analyze our model using a covariance-based structural equation (CB-SEM) using SAS 9.3 software [68] because we were testing a path model (Fig. 1) containing multiple endogenous and exogenous variables with re<sup>fl</sup>ective indicators including mediating effects. Before evaluating our model, we needed to verify that our instruments were valid and captured our intended constructs (i.e., construct validity). Therefore we start our analysis with our instrument validation before moving on to the evaluation of the model.

## 4.1. Instrument validation

Prior to evaluating the model, we conducted <sup>fi</sup>ve analyses to ensure that the latent constructs exhibited factorial validity and reliability. First, we ran an exploratory factor analysis to verify the convergent validity of the constructs. Second, we also checked the Cronbach's alpha values of each construct to examine reliability (see Appendix B). We removed items that did not load well or cross-loaded on more than one construct, leaving us with the items presented in Table 1. Third, we checked for common-method bias by examining our correlations. As all of our correlations were low, common-method bias is less likely a concern than if our correlations were high [69,70]. Fourth, we checked for discriminant validity by examining the square root of the AVE in comparison to construct correlations [71]. The constructs showed strong discriminant validity by having low correlation between constructs and having all correlations below the square root of the AVE. Finally, we checked for multicollinearity by running a regression of all the constructs to predict explanation in<sup>fl</sup>uence and checking the variance in<sup>fl</sup>ation factors (VIF) [72,73]. All VIF values were close to 1 (with a range of 1.06–1.18) and therefore showed no signs of multicollinearity. We present the means, standard deviations, and correlations in Table 2.

Please watch this video and answer the questions. Click play if the video doesn't start automatically.  
![](/api/attachments/F3CTK7Q8/fulltext/images/d4634590f3cf20419054085b3f20375a6181afb5810cc9f713f1b125f8d117e2.jpg)  
Fig. 3. Sample video.

## 4.2. Model evaluation

We tested all of the hypotheses in one model (as shown in Fig. 1). We used CB-SEM to test our model using SAS 9.3 software [68]. CB-SEM estimates all of the paths in the model simultaneously and provides model <sup>fi</sup>t statistics [74], whereas attempting to analyze such a path model with regression techniques results in several statistical issues, including model misspeci<sup>fi</sup>cation [75]. The resulting model provides the regression beta coef<sup>fi</sup>cient and signi<sup>fi</sup>cance for each path. Before testing the hypotheses in the model, it is best to measure how well the model <sup>fi</sup>ts the sample data [76]. To check goodness-of-<sup>fi</sup>t, the <sup>fi</sup>rst thing we check for was a non-signi<sup>fi</sup>cant chi-square, a high goodness-of-<sup>fi</sup>t index (near 1.0), and a high adjusted goodness-of-<sup>fi</sup>t index (near 1.0). Our chi-square was non-signi<sup>fi</sup>cant (0.79), the goodness-of-<sup>fi</sup>t index was high (0.99), and the adjusted goodness-of-<sup>fi</sup>t index was also high (0.97) indicating that our model <sup>fi</sup>ts the sample data. Fig. 5 presents the results of our model testing. Fig. 5 shows that many of our hypotheses were signi<sup>fi</sup>cant. In particular, Fig. 5 shows that the knowledge-based system literature and the <sup>fi</sup>t literature come together to create a more comprehensive explanation of the causal mechanisms behind explanation in<sup>fl</sup>uence. We will examine the results of the speci<sup>fi</sup>c hypotheses in more detail in the discussion.

## 5. Discussion

The purpose of this study was to address the research question, “how does <sup>fi</sup>tting KBS justi<sup>fi</sup>cations to a user's cognitive preferences in<sup>fl</sup>uence the user's acceptance of KBS recommendations?” The overall answer is that <sup>fi</sup>t, as predicted by CFT, causes the KBS to in<sup>fl</sup>uence the user more than when there is no <sup>fi</sup>t as demonstrated by the support for hypotheses 1 and 6. Therefore, we can reject the null hypothesis (H0) and declare that <sup>fi</sup>tting KBS justi<sup>fi</sup>cations to a user's cognitive preferences in<sup>fl</sup>uences the user's acceptance of KBS recommendations. While increasing acceptance, explanation evaluation time is increased as predicted by the PEF paradigm. Table 3 summarizes our tested hypotheses.

Although most of the hypotheses were supported, two of them were not. H5, cognitive <sup>fi</sup>t will increase explanation in<sup>fl</sup>uence, was predicted by CFT but was not supported in our analysis. This non-signi<sup>fi</sup>cant result could have been caused by a small sample size. The result might also have been caused by the mediation of explanation quality, however explanation <sup>fi</sup>t failed the <sup>fi</sup>rst test for mediation (a signi<sup>fi</sup>cant direct relationship to explanation in<sup>fl</sup>uence) with a p-value of 0.192. Therefore, we conclude that explanation <sup>fi</sup>t likely only has an indirect relationship on explanation in<sup>fl</sup>uence by <sup>fi</sup>rst affecting explanation quality and then letting explanation quality affect explanation in<sup>fl</sup>uence.

H7, cognitive <sup>fi</sup>t will decrease explanation evaluation time, was predicted by CFT but was not supported. We believe that the PEF paradigm suggesting <sup>fi</sup>t increases explanation evaluation time, may provide a strong explanation. The PEF paradigm [40] states that when a lack of <sup>fi</sup>t exists among the skills, knowledge, characteristics, or needs of a person and the environment, the person will experience increased stress or strain [77,78]. This stress can cause a withdrawal from the technology [79]. Conversely, lack of stress due to <sup>fi</sup>t can cause an increase in motivation to perform the task and in the satisfaction associated with performing the task [80].

As the use of KBS can be viewed not only as decision support, but also as an opportunity for the user to learn [9], we examine an educational aspect of the PEF paradigm: SEF. As part of the PEF paradigm, SEF is an educational theory [39] that posits that when there is a <sup>fi</sup>t and relatedness between an environment and a student, engagement (e.g., positive behavior and motivation) increases [81,82]. Increased engagement will result in increased time spent absorbing the information in the <sup>fi</sup>tting environment, because the person has the capabilities and available resources to adopt the arrangements [40]. SEF opposes CFT in that SEF predicts that a user will be more engaged and will spend more time reading and evaluating the explanation when there is <sup>fi</sup>t. Consequently, whereas CFT predicts an increase in explanation evaluation speed, SEF predicts a decrease in explanation evaluation speed.

![](/api/attachments/F3CTK7Q8/fulltext/images/9d726408a5fde360c41140482d9cf2e548e642a579756def55853853e95565ce.jpg)  
Fig. 4. Sample displayed explanation.

Table 1  
Factor loadings of scale items.

<table><tr><td>Items</td><td>PTS</td><td>PEU</td><td>PU</td><td>EQ</td></tr><tr><td>PTS1</td><td>0.552</td><td>0.036</td><td>0.227</td><td>0.010</td></tr><tr><td>PTS2</td><td>0.623</td><td>0.047</td><td>0.117</td><td>0.043</td></tr><tr><td>PTS3</td><td>0.719</td><td>0.042</td><td>0.164</td><td>0.077</td></tr><tr><td>PTS5</td><td>0.647</td><td>0.123</td><td>0.084</td><td>0.122</td></tr><tr><td>PEU2</td><td>0.057</td><td>0.647</td><td>0.112</td><td>0.055</td></tr><tr><td>PEU3</td><td>0.084</td><td>0.706</td><td>0.443</td><td>0.123</td></tr><tr><td>PU1</td><td>0.217</td><td>0.200</td><td>0.757</td><td>0.225</td></tr><tr><td>PU3</td><td>0.213</td><td>0.285</td><td>0.840</td><td>0.268</td></tr><tr><td>PU4</td><td>0.103</td><td>0.278</td><td>0.797</td><td>0.260</td></tr><tr><td>EQ1</td><td>0.067</td><td>0.130</td><td>0.286</td><td>0.901</td></tr><tr><td>EQ2</td><td>0.081</td><td>0.083</td><td>0.301</td><td>0.944</td></tr><tr><td>EQ3</td><td>0.116</td><td>0.119</td><td>0.274</td><td>0.951</td></tr><tr><td>EQ4</td><td>0.098</td><td>0.113</td><td>0.268</td><td>0.930</td></tr></table>

## 5.1. Contributions to research

This study has three main contributions to research: 1) explanations that <sup>fi</sup>t in<sup>fl</sup>uence users but indirectly through explanation quality, 2) explanations that <sup>fi</sup>t will likely increase the amount of time the users spends evaluating the explanation, and 3) an integrated model, leveraging system and cognitive components, is necessary to understand the impact of explanations in KBS. Here, we discuss each of these contribu tions in turn.

First, the main theoretical contribution of this study, the one that most directly answers our research question, is that explanations that <sup>fi</sup>t with the user will in<sup>fl</sup>uence the user more than non-cognitively <sup>fi</sup>tting explanations, but that it is not a direct relationship and only indirectly affects explanation in<sup>fl</sup>uence through explanation quality. CFT would predict that the explanation should have more in<sup>fl</sup>uence and users should evaluate the explanation faster when the explanation <sup>fi</sup>ts with the user than when the explanation does not <sup>fi</sup>t with the user. However, the results suggest two <sup>fi</sup>ndings contrary to CFT: 1) that the value of the cognitive <sup>fi</sup>t comes through perceived explanation quality by making users think that the explanation is of higher quality, and 2) contrary to CFT and consistent with PEF, explanation <sup>fi</sup>t increase the time the user spends evaluating the explanation. In answering our research question, we conclude that users of KBS will spend more time evaluating and be in<sup>fl</sup>uenced more by explanations that <sup>fi</sup>t with the users through explanation quality. Future research in KBS needs to consider that <sup>fi</sup>t works through explanation quality.

![](/api/attachments/F3CTK7Q8/fulltext/images/81b50257e642732c5217d66b1fad71825a19748df610e4a117c8e9382a4fd9b3.jpg)  
Regression weights on paths. \*p < .05. \*\*p < .01. \*\*\*p < .001.  
Fig. 5. Model results.

Second, CFT may be unable to explain evaluation time in the context of a KBS and that evaluation time is better explained by the PEF paradigm. This is important for KBS researchers, because explanations that cognitively <sup>fi</sup>t with a user are likely to be engaging and increase the amount of time that a user spends with an explanation. Therefore, research aimed at optimizing evaluation time, such as credibility screening, needs to look at antecedents other than <sup>fi</sup>t. This is an important <sup>fi</sup>nding as it provides a theoretical insight into dividing KBS into those that do not need fast response times that will bene<sup>fi</sup>t from explanations that <sup>fi</sup>t with users and KBS that need fast response times and will not bene<sup>fi</sup>t from explanations that <sup>fi</sup>t with users. KBS that need fast response times will bene<sup>fi</sup>t more by providing quick summary decisions than providing detailed explanations to users.

Last, this study provides an integrated model of KBS-level elements (perceived ease of use and perceived usefulness) and explanation elements (cognitive <sup>fi</sup>t and explanation quality). This model helps answer outstanding research questions about how different types of explanations affect users and different conditions in which these

## Table 2

Construct correlations

<table><tr><td>Latent construct</td><td>Mean</td><td>SD</td><td>AVE</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>(1) Explanation cognitive fit</td><td>1.03</td><td>1.69</td><td>NA</td><td>NA</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Explanation influence</td><td>9.81</td><td>10.36</td><td>NA</td><td>0.109(0.196)</td><td>NA</td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Explanation evaluation time</td><td>19.92</td><td>9.03</td><td>NA</td><td>0.187(0.027)</td><td>0.105(0.213)</td><td>NA</td><td></td><td></td><td></td></tr><tr><td>(4) Explanation quality</td><td>3.59</td><td>1.63</td><td>0.868</td><td>0.189(0.025)</td><td>0.285(0.001)</td><td>0.026(0.756)</td><td>0.932</td><td></td><td></td></tr><tr><td>(5) Perceived ease of use</td><td>5.15</td><td>1.20</td><td>0.458</td><td>-0.082(0.333)</td><td>0.049(0.564)</td><td>0.017(0.838)</td><td>0.099(0.246)</td><td>0.677</td><td></td></tr><tr><td>(6) Perceived usefulness</td><td>4.18</td><td>1.28</td><td>0.638</td><td>0.050(0.555)</td><td>0.254(0.002)</td><td>0.062(0.465)</td><td>0.288(0.001)</td><td>0.278(0.001)</td><td>0.799</td></tr></table>

p-Value is reported beneath correlations; square root of the AVE is on the diagonals.  
SD = Standard Deviation;' AVE = Average Variance Extracted.

Table 3 Summary of hypotheses.

<table><tr><td>Hypothesis</td><td>Findings</td></tr><tr><td>H1: Explanation quality will increase explanation influence.</td><td>Supported</td></tr><tr><td>H2: Explanation quality will increase perceived usefulness of the KBS.</td><td>Supported</td></tr><tr><td>H3: Perceived usefulness of the KBS will increase explanation influence.</td><td>Supported</td></tr><tr><td>H4: Perceived ease of use will increase perceived usefulness.</td><td>Supported</td></tr><tr><td>H5: Explanation cognitive fit will increase explanation influence.</td><td>Not supported</td></tr><tr><td>H6: Explanation cognitive fit will increase explanation quality.</td><td>Supported</td></tr><tr><td>H7: Explanation cognitive fit will decrease explanation evaluation time.</td><td>Significant in opposite direction</td></tr></table>

explanations should be used. Furthermore, this model can now be extended to investigate additional personal traits and states that could in<sup>fl</sup>uence the interactions of system elements and explanation elements.

## 5.2. Limitations and future research

Our implications should be viewed in light of the limitations of our study. Along with the task-performance measures of task speed and task accuracy, CFT has been used to explain an increase in perceived ease of use and in perceived usefulness due to enhanced information processing caused by cognitive <sup>fi</sup>t [83–85]. Because perceived ease of use is the amount of effort the user believes is required to use the KBS or tool and cognitive <sup>fi</sup>t reduces cognitive effort, improved perceived ease of use is a direct result of <sup>fi</sup>t [86]. We did not test these constructs, because we believe that the <sup>fi</sup>t of the explanation (explanation level) and the perceived ease of use and perceived usefulness of the KBS (system level) are on two different conceptual levels and it would not be correct to analyze them together.

Conducting this study in a deception detection environment may have limited the generalizability of the <sup>fi</sup>ndings. Because deception detection is inherently dif<sup>fi</sup>cult and complex for users, CFT may have a larger in<sup>fl</sup>uence in a less complex task. One of the criticisms and limitations of CFT is that the theory is usually tested in simple tasks [62,87,88]. CFT has been extended to complex tasks that involve interruptions, social dimensions, multiple tasks, or extra analysis [89,90], but empirical evidence shows that certain types of complex tasks may not bene<sup>fi</sup>t from cognitive <sup>fi</sup>t [45]. Deception detection may be one of those complex tasks for which CFT does not have a strong impact. Future research should study this phenomenon in another domain with other tasks.

Last, in terms of assessing <sup>fi</sup>t, we only looked at propensity to stereotype as our measure of <sup>fi</sup>t. Future research should look into other measures of <sup>fi</sup>t combined with explanations from KBS. One such research study could be to examine explanation <sup>fi</sup>t with different types of tasks (such as buying a replacement product versus buying a new product to ful<sup>fi</sup>ll a need).

## 5.3. Implications for practice

The results of this study show that a universal explanation will not work for all types of users. Although this is partially in line with previous research, this study takes another step toward understanding what needs to be done to develop adaptive KBS. An explanation from a KBS that cognitively <sup>fi</sup>ts with the user will increase the perceived quality of the explanation to the user. For example, when an of<sup>fi</sup>cer is interacting with a KBS designed to look for deception in a border environment, the of<sup>fi</sup>cer will want the KBS to explain the signs of deception that the KBS recognizes in the individual rather than telling about the cognitive behaviors observed in deceptive monkeys. Consequently, companies should try to learn more about their individual users when presenting them with information. One case of this would be using past purchase histories to help guide the KBS.

In the context of online shopping in which individuals are purchasing experience goods, such as books, a KBS that provides explanations for why the shopper will emotionally enjoy a book, or how others emotionally enjoyed a book, will perform better than an explanation touting the book's technical qualities. Conversely, structured tasks, like purchasing a printer, will need more of a sign-based explanation for why it is a good pick for the shopper. Explanations about how fast it can print compared to other printers will perform above those that discuss the printer's emotional qualities.

If companies can understand how their users process information, they can use that knowledge to build explanations of their KBS that <sup>fi</sup>t with their users. Fitting the explanations to the user will engage the user and allow the user to evaluate the explanation more fully. Fitting the explanations will also increase the likelihood that the user will see the explanation as high quality leading to higher perceived explanation in<sup>fl</sup>uence, and eventual action. However, we urge caution because <sup>fi</sup>tting explanations may cause users to accept the explanations regardless of the accuracy of the system.

## 6. Conclusion

KBS help decision makers make high-quality decisions. This research study explored how cognitively <sup>fi</sup>tting explanations can enhance the in<sup>fl</sup>uence exerted by these KBS. We showed that when there is a cognitive <sup>fi</sup>t between an explanation and a user, the user is more likely to spend more time reading the explanation and to be in<sup>fl</sup>uenced more strongly by the explanation. Contrary to CFT that predicts faster response times, we found that explanations that <sup>fi</sup>t with users lead to enhanced user engagement and longer response times. User engagement with explanations that <sup>fi</sup>t is explained by PEF. Therefore, systems designed to increase user engagement with KBS that can afford longer decision time should use explanations that <sup>fi</sup>t with the users.

## Acknowledgments

This research was supported by the US Department of Homeland Security through the National Center for Border Security and Immigration (Grant # 2008-ST-061-BS0002). However, any opinions, <sup>fi</sup>ndings, and conclusions or recommendations herein are those of the authors and do not necessarily re<sup>fl</sup>ect views of the US Department of Homeland Security. The views, opinions, and/or <sup>fi</sup>ndings in this report are those of the authors.

## Appendix A. Uses of cognitive <sup>fi</sup>t theory in IS

In addition to its use in studies of graphs and tables [91], CFT has been used to explain sense making in data-exploration tasks [92], ef<sup>fi</sup>cient query building [93,94], online shopping [95,96], graphs and information load [97], graphs and uncertainty [98,99], geographical information systems [100–102], accounting visualization [88,103–105], spreadsheet usage and error correction [106], expert-data and selforganizing maps [107], maps [108,109], model comprehension [110–112], ef<sup>fi</sup>cient database views [113], visual interactive simulations [114], multi-attribute data presentation [115], software development [116–118], hypertext and knowledge type [119], executive support systems [120,121], judgment strategies [122], system acceptance [123], multimedia effectiveness [124], interface design [125], decision aid features [126], pattern recognition [127], virtual reality [128], knowledge transfer [129], decision tables, trees, and rules [130], expertise and online reviews [131], as a special case of task-technology <sup>fi</sup>t [132–135], and use of a joystick in tank simulations [136].

## Appendix B. Scale items

<table><tr><td>Construct</td><td>Cronbach&#x27;s Alpha</td><td>Code</td><td>Item (* = removed from analysis)</td></tr><tr><td rowspan="6">Propensity to stereo-type [66]</td><td rowspan="6">Raw: 0.703Std: 0.696</td><td>PTS1</td><td>I feel the nationality of a person can indicate a lot about the person.</td></tr><tr><td>PTS2</td><td>I can tell a great deal about a person by knowing his/her age.</td></tr><tr><td>PTS3</td><td>I can tell a great deal about a person by knowing the person&#x27;s gender</td></tr><tr><td>PTS4</td><td>*I can form an opinion about a person within the first few minutes of interacting with the person.</td></tr><tr><td>PTS5</td><td>I find it easy to know what a person is like just by looking at him/her.</td></tr><tr><td>PTS6</td><td>*When I first meet someone I tend to notice the differences between myself and the other person.</td></tr><tr><td rowspan="4">Perceived ease of use [34]</td><td rowspan="4">Raw: 0.661Std: 0.668</td><td>PEU1</td><td>*My interaction with the system is clear and understandable.</td></tr><tr><td>PEU2</td><td>Interacting with the system does not require a lot of my mental effort.</td></tr><tr><td>PEU3</td><td>I find the system to be easy to use.</td></tr><tr><td>PEU4</td><td>*I find it easy to get the system to do what I want it to do</td></tr><tr><td rowspan="4">Perceived usefulness [34]</td><td rowspan="4">Raw: 0.885Std: 0.885</td><td>PU1</td><td>Using the system improves my performance in [the task].</td></tr><tr><td>PU2</td><td>*Using the system in [the task] increases my productivity.</td></tr><tr><td>PU3</td><td>Using the system enhances my effectiveness in [the task].</td></tr><tr><td>PU4</td><td>I find the system to be useful in [the task].</td></tr><tr><td rowspan="4">Explanation quality [32]</td><td rowspan="4">Multiple measurements</td><td>EQ1</td><td>Weak ... Strong</td></tr><tr><td>EQ2</td><td>Unpersuasive ... Persuasive</td></tr><tr><td>EQ3</td><td>Unconvincing ... Convincing</td></tr><tr><td>EQ4</td><td>Bad Argument ... Good Argument</td></tr></table>

## References

[1] Wikipedia, Watson (computer), http://en.wikipedia.org/wiki/Watson\_ (computer)2012 (accessed December 10, 2012).

[2] J. Lim, Judgmental forecasting with time series and causal information, International Journal of Forecasting 12 (1996) 139–153.

[3] M.L. Jensen, P.B. Lowry, J.K. Burgoon, J.F. Nunamaker Jr., Technology dominance in complex decision making: The case of aided credibility assessment, Journal of Management Information Systems 27 (2010) 175–202.

[4] F. Lai, J. Macmillan, D.H. Daudelin, D.M. Kent, The potential of training to increase acceptance and use of computerized decision support systems for medical diagnosis, Human Factors: The Journal of the Human Factors and Ergonomics Society 48 (2006) 95–108. http://dx.doi.org/10.1518/001872006776412306.

[5] L.R. Ye, P.E. Johnson, The impact of explanation facilities on user acceptance of expert systems advice, MIS Ouarterly 19 (1995) 157–172

[6] D.M. Lamberti, W.A. Wallace, Intelligent interface design: An empirical assessment of knowledge presentation in expert systems, MIS Quarterly 14 (1990) 279–311.

[7] R. Davis, B. Buchanan, E.H. Shortliffe, Production rules as a representation for a knowledge-based consultation program. Artificial Intelligence 8 (1977) 15–45.

[8] V. Arnold, N. Clark, P.A. Collier, S.A. Leech, S.G. Sutton, Explanation provision and use in an intelligent decision aid, Intelligent Systems in Accounting Finance & Management 12 (2004) 5–27.

[9] U. Kayande, A. De Bruyn, G.L. Lilien, A. Rangaswamy, G.H. van Bruggen, How incorporating feedback mechanisms in a DSS affects DSS evaluations, Information Systems Research 20 (2009) 527–546.

[10] W. Wang, I. Benbasat, Recommendation agents for electronic commerce: Effects of explanation facilities on trusting beliefs, Journal of Management Information Systems 23 (2007) 217–246.

[11] K.N. Papamichail, S. French, Explaining and justifying the advice of a decision support system: A natural language generation approach, Expert Systems with Applications 24 (2003) 35–48.

[12] D.S. West, N.E. Wilkin, J.P. Bentley, Role of pharmacy experience and argument types in forming beliefs about pharmacist trustworthiness, American Journal of Health Pharmacy 60 (2003) 1136–1141.

[13] R. Agarwal, S.A. Brown, M. Tanniru, Assessing the impact of expert systems: The experiences of a small <sup>fi</sup>rm, Expert Systems with Applications 7 (1994) 249–257.

[14] R.O. Duda, E.H. Shortliffe, Expert systems research, Science 220 (80) (1983) 261–268.

[15] V. Arnold, N. Clark, P.A. Collier, S.A. Leech, S.G. Sutton, The differential use and effect of knowledge-based system explanations in novice and expert judgment decisions, MIS Quarterly 30 (2006) 79–97.

[16] S. Gregor, Explanations from knowledge-based systems and cooperative problem solving: An empirical study, International Journal of Human Computer Studies 54 (2001) 81–105.

[17] L.R. Ye, The value of explanation in expert systems for auditing: An experimental investigation, Expert Systems with Applications 9 (1995) 543–556.

[18] M.S. Gönül, D. Önkal, M. Lawrence, The effects of structural characteristics of explanations on use of a DSS, Decision Support Systems 42 (2006) 1481–1493.

[20] D. Ehninger, W. Brockriede, Decision by debate, Dodd, Mead & Company, Inc., New York and Toronto, 1963.

[21] W. Brockriede, D. Ehninger, Toulmin on argument: An interpretation and application, The Ouarterly Journal of Speech 46 (1960) 44–53

[22] N. Berente, S. Hansen, J.C. Pike, P.J. Bateman, Arguing the value of virtual worlds: Patterns of discursive sensemaking of an innovative technology, MIS Quarterly 35 (2011) 685–709.

[23] A.J. Freeley, D.L. Steinberg, Argumentation and debate: critical thinking for reasoned decision making, Thomson Wadsworth, Belmont, 2005.

[24] S.E. Toulmin, The uses of argument, Cambridge University Press, Cambridge, UK 1958.

[25] G.F. Smith, P.G. Benson, S.P. Curley, Belief, knowledge, and uncertainty: A cognitive perspective on subiective probability, Organizational Behavior and Human Decision Processes 48 (1991) 291–321.

[26] S.P. Curley, G.J. Browne, G.F. Smith, P.G. Benson, Arguments in the practical reasoning underlying constructed probability responses, Journal of Behavioral Decision Making 8 (1995) 1–20.

[27] P.G. Benson, S.P. Curley, G.F. Smith, Belief assessment: an underdeveloped phase of elicitation probability, Management Science 41 (1995) 1639–1653

[28] G. Wright, G. Rowe, Group-based judgmental forecasting: an integration of extant knowledge and the development of priorities for a new research agenda, International Journal of Forecasting 27 (2011) 1–13.

[29] R.E. Petty, J.T. Cacioppo, The effects of involvement on responses to argument quantity and quality: central and peripheral routes to persuasion, Journal of Personality and Social Psychology 46 (1984) 69–81.

[30] X. Zhao, A. Strasser, J.N. Cappella, C. Lerman, M. Fishbein, A measure of perceived argument strength: reliability and validity, Communication Methods and Measures 5 (2011) 48–75.

[31] W. Wood, J.M. Quinn, Forewarned and forearmed? Two meta-analysis syntheses of forewarnings of in<sup>fl</sup>uence appeals, Psychological Bulletin 129 (2003) 119–138.

[32] J.C. Andrews, T.A. Shimp, Effects of involvement, argument strength, and source characteristics on central and peripheral processing of advertising, Psychology and Marketing 7 (1990) 195–214.

[33] D.H. McKnight, V. Choudhury, C. Kacmar, Developing and validating trust measures for e-commerce: an integrative typology, Information Systems Research 13 (2002) 334–359. http://dx.doi.org/10.1287/isre.13.3.334.81.

[34] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: Four longitudinal field studies Management Science 46 (2000) 186–204

[35] J.J. Jiang, G. Klein, R.G. Vedder, Persuasive expert systems: the in<sup>fl</sup>uence of confidence and discrepancy. Computers in Human Behavior 16 (2000) 99–109.

[36] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: toward a uni<sup>fi</sup>ed view, MIS Quarterly 27 (2003) 425–478.

[37] G.J. Browne, S.P. Curley, P.G. Benson, Evoking information in probability assessment: knowledge maps and reasoning-based directed questions, Management Science 43 (1997) 1–14.

[38] I. Vessey, Cognitive <sup>fi</sup>t: a theory-based analysis of the graphs versus tables literature, Decision Sciences 22 (1991) 219–240

[39] J.S. Eccles, C. Midgley, A. Wig<sup>fi</sup>eld, C.M. Buchanan, D. Reuman, C. Flanagan, et al., Development during adolescence: the impact of stage-environment <sup>fi</sup>t on young adolescents' experiences in schools and in families, The American Psychologist 48 (1993) 90–101.

[40] D.E. Hunt, Person–environment interaction: a challenge found wanting before it was tried, American Educational Research Association 45 (1975) 209–230.

[41] I. Vessey, R. Weber, Structured tools and conditional logic: an empirical investiga tion Communications of the ACM 29 (1986) 48–57

[42] J.R. Bettman, M.A. Zins, Information format and choice task effects in decision making, Journal of Consumer Research 6 (1979) 141–153.

[43] M.I. Hwang, Decision making under time pressure: a model for information systems research, Information Management 27 (1994) 197–203.

[44] T.M. Shaft, I. Vessey, The role of cognitive <sup>fi</sup>t in the relationship between software comprehension and modi<sup>fi</sup>cation, MIS Quarterly 30 (2006) 29–55.

[45] C. Speier, The in<sup>fl</sup>uence of information presentation formats on complex task decision-making performance, International Journal of Human Computer Studies 64 (2006).1115-1131

[46] H.A. Simon, J.R. Hayes, Understanding written problem instructions, in: L.W. Gregg (Ed.), Knowl. Cogn. Lawrence Erlbaum Associates, Potomac, MD, 1974, pp. 165–200.

[47] H.A. Simon, J.R. Hayes, The understanding process: problem isomorphs, Cognitive Psychology 8 (1976) 165–190

[48] H.-K. Lee, K.-S. Suh, I. Benbasat, Effects of task-modality <sup>fi</sup>t on user performance, Decision Support Systems 32 (2001) 27–40

[49] A. Newell, H.A. Simon, Human problem solving, Prentice Hall, Englewood Cliffs, NJ, 1972.

[50] R. Agarwal, A.P. Sinha, M. Tanniru, Cognitive <sup>fi</sup>t in requirements modeling: a study of object and process methodologies, Journal of Management Information Systems 13 (1996) 137–162.

[51] A. Chandra, R. Krovi, Representational congruence and information retrieval: towards an extended model of cognitive <sup>fi</sup>t, Decision Support Systems 25 (1999) 271–288.

[52] I. Vessey, D. Galletta, Cognitive <sup>fi</sup>t: an empirical study of information acquisition, Information Systems Research 2 (1991) 63–84.

[53] T.L. Fox, J.W. Spence, The effect of decision style on the use of a project management tool: an empirical laboratory study, The Database for Advances in Informa tion Systems 36 (2005) 28–42.

[54] N.P. Archer, M.M. Head, J.P. Wollersheim, Y. Yuan, Investigation of voice and text output modes with abstraction in a computer interface, Interacting with Computers 8 (1996) 323–345.

[55] D.L. Davis, J.H. Barnes, W.M. Jackson, Integrating communications theory, cognitive style and computer simulation as an aid to research on implementation of opera tions research, Computers and Operations Research 20 (1993) 215–225.

[56] R. Klimberg, R.M. Cohen, Experimental evaluation of a graphical display system to visualizing multiple criteria solutions, European Journal of Operational Research 119 (1999) 191–208.

[57] V. Khatri, I. Vessey, S. Ram, V. Ramesh, Cognitive <sup>fi</sup>t between conceptual schemas and internal problem representations: the case of geospatial–temporal conceptual schema comprehension, IEEE Transactions on Professional Communication 49 (2006) 109–127.

[58] V. Khatri, I. Vessey, V. Ramesh, P. Clay, S.-J. Park, Understanding conceptual schemas: exploring the role of application and IS domain knowledge, Information Systems Research 17 (2006) 81–99.

[59] J.R. Hayes, H.A. Simon, Psychological differences among problem isomorphs, in: J.N. Castellan Jr., D.B. Pisoni, G.R. Potts (Eds.), Cogn. Theory, 2nd ed.Lawrence Erlbaum Associates, Hillsdale, NJ, 1977, pp. 21–41.

[60] C.-H. Tan, H.-H. Teo, I. Benbasat, Assessing screening and evaluation decision support systems: a resource-matching approach, Information Systems Research 21 (2010) 305–326.

[61] S. Jackson, V. Stone, E. Alvarez, Socialization amidst diversity: the impact of demographics on work team oldtimers and newcomers, in: B. Staw, L. Cummings (Eds.), Res. Organ. Behav. JAI Press, Greenwich CT, 1992, pp. 45–109.

[62] I. Vessey, The effect of information presentation on decision making: a cost–bene<sup>fi</sup>t analysis, Information Management 27 (1994) 103–119.

[63] C.F. Bond Jr., B.M. Depaulo, Accuracy of deception judgments, Personality and Social Psychology Review 10 (2006) 214–234.

[64] J.F. Nunamaker Jr., D.C. Derrick, A.C. Elkins, J.K. Burgoon, M.W. Patton, Embodied conversational agent-based kiosk for automated interviewing, Journal of Manage ment Information Systems 28 (2011) 17–48.

[65] D.R. Compeau, B. Marcolin, H. Kelley, C. Higgins, Generalizability of information systems research using student subjects: a re<sup>fl</sup>ection on our practices and recommendations for future research, Information Systems Research 23 (2012) 1093–1109.

[66] S. Shrivastava, J. Gregory, Exploring the antecedents of perceived diversity, Journal of Management & Organization 15 (2009) 526–542.

[67] J.-Y. Mao, I. Benbasat, The use of explanations in knowledge-based systems: cognitive perspectives and a process-tracing analysis, Journal of Management Information Systems 17 (2000) 153–179.

[68] SAS Institute Inc., SAS 9.3 Software, 2011

[69] P.A. Pavlou, H. Liang, Y. Xue, Understanding and mitigating uncertainty in online exchange relationships: A principal–agent perspective, MIS Quarterly 31 (2007) 105-136.

[70] P.M. Podsakoff, S.B. MacKenzie, J.-Y. Lee, N.P. Podsakoff, Common method biases in behavioral research: a critical review of the literature and recommended remedies The Journal of Applied Psychology 88 (2003) 879–903. http://dx.doi.org/10.1037/ 0021-9010.88.5.879.

[71] D. Gefen, D.W. Straub, A practical guide to factorial validity using PLS-Graph: tutorial and annotated example, Communications of the Association for Information Systems 16 (2005) 91–109

[72] R.T. Cenfetelli, G. Bassellier, Interpretation of formative measurement in Information Systems research, Management Information Systems Quarterly 33 (2009) 689–707.

[73] S. Petter, D.W. Straub, A. Rai, Specifying formative constructs in Information Systems research, Management Information Systems Quarterly 31 (2007) 623–656.

[74] D. Gefen, D.W. Straub, M.-C. Boudreau, Structural equation modeling and regression: guidelines for research practice, Communications of the Association for Information Systems 4 (2000) 1–77.

[75] P.B. Lowry, J. Gaskin, Partial least squares (PLS) structural equation modeling (SEM) for building and testing behavioral causal theory: when to choose it and how to use it, IEEE Transactions on Professional Communication 57 (2014) 123-146 http://dx doiorg/10.1109/TPC 2014.2312452

[76] S.B. Mackenzie, P.M. Podsakoff, N.P. Podsakoff, Construct measurement and validation procedures in MIS and behavioral research: integrating new and existing techniques, MIS Ouarterly 35 (2011) 293–334

[77] R. Ayyagari, V. Grover, R. Purvis, Technostress: technological antecedents and implications, MIS Quarterly 35 (2011) 831–858.

[78] M.A. Chilton, B.C. Hardgrave, D.J. Armstrong, Person–job cognitive style <sup>fi</sup>t for software developers: the effect on strain and performance, Journal of Management Information Systems 22 (2005) 193–226

[79] M. Al-Fudail, H. Mellar, Investigating teacher stress when using technology Computers & Education 51 (2008) 1103–1110.

[80] F. Huda, D. Preston, Kaizen: the applicability of Japanese techniques to IT, Software Quality Journal 1 (1992) 9–26.

[81] R.W. Roeser, J.S. Eccles, A.J. Sameroff, School as a context of early adolescents' academic and social–emotional development: a summary of research <sup>fi</sup>ndings, The Elementary School Journal 100 (2000) 443.

[82] M.J. Zimmer-Gembeck, H.M. Chipuer, M. Hanisch, P.A. Creed, L. McGregor, Relationships at school and stage-environment <sup>fi</sup>t as resources for adolescent engagement and achievement, Journal of Adolescence 29 (2006) 911–933.

[83] B. Adipat, D. Zhang, L. Zhou, The effects of tree-view based presentation adaptation on mobile web browsing, MIS Quarterly 35 (2011) 99–121.

[84] A. Kamis, M. Koufaris, T. Stern, Using an attribute-based decision support system for user-customized products online: an experimental investigation, MIS Quarterly 32 (2008) 159–177.

[85] N.K. Ramarapu, M.N. Frolick, R.B. Wilkes, J.C. Wetherbe, The emergence of hypertext and problem solving: an experimental investigation of accessing and using information from linear versus nonlinear systems, Decision Sciences 28 (1997) 825–849.

[86] K. Mathieson, M. Keil, Beyond the interface: ease of use and task/technology <sup>fi</sup>t, Information Management 34 (1998) 221–230.

[87] P.Y.K. Chau, P.C. Bell, Designing effective simulation-based decision support systems: An empirical assessment of three types of decision support systems, The Journal of the Operational Research Society 46 (1995) 315–331.

[88] C. Frownfelter-Lohrke, The effects of differing information presentations of general purpose <sup>fi</sup>nancial statements on users' decisions, Journal of Information Systems 12 (1998) 99–107.

[89] C. Speier, I. Vessey, J.S. Valacich, The effects of interruptions, task complexity, and information presentation on computer-supported decision-making performance, Decision Sciences 34 (2003) 771–798.

[90] P. Xu, B. Ramesh, Impact of knowledge support on the performance of software process tailoring, Journal of Management Information Systems 25 (2008) 277–314.

[91] M. Kennedy, D. Te'eni, J.B. Treleaven, Impacts of decision task, data and display on strategies for extracting information, International Journal of Human Computer Studies 48 (1998) 159–180.

[92] J. Baker, J. Burkman, D.R. Jones, Using visual representations of data to enhance sensemaking in data exploration tasks, Journal of the Association for Information Systems 10 (2009) 533–559.

[93] A.F. Borthick, P.L. Bowen, D.R. Jones, M.H.K. Tse, The effects of information request ambiguity and construct incongruence on query development, Decision Support Systems 32 (2001) 3–25.

[94] P. De, A.P. Sinha, I. Vessey, An empirical investigation of factors in<sup>fl</sup>uencing objectoriented database querying, Information Technology and Management 2 (2001) 71–93.

[95] E. Brunelle, The moderating role of cognitive <sup>fi</sup>t in consumer channel preference Journal of Electronic Commerce Research: JECR 10 (2009) 178–195.

[96] W. Hong, J.Y.L. Thong, K.Y. Tam, The effects of information format and shopping task on consumers' online shopping behavior: a cognitive <sup>fi</sup>t perspective, Journal of Management Information Systems 21 (2004) 149–184.

[97] S.Y. Chan, The use of graphs as decision aids in relation to information overload and managerial decision quality, Journal of Information Science 27 (2001) 417-425

[98] W.N. Dilla. P.I. Steinbart, Conditions of strict uncertainty, Journal of Information Systems 19 (2005) 29–55.

[99] L.S. Mahoney, P.B. Roush, D. Bandy, An investigation of the effects of decisional guidance and cognitive ability on decision-making involving uncertainty data, Information and Organization 13 (2003) 85–110.

[100] A.R. Dennis, T.A. Carte, Using geographical information systems for decision making: extending cognitive <sup>fi</sup>t theory to map-based presentations, Information Systems Research 9 (1998) 194–203.

[101] A. Ozimec, M. Natter, T. Reutterer, Geographical information systems-based marketing decisions: effects of alternative visualizations on decision quality, Journal of Marketing 74 (2010) 94–110.

[102] M. Gluck, Understanding performance in information systems: blending relevance and competence, Journal of the American Society for Information Science 46 (1995) 446–460.

[103] R.B. Dull, D.P. Tegarden, A comparison of three visual representations of complex multidimensional accounting information, Journal of Information Systems 13 (2000).117-131

[104] C. Dunn, S. Grabski, An investigation of localization as an element of cognitive <sup>fi</sup>t in accounting model representations, Decision Sciences 32 (2001) 55–94.

[105] W.F. Wright, Superior loan collectibility judgments given graphical displays, Auditing 14 (1995) 144–154.

[106] S. Goswami, H.C. Chan, H.W. Kim, The role of visualization tools in spreadsheet error correction from a cognitive <sup>fi</sup>t perspective, Journal of the Association for Information Systems 9 (2008) 321–343.

[107] Z. Huang, H. Chen, F. Guo, J.J. Xu, S. Wu, W.-H. Chen, Expertise visualization: an implementation and study based on cognitive <sup>fi</sup>t theory, Decision Support Systems 42 (2006) 1539–1557

[108] G.S. Hubona, S. Everett, E. Marsh, K. Wauchope, Mental representations of spatial language, International Journal of Human Computer Studies 48 (1998) 705–728.

[109] J.B. Smelcer, E. Carmel, The effectiveness of different representations for managerial problem solving: Comparing tables and maps, Decision Sciences 28 (1997) 391–420.

[110] R. Agarwal, P. De, A.P. Sinha, Comprehending object and process models: an empirical study, IEEE Transactions on Software Engineering 25 (1999) 541–556.

[111] R. Agarwal, P. De, A.P. Sinha, M. Tanniru, On the usability of OO representations Communications of the ACM 43 (2000) 83–89.

[112] A. Classen, Q. Boucher, P. Heymans, A text-based approach to feature modelling: syntax and semantics of TVL, Science of Computer Programming 76 (2011) 1130-1143.

[113] D. Baldwin, Applying multiple views to information systems: a preliminary framework, ACM SIGMIS Database 24 (1993) 15–30.

[114] P.C. Bell, R.M. O'Keefe, An experimental investigation into of the ef<sup>fi</sup>cacy of visual interactive simulation, Management Science 41 (1995) 1018–1038.

[115] N.S. Umanath, I. Vessey, Multiattribute data presentation and human judgment: a cognitive <sup>fi</sup>t perspective, Decision Sciences 25 (1994) 795–824.

[116] I. Vessey, R.L. Glass, Applications-based methodologies development by application domain, Information Systems Management 11 (1994) 53–57.

[117] I. Vessey, R. Glass, Strong vs. weak approaches to systems development, Communications of the ACM 41 (1998) 99–102

[118] H.J. Nelson, J.D. Armstrong, K.M. Nelson, Patterns of transition: the shift from traditional to object-oriented development, Journal of Management Information Systems 25 (2009) 271–297.

[119] N.K. Ramarapu, The impact of hypertext versus sequential information presentation on decision making: a conceptual model, International Journal of Information Management 16 (1996) 183–193.

[120] A.H. Huang, J.C. Windsor, An empirical assessment of a multimedia executive support system, Information Management 33 (1998) 251–262.

[121] S.-Y. Hung, T.-P. Liang, Effect of computer self-ef<sup>fi</sup>cacy on the use of executive support systems, Industrial Management & Data Systems 101 (2001) 227–236.

[122] B.M. Tuttle, R. Kershaw, Information presentation and judgment strategy from a cognitive <sup>fi</sup>t perspective, Journal of Information Systems 12 (1998) 1–17.

[123] D.S. Staples, I. Wong, P.B. Seddon, Having expectations of information systems bene<sup>fi</sup>ts that match received bene<sup>fi</sup>ts: does it really matter? Information Management 40 (2002) 115–131.

[124] A.H. Huang, Effects of multimedia on document browsing and navigation: an exploratory empirical investigation, Information Management 41 (2003) 189–198.

[125] C. Speier, M.G. Morris, The in<sup>fl</sup>uence of query interface design on decision-making performance, MIS Quarterly 27 (2003) 397–423.

[126] P.R. Wheeler, D.R. Jones, The effects of exclusive user choice of decision aid features on decision making, Journal of Information Systems 17 (2003) 63–83.

[127] S.C. Hayne, The use of pattern-communication tools and team pattern recognition, IEEE Transactions on Professional Communication 48 (2005) 377–390.

[128] K.-S. Suh, Y.E. Lee, The effects of virtual reality on consumer learning: an empirical investigation, MIS Quarterly 29 (2005) 673–697.

[129] P. Meso, G. Madey, M.D. Troutt, J. Liegle, The knowledge management ef<sup>fi</sup>cacy of matching information systems development methodologies with application characteristics: an experimental study, Journal of Systems and Software 79 (2006) 15–28.

[130] J. Huysmans, K. Dejaeger, C. Mues, J. Vanthienen, B. Baesens, An empirical evaluation of the comprehensibility of decision table, tree and rule based predictive models, Decision Support Systems 51 (2011) 141–154.

[131] D.-H. Park, S. Kim, The effects of consumer knowledge on message processing of electronic word-of-mouth via online consumer reviews, Electronic Commerce Research and Applications 7 (2008) 399–410.

[132] D.L. Goodhue, R.L. Thompson, Task-technology <sup>fi</sup>t and individual performance Management Information Systems 19 (1995) 213–236

[133] D.L. Goodhue, Understanding user evaluations of information systems, Management Science 41 (1995) 1827–1844

[134] M.T. Dishaw, D.M. Strong, Supporting software maintenance with software engineering tools: a computed task-technology <sup>fi</sup>t analysis, Journal of Systems and Software 44 (1998) 107–120

[135] D.L. Goodhue, B.D. Klein, S.T. March, User evaluations of IS as surrogates for objective performance, Information Management 38 (2000) 87–101.

[136] P.A. Beckman, Concordance between task and interface rotational and translational control improves ground vehicle performance, Human Factors 44 (2002) 644–653.

Justin Scott Giboney is an assistant professor of Information Technology Management at the University at Albany. He received his Ph.D. in Management Information Systems from the University of Arizona. His research involves information security, hacking, privacy, and deception.

Susan A. Brown is a McCoy Rogers fellow and associate professor of Management Information Systems in the University of Arizona's Eller College of Management. She received her Ph.D. from the University of Minnesota and an MBA from Syracuse University. Her research interests include technology implementation, individual adoption, computer-mediated communication, technology-mediated learning, and related topics Her research has been published in MIS Quarterly, Information Systems Research, Organizational Behavior and Human Decision Processes, Journal of MIS, IEEE Transactions on Engineering Management, Communications of the ACM, Journal of the AIS, and others. She has served or is currently serving as an associate editor for MIS Quarterly, Information Systems Research, Journal of the AIS, and Decision Sciences.

Paul Benjamin Lowry is a Full Professor of Information Systems at the Department of Information Systems, City University of Hong Kong where he is also the Associate Director of the MBA program. He received his Ph.D. in Management Information Systems from the University of Arizona. He has published articles in MISQ, JMIS, JAIS, IJHCS, JASIST, ISJ, EJIS, I&M, CACM, Information Sciences, DSS, IEEETSMC, IEEETPC, SGR, Expert Systems with Applications, JBE, Computers & Security, CAIS, and others. He serves as an AE at MIS Quarterly (regular guest), European Journal of IS, Information & Management, Communications of the AIS, AIS-Transactions on HCI, and the Information Security Education Journal. He has also served as an ICIS track co-chair. His research interests include behavioral security issues (e.g., interface design to improve security, IT policy compliance, deception, computer abuse, accountability, privacy, whistle blowing, protection motivation); HCI (e.g., heuristic evaluation, self-disclosure, collaboration, culture, communication, hedonic systems use); E-commerce (e.g., trust, distrust, and branding); and Scientometrics.

Jay F. Nunamaker Jr. is Regents and Soldwedel Professor of MIS, Computer Science, and Communication and Director of the Center for the Management of Information and the National Center for border Security at the University of Arizona. He received his Ph.D. in operations research and systems engineering from Case Institute of Technology, an M.S. and B.S. in engineering from the University of Pittsburgh, and a B.S. from Carnegie Mellon University. He received his professional engineer's license in 1965. Dr. Nunamaker was inducted into the Design Science Hall of Fame in May 2008. He received the LEO Award for Lifetime Achievement from the Association of Information Systems (AIS) in December 2002 and was elected a fellow of the AIS in 2000. He was featured in the July 1997 issue of Forbes magazine on technology as one of the eight key innovators in information technology. He is widely published with an H index of 60. His specialization is in the <sup>fi</sup>elds of system analysis and design, collaboration technology, and deception detection. The commercial product, GroupSystems' think-tank, based on Dr. Nunamaker's research, is often referred to as the gold standard for structured collaboration systems. He founded the MIS Department at the University of Arizona in 1974 and served as department head for 18 years.
