---
otero_id: 26500
otero_key: "VEMY8BDK"
title: "The Impact of Experience and Time on the Use of Data Quality Information in Decision Making"
authors: "Craig W. Fisher; InduShobha Chengalur-Smith; Donald P. Ballou"
year: "2003"
journal: "Information Systems Research"
doi: "10.1287/isre.14.2.170.16017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/VEMY8BDK/fulltext/images/9abf8a0fee0c493a56eec5f8136a5fa2b9287d045ef62f537c8b7477f28cbcaa.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Impact of Experience and Time on the Use of Data Quality Information in Decision Making

Craig W. Fisher, InduShobha Chengalur-Smith, Donald P. Ballou,

To cite this article:

Craig W. Fisher, InduShobha Chengalur-Smith, Donald P. Ballou, (2003) The Impact of Experience and Time on the Use of Data Quality Information in Decision Making. Information Systems Research 14(2):170-188. http://dx.doi.org/10.1287/ isre.14.2.170.16017

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2003 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/VEMY8BDK/fulltext/images/1582f524cb3f9d6e6296db7e86a109af28d6ff40a94f9b4091943d3b3f9b1e35.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Impact of Experience and Time on the Use of Data Quality Information in Decision Making

Craig W. Fisher • InduShobha Chengalur-Smith • Donald P. Ballou Information Systems, Marist College, Poughkeepsie, New York 12601 Management Science and Information Systems, SUNY, University at Albany, Albany, New York 12222 Management Science and Information Systems, SUNY, University at Albany, Albany, New York 12222 craig.fisher@marist.edu • shobha@albany.edu • d.ballou@albany.edu

D<sup>ata</sup> <sup>Quality</sup> <sup>Information</sup> <sup>(DQI)</sup> <sup>is</sup> <sup>metadata</sup> <sup>that</sup> <sup>can</sup> <sup>be</sup> <sup>included</sup> <sup>with</sup> <sup>data</sup> <sup>to</sup> <sup>provide</sup>the user with information regarding the quality of that data. As users are increasingly removed from any personal experience with data, knowledge that would be beneficial in judging the appropriateness of the data for the decision to be made has been lost. Data tags could provide this missing information. However, it would be expensive in general to generate and maintain such information. Doing so would be worthwhile only if DQI is used and affects the decision made.

This work focuses on how the experience of the decision maker and the available processing time influence the use of DQI in decision making. It also explores other potential issues regarding use of DQI, such as task complexity and demographic characteristics. Our results indicate increasing use of DQI when experience levels progress through the stages from novice to professional. The overall conclusion is that DQI should be made available to managers without domain-specific experience. From this it would follow that DQI should be incorporated into data warehouses used on an ad hoc basis by managers.

(Data Quality; Information Quality; Data Quality Information (DQI); Decision Making; Data Quality Tags; Data Warehouse; Metadata)

## Introduction

It has long been recognized that the effectiveness of decision making is influenced by many factors. Among these are the time available before the decision must be rendered, the experience of the decision maker, and the quality of the data needed for the decision. Although ideally the data used should be of high quality, in practice this often is not the case, for reasons that range from the cost of obtaining quality data to the inherent difficulty or even impossibility of doing so for certain data types. Nevertheless, experienced decision makers, especially ones who have worked in a particular milieu for a sufficient period of time, develop a feel for the nuances and eccentricities of the data used and intuitively compensate for them. As organizations increasingly move to stored repositories such as data warehouses, this intuitive feel is not preserved for many who extract data from such sources to support their particular needs.

One solution would be to capture some of the knowledge regarding the data’s quality along with the actual data values. Data tagging to provide information regarding the data has long been proposed (Wang and Madnick 1990); however, it is not clear how or if decision makers would use this data quality information. Chengalur-Smith et al. (1999) define data quality information (DQI) to be metadata that addresses the data’s quality. Clearly, any benefits that accrue from providing information about the quality of the data must outweigh the cost of obtaining and maintaining this metadata. Although logic dictates that DQI would be of benefit, it is also plausible that the benefit of such information would vary considerably depending upon the circumstances.

The effect of providing data quality tags on decision making in controlled environments was explored by Chengalur-Smith et al. (1997, 1998, 1999). They determined that DQI does indeed influence the decision made, but also found differences in the amount of influence based upon factors such as complexity of task, decision strategy, and format of the DQI. Unfortunately, their work provides no guidance as to when it would be appropriate to include DQI in databases. For this, it is necessary to study the behavior of actual decision makers vis-à-vis DQI. Experienced decision makers might find DQI of greater value than inexperienced ones. Also, one would suppose that time constraints (time available for the decision) and time pressures (perceptions about time constraints) would impact the use of DQI. The purpose of this paper is to explore the use of DQI by decision makers, who have various experience levels and who are required to make decisions under various time conditions, to determine who would most benefit from the inclusion of DQI and under what circumstances. Information of this sort would guide data managers as to whether to include DQI in databases.

## Background and Research Model

The diverse uses of data and the increased sharing of data that has arisen as a result of the widespread introduction of data warehouses have exacerbated deficiencies with the quality of data (Ballou and Tayi 1999, Haisten 1995). Researchers have identified many facets or dimensions of data quality such as accuracy, timeliness, completeness, consistency, relevance, and so forth (Ballou and Pazer 1995, Wang and Strong 1996). Wang and Strong (1996) investigated characteristics of data quality from the data consumer perspective and found that of the various dimensions of data quality, data accuracy (used interchangeably with reliability) was most important. For this study, we chose to focus on a single dimension of data quality, namely accuracy. A review of the field of data and information quality research may be found in Wand and Wang (1996) and Wang et al. (1995).

## Decision Processing

Decision making is a response to problems where the problems include choices from among a set of alternatives (Kingma 1996). Over the last half-century significant research has been conducted on decision-making processes and strategies. Simon (1957) defined a rational model of decision making in which decision makers consider all aspects of all alternatives before making a decision. However actual decision making often falls short of the rational ideal (March and Simon 1958). Some of the reasons that decision making falls short of the ideal is that knowledge is incomplete, experience of the consequence is incomplete, there is limited amount of time to explore all alternatives, and humans do not calculate perfectly (March and Simon 1958). These factors have influenced our choice of factors to consider in this study.

Payne et al. (1993) identified seven decision-making strategies and combinations thereof. These strategies may be grouped into two fundamental types— weighted additive and conjunctive. In weighted additive decision making, weights are assigned to each attribute and scores are assigned based on how closely an attribute matches the goals of the decision problem. For each alternative, each attribute is evaluated and the resulting score is multiplied by the weight. These values are then summed to produce an overall score, and the alternative with the largest score is chosen. This summation and weighting process allows for an alternative to be chosen that may have weak scores on some attributes, but high scores on other attributes. In contrast, the conjunctive strategy sets minimum acceptable levels for each attribute. If an alternative has a low score on even one attribute that alternative will be rejected.

In the bounded rationality model (March and Simon 1958), decision makers look for heuristics to reduce task demands. When making a decision, individuals will use a compromise strategy that minimizes their cognitive effort (Payne et al. 1993) and will ignore less relevant information in complex problems (Grether et al. 1986). Thus the nonuse of DQI, if DQI is not recognized as relevant, may be a function of the level of task complexity.

## Task

The degree of task complexity is implied by the number of cells in the decision space that is constructed by building a matrix of decision choices (alternatives) and decision criteria (attributes). Prior research has indicated that 20 cells represent a relatively simple task, while complex tasks may have as many as 40, 60, or 80 cells (Payne et al. 1993).

Chengalur-Smith et al. (1997, 1998, 1999) used a 20-cell apartment selection task to study the use of DQI in a simple task setting. For a complex task they used a business site selection task with 42 cells; their subjects had no problem with these levels of complexity. The subjects were college seniors working under the same time constraints. (By contrast, our study uses novices, experienced managers, and professionals under various time conditions.) Morrow et al. (1992) stated that experience is only important when a task is difficult enough to call on the domain-relevant knowledge; therefore, it was important to develop a task that was more complex than the one that was accomplished by college seniors.

A newly developed job transfer task with 63 cells fits these requirements. This task describes seven alternative jobs along with nine attributes of each job. Subjects are requested to rank the jobs according to predefined weights and scores of each attribute. (See Appendix A). This task provides the ability to examine results by domain-specific experience as well as by general experience. Some people have not changed jobs, some have changed jobs once or twice, and some have changed jobs multiple times.

## Decision Outcome

In a multiattribute decision-making task an actor chooses one alternative from among many alternatives or ranks all alternatives from most preferred to least preferred. Each alternative is described by several attributes. The values of these attributes form the basis for the actor’s decision, such as buying a car based on attributes such as price, safety record, and maintenance record. The choice of one alternative among many alternatives represents the decision outcome. Varying the value of attributes changes the decision outcome to the degree that actors use the attributes in their decision making.

