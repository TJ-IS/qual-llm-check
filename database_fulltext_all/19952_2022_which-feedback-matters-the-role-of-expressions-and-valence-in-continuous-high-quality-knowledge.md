---
otero_id: 19952
otero_key: "CKBVADGA"
title: "Which feedback matters? The role of expressions and valence in continuous high-quality knowledge contribution in the online Q&A community"
authors: "Ning Wang; Yang Liu; Shengsheng Xiao"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113750"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Which feedback matters? The role of expressions and valence in continuous high-quality knowledge contribution in the online Q&A community

![](/api/attachments/CKBVADGA/fulltext/images/8523675513c054c720eb521e9053a7fe22eda0e324d9b7d916115120498e7bc1.jpg)

Ning Wang <sup>a,1</sup>, Yang Liu <sup>b,1</sup>, Shengsheng Xiao <sup>a,\*,1</sup>

<sup>a</sup> Department of Management Information Systems, Shanghai University of Finance and Economics, Shanghai 200433, China <sup>b</sup> School of Management, Hangzhou Dianzi University, Hangzhou 310018, Zhejiang, China

## A R T I C L E I N F O

Keywords: Online Q&A community Continuous knowledge contribution High-quality knowledge Feedback mechanism Feedback expressions Feedback valence

## A B S T R A C T

With the growing popularity of online Q&A communities, motivating continuous high-quality knowledge contribution is a key challenge for sustainable community development. Although feedback mechanisms are designed to meet this challenge, there is still no comprehensive understanding of the impact of feedback. Most previous research focuses on feedback valence (i.e., positive or negative) but ignores potential differences associated with the expression of feedback (i.e., textual or nontextual). To address this research gap, we classify community feedback into four types on the dimension of expression and valence to examine their effects on continuous high-quality knowledge contribution. Using a longitudinal knowledge contribution dataset collected from a leading online Q&A community, our empirical results with a series of robustness checks show that (1) positive nontextual feedback is negatively correlated with the continuous contribution of high-quality knowl edge, whereas the other three types of feedback generate positive effects; (2) textual and nontextual positive feedback generates significantly opposite effects, but there is no statistically significant difference between textual and nontextual negative feedback. The additional analyses generate a deeper understanding of feedback effects, including disassembling feedback effects on the knowledge quantity and quality, and verifying the moderating effects of user reputation values on feedback effects. This study extends research concerning feed back and continuous knowledge contribution and generates important managerial implications for the online Q&A community.

## 1. Introduction

The emergence of online Q&A communities provides a supportive context for worldwide users to communicate, collaborate, and exchange knowledge [1–3]. For the sustainable development of such a utility, participants’ continuous contribution of high-quality knowledge is essential [4–7]. On the one hand, long-term community operations need users’ continuous knowledge contribution to deal with potential issues, such as under-contribution and free-riding behaviors that most users contribute only a few answers and mainly browse knowledge contrib uted by others [8,9]. On the other hand, it is critical that the contributed knowledge is of high quality. Lack of high-quality answers may lead to question starvation, a situation where the questions receive no accept able answer (even if many answers are provided) [10]. For example, the Stack Overflow website has approximately 7 million unresolved ques tions, even though 70% have received answers [11]. An accumulation of useless knowledge reduces the efficiency of users’ knowledge-seeking and increases the cost of community operations [12]. Taking these two challenges together, continuous high-quality knowledge contribu tion in online Q&A communities is particularly important.

Feedback mechanisms are widely applied in online communities to meet these challenges and facilitate knowledge contribution [13–16]. Generally, a feedback mechanism enables participants to respond to the posted answers and knowledge providers. Existing literature on knowledge contribution in Q&A communities discusses the effects of feedback, but extant research on feedback pays considerable attention to the quantity of continuous knowledge contribution [6,7] but less to the quality of knowledge. Some studies suggest that the factors related to knowledge quantity may be different from those with knowledge quality [3,17]. Regarding this, the relationship between feedback and contin uous high-quality knowledge contribution is still unclear in current research.

When investigating feedback mechanisms, previous research has commonly classified feedback, based on different valence, into positive and negative feedback [18]. It is also noticeable that feedback can be expressed in different forms, such as textual feedback and nontextual feedback. The form is performed as detailed comments and reviews, and the latter is shown as symbols such as up-votes, down-votes, and acceptance. Studies on feedback research suggest that feedback in various modes of expression may have different results on recipients [19,20]. However, most existing studies are interested in distinguishing the effects of feedback under different valences (positive and negative) but ignore the role of feedback expressions [1,5,16].

Feedback intervention theory describes two roles of feedback: eval uation and guidance [21]. The evaluation role is mainly performed by different feedback valence [22], and the guidance role refers to the informative messages that offer suggestions. Based on the theory, non textual feedback has the primary role of evaluation via distinct symbols representing positive and negative assessments. Textual feedback plays a dominant role of guidance via content and a less implicit role of evaluation since the content may imply different valence. However, nontextual feedback is more significant as the evaluation role, since it is related to more evidential reputation changes for the recipient in the community. Additionally, self-regulation theory proposes that the evaluation of the user’s previous performance can affect their future behavior in two mechanisms [23]. One is self-efficacy which refers to the user’s confidence in their ability and is affected by the evaluation valence [24,25]. The other is self-satisfaction which refers to the extent of the user’s satisfaction with previous performance and is affected by the rewards and punishment along with the evaluation [26,27]. Conjunction with the self-regulation theory, both nontextual and textual feedback performed as evaluation could affect the recipient’s perceived self-efficacy via different valence. Thus, apart from the previous findings on the different effects of feedback valence, the impacts of feedback in different expressions given the same valence are much likely to vary.

Our research adopts a comparative perspective in two dimensions, i. e., expressions and valence, to provide a nuanced analysis of the influ ence of different types of feedback on users’ continuous high-quality knowledge contribution in online Q&A communities. Specifically, we design our study to answer the following two research questions: (1) Does feedback under different expressions and valence generate different effects on continuous contribution of high-quality knowledge? (2) Given the same valence, which expression of feedback is more powerful?

To address these research questions, we decompose feedback into four categories: positive textual feedback, negative textual feedback, positive nontextual feedback, and negative nontextual feedback. We construct panel models to examine the effects of these types of feedback on continuous high-quality knowledge contribution. The proposed models are calibrated with a granular knowledge contribution dataset in Stack Overflow (hereafter, Sof), a popular worldwide online Q&A community. Our empirical analyses provide three main findings: (1) Receiving positive nontextual feedback reduces the recipient’s contin uous high-quality knowledge contribution, whereas the other three types of feedback (negative nontextual feedback as well as positive and negative textual feedback) generate positive effects. (2) Within the positive valence, different expressions of feedback have opposite effects, in that positive textual feedback benefits continuous high-quality knowledge contribution, but positive nontextual feedback does not. (3) Within the negative valence, there is no statistically significant dif ference between textual and nontextual feedback, and both expressions are positively related to continuous high-quality knowledge contribu tion. To further explore our two research questions, we construct two additional analyses for a deeper understanding of the effects of feedback.

This study contributes to extant literature and practices on online Q&A communities in several ways. First, it provides a nuanced inves tigation of the effect of different types of feedback in online Q&A communities in the dimensions of expression and valence. To the best of our knowledge, this study is among the first to quantitively compare the feedback effects under different expressions and valence. Second, tar geting continuous high-quality knowledge contribution provides a comprehensive understanding of feedback effects compared with pre vious studies which focus on the knowledge quantity alone [1,18]. Specifically, we discover the reverse effect of positive nontextual feed back on knowledge quantity and knowledge quality, which empirically verifies the previous deduction that the factor affecting the quantity of knowledge contribution could generate different effects on knowledge quality [3,17]. Third, drawing on self-regulation theory, our study provides another potential underlying mechanism for the feedback ef fect from the perspective of self-satisfaction. Previous studies illustrate the critical role of feedback through perceived self-efficacy [28–30]. Our study shows that feedback may also influence perceived self satisfaction, leading to an increase or decrease in the extent of the re cipient’s future efforts on knowledge contribution. Our findings also have implications for managerial practice. Our quantitative evidence suggests that community managers should encourage participants to produce more textual feedback to incentivize knowledge contributors to contribute more high-quality knowledge in the future. Moreover, our findings on the moderating effect of reputation suggest that the feedback mechanism may have a stronger effect on contributors with a low reputation. Managers should therefore design other tools to motivate continuous high-quality knowledge contribution from users with higher reputation values.

