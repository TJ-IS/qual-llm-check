---
otero_id: 8994
otero_key: "9TMQ97DX"
title: "Emergency management information systems: Could decision makers be supported in choosing display formats?"
authors: "Milton Shen; Melody Carswell; Radhika Santhanam; Kyle Bailey"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.08.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Emergency management information systems: Could decision makers be supported in choosing display formats? ☆

Milton Shen <sup>a,</sup>⁎, Melody Carswell <sup>b,1</sup>, Radhika Santhanam <sup>c,2</sup>, Kyle Bailey <sup>b,3</sup>

<sup>a</sup> Department of Finance, Accounting, and Economics, University of Alabama in Huntsville, Huntsville, AL 35899, United States

<sup>b</sup> Department of Psychology, University of Kentucky, Lexington, KY 40506, United States

<sup>c</sup> Decision Sciences and Information Systems, University of Kentucky, Lexington, KY, 40506, United States

## a r t i c l e i n f o

Article history: Received 6 August 2009 Received in revised form 10 August 2011 Accepted 25 August 2011 Available online 8 September 2011

Keywords: Cognitive <sup>fi</sup>t theory Decisional guidance Emergency management information system Proximity compatibility principle Theory of data graphics 2D and 3D display formats

## a b s t r a c t

Recent information technologies make it possible to include sophisticated three-dimensional display formats in emergency management information systems (EMIS), decision-support systems that facilitate decision making in crisis situations. However, if decision makers are to improve their decisional performance, they must correctly identify appropriate situations for using these formats. We conduct two experiments and <sup>fi</sup>nd that, as prior research has suggested, decision makers do not choose the most appropriate display format, but their performance improves when given prospective decisional guidance. We discuss implications of these <sup>fi</sup>ndings for EMIS design, for the training of emergency management professionals, and for future research on display formats and decisional guidance.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

To provide adequate decisional support to manage crisis situations, researchers and practitioners in information system and disaster management have urged attention to the development or enhancement of emergency management information systems (EMIS) [5,19,48]. As a decision-support system (DSS), an EMIS helps members of an emergency management team<sup>4</sup> — who are usually performing under conditions of high information load and high time stress — gather and synthesize incomplete but often-critical data [5,40]. Prior studies have recommended not only training strategies that may improve EMIS users' decisional performance, but have also suggested guidelines for EMIS design and implementation, such as communications, data integration, and tools for interface and visualization [11,12,23,33,40].

Most existing EMIS were designed to render geospatial data as two-dimensional (2D) displays [19] that show orientations and relative positions by laying objects in a plane and by using colors or contour lines to represent elevations (e.g., Google Maps; Fig. 1, Panels 1 and 2). As the availability, performance, and cost-effectiveness of information technology constantly increase, attention has increasingly shifted to three-dimensional (3D) visualization, especially after September 11, 2001 [9]. With an extra dimension, 3D displays integrate the presentations of orientations, relative positions, elevations, and shapes of objects in a single view (e.g., Google Earth; Fig. 1, Panel 5). The literature has suggested that such differences in display format and content richness mandate different levels of user skill or experience, cause different levels of mental workload, and thus lead to differences in decision-making performance [35,44]. Although EMIS with either 2D or 3D displays could be utilized in crisis situations, trivial differences in decision performance might cause delays, damage, or casualties. For example, if a 911 call center receives a report of a <sup>fi</sup>re in a downtown skyscraper, incident commanders using an EMIS with 3D views can make decisions promptly, whereas those using an EMIS with 2D displays may require additional assistance to <sup>fi</sup>nd the exact location.

Nevertheless, the technological sophistication and content richness that characterize 3D displays do not guarantee better decision making for all tasks; on the contrary, prior studies in human factors and ergonomics suggest that 2D displays are more useful than 3D when the tasks require judgments on orientation or relative positions, but not on elevations, sizes, or shapes [4,35,36]. In the domain of MIS research, cognitive <sup>fi</sup>t theory (CFT) proposes that the correspondence between task requirements and the information presentation format determines problem-solving performance [41,42], suggesting that the dimensionality itself is not the sole determinant of decision performance. Both streams of research suggest a hybrid EMIS that allows users to switch between visual displays <sup>fl</sup>exibly. Two immediate questions arise: Can EMIS users accurately select display formats with the appropriate dimensionality (i.e., 2D vs. 3D) when given a choice? If not, can they be trained or supported by decisional guidance (DG) to choose appropriate display formats?

![](/api/attachments/9TMQ97DX/fulltext/images/7a8b6efba0cd1e4c1755532168deb5b914edd6c6cf0d93f7fb5591298dd40742.jpg)  
Fig. 1. Display formats

We conducted two related experiments to address these questions. First, using previously validated experimental instruments [4], we examined whether novice EMIS users can choose appropriate display formats without guidance. Speci<sup>fi</sup>cally, research participants were required to select among several 2D and 3D displays to deal with several tasks that each required different information. Based on the results of this experiment, we found that although participants matched display formats to tasks at a rate reliably better than what would be expected by chance, there was still considerable room for improvement in their display selection performance. Thus, in Experiment 2 we explored whether participants made better display format selections after they were exposed to DG about the functionality of the different formats. The combined results from our experiments suggested that novice EMIS users may not automatically choose the best display format for a task, but DG could signi<sup>fi</sup>cantly improve their performance.

Indeed, both DG and training are designed to equip DSS users/ trainees with the knowledge and capability to make better decisions. From various formats of DG [29] we chose to examine the impacts of a prospective DG, where decisional supports are provided prior to decision making. Such decisional guidance, as implemented in our study, might also be seen as a form of training. Although examining only a single type of DG, we believe our research serves as a motivator for future research on other formats of DG and yields implications for EMIS design, for the training of emergency management professionals, and for more basic research on information design.

The rest of this paper is structured as follows. In Section 2, we provide an overview of theoretical foundations and principles that guided our research hypotheses. Section 3 proposes the framework of the research and experiments. We present the experimental methods and results of our two experiments in Sections 4 and 5, respectively. Section 6 concludes the paper with a discussion of our <sup>fi</sup>ndings and implications for practice and for future research.

## 2. Research framework

## 2.1. EMIS design and spontaneous display selections

Disasters such as <sup>fi</sup>res, <sup>fl</sup>oods, earthquakes, airplane crashes, or terrorist attacks may cause crisis situations [33]. Irrespective of the origin, crisis situations are often accompanied by uncertainty, rapidly evolving information, and possibility of serious losses of human lives and property if not managed properly [19,33,39,48]. Hence, the ability to make ef<sup>fi</sup>cient and effective decisions in crisis situations is extraordinarily important, dif<sup>fi</sup>cult, and complex [23,33]. EMIS were developed to help incident commanders quickly collect, organize, and comprehend incoming information, and then make effective and prompt decisions under pressure and time constraints [12,19, 33,39,48]. Researchers have suggested design proposals for EMIS development, emphasizing that designers must pay serious attention to the display of information (i.e., the display formats) and that the latest innovations such as 3D displays should receive consideration [4,23].

One approach to rendering geospatial information in an EMIS is for system designers to analyze anticipated tasks and user characteristics and then determine which display format will have the broadest functionality. EMIS with such fixed displays are inexpensive to develop and easy to use because users need not switch between different display formats. However, the unpredictable characteristics that mark crisis situations suggest that it is quite hard, if not impossible, to anticipate the nature of decision tasks, user characteristics, and the overall context in which the EMIS display format will be used. Thus, a prede<sup>fi</sup>ned display format (e.g., pure 2D or 3D) could prove to be an incompatible or an inappropriate design strategy.

Another, seemingly better, approach to rendering geospatial information is to design an EMIS with adaptable displays that grant users discretion to directly manipulate and choose their display format. Such <sup>fl</sup>exibility in user interfaces is assumed to improve their applicability to a range of situations and, as a result, to improve decisional performance. This is certainly an approach that might be recommended for EMIS [8]. The challenge with this approach, however, is the potential dif<sup>fi</sup>culty that novice users might face in determining which display formats are likely to best meet their task requirements at any given moment. For example, users may be so partial to speci<sup>fi</sup>c display formats that they fail to use more appropriate displays, thus undermining the potential advantages of offering them more choices. Therefore, it is important to examine whether users of an EMIS with adaptable displays can or will choose the best display format for various tasks.

The cognitive <sup>fi</sup>t theory (CFT) asserts that it is important to match the display format to the task to improve decision-making performance [42]. As shown in Fig. 2, CFT proposes that when the problemrepresentation and problem-solving tasks match, decision makers can formulate mental representations for task solutions more effectively and ef<sup>fi</sup>ciently, leading to better problem-solving performance (e.g., speed, accuracy, precision) [42]. Inappropriate displays decrease task performance by increasing the decision makers' workload and associated cognitive costs [42,47].