To study the effect of a new attribute, e.g., consumer rating, researchers may compare decisions made by several people without consumer rating to decisions made by several people with consumer rating. If these groups of people are randomly established and the only difference in the multiattribute task is the existence of the consumer rating, then any difference in the decision choices from one group to the next may be attributable to use of consumer rating in the decision process. When the addition of a new variable does not lead decision makers to make a new decision, then it is said that the decision makers were complacent to the new variable. When the addition of a new variable leads to a new decision, the decision makers were not complacent with respect to the new variable. If the decision makers were not complacent but there was a scattering of multiple new first choices, then there is less consensus. If the decision makers change their order of rankings, then there is less consistency.

To operationalize decision outcome we employ three measures of the impact of DQI (Chengalur-Smith et al. 1997, 1998, 1999). These are: Complacency (a measure of the lack of impact of DQI), consensus (a measure of agreement on the top choice in the presence of DQI), and consistency (a measure of the degree to which the overall rankings are not affected by DQI). These three variables are defined in the context of individual decision making involving decision problems with multiattribute alternatives. Complacency and consensus consider changes in the top-ranked alternative, whereas consistency considers changes in the ranking of all alternatives. The three measures explore different aspects of the impact of DQI, but are not independent.

Complacency is the proportion of people in one group who choose a specific alternative for their first choice as compared to the proportion of people in a second group who choose the same alternative for their first choice. To measure complacency, we identify the top-ranked alternative (say Alternative B) for a group without DQI and record its frequency. We then count the number of subjects that identified the same alternative (here B) among a group with DQI. Because we are examining proportions and dealing with categorical data, the chi-square test of homogeneity is appropriate (Sheskin 2000). A significant chi-square indicates that the groups differed due to the influence of DQI and thus were not complacent, a desirable outcome (Table 1).

Lack of complacency indicates that the people with DQI used it. However, people may use DQI differently, which brings us to consensus. Consensus is similar to complacency in that it compares proportions of people in two groups as to their most-preferred alternative. Consensus differs from complacency in that the most-preferred alternative may be different in each group. Differences in the number of times the top-ranked site is selected by members of the two groups are compared using chi-squared statistics. A significant chi-squared value indicates a change in consensus, implying that DQI either detracted from or enhanced a group’s ability to reach a decision. Or, a significant chi-square indicates a change in the level of agreement, which could be a result of increased uniformity or decreased uniformity. Thus, complacency alone does not provide a complete measure of the impact of DQI. Note that complacency and consensus may be in a hierarchical relationship to each other; i.e., consensus should only be considered after noncomplacency is established.

In some cases the focus may not be on just the top-ranked alternative. Decision consistency refers to the rankings of all alternatives from the most preferred to the least preferred. Thus, consistency can be considered an extension of complacency because it considers the entire set of rankings instead of just the top-ranked alternative. Consistency indicates that

Table 1 Ideal Values for Measures of DQI

<table><tr><td>Measure</td><td>Ideal</td><td>Implication</td></tr><tr><td>Complacency</td><td>Low (high chi-square)</td><td>DQI was used—different first choice</td></tr><tr><td>Consensus</td><td>High (low chi-square)</td><td>DQI did not change level of agreement</td></tr><tr><td>Consistency</td><td>Low (low correlation)</td><td>DQI was used—rankings varied</td></tr></table>

DQI did not influence the decision. To measure consistency, a correlation is performed between the two groups of average rankings for each alternative, with and without DQI. A significant correlation between one group’s rankings and another group’s rankings implies consistency between the groups’ results. Low correlation implies that DQI caused a difference in the overall rankings.

## Experience Level

Gilliland et al. (1994, p. 406) state that there has been “relative lack of attention to the study of prior knowledge in the decision-making literature.” One would expect that experience is an important variable to study in decision making, but there are conflicting possibilities regarding its significance. Some researchers state that experience may improve performance in decision making, while others state the opposite.

Experience may improve performance because it increases alertness to errors (Klein et al. 1997), sensitivity to omissions (Sanbonmatsu et al. 1992), use of relevant information (Sanbonmatsu et al. 1992), adaptation to subtle contextual differences (Payne et al. 1993), ability to identify important features of a problem (Mackay and Elam 1992), ability to organize the information better (Mao and Benbasat 2000), ability to attend to greater amounts of knowledge (Mao and Benbasat 2000) and process it more extensively (Sanbonmatsu et al. 1992). The benefits of experience may be attributable to domain-specific knowledge (Morrow et al. 1992). Mao and Benbasat (2000) stated that domain-specific knowledge is a critical factor in reading-comprehension studies, while Shaft and Vessey (1995) said domain knowledge aids computer programming comprehension. For these reasons it appears that experts would make more use of DQI than novices.

However, there are potential dangers in assuming that an intuitive feel for the data is always positive. Experience may not influence accuracy (Paese and Sniezek 1991), prior experience influences beliefs and expectations about data (Klein et al. 1997), and may truncate the decision process early (Dukerich and Nichols 1991, Hall 1991). A novice may be more attentive to new information (such as DQI) than an expert (Yates et al. 1991). For example, in a business relocation task, people without task-specific experience gave more accurate ratings than did experienced people (Gilliland et al. 1994).

Earlier studies did not have a uniform definition of experience. Chengalur-Smith et al. (1999) found little impact of DQI in complex task scenarios with undergraduate students, and therefore called for research using more experienced people as subjects. Klein (1997) used a mix of graduate and undergraduate students. Mackay and Elam (1992) used professional employees only, and Yates et al. (1991) and Gilliland et al. (1994) used a combination of novices and domain experts. Given the mixed results of these prior studies, we investigated multiple levels of experience, including novice (college freshmen) vs. expert (working MIS professionals); experts working less than or equal to 10 years vs. experts working greater than 10 years; domain-specific experience vs. nondomain-specific experience; and managerial vs. nonmanagerial experience.

## Time

Researchers typically study decision making without time constraints (Ordonez and Benson 1997, Payne et al. 1993). Some researchers (e.g., Ahituv et al. 1998, Morrow et al. 1992) have studied “time pressure” but measured “time pressure” by simply allocating specific time to perform a task. We distinguish between time constraints and time pressure. A time constraint is a specific allotment of time for making a decision, while time pressure is a subjective reaction to the amount of time allotted. Time pressure is experienced whenever the time available for the completion of a task is perceived as being shorter than normally required for the activity (Svenson and Edland 1987). Some people may feel pressure in a long time constraint while others may not feel time pressure in a short time constraint (see Figure 5 in this paper).

While time pressure affects decision processes (Payne et al. 1993), there are some mixed results as to the effects of time on decision making. Some say that time pressure decreases decision accuracy (Zakay and Wooler 1984), while others say that increasing time pressure may increase quality in software development projects (Austin 2001). Time constraints may have more impact on decision making for novices than for the sophisticated decision makers (Dukerich and Nichols 1991). Ahituv et al. (1998) found that time pressure impaired the performance of middle-level field commanders more than it affected top-level commanders. Payne et al. (1993) found that an increase in domain-specific experience level under time pressure improved performance. The time factors, constraint or pressure, have not been studied in relationship to DQI and experience levels until this present study.

In Figure 1, the rectangles represent constructs, the double ovals represent measures (variables), and the ovals represent the values of the measures or constructs. It should be noted that many of the independent variables displayed in Figure 1 take on multiple values; e.g., the variable pressure has two values (felt time pressure and did not feel time pressure). For the sake of simplicity we did not display all of these. Our primary focus is on the exploration of the impact of DQI, together with various facets of time and experience on decision outcome. As seen in Figure 1, we place time and experience in the context of task complexity and also consider three demographic variables: Age, gender, and education.

## Hypotheses

The hypotheses that we explore are motivated by the research described earlier and focus on the time and experience aspects of the research model given in Figure 1. Experience and time are investigated within the context of task complexity. Later, we briefly discuss the role of demographics.

Hypothesis 1 (Experience). For a given value of experience, there will be no differences in decision outcome between subjects with and without DQI.

In the case of experts, this null hypothesis will be tested using the different variables describing expertise that are shown in Figure 1.

Hypothesis 2 (Time). For a given measure of time, there will be no differences in decision outcome between subjects with and without DQI.

This null hypothesis will be tested for different values of the measures of time shown in Figure 1.

Figure 1 Research Model  
![](/api/attachments/VEMY8BDK/fulltext/images/86cd049485270aaf79d4b3736a8fed1d9cae49483de15b6f3756c98425e4643d.jpg)

## Research Method

We performed two experiments to explore the effect of providing DQI in multiattribute decision-making tasks of varying complexity, using subjects with various experience levels and assigned to different time constraints. For the DQI we used interval numbers ranging from 0 to 1, where 1 implies the highestpossible quality and 0 implies no quality.

## Pilot

To test our procedures and determine appropriate time constraints, we conducted pilot tests and recorded the amount of time required to complete the tasks. The pilot studies provided feedback as to the usability and clarity of the questionnaire instruments, and the intelligibility and consistency of the tasks and procedures.