## 2. Related work

## 2.1. Continuous knowledge contribution in online Q&A communities

Continuous knowledge contribution is critical for the sustainable development of online Q&A communities, which induces considerable interest in the literature [1,8,31]. Some studies explore the antecedents of continuous knowledge contribution from the perspective of individ ual motivation, both intrinsic (e.g., enjoyment in helping others, and reciprocity) [5,9,18] and extrinsic (e.g., reputation enhancement and rewards) [29,32]. Recently, an emerging stream of research has focused on the effectiveness of community mechanisms on the continuous contribution of knowledge, such as the rewards mechanism, which is universal among the online Q&A community. For example, badges are the rewards for the participants who have taken a specified number of actions of certain types. Li et al. [33] identify that the newly acquired badges can motivate the participant to increase knowledge contribution, while Anderson et al. [34] discover the different behavior modes of the participant before and after acquiring badges.

Additionally, studies targeting either the motivation for or the effect of mechanisms on continuous knowledge contribution tend to focus on the quantity of knowledge, neglecting its quality. However, some recent studies emphasize the critical role of knowledge quality in the success of knowledge communities. For example, Ghose and Han [35] argue that high-quality knowledge can decrease waiting times for knowledgeseekers and improve the duration of participation in a virtual commu nity. Moreover, it is acknowledged that the factors influencing the quantity of knowledge contribution in online Q&A communities may differ from those affecting its quality [3,17]. For instance, Lou et al. [17] propose that a reputation mechanism is more effective in facilitating the quantity than the quality of knowledge contribution.

Compared with the above existing studies, our research makes two major differences. First, the rewards mechanism, such as badges, may have a similar influence on the user’s reputation to affect their contin uous knowledge contribution as feedback, thus the literature on rewards provides some references to our study. However, different from rewards that indicate the user’s overall participation in the community, feedback is the result of interactions with peers on specific answers. Thus, apart from the motivative influence, feedback plays a different role as a reflection on the user’s previous contribution, which probably impacts the user’s continuous high-quality contribution in different mechanisms. Second, given the importance of high-quality knowledge and the different factors that may influence the quantity and quality of knowl edge, participants’ continuous high-quality knowledge contribution as an important indicator in Q&A online community is still not fully un derstood. Generally, the present study extends research on continuous knowledge contribution by comprehensively examining the effects of different feedback types, and it considers both the quality and quantity of knowledge.

## 2.2. Feedback mechanisms and knowledge contribution

Feedback mechanisms are widely applied in online communities to influence individuals’ decision-making behavior [36,37]. According to feedback intervention theory [21], feedback has two main functions: evaluation and guidance. On the one hand, feedback helps recipients to evaluate their previous performance, which affects their perceived selfefficacy and self-satisfaction and impacts their subsequent behavior [13,37]. On the other hand, feedback also provides guidance to help recipients revise their mistakes and regulate their ongoing behavior [14,19]. Online communities usually adopt both textual and nontextual expressions of feedback, where nontextual feedback is performed as evaluations, and textual feedback plays the dominant role as guidance and offers implicit evaluation for the recipient. [19].

The effectiveness of feedback on individuals’ performance largely depends on the feedback valence $( \mathrm { i . e . , }$ positive or negative) [1,38]. In online Q&A communities, most previous studies distinguish the effects of positive and negative feedback on knowledge contribution. Positive feedback, such as community rewards, signals social approval and recognition, which is thought to enhance the contributor’s perceived self-efficacy and trust and benefit their future contribution [2,38]. In contrast, negative feedback represents disapproval of and disagreement with the knowledge contributed, which may disappoint the recipient and impede their confidence in subsequent contribution [1,19].

A recent stream of studies explores the role of feedback expressions on knowledge contribution. Huang et al. [14] examine the effects of feedback on user-generated content, showing that feedback messages framed in different ways generate different effects on recipients. Chan et al. [18] compare feedback expressed by peers and by the firm under different valences. Their results show that positive peer feedback gen erates more significant effects on knowledge contribution than positive firm feedback as the recipient’s experience increases. According to these studies, the feedback effect on individuals’ knowledge contribution may change according to its expression and/or valence.

Most studies discuss the impact of feedback valence in a specific expression, but few investigate or compare the range of effects that may arise from differences in expression or valence. Rieber et al. [39] discover that nontextual feedback in the form of animated graphics is more accessible for the individual to process and interpret than textual feedback. While Gielen et al. [40] offer evidence that, compared with accurate nontextual feedback, textual feedback with a specific justifi cation is superior in improving recipients’ performances. In online Q&A communities, whether the expression (textual or nontextual) has an impact on the effectiveness of feedback is still an open question. Therefore, our study enriches feedback research by providing a nuanced understanding of various feedback effects on continuous high-quality knowledge contribution from a comparative perspective.

## 3. Hypotheses development

In this section, we first articulate the roles of feedback based on the feedback intervention theory and proceed to discuss their potential affecting mechanisms in conjunction with self-regulation theory. Then, we classify feedback into four types in the dimensions of expression and valence and propose hypotheses on their effects on the recipient’s continuous high-quality knowledge contribution. Moreover, we propose hypotheses to compare the effects of different feedback expressions given the same valence. Fig. 1 illustrates our research model.

## 3.1. Theoretical ground

According to the feedback intervention theory, feedback has two basic roles: evaluation and guidance. The evaluation role is referred to as an indicator to help the recipient assess their previous performance and the achievement of the expected goals [41]. The guidance role conveys informative messages to help the recipient learn and improve their expertise abilities [22]. Accordingly, nontextual feedback performs as symbolic signals that directly show the distinct valence, primarily playing the evaluation role. Textual feedback is generally expressed as reviews, in which the detailed text can offer information as suggestions or assists. Thus, it mainly provides the role of guidance that benefits the improvement of the recipient’s ability by the learning process. Besides, textual feedback can also partly serve as implicit evaluation that the content may convey different valence as approval or criticism.

However, compared with textual feedback, nontextual feedback is more remarkable as the role of evaluation to distinguish different valence [22]. Regarding this, we apply the self-regulation theory to differentiate the process related to nontextual and textual feedback as the role of evaluation. Self-regulation refers to the processes that in dividuals guide their goal-directed activities over time and across changing circumstances, and it comprises two aspects: self-efficacy and self-satisfaction [42]. Self-efficacy refers to the user’s perceived confi dence in their expertise abilities, which is affected by the received assessment from others. Self-satisfaction is driven by valuing outcomes relative to goals, such as the change of social reputation. Nontextual feedback provides a symbolic evaluation and is closely associated with the recipient’s social reputation, thus affects both process of selfsatisfaction and self-efficacy. In contrast, textual feedback provides an implicit evaluation and is not related to explicit reputation change, mainly influences self-efficacy process.

## 3.2. Nontextual feedback and continuous high-quality knowledge contribution

Nontextual feedback is expressed as symbolic assessment such as upvotes and down-votes, which plays an evaluation role to influence the recipient’s self-efficacy and self-satisfaction process. In different sym bols, nontextual feedback can express positive or negative in valence. Positive nontextual feedback indicates the validity of the answer, en hances the recipient’s reputation, and improves their social image in the community [28,41]. In contrast, negative nontextual feedback indicates the invalidity of the answer, decreases the recipient’s reputation, and makes them lose face in the community.

From the self-efficacy perspective, positive nontextual feedback en hances the recipient’s perception of self-efficacy, increasing their con fidence in knowledge ability. In online Q&A communities, it possibly motivates the user to answer more challenging questions [16], which objectively increases the difficulty of being evaluated as high-quality knowledge. On the contrary, receiving negative nontextual feedback will decrease the recipient’s perception of self-efficacy. It makes them re-examine their ability and answer questions that they can better handle, which probably leads to the increase of the high-quality knowledge contribution.