CFT was originally developed to address prior inconsistent results on the effectiveness of graphs and tables [42], but was then applied to other domains and yielded implications for DSS design. A recent review of more than one hundred studies on the application of cognitive <sup>fi</sup>t indicated that CFT is a robust theory that generalizes to any situation where tasks and problem representations are involved [42]. Therefore, CFT serves as an appropriate foundation for the present research — it highlights the general importance of making the choice of display formats contingent on the tasks they are to support, and it also provides guidance for determining how speci<sup>fi</sup>c tasks and formats (e.g., 2D vs. 3D) should be paired.

In addition to CFT in the MIS literature, researchers in human factors, cognitive psychology, and graphic design explore task-display pairings and their relationships to decision performance. For decades, Edward Tufte has cautioned that more advanced visual displays with more features may not necessarily improve decision-making accuracy [38]. Speci<sup>fi</sup>cally, in his theory of data graphics (TDG), Tufte proposed several principles for using graphs to present quantitative information more ef<sup>fi</sup>ciently and effectively [38]. One principle suggested that “the number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data” (p. 71). Hence, 3D representations are not recommended when the decision making requires two dimensions only. Through their proximity compatibility principle (PCP), which is based on a long tradition of psychological research on human attention and perceptual organization, Wickens and Carswell [44] predicted that a given display will be compatible with a given task when its “display proximity” is consistent with the level of mental integration demanded by the task. In other words, when the task requires decision makers to combine information from multiple sources, a visually integrated display (e.g., a 3D display) provides better decisional assistance than several separate 2D ones. Nevertheless, when the display formats are highly integrated but the decision makers need only a subset of the data contained in the displays, the irrelevant information might adversely interfere with users' decision-making processes. Therefore, 3D displays might not be the optimal representation when the task requires consideration of only the relative horizontal position of target objects. In this example, a 2D map might be better than a 3D map for providing decisional support.

Supporting CFT, TDG, and PCP, empirical studies provide evidence that certain tasks are better supported with 3D display formats while others are not. For example, St. John et al. [35] indicated that 3D displays are better for shape-understanding tasks, whereas 2D displays contribute more to the recognition of relative positions. Tory [36] reviewed prior literature and also concluded that 2D and 3D displays differ in their value depending on the scenario. Bailey et al. [4] found that 3D displays were useful only for tasks in which all three spatial dimensions must be used (e.g., similar to the “overall shape” judgments of St. John et al. [35]) to make an emergency response decision. These 3D displays actually degraded performance in tasks where only relative 2D position judgments were required. (See more details about Bailey et al. [4] in Appendix 3.)

Although CFT, TDG, and PCP investigate the associations between task-display pairings and decision performance from different perspectives, they consistently acknowledge that (a) no display format is perfect for all tasks, which supports the development of EMIS with adaptable displays; and (b) decisional performance is in<sup>fl</sup>uenced by the cognitive <sup>fi</sup>t or the match between display formats and problem-solving tasks. Nevertheless, using an adaptable display for EMIS presupposes that novice users are able to intuitively make task-display compatibility decisions of the sort described earlier. Empirical studies, however, show that users make such judgments poorly. For example, users who exhibit familiarity bias or display selection inertia may <sup>fi</sup>xate on a speci<sup>fi</sup>c type of interface or display format that they have learned or frequently used (i.e., usually 2D displays) [3,27], even when a novel format is more task-compatible [4]. Another bias in the selection of displays is “naïve realism,” or a tendency for users and some designers to prefer more photorealistic renderings of information based on their intuition that more realistic-looking displays must be more accurate (e.g., 3D rather than 2D displays of geospatial information) [31]. Smallman and St. John [31] argue that naïve realism on the part of designers has inadvertently led to the development of realistic-looking displays that provide users with <sup>fl</sup>awed, imprecise, or cluttered representations that cause poor performance. These authors also provide evidence that users sometimes prefer these displays, even though they may be associated with performance decrements.

![](/api/attachments/9TMQ97DX/fulltext/images/8f5491d5988a8f98ab8e141846abab0a502a471be89bf45e006665de46b3000d.jpg)  
Fig. 2. Cognitive <sup>fi</sup>t in problem solving (adapted from Vessey [42])

Before proposing an adaptable display approach for EMIS design, it is therefore important to examine whether novice EMIS users, without guidance, behave in a manner consistent with cognitive <sup>fi</sup>t and choose appropriate display formats for their decision making. Hence, we <sup>fi</sup>rst tested the following hypothesis (stated in the null form):

${ \bf H 1 _ { 0 } . }$ Without guidance, novice EMIS users will fail to choose task-appropriate display formats at a rate greater than what would be expected by chance.

Rejection of the null hypothesis would support the potential ability of users to effectively make use of adaptable displays; however, rejection of the null hypothesis is not equivalent to saying that their performance is “good” or even “acceptable” for real-world emergency management scenarios. Thus, we also use data collected in this study to document actual levels of correct display selection to serve as benchmarks to help establish the size of any potential performance improvements that might be obtained through the use of decisional guidance.

## 2.2. Prospective decisional guidance

If novice EMIS users frequently make incorrect task-display compatibility decisions, can their display choices be improved through relatively brief, low-cost interventions, for example through the use of decisional guidance? Silver [28] de<sup>fi</sup>ned decisional guidance (DG) as “how a DSS enlightens or sways its users as they structure and execute their decision-making process.” The purpose of providing decisional guidance is not to tell users about the mechanics of operating a DSS, but to guide them so that they make choices that can enhance their ef<sup>fi</sup>ciency and effectiveness [28].

DG can intervene in the decision-making process in many ways [22]. Prior studies examined the impacts of DG on the performance of decision makers and found overwhelming support that DG expedites decision making [21,25,30,47] and improves accuracy [21,24,25,30,47]. In some studies, decisional performance was not measured in terms of time or accuracy of the decision; instead, researchers examined whether DG changed or in<sup>fl</sup>uenced users' decision strategy [6,15–17,20]. Furthermore, decision makers indicated improved satisfaction with the decision process [25] or increased trust in the DSS [43] when provided such guidance. Studies have also indicated that DG seems to help users learn several fundamental principles and procedures of a given application domain [1,2,25,43]. For example, Antony, Batra, and Santhanam [2] found that DG helped novice system designers learn fundamental principles and procedures on data modeling. Overall, evidence strongly indicates that DG could improve decisional performance and be applied as a training tool in the province of display selection during decision making.

Extending these results to the domain of crisis management and the adaptable display approach to EMIS development, we envisioned that DG can train and guide novice EMIS users to choose appropriate display formats and improve their decisional performance. In other words, we predicted that users with DG will choose display formats with better cognitive <sup>fi</sup>t than if they are not given such decisional support. Hence, we hypothesized the following (in the alternative form):

$\mathbf { H 2 _ { A } } .$ Decision makers given prospective decisional guidance about display format selection will have better decisional performance than those who do not get such guidance.

Following prior literature, this research measured novice EMIS users' decisional performance by accuracy and decision-making time. In addition, the study investigated DG's impacts on decision makers' mental workload, a dimension that the DG literature has not yet explored.

## 3. Research method

A laboratory-based experimental approach was chosen to test the two hypotheses because it allowed the controlled implementation of different tasks and displays, as well as a one DG intervention, and it facilitated subsequent observation of participants' responses [18]. Following Silver's three-step approach [28], this research examined the in<sup>fl</sup>uence of DG by two separate but related experiments. Specifically, in Experiment 1 we <sup>fi</sup>rst explored the extent to which novice EMIS users, without guidance, spontaneously choose display formats that have the best cognitive <sup>fi</sup>t for their tasks. We also replicated and validated these results with actual <sup>fi</sup>rst responders (i.e., employees from local <sup>fi</sup>re and police departments). We then developed an experimental script that used a paper prototype of DG that an EMIS could use (Appendix 1) to provide guidance on which display format to use. In Experiment 2, we examined how the DG affected novice EMIS users on their decisional accuracy, time, and mental workload. In the next two sections, we describe the experimental design, procedures, and results of the two experiments.

## 4. Experiment 1 — Spontaneous display selections

## 4.1. Experimental tasks and instrument

This experiment utilized tasks and displays that were theoretically justi<sup>fi</sup>ed by CFT, PCP, and TDG, and empirically validated by Bailey et al. [4]. Speci<sup>fi</sup>cally, those authors developed three tasks that were best performed by using their “<sup>fi</sup>t” displays. They concluded that (a) planview displays (e.g., Fig. 1, Panel 1) best supported tasks that required only the horizontal information of the target object (i.e., relative positions); (b) elevation-view displays (e.g., Fig. 1, Panel 3) best supported tasks that required only the vertical information of the target objects (i.e., heights); and (c) 3D-view displays (e.g., Fig. 1, Panel 5) best supported tasks that required both the horizontal and vertical information of the target objects.