The pilot study for the simple task included 17 undergraduate students. They took a mean time of 11.2 minutes and a median of 12 minutes to complete this task. The standard deviation was three minutes. All subjects in the pilot finished in less than 40 minutes. To create a short time constraint, we employed the shorter of the Median Method (van Bruggan et al. 1998) or the Mean Method (Ordonez and Benson 1997). The subtraction of one standard deviation from the mean yielded a short time of eight minutes. The short time constraint for the simple task was set at eight minutes and the long time constraint at one hour.

The pilot study for the complex task was conducted with 11 graduate students in a systems design course. Eight of the subjects were full-time employees within the community, while three were fulltime students who completed at least one semester of internship and one full year of graduate school. The mean time required to complete the complex task was 24.2 minutes and the standard deviation was eight minutes. The longest completion time was 35 minutes. Because one of the primary goals of this research was to explore the effect of time, we employed three different time constraints with the expert subjects. The short time constraint for the complex task was set at 15 minutes, the medium time constraint at 25 minutes, and the long time constraint at 45 minutes. The subjects reported that there were no ambiguities in either the task or the questionnaire.

## Experiment 1

Subjects. We used two groups of subjects: Novices and experts. There were 118 novices who were students majoring in computer science, information systems, or information technology and enrolled in a freshman seminar course. There were 21 females and

97 males. There were 38 experts who were professional employees in an information systems organization at a major international service company. This random group had 19 males and 19 females; 27 had managerial experience while 11 did not; 6 had high school education, 1 had two years of college, 25 had a bachelor’s degree, and 6 completed a master’s degree. For the context of our experiments there is face validity to our assertion that the IS professionals had more experience than the freshmen. This assertion was confirmed in our questionnaire (see Question 7, Appendix B) relating to the apartment selection task. Most of the IS professionals had experience in choosing their own apartments, but only a handful of freshmen had ever chosen an apartment on their own.

All subjects were volunteers and received no pay or credit for this activity.

Task. A simple task with only 20 cells required the subjects to select an apartment from among four alternative apartments, based on 5 criteria (Payne et al. 1993, Chengalur-Smith et al. 1999). The five criteria were weighted and scored for each apartment; the weighted scores were provided for each attribute, but were not summed for each alternative. Two forms of the simple task were used, one without data quality information and one with data quality information. All subjects involved with a particular task were given the same numbers for each of the cells in the alternative-criteria matrix. Those with the DQI, however, had additional information as to how reliable some or all of those attributes were. The numbers in the cells and the DQI values were specified so that at an intuitive level at least the inclusion of DQI would be likely to result in different rankings of the alternatives. For instance, Apartment B is very attractive without DQI but much less attractive with DQI. Thus, if the rankings did not change, then the DQI clearly was ignored.

Procedure. Experiment 1 was conducted at two different locations, the national MIS headquarters of an international service company, and on a college campus. Novices and experts were randomly divided into two time groups, short and long, at their respective locations. Within each time constraint, approximately half of the subjects received tasks with no DQI and the other half received tasks with DQI. As each subject completed the task, the moderator collected demographic data on a questionnaire (Appendix B). The procedure was strictly controlled so that the subjects did not view the questionnaire until finished with the task.

## Experiment Design—Experiment 2

Subjects. There were 69 experts who were employed in the information systems department of an international service company. All subjects had at least one full year of work experience, while 34 had greater than 10 years of experience and 35 had less than or equal to 10 years of work experience; 17 were less than or equal to 30 years old, while 51 were greater than 30 years old. There were 28 females and 41 males; 40 reported having at least one year of managerial experience, while 29 did not have managerial experience; 24 had experienced at least one job change that required a household move, while 44 did not have a job change that required a household move. All subjects were volunteers and received no pay or credit for this activity.

Task. A “job transfer task” was developed for this study. The goal was to create a complex task that was deemed to be real and interesting to a group of experienced professionals. In addition, we needed to have a common problem with which the professionals had varying degrees of personal experience and knowledge.

The job transfer task is a complex multiattribute decision task with seven alternatives, each described by nine attributes (Appendix A). Subjects are asked to rank job alternatives from most desirable to least desirable, based on criterion attributes that are weighted (prioritized) and scored. Two forms of the job transfer task were used, one without data quality information and one with data quality information. The nine criteria were weighted and scored for each job; the weighted scores were provided for each attribute but were not summed for each alternative. If a subject used the weighted additive decision process, Alternative B would be the preferred outcome without DQI; with DQI, Alternative G would be preferred and Alternative B would be towards the bottom of the list (see Appendix A).

Procedure. The 69 experts were divided randomly into three time-control groups. There were 21 people in the short time-constraint group, 23 people in the medium time-constraint group, and 25 in the long time-constraint group. Each of these three groups was randomly subdivided into two groups: Those who received tasks with no DQI and those who received tasks with DQI. The task description informed those subjects with DQI of the presence of DQI but did not suggest how to use the DQI. For tasks without DQI there was no mention of DQI.

A posttask questionnaire was used to obtain information to group people by domain-specific experience, years of work experience, management experience, perceptions of time pressure, age, gender, and education.

## Results

The primary purpose of this study was to explore the effects of experience and time on the use of DQI in decision making. We first explore the effects of experience on the use of DQI and later explore different combinations of experience and time. Finally, we address some demographic questions.

## Experience

Table 2 shows the results of testing Hypothesis 1 based on the simple task. The first row establishes that, in the absence of DQI, novices and experts arrive at similar results when performing the simple task. The nonsignificant chi-square statistics imply that the two groups chose the same alternative and did not differ in their level of consensus. Finally, the significant correlation for consistency suggests that the overall rankings given to the sets of alternatives by the novices and experts were essentially the same.

Figure 2 (A) Complacency of Novices; (B) Noncomplacency of Experts  
![](/api/attachments/VEMY8BDK/fulltext/images/e9b58a20e3bb9f79310cf4373b3de92508fddc892822c5433dcd3896b98c24cf.jpg)  
(a)  
Information Systems Research/Vol. 14, No. 2, June 2003

Table 2 Simple Task: Novices Versus Experts

<table><tr><td>ComparisonGroups</td><td>SampleSizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>Novices (no DQI)*</td><td>38</td><td rowspan="2"> $\chi^{2} = 0.4$ (ns)</td><td rowspan="2"> $\chi^{2} = 0.4$ (ns)</td><td rowspan="2">Corr = 0.98(p&lt; 0.05)</td></tr><tr><td>Experts (no DQI)</td><td>20</td></tr><tr><td>Novices (no DQI)</td><td>38</td><td rowspan="2"> $\chi^{2} = 1$ (ns)</td><td rowspan="2"> $\chi^{2} = 1$ (ns)</td><td rowspan="2">Corr = 0.99(p&lt; 0.01)</td></tr><tr><td>Novices (DQI)</td><td>42</td></tr><tr><td>Experts (no DQI)</td><td>20</td><td rowspan="2"> $\chi^{2} = 10.9$ (p&lt; 0.01)</td><td rowspan="2"> $\chi^{2} = 5.4$ (p&lt; 0.05)</td><td rowspan="2">Corr = 0.94(ns)</td></tr><tr><td>Experts (DQI)</td><td>18</td></tr></table>

Note. ∗Technically this is not a complacency measure because neither group had DQI.

The complacency and consistency statistics in the second and third rows show that novices did not use the DQI information in making the apartment selection, while the experts did use the DQI. For a graphical comparison of the complacency of novices versus the noncomplacency of experts, please see Figures 2A and 2B. The first column in each set indicates how many people in that set chose Apartment B as their first choice, while the second column in each set indicates how many people chose one of the other apartments, A, C, or D. The first choice for novices with or without DQI was Apartment B (see Figure 2A). Recall that if DQI was given, Apartment B should not be the right choice. Figure 2B shows that the experts switched from Apartment B to a different apartment when provided with DQI.

![](/api/attachments/VEMY8BDK/fulltext/images/a2f19785a9989d993d9c863f7f236cf68bcdbbaafaeb5d5d755f3e863007ece3.jpg)

The novices were consistent, as the overall rankings with and without DQI differed only slightly, as shown by the correlations of 0.99 in Table 2. The experts were not consistent, as the overall ranks were affected, shown by a nonsignificant correlation. Their consensus levels also changed and by reviewing the choices made by the experts we found that there was not as high agreement on the top choice with DQI as there was without DQI.

Table 2 established the behavior of novices and experts with and without DQI. Next we were interested in directly comparing novices to experts when each group was provided with DQI. Using novices as the basis for comparison (the “expected” group) yielded a significant chi-square statistic of 3.5 $( p < 0 . 0 1 )$ . Thus, these two groups made different top choices in the presence of DQI. In combination with the results in Table 2, we concluded that experts used the DQI whereas novices did not.