From the self-satisfaction perspective, positive nontextual feedback will enhance the recipient’s self-satisfaction with the previous perfor mance, which induces them to exert less effort into the subsequent knowledge contribution. For example, Xu et al. [43] note that partici pants in the Sof community significantly decrease their reputationgenerating activities, including high-quality knowledge contribution, after achieving their goals. Similarly, Goes et al. [44] find that in a hi erarchical reputation mechanism, individuals reduce their knowledge contribution efforts after crossing a certain threshold. Thus, more posi tive nontextual feedback is likely to cut down the future effort of the recipient and lead to less continuous high-quality knowledge contribu tion. In contrast, negative nontextual feedback makes the recipient dissatisfied with their previous knowledge contribution, which drives them to increase the effort in future high-quality knowledge contribu tion so as to earn back their reputation [27]. For example, in a labora tory study, Podsakoff and Farh [45] find that a subject who receives more credible negative feedback will set higher goals and perform at a higher level. Therefore, we formulate the following hypotheses:

![](/api/attachments/CKBVADGA/fulltext/images/0e62ae6db14aa987deeffad8cc8eb5ace5d005096bb0365881bc445dc76198ce.jpg)  
Fig. 1. Classification of feedback and research model.

H1. A knowledge contributor who receives more positive nontextual feedback is more likely to decrease their continuous high-quality knowledge contribution in the online Q&A community.

H2. A knowledge contributor who receives more negative nontextual feedback is more likely to increase their continuous high-quality knowledge contribution in the online Q&A community.

## 3.3. Textual feedback and continuous high-quality knowledge contribution

Textual feedback takes the form of detailed comments aiming to refine the answers, which plays a primary role of guidance, as well as an implicit role of evaluation to influence self-efficacy. Classified by different valence, positive textual feedback often contains approval and appreciation content and provides suggestions for the recipient to optimize the current answer. Negative textual feedback points out the shortcomings of the answer more directly in criticism, which also helps the recipient to improve their expertise.

As a dominant role as guidance, both positive and negative textual feedback can facilitate the learning process by providing informative messages to enhance recipients’ knowledge. Shi et al. [22] find that learning from others’ content can help the recipient improve their knowledge quality. Though, previous studies argue that positive textual feedback is more acceptable for the recipient as suggestions. Overall, both positive and negative textual feedback can generate learning effects to support the recipient to contribute high-quality knowledge in the future.

Textual feedback also acts as a form of evaluation, but this role is relatively implicit. It is similar to the effect of nontextual expression related to self-efficacy. Positive textual feedback improves the re cipient’s self-efficacy to answer more challenging questions, which is negatively associated with continuous high-quality knowledge contri bution. Negative textual feedback has the opposite impact and leads to a reverse result. Thus, we formulate the following hypotheses:

H3. A knowledge contributor who receives more positive textual feedback is more likely to increase their continuous high-quality knowledge contribution in the online Q&A community.

H4. A knowledge contributor who receives more negative textual feedback is more likely to increase their continuous high-quality knowledge contribution in the online Q&A community.

## 3.4. The effects of textual feedback versus nontextual feedback

We next compare the effects of different feedback expressions under the same valence. As we discussed above, for positive feedback, non textual and textual expressions generate the effects in the opposite di rections on the recipient’s continuous high-quality knowledge contribution. Specifically, despite the similar negative effect of both nontextual and textual feedback as the evaluation role via improving self-efficacy of the recipient, nontextual feedback induces a higher de gree of self-satisfaction, which leads to less effort in future contribution, while textual feedback plays a more primary role as guidance that fa cilitates knowledge learning, Gielen et al. [40] offer evidence that compared with nontextual feedback, textual feedback with a specific justification is superior in improving recipients’ performance. Conse quently, we formulate the following hypothesis:

H5. Positive textual feedback is more powerful than positive non textual feedback in increasing the recipient’s continuous high-quality knowledge contribution in the online Q&A community.

Nonetheless, the comparison between the effects of negative non textual and textual feedback can not be directly inferred from their in fluence mechanisms. Although they have similar part of effects as the role of evaluation via self-efficacy, each expression of feedback has an additional influence process. On the one hand, negative nontextual feedback reduces the recipient’s perception of self-satisfaction, which incentivizes them to increase the effort on future knowledge contribu tion. In this way, negative nontextual feedback can be more powerful than negative textual feedback to motivate the recipient to contribute high-quality knowledge.

On the other hand, negative textual feedback plays an extra role as guidance which enables recipients to understand their deficiencies better and learn from the critical comments [40], whereas negative nontextual feedback offers no material effect on the recipient’s exper tise. From this viewpoint, negative textual feedback can be more helpful than negative nontextual feedback to facilitate the user’s continuous high-quality knowledge contribution.

The above considerations indicate that the comparison between the effects of negative textual and nontextual feedback depends on which influence process, self-satisfaction in evaluation or the learning effect in guidance, is more powerful. Yet, it is difficult to infer the conclusion solely from the theories. Therefore, we formulate the following set of competing hypotheses:

H6a. Negative nontextual feedback is more powerful than negative textual feedback in increasing the recipient’s continuous high-quality knowledge contribution in the online Q&A community.

H6b. Negative textual feedback is more powerful than negative non textual feedback in increasing the recipient’s continuous high-quality knowledge contribution in the online Q&A community.

## 4. Research context, data, and method

## 4.1. Research context

In this study, we select a popular global online Q&A knowledge community, Stack Overflow (Sof), as our research context to trace the knowledge contribution behaviors of participants and the feedback they received. The Sof community is a question-and-answer site for profes sional and enthusiast programmers, which consists of more than 14 million users, 21 million questions, and 31 million answers.<sup>2</sup> Users can answer questions posted in the community, and others can offer textual and/or nontextual feedback on the posted answers. Fig. 2 represents the illustration of nontextual and textual feedback. Precisely, nontextual feedback consists of two different forms. One is the votes from others, such as up-votes and down-votes, which correspond to positive valence and negative valence, separately. All registered users can give up-votes when they consider the answer is useful, while only users who own relatively high reputation values can give down-votes under the costs of their reputation values.<sup>3</sup> The combining of two mechanisms confirms the appropriation and credibility of the down-vote. At the same time, nontextual feedback also contains the choice of acceptance, which is a privilege for the questioner, and only one of the followed answers can be accepted for each question. Textual feedback is the other type of feed back in Sof, which is in the form of detailed text such as comments and is accessible for all the users in the community. Previous studies under the context of Sof have verified the informativeness of textual feedback to help the recipient learn from the others [1]. In this study, we confirm the informative of textual feedback by its lexical diversity, which is a widely applied indicator in previous empirical analysis to test text credibility and quality [46,47]. The average lexical diversity of textual feedback in our context is 0.48, which is believed to be credible for the recipient.

In addition to different expressions, another feature that varies be tween nontextual feedback and textual feedback is that the former is related to the recipient’s reputation values while the latter is not. Spe cifically, positive nontextual feedback (i.e., up-votes and acceptance)

can increase user reputation values, and negative nontextual feedback (i.e., down-votes) can decrease it. The Sof community applies the reputation system to indicate the extent of the contribution a user has made to the community. With the increase of reputation values, the user owns higher social status in the community and unlocks more privileges, such as the right to down-votes. Thus, compared with textual feedback, nontextual feedback may impact the reputation mechanism to generate a different influence on the user’s continuous high-quality knowledge contribution. In sum, the large sample of participants and the simulta neous existence of these different feedback expressions and valences make Sof a promising context for our research.

## 4.2. Data and variables

To answer our research questions, we collect answer behaviors and received feedback for users on Sof.<sup>4</sup> We select users who have contrib uted high-quality answers during the observation window from January 1, 2013, to June 31, 2013.<sup>5</sup> Following previous research on continuous knowledge contribution, we apply a fixed-effect Poisson regression model to test our hypotheses, which requires at least two different ob servations for each individual [1,12]. Screening the sample under this condition yields a panel dataset of 559,367 questions and 729,168 an swers from 18,434 users. We then collect both textual and nontextual feedback on the answers posted by the target samples to construct the dependent variable, independent variables, and control variables.

## 4.2.1. Dependent variable

Previous studies tend to use helpfulness/usefulness votes as a proxy for answer quality in the online Q&A community [5,43], such as upvotes and down-votes mechanisms in our context. In Sof, up-votes/ down-votes indicate that the answer is useful/useless for voters. More over, it should be noted that answers posted early may receive more votes from participants in the community. To eliminate the potential bias of this time effect, we follow previous studies in limiting the quality measure window for each posted answer to 1 month from its posting [48].