## 4.2. Research participants

For this experiment, we recruited 48 students from an introductory psychology class at a southern state university. The students received class credit in partial ful<sup>fi</sup>llment of a research-exposure requirement. In addition, 13 members of local <sup>fi</sup>re and police departments were recruited and paid to participate. The latter group included four women and nine men, aged 22 to 68-years-old, with mean job experience of 16 years in an emergency response job (mostly as dispatchers or patrol of<sup>fi</sup>cers).

## 4.3. Experimental procedures

First, participants were trained to perform three types of tasks with each of <sup>fi</sup>ve display formats (two with plan view, two with elevation view, and one with 3D view; Fig. 1). The purpose of training was to ensure participants could comprehend and use the display formats, not to teach them when to use them. To ensure the validity of training, only participants who completed a block of trials with an overall accuracy rate of at least 80% were allowed to proceed to the experiment stage. A high threshold was chosen to ensure that participants could use each of the display formats.

During post-training trials, participants were told which task they were about to perform and were allowed to pick the display they wanted to use. The critical dependent variable in this experiment was the participant's choice of display format from amongst plan views, elevation views, and 3D views. After the participant completed a series of <sup>fi</sup>ve decision trials using the selected format, the procedure was repeated with the remaining tasks. All three tasks were tested on every participant, with order counterbalanced across them.

## 4.4. Results

This research de<sup>fi</sup>ned a display format selection as accurate when the selected format provided the most cognitive <sup>fi</sup>t for decisionmaking purposes, according to CFT, PCP, TDG, and Bailey et al. [4]. Table 1 shows accuracy rates for display selections for all participants, and for <sup>fi</sup>rst responders and students separately. When the task required only horizontal information about the target object, 84% of all participants correctly indicated that the plan view was the best visual representation for the task. However, only 34% and 49% of participants accurately chose graphical displays for tasks that were best supported by elevation views or 3D displays, respectively.

The purpose of H1 was to examine whether novice EMIS users show any evidence of shifting their display selections to <sup>fi</sup>t their anticipated tasks, speci<sup>fi</sup>cally making selections that are consistent with the normative choices (i.e., of CFT, PCP, and TDG). To determine whether there was any statistically reliable tendency for participants to make appropriate choices, we compared their actual percentage of correct choices to the percentage that would be expected to occur by chance. Although exceeding chance performance is a lenient criterion, it provides an objective baseline that allows us to correct for there being more instances of some formats to choose from than others. Of the <sup>fi</sup>ve experimental displays, two were plan views (i.e., Fig. 1, Panels 1 and 2), which are the most congruent with performance of a task requiring only horizontal information. Therefore, random selections of display formats would deliver an average accuracy rate for task-display matches of 40%. One sample t-test against .40 suggested that research participants successfully outperformed chance. The same test was performed for each of the two remaining tasks — one that required only vertical information and one that required a combination of vertical and horizontal information. Although research participants still effectively surpassed random responding for tasks that required 3D displays (t-test against .2), they were not signi<sup>fi</sup>cantly better than chance when the tasks required vertical information only (t-test against .4). The overall accuracy of our participants across all tasks was 56%. Thus, although we found evidence that participants tended to select the appropriate display for two of the three tasks (thus, rejecting the null hypothesis), there was no such evidence of appropriate use for the third task and participants' overall accuracy rates was relatively low.

Accuracy rate, STDEV, and t-test results.

<table><tr><td></td><td>All participants $^{\wedge}$  (n = 61)</td><td>First responders $^{\wedge}$  (n = 13)</td><td>Students $^{\wedge}$  (n = 48)</td><td>Two-sample t-test significance</td></tr><tr><td>Tasks required horizontal information only  $\leftrightarrow$  Plan view $^{\wedge\wedge}$ </td><td>84% (.23) .000***</td><td>90% (.11) .000***</td><td>82% (.25) .000***</td><td>.27</td></tr><tr><td>Tasks required vertical information only  $\leftrightarrow$  Elevation view $^{\wedge\wedge}$ </td><td>34% (.33) .182</td><td>40% (.29) .976</td><td>33% (.34) .144</td><td>.47</td></tr><tr><td>Tasks required both horizontal and vertical information  $\leftrightarrow$  3D view $^{\wedge\wedge\wedge}$ </td><td>49% (.39) .000***</td><td>40% (.37) .075*</td><td>52% (.40) .000***</td><td>.34</td></tr><tr><td>Overall</td><td>56% (.17) .000***</td><td>57% (.14) .000***</td><td>55% (.17) .000***</td><td>.82</td></tr></table>

^: Numbers in cells indicate the mean, STDEV, and the p-value of one-sample t-test results. ^^: t-test against .40; ^^^: t-test against .20.

Frequency of choosing display format.

<table><tr><td rowspan="2"></td><td>All participants^</td><td>First responders^</td><td>Students^</td><td rowspan="2">Two-sample t-test Significance.</td></tr><tr><td>(n=61)</td><td>(n=13)</td><td>(n=48)</td></tr><tr><td rowspan="2">Plan view</td><td>52.78%</td><td>54.59%</td><td>52.29%</td><td>.737</td></tr><tr><td>.22</td><td>.20</td><td>.22</td><td></td></tr><tr><td rowspan="2">Elevation view</td><td>16.56%</td><td>17.95%</td><td>16.18%</td><td>.748</td></tr><tr><td>.17</td><td>.17</td><td>.18</td><td></td></tr><tr><td rowspan="2">3D view</td><td>30.66%</td><td>27.46%</td><td>31.53%</td><td>.565</td></tr><tr><td>.22</td><td>.18</td><td>.23</td><td></td></tr></table>

^: Numbers in cells indicate the mean and STDEV, respectively.

Two-sample t-tests failed to demonstrate differences in performance as a function of either gender or expertise. The failure to <sup>fi</sup>nd differences between actual <sup>fi</sup>rst responders and those with no experience may suggest that the appropriate choice of displays is a skill that does not naturally emerge from experience in the task domain. Although it was the case that <sup>fi</sup>rst responders' performance on tasks that required horizontal information (90%) and vertical information (40%) was better on average than that of college students (82%, 33%), <sup>fi</sup>rst responders' accuracy rate on tasks that required 3D view (40%) was inferior to the other group (52%).

Table 2 shows how frequently participants selected each type of display format, regardless of the task. The most popular display format was the plan view (52.78%), followed by the 3D view (30.66%), and elevation view (16.56%). Although such preferences may contribute to high accuracy when the task requires horizontal information, they also suggest that some participants may <sup>fi</sup>xate on map-like displays even when they need vertical information. Further analysis indicated that three <sup>fi</sup>rst responders (23.1%) and six students (12.5%) chose plan-view displays for N75% of their tasks, demonstrating the potential existence of display selection inertia. Consistent with Smallman and St. John [31], we found two (4.2%) students who chose 3D-view displays for N83% of their tasks, suggesting that naïve realism may play a role in their display format choices.

Overall, the results of Experiment 1 indicated that novice EMIS users without prior training might be under the in<sup>fl</sup>uence of idiosyncratic graphical preferences, display selection inertia, or naïve realism. In addition, although H1 was not fully accepted or rejected, the results nonetheless opened the door to further exploration of the possible bene<sup>fi</sup>ts of DG. Thus, we developed an experimental script that made use of prospective DG to determine whether this relatively simple intervention could help improve novice users' accuracy at selecting display formats based on each format's functional capabilities (Appendix 1; see

Section 5.3 for more details). In Experiment 2 we tested whether this prospective DG actually improved the time, accuracy, and mental workload associated with the choice of displays by novice EMIS users.

## 5. Experiment 2 — Prospective decisional guidance

## 5.1. Treatment — Prospective decisional guidance

We established two groups — an experimental group of participants who received an experimental script that used a paper DG prototype that indicated general principles of display choice (see Appendix 1) and a control group of participants who received a paper script providing general mission statements about the job of an incident commander but no information about display selection (see Appendix 2).

Based on CFT, PCP, TDG, and prior empirical <sup>fi</sup>ndings, we developed experimental DG materials that described the importance of cognitive <sup>fi</sup>t on the selection of display formats and included several speci<sup>fi</sup>c examples. In particular, the experimental materials (Appendix 1) described the concept of cognitive <sup>fi</sup>t and emphasized that displays with more dimensions are not always better. The DG materials further stated that 3D displays are better for decision tasks that require information about overall shape and size of an object or about two objects' relative heights. With respect to 2D displays, the DG script advised that they are better when precise values are required, where distance and direction between two objects are important, or where two objects' relative positions in geographic space (i.e., not height) are necessary. The DG script concluded by emphasizing that one should look at the decision task's characteristics when choosing a display format for a decision task. In the last few paragraphs of the script, several examples of task-display pairings were provided to illustrate and reiterate the concept of cognitive <sup>fi</sup>t.