In the second experiment, experienced professionals performed a complex task. Table 3 shows the chi-square value for complacency, comparing the proportions of experts who chose Job B vs. other choices, was $\chi ^ { 2 } = 5 6 2 .$ $p = 0$ (Row 1). The nonsignificant correlation between the rankings indicate that DQI caused a change (low consistency) in the rankings. The results provide evidence that experienced professionals use DQI on a complex task.

However, the large consensus chi-square value, $\chi ^ { 2 } = 3 4 4$ , indicate that there was a large difference in the amount of agreement among the experts with

Table 3 Complex Task: Expert Usage and Years of Experience

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>Experts (no DQI)</td><td>35</td><td rowspan="2"> $\chi^2=562$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=344$ (p&lt;0.001)</td><td rowspan="2">Corr=0.64(ns)</td></tr><tr><td>Experts (DQI)</td><td>34</td></tr><tr><td>LE 10 years (no DQI)</td><td>18</td><td rowspan="2"> $\chi^2=0$ (ns)</td><td rowspan="2"> $\chi^2=0$ (ns)</td><td rowspan="2">Corr=0.97(p&lt;0.01)</td></tr><tr><td>GT 10 years (no DQI)*</td><td>17</td></tr><tr><td>LE 10 years (no DQI)</td><td>18</td><td rowspan="2"> $\chi^2=36.7$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=113$ (p&lt;0.001)</td><td rowspan="2">Corr=0.51(ns)</td></tr><tr><td>LE 10 years (DQI)</td><td>17</td></tr><tr><td>GT 10 years (no DQI)</td><td>17</td><td rowspan="2"> $\chi^2=40.8$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=56$ (p&lt;0.001)</td><td rowspan="2">Corr=0.73(ns)</td></tr><tr><td>GT 10 years (DQI)</td><td>17</td></tr></table>

Note. ∗Technically this is not a complacency measure because neither group had DQI.

Figure 3 Noncomplacency of Experts on the Complex Task  
![](/api/attachments/VEMY8BDK/fulltext/images/2988c1239d051179b6b37aa867fa59150ea4e8bb98fc09463606601a2bea10cd.jpg)

DQI and those without DQI. Figure 3 displays these proportions graphically. An examination of the two columns in Figure 3 for the group without DQI indicates that an overwhelming proportion of people chose Job B, and with DQI a large proportion of people chose something other than Job B.

We used the responses to the posttask questionnaire to categorize the IS professionals into two groups according to their years of experience. We used 10 years as a cutoff for those with less experience and those with more experience; this created roughly equal-size groups. The second row in Table 3 compares the results of the two groups without DQI and we find no difference in their responses, confirming that in the absence of DQI the ranking of alternatives do not change with length of experience. Rows 3 and 4 show that providing DQI did impact the rankings based on significant chi-square statistics for complacency and nonsignificant correlations for consistency. However, the significant chi-square statistics for consensus were determined to be due to a decrease in consensus when the subjects were provided with DQI.

As before, we directly compared the top choices made by the groups with the two levels of experience when both were provided with DQI. We obtained a nonsignificant chi-square statistic and concluded that the relatively less experienced subjects (in terms of number of years working), used DQI as effectively as the more experienced subjects. Figure 4 provides visual confirmation that the people with greater than 10 years of experience made equivalent choices to those with less than or equal to 10 years experience.

Instead of simply the number of years of experience, the type of experience may be a factor in determining effective use of DQI. Hence, we used the posttask questionnaire again to create two categories of experts, those with management experience and those without. The first row in Table 4 demonstrates that the two groups reacted similarly to the complex task when no DQI was presented. The second and third rows show that both managers and nonmanagers were noncomplacent. The managers had less complacency and less consistency than nonmanagers, but also had less consensus. A comparison of the chisquared values for complacency and the lower correlation values for consistency from Table 4 show that managers made more use of the DQI. A direct comparison of the top choices made by managers and nonmanagers when both groups were provided with DQI yielded a chi-square statistic of 3.89 $( p < 0 . 1 )$ Thus we conclude that management experience was a significant factor in the use of DQI.

Figure 4 Complacency when “Years Working” Is Varied  
![](/api/attachments/VEMY8BDK/fulltext/images/78b6a20c559a0b38d9c3a88a920ef73902e5a1116b70d58b1310a8df9adc95d1.jpg)

To test the effect of domain-specific experience, we categorized the IS professionals, using the posttask questionnaire, into two groups: Those who experienced a job transfer requiring a household move (domain-specific experience) and those who did not (no domain-specific experience). Using domainspecific experience as our independent variable, we investigated the impact of providing DQI to these two groups.

Table 4 Complex Task: Type of Experience—Managerial

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>Manager (no DQI)</td><td>23</td><td rowspan="2"> $\chi^2=2.09$ (ns)</td><td rowspan="2"> $\chi^2=2.09$ (ns)</td><td rowspan="2">Corr=0.98(p&lt;0.01)</td></tr><tr><td>Nonmanager (no DQI)*</td><td>12</td></tr><tr><td>Manager (no DQI)</td><td>23</td><td rowspan="2"> $\chi^2=107$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=101$ (p&lt;0.001)</td><td rowspan="2">Corr=0.51(ns)</td></tr><tr><td>Manager (DQI)</td><td>17</td></tr><tr><td>Nonmanager (no DQI)</td><td>12</td><td rowspan="2"> $\chi^2=12.6$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=56.7$ (p&lt;0.001)</td><td rowspan="2">Corr=0.67(ns)</td></tr><tr><td>Nonmanager (DQI)</td><td>17</td></tr></table>

Note. ∗Technically this is not a complacency measure because neither group had DQI.

The first row in Table 5 shows that without DQI, subjects ranked the same alternative as their top choice (nonsignificant chi-square) and their overall rankings of the alternatives were essentially the same (high correlation of 0.99). This verifies that any subsequent differences we find are attributable to differences in the levels of domain-specific experience.

When the two groups were provided with DQI, there was a significant shift in the top choice as well as a change in the consensus levels. The highly significant chi-square statistics for complacency in the last two rows show that when considering subjects without specific experience with job transfers or those with specific experience, in both cases the subjects pay close attention to the DQI. The consensus statistics are also significant, and by examining the raw data we found that in each case they represent a lowering of consensus. The consistency statistics are considerably lower, representing a change in the overall ranks assigned, again illustrating the impact of providing DQI.

Table 5 Complex Task: Domain-Specific Experience

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>No spec exp (no DQI)</td><td>25</td><td rowspan="2"> $\chi^2=0.9$ (ns)</td><td rowspan="2"> $\chi^2=0.9$ (ns)</td><td rowspan="2">Corr= 0.99(p&lt; 0.01)</td></tr><tr><td>Spec exp (no DQI)*</td><td>10</td></tr><tr><td>No spec exp (no DQI)</td><td>25</td><td rowspan="2"> $\chi^2=143$ (p&lt; 0.001)</td><td rowspan="2"> $\chi^2=143$ (p&lt; 0.05)</td><td rowspan="2">Corr= 0.72(ns)</td></tr><tr><td>No spec exp (DQI)</td><td>19</td></tr><tr><td>Spec exp (no DQI)</td><td>10</td><td rowspan="2"> $\chi^2=89$ (p&lt; 0.001)</td><td rowspan="2"> $\chi^2=10.3$ (p&lt; 0.001)</td><td rowspan="2">Corr= 0.45(ns)</td></tr><tr><td>Spec exp (DQI)</td><td>14</td></tr></table>

Note. ∗Technically this is not a complacency measure because neither group had DQI.

We followed up by directly comparing top choices made by the two groups, those with and without domain-specific experience, when both are provided with DQI. We obtained a chi-square statistic of 4.4 $( p < 0 . 0 5 )$ , which shows that the two groups do indeed differ in their use of DQI. This, coupled with the larger chi-squared statistic for complacency $( \chi ^ { 2 } = 1 4 3 )$ for those who do not have domain-specific experience, shows that that group made more use of DQI. We examine the implications of this and other, related findings in subsequent sections.

## Time

Having established the effect of experience, we now investigate each category of subjects in different time constraints. First we present the results for the novices performing the simple task, followed by the experts performing the same simple task, and then show the results for the experts performing the complex task in Experiment 2. Completion times for the tasks were recorded and the results indicated that the subjects generally used the full time allotted to them.

For the simple task, we see from Table 6 that the novices were complacent, regardless of the time constraints. Novices reached consensus. The novices were generally consistent in their overall rankings, indicating that time constraints did not have an influence on the rankings.

The first two rows of Table 7 show that the experts were not complacent in the presence of DQI when performing the simple task. We see that the experts also were not consistent in their overall rankings. There was no change in the consensus levels between the experts in the short time-constraint group, but there was a significant change (actually a decrease) in the consensus levels between the experts in the long time-constraint group. A direct comparison of the top choices made by the experts in the short and long time-constraint groups in a follow-up test found a nonsignificant chi-square statistic. Hence, we conclude that time constraints were not a factor in the use of DQI by experts on a simple task.