Regarding this, high-quality knowledge refers to the answer that acquires at least one up-vote within a month of its posting, which means that at least one person considers the answer as useful. Specifically, among all the answers posted by the target sample, 66.73% of answers fit this condition to be considered as high-quality knowledge. Thus, in our main model estimation, we define the dependent variable Highquality Knowledge Contribution $( H q K C _ { i , t } )$ to represent the number of highquality answers contributed by user i in period t. Furthermore, we test the robustness of high-quality knowledge identification in other three different measurements, which also generates consistent estimation as shown in Appendix A.1.

## 4.2.2. Independent variables

The independent variables include four types of feedback classified by expression and valence. For nontextual feedback, we define the variable PosiNonText as the sum of up-votes and acceptances that user i’s contributed answers receive during period $t _ { * } ^ { 6 }$ We define the variable NegNonText in the same fashion as the sum of down-votes that user i receives during period t.

![](/api/attachments/CKBVADGA/fulltext/images/2f0b219d3976748cc545da15ad37d4ab86c620b45ca9a8c998a6177c9140f441.jpg)  
Fig. 2. The illustration of textual and nontextual feedback on the posted answer in Sof.

To distinguish the valence of textual feedback, we first apply the Vader package in Python 3.7 to evaluate the emotional preference of contents [49],<sup>7</sup> which is a widely used Natural Language Toolkit (NLTK) technology in previous empirical content analyses [50,51]. Each item of content is assigned a numeric value ranging from − 1 to 1, where 0 represents neutral emotion, − 1 indicates an extremely negative emotion, and 1 represents an extremely positive emotion. We classify each item of textual feedback as having positive, negative, and neutral valence. For example, “Yes that is what I am looking for…” and “Well written answer. Very clear and to the point…” are positive, “Got an error message…” and “I’m still having a problem with the password…” are negative, and “Does this approach still work for you?” is neutral. To validate the accuracy of the Vader approach, we ask three coders to manually divide 2000 randomly selected feedback comments into a positive, a negative, and a neutral set. We label a comment as the valence if more than half of the coders put it as this valence set. Then, we use the cross-validation method to compare the Vader results with the manually coded results and calculate the precision of the Vader approach, which is 88.2%. We then define the variable $P o s i T e x t _ { i , t }$ as the sum of positive comments that user i’s contributed answers receive during period t, and we define the variable $N e g T e x t _ { i , t }$ for the negative comments.

## 4.2.3. Control variables

We also incorporate a set of control variables into our model. First, we add Number $A n s w e r _ { i , t }$ the number of answers that user i posts in period t, and Received $A n s w e r s _ { i , t }$ the number of answers that user i receives to their questions in period t. Second, we construct cumulative indicators to control for differences in the participant’s ability and experience, including the number of questions posted by user i until period t (Total Question ), the number of months between the current period t and user i’s registration month $( T e n u r e _ { i , t } )$ , the reputation values of user i until period $t ( R e p u t a t i o n _ { i , t } ) ,$ , and the number of bronze or gold badges acquired by user i until period t (Bronze Badges , Gold Badges ). Table 1 summarizes the explanations and descriptive statistics for all variables based on the row values. For all the constructed variables, we take the log transformation of the count values. The variance inflation factors (VIFs) range from 1.43 to 5.91, with an average of 2.58, which shows there are no serious multicollinearity issues in our model.

## 4.3. Model specification and estimation

Our research compares the effects of different types of feedback on continuous high-quality knowledge contribution. Given that the dependent variable is a count variable and the distribution is highly skewed, we follow previous studies in applying the panel Poisson regression as our main estimation model [1,5]. To address potential is sues in the estimation, we design our model to take into account the following points. First, the estimation model may face potential reverse causality, since high-quality knowledge contribution may affect the feedback received, reputation change, and achievement of badges in the same observation period. To alleviate these potential endogeneity is sues, we lag the independent and control variables by one period.<sup>8</sup> As the number of contributed answers is prior to the generation of high-

Table 1  
Descriptive and statistics of the main variables.

<table><tr><td>Variables</td><td>Explanations</td><td>Max</td><td>Min</td><td>Mean</td><td>Std.</td></tr><tr><td colspan="6">Dependent variable</td></tr><tr><td> $HqKC_{i,t}$ </td><td>The number of high-quality answers, which acquired at least one up-vote within 1 month since it is posted, contributed by user i in period t.</td><td>575</td><td>0</td><td>5.68</td><td>16.30</td></tr><tr><td colspan="6">Interest variables</td></tr><tr><td> $PosiNonText_{i,t}$ </td><td>The sum of up-votes and acceptance that user i&#x27;s contributed answers receive during period t.</td><td>2484</td><td>0</td><td>19.30</td><td>60.20</td></tr><tr><td> $NegNonText_{i,t}$ </td><td>The sum of down-votes received that user i&#x27;s contributed answers receive during period t.</td><td>49</td><td>0</td><td>0.31</td><td>1.08</td></tr><tr><td> $PosiText_{i,t}$ </td><td>The sum of comments in positive emotion that user i&#x27;s contributed answers receive during period t.</td><td>483</td><td>0</td><td>4.75</td><td>14.51</td></tr><tr><td> $NegText_{i,t}$ </td><td>The sum of comments in negative emotion that user i&#x27;s contributed answers receive during period t.</td><td>195</td><td>0</td><td>1.72</td><td>5.40</td></tr><tr><td colspan="6">Control variables</td></tr><tr><td>Number  $Answers_{i,t}$ </td><td>The number of answers that user i post in period t.</td><td>667</td><td>1</td><td>8.52</td><td>21.12</td></tr><tr><td>Received  $Answers_{i,t}$ </td><td>The number of answers that user i receive in their questions in period t.</td><td>124</td><td>0</td><td>1.52</td><td>3.97</td></tr><tr><td>Total  $Question_{i,t}$ </td><td>The number of questions posted by user i during period t.</td><td>1195</td><td>0</td><td>22.47</td><td>51.56</td></tr><tr><td> $Tenure_{i,t}$ </td><td>The number of months between the current period t and user i&#x27;s registration month.</td><td>59</td><td>1</td><td>29.43</td><td>14.34</td></tr><tr><td> $Reputation_{i,t}$ </td><td>The reputation values of user i until period t.</td><td>4629412</td><td>0</td><td>5210.61</td><td>44338.41</td></tr><tr><td>Bronze  $Badges_{i,t}$ </td><td>The number of bronze badges acquired by user i during period t.</td><td>4442</td><td>0</td><td>27.02</td><td>59.43</td></tr><tr><td>Gold  $Badges_{i,t}$ </td><td>The number of gold badges acquired by user i during period t.</td><td>3236</td><td>0</td><td>13.11</td><td>39.02</td></tr></table>

quality answers, we still take the value of Number Answer at the current period in the model specification. Second, the Poisson regression model in our estimation is a panel model, which naturally presents a choice between a fixed-effects (FE) and a random-effects (RE) model. The pri mary assumption for the RE model is that the unobserved individual factors do not correlate with the covariates in the estimation model, whereas the FE model allows for this type of correlation [52]. We apply the Hausman specification test to our estimation model, and the result $( \chi ^ { 2 } = 4 9 9 7 . 2 6 , p < 0 . 0 0 1 )$ ) confirm that the FE model is the better option [53]. Third, the robust standard error is applied in our estimation model to deal with potential heteroscedasticity, autocorrelation, and overdispersion issues. Formally, we present the estimation model as follows:

$$
\begin{array}{r l} H q K C _ {i, t} = & \exp \left(\beta_ {1} \text {PosiNonText} _ {i, t - 1} + \beta_ {2} \text {NegNonText} _ {i, t - 1} + \beta_ {3} \text {PosiText} _ {i, t - 1} \right. \\ & \left. + \beta_ {4} \text {NegTex} _ {i, t - 1} + \theta \text {Control} _ {i, t} + \text {month} _ {t} + c _ {i}\right) + \varepsilon_ {i, t} \end{array}\tag{1}
$$