Based on Silver's taxonomy [29], such informative guidance could be classi<sup>fi</sup>ed as prede<sup>fi</sup>ned, automatic, and prospective. Speci<sup>fi</sup>cally, it was developed based on prior studies (i.e., prede<sup>fi</sup>ned), its presentation required no speci<sup>fi</sup>c actions on the part of users (i.e., automatic), and it was presented before users' decisions were made (i.e., prospective). Instead of developing or modifying an actual EMIS, this research examined the effectiveness of DG by adopting the paper prototyping approach [34]. In other words, we provided both the experimental and control scripts in written format, rather than offering an actual computer-based EMIS with embedded DG. We believed that this approach would provide us a less-expensive test of the feasibility of DG and give us information that would help us more carefully develop an EMIS.

It was important to devise a control condition that required the same amount of time for participants to read but that did not provide explicit guidance. The resulting control script was equal in length to the experimental script, and even though the control script was titled “Display Formats,” it did not deal with cognitive <sup>fi</sup>t, the speci<sup>fi</sup>cs of display choices, or DG (Appendix 2). Instead, it introduced the responsibilities of an incident commander (IC) with only two sentences concerning display formats. In the <sup>fi</sup>rst paragraph the control script explained, “The IC uses a variety of display formats in two dimensions (2D) and three dimensions (3D) to help make decisions about the situation.” In the last paragraph the control script advised, “Hence, the IC must be careful in choosing the right display format (2D or 3D display) to help in the decision tasks relating to the management of the crisis situation.”

## 5.2. Participants

Sixty-one participants were recruited from an introductory psychology class at a southern state university. They were randomly assigned to the experimental or control group. Participants received credit in partial ful<sup>fi</sup>llment of a research-exposure requirement. As discussed later, we conducted manipulation checks to ensure the successful delivery of treatment conditions. Statistical analyses were conducted only on participants who had correctly answered all manipulation check questions.

![](/api/attachments/9TMQ97DX/fulltext/images/21e8dc0fd12d5341e6f350010fc97f812af8c2fb9c8e55bc3d330ceecd713506.jpg)  
Fig. 3. Research procedures in Experiment 2.

Differences in participants' backgrounds.

<table><tr><td></td><td>Experimental group (with DG)</td><td>Control group (without DG)</td><td>Significance (2-tailed)</td></tr><tr><td>Total number of recruits</td><td>32 (10 Male)</td><td>29 (5 Male)</td><td></td></tr><tr><td>Fail to pass the manipulation checks</td><td>8 (25.0%)</td><td>5 (17.2%)</td><td>.465</td></tr><tr><td>Number of participants</td><td>24</td><td>24</td><td></td></tr><tr><td>Gender – Male (%)</td><td>8 (33.3%)</td><td>3 (12.5%)</td><td>.090*</td></tr><tr><td>Average age</td><td>19.17</td><td>19.04</td><td>.754</td></tr><tr><td>Class standing</td><td></td><td></td><td></td></tr><tr><td>Freshman</td><td>14</td><td>11</td><td>.476^</td></tr><tr><td>Sophomore</td><td>6</td><td>11</td><td></td></tr><tr><td>Junior</td><td>2</td><td>1</td><td></td></tr><tr><td>Senior</td><td>2</td><td>1</td><td></td></tr><tr><td>Graph preference</td><td>6.92</td><td>6.88</td><td>.899</td></tr><tr><td>3D mental rotation ability</td><td>4.58</td><td>4.58</td><td>1.000</td></tr></table>

Denotes the results of chi-square test; \* denotes marginally signi<sup>fi</sup>cant results.

## 5.3. Experimental design and procedures

The experiment used a one-factor (DG — present vs. absent) random-group design. Therefore, the independent variable in the ANCOVA model was the experimental treatment. In addition to using random assignment to control for participants' individual differences, this research collected each participant's gender, age, graph preference (Appendix 4), and 3D mental rotation ability (Appendix 5) so that we could statistically control for these factors. We collected information on three dependent variables — accuracy, time, and mental workload. Participants' self-reported mental workload was measured by using the NASA-TLX scale (Appendix 6), which researchers have frequently used to evaluate workload in various human–machine systems [14].

Fig. 3 shows the research procedure for Experiment 2. Participants volunteered for the research and were randomly assigned to either the experimental or control group. Students were run in groups of 11 to 18 in a conference room, with all members of a single group assigned to the same experimental condition. To simulate the working environment, researchers introduced the role of incident commanders, the importance of their decisional accuracy and speed, and the task of participants — assuming the role of an incident commander and indicating which display format would more appropriately answer the experimental questions (Appendix 7).

As shown in Fig. 3, at the beginning of the experiment, questionnaires were administered to document participants' demographic data, graphical preference, and 3D mental rotation ability. To ensure the successful installment of treatment, we conducted manipulation checks following the treatment or control scripts. Speci<sup>fi</sup>cally, after participants received the DG or control script, they were asked to answer true/false questions such as “A good match between the decision task and the information display leads to better decisions,” or “3D graphs are always better than 2D graphs in supporting decision making.” Participants were not allowed to discuss, take notes, or review the DG or control scripts. Only participants who correctly answered all ten manipulation-check questions were included in the statistical analyses. Next, we projected the horizontal plan view (Fig. 1, Panel 1) and 3D view (Fig. 1, Panel 5) onto a screen mounted at the front of the conference room. Participants then performed the experimental task that involved indicating which display format (i.e., 2D or 3D) was more appropriate for improving the speed and accuracy of decision making for 13 speci<sup>fi</sup>c questions. Participants' selfreported workloads during the experiment were collected through NASA-TLX post-experiment questionnaires. Participants indicated the starting and ending time of the experiment by using a large digital stopwatch located at the front of the conference room.

## 5.4. Tasks

Based on the prior literature [32,35,36], four types of questions — distance, orientation, height, and shape (Appendix 7) — were used to examine whether DG can improve novice EMIS users' speed and accuracy in selecting display formats. Speci<sup>fi</sup>cally, tasks dealing with the distance between two objects (Q1–3) do not require the third axis (i.e., heights); thus, prior literature suggests that 2D display format is more suitable than 3D. Similarly, the orientation of an object or the relative positions of objects are also examples of 2D tasks (Q4). In addition, the overlapping objects in 3D displays and their possible “line-of-sight” problem might hinder users from making orientationrelated decisions [7]. On the other hand, 3D displays provide vertical information (i.e., elevation of an object) and thus are better for tasks dealing with height (Q5–11) or overall shape (Q12–13).

The experimental tasks in Experiments 1 and 2 are different because we had different research goals for the two experiments. Speci<sup>fi</sup>cally, Experiment 1 was an initial attempt to determine the magnitude of the problems that participants would encounter in matching displays to tasks; thus, we used three tasks and displays, following Bailey et al. [4]. Having established that participants overused the plan view displays, we focused on the more familiar of the formats — the plan view (2D) and the 3D view. This allowed us to more thoroughly test the potential impacts of DG in a limited amount of time (i.e., without extensive training on a relatively unfamiliar format) while still collecting data from a representative sample of tasks (i.e., decision types).

## 5.5. Results

Table 3 summarizes participants' demographic information, graph preference, and 3D mental rotation ability. A total of 61 participants took part in the experiment. Because of unexpected participant absenteeism, group sizes were unbalanced across conditions. As indicated previously, we used two sets of different manipulation check questions — one for the experimental group, the other for the control group — to determine whether the treatment was effectively installed. Note that these checks were essentially measures of reading comprehension, and do not ensure that the information will actually be used by participants to perform their decision tasks. It is the actual use of the guidance that is of critical concern in the present study. Two men from both groups, six women from the experimental group, and three women from the control group failed to answer all ten manipulation check questions correctly and thus were excluded from the following statistical analyses. A marginally signi<sup>fi</sup>cant difference in gender composition (p=.09) existed between the experimental and control group, but we observed no other signi<sup>fi</sup>cant differences. Therefore, gender was used as a control variable in the following analyses to mitigate the potential in<sup>fl</sup>uences of genderrelated biases.

ANCOVA results of decision accuracy rate.

<table><tr><td rowspan="2" colspan="2">Tasks</td><td rowspan="2">Number of questions</td><td colspan="3">Percentage of choosing display accurately</td><td>Gender</td></tr><tr><td>Experimental group</td><td>Control group</td><td>Significance (1-tailed)</td><td>Significance (2-tailed)</td></tr><tr><td rowspan="2">2D</td><td>Distance</td><td>3</td><td>90.28%</td><td>77.78%</td><td>.092*</td><td>.578</td></tr><tr><td>Orientation</td><td>1</td><td>91.67%</td><td>75.00%</td><td>.085*</td><td>.695</td></tr><tr><td rowspan="2">3D</td><td>Height</td><td>7</td><td>93.34%</td><td>78.57%</td><td>.005***</td><td>.799</td></tr><tr><td>Shape</td><td>2</td><td>95.83%</td><td>97.92%</td><td>.314</td><td>.768</td></tr></table>

