---
otero_id: 20373
otero_key: "RANT7GYW"
title: "Influence of self-efficacy on execution discrepancy and decision performance"
authors: "Rong-Fuh Day; Feng-Yang Kuo; Yu-Feng Huang"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103470"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Influence of self-efficacy on execution discrepancy and decision performance

![](/api/attachments/RANT7GYW/fulltext/images/2b6b2519ccbdcde7477502f8c971aa2d1f022eea54a4f5a034efb82cef5ab989.jpg)

Rong-Fuh Day <sup>a</sup>, Feng-Yang Kuo <sup>b,</sup>\*, Yu-Feng Huang b

<sup>a</sup> Department of Information Management, National Chi-Nan University, Taiwan

<sup>b</sup> Department of Information Management, National Sun Yat-Sen University, Taiwan

## A R T I C L E I N F O

Keywords: Self-efficacy Decision-making Eye-tracking approach Execution discrepancy

## A B S T R A C T

Researchers of decision-making and human–computer interactions have been concerned with the issue of action slips and the development of supportive functionalities to reduce the occurrence of the slips. However, it remains unclear how to measure slips in a decision-making context and how motivational factors can help to reduce action slips. In this study, we formulate the construct of execution discrepancy to represent an individual’s deviation from his/her planned actions and propose a self-regulatory model to explain the antecedents and consequences of this construct. The model specifies that self-efficacy exerts a positive influence on the reduction of execution discrepancy that, in turn, leads to enhanced decision performance. An experiment was conducted based on the multi-attribute decision paradigm, and decision-makers’ eye movements were tracked to measure their execution discrepancy. The results support our hypothesis that self-efficacy serves as an important moti vational factor to modulate cognitive efforts needed to reduce execution discrepancy during strategy execution. In addition to its theoretical and methodological contribution to the construct of execution discrepancy, this study may have essential implications for the design of technological artifacts that can predict and prevent possible action slips.

## 1. Introduction

Action slips are common in our daily experience. An action slip is an erroneous action that deviates from an individual’s intended action [1–4]. For example, people often commit slips such as mis-ordering, skipping, or repeating steps in a prescribed action sequence [2,3]. In critical settings, minor slips such as pressing an incorrect button on the control panel of an aircraft or misreading a gauge on a medical equip ment in clinical rooms can lead to serious consequences such as air ac cidents or iatrogenic injuries [5–8]. Given that action slips can affect various aspects in daily life [4], it is not surprising that examining action slips have been the focus of many recent studies in the Information Systems (IS) community [9–12].

In general, these studies can be classified into two trends, the first of which concerns IS usage behavior. Polites and Karahanna [10] have proposed that classical predictors such as perceived usefulness and perceived ease of use might not suffice to explain usage behavior because action slips can impede the link between usage intention and actual usage. Specifically, during the introduction of a new system, users might intend to use the new system but turn to perform routines of old systems. This deviance from the intended system usage is considered an action slip that requires interventions to encourage more conscious control over behavior [10]. The importance of this line of study is that it points out an emerging IS inquiry that IT artifacts should not only sup port usefulness and ease of use, but also reduce the frequency of and loss from action slips.

The other trend comes from decision-making and decision support system (DSS) studies that attempt to address why a DSS does not always promote decision quality. One important factor that has been identified is the lack of system capabilities, including a lack of fit between system capability and task type [13]. In addition, in the scenario of multi-attribute decision-making, DSS failure can be explained with people’s tendency to choose effort-saving strategies but not accuracy-maximizing ones [14]. However, while not yet being empiri cally tested, a possible factor of DSS failure is the unrealistic assumption that decision-makers can always execute a strategy correctly. Specif ically, it has been suggested that action slips may negatively impact decision processes and outcomes and that an avenue for DSS to improve decision quality requires approaches that improve “better execution of an existing decision strategy” ([14], p. 370). For example, around 25 % of users without a DSS “iterate through the problem several times and … return to alternatives that had been previously eliminated” during the decision-making process ([15], p. 388). This dysfunctional behavior is specifically considered an action slip in the execution of an intended decision strategy [16], and therefore, several studies have proposed that DSS research should look for factors that can reduce the occurrences of action slips [14,16,17].

Moreover, investigating action slips related to strategy execution is particularly important in modern electronic commerce (EC), in which online consumers are faced with numerous choice tasks but may not execute their choice strategy correctly because online consumers are frequently overwhelmed by the amount and speed of information. On line shops display products or services using multi-attribute presenta tion, in which alternatives are paired with the same attributes for consumer to compare and choose. Consumers are required to execute strategies, or a series of steps, to perform the multi-attribute tasks and then to choose one or more products from EC choice tasks. In reality, due to the lack of competence or the task complexity, people’s strategy execution can go wrong and, subsequently, their decision-making quality is compromised, leading to the reduction of consumer welfare. Again, there has been a lack of theoretical and empirical study on reduction of action slips regarding strategy execution in multi-attribute decision-making. Besides, it remains unclear how researchers can mea sure action slips in terms of strategy execution.

To bridge this research gap, our study has chosen to incorporate the perspective of self-regulation to investigate action slips in strategy execution. In fact, studies of IS usage [10], decision-making [15], and consumer research [9] all point out that self-regulation factors such as engagement, mindfulness, or conscious control may play a critical role to reduce action slips. This is because failure of regulation, whether due to performing a distraction task or due to decrease of cognitive capacity, decreases the ability of goal-directed control and hence actual behavior might deviate from intention [18,19]. For example, the frequency of action slips might be as high as 6 times in a week in people’s daily life especially when peoples’ attention is diverted from the tasks at hand [20]. In consumer research, Labrecque (et al. 2017) also shows that action slips are more frequent when consumers’ attention are distracted; i.e., when people are using a new product relatively mindlessly and thought little about it.

In brief, this study aims to examine factors that reduce action slips in strategy execution, and draws upon the self-regulatory literature because of its importance in researching goal-directed behavior. The core construct of self-regulation literature is self-efficacy, which refers to individuals’ belief in their competence in a specific task. People with high self-efficacy are more motivated to calibrate their behaviors with goals or intentions by maintaining attention in goal-striving activities. In light of this, we theorize that self-efficacy will help to reduce action slips of strategy executions in multi-attribute decision tasks and develop a model that explains the relationships of decision-makers’ self-efficacy, execution discrepancy, and decision performance [21–24]. The execu tion discrepancy is conceptualized as a human agency’s slips in self-regulating oneself to comply with his or her intended strategy in order to arrive at a goal state, whereas self-efficacy is considered as the contributory motivational factor to the engagement of attentional re sources that decreases discrepancy [25–28]. As depicted in Fig. 1, self-efficacy in carrying out the intended strategy is considered as the main antecedent to the execution discrepancy that manifests slip in the implementation of decision processes. To validate the model, we have conducted a laboratory experiment in which participants were required to perform multi-attribute decision tasks with their eye movements recorded [29]. In addition, the eye movement data collected through the tracking device is utilized as a measurement of attention. By applying the Needleman–Wunsch algorithm (NWA) [30] on eye movement data, we develop a process index to objectively measure how discrepancy occurs between the actual and predicted strategy execution behavior. We believe that our study can broaden our understanding of slips as well as provide inspiration for possible managerial and technological in terventions to reduce the occurrences of such behavior.

The next section provides a general overview of the self-regulation perspective, reviews literature on self-efficacy and multi-attribute de cision-making, and presents our hypotheses. This is followed by a sec tion describing the NWA. Next, we describe our experiment and results, and then conclude with our findings’ theoretical and practical implications.

## 2. Literature review

## 2.1. Modeling decision strategies of a multi-attribute decision