where the variables are as defined above. Specifically, Control is a set of variables that includes Number Answers and other control variables with a one-period lag; month is a set of month dummies that control fo time-specific effects; $c _ { i }$ indicates individual fixed-effects to control for unobserved individual time-invariant heterogeneity; and $\varepsilon _ { i , t }$ is the error term. In our estimation, we are interested in parameters $\beta _ { 1 } { - } \beta _ { 4 }$ to compare the effects of different feedback on continuous high-quality knowledge contribution.

## 5. Estimation results

## 5.1. Main results

Table 2 reports the estimation results of our main analysis under the fixed-effects panel Poisson regression model. We add the variables stepwise to provide a comprehensive identification and explanation. In Table 2, Model 1 is a null model with the control variables only; Model 2 adds the two variables for nontextual feedback; Model 3 contains the variables for all four types of feedback. The increasing values of the loglikelihood from Model 1 to Model 3 verify the explanatory power of the independent variables in the model.

We explain the estimation results in Model 3, which includes all independent variables. For nontextual feedback, the estimation coeffi cient of PosiNonText is significantly negative $( \beta _ { 1 } = - 0 . 0 2 5 , p < 0 . 0 1 ) ,$ whereas for NegNonText it is significantly positive $( \beta _ { 2 } = 0 . 0 0 6 , p < 0 . 0 5 )$ These results support H1 and H2 that a knowledge contributor receiving more positive nontextual feedback decreases their high-quality knowl edge contribution in the online Q&A community, whereas negative nontextual feedback has a positive effect on their contribution. Addi tionally, based on the t-test between $\beta _ { 1 }$ and $\beta _ { 2 } ,$ the negative effect of PosiNonText is statistically larger than the positive effect of NegNonText.

Effects of different feedback on continuous high-quality knowledge contribution.

<table><tr><td rowspan="2">Dependent variables</td><td colspan="3">Poisson FE</td></tr><tr><td>(1) HqKC</td><td>(2) HqKC</td><td>(3) HqKC</td></tr><tr><td>Interest Variables</td><td></td><td></td><td></td></tr><tr><td>PosiNonText</td><td></td><td>-0.011***(0.002)</td><td>-0.025***(0.002)</td></tr><tr><td>NegNonText</td><td></td><td>0.011***(0.003)</td><td>0.006**(0.003)</td></tr><tr><td>PosiText</td><td></td><td></td><td>0.015***(0.003)</td></tr><tr><td>NegText</td><td></td><td></td><td>0.010***(0.003)</td></tr><tr><td>Control Variables</td><td></td><td></td><td></td></tr><tr><td>Number Answer</td><td>1.126***(0.003)</td><td>1.127***(0.003)</td><td>1.127***(0.003)</td></tr><tr><td>Total Question</td><td>0.000(0.013)</td><td>0.002(0.013)</td><td>0.003(0.013)</td></tr><tr><td>Received Answers</td><td>0.002(0.003)</td><td>0.004(0.003)</td><td>0.003(0.003)</td></tr><tr><td>Tenure</td><td>0.086***(0.017)</td><td>0.078***(0.017)</td><td>0.081***(0.017)</td></tr><tr><td>Reputation</td><td>0.009***(0.003)</td><td>0.015***(0.003)</td><td>0.012***(0.003)</td></tr><tr><td>Bronze Badges</td><td>0.025**(0.010)</td><td>0.028***(0.010)</td><td>0.027***(0.010)</td></tr><tr><td>Gold Badges</td><td>0.011(0.008)</td><td>0.013(0.008)</td><td>0.011(0.008)</td></tr><tr><td>Month Dummy</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observation</td><td>64,048</td><td>64,048</td><td>64,048</td></tr><tr><td>Num of Participants</td><td>18,434</td><td>18,434</td><td>18,434</td></tr><tr><td>Log-likelihood</td><td>-60,415</td><td>-60,396</td><td>-60,392</td></tr></table>

Notes: Robust standard errors are in parentheses. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * } p <$ 0.01.

For textual feedback, the estimation coefficients of PosiText $( \beta _ { 3 } =$ $0 . 0 1 5 , p < 0 . 0 1 )$ and NegText $( \beta _ { 4 } = 0 . 0 1 0 , p < 0 . 0 1 )$ are both significant and positively associated with high-quality knowledge contribution. Accordingly, the results support H3 and H4 that positive textual feed back and negative textual feedback both incentivize the knowledge contributor to increase their high-quality knowledge contribution. We then construct the t-test to examine the magnitude of coefficients β and $\beta _ { 4 } ,$ and we find no statistically significant difference. Thus, for textual feedback, it is possible that positive and negative feedback do not generate different effects on continuous high-quality knowledge contribution.

Focusing on feedback in different expressions under the same valence, positive nontextual feedback generates a negative effect, decreasing high-quality knowledge contribution, whereas positive tex tual feedback has a positive effect. This result provides support for H5 that textual feedback is more powerful than nontextual feedback for facilitating the recipient’s high-quality knowledge contribution. For negative feedback, both textual and nontextual expressions are posi tively associated with the recipient’s high-quality knowledge contribu tion, and the t-test between the values o $: \beta _ { 2 }$ and $\beta _ { 4 }$ shows no statistically significant differences. Therefore, the results do not support either hy pothesis H6a or H6b, indicating that a difference in the expression of negative feedback (textual or nontextual) does not generate a significant difference. The results indicate two different factors, the learning effects from textual feedback and the reduced self-satisfaction from nontextual feedback, may generate the same benefits in future high-quality knowledge contribution. We also explore the interaction effects be tween positive and negative feedback in one specific expression, and the results are presented in Appendix A.3.

## 5.2. Robustness checks

In this section, we construct a series of robustness checks for our previous empirical findings. First, we construct the fixed-effects ordi nary least squares (OLS) regression in our estimation process to elimi nate potential bias from the model dependence. The OLS provides results that are easy to interpret and provides a consistent evaluation under fixed-effect estimation. Specifically, given the skewness of the original dependent variable, we take the log-transformed values of the number of high-quality answers as the dependent variable. The results of the OLS estimation, shown in column 1 of Table 3, are consistent with the main results reported above.

Second, our data may also be affected by self-selection bias since the contributor chooses questions to answer in the community, which may not be random. Accordingly, the likelihood of knowledge contribution may correlate with the explanatory variables, such as the recipient’s reputation and tenure, as well as with the quality of knowledge contri bution. To account for this potential bias, we apply Heckman’s two-stage selection model [54]. In the first stage, we remove the independent variables and calculate the Inverse Mills Ratio (IMR) to target knowl edge contribution behavior. In the second stage, we combine the IMR in our original Poisson fixed-effect estimation model and add the four types of feedback. Column 2 of Table 3 presents the second stage results, showing that the independent variables do not differ qualitatively from the results in the main research model.

Third, we consider the potential effects of outlier noise, which results in serious skewness in our dataset. To alleviate this potential bias, we reprocess the dataset, eliminating the observation with the largest number (top 1%) of high-quality knowledge contribution. The skewness then decreases from 10.39 to 2.27. We retest our main research model on the new samples, and the estimation results demonstrate the robustness of our main findings, as shown in column 3 of Table 3.

Table 3  
The estimation results of robustness checks.

<table><tr><td rowspan="2">Dependent variables</td><td>OLS regression</td><td>Heckman two-stage model</td><td>Outlier noises</td><td>Alternative measure</td></tr><tr><td>(1) HqKC</td><td>(2) HqKC</td><td>(3) HqKC</td><td>(4) Ratio</td></tr><tr><td colspan="5">Interest variables</td></tr><tr><td rowspan="2">PosiNonText</td><td>-0.029***</td><td>-0.024***</td><td>-0.032***</td><td>-0.050***</td></tr><tr><td>(0.002)</td><td>(0.002)</td><td>(0.003)</td><td>(0.004)</td></tr><tr><td rowspan="2">NegNonText</td><td>0.018***</td><td>0.005*</td><td>0.008*</td><td>0.022***</td></tr><tr><td>(0.004)</td><td>(0.003)</td><td>(0.005)</td><td>(0.006)</td></tr><tr><td rowspan="2">PosiText</td><td>0.019***</td><td>0.014***</td><td>0.022***</td><td>0.028***</td></tr><tr><td>(0.003)</td><td>(0.003)</td><td>(0.004)</td><td>(0.005)</td></tr><tr><td rowspan="2">NegText</td><td>0.019***</td><td>0.010***</td><td>0.014***</td><td>0.026***</td></tr><tr><td>(0.003)</td><td>(0.003)</td><td>(0.003)</td><td>(0.005)</td></tr><tr><td>Control Variables</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month Dummy</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td rowspan="2">Inverse Mills Ratio</td><td></td><td>0.123***</td><td></td><td></td></tr><tr><td></td><td>(0.043)</td><td></td><td></td></tr><tr><td>Observation</td><td>64,048</td><td>64,048</td><td>60,781</td><td>64,048</td></tr><tr><td># of participants</td><td>18,434</td><td>18,434</td><td>18,047</td><td>18,434</td></tr><tr><td>Log-likelihood or R2</td><td>0.753</td><td>-59,734</td><td>-52,316</td><td>-29,101</td></tr></table>