\* Signi<sup>fi</sup>cant at pb.10 level; \*\* Signi<sup>fi</sup>cant at pb.05 level; \*\*\* Signi<sup>fi</sup>cant at pb.01 level.

## 5.5.1. Decision accuracy

Based on the <sup>fi</sup>ndings of prior research, this study used 13 questions to investigate whether DG can help decision makers select appropriate display formats. ANCOVA results (Table 4) indicated that when the tasks were about the distance between objects in the maps or the orientation, research participants in the experimental group were signi<sup>fi</sup>cantly more likely to choose 2D displays. When the tasks dealt with the height of the objects, participants with the assistance of DG were signi<sup>fi</sup>cantly more likely to choose 3D displays. The contribution of DG was not supported when the task was about the shape of the objects in the maps.

## 5.5.2. Decision speed

The ANCOVA results in Table 5 indicated that DG hastened the decision-making process. Participants in the experimental group spent an average of 4 min and 30 s to complete the tasks, signi<sup>fi</sup>cantly faster than those in the control group (mean=5:30). Gender did not alter results. The decision-making time for both groups was rightskewed; nevertheless, the result still held when nonparametric analysis was used (i.e., Mann–Whitney U test's asymptotic signi<sup>fi</sup>cance=.008) or after the data were transformed.

## 5.5.3. Mental workload

To examine the effectiveness of DG and thus provide psychological explanations of why DG contributes to DSS users' performance, we used the NASA-TLX questionnaire to collect participants' selfreported workload during the experiment. One dimension of NASA-TLX, physical workload, was eliminated because our focus was on cognitive workload.

As indicated in Table 5, participants in the experimental group self-reported that they needed marginally more mental and perceptual activity to perform their tasks (one-tailed p-value=.074). Such results suggested that DG users might need more cognitive effort in the early stage to understand and apply DG. An alternative explanation is that DG made the participants aware of the importance of choosing a correct display, which in turn increased their motivation to expend effort on the task. Consistent with the results that DG hastened the decision-making process of experimental group participants, they reported signi<sup>fi</sup>cantly more time pressure during the experiment than those in the control group. Between-group differences in self-evaluations of effort or performance were not observed. Interestingly, participants in the control group felt more frustrated during the experiment, suggesting that the greater competency associated with the presence of DG might translate into affective advantages as well.

ANCOVA results for speed and workload.

<table><tr><td rowspan="2"></td><td colspan="2">Mean (STDEV)</td><td rowspan="2">Significance 1-tailed)</td><td rowspan="2">Gender^ (2-tailed)</td></tr><tr><td>Experimental group</td><td>Control group</td></tr><tr><td>Decision-making time</td><td>4:30(1:53)</td><td>5:30(1:49)</td><td>.025**</td><td>.395</td></tr><tr><td>Workload (NASA-TLX)</td><td></td><td></td><td></td><td></td></tr><tr><td>How much mental and perceptual activity was required to perform previous tasks?</td><td>7.21(2.00)</td><td>6.91(1.59)</td><td>.074*</td><td>.000***</td></tr><tr><td>How much time pressure did you feel during the task?</td><td>5.42(1.91)</td><td>3.50(2.64)</td><td>.001***</td><td>.068*</td></tr><tr><td>How hard did you have to work to accomplish your level of performance?</td><td>5.21(1.61)</td><td>5.13(2.21)</td><td>.443</td><td>.994</td></tr><tr><td>How successful do you think you were in accomplishing the goals of the task?</td><td>7.71(1.00)</td><td>7.67(1.79)</td><td>.494</td><td>.748</td></tr><tr><td>How insecure, discouraged, irritated, stressed, and annoyed did you feel DURING THE TASK?</td><td>1.83(1.24)</td><td>2.58(1.84)</td><td>.035**</td><td>.305</td></tr></table>

^ Gender seems to play a role in the ANCOVA tests, but the sample size (i.e., only three men in the control group) stopped us from further investigations.  
\* Signi<sup>fi</sup>cant at pb.10 level; \*\* Signi<sup>fi</sup>cant at pb.05 level; \*\*\* Signi<sup>fi</sup>cant at pb.01 level.

In summary, Experiment 2 shows that providing novice EMIS users with prospective DG could signi<sup>fi</sup>cantly improve their decisional accuracy and speed and in<sup>fl</sup>uence their mental workload. We used only those participants who passed the manipulation check that they read the DG script. Hence, our results highlight that participants could understand, and also appropriately apply, the principles of choosing a display format for particular decision tasks. Given that one major objective of a DSS tool is to help users make ef<sup>fi</sup>cient and effective decisions in crisis situations, these results show the importance of providing incident commanders an EMIS utilizing both 2D and 3D visualization techniques and giving them guidance on when to use each format.

## 6. Discussion

Crisis situations are critical events that require maximally effective and ef<sup>fi</sup>cient decision making [23,33]. Among the many tools available, an EMIS rendering geospatial information by 3D visualization techniques is an important innovation that has been in the spotlight since the terrorist attacks of September 11, 2001 [10]. Before then, most EMIS presented the geospatial information of the target objects by 2D maps, which means that information about height and shape could be communicated only by symbols, colors, verbal descriptions, or contour maps. For EMIS users or developers, a <sup>fi</sup>xed 2D display strategy forces users to make elevation- or shape-related decisions by translating symbols into internal spatial representations, a transformation that may be time consuming and error prone. Based on the results of prior work, a <sup>fi</sup>xed 3D display strategy may also fail to satisfy users' need to process information ef<sup>fi</sup>ciently or effectively because it provides super<sup>fl</sup>uous information that may distort some perceptual judgments [4,35]. Therefore, two possible strategies seem reasonable to take advantage of the bene<sup>fi</sup>ts of both formats — synthesizing 2D and 3D views together [37], or providing geospatial information both in 2D and 3D displays and allowing users to choose. Focusing on the latter approach, our study suggests that these bene-<sup>fi</sup>ts will be realized if novice EMIS users are given guidance regarding the importance of cognitive <sup>fi</sup>t and methods for choosing display formats for different tasks. Such results not only provide EMIS developers with information regarding potential problems associated with adaptable displays, but also show the signi<sup>fi</sup>cance of providing appropriate decisional guidance.

## 6.1. Limitations

As in any experimental work, this study has several limitations. Creating an experimental scenario that is consistent with its realworld analog is important for ecological validity. Nevertheless, replicating all elements of a crisis situation is dif<sup>fi</sup>cult, if not impossible. Although our study participants were not facing a real crisis, we simulated an emergency situation by asking them to undertake the roles of incident commanders and by emphasizing the importance of quick and accurate responses.

To simplify and expedite the experiment, we adopted the paperprototyping method [34] and provided DG via paper and pencil rather than by actual computer-based or interactive EMIS. Nevertheless, because we intended Experiment 2 to examine the in<sup>fl</sup>uences of prede<sup>fi</sup>ned, prospective DG on novice EMIS users' decisional performance, we believe that the contextual differences between those two methods did not seriously weaken our <sup>fi</sup>ndings. Future researchers who are interested in the dynamics or interactions between DG and users are encouraged to develop or modify an actual EMIS system. In addition, we developed our Experiment 2 questions for each task based on the existing visual displays in Fig. 1. Although we used questions that we felt were practical and that our research participants would relate to, future research could certainly test other tasks. Developing more questions would certainly contribute to establishing content validity as well.

This research examines the in<sup>fl</sup>uences of a prospective DG on EMIS users' decision making. Future should investigate the impacts of alternative formats of DG (e.g., concurrent). To increase the task complexity and remain consistent with prior work [4], Experiment 1 intentionally implemented two plan view examples that differed by rotation (i.e., Panels 1 and 2, Fig. 1), two elevation view examples that differed in layout (i.e., Panels 3 and 4, Fig. 1), and one example for 3D view. Research participants provided informal feedback that revealed possible confusion and unnecessary cognitive burden, especially when they were using the elevation views. Moreover, Experiment 1 was intended to investigate whether novice EMIS users can choose display formats with the best cognitive <sup>fi</sup>t. Therefore, statistical analyses of Experiment 1 grouped <sup>fi</sup>ve displays into three types, and Experiment 2 investigated the impacts of DG by contrasting plan and 3D views only, dropping elevation view. Such change is a trade-off between the task consistency of two experiments and their research objectives. In other words, Experiment 2 is intended to document the in<sup>fl</sup>uences of DG on novice EMIS users' decision making, not to determine how they react spontaneously to different display formats.