Table 6 Simple Task: Novices

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>Short (no DQI)</td><td>16</td><td rowspan="2"> $\chi^2=1.3$ (ns)</td><td rowspan="2"> $\chi^2=1.3$ (ns)</td><td rowspan="2">Corr=0.98(p&lt;0.05)</td></tr><tr><td>Short (DQI)</td><td>20</td></tr><tr><td>Long (no DQI)</td><td>22</td><td rowspan="2"> $\chi^2=0.18$ (ns)</td><td rowspan="2"> $\chi^2=0.18$ (ns)</td><td rowspan="2">Corr=0.99(p&lt;0.01)</td></tr><tr><td>Long (DQI)</td><td>22</td></tr></table>

Table 7 Simple and Complex Tasks: Experts

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td><td>Task</td></tr><tr><td>Short (no DQI)</td><td>10</td><td> $\chi^2=3.6$ </td><td> $\chi^2=1.6$ </td><td>Corr=0.88</td><td>Simple</td></tr><tr><td>Short (DQI)</td><td>10</td><td>(p&lt;0.10)</td><td>(ns)</td><td>(ns)</td><td></td></tr><tr><td>Long (no DQI)</td><td>10</td><td> $\chi^2=9.0$ </td><td> $\chi^2=4.5$ </td><td>Corr=0.85</td><td>Simple</td></tr><tr><td>Long (DQI)</td><td>8</td><td>(p&lt;0.01)</td><td>(p&lt;0.05)</td><td>(ns)</td><td></td></tr><tr><td>Short (no DQI)</td><td>12</td><td> $\chi^2=57$ </td><td> $\chi^2=7.4$ </td><td>Corr=0.63</td><td>Complex</td></tr><tr><td>Short (DQI)</td><td>9</td><td>(p&lt;0.001)</td><td>(p&lt;0.01)</td><td>(ns)</td><td></td></tr><tr><td>Medium (no DQI)</td><td>12</td><td> $\chi^2=49$ </td><td> $\chi^2=48$ </td><td>Corr=0.77</td><td>Complex</td></tr><tr><td>Medium (DQI)</td><td>11</td><td>(p&lt;0.001)</td><td>(p&lt;0.001)</td><td>(p&lt;0.05)</td><td></td></tr><tr><td>Long (no DQI)</td><td>11</td><td> $\chi^2=73$ </td><td> $\chi^2=57$ </td><td>Corr=0.45</td><td>Complex</td></tr><tr><td>Long (DQI)</td><td>14</td><td>(p&lt;0.001)</td><td>(p&lt;0.001)</td><td>(ns)</td><td></td></tr></table>

Based on the last three rows of Table 7, we see that for the complex task, DQI had strong effects in each of the time-constraint groups. In all comparisons between groups with and without DQI there was a decrease in consensus, regardless of the time constraint. Clearly, DQI was the critical factor, rather than time-constraint grouping, for both the simple and complex tasks.

Next we explored the effects of perceptions of time pressure rather than time constraint. The posttask questionnaire allowed us to identify the groups that felt time pressure (see Question 32, Appendix B), an issue for the complex but not the simple task. Figure 5 shows that there is a relationship between assignments to time-constrained groups and feelings of time pressure. However, it also shows that people may be in a short time group and not feel pressure, while others may be in a long time group and feel pressure.

Figure 5 Perception of Time Pressure Within Time Constraints Pressure byConstraint <sub>Pressu</sub>  
![](/api/attachments/VEMY8BDK/fulltext/images/5fd4e61c8ee04c6228a1f861c312c49e0b4cad9fe28f39895e63d7fd8d21bbdc.jpg)

As seen in Table 8, the feeling of time pressure had more impact on the results than did a particular time-constraint group. The first row shows that the groups with and without time pressure behaved similarly when no DQI was available. However, when DQI was available there were differences. Whether or not subjects felt time pressure, they were noncomplacent, but also had difficulty coming to a consensus. A direct comparison of the top choices made by the groups who felt time pressure and those who did not yielded a chi-square of 9.7 $( p < 0 . 0 0 5 )$ when both groups were provided with DQI. This, coupled with the larger chi-square for complacency for the group who felt time pressure, shows that those with DQI while under time pressure made the most use of the available DQI. Time pressure was found to affect the overall ranks as well.

## Demographic Variables

Using categories based on the posttask questionnaire for the complex task, we continued to explore the degree of complacency based on age, education, and gender. Both male and female experts were not complacent to DQI. We found no differences between males and females when using DQI, as shown by a nonsignificant $\chi ^ { 2 } = 0 . 2 3$ . We found some difference based on age. The younger (aged 30 or below) group complacency measure had a $\chi ^ { 2 } = 1 2$ , while the greater than age 30 group had a $\chi ^ { 2 } = 3 6 7$ . A direct comparison of the two groups yielded a $\chi ^ { 2 } = 6 . 8$ with $p < 0 . 0 0 5 .$

Table 8 Time Pressure (Experts—Complex Task)

<table><tr><td>Comparison Groups</td><td>Sample Sizes</td><td>Complacency</td><td>Consensus</td><td>Consistency</td></tr><tr><td>Time pressure (no DQI)</td><td>14</td><td rowspan="2"> $\chi^2=0.22$ (ns)</td><td rowspan="2"> $\chi^2=0.22$ (ns)</td><td rowspan="2">Corr=0.97(p&lt;0.01)</td></tr><tr><td>No time pressure(no DQI)*</td><td>22</td></tr><tr><td>Time pressure (no DQI)</td><td>14</td><td rowspan="2"> $\chi^2=157$ (p&lt;0.001)</td><td rowspan="2"> $\chi^2=63$ (p&lt;0.001)</td><td rowspan="2">Corr=0.3(ns)</td></tr><tr><td>Time pressure (DQI)</td><td>18</td></tr><tr><td>No time pressure(no DQI)</td><td>22</td><td> $\chi^2=86$ </td><td> $\chi^2=0.82$ </td><td rowspan="2">Corr=0.89(p&lt;0.01)</td></tr><tr><td>No time pressure (DQI)</td><td>15</td><td>(p&lt;0.001)</td><td>(p&lt;0.001)</td></tr></table>

Note. ∗Technically this is not a complacency measure because neither group had DQI.

Finally, education was a factor. The high-schoolonly graduates had the lowest noncomplacency at $\chi ^ { 2 } = 7 ~ ( p < 0 . 0 5 )$ , the master’s degree subjects had the next level of non-complacency at $\chi ^ { 2 } = 2 3 . 4 \ ( p < 0 . 0 0 5 )$ and the bachelor’s degree subjects had the highest degree of noncomplacency at $\chi ^ { 2 } = 2 3 1 \ ( p < 0 . 0 0 0 1 )$ This leads to the conclusion that college graduates made more use of DQI than high school graduates or postgraduates, even though all were experienced professionals in the business world.

## Discussion

Because incorporating DQI into a database is both time consuming and expensive, it is important to know the characteristics of users who would benefit from having access to such. Our experiments lead us to some preliminary conclusions.

## Experience

The results from the experiments provide strong evidence that experts use DQI substantially more than do novices. For the simple task in Experiment 1, experts used the DQI and novices ignored the DQI. For the complex task in Experiment 2, the chi-square statistics are indicative of near certainty that DQI influenced the decision making of experts. However, there was not much difference in the use of DQI based on general level of experience when measured by number of years. However, when we categorized the professionals by type of experience, we found that managers were more likely to use DQI, as compared to nonmanagers. This has implications for data warehouses that are designed to support ad hoc decision making.

While managerial experience increased use of DQI, domain experience did not increase use of DQI. Those without domain-specific experience made more use (were less complacent) and better use (had more consensus) of DQI than did those with domain-specific experience. These findings suggest that domainspecific experience may inhibit the use of DQI in decision making. This is consistent with past studies (Gilliland et al. 1994, Yates 1991). Our findings indicate that DQI would be most useful for managers who have little domain-specific experience.

Chengalur-Smith et al. (1999) performed a study using college seniors to perform a simple apartment selection task and a complex restaurant selection task. The college seniors can be said to have an intermediate level of experience—more experience than the current study’s freshmen but less experience than the MIS professionals. That study found that for the college seniors “complacency varied dramatically across the research design” (Chengalur-Smith et al. 1999) and that the seniors were not complacent on the simple task but were complacent on the complex task. Our study found novices were completely complacent to DQI, while experts were not complacent on any tasks. An emerging pattern indicates increasing usage of DQI when experience progresses through the stages defined as novice, intermediate, and professional.

The knowledge gained from these findings could be used to guide the selection of people for training in the use of DQI within an organization. As a person progresses from novice status to an experienced professional, there is most likely some cutoff point at which he or she begins to pay attention to DQI. However, if one considers complacency only, one might wrongly conclude that people who are beyond the cutoff point might not benefit from training in the use of DQI.