Notes: Robust standard errors are in parentheses. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * } p <$ 0.01.

Fourth, we apply an alternative measure of continuous high-quality knowledge contribution: the ratio between the number of high-quality answers and the number of posted answers in a given month. Unlike the quantity measurement, which adopts an overall perspective, the ratio indicator emphasizes the average answer quality, thereby allevi ating the effects from the number of answers. Keeping all the other covariates the same as in the main model, the estimation results under the new dependent variable Ratio (shown in column 4 of Table 3) are consistent with the main findings.

## 6. Additional analyses

In this section, we extend the main analyses by further exploring two research questions to probe our understanding of the feedback effect on continuous high-quality knowledge contribution. The first research question aims to investigate the effects of four types of feedback on continuous high-quality knowledge contribution, a composite indicator that reflects the quantity of high-quality knowledge. To detangle the underlying mechanism on the composite outcome, in the first additional analysis, we disassemble feedback effects on knowledge quantity and quality separately to understand how the different types of feedback impact continuous high-quality knowledge contribution. The second research question intends to compare the effects of different feedback expressions given the same valence, since we propose that nontextual and textual feedback is likely to play different roles and impact different factors. In the online Q&A community, the user’s reputation is a critical characteristic that serves as a proxy of their social status [5]. The per ceptions and attitudes of users on different feedback expressions are likely to vary with different reputation values [23], leading to their varying behaviors on continuous high-quality knowledge contribution. In the second analysis, we explore the moderating role of user reputation values on the relationship between feedback expressions and continuous high-quality knowledge contribution to compare how the effects of different feedback expressions vary on users with different reputation values.

## 6.1. Disassembling feedback effects on knowledge quantity and quality

To disassemble feedback effects on knowledge quantity and quality, we construct two variables to measure the quantity and quality of user knowledge contribution. For knowledge quantity, we apply the variable Number $A n s w e r s _ { i , t }$ the total number of contributed answers by user i in period t. For knowledge quality, we first define a variable $Q u a l i t y _ { j , i , t }$ to represent the quality of each answer j contributed by user i in period $t ,$ which is the number of received up-votes minus down-votes within 1 month since it is posted. Then, we define a variable Knowledge $Q u a l i t y _ { i , t }$ to measure the average knowledge quality of the answers contributed by user i in observation period $t ,$ where:

$$
\text { Knowledge   Quality } _ {i, t} = \sum \text { Quality } _ {j, i, t} / \text { Number   Answers } _ {i, t}\tag{2}
$$

We estimate the feedback effects on these two dependent variables. The panel fixed-effect Poisson model is applied targeting knowledge quantity, and the panel fixed-effect OLS model is applied targeting knowledge quality since the independent variable is a continuous vari able. Table 4 represents the results. Positive nontextual feedback is positively related to knowledge quantity but is negatively related to knowledge quality. It is consistent with our hypotheses that positive nontextual feedback may improve the user’s self-efficacy and thus in crease the quantity of future knowledge contribution. However, it boosts users’ self-satisfaction to make them reduce efforts, which results in the decrease of average knowledge quality and an overall negative effect on continuous high-quality knowledge contribution. The other three types of feedback can benefit continuous high-quality knowledge contribution by increasing both knowledge quantity and quality. Specifically, nega tive nontextual feedback takes advantage of knowledge quality improvement than negative textual feedback, while the latter increases user knowledge quantity, which leads to a close impact on continuous high-quality knowledge contribution, as shown in the main results.

## 6.2. Moderating effects of reputation values

To explore the moderating effect of reputation values, we construct four interaction terms between the user reputation values and four types of feedback and add them into the main model. Table 5 represents the estimation results. Except for positive textual feedback, the estimated coefficients of the interaction terms of the other three types of feedback are all significantly opposite to their main effects. It indicates that the reputation values reduce the feedback effects, i.e., the higher reputation values the recipient has, the weaker the effects of feedback on their continuous high-quality knowledge contribution.

Moreover, the increase of user reputation values narrows the gap between the effects of different expressions feedback. Fig. 3 represents the average marginal effects of different types of feedback with the in crease of reputation values. Specifically, for positive feedback, the advantage of textual feedback over nontextual feedback is narrowing with the increase of user reputation values. For negative feedback, although we find no statistically significant difference in the average effects of two feedback expressions in the main analysis, textual feed back is more beneficial for the users with low reputation values on continuous high-quality knowledge contribution than nontextual feed back, and the gap is gradually closing as the reputation value becomes higher.

Table 4  
Disassembling feedback effects on knowledge quantity and quality.

<table><tr><td rowspan="2">Dependent variables</td><td>Poisson FE</td><td>OLS FE</td></tr><tr><td>(1) Number Answers</td><td>(2) Knowledge Quality</td></tr><tr><td colspan="3">Interest variables</td></tr><tr><td>PosiNonText</td><td>0.068***(0.009)</td><td>-0.104***(0.008)</td></tr><tr><td>NegNonText</td><td>0.034**(0.014)</td><td>0.106***(0.016)</td></tr><tr><td>PosiText</td><td>0.038***(0.012)</td><td>0.044***(0.012)</td></tr><tr><td>NegText</td><td>0.044***(0.012)</td><td>0.044***(0.012)</td></tr><tr><td>Control Variables</td><td>Yes</td><td>Yes</td></tr><tr><td>Month Dummy</td><td>Yes</td><td>Yes</td></tr><tr><td>Observation</td><td>64,048</td><td>64,048</td></tr><tr><td># of participants</td><td>18,434</td><td>18,434</td></tr><tr><td>Log-likelihood or  $R^2$ </td><td>-158,900</td><td>0.061</td></tr></table>

Notes: Robust standard errors are in parentheses. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p$ < 0.01.

Table 5  
Moderating effects of reputation values.

<table><tr><td rowspan="2"></td><td colspan="2">Poisson FE</td></tr><tr><td>(1) HqKC</td><td>(2) HqKC</td></tr><tr><td colspan="3">Interest variables</td></tr><tr><td>PosiNonText</td><td>-0.029***(0.002)</td><td>-0.082***(0.010)</td></tr><tr><td>NegNonText</td><td>0.018***(0.004)</td><td>0.036**(0.015)</td></tr><tr><td>PosiText</td><td>0.019***(0.003)</td><td>0.031**(0.015)</td></tr><tr><td>NegText</td><td>0.019***(0.003)</td><td>0.048***(0.014)</td></tr><tr><td>Reputation*PosiNonText</td><td></td><td>0.007***(0.001)</td></tr><tr><td>Reputation*NegNonText</td><td></td><td>-0.003**(0.001)</td></tr><tr><td>Reputation*PosiText</td><td></td><td>-0.002(0.002)</td></tr><tr><td>Reputation*NegText</td><td></td><td>-0.005***(0.001)</td></tr><tr><td>Control Variables</td><td>Yes</td><td>Yes</td></tr><tr><td>Month Dummy</td><td>Yes</td><td>Yes</td></tr><tr><td>Observation</td><td>64,048</td><td>64,048</td></tr><tr><td># of participants</td><td>18,434</td><td>18,434</td></tr><tr><td>Log-likelihood</td><td>-60,393</td><td>-60,382</td></tr></table>

Notes: Robust standard errors are in parentheses. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * } p <$ 0.01.

## 7. Conclusion and discussion

## 7.1. Conclusion