## 6.2. Implications for practice

Recently many 3D EMIS have been developed to help incident commanders make decisions [9]. Researchers have urged more thought and effort to identify ways to design and develop EMIS, resulting in frameworks, architectures, and design principles that are helpful to the study of EMIS [4,9–12,19,48]. Our study indicates that, as prior studies have cautioned [7,38,39,42], practitioners should use new technologies judiciously, with appropriate guidance regarding when to use them.

To enhance <sup>fl</sup>exibility in interactive systems, Hansen [13] cited eight user engineering principles that formulated the ingredients of data-entry interaction. One of these principles suggested that system developers should change displays as little as possible to carry out users' requests, as users' display selection inertia may in<sup>fl</sup>uence the functionality of the system [27]. Nevertheless, display selection inertia and its associated concept, familiarity bias, have not been addressed in the DSS literature [p. 1, 22]. We found evidence that DG could help novices select from various display formats and could alleviate the familiarity bias, consistent with the <sup>fi</sup>ndings and suggestions of Marett and Adams [22]. Such <sup>fi</sup>nding may help system developers utilize DG to transition their users to a new DSS with modi<sup>fi</sup>ed or improved interfaces or display formats.

The results of Experiment 1 suggest that making task-display compatibility decisions is not intuitive and that EMIS users, when given a choice, might <sup>fi</sup>xate on a speci<sup>fi</sup>c display format (i.e., 2D or 3D). Thus, before implementing or propagating EMIS that provides adaptable or hybrid displays, novice and even experienced incident commanders must be trained and supported to make the most ef<sup>fi</sup>- cient and effective decisions.

## 6.3. Implications for future research

This research is one of the <sup>fi</sup>rst studies to examine the roles of DG and adaptable 2D/3D displays in crisis and other decisional situations, which opens further research avenues to determine when and how to provide this guidance. As we used a paper-based DG in our study, a <sup>fi</sup>rst step would be to replicate the results in a computer-based EMIS and determine whether DG also contributes in users' decisional performance in this context.

Second, as Silver indicated [29], it is possible to examine various formats of DG that may further improve decisional performance. In this research, we provided DG before novice users made their taskdisplay compatibility decision, similar to traditional orientation or training. Future research should investigate the impact of other types of DG, such as advising EMIS users while they are making decisions, providing concurrent (e.g., pop-up windows) or on-demand DG, or offering other automatic reminders (e.g., “tips of the day”). These alternative forms of DG may lead to different decisional performance or outcomes.

Third, in addition to adaptable displays, various methods have been used to develop EMIS or other DSS. For example, some DSS synthesize multiple 2D/3D views into one [37]; whereas others integrate multidimensional data into a single view (e.g., 4D spatial-temporal displays advocated by [26]). How users interact with those innovative systems and whether DG improves users' decisional performance require more explorations.

Fourth, this study examines the selections of “<sup>fi</sup>t” decision aids and focuses only on one attribute — the dimensionality of visual-spatial representation. As decision making becomes more complicated, many DSS have been developed to incorporate or integrate more data into one display. Whether DSS users can choose the most appropriate visual displays from various alternatives deserves more investigations. For example, Google Maps users can easily add more layers to the 2D or 3D maps (e.g., traf<sup>fi</sup>c, real estate, webcam). Such multivariate displays are increasingly common in safety-critical domains such as air traf<sup>fi</sup>c control, computer-aided surgery, and chemical and physical process control. Unnecessarily adding layers, functions, or colors may increase complexity and inadvertently decrease decisional performance. In fact, a growing literature exists on the bene<sup>fi</sup>ts of display “decluttering” algorithms given inherent limitations in the spatial resolution of human attention [45,46]. As a parallel to the present research, the question will be whether decisional guidance can be used by decision makers to determine how to best apply such information presentation options.

Fifth, the effect size of this research deserves further investigation. Speci<sup>fi</sup>cally, this research assumes that failing to choose the display with the best cognitive <sup>fi</sup>t may result in suboptimal performance or other consequences. How severe these negative in<sup>fl</sup>uences are and whether users can be trained to avoid these problems remain unanswered for all stakeholders.

Sixth, incident commanders work under stress. The role of time pressure and whether it mediates or moderates users' decision making requires more empirical investigation. On one hand, time pressure may lead incident commanders to make decisions chaotically and thus show no clear pattern of display choice; on the other hand, the demand for quick decisions in crisis situations may make users less inclined to manipulate display formats, suggesting higher <sup>fi</sup>xation or display selection inertia. In addition, how DG works under time pressure deserves further empirical investigations.

Seventh, an important but unanswered question is whether the demographics (e.g., age, gender) or personal characteristics (e.g., openness to new technologies) of EMIS users in<sup>fl</sup>uence their display format choices. We encourage future research to determine the independent and joint contributions of DG and individual differences such as experience with different formats and differences in visual-spatial processing capacity.

Last, from a theory perspective, our study extends the vast amount of research on the IS theory of CFT and shows that it is appropriate to design displays for incident commanders. The use of CFT and DG (from MIS theories) and PCP (from human factors and cognitive psychology) also shows that technology design and effectiveness evaluation can be enhanced by adopting interdisciplinary perspectives.

In conclusion, ongoing advances in computational power and information technology are improving the performance, availability, and cost effectiveness of 3D visualization techniques. Whether a greater quantity of EMIS display choices will improve the quality of decision making is an important practical and academic question. Through two experiments we provide evidence that novice EMIS users, without guidance, often fail to choose the display format with the best cognitive <sup>fi</sup>t. However, even simple decisional guidance improves their performance.

## Acknowledgements

We thank the members of the review panel for providing many constructive comments to improve the quality of the manuscript.

## Appendix 1. Experiment Script

Instructions Please read the following information very carefully because you will use this information to answer questions in the following pages. You will see two display formats on the screen in front of you. You have to use these display formats to answer the questions. Please wait after you read this.

## Display formats

Display formats are widely used for decision making. Researchers in psychology and information systems have researched this topic. They <sup>fi</sup>nd that a good match between the decision task and the information display leads to better quality decisions. For example, to make a decision about whether you are spending too much money and need to cut back, you could look at a display that shows the various categories of your expenses. As shown below, although a display format in the form of a table that lists the amount spent for each category is useful, a display format in the form of a pie chart may be more useful and is better, that is, most suited for this task. This is because a pie chart directly shows the size of each category relative to the whole (your total expenses).

![](/api/attachments/9TMQ97DX/fulltext/images/b83b70ac4b07155121b60bb3ba2e14ee6ea563f0c50e98c4f6db7e38e76960aa.jpg)

In the above case, neither of the display formats is 3Dimensional (3D). They are both two dimensional (2D). However, some display formats may be in 3D format where the display will provide information about height, width, area, and volume. But remember that displays with more dimensions are not always better. For decision tasks that require information about overall shape and size of an object or about two objects' relative positions in height, 3D displays are better. In tasks where precise values are required, where distance and direction between two objects are important, or where two objects relative positions in geographic space (i.e., no height) are necessary, 2D displays are better suited. Thus, in choosing a display format for a decision task, one should look at the decision task characteristics and choose the display format (2D or 3D). The following are some examples of the principle.

• To determine the related altitude (e.g., is City A higher than City B in terms of altitude?), 3D display is better.

• To determine how many right turns you must make to get from one house to another, 2D display is better.

• To decide exact directions (e.g., is City A northeast of City B?), 2D display is better.

• To determine the relative sizes of two adjoining buildings, 3D displays are preferred.

## Appendix 2. Control Script

Instructions Please read the following information very carefully because you will use this information to answer questions on the following pages. You will see two display formats on the screen in front of you. You have to use these display formats to answer the questions. Please wait after you read this.

## Display formats

The incident commander's (IC) responsibility is the overall management of the incident. On most incidents the command activity is carried out by a single IC. The IC is selected by quali<sup>fi</sup>cations and experience. The IC determines incident objective and strategy, sets immediate priorities, establishes an appropriate organization, authorizes an incident action plan, coordinates activity for all command and general staff, ensures safety, coordinates with key people and of<sup>fi</sup>cials, authorizes release of information to the news media and the public, and other key duties. The IC uses a variety of display formats in two dimensions (2D) and three dimensions (3D) to help make decisions about the situation.

The IC may also have a deputy, who may be from the same agency or from an assisting agency. Deputies may also be used at section and branch levels of the ICS organization. Deputies must have the same quali<sup>fi</sup>cations as the person for whom they work and they must be ready to take over that position at any time.

The IC is faced with many responsibilities when he/she arrives on scene. Unless speci<sup>fi</sup>cally assigned to another member of the command or general staffs, these responsibilities remain with the IC. Some of the more complex responsibilities include:

• Assess the situation and/or obtain a brie<sup>fi</sup>ng from the prior IC.