The study of the multi-attribute decision, referring to people’s choice from a variety of alternatives that share the same set of attributes, has been an important topic in the fields of decision-making and DSS [14,15, 29,31,32]. For example, researchers have been concerned with how to design useful functions or interfaces to support multi-attribute deci sion-making in order to debias individuals’ decision-making process [15,33,34]. An important theory of multi-attribute decision-making is the adaptive decision-making framework developed by Johnson and Payne [35]. Their effort-accuracy tradeoff theory holds that a decision-maker evaluates strategies in terms of perceived effort and accuracy before selecting the most acceptable one from the strategy repository [29,31]. A variety of decision strategies, including the weighted additive rule (WADD), the satisficing heuristic, the equal weight heuristic, and the lexicographic heuristic, are available to guide a decision-maker’s cognitive operations to transform the initial problem state into the goal state in a step-by-step manner. Each step is further composed of elementary information processes (EIPs), such as reading, adding, and comparing, that are used by decision-makers to execute the selected strategy [29,31,35–37].

![](/api/attachments/RANT7GYW/fulltext/images/c01ab4bb5e13f7aef1e099d80fe3f7789be00ea372b966da0a979205e0ecfd7e.jpg)  
Fig. 1. The research model.

Previous studies have shown that the empirical execution steps for intended strategies are not always congruent with the theoretically predicted EIPs [15–17]. Specifically, Payne et al. [29] have suggested many factors to explain multi-attribute decision-making’s action slips (deviance between the intended and the executed strategy), including environmental stressors (such as time pressure and high level of distraction), computation demand (a certain step might require heavy computation), and memory constraint (people may lose track of their goal or sub-goal states). These factors can be generally categorized as limits in human cognition. However, there has been no study to examine the role of self-regulation to affect action slips in strategy execution. Our study therefore adopts the motivation factor of self-efficacy to explain the discrepancy between the actual strategy execution and the theoret ically predicted strategy execution.

## 2.2. Self-regulation perspective and self-efficacy

According to the self-regulatory perspective, human beings are characterized as being goal-directed agents, irrespective of whether the goals are self-generated or assigned by others. In pursuit of goals, an individual’s self-regulatory systems operate in concert to guide their activities along specific paths to particular goals [21,24,38]. Zimmer man [24] has provided the three-phase self-regulatory model. First, in the forethought phase, individuals undertake goal-setting and planning and generate self-motivational belief. This is followed by the perfor mance control phase in which individuals monitor and adjust their ongoing actions. Finally, in the self-reflection phase, individuals eval uate their performance and attribute their success or failure to a number of causes, which influence their future goal-setting and planning.

In this self-regulation model, self-efficacy, referring to an in dividual’s belief in his/her competence in a specific task, is considered to be at the core of the motivation process [25,39]. Self-efficacy influences the extent of interest in working on a specific problem generated by that individual as well as the degree of effort exerted to sustain his/her work in the face of difficulties ([24–26], pp. 16–18). In addition, several theorists argue that self-efficacy plays an vital role in the goal-setting phase, which is responsible for setting the level of resource available for attaining a goal [23,28,40]. The level of self-efficacy further in fluences the goal-striving activities during the performance control phase. In brief, self-efficacy has been found to significantly predict effort engagement throughout all three self-regulation phases in a variety of tasks. In light of this, we theorize that self-efficacy will exert effect on strategy executions in multi-attribute decision tasks.

## 2.3. Self-regulation perspective and strategy execution behavior

In this research, we integrate the self-regulation perspective with the adaptive decision-making theory to formulate a model of decisionmaking behavior. While the information processing paradigm charac terizes individuals as acting like mechanical processors of information, the self-regulation perspective adopts a humanistic approach with respect to the initiation and maintenance of individuals’ goal-directed behaviors. That is, the decision-making process contains a variety of motivational factors responsible for modulating cognitive resources needed to decrease execution discrepancy by aligning actual behaviors, operations, or steps with the intended ones [21,23,24,28,39].

Self-efficacy has been consistently shown to be a positive motiva tional factor that can increase the availability of people’s cognitive resource in a task [21,23,24,28,39]. Many past studies of self-efficacy have shown that high-efficacy individuals would invest greater cogni tive resource to complete the intended task [39,41,42]. For example, people with higher self-efficacy have higher level of persistence, amount of effort, and level of commitment to achieve an intended behavior [43]. That is, people can adjust the amount of cognitive resources to regulate task-related behaviors by monitoring their actual behaviors and align their behaviors with the intended ones. Importantly, the availability of cognitive resource, which can be affected by people’s attempts at self-regulation [44], may increase or diminish the ability to regulate behaviors when performing a task. For example, when people are deprived of available cognitive resources (e.g., after sleep deprivation), their ability to detect their own behavior errors decreased and, in turn, their accuracy and speed to perform tasks are both impaired [45]. Subsequently, people are also more likely to repeat the same errors and, thus, making many slips [45]. Similarly, time pressure at work may deprive some people of cognitive resources and, in turn, increase cognitive failures during work [46]. Therefore, because self-efficacy can increase cognitive resources available in a task and cognitive resources are needed for behavior regulation, it can be inferred that self-efficacy can reduce execution discrepancy.

Evidence from decision-making literature has also suggested that self-efficacy can reduce execution discrepancy. For example, individuals deprived of cognition resources are more likely to adopt simplified de cision strategies that lead to sub-optimal solutions [29,47]. Addition ally, it is shown that low search efficacy leads to greater use of the availability heuristic, while low processing efficacy leads to greater use of the anchoring and representativeness heuristics [48]. All these three types of heuristics are considered intuitive ones that do not require extensive cognitive resource and, accordingly, are more likely to result in judgment and decision-making biases [49]. Conversely, a high level of self-efficacy can encourage the use of optimal decision strategies and thus reducing biases [48]. In short, findings from previous decision-making studies suggest that self-efficacy is critical for decision-makers to reduce execution discrepancy by modulating avail able cognitive resources in a task.

Following this line of thought, we have formulated the construct of self-efficacy to carry out the intended strategy (SEIS), which is defined as the decision-maker’s belief about his/her own competence in applying a specific decision strategy to make a decision. Previous research into selfefficacy has shown that high-efficacy individuals would appropriate greater cognitive resource for the intended task [39,41,42]. Thus, it is likely that, for individuals of high SEIS, the execution of the strategy will receive greater cognitive resource support in the performance phase. Due to the increase in the available cognitive resource, decision-makers are likely to expend a higher level of concentration on the decision process [50]. As a result, the intended strategy will be executed more closely to the theoretically expected execution steps of the strategy.

We conceptually defined the strategy execution discrepancy as the difference between the theoretically predicted and decision-makers actually implemented EIPs. Specifically, we relied on the eye-tracking technology to capture eye movements as a measurement for EIPs. In decision-making research, eye-tracking has been frequently used to capture the information currently being processed [51], and it is well established that the sequence of eye fixations can reflect the order of the corresponding information currently operated on [52–55]. On the one hand, the actual EIPs of the intended strategy are represented by the sequence of actual eye-fixation sequence (AEFS), which occurs during decision-making. On the other hand, according to the EIP’s prescription of the intended strategy, its theoretical fixation sequence can be pre dicted using the sequence of EIPs involved in the prescription. This theoretically predicted eye fixation sequence is abbreviated by theo retical eye-fixation sequence (TEFS, please also refer to Section 3.4). Given that self-efficacy is a motivational factor that increases cognitive resources availability and that cognitive resource availability is critical to reduce biases and errors in decision-making, we hypothesize that self-efficacy can reduce execution discrepancy. The following hypothe sis is proposed:

H1. For individuals of higher SEIS, the discrepancy between the empirical execution steps and the TEFS of an intended strategy will be smaller.