The effects of feedback on continuous high-quality knowledge contribution in the online Q&A community are critical and urgent research topics. Despite the prevalence of feedback mechanisms, feed back functions depend largely on differences of expression and valence. According to feedback intervention theory and self-regulation theory, nontextual feedback play the role of evaluations to affect both the perception of self-efficacy and self-satisfaction of the recipient. In contrast, textual feedback as the role of evaluations provides implicit evaluation to influence the recipient’s perceived self-efficacy, and also offers informative guidance that enables the recipient to improve their expertise to the benefit of their subsequent knowledge contribution. To investigate and compare the feedback influence under different ex pressions and valence, we classify feedback into four different types based on expression (textual or nontextual) and valence (positive or negative). We then compare the effects of these types of feedback on the recipient’s continuous high-quality knowledge contribution. The results show that positive nontextual feedback reduces the recipient's contin: uous high-quality knowledge contribution, whereas the other three types of feedback generate positive effects. Positive textual feedback benefits continuous high-quality knowledge contribution, whereas positive nontextual feedback has the reverse effect. For negative feed back, there is no statistically significant difference between textual and nontextual feedback, both of which are positively correlated with continuous high-quality knowledge contribution. To rule out potential bias and alternative explanations, we conduct a series of robustness checks, and the results confirm our main empirical findings. We also construct two additional analyses to make a deeper understanding, including disassembling feedback effects on knowledge quantity and quality, and investigating the moderating role of user reputation values.

![](/api/attachments/CKBVADGA/fulltext/images/e86b8c1fdc4a074ae68b2cd48bd1e80046cc71f8e533c1e2089858b0c315c0a7.jpg)  
Fig. 3. The average marginal effects of four types of feedback.

## 7.2. Theoretical implications

Our study enhances the literature on knowledge contribution in online Q&A communities in several ways. To the best of our knowledge, our study is among the first to compare feedback effects with differences of expression and valence in online Q&A communities. It extends the current literature on feedback mechanisms by providing quantitative evidence that the effects of feedback expressions on the recipient’s knowledge contribution vary. At the same time, previous research on rewards pays more attention to the motivation influence of feedback [33]. Our study verifies the important role of feedback as guidance to generate learning effects on user knowledge contribution. Therefore, our research provides a nuanced understanding of feedback effects, high lighting the role of feedback expressions in motivating the recipient’s knowledge contribution.

This study also extends the literature on continuous knowledge contribution by taking into account the quality of contributed knowl edge. High-quality knowledge is essential in online communities to improve the efficiency of knowledge-seeking. The contribution of high quality answers requires more effort and expert knowledge from the contributor, and the factors that affect the quantity of knowledge contribution may differ from those that affect the quality of knowledge contribution [17]. Unlike most studies, which focus on the effectiveness of positive feedback on the quantity of knowledge contribution [1,18], we clarify nuanced differences in the effects of feedback valence on continuous knowledge contribution in terms of quality. Specifically, we find that positive nontextual feedback has a detrimental effect on continuous high-quality knowledge contribution, whereas the effect of negative feedback is positive.

Third, drawing on self-regulation theory, our study provides another potential underlying mechanism to understand the effects of feedback. Previous studies use perceived self-efficacy to illustrate the vital role of feedback [28,29]. Our study offers an alternative explanation: feedback may influence the contributor’s perceived self-satisfaction, leading to a decrease or increase in the extent of future efforts. During continuous knowledge contribution, nontextual feedback provides evaluations with extra rewards and punishment for the recipient to measure their fulfillment of expected goals in the previous performance.

## 7.3. Managerial implications

Our study has vital practical implications for managers and de velopers in the online Q&A community who use a feedback mechanism. As textual feedback of either valence can facilitate high-quality contin uous knowledge contribution, the community should guide users to provide more textual feedback to knowledge contributors. In particular, the community manager should design a mechanism that compensates users who contribute textual feedback. which requires more time and effort than nontextual feedback. Our findings also suggest that negative nontextual feedback provides an essential incentive for the recipient to contribute high-quality knowledge. Most online communities encourage positive feedback to create a friendly atmosphere. However, participants should also provide negative nontextual feedback to supervise the recipient to increase the high-quality knowledge contribution.

To strengthen knowledge contribution, Q&A online communities often employ a feedback mechanism that includes a user reputation mechanism. However, our analysis shows the heterogeneous effect of feedback on users with different reputation values. This finding confirms for community managers that the feedback mechanism effectively mo tivates high-quality knowledge contribution from newcomers whose reputation values are still low. It also alerts community managers that other tools are required to boost the high-quality knowledge contribu tion of participants with high reputation values.

## 7.4. Limitations and future work

Our study is subject to a number of limitations that call for future research. First, it emphasizes the importance of feedback expression in online Q&A communities from a comparative perspective, measuring textual feedback in ways that facilitate comparison with nontextual feedback. Future research should explore other aspects of textual feed back, such as its linguistic features, to deepen the understanding of its effects on knowledge contribution. Second, our study may also suffer from data limitations in open-source communities as we are unable to acquire detailed information about users. Future research can extend our research by further considering the potential influences of a range of user traits, including regional characteristics, age, and gender differ ences. Third, in targeting the topic of continuous high-quality knowl edge contribution, we discover that the feedback effect is inhibited by the increase in the recipient’s reputation. Given the importance of this topic in online Q&A communities, we hope that future research can design and verify mechanisms that make up for the shortcomings of the feedback mechanism.

## CRediT authorship contribution statement

Ning Wang: Formal analysis, Software, Visualization. Yang Liu: Investigation, Validation. Shengsheng Xiao: Conceptualization, Meth odology, Software, Writing – review & editing.

## Acknowledgement

This work is supported by the National Natural Science Foundation of China [grant numbers 71701119].

## Appendix A. Supplementary data

Supplementary materials to this article can be found online at htt ps://doi.org/10.1016/j.dss.2022.113750.

## References

[1] L. Chen, A. Baird, D. Straub, Why do participants continue to contribute? Evaluation of usefulness voting and commenting motivational affordances within an online knowledge community, Decis. Support. Syst. 118 (2019) 21–32.

[2] T. Guan, L. Wang, J. Jin, X. Song, Knowledge contribution behavior in online Q&A communities: an empirical investigation, Comput. Hum. Behav. 81 (2018) 137–147.

[3] C.M. Chiu, M.H. Hsu, E.T.G. Wang, Understanding knowledge sharing in virtual communities: an integration of social capital and social cognitive theories. Decis. Support. Syst. 42 (3) (2006) 1872–1888.

[4] Y.-H. Fang, C.-M. Chiu, In justice we trust: exploring knowledge-sharing continuance intentions in virtual communities of practice, Comput. Hum. Behay. 26 (2) (2010) 235–246.

[5] L. Dong, L. Huang, J. (Jove) Hou, Y. Liu, Continuous content contribution in virtual community: the role of status-standing on motivational mechanisms, Decis. Support. Syst. 132 (2020), 113283

[6] J. Jin, Y. Li, X. Zhong, L. Zhai, Why users contribute knowledge to online communities: an empirical study of an online social Q&A community, Inf. Manag. 52 (7) (2015) 840–849.

[7] W. Chen, X. Wei, K.X. Zhu, Engaging voluntary contributions in online communities: a hidden Markov model, MIS O. 42 (1) (2018) 83–100.

[8] M. Xia, Y. Huang, W. Duan, A.B. Whinston, Research note —to continue sharing or not to continue sharing? An empirical analysis of user decision in peer-to-peer sharing networks, Inf. Syst. Res. 23 (1) (2012) 247–259.

[9] M.M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic networks of practice, MIS Q. 29 (1) (2005) 35–57.

[10] N.K. Lankton, C. Speier, E.V. Wilson, Internet-based knowledge acquisition: task complexity and performance, Decis, Support, Syst, 53 (1) (2012) 55–65

[11] F. Calefato, F. Lanubile, N. Novielli, An empirical assessment of best-answer prediction models in technical Q&A sites, Empir. Softw. Eng. 24 (2) (2019) 854–901.

[12] W. He, K.-K. Wei, What drives continued knowledge sharing? An investigation of knowledge-contribution and -seeking beliefs, Decis. Support. Syst. 46 (4) (2009) 826–838.

[13] C.W. Phang, A. Kankanhalli, B.C.Y. Tan, What motivates contributors vs. lurkers?