• Brief command staff and section chiefs.

• Review meetings and brie<sup>fi</sup>ngs.

• Establish immediate priorities especially the safety of responders, other emergency workers, bystanders, and people involved in the incident. • Establish an appropriate organizatior • Establish an appropriate organization.

• Approve the use of trainees, volunteers, and auxiliary personnel.

• Stabilize the incident by ensuring life safety and managing resources ef<sup>fi</sup>ciently and cost effectively.

• Determine incident objectives and strategy to achieve the objectives.

• Authorize release of information to the news media.

• Ensure planning meetings are scheduled as required.

The time urgency characteristic of responding to major incidents and the fact that the IC is operating in an ambiguous, unstructured, and dynamic environment highlight both the importance of decision making and the complexity inherent in the formulation and implementation of decisions and actions. Hence, the IC must be careful in choosing the right display format (2D or 3D display) to help in the decision tasks relating to the management of the crisis situation.

## Appendix 3. Tasks in Bailey et al. [4]

Display formats showed several blocks in the <sup>fi</sup>ctitious city of College Branch. Participants were told that their task was to make decisions surrounding the deployment of resources after a natural disaster. To test the cognitive <sup>fi</sup>t theory and proximity compatibility principle, Bailey et al. [4] developed and tested three tasks to determine whether users with different displays performed differently.

Task that required only the “horizontal” information of the target object

Using one of <sup>fi</sup>ve display formats (Fig. 1), participants were required to determine whether security personnel were adequately located in College Branch using the following decision criteria: (a) Civilians should be able to reach a building with a security of<sup>fi</sup>cer without having to cross more than one street, and (b) They should not have to cross through an intersection diagonally. Participants' response times were recorded and their accuracy rate was determined for comparison purposes. Overall, participants with the horizontal plan view (Fig. 1, Panel 1) performed signi<sup>fi</sup>cantly more accurately and quickly than those with other views.

## Task that required only the “vertical” information of the target object

Participants were told that suspicious activity had been detected in College Branch, and that they were to determine the most likely “plot” that was being executed. This task required participants to distinguish the following conditions as quickly as possible: (a) Suspects located only on the top three <sup>fl</sup>oors of buildings, indicating a possible biological or chemical attack; (b) Suspects located only on the bottom three <sup>fl</sup>oors of buildings, indicating a possible bombing or arson; (c) Suspects never located on the top three or bottom three <sup>fl</sup>oors (only on central <sup>fl</sup>oors), indicating a possible sniper attack; and (d) Suspects scattered throughout buildings (<sup>fi</sup>tting none of the above), indicating that a plot was unlikely. Results indicated that the horizontal elevation views (Fig. 1, Panel 4) provided the greatest performance support.

Task that required both the “horizontal” and “vertical” information of the target objects

Participants were required to evaluate the location of three <sup>fi</sup>re-<sup>fi</sup>ghters relative to a blaze. Their task was to determine whether the following criteria were met: (a) The three <sup>fi</sup>re<sup>fi</sup>ghters were positioned so that each of them could direct water onto a different facade of the burning building (i.e., required horizontal information); (b) There was a <sup>fi</sup>re<sup>fi</sup>ghter above and below the <sup>fl</sup>oor on which the blaze broke out (i.e., required vertical information). This task was best performed with the 3D display (Fig. 1, Panel 5).

## Appendix 4. Questions for Graph Preference (Adapted from [4])

## Appendix 5. Questions for 3D mental rotation ability

Instruction: Please mentally rotate the objects on the left and answer the question – does the figure on the right show an accurate rotation of the figure on the left? Please circle your answers.

4.

Yes

No

![](/api/attachments/9TMQ97DX/fulltext/images/5e57af4147c189c0381d398c773560da9212754c3c7bd3c08a32625be9ab510a.jpg)

## Appendix 6. NASA-TLX for Workload

Please answer the following questions by circling the number that best describes your feelings DURING THE TASK.

1. How much mental and perceptual activity was required to perform previous tasks?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Very Low</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Very High</td></tr><tr><td colspan="10">Note: Higher mental and perpetual activity requires more thinking, deciding, calculating, remembering, looking, and searching.</td></tr></table>

2. How much time pressure did you feel during the task?

<table><tr><td>1Very Low</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10Very High</td></tr></table>

3. How hard did you have to work to accomplish your level of performance?

<table><tr><td>1Very Low</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10Very High</td></tr></table>

4. How successful do you think you were in accomplishing the goals of the task?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Very Poor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Very Good</td></tr></table>

5. How insecure, discouraged, irritated, stressed, and annoyed did you feel DURING THE TASK?

<table><tr><td>1Very Low</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10Very High</td></tr></table>

## Appendix 7. Experimental Tasks

Please look carefully at the two types of display format maps on the screen in front of you. Either type of display format, 2D or 3D, provides similar information about a disaster situation. But only one display format can be shown to an incident commander who is in charge of the crisis situation. Based on the information your received, indicate which of the two display formats (2D or 3D?) should an incident commander use for the following decision tasks so as the make the most accurate and quick decision. He may assign a security of<sup>fi</sup>cer to the area. Consider the affected area only and circle your correct answer.

1. The incident commander thinks that that the distance from 2D 3D Winchester Ave. to Ashland Ave is longer than the distance from Winchester Ave. to Frankfort Ave. Which display will be suited to determine if he is right?

2. Which of the following avenue is closer to Frankfort Ave.? Which 2D 3D display will be suited to this decision task?

3. The incident commander thinks that the distance from to Frankfort Ave 2D 3D to Winchester Ave is shorter than the distance from Winchester Ave. to Ashland Ave. Which display will be suited to determine if he is right?

4. The incident commander thinks Ashland Avenue is north of Winchester 2D 3D Avenue. Which display will be suited to determine if he is right?

5. In the area between Frankfort and Winchester Avenues, is the 2D 3D biohazard in the tallest building? Which display is best suited to answer this question?

6. Are any of the biohazards located above the <sup>fi</sup>re? Which display is best 2D 3D suited to answer this question?

7. Are any of the biohazards in different buildings level with one 2D 3D another? Which display is best suited to answer this question?

8. The incident commander wants to know whether any of the <sup>fl</sup>oors that 2D 3D contain biohazards is more than two <sup>fl</sup>oors below the top of the building. Which display is best suited to answer and help the incident commander in this decision task?

9. Assume that a security of<sup>fi</sup>cer is now inside the building with the <sup>fi</sup>re 2D 3D and is on the <sup>fl</sup>oor directly beneath it. Is it possible for the of<sup>fi</sup>cer to see the tops of all the other buildings between Winchester and Frankfort Avenues? Which display is best suited to answer this question?

10. To land a helicopter, a <sup>fl</sup>at area that is of suf<sup>fi</sup>cient size for the helicopter is 2D 3D necessary. In the meantime, the landing area should be free of obstruction and have no taller buildings within a short distance. To determine where to land a helicopter among two buildings, which display format is better suited?

11. If an incident commander wants to determine appropriate helicopter 2D 3D landings spots on top of a building which of the two display formats is better suited to his decision task?

12. Skyscrapers have more height than width, so they seem tall and 2D 3D skinny. On the contrary, shopping mall buildings have more width than height, so they look short and stout. To determine which of two buildings looks relatively more like a skyscraper, which display is better suited?

13. In the above, to determine which of the two buildings looks relatively 2D 3D more like a shopping mall, which display format is better suited?

## References

[1] S. Antony, R. Santhanam, Could the use of a knowledge-based system lead to implicit learning? Decision Support Systems 43 (1) (2007) 141–151.

[2] S. Antony, D. Batra, R. Santhanam, The use of a knowledge-based system in conceptual data modeling, Decision Support Systems 41 (1) (2005) 176–188.

[3] N. Baddoo, T. Hall, De-motivators for software process improvement: an analysis of practitioners' views, Journal of Systems and Software 66 (1) (2003) 23–33.

[4] K. Bailey, C.M. Carswell, R. Grant, L. Basham, Geospatial perspective-taking: how well do decision makers choose their views? 51st Annual Meeting of the Human Factors and Ergonomics Society, Santa Monica, CA, 2007, pp. 1246–1248

[5] L. Carver, M. Turoff, Human-computer interaction: the human and computer as a team in emergency management information systems, Communications of the ACM.50 (3)(2007).33–38

[6] W.N. Dilla, P.J. Steinbart, Using information display characteristics to provide decision guidance in a choice task under conditions of strict uncertainty, Journal of Information Systems 19 (2) (2005) 29–55

[7] R.B. Dull, D.P. Tegarden, A comparison of three visual representations of complex multidimensional accounting information, Journal of Information Systems 13 (2) (1999) 117–131.

[8] L. Findlater, J. McGrenere, A comparison of static, adaptive, and adaptable menus, Proceedings of the 2004 conference on Human factors in computing systems, 2004, pp. 89–96.