While complacency illustrates that DQI influences decision making of experts, the consensus measures show that experts do not use DQI in the same way; that is, experts who use DQI will make a variety of choices for the first choice. The consensus chi-squared statistics in most cases showed a decline in consensus when DQI was considered. It may not be desirable for an organization to have a situation where different people make different decisions based upon the same data. For an example of lack of consensus that also brings in the concept of domain-specific experience vs. general experience and time pressure, see the USS Vincennes Case (Fisher and Kingma 2001). Because DQI is such a new concept, we feel that training and/or planning sessions concerning the use of DQI by experts may be very worthwhile.

## Time

Two facets of time were considered. The first was time constraint, in which people were put into groups that were allotted a fixed amount of time to complete the tasks. The second facet of time was time pressure, which reflects how people felt about the time they are given to complete a task. Some people in the long time-constraint group felt time pressure, while others in the short time-constraint group did not feel time pressure.

The simple task, when performed by experts given a short time period, led to general consensus. However, providing DQI along with a large amount of time to perform the simple task led to divergent choices or a decrease in consensus. The experts generally were not complacent in the presence of DQI, but time constraints were not a factor for the experts performing the complex task. We found no differences based on actual time constraints, but our data revealed that perceived time pressure did make a difference. Based on self-reports of time pressure, providing DQI led to significant differences in the decision choices between those who experienced time pressure and those who did not. Our data indicates that decision makers who feel time pressure would benefit from having DQI available, as the availability of DQI has a stronger impact on their decisions than for those who do not feel time pressure. This has implications for those who need to make decisions in crisis-type environments (Fisher and Kingma 2001).

## Demographics

From the posttask questionnaire we collected information about gender, age, and education of the subjects in an attempt to find what effect, if any, these demographic characteristics might have on the subjects’ reaction to DQI. Among the experts performing the complex task, we found that age was a factor. We found that both the older and younger groups used DQI, but the degree of noncomplacency was much greater in the older group as compared to the younger group, revealing that older people paid more attention to DQI than younger people.

Among the IS professionals (experts) performing the complex task, education was a factor. Again, based on the questionnaire, we created three post hoc groups. All three education levels considered (high school, bachelor’s degree, and master’s degree) were not complacent. Interestingly, the level of noncomplacency was the lowest for the high-school-only graduates and the highest for the bachelor’s degree subjects. The higher chi-square for those with bachelor’s degrees as compared to the group with master’s degrees could indicate that those with a more generalized background would use DQI more and use it more effectively. This is consistent with the greater use of DQI by managers as opposed to specialists.

## Future Research and Concluding Remarks

At this point we are still investigating whether a decision maker will use DQI or not, and under what conditions. Further work needs to be done to determine if there is in fact a correct way to use DQI. How the DQI should be defined and weighted are key questions and may vary among organizations and problem types. Hence, actual case studies would contribute much to this area. This should be followed up with research on format of DQI for different types of problems. DQI may be formatted as numeric interval data between 0 and 1, as we have done. Alternatively it may be formatted as ordinal data with values such as good, poor, and so forth. It is well known that there are many decision processing strategies with two major categories, compensatory and cutoff (Payne et al. 1993). If cutoff techniques are used with DQI, that may significantly change the relative weight of the DQI; i.e., an alternative with the word “poor” listed as the DQI for one of its attributes may be rejected, whereas it would not have been rejected with interval data and compensatory techniques. This may advise database designers as to the desirability of using one or the other format.

Note that in our study we did not constrain the subjects to using a particular decision-making strategy. Through the posttask questionnaire we attempted to discern the strategy that was used, but found that most subjects used a combination of strategies. Although the focus of this study was whether DQI was used, future research might investigate the issue of how DQI is used when it is used.

Although the idea of incorporating data tags into databases is not new, it is not clear under what circumstances it would be most beneficial. Based on our findings, DQI should be incorporated into those data sets used by management. A direct comparison of those with management and nonmanagement backgrounds showed that the former were more influenced by DQI than were the latter. This is consistent with the finding that those without domain-specific experience used DQI more than those with domainspecific experience. This agrees with the earlier findings that too much domain-specific experience may prevent objective use of all available information (Gilliland et al. 1994, Yates 1991). One could hypothesize that those with the most experience regarding a situation, although they may indeed use DQI, are not as influenced by it on account of prior experience with the issue and similar data. The overall conclusion is that DQI should be made available to management not as familiar with the problem at hand.

Organizations wishing to begin a program of using DQI should be aware of the fact that there was a lack of consensus when experts were presented with DQI. The lack of complacency and consistency among the experts is deemed to be positive as it illustrates that the experts will use the DQI. However, the lower than expected consensus levels indicate that the experts used the DQI differently. We can predict that the addition of information about data quality to a database is likely to change the decision made, but we cannot predict what that new decision may be. Simply put, different experts, given a common task with the same data quality information, reached different decisions. It would be extremely beneficial for organizations to conduct seminars and DQI education prior to beginning a reliance on DQI if the organizations expect to have consensus in their decision making.

## Appendix A. The Job Transfer Task Description<sup>1</sup>

J. Doe’s job is being downsized and his company is allowing him to transfer to one of seven jobs. Unfortunately, J. Doe is sick on the day that he is supposed to submit his choices in order of preference. At a previous time J. Doe began the decision process of examining the jobs. First he identified nine characteristics and indicated which characteristics were most important to him. He reflected these in weights from 1 (most important) to 0.2 (least important). Next he rated each job as to the attractiveness of each individual characteristic on a 100-point scale, where the higher number is more desirable. For example, a rating of 90 for job content is more desirable than a rating of 25. Finally, he multiplied the weight times the ratings to obtain a weighted score for each job characteristic for each job. However, because he became ill, he was unable to finish ranking the jobs. He asked you to review his work and submit his choices ranked in order of preference from the most desirable job (Rank 1) to the least desirable job (Rank 7).

The job characteristics<sup>2</sup> and preferences are: J. Doe’s number one priority is job security because, due to his health, he cannot risk losing his job and benefits. His second highest priority is to maintain his current salary. His third priority is school quality. J. Doe hopes to obtain a job that he likes, thus his fourth priority is job content. His

<table><tr><td colspan="5">Job Alternative A</td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td><td>Weighted Scores</td></tr><tr><td>JOB CONTENT</td><td>0.8</td><td>84</td><td>0.7</td><td>58.8</td></tr><tr><td>CAREER GROWTH</td><td></td><td>24</td><td>0.3</td><td>7.2</td></tr><tr><td>CURRENT SALARY</td><td>0.8</td><td>80</td><td>0.9</td><td>72</td></tr><tr><td>FUTURE SALARY</td><td></td><td>16</td><td>0.5</td><td>8</td></tr><tr><td>LOCATION</td><td></td><td>56</td><td>0.4</td><td>22.4</td></tr><tr><td>CLIMATE</td><td></td><td>50</td><td>0.6</td><td>30</td></tr><tr><td>JOB SECURITY</td><td>0.5</td><td>54</td><td>1</td><td>54</td></tr><tr><td>SCHOOL QUALITY</td><td>1</td><td>42</td><td>0.8</td><td>33.6</td></tr><tr><td>COST OF LIVING</td><td></td><td>22</td><td>0.2</td><td>4.4</td></tr><tr><td colspan="5">Job Alternative B</td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td><td>Weighted Scores</td></tr><tr><td>JOB CONTENT</td><td>0.2</td><td>90</td><td>0.7</td><td>63</td></tr><tr><td>CAREER GROWTH</td><td></td><td>84</td><td>0.3</td><td>12.6</td></tr><tr><td>CURRENT SALARY</td><td>0.7</td><td>70</td><td>0.9</td><td>63</td></tr><tr><td>FUTURE SALARY</td><td></td><td>82</td><td>0.5</td><td>41</td></tr><tr><td>LOCATION</td><td></td><td>60</td><td>0.4</td><td>24</td></tr><tr><td>CLIMATE</td><td></td><td>68</td><td>0.6</td><td>40.8</td></tr><tr><td>JOB SECURITY</td><td>0.2</td><td>90</td><td>1</td><td>90</td></tr><tr><td>SCHOOL QUALITY</td><td>0.2</td><td>80</td><td>0.8</td><td>64</td></tr><tr><td>COST OF LIVING</td><td></td><td>50</td><td>0.2</td><td>10</td></tr><tr><td colspan="5">Job Alternative C</td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td><td>Weighted Scores</td></tr><tr><td>JOB CONTENT</td><td>0.7</td><td>50</td><td>0.7</td><td>35</td></tr><tr><td>CAREER GROWTH</td><td></td><td>20</td><td>0.3</td><td>6</td></tr><tr><td>CURRENT SALARY</td><td>0.8</td><td>16</td><td>0.9</td><td>14.4</td></tr><tr><td>FUTURE SALARY</td><td></td><td>48</td><td>0.5</td><td>24</td></tr><tr><td>LOCATION</td><td></td><td>30</td><td>0.4</td><td>12</td></tr><tr><td>CLIMATE</td><td></td><td>32</td><td>0.6</td><td>19.2</td></tr><tr><td>JOB SECURITY</td><td>0.8</td><td>24</td><td>1</td><td>24</td></tr><tr><td>SCHOOL QUALITY</td><td>1</td><td>20</td><td>0.8</td><td>16</td></tr><tr><td>COST OF LIVING</td><td></td><td>60</td><td>0.2</td><td>12</td></tr></table>