Likewise, less discrepancy implies there is more active monitoring during strategy execution and stronger adherence to a particular strat egy. There would be fewer slips (i.e., fewer additional steps needed to correct errors or to restore forgotten steps during the execution) and, in turn, execution efficiency is increased. Specifically, discrepancy result in more wasted effort, which involves redundant or repetitive work that does not promote performance but increases the overall execution time of a task [56]. For example, when using an electronic search engine, wasted effort is defined as individuals’ inquiries that are repetitive or redundant or those that are rejected by search engines [56]. In the multi-attribute decision-making task, wasted effort includes repetitive or redundant EIPs or those EIPs that used to reverse an error. Those wasted EIPs may not only raise the likelihood of accurate choices but also lead to increase in the overall decision time. We therefore hy pothesize that:

H2. The discrepancy between the empirical execution steps and the TEFS of an intended strategy is positively related to decision time.

Similarly, when there is less discrepancy, a choice being made is more likely to be accurate, or congruent with the expectation of the intended strategy. It is highly likely that execution discrepancy not only includes repetitive or redundant EIPs but also erroneous ones, which are defined as the departures from the prescribed steps and choices [29]. For example, individuals can read a wrong value, make a wrong comparison, or miscalculate an addition or a multiplication. All those errors likely lead to a choice that is not prescribed by intended strategy. Therefore, we hypothesize H3:

H3. The discrepancy between the empirical execution steps and the TEFS of an intended strategy is negatively related to the congruence between the actual choice and the expected choice.

Finally, following H2 (higher execution discrepancy increases deci sion time) and H3 (lower execution discrepancy increases decision ac curacy), it is possible that there exists a negative relationship between decision time and congruency. This relationship has been predicted in self-regulation literature, which indicates that people with high efficacy (usually experts in a field) can perform tasks both accurately and effi ciently [57]. For example, it has been shown that, compared with those with low efficacy, people with high efficacy in using Web search perform search tasks not only more accurately but also with less execution time [58]. The reason behind this relationship is self-regulative; i.e., high-efficacy people can make good use of their cognitive resources by filtering out distraction and focus on methods with which they are most efficacious [57,58]. In the context of multi-attribute decision-making, this good use of cognitive resource suggests the reduction of discrepancy by filtering out unnecessary EIPs and focus on the intended ones, reaching both accuracy and efficiency. Hence, the fourth hypothesis is stated as:

H4. Decision time is negatively related to the congruence between the actual choice and the expected choice.

## 2.4. Eye movement as the measurement of discrepancy

The eye-mind assumption states that people are likely to fixate on an object when their mind is processing that object’s corresponding inter nal representations [51]. This assumption has provided a general justification for using eye movement as a valid indicator to the under lying cognitive process. Many studies from different fields, such as visual search, perception, reading, arithmetic education, and IS research have further explored how eye movements reflect cognitive activities [58–67]. In the field of behavioral decision-making, eye movements have also been applied to observe the external information search to infer a decision strategy. A pioneer study relevant to the choice problem is conducted by Russo and Rosen [68], who used eye tracker to explore how people resolved multi-attribute choice problems. Lohse and John son [69] further compared the eye-tracking method with the comput erized information board on decision-related indices such as percent information searched, search pattern, reacquisition rate, and variability in information search. Their study suggested that the eye movement data can effectively measure decision-making processes and strategies. Based on these studies, the sequence of eye fixations serves as the approximation of decision-makers’ underlying decision process in our study.

To measure the execution discrepancy from eye movements, we calculate the dissimilarity between the TEFS, which is derived in advance from a decision strategy’ theoretical EIPs, and the AEFS, which is collected empirically from the decision-makers’ performance during the experiment. To do so, we have adopted the method proposed by Day [70], who applied the string-editing approach [71–76] to calculate the similarity/dissimilarity between TEFS and AEFS. Known as the Lev enshtein distance [77], the similarity/dissimilarity between two strings (i.e., sequences) can reveal how divergent the empirical decision process is from the theoretical decision process. It measures the dissimilarity between two strings mainly by calculating how many edit operations (i. $\boldsymbol { \mathrm { e } } _ { \cdot \boldsymbol { s } }$ insertion, deletion, and substitution) are needed to transform one string into a target string; the more the edit operations are needed, the more dissimilar the two strings are. To find out the minimum number of edit operations necessary for the transformation and to align two sequences to each other along the entire length, also called global sequence alignment, Day [70] adopted the NWA [30] that allows flex ible specification of the cost of different edit operations optimal for a given situation. This adoption is depicted in Equation (1) (see below), which consisted of two steps: first, finding the local optimal solution, M (i,j) for two partial sequences, $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , . . . , \mathbf { x } _ { \mathrm { i } }$ in X and ${ \bf y } _ { 1 } , { \bf y } _ { 2 } , . . . , { \bf y } _ { \mathrm { j } }$ in $\mathrm { Y , }$ and, second, producing new aligned sequences. To find the local optimal solution, $\mathbf { M } ( \mathrm { i } , \mathrm { j } )$ is achieved with the best result among the three possible aligning conditions, when x and y are aligned, when $\mathbf { X _ { i } }$ is aligned with a gap, or when yj is aligned with a gap. As shown in Equation (1), S is a scoring function which generates a cost for each of the three aligning conditions. In the second step, the algorithm computes all the combi nations of partial sequences and then backtracks M(i,j) to produce new aligned sequences $\mathbf { X } '$ and Y’ for X and Y respectively. The details of the algorithm can be found in Day [70] and Needleman and Wunsch [30].