[14] N. Huang, G. Burtch, B. Gu, Y. Hong, C. Liang, K. Wang, D. Fu, B. Yang, Motivating user-generated content with performance feedback: evidence from randomized field experiments, Manag, Sci, 65 (1) (2019) 327–345.

[15] S. Lee, D.H. Park, I. Han, New members’ online socialization in online communities: the effects of content quality and feedback on new members content-sharing intentions, Comput. Hum. Behav. 30 (2014) 344–354.

[16] J.Y. Moon, L.S. Sproull, The role of feedback in managing the internet-based volunteer work force, Inf. Syst. Res. 19 (4) (2008) 494–515.

[17] J. Lou, Y. Fang, K.H. Lim, J.Z. Peng, Contributing high quantity and quality knowledge to online Q&A communities, J. Am. Soc. Inf. Sci. Technol. 64 (2) (2013) 356–371.

[18] K.W. Chan, S.Y. Li, J. Ni, J.J.J. Zhu, What feedback matters? The role of experience in motivating crowdsourcing innovation, Prod. Oper. Manag. 30 (1) (2021)

[19] J. Hattie. H. Timperley, The power of feedback, Rey, Educ, Res, 77 (1) (2007)

[20] J. Liao, M. Huang, B. Xiao, Promoting continual member participation in firm hosted online brand communities: an organizational socialization approach, J. Bus. Res. 71 (2017) 92–101.

[21] A.N. Kluger, A. DeNisi, The effects of feedback interventions on performance: a historical review, a meta-analysis, and a preliminary feedback intervention theory, Psychol. Bull. 119 (1996) 254–284.

[22] C. Shi, P. Hu, W. Fan, L. Qiu, How learning effects influence knowledge contribution in online O&A community? A social cognitive perspective, Decis Support. Syst. 149 (2021), 113610.

[23] A.A. Nease, B.O. Mudgett, M.A. Quinones, ˜ Relationships among feedback sign, selfefficacy, and acceptance of performance feedback, J. Appl. Psychol. 84 (5) (1999) 806–814.

[24] A. Bandura, Self-efficacy mechanism in human agency, Am. Psychol. 37 (1982) 122–147.

[25] R. Santhanam, S. Sasidharan, J. Webster, Using self-regulatory learning to enhance E-learning-based information technology training, Inf. Syst. Res. 19 (2008) 26–47.

[26] C. Wang, M.K.O. Lee, Z. Hua, A theory of social media dependence: evidence from microblog users, Decis. Support. Syst. 69 (2015) 40–49.

[27] F.Y. Kuo, W.H. Wu, C. Lin, An investigation of self-regulatory mechanisms in learning to program visual basic, J. Educ. Comput. Res. 49 (2) (2013) 225–247.

[28] J. Kuem, L. Khansa, S.S. Kim, Prominence and engagement: different mechanisms regulating continuance and contribution in online communities, J. Manag. Inf. Syst. 37 (1) (2020) 162–190.

[29] L. Zhao, B. Detlor, C.E. Connelly, Sharing knowledge in social Q&A sites: the unintended consequences of extrinsic motivation, J. Manag. Inf. Syst. 33 (1) (2016) 70–100.

[30] Y. Sun, Y. Fang, K.H. Lim, Understanding sustained participation in transactional virtual communities, Decis. Support. Syst. 53 (1) (2012) 12–22.

[31] K. Zhao, A.C. Stylianou, Y. Zheng, Predicting users’ continuance intention in virtual communities: the dual intention-formation processes, Decis. Support. Syst. 55 (4) (2013) 903–910.

[32] M. Ma, R. Agarwal, Through a glass darkly: information technology design, identity verification, and knowledge contribution in online communities. Inf, Syst Res, 18 (1) (2007) 42–67.

[33] L. Zhuolun, K.-W. Huang, Can we gamify voluntary contributions to online Q&A communities? Ouantifving the impact of badges on user engagement, Proceeding Work Inf, Syst. Econ. (2012) 1–38.

[34] A. Anderson, D. Huttenlocher, J. Kleinberg, J. Leskovec, Steering user behavior with badges, in: Proceedings of the 22nd International Conference on World Wide Web, 2013, pp. 95–106.

[35] A. Ghose, S.P. Han, An empirical analysis of user content generation and usage behavior on the mobile internet, Manag. Sci. 57 (9) (2011) 1671–1691.

[36] S. Xiao, Q. Yue, The role you play, the life you have: donor retention in online

[37] W. Jabr, R. Mookeriee, Y. Tan, V.S. Mookeriee, Leveraging philanthropic behavior for customer support: the case of user support forums, MIS Q. 38 (1) (2014) 187–208.

[38] S.K. Shriver, H.S. Nair, R. Hofstetter, Social ties and user-generated content: evidence from an online social network, Manag, Sci. 59 (6) (2013) 1425–1443

[39] L.P. Rieber, M. Smith, S. Al-Ghafry, B. Strickland, G. Chu, F. Spahi, The role of meaning in interpreting graphical and textual feedback during a computer-based simulation, Comput. Educ. 27 (1) (1996) 45–58.

[40] S. Gielen, E. Peeters, F. Dochy, P. Onghena, K. Struyven, Improving the effectiveness of peer feedback for learning, Learn. Instr. 20 (2010) 304–315.

[41] A. Parker, D.S. Halgin, S.P. Borgatti, Dynamics of social capital: effects of performance feedback on network change, Organ. Stud. 37 (3) (2016) 375–397.

[42] P. Karoly, Mechanisms of self-regulation: a systems view, Annu. Rev. Psychol. 4

[43] L. Xu, T. Nian, L. Cabral, What makes geeks tick? A study of stack overflow careers,

[44] P.B. Goes, C. Guo, M. Lin, Do incentive hierarchies induce user effort? Evidence from an online knowledge exchange, Inf. Syst. Res. 27 (3) (2016) 497–516.

[45] P.M. Podsakoff, J.-L. Farh, Effects of feedback sign and credibility on goal setting and task performance, Organ, Behay, Hum, Decis, Process, 44 (1) (1989) 45–67.

[46] S.L. Humpherys, K.C. Moffitt, M.B. Burns, J.K. Burgoon, W.F. Felix, Identification Support, Syst, 50 (2011) 585–594.

[47] M.L. Jensen, J.M. Averbeck, Z. Zhang, K.B. Wright, Credibility of anonymous online product reviews: a language expectancy perspective, J. Manag, Inf, Syst. 30 (2013) 293–324.

[48] R. Beck, I. Pahlke, C. Seebach, Knowledge exchange and symbolic action in socia knowledge seekers and contributors, MIS 0 38 (4) (2014).1245–1270

[49] C. Hutto. E. Gilbert. Vader: a parsimonious rule-based model for sentiment analysis

[50] C.K.H. Lee, How guest-host interactions affect consumer experiences in the sharing economy: new evidence from a configurational analysis based on consumer reviews, Decis. Support. Syst. (2021), 113634.

[51] G. Shan, L. Zhou, D. Zhang, From conflicts and confusion to doubts: examining review inconsistency for fake review detection, Decis. Support. Syst. 144 (2021), 113513.

[52] A.C. Cameron, P.K. Trivedi, Regression Analysis of Count Data, 2nd ed., Cambridge University Press. 2013.

[53] J.A. Hausman. Specification tests in econometrics. Econometrica 46 (6) (1978) 1251–1271.

[54] J. Heckman, Sample specification bias as a selection error, Econometrica 47 (1) (1979) 153–162.

Ning Wang received his Ph.D. in Management Science and Engineering from Shangha University of Finance and Economics. He holds a bachelor of management degree in In formation Management and Information Systems from Shanghai University of Finance and Economics. His research interests include social community detection, user decision behavior and big data analysis

Yang Liu received her Ph.D. in Management Science and Engineering from Shanghai University of Finance and Economics. She is currently an Associate Professor at the School of Management, Hangzhou Dianzi University. Her work has appeared in journals such as Information Systems Research and Journal of Business Research. Her research interests include social networks, group support systems, and online user behavior.

Shengsheng Xiao is an Associate Professor at the Department of Management Information Systems, Shanghai University of Finance and Economics. His research interests include economic of information technology, online crowdfunding markets, and supply chain financing. He has published in Decision Support Systems, Information & Management, Pro duction and Operations Management and authority international conferences such as In ternational Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS) and Conference on Information Systems and Technology (CIST).