<sup>1</sup>This task was developed by drawing on one of the author’s experiences with job transfers and physical relocations as a middlelevel manager at a major computer company. Additionally, four other professionals with varied experience were interviewed to determine the criteria for a relocation decision. They included a retired professional who is now an information systems consultant, a director of career services at a small college, a management consultant (team productivity), and a corporation quality manager. A Delphi process led to the final set of nine attributes for the “job transfer task.”

<sup>2</sup>The job characteristics are indicated in italic letters.

<table><tr><td colspan="6">Job Alternative D</td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td><td>Weighted Scores</td><td></td></tr><tr><td>JOB CONTENT</td><td>0.8</td><td>30</td><td>0.7</td><td>21</td><td rowspan="9"><img src="/api/attachments/VEMY8BDK/fulltext/images/5802c558ecbbeacdd1b513b62e87ffbef93dc785a0552cf6f10757b4815c38a8.jpg"/></td></tr><tr><td>CAREER GROWTH</td><td></td><td>52</td><td>0.3</td><td>15.6</td></tr><tr><td>CURRENT SALARY</td><td>0.6</td><td>48</td><td>0.9</td><td>43.2</td></tr><tr><td>FUTURE SALARY</td><td></td><td>54</td><td>0.5</td><td>27</td></tr><tr><td>LOCATION</td><td></td><td>26</td><td>0.4</td><td>10.4</td></tr><tr><td>CLIMATE</td><td></td><td>54</td><td>0.6</td><td>32.4</td></tr><tr><td>JOB SECURITY</td><td>0.8</td><td>80</td><td>1</td><td>80</td></tr><tr><td>SCHOOL QUALITY</td><td>0.8</td><td>30</td><td>0.8</td><td>24</td></tr><tr><td>COST OF LIVING</td><td></td><td>52</td><td>0.2</td><td>10.4</td></tr><tr><td colspan="4">Job Alternative E</td><td rowspan="2">Weighted Scores</td><td rowspan="2"></td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td></tr><tr><td>JOB CONTENT</td><td>0.8</td><td>50</td><td>0.7</td><td>35</td><td rowspan="9"><img src="/api/attachments/VEMY8BDK/fulltext/images/ffc7c0a5aa1a1948220f1be72719622013c039d7c943a4dc195808fb05243fda.jpg"/></td></tr><tr><td>CAREER GROWTH</td><td></td><td>76</td><td>0.3</td><td>22.8</td></tr><tr><td>CURRENT SALARY</td><td>0.7</td><td>24</td><td>0.9</td><td>21.6</td></tr><tr><td>FUTURE SALARY</td><td></td><td>30</td><td>0.5</td><td>15</td></tr><tr><td>LOCATION</td><td></td><td>56</td><td>0.4</td><td>22.4</td></tr><tr><td>CLIMATE</td><td></td><td>44</td><td>0.6</td><td>26.4</td></tr><tr><td>JOB SECURITY</td><td>0.8</td><td>18</td><td>1</td><td>18</td></tr><tr><td>SCHOOL QUALITY</td><td>1</td><td>48</td><td>0.8</td><td>38.4</td></tr><tr><td>COST OF LIVING</td><td></td><td>56</td><td>0.2</td><td>11.2</td></tr><tr><td colspan="4">Job Alternative F</td><td rowspan="2">Weighted Scores</td><td rowspan="2"></td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td></tr><tr><td>JOB CONTENT</td><td>0.2</td><td>30</td><td>0.7</td><td>21</td><td rowspan="9"><img src="/api/attachments/VEMY8BDK/fulltext/images/5672a4d750e74f3d61df7ead770beb2cedea363cec9aabe9cea825e815e56fa8.jpg"/></td></tr><tr><td>CAREER GROWTH</td><td></td><td>24</td><td>0.3</td><td>7.2</td></tr><tr><td>CURRENT SALARY</td><td>0.8</td><td>18</td><td>0.9</td><td>32.4</td></tr><tr><td>FUTURE SALARY</td><td></td><td>20</td><td>0.5</td><td>10</td></tr><tr><td>LOCATION</td><td></td><td>56</td><td>0.4</td><td>22.4</td></tr><tr><td>CLIMATE</td><td></td><td>18</td><td>0.6</td><td>10.8</td></tr><tr><td>5 JOB SECURITY</td><td>0.5</td><td>82</td><td>1</td><td>82</td></tr><tr><td>SCHOOL QUALITY</td><td>0.2</td><td>72</td><td>0.8</td><td>57.6</td></tr><tr><td>COST OF LIVING</td><td></td><td>44</td><td>0.2</td><td>8.8</td></tr><tr><td colspan="4">Job Alternative G</td><td rowspan="2">Weighted Scores</td><td rowspan="2"></td></tr><tr><td>Criterion</td><td>Reliability</td><td>Rating</td><td>Weight</td></tr><tr><td>JOB CONTENT</td><td>0.8</td><td>50</td><td>0.7</td><td>35</td><td rowspan="9"><img src="/api/attachments/VEMY8BDK/fulltext/images/565ddfbf66c15e10a004f421d4f0e112ef6c21769ce9795de59f5fa3b7cd5433.jpg"/></td></tr><tr><td>CAREER GROWTH</td><td></td><td>90</td><td>0.3</td><td>27</td></tr><tr><td>CURRENT SALARY</td><td>1</td><td>82</td><td>0.9</td><td>73.8</td></tr><tr><td>FUTURE SALARY</td><td></td><td>60</td><td>0.5</td><td>30</td></tr><tr><td>LOCATION</td><td></td><td>24</td><td>0.4</td><td>9.6</td></tr><tr><td>CLIMATE</td><td></td><td>64</td><td>0.6</td><td>38.4</td></tr><tr><td>JOB SECURITY</td><td>0.8</td><td>52</td><td>1</td><td>52</td></tr><tr><td>SCHOOL QUALITY</td><td>0.8</td><td>48</td><td>0.8</td><td>38.4</td></tr><tr><td>COST OF LIVING</td><td></td><td>22</td><td>0.2</td><td>4.4</td></tr></table>

fifth priority is to avoid a colder climate. He is moderately interested in salary increases or future salary. Whatever his new location is he would like to minimize a commute to work. He is not interested in career growth opportunities. His last priority is cost of living since he has acquired most things he needs and can avoid unnecessary expenses.

Information Systems Research/Vol. 14, No. 2, June 2003

The relative weights for these characteristics (criterion weights) are: Job content 07; career growth 03; current salary 09; future salary 05; location 04; climate 06; job security 1; school quality <sub>=</sub> 08; and cost of living <sub>=</sub> 02. The job alternatives from A to G with the criterion weights, ratings, and weighted scores (weight <sub>×</sub> rating) are shown on the next two pages.

Your task is to rank the jobs to meet J. Doe’s needs given his weights and ratings. Rank the jobs from 1, being the best choice, to 7 being the last choice. However, you realize that the data he obtained may not be completely accurate. For instance, his information on job content came from someone who never worked at the new locations. Also, job security current and future salary, and career growth, are dependent on a volatile market. School quality information may be unreliable if presented by real estate people only interested in selling particular houses. Location commute time may be based on single trips at 2 pm at some locations but on many trips during rush hour at other locations. The reliability of the information about the job characteristics came from different sources and may vary from job to job.

You decide to incorporate this uncertainty into your decisionmaking process by using a 0-1 reliability measure where a score of 1 indicates perfectly reliable data and 0 scores imply completely unreliable data. You were only able to estimate reliability for four of the nine criteria.

The job alternatives from A to G with the criterion weights, ratings, and weighted scores (weight X rating) are shown on the next two pages. In addition, you have included a “reliability” column to indicate the 0-1 reliability measure for each criterion for each alternative. Remember that reliability refers to the data and not to the weights. Next to each job description write its rank, along with a brief explanation of exactly how you arrived at the rank.

## Appendix B. Post Questionnaire<sup>3</sup>

Number:

The following information will not be used to identify individuals in any way. Information is recorded based on the random number assigned to your questionnaire. No attempt will be made to correlate these random numbers with any actual identity.

1. Female Male