$$
M (i, j) = \text { Max } \left\{ \begin{array}{l} M (i - 1, j - 1) + S (i, j) \\ M (i - 1, j) + S (i, \text { gap }) \\ M (i, j - 1) + S (\text { gap }, j) \end{array} \right.\tag{1}
$$

## 3. Method

## 3.1. Participants, stimulus materials, and apparatus

A total of 128 graduate and undergraduate students (36 males) participated in the experiment, who were recruited at a major university in Taiwan, with ages ranging from 18 to 28 years. The decision infor mation needed by the choice problem was organized into an information matrix, which has been adopted as the standard representation for multi-attribute decision [29,31,78]. In the experiment, the information matrix had four alternatives and four attributes (see Appendix A); it was shown on the screen in the resolution of 800 × 600 pixels. The EyeLink II (SR Research, Canada) eye tracker was applied in the experiment to record the subjects’ eye movements at a sampling rate of 500 Hz. The Data Viewer software (SR Research, Canada) was used to extract the fixation data for subsequent analysis and statistical processing.

## 3.2. Task and strategies

The experimental task involved the application of two strategies [29]: the WADD and the elimination-by-aspects (EBA). In order to make the performance of each task comparable, each task was provided with an equivalent variant derived from the same information matrix. The variant was created by randomly switching the columns of the four at tributes and/or randomly switching the rows of the four alternatives in the information matrix. Doing so ensured the variants to have the same level of complexity.

## 3.3. Measurement

Two self-efficacy measures were developed, one for the WADD strategy and another for the EBA strategy. According to Bandura’s conceptualization, self-efficacy has two important dimensions: (a) magnitude, e.g., “whether I can complete a task”, and (b) gradation in strength, e.g., “How certainly I can complete a task” [25,79]. Therefore, our questionnaires, which uses Guttman’s scale [80], included these two dimensions to measure subjects’ self-efficacy.

The construct of Execution Discrepancy was developed to measure how an empirical decision process deviates from the decision process theoretically prescribed by an intended decision strategy. It was oper ationalized as the dissimilarity score between AEFS of the empirical strategy execution and TEFS of an intended strategy. In this study, the fixation on a specific piece of decision information was defined to be equivalent to the occurrence of read EIP. As a result, AEFS on a decision information matrix could be considered as the sequence of read EIPs underlying decision strategy. On the other hand, TEFS regarding the intended strategy could be derived by orderly transcribing the read EIPs involved in the EIP model of the intended strategy. Finally, the present study utilized the NWA to calculate and score the dissimilarity between TEFS and AEFS [30,70].

Decision time, representing execution efficiency, is measured with the length of time spent by subjects on completing a choice problem. This measurement is consistent with decision-making literature that efficiency can be defined in terms of the speed of decision-making [17, 81,82]. It was defined as the duration starting from the time when the information matrix for a decision problem was shown on the screen until a subject inputted his or her choice.

Finally, the construct of decision accuracy is defined as whether a choice made by subjects is consistent with the theoretically prescribed choice of the assigned strategy. Note that our experiment required the subject to execute one of the two strategies, WADD and EBA, to complete a given task. When executed properly, there is only one theoretically prescribed choice of the assigned strategy. When discrepancy occurs decision-makers can perform wrong steps and EIPs (reading a wrong value, omitting a critical value, or made errors in comparison), which lead to an unprescribed choice. Following the DSS literature that defines accuracy as the deviation from the intended strategy (e.g., [83]), we consider a choice that equals to the prescribed one accurate and all other choices incorrect.

## 3.4. Design and procedure

The main antecedent factor in our research model is self-efficacy. In this study, the subjects were randomly assigned to receive different levels of training on decision strategies: a high-training environment and a no-prior-training environment. This manipulation was designed to increase the variance of subjects’ perceived self-efficacy [25,79,84], i.e., to reduce the possibility that subjects’ efficacy levels happen to cluster in a small range, which could lead to an adverse effect of reducing the power of the statistical test. In the high training environment, subjects undertook a two-hour training course on the six decision strategies one week prior to the formal experiment before joining the experiment. During this two-hour training course the subjects were taught six deci sion strategies that suggested for multi-attribute decision-making [29]. In contrast, the no-prior-training subjects received no prior training before the experiment.

All subjects in both environments participated in the experiment on an individual basis. The experiment consisted of two sessions: a 30-min ute training session and the eye-tracking experiment session. In the 30- minute session, each subject was instructed to watch a video which described how the WADD and EAB strategy work and then practiced each of the two decision strategies three times; in each practice, the subject received feedback about their decision time on the computer screen and decision accuracy immediately after their choice was entered into the computer. Upon completion of all practices, each subject was required to complete the scales of self-efficacy on the WADD strategy and EBA strategy respectively. Methodologically, the training session was critical to our experimental design because people might have varying knowledge and expertise regarding decision-making; the training session served to ensure that each subject would thoroughly learn the two target strategies, irrespective of whether he/she had participated in the two-hour training course.

The eye-tracking experiment was conducted immediately after the training session. First, the experiment assistant put a padded leather headband of the eye tracker on the subject’s head, and then calibrated the eye tracker. Following this, the assistant launched a customized experimental program that took control of the following experimental procedure. Each subject was asked to undertake four trials, which were presented in the following way: first, the four trials were arranged into two pairs. Each pair consisted of one trial for WADD and one for EBA. While one pair was accompanied by background noise, the other pair was accompanied by silence. The purpose in introducing such back ground noise into the two trials was to compete for subjects’ attentional resource, which, in turn, increases the occurrence of slips in the decision process [2,4,85]. The experimental program then randomized the order of the two pairs, which was followed by random selection of the order of the WADD and EBA trials.

Each trial consisted of two screens. The first screen instructed the subject to complete a choice problem with an assigned strategy as accurately and quickly as possible. The following screen showed the information matrix depicting four protection lotion brands, out of which the subject was to select one. The information matrix remained on the screen until the participant inputted a choice in the program. The pro gram then recorded the subject’s choice, the duration time, as well as eye fixations throughout the entire session.

After the eye-tracking experiment, a cash compensation of NT\$ 150 was paid to each participant for participating in the experiment. If a subject had participated in the two-hour training course in advance, an additional cash compensation of NT\$ 200 was paid.

## 4. Results

Two procedures were conducted in our analysis. First, the execution discrepancy score was computed. Then, we applied the partial least squares (PLS) approach to assess our research model, showing standardized regression coefficients between constructs and $R ^ { 2 }$ values for endogenous constructs [86,87]. PLS is used because it allows us to include multiple measures for the constructs in the research model and provides estimates of the paths among constructs and it is more straightforward to reveal a mediating effect among constructs [86].

Table 2  
Table 1  
Loadings and Cross-Loadings of Measures.

<table><tr><td></td><td>Self-efficacy in Intended Strategy</td><td>Execution Discrepancy</td><td>Decision Accuracy</td><td>Decision Time</td></tr><tr><td>SEIS-1 (WADD)</td><td>0.86</td><td>-0.30</td><td>0.07</td><td>-0.30</td></tr><tr><td>SEIS-2 (EBA)</td><td>0.92</td><td>-0.38</td><td>0.28</td><td>-0.38</td></tr><tr><td>Discrepancy-1 (WADD trial 1)</td><td>-0.33</td><td>0.78</td><td>-0.15</td><td>0.50</td></tr><tr><td>Discrepancy-2 (WADD trial 2)</td><td>-0.27</td><td>0.77</td><td>-0.16</td><td>0.47</td></tr><tr><td>Discrepancy-3 (EBA trial 1)</td><td>-0.29</td><td>0.73</td><td>-0.34</td><td>0.47</td></tr><tr><td>Discrepancy-4 (EBA trial 2)</td><td>-0.25</td><td>0.72</td><td>-0.30</td><td>0.41</td></tr><tr><td>Accuracy-1 (WADD trial 1)</td><td>0.20</td><td>-0.24</td><td>0.57</td><td>-0.06</td></tr><tr><td>Accuracy-2 (WADD trial 2)</td><td>0.18</td><td>-0.10</td><td>0.55</td><td>0.04</td></tr><tr><td>Accuracy-3 (EBA trial 1)</td><td>0.17</td><td>-0.26</td><td>0.71</td><td>-0.10</td></tr><tr><td>Accuracy-4 (EBA trial 2)</td><td>0.01</td><td>-0.19</td><td>0.74</td><td>-0.02</td></tr><tr><td>Time-1 (WADD trial 1)</td><td>-0.20</td><td>0.40</td><td>0.10</td><td>0.76</td></tr><tr><td>Time-2 (WADD trial 2)</td><td>-0.26</td><td>0.45</td><td>0.01</td><td>0.76</td></tr><tr><td>Time-3 (EBA trial 1)</td><td>-0.33</td><td>0.47</td><td>-0.17</td><td>0.68</td></tr><tr><td>Time-4 (EBA trial 2)</td><td>-0.32</td><td>0.47</td><td>-0.10</td><td>0.73</td></tr></table>

## 4.1. Execution discrepancy assessment

We use the NWA to quantify execution discrepancy from eye movements. NWA quantifies the difference between two eye-movement series into a standardized score from 0 (low discrepancy) to 1 (high discrepancy). Before applying the NWA, the raw fixations were mapped to the areas of interest (AOIs) (see Appendix A). Then, we derived a sequence of AOI codes that represented the raw fixations. Further, the same AOI codes that appeared successively in the sequence had to be collapsed by keeping only one of them in the sequence instead [71,76, 88]. For example, supposed the raw sequence of AOI codes was “AABBCCDDD”, it would be collapsed into the sequence, “ABCD”, as the AEFS for later analysis. TEFS for WADD and EBA was coded similarly. Appendix A illustrates the TEFS for the WADD strategy used in this experiment.

Moreover, the scoring parameters for the algorithm are important to derive a reliable result. The study used the same scoring parameters as those Day [70] used to optimize the performance of NWA on the clas sification of different typical strategies. The parameters in our study were configured as follows: the gap penalty was set as -1, the score for matched alignment was set as $^ { 3 , }$ and the score for mismatched alignment was set as -5.

## 4.2. Structural model assessment

PLS allowed us to examine the predictive validity of SEIS and execution discrepancy to the decision time and accuracy. This led to focus on the paths rather than the model fitness. Smart PLS (version 2.0. M3) was used [89]. We both assess how well the measures relate to the associated constructs, and then evaluate the hypothesized relationships at the theoretical level. Tests of significance for all paths were performed using the bootstrap resampling method [90] with the number of samples set to 5000.

Since each subject was assigned the two kinds of strategies, WADD and EBA, to resolve four choice problems, two for WADD and two for EBA, we specified indicator variables for each latent variable in the following way. The latent construct of SEIS was measured with the two indicator variables: self-efficacy in applying the WADD strategy and selfefficacy in applying the EBA strategy. The four scores of the dissimilarity between the AEFS and the TEFS in terms of each choice problem were used as the measurement variables for the execution discrepancy construct. Note that all the levels of SEIS, regardless of their assigned manipulation group, were all simultaneously included in the measure ment model to predict the dependent variables and hence a check on the manipulation was not performed. Similarly, the decision time was measured with the four decision times related to the four choice prob lems, while the decision accuracy construct was measured with the four decision accuracies relating to the four choice problems. The crossloading of indicators (Table 1) shows evidence for discriminant val idity, since the loadings of indicators on their respective latent variables are higher than those of other indicators on these latent variables. Moreover, the composite reliability scores (Table 2) of all constructs are above $0 . 7 ,$ the acceptable level for internal consistency. For a model to have adequate discriminate validity, the square root of the average variance extracted (AVE, the diagonal cells) of the latent variables should be greater than the correlations with other variables in the off diagonal cells [91]. This criterion is satisfied in this model (Table 2).

The structural model estimates are summarized in Table 3. As showr in Fig. 2, all the paths are significantly validated with the exception of path H4 (β = 0.209). SEIS has a significant negative influence on execution discrepancy (H1, β=-0.382, p < .001), which, in turn, exerts a significant positive influence on decision time $( \mathrm { H } 2 , \beta = 0 . 6 1 8 , \beta < . 0 0 1 )$ and a significant negative influence on decision accuracy (congruency) (H3,β=-0.448, p < .001). Finally, in line with our expectation, decision time has a positive correlation with decision accuracy; however, this relationship is not statistically significant. The exploratory power of the structural model is also estimated with the averaged $R ^ { 2 }$ of the dependent constructs in the model, which is 0.219 (see Table 4). The $R ^ { 2 }$ values of all three constructs are considerably higher than the minimum threshold of 0.1.

Internal Consistency and Discriminant Validity.

<table><tr><td></td><td>Composite Reliability</td><td>Self-efficacy in Intended Strategy</td><td>Execution Discrepancy</td><td>Decision Accuracy</td><td>Decision Time</td></tr><tr><td>Self-efficacy in Intended Strategy</td><td>0.89</td><td>0.89</td><td></td><td></td><td></td></tr><tr><td>Execution Discrepancy</td><td>0.84</td><td>-0.38</td><td>0.75</td><td></td><td></td></tr><tr><td>Decision Accuracy</td><td>0.74</td><td>0.21</td><td>-0.32</td><td>0.65</td><td></td></tr><tr><td>Decision Time</td><td>0.82</td><td>-0.39</td><td>0.62</td><td>-0.07</td><td>0.73</td></tr></table>

Table 3  
Structural model estimates.

<table><tr><td>Hypothesis</td><td>PLS path coefficient</td><td>t-Statistics</td><td>p-Values</td></tr><tr><td>H1: Self-efficacy→Execution discrepancy</td><td>β=-0.382</td><td>5.624</td><td>p&lt;.001, supported</td></tr><tr><td>H2: Execution discrepancy →Decision time</td><td>β = 0.618</td><td>11.709</td><td>p&lt;.001, supported</td></tr><tr><td>H3: Execution discrepancy →Decision accuracy</td><td>β=-0.448</td><td>5.048</td><td>p&lt;.001, supported</td></tr><tr><td>H4: Decision time→Decision accuracy</td><td>β = 0.209</td><td>1.267</td><td>unsupported</td></tr></table>

In addition, a competing model is used as a contrast for revealing the significant role of execution discrepancy. The competing model consists only of SEIS, decision time, and decision accuracy (see Fig. 3). Compared with the original model, the $R ^ { 2 }$ of decision time and decision accuracy in the competing model decrease substantially. Collectively, these analyses indicate that the construct of execution discrepancy does serve as a contributing mediating variable between self-efficacy and decision time and accuracy, and our operationalization of this construct contributes to future studies to delineate the theoretical effect between decision time and decision accuracy.

## 5. Discussion and conclusion

In this research, we have employed the eye-tracking technology to investigate the role of self-efficacy in attention engagement in decision strategy execution and how this attention engagement may influence the occurrence of action slips. We formulate the construct of execution discrepancy based on the eye-movement data and develop a regulatory model to examine its antecedents and consequences. This model show that the SEIS, self-efficacy in carrying out an intended strategy, exerts a significant influence on execution discrepancy, which, in turn, impacts decision performance in terms of both efficiency and accuracy. The re sults provide support for our proposition that SEIS may serve as an important motivational factor in modulating cognitive effort engage ment during strategy execution. Specifically, an individual with higher SEIS may appropriate a higher level of mental resource to avoid slips during the execution of planned EIPs, leading to better performance. Theoretically, our study demonstrates that it is possible to integrate the self-regulatory perspective and the multi-attribute decision-making framework that results in enhanced explanatory power. In addition, the application of the eye-tracking technology to compute the dissimilarity between the TEFS and the AEFS can provide a new methodological approach to the investigation of strategy execution behavior.

Our study demonstrates that the strategy execution behaviors may vary with different levels of self-regulation: the higher is the level of selfefficacy, the less likely that action slips may occur. This result contrib utes to the decision-making and DSS literature by examining the assumption that strategy can be correctly executed and by providing self-efficacy as a determinant to reduce action slips in terms of strategy execution. Previously, DSS studies have revealed that DSS might not promote people’s decision quality. Reasons to explain this failure include system design (insufficiency of system capabilities), contingency to the work environment (lack of fit to specific task types), and human factor (decision-makers’ tendency to save effort) [14,15]. Our action slip study adds self-efficacy as an additional explanatory factor. This implies that methods that can promote self-efficacy are likely to increase DSS performance. For example, the four general methods to promote efficacy can be used: mastery experience by providing adequate training, vicarious learning by providing seeded teachers, social persuasion by encouraging and motivating users, and even physiological factors by decreasing user fatigue. By using these methods, people could execute their intended strategy with a high level of accuracy and therefore in crease decision performance.

Our study also contributes to the IS usage and acceptance studies by showing that efficacy can strengthen the link between intention and usage. The study by Polites and Karahanna [10] has proposed that behavior intention might not translate to actual behavior during the introduction of a new IS because routines of old systems might inter vene. They further suggest that one useful method to reduce deviance between intention and actual behavior of IS usage is to provide training-in-context because training increases feelings of self-efficacy. Our study provides the evidence, in a decision-making context, to sup port their proposition by showing that self-efficacy can reduce the gap between usage intention and actual behavior.

Table 4  
R<sup>2</sup> of endogenous constructs.

<table><tr><td>Endogenous construct</td><td> $R^{2}$ </td></tr><tr><td>Execution Discrepancy</td><td>0.146</td></tr><tr><td>Decision time</td><td>0.382</td></tr><tr><td>Decision accuracy</td><td>0.129</td></tr><tr><td>Averaged</td><td>0.219</td></tr></table>

![](/api/attachments/RANT7GYW/fulltext/images/6febf2e60a3f6007d9701eb548865c5966a0dc95010841e9b92064ddb2d4b111.jpg)  
Fig. 2. Model parameters for the research model.

![](/api/attachments/RANT7GYW/fulltext/images/90f4a8d283d66199d36c6e4d8d3d4e431385dac25a87e09f32162c3b9368e07e.jpg)  
Fig. 3. Model parameters for the competing model.

Our eye-tracking algorithm to measure strategy execution not only benefits future research but also can be incorporated into AI-based software agents and machines. Today, much research has been con ducted to build smarter and smarter machines. Yet, we are reminded of the old saying, “to err is human”. In fact, today’s age of smart machine is also seen by many experts as the age of human–machine (AI) collabo ration [92] and the need to lessen possible slips is even greater in the age of smart machine: as the intelligent and autonomous machines begin to alter how work is done in all manner of industries, the need fo human–machine collaboration has actually increased, not diminished, because there remain potentially destructive limitations of the tech nology. The eye-movement data offers a way to develop collaborative systems that are intelligent in both completing tasks and understanding human users. For example, autonomous vehicles that are equipped with the latest computer vision and deep learning technologies would still require data about the driver's cognitive state to attain effective human-machine collaboration. The eye-tracking technology, which en ables automatic collection of eye-movement data, can be important to design smart systems that are capable of detecting the driver’s state of attention and provide suitable assistance during critical moments. Our measurement of execution discrepancy could be implemented as a process monitoring function to remind the driver of the extent of strat egy execution discrepancy, and then providing them with appropriate guidance. In addition, our findings suggest that a possible intervention for enhancing the strategy execution can be developed by bolstering driver self-efficacy to handle critical situations.

## 5.1. Limitation and future research

One important limitation of our study is that the decision informa tion layout accords with the design of Payne’s classical experiment [29]. This design is much simpler than the real world purchasing environment and has the merit of excluding confounding factors. However, it is generally argued that the simplification reduces the external validity of the experiment. Future research can be conducted to evaluate the effect of designs that are more realistic and aesthetic, as those seen in Amazon. com. In addition, this study can provide guidance for the design of functionalities in designing IT-based interventions. For example, future research might develop a “self-efficacy inducing mechanism” into IT artifacts, and/or solution process monitoring functions based on our new measurement of execution discrepancy.

It is also important to note that our experiment includes only a stu dent sample. Although employing student samples has been common in the studies of self-efficacy and decision-making as well as in studies employing the eye-tracking technology in IS research (e.g., [14,43,60, 93]), the extent to which we can generalize from our student sample to the people in general remains unclear. Given that university students are young adults, caution should be exercised to generalize our results to ward other demographic groups such as elderly people or those who have less access of educational resources.

Finally, with regard to theoretical development, in this study we have established the novel construct of execution discrepancy and show that it effectively mediates between self-efficacy and performance. However, how execution discrepancy can interact with other variables that are related to self-efficacy remains untested and deserves future examinations. For example, it is likely that execution discrepancy is an immediate predictor of performance, and therefore, studies can be conducted to evaluate how competence-related factors such as task ef ficiency, risk management, time management, and expertise are medi ated by execution discrepancy to affect performance. Another direction of future study might integrate significant factors relating to the design of interventions with our proposed model in order to examine their combined influence on strategy execution behavior. For example, future researchers might jointly examine the effects of the motivational factor and EIP-automating aids on strategy execution, which was a significant idea proposed by Todd and Benbasat [15].

## Author statement

We are unable to deposit our research data online because the sub jects’ consent document states that their data can only be used for the sole purpose of this research.

## Acknowledgment

This research is sponsored by the NSC of Taiwan, grant no. 99-2410- H-260-050-.

Appendix A

<table><tr><td></td><td>SPF</td><td>Polished</td><td>Moisture</td><td>Fresh</td></tr><tr><td>Cutoff value</td><td>3AOI(21)</td><td>1AOI(22)</td><td>2AOI(23)</td><td>4AOI(24)</td></tr><tr><td>Weight</td><td>4AOI(17)</td><td>5AOI(18)</td><td>1AOI(19)</td><td>2AOI(20)</td></tr><tr><td>Protection Lotion 1</td><td>3AOI(01)</td><td>1AOI(02)</td><td>4AOI(03)</td><td>2AOI(04)</td></tr><tr><td>Protection Lotion 2</td><td>2AOI(05)</td><td>3AOI(06)</td><td>4AOI(07)</td><td>1AOI(08)</td></tr><tr><td>Protection Lotion 3</td><td>3AOI(09)</td><td>2AOI(10)</td><td>1AOI(11)</td><td>4AOI(12)</td></tr><tr><td>Protection Lotion 4</td><td>4AOI(13)</td><td>1AOI(14)</td><td>3AOI(15)</td><td>4AOI(16)</td></tr></table>

The above figure demonstrates an information matrix used in our study. In the figure, the areas of interest, AOIs, are enclosed with the dashed rectangles, and each AOI is identified by the number in parentheses. With respect to this choice problem, the theoretically predicted fixation sequence (TFS) for the WADD strategy can be prescribed in the AOI code as follows: 17, 1, 18, 2, 19, 3, 20, 4, 17, 5, 18, 6, 19, 7, 20, 8, 17, 9, 18, 10, 19, 11, 20, 12, 17, 13, 18, 14, 19, 15, 20, 16.

## References

[11 E. Hollnagel, The phenotype of erroneous actions, Int, J. Man, Stud, 39 (1) (1993) 1–32.

[2] D.A. Norman, Categorization of action slips, Psychol. Rev. 88 (1) (1981) 1–15

[3] D.A. Norman, The Design of Everyday Things, Basic Books, New York, 1988.

[4] J. Reason, Human Error, Cambridge University Press, New York, 1990

[5] M.M. Botvinick, L.M. Bylsma, Distraction and action slips in an everyday task: evidence for a dynamic representation of task context. Psychon, Bull, Rey. 16 (2) (2005).1011-1017

[6] R.B. Duffey, J.W. Saull, Errors in technological systems, Hum. Fact. Ergon. Manuf Serv. Ind. 13 (4) (2003) 279–291.

[7] M.S. Sanders, E.J. McCormick, Human Factors in Engineering and Design, 7 ed., McGraw-Hill book company., Boston, 1993.

[8] J. Zhang, V.L. Patel, T.R. Johnson, E.H. Shortliffeb, A cognitive taxonomy of medical errors, J. Biomed. Inform. 37 (3) (2004) 193–204.

[9] J.S. Labrecque, W. Wood, D.T. Neal, N. Harrington, Habit slips: when consumers

[10] G.L. Polites, E. Karahanna, The embeddedness of information systems habits in organizational and individual level routines: development and disruption, Mis Q. (2013) 221–246.

[11] I.A. Taiba, A.S. McIntosha, C. Caponecchiac, M.T. Baysari, A review of medical error taxonomies: a human factors perspective, Saf. Sci. 49 (5) (2011) 607–615.

[12] A. Vishwanath, Examining the distinct antecedents of E-Mail habits and its influence on the outcomes of a phishing attack, J. Comput. Commun. 20 (5) (2015) 570–584.

[13] S.L. Jarvenpaa, The effect of task demands and graphical format on information processing strategies, Manage. Sci. 35 (3) (1989) 285–303.

[14] P. Todd. I. Benbasat, Evaluating the impact of dss, cognitive effort, and incentives on strategy selection, Inf. Syst. Res. 10 (4) (1999) 356–374.

[15] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aids, Mis Q. 16 (3) (1992) 373-393.

[16] D.T. Singh, M.J. Ginzberg, An empirical investigation of the impact of process monitoring on computer-mediated decision-making performance, Organ. Behav. Hum, Decis, Process, 67 (2) (1996) 156–169.

[17] D.T. Singh, Incorporating Cognitive Aids into Decision Support Systems: The Case of the Strategy Execution Process, Decis. Support Syst. 24 (2) (1998) 145–163.

[18] S. De Wit, I. Van De Vijver, K. Ridderinkhof, Impaired acquisition of goal-directed action in healthy aging, Cogn. Affect. Behav. Neurosci. 14 (2) (2014) 647–658.

[19] W. Wood, D. Rünger, Psychology of habit, Annu. Rev. Psychol. 67 (2016) 289–314.

[20] J. Reason, Actions not as planned: the price of automatization, in: G. Underwood, R. Stevens (Eds.), Aspects of Consciousness, Academic Press, London, 1979 pp. 67–89.

[21] A. Bandura, Social cognitive theory of self-regulation, Organ. Behav. Hum. Decis.

[22] A. Bandura, Toward a psychology of human agency: pathways and reflections,

[23] P. Karoly. Mechanisms of self-regulation: a systems view. Annu. Rey. Psychol. 44

[24] B.J. Zimmerman, Attaining self-regulation: a social cognitive perspective, in: M. Boekaerts, P.R. Printrich, M. Zeidner (Eds.), Handbook of Self-Regulation, Academic Press, New York, 2000

[25] A. Bandura, Self-Efficacy: The Excercise of Control, W.H. Freeman and Company, New York, 1997.

[26] J.S. Eccles, A. Wigfield, Motivational beliefs, values, and goals, Annu. Rev. Psychol. 53 (2002) 109–132.

[27] P.M. Fitts, M.I. Posner, Human Performance, Belmont: Brooks/Cole Publishing Company, California, 1969.

[28] R. Kanfer, P.L. Ackerman, Motivation and cognitive abilities: an integrative / aptitude –treatment interaction approach to skill acquisition, J. Appl. Psychol. 74 (4) (1989) 657–690.

[29] J.W. Payne, J.R. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press, New York, 1993.

[30] S.B. Needleman, C.D. Wunsch, A general method applicable to search for similarities in the amino acid sequence of two proteins, J. Mol. Biol. 48 (1970) 443–453.

[31] J.R. Bettman, E.J. Johnson, J.W. Payne, A componential analysis of cognitive effort in choice, Organ. Behav. Hum. Decis. Process. 45 (1990) 111–139.

[32] J.R. Bettman, M.F. Luce, J.W. Payne, Constructive consumer choice processes, J. Consum. Res. 25 (3) (1998) 187–217.

[33] F.-F. Cheng, C.-S. Wu, Debiasing the framing effect: the effect of warning and involvement, Decis. Support Syst, 49 (3) (2010) 328–334.

[34] P. Todd, I. Benbasat, The influence of decision aids on choice stategies: an experimental analysis of the role of cognitive effort, Organ. Behav. Hum. Decis. Process. 60 (1994) 36–74.

[35] E.J. Johnson, J.W. Payne, Effort and accuracy in choice, Manage. Sci. 31 (4) (1985) 395–414.

[36] I. Benbasat, P. Todd, The effects of decision support and task contingencies on model formulation: a cognitive perspective, Decis. Support Syst. 4 (4) (1996) 241–252.

[37] J.W. Payne, J.R. Bettman, E.J. Johnson, Adaptive strategy selection in decision making, J. Exp. Psychol. Learn. Mem. Cogn. 14 (3) (1988) 534–552.

[38] G.P. Latham, E.A. Locke, Self-regulation through goal setting, Organ. Behav. Hum. Decis. Process, 50 (1991) 212–247

[39] A. Bandura, Social Foundations of Thought and Action: A Social Cognitive Theory, Prentice Hall, Englewood Cliffs, NJ, 1986.

[40] G. Yeo, A. Neal, Subjective cognitive effort: a model of states, traits, and time, J. Appl. Psychol. 93 (3) (2008) 617–631.

[41] M.E. Gist, T.R. Mitchell, Self-efficacy: a theoretical analysis of its determinants and malleability, Acad. Manag. Rev. 17 (2) (1992) 183–211.

[42] R.E. Wood, A. Bandura, Impact of conceptions of ability on self-regulator mechanisms and complex decision making, J. Pers. Soc. Psychol. 56 (3) (1989) 407–415.

[43] G.M. Marakas, M.Y. Yi. R.D. Johnson, The multilevel and multifaceted character of computer self-efficacy: toward clarification of the construct and an integrative framework for research, Inf, Syst. Res. 9 (2) (1998) 126–163.

[44] R.F. Baumeister. T.F. Heatherton. Self-regulation failure: an overview. Psychol Ing. 7 (1) (1996) 1–15.

[45] L.-L. Tsai, H.-Y. Young, S. Hsieh, C.-S. Lee, Impairment of error monitoring following sleep deprivation, Sleep 28 (6) (2005) 707–713.

[46] A. Elfering, S. Grebner, F. de Tribolet-Hardy, The long arm of time pressure at work: cognitive failure and commuting near-accidents, Eur. J. Work. Organ. Psychol. 22 (6) (2013) 737–749.

[47] R.F. Pohl, E. Erdfelder, B.E. Hilbig, L. Liebke, D. Stahlberg, Effort reduction after self-control depletion: the role of cognitive resources in use of simple heuristics, J. Cogn, Psychol, 25 (3) (2013) 267–276.

[48] R. Wood, P. Atkins, C. Tabernero, Self-efficacy and strategy on complex tasks, Appl. Psychol. 49 (3) (2000) 430–446.

[49] D. Kahneman, Maps of bounded rationality: psychology for behavioral economics. Am Fcon Rev 93 (5) (2003) 1449–1475

[50] D. Kahneman, Attention and Effort, Prentice-Hall, Englewood Cliffs, N.J, 1973.

[51] M.A. Just, P.A. Carpenter, Eye fixations and cognitive processes, Cogn. Psychol. 8 (1976) 441–480.

[52] A. Glockner, A.K. Herbold, An eye-tracking study on information processing in risky decisions: evidence for compensatory strategies based on automatic processes, J. Behav. Decis. Mak. 24 (1) (2011) 71–98.

[53] E.J. Johnson, M. Schulte-Mecklenbeck, M.C. Willemsen, Process models deserve process data: comment on Brandstatter, Gigerenzer, and Hertwig (2006), Psychol. Rev, 115 (1) (2008) 263–273.

[54] J.L. Orquin, S. Mueller Loose, Attention and choice: a review on eye movements in

[55] J.E. Russo. B. Dosher. Strategies for multiatribute binary choice, J. Exp. Psychol Learn. Mem. Cogn. 9 (4) (1983) 676–696.

[56] S. Debowski, R.E. Wood, A. Bandura, Impact of Guided Exploration and Enactive Exploration on Self-Regulatory Mechanisms and Information Acquisition through Electronic Search, J. Appl. Psychol. 86 (6) (2001) 1129.

[57] R.B. Slatcher, J.W. Pennebaker, How do I love thee? Let me count the words: the social effects of expressive writing. Psychol. Sci. 17 (8) (2006) 660–664.

[58] F.-Y. Kuo, T.-H. Chu, M.-H. Hsu, H.-S. Hsieh, An investigation of effort–Accuracy trade-off and the impact of self-efficacy on web searching behaviors ". Decis. Support Syst, 37 (3) (2004) 331–342.

[59] B.B. Anderson, J.L. Jenkins, A. Vance, C.B. Kirwan, D. Eargle, Your memory i working against you: how eye tracking and memory explain habituation to security warnings, Decis. Support Syst. 92 (2016) 3–13.

[60] P. Bera, P. Soffer, J. Parsons, Using eye tracking to expose cognitive processes in understanding conceptual models, Mis Q. 43 (4) (2019) 1105–1126.

[61] M. Hegarty, R.E. Mayer, C.E. Green, Comprehension of arithmetic word problems: evidence from students’ eye fixations, J. Educ. Psychol. 84 (1) (1992) 76–84.

[62] M. Hegarty, R.E. Mayer, C.A. Monk, Comprehension of arithmetic word problems: a comparison of successful and unsuccessful problem solvers. J. Educ. Psychol. 87 (1) (1995) 18–32.

[63] P.-M. L´eger, S. S´enecal, F. Courtemanche, A. Ortiz de Guinea, R. Titah, M. Fredette, E. <sup>´</sup> Labonte-LeMoyne, Precision is in the eye of the beholder: application of eye fixation-related potentials to information systems research, J. Assoc. Inf. Syst. 15 (10) (2014) 651–678.

[64] B. Laeng, D.-S. Teodorescu, Eye scanpaths during visual imagery reenact those of perception of the same visual scence, Cogn. Sci. 26 (2002) 207–231.

[65] M. Pomplug, L. Sichelschmidt, K. Wagner, T. Clermont, G. Rickheit, H. Ritter, Comparative visual search: a difference that makes a difference, Cogn. Sci. 25 (2001) 3–36.

[66] K. Rayner, Eye movements in reading and information processing: 20 years of research, Psychol. Bull. 124 (3) (1998) 372–422

[67] Q. Wang, S. Yang, M. Liu, Z. Cao, Q. Ma, An eye-tracking study of website complexity from cognitive load perspective, Decis. Support Syst. 62 (2014) 1–10.

[68] J.E. Russo, L.D. Rosen, An eye fixation analysis of multialternative choice, Mem. Cognit. 3 (3) (1975) 267–276.

[69] G.L. Lohse, E.J. Johnson, A comparison of two process tracing methods for choice tasks, Organ. Behav. Hum. Decis. Process. 68 (1) (1996) 28–43.

[70] R.-F. Day, Examining the validity of the Needleman–Wunsch algorithm in identifying decision strategy with eye-movement data, Decis. Support Syst. 49 (4) (2010) 396–403.

[71] S.A. Brandt, L.W. Stark, Spontaneous eye movements during visual imagery reflect the content of the visual scene, J. Cogn, Neurosci, 9 (1) (1997) 27–38

[72] S.S. Hacisalihzade, L.W. Stark, J.S. Allen, Landis, Z. Gyr, Visual perception and sequences of eye movement fixations: astochastic modeling approach, IEEE Trans. Syst. Man Cybern. 22 (3) (1992) 474–481.

[73] S. Josephson, M.E. Holmes, Visual attention to repeated internet images: testing the scanpath theory on the world Wide web, in: Proceedings of the 2002 Symposium on Eye Tracking Research & Applications New Orleans, Louisiana ACM, 2002, pp. 43–49.

[74] B. Pan, H.A. Hembrooke, G.K. Gay, L.A. Granka, M.K. Feusner, J.K. Newman, The determinants of web page viewing behavior: an eye-tracking study, in: Proceedings of the 2004 Symposium on Eye Tracking Research & Applications, New York: ACM, 2004, pp. 147–154.

[75] D.D. Salvucci, J.R. Anderson, Automated eye-movement protocol analysis, Hum. Interact. 16 (2001).39–86

[76] J.M. West, A.R. Haake, E.P. Rozanski, K.S. Karn, Evepatterns: software for identifying patterns and similarities across fixation sequences, in: Proceedings of the 2006 Symposium on Eye Tracking Research & Applications, New York: ACM, 2006. pp. 149–154.

[77] V.I. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Dokl. Phys. 10 (1966) 707–710.

[78] J.R. Bettman, M.A. Zins, Information format and choice task effects in decisior making, J. Consum. Res. 6 (1979) 141–153.

[79] E.A. Locke, E. Frederick, P. Bobko, Effect of self-efficacy, goals, and task strategies on task performance, J. Appl. Psychol. 69 (2) (1984) 241–251.

[80] A. Bandura, Guide for constructing self-efficacy scales, Self-efficacy beliefs of adolescents 5 (1) (2006) 307–337.

[81] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decis. Support Syst. 14 (3) (1995) 219-235.

[82] R. Sharda, S.H. Barr, J.C. MCDonnell, Decision support system effectiveness: a review and an empirical test, Manage. Sci. 34 (2) (1988) 139–159.

[83] S. Djamasbi, Does positive affect influence the effective usage of a decision support system? Decis. Support Syst. 43 (4) (2007) 1707–1717.

[84] T. Bouffard-Bouchard, Influence of self-efficacy on performance in a cognitive task, J. Soc. Psychol. 130 (3) (1990) 353–363.

[85] J. Reason, Human error: models and management, Br. Med. J. 320 (2000) 768–770.

[86] W.W. Chin, The partial least square approach to structural equation modeling, in: G.A. Marcoulides (Ed.). Modern Methods for Business Research. Lawrence Erlbaum Associates, Mahway, NJ, 1998, pp. 295–336.

[87] D. Gefen, D.W. Straub, M.-C. Boudreau, Structural equation modeling and regression: guidelines for research practice, Commun. Assoc. Inf. Syst. 4 (7) (2000) 1–76.

[88] M.G. Glaholt, E.M. Reingold, The time course of gaze Bias in visual decision tasks, Vis. cogn. 17 (8) (2009) 1228–1243.

[89] C.M. Ringle, S. Wende, A. Will, Smartpls 2.0., University of Hamburg, Hamburg, Germany, 2005.

[90] W.W. Cotterman, J.A. Senn. Challenges and Strategies for Research in Systems Development. John Wiley & Sons. Inc. 1992.

[91] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, J. Mark. Res. 18 (1) (1981) 39–50.

[92] J. Guszcza, S. Pentland, Artificial Intelligence and Human-Computer Collaboration, from, 2019, https://www2.deloitte.com/us/en/pages/deloitte-analytics/article s/artificial-intelligence-human-computer-collaboration.html

[93] J. Cummings, A.R. Dennis, Virtual first impressions matter: the effect of enterprise social networking sites on impression formation in virtual teams, Mis Q. 42 (3) (2018) 697–718.

Rong-Fuh Day is a professor of Information Management at National Chi-Nan University, Taiwan. He received a PhD in Information Management from National Sun Yat-Sen Uni versity, Taiwan. His research interests include behavioral decision-making, eye-tracking approach, web advertisement, and human–computer interaction. He has published article in Decision Support Systems, Computers in Human Behavior, and Psychology & Marketing.

Fang-Yan Kuo is a professor of Information Management in Sun Yat-Sen University, Taiwan. He holds a PhD degree in Information Systems from the University of Arizona. He was a faculty member at Information Systems at University of Colorado at Denver from 1985 to 1997. Professor Kuo’s research interests include cognition and learning in orga nizations, information ethics, and human–computer interactions. He has published articles in Communications of ACM, MIS Quarterly, European Journal of Information Systems, Decision Support Systems, Journal of Business Ethics, Information and Management, Electronic Com merce Research and Applications, ACM Transactions on Management Information Systems, Journal of the American Society for Information Science and Technology, Journal of Computer mediated communication, and Journal of Systems and Software.

Yu-Feng Huang received his PhD in Information Management from National Sun Yat-sen University, Taiwan, and was a research fellow in Duke-NUS Graduate Medical School in Singapore. His research uses EEG, eye-tracking, and fMRI to study the roles of perception, attention, and emotion in decision-making. He has published articles in NeuroImage, Consciousness and Cognition, Vision Research, Internet Research, Computers in Human Behavior, and Electronic Commerce Research and Applications.