[9] S. Fitrianie, L.J.M. Rothkrantz, A Visual Communication Language for Crisis Management, 2008.

[10] S. Fitrianie, D. Datcu, L.J.M. Rothkrantz, Constructing knowledge of the world in crisis situations using visual language, ICSMC 06, IEEE International Conference on Systems, Man and Cybernetics, 1, 2006.

[11] E.A. Gomez, Crisis response communication management: increasing message clarity with training over time, in: F. Fiedrich, B.V.d. Walle (Eds.), 5th International ISCRAM Conference, Washington DC, USA, 2008, pp. 368–375.

[12] J. Hale, A layered communication architecture for the support of crisis response, Journal of Management Information Systems 14 (1) (1997) 235–255.

[13] W.J. Hansen, User engineering principles for interactive systems, ACM, 1971, pp. 523–532.

[14] S. Hart, L. Staveland, Development of NASA-TLX (Task Load Index): results of empirical and theoretical research, Human Mental Workload, 1, 1988, pp. 139–183.

[15] B. Hosack, The effect of system feedback and decision context on value-based decision-making behavior, Decision Support Systems 43 (4) (2007) 1605–1614.

[16] J.J. Jiang, G. Klein, Side effects of decision guidance in decision support systems, Interacting with Computers 12 (5) (2000) 469–481.

[17] D.R. Jones, P. Wheeler, R. Appan, N. Saleem, Understanding and attenuating decision bias in the use of model advice and other relevant information, Decision Support Systems 42 (3) (2006) 1917–1930.

[18] G. Keppel, Design and Analysis: a Researcher's Handbook, 2nd ed. Prentice-Hall, Englewood Cliffs, New Jersey, 1991.

[19] M.P. Kwan, J. Lee, Emergency response after 9/11: the potential of real-time 3D GIS for quick emergency response in micro-spatial environments, Computers, Environment and Urban Systems 29 (2) (2005) 93–113.

[20] C.A. Looney, R.S. Poston, A.Y. Akbulut, Advice availability and gender differences in risky decision making: a study of online retirement planning, 40th Hawaii International Conference on System Sciences, (IEEE, Hawaii, 2007), 2007, p. 408.

[21] L.S. Mahoney, P.B. Roush, D. Bandy, An investigation of the effects of decisional guidance and cognitive ability on decision-making involving uncertainty data, Information and Organization 13 (2) (2003) 85–110.

[22] K. Marett, G. Adams, The role of decision support in alleviating the familiarity bias, 39th Hawaii International Conference on System Sciences, (Kauai, Hawaii, 2006), 2006, p. 31b-31b.

[23] D. Mendonca, Decision support for improvisation in response to extreme events: learning from the response to the 2001 World Trade Center attack, Decision Support Systems 43 (3) (2007) 952–967.

[24] A.R. Montazemi, F. Wang, S.M. Khalid Nainar, C.K. Bart, On the effectiveness of decisional guidance, Decision Support Systems 18 (2) (1996) 181–198

[25] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2) (2001) 303–332.

[26] S. Rozzi, W. Wong, P. Woodward, P. Amaldi, B. Fields, E. Panizzi, A. Malizia, A. Boccalatte, A. Monteleone, L. Mazzuchelli, Developing visualisations to support spatialtemporal reasoning in ATC, 2nd International Conference on Research in Air Traf<sup>fi</sup>c Transportation, Belgrade, Serbia and Montenegro, 2006.

[27] J. Sena, L. Smith, Applying software engineering principles to the user application interface, Human factors in management information systems, 1988, p. 103.

[28] M.S. Silver, Decisional guidance for computer-based decision support, MIS Quarterly 15 (1) (1991) 105–122.

[29] M.S. Silver, Decisional guidance – broadening the scope, in: P. Zhang, D. Galletta (Eds.), Human-computer Interaction and Management Information Systems: Foundations, ME Sharpe, 2006, p. 20.

[30] D.T. Singh, Incorporating cognitive aids into decision support systems: the case of the strategy execution process, Decision Support Systems 24 (2) (1998) 145–163.

[31] H.S. Smallman, M.S.T. John, Naive realism: misplaced faith in realistic displays, ergonomics in design, The Quarterly of Human Factors Applications 13 (3) (2005) 6–13.

[33] J.A. Sniezek, Training for crisis decision-making: psychological issues and computerbased solutions, Journal of Management Information Systems 18 (4) (2002) 147–168.

[34] C. Snyder, Paper prototyping: the fast and easy way to design and re<sup>fi</sup>ne user interfaces, Morgan Kaufmann, 2003.

[35] M. St John, M.B. Cowen, H.S. Smallman, H.M. Oonk, The use of 2D and 3D displays for shape-understanding versus relative-position tasks, Human Factors: The Journal of the Human Factors and Ergonomics Society 43 (1) (2001) 79–98.

[36] M. Tory, Combining 2D and 3D views for visualization of spatial data, School of Computing Science, Simon Fraser University, Burnaby, B.C. Canada, 2004, p. 218.

[37] M. Tory, T. Moller, M.S. Atkins, A.E. Kirkpatrick, Combining 2D and 3D views for orientation and relative position tasks, Proceedings of the SIGCHI conference on Human factors in computing systems (2004) 73–80.

[38] E. Tufte, The Visual Display of Quantitative Information, 2nd ed. Graphics Press, Cheshire Connecticut. 2001.

[39] M. Turoff, C. White, L. Plotnick, S.R. Hiltz, Dynamic emergency response management for large scale decision making in extreme events, in: F. Fiedrich, B.V.d. Walle (Eds.), 5th International ISCRAM Conference Washington DC USA. 2008 pp 462–470

[40] B. Van de Walle, M. Turoff, Decision support for emergency situations, Information Systems and E-Business Management 6 (3) (2008) 295–316.

[41] I. Vessey, Cognitive <sup>fi</sup>t: a theory-based analysis of the graphs versus tables literature, Decision Sciences 22 (2) (1991) 219–240.

[42] I. Vessey, The theory of cognitive <sup>fi</sup>t, in: P. Zhang, D. Galletta (Eds.), Human-computer Interaction and Management Information Systems: Foundations, M.E. Sharpe, Armonk, New York, 2006, pp. 141–183.

[43] W. Wang, I. Benbasat, An empirical investigation of intelligent agents for e-business customer relationship management: a knowledge management perspective, 11th European Conference on Information Systems, Naples, Italy, 2003.

[44] C.D. Wickens, C.M. Carswell, The proximity compatibility principle: its psychological foundation and relevance to display design, Human Factors 37 (3) (1995).

[45] C.D. Wickens, J.G. Hollands, Engineering Psychology and Human Performance, 3 ed. Prentice Hall New York 1999

[46] C.D. Wickens, J.S. McCarley, Applied Attention Theory, 1 ed. CRC, Boca Raton, 2008.

[47] V.E. Wilson, I. Zigurs, Decisional guidance and end-user display choices, Accounting, Management and Information Technologies 9 (1) (1999) 49–75.

[48] S. Zlatanova, D. Holweg, 3D Geo-information in emergency response: a framework, Proceedings of the Fourth International Symposium on Mobile Mapping Technology (MMT'2004), 2004, pp. 29–31, March.

Milton Shen is an Assistant Professor of Accounting at University of Alabama in Huntsville. He received his Ph.D. degree in decision science and information systems from University of Kentucky and two master degrees of accountancy from National Chengchi University in Taiwan and from the Ohio State University. His research and teaching interests lie mainly in the areas of accounting and management information systems, including such topics as graphical <sup>fi</sup>nancial reporting, impression management, business analytics, information technology adoption, and decision support systems.

Melody Carswell is an Associate Professor of Psychology at the University of Kentucky. She is also Associate Director of the university's multidisciplinary Center for Visualization and Virtual Environments, coordinator of the graduate certi<sup>fi</sup>cate program in human-technology interaction studies, and current editor or Ergonomics in Design. Before taking her current position, she was a faculty member at the University of Louisville. She received her A.M. and Ph.D. degrees in engineering psychology from the University of Illinois at Urbana-Champaign.

Radhika Santhanam is a Gatton Endowed Research Professor in the Gatton College of Business & Economics at the University of Kentucky. Her research interests lie in the area of human–computer interaction with a focus on understanding employee learning of new information technologies. Her research <sup>fi</sup>ndings are published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, In ternational Journal of Human-Computer Studies, Information and Organization, and other journals. She served as an associate editor of MIS Quarterly and Computers and Operations Research. She currently serves as an associate editor of Decision Support Systems.

Kyle Bailey graduated with a graduate degree in psychology from the department of Psychology at the University of Kentucky. He is currently an interface specialist at Lexmark International, a printer manufacturing corporation in Lexington, Kentucky.