2. My Education is: (Please indicate the highest level that you have achieved) High School Bachelors Degree Masters Degree Post Masters Degree (Specify:

3. My Occupation may be described as: Professor Professional Educator ; Full time graduate Student ; Engineer ; Programmer Administrative ; Accountant Entrepreneur ; Business Other:

4. My age is 17–20 ; 21–30 ; 31–40 ; 41–50 ; 51–60 ; greater than 60

5. The number of years that I have lived in my own apartments or homes (i.e., not my parents’) is 0 ; 1–5 ; 6–10 ; 11–15 ; 16–20 ; 21–25 ; 26–30 ; greater than 30

6. I am currently a manager or supervisor: Yes ; No

7. I have selected and lived in (how many) apartments or homes.

8. In the apartment selection task what data was most useful to you?

9. In the apartment selection task what data would you like to have had that you did not have?

10. I am confident that my apartment selection choices are correct: Strongly Agree Neither Disagree Strongly Agree Agree/ Disagree Disagree

11. The factors that contribute to my degree of confidence (or lack of) in the apartment selection task are:

12. For the apartment selection task: Did you compare alternatives two at a time and then pick the best one and then compare that one to the next one and so on until only one was left standing?

Always Sometimes Seldom Never

13. For the apartment selection task: Did you focus on single characteristic (attribute) and compare across all alternatives? Always Sometimes Seldom Never

14. For the apartment selection task: Did you tend to compute a sum of all attribute values multiplied by their weights and derive a single score for each alternative? Always Sometimes Seldom Never

15. For the apartment selection task: Did you establish minimal acceptable values for each attribute of each alternative and then see if each alternative, one by one, met that “cutoff?” Always Sometimes Seldom Never

16. For the apartment selection task: Did you use a combination of the above techniques?

Always Sometimes Seldom Never

17. I experienced time pressure to complete the Apartment Selection Task.

Strongly Agree Neither Disagree Strongly Agree Agree/ Disagree Disagree

18. The number of years that I have been a full-time employee is: 0 ; 1–10 ; 11–20 ; 21–30 ; greater than 30

19. In the job relocation task what data was most useful to you?

20. In the job relocation task what data would you like to have had that you did not have?

21. I am confident that my job relocation choices are correct: Strongly Agree Neither Disagree Strongly Agree Agree/ Disagree Disagree

22. The factors that contribute to my degree of confidence (or lack of) are:

23. How many times have you transferred jobs within a location? 0 : 1–3 : 4–6 : 7–9 : 10 or mor

24. How many times have you transferred jobs to a new (e.g., change in commute) that did not require a household move?

25. How many times have you transferred jobs that required a household/apt move?

0 : 1–3 : 4–6 : 7–9 : 10 or more

26. For the job relocation task: Explain the approach that you used in reaching a conclusion. How did you determine the rankings of the alternatives?

27. For the job relocation task: Did you compare alternatives two at a time and then pick the best one and then compare that one to the next one and so on until only one was left standing?

28. For the job relocation task: Did you focus on single characteristic (attribute) and compare across all alternatives? Always Sometimes Seldom Never

29. For the job relocation task: Did you tend to compute a sum of all attribute values multiplied by their weights and derive a single score for each alternative?

30. For the job relocation task: Did you establish minimal acceptable values for each attribute of each alternative and then see if each alternative, one by one, met that “cutoff?” Always Sometimes Seldom Never

31. For the job relocation task: Did you use a combination of the above techniques?

Always Sometimes Seldom Never

32. I experienced time pressure to complete the Job Transfer Task. Strongly Agree Neither Disagree Strongly Agree Agree/ Disagree Disagree

## References

Agarwal, R., V. Sambamurthy, R. M. Stair. 2000. The evolving relationship between general and specific computer self-efficacy— An empirical assessment. Inform. Systems Res. 11(4) 418–430.

Ahituv, N., M. Igbaria, A. Stella. 1998. The effects of time pressure and completeness of information on decision making. J. Management Inform. Systems 15(2) 153–172.

Austin, R. D. 2001. The effects of time pressure on quality in software development: An agency model. Inform. Systems Res. 12(2) 195–207.

Ballou, D. P., H. L. Pazer. 1995. Designing information systems to optimize the accuracy-timeliness tradeoff. Inform. Systems Res. 6(1) 51–72.

, G. Tayi. 1999. Enhancing data quality in data warehouse environments. Comm. ACM 42(1) 54–57.

Chengalur-Smith, I., Pazer, H. 1998. Decision complacency, consensus and consistency in the presence of data quality information. Proc. Conf. Inform. Quality. Cambridge, MA, 88–101.

, D. P. Ballou, H. Pazer. 1997. The impact of data quality tagging on decision complacency. Proc. Conf. Inform. Quality. Cambridge, MA, 209–221.

. 1999. The impact of data quality information on decision making: An exploratory analysis. IEEE Trans. Knowledge and Data Engrg. 11(6) 853–864.

Dukerich, J. M., Mary Lippitt Nichols. 1991. Causal information search in managerial decision making. Organ. Behavior and Human Decision Processes 50 106–122.

Fisher, C. W., 1999. An empirically based exploration of the interaction of time constraints and experience levels on the data quality information (DQI) factor in decision making. Doctoral dissertation, State University of New York at Albany, NY. Dissertation Abstr. Internat. (UMI No. 9954037).

, B. R. Kingma. 2001. Criticality of data quality as exemplified in two disasters. Inform. and Management 39 109–116.

Gilliland, S. W., L. Wood, N. Schmitt. 1994. The effects of alternative labels on decision behavior: The case of corporate site selection decisions. Organ. Behavior and Human Decision Processes 58 406–427.

Grether, D. M., A. Schwartz, L. L. Wilde. 1986. The irrelevance of information overload: An analysis of search and disclosure. Southern California Law Rev. 59 277–303.

Haisten, M. 1995. Planning for a data warehouse. InfoDB (February) 12–21.

Hall, R. H. 1991. Organizations: Structures, Processes and Outcomes. Prentice Hall, Englewood Cliffs, NJ.

Kingma, B. R. 1996. The Economics of Information: A Guide to Economic and Cost-Benefit Analysis for Information Professionals. Libraries Unlimited, Englewood, CO.

Klein, B. D., D. L. Goodhue, G. B. Davis. 1997. Can humans detect errors in data? Impact of base rates, incentives and goals. MIS Quart. 21 169–194.

Mackay, J. M., J. J. Elam. 1992. A comparative study of how experts and novices use a decision aid to solve problems in complex knowledge domains. Inform. Systems Res. 3(2) 150–172.

Mao, J., I. Benbasat. 2000. The use of explanations in knowledgebased systems: Cognitive perspectives and a process-tracing analysis. J. Management Inform. Systems 17(2) 153–179.

March, J. G., H. A. Simon. 1958. Organizations. John Wiley & Sons. New York.

Morrow, D. G., V. O. Leirer, P. A. Altieri. 1992. Aging, expertise, and narrative processing. Psych. Aging 7 376–378.

Ordonez, L., L. Benson III. 1997. Decisions under time pressure: How time constraints affect risky decision making. Organ. Behavior and Human Decision Process 71 121–140.

Paese, P. W., Janet A. Sniezek. 1991. Influences on the appropriateness of confidence in judgment: Practice, effort, information and decision-making. Organ. Behavior and Human Decision Processes 48 100–130.

Payne, J. W., James R. Bettman, Eric J. Johnson. 1993. The Adaptive Decision Maker. Cambridge University Press, Cambridge, MA.

Sanbonmatsu, David M., Frank R. Kardes, Paul M. Herr. 1992. The role of prior knowledge and missing information in multiattribute evaluation. Organ. Behavior and Human Decision Processes 51(1) 76–91.

Shaft, T. M., I. Vessey. 1995. The relevance of application domain knowledge: The case of computer program comprehension. Inform. Systems Res. 6(3) 286–299.

Sheskin, David J. 2000. Handbook of Parametric and Non-parametric Statistical Procedures, 2nd ed. Chapman & Hall, Washington, D.C.

Simon, H. A. 1957. Administrative Behavior: A Study of Decision Making Processes in Administrative Organizations. Collier/ MacMillan, New York.

Svenson, O., A. Edland. 1987. Changes of pressure under time

pressure: Choices and judgments. Scandinavian J. Psych. 28 322–330.

Van Bruggan, G., A. Smidts, B. Wierenga. 1998. Improving decision making by means of a marketing decision support system. Management Sci. 44(5) 645–658.

Wand, Y., Richard Y. Wang. 1996. Anchoring data quality dimensions in ontological foundations. Comm. ACM 39(11) 86–95.

Wang, R. Y., S. E. Madnick. 1990. A Polygon model for hetergeneneous database systems: The source tagging perspective. Proc. 16th Internat. Conf. Very Large Databases. Brisbane, Australia, 519–538.

, D. Strong. 1996. Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems 12 5–34.

, Veda C. Storey, Christopher P. Firth. 1995. A framework for analysis of data quality research. IEEE Trans. Knowledge and Data Engrg. 7(4) 623–639.

Yates, J. F., Linda S. McDaniel, Eric S. Brown. 1991. Probabilistic forecasts of stock prices and earnings: The hazards of nascent expertise. Organ. Behavior and Human Decision Processes 49 60–79.

Zakay, D., S. Wooler. 1984. Time pressure, training, and decision effectiveness. Ergonomics 27 273–284.

Iris Vessey, Associate Editor. This paper was received on September 12, 2002, and was with the authors 6 months for 2 revisions.
